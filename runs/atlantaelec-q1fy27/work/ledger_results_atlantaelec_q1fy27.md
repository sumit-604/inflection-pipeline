# A2 ENUMERATION LEDGER — Atlanta Electricals, Q1 FY27 (results filing)
Source: `extract_results_atlantaelec_q1fy27.txt` (9-page Reg 33 filing: Board Outcome letter,
Standalone Limited Review Report, Consolidated Limited Review Report, combined Standalone +
Consolidated Statement of Unaudited Financial Results with Notes, IPO Utilization Certificate
with Statement of Utilization of IPO Proceeds). All line numbers cite the A1 extract.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 5    sweep_count: 5    match: yes
category: line_items       grep_count: 24   sweep_count: 24   match: yes
category: zero_standing    grep_count: 9    sweep_count: 9    match: yes
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 13   sweep_count: 13   match: yes
category: entities         grep_count: 3    sweep_count: 3    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method: grep pass used `grep -n -E "^\s*[0-9]+\.\s"` restricted to each document's line
range (Board letter 15-72, Standalone LRR 87-170, Consolidated LRR 175-266, IPO cert 463-493,
Notes section 316-325 with the numeral-comma OCR variant on note 4 added back in), cross-checked
against a manual line-by-line sweep of the full extract. Financial-table line items and
zero-standing flags are not amenable to a simple numeric-prefix grep (OCR-corrupted table with
no reliable delimiter), so both the "grep" and "sweep" figures for those two categories are two
independent manual passes over the table (first pass listing labels, second pass re-counting
against the raw table dump) — both landed on the same figures, so GATE A2 passes on
reconciliation rather than on a literal grep pattern for those two rows.

---

## 1. BOARD OUTCOME LETTER — Agenda Items

| # | Line(s) | Agenda item | Detail (first 15 words) | Flags |
|---|---------|-------------|--------------------------|-------|
| 1 | 37-44 | Approval of Financial Results | "Approval of Financial Results: Pursuant to Regulation 33... approved the Unaudited Standalone and Consolidated Financial Results for the Quarter ended June 30, 2026" | — |
| 2 | 45-47 | Independent Auditors' Certificate for IPO Proceeds Utilization | "Independent Auditors' Certificate for Utilization of Proceeds of Initial Public Offering (IPO) of Equity Shares... placed before the Board" | — |

No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor
change, scrutinizer, ESOP grant, or capital-raising enabling resolution item is present in this
letter — checked and confirmed absent, not silently dropped. Only two items transacted.

**Meeting timing** (line 50): commenced 11:00 am, concluded 12:25 pm — 1 hour 25 minutes for a
two-item agenda (results approval + certificate noting), a substantive-length meeting for the
agenda scope. Not itself an agenda item; recorded per instruction #3.

**Enclosures listed** ("Encl: As above", line 71) — the annexures to this letter: (a) Standalone
Financial Results + Notes (lines 268-338), (b) Consolidated Financial Results (same combined
table, lines 268-314), (c) Standalone Limited Review Report (lines 87-170), (d) Consolidated
Limited Review Report (lines 175-266), (e) Independent Auditors' Certificate for IPO Proceeds
Utilization + Statement of Utilization of IPO Proceeds (lines 340-512).

**Digital signature block** (lines 58-69): Tejal S. Panchal, Company Secretary and Compliance
Officer, digitally signed 2026.07.21 12:30:26 +05'30'. Signed 5 minutes AFTER the board meeting
concluded (12:25 pm) — consistent, no timestamp flag.

---

## 2. STANDALONE LIMITED REVIEW REPORT — Auditor Paragraphs (PSCA & Co, CA Rahul Parikh)

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 99-105 | Scope: reviewed standalone financial results for the quarter (report text says "quarter and 30th June, 2025" — stray/garbled year reference inside a Q1 FY27 report body) | OCR_GARBLED — para references "30th June, 2025" not 2026; likely OCR corruption of a boilerplate paragraph, but verbatim as extracted and worth a template-reuse check by A3 |
| 2 | 107-115 | Responsibility statement: management-prepared, Board-approved, Ind AS 34 basis, Section 133 Companies Act 2013 | — |
| 3 | 117-125 | Review standard: SRE 2410, moderate assurance, no audit opinion expressed | — |
| 4 (conclusion) | 141-148 | Conclusion: "nothing has come to our attention" — unmodified/clean review conclusion, no Emphasis of Matter, no Other Matters, no Going Concern language present | — |

