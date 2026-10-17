# A5 ADVERSARY / COMPLETENESS AUDIT: PREMIER POLYFILM LIMITED (PREMIERPOL), Q2 FY27 (loop 2)

Auditor: A5, claude-opus-5-5, fresh context. Date 2026-10-17.
Inputs read: A4 review `runs/premierpol-q2fy27/work/review_premierpol_q2fy27.md` (664 lines, loop 2); A1 fulltext `extracted/premierpol-results-q2fy27-fulltext.md` (body L1 to L522); A1 structured `extracted/premierpol-results-q2fy27-structured.md` (R001 to R401); A2 ledger `work/ledger_results_premierpol_q2fy27.md` (loop 1, incl. section 10A X001 to X012). I did not open the source PDF, anything under `inputs/`, A3's notes or the earlier A5 audits.
Anchors: "L###" = A1 fulltext body line. "rev L###" = line in the A4 review file. "R###" = A1 structured row. "X###" = A2 ledger-only row. All figures in Rs lakhs unless stated as Cr.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: narrative PRESENT, sector PRESENT, business model PRESENT, competition PRESENT, forward map PRESENT. Gate PASSES.

| Brief part | Heading (rev line) | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | rev L541 | 16 lines (rev L542 to L557), inside the 10 to 20 line band. Real content: revenue, margin, cash, debt, decision framing. | present |
| 2. Sector intelligence | rev L559 | 6 bullets (rev L560 to L565): products, resin input, demand drivers, trade policy, GST share trend, disclosure gaps. | present |
| 3. Business-model intelligence | rev L567 | 6 bullets (rev L568 to L573): conversion model, unit economics, cost leverage, capital intensity, three readings, working capital. | present |
| 4. Competition intelligence | rev L575 | 5 bullets (rev L576 to L580): peer prior (flagged INFERENCE), strengths, weaknesses, competitive risk, gaps. | present |
| 5. Forward map | rev L582 | Make-or-break reading plus 8 dated items (rev L583 to L591), each with a bull fork and a bear fork. | present |

---

## 1. COVERAGE AUDIT

Method. I ran a fresh pass over every numbered body line of the fulltext. I listed each line that carries a value token, each dash or glyph cell, each blank labelled row, each note, entity, date, identifier, agenda item and auditor paragraph. I then diffed that list against the structured file and the ledger. Last, I checked each ledger row for a citation or a disposition in the A4 review.

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes (numbered) | 5 (+1 unnumbered R384) | 5 (L152, L153, L155, L157, L158) +1 (L165) | none | PASS |
| Line items, value-bearing | 105 (96 structured + 9 X-rows) | 105 (P&L 23 + p3 10 + CF 21 + BS 42 structured; X001, X003, X005, X006, X007, X009, X010, X011, X012) | none | PASS |
| Value cells | 337 (310 + 27) | 337 | none | PASS |
| Zero-standing cells | 49 (23 + 26) | 49 (R097, R111 to R116, 8 BS pairs; X001 2, X003 1, X004 1, X005 5, X006 6, X007 5, X009 2, X010 1, X011 2, X012 1) | none | PASS |
| Qualifiers | 42 (40 + X002, X008) | 42 under A2's unit. Blank template rows outside R390's L192 to L223 scope have no covering row (L141 to L143, L226 to L228, L230, L233 to L267, L274 to L289, L293 to L295). | none | PASS, STYLE S-20 |
| Footnote markers unresolved | 4 | 4 (L37, L95, L131, L521) | none | PASS |
| Agenda items | 1 | 1 (L25 to L30) | none | PASS |
| Auditor paragraphs | 5 | 5 (title L428, para 1 L451, para 2 L461, para 3 L477, conclusion L490). Para 1 has no own row; R396 "title/scope" carries it. | none | PASS, STYLE S-26 |
| Entities | 23 | 23 (R320 to R342) | none | PASS |
| Dates | 19 | 19 (L10, L18, L25, L28, L35, L71 x4, L152, L172, L179, L182, L307, L312, L315, L408, L435, L516) | none | PASS |
| Identifiers | 9 | 9 (R311 to R319). DIN repeats at L308 and L412 equal R317. Auditor phone and address L416 to L419 are entity detail, not material. | none | PASS |
| Turns / questions / slides | 0 | 0 (results-only run) | n/a | n/a |
| Ledger IDs | 413 (R001 to R401 + X001 to X012) | 413 | none | PASS |

Orphan check. The A4 preamble (rev L41) states "Ledger rows reviewed: 413 of 413" with category counts that match mine. The flagged rows carry row-level dispositions (rev L46 to L59). Every line item is cited by line anchor. So no ledger row is an orphan in form.

One substantive gap sits inside a cited line. L271 carries two cells: R213 (455.00), H1 FY27, and R214 (1,920.00), FY26. A4 cites L271 and analyses R213 at length (rev L274, L310 to L313). R214 appears nowhere in the review (grep "1,920", "1920", "19.20": no match). It is the largest undescribed cash movement in the filing. I raise it as a MISSING finding against A4 (A5-M7, section 3), not as an orphan, because the line is cited and the row is inside the blanket review.

