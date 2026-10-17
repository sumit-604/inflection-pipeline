# Notion payload: INDORAMA Q2 FY27 (READY FOR OPERATOR APPROVAL, NOT WRITTEN)

STATUS: A5 COMPLETE after correction loop 2 (operator-approved 2026-10-17). Write gate
(operator ruling 2026-10-03): no Notion write happens without the operator's explicit
approval of this exact payload. Decision Status is never written. Open STYLE notes S5-S11
are logged in work/audit_indorama_q2fy27.md and do not block the save.

TARGET: no COMPANIES MASTER page exists (live search 2026-10-17: "Indo Rama Synthetics",
"Indorama", "IRSL polyester" returned none). The save therefore needs a NEW page.
- Data source: COMPANIES MASTER, collection://345bb2b9-d3ab-8032-9b46-000ba16ab827
- Call 1: notion-create-pages with properties:
  - Name: "Indo Rama Synthetics (India) Ltd"
  - Ticker: "INDORAMA"
  - Sector: "Textiles / Polyester"
  - date:Analysis Date 1:start: "2026-10-17"
  - Key Notes (new page, so no prior trail to preserve; | escaped as \|):
    "2026-10-17 \| Q2 FY27 pre-thesis read (/run-quarterly; results + press release + Reg 30 capex letter, all 16-Oct-2026; A5 COMPLETE after 2 loops): C PAT 74.08 vs 24.55 (+201.75% YoY off a trough base; core PBT +41.20% vs Q1 FY26) on nil current tax (statutory-rate H1 EPS 3.94 vs 5.28); gross margin 22.60% vs 22.98% YoY, gain from other expenses and FX; net debt -261.47 in H1 (152.45 pre-tax operating cash + 109.02 WC release; about 52/48 at a 25.17% tax); net DTA 39.4% of C equity; subsidiaries 25.7-47.1% of C PAT with no split; Rs 200 cr specialty capex approved, term loan + accruals, COD Oct-2027 to Apr-2028. Verdict PROCEED WITH FLAGS; cash conversion INDETERMINATE-WITH-DIRECTION. No thesis, no spear; Decision Status not set (operator-only)."
  - Decision Status: NOT WRITTEN (operator-only)
- Call 2..n: insert_content, position end, in sequential chunks: the full A4 review below
  (complete tables, includes the PLAIN-LANGUAGE BRIEF), then the three A3 forensics
  tables, then the A5 audit verdict block.

=====================================================================
## CONTENT PART 1: A4 MERGED REVIEW (work/review_indorama_q2fy27.md, verbatim, loop 2)
=====================================================================
# A4 MERGED REVIEW: Indo Rama Synthetics (India) Ltd (INDORAMA), Q2 FY27

Quarter: Q2 FY27 (quarter ended 30-Sep-2026; filings dated 16-Oct-2026)
Protocol: Role 4, Quarterly Results Review Protocol v1.4 (frameworks/Quarterly_Results_Review_Protocol_v1_4.md). Role 5 not run: no concall in --docs.
Documents merged: results filing (Reg 33, standalone + consolidated, limited review), press release (presentation class), capex Board Outcome (Reg 30, one page).
Framing: **PRE-THESIS READ, not a thesis check.** No Notion page, no Decision Status on record, no companies/INDORAMA.md, no spear on record (runs/indorama-q2fy27/work/notion-thesis.md, lines 3-14).
Model: claude-opus-5-5. Reviewer: A4 analyst. Date: 2026-10-17. **Revision: correction loop iterations 1 and 2 (A5 audit runs/indorama-q2fy27/work/audit_indorama_q2fy27.md). Change logs at the end.**

Anchor key: RF = runs/indorama-q2fy27/extracted/indorama-results-q2fy27-fulltext.md; PR = .../indorama-pressrelease-q2fy27-fulltext.md; CX = .../indorama-capex-q2fy27-fulltext.md. "L" = fulltext line. Results table values cite the image-verified VER- lines (RF L196-222 standalone P&L; RF L288-323 standalone balance sheet; RF L374-407 standalone cash flow; RF L590-622 consolidated P&L; RF L680-714 consolidated balance sheet; RF L767-799 consolidated cash flow). "d:" = derived by A4 from the cited lines (arithmetic on filed numbers, not a filed figure). S = standalone, C = consolidated. Unit: Rs crore throughout.

Finding-ID prefixes: results A3 findings keep their IDs (A3-01 to A3-16). The press-release and capex A3 files both number from FN-01, so this review prefixes them PR-FN-xx (forensics_pressrelease) and CX-FN-xx (forensics_capex). A4's own findings are A4-xx.

---

## LEDGER RECONCILIATION PREAMBLE

**Ledger contains 12 notes / 0 turns / 3 slides. All 12 notes, 0 turns and 3 slides reviewed.**

| Document | Ledger | Structured IDs | IDs in ledger | Orphans | Count test | Reviewed |
|---|---|---|---|---|---|---|
| Results | work/ledger_results_indorama_q2fy27.md | 721 (R001-R721) | 721 | none | gate_a2 pass (notes 12, line items 198, zero-standing 85, agenda 2, auditor paras 10, entities 24) | 721 / 721 |
| Press release | work/ledger_pressrelease_indorama_q2fy27.md | 132 (R001-R132) | 132 | none | gate_a2 pass (3 pages/slides, 6 table line items, 0 notes) | 132 / 132 |
| Capex Board Outcome | work/ledger_capex_indorama_q2fy27.md | 47 (R001-R047) | 47 | none | gate_a2 pass (0 notes, 1 agenda item, 12 entities) | 47 / 47 |

Notes = 12 (8 numbered Notes 1-4 in each of the standalone and consolidated filings, plus 4 table-heading Note labels R696, R697, R712, R713). Slides = 3 press-release pages. Turns = 0 (no concall). The capex letter has 0 notes and 1 agenda item.

**Findings incorporated:** A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16 (results); PR-FN-01, PR-FN-02, PR-FN-03, PR-FN-04, PR-FN-05, PR-FN-06, PR-FN-07, PR-FN-08 (press release); CX-FN-01, CX-FN-02, CX-FN-03, CX-FN-04, CX-FN-05, CX-FN-06 (capex). Body anchors for the NEUTRAL-FACT findings: A3-02 (5C), A3-03 (5A), A3-07 (5C), A3-13 (0D), A3-15 (0D), PR-FN-07 (preamble, 1E), PR-FN-08 (1E), CX-FN-06 (0D).

FORWARD-SIGNAL findings routed to questions: A3-09, PR-FN-01, PR-FN-02, CX-FN-01, CX-FN-02. AMBIGUOUS findings routed to questions: A3-01, A3-04, A3-05, A3-06, A3-08, A3-10, A3-11, A3-12, A3-14, A3-16, PR-FN-03, PR-FN-04, PR-FN-05, PR-FN-06, CX-FN-03, CX-FN-04, CX-FN-05. Mapping is in the Step 8.5 table.

A1 data notes carried from A3 and the orchestrator. Checked; none changes an analytic number:
- R145 and R478 carry the label "Other equity, H1 FY26". Values 302.65 (S) and 258.06 (C) equal the 31-Mar-2026 balance sheet other equity (RF L309, L699). This review treats them as 31-Mar-2026 figures.
- R640 truncates the consolidated auditor FRN. RF L520 reads "000756N/N500441", the same as the standalone report (RF L134).
- The press-release table value "246" for Q2 FY26 PAT (PR L104) is a lost decimal. The body text reads 24.6 (PR L120), and the filing reads 24.55 (RF L609). This review uses 24.55 (PR-FN-07).

---

## ROLE 4 STEP 0: PRE-FLIGHT

### 0A. Notion fetch and Decision Status

| Field | Value | Source |
|---|---|---|
| Notion page | NONE (live search 2026-10-17 returned no COMPANIES MASTER page) | notion-thesis.md L3-5 |
| **Decision Status** | **NOT ON RECORD** | notion-thesis.md L7 |
| One-line thesis | ND (not passed) | notion-thesis.md L8-9 |
| Four-pillar destination PE | ND | notion-thesis.md L9 |
| Bear/Base/Bull projections | ND | notion-thesis.md L8 |
| Thesis-broken conditions | ND | notion-thesis.md L8 |
| Monitoring checklist | ND | notion-thesis.md L8 |
| Position size / cost basis | ND (no position on record) | notion-thesis.md L7 |
| Devil's Advocate split | ND | no page |
| Prior-quarter Questions table | ND (first review) | notion-thesis.md L10 |
| Prior promise log | ND | notion-thesis.md L10 |
| Spear line | none on record | notion-thesis.md L11 |
| Tracker rows | not supplied | notion-thesis.md L12 |

Decision Status was verified before any position framing. This review uses no HOLD, ADD, TRIM or EXIT language. The 8A-W branch (non-held) applies.

Prior-quarter answer tracking (protocol non-negotiable): no prior Questions-for-Management table exists, so every question below is first-asked this quarter. Status ND for all.

### 0B. Unit convention
"(Rs in crores, unless otherwise stated)" (RF L153 standalone P&L; RF L535 consolidated P&L; RF L225, L326, L625, L717 statement headings). Press release: Rs crore, per its body text (PR L110 "crore"; the table glyph is garbled, PR L94). Capex letter: "INR 200 Crores" (CX L39). **Conversion factor: x1. All figures are Rs crore.** EPS in Rs.

### 0C. Share count changes
Paid-up equity is 261.11 at face value Rs 10 in all six P&L columns, S and C (RF L219, L619). That is 26.111 crore shares. Balance sheet equity capital is 261.11 at both dates (RF L308, L698). Basic EPS equals diluted EPS in all 24 EPS cells (RF L221-222, L621-622). No split, bonus, rights issue, QIP, ESOP or buyback is disclosed in any period. Reported EPS = share-adjusted EPS. No warrant or ESOP appears in the board outcome (RF L45-61) or the capex letter (CX L36-44).

### 0D. Notes extraction (full)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| S Note 1 (RF L415-417) | Basis of preparation | Ind AS under Section 133 and Reg 33. | nil | all | none |
| S Note 2 (RF L419-421) | Approval and review | Audit Committee reviewed and Board approved on 16 Oct 2026; auditors did a limited review. | nil | Q2/H1 FY27 | none; limited review, not audit |
| S Note 3 (RF L423-426) | Segment | One reportable segment: "manufacturing and trading of polyester goods". | nil | all | no product or geography split; spread per product cannot be read |
| S Note 4 (RF L428-429) | Reference | Directs readers to the website and exchange sites. | nil | n/a | none |
| S BS label "Notes:1" (RF L225) | Statement of assets and liabilities | Heading only. | nil | 30-Sep-2026, 31-Mar-2026 | none |
| S CF label "Note:2" (RF L326) | Statement of cash flows | Heading only; indirect method, H1 FY27 vs H1 FY26. | nil | H1 | enables the Q2 cash check |
| C Note 1 (RF L805) | Basis of preparation | Ind AS, Section 133, Reg 33. | nil | all | none |
| C Note 2 (RF L812) | Consolidation and approval | Ind AS 110; Audit Committee review, Board approval 16 Oct 2026; limited review. | nil | Q2/H1 FY27 | none |
| C Note 3 (RF L819) | Segment | Group has one reportable segment: polyester goods. | nil | all | as S Note 3 |
| C Note 4 (RF L822) | Reference | Website and exchange sites. | nil | n/a | none |
| C BS label "Note No. 1" (RF L625) | Statement of assets and liabilities | Heading only. | nil | both dates | none |
| C CF label "Note No. 2" (RF L717) | Statement of cash flows | Heading only. | nil | H1 | none |
| (P&L line, not a note) RF L211 / L605 | Exceptional item: employee benefit expenses | FY26 carries a charge of 2.69 (S) / 2.70 (C); every other column is nil, so the charge fell in H2 FY26 (A3-01). | 2.69 S / 2.70 C | H2 FY26 | Q2 YoY and QoQ comparisons are clean; the FY26 column is depressed by 2.70 (C); normalised FY26 C PBT = 152.91 (RF L604) |
| (Board outcome) RF L57-59 | Item b heading | Heading says "Audited", body says "Un-audited" (A3-13). | nil | n/a | none; template carryover |
| (Review report) RF L460-461 vs L506-509 | Consolidation perimeter wording | Para 1 says "its subsidiary" (singular); para 4 lists four subsidiaries (A3-14, A3-16). | nil | n/a | perimeter history unverifiable (prior list ND) |
| (Drafting) RF L225, L326 vs L415, L419; RF L63 | Duplicate note numbering; time format | "Note 1" and "Note 2" each label a statement and also a numbered note. The meeting close reads "14:35 PM IST" (A3-15). | nil | n/a | none; cosmetic, counted in the governance drafting tally |
| (Drafting, capex letter) CX L18, L31, L36 | Reference serial; regulation wording | Reference "IRSL: STEXCH:2026-27:" ends with no serial. Subject says "Regulations 30"; body says "Regulation 30" (CX-FN-06). | nil | n/a | none; cosmetic, counted in the governance drafting tally |

Governance drafting tally for this quarter: four cosmetic slips (A3-13, A3-15, CX-FN-06, and the singular "its subsidiary" in A3-14). None changes a number. The tally is a data point for a later Promoter Verdict, not a finding on its own.

Answers to the four note questions:
- No note changes how a Q2 YoY or QoQ comparison reads. The only one-off (the H2 FY26 exceptional of 2.70 C) sits outside the compared quarters.
- No normalisation is needed for Q2 FY27 vs Q2 FY26 or vs Q1 FY27. The FY26 column is normalised only where stated.
- Recurring vs one-off: the notes classify nothing. The P&L template carries a separate "Foreign exchange fluctuation loss" line (RF L208, L602). This review treats it as volatile, not recurring (Step 4).
- Thesis-relevant disclosure: the one-segment note (S Note 3, C Note 3) means spread, volume and mix are not disclosed anywhere in the filing. The tax lines (nil, RF L213-214) are the material thesis disclosure (A3-09, Step 4).

**Auditor opinion check.** Standalone: limited review under SRE 2410. Unmodified conclusion: "nothing has come to our attention ... material misstatement" (RF L124-130). Consolidated: unmodified conclusion (RF L510-517). The consolidated review also ran SEBI Reg 33(8) circular procedures (RF L487-489). Neither report carries an Emphasis of Matter, Going Concern or Other Matter paragraph (A3 F4, F5 PASS). Auditor: S S Kothari Mehta & Co. LLP, FRN 000756N/N500441 (RF L134, L520), partner Vijay Kumar, M.No. 092671 (RF L141, L525). **Status: unmodified; no EoM. No AMBER flag from the auditor.** This is a limited review, not an audit, in every column except FY26 (RF L152, L534).

### 0E. Business type
**Standard operating business** (manufacturing and trading of polyester goods, RF L425-426). Steps 1 and 5 apply, not 1L/5L. Archetype candidate for /fttcp: Commodity converter (Section 1B v3.7 Amendment 17). The basis is the spread-driven cost structure (materials plus traded goods are 77.4% of Q2 C revenue, d: (944.32+116.22-22.94)/1,340.64, RF L593-595, L590) and the CMD's crude-cost attribution (PR L130-131). The classification belongs to /fttcp. This review flags it only (see Step 7).

**Checkpoint.** Notion verified (no page; Decision Status NOT ON RECORD). Units Rs crore x1. No share-count change. 12 notes extracted. Auditor unmodified. Standard business.

---

## STEP 1: DATA EXTRACTION TABLES

The protocol column FY[YY] = FY27 is not complete, so it is ND. H1 FY26 and H1 FY27 columns are added because H1 is the last reported cumulative period. Every cell is from the anchor line in the right-hand column.

### 1A. CONSOLIDATED (RF L590-622, image-verified)

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 1,220.64 | 936.64 | 1,340.64 | 4,910.06 | ND | 2,526.35 | 2,277.28 | RF L590 |
| Other Income | 1.71 | 3.56 | 3.40 | 18.95 | ND | 4.56 | 6.96 | RF L591 |
| Total Income | 1,222.35 | 940.20 | 1,344.04 | 4,929.01 | ND | 2,530.91 | 2,284.24 | RF L592 |
| Cost of Materials Consumed | 931.31 | 584.61 | 944.32 | 3,533.96 | ND | 1,754.02 | 1,528.93 | RF L593 |
| Purchase of Stock-in-Trade | 78.76 | 48.30 | 116.22 | 196.60 | ND | 161.16 | 164.52 | RF L594 |
| Change in Inventories | (69.94) | 62.14 | (22.94) | 36.21 | ND | (4.53) | 39.20 | RF L595 |
| Employee Benefits Expense | 32.38 | 30.97 | 31.53 | 125.31 | ND | 65.79 | 62.50 | RF L596 |
| Finance Costs | 33.57 | 29.38 | 28.99 | 130.31 | ND | 62.60 | 58.37 | RF L601 |
| Depreciation | 11.98 | 12.01 | 12.30 | 47.76 | ND | 23.91 | 24.31 | RF L600 |
| Other Expenses | 169.46 | 106.14 | 157.25 | 668.68 | ND | 333.82 | 263.39 | RF L597 |
| Foreign exchange fluctuation loss (separate line) | 10.28 | 2.91 | 2.51 | 37.27 | ND | 16.84 | 5.42 | RF L602 |
| Total Expenses | 1,197.80 | 876.46 | 1,270.18 | 4,776.10 | ND | 2,453.61 | 2,146.64 | RF L603 |
| Exceptional items (employee benefit) | - | - | - | 2.70 | ND | - | - | RF L605 |
| Profit Before Tax | 24.55 | 63.74 | 73.86 | 150.21 | ND | 77.30 | 137.60 | RF L606 |
| Tax Expense (current) | - | - | - | - | ND | - | - | RF L607 |
| Deferred tax (credit) | - | - | (0.22) | - | ND | - | (0.22) | RF L608 |
| PAT | 24.55 | 63.74 | 74.08 | 150.21 | ND | 77.30 | 137.82 | RF L609 |
| PAT attributable to owners | 24.55 | 63.74 | 74.08 | 150.21 | ND | 77.30 | 137.82 | RF L613 |
| EPS (reported, basic = diluted, Rs) | 0.94 | 2.44 | 2.84 | 5.75 | ND | 2.96 | 5.28 | RF L621-622 |
| EPS (share-adjusted, Rs) | 0.94 | 2.44 | 2.84 | 5.75 | ND | 2.96 | 5.28 | RF L621 (no share change, RF L619) |

Filed subtotal "Profit from operations before D&A, finance costs and FX loss/(gain)" (C): 80.38 / 108.04 / 117.66 / 368.25 / ND / 180.65 / 225.70 (RF L599). This is the press release's "EBITDA" (PR L98). It includes other income and excludes the FX loss.

### 1B. STANDALONE (RF L196-222, image-verified)

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 | Anchor |
|---|---|---|---|---|---|---|---|---|
| Revenue from Operations | 1,166.29 | 817.91 | 1,248.33 | 4,518.73 | ND | 2,351.23 | 2,066.24 | RF L196 |
| Other Income | 3.64 | 6.85 | 5.82 | 27.52 | ND | 8.37 | 12.67 | RF L197 |
| Total Income | 1,169.93 | 824.76 | 1,254.15 | 4,546.25 | ND | 2,359.60 | 2,078.91 | RF L198 |
| Cost of Materials Consumed | 938.30 | 588.21 | 942.04 | 3,523.97 | ND | 1,816.98 | 1,530.25 | RF L199 |
| Purchase of Stock-in-Trade | 4.05 | 17.45 | 42.11 | 17.33 | ND | 12.11 | 59.56 | RF L200 |
| Change in Inventories | (23.30) | 31.92 | 17.98 | 29.14 | ND | 39.50 | 49.90 | RF L201 |
| Employee Benefits Expense | 30.93 | 29.59 | 30.12 | 119.42 | ND | 62.83 | 59.71 | RF L202 |
| Finance Costs | 28.74 | 25.79 | 25.65 | 111.19 | ND | 52.16 | 51.44 | RF L207 |
| Depreciation | 9.59 | 9.63 | 9.87 | 38.24 | ND | 19.15 | 19.50 | RF L206 |
| Other Expenses | 148.75 | 85.37 | 128.76 | 556.10 | ND | 285.16 | 214.13 | RF L203 |
| Foreign exchange fluctuation loss (separate line) | 9.83 | 3.05 | 2.57 | 36.14 | ND | 16.36 | 5.62 | RF L208 |
| Total Expenses | 1,146.89 | 791.01 | 1,199.10 | 4,433.53 | ND | 2,304.25 | 1,990.11 | RF L209 |
| Exceptional items (employee benefit) | - | - | - | 2.69 | ND | - | - | RF L211 |
| Profit Before Tax | 23.04 | 33.75 | 55.05 | 110.03 | ND | 55.35 | 88.80 | RF L212 |
| Tax Expense (current + deferred) | - | - | - | - | ND | - | - | RF L213-214 |
| PAT | 23.04 | 33.75 | 55.05 | 110.03 | ND | 55.35 | 88.80 | RF L215 |
| EPS (reported, basic = diluted, Rs) | 0.88 | 1.29 | 2.11 | 4.21 | ND | 2.12 | 3.40 | RF L221-222 |
| EPS (share-adjusted, Rs) | 0.88 | 1.29 | 2.11 | 4.21 | ND | 2.12 | 3.40 | RF L221 (no share change, RF L219) |

