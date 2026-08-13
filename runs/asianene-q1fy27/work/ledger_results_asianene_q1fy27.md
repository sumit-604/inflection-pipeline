# A2 ENUMERATION LEDGER — ASIANENE Q1 FY27 — Results Filing (Reg 33)

Source: `extract_results_asianene_q1fy27.txt` (A1 extract; unit convention Lakhs,
x0.01 to Rs Cr; line numbers below are the extract's own embedded line numbers,
column 1 of each source row, range 1-642). Prior-quarter ledger: NONE (first
quarterly review for this ticker) — ENTITY_CHANGE and DROPPED-item diffs are
not applicable this run; noted as N/A (no prior baseline) wherever relevant.

```
=== A2 COUNT TEST ===
category: notes_numbered          grep_count: 16  sweep_count: 17  match: yes (reconciled)
category: footnotes_unnumbered    grep_count: 2   sweep_count: 2   match: yes
category: segment_notes_roman     grep_count: 4   sweep_count: 4   match: yes
category: line_items_consol_pl    grep_count: 35  sweep_count: 36  match: yes (reconciled)
category: line_items_consol_seg   grep_count: 14  sweep_count: 14  match: yes
category: line_items_consol_note6 grep_count: 6   sweep_count: 6   match: yes
category: line_items_stand_pl     grep_count: 26  sweep_count: 28  match: yes (reconciled)
category: line_items_stand_note4  grep_count: 6   sweep_count: 6   match: yes
category: agenda_items            grep_count: 1   sweep_count: 1   match: yes
category: auditor_paras_consol    grep_count: 8   sweep_count: 8   match: yes
category: auditor_paras_stand     grep_count: 5   sweep_count: 5   match: yes
category: entities                grep_count: 31  sweep_count: 31  match: yes
category: signature_blocks        grep_count: 4   sweep_count: 5   match: yes (reconciled)
gate_a2: pass
=== END COUNT TEST ===
```

## Reconciliation notes (mismatches found and resolved before emission)

