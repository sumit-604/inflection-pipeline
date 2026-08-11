# A2 COMPLETENESS LEDGER — ZEEL Q1 FY27 Results Filing

Source: `extract_results_zeel_q1fy27.txt` (30 pages, 1616 content lines, Millions,
x0.1 to Rs Crores). Line numbers cited below are the A1 extract's own embedded
line numbers (first tab-delimited field of each content line), not Read-tool
line numbers.

```
=== A2 COUNT TEST ===
category: agenda_items            grep_count: 8    sweep_count: 8    match: yes
category: notes_standalone        grep_count: 15   sweep_count: 15   match: yes
category: notes_consolidated      grep_count: 17   sweep_count: 17   match: yes
category: notes_total             grep_count: 32   sweep_count: 32   match: yes
category: line_items_standalone   grep_count: 33   sweep_count: 33   match: yes
category: line_items_consolidated grep_count: 46   sweep_count: 46   match: yes
category: line_items_total        grep_count: 79   sweep_count: 79   match: yes
category: review_reports          grep_count: 2    sweep_count: 2    match: yes
category: auditor_paras_standalone   grep_count: 6    sweep_count: 6    match: yes
category: auditor_paras_consolidated grep_count: 9    sweep_count: 9    match: yes
category: entities                grep_count: 25   sweep_count: 25   match: yes
category: annexure_a_profiles     grep_count: 6    sweep_count: 6    match: yes
gate_a2: pass
=== END COUNT TEST ===
```

Method note on notes reconciliation: standalone/consolidated note numerals
were recovered via three overlapping grep passes (explicit `N.` markers,
bare `NN` + text markers, and `a)/b)/c)` sub-item markers) plus a manual
paragraph-boundary sweep, cross-anchored against the auditor's own explicit
citations (Note 7 = SEBI Section 206(5) investigation, Note 9 = Jiostar
dispute, Note 15/17 = balancing figures). Every note in both sections has a
numeral either printed, printed as a bare number, or inferable unambiguously
from sequential position between two anchored numbers. Flagged `NUM_LOST`
below where the printed numeral did not survive extraction.

---

## 1. BOARD OUTCOME LETTER — AGENDA ITEMS (8 items, lines 20-61)

Board Meeting: commenced 1.45 p.m., concluded 4:15 p.m. (line 67) — ~2.5 hour
meeting. Digital signature by Company Secretary Ashish Ramesh Agarwal
timestamped 2026.08.10 16:35:34 (line 93) — 20 minutes AFTER meeting
concluded (4:15 p.m.); no `SIGNATURE_BEFORE_CONCLUSION` flag warranted.

| # | Line | Agenda item | First 15 words | Flags |
|---|------|-------------|-----------------|-------|
| 1 | 20-29 | Approval of unaudited standalone & consolidated financial results Q1 FY27 | "the Unaudited Standalone and Consolidated Financial Results of the Company for the quarter ended June" — includes sub-items: enclosure of Limited Review Reports (23-25), authorization of Mr. Uttam Prakash Agarwal (Independent Director, Audit Committee Chairperson) to sign results (27-29) | — |
| 2 | 31-33 | Convening of 44th AGM on Thursday, 17 September 2026, via VC/OAVM | "convening of the 44th Annual General Meeting of the Company on Thursday, September 17, 2026" | — |
| 3 | 35-37 | Re-appointment of Vaibhav P Joshi & Associates as Cost Auditors, FY2026-27 | "re-appointment of Vaibhav P Joshi & Associates, Cost Accountants (Firm Registration No. 101329) as the" | — |
| 4 | 39-40 | Re-appointment of MGB & Co. LLP and CKSP & Co as Internal Auditors, FY2026-27 | "re-appointment of MGB & Co. LLP, Chartered Accountants and CKSP & Co, Chartered Accountants as the" | — |
| 5 | 42-45 | Re-appointment of Ms. Deepu Bansal (DIN 09497525) as Independent Director, 2nd term 13-Oct-2026 to 12-Oct-2031 | "re-appointment of Ms. Deepu Bansal (DIN: 09497525), upon the recommendation of Nomination and" | — |
| 6 | 47-50 | Re-appointment of Mr. Uttam Prakash Agarwal (DIN 00272983) as Independent Director, 2nd term 17-Dec-2026 to 16-Dec-2031 | "re-appointment of Mr. Uttam Prakash Agarwal (DIN: 00272983), upon the recommendation of Nomination" | — |
| 7 | 53-56 | Re-appointment of Dr. Venkata Ramana Murthy Pinisetti (DIN 03483544) as Independent Director, 2nd term 17-Dec-2026 to 16-Dec-2031 | "re-appointment of Dr. Venkata Ramana Murthy Pinisetti (DIN: 03483544), upon the recommendation of" | — |
| 8 | 58-61 | Re-appointment of Mr. Shishir Babubhai Desai (DIN 01453410) as Independent Director, 2nd term 17-Dec-2026 to 16-Dec-2031 | "re-appointment of Mr. Shishir Babubhai Desai (DIN: 01453410), upon the recommendation of Nomination" | — |

