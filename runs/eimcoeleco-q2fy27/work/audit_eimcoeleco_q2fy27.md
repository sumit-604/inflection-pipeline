# A5 AUDIT: Eimco Elecon (India) Limited (EIMCOELECO) | Q2 FY27 | audit of A4 review, Revision Loop 2

Run: /run-quarterly A5 adversary | Model: claude-opus-5-5 | Date: 2026-10-17
Inputs read: A4 review (work/review_eimcoeleco_q2fy27.md, 628 lines); A1 fulltexts (results 523 lines, presentation 787 lines, press release 166 lines); A1 structured files (results R001-R470, presentation R001-R946, press release R001-R092); A2 ledgers (results, presentation, press release).
Not read: source PDFs, anything under inputs/, A3 notes, orchestrator commentary, earlier audit files. No pipeline error arose: every check below resolved from the A1 extracts.
Anchor key: `res / pres / pr Lnnn` = line in the A1 fulltext; `rev Lnnn` = line in the A4 review; `[d]` = arithmetic on filed numbers, lakh basis unless stated.
Finding IDs continue after the IDs that appear in the A4 change logs (F01-F03, M01-M04, C01, S01-S18), so this audit uses F04, M05, M06 and S19 onward.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Heading | Content check | Status |
|---|---|---|---|
| 1. Summary narrative | rev L465 | 18 lines (rev L466-483), inside the 10-20 line band (Quarterly protocol governs). Every figure tier-tagged. | present |
| 2. Sector intelligence | rev L485 | Coal, metals, construction, payer mix, read (rev L486-491). | present |
| 3. Business-model intelligence | rev L493 | Products, segment, installed base, distributor commission, treasury, model drift, disclosure gaps (rev L494-501). | present |
| 4. Competition intelligence | rev L503 | No peer in filings; inferred peers tagged PENDING LIVE VERIFICATION; strengths, weaknesses, margin risk (rev L504-508). | present |
| 5. Forward map | rev L510 | Make-or-break reading plus 7 dated catalysts, each with a bull and a bear fork (rev L511-518). | present |

Gate: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Method: fresh pass over each A1 fulltext, line by line for statements and tables, page markers for slides, then diff against the A2 ledger counts and the structured ID ranges.

### 1A. Results filing (res L1-523)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7: Notes 1-5 (res L188-194), Note 6 (res L266), unnumbered cash-flow Note (res L328) | none | PASS |
| Line items | 99 | 99: P&L 27 (res L154-186), BS 36 (res L204-265, MSME and non-MSME payables split), CF 36 (res L273-326, incl. financing total res L322 = M001; res L316 is a label with no values) | none | PASS |
| Zero-standing | 11 | 11 (res L171, L177-179 blank interim cells; R150 placement; res L236-237 Mar-26 blanks; res L315 H1 FY26 blank; Note 3; Annexure B two N.A. cells) | none | PASS |
| Agenda items | 2 | 2 (res L35, L41) | none | PASS |
| Auditor paragraphs | 4 | 4 (res L94, L100, L108, L119) | none | PASS |
| Entities | 29 | 29; no entity in the fulltext outside R375-R403 | none | PASS |
| Annexures | 3 | 3 (res L79, L457, L481) | none | PASS |
| Signatures | 4 | 4 (res L70-76, L125-136, L337-339, L521-522) | none | PASS |
| Press-release numbers | 10 | 10 (res L395-414) | none | PASS |
| Chart labels | 36 | 36 (res L355-367: 24; res L376-384: 12) | none | PASS |

Missing from structured: M001 only, already carried in the ledger (A2 section 11). Missing from ledger: none.
Data-correction checks (A2/A3, applied by A4 at rev L18-21): R150 belongs to 31.03.26 (NCA sum 31,717.32 ties only with it; 30.09.26 sum 33,502.99 ties without it, res L204-212). R014 = 8,528.25 (7,752.31 + 775.94). R153 = 11,547.54 (current-asset sum ties to 22,558.10). R242 = (308.64) (WC lines tie to 968.10 cash generated). FY26 PPE sale proceeds tie to 121.03 by the investing total; A4 leaves the verbatim value NOT FOUND, which is acceptable. H1 FY26 investing column sums to (364.39) but the values sit against the wrong labels (interest 241.20 and dividend 10.15 match the res L280-281 add-backs one row lower), so A4's H1 FY26 capex ND is correct. All confirmed.

### 1B. Presentation (pres L1-787)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 39 | 39 page markers | none | PASS |
| Line items (table x metric) | 130 | 130: slide 18 = 21, 19 = 33, 20 = 12, 36 = 19, 37 = 33, 38 = 12 | none | PASS |
| Slide numbers | 748 | 748: table cells 617 recounted line by line (slide 18 = 149, 19 = 146, 20 = 48, 36 = 81, 37 = 145, 38 = 48) plus 131 non-table numbers (slide ranges confirmed; slides 15, 16, 17, 24, 28-31, 33 recounted value by value) | none | PASS |
| Zero-standing | 93 | 93: slide 18 = 10, 19 = 37, 20 = 1, 28 = 1, 36 = 4, 37 = 38, 38 = 2 | none | PASS |
| Entities / forward / dates / footnotes | 73 / 18 / 72 / 35 | Contiguous ID ranges R749-R946; slide-level recount on slides 15, 28-31 matched | none | PASS |

