# A3 FORENSIC NOTES: results | GRWRHITECH | q2fy27
Doctype: results (Reg 33 board outcome, 43 pages; pages 16-19 media release; pages 20-43 embedded investor presentation)
Inputs read: A1 structured (R001-R1782, all rows), A1 fulltext (lines 1-1492, all lines), A2 ledger (all sections).
No source PDF opened. Nothing under inputs/ opened.
Prior-quarter fulltext: none (first quarterly run). Auditor, EoM and entity-list diffs against a prior extract are not possible.
Unit: Rs crore. [DERIVED] = arithmetic on filed numbers in this document, formula shown. No number is estimated.

## 0. LEDGER RECONCILIATION
- Rows in ledger: 1,782 structured IDs (A2: orphan_ids []). Rows read at cited line: 1,782. Reconciled: 100%.
- Method: the text layer on pp5-7 and 12-14 is column-displaced. Each table was re-mapped by subtotal tie-outs. Every re-mapped value below ties to a filed subtotal (Total Income, Total Expenses, PBT, NCA subtotal, Total Assets, Total E&L, Operating profit, CGO, CFO, B, C, net change).
- Corrections to the A2 ledger (A2 asked for visual confirmation; arithmetic settles these without the PDF):
  1. ZERO_STANDING falsified on 3 of 11 rows. Consolidated OCI "Items that will be reclassified" carries 0.14 / 0.09 / 1.71 / 0.23 / 3.82 / 5.15 (line 547; proof: -2.06 + 0.63 + 0.14 = -1.29 Total OCI Q2, line 554). Consolidated CF "Net gain on financial assets" carries (23.22) / (14.97) (line 687; operating profit 358.61 ties only with it, line 689). Consolidated CF "Effects of exchange rate changes on cash" carries 1.54 / (0.57) (line 728; 126.53 + 63.55 + 1.54 = 191.62 closing).
  2. ZERO_STANDING unconfirmed on 2 rows: "Assets Classified as Held for Sale" standalone (line 261) and consolidated (line 624). Both current-asset blocks have 9 values for 9 rows and the 9 values sum exactly to total current assets (1,469.87 standalone; 1,558.93 consolidated). By position, HFS = 0.59 (30-Sep-26) / 0.58 (31-Mar-26).
  3. Balance-sheet row-ID labels are displaced in the ledger. Examples: "R255-R256 Other financial assets (current), line 260" holds 3,227.77 / 2,933.15 (TOTAL ASSETS). "R257-R258 TOTAL ASSETS, line 264" holds 23.23 (share capital). "R640 Deferred tax assets, line 611" holds 711.75 (current investments). Consolidated DTA is 1.09 / 0.95 (line 604, R632-R633).
  4. The remaining 6 ZERO_STANDING rows are consistent with zero: OCI tax on reclassified items (551), NCI profit / OCI / TCI (562, 567, 572), CF profit on sale of investment (679), CF provision for doubtful advances (684).

### Re-mapped core figures (all tie to filed subtotals)
| Item | Q2 FY27 | Q1 FY27 | Q2 FY26 | H1 FY27 | H1 FY26 | FY26 |
|---|---|---|---|---|---|---|
| SA revenue (l.170) | 634.09 | 584.14 | 511.82 | 1,218.23 | 964.46 | 1,947.56 |
| SA other income (l.171) | 46.64 | 16.00 | 42.85 | 62.64 | 56.95 | 96.59 |
| SA PBT (l.193) | 176.51 | 168.15 | 131.91 | 344.66 | 231.02 | 434.41 |
| SA total tax (l.200) | 36.64 | 41.57 | 25.39 | 78.21 | 49.91 | 99.68 |
| SA PAT (l.202) | 139.87 | 126.58 | 106.52 | 266.45 | 181.11 | 334.73 |
| C revenue (l.509-510) | 695.53 | 633.08 | 569.69 | 1,328.61 | 1,064.68 | 2,120.11 |
| C other income (l.510-511) | 19.53 | 19.72 | 13.86 | 39.25 | 27.24 | 64.84 |
| C PBT (l.532) | 173.06 | 176.46 | 120.39 | 349.52 | 230.72 | 446.22 |
| C total tax (l.539) | 43.62 | 43.81 | 29.16 | 87.43 | 56.47 | 107.99 |
| C PAT (l.541) | 129.44 | 132.65 | 91.23 | 262.09 | 174.25 | 338.23 |
| C EBITDA incl OI [DERIVED PBT+D&A+fin] | 188.99 | 191.72 | 133.30 | 380.72 | 256.25 | 499.55 |
| C EBITDA ex-OI margin [DERIVED] | 24.4% | 27.2% | 21.0% | 25.7% | 21.5% | 20.5% |
| SA EBITDA ex-OI margin [DERIVED] | 22.7% | 28.4% | 19.7% | 25.5% | 20.5% | 19.9% |

