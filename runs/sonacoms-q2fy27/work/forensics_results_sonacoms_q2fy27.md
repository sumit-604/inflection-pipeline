# FORENSICS: results | SONACOMS | q2fy27 (A3 forensic notes, doctype: results)

Document: Board Outcome (Reg 33) dated 26-Oct-2026 with standalone (SA) and consolidated (C) unaudited results for Q2/H1 FY27, two limited review reports (Walker Chandiok & Co LLP) and Annexure 1 entity list. Units Rs million (x0.1 to Rs Cr). Line numbers (l.) refer to A1 fulltext `extracted/sonacoms-results-q2fy27-fulltext.md`; R### refers to A1 structured rows.

Inputs read: A1 structured (R001-R1098, all rows), A1 fulltext (l.1-660, all lines), A2 ledger (690 lines), Notion page saved 28-Oct-2026 (properties block, Q1 FY27 Step 6B tripwires, Q1 A3 findings, 26-Oct Q2 entry). Not read: source PDF, inputs/, work/a1res page images.

Prior-quarter verbatim diff: NOT RUN. No prior SONACOMS A1 extract exists in the repo. Q1 FY27 facts used below are tagged [NOTION MEMORY] and come from the saved Notion page. They are memory to weigh, not a filed comparison.

---

## 0. LEDGER RECONCILIATION

| item | count | result |
|---|---|---|
| Structured rows (R001-R1098) read at cited fulltext line | 1098 / 1098 | 100% |
| A2 ledger rows (notes 15, line items 249, cells 771, zero-standing 47 cells / 19 lines, agenda 1, auditor paras 9, entities 17, signature blocks 5) | all | reconciled |
| NUMBER rows: value matches fulltext cell at cited line | 841 / 841 | match |
| Rows whose verbatim value is NOT present at the cited fulltext line | 34 | A1 normalisation, not a document issue (see note) |

Note on the 34 rows. R1017-R1022, R1031-R1032, R1034-R1035, R1042-R1047, R1065-R1070, R1079-R1080, R1082-R1083, R1090-R1095 record "(Unaudited)"/"(Audited)" column status tags. The fulltext column headers at l.145, l.233, l.277, l.308, l.469, l.566, l.608, l.641 carry period labels only, without status tags. R1024 and R1072 record the caption "not annualised for quarters"; l.173 and l.504 do not carry it. The balance-sheet headers (l.184, l.515) do carry the tags. No finding below depends on these 34 rows. Verifier A may want to confirm them against the page render.

A2 flags, disposition:

| A2 flag | rows | disposition |
|---|---|---|
| ZERO_STANDING 47 cells / 19 lines | Section 3 of ledger | F1-01, F1-02, F1-03 (every line explained) |
| BLANK_CELL SA Note 3 H1 FY26 total | R381-R385, l.311 | F14-03 |
| LOW_LEGIBILITY R537 (C H1 FY27 remeasurement 7.05) | l.489 | RESOLVED by cross-foot: 7.05 - 1.78 + 53.39 + 277.58 - 69.86 = 266.38 = l.494 H1 OCI total. Also Q1 (0.04) + Q2 7.08 = 7.04, within rounding. R537 = 7.05 stands. |
| SIGNATURE_BEFORE_BOARD | R938, R972 vs R005 | F14-01 |
| NAME_VARIANT "Precisions" | R882, l.437 | F14-02 |
| UNNAMED_ENTITY five foreign subs | R878, l.388 | F3-02 |
| UNNAMED_ENTITY dividend-paying WOS | R869, l.320 | F2-03 |
| UNNAMED_ENTITY slump-sale target "100% subsidiary" | R921/R927, l.318/l.651 | F1-02, F15-02 |
| ENTITY_CHANGE Novelic India | R898, R974, R1063, l.458-460 | F15-01 |
| FORWARD Note 5 DENSO | R918-R929 | F6-01, F6-02, F7-01, commitment register |

