# A5 ADVERSARY / COMPLETENESS AUDIT: GHV Infra Projects Limited (GHVINFRA), Q2 FY27

Agent: A5 adversary | model: claude-opus-5-5 | run date: 2026-10-23
Instruction file: prompts/quarterly-a5-adversary.md
Inputs read (only these):
- A4 review: runs/ghvinfra-q2fy27/work/review_ghvinfra_q2fy27.md (805 lines)
- A1 fulltext (the spine): runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-fulltext.md (843 lines)
- A1 structured: runs/ghvinfra-q2fy27/extracted/ghvinfra-results-q2fy27-structured.md (R001-R821)
- A2 ledger: runs/ghvinfra-q2fy27/work/ledger_results_ghvinfra_q2fy27.md (253 rows)
Not opened: the source PDF and everything under inputs/. A3 reasoning was not read. Every figure below was re-derived from the fulltext.
Anchors: "l###" = fulltext line. "review l###" = A4 review line. Units: Rs Lakhs (L) as filed; Rs Cr = L x 0.01.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

DELIVERABLE-COMPLETENESS: PASS. All five labelled brief parts are present and carry real content.

| Brief part | Heading (review line) | Status | Content check |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (review l665) | present | 17 lines (review l667-683), inside the 10-20 line band. Numbers carry tiers. One dropped qualifier at review l677 (finding M4). |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (review l685) | present | 5 bullets. Filed West Asia quote ties to l483-484. Gaps are stated as NOT FOUND. |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (review l693) | present | 8 bullets. One factual slip at review l700 (finding F2). |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (review l704) | present | 5 bullets. Peer set NOT FOUND, stated honestly. |
| 5. Forward map | "### 5. FORWARD MAP" (review l712) | present | Make-or-break line plus 9 catalysts. Each row has a bull fork and a bear fork. 6 rows carry dates. 3 rows say "undated" or "NOT FOUND" because the filing gives no date (correct under the never-estimate rule). Row order is out of sequence (STYLE S2). |

Gate result: no part missing or empty. The gate does not fail.

---

## 1. COVERAGE AUDIT

### 1A. Fresh enumeration over the fulltext vs the A2 ledger

Method: grep and line-by-line sweep of the fulltext (l1-l843). Counts were taken without reference to the A2 counts, then diffed.

| Category | A2 count | A5 fresh count | Fresh-pass evidence | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes, standalone | 8 | 8 | l463, l467, l470, l476, l481, l491, l493, l494 | none | MATCH |
| Notes, consolidated | 11 | 11 | l765, l768, l770, l772, l775, l778, l783, l787, l795, l796, l797 | none | MATCH |
| Footnotes (EPS asterisk) | 2 | 2 | l356/l358; l660/l662 | none | MATCH |
| Line items, S P&L | 26 | 26 | l328-l357 value lines | L019-L022, L024 uncited; immaterial (OCI, FY26 other equity); blanket mark accepted | MATCH |
| Line items, S balance sheet | 35 | 35 | l371-l411 | L030 (l374); L055 (l405); L056 (l406) | MATCH, ORPHANS |
| Line items, S cash flow | 33 | 33 | l423-l457 | L074 (l435); L075 (l436); L080 (l442); L082 (l444) | MATCH, ORPHANS |
| Line items, C P&L | 36 | 36 | l620-l661 | L117-L128 uncited; OCI/FCTR and capital lines, immaterial; blanket mark accepted | MATCH |
| Line items, C balance sheet | 35 | 35 | l675-l715 | L134 (l678); L158 (l708) | MATCH, ORPHANS |
| Line items, C cash flow | 31 | 31 | l727-l759 | none material (see STYLE S7 on l729) | MATCH |
| Line items, total | 196 | 196 | 26 + 35 + 33 + 36 + 35 + 31 | 9 material orphans (1B) | MATCH, ORPHANS |
| Zero-standing cells | 41 | 41 | 39 dash cells on 24 lines (S P&L 6, S BS 4, S CF 9, C P&L 16, C BS 4) + 2 "Nil" at l572 | none | MATCH |
| Board agenda items | 4 | 4 | l42, l52, l60, l76 | none | MATCH |
| Annexures | 3 | 3 | l118, l174, l812 | none | MATCH |
| Auditor paragraphs | 11 | 11 | S l258, l266, l275, l296; C l514, l523, l531, l543, l561, l569, l591 | none | MATCH |
| Consolidation entities (excl. parent) | 4 | 4 | l545-l548; l770-l771 | none | MATCH |
| Turns / questions / slides | 0 | 0 | results filing | n/a | MATCH |
| Structured IDs referenced in ledger | 821 of 821 | 821 of 821 | every ID R001-R821 traced to a ledger row (NUMBER R001-R615, ENTITY R616-R696, FORWARD R697-R703, DATE R704-R745, QUALIFIER R746-R821) | orphan_ids [] confirmed | MATCH |

Fresh-pass units absent from the structured file:
- l640: a stray "EQUITY AND LIABILITIES" heading printed inside the consolidated P&L, between PAT (l639) and the JV share (l641). It carries no values. A1 captured the similar label slip at l655 (R795, ledger G05) but not this one. No number, fact or verdict depends on it. Logged as STYLE S4. No A2 loop.
- l479-480: "Mrs. Husena A. Musamji shall cease to be classified" is forward wording. It is captured as a qualifier (R768, R812; ledger F04, F15), not in the FORWARD table. A4 carries it as monitorable M6. No gap.

Result: no row exists in the fulltext that the ledger lacks. missing_from_ledger = [].

### 1B. Ledger rows vs A4 review (orphan test)

