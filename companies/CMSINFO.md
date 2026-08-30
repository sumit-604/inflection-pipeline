# CMSINFO — CMS Info Systems Limited
Repo path: `companies/CMSINFO.md`
Exchange: NSE CMSINFO / BSE 543441
Sector: Business services — cash logistics, ATM managed services, BFSI technology
---
## GATE LINES (machine-readable — do not reformat)
```
Spear: HIT
Spear-Date: 2026-08-29
Spear-By: Claude web (live)
Spear-CMP: 243
Understanding-Gate: PROCEED
Mental-Model-Signed: 2026-08-30
Mental-Model-Version: 2.0
Tracker-Proof: PENDING
Handover-Dossier: PENDING
```
---
# MENTAL MODEL DECLARATION — SIGNED
**Version 2.0. Signed by operator: Keerti Kaushik, 30 August 2026.**
Supersedes the DRAFT declaration in `runs/cmsinfo-2026-08-29/outputs/reports/09b-understanding-dossier.md` Section 2.

## MM.1. ARCHETYPE
**Contracted infrastructure operator.**
CMS owns the machines, runs the cash, monitors the sites, and is paid a fixed monthly fee for five to ten years by a small number of large banks.
Manifest correction required before Stage 11: `sector_cap_row` currently reads "Platform / SaaS / IT services" (45x cap). This is wrong. CMS is approximately 85% non-SaaS by revenue. The correct comparison set is contracted infrastructure and equipment rental, not software and not asset-light business services. **Do not run Stage 11 until the manifest is corrected.**
### Per-line archetype
| Line | Share FY26 | Archetype |
|---|---|---|
| ATM Management Solutions | 58% | Contracted infrastructure operator (owned machines + service, fixed fee) |
| Retail Solutions & Currency Logistics | 26% | Outsourced labour network (legacy archetype, being pruned) |
| Technology & Payment Solutions | 16% | Platform layered on existing network, subscription |
| Hardware resale | ~7% of consolidated | No archetype. Pass-through trading, deliberately shrinking |
### Structural feature of the archetype, permanent
CMS physically custodies third-party money. Employee and contractor embezzlement: ₹120.53m FY24, ₹217.22m FY25, ₹125.35m FY26. ADT-4 fraud filings under s.143(12) in two consecutive years. Separate provision line for ATM cash shortages. Auditor unable to confirm audit trail operation for billing software, and for general ledger software post-migration 1-Sep-2025.
Small against ₹14 lakh crore handled annually. Permanent, scales with volume, and distinguishes this archetype from asset-light outsourcing peers (Quess, UDS). Belongs in the FROM state, not in the risk register.

## MM.2. THE TRANSITION
### FROM
Outsourced labour network. Owned vans and employed people, banks owned the machines. Paid per transaction or per unit of work. Advantage was route density: a van passing 40 ATMs costs barely more than one passing 20, so the largest network has the lowest cost per stop.
Capital-light. High return. **Exposed to transaction volume.**
### TO
Contracted infrastructure operator. CMS buys the machine, owns it, leases it to the bank alongside cash service and monitoring. One integrated contract, one fee, five to ten years.
Capital-heavy. Lower return. **Insulated from transaction volume.**
### The engine
The pricing shift and the capital shift are **not two transitions. They are one contract.**
Fixed fee is how CMS is paid. Owning the machine is what CMS had to do to win it. A bank accepts a fixed fee only if the supplier carries equipment risk. A supplier funds equipment only if the fee is contracted long enough to earn it back.
This is also why segment reporting broke. In one integrated fee there is no honest way to separate machine rental from cash logistics from monitoring. Management's May-2026 statement that margin splitting is "not possible and feasible" is a consequence of the model, not an evasion.