Headline EBITDA 189 / 27.2% (line 774-776) = PBT 173.06 + D&A 13.05 + finance 2.89. It includes other income.

## 1. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1a | F1 | R554-R556; R712-R714; R770-R771 | 547, 687, 728 | "0.14 0.09 1.71 0.23 3.82 5.15"; "(23.22) (14.9-7)"; "1.54 (0.57)" | NEUTRAL-FACT | Three A2 ZERO_STANDING rows carry values. FCTR (foreign subsidiaries) flows through OCI. Mutual-fund gains are 23.22 of 39.25 H1 consolidated other income (59%). |
| F1b | F1 | R255-R258 (SA); R661-R663 (C) | 261, 624 (values at 257, 618-619) | "(c) Assets Classified as Held for Sale" | AMBIGUOUS | 9 values fill 9 current-asset rows. HFS likely holds about 0.59 Cr. That points to an asset set aside for disposal (old commodity line or land?). Confirm on the page image; ask what it is. |
| F2a | F2 | R063, R159-R167, R438, R533-R540 | 170-171, 202, 509-510, 541 | "Net Profit after tax (3-4) 139.87 126.58 106.52" | AMBIGUOUS | C-minus-SA PAT gap was +4.80% of SA PAT in Q1 and -7.46% in Q2: a swing of 12.3 pp QoQ. YoY it narrowed 6.9 pp (-14.35% in Q2 FY26). Drivers: a ~28 Cr intra-group dividend sits in SA other income every Q2 (SA CF line 307 "Dividend Income (28.04)"; H1 FY26 28.26). Subsidiaries plus eliminations added +25.30 Cr ex-OI EBITDA in Q2 against +5.84 in Q1 [DERIVED]. SA ex-OI margin fell from 28.4% to 22.7% while the group's fell from 27.2% to 24.4%. Profit moved from parent to subsidiaries in Q2. No JV or associate. |
| F2b | F2 | R405-R406, R1737 | 443, 509, 170 | "total revenues of Rs. 286.63 crores and 554.10 crores" | AMBIGUOUS | Intra-group revenue eliminated [DERIVED SA + subs - C] = 634.09 + 286.63 - 695.53 = 225.19 Cr in Q2 (35.5% of SA revenue) and 443.72 Cr in H1 (36.4%). A Notion tripwire names a "34% customer". On standalone accounts that customer may be the group's own distribution subsidiary. Lead question for A4. |
| F2c | F2 | R411, R1737; SA BS/CF; C BS/CF | 446, 250, 612, 614, 330-333, 709 | "the share of net cash inflow of Rs. 72.91 crores" | AMBIGUOUS | SA trade receivables are 262.59 and consolidated are 71.56, so at least 191.03 Cr of the parent's receivables are intra-group (at least 141.21 at 31-Mar). That is up by at least 49.82 in H1 [DERIVED]. The subsidiaries hold about 155.64 Cr cash (191.62 C less 35.98 SA), up from 81.39. SA CFO is 94.70 against 143.65 in H1 FY26, so CFO/PAT is 35.5% against 79.3%. C CFO is 195.34 (74.5%). Cash builds offshore while the parent waits to be paid. Repatriation and transfer-pricing question. |
| F3 | F3 | R414-R420, R1738; SA CF R340 | 455-459, 335, 690 | "revenue of Rs. Nil and total net loss after tax of Rs. 0.10 crores and 0.38 crores" | AMBIGUOUS | One subsidiary is shell-like: nil revenue, 0.18 Cr assets, management-furnished, not named. The parent put 0.52 Cr into a subsidiary in H1 [DERIVED: SA investing sums to (70.08) only with "(0.52)" on line 335; SA minus C NC investments rose from 1.34 to 1.86]. H1 FY26 was nil. C CF line 690 "Transfer of Foreign Currency Translation Reserve (1.36)". No going-concern language. The other two subsidiaries are non-manufacturing: power & fuel 42.87 SA against 42.88 C, D&A 12.72 against 13.05. They carry real staff and costs: employees +8.98 and other expenses +7.80 per quarter. Ask which entity has nil revenue, whether it is new (FZCO?), and its purpose. |
| F4a | F4 | R404-R410, R1319, R1737 | 441-452 | "reviewed by other auditors whose reports have been furnished to us by the management" | AMBIGUOUS | Other auditors, not the statutory auditor, reviewed 40.55 Cr = 31.3% of Q2 consolidated PAT and 50.61 Cr = 19.3% of H1. That is 41% of revenue and 297.08 Cr of assets. A further 0.10 / 0.38 Cr loss is management-furnished and reviewed by nobody (line 462). Both are above the 10% threshold. YoY trend not assessable (no prior extract). |
| F4b | F4 | R407-R408 | 443-444 | "total net profit after tax of Rs. 40.55 crores and · Rs. 50.61 crores" | AMBIGUOUS | Implied Q1 subsidiary PAT = 50.61 - 40.55 = 10.06 Cr (7.6% of Q1 C PAT) [DERIVED]. Q2 is 40.55 (31.3%). Subsidiary net margin went from 3.8% to 14.1% on revenue growth of +7.2% (267.47 to 286.63). The jump in profit that rests on other auditors' reviews is a separate flag. Possible step-down dividend inside the subsidiary group [INFERENCE]; ask. |
| F6a | F6 | R1391, R1401, R1402, R1406, R1767 | 760, 889, 1106, 1121 | "raises its FY27 EBITDA guidance by 200 bps (to 27% ±2%)"; "(Including Other Income)" | FORWARD-SIGNAL | Guidance EBITDA includes other income: Q2 OI 19.53 = 2.8 pp of revenue, much of it MF gains (F1a). Midpoint maths [DERIVED]: 27% x 2,500 = 675; H1 380.72; so H2 needs 294.28 on 1,171.39 = 25.1%. The "raise" implies H2 margin about 210 bps below Q2's 27.2% and about 360 bps below H1's 28.7%. The 2,500+ revenue target needs H2 growth of only +11.0% YoY against H1's +24.8%. Management is guiding an H2 step-down. Ask why: TPU start-up costs, Middle East, raw material and logistics (line 803)? |
| F6b | F6 | R1393, R1399, R1419, R1424, R1394, R1425, R1417 | 825, 893, 1057, 1210-1214, 711, 598, 1128 | "TPU line commissioning remains on track for Q3 FY27" | FORWARD-SIGNAL | Status word is "on track", not "commissioned", as of 22-Oct-2026. Notion expected October 2026; the filing commits only to the Q3 window. H1 capex was 27.07 Cr (C CF line 711; deck "27 cr capex" line 1130) and CWIP is 37.24 (line 598), against TPU at 118 Cr and the SCF line at 191/192 Cr. Capital advances rose from 27.97 to 50.67. "~170 cr capex" (line 1128) sits in a displaced column: FY27E or medium term? If FY27E, H2 spend must be about 143 Cr. Track "commissioned" at Q3. |
| F7 | F7 | R1757, R1763, R1766, R1772 | 797, 792-793, 1137, 1201, 934 | "despite slowdown in the Middle East amid the ongoing conflict"; "*The actual numbers might vary as per the change in Macro-economic situation" | AMBIGUOUS | No hedge sits inside the statutory notes. The release and deck name two external headwinds: the Middle East slowdown, and a US tariff that held FY26 organic growth to 0.5% ("*Tariff related impact"). The FY27-and-beyond targets carry a macro hedge footnote. This fits the H2 step-down implied in F6a. Ask for Middle East and US revenue shares and the current tariff status. Safe-harbour "No assurance is given" (line 934) is boilerplate. |
| F8 | F8 | R141-R158, R515-R532, R303 | 193, 200, 307, 532, 539 | "Dividend Income (28.04)" | NEUTRAL-FACT | SA ETR: Q2 20.76%, Q1 24.72%, Q2 FY26 19.25%, H1 22.69%, FY26 22.95%, against statutory 25.17%. Excluding the dividend, Q2 tax at statutory rate = (176.51 - 28.04) x 25.168% = 37.37 against 36.64 actual [DERIVED]. So the dividend explains nearly all of the gap. SA dividend received 28.04 is about equal to dividend paid 27.88 (C CF line 722 region). That fits a pass-through deduction. Consolidated ETR is 24.2-25.2%, so there is no group-level ETR step-up risk. Deferred tax is a charge in every period, never a credit. Deferred-tax movements tie: SA DTL +7.01 = P&L 4.77 + OCI 2.24; C net DTL +7.50 = 5.27 + 2.24. No prior-year tax adjustment line. |
| F11 | F11 | R202-R203, R264-R266, R603, R664-R668, R1768-R1769, R1778 | 217, 265, 574, 628, 1137, 1470 | "Reserves excluding Revaluation Reserves ... 2,563.52"; "Annualised ROCE Adjusted for Revaluation reserve of ₹ 764 Cr" | AMBIGUOUS | Net worth ties: SA 23.23 + 2,818.34 = 2,841.57; C 23.23 + 2,883.62 = 2,906.85. But the line "Reserves excluding Revaluation Reserves" equals full other equity at 31-Mar-26 (SA 2,563.52; C 2,632.93), while the deck strips a 764 Cr revaluation reserve. Gap = 28.8% of C net worth (>5%). Candidate reconciling item: revaluation surplus inside other equity, with the line-9 label wrong. Tripwire 1 (ROCE <15%) needs a fixed basis. Deck ROCE: FY26 23%, H1 32%**, both adjusted. Unadjusted [DERIVED, EBIT = PBT + finance cost, on closing net worth + lease liabilities]: FY26 454.42 / 2,671.82 = 17.0%; H1 FY27 annualised 709.72 / 2,919.46 = 24.3%. |
| F12 | F12 | R1321, R1730, R1750, R1354-R1356 | 363, 741, 1148-1160 | "The Company operates in one segment only i.e. Polyester Films" | AMBIGUOUS | One Ind AS 108 segment, but the deck splits revenue CPD 73% / IPD 27% (line 1151, 1160) and VAP 86% (line 1148). There are no segment assets, liabilities or margins, so the VAP-versus-commodity climb cannot be verified from filed segment data. Ask whether the chief operating decision maker reviews CPD and IPD separately, and ask for divisional EBITDA. |
| F13a | F13 | R007; R1729, R1749; R1381-R1385 | 40-43, 357-367, 735-749, 1369-1370 | "Zero Liquid Discharge initiatives"; "sludge and prevent pollution" | AMBIGUOUS | [EXTERNAL, caller input] MPCB forfeited a Rs 25 lakh bank guarantee (letter dated 19-Oct, received 21-Oct; Reg 30 filed 22-Oct). The board met on 22-Oct. The outcome letter, the 3 standalone and 4 consolidated notes, and the deck do not mention it (grep: zero hits for pollution board, consent, guarantee). The ESG slide claims ZLD and 100% water recycling. Rs 0.25 Cr is immaterial to PAT. The forward risk is consent-to-operate compliance at the Waluj plant. Ask which consent conditions were breached and what the remediation timeline is. |
| F13b | F13 | R1435, R1712 | 51 | "The meeting commenced at 11:30 A.M. and concluded around� a.m." | NEUTRAL-FACT | Ended in the a.m., so the meeting ran 30 minutes or less for results, release and deck. The only agenda item is results (line 40). No AR, AGM, dividend, director or capital-raising item. No Role 6 trigger from this outcome. |
| F14 | F14 | R877, R1759, R1775; R1394/R1425; R1427; R1738; R1314-R1318 | 813, 826 vs 1213, 1166-1168 vs 847-849, 465, 426 vs 746, 745 vs 427, 1114 vs 1116, 855 vs 1120 | "Cash and cash equivalents stood at INR 933 crore" | NEUTRAL-FACT | (1) 933 = cash 191.62 + bank 29.45 + current investments 711.75 = 932.82 [DERIVED]. Ind AS cash and cash equivalents are 191.62; the deck calls it "liquidity surplus" (line 1155, 1282). (2) SCF line capex 191 Cr (line 826) against "192Cr" (line 1213). (3) GAS "to be launched in Middle East & USA" against 14 already operating (11 USA, 3 ME). (4) LRR para 7 says "these subsidiaries" for one subsidiary. (5) Step-down Global Hi-Tech Films Inc is listed beside direct subsidiaries in LRR para 4. "Garware Hi Tech" (line 745) against "Garware Hi-Tech" (line 427). (6) FY27E ">20%" organic growth against the Rs 2,500+ Cr target = +17.9% on 2,120.11. (7) GHS 50 studios "by Dec'27" (line 855) against the FY27E column (line 1120, displaced). Each is small; together they are a governance data point. |
| F15 | F15 | R1313-R1318, R1751; SA CF R340 | 424-427, 744-746, 335 | "(100% step d9wn subsidiary)" | AMBIGUOUS | No prior entity list, so no diff is possible. In-document evidence of a perimeter change: a new 0.52 Cr investment in a subsidiary in H1 (H1 FY26 nil), and one unnamed nil-revenue entity. Four entities: parent + GHF International (100%), Global Trading FZCO (100%), Global Hi-Tech Films Inc (100% step-down). Ask whether any entity was set up or recapitalised in FY27. |

