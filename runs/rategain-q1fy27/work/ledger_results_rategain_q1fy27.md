# A2 ENUMERATOR LEDGER — RateGain Travel Technologies Limited (RATEGAIN), Q1 FY27, Results

Source: /home/user/inflection-pipeline/runs/rategain-q1fy27/work/extract_results_rategain_q1fy27.txt
Unit convention: Millions -> x0.1 to Rs Crores (all Rs figures below are AS PRINTED in the extract, i.e. Rs million, per source; no conversion applied in this ledger — A3/A4 apply the x0.1 conversion when needed)
Prior-quarter ledger: not provided — entity/line cross-checks below are noted as "no prior baseline" rather than asserted ENTITY_CHANGE where the change is only inferable from in-document annotations.

```
=== A2 COUNT TEST ===
category: notes_standalone         grep_count: 9    sweep_count: 10   match: no  -> RESOLVED (see reconciliation log)
category: notes_consolidated       grep_count: 12   sweep_count: 12   match: yes
category: line_items_standalone_pl grep_count: 24   sweep_count: 24   match: yes
category: line_items_consol_pl     grep_count: 33   sweep_count: 33   match: yes
category: line_items_ppa_table     grep_count: 7    sweep_count: 7    match: yes
category: agenda_items_board       grep_count: 2    sweep_count: 2    match: yes
category: agenda_items_annexureB   grep_count: 4    sweep_count: 4    match: yes
category: entities_annexureA       grep_count: 11   sweep_count: 18   match: no  -> RESOLVED (see reconciliation log)
category: auditor_paras_standalone grep_count: 5    sweep_count: 5    match: yes
category: auditor_paras_consol     grep_count: 6    sweep_count: 6    match: yes
category: signature_date_blocks    grep_count: 5    sweep_count: 5    match: yes
gate_a2: pass (after reconciliation)
=== END COUNT TEST ===
```

### RECONCILIATION LOG (mismatches found and resolved before emission)

1. **notes_standalone**: naive grep `^\s*[0-9]{1,2}[\s.]` returned 9 hits (notes 1,2,3,4,6,7,8,9,10), skipping Note 5. Manual sweep of the standalone notes block (page 5, lines 230-282) found Note 5 at line 267, but the source PDF's OCR rendered the leading digit "5" as the letter "s" ("s The Company's business activity falls within a single segment..."). Re-swept with an OCR-tolerant pattern (`^\s*([0-9]{1,2}|s)[\s.]`) — confirmed 10 standalone notes, sequential 1-10, none actually missing. This is an OCR artifact, not a missing disclosure; flagged `OCR_ANOMALY` on the Note 5 row below so A3/A4 do not mistake the source digit for a typo in the company's own filing.
2. **entities_annexureA**: naive grep with `^\s{0,4}[0-9]{1,2}\.` (narrow leading-whitespace tolerance) returned 11 hits, missing S.No. 3-9 because those seven rows carry 5 leading spaces before the digit in the extracted text (table column alignment drift from PDF extraction), one more space than the pattern allowed. Re-swept with wider whitespace tolerance (`^\s*[0-9]{1,2}\.\s`) — confirmed all 18 rows of Annexure A (S.No. 1-18), sequential, none missing. Flagged `OCR_ANOMALY` on the entities table note below.

Both mismatches were extraction/whitespace artifacts of the grep pattern, not missing disclosures. Final reconciled counts are used throughout this ledger and match on both count methods.

---

## 1. BOARD OUTCOME — AGENDA ITEMS (Board meeting letter, page 1)

Board meeting commenced 12:00 noon and concluded 1:15 p.m. (line 50) — approx. 1 hour 15 minutes.

| # | Line | Agenda item | Detail | Flags |
|---|------|-------------|--------|-------|
| 1 | 31 | Unaudited (Standalone and Consolidated) Financial Results for quarter ended June 30, 2026 | Approved; disseminated on company website; enclosed as Annexure A: (a) Financial Results, (b) Limited Review Report | — |
| 2 | 40 | Issuance of Corporate Guarantee | Up to USD 65.00 million to banks/FIs for loan facilities to be availed by RateGain Technologies Limited, UK and Sojern, Inc. (wholly owned subsidiaries); details in Annexure B | — |

