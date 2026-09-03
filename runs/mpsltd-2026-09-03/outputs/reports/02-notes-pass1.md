# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 (FULL EXTRACTION)
Company: MPS Ltd (MPSLTD) | Run date: 2026-09-03 | Model: claude-sonnet-5
Primary source: Annual Report 2025-26 (56th AR, FY26 notes with FY25 comparatives) —
`runs/mpsltd-2026-09-03/inputs/annual-report/Annual_Report_2022.pdf` (filename is
legacy/misleading; content confirmed FY2025-26).
All figures in INR lacs unless stated. Standalone notes: printed pp.160-227 (Notes 1-52).
Consolidated notes: printed pp.246-311 (Notes 1-51 + Form AOC-1).
Prior-year AR (FY24-25, 55th) available but not needed for this pass; no note required an
earlier comparative than what FY26 AR already carries.

---

## 1. ACCOUNTING POLICIES & CHANGES

- Recent pronouncements (Ind AS 21 lack-of-exchangeability, Ind AS 1 current/non-current
  with covenants, Ind AS 7/107 supplier finance, Ind AS 12 Pillar Two) all adopted/assessed
  1-Apr-2025; company states "no material impact" on financial statements (Note 2.22,
  consolidated p.260-261). 🟢 Clean — standard boilerplate, no quantified impact disclosed
  either way (nothing to quantify per company).
- Depreciation useful lives: domestic PPE follows Schedule II; overseas entities use
  different useful lives (e.g. plant & equipment 3-5 yrs vs Schedule II 3-6/10/15 yrs;
  software 1-10 yrs) (Note 2.3, consolidated p.249-250). 🟡 Watch — a policy divergence
  across geographies within one Group; not disclosed as producing a quantified P&L
  difference.
- Goodwill impairment testing:
  - Standalone (Note 5(a), p.183): sole CGU "Research solutions", carrying value 4,370.12
    (31-Mar-26) vs 3,938.80 (31-Mar-25). Discount rate 18%-19% (FY26) vs 19%-20% (FY25);
    terminal growth 2%-3% both years. Management states no impairment even if WACC +1% and
    terminal growth -1%. 🟢 Clean disclosure, standard sensitivity given.
  - Consolidated (Note 5(a), p.264-266): goodwill by segment — Research 11,954.85 (FY26)
    vs 10,640.57 (FY25); Education 15,639.49 vs 2,414.86 (+547.6%, driven by acquisitions);
    Corporate Learning 10,037.75 vs 11,330.29 (-11.4%, DECREASE). Total goodwill 37,632.09
    (FY26) vs 24,385.72 (FY25), +54.3%. Discount rate 14.50%-19% (FY26) vs 13.20%-22%
    (FY25); terminal growth 1.5%-4% both years. 🔴 Red Flag — see Finding #1 below: the
    Corporate Learning segment goodwill fall of exactly 1,292.54 corresponds to the
    goodwill impairment booked under Exceptional Items (Note 28(c), p.283).
- Revenue recognition: percentage-of-completion (POC) method for fixed-price contracts,
  output method for time-and-material, straight-line for fixed-price maintenance
  (Note 2.9, consolidated p.254-255). Flagged by the statutory auditor as the SOLE Key
  Audit Matter for FY26 (Auditor's Report p.228-229), citing management judgement in
  performance-obligation identification, standalone selling price allocation, and
  variable consideration. 🟡 Watch — heaviest judgement area in the whole filing per the
  auditor's own assessment.
- Ind AS 116 leases: discount rate (incremental borrowing rate) 7.85%-10% p.a. (standalone
  Note 33(ii), p.210; consolidated Note 32(ii), p.289, "1.50% to 10.00%" range shown at
  consolidated level — wider range than standalone, consistent with overseas entities).
  Standalone ROU gross carrying value grew from an opening 288.94 (1-Apr-24 base within
  FY25 column) to 1,754.70 net at 31-Mar-26 via a huge in-year addition of 2,093.27 in
  FY26 alone (Note 4, p.182) — a step-change, not organic. 🟡 Watch — see Finding #4.
- Intangible Assets under Development: DigiCorePro (next-gen publishing workflow
  software) fully capitalised in FY26 — IAUD balance moves from 298.98 (FY25) to Nil
  (FY26) as 330.88 is capitalised (standalone Note 5(b), p.184). No overdue/impaired IAUD
  projects disclosed either year. 🟢 Clean.
- Business combination method: Group applies the "anticipated acquisition method" for
  remaining non-controlling interests and "Pooling of Interest" for common-control
  combinations, with retrospective restatement of comparatives "as if the merger had
  occurred from the beginning of the comparative period" for common-control mergers
  (Note 2.4, consolidated p.250-251). 🟡 Watch — this boilerplate directly concerns the
  pending ADI BPO Services Ltd amalgamation into MPS Limited (Note 48 standalone / 47
  consolidated). See Finding #3 and Question for Management #1: has anything been
  pre-restated ahead of NCLT approval?

## 2. RELATED PARTY TRANSACTIONS (Note 38 standalone, p.218-221; Note 37 consolidated,
p.298-300)

