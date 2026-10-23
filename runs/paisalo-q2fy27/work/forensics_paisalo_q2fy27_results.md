# A3 FORENSIC NOTES - Paisalo Digital Limited (PAISALO) - Q2 FY27 - doctype: results (Reg 33/52 unaudited results, limited review, board meeting 22-Oct-2026)

Agent: A3 forensic notes | model: claude-opus-5-5 | run date 2026-10-23
Inputs read: A1 structured extraction (R001-R1372, all rows), A1 fulltext (lines 1-1237, including addendum A1-R1 lines 787-1237 used as the value source for pages 2-8), A2 ledger (all sections, including the 8 MISSING_FROM_STRUCTURED rows M-b, M-c, M-d, M-f, M-o, M-p, M-q, M-s read at fulltext lines 1215-1234), Notion thesis copy sections 3 and 4 (data only).
Not read: source PDF, anything under inputs/. No prior-quarter fulltext exists (first pipeline quarterly). Any prior-quarter fact below that is not in this filing's Q1 FY27 or comparative columns is marked (Notion-sourced).
Units: statements Rs Lakhs; note 5 table Rs Cr. "my arithmetic" marks every computed number.

## 0. RECONCILIATION
- Structured IDs in ledger: 1,372 of 1,372 read at their cited lines. A2 added rows M-b, M-c, M-d, M-f, M-o, M-p, M-q, M-s: 8 of 8 read at fulltext l.1215-1234. Reconciled 100%.
- A2 flags weighed: SIGNATURE_BEFORE_MEETING_END -> A3-16 (AMBIGUOUS). SUBSIDIARY_BASIS_NOT_STATED -> A3-08 (AMBIGUOUS). FOOTNOTE_UNRESOLVED (UDINs R1218-R1219, R1230-R1232, R1368; asterisk R1333) -> A3-20, A3-23 (NEUTRAL-FACT). RESTATED_COMPARATIVES (R1352) -> A3-22 (AMBIGUOUS). RESTATED on ratio h/i (R1084-R1087): values tie to statement pages exactly, no finding. SPELLING_VARIANT -> A3-23. Eight Nil/Not-applicable ratio rows: DSCR, ISCR, debtors turnover, inventory turnover, operating margin "Not applicable" and DRR "Not applicable" (NBFC exemption, l.619-620) are normal NBFC presentation; preference shares Nil (l.1217) is a standing Nil line; ratio s is a header. No finding on these eight except ratio l (A3-02) and the adjacent ratio r (A3-18).
- Verification run during the read (my arithmetic; all tie unless listed as a finding): Q1+Q2 = H1 on every P&L line checked; SA and CON balance sheets balance; cash at end = cash + bank balances (SA 6,008.15; CON 10,306.93); D/E 2.83x and debt/assets 0.72 reproduce from the balance sheet; PPE roll-forward ties within 0.29; paid-up capital change 46.27 = note 6 shares; FCCB conversion value 46,27,240 x Rs 45.74 = Rs 2,116.50 Lakhs = cash flow line VII (l.981); investments change = purchases 14,112.99 + fair value gain 267.46; CP discount yields reproduce (9.00%, 8.90%, 8.90%).

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F1 | R044-R049, R522-R527 | fulltext l.804, l.1009 | "(vi) Net gain on derecognition of financial instruments under amortized cost category - - - - - -" | NEUTRAL-FACT | Zero in all six periods, SA and CON. No assignment or co-lending upfront gain has ever been booked in the periods shown. This is the line where direct-assignment or co-lending gains would first appear; watch it as the filed test of the co-lending catalyst. |
| A3-02 | F1 | R1092-R1093 (A2-raised ZERO_STANDING), R110-R112 | l.1227; l.816 | "l \| Bad debts to Account receivable ratio \| Standalone: 0.00 \| Consolidated: 0.00"; "(v) Impairment on financial instruments (37.81) 1,562.79 753.06 1,524.98" | AMBIGUOUS | H1 impairment is Rs 15.25 Cr, yet the bad-debt ratio is 0.00. Reading A: zero write-offs in H1, so GNPA 0.66% is not flattered by write-offs. Reading B: the ratio is computed on trade receivables (Rs 25.57 Cr, l.884), not loans, and says nothing. Separating observation: H1 write-off amount in Rs Cr. Links the open Q1 question on write-offs/PCR (Notion-sourced, Q7 PARTIAL). |
| A3-03 | F1 | R318, R320, R351, R356, R832, R834, R865, R870; R1066-R1070, R1201 | l.882, l.903; l.598 | "(c) Derivative Financial Instruments - -"; "on conversion 2500 Foreign Currency Convertible" | AMBIGUOUS | USD FCCBs exist (note 6) but derivative assets and liabilities are nil on both dates. Either the FX exposure and the conversion option are unhedged and not separately fair-valued, or they sit in borrowings. The remaining FCCB balance is not in this filing. Question: FCCB outstanding at 30-Sep (USD), FX hedge, and accounting of the conversion option. |
| A3-04 | F1 | R473, R475-R476; R995-R997 | l.980; l.1195 | "VI Purchase of Security Receipts - 126.85 2,442.92"; "VI Purchase of Security Receipts - 126.85 1,403.69" | AMBIGUOUS | FY26 shows Rs 24.43 Cr SA (Rs 14.04 Cr CON) on a security-receipts line, positive, inside financing activities. H1 FY27 is nil. Security receipts usually arise from sale of stressed loans to an ARC, which lowers reported GNPA. Question: did Paisalo sell loans to an ARC in FY26, what security receipts are held at 30-Sep, and is any of the H1 investment build (A3-12) security receipts. |
| A3-05 | F3 | R492-R551 vs R014-R073; R564-R635 vs R086-R157 | l.1013 vs l.808; l.1027 vs l.822; l.1025 vs l.820 | "(xi) Others expenses 3,563.85 2,456.71 2,433.16"; "(xi) Other expenses 3,368.51 2,173.42 2,416.11" | AMBIGUOUS | Nupur Finvest is not a shell (own employee cost Rs 0.46 Cr/qtr). Its P&L is changing shape (CON minus SA, my arithmetic): revenue Q2FY26 818.42 -> Q1 566.91 -> Q2 496.80 (-39.3% YoY); other expenses 17.05 -> 283.29 -> 195.34 (11.5x YoY); implied subsidiary cost-to-income 11.9% -> 72.6%. The subsidiary adds 0.73pp to CON Q2 C/I (40.95% CON vs 40.22% SA) and 1.42pp in Q1. Two readings: run-off ahead of merger or sale (the discontinued-operations lines would light up), or a re-tooling with new costs. Separating observation: next quarter's subsidiary loan delta and any board resolution on Nupur. |
| A3-06 | F3 | R839/R841 vs R325/R327; R829/R831 vs R315/R317; R876/R882 vs R362/R368; R842/R844 vs R328/R330; R980-R983 vs R459-R462; R935-R937 vs R414-R418 | l.1099 vs l.886; l.1093 vs l.880; l.1125 vs l.912; l.1101 vs l.888; l.1190 vs l.975; l.1173 vs l.958 | "(e) Loans 7,11,439.93 5,92,950.57"; "(a) Cash & Cash Equivalents 9,959.80 14,698.48"; "I Proceeds from Borrowings 87,046.23" | AMBIGUOUS | Subsidiary balance sheet (CON minus SA, my arithmetic), 31-Mar -> 30-Sep: net loans 135.50 Cr -> 106.49 Cr (-21.4%); cash 0.16 Cr -> 42.95 Cr; external borrowings 29.50 Cr -> 5.09 Cr; debt securities unchanged at 55.70 Cr; investments +11.85 Cr (CF l.1187 minus l.972). The CON cash flow equals SA plus subsidiary with no elimination: CON borrowings proceeds 87,046.23 = SA 84,585.13 + 2,461.10, against a CON balance-sheet change of only 82,143.85; the 4,902.38 gap equals the CON other-financial-assets gap (CF 6,453.52 vs balance-sheet change 1,551.15). [INFERENCE] Paisalo advanced about Rs 49.02 Cr to Nupur in H1, booked in parent "Other Financial Assets" (SA OFA 22.20 Cr -> 86.05 Cr). Nupur used it to repay Rs 24.41 Cr external debt, buy Rs 11.85 Cr investments and hold Rs 42.95 Cr cash while its loan book shrank. Question: amount, terms and purpose of the advance; maturity of Nupur's Rs 55.70 Cr debt securities. |
| A3-07 | F4 (lender reading: PAT resting on unaudited management estimates) | R110-R118, R588-R596, R158-R163, R1116, R1367 | l.816; l.1021; l.699 | "(v) Impairment on financial instruments (37.81) 1,562.79 753.06"; "nothing has come to our attention" | FORWARD-SIGNAL | Q2 SA impairment is a write-back of Rs 0.38 Cr after a Rs 15.63 Cr charge in Q1. The pre-tax swing of 1,600.60 is 382% of the QoQ PAT increase (418.98) and about 18.4% of Q2 PAT after tax at 25.17% (my arithmetic). Above the 10% line. Pre-provision operating profit fell 11.3% QoQ (SA 9,723.31 -> 8,627.54; CON -11.0%) and rose 13.8% YoY. The ECL estimate carries only limited-review (SRE 2410) assurance. If Q3 credit cost returns to the FY26 quarterly average (941.21 SA), PAT falls QoQ. The Q2 PAT growth is an estimate release, not operating growth. |
| A3-08 | F4 | R1125-R1127, R1309, R1371, R1187, R1340 | l.765; l.740-741 | "The Statement includes the results of the wholly owned subsidiary M/s Nupur Finvest Private Limited." | AMBIGUOUS | The consolidated review report does not say whether Saket Jain & Co reviewed Nupur or relied on management-furnished or other-auditor numbers. No Other Matters paragraph. Upper bound of the exposure: subsidiary PAT 58.68 of 6,564.13 CON Q2 PAT = 0.89%; H1 0.82%; Q2FY26 1.43% (my arithmetic). Below the 10% threshold, so not material to PAT, but the omission makes A3-05/A3-06 numbers unverified. Question: who reviewed Nupur's H1 FY27 results. |
| A3-09 | F8 | R176-R187, R654-R665, R375/R380, R430/R434-R435, R331/R333, R371/R377 | l.828; l.829; l.1034; l.919; l.964 | "(2) Deferred Tax 488.70 (100.00) 60.64"; "(2) Deferred Tax 488.90 (99.00) 60.63"; "II Income Tax paid (307.49) (1,149.68) (7,232.56)" | AMBIGUOUS | Total ETR is stable (SA Q2 24.93%, Q1 25.42%, Q2FY26 25.57%, FY26 25.51%; statutory 25.17%; no prior-year tax line in the format). The mix moved: current-tax ETR 26.64% Q1 -> 19.29% Q2; deferred tax from a round (100.00) SA / (99.00) CON credit in Q1 to a 488.70 charge in Q2. Round Q1 numbers suggest an estimate trued up in Q2. DTL rose 388.69 = H1 deferred charge. No DTA, no persistent credits, so no ETR step-up risk. [INFERENCE] DTL growth is consistent with expenses deducted for tax when paid but deferred in the books (A3-15). Cash tax H1 Rs 3.07 Cr vs current tax Rs 38.45 Cr; the FY26 current tax asset (2,465.71) absorbed most of it (ties within 6.88). Question: composition of the Q2 deferred charge. |
| A3-10 | F9 | R218-R259, R696-R737, R1184, R1319 | l.842; l.836; l.820 | "Other Comprehensive Income (A+B) - - - - - -"; "(Revaluation of Building) - - - - - -" | AMBIGUOUS | OCI is nil in every period, including audited FY26, although FY26 employee cost was Rs 74.35 Cr. No Ind AS 19 remeasurement line is visible. The F9 swing test cannot fire on zeros. Verify at the FY26/FY27 Annual Report how gratuity remeasurement is booked. Low materiality. |
| A3-11 | F10 | R266-R314, R780-R828, R1066-R1070, R1351 | l.845; l.848-849; l.1062-1063; l.598 | "Basic (Rs.) 0.71 0.67 0.56 1.38 1.08 2.59" / "Diluted (Rs.) 0.71 0.67 0.56 1.38 1.08 2.59" | AMBIGUOUS | Paid-up capital 9,095.84 -> 9,142.11 (+0.51%) traces exactly to note 6 (46,27,240 shares on 2,500 FCCBs). Basic equals diluted EPS to two decimals in all six periods, SA and CON. Notion records USD 16.5 Mn of USD 50 Mn converted and 94.01 Cr shares post-conversion (Notion-sourced), against 91.42 Cr shares filed at 30-Sep, so convertible FCCBs were outstanding at period end. A zero spread with dilutive instruments outstanding needs an explanation (anti-dilution or omission). A4 to cross-check against the Notion FCCB record. |
| A3-12 | F12 (lender reading: balance-sheet build; Note 4 single segment, no segment table) | R325/R327, R326/R329, R361/R366, R362/R368, R315-R317, R328/R330, R1077-R1078, R453, R404 | l.886; l.887; l.911; l.912; l.1214 | "(c) Debt Securities 1,45,569.36 1,15,597.20"; "(f) Investments 20,585.36 6,204.91"; "a \| Debt-Equity Ratio (No. of Times) \| ... 2.83" | FORWARD-SIGNAL | SA, 31-Mar -> 30-Sep (my arithmetic): loans +20.95%; total debt +26.80% (4,27,447.46 -> 5,42,004.75); net worth +8.0%; D/E 2.41x -> 2.83x in six months. Rs 225.6 Cr went into non-loan assets (investments +143.80 Cr, other financial assets +63.85 Cr, other non-financial assets +17.91 Cr), equal to 18.6% of the loan increase, while cash fell Rs 89.74 Cr. Investments are FVTPL (gain 267.46 in H1) and their composition is not disclosed. At this pace D/E reaches the 3.5x internal cap (Notion-sourced) inside about three quarters without equity. Next equity is FCCB conversion. |
| A3-13 | F12 | R1023-R1065, R1290-R1299, R1343-R1350, R086-R091 | l.579-585; l.588; l.592; l.596 | "12.00% Listed Unsecured Redeemable Non-Convertible Debenture"; "(Discounted price per commercial paper: Rs.4,82,244)" | FORWARD-SIGNAL | Q2 issuance Rs 476.98 Cr: NCDs Rs 419.39 Cr at a weighted coupon of 10.26% (secured Rs 294.92 Cr at 9.52%; unsecured Rs 124.47 Cr at 12.00%); CPs Rs 57.59 Cr at 9.00%/8.90%/8.90% annualised (my arithmetic). H1 implied cost of borrowing is 9.98% (finance cost x2 / average debt). New NCD money costs more than the book average, so spread pressure follows as old debt rolls. CP maturities: 30-Dec-2026, 22-Feb-2027, 23-Mar-2027 (my arithmetic). |
| A3-14 | F12 | R1071, R1353-R1354, R1202 | l.603-605 | "The asset cover available as on September 30, 2026 in respect of listed secured debt securities is 1.10 times." | AMBIGUOUS | Asset cover is 1.10x after Rs 294.92 Cr of new secured NCDs in Q2. No prior-quarter value is on file, so the trend is unknown. Question: covenant minimum per the trust deeds and headroom in Rs Cr of unencumbered receivables. |
| A3-15 | F12 (non-earning asset accretion) | R422-R426, R392-R397, R347/R352, R137-R145, R1360, R1082 | l.961; l.950; l.899; l.821; l.627 | "IV Change in other non-financial assets (2,459.25) - (2,743.16)"; "II Deferred Expense W/O 668.08 174.65 665.18"; "(Equity + Other Equity-Revaluation Reserve-Deferred Expenses)" | FORWARD-SIGNAL | Other non-financial assets rose 3,704.31 -> 5,495.48. Gross additions in H1 were 2,459.25 (1,791.17 net change + 668.08 written off; ties exactly), which is 90% of the full FY26 addition in half the time. The Reg 52 net worth deducts "Deferred Expenses", so the company treats this pool as non-capital. The write-off runs through "Depreciation, amortization and impairment": Q2 D&A 549.01 vs 218.01 in Q2FY26 (+151.8%). [INFERENCE] If the whole H1 addition were expensed, SA H1 cost-to-income would be about 41.9%, not the reported 35.6% (upper bound; the pool may include prepayments). The amortisation of this pool raises D&A in coming quarters. On filed CON numbers, opex grew 34.8% YoY in Q2, 0.2pp below the Notion early-warning threshold of 35%; any expensing crosses it. Question: what the deferred expenses are, and the amortisation period. |
| A3-16 | F13 | R011, R1234-R1238, R1311; R1249-R1306; R1239-R1241 | l.42; l.54; l.179; l.653; l.67 | "has, inter alia, approved"; "concluded at 10:25 A.M."; "NM AGARWAL 10:10:02 +05'30'" | AMBIGUOUS | The only operative item disclosed is the results approval. The MD signed all seven statement pages from 10:09:01 to 10:10:02, and the board sat until 10:25 (15 minutes more). The CS letter is stamped 10:30:07. Reading A: the board approved results, the MD signed, and other business ("inter alia") took the last 15 minutes, undisclosed. Reading B: statements were signed before the formal approval. Separating observation: agenda order in the minutes and any other Reg 30 disclosure dated 22-Oct. No AR, AGM, record date, dividend, director term, auditor or fund-raising item: no Role 6 event to schedule. |
| A3-17 | F14 | R916-R922, R955, R588-R596 | l.1166; l.1021; l.1167; l.1180 | "III Impairment on financial instruments 1,524.98"; "(v) Impairment on financial instruments (24.21) 1,573.35 1,191.55 1,549.14"; "IV Expenditure on CSR 180.07" | NEUTRAL-FACT | CON cash flow adds back impairment of 1,524.98 (the SA figure), against CON P&L H1 impairment of 1,549.14. CON CSR expense is 180.07 against CSR paid 155.91. Both gaps are 24.16. [INFERENCE] Nupur's impairment was posted to the CSR line. Immaterial; one more drafting error in the consolidated statements. |
| A3-18 | F14 | R1098-R1099, R1362 | l.1233 | "r \| Net profit margin (%) \| Standalone: 31.93 \| Consolidated: 31.55" | AMBIGUOUS | 31.93% = H1 PBT / total income (16,825.87 / 52,695.98). PAT margin is 23.90% SA and 23.62% CON (my arithmetic). The Reg 52(4) "net profit margin" is a pre-tax margin and overstates by about 8pp. Any tracker that reads this field gets the wrong number. |
| A3-19 | F14 | R1100-R1101, R1363-R1364 | l.1235 | "s-i \| Net Interest Margin (%) \| Standalone: 6.43 \| Consolidated: 6.46" | AMBIGUOUS | NIM basis is not defined in the document. It does not reproduce from filed numbers: H1 annualised NII (interest income less finance cost) / average loans = 8.23%; / average total assets = 7.68% (my arithmetic). Deck "NIM" is 5.7% (Notion-sourced). Notion's pending ruling (section 3) calls 6.43% "green", but the checklist green band (#6) is 6.5-7.0%; 6.43% sits between red (<6.0%) and green. Question: NIM formula and denominator. |
| A3-20 | F14 | R1216-R1219, R1229-R1232, R1368, R1140 | l.717; l.784; l.709; l.778 | "UDIN : 2£4005qqDPTZTQq314"; "UDIN : 26qo05q9 hl DRPQ£4 550"; "Firm ReI No. 1 @" | NEUTRAL-FACT | Both UDINs and the firm registration number are garbled in the text layer (stamp overprint likely). They cannot be verified from A1 output. Action for the operator or Claude web: read both UDINs from the source image and verify on the ICAI UDIN portal. A3 has no source access. |
| A3-21 | F14 | R477-R479, R459-R466, R429-R432, R1066-R1070 | l.981; l.975; l.977; l.963 | "VII Money received against shares/ securities converted into equity Share Capital 2,116.50"; "I Interest paid (24,193.26)" | NEUTRAL-FACT | The SA cash flow is built from balance-sheet deltas: borrowings proceeds 84,585.13 and debt securities 29,972.16 equal the balance-sheet changes exactly, and interest paid equals the P&L finance cost exactly in all three periods. The FCCB conversion (a non-cash event under Ind AS 7) appears as cash "received", offset by a lower borrowings delta. Gross issuance and repayment cannot be read from this cash flow; use note 5 for gross raises. |
| A3-22 | F14 | R038-R043, R098-R106, R1352 | l.803; l.814; l.601 | "(v) Net gain on fair value changes 185.03 82.43 (45.59)"; "(iii) Net loss on fair value changes - - 48.44"; "reclassified/ regrouped whenever necessary" | AMBIGUOUS | Q2FY26 carries both a negative fair-value "gain" of (45.59) in revenue and a fair-value "loss" of 48.44 in expenses. H1FY26 shows gain nil and loss 48.44. Note 7 regroups comparatives without amounts. The Q2FY26 base for YoY revenue and expense growth is not like-for-like by up to Rs 0.94 Cr. Question: what was regrouped and by how much. |
| A3-23 | F14 | R1333, R1185, R1204, R1252-R1261, R1281 | l.248; l.497; l.850-852; l.1070; l.655 | "STANDALONE CASH FLOW STATEMENT AS AT 30TH SEPTEMBER, 2026"; "*"; "(SUNIL PURUSHOTTANM AGARWAL)" | NEUTRAL-FACT | Cosmetic tally: cash flows titled "as at" instead of "for the period ended"; Roman numeral XVII used twice on SA and CON P&L (XVIII skipped); a stray asterisk on the CON P&L with no footnote text; the MD's typed name reads "PURUSHOTTANM". Individually immaterial; counted toward the drafting tally (section 4). |
| A3-24 | F14 | R885/R891 vs R371/R377; R889/R894 vs R375/R380; R845/R847 vs R331/R333 | l.1130 vs l.917; l.1132 vs l.919 | "(a) Current Tax Liabilities (Net) 731.52 -"; "(a) Current Tax Liabilities (Net) 1,078.93 -" | NEUTRAL-FACT | The CON current tax liability (731.52) is below SA (1,078.93), and CON DTL (1,705.99) is below SA (1,708.38). [INFERENCE] Nupur's tax asset (about 3.47 Cr) is netted against the parent's liability. Ind AS 12 permits cross-entity offset only with a legal right to settle net. Immaterial. |
| A3-25 | F14 | R980-R1003, R935-R937 | l.1190; l.1173; l.1183 | "I Proceeds from Borrowings 87,046.23"; "I Change in Other Financial Assets (6,453.52)" | NEUTRAL-FACT | The consolidated cash flow is the plain sum of parent and subsidiary; the intra-group advance of 4,902.38 (A3-06) is not eliminated. CON operating outflow and CON financing inflow are each overstated by about Rs 49.02 Cr (4.5% of CON CFO). Governance data point on consolidation quality. |

