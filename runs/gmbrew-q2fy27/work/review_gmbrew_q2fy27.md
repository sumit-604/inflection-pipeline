# A4 ANALYST REVIEW: G M Breweries Ltd (GMBREW), Q2 FY27 results

Agent: A4 analyst | model: claude-opus-5-5 | date: 2026-10-17 | amended: correction loop 1 (2026-10-17), A5 items A5-F1, A5-M1 to A5-M3, A5-M6 to A5-M8, style notes A5-S1 to A5-S7; correction loop 2 (2026-10-17), A5-C1 and style notes A5-S9 to A5-S14; see LOOP 1 and LOOP 2 CHANGE LOGS
Protocol loaded: frameworks/Quarterly_Results_Review_Protocol_v1_4.md (Role 4) only. No concall in the run, so Role 5 is not loaded.
Documents merged: results filing (board outcome dated 08-Oct-2026, standalone and consolidated, half-year BS and CF, RPT annexure, two limited review reports).
Inputs read: A1 structured (R001-R757), A1 fulltext (verbatim checks at l30-l383, l555-l620; loop 1 re-checks at l36-l300, l305-l329, l555-l616; loop 2 re-checks at l82, l128-l167, l196-l225, l248-l257, l388), A2 ledger and block (loop 1 amended, M1-M4), A3 forensics and block (loop 1 amended, FN-01 to FN-14), A5 audit (loop 2: LOOP 1 RE-AUDIT section only), orchestrator Notion copy. Source PDF and inputs/ not opened.
Framing: PRE-THESIS READ. There is no Notion page, no spear line and no companies/GMBREW.md. Every thesis-dependent cell is ND.

Anchor convention. "R###" is the A1 structured row. "l###" is the fulltext line. In the P&L tables the A1 row order is Q2 FY27, Q1 FY27, Q2 FY26, H1 FY27, H1 FY26, FY26 (for example R001 = Q2 FY27, R003 = Q2 FY26). The tables below re-order the columns to the protocol order. "Derived" means simple arithmetic on anchored cells, shown inline. Raw values are Rs Lakhs; derived cells are computed from raw Lakhs and then rounded.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 10 notes / 0 turns / 0 slides. All 10 reviewed. Findings incorporated: [FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08, FN-09, FN-10, FN-11, FN-12, FN-13, FN-14].

- The 10 notes are standalone Notes 1-4 (R704-R707, l114-l117), consolidated Notes 1-4 (R715-R718, l420-l423) and the two balance-sheet Note 5 labels (R724 l126, R728 l432). A2 count test: notes grep 10 = sweep 10. Loops 1 and 2 did not change the notes count.
- A2 accounts for all 757 structured IDs (orphans 0) and 173 table line items. A3 read 757 of 757 (100%) plus M1-M4.
- A2 MISSING_FROM_STRUCTURED M1 (standalone current tax liabilities, l167, blank both dates) is taken as ZERO_STANDING. Loop 1: M3 and M4 (Statement C items 1A and 2A, "Total amount outstanding as on date", l278, l282, blank) are taken as ZERO_STANDING; the debt-free reading rests on item 3 Nil (R603 l285). M2 (consolidated LRR para 2, l568-l574) is read and carried in FN-09.
- Loop 1 carries the rows the first pass did not cite: R279-R282 (twins R341-R344) and R417-R418 (twins R491-R492) in Step 5A and 5D (FN-05, FN-14); R539-R568 and R632-R636, RPT rows 1-6, in Step 5E (FN-12, FN-13); R699 and R746, the company's review-scope statements, in 0D and 5D (FN-10).
- A1 extraction defects carried from A3 Section 6 (loop to A1, not document findings). EX-1: R387/R388 consolidated Total Equities and Liabilities are column-shifted; this review uses Total Assets R359/R360 (l455) for the consolidated footing. EX-2: line references on R727/R731. EX-3: EPS rows labelled "Rs Lakhs" in A1 context; EPS is Rs per share. No value used below depends on a defective row.
- No unreviewed ledger row. Proceeding.

---

## STEP 0. PRE-FLIGHT

### 0A. Notion and Decision Status

| Item | Reading |
|---|---|
| Notion page | NONE. Live search 2026-10-17 in COMPANIES MASTER found no G M Breweries page (orchestrator copy, notion-thesis.md) |
| Decision Status (verified before any framing) | NONE (no Notion page) |
| One-line thesis | ND |
| Four-pillar destination PE | ND |
| Bear / Base / Bull projections | ND |
| Thesis-broken conditions | ND |
| Monitoring checklist | ND |
| Position size, cost basis | ND (not held on record) |
| Devil's Advocate split | ND |
| Spear line | none on record |
| Prior-quarter Questions for Management | ND (none passed), so answer-status tracking is N.A. this quarter |

Protocol 0A says "stop and ask" when no page exists. Under /run-quarterly this becomes a flag and a PRE-THESIS READ. No HOLD/ADD/TRIM/EXIT framing appears anywhere in this review.

### 0B. Unit convention

All P&L, BS and CF figures are in Rs Lakhs (R708 l82, R719 l388, R732 l191, R735 l498; RPT annexure "in lakhs" R738 l248). The balance sheets print no unit label (R724, R728); A3 F11 shows the Other Equity roll-forward ties to P&L PAT in Lakhs, so Lakhs is confirmed. Statement C (default table) is in INR crore (R742 l274). Conversion: Rs Lakhs x 0.01 = Rs Cr. All figures below are Rs Cr.

### 0C. Share count changes

| Item | 31-Mar-2026 | 30-Sep-2026 | Anchor |
|---|---|---|---|
| Equity share capital (Rs Cr) | 22.86 | 22.86 | R300, R299 l153; consolidated R362, R361 l458 |
| Face value | Rs 10 | Rs 10 | R614 l112 |
| Implied shares (capital / Rs 10) | 2.2855 Cr shares | 2.2855 Cr shares | derived |
| EPS basis | Basic & Diluted, one line | Basic & Diluted, one line | R710, R721 |

No split, bonus, rights, ESOP, QIP, FPO or buyback in any note or agenda item (R704-R707; agenda R620, l36-l45). Statement B "Not Applicable" (R743 l272). EPS share-adjusted equals EPS reported in every column. A3 F10: EPS-implied share count is 0.03-0.05% below the capital-implied count in every column including audited FY26, so the gap is structural, not dilution.

### 0D. Notes extraction (every numbered note)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 (R704 l114; cons. R715 l420) | Approval | Results reviewed by the audit committee and taken on record by the Board on 08-Oct-2026. | 0.00 | Q2 FY27 | None on numbers. Sequencing conflict with LRR signature stamps and both LRR para 2s (FN-09). |
| 2 (R705 l115; cons. R716 l421) | Tax provision | "Provision for taxation includes provision for current tax." | 0.00 stated | All interim columns | Deferred tax is not computed at interim: DTL flat at 0.84 Cr (R305/R306 l158). Interim ETR 25.16-25.18% vs FY26 23.66% (FN-04). Year-end true-up risk to comparability. |
| 3 (R706 l116; cons. R717 l422) | Segment | "The company's operation at present is confined to only one segment namely Country Liquor." | 0.00 | All | No segment table. "At present" wording, investment property 216.72 Cr and the funded subsidiary (FN-03, FN-06) mark a possible future second segment. |
| 4 (R707 l117; cons. R718 l423) | Regrouping | Prior-period figures regrouped "wherever necessary". | ND (not quantified) | Comparatives | Regrouped lines are not named. Comparatives are taken as printed; a regrouping that moved cost lines would distort the other-expenditure YoY (Step 2). Flag only. |
| 5 (R724 l126) | Standalone balance sheet | Half-year statement of assets and liabilities, 30-Sep-2026 vs 31-Mar-2026. | n.a. | 30-Sep-2026 | No unit label. The company says it was reviewed; the auditor's LRR does not name it (FN-10). |
| 5 (R728 l432) | Consolidated balance sheet | Same, consolidated. | n.a. | 30-Sep-2026 | Consolidated assets and OCL gross up by 1.01 Cr vs standalone (FN-02). |
| Unnumbered: revenue footnote (R701 l88; R712 l394) | Revenue basis | Sales are "inclusive of Excise Duty & VAT". | 1,250.42 H1 FY27 excise in revenue (R058) | All | Gross revenue overstates economic revenue about 4x. This review computes margins on gross AND on net revenue. |
| Unnumbered: OCI line (R711 l110; R722 l416) | Equity fair-value OCI | Line printed, nil in all six columns including audited FY26. | 0.00 | All | FN-01: 659.64 Cr investment book with no fair-value movement booked at interim. |
| Unnumbered: CF indirect taxes (R733 l198; R736 l505) | CF presentation | Indirect taxes added back and deducted, both 1,250.42 Cr. | net 0.00 | H1 FY27 | CFO is unaffected; the CF pre-WC profit line is inflated by excise. |
| Unnumbered: RPT loan columns blank (R741 l250) | RPT disclosure | Loan/ICD columns blank for all rows, including the Buildfort loan (row 10). | 1.01 (R585) | H1 FY27 | Purpose, rate, tenure of the subsidiary loan not disclosed (FN-02, FN-03). |
| Unnumbered: RPT rows 1-6 (R539-R568, R632-R636 l250-l255) | KMP pay and CMD lease | KMP remuneration 2.02 Cr and CMD lease rentals 1.49 Cr in H1, each 50% of its annual approval (row 4 is 50.02% on rounding, l253). | 3.51 H1 combined | H1 FY27 | No right-of-use asset or lease liability on either balance sheet (FN-12). KMP pay within approval; CMD rent above CMD pay (FN-13). See Step 5E. |
| Unnumbered: Statement C (R601-R603 l279-l285; ledger M3, M4 l278, l282) | Indebtedness | Default amounts and total financial indebtedness Nil; items 1A and 2A "Total amount outstanding" blank. | 0.00 | 30-Sep-2026 | Debt-free confirmed on item 3 Nil and a balance sheet with no borrowings line. |

Per-note answers. Note 2 changes the reading of the FY comparison: interim ETR is not comparable with the audited FY ETR. Note 3 discloses information that changes a thesis-level assumption (business may not stay single-segment). Note 4 cannot be normalised because no amount is given. No note discloses a one-off; the exceptional line is nil in all columns (R091-R096 l104). No note requires normalising the prior or current period.

Auditor opinion check. Limited review (SRE 2410, R750 l327), conclusion unmodified (R752 l352; consolidated R755-R756 l601). No Emphasis of Matter, Other Matter or Going Concern language (A3 F5, including consolidated para 2, ledger M2). Auditor: V. P. Mehta & Co, sole proprietor Vipul P. Mehta (R640, R641 l373). AMBER items, not modifications:
- (a) Review scope (FN-10, revised in loop 1, wording tightened in loop 2). The auditor's titles and para 1 name the "Quarter ended September 30, 2026" only (l311, l313-l314, l559, l561-l564). The company states twice that the reviews cover the quarter and the half year: the cover letter (l43-l45, R699) and Statement E (l295-l298, R746). Para 1 quotes the attached statement's title as quarter-only, but the standalone title reads "for the quarter / Half year ended September 30, 2026" (l82). The consolidated title also reads quarter / half year, but it prints "September 30, 2025" (l388, FN-11). Two causes fit [INFERENCE]: a truncated quote, or a template carried over from a quarter-only report. The template reading also fits the four quarter-only repeats (l310-l311, l313-l314, l558-l559, l561-l564) and the para 5 "standalone" slip (l603). Under either cause the wording is a drafting defect, not a stated scope limit. The auditor's own wording still governs assurance: the H1 balance sheet and cash flow are review CLAIMED BY THE COMPANY, NOT CONFIRMED BY THE AUDITOR.
- (b) Consolidated para 5 concludes on the "standalone" statement (l603, FN-11).
- (c) Digital signatures 10:27:50-10:28:32 IST precede the 11:30 board start by 61-62 minutes (l368, l590, l614, l46). Para 2 of both LRRs says the statement "has been approved by the Board of Directors" (l319-l320, l568-l569) before the board met (FN-09).

### 0E. Business type

Standard operating business (country liquor manufacturer, single segment, R624). Steps 1 and 5 apply; lender variants skipped.

Checkpoint: Notion fetched (no page, status NONE), units Lakhs to Cr, no share-count change, all 10 notes extracted, auditor conclusion unmodified with three AMBER items, business type standard.

---

## STEP 1. DATA EXTRACTION TABLE (Rs Cr)

### 1A. Standalone P&L