Filed subtotal "Profit from operations before D&A, finance costs and FX" (S): 71.20 / 72.22 / 93.14 / 298.29 / ND / 143.02 / 165.36 (RF L205).

### 1C. DERIVED METRICS: CONSOLIDATED

Operating EBITDA uses the protocol formula (PBT + D + Finance Costs - Other Income). The filing reports FX loss on a separate line, so the protocol formula keeps the FX loss inside operating EBITDA. A pre-FX variant is shown so neither reading is hidden.

| Derived Metric | Formula (anchors) | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI (RF L606, L600, L601, L591) | 68.39 | 101.57 | 111.75 | 309.33 | ND | 159.25 | 213.32 |
| Operating EBITDA Margin | Op EBITDA / Rev (L590) | 5.60% | 10.84% | 8.34% | 6.30% | ND | 6.30% | 9.37% |
| Operating EBITDA pre-FX (variant) | Filed L599 - OI L591 | 78.67 | 104.48 | 114.26 | 349.30 | ND | 176.09 | 218.74 |
| Operating EBITDA pre-FX Margin | / Rev (L590) | 6.44% | 11.15% | 8.52% | 7.11% | ND | 6.97% | 9.61% |
| Reported EBITDA | PBT + D + FC (L606, L600, L601) | 70.10 | 105.13 | 115.15 | 328.28 | ND | 163.81 | 220.28 |
| Core PBT (ex-Other Income) | PBT - OI (L606, L591) | 22.84 | 60.18 | 70.46 | 131.26 | ND | 72.74 | 130.64 |
| Other Income / PBT | OI / PBT (L591, L606) | 7.0% | 5.6% | 4.6% | 12.6% | ND | 5.9% | 5.1% |
| Effective Tax Rate | (L607 + L608) / PBT (L606) | 0.0% | 0.0% | -0.30% | 0.0% | ND | 0.0% | -0.16% |
| PAT Margin (on Revenue) | PAT (L609) / Rev (L590) | 2.01% | 6.81% | 5.53% | 3.06% | ND | 3.06% | 6.05% |
| Gross margin (A4 add: spread proxy) | (Rev - L593 - L594 - L595) / Rev | 22.98% | 25.79% | 22.60% | 23.28% | ND | 24.37% | 23.92% |
| Gross profit (A4 add) | Rev - L593 - L594 - L595 | 280.51 | 241.59 | 303.04 | 1,143.29 | ND | 615.70 | 544.63 |

FY26 operating EBITDA (309.33) is after the 2.70 exceptional because PBT (RF L606) is post-exceptional. Ex-exceptional: 312.03 (d: 368.25 - 18.95 - 37.27, RF L599, L591, L602).

### 1D. DERIVED METRICS: STANDALONE

| Derived Metric | Formula (anchors) | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI (RF L212, L206, L207, L197) | 57.73 | 62.32 | 84.75 | 231.94 | ND | 118.29 | 147.07 |
| Operating EBITDA Margin | / Rev (L196) | 4.95% | 7.62% | 6.79% | 5.13% | ND | 5.03% | 7.12% |
| Operating EBITDA pre-FX (variant) | Filed L205 - OI L197 | 67.56 | 65.37 | 87.32 | 270.77 | ND | 134.65 | 152.69 |
| Operating EBITDA pre-FX Margin | / Rev (L196) | 5.79% | 7.99% | 7.00% | 5.99% | ND | 5.73% | 7.39% |
| Reported EBITDA | PBT + D + FC (L212, L206, L207) | 61.37 | 69.17 | 90.57 | 259.46 | ND | 126.66 | 159.74 |
| Core PBT (ex-Other Income) | PBT - OI (L212, L197) | 19.40 | 26.90 | 49.23 | 82.51 | ND | 46.98 | 76.13 |
| Other Income / PBT | OI / PBT (L197, L212) | 15.8% | 20.3% | 10.6% | 25.0% | ND | 15.1% | 14.3% |
| Effective Tax Rate | Tax (L213-214) / PBT (L212) | 0.0% | 0.0% | 0.0% | 0.0% | ND | 0.0% | 0.0% |
| PAT Margin (on Revenue) | PAT (L215) / Rev (L196) | 1.98% | 4.13% | 4.41% | 2.44% | ND | 2.35% | 4.30% |
| Gross margin (A4 add) | (Rev - L199 - L200 - L201) / Rev | 21.20% | 22.05% | 19.72% | 20.99% | ND | 20.53% | 20.64% |
| Gross profit (A4 add) | Rev - L199 - L200 - L201 | 247.24 | 180.33 | 246.20 | 948.29 | ND | 482.64 | 426.53 |

### 1E. Press release reconciliation to the filing (cross-document)

| Press release line (PR) | PR value | Filing equivalent | Filing value (RF) | Reconciles? | Note |
|---|---|---|---|---|---|
| Total Income Q2 FY27 (L96) | 1,344.0 | Total income C | 1,344.04 (L592) | yes | PR headline "Revenue Growth of 10%" (L75) is Total Income growth (PR-FN-04) |
| Total Income Q2 FY26 (L96) | 1,222.4 | Total income C | 1,222.35 (L592) | yes | Revenue from operations YoY is +9.83% (d: 1,340.64 / 1,220.64, L590) |
| EBITDA Q2 FY27 (L98) | 117.7 | Profit from ops before D&A, FC and FX | 117.66 (L599) | yes | Includes OI 3.40 (L591), excludes FX loss 2.51 (L602) |
| EBITDA Q2 FY26 (L98) | 80.4 | same | 80.38 (L599) | yes | |
| EBITDA Q1 FY27 (L98) | 108.0 | same | 108.04 (L599) | yes | |
| EBITDA margin Q2 FY27 (L100) | 8.8% | Filed L599 / Total income L592 | 8.75% (d) | yes | PR margins are on Total Income, not revenue |
| EBIT Q2 FY27 (L102) | 102.9 | L599 - D&A L600 - FX L602 | 102.85 (d) | yes | PR "EBIT" deducts FX loss. **Resolves PR-FN-05:** the implied "D&A" of 14.8 is D&A 12.30 + FX 2.51; Q2 FY26 22.3 is 11.98 + 10.28. D&A rose 2.67% YoY. The fall is in the FX loss. |
| EBIT Q2 FY26 (L102) | 58.1 | same | 58.12 (d) | yes | |
| EBIT Q1 FY27 (L102) | 93.1 | same | 93.12 (d) | yes | |
| EBIT H1 FY27 / H1 FY26 (L102) | 196.0 / 139.9 | same | 195.97 / 139.90 (d) | yes | |
| PAT Q2 FY27 (L104) | 74.1 | PAT C | 74.08 (L609) | yes | |
| PAT Q2 FY26 (L104 / L120) | "246" / 24.6 | PAT C | 24.55 (L609) | yes (24.6) | PR-FN-07: glyph loss |
| EBIT - PAT Q2 FY27 (L102, L104) | 28.8 (d) | FC L601 + tax L607-608 | 28.99 - 0.22 = 28.77 | yes | **Resolves PR-FN-06 as Reading A:** nil current tax (RF L607), not a finance-cost collapse |
| H1 Total Income change (L96) | -9.7% | Total income C H1 | -9.75% (d: 2,284.24 / 2,530.91, L592) | yes | Revenue from operations H1: -9.86% (d, L590) |
| Highlight cards (L85, L89) | 1,344 / 118 / 74 Cr; "Yoy" labels with no legible % | Total income / L599 / PAT | 1,344.04 / 117.66 / 74.08 | yes (rounded) | PR-FN-08: card YoY percentages absent from the text layer; the table at L96-104 carries them. Reviewed, no change to the review. |

**Checkpoint.** Extraction tables complete. Every cell is anchored or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26)

### 2A. Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from Operations (L590) | 1,220.64 | 1,340.64 | +120.00 / +9.83% | Growth off a weak base: Q2 FY26 was 6.52% below Q1 FY26 (Step 3) |
| Operating EBITDA (d, protocol) | 68.39 | 111.75 | +43.36 / +63.40% | Strong; 7.77 of the 43.36 (17.9%) is the FX-loss swing |
| Operating EBITDA pre-FX (d) | 78.67 | 114.26 | +35.59 / +45.24% | Strong, but gross profit supplied only 22.53 of it (Step 4) |
| Operating EBITDA Margin (pp change) | 5.60% | 8.34% | +273 bp | Expanded YoY; contracted -251 bp QoQ (10.84% in Q1 FY27) |
| Gross margin (d) | 22.98% | 22.60% | -38 bp | **Spread proxy did not widen YoY** (A4-01) |
| Depreciation (L600) | 11.98 | 12.30 | +0.32 / +2.67% | Steady; no absorption deficit |
| Finance Costs (L601) | 33.57 | 28.99 | -4.58 / -13.64% | Falling with debt repayment |
| EBIT (operating) = Op EBITDA - D (d) | 56.41 | 99.45 | +43.04 / +76.30% | Strong |
| Other Income (L591) | 1.71 | 3.40 | +1.69 / +98.83% | Immaterial at 4.6% of PBT |
| **Core Operating PBT (PBT - OI)** (d) | 22.84 | 70.46 | +47.62 / +208.49% | Real at pre-tax level, but measured off the trough quarter: +41.20% vs Q1 FY26 (49.90) |
| Reported PBT (L606) | 24.55 | 73.86 | +49.31 / +200.86% | |
| PAT (L609) | 24.55 | 74.08 | +49.53 / +201.75% | Pre-tax-equivalent: current tax nil |
| EPS share-adjusted (L621) | 0.94 | 2.84 | +1.90 / +202.13% | Nil tax; statutory-rate Q2 EPS 2.12 (d, Step 4) |

### 2B. Standalone

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from Operations (L196) | 1,166.29 | 1,248.33 | +82.04 / +7.03% | Modest |
| Operating EBITDA (d) | 57.73 | 84.75 | +27.02 / +46.80% | Driven by other expenses (-19.99) and FX (-7.26), not gross profit |
| Operating EBITDA pre-FX (d) | 67.56 | 87.32 | +19.76 / +29.25% | |
| Operating EBITDA Margin (pp change) | 4.95% | 6.79% | +184 bp | Expanded YoY; -83 bp QoQ (7.62% in Q1 FY27) |
| Gross margin (d) | 21.20% | 19.72% | -148 bp | **Standalone gross profit fell 1.04 on +7.03% revenue** (A4-02) |
| Depreciation (L206) | 9.59 | 9.87 | +0.28 / +2.92% | Steady |
| Finance Costs (L207) | 28.74 | 25.65 | -3.09 / -10.75% | Falling |
| EBIT (operating) (d) | 48.14 | 74.88 | +26.74 / +55.55% | |
| Other Income (L197) | 3.64 | 5.82 | +2.18 / +59.89% | Includes interest from subsidiaries (S H1 interest income 5.95 vs C 3.60, RF L378, L771) |
| **Core Operating PBT** (d) | 19.40 | 49.23 | +29.83 / +153.76% | |
| Reported PBT (L212) | 23.04 | 55.05 | +32.01 / +138.93% | |
| PAT (L215) | 23.04 | 55.05 | +32.01 / +138.93% | Nil tax |
| EPS share-adjusted (L221) | 0.88 | 2.11 | +1.23 / +139.77% | |

### 2C. H1 YoY (supplementary; H1 FY27 vs H1 FY26)

| Metric | C H1 FY26 | C H1 FY27 | C change | S H1 FY26 | S H1 FY27 | S change |
|---|---|---|---|---|---|---|
| Revenue from Operations (L590 / L196) | 2,526.35 | 2,277.28 | -249.07 / -9.86% | 2,351.23 | 2,066.24 | -284.99 / -12.12% |
| Operating EBITDA (d) | 159.25 | 213.32 | +54.07 / +33.95% | 118.29 | 147.07 | +28.78 / +24.33% |
| Op EBITDA margin (d) | 6.30% | 9.37% | +307 bp | 5.03% | 7.12% | +209 bp |
| Core PBT (d) | 72.74 | 130.64 | +57.90 / +79.60% | 46.98 | 76.13 | +29.15 / +62.05% |
| PAT (L609 / L215) | 77.30 | 137.82 | +60.52 / +78.29% | 55.35 | 88.80 | +33.45 / +60.43% |
| EPS (L621 / L221) | 2.96 | 5.28 | +78.38% | 2.12 | 3.40 | +60.38% |

### 2D. Six diagnostic answers

1. **Did revenue grow YoY?** Yes. C revenue rose 9.83% (1,220.64 to 1,340.64) and S rose 7.03%. No company guidance and no base case exist (ND), so no comparison to an implied target is possible. H1 C revenue fell 9.86%. Q2 growth is measured against a Q2 FY26 that was already 6.52% below Q1 FY26.
2. **Margin expansion?** C operating EBITDA margin Q2 FY27 8.34% vs Q2 FY26 5.60% = +273 bp YoY. Sequential Q1 to Q2: 10.84% to 8.34% = -251 bp. On the pre-FX variant: 6.44% to 8.52% (+208 bp YoY) and 11.15% to 8.52% (-263 bp QoQ). C gross margin moved 22.98% to 22.60% (-38 bp YoY) and 25.79% to 22.60% (-319 bp QoQ).
3. **Did core operating PBT grow YoY?** Yes. C core PBT rose from 22.84 to 70.46 (+208.49%); S from 19.40 to 49.23 (+153.76%). The headline is real at the pre-tax level. It is pre-tax-equivalent at the PAT level, because current tax is nil. **Base caveat (A5 M3):** Q2 FY26 is the trough quarter of the derivable sequence. Against Q1 FY26 core PBT of 49.90 (d: 72.74 - 22.84, RF L606, L591), Q2 FY27 is +41.20% (70.46 / 49.90), not +208.49%. Of the 47.62 YoY rise, 7.77 (16.32%) is the FX-loss swing that Step 4 classes as non-recurring. Another 13.06 is opex of undisclosed composition (RF L596-597). Gross profit supplied 22.53.
4. **Gap between core PBT growth and reported PAT growth (C)?** Core PBT +47.62; other income +1.69; deferred tax credit +0.22; exceptional 0. Total +49.53 = reported PAT change. The gap is small. The large hidden item is tax: at the 25.17% rate A3 uses, Q2 C PAT would be 55.27, not 74.08 (d: 73.86 x 0.7483).
5. **Are D&A and finance costs scaling faster than revenue?** No. D&A +2.67% and finance cost -13.64% against revenue +9.83%. No absorption deficit. H1 capex was 9.83 (RF L785), so no new plant is being absorbed.
6. **Other income concentration?** No distortion. Q2 OI is 3.40 vs 3.56 in Q1. C OI/PBT is 4.6%. FY26 OI of 18.95 was H2-weighted: H2 FY26 had 14.39 (d: 18.95 - 4.56), so FY26 comparisons carry more treasury income than any FY27 quarter.

**Checkpoint.** YoY tables and diagnostics complete.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

Q3 FY26 and Q4 FY26 are not reported individually in this filing, so they are ND. H2 FY26 is derived (FY26 minus H1 FY26) and shown as a two-quarter block with its per-quarter average. Q1 FY26 is derived (H1 FY26 minus Q2 FY26).

### 3A. Consolidated

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI) | Gross margin (d) | Other exp / revenue (d) | One-offs Flagged | QoQ Run-Rate (revenue) |
|---|---|---|---|---|---|---|---|
| Q1 FY26 (d: H1 minus Q2; L590, L593-597, L600-602, L606) | 1,305.71 | 6.96% (90.86) | 49.90 | 25.67% (335.19) | 12.59% (164.36) | none in template; FX loss 6.56 (d, L602) | ND (Q4 FY25 not in filing) |
| Q2 FY26 (L590 etc.) | 1,220.64 | 5.60% (68.39) | 22.84 | 22.98% | 13.88% | FX loss 10.28 (L602) | -6.52% vs Q1 FY26 |
| Q3 FY26 | ND | ND | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND | ND | ND |
| H2 FY26 two-quarter block (d: FY26 minus H1 FY26) | 2,383.71 (avg 1,191.86/qtr) | 6.30% (150.08) | 58.52 (avg 29.26/qtr) | 22.13% (527.59) | 14.05% (334.86) | exceptional 2.70 (L605); OI 14.39 (d) | avg -2.36% vs Q2 FY26 |
| Q1 FY27 (L590 etc.) | 936.64 | 10.84% (101.57) | 60.18 | 25.79% | 11.33% | MGMT: Middle East supply-chain disruption (PR L112-113) | -21.41% vs H2 FY26 avg; -28.27% YoY vs Q1 FY26 |
| Q2 FY27 (L590 etc.) | 1,340.64 | 8.34% (111.75) | 70.46 | 22.60% | 11.73% | FX loss 2.51 (L602); deferred tax credit 0.22 (L608) | +43.13% vs Q1 FY27; +2.68% vs Q1 FY26 |

### 3B. Standalone

| Quarter | Revenue (Rs Cr) | Op EBITDA Margin | Core PBT (ex-OI) | One-offs Flagged | QoQ Run-Rate (revenue) |
|---|---|---|---|---|---|
| Q1 FY26 (d) | 1,184.94 | 5.11% (60.56) | 27.58 | FX loss 6.53 (d, L208) | ND |
| Q2 FY26 (L196 etc.) | 1,166.29 | 4.95% (57.73) | 19.40 | FX loss 9.83 (L208) | -1.57% vs Q1 FY26 |
| Q3 FY26 | ND | ND | ND | ND | ND |
| Q4 FY26 | ND | ND | ND | ND | ND |
| H2 FY26 block (d) | 2,167.50 (avg 1,083.75/qtr) | 5.24% (113.65) | 35.53 (avg 17.77/qtr) | exceptional 2.69 (L211); OI 19.15 (d) | avg -7.08% vs Q2 FY26 |
| Q1 FY27 (L196 etc.) | 817.91 | 7.62% (62.32) | 26.90 | MGMT supply disruption (PR L112-113) | -24.53% vs H2 FY26 avg |
| Q2 FY27 (L196 etc.) | 1,248.33 | 6.79% (84.75) | 49.23 | FX loss 2.57 (L208) | +52.62% vs Q1 FY27 |

### 3C. Diagnostics
- **Trajectory: a dip and a recovery, not a staircase.** The full derivable C core-PBT sequence is 49.90 (Q1 FY26), 22.84 (Q2 FY26), 29.26 (H2 FY26 per-quarter average), 60.18 (Q1 FY27), 70.46 (Q2 FY27). The last two readings are the highest. The earlier run fell to a trough before it recovered (A5 M5). C revenue recovered from a disrupted Q1 FY27 (936.64) to 1,340.64. That is only 2.68% above Q1 FY26 (1,305.71). H1 FY27 revenue is still -9.86% YoY. Op EBITDA margin fell from 10.84% to 8.34%. In absolute terms, operating EBITDA still rose 10.02% QoQ (101.57 to 111.75).
- **One-off distortion:** Q1 FY27 carried a revenue disruption that management attributes to the Middle East (PR L112-113, MGMT). Q1 FY27 also had the highest gross margin of any reported period (25.79%). **Q1 FY26 gross margin was almost the same, 25.67% (d), and fell 269 bp to 22.98% in Q2 FY26 with no crude attribution in the filings (A5 M1).** The Q1-to-Q2 FY27 drop of 319 bp may therefore be partly a recurring Q1-to-Q2 pattern. The YoY -38 bp is the cleaner spread read. Inventory gains on rising input prices may also play a part, but the filing does not disclose them [INFERENCE]. Q2 FY26 carried an FX loss of 10.28. H2 FY26 carried the 2.70 exceptional.
- **H1 run-rate test:** H1 FY27 C average quarterly revenue is 1,138.64 (d: 2,277.28 / 2). Q2 exceeds it by 17.74%. Q2 operating EBITDA (111.75) exceeds the H1 average (106.66). Q2 margin (8.34%) is below the H1 margin (9.37%). No capex was commissioned in the period (CWIP 42.03 to 38.45, RF L682), so the commissioning version of this test does not apply.
- **Implied Q3 FY27 base:** to keep the YoY trajectory, Q3 FY27 C revenue needs to clear the H2 FY26 per-quarter average of 1,191.86, and operating EBITDA needs to clear 75.04 (d: 150.08 / 2). To keep the sequential step-up, Q3 needs revenue of at least 1,340.64 and an operating EBITDA margin of at least 8.34%. Q3 FY26 alone is ND, so an exact YoY base is not available.