Missing from ledger: none that carry a value or a dash cell. The blank template rows are logged as STYLE (S-20). They carry no value. A4 cites four of them (L276, L278, L282, L286) and treats them correctly for H1 FY27 (financing casts: 147 + 32 = 179, L283, L287, L290). Investing casts in both columns on its visible lines (FY26: 4 - 895 + 4 + 48 - 1,920 = -2,759; H1 FY27: 1 - 581 + 2 + 76 - 455 = -957; L244, L245, L268, L269, L271, L272).

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed by hand from the raw lakh cells. Rounding tolerance: 0.01 Cr, 0.01 pp, 1 bp on rounded inputs.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| P&L casts, six columns (total expenses, PBT, tax, PAT, TCI) | tie | All tie. Q2 FY27: 6,843 + 217 - 78 + 888 + 24 + 118 + 2,295 = 10,307; 11,618 - 10,307 = 1,311; 1,311 - 330 = 981; 981 - 218 = 763 | L77 to L110 | PASS |
| H1 = Q1 + Q2 FY27 (revenue, OOI, CoMC, purchases, change in inventories, employee, GST, other, PBT, tax, PAT, OCI) | implied | All tie (e.g. 10,006 + 11,506 = 21,512; 143 - 78 = 65; 384 - 218 = 166) | L75 to L109 | PASS |
| H1 FY27 finance cost (R046 "At") | 0.44 | 19,158 - (11,804 + 921 + 65 + 1,708 + 236 + 4,380) = 44; also 20 + 24 = 44 | L84, L92 | PASS |
| Net revenue Q2 FY26 / Q1 FY27 / Q2 FY27 / H1 FY26 / H1 FY27 / FY26 | 72.64 / 87.33 / 101.43 / 137.20 / 188.76 / 296.58 | 8,317-1,053; 10,006-1,273; 11,506-1,363; 15,761-2,041; 21,512-2,636; 33,890-4,232 = same | L75, L87 | PASS |
| Material cost (six columns) | 45.55 / 58.08 / 69.82 / 86.07 / 127.90 / 186.22 | 4,555 / 5,808 / 6,982 / 8,607 / 12,790 / 18,622 | L80 to L82 | PASS |
| Gross margin on net revenue | 37.29 / 33.49 / 31.16 / 37.27 / 32.24 / 37.21% | 37.294 / 33.494 / 31.164 / 37.267 / 32.242 / 37.211% | L75, L80 to L82, L87 | PASS |
| Operating EBITDA (PBT + D + FC - OI) | 11.33 / 12.93 / 13.41 / 20.45 / 26.34 / 45.94 | 1,133 / 1,293 / 1,341 / 2,045 / 2,634 / 4,594 | L76, L84, L85, L95 | PASS |
| Op EBITDA margin, net revenue | 15.60 / 14.81 / 13.22 / 14.91 / 13.95 / 15.49% | 15.597 / 14.806 / 13.221 / 14.905 / 13.954 / 15.490% | same | PASS |
| Op EBITDA margin, reported revenue | 13.62 / 12.92 / 11.65 / 12.98 / 12.24 / 13.56% | 13.623 / 12.922 / 11.655 / 12.975 / 12.244 / 13.556% | L75 | PASS |
| Reported EBITDA and margin on net revenue | 12.29 to 48.30; 16.92 / 15.48 / 14.33 / 15.99 / 14.86 / 16.29% | 1,229 / 1,352 / 1,453 / 2,194 / 2,805 / 4,830; 16.919 / 15.481 / 14.325 / 15.991 / 14.860 / 16.286% | L84, L85, L95 | PASS |
| Core PBT (PBT - OI) | 10.04 / 11.55 / 11.99 / 17.75 / 23.54 / 40.44 | 1,004 / 1,155 / 1,199 / 1,775 / 2,354 / 4,044 | L76, L95 | PASS |
| OI / PBT | 8.73 / 4.86 / 8.54 / 7.74 / 6.77 / 5.51% | 8.727 / 4.860 / 8.543 / 7.744 / 6.772 / 5.514% | L76, L95 | PASS |
| ETR | 27.18 / 25.21 / 25.17 / 27.18 / 25.19 / 25.51% | 27.182 / 25.206 / 25.172 / 27.183 / 25.188 / 25.514% | L95, L99 | PASS |
| PAT margin, net / reported | 11.03 / 10.40 / 9.67 / 10.21 / 10.01 / 10.75%; 9.63 / 9.07 / 8.53 / 8.89 / 8.78 / 9.41% | 11.027 / 10.397 / 9.672 / 10.211 / 10.007 / 10.749%; 9.631 / 9.075 / 8.526 / 8.889 / 8.781 / 9.407% | L75, L87, L108 | PASS |
| GST / reported revenue | 12.66 / 12.72 / 11.85 / 12.95 / 12.25 / 12.49% | 12.661 / 12.722 / 11.846 / 12.950 / 12.254 / 12.487% | L75, L87 | PASS |
| A3 F-09 basis note | 14.2% vs 16.7% | 1,453 / 10,255 = 14.17%; 1,229 / 7,360 = 16.70% | L77, L87 | PASS |
| YoY: net revenue / reported revenue / gross profit | +39.63% / +38.34% / +16.69% | 2,879/7,264 = 39.634%; 3,189/8,317 = 38.343%; 452/2,709 = 16.685% | L75, L80 to L82, L87 | PASS |
| YoY: GM / Op EBITDA margin | -613 bps / -238 bps | -6.129 pp / -2.376 pp | same | PASS |
| YoY: conversion costs / Op EBITDA / EBIT / core PBT / PBT / PAT / EPS | +15.48 / +18.36 / +20.26 / +19.42 / +19.18 / +22.47 / +23.68% | 244/1,576; 208/1,133; 206/1,017; 195/1,004; 211/1,100; 180/801; 0.18/0.76 = same | L83, L85, L88, L95, L108, L139 | PASS |
| Opex ratio and offset | 21.70% to 17.94%, +375 bps; -613 + 375 = -238 | 1,576/7,264 = 21.696%; 1,820/10,143 = 17.943%; 375 bps | L83, L88 | PASS |
| QoQ Op EBITDA margin | -159 bps | 14.806 - 13.221 = 1.585 pp | same | PASS |
| H1 YoY set | +37.58 / +28.80% / -95 bps / +32.62 / +31.24 / +34.83 / +34.33% | 5,156/13,720; 589/2,045; 14.905 to 13.954; 579/1,775; 601/1,924; 488/1,401; 0.46/1.34 = same | L75 to L139 | PASS |
| Traded-goods share of material cost | 3.11 / 12.12 / 4.72%; H1 +133.76% | 217/6,982; 704/5,808; 215/4,555; 921/394 = same | L81 | PASS |
| Other expenses QoQ vs revenue | +14.78% vs +16.15%; +1.37% vs +20.22% | 120/812; 1,410/8,733; 11/801; 1,469/7,264 = same | L88 | PASS |
| Q1 FY26 derived (net revenue, GM, Op EBITDA margin, core PBT) | 64.56 / 37.24% / 14.13% / 7.71 | 6,456; 2,404/6,456 = 37.237%; 912/6,456 = 14.126%; 771 | L75 to L95 (H1 FY26 less Q2 FY26) | PASS |
| H2 FY26 derived (net revenue, GM, Op EBITDA margin, core PBT) | 159.38 / 37.16% / 15.99% / 22.69 | 15,938; 5,923/15,938 = 37.163%; 2,549/15,938 = 15.993%; 2,269 | FY26 less H1 FY26 | PASS |
| Run-rates | +12.52 / +9.71 / +9.59 / +16.15%; core PBT QoQ +3.81% | 7,264/6,456; 7,969/7,264; 8,733/7,969; 10,143/8,733; 1,199/1,155 = same | derived | PASS |
| PAT bridge: revenue contribution / GM change | +1,074 / -622 | 2,879 x 0.372935 = 1,073.7; 10,143 x -0.061292 = -621.7; sum 452 = gross profit change | L75 to L87 | PASS |
| PAT bridge: tax at prior ETR / ETR change / total | -57 / +26 (26.35) / +180 | 211 x 0.271818 = 57.4; 1,311 x 0.020102 = 26.35; 211 x 0.728182 + 26.35 = 180.0 | L95, L99, L108 | PASS |
| Bridge shares and recurring split | 596.7 / -345.6 / ... / 117.2%; 78.9 / 6.5 / 14.6% | 1,074/180 etc.; 195 x 0.728182 = 142.0 (78.9%); 16 x 0.728182 = 11.7 (6.5%); 26.35 (14.6%) | derived | PASS |
| PAT with OI and ETR reverted | 9.43 Cr, +17.73% | 1,295 x 0.728182 = 943.0; 943/801 = 1.1773 | derived | PASS |
| CFO cast (H1 FY27) | 1,799 / 1,322 / 186 / 690 | 2,525 - 726; 1,799 - 477; 1,322 - 957 - 179; 504 + 186 | L189, L224 to L231, L272, L290, L292, L296, L298 | PASS |
| FY26 CFO by cast | 26.70 | -581 + 2,759 + 492 = 2,670 | L272, L290, L292 | PASS |
| CFO / PAT | 0.70x / 0.84x | 1,322/1,889 = 0.700; 2,670/3,188 = 0.838 | L108, L231 | PASS |
| FCF (CFO less PPE purchase) | 17.75 / 7.41 / 2.86 | 1,775 / 741 / 286 | L245, L271 | PASS (arithmetic). FY26 qualifier missing, see A5-M7 |
| Capex H1 vs FY26 | 65% | 581/895 = 64.9% | L245 | PASS |
| Trade WC | 70.79 to 71.06 | 5,027 + 4,126 - 2,074 = 7,079; 5,029 + 3,964 - 1,887 = 7,106 | L339, L342, L383 | PASS |
| Trade WC + OCA; wider bound | 78.14 to 84.31 (+7.90%); 90.00 to 100.17 (+11.30%) | 7,814 / 8,431 / 617/7,814 = 7.896%; 9,000 / 10,017 / 11.30% | L346, L349 | PASS |
| Day counts, mixed basis | 44.44 to 33.72; 98.53 to 71.96; 40.65 to 27.00; CCC 102.32 to 78.68 | 4,126/33,890x365; 3,964/21,512x183; 5,027/18,622x365; 5,029/12,790x183; 2,074/18,622x365; 1,887/12,790x183 = same | L339, L342, L383 | PASS |
| Receivable days on net revenue | 50.78 to 38.43 | 4,126/29,658x365; 3,964/18,876x183 = same | same | PASS |
| Day counts, like-for-like (H2 FY26 182 days) | 41.42 / 91.35 / 37.69; CCC 95.08 to 78.68, -16.40; about 30% smaller | 4,126/18,129x182; 5,027/10,015x182; 2,074/10,015x182 = same; 16.40/23.64 = 0.694 | L75, Step 3 | PASS |
| Half-on-half net revenue | +18.43% | 18,876/15,938 = 1.1843 | derived | PASS |
| Net cash, BS basis | 16.68 to 19.36 | 504 + 1,164; 690 + 1,246 | L341, L343 | PASS |
| D/E-implied debt and net debt (Reading 2) | 18.40 to 19.87; 17.61 to 19.29; 1.72 to 3.19; (0.07) to (1.75) | 0.125/0.135 x 14,720; 0.105/0.115 x 16,775; less 1,668 / 1,936 = same | L147, L364 | PASS |
| Reading 3, cash only | 13.36 to 14.83 (0.09 to 0.10x); 10.71 to 12.39 (0.06 to 0.07x); down 2.44 to 2.65 | 1,840 - 504; 1,987 - 504; 1,761 - 690; 1,929 - 690; ratios on 14,720 / 16,775 = same | L147, L343, L364 | PASS |
| FY26 base effect | 22.51 Cr; 70.6% of PAT; 2,297 (+80%); 3,198 (+57%); 3,704 (+11%) | 1,829 + 422 = 2,251; 2,251/3,188 = 70.6%; 4,126 - 1,829; 5,027 - 1,829; 4,126 - 422 = same | L194, L196, L339, L342 | PASS (arithmetic). Composition claim, see A5-F3 |
| OCA reconciliation | 494; hidden +167; identifiable +60; residual +107 / +507; 94 unexplained | 1,084 - 590; -726 - (-893); 236 - 187 + 127 + 56 - 94 - 78; 167 - 60; 167 - 60 + 400; 1,084 - 990 | L191 to L224, L346, L349, L374, L383 to L388 | PASS (see S-21 on the OCFL input) |
| Capitalisation bridge | X = 234; 234 + 347 = 581 | 6,009 - 6,011 + 236 = 234; 397 - 50 = 347 | L85, L245, L320, L321 | PASS |
| Investing readings | A: 480 vs 455; B: 174 vs OCI 166 | 579 - 99; (1,246 - 1,164) + (1,077 - 985) | L109, L330, L336, L341 | PASS (see S-22) |
| FC add-back gap | 12 lakh H1; 57 vs 81 FY26 | 44 - 32; 81 - 57 = 24 | L84, L191 | PASS |
| EPS share basis | about 1,044 (1,038 to 1,049); intersection 1,047 to 1,049; 5 of 6 above PAT/1,059 | 981/0.94; 981/0.945, 981/0.935; max lower bound 801/0.765 = 1,047.1, min upper 981/0.935 = 1,049.2; Q2 FY26 0.756 rounds to 0.76 (equal) | L102, L126, L139 | PASS |
| Treasury share of OOI | 78/171 = 45.6%; alternative lift 93 | same | L76, L268, L269 | PASS |
| FY26 non-TCI equity reduction | 158 lakh; about Rs 0.15 per share | 10,728 + 3,091 - 13,661 = 158; 158/1,059 = 0.149 | L110, L130, L361 | PASS |
| ROCE H1 FY27 BS / with debt | 32.63% / 29.15% | 5,138 / 15,747.5 = 32.63%; 5,138 / 17,627 = 29.15% | L84, L95, L147, L364 | PASS |
| ROCE FY26 | 32.90% | 4,361 / 13,253.5 = 32.90% (opening equity 10,728 + 1,059) | L84, L95, L126, L130, L364 | PASS |
| A21 run-rate | 39.24 annualised; TTM PAT 36.76, net revenue 348.14, EPS 3.50 | 981x4; 3,188 - 1,401 + 1,889; 29,658 - 13,720 + 18,876; 3.04 - 1.34 + 1.80 | L75, L87, L108, L139 | PASS |
| Material cost share | 68.84% vs 62.71% | 6,982/10,143; 4,555/7,264 | derived | PASS |
| GST share history | 13.27% (Q1 FY26), 12.09% (H2 FY26) | 988/7,444; 2,191/18,129 | L75, L87 | PASS |
| BS casts behind F-10 | totals that cast; image values 142 / 130 / 232 / 628 (Q15) | 8,437 - 8,295 = 142 (DTA); 1,309 - 1,077 = 232 (other NCFA); 5,502 - 4,874 = 628 (NCL); 628 - 498 = 130 (DTL) | L330, L334, L337, L374, L391, L397 | PASS |
| Reg 33 dates | 14-02-2027; 30-05-2027; 14-08-2027 | 45 / 60 / 45 days after 31-12-2026, 31-03-2027, 30-06-2027 | R339 | PASS |

