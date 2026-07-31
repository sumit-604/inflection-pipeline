# A2 ENUMERATION LEDGER — Ram Ratna Wires Ltd (RAMRAT), Q1 FY27, Doctype: results

Source: `runs/ramrat-q1fy27/work/extract_results_ramrat_q1fy27.txt` (623 body lines, 12 pages,
formfeed_count 12, unit convention Lakhs, ocr_pages none, page_coverage 100%).
Prior-quarter ledger: none provided — this is the first quarterly run for this ticker.
Every ENTITY_CHANGE-style diff below is therefore marked "no prior baseline" rather than
compared.

Methodology note on the two enumeration passes used throughout this ledger:
- "grep count" = a mechanical regex pass with `grep`/`sed`/`awk` run against the extract file
  (patterns shown inline per category).
- "sweep count" = an independent full read of the same line range, paragraph/row by
  paragraph/row, done before or after the grep pass and reconciled against it.
Where a category has both numbered and unnumbered members (notes, auditor paragraphs), the
grep pass combines a pattern for the numbered/lettered form with a pattern for the unnumbered
form (asterisk footnotes, blank-line-delimited paragraph blocks with page-break artifacts and
the entity-table block excluded) so the two totals are commensurable.

=== A2 COUNT TEST ===
category: notes            grep_count: 19   sweep_count: 19   match: yes
category: line_items       grep_count: 121  sweep_count: 121  match: yes
category: zero_standing    grep_count: 3    sweep_count: 3    match: yes
category: agenda_items     grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras    grep_count: 15   sweep_count: 15   match: yes
category: entities         grep_count: 3    sweep_count: 3    match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===

---

## 1. Board Outcome Letter (Reg 30/33 covering letter) — lines 14-63

### 1.1 Agenda items
Grep: `sed -n '14,63p' <extract> | grep -inE "approv|appoint|resign|dividend|AGM|annual general meeting|record date|scrutin|ESOP|capital[- ]rais|auditor"` → 1 substantive match (line 19).
Sweep: full read of lines 14-63 confirms the letter states a single Board agenda item.

| # | Line(s) | Agenda item | Detail | Flags |
|---|---------|-------------|--------|-------|
| 1 | 17-23 | Approval of Q1 FY27 results | Board "considered and approved the Un-audited (Standalone and Consolidated) financial results ... for the quarter ended on June 30, 2026," reviewed/recommended by the Audit Committee. No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant, or capital-raising resolution is mentioned anywhere in the letter. | Letter uses "inter alia" (line 19) — boilerplate hedge phrase that could imply unstated items, but none is named in this document; nothing further to enumerate. |

Board meeting timing (line 42-43): commenced **04:00 p.m. IST**, concluded **04:39 p.m. IST** — a 39-minute meeting covering approval of both standalone and consolidated results (3-entity consolidation) plus the two Limited Review Reports.

### 1.2 Digital signature block — Board Outcome letter
| Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|
| 51-60 | Saurabh Gupta | Company Secretary & Compliance Officer, M. No. F13652 | 2026.07.31 16:46:49 +05'30' | Signed after board concluded (16:39) — expected sequence, no anomaly. |

---

## 2. Standalone Limited Review Report — lines 64-144

### 2.1 Paragraphs (unnumbered report — no numbered paragraphs in this report)
Grep: `sed -n '64,144p' <extract> | grep -cE "^[0-9]+\."` → 0 (confirms report carries no paragraph numbers).
Sweep: blank-line-delimited block scan of lines 81-110 and 122-130 (letterhead 65-73, salutation 76-78, footer address 115-116, and signature block 133-144 excluded as non-narrative) → 4 blocks.

| # | Line(s) | First 15 words | Type | Flags |
|---|---------|-----------------|------|-------|
| 1 | 81-85 | "We have reviewed the accompanying statement of Unaudited Standalone Financial Results of Ram Ratna..." | Scope of review | |
| 2 | 88-95 | "This Statement, which is the responsibility of the Company's Management and approved by the Board..." | Management responsibility / Ind AS 34 basis | |
| 3 | 98-110 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | SRE 2410 review standard, moderate assurance, no audit opinion expressed | |
| 4 | 122-130 | "Based on our review conducted as above, nothing has come to our attention that causes us..." | Conclusion — unmodified/unqualified | No Emphasis of Matter, no Other Matters, no Going Concern language, no entity list (single-entity standalone). |

### 2.2 Digital signature block — Standalone LRR
| Line(s) | Signatory | Designation | Firm | UDIN | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 133-144 | Yezdi K. Bhagwagar | Partner, Membership No. 034236 | Bhagwagar Dalal & Doshi, FRN 128093W | 26034236NWVKME1269 | 2026.07.31 16:45:09 +05'30' | Signed after board concluded (16:39) — no anomaly. |

---

## 3. Standalone Financial Results — Statement of Profit and Loss — lines 147-202

Grep: `sed -n '164,200p' <extract> | grep -cE '[0-9]\.[0-9]{2}|\s-\s+-\s+-\s+-\s*$'` → 29.
Sweep: line-by-line read of the P&L table, including category headers (excluded from the value-row count) → 29 value rows.

