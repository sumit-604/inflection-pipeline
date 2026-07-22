# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 OF 3 (PATTERN PASS + CONSOLIDATION)
Company: KCPSUGIND (K.C.P. Sugar and Industries Corporation Ltd)
Run date: 2026-07-21
Source: Annual Report FY2024-25 (year ended 31.03.2025), text cache of Annual_Report.pdf
Cache path: runs/kcpsugind-2026-07-21/inputs/_textcache/Annual_Report.txt
Coverage: standalone Notes 1-76 (AR pp.90-129), fully read three times. Page 2 and pp.151-275
(consolidated financials, Eimco's own standalone financials, remaining scanned pages) are
NOT AVAILABLE (no text layer) and no figures from those sections have been inferred at any
pass.

---

## PASS 3 — PATTERN RE-READ (contradictions, mismatches, vague disclosure, restatements,
## subsequent events, going concern)

Targeted keyword sweep of the full text cache (not limited to Notes 1-76) plus a
cross-note consistency check against Pass 1 and Pass 2 findings.

### New pattern-pass finding 1 — CARO "no cash losses" clause reconciles, and materially
### softens the read on, the headline net loss — 🟢 New, clarifying (AR p.83, CARO Annexure A
### clause (xvii))
The independent auditor's CARO Annexure A, clause (xvii), states verbatim: **"the Company
has not incurred cash losses during the financial year and the immediately preceding
financial year."** Read against Pass 1's top finding (reported net loss of ₹(172.24) lakhs
FY25 vs profit of ₹5,626.48 lakhs FY24), this is an important disambiguation: the FY25
accounting loss is not accompanied by a cash loss in either year. This is consistent with,
and independently corroborates from a different part of the annual report (auditor's
statutory annexure, not the notes), Pass 1's finding that the loss is driven by a
₹663.89 lakh non-cash deferred tax charge (Note 22) sitting on top of a still-positive
pre-tax profit of ₹530.03 lakhs (P&L, p.112) and a core Sugar segment operating loss. The
auditor's cash-loss test and the Note 73 DSCR figure of 0.25x (Pass 2 finding) are not
contradictory — they measure different things (net cash generation vs. debt-service
coverage including principal repayment) — but a reader taking the DSCR figure alone could
mistakenly infer outright cash burn; the CARO clause rules that out specifically. Net effect
on interpretation: the loss is an earnings-quality/tax-timing story tied to the volatile
equity portfolio and a weak core segment, not evidence of the company running out of cash
this year. This nuance does not reverse Pass 1's red flags (the core Sugar segment loss and
DSCR collapse are both real and unchanged) but it re-calibrates their severity.

### New pattern-pass finding 2 — No going concern material uncertainty, no Emphasis of
### Matter, no modified opinion — 🟢 New, clean (AR pp.75-83, 9750-9880 boilerplate)
Full-text search of "going concern," "material uncertainty," "Emphasis of Matter," "Key
Audit Matter," "qualified/adverse/disclaimer of opinion" across the entire cache (not just
Notes 1-76) finds only standard SA 570/SA 700 boilerplate describing the auditor's
*responsibility* to consider going concern — there is no company-specific statement that a
material uncertainty exists, no Emphasis of Matter paragraph, and the audit opinion is
unmodified (unqualified). Two Key Audit Matters are identified (NRV of sugar inventory,
already flagged by Pass 1; and classification/measurement of the FVTPL investment
portfolio under Ind AS 109, covered qualitatively by Pass 1's investments section but not
previously labelled as a formal KAM) — both are standard "significant judgment area"
disclosures, not going-concern flags. `going_concern_language: NONE`.