### 1C. Press release (pr L1-166)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages | 4 | 4 | none | PASS |
| Slide numbers | 50 | 50: p1 = 2, p2 = 36 (charts), p3 = 10 (ED remarks), p4 = 2 | none | PASS |
| Entities / forward / dates / qualifiers | 14 / 7 / 14 / 7 | 14 / 7 / 14 / 7 | none | PASS |
| Footnote markers | 0 | 0 | none | PASS |

### 1D. Ledger row to review

A4 marks every ID range reviewed (rev L13: results R001-R470 plus M001; presentation R001-R946; press release R001-R092). The flagged rows are also cited one by one: R150 (rev L18), R014, R153, R242, R267 (rev L19), M001 (rev L21), R443 (rev L44), R452, R453 (rev L57-58), R091 (rev L59), R464 (rev L122); Notes N1-N6 and N-CF (rev L52-58); slide 25 roster (rev L491); R092 label mismatch (rev L389, FN19 / PR/F16-2).
Orphan rows: none. Rows the fresh pass found that the ledger lacks: none.
COVERAGE AUDIT: PASS.

---

## 2. ARITHMETIC AUDIT

Every derived figure in A4 Steps 1-8.5, the brief and the monitorables was recomputed from the lakh statement. Crore = lakhs x 0.01.

