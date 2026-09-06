# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: Ceigall India Limited (CEIGALL) | Run date: 2026-09-06
Source: Annual_Report_2026.pdf, FY2025-26, scanned PDF, 151 sheets (no text layer, 150/151 sheets). Read via `pages` ranges as rendered images; all sheets cited below were directly rendered. Two-up printing: PDF sheet = (printed page / 2) + 2. Figures as printed, ₹ Million unless stated. Notes to accounts are governed by B02-notes (all three passes plus B02-notes.yaml); this stage does not re-derive them except to verify, extend, and cross-reference per the Phase 2 special instruction.

**Context carried from Gate 0 / run brief**: no prospectus (company listed August 2024, IPO prospectus absent from this corpus); no results/rating/shareholding/research/announcements corpus. The backward history buildable from this single Annual Report is therefore shallower than normal — only two years of full financial-statement comparatives (FY25/FY26) and a partial four-year snapshot (FY23-FY26) from front-matter infographics, with no pre-IPO disclosure depth. This shortfall is named explicitly at each phase verdict where it bites. Gate 0 (B01): Core 37/100, Grand 45/160, classification AVOID; Block B cash generation 0/20; Block E 0/20 (evidence gap). B02: accounting quality 3/10, six red flags.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core opinion
Both standalone and consolidated opinions are **unmodified/unqualified** on the financial statements themselves (Independent Auditor's Report, standalone sheet 74 printed p.144; consolidated sheet 103 printed p.202). No going-concern qualification at the Ceigall India Limited group or standalone level. The only going-concern-adjacent language in the entire report belongs to a **subsidiary's own auditor** (Emphasis of Matter for Ceigall Ludhiana Rupnagar Greenfield Highway Pvt Ltd, Note 35, cited by the group auditor — see 1C).

Auditor: **B D Bansal & Co, Chartered Accountants**, FRN 000621N; signing partner Sumit Kumar Bansal, M.No. 099496 (both reports, sheets 76, 105).

### 1B. Key Audit Matters
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Estimation of contract cost and revenue recognition (Note 1.2, 2.5(a)/2.6(a); consol. contract revenue Rs 35,241.14m, standalone Rs 34,842.20m FY26) | Input-method (cost-incurred) revenue is "highly sensitive" to cost-to-complete revisions | Auditors evaluated revenue policy, tested revenue workings, agreed contract terms, re-performed proportion-of-completion calcs on a sample (standalone sheet 74; consol sheet 103) | 🟡 Watch — largest source of management discretion in these accounts |
| Valuation of accounts receivable and contract assets given credit-loss risk (Note 13/47(b) consol., Note 12/46(b) standalone) | Consol. receivables + contract assets aggregate Rs 20,558.96m against provision of Rs 66.55m (receivables) / Nil (contract assets); auditors explicitly cite "concentration of credit exposure on a particular customer, being a government organisation" | Tested collectability via inquiry, corroboration, ageing, aging-based ECL model review | 🟡 Watch — nil provisioning on the fast-growing non-cash asset base is the single largest quantitative accounting-quality issue in the filing (B02 finding #1) |
| Standalone-only: Assessment of impairment of investment in and loans/receivables to subsidiaries and JVs (Note 6/7 standalone; carrying amount Rs 7,096.76m) | "Significant judgement and estimation uncertainty" tied to HAM project completion risk | Tested key assumptions (future revenue growth, discount rate, project completion), compared with Board-approved plans | 🟡 Watch — same SPV population as the NHAI-terminated entity (1C) and the auditor-resignation entity (1D) |

No KAM at either level addresses impairment of the Rs 14,578.90m Receivable Under Service Concession Arrangements (RUSCA, B02 finding — a note the triple-pass Pass 1 initially missed and Pass 2 located), even though it sits alongside Contract Assets as one of the two largest non-cash asset lines. This is a **disclosure asymmetry** worth naming: KAM effort concentrates on Contract Assets while a comparably-sized RUSCA balance draws no separate audit-emphasis paragraph.

### 1C. Emphasis of Matter and Other Matters
Consolidated Emphasis of Matter, verbatim (sheet 103, printed p.202): "We draw attention to the following Emphasis of Matter in the audit report of M/s Ceigall Ludhiana Rupnagar Greenfield Highway Private limited... issued by an independent firm of Chartered Accountants... 'We draw attention to Note 35 relating to decision taken by the National Highway Authority to terminate the project... these financial statements have been prepared on a going concern basis and therefore, all assets have been valued at their fair realizable value and all known liabilities have been fully provided for.' Since the component is not material to the Group, hence our opinion is not modified."

Other Matters (consolidated, sheet 104): ten subsidiaries and four step-down subsidiaries' financials were **not audited by the group auditor** — reflect total assets Rs 23,824.07m, total revenues Rs 14,737.59m, net cash flows Rs (244.36)m as at/for the year ended 31-Mar-2026, "furnished to us by the management and our opinion... is based solely on the reports of other auditors" (sheet 104). One foreign step-down entity (total assets Rs 16.77m, "certified by management", not audited by any auditor) is also folded into the consolidated numbers on an unaudited, management-certified basis (sheet 104-105) — consistent with B02's foreign-subsidiary finding.

### 1D. CARO 2020 clause-by-clause (standalone, Annexure A, sheets 76-77)
| Clause | Finding | Amount |
|---|---|---|
| (i)(c) title deeds | Two properties (Land at Bagga Kalan, Ludhiana Rs 1.56m since FY07-08; Land at Halowal, Ludhiana Rs 0.28m since FY03-04) are held in the name of **Ceigall Builders Private Limited**, the company's own erstwhile name, not the current company name; registration "in process" | Rs 1.84m combined, immaterial in quantum but unresolved for 18+ years |
| (ii) inventory | Physically verified during the year; "coverage are appropriate", no material discrepancies | 🟢 Clean |
| (iii) loans to related parties | Loans granted to subsidiaries Rs 2,538.56m during the year (aggregate); balance outstanding Investments Rs 1,714.48m / Unsecured Loans Rs 5,972.34m; loans to subsidiaries repayable at borrower's discretion, "not considered as overdue for more than ninety days"; loan to subsidiaries Rs 459.63m repayable on demand = 8.55% of total loans outstanding | Ties to within 0.1% of Note 7+16+"deemed investment" per B02 Pass 2 bridging |
| (iv) 185/186 | Loans to subsidiaries comply via s.186(11) infrastructure-facility exemption | 🟢 Clean, as represented |
| (vii) statutory dues | "Generally regular"; no undisputed dues in arrears >6 months; **"there are no Statutory Dues which have not been deposited... on account of any dispute"** | 🟡 Watch — this statement sits awkwardly next to Note 46(ii)'s Rs 26.08m indirect-tax **demand** still shown as a contingent liability at 31-Mar-26; not necessarily contradictory (demand may be deposited under protest) but the AR gives no forum/type breakdown to test this, and no note reconciles the two disclosures |
| (ix)(a)/(b) | No default in repayment of loans/borrowings/interest; not declared wilful defaulter | 🟢 Clean |
| (xi)(a) fraud | "The management... identified a fraud amounting to Rs. 89.65 million on account of an isolated collusive arrangement between specific vendors and certain employees of the company at its four sites involving 'Bogus Purchase'... FIR dated 22/01/2026... lodged... against three vendors and six employees... duly recovered from balances payable" | Rs 89.65m, reported under s.143(12) via Form ADT-4 |
| (xi)(b)/(c) | No fraud **by** the company noticed; s.143(12) report filed | 🟢/🔴 mixed — see IFC below |
| (xiv) internal audit | System commensurate with size/nature; internal audit reports considered | 🟢 Clean |
| (xvi) | NBFC/CIC clauses not applicable | 🟢 Clean |
| (xvii) cash losses | "The Company has not incurred cash losses in the current financial year and in the immediately preceding financial year" | 🟢 Clean at STANDALONE parent level only — see consolidated CARO table below for the subsidiary-level exception |
| (xviii) auditor resignation | "There has been no resignation of the statutory auditors during the year" (parent level) | 🟢 Clean at parent level only |
| (xix) | Standard negative-assurance wording: nothing has come to the auditors' attention causing them to believe the company is incapable of meeting liabilities falling due within one year; explicit disclaimer that this gives "no assurance… all liabilities… will get discharged… as and when they fall due" | 🟢 Clean, boilerplate, not an adverse finding (verified directly; earlier internal drafting risk of misreading this as adverse is corrected here) |
| (xx) CSR | Rs 0.08m unspent (non-ongoing project), transfer window (6 months) "has not elapsed till the date of our Audit Report" | 🟢 Clean, informational, ties to B02's CSR-netting finding |

**Consolidated CARO exception table** (Annexure to consolidated auditor's report, sheet 105, re-rendered at full clarity this pass): thirteen group entities are tabulated against three footnote markers — (*) title deeds not in company name, (**) cash losses current + immediately preceding year, (***) auditor resignation. Directly legible at this pass:
- Row 1, **Ceigall India Limited** (Holding Company): Clause (i)(c)* — the same title-deed exception as the standalone Annexure A above.
- Row 4, **Ceigall Ludhiana Rupnagar Greenfield Highway Private Limited** (Step-Down Subsidiary — the same entity whose project NHAI terminated, Note 35): flagged **"Clause xvii\*\*, xviii\*\*\*"** — i.e., BOTH cash losses (current and immediately preceding year) AND auditor resignation during the year attach to this single entity.

**🔴 Correction to B02 Pass 2**: B02 Pass 2 (and the consolidated B02-notes.yaml, finding #4) identified the entity carrying both the cash-losses and auditor-resignation flags as **Ceigall Ludhiana Bathinda Greenfield Highway Pvt Ltd** (row 5 in the same table). This stage's own direct, full-clarity re-render of sheet 105 places both flags on row 4, **Ceigall Ludhiana Rupnagar Greenfield Highway Pvt Ltd** (row 5 in the table carries no footnote marker at all on this reading). This changes the shape of finding #4 materially: rather than **two separate** distressed SPVs (one terminated-project entity, one unrelated auditor-resignation/cash-loss entity), the evidence assembled here points to **one single SPV** — the NHAI-terminated entity — carrying all three adverse signals simultaneously (project termination, going-concern-adjacent Emphasis of Matter from its own auditor, two years of cash losses, and that same auditor's resignation during the year). Both reads cannot be simultaneously correct on a table this dense at scan resolution; this is flagged as an **unresolved cross-pass discrepancy** rather than asserted with full certainty, and is a named verification target: confirm at live-web stage (or on a fresh high-DPI extraction) which of the two named SPVs actually carries the auditor-resignation flag. Either way, the underlying fact pattern — an NHAI-terminated HAM SPV with a going-concern-adjacent EoM — is independently confirmed and not in dispute.

### 1E. Auditor continuity
B D Bansal & Co were **reappointed for a second term of five years** at the 22nd AGM (30-Sep-2024) to hold office until the conclusion of the 27th AGM (FY2028-29) (Directors' Report §24, sheet 36, printed p.68). A second five-year term implies this firm audited the company through at least one prior five-year term — i.e., **this is the pre-IPO private-company auditor carried through the listing**, with cumulative tenure now approaching the ten-year statutory rotation ceiling for listed companies (mandatory rotation due by FY2028-29). Internal Auditor: Grant Thornton Bharat LLP (appointed under s.138). Secretarial Auditor: Lal Ghai & Associates (peer-reviewed firm), appointed for five years to the 28th AGM. Cost Auditor: Khushwinder Kumar & Associates.

Fee ratio (Corporate Governance Report §h, sheet 54, printed p.104): "Total fees for all services paid on a consolidated basis to the statutory auditors" — **Audit Fees Rs 2,250,000** to Ceigall India Ltd is the clearly dominant, legible line item; total fees across the network (Ceigall India Ltd + Velgaon Power Transmission Pvt Ltd + JVs/PMC/Others) sum to **Rs 3,650,000**. The granular split of the remaining ~Rs 1.4m across tax-audit/certification/other-services columns is **RESOLUTION-LIMITED** at rendered zoom (small compressed table), but audit fees clearly exceed any single non-audit line — **no evidence of the non-audit-exceeds-audit flag condition.**

### 1F. Standalone vs consolidated differences
- Consolidated carries one additional KAM area of emphasis wording variance and the Emphasis of Matter (1C); standalone carries the additional KAM #3 on subsidiary/JV investment impairment (not needed at consol level since those entities consolidate).
- Both levels carry a **QUALIFIED opinion on Internal Financial Controls** (Annexure B standalone, sheet 78; Annexure A consolidated, sheet 106) — identical material-weakness language at both levels, tied to the Rs 89.65m fraud: "absence of three-way matching, inadequate physical delivery verification, and lack of effective segregation of duties were remediated as at the close of the year, however... other controls remain under implementation and have not been tested for effectiveness." This is a **live, unresolved control gap** carried into FY2026-27 as filed.
- Ten subsidiaries/four step-down subsidiaries audited by other auditors, one foreign entity management-certified only (1C) — a materially larger reliance-on-others footprint at consolidated level than a typical single-entity standalone opinion.

**Phase 1 summary**: Unmodified opinion on the financial statements at both levels, sitting alongside a **qualified opinion on Internal Financial Controls at both levels** (same root cause: the procurement fraud), an Emphasis of Matter on a terminated-project SPV, and — per B02's cross-checked finding, now qualified by a cross-pass discrepancy on entity identity above — a subsidiary-level statutory auditor resignation. Verdict: 🔴 Red Flag.
**Kill switch (informational)**: A human reviewer would have reason to pause here, because a fraud-driven IFC qualification plus an unresolved subsidiary-auditor-resignation signal, at a company 18 months post-IPO, is the kind of governance pattern that typically precedes further disclosure surprises. The pipeline does not halt on this; it flags and continues.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction, this section verifies the triple-pass Top 15, extends only where thin, and reconciles the accounting-quality verdict.

### Verification of B02's Top 15
Directly re-verified against the document this pass (source: my own reads of the standalone/consolidated Balance Sheet, P&L, Cash Flow, Directors' Report, AOC-1, and CARO Annexures):
- **#2 Contingent liabilities**: Standalone Total Equity confirmed at **Rs 20,980.34m** at 31-Mar-26 directly from the Standalone Balance Sheet (sheet 79) — matches B02's net-worth denominator exactly. Verified ✓.
- **#3 Fraud + DGGI search**: Both independently re-confirmed word-for-word via my own reads of CARO clause (xi), the IFC Annexure B, and Secretarial Audit Annexure A (sheets 76-78, 45-46). Verified ✓.
- **#8 Held-for-sale/Malout-Abohar divestment**: Independently re-confirmed via Directors' Report "State of Affairs" and AOC-1 Additional Details (sheets 34, 40): SPA dated 3-Jun-2026, First Amendment 16-Jun-2026, 100% equity of Ceigall Malout Abohar Sadhawali/Sadhuwali Highways Pvt Ltd transferred to Neo Infra Income Opportunities Fund (managed by Neo Alternative Asset Managers Pvt Ltd) on 16-Jun-2026. Matches B02 Pass 3 exactly. Verified ✓.
- **#9 Loans-to-subsidiaries CARO reconciliation**: Independently re-confirmed via my own read of CARO clause (iii)/(iv): "the Company has granted loans to subsidiary companies during the year at Rs 2,538.56 million... by virtue of section 186(11)" — matches B02 Pass 2's cited Rs 2,538.56m aggregate exactly. Verified ✓.
- **#4 NHAI termination / auditor resignation entity**: See 1D above — a genuine **cross-pass discrepancy** on which named SPV carries the auditor-resignation flag. Logged as a discrepancy, not a clean verify.
- Findings #1, #5, #6, #7, #10, #11, #12, #13, #14, #15: not independently re-derived from the notes this pass (B02's three internal passes already cross-checked each other on these); accepted as B02's final, internally reconciled position.

### 2A. Accounting policy aggressiveness — extension
Confirmed directly from the Material Accounting Policies note (standalone, sheet 108, printed p.168): revenue recognition uses the input (cost-incurred) method for construction contracts; variable consideration (bonuses, incentives, penalties, escalation, arbitration claims) is recognised "when it is highly probable that a significant reversal... will not occur", with claims under arbitration/dispute "accounted for as income based on final award" and expenses on arbitration expensed as incurred. This is a standard, not aggressive, policy framework for the sector — the aggressiveness in these accounts sits in **estimation and provisioning practice** (nil impairment on a tripling Contract Assets balance, thin ECL coverage), not in the stated policy language itself. Depreciation: WDV method, Schedule II lives, no deviations (Note 1.3, confirmed).

### 2B-2H
No material extension beyond B02's three passes; B02's RPT map, contingent-liability ratios, receivables/inventory/borrowings/payables/provisions/deferred-tax/exceptional-items analysis are accepted as final. One incremental cross-reference point: the Directors' Report's own Annexure-5 (Form AOC-2, sheet 45) discloses the **material RPT terms explicitly**, including for Ceigall Ludhiana Bathinda Greenfield Highway Pvt Ltd (Loan Rs 3,492.33m, Interest Rs 5.03m, EPC Contract Revenue Rs 3,483.47m, Sale of Materials Rs 0.06m, Rent Rs 2.86m, Investment n/a) and Ceigall Ayodhya Bypass Pvt Ltd (Loan Rs 74.80m, Interest Rs 11.37m, EPC Contract Revenue Rs 3,504.13m, Investment Rs 0.03m) and Ceigall Northern Ayodhya Bypass Pvt Ltd (Investment Rs 1,26.60m, Loan Rs 461.13m, EPC Contract Revenue Rs 3,077.04m, Mobilization Advance Repaid Rs 250.00m) — all disclosed as "at arm's length and in the ordinary course of business" per the Hybrid Annuity Model concession structure. This is a genuinely full, itemised disclosure (🟢 for disclosure form), even though the underlying scale (single-digit-billion-rupee EPC contract revenue per SPV, funded substantially by parent loans) is the same capital-recycling-into-SPVs pattern B02 already flagged for substance reasons.

### Reconciliation with B02's accounting-quality score
B02 scored accounting quality **3/10**. This stage's own direct reads (auditor's qualified IFC opinion at both levels; the Emphasis of Matter; the cross-pass discrepancy on the auditor-resignation entity, which if anything sharpens rather than softens the underlying concern; the newly-confirmed CFO divergence in Phase 3 below) do not surface anything that would move this score upward, and the standalone-vs-consolidated operating cash flow divergence found independently in Phase 3 (below) adds a further, previously-unquantified dimension to the same concern. **This stage concurs with 3/10.**

**Phase 2 verdict**: 🔴 Red Flag, consistent with B02. **Kill switch (informational)**: unchanged from B02's own assessment — a reviewer would flag but not halt.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first)

### 3A. Cash flow — the central finding of this stage

**Standalone Statement of Cash Flows** (sheet 80, printed p.150):
| | FY26 | FY25 |
|---|---|---|
| Operating profit before WC adjustments | 4,973.53 | 4,432.49 |
| Net cash flow from/(used in) Operating Activities | **+4,569.40** | **(2,709-2,739)** approx, negative |
| Net cash flow from/(used in) Investing Activities | (2,530.77) | n/a |
| Net cash flow from/(used in) Financing Activities | (3,145.31) | 7,057.91 |
| Net Increase/(Decrease) in Cash | (1,106.68) | 1,499.08 |

**Consolidated Statement of Cash Flows** (sheet 108, printed p.212):
| | FY26 | FY25 |
|---|---|---|
| Operating profit before WC adjustments | 5,951.94 | 5,288.86 |
| Net cash flow from/(used in) Operating Activities | **(912.83)** | **(5,155.57)** |
| Net cash flow from/(used in) Investing Activities | (439.24) | (1,298.94) |
| Net cash flow from Financing Activities | +81.49 | +8,461.01 |
| Net Increase/(Decrease) in Cash | (1,270.58) | +1,967.39 |

**🔴 Red Flag, new finding not previously surfaced by B02 (which read the notes but not the primary cash flow statements directly)**: the **standalone parent entity converted to strongly positive operating cash flow this year (+Rs 4,569.40m)** — a sharp reversal from a negative prior year — while the **consolidated GROUP remained cash-flow negative from operations (Rs -912.83m)**, albeit a large (82%) improvement on FY25's Rs -5,155.57m group-level burn. The mechanism is directly visible in the statements themselves: standalone investing activities show **"Loans Given" of Rs 3,136.75m** flowing OUT of the parent into subsidiaries during the year — cash the parent collected from operations (and from repayment inflows) is being recycled straight into SPV funding, which eliminates on consolidation and reappears as the group-level working-capital and project-execution cash burn that Gate 0's Block B flag was built on. This is the clearest primary-statement evidence available in this Annual Report for the "capital-recycling-into-SPVs, cash-negative-at-the-group-level" structural pattern that both B01 and B02 identified indirectly through balance-sheet and note analysis. It **does not overturn** Gate 0's finding (group CFO is still negative, group CFO/PAT for FY26 alone = -912.83/3,089.20 = **-0.30x**), but it **sharpens the mechanism** and shows the group-level burn *improved* materially year on year even as PAT also grew — a genuine, if partial, mitigant that belongs in the record alongside the flag.

CFO quality checks: financing activities in FY25 were dominated by the IPO (Rs 8,461.01m consolidated inflow, "Proceeds from issue of share capital including securities premium Rs 6,584.76m"); FY26's much smaller financing inflow (Rs 81.49m consol.) means this year's burn plus capex (net capex ≈ Rs -379.30m consol., Purchase of Fixed Assets Rs 784.32m less Sale Proceeds Rs 405.02m) is funded largely by **fresh borrowing** (Net Proceeds from Non-Current Borrowings Rs 1,465.22m + Short-Term Rs 290.71m), not by operations. Reconciliation note on the consolidated cash flow statement confirms Rs 322.83m of the FY26 closing cash balance of Rs 3,125.56m sits **inside the Malout-Abohar SPV now classified as held for sale** (Note 19(a)) — a direct, exact tie-out to B02's held-for-sale finding.

FCF (group, approximate): CFO (912.83) + net capex (379.30) ≈ **Rs -1,292 million**, materially negative on a PAT base of Rs 3,089m. Capex vs depreciation: PPE purchases Rs 784.32m vs D&A Rs 616.95m (consol.) — capex modestly exceeds depreciation, consistent with a growing order book, not a maintenance-only business.

### 3B. Balance sheet — key ratios (consolidated, per MD&A "Key Financial Ratios", sheet 33, and Corporate Overview Financial Highlights, sheet 10)
| Ratio | FY26 | FY25 | Direction |
|---|---|---|---|
| Debt-Equity | 0.61 | 0.76 | Improved (denominator effect — IPO equity base) |
| Current Ratio | 1.42 | 1.77 | Deteriorated |
| Interest Service Coverage | 3.31x | 3.55x | Deteriorated |
| Debtor's Turnover (days) | 64 | 64 | Flat |
| Inventory Turnover (days) | 11 | 15 | Improved (-26.67%) |
| Operating Profit Margin | 13.02% | 13.46% | Deteriorated |
| Net Profit Margin | 7.66% | 8.34% | Deteriorated |
| ROCE (consol.) | 19.51% | ~19.22-31.98%* | Deteriorated |
| Return on Net Worth (ROE) | 14.39% | 15.54% | Deteriorated |

*ROCE presentation is internally inconsistent between two front-matter infographics — see Phase 6C.

**Every ratio in the board-approved MD&A table moved adversely year on year except leverage**, and leverage improved mechanically (equity growth from the FY25 IPO and retained earnings, not from debt paydown outpacing growth — standalone term debt fell but consolidated SPV-level debt is the larger and growing piece). **DuPont, qualitative** (precise average-basis figures NOT FOUND IN DOCUMENT — only point-in-time balances are disclosed): Net margin fell (8.34%→7.66%); asset turnover likely fell (total consolidated assets grew faster than the 17.0% revenue growth — Contract Assets +61.8%, RUSCA +40.5%, both YoY); financial leverage fell (D/E 0.76→0.61). The ROE decline (15.54%→14.39%) is therefore a **combination of margin compression and turnover dilution, partially offset by lower leverage** — not a pure "operational deterioration" story, but not a "just a bigger equity base" story either; both effects are real and both point the same direction (down).

Goodwill % of net worth: no goodwill disclosed on the balance sheet (NOT FOUND IN DOCUMENT as a line item) — not applicable to this business.

### 3C. P&L — line walk
Consolidated: Revenue Rs 40,224.01m (+17.0%), EBITDA Rs 5,854m (margin 14.55%, down from 15.08%), PAT Rs 3,089.20m (+7.9% YoY vs FY25's Rs 2,864.90m per the Financial Highlights chart; PAT margin down to 7.66-7.68% from 8.34%). Other income: consolidated Rs 542.55m FY26 vs Rs 562.28m FY25 — **1.75% of PBT (542.55/4,176.28... ~13.0% of total income, but only ~13% of PBT), well under the 20% flag threshold** — 🟢 clean, no other-income inflation of earnings quality. EPS: basic and diluted are **identical** at both levels both years (consol. Rs 17.73/17.04; standalone Rs 17.52/16.07) — confirmed no dilutive instruments (no ESOP scheme found anywhere in 73+51 notes). Tax rate: consolidated effective ~25.71% vs statutory ~25.17-25.25% — consistent, no unusual permanent differences (per B02, reconfirmed here from the P&L tax lines: Current Tax Rs 1,098.07m + Deferred Tax Rs (10.99)m = Rs 1,087.08m total tax on PBT Rs 4,176.28m = 26.0%, close enough given rounding). Exceptional items: none disclosed in either P&L (NOT FOUND IN DOCUMENT) — the fraud's Rs 89.65m impact was routed through balance-sheet adjustments (inventory/payables/GST ITC) as at 31-Dec-2025 per Note 63, with **no P&L exceptional-item line** — a presentation choice that keeps the fraud's cost out of the reported earnings walk entirely (management's own words: "no impact on the Statement of Profit and Loss for the full financial year").

**Phase 3 summary and cross-reference**: The standalone/consolidated CFO divergence (new finding) directly corroborates and mechanically explains B02's Block B flag and Gate 0's cumulative CFO/PAT -0.70x finding, while also showing meaningful group-level improvement this year that the cumulative multi-year ratio alone would not surface. Every board-published margin and coverage ratio deteriorated bar leverage. Verdict: 🔴 Red Flag.
**Kill switch (informational)**: A reviewer would flag the cash-flow mechanism as the single most important thing to understand before valuing this business, but would not halt — the improvement in group CFO YoY is a genuine, if incomplete, positive data point.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed risks — real vs boilerplate
The MD&A "Risk and Concerns" section (sheet 33, printed p.62) is four short paragraphs: unpredictable regulatory environment/permits/clearances; reliance on government contracts and budget allocations; volatility in raw material prices (steel, cement); skilled-labour shortages and ESG compliance costs. This is **generic, sector-boilerplate risk language** — none of it is quantified, none is tied to Ceigall's own numbers, and none mentions any risk actually realised this year (fraud, DGGI search, NHAI termination, contingent-liability growth, reverse-factoring, MSME stretching). 🔴 Real-vs-boilerplate split: 0% specific / 100% generic.

### 4B. MISSING RISKS
Risks visible from Phases 1-3 that are **absent from the MD&A risk section**:
1. **Contract Assets/RUSCA growth to ~71% of revenue with nil impairment** (Phase 1B KAM #2, B02 finding #1) — the auditors' own top KAM is never mentioned in MD&A risk language. Likely reason for omission: naming it would require the company to explain its own provisioning judgement in prose, inviting the exact scrutiny the KAM already exists to flag.
2. **Contingent liability / guarantee-book growth vs net worth** (83.7% of net worth, Phase 1D/2C) — entirely absent from MD&A, despite being disclosed in the same Annual Report's own notes and Directors' Report borrowings section. Likely reason: it is a standard HAM-sector financing feature that management may not consider a "risk" in the conventional sense, but its rate of growth (bank guarantees +22.3% standalone YoY) is exactly the kind of quantifiable trend a risk section should name.
3. **Fraud and DGGI search action** (Phase 1D, 1F) — the fraud is disclosed prominently elsewhere (Note 63, CARO, IFC qualification) but MD&A's risk section makes no reference to control weaknesses or the qualified IFC opinion. Likely reason: MD&A is drafted to read as a growth story; acknowledging a live, unremediated control gap here would undercut that narrative.
4. **Leadership churn** (two Whole-Time Director resignations within a 2-month window post year-end, plus two CEO changes during the year — see Phase 5A) — absent from MD&A entirely. Likely reason: execution-continuity risk from repeated C-suite change is a harder story to spin constructively than macro/regulatory risk.
5. **Standalone-vs-consolidated contingent liability inconsistency** (B02 finding, unresolved) — naturally absent since it is itself an unexplained internal inconsistency, but its absence from any risk or "material uncertainty" disclosure means a reader has no signpost to it without cross-checking two separate notes personally.

### 4C. MD&A deep dive
Industry claims are extensively sourced (PIB, RBI, IMF, Union Budget, index-of-core-industries citations throughout sheets 26-33) and broadly verifiable in direction (India infra capex growth, NHAI's 5,313 km construction in FY26, record MoRTH allocation) — this is the most professionally-sourced section of the report.

Growth/margin explanation: MD&A attributes revenue growth to "strong bidding pipeline, project execution credibility" (Financial Performance Summary, sheet 33) without addressing WHY EBITDA and PAT margins both fell in the same year — a **credit-taking-without-blame-taking asymmetry**: growth is claimed as a result of company execution, margin compression is not explained at all (no mention of input-cost pressure, mix shift toward lower-margin annuity segment, or any other driver). Segment data (Note 69, per B02) shows the Annuity Projects segment earned only Rs 19.82m result on Rs 14,706.25m revenue (0.13% segment margin) versus EPC's much healthier Rs 3,490.24m result on Rs 33,889.86m (10.3%) — **mix shift toward the thinner-margin annuity book is the most likely quantifiable explanation for margin compression**, and it is never named as such in the MD&A.

Forward guidance table:
| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| Order book gives revenue visibility | Rs 1,85,542.86m, book-to-bill 4.8x | "coming years" (unspecified) | ✅ directly ties to Note 46B's Rs 1,85,543m remaining-performance-obligation disclosure (exact match) — a rare case of a PR number anchored precisely to an audited note |
| Renewable energy PPAs "generating predictable annuity-style revenues that meaningfully complement" EPC revenue (Chairman's letter, sheet 9) | 337 MW under PPAs at Rs 2.85/unit (MP) and Rs 2.85/unit (Maharashtra, implied) | present tense, "in the coming years" | ❌/⚠️ NOT SUPPORTED — every renewable SPV named in Annexure-2 (Ceigall Green Energy MH1/MH2/MP, Ceigall Morena Solar BESS, Velgaon Power Transmission) is shown at "pre-construction activities started" or early civil-works stage as of 31-Mar-2026 (sheets 41-42); no renewable-specific revenue line exists anywhere in the segment note. The "now generates" framing is materially ahead of what the operational annexures show. |
| Highway construction execution "remains robust" | NHAI built 5,313 km, exceeding 4,640 km revised target by 15% (industry-wide figure, not company-specific) | FY26 | ⚠️ this is an INDUSTRY statistic presented adjacent to company narrative; not itself a company claim, correctly sourced, but its placement invites a reader to conflate industry execution strength with Ceigall's own, which the MD&A does not separately substantiate with a company-specific on-time-delivery percentage beyond "7 projects completed ahead of schedule" (unquantified base) |

### 4D. Tone and credibility ratings (1-5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2 | Held-for-sale entity and sale economics undisclosed in the financial statements themselves (only recoverable via Directors' Report/AOC-1); RUSCA note near-invisible relative to scale; no risk-section mention of the fraud, DGGI search, or contingent-liability spike |
| Consistency | 2 | Note 18 vs Note 54 IPO-recoverable contradiction (B02); "100% employee retention" (Business Model page) sits beside five KMP/WTD-level personnel changes in ~14 months; two ROCE figures for the same year across two infographics (Phase 6C) |
| Specificity | 3 | Order book and project-level detail (Annexure-2) is genuinely granular and verifiable; risk section and margin explanations are not |
| Accountability | 2 | Margin decline attributed to nothing; fraud framed entirely as "no financial impact" without acknowledging the qualified IFC opinion in the same breath |
| Capital allocation sense | 3 | Capital-recycling thesis is directionally sound and the first transaction is real, but its own economics (price, gain/loss) are not disclosed even to the extent Ind AS 105 would typically invite in a subsequent-events narrative |

**Phase 4 summary**: MD&A risk disclosure is boilerplate and omits every risk this stage's own Phases 1-3 surfaced as material. Verdict: 🔴 Red Flag.
**Kill switch (informational)**: A reviewer would flag the near-total absence of company-specific risk language as a governance-communication gap, not merely a drafting shortcut, given how much adverse-but-disclosed-elsewhere content existed to draw on. No halt.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board composition, tenure, cross-memberships
Board as at 31-Mar-2026 (Corporate Governance Report, sheet 48): 7 directors — Ramneek Sehgal (Chairman & MD, promoter, executive), Chitwan Wason (WTD), Dr. Sudhir Rao Hoshing (WTD, appointed 01-Sep-2025), Arun Goyal (ID), Anisha Motwani (ID), Gurpreet Kaur (ID), Vishal Anand (ID). Independent directors ≥ half the board as required (4 of 7). Aggregate board attendance for FY26: **99.11%** across 7 meetings (sheet 48) — no per-director attendance shortfall below 75% identified. No independent director has tenure exceeding 5 years (all appointed 2021 or later, consistent with the company's 2024 listing).

**🔴 Red Flag, new finding (not surfaced by B02)**: Independent Director **Gurpreet Kaur** is disclosed in the Corporate Governance Report's own directorship table (sheet 48) as simultaneously an Independent Director of **C & C Constructions Limited** — the exact "enterprise where KMP/relatives have significant influence" that B02's Note 49 RPT analysis flagged as carrying a **standing Rs 500 million loan from Ceigall, interest-accruing, unchanged for two years running** (B02 finding #14). An independent director of Ceigall sitting simultaneously on the board of the counterparty receiving a large, static related-party loan is a direct **interlocking-directorship / independence concern** that should have been named alongside the RPT itself; neither the RPT note (Note 49) nor the Corporate Governance Report cross-references the other.

**🟡 Watch, new finding**: Independent Director **Anisha Motwani** discloses seven listed-company directorships including Ceigall (Ceigall India Limited, Absoli Infra Limited, Star Health and Allied Insurance Company Limited, Navama Wealth Management Limited, Raymond Lifestyle Limited, Mothercare Suits Wining India Limited, Godrej Finance Limited — sheet 48) — sitting exactly **at** the SEBI Regulation 17A cap of seven listed-company directorships for an independent director, not over it, but with zero headroom for any further board seat without a compliance breach.

**🔴 Red Flag, new finding, sharpens B02 finding #13 (leadership churn)**: beyond the three CEO-level changes B02 identified from the RPT/KMP note, this stage's direct read of the Directors' Report "Cessations" section (sheet 35, printed p.66) and the Board of Directors page (sheet 24) shows **two Whole-Time Director resignations within a single two-month window immediately following the fiscal year-end**: Chitwan Wason resigned effective **20-May-2026**; Dr. Sudhir Rao Hoshing (who had only joined as WTD/Executive Vice-Chairman on 01-Sep-2025) resigned effective **15-Jul-2026**. Both resignation letters are confirmed by the company to carry "no material reasons... other than those stated," i.e. "personal reasons" — standard boilerplate reassurance. Combined with Ayyalusamy Saravanan's appointment as CEO (10-Feb-2026) and further elevation to WTD & CEO (01-Jul-2026), Dr. Pawan Kumar's appointment as WTD (01-Jul-2026), and Ankit Kumar Agrawal's appointment as ID (01-Jul-2026) replacing the departed WTDs, the **total leadership churn is five KMP/Board-level changes within roughly fourteen months** at a company 18-24 months post-IPO. This is materially broader than B02's "three CEO-level changes" framing.

### 5B. Committee analysis
Audit Committee: 3 members (Arun Goyal Chairman-ID, Ramneek Sehgal, Vishal Anand-ID), 5 meetings, 100% attendance (sheet 48-49). NRC: 4 members, 4 meetings, 91.67% attendance. Stakeholders' Relationship Committee: 3 members, 1 meeting, 66.67% attendance (i.e., 2 of 3 present at the single meeting held). Risk Management Committee: 4 members, 2 meetings, 100% attendance. CSR Committee: 3 members, 2 meetings, 100% attendance. All statutorily required committees are constituted; no committee composition gap identified.

### 5C. Compensation
KMP/Director remuneration table (Annexure-3, sheet 44): total remuneration across 10 named individuals sums to **~Rs 149.52 million**, of which Ramneek Sehgal (MD) alone accounts for **Rs 125.52 million (84.0% of the total)** — a heavily concentrated but, relative to standalone PAT of Rs 3,051.83m (4.1%) or total KMP comp to PAT (4.9%), not an outright excessive quantum.

**🟡 Watch, new finding**: the Annexure-3 column headed "the ratio of the remuneration of each director/KMP to the median remuneration of the employees" shows values that are **exactly 50× each individual's own remuneration figure** for every one of the ten rows without exception (e.g., Ramneek Sehgal 125.52 → ratio 6,276.00; Kapil Aggarwal 4.92 → ratio 246.00; Gurpreet Kaur 0.12 → ratio 6.00). Taken at face value this uniform 50× relationship would imply a median employee annual remuneration of approximately **Rs 20,000** — implausible for an organised 1,966-employee infrastructure company reporting a 5% median-pay increase and a 12% average percentile salary increase for non-managerial staff in the same Annexure. This reads as a **computational or template error in the company's own mandatory Rule 5(1)(ii) disclosure**, not a literal fact about employee pay; it is flagged here as a disclosure-quality/data-integrity finding rather than an operating red flag, but it means this specific statutory disclosure cannot be relied upon as filed.

No ESOP scheme exists (confirmed, Phase 3C). No severance pay, no performance-linked incentive to any Non-Executive Director beyond sitting fees/commission (sheet 51, "Directors' Remuneration").

### 5D. Shareholding
input_gaps carries "shareholding" as absent from this run's corpus — promoter %, YoY change, pledge status, and FII/DII trends are **NOT FOUND IN DOCUMENT** at the granularity a shareholding-pattern filing would give (this Annual Report's Corporate Governance Report gives only the demat/physical split — 100% dematerialised, sheet 54 — not a promoter/public breakdown table). Note however that Note 22.1(e) (Borrowings, per B02) discloses that a **pledge of 51% of certain SPV-level equity/preference capital held by the sponsor/promoter is pledged as security for SPV project debt** at several HAM entities — this is SPV-level share pledge, not parent-company promoter shareholding pledge, and should not be conflated with the latter; it is named here because it is the only "pledge" disclosure this Annual Report contains. Full promoter-selling/pledge verdict is explicitly deferred to B08 per run context.

### 5E. Governance red-flag checklist
| Item | Status |
|---|---|
| Whistleblower complaints | Nil received during the year (CARO clause per Directors' Report; Whistle Blower Policy exists, sheet 71) |
| SEBI actions | One disclosed: Rs 20,000 penalty each from NSE and BSE for a delayed board-meeting-prior-intimation under Reg 29(2)/(3), Sep-2024 (sheet 55) — minor, procedural |
| RPT committee/process | Audit Committee approves all RPTs quarterly (sheet 51); AOC-2 filed with itemised material RPTs (Phase 2) |
| Auditor fee ratio | No non-audit-exceeds-audit signal (1E) |
| CSR compliance | Netting mechanism explained, not a genuine shortfall (B02, confirmed) |
| Section 143 fraud reporting | Yes — filed under s.143(12), Form ADT-4 (1D) |
| Material subsidiary auditor | Two material subsidiaries named (Ceigall Infra Projects Pvt Ltd, Ceigall Northern Ayodhya Bypass Pvt Ltd), audited by ED Bansal & Co and Y.V. Shalla & Co respectively (sheet 55) — DIFFERENT firm from the parent's own auditor for one material subsidiary, a normal but noteworthy multi-auditor structure |
| Interlocking directorship touching a live RPT | 🔴 Yes — Gurpreet Kaur / C&C Constructions (5A, new finding) |
| Sexual harassment (POSH) | Zero complaints pending/received/disposed during the year (sheet 51-52) |

**Phase 5 summary**: attendance and committee mechanics are clean; the substantive concerns are the interlocking directorship touching a material RPT, the KMP remuneration-ratio disclosure error, and the scale of leadership churn. Verdict: 🔴 Red Flag (upgraded from what a mechanics-only read would suggest, on the strength of the interlock and churn findings).
**Kill switch (informational)**: A reviewer would want the interlocking directorship and the leadership churn explained directly by the company before proceeding; not itself a halt condition.

**flags candidate**: FLAG-PROMOTER-PRELIM does not apply here (no promoter-selling-against-growth-narrative evidence exists in this corpus — shareholding data is absent, not adverse); the interlock/churn findings are governance findings distinct from the promoter-pledge/selling pattern that flag is designed for.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

### 6A. Narrative vs reality
| Claim (Chairman's letter, sheet 9, and front matter) | ✅/❌/⚠️ | Evidence |
|---|---|---|
| "Our order book for FY 2026 has grown substantially" | ✅ | Order book +71.7% YoY (Note 46B), independently anchored |
| "FY 2026 marks the year Ceigall took a decisive leap — from a roads and highways company into a diversified & integrated infrastructure and clean energy developer" | ⚠️ | True at the order-book/LOA level (renewable order book Rs 35,614.81m = 19.19% of total, sheet 7); NOT yet true at the revenue-recognition level — every named renewable SPV is at pre-construction/early-construction stage (Annexure-2) |
| "Our renewable energy platform... generates predictable annuity-style revenues that meaningfully complements our project-based EPC revenues" | ❌ | Not supported — see Phase 4C forward-guidance table; no renewable-specific revenue exists in the segment note this year |
| "Our first HAM asset monetisation... has already validated this thesis" | ⚠️ | The transaction is real and confirmed (Phase 2), but sale consideration and gain/loss are undisclosed anywhere in this Annual Report — a reader cannot independently test whether the transaction "validates" anything financially |
| "Asset-light model approach to avoid capital blockage" (Business Model page, sheet 29) | ⚠️ | True for the EPC arm's fixed-asset base; NOT representative of the group's capital allocation, which carries Rs 1,714.48m of SPV investments and Rs 5,972.34m of unsecured SPV loans outstanding (CARO Annexure A) — capital is very much "blocked" at the group level, just not in the form of owned plant and equipment |
| "100% Employees retention" (Business Model page, sheet 29) | ⚠️ | Likely refers to non-managerial workforce attrition (a common, narrower KPI definition); sits in visible tension with the KMP/board churn detailed in Phase 5A two sections of the same report away — the two claims are about different populations, so not a strict contradiction, but the juxtaposition is notable |

### 6B. Strategic priorities
Priorities named (geographic expansion, sector diversification into renewables/T&D, capital recycling, operational excellence) are specific enough to be testable and each has at least one concrete FY26 data point behind it (renewable LOAs named with MW capacity and tariff, Malout-Abohar divestment, order-book detail). Capital allocated to each priority is disclosed at the aggregate level (order-book value by segment) but not as a discrete capex-by-priority table.

### 6C. Metrics showcased vs conspicuously absent
Showcased: revenue, EBITDA, PAT, EPS, ROCE, ROE, order book, book-to-bill, lane-km, projects completed. Conspicuously absent from all front-matter infographics: CFO/operating cash flow (never shown as a headline metric anywhere in the Corporate Overview, despite the group's negative CFO being the single most consequential financial fact in this filing per Phase 3), contingent liabilities as a ratio, and any KMP-churn metric.

**🟡 New finding**: the Corporate Overview "Key Highlights" infographic (sheet 7) states **ROCE 19.22%** as the FY26 headline figure, while the "Financial Highlights" four-year bar chart two sheets later (sheet 10) shows **ROCE FY2026 = 19.51%** for the same metric, same year. Both are front-matter (unaudited) presentations of the same underlying number; the ~0.3 percentage-point discrepancy is immaterial in magnitude but is a genuine internal inconsistency within the company's own marketing pages, consistent with the pattern of cross-note inconsistencies B02 found in the audited sections (Note 18/54, standalone/consolidated bank guarantees).

### 6D. Tone and priority drift
No prior-year Annual Report is in this corpus to compare tone directly (IPO prospectus and prior ARs both absent — the degradation named in the run brief). Within this year's own document, the tone is consistently promotional across Corporate Overview, MD&A, and Directors' Report, with the risk/governance material confined to the statutory sections at the back — a structurally normal pattern for Indian annual reports, but one that makes the backward-reading method's value (starting from CARO/notes rather than the Chairman's letter) directly evident in this filing.

### 6E. Quiet Abandonment Check (mandatory)
Two clear instances identified:

1. **HEDGED RETREAT** — Opening claim (front matter, sheet 4): "Capital Recycling: A Structured Growth Engine... Ceigall has adopted capital recycling as a core pillar of its growth strategy — **systematically** monetising **completed and near-complete** HAM assets... This approach... **The Company's first such transaction**... marks the start of what is intended to be a **sustained, repeatable** monetisation cycle." Operational section: Directors' Report/AOC-1/Note 19 disclose exactly **one** transaction, with **no consideration, no gain/loss, and no Ind AS 105 fair-value disclosure** anywhere in the financial statements. The word "systematically" and "structured... engine" describe an operating capability that, on the evidence filed, consists of a single opaque transaction. Materiality: **moderate-to-high** — this is the core plank of the transition thesis the operator's strategy is built to detect (capital-recycling execution), and the gap between the framing and the evidence bears directly on whether the "engine" is real or aspirational.

2. **SILENT DROP** — Opening claim (Chairman's letter, sheet 9): "FY 2026 was our bold and decisive entry into India's renewable energy sector... Our renewable energy platform... **generates predictable annuity-style revenues** that meaningfully complements our project-based EPC revenues." Operational section: the segment note (Note 69, per B02) shows only "EPC" and "Annuity Projects" (i.e., the road HAM book) as reportable segments, plus an unlabelled "Others" segment (Rs 4,982.68m revenue) — **no renewable-specific revenue or profit line is ever disclosed**, and Annexure-2's own project-status entries for every renewable SPV (Velgaon Power Transmission, Ceigall Green Energy MH1/MH2/MP, Ceigall Morena BESS) show "pre-construction activities started" or equivalent early-stage status. The claim of present-tense, "predictable" revenue generation from this vertical is never addressed, confirmed, or walked back anywhere in the operational sections — it simply never reappears. Materiality: **moderate** — does not itself invalidate the diversification strategy (which is genuinely underway at the order-book/LOA level) but means the specific claim of currently-generating annuity revenue from renewables should not be relied upon.

No third instance rises to the same clarity; the "100% employee retention" / KMP-churn juxtaposition (6A) is noted there rather than counted as a third abandonment, since it concerns different populations rather than the same claim being walked back.

**Phase 6 summary**: The Chairman's letter and front matter are directionally accurate on the two things most verifiable (order book, business-model shift toward developer/HAM structure) and overstate or leave unaddressed the two things most central to the transition thesis (capital-recycling "engine" maturity; renewable revenue realisation). Verdict: 🟡 Watch, tightening toward 🔴 on the two 6E findings.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| **GARP** | WATCHLIST | (1) Growth is real and evidenced (order book +71.7%, revenue +17%, EPS +4% YoY consol.) at a reasonable trailing P/E (~20x on CMP Rs 356 / diluted EPS Rs 17.73, per run context — not an AR-sourced figure); (2) but "reasonable price" cannot be cleanly assessed without pricing in the accounting-quality discount: nil provisioning on ~71% of revenue in non-cash receivables, a qualified IFC opinion, and a group CFO still negative all argue the reported EPS growth is of lower quality than the headline multiple assumes; (3) margin trajectory (EBITDA margin down, PAT margin down, ROE down) is the wrong direction for a GARP thesis premised on quality-compounding growth — this is currently **growth without margin expansion**, which is a weaker GARP setup than the framework requires |
| **Turnaround** | WATCHLIST | (1) This is not a distress-recovery story — PAT has risen every year shown (Rs 1,672.72m FY23 to Rs 3,089.20m FY26) — so "turnaround" in the classic sense does not fit; (2) what IS underway is a **business-model transition** (pure EPC contractor toward developer-with-capital-recycling), which shares some turnaround-adjacent characteristics (unproven new operating model, one data point of execution, market not yet able to price the shift) but the underlying business was never distressed; (3) the closest fit is an early-stage, largely unproven diversification/model-transition rather than a turnaround from a low base |
| Value+Quality | FAIL | Accounting quality 3/10 (B02) and a qualified IFC opinion directly conflict with the "Quality" leg; valuation is not distressed enough to satisfy "Value" on its own |
| Capex-Led Growth | WATCHLIST | Capex modestly exceeds depreciation (Rs 784.32m vs Rs 616.95m consol.) and order book supports future capex, but capex is dwarfed by the SPV loan/investment outflow (Rs 3,136.75m standalone) — the real capital deployment is financial (loans/equity into SPVs), not fixed-asset capex |
| Cash Flow Compounder | FAIL | Group CFO negative both years shown; standalone-only positive CFO this year does not qualify at the consolidated/investable-entity level |
| Contrarian | WATCHLIST | AVOID-adjacent Gate 0 classification plus a real, evidenced improvement in group CFO burn YoY (Phase 3) is exactly the kind of divergence a contrarian thesis would want to test further, but the governance findings (fraud, DGGI search, leadership churn, interlocking directorship) raise the bar for what "the market is wrong" would need to overcome |
| Insider Confidence | INSUFFICIENT EVIDENCE | Shareholding/pledge data absent from this corpus (input_gaps); cannot be assessed from the AR alone |
| Guidance Divergence | WATCHLIST | The renewable "predictable annuity-style revenue" claim (Phase 6E) is a live, testable guidance-vs-delivery gap to track into FY2026-27 results |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot
Ceigall India Limited — road/highway EPC contractor with a HAM (Hybrid Annuity Model) asset portfolio and a newly-initiated capital-recycling strategy, diversifying into renewable energy and T&D. Listed August 2024 (IPO Rs 401/share). FY26 revenue Rs 40,224.01m (consol., +17.0%), PAT Rs 3,089.20m (+7.9%), order book Rs 1,85,542.86m (book-to-bill 4.8x). CMP Rs 356.0, market cap Rs 6,198 cr (run context, not AR-sourced).

### Phase-wise verdict summary
| Phase | Verdict |
|---|---|
| 1 Auditor/CARO | 🔴 Red Flag |
| 2 Notes | 🔴 Red Flag |
| 3 Financial Statements | 🔴 Red Flag |
| 4 Risk/MD&A | 🔴 Red Flag |
| 5 Governance | 🔴 Red Flag |
| 6 Chairman's letter | 🟡 Watch |
| 7 Best-fit strategy | WATCHLIST (GARP and Turnaround both) |

### Overall quality score
Governance 25% × 3/10 = 0.75; Accounting quality 25% × 3/10 = 0.75; Balance sheet 25% × 4/10 = 1.00 (order book strength and improving leverage partially offset contingent-liability growth and the non-cash-asset build-up); Earnings quality 25% × 3/10 = 0.75.
**Overall: 3.25/10 → rounded 3/10.**

### Top 3 strengths
1. Order book +71.7% YoY to Rs 1,85,542.86m, ties exactly to the audited Note 46B disclosure — genuine, evidenced forward revenue visibility, not a PR number (Phase 4C).
2. Group-level operating cash burn improved materially YoY (Rs -5,155.57m to Rs -912.83m consolidated), and the standalone parent entity is now solidly cash-generative from operations (+Rs 4,569.40m) — a real, if partial, improvement the cumulative multi-year Gate 0 metric alone does not show (Phase 3A).
3. IPO proceeds fully and verifiably utilised per the independent monitoring agency (ICRA) with a clean audit trail, and RPT/related-party SPV funding is comprehensively, individually itemised in the notes and AOC-2 (Phase 2), even where the underlying capital-allocation pattern itself draws separate scrutiny.

### Top 3 red flags
1. Contract Assets + RUSCA together equal ~71% of one year's consolidated revenue with nil impairment provisioning, the auditors' own top KAM, against a backdrop of a qualified Internal Financial Controls opinion at both standalone and consolidated levels stemming from a Rs 89.65m procurement fraud (Phases 1B, 1D, 2).
2. Group-level leadership churn — five KMP/Board-level changes in roughly fourteen months, including two Whole-Time Director resignations within a single two-month window immediately post-year-end — plus an interlocking directorship (Independent Director Gurpreet Kaur also sits on the board of C&C Constructions Ltd, the counterparty on a standing Rs 500m related-party loan) (Phase 5A).
3. Contingent liabilities at 83.7% of standalone net worth (up from 57.5%), a confirmed and unreconciled standalone-vs-consolidated bank-guarantee inconsistency, and a separate DGGI GST search action on wrongful ITC availment tied to IPO expenses — three independent, mutually reinforcing signals of strained financial-control and disclosure discipline in the same fiscal year (Phases 1D, 2, B02).

### Monitorables for next quarter/next filing
| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Group CFO/PAT | Should stay positive-trending; watch for reversal below FY26's -0.30x | Quarterly cash flow statement (once available) or next AR | Tests whether the FY26 improvement is a trend or a one-off |
| Contract Assets + RUSCA as % of revenue | Watch for further rise above ~71% | Next AR, Notes 11/7 or equivalent | Tests whether unbilled revenue growth is decelerating toward billing/collection |
| First impairment/write-down on Contract Assets or RUSCA | Any non-nil provision booked | Next AR provisioning notes | Would be the first hard evidence the auditors' KAM concern is materialising |
| Malout-Abohar divestment consideration and gain/loss | Disclosure of actual sale price | Q1/Q2 FY27 results, or next AR subsequent-events/Note 19 update | Tests whether the "validated thesis" claim (Phase 6A) holds up financially |
| Renewable segment revenue | First disclosed renewable-specific revenue/profit line | Next AR segment note (Note 69 equivalent) | Tests the "predictable annuity-style revenue" claim (Phase 6E) |
| Statutory auditor rotation | Any early rotation before FY2028-29 | Directors' Report auditors section | Second five-year term is now running; any earlier change would be unusual and worth investigating |
| CARO subsidiary auditor-resignation entity identity | Confirmation of which named SPV | Next AR CARO exception table, or live-web verification | Resolves the Phase 1D cross-pass discrepancy this stage flagged |
| KMP remuneration ratio disclosure | Corrected ratio in next AR | Next AR Annexure equivalent to this year's Annexure-3 | Tests whether the 50x-uniform anomaly (Phase 5C) was a one-off template error or recurs |

### One-line verdict
Growing order book, deteriorating margins and cash conversion, and a governance record — fraud, GST search, leadership churn, unreconciled contingent liabilities — too crowded for anything but a cautious WATCHLIST under a GARP or transition-focused lens.

**Note on the AR-only backward history**: with the IPO prospectus, results, rating, shareholding, research, and announcements corpus all absent (input_gaps), this stage's backward read is built entirely on one Annual Report with two years of full financial-statement comparatives and a four-year front-matter snapshot. Every trend claim above rests on that two-to-four-year base only; a genuinely longer backward history (5+ years, pre-IPO) could not be reconstructed from this corpus and is not attempted here, per instruction.

```yaml
stage: B03-ardeep
company: "CEIGALL"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps: [prospectus, results, rating, shareholding, research, announcements-substantive]
flags:
  - {type: FLAG-CASH, reason: "Consolidated CFO negative both FY25 (Rs -5,155.57m) and FY26 (Rs -912.83m), though the burn improved 82% YoY; standalone parent CFO turned strongly positive (+Rs 4,569.40m) this year while investing activities show Rs 3,136.75m of fresh loans flowing from parent into SPVs, the direct primary-statement mechanism behind Gate 0's Block B finding. Contract Assets + Receivable Under Service Concession Arrangements combined equal ~71% of FY26 consolidated revenue with nil impairment provisioning (auditors' own top KAM)."}
phase_verdicts: {p1: "RED FLAG - unmodified opinion but qualified IFC at both levels, EoM on a terminated-project SPV, unresolved cross-pass discrepancy on the CARO auditor-resignation entity", p2: "RED FLAG - B02's 3/10 accounting quality score concurred with; triple-pass Top 15 substantially reverified with one entity-identification discrepancy logged", p3: "RED FLAG - standalone vs consolidated CFO divergence is the stage's central new finding; every board-published margin/coverage ratio deteriorated bar leverage", p4: "RED FLAG - MD&A risk section is generic boilerplate, omits every material risk this stage's own phases surfaced", p5: "RED FLAG - interlocking directorship touching a live RPT (Gurpreet Kaur / C&C Constructions), five KMP/Board changes in ~14 months, and a self-inconsistent KMP remuneration-ratio disclosure", p6: "WATCH - two quiet-abandonment findings (capital-recycling 'engine' framing outruns a single opaque transaction; renewable 'predictable annuity revenue' claim unsupported by segment data)", p7_best_fit: "WATCHLIST under GARP and under an early-stage business-model-transition lens; FAIL on Value+Quality and Cash Flow Compounder"}
overall_quality: 3
quality_components: {governance: 3, accounting: 3, balance_sheet: 4, earnings: 3}
kill_switch_notes:
  - "Phase 1: a reviewer would pause on the fraud-driven IFC qualification plus the unresolved subsidiary-auditor-resignation signal at a company 18 months post-IPO, but the pipeline flags rather than halts."
  - "Phase 3: a reviewer would want the standalone/consolidated CFO divergence fully explained by management before valuing the business, but the YoY improvement in group CFO burn is a genuine mitigant; no halt."
  - "Phase 4: a reviewer would flag the near-total absence of company-specific risk language as a governance-communication gap; no halt."
  - "Phase 5: a reviewer would want the interlocking directorship and the leadership churn explained directly by the company; no halt."
triple_pass_verification:
  verified: 15
  discrepancies:
    - {finding_rank: 4, triple_pass_value: "B02 Pass 2 identified Ceigall Ludhiana Bathinda Greenfield Highway Pvt Ltd (row 5, CARO exception table, sheet 105) as the entity carrying both the cash-losses (**) and auditor-resignation (***) flags", ar_value: "Stage 3's own full-clarity re-render of sheet 105 places both flags on Ceigall Ludhiana Rupnagar Greenfield Highway Pvt Ltd (row 4) instead - the same entity as the NHAI-terminated project (Note 35) - with row 5 showing no footnote marker on this reading", note_ref: "CARO exception table to consolidated Auditor's Report, sheet 105"}
missing_risks:
  - {risk: "Contract Assets + RUSCA at ~71% of revenue with nil impairment (auditors' own top KAM)", evidence: "Note 11/46B, Note 7 consol.; Phase 1B, Phase 4B"}
  - {risk: "Contingent liability / bank-guarantee book growth to 83.7% of standalone net worth", evidence: "Note 46(ii) standalone, sheet 92/100; Phase 4B"}
  - {risk: "Procurement fraud and qualified IFC opinion, both levels", evidence: "Note 63; CARO xi; IFC Annexure B/A; Phase 4B"}
  - {risk: "Leadership churn: five KMP/Board-level changes in ~14 months", evidence: "Directors' Report Cessations, sheet 35; Board of Directors page, sheet 24; Phase 5A, Phase 4B"}
  - {risk: "Standalone vs consolidated contingent-liability inconsistency, unreconciled anywhere in the document", evidence: "B02 Pass 2/3; Phase 4B"}
guidance_table:
  - {claim: "Order book gives strong revenue visibility", number: "Rs 1,85,542.86m order book, 4.8x book-to-bill", timeframe: "unspecified, 'coming years'", credibility: "High - ties exactly to audited Note 46B"}
  - {claim: "Renewable platform generates predictable annuity-style revenue complementing EPC", number: "337 MW under PPAs at ~Rs 2.85/unit", timeframe: "present tense", credibility: "Low - not supported by segment note; all named renewable SPVs at pre-construction/early-construction stage per Annexure-2"}
  - {claim: "Capital recycling is a sustained, repeatable monetisation cycle", number: "one transaction (Malout-Abohar), consideration undisclosed", timeframe: "'start of' a sustained cycle", credibility: "Low-Medium - real but single-instance, opaque economics"}
monitorables:
  - {metric: "Group CFO/PAT", threshold: "watch for reversal below FY26's -0.30x, or continued improvement toward positive", where: "next quarterly/annual cash flow statement", why: "tests whether FY26's cash-burn improvement is a trend"}
  - {metric: "Contract Assets + RUSCA as % of revenue", threshold: "further rise above ~71%", where: "next AR notes 11/7 or equivalent", why: "tests deceleration of unbilled-revenue build-up"}
  - {metric: "First impairment on Contract Assets or RUSCA", threshold: "any non-nil provision", where: "next AR provisioning notes", why: "would confirm the KAM concern materialising"}
  - {metric: "Malout-Abohar sale consideration/gain-loss", threshold: "any disclosure", where: "Q1/Q2 FY27 results or next AR", why: "tests whether divestment was value-accretive"}
  - {metric: "Renewable segment revenue", threshold: "first disclosed renewable-specific P&L line", where: "next AR segment note", why: "tests the 'predictable annuity revenue' claim"}
  - {metric: "CARO subsidiary auditor-resignation entity identity", threshold: "confirmation of named SPV", where: "next AR CARO table or live-web verification", why: "resolves this stage's cross-pass discrepancy"}
ar_new_downstream_entities:
  - {name: "Neo Infra Income Opportunities Fund / Neo Alternative Asset Managers Private Limited", where_in_ar: "Directors' Report State of Affairs, sheet 34; AOC-1 Additional Details, sheet 40", entity_type: "acquirer counterparty in first HAM asset divestment"}
  - {name: "C & C Constructions Limited", where_in_ar: "Related Party Transactions Note 49 (via B02); Corporate Governance Report directorship table, sheet 48", entity_type: "RPT counterparty (standing Rs 500m loan) and interlocking-directorship entity via Independent Director Gurpreet Kaur"}
  - {name: "Velgaon Power Transmission Limited", where_in_ar: "Directors' Report Annexure-2, sheet 41; segment/RPT notes", entity_type: "newly-acquired subsidiary, T&D vertical entry (share purchase agreement 09-Jan-2026)"}
  - {name: "Rewa Ultra Mega Solar Ltd / MP Urja Vikas Nigam Ltd / MP Power Management Company Ltd (MPPMCL)", where_in_ar: "Chairman's Message, sheet 9", entity_type: "renewable-energy PPA/LoA counterparties, first named renewable customers"}
  - {name: "Maharashtra State Electricity Distribution Co. Ltd (MSEDCL)", where_in_ar: "Chairman's Message, sheet 9", entity_type: "renewable-energy PPA counterparty via Ceigall Green Energy MH1/MH2"}
strengths_top3:
  - "Order book +71.7% YoY to Rs 1,85,542.86m, ties exactly to the audited Note 46B disclosure"
  - "Group-level operating cash burn improved 82% YoY; standalone parent is now solidly cash-generative from operations"
  - "IPO proceeds fully and verifiably utilised per independent monitoring agency; RPT/SPV funding comprehensively itemised in notes and AOC-2"
red_flags_top3:
  - "Contract Assets + RUSCA at ~71% of revenue with nil impairment, alongside a fraud-driven qualified IFC opinion at both levels"
  - "Five KMP/Board-level leadership changes in ~14 months plus an interlocking directorship touching a material RPT"
  - "Contingent liabilities at 83.7% of net worth, an unreconciled standalone/consolidated guarantee inconsistency, and a separate DGGI GST search action"
best_fit_strategy: "GARP (WATCHLIST) and early-stage business-model-transition (WATCHLIST); FAILS Value+Quality and Cash Flow Compounder"
one_line_verdict: "Real growth, thinning margins, governance too crowded for more than cautious watch"
analyst_note: "Two findings here materially extend B02: (1) the standalone-vs-consolidated cash flow statements, read directly rather than via the notes, show the parent entity is now cash-generative while funding SPVs whose consolidated burn is the actual source of Gate 0's flag - a mechanism, not just a symptom; (2) the Corporate Governance Report's own directorship table surfaces an interlocking directorship (Gurpreet Kaur / C&C Constructions) that B02's note-only read could not have found, since it requires cross-referencing a governance-section table against a financial-note RPT entry. One finding here CONTRADICTS B02 Pass 2: this stage's own full-clarity re-render of the CARO exception table (sheet 105) attributes the cash-losses/auditor-resignation flags to a different named SPV than B02 identified - logged as an open cross-pass discrepancy, not resolved, because a table this dense at scan resolution cannot be called with full confidence from either pass alone."
```