---

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-01 | F1 | R092-R097, R492-R497, R369-R385, R815-R832 | l.158, l.482, l.309-311, l.642-644 | "Exceptional items (Refer Note No. 3) \| - \| - \| 16.68" | FORWARD-SIGNAL | The exceptional line and both Note 3 rows stay in the template at nil for Q1, Q2 and H1 FY27. The transaction class that repopulates it is Note 5: slump sale of the EV motors and controllers business into a 100% subsidiary at fair value, then DENSO buys 49% at EV Rs 17,500m (l.318-319). In SA a gain on the slump sale and on the 49% share sale lands here. The "acquisition opportunities" row (FY26 108.42, l.309) is nil in Q2 although DENSO definitive agreements were signed 22-Jul-2026 (l.315). Deal costs (valuer, advisers) are not in exceptional items. They sit in other expenses or are deferred. SA other expenses rose 22.5% QoQ (2,133.55 to 2,613.15, l.155) against revenue +19.0%. |
| F1-02 | F1 | R918-R929, R1048, R1096 | l.315, l.319, l.651-652; BS l.185-223, l.516-556 | "to form two Joint Ventures" ... "DENSO will buy 49% equity stake in this subsidiary" | AMBIGUOUS | Note 5 calls the same vehicle a "Joint Venture" and "this subsidiary". The consolidated accounting turns on that word. Reading A (control kept at 51%): the 49% sale is an equity transaction under Ind AS 110. It never touches consolidated P&L or the exceptional line; only SA books a gain. Reading B (joint control): the group loses control, deconsolidates, and remeasures the retained 51% at fair value through P&L. That is a large non-cash consolidated gain. Neither balance sheet has an "assets held for sale" line. That fits Reading A, or a close that management does not judge highly probable within 12 months. Separating observation: the closing note's word for the 51% entity (subsidiary vs joint venture) and whether NCI appears for it. |
| F1-03 | F1 | R110-R115, R510-R515, R141, R541, R274, R720, R287, R333, R340, R782, R774 | l.161, l.485, l.166, l.490, l.237, l.570, l.243, l.266, l.279, l.610, l.597 | "Tax expense - Tax related to previous years \| - \| - \| - \| - \| - \| 9.13" | NEUTRAL-FACT | The other 15 zero-standing lines are template lines with one-off or period-specific use. Prior-year tax: assessment true-ups (non-zero only FY26, see F8-03). OCI tax Q1: immaterial remeasurement (0.03). Allowance for doubtful receivables: nil H1 FY27 vs 2.99 H1 FY26, no new ECL despite C receivables +345.76. Dividend income/received: nil H1 FY26, 594.63 H1 FY27 (Note 6). Deferred payment liabilities: settled in H1 FY26 (10.56), none left. C purchase of non-current investments: nil H1 FY27 vs (16,954.67) H1 FY26 (railway acquisition, Note 2). The SA counterpart is (330.51) (l.265). That is an intra-group capital injection; see F2-03. |
| F2-01 | F2 | R128-R133 vs R528-R533 | l.164, l.488 | SA "1,973.79 \| 2,201.06" vs C "2,229.87 \| 1,785.13" | NEUTRAL-FACT | SA-minus-C PAT gap as % of SA PAT: Q2 FY27 -12.97%, Q1 FY27 +18.90%, Q2 FY26 -2.54%, H1 FY27 +3.83%, H1 FY26 -2.02%, FY26 +2.66%. QoQ swing -31.9 pp (above the 5 pp trigger). Cause: Q1 SA other income 817.83 (l.148) held the Rs 594.63m WOS dividend (l.320, l.243), eliminated on consolidation. Ex-dividend Q1 gap is about -11.1%, so the underlying QoQ move is about -1.9 pp. The Q1 flag [NOTION MEMORY, R-A3-F2-01] has unwound. Consolidated stays the honest basis. |
| F2-02 | F2 | R020-R085 vs R420-R485 | l.146-156, l.470-480 | SA "Revenue from operations \| 13,770.38" vs C "15,358.40" | FORWARD-SIGNAL | YoY the consolidated premium over SA widened by 10.4 pp (-2.54% to -12.97%). Net subsidiary contribution after eliminations (C minus SA): revenue 813.08 to 1,588.02 (+95%); op EBITDA ex-forex 125.60 to 390.60 (+211%); margin 15.4% to 24.6%; share of C op EBITDA 4.4% to 11.3%. Q2 PAT bridge C minus SA = +256.08: EBITDA +390.60, forex +27.83, other income +22.48, D&A -80.62, finance -32.73, tax -71.48 (ties exactly). The subsidiary layer is now material and growing. Which entity drives it is not disclosed. If any of it moves to a 51% vehicle under Note 5, 49% leaks to NCI. |
| F2-03 | F2 | R330-R331 vs R774-R775; R246-R247 vs R692-R693; R338 vs R780; R394, R869 | l.265 vs l.597; l.213 vs l.546; l.278 vs l.609; l.320 | SA "Purchase of non-current investments \| (330.51)" vs C "\| -"; "dividend from one of its wholly owned subsidiary amounting to Rs. 594.63 million" | AMBIGUOUS | In H1 one unnamed WOS paid the parent Rs 594.63m (19-Jun-2026). The parent injected Rs 330.51m back into a subsidiary (SA non-current investments 6,037.85 to 6,369.49, l.191). Subsidiary short-term borrowings (C minus SA) rose 152.54 to 771.25; C-minus-SA net ST borrowing proceeds 578.74. At group level, debt in the subsidiaries partly funded the dividend that flattered Q1 SA PAT [INFERENCE: payer, recipient of the 330.51 and borrower are not named and may be different entities]. Question: name the payer, the investee and the borrowing subsidiary. |
| F2-04 | F2 | R582-R587, R676-R677, R419 | l.497, l.538, l.451 | "Profit attributable to: b) Non-controlling interests \| (4.17) \| (19.55) \| (23.05)" | FORWARD-SIGNAL | The only non-wholly-owned entities are the six Novelic-group companies held 54% (l.451-458). NCI share implies a post-adjustment Novelic-group result of about -9.1m Q2 FY27, -42.5m Q1 FY27, -50.1m Q2 FY26, -238.8m FY26 (my arithmetic: NCI / 0.46). Losses narrowed sharply in Q2. NCI balance ties: 1,492.43 + (21.70) = 1,470.73 (l.538, l.501). Bears on tripwire 3 (Novelic KAM impairment) [NOTION MEMORY]. One quarter only. |
| F2-05 | F2 | R026-R031, R426-R431, R294-R295, R738-R739 | l.147, l.471, l.247, l.579 | SA "Unrealised foreign exchange (gain)/loss (net) \| 181.02 \| (105.90)"; C "Unrealised foreign exchange loss/(gain) (net) \| 116.68" | AMBIGUOUS | P&L shows a net forex GAIN (SA H1 161.00, C H1 197.48). The cash flow adds back an UNREALISED forex LOSS (SA 181.02, C 116.68). H1 FY26 was the reverse (unrealised gain 105.90 SA). So H1 FY27 realised forex exceeds the P&L line [INFERENCE: if the unrealised loss sits in the forex line, realised gain is about 342 SA / 314 C; the loss may instead sit in finance cost on foreign-currency borrowings]. Feeds the pending operator forex-treatment ruling. Op EBITDA margin C Q2: 22.51% ex-forex, 23.20% incl forex (my arithmetic). |
| F2-06 | F2 | R350-R351 vs R792-R793; R062-R067 vs R462-R467 | l.284 vs l.615; l.153 vs l.477 | SA "Interest paid \| (91.52) \| (4.60)" vs C "\| (84.05) \| (1.23)" | AMBIGUOUS | Consolidated interest paid is LOWER than SA in both H1s, although C finance costs exceed SA (H1 227.94 vs 161.55) and subsidiaries added ST debt. That points to interest the parent pays to a subsidiary, eliminated on consolidation, or to subsidiary interest accrued or capitalised but not paid [INFERENCE]. Question: is there an intra-group loan from a subsidiary to the parent? |
| F3-01 | F3 | R250-R251 vs R696-R697; R380 vs R826 | l.215, l.548, l.310, l.643 | "Trade payables - dues of micro enterprises and small enterprises \| 1,451.52 \| 952.83" (identical SA and C) | FORWARD-SIGNAL | MSME payables are identical in SA and C at both dates. The Indian subsidiaries (Comstar Automotive Technologies Services, Sona Comstar eDrive, Novelic India) carry zero MSME trade dues. FY26 New Labour Codes impact was 399.49 SA vs 401.39 C, so Indian subsidiaries carry about 1.90m of it, a thin payroll. Cost lines overall differ (C materials +834.69, employee +250.93, D&A +80.62 in Q2), so the subsidiary layer is operating; no group-level shell. eDrive does not yet run its own Indian supply chain [INFERENCE]. Observable: after the Note 5 slump sale closes, SA and C MSME payables should diverge. |
| F3-02 | F3 / F4 | R406-R414, R878, R1055-R1058 | l.388-394, l.400 | "We did not review the interim financial results of five subsidiaries ... total assets of 2,007.38 million" | AMBIGUOUS | Five unnamed foreign subsidiaries: H1 revenue 389.59 on assets 2,007.38 (about 0.39x annualised), H1 loss (24.20), Q2 profit 5.55. Annexure 1 lists exactly five foreign Novelic-group entities (l.453-457) [INFERENCE: these may be the five; the auditor does not name them]. C goodwill exceeds SA goodwill by 1,936.06 (l.519 vs l.188), unchanged. If the five are Novelic, the assets reviewed by another auditor are about 2,007m against the FY26 Rs 350 Cr investment carrying-value indicator [NOTION MEMORY]. Question: name the five. |
| F6-01 | F6 | R918-R922, R924-R928, R967, R1002, R891 | l.318, l.651, l.448 | "subject to fulfilment of customary conditions, the Company will slump sell its existing EV Motors and controllers business" | FORWARD-SIGNAL | 96 days after signing (22-Jul to 26-Oct), status language is unchanged from Q1 [NOTION MEMORY: "signed 22-Jul, conditional"]. No "initiated / underway / completed" transition. "Sona Comstar eDrive Private Limited" is still in the wholly owned list at 30-Sep (l.448). No close date is given. The Oct postal-ballot RPT approval with eDrive [NOTION MEMORY, 07-Oct entry] is progress outside this filing. Like-for-like on margin and ROCE holds for H1. |
| F6-02 | F6 | R923, R929 | l.319, l.652 | "Both the JV partners will also be paid royalty as agreed in the definitive agreements from their majority owned joint ventures respectively" | AMBIGUOUS | Each partner takes a royalty from the JV it controls. Royalty rate, base and term are not disclosed. For Sona's 51% vehicle the royalty eliminates in consolidation but moves value from the 49% DENSO share to Sona. For the DENSO-majority JV it is a cost to an entity Sona holds 49% of. Net effect on Sona's margin and equity-accounted income is unknown. |
| F7-01 | F7 | R1048, R1096 | l.318, l.651 | "subject to fulfilment of customary conditions" | AMBIGUOUS | Only lexicon hit in the notes. Carried from Q1 [NOTION MEMORY, R-A3-F7-01], not newly added. No new hedge on revenue lumpiness or customer concentration. Conditions are not listed (CCI, valuer report, RPT approval). Timing and quantum of any gain stay undefined. Auditor phrases "to the extent applicable" (l.373) and "based solely on the review report of such other auditor" (l.397) are standard review language. |
| F8-01 | F8 | R098-R103, R122-R127 | l.159, l.163 | "Total tax expense \| 658.29 \| 555.15" | NEUTRAL-FACT | SA ETR: Q2 FY27 25.01%, Q1 FY27 20.14%, Q2 FY26 25.36%, H1 FY27 22.52%, H1 FY26 25.46%, FY26 24.59%. C ETR: Q2 24.66%, Q1 25.91%, Q2 FY26 25.09%, H1 25.22%, H1 FY26 25.62%, FY26 25.24% (statutory 25.17%). The Q1 SA shield (about 503 bps [NOTION MEMORY]) has unwound. Ex-dividend Q1 SA ETR is 25.68% (555.15 / 2,161.58), so the dividend bore almost no tax [INFERENCE: Sec 80M]. No step-up risk carried forward. |
| F8-02 | F8 | R116-R121, R516-R521, R242-R243, R688-R689 | l.162, l.486, l.211, l.544 | "Tax expense - Deferred tax (credit)/ charge \| 122.91 \| 119.85 \| 118.58" | NEUTRAL-FACT | Deferred tax is a persistent CHARGE, not a credit, in all 12 cells. No DTA or carry-forward shield. SA Q2 current tax is 20.34% of PBT and deferred 4.67%. DTL SA +243.89 and C +216.52 in H1, tied to P&L deferred tax (242.76 / 218.06). Cash tax runs below book tax on accelerated tax depreciation. With H1 capex halved (C 1,485.04 vs 3,075.91, l.592), DTL build slows and cash tax converges up. C current tax liabilities rose 91.07 to 352.74 (l.553), which also helps H1 CFO. |
| F8-03 | F8 | R115, R515 | l.161, l.485 | "Tax related to previous years ... \| 9.13" (SA), "8.26" (C) | NEUTRAL-FACT | Non-zero prior-year tax in FY26 only (0.11% / 0.10% of PBT). Nil in all FY27 periods. Immaterial; flagged per rule. |
| F10-01 | F10 | R170-R189, R612-R631 | l.171, l.173-174, l.502, l.504-505 | SA "Earnings per share (Basic) \| 3.17" / "(Diluted) \| 3.16"; C H1 "6.49" / "6.48" | NEUTRAL-FACT | First basic-diluted spread in the series (0.01, about 0.3%). Prior periods equal. Paid-up capital 6,218.47 (Mar) to 6,220.35 (Jun) to 6,241.28 (Sep): +20.93m in Q2 = 2,093,587 shares (+0.34%). Ties to 62,41,28,424 shares [NOTION MEMORY, 05-Oct entry]. Equity proceeds H1 1,075.99 (l.283) are ESOP cash. Options granted 16-Jun at Rs 596.35 (l.313) are in the money at the Notion price, which explains the new spread. |
| F10-02 | F10 | R388, R835, R965 | l.314, l.647 | "the NRC approved an allotment of 1,70,747 equity shares to the MD at face value" | NEUTRAL-FACT | Performance-share grant to the MD at Rs 10 face value on FY26 metrics. About 0.03% dilution; about Rs 13.4 Cr value at Rs 782 [NOTION MEMORY price; my arithmetic]. Q1 capital rise of 1.88m is consistent with this allotment [INFERENCE]. Not in the Notion share log [NOTION MEMORY]. A4 runs the thesis cross-check. |
| F12-01 | F12 | R200-R201 vs R642-R643; R194-R195 vs R636-R637 | l.190 vs l.521; l.187 vs l.518 | C "Intangible assets under development \| 3,058.11 \| 2,911.82" vs SA "61.51 \| 61.75" | FORWARD-SIGNAL | Single reportable segment (l.321, l.653), so F12 runs at entity level. Subsidiaries hold 2,996.60 of capitalised development (C minus SA), up 146.53 in H1 (+5.1%). Subsidiary CWIP is 776.26 vs 494.24 (+57%). The build is in subsidiaries with no separate revenue disclosure, funded partly by the parent's 330.51 injection (F2-03). Capitalised development in a loss-making subsidiary layer is the asset an impairment test would hit first [INFERENCE on location: Novelic radar/sensing is the likely holder]. |
| F12-02 | F12 | R246-R253, R692-R699, R214-R223, R338, R780 | l.213, l.215-216, l.546, l.548-549, l.197, l.200-201 | SA "Current financial liabilities (i) Borrowings \| 3,848.47 \| 2,190.00" | AMBIGUOUS | Liabilities rose sharply with treasury. SA ST borrowings +75.7% (C +97.2%, 2,342.54 to 4,619.72). SA trade payables 4,143.72 to 6,581.23 (+58.8%; MSME +52.3%). Over the same half SA current investments rose +3,060.03, other bank balances +1,440.64 and other current financial assets +2,624.54. The group borrowed while it built treasury. Reading A: cheap export credit (packing credit) carried against deposits, an arbitrage. Reading B: working capital funded by suppliers and banks, with treasury held for the DENSO or other deals. CFO/PAT C H1 1.48x; ex-payables 0.78x; SA 1.31x / 0.73x (my arithmetic). MSME payables up 52% raise the 45-day Sec 43B(h) question. |
| F12-03 | F12 | R288-R289, R732-R733, R280-R281, R726-R727 | l.244, l.576, l.240, l.573 | C "Provision for warranty \| 124.91 \| 21.81"; "Provision for slow moving inventory \| 80.18 \| 12.03" | FORWARD-SIGNAL | Warranty provision C H1 5.7x YoY. Split: SA 76.31 (vs 30.17), subsidiaries 48.60 (vs -8.36, a release last year). Slow-moving inventory provision 6.7x YoY, all in SA. Inventory SA +29.0% in H1. A new warranty charge in the subsidiary layer points to a product issue outside the parent [INFERENCE]. Together the two provisions cost about 70 bps of H1 margin [NOTION MEMORY]. Whether they recur decides if 23% is the floor. |
| F14-01 | F14 | R938, R972, R005, R933, R953, R1010 | l.128, l.418, l.49, l.90-91, l.303 | "approved by the Company's Board of Directors" (report) vs "13:26:32 +05'30'" and "commenced at 2:00 p.m. (IST)" | AMBIGUOUS | Both review reports state the Statement was "approved by" the Board. They were signed 13:26:32 (SA) and 13:27:12 (C), about 33 minutes before the meeting began at 14:00. Q1 [NOTION MEMORY]: C signed 14:11:24 vs 14:15 start; SA signed 14:40:58, mid-meeting. Two quarters running, and the lead widened from about 4 to about 33 minutes. Bull reading: the Audit Committee reviewed on 25-Oct (l.303) and board approval is procedural. Bear reading: the auditor letter asserts an approval that, on the timestamps, had not happened. |
| F14-02 | F14 | R882 vs R847, R850 | l.437 vs l.56, l.81 | "Sona BLW Precisions Forgings Limited" | NEUTRAL-FACT | Holding company misspelt in the auditor's Annexure 1. Immaterial. Cumulative QC data point with F14-03 and F14-04 and the Q1 press-release QC gaps [NOTION MEMORY]. |
| F14-03 | F14 | R381-R385, R373, R096, R831 | l.311 vs l.309, l.158, l.644 | SA Note 3 "Total \| - \| - \| 16.68 \| - \| [blank] \| 507.91" | NEUTRAL-FACT | SA Note 3 Total for H1 FY26 is blank. Its component (l.309), the SA P&L (l.158) and C Note 3 Total (l.644) all show 108.42. Drafting omission [caveat: A1 transcribed this image-only page visually; the render is the only witness]. |
| F14-04 | F14 | R886, R889, R888 | l.443, l.446, l.445 | "Comestel Automotive Technologies Mexicana Ltd" / "Comestel Automotive Technologies Mexicana, S. DE R.L. DE C.V" | NEUTRAL-FACT | Two near-identical Mexican entity names, plus "Comenergia" (l.445), in a list otherwise named "Comstar". Either two distinct legal entities or a duplicate/typo. Confirm against the FY26 AR entity list. |
| F15-01 | F15 | R898, R974, R1063 | l.458, l.460 | "Novelic India Private Limited*" / "* incorporated as on 28 November 2025" | NEUTRAL-FACT | New versus the Q2 FY26 perimeter (incorporated after 30-Sep-2025). Already present in the Q1 FY27 list [NOTION MEMORY: Step 6B tripwire 3; R-A3-F15-01 baselined]. Count is 17 entities in both Q1 [NOTION MEMORY] and Q2. Verbatim QoQ list diff NOT RUN. |
| F15-02 | F15 | R891, R921, R927, R391, R838 | l.448, l.318, l.651 | "9. Sona Comstar eDrive Private Limited" (wholly owned list) | FORWARD-SIGNAL | Relationship change pending. On close, the Note 5 "100% subsidiary" moves from WOS to 51% (subsidiary or JV, see F1-02). Note 5 does not name it. eDrive Pvt Ltd is the likely vehicle [INFERENCE, NOTION MEMORY 07-Oct RPT approval]. Sona BLW eDrive Mexicana (l.449) is the other candidate. Next-quarter entity list is the confirming observation. |

