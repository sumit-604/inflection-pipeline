# A3 FORENSIC NOTES, results, Tinna Rubber and Infrastructure Limited (TINNARUBR) Q2 FY27

Stage: A3-forensics | Model: claude-opus-5-5 | Date: 2026-10-23
Source document (not opened by A3): Tinna_Q2FY27_Results_Reg33_2026-10-22.pdf
Inputs read: A1 structured extraction (R001-R927, 952 lines, all read), A1 fulltext (lines 1-1429, all read), A2 ledger (367 lines, all read).
Prior-quarter fulltext: NONE (first run for this ticker). Every quarter-over-quarter text diff (F5 EoM, F15 entity list, F4 Other Matter trend) is UNTESTABLE. It is not a clean pass.
Notion checklist: NONE. PRE-THESIS READ. No Spear line, no companies/TINNARUBR.md.
Unit: Rs lakhs unless stated. "[derived]" marks an A3 computation from cited cells. Values of record are the structured-file cells (page-image reads); line numbers cite the fulltext.

## 0. LEDGER RECONCILIATION

| Item | Count | Read | Status |
|---|---|---|---|
| Structured IDs in ledger | 927 | 927 | 100% |
| Notes (SA 1-5, CO 1-5) | 10 | 10 | read at lines 580-617, 622-658 (SA), 1198-1236, 1241-1278 (CO) |
| Statement line items | 226 groups / 692 cells | all | read against OCR blocks lines 230-292, 376-447, 517-578, 836-906, 982-1055, 1130-1196 |
| ZERO_STANDING cells | 81 | 81 | see F1 table |
| Agenda items | 1 | 1 | lines 33-48 |
| Auditor paras | 12 | 12 | lines 683-755 (SA), 1299-1389 (CO); OCR page 13 duplicate at 1390-1429 compared, identical in substance |
| Entities | 57 | 57 | - |
| FORWARD / DATE / QUALIFIER | 10 / 45 / 70 | all | - |

Arithmetic re-tested by A3 on key rows (all foot): CO Q2FY27 total expenses 6,449.83+1,525.45-756.66+1,964.43+263.65+427.80+3,531.23 = 13,405.73 (R365); SA Q1FY27 total expenses = 12,445.96 (R073); CO PBT after associate per column (R425-R430); SA and CO net worth (R217, R600); SA DTL movement 820.94 to 1,026.83 = H1 deferred tax 205.89 (R093, R227-R228); CO investment in associate and JV 1,388.97 to 1,422.01 = +33.04 = H1 share of profit 33.04 (R566-R567, R422).

A1 nit (not material): R116 (SA Q2FY26 TCI 1,233.80) carries no OCR_CONFLICT flag, but OCR line 271 reads "1,253.80". The value of record is correct: PAT 1,233.80 (R110) plus nil OCI, and embedded line 211 reads "1,233.80".

### A2 flags resolved

| A2 flag | Resolution | Where |
|---|---|---|
| Chile SpA in Note 4 (R773, R791), absent from auditor entity list (R797-R801) | FINDING A3-18 (F15); forward content in A3-11 (F6) | F15, F6 |
| R822 embedded-layer date 21-Oct on SA balance sheet | RESOLVED, no finding. The page image and OCR read "Date: October 22, 2026" (line 436), the same as every other page. The 21-Oct reading (line 375) is a fault in the filer's scan text layer, not a second signing date. | - |
| R926 Other Matter, 2 subs + 1 JV unreviewed | FINDING A3-07 (F4) | F4 |
| R927 consolidated report page 3 of 3 absent | FINDING A3-08 (F14) | F14 |
| EoM on Panipat HSIIDC land | FINDING A3-09 (F5), A3-10 (F7) | F5, F7 |
| R771 'Bitumen' vs R789 'Modified Bitumen' | FINDING A3-17 (F14) | F14 |
| R906 CO ROU OCR digit conflict | RESOLVED, extraction artefact. 1,003.21 foots the filed non-current total 38,026.15 (R590). | - |
| R866 OCI dashes in period columns | F1 table, A3-02 | F1 |
| R869 stray dash in SA H1FY26 basic EPS cell | Printed on the page (embedded line 218 and OCR line 276 both show "- 13.41"). Folded into A3-17. | F14 |

## 1. STANDALONE vs CONSOLIDATED DECOMPOSITION (first-class metric)

EBITDA = PBT before associate + finance cost + D&A - other income [derived].

