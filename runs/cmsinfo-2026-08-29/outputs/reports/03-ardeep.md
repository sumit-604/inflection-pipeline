# CMS Info Systems Ltd (CMSINFO) — Stage 3: Annual Report Deep Dive, Backward Read
Run: cmsinfo-2026-08-29 | Source: FY2025-26 Annual Report (PDF/txt file misnamed Annual_Report_2023, confirmed FY26 AR at p.2/147: "Annual Report 2025-26"). Page anchors use the extraction marker `p.N/147`. SA = Standalone, CON = Consolidated. ₹ figures in millions unless stated. Builds on Stage 2 (B02-notes); does not re-derive the notes triple-pass, extends and cross-references it.

> **CORRECTION 2026-08-30 (operator, per web-handover-dossier S2):**
> This report assigned the -7.8% FY26 decline to ATM Management Solutions.
> That is WRONG. Verified by 220-DPI rasterized read of FY26 AR p.52 and by
> the Board's Report (p.31/147) naming each figure to each platform:
> ```
>   ATM Management Solutions              12,840 -> 13,515  = +5.3%
>   Retail Solutions & Currency Logistics  6,368 ->  5,872  = -7.8%
>   Technology & Payment Solutions         2,633 ->  3,735  = +42%
> ```
> The tables on p.52 are correctly placed under their headings; an earlier
> transposition hypothesis was tested and withdrawn. The error originated in
> column-collapse in the extracted text. `04-bizmodel.yaml` and
> `business-narrative.md` carried the correct reading. VERIFIER GAP: two blocks
> in the same run contradicted each other on this point and no verifier caught it.
> Any statement below that assigns the -7.8% to ATM Management is superseded by this block.

Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A Core opinion
SA and CON: **unmodified (clean) opinion**, both signed 14-May-2026 by B S R & Co. LLP (Sreeja Marar, Partner, Membership 111410) (Auditor's Report SA p.71/147; CON p.104/147). No going-concern qualification or Emphasis of Matter language anywhere in either opinion (confirmed by direct search; B02's "NONE" finding for going-concern is verified). Standard going-concern assessment paragraphs only (Note 52, SA p.104/147; Note "no significant subsequent events," CON p.136/147, though see 1F/2H below on the scope of that statement).

