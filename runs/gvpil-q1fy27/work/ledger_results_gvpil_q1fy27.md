# A2 COMPLETENESS LEDGER — GVPIL Q1FY27 Results Filing

Source: `runs/gvpil-q1fy27/work/extract_results_gvpil_q1fy27.txt` (621 lines, 9 pages, unit
convention Rs Millions, x0.1 to Rs Crores). Enumeration only; no interpretation performed.
Prior-quarter ledger: NONE — cross-quarter diffs (DROPPED_SLIDE-equivalent, ENTITY_CHANGE)
cannot be run this quarter; flagged `NO_PRIOR_LEDGER` wherever a diff would normally apply.

## METHODOLOGY NOTE ON THE COUNT TEST (read before the gate table)

For the `line_items` and `notes` categories a single generic grep pattern systematically
undercounts financial-statement tables because headers, subtotals, and continuation rows
often carry no leading digit. Two grep passes were run and reconciled against one continuous
manual line-by-line read of the whole extract:

- Pass 1 (`^\s*[0-9]+\s` and lettered `a)`/`1)` sub-item patterns, scoped to the two P&L
  tables): 63 rows caught (18 standalone top-level of 19 + 11 standalone lettered/numbered
  sub-items; 21 consolidated top-level of 21 + 13 consolidated lettered/numbered sub-items).
