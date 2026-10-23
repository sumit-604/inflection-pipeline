# AYE FINANCE LIMITED (AYE): Q2 FY27 COMPLETE QUARTERLY REVIEW (A4 ANALYST)

Quarter: Q2 FY27 (quarter ended 30-Sep-2026). Run type: FULL QUARTER (results filing + investor presentation + earnings call).
Protocols applied: Role 4 Quarterly Results Review v1.4 (lender variant, Steps 1L/5L) and Role 5 Quarterly Concall Analysis v1.1 (lender variant, Step 2L). Master, FTTCP and Section 1B not loaded. Role 4 Steps 6.5 and 7 and Role 5 Step 8D are DEFERRED to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts are flagged in place.
Model: claude-opus-5-5. Run date 2026-10-23.

**Correction loop 1 applied (A5 ADV-1..3).** Grafted: ADV-1 (Step 2 Core PBT row and 4A), ADV-2 (5L lender question 4, watchlist item 8, Q33), ADV-3 (3A opex row, 3B sensitivity and every dependent credibility line). A5 style notes ST-1 to ST-5 applied as well. Changes to figures and statuses: the restated credibility sensitivity (range now A to D); the ST-5 rounding (H2 post-tax RoA 3.07% → 3.08%); watchlist item 8 status (GREEN → GREEN on the trigger / AMBER on the second reading); and the resulting 6B tally (5 GREEN / 2 split → 4 GREEN / 3 split). Protocol verdict, protocol-output grade (70%, B) and position are unchanged.

**Correction loop 2 applied (A5 R1-1, R1-2, R1-S1, R1-S4)** (operator approved 2026-10-24). Preamble ledger counts updated to the corrected A2 ledgers (results M01-M07; presentation M01-M02). M06 and M07 marked reviewed. Loop-1 change log completed (R1-S1). 8E sensitivity wording corrected (R1-S4). No figure changed.

Anchor key (every number carries one):
- `R:R###` / `R:L###` = results structured row / results fulltext line (aye-results-q2fy27-*.md)
- `P:R###` / `P:L###` = presentation structured row / presentation fulltext line
- `C:R###` / `C:L###` = concall structured row / concall fulltext line (machine ASR transcript)
- `A3-##`, `A3P-##`, `A3C-##` = A3 forensic finding IDs; `A4-##` = finding raised in this review (Section C); `A5 ADV-#` = A5 adversary bear counter grafted in correction loop 1
- `[N Lx]` = Notion thesis page (live fetch 2026-10-23, work/notion_thesis_AYE.md, line x); `[S Lx]` = signal context file
- `[A4 calc]` = arithmetic on anchored numbers, shown inline; `[INFERENCE]` = interpretation with stated assumption
- `ND` = not disclosed in any passed document. Nothing is estimated.

Source cautions carried from the run log and A3:
- The concall source is a MACHINE (ASR) transcript (C:R322-R328). Speakers are not separated. Three load-bearing answers fall in audio gaps (A3C-20): overlay amount (C:L413-414), 50 bp rate scenario (C:L729-732), credit-life answer (C:L846-849). Every ASR number is a cross-check item. Filed numbers win.
- Pipeline error respected: presentation R076/R077 labels are swapped. 1,219 is Q1 FY27 disbursement and 1,275 is Q2 FY26 (proof: H1 FY27 2,622 = 1,219 + 1,403, P:L206; A3P pipeline note 1). This review uses the corrected labels.
- Pipeline error respected: concall R149 "10.60 percent" is a funding-cost figure, not a lending rate (A3C pipeline note 1). Not used as a yield.
- Pipeline error respected: results A2 ledger line 28 is wrong. The auditor signed the security cover report at 11:09:12 (R:L980), before the 11:15 board start (R:L43). See A3-18.
- A1 omitted presentation fulltext line 667 ("83 308 6,865", the 30-Jun Stage 2, Stage 3 and total gross loans) and line 807. This review read P:L660-681 directly and uses the printed values. The printed 30-Jun total ECL is 287 (P:L668), one crore above A3P-05's implied 286.

---

## LEDGER RECONCILIATION PREAMBLE (contract addition 1)

Ledger contains 12 notes / 26 turns / 44 slides. All 12 notes, 26 turns and 44 slides reviewed. Findings incorporated: A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, A3-18, A3-19, A3-20, A3-21, A3-22, A3-23, A3-24, A3-25, A3-26, A3-27, A3P-01, A3P-02, A3P-03, A3P-04, A3P-05, A3P-06, A3P-07, A3P-08, A3P-09, A3P-10, A3P-11, A3P-12, A3P-13, A3P-14, A3P-15, A3P-16, A3P-17, A3P-18, A3P-19, A3P-20, A3C-01, A3C-02, A3C-03, A3C-04, A3C-05, A3C-06, A3C-07, A3C-08, A3C-09, A3C-10, A3C-11, A3C-12, A3C-13, A3C-14, A3C-15, A3C-16, A3C-17, A3C-18, A3C-19, A3C-20.

| Ledger | Unit counted | Count | Structured IDs behind it | Reviewed | Orphans |
|---|---|---|---|---|---|
| Results (ledger_results) | numbered notes (plus 4 unnumbered notes R704, R708, R715, R737) | 12 (+4) | R001-R755 (755 rows) + M01-M07 signature lines | all 755 + 7 | 0 |
| Presentation (ledger_presentation) | slides (38 with rows + 6 dividers) | 44 | R001-R913 (913 rows) + M01-M02 (P:L667, P:L807) | all 913 + 2 | 0 |
| Concall (ledger_concall) | speaker turns T1-T26 (10 Q&A pairs + 6 framing turns); 10 questions | 26 | R001-R346 (346 rows) + M1-M7 | all 346 + 7 | 0 |

No ledger row is unreviewed. A4 adds four findings of its own (A4-01 to A4-04, Section C).

Results signature rows added by A2 in the loop (R1-2):
- M06 (R:L980, auditor security-cover report signature 21-10-2026 11:09:12): reviewed via A3-18; precedes the 11:15 board start and the 11:21 approval.
- M07 (R:L1438, CS cover-letter signature 21-10-2026 11:39:14): reviewed, no finding; after the 11:21 approval; CS-signing pattern carried in A3-16.

Presentation rows M01 (P:L667: 83 / 308 / 6,865, 30-Jun Stage 2, Stage 3 and total gross loans) and M02 (P:L807: 0, 10+ year cohort potential capacity) were read directly at the fulltext and are used in Steps 1L, 4C and 5L.

Slides reviewed with no finding and no row-level cite in this review (ST-4): slide 1 (cover letter), 2 (title), 4 (index), 9 and 10 (H1 restatements of cited Q2 rows), 16 (customer profile), 29 (collection tiers), 39 (scrambled balance-sheet summary; the filed balance sheet is used instead), 41 (shareholding; cited only through A3P-12), 42 (CSR), 43 (glossary). The six divider slides (5, 11, 20, 23, 30, 37) carry no rows.

---

# SECTION A: RESULTS REVIEW (ROLE 4, LENDER VARIANT)

## STEP 0: PRE-FLIGHT

### 0A. Notion baseline (live fetch 2026-10-23)

| Item | Notion value |
|---|---|
| Decision Status (VERIFIED before any framing) | **HELD**. Position 4% at avg cost Rs132, bought 2026-07-23 (operator override above the Small 2-3% rule) [N L4 properties; N L12] |
| One-line thesis | "Recovering micro-enterprise NBFC priced at fair value: the asset-quality and returns recovery is real and documented, but at CMP Rs 183 the market already carries it. Accumulated at the MoS floor." [N L16] |
| Entry zone | Entry Price Max Rs148, MoS Rs118, Base 3-yr FV Rs288 (revised 11-Aug from Rs166/Rs133/Rs324) [N L4; N L237-240] |
| CMP on page | Rs162 (screener.in, 13-Oct-2026) [N L412]. **STALE: 10 days old and pre-results.** No CMP-based valuation is computed in this review. |
| Destination PE / pillars | 15x forward destination PE by FY29 (operator 2026-07-22); Pillar 2L Asset-Quality Multiplier 1.00x; Pillar 3 +3x to +4x; Strategic +0x; UA N/A until Feb 2027; Sector cap 18x [N L52, L224-230] |
| Bear/Base/Bull | FY26-defined bands for AUM, PAT, NIM, credit cost, RoA, GNPA, CRAR, CE [N L171-180]; FY29 EPS Bear Rs15.75 / Base Rs19.20 / Bull Rs22.10 [N L235] |
| Thesis-broken triggers | Six bullets [N L43-48]; Step 6C |
| Monitoring checklist | Eight items [N L186-195]; Step 6B |
| Q2 add-gate | Raise above 4% only if ALL FOUR: (i) gross slippage disclosed and consistent with ~3.68% ex-overlay credit cost; (ii) PCR >= 60%; (iii) refined FY27 guidance; (iv) no upward drift in the 4 unwaived covenant instances [N L244-249] |
| Single cleanest Q2 metric (pre-committed) | Gross quarterly slippage. Bull: disclosed <= 3.68% of AUM. Bear: disclosed > 4.5% OR **not disclosed for a third consecutive event** [N L253-256] |
| Devil's Advocate | WEAKENED BUT ALIVE [N L209] |
| Promoter Verdict / Management Grade | TRUSTWORTHY (no identifiable promoter; management/board basis) / Grade C [N L220] |
| Operator rulings pending | Bucket 1 CE as a named tripwire; disbursement growth as a leading indicator for the AUM trigger [N L385-386] |

### 0B. Units
All filing figures are in Rs crores ("All amounts are in Rs. crores unless otherwise stated", R:R701, R:L208). Conversion factor x1. EPS in Rs. Deck figures are Rs crore, rounded (P:R735).

### 0C. Share-count changes
- IPO listed 16-Feb-2026 (R:R638). Fresh issue 5,50,38,759 shares at Rs129 (R:R380, R:R381). Net proceeds Rs672.24 cr fully used by 30-Sep-2026 (R:R386).
- H1 FY27: the Employee Welfare Trust transferred 5,04,152 shares on ESOP exercise; 3,913 new shares were allotted (R:R392, R:R393). Paid-up capital 48.90 to 49.02 (R:R065, R:R064).
- No split, bonus, buyback or rights issue. Q2 FY26 EPS uses the pre-IPO share count, so YoY EPS growth (+96.6% diluted) runs below YoY PAT growth (+151.1%).
- Open item A3-10: the weighted basic share count implied by EPS (Q2: 86.72 / 3.51 = 24.71 cr; H1: 161.22 / 6.53 = 24.69 cr) exceeds the 24.51 cr shares implied by paid-up capital (49.02 / Rs2). Possible treasury-share treatment of Trust holdings. QfM Q31.

### 0D. Notes extraction (12 numbered notes + 4 unnumbered)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 | Regulatory category | Aye Finance is an NBFC-ML registered with RBI (R:R711, R:L478). | 0 | n/a | None. Lender variant applies. |
| 2 | Review and auditor | Limited review by M S K A & Associates, unmodified; Q1 FY27, Q2 FY26, H1 FY26 reviewed and FY26 audited by S S Kothari Mehta & Co. LLP (R:R712, R:L481-488). | 0 | All comparatives | **Auditor changed SSKM to MSKA.** Comparatives rest on the predecessor's work (A3-24). |
| 3 | Basis of preparation | Reg 33/52 and Ind AS; RBI directions implemented "as and when they are issued/applicable" (R:R713, R:R615). | 0 | n/a | None (carried verbatim from Q1, A3 F7). |
| 4 | Resolution framework (OTR) | Restructured exposure 0.04 at 31-Mar-26; 0.01 repaid; 0.02 standard at 30-Sep-26 (R:R350, R:R353, R:R354). The Aug-2020 circular is mislabelled "2.0" (A3-20). | 0.02 | H1 FY27 | None. Immaterial run-off book. |
| 5 | Transfers of loan exposures | Rs39.95 cr of standard loans assigned in H1, all in Q2 (Q1 derecognition gain nil by cross-foot, A3 s.1); MRR 10%; tangible security 0%; unrated (R:R355, R:R356, R:R359). No loans acquired; no stressed loans transferred (R:R718-R720). Arcil SRs in four trusts, RR1-RR2 (R:R372-R375). **New section (d): co-lending, 2 partners, 39,096 cases, Rs53.31 cr, 31.27% rate, NPL 10.61, nil fees** (R:R363-R371). | DA gain 10.12 in Q2 P&L (R:R084) | Q2 FY27 | **Breaks QoQ comparability: Q2 PBT includes a 10.12 DA gain; Q1 had none.** Co-lending NPL 10.61 / 53.31 = 19.9% (A3-12). |
| 6 | Segment | No separate reportable segment under Ind AS 108 (R:R721). | 0 | n/a | No segment walk. State and product asset quality come only from the deck and call. |
| 7 | FAME | 100%-owned Section 8 company not consolidated; rationale rewritten to the Section 8 bar on returns (R:R722, A3-26). | 0 | n/a | No consolidated statement exists (see S-vs-C below). |
| 8 | NCD security | Listed secured NCDs carry a first exclusive charge on book debts of at least 100% (R:R723). | 0 | n/a | Cover printed "1.1"; computed 1.091x (A3-15). |
| 9 | Reg 52(4) | Ratios attached as Annexure I (R:R724). | 0 | H1 FY27 | Source of GNPA 4.20%, NNPA 1.62%, PCR 62.42%, CRAR 41.01%, LCR 404.31% (R:R402-R406). |
| 10 | IPO proceeds | Net Rs672.24 cr fully used; Rs22.63 cr of offer expenses "unutilised" (R:R725, R:R391). | 22.63 balance | H1 FY27 | Basis changed from "incurred" (Q1) to "unutilised" (A3-19). |
| 11 | ESOP | Trust transferred 5,04,152 shares; 3,913 allotted (R:R726). | +0.12 capital | H1 FY27 | Share count; see 0C and A3-10. |
| 12 | Regrouping | Prior figures regrouped or reclassified where necessary (R:R727). | ND | Q2 FY26 | Deck says Q2 FY26 reclassified (P:R734). Deck restates Q1 FY27 ratios with no note (A3P-18). |
| unnumbered | EPS | Interim EPS not annualised (R:R704). | 0 | all | Annualise where used. |
| unnumbered | Cash flow | Indirect method, Ind AS 7 (R:R708). | 0 | H1 | None. |
| unnumbered | OTR footnotes | Overdue principal and OTR 2.0 scope (R:R715, R:R716). | 0 | n/a | None. |
| unnumbered | Reg 52(4) | DSCR, ISCR etc. not applicable (R:R737). | 0 | n/a | None. |

Answers to the four note questions:
- Notes that change a comparison: Note 5 (DA restarted in Q2) and Note 2 (auditor change). Note 12 and the deck restatements (A3P-18) move the Q1 base by 1 to 2 bps on ratios; immaterial.
- Normalisation needed: YES. Q2 PBT is shown with and without the 10.12 DA gain (Step 4). Q2 FY26 is shown with and without its FV gain (29.12) and FV loss (18.66).
- Recurring vs one-off: the DA gain is discretionary and lumpy: 16.28 in Q2 FY26, nil in Q1 FY27, 10.12 in Q2 FY27 (R:R085, R:R089, R:R084).
- Thesis assumption change: Note 5(d), the co-lending book at 19.9% NPL, is new. Note 2, the auditor change, sits beside the security-cover qualification below.

**Auditor opinion check.**
- Limited review report: conclusion UNMODIFIED, with two Other Matter paragraphs. The Employee Welfare Trust is unreviewed (Rs0.12 cr of Q2 PAT = 0.14%; Rs0.47 cr of H1 PAT = 0.29%; R:R696, R:R009, R:R010). Comparatives were reviewed by another auditor (R:R698). Not an Emphasis of Matter. No going-concern language (A3 F3).
- Security cover / covenant certificate (Reg 54(3)): conclusion QUALIFIED, "except for paragraph 12" (R:R740, R:L950). Paragraph 12: "in respect of ISIN INE501X07588, the Company is in breach of the required financial covenant of (PAR 90 + Write off)/Gross Loan Portfolio" (R:R739, R:L932). Second quarter running. The Q1 auditor reported it in an annexure; the new auditor moved it into the body and qualified (A3-03). Annexure 3 reason: "Increase in write-offs in this financial year due to higher delinquencies, industry wide stress in Miro Business Loans and MFI Loans, requisite waiver received." (R:R749, R:L1279).
- **AMBER flag** under the protocol rule for a modified conclusion. It is a covenant certificate, not the financial statements, so the numbers stay usable.

### 0E. Business type
LENDING BUSINESS (NBFC-ML, micro-enterprise lender). Steps 1L and 5L replace Steps 1 and 5.

### Standalone vs consolidated (first-class metric, A3 F2)
The filing carries ONE set of results: the Company plus the Aye Employee Welfare Trust (LRR para 5, R:L155). No consolidated results are filed. FAME is not consolidated (Note 7, R:R722). The standalone-vs-consolidated PAT gap is NOT APPLICABLE. The nearest equivalent is the unreviewed Trust inside the statement:

| Period | Reported PAT | Trust PAT inside it | Trust share | Consolidated PAT |
|---|---|---|---|---|
| Q2 FY27 | 86.72 (R:R180) | 0.12 (R:R009) | 0.14% [A4 calc 0.12/86.72] | ND (none filed) |
| H1 FY27 | 161.22 (R:R183) | 0.47 (R:R010) | 0.29% [A4 calc 0.47/161.22] | ND (none filed) |
| Q1 FY27 | 74.50 (R:R181) | ND (Q1 LRR had no such paragraph, A3-04) | ND | ND (none filed) |

---

## STEP 1L: DATA EXTRACTION TABLE (LENDER)

All Rs crore. "Other/Fee income (net)" = fees and commission + net gain on derecognition + net gain on fair value changes + other income − net loss on fair value changes. This matches the deck's "Fee & Other Income" line, which nets the FV loss, in four columns (deck Q2 FY27 48, Q1 37, H1 85, H1 FY26 98; P:R678, P:R681, P:R683, P:R684). For Q2 FY26 the deck prints 56 (P:L876) against 55.18 on the filed basis; the deck figure is reclassified (P:L887), a 1-crore gap (ST-2). Opex = employee + D&A + other expenses (deck 184 / 180 / 166; P:R699-R701).

| Line Item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 (extra) | H1 FY27 (extra) |
|---|---|---|---|---|---|---|---|
| Interest Income | 371.39 (R:R074) | 452.67 (R:R073) | 479.26 (R:R072) | 1,549.13 (R:R077) | ND (year not complete) | 730.67 (R:R076) | 931.93 (R:R075) |
| Interest Expense (finance cost) | 132.53 (R:R116) | 130.61 (R:R115) | 144.68 (R:R114) | 534.07 (R:R119) | ND | 258.86 (R:R118) | 275.29 (R:R117) |
| Net Interest Income (NII) | 238.86 [371.39 − 132.53] | 322.06 [452.67 − 130.61] | 334.58 [479.26 − 144.68] | 1,015.06 [1,549.13 − 534.07] | ND | 471.81 [730.67 − 258.86] | 656.64 [931.93 − 275.29] |
| of which: fees & commission | 18.10 (R:R080) | 19.56 (R:R079) | 20.51 (R:R078) | 73.54 (R:R083) | ND | 32.69 (R:R082) | 40.07 (R:R081) |
| of which: net gain on derecognition (DA) | 16.28 (R:R085) | 0.00 (R:R089 blank; nil by cross-foot 452.67 + 19.56 + 5.14 = 477.37 = R:R097) | 10.12 (R:R084) | 67.97 (R:R088) | ND | 29.32 (R:R087) | 10.12 (R:R086) |
| of which: net gain on FV changes | 29.12 (R:R092) | 5.14 (R:R091) | 4.50 (R:R090) | 105.79 (R:R095) | ND | 47.67 (R:R094) | 9.64 (R:R093) |
| of which: other income | 10.34 (R:R104) | 12.29 (R:R103) | 12.73 (R:R102) | 48.51 (R:R107) | ND | 19.51 (R:R106) | 25.02 (R:R105) |
| less: net loss on FV changes | 18.66 (R:R122) | 0.00 (R:R121, dash) | 0.00 (R:R120, dash) | 66.77 (R:R125) | ND | 30.75 (R:R124) | 0.00 (R:R123, dash) |
| Other/Fee Income (net) | 55.18 [A4 calc] | 36.99 [A4 calc] | 47.86 [A4 calc] | 229.04 [A4 calc] | ND | 98.44 [A4 calc] | 84.85 [A4 calc] |
| Operating Expenses | 166.13 [119.61 R:R134 + 6.24 R:R140 + 40.28 R:R146] | 180.49 [138.64 R:R133 + 6.17 R:R139 + 35.68 R:R145] | 184.74 [135.74 R:R132 + 6.43 R:R138 + 42.57 R:R144] | 661.07 [480.44 + 26.31 + 154.32; R:R137, R:R143, R:R149] | ND | 314.74 [233.41 + 11.34 + 69.99] | 365.23 [274.38 + 12.60 + 78.25; R:R135, R:R141, R:R147] |
| PPOP | 127.91 [A4 calc] | 178.56 [A4 calc] | 197.70 [A4 calc] | 583.03 [A4 calc] | ND | 255.51 [A4 calc] | 376.26 [A4 calc] |
| Provisions & Write-offs (impairment on financial instruments) | 86.22 (R:R128) | 81.41 (R:R127) | 81.90 (R:R126) | 335.73 (R:R131) | ND | 172.93 (R:R130) | 163.31 (R:R129) |
| PBT | 41.69 (R:R158) | 97.15 (R:R157) | 115.80 (R:R156) | 247.30 (R:R161) | ND | 82.58 (R:R160) | 212.95 (R:R159) |
| Tax | 7.16 (R:R176) | 22.65 (R:R175) | 29.08 (R:R174) | 53.67 (R:R179) | ND | 17.46 (R:R178) | 51.73 (R:R177) |
| PAT | 34.53 (R:R182) | 74.50 (R:R181) | 86.72 (R:R180) | 193.63 (R:R185) | ND | 65.12 (R:R184) | 161.22 (R:R183) |
| EPS basic (reported, not annualised) | 1.80 (R:R224) | 3.02 (R:R223) | 3.51 (R:R222) | 9.73 (R:R227) | ND | 3.40 (R:R226) | 6.53 (R:R225) |
| EPS (share-adjusted = diluted; no split/bonus to adjust) | 1.77 (R:R230) | 3.00 (R:R229) | 3.48 (R:R228) | 9.60 (R:R233) | ND | 3.34 (R:R232) | 6.49 (R:R231) |