A4 cites by fulltext line, not by ledger ID. A4's preamble states "All 253 rows reviewed. No row is unreviewed" (review l17). A5 accepts that blanket mark as "reviewed, no finding" for boilerplate rows, for totals that tie, and for immaterial rows (OCI, CIN, UDIN, signatures). A5 does not accept it for rows that A2 flagged for A3/A4, or for rows whose filed content changes a statement A4 makes. Nine rows fail that test.

| Ledger row | Structured IDs | Fulltext line | Filed content | Why the blanket mark fails | Finding |
|---|---|---|---|---|---|
| L030 | R190-R191 | l374 | S Investments 985.12 L (Mar-26) to 1,189.90 L (Sep-26) | A2 key flag "Investments R190 vs R505" (ledger l24) is never addressed. The figure bounds the parent's Erisha exposure where A4 writes "parent exposure ND" (review l75) | M1 |
| L134 | R505-R506 | l678 | C Investments 0.50 L at both dates | Same A2 flag. 1,189.40 L (11.89 Cr) of S investments is eliminated on consolidation | M1 |
| L080 | R291-R292 | l442 | Investment in Equity Shares of Subsidiaries (204.78) L in H1 FY27 | Equals the full H1 rise in S investments. Fresh parent equity went into subsidiaries with Nil revenue and a 482.78 L H1 loss (l572-573). Not in A4 | M1 |
| L158 | R553-R554 | l708 | C other trade payables 11,686.62 L vs S 10,544.75 L (l404) | Subsidiaries owe 11.42 Cr to third parties. A4's "up to 40.52 Cr" exposure is gross of this. Not in A4 | M1 / M4 |
| L082 | R295-R296 | l444 | Deposits (Placed)/Matured with Others: +5,918.44 L H1 FY27; (960.00) L H1 FY26 | A 59.18 Cr inflow from unnamed "Others", larger than H1 capex 43.71 Cr. It bears on A4's inference that the 149.72 Cr non-current OFA fall is partly a reclassification (review l387). No question to management | M2 |
| L055 | R240-R241 | l405 | S Other Financial Liabilities 6,794.95 L to 9,758.29 L | +29.63 Cr. With L056 these lines total 171.87 Cr, more than trade payables of 158.48 Cr (l403-404). Absent from Step 5 and from A4's "missing evidence" list (review l408) | M3 |
| L056 | R242-R243 | l406 | S Other Current Liabilities 5,003.12 L to 7,428.62 L | +24.26 Cr. Composition (customer advances, retention, capital creditors, related-party balances) is a separating observation for the structural vs growth cash test | M3 |
| L074 | R279-R280 | l435 | CF increase in financial and other liabilities 3,227.61 L | Part of the 56.20 Cr liability cushion inside H1 WC | M3 |
| L075 | R281-R282 | l436 | CF increase in current liabilities and provisions 2,392.10 L | As L074 | M3 |

Coverage verdict: FAIL. 9 orphan rows. Loop to A3 (unreviewed rows, missed forensic), then A4.

---

## 2. ARITHMETIC AUDIT

Every derived metric in A4's tables was recomputed from the filed Lakh figures. "PASS" = matches within rounding (0.01 Cr, 0.01 pp or 1 bp). Two mismatches exceed rounding.