| Metric | Q2FY27 | Q1FY27 | Q2FY26 | H1FY27 | H1FY26 | FY26 |
|---|---|---|---|---|---|---|
| SA revenue (R012-R017) | 14,956.64 | 15,085.10 | 11,685.68 | 30,041.74 | 24,416.12 | 53,323.41 |
| CO revenue (R347-R352) | 15,659.32 | 15,618.12 | 11,951.88 | 31,277.44 | 24,979.21 | 54,580.74 |
| Revenue gap C-S | 702.68 | 533.02 | 266.20 | 1,235.70 | 563.09 | 1,257.33 |
| Gap % of SA revenue | 4.70% | 3.53% | 2.28% | 4.11% | 2.31% | 2.36% |
| SA EBITDA [derived] | 2,805.91 | 3,314.36 | 2,161.86 | 6,120.27 | 4,146.63 | 9,176.56 |
| CO EBITDA [derived] | 2,945.04 | 3,390.37 | 2,156.09 | 6,335.41 | 4,234.86 | 9,352.06 |
| EBITDA gap C-S | 139.13 | 76.01 | (5.77) | 215.14 | 88.23 | 175.50 |
| SA EBITDA margin | 18.76% | 21.97% | 18.50% | 20.37% | 16.98% | 17.21% |
| CO EBITDA margin | 18.81% | 21.71% | 18.04% | 20.26% | 16.95% | 17.13% |
| D&A gap (R401-R406 less R060-R065) | 41.34 | 43.45 | 40.83 | 84.79 | 84.10 | 171.65 |
| Finance cost gap | 1.45 | 1.67 | 2.31 | 3.12 | 4.77 | 8.78 |
| PBT pre-associate gap (R413-R418 less R078-R083) | 96.34 | 30.89 | (48.28) | 127.23 | (0.01) | 4.67 |
| Associate + JV share (R419-R424) | 15.64 | 17.40 | (12.47) | 33.04 | 24.53 | (33.66) |
| Tax gap (R449-R454 less R102-R107) | 14.12 | 2.87 | (3.63) | 16.99 | 5.81 | 9.82 |
| SA PAT (R108-R113) | 1,606.07 | 2,011.22 | 1,233.80 | 3,617.29 | 2,332.06 | 5,323.54 |
| CO PAT (R491-R496) | 1,703.93 | 2,056.64 | 1,176.68 | 3,760.57 | 2,350.77 | 5,284.73 |
| PAT gap C-S | 97.86 | 45.42 | (57.12) | 143.28 | 18.71 | (38.81) |
| PAT gap % of SA PAT | +6.09% | +2.26% | -4.63% | +3.96% | +0.80% | -0.73% |

PAT gap decomposition (subsidiary PAT from the auditor Other Matter, line 1366-1367; Q1 = H1 less Q2) [derived]:

| Component | Q2FY27 | Q1FY27 (implied) | H1FY27 |
|---|---|---|---|
| Subsidiary PAT, 2 subs, unreviewed (R733, R734) | 93.35 | 22.56 | 115.91 |
| Associate + JV share, P&L line (R419, R420, R422) | 15.64 | 17.40 | 33.04 |
| of which JV (Mbodla) share, unreviewed (R738, R739) | (24.98) | (47.22) | (72.20) |
| of which associate (T.P. Buildtech), implied | 40.62 | 64.62 | 105.24 |
| Eliminations and consolidation adjustments (residual) | (11.13) | 5.46 | (5.67) |
| PAT gap C-S | 97.86 | 45.42 | 143.28 |

Revenue elimination [derived]: subsidiary revenue Q2 1,123.67 (R732) less revenue gap 702.68 = 420.99 eliminated (37.5% of subsidiary revenue); H1 1,995.11 (R745) less 1,235.70 = 759.41 (38.1%).
Trend: PAT gap moved -4.63% (Q2FY26) to +2.26% (Q1FY27) to +6.09% (Q2FY27). YoY swing +10.72 pp (above the 5 pp trigger). QoQ +3.83 pp. H1 swing +3.16 pp.
Q2FY26 subsidiary book (ex-associate) was (44.65); Q2FY27 it is +82.22. Swing +126.87 [derived].

