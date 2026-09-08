# IEX — Stage 2 Notes Triple-Pass — PASS 1 (FULL EXTRACTION)

Run date: 2026-09-08. Source: `runs/iex-2026-09-08/work/annual-report__Annual_Report_2026.txt`
(FY2025-26 Annual Report, filed to BSE 14-Aug-2026, board-approved 23-Apr-2026).
Comparative-year source available at `annual-report__Annual_Report_2025.txt` but not
required this pass (FY26 AR carries full FY26-vs-FY25 comparatives in every note).
All native figures are in ₹ Lakhs as printed; ₹Cr conversions shown alongside (÷100).

Coverage: Standalone notes 1-54 (pages 185-230) in full, Consolidated notes 1-55
(pages 231-293) in full, including both Statements of Profit & Loss, both Balance
Sheets, both Cash Flow Statements, both Statements of Changes in Equity, and the
Annexure I internal-financial-controls audit report.

═══════════════════════════════════════════════════════════
LOAD-BEARING FACTS — ANSWERED FIRST
═══════════════════════════════════════════════════════════

**1. Revenue disaggregation by market segment.**
CONTRADICTS Stage 1's finding of "no split found anywhere." A disaggregation
EXISTS but it is coarser than DAM/RTM/TAM/green/certificates: transaction fee
revenue is split only two ways — "Electricity (comprising RTM, DAM, TAM, Green
Segments)" and "Certificates (comprising REC, ESCerts Segments)." Standalone:
Electricity ₹55,851.37L / ₹558.51cr (FY26) vs ₹47,833.81L / ₹478.34cr (FY25);
Certificates ₹2,545.07L / ₹25.45cr (FY26) vs ₹3,520.71L / ₹35.21cr (FY25)
(Note 28, Annual Report FY26 p.211). Identical split appears in the Consolidated
Note 27 (Annual Report FY26 p.273) because the split is applied to transaction
fees, which are IEX-only (ICX contributes membership/processing and I-REC fees
separately, see below). Certificates revenue FELL 27.7% YoY while Electricity
grew 16.8% — a mix shift the P&L headline does not show. 🟡
Separately, Note 44/Ind AS 108 (standalone p.220, consol p.286) confirms Stage
1: the CODM reviews the business as ONE operating segment; no segment note
exists beyond this two-way product disaggregation inside the revenue note. 🟢

**2. Other income composition.**
RESOLVED WITH EXACT RECONCILIATION. The Data_Sheet screener figure of ₹151.10cr
"other income" against FY26 PBT of ₹645.56cr is the SUM of two distinct P&L
lines that the consolidated accounts keep separate:
  - Note 28, Consolidated Other Income = ₹13,130.47L = **₹131.30cr** (Annual
    Report FY26 p.273). Composition: interest income from bank deposits
    ₹5.09cr, interest income on investments at amortised cost ₹57.51cr, gain
    on sale of amortised-cost investments ₹8.09cr, FV gain on FVTPL
    investments ₹34.15cr, gain on sale of FVTPL investments ₹23.31cr,
    dividend income ₹0.05cr (near-zero — see note below), business support
    services ₹0.31cr, miscellaneous ₹2.56cr. ALL of this is treasury /
    investment-book income. None of it is operating (transaction-fee) income.
  - "Share in profit of associate (net of tax)" = ₹1,979.53L = **₹19.80cr**
    (Note 54, Annual Report FY26 p.291), IEX's 47.28% equity-method pickup of
    IGX's profit. This line sits BELOW "Total expenses" in the consolidated
    P&L, not inside Other Income — it is disclosed on its own line: "Profit
    before share of profit of associates and tax" ₹625.77cr, plus "Share in
    profit of associate" ₹19.80cr, equals PBT ₹645.56cr (Annual Report FY26
    p.238, Consolidated Statement of Profit and Loss).
  ₹131.30cr + ₹19.80cr = **₹151.10cr**, matching the screener figure to the
  rupee. Confirms Stage 1's hypothesis precisely, with exact anchors. 🟢
  Standalone Other Income (Note 29, p.211) is ₹136.55cr, ₹5.25cr HIGHER than
  consolidated, almost entirely because standalone recognises ₹5.37cr dividend
  income from IGX directly (IGX is carried at cost in standalone accounts,
  Note 6), while consolidated correctly ELIMINATES this dividend and instead
  nets the ₹5.32cr IGX distribution against the equity-method carrying value
  (Note 54 reconciliation, p.291: "Distribution received from IGX (531.90)").
  This is clean, correct equity-method accounting — no double-count. 🟢
  Net effect on EPS interpretation: of FY26 consolidated PBT ₹645.56cr,
  treasury other income is ₹131.30cr (20.3%) and the IGX equity pickup is
  ₹19.80cr (3.1%) — together 23.4% of PBT is non-operating. Operating PBT
  (Total Income from operations less Total Expenses, i.e. before Other Income
  too) requires netting further; at minimum the two identified non-operating
  lines total ₹151.10cr of ₹645.56cr PBT.