### New pattern-pass finding 3 — Restatement/reclassification note remains unquantified on
### a third read; no other restatement found anywhere in the cache — confirms Pass 1
Targeted search for "restat," "reclassif," "regroup" across the full cache returns only
Note 75 ("Previous year's figures have been regrouped and reclassified wherever
necessary," p.127, already flagged 🟡 by Pass 1) plus one unrelated foreign-currency
translation policy sentence (Note 2, p.99 — routine Ind AS 21 monetary-item restatement
language, not a company restatement). No quantified restatement of any prior-year figure
is found anywhere in the document. `restatements_found: []` (qualitative-only regrouping
note, no quantification disclosed — carried forward as a transparency gap, not a
restatement per se).

**PASS 3 verdict on the pattern sweep**: the two items above are net-clarifying (CARO
cash-loss confirmation, clean audit opinion) rather than newly adverse. No note-vs-note
numerical contradiction was found beyond the already-flagged Note 36 FY24 "Selling
expenses" arithmetic mismatch (Pass 2 finding #3, assessed as a text-extraction/OCR
artifact, not a company reporting error, since the FY25 column reconciles exactly and no
other line item is inconsistent). No subsequent events beyond the Board approval date
(28.05.2025, Note 1) are disclosed anywhere in Notes 1-76.

---

═══════════════════════════════════════════════════════════
## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

### A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Reported net loss ₹(172.24) lakhs FY25 vs profit ₹5,626.48 lakhs FY24 (103% swing); driven by non-cash deferred tax (₹663.89L) on unrealised investment FV gains on top of a still-positive pre-tax profit (₹530.03L); CARO clause (xvii) confirms **no cash loss** either year | Note 22, P&L p.112; CARO Annexure A (xvii) p.83 | 🔴/🟢 (adverse headline, clarified as non-cash) | Sets the entire earnings-quality narrative for the year; must be read with the CARO clarification, not in isolation |
| 2 | Core Sugar segment swung to an operating (PBDIT) loss of ₹(821.03) lakhs from +₹651.41 lakhs a year earlier; Chemicals segment also turned loss-making (-₹42.12L vs +₹59.20L); Power & Fuel result fell 83% while staying positive | Note 76, p.128 | 🔴 | Core operating deterioration in the flagship business, independent of the investment-portfolio/tax noise |
| 3 | Managerial remuneration of ₹60.53 lakhs paid to Executive Chairman and MD for the fifth consecutive year of inadequate profits, pending shareholder special-resolution ratification, in the same year the company recorded its first net loss in this disclosed history | Note 54, p.125; Auditor's Report (g), p.79 | 🔴 | Governance red flag: pay decoupled from performance, statutory exception mechanism used repeatedly |
| 4 | Debt Service Coverage Ratio collapsed to 0.25x (FY24: 1.52x, -84%) | Note 73, p.126 | 🔴 | Harder financing-stress signal than the Debt/Equity improvement (0.30x, deleveraging) conveys alone |
| 5 | Deferred tax liability on FV gains on investments more than doubled (₹583.87L → ₹1,299.04L, +122.5%) even as the pace of P&L-recognised gains slowed (₹4,819.63L FY24 → ₹437.57L FY25, -90.9%) | Note 22, p.110; Note 30, p.111 | 🟡 | Real, market-sensitive future cash tax exposure tied to the equity portfolio |
| 6 | RoCE fell to 3% (FY24: 18%, -81%) and Return on Investment fell to 5% (FY24: 27%, -82%); Net Capital Turnover fell 22% | Note 73, p.126-127 | 🟡 | Capital efficiency collapsed well below any reasonable cost of capital |
| 7 | Trade receivable collection velocity deteriorated 29% YoY (turnover 25.66x → 18.14x; implied days ~14.2 → ~20.1) even as absolute receivables fell 12.8%; 43% of FY25 book >6 months overdue; a static ₹372.67 lakh disputed balance unchanged for two years | Note 10, p.106-107; Note 73, p.126 | 🟡 | Feeds FLAG-CASH — velocity and absolute-balance trends point in different directions |
| 8 | Balance sheet is now more investment portfolio than sugar company: quoted equity + mutual funds = ₹23,494.61 lakhs (46% of total assets); unallocable/corporate segment assets (₹29,102.91L) exceed all six operating segments combined (₹21,878.06L) | Note 5, Note 9, Note 76, p.104-106, 128-129 | 🟡 | Structural, thesis-relevant capital-allocation finding, not inherently negative |
| 9 | Related-party fixed deposits with the company (promoter entity Durgamba Investment, MD Irmgard Velagapudi, subsidiary Eimco) grew 82.5% YoY to ₹1,770.00 lakhs, now 26.9% of the total public deposit book | Note 53(C), p.124 | 🟡 | RPT/governance fairness question on a nominally public deposit scheme |
| 10 | Capital expenditure fell 36.1% YoY (₹342.68L vs ₹536.73L) and is now below FY25 depreciation (₹514.01L) — capex/depreciation ≈0.67x; Urad Dal (the growth segment) received zero capex either year | Note 76, p.128; Note 35, p.112 | 🟡 | Under-investment signal relevant to the GARP/transition thesis |
| 11 | Actual production volumes collapsed across every core line (Sugar -41.9%, Alcohol -82.3%, Molasses -34.4%, Power -24.2%), confirming the revenue decline is volume-driven, not price-driven | Note 44, p.115 | 🟡 | Distinguishes a demand/season problem from a pure realisation/pricing problem |
| 12 | At least three separate one-off/non-recurring gain sources embedded in FY25 results: exceptional plant-sale gain ₹480.54L, agricultural-land sale gain ₹61.09L (routed through Other Income, not flagged as exceptional), and investment FV gain ₹437.57L; new Assets Held for Sale of ₹239.50L signals a further exceptional gain is plausible in FY26 | Note 16, Note 30, p.107-108, 111; P&L p.112 | 🟡 | "Core" earnings are harder to normalise than the P&L presentation implies |
| 13 | Eimco-K.C.P. Ltd (wholly owned material subsidiary) lacked the mandatory audit-trail (edit-log) feature in its accounting software for part of FY25, migrating to a compliant ERP only in H2 FY25; parent company's own audit trail was compliant throughout | Eimco Auditor's Report cross-ref "note 63" (Eimco numbering, text NOT AVAILABLE), AR p.147; Parent Auditor's Report (iv), p.80 | 🟡 | Subsidiary-level internal-control weakness distinct from the parent |
| 14 | Working-capital liability lines show large, unexplained YoY declines: Earnest Money/Other Deposits -83.3% (-₹451.92L), Advance from Customers -94.7% (-₹408.24L), Statutory Liabilities -66.8% | Notes 25, 26, p.111 | 🟡 | Order-book/demand signal not separately narrated by management |
| 15 | CARO clause (xvii): auditor confirms no cash losses in FY25 or the immediately preceding year, despite the reported accounting net loss; no going concern material uncertainty, no Emphasis of Matter, unmodified audit opinion | CARO Annexure A (xvii), p.83; Auditor's Report, pp.75-83 | 🟢 | Clarifies that finding #1 is an earnings-quality/tax-timing issue, not a liquidity crisis |