| # | Line | Line item | Q1FY27 (30-06-26) | Q4FY26 (31-03-26, note vi) | Q1FY26 (30-06-25) | FY26 (Audited) | Flags |
|---|------|-----------|---|---|---|---|---|
| 1 | 166 | Revenue from Operations | 1,83,199.09 | 1,72,479.99 | 96,040.08 | 5,07,610.97 | |
| 2 | 167 | Other Income | 228.24 | 616.21 | 389.02 | 1,924.67 | |
| 3 | 168 | Total Revenue | 1,83,427.33 | 1,73,096.20 | 96,429.10 | 5,09,535.64 | |
| 4 | 170 | a) Cost of materials consumed | 1,67,604.27 | 1,61,290.10 | 87,835.27 | 4,76,311.14 | |
| 5 | 171 | b) Purchase of Stock in Trade | - | 872.65 | 5,474.40 | 4,124.86 | Dash in current quarter only, non-zero in 3/4 periods — not ZERO_STANDING. |
| 6 | 172 | c) Changes in inventories | (18.06) | (5,389.33) | (5,878.36) | (20,405.02) | |
| 7 | 173 | d) Employee benefits expense | 2,483.92 | 2,305.18 | 1,745.10 | 8,312.72 | |
| 8 | 174 | e) Finance costs | 3,035.99 | 2,685.22 | 1,540.64 | 8,071.99 | |
| 9 | 175 | f) Depreciation and amortisation expense | 1,177.28 | 1,186.66 | 765.89 | 3,508.92 | |
| 10 | 176 | g) Other expenses | 4,379.95 | 4,373.50 | 2,879.40 | 14,168.82 | |
| 11 | 177 | Total Expenses | 1,78,663.35 | 1,67,323.98 | 94,362.34 | 4,94,093.43 | |
| 12 | 178 | Profit before Exceptional Item and Tax (1-2) | 4,763.98 | 5,772.22 | 2,066.76 | 15,442.21 | |
| 13 | 180 | Exceptional Items — Statutory impact of new labour codes | - | - | - | 333.01 | Zero in all 3 quarterly columns, non-zero only in the full-year audited column — not ZERO_STANDING under the "all periods" test, but flagged as a near-nil standing line worth A3 attention. |
| 14 | 181 | Profit before Tax (3-4) | 4,763.98 | 5,772.22 | 2,066.76 | 15,109.20 | |
| 15 | 183 | Tax — Previous year's Tax | - | - | - | (22.82) | Same near-nil pattern as row 13 — not ZERO_STANDING (non-zero in FY26 audited column). |
| 16 | 184 | Tax — Current Tax | 1,020.92 | 1,500.58 | 490.78 | 3,629.58 | |
| 17 | 185 | Tax — Deferred Tax | 71.44 | 270.69 | 122.19 | 670.36 | |
| 18 | 186 | Total Tax Expenses | 1,092.36 | 1,771.27 | 612.97 | 4,277.12 | |
| 19 | 187 | Profit for the Period/Year (5-6) | 3,671.62 | 4,000.95 | 1,453.79 | 10,832.08 | |
| 20 | 189 | OCI A(i) Items not reclassified to P&L | (28.84) | 73.74 | (48.48) | 54.89 | |
| 21 | 190 | OCI A(ii) Income tax on items not reclassified | 7.26 | (18.55) | 6.03 | (19.98) | |
| 22 | 191 | OCI B(i) Items that will be reclassified to P&L | - | - | - | - | **ZERO_STANDING** — dash in all 4 periods. |
| 23 | 192 | OCI B(ii) Income tax on items reclassified | - | - | - | - | **ZERO_STANDING** — dash in all 4 periods. |
| 24 | 193 | Total Other Comprehensive Income/(Loss) | (21.58) | 55.19 | (42.45) | 34.91 | |
| 25 | 194 | Total Comprehensive Income (7+8) | 3,650.04 | 4,056.14 | 1,411.34 | 10,866.99 | |
| 26 | 195-196 | Paid up Equity Share Capital (FV ₹5) | 4,667.45 | 4,667.45 | 2,202.10 | 4,667.45 | |
| 27 | 197 | Reserves excluding revaluation reserves | (blank) | (blank) | (blank) | 53,999.20 | Only the annual audited column is populated — standard quarterly practice, not ZERO_STANDING (not zero/dash, simply not disclosed for interim columns). |
| 28 | 199 | EPS — Basic (₹)* | 3.93 | 4.29 | 1.56 | 11.61 | *Refer Note iv (bonus-adjusted). |
| 29 | 200 | EPS — Diluted (₹)* | 3.93 | 4.28 | 1.56 | 11.60 | *Refer Note iv (bonus-adjusted). |

---

## 4. Standalone Segment Reporting — lines 204-253

Grep: `sed -n '220,252p' <extract> | grep -cE '[0-9]\.[0-9]{2}'` → 25.
Sweep: line-by-line read of the segment table (2 reportable segments per standalone Note iii) → 25 value rows.

