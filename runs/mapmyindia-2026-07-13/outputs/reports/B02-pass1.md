# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 (FULL EXTRACTION)
Company: C.E. Info Systems Ltd (MAPMYINDIA) | Run date: 2026-07-13
Source: inputs/_text/annual-report__Annual_Report_2023.txt (page-marked text extract of Annual_Report_2023.pdf)

---

## CRITICAL DATA-PROVENANCE FLAG (read before anything else)

The file supplied as `Annual_Report_2023.txt` is **not** the FY2023 annual report. Its cover page,
letter to exchanges, and audit opinion all identify it as the **30th Annual Report, FY2024-25**
(year ended 31 March 2025), approved by the Board on 9 May 2025, filed with exchanges 2 July 2025
(p.1, p.2, p.106, p.160). Every note in the document carries two columns: "As at/Year ended
31.03.2025" and the comparative "31.03.2024" — there is no FY2023 balance sheet or P&L in this
file at all (FY2023 appears only as a single opening-balance row in the Statement of Changes in
Equity, p.126/180).

**Implication:** this Pass 1 extraction is anchored to FY2025 vs FY2024, not FY2023 vs FY2022 as
the task brief assumed. All figures below are FY25/FY24. If the pipeline genuinely needs FY2023
notes, the wrong PDF was supplied upstream — flagged as `input_gaps` in the eventual Pass 3 YAML.
Given CLAUDE.md's "never estimate" rule, I have extracted exactly what is in the document rather
than guess at FY2023 figures.

**Units:** All statement and note headers state "All amounts are in Indian Rupees in lakhs (except
for share)" (e.g. p.112, p.166, p.184). Per pipeline instruction, figures below are converted to
₹ Crores (1 Cr = 100 lakh); the original lakh figure is shown alongside on first use for audit
trail. Both **Standalone** (parent only) and **Consolidated** (Group) notes are covered — standalone
notes 1–52 run p.118–160(approx. PDF page 119-161); consolidated notes 1–52 run p.172–216 (approx.
PDF page 173-217). Where a finding applies materially differently at standalone vs consolidated
level, both are called out.

---

## 1. ACCOUNTING POLICIES & CHANGES

- **No new Ind AS first-time adoption disclosed this year.** Policy note states policies "consistently
  applied, except where a newly-issued accounting standard is initially adopted" — no such adoption
  is named (Note 2.1(a), standalone p.119, consolidated p.173). 🟢 Clean.
- **Climate-risk assessment boilerplate:** "no material impact on the financial statements" (Note
  2.1(d)(ii), standalone p.119, consolidated p.173). Generic, no company-specific analysis. 🟢 Clean/neutral.
- **Depreciation useful lives** (Note 2.2(a), standalone p.121-122, consolidated p.174): Computers—end
  user 3 yrs, Computers—servers/networks 6 yrs, R&D equipment 15 yrs, Furniture & fixtures 10 yrs,
  Electrical installation 10 yrs, Vehicles 8 yrs, **Map survey vehicles 3 yrs, IoT devices on rent 3
  yrs**. Company explicitly discloses these last two are shorter than Schedule II Part C norms,
  "to reflect actual usage" — self-disclosed and conservative (faster expensing), not aggressive.
  🟢 Clean.
- **Intangible useful lives** (Note 2.2(b), standalone p.123, consolidated p.175): internally generated
  map database 5 yrs, internally generated software 5 yrs, right-to-non-compete 5 yrs, acquired
  computer software 6 yrs, customer contracts (Gtropy, consolidated only) 5 yrs. Standard, no red flags.
- **Capitalisation threshold:** NOT FOUND IN DOCUMENT — no minimum-value capitalisation policy disclosed
  for PP&E or intangibles.
