# A5 ADVERSARY / COMPLETENESS AUDIT: Tejas Networks Limited (TEJASNET), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date 2026-10-23
Review under audit: runs/tejasnet-q2fy27/work/review_tejasnet_q2fy27.md (A4, 1,035 lines; "rv L###" = review line)
Inputs read: A1 fulltexts (results, concall, presentation), A1 structured (R001-R851 / R001-R324 / R001-R210), A2 ledgers (3), A4 review. Source PDFs, inputs/ and A3 notes not opened.
Anchor key: RL / CL / PL = results / concall / presentation fulltext line; R### = A1 structured row ID.
Write log: sections written in order after a network drop (coordinator message, ~18:47 IST). Audits 0-1 first, then 2, then 3, verdict, style notes, YAML. File complete. Block copy: runs/tejasnet-q2fy27/work/blocks/a5.yaml.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

Plain-language brief at rv L895-949.

| Part | Heading (rv line) | Present / empty | Note |
|---|---|---|---|
| 1 Summary narrative | "1. SUMMARY NARRATIVE" (rv L899) | PRESENT | 14 lines (rv L900-913), inside the 10-20 line band; provenance tags on every line |
| 2 Sector | "2. SECTOR INTELLIGENCE" (rv L915) | PRESENT | 6 bullets, anchored CL/PL/RL |
| 3 Business model | "3. BUSINESS-MODEL INTELLIGENCE" (rv L923) | PRESENT | 5 bullets (see CONTRADICTION C2 on the break-even line rv L927) |
| 4 Competition | "4. COMPETITION INTELLIGENCE" (rv L930) | PRESENT | 4 bullets (see FACTUAL F1 on rv L934) |
| 5 Forward map | "5. FORWARD MAP" (rv L936) | PRESENT | 13 catalysts, each with a Bull and a Bear fork; 10 dated, 3 labelled "Undated"/"Any board outcome" (rv L947-949), honest NOT DISCLOSED labelling (STYLE S4) |

DELIVERABLE-COMPLETENESS: PASS. All five parts present and non-empty.

---

## AUDIT 1: COVERAGE

Method: fresh line-by-line pass over each A1 FULLTEXT, counted by A2's category definitions, then diffed against the structured file (grep by line number) and the A2 ledger. Orphan test: each ledger row checked for an A4 citation or the explicit "reviewed" mark.

Orphan test result: A4 rv L14 states "All 851 / 52 / 13 reviewed (results 851 of 851 IDs, concall 324 of 324 IDs, presentation 210 of 210 IDs ... No unreviewed row)". This is the explicit "reviewed" mark for every ledger row. Spot check of every A2-flagged row: OCR pairs R327/R339 (rv L78), R428/R434 (rv L92), R187/R221 (A3 OCR list, rv L15); UNREVIEWED_SUBS R826-R828 (rv L61); R830 xref (rv L49, resolved: cons note 5 is the charge, so the "Refer note-5" xref is correct); TITLE_DISCREPANCY R068 (rv L457, Q17); MGMT_ABSENCE R071/R072 (rv L461); R317 FOOTNOTE_UNRESOLVED (rv L1002, PL337); R209 order-book basis (rv L413, L921); R210 DROPPED_SLIDE (rv L473); CHART_DATA_NOT_EXTRACTED (rv L802); ZERO_STANDING R024/R026/R028 (rv L331). All covered. Orphan rows: none.

### 1A. Results (fulltext RL1-826)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Numbered notes | 12 (std 5 + cons 7) | 12 (RL370, 375, 378, 381, 384; RL757, 769, 775, 778, 799, 802, 805) | none | PASS |
| Footnotes | 2 | 2 (RL646, RL796) | none | PASS |
| Line items | 238 | 242 | none | FAIL (4 missing from structured and ledger) |
| - std P&L | 26 | 28 | | RL159 "(1) Current tax expense/(benefit) : ; 2 é" and RL170 "Income tax relating to above . . * - . *" have no row |
| - std balance sheet | 38 | 38 | | tie |
| - std cash flow | 52 | 53 | | RL338 "Ather finance cast 10.99) {NR" (Other finance cost) has no row; H1 FY27 value (0.99) by identity to RL339 641.14, H1 FY26 (0.89) by identity to RL339 631.74 |
| - cons P&L | 29 | 29 | | tie |
| - cons balance sheet | 38 | 38 | | tie |
| - cons cash flow | 52 | 53 | | RL715 "Repayment of borrowings - non- current (161.22) ." has no row; value confirmed by identity: RL712-725 sum to 641.08 = RL726 only with (161.22) |
| - note 4 summary | 3 | 3 | | tie |
| Zero-standing rows | 37 | 37 + RL159 and RL170 dash cells (column assignment unresolved, up to 12 cells) | none | FAIL (follows line items) |
| Agenda items | 1 | 1 (RL30-34) | none | PASS |
| Auditor paragraphs | 11 (QUALIFIER rows) | 12 paragraphs (std 4: RL76, 86, 93, 104; cons 8: RL423, 437, 444, 456, 480, 488, 496, 507) | none | FAIL (minor): cons para 5 unmodified conclusion RL488-494 has no structured row (R823 is the standalone conclusion RL104; R828 is the Other Matter closing RL507). A4 reviewed it directly (rv L61), so no review content is lost |
| Consolidation entities | 4 | 4 (RL482-486; RL757-767) | none | PASS |
| Signature blocks | 5 | 5 (RL46-52, 111-117, 388-391, 508-514, 809-812) | none | PASS |
| ID accountability | 851 / 851 | 851 | none | PASS |

Materiality of the results gap: RL715 (161.22 repayment of non-current borrowings) is a debt-flow line. Without it the H1 non-current borrowing flow reads as 855.72 gross proceeds, not 694.50 net. A4 does not use either figure, so no A4 number is wrong, but the ledger cannot show the full debt bridge (cash-flow net borrowing 799.17 vs balance-sheet rise 799.88, RL629 + RL635). RL338, RL159 and RL170 are immaterial (0.99 and dash rows).

