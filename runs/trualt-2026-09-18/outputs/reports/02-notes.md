# STAGE 2 — NOTES TO FINANCIAL STATEMENTS, PASS 3 OF 3 (PATTERN PASS + CONSOLIDATION)
Company: TruAlt Bioenergy Ltd (TRUALT) | Run: trualt-2026-09-18 | Model: claude-sonnet-5
Source: Annual_Report_2026.pdf (FY2025-26, 359 pp, ₹ lakh), text route
runs/trualt-2026-09-18/inputs/annual-report/Annual_Report_2026.txt
Prior passes: outputs/reports/02-notes-pass1.md, outputs/reports/02-notes-pass2.md
(both fully re-read as the base for this pass).

---

## PASS 3 — PATTERN RE-READ

Read a third time against four lenses: notes that contradict each other,
note numbers that do not match the face financials, notes disclosed with
visibly different depth to their neighbours, and prior-period restatement
or going-concern language. Two of the four lenses were already substantially
covered by Passes 1-2 (contradictions, standalone-vs-consolidated mismatches).
This pass reports what those earlier passes surfaced case by case, but had
not yet named as a PATTERN, plus two clean checks (restatement, going
concern) that close out the lens list.

1. **PATTERN, not isolated glitch: NIL / full-compliance assertions
   recur alongside harder numbers that undercut them, at least three
   separate times in the standalone notes alone.** (a) Note 57 states NIL
   contingent liabilities; Note 8 discloses a corporate guarantee for
   TGPL's NABARD facility; Note 39(D)(4)/38(D)(4) states flatly "no
   guarantees provided or received." (b) Note 53 (Capital management)
   states the Company "has complied with all externally imposed capital
   requirements and financial covenants... no breaches during the year";
   Note 52's own Schedule III ratio table shows DSCR at 0.99x, a
   sub-1x coverage figure, with the lender's own DSCR definition and
   threshold never disclosed to let a reader verify the compliance claim.
   (c) The credit-terms disclosure itself differs between note sets: "7 to
   27 days" (consolidated Note 42(C)) vs "21 to 27 days" (standalone Note
   42(C)), a small but real internal inconsistency on a number used
   elsewhere (Section 4, receivables ageing) to judge severity. Three
   independent instances of the same failure mode, each previously logged
   individually in Pass 1 or Pass 2, together constitute a *pattern* of
   assertion-versus-number tension rather than three unrelated slips. 🔴
   PATTERN FINDING (new framing, not a new fact).
2. **Disclosure-depth asymmetry: precision is high on routine, low-risk
   items and low on the one item with related-party/subsidiary risk.**
   The borrowings note prices every facility to two decimal places and a
   named security package (Note 20, standalone); the actuarial note
   discloses a full four-way sensitivity table (Note 37); but the one
   number with real contingent-liability exposure — the NABARD guarantee
   for TGPL — is named with no ₹ amount anywhere in the note itself (Note
   8). The company's disclosure appetite is not uniformly thin; it is
   selectively thin exactly where a related-party subsidiary exposure
   sits. 🟡 PATTERN FINDING (new framing).
3. **Numbers vs face financials:** beyond the Note 29/30 finished-goods
   aggregation nuance already reconciled arithmetically in Pass 2 (not an
   error), no further note-to-face mismatch was found on this third read.
   PBT, revenue, and borrowings totals used across notes tie to the figures
   Pass 1 and Pass 2 already anchored. No new item.
4. **Restatements:** NOT FOUND IN DOCUMENT. No note in either note set
   describes a prior-period restatement or reclassification of a
   previously reported figure. The direct DTL-to-retained-earnings credit
   on CCPS conversion (Pass 1, Section 12) is a permitted Ind AS
   presentation choice, not a restatement, and is not reclassified here.
5. **Going concern language:** NONE found. No note in either set (or the
   Schedule III ratio note, which is the closest a reader gets to a
   solvency commentary) uses going-concern language. The auditor's report
   itself sits outside this stage's scope (notes only).

