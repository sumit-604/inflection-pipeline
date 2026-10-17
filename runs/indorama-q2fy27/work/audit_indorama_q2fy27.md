# A5 ADVERSARY / COMPLETENESS AUDIT: Indo Rama Synthetics (India) Ltd (INDORAMA), Q2 FY27

Auditor: A5 adversary. Model: claude-opus-5-5. Date: 2026-10-17. Fresh context.
Under audit: runs/indorama-q2fy27/work/review_indorama_q2fy27.md ("review L" = line in that file).
Inputs read: three A1 fulltexts (RF = results, PR = press release, CX = capex letter), three A1 structured files, three A2 ledgers. No source PDF and nothing under inputs/ was opened. A3 files were not read. Every number below was re-derived from the A1 fulltext VER- lines (RF L196-222, L288-323, L374-407, L590-622, L680-714, L767-799) and the PR/CX text.

---

## DELIVERABLE-COMPLETENESS AUDIT (gate, run first)

| Brief part | Location | Status |
|---|---|---|
| (1) Summary narrative | review L661-669 (8 source lines, about 19 sentences, about 250 words) | PRESENT, real content |
| (2) Sector intelligence | review L671-672 | PRESENT, real content |
| (3) Business-model intelligence | review L674-676 | PRESENT, real content |
| (4) Competition intelligence | review L678-679 | PRESENT, real content |
| (5) Forward map | review L681-689: make-or-break reading plus 7 dated catalysts (M1/M2, M4, M5/M6, M3, M7, M8, M9), each with a Bull and a Bear fork | PRESENT, real content |

**DELIVERABLE-COMPLETENESS AUDIT: PASS. Narrative present; sector present; business model present; competition present; forward map present.**

---

## AUDIT 1: COVERAGE

Fresh enumeration was run by grep over the A1 FULLTEXTS (the spine), then diffed against the A2 ledgers and the A1 structured files.

### 1A. Counts