## 2. CHECKLIST SCORECARD

| check | status | one-line basis |
|---|---|---|
| F1 | FINDING | 102 ZERO_STANDING rows reviewed (table in section 5). Four lines need explanation: derecognition gain (A3-01), bad-debt ratio 0.00 (A3-02), nil derivatives with FCCBs (A3-03), security receipts (A3-04). |
| F2 | PASS | S-vs-C PAT gap 0.74%-1.45% of SA PAT across six periods; largest move 0.71pp, below 5pp. No JV or associate. Gap is Nupur less eliminations (table in section 3). Component shifts are logged at F3. |
| F3 | FINDING | Nupur is not a shell (own employee, other expense and depreciation lines). Its P&L and balance sheet are changing shape (A3-05, A3-06). No going concern EoM to reconcile. |
| F4 | FINDING | Auditor-scope exposure bounded at 0.89% of CON PAT, basis not stated (A3-08). Lender reading: about 18.4% of Q2 PAT rests on an ECL write-back under limited review (A3-07). |
| F5 | PASS | No EoM, no Other Matters, no going concern text in either report (l.678-705, l.739-773). No prior-quarter report on file, so no verbatim diff is possible. Baseline quarter recorded. |
| F6 | PASS | Lexicon sweep: "commenced" (l.54, meeting time), "approved" (l.42, l.564, results approval), "will be" (l.139/143/145 template OCI labels). No forward commitment. A1 FORWARD table holds 0 rows. Commitment register empty. |
| F7 | PASS | No hedge-lexicon hit in notes, letter or review reports. "to the extent" (l.603, l.761) is outside the lexicon and is contractual/scope wording. |
| F8 | FINDING | ETR 24.9%-25.6% vs 25.17% statutory; no earlier-year tax line. Current/deferred mix swing and round Q1 deferred tax (A3-09). |
| F9 | FINDING | OCI nil in all periods including audited FY26; no actuarial line visible (A3-10). Verify at AR. |
| F10 | FINDING | Paid-up change traces to note 6. Basic = diluted with FCCBs outstanding per Notion (A3-11). |
| F11 | PASS | SA Equity + Other Equity 1,91,474.68 vs Reg 52 net worth 1,85,675.10: gap 5,799.58 (3.03%), identical on CON (1,93,596.20 vs 1,87,796.62); reconciling items named in the definition (revaluation reserve, deferred expenses, l.627). Notion book Rs 21.85/share vs filed CON Rs 21.18/share (3.2%); Notion figure is pro forma for post-period conversion (Notion-sourced). D/E deck 2.89x (Notion-sourced) vs filed 2.83x (2.1%). Other equity roll-forward ties within 61.63 SA / 49.34 CON. All gaps below 5%. |
| F12 | FINDING | No segment table (Note 4, l.572). Lender reading on the balance sheet: leverage and non-loan asset build (A3-12), marginal funding cost (A3-13), asset cover 1.10x (A3-14), capitalised deferred expenses (A3-15). |
| F13 | FINDING | Results-only outcome with "inter alia"; MD signatures 15 minutes before meeting end (A3-16). No AR/AGM/director/capital item, no Role 6 event. |
| F14 | FINDING | Nine drafting items (A3-17 to A3-25): CON cash flow misposting and non-elimination, mislabelled net profit margin, undefined NIM, garbled UDINs, derived cash flow, regrouped comparatives, cross-entity tax netting, cosmetics. Note 1 says "reviewed" and the letter says "Limited Review"; no audit/review mismatch. |
| F15 | PASS | Consolidation list: Paisalo (parent) and Nupur Finvest (WOS, RBI-registered NBFC), consistent across note 2 (l.567), the CON report (l.740, l.765) and the NCI lines (nil). No prior filed list on record, so this quarter is the baseline. |
| F16 | N.A. | Results filing; presentation check does not apply (doctype rule). |
| F17 | N.A. | Results filing; concall silence audit does not apply (doctype rule). Checklist coverage by this filing is listed in section 7 for A4. |

