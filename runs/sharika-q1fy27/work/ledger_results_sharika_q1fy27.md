# A2 ENUMERATOR LEDGER — Sharika Enterprises Limited (SHARIKA), Q1FY27 (results)
### REGENERATED against corrected 597-line A1 extract (supersedes prior 539-line-based ledger)

Source: `extract_results_sharika_q1fy27.txt` (A1 extract v2, 9 pages, 597 lines,
unit convention Lakhs). OCR corrections were applied to pages 4, 5, 8, 9
(pages 1, 2, 3, 6, 7 cross-checked and found consistent with the original
text layer, no changes there). Prior-quarter ledger: none available (first
quarterly-pipeline run for this ticker) — entity cross-check and
DROPPED-item checks could not be performed; flagged `NO_PRIOR_LEDGER`
throughout where relevant.

**What changed vs the prior ledger**: two entirely new disclosure blocks were
recovered that the original text-layer extraction had dropped completely —
(1) the standalone auditor's sign-off block (FRN/UDIN/Date/Place, page 4) and
(2) full director sign-off blocks naming Rajinder Kaul, Managing Director,
DIN-01609805, appended to BOTH the standalone (page 5) and consolidated
(page 9) results statements. The consolidated auditor's Membership Number,
previously unreadable ("M.No:~~~"), is now recovered as "57629". A tenth
note (Note 10, joint venture Electromeccanica India Pvt Ltd, investment
eroded to nil, excluded from consolidation) was recovered on both the
standalone and consolidated notes blocks — previously entirely absent from
the extract. All content line numbers shifted (+41 to +56 depending on
page) due to the longer header and the newly recovered text.