Ancillary disclosure referenced but not a numbered agenda item: preferential
issue / ESOP 2026 Regulation 30 disclosure enclosed as Annexure A (lines
63-65) — this is the Warrants/ESOP matter approved by the Board on 1 July
2026 and by shareholders in the EGM of 31 July 2026 (see Note 11, both
notes tables); it is NOT a resolution of this Board meeting (results
meeting), only a disclosure annexure — enumerated separately under
Annexure A below. Not double counted in the 8 agenda items.

---

## 2. NOTES TO STANDALONE FINANCIAL RESULTS (15 notes, lines 315-654)

| Note | Line(s) | First 15 words | Flags |
|------|---------|-----------------|-------|
| 1 | 316-318 | "The above standalone financial results have been reviewed and recommended by the Audit Committee" (board approval / limited review boilerplate) | `NUM_LOST` — no numeral printed |
| 2 | 320-325 | "The above standalone financial results have been prepared in accordance with the recognition and" (Ind AS 34 basis of preparation) | `NUM_LOST` |
| 3 | 327-340 | "The Company had provided commitments for funding shortfalls in Debt Service Reserve Account (DSRA" — Siti Networks Ltd (SNL) DSRA guarantee; IDBI Bank Section 7 IBC petition (6-Sep-2025); IRP admission of ZEEL's operational creditor claim | `NUM_LOST` |
| 4 | 342-375 | "The Company in May 2016 had issued a Letter of Comfort (LOC) to the Yes Bank Limited" — ATL Media Ltd support LOC; Bombay HC plaint (26-Jun-2020) dismissed at ad-interim stage; primary suit still pending | `NUM_LOST` |
| 5 | 377-383 | "a) Exceptional item for the year ended 31 March 2026, includes restructuring cost" (a: Rs 94mn restructuring, FY26); "b) Current tax expense provision ... includes credit of Rs. 969 million" (Margo investment write-off tax credit) | `NUM_LOST` — parent numeral absent; only a)/b) sub-markers present; cross-referenced by table row "Exceptional items (Refer note 5(a))" line 285 |
| 6 | 385-402 | "a) Pursuant to the Board approval dated 17 April 2026, the Company has invested and subscribed" (CCDs in Phantom Digital Effects Ltd, Rs 1,157mn); "b) ... invested Rs. 100 million" (CCPS in Culture of Real Experiences Pvt Ltd, 33.33% stake); "c) ... sold and transferred the business" (slump sale to ZI-IPR Enterprises Ltd, net assets Rs 4,902mn) | `NUM_LOST` — parent numeral absent; cross-referenced by table row "Operational cost (Refer note 10)" is a DIFFERENT note (10), not this one |
| 7 | 404-505 | "The Securities and Exchange Board of India ("SEBI") had passed an ex-parte interim order dated 12 June 2023" — Section 206(5) MCA investigation, Investigation Committee report (no material irregularities), multiple SEBI SCNs, SEBI order 31-Jul-2026 imposing Rs 3mn penalty + 2-month market access restraint, SAT appeal filed | `NUM_LOST`; anchor: explicitly cited as "Note 7" by auditor at line 170 |
| 8 | 506-517 | "In its meeting, held on 16 July 2024, the Board had approved issuance of 5% coupon unsecured, unlisted" — FCCBs USD 239mn approved, USD 23.90mn issued; redemption approved 26-Mar-2026, completed subsequent to quarter-end | `NUM_LOST` |
| 9 | 519-593 | "On 26 August 2022, the Company had entered into an agreement with Jiostar India Private Limited" — Alliance Agreement dispute, LCIA arbitration, JioStar damages claim increased to USD 1.097 billion this quarter, final evidentiary hearing completed subsequent to quarter-end | `NUM_LOST`; anchor: explicitly cited as "Note 9" by auditor at line 197 |
| 10 | 595-599 | "During quarter ended 31 March 2026, the Company had revised its estimates of recording consumption of" — premiere movie inventory revision, Rs 3,022mn additional charge to Operational cost | explicit numeral printed |
| 11 | 601-616 | ". On 1 July 2026, the Board of Directors of the Company approved issue of up to 24,94,85,563" — Warrants to Promoter Group at Rs 126/share, Rs 31,435mn aggregate; ESOP grant of 37,422,835 options; EGM approval 31-Jul-2026; text ends "(Also Refer Note 7)" | `NUM_LOST` (blank-dot artifact where "11" should print); internal cross-reference to "Note 7" at line 627 is anomalous — Note 7 in this document is the SEBI investigation note, not a Warrants/ESOP note — flag `CROSS_REF_ANOMALY` for A3 |
| 12 | 629-636 | "During an earlier year, the Company had received show cause cum demand notice (SCN) from Indirect Tax" — GST input tax credit dispute, Rs 1,736mn, Adjudicating Authority upheld demand, appeal filed | explicit numeral printed |
| 13 | 638-648 | "In an earlier year, Zee Studio Limited, a subsidiary had been allotted plot of land on lease for the purpose of" — RIICO Jaipur land lease cancellation, writ petition at Rajasthan HC | explicit numeral printed |
| 14 | 650 | ". Figures for the previous year/period have been regrouped and/or reclassified wherever considered necessary." | `NUM_LOST` (blank-dot artifact) |
| 15 | 652-654 | "The figures for the quarter ended 31 March 2026 are the balancing figures between the audited figures in" | explicit numeral printed (no period, but "15" printed); anchor: explicitly cited as "Note 15" by auditor at line 229 |