1. **notes_numbered**: naive `^\s*[0-9]+\.\s` grep on the standalone notes
   block returned 7 (notes 1-4, 6-8); it missed note 5 because OCR rendered
   the leading digit "5" as the letter "S" ("S Putsuant to the directions
   issued by Hon'ble National Company Law Tribunal...", line 599). Manual
   sweep caught note 5 by content continuity (identical NCLT-merger paragraph
   appears as numbered note 5 in the consolidated notes block, line 362).
   Re-ran grep tolerant of `[0-9S]` — 8/8 for standalone, 9/9 for
   consolidated, total 17/17. Match confirmed after re-sweep.
2. **line_items_consol_pl**: value-row grep (rows with 2+ numeric/dash
   tokens after stripping the line-number prefix) found 35 of 36 rows. It
   missed line 295 "13 Other equity" — this row is entirely BLANK (not even
   a dash placeholder) in all three interim columns, only the Year Ended
   column is populated (44,923.55). Caught on manual sweep; flagged
   `ZERO_STANDING`.
3. **line_items_stand_pl**: same grep methodology found 26 of 28 rows. It
   missed line 556 "Changes in fair value of investments through OCI"
   (blank in both quarter columns, populated only in 31-Mar-2026 columns)
   and line 565 "11 Other equity" (blank in all interim columns, same
   pattern as item 2 above). Both caught on manual sweep; both flagged
   `ZERO_STANDING`.
4. **signature_blocks**: grep on "Managing Director" (case-insensitive)
   found only 1 of the 2 MD signature blocks — OCR rendered the second
   instance as "Managillg Din1ctor" (line 638), which the literal string
   search missed. Manual sweep, cross-checked against the repeated
   "DIN: 01360843" string (2 hits, lines 415 and 639), confirmed 2 MD
   signature blocks (one per statement: consolidated, standalone), for a
   total of 5 signature blocks including the CS digital signature and the
   two auditor partner signatures. Match confirmed after re-sweep.

---

## 1. BOARD OUTCOME LETTER (Reg 30/33 covering letter, page 1)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1 | Agenda item — results approval | 24-27 | Board approved and took on record un-audited standalone and consolidated financial results for quarter ended 30 June 2026, along with Limited Review Report | ONLY agenda item disclosed in this letter |
| 2 | Board meeting start time | 33 | Commenced 3:15 p.m. | |
| 3 | Board meeting end time | 33-34 | Concluded 4:04 p.m. (49-minute meeting) | |
| 4 | Filing addressees | 8-14 | BSE Limited (Scrip 530355) and NSE (Trading Symbol ASIANENE), both listing departments | |
| 5 | Digital signature block — CS | 43-54 | Shweta Vaibhav Jain, Company Secretary & Compliance Officer, Membership No. 23368; digitally signed 2026.08.13 18:05:32 +05'30' | Timestamp (18:05:32) is AFTER meeting conclusion (16:04) — normal, no flag |

No other agenda items (AR approval, AGM notice, record date, dividend,
director appointment/resignation, auditor change, scrutinizer, ESOP grant
board approval, capital-raising enabling resolution) appear anywhere in this
letter or elsewhere in the filing — confirmed via targeted keyword sweep
(dividend/AGM/record date/scrutinizer/director appoint/auditor appoint/
capital rais/resignation: zero hits in the full extract). This is a
single-item, 49-minute results-only board outcome letter.

---

## 2. CONSOLIDATED AUDITOR'S LIMITED REVIEW REPORT (SGCO & Co. LLP, pages 2-3)

Opinion type: **Review conclusion (unmodified)** — not an audit opinion (SRE 2410).

| Para | Line(s) | First 15 words / content | Flags |
|------|---------|---------------------------|-------|
| 1 | 79-83 | "We have reviewed the accompanying Statement of Unaudited Consolidated Financial Results of Asian Energy Services..." — scope statement | |
| 2 | 85-89 | "This Statement, which is the responsibility of the Parent's management and approved by the Parent's Board..." — management responsibility | |
| 3 | 91-100 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." — review standard, scope, SEBI Reg 33(8) circular procedures | |
| 4 | 102-108 | "Based on our review conducted and procedures performed as stated in paragraph 4 above..." — unmodified conclusion | Internal cross-reference error: refers to "paragraph 4 above" for procedures actually stated in para 3 |
| 5 | 112-118 | "We did not review the interim financial statements of one (1) subsidiary..." — 1 subsidiary reviewed by OTHER auditor, furnished by management; Rs Nil revenue, Rs (325.51) Lakhs net loss, Rs (325.51) Lakhs TCI for the quarter | Entity unaudited by principal auditor |
| 6 | 135-144 | "The Statement includes the interim financial information of twenty-one (21) subsidiaries/step down subsidiaries, which has not been reviewed..." — 21 subs (unreviewed, Rs 1,899.83 Lakhs revenue, Rs 145.19 Lakhs PAT) + 5 JVs (unreviewed, Rs 78.85 Lakhs share of profit) — management states not material to Group | 26 entities described here as unreviewed/management-furnished |
| 7 | 146-154 | "Further, out of above mentioned in para 5 and 6, eighteen (18) subsidiaries/step down subsidiaries are located outside India..." — foreign GAAP conversion adjustments reviewed by principal auditor | 18 of the 22 entities in paras 5+6 are foreign |
| — | 156 | "Our conclusion is not modified in respect of these matters." | |
| OM(a) | 158-164 | "Other Matters — The Statement includes comparative figures of the company for the quarter ended 30th June 2025, which have been reviewed by the predecessor auditor M/s Walker Chandiok and Co LLP..." — predecessor auditor unmodified conclusion dated 12 Aug 2025 | Auditor change from Walker Chandiok to SGCO between the comparative and current quarter |
| Sig | 168-180 | For SGCO & Co. LLP, Chartered Accountants, Firm Reg. No. 112081W/W100184; Partner "Suresh [surname illegible — OCR corrupted]"; Mem. No. 044739; UDIN: 26044739XCBNDT1023; Place: Mumbai; Date: 13 August 2026 | Partner surname not legible in extract; no Emphasis of Matter paragraph present; no Going Concern paragraph present (both confirmed absent by sweep) |

**Entity count cross-check:** paras 5+6 name 1 + 21 = 22 subsidiaries as
unreviewed/other-auditor-reviewed, plus 5 JVs unreviewed = 27 entities
accounted for in the review-basis paragraphs. Annexure 1 (below) lists 26
subsidiaries + 5 JVs = 31 entities total. 26 - 22 = 4 subsidiaries in the
Annexure are not explicitly placed into a reviewed/unreviewed bucket by
paras 5-7. Flag: `ENTITY_COUNT_UNRECONCILED` (worth A3/A4 follow-up; not a
mechanical failure, no prior ledger exists to confirm this is new or
carried-forward).

---

## 3. ANNEXURE 1 — CONSOLIDATION ENTITY LIST (page 4)

Prior-quarter ledger: NONE — `ENTITY_CHANGE` diff not applicable this run.

### 3a. Subsidiaries / step-down subsidiaries (26), lines 194-219

| # | Line | Entity | Jurisdiction |
|---|------|--------|--------------|
| 1 | 194 | Asian Oilfield and Energy Services DMCC | Dubai |
| 2 | 195 | AOSL Energy Services Limited | (not stated) |
| 3 | 196 | Cure Multi Trade Private Limited | (not stated) |
| 4 | 197 | Ivorene Oil Services Nigeria Limited | Nigeria |
| 5 | 198 | Optimum Oil and Gas Private Limited | (not stated) |
| 6 | 199 | AOSL Petroleum Pte Limited (OCR: "PIE") | Singapore |
| 7 | 200 | Kuiper Group Limited | Cayman |
| 8 | 201 | OCB Oilfield Services DMCC | Dubai |
| 9 | 202 | Global Resources Management Employment Services LLC | UAE |
| 10 | 203 | Kuiper Triangle | Dubai |
| 11 | 204 | Nexus People Management | KSA |
| 12 | 205 | Maaber for Logistics Services | Qatar |
| 13 | 206 | Offshore International Management (India) Private Limited | India |
| 14 | 207 | Kuiper International Pte Ltd. | Singapore |
| 15 | 208 | Kuiper Malaysia Sdn. Bhd | Malaysia |
| 16 | 209 | OCB Oilfield Services (B) Sdn Bhd | Brunei |
| 17 | 210 | PT Oilfield Crew Management Ltd | Indonesia |
| 18 | 211 | Nexus People Management Ltd | Thailand |
| 19 | 212 | OCB Oilfield Services Limited | Thailand |
| 20 | 213 | Kuiper Triangle Egypt | Egypt |
| 21 | 214 | Kuiper Labour Supply Services Namibia (Pty) Ltd | Namibia |
| 22 | 215 | Kuiper HR Management and Consultancy WLL | Qatar |
| 23 | 216 | Kuiper Malaysia Manpower Services Sdn. Bhd | Malaysia |
| 24 | 217 | Kuiper Triangle Cyprus Limited (OCR: "Cyrus") | Cyprus |
| 25 | 218 | Kuiper Holdings Limited | Dubai |
| 26 | 219 | Maaber for Logistics Services Oman Operations | Oman |

### 3b. Joint Ventures (5), lines 224-228

| # | Line | Entity |
|---|------|--------|
| 1 | 224 | Zuberi-Asian Joint Venture |
| 2 | 225 | AESL FFIL Joint Venture |
| 3 | 226 | Asian Indwell Joint Venture |
| 4 | 227 | Asian Oilmax Joint Venture |
| 5 | 228 | Asian Global Joint Venture |

Total entities enumerated: 31.

---

## 4. CONSOLIDATED FINANCIAL STATEMENTS — STATEMENT OF P&L (page 5)

Columns: Q ended 30-Jun-2026 (Unaudited, current) / 31-Mar-2026 (Audited) /
30-Jun-2025 (Unaudited, comparator) / FY ended 31-Mar-2026 (Audited).

| Line | Item | Current-Qtr value | Flags |
|------|------|--------------------|-------|
| 244 | 1. Income (header) | — | structural header |
| 245 | (a) Revenue from operations | 27,118.53 | |
| 246 | (b) Other income | 331.93 | |
| 247 | Total income (a+b) | 27,450.46 | |
| 249 | 2. Expenses (header) | — | structural header |
| 250 | (a) Project related expense (Refer Note 6) | 21,892.76 | |
| 251 | (b) Changes in inventories of finished goods | 17.04 | |
| 252 | (c) Employee benefit expense (Refer Note 6) | 1,838.00 | |
| 253 | (d) Finance costs | 376.38 | |
| 254 | (e) Depreciation, depletion and amortisation expense | 438.22 | |
| 255 | (f) Other expenses (Refer Note 3) | 1,256.06 | |
| 256 | Total expenses (a+b+c+d+e+f) | 25,818.46 | |
| 258 | 3. Profit before share of profit of JVs and tax (1-2) | 1,632.00 | |
| 259 | 4. Share of profit from joint ventures | 78.85 | |
| 260 | 5. Profit before exceptional items and tax (3+4) | 1,710.85 | |
| 261 | 6. Exceptional items — net loss (Refer note 8) | nil (dash) | **ZERO_STANDING** — nil in current qtr and 30-Jun-2025 comparator, populated only in 31-Mar columns |
| 262 | 7. Profit before tax (5+6) | 1,710.85 | |
| 263 | 8. Tax expense/(credit) (header) | — | structural header |
| 264 | (a) Current tax: (sub-header) | — | structural header |
| 265 | — current period | 396.39 | |
| 266 | — earlier period | nil (dash) | **ZERO_STANDING** — nil in current qtr and 30-Jun-2025 comparator |
| 267 | (b) Deferred tax charge/(credit) | 33.81 | |
| 268 | Total tax expense/(credit) (a+b) | 435.20 | |
| 269 | 9. Net profit after tax for the period (7-8) | 1,275.65 | |
| 270 | 10. Other comprehensive income/(loss) (header) | — | structural header |
| 271 | (a) Items not to be reclassified... (sub-header) | — | structural header |
| 272 | — Remeasurement gain/(loss) of defined benefit liability | (3.50) | |
| 273 | — Changes in fair value of investments through OCI | nil (dash) | **ZERO_STANDING** — nil in current qtr and 30-Jun-2025 |
| 274 | — Income tax relating to items not reclassified | nil (dash) | **ZERO_STANDING** — nil in current qtr and 30-Jun-2025 |
| 275 | (b) Items to be reclassified... (sub-header) | — | structural header |
| 276 | — Exchange differences on translation of foreign operations | (9.25) | |
| 277 | Total OCI for the period, net of tax (a+b) | (12.75) | |
| 279 | 11. Total comprehensive income for the period (9+10) | 1,262.90 | |
| 281 | Net profit after tax attributable to: (sub-header) | — | structural header |
| 282 | — Owners of the Holding Company | 1,196.06 | |
| 283 | — Non-controlling interest | 79.60 | |
| 285 | OCI attributable to: (sub-header) | — | structural header |
| 286 | — Owners of the Holding Company | (12.75) | |
| 287-288 | — Non-controlling interest | nil (dash), all 4 periods | **ZERO_STANDING** — nil in ALL periods, canonical zero-standing case (OCI has no NCI allocation any period shown) |
| 289 | Total comprehensive income attributable to: (sub-header) | — | structural header |
| 290 | — Owners of the Holding Company | 1,183.31 | |
| 291 | — Non-controlling interest | 79.60 | |
| 293 | 12. Paid up equity share capital (FV Rs 10) | 4,862.90 | |
| 295 | 13. Other equity | blank in interim cols | **ZERO_STANDING** — populated only in Year Ended column (44,923.55); blank (not even a dash) in all three interim columns — this is the exact SOUTHWEST-pattern miss risk (line exists, quarter cells silently blank) |
| 297-298 | 14. EPS attributable to owners (FV Rs 10) [marker "A"] | — | header + footnote marker |
| 299 | (a) Basic (in INR) | 2.53 | |
| 300 | (b) Diluted (in INR) | 2.49 (OCR: "249") | |
| 301 | Footnote: "(Quarterly figures are not annualised)" | — | unnumbered footnote tied to EPS marker |

Consolidated P&L: 36 value-bearing line items enumerated (6 flagged
ZERO_STANDING), plus 9 structural header/sub-header rows and 1 footnote.

---

## 5. CONSOLIDATED SEGMENT INFORMATION (page 6)

| Line | Item | Current-Qtr value | Flags |
|------|------|--------------------|-------|
| 310 | I. Segment Revenue (header) | — | structural header |
| 311 | a) Oil and gas | 24,477.59 | |
| 312 | b) Mineral and other energy services | 2,640.94 | |
| 313 | Total revenue from operations | 27,118.53 | |
| 315 | II. Segment Results (header) | — | structural header |
| 316 | a) Oil and gas | 3,329.93 | |
| 317 | b) Mineral and other energy services | 406.97 | |
| 318 | Total segment results | 3,736.90 | |
| 320 | Less: Depreciation, depletion and amortisation expense | 438.22 | |
| 321 | Add: Other income | 331.93 | |
| 322 | Less: Finance costs | 376.38 | |
| 323 | Less: Other unallocable expenses | 1,622.23 | |
| 324 | Less: Exceptional items | nil (dash) | **ZERO_STANDING** — nil current qtr and 30-Jun-2025 comparator |
| 325 | Profit before share of profit of JVs and tax | 1,632.01 | note: differs from P&L line 258 (1,632.00) by 0.01 — rounding, not material |
| 326 | Add: Share of profit from joint ventures | 78.85 | |
| 327 | Profit before tax | 1,710.85 | |