Net effect of this pass: two genuine new pattern-level readings (items 1-2
above), both built from facts Pass 1/Pass 2 already anchored individually.
No new rupee figure emerges. Proceeding to consolidation.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Government-scheme income (interest subvention + PLI) is **73.2% of standalone PBT** (₹8,018.19 lakh of ₹10,947.48 lakh, FY26) | Note 27/28 (both sets) | 🔴 | Core operating profitability is a minority of reported PBT; both schemes are policy-contingent and time-bound, with no sensitivity to discontinuation disclosed |
| 2 | Related-party feedstock purchases from Nirani-group entities are **72.6% of total raw-material purchases FY26 and EXCEED 100% of disclosed total purchases FY25** | Notes 28 & 38 standalone; 29 & 39 consolidated | 🔴 | Single-counterparty-group dependency for the core input, with an unreconciled arithmetic gap between two notes in the same filing |
| 3 | **Net debt ROSE** (standalone ₹1,384.62cr → ₹1,532.41cr, +10.7%; consol. +11.3%) despite a ₹750cr gross IPO; gearing improved only because the equity denominator grew | Note 53 (Capital management, both sets) | 🔴 | The deleveraging narrative implied by the IPO did not happen; equity dilution, not debt reduction, drove the ratio |
| 4 | Short-term contractual financial obligations (**₹750.4cr consol.**) are **8-15x** cash on hand (₹88.3cr consol. / ₹48.1cr standalone) | Note 42(D)/41(D), both sets | 🔴 | Company-disclosed hard evidence of rollover dependency on short-term debt and receivable/grant collection, not a cash cushion |
| 5 | **DSCR fell to 0.99x (FY26) from 1.28x (FY25)**, the company's own mandatory ratio, with no explanation despite exceeding its own 25%-variance disclosure trigger | Note 52 standalone, p.355 | 🔴 | Net operating income did not fully cover debt service in the year; covenant threshold undisclosed so breach cannot be ruled in or out |
| 6 | Standalone **inventory +155.6%** (₹204.2cr → ₹521.8cr) while **revenue fell 9.3%**; finished goods alone +136.2%, no write-down or composition narrative given | Note 11 standalone | 🔴 | Inventory build sharply outpaced and diverged from revenue direction; no management explanation of finished-goods composition |
| 7 | Corporate guarantee for TGPL's NABARD loan (Note 8) contradicts the NIL contingent-liability note (Note 57) and the "no guarantees" RPT statement (Note 39(D)(4)/38(D)(4)) | Notes 8, 57, 38(D)(4)/39(D)(4) | 🔴 | Three-way internal inconsistency within the same standalone financial statements on a contingent-liability disclosure |
| 8 | Related-party trade payables funded **63.9% (FY26) / 73.5% (FY25)** of total payables; FY25 working capital was **negative ₹183.1cr**, turning positive only after the IPO | Notes 24, 38, 52 | 🔴 | Pre-IPO working capital was structurally financed by promoter-family trade credit, a load-bearing structural fact for the RPT dependency thesis |
| 9 | **Consolidated capital commitments (₹163.7cr) are ~20x the standalone figure (₹7.9cr)** — TGPL alone carries an estimated ~₹155.8cr of forward CBG capex invisible in a standalone-only read | Note 56, consolidated vs standalone | 🔴 | Corrects a "capex is winding down" reading built from the standalone note only; a large new capital programme is ramping up inside the subsidiary |
| 10 | Two separate **~14-week Company Secretary vacancies** (immediately pre- and post-IPO listing) plus a **~6-week CFO vacancy** (Jan-Feb 2025) | Note 39/38 (KMP tenure dates, both sets) | 🔴 | Governance-continuity gap at the two most SEBI LODR compliance-sensitive moments in the company's listed history; visible only by reading KMP dates against the IPO timeline |
| 11 | Trade receivables "not due" share collapsed **69.1% → 34.7%**, "overdue under 6 months" jumped **20.2% → 57.6%**, against a stated 7-27 (consol.) / 21-27 (standalone) day credit term; turnover fell 21% | Note 12, Note 42(C)/41(C), Note 52 | 🟡 | Short-cycle receivables are running several multiples of the stated credit term past due; long tail (>6 months) actually improved slightly |
| 12 | FY26 standalone CFO **−₹296.15cr**; the ₹425cr IPO working-capital tranche was fully utilised per the utilisation table but absorbed by operating cash burn and inventory build, not retained as liquidity | Notes 18, 19, 60/61, cash flow statement | 🟡 | IPO proceeds functioned as a cash-burn backstop, not a war chest; net cash actually received was ₹665.71cr, below the ₹750cr headline |
| 13 | PLI revenue booked ahead of formal claim filing; total government-scheme receivables (interest subvention + PLI + other incentive) grew **31.7%** to ₹129.5cr even as revenue fell 9.4% | Notes 15/16, 26/27 | 🟡 | Judgement-based accrual of government income ahead of realisation, with the receivable growing even as current-year recognised income shrank |
| 14 | Nirani Holdings (promoter entity) sold TGPL shares to Sumitomo Corporation at ₹30.90/share, a ~29% premium to the Company's own ₹24/share entry price 8 months earlier, no pricing rationale disclosed, event named only in consolidated notes | Note 36 standalone / Note 59 consolidated | 🟡 | Related-party entity captured a pricing uplift the Company itself did not, on a subsidiary the Company controls; asymmetric subsequent-event disclosure between note sets |
| 15 | PATTERN: NIL/full-compliance assertions (contingent liabilities, covenant compliance, credit terms) recur at least three times against harder numbers disclosed elsewhere in the same note set | Notes 57 vs 8/39(D)(4); Note 53 vs Note 52; Note 42(C) consol. vs standalone | 🟡 | Not three isolated slips — a recurring disclosure-consistency weakness across the standalone and consolidated note sets, this pass's own contribution |