---

## 2. STANDALONE vs CONSOLIDATED DECOMPOSITION (F2 working, first-class)

Op EBITDA = revenue from operations - (materials + change in inventories) - employee - other expenses. Excludes forex and other income. My arithmetic from l.146-157 and l.470-481. Each EBITDA was checked back to PBT.

| period | SA rev | C rev | C-SA rev | SA op EBITDA (margin) | C op EBITDA ex-fx (margin) | C incl fx margin | C-SA EBITDA (margin on C-SA rev) | SA PAT | C PAT | gap (SA-C)/SA |
|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY27 | 13,770.38 | 15,358.40 | 1,588.02 | 3,066.01 (22.27%) | 3,456.61 (22.51%) | 23.20% | 390.60 (24.6%) | 1,973.79 | 2,229.87 | -12.97% |
| Q1 FY27 | 11,572.38 | 13,012.01 | 1,439.63 | 2,619.77 (22.64%) | 2,934.35 (22.55%) | 23.26% | 314.58 (21.9%) | 2,201.06 | 1,785.13 | +18.90% (ex-div -11.1%) |
| Q2 FY26 | 10,569.85 | 11,382.93 | 813.08 | 2,712.71 (25.66%) | 2,838.31 (24.94%) | 25.39% | 125.60 (15.4%) | 1,662.49 | 1,704.66 | -2.54% |
| H1 FY27 | 25,342.76 | 28,370.41 | 3,027.65 | 5,685.78 (22.44%) | 6,390.96 (22.53%) | 23.22% | 705.18 (23.3%) | 4,174.84 | 4,015.01 | +3.83% (ex-div -12.1%) |
| H1 FY26 | 18,242.99 | 19,922.01 | 1,679.02 | 4,634.33 (25.40%) | 4,893.89 (24.57%) | 24.68% | 259.56 (15.5%) | 2,863.81 | 2,921.73 | -2.02% |
| FY26 | 41,236.74 | 44,494.60 | 3,257.86 | 10,406.47 (25.24%) | 10,811.66 (24.30%) | 24.88% | 405.19 (12.4%) | 6,464.15 | 6,291.90 | +2.66% |