**Checkpoint.** QoQ tables and diagnostics complete.

---

## STEP 4: OPERATIONAL DECOMPOSITION (PAT BRIDGE)

### 4A. Consolidated, Q2 FY27 vs Q2 FY26 (PAT +49.53)

| Component | YoY Change (Rs Cr) | Share of PAT change | Recurring? | Anchor / math |
|---|---|---|---|---|
| Revenue contribution to gross profit | +27.58 | 55.68% | Recurring | d: +120.00 revenue x prior GM 22.98% (L590, L593-595) |
| Margin change contribution (gross margin) | -5.05 | -10.20% | Recurring (spread) | d: (22.60% - 22.98%) x 1,340.64 |
| Employee + other expenses change | +13.06 | 26.37% | Unknown: composition ND | d: employee 32.38 to 31.53 (+0.85, 1.72%), other expenses 169.46 to 157.25 (+12.21, 24.65%) (L596, L597) |
| FX fluctuation loss change | +7.77 | 15.69% | NON-RECURRING (volatile) | d: 10.28 to 2.51 (L602) |
| D&A change | -0.32 | -0.65% | Recurring (post-capex) | L600 |
| Finance cost change | +4.58 | 9.25% | Recurring (post-debt) | L601 |
| Other Income change | +1.69 | 3.41% | NON-RECURRING typically | L591 |
| Effective tax rate change | +0.22 | 0.44% | Mixed (deferred credit) | L608 |
| Exceptional items | 0.00 | 0.00% | NON-RECURRING | L605 (nil both quarters) |
| **Reported PAT YoY change** | **+49.53** | **100%** | | L609: 24.55 to 74.08 |

### 4B. Standalone, Q2 FY27 vs Q2 FY26 (PAT +32.01)

| Component | YoY Change (Rs Cr) | Share of PAT change | Recurring? | Anchor / math |
|---|---|---|---|---|
| Revenue contribution to gross profit | +17.39 | 54.33% | Recurring | d: +82.04 x prior GM 21.20% (L196, L199-201) |
| Margin change contribution (gross margin) | -18.43 | -57.58% | Recurring (spread) | d: (19.72% - 21.20%) x 1,248.33 |
| Employee + other expenses change | +20.80 | 64.98% | Unknown: composition ND | d: employee +0.81 (2.53%), other expenses 148.75 to 128.76 (+19.99, 62.45%) (L202, L203) |
| FX fluctuation loss change | +7.26 | 22.68% | NON-RECURRING | L208 |
| D&A change | -0.28 | -0.87% | Recurring | L206 |
| Finance cost change | +3.09 | 9.65% | Recurring | L207 |
| Other Income change | +2.18 | 6.81% | NON-RECURRING typically | L197 |
| Effective tax rate change | 0.00 | 0.00% | n/a (nil both) | L213-214 |
| Exceptional items | 0.00 | 0.00% | | L211 |
| **Reported PAT YoY change** | **+32.01** | **100%** | | L215: 23.04 to 55.05 |

**A4-01 (C) and A4-02 (S): the spread did not carry the quarter.** In C, gross profit added 22.53 (27.58 - 5.05). Lower other expenses (12.21), a smaller FX loss (7.77) and lower finance cost (4.58) added 24.56. Lower employee cost added 0.85 more, for 25.41 across the four cost lines. In S, gross profit fell 1.04 on 7.03% more revenue. All of the standalone PAT gain came from other expenses (-19.99), FX (-7.26), finance cost (-3.09) and other income (+2.18). The filing does not split other expenses, so the cause is ND. Power and fuel, freight and stores are the usual contents in polyester [INFERENCE].

**Comparators beside A4-01 (A5 M1; Rule J symmetric read).**
- C gross margin by period (d): Q1 FY26 25.67%, Q2 FY26 22.98%, H2 FY26 22.13%, Q1 FY27 25.79%, Q2 FY27 22.60%. The same Q1-to-Q2 fall happened in FY26 (-269 bp). The YoY move (-38 bp) is the cleaner read of the spread.
- C other expenses / revenue (d, RF L597 / L590): Q1 FY26 12.59%, Q2 FY26 13.88%, H2 FY26 14.05%, Q1 FY27 11.33%, Q2 FY27 11.73%.
- Two readings. (a) Durable saving: the lower ratio has now held for two quarters. (b) Denominator effect: revenue rose on price, not tonnes, so a volume-linked cost line fell as a share of revenue. **The separating observation is sales volume in tonnes (Q4 in Step 8.5).** Until volume is disclosed, neither reading is credited.

### 4C. Mandatory questions
- **Recurring vs non-recurring share (C):** revenue, gross margin, opex, D&A and finance cost together give +39.85 (80.46%). FX, other income and deferred tax give +9.68 (19.54%). Within the "recurring" block, the opex saving of 13.06 is unverified because the other-expenses composition is ND. Under conservative reading, the proven-recurring core is gross profit +22.53 plus finance cost +4.58 minus D&A 0.32, which is +26.79 (54.09% of the PAT change).
- **If Other Income reverts to the prior-year level (1.71):** Q2 C PAT = 72.39 (d: 74.08 - 1.69). If the FX loss also reverts to 10.28: 64.62 (d: 72.39 - 7.77). Against the trough Q2 FY26 PAT of 24.55 these are 2.95x and 2.63x. **Against the derived Q1 FY26 PAT of 52.75 (d: 77.30 - 24.55, RF L609), the fully reverted 64.62 is +22.50%, on the same nil-tax basis (A5 M5).** The second benchmark is the better guide to underlying progress.
- **D&A and finance cost steady-state:** D&A is steady at 11.98-12.30 a quarter (L600). Finance cost is falling with the 271.47 debt repayment in H1 (RF L790, L792). The Rs 200 cr specialty capex is to be "financed by taking term loan ... with mix of internal accrual" (CX L43-44). Interest on that loan will run ahead of revenue during the 12-18 month build (CX-FN-03). Finance cost is therefore near a trough, not at steady state.
- **Tax adjustments:** this is the largest issue. Standalone current and deferred tax are nil in all six periods on positive PBT (RF L213-214). The S deferred tax asset stayed at 258.61 at both dates (RF L295). The only C tax line is a 0.22 deferred credit (RF L608): C DTA rose 9.59 (RF L685) and a new C DTL of 9.37 appeared (RF L704) (A3-10). **Reported PAT carries a full tax shield.** At the 25.17% rate A3 uses (the Section 115BAA rate; whether the company has opted in is ND): Q2 FY27 C PAT 55.27, EPS 2.12; H1 FY27 C PAT 102.97, EPS 3.94 (reported 5.28); FY26 C PAT 112.40, EPS 4.30 (reported 5.75). All d: PBT x 0.7483 / 26.111. Reported EPS is 33.6% above the statutory-rate basis (d: 1 / 0.7483 - 1; H1 5.28 vs 3.94 = +34.0% on rounded EPS). The size and expiry of the unabsorbed-loss pool are NOT FOUND in this filing (A3-09).

**Checkpoint.** Bridges and answers complete.

---

## STEP 5: CASH QUALITY AND BALANCE SHEET (H1 cash flow and 30-Sep balance sheet are available at Q2; both used)

### 5A. Consolidated

| Metric | Prior period (H1 FY26 / 31-Mar-2026) | Current period (H1 FY27 / 30-Sep-2026) | Change | Verdict |
|---|---|---|---|---|
| CFO (RF L784) | 91.46 | 328.46 | +237.00 | Strong, but 109.02 is a working-capital release |
| CFO/PAT (L784 / L609) | 1.18x (91.46 / 77.30) | 2.38x (328.46 / 137.82) | +1.20x | Inflated by WC release and by finance cost sitting in financing |
| CFO ex-WC, after interest paid, / PAT (d: L784 - WC - L795) | 1.28x ((91.46 + 70.68 - 63.10) / 77.30) | 1.16x ((328.46 - 109.02 - 59.02) / 137.82) | -0.12x | Underlying conversion is adequate and slightly lower |
| Capex (PPE + CWIP) (L785) | (9.99) | (9.83) | +0.16 | Maintenance level only: 40.4% of H1 D&A of 24.31 (L768) |
| FCF (CFO - Capex) (d) | 81.47 | 318.63 | +237.16 | WC release supplies 109.02 of it |
| Working capital change (d: sum L774-L781) | (70.68) absorbed | +109.02 released | +179.70 | Receivables +140.26 (L774), offset by -31.24 in other WC lines |
| Receivable days (d: closing / period revenue x days) | 18.09 (243.32 / 4,910.06 x 365; L690, L590 FY) | 8.28 (103.06 / 2,277.28 x 183) | -9.81 days | Very low; factoring/discounting ND (A3-11) |
| Inventory days (d: closing / COGS x days; COGS = L593+L594+L595) | 64.62 (666.86 / 3,766.77 x 365) | 72.96 (690.81 / 1,732.65 x 183) | +8.34 days | Rising |
| Payable days (d: total trade payables L708+L709 / COGS x days) | 140.56 (1,450.59 / 3,766.77 x 365) | 154.42 (1,462.03 / 1,732.65 x 183) | +13.86 days | Very high; composition and cost ND (A3-12) |
| Cash Conversion Cycle (d) | -57.85 days | -73.18 days | -15.33 days | Negative CCC funded by supplier credit |
| PPE (L680) | 1,225.06 | 1,214.65 | -10.41 | D&A ran ahead of capex |
| CWIP (L682) | 42.03 | 38.45 | -3.58 | No major capitalisation |
| Gross borrowings (L701 + L706) | 1,131.60 | 860.13 | -271.47 (-23.99%) | Repayment only; no new term debt (A3-03, L791) |
| Cash + other bank balances (L691 + L692) | 18.26 | 8.26 | -10.00 | |
| Net Debt (ex-lease) (d) | 1,113.34 | 851.87 | -261.47 | **Funded 152.45 (58.3%) by pre-tax operating cash before WC, and 109.02 (41.7%) by the WC release.** At a 25.17% tax the split is about 52/48 (split below) |
| Net Debt incl. lease (d: + L702 + L707) | 1,121.61 | 858.80 | -262.81 | |
| Net debt / equity (d: / L700) | 2.14x (/ 519.17) | 1.30x (/ 656.99) | -0.84x | Book equity includes the net deferred tax asset (next rows) |
| Net deferred tax asset in equity (d: L685 - L704) | 258.61 (49.8% of 519.17) | 258.83 (39.4% of 656.99) | +0.22 | Its value rests on the loss pool that is NOT FOUND (A3-09) |
| Net debt / equity excluding net DTA (d) | 4.27x (1,113.34 / 260.56) | 2.14x (851.87 / 398.16) | -2.13x | Leverage on equity excluding the DTA is higher than the headline |
| Net debt / op EBITDA, H1 annualised (d) | 3.60x (/ FY26 309.33) | 2.00x (/ H1 213.32 x 2) | -1.60x | H1 carries the 10.84% Q1 FY27 margin |
| Net debt / op EBITDA, trailing 4 quarters (d: / TTM 363.40, Step 6.5) | 3.60x | 2.34x | -1.26x | **The steadier basis**; 2.89x if the full Rs 200 cr capex is debt-funded (1,051.87 / 363.40) |
| Op EBIT / finance cost, quarter (d) | 1.68x (Q2 FY26: 56.41 / 33.57) | 3.43x (Q2 FY27: 99.45 / 28.99) | +1.75x | |
| Promoter Pledge | ND | ND | ND | Not in filing |

**Net-debt fall, H1 FY27 (C), sources (d: RF L773-L797):**

| Source | Rs Cr | Share of the 261.47 fall | Anchor |
|---|---|---|---|
| Operating profit before WC changes | 216.73 | | L773 |
| Income tax refund | +2.71 | | L783 |
| Finance costs paid | -59.02 | | L795 |
| Capex net of interest received (net investing) | -6.24 | | L789 |
| Lease payments (principal + interest) | -1.73 | | L793-794 |
| **Operating cash before WC, after interest, capex and leases (pre-tax)** | **152.45** | **58.3%** | d |
| **Working-capital release** | **109.02** | **41.7%** | d: sum L774-L781 |
| of which receivables (gross) | 140.26 | 53.6% | L774 |
| of which other WC lines (net) | -31.24 | -11.9% | d |
| **Total = net-debt fall** | **261.47** | **100%** | 1,113.34 - 851.87 |
| Memo: operating cash after a 25.17% tax on H1 PBT 137.60 (d: 152.45 - 34.63) | 117.82 | 51.9% of 226.84 (vs WC 48.1%) | L606 |

**The 152.45 earned share is pre-tax cash (A5 M6).** Current tax is nil (RF L607), and H1 included a 2.71 income-tax refund (RF L783). At 25.17% on H1 PBT of 137.60, tax would be 34.63. The earned share would then be 117.82, and the split about 52/48 against the 109.02 WC release. H1 capex was 9.83, only 40.4% of H1 D&A of 24.31 (RF L785, L768). The earned share therefore also assumes maintenance-level reinvestment, before the Rs 200 cr build starts. Read this way, about half the deleveraging is earned at a normal tax rate and capex level. The other half is a receivable release that can reverse in H2.

### 5B. Standalone

| Metric | Prior period (H1 FY26 / 31-Mar-2026) | Current period (H1 FY27 / 30-Sep-2026) | Change | Verdict |
|---|---|---|---|---|
| CFO (RF L391) | 48.41 | 220.30 | +171.89 | WC release 62.71 |
| CFO/PAT (L391 / L215) | 0.87x (48.41 / 55.35) | 2.48x (220.30 / 88.80) | +1.61x | |
| CFO ex-WC, after interest paid, / PAT (d: L391 - WC - L403) | 1.29x ((48.41 + 75.86 - 52.64) / 55.35) | 1.19x ((220.30 - 62.71 - 52.08) / 88.80) | -0.10x | |
| Capex (L392) | (8.57) | (8.44) | +0.13 | Maintenance |
| FCF (d) | 39.84 | 211.86 | +172.02 | |
| Working capital change (d: sum L381-L388) | (75.86) | +62.71 | +138.57 | Receivables +94.09 (L381) |
| Loans from/(to) subsidiaries, net (L394) | (7.50) lent | 51.75 repaid by subsidiaries | +59.25 | S non-current loans 127.85 to 76.10 (L293) |
| Receivable days (d) | 30.67 (379.70 / 4,518.73 x 365) | 25.29 (285.60 / 2,066.24 x 183) | -5.38 days | At least 182.54 of 285.60 is intercompany (A3-06) |
| Inventory days (d; COGS = L199+L200+L201) | 61.02 (596.88 / 3,570.44 x 365) | 67.97 (609.01 / 1,639.71 x 183) | +6.95 days | |
| Payable days (d; L317+L318) | 141.15 (1,380.76 / 3,570.44 x 365) | 151.63 (1,358.65 / 1,639.71 x 183) | +10.48 days | |
| Cash Conversion Cycle (d) | -49.46 days | -58.37 days | -8.91 days | |
| PPE (L288) | 867.19 | 858.86 | -8.33 | |
| CWIP (L290) | 36.91 | 35.42 | -1.49 | |
| Gross borrowings (L311 + L315) | 943.98 | 719.42 | -224.56 | Repayment 17.58 + current movement 206.98 (L398, L400) |
| Net Debt ex-lease (d: less L301 + L302) | 932.05 | 716.31 | -215.74 | |
| Net debt / equity (d: / L310) | 1.65x | 1.10x | -0.55x | S equity includes DTA 258.61 (L295) at both dates |
| Promoter Pledge | ND | ND | ND | Not in filing |

### 5C. Standalone-vs-consolidated gap (first-class metric; from A3 F2, verified)

All subsidiary figures below are C-minus-S proxies, net of intercompany eliminations. They are not the subsidiaries' own reported numbers, which are not disclosed. Example of the elimination effect: S H1 interest income is 5.95 vs C 3.60 (RF L378, L771).

| Period | S PAT (L215) | C PAT (L609) | C - S | **Gap as % of S PAT** | Subsidiary proxy share of C PAT | Revenue gap (C - S) | EBITDA gap (filed L599 - L205) |
|---|---|---|---|---|---|---|---|
| Q2 FY27 | 55.05 | 74.08 | 19.03 | **34.6%** | 25.7% | 92.31 | 24.52 |
| Q1 FY27 | 33.75 | 63.74 | 29.99 | **88.9%** | 47.1% | 118.73 | 35.82 |
| Q2 FY26 | 23.04 | 24.55 | 1.51 | **6.6%** | 6.2% | 54.35 | 9.18 |
| H1 FY27 | 88.80 | 137.82 | 49.02 | **55.2%** | 35.6% | 211.04 | 60.34 |
| H1 FY26 | 55.35 | 77.30 | 21.95 | **39.7%** | 28.4% | 175.12 | 37.63 |
| FY26 | 110.03 | 150.21 | 40.18 | **36.5%** | 26.7% | 391.33 | 69.96 |

Gap moves: -54.3 pp QoQ, +28.0 pp YoY, +15.5 pp H1 on H1. Every move exceeds the 5 pp trigger (A3-04). The subsidiaries are net traders: the C-minus-S stock-in-trade proxy was 74.11 in Q2 FY27 (d: 116.22 - 42.11, L594, L200) (A3-05). They carry thin payroll, 1.41 a quarter on the proxy, against 355.79 of PPE (d: L596 - L202; L680 - L288) (A3-08). The S-minus-C receivables gap is 182.54 (d: 285.60 - 103.06, L300, L690). That gap is a lower bound on the intercompany receivable the parent holds (A3-06). IVYPL is named a "Wholly Owned Material Subsidiary" (CX L39-40). That confirms ownership for one of the four subsidiaries and supports A3-02 (NCI nil in every period, RF L614).

**Equity gap (A3-07).** At 31-Mar-2026, C other equity (258.06, RF L699) was 44.59 below S (302.65, RF L309). At 30-Sep-2026 it is 4.43 above (395.88 vs 391.45). H1 subsidiary proxy profit of 49.02 erased a cumulative subsidiary deficit or consolidation adjustment. The subsidiaries' profit run is recent, so their earnings history is short.

Balance-sheet blocks with no disclosed composition (A3-12): C other current financial assets 667.63 (21.3% of total assets 3,131.68; L694, L697). C trade payables 1,462.03 (46.7% of total assets). If the payables include acceptances or LC-backed credit, adjusted net debt would be higher than 851.87. The amount is ND.

### 5D. Mandatory questions
- **CFO/PAT vs Pillar 2 band:** no valuation exists, so no band is assumed (ND). Reported H1 C CFO/PAT is 2.38x. The ex-WC, after-interest reading is 1.16x C and 1.19x S. Band selection is deferred to /fttcp and Role 1 (OR-30). Flagged as a pillar fact in Step 7.
- **WC drag structural or growth-induced?** Neither. H1 had a WC *release* (109.02 C) while H1 revenue fell 9.86%, which is the pattern of a shrinking or recovering half [INFERENCE]. The "stopped growing" test cannot run on one half-year. No rating-agency commentary was passed (ND). Receivables at 8.28 days are far below FY26's 18.09 days. Payables rose to 154.42 days. Both point to financing-type working capital (discounting, acceptances), and neither is disclosed.
- **Did CWIP capitalise?** No major commissioning was expected or seen. CWIP fell 3.58 and PPE fell 10.41 net. H1 capex of 9.83 is 40.4% of H1 D&A of 24.31 (L785, L768).
- **Net debt vs projection:** no projection exists (ND). Net debt fell 261.47 to 851.87. Of that, 152.45 (58.3%) came from pre-tax operating cash before WC, and 109.02 (41.7%) from the WC release. At a 25.17% tax the split is about 52/48. The new capex is "financed by taking term loan" (CX L43). If the full Rs 200 cr were debt-funded, net debt would return toward 1,051.87 (d: 851.87 + 200). That figure is a bound, not an estimate; the split is ND.