Arithmetic result: no mismatch above rounding in any A4 table, bridge, ratio or brief number.

---

## 3. ADVERSARIAL READ

### Claim 1. "The headline growth is real in rupees at the operating level" (rev L201); about 79% of the PAT change is recurring (rev L258)
Strongest bear counter from the extract. The incremental economics are thin. Sequentially, Operating EBITDA rose 48 lakh (1,293 to 1,341) on 1,410 lakh more net revenue (8,733 to 10,143), an incremental margin of 3.40% (L75, L76, L84, L85, L87, L95). YoY the incremental margin is 7.22% (208 / 2,879), against a 15.60% starting margin. Incremental gross margin QoQ is 16.74% (236 / 1,410). On Reading 3 the +10.74 Cr revenue contribution in the PAT bridge carries resin price and reverses with it.
Survives? Yes, the extract supports it. It is already in A4 in substance: Step 3 states "the QoQ gain in Q2 FY27 is +3.81% on +16.15% revenue" (rev L229). Step 2 states Op EBITDA "grew at less than half the revenue rate" (rev L183). Reading 3 and the A21 row carry the price-led caveat (rev L209, L408). No graft is required. I log the incremental-margin figures as a STYLE sharpening (S-25).

### Claim 2. "FCF positive": FY26 17.75 Cr, H1 FY27 2.86 to 7.41 Cr (rev L274), with CFO/PAT 0.84x for FY26 as the benchmark
Strongest bear counter from the extract. FY26 has its own undescribed investing outflow, and it is 4.2x the H1 one that A4 reads two ways.
- FY26 "Other inflows (outflows) of cash" in investing is (1,920) lakh (L271, R214). It is 60.2% of FY26 PAT (3,188, L108), 71.9% of derived FY26 CFO (2,670) and 2.1x FY26 PPE purchase (895, L245).
- The FY26 investing total casts on its visible lines: 4 - 895 + 4 + 48 - 1,920 = -2,759 (L244, L245, L268, L269, L271, L272). So no hidden investing line carries a net amount, and the 1,920 sits in the catch-all line. The labelled lines for loans to other parties (L261) and purchases of equity or debt instruments (L237) were not used.
- FY26 CFO less all investing was (89) lakh (2,670 - 2,759). Over FY26 plus H1 FY27, undescribed "other" investing outflows total 2,375 lakh (1,920 + 455). That is 1.6x capex of 1,476 lakh (895 + 581) and 46.8% of PAT of 5,077 lakh. Cash fell from 1,085 to 690 lakh (L296, L298) [FILED, derived].
- Treasury reading: the investment book was 2,149 lakh at 31-03-2026 (985 + 1,164, L330, L341). Interest received rose from 48 lakh in FY26 to 76 lakh in H1 FY27 alone (L269), about 3.2x annualised. That fits an interest-bearing placement made during FY26 [INFERENCE]. On this reading FY26 FCF of 17.75 Cr stands. The investment book is then mostly FY26 operating cash put to work, and whether it is cash-like stays the Q12 question.
- Non-treasury reading (capital advances, loans, other): FY26 FCF falls to (1.45) Cr (1,775 - 1,920). The balance sheet gives this reading little room: other non-current assets were 99 lakh and CWIP 50 lakh at 31-03-2026 (L336, L321) [INFERENCE].
- The split is ND because 31-03-2025 balances are not in this filing.
Survives? Yes. The extract supports it, and the review does not carry it: no "1,920", "19.20" or FY26 investing analysis appears anywhere. A4 gives the H1 455 two readings and an FCF range, but states FY26 FCF as a single positive number. That treatment is not symmetric. It also bears on two A4 positions: the A5-M6 cash-like question and F-14 (silence). It must be grafted. Type MISSING, loop A4 (finding A5-M7; graft text below).