Segment narrative notes (roman numeral, unnumbered relative to main note
series):

| Marker | Line | Content (first 15 words) |
|--------|------|---------------------------|
| I) | 330-332 | "The Group is primarily engaged into the business of providing services in energy sector..." — defines Oil & gas and Mineral/other energy segments |
| II) | 334-335 | "The Chief Operating Decision Maker (CODM) does not review assets and liabilities, depreciation..." — no asset/liability segment disclosure |
| III) | 337-338 | "Segment results represents the profit before depreciation, depletion and amortisation, finance costs and tax expense..." |
| IV) | 340 | "Employee benefit expenses and other expenses that cannot be allocated to the segments are shown as other unallocable expenses." |

Segment table: 14 line items (1 flagged ZERO_STANDING) + 4 segment notes.

---

## 6. CONSOLIDATED NOTE 6 — EMPLOYEE COST RECLASSIFICATION TABLE (lines 372-383)

| Line | Item | Current-Qtr value | Flags |
|------|------|--------------------|-------|
| 375 | Employee benefits expense (gross) | 2,601.54 | |
| 376 | Less — Employee benefits expense related to projects | 763.54 | |
| 378 | Net Employee Benefit cost | 1,838.00 | |
| 380 | Project related cost (excl. reclassified employee cost) | 21,129.22 | |
| 381 | Add — Employee benefits expense related to projects | 763.54 | |
| 383 | Total Project related cost | 21,892.76 | |