## 2. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R191, R192, R570, R571, R300 | 394, 553, 1001 | "iv) Loans 95.27 *" | AMBIGUOUS | A new non-current loan of 95.27 appears from nil. CF "Loan given & received back (89.41)" (line 553). It survives consolidation at 95.27 (line 1001), so the borrower is outside the subsidiary set: the associate, the JV, employees or a third party. Ask counterparty, related-party status, rate and tenor. |
| A3-02 | F1, F9 | R120-R142, R461-R477, R137, R472 | 266-267 | "(b) Change in fair value of equity instrument to other (220.51)" | NEUTRAL-FACT | Interim columns carry no actuarial or FVOCI marks. Both are booked only at year end. FY26 FVOCI loss 220.51 equals 10.9% of the 31-Mar-2026 investments of 2,014.46 (R190) [derived]. The FY27 year-end mark on 2,016.46 (R189) is unbooked, direction unknown. |
| A3-04 | F2 | R108, R110, R491, R493, R733 | 263, 884 | "Owners of Parent Company 1,703.93 2,056.64 1,176.68" | FORWARD-SIGNAL | PAT gap moved from -4.63% to +6.09% of SA PAT YoY (+10.72 pp). The Saudi and Oman subsidiaries swung from a drag of about (44.65) to +82.22 [derived]. Revenue gap widened 2.28% to 4.70%. The overseas book now adds profit, but every rupee of it is unreviewed (A3-07). |
| A3-05 | F2 | R036-R041, R377-R382 | 249, 853 | "(b) Purchase of stock in trade 1,292.46 937.15 1,632.04 2,229.61 3,638.52 5,924.17" vs "b) Purchase of stock in trade 1525,45 1126,58 1363.09 2652.03 3086,04 5,343.27" | AMBIGUOUS | Intra-group trade changed direction. In FY26 CO traded purchases sat below SA (Q2FY26 -268.95, H1FY26 -552.48, FY26 -580.90), so the parent bought from its subsidiaries. In FY27 CO sits above SA (Q1 +189.43, Q2 +232.99, H1 +422.42), and about 421 of Q2 subsidiary revenue is eliminated. Parent now sells to the subsidiaries. The subsidiary profit jump may be transfer-price driven, not third-party demand. Ask for intra-group sales and pricing basis. |
| A3-06 | F2 | R294, R295, R296, R297, R282, R283, R681, R682, R683, R684, R671, R672 | 549, 1155, 1162 | "(Increase)/decrease in other assets 797,43 (2,232.37)" | AMBIGUOUS | The H1FY26 comparative cash flow classifies differently in CO and SA. CO CFO (270.91) vs SA 2,068.30. CO capex (2,904.01) vs SA (5,320.33). CO other assets (2,232.37) vs SA +292.33. CFO plus capex nearly agrees (SA -3,252.03, CO -3,174.92) [derived], so about 2,416 of capital spend sits in CO operating "other assets". H1FY27 columns agree. The CO YoY CFO swing, (270.91) to 6,660.01, is distorted. Use the SA swing, 2,068.30 to 6,822.38. |
| A3-07 | F4 | R926, R730-R742 | 1365-1376 | "has not been reviewed by us or other auditors" | AMBIGUOUS | 100% of consolidated subsidiaries (2 of 2) and the JV are management-certified. Q2 gross unreviewed exposure 93.35 + 24.98 = 118.33, 6.94% of CO PAT (below the 10% trigger). Q1 implied 69.78, 3.39%. Subsidiary PAT rose 22.56 to 93.35 QoQ (+314%) [derived]. Subsidiary total assets 3,195.77 = 5.71% of CO total assets. "Not material" rests on management's word: "According to the information and explanations given to us by the management" (line 1375). YoY trend untestable, no prior Other Matter. |
| A3-08 | F14 | R927, R744 | 1389 | "Page 2 of 3" | AMBIGUOUS | Page 3 of 3 of the consolidated review report is not in the filed PDF. The signature and UDIN sit on page 2 (line 1387), so page 3 is either blank or an annexure. Its content is unknown. Pull the full report from the BSE/NSE filing before relying on the Other Matter scope. |
| A3-09 | F5 | R884-R888, R893, R925, R341, R729 | 645, 653-654 | "filed a curative petition before the Hon'ble Supreme Court of India which was dismissed during the quarter" | FORWARD-SIGNAL | The last judicial remedy on the Panipat land closed in Q2FY27. SLP already dismissed (line 646-647). Relocation is now the operative path. HSIIDC demand 373.27 (line 645) = 23.2% of Q2 SA PAT and 7.0% of FY26 SA PAT [derived]. Paid, provided or contingent: NOT FOUND. Compensation sanctioned but "till date not claimed" (line 650). Representation of 15 May 2025 open 17 months, outcome not stated. Panipat share of capacity and plant carrying value: NOT FOUND. Prior-quarter EoM diff untestable. |
| A3-10 | F7 | R806, R888, R893 | 655-658, 739 | "evaluating various alternative for relocating the plant ... not expected to have any material impact on the Company's operation" | AMBIGUOUS | The note says relocation is under evaluation and also says no material impact on operations. Both cannot hold without a plan, a cost and a timeline. The auditor EoM narrows the claim to "will not have any material financial impact" (line 739) and drops "operation". Hedge sits in a filed note, so it is legal cover ahead of a relocation decision. |
| A3-11 | F6 | R803-R805, R808-R810, R337, R724 | 636-639, 1215 | "Capital infusion is under process" | FORWARD-SIGNAL | Tinna Rubber Chile SpA, authorised CLP 500,000,000. INR equivalent NOT FOUND. Scope adds "plastic waste and scrap, battery waste and scrap" (line 638) beyond tyre recycling: a new waste vertical. No date and no infusion amount given. Watch for the infusion in the Q3 standalone "Investment in subsidiary" line (R302). |
| A3-12 | F8 | R100, R101, R447, R448 | 261, 867 | "c) Tax.pertain to earlier years - - 13.16 13.16" | NEUTRAL-FACT | 13.16 earlier-year tax in H1FY26 and FY26, 0.41% of H1FY26 SA PBT [derived]. Nil in FY27 periods. Small assessment true-up, no pattern. |
| A3-13 | F8 | R090, R091, R102, R227, R228, R173-R176 | 260, 418 | "(b) Deferred tax 167,33 38.56" | AMBIGUOUS | Q2 deferred tax is 4.3x Q1. Q2 SA ETR 27.97% vs statutory 25.17% (+280 bps). Q1 25.56%, H1 26.65% [derived]. Deferred tax is a charge in every period, so this is a DTL build with no DTA shield and no ETR step-up risk from credits. It points to a large Q2 capitalisation: SA PPE 22,281.88 to 27,128.09, CWIP 4,119.11 to 3,135.98. Q2 D&A is flat QoQ (386.46 vs 387.84), so a D&A step-up should show from Q3. Ask which assets were capitalised and when. |
| A3-14 | F10 | R159, R161, R542, R544, R165, R548 | 276, 893 | "a) Basic earning per share (Rs,) 8.91 11,16 7.01 20.08 - 13.41" vs "Basic earning per share (Ra,} 9.46 11.42 687 20.87 13.71" | AMBIGUOUS | Implied weighted shares differ between SA and CO for the same parent. Q2FY26: SA 176.0 lakh vs CO 171.3 lakh. H1FY26: SA 173.9 vs CO 171.5 [derived]. FY26 (178.05 vs 178.06) and FY27 periods (about 180.1-180.2) agree. Candidates: ESOP trust shares treated as treasury shares in CO only during FY26, or an EPS error in the comparative. Paid-up capital is 1,801.58 in every column. The basic-diluted spread holds at about 0.1% (SA H1FY27 20.08 vs 20.06), no new dilutive instrument. |
| A3-15 | F14 | R419-R424, R659, R738-R741, R485-R490, R566, R567 | 862, 1148, 1370-1371, 879 | "Share of profit of an associates (net of tax) 15,64" | AMBIGUOUS | The P&L label names only the associate. The CF line reads "Share of profit/(loss) of an associate and joint venture" (line 1148), and the auditor confirms a JV loss of (24.98) in Q2. So the JV loss is netted inside the associate line, and the implied associate profit is 40.62 Q2 and 105.24 H1 [derived]. The auditor also cites a JV "other comprehensive loss of Rs. (24.98) lakhs" (line 1371), yet the CO "Share of associates in other comprehensive income" line is nil in all columns (R485-R490). The carrying value moves by exactly 33.04, so the auditor wording likely means total comprehensive loss. The South Africa JV loses money every quarter in H1. |
| A3-16 | F14 | R302, R303, R689, R690 | 554, 1167 | "Investment in subsidiary (271.11) (181.47)" vs "Investment in associate and joint venture - (181.47)" | AMBIGUOUS | The same H1FY26 outflow of 181.47 is labelled a subsidiary investment in SA and an associate/JV investment in CO. A subsidiary investment would be eliminated in CO; it was not. One label is wrong. It matters for which entity received FY26 capital. |
| A3-17 | F14 | R882, R914, R771, R789, R861, R872, R869 | 632, 1251, 151, 299, 663, 276 | "manufacturing and trading of Crumb Rubber, Crumb Rubber Modifier, Bitumen" vs "manufacturing Crumb Rubber, Crumb Rubber Modifier, Modified Bitumen" | NEUTRAL-FACT | SA Note 3 says "manufacturing and trading" and "Bitumen". CO Note 3 drops "trading" and says "Modified Bitumen". Also: titles printed "STANDLONE" (line 151) and "LIABILTIES" (line 299), SA notes "Place: Delhi" (line 663) where every other page says New Delhi, stray dash "- 13.41" (line 276). Each is immaterial. Together with A3-08, A3-14, A3-15 and A3-16 they are a governance data point on filing care. |
| A3-18 | F15 | R773, R791, R797-R801, R730 | 635, 1335-1341 | "The Company incorporated Tinna Rubber Chile SpA a wholly owned subsidiary" | AMBIGUOUS | Note 4 names a wholly owned subsidiary that the auditor's entity list omits. The Other Matter "2 subsidiaries" (line 1365) are Saudi Arabia and Oman, so Chile is not consolidated. Likely reason: no capital infused yet (line 639). Incorporation date: NOT FOUND. Prior-quarter entity list unavailable, so additions and deletions are untestable. Ask the incorporation date and the consolidation treatment. |