### Claim 3. "Where the company looks strong": low debt on any reading, ROCE above 29% on any reading (rev L577; Step 6A rev L379)
Strongest bear counter from the extract. The ROCE numerator (PBT + FC) includes Other Operating Income, which is partly treasury (78 of 171 lakh, L76, L268, L269). The denominator (equity, plus implied debt) includes about 30 Cr of cash and investments (690 + 1,246 + 1,077 at 30-09-2026, L330, L341, L343). So the ratio may mix operating and treasury returns.
Test. Operating EBIT, H1 FY27 = 2,634 - 236 = 2,398 lakh, annualised 4,796. Operating capital employed = equity + D/E-implied debt - cash - current and non-current investments: 13,981 at 31-03-2026 and 15,607 at 30-09-2026, average 14,794. Operating ROCE = 32.42%. On BS-basis debt (nil), operating ROCE = 4,796 / 12,914.5 = 37.14% [FILED, derived].
Survives? No. If treasury income and treasury assets are removed, ROCE stays at or above A4's 29.15% to 32.63%. "Low debt" also holds on all three of A4's readings (at most 12.39 Cr net debt, 0.07x equity). The claim stands. The Amendment 17 caveat for a CONVERTER classification is already carried (rev L410).

### Mandatory acquisition-economics probe
Not triggered. The filing describes no acquisition, business purchase or stake buy. Note 5 states no subsidiary, associate or JV (L158). The business-combination and JV lines (L233 to L239) carry no value, and the investing section casts on its visible lines in both columns. The undescribed FY26 and H1 outflows (L271) are not described as acquisitions. Their composition is the subject of A5-M7.