Q2 FY27 PAT bridge C - SA = +256.08: subsidiary op EBITDA +390.60; forex +27.83; other income +22.48; D&A -80.62; finance -32.73; tax -71.48.
Q1 FY27 PAT bridge C - SA = -415.93: op EBITDA +314.58; forex +8.65; other income -560.87 (of which -594.63 dividend elimination); D&A -75.49; finance -33.66; tax -69.14.
JV/associate share: nil. No equity-accounted line exists in the consolidated P&L (l.470-505). Every C-SA gap item is subsidiary contribution or elimination.

Gap trend: QoQ -31.9 pp (FINDING, dividend artefact, F2-01). YoY -10.4 pp (FINDING, subsidiary growth, F2-02). Ex-dividend the Q1 to Q2 move is -1.9 pp.

The SA margin fell 339 bps YoY in Q2 (25.66% to 22.27%). The C ex-forex margin fell 243 bps (24.94% to 22.51%). The subsidiary layer cushions the group margin. Railway sits inside SA (Note 2, l.305: "The Company completed acquisition"), so the SA compression is not a perimeter effect from railway in Q2 (railway was in both Q2 periods).

---

## 3. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 19 zero-standing lines explained. Exceptional line awaits the DENSO gain (F1-01). Consolidated route depends on control vs joint control (F1-02). |
| F2 | FINDING | Gap swung -31.9 pp QoQ (dividend unwind) and -10.4 pp YoY (subsidiary EBITDA x3). Subsidiary funding loop, NCI, forex and interest anomalies (F2-01 to F2-06). |
| F3 | FINDING | No group-level shell (cost lines differ). Identical MSME payables show thin Indian subsidiaries (F3-01). Five unnamed foreign subs (F3-02). No Going Concern anywhere. |
| F4 | PASS | Other-auditor share: assets 2.38%, Q2 revenue 1.37%, Q2 PAT 0.25%, H1 PAT 0.60% (abs) of consolidated. Q1 implied 1.67% (loss 29.75m; [NOTION MEMORY] Rs 2.98 Cr ties). Below 10%, no jump. No unreviewed component. YoY trend not testable (no Q2 FY26 report). |
| F5 | PASS | No Going Concern, no EoM, no modification in either report (l.113-119, l.379-409; "Our conclusion is not modified", l.408). Same five-subsidiary other-auditor scope as Q1 [NOTION MEMORY]. Verbatim paragraph diff NOT RUN: no prior extract. |
| F6 | FINDING | Note 5 DENSO commitments carry no status change one quarter after signing (F6-01). Royalty terms undisclosed (F6-02). Register below. |
| F7 | FINDING | "subject to fulfilment of customary conditions" carried from Q1 (F7-01). No new hedge. |
| F8 | FINDING | SA Q1 ETR shield unwound (F8-01). Persistent deferred charges, no DTA shield (F8-02). FY26 prior-year tax non-zero, immaterial (F8-03). |
| F9 | PASS | Actuarial OCI Q2 7.08 (SA/C) is below the full prior year (FY26 14.11 / 14.07). No swing beyond the prior year. R537 7.05 confirmed by cross-foot. Hedge OCI H1 +277.58 vs FY26 (366.50) is a sign reversal, but its magnitude is below the prior year. |
| F10 | FINDING | First basic-diluted spread (0.01). Q2 share issue +0.34%. MD performance shares (F10-01, F10-02). |
| F11 | PASS | SA 6,241.28 + 56,650.56 = 62,891.84. C 6,241.28 + 57,973.16 + 1,470.73 = 65,685.17 (both dates tie). Other-equity roll-forward: SA residual 1.16m, C residual 6.90m (<0.02%). FY26 total reserves equal Mar other equity. No third-party net-worth figure in context. |
| F12 | FINDING | Single segment, run at entity level. Capitalised development and CWIP build in subsidiaries (F12-01). Borrowings and payables up with treasury (F12-02). Warranty and obsolescence provisions up (F12-03). |
| F13 | PASS | One agenda item: results approval (l.36-38). No AR, AGM, dividend, director, auditor, ESOP or fund-raise item. Signing-time issue is scored under F14. |
| F14 | FINDING | Auditor letter asserts board approval about 33 min before the board met, second quarter running (F14-01). Name misspelling, blank total cell, near-duplicate entity names (F14-02 to F14-04). Q1 columns match the Q1 figures on file [NOTION MEMORY: C PAT 178.51 Cr, SA 220.1 Cr, rev 1,301 Cr], so no restatement is seen. |
| F15 | FINDING | Novelic India new vs Q2 FY26 (F15-01). eDrive WOS-to-51% change pending (F15-02). QoQ verbatim diff NOT RUN. |
| F16 | N.A. | Results filing; presentation-specific check. |
| F17 | N.A. | Results filing; concall-specific check. The Notion live-item cross-reference is in Section 5 as context for A4. |