- **Revenue recognition — percentage-of-completion (POC) for fixed-price contracts,** with a company-set
  threshold of recognising revenue only once "stage of completion of contract exceeds 25%" (Note
  2.2(d), standalone p.120, consolidated p.174). This is independently flagged by the auditor as the
  sole **Key Audit Matter** in both standalone and consolidated opinions, citing "high inherent risk"
  and "high inherent uncertainty" (Auditor's Report, standalone p.106-107, consolidated p.161). 🟡 Watch
  — inherent estimation risk; see Section 11 for the growing share of revenue this method now covers.
- **Goodwill impairment testing:** policy commits to annual testing "relying on operating results,
  business plans and future cash flows" (accounting policy, consolidated p.179) but **no CGU-level
  growth-rate or discount-rate assumptions are disclosed anywhere in the notes**, despite ₹4.34 Cr
  (₹434 lakh) of goodwill sitting static on the consolidated balance sheet both years. NOT FOUND IN
  DOCUMENT for actual testing evidence. 🟡 Watch (low investor materiality: goodwill is 0.5% of
  consolidated equity, but the disclosure gap itself is a transparency miss).
- **ECL methodology:** "simplified approach," lifetime ECL on trade receivables from initial recognition
  (Note 2.2(i)(a), standalone p.122, consolidated p.176-177). See Section 4 for adequacy assessment.
- **Ind AS 116 leases:** incremental borrowing rate fixed at transition (1 April 2018) at **11.25%**,
  unchanged since (Note 35(3) standalone p.152, Note 34(3) consolidated p.209). ROU asset fell from
  ₹5.13 Cr to ₹1.52 Cr; lease liability fell from ₹7.32 Cr to ₹2.23 Cr (both books, both years) as
  older leases roll off (Note 35/34, p.152-153/209). 🟢 Clean — properly disclosed, declining lease
  footprint consistent with the business.
- **Borrowing costs:** standard capitalisation-on-qualifying-assets policy (Note 2.2(k), standalone
  p.146) — not currently applicable as company carries no term debt.

---

## 2. RELATED PARTY TRANSACTIONS

Standalone Note 31 (p.147-149); Consolidated Note 30 (p.202-205).

| Party | Nature | FY25 (₹Cr) | FY24 (₹Cr) | YoY % |
|---|---|---|---|---|
| PT Terra Link Technologies (40% JV, new) | Sale of services | 23.68 | 0.00 | new |
| Gtropy Systems (75.98% sub, standalone-only, eliminated in consol) | Purchase of goods | 27.12 | 27.87 | -2.7% |
| Gtropy Systems | Technical expenses | 19.91 | 15.02 | +32.6% |
| CE Info Systems Intl Inc | Sale of services | 1.28 | 10.87 | -88.2% |
| PhonePe Pvt Ltd (>10% shareholder) | Sale of services | 4.31 | 7.06 | -38.9% |
| Rakesh Kumar Verma (Co-founder/MD) | Salary & allowances | 1.50 | 1.50 | flat |
| Rashmi Verma (Co-founder/CTO) | Salary & allowances | 1.50 | 1.50 | flat |
| Rohan Verma (Whole-time Dir/CEO) | Salary & allowances | 1.50 | 1.50 | flat |
| Rakesh Kumar Verma | **Rent expense (co. pays promoter)** | 0.12 | 0.12 | flat |
| Rashmi Verma | **Rent expense (co. pays promoter)** | 0.06 | 0.06 | flat |
| Shambhu Singh (Non-exec dir) | Commission | 0.16 | 0.06 | +167% |
| Anil Mahajan (Non-exec dir) | Commission | 0.18 | 0.06 | +200% |
| Tina Trikha (Non-exec dir) | Commission | 0.12 | 0.04 | +200% |
| Kogo Tech Labs (associate) | Investment | 0.00 | 9.00 | — |
| Indrones Solutions (associate→FVTPL) | Investment | 0.00 | 4.00 | — |

(Note 31B standalone p.148-149; Note 30b consolidated p.203-204)

- KMP fixed-salary lines are flat YoY despite ~9-10% consolidated PAT growth — no evidence of
  compensation ratcheting. 🟢 Clean.
- Independent-director commission roughly tripled YoY across the board (small absolute amounts,
  ₹0.06-0.18 Cr each) — not explained in the notes; likely reflects a full year of post-IPO
  commission structure vs partial-year FY24. 🟡 Watch (small $, worth one line in questions-for-mgmt).
- **Company pays rent to promoter-family KMPs** (Rakesh & Rashmi Verma) for premises — flat, small,
  but a standing related-party rent arrangement warranting disclosure of arm's-length benchmarking
  (not provided in the note). 🟡 Watch.
- All RPTs asserted to be "at arm's length" (Note 31D standalone p.149 / Note 30g consolidated p.205)
  — standard boilerplate assertion, not independently evidenced in the notes.
- **No loans to promoters/directors/KMP/related parties** at 31 March 2025 or 2024 (Note 31E standalone
  p.149 / Note 30h consolidated p.205). 🟢 Clean.
- Security to subsidiary Gtropy: FD lien **₹19.00 Cr (up from ₹15.00 Cr PY)** against Gtropy's OD/CC
  facility from Bank of India (Note 36ii standalone p.153, Note 35ii consolidated p.209, Note 45
  p.159/215). 🟡 Watch — rising parental collateral support to a subsidiary that itself is
  loss-making at points (see Section 6/12).
- New related parties this year: PT Terra Link Technologies (JV, formed 6-Dec-2024); note also
  records new minority investees Kaainos Geo-Spatial Technologies and SIMDAAS Autonomy (Note 5) —
  not RPTs per se, but new "related" investees to watch.
- RPT scale vs revenue: standalone sale-of-services RPTs (PT Terra Link + CE Info Intl + PhonePe +
  Gtropy) sum to roughly ₹34.6 Cr against standalone revenue of ₹383.87 Cr ≈ 9% of standalone revenue
  — not disclosed as a ratio by the company; computed here for reference.

---

## 3. CONTINGENT LIABILITIES

Standalone Note 36 (p.153); Consolidated Note 35 (p.209).

| Item | FY25 (₹Cr) | FY24 (₹Cr) | YoY % |
|---|---|---|---|
| Bank guarantees (standalone) | 26.62 | 20.36 | +30.7% |
| Bank guarantees (consolidated) | 29.04 | 21.95 | +32.3% |
| FD lien securing Gtropy's OD/CC facility | 19.00 | 15.00 | +26.7% |

- Consolidated bank guarantees / total equity (₹791.70 Cr) = 3.7% — no single item exceeds 10% of net
  worth. 🟢 Clean.
- No tax disputes, litigation contingent liabilities, or guarantees for subsidiaries beyond the FD
  lien are disclosed anywhere in Notes 1-52 (standalone or consolidated). NOT FOUND IN DOCUMENT for
  tax-dispute composition — appears the company simply has none pending, consistent with the
  standalone Auditor's CARO report item 7(b): "no statutory dues...which have not been deposited...
  on account of disputes" (p.109-110).
- The Syska LED Lights tenant-default matter (Note 3(c), standalone p.130-131, consolidated
  p.185-186) is a receivable-recovery legal action (company as claimant, Operational Creditor under
  IBC), not a contingent liability of the company. Quantum of the related provision is **not disclosed**
  (NOT FOUND — see Section 9).
- Overall rating: 🟢 Clean — contingent exposure is low, growing in line with business scale, and
  well within net-worth tolerances.

---

## 4. TRADE RECEIVABLES

Standalone Note 8 (p.133-134); Consolidated Note 8 (p.188-189).

**Consolidated ageing, ₹ Cr (converted from lakh):**

| Bucket | FY25 gross | FY24 gross |
|---|---|---|
| Not due | 69.62 | 51.91 |
| <6 months | 47.10 | 45.82 |
| 6m-1yr | 15.37 | 5.00 |
| 1-2yr | 5.22 | 3.19 |
| 2-3yr | 0.71 | 0.68 |
| >3yr | 0.80 | 0.76 |
| **Total gross** | **138.82** | **107.36** |
| Less ECL | (5.82) | (2.68) |
| **Net** | **133.00** | **104.68** |

- >6 months as % of total gross receivables: FY25 = (5.22+0.71+0.80)/138.82 = **4.9%**; FY24 =
  (3.19+0.68+0.76)/107.36 = **4.3%** — mild deterioration, not alarming in isolation.
- **ECL loss allowance more than doubled: ₹2.68 Cr → ₹5.82 Cr (+117%)** (Note 8, Note 29 credit-risk
  movement, consolidated p.201). The P&L charge for "Provision for doubtful debts" also more than
  doubled: **₹1.88 Cr → ₹4.14 Cr (+120%)** (Note 23 Other Expenses, consolidated p.196) — against
  revenue growth of only 22%. 🔴 Red Flag — receivables-quality deterioration meaningfully outpacing
  revenue growth. **Candidate for FLAG-CASH.**
- Receivable-days proxy: Trade Receivable Turnover ratio (consolidated) fell from 4.66x (FY24) to
  3.90x (FY25), a -16% variance (Note 43, p.213) — implied days-sales-outstanding rose from ~78 to
  ~94 days. Company's own >25%-variance-trigger table does not require an explanation at -16%, but
  the direction is consistent with the ECL deterioration above.
- No single-customer concentration disclosure — NOT FOUND IN DOCUMENT.
- Related-party receivables are small and shrinking: Mappls DT trade receivable fell from ₹2.72 Cr to
  nil; CE Info Systems Intl receivable fell from ₹4.84 Cr to ₹1.19 Cr (Note 31C standalone p.148).
- Average credit period stated as 30-90 days, no interest charged on delayed payments (Note 8(1),
  p.133/188) — standard.

---

## 5. INVENTORY

Standalone Note 7 (p.132); Consolidated Note 7 (p.188).

**Consolidated, ₹ Cr:**

| | FY25 | FY24 | YoY % |
|---|---|---|---|
| Raw material | 9.31 | 7.18 | +29.7% |
| Finished goods | 7.53 | 1.72 | +337.8% |
| Stock-in-trade | 0.00 | 1.58 | -100% |
| Gross | 16.84 | 10.48 | +60.7% |
| Less provisions | (2.13) | (2.14) | flat |
| **Net inventory** | **14.71** | **8.34** | **+76.4%** |

- Inventory grew **76% while consolidated revenue grew only 22%** — a significant divergence, led by
  finished-goods build-up (+338%). 🟡 Watch.
- The company's own Financial Ratios note explains the Inventory Turnover Ratio decline (6.52x →
  4.74x, -27%, consolidated) as: **"Closing inventory increase primarily due to decrease of hardware
  sale"** (Note 43, consolidated p.213) — a self-disclosed admission that hardware (IoT/telematics
  devices, likely Gtropy-related) sales softened, leaving unsold stock. Consistent with Sale of
  Hardware revenue falling 18.4% YoY (₹66.97 Cr → ₹54.64 Cr, Note 19).