*(Findings not making the top 15 but retained as material context: 22-year-pending Supreme
Court captive-power duty case, ₹578.87L, 74.5% of total contingent liabilities but only
1.58% of net worth (Note 45, p.115-116); a >23x increase in unquoted equity holdings to
₹118.99L with one holding's identity not cleanly legible in the source text (Note 5(c),
p.105); an unexplained ₹403.48L "Deposit made as per Court Order" not cross-referenced to
any Note 45 item (Note 7, p.106); a new ₹36.00L doubtful-supplier-advance provision and
₹33.07L of unexplained asset write-offs, both NIL in FY24 (Note 36/15, p.106, 113); the
Note 36 FY24 "Selling expenses" arithmetic mismatch, assessed as an OCR/extraction
artifact requiring source-PDF verification before modelling (p.113); Notes 55-71's clean
Schedule III bundle (no wilful defaulter, no Benami property, no crypto, no
round-tripping) (pp.125-126).)*

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Straightforward point-in-time goods recognition, no aggressive language, but no Ind AS 115 contract asset/liability disclosure and no customer-concentration quantification (Note 29, 40, 49) |
| Expense capitalisation honesty | 6 | No capitalisation threshold disclosed; mixed depreciation method (SLM vs WDV for Registered Office assets) without quantified effect (Note 2(g)); capex now below depreciation, a real (not disclosure) under-investment signal rather than a capitalisation-honesty issue |
| Provisioning adequacy | 5 | ECL allowance for trade receivables flat/unchanged for two years with no ageing-bucket rate matrix disclosed (Note 10, 49); new doubtful supplier-advance provision narrated only via cross-note arithmetic, not directly explained (Note 15/36); litigation carried entirely as disclosed contingent liability, none provided for (Note 45) |
| RPT fairness | 5 | RPT sale-of-goods volume modest (5.5% of revenue) and internally consistent, but related-party FD balances grew 82.5% YoY to 26.9% of the public deposit book, and managerial remuneration was paid via the Schedule V exception in the same year as the first net loss (Notes 53, 54) |
| Disclosure transparency | 5 | Multiple NOT FOUND items across core areas: covenant table, FD scheme rate/tenure, single-customer concentration, capitalisation threshold, impairment rate/growth-rate inputs, 5-year debt maturity ladder, formal effective-vs-statutory tax rate reconciliation, unexplained swings in Notes 7/25/26 with no narrative |
| Consistency with prior years | 6 | Generally consistent presentation; one unquantified regrouping/reclassification note (Note 75); actuarial "assumption changes" cited as driving a ₹128.08L OCI loss despite headline discount/salary/attrition rates being disclosed as unchanged YoY (Note 50) — an internal inconsistency |
| **OVERALL** | **6** | Clean audit opinion, no going concern doubt, no cash loss (CARO); but real core-segment deterioration, thin provisioning disclosure, growing related-party deposit exposure, and multiple undisclosed items pull the score down from a "clean" 8-9 to a mid-range 6 |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Core Sugar segment operating loss persists or widens | High | Segment result (Note 76 equivalent) in next AR; sugar realisation/quota notifications | Next annual report (FY26) |
| DTL on investment FV gains crystallises as cash tax on any future realisation of the equity portfolio | Medium | Note 22 DTL balance; any disposals from the quoted equity book | On realisation of holdings, timing discretionary |
| Related-party deposit concentration continues to grow inside the "public" FD scheme | Medium | Note 53(C) closing balances YoY | Each annual report cycle |
| Receivable collection velocity keeps deteriorating even if absolute balances stay low | Medium | Note 73 Trade Receivable Turnover Ratio and Note 10 ageing buckets | Next quarter/annual disclosure |
| Under-investment (capex < depreciation) compounds if sustained multi-year | Medium | Note 76 segment capex vs Note 35 depreciation | Multi-year trend, watch FY26-27 |
| 22-year-pending Supreme Court captive-power duty case resolves adversely | Low (small vs net worth) but binary | Note 45 status update | Unpredictable; litigation-driven |
| Eimco subsidiary control weakness (pre-H2 FY25 audit trail gap) recurs or is not fully remediated | Low-Medium | Eimco's own auditor's report in next AR (currently NOT AVAILABLE for detail) | Confirm at next annual report |