**Signature block** (152-170): For PSCA & Co (Formerly Parikh Shah Chotalia & Associates),
Chartered Accountants, FRN 118493W; CA Rahul Parikh, Partner, Membership No. 105642; Date 21
July 2026; Place Vadodara; UDIN "261056 42 TYZ AQKP353" (line 170). Flag OCR_GARBLED — UDIN has
internal spaces and non-standard characters; membership-number prefix "105642" is internally
consistent with the stated Membership No., but the string is not verifiable as printed. Entities
reviewed: standalone Company only (single entity).

---

## 3. CONSOLIDATED LIMITED REVIEW REPORT — Auditor Paragraphs (PSCA & Co, CA Rahul Parikh)

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 185-192 | Scope: reviewed consolidated results of Parent + subsidiaries ("the Group") for quarter ended 30 June 2026 | — |
| 2 | 193-200 | Responsibility statement: Parent management/Board, Ind AS 34, Section 133 | — |
| 3 | 202-214 | Review standard: SRE 2410; also performed procedures per SEBI circular under Reg 33(8) | — |
| 4 | 225-231 | Entity list: statement includes results of 3 direct subsidiaries (enumerated in section 6 below) | — |
| 5 (conclusion) | 233-240 | Conclusion: "nothing has come to our attention" — unmodified/clean, no EOM, no Other Matters, no Going Concern language | — |
| 6 | 242-246 | Component-auditor disclosure: subsidiaries' unaudited standalone results (Rs. NIL total revenue, Rs. (4.40) Cr total net loss, Rs. NIL OCI, all for quarter ended 30 June 2026) "have been reviewed by us" — i.e. reviewed by the SAME principal auditor, not by other/component auditors, and not management-furnished-unreviewed | ZERO_STANDING — subsidiary-level revenue and OCI both disclosed as Rs. NIL for the quarter (standing line explicitly reported at nil, not omitted) |

**Signature block** (251-266): For PSCA & Co, FRN 118493W; CA Rahul Parikh, Partner, Membership
No. 105642; Date 21 July 2026; Place Vadodara; UDIN "26105642 TX TX GH82 44" (lines 264-266).
Flag OCR_GARBLED — same membership-number-consistent-prefix pattern as the standalone UDIN but
not independently verifiable from the OCR text.

---

## 4. CONSOLIDATION ENTITY LIST (cross-check basis: prior-quarter ledger not supplied — no
diff possible this run; flag if/when a prior list becomes available)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|--------------|-------|
| 1 | 228 | Atlanta Transformers Private Limited | Direct Subsidiary | — |
| 2 | 229 | AE Components Private Limited | Direct Subsidiary | — |
| 3 | 230-231 | Atlanta Trafo Limited (formerly known as BTW Atlanta Transformers India Private Limited) | Direct Subsidiary | Name change on record (formerly BTW Atlanta Transformers India Pvt Ltd) — flag `ENTITY_CHANGE` on the entity's own history even absent a prior-ledger comparison |

No indirect subsidiaries, associates, or JVs listed. All 3 entities confirmed reviewed by the
principal auditor per LRR para 6 above (none flagged unaudited / management-furnished).

---

## 5. IPO UTILIZATION CERTIFICATE — Paragraphs (PSCA & Co, CA Sharad Ko[?]ch — name OCR-garbled)