**3. IGX — carrying value, stake, accounting treatment, OFS.**
  - Shareholding: **47.28%**, disclosed repeatedly (Note 54, p.291; also in
    front-matter business narrative pp.5, 9).
  - Accounting treatment: **Associate, equity method** in consolidated
    accounts (Note 54, "Investment accounted for using the equity method,"
    p.291). In STANDALONE accounts IGX is carried **at cost**, ₹3,546.00L =
    **₹35.46cr**, unchanged both years (Note 6, p.193; also Note 41 fair value
    table, p.214, confirms "Investments in Equity of associate... At Cost").
  - Consolidated carrying value (equity method): opening ₹7,574.70L, plus
    share of PAT ₹1,979.53L, less distribution received ₹(531.90)L, plus
    share of OCI ₹2.76L, closing **₹9,025.09L = ₹90.25cr** as at 31-Mar-2026
    (Note 54, p.291). Prior year closing was ₹75.75cr — the carrying value
    grew 19.2% YoY purely from retained equity pickup, not fresh investment.
  - IGX's own FY26 PAT (100% basis, per the reconciliation) implies ~₹41.9cr
    (₹19.80cr ÷ 47.28% = ₹41.87cr), consistent with the narrative section
    elsewhere in the AR citing IGX PAT of ₹41.9cr — this cross-check is
    OUTSIDE the notes (business review section) and is cited here only as a
    consistency check, not as an anchored notes finding.
  - Schedule III breakdown (Note 55, p.292): IGX represents 4.02% of
    consolidated net assets (₹54.79cr) and 4.02% of consolidated profit
    (₹19.80cr) for FY26.
  - **OFS / planned stake dilution: NOT FOUND IN THE NOTES TO THE FINANCIAL
    STATEMENTS.** Note 54 discloses only the % holding, accounting method,
    and carrying-value roll-forward. No note anywhere in standalone or
    consolidated notes (including Note 52/45 Related Party Disclosures,
    Note 53/47 Additional Disclosures/CERC note, or an "events after the
    reporting date" note — no dedicated subsequent-events note exists in
    either note set) discusses the PNGRB-mandated dilution to 25%, the IGX
    IPO, or an Offer for Sale. This information is present ELSEWHERE in the
    Annual Report (front-matter business review, pp.48-49, outside the notes
    to financial statements and therefore outside this pass's mandate per
    the pipeline instruction). 🟡 FLAG for stage 3/synthesis: a shareholding
    dilution this consequential to a ₹90.25cr carrying asset and to future
    equity-pickup income has ZERO financial-statement note disclosure —
    worth checking whether it clears the Ind AS 10 subsequent-events
    threshold (board approval was 23-Apr-2026; if the OFS timeline firmed up
    only after that date, non-disclosure in the notes is technically
    defensible, but the notes give no indication either way).
  - ICX (the other consolidated entity) is 100% subsidiary (Note 6, p.193:
    5,000,000 shares of ₹10 each, ₹500.00L = ₹5.00cr cost, unchanged both
    years), fully consolidated line-by-line (not equity method).