---

## 4. COMMITMENT REGISTER (F6)

| commitment | implied date | note / line | status word |
|---|---|---|---|
| Form two JVs with DENSO for EV and hybrid powertrain systems | not stated (FY27 per [NOTION MEMORY]) | SA Note 5 l.315; C Note 5 l.648 | signed (definitive agreements 22-Jul-2026); unchanged vs Q1 |
| JV1, DENSO:SONA 51:49, HV liquid-cooled traction motors and controllers, 4W and larger | not stated | l.316 / l.649 | planned ("will have") |
| JV2, SONA:DENSO 51:49, air-cooled traction motors and controllers, 2W/3W | not stated | l.317 / l.650 | planned ("will develop") |
| Slump sale of existing EV motors and controllers business into 100% subsidiary at FMV per independent valuer | not stated; conditional | l.318 / l.651 | pending ("subject to fulfilment of customary conditions") |
| DENSO buys 49% of that subsidiary at EV Rs 17,500m | not stated | l.319 / l.652 | pending ("will buy") |
| Royalty to each JV partner from its majority-owned JV | post-formation | l.319 / l.652 | agreed in definitive agreements; terms undisclosed |
| ESOP Plan 2023: 1,00,000 options granted at Rs 596.35 | granted 16-Jun-2026; vesting per plan | l.313 / l.646 | completed (grant) |
| PSP 2025: 1,70,747 shares to MD at face value on FY26 metrics | NRC approved 05-May-2026 | l.314 / l.647 | approved (allotment consistent with Q1 capital rise [INFERENCE]) |
| Railway Business of Escorts Kubota, Rs 16,426.32m slump sale | completed 01-Jun-2025 | l.305 / l.638 | completed (restated note) |
| WOS dividend Rs 594.63m to parent | received 19-Jun-2026 | SA Note 6 l.320 | completed |