---

## 3. NOTES TO CONSOLIDATED FINANCIAL RESULTS (17 notes, lines 1024-1436)

| Note | Line(s) | First 15 words | Flags |
|------|---------|-----------------|-------|
| 1 | 1026-1029 | "The above consolidated financial results have been reviewed and recommended by the Audit Committee" | explicit numeral printed |
| 2 | 1031-1036 | "The above consolidated financial results have been prepared in accordance with the recognition and" | explicit numeral printed |
| 3 | 1038-1053 | "The Company had provided commitments for funding shortfalls in Debt Service Reserve Account (DSRA" — same SNL DSRA / IDBI IBC matter as standalone Note 3 | explicit numeral printed |
| 4 | 1055-1123 | "ATL Media Limited (ATL), an overseas wholly owned subsidiary of the Company incorporated in Mauritius" — Put Option dispute with LEL, Supreme Court of Mauritius ruling (28-Feb-2025) in Company's favour, Yes Bank IBU claim against LEL/ATL filed in English Court this quarter (30-Jun-2026) | explicit numeral printed; `CONSOL_ONLY` — no equivalent note in standalone set (standalone Note 4 covers a related but distinct LOC-to-Yes-Bank angle, not this Put Option litigation detail) |
| 5 | 1124-1132 | "a) Exceptional item for the year ended 31 March 2026, includes restructuring cost" / "b) Current tax expense provision ... credit of Rs. 969" | `NUM_LOST` — only a)/b) sub-markers present |
| 6 | 1134-1159 | "a) Pursuant to the Board approval dated 17 April 2026 ... CCDs" / "b) ... Rs. 100 million" CCPS / "c) ... slump sale" to ZI-IPR; adds "Since the transactions are with parties under common control, there is no impact on the consolidated financial results" | `NUM_LOST` |
| 7 | 1170-1253 | "The Securities and Exchange Board of India ("SEBI") had passed an ex-parte interim order dated 12 June" — same Section 206(5) investigation / SEBI SCNs as standalone Note 7, Group-level language | `NUM_LOST`; anchor: explicitly cited as "Note 7" by auditor at line 743 |
| 8 | 1255-1266 | "In its meeting, held on 16 July 2024, the Board had approved issuance of 6% coupon unsecured, unlisted" — FCCB note; coupon printed as "6%" here vs "5%" in standalone Note 8 line 506 (same instrument) | `NUM_LOST`; `DATA_INCONSISTENCY` — coupon rate differs from standalone Note 8 (5% vs 6%), flag for A3/A5 arithmetic-consistency check |
| 9 | 1268-1362 | "On 26 August 2022, the Company had entered into an agreement with Jiostar India Private Limited" — same Alliance Agreement/arbitration dispute, Group-level language | `NUM_LOST`; anchor: explicitly cited as "Note 9" by auditor at line 783 |
| 10 | 1364-1368 | "During quarter ended 31 March 2026, the Company had revised its estimates of recording consumption of" — same premiere-movie inventory revision, Rs 3,022mn | explicit numeral printed |
| 11 | 1370-1388 | ". On 1 July 2026, the Board of Directors of the Company approved issue of up to 24,94,85,563" — same Warrants/ESOP matter; also ends "(Also Refer Note 7)" | `NUM_LOST` (blank-dot artifact); same `CROSS_REF_ANOMALY` as standalone Note 11 |
| 12 | 1390-1398 | "During an earlier year, the Company had received show cause cum demand notice (SCN) from Indirect" — same GST dispute | explicit numeral printed |
| 13 | 1400-1421 | "In an earlier year, Zee Studio Limited, a subsidiary had been allotted plot of land on lease for the purpose" — RIICO Jaipur lease; adds that the Group's statutory auditors put an Emphasis of Matter on this note for the current quarter (lines 1419-1421) | explicit numeral printed; anchor: explicitly cited by auditor at line 801 (EOM paragraph, para 6 of consolidated review report) |
| 14 | 1423-1424 | "The Group operates in a single reporting segment namely 'Content and Broadcasting' and therefore there" | explicit numeral printed; `CONSOL_ONLY` — segment reporting note, no standalone equivalent |
| 15 | 1426-1428 | "The standalone financial results for the quarter ended 30 June 2026 are available on the Company's" | explicit numeral printed; `CONTENT_ANOMALY` — a note under the header "Notes to consolidated financial results" whose text refers to standalone results website availability; likely a template/copy-paste artifact, flag for A3 |
| 16 | 1430-1431 | "Figures for the previous year/period have been regrouped and/or reclassified wherever considered" | explicit numeral printed |
| 17 | 1433-1435 | "The figures for the quarter ended 31 March 2026 are the balancing figures between the audited figures in" | explicit numeral printed; anchor: explicitly cited as "Note 17" by auditor at line 869 |