| Line item | Anchor | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations (gross, incl. excise & VAT) | R013-R018 l90 (sales R001-R006 l88) | 717.85 | 802.90 | 860.62 | 1,355.86 | 1,663.52 | 2,976.57 | ND |
| Other operating revenue | R007-R012 l89 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ND |
| Other Income | R019-R024 l91 | 3.03 | 5.55 | 4.14 | 8.16 | 9.69 | 30.24 | ND |
| Total Income | R025-R030 l92 | 720.88 | 808.45 | 864.76 | 1,364.02 | 1,673.21 | 3,006.81 | ND |
| Cost of Materials Consumed | R031-R036 l94 | 124.28 | 138.25 | 146.56 | 245.39 | 284.81 | 511.82 | ND |
| Purchase of stock in trade | R037-R042 l95 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ND |
| Change in Inventories | R043-R048 l96 | 0.17 | (1.18) | 0.78 | (0.41) | (0.40) | 1.68 | ND |
| Employee Benefits Expense | R049-R054 l97 | 3.12 | 2.95 | 3.00 | 5.89 | 5.95 | 12.61 | ND |
| Excise duty, VAT & TCS | R055-R060 l98 | 537.33 | 603.32 | 647.10 | 1,012.48 | 1,250.42 | 2,228.72 | ND |
| Finance Costs | R061-R066 l99 | 0.01 | 0.07 | 0.04 | 0.28 | 0.11 | 0.32 | ND |
| Depreciation | R067-R072 l100 | 1.20 | 1.50 | 1.50 | 2.40 | 3.00 | 5.19 | ND |
| Other Expenses | R073-R078 l101 | 8.14 | 13.11 | 13.27 | 16.80 | 26.38 | 41.03 | ND |
| Total Expenses | R079-R084 l102 | 674.25 | 758.02 | 812.25 | 1,282.83 | 1,570.27 | 2,801.37 | ND |
| Exceptional item | R091-R096 l104 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ND |
| Profit Before Tax | R097-R102 l105 | 46.63 | 50.43 | 52.51 | 81.19 | 102.94 | 205.44 | ND |
| Tax Expense | R103-R108 l106 | 11.74 | 12.69 | 13.22 | 20.44 | 25.91 | 48.61 | ND |
| PAT | R109-R114 l107 | 34.89 | 37.74 | 39.29 | 60.75 | 77.03 | 156.83 | ND |
| OCI (equity FV, net of tax) | R115-R120 l110 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ND |
| Total Comprehensive Income | R121-R126 l111 | 34.89 | 37.74 | 39.29 | 60.75 | 77.03 | 156.83 | ND |
| EPS reported (Rs) | R127-R132 l112 | 15.27 | 16.52 | 17.20 | 26.59 | 33.72 | 68.64 | ND |
| EPS share-adjusted (Rs) | R127-R132 (no share change, 0C) | 15.27 | 16.52 | 17.20 | 26.59 | 33.72 | 68.64 | ND |
| Net revenue (gross less excise, VAT & TCS) | derived R013-R018 less R055-R060 | 180.52 | 199.58 | 213.52 | 343.38 | 413.10 | 747.85 | ND |

FY27 is ND: the year is not complete. A3 cast every total in all 12 columns; all tie (A3 Section 1).

### 1B. Consolidated P&L (Holding plus Buildfort Infradev Pvt Ltd, R644-R646)

| Line item | Anchor | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations (gross) | R145-R150 l396 | 717.85 | 802.90 | 860.62 | 1,355.86 | 1,663.52 | 2,976.57 | ND |
| Other Income | R151-R156 l397 | 3.03 | 5.55 | 4.14 | 8.16 | 9.69 | 30.24 | ND |
| Total Income | R157-R162 l398 | 720.88 | 808.45 | 864.76 | 1,364.02 | 1,673.21 | 3,006.81 | ND |
| Cost of Materials Consumed | R163-R168 l400 | 124.28 | 138.25 | 146.56 | 245.39 | 284.81 | 511.82 | ND |
| Change in Inventories | R175-R180 l402 | 0.17 | (1.18) | 0.78 | (0.41) | (0.40) | 1.68 | ND |
| Employee Benefits Expense | R181-R186 l403 | 3.12 | 2.95 | 3.00 | 5.89 | 5.95 | 12.61 | ND |
| Excise duty, VAT & TCS | R187-R192 l404 | 537.33 | 603.32 | 647.10 | 1,012.48 | 1,250.42 | 2,228.72 | ND |
| Finance Costs | R193-R198 l405 | 0.01 | 0.07 | 0.04 | 0.28 | 0.11 | 0.32 | ND |
| Depreciation | R199-R204 l406 | 1.20 | 1.50 | 1.50 | 2.40 | 3.00 | 5.19 | ND |
| Other Expenses | R205-R210 l407 | 8.14 | 13.11 | 13.27 | 16.80 | 26.38 | 41.03 | ND |
| Total Expenses | R211-R216 l408 | 674.25 | 758.02 | 812.25 | 1,282.83 | 1,570.27 | 2,801.37 | ND |
| Exceptional item | R223-R228 l410 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ND |
| Profit Before Tax | R229-R234 l411 | 46.63 | 50.43 | 52.51 | 81.19 | 102.94 | 205.44 | ND |
| Tax Expense | R235-R240 l412 | 11.74 | 12.69 | 13.22 | 20.44 | 25.91 | 48.61 | ND |
| PAT | R241-R246 l413 | 34.89 | 37.74 | 39.29 | 60.75 | 77.03 | 156.83 | ND |
| EPS reported / share-adjusted (Rs) | R259-R264 l418 | 15.27 | 16.52 | 17.20 | 26.59 | 33.72 | 68.64 | ND |

All 22 consolidated P&L lines equal the standalone lines cell for cell at whole-Lakh rounding (A2 flag 7). The consolidated title prints "September 30, 2025" while columns read 30.09.2026 (R667, R723 l388; FN-11).

### 1C. Derived metrics (standalone; consolidated identical)

| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 44.81 | 46.45 | 49.91 | 75.71 | 96.36 | 180.71 | ND |
| Op EBITDA margin on gross revenue | Op EBITDA / R013-R018 | 6.24% | 5.79% | 5.80% | 5.58% | 5.79% | 6.07% | ND |
| Op EBITDA margin on net revenue | Op EBITDA / net revenue | 24.82% | 23.27% | 23.37% | 22.05% | 23.33% | 24.16% | ND |
| Reported EBITDA | PBT + D + FC | 47.84 | 52.00 | 54.05 | 83.87 | 106.05 | 210.95 | ND |
| Reported EBITDA margin on net revenue | Rep EBITDA / net revenue | 26.50% | 26.05% | 25.31% | 24.42% | 25.67% | 28.21% | ND |
| Core PBT (ex-Other Income) | PBT - OI | 43.60 | 44.88 | 48.37 | 73.03 | 93.25 | 175.20 | ND |
| Other Income / PBT | OI / PBT | 6.50% | 11.01% | 7.88% | 10.05% | 9.41% | 14.72% | ND |
| Effective Tax Rate | Tax / PBT | 25.18% | 25.16% | 25.18% | 25.18% | 25.17% | 23.66% | ND |
| PAT margin on gross revenue | PAT / R013-R018 | 4.86% | 4.70% | 4.57% | 4.48% | 4.63% | 5.27% | ND |
| PAT margin on net revenue | PAT / net revenue | 19.33% | 18.91% | 18.40% | 17.69% | 18.65% | 20.97% | ND |
| Gross margin on net revenue | (net rev - CoM - chg inv) / net rev | 31.06% | 31.32% | 30.99% | 28.66% | 31.15% | 31.34% | ND |
| CoM / net revenue | R031-R036 / net rev | 68.85% | 69.27% | 68.64% | 71.46% | 68.94% | 68.44% | ND |
| Other expenses / net revenue | R073-R078 / net rev | 4.51% | 6.57% | 6.21% | 4.89% | 6.39% | 5.49% | ND |
| Excise intensity | R055-R060 / R013-R018 | 74.85% | 75.14% | 75.19% | 74.67% | 75.17% | 74.88% | ND |

Why net revenue. Revenue is printed gross of excise and VAT (R701). Excise is about 75% of gross revenue in every column. A margin on gross revenue mostly measures the excise rate, not the business. Analysis anchors to the net-revenue margin; the protocol-formula gross margin is kept for completeness. The derived Q1 FY26 and H2 FY26 gross margins (25.99% and 33.61%) are in Step 3.

Checkpoint: every cell filled or ND.

---

## STEP 2. Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26, standalone; consolidated identical)

| Metric | Q2 FY26 | Q2 FY27 | YoY % change | Verdict |
|---|---|---|---|---|
| Revenue from Operations (gross) | 717.85 (R015) | 860.62 (R013) | +19.89% | Growth |
| Net revenue (ex excise, VAT, TCS) | 180.52 | 213.52 | +18.28% | Growth, 161 bps slower than gross |
| Operating EBITDA | 44.81 | 49.91 | +11.38% | Growth below revenue |
| Op EBITDA margin, net revenue (pp) | 24.82% | 23.37% | -145 bps | Compression |
| Op EBITDA margin, gross revenue (pp) | 6.24% | 5.80% | -44 bps | Compression |
| Depreciation | 1.20 (R069) | 1.50 (R067) | +25.00% | Faster than revenue; immaterial in size |
| Finance Costs | 0.01 (R063) | 0.04 (R061) | +300% | Immaterial (debt nil, R603) |
| EBIT (operating) = Op EBITDA - D | 43.61 | 48.41 | +11.01% | Growth below revenue |
| Other Income | 3.03 (R021) | 4.14 (R019) | +36.63% | Rising, small in Q2 |
| **Core Operating PBT (PBT - OI)** | 43.60 | 48.37 | +10.94% | Real growth, slower than headline |
| Reported PBT | 46.63 (R099) | 52.51 (R097) | +12.61% | Growth |
| PAT | 34.89 (R111) | 39.29 (R109) | +12.61% | Growth |
| EPS share-adjusted (Rs) | 15.27 (R129) | 17.20 (R127) | +12.64% | Growth |

Half-year cross-check (H1 FY27 vs H1 FY26): net revenue +20.30% (413.10 vs 343.38); Op EBITDA +27.28% (96.36 vs 75.71); net-revenue margin +128 bps (23.33% vs 22.05%); core PBT +27.69% (93.25 vs 73.03); PAT +26.80% (77.03 vs 60.75). The half-year YoY is stronger than the quarter YoY because the derived Q1 FY26 base was weak, and it was weak on gross margin (25.99%, Step 3).

Diagnostic answers.
1. Revenue grew YoY. Gross +19.89%, net +18.28% (Q2 FY27 vs Q2 FY26). There is no company guidance (R647, NO_GUIDANCE) and no base case (Notion ND), so no implied-YoY comparison is possible. Volume and price are not split in the filing.
2. Operating EBITDA margin contracted YoY. Q2 FY27 net-revenue margin of 23.37% vs Q2 FY26 margin of 24.82% = -145 bps change. Sequentially Q1 FY27 to Q2 FY27 it rose from 23.27% to 23.37% (+10 bps). On the gross-revenue basis: 5.80% vs 6.24% = -44 bps YoY.
3. Core operating PBT grew YoY: 48.37 vs 43.60 = +10.94%. Reported PBT grew +12.61%. The headline growth is real; the gap is 167 bps.
4. Gap drivers between core PBT growth (+4.77 Cr) and reported PBT growth (+5.88 Cr): Other Income +1.11 Cr. Finance cost change -0.03 Cr is already inside core PBT. Tax rate change 0.00 (ETR 25.18% both quarters). Exceptional items 0.00. PAT growth equals PBT growth (+12.61%) because ETR was flat.
5. D&A rose +25.00% vs net revenue +18.28%. The absolute step is 0.30 Cr against 49.91 Cr EBITDA, so there is no absorption deficit. Finance cost is 0.04 Cr. CWIP of 48.14 Cr (R269) has not capitalised (FN-08); a capitalisation would raise D&A.
6. Other Income concentration. Q2 OI is 7.88% of PBT. At the FY level OI is lumpy: H2 FY26 OI was 22.08 Cr (FY26 30.24 less H1 8.16; R024, R023), 73.0% of FY26 OI. Q2 is not inflated by treasury timing; H2 is where OI concentrates (FN-01). The filing does not split Q3 and Q4, so a Q4 concentration is INFERENCE.

Margin driver. Gross margin on net revenue was flat (31.06% to 30.99%). Other expenditure rose from 8.14 Cr to 13.27 Cr, +63.02% YoY, taking 1.71 pp (171 bps) of net revenue (4.51% to 6.21%). That is more than the whole 145 bps margin fall; employee-cost leverage (+32 bps) and gross margin (-7 bps) net against it. The filing does not split Other expenditure. One related-party item likely sits inside it: CMD lease rentals of 1.49 Cr in H1 (l255; placement INFERENCE, FN-12, Step 5E). The Q2 FY26 rent is ND, so whether rent moved the +5.13 Cr is unknown. Excise intensity rose 34 bps (74.85% to 75.19%), so net realisation grew slower than gross.

---

## STEP 3. SEQUENTIAL TRAJECTORY

The filing gives Q2 FY26, Q1 FY27, Q2 FY27, H1 FY26, H1 FY27 and FY26. Q1 FY26 = H1 FY26 less Q2 FY26. H2 FY26 = FY26 less H1 FY26. Q3 FY26 and Q4 FY26 cannot be separated.

| Quarter | Net revenue (Rs Cr) | Gross revenue (Rs Cr) | Gross margin on net revenue | Op EBITDA margin (net) | Core PBT (ex-OI) | One-offs flagged | QoQ run-rate (net revenue) |
|---|---|---|---|---|---|---|---|
| Q1 FY26 (derived R005-R003, R059-R057; CoM R035-R033; chg inv R047-R045) | 162.86 | 638.01 | 25.99% (42.33 / 162.86; CoM 121.11 = 74.36% of net revenue; chg inv (0.58)) | 18.97% (30.90 / 162.86) | 29.43 | none disclosed (exceptional nil R095) | ND (Q4 FY25 not in filing) |
| Q2 FY26 | 180.52 | 717.85 | 31.06% | 24.82% | 43.60 | none | +10.84% vs Q1 FY26 |
| Q3 FY26 | ND | ND | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND | ND | ND |
| H2 FY26 total (derived R006-R005, R060-R059; CoM R036-R035; chg inv R048-R047), two quarters | 404.47 (202.24 per quarter) | 1,620.71 | 33.61% (135.95 / 404.47; CoM 266.43; chg inv 2.09) | 25.96% (105.00 / 404.47) | 102.17 (51.09 per quarter) | OI 22.08 Cr, 2.7x H1 FY26 OI 8.16; ETR 22.67% (tax 28.17 on PBT 124.25) | +12.03% avg quarter vs Q2 FY26 |
| Q1 FY27 | 199.58 | 802.90 | 31.32% | 23.27% | 44.88 | none | -1.31% vs H2 FY26 quarterly average |
| Q2 FY27 | 213.52 | 860.62 | 30.99% | 23.37% | 48.37 | none | +6.98% vs Q1 FY27 |