```
=== A2 COUNT TEST ===
category: agenda_items       grep_count: 1    sweep_count: 1    match: yes
category: signature_blocks   grep_count: 24   sweep_count: 24   match: yes
category: auditor_paras      grep_count: 28   sweep_count: 28   match: yes
category: notes              grep_count: 20   sweep_count: 20   match: yes
category: line_items         grep_count: 61   sweep_count: 61   match: yes
category: zero_standing      grep_count: 8    sweep_count: 8    match: yes
category: entities           grep_count: 4    sweep_count: 4    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

### Reconciliation method note
Notes: `grep -n -E "^\s*[0-9]{1,2}\s+[A-Z]|^\s*[0-9]{1,2}\s+The"` scoped to
the standalone notes block (lines 295-342) returns 10 matches (1-10, note 5
now correctly OCR'd as "5" per the A1 correction log) and to the
consolidated notes block (lines 557-589) returns 10 matches (1-10). Total
20, matching the manual sweep exactly (GATE A2 pass) — no OCR-error
work-around needed this pass since the A1 header documents the Note 5
digit/letter conflation was already resolved before this extract was
generated.

Line items: same numeric-value-line grep + zero-standing-blank-row method
used in the prior ledger, re-run against the new line ranges (standalone
P&L lines 250-293, consolidated P&L lines 504-555); tables themselves are
byte-for-byte unchanged from the prior extract (only the roman-numeral OCR
garbles persist, unaffected by the page 4/5/8/9 corrections), so counts are
unchanged at 26 standalone + 35 consolidated = 61, with 8 zero-standing rows
(3 standalone, 5 consolidated) — confirmed by re-grep, not just carried
forward.

Signature/certification blocks: grep on `For R D V|Chartered Accountants$|FRN|UDIN|M\.No|Rajinder Kaul|Managing Director|DIN -|Date:|Place:`
against the full file, filtered to the actual body content lines (excluding
header changelog references to the same terms), returns exactly the 24 rows
enumerated in section 2 below — reconciled against manual line-by-line read
of each of the five signature/certification groups (board letter, standalone
auditor block, standalone director block, consolidated auditor block,
consolidated director block).

Auditor paragraphs: standalone report has 14 main paragraphs (title,
addressee, intro, management responsibility, auditor responsibility/SRE
2410, Basis for Qualified Opinion heading, BFQO a/b/c, Qualified Opinion
conclusion, Emphasis of Matter heading, EOM a/b, closing statement) and
consolidated report has 14 main paragraphs (same structure plus the
Master Circular Reg 33(8) paragraph and the entities-list intro, which
standalone lacks, but consolidated's EOM is a single a) item vs standalone's
two — net 14 each). Sign-off/UDIN blocks are enumerated separately under
signature_blocks, not double-counted here. Total 28. (Correction from the
prior ledger version of this file, which stated 27 due to an arithmetic
slip in the closing summary text — the underlying paragraph list there was
in fact already 14+14; this version's summary math is fixed to agree with
its own itemized rows.)

---

## 1. Board Outcome Letter — Agenda Items (page 1, lines 56-110)

| # | Item | Line | Detail | Flags |
|---|------|------|--------|-------|
| 1 | Approval of Un-Audited Financial Results | 73-75 | Board approved standalone (and, per separate consolidated statement, consolidated) unaudited financial results for quarter ended 30 June 2026, reviewed by Audit Committee first, along with Limited Review Report | — |

No other agenda items present: no AR/annual report approval, no AGM notice,
no record date, no dividend, no director appointment/resignation, no
auditor change, no scrutinizer appointment, no ESOP grant, no
capital-raising enabling resolution appear anywhere in the letter.
Single-item board meeting.

**Meeting duration**: commenced 04:30 P.M., concluded 10:00 P.M. (line 80) —
a 5.5-hour meeting for a single disclosed agenda item (results approval
only) is notable; duration disproportionate to the one listed item. Flag
`LONG_MEETING_SINGLE_ITEM`.

## 2. Signature / Certification Blocks (24 rows)

### 2a. Board outcome letter (page 1)
| # | Element | Line(s) | Detail | Flags |
|---|---------|---------|--------|-------|
| 1 | Digital signature block | 86-103 | Pushpa Yadav, Company Secretary & Compliance Officer; digitally signed 2026.08.12 22:14:17 +05'30' — 14 minutes after stated meeting conclusion (10:00 PM) | — (timestamp is after, not before, conclusion; no anomaly) |

### 2b. Standalone auditor's report sign-off (page 4, RECOVERED — dropped entirely in prior extraction)
| # | Element | Line(s) | Detail | Flags |
|---|---------|---------|--------|-------|
| 2 | Firm signature line | 235-236 | "For R D V & Associates, Chartered Accountants" | `NEWLY_RECOVERED` |
| 3 | FRN | 237 | "006??8" — OCR reads "006" then unclear digit(s) then "8", obscured by stamp/seal | `NEWLY_RECOVERED`, `OCR_ILLEGIBLE` |
| 4 | UDIN | 238 | "265478T8DARUYA5196" (low confidence; alternate OCR pass read "265479...SDARUYA5196") | `NEWLY_RECOVERED`, `OCR_LOW_CONFIDENCE` — exact characters not assured, do not treat as verified against UDIN portal without confirmation |
| 5 | Date | 239 | 12-08-2026 | `NEWLY_RECOVERED` |
| 6 | Place | 240 | Delhi | `NEWLY_RECOVERED` |

### 2c. Standalone director sign-off (page 5, RECOVERED — dropped entirely in prior extraction)
| # | Element | Line(s) | Detail | Flags |
|---|---------|---------|--------|-------|
| 7 | Attestation line | 338-339 | "For and on behalf of the Board of Directors of / SHARIKA ENTERPRISES LIMITED" | `NEWLY_RECOVERED` |
| 8 | Signatory name | 340 | Rajinder Kaul | `NEWLY_RECOVERED` — first identification in this filing of who signs on the Board's behalf |
| 9 | Designation | 341 | Managing Director | `NEWLY_RECOVERED` |
| 10 | DIN | 342 | 01609805 (one lower-confidence alternate OCR pass read "01609808"; last digit obscured by stamp) | `NEWLY_RECOVERED`, `OCR_LOW_CONFIDENCE` on last digit |
| 11 | Date | 340 (right column) | 12 Aug 2026 | `NEWLY_RECOVERED` |
| 12 | Place | 341 (right column) | Noida | `NEWLY_RECOVERED` |

### 2d. Consolidated auditor's report sign-off (page 8, RECOVERED heading + corrected M.No)
| # | Element | Line(s) | Detail | Flags |
|---|---------|---------|--------|-------|
| 13 | Firm signature line | 483-484 | "For R D V & Associates, Chartered Accountants" | `NEWLY_RECOVERED` (heading line only; M.No/UDIN/Date/Place lines below it were already present in the prior extraction) |
| 14 | FRN | 485 | Illegible — obscured by stamp/seal, no reliable OCR read in any pass | `OCR_ILLEGIBLE` |
| 15 | M.No | 486 | 57629 | `OCR_CORRECTED` — prior extraction rendered this as "~~~" (unreadable tildes); now recovered cleanly |
| 16 | UDIN | 487 | 26547918ZQNNPE4044 | — (unchanged from prior extraction, already legible) |
| 17 | Date | 488 | 12-08-2026 | — |
| 18 | Place | 489 | Delhi | — |

### 2e. Consolidated director sign-off (page 9, RECOVERED — dropped entirely in prior extraction)
| # | Element | Line(s) | Detail | Flags |
|---|---------|---------|--------|-------|
| 19 | Attestation line | 591-592 | "For and on behalf of the Board of Directors of / SHARIKA ENTERPRISES LIMITED" | `NEWLY_RECOVERED` |
| 20 | Signatory name | 593 | Rajinder Kaul | `NEWLY_RECOVERED` — same signatory as standalone block (2c), consistent |
| 21 | Designation | 594 | Managing Director | `NEWLY_RECOVERED` |
| 22 | DIN | 595 | 01609805 (same low-confidence last-digit caveat as row 10) | `NEWLY_RECOVERED`, `OCR_LOW_CONFIDENCE` |
| 23 | Date | 596 | 12 Aug 2026 | `NEWLY_RECOVERED` |
| 24 | Place | 597 | Noida (OCR-corrected from "Naida") | `NEWLY_RECOVERED`, `OCR_CORRECTED` |

**Prior-ledger flag retired**: `MISSING_STANDALONE_AUDITOR_SIGNOFF_BLOCK` no
longer applies — the block was an extraction gap, not a true absence, and is
now recovered at row 2-6 above (with residual OCR-quality caveats on FRN and
UDIN that A3/A4 should carry forward, not resolve by assumption).

## 3. Standalone Auditor's Report — Main Paragraphs (pages 2-4, lines 119-232)

| # | Paragraph | Line(s) | First ~15 words | Flags |
|---|-----------|---------|------------------|-------|
| 1 | Report title/heading | 119-121 | "Independent Auditor's Report on the Quarterly Unaudited Standalone Financial Results of the Company..." | — |
| 2 | Addressee | 123 | "To the Board of Directors of Sharika Enterprises limited" | — |
| 3 | Intro — statement reviewed | 125-129 | "We have reviewed the accompanying statement of unaudited standalone financial results..." | — |
| 4 | Management's responsibility | 131-137 | "The Company's Management is responsible for the preparation of the Statement..." | — |
| 5 | Auditor's responsibility / SRE 2410 scope | 139-148 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| 6 | Basis for Qualified Opinion — heading/intro | 150-151 | "Attention is invited to the following notes of the accompanying standalone financial results:" | — |
| 7 | BFQO (a) — Note 8, slow/non-moving inventory Rs 149.25 lakh, no obsolescence provision, no ageing/NRV assessment | 153-163 | "Note No. 8 which states that the Company has identified slow/non-moving inventories..." | `RECURRING_QUALIFICATION` (also qualified in FY26 report) |
| 8 | BFQO (b) — Note 9, advances to suppliers/others Rs 210.66 lakh, some >3 yrs old, no recoverability assessment/provision | 171-182 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 9 | BFQO (c) — Note 9, trade receivables Rs 4,862.30 lakh, old balances incl. >3 yrs, no ECL computed under Ind AS 109 | 184-194 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 10 | Qualified Opinion conclusion | 196-205 | "Based on our review conducted and procedures performed as stated in paragraph above, except for..." | — |
| 11 | Emphasis of Matter — heading/intro | 207-209 | "Attention is invited to the following notes of the accompanying standalone financial results:" | — |
| 12 | EOM (a) — Note 7, sequential settlement arrangement with vendors; receivables under this arrangement included in bank stock statements | 211-216 | "Note No. 7 regarding the Company's arrangement with certain vendors for sequential settlement..." | — |
| 13 | EOM (b) — Note 6, investment in Sharika Spintech Rs 579.69 lakh incl. loans, vs accumulated losses Rs 514.68 lakh, no impairment taken | 224-230 | "Note No. 6 regarding the investment made by the Company in Sharika Spintech Private Limited..." | `SOURCE_DOCUMENT_INCONSISTENCY` — this paragraph states accumulated losses of Rs 514.68 lakh; Note 6 itself (section 5, row 6) states Rs 514.63 lakh for the identical fact as at the identical date. Both figures independently OCR-confirmed at 300dpi per the A1 header; not a scan artifact. Unresolved discrepancy in the source filing. |
| 14 | Closing statement | 232 | "Our opinion is not modified in respect of the aforesaid matters." | — |

## 4. Consolidated Auditor's Report — Main Paragraphs (pages 6-8, lines 351-477)

| # | Paragraph | Line(s) | First ~15 words | Flags |
|---|-----------|---------|------------------|-------|
| 1 | Report title/heading | 351-353 | "Independent Auditor's Report on the Quarterly Unaudited Consolidated Financial Results of the Company..." | — |
| 2 | Addressee | 355 | "To the Board of Directors of Sharika Enterprises limited" | — |
| 3 | Intro — statement reviewed | 357-362 | "We have reviewed the accompanying Statement of unaudited Consolidated Financial Results of Sharika Enterprises Limited..." | — |
| 4 | Holding Company management's responsibility | 364-370 | "The Holding Company's Management is responsible for the preparation of the Statement..." | — |
| 5 | Auditor's responsibility / SRE 2410 scope | 372-380 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements..." | — |
| 6 | Master Circular Reg 33(8) procedures (consolidated-only, not present in standalone report) | 382-383 | "We also performed procedures in accordance with the Master Circular issued by the Securities and Exchange Board of India..." | — |
| 7 | Entities included in the Statement — list intro | 385 | "The Statement includes the results of the following entities:" | — |
| 8 | Basis for Qualified Opinion — heading/intro | 394-396 | "Attention is invited to the following notes of the accompanying consolidated financial results:" | — |
| 9 | BFQO (a) — Note 8, holding co. slow/non-moving inventory Rs 149.25 lakh, no obsolescence provision | 398-418 | "Note No. 8 which states that the holding company has identified slow/non-moving inventories..." | `RECURRING_QUALIFICATION` |
| 10 | BFQO (b) — Note 9, holding co. advances Rs 210.66 lakh, no recoverability assessment/provision | 420-431 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION` |
| 11 | BFQO (c) — Note 9, holding co. trade receivables Rs 5,273.38 lakh (consolidated figure, differs from standalone Rs 4,862.30 lakh), no ECL computed | 433-443 | "Note No. 9 regarding non-reconciliation of certain balances and non-availability of party-wise details..." | `RECURRING_QUALIFICATION`; receivables figure differs from standalone (5,273.38 vs 4,862.30) — expected given consolidation scope, flag for A3/A4 arithmetic cross-check |
| 12 | Qualified Opinion conclusion | 445-454 | "Based on our review conducted and procedures performed as stated in paragraph above, except for..." | — |
| 13 | Emphasis of Matter — Note 7, sequential settlement arrangement | 456-476 | "We draw attention to the note no. 7 of the accompanying consolidated financial results regarding the Holding Company's arrangement..." | — |
| 14 | Closing statement | 476-477 | "Our opinion is not modified in respect of this matter." | — |