---

## FINDINGS (tagged)

| ID | Type | Finding | Evidence | Loop |
|---|---|---|---|---|
| A5-M7 | MISSING | FY26 undescribed investing outflow (1,920) lakh (L271, R214) is absent from the review. FY26 FCF 17.75 Cr is stated without the two-reading treatment A4 applies to the H1 455. Not addressed: CFO less all investing (0.89) Cr in FY26, the 18-month 2,375 lakh of undescribed outflows against 1,476 lakh capex, and the 48 to 76 lakh interest-received jump. | L244, L245, L268, L269, L271, L272, L296, L298, L321, L330, L336, L341; rev L274, L310 to L313 | A4 |
| A5-F3 | FACTUAL | "On either label reading, inventory plus receivables rose about 22.51 Cr in FY26" (rev L301 and dependent cells) fails on A1's labels. There, L194 and L196 are both receivable rows, and the inventories row L192 has no value in the text layer, so the FY26 inventory movement is ND. Only the layout reading gives inventory 18.29 + current receivables 4.22 = 22.51 Cr. Each reading shows one elevated 31-03-2026 day-count base, not two: current receivables +80% on A1's labels (L342), or inventories +57% on the layout reading (L339). rev L302 says both gains start from an elevated base. The 22.51 Cr and 70.6% figures stand as the sum of the two FY26 trade cells. | L192 to L196, L339, L342; rev L275, L301, L302, L317, L321, L411, L456, L514, L535, L573, L655 | A4 |
| S-19 to S-27 | STYLE | Nine notes, below. | as listed | none |