| Metric | A4 value (rev line) | Recomputed [d] | Source line | Status |
|---|---|---|---|---|
| Step 1 crore conversions, all 6 columns | rev L81-102 | every cell ties to lakhs / 100 | res L154-186 | PASS |
| Q2 FY27 expense tie | 4,824.54 (rev L104) | 4,824.54 | res L158-167 | PASS |
| Operating EBITDA Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27 | 5.22 / 14.25 / 10.74 / 42.97 / 17.53 / 24.99 (rev L109) | 522.04 / 1,424.71 / 1,074.35 / 4,297.10 / 1,753.07 / 2,499.06 | res L155, L163-164, L168 | PASS |
| Operating EBITDA margin | 15.71 / 18.38 / 18.92 / 18.62 / 17.39 / 18.61% (rev L110) | 15.71 / 18.38 / 18.92 / 18.62 / 17.39 / 18.61% | res L154 | PASS |
| Reported EBITDA | 9.49 / 22.01 / 12.63 / 59.98 / 29.89 / 34.64 (rev L111) | same | res L163-164, L168 | PASS |
| Core PBT (PBT - OI) | 2.62 / 11.86 / 8.55 / 33.35 / 12.94 / 20.41 (rev L112) | 262.00 / 1,185.91 / 855.18 / 3,335.17 / 1,294.14 / 2,041.09 | res L155, L168 | PASS |
| OI / PBT | 62.0 / 39.6 / 18.1 / 33.8 / 48.9 / 32.1% (rev L113) | same | res L155, L168 | PASS |
| Effective tax rate | 22.36 / 21.61 / 24.99 / 23.12 / 21.62 / 22.79% (rev L114) | same | res L168, L173 | PASS |
| PAT margin | 16.10 / 19.84 / 13.79 / 16.78 / 19.68 / 17.28% (rev L115) | same | res L154, L174 | PASS |
| Gross margin, filing basis | 71.75 / 54.14 / 59.88 / 57.13 / 62.70 / 56.57% (rev L116) | GP 2,384.81 / 4,196.84 / 3,401.00 / 13,183.04 / 6,320.68 / 7,597.84 | res L154, L158-160 | PASS |
| Distributor comp / revenue | 11.85 / 11.23 / 5.57 / 11.48 / 11.62 / 8.84% (rev L117) | same | res L154, L165 | PASS |
| Other Expenses / revenue | 19.81 / 14.69 / 22.29 / 14.01 / 17.89 / 17.91% (rev L118) | same | res L154, L166 | PASS |
| Distributor + Other / revenue | 31.66 / 25.92 / 27.86 / 25.48 / 29.51 / 26.75% (rev L119) | H1 FY27 26.74% (3,592.21 / 13,432.03); others same | res L154, L165-166 | PASS (rounding, S19) |
| Employee cost / revenue | 17.90 / 7.47 / 9.76 / 9.54 / 11.46 / 8.44% (rev L120) | same | res L154, L162 | PASS |
| Computed EBITDA growth vs release | +105.8% (rev L122) | 1,074.35 / 522.04 = +105.8% | res L403 | PASS |
| Deck "Other Expenses" = distributor + other | 16 and 20 (rev L122) | 15.83 and 20.10 | pres L391 | PASS |
| Q2 YoY: revenue, PBT, PAT, EPS | +70.9 / +51.5 / +46.4 / +46.3% (rev L132-142) | same | res L154, L168, L174, L185 | PASS |
| Q2 FY26 vs Q1 FY26 revenue | -50.8% (rev L132) | 3,323.64 / 6,756.99 = -50.8% | res L154 | PASS |
| Q2 margin change | +321 bps (rev L134) | +320.9 bps | [d] | PASS |
| D&A, finance cost, OI YoY | -15.1 / -25.5 / -55.7% (rev L135-138) | same | res L155, L163-164 | PASS |
| Operating EBIT | 2.78 to 8.67, +211.6% (rev L137) | 278.40 to 867.39, +211.6% | [d] | PASS |
| Core PBT YoY | +226.4% (rev L139) | 855.18 / 262.00 = +226.4% | [d] | PASS |
| H1 YoY: revenue, op EBITDA, OI, core PBT, PBT, PAT, EPS | +33.2 / +42.6 / -22.0 / +57.7 / +18.8 / +17.0 / +17.0% (rev L144) | same | res L154-185 | PASS |
| H1 margin change | +122 bps (rev L144, L209) | +121.5 bps | [d] | PASS (rounding, S19) |
| TTM core PBT; gain; Q2 share | 40.82; +22.4%; 7.47; 5.93 = 79% (rev L144) | 4,082.12; +22.4%; 746.95; 593.18 = 79.4% | [d] | PASS |
| Trough-free Q1 core PBT | 10.32 to 11.86, +14.9% (rev L144) | 1,032.14 to 1,185.91, +14.9% | [d] | PASS |
| GM / employee / manufacturing / net / combined line, Q2 YoY | -1,187 / +814 / +314 / -59 / +380 bps (rev L148) | -1,187.3 / +813.8 / +314.3 / -59.2 / +380.2 | res L154, L158-166 | PASS |
| Margin without the distributor plus other line | 15.11% (rev L148) | 18.916 - 3.802 = 15.11% | [d] | PASS |
| Other Expenses and distributor comp, rupees YoY | +92.3% / -19.6% (rev L148) | same | res L165-166 | PASS |
| H2 FY26 quarterly average core PBT | 10.21 (rev L149) | 2,041.03 / 2 = 1,020.52 | [d] | PASS |
| TTM EPS vs FY25 | 72.97, -14.4% (rev L149) | 67.11 - 34.38 + 40.24 = 72.97; 72.97 / 85.25 = -14.4% | res L185; pres L715 | PASS |
| Distributor-rate effect | 3.57 cr = 60% (rev L149) | 356.62 lakhs; 60.1% of 593.18 | res L154, L165 | PASS |
| ETR change and cost | +263 bps; 0.28 (rev L150) | +263.6 bps; 27.52 lakhs | res L168, L173 | PASS (rounding, S19) |
| PPE increase | 47.44, +74.0% (rev L151, L242) | 4,744.12; +74.0% | res L204 | PASS |
| FV gains share of H1 OI; book roll | 74.7%; 8.24 = 1.03 + 7.21 (rev L152) | 721.17 / 965.00 = 74.7%; 823.92 = 102.75 + 721.17 | res L209, L216, L278, L305 | PASS |
| Q1 FY26 revenue, margin, core PBT | 67.57 / 18.22% / 10.32 (rev L160) | 6,756.99 / 18.22% / 1,032.14 | [d] | PASS |
| H2 FY26 revenue, margin, core PBT | 129.94 (64.97) / 19.58% / 20.41 (10.21) (rev L162) | 12,994.02 / 19.58% / 2,041.03 | [d] | PASS |
| Q1 FY27 vs H2 average; vs Q1 FY26 | +19.3%; +14.7% (rev L163) | same | [d] | PASS |
| QoQ: revenue, op EBITDA, core PBT, OI, PBT, PAT | -26.7 / -24.6 / -27.9 / -75.6 / -46.8 / -49.1% (rev L166) | same | res L154-174 | PASS |
| Sequential GM Q1 FY26 / H2 FY26 | 58.25 / 52.81% (rev L171-173) | 3,935.87 / 6,756.99; 6,862.36 / 12,994.02 | [d] | PASS |
| Spares share (A3-14 reading) | 21 / 48 / 18 / 35% (rev L171-176) | 14/67.57 = 20.7%; 16/33.24 = 48.1%; 14/77.52 = 18.1%; 20/56.80 = 35.2% | res L357-367 | PASS |
| H2 share of FY26; H1 quarterly average; H2 threshold; book cover | 56.3%; 67.16; 173.1; 77% (rev L181-184) | same | [d] | PASS |
| Q2 PAT bridge, 7 components and shares | +3.70 / +1.82 / +0.37 / +0.04 / -2.38 / -0.79 / -0.28 = +2.48 (rev L193-203) | 370.07 / 182.24 / 36.68 / 4.19 / -238.16 / -79.38 / -27.52 = 248.12; shares 149.2 / 73.4 / 14.8 / 1.7 / -96.0 / -32.0 / -11.1% | [d] | PASS |
| H1 PAT bridge, 7 components and shares | +5.83 / +1.63 / +0.13 / -0.12 / -2.71 / -1.03 / -0.35 = +3.38 (rev L208-216) | 582.83 / 163.16 / 12.88 / -11.92 / -271.39 / -102.83 / -35.02 = 337.71; shares 172.6 / 48.3 / 3.8 / -3.5 / -80.4 / -30.4 / -10.4% | [d] | PASS |
| OI reversion; core PAT | PBT 12.82, PAT 9.62; 6.41 vs 2.03, +215% (rev L220) | 1,282.40 / 961.87; 641.43 vs 203.42, +215.3% | [d] | PASS |
| Ex-deferred H1 ETR; DTL fall | 25.91%; 0.94 (rev L222) | 779.00 / 3,006.09; 770.36 - 676.36 = 94.00 | res L170, L239 | PASS |
| CFO; CFO / PAT | 1.84 / 6.04 / 22.11; 0.08 / 0.30 / 0.57x; -69.6%; -0.23x (rev L232-233) | same | res L174, L300 | PASS |
| CFO without the OFL line | (5.30) / 6.04 / 22.02; (0.23)x (rev L234) | 183.78 - 713.83 = (530.05); 603.91; 2,201.80; -0.228x | res L294, L300 | PASS |
| FCF | (0.28) / (38.44); (7.42) without OFL (rev L236) | (27.70) / (3,844.02) / (741.53) | res L300, L303 | PASS |
| WC change | (15.76) / (6.08) / (11.31); -9.68 (rev L237) | (1,575.83) / (607.73) / (1,130.96) | res L288-294 | PASS |
| Receivable / inventory / payable days; CCC | 114.7 to 123.9 / 400.4 to 361.2 / 65.1 to 81.2; 450.0 to 403.9 (rev L238-241) | 114.66 to 123.89 / 400.44 to 361.22 / 65.05 to 81.18; 450.05 to 403.93 | res L154, L158-160, L214, L217, L252-257 | PASS |
| Net debt ex-investments | 3.55 to 5.75, +2.20 (rev L245) | 355.25 to 574.53, +2.19 | res L218-219, L235, L243-244 | PASS (rounding, S19) |
| Liquid net cash; with leases | 11.86 to (1.53), -13.39; (2.93) (rev L246) | 1,186.31 to (152.54), -1,338.85; (293.07) | res L216, L218-219, L235, L243-244 | PASS |
| Net cash incl. investments; non-current share; ex-MTM | (200.98) to (207.03), +6.05; 98.7%; -1.17 (rev L247) | 20,098.40 to 20,703.04; 98.68%; 604.64 - 721.17 = -116.53 | res L209, L216, L278 | PASS |
| Supporting stock items | receivables +25.8%; inventories +6.4%; current investments -79.7%; investments 37.95% of assets; OCFL +110%; OCL -17.7% (rev L250) | same | res L209-261 | PASS |
| OFL balance-sheet rise | 6.11 (rev L254) | 582.84 + 28.37 = 611.21 | res L236, L260 | PASS |
| Current ratio; NFAT | 3.53; 2.22 (rev L256) | 22,558.10 / 6,399.17 = 3.53; 264.26 / 119.03 = 2.22 | res L204-207, L223, L264 | PASS (basis unstated, S25) |
| FY23-FY26 OCF / PAT | 74 / 149 = 0.50x (rev L258) | 0.497x | pres L713, L762 | PASS |
| TTM revenue, op EBITDA, OI, PAT, EPS | 264.26 / 50.43 (19.08%) / 14.29 / 42.09 / 72.97 (rev L333) | 26,426.05 / 5,043.09 / 1,429.08 / 4,209.04 | [d] | PASS |
| Net cash per share; book value per share | 358.9; 846.7 (rev L335) | 20,703.04 / 57.684 = 358.9; 48,841.06 / 57.684 = 846.7 | res L181, L231 | PASS |
| Order book / TTM revenue | 0.50x (rev L345) | 133 / 264.26 = 0.503x | res L377 | PASS |
| Q3 margin at the Q1 distributor rate | 13.3% (rev L386) | (1,074.35 - 321.37) / 5,679.72 = 13.26% | res L154, L165 | PASS |
| Fixed-cost recovery | +1,128 bps (rev L394) | 813.8 + 314.3 | [d] | PASS |
| Implied FY26 DPS; FY25 DPS | 4.00; 5.00 (rev L400) | 230.74 / 57.684 = 4.00; 288.21 / 57.684 = 5.00 | res L230, L319 | PASS |
| Letter-to-board gap | 38 days (rev L66) | 5 Sep to 13 Oct = 38 | res L32, L486 | PASS |
| Book run-off | about six months (rev L435) | 133 / 264.26 x 12 = 6.0 | [d] | PASS |