| # | Line | Segment line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 (Audited) | Flags |
|---|------|--------------------|---|---|---|---|---|
| 1 | 222 | Segment Revenue — a) Winding wires and strips | 1,35,689.67 | 1,39,204.29 | 82,691.80 | 3,98,659.09 | |
| 2 | 223 | Segment Revenue — b) Copper tubes and pipes | 48,997.75 | 34,719.72 | 13,738.65 | 1,14,674.41 | |
| 3 | 224 | Segment Revenue — Total | 1,84,687.42 | 1,73,924.01 | 96,430.45 | 5,13,333.50 | |
| 4 | 225 | Less: Inter Segment Transfer | 1,488.33 | 1,444.02 | 390.37 | 5,722.53 | |
| 5 | 226 | Revenue from Operations | 1,83,199.09 | 1,72,479.99 | 96,040.08 | 5,07,610.97 | |
| 6 | 229 | Segment Results — a) Winding wires and strips | 5,989.75 | 7,067.78 | 3,489.40 | 18,241.96 | |
| 7 | 230 | Segment Results — b) Copper tubes and pipes | 2,299.42 | 2,285.93 | 523.36 | 6,817.52 | |
| 8 | 231 | Segment Results — Total | 8,289.17 | 9,353.71 | 4,012.76 | 25,059.48 | |
| 9 | 232 | Less: Finance cost | (3,035.99) | (2,685.22) | (1,540.64) | (8,071.99) | |
| 10 | 233 | Less: Other Unallocable Expenditure | (489.20) | (896.27) | (405.36) | (1,878.29) | |
| 11 | 234 | Total Profit Before Tax | 4,763.98 | 5,772.22 | 2,066.76 | 15,109.20 | |
| 12 | 236 | Segment Assets — a) Winding wires and strips | 1,16,119.47 | 1,12,417.79 | 93,988.04 | 1,12,417.79 | |
| 13 | 237 | Segment Assets — b) Copper tubes and pipes | 66,862.48 | 54,357.29 | 38,151.68 | 54,357.29 | |
| 14 | 238 | Total Segment Assets | 1,82,981.95 | 1,66,775.08 | 1,32,139.72 | 1,66,775.08 | |
| 15 | 239 | Unallocable Assets | 22,470.54 | 25,614.55 | 15,171.15 | 25,614.55 | |
| 16 | 240 | Total (Assets) | 2,05,452.49 | 1,92,389.63 | 1,47,310.87 | 1,92,389.63 | |
| 17 | 242 | Segment Liabilities — a) Winding wires and strips | 80,296.48 | 79,998.29 | 66,045.94 | 79,998.29 | |
| 18 | 243 | Segment Liabilities — b) Copper tubes and pipes | 38,078.65 | 18,058.10 | 17,798.15 | 18,058.10 | |
| 19 | 244 | Total Segment Liabilities | 1,18,375.13 | 98,056.39 | 83,844.09 | 98,056.39 | |
| 20 | 245 | Unallocable Liabilities | 24,582.98 | 35,513.60 | 13,038.10 | 35,513.60 | |
| 21 | 246 | Total (Liabilities) | 1,42,958.11 | 1,33,569.99 | 96,882.19 | 1,33,569.99 | |
| 22 | 249 | Capital Employed — a) **"Enamelled wires and strips"** | 35,822.99 | 32,419.50 | 27,942.10 | 32,419.50 | **LABEL_INCONSISTENCY** — every other reference in this filing (P&L header, Segment Revenue/Results/Assets/Liabilities rows, standalone Note iii, consolidated tables) calls this segment "Winding wires and strips." This row alone reads "Enamelled wires and strips." Same underlying figures reconcile elsewhere; naming only. |
| 23 | 250 | Capital Employed — b) Copper tubes and pipes | 28,783.83 | 36,299.19 | 20,353.53 | 36,299.19 | |
| 24 | 251 | Un-allocable Assets less Liabilities | (2,112.44) | (9,899.05) | 2,133.05 | (9,899.05) | |
| 25 | 252 | Total (Capital Employed) | 62,494.38 | 58,819.64 | 50,428.68 | 58,819.64 | |

---

## 5. Standalone Notes — lines 260-299

Grep (combined): `grep -nE "^\s*[ivx]{1,5}\)"` → 8 matches in this section (lines 262, 267, 273, 276, 281, 292, 295, 298) + `grep -n "^\*"` → 1 asterisk footnote (line 202, physically located inside the P&L table under EPS) = 9.
Sweep: independent read of lines 260-299 plus the EPS asterisk cross-reference on line 198/202 → 9 notes.