---

## 4. STANDALONE FINANCIAL RESULTS TABLE — LINE ITEMS (33 rows, lines 272-306)

Columns: Qtr 30-Jun-26 (Unaudited) / Qtr 31-Mar-26 (Unaudited, Refer Note 15) /
Qtr 30-Jun-25 (Unaudited) / Year 31-Mar-26 (Audited). Units Rs Millions.

| # | Line | Item | 30-Jun-26 | 31-Mar-26(Q) | 30-Jun-25 | 31-Mar-26(Y) | Flags |
|---|------|------|-----------|--------------|-----------|--------------|-------|
| 1 | 272 | 1. Revenue from operations | 17,809 | 18,867 | 16,820 | 75,670 | — |
| 2 | 273 | 2. Other income | 21 | 242 | 187 | 764 | — |
| 3 | 274 | Total income [1+2] (subtotal) | 18,030 | 19,109 | 17,026 | 76,434 | — |
| 4 | 275 | 3. Expenses (header) | — | — | — | — | header row, no values |
| 5 | 276 | (a) Operational cost (Refer note 10) | 9,860 | 14,770 | 9,574 | 47,990 | — |
| 6 | 277 | (b) Employee benefits expense | 1,774 | 1,563 | 1,883 | 7,004 | `OCR_GARBLE` printed "(o)" |
| 7 | 278 | (c) Finance costs | 129 | 136 | 72 | 20 | `OCR_GARBLE` printed "(¢)" |
| 8 | 279 | (d) Depreciation and amortisation expenses | 362 | 375 | 492 | 1,783 | — |
| 9 | 280 | (e) Fair value gain on financial instruments at FVTPL | (207) | (34) | (185) | (568) | `OCR_GARBLE` printed "(@)" |
| 10 | 281 | (f) Advertisement and publicity expenses | 2,257 | 4,130 | 2,531 | 13,388 | — |
| 11 | 282 | (g) Other expenses | 1,178 | 1,451 | 1,112 | 5,351 | `OCR_GARBLE` printed "(8)" |
| 12 | 283 | Total expenses [3(a) to 3(g)] (subtotal) | 17,353 | 22,391 | 15,479 | 75,458 | — |
| 13 | 284 | 4. Profit/(loss) before exceptional item and taxes [1+2-3] | 677 | (3,282) | 1,547 | 976 | — |
| 14 | 285 | 5. Exceptional items (Refer note 5(a)) | (blank) | - | (blank) | (94) | `ZERO_STANDING` — dash/blank in 3 of 4 periods |
| 15 | 286 | 6. Profit/(loss) before tax [4+5] | 677 | (3,282) | 1,547 | 882 | — |
| 16 | 287 | 7. Tax expense (header) | — | — | — | — | header row |
| 17 | 288 | (a) Current tax | 177 | (1,229) | 400 | 57 | — |
| 18 | 289 | (b) Current tax - earlier years | - | 49 (OCR "a9") | - | 49 | `ZERO_STANDING` dash in 2 of 4; `OCR_GARBLE` "a9" |
| 19 | 290 | (c) Deferred tax | 27 | (293) | 32 | (429) | — |
| 20 | 291 | Total tax expense [7(a)+7(b)+7(c)] (subtotal) | 204 | (1,473) | garbled "a3" | (323) | `OCR_GARBLE` value illegible for 30-Jun-25 column |
| 21 | 292 | 8. Profit/(loss) for the period/year [6-7] | 473 | (1,809) | 1,115 | 1,205 | — |
| 22 | 293 | 9. Other comprehensive (loss)/income (header) | — | — | — | — | header row |
| 23 | 294 | Items that will not be reclassified to P&L (subheader) | — | — | — | — | subheader, no values |
| 24 | 295 | (a)(i) Re-measurement of defined benefit obligation | (43) | 38 | (13) | 121 | — |
| 25 | 296-297 | (a)(ii) Fair value changes of equity instruments through OCI | - | 124 | - | 124 | `ZERO_STANDING` dash in 2 of 4 |
| 26 | 298-299 | (b) Income-tax relating to items not reclassified | 11 | (40) | 3 | (61) | — |
| 27 | 300 | Total other comprehensive (loss)/income [9(a) to 9(b)] (subtotal) | (32) | 122 | (10) | 184 | — |
| 28 | 301 | 10. Total comprehensive income/(loss) [8+9] | 441 (OCR "a1") | (1,687) | 1,105 | 1,389 | `OCR_GARBLE` current-qtr value printed "a1" |
| 29 | 302 | 11. Paid-up Equity share capital (FV Re 1/-) | 961 | 961 | 961 | 961 | — |
| 30 | 303 | 12. Other equity | (blank) | (blank) | (blank) | 104,671 | `ZERO_STANDING` — blank in 3 of 4 periods (standard, balance-sheet item reported year-end only) |
| 31 | 304 | 13. Earnings per share (not annualised) (header) | — | — | — | — | header row |
| 32 | 305 | Basic (₹) | 0.49 | (1.88) | 1.16 | 1.25 | — |
| 33 | 306 | Diluted (₹) | 0.49 | (1.88) | 1.16 | 1.25 | — |

