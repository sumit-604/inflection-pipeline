# A2 ENUMERATION LEDGER — Black Rose Industries Ltd (BLACKROSE), Q1 FY27, results filing

Source: /home/user/inflection-pipeline/runs/blackrose-q1fy27/work/extract_results_blackrose_q1fy27.txt
(523 lines, 8 pages, Lakhs, x0.01 to Rs Cr; prior-quarter ledger not provided — ENTITY_CHANGE
flags below are based on the current filing's own text of the winding-up resolution, not a
cross-quarter diff.)

```
=== A2 COUNT TEST ===
category: notes            grep_count: 13   sweep_count: 13   match: yes
category: line_items       grep_count: 68   sweep_count: 68   match: yes
category: zero_standing    grep_count: 5    sweep_count: 5    match: yes
category: agenda_items     grep_count: 4    sweep_count: 4    match: yes
category: auditor_paras    grep_count: 12   sweep_count: 12   match: yes
category: entities         grep_count: 1    sweep_count: 1    match: yes
category: annexure_items   grep_count: 8    sweep_count: 8    match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Grep basis (commands run against the extract file):
- notes: `grep -c -E "^\s*[0-9]+\)"` = 11 (numbered financial-statement notes) + `grep -c -E "The figures for the Quarter ended"` = 2 (asterisk-marked balancing-figure footnotes, one per statement) = 13.
- line_items: non-blank line count of standalone table body (lines 254-282, 29 raw lines, 1 merged as OCR artifact -> 28) + consolidated table body (lines 435-474, 40 lines) = 68.
- zero_standing: manual flag count on line_items sweep (below) = 5.
- agenda_items: `grep -n -E "^[0-9]+\.\s"` restricted to lines 36-65 (Board Outcome letter) = 4.
- auditor_paras: `grep -n -E "^\s*[0-9]+\.\s"` restricted to lines 182-232 (standalone report, 4) + lines 329-413 (consolidated report, 6) = 10, plus manual sweep for unnumbered continuation paragraphs (`grep -c -E "We also performed procedures|Our conclusion on the statement is not modified"`) = 2 -> 12.
- entities: `grep -n -i subsidiary` -> 1 distinct entity named (B.R. Chemicals Co. Limited, Japan) across all mentions.
- annexure_items: `sed -n '119,156p' | grep -n -E "^\s*[0-9]+\s"` = 8 (Annexure A, Sr 1-8).
- signature_blocks: `grep -c "Digitally signed"` = 1 + `grep -c "DIN :"` = 2 + `grep -c "UDIN"` = 2 = 5.

---

## 1. Board Outcome letter — agenda items (lines 15-107)

| # | Line | Item | Detail (first 15 words) | Flags |
|---|------|------|--------------------------|-------|
| 1 | 38-44 | Results approval | "Pursuant to Regulation 33... Board... approved the Standalone and Consolidated Unaudited Financial Results for the quarter ended 30th June 2026" | |
| 2 | 46-50 | Interim dividend declaration | "Declaration of payment of Interim Dividend of Rs. 2 per equity (i.e. 200%...)"; Record Date 6 Aug 2026 | |
| 3 | 52-55 | AGM notice | "The Notice of 36th AGM... to be held on Wednesday, 9th September, 2026 at 02:00 p.m. (IST)" via VC/OAVM | |
| 4 | 57-64 | Winding up of B.R. Chemicals Co. Limited, Japan (WOS) | "The Board of Directors considered and approved the winding up of B.R. Chemicals Co. Limited, Japan..." not expected material impact; disclosure at Annexure A | ENTITY_CHANGE |
| — | 80 | Meeting timing (administrative, not a numbered resolution) | "The Meeting of the Board of Directors commenced at 11:30 a.m. (IST) and concluded at 02:47 p.m.(IST)" — duration ~3h17m | |

Note: only 4 numbered resolutions in the letter (results, dividend, AGM notice, subsidiary wind-up).
No AR approval, director appointment/resignation, auditor change, scrutinizer appointment, ESOP grant,
or capital-raising enabling resolution items are present this quarter — their absence is itself
notable against the rule-3 checklist but there is no line to enumerate since they do not appear.

## 2. Signature/timestamp block — cover letter (lines 89-98)

| Line | Signatory | Designation | Timestamp | Flags |
|------|-----------|-------------|-----------|-------|
| 91-97 | Darshana Avadhoot Sawant | Company Secretary and Compliance Officer | Digitally signed, 2026.07.31 14:55:55 +05'30' | Timestamp is 8 min after board meeting concluded (14:47 IST) — consistent, no flag |

## 3. Annexure A — winding-up disclosure table under Reg 30/Sch III (lines 111-165)

| Sr | Line | Particulars | Details | Flags |
|----|------|-------------|---------|-------|
| 1 | 121-124 | Turnover/revenue/income and net worth contributed by unit/subsidiary in last FY | Turnover: Nil; Networth: Rs. 15.58 Lakhs (0.09%) | ZERO_STANDING (turnover Nil) |
| 2 | 127-128 | Date of agreement for sale | Not Applicable | ZERO_STANDING |
| 3 | 130-133 | Expected date of completion of sale/disposal | Voluntary winding up expected complete in 12 months, subject to regulatory approvals | |
| 4 | 134-135 | Consideration received from sale/disposal | Not Applicable | ZERO_STANDING |
| 5 | 137-140 | Buyer details / promoter-group affiliation | Not Applicable | ZERO_STANDING |
| 6 | 142-144 | Related party transaction / arm's length | Not Applicable | ZERO_STANDING |
| 7 | 146-150 | Sale outside Scheme of Arrangement / Reg 37A compliance | Not Applicable | ZERO_STANDING |
| 8 | 151-155 | Slump sale disclosures | Not Applicable | ZERO_STANDING |

(Note: the 6 "Not Applicable" annexure rows are disclosure-field non-events for a winding-up-by-
liquidation, not financial-statement standing line items, so they are tagged ZERO_STANDING here
for completeness per the "never drop a nil row" rule but are counted in the annexure_items
category, not double-counted in line_items.)

## 4. Standalone Limited Review Report — MM Nissim & Co LLP (lines 168-232)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 190-194 | Scope: reviewed Standalone Statement for quarter ended 30 June 2026 per Reg 33 | |
| 2 | 196-202 | Responsibility statement: Statement is management's responsibility, reviewed by Audit Committee, approved by Board, prepared per Ind AS 34 | |
| 3 | 204-213 | Basis of review: SRE 2410 standard, moderate assurance, less in scope than audit, no audit opinion expressed | |
| 4 | 215-221 | Conclusion: "nothing has come to our attention" — unmodified/unqualified review conclusion | |
| — | 223-232 | Signature block: For MM Nissim & Co LLP, Firm Reg No. 107122W/W100672, Saomil R Vora, Partner, Membership No. 135247, UDIN 26135247JBBAUD1348, Mumbai, 31 July 2026 | |

No Emphasis of Matter, no Going Concern paragraph, no Other Matters paragraph in the standalone report.

## 5. Consolidated Limited Review Report — MM Nissim & Co LLP (lines 317-413)

| Para | Line | Content | Flags |
|------|------|---------|-------|
| 1 | 337-342 | Scope: reviewed Consolidated Statement of Holding Company and its Subsidiary ("Group") for quarter ended 30 June 2026 | |
| 2 | 344-350 | Responsibility statement | |
| 3 | 352-363 | Basis of review: SRE 2410, moderate assurance, no audit opinion | |
| 3b (unnumbered) | 364-366 | Additional procedures performed per SEBI circular OR/CFD/CMD1/44/2019 under Reg 33(8) | |
| 4 | 368-370 | Entity list reviewed: "i) B.R. Chemicals Co. Limited (Japan) — Wholly Owned Foreign Subsidiary" | ENTITY_CHANGE |
| 5 | 379-385 | Conclusion: unmodified — "nothing has come to our attention" | |
| Other Matters (header) | 387 | Section heading | |
| 6 | 389-397 | Other Matters: unreviewed foreign subsidiary — total revenue Rs. 0.00 lakhs, net loss after tax Rs. 1.72 lakhs, total comprehensive loss Rs. 0.57 lakhs for the quarter; unaudited, management-furnished, not reviewed by its own auditor; management represents not material to Group | ZERO_STANDING (subsidiary revenue = Rs. 0.00 lakhs) |
| — (unnumbered) | 399-400 | Conclusion not modified in respect of reliance on unaudited interim standalone financial information certified by management | |
| — | 403-413 | Signature block: For MM Nissim & Co LLP, Firm Reg No. 107122W/W100672, Saomil R Vora, Partner, Membership No. 135247, UDIN 26135247AUPDMV7833, Mumbai, 31 July 2026 | |

No Emphasis of Matter, no Going Concern paragraph in the consolidated report; the "Other Matters"
paragraph on the unreviewed subsidiary is the only qualification-adjacent language.

## 6. Consolidation entity list (line 369, cross-referenced lines 338-339, 495-498)

| Entity | Relationship | Line(s) | Flags |
|--------|--------------|---------|-------|
| B.R. Chemicals Co. Limited, Japan | Wholly Owned Foreign Subsidiary — included in consolidated results for Q1 FY27, but Board approved winding it up this same meeting (agenda item 4); classified as discontinued operations since Board resolution of 14 Aug 2025 (continuation of 30 Jan 2025 resolution to discontinue operations) | 338-339, 368-369, 495-498 | ENTITY_CHANGE (subsidiary is mid-exit: discontinued-operations accounting since FY25/26, winding-up approved this quarter, will cease to be a subsidiary on completion — no prior-quarter ledger was supplied to this run for a formal diff, but the entity's own status changed materially within this filing) |

Only one subsidiary/entity in the consolidation scope — no other entities (associates, JVs, step-down
subsidiaries) are named anywhere in the extract.

## 7. Standalone unaudited financial results — line items (lines 237-315)

Figures in Lakhs; QoQ and YoY columns per filing (30-06-2026 Unaudited / 31-03-2026 Audited* /
30-06-2025 Unaudited / FY26 Audited).

| Row | Line | Particulars | Flags |
|-----|------|-------------|-------|
| 1 | 254 | Revenue from operations | |
| 2 | 255 | Other Income | |
| 3 | 256 | Total Revenue (1+2) | |
| 4 (header) | 257 | Expenditure | |
| 4a | 258 | Cost of materials consumed | |
| 4b | 259-260 | Purchase of stock-in-trade (OCR split the value row onto line 260; same line item) | |
| 4c | 261 | Changes in inventories of finished goods, WIP and traded goods | |
| 4d | 262 | Employee benefits expense | |
| 4e | 263 | Finance costs | |
| 4f | 264 | Depreciation and amortisation expense | |
| 4g | 265 | Other expenses | |
| 4-Total | 266 | Total Expenses | |
| 5 | 267 | Profit/(Loss) before exceptional items and tax (3-4) | |
| 6 | 268 | Exceptional items | ZERO_STANDING (dash in all 3 populated periods) |
| 7 | 269 | Profit/(Loss) before Tax (5-6) | |
| 8 (header) | 270 | Tax Expense | |
| 8a | 271 | Income Tax (including earlier year adjustments) | |
| 8b | 272 | Deferred Tax | |
| 9 | 273 | Net Profit/(Loss) from ordinary activities after tax (7-8) | |
| 10 (header) | 274 | Other Comprehensive Income/(loss) | |
| 10i | 275 | Items that will not be reclassified to profit or loss (net of tax) | |
| 10ii | 276 | Items that will be reclassified to profit or loss (net of tax) | ZERO_STANDING (dash in all 3 populated periods) |
| 11 | 277 | Total Comprehensive Income (9+10) | |
| 12 | 278 | Paid-up equity share capital (F.V. Rs 1/- per share) | |
| 13 | 279 | Other Equity excluding Revaluation Reserve | Only FY26 annual column populated (Rs 16,418.02 Lakhs); quarter columns blank — standard for interim filings, not flagged ZERO_STANDING |
| 14 (header) | 280 | Earnings per share (of Rs 1/- each) | |
| 14a | 281 | Basic | |
| 14b | 282 | Diluted | |

Standalone footnote: line 284, asterisk-marked — "The figures for the Quarter ended 31st March,
2026 are the balancing figures between the audited figures... and the year-to-date figures upto
the third Quarter" (counted in notes category).

Standalone notes 1-5 (lines 287-301):
| Note | Line | First 15 words | Flags |
|------|------|-----------------|-------|
| 1 | 288-290 | Results drawn per consistently followed accounting policies; reviewed by Audit Committee, approved by Board 31 July 2026; unmodified auditor report | |
| 2 | 292-293 | Statement prepared per Companies (Indian Accounting Standards) Rules, 2015 (Ind AS) | |
| 3 | 295-296 | Board declared Interim Dividend of Rs. 2 per equity share (200% of paid-up capital); Record Date 6 Aug 2026 | |
| 4 | 298-299 | Company's business falls within single primary segment "Chemicals"; no separate reportable segments per Ind AS 108 | |
| 5 | 301 | Figures of corresponding previous period regrouped wherever necessary | |

Standalone signature block (lines 303-314): For and on behalf of the Board of Directors of Black
Rose Industries Limited, Ambarish Daga, Whole-Time Director, DIN 07125212, Place: Mumbai, Date:
July 31, 2026 (no signing timestamp given, physical/typed signature block).

## 8. Consolidated unaudited financial results — line items (lines 418-518)

| Row | Line | Particulars | Flags |
|-----|------|-------------|-------|
| 1 | 435 | Revenue from operations | |
| 2 | 436 | Other Income | |
| 3 | 437 | Total Revenue (1+2) | |
| 4 (header) | 438 | Expenditure | |
| 4a | 439 | Cost of materials consumed | |
| 4b | 440 | Purchase of stock-in-trade | |
| 4c | 441 | Changes in inventories of finished goods, WIP and traded goods | |
| 4d | 442 | Employee benefits expense | |
| 4e | 443 | Finance costs | |
| 4f | 444 | Depreciation and amortisation expense | |
| 4g | 445 | Other expenses | |
| 4-Total | 446 | Total Expenses | |
| 5 | 447 | Profit/(Loss) before exceptional items and tax (3-4) | |
| 6 | 448 | Exceptional Items | ZERO_STANDING (no values shown in any period) |
| 7 | 449 | Profit/(Loss) before Tax (5-6) | |
| 8 (header) | 450 | Tax Expense | |
| 8a | 451 | Income Tax (including earlier year adjustments) | |
| 8b | 452 | Deferred Tax | |
| 9 | 453 | Net Profit/(Loss) from ordinary activities after tax (7-8) | |
| 10(a) | 454 | Profit before tax from continuing operations | |
| 10(b) | 455 | Tax expense of continuing operations | |
| 11 | 456 | Profit for the period from continuing operations [10(a)-10(b)] | |
| 12(a) | 457 | Profit/(loss) before tax from discontinued operations | |
| 12(b) | 458 | Tax expense of discontinued operations | ZERO_STANDING (blank in all periods) |
| 13 | 459 | Profit/(loss) for the period from discontinued operations [12(a)-12(b)] | |
| 14 | 460 | Profit for the period from continuing and discontinued operations (11+13) | |
| 15 (header) | 461 | Other Comprehensive Income/(loss) | |
| 15i | 462 | Items that will not be reclassified to profit or loss (net of tax) | |
| 15ii | 463 | Items that will be reclassified to profit or loss (net of tax) | ZERO_STANDING (blank in all periods) |
| 15iii | 464 | Other comprehensive income of discontinued operations (net of tax) | One column (30-06-2025) blank, others populated — not flagged fully zero |
| 16 | 465 | Total Comprehensive Income (14+15) | |
| 17 | 466 | Paid-up equity share capital (F.V. Rs 1/- per share) | |
| 18 | 467 | Other Equity excluding Revaluation Reserve | Only FY26 annual column populated (Rs 16,433.61 Lakhs); quarter columns blank — standard, not flagged |
| 19 (header) | 468 | Earnings per share (of Rs 1/- each) | |
| 19-Continuing (header) | 469 | From Continuing operations | |
| 19a | 470 | Basic | |
| 19b | 471 | Diluted | |
| 19-Discontinuing (header) | 472 | From Discontinuing operations | |
| 19a | 473 | Basic | |
| 19b | 474 | Diluted | |

Consolidated footnote: line 476, asterisk-marked — "The figures for the Quarter ended 31st March,
2026 are the balancing figures..." (counted in notes category).

Consolidated notes 1-6 (lines 479-502):
| Note | Line | First 15 words | Flags |
|------|------|-----------------|-------|
| 1 | 480-482 | Results drawn per accounting policies consistently followed by the Group; reviewed by Audit Committee, approved by Board 31 July 2026; unmodified report | |
| 2 | 484-485 | Statement prepared per Companies (Indian Accounting Standards) Rules, 2015 (Ind AS) | |
| 3 | 487-488 | Board declared Interim Dividend of Rs. 2 per equity share (200% of paid-up capital); Record Date 6 Aug 2026 | |
| 4 | 490-491 | Group's business falls within single primary segment "chemicals"; no separate reportable segments per Ind AS 108 | |
| 5 | 495-500 | Business operations of BR Chemicals Co. Ltd (WOS) classified as discontinued operations per Ind AS 105, following Board decision 14 Aug 2025 (continuation of 30 Jan 2025 resolution); discontinued-ops summary for period ended 30 June 2025: Total Income Rs. 0.06 lakhs, Expenses Rs. 1.78 Lakhs, Loss Rs. 1.72 lakhs, Comprehensive loss Rs. 2.29 lakhs | ENTITY_CHANGE (subsidiary status/accounting treatment) |
| 6 | 502 | Figures of corresponding previous period regrouped wherever necessary | |

Consolidated signature block (lines 504-518): For and on behalf of the Board of Directors of Black
Rose Industries Limited, Ambarish Daga, Whole-Time Director, DIN 07125212, Place: Mumbai, Date:
July 31, 2026 (no signing timestamp given).

## 9. Document identifiers (letterhead, not part of GATE A2 count test — captured for completeness)

Scrip Code 514183, ISIN INE761G01016, CIN L17120MH1990PLC054828, registered office 145/A Mittal
Towers, Nariman Point, Mumbai 400021, factory at Shree Laxmi Co-op. Industrial Estate, Hatkanangle,
Kolhapur, repeated identically on every page footer (pages 1,3,5,8) or letterhead (pages 4,6,7).
Auditor: MM Nissim & Co LLP, Chartered Accountants, Firm Reg. No. 107122W/W100672, Regd. Office
Barodawala Mansion, Worli, Mumbai. These are administrative/repeat elements, not disclosure units,
and are excluded from the count test.

---

## SUMMARY OF FLAGS RAISED

- ZERO_STANDING: 5 in-statement line items (standalone Exceptional items line 268; standalone OCI
  reclassifiable items line 276; consolidated Exceptional items line 448; consolidated tax expense
  of discontinued operations line 458; consolidated OCI reclassifiable items line 463) plus 6
  "Not Applicable" Annexure A rows (Sr 2,4,5,6,7,8) and the Sr 1 Nil turnover figure, plus the
  unreviewed-subsidiary Rs. 0.00 lakhs revenue disclosed in auditor Other Matters para 6.
- ENTITY_CHANGE: B.R. Chemicals Co. Limited, Japan — the sole consolidation entity, subject of
  Board Outcome agenda item 4 (winding-up approval), Annexure A, consolidated auditor report para
  4 (entity list) and Other Matters para 6, and consolidated note 5 (discontinued-operations
  classification since 14 Aug 2025 Board decision).

No MGMT_ABSENCE, REPEAT_QUESTION, or DROPPED_SLIDE flags apply — not a concall/presentation doctype.
No signature-timing flag: CS digital signature (14:55:55 IST) postdates board meeting conclusion
(14:47 IST) by 8 minutes, which is consistent, not anomalous.
