# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 2 (WHAT WAS MISSED)
Company: Yasho Industries Ltd (YASHO) | Run date: 2026-09-05
Source: Annual_Report_2026.pdf.txt (FY2026 audited). Cross-checked against Pass 1 output
(02-notes-pass1.md) note by note, Note 1 through Note 56, standalone (SA) and consolidated
(CON). This pass reports ONLY items not already covered in Pass 1. Ratings: 🟢 Clean | 🟡 Watch |
🔴 Red Flag.

Method: re-read every note against the Pass 1 extraction. Notes fully covered (1-6, 10, 21, 25,
36, 37, 38, 50, 52-53, 54 events, GST/contingent detail, EPS, share capital roll-forward, CSR
detail) are skipped below. Fresh material below concentrates on Notes 7-9, 14, 15, 19, 22.1
sub-detail, 26-33 P&L detail, 34-35 tax mechanics, 39 cross-references, 40-46 financial
instruments/risk/capital-management block (largely unexamined in Pass 1, which anchored mainly
on Note 45 ratios and Note 46 drawing-power), and consolidated Note 46's Schedule III
profit/net-asset attribution table.

═══════════════════════════════════════════════════════════════
NEW FINDING 1 — 🔴 Consolidated profit "eliminated on consolidation" is large, volatile, and
connects directly to the intercompany-receivables red flag Pass 1 raised
═══════════════════════════════════════════════════════════════
Note 46 (Consolidated, "Additional Information as required under Schedule III," printed p.213)
gives the full attribution table Pass 1 only partially quoted. Full reconciliation (Rs lakh):

| Entity | FY26 profit contribution | FY25 profit contribution |
|---|---|---|
| Parent (standalone) | 2,147.90 | 602.49 |
| Yasho Industries Europe B.V. | 414.43 | 271.97 |
| Yasho Inc. | 118.81 | 139.91 |
| Sum of entities | 2,681.14 | 1,014.37 |
| **"Adjustments arising out of consolidation"** | **(155.34)** | **(403.86)** |
| Consolidated total | 2,525.79 (matches co. memory Rs 25.26 cr) | 610.52 |

In FY25 the consolidation adjustment erased **66.15%** of the combined parent + subsidiary
profit (Rs 403.86 lakh wiped off a Rs 1,014.37 lakh base). In FY26 it erased 6.15% (Rs 155.34
lakh off Rs 2,681.14 lakh) — the adjustment shrank 61.5% YoY even as intercompany trade
receivables (Note 39/Note 11, flagged 🔴 in Pass 1) grew 78.7% and intercompany sales grew only
15.9%. An adjustment of this kind is standard practice ONLY for unrealised-profit elimination on
inventory the subsidiaries have bought from the parent and not yet resold; its size and
direction should move with intercompany closing inventory, not away from it while intercompany
receivables balloon. The AR gives zero narrative on what "Adjustments arising out of
consolidation" comprises in either year — no split between unrealised-profit elimination, FX
translation of intercompany balances, or other consolidation entries. This is a materially larger
and more central number than Pass 1's DSO-based flag alone suggested, and it directly bears on
how much of the "sales to subsidiaries" trail is real, cash-backed profit versus an accounting
construct waiting to unwind. (Note 46 CON, Schedule III table, printed p.213)

Net-asset side of the same table: consolidation adjustment to net assets was -Rs 1,146.47 lakh
(FY26, -2.58% of consolidated net assets) vs -Rs 947.66 lakh (FY25, -2.26%) — this component grew
21% even as the P&L-side adjustment shrank, a further internal inconsistency in the same note
that the AR does not reconcile.

Also newly visible in this table: Yasho Inc. had NEGATIVE total comprehensive income in FY25
(-Rs 12.61 lakh) despite POSITIVE profit of Rs 139.91 lakh, driven by a -Rs 152.52 lakh OCI
FX-translation loss that alone exceeded the entity's profit. 🟡 Watch — a wholly-owned
subsidiary whose FX translation losses can exceed its trading profit in a given year.

═══════════════════════════════════════════════════════════════
NEW FINDING 2 — 🔴 FX/hedging P&L volatility not previously flagged: three separate
FX-related line items moved sharply and in inconsistent directions
═══════════════════════════════════════════════════════════════
Pass 1 flagged EUR liability exposure growth (+160%) as a standalone balance-sheet item but did
not trace it through to the P&L. Three separate FX-linked lines, none discussed in Pass 1:

- Note 31 (Finance Cost, SA, p.135): "Forward Contract Gain/Loss" of Rs 491.54 lakh (FY26) vs
  Rs 111.56 lakh (FY25), **+340.6% YoY** — booked inside Finance Cost, i.e. treated as a cost/loss
  line, not netted against Other Income. Total Finance Cost still fell 7.3% YoY only because
  interest expense fell more (interest on secured borrowings -12.4%), masking a large embedded
  swing in hedging cost.
- Note 26 (Revenue, "Other Operating Revenue," SA and CON, p.134-135/~186): "Foreign exchange
  gain" of Rs 1,613.78 lakh (FY26) vs Rs 714.54 lakh (FY25), **+125.9% YoY**, booked as revenue.
- Note 9 (Other Assets, current, SA, p.124): "Forward Contract Receivable" Rs 0 (FY26) vs Rs
  67.61 lakh (FY25) — a derivative asset that existed at FY25 year-end has fully unwound to nil.

None of these three lines is cross-referenced to the others, to the EUR/USD exposure table
(Note 43), or to the risk-management narrative (Note 41), despite all four notes describing the
same underlying FX/hedging activity. A Rs 4.92 cr swing in hedging losses embedded in finance
cost, alongside a Rs 8.99 cr swing in FX gains embedded in revenue, in the same year the company
also disclosed a 160% jump in EUR liabilities, is a materially larger FX story than the Note 43
balance alone conveys. 🔴 Red Flag — not fraud-indicative on its own, but a disclosure-assembly
gap that prevents an investor from netting the company's TRUE realised FX/hedging P&L impact
for FY26 from the notes as presented.

Compounding this: Note 42 (Financial Instruments — Accounting Classification and Fair Value,
both SA p.150 and CON p.208) lists NO derivative/forward-contract line item at all in either
year's asset or liability classification table, even though Note 9 shows a Rs 67.61 lakh forward
contract receivable at FY25 year-end. Ind AS 107 classification tables should capture all
recognised financial instruments; this appears to be an incomplete classification table. 🟡 Watch.

═══════════════════════════════════════════════════════════════
NEW FINDING 3 — 🟡 Note 45 ratio table: Pass 1 covered only 2 of 11 disclosed ratios; several
untouched ratios add real signal, one materially so
═══════════════════════════════════════════════════════════════
Pass 1 quoted only Trade Receivables Turnover and Trade Payables Turnover from Note 45 (SA,
p.152-153). The full table has 11 ratios; new items:

- **Debt Service Coverage Ratio: 1.04x (FY26) vs 1.08x (FY25), -4.07%.** DSCR barely above 1.0x
  means net profit + depreciation + amortisation + finance cost covers interest, principal
  repayment and lease-liability repayment with almost no headroom. Against a capex ramp (capital
  commitments nearly quadrupled to Rs 27.51 cr per Note 37) and Rs 1,560.10 lakh of current
  maturities of long-term debt due within a year (Note 20), a DSCR this close to 1.0x leaves
  little buffer if FY27 earnings growth disappoints or if the Pakhajan/MNC capex draws working
  capital faster than planned. 🟡 Watch, elevated to a monitoring priority given the capex
  timeline in Note 48.
- Current Ratio 1.34x (FY26) vs 1.38x (FY25), -3.18%. Company's stated reason: "optimised the
  Working Capital use" — directionally plausible (matches the inventory efficiency gain Pass 1
  flagged 🟢) but the same boilerplate-explanation pattern Pass 1 flagged for payables turnover
  recurs here.
- Net Capital Turnover Ratio 6.57x (FY26) vs 9.71x (FY25), **-32.34%** — a materially large
  deterioration (working capital intensity per rupee of revenue worsened sharply), using the SAME
  boilerplate explanation ("higher earnings and monetisation of the plant capacity") that is
  reused verbatim for four different ratios in this note (payables turnover, DSCR, ROE, net
  profit ratio, net capital turnover — 5 of 11 rows share identical wording regardless of whether
  the ratio improved or worsened). This is the clearest instance yet of the documentation-quality
  defect Pass 1 flagged once (finding 8); it recurs across at least five rows, not one. 🟡 Watch,
  escalated from an isolated defect to a pattern across the note.
- Return on Equity 4.98% (FY26) vs 1.69% (FY25), +195.3%; Net Profit Ratio 2.63% vs 0.90%,
  +192.0%; Return on Capital Employed 8.43% vs 6.70%, +25.8% — all consistent with the
  profitability recovery already known from the P&L; no new signal beyond confirming the turnaround.