- No specific "obsolete inventory" write-down disclosure beyond the standard lower-of-cost-or-NRV
  provisions (₹2.13 Cr FY25, flat YoY) (Note 7).
- Standalone inventory is immaterial (₹0.29 Cr, Note 7 standalone p.132) — the buildup is entirely a
  consolidated-level (Gtropy/hardware) phenomenon.

---

## 6. INVESTMENTS

Consolidated Note 5 (p.186-188); Note 44 subsidiary/associate/JV table (p.214-215); standalone
Note 5 (p.131-132), Note 44 (p.159).

- **Subsidiaries (100% Mappls DT, 100% CE Info Systems Intl, 75.98% Gtropy)** — standalone carrying
  costs: Mappls DT ₹2.66 Cr (equity ₹1.64 Cr + pref ₹1.02 Cr); CE Info Systems Intl ₹7.17 Cr; Gtropy
  ₹13.50 Cr (equity ₹3.86 Cr + pref ₹9.64 Cr) (Note 5 standalone, p.131-132).
- **Indrones Solutions — reclassified out of associate status this year.** Shareholding reduced from
  20.00% to 18.40% on 6-Dec-2024, "therefore it was not subsidiary [associate] after the said
  deduction" (Note 44 footnote **, consolidated p.215). The related preference-share holdings
  re-appear under "carried at fair value through profit and loss," growing from ₹6.58 Cr (FY24,
  ₹2.58+₹4.00 Cr) to ₹14.71 Cr (FY25, ₹6.85+₹7.86 Cr) (Note 5 consolidated, p.187) — a **+124%**
  fair-value step-up embedded in a Level 3 (unobservable-input) instrument in the same year the
  entity lost its equity-method associate status. 🟡 Watch — timing and magnitude of the fair-value
  gain on a newly-reclassified illiquid holding warrants scrutiny.