---

## 5. CONSOLIDATED FINANCIAL RESULTS TABLE — LINE ITEMS (46 rows, lines 960-1010)

Columns: Qtr 30-Jun-26 (Unaudited) / Qtr 31-Mar-26 (Unaudited, Refer Note 17) /
Qtr 30-Jun-25 (Unaudited) / Year 31-Mar-26 (Audited). Units Rs Millions.

| # | Line | Item | 30-Jun-26 | 31-Mar-26(Q) | 30-Jun-25 | 31-Mar-26(Y) | Flags |
|---|------|------|-----------|--------------|-----------|--------------|-------|
| 1 | 960 | 1. Revenue from operations (header) | — | — | — | — | header row |
| 2 | 961 | (a) Advertisement revenue | 6,714 | 8,080 | 7,585 | 32,243 | — |
| 3 | 962 | (b) Subscription revenue | 11,369 | 10,247 | 9,817 | 40,796 | — |
| 4 | 963 | (c) Other sales and services | 990 | 1,921 | 846 | 7,950 | — |
| 5 | 964 | 2. Other income | 312 | 763 | 250 | 1,461 | — |
| 6 | 965 | Total income [1(a) to 1(c)+2] (subtotal) | 19,385 | 21,011 | 18,498 | 82,450 | — |
| 7 | 966 | 3. Expenses (header) | — | — | — | — | header row |
| 8 | 967 | (a) Operational cost (Refer note 10) | 10,317 | 15,048 | 9,710 | 48,594 | — |
| 9 | 968 | (b) Employee benefits expense | 2,126 | 1,920 | 2,201 | 8,424 | — |
| 10 | 969 | (c) Finance costs | 132 | 149 | 77 | 448 | — |
| 11 | 970 | (d) Depreciation and amortisation expense | 435 | 473 | 591 | 2,372 (OCR "2372") | — |
| 12 | 971-972 | (e) Fair value gain on financial instruments at FVTPL | (207) | (138) | (109) | (524) | `OCR_GARBLE` label printed "fsl:air value gain" |
| 13 | 973 | (f) Advertisement and publicity expenses | 4,468 | 4,324 | 2,752 | 14,251 | — |
| 14 | 974 | (g) Other expenses | 1,373 | 1,642 | 1,305 | 6,257 | — |
| 15 | 975 | Total expenses [3(a) to 3(g)] (subtotal) | 18,644 | 23,418 | 16,527 | 79,622 | — |
| 16 | 976-977 | 4. Profit/(loss) before share of profit of JV & associate, exceptional item and taxes [1+2-3] | 781 (OCR "781") | garbled "2aozy" | 21? garbled | 4,828 (OCR "4828") | `OCR_GARBLE` — 31-Mar-26(Q) and 30-Jun-25 values illegible |
| 17 | 978 | 5. Share of profit of joint venture and associate | 0 | 0 | 1 | 2 | `ZERO_STANDING` — nil in 2 of 4 periods |
| 18 | 979 | 6. Profit/(loss) before exceptional items and tax [4+5] | 741 | (2,407) | 1,972 | 2,830 | — |
| 19 | 980 | 7. Exceptional items (Refer note 5(a)) | - | - | garbled "»" | (94) | `ZERO_STANDING` dash in 3 of 4 |
| 20 | 981 | 8. Profit/(loss) before tax [6+7] | 741 | (2,407) | 1,972 | 2,736 | — |
| 21 | 982 | 9. Tax expense (header) | — | — | — | — | header row |
| 22 | 983 | (a) Current tax | 255 | (1,151) | 473 | 375 | — |
| 23 | 984 | (b) Current tax - earlier years | (289) | 19 | - | 19 | `ZERO_STANDING` dash in 1 of 4 |
| 24 | 985 | (c) Deferred tax | 32 | (268) | 62 | (401) | — |
| 25 | 986 | Total tax expense [9(a)+(b)+(c)] (subtotal) | (2) | (1,370) | 535 | 23 | — |
| 26 | 987 | 10. Profit/(loss) for the period/year [8-9] | 743 | (1,037) | 1,437 | 2,713 | — |
| 27 | 988 | 11. Other comprehensive (loss)/income (header) | — | — | — | — | header row |
| 28 | 989 | (A) Items that will not be reclassified to P&L (subheader) | — | — | — | — | subheader |
| 29 | 990 | (a)(i) Re-measurement of defined benefit obligation | (44)? (OCR "(a4)") | 38 | (13) | 120 | `OCR_GARBLE` current-qtr value |
| 30 | 991-992 | (a)(ii) Fair value changes of equity instruments through OCI | garbled "." | garbled "i" | garbled "i" | garbled "i3" | `OCR_ILLEGIBLE` all 4 values unreadable — likely dash/nil across the board (matches standalone counterpart pattern), needs source-doc confirmation, `ZERO_STANDING` suspected |
| 31 | 993 | (b) Income-tax relating to items not reclassified | 11 | (41) | 3 | (62) | — |
| 32 | 994 | (B) Items that will be reclassified to P&L (subheader) | — | — | — | — | subheader |
| 33 | 995-996 | (a) Exchange differences on translation of foreign operations | 166 | 638 | 142 | 1,404 | — |
| 34 | 997 | Total other comprehensive income [11(A)+11(B)] (subtotal) | 133 | 759 | 132 | 1,586 | — |
| 35 | 998 | 12. Total comprehensive income/(loss) [10+11] | 876 | (278) | 1,569 | 4,299 | — |
| 36 | 999 | 13. Profit/(loss) for the period/year attributable to (header) | — | — | — | — | header row |
| 37 | 1000 | Shareholders of the Company | 763 | (1,024) | 1,437 | 2,731 | — |
| 38 | 1001 | Non-controlling interests | (20) | (13) | - | (18) | `ZERO_STANDING` dash in 1 of 4 |
| 39 | 1002 | 14. Total comprehensive income/(loss) attributable to (header) | — | — | — | — | header row |
| 40 | 1003 | Shareholders of the Company | 896 | (265) | 1,569 | 4,317 | — |
| 41 | 1004 | Non-controlling interests | (20) | (13) | - | (18) | `ZERO_STANDING` dash in 1 of 4 |
| 42 | 1005 | 15. Paid-up equity share capital (FV Re 1/-) | 961 | 961 | 961 | 961 | — |
| 43 | 1006 | 16. Other equity | (blank) | (blank) | (blank) | 116,338 | `ZERO_STANDING` blank in 3 of 4 (balance-sheet item, year-end only) |
| 44 | 1007 | 17. Earnings per share (not annualised) (header) | — | — | — | — | header row |
| 45 | 1008 | Basic (₹) | **MISSING** | (1.08) | 1.50 | 2.82 | `MISSING_VALUE` — 30-Jun-26 (current quarter) column absent from extracted table, unlike every other row which reports all 4 periods; flag for A3/A5 |
| 46 | 1009 | Diluted (₹) | **MISSING** | (1.08) | 1.50 | 2.82 | `MISSING_VALUE` — same as above |