Diagnostics.
- Run-rate trajectory: revenue is stepping up. Q2 FY27 net revenue is the highest of the quarters the filing prints individually; Q3 and Q4 FY26 are not separable, so either could exceed 213.52 Cr. Margin is on a plateau at about 23.3%, below the H2 FY26 level of 25.96% and below Q2 FY26 at 24.82%.
- Distortion: no quarter carries a disclosed one-off. H2 FY26 carries the OI and tax step-up (FN-01, FN-04), which affect PBT and PAT but not Op EBITDA.
- H1 run-rate test: H1 FY27 average quarterly net revenue is 206.55 Cr; Q2 FY27 at 213.52 Cr exceeds it by 3.37%. No new capacity commissioned (CWIP moved +0.74 Cr, R269/R270), so the test is not a commissioning test here.
- Seasonality: H2 FY26 Op EBITDA margin (25.96%) exceeded H1 FY26 (22.05%) by 391 bps. Gross margin rose more over the same split (33.61% vs 28.66%, +496 bps), so the seasonal uplift in the one year visible is a gross-margin effect. The derived Q1 FY26 margin (18.97%) is the low point.
- Gross-margin volatility (loop 1, A5-M7). Inside FY26 the gross margin on net revenue ran 25.99% (Q1, derived), 31.06% (Q2) and 33.61% (H2 average, derived). The Q1 to Q2 swing is 5.07 pp; Q1 to H2 is 7.62 pp. At Q2 FY27 net revenue (213.52 Cr) a 5.07 pp swing is worth about 10.82 Cr a quarter, about 2.1x the 5.13 Cr other-expenditure rise that Step 2 and 8C treat as the key test. On filed history, material cost is the larger margin variable. The last three printed quarters (30.99%-31.32%) are the steadiest stretch visible. The cause of the FY26 swing is ND: the filing gives no input-price, mix or inventory-timing split.
- Implied Q3 FY27 base to keep trajectory: net revenue at or above 213.52 Cr and core PBT at or above 48.37 Cr. To grow H2 YoY, H2 FY27 core PBT must exceed 102.17 Cr (51.09 per quarter), which is above Q2 FY27's 48.37.

---

## STEP 4. OPERATIONAL DECOMPOSITION (PAT bridge, Q2 FY27 vs Q2 FY26)

| Component | YoY change (Rs Cr) | YoY change (% of Q2 FY26 PAT 34.89) | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (net revenue +33.00 x prior gross margin 31.06%) | +10.25 | +29.4% | Recurring |
| Margin change contribution: gross margin (30.99% vs 31.06% on 213.52) | -0.14 | -0.4% | Recurring |
| Margin change contribution: employee cost (3.00 vs 3.12) | +0.12 | +0.3% | Recurring |
| Margin change contribution: other expenditure (13.27 vs 8.14) | -5.13 | -14.7% | Unknown (line not split; Note 4 regrouping unquantified; CMD rent likely inside, FN-12) |
| = Operating EBITDA change (49.91 - 44.81) | +5.10 | +14.6% | |
| D&A change (1.50 vs 1.20) | -0.30 | -0.9% | Recurring (post-capex) |
| Finance cost change (0.04 vs 0.01) | -0.03 | -0.1% | Recurring |
| Other Income change (4.14 vs 3.03) | +1.11 | +3.2% | NON-RECURRING typically |
| = PBT change (52.51 - 46.63) | +5.88 | +16.9% | |
| Tax on PBT change at constant ETR (5.88 x 25.18%) | -1.48 | -4.2% | Mixed |
| Effective tax rate change (25.18% both quarters) | 0.00 | 0.0% | Mixed |
| Exceptional items (R091, R093 nil) | 0.00 | 0.0% | NON-RECURRING |
| **Reported PAT YoY change (39.29 - 34.89)** | **+4.40** | **+12.6%** | |

Mandatory answers.
- Recurring vs non-recurring: core PBT change +4.77 Cr after tax at 25.18% = +3.57 Cr, 81% of the +4.40 Cr PAT change. Other Income after tax = +0.83 Cr, 19%.
- If Other Income reverts to the prior-year level (3.03 Cr), Q2 FY27 PAT = 39.29 - (1.11 x 0.748) = 38.46 Cr, +10.2% YoY.
- D&A and finance cost are at steady state for the current asset base. The steady state changes when the 48.14 Cr CWIP capitalises; date and asset life are not disclosed (FN-08), so the step-up is ND.
- Tax adjustments: none in Q2. Deferred tax is not computed at interim (DTL flat at 0.84 Cr, R305/R306). FY26 shows a year-end shield of 3.10 Cr (ETR 23.66% vs 25.17%). A similar year-end true-up in FY27 would lift FY27 PAT above the interim run-rate; FY26 shows it only at the full-year level, so the Q4 timing is INFERENCE. This is a forward reading, not a credit (FN-04).

H1 bridge cross-check (H1 FY27 vs H1 FY26): PAT +16.28 Cr. Op EBITDA +20.65 Cr; within it, CoM ratio fell from 71.46% to 68.94% of net revenue while other expenditure rose +9.58 Cr. OI +1.53 Cr. The H1 improvement comes from material cost ratio, not from other income. The weak base is the derived Q1 FY26 gross margin of 25.99% (Step 3).

---

## STEP 5. CASH QUALITY AND BALANCE SHEET (H1, Reg 33 half-year statements)

Prior period: H1 FY26 for flows; 31-Mar-2026 for balances (the filing prints no 30-Sep-2025 balance sheet, so Sep-2025 balances are ND).

### 5A. Standalone

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | 40.03 H1 FY26 (R434 l217) | 95.53 H1 FY27 (R433) | +55.50 | Strong as printed, WC-assisted; YoY driver split in 5D |
| CFO / PAT | 0.66x (40.03 / 60.75) | 1.24x (95.53 / 77.03) | +0.58x | Above 1.15x band as printed. Readings span 1.02x-1.29x (5D): 1.06x without the payables stretch; 1.20x on FN-05 reading A; 1.29x on FN-14 reading B, weakly evidenced |
| CFO on FN-05 reading A (tax outflow at BS-consistent 26.32 Cr; provisions rise in operating) | ND (no Mar-2025 BS) | 92.25 (95.53 - 3.32 + 0.04; FN-05) | ND | 1.20x PAT (119.8%) |
| CFO before WC change / PAT (Op EBITDA - direct tax) / PAT | 0.95x ((75.71 - 18.00 R430) / 60.75) | 0.95x ((96.36 - 23.00 R429) / 77.03) | flat | Structural pre-WC conversion ~0.95x |
| Capex: PPE incl. capital advances (CWIP inside) | +0.02 inflow (R436 l220) | 5.34 (R435) | +5.36 | Low; BS-implied additions 2.06 Cr; the 3.28 Cr residual closes against the tax lines (FN-05) |
| Capex: investment property | 6.00 (R438 l221) | 2.25 (R437) | -3.75 | Non-operating |
| FCF (CFO - PPE capex) | 40.05 | 90.19 | +50.14 | Strong in H1; 90.19 on either FN-05 reading |
| FCF after investment property | 34.05 | 87.94 | +53.89 | |
| Treasury investment purchases | 12.58 (R440 l222) | 89.24 (R439) | +76.66 | 93% of H1 CFO deployed to investments (FN-06) |
| Working capital change (cash generated less pre-WC profit) | -17.68 build (1,070.51 - 1,088.19; R428, R408) | +22.17 release (1,368.95 - 1,346.78; R427, R407) | +39.85 | YoY swing is OCFL and payables, not OCA (5D) |
| of which Other Current Assets | +40.13 (R416 l207) | +41.06 (R415) | +0.93 | H1 release in both first halves shown; flat YoY. An H2 rebuild is INFERENCE: no H2 cash flow or Sep-2025 BS is printed |
| of which Other current financial liabilities | -57.86 (R426 l213) | -18.74 (R425) | +39.12 | Smaller H1 outflow; largest YoY driver; content ND (FN-07) |
| of which Trade payables | -0.46 (R420 l210) | +13.71 (R419) | +14.17 | Second YoY driver; payables +123.6% vs Mar (11.10 to 24.80, R312, R311) |
| of which Other non-current financial assets | 0.00 (R414) | -12.74 (R413 l206) | -12.74 | Classified in operating; content ND |
| of which Other non-current assets | -6.70 (R418 l208) | -4.05 (R417) | +2.65 | Built inside CFO in both H1s shown; content ND (FN-14) |
| Receivable days (on net revenue) | 1.09 (2.24 at Mar on FY26 net rev 747.85) | 2.23 (5.06 at Sep on H1 net rev x 2 = 826.20) | +1.14 | Negligible credit (cash-and-carry trade) |
| Inventory days (on CoM) | 24.42 (34.24 on FY26 CoM 511.82) | 21.24 (33.14 on H1 CoM x 2 = 569.62) | -3.18 | Improving |
| Payable days (on CoM) | 7.91 (11.10 on 511.82) | 15.89 (24.80 on 569.62) | +7.98 | Doubled; non-MSME line only (R725); MSME payables line not printed |
| Cash Conversion Cycle | 17.59 | 7.58 | -10.02 | Short; OCA 107.72 Cr and OCL 102.36 Cr dominate true WC and are excluded from CCC |
| PPE | 42.10 (R268 l131) | 40.42 (R267) | -1.68 | |
| CWIP | 47.40 (R270 l132) | 48.14 (R269) | +0.74 | CWIP > net PPE; stalled or pre-commissioning (FN-08) |
| Investment property | 214.47 (R272 l133) | 216.72 (R271) | +2.25 | Non-operating (FN-06) |
| Non-current investments | 570.40 (R276 l136) | 659.64 (R275) | +89.24 | 51.4% of total assets |
| Other non-current financial assets | 106.93 (R278 l137) | 119.67 (R277) | +12.74 | Content ND |
| Non-current tax assets (net) | 0.96 (R280 l138) | 1.37 (R279) | +0.41 | Rose while H1 tax expense exceeded tax paid by 2.91 Cr; closes the FN-05 residual |
| Other non-current assets | 45.72 (R282 l139) | 49.76 (R281) | +4.05 | Larger than net PPE; 3.9% of total assets; content ND (FN-14) |
| Other current assets | 148.77 (R294 l147) | 107.72 (R293) | -41.06 | Content ND (FN-07) |
| Other current liabilities | 97.75 (R316 l165) | 102.36 (R315) | +4.61 | Content ND |
| Other current financial liabilities | 35.59 (R314 l164) | 16.85 (R313) | -18.74 | -52.7% (FN-07) |
| Total financial indebtedness | Nil (R603 l285) | Nil (R603) | 0.00 | Debt-free |
| Net Debt / (Net Cash), cash + other bank only | (12.16) (1.57 R290 + 10.59 R292) | (2.05) (0.83 R289 + 1.22 R291) | +10.11 less cash | Net cash |
| Net cash incl. non-current investments | (582.55) | (661.68) | +79.13 | Treasury-heavy |
| Total equity | 1,078.26 (R304 l155) | 1,136.91 (R303) | +58.64 | OE roll-forward = PAT 77.03 less dividend 18.39 (A3 F11) |
| Dividend paid | 15.62 (R454 l231) | 18.39 (R453) | +2.77 | 23.9% of H1 FY27 PAT |
| Promoter Pledge | ND | ND | ND | Not in filing; Q2 FY27 shareholding pattern due by 21-Oct-2026 |

### 5B. Consolidated

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | 40.03 (R508 l524) | 95.53 (R507: 9,552.91 Lakhs) | +55.50 | Same as standalone (gap -0.0011 Cr) |
| CFO / PAT | 0.66x | 1.24x | +0.58x | Same |
| Capex PPE incl. capital advances | +0.02 inflow (R510) | 5.34 (R509 l527) | +5.36 | Same |
| Investment purchases | 12.58 (R514) | 89.24 (R513 l529) | +76.66 | Same |
| Other non-current assets (BS) | 45.72 (R344 l445) | 49.76 (R343) | +4.05 | Same as standalone; Buildfort holds none (FN-14) |
| Other current assets (BS) | 148.78 (R356 l453) | 108.73 (R355) | -40.05 | +1.01 Cr above standalone (Buildfort advance) |
| Other current liabilities (BS) | 97.75 (R378 l470) | 103.37 (R377) | +5.62 | +1.01 Cr above standalone (FN-02) |
| Cash and cash equivalents | 1.57 (R352 l451) | 0.83 (R351: 83.40 Lakhs) | -0.74 | |
| Total assets | 1,225.42 (R360 l455) | 1,284.73 (R359) | +59.31 | +1.01 Cr above standalone |
| Total equity | 1,078.26 (R366 l460) | 1,136.90 (R365) | +58.64 | -0.0056 Cr vs standalone |
| Net Debt / (Net Cash) | Nil debt; cash + bank (12.16) (R352 + R354) | Nil debt; cash + bank (2.05) (R351 + R353) | | Same |
| Promoter Pledge | ND | ND | ND | |

### 5C. Standalone-vs-consolidated gap (first-class metric; A3 F2)

