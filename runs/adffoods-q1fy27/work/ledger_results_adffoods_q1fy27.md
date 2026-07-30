# A2 ENUMERATION LEDGER — ADF Foods Limited (ADFFOODS) — Q1 FY27 — Results doctype

Source: `extract_results_adffoods_q1fy27.txt` (Reg 30 & 33 Board Outcome + Unaudited Standalone and
Consolidated Financial Results Q1 FY27 + Limited Review Report, MSKA & Associates LLP). Units: Lakhs
(x0.01 = Rs Crores). 8 pages, 558 extracted lines. Prior-quarter ledger: not provided — no diff
performed; `ENTITY_CHANGE` / `DROPPED_SLIDE`-style comparisons could not be run this cycle
(flag `NO_PRIOR_LEDGER`).

Methodology note on line-item reconciliation: the main results statement (page 6) and the note-4
FX sub-table are OCR-garbled with numeric values wrapping across physical text lines out of
alignment with their row labels. A naive numeric-pattern grep over-/under-counts rows because of
this wrapping. The grep pass for `line_items` therefore greps for each row's distinct label string
(built from a first manual read of the raw text) and confirms each occurs the expected number of
times in the table's line range; the manual sweep independently re-walks the table top to bottom.
Both methods converge on the same row set — see COUNT TEST.