- **New JV — PT Terra Link Technologies (Indonesia, 40%, formed 6-Dec-2024).** Standalone investment
  ₹34.98 Cr (cash-flow statement, p.116); consolidated carrying value (equity method, net of loss)
  ₹32.16 Cr. Already loss-making: **share of JV loss ₹2.82 Cr in ~4 months of consolidation**
  (Consolidated P&L, p.168; Note 5, p.186). This single new bet equals ~4.4% of total consolidated
  equity. 🟡 Watch — sizeable, immediately dilutive new commitment.
- **Kogo Tech Labs (40.17% associate) continues loss-making**, share of loss ₹1.09 Cr FY25 (₹1.52 Cr
  FY24); carrying value declined to ₹16.52 Cr from ₹17.62 Cr net of cumulative losses (Note 5, p.186).
  Note explicitly states: "the company's board in the year 2024-25 has decided **not to make any
  further investment** in the said company" (Note 44 footnote *, p.215) — a management signal of
  reduced conviction. 🟡 Watch.
- **Minority-stake FVTPL portfolio expanding fast:** aggregate unquoted investments rose from ₹56.05
  Cr to ₹100.10 Cr (+78.6%) (Note 5, p.187), spanning Briskworld, Cusmat, E-Chargeup, Nawgati,
  Kaainos, SIMDAAS, Hicetane, Sree Sai Aerotech. Fair-value hierarchy shows Level 3 exposure rising
  from ₹17.22 Cr to ₹26.64 Cr (Note 29, consolidated p.199-200). Total "Gain on investments (net)"
  in other income rose ₹13.68 Cr → ₹27.02 Cr (**+97.5%**) (Note 20, consolidated p.195), now a
  meaningful and growing share of the ₹52.44 Cr consolidated other income (total income ₹515.69 Cr)
  — i.e. ~5.2% of consolidated total income is unrealised/Level-3 fair-value gains on illiquid
  startup investments. 🟡 Watch — earnings-quality concern; non-cash, judgment-driven, concentration
  risk in a venture-style minority-stake book growing faster than the core business.
- **No ICDs or interest-bearing loans given** to related parties beyond routine lease security deposits
  (₹1.29 Cr) — confirmed by Note 31E/30h ("no loans to promoters, directors, KMPs..."). 🟢 Clean.

---

## 7. BORROWINGS

Standalone: **debt-free** other than lease liabilities (Note 46, capital management, standalone
p.159 — "Total Borrowing – nil" both years).