**4. Settlement, margin and member-deposit balances — cash flow float.**
  RESOLVED (mechanism) for FY26/FY25; FY23 NOT FOUND IN THIS DOCUMENT (this AR
  carries only FY26 and FY25 comparatives; FY23 sits in an AR not in this
  run's corpus). The mechanism is fully evidenced:
  - Balance sheet "Other financial liabilities - Current" (Note 24 standalone
    /23 consolidated, p.210/p.268) is dominated by "Settlement obligation
    payable" ₹75,313.88L = ₹753.14cr and "Trading margin deposits" ₹17,126.35L
    = ₹171.26cr — together ₹924.40cr of the company's ₹974.68cr current
    "other financial liabilities," i.e. these ARE the balance sheet, not a
    manufacturer's payables.
  - Cash flow statement line "Increase in trade payables, other financial
    liabilities, provisions and other liabilities" is the conduit: FY26
    ₹1,180.77L (standalone) / ₹1,198.59L (consol) = ~₹11.8-12.0cr, but FY25
    was ₹25,616.12L (standalone) / ₹25,651.48L (consol) = **~₹256.2cr**
    (Note: Standalone Cash Flow Statement, p.183; Consolidated Cash Flow
    Statement, p.244). This single float-timing line swung by ~₹244cr
    year-on-year while PAT moved only ~₹6cr — this is the mechanism that can
    take CFO far above or far below PAT in any given year purely on
    settlement/margin timing, independent of earnings quality. 🟡
  - FY26 and FY25 CFO were BOTH strongly positive and close to PAT (FY26
    consolidated CFO ₹432.77cr vs PAT ₹492.92cr = 87.8% conversion; FY25 CFO
    ₹427.25cr vs PAT ₹429.17cr = 99.6% conversion) — no red flag in the two
    years this AR covers. The FY23 CFO of -₹22.62cr against PAT of ₹305.89cr
    cited in company memory cannot be verified or explained from this
    document; it is plausible on the same float mechanism (a large net
    OUTFLOW in settlement/margin balances that year) but this is inference,
    not an anchored finding. NOT FOUND IN DOCUMENT for FY23 specifically. 🟡
  - Note 53/50 (SGF) and Note 54/51 (trading margin) explain the underlying
    contractual mechanics: SGF cash margin ₹2,529.10L, of which ₹2,342.04L is
    a current liability disclosed at amortised cost; trading margin cash
    ₹17,126.35L; both are "refundable, subject to adjustments" — inherently
    volatile, member-driven balances (standalone p.226, consol p.287).

**Contingent liabilities (Stage 1: NOT FOUND, E4).** NOW FOUND. Standalone
Note 39 (p.217) and Consolidated Note 38 (p.279) disclose exactly ONE
contingent liability in both years: a Delhi GST demand dated 28-Aug-2024 of
tax ₹260.71L + interest ₹216.97L + penalty ₹26.08L = **₹503.76L = ₹5.04cr**
total, under appeal before the GST Appellate Authority, management assessed
as "not tenable and highly unlikely to be retained." As % of net worth:
₹5.04cr ÷ ₹1,364.56cr consolidated net worth = **0.37%** — immaterial. 🟢
No guarantees for subsidiaries/associate disclosed. No other tax disputes,
customs, excise, or legal contingencies disclosed in either note set.

**CERC market coupling order / litigation.** Found, but NOT as a quantified
contingent liability — it is a stand-alone narrative note because no
monetary claim exists (Standalone Note 47, p.224; Consolidated Note 53,
p.290, word-for-word identical text): CERC's Suo Motu Order dated 23-Jul-2025
proposed DAM market-coupling implementation by Jan-2026; IEX challenged
before APTEL; APTEL held IEX "is not a person aggrieved at this stage" since
coupling requires separate CERC Regulations first; IEX has filed a civil
appeal to the Supreme Court; separately, on 17-Apr-2026 CERC issued DRAFT
CERC (Power Market) (Second Amendment) Regulations 2026 for public
consultation. 🔴 (rated red not for accounting quality but for investor
materiality: this is the single largest business-model risk in the company
and the notes give ZERO quantification of revenue-at-risk, no scenario
analysis, and no discussion of probability or timeline — a bare procedural
narrative, nothing more). The notes contain NOTHING on the APTEL judgment
date (13-Feb-2026 per manifest) or the two Supreme Court orders (11-May-2026,
27-Jul-2026) that the manifest's freshness-pair check says exist — the AR's
narrative stops at the 17-Apr-2026 draft regulations (consistent with board
approval on 23-Apr-2026, before the later SC dates). Confirms the corpus gap
flagged in B00 (regulatory_order_text, HIGH): the notes do not carry the
order texts or the later litigation timeline; that must come from elsewhere.

═══════════════════════════════════════════════════════════
FULL NOTE-BY-NOTE EXTRACTION
═══════════════════════════════════════════════════════════

## 1. Accounting policies & changes
- No policy changes with quantified P&L impact this year. Note 3.15 (p.192,
  standalone) / equivalent consol: MCA amendments to Ind AS 21, Ind AS 1
  (current/non-current liability classification), Ind AS 7/107 (supplier
  finance), Ind AS 12 (Pillar Two) all reviewed, "does not have any impact."
  🟢 routine.
- Depreciation useful lives (Note 3.1.4, p.185): Furniture 3-10y vs Schedule
  II 10y; Computers/servers 3-6y vs Schedule II 3-6y; all WITHIN or SHORTER
  than Schedule II norms — conservative, not aggressive. Software licence
  amortised over 15 years (Note 5 footnote, p.194) — the ₹115.43cr software
  licence intangible (net ₹47.13cr) has a long, judgement-heavy life; no
  impairment test sensitivity disclosed. 🟡
- No impairment testing note found for any CGU/goodwill (company holds no
  goodwill; PPE/intangibles impairment policy is boilerplate Ind AS 36
  language, no CGU-specific assumptions disclosed since no impairment
  triggered). 🟢 N/A, clean.
- ECL: trade receivables use the simplified lifetime-ECL approach but the
  company discloses ZERO impairment provision both years, citing settlement
  guarantee funds and pre-funded T+1 settlement mechanics (Note 42(ii)(b),
  p.216-217). Given the business model (buyer pays before seller is paid),
  this is credible, not aggressive. 🟢
- Ind AS 116 leases: discount rate flat at 10% both years (Note 37(C)
  standalone p.212, Note 36(C) consol p.278) — unusually high for an
  investment-grade issuer with zero debt; worth a management question since
  IEX carries no borrowings to benchmark an incremental borrowing rate
  against. 🟡
- No first-time standard adoptions with material effect.

## 2. Related party transactions
Standalone Note 50 (p.222-223) / Consolidated Note 45 (p.283), full table:
| Party | Nature | FY26 ₹L | FY25 ₹L | YoY % |
|---|---|---|---|---|
| KMP | Salary & wages | 916.16 | 744.69 | +23.0% |
| KMP | Perquisites | 1.19 | 1.21 | -1.7% |
| KMP (6 INEDs) | Sitting fees | 73.75 | 68.75 | +7.3% |
| ICX (subsidiary) | Business support services (income to IEX) | 34.19 | 32.79 | +4.3% |
| ICX | Loan given / repaid | 0 / 150.00 | 300.00 / 150.00 | — |
| ICX | Interest income on loan | 3.34 | 1.06 | +215% |
| IGX (associate) | Business support services (income to IEX) | 55.25 | 90.61 | -39.0% |
| IGX | Reimbursement of expenses TO IGX | 4.71 | 1.89 | +149% |
RPT as % of revenue: KMP compensation ₹9.17cr ÷ standalone revenue ₹608.39cr
= 1.51% (FY26) vs ₹7.46cr ÷ ₹535.37cr = 1.39% (FY25) — rising slightly, driven
by the 23% KMP salary jump plus a ₹3.32cr FY26 variable-pay provision
"payable post requisite approvals" (footnote 1, p.223) that is NOT YET PAID
— an accrual pending board/shareholder sign-off, worth watching for
approval terms. 🟡 Promoter shareholding is explicitly Nil both years (Note
17(g), p.202/Note 45), so there is no promoter-family royalty/rent/loan
channel — the RPT risk surface here is KMP compensation governance, not
promoter extraction. Company asserts (p.223) all RPTs are "on terms
equivalent to arm's length transactions" — standard boilerplate assertion,
not independently evidenced in the notes. 🟢 no non-arm's-length signal
found. No new related parties this year; IGX and ICX are the only ones.

## 3. Contingent liabilities — see Load-Bearing Facts above. 🟢 (immaterial)

## 4. Trade receivables
Tiny relative to balance sheet: standalone ₹122.00L = ₹1.22cr (FY26) vs
₹201.04L = ₹2.01cr (FY25) (Note 11, p.198); consolidated ₹197.50L = ₹1.98cr
vs ₹261.99L = ₹2.62cr (Note 11 consol, p.267 equivalent — actually consol
balance sheet Note 11, ~p.240 area). ALL undisputed, considered good, zero
ECL, zero >6 months (ageing table, standalone p.199, consol p.267-area).
"There are no trade receivables which are 'Not Due'" — i.e., by contract
design every invoice is immediately due, consistent with the exchange's
same-day/T+1 settlement cycle. No single-customer >10% of receivables
disclosed (the >10%-of-REVENUE customer concentration is a separate,
important disclosure — see Section 11 below). No related-party receivables
in trade receivables (RPT recoverables sit in "Other financial assets," Note
15, separately). 🟢 clean, immaterial, structurally low-risk given the
prepay/settlement model.

## 5. Inventory — Not applicable. Company explicitly states (Note 49/46
Analytical Ratios, standalone p.221, consol p.284): "Inventory turnover
ratio... The Company does not have any inventory." Exchange platform
business, no physical goods. 🟢 N/A.

