# A4 MERGED REVIEW: GHV Infra Projects Limited (GHVINFRA), Q2 FY27 (quarter and half year ended 30-Sep-2026)

Agent: A4 analyst | model: claude-opus-5-5 | run date: 2026-10-23
Protocol loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4 only).
Role 5: NOT RUN. No concall held (BSE shows no concall intimation; no presentation or press release filed).
Inputs read: A1 structured extraction (R001-R821), A1 fulltext (verbatim reads at lines 438-499), A2 ledger, A3 forensics, Notion context file (fetched 2026-10-23). No source PDF and nothing under inputs/ was opened.
Unit: source is Rs Lakhs. All figures below are Rs Crores (Lakhs x 0.01) unless marked L. "S" = standalone. "C" = consolidated. "l" = fulltext line. [derived] = computed only from filed numbers.

Orchestrator verification notes applied:
- FN13: the source PRINTS "16,16,667" warrants in S note 3 (l471) and C note 6 (l778), against 83,33,335 shares allotted. A4 treats this as a filing drafting inconsistency, not an OCR error. The OCR-RISK tag on FN13 is closed.
- l786 "Musanjji" is OCR noise. The page image prints "Musamji". Not a finding.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 19 notes (8 standalone + 11 consolidated) plus 2 EPS footnotes / 0 turns / 0 slides. All 19 notes and 2 footnotes reviewed. The full ledger holds 253 rows (L001-L196 line items, A01-A03, B01-B05, C01-C05, D01-D11, E01-E06, F01-F21, G01-G06). They reference all 821 structured IDs, with orphan_ids [] (A2 count test, gate_a2 pass). All 253 rows reviewed. No row is unreviewed.

Findings incorporated: FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20, FN21, FN22, FN23, FN24, FN25.
A3 FORWARD-SIGNAL (10): FN02, FN04, FN06, FN07, FN08, FN10, FN11, FN16, FN17, FN24. A3 AMBIGUOUS (11): FN01, FN03, FN05, FN13, FN14, FN15, FN19, FN21, FN22, FN23, FN25. Each one maps to at least one row in the Step 8.5 table (see the from_finding column).

---

## STEP 0: PRE-FLIGHT

### 0A. Notion page (fetched live 2026-10-23, page 387bb2b9-d3ab-81de-8c50-d96623d49e02)

| Field | Notion value |
|---|---|
| Decision Status (VERIFIED before framing) | AVOID (operator only; this pipeline never writes it) |
| Promoter Verdict | AVOID |
| Gate 0 | AVERAGE, 65/160 (Core 50/100, Moat 15/60) |
| EM | MOAT STRENGTHENING, 27/100 |
| Sector | EPC / Construction |
| CMP on page | Rs 239 (screener.in, 23-Oct-2026 05:34 IST) |
| Entry Price Max / MoS price / Position Size | blank (no levels on file) |
| One-line thesis | Permanent universe-exclusion record (AVOID, May 2026) |
| Four-pillar destination PE | none on file |
| Bear / Base / Bull projections | none on file |
| Thesis-broken frame | three re-entry conditions, ALL required (see 6C) |
| Monitoring checklist | 8 items from the Q1 FY27 review, 11-Aug-2026 (see 6B) |
| Devil's Advocate split | none on file |
| Prior Questions for Management | 6 rows (Q1 FY27; see answer-status table below) |
| Concall promise log | none (no concall in Q1 FY27) |
| Tracker rows | none linked; not supplied |

Framing: the name is NOT held. Decision Status is AVOID. This is a thesis check against an AVOID exclusion record. The position branch is 8A-W. No HOLD / ADD / TRIM / EXIT framing applies.

### 0B. Unit convention

The filing states "(Rs in Lakhs, except earnings per share)" (l325 S P&L; l617 C P&L), "(Rs in Lakhs)" (l367, l420, l671, l724). Conversion factor: Rs Cr = Rs Lakhs x 0.01.

### 0C. Share count changes

| Event | Detail | Anchor |
|---|---|---|
| FY26 sub-division | face value Rs 10 to Rs 5 | l473 |
| FY26 bonus | 3:2 | l473; EPS restated per Ind AS 33 para 64 (footnote l358, l662) |
| Q2 FY27 warrant conversion | Executive Committee on 27-Aug-2026 allotted 83,33,335 shares of Rs 5 to promoter JHV Commercials LLP, ratio 1:5 | l470-473 |
| Paid-up capital | 36.04 Cr (3,603.75 L) to 40.20 Cr (4,020.42 L); 8,04,08,335 shares | l353, l474-475 |
| Pre-conversion share count | 7,20,75,000 [derived: 3,603.75 L / Rs 5] | l353 |
| Pending warrants | 21,83,333 at 30-Sep-2026; at 1:5 = 1,09,16,665 shares, +13.58% on 8,04,08,335 [derived] | l475, l782 |
| Warrant count drafting conflict | Note prints 16,16,667 converted; 83,33,335 shares, 66.67 Cr proceeds (l448) and 50.00 Cr balance (l470) close only on 16,66,667 [derived: 16,66,667 x 5 = 83,33,335; 16,66,667 x Rs 400 = 66.67 Cr] | FN13; orchestrator confirms the source prints 16,16,667 |

Prior-period EPS is share-adjusted in the filing. Check: Q2 FY26 S PAT 1,122.20 L / 7,20,75,000 = Rs 1.557, printed 1.56 (l356) [derived].

### 0D. Notes extraction (all 19 notes and 2 footnotes)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| S1 (l463-466) | Basis | Results follow Ind AS under section 133. | none | all | none |
| S2 (l467-469) | Approval | Audit Committee reviewed, Board approved 22-Oct-2026, "subject to review" by auditors. | none | Q2, H1 | none |
| S3 (l470-475) | Warrant conversion | Promoter JHV Commercials LLP paid 50.00 Cr (5,000.01 L) balance; 83,33,335 shares allotted 27-Aug-2026; 21,83,333 warrants pending. | +50.00 cash; +4.17 capital (416.67 L) | Q2 FY27 | EPS denominator rises 11.56% from Q2 [derived: 83,33,335 / 7,20,75,000]; warrant count drafting conflict (FN13) |
| S4 (l476-480) | Promoter reclassification | AGM of 25-Sep-2026 approved moving Husena A. Musamji (37,50,000 shares, 5.20%) from Promoter to Public under Reg 31A. | none | Q2 FY27 | promoter group shrinks; exchange approval date NOT FOUND |
| S5 (l481-490) | Erisha EPC contract | The FZ-LLC contract with Rana Exim FZ-LLC "was concluded in the fourth week of September 2026 due to prolonged delays"; legal proceedings run; no provision. | 0 booked; C exposure up to 40.52 [derived, FN06]; parent exposure ND | Q2 FY27 onward | a provision can land in one future quarter (FN08) |
| S6 (l491-492) | Segment | One segment, Infrastructure Construction Services. | none | all | no segment split |
| S7 (l493) | Regrouping | Prior figures regrouped and reclassified. | ND (amounts not stated) | prior periods | cost-line mix comparisons carry a caveat (see Step 1 materials vs construction shift) |
| S8 (l494-495) | Availability | Results on company and BSE sites. | none | n/a | none |
| C1 (l765) | Basis | Ind AS basis. | none | all | none |
| C2 (l768-769) | Approval | States the results "have been reviewed by the Statutory Auditors of the Group". | none | Q2, H1 | contradicts auditor para 6 (l569-571): 2 subs and 1 JV unreviewed (FN19) |
| C3 (l770-771) | Scope | 2 wholly owned subs (GHV Infra FZ-LLC, GHV Infra Inc. Ohio) and 2 JVs (RKS-TCIPL, BIL). | n/a | all | entity baseline set this quarter (FN23) |
| C4 (l772) | BIL JV | Not commenced, no transactions to 30-Sep-2026, no share recognised. | 0 | Q2, H1 | none (FN09) |
| C5 (l775-777) | No PY comparatives | Consolidation started Dec-2025 quarter; Sep-2025 C quarter and half not presented. | n/a | Q2 FY26, H1 FY26 | C YoY impossible; ND throughout |
| C6 (l778-782) | Warrant conversion | Restates S3. | as S3 | Q2 FY27 | as S3 |
| C7 (l783-786) | Promoter reclassification | Restates S4. | none | Q2 FY27 | as S4 |
| C8 (l787-793) | Erisha | Restates S5 for the Group; no provision. | as S5 | as S5 | as S5 |
| C9 (l795) | Segment | One segment. | none | all | none |
| C10 (l796) | Regrouping | Prior figures regrouped. | ND | prior | as S7 |
| C11 (l797) | Availability | Results on websites. | none | n/a | none |
| FN-S EPS (l358) | EPS restatement | FY26 bonus and sub-division; EPS restated for all periods (Ind AS 33 para 64). | none | all | EPS comparable across periods |
| FN-C EPS (l662) | EPS restatement | Restates S footnote. | none | all | as above |

Per-note answers:
- Notes that change a YoY or sequential read: S3/C6 (EPS denominator), S5/C8 (contingent loss not in the P&L), C5 (no C YoY), S7/C10 (cost-line regrouping, amounts ND).
- Normalisation needed: no exceptional item is disclosed. The Q1-to-Q2 WIP swing of 13.51 Cr (l335) is not a note, but it distorts both quarters. A4 reads margins on H1 (FN01).
- Recurring vs one-off flags: none in the notes. The Q2 deferred tax credit of 2.02 Cr (l344) is unexplained (FN11).
- Thesis-relevant: S5/C8 (the UAE catalyst on file may be this contract), S3 (promoter capital in, more dilution pending), C2 vs auditor para 6 (governance).

Auditor opinion check:
- Standalone limited review: unmodified conclusion (l296). No Going Concern, no Emphasis of Matter, no Other Matter paragraph.
- Consolidated limited review: unmodified conclusion "based on the consideration of the matters referred to in paragraph 6 and 7" (l561). Para 6 (l569-589): two foreign subsidiaries and one JV "neither been reviewed by us nor reviewed by their auditors"; numbers "furnished to us by the Management"; called "not material to the Group". Para 7 (l591-597): BIL JV not commenced.
- No EoM and no modification. A4 still marks AMBER: the unreviewed share is 19.78% of H1 C PAT and the unreviewed assets are 19.75% of C equity (FN06), and they hold the Erisha exposure.