### 1B Key Audit Matters
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition (SA: Note 2(h),19,41; CON: Note 2(i),18,40) | "Overstatement of revenue is considered as a significant audit risk... fraud risk around existence of unbilled revenue at period end... fraud risk around existence of revenue recognized throughout the year including at year end for pre-mature revenue recognition" (Auditor's Report SA p.71/147, CON p.104-105/147) | Design/effectiveness testing of revenue controls; statistical sampling of revenue transactions against customer confirmations/proof of delivery; sample testing of unbilled transactions for subsequent invoicing; journal-entry testing for unusual/irregular revenue entries | 🟡 Watch — single KAM, standard procedures applied, no exception noted by auditor, but unbilled revenue (contract asset) is growing faster than billed revenue (+8.9% SA/+12.3% CON vs total revenue +2.2%/+2.6%) per B02's accounting-quality table, which is exactly the pattern this KAM exists to police |

Only one KAM in both SA and CON reports — no separate impairment or fair-value KAM despite the receivables-provisioning pattern (Phase 2/B02 Pattern 1); the auditor evidently did not consider loss-allowance adequacy a KAM this year, which is itself worth weighing against the 14.1% SA release finding below.

### 1C Emphasis of Matter and Other Matters
No Emphasis of Matter paragraph found in either report (explicit search). **Other Matters**:
- CON: reliance on other auditors for **8 subsidiaries** — total assets (pre-consolidation) ₹4,576.02m, revenue ₹4,491.32m, net cash inflow ₹75.96m (CON Auditor's Report, Other Matters (a), p.105/147). CON ICFR opinion (Annexure B) separately notes reliance on other auditors' ICFR work for **6** Indian subsidiary companies (p.108/147). Opinion "not modified" in respect of this reliance.
- Both SA and CON: a **scope-limited "Other Matters" carve-out on Rule 11(g) audit trail** (see 1D below) — this is technically an Other Matters paragraph even though framed inside the Section 143(3)(3)(i)/Rule 11 reporting, not the audit opinion itself.

### 1D CARO 2020 clause-by-clause (SA Annexure A, p.73-75/147; CON Annexure A, p.107/147)
| Clause | Finding | Rating |
|---|---|---|
| (i) PPE/intangibles | Proper records maintained; phased 3-year physical verification programme, no material discrepancies; no immovable property (lessee only); no revaluation; no benami proceedings | 🟢 |
| (ii) Inventory | Physically verified, no discrepancies >10% of any class; working capital limits >₹5cr secured on current assets, quarterly returns agree with books | 🟢 |
| (iii) Loans to related parties, repayment reality | Loans to subsidiary (Securens) ₹58.5m advanced/₹45.28m outstanding, repaid on demand, no schedule stipulated. **Loans to "Others-Company" ₹570m advanced/₹580.12m outstanding** — this is the distressed-receivable-to-loan conversion (Note 7(b), p.88/147): "Loans given to one of the customer by converting part of accounts receivable into loan amounting to ₹580.12 million... for working capital requirement, which will be repaid over 3 years and secured by a charge against specific property, plant and equipment of the customer." Note 48 (Section 186 disclosure, p.103/147) **names the counterparty: Transaction Solutions International (India) Private Limited** — confirms and fully anchors B02 Rank 7 (search initially missed the name because the two-column PDF layout splits it across lines; it is present verbatim in Note 48). No overdue >90 days on this loan as of year-end (i.e., the 3-year schedule is being honoured to date, but this is Year 1) | 🟡 Watch |
| (iv) Sec 185/186 compliance | Complied | 🟢 |
| (v) Deposits | None; NA | 🟢 |
| (vi) Cost records | NA (manufacturing segment nascent) | 🟢 |
| (vii) Disputed statutory dues by tax type/forum | No undisputed dues >6 months overdue. Disputed dues table (p.74/147): Customs Duty ₹44.29m+0.85m+2.75m+0.69m (CESTAT Chennai/Mumbai, Addl. Commissioner Customs), Central Sales Tax ₹0.26m, Excise Duty ₹69.03m (CESTAT Chennai), assorted state GST disputes (MP, Jharkhand, Telangana, UP, AP, Bihar, Chandigarh — individually small, ₹0.01m-₹7.03m), Bihar VAT ₹25.73m, Uttarakhand VAT ₹1.72m, Orissa VAT ₹1.86m. Auditor also notes "slight delays in a few cases of professional tax and Labour Welfare Fund" deposits (undisputed, immaterial) | 🟡 Watch (routine litigation profile, not escalating; noted for completeness per protocol instruction) |
| (viii) Undisclosed income | None | 🟢 |
| (ix) Borrowing defaults | No loans/borrowings from any lender during the year — clause NA. Not a wilful defaulter. No term loans. No short-to-long-term diversion. No funds taken to meet subsidiary obligations. No loans raised on pledge of subsidiary securities | 🟢 (company is functionally lender-debt-free at SA level; matches MD&A "debt-free for over a decade" claim, CEO letter p.5/147) |
| (x) IPO/preferential allotment | NA, none during year | 🟢 |
| **(xi) Fraud** | **(a)** 25 instances of cash embezzlement by contractors/employees, ₹125.35m total (FY25: ₹217.22m). Complaints filed with police, insurance claims filed. **Recovered ₹9.98m; ₹12.70m written off as doubtful of recovery** (~₹102.67m still pending resolution/insurance claim as of report date — arithmetic: 125.35 − 9.98 − 12.70). **(b)** Report filed by auditor in **Form ADT-4 under Section 143(12)** with the Central Government — statutory fraud reporting, confirmed (SA Annexure A p.75/147). **(c)** No whistleblower complaints received during the year (management representation) | 🔴 Red Flag — a hard flag per protocol (clause xi is fraud reporting); CON CARO Annexure A confirms the Holding Company itself carries unfavourable remarks under **xi(a) and xi(b)** (CON Annexure A "unfavourable remarks" table, p.107/147) |
| (xii) Nidhi Company | NA | 🟢 |
| (xiii) RPT compliance | Compliant with Sections 177/188 | 🟢 |
| (xiv) Internal audit | System commensurate with size; internal audit reports considered | 🟢 |
| (xv) Non-cash transactions with directors | None | 🟢 |
| (xvi) RBI registration | NA on all four sub-clauses (not NBFC, not CIC, not part of RBI-defined group) | 🟢 |
| **(xvii) Cash losses** | Company (SA): has **not** incurred cash losses in current or immediately preceding year. **CON CARO Annexure A separately flags Securens Systems Private Limited with an unfavourable remark under clause xvii** (cash losses in its stub-period first year under the Group) — matches B02 Finding 13 exactly | 🟡 Watch (subsidiary-level, not parent-level) |
| (xviii) Auditor resignation | None; NA | 🟢 |
| (xix) Going concern / liability discharge | Nothing came to auditor's attention suggesting inability to meet liabilities falling due within one year; explicit disclaimer this is not future-viability assurance | 🟢 |
| (xx) Unspent CSR | (a) No unspent amount under s.135(5) other than ongoing projects — NA. (b) Unspent amount for ongoing projects (₹3.65m; ₹2,712,149 net per Board's Report CSR annexure, p.34/147) transferred to Special Account within 30 days, compliant | 🟢 |

**Also material — internal financial controls scope limitation (both SA and CON, Annexure B, and the Rule 11(g) paragraph, p.72-73/147, p.106-107/147):** the ICFR opinions themselves are **unmodified** ("adequate internal financial controls...operating effectively"), but a specific Rule 11(g) audit-trail carve-out sits underneath that headline opinion: (i) audit trail was **not enabled** for one accounting software used for preparing billing information; (ii) for the general-ledger software post-migration (1-Sep-2025), the auditor is **"unable to comment"** whether the audit-trail feature was enabled/operated throughout the year or tampered with, "in the absence of an independent auditor's report in relation to controls at a service organization" (i.e., no SOC-type report exists for the third-party GL software vendor). Where audit trail was enabled and tested elsewhere, no tampering was found, and prior-year audit trails were preserved. **This is a genuine limitation, not a formal ICFR qualification** — worth stating precisely: the overall ICFR opinion is clean; the audit-trail evidence for the billing system and the migrated GL system is the specific gap. It lands in the same year as the receivables deterioration (Phase 2) and the live GL migration, which is the reason B02 rated it 🔴.

### 1E Auditor continuity
B S R & Co. LLP (Firm's Registration No. 101248W/W-100022) **re-appointed for a further 5-year term, from the conclusion of the 16th AGM to the conclusion of the 21st AGM (2028)** (Board's Report p.34/147). "Further term" language confirms the firm was already the incumbent auditor before this reappointment; the exact original appointment year is **NOT FOUND** in this AR (predates the FY26 disclosure window). Fees: Statutory audit fees ₹14.34m + out-of-pocket ₹1.91m = **₹16.24m total** (consolidated basis, Board's Report p.34/147, Annexure A). No separate non-audit fee line is disclosed in this table — **no non-audit-fee-exceeds-audit-fee condition observable** from the disclosed figures (protocol flag does not trigger). Secretarial Auditor: M/s. Siroya and BA Associates, 5-year term from FY26. Internal Auditor: Grant Thornton Bharat LLP (MD&A p.51/147, Risk Management section); ICFR additionally tested by Baker Tilly DHC Advisory LLP.

### 1F Standalone vs consolidated differences
Both reports carry the same single KAM (revenue recognition) and are both unmodified. The material *difference* is not in the opinion but in the CARO annexure: **only the CON CARO Annexure A carries the xxi "unfavourable remarks" cross-reference table**, which is where Securens' clause (xvii) cash-loss qualification and the Holding Company's own xi(a)/xi(b) fraud-clause flags are consolidated into one place (p.107/147) — a reader relying on the SA CARO alone would see the fraud clauses but not the Securens cash-loss cross-reference, since Securens is not audited by B S R & Co. as a standalone entity in a way that surfaces there. Six Indian subsidiaries' ICFR work and 8 subsidiaries' financial-statement work overall rest on other auditors' reports (1C above) — reliance is disclosed and not qualified.

**Phase 1 summary:** Clean unmodified opinions on both bases with one standard revenue-recognition KAM, but the CARO annexures carry real substance: a statutory fraud filing (ADT-4, s.143(12)) for the third consecutive year per company memory, a genuine (if scoped) audit-trail evidence gap on billing and GL systems, and a subsidiary-level cash-loss qualification (Securens) layered onto an otherwise unremarkable compliance profile (no borrowing defaults, no wilful-defaulter status, clean statutory-dues history bar routine appeals).

**Phase 1 verdict: 🟡 Watch**, driven to the edge of 🔴 by the fraud clause. Kill-switch assessment (informational): a human reviewer would have reason to pause on the ADT-4 fraud filing and the audit-trail scope limitation landing in the same year as a GL migration and receivables deterioration, but neither is a going-concern or opinion-qualifying matter. **Continuing to Phase 2.**

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction: the Top 15 triple-pass findings are **verified against source**, not re-derived. Extension work below covers what the triple-pass was thinner on for Phase 2's specific purposes (2A aggressiveness, 2C contingent-liability ratios, 2F borrowings/debt-wall, plus one material scope clarification on Rank 3).

### Triple-pass verification (Top 15)
| Rank | B02 finding | AR value found | Verdict |
|---|---|---|---|
| 1 | SA loss allowance ₹533.94m→₹458.80m (-14.1%); SA 1-2yr overdue ₹92.14m→₹1,490.59m (16.2x) | Note 12, SA p.89/147: Total trade receivable ₹7,888.26m→₹8,452.56m; Loss allowance ₹(533.94)→₹(458.80); net receivables ₹7,354.32m→₹7,993.76m (+8.7% vs revenue +2.2%). Exact match | ✓ Verified |
| 2 | 1-2yr overdue bucket 8.5x CON / 16.2x SA | CON Note 37 ageing table, p.131/147: 1-2yr bucket ₹177.94m(FY25)→₹1,516.32m(FY26) = 8.52x. Exact match | ✓ Verified |
| 3 | Cash Management services revenue -4.5% SA/-6.6% CON | Note 19 CON, p.124/147: "Cash Management services" **within Sale of services** ₹14,670.91m→₹13,701.18m = -6.61%. Exact match. **Extension/clarification (new, not in B02):** Note 38 segment revenue for the "Cash Management services" *segment* (gross, before inter-segment elimination) is ₹15,951.78m(FY25)→₹15,965.18m(FY26), i.e. roughly **flat (+0.08%)**, not declining. Reconciling: FY26 inter-segment sales elimination is ₹2,264.00m and FY25's is ₹1,280.87m; 15,965.18−2,264.00=13,701.18 (exact match to Note 19 FY26) and 15,951.78−1,280.87=14,670.91 (exact match to Note 19 FY25). **This means the elimination — i.e., intra-group/related-party billing routed through the Cash Management segment — grew 76.7% YoY (₹1,280.87m→₹2,264.00m) while external service revenue in the same segment fell 6.6%.** The segment's total (gross) footprint held up only because intra-group billing filled the gap; external revenue recognized to outside customers is the -6.6% figure. This sharpens, rather than contradicts, B02's finding, and is a good management question in its own right (Note 38/19, CON p.124/147, p.133/147) | ✓ Verified, extended |
| 4 | Cash Management segment result -25.0% (₹4,013.79m→₹3,012.14m) | Note 38, CON p.133/147: exact match (3,012.14/4,013.79−1 = −24.95%) | ✓ Verified |
| 5 | Cash embezzlement 25 instances ₹125.35m, ADT-4 filed | CARO Annexure A xi(a)/(b), SA p.75/147; Board's Report "Reporting of Frauds," p.34/147. Exact match, plus new detail: recovered ₹9.98m, written off ₹12.70m | ✓ Verified, extended |
| 6 | Audit trail limitation | Rule 11(g) paragraph, SA p.72-73/147, CON p.106-107/147. Confirmed as an ICFR **Other Matters scope limitation**, not a qualification of the ICFR opinion itself (see 1D) | ✓ Verified, clarified |
| 7 | Receivable→loan conversion, Transaction Solutions International (India) Pvt Ltd, ₹580.12m | Note 7(b), SA p.88/147 (amount, mechanism, 3-year term, PP&E security) + Note 48, SA p.103/147 (counterparty name, Section 186 table) | ✓ Verified |
| 8 | ₹550m FSS balance absent from Note 31(b), capital-commitments shows ₹0 | Note 31(b), SA p.96/147: "Nil Capital commitment for the year ended March 31, 2026 (March 31, 2025 ₹93.63)." Note 10, SA p.89/147: FSS agreement ₹1,150m total, ₹600m paid 30-Mar-2026, ₹550m balance on completion. Exact match. **Context note (new):** the FSS deal itself is prominently and specifically narrated in MD&A (Board's Report point 4, p.51/147: "₹115 Cr... binding agreement signed, with closure expected in H1 FY27... expected to contribute approximately 4% to FY27 services revenue") and in the CEO letter. The gap is confined to the technical capital-commitments *note*, not a narrative concealment of the transaction | ✓ Verified, contextualised |
| 9 | Cash and cash equivalents nearly halved | Cash Flow Statement, SA p.78/147: ₹2,166.19m→₹904.26m (-58.3%). CON p.109-110/147: ₹2,308.52m→₹1,122.55m (-51.4%). Exact match | ✓ Verified |
| 10 | Dividend +39.2%, buyback ₹340/share underwater | SOCE Note, SA p.79/147: ₹1,063.16m→₹1,479.58m (+39.2%). Board's Report p.31/147: buyback ₹340/share, ₹1,679.30m aggregate. CEO letter (p.5/147) independently states "~₹168 Cr for the buyback," consistent (₹1,679.30m = ₹167.93 Cr) | ✓ Verified |
| 11 | ATM useful life extension, +₹47.65m | Note 4 reference confirmed in B02; not independently re-verified against Note 4 text this pass beyond cross-reference to the ₹47.65m figure carried consistently | ✓ Verified (by consistency; Note 4 full text not re-quoted this pass) |
| 12 | ESOP cost -87.3% CON, CEO exercise driven | Note 39, CON p.134/147: Group recognized ₹38.95m (FY26) vs ₹307.45m (FY25) as ESOP expense — exact match (-87.3%). CEO's cash comp (excl. ESOP) also fell -35.9% YoY per remuneration-ratio table (Board's Report Annexure 2, p.38/147) | ✓ Verified |
| 13 | Quality Logistics negative net worth ₹-52.09m; CMS Securitas net loss ₹-6.31m; Securens CARO cash-loss | Note 40 Schedule III, CON p.134/147: Quality Logistics net worth ₹(52.09)m exact match; CMS Securitas Limited net worth ₹31.03m **(positive, not negative — B02 correctly described this as "net loss," not negative net worth; confirmed precise)**, share in profit ₹(6.31)m exact match; Securens net worth ₹694.82m, share in profit ₹(6.99)m (loss, stub period) — all consistent with B02 | ✓ Verified |
| 14 | ATM cash-shortage provision reclassification ₹577.49m (FY25 comparatives) | CON Note 37, p.131/147: "During the year, Group has presented provision for ATM cash shortage and claim instead of loss allowance..." Movement table shows FY25 "Less: Transfer to cash loss provision considered separately (662.80)" at CON level (differs from B02's SA-anchored ₹577.49m figure, which is a different, SA-scoped number — both are internally consistent within their own basis, SA vs CON). **Extension (new): CON loss allowance actually ROSE FY25→FY26, ₹766.82m→₹825.71m (+7.7%)**, the opposite direction of the SA-only 14.1% release. The "release" in Rank 1 is a standalone-book phenomenon; the consolidated book (which absorbs Securens' opening ECL of ₹74.55m and other subsidiary provisioning) shows a net increase. This distinction should be read precisely: it does not overturn Rank 1 (SA figures are exact and the SA book is where the receivables deterioration concentrates), but a reader must not generalise the "release" to the Group level | ✓ Verified, materially clarified |
| 15 | Lessor lease receivables +117.6% to ₹8,126.31m | Not independently re-verified against Note 29 text this pass; carried forward from B02 on consistency | ✓ Verified (by consistency) |

**13 of 15 fully independently re-verified against primary source this pass; 2 carried on consistency.** Zero true discrepancies found; one finding (Rank 3) required a scope clarification that sharpens rather than weakens the original read; one finding (Rank 14) required a CON-vs-SA distinction that narrows the claim precisely.

### 2A Accounting policy aggressiveness
- **Revenue recognition:** standard Ind AS 115 practical-expedient disclosures (no remaining-performance-obligation disclosure for ≤1yr contracts) — routine, not aggressive (Note 41 CON, p.134/147).
- **Depreciation lives:** the ATM useful-life extension (7→10 years, +₹47.65m favourable, wef 1-Jan-2026) is the one policy change quantified this year, and it lands in the weakest-earnings year on record — a genuine, if modest, earnings-quality flag (B02 Finding 11, unchanged).
- **Capitalisation:** no borrowing-cost capitalisation flags found; capitalisation threshold itself is undisclosed (a minor transparency gap, not a red flag).
- **Impairment/ECL:** qualitative ECL policy only, no ageing-bucket % disclosed in the accounting policy note itself (the ageing table in Note 12/37 is a Schedule III mandated disclosure, separate from the policy note) — this is the disclosure gap that makes Rank 1/14 hard to interrogate further from the AR alone.
- **Ind AS 116 (leases):** no rate or policy change flagged.
- **Net verdict: 5/10** on capitalisation honesty and provisioning adequacy, consistent with B02's per-dimension scoring; no evidence of aggressive revenue-recognition mechanics.

### 2B RPT map, extended
Intra-group "Service charges" (holding company billing/being billed by subsidiaries, Note 30, SA p.86/147): CMS Marshall Limited ₹1,220.89m→₹1,523.22m (+24.8%); Securitrans India Pvt Ltd ₹201.50m→₹404.03m (**+100.5%**, unexplained divergence flagged by B02, unresolved this pass); CMS Securitas Limited ₹273.59m→₹294.20m (+7.5%); Hemabh Technology ₹166.99m→₹126.66m (-24.2%). Sum of major service-charge RPTs ≈ ₹2,439.35m against SA revenue ₹22,721.92m = **10.7% of revenue** — material in scale but structural (holdco-subsidiary cross-billing for the entities that jointly deliver Cash Management services, not third-party value extraction; no promoter exists to extract to). Corporate guarantees to Securitrans lenders ₹600m + customer vaulting facility ₹200m = ₹800m contingent exposure (Note 31(a), SA p.96/147). No related-party loans on non-commercial terms found; Board's Report affirms "no materially significant related party transaction" during the year and all RPTs at arm's length (Board's Report p.48/147).

### 2C Contingent liabilities, ratios
SA (Note 31(a), p.96/147): total ₹959.82m (FY26) vs ₹1,069.87m (FY25), down. Components: disputed Customs ₹48.57m, VAT ₹29.31m, Excise ₹69.03m, CST ₹0.26m, GST ₹12.65m, disputed Income Tax **₹0 (down from ₹118.33m — resolved/settled this year)**, plus corporate guarantees ₹800m (83% of the total; intra-group, to a subsidiary's lenders, not third-party litigation risk).
- **% of net worth (SA equity ₹23,122.55m): 4.15%** — well below the 25% flag.
- **% of PAT (SA ₹2,846.72m): 33.7%** — **crosses the >25%-of-PAT threshold**, though well below 100%. Driven almost entirely by the guarantee, not litigation exposure. **Flagged per protocol threshold but assessed as low-severity given the guarantee's intra-group, secured nature.**

### 2D Receivables (extends B02)
SA ageing (Note 37, p.99/147) confirms: DSO 116 days (FY24, FY25) → 126 days (FY26) per MD&A Key Ratios table (p.52/147) — an independent MD&A-sourced confirmation of the notes-level deterioration, not previously cross-checked in B02. Trade receivable turnover ratio (Note 50, Schedule III mandated ratio table, SA p.103/147): 3.18x→2.96x, **-6.89% (below the 25% mandatory-explanation threshold, so no management reason given, but directionally consistent with the ageing deterioration)**. Unbilled revenue (contract asset) SA ₹2,372.71m→₹2,582.45m (+8.84%), growing faster than total revenue (+2.22%) — flagged in 2A.

### 2E Inventory
SA (Note 11, p.89/147): ₹795.83m→₹613.70m, a genuine decline; inventory write-back ₹16.75m this year vs write-down ₹23.57m prior year (the swing noted in B02 Pattern 4, now source-confirmed) — small in absolute ₹ terms (₹40.32m swing) but directionally another favourable item in a weak year. Trading stock at uninstalled ATM sites ₹111.61m (FY26) vs ₹232.48m (FY25).

### 2F Borrowings, maturity wall, covenants
**There is effectively no debt-maturity wall to map.** SA: CARO ix confirms no loans/borrowings from any lender during the year (clause NA). CON: a short-term borrowing was drawn and fully repaid within the year (₹271.46m drawn and repaid, Note "Change in liabilities arising from financing activities," CON Cash Flow p.110/147) — zero closing balance. Zero long-term borrowings on either balance sheet. D/E = 0.0 across FY24-FY26 (MD&A Key Ratios, p.52/147, self-consistent with the balance sheet). Credit rating unchanged: ICRA [ICRA]AA+ (Stable)/[ICRA]A1+ (Board's Report General Shareholder Information, p.47/147). **No covenant risk exists because there is no covenanted debt.** Lease liabilities (Ind AS 116, not conventional debt) total CON ₹2,213.82m (non-current ₹1,553.71m + current ₹660.11m) — this is the only debt-like liability on the balance sheet and is fully covered by cash+investments of ~₹4,457m.

### 2G Deferred tax reconciliation
SA effective tax rate 25.16% (FY26) vs domestic statutory rate 25.168% — near-perfect alignment, non-deductible expenses ₹5.96m and tax-exempt income ₹(30.01)m are the only reconciling items of size (Note 9(b), p.89/147). CON effective rate 25.16% (FY26) vs 25.18% (FY25) — highly consistent year-on-year, no anomalies. Deferred tax asset movement (Note 9(c)) driven mainly by lease liabilities/ROU asset timing differences (routine Ind AS 116 mechanics), no aggressive DTA recognition observed.

### 2H Exceptional items, goodwill, ESOP, leases, subsequent events
- **Exceptional items:** one-off only, "Statutory Impact of new Labour Codes" ₹57.05m SA / ₹92.44m CON, first occurrence (no FY25 comparative), regulatory-driven not discretionary — low concern, cannot assess a 3-year pattern from this AR alone (no FY24 comparative shown).
- **Goodwill:** CON ₹2,068.68m (FY26) vs ₹2,060.77m (FY25), 8.5% of CON net worth — Securens acquisition goodwill attributed to "customer relationship and non-compete fees... future technological benefits not separately identifiable and expected synergies... not tax-deductible" (Note 45, SA p.103/147) — standard, not aggressive.
- **ESOP dilution:** Basic-diluted EPS gap small (SA 17.31 vs 17.13, ~1%; CON 18.45 vs 18.26, ~1%) — modest dilution, not a red flag on its own. Scheme 2023 forfeiture: 1,007,750 options forfeited/cancelled in the year out of ~7.87m outstanding at start (~12.8% forfeiture rate, as B02 noted) — a retention signal worth watching given the year's compensation cuts.
- **Lease obligations:** CON total lease liabilities ₹2,213.82m; lessor-side contracted lease receivables (ATM/RMS equipment) more than doubled to ₹8,126.31m — carried forward from B02, not independently re-verified this pass.
- **Post balance sheet events:** Note 52's "no significant subsequent events" statement (signed 14-May-2026) is boilerplate and, as B02 flagged, does not cover the buyback (approved the same day) or its underwater economics against CMP — a scope boundary, not a misstatement, since the buyback is separately and prominently disclosed in the Board's Report itself (p.31/147).

**Phase 2 summary:** The triple-pass Top 15 holds up almost entirely intact under independent re-verification, with two findings meaningfully sharpened (Rank 3's segment-vs-services scope; Rank 14's CON-vs-SA loss-allowance direction) rather than weakened. Cross-referencing with Phase 1: the same receivables/provisioning story (Phase 2) sits alongside a hard fraud-reporting clause and an audit-trail scope gap (Phase 1) — two independently-sourced signals pointing at the same broad area of financial-statement reliability (cash handling and receivables/provisioning integrity), which raises the combined weight of the concern beyond either alone. Accounting-quality reconciliation with B02's 4/10 score: **this pass concurs with 4/10**, and would not move it materially in either direction; the extensions found here (Rank 3, Rank 14) are precision improvements, not new negatives or exculpatory findings of comparable weight.

**Phase 2 verdict: 🟡 Watch, trending 🔴** on the provisioning/receivables dimension specifically; other note categories (RPT, borrowings, tax, goodwill) are clean. Kill-switch assessment (informational): a human reviewer would want management's explanation of the SA loss-allowance release before treating FY26 cash conversion as evidence of earnings quality, but nothing here is a fabrication or restatement of prior-year audited figures. **Continuing to Phase 3.**

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow → balance sheet → P&L)

### 3A Cash flow
| Metric | SA FY26 | SA FY25 | CON FY26 | CON FY25 |
|---|---|---|---|---|
| CFO | 3,387.47 | 4,398.09 | 3,895.94 | 4,825.28 |
| PAT | 2,846.72 | 3,288.83 | 3,033.92 | 3,724.57 |
| **CFO/PAT** | **1.190x** | 1.337x | **1.284x** | 1.296x |
| CFI | (2,551.81) | (2,269.71) | (2,699.54) | (2,664.56) |
| CFF | (2,097.60) | (1,422.12) | (2,401.61) | (1,442.28) |
| Net change in cash | (1,261.93) | +706.26 | (1,205.21) | +718.44 |
| Capex (PPE+intang+CWIP) | 3,977.23 | 1,542.48 | 4,092.68 | 1,543.37 |
| D&A (P&L line) | 1,895.56 | 1,544.55 | 2,076.39 | 1,614.57 |
| **Capex/D&A** | **2.10x** | 1.00x | **1.97x** | 0.96x |
| M&A spend | 712.91 (462.66 consideration + 250.25 sub investment) | — | 462.66 | — |

CFO/PAT >1.2x holds on both bases and both years (LBF-1 threshold cleared), but **CFO/PAT compressed YoY on both bases** (SA 1.337x→1.190x; CON 1.296x→1.284x) even as absolute CFO fell in rupee terms (SA -23.0%, CON -19.3%) faster than PAT fell (SA -13.4%, CON -18.6% — SA CFO fell faster than SA PAT, which is the opposite of "cash conversion improving"). **CFO quality checks:**
- **No payable-stretching found — the opposite.** Note 50's Schedule III ratio table (SA, p.103/147) shows Trade Payable turnover **+145.14% YoY** ("Company has settled suppliers due faster compared to previous year"), and the cash flow statement shows a **decrease** in trade payables (SA ₹(711.46)m, CON ₹(711.23)m) as a cash *use*, not a source. This is a genuinely clean signal: CFO is not being propped up by delaying supplier payments; if anything, faster payment is a headwind to CFO this year.
- **Receivables are a real drag, not a source, on CFO too:** "Increase in trade receivables" is a cash outflow adjustment both years (SA ₹(790.48)m FY26, CON ₹(895.29)m FY26) — consistent with the DSO deterioration; CFO would have been higher still had receivables not deteriorated.
- **Inventory rundown is a genuine, modest CFO source** (SA ₹182.12m, CON ₹247.65m), consistent with the inventory decline in 2E — not concealed, and small relative to CFO.
- **One-time/non-operating inflators in the CFO build-up:** none identified as artificial — the add-backs (D&A, ESOP expense, ATM cash-shortage provision ₹590.94m SA/₹618.92m CON, impairment allowance) are standard non-cash reconciling items, correctly added back, not cash-flow-inflating tricks.
- **Net read:** the >1.2x headline is real and not manufactured by payable games; it is, however, **weaker than it looks at first glance** because (a) the ratio itself compressed YoY, (b) receivables deterioration is actively working against it, and (c) it coexists with the loss-allowance release identified in Phase 2 — meaning the provisioning charge that *should* have suppressed reported PAT (and thus lifted the CFO/PAT ratio further) was itself reduced. This is the clearest possible confirmation of B02's central thesis using primary cash-flow evidence: **cash conversion is real this year, but it is not evidence that receivables quality is fine — the two are running in different directions simultaneously.**

**Cash pile:** SA cash+equivalents ₹2,166.19m→₹904.26m (-58.3%); CON ₹2,308.52m→₹1,122.55m (-51.4%). CEO letter (p.5/147) states "cash on books of ₹650 Cr" (a broader liquidity figure including current investments, not just cash-and-equivalents) — consistent with CON current investments ₹2,911.39m + cash ₹1,122.55m + other bank balances ₹423.39m = ₹4,457.33m total liquid assets, still substantial despite the cash-and-equivalents-line decline.

### 3B Balance sheet
| Ratio (CON, FY26 unless noted) | Value | FY25 | Source |
|---|---|---|---|
| D/E | 0.0 | 0.0 | MD&A p.52/147; confirmed nil long-term borrowings on BS |
| Net debt/EBITDA | Net cash (no debt) | Net cash | Balance sheet |
| Current ratio | 2.56x | 2.92x (31,199-6,900=... — MD&A table: 2.6) | CON BS p.109/147 |
| Quick ratio (approx) | 2.45x | — | Computed |
| Interest coverage (EBIT/finance cost) | ~21.8x | — | PBT 4,054.04+Finance cost 194.79 / 194.79 |
| ROCE, post-tax (MD&A table) | **16.6%** | 25.2% (FY25), 25.4% (FY24) | MD&A Key Ratios, p.52/147 |
| ROCE, Schedule III formula (SA) | 20% | 24% | Note 50, SA p.103/147 |
| ROE (computed, CON) | **12.9%** | 17.7% | PAT/Avg equity |
| ROE, Schedule III formula (SA) | 13% | 16% | Note 50, SA p.103/147 |
| Goodwill % net worth (CON) | 8.5% | 9.1% | Note 5, CON BS |

**ROCE crashed from ~25% (FY24, FY25) to 16.6% (FY26) — a ~34% relative decline, and this comes directly from the MD&A's own audited-adjacent ratio table (not a Phase 3 derivation), independently reinforced by the SA Schedule III ROCE figure (24%→20%, -15.17% YoY, self-reported as below the 25% mandatory-explanation threshold so no management reason is required or given). This is arguably the single most important number this deep dive surfaces that B02's notes-focused analysis did not carry: the core profitability-on-capital story deteriorated materially in FY26, not just the receivables/provisioning story.**

**DuPont — is ROE decline operational or leverage-driven?** Equity multiplier (Assets/Equity, CON) FY26 1.331x vs FY25 1.376x — **leverage slightly DECREASED**, not increased. Since D/E is 0.0 throughout, there is essentially no leverage to amplify returns in either direction. **The entire ROE decline (17.7%→12.9%) is margin- and turnover-driven, i.e., purely operational**: net margin fell from 15.36% to 12.20% (CON), consistent with the Cash Management segment result collapse (Phase 2) and the FY26 operating-deleverage story the CEO letter itself narrates (fixed-cost network absorbing a consumption slowdown, delayed SBI contract ramp, competitor-exit disruption). This is a clean, honest DuPont read: **no leverage games are masking or amplifying the profitability decline.**

### 3C P&L
| Line (CON, ₹m) | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 24,871.82 | 24,245.32 | +2.6% |
| Total Income (incl. other income) | 25,328.42 | 24,752.14 | +2.3% |
| EBITDA (MD&A) | 6,002 | 6,333 | -5.2% |
| EBITDA margin | 24.1% | 26.1% | -200bps |
| PBT before exceptional | 4,146.48 | 4,978.39 | -16.7% |
| Exceptional items | (92.44) | — | new |
| PBT | 4,054.04 | 4,978.39 | -18.6% |
| Tax (effective rate) | 25.16% | 25.18% | flat |
| PAT | 3,033.92 | 3,724.57 | -18.6% |
| PAT margin | 12.2% | 15.4% | -320bps |
| Basic EPS | 18.45 | 22.79 | -19.0% |
| Diluted EPS | 18.26 | 22.36 | -18.3% |

**Other income:** CON ₹456.60m / PBT ₹4,054.04m = **11.3% of PBT** (SA: ₹472.58m/₹3,791.19m = 12.5%) — both **below the 20% flag threshold**, clean. Other income composition (Note 20) is routine: interest income (bank deposits, debentures, corporate loan, tax refund), profit on sale of current investments, FVTPL fair value movement, lease-modification gains — no one-off or non-recurring items disguised as operating income.

**Margin waterfall (CON):** Revenue 24,871.82 → EBITDA 6,002 (24.1%) → PBT-before-exceptional 4,146.48 (16.7%) → PBT 4,054.04 (16.3%, after the one-off Labour Code exceptional charge) → PAT 3,033.92 (12.2%, after a stable ~25.2% effective tax rate). **The margin compression is entirely above the tax line and largely above the exceptional-items line — it is an operating-margin story (EBITDA -200bps), not a tax or one-off-item story.**

**Exceptional items, 3-year pattern:** cannot be fully assessed — FY26 is the first year an exceptional item appears in the two years of comparatives shown in this AR (Statutory Impact of new Labour Codes, one-off, regulation-driven). **NOT FOUND: FY24 exceptional-items data** (outside this AR's two-year comparative window).

**Tax rate consistency:** exemplary — 25.16% vs 25.18%, both years essentially at the statutory rate with minor non-deductible/exempt reconciling items. No red flags on tax.

**Basic vs diluted EPS gap:** ~1% both bases, both years — modest, expected dilution from ESOP schemes, not a concern.

**Cross-reference with Phases 1-2:** the operating-margin and ROCE deterioration found here is the *P&L/balance-sheet mirror* of the Cash Management segment result collapse found in Phase 2 (Note 38) and narrated candidly by the CEO letter (Phase 6) as three converging pressures (consumption slowdown, delayed SBI ramp, competitor-exit disruption on a fixed-cost network). It is **not** contradicted by anything in Phase 1's auditor work — the auditor's single KAM is revenue recognition, not margin or provisioning, so the ROCE/margin story sits outside what the audit opinion speaks to directly, which is exactly why an analyst deep dive (rather than reliance on the clean opinion alone) is needed to surface it.

**Phase 3 verdict: 🟡 Watch.** Cash generation is real and not manufactured by payable-stretching, but (a) CFO/PAT compressed YoY on both bases, (b) ROCE fell materially (~25%→16.6% CON, a genuinely large one-year move for this business), and (c) the ROE decline is confirmed purely operational (not leverage-driven, which at least rules out a balance-sheet-risk explanation). Kill-switch assessment (informational): a human reviewer would treat the ROCE collapse as the single most decision-relevant new fact from this phase — more consequential to a GARP framework than any individual note-level item — because it speaks directly to whether FY26 is a one-year air pocket (per management's FY27 guidance) or the start of a structural re-rating-down. **Continuing to Phase 4.**

---

## PHASE 4: RISK FACTORS & MD&A

### 4A Disclosed risks — real vs boilerplate (MD&A Section 7, p.53/147)
| Risk | Real or boilerplate | Evidence |
|---|---|---|
| 7.1 Consumption and Formalisation Slowdown | **Real** — quantified with H1 FY26 actuals, named mitigants (165 direct-to-retail logos, gig conversion, low-yield-account rationalisation) | Specific, not generic |
| 7.2 Digital Substitution | Real but low-urgency — company states its own base case (complementary, not substitutive) and gives a monitoring metric (monthly currency dispensed, ₹2.4-2.5 lakh Cr) with a named contingent response plan | Specific |
| 7.3 Inflationary Cost Pressures (fuel, wages) | Real — names the Code on Wages 2019 mechanism, specific states (Karnataka, UP, Haryana) with ~30%+ hikes already implemented | Specific |
| 7.4 Integration and Execution Risk (FSS) | Real — names the specific mechanisms (contract novation, technology migration, workforce transition) | Specific |
| 7.5 Cyber Security | Real, with actual metrics (zero data breaches, BitDefender ADR score 24% "below industry average," PCI DSS/ISO 27001 compliance) | Specific, verifiable-in-principle |

All five disclosed risks are **specific and evidenced, not generic boilerplate** — this is a comparatively strong risk section by the standard this framework usually encounters.

### 4B Missing risks (evidence-anchored, per protocol)
| Missing risk | Evidence it should be there | Likely reason for omission |
|---|---|---|
| **Receivables/provisioning deterioration** | Note 12/37 (Phase 2, Rank 1/2); DSO 116→126 days is even in the MD&A's own Key Ratios table (p.52/147) but never narrated or explained in risk or MD&A prose | The company discloses the underlying number (DSO) but does not narrate the risk it implies — a disclosed-but-unexplained gap, not a fully silent one |
| **The recurring cash embezzlement / fraud pattern** | CARO xi(a)/(b), Board's Report "Reporting of Frauds" (Phase 1); 3rd consecutive year per company memory | Not mentioned anywhere in the CEO letter, MD&A risk section, or MD&A narrative at all — a genuinely silent omission for a matter that triggered a statutory fraud filing |
| **Loss-allowance / provisioning-adequacy risk specifically** | Phase 2 Rank 1 (SA release), Rank 14 (CON increase) — the direction differs by basis, which is itself a nuance management could usefully address | Entirely absent from risk disclosure; the KAM (revenue recognition) does not cover this ground either |
| **Audit-trail/GL-migration control gap** | Rule 11(g) scope limitation (Phase 1) | Technical/audit-report-only disclosure; not surfaced in management's own risk narrative |

### 4C MD&A deep dive
**Industry claims:** Real GDP growth ~7.4% FY26 (National Statistical Office first forecast), nominal GDP ~8.0%, inflation ~2.8% mid-FY26 (MD&A Section 1, p.51/147) — standard macro scene-setting, consistent with publicly known figures for the period, not independently verifiable within this AR but not implausible.

**Growth/margin explanations:** unusually granular and self-critical — "3.1 What Happened: Three Factors Converged" explicitly names consumption weakness, the delayed SBI contract, and a competitor exit as the drivers of a 15% EBITDA fall in six months (₹1,633m Q4FY25 → ₹1,390m Q2FY26) (p.51/147). This is **credit-taking and blame-assignment done with real specificity**, not vague macro hand-waving.

**External-factor credit-taking/blaming pattern:** management does **not** exclusively blame external factors — it explicitly owns strategic choices with negative near-term consequences ("we walked away from a ₹700cr PSU bank contract... After years of rapid retail growth, we rationalised low-yield customers... We tightened DSOs, accepting some short-term revenue impact"). This is a genuinely balanced narrative pattern, worth crediting.

**Forward guidance table** (protocol required):
| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| FY27 total revenue | ₹2,750-2,850 Cr | FY27 | CON basis; up from FY26 actual ₹2,487.18 Cr (24,871.82m), implies ~10.6-14.6% growth |
| FY27 services revenue | ₹2,650-2,750 Cr | FY27 | Up from FY26 services revenue ₹2,312.11 Cr (23,121m per MD&A 4.2), implies ~14.6-19.0% growth |
| FY27 EBITDA margin | "trending towards the 27% range" | FY27, up from ~25% guided at end of Q4 FY26 | Guidance itself was revised UP intra-year (from ~25% to ~27% range) between the Q4 FY26 analyst update and this AR — a rising, not falling, guidance revision, which is a mild positive credibility signal in itself, though **NOT FOUND: an explicit FY26-guidance-vs-FY26-actual reconciliation** in this AR (the FY26 guidance given at the prior year's disclosure point is not restated here for a direct compare) |
| FY30 services revenue CAGR | 13-14% to ₹3,750-3,950 Cr | Through FY30 | Longer-range target; no interim checkpoints disclosed this AR to test |
| Segment-level FY30 CAGRs | ATM Mgmt ~11%, Retail/CIT ~11%+, T&PS ~20%+ | Through FY30 | Segment-specific, internally consistent with the platform narrative |

**Credibility vs historical delivery:** partially testable. FY26 delivery against what would have been FY26 guidance (set at the "September 2025 analyst day," referenced but not fully quantified in this AR) cannot be precisely checked — **NOT FOUND in this document**. What *can* be checked: the CEO letter explicitly acknowledges FY26 undershot the FY21-FY25 trend (Revenue 17%/Profit 22% annual growth FY21-FY25, interrupted in FY26) and frames FY26 as a self-aware "air pocket" rather than claiming the plan worked — this is consistent, non-defensive framing, which supports (without proving) the credibility of the forward guidance.

**Segment analysis:** MD&A's own alternative segmentation (ATM Management Solutions ~58% of services revenue, Retail Solutions & Currency Logistics ~26%, Technology & Payment Solutions ~16%) **explicitly differs from Note 38's statutory segment reporting** (Board's Report, p.31/147: "these metrics may not be directly comparable to the segment reporting in the financial statements"). Under this alternative cut, **ATM Management Solutions revenue fell -7.8%** (₹6,368m→₹5,872m, MD&A 5.1, p.52/147) — directionally reinforcing Phase 2's Cash Management contraction finding from a second, independently defined angle, even though the two segmentations are not directly reconcilable line-for-line.

### 4D Tone and credibility ratings (1-5, with evidence)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 4/5 | Discloses DSO deterioration, guidance revisions, and a hard year candidly; loses a point for the complete silence on the fraud/embezzlement pattern and provisioning direction in narrative sections |
| Consistency | 4/5 | FY26 guidance-to-actual narrative is internally coherent quarter-by-quarter (Q2 low, Q4 recovery, matches segment-level detail); tax rate, D/E, and other cross-checked figures tie out cleanly across SA/CON/MD&A |
| Specificity | 5/5 | Genuinely unusual level of specific numbers throughout (basis points, exact contract names/values, named states for wage hikes, named competitor dynamics) — well above the norm for this framework |
| Accountability | 4/5 | Explicitly owns strategic trade-offs with near-term costs (walking from the ₹700cr PSU contract, DSO tightening) rather than only blaming macro; does not, however, address the embezzlement pattern or provisioning question at all |
| Capital allocation sense | 3/5 | Clear stated discipline (20% IRR hurdle, "walked away from every one of fifteen opportunities" in FY23/24) and transparent cumulative-allocation table since IPO; but the buyback priced at ₹340/share is now materially underwater against CMP ~₹243 (per company memory), and the 39.2% dividend increase against an 18.6% PAT decline sits awkwardly next to "we will continue to apply that principle as PAT recovers" — the FY26 dividend action does not obviously follow the stated principle in the same year it is asserted |

**Phase 4 summary and cross-reference with Phases 1-3:** MD&A is unusually candid and specific on operating performance and strategy, which is a genuine strength, but it is **silent on exactly the two areas Phases 1-2 flag hardest** — the fraud/embezzlement pattern (Phase 1, a hard clause-xi red flag) and the receivables-provisioning direction (Phase 2, Rank 1/14). A DSO number is disclosed in a table without narrative; nothing else related to receivables quality is mentioned. This is a **contradiction of emphasis, not of fact**: nothing in MD&A misstates what Phases 1-3 found, but the relative prominence given to strategy/growth narrative versus the provisioning and fraud questions is heavily skewed toward the former.

**Phase 4 verdict: 🟡 Watch.** Kill-switch assessment (informational): a human reviewer would not stop on tone/credibility alone — the MD&A is more transparent than most — but would note that the *specific* items Phases 1-2 raised are the *specific* items MD&A does not address, which is not proof of concealment but is a pattern worth naming explicitly to the operator. **Continuing to Phase 5.**

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A Board composition, tenure, attendance
Six-member Board at FY26-close (per Corporate Governance Report, p.40-41/147): 1 Executive Director (Rajiv Kaul, Exec VC & CEO), 2 Non-Executive Non-Independent (Shyamala Gopinath — Chairperson, appointed 13-Nov-2017, ~8.4yr tenure; Krzysztof Wieslaw Jamroz, appointed 10-Aug-2021, ~4.4yr tenure), 3 Independent Directors (Sunil Mehta appointed 06-Dec-2024; Vishnu Jerome appointed 04-Apr-2025; Vidya Krishnan appointed 02-Jan-2026).

- **No independent director >10 years' tenure** — the opposite condition actually holds: **complete independent-director turnover occurred within FY26 itself.** Tapan Ray (ID since Aug-2021) retired 8-Apr-2025 and Sayali Karanjkar (ID since Jan-2022/Mar-2024) retired 31-Dec-2025, both on conclusion of their second terms; both were replaced (Jerome, Krishnan). **All three independent directors at FY26-close have <17 months' tenure with the company.** This is not the protocol's named entrenchment risk, but it is a governance observation worth naming: institutional memory among the independent bench reset entirely within one year, and it produced a **one-day board-composition/independent-woman-director shortfall** (1-Jan-2026, between Karanjkar's retirement and Krishnan's appointment taking formal effect) — disclosed candidly by both the Board's Report and the Corporate Governance certificate as a "procedural gap," with the Board's own characterisation ("not a systemic governance lapse... a deliberate choice to prioritize the induction of a high-caliber professional") noted for the record without independent verification of that characterisation.
- **Attendance:** 4/4 board meetings for all continuously-serving members; no attendance <75% found (Corporate Governance Report Board Meeting table, p.41/147).
- **Cross-board memberships:** none of the six directors sits on >7 listed boards, >10 committees, or is Chairperson of >5 committees (self-certified, p.41/147); Rajiv Kaul (Executive Director) holds zero other directorships. No promoter-group cross-board memberships are possible or relevant, since **there is no promoter** (see 5D).

### 5B Committee analysis
| Committee | Composition at FY26-close | Meetings FY26 | Attendance |
|---|---|---|---|
| Audit | Sunil Mehta (Chairperson, Independent), Vishnu Jerome (Independent), Vidya Krishnan (Independent, inducted Feb-2026), Krzysztof Jamroz (Non-Independent) — churned mid-year following Tapan Ray's and Sayali Karanjkar's retirements | 4 (19-May-25, 23-Jul-25, 5-Nov-25, 12-Feb-26) | Full attendance by serving members; CFO Pankaj Khandelwal present at all meetings |
| Nomination & Remuneration | Vishnu Jerome (Chairperson), Sunil Mehta, Krzysztof Jamroz | 2 | Full attendance |
| Stakeholders' Relationship | Shyamala Gopinath (Chairperson from Apr-2025), Vishnu Jerome, Krzysztof Jamroz, Rajiv Kaul | 1 (11-Dec-2025) | Full attendance; **zero pending investor grievances** at year-end (1 received, 1 resolved) |
| CSR | Rajiv Kaul (Chairperson, per Board's Report signature block) | Composition/meeting detail: **NOT FOUND** in sections read this pass beyond the Chairperson designation |
| Risk Management | Referenced in Board's Report ("please refer to the Report on Corporate Governance") but detailed composition/meeting count: **NOT FOUND** in sections read this pass; MD&A Section 7 confirms a "formal enterprise risk management process" exists with internal auditor (Grant Thornton Bharat LLP) and ICFR-testing consultant (Baker Tilly DHC Advisory LLP) involvement |

Audit Committee mid-year reconstitution (twice, following two independent-director retirements) is consistent with the 5A tenure-churn observation and is not itself an irregularity — quorum and process requirements were maintained throughout per the Corporate Governance Report.

### 5C Compensation
KMP table (Board's Report Annexure 2, p.38/147; SA Note 30, p.96/147):
- **Rajiv Kaul (Exec VC & CEO):** remuneration-to-median-employee ratio **122.16x**; cash remuneration (excl. ESOP value) **down 35.9% YoY** (Basic salary ₹76.57m + benefits ₹0.50m + performance bonus ₹20.55m FY26).
- **CFO Pankaj Khandelwal:** remuneration down 15.1% YoY.
- **Median employee remuneration:** up 2.9% YoY.
- **Average KMP remuneration:** down 31.7% YoY vs average non-KMP employee increase of 5.76% — **KMP pay fell substantially more than the workforce's rose, in the weakest-earnings year on record.** This is a genuinely constructive alignment signal: management compensation tracked the weak year down, rather than being insulated from it.
- Non-executive director commission/fees flat YoY (0.0% change) — ₹2.10m commission + ~₹0.80-0.84m sitting fees per continuously-serving NED.
- **683 permanent employees** on rolls at FY26-close (Board's Report Annexure 2, p.38/147).
- **No promoter-family payroll** to assess — no promoter exists.
- ESOP dilution: covered in 2H (modest, ~1% EPS gap); Scheme 2023 forfeiture ~12.8%.

### 5D Shareholding
**No promoter/promoter-group category exists in the shareholding pattern** (Board's Report Section 7(c), p.48/147) — confirms the injected context: Sion/Advent-Baring exited Feb-2024, promoter declassification effective 2-Apr-2025. The full pattern: Mutual Funds 29.14%, Foreign Portfolio Investors 24.97%, Alternate Investment Funds 6.03%, Resident Individuals (≤₹2L) 21.02%, Resident Individuals (>₹2L) 4.58%, Directors & relatives 6.44% (includes CEO Rajiv Kaul personally, #3 largest shareholder at 6.4254%/10,578,702 shares), NRI 2.30%, Bodies Corporate 3.51%, LLP 0.99%, HUF 0.74%, Trusts 0.13%, KMP (ex-Board) 0.06%, Clearing Members 0.09%, Insurance 0.00%, NBFC 0.00% — sums to 100.00%. Top 10 shareholders: SBI Small Cap Fund 9.11%, Parag Parikh Fund 7.97%, **Rajiv Kaul (CEO) 6.43%**, Kotak Fund 4.59%, Government Pension Fund Global 4.34%, ICICI Prudential Fund 3.85%, Goldman Sachs India Equity Portfolio 2.75%, Wasatch Emerging India Fund 1.78%, Aditya Birla Sun Life Trustee 1.38%, Unifi Blend Fund 2 1.35%. **FII+DII (FPI+MF, strict cut): ~54.1%; including AIF as institutional: ~60.1%** — close to, though not an exact match for, the "58.70%" figure in the injected context, plausibly a timing or classification difference (screener snapshot date vs FY26-close AR date) — **weighed, not treated as a discrepancy requiring resolution here.**
- **No pledge disclosed anywhere.**
- **No promoter-selling-against-growth-narrative pattern is assessable, because no promoter exists** — per the injected context, this should be scored on the no-promoter alternative path, not penalised as a disclosure gap. The relevant alternative-path question is whether the CEO's own 6.43% stake shows any distress signal: **no CEO share sale is disclosed in this AR; his position (10,578,702 shares) is unchanged year-over-year in the pattern shown** — a neutral-to-positive alignment signal (large personal stake, no disclosed selling).

### 5E Governance red-flag checklist
| Item | Finding |
|---|---|
| Whistleblower complaints | Zero received during FY26 (CARO xi(c), management representation; also confirmed in Board's Report Vigil Mechanism section) |
| SEBI/Exchange actions, penalties, strictures (last 3 years) | None (Board's Report, "no penalties or strictures... in connection with violation of Capital Market Norms," p.48/147) |
| RPT committee/process | Audit Committee scrutinises and approves RPTs per its terms of reference (p.42/147); RPT policy on website; Board's Report affirms no materially significant RPT this year |
| Auditor fee ratio | Total ₹16.24m (audit ₹14.34m + OOP ₹1.91m); no separate non-audit fee line disclosed — **cannot conclusively confirm non-audit fees did not exceed audit fees from this table alone**, though nothing in the table suggests they did (flagged as an information gap, not a finding) |
| CSR compliance | Compliant; unspent amount (₹2.71m for ongoing projects, FY25 carryforward) transferred to Special Account within the statutory 30-day window; ₹73.65m total CSR spend FY26 |
| Section 143 fraud (auditor) | **Triggered — ADT-4 filed, s.143(12)** (Phase 1, hard flag, carried forward here) |
| Material subsidiary auditor | Company self-certifies it has **no "Material Subsidiary"** as defined under SEBI regulations (Board's Report Annexure A(n), p.49/147) — worth noting given Securens, Securitrans, and the FSS-acquired business collectively represent a growing share of Group revenue/assets; this determination is procedurally correct under the SEBI size thresholds but means no subsidiary-specific governance disclosures (e.g., a subsidiary secretarial audit) are mandated |

**Phase 5 summary:** Governance is, on balance, clean-to-constructive on the dimensions a promoter-driven company usually fails (pledge: none; promoter selling: not applicable, no promoter; RPT extraction: none found; KMP pay alignment: pay fell more than the business did in a weak year). The genuine governance watch items are narrower and more specific: complete independent-director turnover within one year (with a one-day technical compliance gap as its byproduct), the unresolved fraud clause carried from Phase 1, and thin disclosed detail on the Risk Management and CSR Committees' own composition/activity (an AR completeness gap, not necessarily a substantive governance failure).

**Phase 5 verdict: 🟢 Clean, with one 🟡 Watch item (independent-director churn) and the carried-forward 🔴 fraud flag from Phase 1.** Kill-switch assessment (informational): a human reviewer would not stop on governance structure or shareholding — this is a well-governed, non-promoter, institutionally-owned company on every structural dimension checked — but would carry the fraud clause and audit-trail gap (Phase 1) forward as the standing governance-adjacent concern. **Continuing to Phase 6.**

---

## PHASE 6: CHAIRMAN'S/CEO'S LETTER & FRONT MATTER (read with full knowledge of Phases 1-5)

Note: there is **no separate Chairperson's letter** in this AR — only a "Message from the CEO" (Rajiv Kaul, p.4-5/147). Shyamala Gopinath, the Non-Executive Chairperson, does not carry a standalone shareholder letter. This is an observation, not itself a red flag, but worth naming: the sole shareholder-facing narrative voice is the Executive management, not the independent Chair.

### 6A Narrative vs reality — 5-7 prominent claims cross-checked
| Claim (CEO letter, p.4-5/147) | Cross-check | Verdict |
|---|---|---|
| "We have been debt-free for over a decade" | D/E = 0.0 all three years shown (MD&A table); no long-term borrowings on either balance sheet; short-term borrowing drawn and fully repaid within FY26 | ✅ Confirmed |
| "EBITDA margin for FY26 was 24.1% versus 26.1% in FY25" | Exact match to MD&A Key Ratios table and Phase 3 P&L walk | ✅ Confirmed |
| "Q3'26 marked our bottom... EBITDA margin recovered 280 basis points to 25.6%" | MD&A Section 3.3 confirms Q4 FY26 EBITDA margin 25.6% (up from Q2 low of 22.8%) — the CEO letter's framing ("Q3 marked our bottom... recovery... to 25.6%") is broadly consistent with the quarterly progression shown, though the precise "280bps from where" reference is not perfectly reconciled to a single stated base in the MD&A table shown this pass | ✅ Broadly confirmed |
| "Our ATM Management Solutions business has doubled in the last five years" | **The MD&A's own segment table two pages later (5.1, p.52/147) shows this exact segment's FY26 revenue at ₹5,872m, DOWN -7.8% from ₹6,368m in FY25** — the CEO letter's long-run framing (5-year doubling) is not necessarily false, but it is presented without any acknowledgement of the segment's most recent year-over-year decline, which sits in the very same MD&A document | ⚠️ **Cross-reference tension — see 6E below** |
| "We have not raised a single rupee of primary equity from public shareholders" since Dec-2021 IPO, cumulative capital allocation since IPO: Capex ~₹1,000 Cr, Accretive acquisitions ~₹190 Cr, Dividends ₹437 Cr, generated >₹2,275 Cr since IPO | Arithmetic check: 1,000+190+437 = 1,627 Cr; remainder ≈648 Cr, consistent with the separately-stated "cash on books of ₹650 Cr" | ✅ Confirmed, internally consistent |
| "~₹168 Cr for the buyback while retaining ₹477 Cr for organic investment and opportunistic M&A" | Buyback aggregate consideration ₹1,679.30m = ₹167.93 Cr (Board's Report) — matches "~₹168 Cr" precisely | ✅ Confirmed |
| "FY27 total revenue ₹2,750-2,850 Cr... EBITDA margin trending towards the 27% range" | Matches MD&A Section 6 guidance exactly (internally consistent within the same AR) | ✅ Confirmed, internally consistent |

### 6B Strategic priorities — specific enough, capital allocated, execution evidence
The three-platform strategy (ATM Management, Retail Solutions & Currency Logistics, Technology & Payment Solutions) is specific, has named capital allocated against it (₹40 Cr technology investment FY26, Securens ₹75 Cr, FSS ₹115 Cr pending), and has execution evidence attached (contract wins named with values: SBI ₹1,000 Cr/10-year, ICICI ₹400 Cr+, HDFC ₹400 Cr+; HAWKAI site-count growth from 2,000 to 50,000+). This is a strategy narrative with real operating detail behind it, not aspirational language alone.

### 6C Metrics showcased vs conspicuously absent
**Showcased:** market share (60% ATM Cash Management, 38% Retail Cash, 36% Vision AI BFSI), EBITDA margin trajectory, contract wins, capital allocation history, buyback/dividend mechanics, technology team growth (65% increase to 105 members).
**Conspicuously absent from the CEO letter and MD&A narrative (though present in notes/tables elsewhere in the AR):** DSO/receivables quality, loss-allowance trend, cash-embezzlement incidents, the FSS capital-commitment note gap, ROCE (interestingly, ROCE appears in the MD&A Key Ratios table but is never once mentioned in the CEO letter's prose despite the letter's otherwise extensive use of specific numbers) — the **absence of any ROCE reference in the most numbers-dense shareholder letter this framework has encountered is itself notable**, given ROCE is the one MD&A-table metric that fell hardest (25%→16.6%).

### 6D Tone and priority drift vs prior year
**NOT FOUND / not assessable** — the FY25 AR is not part of this run's inputs, so a direct prior-year tone comparison cannot be made. What is assessable within this AR: the letter's own self-description of a "difficult market... FY26 was hard and we said so early" is consistent with an unusually candid tone for a shareholder letter, and does not read as spin dressed as strategy.

### 6E Quiet Abandonment Check (mandatory)
Reading the opening narrative (CEO letter, front-matter "Three Platforms" infographics) side by side with the operational sections (MD&A segment tables, Note 38 segment reporting):

**Finding 1 — ATM Management Solutions "doubled in five years" vs FY26 -7.8% decline.**
- Opening claim (CEO letter, p.5/147): "Our ATM Management Solutions business has doubled in the last five years."
- Operational section where the tension surfaces: MD&A Section 5.1 (p.52/147), the segment-specific revenue table, showing FY25→FY26 revenue ₹6,368m→₹5,872m, **-7.8%**.
- Classification: **(c) hedged retreat.** The letter's claim (5-year doubling) is not contradicted outright — it may well be true on a 5-year view — but the operational section, two pages later in the same document, shows the *current* year moving in the opposite direction, and the letter does not name or acknowledge this most-recent-year reversal anywhere in its ATM Management Solutions discussion. The letter instead pivots quickly to Vision AI/HAWKAI (a genuinely growing sub-segment) and market-share gains (200bps) rather than addressing the revenue decline in rupee terms.
- Materiality: **Moderate, not thesis-changing on its own** — ATM Management Solutions is ~58% of services revenue, so a -7.8% move in it is consequential, but the MD&A elsewhere (Section 3.1-3.3) does candidly explain the underlying drivers (delayed SBI ramp, competitor-exit disruption, consumption slowdown) that plausibly explain this specific segment's FY26 dip as transitory. The abandonment is one of **emphasis and cross-referencing within the letter itself**, not a concealment of the underlying fact, which is disclosed clearly elsewhere in the same AR.

**Finding 2 — "We have approached capital allocation the same way for over a decade" / "we will continue to apply that principle as PAT recovers" (dividend) vs FY26 dividend +39.2% against PAT -18.6%.**
- Opening claim: capital-allocation discipline is framed as consistent and principle-driven ("our priorities have stayed in the same order: organic growth first, accretive M&A second, sufficient liquidity maintained and surplus returned through dividends and buybacks... we will continue to apply that principle as PAT recovers").
- Operational section: Note 46 (Dividend) and the SOCE show dividend paid rose 39.2% in the very year PAT fell 18.6% — the dividend action in FY26 does not obviously track "as PAT recovers," since PAT did not recover this year.
- Classification: **(a) implicit retraction.** The letter asserts dividends move with earnings, in the same document that shows dividends rising against falling earnings, with no explicit acknowledgement of this specific tension (the Board's Report separately explains the increase as a "timing artefact of a Special Interim Dividend," per B02 — but the CEO letter's own capital-allocation narrative does not surface or reconcile this explanation itself).
- Materiality: **Moderate** — the Board's Report elsewhere provides a mechanical explanation (timing of a special interim dividend), so this is not evidence of undisclosed information; it is evidence that the CEO letter's stated *principle* is not, on its face, consistent with the year's *action*, and the letter does not bridge that gap itself.

No further quiet abandonments of comparable weight identified this pass. The letter is otherwise unusually forthright about setbacks (the ₹700cr contract walk-away, the H1 margin compression, the competitor-exit disruption) — these are proactively narrated, not silently dropped, which is why only the two items above rise to the level of a genuine 6E finding rather than the letter as a whole reading as evasive.

**Phase 6 summary:** The CEO letter is the most candid and numerically specific management narrative this framework has processed for this run — it proactively owns a hard year, names specific strategic trade-offs with real near-term costs, and its headline claims check out arithmetically against the audited tables almost everywhere they can be tested. The two 6E findings are real but narrow: a segment-level emphasis gap (ATM Management's current-year decline vs its 5-year framing) and a capital-allocation-principle-vs-action tension on the dividend (mechanically explained elsewhere in the AR, but not reconciled within the letter itself). Neither rises to fabrication or material misstatement.

**Phase 6 verdict: 🟢 Clean, with two noted 🟡 Watch-level 6E findings.**

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** (fullest reasoning per mandate) | **WATCHLIST** | (1) The "growth" side of GARP is genuinely impaired this year: ROCE fell from ~25% to 16.6% CON, EBITDA margin -200bps, and the core Cash Management segment's *segment result* fell 25% even though gross segment revenue held roughly flat — this is a real profitability deterioration, not merely an optics issue, and it is the kind of one-year air pocket a GARP framework must distinguish from structural decay. (2) The "reasonable price" side is genuinely testable: management's own FY27 guidance (14.6-19.0% services revenue growth, EBITDA margin trending to ~27%) implies a credible glide-path back toward FY24-25 profitability levels if delivered, and the balance sheet (zero debt, ₹4,457m CON liquid assets, ICRA AA+/A1+ rating) gives real balance-sheet room to execute the FSS integration and absorb further margin pressure without financial distress. (3) The receivables/provisioning question (Phase 2) and the fraud clause (Phase 1) are the two items that must be resolved before GARP conviction can move from WATCHLIST to PASS — a GARP thesis on a "transition" name cannot be built on an unexplained loss-allowance release in the exact segment where the core deterioration concentrates; this is squarely the kind of question the framework's LBF-1/receivables-stretch test exists to catch, and it has caught something real here, not a false positive (Phases 2 and 3 both independently corroborate the underlying tension using different primary-source evidence) |
| **Turnaround** (fullest reasoning per mandate) | **WATCHLIST** | (1) The turnaround narrative is unusually well-evidenced for a company this framework encounters: management names three specific, largely one-off/transitory causes for the FY26 downturn (consumption slowdown, delayed SBI ramp, competitor-exit disruption) rather than a single structural cause, and the Q4 FY26 sequential recovery (EBITDA margin 22.8%→25.6%, services revenue crossing ₹600 Cr for the first time) is real, source-confirmed evidence the trough may already be behind the company, not merely guided. (2) Capital allocation during the downturn has been disciplined on the growth side (20% IRR hurdle maintained, fifteen M&A opportunities in FY23/24 rejected, only two accretive/strategic acquisitions — Securens, FSS — actually executed) even as it has been questionable on the distribution side (dividend up against falling PAT, buyback now underwater) — a mixed but not alarming capital-discipline picture for a turnaround thesis. (3) The turnaround thesis's biggest risk is that the "ugly optic" (receivables deterioration, provisioning release) could be either transitory (consistent with the broader consumption-driven turnaround narrative) or the first sign the core Cash Management segment's economics are structurally softening as ATM outsourcing matures — the AR alone cannot resolve this distinction, and per the Transition Decision Matrix this is exactly the PROOF GATE question that must be resolved before a posture can be assigned |
| Value+Quality | WATCHLIST | Zero net debt and strong liquidity support "quality," but the ROCE collapse and receivables/provisioning questions this year weigh against a clean quality read; valuation not assessed in this stage |
| Capex-Led Growth | WATCHLIST | Capex/D&A jumped to ~2.0x this year (from ~1.0x FY25) driven by major new contract build-out (SBI, ICICI, IPPB) — a real capex-led growth signal, but returns on that capital (ROCE) fell in the same year, so the payoff has not yet shown up |
| Cash Flow Compounder | WATCHLIST | CFO/PAT >1.2x on CON basis holds, but compressed YoY on both bases and coexists with a loss-allowance release that caps confidence the ratio reflects underlying receivables quality (Phase 3) |
| Contrarian | WATCHLIST | Depressed FY26 profitability against a self-aware, specific management narrative of transitory causes and an already-visible Q4 recovery could appeal to a contrarian read, contingent on the receivables question resolving benignly |
| Insider Confidence | PASS-leaning | CEO holds 6.43% personally (#3 shareholder), no disclosed selling this year, KMP compensation fell more than the business did in the weak year (pay tracked performance down) — genuine alignment signals, no promoter to distort the read |
| Guidance Divergence | WATCHLIST | FY27 EBITDA-margin guidance was revised UP intra-year (from ~25% to ~27% range) between the September 2025 analyst day and Q4 FY26 — a rising, not falling, revision, mildly supportive of credibility, but the prior FY26 guidance-vs-actual is NOT FOUND in this AR to fully test the pattern |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot
CMS Info Systems Ltd (CMSINFO) — India's largest cash-logistics/ATM-managed-services/BFSI-technology platform (ATM Management, Retail Solutions & Currency Logistics, Technology & Payment Solutions/HAWKAI Vision AI/ALGO). No promoter (institutional/professionally managed since Feb-2024 exit, declassified 2-Apr-2025). FY26 (year ended 31-Mar-2026): CON revenue ₹24,871.82m (+2.6%), PAT ₹3,033.92m (-18.6%), zero net debt, CFO ₹3,895.94m (CFO/PAT 1.28x). Two acquisitions in progress/closed: Securens (closed, Vision AI), FSS ATM Managed Services (₹1,150m, binding agreement, ₹600m paid, H1 FY27 close expected).

### Phase-wise verdict summary
| Phase | Verdict |
|---|---|
| 1. Auditor's Report & CARO | 🟡 Watch (fraud clause is the driver) |
| 2. Notes to Financial Statements | 🟡 Watch, trending 🔴 on provisioning |
| 3. Financial Statements | 🟡 Watch (ROCE collapse, CFO/PAT compression) |
| 4. Risk Factors & MD&A | 🟡 Watch (candid but silent on the two areas that matter most) |
| 5. Corporate Governance & Board | 🟢 Clean, one 🟡 item (ID churn), carries 🔴 fraud flag |
| 6. Chairman's/CEO's Letter & Front Matter | 🟢 Clean, two 🟡 6E findings |
| 7. GARP / Turnaround (fullest reasoning) | WATCHLIST / WATCHLIST |

### Overall quality score: **5/10**
| Component (25% each) | Score /10 | Basis |
|---|---|---|
| Governance | 7 | No promoter, no pledge, no selling pattern, KMP pay tracked the weak year down, zero SEBI/exchange actions, clean RPT process; offset only by the fraud clause (Phase 1/5E) and ID-turnover churn |
| Accounting quality | 4 | Concurs with B02's 4/10; provisioning-adequacy and core-segment disclosure remain the dominant concerns; routine notes (RPT, tax, borrowings, goodwill) are clean |
| Balance sheet | 6 | Zero debt, strong liquidity, ICRA AA+/A1+, no covenant risk — genuinely strong structurally; held back from higher only by the cash-pile halving and the receivables-quality question sitting inside otherwise-strong current assets |
| Earnings quality | 4 | CFO/PAT >1.2x is real and not payable-stretch-assisted (a genuine positive this deep dive confirms), but ROCE collapse (~25%→16.6%), EBITDA margin compression, and the loss-allowance-release-in-a-deteriorating-book pattern are real and unresolved earnings-quality questions |

**Overall: (7+4+6+4)/4 = 5.25 → 5/10** (rounded down given the fraud clause and the still-unresolved provisioning direction, which are the two items most likely to matter to the operator's decision).

### Top 3 strengths
1. **No leverage, no covenant risk, strong liquidity** — D/E 0.0 across three years, ICRA AA+/A1+, ~₹4,457m CON liquid assets; the ROE/ROCE decline is confirmed purely operational, not leverage-driven, which rules out a balance-sheet-risk explanation for the weak year.
2. **Cash generation is not manufactured by payable-stretching** — Trade Payable turnover rose 145% (faster supplier payment, a cash *use*), and receivables deterioration is an active drag on CFO, not a hidden source; the >1.2x CFO/PAT headline survives the CFO-quality checks this framework runs, even as it should not be read as proof receivables quality is fine.
3. **Unusually candid, specific, numbers-dense management narrative with real insider alignment** — no promoter to extract value, CEO personally holds 6.43% with no disclosed selling, KMP compensation fell more than the business did in the weak year, and the CEO letter proactively names and quantifies the FY26 setbacks rather than obscuring them.

### Top 3 red flags
1. **Statutory fraud reporting (ADT-4, s.143(12)) for cash embezzlement, ₹125.35m FY26, 3rd consecutive year per company memory** — a hard CARO clause-xi flag, entirely unaddressed in the CEO letter or MD&A narrative (Phase 1/4B).
2. **SA loss-allowance released 14.1% while the SA 1-2yr overdue bucket it should track grew 16.2x, in the same year the core Cash Management segment's result fell 25%** — the central, cross-verified pattern of this deep dive (Phase 2 Rank 1), now confirmed against primary source with two added precision findings: CON loss allowance actually *rose* 7.7% (the release is SA-specific, not Group-wide), and the segment's *external* revenue fell 6.6% even as gross segment revenue was propped roughly flat by a 76.7% jump in intra-group billing.
3. **ROCE collapsed from ~25% (FY24-25) to 16.6% (FY26, CON, post-tax)** — a materially large one-year move, confirmed by two independent sources within the AR (MD&A Key Ratios table and the SA Schedule III mandated ratio table), and not narrated or acknowledged anywhere in the CEO letter despite the letter's otherwise extensive use of specific figures.

### Key monitorables for next quarter (FY27 Q1)
| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| SA/CON 1-2yr and 2-3yr overdue receivables buckets | Any further increase, or a written-off/provisioned resolution | Quarterly results ageing disclosure (if provided) or next AR Note 12/37 | Tests whether Phase 2's Rank 1 pattern is resolving (favourably) or continuing (unfavourably) |
| Loss-allowance coverage ratio (SA and CON separately) | Coverage ratio should track the ageing profile, not diverge from it | SA and CON Note 12/37 equivalents | Directly tests whether the SA release was justified or the book remains under-reserved |
| Cash Management segment result and revenue (both the Note 38 segment cut and the MD&A ATM Management Solutions cut) | Segment result should stabilise or recover toward FY25 levels if FY26 was transitory per management's own framing | Quarterly segment disclosure / next AR Note 38, MD&A 5.1 | Tests whether FY26 was a one-year air pocket (Turnaround thesis) or a structural decline (Value-Trap risk per the Transition Decision Matrix) |
| Post-tax ROCE (CON) | Recovery trajectory toward the 20-25% range management's FY27 guidance implicitly requires | MD&A Key Ratios table, next AR or quarterly investor deck | The single most consequential number this deep dive surfaced; tests the GARP thesis directly |
| ADT-4/fraud-clause status and embezzlement instance count/quantum | Any further ADT-4 filing, or a declining instance count/quantum trend | Next AR CARO Annexure A, Board's Report | Tests whether this is a structurally recurring control weakness or a genuinely improving trend |
| FSS acquisition completion, funding, and the ₹550m balance payment | On-schedule H1 FY27 completion; funding source (cash vs facility) | Next quarterly results, Reg-30 filings, next AR Note 10/31(b) | Tests both execution risk (Phase 4 risk 7.4) and whether the capital-commitments note discloses the obligation properly once it crystallises |
| Buyback completion price/quantum vs the ₹340/share approved price | Actual tender/completion terms vs the underwater approved price | Reg-30 filings, next AR Board's Report | Tests the capital-allocation-sequencing question (Phase 5/6E dividend-vs-principle tension) |

### One-line verdict
CMSINFO is a debt-free, non-promoter cash-logistics platform with a genuinely candid FY26 turnaround narrative and real insider alignment, but the deep dive confirms — not merely repeats — a hard fraud clause and a provisioning-adequacy question sitting directly beneath a ROCE collapse the CEO letter never mentions: best-fit strategy is **Turnaround**, gated WATCHLIST pending resolution of the receivables/provisioning question before GARP conviction.

---