Consolidated: subsidiary Gtropy Systems carries a **Bank Overdraft/Cash Credit facility of ₹27.62
Cr (FY25) vs ₹18.40 Cr (FY24)** from Bank of India, interest 8.0%-9.5% p.a. on actual utilisation,
repayable on demand, secured by hypothecation of Gtropy's book debts/inventory **and** lien of
parent-company FDs up to ₹19 Cr (Note 14, consolidated p.203). 🟡 Watch — the OD grew 50% YoY and
carries parent-company collateral support, tying group liquidity to a subsidiary's working-capital
cycle (see Section 6 re: Gtropy's inventory build-up).

- Consolidated Debt-Equity ratio 3.77% (FY25) vs 3.90% (FY24) (Note 43, p.213) — trivial leverage
  at group level.
- No covenant breaches, waivers, or term changes disclosed. No 5-year repayment schedule applicable
  (on-demand facility). No related-party borrowings.
- Overall: 🟢 Clean — company remains a net-cash business; the only debt is a modest, growing
  subsidiary working-capital facility.

---

## 8. TRADE PAYABLES

Standalone Note 16 (p.137); Consolidated Note 17 (p.193).

**Consolidated, ₹ Cr:**

| | FY25 | FY24 | YoY % |
|---|---|---|---|
| MSME dues | 3.77 | 11.93 | -68.4% |
| Other creditors | 26.44 | 13.13 | +101.4% |
| **Total** | **30.21** | **25.06** | **+20.6%** |

- No interest due/paid on delayed MSME payments — **NIL** both years, all categories (Note 41,
  consolidated p.211; Note 42, standalone p.155). 🟢 Clean.
- MSME payables **fell 68%** while non-MSME payables **more than doubled** — a significant mix
  shift not explained anywhere in the notes (the Financial Ratios note only comments on the
  aggregate Trade Payables Turnover ratio, which moved -7%, below its own 25% disclosure trigger,
  Note 43 p.213). 🟡 Watch — worth a management question given the magnitude of the MSME-vs-other
  swing even though the aggregate ratio move was small.
- Standalone shows the same MSME-down pattern even more starkly: ₹15.88 Cr → ₹3.94 Cr (-75.2%)
  (Note 16, standalone p.137), while total standalone payables fell ₹21.59 Cr → ₹9.30 Cr — the
  standalone entity evidently paid down a large MSME balance during the year.
- Note observation: the consolidated trade-payables ageing table (Note 17, p.193) shows column
  headers "Not Due / 1-2 years / 2-3 years / More than 3 years" with **no "less than 1 year" bucket**,
  whereas the standalone ageing table (Note 16, p.137) does include that bucket. This is either an
  extraction artifact or a genuine formatting inconsistency between the two ageing tables in the
  source document — flagged for verification against the original PDF if the ageing profile becomes
  decision-relevant.

---

## 9. PROVISIONS

Standalone Note 15 (p.137); Consolidated Note 16 (p.192-193).

- **Gratuity (defined benefit) — funded status weak.** Consolidated PBO ₹21.23 Cr vs plan assets
  ₹9.40 Cr at 31 March 2025 → **plan is only ~44.3% funded**; net liability rose from ₹9.03 Cr (FY24)
  to ₹11.83 Cr (FY25), +31% (Note 31A, consolidated p.206). 🟡 Watch — not alarming for an Indian
  mid-cap but a growing unfunded obligation worth tracking.
- Actuarial assumptions (Note 31G, standalone p.150 / consolidated p.207): discount rate 7.04% (FY25)
  vs 7.25% (FY24); long-term salary growth 12.00% flat; return on plan assets 7.25% vs 7.40%;
  attrition 17% (≤30 yrs) / 9% (31-44 yrs) / 4% (>44 yrs); mortality 100% IALM (2012-14) — standard,
  no unusual assumptions.
- No warranty, decommissioning, or onerous-contract provisions disclosed — NOT FOUND / not
  applicable per notes.
- **Litigation provision for the Syska LED Lights tenant-default matter is qualitative only — the
  rupee amount of the provision is not disclosed** (Note 3(c), standalone p.130-131, consolidated
  p.185-186). NOT FOUND IN DOCUMENT. 🟡 Watch — a quantified provision would improve transparency
  given the company is actively pursuing an IBC claim.
- **"Provision for expenses" (other provisions) nearly tripled: ₹3.66 Cr → ₹10.87 Cr** (consolidated
  Note 16, p.193) with no composition breakdown given. NOT FOUND IN DOCUMENT for what this comprises.
  🟡 Watch — a large, undecomposed provision movement.

---

## 10. DEFERRED TAX

Standalone Note 27 (p.142-143); Consolidated Note 26 (p.197-199).

- **Effective tax rate rose sharply: 28.24% (FY25) vs 23.27% (FY24)** against a flat statutory rate
  of 25.17% both years (Note 26, consolidated p.198). The reconciliation's "Others" line swung from
  a ₹3.83 Cr **credit** (FY24) to a ₹5.81 Cr **charge** (FY25) — a large, undecomposed swing (Note
  26 reconciliation table, p.198). 🟡 Watch — "Others" is not broken down.
- **Prior-period deferred-tax correction, quantified and disclosed:** "Deferred tax for Q4FY25 and
  for the year ended 31/03/2025 is inclusive of **Rs 517 lakhs (₹5.17 Cr) not provided in earlier
  years** on unrealised gains on investment made in unlisted private companies which was accounted
  for in respective years as profit/loss as other income" (Note 26, consolidated p.197; Note 27,
  standalone p.143). This is effectively a **catch-up correction of a prior-period deferred-tax
  under-provision, expensed through the current year's P&L rather than restated** — it depresses
  FY25 reported PAT/EPS by roughly 3.5% (₹5.17 Cr / ₹147.59 Cr consolidated PAT) and is the primary
  driver of the effective-rate jump above. 🔴 Red Flag — one-time, non-recurring, and not separately
  labelled as an exceptional item anywhere in the P&L; investors modelling forward earnings should
  normalise for it. This also raises a mild question about the historical accuracy of unrealised-gain
  tax provisioning on the private-investment book described in Section 6.