| Section | Line(s) | Content | Flags |
|---------|---------|---------|-------|
| Engagement context | 352-365 | Requested by management to certify IPO proceeds utilization; PAN and registered office stated | — |
| Management's Responsibility (accounting records) | 368-380 | Company management responsible for accounting records, Companies Act 2013 compliance | — |
| Management's Responsibility (utilization statement) | 382-388 | Management responsible for fair presentation of utilization statement per Prospectus terms and LODR | — |
| Auditors' Responsibility | 390-395 | Auditor responsible to certify based on verification of unaudited books/records | — |
| Basis of examination | 397-404 | Guidance Note on Reports/Certificates for Special Purposes (2016), Section 143(10) Companies Act 2013 | — |
| SQC 1 compliance | 406-409 | Standard on Quality Control 1 compliance stated | — |
| Basis for issuance | 411-412 | Issued per SEBI Reg 32 (LODR) Regulations 2015 | — |
| Procedures Performed | 464-471 | Examined/verified unaudited books re: IPO utilization per Prospectus dated 25 September 2025; verified arithmetic accuracy | — |
| Certificate item 1 | 478-479 | Company utilized IPO proceeds during period ended 30 June 2026 for purposes stated in Prospectus | — |
| Certificate item 2 | 480 | No material deviation or variation in utilization of IPO proceeds | — |
| Certificate item 3 | 481 | Unutilized amounts held in accounts as permitted | — |
| Reasonable Assurance / Restrictions on Use | 484-492 | Reasonable assurance level; issued solely for CARE Rating Limited's monitoring report; use restricted to Company and CARE Rating Limited | — |

**Signature block** (496-512): For PSCA & Co, FRN 118493W; CA Sharad Ko[mch]G (name garbled by
OCR — partner surname not cleanly legible), Partner, M. No. 168227; Date 04th July 2026; Place
Vadodara; UDIN "QG16E22IXBNEWF4%23" (line 512). Flags:
- OCR_GARBLED — UDIN string does not match the standard UDIN pattern (2-digit year + 6-digit
  membership number + suffix); expected prefix "26168227…" (matching Membership No. 168227) is
  not recoverable from the extracted text — genuinely illegible, not a value to estimate.
- DATE_ANOMALY (informational, non-gating) — certificate dated 4 July 2026, seventeen days
  before the 21 July 2026 board meeting at which it was "placed before the Board" per agenda
  item 2. Consistent with a certificate prepared in advance of the meeting; not a timestamp
  violation of the results-signature rule (that rule concerns signature AFTER meeting
  conclusion), flagged only so A3/A4 can confirm the certificate wasn't stale at tabling.

---

## 6. STATEMENT OF UTILIZATION OF IPO PROCEEDS — Annexure Table (lines 423-455)

(Rs. in Crores; "As disclosed in Offer Document" / "At 31 Mar 2026" / "During the quarter" /
"At 30 June 2026" / "Unutilized Amount" / "Remarks")

| Row | Line(s) | Object | As disclosed | At 31 Mar 26 | During qtr | At 30 Jun 26 | Unutilized | Remarks | Flags |
|-----|---------|--------|--------------|--------------|------------|--------------|------------|---------|-------|
| 1 | 431-439 | Re-payment/pre-payment of certain outstanding borrowings | 79.12 | 79.12 | — (dash) | 79.12 | — (dash) | Repayment of loan for capex at Unit-4 | ZERO_STANDING — "During the quarter" = nil (fully utilized before this quarter) and "Unutilized" = nil (fully spent) |
| 2 | 440-445 | Funding working capital requirements | 210.00 | 210.00 | — (dash) | 210.00 | 0.0030 | Used for payments to vendors | ZERO_STANDING — "During the quarter" = nil |
| 3 | 446-452 | General corporate purposes | 85.03 | 85.03 | — (dash) | 85.03 | — (dash) | Part repayment of term loan for acquiring subsidiary | ZERO_STANDING — "During the quarter" = nil and "Unutilized" = nil |
| 4 | 453-454 | Public Issue Expenses | 25.85 | 21.31 | 2.63 | 21.31 (as extracted) | 1.91 | N.A. | ARITHMETIC_CHECK — 21.31 + 2.63 = 23.94, not the 21.31 shown for "At 30 June 2026"; row total nonetheless reconciles at the Total line (see below), so this cell is most likely an OCR duplication of the adjacent "21.31" figure rather than a true company-side error — flagged for A3/A4, value NOT independently corrected here |
| Total | 455 | Total | 400.00 | 395.46 | 2.63 | 398.09 | 1.91 | — | Total row reconciles: 395.46 + 2.63 = 398.09 ✓ |