Footnote (not a line item, enumerated separately): line 1010 — "'0' (zero)
denotes amounts less than one million."

---

## 6. LIMITED REVIEW REPORTS (2 reports)

### 6a. Standalone Limited Review Report (lines 104-249), Walker Chandiok & Co LLP

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 122-126 | Scope: review of standalone financial results for quarter ended 30-Jun-2026 | — |
| 2 | 128-134 | Management responsibility / Ind AS 34 basis / auditor responsibility to express a conclusion | — |
| 3 | 136-144 | SRE 2410 review standard described; review is substantially less in scope than an audit; no audit opinion expressed | — |
| 4 | 146-152 | Conclusion: unmodified — nothing has come to attention indicating non-disclosure or material misstatement | opinion type: unmodified/unqualified |
| 5(a) | 168-196 | Emphasis of Matter — Note 7, SEBI Section 206(5) investigation, SCNs, SEBI order 31-Jul-2026 | `EOM` |
| 5(b) | 197-211 | Emphasis of Matter — Note 9, JioStar Alliance Agreement arbitration (LCIA), damages claim USD 1,097mn | `EOM` |
| 6 | 229-232 | Other Matter — Note 15, 31-Mar-2026 quarter figures are balancing figures between audited FY and unaudited 9M YTD, reviewed by this firm | Other Matter |
| — | 213 | "Our conclusion is not modified in respect of above-mentioned matters" (covers para 5a/5b) | — |
| Sign-off | 235-249 | Firm: Walker Chandiok & Co LLP, FRN 001076N/N500013; Partner Ashish Gupta, M.No. 504662; UDIN 26504662XBGACE8490; Place New Delhi; Date 10 August 2026 | — |

### 6b. Consolidated Limited Review Report (lines 685-889), Walker Chandiok & Co LLP