═══════════════════════════════════════════════════════════════
NEW FINDING 4 — 🟡 Capital management / gearing ratio disclosure (Note 41 SA / Note 41 CON) —
a distinct, board-approved metric Pass 1 did not extract
═══════════════════════════════════════════════════════════════
Standalone gearing ratio: 54.28% (FY26) vs 55.82% (FY25); Net Debt Rs 52,397.41 lakh (FY26) vs
Rs 53,138.93 lakh (FY25), -1.4%; Total Equity Rs 44,131.46 lakh. Consolidated gearing ratio:
54.09% vs 55.81%; Net Debt Rs 52,291.85 lakh. Company's own policy band is 30%-75%, so both years
sit comfortably inside the band and the trend is a modest improvement — 🟢 consistent with the
Note 15 deleveraging Pass 1 already flagged as clean.

More useful than the ratio itself is the accompanying maturity-profile table (Note 41E,
"contractual undiscounted payments"): of total financial liabilities (ex-lease) of Rs 54,094.07
lakh, **Rs 23,386.05 lakh (43.2%) is classified "On Demand"** — working-capital borrowings
callable at the lender's discretion. Read alongside Pass 1's Red Flag 4 (bank drawing-power
statements differing from books by Rs 31.7-52.7 cr every quarter), nearly half the company's
total financial-liability stack sits in a facility category where a bank could, in principle,
call the loan if it took a stricter view of the drawing-power variances. The AR states covenant
compliance is clean and offers a benign explanation for the variances (FX timing, late invoice
booking); the "on demand" classification is a structural fact worth carrying forward as context
for how much cushion exists if that benign read is ever challenged. 🟡 Watch — new context on an
existing flag, not a new item wholly divorced from Pass 1's finding.

═══════════════════════════════════════════════════════════════
NEW FINDING 5 — 🟡 Consolidated foreign-currency exposure note (Note 43 CON) partially resolves,
but does not close, the EUR-liability-growth item Pass 1 flagged
═══════════════════════════════════════════════════════════════
Pass 1 flagged standalone EUR financial liabilities growing 160% YoY (EUR 0.49mn to EUR 1.09mn,
Rs 456.36 lakh to Rs 1,185.42 lakh) as unexplained. The CONSOLIDATED equivalent (Note 43 CON,
printed p.~209) shows EUR liabilities of only EUR 0.29mn = Rs 320.73 lakh (FY26) vs EUR 0.00mn =
Rs 7.55 lakh (FY25) — i.e., roughly 73% of the standalone EUR liability balance eliminates on
consolidation, meaning most of it is intercompany debt owed to Yasho Industries Europe B.V., not
third-party currency risk. This is a genuine, useful clarification the AR itself never states
explicitly (no cross-reference between Note 43 SA and Note 43 CON). It does NOT fully close the
flag: the external (consolidated) EUR liability still grew from a near-zero Rs 7.55 lakh base to
Rs 320.73 lakh, a real new third-party EUR exposure, just far smaller in absolute terms than the
standalone number implied. 🟡 Watch, refined not resolved.

Separately new: the consolidated NET USD asset cushion (USD financial assets minus USD financial
liabilities) shrank sharply — Rs 549.09 lakh net USD asset position (FY26) vs Rs 1,805.93 lakh
(FY25), a **-69.6% YoY contraction** in the natural USD hedge, driven by USD financial assets
falling from USD 7.85mn to USD 5.59mn while USD liabilities held roughly flat (USD 5.74mn to USD
4.99mn). The company describes itself as having a "net USD asset position (natural partial
hedge)" — that cushion nearly disappeared this year, a new and standalone-invisible fact (only
visible by comparing Note 43 CON's own two years). (Note 43 CON, printed p.~209) 🟡 Watch.