## 6. Investments (subsidiaries, JVs, ICDs, other investments)
- ICX Private Limited (subsidiary, 100%): cost ₹500.00L = ₹5.00cr, unchanged
  both years (Note 6, p.193). Loan/ICD given during FY25 ₹300.00L, fully
  repaid by FY26 (Note 14/14.1, p.204). ICX flipped from a small LOSS
  (₹(11.07)L, FY25) to a PROFIT of ₹473.70L = ₹4.74cr (FY26) per the
  Schedule III breakdown (Note 55, p.292) — a striking swing on a tiny
  subsidiary; the notes do not explain the driver. Revenue-side evidence
  (Note 27 consol, p.273) shows ICX likely earns "Membership, processing and
  transfer fees" (jumped ₹1.42cr FY25 → ₹4.67cr FY26) and "I-REC Issuance
  support fees" (₹1.19cr FY25 → ₹3.75cr FY26) — i.e., ICX's FY26 profit
  appears driven by International-REC certification support fee income, NOT
  carbon-credit trading (Indian Carbon Exchange has not yet generated
  disclosed carbon-trading revenue in these notes). 🟡 flag for management
  question — what specifically drove the ICX swing to profit.
- IGX (associate, 47.28%): see Load-Bearing Fact 3 above. 🟢/🟡 mixed (clean
  accounting, but the OFS gap is a flag).