| Metric | A4 value | Recomputed (from Lakhs) | Source line | Status |
|---|---|---|---|---|
| S Op EBITDA Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27 (Cr) | 22.28 / 27.77 / 35.79 / 90.85 / 30.61 / 63.56 | 2,227.70 / 2,777.40 / 3,578.80 / 9,084.81 / 3,061.32 / 6,356.20 L | l329, l337, l338, l341 | PASS |
| S Op EBITDA margin, same columns | 12.12 / 12.71 / 11.93 / 15.00 / 11.59 / 12.25% | 12.122 / 12.705 / 11.926 / 15.003 / 11.586 / 12.254% | l328 | PASS |
| S Reported EBITDA and margin | 22.34-64.15 Cr; 12.15 / 12.84 / 12.03 / 15.07 / 11.61 / 12.37% | 2,233.57 / 2,805.72 / 3,608.87 / 9,123.60 / 3,068.27 / 6,414.59 L; Q1 margin 12.835% (boundary) | l337, l338, l341 | PASS |
| S Core PBT (ex-OI) | 15.79 / 15.24 / 21.77 / 56.89 / 22.10 / 37.01 | 1,578.86 / 1,524.43 / 2,176.91 / 5,689.44 / 2,209.93 / 3,701.34 L | l329, l341 | PASS |
| S OI / PBT | 0.37 / 1.82 / 1.36 / 0.68 / 0.31 / 1.55% | 0.370 / 1.824 / 1.362 / 0.677 / 0.314 / 1.553% | l329, l341 | PASS |
| S ETR | 29.19 / 27.52 / 16.70 / 26.23 / 28.09 / 21.17% | 29.187 / 27.517 / 16.700 / 26.234 / 28.095 / 21.167% | l341, l346 | PASS |
| S PAT margin | 6.11 / 5.15 / 6.13 / 6.98 / 6.03 / 5.71% | 6.107 / 5.149 / 6.126 / 6.978 / 6.033 / 5.714% | l328, l347 | PASS |
| S Gross margin after direct cost | 16.27 / 17.54 / 15.96 / 20.60 / 16.98 / 16.63% | direct cost 15,386.29 / 18,025.53 / 25,218.57 / 48,080.26 / 21,936.93 / 43,244.10 L; margins 16.272 / 17.541 / 15.961 / 20.598 / 16.977 / 16.627% | l332-l335 | PASS |
| S Op EBIT / finance cost | 3.45 / 2.27 / 2.64 / 2.77 / 3.62 / 2.46x | 3.454 / 2.267 / 2.644 / 2.765 / 3.623 / 2.464x | l337, l338 | PASS |
| WIP-adjusted Op EBITDA margin Q1 / Q2 FY27 | 6.53% (14.26 Cr) / 16.43% (49.30 Cr) | 1,426.39 L = 6.525%; 4,929.81 L = 16.428% | l335 | PASS |
| C Op EBITDA Q1 / Q2 / FY26 / H1; margin | 24.25 / 34.88 / 98.52 / 59.13; 11.09 / 11.62 / 16.01 / 11.40% | 2,424.69 / 3,488.12 / 9,851.73 / 5,912.81 L; 11.092 / 11.624 / 16.007 / 11.400% | l620-l633 | PASS |
| C Core PBT; OI/PBT | 11.52 / 20.66 / 64.49 / 32.19; 2.40 / 1.43 / 0.60 / 1.78% | 1,152.09 / 2,066.47 / 6,449.30 / 3,218.56 L; 2.399 / 1.434 / 0.598 / 1.782% | l621, l633 | PASS |
| C ETR | 36.20 / 17.58 / 24.11 / 24.29% | 36.197 / 17.579 / 24.112 / 24.285% | l633, l638 | PASS |
| C PAT margin incl. JV | 3.37 / 5.79 / 7.96 / 4.77% | 3.369 / 5.792 / 7.964 / 4.771% | l620, l642 | PASS |
| C minus S PAT Q1 / Q2 / FY26 / H1 | (3.89) / (1.00) / +6.76 / (4.90) | (389.05) / (100.47) / +676.28 / (489.52) L | l347, l642 | PASS |
| Gap as % of S PAT | -34.57 / -5.47 / +16.00 / -16.52% | -34.568 / -5.465 / +16.005 / -16.516% | l347, l642 | PASS (Q2 on the rounding boundary) |
| C minus S PBT | (3.72) / (1.10) / +7.60 / (4.83) | (372.34) / (110.44) / +759.86 / (482.78) L; Q2 and H1 tie exactly to the subsidiary losses at l573 | l341, l633, l573 | PASS |
| FY26 subsidiary PBT margin | 76% | 759.86 / 994.23 = 76.4% | l620, l328, l633, l341 | PASS |
| YoY Q2 S: revenue / Op EBITDA / margin / D&A / FC / EBIT / OI / core PBT / PBT / PAT / basic EPS / diluted EPS | +63.30 / +60.65 / -20 bps / +1,331% / +105.78 / +57.54 / +412.27 / +37.88 / +39.27 / +63.82 / +56.41 / +46.71% | +63.298 / +60.650 / -19.6 bps / +1,331.4 / +105.785 / +57.539 / +412.27 / +37.879 / +39.265 / +63.824 / +56.41 / +46.71% | l328-l357 | PASS |
| YoY H1 S: revenue / Op EBITDA / margin / FC / core PBT / PAT / EPS | +96.30 / +107.63 / +67 bps / +200.03 / +67.49 / +85.94 / +85.07% | +96.301 / +107.629 / +66.8 bps / +200.030 / +67.487 / +85.936 / +85.07% | l328-l356 | PASS |
| H2 FY26 S margin | 17.65% | 6,023.49 / 34,130.50 = 17.648% | l328, l341 | PASS |
| Q2 PAT at prior-year ETR / at 25.17% | 15.63 Cr (+39.27%) / 16.51 Cr (+47.16%) | 1,562.83 L / 1,651.48 L | l341, l346 | PASS |
| Tax-line share of the Q2 PAT gain | 2.76 Cr, 38.5% | 275.60 / 716.23 L = 38.48% | l341, l346, l347 | PASS |
| Finance cost share of Q2 Op EBITDA | 37.0% | 1,324.02 / 3,578.80 = 36.996% | l337 | PASS |
| Q1 FY26 derived revenue / margin / core PBT | 80.46 / 10.36% / 6.31 | 8,046.00 L / 10.361% / 631.07 L | l328 | PASS |
| Q2 FY26 vs Q1 FY26 revenue | +128.40% | +128.394% in Lakhs; +128.40% on Cr-rounded inputs | l328 | PASS (rounding) |
| H2 FY26 per-quarter avg vs Q2 FY26; Q1 FY27 vs H2 avg; Q2 vs Q1 FY27 | -7.14% / +28.10% / +37.28% | -7.136% / +28.096% / +37.275% | l328 | PASS |
| C Q2 vs Q1: core PBT / PAT | +79.37% / +136.00% | +79.366% / +135.999% | l633, l642 | PASS |
| H1 FY27 margin gap to H2 FY26 | 540 bps | 539.4 bps | derived | PASS (rounding) |
| Q2 PAT bridge: revenue / margin / D&A / FC / OI / volume tax / ETR | +14.10 / (0.59) / (0.72) / (6.81) / +0.24 / (1.82) / +2.76 = +7.16 | +1,410.05 / -58.95 / -72.43 / -680.62 / +24.20 / -181.62 / +275.60 = +716.23 L; delta PBT 622.25 L | l328-l347 | PASS |
| H1 PAT bridge | +29.48 / +3.47 / (1.18) / (16.85) / +0.51 / (4.33) / +2.60 = +13.70 | +2,948.13 / +346.75 / -118.37 / -1,685.10 / +51.44 / -433.46 / +260.47 = +1,369.86 L | l328-l347 | PASS |
| Recurring share of the Q2 PAT gain | 58% (4.16 of 7.16) | 416.43 / 716.23 L = 58.1% | derived | PASS |
| S CFO / PAT H1 FY26 / H1 FY27; C H1 | -9.57x / -8.24x; -9.97x | -9.568 / -8.245; -9.973x | l439, l347, l742, l642 | PASS |
| S FCF H1 FY26 / H1 FY27; change; C FCF | (153.33) / (288.08); 134.75; (290.14) | (15,333.23) / (28,807.65) L; 134.74; (29,014.07) L | l439, l441, l742, l744 | PASS (rounding) |
| WC change H1 FY26 / ex-borrowing / H1 FY27 | (178.22) / (222.89) / (301.79) | (17,821.51) / (22,289.01) / (30,179.05) L | l428, l433, l437 | PASS |
| Receivable days; with current OFA | 70.04 / 94.38; 144.79 / 253.90 | 70.04 / 94.38; 144.79 / 253.90 | l381, l384, l328 | PASS |
| Inventory days; payable days; CCC | 13.33 / 8.52; 107.79 / 67.07; -24.42 / 35.83 | 13.33 / 8.52; 107.79 / 67.07; -24.42 / 35.83 | l380, l403-l404, l332-l335 | PASS |
| S gross debt; net debt (base / lien case); ND/E | 191.61 / 411.77; 182.65 / 388.24 / 410.39; 1.48 / 1.91 / 2.02x | 19,161.45 / 41,176.57; 18,265.34 / 38,823.98 / 41,039.18 L; 1.479 / 1.911 / 2.020x | l382-l383, l393, l396, l402 | PASS |
| C gross debt; net debt; ND/E; TR days | 191.70 / 411.86; 182.73 / 388.33; 1.39 / 1.88x; 75.15 / 98.19 | 19,169.72 / 41,186.37; 18,272.68 / 38,832.96 L; 1.390 / 1.882x; 75.15 / 98.19 | l685-l706 | PASS |
| Net rise in total other financial assets | 178.42 Cr | 46,285.38 - 28,443.58 = 17,841.80 L | l375, l384 | PASS |
| Unreviewed subsidiary assets as % of C equity | 19.75% | 4,075.53 / 20,638.72 = 19.747% | l572, l697 | PASS |
| Unreviewed share of H1 C PAT (review l102, subsidiaries plus JV) | 19.78% | (482.78 + 6.74) / 2,474.39 = 19.784% | l573, l578, l642 | PASS |
| Q6: unreviewed subsidiaries' H1 loss as % of H1 C PAT (review l579, l754) | 19.78% | 482.78 / 2,474.39 = 19.51%. 19.78% holds only if the unreviewed JV loss (6.74 L, l578) is added | l573, l642 | FAIL (FACTUAL F1) |
| C-over-S assets reconciled to the subsidiaries | 40.52 Cr | (27,830.33 - 26,749.99) + (15,189.67 - 12,218.10) = 4,051.91 L | l381, l386, l685, l690 | PASS (qualifier issue M4) |
| S-over-C current OFA | 13.50 Cr | 45,214.27 - 43,864.36 = 1,349.91 L | l384, l688 | PASS |
| Finance cost annualised / closing debt | 12.86% | 5,296.08 / 41,176.57 = 12.862% | l337, l396, l402 | PASS |
| Pre-allotment shares; Q2 denominator rise; pending dilution; fully diluted | 7,20,75,000; +11.56%; +13.58%; 9,13,25,000 | 3,603.75 L / Rs 5; 83,33,335 / 7,20,75,000 = 11.562%; 1,09,16,665 / 8,04,08,335 = 13.576% | l353, l472-l475 | PASS |
| Warrant count reconciliation | 16,66,667 x 5 = 83,33,335; x Rs 400 = 66.67 Cr | confirmed; 6,666.67 L / 83,33,335 = Rs 80.00 a share | l448, l470-l472 | PASS |
| Q2 basic EPS; H1 EPS on Q2 weighting (S / C) | 2.44; 4.02 / 3.36 vs printed 4.09 / 3.43 | 1,838.43 L / 75,245,291 (35-day weight) = 2.443; 2,963.91 L / 73,668,825 = 4.023; 2,474.39 L / 73,668,825 = 3.359 | l347, l356, l642, l660 | PASS (confirms FN14) |
| Basic-diluted spread Q2 FY26 / Q2 FY27 (S) | 2.6% / 8.6% | 2.56% / 8.61% | l356, l357 | PASS |
| Pending warrant inflow | about 65.50 Cr | 21,83,333 x Rs 400 x 75% = 6,549.999 L | l475, l448 | PASS |
| TTM S PAT; market cap; FD market cap; P/E | 55.95; 1,921.76; 2,182.67; 34.35x | 5,595.36 L; 8,04,08,335 x 239; 9,13,25,000 x 239; 34.35x | l347, l475 (CMP from A4 Notion) | PASS |
| Op EBIT H1; capital employed; spot ROCE | 62.29; 615.08; 20.25% | 6,228.86 L; 61,507.85 L; 20.254% | l337, l338, l393, l396, l401, l402 | PASS |
| Brief: sub-contracting / materials share of H1 revenue; H1 FY26 materials / construction; H1 FY27 construction | 51.81 / 28.84%; 2.16 / 24.80%; 2.72% | 51.806 / 28.844%; 2.161 / 24.802%; 2.723% | l328, l332-l334 | PASS |
| Brief: FY26 subsidiary direct cost (review l700) | "no direct cost" | 69.95 L construction (l625 1,101.69 less l333 1,031.74) less 0.47 L WIP (l627 vs l335) = 69.48 L = 0.69 Cr, 7.0% of the 9.94 Cr revenue | l333, l335, l625, l627 | FAIL (FACTUAL F2) |
| Equity change bridge | +79.62 = "50.00 + 29.64" | 7,962.09 L actual; 5,000.00 + 2,963.53 (TCI) = 7,963.53 L; 1.44 L residual | l393, l347, l352, l448-l449 | PASS (immaterial) |