## 3. F2 DECOMPOSITION (CON minus SA, Rs Lakhs, my arithmetic)

| line | Q2FY27 | Q1FY27 | Q2FY26 | H1FY27 | H1FY26 | FY26 |
|---|---|---|---|---|---|---|
| Total revenue from operations | 496.80 | 566.91 | 818.42 | 1,063.71 | 1,730.08 | 2,629.13 |
| of which interest income | 493.33 | 561.84 | 812.04 | 1,055.17 | 1,717.67 | 2,604.87 |
| Finance costs | 163.59 | 167.99 | 237.37 | 331.58 | 595.76 | 912.60 |
| Impairment | 13.60 | 10.56 | 438.49 | 24.16 | 536.20 | 450.55 |
| Employee benefits | 46.48 | 45.03 | 51.88 | 91.51 | 100.15 | 206.12 |
| Depreciation and amortisation | 0.10 | 0.05 | 0.00 | 0.15 | 0.03 | 0.04 |
| Other expenses | 195.34 | 283.29 | 17.05 | 478.63 | 357.54 | 723.45 |
| PBT | 77.69 | 59.99 | 73.63 | 137.68 | 140.40 | 336.37 |
| Tax (current + deferred) | 19.01 | 15.06 | 0.00 | 34.07 | 16.00 | 84.67 |
| PAT | 58.68 | 44.93 | 73.63 | 103.61 | 124.40 | 251.70 |
| PAT gap % of SA PAT | 0.90% | 0.74% | 1.45% | 0.82% | 1.28% | 1.07% |