- Enviro Enablers India Private Limited: 10% Series Seed Compulsorily
  Convertible Preference Shares, "Strategic investment," ₹122.22L = ₹1.22cr,
  UNCHANGED both years, held at FVTPL but Level 3 (unobservable inputs) —
  i.e., carried flat at cost-equivalent fair value with no observable
  market, both years (Note 6 p.198-199, Note 41 fair value table p.214/280).
  🟡 minor — a small illiquid strategic stake with no disclosed valuation
  methodology beyond "Level 3."
- Extensive treasury book (₹2,197.59L... actually ₹2,19,759.34L total
  financial assets standalone, Note 41 p.214): laddered across bonds,
  target-maturity funds, fixed-maturity plans, commercial paper (25+
  distinct NBFC/corporate CP issuers each ~₹24-74L), arbitrage/liquid mutual
  funds, an equity index fund sleeve (HDFC/SBI/UTI/ICICI Nifty 50 index
  funds, newly added FY26), and an InvIT unit position (IndiGrid, grown from
  ₹10.69cr to ₹30.90cr FY26) (Note 6/10, pp.193-201). No impairment on any
  instrument either year (Note 6 footnote, "Aggregate amount of impairment
  in value of investments: Nil," both notes). 🟢 well-diversified, no credit
  losses, though the sheer granularity (30+ distinct CP/bond/FMP lines) is a
  lot of day-to-day treasury management for an exchange operator — a
  reasonable ROI-optimisation given ~8.4% return on treasury investments
  (Note 49/46 ratio table) but adds operational/counterparty complexity.

## 7. Borrowings — Not applicable. Note 43/42 Capital Management (standalone
p.220, consol p.285): "The Company/Group does not have any debt outstanding
as on 31 March 2026 and 31 March 2025." Undrawn overdraft/SBLC facility of
₹295.00cr held as a liquidity backstop, unused both years (Note 42(i)/41(i),
p.218/283). Zero covenants, zero breaches. 🟢 clean, matches B00's finding
that IEX has no rated debt.