Root cause: A1 dropped these units from the structured file. A2's count test greps the structured file only ("grep = distinct page+line among NUMBER R001-R694", ledger L9), so it cannot see a fulltext unit that A1 never rowed.

### 1B. Concall (fulltext CL1-624)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Participants | 9 | 9 (5 mgmt CL55-64, host CL66, 2 analysts, moderator) | none | PASS |
| Speaker turns | 52 | 52 (T01 CL72 to T52 CL619, re-mapped from content) | none | PASS |
| Questions | 15 | 15 (T09, 11, 13, 15, 17, 19, 24, 27, 30, 32, 38, 40, 43, 45, 47) | none | PASS |
| Management numbers | 53 | 53 (T03 13, T04 19, T05 9, T06 7, plus CL349, 404, 462, 498, 562). The CL356 restatement of "INR1,500 crores" is held as QUALIFIER R303; accepted | none | PASS |
| Forward phrases | 64 | 65 | none | FAIL (minor): CL524-526 "those are due, which whatever comes in, significant amount is going to come in" (collections from past milestones) has no row; R236/R237 cover debt only (CL528-529) |
| Hedge / qualifier phrases | 37 | 39 | none | FAIL (minor): CL516-517 "That's all I can say" and CL590-591 "That's about all I can say. I cannot comment on the revenue numbers" have no rows (R315 is CL514, R320 is CL584). A4 counts both in its 7 defensive phrases (rv L757), so the review is not affected |
| Dates | 38 | 38 by A1's rule (one row per new period phrase; repeats at CL109-117 and CL139-140 folded; CL104 held in FORWARD R188) | none | PASS |
| Entities (non-turn) | 72 | named counterparties spot-checked present: BSNL, TCS, NEC, Rakuten R115, Qualcomm R096, Vi R116, TSDSI R095, TEPC R093, Kavach R122, GoI Enterprise R088, ISPs R089, pan-African operator R090 | none | PASS (spot) |
| ID accountability | 324 / 324 | 324 | none | PASS |

### 1C. Presentation (fulltext PL1-349)

| Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides / pages | 13 | 13 (p1 cover, p2-13) | none | PASS |
| Slide numbers | 98 | 98 (p1 5, p3 13, p4 41, p5 21, p6 4, p7 2, p8 2, p9 7, p10 2, p13 1) | none | PASS |
| Forward statements | 48 | 48 (spot: p11 PL305-318 7 rows; p12 PL324-339 8 rows) | none | PASS |
| Dates | 15 | 15 | none | PASS |
| Footnotes / qualifiers | 20 | 20 | none | PASS |
| Zero-standing | 3 | 3 (R024, R026, R028) | none | PASS |
| Entities | 29 | 29 (spot) | none | PASS |
| ID accountability | 210 / 210 | 210 | none | PASS |

### 1D. Coverage result

- orphan_rows: none (A4 explicit all-reviewed mark, flagged rows verified).
- missing_from_ledger (fresh-pass units the structured file and ledger lack): results RL159, RL170, RL338, RL715, RL488-494; concall CL516-517, CL524-526, CL590-591.
- Finding M1 (MISSING, loop A2): add these units to the structured file and ledger (A2 to route the structured re-extract to A1 or record them as MISSING_FROM_STRUCTURED rows), and add a fulltext-vs-structured count to the A2 count test. Only RL715 is material; the rest are immaterial or already used by A4.

---

## AUDIT 2: ARITHMETIC

Every derived metric in A4's tables recomputed from the raw extracted lines. PASS = within rounding (0.01 Cr, 0.01 pp, 0.1 day).

### 2A. P&L identities and OCR repairs

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Cons revenue Q2 FY27 (OCR "205.68") | 405.68 | 413.45 - 7.77 = 405.68; RL533 405.68 + RL534 nil | RL533-537 | PASS |
| Cons other income Q2 (OCR "777") | 7.77 | 413.45 - 405.68 = 7.77 | RL536-537 | PASS |
| Std other income Q2 (OCR "781") | 7.81 | 412.72 - 404.91 = 7.81 | RL144-146 | PASS |
| Cons total expenses Q2 | 690.33 | 237.81+26.48-13.70+105.14+86.53+91.48-10.55+167.14 = 690.33 | RL539-547 | PASS |
| Std total expenses Q2 | 690.43 | 237.84+26.48-13.70+100.84+86.50+91.48-10.55+171.54 = 690.43 | RL148-156 | PASS |
| Cons tax FY26 (OCR "945.12") | 445.12 | 0.02 + 445.10 = 445.12; 1,354.01 - 908.89 = 445.12 | RL550-553 | PASS |
| Cons tax H1 FY27 (OCR "138.53") | 138.51 | 547.69 - 409.18 = 138.51 | RL548, RL553 | PASS |
| Std tax Q2 FY26 (OCR "265.86") | 165.86 | 473.03 - 307.17 = 165.86 | RL157, RL162 | PASS |
| Std PAT H1 FY27 (OCR "410.03") | 410.01 | 548.52 - 138.51 = 410.01; RL794 410.01 | RL157, RL794 | PASS |
| Std employee H1 FY26 (OCR "123.84") | 183.84 | 1,249.27 - 1,065.43 = 183.84 | RL148-156 | PASS |
| Cons other op revenue Q2 FY26 | 5.15 (cited RL534) | RL534 reads "5.5"; 261.82 - 256.67 = 5.15 | RL533-535 | PASS (value); label STYLE S3 |