Filing integrity checks run in support (no A4 claim depends on them): S Q2 total expenses and PBT tie (l332-l341). S CF sections tie; H1 FY26 cash used in operations sums to 14,760.20 L vs 14,760.19 printed, financing to 19,042.10 vs 19,042.11 (filing rounding). C CF ties in every section. C CF adds back finance cost of 2,527.52 L (l729), the standalone figure, against the C P&L 2,529.38 L (l629) (STYLE S7).

Arithmetic verdict: FAIL on two FACTUAL items (F1, F2). All other derived metrics pass.

---

## 3. ADVERSARIAL READ

The three most positive claims in A4's review are tested below. Each bear counter is built from the A1 extract. The mandatory acquisition-economics probe applies because the filing describes a stake purchase (the promoter's warrant conversion, l470-475) and a capital infusion into subsidiaries (l442).

### Claim 1. Revenue growth is strong and stepping up
A4 text: "Strong growth" (review l238); "revenue is STEPPING UP" (review l305); "Where GHV wins: it grew revenue 96.30% in H1" (review l707).

Strongest bear counter: H1 FY27 standalone cash flow shows a 151.30 Cr increase in trade receivables (l429) and a 220.60 Cr increase in financial and other assets (l432). Together that is 371.90 Cr. It equals 71.7% of H1 revenue of 518.68 Cr (l328) and 146% of the 254.46 Cr YoY revenue increase. On this reading the incremental revenue has not turned into cash. Payer identity is not disclosed in the filing.
Symmetric check: the same ratio was 94.8% in H1 FY26 (l429, l431, l432 against l328: 250.43 Cr on 264.23 Cr). Conversion improved, but it is still deeply negative.
Survives? YES. Already incorporated? YES in substance: Step 5 (review l362-371), the brief summary (review l667) and the Competition bullet that follows (review l708). Graft required: none. Optional in-cell qualifier on the Step 2 verdict (STYLE S6).