- No MAT credit disclosure — not applicable (company pays regular tax; NOT FOUND / N/A).
- No unrecognised DTA disclosed — NOT FOUND IN DOCUMENT.
- Largest DTA component: accrued employee costs, ₹4.12 Cr closing (consolidated, Note 26 p.197) —
  routine.

---

## 11. REVENUE DETAILS

Standalone Note 18 (p.139-140); Consolidated Note 19 (p.194).

**Consolidated revenue mix, ₹ Cr:**

| | FY25 | FY24 | YoY % |
|---|---|---|---|
| Sale of Hardware | 54.64 | 66.97 | -18.4% |
| Map data & services (royalty/annuity/subscription/MaaS/PaaS/SaaS) | 408.61 | 312.45 | +30.8% |
| **Total revenue from operations** | **463.25** | **379.42** | **+22.1%** |
| — of which Fixed price (POC) | 259.93 | 158.42 | +64.1% |
| — of which Time & material | 203.32 | 221.00 | -8.0% |

- Fixed-price/percentage-of-completion revenue is now **56.1% of total revenue (FY25) vs 41.8%
  (FY24)** — a fast-growing share of revenue is subject to the estimation-heavy POC method that the
  auditor separately flagged as its sole Key Audit Matter (see Section 1). 🟡 Watch — rising
  estimation risk in the revenue base, though no evidence of misstatement is present in the notes.
- **Unbilled revenue (contract assets) more than doubled: ₹9.26 Cr → ₹19.91 Cr (+115%)** (Note 19,
  consolidated p.194) — growing far faster than revenue (+22%), consistent with the growing POC
  mix. 🟡 Watch.
- Remaining Performance Obligations (RPO): **₹1,500.40 Cr (FY25) vs ₹1,372.00 Cr (FY24)**, ~20%
  expected to convert to revenue in the next year (vs 15% guided last year) (Note 19, p.194) — RPO
  is ~3.2x annual revenue, a healthy visibility indicator. 🟢 Clean/positive.
- However: "13% out of performance obligations outstanding as on 31 March 2024 was recognised as
  revenue in the current financial year" (Note 19, p.194) — actual FY25 conversion of the FY24 RPO
  balance (13%) came in **below** both the 15% guided a year earlier and the 20% now guided for
  next year. 🟡 Watch — a modest inconsistency worth a management question on RPO conversion-timing
  realism.
- Contract liabilities (deferred revenue): opening ₹29.70 Cr → billed ₹53.11 Cr → recognised
  ₹(52.93) Cr → closing ₹29.88 Cr (Note 19, p.194) — stable, consistent with a subscription/annuity
  book.
- No single-customer revenue concentration disclosed — NOT FOUND IN DOCUMENT.
- No geographic segment revenue breakdown; company reports a single Ind AS 108 operating segment
  (Note 33, consolidated p.208 / Note 34, standalone p.152). Foreign-exchange earnings/outgo note
  (Note 37, consolidated p.210) is the closest proxy: export earnings (royalty/SaaS) rose ₹86.17 Cr
  → ₹152.89 Cr (**+77.4%**), while import of goods rose ₹14.12 Cr → ₹19.15 Cr (+35.6%) — strong
  international growth alongside rising hardware/IoT import dependency.

---

## 12. OTHER CRITICAL NOTES

- **No separately-labelled exceptional/one-time items** in the P&L, despite the ₹5.17 Cr
  prior-period deferred-tax catch-up (Section 10) functioning as one economically. 🟡 Watch —
  disclosure/labelling gap reduces comparability.
- **Goodwill:** ₹4.34 Cr, static both years (consolidated balance sheet); no impairment-test
  evidence disclosed (Section 1). Low materiality (0.5% of equity).
- **Capital commitments:** NOT FOUND IN DOCUMENT — no dedicated capital-commitments note identified
  in either standalone or consolidated Notes 1-52.