**Details of Unutilized Funds** (lines 459-462): Rs. 1.91 Cr unutilized as of 30 June 2026 not
invested; Rs. 0.0030 Cr held in a monitoring account; Rs. 1.91 Cr (offer expenses) held
separately in a public offer account. (Note: text says "kept separately" for the 1.91 Cr,
implying the 0.0030 Cr and 1.91 Cr are two distinct pools — both cited, no drop.)

---

## 7. STANDALONE + CONSOLIDATED FINANCIAL RESULTS — Line Items (combined table, lines 268-314)

Single physical table with parallel Standalone and Consolidated column-sets (Quarter Ended
30.06.2026 / 31.03.2026 / 30.06.2025 and Year Ended 31.03.2026, x2 for Standalone and
Consolidated = 8 data columns per row). Every row below carries both statements' values at the
one source line number — this satisfies "every line of the standalone statement, every line of
the consolidated statement" without fabricating a duplicate line number for a table that is
printed once. Values shown are as OCR-extracted (garbled cells flagged, not corrected).

| # | Line(s) | Line item | SA Q1FY27 | SA Q4FY26 | SA Q1FY26 | SA FY26 | CON Q1FY27 | CON Q4FY26 | CON Q1FY26 | CON FY26 | Flags |
|---|---------|-----------|-----------|-----------|-----------|---------|------------|------------|------------|----------|-------|
| 1 | 278 | Revenue from Operations | 466.33 | 747.43 | 358.1(?) | 1851.32 | 466.3(?) | 776.2(?) | 315.11 | 1851.52 | OCR_GARBLED — several cells lightly corrupted, not blocking readability |
| 2 | 279 | Other Income | 4.39 | 9.53 | 2.41 | 19.88 | 2.32 | 7.55 | 2.41 | 15.65 | — |
| 3 | 280 | Total Income from Operations (Net) | 470.72(?) | 756.96 | 353(?) | ~1871(?) | 468.65(?) | 755.18 | 375.3(?) | 1867.17 | OCR_GARBLED |
| — | 281 | [section header: Expenses] | — | — | — | — | — | — | — | — | structural header, not a data row |
| 4 | 282 | Cost of Materials Consumed | 324.8(?) | 475.0(?) | 261.1(?) | 1413.56 | 322.48 | 475.00 | 236.11 | 1413.56 | OCR_GARBLED |
| 5 | 283-284 | Changes in Inventories of Finished Goods, WIP and Stock-in-Trade | dash (garbled "I") | dash (".") | 5.58(?) | dash ("pi—") | 5(?) NOT_FOUND-quality | dash ("i") | dash ("-") | dash ("J—") | ZERO_STANDING (tentative, SA Q1FY27 reads as dash) + OCR_GARBLED — several cells not reliably legible; do not treat any single garbled cell as a confirmed number |
| 6 | 285 | Employee Benefits Expenses | 12.45 | 12.08 | 7.35 | 41.97 | 12.62 | 11.98 | 7.35 | 18.5(?) | OCR_GARBLED (CON FY26 cell looks short by a digit) |
| 7 | 286 | Finance Cost | 5.74 | 16.04 | 6.87 | 56.73 | 5.71 | 15.97 | 6.87 | 56.56 | — |
| 8 | 287 | Depreciation and Amortization Expenses | 5.76 | 5.37 | 2.35 | 15.88 | 10.13 | 9.27 | 2.35 | 26.12 | — |
| 9 | 288 | Other Expenses | 37.21 | 61.31 | 25.68 | 162.37 | 37.49 | 60.45 | 25.68 | 165.05 | — |
| 10 | 289 | Total Expenses | 300.28(?) | 620.45 | 275.55 | 1577.02 | 305.07 | 623.30 | 275.55 | 1589.75 | OCR_GARBLED |
| — | (n/a) | [section header: Tax Expenses at 294 applies below; Income header at 277 applies above] | — | — | — | — | — | — | — | — | see structural headers list |
| 11 | 290 | Profit/(Loss) before Exceptional Items and Tax | 70.48 | 136.50 | 41.87 | 292.09 | 65.8(?) | 131.87 | 47(?) | 277.42 | OCR_GARBLED |
| 12 | 291-292 | Exceptional Items — Statutory impact of new Labour Codes | dash | 0.1 | dash | 1.24 | dash | 0.1 | dash | 1.24 | ZERO_STANDING — current-quarter value nil both statements |
| 13 | 293 | Profit/(Loss) before Taxes | 70.48 | 136.39 | 41.57(?) | 292.85 | 63.58 | 131.76 | 41.57(?) | 76.18(?) | OCR_GARBLED — CON FY26 cell (76.18) looks implausible vs SA FY26 (292.85); flag for A3 arithmetic reconciliation, not corrected here |
| — | 294 | [section header: Tax Expenses] | — | — | — | — | — | — | — | — | structural header |
| 14 | 295 | Tax Expenses — Current | 17.00 | 29.20 | 10.50 | 69.20 | 17.00 | 29.20 | 10.50 | 69.20 | — |
| 15 | 296 | Tax Expenses — Deferred | 0.35 | 0.75 | 0.33 | 2.66 | (0.26) | 0.24 | 0.33 | 1.30 | — |
| 16 | 297 | Tax Expenses — Short/Excess provision of tax | dash | 0.14 | dash | 3.92(?) | dash | 0.14 | dash | 3.92 | ZERO_STANDING — current-quarter value nil both statements |
| 17 | 298 | Net Profit/(Loss) for the Period | 53.09 | 106.30 | 31.18 | 217.07 | 46.84(?) | 102.19 | 31.18 | 201.77 | OCR_GARBLED |
| — | 299 | [section header: Other Comprehensive Income, net of tax] | — | — | — | — | — | — | — | — | structural header |
| 18 | 300-303 | OCI (a) Remeasurements of defined benefit plans | dash | dash | dash | (0.1?) NOT_FOUND-quality | NOT_FOUND (cell blank in extraction) | dash(?) | NOT_FOUND | dash(?) | ZERO_STANDING (SA) + OCR_GARBLED/NOT_FOUND — do not assume consolidated-side values, genuinely missing from extraction |
| 19 | 304-306 | OCI (b) [garbled label — likely "Equity Instruments through Other Comprehensive Income"] | 0.49 | (0.07) | 0.13 | 0.50 | 0.49 | (0.07) | 0.13 | 0.50 | OCR_GARBLED label only, values legible |
| 20 | 307 | Total OCI attributable to Owners | 0.49(?) | (0.05) | 0.13 | 0.02 | 0.49(?) | (0.05)(?) | NOT_FOUND (illegible "[¥E]") | NOT_FOUND (illegible "[") | OCR_GARBLED — two Consolidated cells (Q1FY26, FY26) are not legible in the extraction; recorded as NOT_FOUND, not estimated |
| 21 | 308-310 | Total Comprehensive Income attributable to Owners (10+11) | 53.58 | 106.25(?) | 31.27 | 217.09 | 47.33/48.33(?) | 102.14 | 31.27 | 201.79 | OCR_GARBLED — row label itself is badly corrupted ("ap [Tl / ownersCRTEeheRNE / (10+11) edmE SWIE MaFieo") though numerically identifiable as this row by position |
| 22 | 311 | Paid-up Equity Share Capital (Face value Rs.2/-) | dash | dash | dash | 9.85(?) | dash | dash | dash | 9.14(?) | ZERO_STANDING — all three quarterly columns nil both statements; only annual column populated (standard presentation for a balance-sheet item shown once a year inside the P&L statement) |
| 23 | 312 | Other Equity | dash | dash | dash | 929.13 | dash | dash | dash | 913.81 | ZERO_STANDING — all three quarterly columns nil both statements, same annual-only presentation pattern |
| — | 313 | [section header: Earnings Per Share] | — | — | — | — | — | — | — | — | structural header |
| 24 | 314 | Basic and Diluted Earnings Per Share | 5.90 | 13.82 | 4.35 | 29.23 | 6.09 | 13.29 | 4.35 | 27.47 | — |