Findings outside the top 15 but retained in the risk/red-flag sections
below: asset pledge growth to ₹343-355cr (+27-29% YoY) with a continuously
rolled promoter share pledge since Feb-2023 (Note 54); new unitemised RPT
lines (₹15.08cr "secondary sale of shares" expense to Nirani Holdings FY25,
reimbursement of expenses +172% FY26, a small direct land purchase from the
Managing Director) (Note 39/38); both operating segments' results falling
YoY with CBG segment liabilities +790% on TGPL's NABARD debt entering
consolidation (Note 40/39); the ₹20cr TGPL capital-infusion reconciliation
gap (Note 8/36); unexplained "Miscellaneous income" ~8-10x jump and
volatile "provision written back" other-operating-revenue line (Note
27/28); the standalone-only 96.4% capital-commitment collapse, which is the
one clean confirmatory finding in the corpus (Note 56 standalone) — the
multi-feed capex programme completed on schedule, at the parent level.

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 4 | PLI booked ahead of claim filing on management judgement; government-scheme income (73.2% of standalone PBT) dominates reported profitability; volatile, unexplained "other operating revenue" write-back and miscellaneous-income lines |
| Expense capitalisation honesty | 7 | Specific borrowing costs on the three grain-conversion units are quantified and traceable to named, dated capex; PPE componentisation still in progress at signing (a live estimate, not settled) is the one open item |
| Provisioning adequacy | 6 | ECL nil is justified by the OMC customer base; full actuarial sensitivity table given; but no inventory write-down/obsolescence figure disclosed despite a 155.6% inventory build |
| RPT fairness | 3 | Feedstock purchases exceed 100% of disclosed total purchases in FY25 (unreconciled); trade payables majority-funded by the same group; corporate guarantee for a related entity omitted from the contingent liabilities note; new unitemised RPT lines with no pricing rationale |
| Disclosure transparency | 4 | Customer names not disclosed; corporate guarantee amount not stated; unrecognised DTA and capitalisation threshold not disclosed; three separate contradiction patterns (guarantee/NIL, DSCR/compliance, credit terms) within the same document |
| Consistency with prior years | 6 | First full listed-company FY; no restatements found; the one large prior-year tax reconciliation item is explained as a one-off correcting entry, not left ambiguous |
| **OVERALL** | **4** | Weighted down by the RPT and disclosure-transparency dimensions, which carry the most investor-relevant findings (guarantee contradiction, RPT concentration, DSCR); no evidence of fraud, restatement, or auditor qualification found within the notes' scope |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Related-party feedstock concentration (Nirani group) | High | RPT pricing disclosure at next AGM, independent-director RPT approval minutes, purchase-vs-total-purchases reconciliation | Ongoing; sharpest at next crush-season contract renewal |
| Liquidity / DSCR coverage | High | Cash on hand vs short-term maturities each quarter; next Schedule III DSCR print; lender covenant definition if ever disclosed | Near-term, next 1-2 quarters if grain ramp-up or receivable collection slips |
| Government-scheme dependency for profitability | High | Interest-subvention scheme renewal (5-year DFPD/NABARD window from 1-Apr-2023, lapses FY2028); PLI claim realisation in cash | Medium-term, window lapse around FY2028; nearer-term on any policy change |
| Subsidiary (TGPL) hidden capex and guarantee exposure | Medium | TGPL capex drawdown and NABARD facility utilisation; corporate-guarantee crystallisation; Sumitomo JV site commissioning | 12-24 months as the five CBG sites commission |
| Governance / KMP continuity | Medium | New CS/CFO tenure stability, SEBI LODR compliance record at next filings | Ongoing, testable at next AGM and compliance filings |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Why did related-party raw-material purchases from the Nirani group
   exceed 100% of disclosed total purchases in FY25, and what reconciles
   the RPT note (Note 38) against the total-purchases note (Note 28)?