## 8. Trade payables
Standalone Note 23 (p.209): total ₹411.10L = ₹4.11cr (FY26) vs ₹333.22L =
₹3.33cr (FY25), +23.4% YoY. MSME portion jumped from ₹6.76L to ₹38.03L — a
462% increase on a tiny base (Note 52 MSME disclosure, p.226/consol Note 48
p.290: no interest accrued or paid on delayed MSME payments either year).
Payable days trend not separately computed in the notes but the "Trade
payables turnover ratio" (Note 49/46) improved from 8.62x to 9.59x
standalone (8.69x → 8.72x consol) — i.e., payables cycle roughly stable to
slightly faster, no stretching-of-payables red flag. 🟢

## 9. Provisions
- Gratuity (unfunded defined benefit): standalone obligation ₹745.85L =
  ₹7.46cr (FY26) vs ₹658.22L = ₹6.58cr (FY25) (Note 36, p.210-212).
  Actuarial assumptions: discount rate 7.90% (up from 7.04%), salary
  escalation 10.00% flat, mortality IALM (2012-14), withdrawal rates 8%/5%/2%
  by age band. Duration of obligation shortened sharply from 19.34 years to
  14.13 years (standalone)/14.40 years (consol) — a large single-year
  duration compression worth a question (large past-service-cost line of
  ₹63.66L booked this year, "including curtailment gains/losses," suggests a
  plan-demographic or headcount change). 🟡
- No warranty, decommissioning, onerous-contract, or litigation provisions
  disclosed (none applicable to an exchange platform business). 🟢 N/A.
- Compensated absences provision: ₹568.37L non-current + ₹14.34L current
  standalone (Note 20/26), routine.