| Period | Standalone PAT | Consolidated PAT | Gap (Rs Cr) | Gap % of standalone |
|---|---|---|---|---|
| Q2 FY26 | 34.89 (R111) | 34.89 (R243) | 0.00 | 0.00% |
| Q1 FY27 | 37.74 (R110) | 37.74 (R242) | 0.00 | 0.00% |
| Q2 FY27 | 39.29 (R109) | 39.29 (R241) | 0.00 | 0.00% |
| H1 FY26 | 60.75 (R113) | 60.75 (R245) | 0.00 | 0.00% |
| H1 FY27 | 77.03 (R112) | 77.03 (R244) | 0.00 printed; CF PBT gap -0.0042 (R467 102.9398 vs R393 102.9440) | 0.00% printed; -0.005% CF-implied |
| FY26 | 156.83 (R114) | 156.83 (R246) | 0.00 | 0.00% |

Balance-sheet gap at 30-Sep-2026: total assets +1.0061 Cr (R359 vs R297), liabilities +1.0117 Cr (R385 vs R321), all in other current liabilities (R377 vs R315). The consolidated CF OCL change exceeds standalone by 1.0105 Cr (R497 5.62 vs R423 4.61), equal to the RPT loan to Buildfort of 1.01 Cr (R585). Reading A: intercompany advance not eliminated. Reading B: Buildfort raised a matching third-party liability. The RPT closing balance prints 0.00 (R587), which conflicts with an outstanding advance. Size 0.08% of assets; a consolidation-process data point, not a value issue (FN-02). Buildfort itself is a shell with H1 loss of 0.0042 Cr and net worth about 0.0044 Cr (FN-03). Trend: gap 0.00% to 0.005%, no move beyond 5 pp.

### 5D. Mandatory answers

- Pillar 2 cash band. H1 FY27 CFO/PAT of 1.24x as printed sits in the 1.15x band and approaches 1.30x. H1 FY26 was 0.66x (0.65x band). Pre-WC conversion is about 0.95x both years. The swing is working capital, and the YoY split below shows which lines. FY26 full-year CFO is not in this filing (ND). With two H1 readings and no full-year reading, the band cannot be fixed. No valuation band exists to compare (Notion ND).
- YoY CFO driver split (loop 1, A5-M6). H1 FY27 less H1 FY26, standalone CF lines (Rs Cr):

| CF working-capital line | H1 FY26 | H1 FY27 | YoY swing | Anchor |
|---|---|---|---|---|
| Other current financial liabilities | (57.86) | (18.74) | +39.12 | l213, R425/R426 |
| Trade payables | (0.46) | 13.71 | +14.17 | l210, R419/R420 |
| Other current assets | 40.13 | 41.06 | +0.93 | l207, R415/R416 |
| Inventories | (4.54) | 1.09 | +5.63 | l205 |
| Other non-current assets | (6.70) | (4.05) | +2.65 | l208, R417/R418 |
| Other non-current liabilities | 0.00 | 0.05 | +0.05 | l211 |
| Trade receivables | (0.01) | (2.82) | (2.81) | l204 |
| Other current liabilities | 11.75 | 4.61 | (7.14) | l212 |
| Other non-current financial assets | 0.00 | (12.74) | (12.74) | l206, R413/R414 |
| Total working-capital change | (17.68) | 22.17 | +39.85 | l202, l214 (lines sum to 39.86 on rounding) |

  The +39.85 Cr YoY swing comes from two liability lines: a smaller OCFL outflow (+39.12 Cr) and a trade-payables stretch (+14.17 Cr; payable days 7.91 to 15.89). The OCA release that the first pass credited was flat YoY (+0.93 Cr). The other six lines net to -14.36 Cr. The filing discloses the content of neither OCFL nor payables. So the YoY cash improvement is liability timing of undisclosed content, not an asset release.

| CFO reading (H1 FY27) | CFO (Rs Cr) | CFO / PAT | FCF (CFO less PPE line) | Basis |
|---|---|---|---|---|
| As printed | 95.53 | 1.24x | 90.19 | l217, l220 |
| Without the payables stretch (less the 13.71 Cr payables inflow) | 81.82 | 1.06x | 76.48 | l210 |
| FN-05 reading A (tax outflow understated 3.32 Cr; capex overstated 3.28 Cr) | 92.25 | 1.20x (119.8%) | 90.19 | FN-05; l215, l138, l166 |
| FN-05 reading A and without the payables stretch | 78.54 | 1.02x | 76.48 | derived |
| FN-14 reading B (other non-current assets are capital advances) | 99.58 | 1.29x | 90.19 | FN-14; l208. Weakly evidenced: the capex line already reads "including Capital Advances" (l219-l220) |

  Reconciliation and evidence rank (loop 2, A5-C1). Reading A moves 3.28 Cr between CFO and capex, so FCF of 90.19 Cr is unchanged and CFO falls to 92.25 Cr. The payables test removes 13.71 Cr from both CFO and FCF. The two stack: 78.54 Cr, 1.02x. FN-14 reading B moves CFO the other way, to 99.58 Cr, 1.29x, also without changing FCF. So the readings span 1.02x-1.29x around the 1.24x print. Each reading takes the same evidence bar, bull side and bear side alike:
  - FN-05 reading A (bear side, 1.20x): supported. The tax-side and capex-side residuals tie to within 0.10 Lakh on filed lines (tax and capex bullet below). The cause of the slip is ND.
  - Payables test (bear side, 1.06x): a timing sensitivity, not an accounting reading. The 13.71 Cr inflow is filed (l210). The test asks only how CFO looks if it reverses. Its content is ND (FN-07).
  - FN-14 reading B (bull side, 1.29x): weakly evidenced. The CF capex line already reads "including Capital Advances" (l219-l220), so capital advances have a filed home in investing. Reading B needs a second home for the same item inside operating cash flow, and no filed line shows one. The FY26 AR other non-current assets note (M2) separates it from the deposit reading.
  On every reading CFO is at or above PAT. The structural anchor stays pre-WC conversion of about 0.95x.
- WC drag test ("if growth stopped, would WC days stay high?"). Receivables (2.23 days) and inventory (21.24 days) are small. The large items are OCA (107.72 Cr), OCL (102.36 Cr), OCFL (16.85 Cr) and other non-current assets (49.76 Cr), whose content is not disclosed. OCA released cash in both first halves shown (40.13 and 41.06 Cr, l207). An H2 rebuild is INFERENCE: the filing prints no H2 cash flow and no Sep-2025 balance sheet. No rating agency commentary is in the corpus. Classification: INDETERMINATE-WITH-DIRECTION. Direction positive (pre-WC conversion ~0.95x, near-zero receivables, debt nil). Missing evidence: FY26 full-year CFO, OCA, OCFL, payables and other non-current asset composition, and the H2 FY27 cash flow. Per house rule this caps the verdict at PROCEED WITH CAVEATS or below.
- Tax and capex residual (FN-05, revised in loop 1, wording in loop 2). H1 tax expense is 25.91 Cr (R103-R108 l106). Direct tax paid is a round 23.00 Cr (R429 l215), a gap of 2.91 Cr. The current tax liability is blank (M1 l167). The non-current tax asset rose 0.41 Cr (0.96 to 1.37, R279/R280 l138) instead of falling. So the tax lines carry 3.32 Cr that no CF line explains. The capex line shows 5.34 Cr (R435 l220) against BS-implied additions of 2.06 Cr, a residual of 3.28 Cr; the provisions rise of 0.04 Cr (l166) has no CF line. Tax side 2.91 + 0.41 = 3.32 Cr; capex side 3.28 + 0.04 = 3.32 Cr. In raw Lakhs the sides are 332.08 and 332.18, so the offset closes to within 0.10 Lakh (l106, l215, l138; l131-l134, l100, l220, l166). The 0.10 Lakh equals the fall in intangible assets (4.10 to 4.00 Lakh, l134). The plug sits between the CF tax line and the capex line. Reading A (most evidenced): tax outflow understated, capex overstated; CFO 92.25 Cr, capex 2.06 Cr. Reading B: CFO and capex as printed; the provision is unbooked and a non-tax item sits in the tax asset, so current liabilities are understated. FCF is 90.19 Cr on either reading. Size: 3.4% of H1 CFO.
- CWIP capitalisation. No capitalisation in H1: CWIP +0.74 Cr, PPE -1.68 Cr (depreciation 3.00 Cr exceeds additions). No projected commissioning exists to test (no guidance, R647).
- Net debt vs projection. Debt is nil (R603). No projection (Notion ND). Cash and bank fell 10.11 Cr as FDs (9.37 Cr, R441) and CFO were moved into non-current investments (89.24 Cr).
- Review status caveat (FN-10, revised in loop 1). The company states that the limited reviews cover the quarter and half year (l43-l45 R699; l295-l298 R746). The LRRs name the quarter only (l311, l559), while misquoting the attached statement's quarter/half-year title (standalone l82; the consolidated title at l388 prints "September 30, 2025", FN-11). The auditor's wording governs. The H1 balance sheet and cash flow used in this step are review CLAIMED BY THE COMPANY, NOT CONFIRMED BY THE AUDITOR. Severity is lower than the first pass stated; the caveat stands.

### 5E. Related-party and governance lines (loop 1, A5-M1; FN-12, FN-13)

| RPT row | Counterparty | Type | Annual value approved (Rs Cr) | H1 FY27 transacted (Rs Cr) | H1 / approved | Anchor |
|---|---|---|---|---|---|---|
| 1 | Jimmy Almeida Kashyap, CMD | Remuneration | 1.80 | 0.90 | 50% | l250, R539-R543 |
| 2 | Jyoti Almeida Kashyap, ED | Remuneration | 1.32 | 0.66 | 50% | l251, R544-R548 |
| 3 | Kiran Parashare, ED | Remuneration | 0.36 | 0.18 | 50% | l252, R549-R553 |
| 4 | S Swaminathan, CFO | Remuneration | 0.3025 | 0.1513 | 50.02% | l253, R554-R558 |
| 5 | Sandeep Kutchhi, VP Finance & CS | Remuneration | 0.2554 | 0.1277 | 50% | l254, R559-R563 |
| 1-5 | KMP total | Remuneration | 4.0379 | 2.0190 | 50% | derived |
| 6 | Jimmy Almeida Kashyap, CMD | Lease rentals | 2.9774 | 1.4887 | 50% | l255, R564-R568 |
| 7 | Jimmy Almeida Kashyap, CMD | Dividend | 12.6992 | 12.6992 | 100% | l256, R569-R573 |

All ten rows show "Approved"; none was ratified later (ft l249-l259). Opening and closing balances are 0.00 on rows 1-7, so no security deposit or rent payable is disclosed.

- KMP pay (FN-13, NEUTRAL-FACT). 2.02 Cr in H1, 50% of approval on every row (row 4 is 50.02% on rounding, 15.13 / 30.25 Lakh, l253), so pay is fixed with no visible variable element and no excess. It equals 33.9% of H1 employee benefits (5.95 Cr, l97 R052); whether that line includes it is ND. It is 2.6% of H1 PAT.
- CMD lease (FN-12, AMBIGUOUS). Rent of 1.49 Cr in H1 is exactly half the 2.98 Cr approved, so the approval is an annual rent. Neither balance sheet prints a right-of-use asset or a lease liability (l131-l170). Non-current liabilities total 1.18 Cr (l160, R309), H1 finance cost is 0.11 Cr (l99, R064), and the financing section shows only interest and dividend (l229-l232). So the rent runs through operating cost, most likely other expenditure [INFERENCE], where it would be 5.6% of H1 other expenditure (26.38 Cr, l101). Reading A: a short-term lease under the Ind AS 116 exemption; accounting correct, but a related-party rent that resets each year, subject to audit-committee approval (l255 "Approved"). Reading B: a multi-year lease without Ind AS 116; lease liability understated (amount NOT FOUND) and reported EBITDA lower than Ind AS 116 EBITDA by the rent (1.5% of H1 Op EBITDA). The separating observation is the FY26 AR Ind AS 116 note.
- Governance line. The CMD received more as the company's landlord (1.49 Cr) than as its managing director (0.90 Cr). Rent is 62% of his 2.39 Cr non-dividend H1 receipts. With his 12.70 Cr dividend his H1 receipts total 15.09 Cr. Nothing exceeds approval. The fact feeds the promoter value-capture tally at the AR and the Pillar 3 read in /fttcp.

Checkpoint complete.

---

## STEP 5.5. DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull

Tracker rows not supplied by the orchestrator, and no Notion company page exists to relate them to.

| Signal Name | Type | Cadence | Latest Observation Date & Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied) | ND | ND | ND | ND | ND | ND |

Flag: fewer than three signals (zero). Role 5.5 has never been run for this name. The quarterly review is the checkpoint to open Role 5.5 if the operator takes the name into coverage.

### 5.5B. Reconciliation

Target reported: strong on revenue (+18.28% net YoY), mixed on margin (-145 bps YoY). Signals said: ND. No four-outcome cell can be assigned. Outcome: NOT RECONCILABLE.

### 5.5C. New signal candidates (payload rows only; written only through the run's operator-approval gate; none written by A4)

No new signals written this quarter. Candidate dependencies surfaced by the filing, for Role 5.5 Case B create-new if the name enters coverage:

| Candidate signal | Why (filed evidence) | Case | Status |
|---|---|---|---|
| State excise duty / country liquor MRP regime (state of operation: factory at Virar, Palghar, R631) | Single segment country liquor (R706); excise intensity 74.85% to 75.19% YoY (R057, R003; R055, R001) | B (create new) | PENDING operator approval; cannot relate to a company page that does not exist |
| Rectified spirit / molasses / grain alcohol input price | CoM 68.64% of net revenue Q2 FY27 (R031) is the dominant cost; FY26 gross margin ran 25.99% to 33.61% (Step 3) | B | PENDING operator approval |