Tie-outs: PPOP − impairment = PBT in every column (Q2 FY27: 197.70 − 81.90 = 115.80; Q1: 178.56 − 81.41 = 97.15; Q2 FY26: 127.91 − 86.22 = 41.69; FY26: 583.03 − 335.73 = 247.30; H1 FY27: 376.26 − 163.31 = 212.95). Deck PPOP 198 / 179 / 128 ties (P:R704-R706). Deck H1 PPOP prints 377 (P:R707) against 376.26 computed; the gap is rounding of 198 + 179.

**Derived lender metrics**

| Derived Metric | Formula / Source | Q2 FY26 | Q1 FY27 | Q2 FY27 |
|---|---|---|---|---|
| NIM (on ATA, disclosed) | deck ROE tree | 13.87% (P:R811) | 15.94% (P:R792, as printed) | 15.59% (P:R810) |
| Cost-to-Income | Opex / (NII + Other net) | 56.50% [166.13/294.04]; deck 56.5% (P:R103) | 50.27% [180.49/359.05]; deck 50.3% (P:R104) | 48.31% [184.74/382.44]; deck 48.3% (P:R105) |
| Credit Cost annualised, disclosed on ATA | deck | 5.00% (P:R387) | 4.03% (P:R388; restated from 4.01%, A3P-18) | 3.82% (P:R389) |
| Credit Cost annualised, protocol basis (provisions / avg AUM) | [A4 calc] | ND (30-Jun-25 AUM not in corpus) | 4.53% [81.41 × 4 / avg(7,044 FY26 AUM [N L4; P:R209]; 7,324 P:R073) = 325.64/7,184] | 4.39% [81.90 × 4 / avg(7,324; 7,597 P:R074) = 327.60/7,460.5] |
| GNPA % / NNPA % | as disclosed | 4.9% / 1.8% (P:R109, P:R112, chart); table basis 272/5,615 = 4.84% (P:L672-674) | 4.49% (P:L667: 308/6,865) [N L188] / 1.7% (P:R113, chart) | 4.20% (R:R402) / 1.62% (R:R403) |
| PCR % (Stage 3 ECL / GS3) | as disclosed | 64.47% (P:R554) | 63.80% filed Q1 (A3-11); 63.84% restated (P:R538) | 62.42% (R:R404) |
| Collection Efficiency % (Non-OD / Bucket 1) | as disclosed | 98.9% / 48.4% (P:R390, P:R393) | 99.2% / 54.5% (P:R391, P:R394) | 99.2% / 52.8% (P:R392, P:R395) |
| AUM / Loan Book (Rs Cr) | as disclosed | AUM 6,028 (P:R072); gross loans 5,615 (P:L672) | AUM 7,324 (P:R073); gross loans 6,865 (P:L667) | AUM 7,597 (P:R074); gross loans 7,119 (P:R516); BS net loans 6,849.85 (R:R020) |
| Disbursements (Rs Cr) | as disclosed (labels corrected) | 1,275 (P:R077 relabelled, A3P err 1) | 1,219 (P:R076 relabelled) | 1,403 (P:R078) |
| RoA (annualised) | disclosed PAT / avg total assets | 2.00% (P:R847) | 3.69% (P:R818; restated from 3.71%) | 4.04% (P:R846) |
| RoE (annualised) | disclosed | 8.08% (P:R855) | 11.60% (P:R840) | 13.09% (P:R854) |
| CRAR % | as disclosed | ND (deck chart carries March dates only, P:R369-R372, P:R377) | 42.4% (prior deck L456, via A3P F11) | 41.01% (R:R405) |

Note on the two credit-cost bases (A4-02). The disclosed 3.82% is on average total assets. Those assets include Rs1,341.66 cr of cash and bank balances at 30-Sep (R:R014 851.21 + R:R016 490.45 = 15.3% of total assets 8,773.51, R:R044). In rupees the charge was flat QoQ (81.41 to 81.90, +0.6%). The "21 bps improvement" is a denominator effect. On average AUM, Q2 is 4.39%, 14 bps better than Q1's 4.53%. The guidance is set on the ATA basis (C:R331-R332, P:R655), so the band test uses ATA. The AUM basis is shown for honesty.

▶ Checkpoint: every cell filled or ND.

---

## STEP 2: Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26), lender substitution

"Core PBT" for this lender = PBT − DA gain − FV gain + FV loss (treasury and assignment items removed; FD interest in other income kept as recurring carry). Q2 FY26: 41.69 − 16.28 − 29.12 + 18.66 = 14.95. Q2 FY27: 115.80 − 10.12 − 4.50 + 0 = 101.18. Q1 FY27: 97.15 − 0 − 5.14 + 0 = 92.01.

| Metric | Q2 FY26 | Q2 FY27 | YoY % Change | Verdict |
|---|---|---|---|---|
| NII (revenue substitute) | 238.86 | 334.58 | +40.1% [334.58/238.86] | Strong. Above AUM growth (+26.0%) on NIM expansion 13.87% to 15.59% |
| PPOP (Op EBITDA substitute) | 127.91 | 197.70 | +54.6% [197.70/127.91] | Strong |
| PPOP / net income (pp) | 43.5% [127.91/294.04] | 51.7% [197.70/382.44] | +820 bps | Strong; opex leverage |
| D&A | 6.24 (R:R140) | 6.43 (R:R138) | +3.0% | Flat; no branch capex |
| Finance costs | 132.53 | 144.68 | +9.2% | Far below interest-income growth (+29.0%); IPO equity cut leverage from 4.03x to 3.24x (P:R853, P:R852) |
| Credit cost (impairment, Rs) | 86.22 | 81.90 | −5.0% | Lower in rupees on a gross book 26.8% larger (5,615 to 7,119) |
| Credit cost ratio (ATA) | 5.00% | 3.82% | −118 bps (deck −119 bps on unrounded, P:R845) | Improved |
| GNPA | 4.84% table / 4.9% chart | 4.20% | −64 bps (table) / −70 bps (chart; C:R042) | Improved |
| Other/Fee income (net) | 55.18 | 47.86 | −13.3% | Weaker: FV gain 29.12 to 4.50; DA 16.28 to 10.12 |
| **Core PBT (ex DA, ex FV)** | **14.95** | **101.18** | **+576.8% [101.18/14.95]** | YoY recovery is real, but its size is base- and capital-driven (A5 ADV-1 bear counter below). The repeatable signal is QoQ core PBT +10.0% |
| Reported PBT | 41.69 | 115.80 | +177.8% | |
| PAT | 34.53 | 86.72 | +151.1% | |
| EPS diluted (share-adjusted) | 1.77 | 3.48 | +96.6% | Below PAT growth because of Feb-26 IPO dilution |

Diagnostic answers:
1. **Did NII grow YoY?** Yes, +40.1%. AUM grew 26.03% YoY (P:R642), inside the FY27 guide of 25-30% (P:R652). Notion base NIM is 14.5% [N L175]; actual 15.59%, so NII runs above base.
2. **PPOP margin.** Q2 FY27 PPOP/net income 51.7% vs Q2 FY26 43.5% = +820 bps YoY. Sequential Q1 FY27 49.7% [178.56/359.05] to 51.7% = +200 bps.
3. **Core PBT.** +576.8% YoY (14.95 to 101.18). Reported PBT grew less (+177.8%) because Q2 FY26 carried large treasury items. YoY, the headline understates core growth, but the multiple runs off a stress-trough base (see the bear counter below). **QoQ the reverse holds:** core PBT +10.0% (92.01 to 101.18) against reported PBT +19.2%. The QoQ headline is inflated by the DA gain (Step 4B).
4. **Gap drivers YoY.** Other income −7.32 (FV gain −24.62, FV loss swing +18.66, DA −6.16, fees +2.41, other income +2.39). Finance cost +12.15 sits inside NII. Tax rate 17.17% [7.16/41.69] to 25.11% [29.08/115.80] cost 9.19 [115.80 × (25.11% − 17.17%)]. No exceptional items.
5. **D&A and finance costs vs revenue.** D&A +3.0% and finance cost +9.2% vs NII +40.1% and interest income +29.0%. No absorption deficit YoY. QoQ differs: finance cost +10.8% vs interest income +5.9% (A3-14), the first sign of negative carry on the liquidity build.
6. **Other income concentration.** FY26 net other/fee income 229.04 included DA 67.97 and FV gain 105.79 (R:R088, R:R095). H1 FY27 is 84.85 with DA 10.12 and FV 9.64. Treasury and assignment items are a smaller share now. The Q2 DA restart is lumpy (16.28 / nil / 10.12 over the last three reported quarters). Stripped of DA and FV, Q2 FY27 other income is 33.24 [20.51 + 12.73] vs Q2 FY26 28.44 [18.10 + 10.34], +16.9%.

**Bear counter (A5 ADV-1, grafted in correction loop 1).**
- **Trough base.** The YoY core multiple runs off the FY26 stress trough. Q2 FY26 core PBT of 14.95 is the lowest print in the Step 3 series (Q1 FY26 21.39; H2 FY26 per-quarter average 51.99). Credit cost that quarter was 5.00% (P:R387), in the period the filing calls "industry wide stress" (R:R749). +576.8% is a recovery-from-trough multiple, not a run-rate.
- **Funding mix.** About Rs14 cr a quarter of the YoY gain comes from the post-IPO funding mix. Finance cost on ATA fell 95 bps, 7.69% to 6.74% (P:R798, P:R797), against blended CoB down only 41 bps, 11.04% to 10.63% (P:L509). The residual (~67 bps of ATA) is a lower debt share of assets after the Feb-26 IPO (leverage 4.03x to 3.24x). [INFERENCE, A5: 10.63% × (7.69/11.04 − 6.74/10.63) × 8,576 / 4 = 14.2, roughly 19% of the 74.11 YoY PBT rise.] Management plans to re-lever to 4-4.5x (C:L272-274), which unwinds this part of NIM. The FY27 NIM guide of 14.25-14.75% (P:R653) already assumes it.
- **ECL draw inside "recurring".** The 4A recurring pool includes the ~13 Q2 ECL draw isolated in 4C. Without it, recurring is ~73.2 [86.23 − 13.0], about 99% of the PBT change (not 116%).
- **Net:** the YoY recovery is real; its size is base- and capital-driven. The repeatable signal is QoQ core PBT +10.0%.

▶ Checkpoint passed.

---

## STEP 3: SEQUENTIAL QoQ TRAJECTORY

The filing gives Q2 FY26, Q1 FY27, Q2 FY27, H1 FY26, H1 FY27 and FY26. Q1 FY26 = H1 FY26 − Q2 FY26. H2 FY26 = FY26 − H1 FY26 (a two-quarter block; Q3 and Q4 FY26 are not separable from the filing).

| Quarter | NII (Rs Cr) | PPOP / net income | Core PBT (ex DA, ex FV) | One-offs flagged | QoQ run-rate (NII) |
|---|---|---|---|---|---|
| Q1 FY26 | 232.95 [471.81 − 238.86] | 46.2% [127.60/276.21] | 21.39 [40.89 − 13.04 − 18.55 + 12.09] | DA 13.04; FV gain 18.55; FV loss 12.09 [H1 FY26 minus Q2 FY26 rows] | base |
| Q2 FY26 | 238.86 | 43.5% | 14.95 | DA 16.28; FV gain 29.12; FV loss 18.66 | +2.5% |
| H2 FY26 (2 qtrs) | 543.25 [1,015.06 − 471.81]; per-qtr avg 271.63 | 48.6% [327.52/673.85] | 103.97 for 2 qtrs [164.72 − 38.65 − 58.12 + 36.02]; per-qtr avg 51.99 | DA 38.65; FV gain 58.12; FV loss 36.02. Memo: Notion records Q4 FY26 PAT Rs86 cr [N L4 Key Notes], so Q3 FY26 PAT ≈ 42.5 [H2 PAT 128.51 − 86] | +13.7% (per-qtr avg vs Q2 FY26) |
| Q1 FY27 | 322.06 | 49.7% [178.56/359.05] | 92.01 | DA nil; overlay build ~Rs6 cr per Q1 call [N L83]; ECL stock +12.45 [A4-03, INFERENCE] | +18.6% vs H2 FY26 per-qtr avg |
| Q2 FY27 | 334.58 | 51.7% | 101.18 | DA 10.12 (R:R084); ECL stock −13 (287 P:L668 to 274 P:L663) | +3.9% |

Diagnostics:
- **Trajectory: STEPPING UP, DECELERATING.** NII per quarter 232.95 → 238.86 → ~271.6 → 322.06 → 334.58. The big step came with the Feb-26 IPO equity. Q2 adds only +3.9% QoQ, in line with AUM +3.7% QoQ (7,324 to 7,597) and gross loans +3.7% (6,865 to 7,119).
- **Distortions:** every FY26 quarter carries treasury FV swings. Q2 FY27 carries the DA gain. Q1 and Q2 FY27 carry an ECL build then an ECL fall of similar size (Step 4C).
- **Latest vs H1 average:** Q2 NII 334.58 vs H1 average 328.32 [656.64/2]: above. Q2 core PBT 101.18 vs H1 average 96.60 [(92.01 + 101.18)/2]: above. Q2 PAT 86.72 vs H1 average 80.61: above.
- **Capacity-commissioning analogue:** zero branches opened in H1 FY27 (P:R627, P:R628; C:L767-768). The 30+ branches due in Q3 (C:R030, C:R246) are the new capacity. Test for Q3/Q4: disbursement must step above Q2's 1,403 by more than the seasonal H2 lift, or the new branches carry cost without volume.
- **Implied Q3 base to hold trajectory:** NII ≥ 334.58; core PBT ≥ 101.18; impairment ≤ 81.90 with total ECL cover not below 3.85% (P:R528). Management's "~3.5% FY27 credit cost" (C:R147) needs much more than this (Step 8C).

---

## STEP 4: OPERATIONAL DECOMPOSITION (LENDER BRIDGE)

### 4A. YoY bridge, Q2 FY26 → Q2 FY27 (PAT +52.19)

| Component | YoY change (Rs Cr) | Share of PBT change (+74.11) | Recurring? |
|---|---|---|---|
| NII change | +95.72 [334.58 − 238.86] (interest income +107.87; finance cost +12.15) | 129.2% | Recurring |
| Fees & commission | +2.41 [20.51 − 18.10] | 3.3% | Recurring |
| Other income (FD interest etc.) | +2.39 [12.73 − 10.34] | 3.2% | Recurring |
| DA (derecognition) gain | −6.16 [10.12 − 16.28] | −8.3% | NON-RECURRING (discretionary) |
| FV gain | −24.62 [4.50 − 29.12] | −33.2% | NON-RECURRING |
| FV loss removed | +18.66 | +25.2% | NON-RECURRING (hedge accounting from FY27 sends derivative MTM to OCI, A3-01) |
| Opex change | −18.61 [184.74 − 166.13] | −25.1% | Recurring |
| Provision change: regular credit cost | +4.32 [86.22 − 81.90] | +5.8% | Recurring; one-off/accelerated split ND (overlay movement not disclosed; ASR gap C:L413-414) |
| Exceptional items | 0 | 0% | n/a |
| **PBT change** | **+74.11** | 100% | |
| Tax change | −21.92 (rate effect −9.19; volume effect −12.73) | | Mixed |
| **Reported PAT YoY change** | **+52.19 [86.72 − 34.53]** | | |

Recurring items (NII + fees + other income − opex + provisions) = +86.23 pre-tax. Non-recurring items net = −12.12 pre-tax. **The YoY PAT increase is 116% recurring on this classification.**

Footnote (A5 ADV-1, grafted in correction loop 1): the recurring provision line includes the ~13 Q2 ECL stock draw isolated in 4C. Moving it out leaves ~73.2 recurring [86.23 − 13.0], about 99% of the PBT change. About Rs14 cr a quarter of the NII gain is the post-IPO funding mix (finance cost on ATA −95 bps, P:R798, P:R797, against CoB −41 bps, P:L509) that the planned re-levering to 4-4.5x (C:L272-274) unwinds [INFERENCE, A5]. The base quarter (Q2 FY26 core 14.95; credit cost 5.00%, P:R387) is the FY26 stress trough. The "recurring" label holds; its size is base- and capital-driven.

### 4B. QoQ bridge, Q1 FY27 → Q2 FY27 (PAT +12.22): where the quality question sits

| Component | QoQ change (Rs Cr) | Share of PBT change (+18.65) | Recurring? |
|---|---|---|---|
| NII | +12.52 [334.58 − 322.06] (interest income +26.59; finance cost +14.07) | 67.1% | Recurring |
| DA gain | +10.12 [10.12 − 0] | **54.3%** | NON-RECURRING |
| Fees | +0.95 | 5.1% | Recurring |
| FV gain | −0.64 | −3.4% | Non-recurring |
| Other income | +0.44 | 2.4% | Recurring |
| Opex | −4.25 [184.74 − 180.49] | −22.8% | Recurring |
| Impairment | −0.49 [81.90 − 81.41] | −2.6% | Recurring |
| **PBT change** | **+18.65** | 100% | |
| Tax | −6.43 [29.08 − 22.65] | | |
| **PAT change** | **+12.22** | | |

The DA gain after tax is 7.57 [10.12 × (1 − 25.17%)], **62.0% of the QoQ PAT rise** (A3-13, A3P-07, A3C-02). Management attributed the PAT rise to credit cost and opex only (C:L60-63, C:L189-196) and never named DA on the call (A3C-18).

### 4C. Provision line split (A4-03: write-offs vs net ECL movement)

H1 identity, exact from the filed cash flow: P&L impairment 163.31 (R:R129) = loans written off 155.56 (R:R256) + loss on settlement 8.30 (R:R258) + net change in ECL allowance (0.55) (R:R250). [155.56 + 8.30 − 0.55 = 163.31.] **In H1 the whole credit charge equals realised losses. The ECL stock did not grow while net loans grew 9.3% (6,266.44 to 6,849.85, R:R021, R:R020).**

