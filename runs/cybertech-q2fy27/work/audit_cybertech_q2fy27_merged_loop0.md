# A5 AUDIT: CYBERTECH Q2 FY27 (merged review: results + press release + earnings presentation)

Company: Cybertech Systems and Software Limited (CYBERTECH). Quarter: q2fy27. Auditor model: claude-opus-5-5.
Under audit: runs/cybertech-q2fy27/work/review_cybertech_q2fy27.md (894 lines; cited "review Lnnn").
Inputs read: A1 fulltexts (results "L", press release "PR L", deck "D L"), A1 structured files (results R001-R739, PR R001-R141, deck R001-R326), the three A2 ledgers, the A4 review.
Input discipline: no source PDF, nothing under inputs/, no A3 file, no base review or base audit opened. Every number below is re-derived from the fulltext lines cited.
Units: results in Rs lakh (L98); release and deck in INR mn (PR L93, D L269). 100 lakh = 1 Cr.

---

## 0. DELIVERABLE-COMPLETENESS AUDIT (hard gate)

| Part | Present? | Where | Content check |
|---|---|---|---|
| 1. Summary narrative | present | review L728-L743 | 14 lines (inside the 10-20 line band); numbers, bear reading, verdict, next test |
| 2. Sector intelligence | present | review L745-L755 | 9 bullets, evidence-tiered (FILED / MGMT / SECONDARY / INFERENCE) |
| 3. Business-model intelligence | present | review L757-L767 | 9 bullets; cost structure, headcount, clients, treasury, drift |
| 4. Competition intelligence | present | review L769-L777 | 7 bullets; partners, peer set marked PENDING LIVE VERIFICATION |
| 5. Forward map | present | review L779-L797 | 11 catalysts, each with a bull and a bear fork; 8 dated, 3 event-driven or undated |

Gate result: PASS. All five parts present and non-empty.

---

## 1. COVERAGE AUDIT

Method: fresh line-by-line pass over each fulltext, counted against the A2 ledger and the A1 structured IDs.

### 1A. Results (Reg 33)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Notes | 7 | 7 (Notes 1-6 at L430-L436, Note 5 para 2 at L435) | none | PASS |
| Line items | 191 | 191 (cons P&L 23 lines L100-L128; cons BS 37 L142-L189; cons CF 38 L201-L242; SA P&L 21 L286-L311; SA BS 36 L324-L370; SA CF 36 L382-L421) | none | PASS |
| Embedded numbers | 42 | 42 with rows; 4 admin identifiers have no row (Lodha telephones L62, L252; company tel/fax on L96, L282) | none | PASS (STYLE S-1) |
| Agenda items | 1 | 1 (L36-L40) | none | PASS |
| Auditor paragraphs | 7 | 7 (consolidated paras 1-4 L68-L78; standalone paras 1-3 L258-L264) | none | PASS |
| Entities | 46 | 46; no material entity outside the rows (address fragments only) | none | PASS |
| Forward statements | 3 | 3 (L434-L435) | none | PASS |
| Dates | 51 | 47 dated occurrences + 4 statute years (R690-R693) = 51; L33 subject-line date has no own row (restates R673) | none | PASS (STYLE S-2) |
| Qualifiers | 46 | 46 | none | PASS |
| Signature blocks | 10 | 10 (9 auditor stamps L83, L133, L194, L247, L269, L316, L375, L426, L443; CS stamp L51) | none | PASS |
| Turns / questions | 0 | 0 (no concall) | n/a | PASS |
| Structured IDs | 739 | 739 referenced in ledger | 0 | PASS |

### 1B. Press release (run as presentation-class)

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Pages | 4 | 4 ([page 1]-[page 4]) | none | PASS |
| Table line items | 14 | 14 (Q2 table PR L94-L101, 8 rows; H1 table PR L106-L111, 6 rows) | none | PASS |
| Table cells | 55 | 55 (Q2 37 = 5 value rows x 5 + 3 margin rows x 4; H1 18 = 6 rows x 3) | none | PASS |
| Notes | 1 unnumbered | 1 ("Note:" PR L140) | none | PASS |
| Numbers | 79 | 79 (12 quote/headline, 55 cells, 4 highlights PR L115-L122, founding PR L129, 7 admin) | none | PASS |
| Entities | 23 | 23; dateline "Mumbai, India" (PR L59) is a dateline, not an entity | none | PASS |
| Forward / qualifiers / dates | 13 / 13 / 13 | 13 / 13 / 13 | none | PASS |
| Structured IDs | 141 | 141 | 0 | PASS |