**Cash conversion classification: INDETERMINATE-WITH-DIRECTION.** Direction is positive: underlying ex-WC, after-interest CFO covers PAT 1.16x (C), and 58.3% of the debt fall came from pre-tax operating cash (about 52% after a statutory-rate tax). Evidence still missing: (1) the receivables discounted or factored at 30-Sep-2026 vs 31-Mar-2026; (2) the composition and cost of 1,462.03 trade payables (acceptances or LC); (3) the composition of 667.63 other current financial assets; (4) the H2 FY27 cash flow, to show whether the release reverses. Under the house rule this caps the verdict at PROCEED WITH CAVEATS or below.

**Checkpoint.** Cash quality tables and answers complete.

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
**Tracker rows not supplied** (notion-thesis.md L12; orchestrator task message). Zero signals for this company.

| Signal Name | Type | Cadence | Latest Observation Date & Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| ND (no tracker rows supplied) | ND | ND | ND | ND | ND | ND |

**Flag:** 0 signals is below the 3-signal floor. Role 5.5 must open at initial workup if the operator takes this name forward (OR-17: three EXTERNAL tracker signals per entity before /fttcp).

### 5.5B. Reconciliation
Not possible: no signal readings exist. Target reported: C revenue +9.83% YoY and operating EBITDA +63.40% YoY. On reported numbers alone the quarter reads "Strong". The "Signals said" column is ND.

### 5.5C. New dependencies surfaced (payload only; no tracker write under /run-quarterly without the operator-approval gate)
No tracker exists for this company, so nothing can be appended. The candidates below go to Role 5.5 at workup. None has been written.
- Candidate (Case B, create-new): **crude oil / polyester raw-material price** (PTA and MEG are the usual inputs [INFERENCE]). Basis: the CMD says "Geopolitical developments in the Middle East led to an increase in crude oil prices, resulting in higher raw material costs" (PR L130-131, MGMT).
- Candidate (Case B): **polyester product-to-input spread** (PSF, PFY, PET resin prices minus input cost). Basis: C gross margin moved -319 bp QoQ (Step 1C). The products are named at PR L148.
- Candidate (Case B): **Middle East supply-chain normalisation** (shipping and input availability). Basis: H1 decline attributed to it (PR L112-113).
- Entity dependency to note: **Indorama Ventures Yarns Pvt Ltd (IVYPL)**, the wholly owned material subsidiary that co-hosts the capex (CX L39-40).
Statement: "No new signals written this quarter; four candidates passed to Role 5.5 because no tracker exists for this company."

### 5.5D. Forward-view weighting
No signal trajectory exists to weigh against the single-quarter print. Step 6 relies on the filed print alone, read conservatively.

---

## STEP 6: RECONCILIATION VS THESIS (PRE-THESIS READ)

No Notion thesis exists. Every projection, checklist, thesis-broken condition and growth trigger is ND. The tables are shown with ND cells as the protocol requires. Actuals are shown so a later thesis can backfill.

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual (Q2 FY27, C) | Lands In |
|---|---|---|---|---|---|
| Revenue (Q) | ND | ND | ND | 1,340.64 (L590) | ND (no thesis) |
| EBITDA Margin (operating) | ND | ND | ND | 8.34% (d) | ND |
| PAT | ND | ND | ND | 74.08 (L609) | ND |
| EPS | ND | ND | ND | 2.84 (L621) | ND |
| Net Debt | ND | ND | ND | 851.87 (d, 30-Sep-2026) | ND |
| ROCE | ND | ND | ND | ND (deferred; Amendment 17 caution, Step 7) | ND |

Probability re-weighting rule: not applicable. No projections exist, so no below-bear count exists. Consecutive-quarter count: 0.

### 6B. Watchlist item status

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| ND | No monitoring checklist (no Notion page) | ND | ND | ND | UNKNOWN |

### 6C. Thesis-broken trigger check

| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| ND: no conditions on record | ND | ND | NOT APPLICABLE |

No condition can fire. The IMMEDIATE EXIT overlay does not apply.

### 6D. Growth trigger status

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| ND: no triggers on record | ND | ND | ND | ND |

Pre-thesis observation, for whoever writes a thesis. Two candidate triggers are visible in the filings. These are observations, not credited triggers:
(1) the Rs 200 cr specialty fibre and filament capex, with COD 16-Oct-2027 to 16-Apr-2028 (CX L39-43; PR L139-142);
(2) deleveraging, with net debt down 261.47 in H1, of which 58.3% came from pre-tax operating cash (about 52% after a statutory-rate tax). Its counter: trailing net debt / EBITDA is 2.34x, and 39.4% of book equity is a deferred tax asset (Step 5A).
One candidate risk is visible: the tax shield ending (A3-09).

**Checkpoint.** 6A-6D presented, all ND by construction.

---

## STEP 6.5: EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH
**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No expectation ledger exists for this name.

Pillar-relevant facts flagged for 6.5A. These are inputs, not a base:
- Trailing-4-quarter C revenue 4,660.99 (d: 4,910.06 - 2,526.35 + 2,277.28, L590). TTM C operating EBITDA 363.40 (d: 309.33 - 159.25 + 213.32). TTM C PAT 210.73 (d: 150.21 - 77.30 + 137.82, L609). TTM EPS 8.07 (d: 5.28 + (5.75 - 2.96), L621).
- Q2 FY27 annualised C PAT 296.32 (d: 74.08 x 4).
- The two bases diverge by 40.6% (d: 296.32 / 210.73). That exceeds the 25% divergence test, and Q1 FY27 was disrupted. A trailing-4-quarter base is the protocol default for lumpy names. Both readings are pre-tax-equivalent (nil tax).
- S TTM PAT 143.48 (d: 110.03 - 55.35 + 88.80, L215).

## STEP 7: FOUR-PILLAR DESTINATION PE RE-VALIDATION
**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No destination PE exists to re-validate. Pillar-relevant facts flagged:

| Pillar / Input | Original Assumption | Fact this quarter (anchored) | Flag for /fttcp and Role 1 |
|---|---|---|---|
| ROCE Base (Pillar 1) | ND | H1 FY27 C operating EBIT 189.01 (d: 213.32 - 24.31). C equity 656.99 (L700). Net debt 851.87 (d). Capital employed 1,508.86 (d). **That capital employed includes the net DTA of 258.83 (d: L685 - L704), 17.2% of it.** Ex-DTA capital employed is 1,250.03 (d). | Archetype candidate is Commodity converter. **If /fttcp classifies it CONVERTER, Amendment 17 bars spot-period ROCE and rupee WC trends from Section 1B.** A4 does not compute a pillar ROCE. /fttcp decides whether the DTA belongs in the ROCE denominator. |
| Cash Multiplier (Pillar 2) | ND | CFO/PAT 2.38x reported; 1.16x ex-WC after interest (C); S 2.48x / 1.19x. All pre-tax (nil current tax, RF L607). | Band choice must use the ex-WC reading or wait for H2. Cash conversion INDETERMINATE-WITH-DIRECTION. |
| Growth Visibility Premium | ND | Rs 200 cr specialty capex, COD 16-Oct-2027 to 16-Apr-2028 (CX L39-43). No tonnage, revenue or return target disclosed. H1 C revenue -9.86%. | Catalyst exists, but its size and economics are ND. |
| Strategic Premium | ND | No moat evidence in the filings. "specialty" and "value-added segments" language only (PR L139-141, MGMT). | Single-credit rule: none credited. |
| UA Multiplier | ND | Institutional ownership and coverage ND in these filings | Qualifiers not testable here. |
| Sector Cap | ND | One segment, polyester goods (RF L425-426) | Sector classification at /fttcp. |
| Hurdle / earnings basis (Amendment 18) | ND | **Reported EPS carries nil tax.** H1 C EPS 5.28 reported vs 3.94 at 25.17% (reported is 33.6% above the statutory basis). FY26 5.75 vs 4.30. TTM 8.07 reported. | Entry EPS and exit EPS must sit on the same tax basis. The loss-pool size and expiry decide when ETR steps up (NOT FOUND, A3-09). |
| Leverage input | ND | Net debt / TTM op EBITDA 2.34x (2.89x if capex fully debt-funded). Net debt / equity ex-net-DTA 2.14x. | Use TTM, not annualised H1 (2.00x). |

---

## STEP 8: POSITION DECISION

**Decision Status verified: NOT ON RECORD (no Notion page, live search 2026-10-17).** The name is not held and not on any recorded watchlist. **Branch: 8A-W.**

### 8A-W walk
- Thesis-broken FIRED? Not applicable (no conditions). No AVOID reclassification arises.
- Below bear on 2+ metrics? Not testable (no projections).
- Between bear and base, or at/above base? Not testable.
- **Output:** entry zone ND, gate ND, proposed Decision Status: none (operator sets). The name has no spear line. CLAUDE.md SPEAR GATE: /run-pipeline and /fttcp cannot run on this name until /step1 writes a Spear line, or the operator writes OVERRIDE, in companies/INDORAMA.md. This review is a pre-thesis read and does not substitute for that gate.
- No trim, exit or add mechanics apply.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: ND. Original trim ladder: ND.
- Candidate tripwires for a future thesis (observations, not rulings):
  (1) a current-tax line appears in S or C P&L, or the AR shows the loss pool expiring within FY28;
  (2) C receivable days rise back above 18.09 (the FY26 level) without matching revenue growth;
  (3) C gross margin at or below 22.13% (the H2 FY26 level) for two quarters;
  (4) the capex term loan is sanctioned above Rs 200 cr, or COD slips past 16-Apr-2028;
  (5) the subsidiaries' proxy share of C PAT stays above 25% with no entity disclosure.

### 8C. Single cleanest metric for next quarter
**Consolidated gross margin**: (revenue from operations - cost of materials - purchase of stock-in-trade - change in inventories) / revenue from operations, Q3 FY27.
It decides whether the YoY margin gain is spread (structural) or cost-and-FX (transient). This quarter's +273 bp operating-margin gain came with a -38 bp gross-margin move (Step 4).
- **Bull threshold:** Q3 FY27 C gross margin at or above 23.92% (the H1 FY27 level), with operating EBITDA margin at or above 8.34%.
- **Bear threshold:** Q3 FY27 C gross margin at or below 22.13% (the H2 FY26 level, d: 527.59 / 2,383.71).
- Between the two: neutral. The margin read then rests on other expenses, which stay undisclosed.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT

Ordered by materiality to a future thesis. Each question references a number from this quarter's filings. "From finding" maps every A3 FORWARD-SIGNAL and AMBIGUOUS finding to at least one question.

| # | Question | Why It Matters | Bull Answer | Bear Answer | Cat | From finding |
|---|---|---|---|---|---|---|
| 1 | Standalone tax is nil in all six reported periods, and the deferred tax asset is unchanged at Rs 258.61 cr. What was the unabsorbed loss and depreciation pool at 31-Mar-2026, and in which financial year does current tax start? | Reported EPS (H1 C 5.28) is pre-tax-equivalent. At 25.17% it is 3.94. The exit-basis EPS depends on the answer. | Pool large enough to shield through FY29 or later, with a disclosed schedule | Pool used up in FY28; ETR steps toward 25% within four quarters | D | A3-09; PR-FN-06 |
| 2 | Consolidated gross margin was 22.60% in Q2 FY27 vs 22.98% in Q2 FY26 and 25.79% in Q1 FY27. What was the realised spread per tonne (product price minus raw-material cost) in Q2 FY27 vs Q2 FY26? | Shows whether the quarter's margin gain came from spread or from cost cuts | Spread per tonne up YoY, with the Q1-to-Q2 dip a seasonal pattern (FY26 showed 25.67% to 22.98%) | Spread per tonne flat or down YoY | C | PR-FN-02; A4-01 |
| 3 | Consolidated other expenses fell from Rs 169.46 cr to Rs 157.25 cr YoY while revenue rose 9.83%. How much of the Rs 12.21 cr fall is power and fuel cost? | Other expenses alone supply 24.65% of the C PAT gain (12.21 / 49.53) and 62.45% of the S gain (19.99 / 32.01), with no composition disclosed | Most of it is a structural power-cost saving (captive or tariff) that repeats | Timing or one-off credits that reverse in H2 | C | A4-02; PR-FN-02 |
| 4 | What were total sales volumes (tonnes) in Q2 FY27 vs Q2 FY26 and Q1 FY27? | Separates the +9.83% YoY revenue into volume and price, and tests whether the other-expense ratio fell on a denominator effect. Q1 FY27 revenue was -28.27% YoY | Volume up YoY; Middle East disruption resolved | Volume flat or down YoY; growth is crude-led price pass-through | A | PR-FN-03; A4-01 |
| 5 | Which of the four subsidiaries earned the subsidiary profit (C-minus-S proxy: Rs 19.03 cr in Q2 FY27, Rs 29.99 cr in Q1 FY27), and what was each entity's H1 FY27 revenue? | The proxy is 25.7% to 47.1% of C PAT with no entity split | One operating entity (IVYPL) with plant, staff and repeatable margin | Profit sits in trading vehicles with about 1.41 cr quarterly payroll; margin is trading timing | E | A3-04; A3-08 |
| 6 | The C-minus-S proxy for subsidiary stock-in-trade purchases was about Rs 74.11 cr in Q2 FY27. What value of H1 FY27 subsidiary purchases came from related parties? | Trading-led subsidiary earnings can carry transfer-pricing risk | Third-party suppliers; related-party value small and at arm's length | Large related-party flows at undisclosed terms | G | A3-05 |
| 7 | Parent receivables are Rs 285.60 cr against consolidated Rs 103.06 cr, so at least Rs 182.54 cr is owed by subsidiaries. What is the intercompany receivable at 30-Sep-2026 and at 31-Mar-2026, and what credit period applies? | Parent receivable quality and parent cash depend on it. The S-minus-C gap rose 46.16 in H1 (136.38 to 182.54), but the change in the intercompany balance itself is ND | Normal trade terms; balance flat or falling | Balance growing, acting as parent funding of subsidiaries | D | A3-06 |
| 8 | Consolidated receivables fell from Rs 243.32 cr to Rs 103.06 cr (about 8 days of sales). What value of receivables was discounted or factored without recourse at 30-Sep-2026 and at 31-Mar-2026? | Decides whether the 41.7% WC share of the Rs 261.47 cr net-debt fall is durable or reclassified financing | Little or no factoring; collections improved structurally | Large factoring increase; debt moved off balance sheet | D | A3-11 |
| 9 | Trade payables are Rs 1,462.03 cr (about 154 days of cost of goods). What amount is acceptances or LC-backed supplier credit, and at what interest cost? | Payables may be debt-like; adjusted net debt could exceed Rs 851.87 cr | Mostly normal supplier credit, no interest | Large acceptances; adjusted leverage materially higher | D | A3-12 |
| 10 | What makes up the Rs 667.63 cr of other current financial assets (21.3% of total assets), and how much is due from related parties? | Undisclosed block of this size affects asset quality and leverage reads | Mostly security deposits, incentives or claims with clear recovery dates | Related-party advances or long-dated claims | D | A3-12 |
| 11 | What capacity in tonnes per annum does the Rs 200 cr specialty capex add, and what revenue do you expect at full use? | Sizes the only disclosed growth catalyst | Capacity and revenue disclosed; asset turn at or above the current level | No capacity or revenue figure given | B | CX-FN-01; PR-FN-01 |
| 12 | On what dates will machinery orders, civil start and trial runs happen toward the COD window of 16-Oct-2027 to 16-Apr-2028? | Converts an "estimated" window into checkable milestones | Dated milestone path, with orders placed in Q3 FY27 | No milestone dates | B | CX-FN-02; PR-FN-01 |
| 13 | What term-loan amount has been sanctioned for the Rs 200 cr capex, and at what interest rate? | Debt reverses part of the H1 deleveraging; interest runs before revenue | Loan of half or less of the outlay, already sanctioned, at a disclosed rate | Fully debt-funded, not yet sanctioned | F | CX-FN-03 |
| 14 | How much of the Rs 200 cr sits in the Company and how much in IVYPL? | Decides where the assets, debt and revenue land in S vs C | Clear split disclosed, with IVYPL funded by parent equity | No split; funding of IVYPL by inter-corporate loan | F | CX-FN-04 |
| 15 | Which subsidiary recognised the new deferred tax liability of Rs 9.37 cr at 30-Sep-2026? | First subsidiary-level tax line; shows which entity now has taxable timing differences | One entity with accelerated depreciation; no cash tax soon | A profitable subsidiary moving to taxable status | D | A3-10 |
| 16 | The FY26 exceptional employee-benefit charge was Rs 2.70 cr (consolidated). Is another such scheme planned for H2 FY27? | A repeat charge would hit H2 PBT | No further scheme | New scheme planned in H2 FY27 | G | A3-01 |
| 17 | On what date did each of the four subsidiaries enter the group, and was any renamed in the last four quarters? | The review report says "its subsidiary" (singular) but lists four; perimeter history is unknown | All four held for more than four quarters, no renames | One or more entered recently, distorting YoY comparisons | G | A3-14; A3-16 |
| 18 | What foreign-currency payable was unhedged at 30-Sep-2026? (FX loss was Rs 10.28 cr in Q2 FY26 vs Rs 2.51 cr in Q2 FY27.) | 15.69% of the C PAT gain came from the FX line | Hedge policy covers most exposure | Large unhedged dollar payables; the swing can reverse | C | PR-FN-05 |
| 19 | Will future press releases headline revenue from operations (Q2 FY27 +9.83%) instead of total income, and show EBITDA excluding other income? | The release labels total income as revenue and puts other income inside EBITDA | Yes, from Q3 FY27 | No change | G | PR-FN-04 |
| 20 | The capex approval came from the same 16-Oct-2026 meeting but was filed separately (signed 14:51:58) and is not in the board outcome items a and b. At what time did each exchange disseminate it? | Tests disclosure timeliness: the meeting ended 14:35 (RF L63), so signing came 17 minutes later | Disseminated within 30 minutes of meeting close | Dissemination later than 30 minutes | G | CX-FN-05 |

**Top 3 by likelihood of thesis-changing information:**
- **Bull probability:** Q2, the spread per tonne YoY. A rising spread makes the margin gain structural and supports a converter-to-specialty climb.
- **Bear confirmation:** Q1, the tax-loss pool and the year current tax starts. An early step-up cuts EPS by 25.17% on the same PBT.
- **Management transparency:** Q5, profit by subsidiary. A refusal, or a "one segment" answer, is itself a governance signal.

**Channel recommendation:** IR email. No concall transcript is in this run, and no concall date is in the filings (ND). Send all 20 questions verbatim. If a Q2 concall is later scheduled within two weeks, put Q1, Q2 and Q5 in the live Q&A and submit the rest in writing.

---

## STEP 9: NOTION UPDATE
No Notion page exists, so A4 makes no write. Decision Status is never written by /run-quarterly. Proposed payload for the operator, used only if a page is created:
- Key Notes prefix: "2026-10-17 | Q2 FY27 pre-thesis read: C PAT 74.08 (+201.75% YoY off a trough base) on nil tax; gross margin -38 bp YoY; net debt -261.47 (152.45 pre-tax operating cash, 109.02 WC release; about 52/48 at a 25.17% tax); Rs 200 cr specialty capex approved, COD Oct-2027 to Apr-2028; verdict PROCEED WITH FLAGS."
- Catalyst status: ND (no thesis). Thesis status: ND (pre-thesis).
- Source: Reg 33 results and Reg 30 filings dated 16-Oct-2026 (RF L18; PR L19; CX L19). Auditor: unmodified limited review. Business type: standard.

---

## A4 OWN FINDINGS (not from A3)