### D. FIVE (PLUS) QUESTIONS FOR MANAGEMENT

1. What is the expected resolution timeline and worst-case cash exposure for the ₹578.87
   lakh captive-power/electricity-duty case pending at the Supreme Court since July 2003
   (approximately 22 years)?
2. Given FY25 is the first net-loss year within the disclosed five-year "inadequate
   profits" stretch, will the Board revisit minimum remuneration paid to the Executive
   Chairman and Managing Director before the next shareholder ratification, and what is
   the Schedule V exception's expected end date?
3. What is the nature, counterparty, and expected recovery timeline for the ₹403.48 lakh
   "Deposit made as per Court Order" (Note 7), and which litigation does it relate to
   (it is not cross-referenced to any item in Note 45)?
4. Why did the doubtful supplier advance (Note 15) increase from ₹4.27 lakh to ₹40.27
   lakh in FY25 (a ~9.4x increase), and who is the counterparty?
5. What drove the ₹451.92 lakh (83.3%) decline in Earnest Money/Other Deposits and the
   ₹408.24 lakh (94.7%) collapse in Advance from Customers — order-book weakness, a
   change in booking practice, or something else?
6. Can management disclose the interest rate and tenure structure of the ₹6,584.25 lakh
   public Fixed Deposit scheme, and confirm what financial covenants (if any) apply to
   the remaining secured bank borrowings?