6 line items, fully populated across all periods, no zero-standing.

---

## 7. CONSOLIDATED NOTES (1-9) — page 7

| Note | Line | First 15 words |
|------|------|-----------------|
| 1 | 345 | "The above Consolidated financial results (the 'results') are prepared in accordance with the recognition..." — Ind AS basis, Audit Committee/Board approval 13 Aug 2026 |
| 2 | 350 | "The consolidated results and standalone results for the quarter ended 30 June 2026 and statutory auditor's review report..." — availability on company website |
| 3 | 353 | "Other expenses also includes the expenditure incurred towards travel and conveyance, security expenses and legal..." |
| 4 | 355-360 | "During the Previous year, The Asian Oilfield & Energy Services DMCC ('Asian DMCC'), a wholly-owned subsidiary, had entered into a Share Purchase Agreement..." — Kuiper acquisition PPA finalized in Q4 FY26, capital reserve Rs 3,996.59 Lakhs recognized |
| 5 | 362-369 | "Pursuant to the directions issued by Hon'ble National Company Law Tribunal, Mumbai Bench ('NCLT Mumbai'), vide its order dated 22nd April 2026..." — Oilmax Energy Pvt Ltd merger by absorption into AESL; NCLT admitted petition 7 Jul 2026; scheme not yet effective, no accounting impact given | Pending scheme — watch item |
| 6 | 370-383 | "During the previous year, the management has reclassified employee costs related to projects from Employee Benefit Expenses..." — reclassification table (see section 6 above) |
| 7 | 386-397 | "During the Quarter the Company has granted 1,77,000 stock options to employees of the Company and 17,000 stock options were allotted..." — ESOP grant (Asian ESOP Scheme 2025/2024, grant date 19 May 2026, ESOP expense Rs 0.58 Cr); SAME NOTE continues with unnumbered paragraph — 47,00,000 convertible warrants allotted 5 Nov 2024, 10,37,298 warrants lapsed 5 May 2026 (upfront Rs 868.74 Lakhs forfeited), 36,62,702 shares approved for allotment on conversion of the remainder via 5 May 2026 circular resolution | Two distinct corporate actions (ESOP grant + warrant lapse/forfeiture) bundled under one note number |
| 8 | 398-402 | "a. Exceptional items in quarter and year ended 31 March 2026 represent amount written of Rs 271.82 lakhs pursuant to..." — Outside Expert Council recommendation, contractual dispute; sub-item (b) — subsidiary one-time acquisition costs Rs 669 Lakhs (Kuiper) |
| 9 | 403-405 | "Figures for the quarters ended 31 March 2026 are the balancing figures between the audited figures for the full financial year..." — Q4 balancing-figure convention, regrouping disclosure |