| Document | Category | A2 count | Fresh count (method) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Notes | 12 | 12: numbered Notes 1-4 at RF L415, L419, L423, L428 (S) and L805, L810, L817, L822 (C); table labels at L225, L326, L625, L717 | none | PASS |
| Results | Line items (VER rows) | 198 | 198: VER-3 27 + VER-4 36 + VER-5 34 + VER-9 33 + VER-10 35 + VER-11 33 | none | PASS |
| Results | Table cells | 626 (R001-R626) | 626: 157 + 72 + 68 + 193 + 70 + 66 | none | PASS |
| Results | Zero-standing cells | 85 | 85: VER-3 28, VER-4 1, VER-5 2 (incl. "0.00" at L399), VER-9 49, VER-10 2, VER-11 3 | none | PASS |
| Results | Agenda items | 2 | 2: items a) L49, b) L57 | none | PASS |
| Results | Auditor paragraphs | 10 | 10: S paras 1-4 (L100, L106, L113, L124); C paras 1-5 (L459, L467, L475, L491, L510) plus unnumbered SEBI 33(8) para (L487) | none | PASS (A2 groups by signature block, not by paragraph; totals agree; see STYLE S5) |
| Results | Entities | 24 | 24 (R643-R666; four subsidiaries at L506-509) | none | PASS |
| Results | Forward items | 2 | 2 (L58, L60) | none | PASS |
| Results | All IDs | 721 in ledger | 721 in structured (grep count of R### rows) | none | PASS |
| Press release | Pages / slides | 3 | 3 (page markers L17, L69, L125) | none | PASS |
| Press release | Table line items | 6 | 6 (L96, L98, L100, L102, L104, L106); 42 cells = R033-R074 | none | PASS |
| Press release | Forward items | 3 | 3 (L138, L139, L140) | none | PASS |
| Press release | Notes / auditor paras / agenda | 0 / 0 / 0 | 0 / 0 / 0 | none | PASS |
| Press release | All IDs | 132 | 132 | none | PASS |
| Capex letter | Agenda items | 1 | 1 (L36-44) | none | PASS |
| Capex letter | Entities | 12 | 12 (R018-R029) | none | PASS |
| Capex letter | Forward items | 5 | 5 (L39, L41, L42, L43 twice) | none | PASS |
| Capex letter | Notes / line items | 0 / 0 | 0 / 0 | none | PASS |
| Capex letter | All IDs | 47 | 47 | none | PASS |
| All | Turns (concall) | 0 | 0 (no transcript in --docs) | none | PASS |

Value spot-check of OCR-vs-image conflicts (structured file uses the image-verified value in each case; all foot to filed totals):
- S Q2 FY27 change in inventories: OCR "47.98" (RF L163) vs VER 17.98 (L201). 942.04 + 42.11 + 17.98 + 30.12 + 128.76 = 1,161.01 = L204. VER correct; R031 = 17.98.
- S H1 FY26 purchase of stock-in-trade: OCR "92.11" (L162) vs VER 12.11 (L200). Foots to 2,216.58 (L204). R029 = 12.11.
- S H1 FY26 other income and revenue: VER 8.37 and 2,351.23 foot to total income 2,359.60 (L198).
- C FY26 employee cost: OCR "126.31" (L548) vs VER 125.31 (L596). Foots to 4,560.76 (L598).
- C Q2 FY27 operating profit: OCR "117.68" (L554) vs VER 117.66 (L599) = 1,344.04 - 1,226.38.
- C total assets 31-Mar: OCR 3,244.08 vs VER 3,244.09 = 1,571.83 + 1,672.26.

### 1B. Fresh-pass units not represented in the structured file
- RF L106-111 and L467-473 (auditor paragraph 2, both reports: management responsibility, Ind AS 34 framework). No dedicated structured row. Boilerplate with no number a conclusion depends on. Logged as STYLE S5, no loop.
- PR L77-78 ("a leading integrated polyester manufacturer in India"). Partly captured: R024 (issuer, L77) and R119 ("integrated manufacturing platform", L147). Not a FAIL. Bears on STYLE S3.
No other fresh-pass unit is missing. **missing_from_ledger: none.**

### 1C. Ledger row to review trace
A4's preamble (review L17-23) marks 721/721, 132/132 and 47/47 rows reviewed. Every A2-flagged row was checked for a body anchor:
- R688 MISMATCH_NOTE (heading "Audited", body "Un-audited"): review L85 (A3-13). Traced.
- R659-R662 ENTITY_CHANGE_UNKNOWN: review L86, Q17 L586. Traced.
- R145 / R478 period label, R640 FRN truncation: review L32-33. Traced.
- PR R063 OCR_GLYPH_DOUBT ("246"): review L34, L210. Traced.
- CX R023/R044 SPLIT_NOT_STATED: Q14 L583, M5 L628. Traced.
- CX R033/R034/R046 FUNDING_UNQUANTIFIED: Q13 L582, M4 L627. Traced.
- CX MEETING_TIMES_ABSENT: A4-04 L615 uses RF L63 (14:35). Traced.
- PR R030 card YoY FOOTNOTE_UNRESOLVED: preamble only; the table carries the YoY values (PR L96-104). Immaterial.
**orphan_rows: none.**

Finding-ID trace (internal consistency, not a ledger row): review L27 and L705 list 30 A3 findings as incorporated. A grep of the review body finds 26 of them cited at a body location. **A3-07, A3-15, PR-FN-08 and CX-FN-06 appear only in the two incorporation lists** (review L27, L705) and in no section, flag, question or table. A5 does not read A3 files, so the content of these four cannot be checked. Under the conservative-bias rule this is a FAIL (MISSING, finding M2): A4 must anchor each one to the section that carries it, or mark it "reviewed, no change to review".

---

## AUDIT 2: ARITHMETIC

About 250 derived figures in A4's tables were recomputed from the raw VER lines. Blocks that reproduce in full are grouped. Every mismatch is itemised.

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| C operating EBITDA, 6 cols (1C) | 68.39 / 101.57 / 111.75 / 309.33 / 159.25 / 213.32 | same (PBT + D + FC - OI) | RF L591, L600, L601, L606 | PASS |
| C op EBITDA margin, 6 cols | 5.60 / 10.84 / 8.34 / 6.30 / 6.30 / 9.37% | same | RF L590 | PASS |
| C pre-FX op EBITDA and margin | 78.67 / 104.48 / 114.26 / 349.30 / 176.09 / 218.74; 6.44 / 11.15 / 8.52 / 7.11 / 6.97 / 9.61% | same (L599 - L591) | RF L591, L599 | PASS |
| C reported EBITDA, core PBT, OI/PBT, ETR, PAT margin | 70.10...220.28; 22.84...130.64; 7.0...5.1%; -0.30% / -0.16%; 2.01...6.05% | same | RF L590-L609 | PASS |
| C gross profit and GM | 280.51 / 241.59 / 303.04 / 1,143.29 / 615.70 / 544.63; 22.98 / 25.79 / 22.60 / 23.28 / 24.37 / 23.92% | same | RF L590, L593-595 | PASS |
| C FY26 op EBITDA ex-exceptional | 312.03 | 312.03 (368.25 - 18.95 - 37.27) | RF L599, L591, L602 | PASS |
| S operating EBITDA, 6 cols (1D) | 57.73 / 62.32 / 84.75 / 231.94 / 118.29 / 147.07 | same | RF L197, L206, L207, L212 | PASS |
| S margins, pre-FX, reported EBITDA, core PBT, OI/PBT, PAT margin, GP, GM | all cells | same | RF L196-L215 | PASS |
| PR reconciliation (1E): EBIT 102.85 / 58.12 / 93.12 / 195.97 / 139.90; EBITDA margin 8.75% on total income; implied D&A 14.81 = 12.30 + 2.51 and 22.26 = 11.98 + 10.28; EBIT - PAT 28.77; H1 total income -9.75%, revenue -9.86% | as shown | same | RF L590-L609; PR L96-L104 | PASS |
| C YoY (2A), 13 rows | e.g. op EBITDA +43.36 / +63.40%; FX share 17.9%; margin +273 bp; GM -38 bp; EBIT +76.30%; PAT +201.75% | same | RF L590-L621 | PASS |
| C core PBT YoY | +208.50% | +208.49% (47.62 / 22.84 = 2.08494) | RF L591, L606 | PASS (rounding; STYLE S4) |
| S YoY (2B), 13 rows; H1 YoY (2C), C and S | all cells | same | RF L196-L221, L590-L621 | PASS |
| 2D.4 walk; statutory Q2 PAT | 47.62 + 1.69 + 0.22 = 49.53; 55.27 | same | RF L606-L609 | PASS |
| QoQ 3A/3B derived blocks | Q1 FY26 1,305.71 / 90.86 / 49.90; H2 FY26 2,383.71 / 150.08 / 58.52; S Q1 FY26 1,184.94 / 60.56 / 27.58; H2 2,167.50 / 113.65 / 35.53; run-rates -6.52%, -2.36%, -21.41%, -28.27%, +43.13%, +2.68%, -1.57%, -7.08%, -24.53%, +52.62% | same | RF L590, L606, L196, L212 | PASS |
| C PAT bridge (4A) | 27.58 - 5.05 + 13.06 + 7.77 - 0.32 + 4.58 + 1.69 + 0.22 = 49.53; shares 55.68 / -10.20 / 26.37 / 15.69 / -0.65 / 9.25 / 3.41 / 0.44% | same | RF L590-L609 | PASS |
| S PAT bridge (4B) | 17.39 - 18.43 + 20.80 + 7.26 - 0.28 + 3.09 + 2.18 = 32.01; shares as shown | same | RF L196-L215 | PASS |
| 4C recurring split; proven core | 39.85 (80.46%) / 9.68 (19.54%); 26.79 (54.09%) | same | derived | PASS |
| 4C reversion PATs | 72.39; 64.62 | same | RF L591, L602, L609 | PASS |
| **4C "Both are still 2.6x the Q2 FY26 PAT" (review L354)** | 2.6x for both | **72.39 / 24.55 = 2.95x; 64.62 / 24.55 = 2.63x** | RF L609 | **FAIL (FACTUAL F3)** |
| 4C statutory-rate PAT / EPS | Q2 55.27 / 2.12; H1 102.97 / 3.94; FY26 112.40 / 4.30 | same (PBT x 0.7483 / 26.111) | RF L606, L619 | PASS |
| 4C deferred tax | DTA +9.59; DTL 9.37; net credit 0.22 | same (268.20 - 258.61; 9.59 - 9.37) | RF L685, L704, L608 | PASS |
| 5A C cash and balance sheet | CFO/PAT 1.18x / 2.38x; ex-WC after interest 1.28x / 1.16x; FCF 81.47 / 318.63; WC (70.68) / +109.02; receivable days 18.09 / 8.28; inventory days 64.62 / 72.96; payable days 140.56 / 154.42; CCC -57.85 / -73.18; borrowings 1,131.60 / 860.13; net debt 1,113.34 / 851.87; incl. lease 1,121.61 / 858.80; ND/E 2.14x / 1.30x; ND/EBITDA 3.60x / 2.00x; EBIT/FC 1.68x / 3.43x | same | RF L680-L714, L767-L799 | PASS |
| 5B S cash and balance sheet | all cells (CFO/PAT 0.87x / 2.48x; ex-WC 1.29x / 1.19x; WC 62.71; days 30.67 / 25.29, 61.02 / 67.97, 141.15 / 151.63; ND 932.05 / 716.31; ND/E 1.65x / 1.10x) | same | RF L288-L323, L374-L407 | PASS |
| 5C S-vs-C gap, 6 periods | C - S, % of S PAT, % of C PAT, revenue gap, EBITDA gap; moves -54.3 / +28.0 / +15.5 pp | same | RF L215, L609, L196, L590, L205, L599 | PASS |
| 5C subsidiary proxies | SiT 74.11; payroll 1.41; PPE 355.79; IC receivables >= 182.54; OFA 21.3%; payables 46.7% of TA | same | RF L594, L200, L596, L202, L680, L288, L300, L690, L694, L697 | PASS (proxy labelling: STYLE S2) |
| **Q7 "the balance rose by at least Rs 46.16 cr in H1" (review L576)** | at least +46.16 | **The S-minus-C receivables gap rose 46.16 (136.38 to 182.54). Parent intercompany receivable = gap + subsidiaries' external receivables. The lower bound holds for the level, not for the change. The change is 46.16 + the change in subsidiaries' external receivables (ND), and C receivables fell 140.26.** | RF L300, L690 | **FAIL (FACTUAL F1)** |
| **Q3 "26.37% of the C PAT gain (and 64.98% of the S gain) is this line" [other expenses] (review L572)** | 26.37% / 64.98% | **Other expenses alone: C 12.21 / 49.53 = 24.65%; S 19.99 / 32.01 = 62.45%. A4's figures are employee plus other expenses (13.06, 20.80).** | RF L596-597, L202-203, L609, L215 | **FAIL (FACTUAL F2)** |
| A4-01 "lower other expenses, a smaller FX loss and lower finance cost added 25.41" (review L350) | 25.41 | 24.56 for the three named lines; 25.41 includes employee cost 0.85 | RF L596, L597, L601, L602 | STYLE S1 (label) |
| 6.5 TTM and divergence | revenue 4,660.99; op EBITDA 363.40; PAT 210.73; EPS 8.07; annualised 296.32; divergence 40.6%; S TTM 143.48 | same | RF L590, L609, L621, L215 | PASS |
| Step 7 | EBIT 189.01; capital employed 1,508.86 | same | derived | PASS |
| 8B / 8C thresholds | H2 FY26 GM 22.13% (527.59 / 2,383.71); H1 FY27 23.92% | same | derived | PASS |
| A4-05 | SiT share 8.67% / 6.45% | same | RF L594, L590 | PASS |
| 0E / brief | materials + traded 77.4%; 1 pt spread = about 13 cr | 77.40%; 13.41 | RF L590, L593-595 | PASS |
| **Analyst note "reported EPS sits about 25% above a statutory-rate basis" (review L766)** | about 25% above | **33.6% above (1 / 0.7483 - 1). H1 C 5.28 vs 3.94 = +34.0%. The statutory basis is 25.17% BELOW reported; Step 8.5 L593 states this correctly.** | RF L606, L621 | **FAIL (FACTUAL F4)** |
| **Net-debt fall attribution (5A cell L382 "Deleveraging, funded by the WC release"; Step 9 payload L602 "net debt -261.47 on WC release"; analyst note L766 "debt fell 271.47 on a receivable release")** | WC release funded the fall | **Net debt fell 261.47 = 152.45 (58.3%) operating cash before WC, after interest paid 59.02, capex net of interest received 6.24 and leases 1.73, plus 109.02 (41.7%) WC release. Receivables were 140.26 gross, offset by -31.24 in other WC lines. A4's own 5A row L370 (ex-WC after-interest CFO 160.42 > WC release 109.02) contradicts the cell.** | RF L773-L784, L789, L793-L797 | **FAIL (CONTRADICTION C1)** |

Note on brief L666 ("Most of the cash came from collecting receivables"): gross receivables (140.26) are 53.6% of the 261.47 net-debt fall, so the sentence holds only on that basis. It is 42.7% of CFO. The brief should carry the split from C1.

---

## AUDIT 3: ADVERSARIAL READ

The three most positive claims in A4's review:

### Claim 1: "The profit jump is real before tax. Core profit before tax rose from Rs 22.84 cr to Rs 70.46 cr" (review L662; 2A L233 "+208.50% ... Core growth is real"; 2D.3 L271)
**Strongest bear counter (same extract):** the YoY base is the trough quarter. Derived quarterly C core PBT runs Q1 FY26 49.90 (d: 72.74 - 22.84, RF L606, L591), Q2 FY26 22.84, H2 FY26 average 29.26 (d: 58.52 / 2), Q1 FY27 60.18, Q2 FY27 70.46. Against Q1 FY26, Q2 FY27 core PBT is +41.2% (70.46 / 49.90), not +208%. Of the 47.62 rise, 7.77 (16.3%) is the FX-loss swing (RF L602). A4 classes that swing NON-RECURRING (review L327) but keeps it inside "core". A further 13.06 is opex of undisclosed composition (RF L596-597). Gross profit supplied 22.53.
**Survives: YES.** The review gives the revenue base effect only (review L269). The core-PBT trough base is absent from the summary, 2A and 2D.3. **Graft:** one sentence in the summary (L662) and in 2D.3 (L271). Type: MISSING (M3).

### Claim 2: Deleveraging (5A L380-386: net debt 1,113.34 to 851.87, ND/E 2.14x to 1.30x, ND/EBITDA 3.60x to 2.00x; L432 "Direction is positive"; Step 6D L504 deleveraging as a candidate trigger)
**Strongest bear counter (same extract):**
(i) ND/EBITDA 2.00x annualises H1 (213.32 x 2), which carries the 10.84% Q1 FY27 margin. On A4's own TTM operating EBITDA of 363.40 (review L515), ND/EBITDA is 2.34x (851.87 / 363.40). If the Rs 200 cr capex is fully term-loan funded (CX L43-44), the bound is 2.89x (1,051.87 / 363.40).
(ii) 30-Sep C equity of 656.99 (RF L700) includes a net deferred tax asset of 258.83 (DTA 268.20, RF L685, less DTL 9.37, RF L704), which is 39.4% of equity. Net debt to equity excluding the net DTA is 2.14x at 30-Sep (851.87 / 398.16) and 4.27x at 31-Mar (1,113.34 / 260.56). The DTA's value rests on the same loss pool that is NOT FOUND (A3-09, review L356). The Step 7 capital employed of 1,508.86 (review L525) also contains it.
**Survives: YES.** Neither the TTM ratio nor the DTA share of equity appears in the review. **Graft** into the 5A table (two rows) and the Step 7 ROCE row. Type: MISSING (M4).

### Claim 3: "Trajectory: RECOVERING ... C core PBT stepped up for a third reading: 49.90 (Q1 FY26), 60.18 (Q1 FY27), 70.46 (Q2 FY27)" (review L309) and "Both are still 2.6x the Q2 FY26 PAT" (review L354)
**Strongest bear counter (same extract):** the three readings are not consecutive. The full derivable sequence is 49.90, 22.84, 29.26 (H2 average), 60.18, 70.46. That is a dip and a recovery, not a staircase. H1 FY27 revenue is still -9.86% (RF L590), and Q2 FY27 revenue is only 2.68% above Q1 FY26 (review L294). The reversion test also benchmarks against the trough. Q2 FY27 PAT with OI and FX reverted (64.62) is +22.5% over the derived Q1 FY26 PAT of 52.75 (d: 77.30 - 24.55, RF L609), on the same nil-tax basis.
**Survives: YES. Graft** the full sequence into 3C (L309) and the Q1 FY26 comparison into 4C (L354). Type: MISSING (M5).

### Mandatory acquisition-economics probe
**Not triggered.** A grep of all three fulltexts for acqui|stake|takeover|amalgamat|merger|share purchase|investment in returns 0 hits. The Rs 200 cr plan is organic capex in the Company and its wholly owned subsidiary IVYPL (CX L39-44; PR L139-142). It buys no entity and no stake. Capacity, revenue and return for the capex are NOT FOUND in the filings, so no price-to-earnings multiple can be stated. A4 already routes these to Q11-Q14 (review L580-583).

---

## OTHER FINDINGS

**M1 (MISSING, loop A4): the Q1 FY26 comparators that test the spread-vs-cost flag are absent.** A4 derives Q1 FY26 revenue, op EBITDA and core PBT (review L288) but not Q1 FY26 gross margin or the other-expense ratio. A4 then reads the -319 bp Q1-to-Q2 FY27 gross-margin fall as crude and inventory-gain driven (3C L310; sector brief L672; Q2 bull answer L571).
- Derived C Q1 FY26 gross margin is 25.67% (d: (615.70 - 280.51) / 1,305.71; RF L590, L593-595). FY26 shows the same Q1-to-Q2 fall, 25.67% to 22.98% (-269 bp), with no crude attribution. The QoQ drop may be partly a recurring Q1-to-Q2 pattern, and the YoY -38 bp is then the cleaner read.
- C other expenses / revenue: Q1 FY26 12.59% (164.36 / 1,305.71), Q2 FY26 13.88%, H2 FY26 14.05% (334.86 / 2,383.71), Q1 FY27 11.33%, Q2 FY27 11.73% (RF L597, L590). Two readings: (a) the lower ratio has held for two quarters, which supports durability (A4-01/A4-02 call it "the open question", L350); (b) revenue rose on price, not tonnes, so a volume-linked cost line fell as a share of revenue (a denominator effect). Volume data (Q4) separates the two.
A symmetric read (Rule J) needs both data points beside A4-01.

**M2 (MISSING, loop A4):** A3-07, A3-15, PR-FN-08 and CX-FN-06 are listed as incorporated (review L27, L705) but cited nowhere in the body. A4 must anchor each one or mark it "reviewed, no change".

**F1-F4 (FACTUAL, loop A4):** see the arithmetic table (Q7 bound, Q3 shares, 4C multiples, analyst-note EPS premium).

**C1 (CONTRADICTION, loop A4):** net-debt attribution; see the arithmetic table.

---

## VERDICT

**INCOMPLETE. Loop back to A4.** No coverage failure: no orphan rows, nothing missing from the ledger, so A2 and A3 are not re-run. The gaps are narrative-layer fixes in the review:
- FACTUAL: F1 (Q7 "at least 46.16" bound), F2 (Q3 shares 26.37% / 64.98% should be 24.65% / 62.45%), F3 (4C "both 2.6x" should be 2.95x and 2.63x), F4 (analyst note "about 25% above" should be 33.6% above).
- CONTRADICTION: C1. The net-debt fall is attributed to the WC release (5A L382, Step 9 L602, analyst note L766). A4's own numbers show 58.3% came from operating cash before WC.
- MISSING: M1 (Q1 FY26 gross-margin and other-expense comparators); M2 (four A3 findings without body anchors); M3, M4, M5 (three surviving bear counters to graft: trough base, TTM leverage and DTA-in-equity, non-consecutive core-PBT sequence).
The protocol verdict PROCEED WITH FLAGS is not challenged by these fixes. The cash classification stays INDETERMINATE-WITH-DIRECTION.

## STYLE NOTES (logged, no loop)
- S1: review L350, "Lower other expenses, a smaller FX loss and lower finance cost added 25.41". 25.41 includes employee cost 0.85. Name it, or use 24.56.
- S2: "Subsidiaries' share of C PAT" (L413), "subsidiary profit" (Q5 L574) and "subsidiary stock-in-trade purchases were 74.11" (L422) are C-minus-S proxies, net of intercompany eliminations. For example, S H1 interest income is 5.95 vs C 3.60 (RF L378, L771). Label them as proxies.
- S3: the competition brief (L679) groups Indo Rama with buyers of inputs [SECONDARY]. It omits the company's own "leading integrated polyester manufacturer" and "integrated manufacturing platform" wording (PR L77-78, L147). Gloss what "integrated" can mean on the filed evidence.
- S4: 2A core PBT YoY reads +208.50%; recompute is +208.49%. Rounding only.
- S5: the A1 results structured file has no row for auditor paragraph 2 in either review report (RF L106-111, L467-473; Ind AS 34 boilerplate). The A2 auditor-paragraph count (10) matches the fresh count (10) by a different grouping. No conclusion depends on it.

```yaml
stage: A5-adversary
company: "INDORAMA"
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
arithmetic_mismatches:
  - {metric: "Q3 share of PAT gain attributed to other expenses (review L572)", a4_value: "C 26.37% / S 64.98%", recomputed: "C 24.65% (12.21/49.53) / S 62.45% (19.99/32.01); A4 figures are employee plus other expenses", source_line: "RF L596-597, L202-203, L609, L215"}
  - {metric: "4C reverted PAT as multiple of Q2 FY26 PAT 24.55 (review L354)", a4_value: "both 2.6x", recomputed: "72.39/24.55 = 2.95x; 64.62/24.55 = 2.63x", source_line: "RF L591, L602, L609"}
  - {metric: "Q7 H1 change in intercompany receivables (review L576)", a4_value: "rose by at least 46.16", recomputed: "S-minus-C receivables gap rose 46.16 (136.38 to 182.54); lower bound holds for the level, not the change", source_line: "RF L300, L690"}
  - {metric: "Analyst note reported EPS premium over statutory-rate EPS (review L766)", a4_value: "about 25% above", recomputed: "33.6% above (1/0.7483 - 1); H1 C 5.28 vs 3.94 = +34.0%", source_line: "RF L606, L621"}
  - {metric: "Net-debt fall attribution (review L382, L602, L766)", a4_value: "funded by the WC release", recomputed: "261.47 = 152.45 (58.3%) operating cash before WC after interest, capex, leases + 109.02 (41.7%) WC release; receivables 140.26 gross offset by -31.24", source_line: "RF L773-L784, L789, L793-L797"}
surviving_bear_counters:
  - {claim: "Core PBT +208.50% YoY, profit jump real before tax (review L233, L271, L662)", counter: "Q2 FY26 core PBT 22.84 is the trough; vs Q1 FY26 49.90 the rise is +41.2%; 7.77 of the 47.62 rise is the FX swing A4 itself calls non-recurring", source_line: "RF L591, L602, L606", type: MISSING}
  - {claim: "Deleveraging: ND/E 1.30x, ND/EBITDA 2.00x, direction positive (review L380-386, L432)", counter: "TTM ND/EBITDA 2.34x (851.87/363.40), 2.89x if capex fully debt-funded; net DTA 258.83 is 39.4% of C equity; ND/equity ex-net-DTA 2.14x (31-Mar 4.27x)", source_line: "RF L685, L700, L704; CX L43-44; review L515", type: MISSING}
  - {claim: "Core PBT stepped up for a third reading; reverted PAT still 2.6x (review L309, L354)", counter: "Readings are non-consecutive; full sequence 49.90, 22.84, 29.26 (H2 avg), 60.18, 70.46 is a dip and recovery; reverted PAT 64.62 is +22.5% over derived Q1 FY26 PAT 52.75", source_line: "RF L590, L591, L606, L609", type: MISSING}
findings_by_type:
  factual:
    - "F1: Q7 (review L576) 'balance rose by at least 46.16' is an invalid bound; only the S-minus-C gap rose 46.16 (RF L300, L690)"
    - "F2: Q3 (review L572) 26.37%/64.98% are employee plus other expenses; other expenses alone 24.65%/62.45%"
    - "F3: 4C (review L354) 'Both are still 2.6x'; 72.39 is 2.95x, 64.62 is 2.63x of 24.55"
    - "F4: analyst note (review L766) 'reported EPS about 25% above statutory basis'; correct is 33.6% above (statutory is 25.17% below)"
  missing:
    - "M1: Q1 FY26 C gross margin 25.67% (same -269 bp Q1-to-Q2 fall in FY26) and other-expense ratio sequence (12.59/13.88/14.05/11.33/11.73%) absent from the spread-vs-cost read (review L310, L350, L571, L672)"
    - "M2: A3-07, A3-15, PR-FN-08, CX-FN-06 listed as incorporated (review L27, L705) with no body anchor"
    - "M3: surviving counter 1, trough base for core PBT, to graft into summary L662 and 2D.3 L271"
    - "M4: surviving counter 2, TTM ND/EBITDA 2.34x and DTA 39.4% of equity (ND/equity ex-DTA 2.14x), to graft into 5A and Step 7"
    - "M5: surviving counter 3, non-consecutive core-PBT sequence and Q1 FY26 PAT benchmark, to graft into 3C L309 and 4C L354"
  contradiction:
    - "C1: 5A row L370 (ex-WC after-interest CFO 160.42 exceeds WC release 109.02) vs net-debt cell L382, Step 9 payload L602 and analyst note L766 that attribute the deleveraging to the WC/receivable release; split is 58.3% operating cash, 41.7% WC"
  style:
    - "S1: review L350 25.41 includes employee cost 0.85; name it or use 24.56"
    - "S2: C-minus-S subsidiary figures (L413, L422, L574) are proxies net of eliminations; label them"
    - "S3: competition brief L679 omits the company's 'integrated' self-description (PR L77-78, L147)"
    - "S4: core PBT YoY 208.50% vs recompute 208.49%, rounding"
    - "S5: A1 results structured file has no row for auditor para 2 (RF L106-111, L467-473); boilerplate; counts match"
loop_back_to: "A4"
gap: "A4 fixes, no re-enumeration: correct F1 Q7 bound, F2 Q3 shares (24.65%/62.45%), F3 4C multiples (2.95x/2.63x), F4 analyst-note EPS premium (33.6%); resolve C1 by stating the net-debt split (152.45 operating cash, 109.02 WC) in 5A L382, Step 9 L602, brief L666 and analyst note; add M1 Q1 FY26 GM 25.67% and opex-ratio sequence beside A4-01; anchor A3-07, A3-15, PR-FN-08, CX-FN-06; graft the three surviving bear counters (M3-M5)"
style_notes:
  - "S1: review L350 25.41 includes employee cost 0.85"
  - "S2: label C-minus-S subsidiary profit and purchases as proxies net of eliminations"
  - "S3: gloss the company's 'integrated' self-description in the competition brief"
  - "S4: 208.50% vs 208.49% rounding"
  - "S5: A1 auditor para 2 has no structured row; boilerplate"
analyst_note: "All five brief parts are present. Coverage is clean: a fresh grep of the three fulltexts reproduces every A2 count, all 900 IDs are ledgered, and A4 marks all of them reviewed. About 250 derived figures were recomputed. Tables 1C to 5C, both PAT bridges, the S-vs-C gap and the TTM block reproduce to rounding. The failures are in the narrative layer: three wrong shares or multiples, one invalid lower bound, and a bear-side overstatement. A4 says the WC release funded the deleveraging, but A4's own 5A numbers show 58% came from operating cash. Each of the three most positive claims has a surviving counter: the Q2 FY26 base is the trough quarter, 39% of book equity is a deferred tax asset, and the core-PBT staircase skips its two low readings. The derived Q1 FY26 gross margin (25.67%) fell by a similar amount from Q1 to Q2 a year earlier, which weakens A4's crude-cost reading of this quarter's fall. No document describes an acquisition, so the probe is not triggered. Every fix is a text edit in A4. The PROCEED WITH FLAGS verdict is not in question."
```

---
---

# RE-AUDIT, LOOP 1

Date: 2026-10-17. Same auditor, same inputs: the three A1 fulltexts, the three A1 structured files and the three A2 ledgers. A3 and the source PDF were not opened.
Under audit: the revised review (853 lines). Revision note at review L7, loop response at L733-748, change log at L750-770, A4 YAML at L774-852. "review L" below refers to the REVISED file.

## R0. DELIVERABLE-COMPLETENESS AUDIT (gate)

| Brief part | Location (revised) | Status |
|---|---|---|
| (1) Summary narrative | review L699-709 (10 source lines, about 260 words) | PRESENT |
| (2) Sector intelligence | review L711-712 | PRESENT |
| (3) Business-model intelligence | review L714-716 | PRESENT |
| (4) Competition intelligence | review L718-719 | PRESENT |
| (5) Forward map | review L721-729: make-or-break reading plus 7 catalysts, each with a Bull and a Bear fork | PRESENT |

**Gate: PASS.**

## R1. COVERAGE

- The A1 structured files and A2 ledgers have not changed. The run-1 fresh counts stand, and the diff against the ledgers is still nil: results 12 / 198 / 626 / 85 / 2 / 10 / 24; press release 3 / 6; capex 1 / 12; 900 of 900 IDs ledgered.
- The review preamble (L17-23) still marks 721/721, 132/132 and 47/47 rows reviewed. The A2-flagged rows checked in run 1 keep their anchors. PR R030 (card YoY) now has a body anchor at 1E L217.
- Finding-ID trace: every one of the 30 incorporated A3 IDs now has a body anchor. A3-07 is at 5C L456; A3-15 at 0D L87; PR-FN-08 at 1E L217; CX-FN-06 at 0D L88. Each is also listed at preamble L27.
**orphan_rows: none. missing_from_ledger: none. Coverage: PASS.**

## R2. STATUS OF RUN-1 FINDINGS

| ID | Type | Run-1 gap | Fix in revised review (verified against fulltext) | Status |
|---|---|---|---|---|
| F1 | FACTUAL | Q7 invalid "at least 46.16" bound | Q7 L611 now says the S-minus-C gap rose 46.16 (136.38 to 182.54) and the intercompany change is ND. 5C L454 keeps the level bound 182.54 (RF L300, L690). | CLOSED |
| F2 | FACTUAL | Q3 shares | Q3 L607: 24.65% (12.21 / 49.53) and 62.45% (19.99 / 32.01). 4A L331 and 4B L346 split employee and other-expense shares (1.72% / 24.65%; 2.53% / 62.45%). | CLOSED |
| F3 | FACTUAL | 4C "2.6x" | 4C L364: 2.95x and 2.63x | CLOSED |
| F4 | FACTUAL | EPS premium | 33.6% at 4C L366, Step 7 L565, Flag 1 L680 and analyst note L850. Top-3 L628 says "cuts EPS by 25.17%". | CLOSED |
| C1 | CONTRADICTION | Net-debt attribution | 5A L392, sources table L402-417, 5D L464, L466, 6D L538, Step 9 L637, brief L705, A4-06 L652 and YAML flag L839 all carry 152.45 (58.3%) / 109.02 (41.7%). The table foots to 261.47. | CLOSED (but see M6) |
| M1 | MISSING | Q1 FY26 comparators | 3A L293-299 adds GM and other-expense columns. 3C L315, comparators L357-360 (two readings plus the separating observation), A4-01 L647, Q2 L606, Q4 L608 and sector L712 updated. | CLOSED (but see F5) |
| M2 | MISSING | Four A3 IDs unanchored | Anchored at L87, L88, L217, L456 | CLOSED |
| M3 | MISSING | Trough base | 2A L238, 2D.3 L276, brief L700-701, Flag 3 L682 | CLOSED |
| M4 | MISSING | Leverage counter | 5A L394-398, Step 7 L559 and L566, Flag 6 L685, A4-06 | CLOSED |
| M5 | MISSING | Non-consecutive sequence | 3C L314; 4C L364 | CLOSED |
| S1-S4 | STYLE | as logged | Fixed at L355, 5C L443-445 and Q5/Q6/8B/brief, L719, L238/L276 | CLOSED |
| S5 | STYLE | A1 boilerplate row | No action (A1-level) | LOGGED, no loop |

## R3. ARITHMETIC RE-AUDIT (new and changed figures)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Core PBT YoY (2A L238, 2D.3 L276) | +208.49% | 47.62 / 22.84 = +208.49% | RF L591, L606 | PASS |
| Core PBT vs Q1 FY26 | +41.20% | 70.46 / 49.90 = 1.4120 | RF L591, L606 | PASS |
| FX share of core-PBT rise | 16.32% | 7.77 / 47.62 = 16.32% | RF L602 | PASS |
| 3A Q1 FY26 GP / GM | 335.19 / 25.67% | 615.70 - 280.51 = 335.19; / 1,305.71 = 25.67% | RF L590, L593-595 | PASS |
| 3A other expenses / revenue | 12.59 / 13.88 / 14.05 / 11.33 / 11.73% (164.36; 334.86) | 333.82 - 169.46 = 164.36; 668.68 - 333.82 = 334.86; ratios same | RF L597, L590 | PASS |
| 3A H2 FY26 GM | 22.13% (527.59) | 1,143.29 - 615.70 = 527.59; / 2,383.71 | RF L590, L593-595 | PASS |
| 4A / 4B split shares | 1.72% / 24.65%; 2.53% / 62.45% | 0.85 / 49.53; 12.21 / 49.53; 0.81 / 32.01; 19.99 / 32.01 | RF L596-597, L202-203 | PASS |
| A4-01 text (L355) | 24.56 + 0.85 = 25.41 | 12.21 + 7.77 + 4.58 = 24.56 | RF L597, L602, L601, L596 | PASS |
| 4C multiples; Q1 FY26 PAT; reverted vs Q1 FY26 | 2.95x / 2.63x; 52.75; +22.50% | 72.39 / 24.55; 64.62 / 24.55; 77.30 - 24.55; 64.62 / 52.75 = 1.2250 | RF L609 | PASS |
| EPS premium (4C, Step 7, Flag 1, analyst note) | 33.6%; +34.0% | 1 / 0.7483 - 1 = 33.64%; 5.28 / 3.94 = 1.3401 | RF L606, L621 | PASS |
| Net DTA and share of equity (5A L395) | 258.61 (49.8%) / 258.83 (39.4%) | 258.61 / 519.17 = 49.81%; (268.20 - 9.37) / 656.99 = 39.40% | RF L685, L704, L700 | PASS |
| ND / equity ex net DTA (5A L396) | 4.27x / 2.14x; -2.13x | 1,113.34 / 260.56 = 4.273; 851.87 / 398.16 = 2.140 | RF L685, L700, L704 | PASS |
| ND / TTM op EBITDA (5A L398) | 3.60x / 2.34x; 2.89x | 1,113.34 / 309.33; 851.87 / 363.40 = 2.344; 1,051.87 / 363.40 = 2.895 | derived | PASS |
| Net-debt sources table (L402-415) | 152.45 (58.3%) + 109.02 (41.7%) = 261.47; receivables 140.26 (53.6%); other WC -31.24 (-11.9%) | 216.73 + 2.71 - 59.02 - 6.24 - 1.73 = 152.45; shares same | RF L773, L783, L795, L789, L793-794, L774-781 | PASS |
| 5C equity gap (A3-07, L456) | -44.59 to +4.43 | 258.06 - 302.65; 395.88 - 391.45. The 49.02 swing equals the H1 C-minus-S PAT gap. S and C other equity each move by exactly their H1 PAT (88.80, 137.82). | RF L309, L699 | PASS |
| Step 7 DTA share of capital employed; ex-DTA CE | 17.2%; 1,250.03 | 258.83 / 1,508.86 = 17.15%; 1,508.86 - 258.83 | derived | PASS |
| Competition: cost of materials share | 70.4% | 944.32 / 1,340.64 = 70.44% | RF L593, L590 | PASS |
| 1E cards (L217) | 1,344 / 118 / 74 | 1,344.04 / 117.66 / 74.08 | PR L85; RF L592, L599, L609 | PASS |
| Loop table L746 anchor for 31-Mar equity | "RF L532" | 519.17 sits at RF L700. RF L532 is a letterhead line. The body rows cite correctly. | RF L700 | STYLE S6 |

**No arithmetic mismatch.**

## R4. ADVERSARIAL READ ON THE REVISED REVIEW

Loop 1 changed which claims are most positive. The three most positive claims in the revised review are tested below.

### Claim A: "The deleveraging is mostly earned, not borrowed from working capital" (L417; also L466 "58.3% of the debt fall came from operating cash"; 6D L538; brief L705; analyst note L850)
**Strongest bear counter (same extract):** the 152.45 is pre-tax cash. Current tax is nil in every consolidated period (RF L607), and H1 brought in a 2.71 tax refund (RF L783). A4 applies a 25.17% sensitivity rate to EPS (4C L366). At that rate, H1 cash tax on PBT of 137.60 (RF L767) would be about 34.63 (d: 137.60 x 0.2517). The operating share would then fall to 117.82 (d: 152.45 - 34.63), and the split becomes about 52% operating cash / 48% WC (117.82 / 226.84). Capex of 9.83 (RF L785) was also only 40.4% of D&A of 24.31 (RF L768), which flatters the "earned" part further. A4 notes capex below D&A in 5D (L463) but does not tie it to this claim.
**Survives: YES.** The review links the tax shield to EPS (4C, Flag 1, Step 7) but never to the cash split. "Mostly" still holds on a taxed basis, but only just. **Graft:** one sentence beside L417. Add "pre-tax, no cash tax paid" to L466 and brief L705. Type: MISSING (M6).

### Claim B: "Against the derived Q1 FY26 PAT of 52.75 ... the fully reverted 64.62 is +22.50% ... The second benchmark is the better guide to underlying progress" (4C L364; with 2A L238 core PBT +41.20%)
**Bear counters tested:**
(i) Tax basis: both periods are untaxed (RF L607), so there is no tax distortion.
(ii) Like-for-like: the reversion charges Q2 FY27 the Q2 FY26 FX loss of 10.28, while Q1 FY26 keeps its own 6.56 (d: 16.84 - 10.28). The +22.50% is therefore, if anything, harsh. Core PBT ex-FX is 72.97 vs 56.46 (+29.2%).
(iii) Season: A4 now shows Q1 carries the high gross margin (25.67%, L293), so Q1 FY26 is not a soft benchmark.
**Survives: NO.** No graft.

### Claim C: "Underlying conversion is adequate"; ex-WC after-interest CFO / PAT 1.16x; "Direction is positive" (5A L380, L466)
**Bear counter tested: tax basis.** On a statutory-rate basis both the numerator and the denominator shrink. The numerator becomes 160.42 - 2.71 - 34.63 = 123.08; the denominator becomes 102.97 (L366). The ratio is 1.20x, so it holds. The YoY decline (1.28x to 1.16x) is already shown at L380.
**Survives: NO.** No graft.

### Mandatory acquisition-economics probe
Not triggered. The documents are unchanged, and the run-1 grep (0 hits for acqui|stake|takeover|amalgamat|merger|share purchase|investment in) stands. The Rs 200 cr is organic capex (CX L39-44). Its economics are NOT FOUND; A4 asks for them at Q11-Q14 (L615-618).

## R5. NEW FINDINGS (loop 1)

**F5 (FACTUAL, loop A4).** Sector brief L712 reads: "A similar Q1-to-Q2 fall happened last year without a crude shock (25.67% to 22.98%) [FILED, derived]". The filings say nothing about crude in Q2 FY26. A grep of all three fulltexts for crude|oil price|raw material returns only PR L130-131, the CMD's Q2 FY27 remark. Only the two gross-margin figures are FILED-derived; "without a crude shock" is not in the extract. The next inference ("so crude explains only part of it") rests on it. 3C L315 states it correctly ("with no crude attribution"). **Fix:** replace "without a crude shock" with "with no crude attribution in the filings", or move the claim to a SECONDARY source with a cite.

**M6 (MISSING, loop A4).** The surviving bear counter to Claim A, as set out in R4. **Graft:** "The 152.45 is pre-tax cash: no current tax was paid and H1 included a 2.71 refund (RF L607, L783). At the 25.17% sensitivity rate, H1 tax would be about 34.63 and the split about 52% operating cash / 48% WC. Capex of 9.83 ran at 40.4% of D&A (RF L785, L768)." Place it beside L417, and qualify L466 and brief L705 as pre-tax.

## R6. VERDICT, LOOP 1

**INCOMPLETE. Loop back to A4.** All ten run-1 FACTUAL, CONTRADICTION and MISSING items are closed, and S1-S4 are fixed. Coverage and the brief gate pass, and no arithmetic mismatch remains. Two new items block save:
- **F5 (FACTUAL):** a mis-tiered claim, "without a crude shock" tagged FILED (L712).
- **M6 (MISSING):** a surviving bear counter to the new "mostly earned" deleveraging claim (L417).

Both fixes are one-sentence edits. A2 and A3 are not re-run. The verdict PROCEED WITH FLAGS and the INDETERMINATE-WITH-DIRECTION cash classification are not affected.

## R7. STYLE NOTES, LOOP 1 (logged, no loop)
- S5 (carried): the A1 auditor paragraph 2 has no structured row. Boilerplate; no action.
- S6: loop-response table L746 cites "RF L532" for the 31-Mar equity of 519.17. The correct line is RF L700. The body rows cite correctly.
- S7: 5C L456 says "The subsidiaries' profit run is recent, so their earnings history is short." This rests on reading the 31-Mar equity gap (-44.59) as a cumulative deficit. A4 itself allows that it may be a consolidation adjustment. Tag it [INFERENCE].
- S8: competition L719 says "It does not mean the company makes its own PTA or MEG." The evidence (materials 70.4% of revenue; the CMD crude remark) fits this but does not prove it. Soften to "The filings give no sign that it makes its own PTA or MEG."

```yaml
stage: A5-adversary
company: "INDORAMA"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 1
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
  - {claim: "The deleveraging is mostly earned, not borrowed from working capital; 58.3% of the net-debt fall from operating cash (review L417, L466, L538, L705)", counter: "The 152.45 is pre-tax cash: nil current tax and a 2.71 refund in H1; at the 25.17% sensitivity rate H1 tax is about 34.63 and the split becomes about 52% operating cash / 48% WC (117.82/226.84); capex 9.83 was 40.4% of D&A 24.31", source_line: "RF L607, L783, L767, L785, L768", type: MISSING}
findings_by_type:
  factual:
    - "F5: sector brief (review L712) says the FY26 Q1-to-Q2 gross-margin fall came 'without a crude shock' and tags it FILED, derived; the only crude text in the filings is the Q2 FY27 CMD quote (PR L130-131); 3C L315 correctly says 'no crude attribution'"
  missing:
    - "M6: surviving bear counter to the loop-1 claim 'deleveraging mostly earned' (review L417): the earned 152.45 is pre-tax cash (RF L607, L783); about 52/48 at 25.17%; capex 40.4% of D&A (RF L785, L768); graft beside L417 and qualify L466 and brief L705"
  contradiction: []
  style:
    - "S5 (carried): A1 results structured file has no row for auditor para 2 (RF L106-111, L467-473); boilerplate"
    - "S6: loop-response table review L746 cites RF L532 for 31-Mar equity 519.17; correct line is RF L700"
    - "S7: 5C review L456 'profit run is recent' rests on reading the -44.59 equity gap as a deficit; tag [INFERENCE]"
    - "S8: competition review L719 'It does not mean the company makes its own PTA or MEG' is categorical; soften to 'the filings give no sign that'"
loop_back_to: "A4"
gap: "A4, two one-sentence edits, no re-enumeration: (F5) review L712 replace 'without a crude shock' with 'with no crude attribution in the filings' or cite a SECONDARY source; (M6) beside review L417 state that the 152.45 earned share is pre-tax cash (nil current tax RF L607, 2.71 refund RF L783; at 25.17% the split is about 52/48) and capex was 40.4% of D&A (RF L785, L768), and add 'pre-tax' to review L466 and brief L705"
style_notes:
  - "S5: A1 auditor para 2 has no structured row; boilerplate"
  - "S6: review L746 anchor RF L532 should be RF L700"
  - "S7: tag review L456 'profit run is recent' as [INFERENCE]"
  - "S8: soften review L719 PTA/MEG sentence"
analyst_note: "Loop 1 closes all ten run-1 items (F1-F4, C1, M1-M5) and fixes S1-S4. Every new figure recomputes from the fulltext, and coverage and the brief gate still pass. Two items remain, each a one-sentence edit. First, the C1 fix created a new most-positive claim: 'the deleveraging is mostly earned' (review L417). Its strongest counter survives. The 152.45 is pre-tax cash (nil current tax, RF L607; a 2.71 refund, RF L783). At A4's own 25.17% sensitivity rate the earned share falls to about 52%, and capex ran at 40% of D&A. A4 ties the tax shield to EPS but not to the cash split. Second, the sector brief says the FY26 Q1-to-Q2 gross-margin fall came 'without a crude shock' and tags it FILED. The only crude text in the filings is the Q2 FY27 CMD quote (PR L130-131). Two other counters were tested and fail: the Q1 FY26 benchmark is on the same nil-tax basis and is if anything harsh, and ex-WC cash conversion holds at 1.20x on a taxed basis. The PROCEED WITH FLAGS verdict is unaffected."
```

---
---

# RE-AUDIT, LOOP 2

Date: 2026-10-17. Same auditor. Inputs: the three A1 fulltexts, the three A1 structured files, the three A2 ledgers, and the revised review. A3 files, the source PDF and inputs/ were not opened.
Under audit: the review after loop 2 (874 lines). Revision note at review L7. Loop 2 response at L772-780, loop 2 change log at L782-791, A4 YAML at L795-873. "review L" below refers to THIS revision.

## L2-0. DELIVERABLE-COMPLETENESS AUDIT (gate)

| Brief part | Location (loop 2) | Status |
|---|---|---|
| (1) Summary narrative | review L700-711 (11 source lines, about 270 words) | PRESENT |
| (2) Sector intelligence | review L713-714 | PRESENT |
| (3) Business-model intelligence | review L716-718 | PRESENT |
| (4) Competition intelligence | review L720-721 | PRESENT |
| (5) Forward map | review L723-731: make-or-break reading plus 7 catalysts (M1/M2, M4, M5/M6, M3, M7, M8, M9), each with a Bull and a Bear fork | PRESENT |

**Gate: PASS.**

## L2-1. COVERAGE (fresh grep pass this loop)

| Document | Category | A2 count | Fresh count this loop (method) | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Line items (VER rows) | 198 | 198 (grep `^VER-(3,4,5,9,10,11) \|` over RF) | none | PASS |
| Results | Notes | 12 | 12: numbered RF L415, L419, L423, L428 (S); L805, L810, L817, L822 (C); labels L225, L326, L625, L717 | none | PASS |
| Results | Agenda items | 2 | 2 (RF L49, L57) | none | PASS |
| Results | Structured IDs | 721 ledgered (ledger L13) | 721 (grep `^R\d{3} \|` over structured) | none | PASS |
| Press release | Pages / slides | 3 | 3 (PR L17, L69, L125) | none | PASS |
| Press release | Structured IDs | 132 ledgered (ledger L2) | 132 | none | PASS |
| Capex letter | Structured IDs; agenda | 47 ledgered (ledger L2); 1 | 47; 1 | none | PASS |
| All | Turns | 0 | 0 | none | PASS |

- The other run-1 categories (table cells 626, zero-standing 85, auditor paragraphs 10, entities 24 and 12, PR line items 6, forward items 2 / 3 / 5) stand. The A1 structured files and the A2 ledgers carry the same headers and ID totals as in run 1. The start-of-session git status lists only the review, the A4 block and the run log as modified in this run folder.
- **A2 flag sweep (new this loop).** I grepped all three ledgers for every upper-case flag token. Flags found: ZERO_STANDING, EXTRACTOR_FLAG, MISMATCH_NOTE / FOOTNOTE_UNRESOLVED (R688), ENTITY_CHANGE_UNKNOWN (R659-R662), SIGNATURE_TIME_ND (results ledger L298), SPLIT_NOT_STATED, FUNDING_UNQUANTIFIED, MEETING_TIMES_ABSENT (capex ledger L16-19), OCR_GLYPH_DOUBT (PR R063), FOOTNOTE_UNRESOLVED (PR R030), and "MISSING_FROM_STRUCTURED: none" (PR ledger L91). Body anchors: R688 at review L85; R659-R662 at L86 and Q17 L622; R063 at L34 and L214; R030 at L217; the capex flags at Q13 L618, Q14 L619, M4 L664, M5 L665; MEETING_TIMES_ABSENT at A4-04 L651 (RF L63).
- **Two signature-time flags have no remark in the body.** These are results SIGNATURE_TIME_ND (R678 and R685 carry a date but no clock time, ledger L298) and the PR cover-letter timestamp "2026.10.16 21:47:58" (PR L52; PR ledger L75). The rows themselves are covered: the preamble marks 721/721 and 132/132 reviewed, and the body uses the 16-Oct-2026 dates. No number or conclusion depends on either flag. Neither my run-1 trace nor my loop-1 trace named them. Logged as STYLE S10, not an orphan.
- Finding-ID trace: all 30 incorporated A3 IDs keep their body anchors (A3-07 L457, A3-15 L87, PR-FN-08 L217, CX-FN-06 L88; the others unchanged).

**orphan_rows: none. missing_from_ledger: none. Coverage: PASS.**

## L2-2. STATUS OF OPEN ITEMS FROM RUN 1 AND LOOP 1

| ID | Type | Gap | Fix in loop-2 review (checked against fulltext) | Status |
|---|---|---|---|---|
| F5 | FACTUAL | "without a crude shock" tagged FILED (sector brief) | Sector L714 now reads "with no crude attribution in the filings (25.67% to 22.98%) [FILED, derived]", followed by "So crude may explain only part of this year's fall [INFERENCE]". 3C L315 and YAML flag L856 use the same wording. A grep finds "crude shock" only in the change-log row L786. A grep of the three fulltexts for timestamps and crude text still finds crude only at PR L130-131 (Q2 FY27). | CLOSED |
| M6 | MISSING | Pre-tax counter to "deleveraging mostly earned" | 5A net-debt row L392 ("pre-tax", 52/48); capex row L381 (40.4% of D&A); sources-table label L411 "(pre-tax)"; memo row L416 (117.82, 51.9% vs 48.1%); paragraph L418 (nil tax RF L607, refund RF L783, 34.63, 117.82, capex 40.4% of D&A); 5D L465; classification L467; 6D L539; Step 7 L561; Step 9 L638; A4-06 L653; Flag 5 L685; brief L706; YAML flag L860; A4 analyst note L871. Every instance of the 58.3% share now carries "pre-tax" and the 52/48 split. | CLOSED |
| F1-F4, C1, M1-M5 (run 1) | mixed | as logged | Regression grep for the run-1 error strings ("2.6x", "rose by at least", "about 25% above", "26.37% of the C PAT gain", "funded by the WC release", "on a receivable release", "208.50") finds them only in change-log rows L758 and L769. | STILL CLOSED |
| S5-S8 | STYLE | as logged | Not applied. A4 records them as optional (L789). | LOGGED, no loop |

## L2-3. ARITHMETIC RE-AUDIT (loop-2 figures, plus a spot re-check of unchanged cells)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Statutory-rate tax on H1 PBT (L416, L418) | 34.63 | 137.60 x 0.2517 = 34.634 | RF L606 | PASS |
| Taxed operating cash (L416, L418) | 117.82 | 152.45 - 34.63 = 117.82 | derived | PASS |
| Taxed split (L416, L392, L465, L539, L638, L653, L685) | 51.9% / 48.1%; "about 52/48" | 117.82 / 226.84 = 51.94%; 109.02 / 226.84 = 48.06% | derived | PASS |
| Capex / D&A (L381, L418, L464, L653, L685) | 40.4% | 9.83 / 24.31 = 40.44% | RF L785, L768 | PASS |
| Pre-tax operating cash re-foot (L411) | 152.45 | 216.73 + 2.71 - 59.02 - 6.24 - 1.73 = 152.45 | RF L773, L783, L795, L789, L793-794 | PASS |
| WC release re-foot (L412) | 109.02 | 140.26 - 9.62 - 11.18 - 23.95 + 11.45 + 2.87 + 10.53 - 11.34 = 109.02 | RF L774-781 | PASS |
| Net-debt fall (L415) | 261.47 | (444.58 + 687.02 - 16.82 - 1.44) - (332.18 + 527.95 - 6.82 - 1.44) = 1,113.34 - 851.87. Borrowings fell 271.47 = 64.49 + 206.98, so there is no non-cash movement. | RF L701, L706, L691-692, L790, L792 | PASS |
| Refund basis inside the taxed figure | 2.71 kept | The 2.71 equals the fall in non-current tax assets, 10.02 to 7.31 (RF L686). It is prior-period cash, so keeping it is defensible. Without it: 115.11 / 224.13 = 51.4%. | RF L783, L686 | PASS (basis note) |
| "About half earned at a normal tax rate and capex level" (L418) | about half | At D&A-level capex: 117.82 - (24.31 - 9.83) = 103.34; 103.34 / 212.36 = 48.7%. With the refund also removed: 100.63 / 209.65 = 48.0%. "About half" holds on every basis. The 52/48 itself is at actual capex. | RF L768, L785 | PASS (wording: STYLE S9) |
| "All pre-tax" covers the S ratios (Step 7 L561) | all pre-tax | S P&L tax nil (RF L213-214); S cash flow shows a 3.76 refund (RF L390). Holds. The anchor cited is the C line RF L607. | RF L390, L213-214 | PASS (anchor: STYLE S11) |
| Spot re-check, unchanged cells | C Q2 op EBITDA 111.75; GP 303.04 / GM 22.60%; ex-WC CFO/PAT 1.16x / 1.28x; H1 FY26 WC (70.68); S ex-WC 1.19x and WC 62.71; days 8.28 / 72.96 / 154.42, CCC -73.18; ND/E 1.30x; net DTA 258.83 (39.4%); TTM op EBITDA 363.40; 5C Q2 gap 19.03 (34.6%) | all same | RF L590-609, L680-714, L767-799, L374-407 | PASS |

**No arithmetic mismatch.**

## L2-4. ADVERSARIAL READ ON THE LOOP-2 REVIEW

The three most positive claims in this revision:

### Claim A: "Read this way, about half the deleveraging is earned at a normal tax rate and capex level" (L418; with "Direction is positive", L467; 6D candidate trigger, L539)
**Bear counters tested (same extract):**
(i) Capex at D&A level. H1 capex was 9.83 against D&A of 24.31 (RF L785, L768). If capex had matched D&A, the earned share would be 103.34, which is 48.7% of the fall on a taxed basis.
(ii) Prior-period refund. Removing the 2.71 refund (RF L783) gives 115.11, or 51.4%.
(iii) Both together give 100.63, or 48.0%.
**Survives: NO.** On every basis the earned share is 48-52%, so "about half" holds. One wording point remains. The 52/48 split is at actual capex, which A4 itself calls 40.4% of D&A. "At a normal ... capex level" therefore needs the 48.7% figure behind it. Also, "the other half is a receivable release" describes a net WC release of 109.02, made of receivables 140.26 less other lines 31.24 (L413-414). Both points are logged as STYLE S9. No graft is needed.

### Claim B: "The fully reverted 64.62 is +22.50% [vs Q1 FY26] ... the better guide to underlying progress"; core PBT +41.20% vs Q1 FY26 (L364, L702, Flag 3 L683, A4 analyst note L871)
**Bear counter tested: catch-up volume.** Q2 FY27 revenue rose 43.13% QoQ after a disrupted Q1 (PR L112-113). Part of Q2 may be Q1 demand that slipped into Q2 [INFERENCE]. If so, one quarter overstates the run-rate. Test this on H1 so that any catch-up nets out. H1 FY27 core PBT averages 65.32 a quarter (d: 130.64 / 2, RF L606, L591). That is +30.9% over Q1 FY26 (49.90) and +79.6% over the H1 FY26 average (36.37). Q1 FY26 is also the high-margin season (GM 25.67%, L293), so it is not a soft base.
**Survives: NO.** Progress holds on the H1 basis. No graft.

### Claim C: "Operating EBITDA ... Strong" +63.40% YoY (2A L230) and "operating EBITDA still rose 10.02% QoQ" (3C L314)
**Bear counter tested: negative incremental leverage QoQ.** Revenue rose 404.00 QoQ, but operating EBITDA rose only 10.18, an incremental margin of 2.52% (d: 10.18 / 404.00, RF L590). On YoY, the trough base and the 17.9% FX share are already in the 2A row (L230). Q1 FY26 operating EBITDA of 90.86 is in 3A L293.
**Survives: NO.** The review already states the substance: the margin fell 251 bp QoQ (L232, L275, L314). The incremental-margin figure restates that fact. No graft.

### Mandatory acquisition-economics probe
**Not triggered.** Re-run this loop: a grep of the three fulltexts for acqui|stake|takeover|amalgamat|merger|share purchase|investment in gives 0 hits. The Rs 200 cr is organic capex (CX L39-44). Its capacity, revenue and return are NOT FOUND. A4 routes them to Q11-Q14 (L616-619).

## L2-5. NEW FINDINGS (loop 2)

No FACTUAL, MISSING or CONTRADICTION finding. Three new STYLE notes (S9-S11) are logged below.

## L2-6. VERDICT, LOOP 2

**COMPLETE.** Both loop-1 items are closed: F5 (FACTUAL) and M6 (MISSING). All ten run-1 items stay closed. The brief gate passes, and coverage passes with no orphan rows and nothing missing from the ledger. No arithmetic mismatch remains, and no bear counter survives. The open findings are STYLE only, and they do not loop. The review may proceed to the operator-approved Notion step. The protocol verdict PROCEED WITH FLAGS and the INDETERMINATE-WITH-DIRECTION cash classification stand.

## L2-7. STYLE NOTES, LOOP 2 (logged, no loop)
- S5 (carried): the A1 results structured file has no row for auditor paragraph 2 (RF L106-111, L467-473). Boilerplate.
- S6 (carried): the loop-1 response row (review L748) cites "RF L532" for the 31-Mar equity of 519.17. The correct line is RF L700.
- S7 (carried): 5C L457, "The subsidiaries' profit run is recent, so their earnings history is short", should carry an [INFERENCE] tag.
- S8 (carried): competition L721, "It does not mean the company makes its own PTA or MEG", is categorical. Soften to "The filings give no sign that it makes its own PTA or MEG."
- S9 (new): L418, "about half the deleveraging is earned at a normal tax rate and capex level". The 52/48 split is at actual capex (40.4% of D&A). Add the D&A-level figure, 48.7% (103.34 / 212.36). In the same paragraph, "the other half is a receivable release" should read "a net WC release (receivables 140.26 gross, other lines -31.24)".
- S10 (new): results SIGNATURE_TIME_ND (ledger L298) and the PR cover-letter timestamp 21:47:58 (PR L52) get no remark beside A4-04 / Q20. The results filing carries no signing time, so the 30-minute timing test runs only for the capex letter. One sentence would record this. My earlier traces also did not name these flags.
- S11 (new): Step 7 L561 cites RF L607 (C) for "All pre-tax". The S ratios rest on RF L213-214 and the S refund at RF L390.

```yaml
stage: A5-adversary
company: "INDORAMA"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
verdict: COMPLETE
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
surviving_bear_counters: []
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "S5 (carried): A1 results structured file has no row for auditor para 2 (RF L106-111, L467-473); boilerplate"
    - "S6 (carried): loop-1 response row review L748 cites RF L532 for 31-Mar equity 519.17; correct line is RF L700"
    - "S7 (carried): 5C review L457 'profit run is recent' needs an [INFERENCE] tag"
    - "S8 (carried): competition review L721 PTA/MEG sentence is categorical; soften to 'the filings give no sign that'"
    - "S9: review L418 'about half earned at a normal tax rate and capex level'; the 52/48 is at actual capex (40.4% of D&A); add the D&A-level figure 48.7% (103.34/212.36); call the 109.02 a net WC release (receivables 140.26 gross, other lines -31.24), not a receivable release"
    - "S10: results SIGNATURE_TIME_ND (ledger L298) and PR cover-letter timestamp 21:47:58 (PR L52) get no remark beside A4-04/Q20; rows covered by the 721/721 and 132/132 marks; non-material; not named in A5's earlier traces"
    - "S11: Step 7 review L561 'All pre-tax' cites RF L607 (C) only; S basis is RF L213-214 and S refund RF L390"
loop_back_to: ""
gap: ""
style_notes:
  - "S5: A1 auditor para 2 has no structured row; boilerplate"
  - "S6: review L748 anchor RF L532 should be RF L700"
  - "S7: tag review L457 'profit run is recent' as [INFERENCE]"
  - "S8: soften review L721 PTA/MEG sentence"
  - "S9: review L418 add the D&A-level earned share 48.7%; call 109.02 a net WC release"
  - "S10: note results SIGNATURE_TIME_ND and PR timestamp 21:47:58 beside A4-04/Q20"
  - "S11: review L561 add S anchors RF L213-214, L390"
analyst_note: "Loop 2 closes both loop-1 items. F5: the sector brief now says the FY26 Q1-to-Q2 gross-margin fall came with no crude attribution in the filings (review L714); 'crude shock' remains only in the change log. M6: every place that carries the 58.3% earned share now says pre-tax and gives the 52/48 split at a 25.17% tax. All loop-2 figures recompute from the fulltext (34.63, 117.82, 51.9%, 40.4%), and no run-1 error text has returned. Coverage is unchanged: fresh greps give 198 VER rows, 12 notes, 3 PR pages and 900 structured IDs, all ledgered and marked reviewed. Three positive claims were attacked again. 'About half the deleveraging is earned' holds at D&A-level capex (48.7%) and without the prior-period refund (51.4%). The Q1 FY26 benchmark holds on an H1-average basis (+30.9%). The QoQ EBITDA rise is already offset by the stated 251 bp margin fall. No counter survives. Seven STYLE notes are logged. S10 records two signature-time flags that my earlier traces did not name; they are non-material. Verdict COMPLETE; PROCEED WITH FLAGS stands."
```