### 0E. Business type

Standard operating business (EPC / infrastructure construction services, one segment, l491). Not a lender. Steps 1 and 5 apply. Steps 1L and 5L do not.

Checkpoint: Notion fetched with Decision Status AVOID; units Rs Lakhs to Rs Cr; share changes listed; 19 notes and 2 footnotes extracted; auditor conclusions unmodified with reliance paragraphs; business type standard.

### Prior-quarter Questions for Management: answer status (Q1 FY27, 11-Aug-2026)

| # | Prior question (short) | From | Status this filing | Evidence |
|---|---|---|---|---|
| 1 | Publish consolidated Q1; quantify S-vs-C gap; BCA royalty / management fee / RPT eliminations | A3-01 | PARTIALLY ANSWERED | C Q1 published in this filing: C PAT 7.36 Cr (l642) vs S 11.25 Cr (l347). BCA royalty, management fee and RPT amounts: NOT DISCLOSED (no RPT note). |
| 2 | Split below-EBITDA charge into D&A vs finance cost; gross debt | A3-02 | ANSWERED | Q1 S finance 12.04 Cr (l337), D&A 0.49 Cr (l338). Gross debt at 30-Sep-2026 411.77 Cr (l396 + l402). Q1-end debt ND (no Jun-2026 balance sheet). |
| 3 | Why implied ETR 27.56% above 25.17%; actual tax; deferred position | A3-02 | PARTIALLY ANSWERED | Q1 tax 4.27 Cr (l346), current 4.61 Cr (l343), deferred (0.33) Cr (l344); Q1 ETR 27.52% [derived]. No reason given. DTA 2.34 Cr at Sep-26 (l376). |
| 4 | Reconcile diluted EPS Rs 1.48 to PAT 11.25 Cr; share counts; dilutive instruments | A3-03 | PARTIALLY ANSWERED | Basic Q1 Rs 1.56 (l356) ties to 7,20,75,000 shares [derived]. Only warrants are disclosed as dilutive (l475). H1 EPS does not reconcile (FN14). Warrant count conflict (FN13). |
| 5 | DINs, dates, AGM terms for the three Additional IDs; Dasgupta independence | A3-04 | NOT ADDRESSED | AGM date appears (l476). No ratification result, DINs or terms. A different ID resigned (l60-63). |
| 6 | Align results date and entity-name usage | A3-05 | PARTIALLY ANSWERED | This filing's letter date equals the board date, 22-Oct-2026 (A2 A03). It uses "Formerly Sindu Valley Technologies Limited" (l70). Corrected in practice; no explanation given. |

Second quarter in a row with Q5 not addressed. Log for the Promoter Verdict record (governance signal; the verdict is already AVOID).

---

## STEP 1: DATA EXTRACTION TABLE (STANDARD BUSINESS)

### 1-S. Standalone (Rs Cr)

FY27 full year is in progress, so the FY27 column is ND. H1 columns are added because Q2 carries the Reg 33 half-year statements.

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 183.77 | 218.60 | 300.08 | 605.53 | ND | 264.23 | 518.68 | l328 |
| Other Income | 0.06 | 0.28 | 0.30 | 0.39 | ND | 0.07 | 0.58 | l329 |
| Total Income | 183.82 | 218.88 | 300.38 | 605.92 | ND | 264.30 | 519.27 | l330 |
| Cost of Materials Consumed | 5.56 | 59.79 | 89.82 | 163.38 | ND | 5.71 | 149.61 | l332 |
| Construction Expenses | 47.66 | 7.00 | 7.13 | 10.32 | ND | 65.53 | 14.13 | l333 |
| Sub-Contracting Charges | 101.17 | 126.98 | 141.73 | 311.42 | ND | 150.22 | 268.71 | l334 |
| Change in Inventories (WIP) | (0.53) | (13.51) | 13.51 | (4.32) | ND | (2.10) | 0.00 (dash) | l335 |
| Employee Benefits Expense | 4.15 | 7.13 | 8.25 | 22.79 | ND | 8.19 | 15.38 | l336 |
| Finance Costs | 6.43 | 12.04 | 13.24 | 32.23 | ND | 8.42 | 25.28 | l337 |
| Depreciation and Amortisation | 0.05 | 0.49 | 0.78 | 1.72 | ND | 0.09 | 1.27 | l338 |
| Other Expenses | 3.48 | 3.44 | 3.86 | 11.09 | ND | 6.05 | 7.30 | l339 |
| Total Expenses | 167.98 | 203.36 | 278.31 | 548.64 | ND | 242.13 | 481.67 | l340 |
| Profit Before Tax | 15.85 | 15.53 | 22.07 | 57.28 | ND | 22.17 | 37.60 | l341 |
| Current Tax | 4.03 | 4.61 | 5.71 | 15.53 | ND | 5.64 | 10.31 | l343 |
| Deferred Tax | 0.60 | (0.33) | (2.02) | (0.08) | ND | 0.59 | (2.35) | l344 |
| Excess provision of earlier years | 0.00 (dash) | 0.00 (dash) | 0.00 (dash) | (0.43) | ND | 0.00 (dash) | 0.00 (dash) | l345 |
| Tax Expense (total) | 4.63 | 4.27 | 3.69 | 15.03 | ND | 6.23 | 7.96 | l346 |
| PAT | 11.22 | 11.25 | 18.38 | 42.26 | ND | 15.94 | 29.64 | l347 |
| EPS adjusted basic (Rs, reported) | 1.56 | 1.56 | 2.44 | 5.86 | ND | 2.21 | 4.09 | l356 |
| EPS diluted (Rs, reported) | 1.52 | 1.48 | 2.23 | 5.68 | ND | 2.19 | 3.86 | l357 |
| EPS (share-adjusted) | 1.56 | 1.56 | 2.44 | 5.86 | ND | 2.21 | 4.09 printed; 4.02 on Q2-consistent weighting [derived, FN14] | l356; FN14 |

### 1-S derived metrics

| Derived Metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 22.28 | 27.77 | 35.79 | 90.85 | ND | 30.61 | 63.56 |
| Operating EBITDA Margin | Op EBITDA / Revenue | 12.12% | 12.71% | 11.93% | 15.00% | ND | 11.59% | 12.25% |
| Reported EBITDA | PBT + D + FC | 22.34 | 28.06 | 36.09 | 91.24 | ND | 30.68 | 64.15 |
| Reported EBITDA Margin | Rep EBITDA / Revenue | 12.15% | 12.84% | 12.03% | 15.07% | ND | 11.61% | 12.37% |
| Core PBT (ex-OI) | PBT - OI | 15.79 | 15.24 | 21.77 | 56.89 | ND | 22.10 | 37.01 |
| Other Income / PBT | OI / PBT | 0.37% | 1.82% | 1.36% | 0.68% | ND | 0.31% | 1.55% |
| Effective Tax Rate | Tax / PBT | 29.19% | 27.52% | 16.70% | 26.23% | ND | 28.09% | 21.17% |
| PAT Margin | PAT / Revenue | 6.11% | 5.15% | 6.13% | 6.98% | ND | 6.03% | 5.71% |
| Gross margin after direct cost | (Rev - materials - construction - subcon - Δinv) / Rev | 16.27% | 17.54% | 15.96% | 20.60% | ND | 16.98% | 16.63% |
| Op EBIT / Finance cost | (Op EBITDA - D) / FC | 3.45x | 2.27x | 2.64x | 2.77x | ND | 3.62x | 2.46x |

All derived from l328-l347. The H1 FY26 operating EBITDA (30.61 Cr) equals the filed "Cash generated from Operations before Working Capital Changes" of 3,061.32 L (l428), which confirms the arithmetic.

WIP distortion (FN01). Q1 carried a WIP credit of 13.51 Cr (l335). Q2 reversed it in full. Q1 operating EBITDA without the credit = 14.26 Cr, a 6.53% margin [derived: 2,777.40 - 1,351.01 L]. Q2 without the charge = 49.30 Cr, a 16.43% margin [derived]. Neither single quarter is a clean read. H1 (12.25%) is the clean read. The Q1 media release headline "EBITDA% 12.83%" included the credit (A3 FN01, prior line 96).

### 1-C. Consolidated (Rs Cr)

Q2 FY26 and H1 FY26 consolidated columns are not presented (C note 5, l775-777). They are ND.

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | ND | 218.60 | 300.08 | 615.47 | ND | ND | 518.68 | l620 |
| Other Income | ND | 0.28 | 0.30 | 0.39 | ND | ND | 0.58 | l621 |
| Total Income | ND | 218.88 | 300.38 | 615.86 | ND | ND | 519.27 | l622 |
| Cost of Materials Consumed | ND | 59.79 | 89.82 | 163.38 | ND | ND | 149.61 | l624 |
| Construction Expenses | ND | 7.94 | 7.25 | 11.02 | ND | ND | 15.19 | l625 |
| Sub-Contracting Charges | ND | 126.98 | 141.73 | 311.42 | ND | ND | 268.71 | l626 |
| Change in Inventories (WIP) | ND | (13.51) | 13.51 | (4.32) | ND | ND | 0.00 (dash) | l627 |
| Employee Benefits Expense | ND | 8.08 | 8.97 | 23.85 | ND | ND | 17.05 | l628 |
| Finance Costs | ND | 12.05 | 13.25 | 32.24 | ND | ND | 25.29 | l629 |
| Depreciation and Amortisation | ND | 0.68 | 0.97 | 1.79 | ND | ND | 1.65 | l630 |
| Other Expenses | ND | 5.07 | 3.93 | 11.61 | ND | ND | 9.00 | l631 |
| Total Expenses | ND | 207.08 | 279.42 | 550.98 | ND | ND | 486.50 | l632 |
| Profit Before Tax | ND | 11.80 | 20.97 | 64.88 | ND | ND | 32.77 | l633 |
| Tax Expense (total) | ND | 4.27 | 3.69 | 15.64 | ND | ND | 7.96 | l638 |
| PAT before JV share | ND | 7.53 | 17.28 | 49.24 | ND | ND | 24.81 | l639 |
| Share of JV profit / (loss) | ND | (0.17) | 0.10 | (0.22) | ND | ND | (0.07) | l641 |
| PAT incl. JV (owners; NCI nil) | ND | 7.36 | 17.38 | 49.02 | ND | ND | 24.74 | l642-643 |
| EPS adjusted basic (Rs) | ND | 1.02 | 2.31 | 6.80 | ND | ND | 3.43 | l660 |
| EPS diluted (Rs) | ND | 0.97 | 2.11 | 6.59 | ND | ND | 3.24 | l661 |
| EPS (share-adjusted) | ND | 1.02 | 2.31 | 6.80 | ND | ND | 3.43 printed; 3.36 on Q2-consistent weighting [derived, FN14] | l660; FN14 |