Consolidated signature block: 409-418 — For Asian Energy Services Limited,
Kapil Garg, Managing Director, DIN: 01360843, Place: Mumbai, Date: 13 August
2026 (date only, no time stamp captured in extract).

9 numbered notes for the consolidated results.

---

## 8. STANDALONE AUDITOR'S LIMITED REVIEW REPORT (SGCO & Co. LLP, pages 8-9)

Opinion type: **Review conclusion (unmodified)**.

| Para | Line(s) | First 15 words / content | Flags |
|------|---------|---------------------------|-------|
| 1 | 434-437 | "We have reviewed the accompanying Statement of Unaudited Standalone Financial Results of Asian Energy Services..." — scope statement | |
| 2 | 440-444 | "This Statement, which is the responsibility of the Management and approved by the Company's Board of Directors..." — management responsibility | |
| 3 | 447-455 | "We conducted our review of the Statement in accordance with the Standard on Review Engagement (SRE) 2410..." — review standard, moderate assurance scope | |
| 4 | 457-462 | "Based on our review conducted as above, nothing has come to our attention that causes us to believe..." — unmodified conclusion | |
| OM(5)(a) | 478-484 | "Other Matters — The Statement includes comparative figures of the company for the Quarter ended 30th June 2025, which have been reviewed by the predecessor auditor M/s Walker Chandiok and Co LLP..." dated 12 Aug 2025, unmodified | Same predecessor-auditor transition as consolidated report |
| Sig | 489-501 | For S G C O & Co. LLP, Chartered Accountants, Firm Reg. No. 112081W/W100184; Partner (name OCR-illegible, "S~Mi"); Mem. No. 044739; UDIN: 26044739OBFLUH7225; Place: Mumbai; Date: 13 August 2026 | No Emphasis of Matter paragraph present; no Going Concern paragraph present (both confirmed absent by sweep); no subsidiary/unreviewed-entity paragraphs (expected — standalone has no consolidation scope) |