Decomposition: JV/associate share nil (none exist); subsidiary contribution as above; eliminations not disclosed separately. The intra-group advance (A3-06) affects the balance sheet and cash flow, not the P&L gap. Q2FY26 subsidiary tax of 0.00 on PBT 73.63 is unexplained but immaterial.

## 4. DRAFTING TALLY (F14, cumulative governance data point)
Nine items this quarter: (1) CON cash flow impairment/CSR misposting 24.16; (2) CON cash flow without intra-group elimination, about Rs 49.02 Cr each side; (3) "net profit margin" computed on PBT; (4) NIM basis undefined and not reproducible; (5) UDINs and firm number unreadable; (6) cash flow derived from balance-sheet deltas, FCCB conversion shown as cash; (7) unquantified regrouping with a two-sided Q2FY26 fair-value entry; (8) cross-entity tax netting; (9) cosmetics (titles, numbering, asterisk, name spelling). Items 1, 2 and 8 all sit in the consolidation layer, and the review basis for the subsidiary is not stated (A3-08). The consolidation process is the weak point.

## 5. F1 ZERO-STANDING LINE REVIEW (why each line exists)

| line (SA ref / CON ref) | status | template purpose / anticipated transaction | A3 reading |
|---|---|---|---|
| Exceptional items (R164-R169 / R642-R647, l.825) | nil except FY26 78.39 | one-off gains/losses | FY26 one-off of Rs 0.78 Cr, also in CF extraordinary items (l.967). H1 nil. Neutral. |
| Discontinued operations IX-XI and their EPS (R194-R211, R291-R302 / R672-R689, R805-R816) | nil all | sale or closure of a business or subsidiary | Schedule III Div III template. A sale or merger of Nupur (A3-05) would appear here. |
| OCI (A)(i) "(Revaluation of Building)" and (B) (R218-R259 / R696-R737) | nil all | revaluation surplus; reclassifiable items | Company-specific label: buildings sit on a revaluation model and a revaluation reserve exists (net worth definition l.627). No revaluation this year. See A3-10. |
| Net gain on derecognition (R044-R049 / R522-R527) | nil all | assignment/securitisation/co-lending gains | A3-01. |
| Rental income, sale of products/services, others, other income (R026-R031, R050-R079 / R504-R557) | nil all | non-lending income | Pure lender; all income in interest, fees, fair value. Neutral. |
| Fees and commission expense (R092-R097 / R570-R575) | nil all | sourcing/BC commissions | Any BC/DSA payouts sit inside other expenses. Neutral; relevant to the other-expense jump. |
| Net loss on derecognition, cost of materials, stock-in-trade, inventories (R101-R133 / R579-R611) | nil all | non-lender template lines | Neutral. |
| Derivative financial instruments, assets and liabilities (R318/R320, R351/R356 / R832/R834, R865/R870) | nil | hedges, embedded options | A3-03. |
| Deferred tax asset, investment property, biological assets, CWIP, intangibles under development, goodwill (R332-R348 / R846-R862) | nil | template | Neutral. No goodwill on the Nupur acquisition. |
| Deposits (R365/R370 / R879/R884) | nil | public deposits | Non-deposit-taking NBFC. Neutral. |
| NCI lines (R750-R779, R900, R905-R906) | nil | minority interest | WOS; consistent with F15. |
| CF: dividend income FY H1FY26, extraordinary items, investment purchases FY26, subordinated liability, dividend H1FY26, security receipts H1FY27, change in other NFA H1FY26 | nil in some columns | cash-flow template | Security receipts A3-04; change in other NFA H1FY26 nil vs 2,459.25 H1FY27 is A3-15. |
| Ratio d preference shares Nil (M-d, l.1217); ratio l bad debts 0.00 (R1092-R1093, l.1227) | Nil / 0.00 | Reg 52(4) template | d neutral; l is A3-02. |

