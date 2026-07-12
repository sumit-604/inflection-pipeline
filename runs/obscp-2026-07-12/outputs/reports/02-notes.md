# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: OBSC Perfection Limited (OBSCP) | Run date: 2026-07-12
Source: runs/obscp-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf (FY2024-25 Annual Report)
Basis: Pass 1 (runs/obscp-2026-07-12/outputs/reports/02-notes-pass1.md, full extraction) and Pass 2
(runs/obscp-2026-07-12/outputs/reports/02-notes-pass2.md, line-by-line verification/cross-check), both
already independently re-reading AR pp.60-77 in full (the only readable pages; pp.3-59 corrupted font,
pp.78-101 blank/truncated).

---

## PASS 3 — PATTERN READ

Approached the readable pages (60-77) one final time looking specifically for contradictions between
notes, numbers that do not match between notes and primary statements, deliberately vague disclosure next
to detailed disclosure, restated prior-year figures, post-balance-sheet events, and going-concern language.

**Findings from the pattern pass (beyond what Passes 1-2 already surfaced):**

1. **Contradiction pattern, Note 3 vs CARO Annexure A**: Note 2's sub-note 3 states flatly "The Company has
   no investments at present" (Note 3 within Note 2, p.76), while CARO Annexure A confirms in the same
   document that the company holds securities/loans in "its Subsidiaries, Joint Ventures, or Associate
   companies" (CARO para v/f, p.68) and extends running-account loans to subsidiaries/JVs (CARO para iii,
   p.65). This is not a numerical contradiction (the two disclosures are reconcilable — loans sit in Note 13
   "Loans & Advances" rather than an "Investments" line, and the company may hold no direct equity
   investment while still having group entities) but it is a juxtaposition worth flagging: a reader relying
   on Note 2 alone would conclude OBSCP has no group structure at all, which the Auditor's Report elsewhere
   contradicts. Already surfaced in Pass 1 Section 6 and Pass 2 §3.1; reconfirmed here as a genuine
   disclosure-contrast pattern, not a new item.
2. **Vague-vs-detailed disclosure pattern**: the EPCG export-obligation paragraph (Note 2.3(b), pp.75-76) is
   unusually precise (FOB value to the rupee, duty exemption to the rupee, USD equivalent, exact
   authorization date) yet contains the block-percentage inconsistency (50%+60% across a stated 6-year
   window) already confirmed verbatim in Pass 2 §3.4/§1 row 28. The precision elsewhere in the same
   paragraph makes the summing error stand out as a genuine drafting defect rather than a rounding
   convention, reinforcing Pass 2's conclusion.
3. **Blank note-number pattern**: two separate instances of missing/illegible cross-references were found
   independently in Pass 2 (RPT note number blank in CARO para xiii, p.67; Note 29 litigation reference
   present but its own content unreadable). Read together, this is a pattern of the audited document itself
   carrying internal referencing gaps (one blank field, one truncated target), not solely a scan/OCR issue
   confined to this recovered copy — worth naming as a document-quality observation distinct from the PDF
   truncation.
4. **No new restatements found**: Note 2.1(b)'s "regrouped and reclassified wherever required" boilerplate
   (p.74) is the only restatement-adjacent language on the readable pages; no item-level restated figures
   are visible anywhere in the Balance Sheet, P&L, or Cash Flow Statement (all single-column current vs
   prior year, no "as restated" markers).
5. **No going-concern language found** anywhere in the readable Auditor's Report or Notes 1-2, beyond the
   standard CARO (xix) 12-month liquidity boilerplate already noted in Pass 1.
6. **No post-balance-sheet events section is reachable** — Note 2's sub-note structure ends at 5.2 (p.77);
   any "Events after the Reporting Period" note (if present) would sit in the truncated Note-pages 5-6 of 6.
   NOT FOUND IN DOCUMENT.

No further material new findings beyond items 1-6 above, all of which either reconfirm and sharpen
Pass 1/Pass 2 items (EPCG blocks, blank note-number pattern, Note 3/CARO juxtaposition) or close open
questions in the negative (no restatements, no going-concern language, no post-balance-sheet events
recoverable). Proceeding directly to the consolidated analysis.

---