| Para | Line(s) | Content | Flags |
|------|---------|---------|-------|
| 1 | 687-693 | Scope: review of consolidated financial results incl. subsidiaries and joint venture per Annexure 1, quarter ended 30-Jun-2026 | — |
| 2 | 695-702 | Management responsibility / Ind AS 34 basis / auditor responsibility | — |
| 3 | 704-715 | SRE 2410 standard described; also performed procedures per Regulation 33(8) circular | — |
| 4 | 731-737 | Conclusion: unmodified | opinion type: unmodified/unqualified |
| 5(a) | 742-768 | EOM — Note 7, SEBI Section 206(5) investigation (Group-level) | `EOM` |
| 5(b) | 783-797 | EOM — Note 9, JioStar Alliance Agreement arbitration (Group-level) | `EOM` |
| 6 | 801-815 | EOM — Note 13, RIICO Jaipur land lease dispute, reproducing EOM of Zee Studios Limited's own auditors (review report dated 30-Jul-2026) | `EOM`; entity-level reliance |
| 7 | 817-824 | Other Matter — did not review 7 subsidiaries (2,443mn assets/relevant base, net profit 602mn); relied on other auditors' review reports | Other Matter; component auditor reliance |
| — | 839-852 | (continuation of para 7) 6 of the 7 subsidiaries located outside India, foreign-GAAP results converted to Ind AS by management, reviewed by other auditors under local standards | — |
| 8 | 853-866 | Other Matter — 9 subsidiaries (112mn base metric, net profit 14mn) and 1 joint venture (0mn) NOT reviewed by any auditor — unreviewed, management-furnished financial information, deemed not material to Group | Other Matter; `UNAUDITED_COMPONENTS` |
| 9 | 868-871 | Other Matter — Note 17, 31-Mar-2026 balancing figures | Other Matter |
| Sign-off | 874-888 | Firm: Walker Chandiok & Co LLP, FRN 001076N/N500013; Partner Ashish Gupta, M.No. 504662; UDIN 26504662BJPCWI1756; Place New Delhi; Date 10 August 2026 | UDIN differs from standalone report (correct — one UDIN per report) |

---

## 7. ANNEXURE 1 — LIST OF ENTITIES IN CONSOLIDATED STATEMENT (25 entities, lines 900-938)

| # | Category | Line | Entity | Flags |
|---|----------|------|--------|-------|
| 1 | Subsidiary | 907 | Zee Studios Limited | — |
| 2 | Subsidiary | 908 | Margo Networks Private Limited | — |
| 3 | Subsidiary | 909 | Zee Multimedia Worldwide (Mauritius) Limited | — |
| 4 | Subsidiary | 910 | ATL Media Limited | — |
| 5 | Subsidiary | 911 | Zbullet Enterprises Limited (w.e.f. 12 June 2025) | `ENTITY_CHANGE` — added prior period, still annotated |
| 6 | Subsidiary | 912 | Rotate Onetouch Limited (w.e.f. 28 June 2025) | `ENTITY_CHANGE` — added prior period |
| 7 | Subsidiary | 913 | ZI-IPR Enterprises Limited (w.e.f. 01 October 2025) | `ENTITY_CHANGE` — added prior period; also the slump-sale transferee entity per standalone/consolidated Note 6(c) |
| 8 | Step Down Subsidiary | 916 | Asia Multimedia Distribution Inc. | — |
| 9 | Step Down Subsidiary | 917 | Asia Today Limited | — |
| 10 | Step Down Subsidiary | 918 | Asia Today Singapore Pte Limited | — |
| 11 | Step Down Subsidiary | 919 | Asia TV Gmbh (liquidated w.e.f. 09 October 2025) | `ENTITY_CHANGE` — liquidated, removed |
| 12 | Step Down Subsidiary | 920 | Asia TV Limited (UK) | — |
| 13 | Step Down Subsidiary | 921 | Asia TV USA Limited | — |
| 14 | Step Down Subsidiary | 922 | ATL Media FZ-LLC | — |
| 15 | Step Down Subsidiary | 923 | OOO Zee CIS LLC (OCR "000 Zee CIS LLC") | — |
| 16 | Step Down Subsidiary | 924 | Taj TV Limited | — |
| 17 | Step Down Subsidiary | 925 | Z5X Global FZ LLC | — |
| 18 | Step Down Subsidiary | 926 | Zee Entertainment Middle East FZ-LLC | — |
| 19 | Step Down Subsidiary | 927 | Zee TV South Africa (Proprietary) Limited | — |
| 20 | Step Down Subsidiary | 928 | OOO Zee CIS Holding LLC (OCR "000 Zee CIS Holding LLC") | — |
| 21 | Step Down Subsidiary | 929 | ZEE Entertainment UK Limited | — |
| 22 | Step Down Subsidiary | 930 | Zee Media Kenya Limited | — |
| 23 | Joint Venture | 933 | Media Pro Enterprise India Private Limited | — |
| 24 | Joint Venture | 934 | Culture of Real Experiences Private Limited (w.e.f. 09 June 2026) | `ENTITY_CHANGE` — added THIS quarter (Q1 FY27); matches standalone/consolidated Note 6(b) CCPS investment |
| 25 | Associate | 937 | Phantom Digital Films Limited (w.e.f. 18 June 2026) (accounted at fair value) | `ENTITY_CHANGE` — added THIS quarter (Q1 FY27); matches standalone/consolidated Note 6(a) CCD investment in "Phantom Digital Effects Limited" — note the name printed here is "Phantom Digital **Films** Limited" vs Note 6(a)'s "Phantom Digital **Effects** Limited"; possible naming inconsistency, flag `NAME_MISMATCH` for A3 |