Mismatches above rounding: none. Four 1 bp or Rs 0.01 cr drifts come from subtracting rounded figures (S19). None changes a conclusion.
ARITHMETIC AUDIT: PASS.

---

## 3. ADVERSARIAL READ

### AR1. Claim: "The filed series shows a mix effect. It shows no price erosion." (rev L178; repeated rev L508, flag rev L614, analyst_note rev L625; rev L148 frames the YoY gross-margin fall as a Q2 FY26 outlier effect)

Strongest bear counter, from the same extract. Use A4's own A3-14 chart reading (spares = upper segment; res L357-367, pr L66-76) and A4's own filing-basis gross margins (res L154, L158-160).

1. A4's own test is met by A4's own table. The competition brief says "Tender pricing would show as a margin fall at a stable spares share" (rev L508). The trough-free Q1 pair, which A4 itself adopted as the clean comparator for profit (rev L144), shows this. Spares share moved from 20.7% to 18.1%. Gross margin fell 411 bps (58.25% to 54.14%).
2. Mix cannot carry the YoY fall at any feasible spares margin. Assume constant segment margins and give mix the most room: spares at a 100% gross margin, chart labels rounded the most favourable way (plus or minus Rs 0.5 cr per label, Rs 1 cr for the derived Q1 segments).