Numbering note: A3-03 was merged into the F1 zero-standing table (equity issue line) and carries no separate finding. IDs are not renumbered so that later stages can cite them as fixed.

## 3. CHECKLIST SCORECARD

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing lines | FINDING | 81 cells explained (table below). A3-01: new non-current loan from nil. A3-02: interim OCI is never marked. |
| F2 Standalone vs consolidated | FINDING | PAT gap YoY swing +10.72 pp of SA PAT (A3-04); intra-group trade flipped direction (A3-05); H1FY26 CO cash flow classification differs (A3-06). |
| F3 Shell entities | PASS | Subsidiaries run operations. Q2 CO less SA: employee +197.00, other expenses +243.55, D&A +41.34, materials +17.62. No shell is consolidated. Chile SpA is a pre-capital vehicle outside the consolidation (F15). No going-concern EoM. |
| F4 Unaudited contribution | FINDING | Q2 gross unreviewed 118.33 = 6.94% of CO PAT, below 10%. QoQ jump from 3.39% and 100% of subsidiaries unreviewed (A3-07). YoY untestable. |
| F5 Going concern / EoM scope | FINDING | No going-concern paragraph. EoM on Panipat land reports a new in-quarter event: curative petition dismissed (A3-09). Prior EoM text unavailable, verbatim diff untestable. |
| F6 Forward-commitment phrases | FINDING | Hits: "under process" (Chile infusion), "in the process of evaluating" (relocation), "expects to receive compensation", "not expected to have". Register below. "commenced" (line 48) is meeting time only. |
| F7 Hedge phrases | FINDING | "evaluating" in Note 5 (A3-10). Auditor materiality rests on "information and explanations given to us by the management" (line 1375). No "subject to", "no assurance", "exploring", "in discussions", "endeavour" hits. |
| F8 Tax forensics | FINDING | Earlier-year tax 13.16 in H1FY26/FY26 (A3-12). Q2 SA ETR 27.97% on a 4.3x deferred charge (A3-13). Deferred tax is a charge every period, so no DTA shield. CO ETR Q2 27.24%, H1 26.14%. |
| F9 OCI forensics | PASS | Interim OCI is FCTR only (CO Q2 18.58, Q1 16.90, H1 35.48). No quarter exceeds the FY26 total (CO FCTR 156.42; SA OCI (209.62)). Actuarial (27.58) booked at year end only; verify assumptions at the FY27 AR. |
| F10 Share count and dilution | FINDING | Paid-up 1,801.58 every column; no equity issued in H1FY27 (R312). Basic-diluted spread steady at about 0.1%. SA vs CO EPS denominators disagree for Q2FY26 and H1FY26 (A3-14). |
| F11 Net worth tie-out | PASS | SA 1,801.58 + 30,565.80 = 32,367.38. CO 1,801.58 + 31,483.76 = 33,285.34. SA roll-forward (27,509.68 + TCI 3,617.29 - dividend 585.52 + ESOP 24.34) misses by 0.01. CO roll-forward misses by 10.87 (0.03%). No third-party figure in context. |
| F12 Segment forensics | PASS | Single reportable segment (Note 3, lines 632, 1251); no segment assets or liabilities disclosed. Capex proxy: SA PPE + CWIP 26,400.99 to 30,264.07, +3,863.08 in H1 [derived]; SA capex cash 4,473.96 (R296). |
| F13 Board outcome | PASS | One agenda item: results approval (lines 41-44). No AR, AGM, record date, dividend, director, auditor, ESOP or capital-raise item. Meeting 11:30 AM to 02:05 PM. |
| F14 Note drafting inconsistencies | FINDING | A3-08 missing report page; A3-15 associate label omits JV and JV OCI mismatch; A3-16 subsidiary vs associate label; A3-17 segment wording and typos. Note vs letter: both say limited review (lines 43, 707-716); no audit/review mismatch. |
| F15 Entity list diffs | FINDING | Chile SpA in Note 4, absent from the consolidated entity list (A3-18). Prior list unavailable; other diffs untestable. |
| F16 Presentation: dropped disclosures | N.A. | Results doctype. |
| F17 Concall: silence audit | N.A. | Results doctype. Also a pre-thesis read: no Notion checklist exists. |

