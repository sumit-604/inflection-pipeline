# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 (RAW EXTRACTION)
Company: OBSC Perfection Limited (OBSCP) | Run date: 2026-07-12
Source: runs/obscp-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf (FY2024-25 Annual Report)

## ⚠️ DOCUMENT TRUNCATION — READ FIRST (affects every section below)

The source PDF was recovered from a truncated collector download. Direct verification of the
PDF (reading every page 1-110 via the Read tool) confirms:

1. **Pages 78-101 are entirely BLANK** (24 blank pages; document ends at page 101 — no content
   beyond page 101 either). This is exactly where the numbered schedule Notes to Accounts
   (Note 3 onward) would sit. The "Notes to Financial Statements" sub-document itself is
   paginated internally "Page 1 of 6" through "Page 6 of 6"; only **note-pages 1-4 of 6**
   survived (AR pages 74-77 = Note 1, and Note 2 "Significant Accounting Policies" sub-topics
   1 through 5.2). **Note-pages 5-6 of 6 — which would contain the remainder of Note 2's policy
   topics AND essentially the entire schedule-notes package (Notes 3 through the highest note
   referenced elsewhere in the AR, Note 29) — are lost.**
2. A SEPARATE, unrelated rendering problem affects AR pages ~3-59 (Board's Report, MD&A,
   Corporate Governance Report): these pages use a corrupted/garbled font encoding and render
   as unreadable glyph noise even visually, not just in copy-paste text. This section is **out
   of scope for this Notes stage** (per pipeline rules, "nothing else in the annual report
   matters for this exercise"), but it means the corresponding B01/board-report stage will hit
   the same corruption and should be told independently. Flagging here for downstream
   inheritance per instruction.
3. What IS fully readable and reliable: page 1 (cover letter), the Independent Auditor's Report
   and annexures (AR pages 60-70), the Balance Sheet / P&L / Cash Flow Statement (AR pages
   71-73), and Note 1 + the surviving portion of Note 2 (AR pages 74-77).

**Practical consequence for this Pass 1**: categories 2 (Related Party Transactions), 3
(Contingent Liabilities detail), 4 (Trade Receivables ageing), 5 (Inventory category detail),
6 (Investments/subsidiaries detail), 7 (Borrowings instrument table), 8 (Trade Payables
ageing/MSME), 9 (Provisions movement), 10 (Deferred Tax reconciliation), 11 (Revenue
disaggregation) and most of 12 (Other Critical Notes) are **NOT FOUND IN DOCUMENT — annual
report pages 78-101 truncated in source PDF**. Where the Balance Sheet, P&L, Cash Flow
Statement, or Auditor's Report reference a specific note number (e.g. "Refer Note No. 29",
"Note: 13 of Loans & Advances", "Note No. 10 on Accounts"), that note number is cited below as
confirmation the schedule exists, but its content is unrecoverable from this file.

---

## 1. ACCOUNTING POLICIES & CHANGES

**Note 1 — Corporate Information** (Note 1, p.74) 🟢
- Incorporated as OBSC Perfection Private Limited, 17 March 2017, CIN U27100DL2017PTC314606.
- Converted Private → Public Company during the year; ROC-CPC approval vide SRN AA7899496
  dated 19 June 2024; fresh Certificate of Incorporation dated 28 June 2024 issued, CIN changed
  to U27100DL2017PLC314606, name changed to OBSC Perfection Limited. (Note 1, p.74)
- Business: manufacture of components made of steel and other metals, primarily for the
  automotive industry. (Note 1, p.74)
- Facilities: two factories in Chakan (suburb of Pune, Maharashtra) plus one factory at Mapedu,
  Sriperumbudur, Tamil Nadu (started production FY ended 31 March 2024). A third unit in
  suburbs of Pune began production during FY ended 31 March 2025 (construction/set-up started
  FY24). (Note 1, p.74)
- No discontinued operations. (Note 1, p.74)

**Note 2 — Significant Accounting Policies** (Note 2, pp.74-77) 🟢 (as far as readable)
- **Basis of preparation**: accrual basis, historical cost convention except where stated;
  complies with "Medium Companies" general instructions under the applicable Accounting
  Standards and Schedule III (as amended by Notification dated 24-3-2021). Prior year figures
  regrouped/reclassified where required; figures rounded to nearest ₹ Lakh. (Note 2.1(a)-(b), p.74)