## 2. CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | FINDING | 11 ZERO_STANDING rows: 3 carry values by arithmetic (F1a), 2 HFS rows unconfirmed (F1b), 6 consistent with zero. Template classes anticipated: HFS = asset disposal; NCI = minority partner in a subsidiary (would activate if the Lubrizol TPU tie-up ever takes equity form); sale of investment = MF/FVOCI exit; doubtful advances = credit loss on capital advances (27.97 to 50.67). |
| F2 | FINDING | PAT gap swing 12.3 pp QoQ, 6.9 pp YoY; intra-group revenue 35.5% of SA; cash and receivable location shift (F2a-c). |
| F3 | FINDING | One shell-like unnamed subsidiary with a new 0.52 Cr infusion. The other two subsidiaries are non-manufacturing distributors with real costs. No going concern (F3). |
| F4 | FINDING | 31.3% of Q2 and 19.3% of H1 consolidated PAT rest on other auditors; a QoQ jump from 7.6% (F4a-b). |
| F5 | PASS | No EoM, no going-concern language, conclusions unmodified in both LRRs (lines 125-135, 429-437, 480). Quarter-over-quarter verbatim diff not possible: no prior extract. |
| F6 | FINDING | No forward language in the statutory notes. 17 commitments registered from the release and deck. The guidance raise implies an H2 step-down; TPU still "on track" (F6a-b). |
| F7 | FINDING | No hedge inside the notes. Middle East, tariff and macro hedges in the release and deck (F7). |
| F8 | FINDING | SA Q2 ETR 441 bps below statutory, explained by the subsidiary dividend. Consolidated ETR at statutory; deferred tax always a charge; no prior-year tax line (F8). |
| F9 | PASS | Largest single-quarter swing in "items not reclassified" is Q2 FY26 (25.22) and Q1 FY27 +20.55, both below the FY26 full-year (36.65). The tax on these items runs about 12-15%, not 25.17%. So OCI is mainly fair-value change on FVOCI equity (NC investments 80.69 to 103.44), not an actuarial assumption change. Investee identity not disclosed: an AR item. |
| F10 | PASS | Paid-up capital 23.23 in every period (lines 264, 569-572, 627). Basic = diluted in every period, SA and C (lines 219-220, 571-572, 576-577). 129.44 / 55.71 = 2.3235 Cr shares. No dilution spread. |
| F11 | FINDING | Net worth ties. The revaluation-reserve label conflicts with the deck's 764 Cr adjustment; unadjusted ROCE 17.0% FY26 [DERIVED] (F11). The "Net Zero debt" claim (line 1274) is consistent: no borrowings line, lease liabilities 12.61 C. |
| F12 | FINDING | One reportable segment against CPD/IPD divisional reporting in the deck; no segment assets or liabilities (F12). |
| F13 | FINDING | Only agenda item is results. Meeting of 30 minutes or less. Silent on the MPCB action received the day before (F13a-b). |
| F14 | FINDING | 7 drafting and labelling inconsistencies, led by the "933 Cr cash" label (F14). Notes against auditor letter consistent ("Unaudited", "reviewed"). |
| F15 | FINDING | No prior list to diff. In-document evidence of a perimeter change (F15). |
| F16 | N.A. | Results doctype per the A3 applicability rule. Also no prior deck exists, so dropped or reframed disclosures cannot be tested. |
| F17 | N.A. | Results doctype; no transcript. Checklist cross-reference supplied below as supplementary, not scored. |