| Pair | GM change | Spares share | Most mix can explain | Within-segment fall, at least |
|---|---|---|---|---|
| H1 FY26 to H1 FY27 | -613 bps (62.70% to 56.57%) | 29.8% to 25.3% (30/100.81; 34/134.32) | about 285 bps | about 330 bps |
| Q2 FY26 to Q2 FY27 | -1,187 bps | 48.1% to 35.2% | about 860 bps | about 330 bps |
| Q1 FY26 to Q1 FY27 (trough-free) | -411 bps | 20.7% to 18.1% | about 290 bps | about 120 bps |

3. At a realistic spares premium the fall inside the segments is larger. The sequential Q1 to Q2 FY27 move (+574 bps on a 17.2 pp spares shift) implies a spares premium of about 33.5 pp. At that premium the within-segment YoY fall is about 320 bps (Q1), 460 bps (H1) and 750 bps (Q2). At the FY26 within-year premium (about 49 pp) it is about 280, 395 and 550 bps.
4. Inventory-build timing does not explain the H1 or Q1 pairs. The FG/WIP build was 2.9% of revenue in H1 FY26 and 0.3% in H1 FY27 (res L154, L160). Q1 drawdowns were similar: 15.9% of revenue in Q1 FY26 [d: (296.02) - (1,372.14) = +1,076.12] and 14.4% in Q1 FY27. Only the Q2 pair is confounded (build 41.3% vs 20.2% of revenue).
5. Under the opposite chart reading (spares = lower segment), the spares share runs 51% / 65% / 80% / 83% (Q2 FY26 / Q2 FY27 / Q1 FY26 / Q1 FY27). Gross margin then ranks inversely with spares share, so the mix reading fails outright.

Symmetric reading (the bull side): the within-segment fall need not be tender price. It can be input cost, or mix inside the equipment line (continuous-miner packages, LHDs, piling rigs). Traded goods do not explain it: stock-in-trade purchases fell (5.54 to 5.24 cr in H1, res L159). The filing cannot split price, cost and inside-equipment mix. Q11 (rev L394) is still the right question.

Survives: YES. The claim "shows no price erosion / mix, not price" is not supported by the extract. Under either chart reading, the series shows a gross-margin fall inside the segments of at least about 120-330 bps YoY. Graft into A4 (A5-F04, FACTUAL). Suggested replacement for rev L178 and rev L508: "Mix explains part of the fall, not all of it. Under the A3-14 chart reading, H1 gross margin fell 613 bps while the spares share fell 4.5 pp. Even at a 100% spares gross margin, mix explains at most about 285 bps. At least about 330 bps is a fall inside the segments. The trough-free Q1 pair shows the same: -411 bps on a 2.7 pp spares shift. The H1 and Q1 pairs are nearly free of inventory-build timing. The fall inside the segments can be price, input cost, or mix inside the equipment line. The filing cannot split them. Q11 is the test." Align rev L148 (the YoY fall is not only an outlier effect: H1 -613 bps, Q1 -411 bps), rev L182, rev L394 (Q11 why), rev L499-500, flag rev L614 and analyst_note rev L625.

### AR2. Claim: "The PAT growth is operating" and core PBT +226% YoY (rev L139, L219, L449)

Strongest bear counter: the +226% runs off the Q2 FY26 trough (revenue -50.8% QoQ, res L154). The trough-free Q1 pair is only +14.9%. Rs 3.57 cr of the Rs 5.93 cr gain (60%) equals the unexplained distributor-rate drop (res L154, L165). The Rs 0.37 cr D&A tailwind is exposed to the Rs 47.44 cr capitalisation (res L164, L204). Q2's Rs 8.55 cr sits below the H2 FY26 quarterly average of Rs 10.21 cr.

Survives as a new item: NO. A4 already carries every element: rev L139, L149, L195, L219, L373, L449 and flag rev L613. No graft needed.

