# FORENSICS (results): RAYMONDREL Q2 FY27 (A3 FORENSIC NOTES)
Company: Raymond Realty Limited | Doctype: results (Board outcome + standalone/consolidated results + limited review reports + press release, one file) | Quarter: Q2 FY27 (quarter and six months ended 30 Sep 2026)
Inputs read: A1 structured (R001-R874, all rows), A1 fulltext (L1-L774, all lines), A2 ledger (all sections incl. M1-M4), Notion monitoring checklist copy (28-Oct-2026). Prior-quarter extract: none (first run for this ticker), so F5 and F15 set a baseline and cannot diff.
Units: statements Rs Lakhs (x0.01 = Rs Cr); press release Rs Cr. All computed figures below are A3 arithmetic on A1 values; the source rows are cited.

## 0. LEDGER RECONCILIATION
| ledger section | rows in ledger | rows read at cited line | note |
|---|---|---|---|
| 1 Notes N01-N13 | 13 | 13 | L309-327, L601-620, L303-305, L596-597 |
| 2 Line items L001-L184 | 184 | 184 | every value read at L167-198, L207-253, L261-301, L466-497, L506-551, L559-594 |
| 2b Table meta | 6 | 6 | |
| 3 ZERO_STANDING | 23 items / 48 cells | 23 / 48 | disposition in section 5 |
| 4 Board agenda B-A1..B-A3, B-T1, B-X | 5 | 5 | L42-69 |
| 5 Auditor paras A01-A13 | 13 | 13 | L97-151, L346-438 |
| 6 Signature blocks G01-G05 | 5 | 5 | |
| 7 Entities (50 rows) | 50 | 50 | |
| 7b Non-statement rows | all | all | |
| 8 Press release rows | all | all | L627-773 |
| 9 MISSING_FROM_STRUCTURED M1-M4 | 4 | 4 | read in fulltext at L427, L435, L147/L150/L437 |
Structured IDs: 874 of 874 read. ledger_reconciled_pct = 100.
A1 loop-back (labelling artefact, not a source defect): R303/R304 (L301) and R602/R603 (L594) are the unlabelled subtotal rows of the cash-and-cash-equivalents composition; A1 tags them "Deposits with maturity up to three months". The source line carries only the totals "8,664 | 9,434" and "12,575 | 10,249". No value is wrong.
OCR_UNCERTAIN R316/R831 resolved by reconciliation, see A3-07.

