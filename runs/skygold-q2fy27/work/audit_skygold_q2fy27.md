# A5 ADVERSARY / COMPLETENESS AUDIT: Sky Gold & Diamonds Ltd (SKYGOLD), Q2 FY27

Stage: A5 adversary | Model: claude-opus-5-5 | Audit date: 2026-10-28
Under audit: runs/skygold-q2fy27/work/review_skygold_q2fy27.md (A4, 939 lines)
Inputs read: A1 fulltexts (results, presentation, press release, EGM, ESOP), A1 structured (results, presentation, press release), A2 ledgers (results, presentation, press release), A4 review. No source PDF and nothing under inputs/ was opened. A3 notes were not read.

Anchor key: rL#### = results fulltext line; dL### = presentation fulltext line; pL### = press release fulltext line; eL### = EGM fulltext line; sL### = ESOP fulltext line. rR / dR / pR = A1 structured row IDs. Statements are in Rs lakhs; all values below are Rs Cr (/100). "computed" = A5 recomputation from the cited lines.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Brief part | Heading in A4 | Content | Status |
|---|---|---|---|
| 1. Summary narrative | "### 1. SUMMARY NARRATIVE" (review L776) | 18 lines (L778-L795), within the 10-20 line band | PRESENT |
| 2. Sector intelligence | "### 2. SECTOR INTELLIGENCE" (L797) | 12 lines, provenance-tagged, names undisclosed items | PRESENT |
| 3. Business-model intelligence | "### 3. BUSINESS-MODEL INTELLIGENCE" (L812) | 13 lines incl. advance-gold mechanics, job-work subsidiaries, model drift | PRESENT |
| 4. Competition intelligence | "### 4. COMPETITION INTELLIGENCE" (L828) | 12 lines, SECONDARY peer data tagged, risks named | PRESENT |
| 5. Forward map | "### 5. FORWARD MAP" (L843) | Make-or-break reading plus 9 dated catalysts, each with a Bull and a Bear fork | PRESENT |

Gate result: PASS. All five parts are present and carry real content.

---

## 1. COVERAGE AUDIT

Method: fresh pass over each A1 fulltext. Results: counted numbered notes, Board-letter agenda items, Annexure A items, auditor paragraphs, consolidation entities and every RENDER-READ statement row (rL1052-rL1321). Presentation: page markers, per-slide numeric tokens on 20 slides (p6-p10, p12, p13, p16, p17, p20, p21, p23, p26-p29, p36, p38-p40) and a text-claim sweep of the narrative slides (p13, p15-p19). Press release: table rows, notes, bullets, quote. ID totals re-grepped in each structured file.