## MM.3. EVIDENCE (all from audited statements)
### MM.3.1 The machines were bought
PPE additions by class, consolidated (FY26 AR Note 4, p.119; FY25 AR Note 4, p.108):
| Class | FY24 | FY25 | FY26 organic |
|---|---|---|---|
| **Plant and machinery** | 377.01 | 1,097.76 | **3,052.01** |
| Vehicles | 488.85 | — | 113.75 |
| Computers | — | — | 47.22 |
| Total organic additions | 987.44 | 1,274.19 | 3,316.28 |
Plant and machinery = 92% of FY26 organic additions. 2.8x FY25, 8.1x FY24. Vehicles gross block fell (2,906.53 → 2,846.87). Plus ₹1,296.52m via business combination (Securens). Gross block 5,343.78 → 9,424.76, +76.4%.
Class contents confirmed by the AR's own useful-life note: "The Group has amended the useful life of ATM Machines (including Cash Deposit Machines and Cash Recyclers) in line with industry practice from 7 years to 10 years with effect from January 01, 2026."
### MM.3.2 The machines are leased out
FY26 AR Note 29, section headed "Group as lessor" (p.127): "The Group has entered into lease arrangement for its ATM management and Remote monitoring service business. These leases have terms ranging between five and seven years."
| | FY25 | FY26 | Change |
|---|---|---|---|
| Contracted future rentals receivable | 3,734.95 | **8,126.31** | **+117.6%** |
| Equipment given on lease, gross block | 2,434.70 | 3,127.92 | +28.5% |
| Lease income recognised | 1,264.10 | 1,753.12 | +38.7% |
### MM.3.3 The pricing changed
Q1 FY27 call, 11-Aug-2026: ATMs at ~70% cash supply saw transactions fall 27%; well-supplied ATMs saw transactions flat. In the same quarter CMS **raised** FY27 EBITDA margin guidance to ~27% from 25-26%, while cutting revenue guidance.
Volumes collapsed and margin guidance rose. Revenue is decoupled from transactions.
### MM.3.4 The mix moved as the model predicts
| | FY25 | FY26 | Change |
|---|---|---|---|
| Managed Services, recurring services line | 5,652.92 | 7,861.92 | **+39.1%** |
| Technology & Payment Solutions | 2,633 | 3,735 | **+42%** |
| Hardware resale (ATM & sites + spares) | 3,193.74 | 2,368.00 | **-25.9%** |
| Cash Management, external only | 14,670.91 | 13,701.18 | **-6.6%** |

## MM.4. UGLINESS CLASSIFICATION
**ARTIFACT OF CLIMB, with a named treadmill risk.** Upgraded from UNRESOLVED.
Basis for the upgrade, all post-dating the Phase 1 gate recommendation:
- 92% of FY26 capex went into the asset class containing ATMs and recyclers, against a four-year flat base (₹3,720m–₹4,790m FY22-FY25)
- ₹8,126m of contracted future rentals, up 117.6%, evidences the harvest is contracted rather than hoped for
- Capex guided down to ₹100-125 Cr from ~₹350 Cr
- ICICI and IPPB were ~90% live at year end with full ramp in Q1 FY27, so assets preceded revenue
**Treadmill risk retained and named:** CWIP ₹1,134.71m at year end with ₹2,809.83m added during FY26 (FY24 CWIP: ₹147.30m), so the build has not finished. FY26 capex overshot its own November-2025 guidance of ~₹300 Cr by roughly 17%.

## MM.5. OPERATOR READING
**Necessity, executed from strength.**
The old model was dying. India's ATM count is falling ~4% p.a., off-site machines are being shut in thousands, and under per-transaction contracts every closure took revenue directly. AGS ran that model with leverage and is in CIRP with ₹13,171 Cr of admitted claims and a 97% collapse in market value.
Banks changed the tender terms. CMS complied. The strongest evidence that this was not a free choice: CMS won the flagship SBI mandate as **L1** after having been the only qualified participant in a first round that was scrapped.
The strength is equally real. Post-AGS, banks tightened credit across every MSP and weaker players hit a funding wall. Balance sheet became the qualification to compete. CMS has zero debt, ~₹600 Cr cash, [ICRA]AA+/A1+. Industry expected to consolidate from 6-7 players to 3-4.
**Investment consequence:** because the move was forced rather than chosen, do NOT assume the destination returns match the origin returns. A company that moves voluntarily moves because the destination is better. A company that moves because it must accepts whatever the market allows. Current spread: 16.6% post-tax ROCE against ~13% cost of equity. Approximately three points. Positive but thin.

## MM.6. PROOF GATE
**Consolidated post-tax ROCE above 22% by FY28, with capital employed flat and capex at or below the guided ₹100-125 Cr.**
FY27 is NOT the test year. Depreciation lags capex: Q1 FY27 D&A annualises to ~₹2,900m against FY26's ₹2,076m, so the depreciation peak is FY27. Judging FY27 as the recovery year produces a false negative. FY28 is the first clean year.
### Gates explicitly rejected, with reasons
| Rejected gate | Why it fails |
|---|---|
| EBITDA margin | The mix shift flatters it. FY26 proved this: EBITDA margin 24.1% looked survivable while ROCE fell 8.6 points |
| Managed Services segment margin | Set by an undisclosed transfer price that moved by 72% of the segment's total profit in one year |
| Technology % of services revenue | Purchasable. FSS guided at ~4% of FY27 services revenue; 16% + 4% = 20% passes the gate with zero organic delivery |
| Segment-level ROCE | Corrupted by the same transfer price |
### Recovery arithmetic (why the gate is 22%, not 44%)
| Cash Mgmt + Managed Services | FY25 | FY26 |
|---|---|---|
| Capital employed | 12,123 | **16,141** |
| Segment result | 5,379 | 4,378 |
| Return on capital | 44.4% | **27.1%** |
The capital base is a third larger and permanent. Profit returning to the FY25 peak restores only 33.3%, not 44.4%. Restoring 44.4% requires profit 33% ABOVE the all-time high. The recovery is partial by construction.

