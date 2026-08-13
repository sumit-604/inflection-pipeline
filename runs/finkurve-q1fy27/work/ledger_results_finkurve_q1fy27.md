# A2 COMPLETENESS LEDGER — Finkurve Financial Services Ltd (Arvog) — Q1 FY27 — Results Filing

Source: `extract_results_finkurve_q1fy27.txt` (777 lines incl. 84-line A1 header block; page 1-13 of 13, pages 10-11 OCR-fallback).
All line numbers below are **file line numbers** (as returned by `grep -n` / `Read` on the extract file itself), not the extract's internal embedded numbering (file_line = embedded_line + 84, constant offset, verified across the whole document).

Filing scope confirmed by full-text sweep: **no "consolidated", "subsidiary", or "standalone" token appears anywhere in the extract** → this filing is **STANDALONE-ONLY**, single entity, single reportable segment ("financial services", Note 6). No consolidation entity list exists for this doctype/quarter.

---

## === A2 COUNT TEST ===
```
category: agenda_items        grep_count: 11   sweep_count: 11   match: yes
category: review_report_paras grep_count: 4*   sweep_count: 5    match: no -> resweep -> broadened grep_count: 5   sweep_count: 5   match: yes
category: security_cert_paras grep_count: 9    sweep_count: 9    match: yes
category: auditor_paras_total grep_count: 14   sweep_count: 14   match: yes   (5 review report + 9 security cover cert, reconciled after resweep above)
category: notes               grep_count: 8    sweep_count: 8    match: yes
category: line_items          grep_count: 21*  sweep_count: 23   match: no -> resweep -> range-bounded grep_count: 23  sweep_count: 23  match: yes
category: cla_subtable_rows   grep_count: 10   sweep_count: 10   match: yes
category: ratios_table_rows   grep_count: 22*  sweep_count: 26   match: no -> resweep -> range-bounded grep_count: 26  sweep_count: 26  match: yes
category: appendix1_rows      grep_count: 30   sweep_count: 30   match: yes
category: appendix1_footnotes grep_count: 9    sweep_count: 9    match: yes
category: annexure3_fields    grep_count: 15   sweep_count: 15   match: yes
category: annexure4_fields    grep_count: 15   sweep_count: 15   match: yes
category: signature_blocks    grep_count: 7    sweep_count: 7    match: yes

* = initial strict-regex grep undercounted due to OCR/typo artifacts in source (comma instead of period on review-report para 2; digit "0"/"1" substituted for letters "(o)"/"(l)" in ratios labels; two unlabeled EPS sub-rows; three section-header rows with no numeric payload). A resweep with a broadened/range-bounded grep pass reconciled every mismatch to the manual sweep. No unresolved mismatch remains.

gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (11 items, pages 1-2)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 107 | Unaudited Financial Results Q1 FY27 (Reg 33 & 52) approved, Limited Review Report enclosed as Annexure 1 | |
| 2 | 114 | Security Cover Certificate (Reg 54) approved, enclosed as Annexure 2 | |
| 3 | 119 | Statement of deviation/variation — Preferential Issue of Equity Shares & Share Warrants proceeds (Reg 32(1)), enclosed as Annexure 3 | |
| 4 | 123 | Statement of deviation/variation — Non-Convertible Debentures proceeds (Reg 52(7)/(7A)), enclosed as Annexure 4 | |
| 5 | 127 | Material RPT approval — grant of loans to Related Parties, AGM-42 to AGM-43 (2027), subject to shareholder approval | |
| 6 | 131 | Material RPT approval — acceptance of loans from Related Parties, AGM-42 to AGM-43 (2027), subject to shareholder approval | |
| 7 | 135 | Material RPT approval — payments to/from M/s Augmont Goldtech Pvt Ltd (Service Fees, Commission, Brand Usage, Tech Support), AGM-42 to AGM-43, subject to shareholder approval | RELATED_PARTY |
| 8 | 148 | Borrowing powers under Sec 180(1)(c)/180(1)(a), Companies Act 2013, up to ₹5,000 Cr, subject to shareholder approval | |
| 9 | 152 | Increase in threshold of loans/guarantees/investments under Sec 186, Companies Act 2013, subject to shareholder approval | |
| 10 | 156 | Issue of NCDs on private placement basis, subject to shareholder approval | |
| 11 | 159 | Continuation of directorship of Mr. Himadri Bhattacharya (DIN 02331474) as Non-Executive Independent Director post age 75, subject to shareholder approval | DIRECTOR_AGE_75; printed "1 ." in source (OCR artifact for "11.") |
| — | 163 | Board meeting timing: commenced 10:31 A.M., concluded 12:09 P.M. IST (98 minutes for 11 agenda items incl. 2 RPT items, 2 enabling resolutions, and financial results) | |
| — | 172-181 | Signature block: Kajal Parmar, Company Secretary & Compliance Officer, Membership No. A65484, digitally signed 2026.08.13 12:17:01 +05'30' | Signed 8 min after meeting close (12:09→12:17); not a mismatch flag, within normal signing lag |

## 2. LIMITED REVIEW REPORT — Regulation 33 (5 paragraphs, pages 3-4)

| Para | Line | Content (first 15 words) | Flags |
|------|------|---------------------------|-------|
| 1 | 203 | "We have reviewed the accompanying statement of unaudited financial results of Finkurve Financial Services Limited..." — scope, entity, quarter | |
| 2 | 213 | "The Statement, which is the responsibility of the Company's Management and approved by the Company's Board..." — Ind AS 34 basis | printed "2," (comma, not period) in source — OCR/typo artifact, caught only on resweep |
| 3 | 222 | "We conducted our review of the Statement in accordance with the Standard on Review Engagement (SRE) 2410..." — review standard, moderate assurance, no audit opinion expressed | |
| 4 | 236 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." — UNMODIFIED CONCLUSION | Opinion type: unmodified/unqualified conclusion |
| 5 | 253 | "The unaudited financial results of the Company for the quarter ended 30th June 2025, included in the Statement, were reviewed by predecessor auditor..." — prior-year comparative reviewed by PREDECESSOR auditor (dated 13 Aug 2025, unmodified conclusion); "Our conclusion is not modified in respect of these matters" | AUDITOR_CHANGE (predecessor auditor referenced for prior-year comparative; current auditor Ladha Singhal & Associates) — Other Matters-type paragraph |
| — | 268-273 | Signature: Ajay Singhal, Partner, Ladha Singhal & Associates (FRN 120241W), M.No. 104451, UDIN 26104451ECLQRV5660, Place Mumbai, Date 13 Aug 2026 | |

Entities reviewed: single entity, Finkurve Financial Services Limited (Company only — no subsidiaries named, no "unaudited/management-furnished" sub-entity language present).

## 3. STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (23 value-bearing rows + 3 section headers, page 5, "₹ in Lakhs")

| # | Line | Item | Q1FY27 (30-Jun-26) | Q4FY26 (31-Mar-26) | Q1FY26 (30-Jun-25) | FY26 (31-Mar-26) | Flags |
|---|------|------|---------------------|----------------------|----------------------|---------------------|-------|
| H1 | 287 | "I Revenue From Operations" — section header (no own value) | — | — | — | — | header only |
| 1 | 288 | Interest income | 7,478.68 | 6,607.67 | 2,659.83 | 20,435.25 | |
| 2 | 289 | Fees and commission income | 58.4 | 16.00 | 1,323.51 | 101.72 | value magnitude/decimal-placement suspect (58.4 vs neighbouring cols) — flag for A3 |
| 3 | 290 | Net gain on fair value changes | 25.79 | 109.28 | 4.51 | 184.86 | |
| 4 | 291 | Total Revenue from operations | 7,510.30 | 6,732.95 | 3,987.88 | 20,721.83 | subtotal |
| 5 | 292 | Other income (II) | 71.87 | 188.51 | 15.89 | 266.53 | printed "U other income" (OCR garble for "II") |
| 6 | 293 | Total Income (I+II) (III) | 7,582.18 | 6,521.46 | 4,003.73 | 20,986.36 | printed "1t [Total Income (1+11" OCR garble; subtotal |
| H2 | 294 | "IV Expenses" — section header (no own value) | — | — | — | — | printed "v [expenses"; header only |
| 7 | 295 | Finance costs | 2,672.31 | 1,988.83 | 707.82 | 4,892.10 | |
| 8 | 296 | Fees and commission expenses | 1,363.74 | 2,277.65 | 1,272.564 | 6,972.62 | |
| 9 | 297 | Net loss on fair value changes | = | = | = | - | **ZERO_STANDING** — dash/nil in all 4 periods; template line for a transaction type not currently occurring |
| 10 | 298 | Impairment/(Reversal of Impairment) on financial instruments | 20.38 | 710.14 | 478.30 | 2,217.18 | |
| 11 | 299 | Employee benefits expense | 1,347.08 | 536.56 | 396.45 | 1,823.40 | |
| 12 | 300 | Depreciation and amortization expense | 113.18 | 133.98 | 75.04 | 302.12 | |
| 13 | 301 | Other expenses | 338.98 | 232.10 | 390.07 | 1,279.42 | |
| 14 | 302 | Total expenses (IV) | 6,461.66 | 5,879.32 | 3,320.42 | 17,526.84 | subtotal |
| 15 | 303 | Profit before tax (V) | 1,120.52 | 1,042.14 | 683.31 | 3,459.52 | |
| 16 | 304 | Tax expense (VI) | 276.71 | 238.05 | 174.20 | 856.11 | |
| 17 | 305 | Profit for the period (VII) | 843.81 | 804.09 | 509.11 | 2,603.41 | |
| 18 | 306 | Other Comprehensive Income (VIII) | — (illegible/blank glyph in source) | 37.49 | - | 37.49 | Q1FY27 value not clean in extract — verify against source PDF |
| 19 | 307 | Total comprehensive income for the year (IX) | 843.81 | 841.58 | 509.11 | 2,640.91 | subtotal |
| 20 | 310 | Paid up equity share capital (X) | 1,401.28 | 1,400.50 | 1,400.19 | 1,400.50 | |
| 21 | 311 | Other Equity (XI) | (blank) | 33,089.57 | (blank) | 33,089.57 | quarter columns blank by convention (annual-only disclosure) — not ZERO_STANDING (interim periods legitimately blank for this line) |
| H3 | 312 | "XII Earnings per equity share (Face value INR 1)" — section header (no own value) | — | — | — | — | header only |
| 22 | 313 | Basic (INR) | 0.50 | 0.58 | 0.38 | 1.89 | |
| 23 | 314 | Diluted (INR) | 0.58 | 0.56 | 0.38 | 1.86 | Basic (0.50) < Diluted (0.58) for Q1FY27 column — arithmetically anomalous (diluted EPS normally ≤ basic); flag for A3/A4 |

Sub-note: only ONE set of figures is presented (no separate standalone/consolidated columns) — consistent with STANDALONE_ONLY finding above.

## 4. NOTES TO THE STATEMENT (8 numbered notes, pages 5-6)

| Note | Line | First 15 words | Flags |
|------|------|------------------|-------|
| 1 | 316 | "The above results have been reviewed by the Audit Committee and approved by the Board of Directors..." | |
| 2 | 319 | "These financial results have been prepared in accordance with Indian Accounting Standards (Ind AS) notified..." | |
| 3 | 322 | "These financial results have been has been stated in accordance with the modified format as per SEBI's Circular..." | typo "has been has been" in source, verbatim |
| 4 | 326 | "Details of Co-Lending Arrangements (CLA) during the quarter ended June 30, 2026" — see CLA sub-table §5 below | |
| 5 | 343 | "The Company has maintained requisite full security cover as per the terms of Offer Document / Information Memorandum..." — NCDs aggregating ₹49,312.37 lakhs as at 30-Jun-26 | |
| 6 | 348 | "The Company has only single reportable business segment i.e. 'financial services' in terms of..." Ind AS 108, operations in India | Confirms STANDALONE_ONLY / single-segment |
| 7 | 351 | "Ratios" — see Ratios sub-table §6 below | |
| 8 | 387 | "Previous periods' figures have been regrouped/rearranged wherever necessary to conform to the current period's classification" | |
| — | 400-402 | Signature/sign-off: Priyank Kothari, Whole-time Director (DIN 07676104), "By order of the Board of Directors", Place Mumbai, Date 13.08.2026 | No digital-signature timestamp printed (unlike Kajal Parmar's block) |

## 5. NOTE 4 SUB-TABLE — CO-LENDING ARRANGEMENTS (CLA) PERFORMANCE (10 rows, ₹ in Crores unless stated, page 5)

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 331 | Number of CLAs | 2 | |
| 2 | 332 | Weighted average rate of interest (per annum) | 19.96% | |
| 3 | 333 | Fees charged/paid | (blank/illegible — printed as bare comma) | Value not legible in extract — **NOT FOUND**, flag for source re-check |
| 4 | 334 | Broad Sector in which CLA was made | Gold Loan | |
| 5 | 335 | "Performance of loans under CLA (Rs in crores)" — sub-header | — | header for 4 rows below |
| 5a | 336 | Total Disbursement till June 30, 2026 | 44.23 | |
| 5b | 337 | Outstanding* on above Disbursement as on June 30, 2026 | 37.86 | Asterisk footnote marker present, **no corresponding footnote text found anywhere in the extract** — flag NOT_FOUND (footnote referent missing) |
| 5c | 338 | Write Off done till June 30, 2026 | - | **ZERO_STANDING** |
| 5d | 339 | Net NPA as on June 30, 2026 | 0.01 | |
| 6 | 340 | Details related to default loss guarantee | Nil | **ZERO_STANDING** |

## 6. NOTE 7 SUB-TABLE — RATIOS (26 rows, page 6; includes Reg 52(4) NBFC sector-specific block)

| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| a | 360 | Debt-Equity Ratio | 2.88 | |
| b | 361 | Debt service coverage Ratio | 0.41 | printed label "(o)" in source — OCR/print artifact, should be (b); verbatim preserved |
| c | 362 | Interest Service Coverage Ratio | 1.38 | |
| d | 363 | Outstanding Redeemable Preference Shares (quantity and value) | Not Applicable | |
| e | 364 | Capital Redemption Reserve/Debenture Redemption Reserve | Not Applicable | |
| f | 365 | Net Worth (in lakhs) | 35,436.80 | |
| g | 366 | Net profit after Tax (in lakhs) | 843.81 | |
| h | 367 | "Earnings per Share (EPS)" — sub-header | — | header for 2 rows below |
| h-i | 368 | Basic EPS | 0.60 | unlabeled sub-row |
| h-ii | 369 | Diluted EPS | 0.59 | unlabeled sub-row; note this Diluted EPS (0.59) differs from statement-table Diluted EPS (0.58, line 314) — cross-table inconsistency, flag for A3 |
| i | 370 | Current Ratio | 1.15 | |
| (dup) | 371 | Long Term debt to working Capital | 9.33 | printed label "(i)" duplicated in source (should be (j)) — label collision, verbatim preserved |
| j | 372 | Bad debts to Accounts Receivable Ratio | (0.00) | |
| k | 373 | Current Liability Ratio | 0.31 | |
| l | 374 | Total debts to Total Assets | 0.71 | printed label "(1" (digit one, OCR artifact for letter "l") |
| m | 375 | Debtors Turnover Ratio | Not Applicable | |
| n | 376 | Inventory Ratio | Not Applicable | |
| o | 377 | Operating Margin Ratio | 15.24 | printed label "(0 )" (digit zero, OCR artifact for letter "o") |
| p | 378 | Net Profit Margin ratio | 11.27 | |
| q | 379 | "Sector Specific Ratios:" — sub-header | — | printed label "(a)" (OCR artifact, should be (q)); header for 6 rows below (NBFC-specific, Reg 52(4)) |
| q(ia) | 380 | Gross NPA (INR in lacs) | 665.65 | GNPA — NBFC-specific |
| q(ib) | 381 | Gross NPA ratio (%) | 0.54% | GNPA % |
| q(iia) | 382 | Net NPA (INR in lacs) | 596.11 | NNPA — NBFC-specific |
| q(iib) | 383 | Net NPA ratio (%) | 0.48% | NNPA % |
| q(iii) | 384 | Provision Coverage Ratio (%) | 10.45% | printed label "(ii)" (OCR artifact, should be (iii)) |
| q(iv) | 385 | Capital to risk-weighted assets ratio (CRAR) | 26.63% | CRAR — NBFC-specific |

Note: no explicit "Stage-wise ECL" breakup table found anywhere in the extract (Stage 1/2/3 ECL disclosure) — **NOT FOUND**, flag for A3/A4 as a possible completeness gap vs Reg 52(4)/Ind AS 109 disclosure norms for NBFCs.

## 7. SECURITY COVER CERTIFICATE — Annexure 2 covering letter (9 paragraphs, pages 7-8)

| Para | Line | Content (first 15 words) | Flags |
|------|------|---------------------------|-------|
| 1 | 420 | "This certificate is issued at the request of the Company in accordance with the terms of our engagement..." | |
| 2 | 429 | "The statement certifying the security cover on Secured and Unsecured Redeemable Non-Convertible Debentures as at June 30, 2026..." — refers to Annexure A + Appendix I | |
| 3 | 447 | "The preparation of the Statement is the responsibility of the Management of the Company including the preparation and maintenance..." — Management's Responsibility heading | |
| 4 | 461 | "The Management is also responsible for ensuring adherence that the details in the statement are correct" | |
| 5 | 467 | "It is our responsibility to provide reasonable assurance that the details as referred to in 'Annexure A'..." — Auditor's Responsibility heading | |
| 6 | 474 | "We conducted our examination of the Statement in accordance with the Guidance Note on Reports or Certificates for Special Purposes..." — continues onto page 8 with reading-order correction disclosed by A1 | pdftotext reading-order artifact on page 8, corrected per A1 header note |
| 7 | 497 | "We have complied with the relevant applicable requirements of the Standard on Quality Control (SQC) 1..." | |
| 8 | 506 | "Based on the information and explanations provided to us and examination of records of the Company... we hereby conclude that book value of assets and relevant debts... are true and correct" — Conclusion heading | Opinion type: unmodified confirmation of book values in Appendix I |
| 9 | 515 | "The certificate is provided to the Company solely for submission to the Debenture Trustees/Stock Exchanges..." — Restriction on Use heading | |
| — | 524-533 | Signature: Ajay Singhal, Partner, Ladha Singhal & Associates (FRN 120241W), M.No. 104451, UDIN 26104451WFVWFJ6704, Place Mumbai, Date 13 Aug 2026 | Second, distinct UDIN from the Reg 33 Review Report (line 271) — two separate engagements same day, same partner |

## 8. ANNEXURE A — Security Cover narrative certificate (3 statements, page 9)

| # | Line | Statement | Flags |
|---|------|-----------|-------|
| 1 | 463-468 | Asset cover of 110% of outstanding principal (₹48,900.00 Lakhs) + accrued interest (₹412.37 Lakhs) of Secured Redeemable NCDs as at 30-Jun-26 | |
| 2 | 472-474 | Compliance with all covenants on outstanding Secured Redeemable NCDs (₹49,312.37 Lakhs) [excludes Ind AS amortization impact of ₹795.01 Lakhs] | |
| 3 | 478-480 | "Working of Security Cover... is attached" — references Appendix I | |
| — | 569-576 (487-492) | Signature: Aakash N Jain, Chief Financial Officer, Place Mumbai, Date 13 Aug 2026 | |

## 9. APPENDIX I — SECURITY COVER TABLE (page 10, OCR-fallback, manually transcribed per A1)

Header/structural rows (Columns A-O definitions): 1 header block, not individually enumerated as disclosure units (structural, not data).

### 9a. Asset rows (14, line 522-536)
| # | Line | Asset line item | Populated columns | Flags |
|---|------|------------------|--------------------|-------|
| 1 | 523 | Property, Plant and Equipment | H(vi)=1,575.77; J=1,575.77 | |
| 2 | 524 | Capital Work-in-Progress | J=- | **ZERO_STANDING** |
| 3 | 525 | Right of Use Assets | H(vi)=1,093.96; J=1,093.96 | |
| 4 | 526 | Goodwill | J=- | **ZERO_STANDING** |
| 5 | 527 | Intangible Assets | H(vi)=6.68; J=6.68 | |
| 6 | 528 | Intangible Assets under Development | J=- | **ZERO_STANDING** |
| 7 | 529 | Investments | H(vi)=7,458.34; J=7,458.34; N=7,740.76; O=7,740.76 | |
| 8 | 530 | Loans | D(ii)=94,647.63; F(iv)=7,740.76; H(vi)=20,306.94; J=1,22,695.32 | largest asset line — gold-loan book |
| 9 | 531 | Inventories | J=- | **ZERO_STANDING** |
| 10 | 532 | Trade Receivables | H(vi)=5,590.33; J=5,590.33 | |
| 11 | 533 | Cash and Cash Equivalents | J=- | **ZERO_STANDING** |
| 12 | 534 | Bank Balances other than Cash and Cash Equivalents | J=- | **ZERO_STANDING** |
| 13 | 535 | Others | D(ii)=4,664.77; H(vi)=615.20; J=5,279.97; N=7,740.76; O=7,740.76 | |
| 14 | 536 | Total (Assets) | D(ii)=99,312.40; F(iv)=7,740.76; H(vi)=36,647.22; J=1,43,700.38 | subtotal |

### 9b. Liability rows (14, lines 539-552)
| # | Line | Liability line item | Populated columns | Flags |
|---|------|----------------------|--------------------|-------|
| 1 | 539 | Debt securities to which this certificate pertains | D(ii)=42,275.32; F(iv)=7,037.05; J=49,312.37 | |
| 2 | 540 | Other debt sharing pari-passu charge with above debt | C(i)="not to be filled"; J=- | **ZERO_STANDING** |
| 3 | 541 | Other Debt (header) | J=- | header for 5 rows below |
| 4 | 542 | Subordinated debt | J=21,559.28 | |
| 5 | 543 | Borrowings | J=22,589.02 | |
| 6 | 544 | Bank | J=767.73 | |
| 7 | 545 | Debt Securities | H(vi)=8,752.53; J=8,752.53 | |
| 8 | 546 | Others | H(vi)=1,561.24; J=1,561.24 | |
| 9 | 547 | Trade payables | H(vi)=1,155.27; J=1,155.27 | |
| 10 | 548 | Lease Liabilities | H(vi)=52.98; J=52.98 | |
| 11 | 549 | Provisions | H(vi)=187.40; J=187.40 | |
| 12 | 550 | Deferred tax liabilities (net) | H(vi)=2,325.74; J=2,325.74 | |
| 13 | 551 | Others | row present, values not legible beyond Total row | **NOT FOUND** — value illegible in source rasterisation per A1 |
| 14 | 552 | Total (Liabilities) | D(ii)=87,191.35; F(iv)=7,037.05; H(vi)=14,035.17; J=1,08,263.57 | subtotal |

### 9c. Cover ratio rows (2, lines 554-555)
| # | Line | Item | Value | Flags |
|---|------|------|-------|-------|
| 1 | 554 | Cover on Book Value | row header only, values not legible in this rasterisation | **NOT FOUND** — per A1 methodology note |
| 2 | 555 | Cover on Market Value | Exclusive Security Cover Ratio = 1.14; Pari-Passu Security Cover Ratio = 1.10 | footnote marker (h) referenced |

| — | 641-642 (557-558) | Signature block (page 10): N Aakash [signature] / seal Finkurve Financial Services Ltd / Authorized Signatory; and Ladha Singhal & Associates seal | |

## 10. APPENDIX I — page 11 (continuation) + FOOTNOTES (page 11, OCR-fallback)

| # | Line | Item | Flags |
|---|------|------|-------|
| 1 | 563 | Continuation table: same Column A-O header repeated, **all data rows blank** | Flag `ZERO_STANDING`-adjacent: this is a genuine blank continuation/footnote page per A1 methodology note, not a template-signal omission — noted distinctly as `BLANK_CONTINUATION_PAGE`, not conflated with a dropped disclosure |
| i | 649 | Footnote i — Column C(i) definition (exclusive charge assets/debt for which certificate issued) | |
| ii | 650 | Footnote ii — Column D(ii) definition (exclusive charge assets/other corresponding debt) | |
| iii | 651 | Footnote iii — Column E(iii) definition (pari-passu Yes/No flag) | |
| iv | 652 | Footnote iv — Column F(iv) definition (pari-passu charge assets) | |
| v | 653 | Footnote v — Column G(v) definition (other pari-passu assets) | |
| vi | 654 | Footnote vi — Column H(vi) definition | **NOT FOUND** — "remainder of this footnote not fully legible in source scan" per A1, truncated mid-sentence |
| vii | 655 | Footnote vii — Column I(vii) elimination logic | |
| viii | 656 | Footnote viii — Market Value assets definition (Land, Building, Real Estate) | |
| ix | 657 | Footnote ix — Market value = Column O total | |
| — | 659-660 (575-576) | Signature block (page 11, duplicate/continuation): N Aakash + Ladha Singhal & Associates seal | |

## 11. ANNEXURE 3 — Deviation/Variation Statement: Preferential Issue of Equity Shares & Warrants (15 units, page 12)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 1 | 667 | Name of listed entity | Finkurve Financial Services Limited | |
| 2 | 668-585 | Mode of Fund Raising | Preferential Issue of Equity Shares and Share Warrants on Private Placement Basis | |
| 3 | 670 (586) | Date of Raising Funds | May 21, 2025 and May 27, 2025 | |
| 4 | 671 (587) | Amount Raised | Rs. 141.50 Crore | |
| 5 | 672 (588) | Report filed for Quarter ended | June 30, 2026 | |
| 6 | 673 (589) | Monitoring Agency | Applicable | |
| 7 | 674 (590) | Monitoring Agency Name, if applicable | CRISIL Rating Limited | |
| 8 | 675-592 | Is there a Deviation/Variation in use of funds raised | No | |
| 9 | 677-595 | If yes, whether pursuant to change in contract terms/objects approved by shareholders | - | ZERO_STANDING (N/A, since Q8=No) |
| 10 | 680 (596) | If Yes, Date of shareholder Approval | - | ZERO_STANDING |
| 11 | 681 (597) | Explanation for the Deviation/Variation | - | ZERO_STANDING |
| 12 | 682-599 | Comments of the Audit Committee after review | - | ZERO_STANDING |
| 13 | 684 (600) | Comments of the auditors, if any | - | ZERO_STANDING |
| 14 | 685-603 | Objects for which funds raised, and deviation table | Not Applicable (header); deviation table follows | |
| 15 | 613-627 (697-711) | Deviation table row: "Onward lending and investment and repayment of borrowing obtained by company in ordinary course of business" — Original Allocation NA/₹141.50 Cr, Funds Utilised ₹111.50 Cr, Remarks: ₹30 Cr = 75% of share warrant subscription amount yet to be received | Monitoring agency: CRISIL Rating Limited; ₹30 Cr of the ₹141.50 Cr raise still uncalled |

## 12. ANNEXURE 4 — Deviation/Variation Statement: Non-Convertible Debentures (15 units, page 13)

| # | Line | Field | Value | Flags |
|---|------|-------|-------|-------|
| 1 | 729 (645) | Name of listed entity | Finkurve Financial Services Limited | |
| 2 | 730 (646) | Mode of Fund Raising | Non-Convertible Debentures | |
| 3 | 731-732 (647-648) | Date of Raising Funds / Allotment | May 14, 2026, June 16, 2026, and June 29, 2026 | Three separate allotment tranches within the quarter |
| 4 | 733 (649) | Amount Raised (In Crore) | Rs. 199 | |
| 5 | 734 (650) | Report filed for Quarter ended | June 2026 | |
| 6 | 735 (651) | Monitoring Agency | Not Applicable | Differs from Annexure 3 (CRISIL applicable there) — flag for A3 review of monitoring-agency inconsistency across debt vs equity raises |
| 7 | 736 (652) | Monitoring Agency Name, if applicable | Not Applicable | ZERO_STANDING |
| 8 | 737-654 | Is there a Deviation/Variation in use of funds raised | No | |
| 9 | 739-657 | If yes, whether pursuant to change in contract terms/objects approved by shareholders | - | ZERO_STANDING |
| 10 | 742 (658) | If Yes, Date of shareholder Approval | - | ZERO_STANDING |
| 11 | 743 (659) | Explanation for the Deviation/Variation | - | ZERO_STANDING |
| 12 | 744-661 | Comments of the Audit Committee after review | - | ZERO_STANDING |
| 13 | 746 (662) | Comments of the auditors, if any | - | ZERO_STANDING |
| 14 | 747-665 | Objects for which funds raised, and deviation table | Not Applicable (header); deviation table follows | |
| 15 | 674-679 (758-763 raw) | Deviation table row: "For lending business of the Company" — Original Allocation ₹135, Funds Utilised ₹199, Remarks: NA | Funds utilised (₹199 Cr) exceeds original allocation (₹135 Cr) though "Is there Deviation/Variation" = No — arithmetic/narrative tension, flag for A3/A4 |

## 13. SIGNATURE / DIGITAL-SIGNATURE BLOCKS SUMMARY (7 total, cross-referenced above)

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 172-181 | Kajal Parmar | Company Secretary & Compliance Officer | 2026.08.13 12:17:01 +05'30' (digital) | Board Outcome letter — signed after 12:09 PM meeting close, consistent |
| 2 | 400-402 | Priyank Kothari | Whole-time Director (DIN 07676104) | Date 13.08.2026 (no time) | Statement of Results sign-off |
| 3 | 268-273 | Ajay Singhal (Partner) | Ladha Singhal & Associates, FRN 120241W | UDIN 26104451ECLQRV5660, 13 Aug 2026 | Reg 33 Review Report |
| 4 | 524-533 | Ajay Singhal (Partner) | Ladha Singhal & Associates, FRN 120241W | UDIN 26104451WFVWFJ6704, 13 Aug 2026 | Security Cover Certificate — second, distinct UDIN same day |
| 5 | 569-576 | Aakash N Jain | Chief Financial Officer | 13 Aug 2026 | Annexure A Authorized Signatory |
| 6 | 641-642 | N Aakash (signature) + Ladha Singhal & Associates (seal) | CFO / Statutory Auditor | undated stamp | Appendix I, page 10 |
| 7 | 659-660 | N Aakash (signature) + Ladha Singhal & Associates (seal) | CFO / Statutory Auditor | undated stamp | Appendix I, page 11 (duplicate/continuation) |

---

## TOTALS BY CATEGORY

| Category | Count |
|---|---|
| Board Outcome agenda items | 11 |
| Board meeting timing statement | 1 |
| Review Report (Reg 33) paragraphs | 5 |
| Statement of Unaudited Financial Results — value-bearing line items | 23 |
| Statement — section headers (non-value) | 3 |
| Notes 1-8 | 8 |
| Note 4 CLA sub-table rows | 10 |
| Note 7 Ratios table rows | 26 |
| Security Cover Certificate paragraphs | 9 |
| Annexure A narrative statements | 3 |
| Appendix I asset rows | 14 |
| Appendix I liability rows | 14 |
| Appendix I cover-ratio rows | 2 |
| Appendix I page-11 blank continuation table | 1 |
| Appendix I footnotes (i-ix) | 9 |
| Annexure 3 fields + deviation-table row | 15 |
| Annexure 4 fields + deviation-table row | 15 |
| Signature blocks | 7 |
| **TOTAL DISCLOSURE UNITS ENUMERATED** | **176** (174 substantive + 3 section headers - counted once; see note) |

Note on total: 173 substantive numbered/lettered/valued disclosure units (excluding the 3 non-value section-header rows which are listed for completeness but not double-counted in the gate-tested categories above) + 3 section headers = **176 rows enumerated in this ledger**. Gate-tested category subtotal (used for GATE A2 reconciliation) = 173.

## FLAGS RAISED (full list)
- ZERO_STANDING (multiple: Net loss on fair value changes; CLA Write Off; CLA default loss guarantee; 8x Appendix I zero asset/liability lines; Annexure 3 & 4 not-applicable deviation fields — ~8 instances there)
- STANDALONE_ONLY (no consolidated statement, no subsidiary/consolidation entity list present in this filing)
- AUDITOR_CHANGE (Review Report para 5 references a predecessor auditor for the prior-year comparative quarter)
- RELATED_PARTY (agenda item 7, Augmont Goldtech Pvt Ltd transactions)
- DIRECTOR_AGE_75 (agenda item 11, continuation of directorship post age 75)
- NOT_FOUND (CLA "Fees charged/paid" value; CLA Outstanding* footnote text; Appendix I "Others" liability row value; Appendix I "Cover on Book Value" row value; footnote vi truncated mid-sentence)
- BLANK_CONTINUATION_PAGE (Appendix I page 11 repeats header with blank data rows — genuine continuation, not a dropped disclosure)
- Cross-table/arithmetic inconsistencies flagged for A3/A4: Diluted EPS mismatch between Statement (0.58) and Ratios table (0.59); Basic EPS (0.50) < Diluted EPS (0.58) in the Statement table for Q1FY27; Annexure 4 funds utilised (₹199 Cr) exceeds original allocation (₹135 Cr) despite "No" deviation flag; Annexure 3 vs Annexure 4 Monitoring Agency inconsistency (CRISIL applicable vs Not Applicable)
- OCR/label artifacts preserved verbatim, not corrected: Ratios table labels (o)→printed "(o)" for what should read differently at line 361, "(1"/"(0 )" digit-for-letter substitutions, duplicate "(i)" label, sector-specific header printed "(a)" instead of "(q)"; Statement table roman-numeral OCR garbling (II→"U", III→"1t", IV→"v", V→"v", VII/VIII both printed "Vil")