| id | Finding | Anchor | Classification |
|---|---|---|---|
| A4-01 | C gross margin 22.60% vs 22.98% YoY (-38 bp) and 25.79% QoQ (-319 bp); the FY26 Q1-to-Q2 fall was similar (25.67% to 22.98%). Op EBITDA margin gain came from opex (-13.06) and FX (-7.77). | RF L590, L593-597, L602 | FORWARD-SIGNAL (lean bear on spread durability) |
| A4-02 | S gross profit fell 1.04 YoY on +7.03% revenue. All S PAT growth came from cost lines, FX, finance cost and OI. | RF L196, L199-203, L208 | AMBIGUOUS |
| A4-03 | Press-release "EBIT" deducts the FX loss, and "EBITDA" includes OI. This resolves PR-FN-05 (no D&A fall) and PR-FN-06 (Reading A, nil tax). | PR L98-104; RF L599-608 | NEUTRAL-FACT |
| A4-04 | The capex letter was signed at 14:51:58, 16 min 58 s after the 14:35 meeting close. That partly resolves CX-FN-05; dissemination time is still ND. | CX L53; RF L63 | NEUTRAL-FACT |
| A4-05 | Stock-in-trade rose to 8.67% of C revenue in Q2 FY27 (116.22 / 1,340.64), from 6.45% in Q2 FY26 (78.76 / 1,220.64). The trading share is rising. | RF L594, L590 | AMBIGUOUS (business-mix drift) |
| A4-06 | The H1 net-debt fall of 261.47 splits 152.45 (58.3%) pre-tax operating cash before WC and 109.02 (41.7%) WC release; about 52/48 at a 25.17% tax, with capex at 40.4% of D&A. Net DTA of 258.83 is 39.4% of C equity, and net debt / TTM op EBITDA is 2.34x. | RF L607, L685, L700, L704, L768, L773-L797 | AMBIGUOUS (leverage read) |

---

## MONITORABLES / CATALYST LIST (seeded from the A3 commitment registers and Board Outcome forward items)

| # | Item | Implied date | Source ref | Status word |
|---|---|---|---|---|
| M1 | Newspaper publication of extract of unaudited Q2/H1 FY27 results (Reg 47(1)(b)) | Not stated in filing; Reg 47 window after 16-Oct-2026 [INFERENCE: about 18-Oct-2026] | RF L57-60 (R667) | initiated |
| M2 | Website publication of the results extract | Not stated; "is also being published" | RF L60 (R668) | underway |
| M3 | Q3 FY27 results: C gross margin (Step 8C), tax line, receivable trend | By 14-Feb-2027 [INFERENCE: Reg 33 45-day window] | Step 8C | scheduled (regulatory) |
| M4 | Term-loan sanction for the Rs 200 cr capex (amount, rate, borrowing entity) | Not stated; before or during build | CX L43-44 (R033, R034) | proposed ("would be") |
| M5 | Capex split Company vs IVYPL disclosed | Not stated | CX L39-40 (R023, R044) | not disclosed |
| M6 | Capex milestones: machinery order, civil start, trial run | Not stated; must precede COD window | CX L42 (R032) | approved (not yet initiated) |
| M7 | FY27 audited results with H2 cash flow: receivable days, payables, CFO ex-WC | By 30-May-2027 [INFERENCE: Reg 33 60-day window] | Step 5 | scheduled (regulatory) |
| M8 | FY27 Annual Report: tax-loss pool note, related-party note, subsidiary financials, other-financial-asset composition | By 30-Sep-2027 AGM [INFERENCE: Companies Act] | A3-09, A3-12, A3-04 | scheduled |
| M9 | Commercial operation of specialty filament and fibre capacity at Butibori | 16-Oct-2027 to 16-Apr-2028 (estimated) | CX L41-43 (R012, R040); PR L139 (R114-R116) | approved (not yet initiated) |
| M10 | Middle East supply-chain normalisation (H1 decline cause) | Undated | PR L112-113 (R080) | management attribution |
| M11 | "Further strengthening our operating and financial performance" | Undated | PR L138 (R113) | aspirational |
| M12 | Investment to "broaden our product portfolio, increase our participation in value-added segments" | Medium term, undated | PR L140-142 (R117) | expected |

---

## VERDICT

**Protocol verdict: PROCEED WITH FLAGS.** Cash conversion is INDETERMINATE-WITH-DIRECTION, which caps the verdict at PROCEED WITH CAVEATS or below. The flags below set it one notch lower. No mechanical failure occurred: the ledgers are reconciled, the tables are complete, and the auditor is unmodified. The verdict is not REWORK or INSUFFICIENT EVIDENCE.