- **Method of accounting**: Mercantile/accrual per AS 9. Input Tax Credits (Excise/Service
  Tax/VAT to 30 June 2017; GST from 1 July 2017) excluded from expense and set off against
  output liabilities. Gratuity for employees completing 5 years' service on actuarial basis per
  AS 15. Leave encashment: accumulated/encashable at retirement or during service (with
  management consent); liability per AS 15, treated as Current Liability. Other terminal
  benefits accounted on payment. Bank charges/interest accounted when debited by bank. Rates
  and taxes accounted on receipt/finalisation of demand. Dividends from subsidiaries/
  investments recognised as revenue only when right to receive is established. (Note 2.1, p.75)
- **Provisions**: created when the company has an obligation from a past event; not discounted
  to present value except where specifically stated on an actuarial basis. (Note 2.2, p.75)
- **Contingent liabilities policy**: claims/demands not acknowledged as liability, or pending in
  appeal/arbitration, that management does not consider likely to be paid, are disclosed as
  contingent liabilities. (Note 2.3(a), p.75)
- **Investments**: "The Company has no investments at present." (Note 3 within Note 2, p.76) 🟡
  — read together with CARO Annexure A(iii), which confirms the company DOES have subsidiaries
  and joint ventures to which it has extended loans/advances on running current-account terms
  (see Related Party section below); those balances evidently sit in Loans & Advances (Note 13)
  rather than an Investments line, which is consistent accounting treatment for a current
  account but means equity stakes in subsidiaries/JVs (if any) are not separately quantified
  anywhere readable in this file.
- **Inventory valuation policy** (Note 4 within Note 2, p.76): exclusive method. Raw materials —
  lower of cost (weighted average) or market value. Finished goods — lower of estimated cost of
  production or realisable value (cost of production = raw material cost + average conversion
  cost). WIP — cost of raw materials + average production cost, restricted to extent of work
  done; raw material issued but not yet processed remains classified as Raw Material. Other
  items — lower of cost (FIFO) or market value.
- **PP&E, depreciation & amortisation policy** (Note 5 within Note 2, pp.76-77):
  - All PP&E (tangible/intangible) capitalised at cost including incidentals and borrowing
    costs to date of use; construction-period expenses allocated to assets.
  - Government grants/subsidies, if received, reduce cost of acquisition; ITC availed on fixed
    assets purchase (pre/post GST cutover) similarly reduces capitalised cost.
  - Impairment: realisable market values reviewed against book values at Balance Sheet date;
    permanent impairment dealt with per Accounting Standards on management review.
  - Depreciation charged only once asset is put to use; useful lives per Schedule II to the
    Companies Act 2013 with residual value at 5% of original cost unless stated otherwise.
    **Plant & Machinery and electrical installations — Straight Line Method (SLM). All other
    assets — Written Down Value (WDV).** — a dual-method policy (SLM for P&M/electrical, WDV
    for the rest) worth noting as non-uniform; not itself a red flag but affects comparability
    of depreciation charge across asset classes.
  - No depreciation on land (freehold or long-term/perpetual leasehold with transfer right).
  - Short-term leased assets not treated as Fixed Assets; yearly lease premium expensed;
    non-refundable/adjustable lease premium amortised per lease terms.
  - Gains/losses on disposal = difference between book value and value realised, taken to P&L.
  - Computer software treated as intangible fixed asset only if custom-built or held >12
    months; software licensed ≤12 months (or annually renewable) expensed to P&L.
  - Financial/borrowing costs include LC charges, guarantee charges, processing/inspection
    charges plus interest; capitalised during construction/erection to date of asset
    capitalisation; forex fluctuation on foreign-currency borrowings till put-to-use also
    capitalised on the same basis.
  - **Amortisation of preliminary/pre-operative and deferred-revenue-nature expenses: over 5
    yearly instalments.** (Note 5.2, p.77)