Quarter split [INFERENCE: applies the same identity to each quarter using the deck's ECL stock; Mar-26 ECL = 274 + 0.55 = 274.55 because the deck gives no March table]:

| Item | Q1 FY27 | Q2 FY27 | H1 FY27 |
|---|---|---|---|
| P&L impairment | 81.41 (R:R127) | 81.90 (R:R126) | 163.31 (R:R129) |
| Total ECL stock, start → end | 274.55 → 287 (P:L668, overlay-inclusive restated) | 287 → 274 (P:L668 → P:R520) | net −0.55 (R:R250) |
| Net ECL change | +12.45 | −13.00 | −0.55 |
| Write-offs + settlement losses (= impairment − ΔECL) | ≈ 68.96 | ≈ 94.90 | 163.86 (155.56 + 8.30, filed) |

Readings (both named; conservative lean):
- Q2 write-offs and settlements of ≈ 94.90 ran about 38% above Q1's ≈ 68.96 [INFERENCE]. The Q2 P&L charge stayed flat because new provisioning (81.90) fell short of write-offs (≈ 94.90), so the ECL stock shrank by 13.
- Holding the 30-Jun total cover of 4.17% (P:R539) on 30-Sep gross loans of 7,119 (P:R516) needs ECL of 296.9 [7,119 × 4.17%], or 22.9 more provision [296.9 − 274]. Post-tax that is 17.1 [22.9 × (1 − 25.17%)], **19.7% of Q2 PAT** [17.1/86.72] (A3P-05).
- DA gain (10.12) plus the ECL stock fall (13.0) = 23.12 pre-tax, above the whole QoQ PBT rise of 18.65. After tax 17.30 vs the PAT rise of 12.22 [INFERENCE]. **Q2's "highest ever quarterly profit" (P:R056) rests on these two items.**
- Bull counter-reading (also anchored): H1 FY27 write-offs + settlements of 163.86 are only +10.0% above H1 FY26's 148.95 [146.20 R:R257 + 2.75 R:R259], while gross loans grew 26.8% YoY (5,615 to 7,119). YoY, realised losses per rupee of book fell.
- What separates them: Q2 gross slippage (not disclosed) and the overlay balance at 30-Jun and 30-Sep (lost in the ASR gap at C:L413-414; the spoken "nearly 45 crores" does not tie to the ~12 cr implied by the restated table, A3C-01).

**Slippage proxy (A4-03, INFERENCE, NOT a disclosed figure).** Stage 3 gross went 308 (P:L667) → 299 (P:R515), −9. If the ≈ 94.90 of write-offs and settlements came out of Stage 3, gross additions to Stage 3 in Q2 were at least ≈ 86 [−9 + 94.90], before any upgrades or cash recoveries. Annualised ≈ 343.6: ≈ 4.6% of average AUM [343.6/7,460.5] and ≈ 4.9% of average on-book gross loans [343.6/6,992]. Both sit above the Notion bear line of 4.5% [N L256]. Assumptions: all write-offs and settlement losses are Stage 3 accounts; ECL table figures are rounded to Rs1 cr; the DA-sold standard loans (39.95 at 0.66% Stage 1 cover) move ECL by only ~0.26. This proxy is not the add-gate reading. The gate reads on disclosure (Step 6).

### 4D. Mandatory questions
- **Recurring vs non-recurring share of YoY PAT change:** 116% recurring (+86.23 pre-tax) against −12.12 non-recurring; ~99% if the Q2 ECL draw is moved out (A5 ADV-1). QoQ, 54.3% of the PBT rise is the non-recurring DA gain.
- **If other income reverts (DA to nil):** Q2 PAT ex-DA = 79.15 [86.72 − 7.57]; annualised 316.6. RoA ex-DA ≈ 3.69% [316.6 / implied ATA 8,586, where ATA = 86.72 × 4 / 4.04%, P:R846] vs reported 4.04% and the FY27 RoTA guide of 4.0-4.5% (P:R641). **Pillar 1 fact flagged (deferred, OR-30).**
- **D&A / finance cost steady state:** D&A flat (6.43). Finance cost will keep running ahead of interest income until the Rs1,341.66 cr liquidity is deployed. Liquidity rose 32.7% in H1 (1,011.07 to 1,341.66) while borrowings rose 16.8% (5,017.63 to 5,858.32; R:R046-R049) and net loans 9.3% (A3-14). H2 opex will step up with 30+ branches (C:R030) and 5-7% more staff (C:R119).
- **Tax adjustments:** deferred tax charge 2.15 in Q2 vs credit (4.55) in Q1 (R:R168, R:R169). Q1 ETR 23.31% was helped by the credit. Q2 ETR 25.11% ≈ statutory 25.17% (A3 F8). No persistent deferred-tax credit.

---

## STEP 5L: ASSET QUALITY & CAPITAL (LENDER)

| Metric | Prior period (Q1 FY27 / 30-Jun-26 unless stated) | Current period (Q2 FY27 / 30-Sep-26) | Change | Verdict |
|---|---|---|---|---|
| Credit cost (annualised) vs guided band 3.5-4.0% | 4.03% ATA (P:R388); 4.53% avg AUM [A4 calc] | 3.82% ATA (P:R389); 4.39% avg AUM [A4 calc]; H1 3.95% ATA (P:R401) | −21 bps ATA (denominator-driven; Rs charge +0.6%) | IN BAND on the guided (ATA) basis; release-assisted (Step 4C) |
| GNPA % | 4.49% (P:L667-668: 308/6,865) | 4.20% (R:R402) | −29 bps | GREEN on the trigger; GS3 Rs308 → Rs299 |
| NNPA % | 1.7% (P:R113, chart) | 1.62% (R:R403) | ≈ −8 bps | GREEN |
| PCR % | 63.80% filed (A3-11) / 63.84% restated (P:R538) | 62.42% (R:R404) | −138 bps (vs filed) | Above the 60% gate but falling. Total ECL cover 4.17% → 3.85% (P:R539, P:R528); Stage 2 cover 58.07% → 47.44% (P:R537, P:R526) |
| Collection efficiency % | Non-OD 99.2%; Bucket 1 54.5% (P:R391, P:R394) | Non-OD 99.2%; Bucket 1 52.8% (P:R392, P:R395) | Non-OD flat; Bucket 1 −1.7 pp, second quarterly fall (Q4 FY26 59.8% [N L313]) | AMBER |
| Restructured / stressed book (Rs Cr and %) | OTR 0.04 at 31-Mar-26 (R:R350); Stage 2 Rs83 = 1.21% (P:L667) | OTR 0.02 (R:R354); Stage 2 Rs90 = 1.26% of gross loans [90/7,119] (P:R514) | OTR immaterial; Stage 2 +Rs7 (+8.4%) | AMBER: Stage 2 grows while Stage 2 cover falls |
| Write-offs in period | H1 FY26 146.20 (R:R257) | H1 FY27 155.56 (R:R256); Q2 alone ND (filing gives H1 only); Q2 write-offs + settlements ≈ 94.90 [INFERENCE, Step 4C] | H1 +6.4% YoY | Mixed: slower than book YoY; up ~38% QoQ [INFERENCE] |
| AUM growth YoY | 28.0% (prior deck L715, A3P-13) | 26.03% (P:R642) | −2.0 pp | GREEN vs 20% trigger; decelerating |
| Disbursement growth YoY | +21.8% [1,219 vs Q1 FY26 1,001; A3P err 1] | +10.0% [1,403/1,275] | −11.8 pp | AMBER: leading indicator for AUM [S L12-14] |
| Cost of funds | Blended 10.78%, incremental 10.20% (C:R062, C:R059) | Blended 10.63%, incremental 10.04% (C:R061, C:R058; deck set P:R338/P:R343, attribution scrambled P:R359) | −15 bps / −16 bps | GREEN on the metric; but finance cost on ATA 6.46% → 6.74% (+28 bps; P:R787, P:R797, P:R788; A3P-08) |
| CRAR % | 42.4% (prior deck L456, A3P F11) | 41.01% (R:R405) | −139 bps | GREEN; leverage 3.24x (P:R852) |
| Promoter pledge | N.A. (no identifiable promoter [N L4]) | N.A. | n/a | n/a |

Half-year cash flow (mandatory Q2 read; for a lender CFO/PAT is not a meaningful ratio):

| Item | H1 FY26 | H1 FY27 | Note |
|---|---|---|---|
| Operating profit before working-capital changes | 468.85 (R:R275) | 637.51 (R:R274) | +36.0% |
| Increase in loan portfolio | (607.44) (R:R279) | (746.94) (R:R278) | Growth absorbs operating cash |
| Net cash from operating activities | (216.47) (R:R295) | (112.35) (R:R294) | Negative by design for a growing lender |
| Income taxes paid vs tax expense | 24.78 vs 17.46 (R:R293, R:R178) | 57.18 vs 51.73 (R:R292, R:R177) | Cash tax ≥ book tax: no accrual gap |
| Net cash from financing | 427.62 (R:R327) | 549.90 (R:R326) | Borrowings fund the book and the liquidity build |
| Fixed deposits > 3 months | 4.55 decrease (R:R305) | (163.21) increase (R:R304) | Liquidity parked in deposits |

**Cash-conversion / earnings-quality classification: INDETERMINATE-WITH-DIRECTION.** Direction: negative CFO is growth-induced (loan book), and cash tax tracks book tax. Indeterminate part: Q2 earnings include a discretionary DA gain (10.12) and a 13-crore fall in the ECL stock, and gross slippage is undisclosed. Missing evidence named: Q2 gross slippage; overlay balance at 30-Jun and 30-Sep; quarterly write-off split. House rule: this caps the verdict at no better than PROCEED WITH CAVEATS.

Mandatory lender questions:
- **Asset-Quality Multiplier band supported:** Sound 1.00x on the headline (GNPA 4.20%, NNPA 1.62%, PCR 62.42%, Non-OD CE 99.2%). Stressed 0.80x is not evidenced. The drift is negative: cover thinning (4.17% → 3.85%), Bucket 1 falling, mortgage PAR X up about 1 pp (C:R162), and a covenant breach on a (PAR 90 + write-off)/GLP test (R:R739). **Pillar 2L fact flagged; band recompute deferred to /fttcp (OR-30).**
- **Credit cost within guided band:** yes on the guided ATA basis (3.82% Q2, 3.95% H1, band 3.5-4.0%). Not a miss for the tracker. On the protocol's avg-AUM basis it is 4.39%.
- **Concentrated or broad-based:** mixed. Bucket 1 CE, Q2 average vs Q1 average, by state group [A4 calc on P:R461-R484]: UP 49.53% vs 51.57% (−2.0 pp; Sep 47.6%, the lowest of nine months across two decks, A3P-06); Rajasthan 55.57% vs 59.93% (−4.4 pp); Rest States, which hold MH/KA/MP, 55.77% vs 56.90% (−1.1 pp); Bihar 38.33% vs 37.87% (+0.5 pp). Three of four groups fell. The two biggest falls (UP, Rajasthan) are not the named drought states. Management has "not identified any particular reason for the dip in UP or other states" (C:L496-497). The stress is spreading but mild.
- **AUM outrunning collection infrastructure:** no. The reverse: disbursement growth (+10.0% YoY) runs below AUM growth (26.03%), and collection staff are being added ahead of H2 (C:L338-349). The classic MFI pre-crisis pattern is absent.
  - **Second reading (A5 ADV-2, grafted in correction loop 1):** the falling repeat share that clears tripwire 8 (52.0% → 51.4%, P:R592, P:R593) also means incremental lending tilts to first-time borrowers. New-customer disbursement +23% YoY, repeat −16% (C:L98-102). Management says repeat loans "perform very well on the credit cost" (C:L259-260). 95% of the book is post-June 2024 (P:R433); 32% of households carry MFI loans (C:L459). The incremental book is therefore less seasoned. Separating observation: Bucket 1 CE and PAR X for the new-to-Aye cohort against the repeat cohort (folded into QfM Q33).

---

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A. Tracker rows for AYE [S]

| Signal Name | Type | Cadence | Latest Observation Date & Value | Direction Since Prior | Per-Company Thesis Element | Signal Health |
|---|---|---|---|---|---|---|
| AYE - Bucket 1 collection efficiency | Tier 2 - Trajectory | Quarterly (monthly in deck) | 2026-10-08: 52.8% Q2 (Q1 54.5%, Q4 FY26 59.8%) [S L5]; confirmed by results deck 52.8% (P:R395); UP Sep 47.6% (P:R472) | Falling | Early warning for 30+ DPD roll ahead of GNPA trigger 1 | Threatens |
| AYE - Disbursement growth YoY vs AUM growth | Tier 2 - Trajectory | Quarterly | 2026-10-08: Rs1,403 cr +10% YoY; AUM +26% [S L12]; confirmed 1,403 (P:R078), +10% (P:R079) | First observation | Leading indicator for the AUM <20% trigger and the 25-30% / 28-33% guidance behind base FV Rs288 | Threatens |

**Flag: the tracker holds 2 signals for AYE, fewer than three.** Role 5.5 should reopen for this company. Candidates are in 5.5C.

Secondary-source note on row 1 [S L8] ("auditor's limited review reportedly flags a breach of the (PAR 90 + write-off)/GLP covenant on INE501X07588") is now CONFIRMED by the filing: R:R739, R:R749.

### 5.5B. Reconciliation

| Target reported | Signals said | Interpretation for AYE |
|---|---|---|
| **Strong** headline: record PAT 86.72 (+151.1% YoY), GNPA 4.20% (lowest on file), credit cost 3.82% | **Falling**: Bucket 1 CE down two quarters; disbursement +10% YoY vs AUM +26% | **Row 2 of the matrix: the target may be over-earning. Treat Q2 as a possible peak print and watch Q3 closely.** The filing itself supports this: the DA gain plus the ECL stock fall exceed the QoQ PBT rise (Step 4C). |

### 5.5C. New signals surfaced this quarter (PAYLOAD ONLY; written only through the run's operator-approval gate; A4 writes nothing)

1. **Drought declarations and rainfall deficit in Maharashtra, Karnataka, Madhya Pradesh** (IMD / state notifications). Management puts these states at ~18% of AUM (C:R011, ASR "AEM") and has moderated disbursement there (P:R027). Monthly. Falsifier: "Rest States" Bucket 1 CE below 55.7% (P:R484) with drought districts widening.
2. **Insurance-commission regulation on credit-linked insurance** (implementation date NOT FOUND). Management names it as an FY28 income headwind and sizes only the offsets (C:L217-220, C:L522-556; A3C-13). Event-driven.
3. **Policy repo rate path** (RBI MPC). "Rising interest rate environment" (C:L215); 25 bp rise already happened (C:L733-734); ROA sensitivity 3 bps FY27 / 6 bps FY28 (C:R171, C:R172). Event-driven.
4. **Pre-IPO investor holdings above 5%** (quarterly shareholding pattern). Alpha Wave India (7.8% at Jun) left the list (A3P-12). Quarterly.

Statement: "New signals proposed for the tracker: drought-state rainfall/declarations (Case B), insurance-commission regulation (Case B), repo rate path (Case B), pre-IPO holder supply (Case B), because each is an external dependency this quarter's filing or call exposed." Not written by A4.

### 5.5D. Forward-view weighting fed to Step 6
Target and signals disagree (matrix row 2). Step 6 weighs the falling Bucket 1 CE and the slowing disbursement above the single strong Q2 print. Monthly Bucket 1 CE fell across Q2 in UP and Rajasthan (P:R467-R478), a multi-month trajectory.

---

## STEP 6: RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

Caveat: Notion's Bear/Base/Bull bands for NIM, credit cost, RoA, GNPA, CRAR and CE were defined for FY26 [N L171-180]. They are the standing bands on the page and are applied to the H1/Q2 FY27 print. AUM and PAT use the Notion trigger floor (bear) and FY27 guide (base).

| Metric | Bear Proj | Base Proj | Bull Proj | Actual | Lands In |
|---|---|---|---|---|---|
| AUM growth FY27 | <20% YoY (trigger floor [N L45]) | 25-30% (FY27 guide [N L148]) | >30% | 26.03% YoY (P:R642) | Base (lower half) |
| NIM | 13.5-14% | 14.5% | 15%+ [N L175] | 15.59% Q2 (P:R810); 15.87% H1 (P:R645) | Bull |
| Credit cost | 5-5.5% | 4.5% | 3.5-4% [N L176] | 3.82% Q2 ATA (P:R389); 3.95% H1; 4.39% avg AUM [A4 calc]; 4.43% ATA if ECL stock held flat [INFERENCE: 94.90 × 4 / 8,576 implied ATA, where 8,576 = 81.90 × 4 / 3.82%] | Bull on the disclosed basis; Base-to-Bull on A4 bases |
| PAT | FY27 < Rs270 cr (trigger [N L46]) | ≥ Rs270 cr | ND (no FY27 bull band on file) | H1 161.22 (R:R183); x2 run-rate 322.44; ex-DA run-rate 307.3 [(161.22 − 7.57) × 2] | At/above Base on run-rate |
| EPS | FY29 Rs15.75 (18% CAGR) | Rs19.20 (26%) | Rs22.10 (32%) [N L235] | H1 FY27 diluted 6.49 vs H1 FY26 3.34 = +94.3% YoY (R:R231, R:R232); FY27 ND | Above all CAGR bands on H1 YoY (IPO-recovery base effect) |
| RoA | 2.0-2.5% | 3.0% | 4%+ [N L177] | 4.04% Q2 (P:R846); 3.90% H1 (P:R651); 3.69% Q2 ex-DA [A4 calc] | Bull on Q2 headline; Base-to-Bull on H1 and ex-DA |
| GNPA | 5.5%+ | 4.5-5% | 4-4.5% [N L178] | 4.20% (R:R402) | Bull |
| CRAR (lender substitute for Net Debt) | 30% | 35% | 40%+ [N L179] | 41.01% (R:R405) | Bull |
| Collection efficiency | 97-98% | 99% | 99.5%+ [N L180] | 99.2% Non-OD (P:R392) | Base-plus |
| ROCE → RoE (lender substitute) | ND (no FY27 band; 3-yr target 17-20%, P:R666) | ND | ND | 13.09% Q2 (P:R854); 12.34% H1 (P:R066) | ND |

Below-bear count: 0. **Probability re-weighting rule: NOT triggered** (needs 2+ metrics below bear for 2 consecutive quarters; prior quarter also 0 [N L182]).

### 6B. Watchlist item status (Notion checklist [N L186-195] + two pending-ruling items [N L385-386])

| # | Watchlist Item | Green Threshold | Red Threshold | This Quarter Reading | Status |
|---|---|---|---|---|---|
| 1 | GNPA trend | At/below 4.49% and declining | Rising two quarters from 4.49% | 4.20% (R:R402), −29 bps QoQ | GREEN |
| 2 | DA % of income | < 4% | > 4% while PAT depends on it | 1.92% Q2 [10.12/527.12, R:R108]; 1.00% H1 [10.12/1,016.78, R:R111]; DA = 54.3% of the QoQ PBT rise | GREEN on threshold / AMBER on dependence |
| 3 | AUM growth YoY | ≥ 25% | < 20% two quarters | 26.03% (P:R642), down from 28.0% | GREEN (decelerating) |
| 4 | FY27 PAT run-rate ≥ Rs270 cr | Run-rate ≥ 270 | < 270 | H1 161.22; run-rate 322.44; ex-DA 307.3 | GREEN |
| 5 | Credit cost band 3.5-4.0% | Within band | Above 4% | 3.82% Q2, 3.95% H1 (ATA) | GREEN on disclosed basis / AMBER (avg-AUM 4.39%; ECL stock fell 13) |
| 6 | PCR ≥ 60% | ≥ 60% | < 60% | 62.42% (R:R404), −138 bps | GREEN, thinning |
| 7 | Covenant unwaived (4 at FY26; no drift) | ≤ 4 and resolving | Count rises | Bank-lender count ND (A3 cross-walk item 7). One listed-NCD breach, INE501X07588, waived (R:R617) and auditor-qualified (R:R740) | UNKNOWN (AMBER on the NCD breach) |
| 8 | Over-lending metrics | No rise in AUM/borrower or repeat share while GNPA rises | Rise with GNPA rising | Repeat share of HL AUM 52.0% → 51.4% (P:R592, P:R593); AUM per active loan ~Rs1.10 lakh, flat (A3P s.5: 7,597 / 6,92,676 loans vs 7,324 / 6,69,261); MFI overlap 8-9% borrower / 32% household (C:R134, C:R135, ASR); GNPA falling. Second reading (A5 ADV-2): the falling repeat share means new lending tilts to first-time borrowers (new-customer disbursement +23% YoY, repeat −16%, C:L98-102; repeat loans perform better on credit cost, C:L259-260) | GREEN on the trigger (condition absent) / AMBER on the second reading |
| P1 | Bucket 1 CE (pending ruling) | ≥ 54.5% with PAR X falling | Third decline below 52.8% with PAR X rising [S L7] | 52.8%; PAR X 6.94% (P:R383) vs 7.01% | AMBER (second decline; falsifier not met) |
| P2 | Disbursement growth YoY (pending ruling) | ≥ 15% | < 15% in Q3 [S L14] | +10.0% Q2 | AMBER (Q3 test) |

Tally: 4 GREEN (1, 3, 4, 6); 3 GREEN/AMBER split (2, 5, 8); 1 UNKNOWN (7); pending items 2 AMBER. Prior AR tally was 6 GREEN / 1 AMBER / 1 UNVERIFIABLE [N L197].

### 6C. Thesis-broken trigger check [N L43-48]

| Thesis-Broken Condition | Threshold | Current Reading | FIRED? |
|---|---|---|---|
| Gross Stage III reversing upward from 4.49% for two consecutive quarters | Two consecutive rises | 4.20%, down 29 bps (R:R402) | NOT FIRED |
| Net gain on derecognition above ~4% of total income while PAT growth depends on it | > 4% AND dependence | 1.92% of income (below); dependence present QoQ (62% of the PAT rise) | NOT FIRED (one of two conditions met) |
| AUM growth below 20% YoY for two consecutive quarters | < 20% twice | 26.03% | NOT FIRED |
| FY27 audited PAT below ~Rs270 cr | FY27 audited PAT | H1 161.22; run-rate 322.44 | NOT TESTABLE until FY27 audit; on track |
| Unwaived covenant-breach instances failing to resolve (AR: 15 → 4) | Count rises / no resolution | Bank count ND; listed-NCD breach waived; breached ISIN redeems 17-Nov-2026 (R:R664) | NOT FIRED (UNVERIFIABLE) |
| Over-lending: AUM per borrower or repeat-loan share rising while GNPA rises | Both | Repeat share falling; GNPA falling | NOT FIRED |

**No condition has FIRED. No exit recommendation.**

### 6D. Growth trigger status
Notion lists no separate growth-trigger table. The triggers below are taken from the thesis line and the Q1 Step 2L log [N L16, L146-160].

| Trigger | Original Confidence | Confirming Evidence | Killing Evidence | Updated Status |
|---|---|---|---|---|
| T1 Asset-quality recovery continues (thesis core) | HIGH [N L16] | GNPA 4.20%, lowest on file; PAR X 6.94% below the 7% H1 target (C:R159) | Write-offs + settlements ~95 vs ~69 QoQ [INFERENCE]; Bucket 1 falling; covenant reason cites "higher delinquencies" this FY (R:R749) | ON TRACK (headline) / WEAKENED (quality) |
| T2 Credit cost into 3.5-4.0%, then 3-3.5% medium term | HIGH [N L150] | 3.82% Q2, 3.95% H1, in band | Rupee charge flat; ECL stock −13; cover 4.17% → 3.85% | ON TRACK (disclosed), conditioned on cover |
| T3 AUM growth 25-30% FY27 / 28-33% 3-yr | HIGH [N L148] | 26.03% | Disbursement +10% YoY; 0 branches in H1; repeat −16% YoY (C:R024); headroom 4,408 vs +8,300-10,300 needed (A3P-01) | WEAKENED |
| T4 RoA 4-4.5% / RoE high teens | MEDIUM [N L154] | Q2 RoA 4.04%, RoE 13.09% | Ex-DA 3.69%; H1 3.90% below band; NIM band implies H2 compression | ON TRACK (headline) / WEAKENED (ex-DA) |
| T5 Funding-cost decline from rating upgrade | HIGH [N L160] | Blended 10.63%, incremental 10.04%; A+ (Stable) upgraded June 2026 (P:R355, P:R357) | Finance cost on ATA +28 bps (liquidity carry) | FIRED (on the CoB metric) |
| T6 Mortgage mix toward 30-35% (secured shift) | MEDIUM [N L158] | None | Share 23.3% → 23.2% (A3P-02); microlap tightened (C:L629-630); mortgage PAR X +1 pp to ~6% (C:R162, C:R163) | DELAYED |
| T7 Gold loans / secured basket | LOW | "Couple of pilot branches" this FY (C:R284) | "Evaluating", "if we decide" (C:R258, C:L262) | NEW |

---

## STEP 6.5: EXPECTATION LEDGER AND A21 BASE REFRESH: DEFERRED to /fttcp and Role 1 (OR-30)

Pillar-relevant facts flagged for the 6.5A refresh (inputs only; no base is set here):
- Q2 PAT 86.72 annualised = 346.88 [× 4]. Known one-offs: DA gain 10.12 pre-tax (7.57 post-tax); ECL stock fall 13.0 pre-tax (9.73 post-tax) [INFERENCE]. Ex-DA annualised 316.6. Ex-DA and ex-ECL-fall annualised ≈ 277.7 [(86.72 − 7.57 − 9.73) × 4].
- Seasonality: H2 carries ~60% of annual disbursement (C:R097, C:R114). A trailing-4-quarter base may suit better: TTM PAT = H2 FY26 128.51 + H1 FY27 161.22 = 289.73 [A4 calc]. Declare the choice at /fttcp.
- Funding-mix carry (A5 ADV-1): about Rs14 cr a quarter of NII reflects post-IPO low leverage and unwinds as leverage returns to 4-4.5x (C:L272-274) [INFERENCE, A5].
- Notion carried base: FY26 diluted EPS 9.60 (R:R233); FY29 EPS base 19.20 [N L235].
- 6.5B Expectation Ledger: ledger rows not passed to A4 (ND). One dated expectation on file resolved this quarter: add-gate leg (i) "slippage disclosed" missed its Q2 date (third non-disclosure). If credited in the ledger, it is a MISSED/decay event under Amendment 25 mechanics. Operator and /fttcp decide.

## STEP 7: FOUR-PILLAR RE-VALIDATION: DEFERRED to /fttcp and Role 1 (OR-30)

| Pillar / Input | Notion assumption | This quarter's flagged fact | Direction |
|---|---|---|---|
| Pillar 1 ROE base | FTTCP-mediated; FY26 RoE 9.3%, Q4 16% [N L224] | Q2 RoE 13.09%, H1 12.34% (P:R854, P:R066); leverage 3.24x (P:R852); RoTA 4.04%, ex-DA 3.69% [A4 calc]; ~Rs14 cr/qtr post-IPO funding-mix carry unwinds on re-levering (A5 ADV-1) | Positive headline; quality caveat |
| Pillar 2L Asset-Quality Multiplier | 1.00x Sound [N L225] | GNPA 4.20; NNPA 1.62; PCR 62.42 (−138 bps); total ECL cover 3.85 (from 4.17); Stage 2 cover 47.44; Bucket 1 52.8; (PAR 90 + WO)/GLP covenant breach; slippage undisclosed three times; H1 write-offs 155.56; incremental tilt to first-time borrowers (A5 ADV-2) | Negative drift; band unchanged on headline |
| Pillar 3 Growth Visibility | +3x to +4x [N L226] | Disbursement +10% YoY; AUM growth 28.0% → 26.03%; 0 branches in H1; guidance repeated, not refined; existing-branch headroom below the 3-yr target gap | Negative |
| Strategic Premium | +0x [N L227] | Gold-loan pilot only | Neutral |
| UA Multiplier | N/A until Feb 2027 [N L229] | One-year listing date ~16-Feb-2027 (listing R:R638); Alpha Wave India left the >5% list (A3P-12) | Watch at the gate |
| Sector Cap | 18x NBFC [N L228] | No reclassification | Hold |
| Hurdle Ratio | CONDITIONAL [N L24] | Recompute deferred | n/a |

Single-credit reminder: the credit-cost improvement may be credited once (Pillar 1 via RoE or Pillar 2L), never through both.

---

## STEP 8: POSITION DECISION

### 8A. Decision logic, HELD branch (Decision Status HELD verified, Step 0A)

| Gate in 8A | Reading | Result |
|---|---|---|
| Any thesis-broken condition FIRED? | None (6C) | Pass on |
| Momentum bucket (chandelier)? | No momentum bucket or chandelier on file [N L412: "No stop or trim line is on file"] | Pass on |
| Actual below BEAR on 2+ key metrics? | 0 below bear (6A) | No trim |
| Between BEAR and BASE? | No key metric lands there on the disclosed basis | n/a |
| At or above BASE | Yes on disclosed metrics → "hold or add per existing entry/MoS rules" | Apply the add rules |
| Existing add rule: Q2 add-gate [N L244-249] | (i) Gross slippage: NOT disclosed for the third consecutive event. Notion's pre-committed rule reads this as BEAR [N L256]. **FAIL.** (ii) PCR 62.42% ≥ 60%: PASS. (iii) Refined FY27 guidance: deck bands repeated verbatim (A3P-14); only verbal points on the call: **NOT MET.** (iv) Covenant non-drift: bank-lender count ND: **UNVERIFIABLE.** | **Gate FAILS (1 of 4 legs passes)** |
| Existing entry rule | Last CMP on file Rs162 (13-Oct, STALE) is above Entry Price Max Rs148 [N] | No add on price either |

**Outcome: HOLD 4% at Rs132. No add. No trim mechanics triggered. Proposed Decision Status: unchanged (HELD). The operator sets it.**

### 8B. Add-back / trim trigger refinement (proposals for operator ruling)

- Original add-back trigger: the four-leg Q2 add-gate [N L244-249].
- Revised add-back trigger (proposed for Q3): (i) gross slippage disclosed ≤ 3.68% of AUM, OR, if still undisclosed, total ECL cover not below 3.85% (P:R528) AND implied write-offs + settlements not above the Q1 level (≈ 69, Step 4C); (ii) PCR ≥ 60%; (iii) a formal narrowing of FY27 bands on the guidance slide; (iv) bank-lender unwaived covenant count disclosed ≤ 4 AND no listed-NCD breach in the Q3 Annexure 3; (v) NEW: Bucket 1 CE for Dec-2026 ≥ 54.5%.
- Original trim ladder: none on file [N L412].
- Revised trim ladder (proposed): trim 25% if any two of these occur at Q3: Bucket 1 CE third consecutive decline below 52.8% with PAR X rising [S L7]; Q3 credit cost above 3.82% ATA; total ECL cover below 3.85% for a second quarter; disbursement growth below 15% YoY [S L14]. Operator decides.
- Pending rulings to close: Bucket 1 CE as a named tripwire; disbursement growth as a leading indicator [N L385-386]. This quarter's data supports both.

### 8C. Single cleanest metric for Q3 FY27

**Q3 FY27 credit cost (ATA, as disclosed), read with total ECL cover held at or above 3.85%.**
- Bull threshold: credit cost ≤ 3.3% with total ECL cover ≥ 3.85%. This puts management's ~3.5% FY27 average (C:R147) within reach without another cover release.
- Bear threshold: credit cost > 3.82%, OR total ECL cover < 3.85% (a second quarter of cover release).
- Why this one: gross slippage, the Q2 metric, resolved BEAR by non-disclosure and cannot be read. Credit cost at constant cover is the filed number that separates "losses are falling" from "reserves are being drawn down".
- Secondary (signal tracker): Bucket 1 CE in the Q3 business update (early January 2027 [N L344]): ≥ 54.5% bull; ≤ 52.8% with PAR X up bear.

---

## STEP 8.5: QUESTIONS FOR MANAGEMENT (also serves as Role 5 Step 8F forward list)

Every A3 finding classed FORWARD-SIGNAL or AMBIGUOUS maps to at least one row (mapping check below the table). A4's own findings A4-01 to A4-04 and the A5 counter ADV-2 are mapped too. Ordered by thesis materiality. Categories: A operational gap, B forward catalyst, C margin, D asset quality, E customer/portfolio, F capital allocation/balance sheet, G governance.

| # | Question | Cat | Why It Matters | Bull Answer | Bear Answer | What to Watch in Next Concall | From findings |
|---|---|---|---|---|---|---|---|
| Q1 | What was gross slippage into Stage 3 (Rs cr) in Q1 and in Q2 FY27? The filing implies write-offs plus settlement losses near Rs95 cr in Q2 against near Rs69 cr in Q1. | D | Add-gate (i); GNPA thesis; third non-disclosure | Slippage ≤ 3.68% of AUM annualised; Q2 write-offs a one-time policy catch-up | Slippage > 4.5% of AUM, or withheld again | Slippage as a standing quarterly disclosure | A3-11, A3P-05, A3P-20, A3C-18, A4-03 |
| Q2 | What was the management overlay at 30-Jun and at 30-Sep, and how much of the Rs13 cr fall in total ECL (287 to 274) went through Q2 P&L? | D | Q2 PAT quality; the ex-overlay test can no longer be run | Overlay reclassified into stages; nothing released | Overlay released into Q2 profit | Overlay balance every quarter | A3C-01, A3P-15, A3P-05 |
| Q3 | For INE501X07588, what are the threshold and the actual for (PAR 90 + write-off)/Gross Loan Portfolio, and which delinquency rose "in this financial year"? | D | Covenant tripwire; the filing text contradicts the GNPA narrative | Legacy FY26 write-off effect; ISIN redeems 17-Nov | Other clause-10.3 deeds near the threshold | Q3 Annexure 3 | A3-03 |
| Q4 | How many bank-lender covenant instances were unwaived at 30-Sep (4 at FY26), and does any deed require exclusive cover of 1.10x (printed 1.1, computed 1.091x)? | F | Add-gate (iv); thesis trigger 5 | ≤ 4, all deeds at 1.00x minimum | Count rises or a 1.10x deed is short | Covenant count disclosure | A3-15, A3-03 |
| Q5 | What was Q2 ROA excluding the Rs10.12 cr DA gain, and is DA a planned lever for H2? | C | DA = 62% of the QoQ PAT rise; trigger 2 dependence | DA opportunistic, ≤ 1% of FY income | DA needed to meet the RoA guide | DA amount each quarter | A3-13, A3P-07, A3C-02 |
| Q6 | Your FY27 credit cost of about 3.5% needs H2 near 3.05% against Q2's 3.82%, and Q2's charge was flat in rupees (81.41 to 81.90). What Q3 credit cost, in rupees and as a ratio, does the plan assume? | B | The hardest testable claim on the call; the QoQ ratio fall came from a larger asset base | ≤ 3.3% with cover held | Path relies on further cover release or a bigger denominator | Q3 credit cost (Rs and ratio) and ECL cover | A3C-08, A4-02 |
| Q7 | What share of September Bucket 1 accounts rolled to 30+ DPD in October? | D | Leading indicator for the GNPA trigger | Roll rate flat vs last year | Roll rate up | Monthly Bucket 1 by state | A3P-06, A3C-03 |
| Q8 | What were mortgage PAR X, Stage 3 and the foreclosure rate in each of the last four quarters? | D | Secured-mix lever; adverse-selection risk | PAR X back below ~6%, foreclosures stable | PAR X and foreclosures both rising | Mortgage asset-quality table | A3C-04 |
| Q9 | What mortgage share of AUM does the FY27 plan assume, and what was Q2 ML disbursement? | E | Promise repeated twice with no delivery (23.3% → 23.2%) | Share rises from Q4 | Share falls below 22% | ML disbursement and share | A3P-02 |
| Q10 | For MH, KA and MP, what are the AUM share, Bucket 1 CE and PAR X at 30-Sep? | D | ~18% of AUM per the call; the deck gave no exposure | Share ≤ 18%; CE stable | Rising PAR X in drought districts | State table | A3P-04, A3C-07 |
| Q11 | How much cattle AUM sits in drought-declared districts, and how much of the book does credit-guarantee cover protect there? | D | Cattle 25-28% of book (C:R111); CGS 200-300 cr (C:R190) | Small cattle exposure in drought districts | Concentrated exposure, little cover | Drought-district exposure | A3C-07, A3C-19 |
| Q12 | You committed at Q1 to narrow FY27 ranges at H1. Will you publish narrowed bands? | B | Add-gate (iii); credibility scoring | Formal narrowing at Q3 | Bands repeated again | Guidance slide | A3P-14 |
| Q13 | Does the 14.25-14.75% NIM band imply H2 NIM of about 12.6-13.6%, and if so, how is RoTA 4.0-4.5% reached? | C | Guidance internal consistency | Band stale; NIM holds near 15% | Real compression; RoTA below 4% | Q3 NIM | A3C-10, A3P-14 |
| Q14 | What was October 2026 disbursement? | A | Disbursement +10% YoY vs AUM +26%; analyst cited 550-600 (C:R129) unanswered | ≥ 550 | Below Q2's monthly run-rate | Monthly disbursement | A3P-13, A3C-14 |
| Q15 | What was Q3 repeat-loan disbursement growth YoY (Q2 was −16%)? | E | Repeat is both the AUM lever and a yield drag | Back to positive growth | Still negative | Repeat vs new split | A3C-14, A3P-13 |
| Q16 | Are split branches counted in the 571, and how many new branches will operate by 31-Dec-2026? | B | Counts on the call varied (30+, 35, 35-40, 40; totals 80-90 and 80); deck channels sum to 624 | Clear count, on schedule | Slips again | Branch count at Q3 | A3C-11, A3P-10, A3C-09 |
| Q17 | The 28-33% 3-year AUM CAGR needs Rs8,300-10,300 cr more AUM; existing-branch headroom is about Rs4,408 cr at Rs21 cr per branch. How many new branches does the plan assume? | B | Pillar 3 growth visibility | Network plan closes the gap | Target needs opex not in the guide | 3-year plan disclosure | A3P-01 |
| Q18 | Finance cost on ATA rose 28 bps while blended CoB fell 15 bps, and cash plus bank reached Rs1,341.66 cr. By when will this liquidity be deployed? | C | NIM drag; negative carry; liquidity also inflates the ATA denominator of every ratio | Deployed in Q3; NIM holds | Liquidity stays; NIM falls | Liquidity and finance cost per average borrowing | A3-14, A3P-08, A3C-05, A4-02 |
| Q19 | Where will the undeployed Rs70 cr of the July 2026 NCD (INE501X07745) go, and by when? | F | Funds raised ahead of need | Deployed in Q3 | Idle into Q4 | Reg 52(7) statement | A3-07 |
| Q20 | For the Rs455 cr of bank/NBFC borrowings without security, when do the lenders' time limits expire? | F | Lender rights; down from 510 at Q1 | Security created by Q3 | Time limits extended again | Annexure footnote | A3-06 |
| Q21 | Was the Q1 auditor's point on Excel-based charge allocation fixed, or does the new auditor not report it? | G | Control over secured-asset allocation | Fixed in the loan system | Still manual | Auditor report | A3-05 |
| Q22 | What product is the Rs53.31 cr co-lending book, whose share is it, and what ECL is held against its 19.9% NPL? | D | New exposure with high NPL and nil fees | Small run-off book, fully provided | Live channel with high losses | Note 5(d) | A3-12 |
| Q23 | Is Gaurav Seth the CFO and a KMP as of 22-Oct-2026, and why did the CS sign every Q2 filing? | G | KMP churn AMBER (3 CFOs in 5 months) | CFO confirmed; signing delegation explained | Undisclosed CFO change | Reg 30 KMP filings | A3-16, A3C-15, A3P-09 |
| Q24 | Was the CTO change a replacement, and why did the previous CTO leave? | G | CFO and CTO seats both moved within a year | New role, orderly handover | Unexplained exit | Reg 30 filings | A3P-09, A3C-15 |
| Q25 | Was the move from SSKM to MSKA only the RBI-mandated rotation? | G | Auditor change in the quarter the covenant observation was escalated | Rotation only | Disagreement | AGM records, auditor letter | A3-24 |
| Q26 | Why did the auditor sign the security-cover report at 11:09:12, before the 11:15 board start, while citing Board-approved results? | G | Process integrity | Signing workflow explained | Report prepared on unapproved figures | Auditor or company explanation | A3-18 |
| Q27 | What agenda items followed the 6-minute results approval, and will a Reg 30 outcome follow? | G | Board scrutiny | Routine items | Material items undisclosed | Reg 30 outcome | A3-08, A3-17 |
| Q28 | When was hedge accounting designated, on what hedged items, and how much derivative MTM now goes to OCI? | F | FY26 PAT comparability | Clean designation from 1-Apr-26 | Volatility moved out of P&L | Hedge note | A3-01 |
| Q29 | What is the carrying value of Arcil security receipts and the provision held against them? | D | Nil provision line; investments 158.14 → 222.96 | Provided and RR1-rated | Unprovided SR exposure | SR note | A3-02 |
| Q30 | Which actuarial assumption produced a Rs5.36 cr H1 loss against Rs0.56 cr for FY26? | G | OCI anomaly | Discount-rate change | Attrition assumption reflecting churn | FY27 AR | A3-09 |
| Q31 | What share count is the EPS denominator, and does it include Trust-held treasury shares? | F | EPS integrity | Reconciled | Error | EPS note | A3-10 |
| Q32 | Will the Rs22.63 cr unutilised offer-expense estimate be revised, and will any surplus return to net proceeds? | F | IPO accounting | Returned to proceeds | Basis drift | Note 10 | A3-19 |
| Q33 | What share of borrowers have two or more unsecured lenders? What are Bucket 1 CE and PAR X for the MFI-overlap cohort vs the rest, and for new-to-Aye borrowers vs repeat borrowers? | E | Over-lending tripwire 8; incremental tilt to first-time borrowers (new +23%, repeat −16%, C:L98-102) | Overlap and new-to-Aye cohorts perform in line | Either cohort worse | Cohort table | A3C-06, A5 ADV-2 |
| Q34 | What was insurance-commission income in FY26 and H1 FY27, in Rs cr and bps of ATA? | C | Size of the FY28 headwind vs the 85-100 bps offsets | Small | > 50 bps of ATA | Fee split | A3C-13, A3P-07 |
| Q35 | What were Q2-only tele-caller productivity and foreclosure rate (the deck moved both to an H1 basis)? | E | Repeat engine | Q2 ≥ Q1 | Q2 near the implied Rs1.37 cr (−22%) | Q3 deck basis | A3P-16 |
| Q36 | Was any portfolio purchased in H1 FY27, and where is purchased DA AUM now reported? | A | Growth attribution | None | Purchased AUM inside "organic" growth | Growth chart | A3P-17 |
| Q37 | Did Alpha Wave India exit fully, and do other pre-IPO holders plan to sell? | F | Supply overhang; UA qualifiers | Placed with long-only holders | Further exits | Shareholding | A3P-12 |
| Q38 | Please list the eight quarterly GNPA prints behind "seven consecutive quarters". Why did the 08-Oct business update show GNPA 4.30%, PAR X 6.88% and AUM 7,604, against 4.20%, 6.94% and 7,597 in the results? | G | Data integrity | Late write-offs or recoveries explained | Unexplained revisions | Business update vs results | A3C-16, A4-01, A4-04 |
| Q39 | What is PAR 30 at 12 months on book for AI-ML-underwritten loans vs cluster-underwritten loans? | A | 32% of underwriting now on AI-ML | Equal or better | Worse | Model performance table | A3C-19 |
| Q40 | When will the board approve gold loans, how many pilot branches, and with what capex? | B | New collateral class with new infrastructure | Small pilot, defined budget | Large unbudgeted build | Board approval | A3C-12 |

Mapping check: results FORWARD-SIGNAL A3-03, A3-06, A3-07, A3-12, A3-13, A3-16 and AMBIGUOUS A3-01, A3-02, A3-05, A3-08, A3-09, A3-10, A3-11, A3-14, A3-15, A3-17, A3-18, A3-19, A3-24; presentation FORWARD-SIGNAL A3P-06, A3P-07, A3P-12, A3P-13 and AMBIGUOUS A3P-01, A3P-02, A3P-04, A3P-05, A3P-08, A3P-09, A3P-10, A3P-14, A3P-15, A3P-16, A3P-17; concall FORWARD-SIGNAL A3C-03, A3C-04, A3C-08, A3C-12 and AMBIGUOUS A3C-01, A3C-02, A3C-05, A3C-06, A3C-07, A3C-09, A3C-10, A3C-11, A3C-13, A3C-14, A3C-15, A3C-16, A3C-19. All 51 have a question row. A4-01 (Q38), A4-02 (Q6, Q18), A4-03 (Q1), A4-04 (Q38) and A5 ADV-2 (Q33) are mapped too. NEUTRAL-FACT and CONFIRMATORY-NEGATIVE findings are carried in the text (A3-04, A3-20 to A3-23, A3-25 to A3-27, A3P-03, A3P-11, A3P-18 to A3P-20, A3C-17, A3C-18, A3C-20).

**Top 3 by likelihood of thesis-changing information:**
- Q1 (gross slippage, Q1 and Q2): a figure at or below 3.68% of AUM would lift the Bull case. A figure above 4.5% would confirm the A4-03 proxy.
- Q3 (covenant threshold and the delinquency that rose "this financial year"): the answer most likely to confirm the Bear case, because it comes from management's own filed text.
- Q2 (overlay at 30-Jun and 30-Sep): the transparency test. Management changed the ECL basis "to make the numbers more transparent" (C:L402-404) while the figure that matters fell into an audio gap.

**Channel recommendation:** IR email now. The concall has occurred without these answers. Send all 40 questions verbatim to the IR contacts (Gaurav Seth, CFO, and Sovan Satyaprakash; P:R911) and to SGA (P:R912). First check the official transcript, when filed, for Q2 (overlay amount, C:L413) and the 50 bp scenario (C:L729-732). Prioritise Q1, Q3 and Q2 for the Q3 FY27 call.

### Prior-quarter Questions for Management: answer status (Role 4 non-negotiable; Role 5 Step 3E)

Source: Q1-Q16 [N L104-121], Q17-Q19 [N L136-140], Q20-Q33 [N L273-283].

| Prior Q | Topic | Answer Status | If answered, what was said | Verdict |
|---|---|---|---|---|
| Q1 | Ex-overlay credit cost, 4 quarters; overlay policy | PARTIALLY ANSWERED | Overlay now included in stage ECL "to make the numbers more transparent" (C:L402-405); amount lost in ASR (C:L413) | Basis changed; ex-overlay view gone (A3P-15) |
| Q2 | Disclose gross slippage as a standing metric | NOT ADDRESSED | Not asked; not volunteered; absent from results and deck | Third non-disclosure event |
| Q3 | Quantify the reducing slippage behind the NIM tailwind | NOT ADDRESSED | n/a | Open |
| Q4 | NIM at 4-4.5x leverage and 30% mortgage; IPO-cash share of 15.9% | PARTIALLY ANSWERED | Band held for mortgage-book and repeat accumulation and rates (C:L724-729) | No quantification |
| Q5 | Explicit FY27 PAT / RoA range | PARTIALLY ANSWERED | RoTA 4.0-4.5% "untouched" (C:L556); no PAT figure | Open on PAT |
| Q6 | Recurring other income ex-DA ex-forex; DA re-pull | NOT ADDRESSED | DA restarted at 10.12 with no comment (A3C-02) | Silent restart |
| Q7 | Gold/solar timeline, capital, FY28 share | PARTIALLY ANSWERED | Gold pilot branches this FY (C:R284); no capital or share | Open |
| Q8 | Which ranges narrow at Q2/H1 | PARTIALLY ANSWERED | Verbal points: credit cost ~3.5% (C:R147), opex ~8.5% (C:R144); deck bands unchanged | Commitment only partly met |
| Q9 | Mortgage lever medium-term; FY27 share | PARTIALLY ANSWERED | 22-23% (C:R177); microlap tightened; scale-up Q4/Q1 (C:R287) | Lever paused |
| Q10 | FY27 CoB reduction from rating upgrade (bps, Rs cr) | PARTIALLY ANSWERED | Blended −15 bps, incremental −16 bps; 25 bp upside next year (C:R277) | No Rs cr |
| Q11 | Forex → OCI scope; DA through P&L | NOT ADDRESSED | Filing shows a cash flow hedge reserve in OCI (A3-01) | Open (now Q28) |
| Q12 | AUM per borrower and repeat-loan share | PARTIALLY ANSWERED | Deck repeat share 51.4% (P:R593); MFI overlap 8-9% / 32% (C:R134-R135) | Repeat share now disclosed |
| Q13 | CRAR 41.3% (call) vs 42.38% (workup) | ANSWERED SPECIFICALLY (by filing) | Filed CRAR 41.01% at 30-Sep (R:R405); Jun 42.4% (prior deck) | Closed |
| Q14 | AUM 7,324 vs 7,384 | ANSWERED SPECIFICALLY (by filing) | Deck Q1 AUM 7,324 (P:R073); business update 7,329 [N L310] | Closed; 5 cr gap noted (A4-01) |
| Q15 | PCR this quarter | ANSWERED SPECIFICALLY (by filing) | 62.42% (R:R404) | Closed |
| Q16 | 14 unwaived covenant instances | NOT ADDRESSED | Not on the call; filing shows the NCD breach waived (R:R617) | Bank count still ND |
| Q17 | CoB trajectory; NCD coupons; Rs cr saving | PARTIALLY ANSWERED | Annexure 3 coupons 9.75% (new NCD) vs 9.95-11.30% (older) (R:R559, R:R545-R558) | No Rs cr |
| Q18 | Covenant status (repeat of Q16) | NOT ADDRESSED | n/a | Second silence on calls |
| Q19 | FY27 funding mix; ALM | PARTIALLY ANSWERED | Bank share 32% → 35% (C:R132-R133); deck "No ALM mismatch" (P:R379) | Mix chart scrambled (P:R359) |
| Q20 | ECL model back-testing (KAM) | NOT ADDRESSED | n/a | Open |
| Q21 | FY27-28 debt raise plan | PARTIALLY ANSWERED | ~1,200 cr borrowed in Q2 (C:R131) | No plan |
| Q22 | NCD Rs4,000 cr envelope tranching | NOT ADDRESSED | n/a | Open |
| Q23 | Auditor rotation matters | NOT ADDRESSED | MSKA now reviewer; covenant observation escalated (A3-03) | Open (now Q25) |
| Q24 | Specifics of the 4 unwaived covenants | NOT ADDRESSED | n/a | Open (now Q4) |
| Q25 | Mortgage Stage 3 +175% root cause | PARTIALLY ANSWERED | Mortgage PAR X +~1 pp to ~6%; MP and Gujarat branches (C:L652-658) | Stage 3 not given |
| Q26 | Write-off recovery track record | NOT ADDRESSED | n/a | Open |
| Q27 | Internal base case within 28-33% | NOT ADDRESSED | Vision repeated (C:R257) | Open (now Q17) |
| Q28 | Gold/affordable/solar launch calendar | PARTIALLY ANSWERED | Gold pilots this FY | Open |
| Q29 | RBI inspection readiness | NOT ADDRESSED | n/a | Open |
| Q30 | CFO departure reason; Seth mandate | NOT ADDRESSED | Seth introduced without a title (C:L44-45) | Worsened (now Q23) |
| Q31 | CS successor | ANSWERED SPECIFICALLY (by filing) | Anuj Jain, CS & Compliance Officer (R:R572) | Closed |
| Q32 | IT/TDS Rs15.80 cr timeline | NOT ADDRESSED | n/a | Open |
| Q33 | Staff embezzlement controls | NOT ADDRESSED | n/a | Open |

Pattern: 4 answered specifically (all by filing); 13 partly answered; 16 not addressed. **Gross slippage (Q2) is now a three-event non-disclosure** (Q1 call deferral twice in one call, AR silence, Q2 results/deck/call silence). It was evaded on a call once (Q1); on the Q2 call no analyst asked. The Role 5 rule on three consecutive call evasions is therefore not met mechanically. It is flagged for the operator as a governance signal.

---

# SECTION B: CONCALL ANALYSIS (ROLE 5, LENDER VARIANT)

## STEP 0: PRE-FLIGHT

### 0A. Notion
Fetched (Step 0A above). Previous concall log passed: Q1 FY27 Step 2L guidance and Step 3 notes [N L144-166]. Devil's Advocate expectation: interrogate the entry down toward Rs86-115 [N L25]. Management Grade C [N L220].

### 0B. Participants

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Viral Shah, IIFL Capital (C:R197, C:L31-35) | Same host as Q1 [N L408]. House-broker status ND (no IPO syndicate data in corpus). Asked substantive questions (Q5, C:L518-613). |
| CMD / Chairman | Govinda Rajulu Chintala, Chairman (P:R297) | Not on the call. |
| Managing Director | Sanjay Sharma, Founder, MD & CEO (C:R199; P:R306) | Present, principal speaker. No identifiable promoter; MD is co-founder. |
| CEO | Same as MD; Niraj Kaushik, Deputy CEO (C:R200; P:R307) | Present. |
| CFO | Gaurav Seth (C:R201) | Present but **introduced without a title** (C:L44-45). Answered the ECL question (C:L399-409). Deck names him CFO (P:R309, P:R911). Every Q2 filing letter is signed by the CS (A3-16). YELLOW FLAG. |
| COO / Other senior | Sovan Satyaprakash, Chief Strategy & IR Officer (C:R202; P:R312) | Present. COO Ujual George (P:R308) not introduced. |
| IR Advisor | Strategic Growth Advisors (C:R203; P:R912) | External firm. Closing remarks direct investors to SGA (C:L857-858). |

Yellow flags: (1) CFO untitled on the call and absent from filing signatures. (2) CTO changed (Jinu Joseph → Nishit Shrivastava) and a new Chief Compliance Officer box (Anuj Jain) appear in the deck with no mention on the call (A3P-09). (3) Three "Year 1" tenures in the management table (P:R320, P:R321, P:R325). Promoter-absence flag: N.A. (MD present). CFO answering operational questions: no; he answered the ECL question, which is his domain. Operational answers came from the MD, Deputy CEO and Strategy officer (speaker split is best effort).

### 0C. Structure and date
- Call: 22-Oct-2026, 10:00-11:11 IST (C:R296, C:R297). Results approved 21-Oct-2026 at 11:21 (R:R004). Gap about 23 hours: next-day call (protocol "same day = canned" band).
- Duration 4,267 s = 71.1 min (C:R001): normal to engaged.
- Q&A: fulltext lines 245-854, about 73% of spoken lines (ledger concall, Q&A share).
- Analysts: 10 questions, 9 identified (several names ASR-uncertain) plus 1 unidentified (ledger, Q2 row).

### 0D. Safe harbour
No spoken safe-harbour or forward-looking disclaimer appears in the ASR text (C:L27-46 hold the moderator introduction and the management roster only). The deck safe harbour matches Q1 (A3P F7; P:R017-R019). New risk framing appears in the commentary, not in caveats: "deficient monsoon rainfall and localised drought conditions" (P:R023) and the named drought states (A3P-04).

### 0E. Business type
LENDING BUSINESS. Step 2L applies.

---

## STEP 1: OPENING REMARKS: CLAIMS INVENTORY (C:L38-233)

| # | Claim | Type | Quantified? | Source Line |
|---|---|---|---|---|
| 1 | 6.9 lakh active borrowers in 18 states and 3 UTs | Backward | YES | C:L51 (C:R002-R004) |
| 2 | "We occupy a dominant position in this market" | Strategic | NO | C:L55 |
| 3 | AUM +26% YoY | Backward | YES | C:L60 (C:R005) |
| 4 | Credit cost 3.82%, improving for the seventh consecutive quarter, within guidance | Backward | YES | C:L60-61 (C:R006, C:R007) |
| 5 | Opex ratio 8.6%, about 32 bps better QoQ | Backward | YES | C:L62 (C:R008, C:R009) |
| 6 | PAT "more than doubling" | Backward | YES | C:L63 (C:R010) |
| 7 | Solid first half "enhanced the conviction to deliver" the FY27 guide | Forward Soft | NO | C:L64-65 (C:R240) |
| 8 | Micro-MSME momentum; working-capital demand | Macro | NO | C:L68-71 |
| 9 | "Trending towards our guidance target ... on all the salient metrics" | Forward Soft | NO | C:L76-77 (C:R241) |
| 10 | Inflation and El Nino not material to customers | Macro | NO | C:L78-79 |
| 11 | Drought declared in parts of MH, KA, MP; ~18% of AUM; disbursement moderated in some districts | Macro / Operational | YES (ASR) | C:L82-87 (C:R011) |
| 12 | Bihar, UP and Rajasthan largely unaffected by the monsoon | Macro | NO | C:L90-91 |
| 13 | Early signs of festive pickup | Forward Soft | NO | C:L92-93 (C:R242) |
| 14 | AUM 7,597 cr, +26% YoY, +4% QoQ; within the 25-30% range | Backward / Forward Guidance | YES | C:L94-95 (C:R013-R016, C:R243) |
| 15 | Disbursement 1,403 cr, +10% YoY, +15% QoQ; 49,000 new borrowers | Backward | YES | C:L96-97 (C:R017-R020) |
| 16 | New-customer disbursement +23% YoY, +11% QoQ | Backward | YES | C:L98-99 (C:R022, C:R023) |
| 17 | Repeat-loan disbursement −16% YoY, +5% QoQ; festive season shifted into Q3 | Backward | YES | C:L100-102 (C:R024, C:R025) |
| 18 | A better quarter in Q3 for repeat loans | Forward Soft | NO | C:L103-104 (C:R244) |
| 19 | H1 disbursement 2,622 cr, +15%; H1 is ~40% of annual | Backward | YES | C:L105-107 (C:R026-R028) |
| 20 | 571 branches; 30+ new branches operational in Q3 "as per plan" | Operational | YES | C:L111-113 (C:R029, C:R030, C:R246) |
| 21 | AUM per employee 0.67 vs 0.57 cr (+18%); AUM per branch 13.3 vs 12.8 cr | Backward | YES | C:L119-123 (C:R031-R035) |
| 22 | Opex 8.61% vs 8.93%; cost-to-income 49% | Backward | YES | C:L124-127 (C:R036-R039) |
| 23 | GNPA declined seven consecutive quarters to 4.20%; −30 bps QoQ; −70 bps YoY | Backward | YES | C:L131-133 (C:R040-R042) |
| 24 | PAR X 6.94%; −7 bps QoQ; −109 bps YoY | Backward | YES | C:L133-135 (C:R043-R046) |
| 25 | PAR X below 6.5% by year end | Forward Guidance | YES | C:L138-139 (C:R047, C:R249) |
| 26 | 95% of the book originated after June 2024 | Backward / Strategic | YES | C:L142-143 (C:R048) |
| 27 | Credit cost 3.82%: −21 bps QoQ from 4.03%, −119 bps YoY; drivers tighter underwriting, stronger collections, better repayment | Backward | YES | C:L144-149 (C:R049-R052) |
| 28 | FY credit cost within the 3.5-4% range | Forward Guidance | YES | C:L150 (C:R250) |
| 29 | Non-OD CE 99.2%, Bucket 1 52.8%: "very good collection efficiencies" | Backward | YES | C:L151-153 (C:R054, C:R055) |
| 30 | CRAR 41%; capital sufficient for ~2 years without fresh equity | Operational / Forward Guidance | YES | C:L159-162 (C:R056, C:R057, C:R251) |
| 31 | Incremental CoB 10.04% vs 10.20%; blended 10.63% vs 10.78%; rating upgrade | Backward | YES | C:L163-174 (C:R058-R062) |
| 32 | CoB benefit to flow through progressively | Forward Soft | NO | C:L175-176 (C:R252) |
| 33 | Gross total income 527 cr, +23% YoY, +8% QoQ | Backward | YES | C:L180-182 (C:R063-R066) |
| 34 | NIM 15.6% above the 14.25-14.75 guide; guide assumed a more aggressive repo rise and excluded the rating upgrade | Backward / Forward Guidance | YES | C:L183-188 (C:R067, C:R068, C:R342, C:R343) |
| 35 | Operating profit 198 cr (+55% YoY, +11% QoQ); PAT 87 cr (+151% YoY, +16% QoQ) | Backward | YES | C:L189-192 (C:R069-R074) |
| 36 | RoA 4% in Q2 vs 3.7% in Q1, on total assets | Backward | YES | C:L195-196 (C:R077, C:R078) |
| 37 | H1: GTI 1,017 (+23%), NIM 15.9%, PPOP 377 (+48%), PAT 162 (+148%), RoA 3.89%, RoE 12.32% | Backward | YES | C:L197-200 (C:R079-R088) |
| 38 | FY27 guidance repeated: AUM 25-30%, credit cost 3.5-4%, NIM 14.25-14.75%, opex 8.25-8.75%, RoTA 4-4.5% | Forward Guidance | YES | C:L202-205 (C:R089-R093, C:R253) |
| 39 | Opex and RoA to move into guided ranges in H2 | Forward Guidance | YES | C:L208-211 (C:R254) |
| 40 | Rising rate environment already in the NIM guidance | Macro | NO | C:L215-216 |
| 41 | Prospective insurance-commission recommendations; levers to compensate (opex, CoB, credit cost) | Macro / Forward Soft | NO | C:L217-220 (C:R255, C:R256) |
| 42 | Three-year vision: AUM CAGR 28-33%, RoA 4-4.5% | Forward Guidance | YES | C:L223-226 (C:R257, C:R094, C:R095) |
| 43 | Evaluating gold loans and secured products; "hope to see this take shape later in the year" | Strategic / Forward Soft | NO | C:L227-231 (C:R258, C:R259) |

Diagnostics:
- **Quantified share:** 31 of 43 claims (72.1%) are quantified, mostly backward. Of the 13 forward claims (7, 9, 13, 18, 25, 28, 30, 32, 38, 39, 41, 42, 43), 6 are quantified (46%).
- **New vs reaffirmed:** New: drought exposure ~18% of AUM; the repeat −16% / new +23% split; 30+ branches dated to Q3; the insurance-commission headwind. Reaffirmed: FY27 bands; PAR X target (Q1: sustainable 6-6.5%); capital runway (was 2-2.5 years, now "around two years"); 3-year vision; gold loans (Q1 mentioned gold/solar [N L110]).
- **Quietly dropped:** the Q1 promise to narrow FY27 bands at H1 [N L113, L162]; any DA comment (Q1 discussed a 5-7% cap [N L159]); the 30-35% mortgage share target; gross slippage.
- **Internal contradictions:** "very good collection efficiencies" (C:L153) vs the Q&A admission that "the bucket one collection has dipped over the last 3-4 months" with no identified reason (C:L492-497). "Funding costs continue to ease" (C:L163) vs finance cost on ATA +28 bps (A3P-08). "Credit cost improving seventh consecutive quarter" vs the filed covenant reason "higher delinquencies" this FY (R:R749).

---

## STEP 2L: LENDER GUIDANCE SET

| Metric | This Quarter's Guidance | Last Quarter's (Q1 FY27) [N L148-160] | Two Quarters Ago (start-FY27) [N L146-153] | Trajectory | Confidence |
|---|---|---|---|---|---|
| AUM / loan book growth (FY) | 25-30% held; "Whether we'll be in the closer to 30%, I wouldn't like to commit now" (C:L264-265) | 25-30% (running 28%) | 25-30% | Maintained (top end hedged) | MEDIUM |
| Disbursement target | H2 ~60% of annual (C:R097, C:R114); no number | ND | ND | New | LOW |
| NIM / spread band | 14.25-14.75% held (H1 15.87%, P:R645); mortgage book, repeat and rates cited (C:L724-729) | 14.25-14.75% held; upside conceded | 14.25-14.75% | Maintained | MEDIUM |
| **Credit cost guided band (critical)** | 3.5-4.0% band; FY27 average "3.5 plus minus a few basis points" (C:L534-535); exit lower (C:L296-297); FY28 10-25 bps better (C:R148) | 3.5-4% "well within grasp"; 3.5% if PAR X ~7% | 3.5-4% | **Tightened (verbal, to the floor)** | HIGH (specific) |
| GNPA trajectory commitment | PAR X < 7% by H1 (met: 6.94%), < 6.5% by FY end (C:R159, C:R160) | Sustainable PAR X 6-6.5%; moderate in H2 | none | Maintained | MEDIUM |
| Collection efficiency target | Non-OD 99.2-99.3% (C:R161); Bucket 1 recovery "post November", then "November could become a December" (C:L498-499, C:L574) | Non-OD 99.2-99.3%, stable | none | Maintained (Non-OD); recovery date slipped within the call | MEDIUM |
| Cost-to-income / opex | Band 8.25-8.75%; FY27 ~8.5% (C:R144); FY28 ~8% or better (C:R146); 3-yr 7.0-7.5% (P:R668) | 8.25-8.75% (Q1 8.9%; in band by Q3-Q4); 7-7.5% in 3 yrs | 8.25-8.75% | Tightened (point estimate) | HIGH |
| RoA / RoE target | RoTA 4.0-4.5% "untouched" (C:L556); RoE high teens to low 20s at 4-4.5x leverage, gradual (C:R102, C:R264); 3-yr RoE 17-20% (P:R666) | RoA 4.5-5% post-tax at 3.5-4% credit cost (basis not recorded) | none | Maintained or lowered (basis ambiguity: Q2 RoA on AUM 4.65%, P:R849; on total assets 4.04%) | MEDIUM |
| Capital raise / CRAR plan | No fresh equity for ~2 years; no dilution in the next two FYs (C:R057, C:R106); CRAR 41% | No raise for ~2-2.5 years; raise at 4-4.5x leverage (~Rs14,000 cr book) | none | Maintained (horizon slightly shorter) | HIGH |
| Branch / geography expansion | 30+ new in Q3 (C:R030); ~35-40 new plus 30-40 splits a year; ~80 incl. splits in FY27 (C:R181, C:R182, C:R189); states inside the existing footprint (C:R231-R236) | +40-50 (~10% of large-branch base); no new geographies | none | Maintained on count; delayed on timing (0 in H1) | MEDIUM |
| Mortgage mix (extra row) | 22-23% (C:R177); microlap tightened; scale-up Q4 FY27 or Q1 FY28 (C:R287) | 22%, marginal in FY27; 30-35% in ~3 years | none | Lowered near term | MEDIUM |
| DA / off-book (extra row) | Not discussed; DA restarted (R:R084) | Cap 5-7% of AUM; DA nil in Q1 | none | DROPPED from discussion | n/a |
| Cost of borrowing (extra row) | Blended 10.63%, incremental 10.04%; 25 bp upside next year (C:R277) | WACB 10.78%, incremental 10.20%; −10-15 bps more from the upgrade | none | Maintained; delivered | HIGH |
| Gold loans (extra row) | Pilot branches this FY with new infrastructure (C:R282-R284) | Gold/solar mentioned [N L110] | none | New detail | LOW |

Diagnostics:
- **Widened or tightened:** credit cost tightened verbally to the floor; opex to a point (8.5%). AUM top end hedged. NIM held. RoTA "untouched".
- **Dropped without acknowledgment:** the Q1 promise to narrow bands at H1 (the deck repeats them word for word, A3P-14). The DA cap commentary.
- **Internal consistency [INFERENCE, equal-weight halves]:** a ~3.5% FY average credit cost after H1 3.95% needs H2 ≈ 3.05% [3.5 × 2 − 3.95] (A3C-08). FY opex ~8.5% after H1 8.83% needs H2 ≈ 8.17%. If the NIM band is honest, H2 NIM ≈ 13.13% [14.5 × 2 − 15.87]. Using H2 NIM 13.13%, fee and other income ~2.2% of ATA (P:R823), opex 8.17% and credit cost 3.05%, H2 pre-tax RoA ≈ 4.11%, post-tax ≈ 3.08% [4.11 × 0.7483 = 3.0755; ST-5]. That cannot deliver FY RoTA of 4.0-4.5% after H1's 3.90%. Either the NIM band is stale (bull reading) or the RoTA band is out of reach (bear reading). Q3 NIM separates them.
- **vs Four-Pillar projections:** NIM and RoA headlines sit above the Notion base; AUM sits in the lower half of base.
- **Guidance refused:** AUM top end (C:L265); size of the insurance-commission hit (A3C-13); October disbursement (A3C-14, A3C-19); AI-ML delinquency numbers (A3C-19).

---

## STEP 3: PROMISE vs DELIVERY AUDIT

### 3A. Q1 FY27 commitments: delivered?

| Commitment From Q1 FY27 Concall [N L146-160] | This Quarter's Actual | Status | Points |
|---|---|---|---|
| AUM growth FY27 25-30% | 26.03% YoY at H1 (P:R642) | UNCLEAR (full-year metric) | excluded |
| NIM band 14.25-14.75% | 15.87% H1 (P:R645) | UNCLEAR (full-year metric) | excluded |
| Credit cost 3.5-4% | 3.95% H1 ATA (P:R401) | UNCLEAR (full-year metric) | excluded |
| Sustainable PAR X 6-6.5%, moderating in H2 | 6.94% (P:R383) | UNCLEAR (H2 metric) | excluded |
| Non-OD CE 99.2-99.3%, stable | 99.2% (P:R392) | DELIVERED | 1.0 |
| Opex 8.25-8.75%, in band by Q3-Q4 | 8.61% in Q2 on ATA (P:R646). Qualifier (A5 ADV-3): delivery is denominator-assisted. Rupee opex +2.4% QoQ (180.49 → 184.74, R:R132-R146); opex on average AUM 10.05% → 9.91% (−14 bps) [180.49 × 4 / 7,184; 184.74 × 4 / 7,460.5] against −32 bps on ATA (8.93% → 8.61%, P:L920, P:R646) | DELIVERED (early, on the guided ATA basis; denominator-assisted) | 1.0 (0.5 if scored PARTIAL; see 3B) |
| RoA 4.5-5% post-tax at 3.5-4% credit cost | Q2 4.04% on total assets; 4.65% on AUM (P:R849); basis not recorded in the Q1 log | UNCLEAR (full-year; basis) | excluded |
| No equity raise for ~2-2.5 years; CRAR | CRAR 41.01%; no raise; now "around two years" | UNCLEAR (multi-year) | excluded |
| Branches +40-50 in FY27; no new geographies | 0 opened in H1 (P:R627); 30+ promised in Q3 | UNCLEAR (full-year; timing at risk) | excluded |
| Leverage 3.15x → 4-4.5x before a raise | 3.24x (P:R852) | UNCLEAR (multi-year) | excluded |
| Mortgage mix 22% (marginal FY27) → 30-35% in ~3 years | 23.2% (P:R282 + P:R283) | UNCLEAR (multi-year) | excluded |
| DA cap 5-7% of AUM | DA restarted (39.95 assigned, R:R355); DA outstanding ND | UNCLEAR | excluded |
| CoB: further −10-15 bps from the rating upgrade | Blended −15 bps; incremental −16 bps (C:R061-R062, C:R058-R059) | DELIVERED | 1.0 |
| Narrow FY27 ranges at Q2/H1 [N L113, L162] | Deck bands verbatim (A3P-14); verbal points for credit cost (~3.5%) and opex (~8.5%) only | PARTIALLY DELIVERED | 0.5 |
| Gross slippage disclosure (deferred twice on the Q1 call; Notion treats the silence as a DROPPED pattern [N L267]) | Not disclosed in results, deck or call (A3-11, A3P-20, A3C-18) | DROPPED (Notion-file convention) | 0 + governance flag |

### 3B. Cumulative track record (trailing 4 concalls)

| Concall Date | Total Commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| Q4 FY26 (maiden; scored at the Q1 review) | ND (prior scoring not passed; Notion grade C, "AUM guidance missed, asset quality delivered" [N L35]) | ND | ND | ND | ND | 0 [N L166] | ND | ND |
| Q1 FY27 (Jul-2026; scored now) | 15 | 3 | 1 | 0 | 0 | 1 | 10 | 3.5 |
| Q2 FY27 (22-Oct-2026) | 24 logged (A3C register C01-C24); scored at the Q3 review | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Credibility Ratio = 3.5 ÷ (15 − 10) = 70.0% → Grade B → Role 1 track-record input "Good"** (codified mapping; five scored commitments). Protocol output unchanged by correction loop 1.

Sensitivity (restated in correction loop 1; the base is thin):
- Protocol-strict reading (slippage was an evasion, never a quantified commitment): 3.5 ÷ 4 = 87.5% → Grade A.
- Opex scored PARTIAL as denominator-assisted (A5 ADV-3): 3.0 ÷ 5 = 60.0% → Grade B at the boundary; one DROPPED, so no downgrade.
- Narrowing promise also scored DROPPED: 3.0 ÷ 5 = 60.0% and two DROPPEDs → automatic one-grade downgrade → Grade C → "Mixed".
- Both (opex PARTIAL and narrowing DROPPED): 2.5 ÷ 5 = 50.0% → Grade C, then two DROPPEDs → automatic one-grade downgrade → Grade D → "Poor".
- The grade ranges A to D on scoring convention alone. A4 records the protocol output (70%, B). The Notion Management Grade (C) changes only by operator action.

DROPPED governance rule: 1 DROPPED in the trailing 4 → no automatic downgrade (needs 2). One more DROPPED (slippage again at Q3, or the narrowing never formalised) triggers it.

### 3C. Pattern recognition
- Management meets or beats ratio guidance (NIM, opex, credit cost on ATA) and holds bands conservatively. Two of those ratio "deliveries" (credit cost, opex) are helped by idle liquidity in the ATA denominator (A4-02, A5 ADV-3).
- Management does not disclose loss-flow numbers: slippage, quarterly write-offs, overlay balance. Three documents running.
- Timelines slip: Bucket 1 recovery moved from November to December inside one call (C:L498-499 vs C:L574); branch openings 0 in H1 against a full-year promise.
- Credibility trend: first scored ratio; trend not computable.

### 3D. Promoter Verdict / Management Grade
- Ratio supports B (protocol output). Notion holds C. No mechanical downgrade fires: no three consecutive misses on one metric; one DROPPED, not two.
- Promoter Verdict (TRUSTWORTHY, management basis): no change proposed. Governance flags carried: CFO untitled and absent from signatures; auditor signed before the board met (A3-18); 6-minute approval (A3-17); slippage non-disclosure pattern.

### 3E. Last quarter's questions
See the prior-question status table in Step 8.5 (33 questions).

---

## STEP 4: Q&A DECOMPOSITION

### 4A. Q&A inventory

| # | Analyst & Firm | Question (1 line) | Category | Response Quality | Substance |
|---|---|---|---|---|---|
| E1 | Name not captured, "ampersand capital" (C:R212, ASR) | Confidence on the AUM top end (30%); ROE path; dilution (C:L248-251, L267-277) | Forward Guidance | B | In range; won't commit to 30% (C:L264-265); ROE high teens/low 20s at 4.5x leverage (C:L273-274); no dilution in two FYs (C:L280-281) |
| E2 | Unidentified (moderator line truncated) | Asset quality under lender stress; cattle; employee additions and productivity (C:L282-288, L323-329) | Financial / Operational | B | Credit cost "closer to 3.5%", exit lower (C:L296-297); cattle 25-28% (C:R111); staff +12-15% budget (C:R113); productivity 4.8 files (C:R117) |
| E3 | "Urban Kumar", firm ASR-garbled (C:R213) | ECL Stage 2 39 → 48 and Stage 3 194 → 197; total ECL ~95?; festive disbursement; fundraising (C:L391-397, L410-411, L429-434) | Financial | C | Basis change explained (overlay now included, C:L401-405); overlay "nearly 45 crores" then a 32 s ASR gap (C:L413-414); the same-basis fall in cover not addressed; October figure unconfirmed |
| E4 | "Winning Akarwal", "Bajaj" (C:R214, ASR) | MFI overlap; AI-ML vs cluster delinquency; UP Bucket 1 falling (C:L453-454, L469-470, L487-490) | Customer / Financial | C | MFI overlap 8-9% / 32% (A on that part); AI-ML answer qualitative only (C:L477-479); UP dip with "not identified any particular reason" (C:L496-497) |
| E5 | Viral Shah, IIFL Capital (host) (C:R215) | Size of insurance mitigation; Bucket 1 stickiness; gold-loan model (C:L522-525, L558-561, L586-590) | Forward Guidance / Strategic | C on the core ask; B on the rest | Offsets sized (opex 50 bps, rate 25 bps, credit 10-25 bps; C:L545-546); the hit itself never sized (A3C-13); Bucket 1 dip attributed to pre-festive cash; gold pilots |
| E6 | Rudraksha Pahija, I-Thought Financial Consulting (C:R216) | Regional caution; plan vs actual; mortgage asset quality (C:L618-619, L638-640, L651) | Operational | B | Microlap tightened in MP and Gujarat; mortgage PAR X +~1 pp to ~6% (C:L652-653); scale-up Q4/Q1 (C:L662-663) |
| E7 | Rahul Kumar, Vaikarya fund (C:R217) | Rural / drought linkage of the book (C:L665-666) | Macro | B | No credit-cost deterioration in past droughts (C:L669-671); no rural branches (C:L676-677). No numbers |
| E8 | "Samir Bisse", firm ASR-garbled (C:R218) | Asset-side repricing; why the NIM band is held (C:L689-690, L714-719) | Financial | B | Pricing power exists, not used (C:L697-698); mortgage book, repeat, rates press yields (C:L724-729); rate sensitivity 3/6 bps; 50 bp case lost to ASR (A3C-20) |
| E9 | "Aditya McClary", firm ASR-garbled (C:R219) | Fixed vs floating; foreclosures; branch expansion (C:L742, L744-745, L761-764) | Operational | B | Asset book fixed-rate only (C:L743); mortgage foreclosures rising (C:L747-748); branch counts inconsistent (A3C-11) |
| E10 | Varun Tube, Share India Securities (C:R220) | Drought cover: NATCAT, CGS, credit life (C:L816-822, L846-848) | Macro / Financial | C | CGS 200-300 cr of ~7,400-7,500 (C:R190, C:R191); credit-life question unanswered or lost (C:L849) |

### 4B. Question pattern analysis
- **Repeated topics:** Bucket 1 CE (E4 and E5: two analysts, so the market did not accept the first answer); drought (E6, E7, E10: three analysts); insurance commission (opening, E5, E8); branch counts (E2 staffing, E9).
- **Topics graded C/D/E:** ECL and overlay (E3), UP Bucket 1 cause (E4), insurance-hit size (E5), AI-ML delinquency (E4), credit-life cover (E10). For a lender, evasion on asset-quality questions inherits the cash-conversion evasion rule. Slippage: evaded on the Q1 call (deferred twice); not asked on the Q2 call. ECL/overlay: partial on the Q2 call. **Two concalls with an incomplete asset-quality answer (Q1 slippage, Q2 overlay amount) = a negative diagnostic for FTTCP lender Transition 3. Flagged for /fttcp.**
- **Buy-side vs sell-side:** best effort, given ASR names. Buy-side likely: Vaikarya fund (E7), a Bajaj entity (E4), "ampersand capital" (E1). Sell-side: IIFL Capital (E5, host), Share India Securities (E10). Consultants: I-Thought (E6). Not a sell-side-only call.
- **Host broker:** Viral Shah asked at Q5, not first, and asked the sharpest sizing question (insurance). Not a softball pattern.
- **Pushback:** E3 followed up on ECL ("Is it like 95 crores approximately?", C:L410-411). E5 followed up for confirmation of "no material impact" (C:L553-555). Light pushback; the ECL topic is contested.

### 4C. The three most important exchanges

**Exchange 1: ECL and overlay (E3)**
- Question (verbatim, C:L391-394): "The ECL provision that you have made, I think in Q1 disclosures you have mentioned it is like 39 crores for stage 2 and 194 crores for stage 3. But in the current disclosures you have increased it to 48 crores and 197 crores. Can you explain that one reason?"
- Response (verbatim, C:L401-409, L413): "The last quarter when we disclosed the ECL provisions, we had not included the management overlays. Now this quarter to make the numbers more transparent, we included the management overlays and we put them into the various stages. So last quarter, we had a management overlay that was built into stage two. That is why it has increased the stage three. ... Yes it is because what we did was we had nearly 45 crores." [32 s audio gap follows]
- Said specifically: the Q1 table excluded overlays; the restated table includes them and spreads them across stages.
- Did NOT say: the overlay balance at 30-Sep; whether any overlay was released through Q2 P&L; why total ECL fell 287 → 274 while gross loans rose 254; why Stage 2 cover fell to 47.44%.
- Implication: the ex-overlay add-gate test can no longer run (A3P-15). The 30-Sep ECL of 274 is about the June ex-overlay level of 275 [4.01% × 6,865, A3P-15], so the overlay looks spent (A3C-01). Q2 PAT quality stays open.
- Follow-up we would ask: Q2 of the Step 8.5 table.

**Exchange 2: Bucket 1 collection efficiency (E4, E5)**
- Questions (verbatim, C:L487-490; C:L558-561): "UP is your second largest A, wherein if I see bucket one connection efficiency, that is continuously it is falling ... What is driving this? Any correction or corrective actions have you taken?" and "the bucket one collection efficiency on a sequential business that is showing some depth. Is that basically more I would say stickiness of the delinquent accounts or is there anything to read over there?"
- Responses (verbatim, C:L491-497; C:L568-575): "in general the bucket one collection has dipped over the last 3-4 months ... At this point of time, we have not identified any particular reason for the dip in UP or other states." and "We would say it is more attributable to the tightening of the cash flows just before the festive season ... the only shift would be this November could become a December".
- Said specifically: a ~5% dip vs April in UP; pre-festive cash tightening; Raksha Bandhan and the Kanwar yatra in August; recovery expected after the festive season.
- Did NOT say: October Bucket 1 CE; the roll rate from Bucket 1 to 30+ DPD; why Rajasthan fell 4.4 pp; why last year's Q1-to-Q2 seasonality went the other way (43.0% → 48.4% [N L343]).
- Implication: the leading indicator for GNPA trigger 1 is weakening with no diagnosed cause, and the recovery date slipped within the call. The seasonal explanation conflicts with last year's pattern.
- Follow-up: Q7 of the Step 8.5 table.

**Exchange 3: credit cost tightened to the floor (E2, E5)**
- Questions (C:L282-288, ASR-garbled; C:L522-525): asset quality under lender stress; quantify the mitigation levers.
- Responses (verbatim, C:L295-299; C:L532-537): "We believe that our credit cost will continue to drop. And we do believe that we will be in that closer to 3.5% and which means that our exit from the year will be even lower than that. That is something that we can see because we are already at 3.82" and "We intend to average around 3.5 plus minus a few basis points for this year. And I think next year, we should see a 10 to 25 basis points improvement for that."
- Said specifically: FY27 average ~3.5%; exit lower; FY28 10-25 bps better.
- Did NOT say: the Q3/Q4 path; the ECL cover assumed; how this squares with Bucket 1 dipping, mortgage PAR X rising and cover already thinner.
- Implication: H2 must run near 3.05% [INFERENCE], about 77 bps below Q2's 3.82%. This is the most testable claim on the call and the basis for Step 8C.
- Follow-up: Q6 of the Step 8.5 table.

---

## STEP 5: NEW INFORMATION AUDIT

### 5A. New disclosures

| Disclosure | Type | Material? | Thesis Impact |
|---|---|---|---|
| Drought states (MH, KA, MP) ~18% of AUM; disbursement moderated in some districts (C:R011, C:L82-87) | Negative surprise / geography | YES | Names a concentration the deck left unsized (A3P-04, A3C-07) |
| Mortgage PAR X +~1 pp in one quarter to ~6%; microlap tightened in MP and Gujarat; scale-up deferred to Q4 FY27 or Q1 FY28 (C:R162, C:R163, C:R224, C:R287) | Negative surprise | YES | Secured-mix lever paused; adverse-selection risk with rising foreclosures (A3C-04) |
| ECL table now includes overlays; Q1 restated (C:R333, C:R334; P:L668-670) | Accounting / disclosure | YES | Ex-overlay credit-cost test lost (A3P-15) |
| MFI overlap 8-9% borrower / 32% household; small-ticket legacy loans at "50-60%" of customers (ASR) (C:R134-R137) | New data (over-lending) | YES | First data for tripwire 8 (A3C-06) |
| Repeat disbursement −16% YoY; new-customer +23% YoY (C:R022, C:R024) | Operational | YES | Growth leans on new borrowers; repeat engine slowing (A3P-16); incremental book less seasoned (A5 ADV-2) |
| Gold-loan pilot branches this FY with new infrastructure (C:R282-R284) | New product | YES (moderate) | New collateral class; opex buffer claimed (C:L609-610) |
| Insurance-commission regulation, FY28 impact, offsets sized at 85-100 bps (C:R255, C:R289) | Regulatory | YES | Fee income headwind of unknown size (A3C-13) |
| Asset book is fixed-rate only (C:R176, C:R344) | Balance-sheet structure | YES | Rising rates squeeze spread until the book reprices |
| Rate sensitivity: ROA −3 bps FY27, −6 bps FY28; 50 bp case unreadable (C:R171-R175) | Sensitivity | Moderate | Small on management's numbers; the 50 bp answer is lost (A3C-20) |
| CGS cover 200-300 cr of the book (C:R190) | Risk transfer | Moderate | Little drought protection |
| 30+ branches in Q3; ~80 incl. splits in FY27 (C:R030, C:R189) | Capacity | YES | Opex step-up in H2 |
| Bank share of borrowing 32% → 35%; ~1,200 cr borrowed in Q2 (C:R131-R133) | Funding | Moderate | Pre-funding; ties to the liquidity build |
| From the filing/deck, not the call: DA restart (R:R084); co-lending book at 19.9% NPL (R:R363-R368); auditor change (R:R574); covenant observation (R:R739); Alpha Wave exit (A3P-12); new CTO and CCO (P:R310, P:R316) | Mixed | YES | Not discussed on the call (5B) |

### 5B. What was NOT discussed

| Expected Topic | Why It Should Have Been Discussed | Significance of Silence |
|---|---|---|
| Gross slippage (add-gate i) | Asked twice at Q1; pre-committed as the single cleanest Q2 metric | RED: third non-disclosure event |
| Write-offs (H1 155.56) | GNPA fell while write-offs ran high | AMBER |
| NCD covenant breach (PAR 90 + write-off)/GLP, second quarter, auditor-qualified | Filed the day before; contradicts the "improving" narrative | RED: thesis tripwire area |
| Bank-lender unwaived covenant count | Tripwire 7 / add-gate iv | AMBER (second call silence) |
| DA gain 10.12 | 62% of the QoQ PAT rise | RED: left out of the profit attribution |
| PCR re-confirmation | Add-gate ii | Routine (filed at 62.42%) |
| Same-basis ECL cover fall (4.17% → 3.85%) | 20% of Q2 PAT to restore | AMBER: only the basis change was explained |
| Refined FY27 guidance | Committed at Q1 | AMBER: verbal points only |
| Alpha Wave exit | >5% holder left | AMBER (supply) |
| CFO status and CTO change | KMP churn AMBER on file | AMBER |
| AGM scrutinizer report (top open item since 17-Sep [N L4]) | Governance tell | AMBER |
| Finance cost on ATA +28 bps vs falling CoB | NIM drag | AMBER |
| Co-lending NPL 19.9% | New disclosure | AMBER |
| Insurance-hit size | Asked directly | AMBER: deflected |
| AI-ML cohort delinquency | Asked directly | AMBER: deflected |
| October disbursement | Asked | AMBER: deflected |
| Credit-life cover in a drought | Asked | Unanswered or lost to ASR |
| Mortgage Stage 3 (+175% YoY at FY26) | Open since the AR review [N L258-261] | AMBER: PAR X given, Stage 3 not |
| Provisional (08-Oct) vs final (21-Oct) GNPA/PAR X/AUM differences (A4-01) | Two filings in two weeks disagree | AMBER |

---

## STEP 6: TONE & SPECIFICITY

### 6A. Tone comparison (prior phrasing from the Notion Q1 log; the Q1 transcript itself was not passed)

| Topic | Prior Concall Phrase | This Concall Phrase | Direction |
|---|---|---|---|
| Credit cost | 3.5-4% "well within grasp" [N L150] | "closer to 3.5% ... exit ... even lower" (C:L296-297) | UPGRADED |
| NIM | Band held; upside conceded [N L149] | "comfortably above"; mix and rates will press yields (C:L184, C:L724-728) | MAINTAINED |
| Macro / weather | "broader macro environment remains uncertain" (Q1 deck, A3P-04) | Drought declared in three states, "not a surprise" (C:L82-84) | DOWNGRADED (risk now named) |
| Collections | Non-OD 99.2-99.3% stable [N L152] | Opening "very good" (C:L153); Q&A "dipped over the last 3-4 months", cause not identified (C:L492-497) | DOWNGRADED |
| Capital runway | No raise ~2-2.5 years [N L155] | "around the next two years" (C:L161-162) | MAINTAINED (shorter) |
| Mortgage | 30-35% "eventually" [N L158] | Microlap tightened; scale-up Q4/Q1 (C:L659-663) | DOWNGRADED |
| Disbursement framing | YoY "+22%" (Q1 deck, A3P-13) | QoQ "+15%" first; YoY +10% second (C:L96-97) | DOWNGRADED (framing) |
| Guidance narrowing | Promised for H1 [N L113] | Bands repeated (C:L202-205) | DROPPED |
| DA | Cap 5-7%, discussed [N L159] | Not mentioned while restarted | DROPPED |

### 6B. Specificity score
Forward statements (A1 FORWARD rows C:R240-R295): 56. Quantified (number, date or binary milestone): 30 (C:R243, R246, R249, R250, R251, R253, R254, R257, R263, R264, R265, R266, R267, R268, R271, R275, R276, R277, R279, R284, R285, R286, R287, R288, R289, R290, R291, R292, R293, R295). Unquantified: 26. **Specificity ratio = 30 / 56 = 0.54: highly specific (just above 0.5).** Much of the specificity restates existing bands.

### 6C. Defensive language count (grep over the full ASR text)
- "we believe" / "I believe" / "we do believe": 9 (C:L86, L295, L296, L313, L381, L498, L527, L532, L661)
- "we expect" / "expecting" (forward): 4 (C:L150, L175, L209, L418)
- "we hope" / "hopefully": 2 (C:L230, L530)
- "evaluating": 1 (C:L227)
- Spoken hedges outside the lexicon: "I wouldn't like to commit now" (C:L265), "it will all depend on" (C:L255-256), "assuming it is implemented" (C:L528): 3
- "take this offline" / "get back to you" / "cannot comment": 0
- **Total 19 (> 5): a hedge-heavy call.** Prior-call count ND (Q1 transcript not passed).

### 6D. Confidence indicators
- Specific numbers: credit cost ~3.5% ± few bps; opex ~8.5% then ~8%; FY28 lever sizes (C:R144-R148, C:R289).
- Dated milestones: 30+ branches in Q3; PAR X < 6.5% by FY end; microlap scale-up Q4/Q1 (C:R246, C:R285, C:R287).
- Misses acknowledged with a recovery plan: Bucket 1 dip (recovery Nov/Dec); mortgage PAR X (branch-level tightening).
- MD (co-founder) answered operational questions directly. No named customer wins (not applicable to this model).

### 6E. Management archetype
Specificity 0.54 (> 0.5) × credibility 70% (≥ 60%, Grade B, n = 5) → **COMMITTED & CREDIBLE (provisional)**. Same label as Q1 [N L4 Key Notes].
Sensitivity (restated in correction loop 1): with opex scored PARTIAL alone (60%, Grade B at the boundary) the label holds. Under the strict scorings in 3B (Grade C at 60% with two DROPPEDs, or Grade D at 50% with two DROPPEDs) the same specificity puts management in the **OVERPROMISER** quadrant. The label rests on one scoring choice. Flagged.

---

## STEP 7: CROSS-REFERENCE

### 7A. Concall narrative vs filing numbers

| Concall Claim | Filing Evidence | Reconciliation |
|---|---|---|
| PAT more than doubled because of lower credit cost and opex (C:L60-63) | PAT +151.1% YoY (R:R180, R:R182). QoQ rise 12.22: DA 7.57 post-tax and an ECL stock fall of 13 pre-tax (Step 4) | PARTIALLY CONFIRMED (true YoY; QoQ attribution omits DA and the ECL fall) |
| Credit cost 3.82%, seventh consecutive improvement (C:L60-61) | 3.82% (P:R389); Rs charge flat QoQ (R:R126-R127); ECL stock −13 | PARTIALLY CONFIRMED (denominator- and release-assisted) |
| Opex ratio down 32 bps to 8.61% (C:L124-126) | 8.61% on ATA (P:R646); rupee opex +2.4% QoQ (R:R132-R146); −14 bps on average AUM [A5 ADV-3] | PARTIALLY CONFIRMED (denominator-assisted) |
| GNPA down seven consecutive quarters to 4.20% (C:L131-132) | 4.20% (R:R402). Three points verifiable: 4.84% (Sep-25) → 4.49% → 4.20% (P:L667-674). H1 write-offs 155.56 (R:R256) | PARTIALLY CONFIRMED (seven-quarter series not in corpus; A4-04) |
| Funding costs continue to ease (C:L163-174) | Blended CoB 10.63% (deck set P:R338); finance cost on ATA +28 bps (P:R797); finance cost +10.8% QoQ (R:R114-R115) | PARTIALLY CONFIRMED (on the CoB metric; contradicted in P&L terms) |
| Collections "very good" (C:L153) | Bucket 1 52.8% vs 54.5% (P:R394-R395); UP Sep 47.6% (P:R472) | CONTRADICTED (trend down; management concedes the dip in Q&A) |
| Balance sheet ready for growth, CRAR 41% (C:L158-159) | 41.01% (R:R405) | CONFIRMED |
| NIM 15.6% (C:L183) | 15.59% (P:R810); −34 bps QoQ as printed (P:R793) unmentioned (ST-1) | CONFIRMED (level); compression not acknowledged |
| AUM per branch 13.3 cr (C:L122) | 7,597 / 571 = 13.30 (P:R074, P:R172) | CONFIRMED |
| RoA 4% in Q2 (C:L196) | 4.04% (P:R846); ex-DA 3.69% [A4 calc] | CONFIRMED (headline includes DA) |
| Drought states ~18% of AUM (C:L85) | Deck map shares are flagged attribution-not-determinable (P:R266). A1's tentative map labels for MH, KA, MP sum to 23.18% (P:R238 7.98, P:R240 7.79, P:R233 7.41) but cannot be relied on | UNVERIFIABLE (possible understatement; QfM Q10) |
| ~1,200 cr borrowed in Q2 (C:L438) | Deck debt raised 1,199.4 (P:R349, chart order) | CONFIRMED (chart-order attribution) |
| Asset quality "stable" (lender check) | PCR −138 bps; cover 4.17% → 3.85%; Stage 2 +Rs7 with cover 58.07% → 47.44%; covenant breach on (PAR 90 + WO)/GLP | PARTIALLY CONFIRMED (headline stable; write-offs and cover tell a weaker story) |

### 7B. Peer concall cross-check
Peer concalls were not passed to this run. **UNVERIFIABLE this run.** Topics to cross-check when available: drought impact in MH/KA/MP; MFI-overlap stress; insurance-commission impact; mortgage foreclosure competition.

### 7C. Concall vs external sources

| Concall Claim | External Source | External Says | Alignment |
|---|---|---|---|
| Funding cost falls on the rating upgrade (C:L168-169) | Rating disclosed in the deck: A+ (Stable), upgraded June 2026 (P:R355, P:R357) | Upgrade confirmed | ALIGNED |
| Asset quality improving | Signal tracker secondary note 22-Oct [S L8]: covenant breach on INE501X07588 | Breach confirmed by the filing (R:R739) | MISALIGNED with the narrative |
| Drought declared in three states (C:L82-83) | IMD / state notifications (not passed) | ND | UNVERIFIABLE |
| Industry stress | The company's own Annexure 3 text: "industry wide stress in Miro Business Loans and MFI Loans" (R:R749) | Sector stress acknowledged in filing | Contradicts "resilient asset quality" framing (C:L88-89) |

---

## STEP 8: THESIS & POSITION (CONCALL)

### 8A. Growth trigger status update

| Trigger | Status Pre-Concall | Concall Evidence | Status Post-Concall |
|---|---|---|---|
| T1 Asset-quality recovery | ON TRACK (GNPA) | Bucket 1 dip with no identified cause; mortgage PAR X +1 pp; incremental tilt to first-time borrowers | WEAKENED |
| T2 Credit cost into band | ON TRACK | Tightened verbally to ~3.5%; ECL basis changed; overlay amount lost | ON TRACK (claim) / WEAKENED (evidence) |
| T3 AUM 25-30% / 28-33% | ON TRACK [N] | Won't commit to 30%; repeat −16%; 0 branches in H1 | WEAKENED |
| T4 RoA 4-4.5% | ON TRACK | "Untouched"; NIM band implies compression; insurance headwind FY28 | WEAKENED |
| T5 Funding cost | ON TRACK | CoB down; bank share up | FIRED |
| T6 Mortgage mix | ON TRACK (medium term) | Microlap tightened; scale-up Q4/Q1 | DELAYED |
| T7 Gold loans | n/a | Pilot branches this FY | NEW |

### 8B. Watchlist items: concall-specific updates

| # | Watchlist Item | This Concall Reading | Status |
|---|---|---|---|
| 1 | GNPA trend | 4.20%, "seven consecutive quarters" (C:L131) | GREEN (series unverified, A4-04) |
| 2 | DA % of income | Not discussed | AMBER (silence) |
| 5 | Credit cost band | ~3.5% FY average promised | GREEN claim / AMBER evidence |
| 6 | PCR | Not discussed | GREEN on filing |
| 7 | Covenants | Not discussed | UNKNOWN |
| 8 | Over-lending | MFI overlap 8-9% / 32% (first data); new-customer +23%, repeat −16% (C:L98-102) | GREEN on the trigger / AMBER on the second reading (A5 ADV-2) |
| P1 | Bucket 1 CE | Dip conceded; cause not identified; recovery Nov/Dec | AMBER |
| P2 | Disbursement growth | Repeat deferral to Q3; October figure deflected | AMBER |

### 8C. Thesis-broken trigger check (concall)

| Thesis-Broken Condition | Threshold | Concall-Relevant Evidence | FIRED? |
|---|---|---|---|
| GNPA up two quarters from 4.49% | Two rises | 4.20%; Bucket 1 dip is the lead risk | NOT FIRED (moved closer in leading indicators) |
| DA > ~4% with PAT dependence | Both | DA not mentioned | NOT FIRED |
| AUM growth < 20% twice | < 20% twice | Range held at 25-30% | NOT FIRED |
| FY27 PAT < Rs270 cr | FY27 audit | No PAT guide | NOT TESTABLE |
| Covenant instances unresolved | Count rises | Not discussed | NOT FIRED (UNVERIFIABLE) |
| Over-lending with rising GNPA | Both | MFI overlap data; GNPA falling | NOT FIRED |

### 8D. Four-Pillar inputs, concall adjustments: DEFERRED to /fttcp and Role 1 (OR-30)
Concall facts flagged for the pillars:
- Pillar 1 (FTTCP ROE forward verdict): RoE "high teens or lower 20s" at 4-4.5x leverage, "gradually" (C:L273-275); no dilution for two FYs (C:L280-281); RoTA 4.0-4.5% "untouched" (C:L556). Re-levering unwinds ~Rs14 cr/qtr of post-IPO funding-mix carry (A5 ADV-1).
- Pillar 2L (Asset-Quality Multiplier): credit cost ~3.5% FY27, FY28 10-25 bps better (C:R147, C:R148); Bucket 1 dip with no identified cause (C:L496); mortgage PAR X +1 pp (C:R162); overlay folded into stages (C:R333); repeat loans perform better on credit cost while the mix tilts to new borrowers (C:L259-260, C:L98-102).
- Pillar 3 (Growth Visibility): AUM top end hedged (C:L265); repeat −16% YoY (C:R024); 30+ branches in Q3 (C:R030); gold pilots (C:R284); 3-year vision repeated (C:R257).
- Strategic Premium: pricing-power claim in hypothecation (C:L705-708), unverified; single-credit rule applies.

### 8E. Position decision (concall overrides checked; Decision Status HELD verified)

| Override | Test | Result |
|---|---|---|
| Credibility ratio below 60% → discount commentary 30-50% | 70% (protocol output); 60% with opex PARTIAL or narrowing DROPPED; 50% with both | Not triggered on the protocol output. Either single scoring choice (opex PARTIAL, or narrowing DROPPED) reaches the 60% boundary; only both together reach 50%, the discount zone |
| Two or more DROPPEDs → automatic grade downgrade | 1 DROPPED | Not triggered |
| Concall reveals undisclosed material risk → trim 25% (held names) | Mortgage PAR X +1 pp, drought exposure ~18%, Bucket 1 dip with no cause. All were disclosed in answers to questions, sized below the company average (mortgage PAR X ~6% vs book 6.94%), and none moves a trigger | A4 judgement: NOT MET. Flagged for the operator, since the conservative reading of this clause is close |
| Concall reveals undisclosed material positive → hold pending verification | None material | n/a |
| Evasion pattern across 3+ quarters | Slippage non-disclosure across three events; call evasion once | Not met mechanically; governance flag |
| Narrative contradicts filing materially → trust the filing | Collections "very good" vs Bucket 1 falling; "funding costs ease" vs finance cost on ATA up; asset quality "resilient" vs covenant reason "higher delinquencies" | YES: trust the filing; note the credibility issue; tighten the Q3 watchlist (Step 8B proposals) |

**Position: HOLD 4% at Rs132. No add, no trim. Decision Status unchanged (HELD); the operator sets it.**

### 8F. Updated questions for the next quarter
The Step 8.5 table (Q1-Q40) is the forward list, with a "What to Watch in Next Concall" column.

### Concall Verdict
- Management Credibility (this quarter): Grade B by ratio (70%, n = 5; range A to D by scoring convention, restated in correction loop 1)
- Trailing 4-Quarter Credibility Ratio: 70.0% (3.5 ÷ (15 − 10)); 60.0% if opex is scored PARTIAL (A5 ADV-3)
- Management Archetype (6E): COMMITTED & CREDIBLE (provisional; OVERPROMISER under the strict scorings)
- Role 1 Track Record Input: Good (mapped from Grade B)
- Net concall impact on thesis: WEAKENED
- Position decision: HOLD
- Source: machine ASR transcript of the 22-Oct-2026 call audio (C:R322). Replace with the official transcript when filed.

---

# SECTION C: COMBINED VERDICT

**Filing-derived signals.** Strong headline: NII +40.1% YoY, PPOP +54.6%, PAT +151.1%, GNPA 4.20%, CRAR 41.01%. The YoY multiples run off the FY26 stress trough, and about Rs14 cr a quarter of the gain is post-IPO funding-mix carry that re-levering unwinds (A5 ADV-1). Weaker quality: Q2 profit rests on a 10.12 DA gain and a 13-crore ECL stock fall that together exceed the QoQ profit rise; the H1 credit charge equals realised losses with zero net reserve build on a book 9.3% larger; PCR −138 bps; total cover 4.17% → 3.85%; a (PAR 90 + write-off)/GLP covenant breach for a second quarter, now auditor-qualified, with a reason that cites "higher delinquencies" this financial year; Rs1,341.66 cr idle liquidity pushing finance cost up faster than income and flattering the ATA-based credit-cost and opex ratios.

**Concall-derived signals.** Credit cost guided to ~3.5% for FY27 (needs H2 ~3.05%); Bucket 1 dip with no identified cause; mortgage PAR X +1 pp; drought states ~18% of AUM; repeat disbursement −16% while new-customer disbursement +23%, so the incremental book is less seasoned (A5 ADV-2); branches start only in Q3; guidance bands repeated, not narrowed; CFO untitled.

**Reconciliation.** Filing and call agree on the headline ratios. They disagree on direction: the call says collections and asset quality are improving; the filing's covenant note, ECL table and write-off identity say losses ran higher in Q2 and reserves were drawn. The filing wins.

**Net thesis impact: WEAKENED (no trigger fired).** Catalyst status (GNPA): ON TRACK. Thesis status: WEAKENED on verification and leading indicators.

**Protocol verdict: PROCEED WITH FLAGS.** Cash conversion INDETERMINATE-WITH-DIRECTION caps the verdict below PROCEED. The adverse findings below are surfaced as flags, and the decision stays with the operator.

**Position decision: HOLD 4% at Rs132 (branch 8A). Add-gate FAILS (leg i bear by non-disclosure; leg iii not met; leg iv unverifiable). Decision Status HELD unchanged.**

Flags:
1. FLAG-ADDGATE: gross slippage undisclosed for the third consecutive event, the pre-committed bear reading; FY27 guidance not refined.
2. FLAG-EARNINGS-QUALITY: DA gain (10.12) + ECL stock fall (13.0) exceed the QoQ PBT rise (18.65); H1 impairment = write-offs + settlements − 0.55.
3. FLAG-COVENANT: auditor-qualified security-cover certificate (para 12); (PAR 90 + write-off)/GLP breach on INE501X07588, second quarter, waived; bank-lender count ND.
4. FLAG-LEADING-INDICATORS: Bucket 1 CE 59.8% → 54.5% → 52.8%; UP Sep 47.6%; mortgage PAR X +1 pp; disbursement +10% YoY.
5. FLAG-KMP: CFO absent from all filing signatures and untitled on the call; CTO replaced.
6. FLAG-PROCESS: 6-minute board approval; security-cover report signed before the board met.
7. FLAG-DATA: ASR transcript; provisional vs final GNPA (4.30% vs 4.20%); Notion GNPA history inconsistent with the deck; deck restatements.
8. FLAG-CASH: INDETERMINATE-WITH-DIRECTION.
9. FLAG-SUPPLY: Alpha Wave India exit; ~50% of equity still with pre-IPO investors (A3P-12).
10. FLAG-SIGNAL-COUNT: tracker holds 2 signals (< 3).
11. FLAG-PRICE-STALE: CMP on file Rs162 (13-Oct-2026), pre-results.
12. FLAG-CREDIBILITY-FRAGILE: ratio 70% on 5 items; 60% if opex is scored PARTIAL (denominator-assisted, A5 ADV-3); range A to D by scoring convention; archetype flips to OVERPROMISER under the strict scorings.
13. FLAG-BASE-EFFECT (A5 ADV-1): YoY core PBT +576.8% runs off the FY26 stress trough; ~Rs14 cr/qtr post-IPO funding-mix carry unwinds on re-levering to 4-4.5x; recurring pool ~73.2 without the ECL draw.
14. FLAG-BORROWER-MIX (A5 ADV-2): incremental lending tilts to first-time borrowers (new +23% YoY, repeat −16%); repeat loans perform better on credit cost per management.

### A4 findings raised in this review

| ID | Classification | Finding | Anchors | QfM |
|---|---|---|---|---|
| A4-01 | AMBIGUOUS | The 08-Oct provisional business update (as recorded on Notion) shows GNPA 4.30%, PAR X 6.88%, AUM 7,604 and Q1 AUM 7,329. The 21-Oct results and deck show GNPA 4.20%, PAR X 6.94%, AUM 7,597 and Q1 AUM 7,324. GNPA improved 10 bps between the two filings while PAR X worsened. | [N L310-313]; R:R402; P:R383; P:R074; P:R073 | Q38 |
| A4-02 | AMBIGUOUS | The disclosed QoQ credit-cost improvement (4.03% → 3.82%) is a denominator effect: the rupee charge rose 0.6% while ATA grew with idle liquidity. On average AUM, 4.53% → 4.39%. The same mechanism applies to opex (A5 ADV-3). | R:R126-R127; P:R388-R389; R:R014, R:R016 | Q6, Q18 |
| A4-03 | FORWARD-SIGNAL | H1 impairment (163.31) equals write-offs (155.56) + settlement loss (8.30) − 0.55 ECL change, exactly. With the deck ECL stock (287 → 274), Q2 write-offs + settlements ≈ 94.90 vs ≈ 68.96 in Q1 [INFERENCE]. Implied Q2 slippage proxy ≈ 86, ≈ 4.6% of average AUM annualised [INFERENCE], above the 4.5% bear line. | R:R129, R:R256, R:R258, R:R250; P:L663, P:L667-668 | Q1 |
| A4-04 | AMBIGUOUS | The deck's 30-Sep-25 table gives GNPA 272/5,615 = 4.84%, consistent with the chart's 4.9% and the call's −70 bps. Notion's GNPA history ("4.21% → 4.77% peak → 4.49%") cannot hold a 4.84% Sep-25 print. Resolves A3C-16 in favour of the filed deck; the Notion series needs correcting. | P:L672-675; P:R109; C:R042; [N L188] | Q38 |

A5 counters grafted in correction loop 1: ADV-1 (Step 2, 4A, 4D, 6.5, 7, 8D), ADV-2 (5L, 6B item 8, 8B item 8, Q33), ADV-3 (3A, 3B, 6E, 7A, 8E, Concall Verdict).

### MONITORABLES / CATALYST LIST (seeded by the A3 commitment registers F6 and Board Outcome F13)

| # | Item | Implied date | Source ref |
|---|---|---|---|
| M1 | Official Q2 FY27 concall transcript (overlay amount, 50 bp scenario, credit-life answer) | ~end-Oct 2026 [INFERENCE: not stated in corpus] | A3C-20; C:L413, L729, L849 |
| M2 | Reg 30 outcome of the "other agenda items" at the 21-Oct board meeting | ND (watch next filings) | R:R613; A3-08 |
| M3 | H1 FY27 RPT disclosure filed with XBRL | date NOT FOUND | R:R614 |
| M4 | INE501X07588 redemption (the breached ISIN), Rs55.22 cr | 17-Nov-2026 | R:R664; R:R528 + R:R532 |
| M5 | Bucket 1 CE recovery "post November", possibly December | Dec-2026 | C:L498-499, C:L574 (C10) |
| M6 | 30+ new branches operational | by 31-Dec-2026 (Q3) | C:R246 (C12) |
| M7 | Deployment of Rs70 cr undeployed NCD balance (INE501X07745) | Q3 FY27 (by 31-Dec-2026) | R:R563, R:R564; A3-07 |
| M8 | INE501X07653 maturity | 31-Dec-2026 | R:R672 |
| M9 | Security creation for Rs455 cr bank/NBFC borrowings | NOT FOUND (lender time limits) | R:R616; A3-06 |
| M10 | Repeat-loan disbursement catch-up | Q3 FY27 | C:R244 (C11) |
| M11 | Q3 FY27 business update (Bucket 1 CE, PAR X, AUM, disbursement) | early Jan 2027 [N L344] | [S L7, L14] |
| M12 | Q3 FY27 results and call (credit cost at constant cover; ECL table; Annexure 3) | ~late Jan 2027 [INFERENCE from Q1 22-Jul and Q2 21-Oct cadence] | Step 8C |
| M13 | One year since listing; UA multiplier gate | ~16-Feb-2027 | R:R638; [N L229] |
| M14 | FY27 guidance close: AUM 25-30%, credit cost ~3.5% avg, opex ~8.5%, NIM band, RoTA 4.0-4.5% | 31-Mar-2027 | P:R637-R641; C:R144, C:R147 |
| M15 | PAR X below 6.5% by FY27 end | 31-Mar-2027 | C:R160 (C08) |
| M16 | Gold-loan pilot branches | by 31-Mar-2027 | C:R284 (C18) |
| M17 | NCD maturities INE501X07661 and INE501X07646 | 20-Mar-2027; 31-Mar-2027 | R:R674; R:R670 |
| M18 | FY27 audited results; PAT ≥ Rs270 cr trigger; FY28 guidance incl. insurance change | ~Apr-May 2027 [INFERENCE] | [N L46]; C:R255 |
| M19 | Microlap (mortgage) disbursement scale-up | Q4 FY27 or Q1 FY28 | C:R287 (C19) |
| M20 | FY28 credit cost 10-25 bps better; opex ~8% | FY28 | C:R148, C:R146 (C03, C05) |
| M21 | Insurance-commission regulation implementation | NOT FOUND | C:L528 (C20) |
| M22 | No fresh equity / no dilution | ~FY29 | C:R106 (C16) |
| M23 | 3-year vision: AUM CAGR 28-33%, RoA 4-4.5%, RoE 17-20%, opex 7-7.5%, credit cost 3.25-3.75% | ~FY29-FY30 | P:R659-R662 |
| M24 | AGM 1-Sep scrutinizer report and dissent % (still open) | overdue | [N L4 Key Notes] |
| M25 | Offer-expense balance Rs22.63 cr resolution | NOT FOUND | R:R618; A3-19 |

---

# PLAIN-LANGUAGE BRIEF

Provenance tiers: FILED (this quarter's results, deck or filing), AGENCY (rating agency), MGMT (management statement, mostly the machine transcript), SECONDARY, INFERENCE (A4 reasoning). "Prior Notion" marks figures carried from the Notion page, not from this quarter's filings.

### 1. SUMMARY NARRATIVE
1. Aye Finance earned Rs86.72 cr in Q2 FY27. That is 151% more than a year ago and 16% more than Q1. [FILED]
2. Bad loans (GNPA) fell to 4.20% from 4.49%. No exit trigger fired. [FILED]
3. The profit is better on the surface than underneath. [INFERENCE]
4. Two items explain more than the whole Rs12 cr profit rise from Q1: a Rs10.12 cr gain from selling loans, and a Rs13 cr fall in loan-loss reserves. [FILED; INFERENCE]
5. Write-offs plus settlement losses ran near Rs95 cr in Q2, against near Rs69 cr in Q1. That helped the bad-loan ratio fall. [INFERENCE from FILED]
6. For the third time, the company did not state how many loans newly went bad. Your rule reads that silence as the bear case. [FILED; prior Notion]
7. Early-warning collections fell again: 52.8% of borrowers 1-30 days late paid up, down from 54.5%. Uttar Pradesh fell to 47.6% in September. Management could not name a cause. [FILED; MGMT]
8. New lending grew only 10% on last year, and more of it went to first-time borrowers. No new branches opened in the half. [FILED; MGMT]
9. A lender covenant on 90-day arrears plus write-offs was breached for a second quarter. The lender waived it. The new auditor now qualifies its certificate on it. [FILED]
10. Management now says credit cost will average about 3.5% this year. That needs the second half near 3.05%, against 3.82% in Q2. [MGMT; INFERENCE]
11. Only one of the four add-gate legs passes. The position stays at 4% at Rs132. Decision Status stays HELD. [prior Notion]
12. The last price on file, Rs162 on 13-Oct, is stale and sits above the Rs148 entry limit. [prior Notion]
13. The next real test is the Q3 result in late January 2027. Credit cost must be 3.3% or lower with reserves held. [INFERENCE]

### 2. SECTOR INTELLIGENCE
- Segment: unorganised micro-enterprises with Rs30 lakh to Rs1 cr turnover and no financial documents (P:R273, P:R276) [FILED, this quarter]. Management calls it under-penetrated (C:L53-54) [MGMT].
- Credit cycle: the industry over-lent in 2024-25. 95% of Aye's book was written after June 2024 (P:R433) [FILED]. The company's own covenant note still cites "industry wide stress in Miro Business Loans and MFI Loans" (R:R749) [FILED]. The stress phase is not over in the filing's own words.
- Weather: drought declared in parts of Maharashtra, Karnataka and Madhya Pradesh, about 18% of AUM (C:R011) [MGMT, ASR]. The deck does not size this exposure [FILED: not disclosed].
- Rates: rising; a 25 bp rise has already happened (C:L733-734) [MGMT]. Aye's loans are all fixed-rate (C:R344) [MGMT], so a rate rise squeezes spread until the book turns over. Funding cost still fell, helped by the June 2026 upgrade to A+ (Stable) (P:R355, P:R357) [FILED; AGENCY rating as reported in the deck].
- Regulation: a prospective change to insurance commissions hits fee income from FY28 (C:L217-220) [MGMT]. Size not disclosed.
- Risk transfer: credit-guarantee cover is only Rs200-300 cr of a ~Rs7,500 cr book (C:R190, C:R191) [MGMT, ASR].
- Market size: Notion rates the runway STRONG, with a 3-year SOM of Rs12,140 cr (18.3% implied CAGR) [prior Notion].
- Not disclosed: industry PAR or credit-cost benchmarks. Management's "better than market" claims (C:L502, C:L578-580) are unverified.

### 3. BUSINESS-MODEL INTELLIGENCE
- How it earns: average yield 22.3% (P:R099); blended cost of borrowing 10.63% (C:R061); NIM 15.59% of average assets (P:R810) [FILED / MGMT]. Part of today's NIM comes from low post-IPO leverage, which the planned re-levering will reverse (C:L272-274) [MGMT; INFERENCE].
- What it spends: opex 8.61% (P:R646) and credit cost 3.82% (P:R389) of average assets, leaving RoA 4.04% (P:R846) [FILED]. Idle cash in the asset base flatters both cost ratios [INFERENCE].
- What it lends: 76.8% hypothecation loans, unsecured or partly secured on business assets, average ticket Rs1.6 lakh; 21.8% loan against property and 1.4% small property loans (P:R284, P:R288, P:R294, P:R282, P:R283) [FILED].
- How it runs: 571 branches, 6.9 lakh borrowers, in-house sourcing and collection, 68% cluster underwriting and 32% AI-ML (P:R172, P:R176, P:R568, P:R567) [FILED].
- Drift this quarter:
  - Growth leaned on new borrowers (+23% disbursement) while repeat loans fell 16% (C:R022, C:R024) [MGMT]. Management says repeat loans have lower credit cost (C:L259-260) [MGMT].
  - The shift to secured lending stalled: mortgage share 23.2%, and the small-mortgage product was tightened after its arrears rose about 1 point (C:R162, C:R163) [FILED / MGMT].
  - Loan sales restarted: Rs39.95 cr sold for a Rs10.12 cr gain (R:R355, R:R084) [FILED].
  - Cash and bank rose to 15.3% of assets [FILED, A4 calc], so borrowing cost now grows faster than interest income [FILED].
  - Gold loans are planned with new branch premises (C:L597-599) [MGMT]: a new collateral type and a new cost line.
- Prior Notion context: lender cash flow is structurally negative; RoE reaches the high teens only at 4-4.5x leverage [prior Notion; C:L273-274 MGMT].

### 4. COMPETITION INTELLIGENCE
- The deck names three competitor classes: microfinance lenders, banks/NBFCs/fintechs, and micro-LAP lenders (P:R268) [FILED].
- Where Aye wins: management claims pricing power and no real competition in hypothecation loans (C:L705-708) [MGMT, unverified]. Its edge rests on cluster underwriting built since 2014 and on in-house collections [FILED].
- Where Aye is weaker: in mortgages, foreclosures are rising and management admits competition (C:L747-755) [MGMT]. 32% of households also carry microfinance loans (C:R135) [MGMT, ASR]. Most of the book is unsecured, so losses per default are high.
- Named listed peers [INFERENCE: the peer set is not on the Notion page or in this corpus; no peer figures are used]: Five-Star Business Finance and SBFC Finance (secured small-business lending), Ugro Capital (MSME lending), CreditAccess Grameen (microfinance, borrower overlap). Peer calls were not passed, so the cross-check is UNVERIFIABLE this run.
- Risk to watch: better mortgage borrowers refinancing out (A3C-04), and microfinance stress spreading through shared households.

### 5. FORWARD MAP (next ~10-11 months)
Make-or-break next reading: **Q3 FY27 results, about late January 2027.** Bull: credit cost 3.3% or lower with total reserve cover at or above 3.85%. Bear: credit cost above 3.82%, or cover below 3.85% for a second quarter.

| Date | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| ~end-Oct 2026 | Official Q2 transcript | Overlay figure shows the Rs13 cr reserve fall was a reclassification | Confirms reserves were released into profit |
| 17-Nov-2026 | Breached NCD (INE501X07588) redeems | Breach leaves with it; no other deed breached at Q3 | Same arrears-plus-write-off clause breaks on another deed |
| Nov-Dec 2026 | Festive season; promised Bucket 1 recovery | Recovery shows in December | No recovery; the seasonal story fails |
| 31-Dec-2026 | 30+ branches open; Rs70 cr NCD balance deployed | Disbursement steps up | Branch cost lands without volume |
| Early Jan 2027 | Q3 business update | Bucket 1 CE 54.5% or higher, PAR X below 6.94% | Bucket 1 CE 52.8% or lower with PAR X rising (tracker falsifier) |
| Late Jan 2027 | Q3 results | See make-or-break above | See make-or-break above |
| ~16-Feb-2027 | One year since listing; UA gate | Qualifiers evidenced | More pre-IPO exits add supply |
| 31-Mar-2027 | FY27 close vs guidance | AUM growth 25-30%, credit cost near 3.5%, PAR X below 6.5% | AUM growth slides toward 20% with disbursement still near 10% |
| ~Apr-May 2027 | FY27 audited results; FY28 guidance | PAT Rs270 cr or more with loan-sale gains under 4% of income | PAT below Rs270 cr, or carried by loan-sale gains |
| Q4 FY27 to Q1 FY28 | Mortgage scale-up | Mortgage arrears back below ~6% and growth resumes | Scale-up postponed again |
| ~Jul-Sep 2027 | Q1 FY28 results; FY27 annual report under the new auditor | Write-offs fall per rupee of book; covenant instances drop | Write-off rate rises; more covenant instances |

```yaml
stage: A4-analyst
company: "AYE"
quarter: "Q2 FY27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, concall, presentation]
ledger_reconciliation:
  notes: 12
  turns: 26
  slides: 44
  all_reviewed: true
  a3_findings_incorporated: ["A3-01","A3-02","A3-03","A3-04","A3-05","A3-06","A3-07","A3-08","A3-09","A3-10","A3-11","A3-12","A3-13","A3-14","A3-15","A3-16","A3-17","A3-18","A3-19","A3-20","A3-21","A3-22","A3-23","A3-24","A3-25","A3-26","A3-27","A3P-01","A3P-02","A3P-03","A3P-04","A3P-05","A3P-06","A3P-07","A3P-08","A3P-09","A3P-10","A3P-11","A3P-12","A3P-13","A3P-14","A3P-15","A3P-16","A3P-17","A3P-18","A3P-19","A3P-20","A3C-01","A3C-02","A3C-03","A3C-04","A3C-05","A3C-06","A3C-07","A3C-08","A3C-09","A3C-10","A3C-11","A3C-12","A3C-13","A3C-14","A3C-15","A3C-16","A3C-17","A3C-18","A3C-19","A3C-20"]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "HELD (4% at Rs132; Entry Max Rs148, MoS Rs118; CMP on page Rs162 13-Oct-2026, stale)"
position_branch: "8A"
sc_gap_pat_pct:
  - {period: "Q2 FY27", gap: "N.A. - no consolidated results filed; Trust inside statement 0.14% of PAT (0.12/86.72)"}
  - {period: "H1 FY27", gap: "N.A. - no consolidated results filed; Trust inside statement 0.29% of PAT (0.47/161.22)"}
  - {period: "Q1 FY27", gap: "N.A. - no consolidated results filed; Trust share ND"}
questions_for_management:
  - {q: "Gross slippage into Stage 3 in Q1 and Q2 FY27 (Rs cr); filing implies Q2 write-offs+settlements ~95 vs ~69 in Q1", from_finding_id: "A3-11, A3P-05, A3P-20, A3C-18, A4-03"}
  - {q: "Overlay balance at 30-Jun and 30-Sep; how much of the Rs13 cr ECL fall (287 to 274) went through Q2 P&L", from_finding_id: "A3C-01, A3P-15, A3P-05"}
  - {q: "INE501X07588 (PAR90+WO)/GLP covenant threshold and actual; which delinquency rose this FY", from_finding_id: "A3-03"}
  - {q: "Bank-lender unwaived covenant count at 30-Sep; any deed needing 1.10x cover (computed 1.091x)", from_finding_id: "A3-15, A3-03"}
  - {q: "Q2 ROA ex the Rs10.12 cr DA gain; is DA a planned H2 lever", from_finding_id: "A3-13, A3P-07, A3C-02"}
  - {q: "FY27 credit cost ~3.5% needs H2 ~3.05% and Q2 charge was flat in rupees; what Q3 credit cost (Rs and ratio) does the plan assume", from_finding_id: "A3C-08, A4-02"}
  - {q: "Share of Sep Bucket 1 accounts rolling to 30+ DPD in Oct", from_finding_id: "A3P-06, A3C-03"}
  - {q: "Mortgage PAR X, Stage 3 and foreclosure rate for the last four quarters", from_finding_id: "A3C-04"}
  - {q: "FY27 mortgage share assumed and Q2 ML disbursement", from_finding_id: "A3P-02"}
  - {q: "MH/KA/MP AUM share, Bucket 1 CE and PAR X at 30-Sep", from_finding_id: "A3P-04, A3C-07"}
  - {q: "Cattle AUM in drought districts and guarantee cover there", from_finding_id: "A3C-07, A3C-19"}
  - {q: "Will FY27 bands be formally narrowed as committed at Q1", from_finding_id: "A3P-14"}
  - {q: "Does the NIM band imply H2 NIM ~12.6-13.6%, and how is RoTA 4.0-4.5% then reached", from_finding_id: "A3C-10, A3P-14"}
  - {q: "October 2026 disbursement", from_finding_id: "A3P-13, A3C-14"}
  - {q: "Q3 repeat-loan disbursement growth YoY", from_finding_id: "A3C-14, A3P-13"}
  - {q: "Are splits counted in 571 branches; how many new branches operating by 31-Dec-2026", from_finding_id: "A3C-11, A3P-10, A3C-09"}
  - {q: "New branches assumed for the 28-33% 3-yr CAGR given ~Rs4,408 cr existing headroom", from_finding_id: "A3P-01"}
  - {q: "Deployment date for Rs1,341.66 cr liquidity; finance cost on ATA +28 bps vs CoB -15 bps", from_finding_id: "A3-14, A3P-08, A3C-05, A4-02"}
  - {q: "Use and timing of undeployed Rs70 cr of INE501X07745", from_finding_id: "A3-07"}
  - {q: "Expiry of lender time limits for Rs455 cr borrowings without security", from_finding_id: "A3-06"}
  - {q: "Was the Q1 auditor's Excel-based charge allocation point fixed", from_finding_id: "A3-05"}
  - {q: "Co-lending Rs53.31 cr book: product, share, ECL held vs 19.9% NPL", from_finding_id: "A3-12"}
  - {q: "Is Gaurav Seth CFO/KMP at 22-Oct-2026; why CS signed all Q2 filings", from_finding_id: "A3-16, A3C-15, A3P-09"}
  - {q: "Was the CTO change a replacement, and why", from_finding_id: "A3P-09, A3C-15"}
  - {q: "Was SSKM to MSKA only the RBI-mandated rotation", from_finding_id: "A3-24"}
  - {q: "Why was the security-cover report signed 11:09:12, before the 11:15 board start", from_finding_id: "A3-18"}
  - {q: "Other agenda items after the 6-minute approval; Reg 30 outcome", from_finding_id: "A3-08, A3-17"}
  - {q: "Hedge accounting designation date, hedged items, MTM now in OCI", from_finding_id: "A3-01"}
  - {q: "Arcil SR carrying value and provision held", from_finding_id: "A3-02"}
  - {q: "Which actuarial assumption caused the H1 Rs5.36 cr loss", from_finding_id: "A3-09"}
  - {q: "EPS denominator; Trust-held treasury shares", from_finding_id: "A3-10"}
  - {q: "Rs22.63 cr unutilised offer expenses: revision and return to proceeds", from_finding_id: "A3-19"}
  - {q: "Share of borrowers with 2+ unsecured lenders; Bucket 1 and PAR X for MFI-overlap vs rest and for new-to-Aye vs repeat cohorts", from_finding_id: "A3C-06, A5 ADV-2"}
  - {q: "Insurance-commission income FY26 and H1 FY27 (Rs cr, bps of ATA)", from_finding_id: "A3C-13, A3P-07"}
  - {q: "Q2-only tele-caller productivity and foreclosure rate", from_finding_id: "A3P-16"}
  - {q: "Any portfolio purchased in H1; where purchased DA AUM is reported", from_finding_id: "A3P-17"}
  - {q: "Alpha Wave India exit and other pre-IPO holders' sale plans", from_finding_id: "A3P-12"}
  - {q: "Eight quarterly GNPA prints; why provisional 4.30%/6.88%/7,604 became 4.20%/6.94%/7,597", from_finding_id: "A3C-16, A4-01, A4-04"}
  - {q: "PAR 30 at 12 months on book, AI-ML vs cluster underwriting", from_finding_id: "A3C-19"}
  - {q: "Gold loans: board approval date, pilot branch count, capex", from_finding_id: "A3C-12"}
monitorables:
  - {item: "Official Q2 transcript (overlay amount, 50 bp scenario)", implied_date: "~end-Oct 2026 (inferred)", source_ref: "A3C-20"}
  - {item: "Reg 30 outcome of other board agenda items", implied_date: "ND", source_ref: "R:R613; A3-08"}
  - {item: "H1 FY27 RPT disclosure with XBRL", implied_date: "NOT FOUND", source_ref: "R:R614"}
  - {item: "INE501X07588 redemption (breached ISIN), Rs55.22 cr", implied_date: "2026-11-17", source_ref: "R:R664"}
  - {item: "Bucket 1 CE recovery post Nov / Dec", implied_date: "2026-12", source_ref: "C:L498-499, C:L574"}
  - {item: "30+ new branches operational", implied_date: "2026-12-31", source_ref: "C:R246"}
  - {item: "Deploy Rs70 cr NCD balance INE501X07745", implied_date: "Q3 FY27", source_ref: "R:R563-R564; A3-07"}
  - {item: "INE501X07653 maturity", implied_date: "2026-12-31", source_ref: "R:R672"}
  - {item: "Security creation for Rs455 cr borrowings", implied_date: "NOT FOUND", source_ref: "R:R616; A3-06"}
  - {item: "Repeat-loan disbursement catch-up", implied_date: "Q3 FY27", source_ref: "C:R244"}
  - {item: "Q3 FY27 business update (Bucket 1 CE, PAR X, disbursement)", implied_date: "early Jan 2027", source_ref: "[N L344]; [S]"}
  - {item: "Q3 FY27 results: credit cost at constant ECL cover (single cleanest metric)", implied_date: "~late Jan 2027 (inferred)", source_ref: "Step 8C"}
  - {item: "One year since listing; UA gate", implied_date: "~2027-02-16", source_ref: "R:R638; [N L229]"}
  - {item: "FY27 guidance close (AUM 25-30%, credit cost ~3.5%, opex ~8.5%, RoTA 4.0-4.5%)", implied_date: "2027-03-31", source_ref: "P:R637-R641; C:R144, C:R147"}
  - {item: "PAR X below 6.5% by FY end", implied_date: "2027-03-31", source_ref: "C:R160"}
  - {item: "Gold-loan pilot branches", implied_date: "2027-03-31", source_ref: "C:R284"}
  - {item: "NCD maturities INE501X07661 / INE501X07646", implied_date: "2027-03-20 / 2027-03-31", source_ref: "R:R674; R:R670"}
  - {item: "FY27 audited results; PAT >= Rs270 cr trigger; FY28 guidance", implied_date: "~Apr-May 2027 (inferred)", source_ref: "[N L46]"}
  - {item: "Microlap scale-up", implied_date: "Q4 FY27 or Q1 FY28", source_ref: "C:R287"}
  - {item: "FY28 credit cost 10-25 bps better; opex ~8%", implied_date: "FY28", source_ref: "C:R148, C:R146"}
  - {item: "Insurance-commission regulation implementation", implied_date: "NOT FOUND", source_ref: "C:L528"}
  - {item: "No fresh equity / no dilution", implied_date: "~FY29", source_ref: "C:R106"}
  - {item: "3-yr vision: AUM CAGR 28-33%, RoA 4-4.5%, RoE 17-20%", implied_date: "~FY29-FY30", source_ref: "P:R659-R662"}
  - {item: "AGM 1-Sep scrutinizer report and dissent %", implied_date: "overdue", source_ref: "[N L4]"}
  - {item: "Offer-expense balance Rs22.63 cr", implied_date: "NOT FOUND", source_ref: "R:R618; A3-19"}
flags:
  - "FLAG-ADDGATE: gross slippage undisclosed third consecutive event (pre-committed bear reading); FY27 guidance not refined; add-gate fails (1 of 4 legs passes)"
  - "FLAG-EARNINGS-QUALITY: DA gain 10.12 + ECL stock fall 13.0 exceed QoQ PBT rise 18.65; H1 impairment = write-offs + settlements - 0.55"
  - "FLAG-COVENANT: auditor-qualified security-cover certificate; (PAR90+WO)/GLP breach on INE501X07588, 2nd quarter, waived; reason cites higher delinquencies; bank count ND"
  - "FLAG-LEADING-INDICATORS: Bucket 1 CE 59.8 -> 54.5 -> 52.8%; UP Sep 47.6%; mortgage PAR X +1pp; disbursement +10% YoY"
  - "FLAG-KMP: CFO absent from all filing signatures and untitled on call; CTO replaced"
  - "FLAG-PROCESS: 6-minute approval; security-cover report signed before board start"
  - "FLAG-DATA: ASR transcript; provisional vs final GNPA 4.30 vs 4.20; Notion GNPA history inconsistent with deck (A4-04)"
  - "FLAG-CASH: INDETERMINATE-WITH-DIRECTION"
  - "FLAG-SUPPLY: Alpha Wave India left >5% list"
  - "FLAG-SIGNAL-COUNT: tracker has 2 signals (<3); 4 Case B candidates proposed as payload"
  - "FLAG-PRICE-STALE: CMP Rs162 (13-Oct-2026) pre-results"
  - "FLAG-CREDIBILITY-FRAGILE: protocol ratio 70% (B) on 5 items; 60% if opex scored PARTIAL (denominator-assisted, A5 ADV-3); range A to D by scoring convention; archetype flips to OVERPROMISER under strict scorings"
  - "FLAG-BASE-EFFECT (A5 ADV-1): YoY core PBT +576.8% runs off the FY26 stress trough; ~Rs14 cr/qtr post-IPO funding-mix carry unwinds on re-levering to 4-4.5x; recurring pool ~73.2 ex ECL draw"
  - "FLAG-BORROWER-MIX (A5 ADV-2): incremental lending tilts to first-time borrowers (new +23% YoY, repeat -16%); repeat loans perform better on credit cost per management"
plain_language_brief_included: true
analyst_note: "Correction loops 1-2 applied (A5 ADV-1..3; R1-1, R1-2, R1-S1, R1-S4); verdict, protocol grade and position unchanged. Headline Q2 is strong and no trigger fired, so HOLD 4% stands and the add-gate fails. The review leans bear on quality. H1 impairment 163.31 equals write-offs 155.56 plus settlements 8.30 minus a 0.55 ECL change, exactly. The deck ECL stock fell 287 to 274 in Q2 while gross loans rose 254, so Q2 write-offs ran near 95 vs 69 in Q1 [inference]. The DA gain plus that ECL fall exceed the whole QoQ PBT rise. Slippage stayed undisclosed a third time, the Notion bear reading; an implied proxy is near 4.6% of average AUM. Bull counter: NII +40%, H1 realised losses +10% YoY on a 27% larger book, CoB down. But YoY core PBT +577% runs off the FY26 trough, and ~Rs14 cr/qtr is post-IPO funding mix that re-levering unwinds. Incremental lending tilts to first-time borrowers. The 70% credibility ratio rests on five items and swings A to D on scoring; opex delivery is denominator-assisted. Notion's GNPA history conflicts with the deck's Sep-25 4.84%. The concall is ASR."
review_path: "runs/aye-q2fy27/work/review_aye_q2fy27.md"
```
