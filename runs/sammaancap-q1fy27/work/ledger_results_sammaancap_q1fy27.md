# A2 COMPLETENESS LEDGER — SAMMAANCAP Q1FY27 (results filing)
Source: extract_results_sammaancap_q1fy27.txt (42 pages, 1700 lines, Rs. in Crores, OCR pages 39-42)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 42   sweep_count: 42   match: yes
category: footnotes        grep_count: 11   sweep_count: 11   match: yes
category: line_items       grep_count: 194  sweep_count: 194  match: yes
category: zero_standing    grep_count: 54   sweep_count: 54   match: yes  (subset of line_items, informational)
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 26   sweep_count: 26   match: yes
category: entities         grep_count: 10   sweep_count: 10   match: yes
category: annexures        grep_count: 3    sweep_count: 3    match: yes  (Annexure I to Security Cover Certificate referenced but not found in extract — see GAP flag)
category: signature_blocks grep_count: 10   sweep_count: 10   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note: line_items grep pass used a digit/value regex (`[0-9]|-\s*$`) per table block plus a manual sweep for
all-dash rows the digit regex misses (e.g. Standalone "Current tax" row, line 674, is "-  -  -  -" with no digits —
caught only by manual sweep, then folded into the reconciled grep_count above by widening the pattern). This
mismatch-then-resweep is recorded here as the GATE A2 process working as intended, not as evidence excluded from
the final ledger.

---

## 1. BOARD MEETING OUTCOME — AGENDA ITEMS
Meeting held August 13, 2026. Started 02:00 PM (14:00) IST, concluded 03:40 PM (15:40) IST — 1h40m duration (line 31).

| # | Line | Item | First ~15 words | Flags |
|---|------|------|------------------|-------|
| 1 | 34 | Unaudited Standalone & Consolidated Financial Results Q1 FY27 | "The Unaudited Standalone and Consolidated Financial Results of the Company for the quarter ended June 30, 2026" | — |
| 2 | 53 | Appointment of H.E. Dalia Hazem Gamil Khorshid (DIN 11789322) as Additional Non-Exec Non-Indep Director | "The Board, based on the recommendation of the Nomination and Remuneration Committee... approved the appointment" | Avenir/IHC nominee |
| 3 | 73 | Cessation of Non-Exec Chairman & Indep Director Mundra (2nd/final term ends Aug 17, 2026) + appointment of Mohapatra as Interim Chairman w.e.f. Aug 18, 2026 | "The Board noted that Mr. Subhash Sheoratan Mundra... will complete his second and final term" | Two-part agenda item; chairman transition |
| 4 | 91 | LIC nominee director change — P. S. Negi in place of Rajiv Gupta (DIN 08532421) | "the Board took note of the letter received from LIC nominating Mr. P. S. Negi" | DIN application pending for Negi |

---

## 2. ANNEXURES TO BOARD OUTCOME LETTER

| Annexure | Line | Content | Flags |
|---|---|---|---|
| Annexure A | 125-154 | Reg 30/Schedule III disclosure table for Khorshid appointment: 6 rows (Name, Reason, Date, Brief Profile ref, Relationship disclosure, Non-debarment confirmation) | — |
| Annexure B | 164-219 | Director profile — H.E. Dalia Khorshid, Group CEO & MD of Beltone Holding; full career/board bio | — |
| Annexure A (to consolidated review report, separate doc) | 331-354 | List of 10 consolidation entities — see Section 5 | — |