═══════════════════════════════════════════════════════════════
NEW FINDING 6 — 🟡 Zero current tax provision in FY26 despite Rs 28.99 cr PBT; entire tax
charge is deferred, with no brought-forward-loss or MAT-credit narrative
═══════════════════════════════════════════════════════════════
Note 35A (SA, p.138): Current Tax = **Rs NIL** (FY26) vs a Rs 83.49 lakh CREDIT (FY25, earlier-
year tax); Deferred Tax = Rs 750.62 lakh (FY26) vs Rs 314.56 lakh (FY25); Total tax charge Rs
750.62 lakh (FY26) vs Rs 231.07 lakh (FY25). The company reported Profit Before Tax of Rs
2,898.52 lakh (FY26, per Pass 1's effective-rate calc) yet paid or provided ZERO current-year
income tax, with the full charge routed through deferred tax. Sec 115BAA (concessional-rate
election, confirmed Note 35A) does not by itself explain a zero current-tax provision on
profitable operations; the most common explanation is utilisation of brought-forward business
losses or unabsorbed depreciation from the Pakhajan capex build-out years, but the AR discloses
no brought-forward-loss schedule, no unabsorbed-depreciation carry-forward table, and (per Pass
1) no MAT credit entitlement anywhere in the notes. This is a legitimate open question for
management: what specifically shelters FY26's current tax to nil, and for how many more years
does that shelter run. 🟡 Watch — a new item, distinct from Pass 1's effective-tax-rate
reconciliation finding, which addressed the blended (current+deferred) rate, not the current-tax
component in isolation.

═══════════════════════════════════════════════════════════════
NEW FINDING 7 — 🟡 Director-loan interest rate is disclosed NOWHERE as a stated %, unlike every
bank tranche
═══════════════════════════════════════════════════════════════
Note 15 (SA, p.128-129) states the exact rate for every secured bank tranche (e.g., "borrowing
carries interest rate of 7.5% to 8.5% p.a. payable at monthly rest," Tranche 1 narrative). For
"Loans From Directors" Rs 4,650.00 lakh (FY26, 9.5% of the Rs 54,094 lakh total financial-
liability book), no rate is stated anywhere in Note 15 or Note 39 — Pass 1's ~9.5% implied rate
is a derived estimate (interest paid / average balance), not a disclosed contractual rate. This
is a disclosure ASYMMETRY worth naming as its own finding: full rate transparency for arm's-
length bank debt, zero rate transparency for promoter-director debt of comparable scale to a
single bank tranche. 🟡 Watch — sharpens Pass 1's rate-differential finding (originally framed
as "the rate is higher"; the sharper point is "the rate is never actually stated, only inferable").

═══════════════════════════════════════════════════════════════
NEW FINDING 8 — 🟡 Note 19 makes an EXPLICIT cross-reference from the advance-received balance
to Note 48 (the MNC contract KAM) that Pass 1 only inferred
═══════════════════════════════════════════════════════════════
Note 19 ("Other Non-Current Liabilities," SA, p.132): "Advances received from customers **(Refer
Note 48)** — Rs 2,744.97 lakh (FY26) vs Rs 0 (FY25)." This is the FIRST explicit textual link in
the AR between a quantified rupee figure and Note 48 (the qualitative, zero-figure MNC-contract
KAM note). Pass 1 treated the Rs 29.52 cr total customer-advance figure as "plausibly but not
explicitly" tied to the MNC contract; Note 19's own cross-reference confirms that AT LEAST the
non-current portion (Rs 27.45 cr of the Rs 29.52 cr total, i.e. ~93%) is explicitly, not
inferentially, linked by the company itself to Note 48. This tightens rather than resolves the
top verification priority: the AR now affirmatively states Rs 27.45 cr of customer advances
relate to the long-term supply agreement, still roughly 28% of company memory's Rs 98.12 cr
figure. (Note 19 SA, p.132; Note 48 SA, p.155) 🔴 carried forward at Pass 1's severity, now with
a stronger textual anchor.

Also newly visible: the auditor's own KAM procedure description (Independent Auditor's Report,
KAM section, p.94-95, quoted only partially in Pass 1) explicitly names "**minimum supply
commitments and potential penalties**" as part of what was evaluated for this contract — meaning
the 15-year MNC agreement includes take-or-pay / minimum-offtake style terms with penalty
exposure, a commercial fact never stated anywhere in Note 48's own qualitative text. The KAM
description is, ironically, more informative about deal terms than the note it is auditing. 🟡
Watch — a real contractual term (penalty exposure) that exists per the auditor's own account but
is entirely unquantified and unmentioned in the substantive note.

═══════════════════════════════════════════════════════════════
NEW FINDING 9 — 🟡 MSME interest disclosure is internally inconsistent (Note 22.1)
═══════════════════════════════════════════════════════════════
Note 22.1 (SA, p.132-133) rows (A) and (E) both show "Interest accrued and remaining unpaid" of
Rs 61.62 lakh (FY26) vs Rs 46.99 lakh (FY25) — i.e., the company acknowledges interest is owed
and unpaid to MSME vendors under Section 16 of the MSME Development Act. Yet rows (C) "Amount of
interest due and payable for the period of delay" and (D) "Further interest due and payable even
in succeeding years" both show "-" (nil) in BOTH years. Rows (A)/(E) and rows (C)/(D) cannot both
be literally true simultaneously if any interest genuinely accrues under Section 16 — either the
Rs 61.62 lakh in (A)/(E) is a management estimate not yet crystallised as "due and payable" under
the Act's own mechanics, or rows (C)/(D) are populated with boilerplate zeros regardless of the
actual position (the same pattern-level documentation-quality issue as the ratio-note boilerplate
in Finding 3 above). Either reading is unflattering: either the accrued-interest number is a soft
estimate, or the "due and payable" rows are not being completed accurately. 🟡 Watch — new,
reinforces the broader documentation-care theme rather than adding a new dollar-figure concern.