## 5. Standalone Notes to Financial Results (page 5-6, lines 295-342)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 297-298 | "The financial results of the Company have been prepared in accordance with Indian Accounting Standard..." | — |
| 2 | 299-300 | "The standalone financial results for the quarter ended 30 June, 2026 have been reviewed by the Audit Committee..." | — |
| 3 | 302-304 | "The results have been subjected to a review by the Statutory Auditors of the Company pursuant to Regulation 33..." | — |
| 4 | 305-307 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | — |
| 5 | 309-312 | "The Company Is primarily engaged In Engineering, Procurement and Construction business (EPC) relating to Electrical..." | `OCR_CORRECTED` — note number OCR-corrected from "S" to "5"; single reportable segment disclosure (Ind AS 108) |
| 6 | 315-319 | "The Company's Investment in Sharika Spintech Private Limited ('Spintech'), comprising of equity and loans, amounting Rs. 579.69 lakhs..." | `OCR_CORRECTED` (date "20Z6"->"2026"); `SOURCE_DOCUMENT_INCONSISTENCY` — states accumulated losses of Rs 514.63 lakh, vs Rs 514.68 lakh in the auditor's EOM paragraph (section 3, row 13) for the same fact; cross-refs EOM |
| 7 | 321-324 | "The Company has entered Into sequential settlement arrangements with certain vendors In respect of specific contracts..." | cross-refs EOM para (section 3, row 12) |
| 8 | 325-326 | "The Company has Identified slow/non-moving inventories amounting to Rs. 149.25 lakhs. The estimated net realizable value..." | cross-refs BFQO para (section 3, row 7); note claims NRV higher than carrying amount — directly contradicted by auditor's qualification that no such assessment was actually carried out |
| 9 | 329-331 | "Certain balances Including trade and other payables. advances from customers, loans and advances, trade and other receivables..." | cross-refs BFQO paras (section 3, rows 8-9) |
| 10 | 336 | "The financials of joint venture company, Electromeccanica India Private Limited is not considered as the investment..." | `NEWLY_RECOVERED` (entire note dropped in prior extraction); joint venture investment eroded to nil by accumulated losses, excluded from consolidation scope — not on the consolidation entity list (section 7); OCR uncertain on exact spelling "Electtromeccanica"/"Electromeccanica" |