### F1 zero-standing table (81 cells)

| Line (cells) | IDs | Why the line exists / transaction class it anticipates | Read |
|---|---|---|---|
| Tax of earlier years, FY27 periods (SA 4, CO 4) | R096-R099, R443-R446 | Assessment true-ups. Non-zero 13.16 in H1FY26/FY26. | A3-12 |
| OCI total and items a/b/c, interim columns (SA 20, CO 15) | R120-R124, R126-R130, R132-R136, R138-R142, R461-R465, R467-R471, R473-R477 | Actuarial remeasurement and FVOCI equity marks. Booked only at year end. | A3-02 |
| Share of associates OCI (CO 6) | R485-R490 | Equity-accounted OCI. Nil in all columns, yet the auditor cites a JV OCI loss. | A3-15 |
| NCI profit and NCI TCI (CO 12) | R503-R514 | Non-wholly-owned subsidiaries. All current subs are wholly owned; a partnered entity (for example a Chile partner) would populate it. | Template |
| Other equity, period columns (SA 5, CO 5) | R151-R155, R534-R538 | Disclosed only for the audited year column. | Template |
| Non-current loans, 31-Mar-2026 (SA 1, CO 1) | R192, R571 | Long-term lending. Now 95.27. | A3-01 |
| Unrealised FX, H1FY26 (SA 1) | R271 | FX exposure. 7.57 in H1FY27 (R270). | Neutral |
| Proceeds from sale of investment, H1FY27 (SA 1, CO 1) | R304, R691 | Divestment. 500.75 SA / 464.63 CO in H1FY26. | Neutral |
| Equity issue, H1FY27 (SA 1, CO 1) | R312, R699 | Capital raise. 7,620.30 in H1FY26. H1FY27 capex runs on CFO and debt (LT proceeds 1,503.22, R314). | Neutral (merged A3-03) |
| Lease principal and interest, H1FY26 (SA 2) | R321, R323 | Lease payments. Began after H1FY26; SA ROU 768.54 to 953.61. | Neutral |
| Investment in associate/JV, H1FY27 (CO 1) | R689 | New equity into associate/JV. Nil this half. | Neutral |