### 1-C derived metrics

| Derived Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|
| Operating EBITDA | ND | 24.25 | 34.88 | 98.52 | ND | ND | 59.13 |
| Operating EBITDA Margin | ND | 11.09% | 11.62% | 16.01% | ND | ND | 11.40% |
| Reported EBITDA | ND | 24.53 | 35.18 | 98.91 | ND | ND | 59.71 |
| Core PBT (ex-OI) | ND | 11.52 | 20.66 | 64.49 | ND | ND | 32.19 |
| Other Income / PBT | ND | 2.40% | 1.43% | 0.60% | ND | ND | 1.78% |
| Effective Tax Rate | ND | 36.20% | 17.58% | 24.11% | ND | ND | 24.29% |
| PAT Margin (incl. JV) | ND | 3.37% | 5.79% | 7.96% | ND | ND | 4.77% |

All derived from l620-l642.

### 1-G. STANDALONE vs CONSOLIDATED GAP (first-class metric, A3 FN04/FN05/FN06)

| Metric | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|
| S PAT | 11.22 | 11.25 | 18.38 | 42.26 | 15.94 | 29.64 | l347 |
| C PAT incl. JV | ND | 7.36 | 17.38 | 49.02 | ND | 24.74 | l642 |
| C minus S PAT | ND | (3.89) | (1.00) | +6.76 | ND | (4.90) | [derived] |
| Gap as % of S PAT | ND | -34.57% | -5.47% | +16.00% | ND | -16.52% | [derived] |
| C minus S PBT (= subsidiaries' result) | ND | (3.72) | (1.10) | +7.60 | ND | (4.83) | l341, l633; H1 ties to sub loss 482.78 L (l573) |
| C minus S revenue (= subsidiary revenue) | ND | 0.00 | 0.00 | +9.94 | ND | 0.00 | l328, l620; subs revenue Nil (l571-572) |

Reading. The gap swung from +16.00% in FY26 to -34.57% in Q1 and -5.47% in Q2. Eliminations are nil at P&L level. The two foreign subsidiaries earned 9.94 Cr revenue in FY26 with zero materials and zero sub-contracting cost (FN05), carrying 7.60 Cr PBT, a 76% margin [derived]. In FY27 they earn nothing and cost 1.10 Cr to 3.72 Cr a quarter. The consolidated entity now earns less than the standalone entity. The Q1 media release headlined S PAT 11.25 Cr only (A3 section 0); C Q1 PAT was 7.36 Cr.

Checkpoint: both tables complete; every cell a line-anchored number, a derived figure, or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### 2-S. Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 183.77 | 300.08 | +63.30% | Strong growth |
| Operating EBITDA | 22.28 | 35.79 | +60.65% | Grew slower than revenue |
| Operating EBITDA Margin (pp change) | 12.12% | 11.93% | -20 bps | Flat to slightly down (Q2 absorbs the 13.51 Cr WIP release) |
| Depreciation | 0.05 | 0.78 | +1,331% (14.3x) | Asset build starting; small in Rs |
| Finance Costs | 6.43 | 13.24 | +105.78% | Absorbs most of the EBITDA gain |
| EBIT (operating) | 22.22 | 35.01 | +57.54% | Grew slower than revenue |
| Other Income | 0.06 | 0.30 | +412.27% | Immaterial in Rs |
| Core Operating PBT (PBT - OI) | 15.79 | 21.77 | +37.88% | Real growth, about 60% of revenue growth rate |
| Reported PBT | 15.85 | 22.07 | +39.27% | Close to core |
| PAT | 11.22 | 18.38 | +63.82% | Inflated by a lower ETR |
| EPS (share-adjusted, basic) | 1.56 | 2.44 | +56.41% | Diluted by the 27-Aug allotment |
| EPS diluted | 1.52 | 2.23 | +46.71% | Basic-diluted spread widened (FN15) |

Anchors: l328, l329, l337, l338, l341, l347, l356, l357; derived lines as Step 1.

### 2-C. Consolidated

Q2 FY26 consolidated: ND (C note 5, l775-777). No consolidated YoY is possible this quarter. The FY26 C figures exist only as a full year.

### 2-H. Half-year YoY (H1 FY27 vs H1 FY26, standalone; cleaner because the WIP swing nets to zero)

| Metric | H1 FY26 | H1 FY27 | YoY % Change |
|---|---|---|---|
| Revenue from Operations | 264.23 | 518.68 | +96.30% |
| Operating EBITDA | 30.61 | 63.56 | +107.63% |
| Operating EBITDA Margin | 11.59% | 12.25% | +67 bps |
| Finance Costs | 8.42 | 25.28 | +200.03% |
| Core PBT (ex-OI) | 22.10 | 37.01 | +67.49% |
| PAT | 15.94 | 29.64 | +85.94% |
| EPS basic (printed) | 2.21 | 4.09 | +85.07% (on printed H1 EPS that does not reconcile, FN14) |

### Six diagnostic answers

1. Did revenue grow YoY? Yes. Q2 FY27 revenue 300.08 Cr vs Q2 FY26 183.77 Cr, +63.30% (l328). H1 grew +96.30%. Company annual guidance: NOT FOUND (no concall, no press release). Notion base case: none on file. No comparison base exists beyond the prior year.
2. Did operating EBITDA margin expand, contract or stay flat YoY? Q2 FY27 margin 11.93% vs Q2 FY26 12.12% = -20 bps, flat. H1 FY27 12.25% vs H1 FY26 11.59% = +67 bps. Both readings sit far below the H2 FY26 standalone margin of 17.65% [derived: FY26 less H1 FY26] and the FY26 full-year 15.00%.
3. Did core operating PBT grow YoY? Yes. 15.79 Cr to 21.77 Cr, +37.88%. The headline is real at the core level, but the core grew at about 60% of the revenue rate.
4. What drove the gap between core PBT growth (+37.88%) and PAT growth (+63.82%)? Other income added 0.24 Cr (immaterial). The ETR fell from 29.19% to 16.70% on a 2.02 Cr deferred tax credit (l344). At the prior-year ETR, Q2 PAT would be 15.63 Cr, +39.27% YoY [derived: 2,206.98 L x (1 - 0.29187)]. At the 25.17% statutory rate, PAT would be 16.51 Cr, +47.16% [derived]. No exceptional item is filed. The tax line explains 2.76 Cr (38.5%) of the 7.16 Cr PAT gain (Step 4).
5. Are D&A and finance costs scaling faster than revenue? Yes. Finance cost +105.78% vs revenue +63.30%. D&A grew 14.3x from a near-zero base. Finance cost took 37.0% of Q2 operating EBITDA [derived: 13.24 / 35.79]. Interest cover (op EBIT / finance cost) fell from 3.45x to 2.64x. This is a debt-absorption deficit, not a D&A capex deficit.
6. Is Other Income concentration changing? No. OI was 1.36% of Q2 PBT and 1.55% of H1 PBT. It does not mask the trajectory.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

The filing gives Q2 FY26, Q1 FY27 and Q2 FY27 directly. Q1 FY26 and H2 FY26 are derived from H1 FY26 and FY26. Q3 FY26 and Q4 FY26 one by one are ND.

### 3-S. Standalone

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI) | One-offs Flagged | QoQ Run-Rate |
|---|---|---|---|---|---|
| Q1 FY26 [derived: H1 FY26 - Q2 FY26] | 80.46 | 10.36% | 6.31 | none filed | base |
| Q2 FY26 | 183.77 | 12.12% | 15.79 | WIP credit 0.53 (l335) | +128.40% vs Q1 FY26 |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND |
| H2 FY26 (2 quarters) [derived: FY26 - H1 FY26] | 341.31 (170.65 per quarter) | 17.65% | 34.80 | FY26 earlier-year tax write-back 0.43 (l345), below PBT | per-quarter avg -7.14% vs Q2 FY26 |
| Q1 FY27 | 218.60 | 12.71% (6.53% ex-WIP credit) | 15.24 | WIP credit 13.51 (l335) | +28.10% vs H2 FY26 quarterly avg |
| Q2 FY27 | 300.08 | 11.93% (16.43% ex-WIP release) | 21.77 | WIP release 13.51 (l335); deferred tax credit 2.02 below PBT (l344) | +37.28% QoQ |

### 3-C. Consolidated

| Quarter | Revenue | Op EBITDA Margin | Core PBT (ex-OI) | One-offs | QoQ |
|---|---|---|---|---|---|
| Q1 FY27 | 218.60 | 11.09% | 11.52 | WIP credit 13.51 (l627); sub loss 3.72 | base |
| Q2 FY27 | 300.08 | 11.62% | 20.66 | WIP release 13.51; sub loss 1.10 | revenue +37.28%; core PBT +79.37%; PAT +136.00% |

### Diagnostics

