# A3 FORENSIC NOTES: FEDFINA (Fedbank Financial Services Ltd) Q2 FY27, doctype RESULTS

Agent: A3 forensics | model: claude-opus-5-5 | run date: 2026-10-17
Inputs read: A1 structured extraction (R001-R748, all rows), A1 fulltext (L1-L997, all 15 pages), A2 ledger (748 of 748 IDs). Prior-quarter extract: NONE (Q1 FY27 was concall only). The source PDF and inputs/ were not opened.
Units: INR Lakhs unless stated. Annexure I is in INR crore (Note 5, L818). All ratios marked "derived" are A3 arithmetic on filed numbers. They are not filed figures.
Lender (NBFC) readings applied throughout. The company has one segment (Note 7, L434), so F12 reads the whole balance sheet and asset quality.

## 0. RECONCILIATION AND PIPELINE NOTES

- Ledger reconciliation: 748 structured IDs, 748 referenced by the A2 ledger, 748 read here at their fulltext lines. 100%. MFS-1/2/3 (agenda enclosures prose, garbled UDINs) read at fulltext L46-58, L190, L730.
- PIPELINE DEFECT (A1 sign misreads, not flagged OCR_UNCERTAIN). The text layer renders an opening "(" as "1" on several OCI and tax cells. A1 carried the misread values. Tie-out against the filed totals gives the correct values below. These are DERIVED by arithmetic, not read. The orchestrator should confirm them against the source before any downstream stage uses them.

| Row | A1 value | Fulltext | Tie-out value | Tie-out used |
|---|---|---|---|---|
| R101 Deferred tax H1 FY26 | (170) | L235 "170)" | (70) | Current tax 5,336 + DT = Tax 5,266 (L232-233) |
| R134 FVOCI Loans Q1 FY27 | 15,851 | L243 "15,851" | (5,851) | OCI total (4,666) (L237) less not-reclassified (269) (L241) = reclassified (4,397); (4,397) - 213 + 271 - 1,512 |
| R135 FVOCI Loans Q2 FY26 | 12,005 | L243 "12,005" | (2,005) | OCI total (1,237) (L237); (1,237) - 352 - 416 |
| R136 FVOCI Loans H1 FY27 | 16,470 | L243 "16,470" | (6,470) | Q1 (5,851) + Q2 (619) |
| R137 FVOCI Loans H1 FY26 | 1,783 | L243 "1783" | (783) | Reclassified total (457) - 173 - 153 |
| R158 OCI reclassified Q1 FY27 | 14,397 | L249 "14,397" | (4,397) | (4,666) - (269) |
| R159 OCI reclassified Q2 FY26 | 11,237 | L249 "11 2371" | (1,237) | equals OCI total, not-reclassified nil |
| R160 OCI reclassified H1 FY27 | 11,883 | L249 "11 883" | (1,883) | (2,004) (L237) - (121) (L241) |

- OCR_UNCERTAIN rows resolved by tie-out (no finding rests on an unresolved value):
  - R187 reserves FY26 = 2,55,189 (BS L322).
  - R364 FD < 3 months H1 FY26 = 39,015 (49,822 - 602 - 10,205, L399-404).
  - R366 = 49,822 (L399).
  - R489 Annexure loans = 16,020.01 Cr (BS loans 16,02,001, L280).
  - R493 Annexure cash = 773.68 Cr (BS cash 77,368, L274).
  - R531 NNPA = 1.18% (L495).
  - R541 GNPA = 1.82% (L494).
  - The Annexure I totals tie to the balance sheet: assets 18,540.36 Cr = 18,54,036 (L777 vs L296), liabilities 15,375.40 Cr = 15,29,838 + 7,702 (L801 vs L311, L317), cover 14,998.92 / 12,077.26 = 1.24 (L803).