### 1C. Earnings presentation

| Category | A2 count | Fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 16 | 16 ([page 1]-[page 16]) | none | PASS |
| Slide numbers | 205 | 205 (slide 5: 3; slide 9: 1; slide 11: 12; slide 12: 21; slide 13: 18; slide 14: 6; slide 15: 143 cells + face value R314) | none | PASS |
| Slide 15 line items | 22 | 22 numeric lines in the image-verified block D L309-L337; D L334 Other equity is blank and carries no row by A1 convention | none | PASS |
| Footnotes / qualifiers | 18 | 18 | none | PASS |
| Forward | 1 | 1 (D L35-L41, safe harbour only) | none | PASS |
| Dates | 24 | 24 | none | PASS |
| Entities | 73 + 5 summary | 78 | none | PASS |
| ZERO_STANDING | 13 (+R256 near-zero) | 13 (+1) | none | PASS |
| Structured IDs | 326 | 326 | 0 | PASS |

Ledger-level totals tie to the A4 preamble (review L48): 8 notes (7 results + 1 release), 0 turns, 20 slides (16 deck + 4 release pages).

### 1D. Ledger rows vs A4 citation

A4 marks every row reviewed in its preamble (review L48-L54: 739 of 739, 141 of 141, 326 of 326; "No row is unreviewed"). I accept that explicit blanket mark as "reviewed". I then tested every A2 flag for a matching A4 treatment:

| A2 flag | A4 treatment | Status |
|---|---|---|
| Results ZERO_STANDING (L114, L118, L145, L147, L178, L209, L210, L234, L235, L405, L406) | cited (review L122-L134, L172-L179, L425, L454) | PASS |
| SIGNATURE_BEFORE_MEETING_CLOSE (R663-R671) | review L142 | PASS (STYLE S-9) |
| AGENDA_NOT_LISTED | review L702 (one agenda item), L134 (no dividend mentioned) | PASS |
| ENTITY_WORDING_DIFF (Canada step-down) | review L122 (A3-18) | PASS |
| ENTITY_UNNAMED (R624) | review L133, L468 | PASS |
| FOOTNOTE_UNRESOLVED R652 (31-09-2025) | review L883 | PASS |
| PR DATE_MISMATCH (R080 vs R084) | review L89 | PASS |
| PR PARTNER_TIER_CONFLICT | review claim 8 (L531), QfM 23 | PASS |
| PR NO_QUANT_GUIDANCE / UNQUANTIFIED_CLAIM R117 | review L20, L346; claim 3 (L526) | PASS |
| PR UNAUDITED_SOURCE / blank margin YoY cells | review L142, L541 | PASS |
| Deck FOOTNOTE_UNRESOLVED R164, R165 | review L278-L281 | PASS |
| Deck ZERO_STANDING-NEAR R256 | review L425 | PASS |
| Deck R284 duplicate OCI caption | not named for the deck (results A3-17 only) | PASS (STYLE S-5) |
| Deck R296 paid-up change | review L105 | PASS |

Line groups with no line or ID cite, carried only by the blanket mark, each tested and none holding a finding: results L119, L143, L148, L150-L151, L158, L160-L162, L175, L187-L189, L201, L203, L205, L207-L208, L213, L225, L227-L229, L231, L236-L242 and their standalone counterparts (for example L304-L305, L386, L404, L407). STYLE S-4 asks A4 to list them as "reviewed, no finding".

Coverage result: orphan_rows = [], missing_from_ledger = []. PASS.

---

## 2. ARITHMETIC AUDIT

All values recomputed from the lakh figures on the cited lines.