### 2B. Derived metrics (rv L121-147)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA cons Q2 FY27 / Q1 / Q2 FY26 | (106.64) / (100.36) / (293.70) | -276.88+91.48+86.53-7.77; -270.81+94.35+85.07-8.97; -472.99+100.98+84.32-6.01 | RL536, 543, 544, 548 | PASS |
| Op EBITDA cons FY26 / H1 FY26 / H1 FY27 | (681.83) / (429.37) / (207.00) | identical formula | same | PASS |
| Op EBITDA std Q2 / Q1 / Q2 FY26 | (107.54) / (100.39) / (293.80) | -277.71+91.48+86.50-7.81 etc. | RL145-157 | PASS |
| Op EBITDA margin cons | -26.29 / -24.96 / -112.18 / -61.80 / -92.70 / -25.62% | same | | PASS |
| Op EBITDA margin std | -26.56 / -24.98 / -112.41% | same | | PASS |
| Reported EBITDA | (98.87) / (91.39) / (287.69) / (648.45) / (413.81) / (190.26) | PBT + D + Fin | | PASS |
| Core PBT (ex-OI) | (284.65) [S (285.52)] / (279.78) / (479.00) [S (479.04)] / (1,387.39) / (785.90) / (564.43) | PBT - OI | | PASS |
| OI as % of loss | 2.81 / 3.31 / 1.27 / 2.47 / 2.02 / 3.06% | same | | PASS |
| Effective tax (credit) rate | 25.26 [S 25.18] / 25.32 / 35.07 [S 35.06] / 32.87 / 34.96 / 25.29% | Tax / PBT | RL548-552 | PASS |
| PAT margin | -51.01 [S -51.31] / -50.29 [S -50.32] / -117.31 [S -117.52] / -82.38 / -108.16 / -50.65% | same | | PASS |
| Gross margin | 38.23% (155.09); 36.05% (144.98); -3.00% (-7.86); ex-charge 52.54% (137.57); FY26 30.48% (336.30); H1 FY27 37.14% (300.07) | Rev - (CoM + purchases + inventory change) | RL535, RL539-541, RL799 | PASS |
| S-vs-C gaps (rev / PAT / %) | Q2 0.77 / 0.83 / 0.40%; Q1 0.21 / 0 / 0; Q2 FY26 0.45 / 0.04 / 0.01%; H1 FY27 0.98 / 0.83 / 0.20%; H1 FY26 (0.10) / 0.08 / 0.02%; FY26 2.50 / 7.54 / 0.82% | same | RL144, RL162, RL535, RL553 | PASS |
| Unreviewed-subsidiary revenue Q1 / intra-group | 0.86 / 2.75 | 4.38 - 3.52; 3.52 - 0.77 | RL499 | PASS |

### 2C. YoY, sequential, PAT bridge (rv L153-235)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Revenue YoY | +143.86 (+54.95%) | 405.68 - 261.82; 143.86 / 261.82 | RL535 | PASS |
| Op EBITDA YoY; ex-charge base; ex-charge gain | +187.06 (63.7%); (148.27); +41.63 | -293.70 + 145.43; -106.64 + 148.27 | RL799 | PASS |
| Margin change; ex-charge base margin | +85.89 pp; -56.63%, +30.34 pp | | | PASS |
| D&A / finance / OI YoY | -9.50 (-9.41%) / +2.21 (+2.62%) / +1.76 (+29.28%) | | RL536, 543, 544 | PASS |
| Operating EBIT | (394.68) / (198.12), +196.56 | Op EBITDA - D&A | | PASS |
| Core PBT YoY; ex-charge | +194.35 (40.6%); (333.57), +48.92 | | | PASS |
| PBT / PAT / EPS YoY | +196.11 (41.5%) / +100.19 (32.6%) / +5.76 (33.1%) | | RL548, 553, 569 | PASS |
| H2 run-rate to Rs 2,000 Cr floor | 596.08 / qtr, +46.9% vs Q2 | (2,000 - 807.84) / 2; / 405.68 | RL535 | PASS |
| Q1 FY26 derived | 201.38; (135.67); -67.37%; (306.90); Q2 FY26 +30.0% | H1 FY26 - Q2 FY26 | RL535, RL548 | PASS |
| H2 FY26 derived | 640.08 (320.04 / qtr); (252.46); -39.44%; core (601.49) | FY26 - H1 FY26 | | PASS |
| QoQ | rev +3.52 (+0.88%); op EBITDA -6.28; core PBT -4.87; PAT -4.70; other exp +35.12 | | | PASS |
| Other expenses ex-warranty Q1 / Q2 | 96.91 / 159.90, +62.99 (+65.0%) | 132.02 - 35.11; 167.14 - 7.24 | RL546, RL802 | PASS (arithmetic); the forex explanation is refuted, FACTUAL F3 in Audit 3 |
| Estimate-adjusted Q2 op EBITDA | (153.14), -37.75%; releases 46.50 | -106.64 - 27.87 - 18.63 | RL545, RL802 | PASS |
| Q2 vs H1 average | 403.92, +0.44% | | | PASS |
| PAT bridge lines | +145.43; +75.59; -58.06; -10.79; +37.20; -28.43; +26.13; +9.50; -2.21; +1.76 = 196.12 | gross-margin line unrounded -58.07; cross-check: gross profit change 162.95 = 145.43 + 17.52; other-expense change 8.77 = 37.20 - 28.43; total 196.11 | RL535-548, RL799, RL802-803 | PASS (0.01 rounding, A4 states it) |
| Non-recurring + estimate total; recurring residual | 208.76; (12.65) | 145.43 + 37.20 + 26.13; 196.11 - 208.76 | | PASS |
| Finance cost annualised; gross borrowing rise | 346.12 (+14.3% vs 302.83); +799.88 | 86.53 x 4; 4,835.35 - 4,035.47 | RL543, RL629, RL635 | PASS |
| DTA / equity; DTA + IAUD / equity | 19.93%; 1,401.50 = 55.45% | 503.75 / 2,527.60; (503.75 + 897.75) / 2,527.60 | RL601, 607, 625 | PASS |
| Run-rate PAT at Q1 estimate rates | (242.0) at "25.17%" | (323.38) x (1 - 0.2526) = (241.70) at the Q2 cons rate; 25.17% has no source | RL548-552 | PASS within 0.3; STYLE S2 |

