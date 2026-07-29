# A2 COMPLETENESS LEDGER — PNGS REVA DIAMOND JEWELLERY LIMITED (PNGSREVA), Q1 FY27, Results filing

Source: `extract_results_pngs_q1fy27.txt` (6 pages, standalone-only Reg 33 filing: Board Outcome
letter, Auditor's Limited Review Report, Unaudited Standalone Financial Results, Notes incl.
IPO-proceeds utilisation, Management Comments). Unit convention: INR Million (x0.1 = Rs Crore).
No prior-quarter ledger exists for this ticker (first `/run-quarterly` cycle) — no diff possible;
`ENTITY_CHANGE` / `DROPPED_SLIDE` checks are therefore N/A this cycle, noted where relevant.

```
=== A2 COUNT TEST ===
category: agenda_items              grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras             grep_count: 4   sweep_count: 4   match: yes
category: line_items (value rows)   grep_count: 24  sweep_count: 24  match: yes  (see note A)
category: notes                     grep_count: 7   sweep_count: 7   match: yes  (see note B)
category: ipo_utilisation_lines     grep_count: 4   sweep_count: 4   match: yes  (see note C)
category: management_comments_items grep_count: 4   sweep_count: 4   match: yes  (see note D)
category: entities                  grep_count: 1   sweep_count: 1   match: yes  (standalone only)
category: signature_blocks          grep_count: 4   sweep_count: 4   match: yes
gate_a2: pass
=== END COUNT TEST ===
```

**Reconciliation notes (mismatch caught and resolved before gate close):**
- **Note A (line_items):** first-pass naive grep `\([0-9]` OR two-decimal pattern returned 26
  hits over lines 177-223 — 2 false positives were label fragments split across OCR line-wraps
  with no independent value (`(1)` in the "Profit before tax (1) - (2)" label at line 192, and
  `(5+6)` in the "Total comprehensive income ... (5+6)" label at line 215). Refined grep
  `\(?[0-9]{1,3}(,[0-9]{3})*\.[0-9]{2}\)?` returns 24, matching the manual sweep of 24
  independent value-bearing rows. Re-swept and reconciled.
- **Note B (notes):** first-pass grep anchored on `^\s*[0-9]+\s+(The|During)` returned 6 —
  missed Note 7 ("Previous period/year figures have been regrouped...", line 281, which does not
  start with "The"/"During"). Broadened grep to `^\s*[0-9]+\s+[A-Za-z]` over the notes block
  (lines 238-282) returns 7, matching manual sweep. Re-swept and reconciled.
- **Note C (IPO utilisation lines):** first-pass grep for rows starting with a capitalised label
  followed by two-decimal figures returned 3 — missed the "Marketing and promotional expenses..."
  row because its label wraps across two source lines (274-275) and the value cluster sits on the
  second (lowercase-starting) line. Manual sweep of the table found all 4 rows (3 objects + Total).
  Re-swept and reconciled.
- **Note D (management_comments_items):** first-pass grep `^\s*[0-9]+\.\s` returned 3 — missed
  item 2 ("website", line 333) because the source line has a leading bullet glyph (`•`) before the
  numeral, pushing the digit off column 1. Manual sweep of the "Management Comments" section
  (lines 305-345) found all 4 numbered items. Re-swept and reconciled.

---

## 1. Board Outcome Letter — agenda items (lines 15-46)

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 15-16, 28-32 | Approval of Q1 FY27 unaudited standalone results | Board, at meeting held July 29, 2026, approved Unaudited Standalone Financial Results for quarter ended June 30, 2026, per Reg 33; Auditor's Limited Review Report enclosed as Annexure I | — |

No other agenda items present in the letter: no AR/annual-report approval, no AGM notice, no
record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer
appointment, no ESOP grant, no capital-raising enabling resolution. Confirmed by keyword sweep
(`approved|resolved|appointed|record date|dividend|AGM|scrutinizer|ESOP|ratif`) over lines 15-46 —
only the single "approved" hit above.