No prior-quarter entity ledger was provided to this run, so the above
`ENTITY_CHANGE` flags are self-evident from the w.e.f./liquidated
annotations printed in this document, not from a diff against a prior list.

---

## 8. ANNEXURE A — DIRECTOR / AUDITOR APPOINTMENT PROFILES (6 profiles, lines 1452-1616)

Table columns per profile: Reason for change, Date of appointment/re-appointment,
Brief Profile, Disclosure of relationships between directors.

| # | Line(s) | Appointee | DIN | Term | Disclosure of relationships | Flags |
|---|---------|-----------|-----|------|------------------------------|-------|
| 1 | 1457-1607 (col 1) | CMA Vaibhav Prabhakar Joshi (Cost Auditor, Vaibhav P Joshi & Associates) | N/A (firm) | FY 2026-27 | Not Applicable (line 1607) | — |
| 2 | 1457-1607 (col 2) | MGB & Co. LLP / CKSP & Co (Internal Auditors) | N/A (firms) | FY 2026-27 | Not Applicable | — |
| 3 | 1457-1607 (col 3) | Ms. Deepu Bansal | 09497525 | 2nd term, 13-Oct-2026 to 12-Oct-2031 | Not Applicable | — |
| 4 | 1457-1607 (col 4) | Mr. Uttam Prakash Agarwal | 00272983 | 2nd term, 17-Dec-2026 to 16-Dec-2031 | Not Applicable | — |
| 5 | 1457-1607 (col 5) | Dr. Venkata Ramana Murthy Pinisetti | 03483544 | 2nd term, 17-Dec-2026 to 16-Dec-2031 | Not Applicable | — |
| 6 | 1457-1607 (col 6) | Mr. Shishir Babubhai Desai | 01453410 | 2nd term, 17-Dec-2026 to 16-Dec-2031 | Not Applicable | — |

Page 30 (line 1610-1616) is the continuation/tail of the "Disclosure of
relationships" row header wrapping to a new page — confirmed by A1 header
note as a genuine table-row continuation with nil data in all six columns,
not truncated content; enumerated here as part of the same row, not a
separate item.

---

## 9. SIGNATURE / DIGITAL-SIGNATURE BLOCKS (5 blocks)

| # | Line(s) | Signatory | Designation | Timestamp/Date | Flags |
|---|---------|-----------|-------------|-----------------|-------|
| 1 | 75-101 | Ashish Ramesh Agarwal | Company Secretary (FCS6669) | Digitally signed 2026.08.10 16:35:34 +05'30 | signed 20 min after Board Meeting concluded (4:15 p.m.) — no flag |
| 2 | 235-249 | Ashish Gupta, Partner, Walker Chandiok & Co LLP | Chartered Accountants, FRN 001076N/N500013 | UDIN 26504662XBGACE8490; Place New Delhi; Date 10 August 2026 | standalone review report signature |
| 3 | 665-668 | Uttam Prakash Agarwal | Independent Director, "For and on behalf of the Board" | Place Mumbai; Date 10 August 2026 | standalone results sign-off |
| 4 | 874-888 | Ashish Gupta, Partner, Walker Chandiok & Co LLP | Chartered Accountants, FRN 001076N/N500013 | UDIN 26504662BJPCWI1756; Place New Delhi; Date 10 August 2026 | consolidated review report signature |
| 5 | 1440-1449 | Uttam Prakash Agarwal | Independent Director, "For and on behalf of the Board" | Place Mumbai; Date 10 August 2026 | consolidated results sign-off |

---

## SUMMARY TOTALS

- Agenda items: 8
- Notes (standalone 15 + consolidated 17): 32
- Result table line items (standalone 33 + consolidated 46): 79
- Limited Review Reports: 2 (with 6 standalone + 9 consolidated = 15 auditor paragraphs)
- Entities in consolidation: 25 (6 flagged `ENTITY_CHANGE`)
- Annexure A appointment profiles: 6
- Signature blocks: 5

Flags raised across the ledger: `ZERO_STANDING` (8 line items), `OCR_GARBLE`
(9 instances), `OCR_ILLEGIBLE` (1 line item, all 4 periods), `MISSING_VALUE`
(2 line items — consolidated EPS current-quarter column), `NUM_LOST` (13
notes across both sections), `CONSOL_ONLY` (2 notes), `CONTENT_ANOMALY` (1
note), `CROSS_REF_ANOMALY` (2 notes), `DATA_INCONSISTENCY` (1 note — FCCB
coupon 5% vs 6%), `ENTITY_CHANGE` (6 entities), `NAME_MISMATCH` (1 entity),
`EOM` (5 auditor paragraphs), `UNAUDITED_COMPONENTS` (1 auditor paragraph).