## 6. Consolidated Notes to Financial Results (page 9, lines 557-589)

| Note # | Line | First ~15 words | Flags |
|--------|------|------------------|-------|
| 1 | 560-561 | "The consolidated financial results of the Company have been prepared in accordance with Indian Accounting Standard..." | — |
| 2 | 562-563 | "The consolidated financial results for the quarter ended 30 June, 2026 have been reviewed by the Audit Committee..." | — |
| 3 | 564-566 | "The consolidated financial results have been subjected to a review by the Statutory Auditors of the Company..." | — |
| 4 | 567-569 | "The figures for the quarter ended March 31, 2026 are the balancing figures between the audited figures..." | — |
| 5 | 570-573 | "The Holding Company is primarily engaged in Engineering, Procurement and Construction business (EPC) relating to Electrical..." | single reportable segment disclosure (Ind AS 108) |
| 6 | 574-578 | "The Holding Company's investment in Sharika Spintech Private Limited ('Spintech'), comprising of equity and loans, amounting Rs. 579.69 lakhs..." | `SOURCE_DOCUMENT_INCONSISTENCY` — states accumulated losses of Rs 514.63 lakh, vs Rs 514.68 lakh in the standalone auditor's EOM paragraph for the identical fact (this note's own consolidated auditor EOM references Note 7, not Note 6 directly, but the underlying 514.63/514.68 discrepancy originates in the company's Note 6 text on both statements) |
| 7 | 579-581 | "The Holding Company has entered into sequential settlement arrangements with certain vendors in respect of specific contracts..." | cross-refs EOM para (section 4, row 13) |
| 8 | 582-584 | "The Holding Company has identified slow/non-moving inventories amounting to Rs. 149.25 lakhs. The estimated net realizable value..." | cross-refs BFQO para (section 4, row 9); same NRV self-assessment contradiction as standalone Note 8 |
| 9 | 585-587 | "Certain balances including trade and other payables, advances from customers, loans and advances, trade and other receivables..." | `NEWLY_RECOVERED` tail ("...those related to MSME and interest etc. if any payable in this respect are currently not ascertainable.") — prior extraction cut this note off mid-sentence; now complete and matches the standalone Note 9 wording. cross-refs BFQO paras (section 4, rows 10-11) |
| 10 | 588 | "The financials of joint venture company, Electromeccanica India Private Limited is not considered as the investment..." | `NEWLY_RECOVERED` (entire note dropped in prior extraction); identical wording to standalone Note 10 (section 5, row 10) |