No CONTRADICTION finding. No arithmetic mismatch. No orphan row. No row missing from the ledger that carries a value.

---

## GRAFT TEXT FOR A4 (exact; insert as written)

### A5-M7 (MISSING)
1. Step 5 FCF row (rev L274), FY26 cell. Replace "FY26: 17.75" with:
   "FY26: 17.75 before the undescribed investing outflow of 19.20 Cr (L271); (1.45) if that outflow is not a treasury placement. FY26 CFO less all investing: (0.89) (L272)"
2. Step 5, new paragraph directly after the "Undescribed investing outflow (455 lakh, L271): two readings" block (after rev L313):
   "FY26 undescribed investing outflow (1,920 lakh, L271, R214; A5-M7). The FY26 investing total casts on its visible lines: 4 - 895 + 4 + 48 - 1,920 = -2,759 (L244, L245, L268, L269, L271, L272). So no hidden investing line carries a net amount, and the 1,920 sits in the catch-all line, not on the loans line (L261) or the debt and equity instruments line (L237). It is 60.2% of FY26 PAT (L108), 71.9% of derived FY26 CFO of 2,670 and 2.1x FY26 PPE purchase of 895 (L245). FY26 CFO less all investing was (89) lakh. Over FY26 and H1 FY27, undescribed other investing outflows total 2,375 lakh (1,920 + 455), 1.6x capex of 1,476 and 46.8% of PAT of 5,077, while cash fell from 1,085 to 690 lakh (L296, L298) [FILED, derived].
   - Reading A, treasury placement. The investment book was 2,149 lakh at 31-03-2026 (L330, L341). Interest received rose from 48 lakh in FY26 to 76 lakh in H1 FY27 alone (L269), about 3.2x annualised [FILED, derived; INFERENCE]. On this reading FY26 FCF of 17.75 Cr stands. The investment book is then mostly FY26 operating cash put to work, and whether it is cash-like stays open (Q12).
   - Reading B, capital advances, loans or other uses. FY26 FCF falls to (1.45) Cr. The balance sheet gives this little room: other non-current assets were 99 lakh and CWIP 50 lakh at 31-03-2026 (L336, L321) [INFERENCE].
   - The 31-03-2025 balances are not in this filing, so the split is ND. Separating observation: the FY26 audited annual results filing under Reg 33, or the FY26 Annual Report. The FY26 column here is marked Audited (L73, L185), so that filing should exist and carry the FY26 cash flow by line and the 31-03-2025 balance sheet [INFERENCE]. It is not in this run's corpus. It would also settle the L194 and L196 labels (F-11) and the FY26 dividend (F-07) before the Q3 FY27 review."
3. Step 8.5, new row 17 (append, numbering stays stable):
   "| 17 | D | The FY26 cash flow shows 'Other inflows (outflows) of cash' of (1,920) lakh in investing (L271), 60% of FY26 PAT and more than twice FY26 PPE purchase of 895 lakh. H1 FY27 adds (455) lakh on the same line. What did each amount buy, by instrument, and on which 30-09-2026 balance-sheet line does it sit? | A5-M7 (F-05, F-14) | FY26 FCF is 17.75 Cr on a treasury reading and (1.45) Cr otherwise. It also decides how much of the investment book is cash-like (Q12). | Fixed deposits or liquid funds inside current investments or other financial assets, consistent with interest received rising from 48 lakh (FY26) to 76 lakh (H1 FY27). | Loans or advances to related parties, capital advances, or unlisted or illiquid instruments. |"
   Update the question count (16 to 17) in rev L449, L477 and the M11 row.
4. Monitorables, new row M12:
   "| M12 | Fetch the FY26 audited annual results filing (Reg 33) or the FY26 Annual Report: FY26 cash flow by line (the 1,920 at L271; the L194 and L196 labels), 31-03-2025 balance sheet, FY26 dividend | Now (due by 30-05-2026 under Reg 33; not in this run's corpus) | A5-M7, F-07, F-11, L271, L194, L196 |"
5. Brief part 1, after rev L551, two lines (the narrative stays inside 20 lines):
   "In FY26, 19.20 Cr went into an investing line the filing does not describe. That is 60% of FY26 profit, and FY26 cash flow after all investing was slightly negative, (0.89) Cr [FILED, derived]."
6. Brief part 5, new first "Now" fork:
   "- Now: fetch the FY26 audited annual results (M12). Bull: the 19.20 Cr FY26 outflow is a placement in liquid funds or deposits, and FY26 FCF stays 17.75 Cr. Bear: loans, advances or illiquid instruments; FY26 FCF then falls to (1.45) Cr."
7. Verdict flag 7 (rev L535) and the YAML cash flag (rev L655): append "; FY26 investing 'other' outflow of 1,920 lakh (L271) undescribed: FY26 FCF 17.75 Cr on a treasury reading, (1.45) Cr otherwise". YAML questions_for_management and monitorables: add Q17 and M12.