5 auditor paragraphs (4 numbered + 1 Other Matters) for the standalone report.

---

## 9. STANDALONE FINANCIAL STATEMENTS — STATEMENT OF P&L (page 10)

Columns: Q ended 30-Jun-2026 (Unaudited, current) / 31-Mar-2026 (Audited) /
30-Jun-2025 (Unaudited, comparator) / FY ended 31-Mar-2026 (Audited).

| Line | Item | Current-Qtr value | Flags |
|------|------|--------------------|-------|
| 526 | 1. Income (header) | — | structural header |
| 527 | (a) Revenue from operations | 14,927.67 | |
| 528 | (b) Other income | 245.86 | |
| 529 | Total income (a+b) | 15,173.53 | |
| 531 | 2. Expenses (header) | — | structural header |
| 532 | (a) Project related expense (Refer Note 4) | 11,335.07 | |
| 533 | (b) Changes in inventories of finished goods | 17.04 | |
| 534 | (c) Employee Benefit expenses (Refer Note 4) | 1,147.11 | |
| 535 | (d) Finance costs | 181.66 | |
| 536 | (e) Depreciation, depletion and amortisation expense | 409.53 | |
| 537 | (f) Other expenses (Refer note 3) | 799.14 | |
| 538 | Total expenses (a+b+c+d+e+f) | 13,889.55 | |
| 540 | 3. Profit before exceptional item and tax (1-2) | 1,283.98 | |
| 541 | 4. Exceptional item — loss (Refer note 7) | nil (dash) | **ZERO_STANDING** — nil current qtr and 30-Jun-2025 comparator |
| 542 | 5. Profit before tax (3+4) | 1,283.98 | |
| 543 | 6. Tax expense/(credit) (header) | — | structural header |
| 544 | (a) Current tax: (sub-header) | — | structural header |
| 545 | — current period | 286.70 | |
| 546 | — earlier period | nil (dash) | **ZERO_STANDING** — nil current qtr and 30-Jun-2025 comparator |
| 547 | (b) Deferred tax charge/(credit) | 42.00 | |
| 548 | Total tax expense/(credit) (a+b) | 328.70 | |
| 550 | 7. Net profit after tax for the period (5-6) | 955.28 | |
| 551 | 8. Other comprehensive income/(loss) (header) | — | structural header |
| 552 | (a) Items not to be reclassified... (sub-header) | — | structural header |
| 553 | — Remeasurement gain/(loss) of defined benefit liability | (3.50) | |
| 556 | — Changes in fair value of investments through OCI | nil (blank) | **ZERO_STANDING** — populated only in 31-Mar-2026 columns; blank (not dash) in both quarter columns shown |
| 557 | — Income tax relating to items not reclassified | nil (dash) | **ZERO_STANDING** — nil current qtr and 30-Jun-2025 comparator |
| 558 | (b) Items to be reclassified subsequently to P&L | nil, ALL periods | **ZERO_STANDING** — canonical all-periods-nil line, no sub-items shown at all |
| 559 | Total OCI for the period, net of tax | (3.50) | |
| 561 | 9. Total comprehensive income for the period (7+8) | 951.78 | |
| 563 | 10. Paid up equity share capital (FV Rs 10) | 4,862.90 | |
| 565 | 11. Other equity | blank in interim cols | **ZERO_STANDING** — populated only in Year Ended column (40,265.82); blank in all interim columns, same pattern as consolidated line 295 |
| 567 | 12. EPS (FV Rs 10) [marker '"'] | — | header + footnote marker |
| 568 | (a) Basic (in INR) | 2.02 | |
| 569 | (b) Diluted (in INR) | 1.99 | |
| 570 | Footnote: "(Quarterly figures are not annualised)" | — | unnumbered footnote tied to EPS marker |

