# A2 ENUMERATION LEDGER — Amagi Media Labs Ltd (AMAGI), Q1 FY27 (results)
Source: extract_results_amagi_q1fy27.txt (804 lines, 13 pages, unit convention: Rs Millions, x0.1 to Rs Cr)
Prior-quarter ledger: NONE (first quarterly run for AMAGI) — no ENTITY_CHANGE / DROPPED_ITEM diff possible.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 16   sweep_count: 16   match: yes
  method: grep for note markers (digit/roman/OCR-glyph "2","3","4","-l","S","5","6","7","8") within the two
  "Notes to..." blocks (lines 246-310 standalone, 541-595 consolidated) gave 9 raw pattern hits standalone
  and 10 raw hits consolidated (19 total); 3 of those are continuation paragraphs of an already-counted note
  (line 254 continues note 1 at 248; line 549 continues note 1 at 542; line 572 continues note 4 at 567).
  19 - 3 = 16 unique notes. Manual content sweep (matching note topics 1-8 across both statements: basis of
  prep/board approval, Note-2 derived-figures caveat, Note-3 IPO, Note-4 CCPS conversion, Note-5 Argoid
  liquidation, Note-6 Labour Codes, Note-7 deferred tax, Note-8 single segment) independently counts 8+8=16.
category: line_items       grep_count: 52   sweep_count: 52   match: yes
  method: grep non-blank lines inside the two P&L tables (204-241 standalone, 459-533 consolidated), strip
  section-header/caption lines (INCOME, EXPENSES, "Tax expense:", "Other comprehensive income/(loss)",
  "Items that will (not) be reclassified...", EPS caption lines) and continuation-only fragments (wrapped
  numeric rows with no new label). Standalone: 30 non-blank lines - 8 captions = 22. Consolidated cross-check
  via structural delta from standalone: 22 + 8 items unique to consolidated (Purchase of stock-in-trade,
  Changes in inventories, tax-line split India/Foreign +1 net, second "Income tax effect on above" line +1,
  Exchange differences on translation, 3x "attributable to Owners of the parent" rows) = 30. 22+30=52.
  Manual line-by-line sweep of both tables independently counts 22 standalone + 30 consolidated = 52.
category: zero_standing    grep_count: 7    sweep_count: 7    match: yes
  (subset of line_items with blank/dash value in ALL four periods shown: standalone Current tax, Deferred
  tax, Total tax expense, Income tax effect on above [OCI] = 4; consolidated Current tax-India taxes, Income
  tax effect on above [OCI defined-benefit], Income tax effect on above [OCI exchange-diff] = 3.)
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
  (grep -n -E "^\s*[0-9]+\.\s" on lines 33-82 of the Board Outcome letter finds 4 numbered items; manual
  sweep of the letter confirms exactly 4 substantive agenda items plus the meeting-timing sentence, which is
  not itself an agenda item.)
category: auditor_paras    grep_count: 13   sweep_count: 13   match: yes
  (standalone report lines 134-167: paras I/1,2,3,4,5 = 5; consolidated report lines 326-427: paras 1,2,3,4,
  5,6,7,8 = 8. grep -n -E "^[0-9]+\.\s|^I\.\s" within each report's line range gives 5 and 8 respectively;
  manual sweep of report text independently confirms 5 and 8. 5+8=13.)
category: entities          grep_count: 11   sweep_count: 11   match: yes
  (consolidated auditor report para 4, lines 353-372, enumerated (i)-(xi) by roman numeral marker; manual
  sweep of the same block counts 1 holding + 5 subsidiaries + 4 step-down subsidiaries + 1 controlled trust
  = 11.)