- Trajectory: revenue is STEPPING UP. Quarterly revenue moved 80.46 to 183.77 to an H2 FY26 average of 170.65 to 218.60 to 300.08 Cr. Margin is NOT stepping up. The H1 FY27 margin of 12.25% is 540 bps below the H2 FY26 margin of 17.65%.
- One-off distortion: Q1 and Q2 FY27 both carry the 13.51 Cr WIP swing (FN01). The H1 view nets it out.
- Latest quarter vs H1 average: Q2 revenue 300.08 Cr exceeds the H1 quarterly average of 259.34 Cr [derived]. Q2 core PBT 21.77 Cr exceeds the H1 average of 18.51 Cr.
- Capex commissioning test: CF capex was 43.71 Cr in H1 (l441) and PPE rose from 2.46 to 15.50 Cr (l371). Revenue rose. Margin did not. No plant-level utilisation is disclosed. ND.
- Implied Q3 FY27 base: revenue at or above 300.08 Cr with an operating EBITDA margin at or above the H1 12.25% keeps the trajectory. A margin below 11.59% (the H1 FY26 level) would mean growth bought with margin.

---

## STEP 4: OPERATIONAL DECOMPOSITION (PAT BRIDGE)

### 4-Q. Q2 FY27 vs Q2 FY26, standalone (Rs Cr)

| Component | YoY Change (Rs Cr) | Share of PAT change | Recurring? |
|---|---|---|---|
| Revenue contribution at Q2 FY26 op margin (Δrevenue 116.32 x 12.12%) | +14.10 | +196.9% | Recurring |
| Margin change contribution (Q2 FY27 revenue x -20 bps) | (0.59) | -8.2% | Recurring (includes WIP release) |
| D&A change | (0.72) | -10.1% | Recurring (post-capex) |
| Finance cost change | (6.81) | -95.0% | Recurring (post-debt) |
| Other Income change | +0.24 | +3.4% | NON-RECURRING typically |
| Tax on higher PBT at Q2 FY26 ETR 29.19% | (1.82) | -25.4% | Recurring |
| Effective tax rate change (29.19% to 16.70%) | +2.76 | +38.5% | Mixed; rests on an unexplained 2.02 Cr deferred credit (FN11) |
| Exceptional items | 0.00 | 0.0% | none filed |
| **Reported PAT YoY change** | **+7.16** | **100.0%** | 11.22 to 18.38 (l347) |

Check: 14.10 - 0.59 - 0.72 - 6.81 + 0.24 = 6.22 = ΔPBT (22.07 - 15.85, l341) [derived, in Lakhs 622.25]. Then 6.22 - 1.82 + 2.76 = 7.16 [derived, in Lakhs 716.23].

### 4-H. H1 FY27 vs H1 FY26, standalone (Rs Cr; WIP swing nets out)

| Component | YoY Change | Share | Recurring? |
|---|---|---|---|
| Revenue contribution at H1 FY26 margin (Δrevenue 254.46 x 11.59%) | +29.48 | +215.2% | Recurring |
| Margin change (+67 bps) | +3.47 | +25.3% | Recurring |
| D&A change | (1.18) | -8.6% | Recurring |
| Finance cost change | (16.85) | -123.0% | Recurring |
| Other Income change | +0.51 | +3.8% | Non-recurring |
| Tax on higher PBT at H1 FY26 ETR 28.09% | (4.33) | -31.6% | Recurring |
| ETR change (28.09% to 21.17%) | +2.60 | +19.0% | Mixed |
| Exceptional items | 0.00 | 0.0% | none |
| **Reported PAT YoY change** | **+13.70** | **100%** | 15.94 to 29.64 (l347) |

### Mandatory questions

- Recurring vs non-recurring share of the Q2 PAT change: about 58% comes from recurring operations net of recurring cost (revenue, margin, D&A, finance, volume tax: +4.16 Cr of +7.16 Cr) [derived]. About 42% comes from the ETR drop and other income (+3.00 Cr). The ETR item is not a filed one-off, but no note explains it.
- If Other Income reverts to the prior-year level: Q2 PBT falls by 0.24 Cr. Run-rate PAT barely moves. The tax line matters more: at the prior-year ETR, Q2 PAT = 15.63 Cr.
- D&A and finance cost steady state: D&A of 0.78 Cr a quarter sits on PPE of 15.50 Cr (l371) plus 29.97 Cr of other non-current assets (l377), likely capital advances [INFERENCE from the CF label "Movement in Capital Advances", l441]. D&A will rise when those assets commission. Finance cost: Q2 charge of 13.24 Cr against closing debt of 411.77 Cr. Average Q2 debt is ND, so the steady-state charge is ND. Debt more than doubled in H1 (191.61 to 411.77 Cr), so the risk is upward.
- Tax adjustments: the deferred tax credit of 2.02 Cr in Q2 and 2.35 Cr in H1 lifted PAT. The DTL of 0.01 Cr (Mar-26, l398) became a DTA of 2.34 Cr (Sep-26, l376). No note explains the temporary difference (FN11). The FY26 earlier-years write-back of 0.43 Cr (l345) sits in the base and must not be extrapolated (FN12).

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (STANDARD BUSINESS)

Q2 review, so the half-year cash flow and balance sheet are mandatory and used.

### 5-S. Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (H1) | (152.52) H1 FY26 (l439) | (244.37) H1 FY27 (l439) | outflow +91.85 | RED |
| CFO / PAT (H1) | -9.57x | -8.24x | n/m (both negative) | RED; below the lowest Pillar 2 band (0.65x) |
| Capex (PPE + capital advances, CF) | 0.81 (l441) | 43.71 (l441) | +42.89 | Step change for a sub-contracting model |
| FCF (CFO - Capex) | (153.33) | (288.08) | outflow +134.75 | RED |
| Working capital change (CF) | (178.22) [derived: l437 - l428]; (222.89) if the 44.68 Cr borrowing inside WC is removed (FN22) | (301.79) [derived] | larger outflow | RED |
| Receivable days (trade, on revenue) | 70.04 (Mar-26, FY26 basis) | 94.38 (Sep-26, H1 basis, 183 days) | +24.34 days | AMBER |
| Receivables + current other financial assets, days | 144.79 (Mar-26) | 253.90 (Sep-26) | +109.11 days | RED (FN24) |
| Inventory days (on direct cost) | 13.33 (Mar-26) | 8.52 (Sep-26) | -4.81 days | neutral |
| Payable days (on direct cost) | 107.79 (Mar-26) | 67.07 (Sep-26) | -40.72 days | AMBER (supplier funding fell) |
| Cash Conversion Cycle (trade only) | -24.42 days | 35.83 days | +60.25 days | RED |
| PPE | 2.46 (l371) | 15.50 (l371) | +13.04 | build |
| CWIP | ND (no CWIP line, l371-377) | ND | ND | ND |
| Other non-current assets | 0.00 (dash, l377) | 29.97 (l377) | +29.97 | new; capital advances [INFERENCE] (FN03) |
| Gross debt (l396 + l402) | 191.61 | 411.77 | +220.15 | RED |
| Cash + other bank balances (l382-383) | 8.96 | 23.53 (1.37 cash + 22.15 bank) | +14.57 | bank balance may be lien-marked (FN03) |
| Net Debt | 182.65 | 388.24 (410.39 if the 22.15 Cr bank balance is lien-marked) | +205.59 | RED |
| Net Debt / Equity | 1.48x | 1.91x (2.02x if lien-marked) | +0.43x | RED |
| Equity | 123.51 (l393) | 203.14 (l393) | +79.62 | promoter warrant money 50.00 + H1 PAT 29.64 |
| Promoter Pledge | ND (not in filing) | ND | ND | UNKNOWN |

Bases: receivable days = closing trade receivables / period revenue x period days (365 FY, 183 H1). Direct cost = materials + construction + sub-contracting + change in WIP (FY26 480.80 Cr; H1 FY27 432.44 Cr). Payables = MSE + other trade payables (l403-404). All [derived] from l328-l335, l380-l404.

Balance-sheet shifts that drive the cash outflow (Mar-26 to Sep-26, S):
- Trade receivables 116.20 to 267.50 Cr (l381), +151.30.
- Current other financial assets 124.00 to 452.14 Cr (l384), +328.14.
- Non-current other financial assets 160.44 to 10.71 Cr (l375), -149.72. Part of the current rise is a reclassification from non-current [INFERENCE]; the net rise in total other financial assets is 178.42 Cr [derived].
- Other current assets 141.55 to 122.18 Cr (l386), -19.37.
- Current borrowings 23.86 to 377.90 Cr (l402). Non-current borrowings 167.76 to 33.87 Cr (l396).

### 5-C. Consolidated

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (H1) | ND (no H1 FY26 C, note 5) | (246.77) (l742) | ND | RED |
| CFO / PAT (H1) | ND | -9.97x | ND | RED |
| Capex | ND | 43.37 (l744) | ND | as S |
| FCF | ND | (290.14) [derived] | ND | RED |
| Trade receivables / days | 126.72 (l685), 75.15 days on FY26 C revenue | 278.30 (l685), 98.19 days on H1 | +23.04 days | AMBER |
| Gross debt (l700 + l706) | 191.70 | 411.86 | +220.17 | RED |
| Net debt | 182.73 | 388.33 | +205.60 | RED |
| Net Debt / Equity | 1.39x (equity 131.49, l697) | 1.88x (equity 206.39, l697) | +0.49x | RED |
| Unreviewed subsidiary assets | ND | 40.76 (l571-572), 19.75% of C equity | n/a | AMBER (FN06) |

### Mandatory questions

- Is CFO/PAT meeting the Pillar 2 band? No. H1 FY27 S CFO/PAT is -8.24x and C is -9.97x. Both sit far below the lowest band (0.65x). No valuation is on file, so there is no assumed band to revise. Pillar-relevant fact flagged for /fttcp and Role 1.
- Is the WC drag structural or growth-induced? Test: if growth stopped, would WC days stay high? Evidence for structural: FY25 CFO was -55.63 Cr (Notion); H1 FY26 CFO was -152.52 Cr; H1 FY27 CFO was -244.37 Cr; cumulative CFO/PAT on file is -3.36x (Notion). Receivables plus current other financial assets went from 144.79 to 253.90 days. Evidence for growth-induced: H1 revenue grew +96.30%, and part of the other-financial-asset rise is a non-current to current shift. Missing evidence that would separate the readings: the make-up of the 452.14 Cr current other financial assets; the related-party share of receivables; the FY26 audited full-year CFO (in the FY26 Annual Report, not in this filing); any rating-agency WC view (none in context). Classification: INDETERMINATE-WITH-DIRECTION, direction structural. Per house rule this caps the verdict at PROCEED WITH CAVEATS or below.
- Did CWIP capitalise? No CWIP line exists. CF capex of 43.71 Cr is close to the PPE rise of 13.04 Cr plus the new other non-current assets of 29.97 Cr, together 43.01 Cr [derived]. Read: about 30 Cr is advances not yet capitalised [INFERENCE].
- Did net debt move within the projected range? No projection exists. Net debt rose 205.59 Cr in six months (S). Q2 finance cost annualised is 12.86% of closing gross debt [derived: 13.24 x 4 / 411.77]. Finance cost will keep flowing through future quarters at this debt level.