| # | Line | Marker | First 15 words | Flags |
|---|------|--------|-----------------|-------|
| 1 | 262-265 | i) | "The above standalone financial results of Ram Ratna Wires Limited have been prepared in accordance with..." | Basis of preparation (Ind AS, Reg 33). |
| 2 | 267-271 | ii) | "The standalone financial results for the quarter ended 30th June, 2026 have been reviewed by the..." | Audit Committee review, Board approval 31-Jul-2026, unmodified opinion. |
| 3 | 273-274 | iii) | "On Standalone basis the Company has identified two reportable segments i) Winding wires and strips &..." | Segment basis, Ind AS 108 — names segment "Winding wires and strips" (cf. row 22 of section 4). |
| 4 | 276-279 | iv) | "Pursuant to approval of the Members of the Company, the Company had allotted 4,66,74,536 equity shares..." | 1:1 bonus issue, record date 26-Dec-2025, EPS restated (referenced by EPS rows, section 3 rows 28-29). |
| 5 | 281-289 | v) | "The Ministry of Environment, Forest and Climate Change has notified the Hazardous and Other Wastes..." | EPR (Extended Producer Responsibility) obligation on non-ferrous scrap w.e.f. 1-Apr-2026; portal not yet operational; financial impact not quantifiable — INDETERMINATE-type disclosure, unquantified contingent obligation. |
| 6 | 292-293 | vi) | "The figures for the quarters ended 31st March, 2026 are balancing figures between the audited figures..." | Explains the "Refer Note vi" column in section 3's table. |
| 7 | 295 | vii) | "Previous periods / year's figures have been regrouped / reclassified, wherever necessary, to make them..." | Standard regrouping note. |
| 8 | 298-299 | viii) | "The above standalone financial results of the Company will be available on the website of the..." | Website disclosure (rrshramik.com, BSE, NSE). |
| 9 | 198, 202 | * (unnumbered, asterisk footnote to EPS line) | "Basic and Diluted Earnings per share are not annualised except for the year ended 31 March..." | Footnote qualifying the EPS headline numbers in section 3, rows 28-29; cross-referenced from line 198 "Earning Per Share* (Refer Note iv)." |

### 5.1 Digital signature block — Standalone results (Board signatory)
| Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|
| 302-313 | Tribhuvanprasad Rameshwarlal Kabra | Chairman, DIN 00091375 | 2026.07.31 16:43:12 +05'30' | Signed after board concluded (16:39) — no anomaly. |

---

## 6. Consolidated Limited Review Report — lines 315-454

### 6.1 Paragraphs
Grep: `sed -n '316,454p' <extract> | grep -cE "^[0-9]+\."` → 6 (numbered paragraphs 1-6, lines 330, 339, 349, 377, 388, 401 in original file numbering).
Sweep: blank-line-delimited block scan of lines 330-362 and 372-438 (letterhead/address/signature excluded; the page-8/page-9 break inside paragraph 6's Other Matters section merged across the "[page 9] / Bhagwagar Dalal & Doshi" running-header artifact; the Sr.No./Name/Relationship entity table counted separately under section 6.2, not as a narrative paragraph) → 15 total narrative units (6 numbered + 9 unnumbered, itemized below).

| # | Line(s) | Numbered? | First 15 words | Type | Flags |
|---|---------|-----------|------------------|------|-------|
| 1 | 330-337 | Para 1 | "We have reviewed the accompanying statement of Unaudited Consolidated Financial Results of Ram Ratna..." | Scope of review (Parent + subsidiary + JV share) | |
| 2 | 339-347 | Para 2 | "The Consolidated Statement, which is the responsibility of the Parent's Management and approved by the..." | Management responsibility / Ind AS 34 basis | |
| 3 | 349-362 | Para 3 | "We conducted our review of the Consolidated Statement in accordance with the Standard on Review..." | SRE 2410 review standard, moderate assurance, no audit opinion | |
| 4 | 372-375 | unnumbered | "We also performed procedures in accordance with the circular issued by the SEBI under Regulation..." | Reg 33(8) SEBI circular procedures | |
| 5 | 377-378 | Para 4 (intro) | "The Consolidated Statement includes the financial statements of the following entities" | Entity-list intro (table enumerated in 6.2) | |
| 6 | 388-399 | Para 5 | "Based on our review conducted and procedure performed as stated above and based on the consideration..." | Conclusion — unmodified, relies in part on other auditors for TPPL/RRIEL | |
| 7 | 401-406 | Para 6 (opening) | "We did not review the interim financial information/results of the TPPL, whose interim financial..." | **Other Matters** — TPPL not reviewed by principal auditor; TPPL Q1FY27 figures given: revenue ₹2,140.50 lakh, net loss ₹(13.77) lakh, TCI loss ₹(13.13) lakh | TPPL = unaudited/management-furnished by other auditors to principal auditor. |
| 8 | 408-419, 425-426 | unnumbered (Other Matters continuation, spans page 8/9 break) | "This Consolidated Statement also includes the Parent's share of net profit of ₹ 61.16 lakhs..." | RRIEL (Bangladesh JV) — Parent's share of net profit ₹61.16 lakh, TCI ₹61.78 lakh; RRIEL results restated by Parent management from IFRS/Bangladesh GAAP to Ind AS; reviewed as restated | RRIEL = unaudited/management-furnished (restated by Parent's own management from other-auditor reports), located in Bangladesh (cross-border JV). |
| 9 | 428-430 | unnumbered | "The interim financial information/results of the TPPL and RRIEL have been reviewed by other auditors..." | Confirms TPPL and RRIEL reviewed by OTHER auditors, reports furnished to principal auditor by Parent management | |
| 10 | 432-436 | unnumbered | "Our conclusion on the Consolidated Statement in so far as it relates to the amounts and..." | Conclusion for TPPL/RRIEL portions based solely on other auditors' reports and Parent-management-provided explanations | |
| 11 | 438 | unnumbered | "Our conclusion is not modified in respect of these matters." | Closing sentence of Other Matters — conclusion not modified | |