### AR3. Claim: "Mitigant: ED Kamlesh Shah signs the statements ... That gives continuity." (rev L451; flag rev L610)

Strongest bear counter: the CFO's letter is addressed to "The Executive Director", with no name (res L488-490). It asks to "work closely with you and the team" on the finance handover (res L510). The board has two Executive Directors: Prayasvin B. Patel (pres L201-202) and Kamlesh Shah (pres L212-213). Kamlesh Shah is the ED who signs the statements (res L337-339) and has the finance profile (pres L214-217). If he is the addressee [INFERENCE], the continuity mitigant is also the officer who held the letter for the 38 days between its date (res L486) and the board noting it (res L32, L41). A4 says the mitigant "does not address the 38-day gap" (rev L451). The extract supports a sharper point: the mitigant may sit inside the gap.

Survives: YES. Graft into A4 (A5-M05, MISSING). Add to verdict item 2 (rev L451), flag rev L610 and Step 0D (rev L66): the letter's addressee is an unnamed ED, one of two. Q9 (rev L392) should ask which ED received the letter and on what date.

### Mandatory acquisition-economics probe

Not triggered. None of the three documents describes an acquisition, a purchase or a stake buy (res L1-523, pres L1-787, pr L1-166). The nearest item is the Rs 47.44 cr PPE capitalisation (res L204). It was funded from the Rs 48.25 cr other non-current assets balance and the FY26 capex payments of Rs 60.55 cr (res L211, L303). No target, price or earnings is stated, so no price-to-earnings multiple can be formed. On its own economics, the asset is 74% of the Mar-26 PPE base and about 18% of TTM revenue [d: 47.44 / 264.26], with no capacity, revenue or return disclosed. Net investment purchases of Rs 1.03 cr (res L305) name no holding. A4 carries the capitalisation (FN09; Q4, Q5; rev L183, L263). No finding.

### Symmetric test of a bear claim (Master v3.7 Rule J: a bear claim carries the same bar)

Claim: "Liquid treasury turned to net borrowing in H1" and "The borrowing is a liquid funding need at the operating level" (rev L246, L264; verdict item 4 rev L453; flag rev L615; summary rev L479).

Counter from the same extract: the liquid net cash fall is Rs 13.39 cr [d]. Rs 11.05 cr of it (82%) is the drop in current investments, from Rs 13.86 cr to Rs 2.81 cr (res L216). In the same half, non-current investments rose Rs 19.28 cr (res L209), and the total book rose Rs 8.24 cr on Rs 1.03 cr of net purchases (res L305) plus Rs 7.21 cr of gains (res L278). The current-investment fall is therefore a shift inside the book, not cash spent. The rest is borrowing of Rs 2.96 cr (res L243) less a Rs 0.62 cr rise in cash and bank (res L218-219). The company also net-bought Rs 1.03 cr of investments in the half it borrowed Rs 2.87 cr (res L305, L315).

Two readings: (bear) the company needed liquidity that a locked or illiquid non-current book could not supply; (bull) it chose to move Rs 11 cr into longer instruments and borrow short rather than sell. The observation that separates them is the composition and redemption terms of the non-current book (Q16) and the facility type (Q14). A4 names both questions but not the attribution.

Survives: YES, as a missing qualifier. Graft into A4 (A5-M06, MISSING). Add the attribution to the Step 5 liquid row (rev L246), the net-debt answer (rev L264), verdict item 4 (rev L453), flag rev L615 and the summary line rev L479, keeping the summary inside 20 lines (now 18).

---

## 4. FINDINGS REGISTER

| ID | Type | Finding | Evidence | Loop to |
|---|---|---|---|---|
| A5-F04 | FACTUAL | "Shows no price erosion / mix, not price" is not supported. Under A4's own chart reading, at least about 330 bps (H1, Q2) and 120 bps (trough-free Q1) of the YoY gross-margin fall is inside the segments. The Q1 pair meets A4's own tender-pricing test (rev L508). | res L154, L158-160, L357-367; AR1 | A4 |
| A5-M05 | MISSING | The continuity mitigant lacks the qualifier that the CFO letter is addressed to an unnamed ED, one of two, and the mitigant may be the addressee who held it for 38 days. | res L32, L41, L337-339, L486-490, L510; pres L201-217; AR3 | A4 |
| A5-M06 | MISSING | The liquid-treasury flag lacks the attribution: 82% of the Rs 13.39 cr fall is a shift inside the investment book, not cash spent. Also missing: net purchases of Rs 1.03 cr during a half with Rs 2.87 cr of new borrowing, and the two readings with their separator. | res L209, L216, L218-219, L243, L278, L305, L315 | A4 |

No CONTRADICTION findings. No coverage or arithmetic failures.

---

## 5. VERDICT