Holding company: ADI BPO Services Limited, 68.34% holding, unchanged both years.

Selected transactions during the year (standalone, ₹ Cr as disclosed in lacs, YoY%):
| Party | Nature | FY26 | FY25 | YoY% |
|---|---|---|---|---|
| ADI BPO Services Ltd | Rentals paid | 243.64 | 211.86 | +15.0% |
| ADI BPO Services Ltd | Infrastructure/electricity | 59.34 | 51.60 | +15.0% |
| ADI BPO Services Ltd | Dividend paid | 5,845.31 | 9,118.68 | -35.9% |
| MPS North America LLC | Rendering of services | 3,737.81 | 434.24 | +761% |
| Semantico Limited | Rendering of services | 798.65 | 866.03 | -7.8% |
| American Journal Experts LLC | Rendering of services | 575.54 | Nil | new |
| MPS North America LLC | Reimbursement of expenses paid | 74.16 | 24.62 | +201% |
| MPS North America LLC | Interest income on loan | 130.90 | 261.44 | -49.9% |
| MPS North America LLC | Investment in subsidiary | 8,876.62 | Nil | new |
| MPS North America LLC | Loan given | 1,749.69 | Nil | new |
| MPS Interactive Systems Ltd | Repayment of loan incl. interest | 328.75 | 875.00 | -62.4% |
| MPS North America LLC | Repayment of loan incl. interest | 1,040.78 | 1,540.36 | -32.4% |

🔴 Red Flag / material finding: "Rendering of services" to MPS North America LLC jumped
761% YoY (434.24 → 3,737.81, Note 38(b) item 5, p.219). Combined with services to AJE
LLC (new, 575.54) and Semantico (798.65), total intercompany services billed by the
standalone entity ≈ 5,111.99, or 11.7% of standalone revenue (43,825.57). This
intercompany recharge growth materially explains why standalone revenue grew 24.7% YoY
while consolidated (eliminated) revenue grew only 5.7% YoY — see Finding #2.

- KMP remuneration: Mr Rahul Arora (Chairman & CEO), short-term benefits 685.97 (FY26) vs
  465.99 (FY25), +47.2%. 🟡 Watch — notable step-up in CEO cash compensation.
- Loans to related parties (Note 7, p.186): non-current 1,839.80 (FY26) vs 1,066.93
  (FY25); current 710.91 vs 796.62; total to MPS North America LLC 2,550.71 (FY26) vs
  1,538.55 (FY25), funding the Unbound Medicine and AJE Group acquisitions, at "interest
  rate as per India Safe Harbour Rules" (exact % NOT FOUND IN DOCUMENT).
- Security deposit paid to ADI BPO Services Limited (Holding Company) for premises/
  infrastructure (Note 8(i) footnote, p.186 and Note 37 footnote, p.299): 82.88 (FY26)
  vs 100.00 (FY25).
- New related party this year: American Journal Experts LLC, North Carolina; Semantico
  Limited transactions scaled materially; American Journal Online (Beijing) entity
  referenced under Note 38(a) subsidiary list but no direct RPT transaction line shown for
  it standalone.
- Non-arm's-length signal: none flagged by the company; standard boilerplate states
  "transactions with related parties are made on terms equivalent to those that prevail
  in arm's length transactions" (Note 38, p.220; Note 37, p.299).