### 2A. Recomputed and PASS

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Op EBITDA Q2 FY26 / Q1 FY27 / Q2 FY27 / FY26 / H1 FY26 / H1 FY27 (lakh) | 461.92 / 571.89 / 808.87 / 1,874.37 / 955.25 / 1,380.76 | same | L101, L106, L107, L110 | PASS |
| Op EBITDA margin | 7.86% / 8.36% / 11.04% / 7.90% / 8.17% / 9.74% | 7.858% / 8.355% / 11.036% / 7.904% / 8.166% / 9.741% | L100 | PASS |
| Reported EBITDA margin on total income | 18.8% / 18.1% / 16.4% / 17.0% / 18.6% / 17.3% | 18.83% / 18.14% / 16.43% / 16.97% / 18.60% / 17.28% | L102; PR L97 | PASS |
| Core PBT ex-OI (lakh) | 345.66 / 442.98 / 681.20 / 1,434.16 / 724.07 / 1,124.18 | same | L101, L110 | PASS |
| OI / PBT | 69.69% / 64.89% / 40.99% / 64.34% / 67.43% / 53.47% | same | L101, L110 | PASS |
| ETR | 24.10% / 24.88% / 24.83% / 24.35% / 24.31% / 24.86% | 24.098% / 24.875% / 24.835% / 24.345% / 24.308% / 24.856% | L110, L112-L114 | PASS |
| PAT margin | 14.72% / 13.85% / 11.84% / 12.83% / 14.39% / 12.81% | same | L100, L115 | PASS |
| SA Op EBITDA (lakh) and margin | 416.87 10.46% / 511.87 11.63% / 482.26 10.94% / 1,589.93 9.91% / 758.32 9.54% / 994.13 11.28% | same | L286-L296 | PASS |
| SA core PBT, OI/PBT, ETR, PAT margin | as review L229-L232 | same (Q2 FY26 OI/PBT 60.885%, rounds 60.89%) | L286-L301 | PASS |
| Sub revenue, Op EBITDA, OI, PAT, S-C gap, sub PAT share (1C, six periods) | review L240-L245 | same (S-C gap 33.61% / 59.47% / 60.56% / 49.03% / 59.99% / 30.21%) | L100-L115 less L286-L301 | PASS |
| Sub revenue YoY; perimeter share of YoY revenue and Op EBITDA growth | +54.3%; 70.8%; 81.2% | +54.33%; 70.85%; 81.15% | L100, L286 | PASS |
| Industry implied revenue (1D, 12 cells) and QoQ/YoY | review L265-L268 | same (Technology +1.13% QoQ; Government +46.0% QoQ, +107.8% YoY) | D L247 x L100 | PASS |
| YoY: revenue, Op EBITDA, EBIT, OI, core PBT, PBT, PAT, EPS (2A) | +24.7%, +75.1%, +97.5%, -40.5%, +97.1%, +1.2%, +0.3%, +2.9% | +24.68%, +75.11%, +97.52%, -40.45%, +97.07%, +1.24%, +0.25%, +2.88% | L100-L127 | PASS |
| SA YoY (2B) | review L332-L342 | same | L286-L310 | PASS |
| Cost ratios YoY (2C item 2) | -209 / -73 / -36 bps; sum 318 | -209.0 / -73.1 / -35.7 bps | L104, L105, L108 | PASS |
| PAT bridge 4A (seven components, sum 2.19) | 114.02 / 232.93 / 12.32 / -23.73 / -321.45 / -3.40 / -8.50 | same; sum 2.19 = L115 867.73 - 865.54 | L100-L115 | PASS |
| PAT bridge 4B (sum -107.37) | 44.24 / 21.15 / 4.04 / -26.06 / -178.46 / +32.34 / -4.62 | same; sum -107.37 = L301 | L286-L301 | PASS |
| CFO/PAT headline | 0.98x / 1.56x | 0.977x / 1.557x | L222, L115 | PASS |
| Matched pre-WC CFO/PAT | 1.05x-1.15x / 1.20x-1.23x | 1.053x, 1.145x / 1.200x, 1.226x (removed income 977.74 and 729.95 lakh tie) | L204-L214, L221 | PASS |
| FCF; WC release share of Op EBITDA | 13.87 / 27.83 Cr; 94.6% | 1,387.32 / 2,782.77 lakh; 94.57% | L222, L224, L219 | PASS |
| Receivable / payable days; CCC | 53.4 / 44.5; 105.1 / 102.6; -51.6 / -58.0 | 53.45 / 44.51; 105.09 / 102.56; -51.64 / -58.04 | L155, L181-L182, L104, L108 | PASS |
| Consolidated net cash | 169.59 / 167.92 Cr | 16,959.49 / 16,792.44 lakh | L147, L154, L156, L157, L178 | PASS |
| SA CFO/PAT, FCF, receivable days | 2.89x / 3.65x; 30.20 / 41.25 Cr; 69.1 / 21.0 | 2.891x / 3.654x; 3,019.96 / 4,125.08 lakh; 69.08 / 20.98 | L401, L403, L337 | PASS |
| Other equity gap (standalone; consolidated) | 1,215.22 lakh = Rs 4.00 x 3,03,80,600 | 11,793.41 + 1,134.74 - (1,498.00 - 85.00) + (47.60 - 10.00) = 11,552.75; less 10,337.53 = 1,215.22. Consolidated 18,749.91 - 17,534.67 = 1,215.24 | L348, L301, L415, L414, L124, L167, L123 | PASS |
| Buyback economics (0C) | Rs 176.24; 18.0x; Rs 54.48 cash (30.9%); ~35x ex-cash; ~18x Q2 run-rate | Rs 176.235; 18.04x; Rs 54.478 (30.91%); 34.9x; 18.1x | L235, L124, L127, L147-L178 | PASS |
| Step 3 derived quarters | Q1 FY26 58.19 Cr, 8.48%, 3.78; H2 FY26 120.17, 7.65%, 7.10 | same | L100-L110 H1 and FY columns | PASS |
| Tax: current-tax rate H1; deferred share | 20.9% vs 24.0%; 14.7% vs 1.3% | 20.92% vs 23.98%; 14.64% vs 1.34% | L112-L113; D L321-L322 | PASS |
| Release and deck tie-out | ties except deck Q2 FY26 FCTR | confirmed; deck Q2 FY26 TCI 114.3 foots only with +29.0 mn FCTR (86.6 - 1.7 + 0.4 + 29.0 = 114.3) | D L330, D L332, L121, L123 | PASS |