### Claim 2. "The headline is real at the core level" (standalone core PBT +37.88%)
A4 text: review l245 ("Real growth"), review l273.

Strongest bear counter: standalone core PBT is "real" only if the parent's carrying values in its subsidiaries hold. Note 5 sits in the STANDALONE results and states that no provision is recognised in the standalone results (l486-487). So the parent itself carries Erisha exposure. A4 records "parent exposure ND" (review l75). The extract bounds it:
- S Investments are 1,189.90 L (l374). C Investments are 0.50 L (l678). So 1,189.40 L (11.89 Cr) is eliminated on consolidation. This is the parent's cost of investment, predominantly in the subsidiaries [INFERENCE; C carries equity-accounted JVs at 0.50 L at most].
- The whole H1 rise in S Investments (204.78 L) is "Investment in Equity Shares of Subsidiaries" (l442). The parent put 2.05 Cr of fresh equity into subsidiaries with Nil revenue (l572) and a 482.78 L H1 loss (l573), in the half when the only named contract ended (l481-484).
- S current other financial assets exceed C by 1,349.91 L (13.50 Cr) (l384 vs l688). A4 derives this itself at Q4 (review l577) but does not carry it into the exposure line. Probable intercompany balance [INFERENCE].
- Bounded parent exposure: 11.89 + 13.50 = up to 25.39 Cr [derived]. That is 68.6% of H1 FY27 S core PBT of 37.01 Cr and 85.7% of H1 S PAT of 29.64 Cr.
- Symmetric qualifier: at group level the "up to 40.52 Cr" is gross. The subsidiaries carry 11.42 Cr of third-party trade payables (l708 11,686.62 L vs l404 10,544.75 L). Net group exposure is about 29.10 Cr [derived].
Acquisition-economics probe (subsidiary infusion): price / target PAT = 2.05 Cr / (4.83) Cr H1 loss. The multiple is negative, so no earnings case exists. Quality markers: revenue Nil, numbers not reviewed (l569-571), net cash flow (0.12) L (l576), only named contract ended. Bear reading: the parent is funding losses or dispute costs [INFERENCE]. No reading in the extract makes the infusion an earnings purchase.
Survives? YES. Incorporated? NO. Graft required (finding M1): replace "parent exposure ND" at review l75 with the bounded figure. Carry it into Flag 1 (review l648), Q4 (review l577) and the Erisha rows of the forward map (review l720-721). Show gross and net group exposure side by side.

### Claim 3. Promoter capital in; warrant conversion is a bull outcome
A4 text: "S3 (promoter capital in, more dilution pending)" (review l97); equity bridge "promoter warrant money 50.00" (review l379); forward-map bull fork "Promoter pays about Rs 65.50 Cr, debt falls" (review l722); Q12 bull answer "Dated, promoter confirms" (review l585).