2. Why was no contingent liability recorded for the corporate guarantee
   given for TruAlt Gas Pvt Ltd's NABARD facility (Note 8), and what is
   the guarantee amount?
3. What is the lender-defined DSCR calculation and covenant threshold, and
   does the Schedule III-calculated 0.99x FY26 DSCR sit inside or outside
   it?
4. What is driving the shift in trade receivables into the "under 6 months
   overdue" bucket (57.6% of book) against a stated 7-27/21-27 day credit
   term, and is it OMC payment-cycle behaviour or company-side billing
   timing?
5. What is the nature and purpose of the ₹40.3cr advance to Accutrade
   Global LLP, the ₹15.08cr "expenses towards secondary sale of shares"
   paid to Nirani Holdings in FY25, and the reimbursement-of-expenses RPT
   line that grew 172% in FY26?

### E. NOTES-BASED RED FLAGS

- PLI revenue recognised ahead of formal claim filing (judgement-based
  accrual, Note 27/26).
- Government-scheme income (interest subvention + PLI) is 73.2% of
  standalone PBT, masking the scale of core operating profitability (Note
  27/28).
- Related-party raw-material purchases exceed disclosed total purchases in
  FY25, unreconciled across two notes in the same filing (Note 28/38).
- Corporate guarantee for a subsidiary's borrowing omitted from the
  contingent liabilities note, contradicted twice more within the same
  standalone notes (Note 8, 57, 38(D)(4)).
- DSCR fell below 1.0x with no management explanation, despite exceeding
  the company's own 25% variance-disclosure trigger (Note 52).
- Net debt increased despite a ₹750cr gross equity raise; the gearing
  improvement is a dilution effect, not deleveraging (Note 53).
- Consolidated capital commitments are ~20x the standalone figure, hiding
  a ~₹155.8cr subsidiary capex programme from a standalone-only read (Note
  56).
- Short-term financial obligations are 8-15x cash on hand per the
  company's own liquidity risk table (Note 42(D)/41(D)).
- Two ~14-week Company Secretary vacancies spanning the IPO window, plus a
  ~6-week CFO vacancy (Note 39/38, KMP tenure dates).
- Unexplained "Miscellaneous income" ~8-10x jump and a volatile,
  unitemised "provision written back" revenue line recurring in both years
  (Note 27/28).

### F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices. Key concern: government-scheme
income and related-party feedstock purchases together obscure how much of
FY26 profitability and input cost is genuinely arm's-length and
operating-driven, compounded by a three-way internal contradiction on a
subsidiary guarantee and a sub-1x DSCR left unexplained. Key strength: the
multi-feed conversion capex is precisely quantified, dated, and traceable
to specific borrowing costs, and the one clean confirmatory finding in the
corpus (the 96.4% standalone capital-commitment collapse) matches the
capex-completion narrative exactly. Overall accounting quality: 4/10.

### COMPANY MEMORY CROSS-CHECK

