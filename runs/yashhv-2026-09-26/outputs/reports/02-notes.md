# STAGE 2: NOTES TO FINANCIAL STATEMENTS, TRIPLE PASS
Company: Yash Highvoltage Ltd (YASHHV) | Run date: 2026-09-26
Source: Annual Report FY26 (RUN/work/extracted/annual-report/Annual_Report_2026.txt),
prior year AR FY25, RHP (2024-12).

## PASS 3: PATTERN PASS

Targeted re-read for contradictions, mismatches, restatement/reclass patterns,
subsequent events, and going-concern language, on top of Pass 1 (full
extraction, 10 findings) and Pass 2 (gap pass, 6 new findings).

- Going concern: checked both standalone and consolidated auditor's report
  boilerplate (SA 570 paragraphs, p.[105-ish]/[10060-10115 in raw text]) and
  the Board's Report Section 34 (Significant Material Orders, p.[4409-4416]).
  No going-concern qualification, no material uncertainty, no adverse order
  affecting ongoing-concern status. CONFIRMS Pass 1/Pass 2: NONE.
- Contradiction check: Pass 2's Finding 1 (FY25 CFO Rs 918.68L IGAAP vs
  Rs 953.13L Ind AS restated, +Rs 34.45L undisclosed) and Pass 1's Finding 4
  (Ind AS 101 adoption "fully explained") are in tension: the reserve-level
  reconciliation is complete but the cash-flow-statement-level reconciliation
  is not. This pass resolves the tension by DOWNGRADING Pass 1 Finding 4's
  characterisation from "fully explained" to "reserve/P&L level explained,
  cash-flow level not reconciled" — carried into Top 15 below as two
  separate line items rather than one.
- Restatement vs main statements: no numeric mismatch found between Note 45
  disclosed FY26 closing stock-statement figures and the face Balance Sheet
  inventory line; the discrepancy is bank-vs-books within the note itself,
  already captured (Pass 2 escalation).
- No new events after balance sheet date beyond what Pass 1/2 already carry
  (cyber fraud is H2FY26, inside the year; the Aug-2026 preferential
  allotment is a B00 input_gap item, outside Notes scope, not renamed here).
- Deliberately vague vs detailed disclosure: Note 45 (2 of 12 quarters
  explained) stands out against the otherwise granular note style
  elsewhere (e.g. Note 36 RPT, Note 10 ageing). No further such pairs found.

PASS 3 verdict: no wholly new finding beyond the CFO-reconciliation /
restatement-completeness tension already surfaced in Pass 2; that tension is
resolved above and folded into the consolidated Top 15, not treated as a
fresh Pass 3 item. Not an empty pass (the going-concern re-check and the
contradiction resolution are load-bearing), but no new finding line is
added beyond what Pass 1 + Pass 2 already carry.

FIRST VERIFICATION PRIORITY (from task): LBF2 cash conversion and LBF3
restatement/controls, pass-3 disposition:
- LBF2 cash conversion: NOT CLEARED. Confirmed deteriorating on two of three
  legs (receivables ageing composition, inventory turnover) even though
  turnover-ratio and DSO both nominally improved; CFO Rs 8.83cr vs PAT
  Rs 37.34cr FY26 stands unexplained by any single note. Remains a FLAG-CASH
  item into synthesis.
- LBF3 restatement/controls: PARTIALLY CLEARED. The Ind AS 101 first-time
  adoption is a standard, auditor-flagged (Emphasis of Matter, unmodified
  opinion), reserve-and-P&L-level explained restatement — not an
  earnings-quality restatement. NOT CLEARED at the cash-flow-statement
  level: the FY25 CFO figure moved Rs 34.45L between the FY25 AR and the
  FY26 AR's restated comparative with no disclosed reconciliation. The
  cyber fraud (Rs 2.10cr) is a control-design finding (mandate + banker
  confirmation obtained, fraud still succeeded) rather than a restatement
  question, and remains YELLOW. Company Secretary change (May-2026) is
  outside Notes scope (governance/other-source item, not evidenced in
  Notes); not resolved here.