═══════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Entire numbered notes-schedule package (Notes 3 through at least Note 29 — RPT table, contingent liabilities/litigation, receivables ageing, inventory detail, subsidiaries/investments, borrowings instrument table, payables/MSME ageing, provisions movement, deferred tax reconciliation, revenue disaggregation, EPS reconciliation, CSR computation, capital commitments, segment reporting) is NOT FOUND IN DOCUMENT. Source AR is doubly degraded: pp.3-59 corrupted font (Board's Report/MD&A/Corp Gov, out of scope for this stage), pp.78-101 blank/truncated (note-pages 5-6 of the internally 6-page Notes document plus the entire schedule package) | Notes 3-29 (missing); pp.78-101 | 🔴 | Caps the evidence base for every downstream stage (valuation, quality scoring, cash-conversion assessment); a mechanical document gap, not a company-quality signal — must not be misread as a red flag on the company itself, but materially constrains what can be verified |
| 2 | Diluted EPS (₹8.12) exceeds Basic EPS (₹6.85) for FY2025 — confirmed byte-for-byte across two independent extractions (Pass 1 + Pass 2), confirmed arithmetically anomalous under AS 20 (dilutive shares can only add to the denominator, never raise EPS above Basic absent an anti-dilutive override), confirmed unexplainable from any readable page. FY2024 shows Basic = Diluted = ₹6.84 (no dilution, normal). This is present in the audited, signed financial statements as filed, not a transcription or OCR artifact | Note 26, p.72 (reconciliation NOT FOUND) | 🔴 | Single highest-priority accounting-quality item in this stage; unresolved after two independent verification passes; the weighted-average share-count reconciliation that would explain it sits in the truncated Note-pages 5-6; requires management clarification or a clean AR copy before this EPS figure can be trusted for any per-share valuation work downstream |
| 3 | Cash conversion weak: OCF ₹8.85 Cr vs PAT ₹16.76 Cr (~52.8% conversion). Fully bridged from readable pages alone (no missing-note dependency): OCF before WC ₹26.91 Cr, less current-asset increase ₹(26.81) Cr, plus current-liability increase ₹14.39 Cr (payables-driven), less taxes paid ₹(5.64) Cr = ₹8.85 Cr. Driven by Trade Receivables +62.3% YoY and Inventory +79.0% YoY, both far outpacing 24.1% revenue growth; partially offset (financed) by Trade Payables +118.3% YoY | Balance Sheet p.71; P&L p.72; Cash Flow Statement p.73 (ageing detail, Notes 14/15, NOT FOUND) | 🔴 | Direct working-capital/quality-of-earnings flag — feeds FLAG-CASH; per pipeline rule this caps at PROCEED WITH CAVEATS with the missing receivables-ageing/ECL evidence named, cannot resolve to a clean PROCEED |
| 4 | Trade Payables more than doubled, +118.3% YoY (₹25.31 Cr vs ₹11.59 Cr), against a comparable purchase-base growth of only +25.3% (Consumption & Manufacturing Expenses + Purchases of finished/traded goods combined) — payables stretching far outpaces even the broadest reasonable expense-base comparator | Note 9, p.71 (ageing/MSME detail NOT FOUND) | 🔴 | Payables stretching is the direct financing counterpart funding roughly half of the receivables/inventory buildup in #3 (₹14.39 Cr of the ₹26.81 Cr current-asset increase); MSME-specific ageing needed to assess supplier-relationship/timing risk, not recoverable from source |
| 5 | Short-term Provisions swung to a negative ₹(0.27) Cr in FY25 from a positive ₹0.66 Cr in FY24. Independently confirmed arithmetically genuine (not a transcription artifact): the Current Liabilities subtotal on the Balance Sheet only foots correctly (₹33.61 Cr) when Short-term Provisions is entered as −₹0.27 Cr | Note 11, p.71 (movement schedule NOT FOUND) | 🔴 | A negative provisions balance is structurally unusual; confirmed real by cross-footing, raising confidence it reflects a genuine reclassification or over-accrual reversal rather than a presentation error, but the specific mechanism is unrecoverable — direct, named management question |
| 6 | Related-party lending to subsidiaries/JVs: aggregate balance-sheet total now quantified — Long-term Loans & Advances (Note 13, p.71) ₹1.53 Cr FY25 vs ₹1.00 Cr FY24, +52.9% YoY — confirmed via CARO Annexure A para iii (running current account, monthly interest, auditor considers rates not prejudicial, no overdue >90 days). Counterparty-level breakdown (names, individual amounts, rates, tenure) remains unrecoverable | Note 13, p.71; CARO Annexure A para iii, p.65 (counterparty detail NOT FOUND) | 🟡 | Related-party exposure is now bounded and quantified in aggregate rather than entirely unknown (a Pass 2 correction to Pass 1's overstated gap), but non-arm's-length risk cannot be assessed without counterparty-level detail; growth rate (+52.9%) alone is not alarming but should be monitored |
| 7 | EPCG capital-goods import: FOB value ₹8.09 Cr, customs duty exemption ₹1.35 Cr, export obligation = 6x duty saved (₹8.09 Cr) over 6 years from Authorization date 26-12-2024. The stated fulfilment blocks ("1st to 4th year — 50%", "5th to 8th year — 60%") sum to 110% and the second block's year-range (5th-8th) extends beyond the stated 6-year total window — confirmed verbatim across two independent extractions, a genuine AR drafting inconsistency, not an OCR artifact | Note 2.3(b), pp.75-76 | 🟡 | Unfulfilled export obligation is a real contingent liability (duty-plus-penalty clawback risk) not separately visible in the missing contingent liabilities table (Note 29); the drafting inconsistency itself should be raised with management/auditors to confirm the actual obligation schedule |
| 8 | Auditor found voucher edits under the mandatory audit-trail (edit-log) feature during FY25 on test check; attributed by the auditor to accounting staff being "not well versed with the intricacies of operating the audit-trail-compliant software," characterised as a "reasonable cause," no P&L/Balance Sheet impact asserted | Independent Auditor's Report, pp.62-63 | 🟡 | Direct evidence-integrity/control-quality item concerning the audit trail SEBI/MCA mandates; auditor's characterisation is low-severity, but this bears directly on confidence in the underlying ledger and should be monitored in subsequent years' audit reports |
| 9 | Effective tax rate ≈18.8% FY25 (Provision for Tax ₹4.65 Cr + Deferred Tax credit ₹(0.78) Cr = ₹3.87 Cr total tax on PBT ₹20.63 Cr), materially below the ~25.17% standard statutory rate. Fully reconciled arithmetically (total tax ties to PAT and to "Transferred to Reserves") but the qualitative reconciling items (MAT credit, depreciation-timing, incentive-linked deductions) that would normally explain the gap sit in the missing Note 6 schedule | Note 6, pp.71-72 (reconciliation NOT FOUND) | 🟡 | Cannot assess whether the sub-statutory effective rate is a clean, sustainable MAT-credit/depreciation-timing effect or something requiring more scrutiny (e.g., unsustainable one-time credits) without the deferred-tax reconciliation note |
| 10 | Company converted from Private to Public Limited during FY25 (28 June 2024) with a large capital raise: Share Capital +37.0% (₹17.85 Cr → ₹24.45 Cr), Reserves & Surplus +550.8% (₹12.22 Cr → ₹79.54 Cr), ₹57.16 Cr fresh share capital/premium infusion per the Cash Flow Statement, total Balance Sheet size +83.2% (₹86.51 Cr → ₹158.55 Cr) | Note 1, p.74; Balance Sheet p.71; Cash Flow Statement p.73 | 🟢 | Confirms the transition-alpha thesis context (private-to-public conversion, pre-listing primary capital raise); clean, fully cross-verified, no red flag |
| 11 | Deleveraging in FY25: Long-term Borrowings −21.8% (₹25.60 Cr → ₹20.02 Cr), Short-term Borrowings −56.2% (₹15.88 Cr → ₹6.95 Cr), net ₹(14.50) Cr outflow in the Cash Flow Statement's borrowings line — funded by the equity raise (#10) rather than by operating cash flow, which itself only generated ₹8.85 Cr (#3). CARO confirms no default, no wilful-defaulter designation, term loans applied for stated purpose, no short-term-to-long-term fund diversion | Notes 5 & 8, p.71; CARO Annexure A paras ix(a)-(d), p.66 | 🟢 | Deleveraging itself is a clean signal, though the source of funding (dilution, not internally generated cash) should be read alongside the weak cash conversion in #3 rather than in isolation |
| 12 | Finance costs rose +16% (₹2.69 Cr → ₹3.12 Cr) despite falling average borrowings (both long- and short-term borrowings declined YoY per #11) — mildly inconsistent on its face; would normally be explained by rate detail and paydown timing in the borrowings note, which is unrecoverable | Note 23, p.72 (borrowings detail NOT FOUND) | 🟡 | A minor but genuine inconsistency between the direction of the borrowings balance and the direction of the finance-cost charge; plausibly explained by mid-year paydown timing or rate resets, but cannot be confirmed from source |
| 13 | Other Income more than doubled (₹1.08 Cr → ₹2.41 Cr); only ₹0.86 Cr of the FY25 total is confirmed as interest income (per the Cash Flow Statement), leaving ~₹1.55 Cr of Other Income with no readable composition disclosure | Note 19, p.72 (composition detail NOT FOUND) | 🟡 | Unexplained non-recurring-vs-recurring composition of a P&L line that grew materially faster than revenue; could include one-time items (e.g., forex gains, asset sale gains, government grants) that a clean quality-of-earnings assessment would need to strip out |
| 14 | Contradiction/juxtaposition pattern: Note 2 sub-note 3 states "The Company has no investments at present" (p.76), while CARO Annexure A independently confirms the company holds subsidiary/JV/associate group entities and extends running-account loans to them (paras iii and v/f, p.65 and p.68). Reconcilable (group-entity lending sits in Loans & Advances, not an Investments line) but a reader relying on Note 2 alone would miss the group structure entirely | Note 3 (within Note 2), p.76; CARO Annexure A paras iii, v/f, pp.65 & 68 | 🟡 | Disclosure-contrast pattern surfaced in the Pass 3 pattern read; equity stakes, ownership %, and carrying values in subsidiaries/JVs (if any exist beyond the loan relationship) are not separately quantified anywhere in the readable document |
| 15 | Statutory dues overdue for >6 months exist per CARO ("except those stated in the Note No. 10 on Accounts," para vii(b), p.66); the amount is bounded above by the Note 10 "Other Current Liabilities" aggregate of ₹1.62 Cr FY25 (vs ₹1.09 Cr FY24, +48.8% YoY) but the specific overdue quantum within that aggregate, and the RPT note number itself (blank/illegible in the source per CARO para xiii, p.67), are both unrecoverable | Note 10, p.71; CARO Annexure A paras vii(b) & xiii, pp.66-67 | 🟡 | Two separate named data gaps (overdue statutory dues quantum; illegible RPT note cross-reference) that are internal to the source document itself, not solely attributable to the PDF truncation — worth flagging to the operator as items to source from a clean AR copy |

---

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | NOT ASSESSABLE (Note 18 disaggregation, contract assets/liabilities, and revenue policy detail all in truncated zone) | — |
| Expense capitalisation honesty | 6/10 (partial) | PP&E/depreciation policy readable and unremarkable (Schedule II lives, no revaluation, standard borrowing-cost capitalisation); but capitalisation-threshold and fixed-asset schedule detail (Notes 12A/12B) NOT FOUND, so cannot fully verify application |
| Provisioning adequacy | 3/10 | Negative short-term provisions balance (#5) is a confirmed, unexplained anomaly; no movement schedule, actuarial assumptions, or litigation-provision detail available to assess adequacy elsewhere |
| RPT fairness | 4/10 (partial) | Aggregate related-party loan balance now quantified (#6) and CARO gives a qualitative "not prejudicial" assessment, but no counterparty-level detail, no royalty/fee/rent-to-promoter disclosure, and the RPT note number itself is illegible in the source (#15) |
| Disclosure transparency | 2/10 | The single largest driver of this stage's findings: the entire numbered schedule-notes package (Notes 3-29) is unavailable, and even the surviving accounting-policy section (Notes 1-2) is itself incomplete, cutting off mid-policy at note-page 4 of an internally 6-page document. This score reflects what is recoverable from this specific file, not necessarily the company's underlying disclosure practice in a complete AR |
| Consistency with prior years | 6/10 | No item-level restatements found; standard "regrouped/reclassified wherever required" boilerplate only; primary statements are internally consistent and cross-foot correctly (Pass 2 verification), but YoY consistency of accounting judgments (ECL matrix, provisioning basis) cannot be assessed without the notes |
| **OVERALL** | **3/10** | Dominated by the disclosure-transparency gap (a document/evidence problem, not necessarily a company-quality problem) combined with two genuine, source-confirmed accounting-quality anomalies that remain unresolved after two verification passes: the Diluted-EPS-exceeds-Basic-EPS anomaly (#2) and the negative short-term provisions balance (#5). Neither anomaly can be waved away as a document-truncation artifact — both are confirmed present and arithmetically real in the readable, audited primary statements themselves |

---

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Cash conversion / working-capital quality (receivables +62.3%, inventory +79.0%, payables +118.3% vs 24.1% revenue growth; OCF/PAT ~52.8%) | High | Next quarter/annual receivables ageing and DSO; whether payables stretching reverses (supplier terms tightening) | Could crystallise in FY26 if receivables are not collected or payables come due faster than customers pay — direct liquidity/covenant risk |
| Diluted EPS > Basic EPS anomaly (unresolved) | High (accounting-quality, not cash) | Whether FY26 AR (or a clean copy of this FY25 AR) resolves the weighted-average share-count reconciliation; any restatement | Any subsequent filing correction or auditor qualification |
| Negative short-term provisions balance | Medium | Whether FY26 balance normalises (returns positive) and whether a note explains the FY25 reversal | Next annual report's Note 11 schedule, if a clean/complete copy becomes available |
| EPCG export-obligation drafting inconsistency (110%-summing blocks) | Medium | Actual export performance against the ₹8.09 Cr obligation within the 6-year window (from 26-12-2024); any DGFT correspondence | Obligation period runs through ~2030-31; shortfall risk crystallises at each block's review, and duty-plus-penalty clawback risk if unmet |
| Related-party lending growth (+52.9% YoY, aggregate) with no counterparty transparency | Medium | Whether the aggregate keeps growing faster than operating scale; any disclosure of counterparty names/terms in a future clean AR | Ongoing; would sharpen if growth accelerates further or if a counterparty is a loss-making subsidiary |
| Audit-trail (edit-log) voucher amendments | Low-Medium | Next year's Auditor's Report — whether the same finding recurs (would upgrade severity) or is resolved (staff training addressed) | FY26 Auditor's Report |
| Entire schedule-notes package unavailable (structural evidence gap, not a company signal) | N/A (document risk, not company risk) | Sourcing a clean/complete copy of the FY25 AR before any downstream valuation or quality conclusion is finalised | Immediate — should be resolved before this run's verdict is finalised if feasible |

---

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Please reconcile the FY2025 EPS calculation: Basic EPS is stated as ₹6.85 and Diluted EPS as ₹8.12 (Note
   26, p.72) — diluted EPS exceeding basic EPS is not ordinarily possible under AS 20. What is the
   weighted-average share count used in each calculation, and what dilutive/anti-dilutive instruments are
   involved?
2. What caused Short-term Provisions to move from a positive ₹0.66 Cr (FY24) to a negative ₹(0.27) Cr
   (FY25) (Note 11, p.71)? Please provide the provisions movement schedule (opening balance, additions,
   utilisations, reversals) underlying this swing.
3. Trade Receivables grew 62.3% and Inventory grew 79.0% YoY against 24.1% revenue growth, while OCF
   converted only ~52.8% of PAT. Can you provide the receivables ageing schedule, single-customer
   concentration, and the specific drivers (new customer terms, channel stuffing, slow-moving inventory
   builds ahead of the new Pune unit ramp-up) behind this working-capital stretch?
4. The EPCG export-obligation disclosure (Note 2.3(b), pp.75-76) states fulfilment blocks of "50%" for
   years 1-4 and "60%" for years 5-8, which sum to 110% against a stated 6-year total obligation window.
   Can you clarify the actual block structure and current progress against the ₹8.09 Cr export obligation?
5. Please provide the counterparty-level detail (subsidiary/JV names, individual loan amounts, interest
   rates, tenure) underlying the aggregate Long-term Loans & Advances balance of ₹1.53 Cr (Note 13, p.71,
   +52.9% YoY), and confirm the note number referenced in CARO Annexure A para xiii (p.67) for related-party
   transactions, which is blank/illegible in the recovered copy of this annual report.

---

## E. NOTES-BASED RED FLAGS

- **Earnings management indicator (unresolved)**: Diluted EPS exceeding Basic EPS is arithmetically
  anomalous and, absent explanation, raises a question about whether the diluted share count or the
  underlying net-profit allocation used in the EPS calculation is correctly stated. Not asserted as
  deliberate manipulation — could be a drafting/typesetting error in the filed statements — but it is a
  genuine, source-confirmed anomaly that a diligence-minded investor cannot wave away.
- **Aggressive working-capital management**: the combination of sharply rising receivables and inventory
  funded substantially by stretched payables (rather than internally generated cash) is a classic
  quality-of-earnings pattern worth monitoring, though it falls short of being labelled manipulation absent
  the ageing/customer-concentration detail that would confirm or refute genuine collectability concerns.
- **Undisclosed risk indicator**: the negative short-term provisions balance is unexplained and, by
  definition, represents either an over-accrual reversal (which would have inflated a prior period's
  provisioning and reduced the current period's) or a reclassification whose net effect on comparability
  cannot be assessed without the movement schedule.
- **Control-quality indicator (low severity per auditor)**: the audit-trail voucher-amendment finding is
  explicitly not characterised by the auditor as an income/loss-affecting issue, but it is a factual,
  disclosed control observation that belongs in this section for completeness.

---

## F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices, though the primary driver is a severe evidence gap rather
than confirmed misconduct. Key concern: the unresolved Diluted EPS (8.12) exceeding Basic EPS (6.85)
anomaly, compounded by weak cash conversion (52.8% of PAT) and the complete unavailability of the
numbered notes-schedule package (Notes 3-29) due to a doubly-degraded source AR. Key strength: the
readable primary statements are internally consistent and fully cross-foot (Pass 2 verification), the
capital-raise and deleveraging narrative is clean and well-evidenced, and no going-concern language or
item-level restatements appear anywhere in the recoverable text. Overall accounting quality: 3/10.

---

## SOURCE PAGE MAP (final, corrected per Pass 2)

| AR page(s) | Content | Readability |
|---|---|---|
| 1 | Cover letter to NSE | Readable |
| 2 | AR cover | Image, readable |
| 3-59 | Board's Report, MD&A, Corporate Governance Report | Corrupted font — unreadable (out of scope for this stage; flagged for downstream inheritance to B01/board-report stage) |
| 60-70 | Independent Auditor's Report + Annexures A & B (CARO, ICFR) | Readable |
| 71 | Balance Sheet as at 31 March 2025 | Readable |
| 72 | Statement of Profit & Loss FY2024-25 | Readable |
| 73 | Cash Flow Statement FY2024-25 | Readable |
| 74-77 | Notes to Financial Statements — Note 1 + Note 2 (sub-topics 1 through 5.2) = note-pages 1-4 of an internally 6-page Notes document | Readable |
| 78-101 | BLANK — note-pages 5-6 of 6 (rest of Note 2) plus the entire schedule Notes package (Note 3 through at least Note 29) lost here | Not recoverable |

---

```yaml
stage: B02-notes
company: "OBSCP"
run_date: "2026-07-12"
model: claude-sonnet-5
status: complete
input_gaps:
  - "AR pp.3-59: corrupted/garbled font encoding, unreadable even visually (Board's Report, MD&A, Corporate Governance Report) — out of scope for this Notes stage but flagged for downstream B01/board-report inheritance"
  - "AR pp.78-101: blank/truncated in source PDF — note-pages 5-6 of an internally 6-page Notes document (remainder of Note 2 policy topics) plus the entire numbered schedule-notes package (Note 3 through at least Note 29: RPT table, contingent liabilities/litigation detail, receivables ageing, inventory category detail, subsidiaries/investments detail, borrowings instrument table, payables MSME ageing, provisions movement/actuarial assumptions, deferred tax reconciliation, revenue disaggregation, EPS weighted-average reconciliation, CSR computation, capital commitments, segment reporting) — all marked NOT FOUND IN DOCUMENT, none estimated"
  - "RPT note number itself is blank/illegible in the source document (CARO Annexure A para xiii, p.67) — not recoverable even with a complete PDF unless a clean copy is sourced"
flags:
  - {type: FLAG-CASH, reason: "OCF Rs 8.85 Cr vs PAT Rs 16.76 Cr (~52.8% conversion); Trade Receivables +62.3% YoY and Inventory +79.0% YoY vs 24.1% revenue growth; Trade Payables +118.3% YoY partially funding the buildup; receivables ageing and ECL adequacy unrecoverable from source (Notes 14/15 truncated) so the flag cannot be resolved to clean, caps at PROCEED WITH CAVEATS"}
  - {type: FLAG-ACCOUNTING-QUALITY, reason: "Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) for FY2025, confirmed genuine and unexplained across two independent verification passes; arithmetically anomalous under AS 20; weighted-average share reconciliation unrecoverable (truncated Note 26 detail)"}
  - {type: FLAG-ACCOUNTING-QUALITY, reason: "Short-term Provisions balance is negative Rs (0.27) Cr in FY25 vs positive Rs 0.66 Cr in FY24, confirmed arithmetically real via balance sheet cross-footing; cause unrecoverable (Note 11 movement schedule truncated)"}
accounting_quality: 3        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Entire numbered notes-schedule package (Notes 3-29) NOT FOUND IN DOCUMENT due to doubly-degraded source AR (pp.3-59 corrupted font, pp.78-101 blank/truncated)", note_ref: "Notes 3-29, pp.78-101", rating: "RED", why: "Caps evidence base for all downstream stages; mechanical document gap, not a company-quality signal"}
  - {rank: 2, finding: "Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) FY2025, confirmed genuine and unresolved across two verification passes; FY2024 Basic=Diluted=Rs 6.84", note_ref: "Note 26, p.72", rating: "RED", why: "Highest-priority accounting-quality item; arithmetically anomalous under AS 20; unexplained from source"}
  - {rank: 3, finding: "Cash conversion weak: OCF Rs 8.85 Cr vs PAT Rs 16.76 Cr (~52.8%), fully bridged from readable pages; driven by receivables +62.3% and inventory +79.0% YoY vs 24.1% revenue growth", note_ref: "Balance Sheet p.71; Cash Flow Statement p.73", rating: "RED", why: "Direct working-capital/quality-of-earnings flag feeding FLAG-CASH; caps at PROCEED WITH CAVEATS"}
  - {rank: 4, finding: "Trade Payables +118.3% YoY (Rs 25.31 Cr vs Rs 11.59 Cr) vs only +25.3% combined purchase-base growth", note_ref: "Note 9, p.71", rating: "RED", why: "Payables stretching funds roughly half the receivables/inventory buildup; MSME ageing detail unrecoverable"}
  - {rank: 5, finding: "Short-term Provisions negative Rs (0.27) Cr FY25 vs positive Rs 0.66 Cr FY24, confirmed arithmetically real via balance-sheet cross-footing", note_ref: "Note 11, p.71", rating: "RED", why: "Structurally unusual negative provisions balance; mechanism unexplained; direct management question"}
  - {rank: 6, finding: "Related-party loans to subsidiaries/JVs aggregate now quantified: Rs 1.53 Cr FY25 vs Rs 1.00 Cr FY24, +52.9% YoY; counterparty breakdown unrecoverable", note_ref: "Note 13, p.71; CARO Annexure A para iii, p.65", rating: "YELLOW", why: "Bounds related-party exposure in aggregate but non-arm's-length risk cannot be assessed without counterparty detail"}
  - {rank: 7, finding: "EPCG export obligation Rs 8.09 Cr over 6 years from 26-12-2024; fulfilment blocks (50%+60%) sum to 110%, confirmed verbatim as a genuine AR drafting inconsistency", note_ref: "Note 2.3(b), pp.75-76", rating: "YELLOW", why: "Unfulfilled export obligation is a real contingent liability not visible in the missing contingent liabilities table"}
  - {rank: 8, finding: "Auditor found voucher edits under mandatory audit-trail feature during FY25, attributed to staff unfamiliarity, no P&L/BS impact asserted", note_ref: "Auditor's Report, pp.62-63", rating: "YELLOW", why: "Evidence-integrity/control-quality item concerning the mandated audit trail; low severity per auditor but worth monitoring"}
  - {rank: 9, finding: "Effective tax rate ~18.8% FY25, materially below ~25.17% statutory rate; arithmetically reconciled to PAT but qualitative reconciling items unrecoverable", note_ref: "Note 6, pp.71-72", rating: "YELLOW", why: "Cannot assess sustainability of the sub-statutory rate without the deferred tax reconciliation note"}
  - {rank: 10, finding: "Private-to-Public conversion (28 June 2024) with large capital raise: Share Capital +37.0%, Reserves +550.8%, Rs 57.16 Cr fresh capital/premium, Balance Sheet +83.2%", note_ref: "Note 1, p.74; Balance Sheet p.71; Cash Flow Statement p.73", rating: "GREEN", why: "Confirms transition-alpha thesis context; clean, fully cross-verified"}
  - {rank: 11, finding: "Deleveraging FY25: Long-term Borrowings -21.8%, Short-term Borrowings -56.2%, funded by equity raise not operating cash flow; no default per CARO", note_ref: "Notes 5 & 8, p.71; CARO Annexure A paras ix(a)-(d), p.66", rating: "GREEN", why: "Clean signal but funded by dilution, not internally generated cash; read alongside weak cash conversion"}
  - {rank: 12, finding: "Finance costs +16% despite falling average borrowings, mildly inconsistent, unreconciled due to missing borrowings note detail", note_ref: "Note 23, p.72", rating: "YELLOW", why: "Minor inconsistency between borrowings direction and finance-cost direction, plausibly timing-driven but unconfirmed"}
  - {rank: 13, finding: "Other Income more than doubled (Rs 1.08 Cr to Rs 2.41 Cr); only Rs 0.86 Cr confirmed as interest income, ~Rs 1.55 Cr composition unexplained", note_ref: "Note 19, p.72", rating: "YELLOW", why: "Unexplained composition of a fast-growing P&L line relevant to quality-of-earnings adjustment"}
  - {rank: 14, finding: "Disclosure contradiction/juxtaposition: Note 2 states company has no investments while CARO confirms subsidiary/JV group entities and related-party lending exist", note_ref: "Note 3 (within Note 2), p.76; CARO Annexure A paras iii, v/f, pp.65 & 68", rating: "YELLOW", why: "Reconcilable but a reader relying on Note 2 alone would miss the group structure entirely; surfaced in Pass 3 pattern read"}
  - {rank: 15, finding: "Statutory dues overdue >6 months exist per CARO, bounded above by Rs 1.62 Cr Other Current Liabilities aggregate; RPT note cross-reference number itself blank/illegible in source", note_ref: "Note 10, p.71; CARO Annexure A paras vii(b) & xiii, pp.66-67", rating: "YELLOW", why: "Two named data gaps internal to the source document itself, not solely attributable to PDF truncation"}
red_flags:
  - "Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) FY2025 — arithmetically anomalous under AS 20, confirmed genuine across two verification passes, unresolved (Note 26, p.72)"
  - "Negative short-term provisions balance Rs (0.27) Cr FY25, confirmed arithmetically real via balance-sheet cross-footing, mechanism unexplained (Note 11, p.71)"
  - "Working-capital quality: receivables +62.3%, inventory +79.0%, payables +118.3% YoY vs 24.1% revenue growth, OCF/PAT conversion only ~52.8%"
questions_for_mgmt:
  - "Reconcile the FY2025 EPS calculation given Diluted EPS (Rs 8.12) exceeds Basic EPS (Rs 6.85) — what weighted-average share counts and dilutive instruments were used? (Note 26, p.72)"
  - "What caused Short-term Provisions to swing from Rs 0.66 Cr (FY24) to negative Rs (0.27) Cr (FY25)? Provide the movement schedule. (Note 11, p.71)"
  - "Provide the receivables ageing schedule, single-customer concentration, and drivers behind receivables +62.3% and inventory +79.0% YoY growth against 24.1% revenue growth."
  - "Clarify the EPCG export-obligation block structure (50%+60% summing to 110% against a 6-year window) and current progress against the Rs 8.09 Cr obligation. (Note 2.3(b), pp.75-76)"
  - "Provide counterparty-level detail for the Rs 1.53 Cr related-party loans/advances balance (Note 13, p.71, +52.9% YoY) and confirm the note number for related-party transactions referenced but left blank in CARO Annexure A para xiii (p.67)."
receivables_trend: "deteriorating - Trade Receivables Rs 34.93 Cr FY25 vs Rs 21.53 Cr FY24, +62.3% YoY, against Income from Operations growth of only +24.1% (Balance Sheet p.71; P&L Note 18 p.72); ageing schedule, single-customer concentration, and ECL provision adequacy NOT FOUND IN DOCUMENT (Note 15 truncated, pp.78-101)"
restatements_found: []
going_concern_language: "NONE - CARO Annexure A para (xix), p.68, gives an unmodified 12-month liquidity opinion subject to standard boilerplate ('no major financial, health or political turmoil'); no management going-concern disclosure found in readable Notes 1-2 or Auditor's Report"
```