### 2D. Cash and balance sheet (rv L241-271)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| CFO change | +198.39 | -311.93 + 510.32 | RL700 | PASS |
| Capex H1 FY26 / H1 FY27; intangible share | 546.92 / 397.18 (-149.74); 90% | 116.19 + 430.73; 38.59 + 358.59; 358.59 / 397.18 = 90.3% | RL702-703 | PASS |
| FCF | (1,057.24) / (709.11), +348.13 | CFO - capex | | PASS |
| WC change (sum RL690-697) | (128.72) / (102.64), +26.08 | sums tie; -208.77 - 102.64 = -311.41 = RL698 | RL688-698 | PASS |
| Receivable days Mar-26 | 1,078.8 (on 3,260.78) | RL604 non-current receivable 4.33 fails its subtotal: RL597-608 Mar-26 sum 2,509.16 (ROU at 114.07; RL598 "214.07" is a second OCR misread) vs RL609 2,505.16, gap 4.00; std RL218 1.33 fails RL223 by 1.00. Identity points to 0.33 in both: 3,256.78 / 1,103.28 x 365 = 1,077.5 days | RL604, RL609, RL614 | FAIL (FACTUAL F2, low severity): OCR-suspect input used without the OCR label A4 applies elsewhere; range 1,077.5-1,078.8 days |
| Receivable days Sep-26 | 487.8 | 2,159.34 / 1,615.68 x 365 | RL604, RL614 | PASS |
| Inventory days | 1,160.3 / 831.8 | 2,438.19 / 766.98 x 365; 2,314.40 / 1,015.54 x 365 | RL539-541, RL611 | PASS |
| Payable days | 227.5 / 158.9 | 477.95 / 766.98 x 365; 442.22 / 1,015.54 x 365 | RL638-639 | PASS |
| CCC | 2,011.6 / 1,160.7 (-850.9) | Mar-26 2,010.3 if the 0.33 identity holds (F2) | | Mar-26 follows F2; Sep-26 PASS |
| PPE / IAUD / other intangibles | -40.85 / -52.68 / +302.05 | | RL597, 600, 601 | PASS |
| Capitalised into intangibles (cash basis) | about 411 | 950.43 + 358.59 - 897.75 = 411.27 | RL601, RL703 | PASS |
| Net debt ex-lease Mar-26 / Sep-26 | 3,530.67 / 4,384.39 (+853.72) | (551.83 + 3,483.64) - (102.68 + 364.89 + 37.23); (1,162.40 + 3,672.95) - (109.76 + 303.99 + 37.21) | RL613-616, 629, 635 | PASS; ties deck 3,531 / 4,384 (PL169) and cash 505 / 451 (PL168) |
| Net debt incl. lease | 3,672.28 / 4,518.90 (+846.62) | + 141.61; + 134.51 | RL630, RL636 | PASS |
| Headroom to Rs 4,500 Cr; Q1 headroom; QoQ rise | 115.61; 223; +107.39 | 4,500 - 4,384.39; 4,500 - 4,277; 4,384.39 - 4,277 | PL169 | PASS |
| Q1 gross debt (deck-derived); QoQ gross fall | 4,866; 30.65 | 4,277 + 589; 4,866 - 4,835.35 | PL168-169 | PASS |
| Book value per share | 139.33 / 141.93; Mar-26 161.92 | 2,527.60 / 18.141; / 17.809; 2,930.87 / 18.101 | RL623, RL625 | PASS |
| EPS-implied shares | 17.809 Cr | 206.94 / 11.62 | RL553, RL569 | PASS |
| NWC (deck definition, A5 check) | not computed by A4 | Sep-26 5,583.15 - 450.96 - (4,586.81 - 3,672.95 - 16.59) = 4,234.92; Mar-26 4,137.90 | RL611-643; PL163 4,235 / 4,138 | ties |