Mandatory acquisition-economics probe (the promoter's stake purchase):
- Price paid: 6,666.67 L (l448) for 83,33,335 shares (l472) = Rs 80.00 a share [derived]. That is Rs 400 a warrant at 1:5 (l472-473).
- Against the company's filed earnings: Rs 80 / FY26 S basic EPS Rs 5.86 (l356) = ~13.65x. Rs 80 / TTM S EPS Rs 6.96 [derived: 55.95 Cr / 8,04,08,335] = ~11.5x. Rs 80 / FY26 C EPS Rs 6.80 (l660) = ~11.8x.
- Against book: Sep-26 S BVPS Rs 25.26 [derived: 20,313.57 L (l393) / 8,04,08,335] gives 3.17x book.
- Against A4's own market figures: Rs 80 is 33.5% of the Rs 239 CMP A4 quotes (review l35, Notion, SECONDARY). The promoter paid ~11.5x TTM earnings. The market pays 34.35x (review l536).
- Quality markers at purchase: H1 S CFO (244.37) Cr (l439); net debt/equity 1.91x [derived]; Q2 interest cover 2.64x [derived]. Representativeness: FY26 EPS rests on an H2 FY26 margin of 17.65% that H1 FY27 did not repeat (12.25%). The earnings year may be a peak.
- Pending tranche: 21,83,333 warrants give 1,09,16,665 shares (l475). At the same Rs 80 [INFERENCE: the filing states no separate price], total consideration is ~87.33 Cr, of which the 65.50 Cr balance is A4's figure. At Rs 239 those shares are worth ~260.91 Cr, a ~173.6 Cr gap. The converted tranche already shows a ~132.50 Cr gap (199.17 Cr at CMP vs 66.67 Cr paid).
- Funding effect: 65.50 Cr would retire 17.3% of the 377.90 Cr current borrowings (l402).
Why is it cheap? The warrant price was fixed at warrant allotment. That date and price are NOT FOUND in this filing. Two readings: (a) the stock re-rated after issue, and the promoter captures that re-rating through a fixed-price option at the cost of minority holders; (b) the price was fair at issue and the CMP is the outlier. The separating observation is the warrant allotment date and the ICDR floor price on that date. Neither is in the filing.
Survives? YES. The extract cannot show that the multiple is fair. Incorporated? NO. Graft required (finding M5): add the conversion price and multiples to Step 0C (review l59-63), Q12 (review l585) and the forward-map warrant row (review l722). The bull fork must state the dilution price next to the cash inflow.

---

## FINDINGS REGISTER (tagged)

| ID | Type | Agent | Gap (exact) | Anchors |
|---|---|---|---|---|
| F1 | FACTUAL | A4 | Q6 says the unreviewed subsidiaries' "H1 loss is 19.78% of H1 C PAT". The subsidiaries' loss is 482.78 L = 19.51% of 2,474.39 L. 19.78% is subsidiaries plus the unreviewed JV (489.52 L). Fix the number or the label in the table and the YAML question | review l579, l754; fulltext l573, l578, l642 |
| F2 | FACTUAL | A4 | Brief says FY26 subsidiary revenue of 9.94 Cr had "no direct cost". The subsidiaries carried 0.69 Cr of construction expense, net of WIP (7.0% of revenue). Step 1-G (review l226) and Q20 correctly say zero materials and zero sub-contracting | review l700; fulltext l333, l335, l625, l627 |
| M1 | MISSING | A3, then A4 | Orphan rows L030, L134, L080, L158. A2 key flag "Investments R190 vs R505" was never addressed. Parent Erisha exposure is bounded at up to 25.39 Cr (11.89 Cr investments eliminated on consolidation, of which 2.05 Cr was invested in H1, plus 13.50 Cr S-over-C current OFA), not "ND". The group "up to 40.52 Cr" is gross of 11.42 Cr subsidiary payables. Surviving bear counter to Claim 2 | review l75, l577, l648, l720-721; fulltext l374, l384, l404, l442, l486-487, l572-573, l678, l688, l708 |
| M2 | MISSING | A3, then A4 | Orphan row L082. Deposits of 59.18 Cr matured from unnamed "Others" in H1 FY27 (9.60 Cr placed in H1 FY26). The counterparty is not named. This bears on A4's inference that the non-current OFA fall is a reclassification. Needs a forensic read and a management question (who are the "Others", is any a related party, where did the deposits sit at Mar-26) | review l387, l580; fulltext l375, l384, l444 |
| M3 | MISSING | A3, then A4 | Orphan rows L055, L056, L074, L075. Other financial liabilities (97.58 Cr) and other current liabilities (74.29 Cr) total 171.87 Cr, up 53.89 Cr in H1 (CF cushion 56.20 Cr). That exceeds trade payables of 158.48 Cr. They are absent from Step 5 and from the list of separating evidence for the structural vs growth cash test. Their composition (customer advances from the parent, retention, capital creditors) is a separating observation | review l362-389, l408; fulltext l403-406, l435-436 |
| M4 | MISSING | A4 | Summary narrative "About Rs 40.52 Cr of subsidiary assets depend on that dispute (FILED, derived)" drops "up to" (used at review l75, l648, l720). It tiers the Erisha linkage as FILED, but the extract supports only the C-over-S asset difference, with no attribution to Erisha [INFERENCE]. Restore "up to" and the INFERENCE tag. Optionally add the net figure (about 29.10 Cr after 11.42 Cr subsidiary payables) | review l677; fulltext l381, l386, l685, l690, l404, l708 |
| M5 | MISSING | A4 | Surviving bear counter to Claim 3 (mandatory acquisition-economics probe). Promoter converted at Rs 80.00 a share (6,666.67 L / 83,33,335), about 13.65x FY26 S EPS, 11.5x TTM S EPS, 3.17x BVPS, and 33.5% of A4's CMP of Rs 239. The pending 1,09,16,665 shares on the same terms come to about 87.33 Cr against about 260.91 Cr at CMP. The 65.50 Cr balance covers 17.3% of current borrowings. A4 frames conversion only as a bull funding event | review l59-63, l97, l585, l722; fulltext l356, l393, l402, l448, l472-475 |
| S1-S7 | STYLE | none | See STYLE NOTES | as listed |

No CONTRADICTION finding is raised separately. One internal inconsistency sits inside M1: A4 states "parent exposure ND" at review l75 but derives a parent-side 13.50 Cr at Q4 (review l577). M1's fix resolves it.

---

## VERDICT

VERDICT: INCOMPLETE.

- Failing agent (first in chain): A3. Gap: forensic read of orphan ledger rows L030, L134, L080, L158 (parent-level Erisha exposure), L082 (59.18 Cr deposits matured from "Others") and L055, L056, L074, L075 (171.87 Cr of non-trade operating liabilities). Type: MISSING.
- Then A4. Gaps: (1) replace "parent exposure ND" with the bounded parent and net group exposure (M1); (2) restore "up to" and the INFERENCE tag in the summary (M4); (3) graft the promoter conversion economics (M5); (4) correct Q6 to 19.51% for the subsidiaries alone, or relabel it (F1); (5) correct the brief's "no direct cost" to 0.69 Cr of construction cost (F2). Types: MISSING, FACTUAL.
- Not affected: the deliverable gate passes. The enumeration matches A2 in every category. About 200 other derived figures recompute within rounding. None of the findings changes the Decision Status framing (AVOID), the protocol verdict ceiling, or the cash conversion classification. They change what the record says about Erisha exposure and promoter dilution.

---

## STYLE NOTES (logged; no loop)

- S1. Prior-question row 6 (review l119) cites l70 for "Formerly Sindu Valley Technologies Limited". l70 is the registered-office footer. The phrase appears at l101, l257 and l320. A1's R626 carries the same mis-anchor. Fix the anchor only.
- S2. Forward map (review l716-726): the "by 14-Aug-2027" row sits after the "about 22-Aug-2027" row. Put the rows in date order.
- S3. Monitorable M3 (review l618) says the Erisha contract end is "completed". The filing says "concluded ... due to prolonged delays" (l482-483). Use "ended early" so that no reader takes it as executed to completion.
- S4. l640 prints a stray "EQUITY AND LIABILITIES" heading inside the consolidated P&L. It is not captured in the structured file or the ledger, unlike the l655 label slip (R795, G05). Add it to the drafting-hygiene record at the next A1/A2 pass. No values are attached. Watchlist item 7 is already RED.
- S5. Rounding-level differences, no action: Q2 gap -5.47% (exact -5.465%); Q2 FY26 QoQ +128.40% (+128.39% in Lakhs); 540 bps (539 bps); FCF change 134.75 (134.74); equity bridge 79.64 vs 79.62 actual.
- S6. The Step 2 revenue verdict "Strong growth" (review l238) and the Competition line "Where GHV wins" (review l707) could carry the cash qualifier in the cell itself (WC build of 371.90 Cr = 71.7% of H1 revenue). The substance is already in Step 5 and the brief.
- S7. The consolidated cash flow adds back finance cost of 2,527.52 L (l729), the standalone figure, against the consolidated P&L 2,529.38 L (l629). The difference is 1.86 L. It is a drafting item for the watchlist item 7 list. No A4 number or conclusion moves.

---

```yaml
stage: A5-adversary
company: "GHVINFRA"
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
  orphan_rows:
    - "L030 (R190-R191, l374) S Investments 985.12 to 1,189.90 L; A2 key flag 'Investments R190 vs R505' never addressed"
    - "L134 (R505-R506, l678) C Investments 0.50 L; 11.89 Cr eliminated on consolidation"
    - "L080 (R291-R292, l442) Investment in Equity Shares of Subsidiaries 204.78 L in H1 FY27"
    - "L158 (R553-R554, l708) C other trade payables 11.42 Cr above S (l404); 40.52 Cr exposure is gross"
    - "L082 (R295-R296, l444) Deposits matured with Others +5,918.44 L H1 FY27; counterparty unnamed"
    - "L055 (R240-R241, l405) S Other Financial Liabilities 6,794.95 to 9,758.29 L"
    - "L056 (R242-R243, l406) S Other Current Liabilities 5,003.12 to 7,428.62 L"
    - "L074 (R279-R280, l435) CF increase in financial and other liabilities 3,227.61 L"
    - "L075 (R281-R282, l436) CF increase in current liabilities and provisions 2,392.10 L"
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "Q6 unreviewed subsidiaries' H1 loss as % of H1 C PAT"
    a4_value: "19.78%"
    recomputed: "19.51% (482.78 / 2,474.39 L); 19.78% only with the unreviewed JV loss 6.74 L added"
    source_line: "fulltext l573, l578, l642; review l579, l754"
  - metric: "FY26 subsidiary direct cost (brief, business model)"
    a4_value: "no direct cost"
    recomputed: "0.69 Cr (construction 1,101.69 - 1,031.74 = 69.95 L, less WIP 0.47 L) = 7.0% of 9.94 Cr revenue"
    source_line: "fulltext l333, l335, l625, l627; review l700"
surviving_bear_counters:
  - claim: "Revenue growth strong and stepping up (+63.30% Q2 YoY, +96.30% H1)"
    counter: "H1 receivables +151.30 Cr and financial/other assets +220.60 Cr = 371.90 Cr, 71.7% of H1 revenue and 146% of the YoY revenue increase; already carried in Step 5 and the brief"
    source_line: "fulltext l328, l429, l432; review l238, l305, l707"
    type: STYLE
  - claim: "Standalone core PBT +37.88%: 'the headline is real at the core level'"
    counter: "Standalone results carry unprovided Erisha exposure (note 5, l486-487): 11.89 Cr investments eliminated on consolidation (2.05 Cr added in H1 into Nil-revenue, loss-making subsidiaries) plus 13.50 Cr S-over-C current OFA = up to 25.39 Cr, 68.6% of H1 S core PBT; A4 writes 'parent exposure ND'"
    source_line: "fulltext l374, l384, l442, l486-487, l572-573, l678, l688; review l75, l245, l273"
    type: MISSING
  - claim: "Promoter capital in; warrant conversion as a bull funding event (about 65.50 Cr, debt falls)"
    counter: "Conversion at Rs 80.00 a share (6,666.67 L / 83,33,335) = ~13.65x FY26 S EPS, ~11.5x TTM S EPS, 3.17x BVPS, 33.5% of A4's CMP Rs 239; pending 1,09,16,665 shares on the same terms ~87.33 Cr vs ~260.91 Cr at CMP; 65.50 Cr = 17.3% of current borrowings"
    source_line: "fulltext l356, l393, l402, l448, l472-475; review l97, l585, l722"
    type: MISSING
findings_by_type:
  factual:
    - "F1 (A4): Q6 attributes 19.78% of H1 C PAT to the subsidiaries' loss; actual 19.51% (review l579, l754; l573, l642)"
    - "F2 (A4): brief says FY26 subsidiary revenue had no direct cost; actual 0.69 Cr construction cost net of WIP (review l700; l333, l625)"
  missing:
    - "M1 (A3 then A4): orphan rows L030/L134/L080/L158; parent Erisha exposure bounded at up to 25.39 Cr, not ND; group 40.52 Cr is gross of 11.42 Cr subsidiary payables"
    - "M2 (A3 then A4): orphan row L082; 59.18 Cr deposits matured from unnamed Others, unread, no management question"
    - "M3 (A3 then A4): orphan rows L055/L056/L074/L075; 171.87 Cr non-trade operating liabilities absent from Step 5 and the separating-evidence list"
    - "M4 (A4): summary l677 drops 'up to' on 40.52 Cr and tiers the Erisha linkage as FILED instead of INFERENCE"
    - "M5 (A4): promoter conversion economics (Rs 80 a share, 13.65x FY26 EPS, 33.5% of CMP) absent from 0C, Q12 and the forward-map warrant row"
  contradiction: []
  style:
    - "S1: review l119 cites l70 for 'Formerly Sindu Valley'; correct anchors l101, l257, l320"
    - "S2: forward map rows out of date order (14-Aug-2027 after 22-Aug-2027)"
    - "S3: monitorable M3 'completed' should read 'ended early' (l482-483)"
    - "S4: stray 'EQUITY AND LIABILITIES' heading at l640 inside the C P&L not captured as a label anomaly"
    - "S5: rounding-level differences only (-5.47 vs -5.465%, 128.40 vs 128.39%, 540 vs 539 bps, 134.75 vs 134.74, 79.64 vs 79.62)"
    - "S6: Step 2 'Strong growth' cell and Competition 'Where GHV wins' could carry the cash qualifier in-cell"
    - "S7: C CF finance cost add-back 2,527.52 L (l729) vs C P&L 2,529.38 L (l629); 1.86 L drafting item"
loop_back_to: "A3"
gap: "A3: forensic read of orphan ledger rows L030, L134, L080, L158 (parent-level Erisha exposure: 11.89 Cr investments eliminated on consolidation, 2.05 Cr H1 infusion, 13.50 Cr S-over-C current OFA, 11.42 Cr subsidiary payables), L082 (59.18 Cr deposits matured from unnamed Others) and L055, L056, L074, L075 (171.87 Cr non-trade operating liabilities) [MISSING]. Then A4: replace 'parent exposure ND' (review l75) with the bounded figure and gross/net group exposure; restore 'up to' and the INFERENCE tag at review l677 [MISSING]; graft promoter conversion economics into 0C, Q12 and review l722 [MISSING]; correct Q6 19.78% to 19.51% for subsidiaries alone (review l579, l754) [FACTUAL]; correct review l700 'no direct cost' to 0.69 Cr construction cost [FACTUAL]."
style_notes:
  - "S1: fix anchor l70 to l101/l320 for 'Formerly Sindu Valley' (review l119)"
  - "S2: reorder forward-map rows by date"
  - "S3: 'completed' to 'ended early' at monitorable M3"
  - "S4: log l640 stray heading in the drafting-hygiene record"
  - "S5: rounding-level differences, no action"
  - "S6: optional in-cell cash qualifier on the Step 2 revenue verdict"
  - "S7: add the C CF finance cost add-back mismatch (1.86 L) to the drafting list"
analyst_note: "Arithmetic is clean. About 200 derived figures recompute within rounding. Two factual slips: Q6 gives the subsidiaries 19.78% of H1 C PAT (19.51% actual), and the brief says FY26 subsidiary revenue had no direct cost (0.69 Cr actual). The real gap is coverage. A5 accepts A4's blanket 'all 253 rows reviewed' only for boilerplate and immaterial rows. A2 flagged 'Investments R190 vs R505', and nobody read it. The parent carries 11.89 Cr of investments eliminated on consolidation (2.05 Cr added in H1 into revenue-less, loss-making subsidiaries) plus 13.50 Cr of S-over-C current financial assets. That bounds a standalone Erisha exposure at up to 25.39 Cr, where A4 writes 'ND'. The 59.18 Cr deposit maturity from unnamed 'Others' and 171.87 Cr of non-trade liabilities are also unread. Symmetric point: the 40.52 Cr group figure is gross of 11.42 Cr of subsidiary payables. The promoter converted at Rs 80 a share, a third of the CMP A4 quotes. That makes the warrant bull fork a value-transfer question. None of this moves the AVOID record."
```