### A5-F3 (FACTUAL)
1. Replace rev L301 with:
   "- On either reading, the two FY26 trade cells (L194, L196) total 22.51 Cr, 70.6% of FY26 PAT of 31.88 Cr (L108) [FILED, derived]. On A1's labels both are receivables, and the FY26 inventory movement is not in the text layer (L192), so inventory plus receivables is 22.51 Cr plus an ND inventory movement. On the layout reading, inventories rose 18.29 Cr and current receivables 4.22 Cr, 22.51 Cr together."
2. Replace the first sentence of rev L302 with:
   "- Each reading shows one elevated 31-03-2026 base, not two: current receivables +80% on A1's labels (L342), or inventories +57% on the layout reading (L339). So part of the H1 FY27 day-count gain (inventory days 91.35 to 71.96, receivable days 41.42 to 33.72, like-for-like) may be an unwind of the FY26 build, not a structural tightening [INFERENCE]."
3. In rev L275, L317, L321, L411, L456, L514, L535, L573 and L655, replace "inventory plus receivables (22.51) / about 22.51 Cr of inventory plus receivables / inventory plus receivables +22.51 Cr on either reading" with "FY26 trade cells of 22.51 Cr (L194 + L196: receivables on A1's labels with inventory ND; inventory plus current receivables on the layout reading)". The numbers 22.51 Cr and 70.6% do not change.

No other table value changes. The verdict and the cash classification are for A4 to restate. On my read the verdict holds (PROCEED WITH FLAGS; INDETERMINATE-WITH-DIRECTION), with one added flag.

---

## VERDICT

**INCOMPLETE.** Failing agent: **A4.**
- A5-M7 (MISSING): FY26 undescribed investing outflow (1,920) lakh at L271 (R214) is not in the review. Graft the FY26 FCF qualifier, the two readings, Q17, M12, and the brief and verdict lines, as written above.
- A5-F3 (FACTUAL): the FY26 base-effect composition "inventory plus receivables 22.51 Cr on either reading" fails on A1's labels. Restate it in the 11 places listed.
Gate 0, the coverage audit and the arithmetic audit all pass. No A2 or A3 loop is needed.

---

## STYLE NOTES (logged, no loop)