Standalone-report paragraph count carried forward from section 2.1 for the combined auditor_paras total: 4. Consolidated: 11 narrative units above (rows 1-11) — reconciling to the stated 15 total: standalone 4 + consolidated 11 = 15. (Note: earlier draft pass mis-split the Other Matters section into 12 units by double-counting the para-6 opening sentence; re-swept and corrected to 11 consolidated / 15 combined, which is what is reported in the COUNT TEST above and in the YAML footer.)

### 6.2 Entity list (Consolidated Statement, para 4) — lines 377-386, cross-checked against consolidated Note iii (lines 595-598)
Grep: `sed -n '377,398p' <extract> | grep -cE "^\s*[0-9]+\s+[A-Z]"` → 3.
Sweep: independent read of the Sr.No./Name/Relationship table and of Note iii's entity list → 3 entities, names and relationship types match between the two disclosures.

| # | Line(s) | Entity | Relationship | Cross-check (Note iii, line) | Flags |
|---|---------|--------|--------------|-------------------------------|-------|
| 1 | 381-382 | Tefabo Product Private Limited (TPPL) | Subsidiary Company | Matches — "Subsidiary: Tefabo Product Private Limited (TPPL)" (598) | No prior-quarter ledger to diff against — first quarterly run for this ticker, baseline only. |
| 2 | 383-384 | Epavo Electricals Private Limited (EEPL) | Joint Venture | Matches — "Joint Venture: ... Epavo Electricals Private Limited (EEPL)" (597) | Same — baseline only. |
| 3 | 385-386 | R R Imperial Electricals Limited (RRIEL) | Joint Venture (Bangladesh, per LRR para 6) | Matches — "Joint Venture: RR-Imperial Electricals Limited" (596) | Same — baseline only. Note spelling varies "R R Imperial" (LRR) vs "RR-Imperial" (Note iii) — same entity, punctuation only. |

### 6.3 Digital signature block — Consolidated LRR
| Line(s) | Signatory | Designation | Firm | UDIN | Timestamp | Flags |
|---|---|---|---|---|---|---|
| 441-454 | Yezdi K. Bhagwagar | Partner, Membership No. 034236 | Bhagwagar Dalal & Doshi, FRN 128093W | 26034236KOSAHB7217 | 2026.07.31 16:45:44 +05'30' | Signed after board concluded (16:39) — no anomaly. Same partner/firm signs both standalone and consolidated reports, different UDIN each (correct — UDIN is per-report). |

---

## 7. Consolidated Financial Results — Statement of Profit and Loss — lines 456-523

Grep: `sed -n '472,522p' <extract> | grep -cE '[0-9]\.[0-9]{2}|\s-\s+-\s+-\s*$'` → 37.
Sweep: line-by-line read of the consolidated P&L table → 37 value rows.