## 10. Deferred tax
Standalone Note 21 (p.208-209): net DTL ₹2,921.34L = ₹29.21cr (FY26) vs
₹3,461.94L = ₹34.62cr (FY25), DECREASING as the temporary difference on
investments unwinds (₹(2,082.17)L vs ₹(2,454.52)L). Effective tax rate
reconciliation (Note 34, p.213 standalone / Note 33 p.271 consol): enacted
rate 25.17% both years; actual effective rate lower than enacted, driven
mainly by "Others including difference in tax rate on capital gain on sale
of investments" — a ₹(848.28)L standalone / ₹(1,216.32)L consol favourable
adjustment (long-term capital gains taxed at a lower rate than the ordinary
25.17%, from the treasury book's realised gains). No MAT credit disclosed
(company is not in a MAT-credit position — regular corporate tax payer at
close to statutory rate). No unrecognised DTA disclosed. 🟢 clean, explained,
consistent with a treasury-heavy income mix.

## 11. Revenue details
Covered in Load-Bearing Fact 1. Additional finding: Revenue amounting to
₹9,862.24L = ₹98.62cr (FY26) — MORE THAN 10% of total revenue — is
"attributable to a single customer" (Note 28 standalone p.211, Note 27
consol p.273, identical wording and figure both statements), up from
₹8,379.07L = ₹83.79cr (FY25). The customer is NOT NAMED in the notes. At
₹98.62cr against standalone revenue of ₹608.39cr, this is ~16.2% of FY26
revenue from one counterparty — a concentration that, for a multilateral
exchange, is unusual and worth identifying (likely the largest state
DISCOM/trading member, but the notes give no identity, sector, or
relationship detail). 🟡 flag for management question.
Contract-liability roll-forward for unamortised subscription/admission fee
income (Note 25(a) standalone, p.210 / Note 24(a) consol, p.268): opening
₹1,373.03L, revenue recognised ₹(2,505.21)L combined, invoices raised
₹2,468.69L, closing ₹1,336.51L — routine, no anomaly.

## 12. Other critical notes
- Segment reporting: single operating segment, Ind AS 108 (Note 44
  standalone p.220, consol p.286) — no reportable-segment disclosures.
- EPS: basic = diluted both years, both statements (dilution from ~25,000
  potential option shares against ~889.3cr shares outstanding — economically
  immaterial, <0.003%) (Note 35 standalone p.213, Note 34 consol p.271).
- Capital commitments: standalone Nil FY26 (vs ₹562.39L FY25) (Note 38,
  p.212); consolidated ₹2.65L FY26 (vs ₹562.39L FY25) (Note 37, p.278) — the
  small standalone-vs-consol difference is ICX-level capex commitment.
- Foreign currency exposure: NONE — "all financial assets/liabilities are
  receivable/payable in Indian currency" (Note 42/41, both statements). 🟢
- CSR: required ₹945.00L, spent ₹945.00L, exactly matched both years, zero
  carry-forward either direction (Note 40 standalone p.217-218, Note 39
  consol p.279-280). Clean compliance, no shortfall, no related-party CSR
  spend (explicitly Nil).
- ESOP: Note 51 standalone (p.223-225) / Note 47 consol (p.284-286). Four
  tranches outstanding, exercise prices ₹140-143, weighted average remaining
  life 2.82 years. New grant 29-Jul-2025, 1,00,000 options at ₹143, Black-
  Scholes fair value ₹45.43, volatility assumption jumped from ~20-23% (2023
  grants) to 41.49% (2025 grant) — reflects genuinely higher realised stock
  volatility over FY24-25, not an aggressive assumption choice. 🟢
- Share capital: no fresh issuance beyond routine ESOP exercise (50,540
  shares, FY26); no bonus, no rights, no further buyback since the FY23
  buyback (disclosed historically in Note 17(d), not a current-year event).
  Final dividend proposed post year-end: ₹2/share (FY26) vs ₹1.50/share
  (FY25 final) — a 33% step-up in the proposed final dividend, alongside an
  unchanged ₹1.50 interim (Note 18(f) standalone p.207).
- Direct debits/credits to reserves bypassing P&L: NONE beyond the standard
  ESOP-reserve transfer mechanics (Note 18, both statements) — no unusual
  equity-route adjustments found.
- Events after the balance sheet date: NO DEDICATED SUBSEQUENT-EVENTS NOTE
  exists in either note set. The only "after year-end" disclosures found are
  embedded inside other notes: the proposed final dividend (Note 18(f)), and
  the 17-Apr-2026 CERC draft regulations mentioned inside the CERC narrative
  note (Note 47/53). No note discloses the Indian Coal Exchange incorporation
  (01-Jun-2026 per company memory) — consistent with it falling after the
  23-Apr-2026 board approval date, so its absence from this AR's notes is
  expected, not a disclosure gap. 🟢 (expected absence, not a red flag).
- Whistleblower complaint: Note 46 standalone (p.224) / Note 49 consolidated
  (p.290) — IDENTICAL WORDING both statements. "During the year, the
  [Holding] Company received a whistle blower complaint relating to alleged
  conflict of interest and potential diversion of business involving certain
  officials. The Audit Committee has initiated an independent investigation,
  which remains ONGOING AS AT THE DATE OF APPROVAL of the [consolidated]
  financial statements by the Board... which do not have a material impact."
  🔴 Governance flag: the investigation was STILL OPEN when the AR was signed
  (23-Apr-2026) and the AR itself (filed 14-Aug-2026) gives no update on
  resolution. "Certain officials" and "diversion of business" are serious
  terms; management's "no material impact" conclusion is asserted, not
  evidenced (no scope, no timeline, no findings-to-date disclosed).
- CERC market coupling: see Load-Bearing Facts.

═══════════════════════════════════════════════════════════
PASS 1 SUMMARY — TOP 10 FINDINGS BY INVESTOR IMPORTANCE
═══════════════════════════════════════════════════════════

1. **Whistleblower complaint on conflict of interest / business diversion by
   "certain officials," investigation still open at AR sign-off** (Note 46
   standalone p.224 / Note 49 consol p.290). 🔴 Governance risk, unresolved,
   under-disclosed (no scope/timeline given).

2. **CERC market coupling litigation carries zero quantification of
   revenue-at-risk** despite being the company's largest structural threat
   (Note 47 standalone p.224 / Note 53 consol p.290). 🔴 Not an accounting
   flag but a critical valuation input the notes do not supply.

3. **Other income (₹131.30cr) + IGX equity pickup (₹19.80cr) = ₹151.10cr of
   ₹645.56cr consolidated PBT is non-operating** — treasury/investment
   income and an associate's profit share, together 23.4% of PBT (Note 28
   consol p.273; Note 54 p.291; P&L p.238). 🟡 Load-bearing for any exit-PE
   or EPS-quality adjustment.