## 6. COMMITMENT REGISTER (F6)

| commitment | implied date | note/turn ref | status word |
|---|---|---|---|
| (none) | - | lexicon sweep over l.17-786: no forward commitment in letter, notes or reports | - |

Dated contractual obligations (not management commitments; for the A4 funding calendar, my arithmetic): CP Rs 38.40 Cr matures 30-Dec-2026 (169 days from 14-07-2026, l.586-587); CP Rs 4.82 Cr matures 22-Feb-2027 (151 days from 24-09-2026, l.590-591); CP Rs 14.37 Cr matures 23-Mar-2027 (180 days from 24-09-2026, l.594-595).

## 7. FOR A4: NOTION CHECKLIST ITEMS THIS FILING EVIDENCES (not an F17 audit; F17 is N.A. on results)
- #2 GNPA 0.66% SA / 0.65% CON (l.1236): green (<1.0%). Tripwire (a) is far away.
- #3 NNPA 0.46% / 0.45% (l.1237): green (<0.7%).
- #6 NIM 6.43% / 6.46% (l.1235): basis undefined (A3-19); below the 6.5% green band; not red.
- #7 Cost-to-income, filed CON (opex / total income less finance cost, Notion method): Q2FY27 40.95%, Q1FY27 32.32%, Q2FY26 35.52% (my arithmetic, l.1013-1027). SA: 40.22%, 30.90%, 36.66%. Upper-bound adjustment for capitalised expenses in A3-15.
- Early warning #5 opex growth: CON Q2 +34.8% YoY on filed numbers (0.2pp below 35%).
- #10 ROA: H1 annualised filed CON PAT / average CON total assets = 3.65% (my arithmetic); deck 3.3% (Notion-sourced).
- #11 ROE: H1 annualised CON PAT / average CON equity = 13.62% (my arithmetic); Notion 13.4%.
- #20 share count: +0.51% in Q2 (filed); Notion 94.01 Cr post-period is +2.8% over filed 91.42 Cr (Notion-sourced).
- #17 RPT borrowing usage: no RPT note in this filing; the Rs 49.02 Cr advance to the WOS (A3-06) is intra-group lending, not promoter RPT borrowing.
- Prior Q1 questions (Notion-sourced) partly answered by this filing: Q3 basis (both SA and CON now filed; gap below 1.5% of PAT); Q10 dividend (H1 dividend paid Rs 4.64 Cr, l.979); Q7 write-offs (ratio l 0.00, see A3-02).
- Out of document, no line cite possible: BSE filing of 22-Oct-2026 on a Reg 60(2) LODR fine, waiver applied (case 283222), amount not disclosed. Not an A3 finding; A4 may raise it from that filing.