**Board meeting timing (line 32):** commenced 12:00 p.m., ended 1:15 p.m. — duration 1h15m for a
single-item (results-only) meeting.

---

## 2. Auditor's Independent Review Report — paragraphs (lines 74-153)

| Para | Line | Content (first ~15 words) | Type | Flags |
|------|------|---------------------------|------|-------|
| Title/addressee | 74-79 | "Independent Auditor's Review Report on unaudited financial results... pursuant to Regulation 33..." addressed "To The Board of Directors" | Header | — |
| 1 | 82-86 | "We have reviewed the accompanying statement of unaudited financial results of PNGS Reva Diamond Jewellery..." | Scope of engagement | — |
| 2 | 88-94 | "This Statement, which is the responsibility of the Company's Management and has been approved by the Company's Board..." | Management responsibility / Ind AS 34 basis | — |
| 3 | 97-105 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | Basis of review; explicit "we do not express an audit opinion" | — |
| 4 | 125-130 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." | Conclusion — unmodified/clean | — |

No separate Emphasis of Matter paragraph, no Other Matters paragraph, no Going Concern paragraph.
Entity list reviewed: single entity, PNGS Reva Diamond Jewellery Limited (standalone) — no
subsidiary/JV entities are subject to this review since this is a standalone-only filing.
No entity within scope is flagged as unaudited/management-furnished other than the entity itself
(reviewed, not audited, consistent with a quarterly Reg 33 review report).

**Auditor signature block (lines 135-153):** MSKA & Associates LLP (Formerly M S KA & Associates),
Chartered Accountants, ICAI FRN 105047W/W101187; Partner: "Yewale" (OCR-garbled first name,
rendered "g h Yewale"); Membership No. 158877; UDIN present but OCR-garbled
("J..615 8877AAJMWB353" — digits do not parse to a clean 18-character UDIN, likely OCR corruption
of the leading year/membership digits); Place: Pune; Date: July 29, 2026. No digital-certificate
timestamp captured in the extract for this signature (contrast with the CS signature below, which
carries one).

---

## 3. Statement of Unaudited Financial Results — table structure and line items (lines 167-223)

Four reporting columns each row: Q ended Jun 30 2026 (Unaudited), Q ended Mar 31 2026 (Unaudited,
Note 4), Q ended Jun 30 2025 (Audited, Note 5), Year ended Mar 31 2026 (Audited).

### 3a. Structural / section-header rows (no independent value of their own — 6 rows)

| Sr | Line | Header | Groups |
|----|------|--------|--------|
| 1 | 177 | Income | Revenue from operations, Other income, Total Income |
| 2 | 182 | Expenses | 6 expense lines + Total Expenses |
| 4 | 194 | Tax expenses | Income Tax charge, Deferred tax, Earlier year taxes, Total tax expenses |
| 6 | 205 | Other comprehensive income | sub-header + 3 lines below |
| — | 206-207 | "Items that will not be reclassified subsequently to profit and loss:" | Re-measurement gain/(loss), Income tax effect on above |
| — | 221 | "Earnings per equity share (Not annualized for quarter):" | Basic (INR), Diluted (INR) |

### 3b. Value-bearing line items (24 rows — reconciled count, see Note A above)