- S-19 (A4, rev L87). Step 0C cites blank L276 and L278 as showing no share issue or buyback, with no period. H1 FY27 financing casts on visible lines (147 + 32 = 179, L283, L287, L290), so those lines are nil for H1 FY27. FY26 financing parts are not in the text layer (A4's own S-14). Paid-up capital of 1,059 in every column (L126, L360) carries the conclusion. Add the period qualifier.
- S-20 (A1/A2). R390 covers blank CF rows L192 to L223 only. The blank labelled rows at L141 to L143 (EPS, discontinued), L226 to L228 and L230, L233 to L267, L274 to L289 and L293 to L295 have no covering qualifier row. A4 relies on four of them (L276, L278, L282, L286) and reviews them. Investing casts in both columns and H1 financing casts, so the blanks are nil by cast there. Only the FY26 financing parts and FY26 operating subtotals are text-layer drops. Suggest one A1 qualifier row and one A2 ledger row. No number changes.
- S-21 (A4, rev L308). The hidden-flow cast counts the other current financial liabilities movement (-94, L384) as wholly operating. F-01 places the debt inside that line. Net of the 147 repayment (L283), the non-debt movement is about +53. The residual is then about -40 with the +400 inside the 1,084, against about +360 if the +400 sat elsewhere. The +400 allocation still fits best. State it as a conditional.
- S-22 (A4, rev L312). The cast-derived other non-current financial assets at 30-09-2026 are 232 (1,309 - 1,077, L334, L330), against 132 at 31-03-2026 (L333): +100 in H1. That is a further candidate home inside the 455. Reading B then reaches at most 274, still short of 455. The conclusion holds. A4 already uses 232 in the Q15 bull answer.
- S-23 (A1/A2/A4). The single "0" at L98 sits at the Q2 FY26 column position (column offsets against L97), not Q2 FY27. So R097's column tag is likely wrong. Interim deferred tax is nil by cast in every column, so no number changes. A4's Step 1 shows the filed "0" under Q2 FY27 (rev L140).
- S-24 (A4, rev L267). A typo: "(422.00 at L196" is missing its closing parenthesis.
- S-25 (A4, Step 3 rev L229). Optional sharpening: incremental Operating EBITDA margin 3.40% QoQ (48 / 1,410) and 7.22% YoY (208 / 2,879). Incremental gross margin 16.74% QoQ.
- S-26 (A1/A2). Auditor paragraph 1 (L451 to L459) has no row of its own. R396 ("title/scope") carries it. The count stays 5.
- S-27 (A4, F-01). Supporting datum: H1 FY27 finance cost of 44 lakh, annualised 88, on D/E-implied debt of 1,761 to 1,929 lakh gives a 4.6% to 5.0% cost (L84, L147, L364). That fits trade credit such as buyer's credit better than term debt [INFERENCE]. It supports the Q3 bull answer and changes nothing.

```yaml
stage: A5-adversary
loop: 2
company: "PREMIERPOL"
quarter: "Q2 FY27"
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
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "FCF positive: FY26 17.75 Cr; H1 FY27 2.86 to 7.41 Cr (Step 5, rev L274)"
    counter: "FY26 investing 'Other inflows (outflows)' of (1,920) lakh (R214) is undescribed and absent from the review: 60.2% of FY26 PAT, 71.9% of derived CFO, 4.2x the H1 455. FY26 CFO less all investing (0.89) Cr. 18-month undescribed outflows 2,375 lakh vs capex 1,476. FY26 FCF 17.75 Cr on a treasury reading (interest received 48 to 76 lakh), (1.45) Cr otherwise. 31-03-2025 balances ND"
    source_line: "L244, L245, L268, L269, L271, L272, L296, L298, L321, L330, L336, L341"
    type: MISSING
  - claim: "Headline growth real at the operating level; about 79% of PAT change recurring (rev L201, L258)"
    counter: "Incremental Op EBITDA margin 3.40% QoQ (48/1,410) and 7.22% YoY (208/2,879); already carried in substance (Step 3 +3.81% on +16.15%, Reading 3); no graft"
    source_line: "L75, L76, L84, L85, L87, L95"
    type: STYLE
findings_by_type:
  factual:
    - "A5-F3: 'inventory plus receivables +22.51 Cr on either label reading' (rev L301, L302 and 9 dependent cells) fails on A1's labels: L194 and L196 are both receivables there and inventories L192 has no value in the text layer, so the FY26 inventory movement is ND. Only the layout reading gives inventory 18.29 + current receivables 4.22. Each reading shows one elevated day-count base, not two. 22.51 Cr and 70.6% stand as the sum of the two trade cells. Loop A4"
  missing:
    - "A5-M7: FY26 undescribed investing outflow (1,920) lakh at L271 (R214) not in the review; FY26 FCF 17.75 Cr carries no qualifier, while the H1 455 gets two readings. Graft: FY26 FCF qualifier, two readings, Q17, M12 (fetch FY26 audited annual results), brief part 1 and 5 lines, verdict flag 7. Loop A4"
  contradiction: []
  style:
    - "S-19: 0C cites blank L276/L278 without period; H1 FY27 nil by financing cast, FY26 parts not in text layer; paid-up 1,059 carries it"
    - "S-20 (A1/A2): blank CF/EPS template rows outside R390 scope (L141-L143, L226-L230, L233-L267, L274-L289, L293-L295) lack a covering qualifier row; no value; A4 reviews the four it cites"
    - "S-21: hidden-flow cast treats OCFL -94 as operating while F-01 puts debt there; net of 147 repayment residual about -40 vs +360; allocation holds"
    - "S-22: cast-derived other NCFA 232 (L334 - L330) is +100 in H1; Reading B max 274, still below 455"
    - "S-23 (A1): L98 '0' sits at the Q2 FY26 column, not Q2 FY27; nil either way"
    - "S-24: typo '(422.00 at L196' in Step 5 column note"
    - "S-25: add incremental Op EBITDA margin 3.40% QoQ, 7.22% YoY to Step 3"
    - "S-26 (A1/A2): auditor para 1 (L451-L459) folded into R396; count unchanged"
    - "S-27: implied cost of D/E-implied debt 4.6% to 5.0% fits buyer's credit; supports Q3 bull answer"
loop_back_to: "A4"
gap: "A5-M7 MISSING: FY26 'Other inflows (outflows)' investing outflow (1,920) lakh at L271 (R214) is absent; graft the FY26 FCF qualifier (17.75 Cr treasury reading vs (1.45) Cr otherwise; CFO less all investing (0.89) Cr), two readings, Q17, M12 and brief/verdict lines per audit graft text. A5-F3 FACTUAL: restate the FY26 base effect as 22.51 Cr of trade cells L194+L196 (receivables on A1's labels with inventory ND; inventory plus current receivables on the layout reading), one elevated base per reading, in 11 places"
style_notes:
  - "S-19 0C period qualifier for L276/L278"
  - "S-20 A1/A2 covering qualifier for blank CF template rows"
  - "S-21 OCFL net of repayment in hidden-flow cast"
  - "S-22 other NCFA +100 as a Reading B candidate"
  - "S-23 R097 column tag likely Q2 FY26"
  - "S-24 missing parenthesis rev L267"
  - "S-25 incremental margins in Step 3"
  - "S-26 auditor para 1 row"
  - "S-27 implied debt cost 4.6% to 5.0%"
analyst_note: "Loop 2 re-audit on a fresh grep of the fulltext. Gate 0 passes. Coverage passes: 105 line items, 337 cells, 49 zero-standing, 42 qualifiers, 413 IDs, no orphan. Every A4 derived metric recomputes within rounding. Two A4 items, both bounded grafts with exact text in the audit; no Step 1 to 4 value changes. (1) MISSING: FY26 investing 'Other inflows (outflows)' of (1,920) lakh (L271, R214) appears nowhere in the review. It is 60.2% of FY26 PAT and 4.2x the H1 455 that A4 reads two ways, yet FY26 FCF 17.75 Cr carries no qualifier. FY26 CFO less all investing was (0.89) Cr. The interest-received jump (48 lakh FY26 to 76 lakh in H1 alone) favours a treasury placement, so the verdict likely holds, but the review must say so. The FY26 audited annual results, already due under Reg 33 and not in this corpus, would settle this, the L194/L196 labels and the dividend now. (2) FACTUAL: 'inventory plus receivables 22.51 Cr on either reading' fails on A1's labels, where the FY26 inventory cell is missing from the text layer. Nine STYLE notes are logged."
```