## 4. COMMITMENT REGISTER (F6)

| # | Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|---|
| C1 | Capital infusion into Tinna Rubber Chile SpA | none stated | SA Note 4, lines 638-639; CO Note 4, line 1215 (R805, R810) | underway ("under process") |
| C2 | Relocation of the Panipat plant | none stated | SA Note 5, line 655; CO Note 5, line 1233 (R806, R811) | initiated ("in the process of evaluating") |
| C3 | Receipt of State-sanctioned compensation | none stated; not yet claimed | SA Note 5, lines 650, 655-656; CO lines 1229-1230, 1233-1234 (R807, R812, R886, R918) | not started ("has till date not claimed"; "expects to receive") |
| C4 | Representation to Principal Secretary, Industries, Haryana, for land release | dated 15 May 2025; open 17 months, no outcome stated | SA Note 5, lines 647-649; CO lines 1226-1228 (R833, R851) | initiated |
| C5 | Curative petition, Supreme Court | dismissed during Q2FY27 | SA Note 5, lines 653-654; CO lines 1231-1232 (R887, R919) | completed (adverse) |
| C6 | HSIIDC allotment demand Rs 373.27 lakhs | none stated | SA Note 5, line 645; CO line 1223 (R341, R729) | status NOT FOUND (paid / provided / contested) |
| C7 | Management view: no material impact on operations and financial results | assertion, undated | SA Note 5, lines 656-658; CO lines 1235-1236 (R888, R920) | assertion, test against C2 |

## 5. QUESTIONS FOR A4 (from FORWARD-SIGNAL and AMBIGUOUS findings)