Status transitions vs Q1 [NOTION MEMORY]: none. Note 5 stayed at "signed / conditional". The next expected transition is "completed" for the slump sale and the 49% sale. Its trace in the filing will be (a) eDrive leaving the WOS list, (b) an SA exceptional gain, (c) NCI or equity-accounted income for the 51% vehicle.

---

## 5. NOTION LIVE ITEMS vs THIS FILING (context for A4; not an F17 silence audit)

| Notion live item [NOTION MEMORY] | what this filing shows | cite |
|---|---|---|
| C op EBITDA margin bull >=24.5% / bear <23.0% (forex ruling pending) | 22.51% ex-forex; 23.20% incl forex. Bull fails on both bases; bear depends on the ruling. Realised forex likely exceeds the P&L line (F2-05). | l.470-479, l.579 |
| CFO/PAT >=1.0x (and ex-payables) | C 1.48x; ex-payables 0.78x. SA 1.31x / 0.73x. C current tax liability +261.67 also helps CFO. | l.591, l.585, l.488, l.553 |
| DENSO close / eDrive deconsolidation | Not closed. eDrive in WOS list. No held-for-sale line. Language unchanged. | l.448, l.651-652 |
| Auditor signing time vs board start | 13:26:32 / 13:27:12 vs 14:00 start. Second quarter running. | l.128, l.418, l.49 |
| Short-term borrowings | C 2,342.54 to 4,619.72; of which subsidiaries 152.54 to 771.25. | l.546, l.213 |
| ROCE | Not disclosed in this filing (deck item). | none |
| Novelic (tripwire 3) | No impairment line. NCI-implied loss narrowed to about -9.1m in Q2. Five foreign subs H1 loss (24.20). | l.497, l.391 |