## MM.7. DOMINANT VARIABLES
| # | Variable | Current | Threshold |
|---|---|---|---|
| 1 | Consolidated post-tax ROCE | 16.6% | >22% by FY28 pass; <18% sustained past FY28 fail |
| 2 | Capital employed vs capex guidance | Capex guided ₹100-125 Cr | Flat capital = build; rising = treadmill |
| 3 | Contracted lease rentals receivable | ₹8,126m, +117.6% | Rising then stabilising = harvest arriving |
| 4 | Loss allowance cover vs aged receivables | **0.29x standalone** (was 4-6x for four years) | Recovery toward historic cover |
| 5 | ATM useful life assumption | 10 years (was 7) | Further extension = warning. Impairment = confession |
**Why variable 5 is dominant, not a footnote.** In a business that owns and leases machines, the useful life assumption IS the profitability. It sets depreciation, which sets whether each contract clears its hurdle. CMS extended life 43% in the same year the fleet grew 76%. Management describes this as "in line with industry practice" — a checkable claim, on the live-web list.
### What the model rejects as noise
- **Whether cash is dying.** Fixed-fee contracts have broken the link. Currency in circulation grew 12% regardless.
- **Market size.** 9.1x revenue headroom, runway STRONG. Execution is the constraint.
- **EBITDA margin.** In an asset-owning business, EBITDA is the number before the cost of the assets. Least informative line in the accounts.
- **Segment-level returns.** Unusable. See MM.8.
- **Promoter alignment.** No promoter exists. Sion exited 27-Feb-2024, declassified 2-Apr-2025. Structural, not a disclosure failure.
- **DSO as a trend.** 140 (FY21) → 115 → 100 → 116 → 116 → 126 (FY26). Non-monotonic, below FY21, no restatement across four ARs. There is no multi-year collection drift. The earlier claim of 73→131 days over eight years was a secondary-source error and is retired.

## MM.8. WHAT CANNOT BE MEASURED (carry to Stage 11 as a discount)
Inter-segment billing rose 1,280.87 → 2,264.00 in FY26, +76.8%, now 9.1% of consolidated revenue (3.3% in FY22). The FY26 increase of ₹983.13m equals 72% of Managed Services' entire segment result.
On the reported split, Cash Management earns 44.1% on capital and Managed Services 14.7%. Holding the charge at the FY25 level inverts it to 29.7% and 25.2%. **One undisclosed number flips the conclusion about whether the transition creates or destroys value.**
Every verification route is closed: pricing basis is "arm's length" only, direction of flow never stated, no standalone Brown Label ATM count exists (folded in, reason given: "fully integrated nature of operations"), no segment depreciation disclosed, segment profitability asked and refused. Inter-segment billing has never been raised by any analyst on any of four calls.
The arm's-length footnote appears for the first time in the FY26 AR, absent FY23-FY25, in the year the line doubled.
**Ruling: this is a permanent discount at valuation, not a monitorable that might clear.** Management has stated the split cannot be produced. Use combined Cash Management + Managed Services returns (MM.6) and never the segment split.
### The tension being underwritten
The transition thesis is a claim that revenue is moving from one segment to another. Management's disclosure position is that the segments are not separable. Both cannot be strongly true. If the business genuinely is one integrated thing, there is no ladder to climb — only a company that got less profitable in FY26 and may or may not get more profitable again.

## MM.9. FALSIFIERS
### Transition falsifier (kills the arrow, not the business)
Capex comes in at the guided ₹100-125 Cr, capital employed goes flat, contracts reach full ramp, and **ROCE still does not clear 20% by FY28.**
Then CMS is buying assets that earn roughly its cost of capital. It converted a high-return labour business into a zero-spread rental book because it had no choice, preserving revenue while destroying returns.
Secondary transition falsifiers: organic Technology + Managed Services external revenue growth falls below 15%; or capex overshoots the guide materially for a second consecutive year.
### Business falsifier (kills the FROM business)
Multi-year decline in national cash usage — CIC growth reversing or UPI substitution outpacing cash-ATM growth for several consecutive years — combined with the core proving permanently unable to recover after the currency-supply shock passes.
**Clean test already available:** national cash fulfilment has recovered from 70% to 80-85%. If it normalises and CMS revenue does not respond, the external-shock framing is dead and the decline is structural.

## MM.10. FRAGILITY: HIGH
Not because there are many variables. Because of what has been withdrawn.
Of five dominant variables, two are audited and clean (ROCE, loss allowance cover), one is checkable annually (capital employed), one is disclosed but new (lease rentals receivable), and the segment attribution that would explain any of them is gone.
**Three disclosure withdrawals in twelve months:**
1. Segment profitability — promised Nov-2025 ("80% of the network running independently" by year end), reversed May-2026 ("not possible and feasible")
2. HAWKAI/ALGO standalone revenue — refused every quarter asked
3. Return on Net Worth — dropped from the FY26 MD&A ratio table, replaced by post-tax ROCE, so no like-for-like multi-year return series exists
Each has a defensible individual explanation. Together they mean the model runs on numbers the company chooses to show.