═══════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Bank quarterly stock-statement discrepancy: 3-year, 12-quarter, near-universally one-directional pattern (books > bank-reported stock), peaking every fiscal year-end (Mar-24 -12.18%, Mar-25 -25.35%, Mar-26 -17.76%); only 2 of 12 quarters carry any stated reason | Note 45, p.143-144 | RED | Systemic control-design/disclosure-appetite question bearing directly on true drawing-power-backed liquidity (LBF2) |
| 2 | Trade receivables not-due bucket collapsed from 68% (FY25) to 3% (FY26) of total, despite the turnover ratio nominally improving 7.44x to 8.07x | Note 10, p.114-115 | RED | Q4 billing-concentration signal that contradicts the turnover-ratio improvement; feeds LBF2 |
| 3 | FY25 CFO differs by +Rs 34.45L between the FY25 AR (Rs 918.68L, IGAAP) and the FY26 AR restated comparative (Rs 953.13L, Ind AS); no formal Ind AS 101 cash-flow reconciliation disclosed | Standalone Cash Flow p.101-102; FY25 AR Cash Flow p.39; Annexure A p.153-157 | RED | The cash-flow number central to the operator's LBF2 test changed between filings with zero signposting; downgrades Pass 1's "fully explained" restatement finding |
| 4 | Inventory +124.7% YoY vs revenue +57.2%; inventory turnover fell 5.83x to 4.88x | Note 9 p.113 / Note 53 p.147 | YELLOW | Working capital, not only capex, is absorbing operating cash flow |
| 5 | Ind AS 101 first-time adoption (transition date 1-Apr-2024) reserve/P&L-level reconciliation complete for FY25/H1FY26 RESTATED labels; six named drivers; net reserve effect only -Rs 6.93L / -Rs 15.40L; auditor Emphasis of Matter, opinion unmodified | Note 1.1 p.105; Annexure A p.153-157 | GREEN (with the Rank 3 caveat) | Standard first-time-adoption disclosure, not an earnings-quality restatement, at the balance-sheet/P&L level |
| 6 | Ind AS 101 P&L reconciliation's two largest lines (Other Expenses -Rs 93.62L, Revenue -Rs 56.74L, FY25) not individually itemised against the six named drivers; only partial traceability via Note 38 lease reclassification | Annexure A p.155-157; Note 38 p.140 | YELLOW | Disclosure-completeness gap in the very note the pipeline relies on to clear LBF3 |
| 7 | Rs 2.10 crore cyber fraud exceptional item; fraud succeeded despite the company obtaining a supporting mandate and banker confirmation before paying | Note 49, p.129-130; consol auditor report p.155 | YELLOW | Control-design finding, not simply external bad luck; auditor Emphasis of Matter, opinion unmodified |
| 8 | Customer concentration rose: single customer = 18.8% of FY26 revenue (Rs 44.17 Cr), vs two customers at ~10.4% each in FY25 | Note 50, p.146 | YELLOW | Feeds LBF1 guidance-vs-delivery test; a single order can move the invoicing number |
| 9 | KMP compensation to promoter-MD doubled YoY (Rs 140.02L to Rs 289.34L, +106.6%); new promoter-family office/car rent and rent-deposit arrangements booked for the first time | Note 36, p.131-134 | YELLOW | RPT quantum and new categories both rising in the same year dividend and ESOP started |
| 10 | Forward contract derivative recognised at Ind AS transition has no traceable outstanding position in FY25/FY26 fair value hierarchy or market risk note, even as USD trade receivables grew ~8x and net USD FX sensitivity flipped from -Rs 8.37L (FY25) to +Rs 29.99L (FY26) | Note 44 p.142-143; Note 46(C) p.144-146; Annexure A p.157 | YELLOW | Rising export receivable exposure appears unhedged in current disclosure; feeds LBF1 export-ramp cross-check |
| 11 | CFO Sumit Poddar (23,500 options) and director Hartmuth Fethake (8,000 options) named as FY26 ESOP grant holders | Note 36(e), p.138 | YELLOW | CFO is both preparer and personal beneficiary of the scheme in a year with rising RPT quantum and open cash-conversion questions |
| 12 | Auditor remuneration rose 78.7% YoY (Rs 6.90L to Rs 12.33L; audit fee Rs 5.38L to Rs 10.00L, +85.9%) in the year the auditor communicated zero Key Audit Matters | Note 40, p.140 | YELLOW | Sharpens the nil-KAM disclosure-appetite observation |
| 13 | No covenant breaches on any borrowing; gearing low at 16.90%; payables grew only 2.6% YoY vs inventory +124.7% (not stretching suppliers to fund WC build) | Note 47 p.147; Note 21 p.120-122 | GREEN | Balance-sheet discipline intact despite working-capital strain |
| 14 | Contract liabilities (customer advances) up 335.6% YoY (Rs 244.69L to Rs 1,066.04L) | Note 26, p.126-127 | GREEN | Genuine forward-order signal consistent with the order-book narrative, though collected cash is not yet booked revenue |
| 15 | New 50% JV Sukrut Electric (Rs 535L, acquired 8-Jan-2026) posted a loss in its first consolidated quarter; two new wholly owned subsidiaries (Power Component, USA Inc) immaterial to date | Note 5 p.117; Note 51 p.207-208 consol | YELLOW | Fresh corporate-structure sprawl to track, though sizes are immaterial today |