No other agenda items disclosed: no AR approval, no AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant resolution, no capital-raising enabling resolution appear in this Board Outcome letter. `ZERO_STANDING` — these categories are template-standard Board Outcome agenda slots that carry no item this quarter.

| # | Line | Standing agenda category (not triggered this quarter) | Flags |
|---|------|---------------------------------------------------------|-------|
| 3 | n/a | AR approval | ZERO_STANDING |
| 4 | n/a | AGM notice / record date | ZERO_STANDING |
| 5 | n/a | Dividend | ZERO_STANDING |
| 6 | n/a | Director appointment/resignation | ZERO_STANDING |
| 7 | n/a | Auditor change | ZERO_STANDING |
| 8 | n/a | Scrutinizer appointment | ZERO_STANDING |
| 9 | n/a | ESOP grant resolution (note: ESOP *exercise*, not grant, is disclosed in Note 6/7 below) | ZERO_STANDING |
| 10 | n/a | Capital-raising enabling resolution | ZERO_STANDING |

## 2. ANNEXURE B — CORPORATE GUARANTEE DISCLOSURE TABLE (page 13, lines 682-703)

| # | Line | S.No. | Particular | Content (first ~15 words) | Flags |
|---|------|-------|------------|----------------------------|-------|
| 1 | 683-685 | 1 | Name of party for which guarantee/indemnity/surety was given | "RateGain Technologies Limited, UK and Sojern, Inc. a wholly owned subsidiaries of the Company" | — |
| 2 | 686-691 | 2 | Promoter/promoter group/group companies interest | "The promoters/promoter group/group companies do not have any interest in this transaction" — arm's length | — |
| 3 | 693-698 | 3 | Brief details of guarantee/indemnity/surety | "Corporate guarantee for an amount of upto USD 65.00 million in favour of HSBC Bank, JP Morgan Bank and CITI Bank" | — |
| 4 | 699-703 | 4 | Impact on listed entity | "Company does not foresee any impact... issued to secure facility extended to RateGain Technologies Limited UK and Sojern Inc." | — |

## 3. SIGNATURE / DATE BLOCKS

| # | Line | Signatory | Designation | Timestamp | Flags |
|---|------|-----------|-------------|-----------|-------|
| 1 | 56-62 | Mukesh Kumar | General Counsel, Company Secretary & Compliance Officer (Membership No. A17925) | Digitally signed 2026.08.06 13:24:02 +05'30 | — (board meeting concluded 1:15 p.m. / 13:15; signature at 13:24 is 9 minutes AFTER conclusion, consistent — not a pre-conclusion-signature flag) |
| 2 | 154-166 | Rajesh Kumar Agarwal, Partner (Membership No. 105546), for Deloitte Haskins & Sells LLP | Standalone auditor review report | Dated August 06, 2026; UDIN at line 164 OCR-garbled ("2b\055465XC.!,OT3b75") | OCR_ANOMALY — UDIN not independently verifiable from this extract; re-source from filed PDF/exchange copy before citing the UDIN number |
| 3 | 317-318 | (unsigned — title only) | Chairman and Managing Director | Date 06 August 2026, Place Noida | ZERO_STANDING — no printed name captured against the standalone statement's CMD signature line in the extract |
| 4 | 405-417 | Rajesh Kumar Agarwal, Partner (Membership No. 105546), for Deloitte Haskins & Sells LLP | Consolidated auditor review report | Dated August 06, 2026; UDIN at line 415 OCR-garbled ("20\0S546WROVOC S \ 4~") | OCR_ANOMALY — UDIN not independently verifiable from this extract |
| 5 | 665-674 | (unsigned — title only, OCR garbage at line 670: "::::::.::::•3 ...") | Chairman and Managing Director | Date 06 August 2026, Place Noida | OCR_ANOMALY / ZERO_STANDING — signature stamp/image not legibly OCR'd; no printed name captured |

## 4. AUDITOR REVIEW REPORT — STANDALONE (pages 2-3, lines 88-171)