### 2B. Mismatches

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Parent (standalone) net cash, 31-Mar-2026, and H1 fall | 53.14 Cr; fall 27.38 Cr (review L469, L472; flag L873) | 60.15 Cr on A4's own consolidated basis (review L449, which counts non-current investments L147); fall 34.39 Cr. The parent's non-current investments at March (L329, 3,036.69) held the 701.16 lakh treasury investment. Proof: the SA current-investment roll-forward 333.96 (L336) + 701.16 (reclass, = L147) + 30.00 (L406) - 376.89 (L407 379.78 less L390 2.89) + 18.69 (L391) = 706.92 = L336 exactly. Parent net cash: 1,585.66 + 3,771.62 + 333.96 + 701.16 - 377.23 = 6,015.17 lakh (L338, L339, L336, L329, L359); Sep-26 2,575.81 lakh. Perimeter net cash 109.44 to 142.17 Cr (+32.72), not 116.45 to 142.16 | L329, L336, L338, L339, L359, L390, L391, L406, L407, L147 | FAIL. CONTRADICTION, loop A4 (C-1) |
| SA delivery cost Q2 FY27 and YoY (claim 3) | 35.15 Cr, +8.9% (review L526) | 35.14 Cr (1,364.63 + 2,149.64 = 3,514.27), +8.84% vs 3,228.83 | L290, L291 | rounding on rounded Cr. STYLE S-6 |
| OI fall QoQ | 3.46 Cr (review L527, L676) | 3.45 Cr (818.55 - 473.23 = 345.32 lakh) | L101 | rounding. STYLE S-6 |
| Government share of the QoQ revenue increment | "about 72%" (review L270, L736) | 71.5% (346.52 / 484.84 lakh); whole-percent shares give a band of about 57%-86%. The printed shares sum to 101.0% in Q1 FY27 and Q2 FY27 (D L247) | D L247, L100 | rounding, conclusion holds. STYLE S-7 |

### 2C. Logic check on a derived inference (top-client billing)

| Claim | A4 text | Re-derivation | Status |
|---|---|---|---|
| Top-client billing split | Step 1D (review L286): 0.55 x 73.30 = 40.31 Cr exceeds "the whole perimeter's 29.20 Cr", so at least 11.1 Cr "would be billed by the Indian parent". Brief (review L763): "the Indian parent must bill part of it directly." | The arithmetic is right; the conclusion is not. A4 defines the perimeter as consolidated less standalone, net of intercompany eliminations (review L8, L236). Consolidated revenue = parent external + subsidiary external. Standalone revenue = parent external + parent intercompany. So the 29.20 Cr = subsidiary external revenue less parent intercompany revenue. The subsidiaries' external billing is 29.20 Cr plus parent intercompany revenue, which is ND. If the parent bills its US subsidiaries 11.1 Cr or more (inside its 44.09 Cr, L286), the subsidiaries can bill the whole 40.31 Cr. A4 itself reads the parent's revenue as "mostly export or intercompany" (review L474). The extract cannot separate the two readings. | FAIL. FACTUAL, loop A4 (F-1) |