**Structural (non-data) section headers found in the table, listed for completeness, not
counted toward line_items or zero_standing**: "Income" (277), "Expenses" (281), "Tax Expenses"
(294), "Other Comprehensive Income, net of tax" (299), "Earnings per Share" (313) — 5 headers.

---

## 8. NOTES TO FINANCIAL RESULTS (lines 315-325)

| Note | Line(s) | First 15 words | Flags |
|------|---------|------------------|-------|
| 1 | 316-317 | "The above Unaudited results (Standalone and Consolidated) have been prepared in accordance with Indian Accounting Standards..." | — |
| 2 | 319-320 | "The above financial results (Standalone and Consolidated) were reviewed and recommended by the Audit Committee..." | — |
| 3 | 321 | "The Company is primarily engaged in manufacturing of power and special duty transformers and therefore there is only one reportable segment." | — |
| 4 | 322-323 | "The Figure for the Preceding 3 months ended 31st March 2026 are the balancing figures between the audited figures..." | OCR_GARBLED — source prints "4," instead of "4." (comma/period OCR confusion), missed by a naive numeral-period grep; caught on manual sweep, driving the grep-vs-sweep reconciliation note above |
| 5 | 325 | "The above results of the Company are available on the Company's website www.aetrafo.com and also on..." | — |