## 7. Consolidation Entity List (lines 387-392)

| # | Entity | Relationship | Line | Flags |
|---|--------|--------------|------|-------|
| 1 | Sharika Enterprises Limited | Holding Company | 388 | — |
| 2 | Sharika Spintech Private Limited | Subsidiary | 390 | subject of EOM Note 6 (accumulated losses Rs 514.63/514.68 lakh — see `SOURCE_DOCUMENT_INCONSISTENCY`) |
| 3 | Sharika Smartec Private Limited | Subsidiary | 391 | no separate note/mention elsewhere in extract |
| 4 | Contronics Switchgear India Private Limited | Subsidiary | 392 | no separate note/mention elsewhere in extract |

Not on this list, per Note 10 (section 5/6, row 10): Electromeccanica India
Private Limited, a joint venture whose investment has been fully eroded by
accumulated losses and whose financials are accordingly not considered in
either the standalone or consolidated statements. This is a disclosed
exclusion, not an omission, but A3/A4 should confirm no residual carrying
value or contingent exposure remains unflagged.

`NO_PRIOR_LEDGER` — cannot cross-check for entities added/removed/renamed vs
prior quarter; no prior-quarter ledger was supplied. A3/A4 should source the
prior quarter's consolidated auditor report entity list independently if an
`ENTITY_CHANGE` check is required.