- RPT as % of standalone revenue: services rendered to related parties (≈5,112) = 11.7%
  of revenue (43,825.57); this is a meaningful share of top-line derived from
  intercompany recharges, a normal feature of a holding/operating structure but relevant
  to interpreting standalone revenue growth quality.

## 3. CONTINGENT LIABILITIES (Note 39 standalone, p.221; Note 38 consolidated, p.301)

| Nature | FY26 | FY25 | % of net worth (FY26) |
|---|---|---|---|
| Income tax disputes, not acknowledged as debt | 403.76 | 377.02 | 1.01% (standalone); 0.68% (consolidated) |

Standalone net worth = 1,710.58 + 38,124.76 = 39,835.34. Consolidated net worth =
1,710.58 + 57,922.18 = 59,632.76. No single item exceeds 10% of net worth. 🟢 Clean,
immaterial in size.

- EPF Supreme Court judgment (28-Feb-2019) on inclusion of allowances in "basic wages"
  for PF computation: company recognised a provision for PF contribution "on the basis
  of above mentioned order with effect from the order date" but the standalone/
  consolidated notes do NOT disclose the rupee amount of this provision (Note 39(ii)
  standalone p.221; Note 38(ii) consolidated p.301). 🟡 Watch — unquantified provision,
  management asserts impact "should not be material." NOT FOUND IN DOCUMENT: quantum.
- No guarantees issued for subsidiaries are disclosed as a contingent liability item
  (the MPSi stake-acquisition obligation is a recognised financial liability, not a
  contingent one — see Section 6).

## 4. TRADE RECEIVABLES

Standalone (Note 11, p.188-189):
- Total (net) 8,696.65 (FY26) vs 7,592.82 (FY25), +14.5%.
- Receivables from subsidiaries: 1,938.90 (FY26) vs 725.23 (FY25), +167.4%.
- Ageing FY26: >6 months bucket (6mo-1yr+1-2yr+2-3yr+>3yr) = 15.11+0.03+0+0 = 15.14 of
  8,751.01 gross = 0.17%. FY25: >6 months = 102.83 of 7,640.79 = 1.35%. Improving.
- ECL allowance 54.36 (FY26) vs 47.97 (FY25), +13.3%, tracking receivables growth
  (+14.5%) — adequate coverage, no standalone-level deterioration signal.
- Trade Receivable Turnover Ratio (Note 51) 5.35x (FY26) vs 5.60x (FY25), -4.46%,
  i.e. days sales outstanding lengthened from ~65.2 to ~68.2 days. Company/auditor labels
  this "not applicable, variation within 25% threshold." 🟡 Watch — mild deterioration,
  immaterial per the company's own threshold.
- Customer concentration: revenue from top 3 customers (each >10% individually) =
  17,105.50 = 39.0% of standalone revenue (FY26) vs top 2 customers = 10,584.85 = 30.1%
  (FY25) (Note 35(ii), p.214). Top 15 customers = 34,529.48 = 78.8% of revenue. 🟡 Watch —
  high and rising customer concentration at standalone level.