**INCOMPLETE.** Failing agent: **A4**.
- A5-F04 (FACTUAL): replace the "mix, not price erosion" reading at rev L178, L508, L614, L625 with the bounded reading in AR1. Align rev L148, L182, L394, L499-500.
- A5-M05 (MISSING): qualify the ED continuity mitigant at rev L451, L610 and rev L66 with the unnamed-addressee point. Sharpen Q9 (rev L392).
- A5-M06 (MISSING): attribute the liquid-treasury fall at rev L246, L264, L453, L615, L479. Name both readings, with Q14 and Q16 as the separator.

Gate, coverage and arithmetic all pass. None of the three fixes needs new data. None challenges the protocol verdict class PROCEED WITH FLAGS. The fixes change what the flags say, so they are not STYLE.

---

## 6. STYLE NOTES (logged; no re-run)

- A5-S19 Rounding drift from subtracting rounded figures: H1 margin change +122 bps vs lakh-basis +121.5 (rev L144, L209); Q2 ETR change +263 bps vs +263.6 (rev L150, L199; the Rs 0.28 cr cost ties); net debt change +2.20 vs +2.19 (rev L245); H1 FY27 distributor plus other 26.75% vs 26.74% (rev L119). Fix: compute changes from unrounded values.
- A5-S20 FN20 is cited for two different issues: the H1 FY26 investing misalignment (rev L20, L58, L235) and the EBITDA definition (rev L122, L403, L412). Confirm the ID.
- A5-S21 rev L449 "two cell positions need the data corrections" understates the preamble list (R150, the six-cell H1 FY26 investing block, R014, R153, R242, R267). Say "the data corrections listed under the preamble".
- A5-S22 The Reg 33 result deadlines (rev L370, L433, L437, L511, L518) are statute, not filing. Tag them [statute, not in filing], as rev L432 does for s.203(4).
- A5-S23 rev L171 and L175 cite res L364-367 for the Q1 spares shares. The H1 segment labels they use sit at res L359 (34) and res L362 (30).
- A5-S24 rev L262 "-6.6% (247 to 231, pres L697)": the anchored deck figures give -6.5%. The -6.6% uses filed 230.75 (res L154). Cite both.
- A5-S25 rev L256 NFAT 2.22 has no stated basis. It ties to TTM revenue 264.26 / (PPE 111.55 + CWIP 0.45 + intangibles 7.03) (res L204-207). The same basis gives FY26 3.11 against deck 3.1 (pres L376), so only the H1 FY27 deck ratio fails to tie.
- A5-S26 Bull-side symmetry: the Sep-25 book of Rs 44 cr (res L381) preceded H2 FY26 revenue of Rs 129.94 cr (0.34x). The Sep-26 book is 0.77x of the H2 FY27 threshold (rev L184). One line would show that visibility is above last year's, and that the book has not been the binding driver of H2 revenue.
- A5-S27 The deck gross margin (pres L389: 56.5% Q2 FY27, 65.2% Q2 FY26) deducts manufacturing expense; the filing basis does not ((5,679.72 - 2,278.72 - 189.93) / 5,679.72 = 56.54%, res L154, L158-161). One reconciling line would stop a reader treating the two as in conflict.
- A5-S28 Current provisions rose from Rs 5.98 cr to Rs 7.72 cr (+29%, res L262) and are not in the supporting stock items (rev L250). A Q3 sub-question could ask whether warranty provisions on higher equipment dispatch sit in Other Expenses.

---