## 1. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | L081, L082, L028, L039 (R275-R278, R169-R170, R191-R192) | L285-286; L212, L225 | "ICD (given)/repaid (net) (12,760) \| -" ; "Loans given to subsidiaries (net) - \| (35,301)" | AMBIGUOUS | The lending line changed caption, the lending did not stop. Standalone loans rose 1,06,830 to 1,19,164 lakhs (+12,334, close to the 12,760 ICD). The consolidated balance sheet has no Loans line (L504-526), so the ICD counterparty sits inside the group. Standalone loans = Rs 1,191.6 Cr, top of checklist item 6 green band (Rs 1,000-1,200 Cr). At +Rs 123 Cr per half, red (>Rs 1,500 Cr) arrives in about 2.5 halves (around H2 FY28). |
| A3-02 | F1 | L078 (R269-R270), L027 (R167-R168), L122 (R478-R479) | L282; L211; L510 | "Purchase of non-current investments (2) \| -" | AMBIGUOUS | Standalone non-current investments rose 13,525 to 13,527 lakhs while consolidated stayed 110 \| 110. The Rs 2 lakh went into a group entity and eliminated on consolidation. That size fits share capital for a newly incorporated SPV. No prior entity list to confirm. A new JDA SPV would bear on checklist item 5 and inflection I-5 (signing pace). |
| A3-03 | F1 | L084, L085, L086 (R281-R286), L047, L050 (R207-R208, R213-R214), L140, L144 (R514-R515, R522-R523), L173-L175 | L289-291; L238, L243; L535, L541; L582-584; L715 | "Proceeds from short-term borrowings (net) 7,500 \| -" ; "With a 308 Crore liquidity buffer, we are fully funded for the next year of construction spends" | FORWARD-SIGNAL | New short-term borrowing line (75 Cr) and no holding-level term loan (nil vs 35,000). Term-loan raising moved to subsidiaries (consolidated proceeds 29,745 vs standalone nil). Standalone current borrowings 17,664 to 33,052; non-current 48,411 to 29,619 (maturities moving inside 12 months). Group current borrowings Rs 452 Cr exceed the Rs 308 Cr liquidity buffer. The "fully funded" claim covers construction spend, not the refinancing of current maturities. |
| A3-04 | F2 | L001, L015, L096, L110 (R028-R033, R112-R117, R339-R344, R423-R428); A11/A12 (R313-R327) | L167, L185, L466, L484; L397-398, L411-412 | "Profit for the period / year (3-4) 5,306 \| 1,343 \| 6,018" vs "4,155 \| 2,638 \| 5,841" | AMBIGUOUS | C-minus-S PAT as % of standalone PAT: Q2 FY27 +27.7%, Q1 FY27 -49.1%, Q2 FY26 +3.0%, H1 FY27 -2.1%, H1 FY26 -10.1%, FY26 +15.9%. Swing +24.7 pp YoY and +76.8 pp QoQ (above the 5 pp line). Decomposition: no JV or associate. Subsidiary PAT Q2 = 1,107 + 2 = 1,109; residual eliminations +42. H1 = (810) + 664 = (146) vs gap (144); residual +2. Subsidiary revenue Q2 47,134 vs Q1 28,870 (+63%). Standalone share of consolidated revenue: 37.4% Q2 FY27, 45.5% Q1, 56.2% Q2 FY26. The consolidated print now depends on lumpy revenue recognition inside the JDA subsidiaries (Q1 loss 1,255, Q2 profit 1,109). |
| A3-05 | F2 | L001 (R028-R030), R859, R734, R792 | L660-662; L167; L687 | "growth was achieved with no new project launches during the quarter, driven entirely by sustained sales velocity and steady price realization within the existing 'Address by GS' portfolio" | AMBIGUOUS | The press release credits Q2 growth to the existing Address by GS portfolio. Standalone revenue fell 29% YoY (39,176 to 27,995); all of the consolidated increase came from subsidiaries. The OC for Address by GS Season 1 Tower B (Thane) came in Q2 FY27, yet standalone revenue barely moved QoQ (23,989 to 27,995). This leaves open which entity books Tower B, which Ind AS 115 method applies (point in time on OC vs over time), and how much of Q2 subsidiary revenue is a one-off OC trigger. |
| A3-06 | F4 | A11, A12 (R311-R328, R716-R717, R830, R832) | L394-398; L409-412 | "We did not review the interim financial information of 5 subsidiaries" ; "we did not jointly review the interim financial information of 2 subsidiaries" | AMBIGUOUS | 5 + 2 = 7 = every subsidiary in Annexure 1. The joint-auditor pair jointly reviewed only the holding company. 5 subs (other auditors): Q2 PAT 1,107 = 20.9% of consolidated Q2 PAT (above 10%); Q2 revenue 44.9%; total assets 48.9%; H1 PAT (810) = 12.2% absolute. 2 subs (one joint auditor alone): assets 23.8%, H1 revenue 24.5%, H1 PAT 664 = 10.0%. Together the subsidiaries hold 63.0% of Q2 consolidated revenue and 72.7% of gross consolidated assets. The JDA growth engine is reviewed outside the joint pair. No prior extract, so the YoY trend is the baseline from this quarter. |
| A3-07 | F4 | R316, R318, R831 (OCR_UNCERTAIN) | L397-398 | "z 1,107 lakhs and z (81 O lakhs)" | NEUTRAL-FACT | The reading (810) is corroborated. H1 subsidiary PAT (810) + 664 = (146) against the C-S H1 gap of (144), residual +2 lakhs. A reading of (81) would leave a residual of 727, against +42 in Q2. Downstream stages may use (810). |
| A3-08 | F6 | R757, R751, R685-R687, R646; L106, L102, L103, L098 | L723-724; L665-666; L479, L475, L476, L468 | "remains on track for ~20% growth in pre-sales, ROCE of ~20%, EBITDA margin of 17-19% and PAT margin of 9-10%" | FORWARD-SIGNAL | H1 FY27 EBITDA margin (PBT + finance costs + D&A on total income, the press-release basis) = 14.3%; Q1 13.1%, Q2 15.2%. At FY26 total income (Rs 3,039 Cr), the FY27 band needs an H2 margin of 19.0-22.5%. FY26 H2 delivered 18.2% (FY26 full year 16.3%, below the band). PAT margin 9-10% needs H2 11.9-13.6% vs H1 5.1% and FY26 H2 11.7%. The guidance is reaffirmed, and H2 must beat last year's H2 to meet it. |
| A3-09 | F6 | R753, R754, R665-R673, R794 | L702-704 | "accelerating our growth trajectory over the next two quarters ... The current financial year will feature two premier JDA project launches" | FORWARD-SIGNAL | Mahim 1 (GDV 1,800 Cr) and Mahim 2 (2,300 Cr) are now dated "next two quarters / current financial year", a window that includes Q4 FY27. Checklist item 4 marks "Delay to Q4 FY27+" red and "Q3 FY27 launch as guided" green. The release no longer pins Q3. |
| A3-10 | F6 | R687, R757 | L724 | "PAT margin of 9-10%" | FORWARD-SIGNAL | Management guides a PAT margin for FY27. Inflection I-6 records the current state as "continued refusal" to guide PAT/OCF. This is either a first PAT guide (I-6 partial green, PAT only, no OCF) or the Notion state is stale. A4 checks which. |
| A3-11 | F7 | R860, R750 | L663-665 | "While margins naturally fluctuate by project phase due to upfront marketing and construction setup costs, they are expected to normalize progressively" | AMBIGUOUS | This is pre-emptive cover for an H1 margin (14.3%) below the 17-19% guide. Read it with A3-08: the hedge prepares for a back-ended year. The statement notes carry no hedge. The disclaimer at L756 ("subject to certain risks and uncertainties") is boilerplate. |
| A3-12 | F8 | L012-L014, L107-L109 (R094-R111, R405-R422); L030, L124, L142, L031, L125, L056, L150; L073, L166 | L182-184; L481-483; L214-215, L250; L512-513, L537; L276, L573 | "Total tax expense 922 \| 618 \| 1,297 \| 1,540 \| 1,939 \| 6,273" | AMBIGUOUS | ETR vs statutory 25.17%. Standalone: Q2 18.2%, Q1 19.0%, Q2 FY26 18.2%, H1 18.5%, H1 FY26 18.5%, FY26 19.3%. Consolidated: Q2 20.0%, Q1 11.5%, Q2 FY26 14.2%, H1 18.4%, H1 FY26 16.3%, FY26 18.7%. The shield is persistent: about 670 bps, or Rs 5.6 Cr on H1 standalone PBT. The source is not disclosed. Standalone deferred tax flipped from credits (FY26 (583)) to charges (Q1 49, Q2 59); DTA 4,374 to 4,265 is unwinding. Taxes paid exceed current tax: standalone 2,359 vs 1,432, non-current tax asset nil to 717; consolidated 2,946 vs 1,441, 326 to 1,620. That points to an H2-weighted full-year taxable-income estimate, or a demand. No prior-year tax line. |
| A3-13 | F10 | L020, L022-L023, L044-L046, L115, L117-L118, L137-L139 (R142-R160, R201-R206, R453-R471, R508-R513); L067 | L194, L197-198; L493, L496-497; L232-234, L529-531; L269 | "Diluted 6.24 \| 3.96 \| 8.77 \| 10.20 \| 12.82 \| 39.23" (identical to Basic) | AMBIGUOUS | Paid-up capital is flat at 6,657 lakhs in every period. Basic = diluted in all twelve EPS cells, though an ESOP charge exists (share-based payment 160). The other-equity roll-forward closes with PAT, dividend and SBP only (standalone 1,48,832 + 6,793 - 1,331 + 160 = 1,54,454 vs 1,54,453; consolidated diff 2). No warrant money was credited in H1 FY27, and financing cash flow has no warrant inflow (L289-293, L582-586). The Notion tracker carries "warrant money received (Rs 102 Cr upfront...)". If received, it predates 31-Mar-2026 or sits outside this entity. A4 runs the cross-check. |
| A3-14 | F11 | R619, R628, R636-R640, R622, R631, R634, R674-R676, R678; L098, L106, L102, L103, L140, L144, L131, L132, L129, L137-L139 | L644-657; L712-715 | "Gross debt of 1,220 Crore and Net Debt of 912 Crore and a debt / equity ratio of 0.8x" | NEUTRAL-FACT | The press release reconciles to the statements. Total income 757 = 75,749. PBT 66 = 6,632. EBITDA 115 = PBT 6,632 + finance costs 4,353 + D&A 539 = 11,524 (includes other income 897; Q2 FY26 101 = 10,106). Gross debt 1,220 = 76,780 + 45,193. Liquid funds computed 303.6 Cr (cash 12,575 + other bank 7,919 + current investments 9,864) vs PR 308; net debt 916 vs PR 912, a gap of 4.4 Cr (0.5%). D/E 0.8x = gross debt / equity 0.752 rounded up; net debt / equity 0.56x. PBT YoY "(6%)" vs -5.4% on lakh values (rounding from Cr). Net worth tie: 6,657 + 1,55,561 = 1,62,218; no minority interest. |
| A3-15 | F11 | R680-R682, R872; L102 (R375) | L717-719; L475 | "~17 Crore is towards Interest to Government authorities: BMC/TMC / MHADA for Additional FSI and Approvals" | AMBIGUOUS | 17 of the 44 Cr Q2 finance cost (39%) is interest to authorities on FSI and approvals, a development-rights cost that sits below EBITDA. Treated as a project cost, Q2 EBITDA is about 98 Cr and the margin about 13.0%, below the 14% stop line. Q1 and Q2 FY26 comparables are not disclosed. This bears on the pending operator ruling on which margin stop binds. |
| A3-16 | F12 | L140, L144, L131, L132, L129 (R514-R515, R522-R523, R496-R499, R492-R493); R625-R627 | L535, L541, L519-522; L646 | "Net Debt of 912 Cr, Debt to Equity ratio of 0.8x, well below the ceiling of 1.0x" | FORWARD-SIGNAL | Computed net debt was Rs 657.8 Cr at 31-Mar-2026 (checklist item 3 baseline Rs 656 Cr) and is Rs 916 Cr (PR 912) at 30-Sep-2026. That is +Rs 258 Cr in H1, about Rs 129 Cr per quarter, against the tracker's +Rs 90 Cr per quarter. Two risk-matrix #2 first signals are now on: net debt above Rs 900 Cr and gross D/E 0.752x above 0.75x. At the H1 pace, the Rs 1,000 Cr checklist line is crossed in Q3 FY27. |
| A3-17 | F12 | L147 (R528-R529), R869 | L545; L712 | "(iii) Other financial liabilities 1,90,820 \| 1,76,021" | AMBIGUOUS | Rs 1,908 Cr of current other financial liabilities (+Rs 148 Cr in H1) sits outside borrowings and outside PR net debt. The net debt definition is not stated (R869). The pending operator ruling on the Rs 210 Cr AIF subsidiary funding needs the composition of this line: landowner/JDA payables, deposits, deferred premium to authorities, or any debt-like instrument. |
| A3-18 | F12 | L128, L148, L163, L167 (R490-R491, R530-R531, R560-R561, R568-R569); L099; R615-R617 | L517, L546, L570, L574; L471; L638-640 | "Net cash used in operating activities (14,702) \| (31,908)" | FORWARD-SIGNAL | Single segment (Note 3, L320/L613), so the whole balance sheet is the segment. Inventories rose 16.8% (+71,760) and other current liabilities (customer-advance line) rose 47.2% (+47,959), so customer money funds a large part of the build. Consolidated H1 CFO was -Rs 147 Cr vs -Rs 319 Cr in H1 FY26; annualised that is better than the tracker model of FY27 -Rs 600 Cr. Inflection I-2 is still on the red side: H1 collections of Rs 1,233 Cr sit below the H1 cost of land, development and construction of Rs 1,674.7 Cr. |
| A3-19 | F12 | L005, L070, L100, L163 (R052-R057, R253-R254, R363-R368, R560-R561) | L174, L273; L473, L570 | "Changes in inventories of properties under development and finished properties ... (16,472)" vs "Increase in inventories (9,517)" | AMBIGUOUS | WIP plus finished stock rose 6,955 lakhs more than total inventory at the holding (standalone 16,472 vs 9,517; consolidated 78,712 vs 71,760, gap 6,952). In H1 FY26 the gap was only 122 (standalone). About Rs 69.5 Cr of non-WIP inventory (land or development rights, at the holding, so likely Thane) moved into development in H1 FY27. That may be a new Thane phase entering construction, which ties to the tracker row "Thane Jekegram launch (RERA) in FY27". |
| A3-20 | F12 | L041, L069, L074, L134 (R195-R196, R251-R252, R261-R262, R502-R503) | L227, L272, L277; L524; L285 | "(Decrease)/ increase in trade and other receivables 18,779 \| (608)" | AMBIGUOUS | Standalone CFO of +Rs 142 Cr comes from a Rs 217 Cr fall in standalone other current assets (85,001 to 63,262). Consolidated other current assets rose (2,06,672 to 2,22,484). In the same half the holding gave an ICD of 12,760. If the release was intra-group (for example an advance to a subsidiary or a JDA-landowner deposit), standalone CFO does not represent customer collections. |
| A3-21 | F14 | N05, N10 (R825, R854); R703; R748 | L327, L620; L76-77; L768 | "Previous periods' figures have been regrouped, whenever considered necessary" ; "(formerly known as Raymond Lifestyle Limited)" | AMBIGUOUS | The document has no demerger, perimeter or comparability note; only the generic regrouping note. The Q2 FY26 and H1 FY26 comparatives (Jul-Sep 2025, the demerger year) carry no basis statement. Only the cover letter carries the former name "Raymond Lifestyle Limited"; no statement page, note or review report does. The press-release contact sits at "Raymond Limited" (shared group services; ties to risk #1). YoY comparisons in this filing rest on an unstated perimeter. |
| A3-22 | F14 | N01, N02, N06, N07 (R821-R822, R850-R851); R638 | L312, L605; L316-317, L609-610; L656 | "Section 133 of of the Companies Act" ; "approved by the Board of Directors at their meeting held on 27 October 2026 respectively" | NEUTRAL-FACT | Minor drafting slips: duplicated "of of" in both Note 1s; "respectively" against a single date; PR PBT YoY "(6%)" vs -5.4% on lakh values. Note 2 ("limited review") matches the auditor letters and enclosure 2. There is no audit vs review mismatch. Individually immaterial. |
| A3-23 | F15 | R721-R722, R835; R332-R338 | L447; L444-450 | "4. Ten X Realty North Limited (formerly known as Chembur Realty Limited)" | AMBIGUOUS | Rename recorded: Chembur Realty Limited to Ten X Realty North Limited, effective date not stated; the entity moves into the TenX brand family. Consolidation list: 7 subsidiaries (baseline; no prior list to diff). Read with A3-02 (Rs 2 lakh group investment): a possible new SPV may not yet appear in Annexure 1. |

## 2. CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 | FINDING | 23 ZERO_STANDING items reviewed (section 5). Template signals: ICD caption replacing loans-to-subs (A3-01), Rs 2 lakh group investment (A3-02), new short-term borrowing line and term-loan shift to subs (A3-03). |
| F2 | FINDING | C-S PAT gap swung +24.7 pp YoY and +76.8 pp QoQ; decomposed to subsidiary PAT with residual eliminations of +42 (Q2) and +2 (H1); no JV or associate (A3-04, A3-05). |
| F3 | PASS | No shell found at aggregate level. Consolidated vs standalone Q2 cost of land 1,26,082 vs 17,331, employee 4,771 vs 4,161, other expenses 7,316 vs 5,006 (L471-477 vs L172-178), so the subsidiaries operate. Per-entity cost data is not disclosed. No Going Concern EoM. The 2 subs have near-nil Q2 PAT (2 lakhs) on Rs 1,881 Cr assets (L410-412). That is a margin point, not a shell signal. |
| F4 | FINDING | 5 subs reviewed by other auditors = 20.9% of Q2 consolidated PAT (above 10%); all 7 subs sit outside joint review (A3-06). No prior extract, so the YoY jump test is baselined. OCR value (810) corroborated (A3-07). |
| F5 | PASS | Neither review report carries an EoM or Going Concern paragraph. Standalone conclusion is unmodified (L130-136). Consolidated conclusion is unmodified (L385-392), and the reliance paragraphs end "Our conclusion is not modified" (L422). No prior quarter text to diff; this quarter is the baseline. |
| F6 | FINDING | Lexicon hits: "will be accelerated" (L666); near-hits "expected to normalize" (L664), "will feature" (L704), "on track" (L665, L723); status word "Completed Projects" (L687). Commitments in section 3 (A3-08, A3-09, A3-10). |
| F7 | FINDING | Margin-lumpiness hedge in the press release (A3-11). Disclaimer "subject to certain risks" (L756) is boilerplate. No hedge in the statement notes. |
| F8 | FINDING | ETR persistently about 670 bps below 25.17%; deferred-tax sign flip; taxes paid exceed provision. No earlier-years tax line (A3-12). |
| F9 | PASS | OCI is nil in all interim periods; only the FY26 year-end remeasurement (standalone 206, consolidated 203; L188, L487). No single-quarter swing, so no assumption-change signal. Remeasurement is booked at year end only. |
| F10 | FINDING | Share capital flat; basic = diluted in all periods despite an ESOP charge; no warrant money in the H1 equity roll or cash flow (A3-13). |
| F11 | FINDING | Net worth ties exactly (standalone 6,657 + 1,54,453 = 1,61,110; consolidated 1,62,218). PR numbers reconcile (A3-14). EBITDA excludes Rs 17 Cr of authority interest (A3-15). |
| F12 | FINDING | Single segment, so the whole balance sheet is the segment: net debt pace (A3-16), other financial liabilities outside net debt (A3-17), advance-funded inventory build and CFO (A3-18), land-to-WIP gap (A3-19), standalone other-current-asset release (A3-20). |
| F13 | PASS | The Board approved only the results, review report and press release (L49-66). No AR, AGM, dividend, director, auditor, ESOP or capital-raising item. The phrase "inter alia" (L50) leaves room for separately filed items; A4 may check same-date exchange filings. |
| F14 | FINDING | No demerger or comparability note; former-name tag only on the cover letter (A3-21). Minor drafting slips; review vs audit wording is consistent (A3-22). |
| F15 | FINDING | Rename Chembur Realty to Ten X Realty North (A3-23); 7 subsidiaries baselined. |
| F16 | N.A. | Results filing; the presentation check does not apply. The press release sits inside this results file; its numbers are reconciled under F11. |
| F17 | N.A. | Results filing; there is no call transcript for a silence audit. Checklist touchpoints are mapped in section 4 for A4. |

## 3. COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| FY27 EBITDA margin 17-19% ("on track") | 31-Mar-2027 | PR L665-666, L724 (R751, R686) | underway |
| FY27 pre-sales growth ~20%, ROCE ~20%, PAT margin 9-10% | 31-Mar-2027 | PR L723-724 (R684-R687, R757) | underway |
| Margins "expected to normalize progressively" | H2 FY27 | PR L664-665 (R750) | underway |
| Mahim 1 (GDV 1,800 Cr) and Mahim 2 (GDV 2,300 Cr) launches, "next two quarters" / "current financial year" | Q3-Q4 FY27, by 31-Mar-2027 | PR L702-709 (R753-R754, R665-R673) | initiated (planned; no RERA or launch evidence in the document) |
| Operational growth "will be accelerated" by the MMR launch pipeline (>4,100 Cr GDV) | H2 FY27 | PR L666-668, L733 (R752, R758) | initiated |
| "fully funded for the next year of construction spends" (Rs 308 Cr buffer) | through about Sep-2027 | PR L715 (R756, R871) | underway |
| Debt/equity ceiling 1.0x | standing | PR L646, L714 (R627, R677, R755) | underway |
| OC received, Address by GS Season 1 Tower B (270 units), RERA date was Mar-28 | Q2 FY27 | PR L687-689, L732 (R734, R793, R690) | completed |
| Final dividend Rs 2/share FY26, paid 14-Jul-2026 | 14-Jul-2026 | Note 4, L324-325, L617-618 (R306-R308, R605-R606); CF L292, L585 | completed |
| Website intimation of the outcome (Reg 30/46) | 27-Oct-2026 | L68-69 (R749) | completed (boilerplate) |

## 4. CHECKLIST TOUCHPOINTS FOR A4 (informational; F17 is N.A. on a results filing)
| Notion item | document evidence | reading |
|---|---|---|
| 1 EBITDA margin | Q1 13.1%, Q2 15.2% (PR basis); about 13.0% if authority interest counts as cost (L717-719) | <14% stop not fired on headline; <15% not fired (15.2%); <18% fired both quarters; ruling pending |
| 2 Booking value | Q1 = 1,602 - 902 = Rs 700 Cr (L634-636) | green (>= Rs 500 Cr) |
| 3 / I-3 Net debt | Rs 912 Cr PR (computed 916), from Rs 658 Cr | not red (<Rs 1,000 Cr); not green (rising); see A3-16 |
| 4 Mahim launch | "next two quarters" / current FY (L702-704) | window includes Q4 FY27 (red zone); A3-09 |
| 5 New JDA signings | "eight projects" (L691); no new signing disclosed | silent in this document; A3-02 possible SPV |
| 6 Loans to subs | standalone loans Rs 1,191.6 Cr (L212 + L225) | top of green band; A3-01 |
| 7 Promoter governance | nothing in the document; PR contact at Raymond Limited (L768) | silent |
| 8 Cost of debt | "~9.60%" (L716) | green (9.5-9.75%) |
| 9 Thane commercial | not mentioned | silent |
| 10 / I-7 CFO | consolidated H1 -Rs 147 Cr (L574) vs -Rs 319 Cr H1 FY26 | still negative; improving |
| I-1 Delivery / OC | OC only for Thane Tower B (L687); no MMR JDA handover | red-side reading ("only Thane delivering") |
| I-2 Collections vs WIP | collections Rs 1,233 Cr vs cost of land/dev Rs 1,674.7 Cr H1 | red-side; A3-18 |
| I-6 PAT/OCF guidance | PAT margin 9-10% guided (L724) | possible partial green; A3-10 |

## 5. ZERO_STANDING DISPOSITION (F1, 23 items / 48 cells)
| ledger | line item | why the line exists / what it anticipates | disposition |
|---|---|---|---|
| L016-L018, L111-L113 | OCI remeasurement, tax, total OCI | actuarial gains/losses; booked at year end only | year-end policy; F9 PASS |
| L031 | Standalone non-current tax assets (Mar-26 nil, Sep-26 717) | advance tax in excess of provision | A3-12 |
| L035 | Standalone current investments (Mar-26 nil, Sep-26 7,779) | mutual fund parking (CF L281 (7,637) + FV gain 141 = 7,778) | ties |
| L056, L150 | Current tax liabilities (Sep-26 nil) | provision settled by advance tax | A3-12 |
| L064, L158 | Gain on sale of investments (H1 FY27 nil) | MF redemption gains; H1 FY27 was a net MF buyer | no sale in period |
| L066 | Loss on disposal of PPE* (both nil) | asset disposals; amount below rounding (L303) | immaterial |
| L078 | Purchase of non-current investments (H1 FY26 nil, H1 FY27 (2)) | subscription to group-entity capital | A3-02 |
| L080 | Investment in preference shares of subs (H1 FY27 nil vs (10,000)) | equity-type funding of subs | paused this half; funding switched to ICD |
| L081, L082 | ICD given (new) / loans to subs (H1 FY27 nil) | intra-group lending | A3-01 |
| L084, L173 | Proceeds from short-term borrowings (H1 FY26 nil) | working-capital / CP-type borrowing | A3-03 |
| L086 | Proceeds from term loans, standalone (H1 FY27 nil) | holding-level term debt | A3-03 (moved to subs) |
| L087, L176 | Dividend paid (H1 FY26 nil) | first final dividend, Rs 13.31 Cr = Rs 2 x 6.657 Cr shares | ties to Note 4 |
| L094 | Deposits up to three months (H1 FY26 nil) | cash-equivalent deposits | treasury mix |

```yaml
stage: A3-forensics
company: "RAYMONDREL"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/raymondrel-q2fy27/work/forensics_results_raymondrel_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: FINDING
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "L285-286; L212; L225", classification: "AMBIGUOUS", implication: "Loans-to-subs caption became ICD (12,760); standalone loans Rs 1,191.6 Cr, top of checklist item 6 green band; red >Rs 1,500 Cr in about 2.5 halves at H1 pace"}
  - {id: "A3-02", check: "F1", line: "L282; L211; L510", classification: "AMBIGUOUS", implication: "Rs 2 lakh investment eliminated on consolidation fits a new group SPV; possible new JDA vehicle (item 5, I-5)"}
  - {id: "A3-03", check: "F1", line: "L289-291; L238; L243; L541; L584; L715", classification: "FORWARD-SIGNAL", implication: "New short-term borrowing, term debt moved to subs; group current borrowings Rs 452 Cr exceed Rs 308 Cr liquidity buffer; refinancing within 12 months"}
  - {id: "A3-04", check: "F2", line: "L167; L185; L466; L484; L397-398; L411-412", classification: "AMBIGUOUS", implication: "C-S PAT gap swung +24.7 pp YoY, +76.8 pp QoQ; subsidiaries (Q1 loss 1,255, Q2 profit 1,109) now drive the consolidated print; standalone revenue share 37.4% vs 56.2% YoY"}
  - {id: "A3-05", check: "F2", line: "L660-662; L167; L687", classification: "AMBIGUOUS", implication: "PR credits growth to Address by GS while standalone revenue fell 29% YoY; entity and Ind AS 115 method for Tower B OC revenue unknown; possible one-off OC trigger"}
  - {id: "A3-06", check: "F4", line: "L394-398; L409-412", classification: "AMBIGUOUS", implication: "All 7 subs outside joint review; 5 subs = 20.9% of Q2 PAT, 44.9% revenue, 48.9% assets; subs = 63.0% revenue and 72.7% gross assets; baseline for trend"}
  - {id: "A3-07", check: "F4", line: "L397-398", classification: "NEUTRAL-FACT", implication: "OCR_UNCERTAIN (81 O) resolves to (810): H1 sub PAT (146) vs C-S gap (144), residual +2"}
  - {id: "A3-08", check: "F6", line: "L723-724; L665-666; L479; L475; L476", classification: "FORWARD-SIGNAL", implication: "H1 EBITDA margin 14.3%; FY27 17-19% needs H2 19.0-22.5% at FY26 income vs FY26 H2 18.2%; PAT 9-10% needs H2 11.9-13.6% vs H1 5.1%"}
  - {id: "A3-09", check: "F6", line: "L702-704", classification: "FORWARD-SIGNAL", implication: "Mahim 1 and 2 window now next two quarters / current FY, which includes Q4 FY27, the checklist item 4 red zone"}
  - {id: "A3-10", check: "F6", line: "L724", classification: "FORWARD-SIGNAL", implication: "PAT margin 9-10% guided; I-6 says current state is refusal; possible partial I-6 green (PAT only, no OCF) or stale Notion state"}
  - {id: "A3-11", check: "F7", line: "L663-665", classification: "AMBIGUOUS", implication: "Margin-fluctuation hedge pre-empts a back-ended year; read with A3-08"}
  - {id: "A3-12", check: "F8", line: "L182-184; L481-483; L214-215; L512-513; L276; L573", classification: "AMBIGUOUS", implication: "ETR about 18.5% vs 25.17%, shield about 670 bps (Rs 5.6 Cr H1) undisclosed; deferred tax flipped credit to charge; taxes paid exceed provision; durability and step-up risk unknown"}
  - {id: "A3-13", check: "F10", line: "L194; L197-198; L496-497; L232-234; L529-531; L269", classification: "AMBIGUOUS", implication: "Capital flat, basic = diluted despite ESOP charge; equity roll closes on PAT, dividend, SBP only, so no warrant money in H1 FY27; cross-check Notion Rs 102 Cr warrant upfront"}
  - {id: "A3-14", check: "F11", line: "L644-657; L712-715", classification: "NEUTRAL-FACT", implication: "PR reconciles: EBITDA = PBT + finance costs + D&A (incl. other income); net debt 916 computed vs 912; D/E 0.8x is gross 0.752 rounded; net D/E 0.56x"}
  - {id: "A3-15", check: "F11", line: "L717-719; L475", classification: "AMBIGUOUS", implication: "Rs 17 Cr authority interest for FSI and approvals sits below EBITDA; as project cost, Q2 margin about 13.0%, below 14% stop; bears on pending margin-stop ruling"}
  - {id: "A3-16", check: "F12", line: "L535; L541; L519-522; L646", classification: "FORWARD-SIGNAL", implication: "Net debt Rs 658 Cr to Rs 916 Cr in H1, about Rs 129 Cr per quarter vs tracker Rs 90 Cr; risk #2 first signals (>Rs 900 Cr, D/E >0.75x) on; Rs 1,000 Cr line crossed in Q3 FY27 at this pace"}
  - {id: "A3-17", check: "F12", line: "L545; L712", classification: "AMBIGUOUS", implication: "Rs 1,908 Cr other financial liabilities outside net debt, definition unstated; composition needed for pending Rs 210 Cr AIF ruling"}
  - {id: "A3-18", check: "F12", line: "L517; L546; L570; L574; L471; L638-640", classification: "FORWARD-SIGNAL", implication: "Inventory +16.8% funded by customer-advance line +47.2%; consolidated CFO -Rs 147 Cr H1, better than model; I-2 still red-side (collections Rs 1,233 Cr < land and development cost Rs 1,674.7 Cr)"}
  - {id: "A3-19", check: "F12", line: "L174; L273; L473; L570", classification: "AMBIGUOUS", implication: "About Rs 69.5 Cr non-WIP inventory moved into development at the holding in H1 FY27; possible new Thane phase (Jekegram launch tracker)"}
  - {id: "A3-20", check: "F12", line: "L227; L272; L277; L524; L285", classification: "AMBIGUOUS", implication: "Standalone CFO +Rs 142 Cr comes from a Rs 217 Cr other-current-asset release not mirrored at group; possibly intra-group, so not collections"}
  - {id: "A3-21", check: "F14", line: "L327; L620; L76-77; L768", classification: "AMBIGUOUS", implication: "No demerger or comparability note; FY26 comparatives perimeter unstated; former name Raymond Lifestyle Limited only on cover letter; PR contact at Raymond Limited"}
  - {id: "A3-22", check: "F14", line: "L312; L605; L316-317; L609-610; L656", classification: "NEUTRAL-FACT", implication: "Minor drafting slips; review wording consistent with auditor letters"}
  - {id: "A3-23", check: "F15", line: "L447; L444-450", classification: "AMBIGUOUS", implication: "Rename Chembur Realty to Ten X Realty North, date unstated; 7-sub baseline; possible new SPV (A3-02) not in Annexure 1"}
forward_signals: ["A3-03", "A3-08", "A3-09", "A3-10", "A3-16", "A3-18"]
ambiguous: ["A3-01", "A3-02", "A3-04", "A3-05", "A3-06", "A3-11", "A3-12", "A3-13", "A3-15", "A3-17", "A3-19", "A3-20", "A3-21", "A3-23"]
commitments:
  - {commitment: "FY27 EBITDA margin 17-19%", implied_date: "2027-03-31", ref: "PR L665-666, L724", status_word: "underway"}
  - {commitment: "FY27 pre-sales growth ~20%, ROCE ~20%, PAT margin 9-10%", implied_date: "2027-03-31", ref: "PR L723-724", status_word: "underway"}
  - {commitment: "Margins expected to normalize progressively", implied_date: "H2 FY27", ref: "PR L664-665", status_word: "underway"}
  - {commitment: "Mahim 1 (1,800 Cr) and Mahim 2 (2,300 Cr) JDA launches", implied_date: "Q3-Q4 FY27, by 2027-03-31", ref: "PR L702-709", status_word: "initiated"}
  - {commitment: "Operational growth will be accelerated by MMR launch pipeline >4,100 Cr GDV", implied_date: "H2 FY27", ref: "PR L666-668, L733", status_word: "initiated"}
  - {commitment: "Fully funded for next year of construction spends (Rs 308 Cr buffer)", implied_date: "about 2027-09", ref: "PR L715", status_word: "underway"}
  - {commitment: "Debt/equity ceiling 1.0x", implied_date: "standing", ref: "PR L646, L714", status_word: "underway"}
  - {commitment: "OC received Address by GS Season 1 Tower B, 270 units (RERA date Mar-28)", implied_date: "Q2 FY27", ref: "PR L687-689, L732", status_word: "completed"}
  - {commitment: "Final dividend Rs 2/share FY26 paid", implied_date: "2026-07-14", ref: "Note 4 L324-325, L617-618", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "The headline beat (EBITDA +14%, margin 15.2%) rests on two things. First, Q2 subsidiary revenue jumped 63% QoQ while standalone revenue fell 29% YoY, so the print depends on lumpy recognition inside JDA SPVs that sit wholly outside joint-auditor review. Second, Rs 17 Cr of interest to authorities for FSI is excluded from EBITDA; counted as cost, the Q2 margin is about 13.0%, under the 14% stop. This matters most for the pending margin-stop ruling. Net debt rose about Rs 129 Cr per quarter, faster than the tracker's Rs 90 Cr. Gross D/E 0.752x and net debt above Rs 900 Cr now meet the risk #2 first signals. Holding-level lending to subsidiaries continues under a new ICD caption, so loans-to-subs reads Rs 1,192 Cr, not a pause. Standalone CFO is positive only through a Rs 217 Cr other-current-asset release that the group does not mirror. Treat it as unproven collections. Guidance needs an H2 EBITDA margin of 19-22.5% against last year's 18.2% H2. The Mahim window now reaches Q4 FY27. The (810) OCR value is confirmed by reconciliation."
```