### 2E. Thesis, concall and synthesis arithmetic

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Annualised revenue; H1 loss vs FY29E bear | 1,622.72; 2.5x | 405.68 x 4; 409.18 / 165 = 2.48 | RL535, RL553 | PASS |
| TTM operating ROCE | -12.31% | H2 FY26 op EBIT (252.46) - 205.29 = (457.75); H1 FY27 (207.00) - 185.83 = (392.83); (850.58) / 6,911.99 | RL544, RL625 | PASS |
| Finance cost QoQ (#10) | +1.46 (+1.7%) | 86.53 - 85.07 | RL543 | PASS |
| BSNL value vs record | -1.7% | 1,500 / 1,526 - 1 | CL349 | PASS |
| Implied Q2 order inflow | about 1,192 | 2,315 - 1,529 + 405.68 = 1,191.68 | PL85, RL535 | PASS |
| CMP vs QIP line | 6.0% above | 424 / 400 - 1 | digest | PASS |
| Break-even revenue (op EBITDA / PBT) | about 684.6 / 1,130 per qtr | 261.73 / 0.3823 = 684.6; 431.97 / 0.3823 = 1,129.9 | RL542, 545, 546 | PASS (arithmetic); input base contradicts Step 3, CONTRADICTION C2 in Audit 3. On Q1 estimate rates: 308.23 / 0.3823 = 806.3; 478.47 / 0.3823 = 1,251.6 |
| Q&A share of call lines | 53.6% | 296 / 552 | CL69-620 | PASS |
| Opening claims quantified; forward quantified | 24 / 45 (53%); 0 / 10 | recount of rv L484-528 | | PASS |
| Credibility ratio | 55.0% | 2.75 / (9 - 4) | rv L568-582 | PASS |
| Q&A grade count | A2 B6 C3 D4 (15) | recount rv L639-653 | | PASS |
| Prior-question tally | 0 / 6 / 1 / 12 = 19 | recount rv L609-627 | | PASS |
| Specificity | 13 / 64 = 0.20 (11 / 62 = 0.18) | | R186-R249 | PASS |
| Defensive phrases | 7 | CL340, 355, 412, 514, 516, 584, 590-591 | | PASS |
| Deck vs filing EBITDA | differ by under 2.0 | (108) vs (106.64); (99) vs (100.36); (293) vs (293.70) | PL131 | PASS |

Arithmetic result: no mismatch above rounding except F2 (OCR-suspect Mar-26 receivable input, 1.3 days). Every other derived metric in A4's tables ties to the extract.

---

## AUDIT 3: ADVERSARIAL READ

A4's review leans bearish. The three MOST POSITIVE claims it makes are the ones that keep the thesis alive: the BSNL trigger has fired, the net-debt trigger has not, and two growth triggers are on track. Each is attacked from the same extract.

### Mandatory acquisition-economics probe
Not triggered. No document describes an acquisition, purchase or stake buy. The NEC item is a technology licence: "we have licensed the massive MIMO 5G radio technology from NEC" (CL585), with no consideration disclosed. The consolidation entity list is unchanged (RL482-486, RL763-767). Investing cash flows are liquid-fund churn (RL707-708) and capex (RL702-703). No purchase multiple exists to state.

### Claim 1: BSNL add-on trigger "FIRED (award)"; Gate 1 "met in substance"; checklist #7 AMBER, "Not RED: scope not reduced"; thesis-broken "BSNL PO not confirmed" NOT FIRED (rv L330, L344, L355, L399, L813)
- Strongest bear counter: The filed Reg 30 deck never says PO. It says "Received the LOI for 18k+ 4G sites" (PL69, PL93) and "Received LoI from TCS for 18,685 add-on sites" (PL187). POs exist only in speech: "LOI and subsequent POs" (CL97-98) and "a part of it ... as and when we get the POs" (CL346-350). The BSNL value inside the book is refused (CL355-358). The implied Q2 order inflow is about 1,192 (2,315 - 1,529 + 405.68, PL85, RL535), and it includes non-BSNL wins named in the same call: BharatNet routers, GoI OTN, GPON, Africa 400G (CL157-168, CL357-358). So the BSNL PO value in the book is below 1,192, and could sit well below the 1,526 on record. The counterparty is TCS (PL187), while the thesis condition names a BSNL PO.
- Does it survive? The quantitative parts are already in A4 (Q3 rv L413, #7 rv L330, pres:A3-08). What survives is an internal contradiction about the status. Line rv L344 says "Human ruling stands (27-Aug framework: 'SUBSTANTIALLY CLEARED in spirit')". Lines rv L349 and rv L911 say the ruling is open: "whether the LoI plus partial POs count as 'confirmed'". Triggers 6D and 8A (rv L355, L813) label it "FIRED" with no qualifier.
- Result: SURVIVES as CONTRADICTION C1. Graft: one status in every cell, for example "FIRED on LoI under the 27-Aug ruling; PO value undisclosed (CL355); operator to reconfirm on PO evidence". Align rv L344, L349, L355, L399, L813, L911 and flag rv L1017.

### Claim 2: Net-debt thesis-broken "NOT FIRED on the definition on file; headroom 115.61" (rv L343, L403, L906)
- Strongest bear counter (run-rate, from the extract): Q2 net debt rose 107.39 (4,277 to 4,384.39, PL169, RL613-635). The headroom is 115.61, so a breach needs only 1.08x the Q2 rise. At the Q2 pace, Q3 lands at 4,491.78, leaving 8.22 of headroom. At the H1 average pace (853.72 / 2 = 426.86 a quarter), Q3 lands at 4,811.25, a breach by 311.25. H1 free cash flow averaged (354.56) a quarter (RL700-703), 3.07x the headroom. The Q2 pace was itself helped by a 190 fall in net-of-advance receivables (2,232 to 2,042, PL166); without that release the Q2 rise would have been about 297 [INFERENCE]. Management says inventory turns into receivables before cash (CL522-523), and that capex "as per the plan" and "operational costs" still draw on debt (CL140-141).
- Does it survive? Yes. A4 says "closer" (rv L837) and sets the Q3 bear line at "above Rs 4,500 Cr" (rv L403), but gives no run-rate. The extract shows that on the H1 pace the breach is the base case unless BSNL cash arrives in Q3.
- Result: SURVIVES as MISSING M3. Graft into Step 6C (rv L343), 8C (rv L403) and the forward-map make-or-break line (rv L937): the Q2-pace and H1-pace Q3 figures, and the note that the Q2 pace already includes a 190 receivable release.

### Claim 3: Trigger 2 BharatNet "ON TRACK" and Trigger 5 DCI "ON TRACK (unquantified, low confidence)" (rv L356, L359, L814, L817)
- Strongest bear counter: The BharatNet evidence is a letter of intent, not a PO. It comes from "a new SI partner" for routers "in 3 states", with no value (CL157-159; PL185-187). The DCI evidence is one sentence, "we are indeed winning several business in this area" (CL476). The analyst asked for orders "in range or a quantum" (CL458-460), and none was given. A4 grades that answer C (rv L645). A4's own concall rule says to discount management commentary by 30-50% at a 55.0% credibility ratio (rv L849). An ungraded, unvalued sentence from a management team A4 classes EVASIVE (rv L766) cannot tell ON TRACK from UNCHANGED.
- Does it survive? Yes, for DCI fully and for BharatNet in part. Both labels lack the evidence tier, the bar Rule J sets for bull and bear claims alike.
- Result: SURVIVES as MISSING M4. Graft: DCI to "UNVERIFIED (no count or value; C-graded answer, CL476)". BharatNet to "ON TRACK at LOI stage, unvalued (CL157-159)".

### Other positive claims tested (counter already in A4; no graft)
- Q2 FY26 charge is non-recurring (rv L213; Q10 graded A, rv L648). Counter: the loss came from "contract manufacturing process losses, design changes" (RL378-379) on "the first 100,000 site order" (CL498-499). The add-on ships from inventory built for it and "carrying for a while" (CL292-293), with inventory at 831.8 days. A4 already carries this risk at Q8 (rv L418) and 7A "PARTIALLY CONFIRMED" (rv L783). Not a new graft.
- Auditor opinion CLEAN (rv L61). Counter: a limited review gives "moderate assurance" only (RL96-102), and 3 subsidiaries were not reviewed (RL496-505). A4 already holds the DTA and IAUD tests for the FY27 audit (rv L945). Not a new graft.

### Further findings from the adversarial pass (same-extract checks on A4's own reasoning)
- FACTUAL F3 (A4): forex is refuted as the cause of the +62.99 QoQ other-expense rise. A4 says the deck's "Net forex loss" "may sit in other expenses" (rv L197), and Q21 offers "Forex one-off" as the bull answer (rv L431). The deck defines EBIT as "PBT - Other Income + Finance Cost including Net forex loss" (PL119, PL139) and shows EBIT (199) for Q2 and (194) for Q1 (PL132). The filing-derived operating EBIT is (198.12) and (194.71) (rv L162; RL536-548). So net forex in operating costs is about -0.9 (a gain) in Q2 and +0.7 in Q1, within the deck's +/-0.5 rounding. It is under about 1.4 Cr each quarter and moved toward a gain. Forex cannot explain a 63 Cr rise. The step-up has no stated cause and may recur, which strengthens A4's bear read. Fix rv L197, Q21 (rv L431) and the flag at rv L1026.
- MISSING M2 (A4): the Q1 FY27 comparators are omitted, so the period test is mismatched. The deck gives net-of-advance trade receivables of 1,905 / 2,232 / 2,042 (PL166) and NWC of 4,138 / 4,478 / 4,235 (PL163). A4 uses only Mar-26 to Sep-26 (+137, rv L249) and calls management's claim "materially misleading" (rv L779). Management's claim is QoQ: "the net working capital compared to Q1 FY27 is lower ... on account of increased collections" (CL128-132). On the deck's QoQ numbers, net-of-advance receivables fell 190 (-8.5%) and NWC fell 243 in Q2. The QoQ claim is CONFIRMED (PL163-166). The H1 reading also holds: receivables up 137, NWC up 97, CFO (311.93). A4's "NEW Gate 5", "net-of-advance trade receivables fall QoQ from 2,042" (rv L399), was already met in Q2 against Q1. Fix: show both periods in the Step 5 table (rv L249), 7A (rv L779), Gate 5 (rv L399) and the brief (rv L905, L938).
- CONTRADICTION C2 (A4): the break-even uses a cost base that A4 itself calls distorted. Step 3 says Q2 is distorted by 46.50 of estimate releases against Q1 rates (rv L199, L203). Section C then holds "Q2 cost base held constant" (rv L879). The brief calls 261.73 "fixed costs near Rs 262 Cr" (rv L927), yet that figure includes an ECL write-back of (10.55), which is a credit, not a fixed cost, and a warranty charge of 7.24 against 35.11 in Q1. On Q1 estimate rates the base is 308.23. Break-even is then about 806 a quarter for op EBITDA and about 1,252 for PBT, against A4's 685 and 1,130. Fix: show both and call 685 / 1,130 the flattered floor.
- FACTUAL F1 (A4): "one PSU customer through one contractor (TCS) dominates the book [MGMT, PL187, PL90]" (rv L934) goes beyond the extract. Management says BSNL is "a substantial portion" (CL357). PL90 gives India at 96%, not BSNL's share. PL187 gives the LoI only. The BSNL value in the book is refused (CL355). Fix: "BSNL is a substantial portion of the book (CL357); the share is not disclosed (CL355)".

---

## FINDINGS BY TYPE

| ID | Type | Loop | Finding | Anchor |
|---|---|---|---|---|
| M1 | MISSING | A2 | Fresh fulltext units with no structured row and no ledger row: results RL159, RL170, RL338, RL715 (161.22 non-current repayment, material), RL488-494 (cons review conclusion); concall CL516-517, CL590-591 (hedges), CL524-526 (collections forward phrase). Line items 242 vs 238; auditor paragraphs 12 vs 11; concall forward 65 vs 64, hedges 39 vs 37 | Audit 1 |
| M2 | MISSING | A4 | Q1 FY27 comparators omitted (net-of-advance receivables 2,232, NWC 4,478); QoQ -190 / -243 confirms management's QoQ collections claim; 7A verdict and Gate 5 rest on H1 data only | PL163-166; CL128-132; rv L249, L399, L779 |
| M3 | MISSING | A4 | Surviving bear counter, net debt: breach needs 1.08x the Q2 rise; Q3 at Q2 pace 4,491.78, at H1 pace 4,811.25; Q2 pace helped by a 190 receivable release | PL166, PL169, RL613-635, RL700-703, CL522-523; rv L343, L403, L937 |
| M4 | MISSING | A4 | Surviving bear counter, triggers: DCI ON TRACK rests on one C-graded unquantified sentence; BharatNet ON TRACK on an unvalued LOI | CL157-159, CL458-476; rv L356, L359, L645, L849 |
| C1 | CONTRADICTION | A4 | BSNL ruling "stands" (rv L344) vs "open" (rv L349, L911) while trigger 1 is labelled "FIRED" (rv L355, L813); deck shows LoI only | PL69, PL93, PL187; CL97-98, CL346-358 |
| C2 | CONTRADICTION | A4 | Break-even (685 / 1,130) and "fixed costs near Rs 262 Cr" use the Q2 base A4 calls distorted by 46.50 of estimate releases; on Q1 rates 806 / 1,252 | rv L199, L203, L879, L927; RL545, RL546, RL802 |
| F1 | FACTUAL | A4 | "dominates the book" not supported; extract says "a substantial portion" | CL355-358; PL90, PL187; rv L934 |
| F2 | FACTUAL | A4 | Mar-26 receivable days use OCR-suspect non-current receivable 4.33 (subtotal RL609 fails by 4.00; std RL223 by 1.00); 1,077.5 vs 1,078.8 days, CCC 2,010.3 vs 2,011.6; label OCR and show the range | RL597-609, RL218-223; rv L248, L252 |
| F3 | FACTUAL | A4 | Forex as the cause of the +62.99 other-expense rise is refuted by the deck EBIT bridge (net forex under about 1.4 Cr a quarter); remove the forex inference and the "Forex one-off" bull answer | PL119, PL132, PL139; rv L162, L197, L431, L1026 |

---

## STYLE NOTES (logged; no re-run)

- S1: Brief rv L905 tags "customer advances fell Rs 1,266.3 Cr" as [FILED]. The filed line is "other liabilities" (RL642, RL697). The "customer advances" label is an INFERENCE from the deck's net-of-advance basis (PL164-166). Implied advances fall from about 1,351 at Mar-26 to about 103 at Sep-26, so the inference holds. Retag as "[FILED amount; label INFERENCE, PL164-166]".
- S2: Step 4 run-rate (rv L235) uses a 25.17% credit rate with no source. The Q2 consolidated rate is 25.26% (rv L130), which gives (241.7) against A4's (242.0).
- S3: rv L79 cites Q2 FY26 other operating revenue of 5.15 to RL534, which reads "5.5". The value is right by identity (261.82 - 256.67). Label it "derived by identity".
- S4: Forward map rv L947-949 has three undated catalysts. They are labelled honestly ("Undated", "Any board outcome"), which is the correct NOT DISCLOSED treatment. Note only.
- S5: rv L932 tags the competitor names (Nokia, Ericsson, Samsung, Ciena, HFCL, ITI) SECONDARY with no named source. Retag as INFERENCE (general knowledge, not verified this run), or name the source.
- S6: The A4 YAML key "ledger_reconciliation.notes: 851" counts all results rows, not the 12 notes. Rename the key to rows.
- S7: Receivable days (rv L248) mix trailing FY26 revenue (a trough year) with annualised H1 revenue. Part of the -591 day improvement is a denominator effect. Say so in the row.
- S8: Q06 (rv L644) is graded B. The TCS data-centre POC half of T19 (CL427-428) got only an implicit answer ("working with the system integrators", CL442). Note the half-answer.

A5 position on A4's DROPPED-count request (rv L592): concur with A4, count 1. The Q1 change gave a new window (a re-date); the Q2 change gave none (a drop). The Q1 evidence sits in the Notion digest, outside A5's inputs, so the operator holds the final call.

---

## VERDICT

VERDICT: INCOMPLETE.
- Failing agents: A2 (M1) and A4 (M2, M3, M4, C1, C2, F1, F2, F3).
- loop_back_to: A2, the earliest failing agent. The A2 fix is ledger-only and adds one material row (RL715). The A3 pass that follows needs to review only the new rows. All eight A4 items can be fixed in the single A4 pass that follows. None of them moves the protocol verdict PROCEED WITH FLAGS (rv L881).
- Finding types: MISSING 4, CONTRADICTION 2, FACTUAL 3, STYLE 8.
- Gates: deliverable-completeness PASS; orphan rows none; arithmetic one low-severity FACTUAL (F2); three surviving bear counters to graft (C1, M3, M4).

---

```yaml
stage: A5-adversary
company: "TEJASNET"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
  forward_map: present
coverage:
  orphan_rows: []
  missing_from_ledger:
    - "results RL159 std P&L current tax line (dash/OCR noise), no structured row"
    - "results RL170 std P&L OCI income tax on reclassifiable items (dash), no structured row"
    - "results RL338 std cash flow Other finance cost, OCR '10.99)'; (0.99) H1 FY27 / (0.89) H1 FY26 by identity to RL339"
    - "results RL715 cons cash flow Repayment of borrowings non-current (161.22); identity RL712-726 confirms (material)"
    - "results RL488-494 cons review report para 5 unmodified conclusion, no QUALIFIER row"
    - "concall CL516-517 hedge 'That's all I can say'"
    - "concall CL590-591 hedge 'That's about all I can say. I cannot comment on the revenue numbers'"
    - "concall CL524-526 forward 'significant amount is going to come in' (collections)"
arithmetic_mismatches:
  - {metric: "Receivable days Mar-26 (and CCC Mar-26)", a4_value: "1,078.8 days on 3,260.78 (CCC 2,011.6)", recomputed: "1,077.5 days on 3,256.78 if RL604 4.33 is OCR for 0.33 (CCC 2,010.3); subtotal RL609 fails by 4.00, std RL223 by 1.00", source_line: "RL597-609, RL614, RL218-223; rv L248, L252"}
surviving_bear_counters:
  - {claim: "BSNL add-on trigger FIRED; Gate 1 met; thesis-broken NOT FIRED (rv L344, L355, L813)", counter: "Deck states LoI only (PL69, PL93, PL187); POs spoken only and partial (CL97-98, CL346-350); BSNL value in book refused (CL355); implied Q2 inflow ~1,192 includes non-BSNL wins; A4 text calls the ruling both 'stands' (rv L344) and 'open' (rv L349, L911)", source_line: "PL187; CL346-358; rv L344, L349, L911", type: CONTRADICTION}
  - {claim: "Net-debt thesis-broken NOT FIRED, headroom 115.61 (rv L343, L403)", counter: "Breach needs 1.08x the Q2 rise of 107.39; Q3 at Q2 pace 4,491.78, at H1 pace 4,811.25; H1 FCF (354.56)/qtr = 3.07x headroom; Q2 pace helped by a 190 fall in net-of-advance receivables", source_line: "PL166, PL169; RL613-635; RL700-703; CL522-523", type: MISSING}
  - {claim: "Trigger 2 BharatNet and Trigger 5 DCI ON TRACK (rv L356, L359)", counter: "BharatNet rests on an unvalued SI LOI for 3 states; DCI on one C-graded unquantified sentence while A4's own rule discounts commentary 30-50% at 55.0% credibility", source_line: "CL157-159; CL458-476; rv L645, L849", type: MISSING}
findings_by_type:
  factual:
    - "F1 (A4): rv L934 'TCS dominates the book' unsupported; extract says 'a substantial portion' (CL357), share undisclosed (CL355)"
    - "F2 (A4): Mar-26 receivable days use OCR-suspect non-current receivable 4.33 (RL604; RL609 subtotal fails by 4.00); label OCR, show 1,077.5-1,078.8"
    - "F3 (A4): forex refuted as cause of +62.99 QoQ other-expense rise; deck EBIT (199)/(194) vs derived (198.12)/(194.71) caps net forex under ~1.4 Cr/qtr (PL119, PL132); fix rv L197, Q21 rv L431, flag rv L1026"
  missing:
    - "M1 (A2): 8 fresh-pass units lack structured and ledger rows (RL159, RL170, RL338, RL715, RL488-494, CL516-517, CL524-526, CL590-591)"
    - "M2 (A4): Q1 FY27 comparators omitted (PL163 NWC 4,478; PL166 net-of-advance receivables 2,232); QoQ -243 / -190 confirms the QoQ collections claim (CL128-132); fix rv L249, L399, L779, L905, L938"
    - "M3 (A4): net-debt run-rate counter (Q3 4,491.78 at Q2 pace, 4,811.25 at H1 pace) absent; graft rv L343, L403, L937"
    - "M4 (A4): DCI and BharatNet ON TRACK lack evidence tier; DCI to UNVERIFIED, BharatNet to ON TRACK at LOI stage, unvalued"
  contradiction:
    - "C1 (A4): BSNL ruling 'stands' (rv L344) vs 'open' (rv L349, L911) while trigger 1 labelled FIRED (rv L355, L813); one status everywhere"
    - "C2 (A4): break-even 685/1,130 and 'fixed costs ~262' use the Q2 base A4 calls distorted by 46.50 of estimate releases (rv L199, L203); on Q1 rates 806/1,252; fix rv L879, L927"
  style:
    - "S1: rv L905 'customer advances' tagged FILED; filed label is 'other liabilities' (RL697); retag label INFERENCE (PL164-166)"
    - "S2: rv L235 25.17% credit rate unsourced; Q2 rate 25.26% gives (241.7)"
    - "S3: rv L79 5.15 cited to RL534 which reads '5.5'; label derived by identity"
    - "S4: forward map rv L947-949 three undated catalysts, honestly labelled; note only"
    - "S5: rv L932 competitor names tagged SECONDARY without a source; retag INFERENCE or name source"
    - "S6: A4 YAML ledger_reconciliation.notes: 851 counts rows, not notes"
    - "S7: rv L248 receivable-days improvement partly a denominator effect (trough FY26 vs annualised H1); say so"
    - "S8: rv L644 Q06 graded B; TCS data-centre POC half (CL427-428) answered only implicitly (CL442)"
loop_back_to: "A2"
gap: "A2: add ledger rows (and route structured rows to A1) for RL159, RL170, RL338, RL715 (161.22 non-current repayment), RL488-494, CL516-517, CL524-526, CL590-591; add a fulltext-vs-structured count to the count test. Then A4 (after A3 reviews the new rows): C1 one BSNL trigger/ruling status across rv L344/L349/L355/L813/L911; C2 restate break-even on Q1 estimate rates (~806 EBITDA, ~1,252 PBT) and drop 'fixed costs' label for the ECL credit; M2 add Q1 FY27 comparators PL163/PL166 and split the 7A collections verdict QoQ vs H1, revisit Gate 5; M3 graft net-debt run-rate (Q3 4,491.78 / 4,811.25); M4 DCI to UNVERIFIED, BharatNet to LOI-stage unvalued; F1 replace 'dominates' with 'substantial portion (CL357)'; F2 label RL604 OCR-suspect, show 1,077.5-1,078.8 days; F3 remove forex as the other-expense explanation (PL132 vs derived EBIT) and reframe Q21."
style_notes:
  - "S1 provenance retag rv L905"
  - "S2 unsourced 25.17% rate rv L235"
  - "S3 identity label rv L79"
  - "S4 undated forward-map items honestly labelled"
  - "S5 SECONDARY tag without source rv L932"
  - "S6 YAML key notes: 851"
  - "S7 receivable-days denominator effect rv L248"
  - "S8 Q06 half-answer rv L644"
analyst_note: "Loop goes to A2 because it is the earliest failing agent. The A2 fix is ledger-only and adds one material row, RL715 (161.22 non-current repayment). A3 then needs to review only the new rows. All eight A4 items fit in one A4 pass, and none moves the PROCEED WITH FLAGS verdict. Two findings cut against A4's bear lean, under the same-bar rule. First, the deck's own Q1 comparator shows net-of-advance receivables fell 190 in Q2, so management's QoQ collections claim holds, while A4's H1 reading also holds. Second, the deck EBIT bridge rules out forex as the cause of the 63 Cr other-expense rise, so the rise has no stated cause and may recur. The net-debt run-rate counter matters most. One more quarter at Q2's 107 Cr pace would use 107 of the 116 Cr headroom, and even that pace was helped by a 190 Cr receivable release. On the DROPPED count A5 concurs with A4 (count 1), but the Q1 evidence sits in the digest, outside A5's inputs."
```