Standalone P&L: 28 value-bearing line items enumerated (6 flagged
ZERO_STANDING), plus 7 structural header/sub-header rows and 1 footnote.

---

## 10. STANDALONE NOTE 4 — EMPLOYEE COST RECLASSIFICATION TABLE (lines 588-597)

| Line | Item | Current-Qtr value | Flags |
|------|------|--------------------|-------|
| 589 | Employee benefits expense (gross) | 1,910.65 | |
| 590 | Less — Employee benefits expense related to projects | 763.54 | |
| 592 | Net Employee Benefit cost | 1,147.11 | |
| 594 | Project related cost (excl. reclassified employee cost) | 10,571.53 | |
| 595 | Add — Employee benefits expense related to projects | 763.54 | |
| 597 | Total Project related cost | 11,335.07 | |

6 line items, fully populated across all periods, no zero-standing.

---

## 11. STANDALONE NOTES (1-8) — page 11

| Note | Line | First 15 words |
|------|------|-----------------|
| 1 | 574 | "The above Standalone financial results (the 'results') are prepared in accordance with the recognition..." — Ind AS basis, Audit Committee/Board approval 13 Aug 2026 |
| 2 | 579-580 | "The Company publishes standalone financial results along with the consolidated financial results. Accordingly, as per Ind AS 108..." — no segment disclosure in standalone (consistent with section 9 above having no segment table) |
| 3 | 581 | "Other expenses also includes the expenditure incurred towards travel and conveyance, security expenses and legal..." |
| 4 | 583-597 | "During the Previous year, the management has reclassified employee costs related to projects from Employee Benefit Expenses..." — reclassification table (see section 10 above) |
| 5 | 599-606 | "Pursuant to the directions issued by Hon'ble National Company Law Tribunal, Mumbai Bench ('NCLT Mumbai'), vide its order dated 22nd April 2026..." — OCR renders leading digit as "S"; same Oilmax merger disclosure as consolidated note 5 | OCR digit corruption "5"->"S"; caught only via manual sweep (see Reconciliation note 1) |
| 6 | 607-618 | "During the Quarter the Company has granted 1,77,000 stock options to employees of the Company and 17,000 stock options were allotted..." — same ESOP grant + warrant lapse/forfeiture disclosure as consolidated note 7, bundled under one note number | Two distinct corporate actions bundled under one note number |
| 7 | 621-622 | "Exceptional items for the quarter and year ended 31 March 2026 represent amount written of Rs 271.82 lakhs pursuant to..." — Outside Expert Council, contractual dispute (standalone entity only; no subsidiary sub-item, unlike consolidated note 8) |
| 8 | 624-626 | "Figures for the quarters ended 31 March 2026 are the balancing figures between the audited figures for the full financial year..." — Q4 balancing-figure convention |