- Page 15 RPT table: the text layer is partly garbled (L943-L997). Any finding that rests on it says so.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R139-R144 (R141/R143/R144 ZERO_STANDING), R201-R202, R312-R313 | L244-245, L281, L371-372 | "Fair value gain I (loss) - OCI - Investment In Government Securities ... (325} 213 . (112) . ." | NEUTRAL-FACT | A new G-sec book opened in FY27. The line was nil in all FY26 periods. It is 213 in Q1 and (325) in Q2. CF shows G-sec bought (97,366) and redeemed 84,839 in H1. Investments rose 40,167 to 79,853. The company now carries mark-to-market risk through OCI on a liquidity book (LCR 156.85%, L496). |
| A3-02 | F1 | R468-R471, R718 (FOOTNOTE_UNRESOLVED) | L524-529 | "Number of accounts 48 ... Nol book value of loans transferred (at the time of transfer)' . Aggregate consideration (INR in Lakhs) 3" | AMBIGUOUS | 48 NPA accounts, including written-off loans, went to ARCs for Rs 3 lakh. Net book value is nil. The "Aggregate principal outstanding" and "residual tenor" rows are blank (L525-526). The asterisk on NBV has no footnote. The size of the written-off pool cannot be read from the filing. A4 question: principal outstanding sold, and Q1+Q2 FY27 write-offs. |
| A3-03 | F5 | R727, R662-R664, R616-R617, R639 | L168-175 | "were reviewed by one of the joint auditors, KKC & Associates LLP ... Our conclusion is not modified in respect of this matter." | AMBIGUOUS | This Other Matter paragraph is new in Q2 FY27. The paragraph itself states that Q1 FY27 was reviewed by KKC alone, so the joint-auditor arrangement starts this quarter. No Going Concern or EoM paragraph exists. V. Sankar Aiyar also signs the security cover certificate "as Statutory Auditor" (L591). [INFERENCE: the RBI joint-audit rule for entities with assets of Rs 15,000 Cr or more is a candidate trigger. Total assets were Rs 16,875 Cr at Mar 31 2026 (L296). This rule is not in the filing.] The board outcome has no auditor appointment item. A4 question: appointment date, trigger, tenure. |
| A3-04 | F6 | R388-R391, R424-R427, R537-R544, R653-R656, R519-R520 | L483, L493, L884-891, L803, L819 | "Total Debt to Equity ratio lo be within 6x 4.61x Complied" | FORWARD-SIGNAL | The newest secured NCD (trust deed 06 Jan 2026, L875) caps D/E at 6x. Older NCDs cap TOL/ATNW at 7.0. D/E went 3.78 (Sep 25) to 4.61 (Mar 26) to 4.89 (Jun 26) and back to 4.61 (Sep 26). Headroom to 6x is 1.39x of Rs 3,165 Cr net worth, about Rs 4,399 Cr of extra debt at constant net worth (derived). D/E fell in Q2, the same quarter as Rs 877 Cr of direct assignment (A3-12). CRAR fell 22.40% to 20.96% in H1 (floor 15-16%). Security cover is 1.24 against a 1.10 floor. Growth at the H1 pace needs equity, more DA or co-lending. A4 question on capital-raise timing. |
| A3-05 | F8 | R073-R102 | L231-235 | "Tax expense 4,725 ... Current tax 5,256 ... Deferred tax (531" | AMBIGUOUS | ETR (derived) was 26.54% in Q2 FY27, against 25.48% in Q1 FY27, 25.42% in Q2 FY26, 25.47% in FY26 and 25.17% statutory. Current tax is 29.53% of PBT. Deferred credits cut ETR by 298 bps in Q2 and 313 bps in Q1. DTA rose 938 to 2,613 (+1,675). That equals the P&L DT credit of 1,011 plus OCI tax of 622 + 42 exactly. Persistent DT credits on rising provisions reverse as a charge at write-off. A4 question: what drove the 106 bps QoQ rise in ETR. |
| A3-06 | F8 | R091-R096 (R091-R095 ZERO_STANDING) | L234 | "Short/ (Excess} provision for earlier years . . . . . (18" | NEUTRAL-FACT | The earlier-year tax line is non-zero only in FY26: an excess of (18). That is 0.04% of FY26 PBT and immaterial. It is nil in all FY27 periods. |
| A3-07 | F9 | R115-R132 (R117/R123/R129 ZERO_STANDING) | L239-241 | "Re-measurement of net defined benefit olan 198 (361 . (163 (107} (58)" | NEUTRAL-FACT | Actuarial items were (361) in Q1 FY27 and +198 in Q2. Each single quarter is larger than the full FY26 total of (58), about 6x. This points to a discount-rate or plan-asset assumption change. Verify at the FY27 Annual Report. Amounts are small (Rs 3.6 Cr). |
| A3-08 | F9 | R145-R150, R193-R194, R227-R228 (R228 ZERO_STANDING) | L247, L276, L300 | "instruments in a cash flow hedQe 4,348 1271) 352 4,077 173 3,182" | AMBIGUOUS | The Q2 FY27 cash-flow hedge gain of 4,348 alone is larger than the full FY26 total of 3,182. Derivative assets rose 21,502 to 27,846. A derivative liability of 416 appeared from nil. This reads as hedged foreign-currency borrowing with an FX or rate move. A4 question: size of FCY or ECB borrowing and the hedge tenor. The hedge reserve recycles to P&L as the hedged flows occur. |
| A3-09 | F9 | R133-R138, R157-R162 (A1 sign misreads, Section 0) | L243, L249 | "Fair value oain I /loss\• OCI - Loans (619 15,851 12,005 16,470 1783 (1,125)" | AMBIGUOUS | Tie-out values: FVOCI Loans (5,851) in Q1 FY27 and (619) in Q2, against (1,125) for all of FY26. The Q1 single quarter is 5.2x the prior full year. FVOCI loans are the hold-to-collect-and-sell (assignment) pool. An OCI loss here usually means fair-value gains moved to P&L on derecognition. A4 question: gain on derecognition booked in P&L in Q1 and Q2 FY27, and the share of PBT. This is profit quality. |
| A3-10 | F10 | R169-R186, R456-R467, R369 | L251, L254-255, L505-506, L429 | "- Basic (Rs .) 3.56 3.05 2.15 6.54" | AMBIGUOUS | Q2 FY27 EPS does not reconcile. PAT 13,075 / 3.56 implies 3,673 lakh weighted shares. Paid-up capital 37,514 is 3,751 lakh shares, and Q1 implies 3,750 lakh. Q1 3.05 + Q2 3.56 = 6.61, but H1 is 6.54, which implies Q2 at about 3.49. Diluted 3.53 implies 3,704 lakh shares, fewer than basic. That is impossible. The same 3.56/3.53 appears in the Reg 52(4) table (L505-506), so this is not an OCR error. The basic/diluted spread is stable at 0.7-1.0% in every period, so the dilution reading itself is clean. A4 question: will the company correct Q2 EPS. |
| A3-11 | F12 | R428-R443, R043-R048 | L494-497, L226 | "Gross Non Performing Assets (GNPA) 5 1.82% 1.55% 1.87% 1.90% ... Provision CoveraAe Ratio (PCR)7 35.37% 38.36% 32.29% 31.99%" | FORWARD-SIGNAL | GNPA rose 27 bps QoQ (1.55% to 1.82%). NNPA rose 22 bps (0.96% to 1.18%). PCR fell 299 bps (38.36% to 35.37%). The P&L impairment charge fell 20.5% QoQ (3,406 to 2,708). Part of the Q2 PBT rise (15,348 to 17,800, +16%) came from provisioning that did not track Stage 3. Monitoring item 2 (PCR at or above 38%, rising) fails. The 32% red line holds. The Pillar 2L clause "PCR thins further" is met QoQ but not against Mar 26 (32.29%). The operator must name the baseline. Covenant GNPA caps (4-5%) are far away. |
| A3-12 | F12 | R472-R479, R284-R285, R241-R242, R300-R301 | L533-537, L352, L310, L362 | "Aomeoate amount of Loan transferred <INR In Lakhsl 87,689 ... Retention of beneficial economic interest 10%" | AMBIGUOUS | Rs 877 Cr of loans not in default were assigned in Q2 alone. Residual maturity is 23 months, holding period 8 months, retention 10% and tangible security 100%. The tenor suggests LAP or housing, not gold loans [INFERENCE]. The CF excess-interest-spread adjustment flipped from (116) to +1,405. Other financial liabilities more than doubled, 21,638 to 46,819 (+116%). One reading: collections payable to assignees from a larger assigned pool. Another reading: other payables or margin money building up. A4 questions: off-book AUM, DA gain in P&L, and what makes up the other financial liabilities. |
| A3-13 | F12 | R189-R202, R290-R307, R545-R558, R628 (p15 OCR-garbled) | L274, L281, L357, L366, L956-961 | "(lncrease)/decrease in loans (1 ,84,315) 169" | NEUTRAL-FACT | The H1 FY27 loan build of Rs 1,843 Cr was funded by drawing cash down 42% (1,33,973 to 77,368) and by net new borrowing. Operating CF was (71,888). In H1 FY26 the loan book was flat (+169). Promoter Federal Bank funding is falling: term loan 1,06,597 to 90,542 (p15, OCR-garbled, "1.06 597.22"), WCDL 6,000, NCDs 23,470. Balances held with Federal Bank closed at 48,766 against cash of 77,368. Promoter-bank liquidity concentration and the funding mix are worth tracking. |
| A3-14 | F14 | R616-R617, R639 | L49-50, L107, L179, L559 | "M/s. V. Sankar Aiyar & Associates, Chartered Accountants, Joint Statutory Auditors" vs "V. Sankar Aiyar & Co." | NEUTRAL-FACT | The cover letter names a different firm style from the one on the review report and the certificate (FRN 109208W, L182). This adds to the governance drafting record. |
| A3-15 | F14 | R527-R528, R535-R536, R743-R744, R388-R390 | L841-844, L866-869 | "Total outstanding liability to Adjusted tangible net worth is not more lhan 7.0 4.61x Complied ... Calculaled based on audiled figures ie. For 31st March 2026" | AMBIGUOUS | The filed 4.61x equals the Reg 52(4) D/E at Mar 26 (4.61), which uses borrowings only. TOL/ATNW computed from the Mar 26 audited balance sheet is 13,94,868 / 2,91,283 = 4.79x (derived; ATNW = NW less DTA 938, intangibles 362, IAUD 27). For Sep 26 it is 4.90x. Either the trust deed defines TOL as borrowings or the label and number do not match. Headroom to 7.0 holds on either reading. |
| A3-16 | F14 | R562-R565 (R563/R564 ZERO_STANDING), R570-R573 (p15 OCR-garbled) | L963-966 | "Derivative Margin Deoosit - - 1615.50" | AMBIGUOUS | The approved limit is 24,500. The value during the half year is "-" and the opening balance is "-", yet the closing balance is 1,615.50. The table does not reconcile, subject to the p15 garble. Brand usage charges to the promoter were 184.97 in H1 (0.75% of H1 PAT, derived). A4 questions: the margin deposit flow and the basis and start date of the brand fee. |
| A3-17 | F14 | R680, R747, R699, R367, R506, R729 | L55-58, L734, L824, L936, L423, L784, L592-593 | "Disclosure of security cover ... as Annexure 1 ... related party transactions ... as Annexure 2" | NEUTRAL-FACT | Annexure labels collide. The cover letter has Annexure 1 = security cover and 2 = RPT. The filed pages carry "Annexure I" (security cover), "Annexure II" (covenant compliance) and "ANNEXURE-2" (RPT). Note 3 secured NCDs are 27,875 Lakhs, while Annexure I shows 279.28 Cr (27,928 Lakhs), a gap of 53 Lakhs that is likely accrued interest. The certificate scope covers "column A to J" only (L592-593). Each item is immaterial. Together they are a drafting data point. |