- Pass 2 (literal-string grep for known subtotal/header/continuation text — "Total expenses
  (4)", "Exceptional items [refer note", "Items that will not be reclassified", "Basic and
  diluted EPS", "Total Income", "Total Expenses", "Remeasurements of defined benefit
  liability", "Income tax relating to above", etc.): +25 new rows caught.
- Combined grep = 88. Manual sweep = 94. The 6-row gap was traced and every row named below;
  4 are genuine wording variants no regex in Pass 1/2 targeted, 2 are OCR artifacts:
  - Line 176: standalone item "1 Revenue from operations" is rendered `.1 Revenue from
    operations` (period substituted for nothing before the digit) — grep pattern requiring
    digit-at-line-start missed it. Flag `OCR_ARTIFACT`.
  - Lines 200-202: standalone "Profit(+/Loss(-) from discontinued operations before
    exceptional items" (item 9's profit sub-line) — wording variant, not caught by Pass 2.
  - Line 214: standalone "Remeasurements OR defined benefit liability- Discontinued
    Operations" — OCR mis-scan of "of" as "or" meant the Pass 2 literal string ("...liability")
    still half-matched on "liability" but the row was verified only by manual read; flag
    `OCR_ARTIFACT`.
  - Line 262: standalone embedded discontinued-ops table, row 5 "Profit(+/Loss(-) from
    discontinued operations before exceptional items" — wording variant.
  - Lines 454-456: consolidated equivalent of the 200-202 row.
  - Line 520: consolidated embedded discontinued-ops table, row 5 equivalent of line 262.
  After re-sweep, both totals are reconciled to 94. No disclosure unit is missing from the
  ledger; the gap was purely a grep-pattern limitation, resolved before emission per GATE A2.
- `notes`: Pass 1 grep (`^\s*[0-9]+\s`, scoped to the two Notes sections) caught 16 of 17
  numbered notes. Consolidated Note 1 (line 486, "The unaudited Consolidated financial
  results include results of GE Power India Ltd...") carries **no visible numeral** in the
  source extraction — every subsequent consolidated note (2 through 9) is numbered normally,
  and the table cross-reference "(refer note 9)" at line 426 confirms 9 total consolidated
  notes, so this is note 1 with a dropped/illegible numeral, not a missing note. Flag
  `NOTE_NUMBERING_GAP`. Manual sweep = 17 (8 standalone + 9 consolidated). Reconciled: 17 = 17.

=== A2 COUNT TEST ===
category: notes            grep_count: 17 (16 auto + 1 manually confirmed unnumbered)   sweep_count: 17   match: yes
category: line_items       grep_count: 94 (88 combined auto passes + 6 manually confirmed)   sweep_count: 94   match: yes
category: zero_standing    grep_count: 15   sweep_count: 15   match: yes
category: agenda_items     grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras    grep_count: 10   sweep_count: 10   match: yes
category: entities         grep_count: 2    sweep_count: 2    match: yes
category: signature_blocks grep_count: 5    sweep_count: 5    match: yes
category: media_release_items grep_count: 8 sweep_count: 8    match: yes
gate_a2: pass
=== END COUNT TEST ===

---

## TABLE 1 — BOARD OUTCOME / COVER LETTER (Reg 30 & 33), pages 1

| # | Item | Line(s) | Detail | Flags |
|---|------|---------|--------|-------|
| 1 | Agenda item — approval of results | 51-53 | Board approved unaudited standalone AND consolidated financial results for quarter ended 30 June 2026 | — |
| 2 | Agenda item — noted Limited Review Report | 52-54 | Board noted the Limited Review Report issued by M/s. Deloitte Haskins & Sells, Chartered Accountants, Statutory Auditors | — |
| 3 | Board meeting timing | 63 | Commenced 02:54 P.M. IST, concluded 04:25 P.M. IST — duration 91 minutes | informational |
| 4 | Other standard agenda categories swept for and NOT found | n/a | No AR approval, no AGM notice, no record date, no dividend, no director appointment/resignation, no auditor change, no scrutinizer appointment, no ESOP grant, no capital-raising enabling resolution anywhere in the cover letter | absence confirmed by manual sweep |
| 5 | Enclosures listed | 56-57, 87 | "A copy of aforementioned results with Limited Review Report thereon along with Media Release issued by the Company is enclosed"; "Encl: a/a" | — |

## TABLE 2 — SIGNATURE BLOCKS

| # | Signatory | Role | Line(s) | Detail | Flags |
|---|-----------|------|---------|--------|-------|
| 1 | Vipul Sharma | Company Secretary and Compliance Officer | 69-85 | Digitally signed; DN cn=VIPUL SHARMA c=IN o=Personal; Date: 2026-08-13 17:36+05:30 | Signature timestamp (17:36 IST) is AFTER board meeting conclusion (16:25 IST) — no timing flag warranted (this is the expected sequence) |
| 2 | Vikas Khurana | Partner, Deloitte Haskins & Sells (Standalone LR Report) | 143-155 | Firm Reg No. 015125N; Membership No. 503760; UDIN 26503760HQEVPP2136; Place Noida; Date 13 Aug 2026 | — |
| 3 | Vikas Khurana | Partner, Deloitte Haskins & Sells (Consolidated LR Report) | 398-408 | Firm Reg No. 015125N; Membership No. 503760; UDIN 26503760LNTANT6345; Place Noida; Date 13 Aug 2026 | Note: same partner, two distinct UDINs for standalone vs consolidated reports (expected — one per opinion) |
| 4 | Puneet Bhatla | Managing Director (Standalone financial results) | 301-308 | DIN 09536236; Place Noida; Date 13 Aug 2026; "For and on behalf of the Board" | — |
| 5 | Puneet Bhatla | Managing Director (Consolidated financial results) | 555-562 | DIN 09536236; Place Noida; Date 13 Aug 2026; "For and on behalf of the Board" | — |

## TABLE 3 — AUDITOR REPORT PARAGRAPHS: STANDALONE LIMITED REVIEW REPORT (Deloitte Haskins & Sells), pages 2

| Para | Line(s) | First ~15 words | Type | Flags |
|------|---------|------------------|------|-------|
| Title/addressee | 104-107 | "INDEPENDENT AUDITOR'S REVIEW REPORT ON REVIEW OF INTERIM STANDALONE FINANCIAL RESULTS... TO THE BOARD OF DIRECTORS" | header | — |
| 1 | 109-113 | "We have reviewed the accompanying Statement of Standalone Unaudited Financial Results of GE Power India Limited..." | scope of engagement | — |
| 2 | 115-121 | "This Statement, which is the responsibility of the Company's Management and approved by the Board..." | management responsibility statement | — |
| 3 | 123-132 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." | basis of review; explicit "we do not express an audit opinion" | — |
| 4 | 134-140 | "Based on our review conducted as stated in paragraph 3 above, nothing has come to our attention..." | conclusion — unmodified/clean | opinion type: UNMODIFIED |
| Entity list | n/a | Standalone report reviews GE Power India Limited only (no subsidiary/JV language) | scope | — |
| Signature block | 143-155 | See Table 2, row 2 | — | — |

Standalone auditor-report paragraph count: 4 numbered paragraphs.

## TABLE 4 — AUDITOR REPORT PARAGRAPHS: CONSOLIDATED LIMITED REVIEW REPORT (Deloitte Haskins & Sells), pages 5-6

| Para | Line(s) | First ~15 words | Type | Flags |
|------|---------|------------------|------|-------|
| Title/addressee | 327-330 | "INDEPENDENT AUDITOR'S REVIEW REPORT ON REVIEW OF INTERIM CONSOLIDATED FINANCIAL RESULTS... TO THE BOARD" | header | — |
| 1 | 332-338 | "We have reviewed the accompanying Statement of Consolidated Unaudited Financial Results of GE Power India Limited (the Parent)..." | scope of engagement | — |
| 2 | 340-346 | "This Statement, which is the responsibility of the Parent's Management and approved by the Parent's Board..." | management responsibility statement | — |
| 3 | 348-361 | "We conducted our review of the Statement in accordance with the Standard on Review Engagements (SRE) 2410..." plus SEBI Reg 33(8) circular procedures sentence (359-361) | basis of review; explicit "we do not express an audit opinion" | — |
| 4 | 363-366 | "The Statement includes the results of the following entities:" | entity list — see Table 10 | — |
| 5 | 368-375 | "Based on our review conducted and procedures performed as stated in paragraph 3 above, nothing has come to our attention..." | conclusion — unmodified/clean | opinion type: UNMODIFIED |
| 6 | 385-395 | "The consolidated unaudited financial results include the Group's share of profit after tax of Rs. 11.8 million..." | Other Matters — reliance on other auditor for the JV (unreviewed by Deloitte, reviewed by other auditors, furnished by Management) | entity NOT reviewed directly by principal auditor — JV relies on other auditor's report per para 6 |
| Signature block | 398-408 | See Table 2, row 3 | — | — |

Consolidated auditor-report paragraph count: 6 numbered paragraphs.

Combined auditor_paras total (standalone + consolidated): **10**.

## TABLE 5 — ENTITIES IN CONSOLIDATION

| # | Entity | Relationship | Line(s) | Flags |
|---|--------|--------------|---------|-------|
| 1 | GE Power Boilers Services Limited | Subsidiary Company | 365, 486-487 | — |
| 2 | NTPC GE Power Services Private Limited | Joint Venture (unreviewed by principal auditor; reviewed by other auditor per para 6, Table 4) | 366, 487 | NO_PRIOR_LEDGER — cannot cross-check add/remove/rename vs prior quarter |

## TABLE 6 — STANDALONE STATEMENT OF FINANCIAL RESULTS (page 3), line items

Columns present: 30 June 2026 (Unaudited), 31 March 2026 (Unaudited, refer note 8), 30 June
2025 (Unaudited), 31 March 2026 Year ended (Audited). "ZERO in ALL periods shown" and "ZERO in
quarter columns only (annual column nonzero)" both get `ZERO_STANDING` per instructions —
qualifier noted in the flag.

| Item | Line(s) | Label | Flags |
|------|---------|-------|-------|
| 1 | 176 | Revenue from operations | OCR_ARTIFACT (rendered ".1" not "1") |
| 2 | 177 | Other income | — |
| 3 | 179 | Total income (1+2) | — |
| 4 | 181 | Expenses [header] | — |
| 4a | 182 | Cost of material and erection services | — |
| 4b | 183 | Changes in work in progress | — |
| 4c | 184 | Employee benefits expense | — |
| 4d | 185 | Finance costs | — |
| 4e | 186 | Depreciation and amortisation expense | — |
| 4f | 187 | Other expenses | — |
| 4-total | 188 | Total expenses (4) | — |
| 5 | 190-192 | Profit(+)/Loss(-) before exceptional items from continuing operations (3-4) | — |
| 5-exceptional | 193 | Exceptional items [refer note 3] | ZERO_STANDING (nil in all 3 quarter columns; -275.7 only in FY26 annual column) |
| 6 | 194 | Profit(+/Loss(-) before tax from continuing operations | — |
| 7 | 195 | Tax expense (+)/Tax credit (-) [header] | — |
| 7-1 | 196 | Current tax | — |
| 7-2 | 197 | Deferred tax charge/(credit) | ZERO_STANDING (nil/dash in all 4 periods) |
| 8 | 198 | Net Profit(+)/Loss(-) after tax from continuing operations (6-7) | — |
| 9 | 199 | Discontinued operations [header] | — |
| 9-profit | 200-202 | Profit(+/Loss(-) from discontinued operations before exceptional items [refer note 2(i) and 2(ii)] | — |
| 9-exceptional | 203 | Exceptional items [refer note 3] | ZERO_STANDING (nil in all 3 quarter columns; -150.0 only in FY26 annual column) |
| 10 | 204 | Profit(+)/Loss(-) before tax from discontinued operations | — |
| 11 | 205 | Tax expense (+)/Tax credit (-) [header] | — |
| 11-1 | 206 | Current tax | ZERO_STANDING (nil/dash in all 4 periods) |
| 11-2 | 207 | Deferred tax charge/(credit) | ZERO_STANDING (nil/dash in all 4 periods) |
| 11-3 | 208 | Tax adjustments related to earlier years | ZERO_STANDING (dash/nil in all 3 quarter columns; -0.6 only in FY26 annual column) |
| 12 | 209 | Net Profit(+/Loss(-) after tax from discontinued operations (10-11) | — |
| 13 | 210 | Net Profit(+)/Loss(-) for the period/year (8+12) | — |
| 14 | 211 | Other comprehensive income(+)/loss(-) [header] | — |
| 14-sub | 212 | Items that will not be reclassified to profit or loss [subheader] | — |
| 14a | 213 | Remeasurements of defined benefit liability — Continued Operations | — |
| 14b | 214 | Remeasurements of defined benefit liability — Discontinued Operations | OCR_ARTIFACT ("Remeasurements OR defined benefit liability" — "or" for "of"); nil in current quarter and 30 June 2025 column |
| 15 | 215 | Other comprehensive income(+)/loss(-), net of tax | — |
| 16 | 216 | Total comprehensive income(+)/loss(-) for the period/year (13+/-15) | — |
| 17 | 217-218 | Paid-up equity share capital (Face value per share ₹10) | — |
| 18 | 219 | Other equity as per audited balance sheet | ZERO_STANDING (dash in all 3 quarter columns; 4,765.4 only in FY26 annual column — canonical annual-only template line) |
| 19 | 220 | Earning per share (EPS) [header] | — |
| 19a | 221 | Basic and diluted EPS (₹) (not annualised) from continuing operations | — |
| 19b | 222 | Basic and diluted EPS (₹) (not annualised) from discontinued operations | — |
| 19c | 223-224 | Basic and diluted EPS (₹) (not annualised) from continuing operations and discontinued operations | — |

Standalone P&L line-item count: **40**.

## TABLE 7 — STANDALONE NOTES (page 4), plus embedded discontinued-ops detail table

| Note | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 230-232 | "The unaudited Standalone financial results have been prepared in accordance with the recognition and measurement principles..." | — |
| 2(i) | 234-244 | "On 18 September 2025, the Board of Directors of the Company have approved the Scheme of Arrangement and Demerger..." — JSW Energy demerger of Durgapur facility, held-for-sale/discontinued-ops classification | material subsequent event; depreciation on tangible assets discontinued effective 18 Sep 2025 |
| 2(ii) | 247-265 | "Brief detail of results of discontinued operations for the quarter ended 30 June 2026 are given as under:" — embedded table, see rows below | — |
| 2(ii)-row1 | 257 | Total Income (discontinued ops detail table) | — |
| 2(ii)-row2 | 258 | Total Expenses (discontinued ops detail table) | — |
| 2(ii)-row3 | 259 | Profit(+)/Loss(-) from discontinued operations including internal revenue | — |
| 2(ii)-row4 | 260 | Less: Internal revenue | — |
| 2(ii)-row5 | 262 | Profit(+/Loss(-) from discontinued operations before exceptional items | — |
| 2(ii)-footnote | 264-265 | "Revenue from operations of the Durgapur undertaking is only from internal billing to the Company..." | unmarked footnote (no asterisk in standalone version, contrast Table 9 consolidated equivalent which does carry a bullet marker) |
| 3 | 266-271 | "On 21 November 2025, the Government of India notified the four Labour Codes - The Code on Wages, 2019..." — additional labour-code provision of ₹425.7 million (incl. ₹150.0 million discontinued ops) taken in FY26, presented as Exceptional item | — |
| 4 | 273-281 | "During the previous year, GE Power India Limited ('the Company' or 'GEPIL') executed, along with other GE Vernova entities, a settlement agreement..." — BHEL settlement, ₹3,400 million agreed, ₹3,430.6 million received FY26 incl FX translation impact | — |
| 5 | 283-286 | "Chief Operating Decision maker of the Company is the Managing Director, along with the Board of Directors, performs a detailed review..." — single operating segment (Power Generation equipment and related services) | — |
| 6 | 288-290 | "The above Standalone financial results have been reviewed by the Audit Committee and have been approved by the Board..." | — |
| 7 | 292-294 | "The unmodified report of the Statutory Auditor is being filed with BSE Limited and National Stock Exchange..." | — |
| 8 | 296-297 | "Figures for the quarter ended 31 March 2026 are the balancing figures between audited figures in respect of full financial year..." | — |

Standalone notes count: **8** numbered notes (note 2 has two sub-parts); embedded
discontinued-ops table adds 5 further line-item rows (counted in Table 6's parent total below).

## TABLE 8 — CONSOLIDATED STATEMENT OF FINANCIAL RESULTS (page 7), line items

| Item | Line(s) | Label | Flags |
|------|---------|-------|-------|
| 1 | 428 | Revenue from operations | — |
| 2 | 429 | Other income | — |
| 3 | 431 | Total income (1+2) | — |
| 4 | 433 | Expenses [header] | — |
| 4a | 434 | Cost of material and erection services | — |
| 4b | 435 | Changes in work in progress | — |
| 4c | 436 | Employee benefits expense | — |
| 4d | 437 | Finance costs | — |
| 4e | 438 | Depreciation and amortisation expense | — |
| 4f | 439 | Other expenses | — |
| 4-total | 440 | Total expenses (4) | — |
| 5 | 441-442 | Profit(+/Loss(-) before exceptional Items and profit on Joint Venture from continuing operations (3-4) | — |
| 6 | 443 | Share of profit of Joint Venture (net of tax) | — |
| 7 | 444-446 | Profit(+)/Loss(-) before exceptional items from continuing operations (5+6) | — |
| 7-exceptional | 447 | Exceptional items [refer note 4] | ZERO_STANDING (nil in quarter columns; -275.7 only in FY26 annual column); FORMATTING_GAP — row shows only 3 numeric tokens where 4 are expected (likely a dropped dash for the 31 Mar 2026 quarter column in extraction), verify against source PDF |
| 8 | 448 | Profit(+)/Loss(-) before Tax from continuing operations | OCR_ARTIFACT (bullet "•" substituted for minus sign in "Loss(•)") |
| 9 | 449 | Tax expense (+)/Tax credit (-) [header] | — |
| 9-1 | 450 | Current tax | — |
| 9-2 | 451 | Deferred tax charge/(credit) | ZERO_STANDING (dash in all 4 periods) |
| 10 | 452 | Net Profit(+)/Loss(-) after tax from continuing operations (8-9) | — |
| 11 | 453 | Discontinued operations [header] | — |
| 11-profit | 454-456 | Profit(+/Loss(-) from discontinued operations before exceptional items [refer note 3(i) and 3(ii)] | — |
| 11-exceptional | 457 | Exceptional items [refer note 4] | ZERO_STANDING (nil in quarter columns; -150.0 only in FY26 annual column) |
| 12 | 458 | Profit(+)/Loss(-) before tax from discontinued operations | — |
| 13 | 459 | Tax expense (+)/Tax credit (-) [header] | — |
| 13-1 | 460 | Current tax | ZERO_STANDING (dash in all 4 periods) |
| 13-2 | 461 | Deferred tax charge/(credit) | ZERO_STANDING (dash in all 4 periods) |
| 13-3 | 462 | Tax adjustments related to earlier years | ZERO_STANDING (dash in all 3 quarter columns; -0.6 only in FY26 annual column) |
| 14 | 463 | Net Profit(+)/Loss(-) after tax from discontinued operations (12-13) | — |
| 15 | 464 | Net Profit(+)/Loss(-) for the period/year (10+14) | — |
| 16 | 465 | Other comprehensive income(+)/loss(-) [header] | — |
| 16-sub | 466 | Items that will not be reclassified to profit or loss [subheader] | — |
| 16a | 467 | a) Remeasurements of defined benefit liability — Continued Operations | — |
| 16a-ii | 468 | Remeasurements of defined benefit liability — Discontinued Operations | dash in current quarter and 30 June 2025 column (30 June 2025 value cell appears blank in extraction — FORMATTING_GAP, verify against source) |
| 16b | 469 | b) Share of other comprehensive income(+)/loss(-) of Joint Venture | — |
| 16b-tax | 470 | Income tax relating to above | ZERO_STANDING (dash in all 4 periods — fully zero template line) |
| 17 | 471 | Other comprehensive income(+)/loss(-), net of tax | — |
| 18 | 472 | Total comprehensive income(+)/loss(-) for the period/year (15+/-17) | — |
| 19 | 473-474 | Paid-up equity share capital (Face value per share ₹10) | — |
| 20 | 475 | Other equity as per audited balance sheet | ZERO_STANDING (dash in all 3 quarter columns; 5,153.1 only in FY26 annual column — canonical annual-only template line) |
| 21 | 476 | Earning per share (EPS) [header] | — |
| 21a | 477 | Basic and diluted EPS (₹) (not annualised) from continuing operations | — |
| 21b | 478 | Basic and diluted EPS (₹) (not annualised) from discontinued operations | — |
| 21c | 479-480 | Basic and diluted EPS (₹) (not annualised) from continuing operations and discontinued operations | — |

Consolidated P&L line-item count: **44**.

## TABLE 9 — CONSOLIDATED NOTES (page 8), plus embedded discontinued-ops detail table

| Note | Line(s) | First ~15 words | Flags |
|------|---------|------------------|-------|
| 1 | 486-487 | "The unaudited Consolidated financial results include results of GE Power India Ltd. ('the Holding Company') and its subsidiary..." | NOTE_NUMBERING_GAP — no leading numeral visible in extraction (see Methodology Note); functionally note 1 |
| 2 | 489-491 | "The unaudited Consolidated financial results have been prepared in accordance with the recognition and measurement principles..." | — |
| 3(i) | 492-502 | "On 18 September 2025, the Board of Directors of the Company have approved the Scheme of Arrangement and Demerger..." — JSW Energy demerger, consolidated version of standalone note 2(i) | material subsequent event |
| 3(ii) | 505-523 | "Brief detail of results of discontinued operations for the quarter ended 30 June 2026 are given as under:" — embedded table, see rows below | — |
| 3(ii)-row1 | 515 | Total Income (discontinued ops detail table) | — |
| 3(ii)-row2 | 516 | Total Expenses (discontinued ops detail table) | — |
| 3(ii)-row3 | 517 | Profit(+)/Loss(-) from discontinued operations including internal revenue | — |
| 3(ii)-row4 | 518 | Less: Internal revenue | OCR_ARTIFACT ("(247,0)" comma for decimal point) |
| 3(ii)-row5 | 520 | Profit(+/Loss(-) from discontinued operations before exceptional items | — |
| 3(ii)-footnote | 522-523 | "• Revenue from operations of the Durgapur undertaking is only from internal billing to the Company..." | bullet-marked footnote (contrast standalone equivalent, Table 7, which is unmarked) |
| 4 | 525-530 | "On 21 November 2025, the Government of India notified the four Labour Codes - The Code on Wages, 2019..." — consolidated version of standalone note 3 | — |
| 5 | 532-540 | "During the previous year, GE Power India Limited ('the Company' or 'GEPIL') executed, along with other GE Vernova entities, a settlement agreement..." — consolidated version of standalone note 4 (BHEL settlement) | — |
| 6 | 542-545 | "Chief Operating Decision maker of the Company is the Managing Director, along with the Board of Directors, performs a detailed review..." — single operating segment, Group level | — |
| 7 | 546-548 | "The above Consolidated financial results have been reviewed by the Audit Committee and have been approved by the Board..." | — |
| 8 | 549-551 | "The unmodified report of the Statutory Auditor is being filed with BSE Limited and National Stock Exchange..." | — |
| 9 | 552-553 | "Figures for the quarter ended 31 March 2026 are the balancing figures between audited figures in respect of full financial year..." | — |

Consolidated notes count: **9** numbered notes (note 3 has two sub-parts; note 1's numeral is
missing in extraction, see flag above); embedded discontinued-ops table adds 5 further
line-item rows.

## TABLE 10 — MEDIA RELEASE (page 9)

| # | Unit | Line(s) | Content | Flags |
|---|------|---------|---------|-------|
| 1 | Headline | 570 | "GE Power India Ltd (GEPIL) reports Q1 FY 2026-27 Results" | — |
| 2 | Bullet — Total income | 576-577 | Total income continuing ops INR 3,405.7 million, up 0.2% vs INR 3,398.3 million Q1FY26 | — |
| 3 | Bullet — Profit before tax | 579-580 | PBT and exceptional items continuing ops INR 688.2 million vs INR 440.2 million Q1FY26 | — |
| 4 | Bullet — Profit after tax | 582-583 | PAT (incl. exceptional items) INR 525.5 million vs INR 316.1 million Q1FY26 | — |
| 5 | Bullet — EBITDA margin | 585-587 | EBITDA before exceptional items, continuing ops, 22.5% vs 15.6% Q1FY26 | — |
| 6 | Bullet — Order backlog | 590-592 | Order backlog INR 15,454 million, down 41.4% vs INR 26,353 million Q1FY26, "driven by termination of two FGD EP contracts, Jaypee Bina and Nigrie amounting to INR 7,749 million" | — |
| 7 | MD quote | 594-604 | Puneet Bhatla, Managing Director — qualitative commentary on strategic transformation, margin improvement, portfolio mix, no numbers cited within the quote itself | — |
| 8 | About-company paragraph + press contact | 606-621 | Company boilerplate description; contact Kanika Arora, Communications Lead South Asia | — |

Media release content-unit count: **8**.

---

## FLAGS SUMMARY (all instances)

- `ZERO_STANDING` (15 instances): standalone lines 193, 197, 203, 206, 207, 208, 219;
  consolidated lines 447, 451, 457, 460, 461, 462, 470, 475.
- `OCR_ARTIFACT` (5 instances): line 176 (".1" for "1"), line 190 (bullet for minus), line 214
  ("or" for "of"), line 448 (bullet for minus), line 518 (comma for decimal point).
- `NOTE_NUMBERING_GAP` (1 instance): consolidated note 1, line 486 (no visible numeral).
- `FORMATTING_GAP` (2 instances): line 447 (consolidated exceptional items row appears to be
  missing one numeric token), line 468 (consolidated OCI discontinued-ops remeasurement row,
  30 June 2025 column appears blank).
- `NO_PRIOR_LEDGER` (applies filing-wide): entity add/remove/rename cross-check (Table 5) and
  any quarter-over-quarter diff cannot be performed this cycle; no prior quarterly ledger
  exists for GVPIL.
- No `MGMT_ABSENCE`, `REPEAT_QUESTION`, `DROPPED_SLIDE`, or `ENTITY_CHANGE` — not applicable
  to this doctype/quarter (results filing, no prior ledger, no concall/deck in this extract).

---

```yaml
stage: A2-enumerator
company: "GVPIL"
quarter: "Q1FY27"
doctype: "results"
model: claude-sonnet-5
status: complete
ledger_path: "runs/gvpil-q1fy27/work/ledger_results_gvpil_q1fy27.md"
counts:
  notes: 17
  line_items: 94
  zero_standing: 15
  agenda_items: 2
  auditor_paras: 10
  entities: 2
  signature_blocks: 5
  media_release_items: 8
  turns: 0
  questions: 0
  mgmt_numbers: 0
  slides: 0
  slide_numbers: 0
flags_raised: [ZERO_STANDING, OCR_ARTIFACT, NOTE_NUMBERING_GAP, FORMATTING_GAP, NO_PRIOR_LEDGER]
gate_a2: pass
mismatch_note: ""
```