- **First-time standard adoptions / policy changes with quantified P&L impact**: NOT FOUND IN
  DOCUMENT — the accounting-policy note is cut off at Note 5.2 (note-page 4 of 6); any
  disclosure of policy changes, revenue recognition detail (Ind AS 115-style or AS 9 percentage
  completion specifics), taxation policy, EPS policy, financial instruments/fair value policy,
  or first-time adoption commentary would sit on note-pages 5-6, which are in the blank/
  truncated zone (AR pp.78-79 onward). 🔴 gap.
- **Ind AS 116 / lease accounting**: Not applicable as drafted — the company's financial
  statements are prepared under the "Medium Companies" AS framework (Note 2.1(a), p.74), not
  Ind AS, so ROU/lease liability disclosures under Ind AS 116 do not apply. Short-term lease
  treatment is covered in the PP&E policy above (Note 5(vii), p.77). No lease liability or ROU
  asset line appears on the Balance Sheet (p.71).
- **Depreciation useful lives vs norm / capitalisation threshold / impairment test assumptions
  (growth & discount rates) / ECL matrix**: NOT FOUND IN DOCUMENT — these normally sit in the
  fixed-asset schedule (Note 12A/12B) and a separate financial-instruments/impairment note,
  both in the truncated zone.

## 2. RELATED PARTY TRANSACTIONS — NOT FOUND IN DOCUMENT (truncated) 🔴

Full RPT table (party, relationship, nature, current/prior year ₹, YoY%) is not available; the
relevant schedule note is beyond the surviving pages. Two corroborating facts from the readable
portions of the file:
- The Independent Auditor's Report (CARO Annexure A, para xiii, p.68) states: "the related
  party transactions in compliance with section 188 of Companies Act 2013 and Accounting
  Standard AS 18 have been reported in Note No. ___ to the financial statements" — **the note
  number itself is blank/illegible in the source**, so even the note reference cannot be
  confirmed. 🔴
- CARO Annexure A (para iii, pp.65-66) confirms the company has extended loans/advances "in the
  nature of loans" to its subsidiaries and joint venture companies via running current accounts,
  with monthly interest charged at rates the auditor considers not prejudicial to the company;
  parties are repaying principal as stipulated and are current on interest; no overdue amount
  exceeds 90 days. Full detail (counterparty names, amounts, rates) is under "Note: 13 of Loans
  & Advances" — content NOT FOUND due to truncation.
- No data on: RPTs as % of revenue, non-arm's-length signals, loans to promoter entities,
  royalty/fee/rent to promoter family, or new related parties this year. NOT FOUND IN DOCUMENT.

## 3. CONTINGENT LIABILITIES — mostly NOT FOUND IN DOCUMENT (truncated) 🔴

- The Independent Auditor's Report (p.61, clause (g)(i)) states: "The Company has disclosed the
  impact of pending litigations on its financial position in its financial statements — Refer
  Note No. 29 to the financial statements." **Note 29 itself is entirely in the truncated
  zone.** Full contingent liabilities table (nature, amount, stage, company's assessment), total
  as % of net worth, any single item >10% of net worth, tax dispute composition, and guarantees
  for subsidiaries: NOT FOUND IN DOCUMENT.
- One quantified contingent-liability-adjacent item IS readable from the accounting-policy note
  itself (Note 2.3(b), p.76): the company imported Capital Goods (Plant & Machinery) with FOB
  value **₹8,08,68,765 (≈₹8.09 Cr; US$9,63,870.85)**, availing customs duty exemption of
  **₹1,34,78,128 (≈₹1.35 Cr)** under the EPCG-style Foreign Trade Policy 2023 scheme. Attached
  Export Obligation = 6× duty saved = **₹8,08,68,765 (≈₹8.09 Cr)** of exports required within 6
  years of Authorization date **26-12-2024**, in two blocks (as printed: "1st to 4th year (1st
  Block) — 50%" and "5th to 8th year (2nd Block) — 60%"; these two percentages as transcribed
  from the source do not sum to a clean 100%, which may reflect an OCR/scan artifact in the
  source PDF rather than the company's actual undertaking — flagged for verification against a
  cleaner copy, not asserted as fact). (Note 2.3(b), p.76) 🟡 — this is an unfulfilled export
  obligation that, if not met, would crystallise a duty-plus-penalty liability; it is not
  captured as a line item in whatever remains of the contingent liabilities table because that
  table (Note 29) is unreadable.