## B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | No aggressive recognition finding across three passes; contract liability growth consistent with billing timing, not premature booking |
| Expense capitalisation honesty | 7 | No capitalisation-threshold abuse or impairment-assumption red flag found; cyber fraud correctly expensed as exceptional, not buried |
| Provisioning adequacy | 6 | ECL/provisioning notes present and Ind AS 109-compliant post-transition; no stress-tested against the receivables ageing collapse (Finding 2) which raises the question but does not yet show under-provisioning |
| RPT fairness | 5 | KMP pay doubling, new promoter-family rent arrangements, and CFO/director personal ESOP stake all land in the same year as rising cash-conversion strain; no non-arm's-length pricing proven, but the pattern warrants caution |
| Disclosure transparency | 4 | Note 45's 12-quarter, near-universally unexplained bank-stock discrepancy, nil KAM in a year of rising audit fees, and the CFO-figure change between filings with no reconciliation are all disclosure-appetite concerns |
| Consistency with prior years | 5 | Ind AS 101 transition is well-reconciled at reserve/P&L level but not at cash-flow level; the FY25 CFO number itself is inconsistent across the two annual reports |
| **OVERALL** | **5/10** | Moderate. Core accounting (revenue, expense, provisioning) is clean; the drag is disclosure transparency and cash-flow consistency, both directly load-bearing for the pipeline's LBF2/LBF3 tests |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Cash conversion gap widening (receivables composition + inventory build) | HIGH | H1FY27 ageing schedule; CFO vs PAT ratio; DSO trend | Next half-yearly result (est. Nov-2026) |
| Bank stock-statement discrepancy unexplained and growing | HIGH | Whether Note 45 in FY27 AR names causes; drawing-power/borrowing-base implications | Next AR (FY27, ~Aug-2027) or any covenant review |
| Restatement traceability gap at cash-flow-statement level | MEDIUM | Any further re-presentation of FY25/FY26 cash flow in subsequent filings | Next filing that repeats a prior-year cash flow column |
| RPT/KMP pay escalation concurrent with cash strain | MEDIUM | Board/AC minutes on KMP pay revision; further promoter-family arrangements | AGM disclosures, next AR RPT note |
| Customer concentration (18.8% single customer) | MEDIUM | Whether concentration persists or diversifies as order book executes | H1FY27/FY27 segment and customer notes |
| Unhedged rising USD receivable exposure | MEDIUM | INR/USD move; whether a hedging policy is adopted | Any material INR depreciation before FY27 close |
| Nil KAM with rising audit fee, new JV/subsidiary sprawl | LOW-MEDIUM | Whether FY27 audit report continues nil KAM despite corporate complexity | FY27 auditor's report |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. What caused the FY25 CFO figure to move from Rs 918.68 lakh (FY25 AR) to Rs 953.13 lakh (FY26 AR's restated comparative), and why is there no line-item cash-flow reconciliation in the Ind AS 101 transition note?
2. What is the root cause of the recurring, near-universally one-directional bank-vs-books stock-statement discrepancy across 12 consecutive quarters, and why do only 2 of those quarters carry a stated reason?
3. Why did the trade-receivables not-due bucket fall from 68% to 3% of the total in FY26 even as the reported turnover ratio nominally improved, and how much of Q4 FY26 revenue was billed in March?
4. What internal control gap allowed the Rs 2.10 crore cyber fraud to succeed despite an obtained supporting mandate and banker confirmation, and what has changed in the payment-authorisation process since?
5. Is there a company hedging policy for the growing USD trade receivable book, given the forward-contract balance recognised at Ind AS transition shows no traceable outstanding position in the FY26 fair-value or market-risk notes?

## E. NOTES-BASED RED FLAGS

- Earnings management: none proven; revenue recognition and expense capitalisation both read clean across three passes.
- Aggressive accounting: none found; the Ind AS 101 transition is a standard first-time-adoption exercise at reserve/P&L level, auditor-flagged with an unmodified opinion.
- Undisclosed risk indicators:
  - Bank quarterly stock-statement discrepancy, systemic, 12-quarter, mostly unexplained (Note 45).
  - FY25 CFO figure inconsistency between two annual reports with no reconciliation.
  - Unhedged USD receivable growth against a dormant forward-contract disclosure.
  - Receivables ageing composition deteriorating sharply even as the summary turnover ratio improves (an internal contradiction within the same note set).

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, clean on recognition and provisioning but weak on disclosure follow-through. Key concern: the bank stock-statement discrepancy and the unreconciled FY25 cash-flow figure both bear directly on the cash-conversion question the operator most needs answered. Key strength: no covenant breaches, disciplined payables, and a fully reserve-level-explained Ind AS 101 transition with an unmodified audit opinion. Overall accounting quality: 5/10.