Flags:
1. **Zero-tax earnings.** S current tax is nil in all six periods; C ETR is -0.30% in Q2. Statutory-rate C H1 EPS is 3.94 vs 5.28 reported; reported is 33.6% above the statutory basis (A3-09).
2. **Spread did not widen.** C gross margin -38 bp YoY, -319 bp QoQ (FY26 showed a similar Q1-to-Q2 fall). The operating-margin gain is opex and FX (A4-01, A4-02).
3. **Trough base.** Core PBT +208.49% YoY is measured off Q2 FY26, the trough. Against Q1 FY26 it is +41.20%.
4. **Subsidiary opacity.** The C-minus-S proxy is 25.7% of Q2 and 47.1% of Q1 C PAT, with no entity split. At least 182.54 of parent receivables is intercompany. Trading share is rising (A3-04, A3-05, A3-06, A3-08, A4-05).
5. **Financing-type working capital.** CFO includes a 109.02 WC release (41.7% of the net-debt fall). The other 152.45 is pre-tax operating cash; at a 25.17% tax and with capex at 40.4% of D&A, the split is about 52/48. Receivables are at 8.28 days and payables at 154.42 days of COGS. Factoring and acceptances are undisclosed (A3-11, A3-12).
6. **Leverage on book equity.** Net DTA 258.83 is 39.4% of C equity; net debt / equity ex-DTA is 2.14x; net debt / TTM op EBITDA is 2.34x (A4-06).
7. **Cash conversion INDETERMINATE-WITH-DIRECTION.** Missing evidence: factoring at both dates, payables composition and cost, other-financial-asset composition, H2 cash flow.
8. **Press-release reframing.** "Revenue" means total income; EBITDA includes OI and excludes FX; the margin-expansion headline is YoY only (PR-FN-02, PR-FN-04).
9. **Capex funding open.** Rs 200 cr by term loan plus accruals, split unquantified. Company/IVYPL split unstated. COD 16-Oct-2027 to 16-Apr-2028 (CX-FN-01 to CX-FN-04).
10. **No thesis.** Decision Status NOT ON RECORD; no spear; the spear gate blocks pipeline runs until /step1.
11. **Tracker below floor.** 0 signals supplied.
12. **Converter caution.** If /fttcp classifies the name CONVERTER, Amendment 17 bars spot ROCE and rupee WC trends from Section 1B.

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (this quarter's filings), MGMT (management statement in the press release or letter), SECONDARY (general market knowledge, not from these filings), INFERENCE (A4 reasoning). No prior Notion or peer work exists for this name. Every FILED and MGMT figure below comes from this quarter's filings. Metrics the filings do not disclose: volumes, realisations, spread per tonne, capacity use, product mix, subsidiary-level results, tax-loss pool, factoring, payables composition, promoter pledge.

### 1. Summary narrative
Indo Rama made Rs 74.08 cr consolidated profit in Q2 FY27, against Rs 24.55 cr a year ago [FILED]. Revenue rose 9.83% to Rs 1,340.64 cr [FILED]. Core profit before tax rose from Rs 22.84 cr to Rs 70.46 cr [FILED, derived].
That comparison starts from a weak quarter. Against Q1 FY26 (Rs 49.90 cr), core profit is up 41.20% [FILED, derived].
The company paid no current tax [FILED]. At a normal 25.17% rate, quarterly profit would be about Rs 55.27 cr [INFERENCE]. Nobody outside the company yet knows how long the tax shield lasts.
The raw-material spread did not widen. Gross margin was 22.60%, against 22.98% a year ago [FILED, derived]. Most of the margin gain came from Rs 12.21 cr lower other expenses and a Rs 7.77 cr smaller currency loss [FILED].
The half-year was weak. Q1 revenue fell 28.27% year on year [FILED, derived]. Management blames Middle East supply problems [MGMT].
Net debt fell Rs 261.47 cr in six months [FILED, derived]. Rs 152.45 cr of that came from pre-tax operating cash, and Rs 109.02 cr from releasing working capital [FILED, derived]. After a normal tax, the two parts would be about equal [INFERENCE].
Receivables are now about 8 days of sales, and payables about 154 days of cost [FILED, derived].
A deferred tax asset makes up 39.4% of book equity [FILED, derived].
Four subsidiaries made a quarter to nearly half of group profit, and the filing gives no split [FILED, derived].
The board approved Rs 200 cr for specialty fibre and filament, mostly on a term loan, starting output between October 2027 and April 2028 [FILED].
There is no thesis on record, so this read changes no decision. The verdict is PROCEED WITH FLAGS.

### 2. Sector intelligence
Polyester makers buy crude-linked inputs, usually PTA and MEG, and sell fibre, yarn and resin [SECONDARY]. Profit depends on the spread between the two, not on revenue. The CMD says Middle East events raised crude and raw-material costs and kept the chain volatile [MGMT, PR L130-131]. Gross margin fell from 25.79% to 22.60% QoQ [FILED, derived]. A similar Q1-to-Q2 fall happened last year, with no crude attribution in the filings (25.67% to 22.98%) [FILED, derived]. So crude may explain only part of this year's fall [INFERENCE]. Rising input prices also lift reported revenue without more tonnes [INFERENCE]. That is why the missing volume figure matters. Demand cycle, import competition, and trade-protection measures on polyester inputs and fibre are not mentioned in these filings [not disclosed]. A crude spike usually squeezes non-integrated spreads first and relieves them later [SECONDARY].

### 3. Business-model intelligence
The company converts bought raw material into polyester staple fibre, filament yarn, textured yarn, chips and bottle-grade PET resin at one Butibori site [MGMT, PR L146-149]. Stated capacity is 6.72 lakh tonnes a year, including 2.52 lakh tonnes of PET resin and 1.75 lakh tonnes of textured yarn [MGMT, PR L149-150]. Materials and traded goods take 77.4% of revenue, so a 1-point spread move shifts EBITDA by about Rs 13 cr a quarter [FILED, derived; INFERENCE]. The balance sheet runs on supplier credit: payables of Rs 1,462.03 cr fund a negative cash cycle of about 73 days [FILED, derived].
Two drifts show this quarter. First, trading grew: bought-in goods rose to 8.67% of revenue from 6.45% [FILED, derived], and much of it sits in subsidiaries [FILED, derived proxy]. Second, the board wants to move toward specialty products with the Rs 200 cr plan [FILED]. Neither drift has disclosed unit economics yet.

### 4. Competition intelligence
These filings name no competitor. Peer context is SECONDARY and from no prior Notion work. The company calls itself "a leading integrated polyester manufacturer" with an "integrated manufacturing platform" [MGMT, PR L77, L147]. On the filed evidence, "integrated" means one site that runs from polymer through fibre, yarn, texturing and resin [MGMT, PR L146-149]. It does not mean the company makes its own PTA or MEG: cost of materials is 70.4% of revenue, and the CMD says crude raised "raw material costs" [FILED, RF L593, L590; MGMT, PR L130-131; INFERENCE]. Reliance Industries is the large producer that makes its own PTA and MEG [SECONDARY]. Listed converters such as Filatex India and Sanathan Textiles buy those inputs, as Indo Rama appears to [SECONDARY; INFERENCE]. Indo Rama wins on scale at one site and a broad range that includes PET resin [MGMT capacity figures; comparison is INFERENCE]. It is weaker where an input-integrated producer controls cost and can set product prices [INFERENCE]. The risk to watch is whether the specialty capex earns a premium spread, or lands where input-integrated and Chinese producers already compete [INFERENCE]. Market share and peer spreads are not disclosed.

### 5. Forward map (next about 10-11 months)
**Make-or-break reading:** Q3 FY27 consolidated gross margin, due with results by 14-Feb-2027 [INFERENCE: Reg 33 window]. Bull at or above 23.92%. Bear at or below 22.13%.
- **Newspaper and website extract (M1, M2), about 18-Oct-2026.** Bull: published on time. Bear: late, adding to the drafting-slip count.
- **Term-loan sanction for the capex (M4), date not stated.** Bull: sanction disclosed, with internal accruals carrying a real share. Bear: the full Rs 200 cr is borrowed, and net debt climbs back toward Rs 1,051.87 cr (2.89x TTM EBITDA).
- **Capex split and milestones (M5, M6), date not stated.** Bull: Company/IVYPL split and dated orders disclosed. Bear: still undisclosed by Q3 FY27 results.
- **Q3 FY27 results (M3), by 14-Feb-2027.** Bull: a tax line still nil and receivables still near 8 days. Bear: receivables rebuild toward 18.09 days, or current tax appears.
- **FY27 audited results (M7), by 30-May-2027.** Bull: H2 cash flow ex-WC still covers profit at 1.16x or better. Bear: the H1 working-capital release of Rs 109.02 cr reverses.
- **FY27 Annual Report (M8), by 30-Sep-2027.** Bull: a disclosed loss pool shields tax through FY29, and the subsidiaries' accounts show an operating plant. Bear: the pool runs out in FY28, or the subsidiaries prove to be trading vehicles with related-party flows.
- **Capex COD window (M9), 16-Oct-2027 to 16-Apr-2028, just past this horizon.** Bull: milestones on track by the AR. Bear: no orders placed by Q4 FY27.

---

## LOOP 1 RESPONSE

A4 checked every A5 number against the fulltext lines before using it. No disagreement.

| A5 item | A4 check (fulltext lines) | Result |
|---|---|---|
| F1 Q7 bound | S receivables 285.60 (RF L300) less C 103.06 (RF L690) = 182.54; 31-Mar 379.70 - 243.32 = 136.38; gap rose 46.16. Intercompany = gap + subsidiaries' external receivables, so the gap bounds the level, not the change. | Agree |
| F2 Q3 shares | 12.21 / 49.53 = 24.65%; 19.99 / 32.01 = 62.45% (RF L597, L203, L609, L215) | Agree |
| F3 4C multiples | 72.39 / 24.55 = 2.95x; 64.62 / 24.55 = 2.63x (RF L609) | Agree |
| F4 EPS premium | 1 / 0.7483 - 1 = 33.6%; 5.28 / 3.94 = +34.0% (RF L606, L621) | Agree |
| C1 net-debt split | 216.73 + 2.71 - 59.02 - 6.24 - 1.73 = 152.45; WC 109.02; total 261.47 (RF L773, L783, L795, L789, L793-794, L774-781) | Agree |
| M1 comparators | Q1 FY26 GM (615.70 - 280.51) / 1,305.71 = 25.67%; other exp / revenue 164.36 / 1,305.71 = 12.59%, 334.86 / 2,383.71 = 14.05% (RF L590, L593-597) | Agree |
| M3 trough base | 70.46 / 49.90 = +41.20%; 7.77 / 47.62 = 16.32% (RF L591, L602, L606) | Agree |
| M4 leverage | 851.87 / 363.40 = 2.34x; 1,051.87 / 363.40 = 2.89x; net DTA 268.20 - 9.37 = 258.83, 39.4% of 656.99; 851.87 / 398.16 = 2.14x; 1,113.34 / 260.56 = 4.27x (RF L685, L700, L704, L532) | Agree |
| M5 sequence | 49.90, 22.84, 29.26, 60.18, 70.46; 64.62 / 52.75 = +22.50% (RF L606, L591, L609) | Agree |
| A3-07 anchor | C other equity 258.06 vs S 302.65 at 31-Mar (-44.59); 395.88 vs 391.45 at 30-Sep (+4.43) (RF L699, L309) | Agree |

## LOOP 1 CHANGE LOG

| Item | Type | Fix | Location |
|---|---|---|---|
| F1 | FACTUAL | Q7 now states the S-minus-C gap rose 46.16 and that the change in the intercompany balance is ND; the level bound of 182.54 stays | Step 8.5 Q7; 5C text |
| F2 | FACTUAL | Q3 shares corrected to 24.65% (C) and 62.45% (S) for other expenses alone; bridge rows split employee vs other-expense shares | Step 8.5 Q3; 4A, 4B rows |
| F3 | FACTUAL | "2.6x" replaced by 2.95x and 2.63x | 4C |
| F4 | FACTUAL | Analyst note now says reported EPS is 33.6% above the statutory basis; same figure added in 4C, Step 7 and Flag 1; Top-3 wording now "cuts EPS by 25.17%" | analyst note; 4C; Step 7; Verdict |
| C1 | CONTRADICTION | Net-debt fall split stated: 152.45 (58.3%) operating cash, 109.02 (41.7%) WC; new sources table | 5A net-debt row and table; 5D; 6D; Step 9 payload; brief summary; analyst note; A4-06 |
| M1 | MISSING | Q1 FY26 GM 25.67% and other-expense ratio sequence added beside A4-01, with two readings and the separating observation (volume) | 3A columns; 3C; 4A comparators; A4-01; Q2, Q4; sector brief |
| M2 | MISSING | A3-07 anchored in 5C; A3-15 and CX-FN-06 in 0D with a drafting tally; PR-FN-08 in 1E | preamble; 0D; 1E; 5C |
| M3 | MISSING | Trough-base counter grafted (core PBT +41.20% vs Q1 FY26; FX share 16.32%) | 2A; 2D.3; brief summary; Flag 3 |
| M4 | MISSING | TTM ND/EBITDA 2.34x (2.89x capex bound), net DTA 39.4% of equity, ND/equity ex-DTA 2.14x (4.27x at 31-Mar), DTA inside capital employed | 5A rows; Step 7 ROCE and leverage rows; Flag 6; A4-06 |
| M5 | MISSING | Full non-consecutive core-PBT sequence and Q1 FY26 PAT benchmark (+22.50%) | 3C; 4C |
| S1 | STYLE | 25.41 relabelled: 24.56 for the three named lines plus employee 0.85 | 4A A4-01 text |
| S2 | STYLE | C-minus-S subsidiary figures labelled as proxies net of eliminations | 5C; Q5; Q6; 8B; brief |
| S3 | STYLE | Competition brief glosses the company's "integrated" self-description against filed evidence | brief part 4 |
| S4 | STYLE | Core PBT YoY 208.50% corrected to 208.49% | 2A; 2D.3 |
| S5 | STYLE | No action (A1 structured-file boilerplate; no conclusion depends on it) | n/a |

## LOOP 2 RESPONSE

A4 checked each loop-2 number against its fulltext line. No disagreement.

| A5 item | A4 check (fulltext lines) | Result |
|---|---|---|
| F5 crude wording | The FY26 Q1-to-Q2 gross-margin fall (25.67% to 22.98%) has no crude attribution in any of the three filings. The CMD's crude remark (PR L130-131) covers Q2 FY27 only. A4 holds no SECONDARY source for FY26 crude moves, so the wording now states only what the filings show. | Agree; wording replaced |
| M6 pre-tax | Current tax nil (RF L607); refund 2.71 (RF L783); tax at 25.17% on H1 PBT 137.60 (RF L606) = 34.63; 152.45 - 34.63 = 117.82; 117.82 / (117.82 + 109.02) = 51.9%, so about 52/48 | Agree |
| M6 capex | Capex 9.83 (RF L785) / D&A 24.31 (RF L768) = 40.4% | Agree |

## LOOP 2 CHANGE LOG

| Item | Type | Fix | Location |
|---|---|---|---|
| F5 | FACTUAL | "without a crude shock" replaced with "with no crude attribution in the filings"; 3C uses the same wording | Sector brief (part 2); 3C |
| M6 | MISSING | Stated that the 152.45 earned share is pre-tax cash (nil current tax RF L607; 2.71 refund RF L783); about 52/48 at a 25.17% tax (117.82 vs 109.02); capex 40.4% of D&A (RF L785, L768). Memo row added to the sources table | 5A net-debt row, capex row, sources table and paragraph |
| M6 (same claim elsewhere) | MISSING | "pre-tax" and the 52/48 split added wherever the 58.3% earned share appears | 5D; cash-conversion classification; 6D; Step 7 Pillar 2 row; Step 9 Key Notes; A4-06; Verdict Flag 5; brief summary; YAML flags; analyst note |
| S6-S8 | STYLE | Optional; not applied. A4 did not re-read the audit file in this loop, per the coordinator's instruction | n/a |

Verdict unchanged: PROCEED WITH FLAGS. Cash classification unchanged: INDETERMINATE-WITH-DIRECTION.

---

```yaml
stage: A4-analyst
company: "INDORAMA"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
loop_iteration: 2
docs_merged: [results, presentation]   # results = Reg 33 filing + Reg 30 capex Board Outcome (results class); presentation = press release
ledger_reconciliation:
  notes: 12
  turns: 0
  slides: 3
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, PR-FN-01, PR-FN-02, PR-FN-03, PR-FN-04, PR-FN-05, PR-FN-06, PR-FN-07, PR-FN-08, CX-FN-01, CX-FN-02, CX-FN-03, CX-FN-04, CX-FN-05, CX-FN-06]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "NOT ON RECORD (no Notion page, live search 2026-10-17); framed as PRE-THESIS READ"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY27", gap_pct_of_s_pat: 34.6, c_minus_s: 19.03}
  - {period: "Q1 FY27", gap_pct_of_s_pat: 88.9, c_minus_s: 29.99}
  - {period: "Q2 FY26", gap_pct_of_s_pat: 6.6, c_minus_s: 1.51}
  - {period: "H1 FY27", gap_pct_of_s_pat: 55.2, c_minus_s: 49.02}
  - {period: "H1 FY26", gap_pct_of_s_pat: 39.7, c_minus_s: 21.95}
  - {period: "FY26", gap_pct_of_s_pat: 36.5, c_minus_s: 40.18}
questions_for_management:
  - {q: "Unabsorbed loss/depreciation pool at 31-Mar-2026 and the FY in which current tax starts (S tax nil all six periods; DTA flat at 258.61)", from_finding_id: "A3-09; PR-FN-06"}
  - {q: "Realised spread per tonne Q2 FY27 vs Q2 FY26 (C gross margin 22.60% vs 22.98%; 25.79% in Q1 FY27; 25.67% in Q1 FY26)", from_finding_id: "PR-FN-02; A4-01"}
  - {q: "Share of the 12.21 cr YoY fall in C other expenses that is power and fuel cost (other expenses alone = 24.65% of C PAT gain, 62.45% of S)", from_finding_id: "A4-02; PR-FN-02"}
  - {q: "Total sales volume (tonnes) Q2 FY27 vs Q2 FY26 and Q1 FY27", from_finding_id: "PR-FN-03; A4-01"}
  - {q: "Which subsidiary earned the C-minus-S proxy profit of 19.03 cr (Q2) and 29.99 cr (Q1); each entity's H1 FY27 revenue", from_finding_id: "A3-04; A3-08"}
  - {q: "Value of H1 FY27 subsidiary stock-in-trade purchases from related parties (C-minus-S proxy about 74.11 cr in Q2)", from_finding_id: "A3-05"}
  - {q: "Intercompany receivable owed to the parent at 30-Sep-2026 and 31-Mar-2026 (at least 182.54 at 30-Sep; S-minus-C gap rose 46.16) and its credit period", from_finding_id: "A3-06"}
  - {q: "Receivables discounted/factored without recourse at 30-Sep-2026 and 31-Mar-2026 (C receivables 243.32 to 103.06)", from_finding_id: "A3-11"}
  - {q: "Acceptances/LC-backed credit within 1,462.03 cr trade payables and their interest cost", from_finding_id: "A3-12"}
  - {q: "Composition of 667.63 cr other current financial assets and related-party share", from_finding_id: "A3-12"}
  - {q: "Capacity (tpa) added by the Rs 200 cr specialty capex and revenue at full use", from_finding_id: "CX-FN-01; PR-FN-01"}
  - {q: "Dated milestones (machinery order, civil start, trial run) toward COD 16-Oct-2027 to 16-Apr-2028", from_finding_id: "CX-FN-02; PR-FN-01"}
  - {q: "Term-loan amount sanctioned for the capex and its interest rate", from_finding_id: "CX-FN-03"}
  - {q: "Split of the Rs 200 cr between the Company and IVYPL", from_finding_id: "CX-FN-04"}
  - {q: "Which subsidiary recognised the new 9.37 cr deferred tax liability", from_finding_id: "A3-10"}
  - {q: "Whether another employee-benefit scheme (FY26 exceptional 2.70 cr) is planned in H2 FY27", from_finding_id: "A3-01"}
  - {q: "Date each of the four subsidiaries entered the group; any rename in the last four quarters", from_finding_id: "A3-14; A3-16"}
  - {q: "Unhedged foreign-currency payable at 30-Sep-2026 (FX loss 10.28 cr Q2 FY26 vs 2.51 cr Q2 FY27)", from_finding_id: "PR-FN-05"}
  - {q: "Will press releases headline revenue from operations and EBITDA excluding other income from Q3 FY27", from_finding_id: "PR-FN-04"}
  - {q: "Exchange dissemination time of the separately filed capex approval (signed 14:51:58; meeting closed 14:35)", from_finding_id: "CX-FN-05"}
monitorables:
  - {item: "Reg 47(1)(b) newspaper extract of Q2/H1 FY27 results", implied_date: "not stated; Reg 47 window after 16-Oct-2026 (about 18-Oct-2026, INFERENCE)", source_ref: "RF L57-60 (R667)"}
  - {item: "Website publication of results extract", implied_date: "not stated; underway", source_ref: "RF L60 (R668)"}
  - {item: "Q3 FY27 results: C gross margin (bull >=23.92%, bear <=22.13%), tax line, receivable days", implied_date: "by 2027-02-14 (INFERENCE: Reg 33 45-day window)", source_ref: "Step 8C"}
  - {item: "Term-loan sanction for Rs 200 cr capex (amount, rate, borrower)", implied_date: "not stated; before or during build", source_ref: "CX L43-44 (R033, R034)"}
  - {item: "Capex split Company vs IVYPL", implied_date: "not stated", source_ref: "CX L39-40 (R023, R044)"}
  - {item: "Capex milestones: machinery order, civil start, trial run", implied_date: "not stated; before COD window", source_ref: "CX L42 (R032)"}
  - {item: "FY27 audited results with H2 cash flow (receivable days, payables, CFO ex-WC)", implied_date: "by 2027-05-30 (INFERENCE: Reg 33 60-day window)", source_ref: "Step 5"}
  - {item: "FY27 Annual Report: tax-loss pool, related-party note, subsidiary financials, other financial assets", implied_date: "by 2027-09-30 (INFERENCE: AGM deadline)", source_ref: "A3-09, A3-12, A3-04"}
  - {item: "COD of specialty filament and fibre capacity at Butibori", implied_date: "2027-10-16 to 2028-04-16 (estimated)", source_ref: "CX L41-43 (R012, R040); PR L139 (R114-R116)"}
  - {item: "Middle East supply-chain normalisation", implied_date: "undated", source_ref: "PR L112-113 (R080)"}
  - {item: "Further strengthening of operating and financial performance", implied_date: "undated", source_ref: "PR L138 (R113)"}
  - {item: "Portfolio broadening into value-added segments", implied_date: "medium term, undated", source_ref: "PR L140-142 (R117)"}
flags:
  - "ZERO-TAX EARNINGS: S current tax nil all six periods, DTA flat 258.61; C ETR -0.30% Q2; statutory-rate (25.17%) C H1 EPS 3.94 vs 5.28 reported; reported is 33.6% above statutory basis (A3-09)"
  - "SPREAD NOT WIDENED: C gross margin 22.60% vs 22.98% YoY (-38 bp), 25.79% QoQ (-319 bp; FY26 Q1-to-Q2 was 25.67% to 22.98%, no crude attribution in the filings); op EBITDA margin +273 bp YoY came from other expenses -12.21 and FX loss -7.77 (A4-01)"
  - "TROUGH BASE: C core PBT +208.49% YoY is off the Q2 FY26 trough; +41.20% vs Q1 FY26 (49.90); FX swing 16.32% of the rise"
  - "STANDALONE GROSS PROFIT FELL 1.04 YoY on revenue +7.03%; S PAT growth all from cost lines, FX, finance cost, OI (A4-02)"
  - "SUBSIDIARY OPACITY: C-minus-S proxy 25.7% (Q2) / 47.1% (Q1) of C PAT, no entity split; >=182.54 intercompany receivables (level bound); trading share 8.67% of C revenue vs 6.45% (A3-04/05/06/08, A4-05)"
  - "NET-DEBT SPLIT: -261.47 = 152.45 (58.3%) pre-tax operating cash before WC (nil current tax RF L607; 2.71 refund RF L783) + 109.02 (41.7%) WC release; about 52/48 at a 25.17% tax; capex 40.4% of D&A; receivables 8.28 days; payables 154.42 days; factoring and acceptances undisclosed (A3-11/12, A4-06)"
  - "LEVERAGE ON BOOK EQUITY: net DTA 258.83 = 39.4% of C equity; ND/equity ex-DTA 2.14x (4.27x at 31-Mar); ND/TTM op EBITDA 2.34x, 2.89x if capex fully debt-funded (A4-06)"
  - "CASH CONVERSION INDETERMINATE-WITH-DIRECTION: missing factoring at both dates, payables composition/cost, other financial assets composition, H2 cash flow; verdict capped"
  - "PRESS RELEASE REFRAMING: revenue = total income; EBITDA includes OI and excludes FX; margin-expansion headline YoY only (PR-FN-02/04)"
  - "CAPEX Rs 200 cr: term loan + accruals unquantified; Company/IVYPL split unstated; COD 2027-10-16 to 2028-04-16 (CX-FN-01..04)"
  - "NO THESIS: Decision Status NOT ON RECORD; no spear; /step1 required before any pipeline run (spear gate)"
  - "TRACKER BELOW FLOOR: 0 downstream signals supplied; Role 5.5 to open at workup"
  - "CONVERTER CAUTION: if /fttcp classifies CONVERTER, Amendment 17 bars spot ROCE and rupee WC trends from Section 1B"
  - "OR-30: Steps 6.5 and 7 deferred to /fttcp and Role 1; pillar facts flagged in Step 7 table"
  - "A1 DATA NOTES: R145/R478 are 31-Mar-2026 other equity; R640 FRN truncated (full 000756N/N500441 at RF L520); PR Q2 FY26 PAT '246' = 24.6"
plain_language_brief_included: true
analyst_note: "Pre-thesis read; no decision framing. Loops 1 and 2 applied every A5 FACTUAL, CONTRADICTION and MISSING item after line checks; no disagreement. The headline (C PAT 74.08 vs 24.55) is real pre-tax but runs off the trough quarter; against Q1 FY26 core PBT is +41.20%. Three facts cap the reading. Tax: no current tax, so reported EPS is 33.6% above a statutory-rate basis; any Amendment 18 entry/exit pairing must fix the tax basis first. Margin source: gross margin fell 38 bp YoY; the operating gain is other expenses and FX of undisclosed composition, and FY26 showed the same Q1-to-Q2 gross-margin fall, so spread durability is unproven until volume is disclosed. Balance sheet: net debt fell 261.47; 152.45 was pre-tax operating cash at maintenance capex (40.4% of D&A) and 109.02 a WC release that can reverse, about 52/48 at a 25.17% tax. 39.4% of book equity is a deferred tax asset resting on the undisclosed loss pool; TTM net debt / EBITDA is 2.34x."
review_path: "runs/indorama-q2fy27/work/review_indorama_q2fy27.md"
```

## CONTENT PART 2: A3 FORENSICS, RESULTS (verbatim)
# A3 FORENSIC NOTES: INDORAMA (Indo Rama Synthetics (India) Ltd), Q2 FY27, doctype: results

Inputs read: A1 structured `runs/indorama-q2fy27/extracted/indorama-results-q2fy27-structured.md` (R001-R721, all rows); A1 fulltext `runs/indorama-q2fy27/extracted/indorama-results-q2fy27-fulltext.md` (lines 1-837, all lines; VER- image-verified lines govern over the OCR text); A2 ledger `runs/indorama-q2fy27/work/ledger_results_indorama_q2fy27.md`. Prior-quarter fulltext: ND. Notion checklist: NONE (no Notion page, no spear on record). Source PDF and `inputs/` not opened.

Unit: Rs crore unless stated. S = standalone, C = consolidated. "Derived" = A3 arithmetic on filed numbers, not a filed figure.

## 0. LEDGER RECONCILIATION
- Ledger accounts for 721 of 721 structured IDs (ledger line 13, orphan_ids empty). A3 read all 721 rows in the structured file and the cited fulltext line for each. Reconciled: 721 / 721 = 100%.
- Arithmetic tie-outs (all PASS): S and C P&L subtotals for all six columns; Q1 + Q2 = H1 on revenue, D&A, finance cost and PAT; S and C balance sheets foot both dates; S and C cash flows foot to closing cash (S 1.65, C 6.82); other equity roll-forward equals H1 total comprehensive income exactly (S 302.65 + 88.80 = 391.45; C 258.06 + 137.82 = 395.88); EPS = PAT / 26.111 crore shares in every column.
- Borrowings tie: S total 943.98 to 719.42 = -224.56 = repayment 17.58 + current movement 206.98. C total 1,131.60 to 860.13 = -271.47 = 64.49 + 206.98. S non-current fall 65.49 less repayment 17.58 = 47.91 reclassified to current maturities.

### Extraction notes for A4 / verifiers (A1 issues, not filer findings)
- R145 and R478 carry the label "Other equity, H1 FY26". Their values (302.65 S, 258.06 C) equal the 31 Mar 2026 balance-sheet other equity (R201 line 309; R530 line 699). The VER lines (220, 620) give only five cells for six columns. Treat both as the FY26 (31 Mar 2026) figure, not H1 FY26.
- R640 records the consolidated firm registration as "000756N". Fulltext line 520 reads "000756N/N500441", the same as the standalone report. A1 truncation, no source inconsistency.
- Derived subsidiary borrowings at 31 Mar 2026 equal 93.81 in both non-current (444.58 - 350.77) and current (687.02 - 593.21). The current gap is again 93.81 at 30 Sep 2026 (527.95 - 434.14). The arithmetic is possible, but a verifier should confirm lines 701 and 706 against the page 10 image.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R091-R096, R388-R393 | 211, 605 | "Exceptional items - Employee benefit expenses \| - \| - \| - \| - \| - \| 2.69" | AMBIGUOUS | A named employee-benefit exceptional of 2.69 (S) / 2.70 (C) hit FY26. H1 FY26 shows nil, so the charge fell in H2 FY26. The template keeps a line for this transaction class (typically a separation/VRS scheme; the filing does not name it). Ask what the FY26 charge was and whether a further scheme is planned for H2 FY27. |
| A3-02 | F1 | R442-R447, R454-R459, R466-R471 | 614 | "Profit attributable to Non Controlling interest \| - \| - \| - \| - \| - \| -" | NEUTRAL-FACT | NCI is nil in every period, so the four subsidiaries are wholly owned (implied, not stated). All subsidiary profit flows to parent shareholders. |
| A3-03 | F1 | R280-R281, R609-R610, R268, R599 | 399, 791 | "Proceeds from non-current borrowings \| 0.00 \| 44.00" | NEUTRAL-FACT | H1 FY27 raised no new term debt (H1 FY26: 44.00) and sold no PPE. The 271.47 debt fall is all repayment, with no refinancing behind it. |
| A3-04 | F2 | R115-R120, R412-R417, R055-R060, R352-R357 | 609, 215 | "Net profit/(loss) for the period (12-13) \| 74.08 \| 63.74 \| 24.55 \| 137.82 \| 77.30 \| 150.21" | AMBIGUOUS | The C-minus-S PAT gap as a % of S PAT is 34.6% (Q2 FY27), 88.9% (Q1 FY27), 6.6% (Q2 FY26). That is -54.3 pp QoQ and +28.0 pp YoY. H1 gap: 39.7% to 55.2%, +15.5 pp. All moves exceed the 5 pp trigger. Subsidiaries made 47.1% of C PAT in Q1 and 25.7% in Q2, with no entity split. Ask which subsidiary earns this and why it swings. |
| A3-05 | F2 | R025-R030, R322-R327, R031-R036, R328-R333 | 594, 200 | "(b) Purchase of stock-in-trade \| 116.22 \| 48.30 \| 78.76" | AMBIGUOUS | Subsidiary traded-goods purchases (derived C - S) were 74.11 in Q2 FY27, 30.85 in Q1 FY27, 74.71 in Q2 FY26 and 179.27 in FY26. The subsidiary revenue gap (92.31 in Q2) is mostly trading, not conversion. Subsidiary earnings ride trading margins and inventory timing: the Q2 inventory change gap is -40.92. Ask what the subsidiaries trade and from whom. |
| A3-06 | F2 | R182-R183, R511-R512 | 690, 300 | "Trade receivables \| 103.06 \| 243.32" vs S "Trade receivables \| 285.60 \| 379.70" | AMBIGUOUS | C receivables sit below S by 182.54 (31 Mar 2026: 136.38). At least 182.54, or 63.9%, of the parent's receivables are therefore owed by subsidiaries and are eliminated. Intercompany credit grew by 46.16 or more while the parent's reported receivables fell 94.10. The parent's external receivables are 103.06 or less. Ask about intercompany sale terms and settlement. |
| A3-07 | F2 | R200-R201, R529-R530, R145, R478 | 699, 309 | "Other equity \| 395.88 \| 258.06" vs S "Other equity \| 391.45 \| 302.65" | NEUTRAL-FACT | At 31 Mar 2026, C other equity was 44.59 below S, so the subsidiaries carried a net cumulative deficit or consolidation adjustments. H1 subsidiary profit of 49.02 turned the gap to +4.43. The subsidiaries' turnaround is recent. |
| A3-08 | F3 | R037-R042, R334-R339, R019-R024, R316-R321, R158-R159, R491-R492, R061-R066, R358-R363 | 596, 593, 680 | "(d) Employee benefits expense \| 31.53 \| 30.97"; "(a) Cost of materials consumed \| 944.32 \| 584.61" | AMBIGUOUS | The subsidiaries are not shells in aggregate: derived PPE of 355.79, D&A 2.43 a quarter, other expenses 28.49 a quarter. But payroll is thin at 1.41 a quarter against 355.79 of PPE. C materials cost sits below S in 4 of 6 periods (Q1 FY27: 584.61 vs 588.21), so the parent buys materials from the subsidiaries as well as sells to them. The partial-shell signature fits asset-holding or trading vehicles. Ask which of the four entities run plant and who staffs it. |
| A3-09 | F8 | R103-R114, R097-R102, R172-R173, R400-R405 | 213, 214, 295 | "Tax expense/(credit) \| - \| - \| - \| - \| - \| -"; "Deferred tax assets (net) \| 258.61 \| 258.61" | FORWARD-SIGNAL | S effective tax rate (ETR) is 0% in all six periods on positive PBT (FY26 110.03; H1 FY27 88.80). The 258.61 S deferred tax asset (DTA) did not move in H1. Derived shield against the 25.17% statutory rate: 22.35 S / 34.85 C in H1 FY27, about 2,517-2,533 bps of PBT. At 25.17%, C H1 EPS would be 3.94, not the reported 5.28. ETR step-up risk arises when the unrecognised loss pool is used up, or when DTA utilisation starts to run through P&L. No earlier-years tax adjustment line exists. |
| A3-10 | F8 | R406-R411, R501-R502, R539-R540 | 608, 685, 704 | "Deferred tax (credit) \| (0.22) \| - \| - \| (0.22)"; "Deferred tax liabilities (net) \| 9.37 \| -" | AMBIGUOUS | C DTA rose 9.59 and a new C DTL of 9.37 appeared (nil at 31 Mar 2026). Net movement +0.22 ties to the P&L credit. The gross-up means one subsidiary now carries a DTL and another holds the added DTA. This is the first tax line at subsidiary level. Ask which entity and why. |
| A3-11 | F12 | R204-R205, R212-R213, R533-R534, R543-R544, R575-R576, R607-R608, R611-R612 | 701, 706, 774 | "Borrowings (current) \| 527.95 \| 687.02"; "Changes in trade receivables \| 140.26 \| 3.50" | AMBIGUOUS | There is one reportable segment (lines 425, 819), so the segment test runs on the entity balance sheet. C borrowings fell 271.47 (-24.0%) in H1. C receivables fell 57.6% (243.32 to 103.06) while Q2 C revenue rose 9.8% YoY. That implies about 7 days of Q2 sales in receivables (derived). Of the H1 C operating cash flow of 328.46, 109.02 is a working-capital release. This could be a working-capital unwind or a durable fall in debt. Ask about receivable discounting/factoring, quarter-end timing, and whether it repeats in H2. |
| A3-12 | F12 | R190-R191, R218-R219, R519-R520, R549-R550 | 694, 709 | "Other financial assets (current) \| 667.63 \| 658.25"; "Trade payables other than MSME \| 1,444.43 \| 1,433.26" | AMBIGUOUS | Two undisclosed blocks dominate the balance sheet. Other financial assets are 21.3% of C total assets (3,131.68). Total trade payables (1,462.03) are 46.7%, about 126 days of Q2 materials plus traded purchases (derived). Payables of this size usually include acceptances or LC-backed supplier credit, which is debt-like. The filing does not name the counterparty or say whether it is a related party. Ask what makes up both lines and what the payables cost. |
| A3-13 | F14 | R688 | 57, 59 | "b) Publication of Extract of Audited Financial Results" vs "publishing Extract of Un-audited Financial Results" | NEUTRAL-FACT | The heading was carried over from a year-end template. Immaterial alone; counts toward the governance data point. |
| A3-14 | F14 | R657, R708, R717 | 460-461, 505, 811 | "its subsidiary (Holding Company and its subsidiary together referred to as “the Group”)" | AMBIGUOUS | Para 1 of the consolidated review report uses the singular. Para 4 lists four subsidiaries (lines 506-509) and Note 2 says "its subsidiaries" (line 811). A singular left in the template can mean the perimeter was one subsidiary when the template was set. Links to A3-16. |
| A3-15 | F14 | R696, R697, R712, R713, R700, R716, R630 | 225, 415, 63 | "Notes:1 Unaudited Standalone Statement of Assets and Liabilities"; "concluded at 14:35 PM IST" | NEUTRAL-FACT | "Note 1" and "Note 2" each appear twice per filing: the balance sheet and cash flow labels, then the numbered notes. The time format mixes 24-hour and PM. Cosmetic; counts toward the cumulative data point. |
| A3-16 | F15 | R659-R662, R708 | 506-509 | "Indorama Ventures Yarns Private Limited ... Indorama Sustainable Polyester Yarns Private Limited" | AMBIGUOUS | The perimeter is four subsidiaries, no JV or associate. The prior-quarter list is ND, so additions, deletions or renames cannot be diffed. Lean bear on A3-14. Ask when each of the four entered the group and whether any were renamed or reclassified in the last four quarters. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 85 ZERO_STANDING cells on 22 line items, all read. Employee-benefit exceptional line (A3-01). Nil NCI means wholly owned (A3-02). No new term debt or asset sales (A3-03). Nil tax: see F8. Nil interim OCI: see F9. New intangible of 0.04 at 30 Sep 2026 is immaterial. |
| F2 S vs C decomposition | FINDING | No JV or associate, so the gap is subsidiaries net of eliminations. PAT-gap moves exceed 5 pp in every comparison (A3-04). Trading-led subsidiary activity (A3-05). Intercompany receivables of 182.54 or more (A3-06). Subsidiary deficit at FY26 (A3-07). Table in section 4. |
| F3 Shell-entity detection | FINDING | Not shells in aggregate. Thin payroll, and C materials below S, give a partial-shell signature. Per-entity split ND (A3-08). No Going Concern EoM to reconcile. |
| F4 Unaudited contribution ratio | PASS | The consolidated review report lists four subsidiaries (lines 505-509) and has no Other Matter paragraph on component auditors or unreviewed component financials. Conclusion unmodified (line 510). Unreviewed share of C PAT stated as 0. Every period is limited review, not audit. |
| F5 Going Concern / EoM scope | PASS | Neither review report has an Emphasis of Matter or Going Concern paragraph (S lines 124-130; C lines 510-517; grep returned none). No current-quarter scope to expand. The prior-quarter verbatim diff did not run (prior extract ND), so a dropped prior EoM cannot be excluded. |
| F6 Forward-commitment phrases | PASS | Lexicon hits: line 63 "commenced" (meeting start, past tense, no commitment); lines 58-60 "would be publishing" and "being published" (procedural Reg 47 extract). The notes (lines 415-429, 805-823) hold no business commitment: no capex, project, approval or timeline. See register. |
| F7 Hedge phrases | PASS | Zero hits for the lexicon in notes or reports (grep). |
| F8 Tax forensics | FINDING | S ETR 0% in all periods; C ETR -0.3% in Q2 FY27 and 0% elsewhere; frozen DTA and shield quantified (A3-09). Subsidiary DTA/DTL gross-up (A3-10). No earlier-years tax line. Income-tax refund of 3.76 ties to the S non-current tax asset fall (8.42 to 4.66). |
| F9 OCI forensics | PASS | Interim OCI is nil in every quarter and half-year. FY26 OCI is 0.77 S / 0.75 C, so remeasurement runs at year-end only. No single-quarter swing. Verify FY27 actuarial assumptions at the Annual Report. |
| F10 Share count / dilution | PASS | Paid-up 261.11 in every period (26.111 crore shares). Basic = diluted in all 12 EPS cells: no dilutive instruments in the EPS. A4 runs the warrant/ESOP cross-check. |
| F11 Reserves / net worth tie-out | PASS | S 261.11 + 391.45 = 652.56; C 261.11 + 395.88 = 656.99. Both dates tie. The H1 roll-forward equals total comprehensive income exactly, so no dividend or other reserve movement. No third-party figure in the document to reconcile. |
| F12 Segment forensics | FINDING | One reportable segment, no segment assets or liabilities table. Test applied to the entity balance sheet: sharp debt and receivable fall (A3-11); undisclosed other financial assets and payables blocks (A3-12). |
| F13 Board outcome beyond results | PASS | Agenda items a and b only (lines 49-61): results and Reg 47 extract. No AR, AGM, record date, dividend, fund-raising enabling resolution or director appointment. No Role 6 trigger from this filing. |
| F14 Note drafting inconsistencies | FINDING | Audited vs Un-audited heading (A3-13). Singular "its subsidiary" vs four listed (A3-14). Duplicate note numbering and time format (A3-15). Note 2 "limited review" (lines 421, 815) matches both auditor reports. |
| F15 Entity list diffs | FINDING | Four subsidiaries (lines 506-509). Prior list ND, A2 flags ENTITY_CHANGE_UNKNOWN. The singular "its subsidiary" hints at a perimeter change (A3-16). |
| F16 Presentation: dropped/reframed disclosures | N.A. | Results doctype; no presentation. |
| F17 Concall silence audit | N.A. | Results doctype; no transcript. No Notion checklist exists (pre-thesis read). The filing's notes carry no business commentary, so no commitment exists to track for silence. |

## 3. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| Publish extract of unaudited Q2/H1 FY27 results in newspapers under Reg 47(1)(b) | Not stated in filing (statutory Reg 47 window after the 16 Oct 2026 meeting) | Board outcome item b, lines 57-60 (R667) | initiated ("would be publishing") |
| Publish extract on company website www.indoramaindia.com | Not stated in filing | Board outcome item b, line 60 (R668) | underway ("is also being published") |

Neither entry is a business commitment. The notes contain no capex, commissioning, approval or restructuring commitment that could feed the Role 5 promise-vs-delivery tracker or the FTTCP catalyst timeline.

## 4. F2 WORKING: S vs C GAP BY PERIOD (derived, C minus S)

| period | revenue gap | % of S revenue | EBITDA* gap | % of S EBITDA | PAT gap | % of S PAT | subs share of C PAT |
|---|---|---|---|---|---|---|---|
| Q2 FY27 | 92.31 | 7.4% | 24.52 | 26.3% | 19.03 | 34.6% | 25.7% |
| Q1 FY27 | 118.73 | 14.5% | 35.82 | 49.6% | 29.99 | 88.9% | 47.1% |
| Q2 FY26 | 54.35 | 4.7% | 9.18 | 12.9% | 1.51 | 6.6% | 6.2% |
| H1 FY27 | 211.04 | 10.2% | 60.34 | 36.5% | 49.02 | 55.2% | 35.6% |
| H1 FY26 | 175.12 | 7.4% | 37.63 | 26.3% | 21.95 | 39.7% | 28.4% |
| FY26 | 391.33 | 8.7% | 69.96 | 23.5% | 40.18 | 36.5% | 26.7% |

*EBITDA = "Profit from operations before D&A, finance costs and FX loss/(gain)" (lines 205, 599).

Q2 FY27 subsidiary bridge (C - S): revenue +92.31; other income -2.42 (intercompany interest eliminated: S H1 interest income 5.95 vs C 3.60); materials +2.28; stock-in-trade +74.11; inventory change -40.92; employee +1.41; other expenses +28.49; EBITDA +24.52; D&A +2.43; finance cost +3.34; FX -0.06; PBT +18.81; deferred tax credit +0.22; PAT +19.03.

Implied subsidiary PAT by quarter (derived): Q1 FY26 20.44, Q2 FY26 1.51, H2 FY26 18.23 (two quarters), Q1 FY27 29.99, Q2 FY27 19.03.

Subsidiary cash and funding (derived, H1 FY27): operating cash flow 108.16 (C 328.46 - S 220.30); repaid the parent 51.75 (S cash flow line 394, matching the S non-current loans fall 127.85 to 76.10); repaid external term debt 46.91 (C 64.49 - S 17.58). The parent's investment in subsidiaries is 16.10 (line 292); consolidation eliminates both the 16.10 and the 76.10 of loans.

## 5. FORWARD-SIGNAL AND AMBIGUOUS FLAGS FOR A4
- FORWARD-SIGNAL: A3-09 (zero-tax earnings; ETR step-up risk; reported EPS overstates statutory-rate EPS by about 25%).
- AMBIGUOUS (convert to management questions): A3-01, A3-04, A3-05, A3-06, A3-08, A3-10, A3-11, A3-12, A3-14, A3-16.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_results_indorama_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: FINDING
  F3: FINDING
  F4: PASS
  F5: PASS
  F6: PASS
  F7: PASS
  F8: FINDING
  F9: PASS
  F10: PASS
  F11: PASS
  F12: FINDING
  F13: PASS
  F14: FINDING
  F15: FINDING
  F16: N.A.
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "211, 605", classification: "AMBIGUOUS", implication: "Employee-benefit exceptional 2.69 S / 2.70 C in H2 FY26; line retained; ask nature and whether further scheme planned"}
  - {id: "A3-02", check: "F1", line: "614", classification: "NEUTRAL-FACT", implication: "NCI nil all periods; four subsidiaries wholly owned (implied)"}
  - {id: "A3-03", check: "F1", line: "399, 791", classification: "NEUTRAL-FACT", implication: "No new term debt (H1 FY26 44.00) and no PPE sales in H1 FY27; debt fall is pure repayment"}
  - {id: "A3-04", check: "F2", line: "609, 215", classification: "AMBIGUOUS", implication: "PAT gap % of S PAT 34.6% Q2 FY27 vs 88.9% Q1 FY27 vs 6.6% Q2 FY26; subs 25.7%-47.1% of C PAT with no entity split"}
  - {id: "A3-05", check: "F2", line: "594, 200", classification: "AMBIGUOUS", implication: "Subsidiary stock-in-trade purchases 74.11 in Q2 FY27; subsidiary revenue is trading-led, earnings ride trading margin and inventory timing"}
  - {id: "A3-06", check: "F2", line: "690, 300", classification: "AMBIGUOUS", implication: "C receivables 103.06 below S 285.60; at least 182.54 (63.9%) of parent receivables are intercompany, up at least 46.16 in H1"}
  - {id: "A3-07", check: "F2", line: "699, 309", classification: "NEUTRAL-FACT", implication: "C other equity 44.59 below S at 31 Mar 2026, +4.43 at 30 Sep 2026; subsidiary deficit erased by H1 profit"}
  - {id: "A3-08", check: "F3", line: "596, 593, 680", classification: "AMBIGUOUS", implication: "Subs hold 355.79 PPE but payroll 1.41/qtr and C materials below S in 4 of 6 periods; partial-shell or trading-vehicle signature; per-entity split ND"}
  - {id: "A3-09", check: "F8", line: "213, 214, 295", classification: "FORWARD-SIGNAL", implication: "S ETR 0% all periods, DTA frozen at 258.61; H1 FY27 shield 22.35 S / 34.85 C (~2,517-2,533 bps); C H1 EPS at statutory rate 3.94 vs reported 5.28; ETR step-up risk"}
  - {id: "A3-10", check: "F8", line: "608, 685, 704", classification: "AMBIGUOUS", implication: "C DTA +9.59 and new DTL 9.37 net to the 0.22 credit; first subsidiary-level tax line; ask entity and cause"}
  - {id: "A3-11", check: "F12", line: "701, 706, 774", classification: "AMBIGUOUS", implication: "C borrowings -271.47 (-24.0%) funded by receivables -57.6% (~7 days of sales); WC unwind vs durable deleveraging; ask factoring/discounting and H2 repeat"}
  - {id: "A3-12", check: "F12", line: "694, 709", classification: "AMBIGUOUS", implication: "Other financial assets 21.3% and trade payables 46.7% of C total assets (~126 days of purchases); composition, related-party share and cost undisclosed; payables may be debt-like"}
  - {id: "A3-13", check: "F14", line: "57, 59", classification: "NEUTRAL-FACT", implication: "Item b heading says Audited, body says Un-audited; template carryover"}
  - {id: "A3-14", check: "F14", line: "460-461, 505, 811", classification: "AMBIGUOUS", implication: "Review report para 1 says its subsidiary (singular) while para 4 lists four; possible perimeter change since template set"}
  - {id: "A3-15", check: "F14", line: "225, 415, 63", classification: "NEUTRAL-FACT", implication: "Duplicate Note 1/Note 2 numbering and 14:35 PM time format; cosmetic, cumulative governance data point"}
  - {id: "A3-16", check: "F15", line: "506-509", classification: "AMBIGUOUS", implication: "Four subsidiaries, prior list ND so no diff possible; ask entry date and any rename/reclassification in last four quarters"}