Consolidated (Note 11, p.270-271; Note 34, p.294):
- Total (net) 13,347.56 (FY26) vs 11,658.31 (FY25), +14.5%.
- ECL allowance 429.85 (FY26) vs 317.36 (FY25), +35.4% — growing much faster than gross
  receivables (+15.0%). 🔴 Red Flag — ECL coverage on the >180-days bucket rose from
  71.5% (263.89/369.25, FY25) to 90.8% (374.52/412.38, FY26), i.e. management became
  materially more conservative on aged receivables at the consolidated (subsidiary)
  level even though the >180-day bucket itself barely moved as a % of total (2.19% →
  2.10%). This coincides with the AJE Group policy change on writing off customer
  advances disclosed in Exceptional Items (Note 28(e), p.283: "written back INR 1,394.96
  lacs pursuant to change in policy w.r.t. write of advances from customer in AJE
  Business to align policy with market conditions/competition").
- Consolidated-only ageing category "Undisputed — significant increase in credit risk"
  totals 256.54 (FY26) across buckets (p.270) — this category is entirely zero at
  standalone level. 🟡 Watch — subsidiary-level credit-risk deterioration invisible in
  the standalone accounts.
- Top customer concentration consolidated: 1 customer = 13,317.26 = 17.3% of revenue
  (FY26) vs 1 customer = 13,514.08 = 18.6% (FY25) (Note 34(ii), p.294) — mild
  improvement at group level, contrasting with the standalone worsening above.

## 5. INVENTORY

NOT FOUND IN DOCUMENT — no inventory note present. MPS Ltd is a knowledge-services
company (no manufacturing/goods inventory); absence is consistent with the business
model, not a disclosure gap. 🟢 N/A.

## 6. INVESTMENTS

Standalone non-current investments (Note 6(i), p.185):
| Subsidiary | FY26 | FY25 | YoY% |
|---|---|---|---|
| MPS North America LLC (78,582 units of USD 100, up from 66,500) | 13,134.01 | 4,257.40 | +208.6% |
| MPS Interactive Systems Limited | 6,093.66 | 6,095.01 | -0.02% |
| TOPSIM GMBH | 599.18 | 599.18 | flat |
| MPS Europa AG | 810.39 | 810.39 | flat |
| Deemed investment (ESOP to subsidiary employees) | 19.19 | 15.52 | +23.7% |
| **Total** | **20,656.43** | **11,777.50** | **+75.4%** |

The MPS North America LLC increase (+8,876.62) funds the Unbound Medicine, Inc.
acquisition (100% stake, USD 16.50 million consideration, completed 09-Feb-2026 —
Note 40(a) consolidated, p.301-302).

- No impairment recognised on any standalone subsidiary investment; management assessed
  recoverable amount via value-in-use/fair value and concluded no provision required
  (Note 6(i) footnote, p.185). 🟢 Clean at standalone level.
- 🔴 Red Flag (cross-referenced, see Finding #1): at the CONSOLIDATED level, Exceptional
  Items (Note 28(c), p.283) records an "Impairment loss on Goodwill" of 1,292.54 for
  FY26, which the segment goodwill roll-forward (Note 5(a)) shows sits entirely in the
  Corporate Learning CGU (goodwill fell 11,330.29 → 10,037.75, a fall of exactly
  1,292.54). This is the SAME segment where MPSi (the subsidiary holding Corporate
  Learning/Liberate Group) just completed 100% buy-out of Liberate Group and admitted a
  new equity investor.
- Derivative asset — "Derivative Asset towards further stake acquisition in subsidiary"
  (standalone Note 8(i), p.186; fair value Note 34, p.211-212): 112.43 (FY26) vs Nil
  (FY25). Level 3, Monte Carlo simulation. Sensitivity: a ±1% move in equity value swings
  the asset value by ±112.34/112.51 — i.e. essentially 100% of the asset's own value.
  🟡 Watch — high estimation uncertainty embedded in a Level 3 instrument tied to the
  MPS Interactive Systems Limited (MPSi) Share Subscription and Shareholders Agreement
  (SSSHA) dated 10-Oct-2025 with Mr Rodney Charles Beach (Australian resident investor),
  who invested 874 lacs via preferential allotment into MPSi and — per Note 28(d)
  consolidated (p.283) — "has assumed the role of President of Corporate Learning." This
  places a new external equity partner as segment head of Corporate Learning in the same
  year that segment's goodwill was impaired.
- Loans/ICDs: Loan to MPS Interactive Systems Limited (10.50% p.a., granted FY24 for
  Liberate Group acquisition) fully repaid in FY26 (Note 44(b), p.223); outstanding
  Nil (FY26) vs 325.00 (FY25).
- Current investments (mutual funds, FVPL): standalone 1,637.01 (FY26) vs 1,847.85
  (FY25); consolidated 2,465.91 (FY26) vs 2,146.65 (FY25). No unrealised losses of
  concern; routine liquidity parking. 🟢 Clean.

## 7. BORROWINGS (Note 14 standalone, p.194; Note 14 consolidated, p.276-277)

- FIRST-EVER borrowing for the company: secured term loan from ICICI Bank Limited,
  facility of 4,200 (drawn 4,025: 2,975 non-current + 1,050 current maturities),
  availed 06-Feb-2026, rate = I-MCLR-1M, 4-year tenure, obtained specifically "for equity
  infusion in MPS North America LLC for acquisition of Unbound Medicine Inc." Security:
  charge over current assets and movable fixed assets.
- Covenants: DSCR, Total Debt/EBITDA, Total Debt/Tangible Net Worth (standalone); at
  consolidated level, Total Debt/Net Worth ratio substituted for Tangible Net Worth
  ratio. Company states full compliance, no breach or waiver either level.
- 🟡 Watch — structural balance-sheet change: the company converts from a fully
  net-cash entity (Debt-Equity ratio "NA," no debt, FY25) to net debt of 1,618.90
  standalone (Gearing ratio 4.06%, Note 36) / Debt-Equity 0.11x (Note 51). Not a red
  flag per se (funds a strategic acquisition) but a first for the company and worth
  monitoring against the newly-instituted covenants.
- Fair value of borrowings ≈ carrying value, 4,025 (Note 34(h), p.213), DCF-based.

## 8. TRADE PAYABLES

Standalone (Note 17, p.198): total 1,436.82 (FY26) vs 1,350.48 (FY25), +6.4%. MSME dues
45.20 (FY26) vs 38.94 (FY25). No disputed dues either category. Payable Turnover Ratio
5.89x (FY26) vs 5.98x (FY25), -1.51%, broadly stable.

🟡 Watch — MSME interest: "amount of interest accrued and remaining unpaid at the end
of the year" and "amount of further interest remaining due... in succeeding years" are
BOTH static at 0.31 for FY26 and FY25 (Note 31(iv)/(vi), p.204). An unmoving 0.31 legacy
MSME interest balance across two years suggests an old, unresolved item rather than
current-year MSME delay.

Consolidated (Note 17, p.276): total 4,265.31 (FY26) vs 2,545.45 (FY25), +67.6% — a much
sharper increase than standalone, driven by trade payables assumed on the Unbound
Medicine (1,645.73) and AJE Group true-up (1,108.79) acquisitions (Note 40(a)/(b)). MSME
dues consolidated: 94.23 (FY26) vs 64.96 (FY25).

## 9. PROVISIONS

- Gratuity (standalone Note 32(b), p.205-207): present value of obligation jumped
  1,064.23 (FY25) → 1,681.79 (FY26), +58.0%, driven by past service cost of 541.51
  (vs a credit of -89.99 in FY25). Net liability recognised in balance sheet 699.92
  (FY26) vs 93.21 (FY25) (Note 20, p.199).
- Compensated absences (standalone Note 32(c), p.208): net PVO 41.37 (FY25) →
  280.79 (FY26), +578.9%. Gross obligation 491.91 (FY25) → 799.49 (FY26), +62.5%.
- 🟡 Watch, but well-explained: both increases are tied to a disclosed, dated,
  non-recurring cause. On 21-Nov-2025 the Government of India notified the Labour Codes
  (Wages, Industrial Relations, Social Security, Occupational Safety codes). The company
  recognised, as an Exceptional Item, an incremental impact of gratuity of 450.16 and
  long-term compensated absences of 161.14 (Note 28, p.202, standalone; total exceptional
  charge 611.30 standalone / 701.44 consolidated). This is transparently disclosed as
  one-time and attributable to regulatory change, not deteriorating employee-cost
  management. 🟢 rated for disclosure quality, 🟡 for the magnitude of the balance-sheet
  swing.
- Consolidated-only "Provision towards future service obligation": 20.51 non-current +
  163.12 current (Note 16, p.277). No equivalent line in standalone Note 20 — this is a
  subsidiary-specific provision whose nature is NOT FOUND IN DOCUMENT (label only, no
  narrative given).
- No warranty, decommissioning, or onerous-contract provisions found (consistent with a
  services business model). No litigation provisions beyond the income-tax contingent
  liability in Section 3.

## 10. DEFERRED TAX (Note 29 standalone, p.202-203; Note 18 consolidated, p.278-279)

- Standalone effective tax rate: FY26 = 4,167.82/16,893.72 = 24.67%; FY25 =
  3,516.13/14,516.09 = 24.22%, vs statutory 25.168% both years. Key reconciling items:
  exempt dividend income (-292.89 FY26 / -329.79 FY25), state tax on USA operations
  (3.90 / 15.14), and an unexplained "Others" bucket of 85.09 (FY26) / 132.70 (FY25).
  🟡 Watch — the "Others" residual is ~0.5-0.9% of PBT and not itemised.
- Standalone net DTL: 179.12 (FY26) vs 234.65 (FY25) — small net liability, no MAT
  credit disclosure found (NOT FOUND IN DOCUMENT, consistent with no MAT applicability
  disclosed).
- Consolidated DTA on carry-forward business losses jumped 19.77 (FY25) → 649.80 (FY26),
  of which 644.34 arose from "Assets acquired in Business Combination" (Note 18, p.278).
  🟡 Watch — DTA recognised on acquired entities' brought-forward tax losses; realism
  depends on future profitability of Unbound Medicine/AJE Group, which the notes
  describe as currently profitable on a stub-period basis (Unbound Medicine PAT 171.42
  for 10-Feb-26 to 31-Mar-26; AJE Group reported a LOSS after tax of 134.77 for its
  stub period in the prior acquisition, Note 40(b), p.303) — mixed picture, warrants a
  management question (see Q4).

## 11. REVENUE DETAILS

- Standalone revenue (Note 22, p.198-199 / Note 45, p.223-224): 43,825.57 (FY26) vs
  35,133.52 (FY25), +24.7%. Exports 43,720.16 (99.76% of revenue); Domestic 105.41.
  Segment split: Research solutions 30,532.17 (+20.6%), Education solutions 13,293.40
  (+35.4%).
- Consolidated revenue (Note 22, p.281; Note 43, p.305): 76,836.38 (FY26) vs 72,688.85
  (FY25), +5.7% — much slower than standalone's +24.7%. 🔴 Red Flag / material finding
  (Finding #2): the divergence is explained by the intercompany services recharge
  documented in Section 2 (standalone billing MPS North America LLC 3,737.81, up from
  434.24) which is eliminated on consolidation. Consolidated segment detail:
  Research 46,351.09 (+1.05%), Education 20,890.03 (+36.3%), **Corporate Learning
  9,595.26 (-16.5%)** (Note 43(ii)/36, p.297, 305). Corporate Learning segment RESULTS
  (profit) fell even harder: 1,130.76 (FY26) vs 1,999.77 (FY25), -43.4% (Note 36(i),
  p.297). This is the segment carrying the goodwill impairment noted in Section 6.
- Contract balances (standalone Note 45(iii), p.224; consolidated Note 43(iii), p.306):
  standalone contract assets 3,577.74 → 4,074.89 (+13.9%); contract liabilities 1,488.42
  → 1,636.12 (+9.9%). Consolidated contract liabilities 9,879.25 → 12,296.98 (+24.5%),
  growing faster than contract assets 4,882.62 → 5,830.05 (+19.4%) — deferred revenue
  building faster than unbilled revenue at group level, a mildly positive cash-flow
  signal (customers pre-paying more). 🟢 Clean/positive.
- No disclosed unsatisfied performance obligations >1 year (practical expedient taken,
  Note 45(vi) standalone / 43(vi) consolidated).

## 12. OTHER CRITICAL NOTES

- Exceptional items (Note 28 standalone p.202; Note 28 consolidated p.283):
  - Standalone: Labour Code impact 611.30 (FY26); Nil (FY25).
  - Consolidated FY26: Employee severance (AJE restructuring) -209.42; Labour Code
    impact -701.44; Impairment loss on Goodwill -1,292.54; Liability written back
    +2,967.64 (comprising Liberate deferred-consideration reversal +591.07 and AJE
    customer-advances policy-change write-back +1,394.96, plus other items). **Net
    exceptional GAIN of 764.24 (FY26) vs a net gain of 591.07 (FY25).**
  - 🔴 Red Flag / material finding (Finding #5): exceptional items have been a NET
    POSITIVE contributor to consolidated pre-tax profit in BOTH FY25 and FY26, driven
    substantially by liability/provision write-backs rather than genuine one-off costs.
    A "below the line, exceptional" bucket that recurringly nets positive across
    consecutive years is a pattern investors should treat cautiously — it can mask
    underlying operating performance and raises the question of whether provisions were
    conservatively over-stated in earlier periods and released now.
- Audit trail (edit log) qualification (Note 47 standalone, p.225; Note 46 consolidated,
  p.308): both standalone and consolidated financial statements disclose that "the
  audit trail (edit log) features for any direct changes made at the database level
  were not enabled for the accounting software" during the year, though application-level
  edit logs were operative and independently retained. 🟡 Watch — an IT-control
  disclosure gap, common across Indian filers post the CARO/Rule 3(1) mandate, but a
  genuine (if industry-wide) governance flag.
- Amalgamation in progress (Note 48 standalone, p.225; Note 47 consolidated, p.308):
  Board approved a draft Scheme of Amalgamation on 18-Jul-2025 to merge ADI BPO Services
  Limited (the Holding Company, post demerger of its infrastructure-management and
  investing undertakings) into MPS Limited under Sections 230-232 of the Companies Act.
  Stock Exchange No Objection received 02-Mar-2026; filed before NCLT Chennai
  17-Apr-2026; hearing pending as of the report date (15-May-2026). No financial impact
  yet recognised. 🟡 Watch — major pending related-party corporate action; combined
  with the accounting policy for common-control mergers (Section 1) requiring
  retrospective comparative restatement once effective, this deserves a dedicated
  question to management (Q1).
- Intangibles amortisation trajectory: standalone amortisation on intangibles FELL from
  538.43 (FY25) to 267.26 (FY26) (Note 26, p.200) even as the intangible base grew;
  consolidated amortisation also fell slightly, 1,862.37 → 1,717.43 (Note 26, p.283),
  despite the Unbound Medicine and AJE Group intangibles additions (customer
  relationships, trademarks) recognised mid-year. 🟡 Watch, forward-looking: only a
  partial year of amortisation on newly acquired intangibles has hit FY26 P&L (Unbound
  Medicine from 09-Feb-2026 only, ~7 weeks); a materially larger amortisation charge
  should be expected in FY27 once acquired intangibles amortise for a full year.
- CSR (Note 41 standalone, p.221-222): required 265.34 (FY26) vs 232.49 (FY25); spent
  266.00 vs 234.00 — fully compliant, no shortfall either year. 🟢 Clean.
- EPS dilution (Note 30 standalone, p.204; Note 30 consolidated, p.284): basic 75.01 vs
  diluted 74.98 (standalone, FY26) — minimal dilution (7,822 shares). Consolidated basic
  and diluted EPS are IDENTICAL at 102.11/102.06 (both years) — the consolidated note
  states "Earnings per share — basic & diluted" as one combined line, meaning the
  dilutive ESOP effect is treated as immaterial/anti-dilutive at group level despite
  being separately quantified at standalone level. 🟡 Watch — mild internal
  inconsistency in presentation between standalone and consolidated EPS notes worth a
  cross-check.
- Foreign currency translation reserve (OCI): standalone 587.74 → 934.30 (+59.0%);
  consolidated 2,843.06 → 5,739.89 (+101.9%) (Note 13(ii)(h)/(i)). Large FX translation
  gain flowing through OCI/equity, driven by INR depreciation against a growing USD/EUR/
  GBP-denominated net asset base post-acquisitions. 🟢 Legitimate translation mechanics,
  not P&L manipulation, but material in size and worth noting given the "largely USD
  revenue" profile.
- Events after balance sheet date (Note 49 standalone, p.225; Note 48 consolidated,
  p.308): 5th ESOP grant of 79,009 options approved 04-May-2026 by NRC, before the
  15-May-2026 report date. Properly disclosed subsequent event. 🟢 Clean.
- Share capital / promoter holding: ADI BPO Services Limited holds 68.34% both years,
  unchanged (Note 13(i)(e)). No pledge disclosure in these notes (expected; pledge is a
  shareholding-pattern disclosure, not an AR note item). 🟢 Clean.
- Benami property, crypto/virtual currency, struck-off company dealings, undisclosed
  income in tax proceedings — all Nil/none per "Other Statutory Information" (Note 52
  standalone, p.227; Note 51 consolidated, p.310). 🟢 Clean.
- No qualified audit opinion; same statutory auditor (Walker Chandiok & Co LLP) and
  signing partner (Rohit Arora) both years, both levels. 🟢 Clean.

---

## PASS 1 SUMMARY — TOP 10 MOST SIGNIFICANT FINDINGS

1. **Corporate Learning segment goodwill impairment of 1,292.54 coincides exactly with
   an 11.4% goodwill decline in that CGU, a 16.5% revenue decline, and a 43.4% profit
   decline in the same segment** — and coincides with MPSi's 100% buyout of Liberate
   Group plus admission of a new external equity partner (Mr Rodney Charles Beach) who
   was installed as President of Corporate Learning the same year. (Note 28(c)/(d) and
   Note 36, consolidated, pp.283, 297) 🔴 Red Flag — highest-priority cross-note pattern.

2. **Standalone revenue grew 24.7% YoY vs only 5.7% at consolidated level**, explained
   by a 761% surge in intercompany "rendering of services" billed to MPS North America
   LLC (434.24 → 3,737.81), eliminated on consolidation. Standalone revenue growth is
   materially inflated by intercompany recharges relative to true group organic growth.
   (Note 38(b), p.219; Note 22, pp.198, 281) 🔴 Red Flag.

3. **Consolidated ECL allowance on trade receivables grew 35.4% (317.36 → 429.85) while
   gross receivables grew only 15.0%**, with >180-day-bucket coverage rising from 71.5%
   to 90.8%, coinciding with a subsidiary (AJE) policy change on writing off customer
   advances. A new "significant increase in credit risk" ageing category (256.54)
   exists only at consolidated level, invisible in standalone accounts. (Note 34, p.294;
   Note 28(e), p.283) 🔴 Red Flag.

4. **Exceptional items have been a net POSITIVE contributor to consolidated pre-tax
   profit in both FY25 (+591.07) and FY26 (+764.24), driven substantially by liability
   and provision write-backs**, not genuine one-off costs. A recurring pattern of
   positive "exceptional" items warrants scrutiny of whether prior-period provisioning
   was conservative and is now being released into profit. (Note 28, p.283) 🔴 Red Flag.

5. **The company took on its first-ever borrowing** (4,025 secured term loan from ICICI
   Bank) to fund the Unbound Medicine, Inc. acquisition, converting from a net-cash to a
   net-debt company for the first time, with new financial covenants (DSCR, Debt/EBITDA,
   Debt/Net Worth) now in force. (Note 14, p.194) 🟡 Watch.

6. **Goodwill and other intangibles grew 54.3%/54.8% at consolidated level** on the back
   of the Unbound Medicine (09-Feb-2026) and AJE Group acquisitions, but amortisation
   expense on intangibles actually FELL slightly in FY26 — a full year of amortisation
   on the newly acquired intangibles has not yet hit the P&L; expect a step-up in FY27.
   (Note 5, pp.264-267; Note 26, p.283) 🟡 Watch, forward-looking.

7. **Gratuity and compensated-absence obligations swelled sharply** (gratuity PVO
   +58.0%, compensated absences net liability +578.9% standalone) due to the newly
   notified Labour Codes (21-Nov-2025), transparently disclosed as a one-time,
   non-recurring Exceptional Item (611.30 standalone / 701.44 consolidated). Well
   explained, but a material balance-sheet swing to track for FY27 continuation. (Note
   32, pp.205-208; Note 28, p.202) 🟡 Watch.

8. **Standalone customer concentration is high and rising**: top 3 customers = 39.0% of
   revenue (FY26) vs top 2 = 30.1% (FY25); top 15 = 78.8% of revenue. Consolidated
   concentration is milder and improving (top 1 customer 17.3% vs 18.6%). (Note 35(ii),
   p.214; Note 34(ii), p.294) 🟡 Watch.

9. **Both standalone and consolidated financial statements disclose an audit-trail
   (edit log) control gap** at the database level of the accounting software during
   FY26, though application-level logs were retained. (Note 47/46, pp.225, 308)
   🟡 Watch — governance/IT-control disclosure, industry-wide pattern.

10. **A major related-party corporate restructuring is in progress and unresolved**:
    the Board-approved amalgamation of holding company ADI BPO Services Limited into
    MPS Limited is pending NCLT Chennai approval, with an accounting policy on the books
    (Note 2.4) requiring retrospective comparative restatement for common-control
    mergers once effective — no financial impact recognised yet, but a significant
    structural event to track into FY27. (Note 48/47, pp.225, 308; Note 2.4, p.250-251)
    🟡 Watch.