GATE A3: pass (17 of 17 marked, 0 blank).

## 3. COMMITMENT REGISTER (F6)
| # | commitment | implied date | ref (line) | status word |
|---|---|---|---|---|
| C1 | FY27 EBITDA margin 27% ±2%, incl other income; raised 200 bps from 23-27% | FY27 (to Mar-2027) | 760, 889, 1106, 1118, 1121 | raised |
| C2 | FY27 revenue Rs 2,500+ Cr | FY27 | 761, 1108, 1116 | reaffirmed |
| C3 | FY27E organic sales growth >20% | FY27 | 1114 | stated |
| C4 | TPU line, Rs 118 Cr, 360 LSF p.a. | Q3 FY27 (Oct-Dec 2026) | 825, 893, 973, 1057, 1210-1214 | underway ("remains on track") |
| C5 | TPU adds 150-200 bps consolidated EBITDA margin; 75% backward integration for PPF | after commissioning | 1059-1067, 1119 | stated |
| C6 | Lubrizol MoU, TPU-based films in India | undated | 830-833, 1053 | initiated (MoU signed) |
| C7 | SCF line Rs 191 Cr (192 Cr on p33), about 1,200 LSF | H1 FY28 (Apr-Sep 2027) | 826-828, 1211-1215 | initiated ("expected to commence") |
| C8 | Further capacity additions | undated | 894, 974 | underway |
| C9 | GHS +12 studios in Q3 (Delhi NCR, Mumbai) | Q3 FY27 | 854 | initiated ("Plans to add") |
| C10 | GHS 50 studios | Dec-2027 (line 855); FY27E column (line 1120, displaced) | 855, 1120 | targeting |
| C11 | GAS / PPF distributors 250+ to 300 | undated | 1307-1310 | target |
| C12 | FY28-31: about 20% revenue CAGR; EBITDA >27% (+150-200 bps TPU); ROCE >25%; studios >200 / >300 / >400 | FY28-31 | 1111-1128 | commitment |
| C13 | Capex about 170 Cr | FY27E or medium term (displaced column) | 1128 | stated |
| C14 | Export share 70%+, VAP 85%+ | FY27 and beyond | 1199 | stated |
| C15 | PPF capacity doubled to 60 mn sq ft | Q2 FY26 | 1206-1210 | completed ("Commissioned") |
| C16 | PDLC switchable-film facility launched | Q2 FY27 | 837-838 | completed |
| C17 | 2 new GAS in USA; network 14 (11 USA, 3 ME); GHS 9 to 14 | Q2 FY27 | 847-852 | completed |