## 8. Standalone Statement of Financial Results — Line Items (page 5, lines 250-293)

Values shown for reference are the current quarter (30-Jun-2026) column only;
full four-period detail (30-Jun-2026 / 31-Mar-2026 / 30-Jun-2025 / FY26) is in
the source table.

| # | Line item | Line | Q1FY27 value (Rs lakh) | Flags |
|---|-----------|------|--------------------------|-------|
| 1 | Revenue From Operations | 251 | 2,219.83 | — |
| 2 | Other Income | 252 | 15.04 | — |
| 3 | Total Income (I+II) | 253 | 2,234.87 | — |
| 4 | Cost of materials consumed | 255 | 1,573.50 | — |
| 5 | Sub-contracting charges | 256 | 197.37 | — |
| 6 | Employee benefit expenses | 257 | 145.05 | — |
| 7 | Finance costs | 258 | 88.67 | — |
| 8 | Depreciation and amortisation expenses | 259 | 22.60 | — |
| 9 | Other expenses | 260 | 175.80 | — |
| 10 | Total expenses | 261 | 2,202.99 | — |
| 11 | Profit before Exceptional Items and Tax (III-IV) | 262 | 31.88 | — |
| 12 | Exceptional Items | 263 | "-" (dash, all 4 periods) | `ZERO_STANDING` |
| 13 | Profit/(Loss) before Tax (V-VI) | 264 | 31.88 | — |
| 14 | Current tax | 266 | "-"/blank (dash or blank, all 4 periods) | `ZERO_STANDING` |
| 15 | Deferred tax | 267 | 9.02 | — |
| 16 | Taxation pertaining to earlier years | 268 | blank, no value in any period | `ZERO_STANDING` |
| 17 | Total Tax Expense | 269 (OCR-wrapped across 269-273) | 9.02 | — |
| 18 | Profit/(Loss) after tax (VII-VIII) | 274 | 22.86 | — |
| 19 | Re-measurement gains on Defined Benefit Plans | 277 | 0.65 | — |
| 20 | Less: Tax effect on Re-measurement of Defined Benefit Plans | 278 | (0.17) | — |
| 21 | Other Comprehensive Income/(loss) (net of tax) (i+ii) | 280-281 | 0.48 | — |
| 22 | Total comprehensive Income/(Loss) for the period (IX+X) | 283 | 23.34 | — |
| 23 | Paid-up equity share capital (face value Rs 5 each) | 286-287 | 2,165.00 | — |
| 24 | Other Equity Excluding Revaluation Reserves | 288 | blank in all 3 quarter-columns; (217.33) only in "Year Ended 31-Mar-2026" column | `PARTIAL_DISCLOSURE` — reported once a year (opening reserves convention), not a true zero-standing but only 1 of 4 period columns populated |
| 25 | Earnings per equity share — Basic | 292 | 0.05 | — |
| 26 | Earnings per equity share — Diluted | 293 | 0.05 | — |

