# A3 FORENSIC NOTES: Aurum PropTech Ltd (AURUM) | doctype: results | Q2 FY27 (quarter and half year ended 30 Sep 2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date: 2026-10-17
Inputs read: A1 structured (R001-R1728), A1 fulltext (L1-L1074, every line), A2 ledger (511 rows).
Not read: source PDF, inputs/. Prior-quarter fulltext: not on file. The F5 and F15 prior-quarter comparisons use the Q1 FY27 Notion record and in-document change statements only.
Units: statement tables are in INR lakhs (x0.01 = Rs Cr). Press release pages 2-4 use Rs Cr. Every number below is in lakhs unless marked Cr.

## 0. LEDGER RECONCILIATION

| Ledger category | Rows | Read at cited fulltext line | Result |
|---|---|---|---|
| note (N-C1..17, N-S1..17) | 34 | L525-L666, L941-L1068 | read |
| line_item (LI001-LI354) | 354 | L308-L1065 (9 tables) | read; 48 cells on 11 lines spot-checked against structured rows (L349, L350, L381, L405, L406, L437, L447, L794, L806, L807, L838): all match |
| agenda_item (AG01-AG14) | 14 | L18-L43 | read |
| auditor_para (AP01-AP10, AP-S2) | 11 | L173-L297, L679-L773 (AP-S2 at L701, no structured row, text read) | read |
| entity (E-R1562..R1576) | 15 | L227-L244 | read |
| signature (SG01-SG10) | 10 | L46-L49, L668-L672, L1070-L1074 | read |
| press_release (PR001-PR044) | 44 | L52-L166 | read |
| table_qualifier (TQ001-TQ020) | 20 | L301-L1026 | read |
| missing (MS01-MS09) | 9 | L530-L543 | read; A2 is right that all nine restate entities in the auditor list |
| TOTAL | 511 | 511 | 100% (structured IDs 1728/1728, per A2 orphan test) |

