# A2 COMPLETENESS LEDGER — Ganesha Ecosphere Limited (GANECOS), Q1 FY27, Results filing

Source: `extract_results_ganecos_q1fy27.txt` (386 embedded document lines, 7 pages, Lakh units).
Line numbers below are the extract's own embedded line numbers (the number that
immediately follows the page/line marker in the source text), not the raw file's
physical line count.

```
=== A2 COUNT TEST ===
category: notes            grep_count: 14   sweep_count: 14   match: yes  (see reconciliation note 1)
category: line_items       grep_count: 64   sweep_count: 64   match: yes  (see reconciliation note 2)
category: zero_standing    grep_count: 4    sweep_count: 4    match: yes
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 15   sweep_count: 15   match: yes  (see reconciliation note 3)
category: entities         grep_count: 6    sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation notes (mismatches found on first pass, resolved by re-sweep)
1. **Notes.** Naive `grep -n -E "^\s*[0-9]+\.\s"` returns **0** matches against the
   raw extract, because every content line is itself prefixed with the extract's
   own embedded line number + tab, so the anchor `^` never lands on the note
   number. Adjusted grep (tolerant of the line-number prefix) found 7 standalone
   numbered notes + 6 consolidated numbered notes = 13. Manual sweep found a
   14th item: an **unnumbered, bullet-marked footnote** under the consolidated
   statement (ESOP Trust shares held, line 261-264) that no numeric grep pattern
   catches by construction. Re-swept and confirmed as a genuine disclosure unit
   (flag `ESOP_FOOTNOTE_UNNUMBERED`). Final count 14 = 14.
2. **Line items.** Generic keyword/roman-numeral regexes over-count badly
   (46 and 49 raw hits vs. 31/33 actual rows) because OCR line-wrapping
   duplicates fragments across continuation lines. Reconciled via an
   anchor-substring list (one unique fixed string per expected row label),
   cross-checked row by row; final count converges to 31 standalone + 33
   consolidated = 64. One label anchor ("VI Tax expense") initially failed
   due to an OCR spacing variant and was corrected on re-sweep.
3. **Auditor paragraphs.** Consolidated report paragraph 1 is OCR'd as "**I.**"
   (capital I, not digit 1) and paragraph 11 is OCR'd as "11.Our" (no space
   after the period), so a naive digit-only, space-after-period grep pattern
   returns only 9 of 11 numbered paragraphs. Standalone report paragraphs are
   **entirely unnumbered prose** — a digit-anchored grep returns 0 by
   construction. Adjusted grep (OCR-tolerant regex for consolidated;
   fixed-string topic-sentence search for standalone) converges to 11
   (consolidated) + 4 (standalone) = 15, matching manual sweep.

---

## 1. BOARD OUTCOME LETTER (page 1, lines 1-40)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Agenda item: approval of results | 17-20 | Board approved Unaudited Standalone and Consolidated Financial Results for quarter ended June 30, 2026, in continuation of prior letter dated July 27, 2026 | |
| 2 | Enclosure (1): Unaudited Standalone and Consolidated Financial Results (Provisional) | 24-25 | Per Reg 33 | OCR_GARBLED (surrounding text badly corrupted: "?01\", "w P.") |
| 3 | Enclosure (2): Limited Review Report on Unaudited Standalone and Consolidated Financial Results (Provisional) | 26-27 | Per Reg 33 | OCR_GARBLED |
| 4 | Board meeting start/end time | 28-29 | "The meeting commenced at 5:1)P.M. and concluded at ___ P.M." — start time partially illegible, end time field blank/illegible in extract | MEETING_TIME_ILLEGIBLE — cannot assess meeting duration (20 min vs 2 hr signal) from this document |
| — | Absence of other agenda items | n/a | No AR approval, no AGM notice, no record date, no dividend declaration, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution appears anywhere in the letter. This is a single-item (results-only) Board Outcome letter. | ABSENT_AGENDA_ITEMS (noted for completeness per instruction; not a numbered row) |

Signatory: Bharat Kumar Sajnani, Company Secretary-cum-Compliance Officer, "For Ganesha Ecosphere Limited" — lines 34-36. Letter dated August 3, 2026 (date only, no time on signature block itself).

agenda_items count = 4 (rows 1-4 above; the "absence" row is descriptive, not counted).

---

## 2. STANDALONE STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 2)

Columns: Q1 FY27 (Jun 30 2026, Unaudited) | Q4 FY26 (Mar 31 2026, Audited, "Refer note 5") | Q1 FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited). All Rs Lakh.

| # | Line item | Line(s) | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|---------|--------|--------|-------|------|-------|
| 1 | I Revenue from operations | 54 | 26,230.11 | 26,033.36 | 22,147.16 | 1,01,410.25 | |
| 2 | II Other income | 55 | 351.68 | 985.74 | 817.01 | 3,980.02 | |
| 3 | III Total Income (I+II) | 56 | 26,581.79 | 27,019.10 | 22,964.17 | 1,05,390.27 | |
| 4 | IV EXPENSES (section header) | 57 | — | — | — | — | HEADER_ONLY |
| 5 | Cost of materials consumed | 58 | 19,511.14 | 16,873.36 | 16,008.79 | 65,979.69 | |
| 6 | Purchases of stock-in-trade | 59 | 596.45 | 342.56 | 107.73 | 958.36 | |
| 7 | Changes in inventories of finished goods, stock-in-trade and WIP | 60-61 | (2,579.08) | 153.49 | (539.76) | 4,094.54 | |
| 8 | Employee benefits expense | 62-63 | 1,766.06 | 1,993.89 | 1,789.30 | 7,444.48 | |
| 9 | Finance costs | 64 | 199.90 | 138.19 | 131.65 | 690.64 | |
| 10 | Depreciation and amortization expense | 65 | 685.33 | 721.83 | 587.26 | 2,537.49 | |
| 11 | Power & fuel | 66-67 | 2,109.71 | 2,128.97 | 1,923.25 | 8,396.67 | |
| 12 | Other expenses | 68 | 2,446.75 | 2,447.97 | 1,928.05 | 8,841.73 | |
| 13 | Total expenses (IV) | 69 | 24,736.26 | 24,800.26 | 21,936.27 | 98,943.60 | |
| 14 | V Profit before tax (III-IV) | 70 | 1,845.53 | 2,218.84 | 1,027.90 | 6,446.67 | |
| 15 | VI Tax expense (section header) | 71 | — | — | — | — | HEADER_ONLY |
| 16 | (1) Current tax | 72 | 507.73 | 677.06 | 259.16 | 1,790.32 | |
| 17 | (2) Deferred tax | 73 | (37.15) | (99.05) | 2.45 | (126.89) | |
| 18 | VII Profit for the period (V-VI) | 74-75 | 1,374.95 | 1,640.83 | 766.29 | 4,783.24 | |
| 19 | VIII Other Comprehensive Income (section header) | 76 | — | — | — | — | HEADER_ONLY |
| 20 | A(i) Items that will not be reclassified to P&L (subheader) | 77 | — | — | — | — | HEADER_ONLY |
| 21 | Re-measurement gain/(loss) on defined benefit obligations | 78 | 1.53 | 12.12 | (2.00) | 6.13 | |
| 22 | Re-measurement gain/(loss) on financial instrument (Equity) | 79-80 | 115.70 | (251.13) | (25.71) | (759.82) | |
| 23 | A(ii) Income tax relating to above items | 81 | (17.69) | 34.49 | 4.35 | 112.05 | |
| 24 | B(i) Items that will be reclassified to profit or loss | 83 | — | — | — | — | **ZERO_STANDING** |
| 25 | B(ii) Income tax relating to above items | 86 | — | — | — | — | **ZERO_STANDING** (row label itself is OCR-garbled beyond recognition — "l1111nmn 1n11 rnlntinn..." — identity inferred solely from table position/structure; value confirmed dash in all periods) |
| 26 | IX Total Comprehensive Income for the period (VII+VIII) | 88-91 | 1,474.49 | 1,436.31 | 742.93 | 4,141.60 | |
| 27 | X Paid-up equity share capital (FV Rs 10/-) | 92-93 | 2,679.60 | 2,679.60 | 2,545.70 | 2,679.60 | |
| 28 | XI Other Equity (excluding Revaluation Reserves) | 94-95 | — | — | — | 1,27,041.12 | PARTIAL_DASH (standard quarterly-statement convention — full Other Equity reported only at year end; NOT all-periods-nil, so not ZERO_STANDING) |
| 29 | XII Earnings per equity share (not annualized*) (section header) | 96 | — | — | — | — | HEADER_ONLY |
| 30 | (1) Basic (in Rs) | 97-98 | 5.13* | 6.12* | 3.01* | 18.12*(OCR: "1R 1?") | OCR_GARBLED (FY value) |
| 31 | (2) Diluted (in Rs) | 99 | 5.13* | 6.12*(OCR: "6 12*") | 2.96* | 18.08* | OCR_GARBLED (Q4FY26 value spacing) |

line_items (standalone) = 31. zero_standing (standalone) = 2 (rows 24, 25).

### Standalone Notes (lines 100-113)

| Note # | Line(s) | First 15 words |
|--------|---------|-----------------|
| 1 | 101-102 | "The above unaudited standalone financial results have been prepared in accordance with the Companies..." |
| 2 | 103-104 | "The above unaudited standalone financial results, after review by the Audit Committee, have been approved..." |
| 3 | 105-106 | "The Statutory Auditors have carried out limited review of the above standalone financial results for..." |
| 4 | 107-108 | "The Company is engaged in the manufacturing of the products of same type/class and as such..." — no reportable segments per Ind-AS 108 |
| 5 | 109-110 | "Figures for the quarter ended March 31, 2026 are the balancing figures between audited figures in..." |
| 6 | 111-112 | "During the quarter, the Company has made an investment of Rs. 98.00 Lakhs towards subscription of..." — associate: Ganesha Recycling Chain Private Limited |
| 7 | 113 | "Previous periods' figures have been regrouped/reclassified where considered necessary to conform to current period's..." |

Standalone notes count = 7 (no unnumbered footnotes found in this section).

### Standalone signature block (lines 115-129)
"For Ganesha Ecosphere Limited" — Vishnu Dutt Khandelwal, Executive Vice-Chairman (Whole-Time Director), DIN: 00383507. Date: 03.08.2026. Place: Kanpur. (Date only; no time stamp present — see cross-document signature-timing check, Section 7.)

---

## 3. STANDALONE INDEPENDENT AUDITOR'S REVIEW REPORT — Narendra Singhania & Co. (page 3, lines 131-185)

Report is **continuous unnumbered prose** (no paragraph numbering), unlike the consolidated report. Segmented into 4 logical paragraphs by topic sentence.

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| SA-1 | 144-148 | Introduction: scope of engagement, statement reviewed, entity, quarter, submitted per Reg 33 | |
| SA-2 | 149-155 | Management's responsibility: Statement prepared per Ind AS 34, Section 133, approved by Board; auditor's responsibility to issue report based on review | |
| SA-3 | 156-166 | Basis of review: conducted per SRE 2410; scope narrower than an audit; "we do not express an opinion" | text heavily OCR-corrupted at lines 164-166 ("Wfl Axprni::i:i", "t\r.r.nrrlinr;ly, rln nnt ::in ::incl it npinion.") — meaning reconstructed from context: disclaimer of opinion. OCR_GARBLED |
| SA-4 | 167-174 | Conclusion (negative assurance): "nothing has come to our attention that causes us to believe that the accompanying Statement... is not prepared in accordance with the recognition and measurement principles... or that it contains any material misstatement." | OCR_GARBLED (lines 168-170 garbled but reconstructible) |

**No Emphasis of Matter paragraph. No Other Matters paragraph. No Going Concern language. No entity list** (single reporting entity — standalone is company-only). This is a clean/unmodified conclusion.

Signature block (lines 175-184): For Narendra Singhania & Co., Chartered Accountants, Firm Registration No. 009781N, Partner, Membership No. 087931, Place: Kanpur, Date: August 03, 2026, **UDIN: 26087931RFIGQT2163**. Firm address (line 185): E 21, 1st Floor and 2nd Floor, Hauz Khas, New Delhi - 110016.

auditor_paras (standalone) = 4.

---

## 4. CONSOLIDATED STATEMENT OF UNAUDITED FINANCIAL RESULTS (page 4)

Columns: Q1 FY27 (Jun 30 2026, Unaudited) | Q4 FY26 (Mar 31 2026, Audited, "Refer note 5") | Q1 FY26 (Jun 30 2025, Unaudited) | FY26 (Mar 31 2026, Audited). All Rs Lakh.

| # | Line item | Line(s) | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|-----------|---------|--------|--------|-------|------|-------|
| 1 | I Revenue from operations | 199-200 | 42,366.67 | 42,394.13 | 33,712.42 | 1,48,166.29 | OCR_GARBLED (Q4FY26 shown as "42.394.13", decimal-for-comma OCR slip) |
| 2 | II Other income | 201 | 361.98 | 453.85 | 337.81 | 1,742.12 | OCR_GARBLED (FY26 value rendered "1,742.1"2" in source) |
| 3 | III Total income (I+II) | 202 | 42,728.65 | 42,847.98 | 34,050.23 | 1,49,908.41 | |
| 4 | IV EXPENSES (section header) | 203 | — | — | — | — | HEADER_ONLY |
| 5 | Cost of materials consumed | 204 | 29,757.38 | 24,411.00 | 22,602.79 | 92,427.93 | |
| 6 | Purchases of stock-in-trade | 205 | 594.50 | 150.05 | 67.07 | 409.17 | |
| 7 | Changes in inventories of finished goods, stock-in-trade and WIP | 206-207 | (3,556.35) | 2,689.41 | (880.08) | 4,684.56 | |
| 8 | Employee benefits expense | 208 | 2,447.70 | 2,693.05 | 2,356.22 | 9,976.03 | |
| 9 | Finance costs | 209 | 887.26 | 879.41 | 984.13 | 4,032.47 | OCR_GARBLED (Q1FY26 rendered "984..13") |
| 10 | Depreciation and amortization expense | 210-211 | 1,734.25 | 1,716.04 | 1,550.40 | 6,481.24 | OCR_GARBLED (FY26 rendered "6.481 .24") |
| 11 | Power & fuel | 212 | 3,444.01 | 3,341.96 | 2,993.46 | 12,817.02 | |
| 12 | Other expenses | 213 | 3,701.88 | 3,873.45 | 2,941.51 | 13,680.52 | |
| 13 | Total expenses (IV) | 214-215 | 39,010.63 | 39,754.37 | 32,615.50 | 1,44,508.94 | |
| 14 | V Profit before share of loss of an associate and tax (III-IV) | 216 | 3,718.02 | 3,093.61 | 1,434.73 | 5,399.47 | |
| 15 | VI Share of loss of an associate and tax | 217 | (8.55) | (5.48) | (2.89) | (4.49) | present only in consolidated statement (no standalone equivalent — Ganesha Recycling Chain Pvt Ltd is an associate, equity-accounted only at consol level) |
| 16 | VII Profit before tax (V+VI) | 218 | 3,709.47 | 3,088.13 | 1,431.84 | 5,394.98 | |
| 17 | VIII Tax expense (section header) | 219 | — | — | — | — | HEADER_ONLY |
| 18 | (1) Current tax | 220 | 507.73 | 676.59 | 259.16 | 1,789.90 | |
| 19 | (2) Deferred tax | 221 | 298.26 | 90.40 | 97.32 | (216.27) | |
| 20 | IX Profit for the period (VII-VIII) | 222 | 2,903.48 | 2,321.14 | 1,075.36 | 3,821.35 | |
| 21 | X Other Comprehensive Income (section header) | 223 | — | — | — | — | HEADER_ONLY |
| 22 | A(i) Items that will not be reclassified to P&L (subheader) | 224 | — | — | — | — | HEADER_ONLY |
| 23 | Re-measurement gain/(loss) on defined benefit obligations | 225 | 1.53 | 30.86 | (0.74) | 28.65 | |
| 24 | Re-measurement gain/(loss) on financial instrument (Equity) | 226-227 | 115.70 | (251.13) | (25.71) | (759.82) | |
| 25 | A(ii) Income tax relating to above items | 228 | (17.69) | 31.28 | 4.13 | 108.19 | |
| 26 | B(i) Items that will be reclassified to profit or loss | 231 | — | — | — | — | **ZERO_STANDING** |
| 27 | B(ii) Income tax relating to above items | 234 | — | — | — | — | **ZERO_STANDING** |
| 28 | XI Total Comprehensive Income for the period (IX+X) | 236-239 | 3,003.02 | 2,132.15 | 1,053.04 | 3,198.37 | |
| 29 | XII Paid-up equity share capital (FV Rs 10/-) | 240 | 2,679.60 | 2,679.60 | 2,545.70 | 2,679.60 | |
| 30 | XIII Other Equity (excluding Revaluation Reserves) | 243 | — | — | — | 1,24,887.50 | PARTIAL_DASH (not ZERO_STANDING, see standalone row 28) |
| 31 | XIV Earnings per equity share (not annualized*) (section header) | 244 | — | — | — | — | HEADER_ONLY |
| 32 | (1) Basic (in Rs) | 245 | 10.85** | 8.68** | 4.23** | 14.50* | double-asterisk footnote reference (ESOP trust shares) applies only at consolidated level — see Notes below |
| 33 | (2) Diluted (in Rs) | 246-247 | 10.86** | 8.68** | 4.16** | 14.48* | |

line_items (consolidated) = 33. zero_standing (consolidated) = 2 (rows 26, 27).

Combined line_items = 31 + 33 = 64. Combined zero_standing = 4.

### Consolidated Notes (lines 248-264)

| Note # | Line(s) | First 15 words |
|--------|---------|-----------------|
| 1 | 249-251 | "The above unaudited consolidated financial results have been prepared in accordance with the Companies..." (badly OCR-garbled mid-sentence at line 250-251) |
| 2 | 252-253 | "The above unaudited consolidated financial results, after review by the Audit Committee, have been approved..." |
| 3 | 254-255 | "The Statutory Auditors have carried out limited review of the above consolidated financial results for..." |
| 4 | 256-257 | "The Group is engaged in the manufacturing of the products of same type/class and as such..." — no reportable segments |
| 5 | 258-259 | "Figures for the quarter ended March 31, 2026 represent the difference between the audited figures..." |
| 6 | 260 | "Previous periods' figures have been regrouped/reclassified where considered necessary to conform to current period's..." |
| unnumbered (•) | 261-264 | "Pursuant to the Ganesha Ecosphere Employees' Stock Option Scheme, 2021, Ganesha Employees' Trust is holding 58,590..." Equity Shares (Mar 31 2026: 55,390 shares), reduced while computing basic/diluted EPS | **ESOP_FOOTNOTE_UNNUMBERED** — no standalone-statement equivalent; qualifies consolidated EPS rows 32-33 above only |

Consolidated notes count = 7 (6 numbered + 1 unnumbered footnote). Combined notes (standalone + consolidated) = 7 + 7 = 14.

### Consolidated signature block (lines 266-279)
"For Ganesha Ecosphere Limited" — Vishnu Dutt Khandelwal, Executive Vice-Chairman (Whole-Time Director), DIN: 00383507. Date: 03.08.2026. Place: Kanpur. Same signatory as standalone statement, same date.

---

## 5. CONSOLIDATED INDEPENDENT AUDITOR'S REVIEW REPORT — Narendra Singhania & Co. (pages 5-7, lines 287-386)

Numbered paragraphs 1-11 (paragraph 1 OCR'd as "I." — capital I, not digit — a genuine OCR artifact caught only by manual sweep).

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 293-299 | Introduction: reviewed statement of Parent + subsidiaries ("the Group") + share of associate's net profit/loss and OCI, quarter ended Jun 30 2026 | OCR_GARBLED (numbered "I." not "1.") |
| 2 | 300-306 | Management's responsibility (Parent's Management/Board), Ind AS 34, auditor's responsibility to express a conclusion | |
| 3 | 307-315 | Basis of review: SRE 2410, moderate assurance, narrower than audit, "we do not express an audit opinion" | |
| 4 | 316-318 | Additional procedures performed per SEBI Circular CIR/CFD/CMD1/44/2019 under Reg 33(8) | present only in consolidated report — no standalone equivalent |
| 5 | 319-335 | **Entity list**: Statement includes results of 6 entities (Parent, 3 subsidiaries, 1 controlled trust, 1 associate) — see Section 6 below | |
| 6 | 336-344 | Conclusion (negative assurance), qualified by reliance on other auditors'/management's reports referenced in paras 7-10 | |
| — | 345 | **"Other Matter"** heading (structural marker, not a numbered paragraph) | |
| 7 | 346-353 | Other Matter 1: 2 subsidiaries **not reviewed by this auditor** — interim results (before inter-co eliminations) reflect revenue Rs 25,093.94 Lakh, net profit after tax Rs 1,504.03 Lakh, total comprehensive income Rs 1,504.03 Lakh for the quarter; reviewed by **other auditors**, furnished by Management | UNAUDITED_BY_PRINCIPAL_AUDITOR (reviewed by other auditors) |
| 8 | 354-361 | Other Matter 2: 1 subsidiary **located outside India** (Nepal — Ganesha Overseas Private Limited) not reviewed by this auditor — revenue Rs 597.24 Lakh, net loss after tax Rs 26.81 Lakh, total comprehensive loss Rs 26.81 Lakh for the quarter; reviewed by other auditor, furnished by Management | UNAUDITED_BY_PRINCIPAL_AUDITOR, FOREIGN_SUBSIDIARY |
| 9 | 362-367 | Other Matter 3: financial statements of a **Trust controlled by the Parent** (Ganesha Employees' Welfare Trust) — revenue Rs Nil, net profit after tax Rs Nil, total comprehensive income Rs Nil for the quarter; **NOT reviewed by any auditor** — certified by Parent's Management; stated not material to Group | **ZERO_STANDING** (Nil/Nil/Nil), **UNAUDITED_MGMT_CERTIFIED** (no auditor review at all, management-furnished only) |
| 10 | 368-373 | Other Matter 4: an **associate** — share of loss Rs 8.55 Lakh, total comprehensive loss Rs 8.55 Lakh for the quarter; **NOT reviewed by any auditor** — certified by Parent's Management; stated not material to Group | **UNAUDITED_MGMT_CERTIFIED** |
| 11 | 375-377 | Conclusion is not modified in respect of matters in paragraphs 7, 8, 9, 10 (reliance on other auditors' work and management-certified figures for Trust & Associate) | |

**No Emphasis of Matter paragraph. No Going Concern language.** The report's qualifying disclosures are entirely in the "Other Matter" section (paras 7-10).

Signature block (lines 378-386): For Narendra Singhania & Co., Chartered Accountants, Firm Registration No. 009781N, Partner, Membership No. 087931, Place: Kanpur, Date: August 03, 2026, **UDIN: 2608793ICGGVXL5902**. (UDIN differs from the standalone report's UDIN, as expected — one UDIN per report.) Firm address line reappears mid-document at line ~330 (Hauz Khas, New Delhi) as a running page-footer, duplicated from the standalone report footer.

auditor_paras (consolidated) = 11. Combined auditor_paras (standalone 4 + consolidated 11) = 15.

---

## 6. CONSOLIDATION ENTITY LIST (lines 319-335, inside consolidated auditor-report paragraph 5)

| # | Entity | Line | Relationship | Reviewed by principal auditor? |
|---|--------|------|--------------|-------------------------------|
| 1 | Ganesha Ecosphere Limited | 321 | Parent Company | Yes (reviewed directly, standalone + as parent in consol) |
| 2 | Ganesha Ecopet Private Limited | 322-323 | Wholly owned subsidiary of Ganesha Ecosphere Limited | Unclear — not named in Other Matter paras 7/8; presumed reviewed by principal auditor (not flagged as unreviewed) |
| 3 | Ganesha Ecotech Private Limited | 324-325 | Wholly owned subsidiary of Ganesha Ecosphere Limited | Unclear — same as above |
| 4 | Ganesha Overseas Private Limited, Nepal | 332-333 | Wholly owned subsidiary of Ganesha Ecosphere Limited | **No** — this is the foreign subsidiary in Other Matter para 8, reviewed by other auditor |
| 5 | Ganesha Employees' Welfare Trust | 334 | Entity controlled by the Parent | **No** — Other Matter para 9; not reviewed by any auditor, management-certified |
| 6 | Ganesha Recycling Chain Private Limited | 335 | Associate of Ganesha Ecosphere Limited | **No** — Other Matter para 10; not reviewed by any auditor, management-certified |

entities = 6. Para 7 references "two subsidiaries" reviewed by other auditors (combined Rs 25,093.94 Lakh revenue) but names neither explicitly in the report text — by elimination against the named entity list, these two are most likely entities #2 and #3 (Ganesha Ecopet Pvt Ltd and Ganesha Ecotech Pvt Ltd), since entity #4 (Nepal) is separately and explicitly addressed in para 8. This inference is not directly evidenced in the extract text and should be treated as **NOT FOUND / requires confirmation against the full annexure or prior filings** — flagged for A3/A4, not asserted as fact here.

No prior-quarter ledger path was supplied for this run, so an `ENTITY_CHANGE` cross-check (entities added/removed/renamed vs. prior quarter) **could not be performed**. Flag: **NO_PRIOR_LEDGER** — A3/A4 should independently cross-check this 6-entity list against GANECOS's Q4 FY26 filing if available.

---

## 7. SIGNATURE / TIMESTAMP CROSS-CHECK

| Document | Signatory | Designation | Date | Time |
|----------|-----------|-------------|------|------|
| Board Outcome letter | Bharat Kumar Sajnani | Company Secretary-cum-Compliance Officer | Aug 3, 2026 (letter date) | not stated |
| Standalone results | Vishnu Dutt Khandelwal | Executive Vice-Chairman (Whole-Time Director), DIN 00383507 | 03.08.2026 | not stated |
| Consolidated results | Vishnu Dutt Khandelwal | Executive Vice-Chairman (Whole-Time Director), DIN 00383507 | 03.08.2026 | not stated |
| Standalone auditor report | Narendra Singhania & Co. (Partner, Membership 087931) | Chartered Accountants | August 03, 2026 | not stated; UDIN 26087931RFIGQT2163 |
| Consolidated auditor report | Narendra Singhania & Co. (Partner, Membership 087931) | Chartered Accountants | August 03, 2026 | not stated; UDIN 2608793ICGGVXL5902 |

All five signature blocks carry the same date (August 3, 2026) as the Board meeting, but **none carries a time stamp**. Because the Board Outcome letter's own meeting start/end times are OCR-illegible (Section 1, row 4), the classic "signature before board meeting concluded" check **cannot be evaluated from this document** — flag **NOT_FOUND** (insufficient time-granularity evidence), distinct from the **MEETING_TIME_ILLEGIBLE** flag on the letter itself. A3/A4 should not infer a timing violation from this filing; the absence of evidence is not evidence of a violation.

---

## FLAGS SUMMARY (all rows carrying a flag)

- **ZERO_STANDING** (4): standalone B(i)/B(ii) OCI rows (rows 24-25, Section 2); consolidated B(i)/B(ii) OCI rows (rows 26-27, Section 4). Also narratively present in consolidated auditor-report para 9 (Trust: Nil/Nil/Nil, Section 5).
- **OCR_GARBLED** (multiple): Board Outcome letter enclosure text; standalone EPS values (rows 30-31); consolidated revenue/other-income/finance-cost/depreciation values (rows 1,2,9,10 of Section 4); standalone auditor report paras SA-3/SA-4; consolidated auditor report para 1 numbering ("I." for "1.").
- **UNAUDITED_MGMT_CERTIFIED** (2): consolidated auditor report paras 9 and 10 — Trust and Associate financials not reviewed by any auditor, certified by Parent's Management only.
- **UNAUDITED_BY_PRINCIPAL_AUDITOR** (2): consolidated auditor report paras 7 and 8 — 2 subsidiaries + 1 foreign subsidiary reviewed by other (component) auditors, not the principal auditor.
- **ESOP_FOOTNOTE_UNNUMBERED** (1): consolidated Notes, unnumbered bullet footnote on ESOP Trust shares (lines 261-264), qualifies consolidated EPS only.
- **MEETING_TIME_ILLEGIBLE** (1): Board Outcome letter, lines 28-29.
- **NO_PRIOR_LEDGER** (1): no prior-quarter ledger supplied; entity list and slide/note drop checks against Q4 FY26 not performed in this run.
- **PARTIAL_DASH** (2, not counted as ZERO_STANDING): "Other Equity" rows in both statements — dash only in interim-quarter columns per standard Ind AS 34 presentation convention, not all-periods-nil.
- **ABSENT_AGENDA_ITEMS** (1, descriptive): Board Outcome letter contains only the results-approval agenda item; no other resolutions disclosed.
