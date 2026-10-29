# SYNGENE Q2 FY27: A5 ADVERSARY / COMPLETENESS AUDIT

Company: Syngene International Ltd (SYNGENE) | Quarter: q2fy27 | Agent: A5 adversary | model: claude-opus-5-5 | audit date: 2026-10-28
Under audit: runs/syngene-q2fy27/work/review_syngene_q2fy27.md (A4, 687 lines)
Inputs read: A1 fulltexts (results, presentation, press release, disclosure), A1 structured files (4), A2 ledgers (results, presentation, press release). No source PDF and nothing under inputs/ was opened.

Anchor key: res / deck / PR / disc = A1 fulltext line; review l.N = line in the A4 review; R### = structured row ID in the named document. All figures are Rs Cr unless stated. Rs Mn x 0.1 = Rs Cr.

---

## AUDIT 0: DELIVERABLE-COMPLETENESS (hard gate)

DELIVERABLE-COMPLETENESS AUDIT: narrative PRESENT (review l.527-545, 18 lines, inside the 10-20 band) | sector PRESENT (l.547-554) | business_model PRESENT (l.556-565) | competition PRESENT (l.567-574) | forward_map PRESENT (l.576-590; 10 dated rows, each row has a bull fork and a bear fork). **Gate: PASS.**

---

## AUDIT 1: COVERAGE

Method: a fresh count over each A1 fulltext (line-by-line for statements and tables; grep for page markers, numbered notes and auditor paragraphs), then a grep of row IDs in each structured file, then a diff against the A2 ledgers and the A4 review.

| Document | Category | A2 count | A5 fresh count | Orphan rows | Status |
|---|---|---|---|---|---|
| Results | structured row IDs | 828 | 828 (grep `^R\d{3} \|`) | none (ledger orphan_ids []) | PASS |
| Results | numbered notes | 9 | 9 (bare numerals res l.455-462 + note 9 at l.463; texts l.471, 474, 479, 486, 490, 495, 497, 504) | none | PASS |
| Results | line items (pages 2-7) | 227 | 227 (cons P&L 28, cons BS 43, cons CF 43, stand P&L 29, stand BS 42, stand CF 42) | none | PASS |
| Results | zero-standing lines | 15 | 15 (res l.89, 174, 209, 210, 216, 231, 280, 283, 290, 367, 401, 405, 407, 423, 434) | none | PASS |
| Results | agenda items | 1 | 1 (res l.40-44) | none | PASS |
| Results | auditor paragraphs | 12 | 12 (grep: cons 1-6 + unnumbered l.547; stand 1-5) | none | PASS |
| Results | entities | 5 | 5 (res l.549-554) | none | PASS |
| Results | signatures | 4 | 4 (res l.65-67, l.513-517, l.581-584, l.636-639) | none | PASS |
| Presentation | structured row IDs | 350 | 350 (grep) | none | PASS |
| Presentation | slides | 32 | 32 (grep `[page N]`) | none | PASS |
| Presentation | financial line items (p27, p28) | 45 | 45 (p27 17 + 5 BS; p28 18 + 5 BS) | none | PASS |
| Presentation | footnote markers | 10 | 10 (deck l.228, 429, 582, 650-652, 714, 718, 720, 722) | none | PASS |
| Presentation | forward statements | 7 | 7 (deck l.121-123, l.139-140, p13 x3, p21 roadmap, p6 dual-continent) | none | PASS |
| Presentation | zero-standing | 1 | 1 (deck l.510) | none | PASS |
| Presentation | MISSING_FROM_STRUCTURED | M01-M09 | same 9 (boilerplate, certifications, contact) | carried in ledger as M-rows | PASS (immaterial; no loop) |
| Press release | structured row IDs | 879 | 879 (grep) | none | PASS |
| Press release | numbered notes | 13 | 13 (grep `^Note \d+\.`) | none | PASS |
| Press release | unnumbered footnotes | 15 | 15 (PR L95, L115; p7 x5; p8 x5; p9 x3) | none | PASS |
| Press release | line items | 139 | 139 (p2 13; p6 BS 42; p7 28; p8 28; p9 28) | none | PASS |
| Press release | zero-standing cells | 12 | 12 (PR L91, L279, L326 x2, L366, L408 x7) | none | PASS |
| Press release | forward statements | 18 | 18 (PR L121-122, 126, 136, 141, 150, 153-154, 159-160 x2, 161, 166, 191, 192, 202, 206, 210, 212, 432, 441) | none | PASS |
| Press release | MISSING_FROM_STRUCTURED | NEW-1, NEW-2 | same 2 (postal codes PR L32) | carried in ledger | PASS (immaterial) |
| Disclosure (no ledger by design) | structured row IDs | n/a | 71 (grep; NUMBER 12, ENTITY 21, FORWARD 5, DATE 21, QUALIFIER 12) | n/a | PASS on extraction |
| Disclosure | people changes | n/a | 4 (disc l.43-58; R019-R022) | n/a | PASS |
| Disclosure | material rows vs review | n/a | cited: R034, R036-R038, R040-R042, R053, R070-R071 | **R043 / R054 (resignation letter date) not treated** | FAIL, see M1 |