Reconciliation notes (A1 defects, immaterial):
- R106 has the label "consolidated" but cites page 19 L949, which is the standalone note. The consolidated version of the same claim is at L549 ("INR 12.772 lakhs", an OCR comma error) and has no separate row. The value is the same.
- Page 12 (consolidated notes) is raw OCR. Note numbers "41", "42", "43" at L525/L606/L608 are OCR errors for 1, 12, 13. Values in notes 3-13 agree with the standalone notes on page 19, except for the cases flagged in F14.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | LI017-LI019, LI172-LI191, N-C14 | L327-L330, L627 | "8 Profit / (loss) from discontinued operations \| - \| 5,240" ; "sale transaction was concluded" | NEUTRAL-FACT | Q2 discontinued ops are nil. H1 net profit is 4,947, and 4,552 of it (92%) is the Q1 Navi Mumbai building gain after tax. Q2 continuing PAT of 429 is the clean base. Held-for-sale residue is assets 2 and liabilities 170 (L426, L450), still to settle. The line should stay nil from Q3. |
| F1-02 | F1 | LI124 | L465, L418 | "Provision for doubtful debts \| 444 \| - \| 1,043" | AMBIGUOUS (bear lean) | The provision is 444 in H1 FY27 against nil in H1 FY26. That is 1,487 in 18 months against a receivables book of 4,811. Receivables fell 5,222 to 4,811 while Locon was added. The interim filing has no ageing table, so it cannot show whether the >1-year buckets stopped growing (checklist item 4). Ask for the ageing schedule and how much of the 444 is specific provision. |
| F1-03 | F1 | LI154, LI311, LI312 | L498, L916-L917 | "Repayment of loan - related parties \| (0) \| (1,589)" ; "Proceeds from loan - related parties \| - \| 317" | NEUTRAL-FACT | No related-party borrowing or repayment in H1 FY27, against 1,589 repaid (consolidated) and 317 raised (standalone) in H1 FY26. The line covers borrowing FROM related parties. It does not answer the checklist item 8 named test (loans TO AREDL). |
| F2-01 | F2 | LI016, LI214, LI010 | L325, L796, L318 | "Profit / (loss) after tax from Continuing Operations \| 429 \| (34) \| (784)" ; "Profit after tax from Continuing Operations \| 267 \| 194 \| 149" | NEUTRAL-FACT | The consolidated minus standalone continuing PAT gap swung from -117.5% of standalone PAT (Q1) to +60.7% (Q2). YoY it was -626.2%. Subsidiaries plus eliminations moved from -127 (Q1) to +140 (Q2). Standalone is a holding/treasury entity: revenue 6, other income 837 (mostly intra-group interest, L881). From Q3 the gap will be driven by Locon (Housing.com). |
| F2-02 | F2 | LI009, LI002, PR007 | L317, L309, L74 | "Profit / (loss) before share of profit / (loss) of an associate and tax \| 660" ; "Other income \| 712" ; "fourth consecutive quarter of positive PBT" | CONFIRMATORY-NEGATIVE | Operating PBT before associate, ex-OI, is 660 - 712 = -52 (Rs -0.52 Cr). Q1 was -486 (Rs -4.86 Cr). This is the second consecutive negative quarter on the checklist item 1 definition. The press release claims positive PBT. In H1, at least 741 of OI 1,429 is non-recurring: lease-termination gains 451, provision reversals 267, PPE gain 23 (L470-L473). |
| F2-03 | F2 | LI126, LI090 | L467, L421 | "Interest income on loans \| (201) \| (57) \| (161)" ; "Financial assets - Loans \| 952 \| 952" | AMBIGUOUS | Intra-group loans eliminate on consolidation, so the 952 consolidated loan book is owed by a borrower outside the group. Interest of 201 in H1 on a flat 952 is about 21% per half, or about 42% annualised. FY26 was about 17%. The filing does not name the borrower or explain the yield. Ask who the borrower is (associate Integrow, a related party such as AREDL, or a third party), plus the rate and the security. This bears directly on the checklist item 8 named test. |
| F4-01 | F4 | AP04, LI010 | L264-L269, L318 | "Rs. 22 lakhs and Rs. (79) Lakhs ... furnished to us by the Management" | AMBIGUOUS | Management-certified associate (Integrow) share: H1 (79) = 20.0% of H1 continuing PAT 395, above the 10% bar. Q2 is +22 = 5.1% of 429. The associate swung by 123 (from -101 in Q1 to +22 in Q2). That is 22% of the 552 QoQ PBT improvement, on numbers the auditor did not review. The ratio is falling, not rising (Q2 FY26 32.5%), so the YoY jump test does not fire. Ask what turned Integrow profitable. |
| F6-01 | F6 | N-C4, N-S4, LI075, LI076 | L561-L564, L405-L406 | "provisional fair values ... Any necessary adjustments to these provisional amounts will be made within the measurement period" | FORWARD-SIGNAL | Goodwill rose 20,717 to 54,945 (+34,228). Intangibles rose 9,098 to 41,005 (+31,907). Both are provisional. The Ind AS 103 measurement period closes by 29 Sep 2027 at the latest. Q3 FY27 is the first full Locon quarter. Amortisation of about 31,900 of acquired intangibles will step up D&A. Useful lives are not disclosed. The goodwill/intangible split can still move. |
| F6-02 | F6 | N-C5, N-S5 | L566-L571, L972-L974 | "The balance 75% of the issue price shall be payable by AREDL at the time of exercise ... at its option, within a period of 18 months" | FORWARD-SIGNAL | 51,00,000 warrants at INR 231.421 (11,802.47). 2,950.62 (25%) was received on 13 Oct 2026, after period end, so it is not in Sep-26 equity. The other 8,851.85 is optional for AREDL and due by about 13 Apr 2028. On exercise: 51 lakh new shares, 5.3% of 963.2 lakh in issue. The price is the same as the Locon swap (45,806 / 1,97,93,309 = Rs 231.42). |
| F6-03 | F6 | N-C7, N-S7 | L583-L585, L589 | "considering a prospective restructuring of the equity of Integrow ... in abeyance until March 31, 2027" | FORWARD-SIGNAL | Dated catalyst: by 31 Mar 2027 the abeyance ends. Integrow then either goes back to subsidiary consolidation or completes the restructuring. The holding is 48.16%. The document gives no status word ("prospective" since Jul 2025). A4 should confirm whether Integrow is the SM-REIT vehicle (checklist item 3). This filing does not say so. |
| F6-04 | F6 | N-C3, N-S3 | L552-L554 | "The balance 3 42 697 shares which are not fully paid due to unpaid call money are not available for trading" | NEUTRAL-FACT | Calls of 184 (161 + 23) are still unpaid 18 months after the final call (Mar 2025). Expect forfeiture or recovery. Immaterial. |
| F8-01 | F8 | LI014, LI012, LI015, N-C12 | L321-L324, L606 | "Deferred tax charge / (benefit) \| (135) \| (132) \| (196) \| (266) \| (316) \| (730)" | FORWARD-SIGNAL | Deferred tax is a credit in every period shown. Q2 ETR is 37.1% reported and 56.9% on current tax alone, against 25.17% statutory. The deferred shield is 1,979 bps in Q2 and 3,272 bps in H1. Note 12 magnitudes (133/267) suggest the source is DTL unwind on acquired intangibles [inference]. Locon adds about 31,900 of intangibles, so non-cash deferred credits should grow from Q3. They will flatter reported ETR while cash tax stays at the current-tax level. |
| F8-02 | F8 | LI081, LI105, LI239 | L411, L437, L830 | "Deferred tax assets (net) \| - \| 2,766" ; "Deferred tax liabilities (net) \| 5,044 \| -" ; standalone "Deferred tax assets (net) \| 602 \| 538" | AMBIGUOUS | Net deferred tax moved from +2,766 to -5,044 (a 7,810 swing). Over the same half the P&L booked deferred credits of about 325. The most likely source is DTL on the Locon PPA: 31,907 x 25.17% = about 8,031 [inference]. But the consolidated DTA is nil while the parent alone carries a DTA of 602. That suggests DTA/DTL were netted across entities. Ind AS 12 allows offset only within one taxable entity. Ask for gross DTA and DTL by entity and the Locon PPA DTL. |
| F9-01 | F9 | LI219 | L802 | "Other Comprehensive Income CONTINUING OPERATIONS (i) ... \| (2) \| (3) \| 2 \| (5) \| (0) \| (1)" | NEUTRAL-FACT | Standalone single-quarter remeasurement ((3) in Q1, (2) in Q2) is larger than the whole of FY26 ((1)). This meets the rule mechanically but is immaterial (Rs 0.03 Cr). Check the discount-rate assumption at the FY27 AR. Consolidated passes: Q2 (7) against FY26 21 (L332). |
| F10-01 | F10 | LI040, LI044, LI225, LI229 | L351, L355, L808, L812, L560 | "EPS TOTAL Basic (INR) \| 0.52 \| 5.94 \| (1.26) \| 5.79" | AMBIGUOUS | Implied weighted basic shares: Q1 4,557/5.94 = 767 lakh; Q2 451/0.52 = about 867 lakh; H1 5,008/5.79 = about 865 lakh. About 765 lakh shares were in issue until the 29 Sep 2026 issue. So Q2 and H1 should both be about 769 lakh. A day-weighted H1 built from 767 and 867 would be about 817, not 865. The Q2 and H1 denominators therefore cannot both be right. If the expected count holds, reported EPS is understated by about 11%. The standalone statement uses the same denominators. Ask for the share bridge. |
| F10-02 | F10 | LI045, LI041 | L352, L356, L569-L570 | "EPS TOTAL Diluted (INR) \| 0.50 \| 5.82 \| (1.26) \| 5.57" | FORWARD-SIGNAL | The basic-to-diluted spread widened from 2.0% (Q1) to 3.8% (H1; Q2 3.8% at coarse precision). Dilutive instruments are rising. The warrants allotted on 13 Oct 2026 add up to 51 lakh potential shares from Q3. A4 should cross-check against the ESOP pool and the 3,42,697 partly paid shares. |
| F12-01 | F12 | LI052, LI058, LI067, LI103, LI109 | L373, L379, L389, L435, L441 | "Segment Results CONTINUING OPERATIONS Rental \| 93 \| 63 \| (428)" ; "Finance cost \| (632)" | AMBIGUOUS (bear lean) | Rental segment result is +93 (Q2) and +156 (H1), but it is stated BEFORE finance cost, which sits unallocated. Lease liabilities of 21,691 (13,865 + 7,826) appear to sit mostly in Rental segment liabilities of 25,449 [inference]. On a lease-interest-inclusive basis, Rental is likely still loss-making. Checklist item 5 ("breakeven") depends on the definition. Rental assets fell 18% YoY (50,697 to 41,599) while revenue rose 10%. Lease-exit gains (451 H1, L470) feed OI, not the segment. |
| F12-02 | F12 | LI062, LI064, LI068 | L384, L386, L390 | "Unallocable Corporate assets \| 78,510 \| 21,360" ; "Segment Liabilities CONTINUING OPERATIONS Distribution \| 34,431 \| 7,058" | AMBIGUOUS | Unallocable assets rose 57,150 while goodwill plus intangibles rose 66,135. Distribution assets rose only 15,974, but Distribution liabilities rose 27,373 (4.9x). Acquired Locon liabilities sit in Distribution. Most acquired goodwill/PPA intangibles appear to sit unallocated [inference]. Distribution capital employed is understated until goodwill is allocated to a CGU, and the impairment test basis is not set. Ask where Locon goodwill sits (checklist item 7). |
| F12-03 | F12 | LI047, LI053 | L368, L374 | "Segment Results CONTINUING OPERATIONS Distribution \| 1,139 \| 797 \| 551" | AMBIGUOUS | Distribution segment result margin was 20.3% (Q2 FY26), 14.2% (Q1), 16.3% (Q2): down 400 bps YoY, up 210 bps QoQ. Segment result is not EBITDA, so checklist item 6 (EBITDA >=12%, not declining) cannot be scored from this table. Ask for Distribution EBITDA by brand, including PropTiger mix. |
| F14-01 | F14 | AP04, E-R1571 | L268, L238, L243 | "in respect of this subsidiary" ; "10 \| Locon Solutions Private Limited" / "15 \| Locon Solutions Private Limited" | NEUTRAL-FACT | The auditor paragraph 6 describes "one associate" and then calls it "this subsidiary". The entity table lists Locon twice (16 rows, 15 entities). These are drafting slips in the review report. Each is immaterial. Together they are a governance data point. |
| F14-02 | F14 | N-C2 (R1585), AP03 | L542, L227-L244 | "Helloworid Living Private Limited, wholly owned subsidiary of HelloWorld Technologies Private Limited, wef December 31. 202[5]" | AMBIGUOUS | Note 2 includes HelloWorld Living in the Group, but the auditor's para 4 entity list omits it. Ask whether HelloWorld Living is inside the limited-review scope, and its size. |
| F14-03 | F14 | N-C2 (R1638, R1699), E-R1568, E-R1573, E-R1564 | L541 vs L235/L577; L531 vs L240; L532 vs L231 | "PropTiger Marketing Services Private Limited, wholly owned subsidiary we f September 26, 2025" | NEUTRAL-FACT | The PropTiger date is 26 Sep in note 2 and 25 Sep in the auditor list and note 6. Page 12 is raw OCR, so this may be an OCR error (OCR_VERIFY). Monk Tech Labs is "wholly owned foreign subsidiary" in note 2 but "(Subsidiary)" in the auditor list. HelloWorld Technologies has "India" in its name in the auditor list only. |
| F14-04 | F14 | N-C12, LI014, LI105 | L606, L323, L437 | "Company has recognised deferred tax liability of INR' 133 lakhs and INR 267 lakhs respectively" | AMBIGUOUS | Note 12 says DTL recognised. The P&L shows a deferred tax BENEFIT of (135)/(266), and the BS DTL rose 5,044. The note matches neither the sign nor the balance. The standalone note 12 does tie: DTA 538 to 602 = 64 (L1010, L830). |
| F14-05 | F14 | LI163, LI198-LI201, LI158, LI315 | L505-L508 vs L660-L663; L502; L920 | "Cash flow from operating activities \| 710 \| 214 \| 840" vs note 14c "\| 710 \| 300 \| 840" ; "Interest and other finance charges paid \| (2) \| (1,711) \| (148)" | NEUTRAL-FACT | The H1 FY26 discontinued cash flow differs between the main CF (D = (60)) and note 14c (D = 14), a 74 gap. Both pages are image-verified. H1 FY26 interest paid (1,711) is larger than the FY26 full-year figure (148), so lease interest is classified differently across comparatives. The standalone shows the same pattern ((337) vs (53)). The real lease cash cost is about 4,779 in H1 (L501-L502). |
| F14-06 | F14 | PR003, PR004 (R1678), PR005 | L64-L66 | "Adjusted EBITDA Margin (%) 3.1% 11.5% +840 bps" ; "Total Income (₹ Cr) 88 137" | AMBIGUOUS | "Adjusted EBITDA" has no definition. Implied: 11.5% x 137 Cr = about 15.8 Cr. Statement EBITDA ex-OI is 3,386 (33.9 Cr). The gap is consistent with a lease-rent deduction [inference]. The Q2 FY26 base of 88 Cr = continuing 8,452 + discontinued 314. On a continuing basis growth is +62.5%, not +57%. The PBT margin of 4.8% is pre-associate PBT (660/13,731). Ask for the Adjusted EBITDA bridge. |
| F14-07 | F14 | AP05, AP06 (R051, R099) | L289, L765 | "UDIN: DE 1DVIGITGGEFSIGSS" ; "UDIN: 2642 VIED HERTEM $6 FO" | NEUTRAL-FACT | Both UDINs are illegible after OCR. They cannot be checked on the ICAI portal from this extract. The operator should check them against the exchange filing copy. |
| F15-01 | F15 | E-R1571, N-C4, MS09 | L238, L543, L561 | "Locon Solutions Private Limited \| (Wholly Owned Subsidiary) (Effective September 29, 2026)" | FORWARD-SIGNAL | New entity this quarter. Locon was consolidated one day before period end: full balance sheet, about 2 days of P&L. Cash acquired was 2,220 (L511). Other current liabilities rose 887 to 10,461 (L447), mostly acquired [inference]. Q3 is the first quarter showing Housing.com P&L, PPA amortisation and DTL unwind together. |
| F15-02 | F15 | E-R1563, E-R1565, E-R1567, N-C2 (R1585) | L230, L232, L234, L542 | "(formerly known as Aurum RealTech Services Private Limited)" | NEUTRAL-FACT | Three "formerly known as" renames (Liv Real, Aurum Analytica, YieldWiseX) and the HelloWorld Living addition (wef 31 Dec 2025) are in-document statements. With no prior-quarter list, it cannot be shown whether any rename is new this quarter. Integrow (subsidiary to associate, Jul 2025) and the ASSL merger into LIV (effective 31 Mar 2026, L610) are older changes. |

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 93 line items carry a nil cell. The meaningful ones are discontinued ops going nil (F1-01), doubtful-debt provision switching on (F1-02) and related-party loan lines going nil (F1-03). "Taxation in respect of earlier years" is nil in all periods (L322, L640). |
| F2 Standalone vs consolidated | FINDING | The PAT gap swung from -117.5% to +60.7% of standalone PAT QoQ (F2-01). Operating PBT ex-OI is still negative (F2-02). Interest on the consolidated external loan book is unexplained (F2-03). |
| F3 Shell-entity detection | PASS | Standalone vs consolidated: employee cost 201 vs 3,416, D&A 112 vs 2,806, other expenses 153 vs 6,217 (L787-L790 vs L312-L315). Subsidiaries run the operations. The standalone entity is the holding/treasury entity. Discontinued ops are the same in both (parent-owned buildings). No Going Concern EoM to reconcile. |
| F4 Unaudited contribution | FINDING | Associate share (79) = 20% of H1 continuing PAT (F4-01). No component-auditor paragraph. Locon and all subsidiaries are inside the K&P review per para 4 and para 6. |
| F5 Going concern / EoM | PASS | Neither review report has an EoM, Going Concern paragraph or modification (L253-L271, L736-L744). Conclusions are unmodified, consistent with the Q1 FY27 Notion record (K&P, unmodified). No prior fulltext, so the Other Matter paragraph (L264-L271) could not be compared word for word. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "is to be discharged" L559 (completed L560), "will be made" L564/L966, "shall be payable" L570/L973, "will be merged" L609 (completed L610), "completed" L551/L600, plus "in abeyance until" L585. Four findings, F6-01 to F6-04. Register in section 3. |
| F7 Hedge phrases | PASS | Zero hits for the F7 lexicon inside notes. The only hedge is the press-release safe harbour (L153-L157, boilerplate). The new "provisional" PPA caveat is carried once, under F6-01, not credited twice. |
| F8 Tax forensics | FINDING | ETR is 37.1% in Q2 (56.9% on current tax alone) against 25.17% statutory. Deferred credits are persistent (F8-01). DTA/DTL presentation (F8-02). Prior-year tax is nil. Standalone ETR is 26.0% in Q2, near statutory. Discontinued ETR was 13.1% in Q1 on the building gain (L328). |
| F9 OCI forensics | FINDING | Standalone remeasurement quarters exceed the FY26 total, immaterial (F9-01). Consolidated passes. |
| F10 Share count / dilution | FINDING | Paid-up rose 3,825 to 4,816 (+991). Locon shares account for 989.67 (1,97,93,309 x 5) and about 1.3 is call money/ESOP, so the bridge ties. The EPS denominators are internally inconsistent (F10-01). The diluted spread widened (F10-02). |
| F11 Reserves / net worth | PASS | Consolidated 4,816 + 96,549 = 1,01,365 (L431). Standalone 4,816 + 1,06,523 = 1,11,339 (L848). Both tie, and results-table reserves match the BS. Consolidated other-equity roll-forward: expected +50,023 (Locon premium 44,816 + owners' TCI 5,003 + SBP 201 + calls 3), actual +49,745, gap -278 (0.6%, under 5%). NCI rose 381 to 599 despite a (63) loss share and nil subsidiary share issue (L497). The +281 matches the gap, consistent with a transfer from owners to NCI [inference]. No third-party net worth figure in the document. |
| F12 Segment forensics | FINDING | Rental "profit" is pre-finance cost (F12-01). Locon goodwill sits unallocated while its liabilities sit in Distribution (F12-02). Distribution margin is down YoY (F12-03). Segment totals tie to the BS: 62,155 = 61,985 + 170. |
| F13 Board outcome | PASS | One agenda item, results approval (L34-L36). Meeting 11:00-12:30. Digital signature at 12:33:37 (L47) is consistent. No AR, AGM, director or fund-raise resolution. The 13 Oct 2026 warrant allotment board is disclosed in note 5 and covered under F6-02/F10-02. |
| F14 Note drafting inconsistencies | FINDING | Seven items, F14-01 to F14-07: auditor wording, HelloWorld Living scope, entity dates/names, note 12 sign, cash-flow comparatives, PR metric basis, illegible UDINs. |
| F15 Entity list diffs | FINDING | Locon added wef 29 Sep 2026 (F15-01). Renames and HelloWorld Living cannot be dated against a prior list (F15-02). |
| F16 Presentation: dropped / reframed | N.A. | Doctype is results. |
| F17 Concall: silence audit | N.A. | Doctype is results. The checklist touchpoints this filing evidences are mapped in section 4 for A4, as information only. |

## 3. COMMITMENT REGISTER (F6)

| Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|
| Locon PPA: adjust provisional fair values and goodwill | by 29 Sep 2027 (Ind AS 103 one-year cap; document says "within the measurement period") | C-note 4 L563-L564; S-note 4 L966 | underway |
| AREDL warrants: 75% balance (8,851.85) on exercise, optional, one or more tranches | by about 13 Apr 2028 (18 months from 13 Oct 2026 allotment) | C-note 5 L569-L571; S-note 5 L972-L974 | initiated (allotted; 25% received 13 Oct 2026) |
| Integrow: equity restructuring; board control in abeyance | 31 Mar 2027 | C-note 7 L584-L585; S-note 7 L988-L989 | underway ("prospective"; no status change stated) |
| Unpaid rights calls of 184 on 3,42,697 partly paid shares | none stated | C-note 3 L552-L554; S-note 3 L953-L955 | underway (open since Mar 2025) |
| Housing.com integration into the Aurum ecosystem | none stated | PR L56 | underway |
| AI-native real estate operating system | none stated | PR L57, L77 | underway ("continued development", "we are building") |
| Capitalised product development (374 Q2 / 711 H1 consolidated) | ongoing | C-note 11 L602-L604; S-note 11 L1006-L1008 | underway |
| Locon consideration discharged by issue of 1,97,93,309 shares | 29 Sep 2026 | C-note 4 L559-L560 | completed ("is to be discharged" then "discharged") |
| Navi Mumbai buildings sale at 11,200 | Q1 FY27 | C-note 14 L625-L627 | completed ("sale transaction was concluded") |
| ASSL merged into LIV | confirmation order 15 May 2026 | C-note 13 L608-L610 | completed |
| NestAway Technologies CCPS, holding to 99.78% (92) | Q2 FY27 | C-note 9 L596-L597 | completed |
| Rights calls: corporate action, 30,047 shares made fully paid | to 30 Sep 2026 | C-note 3 L551-L552 | completed |
| NestAway PropTech Mena further equity 101.63 (AED 3.83 lakh) | Q2 FY27 | C-note 8 L594 | completed |

## 4. CHECKLIST TOUCHPOINTS (information for A4; F17 itself is N.A. on results)

| Notion item | What this filing shows | Cite |
|---|---|---|
| 1 Operating profit ex one-times | Q2 operating PBT ex-OI = -52 (Rs -0.52 Cr), Q1 -486. This is the second consecutive negative quarter. A4 scores it. | L317, L309 (F2-02) |
| 2 Organic revenue ex-PropTiger | NOT DETERMINABLE. There is no entity split. PropTiger was consolidated from 25 Sep 2025, so the Q2 FY26 base holds about 6 days of it. Distribution revenue is +156% YoY. | L368, L577 |
| 3 SM-REIT | Not mentioned. Integrow abeyance runs to 31 Mar 2027. | L585 (F6-03) |
| 4 Receivables >1yr | No ageing in the filing. Provision 444 in H1 against nil. | L465 (F1-02) |
| 5 Rental breakeven | Segment +93 Q2 / +156 H1, but before lease interest. | L373, L379 (F12-01) |
| 6 Distribution EBITDA margin | Only segment result is available: 16.3%, down from 20.3% YoY. | L374 (F12-03) |
| 7 Goodwill | No impairment line. Goodwill 20,717 to 54,945 (provisional). The checklist baseline of 174.25 Cr does not match the audited Mar-26 goodwill of 207.17 Cr (L405). Reconcile the baseline. | L405 (F6-01, F12-02) |
| 8 Audit / RPT / auditor | Both reviews unmodified. Auditor K&P, partner Suhrud Lele, unchanged. No RPT note in the results. The AREDL named test is NOT DETERMINABLE here and needs the H1 Reg 23(9) RPT disclosure. The external loan of 952 with 201 interest is open. | L271, L736, L421, L467 (F2-03) |
| 9 Fund-raise | Swap issued 29 Sep 2026 at an effective Rs 231.42. Warrant 25% (2,950.62) received 13 Oct 2026. Same price for both. | L560, L569 (F6-02) |

## 5. GATE A3
All 17 checks marked (15 applicable, 2 N.A.). No blanks. gate_a3: pass.

```yaml
stage: A3-forensics
company: "AURUM"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\aurum-q2fy27\\work\\forensics_results_aurum_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "L327-L330, L627", classification: "NEUTRAL-FACT", implication: "Q2 discontinued ops nil; 4,552 of H1 net profit 4,947 (92%) is the Q1 building gain; residual held-for-sale liabilities 170 to settle"}
  - {id: "F1-02", check: "F1", line: "L465, L418", classification: "AMBIGUOUS", implication: "Doubtful-debt provision 444 in H1 FY27 vs nil H1 FY26 (1,487 over 18 months vs receivables 4,811); no ageing in filing; checklist item 4 unscored; bear lean"}
  - {id: "F1-03", check: "F1", line: "L498, L916-L917", classification: "NEUTRAL-FACT", implication: "No related-party borrowing/repayment in H1 FY27 (H1 FY26 repaid 1,589); does not answer the AREDL-loan named test"}
  - {id: "F2-01", check: "F2", line: "L325, L796, L318", classification: "NEUTRAL-FACT", implication: "Consolidated minus standalone PAT gap swung from -117.5% to +60.7% of standalone PAT QoQ; subs+elims -127 to +140; Locon drives the gap from Q3"}
  - {id: "F2-02", check: "F2", line: "L317, L309, L74", classification: "CONFIRMATORY-NEGATIVE", implication: "Operating PBT ex-OI -52 (Rs -0.52 Cr), second negative quarter after Q1 -4.86 Cr; at least 741 of H1 OI 1,429 non-recurring; PR claims positive PBT"}
  - {id: "F2-03", check: "F2", line: "L467, L421", classification: "AMBIGUOUS", implication: "Interest on loans 201 in H1 on a flat external loan book of 952 (about 42% annualised); borrower outside group not named; bears on AREDL named test"}
  - {id: "F4-01", check: "F4", line: "L264-L269, L318", classification: "AMBIGUOUS", implication: "Management-certified associate (79) = 20% of H1 continuing PAT; Q2 swing of +123 is 22% of QoQ PBT improvement on unreviewed numbers"}
  - {id: "F6-01", check: "F6", line: "L561-L564, L405-L406", classification: "FORWARD-SIGNAL", implication: "Provisional Locon PPA: goodwill +34,228, intangibles +31,907; D&A step-up from Q3; split can move until about 29 Sep 2027"}
  - {id: "F6-02", check: "F6", line: "L566-L571", classification: "FORWARD-SIGNAL", implication: "Warrants: 2,950.62 received 13 Oct 2026; optional 8,851.85 by about 13 Apr 2028; 51 lakh shares = 5.3% dilution; same Rs 231.42 price as Locon swap"}
  - {id: "F6-03", check: "F6", line: "L583-L585, L589", classification: "FORWARD-SIGNAL", implication: "Integrow control abeyance ends 31 Mar 2027 with a prospective equity restructuring; re-consolidation or restructuring is a dated catalyst; confirm the SM-REIT link"}
  - {id: "F6-04", check: "F6", line: "L552-L554", classification: "NEUTRAL-FACT", implication: "Unpaid rights calls of 184 on 3,42,697 shares, open since Mar 2025; forfeiture or recovery; immaterial"}
  - {id: "F8-01", check: "F8", line: "L321-L324, L606", classification: "FORWARD-SIGNAL", implication: "Deferred credit in every period; Q2 ETR 37.1% reported vs 56.9% current-only; shield 1,979 bps Q2 / 3,272 bps H1; Locon intangibles will enlarge non-cash credits from Q3"}
  - {id: "F8-02", check: "F8", line: "L411, L437, L830", classification: "AMBIGUOUS", implication: "Net deferred tax +2,766 to -5,044 (7,810 swing, likely Locon PPA DTL about 8,031 [inference]); consolidated DTA nil while parent DTA 602 implies cross-entity netting"}
  - {id: "F9-01", check: "F9", line: "L802", classification: "NEUTRAL-FACT", implication: "Standalone remeasurement (3)/(2) per quarter exceeds FY26 total (1); immaterial; check discount rate at FY27 AR"}
  - {id: "F10-01", check: "F10", line: "L351, L355, L808, L812, L560", classification: "AMBIGUOUS", implication: "Implied basic denominators Q1 767 / Q2 about 867 / H1 about 865 lakh vs about 769 expected with shares issued 29 Sep; Q2 and H1 cannot both be right; EPS possibly understated about 11%"}
  - {id: "F10-02", check: "F10", line: "L352, L356, L569-L570", classification: "FORWARD-SIGNAL", implication: "Basic-to-diluted spread widened from 2.0% (Q1) to 3.8% (H1); warrants allotted 13 Oct 2026 add up to 51 lakh potential shares from Q3"}
  - {id: "F12-01", check: "F12", line: "L373, L379, L389, L435, L441", classification: "AMBIGUOUS", implication: "Rental segment +93 Q2 is before finance cost; lease liabilities 21,691 appear to sit in Rental; breakeven definition for checklist item 5 is open; bear lean"}
  - {id: "F12-02", check: "F12", line: "L384, L386, L390", classification: "AMBIGUOUS", implication: "Unallocable assets +57,150 hold acquired goodwill/intangibles [inference] while Distribution liabilities +27,373 (4.9x); Distribution capital employed understated; CGU allocation pending"}
  - {id: "F12-03", check: "F12", line: "L368, L374", classification: "AMBIGUOUS", implication: "Distribution segment result margin 20.3% to 14.2% to 16.3% (down 400 bps YoY); not EBITDA, so checklist item 6 is unscored"}
  - {id: "F14-01", check: "F14", line: "L268, L238, L243", classification: "NEUTRAL-FACT", implication: "Auditor para 6 calls the associate 'this subsidiary'; Locon listed twice in the entity table"}
  - {id: "F14-02", check: "F14", line: "L542, L227-L244", classification: "AMBIGUOUS", implication: "HelloWorld Living in note 2 Group list but absent from auditor para 4 list; review scope unclear"}
  - {id: "F14-03", check: "F14", line: "L541, L235, L577, L531, L240, L532, L231", classification: "NEUTRAL-FACT", implication: "PropTiger date 26 vs 25 Sep 2025 (OCR_VERIFY); Monk Tech Labs and HelloWorld Technologies labels differ between note 2 and auditor list"}
  - {id: "F14-04", check: "F14", line: "L606, L323, L437", classification: "AMBIGUOUS", implication: "Consolidated note 12 says DTL recognised 133/267 but the P&L shows a benefit (135)/(266) and BS DTL rose 5,044; standalone note 12 ties"}
  - {id: "F14-05", check: "F14", line: "L505-L508, L660-L663, L502, L920", classification: "NEUTRAL-FACT", implication: "H1 FY26 discontinued CF differs main vs note 14c (D (60) vs 14); H1 FY26 interest paid 1,711 exceeds FY26 148; lease cash cost about 4,779 per half"}
  - {id: "F14-06", check: "F14", line: "L64-L66", classification: "AMBIGUOUS", implication: "Adjusted EBITDA undefined (implied about 15.8 Cr vs EBITDA ex-OI 33.9 Cr); Q2 FY26 base 88 Cr includes discontinued 314; continuing growth +62.5%"}
  - {id: "F14-07", check: "F14", line: "L289, L765", classification: "NEUTRAL-FACT", implication: "Both UDINs OCR-illegible; operator to verify on ICAI portal from the exchange copy"}
  - {id: "F15-01", check: "F15", line: "L238, L543, L561", classification: "FORWARD-SIGNAL", implication: "Locon added wef 29 Sep 2026; full BS but about 2 days of P&L; Q3 first quarter with Housing.com P&L, PPA amortisation and DTL unwind"}
  - {id: "F15-02", check: "F15", line: "L230, L232, L234, L542", classification: "NEUTRAL-FACT", implication: "Three 'formerly known as' renames and HelloWorld Living (wef 31 Dec 2025) cannot be dated against a prior list; no prior fulltext on file"}
forward_signals: ["F6-01", "F6-02", "F6-03", "F8-01", "F10-02", "F15-01"]
ambiguous: ["F1-02", "F2-03", "F4-01", "F8-02", "F10-01", "F12-01", "F12-02", "F12-03", "F14-02", "F14-04", "F14-06"]
commitments:
  - {commitment: "Locon PPA provisional fair values and goodwill to be finalised", implied_date: "by 2027-09-29 (Ind AS 103 cap)", ref: "C-note 4 L563-L564; S-note 4 L966", status_word: "underway"}
  - {commitment: "AREDL warrant exercise, 75% balance INR 8,851.85 lakhs, optional", implied_date: "by about 2028-04-13", ref: "C-note 5 L569-L571; S-note 5 L972-L974", status_word: "initiated"}
  - {commitment: "Integrow equity restructuring; board control in abeyance", implied_date: "2027-03-31", ref: "C-note 7 L584-L585; S-note 7 L988-L989", status_word: "underway"}
  - {commitment: "Unpaid rights calls INR 184 lakhs on 3,42,697 shares", implied_date: "none stated", ref: "C-note 3 L552-L554", status_word: "underway"}
  - {commitment: "Housing.com integration into the Aurum ecosystem", implied_date: "none stated", ref: "PR L56", status_word: "underway"}
  - {commitment: "AI-native real estate operating system build", implied_date: "none stated", ref: "PR L57, L77", status_word: "underway"}
  - {commitment: "Product development capitalisation (374 Q2 / 711 H1 lakhs)", implied_date: "ongoing", ref: "C-note 11 L602-L604", status_word: "underway"}
  - {commitment: "Locon consideration discharged by issue of 1,97,93,309 shares", implied_date: "2026-09-29", ref: "C-note 4 L559-L560", status_word: "completed"}
  - {commitment: "Navi Mumbai buildings sale at INR 11,200 lakhs", implied_date: "Q1 FY27", ref: "C-note 14 L625-L627", status_word: "completed"}
  - {commitment: "ASSL merged into LIV", implied_date: "2026-05-15", ref: "C-note 13 L608-L610", status_word: "completed"}
  - {commitment: "NestAway Technologies CCPS, holding to 99.78%", implied_date: "Q2 FY27", ref: "C-note 9 L596-L597", status_word: "completed"}
  - {commitment: "Rights-call corporate action, 30,047 shares fully paid", implied_date: "2026-09-30", ref: "C-note 3 L551-L552", status_word: "completed"}
  - {commitment: "NestAway PropTech Mena further equity INR 101.63 lakhs", implied_date: "Q2 FY27", ref: "C-note 8 L594", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Headline positive PBT (682) rests on other income: PBT before associate minus OI is -52 lakhs, the second negative quarter on checklist item 1 (Q1 -4.86 Cr). Q2 is the last quarter without Housing.com P&L. Q3 brings three moving parts together: amortisation of about 31,900 lakhs of provisional PPA intangibles, a larger non-cash DTL unwind credit that flatters ETR, and full-quarter Locon revenue. Separate them before reading margins. Checklist item 8 cannot be closed from this filing. There is no RPT note, and the 952-lakh external loan earning 201 lakhs in H1 (about 42% annualised) is the item to trace in the Reg 23(9) disclosure. The Rental breakeven and the Distribution margin are both segment-result figures before lease interest and before goodwill allocation. They are not checklist-grade metrics. The checklist goodwill baseline of 174.25 Cr does not match the audited Mar-26 figure of 207.17 Cr (L405). Reconcile it before scoring item 7. EPS denominators look internally inconsistent, in the understating direction."
```