## 2. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing | FINDING | 38 ZERO_STANDING rows read. G-sec OCI line activated (A3-01). NPA-to-ARC table has blank principal/tenor and an unresolved asterisk (A3-02). The rest are template lines (IBC resolution categories, write-offs nil, no ESOS grants, no acquisitions, RPT opening nils). |
| F2 Standalone vs consolidated | PASS | Checked. Standalone only: "does not have any subsidiary/associate/join! venture" (Note 6, L432). The S-vs-C gap is zero in all periods. |
| F3 Shell entities | PASS | Checked. No subsidiaries (L432), so no shell candidates. No Going Concern EoM. |
| F4 Unaudited contribution | PASS | Checked. No JV, associate or component auditor. Rs 0 and 0% of PAT rests on unreviewed numbers. The whole statement is limited review (SRE 2410, L144-150). The prior-period comparatives were reviewed or audited by KKC alone (L168-174). |
| F5 Going concern / EoM scope | FINDING | No Going Concern or EoM paragraph. The new Other Matter paragraph records the first joint review (A3-03). The verbatim prior-quarter diff is not possible (no prior extract). Newness is shown by the paragraph's own text. |
| F6 Forward-commitment phrases | FINDING | Lexicon sweep found no milestone phrases. The only "commenc" hit is the meeting time at L78. The covenant "shall maintain ... until the Final Settlement Date" obligations go into the register. The leverage covenant is tightening against D/E (A3-04). |
| F7 Hedge phrases | PASS | Checked. No hits for "no assurance", "subject to", "evaluating", "exploring", "in discussions" or "endeavour" in the notes. Note 1 "implemented as and when they are Issued / applicable" (L418) is boilerplate. No prior notes exist to diff. |
| F8 Tax forensics | FINDING | Q2 ETR is 26.54%, 137 bps above statutory (A3-05). The earlier-years line is non-zero in FY26 (A3-06). The DTA movement ties exactly. |
| F9 OCI forensics | FINDING | The actuarial swing (A3-07), the hedge reserve swing (A3-08) and the FVOCI loans swing (A3-09) each exceed the full prior year in a single quarter. A1 sign misreads were corrected by tie-out (Section 0). |
| F10 Share count / dilution | FINDING | Paid-up 37,421 to 37,491 to 37,514 traces to ESOP allotments (Note 5, 2,35,701 shares in Q2, L429). The basic/diluted spread is stable at 0.7-1.0%. Q2 EPS does not reconcile (A3-10). |
| F11 Reserves / net worth tie | PASS | Checked. 37,514 + 2,78,982 = 3,16,496 = Reg 52(4) net worth (L321-323, L491). The roll-forward ties exactly: 2,92,610 + TCI 22,509 + equity issued 94 + premium 594 + application money 5 + SBP 684 = 3,16,496. This implies no dividend paid in H1 FY27. Annexure I totals tie to the balance sheet. |
| F12 Segment forensics (lender read) | FINDING | One segment (Note 7, L434). Lender read: Stage 3 rose while PCR and impairment fell (A3-11). Large DA and the other-financial-liabilities jump (A3-12). Funding and liquidity mix (A3-13). |
| F13 Board outcome | PASS | Checked. A single-item outcome: results plus enclosures a-e (L44-58). No AR, AGM, dividend, director, auditor or fund-raise item. Meeting ran 11.10 to 12:25 (L78). IDs are w.e.f. Sep 2024 to Jan 2025 (L987-997), so no term ends in the near window. The joint-auditor change without an agenda item is recorded at A3-03. |
| F14 Note drafting inconsistencies | FINDING | Auditor firm-name mismatch (A3-14). TOL/ATNW label vs D/E number (A3-15). RPT margin deposit does not reconcile (A3-16). Annexure numbering collision and minor tie gaps (A3-17). The Q2 EPS error is cross-referenced (A3-10). The note text says "limited review" (L422) and so does the auditor letter (L144), so they agree. |
| F15 Entity list diffs | PASS | Checked. The consolidation list is nil (L432, R648). No prior ledger exists, but there is no entity to diff. |
| F16 Presentation: dropped/reframed | N.A. | Results filing. The presentation check does not apply to this doctype. |
| F17 Concall: silence audit | N.A. | Results filing. The concall check does not apply to this doctype. The monitoring read-across is in Section 4 for A4. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Publish Q2/H1 results in Business Standard (English, all India) and Pratahkal (Marathi) | within prescribed timelines (Reg 47), about 17 Oct 2026 | Cover letter L61-64 (R649) | initiated ("would be publishing") |
| Maintain CRAR at or above 16% at all times (INE007N07041, INE007N07058) | until Final Settlement Date (undated) | Annexure II L833-835, L856-861 (R654) | complied (20.96%) |
| Maintain CRAR at or above 15% at all times (INE007N07066) | until Final Settlement Date (undated) | Annexure II L882-886 (R655) | complied (20.96%) |
| NNPA at or below 4%, GNPA at or below 5% standalone (07041, 07058) | tenor of debentures | L836-840, L862-865 | complied (1.18% / 1.82%) |
| NNPA at or below 3%, GNPA at or below 4% standalone (07066) | tenor of debentures | L887-890 | complied (1.18% / 1.82%) |
| Total outstanding liability / ATNW at or below 7.0 (07041, 07058) | tenor; tested on audited 31 Mar 2026 | L841-844, L866-869 (R653) | complied (4.61x as filed; see A3-15) |
| Total Debt / Equity within 6x (07066) | tenor; tested on 30 Sep 2026 | L891-894 | complied (4.61x) |
| Security cover at or above 1.10x on secured NCDs (Rs 27,875 Lakhs) | ongoing | Note 3 L423-424; Annexure I Note 6 L819 (R656) | complied (1.24x) |
| Implement RBI and regulator guidance as and when issued | ongoing | Note 1 L418-419 (R650) | boilerplate |
| Management certifies compliance with other NCD covenants | as at 30 Sep 2026 | Annexure II Part B L926-927 (R652) | completed (certified) |