7. What is the identity and business rationale for the unquoted equity holding that grew
   from ₹5 lakh to approximately ₹119 lakh (>23x) in FY25 (Note 5(c))?

### E. NOTES-BASED RED FLAGS

- **Earnings quality**: FY25 net loss is entirely attributable to a non-cash deferred tax
  charge tied to unrealised investment gains and a core Sugar segment swing to an
  operating loss, not to a cash-flow crisis (CARO confirms no cash loss either year) — an
  accounting-quality flag on presentation/normalisation, not a liquidity flag.
- **Governance — managerial remuneration**: full remuneration paid to promoter-family
  executives under the Schedule V inadequate-profits exception for a fifth consecutive
  year, in the same year the company posted its first net loss in this disclosed history.
- **Financing stress signal (ratio-level)**: DSCR of 0.25x, down 84% YoY, despite an
  improving Debt/Equity ratio — the two metrics point in different directions and should
  not be read in isolation.
- **RPT concentration in a public-facing deposit scheme**: related-party FD balances up
  82.5% YoY to 26.9% of the total public deposit book.
- **Aggressive accounting**: none identified with a numeric earnings impact beyond the
  above; no goodwill impairment games, no ESOP dilution obfuscation, no direct
  reserve-bypass irregularities found.
- **Undisclosed risk indicators**: absence of a covenant table, FD rate/tenure schedule,
  customer concentration disclosure, capitalisation threshold, and impairment rate inputs
  collectively limit independent verification of several balance sheet items.

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, mixed with some deliberately thin
disclosure areas. Key concern: core Sugar segment turned operating-loss-making while
managerial remuneration continued via the Schedule V exception in the same loss year. Key
strength: the headline net loss is confirmed non-cash by the auditor's own CARO clause,
and the audit opinion is clean with no going concern doubt. Overall accounting quality:
6/10.

---

