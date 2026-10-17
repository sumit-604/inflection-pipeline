# A3 FORENSIC NOTES: POONAWALLA (Poonawalla Fincorp Limited), q2fy27, doctype: results (Reg 30/33/51/52 Board Outcome, 30 pages)

Stage: A3-forensics | Model: claude-opus-5-5 | Date: 2026-10-17
Inputs read: A1 structured (R001-R1327, all rows), A1 fulltext (lines 1-1765, all lines), A2 ledger (all T1-T8 rows incl. M001-M006).
Not supplied: prior-quarter fulltext (ND), Notion monitoring checklist (NONE; pre-thesis read, no companies/ file, no spear on record).
Source PDF and inputs/ were not opened.
Lender name (NBFC). The 1L/5L lender variants in frameworks/Quarterly_Results_Review_Protocol_v1_4.md govern downstream analysis. Every computation below is shown for standalone (S) and consolidated (C).
Quote convention: verbatim from the fulltext at the cited line, with runs of whitespace collapsed to one space. OCR glyphs are kept as printed.
Units: Rs crore unless stated. Page 20-21 figures are Rs million (x0.1 to get crore). Page 24-25 figures are absolute rupees.

## 0. LEDGER RECONCILIATION

| Item | Count | Read at cited line | Status |
|---|---|---|---|
| Structured row IDs referenced by ledger | 1327 | 1327 | 100% |
| T8 MISSING_FROM_STRUCTURED units (M001-M006, lines 81, 159, 168, 228, 572, 1488) | 6 | 6 | 100% |
| Ledger units with no structured row (AUDC2, AUDC5, AUDS0-AUDS2, AUDK3, AUDK4, AUDK7, AUDK8, AUDK10, AUDK12, FN02, ENC3) | 13 | 13 (by line range) | 100% |

ledger_reconciled_pct: 100.