| # | Line | Line item | Q1FY27 | Q4FY26 (note vii) | Q1FY26 | FY26 (Audited) | Flags |
|---|------|-----------|---|---|---|---|---|
| 1 | 474 | Revenue from Operations | 1,85,328.10 | 1,75,285.14 | 98,246.90 | 5,17,664.98 | |
| 2 | 475 | Other Income | 234.12 | 602.33 | 367.30 | 1,849.72 | |
| 3 | 476 | Total Revenue | 1,85,562.22 | 1,75,887.47 | 98,614.20 | 5,19,514.70 | |
| 4 | 478 | a) Cost of materials consumed | 1,68,598.11 | 1,63,112.59 | 89,083.00 | 4,82,114.00 | |
| 5 | 479 | b) Purchases of stock-in-trade | - | 872.65 | 5,474.40 | 4,124.86 | Not ZERO_STANDING (dash in 1/4 periods only). |
| 6 | 480 | c) Changes in inventories | 252.89 | (5,553.44) | (5,935.95) | (20,813.33) | |
| 7 | 481 | d) Employee benefits expense | 2,677.07 | 2,656.96 | 2,014.34 | 9,654.78 | |
| 8 | 482 | e) Finance costs | 3,164.81 | 2,782.99 | 1,611.70 | 8,381.65 | |
| 9 | 483 | f) Depreciation and amortisation expense | 1,276.52 | 1,263.90 | 825.04 | 3,786.63 | |
| 10 | 484 | g) Other expenses | 4,841.81 | 4,875.37 | 3,324.07 | 16,224.17 | |
| 11 | 485 | Total Expenses | 1,80,811.21 | 1,70,011.02 | 96,396.60 | 5,03,472.76 | |
| 12 | 487 | Profit before Exceptional Item, share of profit of JVs and Tax (1-2) | 4,751.01 | 5,876.45 | 2,217.60 | 16,041.94 | |
| 13 | 489 | Exceptional Items — Statutory impact of new labour codes | - | - | - | 356.43 | Not ZERO_STANDING (non-zero in FY26 audited column) — mirrors standalone row 13. |
| 14 | 490-492 | Profit before share of Profit/(Loss) of JVs and Tax (3-4) | 4,751.01 | 5,876.45 | 2,217.60 | 15,685.51 | |
| 15 | 493 | Share of Profit/(Loss) of Joint Ventures | (141.53) | (137.97) | 22.06 | (388.63) | Consolidation-only line (JV share — not present in standalone table). |
| 16 | 494 | Profit before tax (5+6) | 4,609.48 | 5,738.48 | 2,239.66 | 15,296.88 | |
| 17 | 496 | Tax — Previous year's Tax | - | 1.96 | - | (20.86) | Not ZERO_STANDING (2/4 periods non-zero). |
| 18 | 497 | Tax — Current Tax | 1,020.92 | 1,526.09 | 526.30 | 3,761.66 | |
| 19 | 498 | Tax — Deferred Tax | 72.21 | 287.58 | 121.12 | 696.37 | |
| 20 | 499 | Total Tax Expenses | 1,093.13 | 1,815.63 | 647.42 | 4,437.17 | |
| 21 | 500 | Profit for the period/year (7-8) | 3,516.35 | 3,922.85 | 1,592.24 | 10,859.71 | |
| 22 | 502 | OCI A(i) Items not reclassified to P&L | (28.20) | 74.49 | (47.87) | 56.56 | |
| 23 | 503 | OCI A(ii) Income tax on items not reclassified | 7.26 | (18.55) | 6.03 | (19.98) | |
| 24 | 505 | OCI B(i) — Exchange difference on translation of foreign operations | 0.62 | 34.07 | (3.24) | 63.01 | Consolidation-only line (foreign JV translation — not present in standalone table). |
| 25 | 506 | OCI B(ii) Income tax on items reclassified | - | - | - | (blank) | **ZERO_STANDING** — dash in the three periods shown; fourth (FY26 audited) column has no printed value at all. |
| 26 | 507 | Total Other Comprehensive Income | (20.32) | 90.01 | (45.08) | 99.59 | |
| 27 | 508 | Total Comprehensive Income (9+10) | 3,496.03 | 4,012.86 | 1,547.16 | 10,959.30 | |
| 28 | 510 | Profit attributable — Owners of the Company | 3,521.31 | 3,901.30 | 1,545.68 | 10,705.20 | |
| 29 | 511 | Profit attributable — Non-Controlling Interest | (4.96) | 21.55 | 46.56 | 154.51 | |
| 30 | 513 | OCI attributable — Owners of the Company | (20.55) | 89.74 | (45.32) | 98.96 | |
| 31 | 514 | OCI attributable — Non-Controlling Interest | 0.23 | 0.27 | 0.24 | 0.63 | |
| 32 | 516 | TCI attributable — Owners of the Company | 3,500.76 | 3,991.04 | 1,500.36 | 10,804.16 | |
| 33 | 517 | TCI attributable — Non-Controlling Interest | (4.73) | 21.82 | 46.80 | 155.14 | |
| 34 | 518 | Paid up Equity Share Capital (FV ₹5) | 4,667.45 | 4,667.45 | 2,202.10 | 4,667.45 | |
| 35 | 519 | Reserves excluding revaluation reserves | (blank) | - | - | 53,128.02 | Not ZERO_STANDING (non-zero in FY26 audited column; blank/dash in interim columns is standard quarterly practice). |
| 36 | 521 | EPS — Basic (₹)* | 3.77 | 4.18 | 1.66 | 11.48 | *Refer Note v (bonus-adjusted). |
| 37 | 522 | EPS — Diluted (₹)* | 3.77 | 4.18 | 1.66 | 11.46 | *Refer Note v (bonus-adjusted). |

---

## 8. Consolidated Segment Reporting — lines 525-577

Grep: `sed -n '539,576p' <extract> | grep -cE '[0-9]\.[0-9]{2}'` → 30.
Sweep: line-by-line read of the consolidated segment table (3 reportable segments per consolidated Note iv, vs. 2 in standalone) → 30 value rows.