## MM.11. MANAGEMENT: DOWNGRADE B → B-
Not for any single miss. For a consistent directional pattern: every commitment that would have created visibility into a weakening number was dropped, each replaced by an explanation of why it was never possible.
| Promised | When | Outcome |
|---|---|---|
| 74,000-75,000 ATMs by March 2026 | Nov-2025, reaffirmed Feb-2026 | Still ~70,000. Never mentioned again |
| DSO back to normal by end-March 2026 | Feb-2026 | Never mentioned again. Days rose to 126 |
| 80% of network independently reportable | Nov-2025 | Reversed May-2026 |
Offsetting, and genuine: guidance cut on revenue and raised on margin in the same breath with a quantified ₹25 Cr cause and a printed 27.2% quarter behind it. Two named self-admissions (SBI capacity over-investment, two-year forecasting miss streak). CEO Rajiv Kaul raised his personal stake from ~2.6% to 6.43% through the PE exit and the FY26 price fall, with no disclosed selling.
Promoter verdict remains TRUSTWORTHY (no promoter exists; applies to professional management and board; 6 clean / 4 caution / 0 red; zero SEBI, criminal, tax or NCLT adverse findings).

## MM.12. CORRECTIONS TO THE RUN RECORD
Log these against `runs/cmsinfo-2026-08-29`:
1. **`outputs/reports/03-ardeep.md` is wrong on segment attribution.** It assigns the -7.8% decline to ATM Management Solutions. The MD&A tables are correctly placed (verified by rasterized read and by the Board's Report naming each figure to each platform). ATM Management **grew 5.3%** (12,840 → 13,515); **Retail & Currency Logistics fell 7.8%** (6,368 → 5,872). `04-bizmodel.yaml` and `business-narrative.md` had this right. The two blocks contradicted each other and no verifier caught it.
2. **Contingent liabilities: Gate 0 was correct.** ₹554.60m consolidated is the full FY26 figure, the sum of all nine sub-clauses, not one sub-clause. A secondary-source claim of "₹604 crore" was a unit error (₹604.39 **million** = ₹60.4 Cr) and the prior year. No Gate 0 rescore required.
3. **`manifest.yaml` sector_cap_row is wrong** ("Platform / SaaS / IT services"). Same defect class as DIVGIITTS ("Agri processing"). Blocks Stage 11.
4. **Collector defect:** screener split CSVs (Profit_Loss, Balance_Sheet, Cash_Flow, Quarters) are header-only for CMSINFO and all six peers — 42 empty files. Blocked four of twelve moat tests and the capex-embedded-growth calculation. Bug in `collect_to_repo.py`.
5. **Fabricated figure in `06-peers.md`:** QUESS "₹176 Cr one-time Labour Code pass-through" does not appear in the Feb-2026 or May-2026 QUESS transcripts. Actual figure ₹7 Cr. Caught by Verifier D, corrected at synthesis, load-bearing for nothing. Also: an AGSTRA quote misattributed to the wrong call and wrong speaker.
6. **HAWKAI revenue resolved to ₹200 Cr.** The Directors' Report "₹200 million" is a typo. Test: Technology & Payment Solutions totals ₹3,735m (₹373.5 Cr), so ₹200 Cr fits inside it and ₹200 million cannot be its largest component.
7. **MD&A capex claim is false.** FY26 MD&A states the increase came "after 2 years of subdued capex averaging less than ₹1,000 million." Cash flow statements: FY24 ₹1,083.76m, FY25 ₹1,543.37m, average ₹1,313.57m — 31% above the claim. Separately, MD&A asset additions ₹3,520m vs cash flow ₹4,092.68m, a ₹572.68m gap. Verified unique to FY26: FY23 and FY25 MD&A figures matched their cash flows exactly.
8. **SBI mandate ATM count stated five ways:** ~10,000 (original, sole eligible bidder) → ~5,000 (Feb-2026 call, L1 of re-tender) → 5,000 (Finvezto) → 4,000 (FY26 MD&A p.52) → no count (Board's Report, CEO letter). The ₹1,000 Cr headline never moved while the volume fell ~60%.
### Analyst-side reversals during Halt 1 (logged for calibration)
- Claimed the MD&A segment tables were transposed. **Wrong.** Column-collapse artifact in the text extraction. Tables are correctly placed. Conclusion happened to be right; reasoning was not.
- Claimed an eight-year DSO drift from 73 to 131 days. **Wrong.** Secondary-source series. ARs show 140 → 115 → 100 → 116 → 116 → 126, non-monotonic and below FY21.
- Claimed Managed Services was a broken growth engine (+₹1,501m revenue, +₹0.27m profit). **Wrong.** Its internal bill rose ₹983m in the same year.
- Claimed Gate 0 may have mis-scored contingent liabilities. **Wrong.** Gate 0 was correct.
- Proposed the rental archetype, **withdrew it** on two secondary sources, then **reinstated it** on the PPE and lessor notes. The withdrawal was the error: secondary sources were allowed to override a balance-sheet question that had not yet been checked. The PPE note should have been read first.

## MM.13. OUTSTANDING BEFORE FTTCP
| # | Item | Owner |
|---|---|---|
| 1 | Correct `manifest.yaml` sector_cap_row | Claude Code |
| 2 | Verify Hitachi Payment Services acquisition of a competitor (flagged by Finvezto, absent from corpus; unlisted so invisible to the peer set) | Claude web, live |
| 3 | Verify Brink's / NCR Atleos transaction and its India implications | Claude web, live |
| 4 | Verify whether 10-year ATM useful life is genuinely "in line with industry practice" | Claude web, live |
| 5 | Role 5.5 tracker rows in Notion DOWNSTREAM SIGNAL TRACKER | Claude web |
| 6 | Web handover dossier at `runs/cmsinfo-2026-08-29/inputs/research/web-handover-dossier.md` | Claude web |
| 7 | Peer set requires revision for valuation: RADIANTCMS/SIS/QUESS/UDS reflect the FROM archetype. Add contracted-infrastructure comparables. Global anchors: Brink's, Loomis, Euronet | Operator ruling |

## MM.14. MENTAL MODEL RULING LOG
```
2026-08-30 | Keerti | MENTAL MODEL SIGNED v2.0. Archetype: contracted infrastructure operator.
                      Transition: per-transaction/asset-light -> fixed-fee/asset-owning, one integrated
                      contract not two transitions. Reading: NECESSITY EXECUTED FROM STRENGTH.
                      Ugliness: ARTIFACT OF CLIMB with named treadmill risk. Fragility: HIGH.
                      Proof gate: consolidated post-tax ROCE >22% by FY28, capital flat, capex at guide.
                      FY28 is the test year, not FY27. Segment-level attribution ruled permanently
                      unusable and carried to Stage 11 as a discount. Management B -> B-.
                      Understanding-Gate: PROCEED.
2026-08-29 | Keerti | SPEAR VERDICT: HIT. Enters heavy pipeline. Peer set approved.
```
---
## 1. SPEAR PASS RECORD
**Date:** 29 August 2026
**Performed by:** Claude web, live web sources. Not a Claude Code output.
**Verdict:** HIT — enters heavy pipeline.
### 1.1 Anchor numbers at spear
| Item | Value | Basis |
|---|---|---|
| CMP | ₹243 | NSE close 28-Aug-2026 (₹243.10 NSE / ₹243.35 BSE) |
| Shares outstanding | ~16.00 Cr | 15,96,98,415 post-buyback extinguishment + ESOP allotments |
| Market cap | ~₹3,888 Cr | CMP × shares |
| Cash + investments | ₹610.08 Cr at 31-Mar-2026, less ₹167.93 Cr buyback → ~₹442 Cr | Buyback LoF / FY26 AR |
| FY26 total revenue | ₹2,487 Cr (₹24,871.82 m) | FY26 AR consolidated P&L p.212 |
| FY26 services revenue | ₹2,310 Cr | FY26 earnings presentation, 14-May-2026 |
| FY26 EBITDA | ₹596 Cr, 24.0% margin | FY26 earnings presentation |
| FY26 PAT | ₹303 Cr (₹3,033.92 m) | FY26 AR consolidated P&L p.212 |
| FY26 EPS (post-buyback share count) | ₹18.9 | Derived |
| Trailing P/E | 12.8x | Derived |
| 52-week range | ₹239 – ₹432.85 | Live, 28-Aug-2026 |
| 1-year price return | approx. −43% | Live |
### 1.2 POND — real opportunity size
Two ponds moving in opposite directions.
**Shrinking (units).** Total India ATM network 208,063, down about 4% from 216,352 a year earlier. Net ATM reductions have been the norm since 2022, led by private banks cutting off-site machines.
**Growing (cash volume).** Currency in circulation ₹42.56 lakh Cr as at 29-May-2026, up 12% YoY. Banknotes in circulation ₹41.23 trillion at end-March 2026, up 11.9%; volume 171.32 bn pieces, up 10.5%. Fewer machines handling more money.
**CMS position (company-disclosed shares).**
- 73,000 ATMs managed = approx. 47% of all outsourced ATMs in India
- Retail cash management share 38%, up 400 bps in two years
- BFSI Vision AI, CMS + Securens combined, 36% share
**Competitor hole.** AGS Transact, formerly the second-largest ATM managed services player, entered CIRP on 25-Aug-2025 (NCLT Mumbai) after an IND D downgrade in Feb-2025. Roughly 12% of the market orphaned. CMS has been absorbing it, including replacing 1,000 ATMs and cash dispensers for India Post Payments Bank.
**Live bottleneck.** National cash fulfilment — share of indented cash actually received for ATM replenishment — fell to 57% in April 2026 from about 80% in November 2025. March and April indents were near ₹94,000 Cr per month against receipts of about ₹61,000 Cr and ₹54,000 Cr. CATMi attributes the concentration of the problem to SBI, supplying 55-65% of requirement in April 2026. RBI Governor stated on 05-Jun-2026 that currency stocks are adequate and shortages will be met promptly.
**Derived addressable pond [INFERENCE — analyst arithmetic, back-solved from disclosed shares]:**
| Slice | CMS revenue | Disclosed share | Implied pond |
|---|---|---|---|
| ATM Management Solutions | ~₹1,300 Cr (FY25) | 47% of outsourced | ~₹2,800 Cr |
| Retail & Currency Logistics | ~₹600 Cr | 38% | ~₹1,580 Cr |
| Tech & Payments | ~₹370 Cr | 36% BFSI Vision AI + software | ~₹800-1,000 Cr |
| **Total** | **₹2,310 Cr services** | | **~₹5,000-5,500 Cr** |
**Pond verdict:** CMS already holds roughly 43% of its own addressable pond. This is a share-of-wallet runway of roughly 2x plus pond growth, not a multi-bagger TAM story. Any thesis built on a large unpenetrated market is wrong on the facts.
Material caveat: Hitachi Payment Services, FSS, Writer Business Services and Securens are unlisted. The listed peer set understates the competitive field.
### 1.3 CATCH — three-year outcomes to FY29
Signed conversion evidence anchored to:
| Win | Value | Term | Annual run-rate | Status |
|---|---|---|---|---|
| SBI integrated cash solutions | ₹1,000 Cr | 10 years | ~₹100 Cr; company states ~₹500 Cr incremental | Live Jan-2026 |
| HDFC Bank, 6,000 ATMs | ₹400 Cr | 5 years | ~₹80 Cr | From FY27 |
| FSS ATM managed services (asset buy) | ₹115 Cr paid | — | Adds 8,000 units, 31k → 39k managed | Closed Q1 FY27 |
| ICICI Bank expanded partnership | Not disclosed | — | — | FY26 |
| IPPB ATM replacement | 1,000 units | — | — | FY26, post-AGS |
| | Careful | Fair | Dream |
|---|---|---|---|
| Services revenue CAGR | 8% | 12% | 16% |
| FY29 services revenue | ₹2,910 Cr | ₹3,246 Cr | ₹3,610 Cr |
| FY29 total revenue | ₹3,100 Cr | ₹3,450 Cr | ₹3,850 Cr |
| EBITDA margin | 24.5% | 26.5% | 28.0% |
| FY29 EBITDA | ₹760 Cr | ₹915 Cr | ₹1,078 Cr |
| FY29 PAT | ₹370 Cr | ₹480 Cr | ₹590 Cr |
| FY29 EPS | ₹23.1 | ₹30.0 | ₹36.9 |
Case logic:
- **Careful:** cash-supply squeeze persists into FY28; ATM units keep falling 4% a year; new bank contracts only replace base attrition.
- **Fair:** company's own FY30 path of 13-14% discounted by about two points; private bank mix and software carry margin to 26.5%.
- **Dream:** AGS share fully absorbed; cash fulfilment normalises; Tech & Payments reaches 22% of revenue.
Calibration checks:
- Management FY27 guidance is services ₹2,650-2,750 Cr, i.e. 15-19% growth. The Fair case runs slower.
- Four covering analysts forecast FY27 revenue ₹27.6 bn and EPS ₹22.51 (post-Q1 FY27, cut from ₹23.20). The Fair case at ₹30.0 by FY29 sits behind the street compounded.
- Share count assumed flat at 16.0 Cr. Further buybacks treated as upside, not modelled.
### 1.4 PRICE (spear-level only — not a Role 1 substitute)
Weights 35% Careful / 45% Fair / 20% Dream. Exit multiples 13x / 16x / 20x against current 12.8x. Dividends approx. ₹18 over three years (FY26 total ₹5.25/share: ₹2.75 interim + ₹2.50 final).
- Probability-weighted FY29 value: **₹487 per share**
- Entry price for 25% CAGR: ₹487 ÷ 1.25³ = **₹249**
- CMP ₹243 sits about 2% below the 25% CAGR entry, with no margin of safety layered on top.
No exit-multiple derivation, no Section 1B, no Damodaran work performed at spear. Destination PE is Role 1's job under the current framework. The old "exit PE max 20x" project rule was NOT applied.
### 1.5 VERDICT — HIT
Shape fits the transition template. Market is pricing a business that dies with the ATM. Filings show revenue tracking cash volume (+12%) rather than machine count (−4%). The second-largest competitor collapsed into insolvency and its customers are being re-tendered to the only player with the scale and balance sheet to absorb them. Three of India's largest banks signed integrated outsourcing contracts in eight months. Current earnings are depressed by an external cash-supply failure at bank branches, not by franchise damage. The de-rating from roughly 25x to 12.8x supplies the second return engine if the engine is real.
Three named reasons this could be wrong, all serious:
1. Pond is small relative to the company — 2x share story, not 10x.
2. About 82% of revenue still touches physical cash. Tech & Payments at 18% is the only genuine escape and it is roughly ₹400 Cr.
3. ₹167.93 Cr buyback executed at ₹340 in June 2026 is roughly 40% underwater at ₹243. Capital allocation question the pipeline must answer.
---
## 2. LOAD-BEARING FACTS — first verification targets
All four from filed documents or the company's own transcripts. No aggregator sources. Each must be confirmed against primary text before anything is built on it.

**LBF-1 — Cash conversion above 1.2x, three years running.**
FY26 consolidated CFO ₹3,895.94 m vs PAT ₹3,033.92 m (FY26 AR consolidated cash flow p.214; P&L p.212). FY25 ₹4,825.28 m vs ₹3,724.57 m. FY24 ₹4,398.93 m vs ₹3,471.41 m.
*Verify against audited cash flow statements, not presentations. This is the spine of the thesis and the Pillar 2 input.*

**LBF-2 — Q1 FY27 revenue hit is external and quantified.**
CEO on the 11-Aug-2026 call stated banks supplied about 70% of the currency the industry indented, and that this cost roughly ₹25 Cr of revenue with an operating deleverage effect.
*Verify exact wording and figure in the primary transcript. If it recurs at that rate the annual drag is about ₹100 Cr.*

**LBF-3 — Guidance cut on revenue and raised on margin in the same breath.**
Same call: FY27 services revenue reset to ₹2,650-2,750 Cr from ₹2,700-2,800 Cr; total revenue to ₹2,750-2,850 Cr; EBITDA margin raised to about 27% from 25-26%.
*Verify the May-2026 and August-2026 guidance side by side. This combination is the signature of a genuine mix shift and is the strongest single piece of transition evidence.*

**LBF-4 — Cash embezzlement is a recurring CARO line, not a one-off.**
FY26: 25 instances, ₹125.35 m, ₹9.98 m recovered, ₹12.70 m written off, ADT-4 filed under s.143(12). FY25: 28 instances, ₹217.22 m. FY24: 10-11 instances, ₹120.53 m.
*Verify the CARO annexure directly. Also verify the FY26 audit-trail comment: audit trail not enabled for one billing software, and auditors unable to comment at application/database level for the general ledger software post-migration from 1-Sep-2025.*
---
## 3. GAPS TO CLOSE BEFORE HALT 1
| # | Gap | Where to fetch |
|---|---|---|
| G-1 | DSO moved 116 → 126 days while screener shows working capital days rising 75.9 → 117. Contradicts the strong CFO story. | FY26 AR MD&A ratios p.99; consolidated Note 11 trade receivables; reconcile against cash flow working capital movement |
| G-2 | Q1 FY27 EBITDA margin appears as both 26.6% and 27.2%. Likely total-revenue vs services-revenue basis. Must be pinned. | Q1 FY27 earnings presentation 10-Aug-2026, slides 3 and 4; Q1 FY27 results filing |
| G-3 | ₹115 Cr FSS acquisition has no disclosed revenue contribution anywhere in corpus. | Reg-30 filing 30-Mar-2026; Q1 FY27 concall Q&A; FY27 half-year results |
| G-4 | Half-year (H1/H2) splits FY24-FY26 not disclosed. Full quarterly P&L for FY24 and FY25 quarters not disclosed beyond services revenue and margin. | BSE quarterly filings, reconstruct from Reg-33 submissions |
| G-5 | Geographic and metro/SURU revenue split not disclosed in any year. | Likely does not exist. Opacity is itself a data point |
| G-6 | Full rating rationale (CRISIL/ICRA/CARE) not in corpus. | Rating agency site |
| G-7 | Q1 FY27 concall transcript — confirm it is in the run corpus and is newer than the Q1 results filing. | Company IR page, 11-Aug-2026 |
---
## 4. STRUCTURAL NOTES CARRIED FORWARD
- **No promoter.** Sion Investment Holdings Pte Ltd (Advent/Baring affiliate) sold its remaining 26.66% on 27-Feb-2024 and was declassified from promoter to public with effect from 2-Apr-2025. Post-buyback the register is 100% institutional and public, with no promoter category. Promoter-based framework tests (pledge, promoter remuneration as % of PAT, SEBI action on promoter) are NOT DISCLOSED because there is no promoter, not because disclosure failed.
- **Undiscovered Alpha Multiplier does NOT apply.** Institutional ownership is high, not absent. Mutual funds approx. 30%, FII approx. 25%, AIF approx. 6% at 31-Mar-2026. PPFAS raised its stake to 7.97% in March 2026.
- **FY26 exceptional item** ₹92.44 m consolidated, ₹57.05 m standalone, from Labour Codes statutory impact.
- **Accounting estimate change:** ATM machine useful life extended from 7 to 10 years effective 1-Jan-2026, lowering FY26 depreciation by ₹47.65 m. Flag for earnings-quality review.
- **Corporate guarantees** ₹800 m on behalf of Securitrans India Pvt Ltd, unchanged FY24 through FY26 (₹600 m to lenders, ₹200 m to a customer for overnight vaulting).
- **Loan to non-subsidiary:** Transaction Solutions International (India) Pvt Ltd, ₹580.12 m outstanding at 31-Mar-2026. Relationship as customer or supplier NOT DISCLOSED. Flag for the extraction prompt.
- **Board:** Will Poole (William Poole VIII) appointed Additional Independent Director effective 10-Aug-2026 for three years, subject to shareholder approval. Ex-Microsoft CVP, co-founder of Capria Ventures. Signals the AI/software pivot.
- **AGM:** 19th AGM on 21-Sep-2026 via VC. BRSR filed 27-Aug-2026.
---
## 5. PEER SET (for pipeline peer comparison)
| Ticker | Company | Tier | Role in comparison |
|---|---|---|---|
| RADIANTCMS | Radiant Cash Management Services | 1 — direct | Only listed pure-play retail cash logistics competitor. Similar P/E, materially worse ROCE (12.7%) |
| SIS | SIS Ltd | 1 — direct | Security plus SIS Cash Services. Same WC shape, same Labour Codes exposure. Note: acquired 4.2% of UDS on 05-Jun-2026, so SIS and UDS are not independent observations |
| AGSTRA | AGS Transact Technologies | 1 — failure case | In CIRP. Same model with leverage and stretched receivables. Use for counterfactual, EXCLUDE from median |
| QUESS | Quess Corp | 2 — same economics | Indian outsourcing platform multiple benchmark |
| UDS | Updater Services | 2 — same economics | Cautionary comparable on the "diversified business services platform" narrative. 3-yr ROE 10.9% |
| AURIONPRO | Aurionpro Solutions | 3 — segment only | For the 18% Tech & Payments slice. Software multiple. EXCLUDE from headline median or it distorts |
Global anchors for the exit-multiple work at Role 1 (not on screener): Brink's, Loomis, Euronet Worldwide.
---
## 6. RULING LOG
*(Operator entries appended below. Newest first. Every ruling dated and signed.)*
```
2026-08-30 | Keerti | MENTAL MODEL SIGNED v2.0. Archetype: contracted infrastructure operator. Understanding-Gate: PROCEED. Halt 1 cleared. Manifest sector_cap_row correction required before Stage 11.
2026-08-29 | Keerti | SPEAR VERDICT: HIT. Enters heavy pipeline. Peer set approved as listed in Section 5.
```
---
## 7. GATE STATUS
| Gate | Requirement | Status |
|---|---|---|
| Spear | `Spear: HIT` line present | ✅ SET 29-Aug-2026 |
| Halt 1 | Stage 09b dossier + signed mental model + PROCEED | ✅ SIGNED 30-Aug-2026 (Mental Model v2.0, PROCEED) |
| Role 5.5 tracker | Tracker row proof-of-write logged here | ⬜ Pending |
| Handover | `runs/cmsinfo-<date>/inputs/research/web-handover-dossier.md` exists | ⬜ Pending |
| P/E gate | Operator rulings on Pillar 1 base, cash multiplier, growth premium, earnings basis | ⬜ Pending |
| Amendment 16 | ROCE vs cost of capital crossing during projection | ⬜ Not yet assessed |
| Amendment 17 | Converter classification per slice | ⬜ Not yet assessed |
| Amendment 18 | Exit-basis symmetry, Option Resolution Calendar | ⬜ Not yet assessed |
| Amendment 19 | FV path table, FV CAGR, return-source classification | ⬜ Not yet assessed |
---
## 8. NEXT-QUARTER FALSIFICATION LINE
Q2 FY27 results, expected around November 2026.
The thesis is falsified, not merely dented, if **all three** of the following hold:
1. Services revenue comes in below ₹625 Cr, i.e. no sequential growth off the Q1 FY27 record despite the SBI, HDFC and FSS additions being live.
2. EBITDA margin falls back below 25%, breaking the recovery from the Q3 FY26 bottom and contradicting the raised ~27% FY27 guidance.
3. National cash fulfilment has recovered above 75% (per CATMi/IBA data) yet CMS revenue has still not responded — which would mean the revenue loss was never the external cash-supply issue management attributed it to.
Condition 3 is the decisive one. If fulfilment recovers and revenue does not, the "external shock" explanation fails and the business is structurally losing ground rather than waiting out a distribution problem.