Row-to-review test. A4 marks every ledger row reviewed by blanket ("All rows read", "Unreviewed ledger rows: none", review l.17-26). I tested the blanket on every A2-flagged row and every row that carries a thesis fact. Two rows fail the test:
- PR R749 (PR L175) and deck R022 (deck l.130): the commissioned Clinical Translational Sciences laboratory. A4 never mentions it and states the opposite (review l.195). See F3.
- Disclosure R043 / R054 (disc l.64, l.144): the resignation letter is dated 23-Oct-2026. A4 never mentions the date. See M1.

Ledger-level result: orphan_rows [] and missing_from_ledger []. My fresh pass found no unit that the ledgers lack. One non-enumeration gap is logged as style: deck l.369 ("demanding operating environment") has no structured row. A4 cites the fulltext correctly (S8).

---

## AUDIT 2: ARITHMETIC

Every derived metric in the A4 tables was recomputed from the raw extract lines. Tolerance: display rounding (0.1 Cr, 0.1 pp, 1 bp).

| # | Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|---|
| 1 | Step 1 raw lines, all 18 rows x 6 columns | as tabled | all 108 cells match x0.1 | res l.76-107 (column order Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26, FY26; 8,327 + 7,360 = 15,687 confirms) | PASS |
| 2 | Op EBITDA Q2 FY27 / Q1 / Q2 FY26 | 147.4 / 90.8 / 199.5 | 53.7+111.7+10.0-28.0 = 147.4; -5.7+112.2+9.6-25.3 = 90.8; 85.2+116.5+13.2-15.4 = 199.5 | res l.77, 83, 84, 88 | PASS |
| 3 | Op EBITDA H1 FY27 / H1 FY26 / FY26 | 238.2 / 405.9 / 918.5 | 48.0+223.9+19.6-53.3; 186.5+227.7+24.8-33.1; 487.5+452.9+48.8-70.7 | same | PASS |
| 4 | Op margin Q2 / Q1 / Q2 FY26 / H1 / H1 FY26 / FY26 | 17.70 / 12.34 / 21.91 / 15.18 / 22.74 / 24.57% | 17.701 / 12.337 / 21.908 / 15.185 / 22.738 / 24.567% | res l.76 | PASS |
| 5 | YoY margin change | -421 bps | -420.7 bps | computed | PASS |
| 6 | Ex-FX margin Q2 / Q2 FY26 / H1 / FY26 | 25.07 / 23.20 / 22.29 / 26.20% | 208.8/832.7 = 25.075; 211.3/910.6 = 23.204; 349.7/1,568.7 = 22.292; 979.4/3,738.7 = 26.196 | res l.86 | PASS |
| 7 | Normalised Q2 FY26 op EBITDA / ex-FX | 227.2 (24.95%) / 239.0 (26.25%) | 199.5+27.7; 211.3+27.7 | PR L434 | PASS |
| 8 | Normalised YoY margin change | -725 bps | 17.70 - 24.95 = -7.25 pp | computed | PASS |
| 9 | Ex-FX vs normalised base | -118 bps | -117 bps unrounded | computed | PASS (rounding) |
| 10 | Core PBT Q2 / Q2 FY26 / YoY | 25.7 / 69.8 / -63.2% | 53.7-28.0; 85.2-15.4; -63.18% | res l.77, l.88 | PASS |
| 11 | H1 core PBT | (5.3) | 48.0 - 53.3 | res l.77, l.88 | PASS |
| 12 | OI share of Q2 PBT pre-exc / after exc | 52.1% / 59.6% | 28.0/53.7 = 52.14%; 28.0/47.0 = 59.57% | res l.77, 88, 90 | PASS |
| 13 | H1 OI vs FY26 OI | 75% | 53.3/70.7 = 75.4% | res l.77 | PASS |
| 14 | ETR Q2 / Q2 FY26 / H1 / H1 FY26 / FY26 | 31.5 / 21.2 / 16.5 / 17.5 / 22.9% | 14.8/47.0; 18.1/85.2; 4.6/27.8; 32.7/186.5; 94.2/410.9 | res l.90, l.94 | PASS |
| 15 | PAT / EPS YoY | -52.0% / -52.1% | 32.2/67.1-1; 0.80/1.67-1 | res l.95, l.106 | PASS |
| 16 | Standalone op EBITDA Q2 / Q1 / Q2 FY26 / H1 / H1 FY26 / FY26 | 147.4 / 78.4 / 177.5 / 225.8 / 345.6 / 814.6 | 75.7+95.1+4.1-27.5; 3.5+95.6+4.1-24.8; 84.2+100.1+7.4-14.2; 79.2+190.7+8.2-52.3; 168.4+194.7+13.3-30.8; 468.4+387.1+26.0-66.9 | res l.268, 274, 275, 279 | PASS |
| 17 | Standalone op margin Q2 / H1 | 18.95% / 15.67% | 147.4/777.9; 225.8/1,440.9 | res l.267 | PASS |
| 18 | Subsidiary revenue / op EBITDA / PAT, Q2 | 54.8 / 0.0 / (16.5) | 832.7-777.9; 147.4-147.4; 32.2-48.7 | res l.76, l.95, l.267, l.286 | PASS |
| 19 | PAT gap % Q2 / H1 / Q2 FY26 / H1 FY26 / FY26 | -33.9 / -50.2 / +1.4 / +9.7 / +3.9% | -16.5/48.7; -23.4/46.6; 0.9/66.2; 13.6/140.2; 11.8/304.9 | res l.95, l.286 | PASS |
| 20 | Gap swing Q2 / H1 | 35.3 pp / 59.9 pp | 35.2 / 59.9 pp unrounded | computed | PASS (rounding) |
| 21 | Subsidiary deferred tax Q2 / H1 | (5.5) / (7.9) | 5.4-10.9; -4.9-3.0 | res l.93, l.284 | PASS |
| 22 | PAT bridge: revenue / margin components | (17.1) / (35.0) | -77.9 x 21.908% = -17.07; 832.7 x -4.207% = -35.03 | computed | PASS |
| 23 | PAT bridge: FX increase / ex-FX effect | (49.6) / +14.6 | 61.4-11.8; -35.0+49.6 | res l.86 | PASS |
| 24 | PAT bridge: tax split | +8.1 / (4.8) | 38.2 x 21.24% = 8.11; 47.0 x 10.25 pp = 4.82 | res l.90, l.94 | PASS |
| 25 | PAT bridge foots | -34.9 | -17.1-35.0+4.8+3.2+12.6+3.3-6.7 = -34.9 = 32.2-67.1 | res l.95 | PASS |
| 26 | Recurring share of fall | 126% | 44.1/34.9 = 126.4% | computed | PASS |
| 27 | OI-reverts PAT | ~23.6 | 34.4 x (1-0.3149) = 23.57 | computed | PASS |
| 28 | **Q1 tax credit vs Q1 pre-tax loss (review l.227)** | **"credit of 10.2 exceeded the Q1 pre-tax loss"** | **Pre-exceptional: normalised credit 6.7 vs loss 5.7, PAT pre-exc +1.0. After exceptional: credit 10.2 vs loss 19.2, credit is smaller.** | **PR L405-407; deck l.670-672; res l.90, l.94** | **FAIL (F1)** |
| 29 | **Note 4 Rs Cr impact (review l.65)** | **0.07** | **0.73 (729,727 x Rs 10 = Rs 7.30 Mn); paid-up +0.8 on rounded Mn** | **res l.471-473; res l.103** | **FAIL (F2)** |
| 30 | Pre-op capitalised H1 / if expensed PBT | +66.1 / (38.3) | 124.6-58.5; 27.8-66.1 | res l.477; res l.90 | PASS |
| 31 | Pre-op growth in H1 | +113% | 124.6/58.5-1 = 113.0% | res l.477 | PASS |
| 32 | CFO cons / stand, change | (143.2) / (155.4); (98.1) / (85.4) | res values x0.1 | res l.226, l.418 | PASS |
| 33 | CFO/PAT; CFO/op EBITDA | (6.17)x; (60.1%) vs (11.1%) | -143.2/23.2; -143.2/238.2; -45.1/405.9 | res l.226 | PASS |
| 34 | Op profit before WC change | -52.3% | 216.2/453.3-1 | res l.218 | PASS |
| 35 | WC change sum | (306.9) vs (451.9) | -26.5+116.9-15.1-382.2; -33.8-35.1-117.3-265.7 | res l.220-223 | PASS |
| 36 | Capex; FCF | 220.2 (+31.9%); (363.4) | 209.9+10.3; 155.2+11.7; -143.2-220.2 | res l.228, l.230 | PASS |
| 37 | Receivable days | 49.7 to 44.8 (-4.9) | 49.67 to 44.85 (-4.8 unrounded) | res l.155, l.76 | PASS (rounding) |
| 38 | Inventory days | 56.1 to 82.3 | 141.3/918.6 x 365 = 56.14; 167.8/744.0 x 365 = 82.32 | res l.152, l.80-81 | PASS |
| 39 | Payable days | 63.7 to 82.0 | 280.9/1,610.3 x 365 = 63.67; 303.3/1,350.4 x 365 = 81.98 | res l.182-183, l.80-81, l.85 | PASS |
| 40 | CCC | 42.1 to 45.1 | 42.1 to 45.2 unrounded | computed | PASS (rounding) |
| 41 | Liquid funds | 1,178.0 to 730.5 | 286.3+461.0+228.6+202.1; 200.5+409.3+119.9+0.8 | res l.144, 154, 156, 157 | PASS |
| 42 | Other current liabilities fall | 313.4 (40%); parent 312.7 | 780.8-467.4 = 313.4 (40.1%); 773.2-460.5 | res l.188, l.380 | PASS |
| 43 | Non-US subsidiary CWIP | 97.2 | 1,140.6-555.8-487.6 | res l.138, l.331, l.476 | PASS |
| 44 | Parent net investment in subsidiaries | 833.9 flat | 1,034.4-200.5 = 833.9; 1,120.2-286.3 = 833.9 | res l.144, l.337 | PASS |
| 45 | Net derivative liability; current net | 96.5; 101.7 | (19.6+104.3)-(24.8+2.6); 104.3-2.6 | res l.145, 158, 172, 184 | PASS |
| 46 | CWIP share of total assets | 17.1% | 1,140.6/6,658.5 = 17.13% | res l.138, l.162 | PASS |
| 47 | QoQ table: revenue, margin, core PBT, QoQ % for 6 quarters | as tabled | all match (e.g. Q4 FY26 2,020-222 = 179.8; Q1 FY27 -57-253 = -31.0) | PR L378, L380, L388, L405 | PASS |
| 48 | Q1-to-Q2 seasonal steps cited | FY24 +12.6%, FY25 +12.8% | 12.62%, 12.83%; FY26 step +4.13% not cited | PR L378 | PASS (omission logged S1) |
| 49 | Q2 FY27 rank in 14 quarters | 4th-lowest revenue; 2nd-lowest margin | confirmed | PR L378, L380 | PASS |
| 50 | FX loss rising in 5 of last 6 quarters | 5 of 6 | 48>46, 118>48, 233>118, 209<233, 501>209, 614>501 | PR L398 | PASS |
| 51 | Implied Q3 FY27 | 781 / 882 / 839 | 832.7 x 0.9378 / 1.0591 / 1.0071 | PR L378 | PASS |
| 52 | Guidance floor; H2 needs | 3,364.8; 1,796.1 (base 1,767.3) | 0.9 x 3,738.7; 3,364.8-1,568.7; 3,336-1,568.7 | res l.76 | PASS |
| 53 | T5 H2 thresholds; best H2 | 32.9% / 33.6%; 32.0% (FY25) | (880.6-238.2)/1,953.6; (841.2-238.2)/1,796.1; 6,272/19,617 | PR L378-379 | PASS ("flat H2" undefined, S5) |
| 54 | R2 / T1 research shares | 73.3% / 69.7% | 610/832.7; 580/832.7 | computed | PASS |
| 55 | ROCE H1 annualised | ~2.5% | 135.2/5,366.2 = 2.52% | res l.83, 88, 167, 171, 179, 180 | PASS |
| 56 | TTM revenue | 3,522.3 | 917.1+1,036.5+736.0+832.7 = 3,738.7-1,785.1+1,568.7 | PR L378; res l.76 | PASS |
| 57 | **TTM PAT after exceptional (review l.381)** | **184.2** | **186.1 from audited results (316.7-153.8+23.2). Fact-sheet H2 FY26 = 15.0+146.0 = 161.0 against results 162.9. Fact-sheet FY26 quarters sum to 314.8 against audited 316.7.** | **PR L409 vs res l.95** | **FAIL, filed-source conflict (C2)** |
| 58 | TTM EPS; PE | 4.63; ~77x / ~83x | 7.87-3.82+0.58; 356/4.63; 386/4.63 | res l.106 | PASS |
| 59 | Implied price; promoter | ~Rs 356; ~52.6% | 14,382/40.37; 100-47-0.4 | deck l.774-787; res l.103 | PASS |
| 60 | A3P-08 resolution | gap 9 / 10 / 13 = finance cost | 175-112-54; 116-112+6; 215-117-85 | deck l.665-670; res l.83 | PASS |
| 61 | A3P-11 resolution; FY26 deck PAT bridge | 766 = 463 + 303; 380-38-25 = 317 | confirmed | res l.89, 481, 486; deck l.714, 740-742 | PASS |
| 62 | Q2 annualised PAT vs Notion base | -38% | 128.8/207-1 = -37.8% | res l.95 | PASS |