═══════════════════════════════════════════════════════════════
NEW FINDING 10 — 🟡 Unexplained swings in two "Other Assets" lines, plausibly capex-related but
unstated
═══════════════════════════════════════════════════════════════
Note 9 (SA, p.124): GST Refund Receivable fell from Rs 1,126.37 lakh (FY25) to Rs 217.35 lakh
(FY26), **-80.7%**, while Custom Duty Paid in Advance rose from Rs 90.36 lakh to Rs 757.96 lakh,
**+739%**. Both are plausibly connected to the Pakhajan capex ramp (customs duty on imported
plant/machinery; GST refunds cycling through as export-linked claims are received) but the note
gives no narrative link, and the swings are large enough (Rs 9.09 cr and Rs 6.68 cr respectively)
to be worth a direct management question rather than an assumed explanation. 🟡 Watch.

═══════════════════════════════════════════════════════════════
NEW FINDING 11 — 🟢/🟡 R&D spend up sharply; catch-all "Other Expense" line up sharply with no
breakdown
═══════════════════════════════════════════════════════════════
Note 33 (Other Expenses, SA, p.135): Research & Development Expense Rs 196.92 lakh (FY26) vs Rs
56.10 lakh (FY25), **+251.0%** — a genuine positive signal of capability investment, not
previously extracted. 🟢. Against this, the generic "Other Expense" line item (a distinct,
unbroken-down catch-all within Note 33, separate from R&D, legal, insurance etc.) rose from Rs
828.29 lakh to Rs 1,400.41 lakh, **+69.1%**, with no sub-components disclosed — the largest
percentage mover in the entire Note 33 table after R&D, and it is the one line the note does not
itemise further. 🟡 Watch — modest in absolute size (Rs 5.72 cr increase) but a disclosure gap
at the point of the note's least transparency.

═══════════════════════════════════════════════════════════════
PASS 2 NEW FINDINGS SUMMARY
═══════════════════════════════════════════════════════════════

Eleven new findings surfaced on the second read-through, none contradicting Pass 1 but several
materially sharpening it. Two stand out for escalation into the Pass 3 consolidation:

1. The consolidated "Adjustments arising out of consolidation" line (Note 46 CON Schedule III
   table) erased 66% of combined group profit in FY25 and 6% in FY26, with no narrative
   breakdown, moving in the OPPOSITE direction to the 78.7% growth in intercompany trade
   receivables Pass 1 flagged as its #2 finding — these two notes, read together, raise more
   doubt about the quality of intercompany-linked profit than either did alone. (🔴, Note 46 CON,
   p.213)
2. FX/hedging P&L volatility (Forward Contract Gain/Loss in Finance Cost +340.6% YoY; FX gain in
   Revenue +125.9% YoY; a forward-contract derivative asset unwinding to nil) was invisible in
   Pass 1's balance-sheet-only EUR exposure flag and is large enough, and scattered across enough
   separate notes (9, 26, 31, 42, 43), to independently warrant a 🔴 rating for disclosure
   fragmentation. (Note 31 p.135, Note 26 p.134, Note 9 p.124)
3. The DSCR of 1.04x (Note 45) — a genuinely new number, not derivable from anything Pass 1
   extracted — is the single most decision-relevant new fact: it quantifies how thin the debt-
   service cushion is heading into a capex ramp whose capital commitments nearly quadrupled.
4. Note 19's explicit "(Refer Note 48)" cross-reference tightens, without resolving, the top
   verification priority from Pass 1 (MNC advance reconciliation): the AR itself now affirmatively
   ties Rs 27.45 cr of the Rs 29.52 cr customer-advance total to the MNC contract, still well
   short of company memory's Rs 98.12 cr.
5. A pattern-level documentation-quality issue recurs beyond the single instance Pass 1 flagged:
   boilerplate ratio-variance explanations appear identically across at least five rows of Note
   45, and the MSME interest note (22.1) shows an internal contradiction between accrued and
   "due and payable" interest fields.

No findings in this pass overturn Pass 1's overall read (clean audit opinion, deleveraging on
secured debt, improving inventory discipline). The new material adds texture and urgency to the
cash-conversion and related-party threads that were already the run's stated verification
priority; it does not surface a wholly new category of concern.
