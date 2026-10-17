# A4 MERGED REVIEW: SUPREMEPWR (Supreme Power Equipment Limited), H1 FY27 results

Run type: FULL QUARTER, results filing only (SME half-yearly filer; no concall, no presentation). Protocol: Role 4, Quarterly Results Review Protocol v1.4. Role 5 not passed.
Review date: 2026-10-17. Analyst: A4 (claude-opus-5-5). Revision: CORRECTION LOOP 2 (audit items M-2 two-way intercompany flows, M-3 unrealised profit in Danya stock, A3-18 H2FY26 caveat, 589-ID register, style items). Loop 1 items (M-4 to M-7, C-1, F-1 to F-3) stand.
Inputs: A1 structured (R001-R554), A1 fulltext (verbatim reads at lines 1-60, 115-131, 190-197, 237-239, 290-339, 464-485, 655-699, 752, 838-862, 874-1193), A2 ledger (M01-M35; M19-M35 added in A2 loop 2), A3 forensics (correction loop 2: section 6 register at 589 IDs, 6a and 6d targeted reviews, A3-17, A3-18, table 3d), orchestrator Notion copy. Source PDF and inputs/ not opened.
Framing: **PRE-THESIS READ.** No Notion company page, no companies/SUPREMEPWR.md, no Spear line. Decision Status ND. Every thesis field below is ND 'not passed'.

Anchor convention: "L###" = A1 fulltext line; "R###" = A1 structured row; "M##" = A2 missing-row id; "A3-##" = A3 finding. A row anchor applies to every period cell on that row (A1 extracted each line item from one fulltext line). Derived cells name their formula and inputs.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 21 notes / 0 turns / 0 slides. All 21 reviewed. Findings incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18].

**Reconciliation basis: A3 section 6 ledger review register.** The A2 ledger carries 589 IDs: 554 structured rows (R001-R554; referenced 554, orphans 0) and 35 MISSING_FROM_STRUCTURED rows (M01-M35; M12-M18 added in A2 correction loop 1, M19-M35 in loop 2). A3 section 6 disposes of every one of the 589:
| Disposition (A3 section 6) | IDs | Where listed |
|---|---|---|
| CITED by a finding when first raised | 156 (154 in 6c + M33, M34 cited by A3-18) | A3 6c, 6d |
| ROUTED to a finding in a correction loop | 138 (136 in 6b + R512, R532 routed to A3-18) | A3 6b, 6d |
| REVIEWED, NO FINDING (read at its fulltext line; ties or no forensic content) | 295 (280 in 6b + 15 in 6d) | A3 6b, 6d |
| **Total** | **589 = 554 R + 35 M; zero unaccounted** | A3 6 count check (416 in 6b + 154 in 6c + 19 in 6d) |

A4 checks on the register:
- The 21 notes each carry a disposition: SA notes R516, R517, R522, R523 reviewed no finding; R518 routed A3-05; R519 cited A3-07; R520 cited A3-11; R521 cited A3-10. CON notes R536, R537, R543, R544 reviewed no finding; R538 routed A3-16; R539 cited A3-12 / A3-04; R540 cited A3-07; R541 cited A3-10; R542 cited A3-11. CF notes R525, R526, R546, R547 reviewed no finding. Every note also appears in table 0D below.
- M12-M18 (A3 6a): M12, M13, M16, M18 reviewed no finding; M14 routed A3-14; M15 routed A3-15; M17 routed A3-12.
- M19-M35 and two re-routed R rows (A3 6d, 19 IDs): M19-M32 and M35 (status headers, signing dates, period titles, date mentions, SA CF notes text layer) reviewed no finding; M33, M34 cited A3-18; R512, R532 (P&L column status labels) moved from 6b and routed A3-18. A3 6d tests pass: every column audit-status label matches the review scope, and every signing date reads 16-10-2026 (M28 "6-10-2026" is an OCR drop, twin L1143).
- Supporting counts (A2 count test, all matched): line items 153 (+M12-M15), zero-standing 13 (+8 from M01-M07, M09), agenda items 2, auditor paragraphs 9 structured (the ledger carries M10, M11, M16, M17 separately as MISSING_FROM_STRUCTURED, count-test line 8 and section 5), entities 20 (+M18), forward 10, dates 35 (+14 fulltext date lines in M19-M32), qualifiers 48 (+M19-M22, M33-M35), notes 21.
- No unreviewed row exists on the register. Proceed.

