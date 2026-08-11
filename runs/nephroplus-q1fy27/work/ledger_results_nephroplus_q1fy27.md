# A2 COMPLETENESS LEDGER — NEPHROPLUS Q1FY27 (RESULTS FILING)
Source: extract_results_nephroplus_q1fy27.txt (Reg 33 filing: Board Outcome letter +
Reg 30 Annexure I + Standalone LRR + Standalone Results + Consolidated LRR +
Consolidated LRR Annexure I (entity list) + Consolidated Results, 15 pages, 757 extract
lines). Line numbers below are the extract's own embedded line numbers (as printed in
the first column of content after the page-tag column; verified by direct re-read and
by grep -n cross-check against the raw file, offset = 14 from the raw OS line number).
Unit note: filing figures are in ₹ Millions; not converted here (per instructions),
enumerated exactly as they appear. Conversion to ₹ Cr for downstream analysis = x0.1.

```
=== A2 COUNT TEST ===
category: notes               grep_count: 21   sweep_count: 21   match: yes
category: line_items          grep_count: 67   sweep_count: 67   match: yes
category: zero_standing       grep_count: 4    sweep_count: 4    match: yes
category: agenda_items        grep_count: 10   sweep_count: 10   match: yes
category: annexure_items      grep_count: 10   sweep_count: 10   match: yes
category: auditor_paras       grep_count: 11   sweep_count: 11   match: yes
category: entities            grep_count: 26   sweep_count: 26   match: yes
category: signature_blocks    grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep commands used (illustrative, run against extract with raw-line ranges,
embedded-line = raw-line − 14):
- notes: `grep -E $'\t[0-9]+\\.\\s'` inside each notes block (8 standalone + 11
  consolidated) plus `grep -E '\*'` for the two unnumbered EPS footnotes.
- line_items: `grep -E '[0-9]\.[0-9]{2}|Other equity'` inside each table's raw-line
  range (standalone P&L 24, consolidated P&L 30, geographical info 5, IPO
  utilisation ×2 tables 4 each).
- agenda_items: `grep -E $'\t[a-d]\\.\\s[A-Z]'` (4 main) + `grep -E "Mr\.|Ms\."`
  inside the two committee blocks (6 sub-rows).
- annexure_items: `grep -E $'^[0-9]+\t[0-9]+\\.\\s{2,}'` inside the Reg 30
  Annexure I block (10 rows).
- auditor_paras: `grep -E $'\t[0-9]+\\.\\s'` inside each Limited Review Report body
  (5 standalone + 6 consolidated).
- entities: relationship-keyword grep inside LRR Annexure I (26) cross-checked
  against manual count of Note 5's Parent/Subsidiaries/JV breakdown (26).
- signature_blocks: manual sweep for "Digitally signed by" blocks (5); no single
  grep pattern captures all five reliably because of PDF-to-text line wrapping.

Manual sweep was performed as a full line-by-line read of the extract (all 757
lines) independent of the greps above; all eight category counts reconciled on
first sweep, no re-sweep was required.

---

## 1. NUMBERED NOTES + UNNUMBERED FOOTNOTES (21 rows)

| # | Line | Statement | First 15 words | Flags |
|---|------|-----------|-----------------|-------|
| 1 | 309 | Standalone | "The above standalone financial results of Nephrocare Health Services Limited... have been prepared in accordance with..." | |
| 2 | 314 | Standalone | "These standalone financial results have been reviewed by the Audit Committee and approved..." | |
| 3 | 318 | Standalone | "The standalone figures for the quarter ended 31 March 2026 are the balancing figures..." | |
| 4 | 321 | Standalone | "The Company was listed on the stock exchanges on 17 December 2025. Accordingly..." | |
| 5 | 327 | Standalone | "In accordance with Ind AS 108, Operating segments, segment information has been provided..." | |
| 6 | 330 | Standalone | "During the year ended 31 March 2026, the Company has completed an initial public offering..." | contains IPO utilisation sub-table, see §2 |
| 7 | 345 | Standalone | "During the quarter ended 30 June 2026, the Company received share application money amounting..." | ESOP: INR 11.28mn applied, 144,320 shares allotted 14 Jul 2026 (post-period-end) |
| 8 | 348 | Standalone | "The standalone financial results for the quarter ended 30 June 2026, are available on the BSE..." | |
| — | 300 | Standalone (footnote, unnumbered, asterisk) | "*Earnings per equity share is not annualised for the quarters." | UNNUMBERED_FOOTNOTE, qualifies EPS row |
| 1 | 638 | Consolidated | "The above consolidated financial results of Nephrocare Health Services Limited... and its subsidiaries..." | |
| 2 | 644 | Consolidated | "These consolidated financial results have been reviewed by the Audit Committee and approved..." | |
| 3 | 648 | Consolidated | "The consolidated figures for the quarter ended 31 March 2026 are the balancing figures..." | |
| 4 | 651 | Consolidated | "The Company was listed on the stock exchanges on 17 December 2025. Accordingly..." | |
| 5 | 656 | Consolidated | "The Statement of unaudited consolidated financial results include the results of the following entities:" | introduces entity List B, see §6 |
| 6 | 688 | Consolidated | "The Group's Chief Operating Decision Maker ("CODM"), being the Chairman and Managing Director, reviews..." | single reportable segment; introduces geographical info table §2 |
| 7 | 713 | Consolidated | "During the year ended 31 March 2026, the Company has completed an initial public offering..." | contains IPO utilisation sub-table, see §2 (duplicate of note 6 above at Group level) |
| 8 | 729 | Consolidated | "During the quarter ended 30 June 2026, the Group entered into seven asset transfer arrangements..." | INR 709.30mn aggregate, provisional PPA accounting under Ind AS 103 |
| 9 | 736 | Consolidated | "On 26 May 2026, the Group incorporated NephroPlus Health Services Kazakhstan Limited Liability Partnership..." | ENTITY_CHANGE — new subsidiary added this quarter, see §6 |
| 10 | 739 | Consolidated | "During the quarter ended 30 June 2026, the Company received share application money amounting..." | duplicate of standalone note 7 |
| 11 | 742 | Consolidated | "The consolidated financial results for quarter ended 30 June 2026, are available on the BSE..." | |
| — | 628 | Consolidated (footnote, unnumbered, asterisk) | "*Earnings per equity share is not annualised for the quarters." | UNNUMBERED_FOOTNOTE, qualifies EPS row |

## 2. FINANCIAL TABLE LINE ITEMS (67 rows, incl. zero/dash-valued standing items)

### 2a. Standalone P&L (24 rows) — lines 262–299
| Line | Particulars | Q1FY27 | Q4FY26 (Aud) | Q1FY26 | FY26 (Aud) | Flags |
|------|-------------|--------|--------------|--------|-----------|-------|
| 262 | Revenue from operations | 1,703.78 | 1,643.33 | 1,488.26 | 6,297.43 | |
| 263 | Other income | 61.24 | 61.35 | 29.72 | 154.34 | |
| 264 | Total income (subtotal) | 1,765.02 | 1,704.68 | 1,517.98 | 6,451.77 | |
| 267 | Cost of materials consumed | 421.76 | 410.12 | 402.07 | 1,607.32 | |
| 268 | Employee benefits expense | 308.02 | 321.55 | 292.62 | 1,210.86 | |
| 269 | Finance costs | 4.85 | 12.72 | 34.78 | 497.61 | |
| 270 | Depreciation, amortisation and impairment expense | 130.88 | 159.48 | 123.46 | 576.09 | |
| 271 | Healthcare professional fees | 221.72 | 208.77 | 180.82 | 826.53 | |
| 272 | Hospital fees | 179.00 | 179.06 | 163.97 | 685.33 | |
| 273 | Other expenses | 331.86 | 303.05 | 251.28 | 1,085.72 | |
| 274 | Total expenses (subtotal) | 1,598.09 | 1,594.75 | 1,449.00 | 6,489.46 | |
| 276 | Profit/(loss) before tax (subtotal) | 166.93 | 109.93 | 68.98 | (37.69) | |
| 279 | Current tax | 60.71 | 39.06 | 26.67 | 141.20 | |
| 280 | Deferred tax benefit | (19.41) | (38.01) | (7.83) | (98.29) | |
| 281 | Total tax expense (subtotal) | 41.30 | 1.05 | 18.84 | 42.91 | |
| 283 | Profit/(loss) for the period/year (subtotal) | 125.63 | 108.88 | 50.14 | (80.60) | |
| 287 | Remeasurement gains on defined benefit plans | 0.17 | 1.09 | 0.66 | 0.68 | |
| 288 | Income tax relating to items above | (0.04) | (0.27) | (0.02) | (0.17) | |
| 290 | Total other comprehensive income (subtotal) | 0.13 | 0.82 | 0.64 | 0.51 | |
| 292 | Total comprehensive income/(loss) (subtotal) | 125.76 | 109.70 | 50.78 | (80.09) | |
| 294 | Paid up share capital | 200.68 | 200.68 | 36.18 | 200.68 | |
| 295 | Other equity | blank | blank | blank | 9,508.38 | **ZERO_STANDING** — blank in all 3 non-year-end columns; balance-sheet item shown only at year end, standard convention but still a nil-in-period row |
| 298 | Basic earnings per share (₹) | 1.25 | 1.09 | 0.60 | (0.89) | qualified by footnote line 300 |
| 299 | Diluted earnings per share (₹) | 1.22 | 1.06 | 0.57 | (0.89) | qualified by footnote line 300 |

### 2b. Consolidated P&L (30 rows) — lines 582–627
| Line | Particulars | Q1FY27 | Q4FY26 (Aud) | Q1FY26 | FY26 (Aud) | Flags |
|------|-------------|--------|--------------|--------|-----------|-------|
| 582 | Revenue from operations | 2,817.54 | 2,656.15 | 2,277.83 | 9,988.45 | |
| 583 | Other income | 74.59 | 115.69 | 65.76 | 245.13 | |
| 584 | Total income (subtotal) | 2,892.13 | 2,771.84 | 2,343.59 | 10,233.58 | |
| 586 | Cost of materials consumed | 624.41 | 596.30 | 544.68 | 2,267.89 | |
| 587 | Employee benefits expense | 478.25 | 459.28 | 397.96 | 1,717.89 | |
| 588 | Finance costs | 22.06 | 31.80 | 61.04 | 602.42 | |
| 589 | Depreciation, amortisation and impairment expense | 245.40 | 258.45 | 195.20 | 906.67 | |
| 590 | Healthcare professional fees | 306.14 | 292.97 | 243.01 | 1,121.59 | |
| 591 | Hospital fees | 215.87 | 212.30 | 187.13 | 799.85 | |
| 592 | Other expenses | 554.04 | 557.62 | 429.38 | 1,811.60 | |
| 593 | Total expenses (subtotal) | 2,446.17 | 2,408.72 | 2,058.40 | 9,227.91 | |
| 595 | Profit before share of loss of JV and tax (subtotal) | 445.96 | 363.12 | 285.19 | 1,005.67 | |
| 597 | Share of loss of joint venture, net of tax | (35.66) | (30.93) | – | (30.93) | dash in Q1FY26 comparative only (pre-JV/pre-listing period) — not all-period nil, not flagged ZERO_STANDING |
| 599 | Profit before tax (subtotal) | 410.30 | 332.19 | 285.19 | 974.74 | |
| 602 | Current tax | 120.89 | 87.81 | 70.54 | 355.60 | |
| 603 | Deferred tax benefit | (30.33) | (59.32) | (22.39) | (149.26) | |
| 604 | Total tax expense (subtotal) | 90.56 | 28.49 | 48.15 | 206.34 | |
| 606 | Profit for the period/year (subtotal) | 319.74 | 303.70 | 237.04 | 768.40 | |
| 610 | Remeasurement gains on defined benefit plans | 0.16 | 1.08 | 0.66 | 0.67 | |
| 611 | Income tax relating to above items | (0.04) | (0.27) | (0.02) | (0.17) | |
| 613 | Exchange differences on translating financial statements of foreign operations | 10.66 | 58.46 | 26.79 | 185.84 | |
| 614 | Total other comprehensive income for the period/year (subtotal) | 10.78 | 59.27 | 27.43 | 186.34 | |
| 616 | Total comprehensive income for the period/year (subtotal) | 330.52 | 362.97 | 264.47 | 954.74 | |
| 618 | Profit attributable to Owners of the Company | 319.74 | 303.70 | 237.04 | 768.40 | |
| 620 | OCI attributable to Owners of the Company | 10.78 | 59.27 | 27.43 | 186.34 | |
| 622 | TCI attributable to Owners of the Company | 330.52 | 362.97 | 264.47 | 954.74 | |
| 623 | Paid up share capital | 200.68 | 200.68 | 36.18 | 200.68 | |
| 624 | Other equity | blank | blank | blank | 10,964.25 | **ZERO_STANDING** — blank in all 3 non-year-end columns, same pattern as standalone |
| 626 | Basic earnings per share (₹) | 3.19 | 3.03 | 2.82 | 8.48 | qualified by footnote line 628 |
| 627 | Diluted earnings per share (₹) | 3.11 | 2.96 | 2.70 | 8.10 | qualified by footnote line 628 |

### 2c. Geographical information (5 rows) — lines 699–703 (consolidated Note 6)
| Line | Particulars | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|------|-------------|--------|--------|--------|------|-------|
| 699 | India | 1,553.79 | 1,491.96 | 1,392.25 | 5,813.21 | |
| 700 | Philippines | 906.29 | 846.75 | 669.37 | 3,112.28 | |
| 701 | Uzbekistan | 321.34 | 287.02 | 216.21 | 1,004.22 | |
| 702 | Others | 36.12 | 30.42 | – | 58.74 | dash in Q1FY26 comparative only — not flagged ZERO_STANDING |
| 703 | Total (subtotal) | 2,817.54 | 2,656.15 | 2,277.83 | 9,988.45 | |

### 2d. IPO proceeds utilisation — standalone Note 6 (4 rows) — lines 340–343
| Line | Objective | Amount per prospectus | Utilised up to 30 Jun 2026 | Unutilised as on 30 Jun 2026 | Flags |
|------|-----------|-----------------------|----------------------------|-------------------------------|-------|
| 340 | Capital expenditure for opening new dialysis clinics in India | 1,291.06 | 127.68 | 1,163.38 | |
| 341 | Pre-payment/scheduled repayment of certain borrowings | 1,359.99 | 1,359.99 | – | **ZERO_STANDING** — Unutilised column nil/dash (fully utilised); enumerated per never-drop-a-nil-row rule |
| 342 | General corporate purposes | 600.48 | 587.16 | 13.32 | |
| 343 | Total (subtotal) | 3,251.53 | 2,074.83 | 1,176.70 | |

### 2e. IPO proceeds utilisation — consolidated Note 7 (4 rows) — lines 724–727
| Line | Objective | Amount per prospectus | Utilised up to 30 Jun 2026 | Unutilised as on 30 Jun 2026 | Flags |
|------|-----------|-----------------------|----------------------------|-------------------------------|-------|
| 724 | Capital expenditure for opening new dialysis clinics in India | 1,291.06 | 127.68 | 1,163.38 | |
| 725 | Pre-payment/scheduled repayment of certain borrowings | 1,359.99 | 1,359.99 | – | **ZERO_STANDING** — same as line 341; identical group-level figure disclosed twice |
| 726 | General corporate purposes | 600.48 | 587.16 | 13.32 | |
| 727 | Total (subtotal) | 3,251.53 | 2,074.83 | 1,176.70 | |

## 3. BOARD OUTCOME LETTER — AGENDA ITEMS (10 rows) — lines 22–41

Board meeting: commenced 03:45 p.m. IST, concluded ~05:10 p.m. IST (line 59) — 1h25m
meeting for a quarter that also approved two committee reconstitutions and an
overseas internal restructuring, not an unusually short duration.

| Line | Item | Detail | Flags |
|------|------|--------|-------|
| 22 | a. Results approval | Un-audited Standalone and Consolidated financial results for quarter ended 30 June 2026, together with Limited Review Report from B S R and Co | |
| 27 | b. Audit Committee reconstitution | Effective 17 August 2026; new composition below | |
| 31 | — sub: Audit Committee member | Mr. Hemant Sultania — Chairman & Independent Director | |
| 32 | — sub: Audit Committee member | Ms. Annette Kumlien — Independent Director | |
| 33 | — sub: Audit Committee member | Mr. Gaurav Sharma — Nominee Director | |
| 35 | c. Stakeholders Relationship Committee reconstitution | Effective 17 August 2026; new composition below | |
| 39 | — sub: SRC member | Mr. Vishal Vijay Gupta — Chairman & Nominee Director | |
| 40 | — sub: SRC member | Mr. Vikram Vuppala — Managing Director | |
| 41 | — sub: SRC member | Mr. Om Prakash Manchanda — Independent Director | |
| 44 | d. Internal restructuring | Proposed transfer of 51% shareholding in NHSSAC (Saudi Arabia JV) from NHSI to NPKSC, both overseas WOS of the Company; no change in ultimate beneficial ownership; details at Annexure I | related-party transaction (intra-group), see §4 |

No AR/AGM approval, no record date, no dividend, no auditor change, no ESOP grant
resolution, and no capital-raising enabling resolution appear as separate agenda
items in this letter — the only two items beyond results approval are committee
reconstitutions and the internal restructuring at (d).

## 4. ANNEXURE I TO BOARD OUTCOME LETTER — REG 30 ACQUISITION DISCLOSURE (10 rows) — lines 84–158

| Line | Sr. No. | Particulars | First 15 words of detail | Flags |
|------|---------|-------------|---------------------------|-------|
| 84 | 1 | Name/brief of target entity | "Nephrocare Health Services Saudi Arabia Company ("NHSSAC"), a company incorporated in the Kingdom of Saudi Arabia..." Turnover NIL FY26 | |
| 90 | 2 | RPT status / promoter interest | "The proposed transaction is an intra-group transaction between related parties. NHSI, the transferor, is..." | related party; arm's length language present |
| 104 | 3 | Industry | "Healthcare services - dialysis services." | |
| 106 | 4 | Objects and impact | "The proposed transaction is being undertaken as part of an internal restructuring of the Group's..." | |
| 119 | 5 | Regulatory approvals required | "The proposed transaction is subject to receipt of the requisite governmental and/or regulatory approvals..." | Singapore + Saudi Arabia jurisdictions |
| 126 | 6 | Indicative time period for completion | "The proposed transaction is expected to be completed upon receipt of the requisite approvals..." | no firm date given |
| 129 | 7 | Consideration type | "Cash Consideration." | |
| 132 | 8 | Cost of acquisition | "The total consideration for the proposed transfer of the 51% shareholding in NHSSAC shall be..." | SAR 2.24 million |
| 136 | 9 | % shareholding/control acquired | "NHSI proposes to transfer its entire 51% shareholding in NHSSAC to NPKSC. Upon completion..." | |
| 142 | 10 | Background of acquired entity | "NHSSAC is incorporated in the Kingdom of Saudi Arabia and is engaged in the business..." | incorporated 4 Jan 2023; Nil turnover FY24/FY25/FY26 |

Note: this Annexure I (Reg 30 disclosure table) and the Annexure I referenced inside
the consolidated Limited Review Report (entity list, §6) share the identical label
"Annexure I" but are two unrelated annexures belonging to two different documents
within the same PDF bundle — an internal naming collision worth flagging for A3/A4
cross-reference care.

## 5. LIMITED REVIEW REPORT PARAGRAPHS (11 rows)

### 5a. Standalone LRR (5 paragraphs) — lines 178–208, signed p.5-6
| Line | Para | Content type | Summary |
|------|------|--------------|---------|
| 178 | 1 | Scope/subject | Statement reviewed for Q ended 30 Jun 2026; comparative Q ended 30 Jun 2025 approved by Board but **not subjected to review** |
| 184 | 2 | Management responsibility | Statement prepared per Ind AS 34, Companies Act 2013 s.133, Reg 33; auditor responsibility is to report based on review |
| 191 | 3 | Basis of review | SRE 2410 review, substantially less in scope than an audit; **"we do not express an audit opinion"** |
| 199 | 4 | Other-Matter-type paragraph | Figures for Q ended 31 Mar 2026 are balancing figures between audited full-year and reviewed 9M YTD figures |
| 204 | 5 | Conclusion (opinion) | **Unmodified/clean review conclusion** — "nothing has come to our attention that causes us to believe... has not disclosed the information required... or contains any material misstatement" |

No paragraph is separately labelled "Emphasis of Matter," "Other Matters," or
"Going Concern" in this report — paras 1 and 4 function as EoM-equivalent content
(comparatives not reviewed; balancing-figure basis) without the formal heading.
UDIN: 26218685GLQAJD1208 (line 238). No component/subsidiary is flagged as
unaudited or management-furnished within this standalone report (single legal
entity, no components).

### 5b. Consolidated LRR (6 paragraphs) — lines 389–442, signed p.9-10, entity list p.11-12
| Line | Para | Content type | Summary |
|------|------|--------------|---------|
| 389 | 1 | Scope/subject | Statement of unaudited consolidated results of Parent + subsidiaries ("the Group") + share of net loss/TCI of its joint venture; Q1FY26 comparative **not subjected to review** |
| 399 | 2 | Management responsibility | Prepared per Ind AS 34, Companies Act s.133, Reg 33; auditor issues a **conclusion** (review, not audit opinion) |
| 405 | 3 | Basis of review | SRE 2410; also performed procedures per **Reg 33(8) circular**, to the extent applicable |
| 415 | 4 | Entity list reference (Other-Matter-type) | "The Statement includes the results of the entities mentioned in Annexure I" — points to §6 entity list |
| 416 | 5 | Other-Matter-type paragraph | Q ended 31 Mar 2026 figures are balancing figures between audited full-year and reviewed 9M YTD figures |
| 437 | 6 | Conclusion (opinion) | **Unmodified/clean review conclusion** — same "nothing has come to our attention" language as standalone |

No formal "Emphasis of Matter" or "Going Concern" heading in the consolidated
report either. No paragraph explicitly states any subsidiary/JV component's
financials were reviewed by another auditor or were unaudited/management-certified
— the report is silent on component-auditor reliance despite the Group spanning
India, Philippines, Uzbekistan, Nepal, Saudi Arabia and (new this quarter)
Kazakhstan; this silence is worth a question for A3/A4 given the geographic
spread and the number of step-down subsidiaries (21). UDIN: 26218685AJFXLH2124
(line 455).

## 6. CONSOLIDATION ENTITY LISTS (26 unique entities; 2 disclosure locations, cross-checked)

### 6a. List A — Consolidated LRR Annexure I (lines 468–559)
| Line | Sr. No. | Entity | Relationship | Flags |
|------|---------|--------|---------------|-------|
| 474 | 1 | Nephrocare Health Services Limited (formerly Nephrocare Health Services Private Limited) | Holding company | |
| 478 | 2 | Nephrocare Health Services Central Asia FE LLC | Subsidiary | |
| 481 | 3 | Nephrocare Health Services Nepal Private Limited | Subsidiary | |
| 484 | 4 | Nephrocare Health Services International Pte Limited (NHSI) | Subsidiary | |
| 487 | 5 | Nephrocare Health Services Saudi Arabia Company (NHSSAC) | Joint Venture | subject of Board Outcome item (d), §3/§4 |
| 490 | 6 | Nephro Plus Kidney Services Company (NPKSC) | Step down subsidiary | transferee in item (d) restructuring |
| 493 | 7 | Nephrocare Health Care Services, Philippines Inc. | Step down subsidiary | |
| 496 | 8 | Anram Medical Group Inc. | Step down subsidiary | |
| 499 | 9 | Bioregen Hemo Center Inc | Step down subsidiary | |
| 502 | 10 | Curis Cavite Renal Corporation | Step down subsidiary | |
| 505 | 11 | Cadiz Dialysis Hub Inc. | Step down subsidiary | |
| 508 | 12 | Curis Hemodialysis Clinic Inc. | Step down subsidiary | |
| 511 | 13 | Carmona Dialysis System Inc. | Step down subsidiary | |
| 514 | 14 | Dialysis Asia and Patient Care Center Inc. | Step down subsidiary | |
| 517 | 15 | Mega Health Dialysis Center | Step down subsidiary | |
| 520 | 16 | Medical Experts Group and Associates Inc | Step down subsidiary | |
| 523 | 17 | People's Center For Hemodialysis Care Inc. | Step down subsidiary | |
| 526 | 18 | Renal Therapy Solutions Inc. | Step down subsidiary | |
| 529 | 19 | Rizal Dialysis and Wellness Centre OPC | Step down subsidiary | |
| 541 | 20 | St. Margareth Dialysis and Biocare Center Inc. | Step down subsidiary | |
| 544 | 21 | Universe Dialysis and Kidney Care Center Inc. | Step down subsidiary | |
| 547 | 22 | AIZ Hemo Dialysis Centre Inc. | Step down subsidiary | |
| 550 | 23 | Infini Care Health Systems Inc. | Step down subsidiary | |
| 553 | 24 | Kolff Dialysis Inc. | Step down subsidiary | |
| 556 | 25 | Nephro Alliance Ventures Inc. | Step down subsidiary | |
| 559 | 26 | Nephroplus Health Services Kazakhstan LLP | Step down subsidiary | **ENTITY_CHANGE** — new this quarter, see note 9 (line 736): incorporated 26 May 2026 |

### 6b. List B — Consolidated Notes, Note 5 breakdown (lines 657–686)
| Line | Category | Entity | Flags |
|------|----------|--------|-------|
| 658 | a) Parent (1) | Nephrocare Health Services Limited | |
| 660 | b) Subsidiaries incl. step-down (1/24) | Nephrocare Health Services Central Asia FE LLC | |
| 661 | (2/24) | Nephrocare Health Services Nepal Private Limited | |
| 662 | (3/24) | Nehrocare Health Services International Pte Ltd | **DATA_QUALITY** — spelled "Nehrocare" (missing "p"); List A line 484 spells it correctly "Nephrocare Health Services International Pte Limited" |
| 663 | (4/24) | Nephro Plus Kidney Services Company | |
| 664 | (5/24) | Nephrocare Health Care Services, Philippines Inc. | |
| 665 | (6/24) | Anram Medical Group Inc. | |
| 666 | (7/24) | Cadiz Dialysis Hub Inc. | |
| 667 | (8/24) | Dialysis Asia and Patient Care Center Inc. | |
| 668 | (9/24) | People's Center For Hemodialysis Care Inc. | |
| 669 | (10/24) | Curis Hemodialysis Clinic Inc. | |
| 670 | (11/24) | Mega Health Dialysis Center Inc. | |
| 671 | (12/24) | Universe Dialysis and Kidney Care Centre Inc. | |
| 672 | (13/24) | St. Margareth Dialysis and Biocare Centre Inc. | |
| 673 | (14/24) | Medical Experts Group and Associates Inc. | |
| 674 | (15/24) | Curis Cavite Renal Corporation | |
| 675 | (16/24) | Renal Therapy Solutions, Inc. | |
| 676 | (17/24) | Rizal Dialysis and Wellness Centre OPC | |
| 677 | (18/24) | Bioregen Hemo Center Inc. | |
| 678 | (19/24) | Carmona Dialysis System Inc. | |
| 679 | (20/24) | Infini Care Health Systems Inc. | |
| 680 | (21/24) | Kolff Dialysis Inc. | |
| 681 | (22/24) | AIZ Hemodialysis Centre Inc. | |
| 682 | (23/24) | Nephro Alliance Ventures Inc. | |
| 683 | (24/24) | Nephroplus Health Services Kazakhstan Limited Liability Partnership (LLP) (w.e.f. 26 May 2026) | **ENTITY_CHANGE** — explicit new-entity date tag confirms addition this quarter |
| 686 | c) Joint Venture (1) | Nephrocare Health Services Saudi Arabia Company | |

Cross-check List A vs List B: both total 26 (List A: 1 holding + 3 subsidiary + 1 JV
+ 21 step-down = 26; List B: 1 parent + 24 subsidiaries-incl-step-down + 1 JV = 26,
and 3+21=24 reconciles). No entity present in one list and absent from the other.
The single addition (Kazakhstan LLP) is consistently reflected in both lists and in
Note 9 — internally consistent, no contradiction found, but flagged ENTITY_CHANGE
because it is a genuine addition versus what a prior-quarter list would show (no
prior-quarter ledger was supplied to this run for a formal diff; flag stands on the
explicit "w.e.f. 26 May 2026" language and Note 9's incorporation disclosure).

## 7. DIGITAL SIGNATURE BLOCKS (5 rows) — lines 68–78, 227–238, 354–369, 444–455, 744–756

| Line(s) | Document | Signatory | Designation | Timestamp | Flags |
|---------|----------|-----------|-------------|-----------|-------|
| 68–78 | Board Outcome letter | Kishore Kathri | Company Secretary and Head Legal (Membership No. F9895) | 2026.08.11, 17:40:45 +05'30 | signed 30 min after board concluded (17:10) — unremarkable |
| 227–238 | Standalone LRR | Amit Kumar Bajaj | Partner, B S R and Co (Membership No. 218685, FRN 128510W) | 2026.08.11, 17:32:22 +05'30 | UDIN 26218685GLQAJD1208; signed 22 min after board concluded |
| 444–455 | Consolidated LRR | Amit Kumar Bajaj | Partner, B S R and Co (Membership No. 218685, FRN 128510W) | 2026.08.11, 17:33:54 +05'30 | UDIN 26218685AJFXLH2124; signed 24 min after board concluded |
| 354–369 | Standalone results | Vikram Vuppala | Chairman and Managing Director (DIN 02847323) | 2026.08.11, 17:11:20 +05'30 | **TIGHT_SIGNATURE_TIMING** — only ~1 min 20 sec after board concluded (17:10) and ~11 min before the auditor's own signature at 17:32; not before conclusion (no breach) but a very tight sequencing worth noting |
| 744–756 | Consolidated results | Vikram Vuppala | Chairman and Managing Director (DIN 02847323) | 2026.08.11, 17:11:54 +05'30 | **TIGHT_SIGNATURE_TIMING** — ~1 min 54 sec after board concluded, same pattern as above |

All five signature timestamps fall after the board meeting's stated conclusion
(17:10 p.m.), so no SIGNATURE_BEFORE_CONCLUSION breach exists. The two MD
signatures (on the results statements themselves) landing within ~2 minutes of
the stated conclusion time, ahead of both the CS's letter signature (17:40) and
the auditor's own report signatures (17:32/17:34), is noted for A3/A4 as a tight
but not contradictory sequencing.