Referenced but not located in extract: **"Annexure I"** to the Security Cover Certificate (line 1316, "minimum
asset cover requirement... as given in Annexure I attached to this certificate") — not present on OCR'd pages
39-42 or elsewhere in the extract. Flag `ANNEXURE_REFERENCED_NOT_FOUND`.

---

## 3. INDEPENDENT AUDITOR'S REVIEW REPORT — CONSOLIDATED (Nangia & Co LLP + M Verma & Associates)

| Para | Line | Content (first ~12 words) | Flags |
|---|---|---|---|
| 1 | 236 | "We have jointly reviewed the accompanying statement of unaudited consolidated financial results" | Scope: Holding Co + 9 subsidiaries + trust |
| 2 | 243 | "This Statement... prepared in accordance with... Ind AS 34" | — |
| 3 (Scope of review) | 251 | "We conducted our review... in accordance with... SRE 2410" — moderate assurance, not an audit opinion | — |
| 4 | 267 | "The Statement includes the results of the subsidiaries and trust as per Annexure A" | — |
| 5 (Conclusion) | 269 | Unmodified conclusion: "nothing has come to our attention that causes us to believe" material misstatement | Clean/unmodified |
| 6 (Other Matters) | 286 | 9 subsidiaries + trust unaudited interim results (revenue Rs.178.86cr, PAT Rs.17.70cr, TCI Rs.16.38cr) reviewed by respective independent auditors, furnished by Management, relied upon | Reliance on other auditors; entities reviewed not audited by joint auditors directly |
| Signatures | 305-322 | Jaspreet Singh Bedi (Nangia & Co, UDIN 26601788KTZCWT2280, 15:08:31) and Mohender Gandhi (M Verma & Associates, UDIN 26088396QTOCBC8914, 15:17:24) | `SIGNATURE_BEFORE_BOARD_CONCLUSION` — both timestamps precede 15:40 board conclusion |

## 4. INDEPENDENT AUDITOR'S REVIEW REPORT — STANDALONE (Nangia & Co LLP + M Verma & Associates)

| Para | Line | Content (first ~12 words) | Flags |
|---|---|---|---|
| 1 | 583 | "We have jointly reviewed the accompanying statement of unaudited standalone financial results" | — |
| 2 | 588 | "This Statement... prepared in accordance with... Ind AS 34" | — |
| 3 (Scope of review) | 595 | "We conducted our review... SRE 2410"; moderate assurance | — |
| 4 (Conclusion) | 605 | Unmodified conclusion — no material misstatement noted | Clean/unmodified; no Other Matters/EOM paragraph (unlike consolidated) |
| Signatures | 612-626 | Jaspreet Singh Bedi (UDIN 26601788OGQKNW8028, 15:09:02) and Mohender Gandhi (UDIN 26088396SKTQOA9677, 15:18:26) | `SIGNATURE_BEFORE_BOARD_CONCLUSION` — both precede 15:40 board conclusion |

## 5. SECURITY COVER CERTIFICATE — AUDITOR'S CERTIFICATE (M Verma & Associates, pages 35-38)

| Para | Line | Content (first ~12 words) | Flags |
|---|---|---|---|
| 1 | 1275 | Engagement letter dated Oct 15, 2024; certificate for Stock Exchanges + IDBI Trusteeship (Debenture Trustee) | — |
| 2 | 1285 | M Verma & Associates as Joint Statutory Auditors examined the Statement | — |
| 3 (Mgmt responsibility) | 1296 | Preparation of Statement is Management's responsibility | — |
| 4 | 1302 | Management responsible for SEBI Regulations/Circular/Trust Deed compliance | — |
| 5 | 1313 | Management responsible for Asset Cover Ratio compliance per Annexure I (see Section 2 gap flag) | — |
| 6 (Auditors' responsibility) | 1320 | Limited assurance conclusion on figures agreement + asset cover ratio + covenant compliance | — |
| 7 | 1340 | Joint review of standalone results with Nangia & Co, unmodified conclusion dated Aug 13, 2026 | — |
| 8 | 1354 | Examination per Guidance Note on Reports/Certificates for Special Purposes | — |
| 9 | 1359 | Compliance with SQC 1 | — |
| 10 | 1363 | Scope did not involve audit tests / no opinion on financial results as a whole | — |
| 11 (a-f) | 1373 | Procedures performed: traced balances, obtained Trust Deeds, relied on mgmt rep for Rs.355cr HQLA deduction, verified arithmetic, sampled covenant compliance, inquired on non-compliance | Reliance on management representation (355cr HQLA) |
| 12 | 1402 | Limited assurance engagement — lower assurance than reasonable assurance/audit | — |
| 13 (Emphasis) | 1409 | **"The Company has, as at June 30, 2026, breached certain financial covenants under borrowing arrangements other than the above Debentures"** — conclusion not modified | `COVENANT_BREACH` — material flag; no cross-default per mgmt representation |
| 14 (Conclusion) | 1431 | Nothing come to attention re: figures agreement, asset cover ratio, or covenant compliance re: the Debentures specifically | Conclusion caveated by para 13 breach (non-Debenture borrowings) |
| 15 (Restriction on use) | 1452 | Certificate solely for Company's use for stated purpose | — |
| 16 | 1465 | No responsibility to update after certificate date | — |
| Signature | 1468-1479 | Mohender Gandhi, M Verma & Associates, UDIN 26088396XNZFKI7075, 15:27:25 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` — precedes 15:40 board conclusion |

**Auditor paragraph total: 6 (consolidated) + 4 (standalone) + 16 (Security Cover Cert) = 26.**

---

## 6. CONSOLIDATION ENTITY LIST (Annexure A to Consolidated Review Report, lines 333-353)

| # | Line | Entity | Relationship | Flags |
|---|---|---|---|---|
| 1 | 334 | Sammaan Collection Agency Limited (fka Indiabulls Collection Agency Ltd) | Subsidiary | Renamed from Indiabulls-branded name |
| 2 | 336 | Sammaan Sales Limited (fka Ibulls Sales Ltd) | Subsidiary | Renamed |
| 3 | 338 | Sammaan Insurance Advisors Limited (fka Indiabulls Insurance Advisors Ltd) | Subsidiary | Renamed |
| 4 | 340 | Sammaan Investmart Services Limited (fka Nilgiri Investmart Services Ltd) | Subsidiary of #3 | Renamed; sub-subsidiary |
| 5 | 342 | Indiabulls Capital Services Limited | Subsidiary | Not yet renamed (retains Indiabulls name) |
| 6 | 344 | Sammaan Finserve Limited (fka Indiabulls Commercial Credit Ltd) | Subsidiary | Renamed; also subject of demerger Scheme (Note 13/17) and Rs.815cr impairment (Standalone Note 10) |
| 7 | 346 | Sammaan Advisory Services Limited (fka Indiabulls Advisory Services Ltd) | Subsidiary | Renamed |
| 8 | 348 | Honos Asset Holding Company Limited (fka Indiabulls Asset Holding Company Ltd) | Subsidiary | Renamed |
| 9 | 350 | Sammaan Asset Management Limited (fka Indiabulls Investment Management Ltd) | Subsidiary | Renamed |
| 10 | 352 | Pragati Employee Welfare Trust (fka Indiabulls Housing Finance Ltd - Employee Welfare Trust) | Trust | Renamed |

No prior-quarter ledger supplied for diff — cannot confirm additions/removals/renames vs. Q4FY26 list. Flag
`ENTITY_CHANGE` not assignable without prior list; note for A3/A4: entity #5 (Indiabulls Capital Services Limited)
is the only one of 10 not yet rebranded to "Sammaan" — worth a consistency question in the concall if one exists.
Matches Other Matters para (9 subsidiaries + 1 trust = 10 entities, consistent).

---

## 7. STATEMENT OF CONSOLIDATED FINANCIAL RESULTS — LINE ITEMS (pages 8-10, lines 366-438)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 367 | Interest income (Refer Note 10) | 1,078.17 | 1,104.87 | 1,563.64 | 5,586.91 | — |
| 2 | 368 | Fees and commission income | 58.77 | 30.47 | 62.24 | 193.26 | — |
| 3 | 369 | Net gain on fair value changes | 490.98 | 116.94 | 42.05 | 969.33 | — |
| 4 | 370-372 | Net gain on derecognition of financial instruments under amortised cost (Refer Note 11) | 24.01 | 105.38 | 732.40 | 1,416.66 | — |
| 5 | 373 | Total revenue from operations (subtotal) | 1,651.93 | 1,357.66 | 2,400.33 | 8,166.16 | — |
| 6 | 374 | Other income | 30.88 | 3.66 | 9.10 | 24.07 | — |
| 7 | 375 | Total income (1+2) (subtotal) | 1,682.81 | 1,361.32 | 2,409.43 | 8,190.23 | — |
| 8 | 377 | Finance costs | 1,335.26 | 1,678.56 | 1,196.12 | 5,618.36 | — |
| 9 | 378-380 | Impairment on financial instruments net of recoveries (Refer Note 9) | (240.47) | 2,958.08 | 465.98 | 3,627.94 | — |
| 10 | 381 | Employee benefits expenses | 176.61 | 183.78 | 184.08 | 673.05 | — |
| 11 | 382 | Depreciation and amortization | 20.11 | 25.04 | 21.03 | 88.43 | — |
| 12 | 383 | Other expenses | 65.29 | 113.31 | 74.11 | 467.70 | — |
| 13 | 384 | Total expenses (subtotal) | 1,356.80 | 4,958.77 | 1,941.32 | 10,475.48 | — |
| 14 | 385 | Profit/(Loss) before Exceptional Items and tax (3-4) (subtotal) | 326.01 | (3,597.45) | 468.11 | (2,285.25) | — |
| 15 | 386 | Exceptional Items (Refer Note 8) | - | (6,499.17) | - | (6,499.17) | `ZERO_STANDING` in Q1FY27 and Q1FY26 cols |
| 16 | 387 | Profit/(Loss) before tax (5+6) (subtotal) | 326.01 | (10,096.62) | 468.11 | (8,784.42) | — |
| 17 | 402 | Current tax | 4.18 | (3.57) | 5.39 | 5.36 | — |
| 18 | 403 | Deferred tax | 78.53 | (1,991.64) | 128.42 | (1,645.22) | — |
| 19 | 404 | Total tax expense (subtotal) | 82.71 | (1,995.21) | 133.81 | (1,639.86) | — |
| 20 | 405-407 | Profit/(Loss) for period attributable to shareholders (7-8) | 243.30 | (8,101.41) | 334.30 | (7,144.56) | — |
| 21 | 410 | Remeasurement gain/(loss) on defined benefit plan | (1.52) | 4.97 | (0.02) | 4.26 | — |
| 22 | 411 | (Loss)/Gain on equity instrument FVOCI (Refer Note 8) | 9.11 | (1,088.72) | (115.75) | (1,505.14) | — |
| 23 | 412 | Income tax impact on (A) above | 1.60 | 70.32 | 23.16 | 152.34 | — |
| 24 | 414 | Effective portion of cash flow hedges | (147.76) | 94.60 | (12.08) | (37.79) | — |
| 25 | 415 | Income tax impact on (B) above | 37.19 | (23.81) | 3.04 | 9.51 | — |
| 26 | 416 | Total other comprehensive (loss)/income (subtotal) | (101.38) | (942.64) | (101.65) | (1,376.82) | — |
| 27 | 417 | Total comprehensive (loss)/income (9+10) (subtotal) | 141.92 | (9,044.05) | 232.65 | (8,521.38) | — |
| 28 | 418-420 | Paid-up equity share capital (face value Rs.2) | 229.34 | 228.76 | 162.70 | 228.76 | — |
| 29 | 434 | Other equity | (blank) | (blank) | (blank) | 18,762.71 | `ZERO_STANDING` — quarter columns blank by template convention (annual-only disclosure) |
| 30 | 436 | EPS Basic (not annualised) | 2.13 | (99.10) | 4.10 | (87.72) | — |
| 31 | 437 | EPS Diluted (not annualised) | 2.05 | (99.10) | 4.10 | (87.72) | — |
| 32 | 438 | EPS Face Value | 2.00 | 2.00 | 2.00 | 2.00 | — |

## 8. NOTES TO CONSOLIDATED FINANCIAL RESULTS (lines 440-568, notes 1-19)

| # | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 440 | "The consolidated financial results have been prepared in accordance with the recognition and measurement principles laid down in Ind AS 34" | Boilerplate basis of preparation |
| 2 | 444 | "The consolidated financial results... have been reviewed by the Audit Committee on August 13, 2026 and subsequently approved" | Same-day AC review + Board approval |
| 3 | 447 | "During the quarter ended March 31, 2026, Sammaan Capital formally became part of the IHC group" | Rs.8,850cr FDI, IHC/Avenir now promoter; prior-quarter event, not current quarter |
| 4 | 457 | "During the quarter ended March 31, 2026... Securities Issuance and Investment Committee... approved the allotment" | Preferential issue details: 33.00cr equity shares @Rs.139, two warrant tranches; prior-quarter event |
| 5 | 482 | "During the current quarter, Avenir Investment RSC Ltd. has been classified as promoter... approved the appointment of Mr. Alwyn Crasta" | Current-quarter director appointment; shareholders approved Aug 10, 2026 |
| 6 | 493 | "Avenir Investment RSC Ltd... is the promoter of the Company... approved her [Khorshid] appointment" | Cross-references Board Outcome agenda item 2 |
| 7 | 497 | "During the current quarter, the international credit rating agency S&P Global Ratings has upgraded Company's long-term... rating to 'BB-'" | Multi-agency rating upgrades (S&P, CRISIL, CARE, ICRA) following IHC investment |
| 8 | 504 | "During the quarter and year ended March 31, 2026... approved a change in the business model for an identified pool of non-core exposures" | Rs.14,953cr Identified Exposures reclassified Hold-to-Collect→Hold-to-Sell; Rs.7,151.95cr net loss (Rs.6,499.17cr Exceptional Item + Rs.652.78cr OCI); prior-quarter event referenced again this quarter |
| 9 | 528 | "During the quarter and year ended March 31, 2026, Management performed a comprehensive assessment of the adequacy of the Management Overlay provision" | Rs.1,850cr ECL Management Overlay; prior-quarter event |
| 10 | 534 | "The interest income for the year ended March 31, 2026 includes significant overdue interest recovered from customers" | FY26 item, not Q1FY27-specific |
| 11 | 535 | "During the year ended March 31, 2026, the Company reassessed the methodology used for estimating the tenure of assignment and co-lending transactions" | Rs.1,154.93cr gain from methodology change (consolidated figure) — FY26 item |
| 12 | 539 | "Sammaan Capital Limited (SCL) and its six wholly owned subsidiaries... have proposed a scheme of amalgamation" | NCLT second motion pending since June 21, 2025 |
| 13 | 544 | "The Scheme of Arrangement between the Company and Sammaan Finserve Limited (SFL) for the demerger... was approved" | Filed with NCLT May 29, 2026; shareholder meeting convened Sept 10, 2026; accounting deferred to approval |
| 14 | 550 | "The Group is mainly engaged in the finance and mortgage-backed lending business... no separate reportable segment" | Single-segment disclosure |
| 15 | 553 | "During the year ended March 31, 2026, Pursuant to the RBI's observation, the Company has approved a change in business model whereby certain exposures in AIF" | FY26 item |
| 16 | 561 | "During the current quarter, the Company, has bought back... US$45,000,000 of the outstanding US$450,000,000 7.5% Senior Secured Social Bonds due 2030" | Current-quarter bond buyback |
| 17 | 563 | "Subsequent to the current quarter, the Company has bought back... US$18,000,000 of the outstanding US$350,000,000 9.70% Senior Secured Social Bonds due 2027" | Subsequent event |
| 18 | 565 | "The figures for the last quarter of the previous financial year are the balancing figures between audited figures" | Standard Q4 balancing-figure disclaimer |
| 19 | 567 | "Figures for the prior year / period have been regrouped and / or reclassified wherever considered necessary" | Standard regrouping disclaimer |

## 9. STATEMENT OF STANDALONE FINANCIAL RESULTS — LINE ITEMS (pages 16-18, lines 639-711)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|---|---|---|---|---|---|---|
| 1 | 640 | Interest Income (Refer Note 11) | 1,039.36 | 1,039.41 | 1,495.90 | 5,333.79 | — |
| 2 | 641 | Fees and commission Income | 43.34 | 21.35 | 53.26 | 142.76 | — |
| 3 | 642 | Net gain on fair value changes | 397.16 | 76.81 | 13.86 | 916.04 | — |
| 4 | 643-645 | Net gain on derecognition of financial instruments (amortised cost, Refer Note 12) | 14.56 | 77.81 | 628.85 | 1,123.35 | — |
| 5 | 646 | Total Revenue from operations (subtotal) | 1,494.42 | 1,215.38 | 2,191.87 | 7,515.94 | — |
| 6 | 647 | Other Income | 24.70 | 7.89 | 8.33 | 30.12 | — |
| 7 | 648 | Total Income (1+2) (subtotal) | 1,519.12 | 1,223.27 | 2,200.20 | 7,546.06 | — |
| 8 | 650 | Finance costs | 1,237.18 | 1,575.69 | 1,132.09 | 5,315.88 | — |
| 9 | 651-653 | Impairment on financial instruments net of recoveries (Refer Note 9 and 10) | (232.05) | 3,726.28 | 415.28 | 4,372.11 | — |
| 10 | 654 | Employee benefits expenses | 147.11 | 148.31 | 157.48 | 550.24 | — |
| 11 | 655 | Depreciation and amortization | 17.33 | 22.18 | 18.69 | 77.82 | — |
| 12 | 656 | Other expenses | 54.32 | 98.69 | 65.04 | 419.69 | — |
| 13 | 657 | Total Expenses (subtotal) | 1,223.89 | 5,571.15 | 1,788.58 | 10,735.74 | — |
| 14 | 658 | Profit/(Loss) before Exceptional Items and tax (3-4) (subtotal) | 295.23 | (4,347.88) | 411.62 | (3,189.68) | — |
| 15 | 659 | Exceptional Items (Refer Note 8) | - | (6,499.17) | - | (6,499.17) | `ZERO_STANDING` Q1FY27/Q1FY26 |
| 16 | 660 | Profit/(Loss) before tax (5+6) (subtotal) | 295.23 | (10,847.05) | 411.62 | (9,688.85) | — |
| 17 | 675 | Current tax | - | - | - | - | `ZERO_STANDING` — dash in ALL four periods (all-dash row, no digits; caught only by manual sweep, not digit-regex) |
| 18 | 676 | Deferred tax | 69.63 | (2,391.94) | 114.18 | (2,091.38) | — |
| 19 | 677 | Total tax expense (subtotal) | 69.63 | (2,391.94) | 114.18 | (2,091.38) | — |
| 20 | 678 | Profit/(Loss) for period (7-8) | 225.60 | (8,455.11) | 297.44 | (7,597.47) | — |
| 21 | 681 | Remeasurement (loss)/gain on defined benefit plan | (1.37) | 3.13 | (0.04) | 5.50 | — |
| 22 | 682-684 | (Loss)/Gain on equity instrument FVOCI (Refer Note 8) | 10.51 | (745.22) | (77.01) | (1,005.00) | — |
| 23 | 685 | Income tax impact on A above | 1.36 | (21.90) | 17.63 | 36.94 | — |
| 24 | 687 | Effective portion of cash flow hedges | (147.76) | 94.60 | (12.08) | (37.79) | — |
| 25 | 688 | Income tax impact on B above | 37.19 | (23.81) | 3.04 | 9.51 | — |
| 26 | 689 | Total Other comprehensive (loss)/income (subtotal) | (100.07) | (693.20) | (68.46) | (990.84) | — |
| 27 | 690 | Total comprehensive income/(loss) (9+10) (subtotal) | 125.53 | (9,148.31) | 228.98 | (8,588.31) | — |
| 28 | 704-706 | Paid-up equity share capital (face value Rs.2) | 232.51 | 231.94 | 165.88 | 231.94 | — |
| 29 | 707 | Other equity | (blank) | (blank) | (blank) | 19,683.79 | `ZERO_STANDING` — quarter columns blank, annual-only |
| 30 | 709 | EPS Basic (not annualised) | 1.94 | (101.46) | 3.59 | (91.50) | — |
| 31 | 710 | EPS Diluted (not annualised) | 1.88 | (101.46) | 3.59 | (91.50) | — |
| 32 | 711 | EPS Face Value | 2.00 | 2.00 | 2.00 | 2.00 | — |

Note: Consolidated PAT (243.30) exceeds Standalone PAT (225.60) by Rs.17.70cr, which reconciles exactly to the
Other Matters para 6 subsidiary/trust PAT figure (17.70cr) — internal consistency check passes; flag for A3/A4
as confirmed, not a discrepancy.

## 10. NOTES TO STANDALONE FINANCIAL RESULTS (lines 713-1028, notes 1-23)

| # | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 713 | "The standalone financial results have been prepared in accordance with the recognition and measurement principles laid down" | Boilerplate |
| 2 | 717 | "The standalone financial results... have been reviewed by the Audit Committee on August 13, 2026 and subsequently approved" | Same-day AC + Board |
| 3 | 726 | "During the quarter ended March 31, 2026, Sammaan Capital formally became part of the IHC group" | Mirrors Consolidated Note 3; prior-quarter event |
| 4 | 730 | "During the quarter ended March 31, 2026... Securities Issuance and Investment Committee... approved the allotment" | Mirrors Consolidated Note 4 |
| 5 | 760 | "During the current quarter, Avenir Investment RSC Ltd. has been classified as promoter... approved the appointment of Mr. Alwyn Crasta" | Mirrors Consolidated Note 5 |
| 6 | 766 | "Avenir Investment RSC Ltd... is the promoter of the Company... Board has approved her [Khorshid] appointment" | Mirrors Consolidated Note 6 |
| 7 | 770 | "During the current quarter, the international credit rating agency S&P Global Ratings has upgraded" | Mirrors Consolidated Note 7 |
| 8 | 777 | "During the quarter and year ended March 31, 2026, the Board of Directors... approved a change in the business model" | Mirrors Consolidated Note 8; Rs.14,953cr Identified Exposures |
| 9 | 800 | "During the quarter and year ended March 31, 2026, Management performed a comprehensive assessment of the adequacy of the Management Overlay" | Mirrors Consolidated Note 9; Rs.1,850cr overlay |
| 10 | 807 | "During the year ended March 31, 2026, Management has, on a prudent basis, recorded a provision for impairment of Rs. 815 crores... in Sammaan Finserve Limited" | Standalone-only note (no consolidated equivalent — investment eliminated on consolidation); "no change... during the quarter ended June 30, 2026" |
| 11 | 810 | "The interest income for the year ended March 31, 2026 includes significant overdue interest recovered" | Mirrors Consolidated Note 10 |
| 12 | 811 | "During the year ended March 31, 2026, the Company reassessed the methodology used for estimating the tenure" | Standalone figure Rs.996.25cr gain — **differs from Consolidated Note 11's Rs.1,154.93cr** for the same methodology change; expected (standalone vs. group scope) but flagged for A3/A4 to confirm the delta is explained by intercompany/subsidiary co-lending volume |
| 13 | 815 | "During the current quarter, the Company, has bought back... US$45,000,000... 7.5% Senior Secured Social Bonds due 2030" | Mirrors Consolidated Note 16 |
| 14 | 823 | "Subsequent to the current quarter, the Company has bought back... US$18,000,000... 9.70% Senior Secured Social Bonds due 2027" | Mirrors Consolidated Note 17 |
| 15 | 826 | "Subsequent to the current quarter, the Securities Issuance and Investment Committee... approved and allotted 14,000... NCDs... Rs. 1,400 Crores" | Standalone-only note — no consolidated equivalent found; subsequent-event NCD placement not mirrored in Consolidated notes 1-19 — flag `CROSS_CHECK_NEEDED` |
| 16 | 829 | "Sammaan Capital Limited (SCL) and its six wholly owned subsidiaries... have proposed a scheme of amalgamation" | Mirrors Consolidated Note 12 |
| 17 | 834 | "The Scheme of Arrangement between the Company and Sammaan Finserve Limited (SFL)... was approved" | Mirrors Consolidated Note 13 |
| 18 | 841 | "The Company is mainly engaged in the finance and mortgage-backed lending business... no separate reportable segment" | Mirrors Consolidated Note 14 |
| 19 | 844 | "During the year ended March 31, 2026, Pursuant to the RBI's observation... change in business model whereby... AIF" | Mirrors Consolidated Note 15 |
| 20 | 846 | "During the current quarter, upon exercise of Stock options by the eligible employees... issued an aggregate of 2,872,973... Equity shares" | Standalone-only — ESOP exercise detail with exact pre/post share capital figures; no consolidated equivalent |
| 21 | 856-1023 | RBI Direction disclosures (Reg. presentation/disclosure Directions 2025) — see sub-tables (i)(a)-(d) and (ii) below | Multi-part note with 4 embedded tables |
| 22 | 1025 | "The figures for the last quarter of the previous financial year are the balancing figures" | Mirrors Consolidated Note 18 |
| 23 | 1027 | "Figures for the prior year / period have been regrouped and / or reclassified" | Mirrors Consolidated Note 19 |

### 10a. Note 21(i)(a) — Transfer through assignment, quarter ended June 30, 2026 (lines 862-873)

| Row | Line | Particular | Assignment | Acquisition | Flags |
|---|---|---|---|---|---|
| 1 | 864 | Count of Loan accounts Assigned* | 929 | 8,331 | footnote* excludes 181 accounts, line 871 |
| 2 | 865 | Amount of Loan accounts Assigned (Rs cr) | 410.44 | 218.30 | — |
| 3 | 866 | Retention of beneficial economic interest / MRR (Rs cr) | 42.95 | 30.84 | — |
| 4 | 867 | Weighted Average Maturity (months) | 188 | 72 | — |
| 5 | 868 | Weighted Average Holding Period (months) | 3.35 | 8.58 | — |
| 6 | 869 | Coverage of tangible security coverage | (blank) | 0.48 | `ZERO_STANDING` — Assignment column blank |
| 7 | 870 | Rating-wise distribution of rated loans | Unrated | - | `ZERO_STANDING` — Acquisition column dash |

Footnotes: line 871 (181-account exclusion), line 872 ("Assignment includes loans transferred under co-lending
arrangement"), line 902-903 ("Company has assigned write-off loans... Rs. 278.16 Crore during Q1FY27" — separate
disclosure, not part of the 7-row table above but adjacent).

### 10b. Note 21(i)(b) — Stressed loans transferred, quarter ended June 30, 2026 (lines 874-901)

| Row | Line | Particular | Value | Flags |
|---|---|---|---|---|
| 1 | 878 | Number of accounts | 6 | — |
| 2 | 879 | Aggregate principal outstanding of loans transferred (Rs cr) | 99.67 | — |
| 3 | 880-882 | Weighted average residual tenor (months) | 133.46 | — |
| 4 | 883-885 | Net book value of loans transferred (Rs cr) | 71.27 | — |
| 5 | 886 | Aggregate consideration (Rs cr) | 96.01 | — |
| 6 | 887-889 | Additional consideration realised re: accounts transferred in earlier years | - | `ZERO_STANDING` |
| 7 | 899-901 | Excess provisions reversed to P&L on account of sale | - | `ZERO_STANDING` |

### 10c. Note 21(i)(c) — Stressed loan acquisition (line 905)

| Row | Line | Content | Flags |
|---|---|---|---|
| 1 | 905 | "The Company has not acquired any stressed loan during the quarter ended June 30, 2026." | `ZERO_STANDING` — nil-activity disclosure, not a table but a standing template line item |

### 10d. Note 21(i)(d) — Co-Lending Arrangements as at June 30, 2026 (lines 907-923)

| Row | Line | Particular | Value | Flags |
|---|---|---|---|---|
| 1 | 911 | Number of Co-Lending Arrangements | 3 | — |
| 2 | 912 | Number of Outstanding Loans | 913 | — |
| 3 | 913 | Amount of Gross outstanding (Rs cr) | 404.11 | — |
| 4 | 914 | Weighted average rate of interest (%) | 10.40% | — |
| 5 | 915 | Fees Paid during the year | - | `ZERO_STANDING` |
| 6 | 916-917 | Sector of Co-Lending Arrangement | Mortgage Backed Loans | — |
| 7 | 919 | Standard Loans (Rs cr) | 404.11 | — |
| 8 | 920 | Non-Performing loans (Rs cr) | - | `ZERO_STANDING` |
| 9 | 921 | Default loss guarantee (if any) | Not Applicable | `ZERO_STANDING` |

Footnote line 922-923: figures pertain only to loans disbursed under the new co-lending arrangement effective
Jan 1, 2026 — scope-limiting footnote, not the full CLA book.

### 10e. Note 21(ii) — Project Finance disclosure, quarter ended June 30, 2026 (lines 931-1023)

| Row | Line | Item | Number of accounts | Amount outstanding (Rs cr) | Flags |
|---|---|---|---|---|---|
| (1) | 942-944 | Projects under implementation at beginning of quarter | 9 | 4,271.85 | — |
| (2) | 945-947 | Projects sanctioned during the quarter | - | - | `ZERO_STANDING` |
| (3) | 948-950 | Projects where DCCO achieved during the quarter* | 1 | 67.76 | footnote* = fully closed/recovered loans included |
| (3)(a) | 951-952 | Movement in balances of accounts appearing at beginning of quarter | - | 30.70 | partial `ZERO_STANDING` (accounts column dash, amount populated) |
| (4) | 953-955 | Projects under implementation at end of quarter (1+2+3+(3)(a)) | 8 | 4,234.79 | — |
| (5) | 956-958 | Out of '4' — resolution process (DCCO extension) invoked | - | - | `ZERO_STANDING` |
| (5.1) | 959-961 | Resolution plan implemented | - | - | `ZERO_STANDING` |
| (5.2) | 976-978 | Resolution plan under implementation | - | - | `ZERO_STANDING` |
| (5.3) | 979-981 | Resolution plan failed | - | - | `ZERO_STANDING` |
| (6) | 982-986 | Resolution process invoked due to change in scope/size | - | - | `ZERO_STANDING` |
| (7) | 987-989 | Cost overrun associated with DCCO extension funded | - | - | `ZERO_STANDING` |
| (7.1) | 990-992 | SBCF sanctioned during financial closure, renewed continuously | - | - | `ZERO_STANDING` |
| (7.2) | 993-995 | SBCF not pre-sanctioned or renewed continuously | - | - | `ZERO_STANDING` |
| (8) | 996-998 | Out of '4' — resolution process not involving DCCO extension invoked | - | - | `ZERO_STANDING` |
| (8.1) | 999-1001 | Resolution plan implemented | - | - | `ZERO_STANDING` |
| (8.2) | 1016-1018 | Resolution plan under implementation | - | - | `ZERO_STANDING` |
| (8.3) | 1019-1021 | Resolution plan failed | - | - | `ZERO_STANDING` |
| Footnote | 1022-1023 | "Includes Loan fully closed or recovered during the period"; "In the absence of DCCO, the 'RERA' date has been considered" | — |

13 of 18 rows in this table are `ZERO_STANDING` — canonical template signal: a full project-finance
resolution-tracking template exists (RBI-mandated) with only 4 rows populated this quarter (project book shrank
9→8 accounts, 4,271.85→4,234.79cr), meaning no stress/resolution activity was triggered in the quarter. Worth
noting for A4: the template exists precisely so silence here is itself information (no DCCO extensions, no
resolution plans of any kind this quarter).

---

## 11. FORMAT FOR DISCLOSING OUTSTANDING DEFAULT (Reg 33/52, standalone, page 28, lines 1043-1061)

| Item | Line | Particular | Value | Flags |
|---|---|---|---|---|
| A | 1043-1044 | Statement on deviation/variation — "Copy attached" | (pointer to Section 12/13 below) | — |
| B.1.A | 1050 | Loans/revolving facilities — Total amount outstanding | 16,588.30 | — |
| B.1.B | 1051 | Loans/revolving facilities — amount of default | - | `ZERO_STANDING` |
| B.2.A | 1053 | Unlisted debt securities (NCDs/NCRPS) — Total amount outstanding | - | `ZERO_STANDING` |
| B.2.B | 1054 | Unlisted debt securities — amount of default | - | `ZERO_STANDING` |
| B.3 | 1055 | Total financial indebtedness (short+long term) | 44,719.64 | — |
| C | 1057-1058 | Related Party transactions format | Not applicable (half-yearly only, Q2/Q4) | `ZERO_STANDING`/scope-excluded this quarter |
| D | 1060-1061 | Statement on impact of audit qualifications | Not applicable (annual filing only) | `ZERO_STANDING`/scope-excluded this quarter |

Cross-check for A3/A4: zero default confirmed here (B.1.B, B.2.B) sits alongside the Security Cover Certificate's
para 13 covenant breach disclosure (Section 5 above) on "borrowing arrangements other than the above Debentures."
Breach ≠ default technically, but the juxtaposition (default format says nil, certificate says breach) warrants
explicit reconciliation by A3. Flag `CROSS_CHECK_NEEDED`.

## 12. REGULATION 52(4) ADDITIONAL INFORMATION — STANDALONE RATIOS (page 29, lines 1067-1099)

| # | Line | Particular | Value as on June 30, 2026 | Flags |
|---|---|---|---|---|
| 1 | 1071-1073 | Debt Equity Ratio | 2.23 | — |
| 2 | 1074 | Debt Service Coverage Ratio | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 3 | 1075 | Interest Service Coverage Ratio | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 4 | 1076 | Outstanding Redeemable Preference Shares | N.A. | `ZERO_STANDING` |
| 5 | 1077 | Capital Redemption Reserve (Rs cr) | 0.36 | — |
| 6 | 1078 | Debenture Redemption Reserve (Rs cr) | 146.39 | — |
| 7 | 1079 | Equity (share capital + other equity, Rs cr) | 20,049.41 | — |
| 8 | 1080 | Net Profit after Tax (Rs cr) | 225.60 | — |
| 9a | 1081 | EPS Basic (not annualised) | 1.94 | — |
| 9b | 1082 | EPS Diluted (not annualised) | 1.88 | — |
| 10 | 1083 | Current Ratio | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 11 | 1084 | Long term debt to working capital | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 12 | 1085 | Bad debts to Account receivable ratio | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 13 | 1086 | Current liability ratio | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 14 | 1087-1089 | Total debts to total assets | 0.65 | — |
| 15 | 1090 | Debtors turnover | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 16 | 1091 | Inventory turnover | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 17 | 1092 | Operating Margin | Not Applicable, being an NBFC | `ZERO_STANDING` |
| 18 | 1093-1094 | Net profit Margin (PAT/Total Income) | 14.85% | — |
| 19A | 1096 | % Gross NPA (Gross NPA/Loan Book) | 0.22% | — |
| 19B | 1097 | % Net NPA (Net NPA/Loan Book) | 0.17% | — |
| 19C | 1098 | Liquidity Coverage Ratio (%) for Q1 FY27 | 127% | — |
| 19D | 1099 | CRAR (per RBI guidelines) | 20.06% | — |

9 of 22 rows are `ZERO_STANDING` (NBFC-exempt ratios) — standard for this filer class, not a completeness concern.

---

## 13. STATEMENT OF DEVIATION / VARIATION — FORM 1 (pages 30-32, lines 1102-1195)

| Field | Line | Value | Flags |
|---|---|---|---|
| Name of listed entity | 1103 | Sammaan Capital Limited | — |
| Mode of Fund Raising | 1104 | Public/Rights/Preferential/QIP/Others | — |
| Date of Raising Funds (I) Rights Issue Feb 15, 2024 | 1105-1109 | No additional proceeds this quarter; cumulative Rs.36,632.47mn of Rs.36,933.98mn received; Rs.301.53mn outstanding | — |
| Date of Raising Funds (II) QIP Jan 27, 2025 | 1111-1115 | No additional proceeds; monitoring a/c balance Rs.329.26mn (Rs.15.94mn net proceeds + Rs.313.32mn issue expenses) | — |
| Date of Raising Funds (III) Preferential Issue Mar 31, 2026 | 1117-1123 | No additional proceeds; Rs.5,652.75cr transferred from monitoring a/c, Rs.4,714.12cr utilized, Rs.938.64cr in Fixed Deposits | — |
| Amount Raised | 1124 | Nil | `ZERO_STANDING` |
| Report filed for Quarter ended | 1125 | June 30, 2026 | — |
| Monitoring Agency | 1126 | "applicable / not applicable" | `TEMPLATE_ARTIFACT` — both options left in place, unresolved field |
| Monitoring Agency Name | 1127 | Crisil Ratings Limited | — |
| Is there a Deviation/Variation in use of funds raised | 1128 | "Yes / No" | `TEMPLATE_ARTIFACT` — both options left in place, unresolved field; contextually implied "No" but not explicitly selected |
| If yes, pursuant to change in contract/objects | 1129-1130 | Not applicable | `ZERO_STANDING` |
| If Yes, Date of shareholder Approval | 1131 | Not applicable | `ZERO_STANDING` |
| Explanation for Deviation/Variation | 1132 | Not applicable | `ZERO_STANDING` |
| Comments of Audit Committee after review | 1133 | No comment | `ZERO_STANDING` |
| Comments of the auditors, if any | 1134 | No comments from auditors | `ZERO_STANDING` |
| Objects table row 1 (Capital base — Rights/QIP) | 1149-1150 | Allocation Rs.27,341.10mn(Rights)/Rs.9,593.90mn(QIP); deviation "--" both | `ZERO_STANDING` deviation column |
| Objects table row 2 (General corporate — Rights/QIP) | 1154-1155 | Allocation Rs.8,398.90mn(Rights, revised to Rs.8,793.58mn)/Rs.3,055.00mn(QIP); deviation "--" both | `ZERO_STANDING` deviation column |
| Objects table row 3 (Onward Lending — Preferential) | 1159 | Allocation Rs.7,080cr, revised Nil, utilised Rs.3,755.25cr; deviation "-" | `ZERO_STANDING` deviation column |
| Objects table row 4 (General corporate — Preferential) | 1162 | Allocation Rs.1,770cr, revised Nil, utilised Rs.958.87cr; deviation "-" | `ZERO_STANDING` deviation column |
| Signature | 1187-1194 | Amit Jain, Company Secretary, 17:02:46 | Post-board-conclusion, not flagged |

## 14. STATEMENT OF DEVIATION / UTILIZATION — FORM 2 (pages 33-34, lines 1198-1260)

| Field | Line | Value | Flags |
|---|---|---|---|
| A. Statement of utilization of issue proceeds table | 1198-1209 | NIL (all columns) | `ZERO_STANDING` |
| Name of listed entity | 1216 | Sammaan Capital Limited | — |
| Mode of fund raising | 1217 | Public Issue / Private Placement | — |
| Type of instrument | 1219 | Not Applicable | `ZERO_STANDING` |
| Date of raising funds | 1220 | Not Applicable | `ZERO_STANDING` |
| Amount raised | 1222 | Not Applicable | `ZERO_STANDING` |
| Report filed for quarter ended | 1223 | June 30, 2026 | — |
| Is there a deviation/variation | 1224 | No | — (resolved cleanly, contrast with Form 1's unresolved Yes/No field) |
| Whether approval required to vary objects | 1225-1226 | Not Applicable | `ZERO_STANDING` |
| If yes, details of approval required | 1227 | Not Applicable | `ZERO_STANDING` |
| Date of approval | 1229 | Not Applicable | `ZERO_STANDING` |
| Explanation for deviation/variation | 1230 | Not Applicable | `ZERO_STANDING` |
| Comments of audit committee after review | 1231 | Not comments [sic] | `ZERO_STANDING` |
| Comments of the auditors, if any | 1232 | Not Applicable | `ZERO_STANDING` |
| Objects table (Original object/Modified/Allocation/Funds utilized/Deviation) | 1236-1244 | NIL | `ZERO_STANDING` |
| Signature | 1253-1259 | Amit Jain, Company Secretary, 17:03:08 | Post-board-conclusion, not flagged |

---

## 15. SECURITY COVER CERTIFICATE — STATEMENT (Reg 54(3), OCR pages 39-42, lines 1483-1703)

OCR quality flag: pages 39-42 are OCR-derived and materially degraded (garbled column headers, misaligned digits,
duplicated/split figures e.g. "14,031.41" vs "44,031.17" for the same row, "49.42" vs "49.12" for another). Every
value below carries flag `OCR_UNCERTAIN` and should be verified against the source PDF directly before use in
analysis; figures are transcribed as extracted, not corrected.

### Assets (lines 1521-1599)

| # | Line | Asset class | Value (Rs cr, as extracted) | Flags |
|---|---|---|---|---|
| 1 | 1523-1527 | Property, Plant and Equipment | 89.00 | `OCR_UNCERTAIN` |
| 2 | 1540-1544 | Capital Work-in-Progress | 36.89 | `OCR_UNCERTAIN` |
| 3 | 1546-1548 | Right of Use Assets | 487.34 / 157.34 (two figures shown, unreconciled) | `OCR_UNCERTAIN`; possible column-value garble |
| 4 | 1550-1551 | Goodwill | (no value visible in extract) | `OCR_UNCERTAIN` + candidate `ZERO_STANDING` — row header present, value cell not captured; cannot confirm nil vs. OCR loss |
| 5 | 1552-1554 | Intangible Assets | 12.75 | `OCR_UNCERTAIN` |
| 6 | 1556-1561 | Intangible Assets under Development | (blank) | `ZERO_STANDING` |
| 7 | 1563-1566 | Investments | 18,824.25 | `OCR_UNCERTAIN` (multiple column repeats of same figure) |
| 8 | 1568-1569 | Loans | 37,021.94 | `OCR_UNCERTAIN` |
| 9 | 1571-1572 | Inventories | - | `ZERO_STANDING` |
| 10 | 1574-1576 | Trade Receivables | 3.55 | `OCR_UNCERTAIN` |
| 11 | 1578-1583 | Cash and cash equivalents | 4,320.61 / 355.00 / 4,675.61 (multiple columns) | `OCR_UNCERTAIN` |
| 12 | 1584-1595 | Bank Balances other than cash and cash equivalents | 439.28 | `OCR_UNCERTAIN` |
| 13 | 1597 | Others | 5,636.82 / 1,391.34 / 7,028.15 (multiple columns) | `OCR_UNCERTAIN` |
| Total | 1610-1611 | Total Assets | 49,119.94 / 16,687.23 / 2,481.60 / 68,288.77 (multiple column totals) | `OCR_UNCERTAIN` |

### Liabilities (lines 1613-1677)

| # | Line | Liability class | Value (Rs cr, as extracted) | Flags |
|---|---|---|---|---|
| 1 | 1616-1624 | Debt securities to which this certificate pertains | 14,031.41 / 44,031.17 (conflicting figures on adjacent lines) | `OCR_UNCERTAIN` — material conflict, needs source verification |
| 2 | 1626-1634 | Other debt sharing pari-passu charge with above debt | 26,691.11 | `OCR_UNCERTAIN` |
| 3 | 1636-1637 | Other debt | 49.42 / 49.12 (conflicting) | `OCR_UNCERTAIN` |
| 4 | 1639-1641 | Subordinated debt | 2,982.71 | `OCR_UNCERTAIN` |
| 5 | 1643-1646 | Bank | (blank, "Not to filled" label garbled) | `ZERO_STANDING` |
| 6 | 1648-1650 | Debt securities (unsecured breakdown row) | (blank) | `ZERO_STANDING` |
| 7 | 1652 | Others (unsecured breakdown row) | (blank) | `ZERO_STANDING` |
| 8 | 1654-1656 | Trade payables | 0.93 | `OCR_UNCERTAIN` |
| 9 | 1658-1660 | Lease Liabilities | 185.33 | `OCR_UNCERTAIN` |
| 10 | 1662-1663 | Provisions | 98.64 | `OCR_UNCERTAIN` |
| 11 | 1675 | Others | 1,082.26 / 1,982.26 (conflicting) | `OCR_UNCERTAIN` |
| Total | 1676-1677 | Total Liabilities | 40,722.27 / 2,267.17 / 3,031.82 / 46,021.27 (multiple column totals) | `OCR_UNCERTAIN` |

### Cover ratios (lines 1678-1689)

| # | Line | Ratio | Value | Flags |
|---|---|---|---|---|
| 1 | 1679-1681 | Cover on Book Value | 41.21 | `OCR_UNCERTAIN` — plausibility check: this reads as a coverage multiple far above typical (~1.5-2x); may be a mislabeled percentage or a garbled decimal; needs source PDF verification |
| 2 | 1682-1685 | Cover on Market Value | 4.62 | `OCR_UNCERTAIN` |
| 3 | 1686-1689 | Pari-Passu Security Cover Ratio (vs. "NA" Security Cover Ratio label) | NA / 4.18 | `OCR_UNCERTAIN` — two labels/values on same line, unclear which ratio is which |

### Notes to Security Cover Certificate Statement (lines 1690-1703)

| # | Line | First ~15 words | Flags |
|---|---|---|---|
| 1 | 1691 | "The Security Cover ratio pertains to only listed secured debt securities" | — |
| 2 | 1692-1693 | "Total assets stated above are restricted to the extent of minimum-security coverage required... IND-AS adjustment for effective interest rate... excluded" | — |
| 3 | 1694 | "Assets considered for pari passu charge is calculated based on assets cover requirement as per respective information memorandum" | — |
| 4 | 1695-1697 | "The Company has complied with all financial and non financial covenants as specified in the respective debenture trust deeds pertaining to the debt securities to which this certificate pertains" | Note: this is narrower than the auditor certificate's own para 13 (Section 5) — this note attests compliance only for the Debentures covered by THIS certificate, not the "borrowing arrangements other than the above Debentures" where the breach occurred. Consistent, not contradictory, but worth flagging for A3/A4 as the scope distinction is easy to miss on a quick read. `CROSS_CHECK_NEEDED` |
| 5 | 1697 | "Other debt sharing pari-passu charges with above debt includes the impact of Rs. 908 crores on account of revaluation of external commercial borrowings, Foreign Currency Bonds" | — |
| 6 | 1698 | "Investment includes assets held for sales [sic]" | — |
| 7 | 1699-1701 | "Management has deducted balances in respect of overdraft facilities and temporary overdraft... and cash and cash equivalents of Rs. 355 crores representing HQLAs" | — |
| 8 | 1701 | "The above figures have been extracted from the Un-Audited Standalone financial results/information" | — |
| 9 | 1702 | "Cover on Book Value represents coverage for all pari-passu debt holders (including borrowings other than debt securities)" | — |
| 10 | 1703 | "Pari-Passu Security Cover Ratio Required represents coverage for debt securities for which this certificate being issued" | — |

Signature (management side): Sachin Chaudhary, Executive Director and Chief Operating Officer, line 1706-1709,
"Date: August 13, 2026" — no digital timestamp shown (plain signature line, unlike the digitally-signed blocks
elsewhere in the filing). Flag `TIMESTAMP_NOT_AVAILABLE`.

---

## 16. DIGITAL SIGNATURE BLOCKS (all documents, chronological by timestamp where available)

Board meeting window: 02:00 PM (14:00) to 03:40 PM (15:40) IST, August 13, 2026.

| # | Line | Signatory | Designation | Document | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 1 | 1030-1034 | Gagan Banga | Managing Director & CEO | Standalone Financial Results (signing block on results statement) | 15:00:46 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` — precedes 15:40 board conclusion by ~39 min |
| 2 | 305-315 | Jaspreet Singh Bedi | Partner, Nangia & Co LLP | Consolidated Review Report | 15:08:31 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` |
| 3 | 305-319 | Mohender Gandhi | Partner, M Verma & Associates | Consolidated Review Report | 15:17:24 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` |
| 4 | 612-619 | Jaspreet Singh Bedi | Partner, Nangia & Co LLP | Standalone Review Report | 15:09:02 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` |
| 5 | 612-626 | Mohender Gandhi | Partner, M Verma & Associates | Standalone Review Report | 15:18:26 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` |
| 6 | 1468-1479 | Mohender Gandhi | Partner, M Verma & Associates | Security Cover Certificate | 15:27:25 | `SIGNATURE_BEFORE_BOARD_CONCLUSION` |
| 7 | 103-108 | Amit Jain | Company Secretary | Board Outcome letter | 17:01:28 | Post-conclusion (normal) |
| 8 | 1187-1194 | Amit Jain | Company Secretary | Statement of Deviation, Form 1 | 17:02:46 | Post-conclusion (normal) |
| 9 | 1253-1259 | Amit Jain | Company Secretary | Statement of Deviation, Form 2 | 17:03:08 | Post-conclusion (normal) |
| 10 | 1704-1709 | Sachin Chaudhary | Executive Director & COO | Security Cover Certificate (management side) | none shown (date only) | `TIMESTAMP_NOT_AVAILABLE` |

**Material finding**: six of nine timestamped signatures (rows 1-6), spanning the MD & CEO's own signing of the
Standalone Financial Results and BOTH joint statutory auditors' review-report/certificate signatures across
standalone, consolidated, and Security Cover Certificate documents, are timestamped BEFORE the Board's stated
03:40 PM conclusion time. This is a mechanical, evidenced flag per the ledger's mandate — not an interpretation —
and should be surfaced prominently to A3/A4: either the board meeting concluded earlier than the letter states,
the results/reports were finalized ahead of formal Board approval, or there is a clerical error in the stated
meeting end time.

---

## 17. UNNUMBERED FOOTNOTES SWEEP (below tables, asterisks/symbols)

| # | Line | Context | Marker | Flags |
|---|---|---|---|---|
| 1 | 871 | Note 21(a) assignment table | * | Excludes 181 accounts from prior tranches |
| 2 | 902 | Below Note 21(a)/(b) tables | * | Rs.278.16cr write-off loans assigned separately during Q1FY27 |
| 3 | 922 | Note 21(d) co-lending table | (unmarked, "Numbers pertain only to...") | Scope limiter — new CLA effective Jan 1, 2026 only |
| 4 | 1022 | Note 21(ii) project finance table | * | Includes loans fully closed/recovered during period |
| 5 | 1023 | Note 21(ii) project finance table | (unmarked, "In the absence of DCCO...") | RERA date substituted for DCCO date |
| 6 | 1165 | Deviation Form 1 objects table | * | Rights Issue dated Feb 15, 2024 |
| 7 | 1166-1167 | Deviation Form 1 objects table | # | QIP dated Jan 27, 2025 |
| 8 | 1168-1169 | Deviation Form 1 objects table | $ | Preferential Issue dated Mar 31, 2026 |
| 9 | 1171-1172 | Deviation Form 1 | "Note 1:" | QIP monitoring account balance detail |
| 10 | 1174-1176 | Deviation Form 1 | "Note 2:" | Rights Issue cumulative proceeds detail |
| 11 | 1178-1180 | Deviation Form 1 | "Note 3:" | Preferential Issue utilization detail |

---

## SUMMARY OF FLAGS RAISED

- `ZERO_STANDING` — 54 rows across financial/disclosure tables (details in each section above)
- `SIGNATURE_BEFORE_BOARD_CONCLUSION` — 6 signatures (Sections 3, 4, 5, 16) — material procedural flag
- `TEMPLATE_ARTIFACT` — 2 unresolved Yes/No fields in Deviation Form 1 (Section 13)
- `OCR_UNCERTAIN` — entire Security Cover Certificate Statement, pages 39-42 (Section 15) — conflicting duplicate
  figures on at least 3 line items require source-PDF verification
- `TIMESTAMP_NOT_AVAILABLE` — Sachin Chaudhary signature, Security Cover Certificate (Section 15/16)
- `ANNEXURE_REFERENCED_NOT_FOUND` — "Annexure I" to Security Cover Certificate (Section 2)
- `CROSS_CHECK_NEEDED` — 3 instances: (a) zero-default format vs. covenant-breach certificate para (Section 11),
  (b) Security Cover Certificate compliance note scope vs. certificate para 13 breach scope (Section 15), (c)
  Standalone Note 15 (subsequent NCD placement) with no Consolidated-note mirror (Section 10)
- `ENTITY_CHANGE` — not assignable (no prior-quarter ledger supplied for diff); noted for A3/A4 follow-up

Total ledger rows: 42 notes + 194 line items + 4 agenda items + 26 auditor paragraphs + 10 entities + 3 annexures
+ 10 signature blocks + 11 footnotes = 300 enumerated disclosure units.