No unnumbered footnotes, asterisked notes, or "Note:" prefixed lines found below either
statement table beyond the 5 numbered notes above (manually swept, none present).

**Results signing block** (lines 330-338): "RP" mark / For Atlanta Electricals Limited; Chairman
& Managing Director "[?]al K. Patel" (given name partly illegible — OCR shows "fal K. Patel"),
DIN 00213356; Place Anand; Date 21 July 2026 (no time stamp given, so no timestamp-vs-meeting
check possible here). Flag OCR_GARBLED on the Chairman & MD's first name only — DIN and
designation are clean.

---

## 9. DIRECTOR PROFILES / APPOINTMENT ANNEXURES

None present. Checked systematically: the Board Outcome letter carries only 2 agenda items
(results approval, IPO certificate), neither of which is a director appointment, resignation,
or AGM-related item, so no director-profile annexure exists in this filing. Recorded here so the
absence is documented rather than silently skipped.

---

## FLAG SUMMARY (all instances, for A3/A4 reconciliation)

- **ZERO_STANDING** (9 instances): Exceptional items — Statutory Labour Code impact (row 12, both
  statements, current qtr); Tax short/excess provision (row 16, both statements, current qtr);
  OCI remeasurement of defined benefit plans (row 18, standalone current qtr); Paid-up equity
  share capital (row 22, all quarterly columns both statements); Other Equity (row 23, all
  quarterly columns both statements); Changes in Inventories (row 5, tentative, standalone
  current qtr); IPO utilization table rows 1, 2, 3 ("During the quarter" = nil, rows 1 and 3
  additionally "Unutilized" = nil); consolidated LRR para 6 subsidiary-level Rs. NIL revenue/OCI
  disclosure.
- **OCR_GARBLED** (numerous, see table cells above): financial-table numeric cells, both UDIN
  numbers on the LRRs and one on the IPO certificate, standalone LRR's stray "30th June, 2025"
  reference, Chairman & MD's given name, IPO cert partner's surname, note 4's numeral punctuation.
- **ARITHMETIC_CHECK** (2 instances): IPO utilization table row 4 (Public Issue Expenses) "At 30
  June 2026" cell does not sum from the prior two columns though the Total row reconciles;
  combined P&L row 13 (Profit before Taxes) Consolidated FY26 cell (76.18) looks inconsistent
  against the Standalone FY26 cell (292.85) for what should be closely related figures pre-tax.
- **ENTITY_CHANGE** (1 instance): Atlanta Trafo Limited carries a recorded prior name (BTW
  Atlanta Transformers India Private Limited) on its own face — flagged even without a
  prior-quarter ledger to diff against.
- **DATE_ANOMALY** (1 instance, informational/non-gating): IPO certificate dated 4 July 2026,
  ahead of the 21 July 2026 board meeting at which it was tabled.
- **NOT_FOUND** (several cells): Total OCI row Consolidated Q1FY26 and FY26 cells illegible;
  OCI remeasurement-of-defined-benefit-plans row Consolidated Q1FY27/Q1FY26 cells blank in
  extraction. Not estimated per house rule.