- **Foreign-currency exposure:** small and undedged — net USD exposure ₹6.52 Cr, EUR negligible,
  BND ₹0.91 Cr (consolidated); a 1% INR move affects P&L by ~₹0.07 Cr (Note 29, consolidated p.200).
  No derivatives/hedge accounting disclosed. 🟢 Clean — exposure genuinely immaterial.
- **Segment reporting:** single reportable segment (Note 33/34) — limits investor visibility into
  the economics of the diversifying hardware/IoT (Gtropy) vs core map-data/SaaS businesses. 🟡 Watch
  on disclosure granularity given the genuine business-mix shift evident elsewhere in the notes.
- **Basic vs diluted EPS gap:** consolidated Basic ₹27.05 vs Diluted ₹26.77 (FY25); ₹24.78 vs ₹24.58
  (FY24) (Note 28, p.199) — ~1.0% dilution from ESOP, modest and stable. 🟢 Clean.
- **Events after balance-sheet date:** sale of the Jasola (DLF Tower A) commercial property for
  ₹4.4954 Cr, advance of ₹0.454 Cr received in FY25, registration/completion on 24 April 2025
  post-year-end (Note 49, standalone p.157 / consolidated p.215) — properly disclosed subsequent
  event.
- **CSR:** consolidated required spend ₹2.85 Cr vs actual spend ₹2.77 Cr for the year, but net
  position shows "excess spend during the year ₹0.17 Cr" and "shortfall at year end: nil" after
  applying a ₹0.30 Cr prior-year carryforward (Note 39, consolidated p.210). New this year: **₹0.05
  Cr of FY25 CSR spend was "disallowed due to unavailability of utilisation certificate"** (Note
  39(f), p.210) — a small documentation/compliance gap not present in the FY24 comparative in the
  same form. 🟡 Watch (minor).
- **ESOP dilution:** options outstanding fell from 8,89,365 (FY24) to 5,69,116 (FY25); exercise
  price flat at ₹12.15 throughout; 29,340 new options granted FY25 vs 8,000 FY24, all under the
  legacy 2008-09 scheme (no new scheme created) (Note 32, consolidated p.207-208 / Note 33,
  standalone p.151-152). Outstanding options ≈ 1.0% of shares — low ongoing overhang. 🟢 Clean.
- **Share capital changes:** 3,48,089 new equity shares issued on ESOP exercise during the year
  (Note 12, p.190-191) — routine, no other capital-structure change.
- **No direct debits/credits to reserves bypassing P&L** beyond the standard Ind AS 19 OCI route for
  actuarial gains/losses (net +₹0.55 Cr FY25) and the standard ESOP-reserve-to-securities-premium
  transfer mechanics visible in the Statement of Changes in Equity (p.126-127/180-181). 🟢 Clean —
  properly presented, no earnings-management bypass observed.
- **Dividend:** final dividend of ₹3.50/share proposed for FY25 (~₹19 Cr cash outflow in FY26),
  matching the FY24 proposed dividend (Note 13.1, standalone p.145 / consolidated p.201) — stable
  payout continuity.
- **Financial Ratios note (Note 43) is a relatively strong, proactive disclosure** — SEBI requires
  explanation of any ratio moving >25% YoY, and the company provides one for each triggered ratio
  (p.156-157 standalone, p.213-214 consolidated). Some explanations are thin/circular (e.g. debt
  service coverage: "The company's EBIT has been increased during the year" doesn't really explain
  the *ratio*), but the mechanism itself is a positive transparency signal. 🟢 Clean/positive with
  minor reservation.
- **US subsidiary (CE Info Systems International Inc) continues to be loss-making but improving:**
  contributed ₹(0.58) Cr to consolidated profit FY25 vs ₹(1.04) Cr FY24 (Note 42, net-assets/profit
  share table, consolidated p.211-212).
- **Consolidation contribution table (Note 42, consolidated only, p.211-212) is a standout finding:**
  the standalone parent alone represents **97.05% of consolidated net assets and 100.07% of
  consolidated profit** for FY25; summing all subsidiaries/associates/JV contributions nets to
  roughly *negative* (Gtropy +1.11% of profit, Mappls DT +1.81%, CE Info Intl -0.39%, Kogo -0.73%,
  PT Terra Link JV -1.88%). **Essentially all Group value creation is standalone-entity driven; the
  diversification bets (Gtropy IoT/SaaS, international JV, associate stakes) are currently
  value-neutral-to-dilutive at the consolidated level.** 🟡 Watch — directly relevant to any
  investment thesis resting on diversification/optionality beyond the core mapping/software
  business; these bets are unproven as of FY25.