### 5.5D. Forward-view weighting

No signals exist, so Step 6 rests on the single-quarter print and two half-year cash readings. A single quarter is one data point; no weighting toward signals is possible.

---

## STEP 6. RECONCILIATION VS THESIS (PRE-THESIS READ)

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual | Lands In |
|---|---|---|---|---|---|
| Revenue (Q2 FY27 net) | ND | ND | ND | 213.52 (derived R013, R055) | ND (no projections) |
| Revenue (H1 FY27 net) | ND | ND | ND | 413.10 (derived R016, R058) | ND |
| Op EBITDA margin (net revenue, Q2) | ND | ND | ND | 23.37% | ND |
| PAT (Q2 FY27) | ND | ND | ND | 39.29 (R109) | ND |
| EPS (Q2 FY27, Rs) | ND | ND | ND | 17.20 (R127) | ND |
| Net Debt | ND | ND | ND | Nil debt (R603); net cash 2.05 ex investments | ND |
| ROCE | ND | ND | ND | ND (recompute deferred to /fttcp; see pillar flags) | ND |

Probability re-weighting rule: not applicable (no projections, no prior quarter on record). State: no counter started.

### 6B. Watchlist items

No Notion monitoring checklist exists.

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| ND | No checklist on record | ND | ND | ND | UNKNOWN |