---

## 3. ADVERSARIAL READ

### Claim 1. "Profit before tax without other income nearly doubled"; operating margin +318 bps (review L323, L347, L732-L733)

Strongest bear counter from the extract: the step is one quarter old and its cost profile does not look repeatable. QoQ the consolidated incremental Op EBITDA margin was 48.9% (236.98 lakh Op EBITDA gain on 484.84 lakh revenue gain; L100-L110). Delivery cost rose 4.7% QoQ (5,459.58 to 5,718.20 lakh, L104-L105) against revenue +7.1%, and other expenses fell 1.3% (L108). All of the QoQ gain sits outside the parent (subsidiary Op EBITDA 60.02 to 326.61 lakh), whose margin was 2.4% and 2.5% before. Q2 FCTR swung from -24.96 to +217.88 lakh (L121). Government supplied about 71.5% of the revenue increment (D L247).
Survives: yes. Already in A4 (2C item 3 at review L349; Step 3 at L377; brief L737; Q3 separator 11.04% vs 8.36%). No graft is needed for this claim beyond the currency leg in Claim 3. STYLE S-10: add the 48.9% incremental-margin figure to 2C item 3.

### Claim 2. Cash conversion "favourable"; headline 1.56x, matched pre-WC 1.20x-1.23x and improving (review L438-L439, L483, L738)

Bear counter (a): the H1 headline rests on a 13.06 Cr working-capital release (L219), 85.2% of it from liabilities (L218), which can reverse in H2. Survives, and A4 already carries it (review L479, L483, L793).
Bear counter (b), new test: the 12.15 Cr Other equity debit (review L456) sits in other financial liabilities (current). If the cash-flow statement counted that liability rise inside "Increase in trade payables, other financial liabilities and other liabilities", H1 CFO would be overstated by 12.15 Cr and headline CFO/PAT would be 0.89x ((2,826.32 - 1,215.22) / 1,815.45), not 1.56x.
Test on the standalone statements: operating-liability lines rose 1,492.92 lakh on the balance sheet (L354 -104.85; L362 -79.65; L363 +441.14; L364 +1,295.86; L365 -161.88; L366 +102.30). The cash-flow line L397 shows +275.09. The gap is 1,217.83 lakh, within 2.61 lakh of the 1,215.22 lakh equity gap. The consolidated gap points the same way (balance-sheet rise 2,153.98 lakh at L173, L181-L185 vs 1,112.60 at L218; gap 1,041.38 lakh). [INFERENCE] The item was booked as a non-cash current liability and kept out of CFO. That fits the declared-dividend reading.
Survives: no. Counter (b) fails; the CFO figures stand. STYLE S-11: A4 may add this tie to Step 5A and to the dividend reading. It firms the reading but does not confirm it, and the flag (no note) stands.

### Claim 3. "Currency is a weak explanation for Q1 ... So the revenue step looks real on the extract" (review L377; carried into L376 STEPPING UP, the brief at L737 and the sector line at L753)

A4's test: Q1 FY27 revenue was 13.9% above the H2 FY26 average while Q1 FCTR was negative (-24.96 lakh, L121).
Strongest bear counter, from the same line: FCTR measures the translation of the subsidiaries' net assets at the closing rate (Jun-26 vs Mar-26). It does not measure the average rate used to translate a quarter's revenue. The same line L121 gives FY26 FCTR +866.80 lakh and H1 FY26 +313.14 lakh. So H2 FY26 FCTR was +553.66 lakh (+5.54 Cr). [INFERENCE, same sign convention A4 uses at review L248 and L753] The rupee weakened through H2 FY26. From Sep-25 to Sep-26 the cumulative FCTR is +746.58 lakh (553.66 + 192.92). Both comparisons A4 relies on therefore cross a weaker rupee: Q1 FY27 vs the H2 FY26 average (+13.9%), and Q2 FY27 vs Q2 FY26 (+24.7%). A small closing-rate gain within Q1 does not rule out a higher Q1 average rate than the H2 FY26 average. With 99% of revenue in the US (D L246) and an INR cost base in the parent, this also bears on the YoY margin step (+318 bps), not only the QoQ step. Constant-currency growth and USD revenue are ND in all three documents. The extract cannot size the currency share. It can only show that the Q1 FCTR test does not exclude it.
Survives: yes. MISSING from A4. The review states FY26 FCTR as data (review L179) but never derives H2 FY26 or uses it. It confines currency to Q2 (review L248, L349, L753) and uses Q1 FCTR alone to dismiss it for Q1 (L377). QfM 5 asks for USD revenue, but the review does not tie it to this evidence.
Graft (A4): in Step 3 (L377), replace "Currency is a weak explanation for Q1 ... So the revenue step looks real on the extract" with a statement that the Q1 FCTR test cannot exclude currency, citing H2 FY26 FCTR +5.54 Cr and cumulative Sep-25 to Sep-26 FCTR +7.47 Cr (L121), with constant-currency ND and QfM 5 as the separator. Carry one line into 2C item 3 (L349), the brief summary (L737) and the sector line (L753).