Result: 62 metric groups recomputed. 59 pass. 3 fail (rows 28, 29, 57).

---

## AUDIT 3: ADVERSARIAL READ

The three most positive claims in the A4 review, each with the strongest bear counter from the same extract.

### P1. "Revenue beat the Notion base path"; Q2 revenue path GREEN; H1 "Between Base and Bull"
Where: review l.159, l.297-298, l.324 (watchlist #5 GREEN), l.531, l.684.
Bear counter: the beat is in rupees and cash does not confirm it.
- H1 revenue was Rs 1,568.7 Cr (res l.76). In the same half, other current liabilities fell Rs 313.4 Cr, 40% (res l.188). Rs 312.7 Cr of that fall was at the parent (res l.380). H1 CFO was -Rs 143.2 Cr (res l.226).
- For a CRDMO these liabilities are usually customer advances and contract liabilities [INFERENCE; composition NOT FOUND]. If so, part of H1 revenue used up cash received before 1-Apr-2026. Then the beat says nothing about new order intake.
- The rupee that produced the Rs 61.4 Cr hedge loss (res l.86; "forex hedge losses", PR L135) also lifts revenue translated at spot [INFERENCE].
- Counter-check: H1 FY26 also had a liabilities unwind of Rs 265.7 Cr (res l.223), with revenue of Rs 1,785.1 Cr. So this is a qualifier, not a reversal.
Survives: YES, as a qualifier. A4 has the cash readings (review l.258) but does not attach them to the revenue verdict.
Graft (A4): on watchlist #5 and the 6A revenue rows, add: "GREEN on reported rupee revenue. Cash has not confirmed it: other current liabilities fell Rs 313.4 Cr in H1. Q6 decides whether the beat used up prior advances."

### P2. "Without the hedge loss, the margin was 25.1%"; "Underlying ex-FX margin is flat to slightly down"
Where: review l.120, l.127, l.173, l.534.
Bear counter: the ex-FX margin is a counterfactual and it is flattered twice.
- Capitalisation: H1 Bayview pre-operative cost of Rs 66.1 Cr went to CWIP, not the P&L (res l.476-477). Expensed, it takes the H1 ex-FX operating EBITDA from 349.7 to 283.6. The H1 ex-FX margin moves from 22.29% to 18.08% (computed). This is an upper bound: the pre-op composition and the Q2 share are NOT FOUND.
- Acceleration: the pre-op balance at 31-Mar-2026 was Rs 58.5 Cr (res l.477). So the H1 FY27 addition alone exceeds the whole FY26 closing balance. The +187 bps YoY ex-FX comparison (review l.173) therefore includes faster capitalisation.
- Hedge: the loss is recurring. It grew in 5 of the last 6 quarters (PR L398). A net derivative liability of Rs 96.5 Cr remains at 30-Sep-2026 (res l.145, l.158, l.172, l.184). Dropping the hedge cost while keeping spot-rate revenue gives the margin of an unhedged company, not this company [INFERENCE on mechanism].
Survives: YES. A4 has the PBT effect of the pre-op (review l.66) but not the margin effect. It also labels the ex-FX margin "underlying".
Graft (A4): in Step 2 diagnostic 2 and Brief §1, replace "underlying" with "ex-hedge". Add: "With the H1 Bayview pre-op expensed, the H1 ex-FX margin would be about 18.1%, not 22.3% (upper bound; composition not disclosed)."

### P3. "CDMO share > 22%: ON TRACK (MGMT claim only)"
Where: review l.373 (6D). Confirming evidence cited at l.371 and l.373.
Bear counter:
- The claim rests on unquantified management words: "positive traction in our CDMO business" (PR L130). The Chair says "early signs" (PR L124).
- Filed material intensity barely moved: 23.9% against 23.6% in Q1 (PR L391). On results lines it is (203.0-4.4)/832.7 = 23.85% against 23.56% (res l.80-81). A4 itself lists this as killing evidence.
- The Bayview deal yields process development in India "this fiscal" and drug-substance manufacturing only "in the next financial year" (PR L159-161). The Unit 3 deal is for "clinical supplies" (PR L164-165).
- A4's own watchlist rates the same variable UNKNOWN (review l.321).
Survives: YES. This is an internal contradiction. See C1.
Graft (A4): set 6D row 3 to UNKNOWN (MGMT claim unquantified; filed mix evidence neutral). This matches 6B row 2.

### MANDATORY ACQUISITION-ECONOMICS PROBE
The documents describe three purchases: the Bayview site, the Unit 3 Stelis facility, and a new Rs 2.5 Cr equity stake.

**Bayview, Baltimore (PR L441-446; res l.474-478; deck l.199-201, l.256-257).**
- Price: CWIP Rs 298.1 Cr (USD 34.89m) plus land Rs 31.1 Cr (USD 3.64m), including Rs 10.1 Cr pre-transaction cost = **Rs 329.2 Cr (USD 38.53m)** at 31-Mar-2025 (PR L445-446).
- Earnings multiple: **~Rs 329.2 Cr / target PAT nil = no earnings multiple (n/m).** The deal was booked as an "asset acquisition" under Ind AS 103 (res l.475; PR L444). So no business, no earnings and no customer book came with it. Target ROCE, debt, cash and customer tenure: NOT FOUND.
- Cost to date: CWIP Rs 487.6 Cr at 30-Sep-2026 (res l.476). That is +Rs 189.5 Cr, **+63.6%** on the acquisition-date CWIP in 18 months. Of the total, Rs 124.6 Cr is pre-operative cost (res l.477). All-in with land: **at least Rs 518.7 Cr, +57.6%** (land at the Mar-2025 value; Sep-2026 land value NOT FOUND). Some of the rupee growth may be translation of a USD asset [INFERENCE; split NOT FOUND].
- Revenue: none yet. First manufacturing agreement signed in Q2 FY27, customer unnamed (PR L156). Drug-substance manufacturing starts FY28 (PR L160).
- Bear reading: the low headline price bought capacity, not earnings. The real price is the headline plus the carry until revenue, and the carry runs at about Rs 132 Cr a year on the H1 pace (computed). Why was it cheap? The extract does not say. A site without contracted customers is the reading the filings support [INFERENCE].
- **Survives: YES.** A4 tracks the CWIP and pre-op but never compares cost to date with the purchase price. Its PR Note 9 row calls the note "stale" (review l.75). Graft: see M4.

**Unit 3, Stelis Biopharma (PR L419, L438-440; deck l.191-193, l.254).** Purchase consideration: NOT FOUND in the extract. Target PAT: NOT FOUND. Rs 343.8 Cr was capitalised for one licensed drug-substance line (PR L439). The multiple cannot be computed. The bear reading (capitalised without lifting revenue) is already in A4 (review l.195). No graft.

**Rs 2.5 Cr equity investment (res l.231, l.423).** Investee unnamed. Target PAT: NOT FOUND, so no multiple. The size is 0.05% of equity of Rs 4,858.8 Cr (res l.167). The governance reading is already in A4 (T6, Q20, A3-03). No graft.

---

## FINDINGS (tagged)

### FACTUAL (loop A4)
- **F1. Q1 FY27 tax pairing is wrong (review l.227).** A4 writes "The Q1 tax credit of 10.2 exceeded the Q1 pre-tax loss". The 10.2 is the total tax credit (res l.94), which includes the shield on the Rs 13.5 Cr exceptional. Against the loss after exceptional, Rs 19.2 Cr (res l.90), it does not exceed. The correct pair is the normalised pre-exceptional credit of Rs 6.7 Cr against the pre-exceptional loss of Rs 5.7 Cr (PR L405-406; deck l.670-671). That pair gives PAT before exceptional of +Rs 1.0 Cr (PR L407; deck l.672). The sentence also clashes with A4's own Step 1 cell "credit 10.2 on loss 19.2" (review l.124). Fix: "The Q1 normalised tax credit of 6.7 exceeded the Q1 pre-exceptional loss of 5.7 (PR L405-406), turning it into PAT before exceptional of +1.0."
- **F2. Note 4 impact understated tenfold (review l.65).** The "Rs Cr impact" cell reads 0.07. 729,727 shares x Rs 10 = Rs 7.30 Mn = Rs 0.73 Cr (res l.471-473). The same cell says paid-up rose Rs 0.8 Cr (res l.103). Fix: 0.73.
- **F3. "No new capacity has commissioned in H1" is contradicted (review l.195).** The press release says "Syngene commissioned a new Clinical Translational Sciences (CTS) Laboratory in Bengaluru" (PR L175-180; R749). The deck says the same (deck l.130-133; R022). The review never mentions this facility. Fix: "No new manufacturing capacity commissioned in H1. A CTS laboratory (clinical biomarker, biobanking, bioanalytical) was commissioned in Q2 (PR L175; deck l.130). Capex and capacity are not stated." Add one question on its capex and revenue line.

### MISSING (loop A4)
- **M1. Resignation-letter date absent (disclosure R043, R054).** Mr Tandon's letter is dated 23-Oct-2026 (disc l.64, l.144). The Reg 30 disclosure is dated 27-Oct-2026 (disc l.19; R039) and cites "Regulation 30(6)" (disc l.60; R069). The letter opens "As discussed" (disc l.155). The receipt date is NOT FOUND, so a timing lapse cannot be asserted. The four-day gap is still a governance data point in a review that rates management change RED (review l.332). Fix: add the two dates to the preamble's Reg 30 resolution (review l.37). Extend Q31 to ask: "On what date did the company receive the 23-Oct-2026 resignation letter?" Mark any timeliness reading [INFERENCE].
- **M2. Ex-FX "underlying" margin bear counter not grafted (P2).** See Audit 3, P2. Fix in Step 2 diagnostic 2 (review l.173) and Brief §1 (review l.534).
- **M3. Revenue-beat qualifier not grafted (P1).** See Audit 3, P1. Fix at watchlist #5 (review l.324) and the 6A revenue rows (review l.297-298).
- **M4. Bayview acquisition economics not stated (probe).** See Audit 3. Fix: add one line to the PR Note 9 row (review l.75) or the CWIP answer (review l.259): "Bayview cost to date: CWIP Rs 487.6 Cr against Rs 298.1 Cr at acquisition, +63.6% in 18 months (res l.476; PR L445). All-in with land at least Rs 518.7 Cr against Rs 329.2 Cr paid. Asset acquisition, so no earnings multiple exists. No revenue until FY28 (PR L160)."

### CONTRADICTION (loop A4)
- **C1. CDMO share rated two ways.** Watchlist 6B row 2 says UNKNOWN (review l.321). Growth trigger 6D row 3 says ON TRACK for the same variable on the same evidence (review l.373). Under the conservative reading of filed evidence (OR-26), an unquantified management claim with neutral filed mix data is UNKNOWN. Fix: set 6D row 3 to UNKNOWN.
- **C2. TTM PAT rests on a fact-sheet series that does not foot (review l.381).** A4's TTM PAT after exceptional of Rs 184.2 Cr sums the fact sheet (PR L409). From the audited results it is Rs 186.1 Cr (316.7-153.8+23.2; res l.95). The fact sheet's FY26 quarters sum to Rs 314.8 Cr against audited Rs 316.7 Cr. The Rs 1.9 Cr gap sits in H2 FY26 (fact sheet 161.0, results 162.9). It traces to net-of-tax exceptional: fact sheet Rs 65.1 Cr (PR L408) against Rs 63 Cr in the deck (deck l.714) and about Rs 63.2 Cr implied by the results. Fix: show 186.1 (results) as primary and 184.2 (fact sheet) beside it. Name the filed inconsistency and add it to the IR-email list.

---

## VERDICT

**INCOMPLETE.** Loop back to **A4**.
Gap (FACTUAL / MISSING / CONTRADICTION only):
- F1: Step 4 Q1 tax pairing; use 6.7 against 5.7.
- F2: Note 4 impact 0.07 should be 0.73.
- F3: CTS laboratory commissioned; "no new capacity" is wrong.
- M1: add the 23-Oct-2026 letter date against the 27-Oct-2026 filing.
- M2: graft the pre-op and hedge counter onto the ex-FX "underlying" margin.
- M3: graft the cash qualifier onto revenue GREEN.
- M4: state Bayview cost to date against the purchase price, and state that no earnings multiple exists.
- C1: align 6D CDMO share to UNKNOWN.
- C2: show the results-based TTM PAT of 186.1 and flag the fact-sheet conflict.

No A2 or A3 loop. Coverage is clean at the ledger level. Every fix is a one-line edit or graft inside the A4 review. None needs a new extraction.

---

## STYLE NOTES (logged; no re-run)
- S1. The seasonality sentence (review l.193) cites the FY24 (+12.6%) and FY25 (+12.8%) Q1-to-Q2 steps. It omits FY26 (+4.1%, PR L378), which A4's own Step 3 table shows. The conclusion "mostly seasonal" still holds on the three-year average of 9.8%. Add FY26 for symmetry (Rule J).
- S2. In the Forward Map, the ~6-Nov-2026 row comes before the 5-Nov-2026 row (review l.581-582). Put them in date order.
- S3. Brief §1 "A forex hedge loss of Rs 61.4 Cr caused most of that fall [FILED]" (review l.533). The attribution is computed, so tag it [FILED, computed]. The FX increase of 49.6 exceeds the whole margin effect of 35.0 (review l.205).
- S4. Step 7 cites "disc l.43-58" for "both discovery heads leaving" (review l.393). Disc l.43-49 records only an SMP to Non-SMP redesignation. The departure is PR L153-154. Cite PR.
- S5. T5 "flat H2" (review l.358) is undefined. It means H2 FY27 revenue equal to H2 FY26 (Rs 1,953.6 Cr).
- S6. The press-release headline "Operating EBITDA margin improves by 6 percentage points" (PR L42, L74, L131) is 5.4 pp on filed figures (12.34% to 17.70%). The 6 comes from rounded 12% and 18%. An optional line.
- S7. A1 disclosure structured anchors drift 1-8 lines on boilerplate rows (R003, R005, R006, R014-R016, R047, R048, R050-R052). The material rows R034-R042 and R053 anchor correctly. For A1 maintenance only.
- S8. The deck structured file has no row for the slide 16 bullet "demanding operating environment" (deck l.369). A4 cites it from the fulltext correctly. It is not an A2 enumeration category, so no ledger gap.

---

```yaml
stage: A5-adversary
company: "SYNGENE"
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
  - {metric: "Q1 FY27 tax credit vs pre-tax loss (Step 4, review l.227)", a4_value: "credit 10.2 exceeded the Q1 pre-tax loss", recomputed: "pre-exceptional credit 6.7 vs loss 5.7 (PAT pre-exc +1.0); after exceptional credit 10.2 vs loss 19.2 (credit smaller)", source_line: "PR L405-407; deck l.670-672; res l.90, l.94"}
  - {metric: "Note 4 share allotment Rs Cr impact (Step 0D, review l.65)", a4_value: "0.07", recomputed: "0.73 (729,727 x Rs 10 = Rs 7.30 Mn)", source_line: "res l.471-473; res l.103"}
  - {metric: "TTM PAT after exceptional (Step 6.5A, review l.381)", a4_value: "184.2 (fact sheet)", recomputed: "186.1 from audited results (316.7 - 153.8 + 23.2); fact-sheet H2 FY26 161.0 vs results 162.9", source_line: "PR L409 vs res l.95"}
surviving_bear_counters:
  - {claim: "Revenue beat the ~Rs 790 Cr base path; Q2 revenue GREEN (review l.159, l.297-298, l.324, l.531)", counter: "Beat is in spot rupees and cash does not confirm it: other current liabilities fell Rs 313.4 Cr (40%) in H1, Rs 312.7 Cr at the parent, and H1 CFO was -143.2; if these are advances [INFERENCE], part of H1 revenue used up prior-period cash; the same weak rupee behind the hedge loss lifts spot revenue [INFERENCE]", source_line: "res l.76, l.188, l.223, l.226, l.380, l.86; PR L135", type: MISSING}
  - {claim: "Ex-FX margin 25.07% is the underlying margin; hedge loss explains the contraction (review l.120, l.127, l.173, l.534)", counter: "Expensing H1 Bayview pre-op of 66.1 cuts the H1 ex-FX margin from 22.29% to 18.08% (upper bound); H1 pre-op addition exceeds the whole Mar-26 balance of 58.5; the hedge loss recurs (5 of 6 quarters) and a net derivative liability of 96.5 remains", source_line: "res l.476-477, l.86, l.145, l.158, l.172, l.184; PR L398", type: MISSING}
  - {claim: "CDMO share > 22% ON TRACK (review l.373)", counter: "Unquantified MGMT claim (PR L130); material intensity flat at 23.9% vs 23.6% (PR L391); Bayview yields only process development in FY27 and DS manufacturing in FY28 (PR L159-161); Unit 3 deal is clinical supplies (PR L164-165); the same variable is UNKNOWN in 6B (review l.321)", source_line: "PR L124, L130, L159-165, L391; res l.80-81", type: CONTRADICTION}
  - {claim: "Bayview acquisition: 50,000L biologics capacity bought cheaply as an asset acquisition (acquisition-economics probe)", counter: "~Rs 329.2 Cr paid / target PAT nil = no earnings multiple (asset acquisition, Ind AS 103); CWIP up from 298.1 to 487.6 (+63.6%) in 18 months, pre-op 124.6, all-in at least 518.7, no revenue until FY28", source_line: "PR L441-446, L156, L160; res l.474-478", type: MISSING}
findings_by_type:
  factual:
    - "F1: Step 4 (review l.227) says the Q1 tax credit of 10.2 exceeded the pre-tax loss; correct pair is 6.7 vs 5.7 pre-exceptional (PR L405-406; deck l.670-671); 10.2 is smaller than the 19.2 loss after exceptional (res l.90, l.94)"
    - "F2: Note 4 Rs Cr impact shown as 0.07 (review l.65); correct is 0.73 (729,727 x Rs 10; res l.471-473)"
    - "F3: 'no new capacity has commissioned in H1' (review l.195) contradicts the CTS laboratory commissioned in Bengaluru (PR L175-180, R749; deck l.130-133, R022), which the review never mentions"
  missing:
    - "M1: Tandon resignation letter dated 23-Oct-2026 (disc l.64, l.144; R043, R054) vs Reg 30 filing 27-Oct-2026 citing Reg 30(6) (disc l.19, l.60); receipt date NOT FOUND; add the fact and a question, no breach asserted"
    - "M2: surviving bear counter P2 not grafted; ex-FX 'underlying' margin flattered by capitalised pre-op (H1 22.29% to 18.08% if expensed) and recurring hedge cost"
    - "M3: surviving bear counter P1 not grafted; revenue GREEN lacks the qualifier that H1 cash and a Rs 313.4 Cr liabilities drawdown do not confirm it"
    - "M4: Bayview acquisition economics not stated; no earnings multiple (asset acquisition); cost to date +63.6% on acquisition CWIP; review l.75 calls Note 9 stale"
  contradiction:
    - "C1: CDMO share > 22% is UNKNOWN in 6B row 2 (review l.321) but ON TRACK in 6D row 3 (review l.373) on the same evidence"
    - "C2: TTM PAT 184.2 from fact sheet (PR L409) vs 186.1 from audited results (res l.95); fact-sheet FY26 quarters sum to 314.8 vs audited 316.7; filed conflict not flagged"
  style:
    - "S1: seasonality sentence (review l.193) omits the FY26 Q1-to-Q2 step of +4.1% (PR L378); conclusion holds on the 3-year average of 9.8%"
    - "S2: Forward Map rows ~6-Nov and 5-Nov out of date order (review l.581-582)"
    - "S3: Brief l.533 attribution tagged [FILED]; should be [FILED, computed]"
    - "S4: Step 7 (review l.393) cites disc l.43-58 for discovery heads leaving; departure is PR L153-154"
    - "S5: T5 'flat H2' undefined (review l.358); means H2 FY27 revenue = H2 FY26 1,953.6"
    - "S6: PR headline '6 percentage points' is 5.4 pp on filed figures (PR L42, L74, L131)"
    - "S7: A1 disclosure structured anchors drift 1-8 lines on boilerplate rows; material rows correct"
    - "S8: deck l.369 bullet has no structured row; A4 cites fulltext correctly; not an A2 category"
loop_back_to: "A4"
gap: "F1 Step 4 Q1 tax pairing (use 6.7 vs 5.7); F2 Note 4 impact 0.07 to 0.73; F3 CTS lab commissioned, fix 'no new capacity'; M1 add 23-Oct letter vs 27-Oct filing dates; M2 graft pre-op and hedge counter onto ex-FX 'underlying' margin; M3 graft cash qualifier onto revenue GREEN; M4 state Bayview cost to date vs price and no earnings multiple; C1 set 6D CDMO share to UNKNOWN; C2 show results-based TTM PAT 186.1 and flag the fact-sheet conflict"
style_notes:
  - "S1: add FY26 Q1-to-Q2 step (+4.1%) to the seasonality sentence"
  - "S2: reorder Forward Map rows by date"
  - "S3: retag Brief l.533 as [FILED, computed]"
  - "S4: cite PR L153-154 for discovery heads leaving"
  - "S5: define 'flat H2' in T5"
  - "S6: optional note that the '6 pp' headline is 5.4 pp"
  - "S7: A1 disclosure anchor drift on boilerplate rows"
  - "S8: deck l.369 bullet has no structured row; no ledger gap"
analyst_note: "Coverage is clean. Every count matches A2, and every structured ID sits in a ledger or, for the disclosure, in the structured file. Arithmetic is strong: 62 metric groups recomputed, 59 pass. Three numbers fail. Step 4 pairs the 10.2 total tax credit with the 5.7 pre-exceptional loss; the right pair is 6.7 against 5.7. Note 4 is tenfold low. TTM PAT uses a fact-sheet series that misses audited FY26 PAT by Rs 1.9 Cr. Two grafts matter most. First, the ex-FX margin is not underlying: expensing H1 Bayview pre-op takes it from 22.3% to about 18.1%. Second, Bayview has cost 64% more than its acquisition CWIP with no revenue until FY28, and as an asset deal it has no earnings multiple. On my reading no finding moves the PROCEED WITH FLAGS verdict. They correct numbers and add bear qualifiers. One A4 pass fixes all nine items."
```