Proposed seed items for a future checklist (A4 proposal from this quarter's findings, not Notion; thresholds anchored to this filing):

| # | Proposed item | Proposed green | Proposed red | This quarter reading |
|---|---|---|---|---|
| P1 | Op EBITDA margin on net revenue | >= 24.82% (Q2 FY26 level) | < 23.27% (Q1 FY27 level) | 23.37% |
| P2 | Other expenses / net revenue | <= 4.51% (Q2 FY26) | >= 6.57% (Q1 FY27) | 6.21% |
| P3 | Non-operating assets (investments + investment property) / total assets | stable or falling from 68.3% | rising above 68.3% | 68.3% (876.36 / 1,283.73) |
| P4 | Half-year CFO / PAT | >= 1.00x | < 0.65x | 1.24x H1 FY27 (readings 1.02x-1.29x, 5D; 1.06x without the payables stretch; the 1.29x high end is weakly evidenced) |
| P5 | Buildfort Infradev funding (RPT row) | no further funding, or a disclosed plan | further funding with no disclosed purpose | 1.01 Cr, purpose blank (R585, R741) |

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| ND (no conditions on record) | ND | ND | N.A. |

No condition exists, so none can fire. No exit or AVOID recommendation follows from 6C.

### 6D. Growth trigger status

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| ND (no triggers on record) | ND | ND | ND | N.A. |

---

## STEP 6.5. EXPECTATION LEDGER AND A21 BASE REFRESH: DEFERRED TO /fttcp AND ROLE 1 (OR-30)

No expectation ledger exists for this name. The A21 refresh is deferred. Facts that the refresh will need, flagged here:

| Fact | Value | Anchor / derivation | Pillar / input touched |
|---|---|---|---|
| Q2 FY27 PAT annualised | 157.16 Cr | 39.29 x 4 (R109) | A21 single-quarter base |
| Trailing-4Q PAT | 173.11 Cr | FY26 156.83 - H1 FY26 60.75 + H1 FY27 77.03 (R114, R113, R112) | A21 trailing base (recommended: OI and tax are seasonal, H2-loaded) |
| Trailing-4Q EPS | Rs 75.77 | 68.64 - 26.59 + 33.72 (R132, R131, R130) | A21 base |
| Trailing-4Q net revenue | 817.57 Cr | 747.85 - 343.38 + 413.10 | A21 base |
| Trailing-4Q Op EBITDA | 201.36 Cr | 180.71 - 75.71 + 96.36 | A21 base |
| Trailing-4Q Other Income | 31.77 Cr | 30.24 - 8.16 + 9.69 (R024, R023, R022) | one-off / treasury adjustment to the base |
| Year-end tax shield FY26 | 3.10 Cr | FY26 tax at 25.17% vs actual (FN-04) | base PAT normalisation |
| Seasonality | H2 FY26 Op EBITDA margin 25.96% vs H1 FY26 22.05%; gross margin 33.61% vs 28.66% | Step 3 | trailing-4Q base, not single-quarter |

## STEP 7. FOUR-PILLAR RE-VALIDATION: DEFERRED TO /fttcp AND ROLE 1 (OR-30)

No destination PE exists (Notion ND). No pillar is recomputed here. Pillar-relevant facts, flagged:

| Pillar / input | Fact this quarter | Anchor | Note for /fttcp |
|---|---|---|---|
| ROCE base (Pillar 1) | ROE H1 annualised 13.9% (77.03 x 2 / average equity 1,107.59) | R112, R303, R304 | Treasury drags ROE: the non-operating book (951.01 Cr average, 7A) earns a recognised 3.34% pre-tax. 68.3% of assets are non-operating. FTTCP must declare an operating vs whole-company basis. |
| ROCE base (Pillar 1) | Operating capital is small: PPE 40.42 + CWIP 48.14 + inventory 33.14 + receivables 5.06 Cr. Beside it sit other non-current assets 49.76 Cr and other NC financial assets 119.67 Cr, content ND | R267, R269, R285, R287, R281, R277 | An operating ROCE will be very high; OCA, OCL, other NC financial assets and other non-current assets (49.76 Cr, larger than net PPE, FN-14) must be known first. INFERENCE. |
| Cash multiplier (Pillar 2) | H1 CFO/PAT 1.24x printed; readings span 1.02x-1.29x (1.06x without the payables stretch; 1.20x on FN-05 reading A; 1.29x on FN-14 reading B, weakly evidenced); H1 FY26 0.66x; pre-WC ~0.95x | R433, R434; 5D | INDETERMINATE-WITH-DIRECTION; full-year CFO ND |
| Margin durability (Pillar 1 input) | FY26 gross margin 25.99% (Q1) to 33.61% (H2 average); last three printed quarters 30.99%-31.32% | Step 3 | Material cost is the larger margin variable on filed history; cause ND |
| Growth visibility premium | No guidance, no concall, no capacity data; CWIP 48.14 Cr undisclosed project | R647, R269 | Visibility is low on filed evidence |
| Strategic premium | Single-segment country liquor, licence-regulated market (INFERENCE); no moat data in filing | R706 | Licence/scarcity archetype candidate; evidence ND |
| Promoter governance (Pillar 3 input) | CMD lease rentals 1.49 Cr H1 with no lease liability; CMD rent above CMD pay (0.90 Cr) | l250, l255; 5E | FN-12 readings decide whether the related-party rent is a yearly reset or an unrecognised liability |
| UA multiplier | Institutional ownership ND | not in filing | Qualifiers unevidenced |
| Sector cap | "At present" single segment; investment property 216.72 Cr; funded real-estate-named subsidiary | R706, R271, R585 | Possible SOTP / holding-structure question before a single-sector cap applies |
| Hurdle ratio | CMP and current PE ND | not passed | Cannot be computed |

### 7A. Treasury recognised yield (loop 1, A5-M8; feeds FN-06, FN-01)

| Item | Value | Anchor |
|---|---|---|
| Non-operating book, 31-Mar-2026: investment property + NC investments + other NC financial assets + cash + other bank | 903.96 Cr (214.47 + 570.40 + 106.93 + 1.57 + 10.59) | l133, l136, l137, l145, l146 |
| Non-operating book, 30-Sep-2026 | 998.07 Cr (216.72 + 659.64 + 119.67 + 0.83 + 1.22; components rounded) | same lines |
| Average book | 951.01 Cr | derived |
| TTM other income | 31.77 Cr (30.24 - 8.16 + 9.69) | l91 |
| Recognised pre-tax yield on the average book | 3.34% | derived |
| Post-tax at the 25.17% interim ETR | 2.50% (23.77 Cr; book about 40x recognised post-tax earnings) | derived, l105, l106 |
| Average NC investments alone | 615.02 Cr | l136 |
| Recognised pre-tax yield if all OI is attributed to investments | 5.17% (upper bound) | derived |
| H1 FY27 OI composition | interest 4.87 + dividend 0.38 + other non-operating 4.44 = 9.69 Cr, all cash items | l199-l201, l225-l227 |
| Fair-value gain recognised in H1 | 0.00 (OCI line nil, l110; investments rose exactly by the 89.24 Cr cash spent, l136, l222) | FN-01 |

Notes. Other NC financial assets sit in operating CF and their content is ND; dropping them from the book raises the yield toward the 5.17% bound. Investment-property rent sits inside other non-operating income (FN-06), so the 3.34% includes it. Dividends are 0.38 Cr on a 659.64 Cr book. Bear reading: unless unrecognised gains exist (FN-01 reading A), each rupee moved from the liquor business into this book earns 3.3-5.2% pre-tax, and it pulls H1 ROE down to 13.9%. Bull reading: FN-01 reading A, treasury gains recognised only at year-end or on redemption, would lift the true yield; the FY26 AR investments note separates the two. For /fttcp: a whole-company PE would price this low-yield book at the liquor multiple.

---

## STEP 8. POSITION DECISION

Decision Status verified: NONE (no Notion page, live fetch 2026-10-17). The name is not held on record. Branch: **8A-W (watchlist / non-held)**.

### 8A-W

- Thesis-broken condition FIRED? None exist. Not applicable.
- Below bear / between bear and base / at or above base? Not assessable: no projections exist.
- Output. Updated entry zone: ND (no valuation, no CMP). Updated gate: none on record. Proposed Decision Status: none proposed. If the operator wants coverage, the house rules require a /step1 intake (Spear line) before /run-pipeline. This quarter supplies a clean filed baseline for that intake: growing net revenue (+18.28% YoY), compressed quarter margin (-145 bps), strong H1 cash as printed (1.24x; readings 1.02x-1.29x, 1.06x without the payables stretch), debt nil, and a treasury, lease and subsidiary question that decides how the business should be valued.

### 8B. Add-back / trim triggers

- Original add-back trigger: ND (none on record).
- Revised add-back trigger: none set; no position.
- Original trim ladder: ND.
- Revised trim ladder: none; no position.

### 8C. Single cleanest metric for Q3 FY27

**Operating EBITDA margin on net revenue (revenue net of excise, VAT and TCS).** It isolates the business from the excise rate and from treasury income, and it tests whether the other-expenditure step-up is permanent.
- Bull threshold: Q3 FY27 at or above 24.82% (Q2 FY26 level, Step 1C).
- Bear threshold: Q3 FY27 below 23.27% (Q1 FY27 level, Step 1C).
- Read with: (1) other expenses / net revenue back toward 4.51%; (2) gross margin on net revenue against 30.99% in Q2 FY27, because FY26 ran from 25.99% (Q1) to 33.61% (H2 average) and a gross-margin move can outweigh the other-expenditure test (Step 3); (3) Q3 FY26 is ND as a YoY base (only the H2 FY26 averages of 25.96% Op EBITDA margin and 33.61% gross margin exist).

---

## STEP 8.5. QUESTIONS FOR MANAGEMENT

Fourteen questions. The protocol asks for 5-8; the A4 contract requires one question per A3 FORWARD-SIGNAL or AMBIGUOUS finding (twelve findings: FN-03 plus eleven AMBIGUOUS), plus two Step 2 gaps. Ordered by materiality, with the loop 1 additions (Q13, Q14) last.

| # | Cat | Question | Why it matters | Bull answer | Bear answer | From |
|---|---|---|---|---|---|---|
| 1 | A/E | Net revenue rose 18.28% YoY (180.52 to 213.52 Cr). How many cases did you sell in Q2 FY27 and in Q2 FY26? | Volume vs price split is not in the filing. Growth quality depends on it. | Volume growth of 10% or more, with price on top | Volume flat; growth is MRP or duty-led | A4 Step 2 |
| 2 | C | Other expenditure rose from 8.14 to 13.27 Cr (+63.0%) and cut the net-revenue margin from 24.82% to 23.37%. Which single cost line drove the 5.13 Cr increase, and is it recurring? | It took 171 bps of net revenue, more than the whole 145 bps margin fall. The CMD rent likely sits in this line (FN-12). | A named one-time or regrouped item (Note 4) | A recurring cost (brand spend, licence fee, freight, rent) | A4 Step 2 |
| 3 | F | H1 investment purchases of 89.24 Cr took 93% of H1 CFO. Investments plus investment property are 876.36 Cr, 68.3% of assets. Does the board have a written cap on non-operating assets, yes or no, and what is the cap? | Capital is moving away from the liquor business. The book earns a recognised 3.34% pre-tax (TTM OI 31.77 Cr on a 951.01 Cr average book, 7A). It decides how the company should be valued. | Yes, with a cap and a stated payout or buyback policy | No policy; accumulation continues | FN-06 |
| 4 | D | What Ind AS 109 category are the 659.64 Cr non-current investments in (FVTPL, FVOCI or amortised cost), and how much of FY26 Other Income of 30.24 Cr was booked in Q4 FY26? | OI is H2-loaded (22.08 Cr in H2 FY26). H1 OI of 9.69 Cr is all cash items (interest 4.87, dividend 0.38, other 4.44) with no fair-value gain; the recognised yield is 5.17% even on investments alone. Interim PAT may understate, or the book may be illiquid. | FVTPL or liquid funds; gains recognised on redemption with a disclosed policy | Unlisted or illiquid instruments carried at cost | FN-01 |
| 5 | F | Buildfort Infradev received 1.01 Cr this half. What asset or project did it fund, and what total sum will the board commit to Buildfort in FY27? | A dormant shell started deploying parent cash. A non-liquor activity may begin. | A small, dated, disclosed purpose with a cap | Open-ended real-estate funding with no cap | FN-03 |
| 6 | D | Other current financial liabilities fell 18.74 Cr to 16.85 Cr (after a 57.86 Cr outflow in H1 FY26), and trade payables rose 13.71 Cr to 24.80 Cr. Other current assets fell 41.06 Cr to 107.72 Cr. What are the three largest items in OCFL and in OCA, in Rs Cr, and why did payables more than double? | The YoY CFO jump (0.66x to 1.24x PAT) comes from the smaller OCFL outflow (+39.12 Cr) and payables (+14.17 Cr), not OCA (+0.93 Cr). Without the payables stretch CFO is 1.06x PAT. | OCFL is a seasonal duty or deposit payable; payables reflect a one-time purchase timing; OCA is prepaid duty or licence fee | OCFL repayments were deferred; payables stretched to fund the treasury build; OCA holds advances to related or unnamed parties | FN-07 |
| 7 | B | Capital work-in-progress is 48.14 Cr, above net PPE of 40.42 Cr, and moved only 0.74 Cr in H1. What is the project, and on what date will it capitalise? | It is the only visible capacity signal. Stalled CWIP carries impairment risk. | Named capacity project with a date in FY27 | No date; aged more than 3 years | FN-08 |
| 8 | D | H1 tax expense was 25.91 Cr but direct tax paid was a round 23.00 Cr (R429), and the non-current tax asset rose 0.41 Cr (0.96 to 1.37 Cr) instead of falling. What was H1 direct tax actually paid (advance tax, TDS credits, self-assessment), and what does the 5.34 Cr PPE and capital-advance line contain beyond 2.06 Cr of fixed-asset additions? | The 3.32 Cr residual closes to within 0.10 Lakh between the CF tax and capex lines (FN-05). On reading A, CFO is 92.25 Cr (1.20x), not 95.53 Cr (1.24x). FCF is 90.19 Cr either way. | A CF grouping slip (for example TDS credits inside the capex line); provision correctly booked | No clear answer; provision unbooked and current liabilities understated | FN-05 |
| 9 | D | FY26 ETR was 23.66% against 25.17% in every interim quarter. Was the 3.10 Cr difference from lower-rate capital gains or from a prior-year reversal? | It decides whether a year-end FY27 tax true-up is likely. | Capital-gains rate on treasury income, recurring | A one-time prior-year reversal | FN-04 |
| 10 | G | Was the 1.01 Cr intercompany advance to Buildfort eliminated on consolidation, yes or no? Why does the RPT annexure show a closing balance of 0.00? | Consolidated assets and OCL gross up by 1.01 Cr. It tests consolidation process quality. | Yes, with a corrected RPT closing balance | No; or no explanation | FN-02 |
| 11 | G | At what time did the audit committee meet on 08-Oct-2026? All four LRR signature stamps (10:27:50-10:28:32 IST) precede the 11:30 board meeting, yet para 2 of both LRRs (l319-l320, l568-l569) says the statement "has been approved by the Board of Directors". | Sequencing of review and approval is a governance signal. | Audit committee met before 10:00 and the auditor signed on the AC-reviewed draft | No AC minutes time; or the auditor signed before any review | FN-09 |
| 12 | G | Your cover letter (l43-l45) and Statement E (l295-l298) say the limited reviews cover the quarter and the half year. Both auditor reports name only the quarter (l311, l559). Will the auditor confirm in writing that the reviewed statement included the H1 columns, the half-year balance sheet and the cash flow statement? | Reg 33 requires review of the half-year statements. The Step 5 cash reading depends on them. Auditor wording governs assurance. | Yes, with a corrected LRR title | The auditor declines to confirm | FN-10 |
| 13 | G | The RPT annexure shows lease rentals to the CMD of 1.49 Cr in H1 against 2.98 Cr approved (l255). Neither balance sheet shows a right-of-use asset or a lease liability. Which property is leased, what are the annual rent, escalation and term, is it a short-term lease under Ind AS 116, and what was the Q2 FY26 and FY26 rent? | The CMD earns more as landlord (1.49 Cr) than as managing director (0.90 Cr, FN-13). Either the rent resets yearly, subject to audit-committee approval, or a lease liability is unrecognised. The rent likely sits in the unsplit other expenditure. | Short-term lease at a disclosed market rent, unchanged vs FY26 | Multi-year lease without Ind AS 116, or a rent step-up in FY27 | FN-12 |
| 14 | D | Other non-current assets are 49.76 Cr (l139), larger than net PPE, and grew 4.05 Cr in H1 FY27 and 6.70 Cr in H1 FY26 (l208). What are the three largest items (capital advances, deposits with excise or tax authorities, amounts paid under protest), and are any linked to disputed demands? | The build ran inside CFO in both first halves shown. Capital advances would move CFO up and capex up; payments under protest would mark contingent liabilities. | Refundable deposits with no dispute, or capital advances for a dated project | Payments under protest against disputed excise or tax demands | FN-14 |

FN-11 and FN-13 (NEUTRAL-FACT) produce monitorables (M4, M6), not questions. FN-13 also informs Q13.

**Top 3 by likelihood of thesis-changing information.**
- Q3 (treasury policy). A written cap with a payout policy raises the case for valuing the liquor engine on its own. No policy confirms a cash-hoarding holding structure.
- Q2 (other expenditure). A recurring cost confirms the bear reading that the Q2 margin is the new level.
- Q11 (signing sequence). A vague answer is itself a governance signal on the review process.

**Channel recommendation.** IR email. No concall exists in the corpus. Address it to the Company Secretary, Sandeep Kutchhi, VP Finance & CS (R622, l70). Repeat the questions at the next AGM. The pipeline does not send the email; the operator decides.

**IR email draft (verbatim, for the operator):**
> Subject: G M Breweries Ltd, Q2 FY27 results: fourteen factual questions
> Dear Mr Kutchhi, we have read the results filed on 08-Oct-2026. Please answer the following, each with a number, a date or yes/no.
> 1. Cases sold in Q2 FY27 and Q2 FY26.
> 2. The cost line that drove the Rs 5.13 Cr rise in other expenditure (Rs 8.14 Cr to Rs 13.27 Cr), and whether it recurs.
> 3. Whether the board has a written cap on non-operating assets, and the cap.
> 4. The Ind AS 109 category of the Rs 659.64 Cr non-current investments, and the Q4 FY26 share of FY26 other income of Rs 30.24 Cr.
> 5. The asset or project funded by the Rs 1.01 Cr advance to Buildfort Infradev, and the FY27 funding limit.
> 6. The three largest items in other current financial liabilities (Rs 16.85 Cr) and in other current assets (Rs 107.72 Cr), and the reason trade payables rose from Rs 11.10 Cr to Rs 24.80 Cr.
> 7. The CWIP project (Rs 48.14 Cr) and its capitalisation date.
> 8. H1 direct tax actually paid (advance tax, TDS credits, self-assessment), and the content of the Rs 5.34 Cr PPE and capital-advance cash flow line.
> 9. The cause of the FY26 effective tax rate of 23.66%.
> 10. Whether the Rs 1.01 Cr Buildfort advance was eliminated on consolidation, and why the RPT closing balance shows 0.00.
> 11. The time the audit committee met on 08-Oct-2026.
> 12. Whether the auditor will confirm that the limited reviews covered the half-year figures, balance sheet and cash flow.
> 13. The property leased from the Chairman and Managing Director, its annual rent, escalation and term, its Ind AS 116 treatment, and the Q2 FY26 and FY26 rent.
> 14. The three largest items in other non-current assets of Rs 49.76 Cr, and whether any relate to disputed demands.

---

## MONITORABLES / CATALYSTS

A3 commitment register (F6): none. Board outcome forward items (F13): none (one agenda item, results only). The list below is seeded from the findings and the statutory calendar. Dates marked INFERENCE come from SEBI LODR / Companies Act deadlines, not from the company.

| # | Item | Implied date | Source ref |
|---|---|---|---|
| M1 | Q2 FY27 shareholding pattern: promoter %, pledge, institutional % (UA qualifier). Promoter-group dividends of 15.30 Cr are 83.2% of the 18.39 Cr paid (RPT values l256-l258 against CF cash paid l231). This ratio is not a holding figure: read as a holding, 83% would exceed the 75% maximum promoter holding under the minimum public shareholding rule [INFERENCE, regulatory, not in the filing]. The pattern settles it. | by 21-Oct-2026 (Reg 31, 21 days; INFERENCE) | Step 5 Promoter Pledge ND; F10; R569-R580 |
| M2 | FY26 Annual Report notes: investment category, CWIP ageing, tax reconciliation and tax-asset note, OCA breakdown, Ind AS 116 lease note, other non-current assets note, Buildfort AOC-1 | date ND (FY26 AR filing date not in corpus) | FN-01, FN-03, FN-04, FN-05, FN-07, FN-08, FN-12, FN-14 |
| M3 | Q3 FY27 results: Op EBITDA margin on net revenue (8C), gross margin on net revenue, other expenses / net revenue, excise intensity, D&A step if CWIP capitalises | by 14-Feb-2027 (Reg 33, 45 days; INFERENCE). Q2 was filed 8 days after quarter end. | Step 8C; Step 3; FN-08 |
| M4 | Q3 FY27 board outcome: LRR signature time vs meeting time; LRR period scope; title dates | with M3, by 14-Feb-2027 (INFERENCE) | FN-09, FN-10, FN-11 |
| M5 | Q3 FY27 shareholding pattern | by 21-Jan-2027 (Reg 31; INFERENCE) | M1 follow-up |
| M6 | FY27 audited results: Q4 other-income step-up, year-end ETR true-up, H2 FY27 cash flow (OCA rebuild, OCFL and payables reversal, other non-current asset build), H2 RPT annexure (Buildfort balance, CMD rent and KMP pay vs approval), audit report scope | by 30-May-2027 (Reg 33, 60 days; INFERENCE) | FN-01, FN-04, FN-07, FN-02, FN-03, FN-10, FN-12, FN-13, FN-14 |
| M7 | FY27 Annual Report and AGM: Buildfort financials, segment note wording ("at present"), investment schedule | AGM by 30-Sep-2027 (Companies Act s.96; INFERENCE) | FN-03, FN-06 |
| M8 | IR email reply to the fourteen questions | ND (operator sends) | Step 8.5 |

---

## STEP 9. NOTION UPDATE: PAYLOAD ONLY

No Notion page exists, so there is nothing to update. A4 writes nothing to Notion and never writes Decision Status. Proposed payload if the operator creates a page: Key Notes line "2026-10-17 | Q2 FY27 PRE-THESIS READ | net rev +18.3% YoY, op margin (net) -145 bps to 23.37%, H1 CFO/PAT 1.24x (readings 1.02x-1.29x; 1.06x ex payables stretch), debt nil, investments plus property 68% of assets; 951 Cr average non-operating book at a recognised 3.3% pre-tax yield, Buildfort funded 1.01 Cr, CMD lease with no lease liability, LRR signed before board | PROCEED WITH FLAGS". Catalyst status: N.A. Thesis status: N.A. (no thesis).

---

## VERDICT

**Protocol verdict: PROCEED WITH FLAGS.**

Cash conversion is INDETERMINATE-WITH-DIRECTION, which caps the verdict at PROCEED WITH CAVEATS. Governance and process flags (signing sequence, review scope, consolidation elimination, related-party lease) add flags on top. The caveats are named: FY26 full-year CFO ND; OCA, OCFL, payables and other non-current asset composition ND; H1 BS and CF review claimed by the company, not confirmed by the auditor.

Loop 1 re-check. The verdict and the cash classification still follow. FN-10 is lower in severity than the first pass stated, but the auditor's wording still governs. FN-12 (CMD lease with no lease liability) and FN-14 (49.76 Cr non-current asset, content ND) add flags. The YoY cash split moves the source of the cash strength from an asset release to liability timing.

Loop 2 re-check (A5-C1). The alternative readings span 1.02x-1.29x around the 1.24x print. The low end (1.02x) stacks FN-05 reading A, supported by a filed tie, and the payables timing test. The high end (1.29x, FN-14 reading B) is weakly evidenced, because the CF capex line already includes capital advances (l219-l220). No reading takes CFO below PAT. None fixes the band, because full-year CFO is ND. No item lifts the cash cap, and no table number, cap or verdict moved.

Flags (surfaced; decisions stay with the operator):
1. PRE-THESIS READ: no Notion page, no spear, no company memory.
2. Cash conversion INDETERMINATE-WITH-DIRECTION: H1 CFO/PAT 1.24x as printed. The YoY jump from 0.66x comes from a smaller OCFL outflow (+39.12 Cr) and a payables stretch (+14.17 Cr); the OCA release was flat YoY (+0.93 Cr). Readings span 1.02x-1.29x: 1.06x without the payables stretch; 1.20x on FN-05 reading A; 1.29x on FN-14 reading B, weakly evidenced (capex line already includes capital advances, l219-l220). FY CFO ND (FN-07, FN-05, FN-14).
3. LRR digital signatures precede the board meeting by 61-62 minutes, and para 2 of both LRRs says the board had approved (FN-09).
4. LRR scope: the company claims a quarter and half-year review (l43-l45, l295-l298); the auditor names the quarter only (l311, l559). Auditor wording governs; H1 BS and CF review claimed by the company, not confirmed by the auditor (FN-10).
5. Consolidation gross-up of 1.01 Cr; RPT closing balance 0.00 conflicts (FN-02).
6. Buildfort Infradev activated with parent funding; purpose undisclosed (FN-03).
7. Investments plus investment property 876.36 Cr = 68.3% of assets; 93% of H1 CFO went to investments. The 951.01 Cr average non-operating book (adding other NC financial assets and cash, 7A) earns a recognised 3.34% pre-tax (5.17% if all OI is attributed to investments alone), all cash items, no fair-value gain; "at present" single segment (FN-06, FN-01).
8. Q2 op margin on net revenue -145 bps YoY on other expenditure +63.0%; line not split. FY26 gross margin ran 25.99% to 33.61%, so material cost is a second, larger margin variable.
9. Excise intensity up 34 bps YoY; net revenue grows slower than gross.
10. Tax: interim ETR 25.17% vs FY26 23.66% (FN-04). The 3.32 Cr tax residual closes to within 0.10 Lakh against the capex line (non-current tax asset +0.41 Cr); FCF 90.19 Cr on either reading (FN-05).
11. CMD lease rentals 1.49 Cr H1 with no right-of-use asset, lease liability or lease outflow; CMD rent exceeds CMD pay of 0.90 Cr (FN-12, FN-13).
12. Other non-current assets 49.76 Cr, larger than net PPE, built inside CFO in both H1s shown; content ND (FN-14).
13. Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar facts flagged above.
14. Downstream tracker: zero signals; Role 5.5 never run.
15. A1 extraction defects EX-1 to EX-3 loop to A1; no value used depends on them.

---

## LOOP 1 CHANGE LOG

Correction loop 1, 2026-10-17. Scope: the A5 items named by the orchestrator. No other step was re-derived. "rv l###" is the first-pass review line that A5 cited; the new location is given by section. Every added number was checked at its fulltext line (l36-l300, l305-l329, l555-l616) or taken from the loop 1 A3 forensics.

| Item | First-pass lines (rv l###) | Sections changed | Outcome |
|---|---|---|---|
| A5-F1 FACTUAL | l605 | Brief part 4 | Fixed. "Strong on cost [FILED]" dropped. The [FILED] claim now covers cash only (debt nil, receivables about 2 days). Cost position is stated as not known, [INFERENCE], with no filed comparator. |
| A5-M1 (FN-12, FN-13) | l195, l477 (no prior lease text) | Preamble; 0D new RPT row; Step 2 margin driver; Step 4 other-expenditure row; new Step 5E; Step 7 Pillar 3 row; Q2, new Q13; M2, M6; Step 9; Verdict flag 11; Brief parts 1, 3 | Done. Lease with no ROU or lease liability carried as AMBIGUOUS with two readings and Q13. KMP pay (NEUTRAL-FACT) carried as a governance line: CMD rent 1.49 Cr above CMD pay 0.90 Cr. |
| A5-M2 (FN-14, revised FN-05) | l261, l266, l434, l483, l555 | 5A new rows (NC tax assets, other non-current assets, CF line); 5B new row; 5D tax-and-capex bullet and readings table; Step 7 operating-capital row; Q8 revised, new Q14; M2, M6; Verdict flags 10, 12 | Done. FN-05 residual shown closing between the tax and capex lines (2.91 + 0.41 = 3.28 + 0.04 = 3.32 Cr; loop 2 wording: within 0.10 Lakh, A5-S9). Reading A CFO 92.25 Cr (119.8% of PAT); FCF 90.19 Cr unchanged. Other non-current assets 49.76 Cr added to Step 7 operating capital and as AMBIGUOUS with Q14. |
| A5-M3 (revised FN-10; extended FN-09) | l78, l325, l486, l487, l549 | 0D note 5 row and auditor check (a), (c); 5D review caveat; Q11, Q12 revised; Verdict flags 3, 4; Brief part 1 | Done. Both readings stated; auditor wording governs; H1 BS and CF review "claimed by the company, not confirmed by the auditor". FN-09 now cites para 2 of both LRRs and 61-62 minutes. |
| A5-M6 cash attribution | l266, l321-l322, l547, l572-l573 | 5A WC rows re-verdicted; 5D new YoY driver table and CFO readings table; Step 7 Pillar 2 row; P4; Q6 revised; Step 8A-W; Step 9; Verdict flag 2; Brief part 1 | Done. OCFL +39.12 Cr, payables +14.17 Cr, OCA +0.93 Cr; other six lines -14.36 Cr. Ex-payables CFO 81.82 Cr, 1.06x. Reconciled with FN-05 reading A (92.25 Cr, 1.20x; both together 78.54 Cr, 1.02x) and FN-14 reading B (99.58 Cr, 1.29x). Cash class unchanged. |
| A5-M7 gross margin | l205, l246, l466, l569, l594 | 1C note; Step 2 H1 cross-check; Step 3 new gross-margin column and diagnostic; Step 4 H1 note; 5.5C; Step 6.5 seasonality; Step 7 new margin row; 8C read-with list; M3; Verdict flag 8; Brief parts 1, 3 | Done. Derived Q1 FY26 gross margin 25.99% (CoM 74.36%), Q2 FY26 31.06%: 5.07 pp swing, about 10.82 Cr a quarter at Q2 FY27 net revenue. Also derived H2 FY26 33.61% (7.62 pp above Q1 FY26). Gross margin added to 8C read-with. |
| A5-M8 treasury yield | l433, l597-l598, l478, l479 | Step 7 ROCE row; new 7A table; Q3, Q4 rationale; Step 9; Verdict flag 7; Brief part 3 | Done. 3.34% pre-tax on the 951.01 Cr average book (2.50% post-tax); 5.17% on investments alone; H1 OI 9.69 Cr all cash items, no fair-value gain. |
| A5-S1 rounding | l185, l195, l271, l273, l285 | Step 2, 5A | Applied from raw Lakhs: 27.28%, 1.71 pp, 2.23 days (change +1.14), 7.91 days (change +7.98), CCC 7.58 (change -10.01; loop 2: -10.02, A5-S14), 582.55 / 661.68. |
| A5-S2 | l214 | Step 3 | Applied: "highest of the quarters the filing prints individually". |
| A5-S3 | l193, l215, l244 | Step 2 diag 6, Step 3, Step 4 | Applied: H2, with Q4 tagged INFERENCE. |
| A5-S4 | l195 | Step 2 margin driver | Applied: "more than the whole 145 bps fall" (171 bps). |
| A5-S5 | l260, l483 | 5A pre-WC row, 5D, Q8 | Applied: R429 / R430 cited. |
| A5-S6 | l618 | Brief part 5, M2 | Applied: "date ND". |
| A5-S7 | l522 | M1 | Applied: caveat that 83.2% is not a holding figure. |
| A5-S8 | n.a. | none | A1 extraction note; not an A4 change. Approval status of all ten RPT rows noted in 5E. |
| Verdict re-check | l541-l558 | Verdict | PROCEED WITH FLAGS stands. Cash INDETERMINATE-WITH-DIRECTION stands. Flags renumbered 1-15 (two added: 11, 12). |
| Block | l626-l689 | YAML | Rewritten: FN-01 to FN-14 incorporated; 14 questions; monitorables and flags updated; analyst_note revised. |

---

## LOOP 2 CHANGE LOG

Correction loop 2, 2026-10-17. Scope: A5-C1 (CONTRADICTION) and style notes A5-S9 to A5-S14 from the A5 LOOP 1 RE-AUDIT. No other step was re-derived. "rv l###" is the loop-1 review line that A5 cited. Every changed figure was re-checked at its fulltext line (l82, l128-l167, l196-l225, l248-l257, l388).

| Item | Loop-1 lines (rv l###) | Sections changed | Outcome |
|---|---|---|---|
| A5-C1 CONTRADICTION | l358, l625, l629, l450, l492, l615, l805 | 5A CFO/PAT verdict; 5D readings table (Basis cell of the FN-14 reading B row only) and the reconciliation text under it; P4; Step 7 Pillar 2 row; Step 8A-W; Step 9; Verdict loop 2 re-check; flag 2; Brief part 1; YAML flag 2 and analyst_note | Fixed by both options together. The text now states the 1.02x-1.29x range around the 1.24x print. It also ranks each reading on one evidence bar. FN-05 reading A (bear) is supported by a filed tie. The payables test (bear) is a timing sensitivity. FN-14 reading B (bull) is weakly evidenced, because the CF capex line already includes capital advances (ft l219-l220). Re-checked: 9,553.02 + 404.73 = 9,957.75 Lakh = 99.58 Cr; / 7,703 = 1.29x; FCF 9,957.75 - 939.22 = 9,018.53 Lakh = 90.19 Cr (ft l107, l208, l217, l220). No table number, cap or verdict moved. |
| A5-S9 | l360, l559, l637, l654, l798 | 5D tax and capex bullet; Q8; flag 10; loop 1 log row A5-M2; YAML flag 10 and Q8 | Applied: "closes to within 0.10 Lakh". Tax side 332.08 Lakh, capex side 332.18 Lakh; the gap equals the 0.10 Lakh fall in intangible assets (ft l134). |
| A5-S10 | l615, l634, l687, l795 | Step 7 ROCE row; Step 9; flag 7; Brief parts 1, 3; YAML flag 7 and analyst_note | Applied: the 3.34% yield is named on the 951.01 Cr average non-operating book (7A). The 876.36 Cr figure is named as investments plus investment property only. No number changed. |
| A5-S11 | l708, l359 | Brief part 3; 5A OCA and other non-current asset rows; 5D WC drag bullet; Q14; flag 12; YAML flag 12 | Applied: "both first halves shown". The OCA H2 rebuild is tagged INFERENCE, because the filing prints no H2 cash flow and no Sep-2025 BS. |
| A5-S12 | l81, l363 | 0D auditor check (a); 5D review caveat | Applied: the cause is tagged INFERENCE with both readings named (truncated quote; template carried over from a quarter-only report). The l388 citation now says the consolidated title prints "September 30, 2025" (FN-11). |
| A5-S13 | l381 | 5E CMD lease bullet; Q13 rationale | Applied: "resets each year, subject to audit-committee approval" (ft l255 "Approved"). |
| A5-S14 | l282, l75, l380 | 5A CCC row; 0D RPT row; 5E table row 4 and KMP bullet | Applied. Two derived cells changed at the 0.01 level, as rounding fixes from raw values: CCC change -10.01 to -10.02 (raw -10.0155); 5E row 4 ratio 50% to 50.02% (15.13 / 30.25 Lakh, ft l253). Neither cell feeds a cap or the verdict. |
| A5-S15, A5-S8 | n.a. | none | A2 and A1 notes; not A4 changes. |
| Verdict re-check | l621-l642 | Verdict | PROCEED WITH FLAGS stands. Cash INDETERMINATE-WITH-DIRECTION stands. Flags stay numbered 1-15. |
| Block | l740-l807 | YAML | Rewritten: flags 2, 7, 10, 12, the FN-05 question and the analyst_note updated; everything else kept. |

---

## PLAIN-LANGUAGE BRIEF

### 1. Summary narrative

G M Breweries sold Rs 213.52 Cr of country liquor after excise in Q2 FY27 [FILED, this quarter]. That is 18.3% more than a year ago [FILED].
Operating profit rose less, by 11.4%, to Rs 49.91 Cr [FILED].
The operating margin fell from 24.8% to 23.4% [FILED].
Material cost took about 69% of net revenue in both quarters. Other expenses rose 63%, and the filing does not say why [FILED].
Material cost is not always this steady. Gross margin was 26.0% in Q1 FY26 and 31.1% in Q2 FY26 [INFERENCE from FILED, derived].
Profit after tax was Rs 39.29 Cr, up 12.6% [FILED]. About 81% of that gain came from the business, not from treasury income [INFERENCE from FILED].
For the half year, profit rose 26.8%, because the first quarter of last year had a weak gross margin [FILED, derived].
Cash from operations was Rs 95.53 Cr in the half, 1.24 times profit [FILED].
Most of the gain on last year's 0.66 times came from smaller payouts on other financial liabilities and slower supplier payments [FILED]. Without the supplier stretch, cash was 1.06 times profit [INFERENCE from FILED].
Other readings of the same cash statement give 1.02 to 1.29 times profit. The top reading has weak support [INFERENCE from FILED].
The company has no debt [FILED].
It holds Rs 659.64 Cr of investments and Rs 216.72 Cr of investment property, 68% of all assets [FILED].
This half it put 93% of operating cash into investments [FILED]. With deposits and cash added, the non-operating book averaged about Rs 951 Cr. Over the last four quarters it earned 3.3% before tax in recognised income [INFERENCE from FILED].
A dormant subsidiary with a real estate name received Rs 1.01 Cr [FILED].
The chairman received Rs 1.49 Cr of rent from the company in the half, more than his Rs 0.90 Cr pay. The balance sheet shows no lease [FILED].
The auditor signed the review about one hour before the board met [FILED]. The company says the review covers the half year; the auditor's report names only the quarter [FILED].
We have no thesis, no Notion page and no position. This is a first read, not a thesis check.
The next test is the Q3 FY27 margin on net revenue: 24.8% or above is good, below 23.3% is bad. Read it with the gross margin.

### 2. Sector intelligence

Country liquor is a state-regulated product. The state sets duty and often the retail price [INFERENCE, not in filings].
The filing shows excise, VAT and TCS take 75.2% of gross sales [FILED, this quarter]. That share rose from 74.9% a year ago [FILED].
A rising duty share means the state takes more of each rupee. Net price growth then lags gross price growth [INFERENCE].
The factory is at Virar in Palghar district, Maharashtra [FILED]. So Maharashtra excise policy is the main sector variable [INFERENCE].
Demand data, licence counts and state duty changes are not in the corpus. Each is PENDING LIVE VERIFICATION.
No Notion sector work exists for this name.

### 3. Business-model intelligence

The company buys spirit and materials, bottles country liquor, and sells it with duty included [FILED: single segment, R706; revenue inclusive of excise, R701].
Material cost is about 69% of net revenue [FILED]. Gross margin was near 31% in the last three printed quarters [FILED]. In FY26 it ran from 26.0% in Q1 to 33.6% across H2 [INFERENCE from FILED, derived]. Material cost is the larger margin variable.
Receivables are about 2 days and inventory about 21 days [INFERENCE from FILED]. Buyers pay almost at once.
Fixed assets are small: plant and equipment of Rs 40.42 Cr [FILED]. Capital work in progress of Rs 48.14 Cr is larger than the plant itself, and its purpose is not disclosed [FILED]. Other non-current assets of Rs 49.76 Cr are also larger than the plant, grew in both first halves shown, and are not explained [FILED].
The model drifts in one direction. Profit becomes cash, and cash becomes investments and property, not plant [FILED].
The wider non-operating book, about Rs 951 Cr on average with deposits and cash, earns a recognised 3.3% a year before tax [INFERENCE from FILED]. So the company is part liquor maker, part low-yield investment holder [INFERENCE].
The chairman leases property to the company. The rent does not appear as a lease on the balance sheet [FILED].
The filing does not disclose volumes, prices, brands, plant use, the investment type or the lease term. Each is ND.

### 4. Competition intelligence

The filing names no competitor and gives no market share [FILED: none disclosed].
Listed alcohol peers include United Spirits, Radico Khaitan and Tilaknagar Industries in branded liquor, and Globus Spirits in country liquor and spirit [INFERENCE, not from this quarter's filings or Notion; PENDING LIVE VERIFICATION].
G M Breweries looks strong on cash: debt is nil and buyers pay in about 2 days [FILED].
Whether it is strong on cost is not known. The filing has no peer comparator, and this quarter other expenses rose 63% [INFERENCE; FILED].
It looks weaker on growth visibility. It gives no guidance, holds no concall and has one segment in one state [FILED, INFERENCE].
The risk to watch is a state duty or price change that compresses the net margin, or a licensed rival taking volume [INFERENCE].
Peer margins and volumes are ND in this corpus.

### 5. Forward map (next ~10-11 months)

Make-or-break reading: Q3 FY27 operating margin on net revenue, due by 14-Feb-2027. Read it with the gross margin on net revenue.
- Bull fork: 24.82% or above, so the other-expense rise was a one-time item.
- Bear fork: below 23.27%, so the cost rise is permanent, or the gross margin has slipped.

Dated catalysts:
- 21-Oct-2026, Q2 shareholding pattern. Bull: no pledge. Bear: pledge appears.
- Date ND, FY26 annual report notes. Bull: investments are liquid and marked at fair value; CWIP has a date; the chairman's lease is short-term; other non-current assets are refundable deposits. Bear: investments are illiquid at cost; CWIP has aged; a lease liability is missing; payments sit under protest.
- By 14-Feb-2027, Q3 board outcome. Bull: the review covers the half year and is signed after the board meets. Bear: the same signing pattern repeats.
- By 30-May-2027, FY27 audited results. Bull: other income steps up and cash holds through H2. Bear: other current assets rebuild, the supplier stretch reverses, and full-year cash falls below profit.
- By 30-May-2027, H2 related-party annexure. Bull: Buildfort funding stops or gets a disclosed plan; rent stays within approval. Bear: further open-ended funding, or a rent step-up.
- By 30-Sep-2027, FY27 AGM. Bull: a treasury policy with a payout. Bear: more assets move out of liquor.

---

```yaml
stage: A4-analyst
company: "GMBREW"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results]
ledger_reconciliation:
  notes: 10
  turns: 0
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: ["FN-01", "FN-02", "FN-03", "FN-04", "FN-05", "FN-06", "FN-07", "FN-08", "FN-09", "FN-10", "FN-11", "FN-12", "FN-13", "FN-14"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "NONE (no Notion page; live fetch 2026-10-17; PRE-THESIS READ)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY26", gap_pct: 0.00}
  - {period: "Q1 FY27", gap_pct: 0.00}
  - {period: "Q2 FY27", gap_pct: 0.00}
  - {period: "H1 FY26", gap_pct: 0.00}
  - {period: "H1 FY27", gap_pct: 0.00, note: "printed; CF-implied PBT gap -0.0042 Cr = -0.005%"}
  - {period: "FY26", gap_pct: 0.00}
questions_for_management:
  - {q: "Cases sold in Q2 FY27 vs Q2 FY26 (net revenue +18.28% YoY, 180.52 to 213.52 Cr)", from_finding_id: "A4-Step2"}
  - {q: "Which cost line drove the 5.13 Cr rise in other expenditure (8.14 to 13.27 Cr; 171 bps of net revenue vs a 145 bps margin fall), and is it recurring?", from_finding_id: "A4-Step2"}
  - {q: "Is there a written board cap on non-operating assets (876.36 Cr, 68.3% of assets; 93% of H1 CFO invested; recognised pre-tax yield 3.34% on a 951.01 Cr average book), and what is it?", from_finding_id: "FN-06"}
  - {q: "Ind AS 109 category of the 659.64 Cr investments, and the Q4 FY26 share of FY26 other income of 30.24 Cr? (H1 OI 9.69 Cr all cash items, no fair-value gain; 5.17% recognised yield on investments alone)", from_finding_id: "FN-01"}
  - {q: "What did the 1.01 Cr advance to Buildfort Infradev fund, and what is the FY27 funding limit?", from_finding_id: "FN-03"}
  - {q: "Three largest items in OCFL (16.85 Cr, outflow 18.74 Cr H1) and OCA (107.72 Cr, 41.06 Cr release), and why did trade payables rise from 11.10 to 24.80 Cr? (YoY CFO jump = OCFL +39.12 Cr, payables +14.17 Cr, OCA +0.93 Cr)", from_finding_id: "FN-07"}
  - {q: "What is the 48.14 Cr CWIP project and its capitalisation date?", from_finding_id: "FN-08"}
  - {q: "H1 direct tax actually paid (advance tax, TDS, self-assessment) vs the round 23.00 Cr printed, and what the 5.34 Cr PPE and capital-advance line holds beyond 2.06 Cr of additions? (3.32 Cr residual closes to within 0.10 Lakh between CF tax and capex lines; reading A CFO 92.25 Cr)", from_finding_id: "FN-05"}
  - {q: "Was the FY26 ETR of 23.66% (3.10 Cr shield) from capital-gains rate or a prior-year reversal?", from_finding_id: "FN-04"}
  - {q: "Was the 1.01 Cr Buildfort advance eliminated on consolidation, and why is the RPT closing balance 0.00?", from_finding_id: "FN-02"}
  - {q: "What time did the audit committee meet on 08-Oct-2026, given all four LRR signatures (10:27:50-10:28:32 IST) precede the 11:30 board and both LRR para 2s say the board had approved?", from_finding_id: "FN-09"}
  - {q: "Company says the LRRs cover quarter and half year (l43-l45, l295-l298); auditor names the quarter only (l311, l559). Will the auditor confirm the H1 columns, half-year BS and CF were reviewed?", from_finding_id: "FN-10"}
  - {q: "Which property does the CMD lease to the company (1.49 Cr H1 rent, 2.98 Cr approved, no ROU or lease liability); annual rent, escalation, term, Ind AS 116 treatment, Q2 FY26 and FY26 rent?", from_finding_id: "FN-12"}
  - {q: "Three largest items in other non-current assets of 49.76 Cr (built 4.05 Cr H1 FY27, 6.70 Cr H1 FY26); any linked to disputed demands?", from_finding_id: "FN-14"}
monitorables:
  - {item: "Q2 FY27 shareholding pattern: promoter %, pledge, institutional %; 83.2% promoter-group dividend share is not a holding figure", implied_date: "2026-10-21 (Reg 31; inference)", source_ref: "Step 5 pledge ND; A3 F10; M1"}
  - {item: "FY26 Annual Report notes: investment category, CWIP ageing, tax reconciliation and tax-asset note, OCA breakdown, Ind AS 116 lease note, other non-current assets note, Buildfort AOC-1", implied_date: "date ND (FY26 AR filing date not in corpus)", source_ref: "FN-01, FN-03, FN-04, FN-05, FN-07, FN-08, FN-12, FN-14"}
  - {item: "Q3 FY27 results: op EBITDA margin on net revenue (bull >=24.82%, bear <23.27%), gross margin on net revenue (vs 30.99%), other expenses/net revenue, excise intensity", implied_date: "by 2027-02-14 (Reg 33; inference)", source_ref: "Step 8C; Step 3; FN-08"}
  - {item: "Q3 FY27 board outcome: LRR signing time vs meeting, LRR period scope, title dates", implied_date: "by 2027-02-14 (inference)", source_ref: "FN-09, FN-10, FN-11"}
  - {item: "Q3 FY27 shareholding pattern", implied_date: "2027-01-21 (Reg 31; inference)", source_ref: "M1 follow-up"}
  - {item: "FY27 audited results: Q4 OI step-up, year-end ETR true-up, H2 CFO (OCA rebuild, OCFL and payables reversal, other NC asset build), H2 RPT (Buildfort balance, CMD rent and KMP pay vs approval), audit scope", implied_date: "by 2027-05-30 (Reg 33; inference)", source_ref: "FN-01, FN-02, FN-03, FN-04, FN-07, FN-10, FN-12, FN-13, FN-14"}
  - {item: "FY27 Annual Report and AGM: Buildfort financials, segment wording, investment schedule", implied_date: "by 2027-09-30 (Companies Act s.96; inference)", source_ref: "FN-03, FN-06"}
  - {item: "IR email reply to the fourteen questions", implied_date: "ND (operator sends)", source_ref: "Step 8.5"}
flags:
  - "PRE-THESIS READ: no Notion page, no spear, no companies/GMBREW.md"
  - "Cash conversion INDETERMINATE-WITH-DIRECTION: H1 CFO/PAT 1.24x printed; YoY jump from OCFL (+39.12 Cr) and payables (+14.17 Cr), OCA flat (+0.93 Cr); readings span 1.02x-1.29x: 1.06x ex payables stretch, 1.20x on FN-05 reading A, 1.29x on FN-14 reading B (weakly evidenced: CF capex line already includes capital advances, ft l219-l220); FY CFO ND (FN-07, FN-05, FN-14)"
  - "LRR digital signatures 10:27:50-10:28:32 IST precede 11:30 board by 61-62 min; both LRR para 2s say board approved (FN-09)"
  - "LRR scope: company claims quarter and half year, auditor names quarter only; auditor wording governs; H1 BS and CF review claimed by company, not confirmed by auditor (FN-10)"
  - "Consolidated assets/OCL gross up 1.01 Cr vs standalone; RPT closing balance 0.00 conflicts (FN-02)"
  - "Buildfort Infradev shell funded 1.01 Cr by parent; purpose undisclosed (FN-03)"
  - "Investments plus investment property 876.36 Cr = 68.3% of assets; 89.24 Cr H1 investment purchases = 93% of CFO; recognised pre-tax yield 3.34% on the 951.01 Cr average non-operating book (5.17% if all OI is attributed to investments alone), no fair-value gain; 'at present' single segment (FN-06, FN-01)"
  - "Q2 op EBITDA margin on net revenue -145 bps YoY (24.82% to 23.37%) on other expenditure +63.0%; FY26 gross margin ran 25.99% to 33.61%"
  - "Excise intensity +34 bps YoY (74.85% to 75.19%)"
  - "Tax: interim ETR 25.17% vs FY26 23.66% (FN-04); 3.32 Cr tax residual closes to within 0.10 Lakh against the capex line; FCF 90.19 Cr on either reading (FN-05)"
  - "CMD lease rentals 1.49 Cr H1 with no ROU asset, lease liability or lease outflow; CMD rent above CMD pay 0.90 Cr (FN-12, FN-13)"
  - "Other non-current assets 49.76 Cr, above net PPE, built inside CFO in both H1s shown; content ND (FN-14)"
  - "Role 4 Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar facts flagged"
  - "Downstream tracker: zero signals; Role 5.5 never run"
  - "A1 extraction defects EX-1..EX-3 loop to A1; no used value depends on them"
plain_language_brief_included: true
analyst_note: "Loop 2 is scoped to A5-C1 and style notes S9-S14; nothing else was re-derived. The verdict holds at PROCEED WITH FLAGS and cash stays INDETERMINATE-WITH-DIRECTION. No cap or verdict moved; two derived cells changed at the 0.01 level as S14 rounding fixes (CCC change -10.02; 5E row 4 at 50.02%). H1 CFO/PAT prints 1.24x. The YoY rise from 0.66x is a smaller OCFL payout (+39.12 Cr) and a payables stretch (+14.17 Cr); OCA was flat (+0.93 Cr). The alternative readings span 1.02x-1.29x, and each takes the same evidence bar. FN-05 reading A (1.20x, bear) rests on a filed tie of the tax and capex residuals to within 0.10 Lakh. The payables test (1.06x, bear) is a timing sensitivity. FN-14 reading B (1.29x, bull) is weakly evidenced, because the CF capex line already includes capital advances (ft l219-l220). FCF of 90.19 Cr holds on both accounting readings. Pre-WC conversion of about 0.95x stays the structural anchor; full-year CFO is ND. The 3.34% recognised yield is on the 951.01 Cr average non-operating book, so /fttcp must value it apart from the liquor business. S15 belongs to A2, S8 to A1."
review_path: "runs/gmbrew-q2fy27/work/review_gmbrew_q2fy27.md"
```