## 4. SUPPLEMENTARY: NOTION CHECKLIST CROSS-REFERENCE (not scored; F17 is N.A. for results)
| checklist item | filing addresses it? | cite | quarters silent (this pipeline) |
|---|---|---|---|
| TB1 ROCE <15% for 2Q | Indirectly. Deck ROCE is revaluation-adjusted (FY26 23%, H1 32%**). Unadjusted [DERIVED] FY26 17.0%, H1 annualised 24.3%. | 1128-1137, 1470 | n/a |
| TB2 34% customer cuts volume >20% | Silent on customer concentration. Intra-group sales [DERIVED] 35.5% of SA revenue (F2b). | 443, 509 | 1 |
| TB3 operating EBITDA margin <18% for 2Q | Q2 ex-OI 24.4% [DERIVED]; headline 27.2% incl OI. Q3 FY26 headline 18.9% (line 1021). Its ex-OI figure: NOT FOUND in this filing. | 774-776, 1021 | n/a |
| TB4 promoter verdict AVOID | Not a filing item | none | n/a |
| Identity of 34% customer | Silent; see F2b | none | 1 |
| FY27 Q1-Q2 trajectory and guidance | Q1 633.08 / 192 / 30.3% matches Notion (no restatement). H1 1,328.61 (+24.8% YoY). Guidance raised on an OI-inclusive basis (F6a). | 772-776, 1106-1121 | addressed |
| TPU commissioning Oct 2026; Lubrizol MoU | "on track for Q3 FY27", not commissioned; MoU described | 825, 830, 1053 | addressed (partial) |
| Anti-dumping duty status | Silent (grep: zero hits) | none | 1 |
| MPCB Rs 25 lakh BG forfeiture (22-Oct Reg 30) | Silent; ESG slide claims ZLD (F13a) | 1369-1370 | 1 |