## 8. YAML BLOCK

```yaml
stage: A3-forensics
company: "PAISALO"
quarter: "Q2 FY27"
doctype: "results"
model: "claude-opus-5-5"
status: complete
forensics_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\quarterly-paisalo-q2fy27-095262\\runs\\paisalo-q2fy27\\work\\forensics_paisalo_q2fy27_results.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: PASS
  F3: FINDING
  F4: FINDING
  F5: PASS
  F6: PASS
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
  F17: N.A.
findings:
  - {id: "A3-01", check: "F1", line: "fulltext l.804, l.1009", classification: "NEUTRAL-FACT", implication: "Derecognition gain nil in all periods; first line where co-lending/assignment gains would show"}
  - {id: "A3-02", check: "F1", line: "l.1227, l.816", classification: "AMBIGUOUS", implication: "Bad-debt ratio 0.00 vs H1 impairment Rs 15.25 Cr; ask H1 write-offs and ratio denominator"}
  - {id: "A3-03", check: "F1", line: "l.882, l.903, l.598", classification: "AMBIGUOUS", implication: "Nil derivatives while USD FCCBs exist; ask FCCB outstanding, FX hedge, option accounting"}
  - {id: "A3-04", check: "F1", line: "l.980, l.1195", classification: "AMBIGUOUS", implication: "FY26 security-receipts flow Rs 24.43 Cr SA; ask ARC sales and SRs held"}
  - {id: "A3-05", check: "F3", line: "l.1013 vs l.808, l.1027 vs l.822", classification: "AMBIGUOUS", implication: "Nupur revenue -39% YoY, other expenses 11.5x, implied C/I 12%->73%; run-off or re-tool"}
  - {id: "A3-06", check: "F3", line: "l.1099/886, l.1093/880, l.1125/912, l.1101/888, l.1190/975, l.1173/958", classification: "AMBIGUOUS", implication: "Inferred Rs 49.02 Cr parent advance to Nupur; Nupur book -21%, cash Rs 42.95 Cr; ask purpose and Nupur Rs 55.70 Cr debt maturity"}
  - {id: "A3-07", check: "F4", line: "l.816, l.1021, l.699", classification: "FORWARD-SIGNAL", implication: "Q2 PAT growth rests on ECL write-back (~18.4% of PAT); PPOP -11.3% QoQ; Q3 credit-cost normalisation cuts PAT"}
  - {id: "A3-08", check: "F4", line: "l.765", classification: "AMBIGUOUS", implication: "Review basis of Nupur not stated; exposure bounded at 0.89% of CON PAT"}
  - {id: "A3-09", check: "F8", line: "l.828, l.829, l.1034, l.919, l.964", classification: "AMBIGUOUS", implication: "Round Q1 deferred tax (100.00)/(99.00) trued up to 488.70 charge in Q2; ETR stable"}
  - {id: "A3-10", check: "F9", line: "l.842, l.836, l.820", classification: "AMBIGUOUS", implication: "OCI nil incl audited FY26; verify gratuity remeasurement at AR"}
  - {id: "A3-11", check: "F10", line: "l.845, l.848-849, l.1062-1063, l.598", classification: "AMBIGUOUS", implication: "Basic = diluted EPS with FCCBs outstanding (Notion-sourced); A4 cross-check"}
  - {id: "A3-12", check: "F12", line: "l.886, l.887, l.911, l.912, l.1214", classification: "FORWARD-SIGNAL", implication: "D/E 2.41x->2.83x in H1; Rs 225.6 Cr into undisclosed non-loan assets; 3.5x cap within ~3 qtrs without equity"}
  - {id: "A3-13", check: "F12", line: "l.579-585, l.588, l.592, l.596", classification: "FORWARD-SIGNAL", implication: "Q2 NCD coupon 10.26% (unsecured 12.00%) vs book CoB 9.98%; spread pressure as debt rolls"}
  - {id: "A3-14", check: "F12", line: "l.603-605", classification: "AMBIGUOUS", implication: "Asset cover 1.10x after Rs 294.92 Cr new secured NCDs; ask covenant floor and headroom"}
  - {id: "A3-15", check: "F12", line: "l.961, l.950, l.899, l.821, l.627", classification: "FORWARD-SIGNAL", implication: "Rs 24.59 Cr H1 expenses deferred; D&A +152% YoY; expensed SA H1 C/I ~41.9% vs 35.6% (upper bound)"}
  - {id: "A3-16", check: "F13", line: "l.42, l.54, l.179, l.653, l.67", classification: "AMBIGUOUS", implication: "MD signed 10:09-10:10, board ended 10:25, 'inter alia'; ask what else the board transacted"}
  - {id: "A3-17", check: "F14", line: "l.1166, l.1021, l.1167, l.1180", classification: "NEUTRAL-FACT", implication: "CON CF impairment uses SA figure; 24.16 sits in CSR line"}
  - {id: "A3-18", check: "F14", line: "l.1233", classification: "AMBIGUOUS", implication: "Reg 52 'net profit margin' 31.93% is PBT margin; PAT margin 23.90%"}
  - {id: "A3-19", check: "F14", line: "l.1235", classification: "AMBIGUOUS", implication: "NIM 6.43% basis undefined, not reproducible; below 6.5% checklist green band"}
  - {id: "A3-20", check: "F14", line: "l.717, l.784, l.709, l.778", classification: "NEUTRAL-FACT", implication: "UDINs and firm no. unreadable; operator/Claude web to verify on ICAI from source image"}
  - {id: "A3-21", check: "F14", line: "l.981, l.975, l.977, l.963", classification: "NEUTRAL-FACT", implication: "SA CF built from balance-sheet deltas; FCCB conversion shown as cash; use note 5 for gross raises"}
  - {id: "A3-22", check: "F14", line: "l.803, l.814, l.601", classification: "AMBIGUOUS", implication: "Q2FY26 two-sided fair-value entry and unquantified regrouping; YoY base not like-for-like"}
  - {id: "A3-23", check: "F14", line: "l.248, l.497, l.850-852, l.1070, l.655", classification: "NEUTRAL-FACT", implication: "Cosmetic drafting tally"}
  - {id: "A3-24", check: "F14", line: "l.1130 vs l.917, l.1132 vs l.919", classification: "NEUTRAL-FACT", implication: "Subsidiary tax asset netted against parent liability in CON"}
  - {id: "A3-25", check: "F14", line: "l.1190, l.1173, l.1183", classification: "NEUTRAL-FACT", implication: "CON CF not eliminated for intra-group advance; CFO and CFF each overstated ~Rs 49.02 Cr"}
forward_signals: ["A3-07", "A3-12", "A3-13", "A3-15"]
ambiguous: ["A3-02", "A3-03", "A3-04", "A3-05", "A3-06", "A3-08", "A3-09", "A3-10", "A3-11", "A3-14", "A3-16", "A3-18", "A3-19", "A3-22"]
commitments: []
gate_a3: pass
blank_checks: []
analyst_note: "Q2 PAT growth comes from an ECL estimate, not operations. Impairment moved from a Rs 15.63 Cr charge to a Rs 0.38 Cr write-back. PPOP fell 11.3% QoQ, and only a limited review covers it (A3-07). Opex is understated by capitalisation: Rs 24.59 Cr went into other non-financial assets in H1 against Rs 6.68 Cr written off. The Reg 52 net worth deducts 'Deferred Expenses', so the company itself treats the pool as non-capital (A3-15). Expensed, SA H1 cost-to-income is about 41.9%, not 35.6% (upper bound). The consolidated cash flow is the plain sum of parent and Nupur. A Rs 49.02 Cr parent advance to Nupur sits gross in both operating and financing lines (A3-06, A3-25), while Nupur shrinks its book and holds Rs 42.95 Cr cash. Three of nine drafting errors sit in the consolidation layer. Reg 52 'net profit margin' is a PBT margin. NIM 6.43% does not reproduce and sits below the 6.5% green band that Notion's ruling text calls green. The Reg 60(2) fine is out of document, so A3 records no finding."
```