**Updated A3 findings and how this review uses them.**
| A3 change (loops 1 and 2) | Use in this review |
|---|---|
| A3-18 new, loop 2 (NEUTRAL-FACT: the H2FY26 column is a balancing figure between audited FY26 and H1FY26, labelled "Unaudited", with no balancing-figure note and no Other Matter on comparatives; no auditor signed it off at the half level) | Caveat carried on every H2FY26-based comparison: 1-SVC H2FY26 column (A3-02 revenue and EBITDA gaps, A3-03 employee cost cell), Step 3 HoH steps, Step 5-D Danya HoH trend, Step 6.5 trailing base, Q9. H2FY26 deltas are weighted below YoY reads of H1FY27 vs H1FY26 and below FY26 audited figures. No management question (A3: none needed). |
| A3-13 reclassified NEUTRAL-FACT (Mar-26 SA receivables and the SA CF receivables change are the scan's 5-read-as-8 OCR defect; reclass reading eliminated) | Management question removed (was Q13). Routed to A1 for re-read (list below). Neither value is used as a line metric. |
| A3-17 new (SA other current liabilities fell Rs 4.00 Cr after the FY26 Rs 14.56 Cr build) | Step 5 cash answer; Q17; monitorables 3 and 6. |
| A3-14 amended (FY26 SA CFO likely carries about Rs 2.12 Cr non-cash Danya profit; Mar-25 investment is the separating observation) | Step 5-SA CFO/PAT row; Q14. |
| A3-16 amended (parent left full share in Danya and injected Rs 2.75 Cr; minority drew Rs 0.20 Cr; Danya term debt moved to the parent; no interest on capital to the parent) | Step 5-D Danya capital probe; Q12, Q13. |
| A3-04 amended (Danya-attributable receivables figures; the 163.42 to 1,031.24 roll depends on the A3-13 reading) | Q11 wording; the conditional roll is NOT used. The consolidated-minus-standalone build is used only as a bound that holds under every reading (Step 2). |
| A3-10 amended (implied fixed Rs 135 price behind the frozen diluted count) | 0C; Q18. |
| A3-15 amended (A1 routing list widened: R153, R190, R382, R383, R185, R169/R195, R252, M08, M15) | A1 routing list below; no A4 figure rests on those cells except where noted. |
| Table 3d (tax shown gross: current tax in ST provisions, advance tax in other current assets) | Step 5 working-capital ratios use receivables, inventory and trade payables only; both tax balances are excluded, never one without the other. |

**A3 section 0a handling (A1 rows that fail arithmetic).** These go back to A1; they are NOT replacement values. This review therefore:
- marks SA H1FY27 Total Expenses (R043) ND and computes every SA margin from PBT, D&A, finance cost and other income, which tie across L896, L899, L901 and L976;
- carries SA H1FY27 Other Direct Expenses (R023, 312.82 lakh) with a 0.30 lakh residual noted;
- reads SA H1FY26 deferred tax (R065) as a 0.30 lakh CREDIT (PAT arithmetic ties only with a credit);
- uses SA Mar-26 MSE trade payables at 2,879.29 lakh (L937 OCR, ties to CF L991), not the text-layer 2,870.29;
- uses SA Mar-26 other creditors at 3,074.78 lakh (R108, OCR_UNCERTAIN; the L939 cell is garbled, and the value ties as 5,954.07 - 2,879.29 = 3,074.78 per A3 0a);
- does NOT use SA Mar-26 trade receivables (R130) or the SA CF receivables change (R153) for any days or change metric (A3-13). One exception, stated where used: the consolidated-minus-standalone receivables build in Step 2 is quoted only as a lower bound, because every candidate reading (R153 as extracted, the A3 arithmetic reading, the R130-based balance-sheet change) gives the same direction and at least the same size;
- reads the 109.73 lakh partnership-share deduction (R147/R148) as the H1FY27 column (A3 0a);
- reads CON prior-year tax as 0.37 lakh charge in H2FY26 and FY26, nil in H1FY27 and H1FY26 (A3 0a);
- uses CON DTL 30-Sep-26 at 227.39 lakh (footing confirmed);
- uses CON H1FY27 investing at the A3-tied 849.05 only for context; no metric here depends on it.

**Routed to A1 for re-read (pipeline items, not management questions).** R130 and R153 (Mar-26 SA receivables 4,821.09 vs arithmetic 4,521.09; CF change 718.82 vs 715.82; A3-13); R043, R023 (SA total expenses footing); R065 (sign); R106 (2,870.29 vs 2,879.29); R141 (4.37 vs 5.37); R169 / R195 (0.06-0.07); R185 (0.99); R190 (3,557.49 vs 3,337.49); R252 (2,851.06 vs 2,851.66); R382 (3.39 vs 33.39); R383 (849.08 vs 849.05); M08, M14, M15 (unreadable); R289 (value correct, OCR_UNCERTAIN flag missing); R117 / R118 (SA intangible assets 5.02 / 5.61: values correct, but the line anchor is L945, the section header; the values sit at L947). Note for A1, no value impact: the "Paid up Equity Share Capital" rows in both P&Ls (L909 SA, L1083 CON) carry no value in any column; share capital is taken from the balance sheet (R091/R092 L926). Source: A3 0a, A3-13, A3-15, A3 6a; A4 loop 2 read of L909, L945-L947, L1083.

---

## STEP 0. PRE-FLIGHT

### 0A. Notion fetch
| Field | Value | Source |
|---|---|---|
| One-line thesis | ND 'not passed' (no Notion page) | notion-thesis.md L2-L6 |
| Four-pillar destination PE | ND 'not passed' | notion-thesis.md L6 |
| Bear/Base/Bull projections | ND 'not passed' | notion-thesis.md L6 |
| Thesis-broken conditions | ND 'not passed' | notion-thesis.md L6 |
| Monitoring checklist | ND 'not passed' | notion-thesis.md L5 |
| Position size / cost basis | ND 'not passed' | notion-thesis.md L5 |
| **Decision Status (verified first)** | **ND (no page). Treated as NOT HELD. No HOLD/ADD/TRIM/EXIT framing used.** | notion-thesis.md L5 |
| Devil's Advocate split | ND 'not passed' | notion-thesis.md L6 |
| Spear line | ND (companies/SUPREMEPWR.md absent) | notion-thesis.md L3 |
| Prior Questions-for-Management table | ND (first review; answer-status tracking not possible) | notion-thesis.md L6 |

### 0B. Units
All figures in the filing are Rs Lakhs, except share counts and EPS (R511 L879; R514 L922; R524 L971; R531 L1033; R533 L1099; R545 L1149). This review converts to **Rs Crores at 1 Cr = 100 Lakhs (divide by 100)**. Day counts use 183 days for Apr-Sep and 182 days for Oct-Mar.

### 0C. Share count changes
| Item | Value | Anchor |
|---|---|---|
| Paid-up share capital 30-Sep-26 / 31-Mar-26 | Rs 24.99 Cr / Rs 24.99 Cr (2,499.11 lakh both) | R091, R092 L926 (the P&L "Paid up Equity Share Capital" rows at L909 and L1083 carry no value) |
| Basic weighted shares, all four periods | 2,49,91,135 | R079-R082 L910 |
| Diluted weighted shares H1FY27 / H2FY26 / H1FY26 / FY26 | 2,50,67,330 / 2,50,67,330 / 2,49,91,135 / 2,50,67,330 | R083-R086 L911 |
| Split, bonus, rights, QIP, buyback in any period | None disclosed | Notes R516-R523 |
| Convertible warrants outstanding | 12,47,000, allotted 27-Aug-2025, 25% paid (Rs 42.25), Rs 126.75 balance payable only if the holder exercises, 18-month exercise window; zero converted at 30-Sep-26 | R411, R413, R414, R417, R480, R187 L1012; L848-850 |
| Full-conversion share count | 2,62,38,135 (+4.99%) | A3-05; 12,47,000 / 2,49,91,135 = 4.99% |

EPS (share-adjusted) equals EPS (reported): no corporate action in any comparison period. Diluted count is frozen across H2FY26, FY26 and H1FY27 against note 6 day-weighting; A3 reads it as a treasury-stock count at one fixed average price of about Rs 135.00 [INFERENCE, A3-10].

### 0D. Notes extraction (every numbered note)
| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| SA 1 (R516 L294-299) | Basis, approvals | Results per Reg 33, reviewed by Audit Committee, approved by Board 16-10-2026, limited review by statutory auditors, prepared under AS (Section 133). | Nil | H1FY27 | None. Indian GAAP basis. |
| SA 2 (R517 L301-304) | Ind AS exemption | SME-listed company exempt from Ind AS (MCA notification 16-Feb-2015). | Nil | All | No OCI statement; AS 21 consolidation of a partnership firm. |
| SA 3 (R518 L305-319) | Convertible warrants | 12,47,000 warrants at Rs 169 allotted 27-Aug-2025; Rs 5,26,85,750 (25%) received; the Rs 126.75 per warrant balance is payable only upon exercise, which holders may choose within 18 months of allotment. | 5.27 received; 15.81 receivable only on exercise | FY26 receipt; exercise window closes ~27-Feb-2027 | Potential 4.99% dilution; contingent funding source (A3-01, A3-05). |
| SA 4 (R519 L321-322) | Balance confirmation | Trade payables, loans and advances, other current liabilities are subject to confirmation and reconciliation; adjustments booked in the year of confirmation. | ND (no amount) | Open; undated | Possible FY27 audit adjustment over SA payables Rs 75.61 Cr (A3-07). |
| SA 5 (R520 L323-324) | Segment | Single business segment; no segment disclosure. | Nil | All | No manufacturing vs trading split (A3-11). |
| SA 6 (R521 L325-327) | EPS method | Half-year EPS uses day-weighted shares; half-year EPS may not sum to annual. | Nil | All | Diluted count inconsistency (A3-10). |
| SA 7 (R522 L329) | Regrouping | Prior figures regrouped / reclassified where necessary. | ND | Comparatives | Comparatives may not be like-for-like. The SA receivables gap is now an OCR item, not a reclass (A3-13). |
| SA 8 (R523 L330) | Exceptional | No exceptional or extraordinary items. | Nil | H1FY27 | Exceptional rows dash (R051-R054, M01). |
| CON header (R535 L656) | Header | Notes on consolidated results. | Nil | n.a. | None. |
| CON 1 (R536 L658-666) | Basis | Same as SA 1; limited review for half year ended 30-Sep-2026. | Nil | H1FY27 | None. |
| CON 2 (R537 L667-671) | Ind AS exemption | Same as SA 2. | Nil | All | None. |
| CON 3 (R538 L672-681) | Consolidation | Only subsidiary Danya Electric Company, partnership firm, 90% profit share; MD Vee Rajmohan 7.5% and K.V. Pradeep Kumar 2.5%; line-by-line AS 21; inter-company sales / purchases, balances and "unrealised profit in closing stock, if any" eliminated in full (L679). | MI 3.99 Cr at 30-Sep-26 | All | Related-party structure; S-vs-C gaps (A3-02, A3-03, A3-16); no unrealised-profit elimination is visible in PAT (Step 2, bear counter 2). |
| CON 4 (R539 L683-685) | Subsidiary review status | Danya H1FY27 results unaudited and "[reviewed by the Statutory Auditors / certified by the management]" (bracket left unresolved). | ND | H1FY27 | Governance flag; Danya figures most likely management-certified (A3-04, A3-12). |
| CON 5 (R540 L686-688) | Balance confirmation | Same as SA 4 at group level. | ND | Open | Same as SA 4. |
| CON 6 (R541 L689-691) | EPS method | Same as SA 6. | Nil | All | Same as SA 6. |
| CON 7 (R542 L692-693) | Segment | Group single segment. | Nil | All | Same as SA 5. |
| CON 8 (R543 L694) | Regrouping | Same as SA 7. | ND | Comparatives | Same as SA 7. |
| CON 9 (R544 L696) | Exceptional | No exceptional or extraordinary items. | Nil | H1FY27 | Rows dash (R245-R248, M09). |
| SA CF (i) (R525 L1019) | Sign convention | Brackets are outflows. | Nil | n.a. | None. |
| SA CF (ii) (R526 L1020) | Method | Indirect method, AS-3. | Nil | n.a. | None. |
| CON CF (i) (R546 L1184) | Sign convention | Brackets are outflows. | Nil | n.a. | None. |
| CON CF (ii) (R547 L1185) | Method | Indirect method, AS-3. | Nil | n.a. | None. |
| Certificate 1 (R553 L841-846) | Warrant terms | 12,47,000 warrants, Rs 169, 25%/75% split. | n.a. | n.a. | Restates SA 3. |
| Certificate 2 (R554 L848-850) | Receipt | Only the 25% subscription received; "The balance amount will be payable upon the exercise of the warrants." | 5.27 received | To date | Restates SA 3. |
| BS footers (R515 L957; R534 L1136) | Reclassification | Previous period figures rearranged / reclassified. | ND | Mar-26 BS | Mar-26 SA BS foots only with receivables read as 4,521.09 (A3-13, OCR, routed to A1). |

Note-by-note answers:
- Notes that change YoY or sequential reading: CON 3 and CON 4 (the S-vs-C divergence and an unaudited, possibly uncertified subsidiary); SA 7 / CON 8 and the BS footers (Mar-26 comparatives reclassified; SA receivables held out pending A1). No note flags the H2FY26 column as a balancing figure (A3-18).
- Normalisation required: none for one-offs (no exceptional items, R523, R544). The SA other income carries the 90% Danya profit share (H1FY27 1.10 Cr, R147/R148 L983 per A3 0a); Core PBT strips it.
- Recurring vs one-off flag: no one-off disclosed. The deferred tax charge is recurring capex timing (A3-09).
- Thesis-relevant disclosures: warrant balance contingent on exercise (SA 3), subsidiary governance (CON 3, CON 4), balance confirmation hedge (SA 4).

**Auditor opinion check.** Limited review, not an audit (R509, R510 L115-117; R527, R528). Standalone conclusion unmodified: "nothing has come to our attention ..." (M10, L124-131). Consolidated conclusion unmodified (M11, L476-485), but it rests on "the statement provided by the management related to Parent & Subsidiary" (L476-477), and the subsidiary information "is based solely on such unaudited interim financial results" (R530, L472-474). No Emphasis of Matter, Other Matter, or Going Concern paragraph (A2 section 5; A3 F5); in particular no Other Matter on the comparative H2FY26 column (A3-18). Column audit-status labels match the review scope in all six statements (A3 6d). Reading: CLEAN conclusion with an AMBER reliance flag on the subsidiary (A3-04, A3-12).

### 0E. Business type
Standard operating business, not a lender. Steps 1 and 5 apply. Archetype is UNRESOLVED from the filing: every rupee of material cost sits in "Purchases of Stock in Trade" (R015-R018 L887; R209-R212 L1046), there is no "Cost of materials consumed" line, and a factory is under construction (CWIP Rs 31.91 Cr, R119 L948). Manufacturer vs trader is open (A3-11).

Checkpoint: Notion state verified (ND), units Rs Lakhs to Cr stated, no share-count change, all notes tabulated, auditor conclusion recorded, business type stated.

---

## STEP 1. DATA EXTRACTION TABLES (Rs Cr; standard business)

Column map: Q[N] FY[YY-1] = H1FY26 (half ended 30-Sep-25); Q[N-1] FY[YY] = H2FY26 (half ended 31-Mar-26); Q[N] FY[YY] = H1FY27 (half ended 30-Sep-26); FY[YY-1] = FY26 (audited, R512, R532); FY[YY] = FY27 (not yet reported, ND). H1, H2 and H1FY27 columns are unaudited. **A3-18 caveat:** H1FY27 is the only half covered by the limited review (L90-92, L432-435). H2FY26 is a derived balancing column (FY26 audited less H1FY26), labelled "Unaudited", with no balancing-figure note and no Other Matter; every H2FY26 cell below carries no half-level assurance.

### 1-SA. Standalone
| Line item | H1FY26 | H2FY26 | H1FY27 | FY26 | FY27 | Anchor |
|---|---|---|---|---|---|---|
| Revenue from Operations | 80.66 | 109.42 | 127.14 | 190.08 | ND | R003-R006 L883 |
| Other Income | 0.97 | 1.37 | 1.30 | 2.34 | ND | R007-R010 L884 (FY26 OCR; H1+H2 ties) |
| Total Income | 81.63 | 110.79 | 128.44 | 192.41 | ND | R011-R014 L885 |
| Cost of Materials Consumed | ND (no such line; see Purchases) | ND | ND | ND | ND | A3-11 |
| Purchases of Stock in Trade | 71.64 | 100.47 | 120.65 | 172.11 | ND | R015-R018 L887 |
| Change in Inventories | (9.01) | (14.02) | (24.88) | (23.03) | ND | R019-R022 L888 |
| Other Direct Expenses | 1.18 | 1.27 | 3.13 (0.30 lakh residual, A3 0a) | 2.45 | ND | R023-R026 L889 |
| Employee Benefits Expense | 1.52 | 2.80 | 4.09 | 4.32 | ND | R027-R030 L890 |
| Finance Costs | 0.87 | 1.55 | 2.80 | 2.42 | ND | R031-R034 L891 |
| Depreciation | 0.35 | 1.30 | 1.99 | 1.65 | ND | R035-R038 L892 |
| Other Expenses | 2.81 | 2.77 | 2.78 | 5.58 | ND | R039-R042 L893 |
| Total Expenses | 69.35 | 96.14 | ND (A1 11,086.31 lakh fails footing, A3 0a / A3-15) | 165.49 | ND | R043-R046 L894 |
| Profit Before Tax | 12.27 | 14.65 | 17.88 | 26.92 | ND | R055-R058 L901 (also L896, L899, L976) |
| Current Tax | 2.87 | 2.44 | 3.45 | 5.31 | ND | R059-R062 L903 |
| Deferred Tax | (0.00) credit 0.30 lakh (A3 0a) | 1.17 | 0.77 | 1.17 | ND | R063-R066 L904 |
| Tax Expense (total) | 2.86 | 3.61 | 4.23 | 6.48 | ND | Derived: current + deferred |
| PAT | 9.41 | 11.03 | 13.65 | 20.44 | ND | R067-R070 L194 |
| EPS basic (Rs) | 3.76 | 4.41 | 5.46 | 8.18 | ND | R071-R074 L907 |
| EPS diluted (Rs) | 3.76 | 4.40 | 5.45 | 8.15 | ND | R075-R078 L908 |
| EPS (share-adjusted, basic) | 3.76 | 4.41 | 5.46 | 8.18 | ND | No corporate action (0C) |

Internal ties: H1FY26 + H2FY26 = FY26 for revenue (80.66 + 109.42 = 190.08), PBT (12.27 + 14.65 = 26.92), current tax and PAT. These ties hold by construction, because H2FY26 is the balancing column (A3-18). Reserves rise 13.65 Cr (8,794.70 to 10,159.80 lakh, R093/R094) = H1FY27 PAT 1,365.09 lakh; no dividend (A3 F11).

Derived metrics, standalone (Rs Lakhs inputs, results in Cr or %):
| Derived metric | Formula | H1FY26 | H2FY26 | H1FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 12.53 | 16.12 | 21.37 | 28.65 | ND |
| Operating EBITDA margin | Op EBITDA / Revenue | 15.53% | 14.74% | 16.81% | 15.07% | ND |
| Reported EBITDA | PBT + D + FC | 13.49 | 17.49 | 22.67 | 30.99 | ND |
| Core PBT (ex OI) | PBT - OI | 11.31 | 13.28 | 16.57 | 24.58 | ND |
| Other Income / PBT | OI / PBT | 7.87% | 9.35% | 7.28% | 8.67% | ND |
| Effective tax rate | Tax / PBT | 23.33% | 24.68% | 23.64% | 24.07% | ND |
| PAT margin | PAT / Revenue | 11.66% | 10.08% | 10.74% | 10.75% | ND |
| Gross margin (rev - purchases - change in inv) | (Rev - material cost) / Rev | 22.36% | 20.99% | 24.67% | 21.57% | ND |

Lakh workings: Op EBITDA H1FY27 = 1,787.67 + 199.30 + 280.11 - 130.19 = 2,136.89; H1FY26 = 1,227.24 + 35.08 + 87.08 - 96.56 = 1,252.84; H2FY26 = 1,464.63 + 130.18 + 154.50 - 136.95 = 1,612.36; FY26 = 2,865.20 (= H1 + H2). Material cost H1FY27 = 12,064.96 - 2,487.75 = 9,577.21; gross profit 3,136.58. FY26 gross profit = 19,007.73 - 17,210.72 + 2,302.79 = 4,099.80 (21.57%).
Standalone other income contains the 90% Danya profit share (H1FY27 109.73 lakh, L983 per A3 0a; ETR ex this share 25.18%, A3-09). Standalone Core PBT therefore excludes all Danya profit while standalone revenue includes sales to Danya.

### 1-CON. Consolidated
| Line item | H1FY26 | H2FY26 | H1FY27 | FY26 | FY27 | Anchor |
|---|---|---|---|---|---|---|
| Revenue from Operations | 75.19 | 106.45 | 135.31 | 181.64 | ND | R197-R200 L1042 |
| Other Income | 0.16 | 0.30 | 0.26 | 0.46 | ND | R201-R204 L1043 |
| Total Income | 75.36 | 106.75 | 135.57 | 182.10 | ND | R205-R208 L1044 |
| Cost of Materials Consumed | ND (no such line) | ND | ND | ND | ND | A3-11 |
| Purchases of Stock in Trade | 69.00 | 96.95 | 126.54 | 165.95 | ND | R209-R212 L1046 |
| Change in Inventories | (13.74) | (16.82) | (25.36) | (30.56) | ND | R213-R216 L1047 |
| Other Direct Expenses | 1.27 | 1.37 | 3.24 | 2.64 | ND | R217-R220 L1048 |
| Employee Benefits Expense | 2.18 | 2.36 | 4.20 | 4.54 | ND | R221-R224 L1049 |
| Finance Costs | 1.01 | 2.02 | 2.92 | 3.03 | ND | R225-R228 L1050 |
| Depreciation | 0.40 | 1.35 | 2.04 | 1.74 | ND | R229-R232 L1051 |
| Other Expenses | 2.37 | 3.87 | 3.33 | 6.24 | ND | R233-R236 L1052 |
| Total Expenses | 62.49 | 91.10 | 116.91 | 153.59 | ND | R237-R240 L1053 (H1FY27 foots) |
| Profit Before Tax | 12.87 | 15.65 | 18.66 | 28.52 | ND | R249-R252 L1064; R241-R244 L1055 |
| Current Tax | 3.37 | 3.29 | 4.11 | 6.66 | ND | R253-R256 L1067 |
| Deferred Tax | (0.00) credit 0.20 lakh | 1.18 | 0.77 | 1.17 | ND | R257-R260 L1069 |
| Tax adj. earlier years | nil | 0.00 (0.37 lakh) | nil | 0.00 (0.37 lakh) | ND | R261-R264 L1071, A3 0a / A3-08 |
| PAT (group) | 9.50 | 11.17 | 13.77 | 20.68 | ND | R265-R268 L1072 |
| Minority interest | 0.09 | 0.14 | 0.12 | 0.24 | ND | R269-R272 L1073 |
| PAT to owners | 9.41 | 11.03 | 13.65 | 20.44 | ND | R273-R276 L1074 |
| EPS basic (Rs) | 3.76 | 4.41 | 5.46 | 8.18 | ND | R277-R280 L1080 |
| EPS diluted (Rs) | 3.76 | 4.40 | 5.45 | 8.15 | ND | R281-R284 L1082 |
| EPS (share-adjusted, basic) | 3.76 | 4.41 | 5.46 | 8.18 | ND | 0C |

Derived metrics, consolidated:
| Derived metric | Formula | H1FY26 | H2FY26 | H1FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|
| Operating EBITDA | PBT + D + FC - OI | 14.11 | 18.71 | 23.35 | 32.82 | ND |
| Operating EBITDA margin | Op EBITDA / Revenue | 18.77% | 17.58% | 17.26% | 18.07% | ND |
| Reported EBITDA | PBT + D + FC | 14.27 | 19.01 | 23.62 | 33.29 | ND |
| Core PBT (ex OI) | PBT - OI | 12.71 | 15.35 | 18.40 | 28.06 | ND |
| Other Income / PBT | OI / PBT | 1.26% | 1.91% | 1.42% | 1.62% | ND |
| Effective tax rate | Tax / PBT | 26.17% | 28.59% | 26.19% | 27.50% | ND |
| PAT margin (group PAT) | PAT / Revenue | 12.64% | 10.50% | 10.18% | 11.38% | ND |
| Gross margin | (Rev - material cost) / Rev | 26.51% | 24.72% | 25.22% | 25.46% | ND |

Lakh workings: CON Op EBITDA H1FY27 = 1,866.01 + 204.10 + 291.79 - 26.45 = 2,335.45; H1FY26 = 1,287.07 + 39.60 + 100.80 - 16.16 = 1,411.31; H2FY26 = 1,871.11; FY26 = 3,282.42 (= H1 + H2). Material cost H1FY27 = 12,653.73 - 2,535.78 = 10,117.95; gross profit 3,412.96; H1FY26 gross profit 1,993.29.

**Interpretive anchor.** The consolidated statement is the economic view of the group. Standalone revenue includes sales to Danya and standalone other income includes Danya's profit share; both are eliminated or replaced on consolidation. Under conservative bias this review anchors margin reading to CONSOLIDATED and reports standalone alongside.

### 1-SVC. Standalone vs consolidated gap (first-class metric; A3 F2, section 3b)
| Metric (CON minus SA) | H1FY26 | H2FY26 (balancing column, A3-18) | FY26 (audited) | H1FY27 | Anchor |
|---|---|---|---|---|---|
| Revenue gap, Rs Cr | (5.47) | (2.97) | (8.44) | +8.17 | R003-R006 L883 vs R197-R200 L1042; A3-02 |
| Purchases of stock in trade gap, Rs Cr | (2.63) | (3.52) | (6.16) | +5.89 | R015-R018 L887 vs R209-R212 L1046; lakh: -263.45, -352.19, -615.62, +588.77 |
| Inventory build gap (CON minus SA change in inventories), Rs Cr | 4.73 | 2.80 | 7.53 | 0.48 | R019-R022 L888 vs R213-R216 L1047; lakh: 472.94, 279.81, 752.75, 48.03 |
| Implied Danya stock at period end (CON minus SA inventories), Rs Cr | ND (30-Sep-25 BS not filed) | 16.53 (31-Mar-26) | 16.53 (31-Mar-26) | 17.02 (30-Sep-26) | L953 vs L1131; 6,209.72 - 4,556.25 = 1,653.47; 8,745.50 - 7,044.00 = 1,701.50 |
| Other creditors (non-MSE trade payables) gap at period end, Rs Cr | ND | (4.48) (31-Mar-26) | (4.48) (31-Mar-26) | (0.81) (30-Sep-26) | SA R108 L939 (3,074.78, OCR_UNCERTAIN, tied A3 0a) and L939 4,457.00 vs CON L1118 2,627.00 and 4,376.18 |
| Operating EBITDA gap, Rs Cr | +1.58 | +2.59 | +4.17 | +1.99 | Derived tables above |
| Op EBITDA gap, % of SA PAT | 16.8% | 23.5% | 20.4% | 14.5% | A3 3b; 158.47/940.87, 258.75/1,103.18, 417.22/2,044.06, 198.56/1,365.09 |
| Op EBITDA margin gap, pp (CON - SA) | +3.24 | +2.84 | +3.00 | +0.45 | 18.77-15.53; 17.58-14.74; 18.07-15.07; 17.26-16.81 |
| PAT to owners gap, Rs Cr | 0.00 | 0.00 | 0.00 | +0.00 (0.01 lakh) | R067-R070 L194 vs R273-R276 L1074 |
| PAT to owners gap, % of SA PAT | 0.00% | 0.00% | 0.00% | 0.00% | Same |
| Group PAT (incl. MI) gap, % of SA PAT | 1.00% | 1.28% | 1.15% | 0.89% | MI R269-R272 / SA PAT |
| Derived Danya PAT (MI x 10), Rs Cr | 0.94 | 1.41 | 2.35 | 1.22 | A3 3b |
| Derived Danya PAT, % of CON PAT | 9.9% | 12.6% | 11.4% | 8.85% | A3-04 |
| Implied Danya employee cost (CON - SA), Rs Cr | 0.66 | (0.44) | 0.22 | 0.11 | A3-03 |
| Receivables build, CON minus SA, Rs Cr | ND | ND | ND | at least 8.65 (bound; see Step 2) | CON R359 L1164 vs SA R153 L988; A3-04, A3-13 |

Reading: owners' PAT ties to within 0.01 lakh because standalone books the Danya share. The gap moved inside the P&L: the revenue gap flipped sign (swing Rs 13.64 Cr YoY), the EBITDA margin gap shrank from 3.24 pp to 0.45 pp YoY, and two cost lines consolidate below standalone in some periods (other expenses H1FY26 by Rs 0.43 Cr; employee cost H2FY26 by Rs 0.44 Cr, an unassured balancing cell; A3-03, A3-18).

**Goods moved both ways between the parent and Danya in FY26.** On a line-by-line combination with intercompany trade removed, CON purchases = SA purchases + Danya's external purchases - Danya's sales to the parent, and CON revenue = SA revenue + Danya's external revenue - the parent's sales to Danya.
- FY26 CON purchases sit Rs 6.16 Cr below SA (16,595.10 L1046 vs 17,210.72 L887). Danya's external purchases cannot be negative, so the parent bought at least Rs 6.16 Cr of goods from Danya.
- FY26 CON revenue sits Rs 8.44 Cr below SA (18,164.04 L1042 vs 19,007.73 L883). By the same logic, the parent sold at least Rs 8.44 Cr of goods into Danya.
- Both figures are floors on audited FY26 numbers. Each true figure equals the floor plus Danya's external purchases or external revenue, which the filing does not give.
- At 31-Mar-26, CON other creditors sit Rs 4.48 Cr below SA (2,627.00 L1118 vs 3,074.78 R108 L939). A line-by-line combination only adds Danya's creditors to the parent's. A lower consolidated figure therefore means one of two things: the parent owed Danya at least Rs 4.48 Cr, eliminated on consolidation, or balances were regrouped between lines (BS footer L1136). The gap narrows to Rs 0.81 Cr at 30-Sep-26 (4,376.18 L1118 vs 4,457.00 L939).
- In H1FY27, CON purchases and CON revenue both exceed SA (+5.89 Cr, +8.17 Cr). The floors do not bind, so two-way flow in the half can be neither shown nor excluded.
- [INFERENCE] When a parent both sells to and buys from a firm in which its MD is a partner, the margin split between the two books is a transfer-pricing choice. That mechanism can move SA margin up 128 bps while CON margin falls 151 bps (Step 2). It also creates the unrealised-profit question in Step 2, bear counter 2.

Two readings of the H1FY27 revenue flip: (1) Danya's external sales grew; (2) SA sales to Danya fell or shifted. Separating observation: Danya standalone revenue and intercompany sales in each direction by period, plus the intercompany balance at each date. The filing discloses none of them (Q7, Q20). The H1FY27 revenue booked outside the parent came with a larger receivables build than the parent's (Step 2, answer 3). A3-18 caveat: the H2FY26 column is a derived balancing figure with no half-level assurance. The FY26 floors rest on audited figures and do not depend on it.

Checkpoint: extraction tables complete; every cell a number with row anchor or ND.

---

## STEP 2. YoY COMPARISON (H1FY27 vs H1FY26)

### 2-CON. Consolidated (anchor view)
| Metric | H1FY26 | H1FY27 | YoY % change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 75.19 | 135.31 | +79.95% | Strong growth |
| Operating EBITDA | 14.11 | 23.35 | +65.48% | Grew, slower than revenue |
| Op EBITDA margin (pp) | 18.77% | 17.26% | -151 bps | Contraction |
| Depreciation | 0.40 | 2.04 | +415.4% | Capex absorption step |
| Finance Costs | 1.01 | 2.92 | +189.5% | Debt-funded growth |
| EBIT (operating) = Op EBITDA - D | 13.72 | 21.31 | +55.38% | Grew below revenue |
| Other Income | 0.16 | 0.26 | +63.68% | Immaterial (1.42% of PBT) |
| **Core Operating PBT (PBT - OI)** | **12.71** | **18.40** | **+44.74%** | **Real growth, below revenue** |
| Reported PBT | 12.87 | 18.66 | +44.98% | Matches core |
| PAT (group) | 9.50 | 13.77 | +44.94% | Matches core |
| PAT to owners | 9.41 | 13.65 | +45.09% | Matches core |
| EPS (share-adjusted) | 3.76 | 5.46 | +45.21% | No dilution yet |

### 2-SA. Standalone
| Metric | H1FY26 | H1FY27 | YoY % change | Verdict |
|---|---|---|---|---|
| Revenue from Operations | 80.66 | 127.14 | +57.62% | Strong growth |
| Operating EBITDA | 12.53 | 21.37 | +70.56% | Grew faster than revenue |
| Op EBITDA margin (pp) | 15.53% | 16.81% | +128 bps | Expansion (contradicts CON) |
| Depreciation | 0.35 | 1.99 | +468.1% | Capex absorption step |
| Finance Costs | 0.87 | 2.80 | +221.7% | Debt-funded growth |
| EBIT (operating) | 12.18 | 19.38 | +59.11% | In line with revenue |
| Other Income | 0.97 | 1.30 | +34.83% | Mostly Danya share (1.10 Cr H1FY27) |
| **Core Operating PBT (PBT - OI)** | **11.31** | **16.57** | **+46.59%** | **Real growth, below revenue** |
| Reported PBT | 12.27 | 17.88 | +45.67% | Matches core |
| PAT | 9.41 | 13.65 | +45.09% | Matches core |
| EPS (share-adjusted) | 3.76 | 5.46 | +45.21% | No dilution yet |

Lakh workings for YoY: CON revenue +6,011.47 / 7,519.44; CON Op EBITDA +924.14 / 1,411.31; CON core PBT +568.65 / 1,270.91; SA revenue +4,647.69 / 8,066.10; SA Op EBITDA +884.05 / 1,252.84; SA core PBT +526.80 / 1,130.68; SA PAT +424.22 / 940.87.

Six diagnostic answers:
1. **Revenue YoY.** Yes. CON +79.95% (Rs 75.19 Cr to Rs 135.31 Cr); SA +57.62% (Rs 80.66 Cr to Rs 127.14 Cr). Company guidance: ND (none in filing). Base case: ND 'not passed'.
2. **Op EBITDA margin YoY.** CON contracted: H1FY27 17.26% vs H1FY26 18.77% = -151 bps. SA expanded: 16.81% vs 15.53% = +128 bps. The directions disagree; the group view (CON) shows contraction. CON gross margin fell 129 bps (26.51% to 25.22%) while SA gross margin rose 231 bps (22.36% to 24.67%). This pattern points to intercompany pricing or Danya mix, not to a group-level margin gain. FY26 audited figures show goods moving in both directions between the two books (1-SVC), which is the channel for such a shift.
3. **Core operating PBT YoY.** Grew: CON +44.74% (Rs 12.71 Cr to Rs 18.40 Cr); SA +46.59%. Reported PAT growth (+45%) is real at the PBT level; it is not driven by other income.
   **Bear counter 1 (collection of the revenue booked outside the parent).** CON revenue exceeds SA revenue by Rs 8.17 Cr in H1FY27 (R003 vs R197). In the same half the CON receivables build was Rs 15.84 Cr (R359 L1164, ties to BS R335/R336), against an SA build of Rs 7.19 Cr (R153 L988 as extracted). The difference is Rs 8.65 Cr. This bound holds under every candidate SA reading: Rs 8.65 Cr with R153 as extracted (718.82), Rs 8.68 Cr on the A3 arithmetic reading (715.82), and Rs 11.68 Cr with the BS change implied by R130 as extracted (415.82) (A3-13). The CON-minus-SA build equals the change in Danya's receivables less the change in what Danya owes the parent (eliminated on consolidation, CON note 3 L677-678). If intercompany balances held steady, Danya's receivables rose by at least Rs 8.65 Cr while the revenue it added beyond the parent was Rs 8.17 Cr: that revenue was not collected at 30-Sep-26. [INFERENCE] Receivables carry GST and revenue does not; at 18% GST, Rs 8.65 Cr of receivables is about Rs 7.33 Cr of net revenue, still about 90% of the Rs 8.17 Cr. Reading 2: the parent's receivable from Danya fell in the half (Danya paid the parent down), which would make Danya's external build smaller than Rs 8.65 Cr. Separating observation: Danya receivables and the intercompany balance at both dates (not in the filing; Q11). Danya's numbers are unaudited (A3-04, A3-12).
   **Bear counter 2 (unrealised profit in Danya's stock; A4 loop 2).**
   - CON note 3 says inter-company sales and "unrealised profit in closing stock, if any" are eliminated in full (L679).
   - SA PAT already contains 90% of Danya's own reported PAT (inside other income). Any elimination of unrealised profit on stock that Danya bought from the parent would therefore push CON owners' PAT below SA PAT.
   - Owners' PAT equals SA PAT in all four periods: 1,365.09 vs 1,365.10 lakh (H1FY27, a 0.01 lakh rounding), 1,103.18, 940.87 and 2,044.06 (SA L194 vs CON L1074). No unrealised profit was eliminated in any period [FILED arithmetic].
   - Danya holds material stock. Implied Danya stock (CON minus SA inventories) is Rs 16.53 Cr at 31-Mar-26 and Rs 17.02 Cr at 30-Sep-26, 19.5% of group stock of Rs 87.46 Cr (1,701.50 / 8,745.50; L953 vs L1131). Danya's stock rose Rs 7.53 Cr in FY26 (CON change in inventories 3,055.54 vs SA 2,302.79, L1047 vs L888).
   - Danya holds almost no cash: 2.90 lakh at 30-Sep-26 (CON 24.81 L1133 less SA 21.91 L955).
   - The parent sold at least Rs 8.44 Cr of goods into Danya in FY26 (1-SVC).
   - [INFERENCE] Upper bound on the FY26 effect. Suppose the whole FY26 rise in Danya's stock was goods bought from the parent at the parent's FY26 gross margin of 21.57%. The margin then left in FY26 CON profit is at most 752.75 x 21.57% = 162.4 lakh, about Rs 1.62 Cr pre-tax, or 5.7% of FY26 CON PBT of 2,851.66 lakh. The bound uses the parent's average gross margin as a proxy for the transfer margin. A higher transfer margin would raise it.
   - H1FY27 growth is not inflated by this item. Danya's stock rose only Rs 0.48 Cr in the half (48.03 lakh; L1047 vs L888, equal to the BS change 1,701.50 - 1,653.47). On the same method the H1FY27 effect is at most 48.03 x 24.67% = 11.85 lakh (Rs 0.12 Cr). The H1FY26 base had a Rs 4.73 Cr Danya stock build (472.94 lakh), which on the same bound could carry up to 105.75 lakh (Rs 1.06 Cr; 472.94 x 22.36%). If anything, the YoY comparison is understated, not overstated [INFERENCE].
   - Two readings. (1) Danya's stock was bought from outside suppliers, or the intercompany goods carried no margin, so a nil elimination is correct. (2) Parent-sourced stock sits in Danya at the parent's selling price, and FY26 group profit and group equity include margin not yet earned outside the group. Separating observation: the parent-sourced share of Danya's closing stock and the transfer margin at 31-Mar-26 and 30-Sep-26 (Q21; FY27 audited accounts).
4. **Gap between core PBT growth and PAT growth.** Small. CON: core PBT +5.69 Cr, other income +0.10 Cr, tax -1.52 Cr (ETR 26.17% to 26.19%, +2 bps), exceptional nil, MI -0.03 Cr. PAT growth 44.94% vs core PBT growth 44.74%.
5. **D&A and finance cost vs revenue.** Yes, both outran revenue. CON D&A +415.4% and finance cost +189.5% against revenue +79.95%. Combined D&A + finance cost rose from 1.87% of CON revenue (1.40 Cr / 75.19 Cr) to 3.67% (4.96 Cr / 135.31 Cr). This is the capex absorption pattern: FY26 capex Rs 57.48 Cr (R378) plus CWIP Rs 31.91 Cr still not earning. EBIT growth (+55.38%) trails revenue growth (+79.95%).
6. **Other income concentration.** Not a factor at CON (1.42% of PBT). At SA, other income is 7.28% of PBT and is mostly the Danya profit share; it is operating income of the group, so stripping it understates SA economics but is the protocol-correct core view.

Checkpoint: YoY tables and six answers complete.

---

## STEP 3. SEQUENTIAL TRAJECTORY (half-year cadence; only three halves are filed)

| Half | CON revenue (Rs Cr) | CON Op EBITDA margin | CON Core PBT (Rs Cr) | SA revenue (Rs Cr) | SA Op EBITDA margin | SA Core PBT (Rs Cr) | One-offs flagged | HoH run-rate (CON revenue) |
|---|---|---|---|---|---|---|---|---|
| H1FY26 | 75.19 | 18.77% | 12.71 | 80.66 | 15.53% | 11.31 | None (R523, R544) | Base |
| H2FY26 (balancing column, A3-18) | 106.45 | 17.58% | 15.35 | 109.42 | 14.74% | 13.28 | CON prior-year tax 0.37 lakh (immaterial) | +41.56% |
| H1FY27 | 135.31 | 17.26% | 18.40 | 127.14 | 16.81% | 16.57 | None | +27.12% |
| H1FY25 and earlier history | ND | ND | ND | ND | ND | ND | ND (no older halves in filing) | ND |

HoH workings: CON revenue 10,644.60 / 7,519.44 = +41.56%; 13,530.91 / 10,644.60 = +27.12%. SA 10,941.63 / 8,066.10 = +35.65%; 12,713.79 / 10,941.63 = +16.20%. CON core PBT H1FY27 vs H2FY26 +19.87% (304.93 / 1,534.63); SA +24.84%.

A3-18 weighting: both HoH steps run through H2FY26, a derived column with no half-level assurance. They are weighted below the YoY comparison of H1FY27 with H1FY26 (Step 2) and below the audited FY26 total.

Diagnostics:
- **Run-rate trajectory:** Stepping up on revenue and core PBT for three consecutive halves. CON Op EBITDA margin is dipping in every half (18.77% to 17.58% to 17.26%). Growth is bought with margin and working capital. The YoY margin fall (-151 bps, two filed halves) carries the read; the middle step is the unassured column.
- **One-off distortion:** None disclosed (R523, R544). CON prior-year tax 0.37 lakh is immaterial (A3-08).
- **Latest half vs prior run-rate (capex commissioning test):** D&A stepped from 0.35 Cr (H1FY26) to 1.30 Cr (H2FY26) to 1.99 Cr (H1FY27), so assets capitalised from FY26 capex (Rs 57.46 Cr SA, R178). H1FY27 revenue (CON 135.31 Cr) is above both pre-commissioning halves, so the run-rate did lift. The filing does not show whether the lift came from the new assets or from traded volume (A3-11). Plant utilisation: ND.
- **Implied next-half base:** To hold trajectory, H2FY27 CON revenue must be at or above H1FY27 (Rs 135.31 Cr) and above H2FY26 (Rs 106.45 Cr) YoY. Seasonality: one year only (H2FY26 above H1FY26); a seasonal pattern cannot be confirmed from one year. ND.

Checkpoint: trajectory table and diagnostics complete.

---

## STEP 4. OPERATIONAL DECOMPOSITION (PAT bridge, YoY)

### 4-CON. Consolidated group PAT, H1FY26 to H1FY27
| Component | YoY change (Rs Cr) | % of H1FY26 group PAT | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (dRev x prior GM 26.51%) | +15.94 | +167.70% | Recurring |
| Gross margin change contribution (H1FY27 Rev x -1.29 pp) | -1.74 | -18.30% | Recurring (watch) |
| Other operating costs (other direct + employee + other exp) | -4.96 | -52.15% | Recurring |
| D&A change | -1.65 | -17.31% | Recurring (post-capex) |
| Finance cost change | -1.91 | -20.10% | Recurring (post-debt) |
| Other income change | +0.10 | +1.08% | Non-recurring typically |
| Tax on higher PBT at prior ETR 26.17% | -1.52 | -15.94% | Mixed |
| Effective tax rate change (+2 bps) | -0.00 (0.41 lakh) | -0.04% | Mixed |
| Exceptional items | 0.00 | 0.00% | Non-recurring (none, R245-R248) |
| **Reported group PAT YoY change** | **+4.27** | **+44.94%** | |
| Minority interest change | -0.03 | | |
| **PAT to owners YoY change** | **+4.24** | **+45.09% of 9.41** | |

Lakh workings: dRev 6,011.47 x 0.265085 = 1,593.55; 13,530.91 x (0.252234 - 0.265085) = -173.88; opex 1,077.51 - 581.98 = 495.53; D&A 164.50; FC 190.99; OI +10.29; PBT change 578.94; tax 488.72 - 336.81 = 151.91 (151.50 rate-constant + 0.41 rate change); PAT +427.03.

### 4-SA. Standalone PAT, H1FY26 to H1FY27
| Component | YoY change (Rs Cr) | % of H1FY26 PAT | Recurring? |
|---|---|---|---|
| Revenue contribution to gross profit (dRev x prior GM 22.36%) | +10.39 | +110.45% | Recurring |
| Gross margin change contribution (H1FY27 Rev x +2.31 pp) | +2.94 | +31.23% | Recurring only if intercompany pricing is stable (A3-02; two-way flows, 1-SVC) |
| Other operating costs (balancing to PBT-anchored EBITDA) | -4.49 | -47.72% | Recurring |
| D&A change | -1.64 | -17.45% | Recurring (post-capex) |
| Finance cost change | -1.93 | -20.52% | Recurring (post-debt) |
| Other income change (mostly Danya share) | +0.34 | +3.57% | Recurring to the extent Danya earns |
| Tax on higher PBT at prior ETR 23.33% | -1.31 | -13.90% | Mixed |
| Effective tax rate change (+30 bps) | -0.05 | -0.58% | Mixed |
| Exceptional items | 0.00 | 0.00% | Non-recurring (none, R051-R054) |
| **Reported PAT YoY change** | **+4.24** | **+45.09%** | |

Lakh workings: 4,647.69 x 0.223597 = 1,039.21; 12,713.79 x 0.023110 = 293.81; opex balancing = 884.05 - 1,333.02 = -448.97 (line-item sum gives -449.28; the 0.31 residual is the A3-15 / R023 item); D&A -164.22; FC -193.03; OI +33.63; PBT +560.43; tax -136.21 (130.77 + 5.44); PAT +424.22.

Mandatory answers:
- **Recurring vs non-recurring share:** At CON, other income explains +0.10 Cr of a +5.79 Cr PBT change (1.8%); about 98% of the PBT change is recurring operations. At SA, other income explains 6.0% of the PBT change (33.63 / 560.43 lakh). No unrealised-profit release or build distorts the H1FY27 bridge by more than Rs 0.12 Cr (Step 2, bear counter 2).
- **If other income reverts to prior level:** CON PAT changes by about -0.08 Cr (10.29 lakh x (1 - 26.19%)); immaterial. SA PAT would fall by 0.26 Cr (33.63 x (1 - 23.64%)), but SA other income is the Danya share and should not revert unless Danya earns less.
- **D&A and finance cost at steady state?** Still ramping. CWIP rose Rs 3.93 Cr in the half to Rs 31.91 Cr (R119/R120) and IAUD to Rs 1.74 Cr (R121). When CWIP capitalises, D&A steps up again; gross debt rose Rs 9.29 Cr SA in the half, so finance cost steps up too. Steady-state level: ND (commissioning date and debt plan not disclosed).
- **Tax adjustments:** Deferred tax is a persistent CHARGE (SA 0.77 Cr H1FY27; DTL 1.35 Cr to 2.12 Cr, R099/R100). It reduces reported PAT, not inflates it; it defers cash tax by 432 bps of PBT in H1FY27 (A3-09; the 801 bps H2FY26 reading rests on the unassured balancing column, A3-18). SA ETR 23.64% equals 25.18% ex the exempt Danya share. No DTA recognition, no tax credit. Tax is presented gross (current tax in ST provisions, advance tax in other current assets; A3 table 3d); Danya took a net refund of 0.08 Cr in the half.

Checkpoint: bridges and answers complete.

---

## STEP 5. CASH QUALITY AND BALANCE SHEET

H1 cash flow and balance sheet are filed (Reg 33 half-yearly). Prior period for flows = FY26 (only comparative in the CF statements); prior period for balances = 31-Mar-26. Working-capital ratios use receivables, inventory and trade payables only; ST provisions (gross current tax) and advance tax (inside other current assets) are both excluded (A3 table 3d).

### 5-CON. Consolidated (anchor view; CF ties internally)
| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | FY26 25.90 (R376 L750) | H1FY27 (5.74) (R375 L750) | Negative in the half | RED |
| CFO / PAT | FY26 1.25x (2,590.47/2,067.56) | H1FY27 -0.42x (-573.76/1,377.29) | Below any cash band | RED |
| Capex (PPE + CWIP) | FY26 57.48 (R378 L752) | H1FY27 8.68 (R377 L752) | Capex slowed | Neutral |
| FCF (CFO - capex) | FY26 (31.58) | H1FY27 (14.42) | Negative both periods | RED |
| Working capital change (CF) | FY26 +2.82 inflow (derived, L1164-L1169) | H1FY27 (26.75) outflow | Swing -29.57 | RED |
| Receivable days (end balance / half revenue x days) | 31-Mar-26 80.10 (4,684.51/10,644.60 x 182) | 30-Sep-26 84.77 (6,268.15/13,530.91 x 183) | +4.68 days | AMBER |
| Inventory days (on material cost) | 31-Mar-26 141.04 (6,209.72/8,013.40 x 182) | 30-Sep-26 158.18 (8,745.50/10,117.95 x 183) | +17.14 days | RED |
| Payable days (on purchases) | 31-Mar-26 116.77 (6,220.03/9,695.02 x 182) | 30-Sep-26 122.34 (8,459.28/12,653.73 x 183) | +5.57 days | AMBER (supplier funding up; see Step 7 bear counter) |
| Cash conversion cycle | 104.36 days | 120.61 days | +16.25 days | RED |
| Other current liabilities | 18.44 (R318 L1119) | 14.42 (R317 L1119) | -4.03 (-21.8%) | AMBER (A3-17) |
| PPE | 90.30 (R324) | 92.64 (R323) | +2.34 | Neutral |
| CWIP | 27.98 (R328) | 31.91 (R327) | +3.93 (+14.0%) | Not yet earning |
| Gross debt (LT + ST borrowings) | 49.97 (R306, R312) | 57.45 (R305, R311) | +7.47 | AMBER |
| Trade payables (MSE + others) | 62.20 (R314, R316) | 84.59 (R313, R315 L1116-L1118) | +22.39 | AMBER (147.3% of gross debt) |
| Cash and equivalents | 9.75 (R338) | 0.25 (R337) | -9.50 | RED |
| Net Debt | 40.23 | 57.20 | +16.97 (+42.2%) | RED |
| Promoter pledge | ND (not in filing) | ND | ND | UNKNOWN |

CON balance ties: receivables 4,684.51 to 6,268.15 lakh (+1,583.64) = CF L1164; inventories +2,535.78 = L1165; payables 6,220.03 to 8,459.28 (+2,239.25) = L1168; other current liabilities 1,844.40 to 1,441.77 (-402.63) = CF R369 (A3 6a); CF arithmetic 2,311.34 - 2,675.10 = (363.76) cash generated, less taxes 210.00 = (573.76) CFO (R373, R375). The CON receivable-days prior point uses H2FY26 revenue, the unassured balancing column (A3-18).

### 5-SA. Standalone
| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO | FY26 27.73 (R170 L999) | H1FY27 (5.23) (R169 L999, OCR; A3 recomputes (5.23) at 522.96 lakh) | Negative in the half | RED |
| CFO / PAT | FY26 1.36x (2,773.36/2,044.06); likely carries about 2.12 Cr non-cash Danya profit and a 14.56 Cr OCL build (A3-14, A3-17) | H1FY27 -0.38x (-522.90/1,365.09) | Below any band | RED |
| Capex (PPE + CWIP) | FY26 57.46 (R178 L1006) | H1FY27 8.56 (R171 L1003) | Line switched between periods (A3-14) | Neutral |
| FCF (CFO - capex) | FY26 (29.73) | H1FY27 (13.79) | Negative both periods | RED |
| Investment into Danya | FY26 +0.09 inflow (R180) | H1FY27 (2.75) (R179 L1007) | Parent funded subsidiary | AMBER (A3-16; Step 5-D) |
| Working capital change (CF) | FY26 +4.71 inflow (derived L987-L993) | H1FY27 (24.16) on the A3-13 reading; (24.19) with R153 as extracted | 0.03 Cr difference is the A3-13 OCR item | RED |
| Receivable days | 31-Mar-26 ND (R130 not used, A3-13) | 30-Sep-26 75.38 (5,236.91/12,713.79 x 183) | ND | UNKNOWN |
| Inventory days | 31-Mar-26 95.92 (4,556.25/8,645.40 x 182) | 30-Sep-26 134.60 (7,044.00/9,577.21 x 183) | +38.68 days | RED |
| Payable days | 31-Mar-26 107.86 (5,954.07/10,047.21 x 182) | 30-Sep-26 114.68 (7,560.72/12,064.96 x 183) | +6.82 days | AMBER |
| Cash conversion cycle | ND (receivables) | 95.30 days | ND | UNKNOWN |
| Other current liabilities | 18.29 (R110 L940) | 14.29 (R109 L940) | -4.00 (-21.9%) | AMBER (A3-17) |
| PPE | 86.65 (R116) | 88.92 (R115) | +2.27 | Neutral |
| CWIP | 27.98 (R120) | 31.91 (R119) | +3.93 | Not yet earning |
| Gross debt | 45.73 (R098, R104) | 55.02 (R097, R103) | +9.29 | AMBER |
| Trade payables (MSE + others) | 59.54 (R106 at 2,879.29, R108) | 75.61 (R105 L237, R107 L939) | +16.07 | AMBER (137.4% of gross debt) |
| Cash | 9.74 (R132) | 0.22 (R131) | -9.52 | RED |
| Net Debt | 35.99 | 54.80 | +18.81 (+52.3%) | RED |
| Net worth ex warrants (capital + reserves) | 112.94 | 126.59 | +13.65 = PAT | Neutral |
| Net debt / net worth (ex warrants) | 0.32x | 0.43x | +0.11x | AMBER |
| Promoter pledge | ND | ND | ND | UNKNOWN |

SA notes: inventories 4,556.25 to 7,044.00 lakh (+54.6%, R127/R128) ties to CF (2,487.75) L987. Payables total 5,954.07 to 7,560.72 (+1,606.65) ties to CF L991 with 2,879.29 (A3 0a). Other current assets rose 739.73 lakh on the BS vs 521.97 in the CF; the 217.76 difference equals income taxes paid (R167 L998), so advance tax sits in other current assets (A3 table 3d). SA receivables: the R130-based BS change (415.82) and the CF change (R153, 718.82) disagree by 303.00. A3-13 now resolves both as the scan's 5-read-as-8 defect (Mar-26 4,521.09; CF 715.82): that reading balances the Mar-26 SA BS (24,873.69 vs 24,873.68) and the CF subtotal (305.21 vs 305.20). A3-13 is NEUTRAL-FACT and routed to A1; this review uses neither value as a line metric until A1 confirms. SA E&L 30-Sep-26 foots at 28,802.45 lakh (R113).

Mandatory answers:
- **CFO/PAT vs the Pillar 2 band:** Assumed band ND 'not passed'. H1FY27 CFO/PAT is negative at both levels (CON -0.42x, SA -0.38x), below the lowest band (0.65x). FY26 read 1.25x CON / 1.36x SA, but FY26 rested on payables +30.67 Cr and other current liabilities +14.56 Cr (CON L1168-L1169), and FY26 SA CFO likely carries about Rs 2.12 Cr of non-cash Danya profit (A3-14). FY26 CON PAT may also carry up to about Rs 1.62 Cr pre-tax of unrealised margin on Danya stock, which by nature has no cash behind it (Step 2, bear counter 2; INFERENCE). Two readings a year are available; this is reading one of FY27. Flag for Pillar 2 (deferred, OR-30).
- **Other current liabilities (A3-17).** SA OCL fell Rs 4.00 Cr (21.9%) in H1FY27 after a Rs 14.56 Cr build in FY26 that supplied 52.5% of FY26 SA CFO (R161/R162 L992). CON fell Rs 4.03 Cr. Reading 1: customer advances unwound into revenue faster than new advances arrived, so order intake lags execution and FY26 CFO was partly borrowed from later halves. Reading 2: non-trade items paid down or re-presented (capital creditors, statutory dues, or current maturities moved into short-term borrowings, which rose Rs 4.19 Cr SA in the same half). Separating observation: OCL breakup at both dates (Q17).
- **WC drag structural or growth-induced:** The test is days, not rupees. CON inventory days rose 17.14 and the CCC rose 16.25 days in one half. Growth-induced WC would hold days flat while rupees rise; here days rose. No rating-agency commentary is in the corpus. One half cannot separate the readings. **Classification: INDETERMINATE-WITH-DIRECTION (direction: deteriorating).** Missing evidence: order book and inventory composition (finished goods vs raw material), OCL breakup, FY27 full-year CFO, rating rationale.
- **CWIP capitalisation:** CWIP did not capitalise in the half; it rose Rs 3.93 Cr to Rs 31.91 Cr. PPE rose Rs 2.27 Cr after Rs 1.99 Cr D&A. Projected commissioning: ND (no thesis, no disclosure).
- **Net debt vs projection:** Projection ND. Net debt rose 42.2% CON / 52.3% SA in six months. Cash is near zero (SA Rs 0.22 Cr). The unexercised warrant balance of Rs 15.81 Cr is the nearest equity source, but it arrives only if holders choose to exercise (L848-850; A3-01).

**Cash conversion verdict cap.** INDETERMINATE-WITH-DIRECTION caps the protocol verdict at PROCEED WITH CAVEATS or below. Named missing evidence: order book, inventory composition, OCL breakup, undrawn bank limits, FY27 CFO.

### 5-D. Acquisition probe applied to the parent's capital in Danya (no acquisition in the filing)
The filing reports no acquisition, business purchase or new investee: the entity list carries one subsidiary only (R442-R458; CON note 3 L672-681, "its only subsidiary"). The largest capital the parent deploys outside its own assets is its capital account in Danya, so the acquisition probe runs on it.
| Probe test | Reading | Anchor |
|---|---|---|
| Capital deployed ("price paid") | Parent capital in Danya Rs 12.68 Cr (31-Mar-26) to Rs 16.52 Cr (30-Sep-26), +Rs 3.84 Cr (+30.3%): Rs 2.75 Cr cash in plus Rs 1.10 Cr profit share left in | R123/R124 L950; R179 L1007; L983; A3 table 3e |
| Multiple paid on earnings | Annualised profit share = 109.73 lakh x 2 = 219.46 lakh (Rs 2.19 Cr). Closing capital 16.52 / 2.19 = 7.5x; yield 13.3% post-tax on closing capital (219.46 / 1,652.05 lakh) | Derived; L983, L950 |
| Earnings trend of the asset | Danya PAT (MI x 10) Rs 1.41 Cr H2FY26 to Rs 1.22 Cr H1FY27 = -13.6% HoH (H2FY26 is the unassured balancing column, A3-18); +29.8% YoY vs Rs 0.94 Cr H1FY26 | R269-R272 L1073; A3 3b |
| Pre-tax return vs group | Danya PBT 188.07 lakh (A3 3b) annualised 376.14 / closing partners' capital 2,051.00 = 18.3%. On the group's basis (EBIT incl. Danya finance cost 11.68, annualised 399.50, on average capital incl. Danya debt 2,196.28) = 18.2%. Group ROCE 23.6% (Step 7) | A3 3b, 3e; L1050 vs L891 |
| Tax leakage | Danya tax 66.15 / PBT 188.07 = 35.2% (taxed as a firm) vs parent 25.18% ex the exempt share (A3-09). [INFERENCE] The same profit earned inside the parent would carry about 18.79 lakh less tax per half (188.07 x 10.0 pp) | A3 3b, 3d; A3-09 |
| Funding cost vs yield | SA finance cost 280.11 lakh x 2 on average SA gross debt 5,037.40 lakh = 11.1%; [INFERENCE] about 8.3% after tax at 25.17%. The 13.3% post-tax yield clears it by about 5 pp | R031 L891; R097/R098, R103/R104 |
| Debt shift | Danya term debt (CON minus SA long-term borrowings) fell 317.80 to 21.35 lakh (-296.45, Rs 2.96 Cr repaid). Danya short-term debt (CON minus SA short-term borrowings) rose 106.80 to 221.12 lakh (+114.32, Rs 1.14 Cr). Danya total debt therefore fell 182.13 lakh (Rs 1.82 Cr). The parent borrowed 510.87 term and injected 274.59 [INFERENCE, A3-16] | L1110 vs L930; L1114 vs L934; A3 3e; R183 |
| Stock held in the asset | Implied Danya stock Rs 17.02 Cr at 30-Sep-26 (19.5% of group stock) against cash of 2.90 lakh; no unrealised profit eliminated in any period (Step 2, bear counter 2) | L953 vs L1131; L955 vs L1133; L194 vs L1074 |
| Related party | MD Vee Rajmohan holds 7.5% of Danya profit (L674-675). Minority drew 20.00 lakh (L1180), 7.81 above its 12.19 share. Minority capital share 19.5% vs 10% profit share. Interest on capital or remuneration to partners: NOT FOUND. The parent books no interest on capital from Danya (A3-16). Goods move both ways between the parent and Danya (FY26 floors Rs 8.44 Cr sold to, Rs 6.16 Cr bought from; 1-SVC) | A3-16; R427-R429, R452; L883/L1042, L887/L1046 |
| Assurance on the asset | Danya H1FY27 figures unaudited; review status bracket unresolved (L684) | A3-04, A3-12 |

Readings. Bull: the parent earns 13.3% post-tax on its Danya capital, above its after-tax cost of debt; if partners get no interest on capital, the minority's 19.5% capital share against a 10% profit share subsidises the parent. Bear: the parent grew its capital in Danya 30.3% in one half while its own cash fell to Rs 0.22 Cr. The asset's profit fell 13.6% HoH (against an unassured base), it earns about 18% pre-tax against the group's 23.6%, and it pays about 10 pp more tax. Its figures are unaudited, the MD is a partner, it trades with the parent in both directions, and it holds Rs 17.02 Cr of stock with no profit eliminated on it. Separating observation: Danya's FY27 audited accounts and partners' current-account statement (interest on capital, remuneration, drawings), plus intercompany flows and stock by source (Q12, Q13, Q20, Q21).

Checkpoint: cash quality tables, probe and answers complete.

---

## STEP 5.5. DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker pull
| Signal Name | Type | Cadence | Latest Observation | Direction | Thesis element | Signal Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied) | ND | ND | ND | ND | ND | ND |

Flag: fewer than three signals (zero supplied). Role 5.5 has not run for this company (no initial workup exists). The Role 5.5 signal set belongs to the initial workup, after the spear / Step-1 intake.

### 5.5B. Reconciliation
Target reported: STRONG on revenue and PAT (+80% / +45% CON YoY), WEAK on cash (CFO negative). Signals: ND. Matrix outcome: ND, not determinable.

### 5.5C. New signals
No new signals surfaced this quarter from the filing. The filing names no customer above 10%, no foreign partner, and no regulatory dependency. Payload rows for the tracker: none. (Under /run-quarterly, any row would pass the operator approval write gate; Decision Status is never written.)

### 5.5D. Forward view weighting
No signal trajectory exists, so Step 6 rests on the single half-year print only. Weight this print as one data point.

---

## STEP 6. RECONCILIATION VS THESIS (PRE-THESIS READ)

### 6A. Variance vs Notion projections
| Metric | Bear Proj | Base Proj | Bull Proj | Actual (H1FY27) | Lands In |
|---|---|---|---|---|---|
| Revenue | ND 'not passed' | ND 'not passed' | ND 'not passed' | CON 135.31 Cr / SA 127.14 Cr | ND |
| Op EBITDA margin | ND 'not passed' | ND 'not passed' | ND 'not passed' | CON 17.26% / SA 16.81% | ND |
| PAT | ND 'not passed' | ND 'not passed' | ND 'not passed' | Owners 13.65 Cr (CON = SA) | ND |
| EPS | ND 'not passed' | ND 'not passed' | ND 'not passed' | Rs 5.46 basic / Rs 5.45 diluted | ND |
| Net Debt | ND 'not passed' | ND 'not passed' | ND 'not passed' | CON 57.20 Cr / SA 54.80 Cr | ND |
| ROCE | ND 'not passed' | ND 'not passed' | ND 'not passed' | Indicative, annualised H1 EBIT / average capital employed: SA 23.6%, CON 23.6% (CON capital includes minority interest; 24.1% without it). Trade payables sit outside capital employed (Step 7 bear counter) | ND |

Probability re-weighting rule: not applicable (no projections; first review).

### 6B. Watchlist items
| # | Watchlist item | Green threshold | Red threshold | This half reading | Status |
|---|---|---|---|---|---|
| 1 | ND 'not passed' (no checklist) | ND | ND | ND | UNKNOWN |

### 6C. Thesis-broken trigger check
| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| ND 'not passed' (no conditions on record) | ND | ND | ND (cannot fire) |

### 6D. Growth trigger status
| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| ND 'not passed' | ND | ND | ND | ND |

Checkpoint: 6A-6D presented; all thesis fields ND.

---

## STEP 6.5. EXPECTATION LEDGER REVIEW AND A21 BASE REFRESH

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No expectation ledger exists for this name.
Pillar-relevant and base-relevant facts flagged for the downstream recompute (facts only, no recompute):
- [A21 BASE] H1FY27 PAT to owners Rs 13.65 Cr (R273); trailing two halves (H2FY26 + H1FY27) Rs 24.68 Cr (1,103.18 + 1,365.10 lakh); trailing basic EPS Rs 9.87 (4.41 + 5.46). The H2FY26 half is an unassured balancing figure (A3-18); FY26 audited PAT Rs 20.44 Cr is the assured anchor. FY26 shows H2 above H1; one year cannot establish seasonality, so the choice of single-half annualisation vs trailing base is open.
- [A21 BASE] No one-offs disclosed (R523, R544). SA other income includes the Danya share (1.10 Cr); group view has no treasury distortion (OI 1.42% of PBT). FY26 CON PBT may carry up to about Rs 1.62 Cr of unrealised margin on Danya stock (INFERENCE bound; H1FY27 at most Rs 0.12 Cr) (Step 2, bear counter 2).
- [SHARE COUNT] Basic 2,49,91,135; full warrant conversion 2,62,38,135 (+4.99%) if holders exercise within the window closing about 27-Feb-2027 (A3-05). Use 12,47,000 warrants, not the frozen diluted count (A3-10).
- [6.5B] Expectation ledger rows: none (ND).

## STEP 7. FOUR-PILLAR DESTINATION PE RE-VALIDATION

**Deferred to /fttcp and Role 1 (operator ruling OR-30).** No destination PE on record.
| Pillar / input | Original assumption | Current reading (fact flagged) | Action |
|---|---|---|---|
| ROCE base | ND 'not passed' | Indicative spot reading only: SA annualised H1 EBIT (PBT + FC = 20.68 Cr x 2) / average capital employed (net worth incl. warrants + debt; 163.93 Cr Mar-26, 186.88 Cr Sep-26) = 23.6%; CON (21.58 Cr x 2) / average capital employed incl. minority interest (172.25, 193.29) = 23.6%, or 24.1% with minority interest excluded (168.18, 189.30). CWIP 31.91 Cr is in capital employed and not earning. Trade payables (CON 84.59 Cr) are outside it (bear counter below). Archetype unresolved (A3-11); if a CONVERTER classification follows, spot ROCE must not feed Section 1B (v3.7 A17). | Deferred; FTTCP ROCE verdict is the sole authority |
| Cash multiplier | ND 'not passed' | H1FY27 CFO/PAT CON -0.42x, SA -0.38x; FY26 1.25x / 1.36x; INDETERMINATE-WITH-DIRECTION | Deferred; second reading due with FY27 results |
| Growth visibility premium | ND 'not passed' | Revenue CON +79.95% YoY, +27.12% HoH (HoH base unassured, A3-18); no order book disclosed; OCL (possible customer advances) down 21.9% (A3-17); EM score ND | Deferred |
| Strategic premium | ND 'not passed' | Moat ND; manufacturer vs trader unresolved; single-credit rule state ND | Deferred |
| UA multiplier | ND 'not passed' | Institutional ownership ND (not in filing) | Deferred |
| Sector cap | ND 'not passed' | Sector classification depends on A3-11 answer | Deferred |
| Hurdle ratio | ND 'not passed' | CMP ND, current PE ND, EPS CAGR ND | Deferred |

**Bear counter to the 23.6% spot ROCE: supplier credit funds the business outside capital employed.**
| Item (30-Sep-26 unless stated) | SA | CON | Anchor |
|---|---|---|---|
| Trade payables, Rs Cr | 75.61 (31.04 MSE + 44.57 others) | 84.59 (40.83 MSE + 43.76 others) | SA R105 L237, R107 L939; CON R313-R316 L1116-L1118 |
| Gross borrowings, Rs Cr | 55.02 | 57.45 | SA R097, R103; CON R305, R311 L1110, L1114 |
| Trade payables / borrowings | 137.4% | 147.3% | Derived |
| MSE share of trade payables | 41.1% | 48.3% | Derived |
| H1FY27 spend: purchases + other direct + other expenses + capex, Rs Cr | 135.12 (12,064.96 + 312.82 + 277.90 + 855.85 lakh) | 141.79 (12,653.73 + 323.88 + 333.44 + 867.85 lakh) | L887, L889, L893, L1003; L1046, L1048, L1052, L752 |
| MSE dues as days of total half-year spend (x 183), ex GST | 42.0 | 52.7 | Derived; a lower bound (see below) |
| Same, spend grossed up for 18% GST [INFERENCE: rate assumed] | 35.6 | 44.7 | Derived |
| Statutory maximum payment term to MSEs | 45 days with a written agreement, 15 days without (MSMED Act 2006, s.15) [INFERENCE: background law, not in filing] | Same | Background law |
| Overdue-MSE disclosure (principal or interest) in the filing | None | None | Grep L1-L1193: no "overdue", no MSMED interest line |
| ROCE with trade payables counted as capital [INFERENCE sensitivity] | 17.0% (4,135.56 / avg 24,298.01 lakh) | 16.8% (4,315.60 / avg 25,616.66 lakh) | Derived |

How to read the bound: the denominator assumes every rupee of half-year spend went to MSE suppliers, so the true MSE payable days can only be equal or longer. On that bound, consolidated MSE dues equal at least 52.7 days of spend, or about 44.7 days if the spend carries 18% GST like the payable balance does. The like-for-like (GST) figure sits at the 45-day statutory ceiling with no headroom; the ex-GST figure is above it. The standalone bound is lower (42.0 / 35.6), so the excess sits in the consolidated-minus-standalone part: Danya plus eliminations, MSE dues Rs 9.79 Cr (40.83 - 31.04) [INFERENCE]. Reading 1: normal trade credit, mostly from large suppliers (MSEs hold under half of payables) on standard terms; the high ROCE is a supplier-funded, capital-light working-capital model. Reading 2: small suppliers are paid beyond the statutory term; that carries interest under MSMED s.16 and a tax-deduction disallowance under Income-tax Act s.43B(h) [INFERENCE: background law], and the ROCE overstates what the business earns on the capital it would need if supplier credit tightened (16.8% with payables counted). Separating observation: principal and interest overdue to MSEs at 31-Mar-2027 (FY27 Annual Report MSMED disclosure) or a direct company answer (Q16).

---

## STEP 8. POSITION DECISION

Decision Status verified in Step 0A: **ND (no Notion page). Not held. Branch: 8A-W (watchlist / non-held).**

8A-W walk:
- Thesis-broken condition FIRED? Cannot be tested (no conditions on record). Not reclassified.
- Below bear on 2+ metrics? Cannot be tested (no projections).
- Between bear and base / at or above base? Cannot be tested.
- Output: **no entry zone exists; no gate exists.** The next gate is the spear gate: a Spear line in companies/SUPREMEPWR.md (via /step1 intake or the web spear) before any /run-pipeline work. Proposed Decision Status: none proposed; the operator sets it.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: ND 'not passed'. Revised: not applicable (not held).
- Original trim ladder: ND 'not passed'. Revised: not applicable.
- Pre-thesis watch conditions this filing suggests for any future thesis: CON CCC back at or below 104.4 days; warrants exercised in full; Danya review status resolved; manufacturer vs trader split disclosed; no MSE dues overdue; intercompany flows and Danya stock by source disclosed.

### 8C. Single cleanest metric for next reading
**Consolidated cash conversion cycle at 31-Mar-2027** (receivable + inventory - payable days, end balance on half-year revenue or material cost), filed with FY27 results.
- Bull threshold: at or below 104.4 days (back to the 31-Mar-26 level), which would show the H1FY27 build as growth timing.
- Bear threshold: above 120.6 days (worse than 30-Sep-26), which would show structural working capital and continued funding strain.
Why this one: it separates the two readings of the H1FY27 cash outflow (growth timing vs structural), and it drives the funding need that bank lines, and warrant exercise if holders choose it, must meet. Read it with payable days: a CCC held down only by longer payables is not a bull reading (Step 7 bear counter).

---

## STEP 8.5. QUESTIONS FOR MANAGEMENT

Every A3 FORWARD-SIGNAL (A3-01, A3-05, A3-06) and AMBIGUOUS finding (A3-02, A3-03, A3-04, A3-07, A3-10, A3-11, A3-12, A3-14, A3-16, A3-17) maps to at least one question. A3-13 is NEUTRAL-FACT (OCR) and goes to A1 as a re-read, not to management (preamble routing list). A3-18 is NEUTRAL-FACT; it is carried as a caveat on H2FY26 cells and needs no question (A3). Q20 and Q21 come from A4's loop 2 reads of the S-vs-C gap (two-way flows, unrealised profit) and sit under A3-02. Ordered by importance. 21 questions.

| # | Cat. | Question | Why it matters | Bull answer | Bear answer | From finding |
|---|---|---|---|---|---|---|
| 1 | F | Of the 12,47,000 warrants, how many are held by the Promoter group, and on what exact date does the 18-month exercise window close? Do the holders intend to exercise and pay the Rs 126.75 balance (Rs 15.81 Cr in total) before that date: yes or no? | Zero conversions at 30-Sep-26 (L1012); the balance is payable only if holders exercise (L848-850); SA cash Rs 0.22 Cr. | Promoter majority, full exercise intended before the deadline. | Partial or no exercise; 25% money forfeited. | A3-01, A3-05 |
| 2 | D | SA net debt rose Rs 18.81 Cr to Rs 54.80 Cr and cash fell to Rs 0.22 Cr in six months. What sanctioned working capital limits were undrawn at 30-Sep-26, in Rs Cr? | Tests liquidity headroom for H2FY27 at negative CFO (SA Rs (5.23) Cr). | Undrawn limits above Rs 15 Cr, renewal confirmed. | Limits near fully drawn; new debt or equity needed. | A3-01 |
| 3 | D | SA inventory rose Rs 24.88 Cr (+54.6%) to Rs 70.44 Cr. What share is finished goods awaiting dispatch against confirmed orders, and what was the order book at 30-Sep-26, in Rs Cr? | Separates growth-induced WC from structural build; CON CCC rose 16.25 days. | Most inventory is order-backed FG; order book covers more than one year of revenue. | Raw material or unsold stock; order book not disclosed. | Step 5 (cash classification) |
| 4 | A | The P&L shows all material cost as "Purchases of Stock in Trade" (Rs 120.65 Cr SA H1FY27) with no cost of materials consumed line. What % of H1FY27 revenue came from goods manufactured in-house vs traded? | Sets the archetype and Section 1B rung; the company is building a factory. | Mostly manufactured; label is a presentation choice to be corrected. | Material share of traded goods; manufacturing is minor. | A3-11 |
| 5 | B | CWIP stands at Rs 31.91 Cr (up Rs 3.93 Cr in the half). What asset is it, what capacity does it add, and what is the commissioning date (month and year)? | D&A and finance cost already outrun revenue; capitalisation adds more fixed cost. | Named asset, date within FY27, capacity quantified. | No date or date slipping beyond FY28. | A3-11 |
| 6 | F | Of the Rs 5.20 Cr of warrant proceeds utilised, how much went to factory premises, how much to working capital, and how much to general corporate purposes, in Rs lakh? | One blended object makes "no deviation" untestable (L834). | Majority to factory, split disclosed. | Mostly WC or GCP; split refused. | A3-06 |
| 7 | A | What were Danya Electric Company's revenue and intercompany sales with the parent in H1FY27 and H1FY26, in Rs Cr? | CON minus SA revenue flipped from Rs (5.47) Cr to +Rs 8.17 Cr; CON margin fell while SA margin rose. | Danya external sales grew; intercompany stable. | SA margin gain came from intercompany pricing or reduced eliminations. | A3-02 |
| 8 | C | CON operating EBITDA margin fell 151 bps YoY to 17.26% and CON gross margin fell 129 bps to 25.22%. Was the cause input cost or selling price and mix? Give the gross margin bridge in bps. | Group margin dipped in each of the last three halves. | Input cost spike with pass-through clauses in place. | Price concessions to win volume. | A3-02 |
| 9 | G | Did any staff or expenses move between Danya and the parent in FY26 or H1FY27? Consolidated other expenses in H1FY26 are Rs 0.43 Cr below standalone, and consolidated employee cost in H2FY26 is Rs 0.44 Cr below standalone. | Line-by-line consolidation should not reduce a cost line. The H1FY26 cell is a filed half; the H2FY26 cell is an unassured balancing figure (A3-18). | Disclosed intercompany charge eliminated; amount stated. | No explanation; reclassification of unknown size. | A3-03 |
| 10 | G | Were Danya's H1FY27 results reviewed by the statutory auditor, or certified by management only: which one? Will the company file a corrected note 4? | Filed note leaves "[reviewed by the Statutory Auditors / certified by the management]" unresolved (L684). | Auditor-reviewed; corrected note filed. | Management-certified; no correction. | A3-12, A3-04 |
| 11 | G | In H1FY27 the consolidated receivables build exceeded the standalone build by at least Rs 8.65 Cr, while consolidated revenue exceeded standalone by Rs 8.17 Cr. How much of that difference is Danya's external receivables, and how much is a change in the parent's receivable from Danya? Will the company disclose Danya's revenue, PAT and receivables in Rs each half? | The difference moves with both Danya's receivables and intercompany balances; Danya's numbers are unaudited (L472-474). | Intercompany balance fell; Danya's external receivables flat; disclosure from FY27. | Danya's external receivables rose by the full amount; no disclosure. | A3-04 |
| 12 | G | Does Danya pay the MD (a 7.5% partner) or the other partner interest on capital, salary or remuneration? State the amounts for FY26 and H1FY27. Why did the minority partners withdraw Rs 0.20 Cr, above their Rs 0.12 Cr profit share, while the parent injected Rs 2.75 Cr? | Related-party flows against the listed parent (L1007, L1180); the parent books no interest on capital from Danya. | No payments to partners; withdrawal is a one-off. | Material partner interest or remuneration; flows unexplained. | A3-16 |
| 13 | G | In H1FY27 Danya repaid Rs 2.96 Cr of term debt while its short-term debt rose Rs 1.14 Cr, so its total debt fell Rs 1.82 Cr; in the same half the parent took on Rs 5.11 Cr of term debt. Why did the debt move to the parent, and why grow the parent's capital in Danya 30.3% (to Rs 16.52 Cr) in a firm taxed at about 35% that earns about 18% pre-tax against the group's 23.6%? Is there a plan to merge Danya or buy out the partners? | Debt moved to the listed parent; tax leakage about 10 pp on Danya profit (Step 5-D). | Stated project inside Danya; merger or buyout plan with timeline. | No rationale; capital keeps flowing to a related-party firm. | A3-16 |
| 14 | D | In the FY26 SA cash flow, where was the Danya profit share (about Rs 2.12 Cr) removed as non-cash, and what was the parent's investment in Danya at 31-Mar-2025? How much of FY26 SA CFO (Rs 27.73 Cr) is non-cash firm profit? | FY26 CFO/PAT 1.36x may be overstated (A3-14). | Deducted elsewhere; amount and Mar-25 balance stated. | Not deducted; FY26 CFO overstated. | A3-14 |
| 15 | D | Note 4 says payables, loans and advances and other current liabilities await confirmation. What % of SA trade payables (Rs 75.61 Cr) were confirmed at the FY26 audit, and what adjustment was booked in Rs? | Adjustments land in "the year of confirmation" (L321-322), possibly the FY27 audit. | Above 90% confirmed; nil adjustment. | Low coverage; adjustments pending. | A3-07 |
| 16 | D | Of the Rs 40.83 Cr consolidated dues to micro and small enterprises at 30-Sep-26, how much was outstanding beyond the agreed or statutory term, and what interest was accrued under MSMED s.16? Any s.43B(h) tax disallowance expected for FY27? | MSE dues equal at least 52.7 days of half-year spend (44.7 with GST) against a 45-day term; no overdue disclosure in the filing (Step 7). | Nil overdue; nil interest. | Material overdue amount; interest and tax add-back. | A3-07 (Step 7 bear counter) |
| 17 | D | Give the breakup of other current liabilities (customer advances, capital creditors, statutory dues, current maturities of debt) at 31-Mar-26 and 30-Sep-26. Did customer advances fall in H1FY27? | SA OCL fell Rs 4.00 Cr after the FY26 Rs 14.56 Cr build that supplied 52.5% of FY26 SA CFO. | Fall is capital creditors or a reclass; customer advances stable or up. | Customer advances unwound; order intake lags execution. | A3-17 |
| 18 | G | The diluted share count is 2,50,67,330 in H2FY26, FY26 and H1FY27. Which method and which share price produced it, and why does the FY26 day-weighted count equal the H2FY26 count? | Note 6 says day-weighting; the count implies one fixed price of about Rs 135; diluted EPS shows 0.3% dilution vs 4.99% on full conversion. | Treasury-stock method with prices stated; FY26 count corrected. | No method disclosed. | A3-10 |
| 19 | E | What share of H1FY27 revenue came from the top customer and from the top five, and are any of them state utilities? | CON receivable days 84.77; no customer data in the filing. | Diversified; no customer above 10%. | Concentrated or utility-heavy with long payment cycles. | Step 5 (cash) |
| 20 | G | In FY26 the parent sold at least Rs 8.44 Cr of goods to Danya and bought at least Rs 6.16 Cr from it (consolidated revenue and purchases sit those amounts below standalone). What were the intercompany sales in each direction in FY26 and H1FY27, in Rs Cr? What goods move each way, and on what pricing basis? What did the parent owe Danya at 31-Mar-26 and 30-Sep-26 (consolidated other creditors sit Rs 4.48 Cr below standalone at 31-Mar-26)? | Two-way trade with a firm in which the MD is a partner makes the margin split a pricing choice; SA margin +128 bps vs CON -151 bps (1-SVC, Step 2). | Distinct product flows each way (for example components one way, finished units the other) at stated cost-plus terms; balances disclosed. | Same goods moving both ways; pricing undisclosed; the creditors gap is an unexplained regrouping. | A3-02, A3-03 (A4 loop 2, 1-SVC) |
| 21 | G | Consolidated owners' PAT equals standalone PAT in all four periods, so no unrealised profit in Danya's closing stock was eliminated. How much of Danya's Rs 17.02 Cr stock at 30-Sep-26 (Rs 16.53 Cr at 31-Mar-26) was bought from the parent, and at what margin? Why did no elimination arise? What does Danya hold, and how does it fund that stock with Rs 2.90 lakh of cash? | FY26 CON profit could carry up to about Rs 1.62 Cr pre-tax of margin not yet earned outside the group (INFERENCE bound); Danya holds 19.5% of group stock (Step 2, bear counter 2). | Stock bought from outside suppliers; nil intercompany stock; nil elimination correct. | Parent-sourced stock at the parent's selling price; FY26 profit and equity overstated by the unrealised margin. | A3-02 (A4 loop 2, Step 2 bear counter 2) |

**Top 3 questions by likelihood of changing the read:**
- Q4 (manufactured vs traded share): a "mostly manufactured" answer raises the bull case probability and sets the archetype.
- Q2 (undrawn limits): a "near fully drawn" answer confirms the bear case of balance-sheet strain.
- Q10 (Danya auditor-reviewed or management-certified): a direct test of management transparency.

**Channel recommendation:** IR email / formal IR letter now. SME company with no concall in this run; AGM Q&A is the only live channel, and the next AGM date is ND. Send all 21 questions verbatim in writing. The A3-13 receivables item is not in the letter; it goes to A1.

---

## STEP 9. NOTION UPDATE (payload only)

No Notion company page exists. /run-quarterly writes Notion only after operator approval of a printed payload, and never writes Decision Status. Proposed payload: none for the company row (no page to update). Recommended action for the operator: decide whether to open the name via /step1 intake; if so, this review is the first institutional record (full tables above).
- Catalyst status: ND. Thesis status: ND (pre-thesis).
- Source: NSE results filing dated 16.10.2026 (R001, R472; outcome letter addressed to the NSE Listing Department, L19-26), SupremePower_H1FY27_Results.pdf.
- Auditor opinion: Limited review, unmodified conclusion (SA and CON); consolidated reliance on unaudited, likely management-certified subsidiary.
- Business type: Standard.

---

## MONITORABLES / CATALYST LIST (from A3 F6 register and F13 board outcome)

| # | Item | Implied date | Source ref |
|---|---|---|---|
| 1 | Warrant exercise or lapse: 12,47,000 warrants; Rs 15.81 Cr balance payable only if holders exercise; +4.99% shares on full exercise | about 27-Feb-2027 (18 months from 27-Aug-2025; exact ICDR end date ND) | A3-01, A3-05; R417, R464, R480; L314-315, L848-855 |
| 2 | Next Reg 32 utilisation certificate: use of the 6.55 lakh unutilised and any new proceeds, split by object | with FY27 annual results, by about 30-May-2027 (implied, Reg 33 60-day rule) | A3-06; R403-R406, R551; L818-836 |
| 3 | FY27 annual results (H2FY27 half): CON CCC (the 8C metric), payable days, FY27 CFO/PAT, net debt, OCL level | by about 30-May-2027 (implied) | Step 5, Step 8C; A3-17 |
| 4 | Balance-confirmation adjustments on payables, loans and advances, other current liabilities | Undated by the company (note 4: "the year of confirmation"); earliest observable with FY27 audited results, about 30-May-2027 | A3-07; R466, R467; L321-322, L686-688 |
| 5 | CWIP Rs 31.91 Cr capitalisation (visible as a D&A step and PPE jump) | Undated (no commissioning date filed); earliest observable in FY27 results, about 30-May-2027 | A3-11; R119, R120 |
| 6 | FY27 Annual Report: Danya review status and audited figures, partner payments, intercompany sales each way and Danya stock by source (unrealised-profit elimination), MSMED overdue principal and interest, OCL breakup | before the AGM (AGM by 30-Sep-2027, implied) | A3-02, A3-04, A3-12, A3-16, A3-17; R539, R456-R458; 1-SVC; Step 2 bear counter 2; Step 7 |
| 7 | Board outcome forward items | None beyond results and the Reg 32 statement (no dividend, AGM, record date, director or auditor items) | A3 F13; R472-R474, R551 |

---

## PROTOCOL VERDICT

**PROCEED WITH FLAGS.**
- Cash conversion is INDETERMINATE-WITH-DIRECTION (deteriorating), which caps the verdict below PROCEED; named missing evidence: order book, inventory composition, OCL breakup, undrawn limits, FY27 CFO.
- Flags: negative CFO with near-zero cash and net debt up 42% to 52%; group margin down 151 bps YoY while standalone shows a gain; revenue booked outside the parent not collected (receivables build at least Rs 8.65 Cr against Rs 8.17 Cr revenue); goods moving both ways between the parent and Danya in FY26 with no unrealised profit eliminated on Danya's Rs 17.02 Cr stock (FY26 effect at most about Rs 1.62 Cr pre-tax, INFERENCE; H1FY27 not inflated); trade payables 147% of borrowings with MSE dues at the statutory ceiling on the bound; an unaudited subsidiary partly owned by the MD, with the parent's capital in it up 30.3%; archetype unresolved (trading label vs factory build); A1 rows that fail arithmetic (SA H1FY27 total expenses ND, SA Mar-26 receivables held out, routed to A1); H2FY26 column unassured (A3-18), so HoH reads are weighted lower.
- Not REWORK: no Verifier A CRITICAL; the headline numbers (revenue, PBT, PAT, CON balance sheet and cash flow) tie internally.
- Not INSUFFICIENT EVIDENCE: the filing supports a full extraction; only the thesis baseline is missing, which the pre-thesis framing handles.

---

## PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (this filing), MGMT (management statement), AGENCY (rating agency), SECONDARY (third-party), INFERENCE (analyst reasoning or background knowledge). No prior Notion or peer work exists; every figure below comes from this half's filing unless marked otherwise.

### 1. Summary narrative
Supreme Power grew fast this half. Group revenue was Rs 135.31 Cr, up 79.95% from Rs 75.19 Cr a year ago [FILED]. Group profit after tax was Rs 13.77 Cr, up 44.94% [FILED]. Profit grew slower than sales. The group operating margin fell from 18.77% to 17.26% [FILED].
Depreciation and interest rose much faster than sales [FILED]. The likely cause is new assets: the company spent Rs 57.48 Cr on assets in FY26 and still holds Rs 31.91 Cr of unfinished assets [FILED figures; the link is INFERENCE].
Cash went the other way. Operations used Rs 5.74 Cr of cash in the half [FILED]. Inventory rose Rs 25.36 Cr and customer dues rose Rs 15.84 Cr [FILED]. Cash fell to Rs 0.25 Cr and net debt rose to Rs 57.20 Cr [FILED].
Sales booked outside the parent were Rs 8.17 Cr, and the group's customer dues rose at least Rs 8.65 Cr more than the parent's [FILED, derived]. That money had not come in by 30 September [INFERENCE].
Suppliers fund more of the business than banks do. Group trade payables are Rs 84.59 Cr, 147% of borrowings [FILED, derived].
Investors paid 25% upfront on the company's convertible warrants [FILED]. The other 75%, Rs 15.81 Cr, comes in only if holders choose to convert before the window closes, about February 2027 [FILED; date INFERENCE from the 18-month window]. No holder has converted yet [FILED].
The only subsidiary, Danya Electric Company, is a partnership in which the managing director holds 7.5% [FILED]. Its numbers are unaudited, and the filing does not say whether the auditor reviewed them [FILED]. The parent raised its capital in Danya 30.3% to Rs 16.52 Cr this half [FILED, derived].
Goods moved both ways between the parent and Danya in FY26. The parent sold at least Rs 8.44 Cr to Danya and bought at least Rs 6.16 Cr from it [FILED, derived]. Danya holds Rs 17.02 Cr of stock and almost no cash [FILED, derived]. The group removed no profit on that stock. FY26 group profit may therefore include up to about Rs 1.62 Cr of margin not yet earned outside the group [INFERENCE]. This half is not inflated this way, because Danya's stock rose only Rs 0.48 Cr [FILED, derived].
This is a first read. There is no thesis, no entry price and no Decision Status. The decision stays with the operator: open the name through the spear gate, or leave it.

### 2. Sector intelligence
- The filing calls the company a single-segment business and gives no sector data [FILED].
- Background, not from the filing: Supreme Power Equipment is understood to make transformers in Tamil Nadu, for utilities and renewable projects [INFERENCE, model background, PENDING LIVE VERIFICATION].
- Sector demand cycle, utility tender flow and copper or steel input cost: ND in this corpus. No AGENCY or SECONDARY source was supplied.
- What this half shows that fits a strong demand cycle: revenue up 79.95% YoY and up 27.12% on the prior half [FILED; the prior half is an unassured balancing figure]. What it shows that fits a stretched cycle: inventory days up 17.14 to 158.18 [FILED, derived].
- Rule that bears on small suppliers: Indian law caps payment terms to micro and small suppliers at 45 days [INFERENCE, background law]. The group's dues to them sit at that ceiling on the most generous measure [FILED, derived].

### 3. Business-model intelligence
- The P&L lists all material cost as goods bought for resale. There is no raw-material line [FILED]. Yet the company is building a factory [FILED]. Either the label is wrong or a large share of sales is traded goods [INFERENCE]. This one answer decides how the business should be valued.
- Unit economics: group gross margin 25.22%, operating margin 17.26%, profit margin 10.18% in H1FY27 [FILED, derived].
- Model drift this half: (a) fixed costs are rising. Depreciation plus interest went from 1.87% to 3.67% of group sales [FILED, derived]. (b) Working capital is getting heavier. The group cash cycle rose from 104.4 to 120.6 days [FILED, derived]. (c) Margin is moving between parent and subsidiary. The standalone margin rose 128 bps while the group margin fell 151 bps [FILED, derived]. Goods flow both ways between the two, so the split is partly a pricing choice [INFERENCE]. (d) Return on capital looks high because suppliers carry much of the funding. The spot return is 23.6%, or 16.8% if supplier credit counts as capital [FILED, derived; INFERENCE sensitivity].
- Capital sent to Danya earns 13.3% after tax on the parent's share. That beats the cost of debt but trails the group's own return, and Danya pays about 10 points more tax [FILED, derived; INFERENCE].
- Not disclosed: order book, capacity, utilisation, customer mix, product mix, Danya revenue, intercompany sales, Danya stock by source, overdue supplier dues.

### 4. Competition intelligence
- Named peers from background, not from the filing: other Indian listed transformer makers such as Shilchar Technologies, Voltamp Transformers, Transformers and Rectifiers India, Indo Tech Transformers and Danish Power [INFERENCE, model background, PENDING LIVE VERIFICATION]. No peer figures are in the corpus. Peer margins, growth and working capital are ND.
- Where the company looks strong: growth of 79.95% YoY and a group operating margin near 17% [FILED].
- Where it looks weak: a thin balance sheet (cash Rs 0.25 Cr, net debt Rs 57.20 Cr) and a cash cycle of 120.6 days [FILED]. A small maker that funds growth with debt and supplier credit has less room to bid on large tenders than a cash-rich peer [INFERENCE].
- Risk to watch: price concession to win volume. The group gross margin fell 129 bps YoY [FILED]. The filing does not show whether input cost or pricing caused it.

### 5. Forward map (next ~10-11 months)
- **Make-or-break reading:** group cash conversion cycle at 31-Mar-2027, with FY27 results by about 30-May-2027. Bull: at or below 104.4 days. Bear: above 120.6 days.
- **Warrant window, about 27-Feb-2027.** Bull: holders exercise and pay the Rs 15.81 Cr balance in full, and cash pressure eases. Bear: holders do not exercise, the 25% is forfeited, and debt must fund the gap.
- **FY27 results and Reg 32 certificate, about 30-May-2027.** Bull: CFO turns positive for the year and the proceeds split favours the factory. Bear: CFO stays negative and proceeds went to working capital.
- **Balance-confirmation adjustments, earliest with FY27 audited results, about 30-May-2027 (the company gives no date).** Bull: nil adjustment. Bear: a write-down against payables or advances.
- **CWIP Rs 31.91 Cr capitalisation, earliest visible in FY27 results, about 30-May-2027 (no commissioning date filed).** Bull: the plant starts and lifts both margin and sales. Bear: the date slips while interest and depreciation keep rising.
- **FY27 Annual Report, before the AGM (by about 30-Sep-2027).** Bull: Danya is audited, partner payments are nil or small, intercompany flows are disclosed and Danya's stock came from outside suppliers, no supplier dues are overdue, and the manufacturing share is disclosed. Bear: Danya stays management-certified, related-party flows grow, parent-sourced stock sits in Danya with no profit removed, and overdue supplier dues appear.

---

```yaml
stage: A4-analyst
company: "SUPREMEPWR"
quarter: "h1fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results]
ledger_reconciliation:
  notes: 21
  turns: 0
  slides: 0
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "ND (no Notion page; companies/SUPREMEPWR.md absent; no spear). PRE-THESIS READ, treated as not held"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "H1FY26", owners_pat_gap_pct: 0.00, group_pat_incl_mi_gap_pct: 1.00}
  - {period: "H2FY26", owners_pat_gap_pct: 0.00, group_pat_incl_mi_gap_pct: 1.28}
  - {period: "FY26", owners_pat_gap_pct: 0.00, group_pat_incl_mi_gap_pct: 1.15}
  - {period: "H1FY27", owners_pat_gap_pct: 0.00, group_pat_incl_mi_gap_pct: 0.89}
questions_for_management:
  - {q: "Promoter share of the 12,47,000 warrants, exact exercise-window end date, and do holders intend to exercise and pay the Rs 15.81 Cr balance before it (yes/no)?", from_finding_id: "A3-01, A3-05"}
  - {q: "Undrawn sanctioned working capital limits at 30-Sep-26 in Rs Cr, given SA cash Rs 0.22 Cr and net debt Rs 54.80 Cr?", from_finding_id: "A3-01"}
  - {q: "Share of the Rs 70.44 Cr SA inventory that is order-backed finished goods, and order book at 30-Sep-26 in Rs Cr?", from_finding_id: "A4-step5"}
  - {q: "Percent of H1FY27 revenue manufactured in-house vs traded, and why no cost of materials consumed line?", from_finding_id: "A3-11"}
  - {q: "What asset is CWIP Rs 31.91 Cr, what capacity, and what commissioning month?", from_finding_id: "A3-11"}
  - {q: "Split of the Rs 5.20 Cr warrant proceeds utilised across factory, working capital and GCP, in Rs lakh?", from_finding_id: "A3-06"}
  - {q: "Danya revenue and intercompany sales with the parent in H1FY27 and H1FY26, in Rs Cr?", from_finding_id: "A3-02"}
  - {q: "Gross margin bridge in bps for the 129 bps CON gross margin fall: input cost or price and mix?", from_finding_id: "A3-02"}
  - {q: "Did staff or expenses move between Danya and the parent; why are CON other expenses Rs 0.43 Cr below SA in H1FY26 and CON employee cost Rs 0.44 Cr below SA in H2FY26 (unassured balancing column)?", from_finding_id: "A3-03"}
  - {q: "Were Danya H1FY27 results auditor-reviewed or management-certified, and will note 4 be corrected?", from_finding_id: "A3-12, A3-04"}
  - {q: "Of the at-least Rs 8.65 Cr by which the CON receivables build exceeded SA, how much is Danya external receivables vs a change in the parent's receivable from Danya; will Danya revenue, PAT and receivables be disclosed each half?", from_finding_id: "A3-04"}
  - {q: "Does Danya pay the MD or the other partner interest on capital or remuneration (FY26, H1FY27 amounts); why did minority partners withdraw Rs 0.20 Cr, above their Rs 0.12 Cr share, while the parent injected Rs 2.75 Cr?", from_finding_id: "A3-16"}
  - {q: "Danya repaid Rs 2.96 Cr of term debt while its short-term debt rose Rs 1.14 Cr (total debt down Rs 1.82 Cr) as the parent took on term debt: why did debt move to the parent, and why grow parent capital in Danya 30.3% in a firm taxed about 35% earning about 18% pre-tax vs group 23.6%; any merger or partner buyout plan?", from_finding_id: "A3-16"}
  - {q: "Where was the about Rs 2.12 Cr Danya profit share removed in the FY26 SA cash flow, what was the parent's investment in Danya at 31-Mar-2025, and how much of FY26 SA CFO Rs 27.73 Cr is non-cash?", from_finding_id: "A3-14"}
  - {q: "Percent of SA trade payables (Rs 75.61 Cr) confirmed at the FY26 audit and adjustments booked, in Rs?", from_finding_id: "A3-07"}
  - {q: "Of the Rs 40.83 Cr consolidated MSE dues at 30-Sep-26, how much was beyond the agreed or statutory term, what MSMED s.16 interest was accrued, and any s.43B(h) disallowance expected for FY27?", from_finding_id: "A3-07"}
  - {q: "Breakup of other current liabilities (customer advances, capital creditors, statutory dues, current maturities) at 31-Mar-26 and 30-Sep-26; did customer advances fall in H1FY27?", from_finding_id: "A3-17"}
  - {q: "Method and price behind the frozen diluted count 2,50,67,330 across H2FY26, FY26 and H1FY27 (implied fixed price about Rs 135)?", from_finding_id: "A3-10"}
  - {q: "Top customer and top-five share of H1FY27 revenue; any state utilities?", from_finding_id: "A4-step5"}
  - {q: "FY26: parent sold at least Rs 8.44 Cr to Danya and bought at least Rs 6.16 Cr from it. Intercompany sales each way in FY26 and H1FY27 in Rs Cr, goods and pricing basis each way, and amount owed by the parent to Danya at 31-Mar-26 and 30-Sep-26 (CON other creditors Rs 4.48 Cr below SA at 31-Mar-26)?", from_finding_id: "A3-02, A3-03 (A4 loop 2, 1-SVC)"}
  - {q: "Owners' PAT equals SA PAT in all four periods, so no unrealised profit was eliminated: how much of Danya's Rs 17.02 Cr stock (Rs 16.53 Cr at 31-Mar-26) was bought from the parent, at what margin, why no elimination, what Danya holds, and how it funds that stock with Rs 2.90 lakh cash?", from_finding_id: "A3-02 (A4 loop 2, Step 2 bear counter 2)"}
monitorables:
  - {item: "Warrant exercise or lapse, 12,47,000 warrants, Rs 15.81 Cr balance payable only on exercise, +4.99% shares on full exercise", implied_date: "about 27-Feb-2027", source_ref: "A3-01, A3-05; R417, R464, R480; L314-315, L848-855"}
  - {item: "Next Reg 32 utilisation certificate with object-wise split", implied_date: "about 30-May-2027 (with FY27 results, implied)", source_ref: "A3-06; R403-R406, R551; L818-836"}
  - {item: "FY27 results: CON cash conversion cycle (bull <=104.4 days, bear >120.6 days), payable days, FY27 CFO/PAT, net debt, OCL level", implied_date: "about 30-May-2027 (implied, Reg 33)", source_ref: "Step 5, Step 8C; A3-17"}
  - {item: "Balance-confirmation adjustments on payables, advances, other current liabilities", implied_date: "undated by company; earliest with FY27 audited results, about 30-May-2027", source_ref: "A3-07; R466, R467; L321-322, L686-688"}
  - {item: "CWIP Rs 31.91 Cr capitalisation (D&A step, PPE jump)", implied_date: "undated (no commissioning date filed); earliest in FY27 results, about 30-May-2027", source_ref: "A3-11; R119, R120"}
  - {item: "FY27 Annual Report: Danya review status and audited figures, partner payments, intercompany sales each way and Danya stock by source (unrealised-profit elimination), MSMED overdue principal and interest, OCL breakup", implied_date: "before AGM (by about 30-Sep-2027)", source_ref: "A3-02, A3-04, A3-12, A3-16, A3-17; R539, R456-R458; 1-SVC; Step 2 bear counter 2; Step 7"}
flags:
  - "PRE-THESIS READ: no Notion page, no companies file, no spear line; Decision Status ND; all thesis fields ND"
  - "Cash conversion INDETERMINATE-WITH-DIRECTION (deteriorating): CFO CON Rs (5.74) Cr, SA Rs (5.23) Cr vs PAT Rs 13.77 / 13.65 Cr; CON CCC 104.36 to 120.61 days; missing: order book, inventory mix, OCL breakup, undrawn limits, FY27 CFO"
  - "Funding strain: SA cash Rs 9.74 Cr to Rs 0.22 Cr; SA net debt +Rs 18.81 Cr (+52.3%); CON net debt +42.2% to Rs 57.20 Cr"
  - "Warrant balance Rs 15.81 Cr unexercised and payable only if holders exercise; window closes about 27-Feb-2027; zero conversions at 30-Sep-26"
  - "S-vs-C divergence: CON Op EBITDA margin -151 bps YoY (18.77% to 17.26%) vs SA +128 bps; revenue gap flipped from Rs (5.47) Cr to +Rs 8.17 Cr; CON receivables build exceeds SA by at least Rs 8.65 Cr"
  - "Two-way intercompany trade (FY26 audited): parent sold at least Rs 8.44 Cr to and bought at least Rs 6.16 Cr from Danya; CON other creditors Rs 4.48 Cr below SA at 31-Mar-26 (L1118 vs R108 L939)"
  - "No unrealised profit eliminated: owners' PAT = SA PAT in all four periods (L194 vs L1074); Danya stock Rs 17.02 Cr (19.5% of group) with Rs 2.90 lakh cash; FY26 CON profit could carry up to about Rs 1.62 Cr pre-tax (INFERENCE bound); H1FY27 at most Rs 0.12 Cr (Danya stock +Rs 0.48 Cr), so H1FY27 growth not inflated"
  - "Supplier funding outside ROCE: CON trade payables Rs 84.59 Cr = 147.3% of borrowings; MSE dues Rs 40.83 Cr = at least 52.7 days of half-year spend (44.7 with GST) vs 45-day statutory term (INFERENCE, background law); no overdue-MSE disclosure; ROCE 16.8% with payables counted"
  - "Governance: sole subsidiary Danya is unaudited, review-status bracket unresolved in note 4, MD is a 7.5% partner; parent capital in Danya +30.3% to Rs 16.52 Cr (Rs 2.75 Cr cash) while partners withdrew Rs 0.20 Cr; Danya earns 18.3% pre-tax vs group 23.6%, taxed 35.2%"
  - "Other current liabilities fell Rs 4.00 Cr SA (21.9%) after the FY26 Rs 14.56 Cr build that supplied 52.5% of FY26 SA CFO (A3-17)"
  - "Archetype unresolved: all material cost labelled stock-in-trade while a factory is built (CWIP Rs 31.91 Cr)"
  - "H2FY26 column is an unassured balancing figure (A3-18): H2FY26-based HoH deltas and cells in A3-02, A3-03, A3-09 weighted lower"
  - "Extraction integrity: SA H1FY27 total expenses ND (R043 fails footing); SA Mar-26 receivables (R130, R153) held out pending A1 re-read (A3-13 NEUTRAL-FACT); R065 read as credit; R117/R118 anchor L945 vs values at L947; routing list in preamble"
  - "Capex absorption: CON D&A +415% and finance cost +190% vs revenue +80% YoY"
  - "Tracker rows not supplied: Step 5.5 ND, zero signals (below the floor of three)"
  - "Steps 6.5 and 7 deferred to /fttcp and Role 1 (OR-30); pillar-relevant facts flagged in review"
plain_language_brief_included: true
analyst_note: "Growth is real at PBT (CON core PBT +44.74%, other income immaterial), with three bear counters. (1) The Rs 8.17 Cr of revenue booked outside the parent came with a receivables build at least Rs 8.65 Cr above the parent's. (2) FY26 audited figures show goods moving both ways: the parent sold at least Rs 8.44 Cr to Danya and bought at least Rs 6.16 Cr from it. Owners' PAT equals SA PAT in all four periods, so no unrealised profit was eliminated; FY26 CON profit could carry up to about Rs 1.62 Cr pre-tax (INFERENCE, parent gross margin as transfer-margin proxy). H1FY27 is not inflated (Danya stock +Rs 0.48 Cr). (3) The 23.6% spot ROCE excludes Rs 84.59 Cr of trade payables; 16.8% with them. Margin is read on consolidated. H2FY26 is an unassured balancing column (A3-18), so HoH reads are weighted lower. FLAGS, not CAVEATS: negative CFO with near-zero cash, related-party subsidiary governance, unresolved archetype. Not REWORK: headline statements tie. A3-13 goes to A1. Spot ROCE must not feed Section 1B before the FTTCP verdict and archetype exist."
review_path: "runs/supremepwr-h1fy27/work/review_supremepwr_h1fy27.md"
```
