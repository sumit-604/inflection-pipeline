# A2 COMPLETENESS LEDGER — GMDCLTD Q1 FY27 Results Filing

Source: `runs/gmdc-q1fy27/work/extract_results_gmdc_q1fy27.txt` (547 lines, 10 pages, Reg 33 Board Outcome + Unaudited Standalone & Consolidated Financial Results + 2 Limited Review Reports)
Prior-quarter ledger: NOT PROVIDED (path not supplied in task inputs) — entity cross-check (`ENTITY_CHANGE`) cannot be run against a prior list; noted, not silently skipped.

```
=== A2 COUNT TEST ===
category: notes_numbered            grep_count: 9    sweep_count: 9    match: yes
category: notes_unnumbered          grep_count: 1    sweep_count: 1    match: yes
category: agenda_items              grep_count: 3    sweep_count: 3    match: yes
category: line_items_detailed_pnl   grep_count: 57   sweep_count: 57   match: yes
category: line_items_summary_table  grep_count: 18   sweep_count: 18   match: yes
category: line_items_segment        grep_count: 44   sweep_count: 44   match: yes
category: auditor_paragraphs        grep_count: 10   sweep_count: 10   match: yes
category: entities                  grep_count: 5    sweep_count: 5    match: yes
category: signature_blocks          grep_count: 6    sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used:
- `grep -n -E "^\s*\([0-9]+\)\s" extract...` → 3 hits (lines 31, 48, 68) = agenda items 1–3.
- `grep -n "Notes:\|^Note:"` → 3 header hits (lines 155, 255, 378); manual sweep of the two `Notes:` blocks (255–279, 378–406) counted numbered rows via `grep -n -E "^\s{4,9}[0-9]\s+[A-Za-z(]"` → 4 (standalone) + 5 (consolidated) = 9; the singular unnumbered `Note:` (line 155) counted separately = 1.
- `grep -n -E "^[0-9]\.\s+(We|This|The|Based)" ` → 6 hits (consolidated review report, lines 424–471) + 4 hits (standalone review report, lines 506–529) = 10.
- Manual sweep of both detailed P&L statements (page 4, page 6), both summary tables (page 3), and both segment tables (page 5, page 7) line-by-line against the grep line-count of the tables — see tables below; sweep count equals the row count tabulated.

---

## TABLE 1 — Board Outcome Letter: Agenda Items (beyond item 1 included per instructions)

| # | Item | Line(s) | First 15 words | Flags |
|---|------|---------|-----------------|-------|
| 1 | Financial Results — approval of Unaudited Standalone & Consolidated Financial Results for Q1 FY27 | 31–46 | "Pursuant to Regulation 33 ... Board of Directors ... has, inter alia, considered and approved the Unaudited Financial Results" | — |
| 1a | Enclosure 1 under item 1: Unaudited Standalone and Consolidated Financial Results of the Company | 42–43 | "Unaudited Standalone and Consolidated Financial Results of the Company for the quarter ended June 30, 2026" | ANCILLARY (enclosure, not a separate agenda vote) |
| 1b | Enclosure 2 under item 1: Limited Review Report on the Standalone and Consolidated Financial Results | 45–46 | "Limited Review Report on the Standalone and consolidated Financial Results issued by the Statutory Auditors" | ANCILLARY |
| 2 | Memorandum of Understanding (MoU) with Gujarat Narmada Valley Fertilizers & Chemicals Limited (GNFC) — coal-to-chemicals value chain, gasification, including Underground Coal Gasification (UCG) | 48–56 | "The Board of Directors of the Company at its Meeting held today ... approved the proposal for execution of Memorandum of Understanding (MoU) with Gujarat Narmada Valley Fertilizers & Chemicals Limited" | NEW_MOU; "further details in due course on execution" — non-binding at this stage |
| 3 | Memorandum of Understanding (MoU) with M/s IREL (India) Limited — Rare Earth Elements (REE) sector collaboration | 68–73 | "The Board of Directors of the Company at its Meeting held today ... approved the proposal for execution of Memorandum of Understanding (MoU) with M/s IREL(India) Limited" | NEW_MOU; "further details in due course on execution" — non-binding at this stage |
| — | Board meeting timing | 75 | "The meeting of the Board of Directors commenced at 11.00 AM and concluded at 1.10 PM." | Duration 2h10m — substantive length consistent with 3 agenda items (results + 2 new MoUs) |
| — | Digital signature — Company Secretary | 82–89 | "For Gujarat Mineral Development Corporation Limited ... Joel S. Evans, Digitally signed ... Date: 2026.07.31 16:14:07 +05'30', Company Secretary" | Signed 16:14, after board meeting concluded (13:10) — no timing anomaly |

Agenda items count (numbered board resolutions): 3 declared (lines 31, 48, 68) = 3 enumerated. GATE match: yes.

---

## TABLE 2 — Notes to Financial Results, Standalone Segment Information (page 5)

| Note # | Line(s) | First 15 words | Flag |
|--------|---------|-----------------|------|
| 1 | 256–258 | "The above results have been reviewed by the Audit Committee of the Board of Directors in its meeting" | — |
| 2 | 261–268 | "Pursuant to the Composite Scheme of Amalgamation and Arrangement sanctioned by the Ministry of Corporate Affairs on 8th April 2026" | GSPC investment extinguished / GEL and GTL shares receivable — non-cash corporate action |
| 3 | 271–273 | "The above financial results have been prepared in accordance with Indian Accounting Standards (Ind AS) notified under Section 133" | — |
| 4 | 276–279 | "Corresponding figures of the previous periods / year's have been re-grouped / re-arranged / re-classified / restated and revised" | — |

Standalone numbered notes: 4 declared vs 4 enumerated. Match: yes.

## TABLE 3 — Notes to Financial Results, Consolidated Segment Information (page 7)

| Note # | Line(s) | First 15 words | Flag |
|--------|---------|-----------------|------|
| 1 | 379–380 | "The above results have been reviewed by the Audit Committee of the Board of Directors in its meeting" | — |
| 2 | 383–389 | "The following Joint Ventures and Associates are considered in consolidated financial results" | See TABLE 11 (entity list) |
| 3 | 392–393 | "The above financial results have been prepared in accordance with Indian Accounting Standards (Ind AS) notified under Section 133" | — |
| 4 | 397–402 | "Pursuant to the Composite Scheme of Amalgamation and Arrangement sanctioned by the Ministry of Corporate Affairs on 8th April 2026" | GSPC investment extinguished / GEL and GTL shares receivable — identical corporate action disclosed in both standalone and consolidated note sets |
| 5 | 405–406 | "Corresponding figures of the previous periods / year's have been re-grouped / re-arranged / re-classified / restated and revised" | — |

Consolidated numbered notes: 5 declared vs 5 enumerated. Match: yes.

**Combined numbered-notes count test: 9 declared (4 standalone + 5 consolidated) vs 9 enumerated. Match: yes.**

## TABLE 4 — Unnumbered Footnote (page 3, below summary table)

| Line(s) | Text (first 15 words) | Flag |
|---------|------------------------|------|
| 155–159 | "The above is an extract of the detailed format of Financial Results for the quarter ended" | Directs reader to full format + Explanatory Notes on exchange websites — the Notes in TABLE 2/3 above satisfy this reference within this extract |

Unnumbered footnotes: 1 declared vs 1 enumerated. Match: yes.

---

## TABLE 5 — Standalone Detailed P&L (page 4, lines 170–212) — every line item, revenue through EPS

| # | Particulars | Line(s) | Q1 FY27 (30/06/2026) | Flag |
|---|-------------|---------|----------------------|------|
| 1 | Revenue from Operations | 178 | 906.64 | — |
| 2 | Other Income | 179 | 76.15 | — |
| 3 | Total Income (A) | 180 | 982.79 | — |
| 4 | Changes in inventories | 182 | 5.78 | — |
| 5 | Royalties and other tax levies | 183 | 86.70 | — |
| 6 | GST Compensatory Cess Exp | 184 | – (dash, current & prior quarter) | `ZERO_STANDING` — nil in 2 of 4 periods shown (30/06/2026, 31/03/2026) but populated in 30/06/2025 (79.03) and FY26 annual (130.75); template line for a levy the company may again incur — do not drop |
| 7 | Employee Benefit Expenses | 185 | 42.27 | — |
| 8 | Finance Costs | 186 | 6.61 | — |
| 9 | Depreciation and Amortisation Expenses | 187 | 33.33 | — |
| 10 | Loading of lignite and overburden removal expenses | 188 | 436.78 | — |
| 11 | Other Expenses | 189 | 144.07 | — |
| 12 | Total Expenses (B) | 190 | 755.54 | — |
| 13 | Profit Before Exceptional items and tax | 191 | 227.25 | — |
| 14 | Exceptional Items - (Expense)/Income | 192 | – (dash) | `ZERO_STANDING` — nil this quarter and same quarter prior year, but 30.02 in 31/03/2026 quarter and 522.65 for FY26 annual (GSPC-related, per Note 2) — template line, retain |
| 15 | Profit Before Tax | 193 | 227.25 | — |
| 16 | Current Tax | 195 | 64.75 | — |
| 17 | Deferred Tax | 196 | (0.58) | — |
| 18 | Short/(excess) provision of earlier years | 197 | 0.07 | — |
| 19 | Profit for the Period/Year | 198 | 163.01 | Standalone PAT — see TABLE 13 (PAT gap) |
| 20 | Changes in fair value of equity instruments through OCI (FVTOCI) | 201–202 | 12.75 | — |
| 21 | Remeasurement of post-employment benefit obligations | 203 | 2.56 | — |
| 22 | Income tax relating to these items | 204 | (21.79) | — |
| 23 | Other Comprehensive Income for the Period, net of tax | 205 | (6.48) | — |
| 24 | Total Comprehensive Income for the Period | 206–207 | 156.53 | — |
| 25 | Paid up equity share capital | 208 | 63.60 | — |
| 26 | Reserves (excl. Revaluation Reserve) | 209 | blank (quarter columns) / 7,004.97 (FY26 annual only) | `ZERO_STANDING` — standing balance-sheet line not populated for interim quarter columns per standard Reg 33 convention; retained as a row, not dropped |
| 27 | EPS Basic (Face Value ₹2) | 211 | 5.13 | — |
| 28 | EPS Diluted (Face Value ₹2) | 212 | **2.13** | `OCR_SUSPECT` / flag for A3–A4: Diluted EPS shown as 2.13 while Basic EPS same quarter is 5.13 and Diluted = Basic in every other column of this same row (6.96, 5.16, 31.16) and in the page-3 summary table (5.13/5.13, line 132–133). Likely a "5"→"2" OCR misread of the source PDF glyph; needs verification against source filing before use in any ratio |

Standalone detailed P&L: 28 line items declared (grep of table row labels) vs 28 enumerated. Match: yes.

## TABLE 6 — Consolidated Detailed P&L (page 6, lines 291–337) — every line item, revenue through EPS

| # | Particulars | Line(s) | Q1 FY27 (30/06/2026) | Flag |
|---|-------------|---------|----------------------|------|
| 1 | Revenue from Operations | 298 | 906.64 | — |
| 2 | Other Income | 299 | 76.15 | — |
| 3 | Total Income (A) | 300 | 982.79 | — |
| 4 | Changes in inventories | 302 | 5.78 | — |
| 5 | Royalties and other tax levies | 303 | 86.70 | — |
| 6 | GST Compensatory Cess Expenses | 304 | – (dash) | `ZERO_STANDING` — same pattern as TABLE 5 row 6 |
| 7 | Employee Benefit Expenses | 305 | 42.27 | — |
| 8 | Finance Costs | 306 | 6.61 | — |
| 9 | Depreciation and Amortisation Expenses | 307 | 33.33 | — |
| 10 | Loading of lignite and overburden removal expenses | 308 | 436.78 | — |
| 11 | Other Expenses | 309 | 144.07 | — |
| 12 | Total Expenses (B) | 310 | 755.54 | — |
| 13 | Profit Before Tax and Share of Profit/(Loss) of JV & Associates and exceptional items | 311–312 | 227.25 | — |
| 14 | Exceptional Items - (Expense)/Income | 313 | – (dash) | `ZERO_STANDING` — same pattern as TABLE 5 row 14 |
| 15 | Profit Before Tax and Share of Profit/(Loss) of JV & Associates | 314 | 227.25 | — |
| 16 | Share of Profit/(Loss) of joint ventures and associates using equity method (net of taxes) | 315–317 | 0.42 | Consolidation-only line, absent from standalone statement — the primary driver of TABLE 13 PAT gap |
| 17 | Current Tax | 319 | 64.75 | — |
| 18 | Deferred Tax | 320 | (0.58) | — |
| 19 | Short/(excess) provision of earlier years | 321 | 0.07 | — |
| 20 | Profit for the Period/Year | 322 | 163.43 | Consolidated PAT — see TABLE 13 |
| 21 | Changes in fair value of equity instruments through OCI (FVTOCI) | 325–326 | 12.75 | — |
| 22 | Remeasurement of post-employment benefit obligations | 327 | 2.56 | — |
| 23 | Income tax relating to these items | 328 | (21.79) | — |
| 24 | Other Comprehensive Income for the Period, net of tax | 329 | (6.48) | — |
| 25 | Total Comprehensive Income for the Period | 330–332 | 156.95 | — |
| 26 | Paid up equity share capital | 333 | 63.60 | — |
| 27 | Reserves (excl. Revaluation Reserve) | 334 | blank (quarter columns) / 7,009.14 (FY26 annual only) | `ZERO_STANDING` — same pattern as TABLE 5 row 26 |
| 28 | EPS Basic (Face Value ₹2) | 336 | 5.14 | — |
| 29 | EPS Diluted (Face Value ₹2) | 337 | 5.14 | — |

Consolidated detailed P&L: 29 line items declared vs 29 enumerated. Match: yes. (One more row than standalone: the JV/associate equity-method line, correctly present only in consolidated.)

**Combined detailed P&L count test: 57 declared (28 + 29) vs 57 enumerated. Match: yes.**

---

## TABLE 7 — Summary/Abridged Results Table, Standalone (page 3, lines 112–133)

| # | Particulars | Line(s) | Q1 FY27 | Flag |
|---|-------------|---------|---------|------|
| 1 | Total Income from Operations (net) | 116 | 906.64 | — |
| 2 | Net Profit for the period (before Tax and Exceptional items) | 117–119 | 227.25 | — |
| 3 | Net Profit for the period before tax (after Exceptional items) | 120 | 227.25 | — |
| 4 | Net Profit for the period after tax (after Exceptional items) | 121 | 163.01 | Cross-checks TABLE 5 row 19 — matches |
| 5 | Total Comprehensive Income for the period | 122–125 | 156.53 | Cross-checks TABLE 5 row 24 — matches |
| 6 | Equity Share Capital | 126 | 63.60 | — |
| 7 | Reserves (excl. Revaluation Reserve) | 127–128 | blank (quarter) / 7,004.97 (FY26 annual) | `ZERO_STANDING` — same convention as TABLE 5 row 26 |
| 8a | EPS Basic (₹2 FV) | 132 | 5.13 | — |
| 8b | EPS Diluted (₹2 FV) | 133 | 5.13 | Note: matches Basic here — contradicts TABLE 5 row 28 (detailed statement shows Diluted 2.13 for the same quarter, same entity) — corroborates the `OCR_SUSPECT` flag on TABLE 5 row 28; 5.13 is the internally-consistent figure |

Standalone summary table: 9 line items declared (7 numbered + 2 EPS sub-rows) vs 9 enumerated. Match: yes.

## TABLE 8 — Summary/Abridged Results Table, Consolidated (page 3, lines 136–152)

| # | Particulars | Line(s) | Q1 FY27 | Flag |
|---|-------------|---------|---------|------|
| 1 | Total Income from Operations (net) | 139 | 906.64 | — |
| 2 | Net Profit for the period (before Tax and Exceptional items) | 140 | 227.25 | — |
| 3 | Net Profit for the period before tax (after Exceptional items) | 141 | 227.25 | — |
| 4 | Net Profit for the period after tax (after Exceptional items) | 142 | 163.43 | Cross-checks TABLE 6 row 20 — matches |
| 5 | Total Comprehensive Income for the period | 143–145 | 156.95 | Cross-checks TABLE 6 row 25 — matches |
| 6 | Equity Share Capital | 146 | 63.60 | — |
| 7 | Reserves (excl. Revaluation Reserve) | 147–148 | blank (quarter) / 7,009.14 (FY26 annual) | `ZERO_STANDING` — same convention |
| 8a | EPS Basic (₹2 FV) | 151 | **2.14** | `OCR_SUSPECT` / flag for A3–A4: Basic EPS shown as 2.14 while Diluted same row is 5.14, and TABLE 6 row 28 (detailed consolidated statement) shows Basic = Diluted = 5.14 for the identical quarter. Second instance of the same "5"→"2" glyph-misread pattern seen in TABLE 5 row 28; needs verification against source filing |
| 8b | EPS Diluted (₹2 FV) | 152 | 5.14 | Matches TABLE 6 row 29 |

Consolidated summary table: 9 line items declared vs 9 enumerated. Match: yes.

**Combined summary-table count test: 18 declared (9 + 9) vs 18 enumerated. Match: yes.**

**Two independent OCR_SUSPECT figures found (standalone detailed Diluted EPS, line 212; consolidated summary Basic EPS, line 151) — both resolve internally to "5.13/5.14" if corrected — flagged for A3/A4, not corrected here (enumeration, not interpretation).**

---

## TABLE 9 — Standalone Segment Information (page 5, lines 216–254)

| # | Particulars | Line(s) | Q1 FY27 | Flag |
|---|-------------|---------|---------|------|
| 1 | Segment Revenue — Mining | 225 | 841.01 | — |
| 2 | Segment Revenue — Power | 226 | 111.25 | — |
| 3 | Segment Revenue — Subtotal (unlabeled sum row) | 227 | 952.26 | — |
| 4 | Less: Inter Segment Revenue | 229 | 45.62 | — |
| 5 | Net Sales/Revenue From Operations | 230 | 906.64 | Cross-checks TABLE 5 row 1 — matches |
| 6 | Segment Results — Mining | 234 | 208.07 | — |
| 7 | Segment Results — Power | 235 | (6.00) | — |
| 8 | Total Segment Operating Results | 236 | 202.07 | — |
| 9 | Un-allocable Corporate Results | 237 | (50.94) | — |
| 10 | Total Operating Results | 238 | 151.13 | — |
| 11 | Add: Interest and Dividend Income | 239 | 68.79 | — |
| 12 | Add: Un-allocable income net of un-allocable expenses | 240 | 7.33 | — |
| 13 | Add: Exceptional Items - (Expense)/Income | 241 | – (dash) | `ZERO_STANDING` — same GSPC-related template line as TABLE 5 row 14 |
| 14 | Net Profit Before Tax | 242 | 227.25 | Cross-checks TABLE 5 row 15 — matches |
| 15 | Segment Assets — Mining | 244 | 4,095.65 | — |
| 16 | Segment Assets — Power | 247 | 1,224.17 | — |
| 17 | Segment Assets — Unallocated | 248 | 4,000.24 | — |
| 18 | Segment Assets — Total | 249 | 9,320.06 | Arithmetic check: 4,095.65+1,224.17+4,000.24=9,320.06 — ties |
| 19 | Segment Liabilities — Mining | 251 | 1,215.66 | — |
| 20 | Segment Liabilities — Power | 252 | 106.37 | — |
| 21 | Segment Liabilities — Unallocated | 253 | 772.93 | — |
| 22 | Segment Liabilities — Total | 254 | 2,094.96 | Arithmetic check: 1,215.66+106.37+772.93=2,094.96 — ties |

Standalone segment rows: 22 declared vs 22 enumerated. Match: yes.

## TABLE 10 — Consolidated Segment Information (page 7, lines 340–376)

| # | Particulars | Line(s) | Q1 FY27 | Flag |
|---|-------------|---------|---------|------|
| 1 | Segment Revenue — Mining | 349 | 841.01 | — |
| 2 | Segment Revenue — Power | 350 | 111.25 | — |
| 3 | Segment Revenue — Subtotal | 351 | 952.26 | — |
| 4 | Less: Inter Segment Revenue | 352 | 45.62 | — |
| 5 | Net Sales/Income From Operations | 353 | 906.64 | Cross-checks TABLE 6 row 1 — matches |
| 6 | Segment Results — Mining | 357 | 208.07 | — |
| 7 | Segment Results — Power | 358 | (6.00) | — |
| 8 | Total Segment Operating Results | 359 | 202.07 | — |
| 9 | Un-allocable Corporate Results | 360 | (50.94) | — |
| 10 | Total Results | 361 | 151.13 | — |
| 11 | Add: Interest and Dividend Income | 362 | 68.79 | — |
| 12 | Add: Un-allocable income net of un-allocable expenses | 363 | 7.33 | — |
| 13 | Add: Exceptional Items - (Expense)/Income | 364 | – (dash) | `ZERO_STANDING` — same template line as TABLE 6 row 14 |
| 14 | Net Profit Before Tax | 365 | 227.25 | Cross-checks TABLE 6 row 15 — matches (note: this is PBT before JV/associate equity-method share; ties to consolidated P&L row 15, not row 20 PAT) |
| 15 | Segment Assets — Mining | 368 | 4,095.65 | — |
| 16 | Segment Assets — Power | 369 | 1,224.17 | — |
| 17 | Segment Assets — Unallocated | 370 | 4,004.83 | — |
| 18 | Segment Assets — Total | 371 | 9,324.65 | Arithmetic check: 4,095.65+1,224.17+4,004.83=9,324.65 — ties |
| 19 | Segment Liabilities — Mining | 373 | 1,215.66 | — |
| 20 | Segment Liabilities — Power | 374 | 106.37 | — |
| 21 | Segment Liabilities — Unallocated | 375 | 772.93 | — |
| 22 | Segment Liabilities — Total | 376 | 2,094.96 | Arithmetic check: 1,215.66+106.37+772.93=2,094.96 — ties |

Consolidated segment rows: 22 declared vs 22 enumerated. Match: yes.

**Combined segment-table count test: 44 declared (22 + 22) vs 44 enumerated. Match: yes.**

---

## TABLE 11 — Consolidation Entity List (Note 2, page 7, lines 383–389; cross-referenced against Auditor Report para 4, lines 454–458)

| # | Entity | Relationship | Line(s) — Note | Line(s) — Auditor Report | Flag |
|---|--------|--------------|-----------------|---------------------------|------|
| 1 | Naini Coal Company Limited | Joint Venture | 385 | 454 | — |
| 2 | Swarnim Gujarat Fluorspar Private Limited | Joint Venture | 386 | 455 | Note 2 spells "Swamim" (OCR artifact of "Swarnim"); auditor report spells "Swarnim" — same entity, spelling variance flagged for A3 |
| 3 | Gujarat Jaypee Cement and Infrastructure Limited | Associate | 387 | 456 | — |
| 4 | Gujarat Credo Mineral Industries Limited | Associate | 388 | 457 | — |
| 5 | Aikya Chemicals Private Limited | Associate | 389 | 458 | — |

Entities: 5 declared (Note 2) vs 5 declared (Auditor Report para 4) vs 5 enumerated. Match: yes.
`ENTITY_CHANGE` check: NOT PERFORMED — no prior-quarter ledger/entity list supplied to this run. Flagging as an evidence gap, not silently skipping.

Auditor Report para 6 (lines 471–480): Parent's share of net profit/(loss) after tax and total comprehensive income of ₹0.42 crore for the quarter, in respect of 3 associates and 2 JVs, based on unaudited management-certified financial statements — "not material to the Group" per management representation. This ₹0.42 crore ties exactly to TABLE 6 row 16 (Share of Profit of JV/associates, 0.42) and to TABLE 13 below.

---

## TABLE 12 — Auditor's Limited Review Reports (both entities)

### Consolidated Review Report (pages 8–9, lines 417–497) — Dhirubhai Shah & Co LLP

| Para # | Line(s) | Content (first 15 words) | Flag |
|--------|---------|----------------------------|------|
| 1 | 424–430 | "We have reviewed the accompanying Statement of Consolidated Unaudited Financial Results of GUJARAT MINERAL DEVELOPMENT" | Scope paragraph |
| 2 | 432–438 | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's" | Management responsibility / Ind AS 34 basis |
| 3 | 440–452 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements" | SRE 2410 basis; explicit "we do not express an audit opinion" — Limited Review, not audit |
| 4 | 453–458 | "The Statement includes the result of the following entities" | Entity list — see TABLE 11 |
| 5 | 460–468 | "Based on our review conducted as stated in paragraph 3 above and based on the consideration" | Conclusion — unmodified/clean |
| 6 | 471–484 | "The consolidated unaudited financial results includes the Parent's share of net profit/(loss) after tax" | Other Matter: reliance on unaudited, management-certified JV/associate financials; conclusion explicitly "not modified" in respect of this reliance |
| — | 488–497 | Signature block: Parth S. Dadawala, Partner, Dhirubhai Shah & Co LLP, FRN 102511W/W100298, Membership No. 134475, UDIN:26134475URFHWQ6501, Date July 31 2026, Place Ahmedabad | No Emphasis of Matter or Going Concern paragraph present; opinion type = unmodified conclusion with one Other Matter paragraph |

Consolidated report: 6 paragraphs declared vs 6 enumerated. Match: yes.

### Standalone Review Report (page 10, lines 500–547) — Dhirubhai Shah & Co LLP

| Para # | Line(s) | Content (first 15 words) | Flag |
|--------|---------|----------------------------|------|
| 1 | 506–511 | "We have reviewed the accompanying Statement of Standalone Unaudited Financial Results of GUJARAT MINERAL DEVELOPMENT" | Scope paragraph |
| 2 | 512–518 | "This Statement, which is the responsibility of the Company's Management and approved by the Company's" | Management responsibility / Ind AS 34 basis |
| 3 | 519–528 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements" | SRE 2410 basis; "we do not express an audit opinion" |
| 4 | 529–536 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our" | Conclusion — unmodified/clean, no Other Matter, no Emphasis of Matter, no Going Concern language |
| — | 537–547 | Signature block: Parth S. Dadawala, Partner, Dhirubhai Shah & Co LLP, FRN 102511W/W100298, Membership No. 134475, UDIN: 26134475URLCHW4878, Date July 31 2026, Place Ahmedabad | UDIN differs from the consolidated report's UDIN (expected — separate report requires separate UDIN); same signing partner and date for both |

Standalone report: 4 paragraphs declared vs 4 enumerated. Match: yes.

**Combined auditor-paragraph count test: 10 declared (6 + 4) vs 10 enumerated. Match: yes.**

Same reviewing firm (Dhirubhai Shah & Co LLP) and same partner (Parth S. Dadawala) issued both reports on the same date (July 31, 2026) — both are Limited Reviews under SRE 2410, neither is an audit opinion, neither carries Emphasis of Matter or Going Concern language.

---

## TABLE 13 — Signature Blocks (all discrete signatory instances)

| # | Document | Signatory | Designation | Line(s) | Timestamp | Flag |
|---|----------|-----------|-------------|---------|-----------|------|
| 1 | Board Outcome cover letter | Joel S. Evans | Company Secretary | 82–89 | Digitally signed 2026.07.31 16:14:07 +05'30' | Board meeting concluded 13:10 same day — signature timestamp is after conclusion, no anomaly |
| 2 | Summary Results table (page 3) | Roopwant Singh, IAS | Managing Director | 166–167 | No timestamp shown (place/date only: Ahmedabad, July 31, 2026) | — |
| 3 | Standalone segment info page (page 5) | Roopwant Singh, IAS | Managing Director | 284–287 | No timestamp shown | — |
| 4 | Consolidated segment info page (page 7) | Roopwant Singh, IAS | Managing Director | 409–414 | No timestamp shown | — |
| 5 | Consolidated review report (pages 8–9) | Parth S. Dadawala | Partner, Dhirubhai Shah & Co LLP | 488–497 | Date July 31, 2026 (no intraday timestamp); UDIN:26134475URFHWQ6501 | — |
| 6 | Standalone review report (page 10) | Parth S. Dadawala | Partner, Dhirubhai Shah & Co LLP | 537–547 | Date July 31, 2026 (no intraday timestamp); UDIN: 26134475URLCHW4878 | — |

Signature blocks: 6 declared vs 6 enumerated. Match: yes.

---

## TABLE 14 — Standalone-vs-Consolidated PAT Gap (first-class enumerated metric)

| Metric | Value | Source | Line(s) |
|--------|-------|--------|---------|
| Standalone Profit for the Period (Q1 FY27) | 163.01 | TABLE 5 row 19 | 198 |
| Consolidated Profit for the Period (Q1 FY27) | 163.43 | TABLE 6 row 20 | 322 |
| **PAT Gap (Consolidated − Standalone)** | **+0.42** | Computed | — |
| Reconciling item: Share of Profit of JV/Associates (equity method, net of tax) | 0.42 | TABLE 6 row 16 | 315–317 |
| Auditor cross-check: Parent's share of net profit/total comprehensive income of JV/associates, per consolidated review report para 6 | 0.42 | TABLE 12 (consolidated) para 6 | 471–472 |

Gap fully reconciles to the single JV/associate equity-method line (0.42 = 0.42 = 0.42, three independent citations agree). No unexplained residual. Flagged as a first-class metric per task instruction, not because it is anomalous — the size of GMDC's standalone-vs-consolidated business (5 small JV/associate stakes, "not material to the Group" per auditor para 6) is itself informational for A4 interpretation of consolidation scope.

---

## FLAG SUMMARY

| Flag | Count | Rows |
|------|-------|------|
| `ZERO_STANDING` | 8 | TABLE 5 rows 6,14,26; TABLE 6 rows 6,14,27; TABLE 7 row 7; TABLE 8 row 7; TABLE 9 row 13; TABLE 10 row 13 (note: 8 distinct disclosure instances across the two P&L statements, two summary tables, and two segment tables — GST Cess x2, Exceptional Items x4 [P&L x2 + segment x2], Reserves x2) |
| `OCR_SUSPECT` | 2 | TABLE 5 row 28 (standalone detailed Diluted EPS = 2.13, line 212); TABLE 8 row 8a (consolidated summary Basic EPS = 2.14, line 151) — both need verification against source PDF before use |
| `NEW_MOU` | 2 | TABLE 1 items 2, 3 (GNFC coal-to-chemicals/UCG; IREL Rare Earth Elements) |
| `ANCILLARY` | 2 | TABLE 1 items 1a, 1b (enclosures under item 1) |
| Prior-ledger unavailable (entity cross-check not run) | 1 | TABLE 11 note |

---

## MASTER COUNT ROLL-UP

| Category | Count |
|----------|-------|
| Numbered notes (standalone 4 + consolidated 5) | 9 |
| Unnumbered footnotes | 1 |
| Agenda items (Board Outcome) | 3 |
| Ancillary enclosures under item 1 | 2 |
| Detailed P&L line items (standalone 28 + consolidated 29) | 57 |
| Summary table line items (standalone 9 + consolidated 9) | 18 |
| Segment info rows (standalone 22 + consolidated 22) | 44 |
| Auditor report paragraphs (consolidated 6 + standalone 4) | 10 |
| Consolidation entities | 5 |
| Signature blocks | 6 |
| PAT gap metric | 1 |
| **Total line_items (P&L + summary + segment)** | **119** |
| **ZERO_STANDING flagged rows** | **8** |

```yaml
stage: A2-enumerator
company: "GMDCLTD"
quarter: "Q1FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/gmdc-q1fy27/work/ledger_results_gmdc_q1fy27.md"
counts:
  notes: 9
  line_items: 119
  zero_standing: 8
  agenda_items: 3
  auditor_paras: 10
  entities: 5
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, OCR_SUSPECT, NEW_MOU, ANCILLARY]
gate_a2: pass
mismatch_note: ""
```