forward_signals: ["A3-09"]
ambiguous: ["A3-01", "A3-04", "A3-05", "A3-06", "A3-08", "A3-10", "A3-11", "A3-12", "A3-14", "A3-16"]
commitments:
  - {commitment: "Publish extract of unaudited Q2/H1 FY27 results in newspapers (Reg 47(1)(b))", implied_date: "not stated in filing; statutory Reg 47 window after 16 Oct 2026", ref: "Board outcome item b, lines 57-60 (R667)", status_word: "initiated"}
  - {commitment: "Publish extract on www.indoramaindia.com", implied_date: "not stated in filing", ref: "Board outcome item b, line 60 (R668)", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Three reads matter for A4. First, every rupee of reported profit is pre-tax: standalone tax is nil in all six periods while the 258.61 DTA did not move, so at 25.17% consolidated H1 EPS is 3.94, not 5.28. The tax-loss pool size is NOT FOUND here; the AR tax note decides how long the shield runs. Second, the subsidiaries supplied 25.7%-47.1% of consolidated PAT, run on trading purchases and 1.41 of payroll a quarter, and owe the parent at least 182.54 of receivables. The quarter's earnings mix and the parent's receivable quality both depend on four wholly owned entities with no per-entity disclosure. Third, the 271.47 debt fall came from a receivable release to about 7 days of sales, with payables at about 126 days. Until the factoring and acceptance terms are known, A3 treats it as working-capital timing, not proven deleveraging. Limits: prior quarter ND, so the F5 and F15 diffs did not run. R145/R478 are mislabelled H1 FY26; they are the 31 Mar 2026 balances."
```

## CONTENT PART 3: A3 FORENSICS, PRESS RELEASE (verbatim)
# A3 FORENSIC NOTES: INDORAMA Q2 FY27, doctype presentation (pressrelease: Reg 30 cover + media release, 3 pages)

Inputs read: A1 structured (R001-R132), A1 fulltext (lines 1-181), A2 ledger. Source PDF and inputs/ not opened.
Prior-quarter fulltext: ND (not available). Notion checklist: NONE (no page, no spear).
Unit: Rs crore. Table basis consolidated (line 92). Results unaudited (line 39-40).

## LEDGER RECONCILIATION
- Rows in ledger: 132 (R001-R132, orphan_ids none). Rows read at cited fulltext line: 132. Reconciled: 100%.
- Line cites verified. Minor span notes only: R020 block spans lines 64-67; R130 block spans 160-169; R131 heading at 173, text 174-180; R003 exchange name at line 23 (line 22 is the department). None changes a value.
- Arithmetic tie-out of the page 2 table (line 96-106): H1 = Q1 + Q2 holds for Total Income (940.2 + 1,344.0 = 2,284.2), EBITDA (108.0 + 117.7 = 225.7), EBIT (93.1 + 102.9 = 196.0), PAT (63.7 + 74.1 = 137.8). All margins recompute to the stated 1 dp. Four growth cells sit 0.1 pp below recompute from rounded inputs (EBITDA QoQ 8.9% vs 9.0%; EBIT YoY 77.0% vs 77.1%; EBIT QoQ 10.4% vs 10.5%; PAT QoQ 16.2% vs 16.3%). Each is reachable from unrounded inputs; not a finding.
- Derived prior-year quarter (H1FY26 minus Q2FY26): Q1FY26 Total Income 1,308.5; EBITDA 100.3; EBIT 81.8; PAT 52.7; implied D&A 18.5.

## FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | R114, R115, R116, R117 | 139-140 | "we plan to invest approximately X200 crore over the next 12—18 months to diversify in specialty fibre and filament products" | FORWARD-SIGNAL | First quantified diversification spend. Rs 200 cr = 0.89x H1FY27 EBITDA (225.7, line 98). Window from 16 Oct 2026 ends Oct 2027 to Apr 2028. No funding source, board approval, tonnage, product list, start date or return target stated. Feeds Role 5 promise tracker and FTTCP catalyst timeline. |
| FN-02 | F16 | R049, R051, R070, R072, R104 | 73-74; 100; 130-131 | "Marks a Strong Quarter of Profit Growth and Margin Expansion"; "EBITDA Margin % 8.8% 6.6% 11.5%"; "higher raw material costs and continued volatility across the polyester value chain" | FORWARD-SIGNAL | Headline margin expansion is YoY only. QoQ EBITDA margin fell 270 bp (11.5% to 8.8%) and PAT margin 130 bp (6.8% to 5.5%). CMD calls the crude-led cost pressure "continued". Lean bear: Q3 spread at risk if crude stays high. |
| FN-03 | F16 | R036, R038, R039, R040, R079, R080 | 96; 111-113 | "degrowth of 9.7% due to supply chain issues in view of geopolitical issues in the middle east" | AMBIGUOUS | Derived Q1FY27 total income 940.2 vs Q1FY26 1,308.5 = -28.1% YoY; release states only the H1 -9.7%. Q2FY27 1,344.0 is just 2.7% above Q1FY26. The +43.0% QoQ is a rebound from a disrupted Q1. The release gives no volume or realisation split; crude-led price pass-through could carry the +10% YoY. Question: Q2 volumes and realisations YoY and QoQ; is supply chain normal now. |
| FN-04 | F16 | R014, R021, R033, R035, R102 | 75; 96; 129 | "For Q2FY27 Revenue Growth of 10% y-o-y"; "Total Income 1,344.0 \| 1,222.4 \| 10.0%"; "revenue from operations improving" | AMBIGUOUS | Headline "revenue" growth is Total Income growth. Revenue from operations and other income are not disclosed. EBITDA margin recomputes on Total Income (117.7 / 1,344.0 = 8.76%), so other income may sit inside EBITDA. Question: revenue from operations and other income for Q2FY27, Q2FY26, Q1FY27; is other income in EBITDA. |
| FN-05 | F16 | R041, R042, R044, R054, R055, R057 | 98; 102 | "EBITDA 117.7 80.4 46.4% 108.0"; "EBIT 102.9 58.1 77.0% 93.1" | AMBIGUOUS | Implied D&A (EBITDA minus EBIT): 14.8 Q2FY27, 22.3 Q2FY26, 14.9 Q1FY27, 18.5 Q1FY26 (derived). D&A down 7.5 cr YoY (-34%), which supplies 16.7% of the 44.8 cr EBIT increase. Readings: asset sale or impairment lowering the base, useful-life change, or a Q2FY26 one-off. Question: depreciation and amortisation by quarter and the cause of the fall. |
| FN-06 | F8 | R054, R055, R057, R060, R062, R065, R068 | 102; 104 | "EBIT 102.9 58.1 ... 93.1 ... 139.9"; "PAT 74.1 246 ... 63.7 ... 77.3" | AMBIGUOUS | EBIT minus PAT (finance cost + tax + any exceptional, not split in the release): 28.8 Q2FY27, 33.5 Q2FY26, 29.4 Q1FY27, 29.1 Q1FY26 (derived). The wedge is flat at 28.8-29.4 cr in 3 of 4 quarters while EBIT moves 81.8-102.9 cr. A flat wedge fits finance cost with little profit-linked tax. Reading A: near-nil tax (loss carry-forward or DTA); at 25.17% on implied PBT 74.1, PAT would be about 55.4 cr (-25%), an ETR step-up risk. Reading B: full tax already charged, which needs finance cost near 3.9 cr in Q2FY27 vs about 25.2 cr in Q2FY26. Separating observation: finance cost and tax lines in the results filing. Lean bear on Reading A. |
| FN-07 | F14 | R063, R092, R071 | 104; 120 | "PAT 74.1 246 201.8%"; "compared with X24.6 crore in Q2 FY26" | NEUTRAL-FACT | Table value 246 is a decimal glyph loss. 24.6 is confirmed three ways: PAT margin 2.0% (24.6 / 1,222.4 = 2.01%), H1FY26 77.3 minus 24.6 = 52.7 (246 would exceed H1), YoY 201.8% fits an unrounded base near 24.55. Use 24.6. |
| FN-08 | F14 | R030, R027, R028, R029 | 85; 89 | "Yoy Yoy Yoy" | NEUTRAL-FACT | Card YoY percentages are absent from the text layer (likely graphic). Card values are rounded (118 Cr, 74 Cr) versions of table values 117.7 and 74.1. No conflict; FOOTNOTE_UNRESOLVED stands. |

## CHECKLIST SCORECARD
| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Press release, no statutory template; A2 ledger zero_standing 0 (ledger line 34). |
| F2 Standalone vs consolidated | N.A. | Consolidated only (line 80, 92); no standalone figures in doc. |
| F3 Shell-entity detection | N.A. | No standalone cost lines, no entity list. |
| F4 Unaudited contribution ratio | N.A. | No auditor report or Other Matters para; results "Un-audited" (line 39-40). |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph; prior-quarter fulltext ND. |
| F6 Forward-commitment mining | FINDING | FN-01: Rs 200 cr capex, 12-18 months (line 139). Lexicon note: no exact-phrase hit ("will be", "commenc", "board has approved" absent); "is expected to broaden" (line 140) is the nearest. Commitment captured as dateable. |
| F7 Hedge phrase mining | PASS | Only lexicon hit is safe-harbor boilerplate "subject to risks and uncertainties" (line 175). No prior deck to diff for newly added hedges. |
| F8 Tax forensics | FINDING | No tax, PBT or finance-cost line; ETR not computable. FN-06: flat EBIT-to-PAT wedge implies either sub-statutory tax or a finance-cost collapse. |
| F9 OCI forensics | N.A. | No OCI data. |
| F10 Share count and dilution | N.A. | Release carries no paid-up capital, share count or EPS. |
| F11 Reserves and net worth | N.A. | Release carries no equity or net worth figure. |
| F12 Segment forensics | N.A. | No segment data. |
| F13 Board outcome | N.A. | No board outcome in this document; board meeting times absent. Cover signed 2026.10.16 21:47:58 (line 52). A4 to read the results filing for board items. |
| F14 Drafting inconsistencies | FINDING | FN-07 (246 vs 24.6), FN-08 (card YoY blanks). Both text-layer artefacts, resolved or neutral. Cover title "INDORAMA Marks..." (line 41) vs page 2 "Indo Rama Synthetics Marks..." (line 73): cosmetic. |
| F15 Entity list diffs | N.A. | No consolidation entity list; prior ND. |
| F16 Dropped / reframed disclosures | FINDING | Cross-deck diff not possible (prior ND). Within-document reframing: FN-02 (margin headline YoY only), FN-03 (H1 cause stated, Q1 -28.1% YoY not stated), FN-04 (Total Income labelled revenue), FN-05 (undisclosed D&A fall lifts EBIT growth). |
| F17 Silence audit | N.A. | Concall-specific; no transcript in this doctype; no Notion checklist exists. Disclosure gaps for A4 listed below. |

## COMMITMENT REGISTER (F6)
| commitment | implied date | ref | status word |
|---|---|---|---|
| Invest approx. Rs 200 cr to diversify into specialty fibre and filament products | Oct 2027 to Apr 2028 (12-18 months from 16 Oct 2026) | line 139 (R114-R116) | planned (pre-initiation; not initiated/underway/completed) |
| Investment to broaden portfolio, raise value-added participation, support growth | medium term, undated | line 140-142 (R117) | expected |
| Further strengthen operating and financial performance | undated | line 138 (R113) | aspirational, no milestone |

## DISCLOSURE GAPS FOR A4 (not an F17 silence audit; one-quarter view, consecutive count ND)
| item absent from the release | relevance |
|---|---|
| Revenue from operations, other income | FN-04 |
| Volumes, realisations, product mix | FN-03 |
| Depreciation, finance cost, tax, exceptional items | FN-05, FN-06 |
| Funding plan, board approval, tonnage for Rs 200 cr capex | FN-01 |
| Debt, net worth, cash flow | F10/F11 not testable |
| Q1FY27 YoY decline (derived -28.1%) | FN-03 |

## A4 FLAGS
- FORWARD-SIGNAL: FN-01, FN-02.
- AMBIGUOUS (convert to management questions): FN-03, FN-04, FN-05, FN-06.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "presentation (pressrelease: Reg 30 cover + media release)"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_pressrelease_indorama_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "139-140", classification: "FORWARD-SIGNAL", implication: "Rs 200 cr specialty fibre/filament capex over 12-18 months (window Oct 2027-Apr 2028); 0.89x H1 EBITDA; no funding, approval, tonnage or returns stated"}
  - {id: "FN-02", check: "F16", line: "73-74; 100; 130-131", classification: "FORWARD-SIGNAL", implication: "Margin expansion headline is YoY only; QoQ EBITDA margin 11.5% to 8.8% (-270 bp); CMD says cost volatility continued; Q3 spread risk"}
  - {id: "FN-03", check: "F16", line: "96; 111-113", classification: "AMBIGUOUS", implication: "Derived Q1FY27 total income -28.1% YoY; Q2FY27 only 2.7% above Q1FY26; +43% QoQ is rebound; volume vs price split absent"}
  - {id: "FN-04", check: "F16", line: "75; 96; 129", classification: "AMBIGUOUS", implication: "Headline revenue growth is Total Income growth; revenue from operations and other income undisclosed; other income may sit in EBITDA"}
  - {id: "FN-05", check: "F16", line: "98; 102", classification: "AMBIGUOUS", implication: "Implied D&A 14.8 vs 22.3 YoY (-34%) supplies 7.5 of 44.8 cr EBIT growth; cause undisclosed"}
  - {id: "FN-06", check: "F8", line: "102; 104", classification: "AMBIGUOUS", implication: "EBIT-PAT wedge flat 28.8-29.4 cr in 3 of 4 quarters; either near-nil tax (statutory tax would cut PAT to about 55 cr) or finance cost fell to about 3.9 cr; results filing separates"}
  - {id: "FN-07", check: "F14", line: "104; 120", classification: "NEUTRAL-FACT", implication: "Q2FY26 PAT table 246 is glyph loss; 24.6 confirmed by margin, H1 and YoY tie-outs"}
  - {id: "FN-08", check: "F14", line: "85; 89", classification: "NEUTRAL-FACT", implication: "Card YoY percentages absent from text layer; card values are rounded table values"}
forward_signals: ["FN-01", "FN-02"]
ambiguous: ["FN-03", "FN-04", "FN-05", "FN-06"]
commitments:
  - {commitment: "Invest approx. Rs 200 cr to diversify into specialty fibre and filament products", implied_date: "Oct 2027 to Apr 2028", ref: "line 139 (R114-R116)", status_word: "planned"}
  - {commitment: "Broaden portfolio, raise value-added participation, support growth", implied_date: "medium term, undated", ref: "line 140-142 (R117)", status_word: "expected"}
  - {commitment: "Further strengthen operating and financial performance", implied_date: "undated", ref: "line 138 (R113)", status_word: "aspirational"}
gate_a3: pass
blank_checks: []
analyst_note: "This is a press release only. It carries no notes, auditor text, standalone, segment or balance sheet data, so F1-F5, F9-F13, F15 and F17 are N.A. No prior deck exists, so F16 is a within-document reading. FN-06 is the load-bearing item. EBIT minus PAT holds at 28.8-29.4 cr in three of four quarters while EBIT moves from 81.8 to 102.9 cr. A flat wedge fits finance cost with little profit-linked tax. In that case, 74.1 cr PAT carries a tax shield, and at 25.17% on implied PBT PAT would be about 55 cr. The other reading needs finance cost near 3.9 cr, against about 25 cr a year earlier. The finance cost and tax lines in the results filing separate the two readings. The 202% PAT headline rests on a weak base of 24.6 cr. Derived Q1FY27 income fell 28.1% YoY, and Q2FY27 is only 2.7% above Q1FY26. Margin fell 270 bp QoQ while the headline claims expansion. The Rs 200 cr capex states no funding, tonnage or approval."
```

## CONTENT PART 4: A3 FORENSICS, CAPEX LETTER (verbatim)
# A3 FORENSIC NOTES: INDORAMA, Q2 FY27, doctype results (file tag "capex": Reg 30 Board Outcome, capex approval, 16-Oct-2026)

Inputs read: A1 structured `runs/indorama-q2fy27/extracted/indorama-capex-q2fy27-structured.md` (R001-R047), A1 fulltext `runs/indorama-q2fy27/extracted/indorama-capex-q2fy27-fulltext.md` (62 lines, 1 page), A2 ledger `runs/indorama-q2fy27/work/ledger_capex_indorama_q2fy27.md`. Prior-quarter fulltext: ND. Notion checklist: NONE (no page, no spear on record). Source PDF and `inputs/` not opened.

Document scope: a one-page Regulation 30 letter. It carries one agenda item (capex approval). It carries no financial statements, no notes, no auditor report, no segment data, no entity list. Most balance-sheet checks (F1-F5, F8-F12, F15) therefore have nothing to test and are marked N.A. with that basis.

## LEDGER RECONCILIATION (47 of 47 rows read at cited line = 100%)

| Ledger group | Row IDs | Read at fulltext line | Result |
|---|---|---|---|
| A01 capex approval | R011, R022, R023, R027, R030, R031, R042, R044 | 37-41 | Verbatim match. R022 full name "Indo Rama Synthetics (India) Limited" is not on line 39; line 39 reads "in the Company"; the full name sits at lines 51 and 59. Meaning unchanged. R027 "Board of / Directors" spans lines 37-38. |
| A01a timeline | R012, R032, R040, R043 | 42-43 | Verbatim match. "12-18" on line 42, "months" on line 43. |
| A01b financing | R033, R034, R046 | 43-44 | Verbatim match. "internal accrual" closes on line 44. |
| Entities | R018-R029 | 21-62 | Match. R018 cites line 21; line 21 is "Corporate Listing Department", the NSE name is on line 22 and "NEAPS" on line 26. R024 "Butibori Plant," line 41, "Nagpur, Maharashtra" line 42. Cite drift only. |
| Signature | R013, R014, R028, R039, R047 | 52-56 | Verbatim match. |
| Reference / addressing | R001-R008, R020, R035 | 18-29 | Verbatim match. |
| Dates / LODR basis | R009, R010, R036, R037, R038, R041, R045 | 19, 36-38, 62 | Verbatim match. |
| Address / CIN | R015, R016, R017, R029 | 60-62 | Verbatim match. |

A2 flags carried and tested: SPLIT_NOT_STATED (confirmed, FN-04), FUNDING_UNQUANTIFIED (confirmed, FN-03), MEETING_TIMES_ABSENT (confirmed, FN-05). No row unread. No orphan ID.

## FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FN-01 | F6 | A01: R011, R030, R031, R024-R026, R042 | 38-41 | "have considered and approved expansion plan of approx. INR 200 Crores ... towards capex for speciality filament and speciality Fibre production at Butibori Plant" | FORWARD-SIGNAL | A dated board-approved capex commitment of about Rs 200 Cr aimed at speciality (not commodity) filament and fibre at the existing Butibori site. Feeds the Role 5 promise-vs-delivery tracker. A4 asks: capacity added (tpa), product mix, incremental revenue at full use, and whether the spend is brownfield on existing land and utilities. |
| FN-02 | F6 | A01a: R012, R032, R040, R043 | 42-43 | "with an estimated commercial operation date in next 12-18 months" | FORWARD-SIGNAL | Commissioning window 16-Oct-2027 to 16-Apr-2028 (12-18 months from the 16-Oct-2026 meeting, line 38). Earliest revenue contribution falls in Q3 FY28; latest in Q1 FY29. Catalyst-timeline entry. The word "estimated" means the tracker holds a range, not a date. A4 asks for the milestone path (orders for machinery, civil start, trial run). |
| FN-03 | F6 | A01b: R033, R034, R046 | 43-44 | "The projects would be financed by taking term loan for the same with mix of internal accrual." | AMBIGUOUS | Debt is the named primary source; the debt-to-accrual split is not quantified. Conservative read: up to most of Rs 200 Cr is new term debt, with interest cost running ahead of revenue during the 12-18 month build. A term-loan sanction is a likely follow-on disclosure. A4 asks: loan quantum, lender, tenor, rate, which entity borrows, and whether the term loan is already sanctioned. |
| FN-04 | F13 | A01: R022, R023, R044 | 39-40 | "in the Company and its Wholly Owned Material Subsidiary, i.e., Indorama Ventures Yarns Private Limited (IVYPL)" | AMBIGUOUS | One outlay spans two entities with no split stated. The split decides where the assets, the term loan and the future revenue land, so it decides the standalone-vs-consolidated read in later results (F2/F3 next quarter). IVYPL is named a "Material Subsidiary". A4 asks: Rs split between the Company and IVYPL, which product line sits in which entity, and how IVYPL is funded (equity infusion, inter-corporate loan, or its own term loan). |
| FN-05 | F14 | A01, R037, R014, R039 | 38, 53 | "in their meeting held today, i.e., 16th October 2026" / "Date: 2026.10.16 14:51:58 +05'30'" | AMBIGUOUS | The letter states no meeting start or end time. With only the 14:51:58 signature time, the timeliness of the board-outcome disclosure against meeting close cannot be tested from the document. Individually minor; a governance data point. A4 or Claude web checks meeting times and the exchange dissemination time on NSE/BSE. |
| FN-06 | F14 | R001, R002, R035, R009 | 18, 31, 36 | "IRSL: STEXCH:2026-27:" / "Disclosure under Regulations 30" / "Pursuant to Regulation 30" | NEUTRAL-FACT | Reference number ends in a trailing colon with no serial. Subject line says "Regulations 30", body says "Regulation 30". Immaterial drafting slips; logged for the cumulative governance count only. Not routed to A4. |

## CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing line items | N.A. | No financial table; ledger line_items count 0, no ZERO_STANDING rows. |
| F2 Standalone vs consolidated decomposition | N.A. | No standalone or consolidated figures in the letter. |
| F3 Shell-entity detection | N.A. | No cost lines. IVYPL is described as an operating capex site entity (line 40-41), no cost data to test. |
| F4 Unaudited contribution ratio | N.A. | No auditor report; ledger auditor_paras count 0. |
| F5 Going concern / EoM scope tracking | N.A. | No EoM paragraph; prior-quarter fulltext ND. |
| F6 Forward-commitment phrase mining | FINDING | FN-01, FN-02, FN-03. "approved" (lines 38-39, equivalent of "board has approved"), "estimated commercial operation date" (line 42), "would be financed" (line 43). |
| F7 Hedge phrase mining | PASS | Zero lexicon hits (no "subject to", "no assurance", "evaluating", "exploring", "in discussions", "endeavour", "may sometimes", "could have an effect"). Non-lexicon qualifiers "approx." (line 39), "estimated" (line 42) and "would be" (line 43) are carried on the F6 commitment rows. |
| F8 Tax forensics | N.A. | No P&L or tax lines. |
| F9 OCI forensics | N.A. | No OCI lines. |
| F10 Share count and dilution | N.A. | No paid-up capital or EPS data; no equity-raise item in the board outcome. |
| F11 Reserves and net worth tie-out | N.A. | No balance-sheet data. |
| F12 Segment forensics | N.A. | No segment data. Capex will add segment assets in a later quarter; trend from next results. |
| F13 Board outcome beyond the results | FINDING | FN-04. Single agenda item: capex approval funded by term loan plus accruals. No AR, AGM, record date, director, auditor, ESOP or capital-raising enabling resolution (ledger line 20). |
| F14 Note drafting inconsistencies | FINDING | FN-05 (meeting times absent), FN-06 (reference serial missing; "Regulations"/"Regulation"). |
| F15 Entity list diffs | N.A. | No consolidation list; prior-quarter list ND (ledger line 23). |
| F16 Presentation: dropped and reframed disclosures | N.A. | Not a presentation (doctype results). |
| F17 Concall silence audit | N.A. | Not a concall; no Notion checklist exists (pre-thesis read). |

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Capex of approx. Rs 200 Cr across the Company and IVYPL for speciality filament and speciality fibre at Butibori | approved 16-Oct-2026 | line 38-41 (R011, R030, R031) | approved (not yet initiated) |
| Commercial operation of the speciality filament and fibre capacity | 16-Oct-2027 to 16-Apr-2028 (estimated) | line 42-43 (R012, R032, R040) | approved (not yet initiated) |
| Financing by term loan with a mix of internal accrual, split not stated | not stated (before or during build) | line 43-44 (R033, R034, R046) | proposed ("would be") |

## A4 ROUTING
Forward signals: FN-01, FN-02. Ambiguous (convert to management questions): FN-03, FN-04, FN-05.

```yaml
stage: A3-forensics
company: "INDORAMA"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/indorama-q2fy27/work/forensics_capex_indorama_q2fy27.md"
ledger_reconciled_pct: 100        # 47 of 47 rows read at cited line
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: N.A.
findings:
  - {id: "FN-01", check: "F6", line: "38-41", classification: "FORWARD-SIGNAL", implication: "Board-approved capex approx Rs 200 Cr for speciality filament and speciality fibre at Butibori; tracker entry; ask capacity, mix, revenue at full use, brownfield scope."}
  - {id: "FN-02", check: "F6", line: "42-43", classification: "FORWARD-SIGNAL", implication: "Estimated COD 16-Oct-2027 to 16-Apr-2028; earliest revenue Q3 FY28, latest Q1 FY29; catalyst timeline holds a range; ask milestone path."}
  - {id: "FN-03", check: "F6", line: "43-44", classification: "AMBIGUOUS", implication: "Term loan plus internal accrual, split unquantified; lean bear: most of Rs 200 Cr may be new debt with interest ahead of revenue; ask quantum, lender, tenor, rate, borrowing entity, sanction status."}
  - {id: "FN-04", check: "F13", line: "39-40", classification: "AMBIGUOUS", implication: "Outlay spans Company and IVYPL (wholly owned material subsidiary) with no split; decides where assets, debt and revenue land in standalone vs consolidated; ask split and IVYPL funding route."}
  - {id: "FN-05", check: "F14", line: "38, 53", classification: "AMBIGUOUS", implication: "No meeting start/end time; only signature 14:51:58; disclosure timeliness untestable; verify meeting times and exchange dissemination time."}
  - {id: "FN-06", check: "F14", line: "18, 31, 36", classification: "NEUTRAL-FACT", implication: "Reference number has no serial; 'Regulations 30' vs 'Regulation 30'; immaterial drafting slips, cumulative governance count only."}
forward_signals: ["FN-01", "FN-02"]
ambiguous: ["FN-03", "FN-04", "FN-05"]
commitments:
  - {commitment: "Capex approx Rs 200 Cr, Company plus IVYPL, speciality filament and speciality fibre, Butibori", implied_date: "approved 2026-10-16", ref: "line 38-41 (R011, R030, R031)", status_word: "approved (not yet initiated)"}
  - {commitment: "Commercial operation of new speciality capacity", implied_date: "2027-10-16 to 2028-04-16 (estimated)", ref: "line 42-43 (R012, R032, R040)", status_word: "approved (not yet initiated)"}
  - {commitment: "Financing by term loan with mix of internal accrual, split not stated", implied_date: "not stated", ref: "line 43-44 (R033, R034, R046)", status_word: "proposed"}
gate_a3: pass
blank_checks: []
analyst_note: "One-page Reg 30 letter tagged doctype results; it holds no financials, so F1-F5, F8-F12 and F15 are N.A. on content, not skipped. The forward content is three parameters, each softened: amount 'approx.', date 'estimated', funding 'would be'. The two missing splits matter more than the hedges. Company vs IVYPL decides which books carry the asset, the loan and the revenue, so next quarter's F2/F3 standalone-vs-consolidated read depends on it. Debt vs accrual decides leverage and interest drag during a 12-18 month build with no revenue. Lean bear on funding until the term-loan sanction is disclosed. 'Speciality' product language is a possible mix-shift signal; A3 does not judge it, A4 should ask for capacity and mix. Structured-file cite drift (R018 line 21 vs 22; R022 full name not on line 39) does not change any meaning. No prior-quarter text and no Notion checklist, so no diff or silence audit was possible."
```

## CONTENT PART 5: A5 AUDIT VERDICT (work/blocks/a5.yaml, loop 2)
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