Standalone line items: 26. Standalone zero_standing: 3 (rows 12, 14, 16).

## 9. Consolidated Statement of Financial Results — Line Items (page 9, lines 504-555)

Values shown for reference are the current quarter (30-Jun-2026) column only.

| # | Line item | Line | Q1FY27 value (Rs lakh) | Flags |
|---|-----------|------|--------------------------|-------|
| 1 | Revenue From Operations | 504 | 2,220.07 | — |
| 2 | Other Income | 505 | 11.56 | — |
| 3 | Total Income (I+II) | 506 | 2,231.63 | — |
| 4 | Cost of materials consumed | 508 | 1,603.18 | — |
| 5 | Sub-contracting charges | 509 | 197.37 | — |
| 6 | Changes in inventories of finished goods and Stock-in-trade | 510 | (34.14) | line not present in standalone table — consolidated-only item |
| 7 | Employee benefit expenses | 511 | 173.79 | — |
| 8 | Finance costs | 512 | 89.49 | — |
| 9 | Depreciation and amortisation expenses | 513 | 28.89 | — |
| 10 | Other expenses | 514 | 132.08 | — |
| 11 | Total expenses | 515 | 2,190.66 | — |
| 12 | Profit before share of profit/(loss) of joint ventures and associate and tax | 516-517 | 40.97 | — |
| 13 | Share in profit/(loss) of joint ventures and associate (net) | 518 | blank, no value any period | `ZERO_STANDING` — template line for JV/associate profit share; cross-refs Note 10 (JV Electromeccanica excluded, investment eroded to nil, so no share of profit/loss recognized) |
| 14 | Profit before exceptional items and tax | 519 | 40.97 | — |
| 15 | Exceptional Items | 520 | blank, no value any period | `ZERO_STANDING` |
| 16 | Profit/(Loss) before Tax | 521 | 40.97 | — |
| 17 | Current tax | 523 | blank, no value any period | `ZERO_STANDING` |
| 18 | Deferred tax | 524 | 11.11 | — |
| 19 | Taxation pertaining to earlier years | 525 | blank, no value any period | `ZERO_STANDING` |
| 20 | Total Tax Expense | 526 | 11.11 | — |
| 21 | Profit/(Loss) after tax | 527 | 29.86 | — |
| 22 | Re-measurement gains on Defined Benefit Plans | 530 | 0.65 | — |
| 23 | Less: Tax effect on Re-measurement of Defined Benefit Plans | 531 | (0.17) | — |
| 24 | Other Comprehensive Income/(loss) (net of tax) | 532 | 0.48 | — |
| 25 | Total comprehensive Income/(Loss) for the period | 533 | 30.34 | — |
| 26 | Profit/(Loss) for the period attributable to: Owners of the Company | 535 | 34.61 | — |
| 27 | Profit/(Loss) for the period attributable to: Non-Controlling interest | 536 | (4.75) | — |
| 28 | Other Comprehensive Income/(Loss) attributable to: Owners of the Company | 540 | 0.48 | — |
| 29 | Other Comprehensive Income/(Loss) attributable to: Non-Controlling interest | 541 | blank, no value any period | `ZERO_STANDING` — NCI's OCI share is nil every period shown |
| 30 | Total OCI attributable to: Owners of the Company | 545 | 35.09 | — |
| 31 | Total OCI attributable to: Non-Controlling interest | 546 | (4.75) | — |
| 32 | Paid up equity share capital (face value Rs 5/- each) | 550-551 | 2,165.00 | — |
| 33 | Other Equity Excluding Revaluation Reserves | 552 | blank in all 3 quarter-columns; (835.99) only in "Year Ended 31-Mar-2026" column | `PARTIAL_DISCLOSURE` — same convention as standalone row 24 |
| 34 | Earnings per equity share — Basic | 554 | 0.08 | — |
| 35 | Earnings per equity share — Diluted | 555 | 0.08 | — |

