# A2 COMPLETENESS LEDGER — Fujiyama Power Systems Ltd (UTLSOLAR / BSE 544613)
Doctype: results | Quarter: Q1 FY27 (quarter ended 30 June 2026)
Source: /home/user/inflection-pipeline/runs/utlsolar-q1fy27/work/extract_results_utlsolar_q1fy27.txt
Units: source stated in Rs million; converted x0.1 to Rs Crores throughout this ledger unless marked "per share" (EPS, not converted).
Prior-quarter ledger: not supplied to A2 — no cross-quarter diff possible; noted wherever the diff instruction applies (consolidation entity list, dropped disclosures).

```
=== A2 COUNT TEST ===
category: pnl_line_items    grep_count: 29   sweep_count: 29   match: yes
category: notes             grep_count: 8    sweep_count: 8    match: yes   (see NOTES COUNT-TEST METHOD below — prompt-specified digit+period regex returns 0 on this section; a layout-aware two-pass grep was substituted and cross-validated)
category: agenda_items      grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras     grep_count: 13   sweep_count: 13   match: yes   (6 standalone + 7 consolidated)
category: annexure_rows     grep_count: 12   sweep_count: 12   match: yes   (3 annexures x 4 rows: B, C, D)
category: entities           grep_count: 3    sweep_count: 3   match: yes   (Holding Co + 2 associates, consolidated report para 4)
category: signature_blocks  grep_count: 8    sweep_count: 8   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### NOTES COUNT-TEST METHOD (page 8 is OCR-degraded — see A1 DATA-QUALITY NOTE)
The prompt-specified pattern `grep -n -E "^\s*[0-9]+\.\s"` returns **zero** matches
inside the notes block (lines 538-602) because this filing's note markers carry
no trailing period, and OCR further corrupted several markers into non-digit
glyphs (note 2 -> "ns", note 5 -> "a", note 6 -> "a", note 8 -> "&"). A digit-only
regex therefore silently underenumerates — exactly the OCR-driven miss GATE A1's
page-7 fidelity pass already anticipated for this document. Two independent
mechanical passes were substituted:
- Pass 1 (label+text on one line): `grep -nE "^ {1,6}[^ ]{1,3} {3,}[A-Za-z]"` on
  lines 538-602 -> 5 hits: notes 1, 3, 4, 7, 8 (lines 541, 554, 565, 596, 600).
- Pass 2 (label alone on its own line, body text wrapped below/above):
  `grep -nE "^ {1,6}[^ ]{1,3}\s*$"` on lines 538-602 -> 3 hits: notes 2, 5, 6
  (lines 549, 572, 584 — OCR glyphs "ns", "a", "a").
- Combined mechanical count: 8. Manual content sweep (topic-boundary read):
  8 distinct topics. Cross-validated against two independent citation trails
  inside the same extract: (a) page 7 table "[Refer note N]" cites N = 8, 7, 5,
  6, 5, 5 (all present, none orphaned); (b) both auditor reports cite "note no.
  3" (fire) and "note no. 5" (Zayo entities/first consolidation), both present
  and content-consistent. 8 == 8, match: yes.

---
## 1. P&L LINE ITEMS — STANDALONE + CONSOLIDATED, ALL PERIODS (Rs Crores)
Source: A1 VERIFIED TRANSCRIPTION, page 7, lines 450-523 (grep basis: numeric
line-item rows matched by `awk 'NR==450,NR==523' | grep -nE "[0-9]+\.[0-9]{2}"`
after excluding the 5 explanatory footnote lines inside the flagged-cell note
[offsets 32-34, 38-39] -> 29 data rows; manual sweep of the transcription table
independently itemises the same 29 captions -> match).

| # | Line item | Line(s) | Std Q1FY27 | Std Q1FY26 | Std Q4FY26(unaud.) | Std FY26(aud.) | Consol Q1FY27 | Consol Q1FY26 | Consol Q4FY26(unaud.) | Consol FY26(aud.) | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | I. Revenue from operations | 450 | 1,345.693 | 597.349 | 900.773 | 2,654.506 | 1,345.693 | 597.349 | 900.773 | 2,654.506 | |
| 2 | II. Other income | 451 | 2.350 | 0.437 | 2.828 | 5.521 | 2.350 | 0.437 | 2.828 | 5.521 | |
| 3 | III. Total income (I+II) [subtotal] | 452 | 1,348.043 | 597.786 | 903.601 | 2,660.027 | 1,348.043 | 597.786 | 903.601 | 2,660.027 | |
| 4 | Cost of materials consumed | 455 | 1,063.978 | 413.242 | 670.420 | 2,027.843 | 1,063.978 | 413.242 | 670.420 | 2,027.843 | |
| 5 | Changes in inventories | 456 | (100.895) | 6.759 | (46.648) | (185.580) | (100.895) | 6.759 | (46.648) | (185.580) | |
| 6 | Other operating expenses | 457 | 35.401 | 18.739 | 25.053 | 82.436 | 35.401 | 18.739 | 25.053 | 82.436 | |
| 7 | Employee benefits expense | 458 | 38.937 | 23.400 | 33.989 | 112.356 | 38.937 | 23.400 | 33.989 | 112.356 | |
| 8 | Finance costs | 459 | 10.901 | 9.385 | 9.576 | 43.598 | 10.901 | 9.385 | 9.576 | 43.598 | |
| 9 | Depreciation and amortisation expense | 460-461 | 25.017 | 7.011 | 20.601 | 44.194 | 25.017 | 7.011 | 20.601 | 44.194 | |
| 10 | Other expenses | 462 | 53.462 | 29.316 | 46.495 | 127.151 | 53.462 | 29.316 | 46.495 | 127.151 | |
| 11 | Total Expenses [subtotal] | 463 | 1,126.801 | 507.852 | 759.486 | 2,251.998 | 1,126.801 | 507.852 | 759.486 | 2,251.998 | |
| 12 | V. Profit before exceptional items, share in loss of associates and tax [subtotal] | 465-467 | 221.242 | 89.934 | 144.115 | 408.029 | 221.242 | 89.934 | 144.115 | 408.029 | |
| 13 | Exceptional items: Loss due to fire in Bawal Plant (refer note 3) | 468-470 | 143.581 | 0 (dash) | 0 (dash) | 0 (dash) | 143.581 | 0 (dash) | 0 (dash) | 0 (dash) | ZERO_STANDING (dash in 3 of 4 periods both sides; one-off exceptional item, see note 3) |
| 14 | VI. Profit before share in loss of associates and tax [subtotal] | 472-473 | 77.661 | 89.934 | 144.115 | 408.029 | 77.661 | 89.934 | 144.115 | 408.029 | |
| 15 | Share in loss of associates | 474 | 0 (dash, all periods) | 0 (dash) | 0 (dash) | 0 (dash) | (0.001) | 0 (dash) | 0 (dash) | 0 (dash) | ZERO_STANDING; standalone structurally N/A (no associates at standalone level); consol nonzero only in Q1FY27, the first consolidation quarter — ENTITY_CHANGE origin |
| 16 | VII. Profit before tax [subtotal] | 476 | 77.661 | 89.934 | 144.115 | 408.029 | 77.660 | 89.934 | 144.115 | 408.029 | see PAT GAP section 2 |
| 17 | Current tax | 479-491 | 19.804 | 20.435 | 24.038 | 88.552 | 19.804 | 20.435 | 24.038 | 88.552 | A1-flagged cell: consolidated FY26 (year-ended 31-Mar-26) column source glyph ambiguous ("385.52" vs "885.52"); A1 resolved to 88.552 Cr (885.52m) by arithmetic reconciliation against printed Total tax expense of 103.904 Cr (1,039.04m). Carried forward as AMBIGUOUS_CELL_RESOLVED_BY_A1 — A3/A4 should treat this cell as reconciled-but-not-visually-confirmed. |
| 18 | Income tax relating to earlier period | 492-493 | 0 (dash) | 0 (dash) | 0.104 | 0.104 | 0 (dash) | 0 (dash) | 0.104 | 0.104 | ZERO_STANDING (dash in both current-quarter columns each side; nonzero only in FY26 full-year column) |
| 19 | Deferred tax | 494 | 0.062 | 1.912 | 13.650 | 15.248 | 0.062 | 1.912 | 13.650 | 15.248 | |
| 20 | Total tax expense [subtotal] | 495 | 19.866 | 22.347 | 37.792 | 103.904 | 19.866 | 22.347 | 37.792 | 103.904 | |
| 21 | IX. Profit for the period/year (VII-VIII) — PAT | 497-498 | 57.795 | 67.587 | 106.323 | 304.125 | 57.794 | 67.587 | 106.323 | 304.125 | standalone-vs-consol PAT gap, see section 2 |
| 22 | X.(i) Remeasurement gain/(loss) of defined benefit obligation plans | 500-503 | (0.247) | (0.070) | (0.280) | (0.242) | (0.247) | (0.070) | (0.280) | (0.242) | |
| 23 | X.(ii) Income tax relating to items that will not be reclassified to P&L | 504-507 | 0.062 | 0.018 | 0.070 | 0.061 | 0.062 | 0.018 | 0.070 | 0.061 | |
| 24 | Total other comprehensive income/(loss), net of tax [subtotal] | 508-509 | (0.185) | (0.052) | (0.210) | (0.181) | (0.185) | (0.052) | (0.210) | (0.181) | |
| 25 | XI. Total comprehensive income for the period/year (IX+X) [subtotal] | 511-512 | 57.610 | 67.535 | 106.113 | 303.944 | 57.609 | 67.535 | 106.113 | 303.944 | mirrors PAT gap (0.001 Cr) |
| 26 | XII. Paid up equity share capital (face value Re 1/share) | 514-516 | 30.690 | 28.010 | 30.642 | 30.642 | 30.690 | 28.010 | 30.642 | 30.642 | |
| 27 | XIII. Reserves | 518 | 0 (dash) | 0 (dash) | 0 (dash) | 1,242.714 | 0 (dash) | 0 (dash) | 0 (dash) | 1,242.714 | ZERO_STANDING (dash in all quarterly columns both sides — standard interim-reporting convention, Reserves shown only at year-end) |
| 28 | XIV. EPS – Basic (INR/share, not annualised for quarters, not Cr-converted) | 520-521 | 1.88 | 2.41 | 3.58 | 10.24 | 1.88 | 2.41 | 3.58 | 10.24 | |
| 29 | XIV. EPS – Diluted (INR/share, not annualised for quarters, not Cr-converted) | 521-522 | 1.88 | 2.40 | 3.57 | 10.21 | 1.88 | 2.40 | 3.57 | 10.21 | |

Note on face value: page 7's own header block (garbled OCR, line 412) misreads
"Re. 1" as "Re. 4/-"; the A1-verified transcription (line 520) reads "INR 1/-"
correctly, consistent with the paid-up capital of Rs 306.90m over what the
company's other filings identify as a Re-1-face-value share. Flag for A3:
RAW_VS_VERIFIED_DISCREPANCY (raw OCR only, not a document inconsistency).

---
## 2. STANDALONE vs CONSOLIDATED PAT GAP — COMPUTED METRIC (first-class row)

| Period | Standalone PAT (Cr) | Consolidated PAT (Cr) | Gap (Cr) | Gap (Rs) | Driver | Line(s) |
|---|---|---|---|---|---|---|
| Q1 FY27 (30 Jun 2026) | 57.795 | 57.794 | 0.001 | ~Rs 10,000 | Entirely "Share in loss of associates" (0.001 Cr / Rs 0.01m), the Group's equity-method share of Zayo Cables Pvt Ltd + Zayo Energy Pvt Ltd net loss since acquisition (25 Apr 2026); no other standalone-vs-consol adjustment present | 474, 476, 497-498 |
| Q1 FY26 (30 Jun 2025) | 67.587 | 67.587 | 0.000 | Rs 0 | Pre-consolidation comparative; consol column is standalone-sourced per note 6 (no associates existed yet) | 497-498 |
| Q4 FY26 (31 Mar 2026, unaudited) | 106.323 | 106.323 | 0.000 | Rs 0 | Same — pre-consolidation comparative, standalone-sourced per note 7 | 497-498 |
| FY26 (year ended 31 Mar 2026, audited) | 304.125 | 304.125 | 0.000 | Rs 0 | Same — pre-consolidation comparative | 497-498 |

Interpretive note (enumeration only, not analysis): this is the Group's
**first-ever consolidated result** (note 5). The gap is immaterial in this
quarter purely because the two new associates were only 31%-held and only
in scope for ~2 of the 3 months of the quarter (acquired 25 Apr 2026, quarter
began 1 Apr but the "quarter ended 30 June 2026" quarter runs Apr-Jun so ~9
weeks of exposure). A3/A4 should treat the standalone-only comparative
columns as NOT structurally comparable to a "real" consolidated trend since
every consolidated comparative cell in this filing is standalone data
relabelled, per notes 5 and 6 — this is not organic like-for-like.

---
## 3. BOARD OUTCOME — AGENDA ITEMS (page 1, lines 44-99)
Grep: `grep -nE "^\s*[0-9]+\.\s"` on lines 44-100 -> 4 hits (lines 70, 73, 78,
84). Manual sweep of the "inter alia, considered and approved" list -> 4
items. Match: yes.
Board meeting timing (line 103): commenced 05:30 P.M. IST, concluded 06:50
P.M. IST — 1 hour 20 minutes.

| # | Agenda item | Line(s) | Detail | Flags |
|---|---|---|---|---|
| 1 | Financial results approval | 70-71 | Un-audited Standalone and Consolidated financial results for Q1 FY27, with Limited Review Report as Annexure A | |
| 2 | Internal Auditor re-appointment | 73-76 | Mr. Rohit Garg re-appointed Internal Auditor, FY2026-27; detail at Annexure B | |
| 3 | Cost Auditor re-appointment | 78-82 | M/s Chandra Bhushan Kumar & Co., Cost Accountants, re-appointed Cost Auditor, FY2026-27; detail at Annexure C | |
| 4 | Secretarial Auditor re-appointment | 84-89 | M/s Raghav Bansal & Associates, Practising Company Secretaries, re-appointed for 5-year term FY2026-27 to FY2030-31, subject to shareholder approval at ensuing AGM; detail at Annexure D | shareholder-approval-pending caveat |

No dividend, AGM notice/record date, director appointment/resignation, ESOP
grant, or capital-raising enabling resolution item is present in this Board
Outcome letter — only 4 items, all administrative/compliance re-appointments
plus the quarterly results. Absence of any dividend agenda item is noted as
a structural fact, not flagged (results-only meeting).

---
## 4. NOTES TO THE RESULTS (page 8, lines 538-602) — 8 notes, count-test above

| Note | Line(s) | One-line content tag | Flags |
|---|---|---|---|
| 1 | 541-544 | Basis of filing: results reviewed by Audit Committee, approved by Board 13 Aug 2026, filed with BSE/NSE, subjected to limited review | |
| 2 | 548-550 (marker OCR-garbled to "ns") | Basis of preparation: Ind AS per Companies (Ind AS) Rules 2015, Section 133 Companies Act 2013 | |
| 3 | 554-561 | Bawal, Rewari plant fire (6 May 2026 — NB: para itself misprints "2025", contradicts the auditor's EOM paragraphs and the header which both say 6 May 2026; see flag): net carrying value damage Rs 1,435.81m (143.581 Cr), insurance claim lodged, loss recovery not yet ascertainable, presented as exceptional item "Loss due to Fire in Bawal Plant" | DATE_DISCREPANCY: note 3 body text reads "06 May 2025"; both auditor EOM paragraphs (lines 189, 282) and the quarter context (event inside a quarter ended 30 Jun 2026) read "06 May 2026" — near-certain OCR/typo in the note body, flagged for A3 verbatim capture rather than silently corrected |
| 4 | 565-569 | BIS inspections/seizures at two plants: Ecotech Extension-1 Greater Noida (goods worth Rs 24.50m seized, 24 Mar 2026) and Bawal, Rewari (goods worth Rs 19m seized, 28 Apr 2026); company disputes non-compliance allegation, has filed submission, awaiting BIS response | contingency, unquantified financial exposure beyond seized-goods value |
| 5 | 571-581 (marker OCR-garbled to "a") | First-time consolidation: Board approved 25 Apr 2026 acquisition of 3,100 equity shares (31% stake) each in Zayo Energy Pvt Ltd and Zayo Cables Pvt Ltd; both became associates w.e.f. 25 Apr 2026, equity-method (Ind AS 28); this is the Group's first consolidated result — no prior-period consolidated comparatives exist | ENTITY_CHANGE (Zayo Cables Pvt Ltd, Zayo Energy Pvt Ltd — both newly added to consolidation scope this quarter; no prior list to diff against, first consolidation) |
| 6 | 583-593 (marker OCR-garbled to "a") | Comparative Q1 FY26 (30 Jun 2025) figures sourced from IPO-process audited restated financial information (examination report dated 13 Oct 2025), not from a standard prior-period result filing | |
| 7 | 596-597 | Q4 FY26 (31 Mar 2026) column is a balancing figure: full-year audited minus published 9M unaudited (itself limited-reviewed) | derived/balancing figure, not independently reviewed as a standalone quarter |
| 8 | 600-601 (marker OCR-garbled to "&") | Segment disclosure: single reportable segment (SPGS — solar power generating systems products), predominantly India-only operations, no separate segment per Ind AS 108 | see SEGMENT section 8 below |

---
## 5. AUDITOR REPORT — STANDALONE (pages 3-4, lines 154-228) — 6 paragraphs

| Para | Line(s) | Content tag | Flags |
|---|---|---|---|
| 1 | 159-163 | Scope: reviewed unaudited standalone results for quarter ended 30 Jun 2026, per Reg 33 SEBI LODR | |
| 2 | 165-170 | Responsibility statement: Ind AS 34, Companies Act s.133, auditor expresses conclusion not opinion | |
| 3 | 172-179 | Review standard: SRE 2410 (ICAI); review is substantially less in scope than audit; no audit opinion expressed | |
| 4 | 181-186 | Conclusion: nothing has come to attention indicating non-disclosure per Reg 33 or material misstatement | unmodified conclusion |
| 5 | 188-193 | EMPHASIS OF MATTER: draws attention to note 3, Bawal fire, aggregate carrying value Rs 1,435.81m (143.581 Cr) recognised as exceptional item; "conclusion is not modified in respect of this matter" | EOM_PARAGRAPH — flagged for A3 verbatim capture |
| 6 | 202-213 | Other Matter: Q1 FY26 comparative figures extracted from IPO-process audited restated financial information (examination report dated 13 Oct 2025, per SEBI ICDR Regs 2018 / Guidance Note); "conclusion is not modified in respect of this matter" | |

Signatory: Rahul Singhal, Partner, S N Dhawan & CO LLP, Membership No. 096570,
UDIN 26096570UZPIQM1192, Place Gurugram, Date 13 August 2026 (lines 215-228).
Firm Registration No. 000050N/N500045.

---
## 6. AUDITOR REPORT — CONSOLIDATED (pages 5-6, lines 238-340) — 7 paragraphs

| Para | Line(s) | Content tag | Flags |
|---|---|---|---|
| 1 | 243-248 | Scope: reviewed unaudited consolidated results (Holding Co + share of associates' net loss/TCL) for quarter ended 30 Jun 2026, per Reg 33 SEBI LODR | |
| 2 | 250-255 | Responsibility statement: Ind AS 34, Companies Act s.133 | |
| 3 | 257-267 | Review standard SRE 2410; sub-paragraph: procedures also performed per SEBI circular under Reg 33(8) | |
| 4 | 269-273 | ENTITY LIST — see section 7 below (3 entities: Holding Co + 2 associates) | see ENTITY_CHANGE flags below |
| 5 | 274-279 | Conclusion: nothing has come to attention indicating non-disclosure or material misstatement | unmodified conclusion |
| 6 | 281-286 | EMPHASIS OF MATTER: draws attention to note 3, Bawal fire, aggregate carrying value Rs 1,435.81m (143.581 Cr) recognised as exceptional item; "conclusion is not modified" | EOM_PARAGRAPH — flagged for A3 verbatim capture; substantively identical wording to standalone para 5 |
| 7a | 305-309 | Other Matter (a): consolidated results prepared for the first time (note 5); comparative info for preceding quarter, prior-year quarter, and prior year-end are standalone-only figures relabelled | FIRST_TIME_CONSOLIDATION — comparability caveat, feeds section 2 gap analysis |
| 7b | 311-323 | Other Matter (b): Q1 FY26 comparative sourced from IPO-process restated financial info (examination report dated 13 Oct 2025); "conclusion is not modified in respect of these matters" | |

Signatory: Rahul Singhal, Partner, S N Dhawan & CO LLP, Membership No. 096570,
UDIN 26096570ZFZAOM9125, Place Gurugram, Date 13 August 2026 (lines 326-340).
Firm Registration No. 000050N/N500045. Same partner signed both reports
(consistent, not a flag).

---
## 7. CONSOLIDATION ENTITY LIST (para 4 of consolidated auditor report, lines 269-273)

| # | Entity | Relationship | Line | Flags |
|---|---|---|---|---|
| a | Fujiyama Power Systems Limited | Holding Company | 270 | |
| b | Zayo Cables Private Limited | Associate (31% stake) w.e.f. 25 April 2026 | 271 | ENTITY_CHANGE — newly added, first consolidation quarter |
| c | Zayo Energy Private Limited | Associate (31% stake) w.e.f. 25 April 2026 | 272 | ENTITY_CHANGE — newly added, first consolidation quarter |

No prior-quarter entity list was supplied to A2 (PRIOR_LEDGER_PATH not
provided) — per note 5 there is no prior consolidated result at all, so a
diff is structurally impossible for this filing regardless; both additions
are inherent to the first consolidation, not comparable to a "removed/
renamed" case.

---
## 8. SEGMENT DISCLOSURE

Single item, note 8 (line 600-601): no separate reportable segment under Ind
AS 108 — company operates in one segment (solar power generating systems /
SPGS products), predominantly India. No segment-wise revenue/profit/assets
table is presented anywhere in the filing (consistent with the single-segment
claim — nothing to cross-check it against within this document).

---
## 9. TAX LINES / OCI LINES / EPS — cross-reference
All tax lines (Current tax, Income tax relating to earlier period, Deferred
tax, Total tax expense), OCI lines (remeasurement gain/loss, tax on OCI item,
Total OCI), and EPS (Basic, Diluted) are enumerated as line items 17-20,
22-24, 28-29 respectively in section 1 above (both standalone and
consolidated, all 4 periods each side). No separate table exists in the
filing for these — they are components of the single P&L statement.

---
## 10. ANNEXURES B, C, D — SEBI Master-Circular re-appointment disclosure tables
Each annexure has an identical 4-row structure. Grep
`grep -nE "^\s*[0-9]+\.\s"` restricted to each annexure's line range -> 4 hits
each (12 total); manual sweep of each table -> 4 rows each (12 total). Match:
yes.

### Annexure B — Internal Auditor re-appointment (page 9, lines 618-657)
| Row | Line | Field | Value |
|---|---|---|---|
| 1 | 628-630 | Reason for change | Re-appointment |
| 2 | 632-633 | Date/term | Re-appointed 13 Aug 2026, for FY2026-27 |
| 3 | 635-639 | Brief profile | Mr. Rohit Garg, Company employee, finance/accounts/internal controls/audit experience |
| 4 | 641 | Director relationships | Not Applicable (not a director appointment) |

### Annexure C — Cost Auditor re-appointment (page 10, lines 659-707)
| Row | Line | Field | Value |
|---|---|---|---|
| 1 | 669-671 | Reason for change | Re-appointment |
| 2 | 673-674 | Date/term | Re-appointed 13 Aug 2026, for FY2026-27 |
| 3 | 676-689 | Brief profile | M/s Chandra Bhushan Kumar & Co., sole-proprietorship cost accountancy firm, FRN002885 |
| 4 | 691 | Director relationships | Not Applicable |

### Annexure D — Secretarial Auditor re-appointment (page 11, lines 709-765)
| Row | Line | Field | Value |
|---|---|---|---|
| 1 | 720-722 | Reason for change | Re-appointment |
| 2 | 724-728 | Date/term | Re-appointed 13 Aug 2026, 5-year term FY2026-27 to FY2030-31, subject to shareholder approval at ensuing AGM |
| 3 | 730-745 | Brief profile | Raghav Bansal & Associates, practising CS firm, founded by Raghav Bansal (BBA, LL.B., FCS) |
| 4 | 747 | Director relationships | Not Applicable |

No director appointment/resignation/DIN/term-dates/background/relationship
disclosure appears anywhere in this filing — all three re-appointments are
auditor/professional-firm roles, not directorships, so the "director profile"
enumeration instruction (rule 4, ENUMERATE — RESULTS FILING) has no rows to
produce this quarter. Noted as a structural absence, not a gap.

---
## 11. DIGITAL SIGNATURE / SIGNOFF BLOCKS — 8 total

| # | Location | Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | Cover letter (page 2) | 118-123 | Mayuri Gupta | Company Secretary & Compliance Officer | OCR-garbled ("esios0s30" / "Date: .08.") — date/time not legible | SIGNATURE_TIMESTAMP_ILLEGIBLE — cannot verify signing time vs board meeting conclusion (06:50 PM per line 103) |
| 2 | Standalone auditor report (page 4) | 221-228 | Rahul Singhal, Partner | S N Dhawan & CO LLP | Place Gurugram, Date 13 August 2026 (typed, legible) | not a digital-signature block; UDIN 26096570UZPIQM1192 |
| 3 | Consolidated auditor report (page 6) | 333-340 | Rahul Singhal, Partner | S N Dhawan & CO LLP | Place Gurugram, Date 13 August 2026 (typed, legible) | not a digital-signature block; UDIN 26096570ZFZAOM9125 |
| 4 | Results statement (page 7) | 525-528 | Yogesh Dua (name given in A1's bracketed identification only) | Joint Managing Director & CEO | illegible beyond identification (company seal + auditor seal present but no readable timestamp) | SIGNATURE_TIMESTAMP_ILLEGIBLE |
| 5 | Notes footer (page 8) | 610-616 | Yogesh Dua | Joint Managing Director & CEO, DIN 00315251 | Place Delhi, Date 13 August 2026 (typed, legible) | not a digital-signature block |
| 6 | Annexure B (page 9) | 646-648 | Mayuri Gupta | Company Secretary & Compliance Officer | OCR-garbled, no legible timestamp | SIGNATURE_TIMESTAMP_ILLEGIBLE |
| 7 | Annexure C (page 10) | 696-698 | Mayuri Gupta | Company Secretary & Compliance Officer | OCR-garbled, no legible timestamp | SIGNATURE_TIMESTAMP_ILLEGIBLE |
| 8 | Annexure D (page 11) | 752-758 | Mayuri Gupta | Company Secretary & Compliance Officer | explicit "Digitally signed b'" text fragment present, but full timestamp OCR-garbled | SIGNATURE_TIMESTAMP_ILLEGIBLE |

Net: 4 of 8 signoff blocks (all four Mayuri Gupta / Company Secretary blocks,
#1/#6/#7/#8) carry illegible digital-signature timestamps. This blocks the
"signature before board meeting concluded" tripwire check the operating
rules call for — flagged as present-but-illegible for A3/A4, not resolved
here (no arithmetic cross-check is available for a timestamp the way A1 had
one for the ambiguous tax-cell digit).

---
## SUMMARY OF FLAGS RAISED
- ZERO_STANDING (4 line items: Exceptional items/fire loss, Share in loss of
  associates, Income tax relating to earlier period, Reserves)
- ENTITY_CHANGE (2 entities: Zayo Cables Pvt Ltd, Zayo Energy Pvt Ltd — first
  consolidation quarter, no prior list to diff against)
- FIRST_TIME_CONSOLIDATION (comparative-info caveat, auditor Other Matter 7a)
- EOM_PARAGRAPH (x2: standalone para 5, consolidated para 6 — Bawal fire)
- AMBIGUOUS_CELL_RESOLVED_BY_A1 (Current tax, consolidated FY26 column —
  885.52m resolved by A1 via arithmetic reconciliation, not visually
  confirmed)
- DATE_DISCREPANCY (note 3 body says fire occurred "06 May 2025"; both
  auditor EOM paragraphs and quarter context say "06 May 2026")
- RAW_VS_VERIFIED_DISCREPANCY (raw OCR page-7 header misreads face value as
  "Re. 4/-"; A1-verified transcription correctly reads "Re. 1/-" — OCR
  artifact only, not a document inconsistency)
- SIGNATURE_TIMESTAMP_ILLEGIBLE (4 of 8 signoff blocks — all Mayuri Gupta /
  Company Secretary digital signatures; board-meeting-timing cross-check
  blocked)

## PRESENT-BUT-ILLEGIBLE ITEMS FOR A3/A4 (treat as limitations, not gaps)
1. Current tax, consolidated, Year Ended 31 March 2026 column (line 479-491):
   source glyph ambiguous; A1 resolved to Rs 885.52m / Rs 88.552 Cr by
   arithmetic reconciliation against the printed Total tax expense row. A3/A4
   should cite this as "reconciled, not visually confirmed."
2. All four Company Secretary (Mayuri Gupta) digital-signature timestamps
   (cover letter, Annexures B/C/D) — cannot confirm signing time relative to
   the 06:50 PM board meeting conclusion.
3. Results-statement signature/seal block (page 7, lines 525-528) — company
   seal and auditor seal present in the scan but carry no legible additional
   data beyond identification.
4. Note 3's "06 May 2025" fire date — near-certainly a typo/OCR artifact
   (auditor EOM paragraphs both independently say "06 May 2026," consistent
   with the quarter being reported), but A2 does not silently correct
   source text; flagged verbatim for A3.