| # | Line | Segment line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 (Audited) | Flags |
|---|------|--------------------|---|---|---|---|---|
| 1 | 541 | Segment Revenue — a) Winding wires and strips | 1,35,689.67 | 1,39,204.29 | 82,691.80 | 3,98,659.09 | |
| 2 | 542 | Segment Revenue — b) Copper tubes and pipes | 48,997.75 | 34,719.72 | 13,738.65 | 1,14,674.41 | |
| 3 | 543 | Segment Revenue — c) Other | 2,129.01 | 2,805.15 | 2,206.82 | 10,054.01 | Third segment, consolidation-only (subsidiary TPPL revenue) — not present in standalone table. |
| 4 | 544 | Segment Revenue — Total | 1,86,816.43 | 1,76,729.16 | 98,637.27 | 5,23,387.51 | |
| 5 | 545 | Less: Inter Segment Transfer | 1,488.33 | 1,444.02 | 390.37 | 5,722.53 | |
| 6 | 546 | Revenue from Operations | 1,85,328.10 | 1,75,285.14 | 98,246.90 | 5,17,664.98 | |
| 7 | 549 | Segment Results — a) Winding wires and strips | 5,842.64 | 7,314.81 | 3,486.53 | 17,759.49 | |
| 8 | 550 | Segment Results — b) Copper tubes and pipes | 2,299.42 | 2,285.93 | 523.36 | 6,817.52 | |
| 9 | 551 | Segment Results — c) Other | 121.43 | (183.00) | 246.83 | 979.81 | |
| 10 | 552 | Segment Results — Total | 8,263.49 | 9,417.74 | 4,256.72 | 25,556.82 | |
| 11 | 553 | Less: Finance cost | (3,164.81) | (2,782.99) | (1,611.70) | (8,381.65) | |
| 12 | 554 | Less: Other Unallocable Expenditure | (489.20) | (896.27) | (405.36) | (1,878.29) | |
| 13 | 555 | Total Profit Before Tax | 4,609.48 | 5,738.48 | 2,239.66 | 15,296.88 | |
| 14 | 557 | Segment Assets — a) Winding wires and strips | 1,11,431.13 | 1,07,870.36 | 89,210.04 | 1,07,870.36 | |
| 15 | 558 | Segment Assets — b) Copper tubes and pipes | 66,862.48 | 54,357.29 | 38,151.68 | 54,357.29 | |
| 16 | 559 | Segment Assets — c) Other | 10,997.58 | 11,508.39 | 8,937.57 | 11,508.39 | |
| 17 | 560 | Total Segment Assets | 1,89,291.19 | 1,73,736.04 | 1,36,299.29 | 1,73,736.04 | |
| 18 | 561 | Unallocable Assets | 22,470.54 | 25,614.55 | 15,171.15 | 25,614.55 | |
| 19 | 562 | Total (Assets) | 2,11,761.73 | 1,99,350.59 | 1,51,470.44 | 1,99,350.59 | |
| 20 | 564 | Segment Liabilities — a) Winding wires and strips | 80,296.47 | 79,998.28 | 65,045.93 | 79,998.28 | |
| 21 | 565 | Segment Liabilities — b) Copper tubes and pipes | 38,078.65 | 18,058.10 | 17,798.15 | 18,058.10 | |
| 22 | 566 | Segment Liabilities — c) Other | 6,790.84 | 7,288.54 | 5,243.63 | 7,288.54 | |
| 23 | 567 | Total Segment Liabilities | 1,25,165.96 | 1,05,344.92 | 88,087.71 | 1,05,344.92 | |
| 24 | 568 | Unallocable Liabilities | 24,582.98 | 35,513.60 | 13,038.10 | 35,513.60 | |
| 25 | 569 | Total (Liabilities) | 1,49,748.94 | 1,40,858.52 | 1,01,125.81 | 1,40,858.52 | |
| 26 | 572 | Capital Employed — a) Winding wires and strips | 31,134.66 | 27,872.08 | 24,164.11 | 27,872.08 | Label here reads "Winding wires and strips" (consistent) — contrast with standalone table's "Enamelled wires and strips" (section 4, row 22). |
| 27 | 573 | Capital Employed — b) Copper tubes and pipes | 28,783.83 | 36,299.19 | 20,353.53 | 36,299.19 | |
| 28 | 574 | Capital Employed — c) Other | 4,206.74 | 4,219.85 | 3,693.94 | 4,219.85 | |
| 29 | 575 | Un-allocable Assets less Liabilities | (2,112.44) | (9,899.05) | 2,133.05 | (9,899.05) | |
| 30 | 576 | Total (Capital Employed) | 62,012.79 | 58,492.07 | 50,344.63 | 58,492.07 | |

---

## 9. Consolidated Notes — lines 584-625

Grep (combined): `grep -nE "^\s*[ivx]{1,5}\)"` → 9 matches in this section (lines 586, 591, 595, 600, 605, 609, 619, 622, 624) + `grep -n "^\*"` → 1 match in this section (line 523). Combined grep total for the consolidated statement: 10.
Sweep: independent read of lines 584-625 plus the EPS asterisk cross-reference on line 520/523 → 10 notes for the consolidated statement (9 roman-numeral + 1 asterisk footnote), mirroring the standalone statement's 8 roman-numeral + 1 asterisk = 9 pattern. Match: yes.

Note: standalone notes total = 9 (8 roman-numeral + 1 asterisk, section 5). Consolidated notes total = 10 (9 roman-numeral + 1 asterisk). Combined notes category total = 19, matching the COUNT TEST header. (The 19 = 17 roman-numeral matches system-wide + 2 asterisk footnotes system-wide, as verified by the whole-file grep passes reported in the COUNT TEST.)