4. **IGX carrying value ₹90.25cr (equity method, 47.28% stake) with the
   PNGRB-mandated dilution/OFS to 25% disclosed nowhere in the financial
   statement notes** (Note 54, p.291). 🟡 Material forward-looking event
   entirely absent from the notes; must be sourced elsewhere.

5. **Revenue disaggregation exists but is coarser than assumed** — two-way
   Electricity vs Certificates split only, Certificates revenue DOWN 27.7%
   YoY while Electricity grew 16.8% (Note 28 p.211 / Note 27 p.273). 🟡
   Corrects Stage 1; a real mix-shift signal the headline P&L hides.

6. **₹98.62cr (16.2% of standalone revenue) from a single unnamed customer**,
   up from ₹83.79cr FY25 (Note 28 p.211 / Note 27 p.273). 🟡 Concentration
   risk in a business model presumed to be atomised.

7. **Settlement/margin float swung ~₹244cr YoY through the cash flow
   statement** (₹256.2cr inflow FY25 vs ₹12.0cr FY26 on the "increase in
   other financial liabilities" line) — mechanism confirmed for the
   float-driven CFO volatility hypothesis, though FY23's negative CFO cannot
   be verified from this document (Cash Flow Statements, p.183/p.244). 🟡

8. **KMP compensation up 23% YoY plus a ₹3.32cr unpaid variable-pay accrual
   "pending requisite approvals"** against zero promoter shareholding (Note
   50 p.222-223 / Note 45 p.283). 🟡 Governance/RPT watch item.

9. **ICX (subsidiary) flipped from a ₹(0.11)cr loss to a ₹4.74cr profit**,
   apparently driven by I-REC issuance support fee growth (₹1.19cr → ₹3.75cr)
   rather than carbon-exchange trading revenue (Note 55 p.292; Note 27 p.273).
   🟡 Unexplained in the notes; a question for management on what "Indian
   Carbon Exchange" is actually monetising today.

10. **Contingent liabilities total only ₹5.04cr (0.37% of net worth), one
    GST matter, deemed not tenable by management** — genuinely clean, no
    guarantees, no other litigation quantified (Note 39 p.217 / Note 38
    p.279). 🟢 Resolves Stage 1's E4 NOT FOUND gap with a clean answer.

Ratings tally across all findings above: 3 🔴, 6 🟡, remainder 🟢 (borrowings,
receivables, CSR, tax reconciliation, deferred tax, MSME/payables cycle,
foreign currency, ESOP dilution, investment impairments all clean).