OCR_SUSPECT values cross-footed before use (all tie):
- R021 "2,4 l 5.54" = 2,415.54. C Q2 revenue foots: 2,415.54 + 0.95 + 207.47 + 0.54 + 0 = 2,624.50 (line 297).
- R118 "I 14.71" = 114.71. C Q1 tax: 114.71 - 0.19 - 10.97 = 103.55 (line 313).
- R133 "I 24.47" = 124.47. C FY26 tax: 57.34 - 0.01 + 124.47 = 181.80.
- R509 "16.5?" = 16.52. S H1 FY26 tax: 29.01 + 16.52 = 45.53.
- R150 "(177)" = (1.77) (matches S R527). R161 "(118)" = (1.18) = (1.91) + 0.73.
- R232 loans 69,562.71: C financial-asset subtotal foots to 73,635.12 (line 368).
- R260 / R619 total assets 74,583.94 (C) / 74,533.26 (S): both foot to total liabilities and equity.
- R288 / R647 other equity 13,577.95 (C) / 13,527.27 (S): share capital 176.12 + other equity = net worth in Reg 52(4) (line 997).
- R974 "121•1." = 121%: 5.82 / 4.81 = 1.210.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F1-1 | F1 | LI7_296 (R045), LI13_648 (R423), NS11a (R744-R750) | 296, 648, 874-876 | "(e) Net gain on derecognition of financial instruments - 50.93 34.82 50.93 97.50 216.83"; "Retention of beneficial economic interest (MRR) - 10%" | FORWARD-SIGNAL | Q2 has no assignment gain. The 1,000.34 Cr direct assignment (15,883 accounts) sits wholly in Q1, and the MRR quarter cell is a dash. Q1 gain 50.93 = 12.4% of Q1 PBT 411.26. FY26 gain 216.83 = 30.0% of FY26 PBT 723.61. The line is the lender's lumpy upfront-income channel. A restart in H2 lifts reported PBT by tens of crore per quarter without any change in the run-rate. A4 question: is DA a planned funding tool for H2 FY27, and at what volume? |
| F1-2 | F1 | AUDC6 (R012-R015), FN01 (R1226), LI8_379 (R258-R259), LI14_734 (R617-R618) | 239, 226, 379, 734 | "share of net profit after tax of ~ Nil and ~ Nil"; C "Assets held for sale 50.70 50.70"; S "Assets held for sale 0.02 0.02" | FORWARD-SIGNAL | The JV-share line exists because JASPL is still in scope, held for sale. It anticipates a gain or loss on sale of a JV. S carries JASPL at 0.02 Cr, C at 50.70 Cr. The 50.68 Cr gap (accumulated equity-method share up to 13 Dec 2021) is the only S-vs-C difference in the group. On completion, S books a gain on any price above 0.02 Cr. C books a gain or loss against 50.70 Cr. That will be the first S-vs-C P&L divergence. Consideration NOT FOUND. |
| F4-1 | F4 | AUDS5 (R388-R393, R1255-R1257), ENT02, LI9_451 (R346-R347), LI15_809 (R705-R706) | 580-584, 451, 809 | "PFL Employee Welfare Trust ('Welfare Trust') which has not been reviewed by other auditor"; "Sale by PFL Employee Welfare Trust (treasury shares) 227.66 3.54" | AMBIGUOUS | PAT test passes. The unreviewed share of PAT is Nil for the trust and ~Nil for the JV (0% of S and C PAT, below the 10% bar). Scope test fails on activity. The unreviewed trust drove a 227.66 Cr treasury-share sale in H1 FY27 against 3.54 Cr in H1 FY26 (a 64x jump). That is 33.4% of H1 PAT 682.56 and 1.7% of S net worth, booked straight to equity. The auditor reports the trust only as "cash flows (net) of ~ 0.15 crores" (line 584). A4 questions: buyer and price of the treasury shares (market sale or ESOP exercise)? Shares the trust still holds? Was a trust audit planned? |
| F5-1 | F5 | AUDC7 (R1002, R1125-R1130, R1230-R1231), AUDS6 (R1152-R1154, R1258) | 249-257, 598-607 | "reviewed by Kirtane & Pandit LLP, one of the previous joint auditors of the Company, whose report dated 17 July 2026" | AMBIGUOUS | New language this quarter. The joint-auditor pair changed between 17 July 2026 (K&P's Q1 FY27 review) and 09 Oct 2026. The other predecessor joint auditor is not named, so we cannot tell which of MSKA / B K Khare is new. No EoM and no Going Concern language in either LRR. Other-matter scope (JV ~Nil; trust 0.41 Cr assets) cannot be verbatim-diffed against Q1: prior-quarter text not supplied. The filing gives no reason for the change and no appointment date. The FY27 year-end audit will be the new pair's first audit of ECL and write-off policy. A4 questions: reason for the change, appointment date and approving body, and whether any review-procedure differences arose on the Q1 comparatives. |
| F6-1 | F6 | NC9 (R1100-R1102, R1146-R1148, R1251), NS9 (R1104-R1105, R1170-R1172, R1277), ENT01 | 509-513, 858-861, 226-227 | "has received regulatory approval and is expected to be completed in due course"; "equity method accounting has been discontinued with effect from 13 December 2021" | FORWARD-SIGNAL | Undated commitment, now in its fifth year. Sale approved 2 Nov 2021 and 13 Dec 2021, reaffirmed 05 May 2026. Status word moved to regulatory approval received. Held-for-sale classification has run about 4.8 years against Ind AS 105's normal one-year completion expectation. If the sale falls through, the classification reverts. If it completes below 50.70 Cr, C takes a write-down. A4 questions: closing date, counterparty and price; when the regulatory approval was received; and the Ind AS 105 basis for keeping the classification past 12 months. |
| F8-1 | F8 | LI7_311 (R123-R127), LI13_663 (R501-R504) | 311, 663 | "- Earlier period/year (0 19) - (0 19) - (0.01)" | NEUTRAL-FACT | Non-zero earlier-year tax: Q1 FY27 (0.19) and FY26 (0.01), both credits, same in S and C. Immaterial: 0.05% of Q1 PBT. ETR S = C: Q2 FY27 25.22%, Q1 25.18%, Q2 FY26 24.97%, H1 FY27 25.20%, H1 FY26 24.97%, FY26 25.12%. All sit at the statutory 25.17%. No ETR step-up risk. |
| F8-2 | F8 | LI7_312 (R128-R133), LI13_664 (R505-R510), LI8_371 (R242-R243), LI9_445 (R336-R337) | 312, 664, 371, 445 | "(b) Deferred tax (13.36) (10.97) 8.96 (24.33) 16.52 I 24.47"; "Income taxes paid (net of refund s) (148.34) (53.40)" | AMBIGUOUS | Deferred-tax sign flip. FY26 was a 124.47 charge (68% of FY26 tax; current tax only 57.34). H1 FY27 is a 24.33 credit, a 267 bps shield on H1 PBT. The current-tax rate is 27.89% against a book ETR of 25.20%. DTA net 72.70 to 91.16 ties exactly: 72.70 + 24.33 - 6.28 + 0.41 = 91.16. Cash taxes rose 2.8x (148.34 vs 53.40). The shield is a timing build, not a future ETR step-up. A4 question: which temporary difference drives the build (ECL provisions running ahead of write-offs?), and is the FY26 DTA draw-down finished? |
| F9-1 | F9 | LI7_317 (R146-R151), LI13_669 (R523-R528) | 317, 669 | "Remeasurements of the defined benefit plans 1.04 (2.66) 0.36 ( 1.62) (177) (2.04)" | NEUTRAL-FACT | Rule trigger. The Q1 FY27 actuarial loss (2.66) exceeds the full FY26 loss (2.04). Q2 then reversed by +1.04. Amounts are immaterial (0.9% of Q1 PAT). Verify the discount-rate and plan-asset assumptions at the FY27 Annual Report. |
| F9-2 | F9 | LI7_326 (R164-R169), LI13_676 (R541-R546), LI8_362 (R228-R229) | 326, 362 | "34.07 (7.93) 12.00 26.14 (8.20) 35.12"; "Derivative financial instruments 399.5 6 340.26" | AMBIGUOUS | The Q2 cash-flow-hedge OCI gain of 34.07 equals 97% of the full FY26 gain (35.12). Derivative assets rose 340.26 to 399.56. A cash-flow hedge reserve points to hedged foreign-currency or floating-rate borrowings. The hedged notional and currency are NOT FOUND in this filing. A4 question: size and tenor of the hedged borrowings (ECB?), and the hedge-reserve recycling profile. |
| F10-1 | F10 | LI7_339 (R206-R211), LI13_683 (R565-R570), NC6/NS6 (R378, R737), NC7/NS7 (R380-R383, R738-R740), LI9_451 | 339, 683, 493, 497-498, 451 | "Paid-un eauity share canital (Face value on' 2 each) 176.12 175.1 6 161.49 176.12 161.49 161.59"; "allotted 353, 113 fully paid up equity shares" | AMBIGUOUS | Paid-up capital rose 14.53 Cr in H1 (161.59 to 176.12; S = C). Notes explain 13.56 Cr: QIP 67,430,883 x Rs 2 = 13.49, plus ESOP 353,113 x Rs 2 = 0.07. Residual 0.97 Cr = about 4.87 million Rs 2 shares, almost all of it in Q2 (Q2 rise 0.96 Cr). Candidate reconciling item: treasury shares released by the Welfare Trust (227.66 Cr, line 451). [INFERENCE] If the whole residual is treasury release, the implied price is about Rs 468 a share. Basic vs diluted EPS spread is stable: 0.01 (Q2 4.27/4.26; Q1 3.55/3.54), 0.02 (H1 7.82/7.80; FY26 6.84/6.82). No new dilutive instruments visible. A4: reconcile the share count, and cross-check against the ESOP pool once a thesis exists. |
| F12-1 | F12 (lender variant) | LI8_365, LI8_389-LI8_391, LI14_718, LI14_745-LI14_747, R52_989 (R791-R792), LI9_456-LI9_463, ANX30_1722-ANX30_1736 | 365, 389-391, 989, 1722-1736 | "Loans 69,562. 71 55,951.49"; "Borrowings (other than debt securities) 40,633.05 32,933.1 3"; "Debt-equity ratio 4.30 4.28" | FORWARD-SIGNAL | Single segment (note 5, line 490), so the segment test runs on the whole lender balance sheet. Loans grew 24.3% in six months (55,951.49 to 69,562.71; S = C). Equity grew 3,405.83 (S); 71% of that was QIP. D/E fell from 4.67x (S, Mar, computed) to 4.30x (S) / 4.28x (C) only because of the QIP. Incremental debt was 10,767.11: bank and other borrowings +7,699.92 (71.5%), debt securities +2,582.30 (+17.5%), subordinated +484.89 (+129%). Annexure II split at 30 Sep (incl. accrued interest, total 59,477.31): bank TL/WCDL 33,565.29 (56.4%), other TL 4,586.45 (7.7%), secured NCD 17,854.24 (30.0%), CP 2,574.52 (4.3%), sub debt + POI 896.81 (1.5%). At this growth, leverage rebuilds within a few quarters on internal accrual (H1 PAT 682.56). The agenda carries no capital-raising enabling resolution (ledger T4 note). A4 questions: target leverage ceiling, next equity timing, bank-line concentration. |
| F12-2 | F12 (lender variant) | ANX30_1708 (R932-R935), ANX30_1742 (R974-R975), ANXII_N1 (R1324), ANXII_N2 (R1325), NS10 (R1106, R1278) | 1742, 1752, 862-864 | "Cover on Book Value 121•1. 101%"; "considered the book value (Gross of impairment provision)" | AMBIGUOUS | Pari-passu NCD cover is 17,980.96 / 17,849.43 = 100.7%, a headroom of 131.53 Cr (0.73% of the charged pool). Cover is measured on book value gross of ECL (Annex II note 2). Note 1 says the charged pool is sized "based on asset cover requirement", so cover runs at the minimum by design. If ECL on the charged pool exceeds 0.73%, cover net of impairment is below 100%. ECL on that pool is NOT FOUND. Exclusive cover 5.82 / 4.81 = 121%. Note 10 claims the NCDs are "fully secured ... to the extent as stated in the respective information memorandum". A4 question: covenant cover level per IM, and cover net of ECL. |
| F12-3 | F12 (lender variant) | FN04 (R763-R766, R1284), NS11c (R753-R762), NS11d (R1014-R1034), LI8_366 (R234-R235) | 912-914, 903-908, 926, 934-937, 366 | "transferred 10,558 loan accounts durmg the quarter ... consideration including security receipts on 83.92 crores ... already written off in the books"; "Arcil•Trust•2027-002 Unrated" | FORWARD-SIGNAL | Stressed loans and written-off pools are being sold to ARCs for consideration that includes security receipts (SRs). Q2: 5,312 stressed accounts (principal 161.60, NBV 92.49, consideration 89.19), plus 10,558 written-off accounts for 83.92. H1: 11,138 accounts (280.50 / 146.78 / 140.46), plus 23,421 written-off accounts for 151.03. 5 of 20 SR trusts are unrated, 4 of them new FY27 Arcil series. Investments rose 587.34 (2,490.46 to 3,077.80); the SR share is NOT FOUND. The P&L line that takes the 83.92 written-off-pool consideration is NOT FOUND. If it sits in impairment, Q2 impairment of 346.37 is net of up to 83.92 (24.2% of the line). H1 annualised impairment on simple-average loans is 2.23% (computed). Unrated SRs carry future fair-value markdown risk. A4 questions: where the recovery is booked, SR book size, cash vs SR mix, SR provisioning policy. |
| F12-4 | F12 (lender variant) | LI7_302 (R075-R080), LI13_654 (R453-R458), NS11c (R759-R762) | 302, 906, 908 | "Net loss on derecognition of financial instruments 29.33 19.76 30.00 49.09 30.00 105.79"; "Net book value of loans transferred ... 92.49 146.78"; "Aggregate consideration including security receipts(< in crores) 89. 19 140.46" | AMBIGUOUS | The P&L derecognition loss (Q2 29.33, H1 49.09; S = C) does not tie to note 11(c). Consideration minus NBV gives a loss of only 3.30 (Q2) and 6.32 (H1). Unexplained: 26.03 (Q2) and 42.77 (H1). On a gross-principal basis the loss would be 72.41 (Q2), so neither basis ties. A4 question: decompose the derecognition-loss line (ARC sales, write-off pool, DA-related, other). |
| F13-1 | F13 | AG2 (R1096, R1113-R1114, R1218), AG3 (R1097), ANXA2 (R1098, R1119-R1120), ANXA3 | 78-80, 90-92, 127-130, 131-157 | "Re-appointment of Ms. Kemisha Soni (DIN: 06805708), Independent Director of the Company, for a second term of 3 (Three) years, with effect from January 30, 2027 till January 29, 2030" | NEUTRAL-FACT | ID with forensic-audit, IS-audit and NBFC-accounting expertise renewed through Jan 2030 via postal ballot (special resolution). The second term is 3 years. The filing does not state her committee roles. Governance continuity is mildly positive. The letter carries no AR / Board's Report approval, AGM notice, record date, dividend, auditor appointment or capital-raising enabling resolution. No Role 6 AR Deep Dive event to schedule from this outcome. Investor presentation sent separately (line 71). |
| F14-1 | F14 | NC7 (R1144, R1249), NS7 (R1168, R1275), ANX20_1078 (R1185) | 497, 850, 1078 | "completed a Qualified lnstitutions Placement (" QIP") on 13 April 2026"; "Date _ofRaisingFunds _J January 16, 2026 _" | AMBIGUOUS | The QIP date conflicts between notes 7 (C and S: 13 April 2026) and the CFO-signed Reg 32(1) statement (16 January 2026). The paid-up capital trend supports April: Mar 2026 161.59, then Jun 2026 175.16 (+13.57, about the 13.49 QIP face value). The cash-flow equity proceeds of 2,450.00 sit in H1 FY27. January 16, 2026 may be an approval or launch date mislabelled. A4 question: what the 16 Jan 2026 date represents. The monitoring agency (Crisil Ratings) reports rest on this form. |
| F14-2 | F14 | ANX30_1740 (R967-R968), ANX30_1741 (R969-R973), AUDK9 (R1313-R1314) | 1740, 1741, 1482 | "Others ... 939.30 871.26"; "Total 4.81 17 849.43 38,151.74 4 891.92 60,829.87"; "(e) Verified the arithmetical accuracy of the Statement" | AMBIGUOUS | Annexure II liabilities fail a cross-foot. The "Others" row shows 939.30 in one column and 871.26 in the total column. The column subtotal 4,891.92 foots only with 939.30; the grand total 60,829.87 foots only with 871.26 (and ties to the balance sheet: 60,722.39 + 107.48). The break is 68.04 Cr. Both readings are confirmed by their own subtotals, so this is not OCR, though column mapping is A1 COLUMN_UNRESOLVED. The asset side cross-foots fully. The certificate says its auditor verified the arithmetic. The break is immaterial in size but adds to the governance data point. A4 / A1: confirm against the page image if material. |
| F14-3 | F14 | R52_1018-R52_1019 (R829-R830), R52_994 (R797), ENC6 (R1111), NS10 (R742, R1173), FN08 (R1299), NC8 | 1018-1019, 994, 61, 866, 1039, 504 | "a) Gross stage 3 % 1.20%" (one column only); "b) value('!; in crores)" (blank); "dated September 28, 2026" vs "dated 13 August 2025"; "Bombay Stock Exchange" vs "BSE Limited" | NEUTRAL-FACT | Small drafting items, individually immaterial: (1) the Reg 52(4) sector ratios give a standalone column only, while every other line gives S and C; (2) the RPS value cell is blank beside quantity NIL; (3) the cover letter cites a Reg 54 master circular dated 28 Sep 2026, while note 10 and the certificate cite the 13 Aug 2025 circular; (4) the exchange is named "BSE Limited" in the notes and "Bombay Stock Exchange" on p19. Note text and auditor letters agree on "limited review" (no audit/review conflict). Cumulative governance data point only. |
| F17-1 | F17 (orchestrator-directed filing-silence audit) | R52_1018-R52_1019, AG4 (R984, R1095) | 1017-1019, 71-72 | "r. Sector specific equivalent ratio a) Gross stage 3 % 1.20% b) Net stage 3% 0.61%"; "Investor's Presentation is being sent separately" | AMBIGUOUS | The Notion checklist was not supplied. Silence is audited against standard lender monitorables (table in section 4). The filing is silent on 11 of 13 items. The Reg 52(4) "sector specific equivalent ratio" carries only GS3 and NS3, with no CRAR, Tier 1, PCR or Stage 2. Prior-quarter filing not supplied, so consecutive-quarter count = 1 (this filing), prior ND. Most items probably sit in the separately sent investor presentation. A4 should source them there and ask on the call for anything absent. |

## 2. CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 Zero-value standing items | FINDING | 33 ZERO_STANDING rows on 17 lines read. Material: derecognition-gain dash in Q2 (F1-1) and JV ~Nil line with 50.70 / 0.02 held-for-sale gap (F1-2). Rest is template: earlier-year tax dashes (R124, R126, R503), CF FV-loss dash (R300, R659), trust Nil (R389-R392), note 11(b) NIL purchased pools (R751-R752), COVID-framework dashes (R769-R779; only "Others" 8.82 to 7.46 remains, foots 8.82 - 0.32 - 0.21 - 0.83 = 7.46), RPS NIL (R795-R796), DRR NIL exempt under Rule 18(7)(b)(iii) (R800-R801, line 1033). |
| F2 S vs C decomposition | PASS | P&L identical in all 6 periods (revenue 2,624.50 / 2,330.22 / 1,542.30 / 4,954.72 / 2,856.27 / 6,790.18; PAT 374.85 / 307.71 / 74.20 / 682.56 / 136.80 / 541.81). Gap 0.00 = 0% of S PAT every period, so no trend move. No subsidiaries. JV equity method discontinued 13 Dec 2021, JV share ~Nil, no eliminations. Balance-sheet gap is a constant 50.68 Cr at 31 Mar and 30 Sep (assets held for sale 50.70 vs 0.02; other equity 13,577.95 vs 13,527.27 and 10,186.65 vs 10,135.97). Reg 52(4): D/E 4.30 S / 4.28 C both tie to 58,865.41 debt (excl. lease) over net worth; net margin 14.28% = 374.85 / 2,624.84 total income; total debt / total assets 0.79. |
| F3 Shell-entity detection | PASS | Cost lines identical S vs C because the group has no subsidiaries, not because entities are dormant. JASPL is a held-for-sale JV with no line-by-line consolidation. The Welfare Trust is inside the standalone. No Going Concern EoM on any entity. |
| F4 Unaudited contribution ratio | FINDING | Unreviewed PAT = Nil (trust) + ~Nil (JV) = 0% of S and C PAT, below the 10% bar. Separate finding on scope and YoY jump: the unreviewed trust's treasury-share sale rose to 227.66 Cr from 3.54 Cr (F4-1). |
| F5 Going concern / EoM scope | FINDING | No GC, no EoM in either LRR or the certificate. New predecessor-auditor paragraph this quarter (AUDC7, AUDS6): the joint-auditor pair changed after 17 Jul 2026 (F5-1). Verbatim diff against the prior quarter is impossible: prior-quarter fulltext not supplied. Comparative wording shows K&P reviewed Q1 FY27 and Q2 FY26 and audited FY26, all unmodified. |
| F6 Forward-commitment phrases | FINDING | Lexicon hits: "will also be published" (44), "will be uploaded" (72), "subject to the approval" (80, 129), "has completed" (497, 850), "have been utilized" (500, 852), "expected to be completed" (512, 860), "shall be filed" (487, 844), "has been separately filed" (866), "commenced/commencing" (94, 128), "reaffirmed" (510, 859), escrow "subsequently closed" (1153). Register in section 3. Material: JASPL undated (F6-1). |
| F7 Hedge phrases | PASS | "subject to" hits are procedural (shareholder approval of the ID re-appointment). "no assurance" hits are auditor SRE 2410 boilerplate (215, 569, 1434). No "may sometimes", "could have an effect", "evaluating", "exploring", "in discussions" or "endeavour" in notes. No new hedge on revenue lumpiness or concentration. The "to the extent as stated" wording in note 10 (863) is handled under F12-2. |
| F8 Tax forensics | FINDING | ETR 24.97% to 25.22% in all periods vs 25.17% statutory (S = C). Earlier-year tax non-zero in Q1 FY27 and FY26 (F8-1). DT sign flip and cash-tax rise (F8-2). DTA roll ties exactly. |
| F9 OCI forensics | FINDING | The Q1 FY27 actuarial swing (2.66) exceeds the full FY26 (2.04), which is the rule trigger (F9-1). Cash-flow hedge Q2 34.07 is about the full FY26 35.12 (F9-2). FVOCI (1.91) Q2 is small. |
| F10 Share count and dilution | FINDING | Paid-up rise has a 0.97 Cr residual not explained by notes 6 and 7 (F10-1). Basic vs diluted spread stable at 0.01 to 0.02. Cross-check with known warrants / ESOPs deferred to A4 (no thesis). |
| F11 Reserves and net worth tie-out | PASS | C: 176.12 + 13,577.95 = 13,754.07 = Reg 52(4) net worth (line 997). S: 176.12 + 13,527.27 = 13,703.39 = Reg 52(4). March: C 161.59 + 10,186.65 = 10,348.24; S 161.59 + 10,135.97 = 10,297.56. S other-equity roll: 10,135.97 + TCI 700.03 + QIP premium 2,486.51 - issue costs 65.34 (644.84m + 8.60m) + ESOP expense 35.63 + trust treasury release 226.69 (227.66 less 0.97 face value) = 13,519.49 vs reported 13,527.27. Residual +7.78 Cr (0.06%), below the 5% bar. Candidates: ESOP exercise premium, and cash-flow equity proceeds of 2,450.00 vs QIP net-of-cost 2,434.66. No third-party net-worth figure in the filing. |
| F12 Segment forensics | FINDING | Single segment (note 5), so the lender variant applies the asset/liability test to the whole balance sheet and the Annexure II encumbrance split: leverage and funding mix (F12-1), 101% gross-basis NCD cover (F12-2), ARC and written-off-pool sales for SRs (F12-3), derecognition-loss mismatch (F12-4). |
| F13 Board outcome beyond results | FINDING | ID re-appointment through 29 Jan 2030 by postal ballot. No AR, AGM, dividend, record date, auditor or capital-raise items (F13-1). Meeting 1:45 to 3:32 PM (107 min). Letter signed 16:23:14, after close. |
| F14 Note drafting inconsistencies | FINDING | QIP date conflict (F14-1). Annexure II 68.04 Cr cross-foot break despite the certificate's arithmetic check (F14-2). Minor items (F14-3). No audit vs limited-review wording conflict. MSKA signatory name truncated at line 617 and absent at line 262: capture artefact, not counted. |
| F15 Entity list diffs | PASS | Consolidation list: JASPL (JV, held for sale), 1 entity. Standalone includes PFL Employee Welfare Trust. No subsidiaries. No addition, deletion, rename or relationship change is visible in the filing; the comparative paragraphs note no entity change. The prior-quarter list was not supplied (ENTITY_CHANGE ND). Re-test when a prior ledger exists. |
| F16 Presentation: dropped / reframed | N.A. | Results doctype. No deck in scope. The investor presentation was sent separately. |
| F17 Silence audit | FINDING | The doctype rule makes F17 N.A. on a results filing. Run at orchestrator direction as a filing-silence audit against standard lender monitorables. Checklist not supplied. Silent on 11 of 13 items (F17-1, section 4). |

## 3. COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Note / line ref | Status word |
|---|---|---|---|---|
| 1 | Sell entire JASPL shareholding (JV); regulatory approval received | Undated ("in due course"); held for sale since 13 Dec 2021 | C note 9 lines 509-513; S note 9 lines 858-861; LRR para 4 line 226 | underway |
| 2 | Re-appoint Kemisha Soni (ID) for a second 3-year term, 30 Jan 2027 to 29 Jan 2030, by special resolution via postal ballot | Shareholder result before 30 Jan 2027 | Cover letter lines 78-92; Annexure A lines 127-130 | initiated |
| 3 | Upload investor presentation to website | After 09 Oct 2026 (sent separately) | Line 71-73 | initiated |
| 4 | Publish results in newspaper in LODR format | After 09 Oct 2026 | Line 44-45 | initiated |
| 5 | File results with BSE / NSE and on website | 09 Oct 2026 (this filing) | C note 4 line 487; S note 4 line 844 | completed |
| 6 | QIP: 67,430,883 shares at Rs 370.75 = 2,500.00 Cr; net proceeds 24,315.16m fully used by 30 Jun 2026; escrow 40m used in Q2 (8.60m issue costs + 31.4m GCP), escrow closed | Completed 13 Apr 2026 per notes (16 Jan 2026 per Reg 32 form: conflict, F14-1) | C note 7 lines 497-500; S note 7 lines 850-853; p21 lines 1144-1153 | completed |
| 7 | NCD issues Q2: 7 tranches, 2,265.00 Cr, value dates 03 Jul to 16 Sep 2026; fully used; no deviation | Completed 16 Sep 2026 | p22 line 1186; p23 lines 1233-1247; p24-25 lines 1273-1341 | completed |
| 8 | Maintain required security cover on secured NCDs "at all times" | Standing; tested quarterly (101% pari-passu at 30 Sep 2026) | S note 10 lines 862-866; p30 line 1742 | underway |
| 9 | File security cover certificate under Reg 54(3) | 09 Oct 2026 | S note 10 lines 865-866; certificate lines 1357-1531 | completed |
| 10 | COVID resolution-framework book run-off | Ongoing; 7.46 Cr standard at 30 Sep 2026 | S note 12 lines 941-962 | underway |

## 4. LENDER MONITORABLE SILENCE TABLE (F17, orchestrator-directed; Notion checklist not supplied)

| Monitorable | In this filing? | What the filing gives (line) | Consecutive quarters silent |
|---|---|---|---|
| AUM (on + off book) | NO | Net loans 69,562.71 only (365, 718). Off-book DA pool NOT FOUND | 1 (prior ND) |
| Disbursements | NO | CF loans outflow 14,361.33 H1 is a net figure, not disbursement (436) | 1 (prior ND) |
| NIM | NO | Computable proxy only: (4,533.94 - 1,957.10) x 2 / simple-average loans 62,757.10 = 8.21% (computed, approximate) | 1 (prior ND) |
| Cost of funds | NO | Proxy: 1,957.10 x 2 / simple-average borrowings 53,481.86 = 7.32% (computed; includes lease interest) | 1 (prior ND) |
| Credit cost | PARTIAL | Impairment line only: Q2 346.37, Q1 353.57; H1 annualised 2.23% on simple-average loans (computed). Possible netting of written-off-pool recoveries (F12-3) | 1 (prior ND) |
| GNPA / NNPA (GS3 / NS3) | YES (S only) | GS3 1.20%, NS3 0.61% (1018-1019). No C column, no prior period | 0 |
| Stage 2 | NO | NOT FOUND | 1 (prior ND) |
| ECL coverage / PCR | NO | Stage 3 PCR roughly 49% from GS3/NS3 (approximate; denominators differ; Stage 3 ECL NOT FOUND) | 1 (prior ND) |
| Write-offs | NO | Only written-off accounts sold: 10,558 / 83.92 Q2; 23,421 / 151.03 H1 (912-913) | 1 (prior ND) |
| CRAR / Tier 1 | NO | Absent from Reg 52(4)(r) sector ratios (1017-1019) | 1 (prior ND) |
| ALM | NO | NOT FOUND | 1 (prior ND) |
| Borrowing mix | YES (point in time) | BS lines (389-391); Annexure II split at 30 Sep (1722-1741). No March split in Annexure II | 0 |
| Liquidity buffer / LCR | NO | Cash 215.98 (360), investments 3,077.80 (366); composition and LCR NOT FOUND | 1 (prior ND) |

## 5. ITEMS FOR A4 (FORWARD-SIGNAL and AMBIGUOUS, to convert into management questions)

FORWARD-SIGNAL: F1-1, F1-2, F6-1, F12-1, F12-3.
AMBIGUOUS: F4-1, F5-1, F8-2, F9-2, F10-1, F12-2, F12-4, F14-1, F14-2, F17-1.
Pillar-relevant facts flagged for /fttcp and Role 1 per OR-30, not analysed here: leverage rebuild rate (F12-1), credit cost netting (F12-3), assignment-gain lumpiness (F1-1), JASPL S-vs-C split on sale (F1-2).
Pipeline notes: no source access was needed. A1 should confirm the p30 Annexure II "Others" row against the page image if A4 treats F14-2 as material. The p20 QIP form is OCR-garbled; only "No" is legible on the deviation answer (line 1089).

```yaml
stage: A3-forensics
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/poonawalla-q2fy27/work/forensics_results_poonawalla_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: PASS
  F4: FINDING
  F5: FINDING
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: FINDING
  F10: FINDING
  F11: PASS
  F12: FINDING
  F13: FINDING
  F14: FINDING
  F15: PASS
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F1-1", check: "F1", line: "296, 648, 874-876", classification: "FORWARD-SIGNAL", implication: "Q2 derecognition gain is nil (Q1 50.93 = 12.4% of PBT; FY26 216.83 = 30.0% of PBT); DA 1,000.34 Cr all in Q1; DA restart in H2 makes reported PBT lumpy"}
  - {id: "F1-2", check: "F1", line: "239, 226, 379, 734", classification: "FORWARD-SIGNAL", implication: "JASPL carried at 50.70 Cr (C) vs 0.02 Cr (S); on sale S books gain above 0.02, C gain or loss vs 50.70; first S-vs-C P&L split"}
  - {id: "F4-1", check: "F4", line: "580-584, 451, 809", classification: "AMBIGUOUS", implication: "Unreviewed PAT 0% (passes 10% test) but unreviewed Welfare Trust sold 227.66 Cr treasury shares in H1 vs 3.54 Cr (64x); 33.4% of H1 PAT, straight to equity"}
  - {id: "F5-1", check: "F5", line: "249-257, 598-607", classification: "AMBIGUOUS", implication: "Joint-auditor pair changed after 17 Jul 2026; second predecessor unnamed; no reason given; FY27 audit is new pair's first look at ECL; no EoM/GC; prior text not supplied"}
  - {id: "F6-1", check: "F6", line: "509-513, 858-861, 226-227", classification: "FORWARD-SIGNAL", implication: "JASPL sale undated after ~4.8 years held for sale; regulatory approval received; Ind AS 105 basis and closing date to confirm"}
  - {id: "F8-1", check: "F8", line: "311, 663", classification: "NEUTRAL-FACT", implication: "Earlier-year tax (0.19) Q1 FY27 and (0.01) FY26; ETR 24.97-25.22% vs 25.17% statutory, S = C"}
  - {id: "F8-2", check: "F8", line: "312, 664, 371, 445", classification: "AMBIGUOUS", implication: "DT flipped from FY26 124.47 charge to H1 FY27 24.33 credit (267 bps shield); DTA 72.70 to 91.16 ties; cash tax 2.8x; driver of the build to confirm"}
  - {id: "F9-1", check: "F9", line: "317, 669", classification: "NEUTRAL-FACT", implication: "Q1 actuarial loss 2.66 exceeds full FY26 2.04; verify assumptions at FY27 AR"}
  - {id: "F9-2", check: "F9", line: "326, 362", classification: "AMBIGUOUS", implication: "Q2 cash-flow hedge OCI 34.07 = 97% of FY26; derivatives 399.56; hedged borrowing size NOT FOUND"}
  - {id: "F10-1", check: "F10", line: "339, 683, 493, 497-498, 451", classification: "AMBIGUOUS", implication: "Paid-up +14.53 Cr vs 13.56 explained by QIP and ESOP; 0.97 Cr (~4.87m shares) residual, likely trust treasury release; EPS spread stable 0.01-0.02"}
  - {id: "F12-1", check: "F12", line: "365, 389-391, 989, 1722-1736", classification: "FORWARD-SIGNAL", implication: "Loans +24.3% in H1; D/E 4.67x to 4.30x only via QIP; 71.5% of new debt from banks; leverage rebuilds fast; no capital-raise enabling item"}
  - {id: "F12-2", check: "F12", line: "1742, 1752, 862-864", classification: "AMBIGUOUS", implication: "Pari-passu NCD cover 100.7% on gross book value; 131.53 Cr headroom = 0.73% of pool; net-of-ECL cover NOT FOUND"}
  - {id: "F12-3", check: "F12", line: "912-914, 903-908, 926, 934-937, 366", classification: "FORWARD-SIGNAL", implication: "Stressed and written-off pools sold to ARCs for SR-inclusive consideration (Q2 89.19 + 83.92); 5 of 20 SR trusts unrated; if recovery sits in impairment, Q2 credit cost netted by up to 24%"}
  - {id: "F12-4", check: "F12", line: "302, 906, 908", classification: "AMBIGUOUS", implication: "P&L derecognition loss 29.33 Q2 / 49.09 H1 vs note 11(c) NBV gap 3.30 / 6.32; 26.03 / 42.77 unexplained"}
  - {id: "F13-1", check: "F13", line: "78-80, 90-92, 127-130", classification: "NEUTRAL-FACT", implication: "Forensic-audit ID renewed to 29 Jan 2030 via postal ballot; no AR, AGM, dividend, auditor or capital-raise items"}
  - {id: "F14-1", check: "F14", line: "497, 850, 1078", classification: "AMBIGUOUS", implication: "QIP date 13 Apr 2026 (notes) vs 16 Jan 2026 (Reg 32 form); share-capital trend supports April"}
  - {id: "F14-2", check: "F14", line: "1740, 1741, 1482", classification: "AMBIGUOUS", implication: "Annexure II Others row 939.30 vs 871.26; 68.04 Cr cross-foot break despite certificate claiming arithmetic verified"}
  - {id: "F14-3", check: "F14", line: "1018-1019, 994, 61, 866, 1039, 504", classification: "NEUTRAL-FACT", implication: "Sector ratios S-only, RPS value blank, Reg 54 circular date mismatch, exchange naming; cumulative governance data point"}
  - {id: "F17-1", check: "F17", line: "1017-1019, 71-72", classification: "AMBIGUOUS", implication: "Filing silent on 11 of 13 lender monitorables (no CRAR, Stage 2, PCR, AUM, disbursement, ALM); source from investor presentation; checklist not supplied"}
forward_signals: ["F1-1", "F1-2", "F6-1", "F12-1", "F12-3"]
ambiguous: ["F4-1", "F5-1", "F8-2", "F9-2", "F10-1", "F12-2", "F12-4", "F14-1", "F14-2", "F17-1"]
commitments:
  - {commitment: "Sell JASPL JV shareholding; regulatory approval received", implied_date: "undated (in due course); held for sale since 13 Dec 2021", ref: "C note 9 L509-513; S note 9 L858-861", status_word: "underway"}
  - {commitment: "Re-appoint Kemisha Soni as ID, 30 Jan 2027 to 29 Jan 2030, special resolution via postal ballot", implied_date: "before 30 Jan 2027", ref: "cover letter L78-92; Annexure A L127-130", status_word: "initiated"}
  - {commitment: "Upload investor presentation to website", implied_date: "after 09 Oct 2026", ref: "L71-73", status_word: "initiated"}
  - {commitment: "Publish results in newspaper", implied_date: "after 09 Oct 2026", ref: "L44-45", status_word: "initiated"}
  - {commitment: "File results with BSE/NSE and website", implied_date: "09 Oct 2026", ref: "C note 4 L487; S note 4 L844", status_word: "completed"}
  - {commitment: "QIP 2,500 Cr completed, proceeds fully utilised, escrow closed", implied_date: "13 Apr 2026 per notes (16 Jan 2026 per Reg 32 form)", ref: "C note 7 L497-500; S note 7 L850-853; p21 L1144-1153", status_word: "completed"}
  - {commitment: "Q2 NCD issues 2,265 Cr in 7 tranches, fully utilised, no deviation", implied_date: "03 Jul to 16 Sep 2026", ref: "p22 L1186; p23 L1233-1247; p24-25 L1273-1341", status_word: "completed"}
  - {commitment: "Maintain required security cover on secured NCDs at all times", implied_date: "standing (101% pari-passu at 30 Sep 2026)", ref: "S note 10 L862-866; p30 L1742", status_word: "underway"}
  - {commitment: "File Reg 54(3) security cover certificate", implied_date: "09 Oct 2026", ref: "S note 10 L865-866; certificate L1357-1531", status_word: "completed"}
  - {commitment: "COVID resolution-framework book run-off", implied_date: "ongoing (7.46 Cr at 30 Sep 2026)", ref: "S note 12 L941-962", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Earnings quality and funding carry the forward signal. Q2 PAT 374.85 Cr has no assignment gain (Q1 50.93; FY26 216.83 = 30% of PBT), so Q2 is cleaner than Q1 on that axis. Against that, written-off pools sold for 83.92 Cr of SR-inclusive consideration in Q2; the P&L line taking it is NOT FOUND. If it nets inside impairment, Q2 credit cost is flattered by up to 24%. Five SR trusts are unrated, four new FY27 series. The derecognition loss (29.33) does not tie to note 11(c) (3.30). Leverage fell to 4.30x only through the 2,500 Cr QIP. Loans grew 24.3% in six months, new debt is 72% bank lines, and pari-passu NCD cover is 101% gross of ECL. S equals C on P&L; JASPL's 50.68 Cr carrying gap will split them on sale. Auditor pair changed after Q1. The QIP date conflict and the 68.04 Cr Annexure II break are drafting signals. Prior-quarter text and checklist not supplied: all diffs are within-filing."
```