| Sr | Line | Particulars | Q1 FY27 | Q4 FY26 | Q1 FY26 | FY26 | Flags |
|----|------|-------------|---------|---------|---------|------|-------|
| — | 178 | Revenue from operations | 1,179.73 | 1,381.26 | 537.49 | 4,390.28 | — |
| — | 179 | Other income | 55.76 | 15.22 | 2.87 | 20.35 | — |
| — | 180 | **Total Income** | 1,235.49 | 1,396.48 | 540.36 | 4,410.63 | — |
| — | 183 | Purchases of stock-in-trade | 1,066.19 | 964.44 | 595.32 | 4,737.05 | — |
| — | 184 | Changes in inventories of finished goods | (304.78) | 33.76 | (227.01) | (1,561.37) | — |
| — | 185 | Employee benefits expense | 22.90 | 21.72 | 14.69 | 79.78 | — |
| — | 186 | Finance costs | 27.48 | 31.20 | 19.85 | 98.67 | — |
| — | 187 | Depreciation and amortization expense | 3.57 | 2.38 | 0.38 | 6.63 | — |
| — | 188 | Other expenses | 56.15 | 55.56 | 38.66 | 185.15 | — |
| — | 189 | **Total Expenses** | 871.51 | 1,109.06 | 441.89 | 3,545.91 | — |
| 3 | 192/195 | Profit before tax (1) - (2) | 363.98 | 287.42 | 98.47 | 864.72 | — |
| — | 198 | Income Tax charge | 92.80 | 70.34 | 24.98 | 218.90 | — |
| — | 199 | Deferred tax charge/(credit) | (0.92) | 2.71 | (0.99) | (1.01) | — |
| — | 200 | Earlier year taxes | *(blank)* | 0.28 | *(blank)* | 0.28 | **ZERO_STANDING** (nil in current qtr and Q1FY26; only populated for the two Mar-31-2026 columns) |
| — | 201 | **Total tax expenses** | 91.88 (printed "91,88") | 73.33 | 23.99 | 218.17 | OCR: comma/period typo in source, not a value error |
| 5 | 203 | Profit for the period/year (3) - (4) | 272.10 | 214.09 | 74.48 | 646.55 (printed "646,55") | — |
| — | 208 | Re-measurement gains/(loss) on defined benefit plans | (0.16) | (0.39) | (0.41) | (0.59) | — |
| — | 209 | Income tax effect on above | 0.04 | 0.10 | 0.10 | 0.15 | — |
| — | 210 | **Total other comprehensive income/(loss)** | (0.12) | (0.29) | (0.31) | (0.44) | — |
| 7 | 213-215 | Total comprehensive income, net of tax (5+6) | 271.98 | 213.80 | 74.17 | 646.11 | — |
| 8 | 218 | Paid-up equity share capital (FV INR 10 each) | 316.98 | 316.98 | 218.66 | 316.98 | — |
| — | 219 | Other equity | *(blank)* | *(blank)* | *(blank)* | 4,835.02 | **ZERO_STANDING** (balance-sheet line disclosed only for FY-end column, standard Reg 33 quarterly practice, not a transaction absence) |
| — | 222 | Basic EPS (INR), not annualized | 8.58 | 8.40 | 3.41 | 28.41 | — |
| — | 223 | Diluted EPS (INR), not annualized | 8.58 | 8.40 | 3.41 | 28.41 | Basic = Diluted every period — no dilutive instruments outstanding |

`zero_standing` count for this filing = **2** (Earlier year taxes; Other equity).

---

## 4. Notes to the Unaudited Financial Results (lines 238-282)

| Note | Line | First ~15 words | Flags |
|------|------|------------------|-------|
| 1 | 242-244 | "The above financial results for the quarter ended June 30, 2026 have been reviewed by the Audit Committee..." | — |
| 2 | 246-248 | "The above financial results have been prepared in accordance with the recognition and measurement principles laid down in Ind AS 34..." | — |
| 3 | 251-254 | "The Company is engaged in the business of trading diamond jewellery, platinum jewellery and other precious stones..." — single reportable segment (Ind AS 108), no single customer >10% of revenue | — |
| 4 | 257-258 | "The figures for quarter ended March 31, 2026 are the balancing figures between audited figures... and published year to date unaudited figures for the nine months..." | — |
| 5 | 259-260 | "The figures for the quarter ended June 30, 2025 are based on audited special purpose financial statements... unmodified opinion vide their audit report dated October 18, 2025." | Note the prior-year comparative quarter is a *special-purpose* audited statement, not a regular quarterly review — worth tracking for comparability in A3/A4 |
| 6 | 261-279 | "During the financial year ended March 31, 2026 the Company had completed the Initial Public Offering (IPO) and the details of utilisation..." — introduces IPO utilisation table (see §5 below) | — |
| 7 | 281 | "Previous period/year figures have been regrouped/ rearranged wherever considered necessary." | Boilerplate regrouping note — no specifics of what was regrouped given |