Cash conversion classification: INDETERMINATE-WITH-DIRECTION (structural lean). Missing evidence named above.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull

| Signal Name | Type | Cadence | Latest Observation | Direction | Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| none linked | ND | ND | ND | ND | ND | ND |

Tracker rows were not supplied, and Notion shows "Downstream Signals: none linked". Flag: fewer than three signals (zero). For an AVOID exclusion record this is expected. Reopening Role 5.5 is the operator's call; A4 does not recommend it while the name stays AVOID.

### 5.5B. Reconciliation

No signal readings exist. Target reported: strong revenue, weak cash. Matrix outcome: ND. The forward view rests on the filing alone.

### 5.5C. New signals surfaced (payload rows only; written only through the run's operator-approval gate; Decision Status never written)

- Candidate signal (Case B, create new): "Erisha / Rana Exim FZ-LLC legal proceedings outcome", event-driven. Reason: S note 5 / C note 8 (l481-490, l787-793) name a new external counterparty and a live dispute that can drive a one-quarter provision.
- Candidate signal (Case B, create new): "JHV Commercials LLP balance warrant conversion (21,83,333 warrants)", event-driven. Reason: S note 3 (l475); dilution and funding.
- No new customer above 10% is named. Customer concentration data is ND in this filing.

### 5.5D. Forward-view weighting

No signals to weigh. Step 6 runs on the filing alone, with the conservative bias.

---

## STEP 6: RECONCILIATION VS THESIS

Frame: Decision Status AVOID (verified). The thesis on file is an exclusion record, not a buy case.

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual | Lands In |
|---|---|---|---|---|---|
| Revenue (Q2 FY27, S) | ND | ND | ND | 300.08 (l328) | ND (no projections on the AVOID page) |
| EBITDA Margin (Q2 FY27 op, S) | ND | ND | ND | 11.93% [derived] | ND |
| PAT (Q2 FY27, S / C) | ND | ND | ND | 18.38 (l347) / 17.38 (l642) | ND |
| EPS (Q2 FY27 basic, S / C) | ND | ND | ND | 2.44 (l356) / 2.31 (l660) | ND |
| Net Debt (30-Sep-2026, S) | ND | ND | ND | 388.24 [derived] | ND |
| ROCE | ND | ND | ND | ND (not computed as a pillar input; see Step 7 flags) | ND |

Probability re-weighting rule: not applicable. No projections exist, so no below-bear count exists.

### 6B. Watchlist item status (Notion checklist, 11-Aug-2026)

Notion states no numeric green or red threshold for these items. A4 uses "disclosed and clean" as green and "absent or adverse" as red.

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| 1 | Reg 33 full statement with C, notes, limited review | full S + C statements, notes, LRR | partial filing | Delivered: S and C P&L, BS, CF; 8 + 11 notes; two LRRs (l245-808) | GREEN |
| 2 | AGM ratification of 3 Additional IDs; Dasgupta independence | ratification, DINs and terms disclosed | silent or adverse | Silent. AGM held 25-Sep-2026 (l476). ID Ravi Kumar Seth resigned on results day and left Audit and NRC (l60-63) | UNKNOWN (AMBER bias from the Seth exit) |
| 3 | C results and S-vs-C PAT gap (parent / BCA / RPT) | gap small and explained; RPT disclosed | gap large or RPT silent | Gap -5.47% Q2, -16.52% H1, -34.57% Q1, +16.00% FY26. BCA / RPT amounts NOT DISCLOSED | AMBER |
| 4 | Finance cost vs depreciation split | split disclosed; finance cost contained | finance cost dominates | Split disclosed. Q2 finance 13.24 Cr vs D&A 0.78 Cr; finance +105.78% YoY; cover 2.64x | AMBER |
| 5 | Basic / diluted EPS reconciliation, share count, PY EPS | reconciles | does not reconcile | Share count 8,04,08,335 and PY comparator given. H1 EPS overstated about Rs 0.07 (FN14). Warrant count printed 16,16,667 vs 16,66,667 arithmetic (FN13) | AMBER |
| 6 | Re-entry data: non-RPT order book %, CBI status, cumulative CFO | non-RPT > 40%; CBI closed; CFO positive | none met | Order book NOT DISCLOSED. CBI NOT DISCLOSED. H1 FY27 S CFO (244.37) Cr; H1 FY26 (152.52) Cr | RED |
| 7 | Governance-hygiene drafting errors | none | repeated errors | FN13, FN14, FN19, FN20, FN21, FN22 | RED |
| 8 | KMP churn (CFO / CS) | stable KMP | another change | New CFO Salim Yahoo w.e.f. 22-Oct-2026 (l53). Predecessor not named in the filing; Notion records CFO Sadanand Shetty resigned 21-Oct-2026. CS Daksh Mewada unchanged (l110) | RED (CFO); GREEN (CS) |

### 6C. Thesis-broken / re-entry trigger check

The AVOID page frames its conditions as RE-ENTRY conditions. All three are required for re-entry.

| Re-entry Condition | Threshold | Current Reading | MET? |
|---|---|---|---|
| (a) Non-related-party share of order book | > 40% for four consecutive quarters | Order book NOT DISCLOSED in this filing. Last known: 22-Jun-2026 Rs 213 Cr order from parent GHV (India) Pvt Ltd (RPT, Notion) | NOT MET (no evidence) |
| (b) CBI matter naming the promoter | closed, dismissed or exonerated | NOT DISCLOSED (no note) | NOT MET (no evidence) |
| (c) Cumulative CFO | positive for two consecutive years | H1 FY27 S CFO (244.37) Cr (l439); H1 FY26 (152.52) Cr (l439); FY25 (55.63) Cr (Notion); FY26 full-year CFO ND in this filing | NOT MET; moving away |

Original Gate 0 deal-breakers and promoter AVOID findings, status this quarter:

| AVOID basis (Notion) | This quarter | Direction |
|---|---|---|
| Operating history under 3 years | unchanged fact | n/a |
| Cumulative CFO/PAT -3.36x | H1 FY27 CFO/PAT -8.24x (S) | REINFORCED |
| Block B cash 3/20 | net debt 182.65 to 388.24 Cr | REINFORCED |
| Active CBI case naming promoter | not disclosed | UNCHANGED (no evidence) |
| Three CFO changes in 13 months | another CFO change (22-Oct-2026) | REINFORCED |
| Three CS changes in 13 months | CS unchanged across Q1 and Q2 | no new change |
| Audit-trail preservation failures | not testable in a limited review | UNCHANGED |
| 100% FY25 receivables from parent | related-party share ND | UNCHANGED (no evidence) |
| Reverse merger, BCA royalty / fee extraction | BCA amounts not disclosed | UNCHANGED (no evidence) |

Record inconsistency flag for the operator: Notion records "three CFO changes in 13 months" (May 2026) and also says the 21-Oct-2026 resignation letter calls Mr Shetty the "first CFO" with about 2 years tenure. The two Notion statements conflict. The filing names neither. A4 does not resolve it.

No condition for re-entry is met. The AVOID record is reinforced on cash, leverage and KMP churn. No trigger fires that would change Decision Status.

### 6D. Growth trigger status (EM catalyst list on file)

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| UAE contract, Rs 2,645 Cr | not stated on page | none | The FZ-LLC Erisha EPC contract at RAKEZ "was concluded in the fourth week of September 2026 due to prolonged delays", with legal proceedings (l481-486). Subsidiary revenue Nil in Q2 and H1 (l571-572). Contract value not stated in the filing, so identity with the Rs 2,645 Cr catalyst is unconfirmed (pending operator ruling 1) | DEAD if the same contract; WEAKENED at minimum |
| USA contract, Rs 840 Cr | not stated | none | GHV Infra Inc. (Ohio) is one of two subs with Nil revenue (l571-572) | DELAYED |
| Cameroon contract, Rs 7,000 Cr | not stated | none | Filing silent; no Cameroon entity in the consolidation list (l770-771) | DELAYED |
| Rs 213 Cr parent work order (22-Jun-2026, 14 months, RPT) | not stated | Revenue +63.30% YoY in Q2 is consistent with execution, but the filing does not attribute revenue to orders | none | UNVERIFIED (filing silent; outside the protocol status set, flagged) |

Checkpoint: 6A-6D complete.

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

DEFERRED to /fttcp and Role 1 (operator ruling OR-30). No expectation ledger rows are on file for this AVOID name.

Pillar-relevant facts flagged for the A21 base (not computed into a base here):
- H1 FY27 S revenue 518.68 Cr (l328), S PAT 29.64 Cr (l347). The Q1 and Q2 quarters carry the 13.51 Cr WIP swing, so single-quarter annualisation is distorted. An H1 or trailing-4-quarter base is the defensible choice.
- TTM S PAT = 55.95 Cr [derived: FY26 42.26 - H1 FY26 15.94 + H1 FY27 29.64]. TTM C PAT is ND (no H1 FY26 C).
- The Q2 ETR of 16.70% is not a run-rate ETR (FN11).

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION

DEFERRED to /fttcp and Role 1 (operator ruling OR-30). No pillar values exist on file.