```yaml
stage: B02-notes
company: "KCPSUGIND"
run_date: "2026-07-21"
model: claude-sonnet-5
status: complete
input_gaps:
  - "AR p.2 and pp.151-275 (consolidated financial statements and notes; Eimco-K.C.P. Ltd's own standalone financial statements/notes) are scanned images with no text layer and were NOT AVAILABLE for extraction across all three passes."
  - "Several standard disclosures NOT FOUND IN DOCUMENT within the available standalone notes: covenant table for borrowings, FD scheme interest rate/tenure structure, single-customer revenue concentration, capitalisation threshold, impairment test growth/discount rate inputs, formal effective-vs-statutory tax rate reconciliation, 5-year debt maturity ladder, quantified detail behind the Note 75 regrouping/reclassification statement."
flags:
  - {type: FLAG-CASH, reason: "Trade receivable turnover deteriorated 29% YoY (25.66x to 18.14x; implied days ~14.2 to ~20.1) even as absolute receivables fell 12.8%; 43% of FY25 receivables are >6 months overdue; DSCR collapsed to 0.25x from 1.52x (Note 10, Note 73, AR p.106-107, 126)."}
accounting_quality: 6        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:                # max 15
  - {rank: 1, finding: "Reported net loss Rs(172.24) lakhs FY25 vs profit Rs5,626.48 lakhs FY24, driven by a non-cash Rs663.89 lakh deferred tax charge on unrealised investment gains on top of a positive Rs530.03 lakh pre-tax profit; CARO confirms no cash loss either year", note_ref: "Note 22, P&L p.112; CARO Annexure A (xvii) p.83", rating: "Red Flag / clarified", why: "Sets the earnings-quality narrative; loss is non-cash, not a liquidity event"}
  - {rank: 2, finding: "Core Sugar segment swung to operating loss of Rs(821.03) lakhs from +Rs651.41 lakhs; Chemicals also turned loss-making; Power & Fuel result fell 83%", note_ref: "Note 76, p.128", rating: "Red Flag", why: "Core operating deterioration independent of portfolio/tax noise"}
  - {rank: 3, finding: "Managerial remuneration of Rs60.53 lakhs paid to Executive Chairman and MD for the fifth consecutive year of inadequate profits, in the first net-loss year of that stretch", note_ref: "Note 54, p.125; Auditor's Report (g), p.79", rating: "Red Flag", why: "Governance: pay decoupled from performance"}
  - {rank: 4, finding: "Debt Service Coverage Ratio collapsed to 0.25x from 1.52x, -84% YoY", note_ref: "Note 73, p.126", rating: "Red Flag", why: "Harder financing-stress signal than Debt/Equity improvement alone conveys"}
  - {rank: 5, finding: "Deferred tax liability on investment FV gains more than doubled (Rs583.87L to Rs1,299.04L) even as P&L-recognised gains slowed 90.9%", note_ref: "Note 22, p.110; Note 30, p.111", rating: "Watch", why: "Real, market-sensitive future cash tax exposure"}
  - {rank: 6, finding: "RoCE fell to 3% from 18% and Return on Investment fell to 5% from 27%", note_ref: "Note 73, p.126-127", rating: "Watch", why: "Capital efficiency collapsed well below cost of capital"}
  - {rank: 7, finding: "Receivable collection velocity deteriorated 29% YoY even as absolute receivables fell 12.8%; 43% of book >6 months overdue; static Rs372.67 lakh disputed balance unchanged two years", note_ref: "Note 10, p.106-107; Note 73, p.126", rating: "Watch", why: "Feeds FLAG-CASH; velocity and balance trends diverge"}
  - {rank: 8, finding: "Balance sheet now more investment portfolio than sugar company: quoted equity + MF = 46% of total assets; unallocable segment assets exceed all six operating segments combined", note_ref: "Note 5, Note 9, Note 76, p.104-106, 128-129", rating: "Watch", why: "Structural, thesis-relevant capital allocation finding"}
  - {rank: 9, finding: "Related-party fixed deposits with the company grew 82.5% YoY to Rs1,770.00 lakhs, now 26.9% of the public deposit book", note_ref: "Note 53(C), p.124", rating: "Watch", why: "RPT/governance fairness on a nominally public deposit scheme"}
  - {rank: 10, finding: "Capex fell 36.1% YoY and is now below FY25 depreciation (capex/depreciation approximately 0.67x); Urad Dal growth segment received zero capex", note_ref: "Note 76, p.128; Note 35, p.112", rating: "Watch", why: "Under-investment signal relevant to transition thesis"}
  - {rank: 11, finding: "Production volumes collapsed across every core line (Sugar -41.9%, Alcohol -82.3%, Molasses -34.4%, Power -24.2%), confirming volume-driven not price-driven revenue decline", note_ref: "Note 44, p.115", rating: "Watch", why: "Distinguishes demand/season problem from pricing problem"}
  - {rank: 12, finding: "At least three one-off gain sources in FY25 (plant sale Rs480.54L, agricultural land Rs61.09L, investment FV gain Rs437.57L); new Rs239.50L Assets Held for Sale signals further FY26 exceptional gain", note_ref: "Note 16, Note 30, p.107-108, 111", rating: "Watch", why: "Core earnings harder to normalise than P&L presentation implies"}
  - {rank: 13, finding: "Eimco-K.C.P. Ltd (wholly owned subsidiary) lacked mandatory audit-trail feature for part of FY25; parent's own audit trail was compliant throughout", note_ref: "Eimco Auditor cross-ref note 63 (text NOT AVAILABLE), AR p.147; Parent Auditor's Report (iv), p.80", rating: "Watch", why: "Subsidiary-level internal control weakness distinct from parent"}
  - {rank: 14, finding: "Working-capital liabilities show large unexplained declines: Earnest Money/Other Deposits -83.3%, Advance from Customers -94.7%, Statutory Liabilities -66.8%", note_ref: "Notes 25, 26, p.111", rating: "Watch", why: "Order-book/demand signal not separately narrated"}
  - {rank: 15, finding: "CARO clause (xvii) confirms no cash losses in FY25 or the prior year; no going concern material uncertainty, no Emphasis of Matter, unmodified audit opinion", note_ref: "CARO Annexure A (xvii), p.83; Auditor's Report pp.75-83", rating: "Clean", why: "Clarifies rank-1 finding is earnings-quality/tax-timing, not a liquidity crisis"}
red_flags:
  - "FY25 net loss driven entirely by non-cash deferred tax and core Sugar segment operating loss, not by cash-flow deterioration (CARO confirms no cash loss) (Note 22, P&L p.112; CARO p.83)"
  - "Full managerial remuneration paid to promoter-family Executive Chairman and MD under the Schedule V inadequate-profits exception for a fifth consecutive year, coinciding with the first net-loss year (Note 54, p.125)"
  - "DSCR collapsed to 0.25x from 1.52x, an 84% decline, despite an improving Debt/Equity ratio (Note 73, p.126)"
  - "Related-party fixed deposits within the public deposit scheme grew 82.5% YoY to 26.9% of the total book (Note 53(C), p.124)"
  - "Core Sugar segment result swung to a -Rs821.03 lakh operating loss from +Rs651.41 lakhs; Chemicals segment also turned loss-making (Note 76, p.128)"
questions_for_mgmt:
  - "What is the expected resolution timeline and worst-case cash exposure for the Rs578.87 lakh captive-power/electricity-duty case pending at the Supreme Court since July 2003 (~22 years)?"
  - "Given FY25 is the first net-loss year within the disclosed five-year inadequate-profits stretch, will the Board revisit minimum remuneration paid to the Executive Chairman and MD before the next shareholder ratification?"
  - "What is the nature, counterparty, and expected recovery timeline for the Rs403.48 lakh Deposit made as per Court Order (Note 7), not cross-referenced to any Note 45 contingent liability?"
  - "Why did the doubtful supplier advance (Note 15) increase from Rs4.27 lakh to Rs40.27 lakh in FY25 (~9.4x), and who is the counterparty?"
  - "What drove the Rs451.92 lakh decline in Earnest Money/Other Deposits and the Rs408.24 lakh (94.7%) collapse in Advance from Customers?"
  - "Can management disclose the interest rate and tenure structure of the Rs6,584.25 lakh public Fixed Deposit scheme and confirm covenants on remaining secured bank borrowings?"
  - "What is the identity and business rationale for the unquoted equity holding that grew from Rs5 lakh to approximately Rs119 lakh (>23x) in FY25 (Note 5(c))?"
receivables_trend: "mixed / net deteriorating: absolute net trade receivables fell 12.8% (Rs1,182.31L to Rs1,030.72L) and the >6-months-overdue share improved from 52.6% to 43.0% of the book, but collection velocity worsened materially -- Trade Receivable Turnover Ratio fell 29% (25.66x to 18.14x FY24 to FY25, Note 73, p.126), implying days sales outstanding lengthened from approximately 14.2 to approximately 20.1 days (Note 10, p.106-107; Note 73, p.126) -- velocity deterioration is weighted deteriorating for FLAG-CASH purposes"
restatements_found: []
going_concern_language: "NONE -- full-text search of the annual report cache found only standard SA 570/SA 700 auditor-responsibility boilerplate regarding going concern (e.g. p.5351-5352, p.9819-9820 of extracted text); no company-specific material uncertainty, no Emphasis of Matter paragraph, and an unmodified (unqualified) audit opinion for FY25 and FY24 (Auditor's Report pp.75-83)"
```