**Signature block for Notes section (lines 284-292):** "For and on behalf of Board of Directors,
PNGS Reva Diamond Jewellery Limited" — Govind Gadgil, Director, DIN 00616617, Place: Pune, Date:
July 29, 2026. Image/scanned signature in extract, no digital-certificate timestamp captured.

---

## 5. Note 6 sub-table — IPO net-proceeds utilisation (lines 265-279)

Columns: Amount to be Utilised (per Prospectus) | Amount Utilised upto June 30, 2026 | Un-utilized amount as on June 30, 2026 (#)

| # | Line | Object | To be utilised | Utilised to date | Un-utilised | Flags |
|---|------|--------|-----------------|-------------------|-------------|-------|
| 1 | 273 | Funding expenditure towards setting-up of 15 New Stores | 2,865.64 | 404.88 | 2,460.76 | Only 14.1% utilised as of Q1FY27 vs full prospectus object — pace-of-utilisation watch item for A4 |
| 2 | 274-275 | Marketing and promotional expenses for launch of the 15 New Stores (brand "Reva") | 354.00 | 4.61 | 349.39 | Only 1.3% utilised — same watch item |
| 3 | 277 | General corporate purposes | 271.59 | 236.11 | 35.48 | 86.9% utilised — contrast with the two objects above |
| 4 | 278 | **Total** | 3,491.23 | 645.60 | 2,845.63 | Only 18.5% of net IPO proceeds utilised as of Q1FY27 |
| footnote | 279 | "# IPO proceeds which are unutilised... temporarily retained in fixed deposits & monitoring account." | — | — | — | Footnote qualifying the "Un-utilised" column |

---

## 6. Management Comments section (lines 305-355)

| # | Line | Item | Detail | Flags |
|---|------|------|--------|-------|
| 1 | 309-320 | Summary of Revenue (sub-table, 3 rows, see §6a) | Revenue split: Diamond studded jewellery vs Gold Sales | — |
| — | 322-331 | Footnote/explanation on Gold Sales line (3 paragraphs, marked with `*`) | Gold sales are incidental — customer old-gold exchange excess, not bullion trading | — |
| 2 | 333-336 | Website | Results to be published on BSE, NSE, and company website | — |
| 3 | 338-340 | Store count | 34 SIS stores with P.N. Gadgil & Sons Ltd + 3 exclusive brand stores as of July 29, 2026, vs 34 SIS + 2 exclusive brand stores as of March 31, 2026 | Net +1 exclusive brand store added in the quarter — operating KPI |
| 4 | 342-343 | Advance tax paid | Rs 30.00 million advance tax paid for Tax Year 2026-27 up to July 29, 2026 | — |

### 6a. Summary of Revenue sub-table (lines 317-320)

| Line | Particulars | Q1 FY27 (Unaudited) | Q1 FY26 (Audited) | FY26 (Audited) | Flags |
|------|-------------|----------------------|---------------------|-----------------|-------|
| 317-318 | Diamond studded jewellery incl. precious stones | 1,159.87 | 521.65 | 3,821.01 | — |
| 319 | Gold Sales* | 19.86 | 15.84 | 569.27 | Footnoted — incidental gold from customer exchange, not bullion trading (lines 322-331) |
| 320 | **Total Revenue from operations** | 1,179.73 | 537.49 | 4,390.28 | Ties to line 178 in main P&L — cross-check clean |

**Signature block for Management Comments section (lines 350-355):** Govind Gadgil, Chairman &
Director, DIN 00616617, Place: Pune, Date: July 29, 2026. Same individual as the Notes-section
signatory (line 290) but with a different designation given ("Director" at line 291 vs "Chairman &
Director" at line 352) — worth a consistency note for A3, not a hard flag.

---

## 7. Entities in scope (standalone-only filing)

| # | Line | Entity | Relationship | Flags |
|---|------|--------|---------------|-------|
| 1 | throughout | PNGS Reva Diamond Jewellery Limited (CIN L32111PN2024PLC236494), formerly Gadgil Metals & Commodities | Reporting entity, standalone | No consolidated financials in this filing; no subsidiary/JV/associate list present to enumerate. `ENTITY_CHANGE` check is N/A this cycle (no prior-quarter list to diff against — first `/run-quarterly` cycle for this ticker) |

---

## 8. Signature / digital-certification blocks (all occurrences)

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 36-44 | Kirti Suryakant Vaidya | Company Secretary & Compliance Officer (ICSI M. No. A31430) | Digitally signed 2026.07.29 13:23:49 +05'30 | Board meeting ended 1:15 p.m. (13:15); signature timestamp 13:23:49 is ~8 minutes **after** meeting close — normal sequencing, not the "signed-before-conclusion" red flag pattern |
| 2 | 135-153 | "Yewale" (OCR-garbled given name), Partner, MSKA & Associates LLP | Engagement Partner, Membership No. 158877 | Typed date only ("July 29, 2026"); UDIN present but OCR-garbled, no digital-cert timestamp captured | UDIN string does not cleanly parse — flag for A3 to request clean UDIN from source PDF/BSE annex if precision needed |
| 3 | 288-292 | Govind Gadgil | Director, DIN 00616617 (signing Notes to Financial Results) | Typed date only ("Date: July 29, 2026"); image-based signature, no digital-cert timestamp captured | — |
| 4 | 350-355 | Govind Gadgil | Chairman & Director, DIN 00616617 (signing Management Comments) | Typed date only ("Date: July 29, 2026") | Designation differs from #3 above (Director vs Chairman & Director) for the same DIN in the same filing |

---

## 9. Categories checked and confirmed NOT PRESENT in this filing

| Category | Status |
|----------|--------|
| Consolidated financial results | Not present — standalone-only filing per header/instructions |
| Shareholding pattern table | Not present in this extract |
| Segment reporting table | Not present — Note 3 explicitly states single reportable segment, no table given |
| Director profile annexure (DIN/term/background table) | Not present — this filing has no director appointment/resignation agenda item |
| Concall transcript | N/A — this is a results-filing doctype, not a transcript |
| Investor presentation / slides | N/A — this is a results-filing doctype, not a deck |
| Prior-quarter ledger for diff (`ENTITY_CHANGE`, `DROPPED_SLIDE`) | Not available — first `/run-quarterly` cycle for PNGSREVA |

Repeated page-footer boilerplate (company letterhead, CIN, GST number, address, watermark-style
character noise from OCR) appears on all 6 pages (e.g. lines 51-58, 228-236, 297-303, 359-366).
This is letterhead artifact, not a distinct disclosure unit, and is excluded from the counts above
by design — noted here so it is not mistaken for an omission.

---

## Summary counts

| Category | Count |
|----------|-------|
| Agenda items (Board Outcome letter) | 1 |
| Auditor report paragraphs (numbered) | 4 |
| P&L value-bearing line items | 24 |
| P&L structural/header rows | 6 |
| Zero/nil-standing line items (subset of the 24) | 2 |
| Notes to Financial Results | 7 |
| IPO utilisation table rows (incl. Total) | 4 |
| IPO utilisation footnotes | 1 |
| Management Comments numbered items | 4 |
| Summary-of-Revenue sub-table rows | 3 |
| Entities in scope | 1 |
| Signature/certification blocks | 4 |

**flags_raised: [ZERO_STANDING] (x2: Earlier year taxes; Other equity)**