| Pillar / Input | Original Assumption | Current Reading (fact flagged) | Action |
|---|---|---|---|
| ROCE Base | none on file | Op EBIT H1 FY27 62.29 Cr (S) [derived]; capital employed at Sep-26: equity 203.14 + gross debt 411.77 + lease 0.18 = 615.08 Cr [derived]. Spot, H1 annualised, closing-balance reading 20.25% [derived]; information only, not a pillar input | Deferred; FTTCP ROCE forward verdict governs |
| Cash Multiplier | none on file | CFO/PAT H1 FY27 -8.24x (S), -9.97x (C); below the 0.65x band | Deferred; flag |
| Growth Visibility Premium | none on file | Order book ND; UAE catalyst likely ended; subs Nil revenue | Deferred; flag |
| Strategic Premium | none on file | no moat evidence in filing | Deferred |
| UA Multiplier | none on file | qualifiers not testable from this filing | Deferred |
| Sector Cap | EPC / Construction | no reclassification; one segment (l491) | Hold |
| Hurdle Ratio recheck | none on file | CMP Rs 239 (Notion, SECONDARY). Market cap Rs 1,921.76 Cr on 8,04,08,335 shares [derived]; Rs 2,182.67 Cr on 9,13,25,000 fully diluted shares [derived]. P/E on TTM S PAT 34.35x [derived] | Deferred |

---

## STEP 8: POSITION DECISION

Decision Status verified at Step 0A: AVOID. Branch: 8A-W (non-held name).

### 8A-W logic applied

- Thesis-broken condition fired? The page is already AVOID. No re-entry condition is met (6C). Output: AVOID stands. What must reverse for re-entry is unchanged: (a), (b) and (c) above.
- Below bear on 2+ metrics? ND (no projections).
- Updated entry zone: none. No levels on file, and no valuation runs on an AVOID record.
- Updated gate: unchanged. The re-entry gate stays the three conditions.
- Proposed Decision Status: NO CHANGE (AVOID). The operator sets it.

### 8B. Trigger refinement (proposal only; the operator decides)

- Original add-back (re-entry) triggers: (a) non-RPT order book > 40% for 4 quarters; (b) CBI matter closed; (c) two consecutive years of positive cumulative CFO.
- Proposed additions:
  - (d) Erisha contingency resolved, with the GHV Infra FZ-LLC exposure quantified and either recovered or provided, and FZ-LLC numbers reviewed by an auditor.
  - (e) Consolidated PAT at or above standalone PAT for two consecutive quarters (the S-vs-C gap stops being negative), with BCA royalty / fee amounts disclosed.
- Original trim ladder: not applicable (not held).

### 8C. Single cleanest metric for the next reading

Metric: FY27 standalone CFO (and H2 FY27 CFO, derived as FY27 less H1 FY27 (244.37) Cr). Reading date: FY27 audited results, Reg 33 deadline 30-May-2027. Q3 FY27 (deadline 14-Feb-2027) carries no cash flow statement, so its proxy is finance cost and the Erisha note.
- Bull threshold: H2 FY27 CFO at or above +244.37 Cr, so FY27 CFO is zero or positive.
- Bear threshold: FY27 CFO negative, which pushes re-entry condition (c) out by at least two more years.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

No concall. Channel: IR email, plus AGM Q&A at the FY27 AGM. Ordered by thesis materiality.

| # | Question | Cat | From finding | Why it matters | Bull answer | Bear answer |
|---|---|---|---|---|---|---|
| 1 | Of the Rs 40.76 Cr of assets in the two unreviewed subsidiaries (l571-572), what Rs amount is receivable from or advanced against Rana Exim FZ-LLC on Erisha? | D | FN06, FN02 | A3 reconciles Rs 40.52 Cr of these assets to receivables and other current assets with no provision | A Rs figure, with security or advance cover | No figure, or most of the 40.52 Cr is unsecured |
| 2 | Is the Erisha EPC contract the Rs 2,645 Cr UAE contract announced earlier? State its contract value. | E | FN10 | Decides whether the main UAE catalyst on file is dead (operator ruling 1) | Different contract; UAE order still live with a value | Yes, same contract |
| 3 | In the Erisha legal proceedings, which party started them, and what is the Rs claim amount on each side? | E | FN10 | Sizes the contingent loss or recovery | GHV is claimant, claim above exposure | Counterclaim against GHV, or amount refused |
| 4 | Does the parent carry a guarantee, back-to-back sub-contract or receivable from FZ-LLC tied to Erisha? Yes or no, with the Rs amount. | D | FN10 | The standalone note also states "no provision" (l487); S current other financial assets exceed C by Rs 13.50 Cr [derived, l384 vs l688] | No; the 13.50 Cr is unrelated | Yes; parent carries the exposure |
| 5 | By which quarter do you expect the Erisha outcome to be "reasonably ascertainable" (l489), and will the Q3 FY27 review include a provision assessment? | B | FN08 | A provision can land in one quarter | A dated outcome, with assessment in Q3 | "Cannot say" |
| 6 | What is the quantitative basis for calling the unreviewed subsidiaries "not material" (l588), when their H1 loss is 19.78% of H1 C PAT and their assets are 19.75% of C equity? When will an auditor review FZ-LLC? | G | FN06 | Reliance on management-certified numbers holds the Erisha exposure | A dated review appointment | No basis given, no date |
| 7 | What makes up the Rs 452.14 Cr current other financial assets (l384): unbilled revenue, retention, deposits, related-party balances? Give each in Rs. | D | FN24 | Drives the -8.24x CFO/PAT and the structural vs growth-induced test | Mostly unbilled revenue on billed milestones | Material related-party deposits or advances |
| 8 | What share of the Rs 267.50 Cr trade receivables (l381) is due from GHV (India) Pvt Ltd or other related parties? | E | FN24 | Re-entry condition (a); FY25 receivables were 100% parent (Notion) | Below 40% | Above 40% or not given |
| 9 | Give the debt schedule for the Rs 377.90 Cr current borrowings (l402): lender, facility, rate. Was the Rs 133.89 Cr fall in non-current borrowings a repayment or a move to current maturities? | F | FN25 | Debt doubled in H1; CF lines equal BS deltas to the paisa | Working-capital lines with stated rates; genuine refinancing | Short-term debt funding long-dated receivables |
| 10 | Does the board plan an equity raise (QIP, preferential or rights) in FY27? State the amount and target date. | F | FN16 | New CFO's profile centres on QIPs and IPOs (l135); CFO (244.37) Cr | Raise sized to retire short-term debt | Repeated raises to fund WC |
| 11 | Name the outgoing CFO and his last working day. Is the change linked to the audit or the H1 debt build-up? Yes or no. | G | FN16 | Notion records CFO Shetty resigned 21-Oct-2026; the filing names no predecessor | Clear handover; no link | Evasion |
| 12 | What is the exercise deadline and price of the 21,83,333 pending warrants, and will JHV Commercials LLP convert them? | F | FN07 | About Rs 65.50 Cr inflow [derived, at Rs 400 and 75% balance] and +13.58% shares | Dated, promoter confirms | No date; lapse risk |
| 13 | Note 3 and note 6 print 16,16,667 warrants converted, but 83,33,335 shares and Rs 66.67 Cr close only on 16,66,667. Which is correct, and will you file a correction? | G | FN13 | A capital-structure note that does not add up | Typo admitted; corrected filing | No answer |
| 14 | Give the weighted-average share count behind H1 basic EPS of Rs 4.09 (S) and Rs 3.43 (C). | G | FN14 | A3 derives Rs 4.02 and Rs 3.36 on the Q2 weighting | Count given, error corrected | No count |
| 15 | Apart from the 21,83,333 warrants, does any dilutive instrument exist (ESOP, convertible, other warrant)? Yes or no. | F | FN15 | Basic-diluted spread rose from 2.6% to 8.6% (S) | No; the spread is a price effect | Yes, an undisclosed instrument |
| 16 | Which temporary difference created the Rs 2.02 Cr Q2 deferred tax credit (l344) and the Rs 2.34 Cr DTA (l376)? What ETR do you expect for FY27? | C | FN11 | Lifted Q2 PAT growth from +39% to +64% | A named, durable difference | No answer; ETR reverts |
| 17 | What cost did you carry into WIP in Q1 FY27 (Rs 13.51 Cr) and why did it release in full in Q2 (l335)? | C | FN01 | The Q1 release headline margin rested on it | Billing timing on a named milestone | No answer |
| 18 | Is the Rs 22.15 Cr bank balance (l383) lien-marked as margin money? Yes or no. | D | FN03 | Net debt 388.24 Cr vs 410.39 Cr | Free cash | Lien-marked |
| 19 | What is the Rs 29.97 Cr of other non-current assets (l377), and to whom were capital advances paid? | F | FN03, FN25 | Capex 43.71 Cr is a step change for a sub-contractor | Named equipment vendor, dated delivery | Advance to a related party |
| 20 | What was the Rs 9.94 Cr FY26 subsidiary revenue, booked with no material or sub-contracting cost? | C | FN05 | FY26 C PAT beat S by Rs 6.76 Cr on it | A named, billed, collected fee | Unbilled or uncollected |
| 21 | Will the board wind down or redeploy GHV Infra FZ-LLC and GHV Infra Inc.? State the decision date. | B | FN02, FN05 | Subs cost Rs 1.10 Cr (Q2) to Rs 3.72 Cr (Q1) a quarter with Nil revenue | Dated decision | Indefinite carry |
| 22 | Will future consolidated notes carry the auditor's reliance caveat, instead of "reviewed by the Statutory Auditors of the Group" (l768-769)? Yes or no. | G | FN19 | Note overstates review coverage | Yes | No |
| 23 | After Mr Seth's exit, how many independent directors sit on the board and on the Audit Committee? Were the three Additional IDs regularised at the 25-Sep-2026 AGM? | G | FN17 | Committee independence; prior Q5 not addressed for two quarters | Counts given, compliant | Below the required count |
| 24 | Which entity is the "Partnership Firm" in both cash flows (Rs 0.22 Cr, l426, l731), and what is the correct H1 FY27 adjustment? | G | FN21 | The figure equals the FY26 JV share, a stale plug | Named entity; corrected | No answer |
| 25 | Who are RKS and TCIPL in the GHV Infra Projects-RKS-TCIPL JV? Is either a related party? Yes or no. | E | FN23 | RPT exposure through JVs | Third parties | Related party |
| 26 | Why did the H1 FY26 comparative CFO include a Rs 44.68 Cr "Increase in Borrowings" inside working capital (l433)? Will the FY27 accounts reclassify it? | D | FN22 | H1 FY26 CFO would be (197.19) Cr without it [derived]; re-entry (c) series | Reclassified | Kept in CFO |
| 27 | What royalty and management fee did the company pay GHV (India) Pvt Ltd under the BCA in H1 FY27, in Rs? | E | FN04 | Notion AVOID basis 6; prior Q1 not answered | Small and disclosed | Not disclosed |
| 28 | What is the 30-Sep-2026 order book, and what Rs share comes from non-related-party customers? What is the status of the CBI matter? | B | 6C re-entry (a), (b) | Re-entry data; filing silent | Non-RPT > 40%; CBI closed | Not disclosed |