### Mandatory acquisition-economics probe

No document describes the acquisition of an external target. The consolidated investing section has no acquisition line (L223-L231), there is no goodwill, intangibles are nil (L145), and the perimeter is the same three WOS (L73-L76, L431). Two purchase-type transactions exist.
(i) Buyback, Q1 FY27: ~Rs 14.98 Cr consideration incl. costs (L235) / 8,50,000 shares (L124: capital 3,113.06 to 3,028.06 lakh) = Rs 176.24 a share.
- vs FY26 basic EPS Rs 9.77 (L127) = ~18.0x earnings.
- Less group net cash of Rs 54.48 a share (16,959.49 lakh / 3,11,30,600) = Rs 121.76.
- vs FY26 core EPS ex-OI Rs 3.49 = ~34.9x.
- vs the Q1 FY27 core run-rate, the quarter of the buyback (442.98 x 4 x 0.7512 / 3,02,80,600 = Rs 4.40) = ~27.7x.
- vs the Q2 FY27 core run-rate (Rs 6.74) = ~18.1x.
Is the earnings year representative? FY26 core PBT was 14.34 Cr; H1 FY27 alone was 11.24 Cr (L101, L110). FY26 was a trough against the run-rate, so the trailing 35x overstates the price. On the run-rate at the time of purchase it was ~28x.
Bear reading: "not cheap on trailing core; fair only if the Q2 run-rate holds." It survives and A4 already carries it (Step 0C, review L111-L115). STYLE S-12: add the ~28x Q1 run-rate multiple.
(ii) 41.13 Cr injection into an unnamed WOS (L405): ownership does not change, so no price multiple applies. Against perimeter FY26 PAT of 7.06 Cr it is 5.8x, but it bought nothing external. The subsidiaries put 32.64 Cr into treasury investments in H1 (L226 3,293.77 less L406 30.00). A4 already carries this (5B at review L472; QfM 10-11). No graft.

---

## FINDINGS (tagged)

| ID | Type | Finding | Evidence | Loop |
|---|---|---|---|---|
| F-1 | FACTUAL | Top-client inference is invalid. "The Indian parent must bill part of it directly" (review L763; also L286) ignores that the perimeter's 29.20 Cr is net of parent intercompany revenue (review L8, L236). The subsidiaries' external billing is 29.20 Cr + parent intercompany revenue (ND). Restate it as two readings: (a) the parent bills at least 11.1 Cr of the top client directly, or (b) the parent bills the subsidiaries at least 11.1 Cr intercompany and they bill the client. The extract cannot separate them. Optionally add a QfM for intercompany revenue. | L100, L286; review L474 | A4 |
| C-1 | CONTRADICTION | Net-cash basis differs between Step 5A and Step 5B. 5A counts non-current investments (review L449: L147). 5B omits the parent's 701.16 lakh non-current treasury investment, which A4 itself identifies (review L472, A3-01 tie). Parent net cash at 31-Mar-2026 is 60.15 Cr on the 5A basis, not 53.14 Cr. The H1 fall is 34.39 Cr, not 27.38 Cr. Perimeter net cash is 109.44 to 142.17 Cr. Align the basis in review L469, L472 and flag L873. | L329, L336, L338, L339, L359, L390, L391, L406, L407 | A4 |
| M-1 | MISSING | Surviving bear counter to "revenue step looks real": H2 FY26 FCTR +5.54 Cr and Sep-25 to Sep-26 FCTR +7.47 Cr (L121) show the rupee weakened across both comparison bases. The Q1 closing-rate FCTR cannot exclude an average-rate lift. Graft into Step 3 (L377), 2C item 3 (L349), the brief (L737) and the sector line (L753). | L121; D L246 | A4 |