- **Labelling ambiguity in the consolidation-scope table:** the "Consolidated financial information
  comprises the financial information of member of the group" table (Note 1, consolidated p.172)
  lists Kogo Tech Labs (40.17%) and PT Terra Link (40%) alongside the 100%/75.98% subsidiaries
  without distinguishing that these are equity-method associates/JV, not line-by-line consolidated
  entities. The P&L and Note 42 correctly separate "Share of profit (loss) of associates/JV," so
  this is a disclosure-clarity issue rather than a computational error. 🟡 Watch (minor).

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

Ranked by investor importance (accounting-quality/notes findings only; the FY2023-vs-FY2025
document-mismatch issue is a process flag, not a notes finding, and is called out separately above
and in the eventual YAML `input_gaps`).

| Rank | Finding | Note Anchor | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Prior-period deferred-tax correction of ₹5.17 Cr expensed through FY25 P&L (unprovided tax on unrealised investment gains from earlier years), pushing effective tax rate to 28.24% vs 25.17% statutory | Note 26 consolidated p.197-198 / Note 27 standalone p.143 | 🔴 Red Flag | One-time, ~3.5% of PAT, not labelled as exceptional — distorts YoY earnings comparability; normalise before modelling forward EPS |
| 2 | Trade receivables ECL allowance +117% (₹2.68→₹5.82 Cr) and bad-debt P&L charge +120% (₹1.88→₹4.14 Cr) vs 22% revenue growth | Note 8, Note 23, Note 29 consolidated p.188-189, 196, 201 | 🔴 Red Flag | Receivables quality deteriorating meaningfully faster than the topline — candidate FLAG-CASH |
| 3 | Inventory +76% (₹8.34→₹14.71 Cr) vs 22% revenue growth, driven by finished-goods buildup (+338%) amid an 18% hardware-revenue decline; company itself attributes this to slower hardware sales | Note 7, Note 43 consolidated p.188, 213 | 🟡 Watch | Working-capital quality signal; hardware/IoT demand softness self-disclosed by management |
| 4 | Unbilled revenue (contract assets) +115% (₹9.26→₹19.91 Cr), alongside fixed-price/POC revenue rising from 42% to 56% of total — the sole item flagged by the auditor as Key Audit Matter | Note 19 consolidated p.194; Auditor KAM p.106-107/160-161 | 🟡 Watch | Rising estimation-heavy revenue recognition and unbilled balances increase both earnings-quality and working-capital risk |
| 5 | New JV (PT Terra Link Technologies, Indonesia, 40%, ₹34.98 Cr standalone commitment) immediately loss-making (₹2.82 Cr share of loss in ~4 months); associate Kogo Tech Labs continues losses with board declining further investment | Note 5, Note 44 p.186-187, 214-215; P&L p.168/195 | 🟡 Watch | ~4.4% of consolidated equity deployed into an unproven, currently loss-making venture; capital-allocation discipline question |
| 6 | Consolidation contribution table: standalone parent = 97% of net assets, 100%+ of profit; all subsidiary/associate/JV bets net to roughly value-neutral-to-dilutive | Note 42 consolidated p.211-212 | 🟡 Watch | Directly tests any "diversification optionality" component of the investment thesis — unproven as of FY25 |
| 7 | Fair-value gains on Level-3/illiquid minority investments (+97.5%, ₹13.68→₹27.02 Cr) now ~5.2% of consolidated total income; unquoted investment book +79% (₹56.05→₹100.10 Cr); Indrones reclassified out of associate status the same year its FVTPL carrying value stepped up +124% | Note 5, Note 20, Note 29 consolidated p.186-188, 195, 199-200 | 🟡 Watch | Growing, judgment-driven, non-cash contribution to reported profit; concentration in a fast-expanding venture-style book |
| 8 | Trade payables mix shift: MSME dues -68% (₹11.93→₹3.77 Cr) while other creditors +101% (₹13.13→₹26.44 Cr); no interest on delayed MSME payments (NIL both years) | Note 17, Note 41 consolidated p.193, 211 | 🟢/🟡 | Large, unexplained mix swing worth a management question; MSME compliance itself is clean |
| 9 | Gratuity plan funded at only ~44% (plan assets ₹9.40 Cr vs PBO ₹21.23 Cr); net liability +31% YoY (₹9.03→₹11.83 Cr) | Note 31A consolidated p.206 | 🟡 Watch | Growing unfunded employee-benefit obligation; not unusual for Indian mid-caps but merits monitoring |
| 10 | Balance-sheet strength and disclosure positives: standalone debt-free, consolidated D/E only 3.77%, zero MSME interest defaults, no loans to promoters/KMP, RPO ~3.2x revenue, proactive >25%-variance ratio explanations (Note 43), revenue mix shifting toward higher-margin SaaS/map-data (+31%) away from hardware (-18%) | Notes 43, 46, 41/42(std), 30h/31E, 19 | 🟢 Clean | Meaningful counterweight to the flags above — core balance sheet and revenue-mix trajectory are healthy |