Top 3 questions ranked by likelihood of thesis-changing information:
- Q2 (UAE catalyst identity): a "different contract" answer reopens the UAE catalyst. A "same contract" answer confirms it dead.
- Q7 (make-up of the Rs 452.14 Cr other financial assets): material related-party balances would confirm the structural cash reading and the bear case.
- Q6 (basis for "not material" and FZ-LLC review date): an evasive answer is itself a transparency test.

Channel recommendation: IR email now, with all 28 questions verbatim (no concall is scheduled, and the Q1 questions went unanswered). Repeat the top 3 at the FY27 AGM.

---

## MONITORABLES / CATALYST LIST (A3 commitment register C1-C9 plus Board Outcome items)

| # | Item | Implied date | Source |
|---|---|---|---|
| M1 | Q3 FY27 results: Erisha reassessment (C2), finance cost, ETR, S-vs-C gap | by 14-Feb-2027 (Reg 33, 45 days) | S note 5 l488; C note 8 l792 |
| M2 | Erisha outcome disclosure and any provision (C3) | undated, outcome-dependent | S note 5 l489; C note 8 l793 |
| M3 | Erisha contract end (C4): completed; legal proceedings ongoing | fourth week of Sep-2026 (done) | l482, l788 |
| M4 | Conversion of the 21,83,333 pending warrants (C1) | NOT FOUND (no deadline filed) | S note 3 l475; C note 6 l782 |
| M5 | BIL JV commencement (C5) | NOT FOUND | C note 4 l772; auditor para 7 l591 |
| M6 | Husena A. Musamji reclassification, exchange approval (C6) | NOT FOUND (members approved 25-Sep-2026) | l476-480 |
| M7 | New CFO Salim Yahoo in office (C7); watch KMP churn | from 22-Oct-2026 | l52-54 |
| M8 | ID Ravi Kumar Seth exit (C8); board and Audit Committee recomposition | exit 22-Oct-2026; replacement by 22-Jan-2027 if the board falls below the required ID count (Reg 25(6), three months) [INFERENCE] | l60-63; l827 |
| M9 | Results upload to website (C9) | 22-Oct-2026 (done) | l49-50 |
| M10 | FY26 Annual Report (AGM held 25-Sep-2026): schedule Role 6; extract FY26 audited CFO, RPT, BCA amounts | now | l476 (FN18) |
| M11 | FY27 audited results: FY27 CFO (cleanest metric), re-entry (c) | by 30-May-2027 (Reg 33, 60 days) | Step 8C |
| M12 | Q1 FY28 results | by 14-Aug-2027 (Reg 33) | regulatory calendar [INFERENCE] |
| M13 | Rs 213 Cr parent work order, 14-month execution from 22-Jun-2026 | about 22-Aug-2027 | Notion (MGMT, prior record) |
| M14 | Possible equity raise (QIP / preferential) | NOT FOUND [INFERENCE from FN16] | l127-136 |

---

## STEP 9: NOTION PAYLOAD (not written by A4; operator-approval gate only)

- Decision Status: NOT WRITTEN. Proposed change: none. No trigger fired.
- Promoter Verdict: no change proposed (AVOID). Governance log: prior Q5 not addressed for two quarters; another CFO change.
- Key Notes prepend (proposed): "2026-10-23 | Q2 FY27 results review: revenue +63.30% YoY, core PBT +37.88%, H1 CFO -244.37 Cr, net debt 388.24 Cr; Erisha UAE contract ended with legal proceedings, no provision; AVOID reinforced, no re-entry condition met."
- Page content: append this full review (all tables).

Catalyst status: DEAD (UAE, if same contract) / DELAYED (USA, Cameroon). Thesis status (AVOID record): INTACT, reinforced.
Auditor opinion: Unmodified (S); Unmodified with reliance paragraphs 6-7 (C). Business type: Standard.
Source: BSE Reg 33 filing GHV_Q2FY27_Results_Reg33_2026-10-22 (A1 extraction).

---

## FLAGS (surfaced for the operator; the decision stays human)

1. Erisha: the FZ-LLC EPC contract ended early with legal proceedings. Up to 40.52 Cr of subsidiary assets sit unprovided and unreviewed (FN06, FN08, FN10).
2. Cash: H1 FY27 S CFO (244.37) Cr against PAT 29.64 Cr (-8.24x). Cash conversion INDETERMINATE-WITH-DIRECTION (structural lean).
3. Leverage: gross debt 191.61 to 411.77 Cr in six months; current borrowings 377.90 Cr; net debt / equity 1.91x.
4. Earnings quality: 38.5% of the Q2 PAT gain comes from an unexplained ETR drop (16.70%).
5. S-vs-C gap negative: C PAT below S PAT in Q1, Q2 and H1.
6. Governance drafting: warrant count (printed 16,16,667 vs 16,66,667), H1 EPS, C note 2 vs auditor para 6, stale CF plug, template labels.
7. KMP and board churn: new CFO on results day; ID left Audit and NRC on results day.
8. Notion record conflict: "three CFO changes in 13 months" vs "first CFO, about 2 years".
9. UAE Rs 2,645 Cr catalyst: likely dead; operator ruling 1 pending.
10. Q1 media release reported S only; its headline margin rested on a 13.51 Cr WIP credit.

Protocol verdict: PROCEED WITH FLAGS. The filing is complete and every step ran. Cash conversion is INDETERMINATE-WITH-DIRECTION, which caps the verdict at PROCEED WITH CAVEATS or below. The flags above propagate.

---

## PLAIN-LANGUAGE BRIEF

### 1. SUMMARY NARRATIVE

GHV Infra grew fast this quarter, but the cash went the other way.
Q2 FY27 revenue was Rs 300.08 Cr, up 63.30% on last year (FILED, this quarter).
Standalone PAT was Rs 18.38 Cr, up 63.82% (FILED).
Core profit before tax, without other income, grew only 37.88% (FILED, derived).
A lower tax rate gave about 38% of the profit gain. No note explains it.
In the half year, the company used Rs 244.37 Cr of cash in operations (FILED).
Debt more than doubled, from Rs 191.61 Cr to Rs 411.77 Cr (FILED).
Most new debt is short-term, Rs 377.90 Cr.
The UAE Erisha contract, run by the UAE subsidiary GHV Infra FZ-LLC, ended early (FILED).
Legal proceedings are now open. The company booked no provision.
About Rs 40.52 Cr of subsidiary assets depend on that dispute (FILED, derived).
No auditor reviewed those subsidiary numbers.
The consolidated group now earns less than the standalone company.
A new CFO with a fund-raising profile joined on results day. An independent director left the same day.
The Notion record says AVOID. Nothing in this filing meets any of the three re-entry conditions.
The cash and leverage facts make the AVOID case stronger, not weaker.
The next decisive reading is FY27 operating cash flow, due by 30-May-2027.

### 2. SECTOR INTELLIGENCE

- Indian EPC contractors sell execution capacity on fixed or item-rate contracts. Cash follows milestone billing and client payment, so working capital decides returns [INFERENCE, general sector frame; no sector numbers in the inputs].
- West Asia project risk is real for this company. The filing gives "uncertainties arising from the geopolitical situation in West Asia" and "prolonged delays in obtaining Project and Master Plan approvals" as the reasons the Erisha contract ended (FILED, l483-484, this quarter).
- Payer mix: the parent GHV (India) Pvt Ltd gave 100% of FY25 receivables and the Rs 213 Cr June 2026 order (MGMT/prior record, Notion). This filing gives no payer split (NOT DISCLOSED).
- Rising interest burden is a sector-wide risk for small contractors who fund receivables with short-term debt. GHV's Q2 finance cost was 12.86% of closing debt annualised (FILED, derived).
- Sector demand cycle, government capex data and peer order-inflow data: NOT FOUND in the inputs.

### 3. BUSINESS-MODEL INTELLIGENCE

- The company sub-contracts most of its work. Sub-contracting was 51.81% of H1 FY27 revenue and materials were 28.84% (FILED, derived, this quarter).
- After all direct costs, the gross margin was 16.63% in H1 FY27 against 16.98% in H1 FY26 (FILED, derived). Total direct cost is stable.
- The cost mix inside direct cost moved. Materials rose from 2.16% to 28.84% of revenue. Construction expenses fell from 24.80% to 2.72% (FILED, derived). Note 7 says prior figures were regrouped, so part of this may be classification (FILED, l493).
- The model is getting heavier. Capex was Rs 43.71 Cr in H1 against Rs 0.81 Cr a year earlier (FILED). PPE rose from Rs 2.46 Cr to Rs 15.50 Cr. A pass-through sub-contractor is starting to own assets [INFERENCE].
- Unit economics after finance cost are thin. Finance cost took 37.0% of Q2 operating EBITDA (FILED, derived).
- The overseas arm made money in FY26 (Rs 9.94 Cr revenue with no direct cost, FILED derived) and makes losses now. That revenue type is unexplained.
- Model drift this quarter: more own procurement, more own assets, more short-term debt, and a dead or stalled overseas leg.
- Order book, utilisation, bid pipeline and billing terms: NOT DISCLOSED.

### 4. COMPETITION INTELLIGENCE