## 5. QUESTIONS FLAGGED FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)
1. F2b / TB2: Is the 34% customer in the FY26 standalone disclosure the group's own subsidiary? What share of revenue does the largest external customer hold?
2. F6a: Midpoint guidance implies H2 EBITDA margin near 25.1% against 27.2% in Q2. What drives the step-down? How much of guided EBITDA is other income?
3. F11: Is the 764 Cr revaluation reserve inside other equity? Which ROCE basis does management use, and which should tripwire 1 use?
4. F2a / F2c / F4b: Why did subsidiary PAT rise from 10.06 to 40.55 Cr QoQ while standalone margin fell? Why do the subsidiaries hold about 156 Cr cash while owing the parent at least 191 Cr?
5. F6b: Has the TPU line been commissioned? What is the FY27 capex plan: is about 170 Cr the FY27 figure?
6. F3 / F15: Which subsidiary has nil revenue? Was it formed or recapitalised in FY27, and for what?
7. F13a: Which MPCB consent conditions were breached? Is consent-to-operate at Waluj at risk?
8. F7: What are the Middle East and US revenue shares? What is the tariff status now?
9. F12: Does management review CPD and IPD margins separately? Will it disclose them?
10. F1b: What asset sits in Held for Sale?

```yaml
stage: A3-forensics
company: "GRWRHITECH"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/grwrhitech-q2fy27/work/forensics_grwrhitech_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: FINDING
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1a", check: "F1", line: "547, 687, 728", classification: "NEUTRAL-FACT", implication: "3 of 11 A2 ZERO_STANDING rows carry values by arithmetic (OCI reclassifiable, MF gain 23.22, FX on cash 1.54); MF gains are 59% of H1 consolidated other income"}
  - {id: "F1b", check: "F1", line: "261, 624", classification: "AMBIGUOUS", implication: "9 values fill 9 current-asset rows; Held for Sale likely about 0.59 Cr; an asset set aside for disposal; confirm on page image"}
  - {id: "F2a", check: "F2", line: "170-171, 202, 509-510, 541, 307", classification: "AMBIGUOUS", implication: "C-SA PAT gap swung 12.3 pp QoQ (+4.80% to -7.46%); 28 Cr intra-group dividend each Q2; subs+elim ex-OI EBITDA +25.30 Q2 vs +5.84 Q1; SA ex-OI margin 28.4% to 22.7%; profit moved parent to subs"}
  - {id: "F2b", check: "F2", line: "443, 509, 170", classification: "AMBIGUOUS", implication: "Derived intra-group sales 225.19 Cr Q2 = 35.5% of SA revenue (H1 36.4%); the Notion 34% customer may be the group's own subsidiary"}
  - {id: "F2c", check: "F2", line: "446, 250, 612, 614, 330-333, 709", classification: "AMBIGUOUS", implication: "Parent intra-group receivables >=191 Cr, up >=49.82 in H1; subs hold about 155.64 Cr cash (+72.91 H1); SA CFO/PAT 35.5% vs 79.3% H1 FY26; consolidated 74.5%"}
  - {id: "F3", check: "F3", line: "455-459, 335, 690", classification: "AMBIGUOUS", implication: "One unnamed nil-revenue management-furnished subsidiary (assets 0.18, H1 loss 0.38); new 0.52 Cr parent investment in a subsidiary; other two subs are non-manufacturing distributors"}
  - {id: "F4a", check: "F4", line: "441-452, 462", classification: "AMBIGUOUS", implication: "40.55 Cr = 31.3% of Q2 (19.3% H1) consolidated PAT and 41% of revenue reviewed by other auditors only; above the 10% threshold"}
  - {id: "F4b", check: "F4", line: "443-444", classification: "AMBIGUOUS", implication: "Derived Q1 sub PAT 10.06 (7.6%) to Q2 40.55 (31.3%); sub net margin 3.8% to 14.1% on +7.2% revenue"}
  - {id: "F6a", check: "F6", line: "760, 889, 1106, 1121", classification: "FORWARD-SIGNAL", implication: "Guidance EBITDA includes other income; midpoint 27% on 2,500 Cr implies H2 margin about 25.1% vs Q2 27.2%; revenue target needs only +11.0% H2 YoY growth; guided step-down"}
  - {id: "F6b", check: "F6", line: "825, 893, 1057, 1210-1214, 711, 598, 1128", classification: "FORWARD-SIGNAL", implication: "TPU still 'on track' for Q3 FY27, not commissioned as of 22-Oct; H1 capex 27.07 vs TPU 118 and SCF 191 Cr; about 170 Cr capex column ambiguous"}
  - {id: "F7", check: "F7", line: "797, 792-793, 1137, 1201", classification: "AMBIGUOUS", implication: "Middle East slowdown, US tariff (FY26 organic growth 0.5%) and macro hedge on FY27+ targets; consistent with the implied H2 step-down"}
  - {id: "F8", check: "F8", line: "193, 200, 307, 532, 539", classification: "NEUTRAL-FACT", implication: "SA Q2 ETR 20.76% vs 25.17% explained by the 28.04 Cr sub dividend (ex-dividend tax 37.37 vs 36.64); consolidated ETR 24.2-25.2%; deferred tax always a charge"}
  - {id: "F11", check: "F11", line: "217, 265, 574, 628, 1137, 1470", classification: "AMBIGUOUS", implication: "Reserves excl revaluation equal full other equity despite 764 Cr reval reserve (28.8% of NW); unadjusted ROCE FY26 17.0% vs deck 23%; tripwire 1 basis must be fixed"}
  - {id: "F12", check: "F12", line: "363, 741, 1148-1160", classification: "AMBIGUOUS", implication: "One segment filed vs CPD 73% / IPD 27% in deck; VAP climb not verifiable from segment data"}
  - {id: "F13a", check: "F13", line: "40-43, 357-367, 735-749, 1369-1370", classification: "AMBIGUOUS", implication: "Filing silent on MPCB BG forfeiture received 21-Oct [EXTERNAL caller input]; ESG slide claims ZLD; consent-to-operate risk at Waluj"}
  - {id: "F13b", check: "F13", line: "51", classification: "NEUTRAL-FACT", implication: "Board meeting 30 minutes or less; results the only agenda item; no AR, AGM, dividend or director item"}
  - {id: "F14", check: "F14", line: "813, 826, 1213, 1166, 465, 426, 745, 1114, 855", classification: "NEUTRAL-FACT", implication: "933 Cr labelled cash and cash equivalents (Ind AS C&CE 191.62); 191 vs 192 Cr; stale GAS text; entity-name variants; >20% growth vs 2,500 Cr target"}
  - {id: "F15", check: "F15", line: "424-427, 744-746, 335", classification: "AMBIGUOUS", implication: "No prior list to diff; new 0.52 Cr subsidiary investment (H1 FY26 nil) and unnamed nil-revenue entity suggest a perimeter change"}
forward_signals: ["F6a", "F6b"]
ambiguous: ["F1b", "F2a", "F2b", "F2c", "F3", "F4a", "F4b", "F7", "F11", "F12", "F13a", "F15"]
commitments:
  - {commitment: "FY27 EBITDA margin 27% +/-2% incl other income (raised 200 bps)", implied_date: "FY27", ref: "line 760, 1106, 1121", status_word: "raised"}
  - {commitment: "FY27 revenue Rs 2,500+ Cr", implied_date: "FY27", ref: "line 761, 1108", status_word: "reaffirmed"}
  - {commitment: "FY27E organic sales growth >20%", implied_date: "FY27", ref: "line 1114", status_word: "stated"}
  - {commitment: "TPU line Rs 118 Cr, 360 LSF p.a.", implied_date: "Q3 FY27", ref: "line 825, 893, 1057, 1210-1214", status_word: "underway"}
  - {commitment: "TPU adds 150-200 bps consolidated EBITDA margin", implied_date: "post-commissioning", ref: "line 1065, 1119", status_word: "stated"}
  - {commitment: "Lubrizol MoU for TPU films in India", implied_date: "undated", ref: "line 830, 1053", status_word: "initiated"}
  - {commitment: "SCF line Rs 191 Cr (192 Cr p33), about 1,200 LSF", implied_date: "H1 FY28", ref: "line 826-828, 1211-1215", status_word: "initiated"}
  - {commitment: "Further capacity additions", implied_date: "undated", ref: "line 894, 974", status_word: "underway"}
  - {commitment: "GHS +12 studios in Q3 (Delhi NCR, Mumbai)", implied_date: "Q3 FY27", ref: "line 854", status_word: "initiated"}
  - {commitment: "GHS 50 studios", implied_date: "Dec-2027 (line 855) or FY27E (line 1120, displaced)", ref: "line 855, 1120", status_word: "targeting"}
  - {commitment: "GAS/PPF distributors 250+ to 300", implied_date: "undated", ref: "line 1307-1310", status_word: "target"}
  - {commitment: "FY28-31 about 20% revenue CAGR, EBITDA >27%, ROCE >25%", implied_date: "FY28-31", ref: "line 1111-1128", status_word: "commitment"}
  - {commitment: "Capex about 170 Cr", implied_date: "FY27E or medium term (displaced)", ref: "line 1128", status_word: "stated"}
  - {commitment: "Export share 70%+, VAP 85%+", implied_date: "FY27+", ref: "line 1199", status_word: "stated"}
  - {commitment: "PPF capacity doubled to 60 mn sq ft", implied_date: "Q2 FY26", ref: "line 1206-1210", status_word: "completed"}
  - {commitment: "PDLC facility launched", implied_date: "Q2 FY27", ref: "line 837", status_word: "completed"}
  - {commitment: "GAS network 14 (11 USA, 3 ME); GHS 9 to 14", implied_date: "Q2 FY27", ref: "line 847-852", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Profit and cash moved between parent and subsidiaries in Q2, and the headline hides it. Subsidiaries earned 40.55 Cr (31% of group PAT, reviewed by other auditors) against a derived 10.06 Cr in Q1. Standalone ex-OI margin fell from 28.4% to 22.7%. Subsidiaries added 72.91 Cr cash while the parent's intra-group receivables rose by at least 50 Cr. Standalone CFO/PAT fell to 35.5%. Derived intra-group sales are 35.5% of standalone revenue, close to the Notion 34% customer. That customer may be the group's own distribution arm: a lead question, not a conclusion. Guidance EBITDA includes other income, and at its midpoint it implies an H2 margin near 25.1%, below Q2's 27.2%. Deck ROCE excludes a 764 Cr revaluation reserve. Derived unadjusted FY26 ROCE is 17.0%, 2 points above tripwire 1. A2 marked 3 of 11 ZERO_STANDING rows as zero, but arithmetic shows they carry values. The pp6/13 row IDs are displaced, so all values here were re-mapped by subtotal tie-outs."
```