1. A3-09, A3-10: What share of production and revenue comes from Panipat? What is the relocation cost, site and timeline? Is the Rs 373.27 lakh demand paid, provided or contingent? What is the compensation amount, and why is it still unclaimed?
2. A3-04, A3-05, A3-07: What were intra-group sales from the parent to the Saudi and Oman subsidiaries in Q2? On what pricing basis? Why did Q2 subsidiary PAT rise from 22.56 to 93.35? Will the subsidiaries get a review or audit before FY27 year end?
3. A3-08: What does page 3 of the consolidated review report contain?
4. A3-11, A3-18: When was Chile SpA incorporated? How much capital goes in, and when? Why is it outside the consolidation? Is battery and plastic waste a planned new line?
5. A3-06: Why does the H1FY26 consolidated cash flow carry about 2,416 of capital spend in operating "other assets"?
6. A3-13: Which assets were capitalised in Q2? What D&A run-rate follows from Q3?
7. A3-14: Why do Q2FY26 and H1FY26 EPS imply different share counts in standalone and consolidated? Is there an ESOP trust?
8. A3-15, A3-16: What are the separate associate and JV shares? What is the plan for the loss-making Mbodla JV? Which entity received the H1FY26 181.47?
9. A3-01: Who received the 95.27 non-current loan? Is it a related party?

## 6. UNSCORED OBSERVATIONS (cited, for A4 context; not check findings)

- Dividend paid H1FY27 585.52 (R324, line 566) = Rs 3.25 per share on 180.158 lakh shares [derived], vs 692.70 in H1FY26 (R325) on a smaller share base. Payout per share fell YoY while FY26 PAT grew. Possible cash conservation for capex or relocation.
- SA EBITDA margin fell from 21.97% (Q1) to 18.76% (Q2), -321 bps QoQ [derived]. Gross material cost stayed near 47.4-47.8% of revenue. The drop came from employee cost +254.39 QoQ (R048 vs R049, +16.8%) and other expenses +237.54 (R066 vs R067).
- SA H1FY27 CFO 6,822.38 (R294) = 189% of PAT. It is helped by a receivables release of 1,323.64 (R278) and other assets of 857.81 (R282). SA gross debt fell from 12,057.19 to 11,128.73 [derived from R221, R222, R233, R234].