| Document | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | Numbered notes (SA 1-6 rL542-562; cons 1-9 rL1333-1344) | 15 | 15 | 0 | PASS |
| Results | Statement line items (SA P&L 28, SA BS 37, SA CF 42, cons P&L 41, cons BS 41, cons CF 50, note 5(i) 3, note 5(ii) 3) | 245 | 245 | 0 | PASS |
| Results | Line-item cells (R001-R780) | 780 | 780 (27x6+1; 37x2; 42x2; 40x6+1; 41x2; 50x2; 6x6) | 0 | PASS |
| Results | Board agenda items (rL46-84) | 5 (+2 unnumbered) | 5 | 0 | PASS |
| Results | Annexure A items (rL121-202) | 8 | 8 | 0 | PASS |
| Results | Auditor paragraphs (SA 1-5, rL220-250 + rL1324; cons 1-7, rL595-688) | 12 | 12 | 0 | PASS |
| Results | Consolidation entities (rL636-646, rL1335) + 2 unnamed other-auditor subs (rL667) + Purvi (rL1342) | 6 + 2 + 1 | 6 + 2 + 1 | 0 | PASS |
| Results | Structured IDs (grep ^R###) | 963 | 963 | 0 | PASS |
| Presentation | Slides (page markers [page 1]-[page 41]) | 41 | 41 | 0 | PASS |
| Presentation | NUMBER rows, spot-check of 20 slides (e.g. p8 = 20, p9 = 88, p10 = 122, p17 = 17, p20 = 16, p21 = 19, p36 = 54, p38 = 45, p39 = 18, p40 = 20) | 760 | Matches on every slide checked | 0 | PASS |
| Presentation | Structured IDs | 915 | 915 unique (921 ^R lines = 915 + 6 addendum correction lines, structured L933-938) | 0 | PASS |
| Presentation | Fulltext units with no structured row (MISSING_FROM_STRUCTURED) | 4 (M001-M004) | 10 (M001-M004 + 6 below) | n/a | **FAIL (A2)** |
| Press release | Table line items (pL80-100) / cells | 11 / 88 | 11 / 88 | 0 | PASS |
| Press release | Notes (pL102) / bullets (pL112-132) | 1 / 7 | 1 / 7 | 0 | PASS |
| Press release | Structured IDs | 180 | 180 | 0 | PASS |
| A4 citation | Ledger rows cited or marked reviewed | all | A4 preamble (review L18): "All ... 963 results rows, 41 slides (915 rows) and 180 press-release rows reviewed ... Unreviewed ledger rows: none"; YAML all_reviewed: true | 0 | PASS (blanket marking accepted) |

**Six fresh-pass units the ledger lacks (presentation; no structured row, no M-row; grep of the structured file for "TAM", "veteran", "Promoter-led", "willingness", "organised manufacturers" returns nothing):**

| New unit | Fulltext | Text | Type | Why it matters |
|---|---|---|---|---|
| M005 | p16 dL368-369 | "Product Superiority & Agility ... This innovation directly increases the customer's willingness to pay for refined, lightweight jewelry." | QUALIFIER / pricing-power claim | Quality-ladder (pricing power) input; no row, so A3/A4 never tested it |
| M006 | p17 dL384 | "Promoter-led operations with early steps toward professionalisation and governance strengthening" (FY23 self-description) | QUALIFIER / governance | Governance baseline the deck sets for itself |
| M007 | p17 dL393-394 | "Portfolio strengthened through strategic acquisitions, expanding TAM and product depth" | FORWARD / acquisition claim | Feeds the acquisition-economics probe (Audit 3) |
| M008 | p17 dL396-397 (right column) | "Board of Directors reinforced with industry veterans, alongside key leadership hires across domains" | ENTITY / governance claim | Distinct from R497 (dL402, left column, FY23 plan) |
| M009 | p19 dL433-435 | "The Indian jewellery industry continues to witness an increasing presence of organised manufacturers ... favourable backdrop" | QUALIFIER / sector claim | Only sector claim in the deck; R518 covers only the first sentence of dL433 |
| M010 | p19 dL446-447, dL455-456 | "Its asset-light advance gold model has helped minimize working capital intensity" and "advance gold model, which has contributed to positive operating cash flow generation and healthy returns on invested capital" | FORWARD / capital-raise rationale | The deck's stated reason the model funds itself; tested in Audit 3 against the payables-funded CFO |

A2's count test (ledger L8) states its independent sweep was a numeric-token sweep; M004 shows A2 also counts text claims, so these six fall under the same standard. Finding A5-M1 (MISSING, loop A2).

Uncited material rows. A4 marks every row reviewed, so there are no orphans by rule. Four uncited row groups carry content that produces surviving findings below: dR519-R520 (p19 capital-raise framing), dR523-R551 and dR553-R555 (p20 acquisition track record; only dR552 is cited), dR711-R712 (goodwill Rs 42.3 Cr Mar-25 to Rs 250.5 Cr Mar-26), and the NCI rows rR496-R501 as a perimeter measure. These are handled as A4 grafts (A5-M2, A5-M3, A5-M4), not as orphans.

---

## 2. ARITHMETIC AUDIT

All recomputations use full-precision lakh values from the RENDER-READ section. "Rounding" = difference vanishes when A4's own 2-decimal inputs are used.

### 2a. Consolidated P&L derived metrics

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY27 (PBT pre-exc + D + Fin - OI) | 189.77 | 173.3844 + 5.3239 + 25.4981 - 14.4328 = 189.77 | rL1183, L1180, L1179, L1173 | PASS |
| Op EBITDA Q1 FY27 / Q2 FY26 | 156.73 / 99.89 | 156.73 / 99.89 | same | PASS |
| Op EBITDA H1 FY27 / H1 FY26 / FY26 | 346.50 / 171.26 / 434.35 | 346.50 / 171.26 / 434.35 | same | PASS |
| Op EBITDA margin Q2 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 | 7.94% / 6.73% / 7.87% / 6.55% | 7.938% / 6.729% / 7.869% / 6.548% | + rL1172 | PASS |
| Reported EBITDA Q2 FY27 / FY26 | 196.85 / 470.74 | 196.85 / 470.74 | rL1185 | PASS |
| Core PBT ex-OI Q2 FY27 / Q2 FY26; pre-exceptional Q2 FY27 | 151.60 / 79.91; 158.95 | 151.60 / 79.91; 158.95 | rL1183-1185 | PASS |
| ETR Q2 FY27 / Q2 FY26 / H1 FY27 / FY26 | 22.09% / 23.78% / 22.13% / 25.65% | 22.09% / 23.78% / 22.13% / 25.65% | rL1189, L1185 | PASS |
| PAT margin Q2 FY27 / Q2 FY26 | 5.41% / 4.51% | 5.41% / 4.51% | rL1190 | PASS |
| Gross profit Q2 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 | 229.06 / 122.46 / 416.57 / 213.80 | 229.06 / 122.46 / 416.57 / 213.80 | rL1175-1177 | PASS |
| Gross margin Q2 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 | 9.58 / 8.25 / 9.46 / 8.17% | 9.58 / 8.25 / 9.46 / 8.17% | same | PASS |
| YoY revenue / Op EBITDA / core PBT / PAT / owners' PAT | +61.05% / +89.98% / +89.7% / +93.1% / +90.9% | +61.05% / +89.97% (89.98% on rounded inputs) / +89.72% / +93.08% / +90.87% | rL1172, L1190, L1200 | PASS (rounding) |
| EPS basic YoY | +88.6% | 8.26 / 4.38 = +88.6% | rL1211 | PASS |
| Within / outside India YoY; export mix | +46.9% / +183.9%; 18.19% vs 10.32% | +46.91% / +183.87%; 18.19% vs 10.32% | rL1313-1314 | PASS |
| Q1 FY26 derived revenue, margin; Q3+Q4 FY26 | 1,131.24, 6.31%; 3,679.19, 7.15% | 1,131.24, 6.309%; 3,679.19, 7.151% | rL1172, L1183 | PASS |
| Diag. 4: ETR saving on Q2 PAT | 2.81 | (23.785% - 22.091%) x 166.03 = 2.81 | rL1185, L1189 | PASS |

### 2b. Standalone and S-vs-C gap

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| SA Op EBITDA Q2 FY27 / Q2 FY26 / Q1 FY27 | 123.80 / 79.75 / 96.12 | 123.80 / 79.75 / 96.12 | rL1066, L1063, L1062, L1057 | PASS |
| SA Op EBITDA margin YoY | 6.79% vs 6.94% (-15 bps) | 6.785% vs 6.938% (-15 bps) | rL1056 | PASS |
| SA gross margin / ETR Q2 FY27 | 8.34% / 25.18% | 8.336% / 25.18% | rL1059-1060, L1070 | PASS |
| Revenue gap Q2 FY27 / Q2 FY26 | 566.11 / 335.04 | 566.11 / 335.04 | rL1172 vs L1056 | PASS |
| Op EBITDA gap Q2 FY27 / Q2 FY26 | 65.97 / 20.14 | 65.97 / 20.15 | derived | PASS (rounding) |
| Implied subsidiary margin Q2 FY27 / Q1 FY27 / Q2 FY26 | 11.65% / 10.58% / 6.01% | 11.65% / 10.58% / 6.01% | derived | PASS |
| PAT gap % SA PAT (Q2 FY26, Q1, Q2 FY27, H1 FY26, H1 FY27, FY26) | 22.18 / 73.14 / 51.52 / 26.50 / 60.49 / 32.45 | 22.18 / 73.14 / 51.52 / 26.49 / 60.49 / 32.45 | rL1071, L1190 | PASS (rounding) |
| Implied subsidiary ETR Q2 FY27 / Q2 FY26 | 15.31% / 24.76% | 7.9495 / 51.9298 = 15.31%; 4.003 / 16.1659 = 24.76% | rL1070, L1189 | PASS |
| Other-auditor subs' PAT share of cons PAT Q2 / H1 | 21.25% / 21.31% | 27.4884 / 129.3528 = 21.25%; 49.9294 / 234.2547 = 21.31% | rL669-670 | PASS |

### 2c. PAT bridge (Step 4)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Revenue contribution (906.20 x 8.2495%) | +74.76 | +74.76 | rL1172, derived GM | PASS |
| Gross-margin change (2,390.66 x 1.3321%) | +31.85 | +31.85 | derived | PASS |
| Employee + other expenses | -16.72 | -16.72 | rL1178, L1181 | PASS |
| Recurring operating subtotal; post-tax; share | +79.04; 60.24; 96.6% | +79.04; 60.24; 96.6% | derived | PASS |
| OI; exceptional; ETR effect | +6.44 (7.9%); -7.35 (-9.0%); +2.81 (4.5%) | +6.44 (7.87%); -7.35 (-8.99%); +2.81 (4.51%) | rL1173, L1184 | PASS |
| Reported PAT change | +62.36 | 129.3528 - 66.9931 = 62.36 | rL1190 | PASS |
| OI-reversion PAT; core at statutory tax | 124.33; 118.94 | 124.34; 118.95 | derived | PASS (rounding) |
| SA bridge ETR cost | 1.85 | 1.84 | rL1070, L1066 | PASS (rounding) |

### 2d. Cash flow and balance sheet (Step 5)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Cons CFO H1 FY27 / H1 FY26; change | 136.66 / (100.87); +237.53 | 136.66 / (100.87); +237.53 | rL1285 | PASS |
| Cons CFO/PAT | 0.58x / (0.91)x | 0.583x / (0.912)x | rL1285, L1190 | PASS |
| Cons CFO ex-payables | (208.62) / (139.44) | (208.62) / (139.44) | rL1271 | PASS |
| Cons capex; FCF | 17.72 / 55.02; 118.94 / (155.89) | 17.72 / 55.02; 118.94 / (155.89) | rL1286, L1289 | PASS |
| Cons WC change (cash generated - op profit before WC) | (187.90) / (242.73) | (187.90) / (242.73) | rL1283, L1270 | PASS |
| Cons receivable / inventory / payable days Sep-26; CCC | 35.5 / 41.5 / 18.1; 72.8 to 58.9 | 35.47 / 41.55 / 18.13; 72.85 to 58.89 | rL1226-1227, L1248-1249 | PASS |
| Gross borrowings; change | 847.87 to 939.45; +91.57 | 847.87 to 939.45; +91.57 | rL1241, L1246 | PASS |
| Net debt strict; change | 612.43 to 874.33; +42.8% | 612.43 to 874.33; +42.76% | rL1228-1229 | PASS |
| Net debt if OFA free | 593.61 to 492.01 | 593.62 to 492.01 | rL1231 | PASS (rounding) |
| Net debt / equity | 0.51x / 0.61x | 0.508x / 0.615x | rL1240 | PASS |
| Cash tax lag H1 | about 40 | 66.36 - 25.87 = 40.49 | rL1186, L1284 | PASS |
| SA CFO; CFO ex-payables | 22.11; (206.65) | 22.11; (206.65) | rL1150, L1136 | PASS |
| **SA WC change H1 FY26** | **(209.84)** | **(71.5029) - 138.5861 = (210.09)** | **rL1148 "(7,150.29)"; rL1135 "13,858.61"** | **FAIL** |
| **SA WC change, YoY delta** | **+20.22** | **(189.62) - (210.09) = +20.47** | **rL1135, L1148 (H1 FY27: 23,004.40; 4,042.28)** | **FAIL** |
| SA net debt strict; change | 466.08 to 733.94; +57.5% | 466.08 to 733.94; +57.47% | rL1098-1099, L1109, L1113 | PASS |
| SA borrowings rise vs net FD placement | 143.85 vs 147.43 | 143.85 vs 147.43 | rL1155-1156 | PASS |
| Equity-to-debt move (R-A3-14) | 17.32 | Other equity: 1,037.13 + 229.10 + 1.66 - 1,250.57 = 17.32; borrowings: 939.45 - (847.87 + 76.96 - 2.71) = 17.32 | rL1238, L1206, L1262, L1241, L1246, L1299, L1301 | PASS |

The SA WC error is internal to A4: A4's own 5-CF table carries the correct inputs (review L419: 138.59; L432: (71.50)), so 5-S contradicts 5-CF.

### 2e. Capital events, pillar facts, verdict-card items

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| QIP vs cons / SA equity; vs H1 PAT | 1.27x / 1.43x; 7.68x | 1.265x / 1.426x; 7.68x | rL46; rL1240; rL1108 | PASS |
| Market cap at Rs 858; new shares; increase; % post-issue | 13,288; 20,979,021; 13.55%; 11.93% | 13,288.18; 20,979,021; 13.546%; 11.930% | rL1080 | PASS |
| ESOP share of equity; intrinsic value | 0.0022%; 0.30 Cr | 0.00225%; 0.295 Cr | sL38, sL97 | PASS |
| ROCE FY26 deck-basis / all-debt | 36% / 22.3% | 457.91 / (2,195.03 - 923.53) = 36.0%; 457.91 / (1,205.88 + 847.87) = 22.3% | rL1185, L1179; rL1236, L1254, L1240-1246 | PASS |
| Deck Op PAT Q2 reconciliation | 134.90 | 129.3528 + 7.3549 x 0.7483 = 134.86 | rL1190, L1184; dL198 | PASS (rounding) |
| Trailing-4Q PAT (as labelled, incl. NCI) | 405.50 | 405.51 | rL1190 | PASS |
| **Trailing PE at CMP (Step 6.5-7 table)** | **32.8x on 405.50** | **Market cap prices owners' equity. Owners' trailing-4Q PAT = 275.32 - 110.58 + 231.15 = 395.89; 13,293 / 395.89 = 33.6x** | **rL1200 (27,532.49; 11,058.01; 23,114.88 lakhs)** | **FAIL (basis)** |
| Asset lines cleared (Flag 5) | 46.4 | 44.04 + (2.45 - 0.03) = 46.46 | rL1221, L1218 | STYLE (truncation) |

---

## 3. ADVERSARIAL READ

### Claim 1. "Growth is real at the core PBT level" / "Headline growth is operational, not treasury" / "96.6% of the PAT change comes from recurring core operations" (review L757, L248, L304)

Strongest bear counter, from the extract: part of the YoY growth is bought, and A4 does not strip it. The Q2 FY26 base excludes Shri Rishab (51%, acquired Dec-25, dR552 dL480). It carries Speed Bangle for two months at most (acquired Aug-25, dR551 dL475). The NCI line moves from nil in Q2 FY26 to 1.48 Cr in Q2 FY27 (rL1201: "-" vs 148.26 lakhs). Every subsidiary other than Shri Rishab is wholly owned (rL1335), so Shri Rishab's Q2 FY27 PAT is about 148.26 / 0.49 = 3.03 Cr [computed; assumes a 49% profit share]. That is 4.9% of the 62.36 Cr PAT change from one acquired entity alone. Speed Bangle's increment is not disclosed. Both are job-work entities (dR553-R554). A4 applies strip-out discipline to Purvi for Q3 (M7; 0D note SA 4) but not to the FY26 acquisitions inside the Q2 YoY. It mentions the Shri Rishab perimeter only for the S-vs-C gap (review L204).
Survives? YES, as a qualifier. "Real" holds at core PBT. "Organic" is not established, and organic growth is ND. **Graft into A4**: Step 2 verdicts, Diagnostic 3, Step 4 "Recurring" label, the VERDICT line and Brief Summary must state that YoY growth includes acquired entities (Shri Rishab absent from the base; Speed Bangle part-period). Give the NCI-implied 3.03 Cr and state organic growth ND. Add a management question on the inorganic contribution to Q2 revenue and PAT. Finding A5-M3 (MISSING, A4).

### Claim 2. "Trajectory: stepping up ... cons margin rose from 6.31% to 7.94% across five readings"; Op EBITDA margin +121 bps YoY (review L278, L216)

Strongest bear counter, from the extract: the five-reading window (Q1 FY26 to Q2 FY27) spans the consolidation of two job-work subsidiaries. Their revenue excludes metal, so their margin percentage is high by construction. Speed Bangle earned FY26 PAT 16.6 Cr on 42 Cr turnover, a 39.5% PAT margin (dR541, dR543 dL472-474; computed). Shri Rishab earned 18.8 Cr on 175 Cr, 10.7% (dR548, dR550 dL477-479). Adding them lifts the consolidated margin through mix, not through price or efficiency. This joins the two readings A4 already carries: the advance-gold denominator (dR513 dL418, D-A3-30) and the Q2 regroup (purchases of stock-in-trade -43.59, rL1176).
Survives? YES, in part. A4 states the job-work fact in the Brief (review L818) but never links it to the trajectory or to the +121 bps. **Graft into A4** Step 3 diagnostics and the Step 2 margin verdict as a third reading (perimeter mix). This is carried under A5-M3, with no separate loop.

### Claim 3. Guidance-delivery scorecard: "EBITDA margin 7.0-7.5% exceeded (7.94% Q2)", "PAT margin exceeded", "CFO/EBITDA 20%: delivered 39% H1", "Cash-flow neutrality completed early" (review L741-747; deck dR565-R576, press pL128)

Strongest bear counter, from the extract: CFO/EBITDA of 39.4% (136.66 / 346.50) becomes -60.2% without the payables build (-208.62 / 346.50). It is 27.8% net of the 40.49 Cr unpaid H1 current tax (rL1186 vs rL1284) [computed]. The guidance horizon for the 20% is not stated (A4 notes "horizon not found"). The margin "exceeded" rows compare a single quarter with undated guidance.
Survives? YES, but already incorporated. A4 carries the payables reading in Flag 1, Step 5-C and the adjacent register rows ("payables-funded"). Only the CFO/EBITDA register row lacks it. No graft beyond a STYLE fix (S4).

### MANDATORY ACQUISITION-ECONOMICS PROBE

**(a) Purvi Gems & Jewellery (India) Pvt Ltd, 100%, completed 07-Oct-2026.** Consideration Rs 9 Cr cash (pL130-132; dR439 dL290). Target revenue, PAT, net worth, ROCE, debt: NOT DISCLOSED in any of the five documents (rL556-557, rL1342; dL288-297; pL130-132; the EGM has no Purvi mention, eL87-946 grep). **Multiple: NOT COMPUTABLE (Rs 9 Cr / target PAT ND).** Size context: 9 / 234.25 = 3.8% of H1 FY27 cons PAT [computed]. Sellers are named only as "its existing shareholders" (rL557, rL1342). The deck sells it as "an established business, customer relationships, manufacturing capabilities and an experienced team" with Middle East export reach (dL293-297). Bear reading: at Rs 9 Cr, an "established business" is either immaterial to a Rs 6,295 Cr group, which would make the export claim overstated, or cheap for a reason (losses, liabilities, related sellers). A4 Q9 asks for financials and goodwill. It does not ask who the sellers are or whether they are related, although A4 itself flags a related-party history on the land sale (Q10, dR582). Survives as a MISSING question.

**(b) Deck p20 "Track Record of Successful Acquisitions" (dR523-R555 dL460-480): untested by A4.** This is the deck's most positive acquisition claim. A4 cites only dR552.

| Entity | Pre-deal (as stated) | FY26 (as stated) | Deal cash visible in corpus | Multiple | Read |
|---|---|---|---|---|---|
| Speed Bangle (acq. Aug-25; "Revenues mainly on job work basis") | Turnover 0.87, PAT 0.07 (Mar-25) | Turnover 42, PAT 16.6 (39.5% PAT margin) | H1 FY26 "Acquisition of Subsidiary (24.26)" lakhs = 0.24 Cr (rL1290; SA rL1157 "Investment in subsidiary company (24.26)"; cash acquired 14.91 lakhs rL1306) [INFERENCE: only acquisition dated inside H1 FY26 on dL475 and dL588-596] | 0.24 / 0.07 = 3.5x pre-deal PAT; 0.24 / 16.6 = 0.015x FY26 PAT | PAT rose 237x within about 8 months of purchase on job-work revenue. The earnings were not bought. They were created after the deal. |
| Shri Rishab Gold (51% via Starmangalsutra, acq. Dec-25; job work) | Turnover 49, PAT 1.60 (Mar-25) | Turnover 175, PAT 18.8 | Not disclosed | NOT COMPUTABLE | NCI-implied PAT: FY26 consolidated period 650.61 / 0.49 = 13.28 Cr in four months or less; H1 FY27 310.59 / 0.49 = 6.34 Cr, annualised 12.68 Cr, 33% below the deck's 18.8 Cr [computed; 49% profit share assumed]. The stated FY26 year looks like a peak, not a run-rate. |
| Goodwill (group) | 42.3 at Mar-25 (dR712 dL721) | 250.5 at Mar-26 (dR711; rL1219 250.51) | +208.2 Cr in FY26. Visible acquisition cash: 0.24 Cr in H1 FY26. Total H2 FY26 investing outflow was only -123.7 - (-74.98) = -48.7 Cr (dR850 dL754; rL1296) [computed] | n/a | FY26 owners' equity rose 508.2 Cr (683.8 to 1,192.0, dR772, dR771). Owners' TCI was 265.90 Cr (rL1206) and H1 FY26 equity cash 15.89 Cr (rL1297-1298), leaving 226.4 Cr not explained by profit or H1 cash [computed; H2 FY26 cash flow not in corpus]. Share capital was flat Sep-25 to Mar-26 (rL1080 15,486.39 vs 15,487.39 lakhs). [INFERENCE: FY26 acquisition consideration was settled largely in non-cash or deferred form; nature undisclosed.] |

Bear reading (survives). The "successful acquisitions" are small units bought cheaply whose post-deal PAT is mostly job-work income. If that work is billed to group companies, the profit moved out of the parent rather than arriving with the asset [INFERENCE]. The parent's margin fell 15 bps YoY while the implied subsidiary margin rose to 11.65% at a 15.31% implied ETR (review Step 1-G). This is the same mechanism behind A4 Flag 3, and the deck presents it as acquisition skill. The one entity with an outside read (Shri Rishab, via NCI) earns at a run-rate a third below its showcased year. FY26 goodwill rose 208.2 Cr with no matching visible cash, and the consideration is undisclosed. The QIP objects include "(c) investment in subsidiaries" and "(g) funding of acquisitions" (eL908; review CE-2), so acquisition economics bear directly on the use of the Rs 1,800 Cr. The bear reading survives and must be grafted.

**Graft into A4:**
1. Step 1-G read and Flag 3: name the p20 job-work entities as a source of subsidiary margin, with the multiples above or NOT COMPUTABLE.
2. Brief Business-model section: add the p20 claim and its counter.
3. CE-5: add a goodwill line, +208.2 Cr in FY26, consideration undisclosed.
4. New management question: consideration, mode of settlement and sellers for Speed Bangle and the 51% of Shri Rishab; source of the FY26 goodwill +208.2 Cr; share of subsidiary job-work revenue billed to group entities; Shri Rishab FY26 vs H1 FY27 PAT.
5. Q9: add Purvi seller identity and related-party status.

Finding A5-M2 (MISSING, A4).

### Additional surviving counter: deck p19 frames the raise itself (dR518-R520)

A4 Flag 4 reads "Reverses the deck's internal-funding statement" (review L763; YAML L928). The register lists "Expansion funded by internal cash | standing" (L741). The Brief says "The deck had said growth would be funded from internal cash" (L789). The deck does not hold that statement. It retires it: "Sky Gold had previously indicated that expansion would be supported through internal cash generation" (dL433). It then pre-frames a raise: "Similar capital-raising initiatives undertaken in the past have coincided with periods of business expansion ... supported by the company's asset-light advance gold model, which has contributed to positive operating cash flow generation and healthy returns on invested capital" (dL453-456, dR520). It does not name the QIP or the amount. The sharper bear point A4 misses: the company's stated reason the business can carry a raise is advance-gold cash generation. A4's own Step 5 shows H1 CFO turned positive only on a 345.28 Cr payables build (ex-payables -208.62).
Survives? YES. **Graft into A4**: correct Flag 4, the register status ("retired by the deck itself, p19") and the Brief line. Add to Flag 7: the deck pre-frames the raise without naming it, and its rationale rests on payables-funded CFO. Finding A5-M4 (MISSING, A4).

---

## FINDINGS REGISTER

| ID | Type | Gap | Loop | Moves a verdict-card number? |
|---|---|---|---|---|
| A5-F1 | FACTUAL | 5-S SA WC change H1 FY26 (209.84) should be (210.09); YoY delta +20.22 should be +20.47 (rL1135, rL1148). Contradicts A4's own 5-CF table | A4 | No |
| A5-F2 | FACTUAL | Step 6.5-7 trailing PE 32.8x uses PAT incl. NCI; on owners' trailing-4Q PAT 395.89 it is 33.6x (rL1200) | A4 | No (context row, deferred to Role 1) |
| A5-M1 | MISSING | Six presentation text units absent from structured and ledger: dL368-369, dL384, dL393-394, dL396-397, dL433-435, dL446-447/455-456 (log as M005-M010) | A2 | No |
| A5-M2 | MISSING | Acquisition-economics probe: Purvi multiple NOT COMPUTABLE and seller identity unasked; deck p20 track record untested (Speed Bangle 0.24 Cr vs 16.6 Cr PAT; Shri Rishab NCI-implied run-rate 12.68 vs 18.8 Cr; goodwill +208.2 Cr FY26 with no visible cash) | A4 | No (adds qualifier to Flag 3 and a question) |
| A5-M3 | MISSING | Perimeter qualifier absent from the growth and margin-trajectory claims (Shri Rishab not in base, NCI-implied 3.03 Cr Q2 PAT; Speed Bangle part-period; organic ND) | A4 | No (qualifies verdict-line wording) |
| A5-M4 | MISSING | Deck p19 (dL433, dL453-456) retires the internal-funding stance and pre-frames the raise on advance-gold cash generation; A4 Flag 4, register and Brief misstate this | A4 | No (Flag 4 and Flag 7 wording) |

No CONTRADICTION-tagged findings. A5-F1 is also an internal A4 inconsistency; it carries one tag, FACTUAL.

---

## VERDICT

**INCOMPLETE.**
- Failing agent, first in chain: **A2** (A5-M1, MISSING). Six presentation text-claim units are absent from the ledger.
- Then **A4**: two FACTUAL items (A5-F1 SA WC arithmetic; A5-F2 PE basis) and three MISSING surviving bear counters to graft (A5-M2 acquisition economics; A5-M3 perimeter; A5-M4 deck p19 raise framing).
- The A4 protocol verdict (PROCEED WITH FLAGS) and cash_conversion (INDETERMINATE-WITH-DIRECTION) are not challenged. No verdict-card number changes. All grafts add qualifiers, a goodwill line and management questions.

---

## STYLE NOTES (logged, no re-run)

- S1. Flag 5 and the YAML flag say "Rs 46.4 Cr of asset lines cleared". The sum is 44.04 + 2.42 = 46.46 (46.5 at one decimal). Name the two lines.
- S2. Flag 7 "H1 234.5 vs 243.46 sum" compares the release's H1 with its own Q1 + Q2 (104.9 + 138.56). A4's resolution table (review L32) names the deck's 239.8 as the correct H1. Cite both comparators so 243.46 is not read as the right figure.
- S3. Step 0C says "Share count flat; reported EPS = share-adjusted EPS". This holds for period-end shares only. Implied Q2 FY26 weighted shares are about 15.30 Cr (66.99 / 4.38) against 15.49 Cr, so EPS growth (+88.6%) trails owners' PAT growth (+90.9%). Add the weighted-average note.
- S4. The commitment register row "CFO/EBITDA 20% | delivered 39% H1" (L747) lacks the payables qualifier that the adjacent rows carry. Add: ex-payables -60.2%; 27.8% net of tax lag.
- S5. Step 5-C says "All of the fall is payables" (L328). On A4's own basis inventory days also fell 4.1 days, and payables explain 12.8 of the 13.9-day fall. The deck basis (dR081-R088) does support "all". Specify the basis.
- S6. "Q2 FY27 is its first review (dR452 L303)" (L98) and Flag 5 "First quarter under a new ... auditor". The deck says "The current quarter's financials have been reviewed by them" (dL303), not "first". The Q1 FY27 reviewer is unstated, and A4's own Q7 asks for it. Tag [INFERENCE].
- S7. EGM cut-off "11-Nov governs on three of four mentions" (L36, L561). The notice body repeats 11-Nov at eL518, eL527 and eL529, so the count understates the weight for 11-Nov. The conflict itself (eL47 vs eL53) is correctly flagged.

---

```yaml
stage: A5-adversary
company: "SKYGOLD"
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
    - "presentation p16 dL368-369: 'increases the customer's willingness to pay' (pricing-power claim), propose M005"
    - "presentation p17 dL384: 'Promoter-led operations with early steps toward professionalisation', propose M006"
    - "presentation p17 dL393-394: 'Portfolio strengthened through strategic acquisitions, expanding TAM and product depth', propose M007"
    - "presentation p17 dL396-397: 'Board of Directors reinforced with industry veterans, alongside key leadership hires', propose M008"
    - "presentation p19 dL433-435: 'increasing presence of organised manufacturers ... favourable backdrop' (sector claim), propose M009"
    - "presentation p19 dL446-447 and dL455-456: advance gold model credited with low WC intensity, positive operating cash flow and returns on invested capital, propose M010"
arithmetic_mismatches:
  - {metric: "SA working-capital change H1 FY26 (Step 5-S)", a4_value: "(209.84)", recomputed: "(210.09)", source_line: "results rL1148 (7,150.29) lakhs; rL1135 13,858.61 lakhs"}
  - {metric: "SA working-capital change YoY delta (Step 5-S)", a4_value: "+20.22", recomputed: "+20.47", source_line: "results rL1135, rL1148"}
  - {metric: "Trailing PE at CMP (Step 6.5-7 pillar table)", a4_value: "32.8x on PAT incl. NCI 405.50", recomputed: "33.6x on owners' trailing-4Q PAT 395.89", source_line: "results rL1200 (27,532.49; 11,058.01; 23,114.88 lakhs)"}
surviving_bear_counters:
  - {claim: "Growth is real at core PBT; 96.6% of PAT change recurring; cons margin stepping up 6.31% to 7.94% over five readings", counter: "YoY growth and the margin trajectory include acquired job-work entities: Shri Rishab absent from Q2 FY26 (NCI 1.48 implies ~3.03 Cr Q2 FY27 PAT, 4.9% of the 62.36 PAT change); Speed Bangle only from Aug-25 (FY26 PAT margin 39.5% on job work). Organic growth ND; A4 strips Purvi for Q3 but not FY26 acquisitions in Q2", source_line: "results rL1201, rL1335; presentation dL472-480 (dR541-R554)", type: "MISSING"}
  - {claim: "Deck p20 'Track Record of Successful Acquisitions' and Purvi as an 'established business' for Rs 9 Cr (acquisition-economics probe)", counter: "Purvi multiple NOT COMPUTABLE (PAT ND; sellers unnamed). Speed Bangle bought for ~0.24 Cr [INFERENCE] = 3.5x pre-deal PAT, 0.015x FY26 PAT; PAT up 237x in ~8 months on job work. Shri Rishab NCI-implied H1 FY27 run-rate 12.68 Cr vs 18.8 Cr showcased. Goodwill +208.2 Cr in FY26 with no visible cash; 226.4 Cr of FY26 equity rise unexplained. Post-deal PAT looks routed, not acquired; QIP objects include acquisitions", source_line: "presentation dL460-480, dL721, dL754, dL290-297; results rL1290, rL1157, rL1206, rL1201, rL1296-1298, rL557, rL1342; EGM eL908", type: "MISSING"}
  - {claim: "QIP reverses the deck's internal-funding statement (Flag 4; register 'standing')", counter: "The deck itself retires the stance ('had previously indicated') and pre-frames a raise on advance-gold 'positive operating cash flow generation', which A4 shows is payables-funded (ex-payables CFO -208.62)", source_line: "presentation dL433, dL453-456 (dR518, dR520); results rL1271, rL1285", type: "MISSING"}
  - {claim: "CFO/EBITDA 39% vs 20% guidance delivered (register)", counter: "Ex-payables CFO/EBITDA -60.2%; 27.8% net of 40.49 Cr unpaid H1 tax. Already carried elsewhere in A4; register row lacks the qualifier", source_line: "results rL1285, rL1271, rL1186, rL1284", type: "STYLE"}
findings_by_type:
  factual:
    - "A5-F1: Step 5-S SA WC change H1 FY26 (209.84) should be (210.09); delta +20.22 should be +20.47; contradicts A4's own 5-CF inputs (rL1135, rL1148). Loop A4. No verdict-card number moves"
    - "A5-F2: Step 6.5-7 trailing PE 32.8x uses PAT incl. NCI; owners' basis 395.89 gives 33.6x (rL1200). Loop A4. Context row only; no verdict-card number moves"
  missing:
    - "A5-M1: six presentation text units missing from structured and ledger (dL368-369, dL384, dL393-394, dL396-397, dL433-435, dL446-447/455-456); log as M005-M010. Loop A2. No verdict-card number moves"
    - "A5-M2: acquisition-economics probe not run in A4: Purvi multiple NOT COMPUTABLE, seller identity unasked; deck p20 track record untested; goodwill +208.2 Cr FY26 consideration undisclosed. Graft into Step 1-G, Flag 3, Brief, CE-5 and Q9 plus a new question. Loop A4. No verdict-card number moves"
    - "A5-M3: perimeter qualifier missing from growth and margin-trajectory claims (Shri Rishab NCI-implied 3.03 Cr Q2 PAT; Speed Bangle part-period; organic ND). Graft into Step 2, Diag 3, Step 3, Step 4, Verdict, Brief. Loop A4. No verdict-card number moves"
    - "A5-M4: deck p19 retires the internal-funding stance and pre-frames the raise on advance-gold cash generation; Flag 4, register row and Brief misstate it; add to Flag 7. Loop A4. No verdict-card number moves"
  contradiction: []
  style:
    - "S1: Flag 5 'Rs 46.4 Cr asset lines cleared' = 46.46; name the lines"
    - "S2: Flag 7 'H1 234.5 vs 243.46 sum'; also cite deck 239.8 as the correct H1"
    - "S3: Step 0C 'share count flat' holds at period end only; Q2 FY26 weighted shares ~15.30 Cr explain EPS +88.6% vs owners' PAT +90.9%"
    - "S4: register CFO/EBITDA 39% row lacks the payables qualifier carried elsewhere"
    - "S5: Step 5-C 'all of the fall is payables'; on A4's basis inventory days also fell 4.1"
    - "S6: 'Q2 FY27 is its first review' is an inference (dL303 says current quarter reviewed); tag [INFERENCE]"
    - "S7: EGM cut-off '11-Nov on three of four mentions' undercounts (eL518, eL527, eL529 also 11-Nov)"
loop_back_to: "A2"
gap: "A2: append six presentation text units as M005-M010 (dL368-369, dL384, dL393-394, dL396-397, dL433-435, dL446-447/455-456). A4: fix SA WC H1 FY26 to (210.09) and delta to +20.47; restate trailing PE on owners' PAT (33.6x); graft the acquisition-economics counter (Purvi multiple NOT COMPUTABLE, sellers; p20 Speed Bangle 0.015x FY26 PAT, Shri Rishab run-rate 12.68 vs 18.8; goodwill +208.2 Cr undisclosed consideration); add the perimeter qualifier to growth and margin claims; correct Flag 4, register and Brief for deck p19 raise framing."
style_notes:
  - "S1: name the two asset lines behind 46.4 (44.04 investments; 2.42 investment property; sum 46.46)"
  - "S2: Flag 7 should cite deck H1 Op PAT 239.8 alongside 243.46"
  - "S3: note weighted-average share effect on Q2 FY26 EPS"
  - "S4: add payables qualifier to the CFO/EBITDA register row"
  - "S5: state the basis for 'all of the fall is payables'"
  - "S6: tag 'first review by MSKA' as [INFERENCE]"
  - "S7: EGM cut-off count understates 11-Nov mentions"
analyst_note: "A4's numbers tie: over 120 derived metrics recomputed, two errors, neither on the verdict card. The gaps are reads, not sums. A4 never ran the acquisition test on deck slide 20. That slide is the cleanest window into its own Flag 3. Speed Bangle was bought for about Rs 0.24 Cr and earned Rs 16.6 Cr PAT within months on job work. Shri Rishab's NCI-implied run-rate is a third below its showcased year. Goodwill rose Rs 208.2 Cr in FY26 with no visible cash. The subsidiary margin may be routed, not acquired, and the Rs 1,800 Cr objects include acquisitions. The A2 gap is low-materiality text claims. The orchestrator may batch it as a ledger append ahead of the A4 grafts. Verdict PROCEED WITH FLAGS and cash conversion stand."
```

---

# LOOP 1 RE-AUDIT (2026-10-29)

Stage: A5 adversary, loop 1 (the one permitted re-audit) | Model: claude-opus-5-5
Inputs read: revised review runs/skygold-q2fy27/work/review_skygold_q2fy27.md (1,010 lines; LOOP 1 CHANGE LOG at review L62-77); pre-loop review C:/Users/SUMITS~1/AppData/Local/Temp/claude/C--Users-SUMIT-SHARMA-repos-inflection-pipeline--claude-worktrees-qr-skygold-q2fy27-7e1298/d9051429-736b-463a-9ce7-54ec436764e1/scratchpad/review_loop0.md (938 lines); presentation ledger M001-M017 (ledger L1007-1027); presentation fulltext and structured. No source PDF and nothing under inputs/ was opened. Review line numbers below (Lnnn) refer to the revised review.

## L1-A. Status per loop-0 finding (re-derived, not taken from the change log)

| ID | Type | Loop-1 evidence in the review | A5 re-derivation | Status |
|---|---|---|---|---|
| A5-F1 | FACTUAL | L401: 5-S WC change "(210.09) ... (189.62) ... +20.47" | 5-CF inputs L473 138.59 and L486 (71.50): -71.5029 - 138.5861 = (210.09); (189.62) - (210.09) = +20.47 (rL1135, rL1148). 5-S now agrees with 5-CF. Old figures appear nowhere else (grep) | RESOLVED |
| A5-F2 | FACTUAL | L598: owners' trailing-4Q PAT 395.89; PE 33.6x; incl.-NCI 405.50 / 32.8x kept as a labelled alternative | 275.32 - 110.58 + 231.15 = 395.89 (rL1200); 13,293 / 395.89 = 33.58x, rounds to 33.6x | RESOLVED |
| A5-M1 | MISSING | Ledger M005-M010 = A5's six units at the same lines; A2 added M011-M017 from a second sweep; review preamble L18 and disposition table L24-44 cover all 17 | Each of M005-M017 checked at its fulltext line (see L1-B). M011-M017 grep-confirmed absent from the structured file | RESOLVED |
| A5-M2 | MISSING | Step 1-G table and read L246-256; Flag 3 L821; CE-5 L682-685; Brief part 3 L880-885; Q9 L732 (sellers and related-party status added); new Q20 L743 | 16.6 / 42 = 39.5%; 0.24 / 0.07 = 3.5x; 0.24 / 16.6 = 0.015x; 310.59 / 0.49 = 6.34, x2 = 12.68, 32.6% below 18.8; 22.3 + 22.9 + 16.6 + 18.8 = 80.6 = 28.6% of 281.83; 250.5 - 42.3 = 208.2; 9 / 234.25 = 3.8%. Purvi multiple NOT COMPUTABLE, as required. [INFERENCE] tags kept | RESOLVED |
| A5-M3 | MISSING | Step 2-C verdicts L266, L268, L273, L275; perimeter note L278; Diag 3 L302; Step 3 L332; Step 4 L349, L358; VERDICT L816; Brief L839-840; new Q21 L744 | 148.26 / 0.49 = 302.57 lakhs = 3.03 Cr; 3.03 / 62.36 = 4.9%. Organic stated ND throughout. Perimeter mix added as third margin reading | RESOLVED |
| A5-M4 | MISSING | Flag 4 L822; Flag 7 L825; register row L800 ("retired by the deck itself"); Brief L850 | Quotes match dL433 ("had previously indicated") and dL453-456. Flag 7 now ties the raise rationale to payables-funded CFO | RESOLVED |
| S2 / S4 | STYLE | Flag 7 L825 cites 243.46 and 239.8; register L806 carries "ex-payables -60.2%; 27.8% net of the 40.49 unpaid H1 current tax" | (208.62) / 346.50 = -60.2%; (136.66 - 40.49) / 346.50 = 27.75% | APPLIED |
| S1, S3, S5, S6, S7 | STYLE | Untouched by design (change log L76) | Still as logged | OPEN, logged, no loop |

Supporting detail not carried (acceptable): the M2 graft omits A5's FY26 owners'-equity bridge (226.4 Cr not explained by TCI or H1 cash). The review's [INFERENCE] on non-cash or deferred consideration rests instead on "no matching acquisition cash visible". The conclusion and the management question (Q20) are unchanged by the omission.

## L1-B. New ledger rows M005-M017 checked against the presentation fulltext

| Unit | Ledger line cite | Fulltext check | Absent from structured? | Result |
|---|---|---|---|---|
| M005 | 368-369 | dL368-369 "Product Superiority & Agility ... willingness to pay" | Yes (loop 0 grep) | OK. Cosmetic: the ledger says R468-R470 cover "ERP, value-added share and recognition"; recognition is R471 (S9) |
| M006 | 384 (continues 386) | dL384, dL386 | Yes | OK |
| M007 | 393-394 | dL393-394 | Yes | OK |
| M008 | 396-397 | dL396-397 right column | Yes | OK |
| M009 | 433-435 | dL433-435 | Yes | OK |
| M010 | 446-447, 455-456 | dL446-447, dL455-456 | Yes | OK |
| M011 | 296-297 | dL296-297 "Provides access to an established business ..." | Yes (grep "established business": none) | OK |
| M012 | 305-306 | dL305-306 (continues dL307 "industries.") | Yes (grep "risk-based": none) | OK |
| M013 | 347 | dL347 | Yes (grep "technological innovation": none) | OK |
| M014 | 351-353 | dL351-353 "significant competitive moat" | Yes (grep "competitive moat": none) | OK |
| M015 | 413 | dL413 "progressively upgraded our guidance" | Yes (grep: none) | OK |
| M016 | 418-419 | Quoted words sit on dL419-420 ("eliminates inventory risk ... minimal / balance sheet impact") | Yes (grep "eliminates inventory": none) | OK (anchor within the A1 +-2 line convention) |
| M017 | 615-618 | dL615-618; fulltext says "technical mastery in plant and machinery", not "investment in plant and machinery" | Yes (grep "plant and machinery": none; "automation" hits only R497 at dL402) | OK. Cosmetic paraphrase error (S9) |

Coverage re-run (presentation, units with no structured row): ledger 17, A5 fresh 17 (A5's 10 from loop 0 plus M011-M017 verified). Orphan rows 0. Results and press-release ledgers unchanged since loop 0. Status: PASS.

## L1-C. Drift check (pre-loop vs revised, section by section)

| Section | Change found | In the change log? | Drift? |
|---|---|---|---|
| Header L1-12; A3 cross-document resolution table | None | n/a | No |
| Preamble L18; new M-unit disposition table L24-44 | Count text and table added | Yes (Ledger row) | No |
| LOOP 1 CHANGE LOG L62-77 | New | n/a | No |
| Step 0A-0E; 1-C, 1-C derived, 1-S, 1-S derived; 1-G table and first read paragraph | None | n/a | No |
| Step 1-G acquisition-economics read L246-256 | New | Yes (A5-M2) | No |
| Step 2-C | Verdict cells for revenue, margin, core PBT, PAT; perimeter note. The margin cell also names the deck's value-added-mix claim (MGMT, dR469) as a first reading | Yes (A5-M3) | No. The added reading is MGMT-sourced, sits inside a patched cell, and changes no number |
| Step 2-S; Diagnostics 1, 2, 4, 5, 6 | None | n/a | No |
| Diagnostic 3; Step 3 first diagnostic | Perimeter qualifier | Yes (A5-M3) | No |
| Step 4 | Recurring-subtotal label; first mandatory answer | Yes (A5-M3) | No |
| Step 5 (5-C, 5-BS, 5-CF, mandatory questions) | 5-S WC row only | Yes (A5-F1) | No |
| Steps 5.5, 6A-6D | None | n/a | No |
| Step 6.5/7 table | Earnings-base row only | Yes (A5-F2) | No |
| CE-1 to CE-4 | None | n/a | No |
| CE-5 | Purvi row extended; Speed Bangle, Shri Rishab 51% and goodwill rows added | Yes (A5-M2) | No |
| Step 8, 8B, 8C; Step 9; Monitorables M1-M18 | None | n/a | No |
| Step 8.5 | Q9 extended; Q20, Q21 added; Q1-Q8 and Q10-Q19 unchanged | Yes | No (see S8 on routing) |
| Commitment register | Internal-cash row and CFO/EBITDA row only | Yes (A5-M4, S4) | No |
| VERDICT | Opening line; Flags 3, 4, 7. Flags 1, 2, 5, 6, 8, 9 unchanged | Yes | No |
| Brief | Part 1: two lines added (L839-840), one line replaced (L850). Part 3: six lines added (L880-885). Parts 2, 4, 5 unchanged | Yes | No |
| YAML | loop: 1; loop_1_fixed; deck_missing_units_reviewed: 17; Q9, Q20, Q21; flags 3, 4, 7. analyst_note and monitorables unchanged | Yes | No |

Verdict-card numbers checked unchanged: 136.66, 345.28, 208.62, 874.33, 492.01, 382.32, 11.65%, 6.01%, 15.31%, 51.52%, 21.25%, 1,800, 1.27x, 13.55%, 7.35, 17.32, 46.4, 22.09%, 25.17%, 36% / 22.3%. Protocol verdict PROCEED WITH FLAGS and cash_conversion INDETERMINATE-WITH-DIRECTION are unchanged. **Result: no drift in substance.**

## L1-D. Audit 0 re-run (brief gate)

| Part | Heading | Content | Status |
|---|---|---|---|
| 1. Summary narrative | L835 | 20 lines (L837-856), at the top of the 10-20 band | PRESENT |
| 2. Sector | L858 | Unchanged, 12 lines | PRESENT |
| 3. Business model | L873 | 19 lines incl. the acquisition graft | PRESENT |
| 4. Competition | L895 | Unchanged, 12 lines | PRESENT |
| 5. Forward map | L910 | Make-or-break reading plus 9 dated catalysts, each with Bull and Bear | PRESENT |

Gate result: PASS.

## L1-E. Arithmetic on numbers new in loop 1

| Metric | Review value | Recomputed | Source line | Status |
|---|---|---|---|---|
| SA WC change H1 FY26; delta | (210.09); +20.47 | (210.09); +20.47 | rL1135, rL1148 | PASS |
| Owners' trailing-4Q PAT; PE | 395.89; 33.6x | 395.89; 33.58x | rL1200 | PASS |
| Shri Rishab Q2 FY27 PAT (NCI-implied); share of PAT change | 3.03; 4.9% | 3.03; 4.86% | rL1201 | PASS |
| Shri Rishab H1 FY27 PAT; annualised; gap to 18.8 | 6.34; 12.68; 33% | 6.34; 12.68; 32.6% | rL1201; dL479 | PASS |
| Speed Bangle PAT margin; multiples | 39.5%; 3.5x; 0.015x | 39.5%; 3.47x; 0.0146x | dL472-474; rL1290 | PASS |
| Four acquired entities' FY26 PAT; share of cons | 80.6; 28.6% | 80.6; 28.60% | dL464-479; rL1190 | PASS |
| Goodwill rise FY26 | +208.2 | 250.5 - 42.3 = 208.2 | dL721 | PASS |
| Purvi price vs H1 PAT | 3.8% | 9 / 234.25 = 3.84% | pL132; rL1190 | PASS |
| CFO/EBITDA ex-payables; net of tax lag | -60.2%; 27.8% | -60.21%; 27.75% | rL1285, rL1271, rL1186, rL1284 | PASS |

No mismatch above rounding.

## L1-F. New findings (loop 1)

| ID | Type | Finding | Fix | Loop |
|---|---|---|---|---|
| S8 | STYLE | Q20 and Q21 were added but the routing text was not aligned. L720 "Q1-Q8 for live Q&A; Q9-Q19 in writing"; L751 "Submit Q3, Q5-Q19 in writing"; L768 M1 "questions Q1-Q19"; L979 YAML monitorable "Q1-Q19 answers". Q20 carries the A5-M2 acquisition-consideration question, so an operator who follows the routing line alone would not send it. Logged as STYLE because both questions sit in the table and the YAML payload, and no number, fact or verdict changes | Extend each range to Q21 and route Q20 and Q21 in writing (or ask Q20 live) | none |
| S9 | STYLE (A2 ledger) | M017 paraphrases dL615 "technical mastery in plant and machinery" as "investment in plant and machinery". M005 names R468-R470 for "recognition"; recognition is R471 | Correct the paraphrase and the row range at the next ledger touch | none |

No new FACTUAL, MISSING or CONTRADICTION finding.

## L1-G. VERDICT (loop 1)

**COMPLETE.** All six loop-0 findings (A5-F1, A5-F2, A5-M1, A5-M2, A5-M3, A5-M4) are RESOLVED. I found no drift, the brief gate passes, and the coverage re-run passes. Open items are STYLE only (S1, S3, S5, S6, S7 from loop 0; S8, S9 new) and are logged without a re-run. The review may proceed to the Notion save gate.

```yaml
stage: A5-adversary
company: "SKYGOLD"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
loop: 1
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
loop1_resolved:
  - "A5-F1 RESOLVED: Step 5-S SA WC change H1 FY26 (210.09), delta +20.47 (review L401; rL1135, rL1148)"
  - "A5-F2 RESOLVED: trailing PE 33.6x on owners' trailing-4Q PAT 395.89; incl.-NCI 32.8x labelled alternative (review L598; rL1200)"
  - "A5-M1 RESOLVED: ledger M005-M017 present; M005-M010 match A5 units; M011-M017 verified at fulltext and absent from structured"
  - "A5-M2 RESOLVED: acquisition-economics graft in Step 1-G, Flag 3, CE-5, Brief part 3, Q9, Q20; multiples re-derived; Purvi NOT COMPUTABLE"
  - "A5-M3 RESOLVED: perimeter qualifier in Step 2-C, Diag 3, Step 3, Step 4, Verdict, Brief part 1, Q21; NCI-implied 3.03 Cr re-derived"
  - "A5-M4 RESOLVED: Flag 4, Flag 7, register row and Brief corrected to the deck p19 framing (dL433, dL453-456)"
  - "S2, S4 APPLIED"
drift: "none in substance; all changes sit at change-logged points; verdict-card numbers, protocol verdict and cash_conversion unchanged"
findings_by_type:
  factual: []
  missing: []
  contradiction: []
  style:
    - "S1 (open): Flag 5 'Rs 46.4 Cr asset lines cleared' = 46.46; name the lines"
    - "S3 (open): Step 0C 'share count flat' holds at period end only; Q2 FY26 weighted shares ~15.30 Cr"
    - "S5 (open): Step 5-C 'all of the fall is payables'; on A4's basis inventory days also fell 4.1"
    - "S6 (open): 'Q2 FY27 is its first review' is an inference; tag [INFERENCE]"
    - "S7 (open): EGM cut-off '11-Nov on three of four mentions' undercounts"
    - "S8 (new): Q20 and Q21 not routed; review L720, L751, L768 and YAML L979 still read Q1-Q19 / Q9-Q19 / Q5-Q19"
    - "S9 (new, A2 ledger): M017 paraphrase 'investment' vs fulltext 'technical mastery' (dL615); M005 row range omits R471"
loop_back_to: ""
gap: ""
style_notes:
  - "S1: name the two asset lines behind 46.4 (44.04 investments; 2.42 investment property; sum 46.46)"
  - "S3: note weighted-average share effect on Q2 FY26 EPS"
  - "S5: state the basis for 'all of the fall is payables'"
  - "S6: tag 'first review by MSKA' as [INFERENCE]"
  - "S7: EGM cut-off count understates 11-Nov mentions"
  - "S8: extend question ranges to Q21 at review L720, L751, L768, L979 and route Q20-Q21 in writing"
  - "S9: correct M017 paraphrase and M005 row range in the presentation ledger"
analyst_note: "Loop 1 closes every loop-0 finding. I re-derived each patched number from the fulltext rather than the change log, and all tie within rounding. The section-by-section diff against the pre-loop text shows changes only at change-logged points. Verdict-card numbers, PROCEED WITH FLAGS and the cash-conversion call are unchanged. The ledger grew to 17 M-units. A2's second sweep found seven more beyond A5's six, and each checks out at its fulltext line. One omission is acceptable: the graft drops A5's FY26 equity-bridge support for the non-cash-consideration inference, but Q20 still asks the question. Fix S8 before the call: Q20 and Q21 exist but the routing lines still stop at Q19, and Q20 is the acquisition-consideration question."
```