- Named peer set: NOT FOUND. The Notion page passes no peers, and the filing names none. A4 adds no peer numbers.
- Where GHV wins: it grew revenue 96.30% in H1 (FILED). It has a captive order source in its parent (MGMT/prior record, Notion), which gives volume without open bidding.
- Where GHV is structurally weaker: the captive source is a related party, so the volume does not prove market competitiveness [INFERENCE]. Its cash cycle widened to 253.90 days of receivables plus other financial assets (FILED, derived). A contractor that funds clients on short-term debt loses when rates or collections move against it [INFERENCE].
- Its only named third-party overseas contract has ended in a dispute (FILED). That weakens the claim that it can win and run work outside the parent group [INFERENCE].
- Competitive risk to watch: whether any non-related-party order appears with a stated value. The filing discloses none.

### 5. FORWARD MAP (next ~10-11 months, to about Sep-2027)

Make-or-break reading: FY27 standalone CFO, due with FY27 audited results by 30-May-2027. Bull: H2 FY27 CFO at or above +Rs 244.37 Cr, so FY27 CFO is zero or positive. Bear: FY27 CFO negative.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| Now | FY26 Annual Report (AGM held 25-Sep-2026) | FY26 CFO, RPT and BCA amounts show a smaller parent share | AR confirms high parent dependence and negative FY26 CFO |
| by 22-Jan-2027 [INFERENCE] | Board and Audit Committee recomposition after the Seth exit | A new independent director is named, committees compliant | Seat stays empty or a related person fills it |
| by 14-Feb-2027 | Q3 FY27 results | Revenue at or above Rs 300.08 Cr, op margin at or above 12.25%, Erisha recovery stated | Erisha provision on up to Rs 40.52 Cr, or margin below 11.59% |
| undated | Erisha legal outcome | GHV recovers its exposure | One-quarter write-down of subsidiary assets |
| NOT FOUND | Conversion of 21,83,333 warrants | Promoter pays about Rs 65.50 Cr, debt falls | Warrants lapse; funding gap stays |
| NOT FOUND [INFERENCE] | Possible QIP or preferential raise | Raise retires short-term debt | Raise funds more receivables; dilution without cash return |
| by 30-May-2027 | FY27 audited results | FY27 CFO zero or positive | FY27 CFO negative; re-entry (c) pushed out two more years |
| about 22-Aug-2027 | Rs 213 Cr parent order completes | Billed and collected in cash | Billed but sits in receivables from the parent |
| by 14-Aug-2027 | Q1 FY28 results | Non-related-party order disclosed with a value | Order book still silent |

---

```yaml
stage: A4-analyst
company: "GHVINFRA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results]
ledger_reconciliation:
  notes: 19
  turns: 0
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: [FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20, FN21, FN22, FN23, FN24, FN25]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "AVOID"
position_branch: "8A-W"
sc_gap_pat_pct: ["Q2FY26: ND (no C comparative, note 5 l775)", "H1FY26: ND", "FY26: +16.00", "Q1FY27: -34.57", "Q2FY27: -5.47", "H1FY27: -16.52"]
questions_for_management:
  - {q: "Rs amount of the 40.76 Cr unreviewed subsidiary assets receivable from or advanced against Rana Exim on Erisha", from_finding_id: "FN06"}
  - {q: "Is the Erisha EPC contract the Rs 2,645 Cr UAE contract; state its value", from_finding_id: "FN10"}
  - {q: "Who started the Erisha legal proceedings and what is the Rs claim on each side", from_finding_id: "FN10"}
  - {q: "Does the parent carry an Erisha guarantee, back-to-back sub-contract or receivable from FZ-LLC; Rs amount", from_finding_id: "FN10"}
  - {q: "By which quarter will the Erisha outcome be ascertainable; will Q3 FY27 carry a provision assessment", from_finding_id: "FN08"}
  - {q: "Basis for 'not material' at 19.78% of H1 C PAT; date of auditor review of FZ-LLC", from_finding_id: "FN06"}
  - {q: "Make-up of the 452.14 Cr current other financial assets in Rs", from_finding_id: "FN24"}
  - {q: "Related-party share of the 267.50 Cr trade receivables", from_finding_id: "FN24"}
  - {q: "Debt schedule for 377.90 Cr current borrowings; repayment or reclass of the 133.89 Cr non-current fall", from_finding_id: "FN25"}
  - {q: "Planned FY27 equity raise: amount and date", from_finding_id: "FN16"}
  - {q: "Name the outgoing CFO; is the change linked to the audit or debt build-up (yes/no)", from_finding_id: "FN16"}
  - {q: "Exercise deadline and price of 21,83,333 pending warrants; will JHV convert", from_finding_id: "FN07"}
  - {q: "16,16,667 vs 16,66,667 warrants converted; which is correct; corrected filing", from_finding_id: "FN13"}
  - {q: "Weighted share count behind H1 EPS Rs 4.09 S and Rs 3.43 C", from_finding_id: "FN14"}
  - {q: "Any dilutive instrument besides the pending warrants (yes/no)", from_finding_id: "FN15"}
  - {q: "Temporary difference behind the 2.02 Cr Q2 deferred credit and 2.34 Cr DTA; FY27 ETR", from_finding_id: "FN11"}
  - {q: "What cost sat in Q1 WIP (13.51 Cr) and why it released in Q2", from_finding_id: "FN01"}
  - {q: "Is the 22.15 Cr bank balance lien-marked (yes/no)", from_finding_id: "FN03"}
  - {q: "What is the 29.97 Cr other non-current assets; capital advances paid to whom", from_finding_id: "FN03"}
  - {q: "What was the 9.94 Cr FY26 subsidiary revenue booked with no direct cost", from_finding_id: "FN05"}
  - {q: "Wind down or redeploy FZ-LLC and GHV Infra Inc.; decision date", from_finding_id: "FN02"}
  - {q: "Will C notes carry the auditor reliance caveat instead of 'reviewed' (yes/no)", from_finding_id: "FN19"}
  - {q: "ID and Audit Committee independent counts after Seth; Additional IDs regularised at AGM", from_finding_id: "FN17"}
  - {q: "Which entity is the CF 'Partnership Firm' (0.22 Cr); correct H1 adjustment", from_finding_id: "FN21"}
  - {q: "Who are RKS and TCIPL; is either a related party (yes/no)", from_finding_id: "FN23"}
  - {q: "Why H1 FY26 CFO included 44.68 Cr borrowings in WC; will FY27 reclassify", from_finding_id: "FN22"}
  - {q: "H1 FY27 BCA royalty and management fee paid to the parent in Rs", from_finding_id: "FN04"}
  - {q: "30-Sep-2026 order book and non-RPT share; CBI matter status", from_finding_id: "6C-reentry"}
monitorables:
  - {item: "Q3 FY27 results: Erisha reassessment, finance cost, ETR, S-vs-C gap", implied_date: "2027-02-14", source_ref: "S note 5 l488; C note 8 l792"}
  - {item: "Erisha outcome disclosure and any provision", implied_date: "undated", source_ref: "S note 5 l489; C note 8 l793"}
  - {item: "Conversion of 21,83,333 pending warrants", implied_date: "NOT FOUND", source_ref: "S note 3 l475; C note 6 l782"}
  - {item: "BIL JV commencement", implied_date: "NOT FOUND", source_ref: "C note 4 l772"}
  - {item: "Musamji reclassification exchange approval", implied_date: "NOT FOUND", source_ref: "S note 4 l476-480"}
  - {item: "New CFO in office; KMP churn watch", implied_date: "2026-10-22 onward", source_ref: "l52-54"}
  - {item: "Board and Audit Committee recomposition after Seth exit", implied_date: "2027-01-22 [INFERENCE, Reg 25(6)]", source_ref: "l60-63; l827"}
  - {item: "FY26 Annual Report Role 6 deep dive: FY26 CFO, RPT, BCA", implied_date: "now (AGM 2026-09-25)", source_ref: "l476"}
  - {item: "FY27 audited results: FY27 CFO (cleanest metric), re-entry (c)", implied_date: "2027-05-30", source_ref: "Step 8C"}
  - {item: "Q1 FY28 results", implied_date: "2027-08-14", source_ref: "Reg 33 calendar [INFERENCE]"}
  - {item: "Rs 213 Cr parent order completion", implied_date: "about 2027-08-22", source_ref: "Notion prior record"}
  - {item: "Possible QIP or preferential raise", implied_date: "NOT FOUND", source_ref: "l127-136 [INFERENCE]"}
flags:
  - "Erisha FZ-LLC contract ended early with legal proceedings; up to 40.52 Cr subsidiary assets unprovided and unreviewed"
  - "H1 FY27 S CFO -244.37 Cr vs PAT 29.64 Cr (-8.24x); cash conversion INDETERMINATE-WITH-DIRECTION (structural lean)"
  - "Gross debt 191.61 to 411.77 Cr in H1; current borrowings 377.90 Cr; net debt/equity 1.91x"
  - "38.5% of Q2 PAT gain from unexplained ETR drop to 16.70%"
  - "C PAT below S PAT in Q1, Q2, H1"
  - "Drafting: warrant count 16,16,667 printed vs 16,66,667 arithmetic; H1 EPS; C note 2 vs auditor para 6; stale CF plug"
  - "New CFO and ID resignation on results day"
  - "Notion record conflict: three CFO changes in 13 months vs first CFO about 2 years"
  - "UAE Rs 2,645 Cr catalyst likely dead; operator ruling 1 pending"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); Role 5 not run (no concall)"
plain_language_brief_included: true
analyst_note: "The quarter reads strong on revenue and weak on everything that converts revenue into owner value. Core PBT grew 37.88% against revenue 63.30%; finance cost doubled and took 37% of operating EBITDA; an unexplained deferred tax credit supplied 38.5% of the PAT gain. Q1 and Q2 single-quarter margins are both distorted by a 13.51 Cr WIP swing, so H1 (12.25%) is the only clean margin, and it sits 540 bps below H2 FY26. The decisive new fact is Erisha: the subsidiary's only named third-party contract ended in a dispute, its assets are management-certified, and the notes defer any loss to an undated outcome. The structural-vs-growth cash call cannot close without the make-up of the 452.14 Cr other financial assets and the related-party share of receivables; both are the separating observations. Nothing here meets any AVOID re-entry condition. The Notion page carries an internal conflict on CFO history that the operator should resolve."
review_path: "runs/ghvinfra-q2fy27/work/review_ghvinfra_q2fy27.md"
```