---

## 6. FLAGS FOR A4 (management questions)

FORWARD-SIGNAL: F1-01, F2-02, F2-04, F3-01, F6-01, F12-01, F12-03, F15-02.
AMBIGUOUS: F1-02, F2-03, F2-05, F2-06, F3-02, F6-02, F7-01, F12-02, F14-01.

Pipeline notes: (1) Prior-quarter verbatim diffs for F5 and F15 could not run; a Q1 FY27 A1 extract would close this. (2) 34 A1 structured rows carry column-status or caption text absent from the fulltext line (Section 0). (3) SA Note 3 blank cell rests on a visual transcription of an image-only page.

```yaml
stage: A3-forensics
company: "SONACOMS"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/forensics_results_sonacoms_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: PASS
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "F1-01", check: "F1", line: "l.158, l.482, l.309-311, l.642-644", classification: "FORWARD-SIGNAL", implication: "Exceptional line nil in FY27; DENSO slump-sale and 49% sale gain lands here in SA; DENSO deal costs not booked as exceptional"}
  - {id: "F1-02", check: "F1", line: "l.315, l.319, l.651-652", classification: "AMBIGUOUS", implication: "Note 5 says both 'Joint Ventures' and 'this subsidiary'; control kept = consolidated equity transaction, no P&L gain; joint control = deconsolidation plus remeasurement gain; no held-for-sale line"}
  - {id: "F1-03", check: "F1", line: "l.161, l.166, l.237, l.243, l.266, l.279, l.485, l.490, l.570, l.597, l.610", classification: "NEUTRAL-FACT", implication: "Remaining 15 zero-standing lines are template or one-off; C nil purchase of NC investments vs SA 330.51 routed to F2-03"}
  - {id: "F2-01", check: "F2", line: "l.164, l.488, l.148, l.320", classification: "NEUTRAL-FACT", implication: "SA-C PAT gap +18.90% to -12.97% (-31.9 pp QoQ) is the Q1 Rs 594.63m WOS dividend unwinding; ex-dividend move about -1.9 pp; consolidated is the honest basis"}
  - {id: "F2-02", check: "F2", line: "l.146-156, l.470-480", classification: "FORWARD-SIGNAL", implication: "Gap widened 10.4 pp YoY; subsidiary op EBITDA 125.60 to 390.60 (15.4% to 24.6% margin), now 11.3% of group; 49% leaks to NCI if moved into a 51% vehicle"}
  - {id: "F2-03", check: "F2", line: "l.265 vs l.597, l.213 vs l.546, l.278 vs l.609, l.320", classification: "AMBIGUOUS", implication: "WOS paid parent 594.63m, parent injected 330.51m, subsidiary ST debt 152.54 to 771.25; dividend partly debt-funded at group level; entities unnamed"}
  - {id: "F2-04", check: "F2", line: "l.497, l.538, l.451", classification: "FORWARD-SIGNAL", implication: "NCI-implied Novelic-group loss about -9.1m Q2 vs -42.5m Q1 vs -50.1m Q2 FY26; narrowing bears on tripwire 3; one quarter only"}
  - {id: "F2-05", check: "F2", line: "l.147, l.471, l.247, l.579", classification: "AMBIGUOUS", implication: "P&L forex gain 197.48 C H1 sits beside an unrealised forex loss add-back 116.68; realised forex likely larger than P&L line; input to pending forex-treatment ruling; C Q2 margin 22.51% ex-fx / 23.20% incl"}
  - {id: "F2-06", check: "F2", line: "l.284 vs l.615, l.153 vs l.477", classification: "AMBIGUOUS", implication: "Consolidated interest paid below standalone in both H1s; possible intra-group loan from a subsidiary to the parent"}
  - {id: "F3-01", check: "F3", line: "l.215, l.548, l.310, l.643", classification: "FORWARD-SIGNAL", implication: "Identical SA/C MSME payables; Indian subsidiaries incl eDrive carry no MSME dues and thin payroll; divergence after close will confirm the slump sale"}
  - {id: "F3-02", check: "F3", line: "l.388-394, l.400, l.453-457", classification: "AMBIGUOUS", implication: "Five unnamed foreign subs: assets 2,007.38, H1 loss 24.20; count matches the five foreign Novelic entities (inference); relevant to Novelic carrying value"}
  - {id: "F6-01", check: "F6", line: "l.318, l.651, l.448", classification: "FORWARD-SIGNAL", implication: "No DENSO status transition 96 days after signing; eDrive still WOS; like-for-like H1 holds; close date unstated"}
  - {id: "F6-02", check: "F6", line: "l.319, l.652", classification: "AMBIGUOUS", implication: "Royalty to each partner from its majority JV; rate, base, term undisclosed; net margin effect unknown"}
  - {id: "F7-01", check: "F7", line: "l.318, l.651", classification: "AMBIGUOUS", implication: "'subject to fulfilment of customary conditions' carried from Q1, conditions unlisted; gain timing and quantum undefined; no new revenue or concentration hedge"}
  - {id: "F8-01", check: "F8", line: "l.159, l.163", classification: "NEUTRAL-FACT", implication: "SA ETR Q1 20.14% to Q2 25.01%; Q1 dividend shield unwound; C ETR 24.66% to 25.91% near statutory"}
  - {id: "F8-02", check: "F8", line: "l.162, l.486, l.211, l.544", classification: "NEUTRAL-FACT", implication: "Persistent deferred tax charges, no DTA shield; cash tax below book via DTL build; slower capex means cash tax converges up"}
  - {id: "F8-03", check: "F8", line: "l.161, l.485", classification: "NEUTRAL-FACT", implication: "Prior-year tax 9.13 SA / 8.26 C in FY26 only; immaterial"}
  - {id: "F10-01", check: "F10", line: "l.171, l.173-174, l.504-505", classification: "NEUTRAL-FACT", implication: "First basic-diluted EPS spread (0.01); Q2 capital +2,093,587 shares (+0.34%) from ESOP exercises"}
  - {id: "F10-02", check: "F10", line: "l.314, l.647", classification: "NEUTRAL-FACT", implication: "1,70,747 performance shares to MD at face value; about Rs 13.4 Cr at Rs 782; not in Notion share log"}
  - {id: "F12-01", check: "F12", line: "l.190 vs l.521, l.187 vs l.518", classification: "FORWARD-SIGNAL", implication: "Subsidiaries hold 2,996.60 capitalised development (+5.1% H1) and CWIP 776.26 (+57%); build in a loss-making layer is first in line for impairment"}
  - {id: "F12-02", check: "F12", line: "l.213, l.215-216, l.546, l.197, l.200-201", classification: "AMBIGUOUS", implication: "ST borrowings +75.7% SA / +97.2% C and payables +58.8% while treasury rose; arbitrage or supplier-funded WC; CFO/PAT 1.48x vs 0.78x ex-payables"}
  - {id: "F12-03", check: "F12", line: "l.244, l.576, l.240, l.573", classification: "FORWARD-SIGNAL", implication: "Warranty provision C 124.91 vs 21.81 (subsidiaries 48.60 vs -8.36); slow-moving inventory 80.18 vs 12.03; recurrence decides the margin floor"}
  - {id: "F14-01", check: "F14", line: "l.128, l.418, l.49, l.90-91, l.303", classification: "AMBIGUOUS", implication: "Review reports cite board approval but were signed about 33 min before the 14:00 start; second quarter running, lead widened from about 4 min"}
  - {id: "F14-02", check: "F14", line: "l.437", classification: "NEUTRAL-FACT", implication: "Holding company spelt 'Precisions' in Annexure 1; cumulative QC point"}
  - {id: "F14-03", check: "F14", line: "l.311", classification: "NEUTRAL-FACT", implication: "SA Note 3 H1 FY26 total blank vs 108.42 elsewhere; drafting omission (visual transcription caveat)"}
  - {id: "F14-04", check: "F14", line: "l.443, l.446", classification: "NEUTRAL-FACT", implication: "Two near-identical 'Comestel ... Mexicana' entity names; confirm distinct entities against AR"}
  - {id: "F15-01", check: "F15", line: "l.458, l.460", classification: "NEUTRAL-FACT", implication: "Novelic India new vs Q2 FY26 perimeter, already in Q1 list per Notion memory; 17 entities both quarters; verbatim diff not run"}
  - {id: "F15-02", check: "F15", line: "l.448, l.318, l.651", classification: "FORWARD-SIGNAL", implication: "eDrive WOS-to-51% relationship change pending on DENSO close; next entity list confirms vehicle and accounting"}
forward_signals: ["F1-01", "F2-02", "F2-04", "F3-01", "F6-01", "F12-01", "F12-03", "F15-02"]
ambiguous: ["F1-02", "F2-03", "F2-05", "F2-06", "F3-02", "F6-02", "F7-01", "F12-02", "F14-01"]
commitments:
  - {commitment: "Form two JVs with DENSO (EV and hybrid powertrain)", implied_date: "not stated", ref: "SA Note 5 l.315; C Note 5 l.648", status_word: "signed 22-Jul-2026, unchanged vs Q1"}
  - {commitment: "Slump sale of EV motors and controllers business into 100% subsidiary at FMV per independent valuer", implied_date: "not stated, conditional", ref: "l.318; l.651", status_word: "pending (subject to customary conditions)"}
  - {commitment: "DENSO buys 49% of that subsidiary at EV Rs 17,500m", implied_date: "not stated", ref: "l.319; l.652", status_word: "pending"}
  - {commitment: "Royalty to each JV partner from its majority-owned JV", implied_date: "post-formation", ref: "l.319; l.652", status_word: "agreed, terms undisclosed"}
  - {commitment: "ESOP Plan 2023: 1,00,000 options at Rs 596.35", implied_date: "granted 16-Jun-2026", ref: "l.313; l.646", status_word: "completed (grant)"}
  - {commitment: "PSP 2025: 1,70,747 shares to MD at face value", implied_date: "NRC approved 05-May-2026", ref: "l.314; l.647", status_word: "approved"}
  - {commitment: "WOS dividend Rs 594.63m to parent", implied_date: "received 19-Jun-2026", ref: "SA Note 6 l.320", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "Consolidated stays the honest basis. Q1's +18.9% standalone premium was the Rs 594.63m WOS dividend. Ex-dividend, the gap sits near -11% to -13% in both quarters. The real change is YoY: subsidiary op EBITDA tripled (125.6m to 390.6m) and is now 11.3% of group. That matters for DENSO. Note 5 calls the vehicle both 'Joint Ventures' and 'this subsidiary'. If Sona keeps control at 51%, the consolidated 49% sale is an equity transaction and never reaches the exceptional line; only standalone books a gain. Under joint control the group deconsolidates and remeasures the retained 51% through P&L. Neither balance sheet has a held-for-sale line. Subsidiary short-term debt rose from 152.5m to 771.3m in the half in which one WOS paid the parent 594.63m and the parent put 330.51m back in. Gate inputs: margin 22.5% ex-forex / 23.2% incl forex. CFO/PAT 1.48x, or 0.78x ex-payables. The 116.68m unrealised forex loss add-back suggests realised forex exceeds the P&L line, relevant to the pending forex ruling. F5 and F15 verbatim diffs did not run; Q1 facts are Notion memory."
```