### STYLE NOTES (logged; no re-run)

- S-1: Admin identifiers with no structured row: Lodha telephones L62, L252; company tel/fax L96, L282; exchange PIN codes PR L26, PR L30. A1/A2 capture admin identifiers selectively (page-1 telephone R559 is captured). No analytical effect; A4 already carries the telephone mismatch (A3-20).
- S-2: Results L33 subject-line date has no own DATE row. It restates R673.
- S-3: The A1 results header says blank cells carry no row, yet R121, R122, R394 and R395 exist as blank-value rows. No effect.
- S-4: Coverage rests on a blanket attestation (review L48-L54). List the uncited line groups in 1D as "reviewed, no finding".
- S-5: The deck repeats the results' OCI caption error (D L331, D R284). Name it beside A3-17 in the flags (review L883).
- S-6: Rounding on rounded Cr. Standalone delivery cost is 35.14 Cr and +8.8% (L290-L291), not 35.15 Cr and +8.9% (review L526). The OI QoQ fall is 3.45 Cr, not 3.46 Cr (review L527, L676).
- S-7: "About 72%" Government share of the QoQ increment is 71.5% unrounded. The deck's shares sum to 101.0% in Q1 FY27 and Q2 FY27 (D L247). Carry the band (about 57%-86%) next to the figure in the brief (review L736).
- S-8: "Cash tax" (review L425, L598, L881) is the current-tax charge (20.9%). Direct taxes paid were 17.5% of H1 PBT (L221: 422.00 / L201: 2,415.95). Relabel it "current tax"; the direction holds.
- S-9: "Ordinary approve-then-sign order" (review L142): the filing gives no approval time inside the 19:20-20:30 meeting (L46). Tag it [INFERENCE].
- S-10: Add the 48.9% QoQ incremental Op EBITDA margin to the Claim 1 bear reading (2C item 3).
- S-11: Add the standalone liability tie (1,217.83 vs 1,215.22 lakh) as support for the dividend reading and for CFO integrity (Step 5A).
- S-12: Add the ~27.7x Q1 FY27 run-rate ex-cash buyback multiple to Step 0C.
- S-13: Forward map: give the event-driven and undated rows a check date (for example "check at Q3 FY27 results, 14-Feb-2027").

---

## VERDICT

INCOMPLETE. Loop back to A4.
Gap: (F-1, FACTUAL) correct the top-client billing inference at review L286 and L763. (C-1, CONTRADICTION) align the parent net-cash basis at review L469, L472 and L873: 60.15 Cr at March, fall 34.39 Cr. (M-1, MISSING) graft the H2 FY26 FCTR currency counter into Step 3 L377, 2C item 3 L349, brief L737 and sector L753.
Audits 0 and 1 pass. All other arithmetic recomputes within rounding. The 13 STYLE notes are logged only. The verdict (PROCEED WITH FLAGS) and cash classification are not affected by these findings, but the brief carries F-1 and M-1, so save waits for the A4 fix.