No "initiated", "underway" or "completed" milestone language appears in the notes. Status-change tracking against Q1 FY27 is not testable because no prior results extract exists.

## 4. MONITORING CHECKLIST READ-ACROSS (informational for A4; F17 is N.A. on a results filing)

| # | Item | Q2 FY27 filed evidence | Read |
|---|---|---|---|
| 1 | Credit cost at or below 1.1% of avg assets; FY27 guidance | H1 impairment 6,114 (L226). Annualised over the Mar/Sep average of total assets 17,70,757 gives 0.69% (derived). Guidance: NOT DISCLOSED (results) | MET on level. The Q2 fall came with rising Stage 3 (A3-11) |
| 2 | PCR at or above 38% and rising (red below 32%) | 35.37%, down from 38.36% (L497) | NOT MET. Above the red line |
| 3 | Gold branches 140-150, AUM/branch above Rs 13.3 Cr | NOT DISCLOSED in results | Deck/concall item |
| 4 | Cost-to-income materially below about 57% and falling | Q2 52.47%, Q1 52.83%, Q2 FY26 56.86%, FY26 57.23% (derived: opex / total income less finance cost) | MET |
| 5 | ROE toward 14-15%, ROA at or above 2.5% | H1 annualised ROE 16.10%, ROA 2.77% (derived, two-point averages) | MET. Flattered by the lower Q2 provision (A3-11) and possibly by DA gains (A3-09, A3-12) |
| 6 | GNPA at or below about 1.9-2.1% | 1.82% (L494). Up 27 bps QoQ, down 8 bps YoY | MET on level, rising QoQ |
| 7 | ST LAP in-housing complete, disbursals above Rs 208 Cr | NOT DISCLOSED in results | Deck/concall item |
| 8 | Gold tonnage disclosed and rising | NOT DISCLOSED in results | Deck/concall item |
| T | Tripwires: credit cost above 1.1%; ROE below 14% by FY28; PCR below 32% | None fired | Pillar 2L "PCR thins further": met QoQ (-299 bps), not met vs Mar 26 (+308 bps). Baseline undefined. Operator ruling needed |