category: turns             grep_count: 0    sweep_count: 0    match: yes   (n/a — results filing, no transcript)
category: questions         grep_count: 0    sweep_count: 0    match: yes   (n/a)
category: mgmt_numbers      grep_count: 0    sweep_count: 0    match: yes   (n/a)
category: slides            grep_count: 0    sweep_count: 0    match: yes   (n/a — no investor deck in this doctype)
gate_a2: pass
=== END COUNT TEST ===
```

---

## SECTION 1 — BOARD OUTCOME LETTER: AGENDA ITEMS (pages 1-2, lines 30-90)
Meeting: Thursday, August 13, 2026. **Commenced 09:00 A.M. IST, concluded 10:35 A.M. IST** (line 86) — 95
minutes covering 4 substantive resolutions plus 3 Regulation-30 annexures.

| # | Line | Agenda item | First 15 words | Annexure | Flags |
|---|------|-------------|-----------------|----------|-------|
| 1 | 33-38 | Approval of Q1FY27 unaudited standalone + consolidated financial results, with limited review reports | "Approved the Unaudited Standalone and Consolidated Financial Results of the Company for the quarter" | Annexure I | |
| 2 | 40-46 | Re-appointment of Mr. Baskar Subramanian (DIN 02014529) as MD & CEO, subject to shareholder approval | "Approved and recommended the re-appointment of Mr. Baskar Subramanian (DIN: 02014529) as the Managing Director" | Annexure II | |
| 3 | 48-61 | Reclassification of Authorised Share Capital and consequent amendment of Clause V of the MOA, subject to shareholder approval | "Approved and recommended the reclassification of Authorised Share Capital and consequent amendment of Memorandum" | Annexure III | |
| 4 | 76-82 | Appointment of M/s. BMP & Co. LLP as Secretarial Auditors for 5 years, subject to shareholder approval | "Approved and recommended the appointment of M/s. BMP & Co. LLP, Company Secretaries, (Firm Registration" | Annexure IV | |

## SECTION 2 — BOARD OUTCOME LETTER: SIGNATURE BLOCK (lines 92-103)
| Signatory | Designation | Timestamp | Line | Flags |
|---|---|---|---|---|
| Sridhar Muthukrishnan (Membership No. F9606) | Company Secretary and Compliance Officer | Digitally signed 2026.08.13 10:35:38 +05'30' | 94-103 | Signed 38 seconds after the stated meeting-conclusion time of 10:35 A.M. — after, not before, so no SIGNATURE_BEFORE flag; noted as a very tight margin for the record. |

## SECTION 3 — STANDALONE AUDITOR'S LIMITED REVIEW REPORT (Annexure I, pages 3, lines 119-187)
Auditor: S.R. Batliboi & Associates LLP (ICAI FRN 101049W/E300004), per Pankaj Agarwal, Partner.

| Para | Line | First 15 words | Type | Flags |
|---|---|---|---|---|
| I (=1) | 134-138 | "We have reviewed the accompanying statement of unaudited standalone financial results of Amagi" | Scope of review | |
| 2 | 140-146 | "The Company's Management is responsible for the preparation of the Statement in accordance" | Management responsibility | |
| 3 | 148-156 | "We conducted our review of the Statement in accordance with the Standard on Review" | Basis of review (SRE 2410) | |
| 4 | 158-163 | "Based on our review conducted as above, nothing has come to our attention that" | Conclusion — unmodified/clean | |
| 5 | 165-167 | "The comparative financial information of the Company for the quarter ended June 30, 2025" | Other Matters — comparative Q1FY26 not audited/reviewed | |
| — | 170-181 | Signature block: "For S.R. Batliboi & Associates LLP...per Pankaj Agarwal, Partner, Membership Number: 217018" | Signature | UDIN: 26217018MXROFE6654 (OCR: "262170 l 8MXROFE6654") — verify digit string against source PDF |

No Emphasis of Matter, no Going Concern paragraph in the standalone report.

## SECTION 4 — STANDALONE STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 4, lines 195-243)
Periods: Q1FY27 (Jun-30-26, Unaudited) | Q4FY26 (Mar-31-26, Audited, Note 2) | Q1FY26 (Jun-30-25, Unaudited, Note 2) | FY26 (Mar-31-26, Audited).

| Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|
| Revenue from operations | 205 | 2,756.36 | 2,488.96 | 2,065.27 | 9,492.32 | |
| Other income | 206 | 244.68 | 241.60 | 151.43 | 645.31 | |
| Total income (I) | 207 | 3,001.04 | 2,730.56 | 2,216.70 | 10,137.63 | |
| Employee benefits expense | 211 | 1,000.50 | 848.08 | 885.34 | 3,640.35 | |
| Finance costs | 212 | 6.02 | 6.56 | 7.85 | 30.69 | |
| Depreciation and amortisation expense | 213 | 37.00 | 37.26 | 35.15 | 145.40 | |
| Other expenses | 214 | 1,727.81 | 1,641.69 | 1,343.66 | 6,056.72 | |
| Total expenses (II) | 215 | 2,771.33 | 2,533.59 | 2,272.00 | 9,873.16 | |
| Profit/(loss) before tax (III=I-II) | 217 | 229.71 | 196.97 | (55.30) | 264.47 | |
| Current tax | 219 | — | — | — | — | ZERO_STANDING |
| Deferred tax (Refer Note 7) | 220 | — | — | — | — | ZERO_STANDING |
| Total tax expense (IV) | 221 | — | — | — | — | ZERO_STANDING (confirmed: PBT=PAT every period) |
| Profit/(loss) for the period/year (V=III-IV) | 222 | 229.71 | 196.97 | (55.30) | 264.47 | |
| Re-measurement (losses)/gains on defined benefit plans | 226 | (29.86) | 18.02 | (4.07) | 7.21 | |
| Income tax effect on above | 227 | — | — | — | — | ZERO_STANDING |
| OCI for the period/year, net of tax (VI) | 228 | (29.86) | 18.02 | (4.07) | 7.21 | |
| Total comprehensive income/(loss) (VII=V+VI) | 229 | 199.85 | 214.99 | (59.37) | 271.68 | |
| Paid up equity share capital (Rs 5 FV) | 232 | 1,081.70 | 1,081.70 | 170.81 | 1,081.70 | |
| Instruments entirely equity in nature | 233 | — | — | 8,748.14 | — | non-zero in Q1FY26 only (pre-IPO CCPS); not ZERO_STANDING |
| Other equity | 234 | (n/a, qtr col) | (n/a, qtr col) | (n/a, qtr col) | 15,223.16 | annual-only disclosure line, not ZERO_STANDING |
| Basic EPS (Rs.) | 239 | 1.01 | 0.89 | (0.29) | 1.27 | |
| Diluted EPS (Rs.) | 240 | 1.01 | 0.88 | (0.29) | 1.26 | |

Standalone line items: 22 (of which 4 ZERO_STANDING).

## SECTION 5 — STANDALONE NOTES (page 5, lines 246-310)
| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 248, 254 | "The Unaudited Standalone Financial Results of Amagi Media Labs Limited (formerly Amagi Media Labs" + "These Unaudited Standalone Financial Results have been reviewed by the Audit Committee..." | basis of preparation + Board/AC approval, two paragraphs, one note |
| 2 | 257-262 | "The figures for the quarter ended March 31, 2026 are the derived balancing figures" | Q4 derived-balancing-figure caveat + Q1FY26 comparative unreviewed caveat |
| 3 | 264-268 | "During the quarter and year ended March 31, 2026, the Company completed its Initial" | IPO mechanics: fresh issue Rs 8,160.00mn + OFS Rs 9,726.19mn, listing Jan 21, 2026 |
| 4 | 271-277 | "During the year ended March 31, 2026 the Company pursuant to a circular resolution" | CCPS-to-equity conversions (two tranches: 3,804 Series D1 CCPS conv. ratio 1.72; 12,430,901 CCPS into 159,300,958 equity shares) |
| 5 | 279-280 | "The Board of Directors of Argoid Analytics Private Limited, a subsidiary at its meeting" | Argoid liquidation approved Nov 17, 2025 |
| 6 | 282-288 | "On November 21, 2025, the Government of India notified the Code on Wages, 2019" | Labour Codes — incremental past service cost Rs 76.24mn recognised in FY26 |
| 7 | 290-293 | "The Company has significant unabsorbed depreciation and carried forward losses and has also incurred" | No DTA recognised (Ind AS 12) |
| 8 | 295-296 | "The Company is engaged in the business of providing media technologies and related services" | Single reportable segment (Ind AS 108) |

Standalone notes: 8.

## SECTION 6 — STANDALONE SIGNATURE BLOCK (lines 298-310)
| Signatory | Designation | Line | Flags |
|---|---|---|---|
| Baskar Subramanian (DIN 02014529) | Managing Director and Chief Executive Officer | 305-307 | Place: Bengaluru, Date: August 13, 2026; no digital timestamp captured (image/wet-style signature block, unlike the CS letter) |

## SECTION 7 — CONSOLIDATED AUDITOR'S LIMITED REVIEW REPORT (Annexure I, pages 6-7, lines 312-442)
Auditor: S.R. Batliboi & Associates LLP, per Pankaj Agarwal, Partner.

| Para | Line | First 15 words | Type | Flags |
|---|---|---|---|---|
| 1 | 326-331 | "We have reviewed the accompanying Statement of Unaudited Consolidated Financial Results of Amagi" | Scope of review | |
| 2 | 333-338 | "The Holding Company's Management is responsible for the preparation of the Statement in" | Management responsibility | |
| 3 | 340-351 | "We conducted our review of the Statement in accordance with the Standard on Review" | Basis of review (SRE 2410) + additional procedures under SEBI Master Circular Reg 33(8) | |
| 4 | 353-372 | "The Statement includes the results of the following entities:" | Entity list — see Section 8 | |
| 5 | 382-389 | "Based on our review conducted and procedures performed as stated in paragraph 3 above" | Conclusion — unmodified/clean | |
| 6 | 391-409 | "The accompanying Statement includes the unaudited interim financial results and other unaudited financial" | Other Matters — 5 subsidiaries + controlled trust reviewed by other auditors (revenue Rs 1,166.33mn, PAT Rs 66.00mn, TCI Rs 66.00mn for the quarter); foreign-GAAP-to-Ind-AS conversion adjustments reviewed by principal auditor | |
| 7 | 411-419 | "The accompanying Statement includes unaudited interim financial results and other unaudited financial information" | Other Matters — 3 subsidiaries unaudited/unreviewed, management-furnished (revenue Rs Nil, net loss Rs 0.25mn, TCI loss Rs 0.25mn); management represents not material to Group | |
| 8 | 425-427 | "The comparative consolidated financial information of the Group for the quarter ended June" | Other Matters — Q1FY26 comparative not audited/reviewed | |
| — | 430-442 | Signature block: "For S.R. Batliboi & Associates LLP...per Pankaj Agarwal, Partner, Membership Number: 217018" | Signature | UDIN: 26217018ZGWATV1751 |

No Emphasis of Matter, no Going Concern paragraph. Conclusion in para 5 is stated as "not modified" with respect to reliance on other auditors (line 421-423).

**ENTITY_COVERAGE_GAP flag**: para 6 covers 5 subsidiaries + 1 trust (6 entities); para 7 covers 3 subsidiaries (3 entities). 6+3 = 9 non-holding entities with review-basis stated. The entity list in para 4 (Section 8 below) shows 10 non-holding entities (5 subsidiaries + 4 step-down subsidiaries + 1 trust). One non-holding entity's audit/review basis is not explicitly stated in paras 6 or 7 (most likely it is reviewed directly by the principal auditor as an Indian entity, e.g. Amagi AI Private Limited or Argoid Analytics Private Limited, but the report does not say so explicitly) — flagged for A3/A4 to chase.

## SECTION 8 — CONSOLIDATED AUDITOR REPORT: ENTITY LIST (para 4, lines 353-372)
| # | Entity | Relationship | Location | Line | Flags |
|---|---|---|---|---|---|
| i | Amagi Media Labs Limited | Holding Company | India | 356 | |
| ii | Amagi Corporation | Subsidiary | USA | 359 | |
| iii | Amagi Media Private Limited | Subsidiary | UK | 360 | |
| iv | Amagi Media Labs Pte. Limited | Subsidiary | Singapore | 361 | |
| v | Amagi Canada Corporation Inc. | Subsidiary | Canada | 362 | |
| vi | Amagi AI Private Limited | Subsidiary | India | 363 | |
| vii | Amagi Media UK Private Limited | Step-down subsidiary | UK | 366 | |
| viii | Amagi Eastern Europe d.o.o. za usluge | Step-down subsidiary | Croatia | 367 | |
| ix | Argoid Analytics Inc. | Step-down subsidiary | USA | 368 | |
| x | Argoid Analytics Private Limited | Step-down subsidiary (under liquidation since Nov 17, 2025) | India | 369 | cross-refs standalone/consolidated Note 5 |
| xi | Amagi Foundation | Controlled trust | India | 372 | |

Entities: 11 (no prior-quarter list exists for this ticker, so ENTITY_CHANGE cannot be tested this run; treat as the baseline list for next quarter's diff).

## SECTION 9 — CONSOLIDATED STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 8, lines 450-535)
Periods: Q1FY27 | Q4FY26 (Note 2) | Q1FY26 (Note 2) | FY26.

| Line item | Line | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|
| Revenue from operations | 460 | 4,368.78 | 3,969.71 | 3,300.61 | 15,056.06 | |
| Other income | 461 | 175.86 | 242.44 | 142.70 | 645.37 | |
| Total income (I) | 462 | 4,544.64 | 4,212.15 | 3,443.31 | 15,701.43 | |
| Purchase of stock-in-trade | 465 | 12.07 | — | — | 0.45 | new-in-consolidated line vs standalone; non-zero in 2 of 4 periods, not ZERO_STANDING |
| Changes in inventories of stock-in-trade | 466 | (12.07) | 0.37 | — | 0.60 | non-zero in 3 of 4 periods, not ZERO_STANDING |
| Employee benefits expense | 467 | 2,063.53 | 1,878.92 | 1,777.05 | 7,771.96 | |
| Finance costs | 468 | 11.37 | 14.64 | 15.32 | 60.45 | |
| Depreciation and amortisation expense | 469 | 58.86 | 61.14 | 49.68 | 215.96 | |
| Other expenses | 470 | 2,006.81 | 1,851.66 | 1,535.32 | 6,779.45 | |
| Total expenses (II) | 471 | 4,140.57 | 3,806.73 | 3,377.37 | 14,828.87 | |
| Profit before tax (III=I-II) | 473 | 404.07 | 405.42 | 65.94 | 872.56 | |
| Current tax — India taxes | 476 | — | — | — | — | ZERO_STANDING |
| Current tax — Foreign taxes | 477 | 58.50 | 56.51 | (1.52) | 306.53 | |
| Deferred tax charge/(credit) (Refer Note 7) | 478 | 6.52 | 6.28 | 28.05 | (150.70) | |
| Total tax expense (IV) | 479 | 65.02 | 62.79 | 26.53 | 155.83 | |
| Profit for the period/year (V=III-IV) | 480 | 339.05 | 342.63 | 39.41 | 716.73 | |
| Re-measurement (losses)/gains on defined benefit plan | 484 | (29.86) | 18.02 | (4.07) | 7.21 | |
| Income tax effect on above (#1, defined benefit) | 485 | — | — | — | — | ZERO_STANDING |
| Exchange differences on translating FS of foreign operations | 487-488 | 91.24 | 74.67 | 148.08 | 159.76 | |
| Income tax effect on above (#2, exchange differences) | 489 | — | — | — | — | ZERO_STANDING |
| OCI for the period/year, net of tax (VI) | 490 | 61.38 | 92.69 | 144.01 | 166.97 | |
| Total comprehensive income for the period/year (VII=V+VI) | 491 | 400.43 | 435.32 | 183.42 | 883.70 | |
| Profit attributable to: Owners of the parent | 494-495 | 339.05 | 342.63 | 39.41 | 716.73 | no separate NCI line shown; owners' total = Group total (no NCI disclosed) |
| OCI attributable to: Owners of the parent | 496-497 | 61.38 | 92.69 | 144.01 | 166.97 | |
| TCI attributable to: Owners of the parent | 505-506 | 400.43 | 435.32 | 183.42 | 883.70 | |
| Paid up equity share capital (Rs 5 FV) | 509 | 1,081.70 | 1,081.70 | 170.81 | 1,081.70 | |
| Instrument entirely in the nature of equity | 510 | — | — | 8,748.14 | — | non-zero in Q1FY26 only; not ZERO_STANDING |
| Other equity | 511 | (n/a, qtr col) | (n/a, qtr col) | (n/a, qtr col) | 16,486.39 | annual-only line, not ZERO_STANDING |
| Basic EPS (Rs) | 517/524 | 1.49 | 1.54 | 3.44 (OCR: "3 +4") | (garbled — verify against source) | value pair "1.49 / 1.54 / 3.44" line-wraps badly in OCR (lines 516-534); FY26 column value not legible in extract, verify against source PDF |
| Diluted EPS (Rs) | 518/525 | 1.49 | 1.54 | 3.23 (OCR: "3 .!3") | (garbled — verify against source) | same OCR-legibility caveat as Basic EPS |

Consolidated line items: 30 (of which 3 ZERO_STANDING).

## SECTION 10 — CONSOLIDATED NOTES (page 9, lines 541-595)
| Note | Line(s) | First 15 words | Flags |
|---|---|---|---|
| 1 | 542, 549 | "The Unaudited Consolidated Financial Results of Amagi Media Labs Limited (formerly Amagi Media" + "These Unaudited Consolidated Financial Results have been reviewed by the Audit Committee..." | basis of preparation + Board/AC approval, two paragraphs, one note |
| 2 | 553-558 | "The figures for the quarter ended March 31, 2026 are the derived balancing figures" | Q4 derived-balancing-figure caveat + Q1FY26 comparative unreviewed caveat |
| 3 | 560-564 | "During the quarter and year ended March 31, 2026, the Holding Company completed its" | IPO mechanics (same figures as standalone Note 3) |
| 4 | 567-573 | "During the year ended March 31, 2026, the Holding Company, pursuant to a circular" | CCPS-to-equity conversions (same as standalone Note 4), continuation at line 572 "Further, on November 21, 2025..." |
| 5 | 576-577 | "The Board of Directors of Argoid Analytics Private Limited, a subsidiary, at its meeting" | Argoid liquidation approved Nov 17, 2025 |
| 6 | 579-585 | "On November 21, 2025, the Government of India notified the Code on Wages, 2019" | Labour Codes — incremental past service cost Rs 76.24mn (Group level) |
| 7 | 588-591 | "The Holding Company has significant unabsorbed depreciation and earned forward losses and has also" | No DTA recognised (Ind AS 12) | TEXT_ANOMALY: text says "...has not been recognised by the Holding Company **in its standalone financial results** as at and for the quarter ended June 30, 2026..." inside the CONSOLIDATED notes — apparent copy-paste artifact from the standalone note, should read "consolidated financial results"; flagged for A3 |
| 8 | 593-594 | "The Group is engaged in the business of providing media technologies and related services" | Single reportable segment (Ind AS 108) |

Consolidated notes: 8.

## SECTION 11 — CONSOLIDATED SIGNATURE BLOCK (lines 597-608)
| Signatory | Designation | Line | Flags |
|---|---|---|---|
| Baskar Subramanian (DIN 02014529) | Managing Director and Chief Executive Officer | 603-605 | Place: Bengaluru, Date: August 13, 2026; no digital timestamp captured |

## SECTION 12 — ANNEXURE II: MD RE-APPOINTMENT DETAILS (Regulation 30/Sch III) (page 10, lines 611-665)
| S.No | Line | Particulars | Detail (first 15 words) | Flags |
|---|---|---|---|---|
| 1 | 618-620 | Reason for change | "Re-appointment of Mr. Baskar Subramanian (DIN: 02014529) as the Managing Director and Chief" | |
| 2 | 622-626 | Date of appointment/term | "Mr. Baskar Subramanian will be re-appointed as Managing Director and Chief Executive Officer for" — term: Dec 1, 2026 to Nov 30, 2031 (5 years) | |
| 3 | 628-642 | Brief profile | "Mr. Baskar Subramanian is one of the Promoters of the Company. He holds a" — B.Eng, Govt College of Technology Coimbatore; ex-ImpulseSoft CTO, ex-Texas Instruments (India); 23+ yrs experience; designated partner Vinculum Advisors LLP; director on 4 overseas subsidiary boards | |
| 4 | 644-646 | Relationships with other directors | "Mr. Baskar Subramanian is not related interse to any other Director of the Company." | |
| 5 | 648-653 | Debarment disclosure (BSE/NSE circulars) | "Mr. Baskar Subramanian is not debarred from accessing the capital markets and/or restrained from" | |

Director profile row: Baskar Subramanian, DIN 02014529, MD & CEO, term Dec-1-2026 to Nov-30-2031 (subject to shareholder approval), Promoter, no inter-se relationships disclosed.

## SECTION 13 — ANNEXURE III: MOA / AUTHORISED CAPITAL RECLASSIFICATION (pages 11-12, lines 668-736)
| # | Line | Content | Flags |
|---|---|---|---|
| 1 | 673-692 | Existing Clause V of MOA — Authorised Share Capital INR 2,47,25,13,655 divided into (a) 23,51,64,091 Ordinary Equity Shares of Rs 5 each, (b) 1,24,66,932 CCPS of Rs 100 each, (c) 5,00,000 OCPS of Rs 100 each | |
| 2 | 694-713 | Rationale — all CCPS/OCPS fully converted to equity pre-IPO; no CCPS/OCPS outstanding post-listing (Jan 21, 2026); reclassification aligns MOA with post-IPO single-class capital structure; no cancellation/reduction of paid-up capital, no effect on existing shareholder rights | |
| 3 | 730-735 | Amended Clause V of MOA — Authorised Share Capital INR 2,47,25,13,655 comprising 49,45,02,731 Ordinary Equity Shares of Rs 5 each (single class) | |

## SECTION 14 — ANNEXURE IV: SECRETARIAL AUDITOR APPOINTMENT DETAILS (page 13, lines 750-793)
| S.No | Line | Particulars | Detail (first 15 words) | Flags |
|---|---|---|---|---|
| 1 | 757-761 | Reason for change | "Appointment of M/s. BMP & Co. LLP, Peer reviewed Firm of Company Secretaries in" | |
| 2 | 763-768 | Date/term of appointment | "The Board at its meeting held on August 13, 2026, approved the appointment of" — 5 years, FY2026-27 to FY2030-31 (first term) | |
| 3 | 770-789 | Brief profile | "BMP is a firm of Practicing Company Secretaries with offices in Bengaluru, Mumbai, and" — founded 2017, peer-reviewed, offices Bengaluru/Mumbai/Delhi NCR | |
| 4 | 791-793 | Relationships with directors | "Not Applicable" | |

---

## SUMMARY COUNTS
- Notes: 16 (8 standalone + 8 consolidated)
- Line items (financial statement rows, both statements): 52 (22 standalone + 30 consolidated)
- Zero-standing line items: 7 (4 standalone + 3 consolidated), all `ZERO_STANDING`
- Board Outcome agenda items: 4
- Auditor report paragraphs: 13 (5 standalone + 8 consolidated)
- Consolidation entities: 11 (1 holding + 5 subsidiaries + 4 step-down subsidiaries + 1 controlled trust)
- Annexure detail rows: 12 (5 in Annexure II + 3 in Annexure III + 4 in Annexure IV)
- Signature blocks: 5 (Board Outcome letter CS, standalone MD, consolidated MD, standalone auditor, consolidated auditor)

## FLAGS RAISED
- `ZERO_STANDING` x7 (standalone: Current tax, Deferred tax, Total tax expense, Income tax effect on above-OCI; consolidated: Current tax-India taxes, Income tax effect on above-OCI defined benefit, Income tax effect on above-OCI exchange differences)
- `ENTITY_COVERAGE_GAP` — consolidated auditor report paras 6+7 account for 9 of 10 non-holding entities' review basis; 1 entity's basis unstated (Section 7/8)
- `TEXT_ANOMALY` — consolidated Note 7 (line 590) refers to "standalone financial results" inside the consolidated notes block, apparent copy-paste artifact (Section 10)
- OCR-legibility caveats (not formal flags, but verify against source PDF): standalone auditor UDIN digit string (line 178); consolidated EPS FY26 column values (lines 516-534, badly line-wrapped in extraction)