```yaml
stage: A3-forensics
company: "TINNARUBR"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/tinnarubr-q2fy27/work/forensics_results_tinnarubr_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: PASS
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "394, 553, 1001", classification: "AMBIGUOUS", implication: "New non-current loan 95.27 from nil; survives consolidation, so borrower is outside the subsidiary set; counterparty and related-party status unknown"}
  - {id: "A3-02", check: "F1", line: "266-267", classification: "NEUTRAL-FACT", implication: "Interim OCI never marked; FY26 FVOCI loss 220.51 (10.9% of 2,014.46); FY27 year-end mark on 2,016.46 unbooked"}
  - {id: "A3-04", check: "F2", line: "263, 884", classification: "FORWARD-SIGNAL", implication: "CO-SA PAT gap -4.63% to +6.09% of SA PAT YoY (+10.72 pp); overseas subs swung from (44.65) to +82.22; all unreviewed"}
  - {id: "A3-05", check: "F2", line: "249, 853", classification: "AMBIGUOUS", implication: "Intra-group trade flipped: FY26 parent bought from subs, FY27 parent sells to subs (about 421 eliminated in Q2); sub profit jump may be transfer-price driven"}
  - {id: "A3-06", check: "F2", line: "549, 1155, 1162", classification: "AMBIGUOUS", implication: "H1FY26 CO cash flow carries about 2,416 of capex in operating other assets; CO CFO YoY swing distorted; use SA 2,068.30 to 6,822.38"}
  - {id: "A3-07", check: "F4", line: "1365-1376", classification: "AMBIGUOUS", implication: "100% of subs plus JV unreviewed; Q2 gross 118.33 = 6.94% of CO PAT, up from 3.39% QoQ; sub PAT 22.56 to 93.35; materiality per management"}
  - {id: "A3-08", check: "F14", line: "1389", classification: "AMBIGUOUS", implication: "Consolidated review report page 3 of 3 missing from filing; content unknown"}
  - {id: "A3-09", check: "F5", line: "645, 653-654", classification: "FORWARD-SIGNAL", implication: "Curative petition dismissed in Q2FY27, last judicial remedy closed; Panipat relocation now operative; demand 373.27 = 23.2% of Q2 SA PAT, provision status NOT FOUND"}
  - {id: "A3-10", check: "F7", line: "655-658, 739", classification: "AMBIGUOUS", implication: "Relocation under evaluation yet no material operational impact claimed; auditor narrows to financial impact only"}
  - {id: "A3-11", check: "F6", line: "636-639, 1215", classification: "FORWARD-SIGNAL", implication: "Chile SpA capital infusion under process; scope adds plastic and battery waste recycling; amount and date NOT FOUND"}
  - {id: "A3-12", check: "F8", line: "261, 867", classification: "NEUTRAL-FACT", implication: "Earlier-year tax 13.16 in H1FY26/FY26; nil in FY27"}
  - {id: "A3-13", check: "F8", line: "260, 418", classification: "AMBIGUOUS", implication: "Q2 deferred tax 4.3x Q1, SA ETR 27.97%; DTL build from Q2 capitalisation; D&A step-up expected from Q3"}
  - {id: "A3-14", check: "F10", line: "276, 893", classification: "AMBIGUOUS", implication: "SA vs CO EPS imply different share counts for Q2FY26 (176.0 vs 171.3 lakh) and H1FY26; FY26 and FY27 agree"}
  - {id: "A3-15", check: "F14", line: "862, 1148, 1370-1371, 879", classification: "AMBIGUOUS", implication: "Associate line nets the loss-making JV; implied associate profit 40.62 Q2, 105.24 H1; auditor JV OCI loss vs nil OCI line"}
  - {id: "A3-16", check: "F14", line: "554, 1167", classification: "AMBIGUOUS", implication: "Same H1FY26 181.47 labelled subsidiary investment in SA and associate/JV investment in CO"}
  - {id: "A3-17", check: "F14", line: "632, 1251, 151, 299, 663, 276", classification: "NEUTRAL-FACT", implication: "Segment wording differs SA vs CO; title typos; place mismatch; cumulative filing-care data point"}
  - {id: "A3-18", check: "F15", line: "635, 1335-1341", classification: "AMBIGUOUS", implication: "Chile SpA named as wholly owned subsidiary but absent from consolidated entity list; incorporation date NOT FOUND; prior list untestable"}
forward_signals: ["A3-04", "A3-09", "A3-11"]
ambiguous: ["A3-01", "A3-05", "A3-06", "A3-07", "A3-08", "A3-10", "A3-13", "A3-14", "A3-15", "A3-16", "A3-18"]
commitments:
  - {commitment: "Capital infusion into Tinna Rubber Chile SpA", implied_date: "none stated", ref: "SA Note 4 lines 638-639; CO Note 4 line 1215", status_word: "underway"}
  - {commitment: "Relocation of Panipat plant", implied_date: "none stated", ref: "SA Note 5 line 655; CO line 1233", status_word: "initiated"}
  - {commitment: "Receipt of sanctioned compensation", implied_date: "none stated; not yet claimed", ref: "SA Note 5 lines 650, 655-656; CO lines 1229-1234", status_word: "not started"}
  - {commitment: "Representation for land release dated 15 May 2025", implied_date: "open 17 months, no outcome stated", ref: "SA Note 5 lines 647-649; CO lines 1226-1228", status_word: "initiated"}
  - {commitment: "Curative petition, Supreme Court", implied_date: "dismissed during Q2FY27", ref: "SA Note 5 lines 653-654; CO lines 1231-1232", status_word: "completed (adverse)"}
  - {commitment: "HSIIDC allotment demand Rs 373.27 lakhs", implied_date: "none stated", ref: "SA Note 5 line 645; CO line 1223", status_word: "status NOT FOUND"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read, first run. Every QoQ text diff (EoM, entity list, Other Matter) is untestable, not clean. Three items matter. First, the Panipat land route closed this quarter. The curative petition was dismissed, so relocation is the operative path. Note 5 still claims no material impact on operations and gives no plant share, cost, timeline, or provision status for the Rs 373.27 lakh demand. Lean bear until management sizes it. Second, the consolidated premium over standalone is new and unreviewed. The PAT gap moved from -4.63% to +6.09% of standalone PAT YoY, 100% of subsidiary numbers are management-certified, and page 3 of the review report is missing. Subsidiary PAT quadrupled QoQ while intra-group trade changed direction, so part of the gain may be transfer pricing, not third-party demand. Third, the H1FY26 consolidated cash flow parks about Rs 2,416 lakh of capex in operating other assets. Use standalone CFO for the YoY read. The Mbodla JV loses money inside a line labelled associate only. Chile SpA widens scope to battery and plastic waste and is not yet consolidated."
token_estimate: "about 165k tokens (about 150k input incl. full structured file and fulltext, about 15k output)"
```