Consolidated line items: 35. Consolidated zero_standing: 5 (rows 13, 15, 17,
19, 29).

**Cross-table arithmetic flag**: consolidated Profit/(Loss) after tax
(29.86, row 21) = Owners' share (34.61) + NCI share (-4.75) = 29.86 — ties
out. Consolidated PAT (29.86) exceeds standalone PAT (22.86, section 8 row
18) by 7.00; consolidated revenue (2,220.07) is close to but not equal to
standalone revenue (2,219.83) despite Sharika Enterprises being the sole
"Holding Company" reporting entity in both — expected due to subsidiary
contribution and inter-company eliminations, but flag
`RECONCILE_STANDALONE_VS_CONSOLIDATED` for A3/A4 to trace the subsidiaries'
individual contribution, since none of the three subsidiaries file separate
line-item detail in this extract.

---

## SECTION TOTALS (feeds COUNT TEST and YAML block)

| Category | Count |
|---|---|
| Agenda items (Board Outcome letter) | 1 |
| Signature/certification block elements (5 groups, 24 individual rows) | 24 |
| Auditor report main paragraphs (standalone 14 + consolidated 14) | 28 |
| Notes (standalone 10 + consolidated 10) | 20 |
| Line items, standalone P&L | 26 |
| Line items, consolidated P&L | 35 |
| **Line items, total** | **61** |
| Zero-standing rows, standalone | 3 |
| Zero-standing rows, consolidated | 5 |
| **Zero-standing rows, total** | **8** |
| Entities in consolidation | 4 |

Flags raised across the ledger: `LONG_MEETING_SINGLE_ITEM`, `NEWLY_RECOVERED`
(x17: 5 standalone auditor sign-off elements, 6 standalone director sign-off
elements, 1 consolidated auditor firm-heading line, 6 consolidated director
sign-off elements — plus the two recovered notes counted separately below),
`OCR_ILLEGIBLE` (x2: standalone and consolidated FRN), `OCR_LOW_CONFIDENCE`
(x3: standalone UDIN, standalone DIN last digit, consolidated DIN last
digit), `OCR_CORRECTED` (x3: consolidated M.No, standalone Note 5 number,
standalone Note 6 date garble, consolidated director-block Place typo —
see individual rows), `RECURRING_QUALIFICATION` (x6), `SOURCE_DOCUMENT_INCONSISTENCY`
(x3: standalone EOM para, standalone Note 6, consolidated Note 6 — all the
same 514.63-vs-514.68 lakh Spintech accumulated-loss discrepancy between the
company's Note 6 and the auditor's qualified-opinion paragraph, confirmed by
independent OCR and left unharmonized per the zero-interpretation mandate),
`NO_PRIOR_LEDGER`, `ZERO_STANDING` (x8), `PARTIAL_DISCLOSURE` (x2),
`RECONCILE_STANDALONE_VS_CONSOLIDATED`. Two `NEWLY_RECOVERED` notes (standalone
and consolidated Note 10, JV Electromeccanica) are counted under the notes
category, not the signature_blocks category.