- Load-bearing fact 1 (utilisation/grain economics vs guidance): the notes
  do not carry quarterly utilisation figures (that data lives in concalls
  and results, outside this stage's scope); the notes CONFIRM the physical
  capex is real and dated (three units, ₹849.03 + ₹883.80 lakh + a third
  IPO-funded unit, specific borrowing costs, Note 5) but leave the
  margin-compression claim (Rs 15-16 to Rs 6-7/litre) untested here — that
  evidence sits in the concalls, not the notes.
- Load-bearing fact 2 (cash conversion / IPO money): CONFIRMED and
  materially deepened. FY26 CFO of exactly ₹(296.15)cr standalone matches
  company memory to the rupee; the ₹425cr working-capital tranche was
  fully utilised per the IPO table but the notes show it was absorbed by
  operating cash burn and inventory build, not retained as a cushion; net
  debt actually rose despite the IPO.
- Load-bearing fact 3 (Nirani-group feedstock RPT, Unit 5 sale, pledge):
  CONFIRMED and deepened. RPT feedstock dependency, the corporate
  guarantee/contingent-liability contradiction, and the asset-pledge
  pattern are all now quantified. Unit 5 (Badami) sale to Onkar Agro
  Sugars & Energy (04-Aug-2026) correctly does NOT appear in this AR — it
  postdates the 22-May-2026 board-approval date, as company memory itself
  anticipated.
- Load-bearing fact 4 (governance churn): PARTIALLY CONFIRMED, PARTIALLY
  OPEN. The notes independently surface a governance-continuity finding
  company memory did not specifically name (the two ~14-week CS vacancies
  and the CFO vacancy). The Aug-2026 chairman change, director cessation,
  exchange fines, and GST demand order are outside this AR's window
  (signed 22-May-2026) and remain open items for later stages / live
  verification, not contradicted by anything in the notes.

---

```yaml
stage: B02-notes
company: "TRUALT"
run_date: "2026-09-18"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "FY26 standalone CFO -Rs 296.15cr, net debt rose despite Rs 750cr IPO, short-term financial obligations 8-15x cash on hand, DSCR fell to 0.99x, receivables short-cycle ageing deteriorated"}
  - {type: FLAG-RPT, reason: "Related-party feedstock purchases 72.6% of FY26 total purchases and exceed 100% of FY25 total purchases (unreconciled); related-party trade payables funded 63.9-73.5% of total payables; corporate guarantee for subsidiary contradicts NIL contingent liability note"}
  - {type: FLAG-EARNINGS-QUALITY, reason: "Government-scheme income (interest subvention plus PLI) is 73.2% of standalone PBT FY26; PLI revenue booked ahead of formal claim filing"}
  - {type: FLAG-GOVERNANCE, reason: "Two ~14-week Company Secretary vacancies spanning the IPO listing window plus a ~6-week CFO vacancy, per KMP tenure dates in the related-party note"}
accounting_quality: 4
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Government-scheme income (interest subvention plus PLI) is 73.2% of standalone PBT FY26 (Rs 8,018.19 lakh of Rs 10,947.48 lakh)", note_ref: "Note 27/28, both sets", rating: "red", why: "Core operating profitability is a minority of reported PBT; both schemes are policy-contingent and time-bound with no discontinuation sensitivity disclosed"}
  - {rank: 2, finding: "Related-party feedstock purchases from the Nirani group are 72.6% of total raw-material purchases FY26 and exceed 100% of disclosed total purchases FY25", note_ref: "Notes 28 and 38 standalone; 29 and 39 consolidated", rating: "red", why: "Single-counterparty-group dependency for the core input, with an unreconciled arithmetic gap between two notes in the same filing"}
  - {rank: 3, finding: "Net debt rose (standalone +10.7%, consolidated +11.3%) despite a Rs 750cr gross IPO; gearing improved only because the equity denominator grew", note_ref: "Note 53, both sets", rating: "red", why: "The deleveraging narrative implied by the IPO did not happen; equity dilution, not debt reduction, drove the ratio"}
  - {rank: 4, finding: "Short-term contractual financial obligations (Rs 750.4cr consolidated) are 8-15x cash on hand (Rs 88.3cr consolidated / Rs 48.1cr standalone)", note_ref: "Note 42(D)/41(D), both sets", rating: "red", why: "Company-disclosed hard evidence of rollover dependency on short-term debt and receivable or grant collection, not a cash cushion"}
  - {rank: 5, finding: "DSCR fell to 0.99x (FY26) from 1.28x (FY25), the company's own mandatory ratio, with no explanation given", note_ref: "Note 52 standalone, p.355", rating: "red", why: "Net operating income did not fully cover debt service in the year; the covenant threshold is undisclosed so breach cannot be ruled in or out"}
  - {rank: 6, finding: "Standalone inventory grew 155.6% (Rs 204.2cr to Rs 521.8cr) while revenue fell 9.3%; finished goods alone grew 136.2% with no write-down or composition narrative", note_ref: "Note 11 standalone", rating: "red", why: "Inventory build sharply outpaced and diverged from revenue direction with no management explanation of composition"}
  - {rank: 7, finding: "Corporate guarantee for TGPL's NABARD loan contradicts the NIL contingent liability note and the no-guarantees RPT statement", note_ref: "Notes 8, 57, 38(D)(4)/39(D)(4)", rating: "red", why: "Three-way internal inconsistency within the same standalone financial statements on a contingent liability disclosure"}
  - {rank: 8, finding: "Related-party trade payables funded 63.9% (FY26) and 73.5% (FY25) of total payables; FY25 working capital was negative Rs 183.1cr, turning positive only after the IPO", note_ref: "Notes 24, 38, 52", rating: "red", why: "Pre-IPO working capital was structurally financed by promoter-family trade credit"}
  - {rank: 9, finding: "Consolidated capital commitments (Rs 163.7cr) are about 20x the standalone figure (Rs 7.9cr); TGPL carries an estimated Rs 155.8cr forward CBG capex invisible in a standalone-only read", note_ref: "Note 56, consolidated vs standalone", rating: "red", why: "Corrects a capex-winding-down reading built from the standalone note only; a large new capital programme is ramping up inside the subsidiary"}
  - {rank: 10, finding: "Two separate ~14-week Company Secretary vacancies (immediately pre- and post-IPO listing) plus a ~6-week CFO vacancy (Jan-Feb 2025)", note_ref: "Note 39/38, KMP tenure dates, both sets", rating: "red", why: "Governance-continuity gap at the two most SEBI LODR compliance-sensitive moments in the company's listed history"}
  - {rank: 11, finding: "Trade receivables not-due share collapsed 69.1% to 34.7%, overdue-under-6-months jumped 20.2% to 57.6%, against a 7-27 or 21-27 day stated credit term; turnover fell 21%", note_ref: "Note 12, Note 42(C)/41(C), Note 52", rating: "yellow", why: "Short-cycle receivables are running several multiples of the stated credit term past due, though the long tail beyond 6 months actually improved slightly"}
  - {rank: 12, finding: "FY26 standalone CFO was -Rs 296.15cr; the Rs 425cr IPO working-capital tranche was fully utilised per the utilisation table but absorbed by cash burn and inventory build, not retained as liquidity", note_ref: "Notes 18, 19, 60/61, cash flow statement", rating: "yellow", why: "IPO proceeds functioned as a cash-burn backstop rather than a war chest; net cash actually received was Rs 665.71cr, below the Rs 750cr headline"}
  - {rank: 13, finding: "PLI revenue booked ahead of formal claim filing; total government-scheme receivables grew 31.7% to Rs 129.5cr even as revenue fell 9.4%", note_ref: "Notes 15/16, 26/27", rating: "yellow", why: "Judgement-based accrual of government income ahead of realisation, with the receivable growing even as current-year recognised income shrank"}
  - {rank: 14, finding: "Nirani Holdings sold TGPL shares to Sumitomo Corporation at Rs 30.90/share, a 29% premium to the Company's own Rs 24/share entry price 8 months earlier, no pricing rationale disclosed, named only in consolidated notes", note_ref: "Note 36 standalone / Note 59 consolidated", rating: "yellow", why: "A related-party entity captured a pricing uplift the Company itself did not, on a subsidiary the Company controls"}
  - {rank: 15, finding: "NIL or full-compliance assertions recur at least three times against harder numbers disclosed elsewhere in the same note set (guarantee versus NIL contingent liabilities, covenant compliance versus 0.99x DSCR, credit terms differing between note sets)", note_ref: "Notes 57 vs 8/39(D)(4); Note 53 vs Note 52; Note 42(C) consolidated vs standalone", rating: "yellow", why: "A recurring disclosure-consistency weakness across the standalone and consolidated note sets, not three isolated slips"}
red_flags:
  - "PLI revenue recognised ahead of formal claim filing (judgement-based accrual, Note 27/26)"
  - "Government-scheme income (interest subvention plus PLI) is 73.2% of standalone PBT, masking the scale of core operating profitability (Note 27/28)"
  - "Related-party raw-material purchases exceed disclosed total purchases in FY25, unreconciled across two notes in the same filing (Note 28/38)"
  - "Corporate guarantee for a subsidiary's borrowing omitted from the contingent liabilities note, contradicted twice more within the same standalone notes (Note 8, 57, 38(D)(4))"
  - "DSCR fell below 1.0x with no management explanation despite exceeding the company's own 25% variance-disclosure trigger (Note 52)"
  - "Net debt increased despite a Rs 750cr gross equity raise; the gearing improvement is a dilution effect, not deleveraging (Note 53)"
  - "Consolidated capital commitments are about 20x the standalone figure, hiding a Rs 155.8cr subsidiary capex programme from a standalone-only read (Note 56)"
  - "Short-term financial obligations are 8-15x cash on hand per the company's own liquidity risk table (Note 42(D)/41(D))"
  - "Two ~14-week Company Secretary vacancies spanning the IPO window, plus a ~6-week CFO vacancy (Note 39/38, KMP tenure dates)"
  - "Unexplained Miscellaneous income ~8-10x jump and a volatile, unitemised provision-written-back revenue line recurring in both years (Note 27/28)"
questions_for_mgmt:
  - "Why did related-party raw-material purchases from the Nirani group exceed 100% of disclosed total purchases in FY25, and what reconciles Note 38 against Note 28?"
  - "Why was no contingent liability recorded for the corporate guarantee given for TruAlt Gas Pvt Ltd's NABARD facility (Note 8), and what is the guarantee amount?"
  - "What is the lender-defined DSCR calculation and covenant threshold, and does the Schedule III-calculated 0.99x FY26 DSCR sit inside or outside it?"
  - "What is driving the shift of trade receivables into the under-6-months-overdue bucket (57.6% of book) against a stated 7-27/21-27 day credit term?"
  - "What is the nature and purpose of the Rs 40.3cr advance to Accutrade Global LLP, the Rs 15.08cr secondary-sale-of-shares expense paid to Nirani Holdings in FY25, and the reimbursement-of-expenses RPT line that grew 172% in FY26?"
receivables_trend: "deteriorating (short-cycle): not-due share fell from 69.1% to 34.7% of book FY25 to FY26 while under-6-months-overdue rose from 20.2% to 57.6%; receivables turnover fell from 5.68x to 4.51x (-21%, Note 52 standalone); the long tail beyond 6 months improved slightly, from 10.6% to 7.7% of book (Note 12 standalone)"
restatements_found: []
going_concern_language: "NONE"
analyst_note: "The single highest-value read of this stage is that TRUALT's reported FY26 profitability and cash position are both substantially propped up: 73.2% of standalone PBT traces to two government schemes rather than core ethanol economics, and the Rs 750cr IPO raise coincided with a rise, not a fall, in net debt because the working-capital tranche was consumed by cash burn and inventory build. Layered on top is a related-party feedstock dependency that the company's own notes cannot arithmetically reconcile in FY25, and a corporate guarantee the company itself discloses in one note while denying in two others. None of this is evidence of fraud on its own; each item has a plausible benign explanation (OMC customer base, ethanol-price administration, first-year listed-company disclosure growing pains). But the volume and clustering of unresolved contradictions, all concentrated in the RPT and cash-conversion areas that matter most for a transition-alpha thesis, argues for treating every subsequent stage's use of FY26 margin, cash conversion, and RPT-adjusted revenue with active scepticism until claude.ai live verification closes the gaps named in the five questions above."
```