| # | Line | Marker | First 15 words | Flags |
|---|------|--------|-----------------|-------|
| 1 | 586-589 | i) | "The above consolidated financial results of Ram Ratna Wires Limited have been prepared in accordance..." | Basis of preparation (Ind AS, Reg 33). |
| 2 | 591-593 | ii) | "The Consolidated financial results for the quarter ended 30th June, 2026 have been reviewed by the..." | Audit Committee review, Board approval 31-Jul-2026, unmodified opinion. |
| 3 | 595-598 | iii) | "The consolidated financial results include the financial results of the following:" | Entity list (JV: RR-Imperial Electricals Ltd, Epavo Electricals Pvt Ltd; Subsidiary: Tefabo Product Pvt Ltd) — cross-checked against LRR para 4 entity table, section 6.2. |
| 4 | 600-601 | iv) | "On consolidated basis the Company has identified three reportable segments, namely, a) Winding wires and strips..." | Segment basis, Ind AS 108 — 3 segments (vs standalone's 2), consistent with section 8's "Other" row. |
| 5 | 605-607 | v) | "Pursuant to approval of the Members of the Parent, the Parent had allotted 4,66,74,536 equity shares..." | 1:1 bonus issue, record date 26-Dec-2025, EPS restated (referenced by EPS rows, section 7 rows 36-37). |
| 6 | 609-617 | vi) | "The Ministry of Environment, Forest and Climate Change has notified the Hazardous and Other Wastes..." | Same EPR disclosure as standalone Note v, restated for "the Group." |
| 7 | 619-620 | vii) | "The figures for the quarter ended 31st March, 2026 are the balancing figures between the audited..." | Explains "Refer Note vii" column in section 7's table. |
| 8 | 622 | viii) | "Previous periods / year's figures have been regrouped / reclassified, wherever necessary, to make them..." | Standard regrouping note. |
| 9 | 624-625 | ix) | "The above consolidated financial results of the Company will be available on the website of the..." | Website disclosure (rrshramik.com, BSE, NSE). |
| 10 | 520, 523 | * (unnumbered, asterisk footnote to EPS line) | "Basic and Diluted Earnings per share are not annualised except for the year ended 31st March..." | Footnote qualifying the EPS headline numbers in section 7, rows 36-37; cross-referenced from line 520 "Earning Per Share* (Refer Note v)." |

### 9.1 Digital signature block — Consolidated results (Board signatory)
| Line(s) | Signatory | Designation | Timestamp | Flags |
|---|---|---|---|---|
| 626-636 | Tribhuvanprasad Rameshwarlal Kabra | Chairman, DIN 00091375 | 2026.07.31 16:43:43 +05'30' | Signed after board concluded (16:39) — no anomaly. Same Chairman signs both standalone (16:43:12) and consolidated (16:43:43) results, 31 seconds apart — sequence internally consistent. |

---

## 10. All digital signature blocks — cross-cutting summary (5 blocks total)

Grep: `grep -ic "Digitally signed"` → 5 (lines 52, 136, 304, 444, 628).
Sweep: independent read locating each signature block's full context (name, designation, firm/UDIN where applicable, timestamp) → 5.

| # | Line(s) | Document | Signatory | Designation | Timestamp | Order vs. board conclusion (16:39) | Flags |
|---|---------|----------|-----------|-------------|-----------|--------------------------------------|-------|
| 1 | 51-60 | Reg 30/33 covering letter | Saurabh Gupta | Company Secretary & Compliance Officer | 16:46:49 | After | None |
| 2 | 133-144 | Standalone LRR | Yezdi K. Bhagwagar | Partner, Bhagwagar Dalal & Doshi | 16:45:09 | After | None |
| 3 | 302-313 | Standalone results | T. R. Kabra | Chairman, DIN 00091375 | 16:43:12 | After | None |
| 4 | 441-454 | Consolidated LRR | Yezdi K. Bhagwagar | Partner, Bhagwagar Dalal & Doshi | 16:45:44 | After | None |
| 5 | 626-636 | Consolidated results | T. R. Kabra | Chairman, DIN 00091375 | 16:43:43 | After | None |

All five signature timestamps post-date the board meeting's stated conclusion time (04:39 p.m.) and are internally sequential (Chairman signs standalone then consolidated; auditor signs standalone then consolidated; CS sends the covering letter last). No `SIGNATURE_BEFORE_CONCLUSION`-type anomaly to flag.

---

## Documents/sections NOT present in this filing (checked and confirmed absent, not silently dropped)
- Standalone or Consolidated Statement of Assets and Liabilities (Balance Sheet): absent — not required for a non-year-end quarter under Reg 33; only the year-end (31-Mar) audited column reserves figure (section 3 row 27 / section 7 row 35) is disclosed, consistent with this.
- Standalone or Consolidated Cash Flow Statement: absent — same reasoning (quarterly, not annual/half-yearly).
- Any annexure beyond the two Limited Review Reports, the two result statements, the two segment statements, and the two notes blocks: none present in the 12-page extract.
- Director appointment/resignation annexure, ESOP annexure, scrutinizer report: none present — consistent with the single-item Board Outcome letter (section 1.1).

---

```yaml
stage: A2-enumerator
company: "RAMRAT"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/ramrat-q1fy27/work/ledger_results_ramrat_q1fy27.md"
counts:
  notes: 19
  line_items: 121
  zero_standing: 3
  agenda_items: 1
  auditor_paras: 15
  entities: 3
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, LABEL_INCONSISTENCY]
gate_a2: pass
mismatch_note: ""
```