Standalone signature block: 630-642 — For Asian Energy Services Limited,
Kapil Garg, Managing Director, DIN: 01360843, Place: Mumbai, Date: 13 August
2026 (date only, no time stamp captured in extract).

8 numbered notes for the standalone results.

---

## 12. DIGITAL / WET SIGNATURE BLOCKS — SUMMARY

| # | Line(s) | Signatory | Designation | Entity/Doc | Timestamp | Flags |
|---|---------|-----------|-------------|------------|-----------|-------|
| 1 | 43-54 | Shweta Vaibhav Jain | Company Secretary & Compliance Officer | Board Outcome letter | 2026.08.13 18:05:32 +05'30' (true digital signature, cryptographic timestamp) | Timestamp is AFTER board meeting conclusion (16:04) — expected, no flag |
| 2 | 168-180 | Suresh [surname OCR-illegible] | Partner, SGCO & Co. LLP | Consolidated Review Report | Date only: 13 August 2026, no time | UDIN 26044739XCBNDT1023 |
| 3 | 489-501 | [name OCR-illegible: "S~Mi"] | Partner, SGCO & Co. LLP | Standalone Review Report | Date only: 13 August 2026, no time | UDIN 26044739OBFLUH7225; same Mem. No. 044739 as sig #2 — appears to be the same partner signing both reports |
| 4 | 409-418 | Kapil Garg | Managing Director (DIN 01360843) | Consolidated results | Date only: 13 August 2026, no time | |
| 5 | 630-642 | Kapil Garg | Managing Director (DIN 01360843) | Standalone results | Date only: 13 August 2026, no time | |

5 signature blocks total; only 1 carries a machine timestamp precise enough
to sequence against the board meeting clock.

---

## SUMMARY COUNTS

- Numbered notes: 17 (9 consolidated + 8 standalone)
- Unnumbered footnotes (EPS annualization): 2
- Segment narrative notes (roman numeral): 4
- Total notes-category disclosure units: 23
- Financial statement line items (all tables): 90
  - Consolidated P&L: 36 | Consolidated segment: 14 | Consolidated note 6 table: 6
  - Standalone P&L: 28 | Standalone note 4 table: 6
- ZERO_STANDING flagged line items: 13
- Board Outcome agenda items: 1
- Auditor report paragraphs: 13 (8 consolidated + 5 standalone)
- Consolidation entities (Annexure 1): 31 (26 subsidiaries/step-down + 5 JVs)
- Digital/wet signature blocks: 5