- No going-concern-related contingent items found in the readable text; auditor's CARO clause
  (xix), p.68, states no material uncertainty exists as to the company meeting liabilities due
  within one year "subject to the fact there is no major financial, health or political
  turmoil" (standard boilerplate qualifier).

## 4. TRADE RECEIVABLES — ageing/customer detail NOT FOUND; balance-level trend available 🔴/🟡

Note 15 (Trade Receivables schedule, ageing, ECL, related-party receivables, single-customer
concentration) is in the truncated zone — NOT FOUND IN DOCUMENT. What can be derived from the
primary statements (not notes, but load-bearing for this stage's job of flagging cash quality):

- Trade Receivables (Balance Sheet, Note 15, p.71): **₹34.93 Cr as at 31 Mar 2025** vs **₹21.53
  Cr as at 31 Mar 2024** — **+62.3% YoY**, against Income from Operations growth of **+24.1%**
  (₹142.79 Cr FY25 vs ₹115.03 Cr FY24; P&L Note 18, p.72). Receivables growing 2.6x faster than
  revenue is a working-capital/quality-of-earnings flag. 🔴
- Cash Flow Statement (p.73) shows the "[Increase]/Decrease in Current Assets" line at
  **₹(26.81) Cr** for FY25 vs ₹(9.57) Cr FY24 — consistent with the receivables and inventory
  buildup noted above.
- Receivable days trend (3 years), ECL provision adequacy, single-customer >10% concentration,
  and receivables from related parties: NOT FOUND IN DOCUMENT (Note 15 detail lost).

## 5. INVENTORY — category breakdown NOT FOUND; balance-level trend available 🔴/🟡

Note 14 (Inventory schedule — category breakdown, write-downs, obsolescence) is in the
truncated zone — NOT FOUND IN DOCUMENT. Valuation policy is available (see Section 1 above).
From the primary statements:

- Inventories (Balance Sheet, Note 14, p.71): **₹26.69 Cr as at 31 Mar 2025** vs **₹14.91 Cr as
  at 31 Mar 2024** — **+79.0% YoY**, again far outpacing the 24.1% revenue growth. 🔴
- P&L "Change in inventories — Finished Goods, WIP and Stock in trade" (Note 21, p.72) was
  **₹(6.20) Cr** for FY25 vs ₹(4.11) Cr FY24 (both negative, i.e., inventory build reducing
  reported cost of goods, consistent with the balance sheet growth).
- Finished-goods-specific growth vs revenue growth, write-downs, inventory days trend, and
  obsolete-inventory disclosure: NOT FOUND IN DOCUMENT (Note 14 detail lost).

## 6. INVESTMENTS — policy statement available; subsidiary/JV detail NOT FOUND 🔴

- Accounting policy note states plainly: "The Company has no investments at present." (Note 3
  within Note 2, p.76.)
- However, CARO Annexure A confirms subsidiaries and joint venture companies exist (loans/
  advances extended to them, per para iii, pp.65-66, and para v/f on pledge of securities held
  in "its Subsidiaries, Joint Ventures, or Associate companies," p.68) — meaning the company
  has group entities even though it holds no separately-disclosed "Investments" line; equity
  stakes, ownership %, carrying values, impairments, and any loss-making subsidiaries are NOT
  FOUND IN DOCUMENT (would sit in Note 13 detail / a subsidiaries note, both truncated).
- ICDs/loans given (to whom, amount, rate, tenure): confirmed to exist (running current
  account, monthly interest, "not prima facie prejudicial" per auditor) but amounts NOT FOUND
  IN DOCUMENT.
- Other investments with unrealised gains/losses: NOT FOUND IN DOCUMENT (policy states no
  investments held, so likely not applicable, but cannot be confirmed from a dedicated note).

## 7. BORROWINGS — instrument-level detail NOT FOUND; balance-level trend available 🔴/🟢

Note 5 (Long-term Borrowings) and Note 8 (Short-term Borrowings) schedules — instrument table,
rate, maturity, security, covenants, fixed vs floating, repayment schedule, related-party
borrowings — are in the truncated zone. NOT FOUND IN DOCUMENT. From the primary statements:

- Long-term Borrowings (Balance Sheet, Note 5, p.71): **₹20.02 Cr** (FY25) vs **₹25.60 Cr**
  (FY24) — down 21.8%.
- Short-term Borrowings (Balance Sheet, Note 8, p.71): **₹6.95 Cr** (FY25) vs **₹15.88 Cr**
  (FY24) — down 56.2%.
- Cash Flow Statement (p.73): "Increase/[Decrease] in borrowings" of **₹(14.50) Cr** FY25 vs
  +₹8.07 Cr FY24 — net deleveraging in FY25, funded by the large equity raise (₹57.16 Cr share
  capital + premium infusion, same statement) rather than operating cash flow. 🟢 (deleveraging
  itself is a clean signal, though funded by dilution not cash generation)
- Finance costs (P&L Note 23, p.72): ₹3.12 Cr FY25 vs ₹2.69 Cr FY24 — up 16% despite falling
  average borrowings, which is mildly inconsistent and would normally be explained by the
  borrowings note (rate detail, timing of paydown during the year); NOT FOUND IN DOCUMENT to
  reconcile. 🟡
- CARO Annexure A (paras ix(a)-(c), p.67): no default in repayment of loans/borrowings to any
  financial institution, bank, government, or debenture holders; company not declared a
  wilful defaulter; term loans applied for their stated purpose; short-term funds not diverted
  to long-term use. 🟢
- Covenant breaches/waivers, security detail, fixed vs floating split: NOT FOUND IN DOCUMENT.

## 8. TRADE PAYABLES — ageing/MSME detail NOT FOUND; balance-level trend available 🔴/🟡

Note 9 (Trade Payables schedule, incl. MSME ageing >45 days, interest on delayed MSME payments)
is in the truncated zone — NOT FOUND IN DOCUMENT. From the primary statements:

- Trade Payables (Balance Sheet, Note 9, p.71): **₹25.31 Cr as at 31 Mar 2025** vs **₹11.59 Cr
  as at 31 Mar 2024** — **+118.3% YoY**, more than double, against Consumption & Manufacturing
  Expenses growth of ~34.4% (₹93.65 Cr FY25 vs ₹69.67 Cr FY24, P&L Note 20, p.72). Payables
  growing far faster than the purchase base that generates them is a stretching-of-payables
  flag, partially funding the receivables/inventory buildup noted above. 🔴
- MSME-specific ageing, interest on delayed MSME payments, and payable days trend: NOT FOUND IN
  DOCUMENT.

## 9. PROVISIONS — movement/actuarial detail NOT FOUND; one balance-level anomaly found 🔴

Note 7 (Long-term Provisions) and Note 11 (Short-term Provisions) schedules — warranty
movement, employee benefit funded status/actuarial assumptions, decommissioning, onerous
contracts, litigation provisions — are in the truncated zone. NOT FOUND IN DOCUMENT. One
anomaly is visible at the balance-sheet level:

- **Short-term Provisions (Balance Sheet, Note 11, p.71): ₹(0.27) Cr [negative/(27.34) Lakh] as
  at 31 Mar 2025 vs ₹0.66 Cr [66.48 Lakh] as at 31 Mar 2024.** A negative provisions balance is
  unusual on a balance sheet (provisions are normally a credit/liability balance ≥0) and
  suggests either a reclassification, an over-accrual reversal, or a presentation error. Cannot
  be explained without the Note 11 schedule, which is NOT FOUND IN DOCUMENT. 🔴 flag for
  management question.
- Long-term Provisions (Balance Sheet, Note 7, p.71): ₹0.17 Cr FY25 vs ₹0.08 Cr FY24 — small
  balances, more than doubled but immaterial in absolute terms.

## 10. DEFERRED TAX — reconciliation NOT FOUND; balance/P&L movement available 🔴/🟢

Note 6 (Deferred Tax) — effective vs statutory rate reconciliation, MAT credit and utilisation
timeline, DTA realism, unrecognised DTA — is in the truncated zone. NOT FOUND IN DOCUMENT. From
the primary statements:

- Deferred Tax Liability (net) (Balance Sheet, Note 6, p.71): ₹0.76 Cr FY25 vs ₹1.54 Cr FY24 —
  down 50.4%.
- P&L "Deferred Tax Adjustment" (Note 6, p.72): **₹(0.78) Cr** credit FY25 vs ₹0.38 Cr charge
  FY24 — sign flip year-on-year.
- Effective tax rate (derivable, not a note disclosure): Provision for Tax ₹4.65 Cr + Deferred
  Tax Adjustment ₹(0.78) Cr = ₹3.87 Cr total tax on PBT of ₹20.63 Cr ≈ **18.8% effective rate**
  for FY25, materially below the ~25.17% Indian statutory corporate rate (assuming standard
  domestic company rate applies) — the reconciling items (which would normally include this
  gap) are entirely in the missing Note 6 schedule. 🟡 flag — cannot assess whether this is a
  clean MAT-credit/depreciation-timing effect or something requiring more scrutiny without the
  schedule.
- MAT credit entitlement/utilisation, unrecognised DTA rationale: NOT FOUND IN DOCUMENT.

## 11. REVENUE DETAILS — disaggregation NOT FOUND; headline only 🔴

Note 18 (Revenue) — disaggregation by product/segment/geography, contract assets/liabilities,
unsatisfied performance obligations, top-customer revenue — is in the truncated zone. NOT FOUND
IN DOCUMENT. Headline only: Income from Operations ₹142.79 Cr FY25 vs ₹115.03 Cr FY24 (+24.1%,
P&L Note 18, p.72); Other Income ₹2.41 Cr FY25 vs ₹1.08 Cr FY24 (P&L Note 19, p.72), more than
doubled — composition of Other Income (interest income confirmed at ₹0.86 Cr per Cash Flow
Statement, p.73, implying ~₹1.55 Cr of Other Income is non-interest and unexplained by any
readable note) NOT FOUND IN DOCUMENT. 🟡

## 12. OTHER CRITICAL NOTES

- **EPS anomaly** (P&L, Note 26, p.72) 🔴: **Basic EPS ₹6.85, Diluted EPS ₹8.12** for FY2025
  (Face value ₹10/share). Diluted EPS exceeding Basic EPS is not mathematically ordinary —
  diluted EPS is derived by adding potential dilutive shares to the weighted-average
  denominator, which should reduce (or at most leave unchanged) EPS relative to Basic, never
  increase it, absent anti-dilutive adjustments being handled unusually. Prior year FY2024
  shows Basic = Diluted = ₹6.84 (no dilution effect, consistent with a normal capital
  structure). The Note 26 EPS reconciliation that would show the weighted-average share count
  used for each calculation is in the truncated zone (NOT FOUND IN DOCUMENT), so the anomaly is
  unexplained from source. This is flagged as the single most important accounting-quality
  question arising from what is readable in this file.
- **Capital raise / IPO-adjacent activity** 🟢 (Note 1, p.74; Balance Sheet p.71; Cash Flow
  Statement p.73): Share Capital rose ₹17.85 Cr → ₹24.45 Cr (+37.0%); Reserves & Surplus rose
  ₹12.22 Cr → ₹79.54 Cr (+550.6%); Cash Flow Statement shows "Increase in Share Capital &
  premium" of ₹57.16 Cr during financing activities (FY25) with none in FY24. This lines up
  with the Note 1 disclosure that the company converted from Private to Public Limited during
  the year (28 June 2024) — consistent with a pre-listing primary capital raise. Total Balance
  Sheet size nearly doubled, ₹86.51 Cr → ₹158.55 Cr (+83.2%).
- **Audit trail (edit log) irregularity** 🟡 (Independent Auditor's Report, "Report on other
  legal and regulatory requirements," p.62-63): the accounting software has an audit-trail
  (edit log) feature operative throughout FY25; on test check, certain vouchers were found
  amended. Discussion with staff and review of corroborative documents indicated the
  modifications were to "incorporate further details in narrations etc., without impacting the
  incomes/(losses) and state of affairs of the company." The auditor attributes the editing to
  "accounting staff not being well versed with the intricacies of operating the audit-trail-
  compliant software" and calls this "a reasonable cause," noting the software itself is fully
  capable of retaining original-format records. No P&L/Balance Sheet impact asserted, but this
  is a control-quality item worth monitoring given it directly concerns the integrity of the
  audit trail SEBI/MCA now mandates.
- **CSR** 🟡 (CARO Annexure A, para xx, p.68): Company paid ₹18.04 Lakh (₹0.18 Cr) to "Swachh
  Paryavaran Trust" to spend on CSR under section 135(5) of the Companies Act 2013. CSR
  required amount (2% of average net profits of preceding 3 years) vs actual spend
  cross-check, and any unspent/carried-forward CSR obligation, NOT FOUND IN DOCUMENT (would be
  detailed in a CSR note in the truncated zone). Routing CSR spend through a third-party trust
  rather than direct project execution is not unusual but worth noting for a first pass.
- **Statutory dues overdue** 🟡 (CARO Annexure A, para vii(b), p.67): "there are no undisputed
  amounts payable in respect of Duty of Customs, Goods and Services Tax, Cess and any other
  Statutory dues, which have remained outstanding... for a period of more than six months...
  **except those stated in the Note No. 10 on Accounts**." This confirms at least one
  overdue-statutory-dues item exists; amount and nature NOT FOUND IN DOCUMENT (Note 10
  truncated).
- **Going concern language**: NONE found in the readable Auditor's Report text or in Notes 1-2;
  CARO para (xix), p.68, gives an unmodified 12-month liquidity opinion subject to standard
  "no major financial, health or political turmoil" boilerplate. No management going-concern
  disclosure is present in the readable Notes (would ordinarily sit in Note 2 policy text if
  material doubt existed — none appears in what survived).
- **Restatements/reclassifications**: Note 2.1(b) (p.74) states prior-year figures have been
  "regrouped and reclassified wherever required" — standard boilerplate, no specifics
  quantified. No item-level restatement disclosure found (would be in the truncated schedule
  notes if material).
- **CFO/Director dual role** (Balance Sheet/P&L signature block, pp.71-72) 🟡: Sanjeev Verma is
  designated "CFO / Director" (combined role) per the financial statement signature block, and
  Saksham Lekha (Managing Director) and Ashwani Lekha (Director) share the surname "Lekha,"
  consistent with a promoter-family-controlled board. This is a governance observation from the
  primary statements' signature block, not a note, included here only because it bears on how
  RPT and related-party lending (Section 2 above) should be read once that note becomes
  available; not itself a Notes-based finding.
- Exceptional items, goodwill impairment/sensitivity, intangibles detail, capital commitments,
  foreign currency exposure/hedging, segment reporting, ESOP dilution, share capital
  movement schedule, direct debits/credits to reserves bypassing P&L: **all NOT FOUND IN
  DOCUMENT** (truncated zone).

---

## SOURCE PAGE MAP (for downstream stage reference)

| AR page(s) | Content | Readability |
|---|---|---|
| 1 | Cover letter to NSE | Readable |
| 2 | AR cover | Image, readable |
| 3-59 | Board's Report, MD&A, Corporate Governance Report | **Corrupted font — unreadable** (separate issue, out of scope for Notes stage) |
| 60-70 | Independent Auditor's Report + Annexures A & B (CARO, ICFR) | Readable |
| 71 | Balance Sheet as at 31 March 2025 | Readable |
| 72 | Statement of Profit & Loss FY2024-25 | Readable |
| 73 | Cash Flow Statement FY2024-25 | Readable |
| 74-77 | Notes to Financial Statements — Note 1 (Corporate Info) + Note 2 (Accounting Policies, sub-topics 1 through 5.2) = note-pages 1-4 of an internally-paginated 6-page Notes document | Readable |
| 78-101 | **BLANK — note-pages 5-6 of 6 (rest of Note 2) plus the entire schedule Notes package (Note 3 through at least Note 29) lost here** | Not recoverable |
| 101 | Document ends | — |

---

# PASS 1 SUMMARY — TOP 10 FINDINGS RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note anchor | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Entire quantitative Notes package (Notes 3-29: RPT, contingent liabilities/litigation, receivables ageing, inventory detail, investments/subsidiaries, borrowings table, payables/MSME ageing, provisions movement, deferred tax reconciliation, revenue disaggregation, EPS reconciliation, CSR, commitments) is NOT FOUND IN DOCUMENT — AR pages 78-101 truncated in source PDF | Notes 3-29, p.78-101 (missing) | 🔴 | Caps the evidence base for every other finding below and for downstream stages (valuation, quality, cash conversion); this is a mechanical document gap, not a company-quality signal, and must not be read as a red flag on the company itself |
| 2 | Diluted EPS (₹8.12) exceeds Basic EPS (₹6.85) for FY2025 — arithmetically anomalous; FY2024 showed Basic=Diluted=₹6.84 with no dilution | Note 26, p.72 (supporting detail NOT FOUND) | 🔴 | Genuine accounting-quality question unexplained from source; needs the EPS reconciliation note or management clarification before this figure can be trusted |
| 3 | Cash conversion weak: OCF ₹8.85 Cr vs PAT ₹16.76 Cr (~52% conversion), driven by receivables +62% and inventory +79% YoY, both far outpacing 24.1% revenue growth | Balance Sheet p.71; Cash Flow Statement p.73 (ageing detail in Notes 14/15 NOT FOUND) | 🔴 | Direct working-capital/cash-quality flag; feeds FLAG-CASH per pipeline rules — cannot be resolved to a clean PROCEED without the receivables ageing/ECL note |
| 4 | Short-term Provisions swung to negative ₹(0.27) Cr in FY25 from positive ₹0.66 Cr in FY24 | Note 11, p.71 (schedule NOT FOUND) | 🔴 | Negative provisions balance is unusual on a balance sheet; unexplained without the schedule — direct management question |
| 5 | Trade Payables more than doubled (+118.3% YoY) against ~34% growth in the expense base they fund | Note 9, p.71 (ageing/MSME detail NOT FOUND) | 🟡 | Payables stretching is partially financing the receivables/inventory buildup in #3; MSME-specific ageing needed to assess supplier-relationship risk |
| 6 | Auditor found voucher edits under the mandatory audit-trail (edit-log) feature during FY25; attributed to staff unfamiliarity with the software, no P&L/BS impact asserted | Independent Auditor's Report, p.62-63 | 🟡 | Direct evidence-integrity/control-quality item; low severity as characterised by the auditor but worth monitoring given it concerns the audit trail itself |
| 7 | EPCG capital goods import (FOB ₹8.09 Cr) with customs duty exemption ₹1.35 Cr; export obligation of 6× duty saved (₹8.09 Cr) over 6 years from 26-12-2024 | Note 2.3(b), p.76 | 🟡 | Unfulfilled export obligation is a real contingent liability (duty + penalty clawback risk) not separately visible in the (missing) contingent liabilities table |
| 8 | Confirmed related-party lending to subsidiaries/JVs exists (running current account, monthly interest, no overdue >90 days per auditor) but amounts, rates, and the RPT note number itself are unrecoverable | CARO Annexure A(iii), p.65-66; RPT note number illegible, p.68; Note 13 detail NOT FOUND | 🟡 | Cannot assess non-arm's-length risk or quantify related-party exposure from source; a named data gap for the operator to source from a clean copy of the AR |
| 9 | Company converted Private→Public during FY25 with a large capital raise: Share Capital +37.0%, Reserves +550.6%, ₹57.16 Cr fresh share capital/premium infusion; balance sheet size +83.2% YoY | Note 1, p.74; Balance Sheet p.71; Cash Flow Statement p.73 | 🟢 | Confirms the transition-alpha thesis context (private→public conversion, pre-listing capital raise); clean, well-evidenced, no red flag |
| 10 | Accounting policies as disclosed (Notes 1-2, the only fully complete notes) show no unusual departures — Schedule II useful lives, no PP&E revaluation, standard inventory/gratuity/leave policy — but the Notes document itself is only 6 pages total and cuts off after note-page 4, i.e. even the surviving accounting-policy section is incomplete on standard topics (revenue recognition detail, taxation, financial instruments) | Note 2, pp.74-77 | 🟢 | What is readable is clean; but flags that even a "complete" version of this AR would have an unusually terse (6-page) Notes-to-Accounts document for a company of this balance-sheet size — worth a management question on disclosure depth once a clean copy is sourced |