```yaml
stage: A5-adversary
company: "CYBERTECH"
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
arithmetic_mismatches:
  - {metric: "Parent (standalone) net cash 31-Mar-2026 and H1 fall", a4_value: "53.14 Cr; fall 27.38 Cr (review L469, L472, flag L873)", recomputed: "60.15 Cr; fall 34.39 Cr on the review's own 5A basis (includes 701.16 lakh non-current treasury investment inside L329); perimeter net cash 109.44 to 142.17 Cr", source_line: "results L338+L339+L336+L329(701.16 portion)-L359; roll-forward L336 333.96+701.16+30.00(L406)-376.89(L407-L390)+18.69(L391)=706.92"}
surviving_bear_counters:
  - {claim: "Revenue step looks real; currency a weak explanation for Q1 (review L377, L737, L753)", counter: "H2 FY26 FCTR +553.66 lakh (FY26 866.80 less H1 FY26 313.14) and Sep-25 to Sep-26 FCTR +746.58 lakh show the rupee weakened across both comparison bases; Q1 closing-rate FCTR cannot exclude an average-rate lift; constant currency ND", source_line: "results L121; D L246", type: "MISSING"}
  - {claim: "Core PBT ex-OI nearly doubled; Op EBITDA margin +318 bps (review L323, L732)", counter: "QoQ incremental Op EBITDA margin 48.9% (236.98/484.84 lakh); delivery cost +4.7% vs revenue +7.1%; all gain outside the parent; already incorporated at review L349, L377, L737", source_line: "results L100-L110, L121", type: "STYLE"}
  - {claim: "Buyback purchase economics (review L111-L115)", counter: "Rs 176.24 a share; 18.0x FY26 EPS; ex-cash 34.9x FY26 core, 27.7x Q1 FY27 run-rate, 18.1x Q2 run-rate; already incorporated; add Q1 multiple", source_line: "results L124, L127, L235, L101, L110", type: "STYLE"}
findings_by_type:
  factual:
    - "F-1: review L286 and L763 say the parent must bill part of the 55% client directly because 40.31 Cr exceeds the perimeter's 29.20 Cr; the perimeter is net of parent intercompany revenue (review L8, L236), so subsidiary external billing = 29.20 Cr + intercompany (ND); restate as two readings"
  missing:
    - "M-1: H2 FY26 FCTR +5.54 Cr and cumulative +7.47 Cr (L121) currency counter to 'revenue step looks real' absent; graft into Step 3 L377, 2C item 3 L349, brief L737, sector L753"
  contradiction:
    - "C-1: Step 5A net cash includes non-current investments (L147); Step 5B omits the parent's 701.16 lakh non-current treasury investment (L329); parent March net cash 60.15 Cr not 53.14 Cr, H1 fall 34.39 Cr not 27.38 Cr (review L469, L472, L873)"
  style: ["S-1", "S-2", "S-3", "S-4", "S-5", "S-6", "S-7", "S-8", "S-9", "S-10", "S-11", "S-12", "S-13"]
loop_back_to: "A4"
gap: "F-1 FACTUAL: correct top-client billing inference (review L286, L763). C-1 CONTRADICTION: align parent net-cash basis (review L469, L472, L873: 60.15 Cr March, fall 34.39 Cr). M-1 MISSING: graft H2 FY26 FCTR currency counter into Step 3 L377, 2C L349, brief L737, sector L753."
style_notes:
  - "S-1 admin identifiers without rows (L62, L96, L252, L282; PR L26, L30); no effect"
  - "S-2 L33 subject-line date has no own row (restates R673)"
  - "S-3 blank-value rows R121, R122, R394, R395 contradict A1 header convention"
  - "S-4 list uncited ledger line groups as 'reviewed, no finding'"
  - "S-5 deck repeats OCI caption error D L331 / R284; name beside A3-17"
  - "S-6 SA delivery cost 35.14 Cr +8.8% (not 35.15, +8.9%); OI QoQ fall 3.45 Cr (not 3.46)"
  - "S-7 Government share of QoQ increment 71.5% unrounded, band ~57-86%; deck shares sum to 101.0% in Q1 and Q2 FY27"
  - "S-8 'cash tax' is the current-tax charge; taxes paid 17.5% of H1 PBT (L221)"
  - "S-9 'approve-then-sign' order is an inference; approval time not filed"
  - "S-10 add 48.9% QoQ incremental margin to claim-1 bear reading"
  - "S-11 add standalone liability tie 1,217.83 vs 1,215.22 lakh (dividend reading, CFO integrity)"
  - "S-12 add ~27.7x Q1 run-rate ex-cash buyback multiple"
  - "S-13 give event-driven forward-map rows a check date"
analyst_note: "Audits 0 and 1 pass: all five brief parts present; fresh counts match all three ledgers (739, 141, 326 IDs; 8 notes, 20 slides). Coverage of uncited subtotal and zero-standing line groups rests on A4's explicit blanket attestation; each was tested and none holds a finding, so no orphan is declared. Arithmetic recomputes within rounding everywhere except the standalone net-cash basis (C-1). The roll-forward 333.96 + 701.16 + 30.00 - 376.89 + 18.69 = 706.92 lakh proves the parent held the 701.16 treasury investment at March. F-1 is a logic error in the brief, not arithmetic: the perimeter figure is net of intercompany. M-1: A4 tests currency with a closing-rate FCTR while revenue is translated at average rates; H2 FY26 FCTR (+5.54 Cr) was never derived. A tested bear that failed: the 12.15 Cr liability was kept out of CFO (standalone tie within 2.61 lakh), so CFO/PAT 1.56x stands and the dividend reading firms. None of the three loop findings changes the PROCEED WITH FLAGS verdict."
```