```yaml
stage: A5-adversary
company: "EIMCOELECO"
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
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - {claim: "The filed series shows a mix effect; it shows no price erosion (rev L178, L508, L614, L625; rev L148 frames the YoY GM fall as an outlier-base effect)", counter: "Under A4's own A3-14 chart reading, mix cannot carry the YoY GM fall. Trough-free Q1 FY27 vs Q1 FY26: spares share 20.7% to 18.1%, GM -411 bps, which meets A4's own tender-pricing test (rev L508). Even at a 100% spares gross margin and the most favourable chart rounding, mix explains at most about 285 of the 613 bps H1 fall and about 860 of the 1,187 bps Q2 fall; at least about 330 bps (H1, Q2) and 120 bps (Q1) is within-segment. H1 and Q1 pairs are nearly free of FG/WIP build timing. The residual may be price, input cost or mix inside equipment; the filing cannot split them. Under the opposite chart reading GM ranks inversely with spares share.", source_line: "res L154, L158-160, L357-367; pr L66-76", type: FACTUAL}
  - {claim: "ED Kamlesh Shah signs the statements and gives continuity (rev L451, L610)", counter: "The CFO letter is addressed to an unnamed 'The Executive Director' (res L488-490) and offers to 'work closely with you' on the finance handover (res L510). The board has two EDs, Prayasvin B. Patel and Kamlesh Shah (pres L201-202, L212-213). If the addressee is Kamlesh Shah [INFERENCE], the continuity mitigant is also the officer who held the letter through the 38 days before the board noted it (res L486, L32, L41). Q9 should name the addressee and the receipt date.", source_line: "res L32, L41, L337-339, L486-490, L510; pres L201-217", type: MISSING}
findings_by_type:
  factual:
    - "A5-F04: 'mix, not price erosion' (rev L178, L508, L614, L625) unsupported; at least ~330 bps (H1, Q2) and ~120 bps (trough-free Q1) of the YoY GM fall is within-segment under A4's own chart reading; Q1 meets A4's own tender-pricing test. Loop A4."
  missing:
    - "A5-M05: ED continuity mitigant (rev L451, L610) lacks the qualifier that the CFO letter is addressed to an unnamed ED, one of two (res L489; pres L201-213); the mitigant may be the addressee who held it 38 days. Loop A4."
    - "A5-M06: liquid-treasury flag (rev L246, L264, L453, L615, L479) lacks the attribution: Rs 11.05 cr (82%) of the Rs 13.39 cr fall is current investments moving inside the book (total book +8.24 on 1.03 net purchases + 7.21 gains), not cash spent; Rs 1.03 cr net purchases during Rs 2.87 cr new borrowing; name both readings and Q14/Q16 as separator. Loop A4."
  contradiction: []
  style: [A5-S19, A5-S20, A5-S21, A5-S22, A5-S23, A5-S24, A5-S25, A5-S26, A5-S27, A5-S28]
loop_back_to: "A4"
gap: "A5-F04 (FACTUAL): replace 'shows no price erosion / mix, not price' at rev L178, L508, L614, L625 with the bounded reading (H1 GM -613 bps on a 4.5 pp spares fall; mix at most ~285 bps even at a 100% spares margin; >= ~330 bps within-segment; trough-free Q1 -411 bps on 2.7 pp; residual = price, input cost or inside-equipment mix, unsplit; Q11 tests); align rev L148, L182, L394, L499-500. A5-M05 (MISSING): add to verdict item 2, flag and Step 0D that the CFO letter's addressee is an unnamed ED, one of two (res L489; pres L201-213), so the mitigant may sit inside the 38-day gap; Q9 asks which ED and the receipt date. A5-M06 (MISSING): add to the Step 5 liquid row, net-debt answer, verdict item 4, flag and summary that 82% (Rs 11.05 cr) of the Rs 13.39 cr liquid-net-cash fall is an inside-book shift from current to non-current investments, not cash spent, and that the company net-bought Rs 1.03 cr of investments while borrowing Rs 2.87 cr; name the liquidity-need and allocation-choice readings with Q14/Q16 as separator. Keep the summary within 20 lines."
style_notes:
  - "A5-S19: rounding drift from rounded inputs: H1 margin +122 vs +121.5 bps; Q2 ETR +263 vs +263.6 bps; net debt +2.20 vs +2.19; H1 FY27 dist+other 26.75 vs 26.74%. Compute from lakhs."
  - "A5-S20: FN20 cited for both the H1 FY26 investing misalignment (rev L20, L58, L235) and the EBITDA definition (rev L122, L403, L412); confirm the ID."
  - "A5-S21: rev L449 'two cell positions' understates the preamble's data corrections; reword."
  - "A5-S22: Reg 33 deadlines (rev L370, L433, L437, L511, L518) are statute, not filing; tag as rev L432 does."
  - "A5-S23: Q1 spares-share anchors should add res L359 and L362 (H1 segment labels)."
  - "A5-S24: rev L262 -6.6% uses filed 230.75 (res L154); the anchored deck figures give -6.5%; cite both."
  - "A5-S25: NFAT 2.22 basis unstated; ties to TTM revenue / (PPE + CWIP + intangibles); same basis gives FY26 3.11 vs deck 3.1."
  - "A5-S26: bull symmetry: Sep-25 book Rs 44 cr was 0.34x of H2 FY26 revenue; Sep-26 book is 0.77x of the H2 FY27 threshold."
  - "A5-S27: deck GM (pres L389) deducts manufacturing expense; filing basis does not (Q2 FY27 56.54% vs 59.88%); add one reconciling line."
  - "A5-S28: current provisions +29% (Rs 5.98 to 7.72 cr, res L262) absent from supporting stock items; candidate Q3 sub-question on warranty provisions."
analyst_note: "Loop 2 revision audited fresh. Gate, coverage and arithmetic pass: every derived figure was recomputed from lakhs, with no mismatch above rounding. Three findings loop to A4. F04: the 'mix, not price erosion' reading fails A4's own test. Under the A3-14 chart reading, Q1 FY27 vs Q1 FY26 gross margin fell 411 bps on a 2.7 pp spares shift. Even at a 100% spares margin, mix explains at most about half of the 613 bps H1 fall; at least about 330 bps is within-segment. The H1 and Q1 pairs are nearly free of inventory-build timing. The residual may be price, input cost or mix inside equipment, and the filing cannot split them. M05: the CFO letter is addressed to an unnamed Executive Director, and the board has two; the continuity mitigant may be the addressee. M06: 82% of the liquid-treasury fall is current investments moving inside the book, not cash spent, so the bear and allocation-choice readings both fit. The verdict class PROCEED WITH FLAGS is not challenged. The acquisition probe was not triggered: no deal is described."
```