## 5. LOOP 1 ADDENDUM (correction loop 1, A5 gap; A2 added four ledger rows)

| New A2 row | Fulltext line | Verbatim | A3 review | Effect |
|---|---|---|---|---|
| Note 10(I) principal outstanding, NOT DISCLOSED | L525 | "Aggregate principal outstanding of loans transferred" (value cell blank) | Read. This blank cell is already covered by A3-02 | No new finding |
| Note 10(I) residual tenor, NOT DISCLOSED | L526 | "Weigh ted average residual tenor of the loans transferred" (value cell blank) | Read. This blank cell is already covered by A3-02 | No new finding |
| Annexure I company signature block | L812 | "For Fedbank Fin~ I Services Limited." | Read. Identity only, no signatory name or date in the text layer | No new finding |
| Annexure II company signature block | L932 | "For Fedbank Financia~ices Limited." | Read. Identity only, no signatory name or date in the text layer | No new finding |

The four rows were already read in the first pass, at L524-529 and L811-819 / L924-934. They change no F1-F17 status, finding, classification or commitment. Ledger reconciliation stays at 100% (752 of 752 rows, including the four new ones).

```yaml
stage: A3-forensics
company: "FEDFINA"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\fedfina-q2fy27\\work\\forensics_results_fedfina_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: PASS
  F4: PASS
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L244-245, L281, L371-372", classification: "NEUTRAL-FACT", implication: "New G-sec FVOCI book in FY27 (nil in FY26); investments 40,167 to 79,853; OCI MTM exposure on liquidity book"}
  - {id: "A3-02", check: "F1", line: "L524-529", classification: "AMBIGUOUS", implication: "48 NPA/written-off accounts sold to ARCs for Rs 3 lakh; principal outstanding and tenor blank, asterisk footnote missing; write-off pool cannot be sized"}
  - {id: "A3-03", check: "F5", line: "L168-175", classification: "AMBIGUOUS", implication: "New Other Matter: first joint review with V Sankar Aiyar in Q2 FY27; no EoM or Going Concern; appointment trigger and tenure not in filing"}
  - {id: "A3-04", check: "F6", line: "L483, L493, L884-891, L803", classification: "FORWARD-SIGNAL", implication: "Newest NCD caps D/E at 6x vs 4.61x (peak 4.89 Jun 26); CRAR 22.40 to 20.96; DA acting as leverage valve; capital raise or more DA needed at H1 growth pace"}
  - {id: "A3-05", check: "F8", line: "L231-235", classification: "AMBIGUOUS", implication: "Q2 ETR 26.54% vs 25.17% statutory and 25.48% Q1; current tax 29.5% of PBT; DT credit shield 298 bps; DTA +1,675 ties exactly"}
  - {id: "A3-06", check: "F8", line: "L234", classification: "NEUTRAL-FACT", implication: "Earlier-years tax (18) in FY26 only; immaterial"}
  - {id: "A3-07", check: "F9", line: "L239-241", classification: "NEUTRAL-FACT", implication: "Actuarial (361) Q1 and +198 Q2 each exceed FY26 full-year (58); assumption change; verify at FY27 AR"}
  - {id: "A3-08", check: "F9", line: "L247, L276, L300", classification: "AMBIGUOUS", implication: "Q2 cash-flow hedge gain 4,348 exceeds FY26 full year 3,182; derivative asset +6,344; FCY borrowing size and hedge tenor unknown"}
  - {id: "A3-09", check: "F9", line: "L243, L249", classification: "AMBIGUOUS", implication: "FVOCI loans (5,851) Q1 FY27 (tie-out corrected) is 5.2x FY26 full year; likely recycling to P&L on assignment; DA gain share of PBT is a profit-quality question"}
  - {id: "A3-10", check: "F10", line: "L254-255, L505-506, L251", classification: "AMBIGUOUS", implication: "Q2 EPS 3.56/3.53 does not reconcile: Q1+Q2 = 6.61 vs H1 6.54; diluted shares implied below basic; filed twice, not OCR"}
  - {id: "A3-11", check: "F12", line: "L494-497, L226", classification: "FORWARD-SIGNAL", implication: "GNPA 1.55 to 1.82, NNPA 0.96 to 1.18, PCR 38.36 to 35.37 while impairment fell 20.5% QoQ; Q2 profit partly from under-provisioning; checklist item 2 fails; Pillar 2L 'PCR thins further' met QoQ"}
  - {id: "A3-12", check: "F12", line: "L533-537, L352, L310", classification: "AMBIGUOUS", implication: "Rs 877 Cr DA in Q2 (23m residual, 10% retention); EIS adjustment flip to +1,405; other financial liabilities +116% to 46,819; off-book AUM and DA gain reliance"}
  - {id: "A3-13", check: "F12", line: "L274, L281, L357, L366, L956-961", classification: "NEUTRAL-FACT", implication: "H1 loan build Rs 1,843 Cr funded by 42% cash drawdown and borrowing; OCF (71,888); Federal Bank term loan falling; 48,766 held at promoter bank (p15 OCR-garbled)"}
  - {id: "A3-14", check: "F14", line: "L49-50, L179, L559", classification: "NEUTRAL-FACT", implication: "Cover letter 'V. Sankar Aiyar & Associates' vs report/certificate 'V. Sankar Aiyar & Co.'"}
  - {id: "A3-15", check: "F14", line: "L841-844, L866-869", classification: "AMBIGUOUS", implication: "TOL/ATNW filed 4.61x equals D/E; computed TOL/ATNW 4.79x Mar 26 and 4.90x Sep 26; definition or label mismatch; headroom to 7.0 holds"}
  - {id: "A3-16", check: "F14", line: "L963-966", classification: "AMBIGUOUS", implication: "RPT derivative margin deposit nil opening and nil flow but 1,615.50 closing (p15 OCR-garbled); brand fee to promoter 184.97 in H1"}
  - {id: "A3-17", check: "F14", line: "L55-58, L734, L824, L936, L423, L784", classification: "NEUTRAL-FACT", implication: "Annexure numbering collision; Note 3 NCD 27,875 vs Annexure 279.28 Cr; certificate scope columns A-J only"}
forward_signals: ["A3-04", "A3-11"]
ambiguous: ["A3-02", "A3-03", "A3-05", "A3-08", "A3-09", "A3-10", "A3-12", "A3-15", "A3-16"]
commitments:
  - {commitment: "Publish Q2/H1 results in Business Standard and Pratahkal", implied_date: "within Reg 47 timelines, about 2026-10-17", ref: "cover letter L61-64", status_word: "initiated"}
  - {commitment: "CRAR >= 16% at all times (INE007N07041, 07058)", implied_date: "until Final Settlement Date", ref: "Annexure II L833-861", status_word: "complied 20.96%"}
  - {commitment: "CRAR >= 15% at all times (INE007N07066)", implied_date: "until Final Settlement Date", ref: "Annexure II L882-886", status_word: "complied 20.96%"}
  - {commitment: "NNPA <= 4%, GNPA <= 5% (07041, 07058); NNPA <= 3%, GNPA <= 4% (07066)", implied_date: "tenor of debentures", ref: "Annexure II L836-890", status_word: "complied 1.18%/1.82%"}
  - {commitment: "TOL/ATNW <= 7.0 (07041, 07058)", implied_date: "tenor; audited 31 Mar 2026 basis", ref: "Annexure II L841-869", status_word: "complied 4.61x as filed"}
  - {commitment: "Debt/Equity within 6x (07066)", implied_date: "tenor; 30 Sep 2026 basis", ref: "Annexure II L891-894", status_word: "complied 4.61x"}
  - {commitment: "Security cover >= 1.10x on secured NCDs Rs 27,875 Lakhs", implied_date: "ongoing", ref: "Note 3 L423-424; Annexure I L819", status_word: "complied 1.24x"}
  - {commitment: "Implement RBI/regulator guidance as and when issued", implied_date: "ongoing", ref: "Note 1 L418-419", status_word: "boilerplate"}
  - {commitment: "Management certifies compliance with other NCD covenants", implied_date: "as at 2026-09-30", ref: "Annexure II Part B L926-927", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "loop_1: reviewed (L525, L526, L812, L932; no new finding). The main signal is lender asset quality (A3-11). GNPA rose 1.55% to 1.82% and PCR fell 38.36% to 35.37%, while the impairment charge fell 20.5% QoQ. Part of the 16% QoQ PBT rise came from provisioning that did not track Stage 3. Checklist item 2 fails; the 32% red line holds. The Pillar 2L clause 'PCR thins further' is met QoQ but not against March (32.29%), so the operator must name the baseline. Leverage (A3-04): D/E fell 4.89 to 4.61 in the quarter of Rs 877 Cr direct assignment, and the newest NCD caps D/E at 6x, so DA works as a leverage valve. A3-09 and A3-12 ask how much DA gain sits in profit. Q2 EPS 3.56 does not reconcile with PAT, share count or H1 6.54 (A3-10). PIPELINE: A1 misread '(' as '1' on R101, R134-R137 and R158-R160; tie-out values need source confirmation. OCR_UNCERTAIN rows R187, R364, R366, R489, R493, R531 and R541 resolve by tie-out. Gold, LAP and tonnage items are not in a results filing."
```