| # | Line | Paragraph | First ~15 words | Flags |
|---|------|-----------|-------------------|-------|
| 1 | 94-98 | Para 1 (scope statement) | "We have reviewed the accompanying Statement of Standalone Unaudited Financial Results... includes RateGain Employees Benefit Trust" | — |
| 2 | 100-105 | Para 2 (management responsibility / Ind AS 34 basis) | "This Statement, which is the responsibility of the Company's Management and approved by the Board" | — |
| 3 | 107-119 | Para 3 (SRE 2410 basis of review, scope-limitation language, no audit opinion expressed) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410" | — |
| 4 | 121-128 | Para 4 (conclusion — unmodified) | "Based on our review conducted and procedures performed... nothing has come to our attention that causes us to believe" | — |
| 5 | 142-151 | Para 5 (Other Matter — RateGain Employees Benefit Trust not reviewed by this auditor; total revenue NIL, net loss Rs 0.004 mn, relies on other auditor's report; conclusion not modified) | "We did not review the interim financial results of RateGain Employees Benefit Trust... total revenue of Rs NIL" | — |

Opinion type: unmodified review conclusion. No Emphasis of Matter. One Other Matter paragraph (para 5, Trust carve-out). No Going Concern paragraph. Entity reviewed directly: RateGain Travel Technologies Limited (standalone) including the Trust by reliance on another auditor. Unaudited/management-furnished entity: RateGain Employees Benefit Trust (reviewed by a different/other auditor, not Deloitte).

## 5. AUDITOR REVIEW REPORT — CONSOLIDATED (pages 7-9, lines 336-475)

| # | Line | Paragraph | First ~15 words | Flags |
|---|------|-----------|-------------------|-------|
| 1 | 342-347 | Para 1 (scope statement, Group definition) | "We have reviewed the accompanying Statement of Consolidated Unaudited Financial Results... Parent and its subsidiaries" | — |
| 2 | 349-354 | Para 2 (management responsibility / Ind AS 34 basis) | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's Board" | — |
| 3 | 356-368 | Para 3 (SRE 2410 basis, scope limitation, no audit opinion) | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410" | — |
| 4 | 370 | Para 4 (entity list reference) | "The Statement includes the results of the entities listed in Annexure A." | — |
| 5 | 372-379 | Para 5 (conclusion — unmodified) | "Based on our review conducted and procedures performed... nothing has come to our attention that causes us to believe" | — |
| 6 | 393-403 | Para 6 (Other Matter — Trust carve-out, same as standalone para 5; total revenue NIL, net loss Rs 0.004 mn) | "We did not review the interim financial results of RateGain Employees Benefit Trust... whose interim financial results reflect total revenue of Rs NIL" | — |

Opinion type: unmodified review conclusion. No Emphasis of Matter. One Other Matter paragraph (para 6, Trust carve-out). No Going Concern paragraph. Entity list: Annexure A (18 entities, enumerated in section 6 below). Unaudited/management-furnished by this auditor: RateGain Employees Benefit Trust only (relies on other auditor).

## 6. ANNEXURE A — CONSOLIDATION ENTITY LIST (page 9, lines 427-470)

Total 18 entities: 1 parent + 16 subsidiaries + 1 trust. Cross-checked internally against consolidated Note 3 ("the Company and 16 subsidiaries") — consistent (rows 2-8 = 7 RateGain-chain subsidiaries; rows 10-18 = 9 Sojern-chain subsidiaries; 7+9=16). No prior-quarter entity ledger was supplied to this run, so additions/removals cannot be asserted; renames/mergers/liquidations that are self-disclosed within this filing's own text are flagged below.

| # | Line | S.No. | Entity name | Relationship | Flags |
|---|------|-------|-------------|--------------|-------|
| 1 | 432 | 1 | RateGain Travel Technologies Limited | Parent | — |
| 2 | 433-434 | 2 | RateGain Technologies Limited | Wholly Owned Subsidiary of Parent | — |
| 3 | 435-436 | 3 | RateGain Technologies Inc. | WOS of RateGain Technologies Limited | — |
| 4 | 437-438 | 4 | RateGain Germany GmbH (Formerly Known As MyHotelShop GmbH) | WOS of RateGain Technologies Limited | ENTITY_CHANGE — renamed from MyHotelShop GmbH; self-disclosed in-document, no prior ledger to cross-check timing |
| 5 | 439-440 | 5 | RateGain Technologies Spain, S.L. | WOS of RateGain Technologies Limited | — |
| 6 | 441-442 | 6 | RateGain Technologies LLC | WOS of RateGain Technologies Limited | — |
| 7 | 443-445 | 7 | RateGain Adara Inc. (BCV Social LLC merged into RateGain Adara Inc. w.e.f. April 1 2025) | WOS of RateGain Technologies Inc. | ENTITY_CHANGE — merger of BCV Social LLC into this entity noted in-document; effective date pre-dates this quarter |
| 8 | 446-447 | 8 | RateGain Adara Japan GK | WOS of Sojern Inc. | — |
| 9 | 448-450 | 9 | RateGain Employees Benefit Trust | Trust (included in standalone results of Parent) | — |
| 10 | 451-452 | 10 | Sojern Inc. # | WOS of RateGain Technologies Limited | — |
| 11 | 453-454 | 11 | Sojern Limited # | WOS of Sojern Inc. | — |
| 12 | 455-456 | 12 | Sojern Mexico S. De R.L. De Cv # | WOS of Sojern Inc. | — |
| 13 | 457-458 | 13 | Sojern Intl Ltd. # | WOS of Sojern Inc. | — |
| 14 | 459-460 | 14 | Sojern Asia Pte. Ltd. # | WOS of Sojern Inc. | — |
| 15 | 461-462 | 15 | Sojern MENA FZCO # (Formerly Known As Sojern MENA DMCC) | WOS of Sojern Inc. | ENTITY_CHANGE — renamed from Sojern MENA DMCC; self-disclosed in-document |
| 16 | 463-464 | 16 | Sojern Hong Kong Limited # (Liquidated w.e.f. July 10 2026) | WOS of Sojern Inc. | ENTITY_CHANGE — liquidated subsequent to quarter-end (30 June 2026); cross-referenced at consolidated Note 12 (line 660-661) as a subsequent event |
| 17 | 465-466 | 17 | Sojern Germany GmbH # | WOS of Sojern Inc. | — |
| 18 | 467-468 | 18 | Nrejos SARL # | WOS of Sojern Inc. | — |

Footnote (line 470): "# Refer Note 5 of the Notes to Consolidated Unaudited Financial Results" — all Sojern-chain entities (rows 10-18) are footnoted to consolidated Note 5, the Sojern acquisition note. Enumerated as footnote row: line 470, applies to S.No. 10-18.

## 7. STANDALONE STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (page 4, lines 179-227)

Columns: Q1 FY27 (30 Jun 2026, Unaudited) | Q4 FY26 (31 Mar 2026, Unaudited, Refer Note 3) | Q1 FY26 (30 Jun 2025, Unaudited) | FY26 (31 Mar 2026, Audited)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 189 | Revenue from operations | 681.89 | 637.81 | 588.58 | 2,488.13 | — |
| 2 | 190 | Other income | 21.60 | 58.15 | 188.08 | 443.91 | — |
| 3 | 191 | Total income | 703.49 | 695.96 | 776.66 | 2,932.04 | — |
| 4 | 194 | Employee benefits expense | 518.88 | 429.70 | 436.78 | 1,768.31 | — |
| 5 | 195 | Finance costs | 2.27 | 2.32 | 2.61 | 9.94 | — |
| 6 | 196 | Depreciation and amortisation expenses | 12.69 | 11.74 | 11.33 | 46.90 | — |
| 7 | 197 | Other expenses | 112.88 | 100.30 | 84.45 | 377.41 | — |
| 8 | 198 | Total expenses | 646.72 | 544.06 | 535.17 | 2,202.56 | — |
| 9 | 200 | Profit before exceptional items and tax | 56.77 | 151.90 | 241.49 | 729.48 | — |
| 10 | 201 | Exceptional items (Refer Note 9) | - | - | - | 47.94 | ZERO_STANDING — nil in all three quarterly columns; only the audited annual column carries a value |
| 11 | 203 | Profit before tax | 56.77 | 151.90 | 241.49 | 681.54 | — |
| 12 | 205 | Current tax | 17.36 | 45.35 | 64.47 | 194.26 | — |
| 13 | 206 | Deferred tax credit | (2.68) | (10.70) | (3.53) | (16.13) | — |
| 14 | 207 | Total tax expense | 14.68 | 34.65 | 60.94 | 178.13 | — |
| 15 | 209 | Profit after tax | 42.09 | 117.25 | 180.55 | 503.41 | — |
| 16 | 212 | Remeasurement of net defined benefit plan | 2.23 | (2.90) | (1.37) | 8.92 | — |
| 17 | 213 | Income tax relating to the above item | (0.56) | 0.73 | 0.34 | (2.24) | — |
| 18 | 214 | Total OCI (net of tax) | 1.67 | (2.17) | (1.03) | 6.68 | — |
| 19 | 216 | Total comprehensive income (net of tax) | 43.76 | 115.08 | 179.52 | 510.09 | — |
| 20 | 218 | Paid-up share capital | 118.36 | 118.10 | 118.01 | 118.10 | — |
| 21 | 219 | Other equity | blank | blank | blank | 14,148.01 | ZERO_STANDING — dash/blank in all three quarterly columns; standard annual-only presentation line |
| 22 | 221 | Basic EPS (Rs, Refer Note 10) | 0.36 | 0.99 | 1.53 | 4.27 | — |
| 23 | 222 | Diluted EPS (Rs) | 0.36 | 0.99 | 1.53 | 4.26 | — |
| 24 | 224 | Face value per share (Rs) | 1.00 | 1.00 | 1.00 | 1.00 | — |

## 8. CONSOLIDATED STATEMENT OF UNAUDITED FINANCIAL RESULTS — LINE ITEMS (page 10, lines 484-554)

Columns: Q1 FY27 (30 Jun 2026, Unaudited) | Q4 FY26 (31 Mar 2026, Unaudited, Refer Note 4) | Q1 FY26 (30 Jun 2025, Unaudited) | FY26 (31 Mar 2026, Audited)

| # | Line | Line item | Q1FY27 | Q4FY26 | Q1FY26 | FY26 | Flags |
|---|------|-----------|--------|--------|--------|------|-------|
| 1 | 493 | Revenue from operations | 7,850.12 | 7,155.50 | 2,729.15 | 18,235.54 | — |
| 2 | 494 | Other income | 30.85 | 25.73 | 206.58 | 613.36 | — |
| 3 | 495 | Total income | 7,880.97 | 7,181.23 | 2,935.73 | 18,848.90 | — |
| 4 | 498 | Employee benefits expense | 2,947.60 | 2,694.87 | 1,091.49 | 7,116.74 | — |
| 5 | 499 | Finance costs | 165.43 | 184.38 | 2.98 | 314.99 | — |
| 6 | 500 | Depreciation and amortisation expenses | 375.18 | 349.86 | 87.00 | 807.13 | — |
| 7 | 501 | Other expenses | 3,187.21 | 2,990.31 | 1,140.99 | 7,744.26 | — |
| 8 | 502 | Total expenses | 6,675.42 | 6,219.42 | 2,322.46 | 15,983.12 | — |
| 9 | 504 | Profit before exceptional items and tax | 1,205.55 | 961.81 | 613.27 | 2,865.78 | — |
| 10 | 506 | Exceptional items (Refer Note 10) | - | - | - | 346.18 | ZERO_STANDING — nil in all three quarterly columns; only audited annual column carries a value |
| 11 | 508 | Profit before tax | 1,205.55 | 961.81 | 613.27 | 2,519.60 | — |
| 12 | 511 | Current tax | 202.38 | 134.28 | 143.02 | 569.80 | — |
| 13 | 512 | Deferred tax charge | 54.07 | 127.64 | 0.93 | 5.93 | — |
| 14 | 513 | Total tax expense | 256.45 | 261.92 | 143.95 | 575.73 | — |
| 15 | 515 | Profit after tax | 949.10 | 699.89 | 469.32 | 1,943.87 | — |
| 16 | 519 | Remeasurement of net defined benefit plan | 2.23 | (2.90) | (1.37) | 8.92 | — |
| 17 | 520 | Income tax relating to the above item | (0.56) | 0.73 | 0.34 | (2.24) | — |
| 18 | 521 | Sub-total (i) | 1.67 | (2.17) | (1.03) | 6.68 | — |
| 19 | 524 | Exchange differences on translation of foreign operations | 116.17 | 745.66 | 113.64 | 1,245.83 | — |
| 20 | 525 | Sub-total (ii) | 116.17 | 745.66 | 113.64 | 1,245.83 | — |
| 21 | 527 | Total OCI (net of tax) (i+ii) | 117.84 | 743.49 | 112.61 | 1,252.51 | — |
| 22 | 530 | Total comprehensive income (net of tax) | 1,066.94 | 1,443.38 | 581.93 | 3,196.38 | — |
| 23 | 534 | PAT attributable to: Owners of the Company | 949.10 | 699.89 | 469.32 | 1,943.87 | — |
| 24 | 535 | PAT attributable to: Non-controlling interest | - | - | - | - | ZERO_STANDING — nil in all four columns every period; template line for a minority-interest structure the Group does not currently have (all subsidiaries wholly owned) |
| 25 | 538 | OCI attributable to: Owners of the Company | 117.84 | 743.49 | 112.61 | 1,252.51 | — |
| 26 | 539 | OCI attributable to: Non-controlling interest | - | - | - | - | ZERO_STANDING — nil in all four columns every period |
| 27 | 542 | TCI attributable to: Owners of the Company | 1,066.94 | 1,443.38 | 581.93 | 3,196.38 | — |
| 28 | 543 | TCI attributable to: Non-controlling interest | - | - | - | - | ZERO_STANDING — nil in all four columns every period |
| 29 | 545 | Paid-up share capital | 118.36 | 118.10 | 118.01 | 118.10 | — |
| 30 | 546 | Other equity | blank | blank | blank | 19,940.45 | ZERO_STANDING — dash/blank in all three quarterly columns; annual-only presentation line |
| 31 | 549 | Basic EPS (Rs, Refer Note 11) | 8.03 | 5.93 | 3.98 | 16.47 | — |
| 32 | 550 | Diluted EPS (Rs) | 8.02 | 5.91 | 3.98 | 16.43 | — |
| 33 | 551 | Face value per share (Rs) | 1.00 | 1.00 | 1.00 | 1.00 | — |

## 9. CONSOLIDATED NOTE 5 — PURCHASE PRICE ALLOCATION (PPA) TABLE, SOJERN ACQUISITION (page 11, lines 596-609)

| # | Line | Particular | Amount (Rs million) | Amount (USD million) | Flags |
|---|------|------------|----------------------|------------------------|-------|
| 1 | 598 | Purchase consideration | 22,220.83 | 250.92 | — |
| 2 | 602 | Intangible assets recognised — Customer relationships | 3,827.18 | 43.22 | — |
| 3 | 603 | Intangible assets recognised — Trademarks | 887.37 | 10.02 | — |
| 4 | 604 | Intangible assets recognised — Softwares | 1,875.88 | 21.18 | — |
| 5 | 605 | Other identified assets (net of liabilities) | 3,918.28 | 44.25 | — |
| 6 | 607 | Add: Deferred tax liability on intangible assets recognised | 1,307.89 | 14.77 | — |
| 7 | 609 | Goodwill | 13,020.01 | 147.02 | — |

Useful lives disclosed (line 612-613, same row as goodwill note, not a separate table row but recorded here): customer relationships 7 years, trademarks 7 years, softwares 6 years.

## 10. NOTES TO STANDALONE UNAUDITED FINANCIAL RESULTS (pages 5-6, lines 234-318)

| # | Line | Note | First ~15 words | Flags |
|---|------|------|-------------------|-------|
| 1 | 234-238 | Note 1 | "These standalone unaudited financial results for the quarter ended 30 June 2026 have been prepared in accordance with Ind AS 34" | — |
| 2 | 240-247 | Note 2 | "In terms of Regulation 33... reviewed and recommended for approval by the Audit Committee and approved by the Board on 6 August 2026" | — |
| 3 | 250-253 | Note 3 | "The figures for the quarter ended 31 March 2026... are the balancing figures between audited full-year and published nine-month figures" | — |
| 4 | 256-264 | Note 4 | "On 06 November 2025, the Company, through its wholly owned subsidiary, has completed acquisition of 100% equity shares of Sojern Inc." — consideration Rs 22,220.83 mn (USD 250.92 mn); working capital adjustment finalised, reducing consideration/goodwill by Rs 6.36 mn (USD 0.07 mn); transaction costs Rs 25.92 mn disclosed as exceptional items | — |
| 5 | 267-268 | Note 5 | "The Company's business activity falls within a single segment... hospitality and travel industry... in terms of Ind AS 108" | OCR_ANOMALY — leading digit "5" rendered as "s" in extract (see reconciliation log) |
| 6 | 271-277 | Note 6 | "During the quarter ended 30 June 2026, 493,689 Employee Stock Options... exercised... 260,133 equity shares issued on 18 June 2026; 37,453 shares issued 28 July 2026 (post quarter-end)" | — |
| 7 | 280-281 | Note 7 | "The paid up share capital of the Company excludes 67,631 (31 March 2026: 67,631) equity shares held by the ESOP Trust" | ZERO_STANDING (constant across periods — same 67,631 figure both current and comparative) |
| 8 | 289-299 | Note 8 | "On 21 November 2025, Government of India notified provisions of the Code on Wages, 2019... Labour Codes... increase in gratuity/leave liability of Rs 22.02 million recognised as exceptional item in FY26" | — |
| 9 | 302-308 | Note 9 | "During the year ended 31 March 2026, the Company has recognised certain non-recurring expenses, disclosed as exceptional items" — breakdown: (a) Sojern acquisition costs Rs 25.92 mn, (b) Labour Code gratuity/leave impact Rs 22.02 mn | — |
| 10 | 311-312 | Note 10 | "Earnings per equity share for the quarters ended 30 June 2026, 31 March 2026 and 30 June 2025 have not been annualised" | — |

Signature line (not a numbered note): line 317-318, "Date: 06 August 2026 / Place: Noida — Chairman and Managing Director" — see Signature Blocks section 3, row 3.

## 11. NOTES TO CONSOLIDATED UNAUDITED FINANCIAL RESULTS (pages 11-12, lines 561-661)

| # | Line | Note | First ~15 words | Flags |
|---|------|------|-------------------|-------|
| 1 | 561-565 | Note 1 | "These consolidated unaudited financial results for the quarter ended 30 June 2026 have been prepared in accordance with Ind AS 34" | — |
| 2 | 567-574 | Note 2 | "In terms of Regulation 33... reviewed and recommended for approval by the Audit Committee and approved by the Board on 6 August 2026" | — |
| 3 | 577-579 | Note 3 | "The consolidated unaudited financial results include the results of the Company and 16 subsidiaries" | — |
| 4 | 582-585 | Note 4 | "The figures for the quarter ended 31 March 2026... are the balancing figures between audited full-year and published nine-month figures" | — |
| 5 | 588-618 | Note 5 | "On 06 November 2025, the Company has completed acquisition of 100% equity shares of Sojern Inc." — consideration Rs 22,220.83 mn (USD 250.92 mn); includes embedded PPA table (see section 9); goodwill Rs 13,020.01 mn; transaction costs Rs 324.16 mn disclosed as exceptional items; results consolidated from acquisition date — quarter not comparable to prior periods | — |
| 6 | 625-626 | Note 6 | "The Group's business activity falls within a single segment... hospitality and travel industry... in terms of Ind AS 108" | — |
| 7 | 629-634 | Note 7 | "During the quarter ended 30 June 2026, 493,689 Employee Stock Options... exercised... 260,133 shares issued 18 June 2026; 37,453 shares issued 28 July 2026 (post quarter-end)" | — |
| 8 | 636-637 | Note 8 | "The paid up share capital of the Company excludes 67,631 (31 March 2026: 67,631) equity shares held by the ESOP Trust" | ZERO_STANDING (constant across periods) |
| 9 | 640-649 | Note 9 | "On 21 November 2025, Government of India notified provisions of the Code on Wages, 2019... Labour Codes... increase in gratuity/leave liability of Rs 22.02 million" | — |
| 10 | 651-655 | Note 10 | "During the year ended 31 March 2026, the Group has recognised certain non-recurring expenses" — breakdown: (a) Sojern acquisition costs Rs 324.16 mn, (b) Labour Code impact Rs 22.02 mn | — |
| 11 | 658 | Note 11 | "Earnings per equity share for the quarters ended 30 June 2026, 31 March 2026 and 30 June 2025 have not been annualised" | — |
| 12 | 660-661 | Note 12 | "Subsequent to quarter ended 30 June 2026, Sojern Hong Kong Limited, a wholly-owned subsidiary of Sojern Inc., has been liquidated w.e.f. 10 July 2026" | ENTITY_CHANGE — cross-referenced to Annexure A row 16 (section 6 above); subsequent event, post quarter-end |

Signature block (not a numbered note): lines 665-674 — see Signature Blocks section 3, row 5.

## 12. MATERIAL DISCREPANCY BETWEEN STANDALONE AND CONSOLIDATED SOJERN COST DISCLOSURES (cross-table observation, not a new enumeration unit — flagged for A3/A4 attention)

Standalone Note 4/9 (lines 258-264, 306-307) discloses Sojern transaction/incidental costs of Rs 25.92 million as the standalone-level exceptional item. Consolidated Note 5/10 (lines 614, 654) discloses the same category of cost at Rs 324.16 million at the Group level. Both figures are present verbatim in the extract at the line numbers cited; this is a standalone-vs-consolidated scope difference (deal costs incurred at subsidiary/Group level vs. parent standalone level), not a count-test item, but it is recorded here so A3/A4 do not read it as an inconsistency to chase — the two ledger rows above (Note 4/Note 9 standalone; Note 5/Note 10 consolidated) already carry both values with their own line numbers.

---

## SUMMARY COUNTS

- Board Outcome agenda items (triggered): 2 (line 31, line 40)
- Board Outcome standing agenda categories (ZERO_STANDING, not triggered): 8
- Annexure B disclosure table rows: 4
- Signature/date blocks: 5
- Auditor report paragraphs — standalone: 5
- Auditor report paragraphs — consolidated: 6
- Consolidation entity list (Annexure A): 18 (4 flagged ENTITY_CHANGE)
- Standalone P&L line items: 24 (2 ZERO_STANDING)
- Consolidated P&L line items: 33 (5 ZERO_STANDING)
- Consolidated Note 5 PPA table rows: 7
- Standalone notes: 10 (1 OCR_ANOMALY)
- Consolidated notes: 12 (1 ENTITY_CHANGE cross-reference)
- Total numbered notes (standalone + consolidated): 22
- Total financial-table line items (standalone P&L + consolidated P&L + PPA table): 64
- Total ZERO_STANDING flags: 7 (2 standalone P&L + 5 consolidated P&L)
- Total ENTITY_CHANGE flags: 4 (Annexure A rows 4, 7, 15, 16)
- Total OCR_ANOMALY flags: 4 (standalone Note 5 digit; Annexure A whitespace drift rows 3-9; standalone UDIN; consolidated UDIN; consolidated CMD signature block — see individual rows)

```yaml
stage: A2-enumerator
company: "RATEGAIN"
quarter: "Q1 FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "/home/user/inflection-pipeline/runs/rategain-q1fy27/work/ledger_results_rategain_q1fy27.md"
counts:
  notes: 22
  line_items: 64
  zero_standing: 7
  agenda_items: 6
  auditor_paras: 11
  entities: 18
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, ENTITY_CHANGE, OCR_ANOMALY]
gate_a2: pass
mismatch_note: "Two initial grep passes undercounted (notes_standalone 9 vs sweep 10; entities_annexureA 11 vs sweep 18), both traced to OCR/whitespace extraction artifacts, not missing disclosures. Re-swept with tolerant patterns; final grep and sweep counts match on all categories. Full reconciliation log in ledger body."
```