```
=== A2 COUNT TEST ===
category: notes           grep_count: 8    sweep_count: 8    match: yes
category: line_items      grep_count: 76   sweep_count: 76   match: yes
category: agenda_items    grep_count: 1    sweep_count: 1    match: yes
category: auditor_paras   grep_count: 12   sweep_count: 12   match: yes
category: entities        grep_count: 8    sweep_count: 8    match: yes
category: signature_blocks grep_count: 5   sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

---

## 1. Board Outcome Letter (page 1, lines 15-71)

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Subject / Reg 30 & 33 disclosure | 31, 35-39 | "Outcome of the Board Meeting held today i.e. on Wednesday, 29th July, 2026" — Board approved Unaudited Standalone and Consolidated Financial Results for Q1 FY27 (quarter ended 30 June 2026) | — |
| 2 | "inter alia" phrasing | 37-38 | Letter states Board "has inter alia approved" the results, implying other business may have been transacted at the same meeting but is not itemised in this letter | INTER_ALIA_UNDISCLOSED |
| 3 | Enclosures | 41-45 | Unaudited Standalone and Consolidated Financial Results + Limited Review Report by M/s. MSKA & Associates LLP (FRN 105047W) | — |
| 4 | Board Meeting timing | 47 | Commenced 05.00 p.m., concluded 07.15 p.m. — duration 2h15m | — |
| 5 | Signatory | 53-61 | Shalaka Ovalekar, Company Secretary, "For ADF Foods Limited" | see Signature Blocks §7 |
| 6 | Registered / Corporate office footer block | 68-71 | CIN L15400GJ1990PLC014265, Nadiad regd office, Mumbai corp office, contact details | — |

Agenda items count (substantive, voted/approved matters explicitly named): **1** (results approval).
No AR approval, AGM notice, record date, dividend, director appointment/resignation, auditor
change, scrutinizer appointment, ESOP grant, or capital-raising enabling resolution appears in this
letter.

---

## 2. Auditor Review Report — Standalone (page 2, lines 84-138)

| Para | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 90-94 | "We have reviewed the accompanying statement of standalone unaudited financial results of ADF Foods..." (scope) | — |
| 2 | 96-102 | "This Statement, which is the responsibility of the Company's Management and has been approved..." (Ind AS 34 basis, management responsibility) | — |
| 3 | 104-112 | "We conducted our review... in accordance with... SRE 2410... does not enable us to obtain assurance... Accordingly, we do not express an audit opinion" (review scope, no audit opinion) | — |
| 4 | 114-119 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." (unmodified/clean conclusion) | — |
| — | 121-134 | Firm signature block: For M S K A & Associates LLP, FRN 105047W/W101187 | see Signature Blocks §7 |

Opinion type: unmodified review conclusion (no Emphasis of Matter, no Other Matters, no Going
Concern paragraph in the Standalone report).

## 3. Auditor Review Report — Consolidated (pages 3-5, lines 140-306)

| Para | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 157-162 | "We have reviewed the accompanying Statement of consolidated unaudited financial results of ADF Foods..., its subsidiaries..." (scope, Group defined) | — |
| 2 | 164-170 | "This Statement, which is the responsibility of the Holding Company's Management and approved..." (Ind AS 34 basis) | — |
| 3 | 172-183 | "We conducted our review... SRE 2410... Accordingly, we do not express an audit opinion" + SEBI Reg 33(8) circular procedures performed | — |
| 4 | 185-201 | "This Statement includes the results of the Holding Company and the following entities:" — 7-entity consolidation table | see Entities §4 |
| 5 | 217-223 | "Based on our review conducted and procedures performed... nothing has come to our attention..." (unmodified conclusion, relies on other auditors per para 6) | — |
| 6 | 225-247 | "We did not review the interim financial information of three subsidiaries included in the Statement, whose interim financial information reflects total revenues of Rs. 8,440.93 lakhs..." (reliance on other auditors — Other Matters-type paragraph) | AUDITOR_RELIANCE (3 unnamed subsidiaries, foreign, revenue Rs 8,440.93L, net PAT Rs 77.20L, TCI Rs 77.20L for the quarter) |
| 7 | 264-275 | "The Statement includes the interim financial information of three subsidiaries which have not been reviewed by their auditors, whose interim financial information reflects total revenue of Rs. 177.02 lakhs..." (unreviewed, management-furnished — Other Matters-type paragraph) | UNAUDITED_MGMT_FURNISHED (3 unnamed subsidiaries, revenue Rs 177.02L, net loss Rs (115.82)L, TCI loss Rs (115.15)L; management represents not material to Group) |
| 8 | 277-282 | "The Statement does not include the interim financial information of one of its subsidiary Company 'Power Brands (Foods) Private Limited' incorporated in India which is under voluntary liquidation" (exclusion — Other Matters-type paragraph) | EXCLUDED_ENTITY — see Entities §4 |
| — | 284-298 | Firm signature block: For M S K A & Associates LLP, FRN 105047W/W101187 | see Signature Blocks §7 |

Opinion type: unmodified review conclusion, with three Other-Matters-type paragraphs (6, 7, 8)
addressing reliance on other auditors, unaudited/management-furnished subsidiaries, and one
excluded subsidiary. No Emphasis of Matter, no Going Concern paragraph.

Standalone + Consolidated auditor paragraphs total: 4 + 8 = **12**.

---

## 4. Consolidation Entity List (page 3, lines 185-201) + entity referenced in exclusion (page 5, line 277-278)

| Sr. | Entity | Line | Relationship | Audit status (cross-ref para 6/7) | Flags |
|-----|--------|------|--------------|-------------------------------------|-------|
| 1 | Telluric Foods (India) Limited | 189 | Wholly owned subsidiary | Not individually named as unreviewed/unaudited-mgmt-furnished in report text | — |
| 2 | ADF Foods UK Limited | 191 | Wholly owned subsidiary | Not individually named | — |
| 3 | ADF Foods Australia Pty Limited | 193 | Wholly owned subsidiary | Not individually named | — |
| 4 | Telluric Foods Limited | 195 | Wholly owned stepdown subsidiary | Not individually named | — |
| 5 | ADF Holdings (USA) Ltd. | 197 | Wholly owned stepdown subsidiary | Not individually named | — |
| 6 | ADF Foods (USA) Ltd. | 199 | Wholly owned stepdown subsidiary | Not individually named | — |
| 7 | Vibrant Foods New Jersey LLC | 201 | Wholly owned stepdown subsidiary | Not individually named | — |
| 8 | Power Brands (Foods) Private Limited | 277-278 | Subsidiary incorporated in India, under voluntary liquidation | Excluded from Consolidated Statement entirely (not material per Management) | EXCLUDED_ENTITY |

Note: para 6 (line 225-232) refers to "three subsidiaries" reviewed by other auditors (foreign,
revenue Rs 8,440.93L) and para 7 (line 264-270) refers to a different set of "three subsidiaries"
whose information is unreviewed/management-furnished (revenue Rs 177.02L) — the report does not
name which of the 7 table entities fall in each bucket. This mapping gap is flagged for A3/A4.

Entities count: 7 (consolidation table) + 1 (named excluded entity) = **8**.
No prior-quarter entity list supplied — `NO_PRIOR_LEDGER`, `ENTITY_CHANGE` comparison not run.

---

## 5. Notes to the Financial Results (page 7, lines 455-489)

| Note | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 456-458 | "The above Unaudited financial results published in accordance with Regulation 33 of the SEBI..." (basis of preparation, Audit Committee review, Board approval date, limited review) | — |
| 2 | 460-461 | "The figures for the quarters ended March 31 as reported in this results are the balancing figures..." (Q4 = derived balancing figure, standard boilerplate) | — |
| 3 | 463-465 | "The Consolidated financial results has been prepared in accordance with Indian Accounting Standards Ind AS-110..." (consolidation basis, subsidiary list restated in prose) | — |
| 4 | 467-472 | "Other income and other expenses above includes net foreign exchange gain and loss respectively for each reporting period as under" — embedded FX sub-table | see §6 |
| 5 | 474-476 | "Effective 21st November, 2025, The Government of India has consolidated multiple existing labour legislations into a unified framework... 'New Labour Codes'..." (incremental gratuity/leave liability Rs 6.83 Cr recognized as at 31 Dec 2025, presented as Exceptional Item) | — |
| 6 | 478-483 | "During the quarter ended June 30, 2026, the Company's wholly owned subsidiary received a refund of USD 2.08 million (INR 19.69 crores) from the United States Government in respect of import tariffs..." (US tariff refund: USD 0.33mn/INR 3.12Cr to inventory carrying value, USD 0.77mn/INR 7.29Cr to reduction of COGS, USD 0.98mn/INR 9.28Cr held for customer commercial-arrangement evaluation; ongoing tariff monitoring language) | — |
| 7 | 486-487 | "The Entity's Chief Operating Decision Maker (CODM) has identified two business segments 'Processed and Preserved Foods Business' and 'Distribution Business'..." (segment identification, cross-ref to segment annexure page 8) | — |
| 8 | 489 | "The above unaudited financial results of the Company are available on the Company's (www.adf.foods.com) and stock exchanges websites..." (website availability boilerplate) | — |

Notes count: **8**. Unnumbered footnote also present: "(Quarterly EPS not annualised)" parenthetical
under the EPS caption (line 425) — recorded under §6 row 43 below, not a standalone numbered note.
Superscript "1"-like OCR artifacts after period-column headers at line 320 could not be resolved
to a genuine footnote marker versus an OCR misread of a table border character — flag `OCR_AMBIGUOUS`.

---

## 6. Statement of Unaudited Financial Results — Standalone + Consolidated (page 6, lines 315-448)

One row per Particulars label; each row carries 8 data columns (Standalone: Q1FY27 unaudited /
Q4FY26 audited / Q1FY26 unaudited / FY26 audited; Consolidated: same four periods). Values not
transcribed here (A2 enumerates disclosure units, not the raw figures) except where needed to
identify a `ZERO_STANDING` cell pattern.

| # | Particulars | Line(s) | Flags |
|---|-------------|---------|-------|
| 1 | Revenue from Operations (section header, item 1) | 322 | — |
| 2 | Income from operations | 323 | — |
| 3 | Other income | 324 | — |
| 4 | Total Income | 325 | — |
| 5 | Cost of material consumed | 327 | — |
| 6 | Purchases of Stock-in-trade | 328 | — |
| 7 | Changes in inventories of finished goods, Stock-in-Trade and work-in-progress | 329-330 | — |
| 8 | Employee benefits expense | 332 | — |
| 9 | Finance costs | 334 | — |
| 10 | Depreciation, amortization and impairment expenses | 335 | — |
| 11 | Other expenses | 336 | — |
| 12 | Total Expenses (item 2) | 337 | — |
| 13 | Profit before exceptional items and tax (1-2) (item 3) | 338 | — |
| 14 | Exceptional Items (Refer note 5) (item 4) | 339 | ZERO_STANDING — blank in all four Quarter-ended columns (Standalone Jun26, Standalone Jun25, Consol Jun26, Consol Jun25); populated only in the two Year-ended-Mar26 columns (683.00), per Note 5 (Labour Code gratuity/leave liability, non-recurring) |
| 15 | Profit before tax (item 5) | 340 | — |
| 16 | Tax Expense (section header, item 6) | 341 | — |
| 17 | a) Current tax | 342 | — |
| 18 | b) Deferred tax | 345-358 (OCR-wrapped across several physical lines; values interleaved with row 19) | — |
| 19 | c) Adjustment of tax relating to earlier periods | 346-354 (OCR-wrapped, interleaved with row 18) | — |
| 20 | Total tax expense | 359-361 | — |
| 21 | Profit after tax (item 7) | 363-365 | — |
| 22 | Other comprehensive income (section header, item 8) | 366 | — |
| 23 | a) Items that will not be reclassified to profit or loss (sub-header) | 368-370 | — |
| 24 | i) Remeasurements of the defined benefit plan | 377 | — |
| 25 | ii) Income tax relating to items that will not be reclassified to profit or loss | 379-380 | — |
| 26 | b) Items that will be reclassified to profit or loss (sub-header) | 383 | — |
| 27 | i) Exchange differences on translating the financial statements of subsidiaries | 384-394 | ZERO_STANDING (partial) — blank in all four Standalone columns (no subsidiaries to translate at Standalone level); populated in all four Consolidated columns |
| 28 | ii) Net gain/(loss) on cash flow hedges | 396 | — |
| 29 | iii) Income tax relating to items that will be reclassified to profit or loss | 398-399 | — |
| 30 | Other comprehensive income (subtotal) | 401 | — |
| 31 | Total comprehensive income for the period/year (item 9) | 402 | — |
| 32 | Net Profit attributable to: (section header, item 10) | 404 | — |
| 33 | a) Owners of the Company | 405-408 | — |
| 34 | b) Non-controlling interests | 409 | ZERO_STANDING — blank across all 8 columns (Standalone + Consolidated, all four periods each); company's subsidiaries are all wholly owned, no NCI exists, but the line item is retained in the template |
| 35 | Other comprehensive income attributable to: (section header, item 11) | 410 | — |
| 36 | a) Owners of the Company | 411 | — |
| 37 | b) Non-controlling interests | 412 | ZERO_STANDING — blank across all 8 columns |
| 38 | Total comprehensive income attributable to: (section header, item 12) | 413 | — |
| 39 | a) Owners of the Company | 414 | — |
| 40 | b) Non-controlling interests | 415 | ZERO_STANDING — blank across all 8 columns |
| 41 | Paid-up Equity Share Capital (Face value Rs. 2/- each) (item 13) | 416-418 | — |
| 42 | Other Equity (item 14) | 421 | ZERO_STANDING (partial/structural) — blank in all four Quarter-ended columns (Standalone Jun26/Jun25, Consol Jun26/Jun25); populated only in the two Year-ended-Mar26 columns (57,236.78 Standalone / 54,957.74 Consolidated). This is standard SEBI quarterly-format practice (Other Equity disclosed at year-end only) rather than a transaction signal, but is enumerated per the never-drop-a-nil-row rule |
| 43 | Earnings per equity share (EPS) (of Rs. 2/- each) (Quarterly EPS not annualised) (section header, item 15) | 423-425 | — |
| 44 | (1) Basic (Rs.) | 430 | — |
| 45 | (2) Diluted (Rs.) | 431-432 | — |

Main statement line items: **45**.

---

## 7. Note 4 — Net Foreign Exchange Gain/(Loss) Sub-table (page 7, lines 467-472)

| # | Particulars | Line(s) | Detail | Flags |
|---|-------------|---------|--------|-------|
| 1 | Net exchange gain/(Loss), reflected within Other income/(Expenses) | 471-472 | Standalone: (87.84) Q1FY27, 796.90 Q4FY26, 114.18 Q1FY26, 1,425.41 FY26; Consolidated: (85.05) Q1FY27, 800.56 Q4FY26, 108.68 Q1FY26, 1,429.59 FY26 | — |

Note 4 sub-table line items: **1**.

---

## 8. Segment-wise Revenue, Results, Assets and Liabilities — Consolidated (page 8, lines 507-545)

| # | Particulars | Line | Flags |
|---|-------------|------|-------|
| 1 | Segment Revenue (Sales and Other operating income) (section header) | 512 | — |
| 2 | Distribution business (revenue) | 513 | — |
| 3 | Processed and preserved foods (revenue) | 514 | — |
| 4 | Unallocated other operating revenue | 515 | ZERO_STANDING — dash across all four periods |
| 5 | Total | 516 | — |
| 6 | Less: Intersegment Revenue | 517 | ZERO_STANDING — dash across all four periods |
| 7 | Total Segment Revenue | 518 | — |
| 8 | Segment Results (section header) | 519 | — |
| 9 | Distribution business (results) | 520 | — |
| 10 | Processed and preserved foods (results) | 521 | — |
| 11 | Total Segment Results | 522 | — |
| 12 | Add/(Less): Exceptional items | 524 | ZERO_STANDING — dash in both Quarter-ended columns; populated only in Year-ended-Mar26 column, (683.00), consistent with §6 row 14 |
| 13 | Less: Finance cost | 525 | — |
| 14 | Add/(Less): Finance income and other unallocable income (net) of unallocable expenditure | 526-527 | — |
| 15 | Total Profit Before Tax | 528 | — |
| 16 | Segment Assets (section header) | 530 | — |
| 17 | Distribution business (assets) | 532 | — |
| 18 | Processed and preserved foods (assets) | 533 | — |
| 19 | Unallocated Corporate Assets | 534 | — |
| 20 | Total Segment Assets | 535 | — |
| 21 | Segment Liabilities (section header) | 536 | — |
| 22 | Distribution business (liabilities) | 537 | — |
| 23 | Processed and preserved foods (liabilities) | 538 | — |
| 24 | Unallocated Corporate Liabilities | 539 | — |
| 25 | Total Segment Liabilities | 540 | — |
| 26 | Capital employed (Assets - Liabilities) (section header) | 541 | — |
| 27 | Distribution business (capital employed) | 542 | — |
| 28 | Processed and preserved foods (capital employed) | 543 | — |
| 29 | Unallocated (capital employed) | 544 | — |
| 30 | Total Capital employed | 545 | — |

Segment table line items: **30**.

Grand total line_items across §6 + §7 + §8: 45 + 1 + 30 = **76**.
Grand total ZERO_STANDING flags: §6 rows 14, 27(partial), 34, 37, 40, 42(partial) = 6; §8 rows 4, 6, 12 = 3.
**Total ZERO_STANDING = 9.**

---

## 9. Digital Signature Blocks

| # | Signatory | Designation | Document | Line(s) | Timestamp | Flags |
|---|-----------|-------------|----------|---------|-----------|-------|
| 1 | Shalaka Swapnil Ovalekar | Company Secretary | Board Outcome letter | 53-61 | 2026.07.29 20:14:52 +05'30' | Signed 2h59m after meeting concluded (07.15 p.m.) — no anomaly |
| 2 | Amrish Anup Vaidya | Partner, M S K A & Associates LLP (FRN 105047W/W101187, Membership No. 101739) | Standalone Auditor's Review Report | 121-134 | 2026.07.29 19:23:41 +05'30' | UDIN 26101739TUWERW5820. Signed 8m41s after meeting concluded (07.15 p.m.) — no anomaly |
| 3 | Amrish Anup Vaidya | Partner, M S K A & Associates LLP (FRN 105047W/W101187, Membership No. 101739) | Consolidated Auditor's Review Report | 284-298 | 2026.07.29 19:44:10 +05'30' | UDIN 26101739LNNQCA9041. Signed 29m10s after meeting concluded — no anomaly |
| 4 | [Name not shown; designation only] | Chairman, Managing Director & C.E.O. (DIN: 00087404) | Financial Results statement | 494-501 | Not a digital-certificate timestamp; "Place: Mumbai, Date: July 29, 2026" only | Image/wet signature style, no digital-signature timestamp captured in extract |
| 5 | [Name not shown; designation only] | Chairman, Managing Director & C.E.O. (DIN: 00087404) | Segment-wise statement | 548-558 | Not a digital-certificate timestamp; "Place: Mumbai, Date: July 29, 2026" only | Image/wet signature style, no digital-signature timestamp captured in extract |

Signature blocks: **5**. No signature timestamp precedes the board meeting's stated conclusion time
(07.15 p.m.) — checked and cleared, not a flag.

---

## FLAG SUMMARY

- `ZERO_STANDING` x9 (§6 rows 14, 27, 34, 37, 40, 42; §8 rows 4, 6, 12)
- `AUDITOR_RELIANCE` x1 (§3 para 6 — reliance on other auditors for 3 unnamed foreign subsidiaries)
- `UNAUDITED_MGMT_FURNISHED` x1 (§3 para 7 — 3 unnamed subsidiaries, unreviewed, management-furnished)
- `EXCLUDED_ENTITY` x1 (§3 para 8 / §4 row 8 — Power Brands (Foods) Private Limited, under voluntary liquidation, excluded from consolidation)
- `INTER_ALIA_UNDISCLOSED` x1 (§1 row 2 — Board Outcome letter uses "inter alia approved," implying undisclosed additional business)
- `OCR_AMBIGUOUS` x1 (§5 — unresolved superscript-like "1" characters near period-column headers, line 320)
- `NO_PRIOR_LEDGER` x1 (no prior-quarter ledger supplied; entity-list and slide-drop diffs not run)

No `ENTITY_CHANGE`, `DROPPED_SLIDE`, `MGMT_ABSENCE`, or `REPEAT_QUESTION` flags apply — this doctype
has no concall/presentation content and no prior-quarter baseline was supplied for comparison.
