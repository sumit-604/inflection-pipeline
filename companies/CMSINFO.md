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
Mental-Model-Version: 2.1
Tracker-Proof: WRITTEN 2026-08-30 (5 rows, all Case B)
Companies-Master-Row: https://app.notion.com/p/3ccbb2b9d3ab81eea904dd45d21f8825
Handover-Dossier: runs/cmsinfo-2026-08-29/inputs/research/web-handover-dossier.md
```
---
# MENTAL MODEL DECLARATION — SIGNED
**Version 2.1. Signed by operator: Keerti Kaushik, 30 August 2026.**
Supersedes v2.0 (same date) and the DRAFT declaration in `runs/cmsinfo-2026-08-29/outputs/reports/09b-understanding-dossier.md` Section 2.
v2.1 changes: seven amendments from ValuePickr thread 92804 (pages 8-9), integrated into Sections MM.2, MM.7, MM.8 and MM.11. Changes are marked [v2.1] throughout.
*(Section numbers below carry an MM. prefix to keep the declaration distinct from this file's native Sections 1-8; the operator's numbering is otherwise unchanged.)*

## MM.1. ARCHETYPE
**Contracted infrastructure operator.**
CMS owns the machines, runs the cash, monitors the sites, and is paid a fixed monthly fee for five to ten years by a small number of large banks.
Manifest correction required before Stage 11: `sector_cap_row` currently reads "Platform / SaaS / IT services" (45x cap). This is wrong. CMS is approximately 85% non-SaaS by revenue. The correct comparison set is contracted infrastructure and equipment rental, not software and not asset-light business services. **Do not run Stage 11 until the manifest is corrected.**
### Per-line archetype
| Line | Share FY26 | Archetype |
|---|---|---|
| ATM Management Solutions | 58% | Contracted infrastructure operator (owned machines + service, fixed fee) |
| Retail Solutions & Currency Logistics | 26% | Outsourced labour network (legacy archetype, being pruned) |
| Technology & Payment Solutions | 16% | Platform layered on existing network, subscription. **Also a hardware-displacement wedge — see 2.4** [v2.1] |
| Hardware resale (banking automation) | ~7% of consolidated | No archetype. Machine supply to bank-owned estates, deliberately shrinking |
### Structural feature of the archetype, permanent
CMS physically custodies third-party money. Employee and contractor embezzlement: ₹120.53m FY24, ₹217.22m FY25, ₹125.35m FY26. ADT-4 fraud filings under s.143(12) in two consecutive years. Separate provision line for ATM cash shortages. Auditor unable to confirm audit trail operation for billing software, and for general ledger software post-migration 1-Sep-2025.
Small against ₹14 lakh crore handled annually. Permanent, scales with volume, and distinguishes this archetype from asset-light outsourcing peers (Quess, UDS). Belongs in the FROM state, not the risk register.
---
## MM.2. THE TRANSITION
### 2.1 Restated [v2.1]
v2.0 stated the transition as asset-light to asset-owning. **That was imprecise.** CMS has owned machines for over a decade: it entered ATM and cash-recycler deployment in 2013 in partnership with Nautilus Hyosung, and won a ₹255 Cr SBI mandate in January 2015 to deploy 2,300+ cash recyclers. The capital was always partly there.
**FROM:** own the machine, **paid per transaction.** Depreciation runs continuously; revenue stops when volumes stop. Both risks, neither protection.
**TO:** own the machine, **paid a fixed monthly fee** on five-to-ten-year contracts. Depreciation runs continuously; revenue does not depend on volumes.
**What changed is the pricing, not the ownership.**
A second, distinct strand runs alongside it:
| Machine model | Who owns | Where disclosed | FY26 direction |
|---|---|---|---|
| Supply and support | The bank | Banking automation / hardware sale line | **-25.9%** |
| Own and lease | CMS | Note 29 "Group as lessor" | **+117.6%** |
CMS has run the first model since 2013 (the 2015 SBI deal included two years' warranty and five years' support on bank-owned machines). It is the low-margin pass-through line and is being deliberately shrunk. The second is the growth engine.
**So: from selling machines to owning them, and from per-transaction to per-month.** Both strands, same direction.
### 2.2 Why the two halves are one contract
Fixed fee is how CMS is paid. Owning the machine is what CMS had to do to win it. A bank accepts a fixed fee only if the supplier carries equipment risk. A supplier funds equipment only if the fee is contracted long enough to earn it back.
This is also why segment reporting broke. In one integrated fee there is no honest way to separate machine rental from cash logistics from monitoring. Management's May-2026 statement that margin splitting is "not possible and feasible" is a consequence of the model, not an evasion.
### 2.3 The residue of the old model [v2.1]
Transaction-linked Brown Label contracts remain on the book and are where the FROM archetype still bites.
[SECONDARY, ValuePickr #179, 10-Aug-2026, invested member]: the Q1 FY27 EBIT hit came from transaction-pricing linked BLA contracts, "where depreciation bites at you consistently, but if you're not replenishing the ATM then you're not earning anything on that. There was no cash to replenish."
This resolves an anomaly the pipeline flagged but could not explain: Q1 FY27 EBITDA margin **rose** ~190bps while EBIT margin compressed to 10.3% from 14.1%. Part is FY26 capex depreciation landing. Part is this: on the transaction-linked book, depreciation ran while revenue stopped.
**This is the exact combination that killed AGS** (transaction-based revenue model, aggressive BLA capex with poor returns, per the CMS-vs-AGS structural comparison). CMS still carries a residual position in it.
Size: [SECONDARY, weak — ChatGPT-assisted forum table] "<10% of revenue." **NOT DISCLOSED in any filing. Must be pinned.** See MM.13.
### 2.4 ALGO as a hardware-displacement wedge [v2.1]
**Reclassification.** ALGO MVS is not primarily a technology revenue line. It is the mechanism by which CMS displaces incumbent hardware.
[SECONDARY, ValuePickr #170, 12-Jun-2026]: the biggest fear for a PSU bank switching hardware is software incompatibility. ALGO Multi-Vendor Software removes hardware dependence. Once that dependence is gone, CMS can convince banks to swap NCR machines for CMS-deployed cash recyclers.
Sequence: sell vendor-agnostic software → bank's hardware lock-in dissolves → CMS bids to replace the incumbent's estate with its own machines under an integrated fixed-fee contract.
Supporting disclosed facts: ALGO runs ~65,000 ATMs including the entire SBI network, ~40% share of ATM software; ICICI expected live in FY27 adding 10,000+ machines; CMS has held a Nautilus Hyosung supply relationship since 2013 and was "market leader in deployment of intelligent deposit systems."
**Consequence for monitoring:** ALGO's installed-ATM share matters more than ALGO's revenue. Track machines under ALGO, not rupees.
**Status: UNVERIFIED forum reasoning.** Plausible, internally consistent, and consistent with disclosed facts, but no filing states this strategy. On the live-web list.
---
## MM.3. EVIDENCE (all from audited statements)
### 3.1 The machines were bought
PPE additions by class, consolidated (FY26 AR Note 4, p.119; FY25 AR Note 4, p.108):
| Class | FY24 | FY25 | FY26 organic |
|---|---|---|---|
| **Plant and machinery** | 377.01 | 1,097.76 | **3,052.01** |
| Vehicles | 488.85 | — | 113.75 |
| Computers | — | — | 47.22 |
| Total organic additions | 987.44 | 1,274.19 | 3,316.28 |
Plant and machinery = 92% of FY26 organic additions. 2.8x FY25, 8.1x FY24. Vehicles gross block **fell** (2,906.53 → 2,846.87). Plus ₹1,296.52m via business combination (Securens). Gross block 5,343.78 → 9,424.76, +76.4%.
Class contents confirmed by the AR's own useful-life note: "The Group has amended the useful life of ATM Machines (including Cash Deposit Machines and Cash Recyclers) in line with industry practice from 7 years to 10 years with effect from January 01, 2026."
### 3.2 The machines are leased out
FY26 AR Note 29, "Group as lessor" (p.127): "The Group has entered into lease arrangement for its ATM management and Remote monitoring service business. These leases have terms ranging between five and seven years."
| | FY25 | FY26 | Change |
|---|---|---|---|
| Contracted future rentals receivable | 3,734.95 | **8,126.31** | **+117.6%** |
| Equipment given on lease, gross block | 2,434.70 | 3,127.92 | +28.5% |
| Lease income recognised | 1,264.10 | 1,753.12 | +38.7% |
### 3.3 The pricing changed
Q1 FY27 call, 11-Aug-2026: ATMs at ~70% cash supply saw transactions fall 27%; well-supplied ATMs saw transactions flat. In the same quarter CMS **raised** FY27 EBITDA margin guidance to ~27% from 25-26%, while cutting revenue guidance.
Volumes collapsed and margin guidance rose. On the fixed-fee book, revenue is decoupled from transactions. On the transaction-linked BLA residue, it is not — see 2.3.
### 3.4 The mix moved as the model predicts
| | FY25 | FY26 | Change |
|---|---|---|---|
| Managed Services, recurring services line | 5,652.92 | 7,861.92 | **+39.1%** |
| Technology & Payment Solutions | 2,633 | 3,735 | **+42%** |
| Hardware resale (ATM & sites + spares) | 3,193.74 | 2,368.00 | **-25.9%** |
| Cash Management, external only | 14,670.91 | 13,701.18 | **-6.6%** |
---
## MM.4. UGLINESS CLASSIFICATION
**ARTIFACT OF CLIMB, with a named treadmill risk.** Upgraded from UNRESOLVED.
Basis, all post-dating the Phase 1 gate recommendation:
- 92% of FY26 capex into the asset class containing ATMs and recyclers, against a four-year flat base (₹3,720m–₹4,790m FY22-FY25)
- ₹8,126m of contracted future rentals, +117.6%, evidencing the harvest is contracted rather than hoped for
- Capex guided down to ₹100-125 Cr from ~₹350 Cr
- ICICI and IPPB ~90% live at year end, full ramp Q1 FY27, so assets preceded revenue
**Treadmill risk retained and named:** CWIP ₹1,134.71m at year end with ₹2,809.83m added during FY26 (FY24 CWIP: ₹147.30m), so the build has not finished. FY26 capex overshot its own November-2025 guidance of ~₹300 Cr by roughly 17%.
---
## MM.5. OPERATOR READING
**Necessity, executed from strength.**
The old model was dying. India's ATM count is falling ~4% p.a., off-site machines are being shut in thousands, and under per-transaction contracts every closure took revenue directly. AGS ran that model with leverage and is in CIRP with ₹13,171 Cr of admitted claims and a 97% collapse in market value.
[v2.1] The Q1 FY27 experience makes this concrete rather than theoretical: on the transaction-linked residue, a single quarter's cash shortage stopped revenue while depreciation continued. **CMS is moving off transaction pricing because transaction pricing nearly hurt it badly in one quarter of one bad year.**
Banks changed the tender terms. CMS complied. Strongest evidence this was not a free choice: CMS won the flagship SBI mandate as **L1** after having been the only qualified participant in a first round that was scrapped.
The strength is equally real. Post-AGS, banks tightened credit across every MSP and weaker players hit a funding wall. Balance sheet became the qualification to compete. CMS has zero debt, ~₹600 Cr cash, [ICRA]AA+/A1+. Industry expected to consolidate from 6-7 players to 3-4.
**Investment consequence:** because the move was forced rather than chosen, do NOT assume destination returns match origin returns. A company that moves voluntarily moves because the destination is better. A company that moves because it must accepts whatever the market allows. Current spread: 16.6% post-tax ROCE against ~13% cost of equity. Approximately three points. Positive but thin.
---
## MM.6. PROOF GATE
**Consolidated post-tax ROCE above 22% by FY28, with capital employed flat and capex at or below the guided ₹100-125 Cr.**
FY27 is NOT the test year. Depreciation lags capex: Q1 FY27 D&A annualises to ~₹2,900m against FY26's ₹2,076m, so the depreciation peak is FY27. Judging FY27 as the recovery year produces a false negative. FY28 is the first clean year.
### Secondary gate, organic growth [v2.1 — REVISED]
v2.0 set organic Technology + Managed Services external growth at 15% or better.
**Management's own FY30 decomposition is approximately 12% organic plus 4% inorganic** [SECONDARY, ValuePickr #163, sourced to management commentary]. The 13-14% headline services CAGR is therefore **not all organic.**
The 15% gate was set above what the company is guiding to. Two options, operator ruled:
**RULING: retain 15% as a deliberate stretch, and record why.** If CMS is genuinely climbing a quality ladder, the segments it is climbing into (Managed Services external, Technology) must outgrow the blended guide, because the blend includes the declining core. 15% on the growth lines is consistent with 12% at group level. If the growth lines only manage 12%, the mix shift is too slow to matter within a 3-5 year hold.
**Explicitly exclude FSS and Securens revenue from this measurement.** FSS is guided at ~4% of FY27 services revenue; 16% + 4% = 20% would pass a naive technology-share gate with zero organic delivery.
### Gates explicitly rejected, with reasons
| Rejected gate | Why it fails |
|---|---|
| EBITDA margin | The mix shift flatters it. FY26 proved this: EBITDA margin 24.1% looked survivable while ROCE fell 8.6 points. [v2.1] Q1 FY27 proved it again: EBITDA +190bps while EBIT fell 14.1% → 10.3% |
| Managed Services segment margin | Set by an undisclosed transfer price that moved by 72% of the segment's total profit in one year |
| Technology % of services revenue | Purchasable. See above |
| Segment-level ROCE | Corrupted by the same transfer price |
### Recovery arithmetic (why the gate is 22%, not 44%)
| Cash Mgmt + Managed Services | FY25 | FY26 |
|---|---|---|
| Capital employed | 12,123 | **16,141** |
| Segment result | 5,379 | 4,378 |
| Return on capital | 44.4% | **27.1%** |
The capital base is a third larger and permanent. Profit returning to the FY25 peak restores only 33.3%, not 44.4%. Restoring 44.4% requires profit 33% ABOVE the all-time high. The recovery is partial by construction.
---
## MM.7. DOMINANT VARIABLES
| # | Variable | Current | Threshold |
|---|---|---|---|
| 1 | Consolidated post-tax ROCE | 16.6% | >22% by FY28 pass; <18% sustained past FY28 fail |
| 2 | Capital employed vs capex guidance | Capex guided ₹100-125 Cr | Flat capital = build; rising = treadmill |
| 3 | Contracted lease rentals receivable | ₹8,126m, +117.6% | Rising then stabilising = harvest arriving |
| 4 | Loss allowance cover vs aged receivables | **0.29x standalone** (4-6x for four prior years) | Recovery toward historic cover |
| 5 | ATM useful life assumption | 10 years (was 7) | Further extension = warning. Impairment = confession |
| 6 [v2.1] | **Transaction-linked BLA as % of revenue** | <10% [SECONDARY, unpinned] | Falling = old model retiring. Rising or flat = FROM archetype persists |
| 7 [v2.1] | **ATMs running ALGO** | ~65,000, ~40% share | Rising ahead of contract wins = the wedge working |
**Why variable 5 is dominant, not a footnote.** In a business that owns and leases machines, the useful life assumption IS the profitability. It sets depreciation, which sets whether each contract clears its hurdle. CMS extended life 43% in the same year the fleet grew 76%. Management describes this as "in line with industry practice" — a checkable claim, on the live-web list.
**Why variable 6 [v2.1].** This is where the AGS failure mode still lives inside CMS. It is the only part of the book carrying both depreciation and volume risk. It is also, per 2.3, where the Q1 FY27 EBIT damage concentrated.
**Why variable 7 [v2.1].** Track machines, not rupees. Per 2.4, ALGO's function is to dissolve hardware lock-in ahead of the renewal window. Its installed base is the leading indicator; its revenue is the lagging one.
### What the model rejects as noise
- **Whether cash is dying.** Fixed-fee contracts have broken the link on the new book. CIC grew 12% regardless.
- **Market size.** 9.1x revenue headroom, runway STRONG. Execution is the constraint.
- **EBITDA margin.** In an asset-owning business, EBITDA is the number before the cost of the assets. Least informative line in the accounts.
- **Segment-level returns.** Unusable. See MM.8.
- **Promoter alignment.** No promoter. Sion exited 27-Feb-2024, declassified 2-Apr-2025. Structural.
- **DSO as a trend.** 140 (FY21) → 115 → 100 → 116 → 116 → 126 (FY26). Non-monotonic, below FY21, no restatement across four ARs. There is no multi-year collection drift. The earlier claim of 73→131 days over eight years was a secondary-source error and is retired.
- **Currency-in-circulation as a primary KPI** [v2.1]. CIC rises with nominal GDP regardless. The binding metrics are ATM replenishment frequency, machines serviced, and route density — not the stock of notes.
---
## MM.8. WHAT CANNOT BE MEASURED (carry to Stage 11 as a discount)
Inter-segment billing rose 1,280.87 → 2,264.00 in FY26, +76.8%, now 9.1% of consolidated revenue (3.3% in FY22). The FY26 increase of ₹983.13m equals 72% of Managed Services' entire segment result.
On the reported split, Cash Management earns 44.1% on capital and Managed Services 14.7%. Holding the charge at the FY25 level inverts it to 29.7% and 25.2%. **One undisclosed number flips the conclusion about whether the transition creates or destroys value.**
Every verification route is closed: pricing basis is "arm's length" only, direction of flow never stated, no standalone Brown Label ATM count exists (folded in, reason given: "fully integrated nature of operations"), no segment depreciation disclosed, segment profitability asked and refused. Inter-segment billing has never been raised by any analyst on any of four calls.
The arm's-length footnote appears for the first time in the FY26 AR, absent FY23-FY25, in the year the line doubled.
**Ruling: permanent discount at valuation, not a monitorable that might clear.** Management has stated the split cannot be produced. Use combined Cash Management + Managed Services returns (MM.6) and never the segment split.
[v2.1] **Note the compounding problem.** The absence of a standalone BLA disclosure now blocks two separate questions: the volume-vs-price test on inter-segment billing, AND the sizing of transaction-linked BLA exposure (variable 6). The same withheld number obscures both.
### The tension being underwritten
The transition thesis is a claim that revenue is moving from one segment to another. Management's disclosure position is that the segments are not separable. Both cannot be strongly true. If the business genuinely is one integrated thing, there is no ladder to climb — only a company that got less profitable in FY26 and may or may not get more profitable again.
---
## MM.9. FALSIFIERS
### Transition falsifier (kills the arrow, not the business)
Capex comes in at the guided ₹100-125 Cr, capital employed goes flat, contracts reach full ramp, and **ROCE still does not clear 20% by FY28.**
Then CMS is buying assets that earn roughly its cost of capital. It converted a high-return labour business into a zero-spread rental book because it had no choice, preserving revenue while destroying returns.
Secondary transition falsifiers: organic Technology + Managed Services external growth falls below 15%; capex overshoots the guide materially for a second consecutive year; or [v2.1] transaction-linked BLA fails to shrink as a share of revenue.
### Business falsifier (kills the FROM business)
Multi-year decline in national cash usage — CIC growth reversing or UPI substitution outpacing cash-ATM growth for several consecutive years — combined with the core proving permanently unable to recover after the currency-supply shock passes.
**Clean test already available:** national cash fulfilment has recovered from 70% to 80-85%. If it normalises and CMS revenue does not respond, the external-shock framing is dead and the decline is structural.
---
## MM.10. UNMODELLED UPSIDE [v2.1 — NEW SECTION]
Not in any projection. Recorded because the trigger is external, dated and observable.
**UPI monetisation.** The entire bear case on CMS is that free UPI kills cash. If UPI stops being free, that case weakens structurally, through legislation rather than through anything CMS does.
Evidence [SECONDARY, forum-sourced with links]:
- Lok Sabha passed a bill allowing charges on UPI and other digital payments (Aug-2026)
- A parliamentary panel proposed tiered UPI charging, small merchants exempt, larger entities paying (Mar-2026)
- RBI Governor Sanjay Malhotra has said publicly that somebody has to pay for it
- RBI separately introducing ₹10 and ₹20 notes
**Trigger to watch:** charges actually landing on consumers rather than being absorbed by banks or merchants. Until then this is a possibility, not a forecast.
**Explicitly excluded from base, bear and bull cases.** If it fires, it fires as pure upside.
**Second unmodelled item: the PSU renewal window.** PSU bank contracts awarded 2018-2020 come up for renewal from **end-2026 through 2028** [SECONDARY, ValuePickr #170]. Over 100,000 ATMs remain un-outsourced by large PSU banks (FY26 MD&A). Combined with the ALGO wedge (2.4), this is the mechanism through which the outsourcing pool converts. Dated, checkable, and not in the numbers.
---
## MM.11. FRAGILITY: HIGH
Not because there are many variables. Because of what has been withdrawn.
Of seven dominant variables, two are audited and clean (ROCE, loss allowance cover), one is checkable annually (capital employed), one is disclosed but new (lease rentals receivable), one is an accounting assumption (useful life), and two [v2.1] are NOT DISCLOSED at all (transaction-linked BLA share, ALGO installed base is disclosed only sporadically in presentations).
**Three disclosure withdrawals in twelve months:**
1. Segment profitability — promised Nov-2025 ("80% of the network running independently" by year end), reversed May-2026 ("not possible and feasible")
2. HAWKAI/ALGO standalone revenue — refused every quarter asked
3. Return on Net Worth — dropped from the FY26 MD&A ratio table, replaced by post-tax ROCE, so no like-for-like multi-year return series exists
Each has a defensible individual explanation. Together they mean the model runs on numbers the company chooses to show.
---
## MM.12. MANAGEMENT: DOWNGRADE B → B-
Not for any single miss. For a consistent directional pattern: every commitment that would have created visibility into a weakening number was dropped, each replaced by an explanation of why it was never possible.
### Dropped commitments
| Promised | When | Outcome |
|---|---|---|
| 74,000-75,000 ATMs by March 2026 | Nov-2025, reaffirmed Feb-2026 | Still ~70,000. Never mentioned again |
| DSO back to normal by end-March 2026 | Feb-2026 | Never mentioned again. Days rose to 126 |
| 80% of network independently reportable | Nov-2025 | Reversed May-2026 |
### Guidance record: THREE consecutive years, not two [v2.1 — CORRECTED]
| Year | Guided | Path | Outcome |
|---|---|---|---|
| FY25 | ₹2,500-2,700 Cr (H2 2024) | Q1 FY25 "top end" → next quarter "mid-range" | Below ₹2,500 Cr |
| FY26 | Services growth 8% (Nov-2025) | — | Actual 6% |
| FY27 | Services ₹2,700-2,800 Cr (Nov-2025, reaffirmed Feb & May) | — | Cut to ₹2,650-2,750 Cr (Aug-2026) |
The pattern is identical each year: guide, walk down within the year, miss. [SECONDARY, ValuePickr #163 for the FY25 sequence; FY26 and FY27 from corpus.]
Management has itself acknowledged a "two-year forecasting miss streak." On this record it is three.
Offsetting, and genuine: guidance cut on revenue and raised on margin in the same breath with a quantified ₹25 Cr cause and a printed 27.2% quarter behind it. Two named self-admissions (SBI capacity over-investment, forecasting miss streak). CEO Rajiv Kaul raised his personal stake from ~2.6% to 6.43% through the PE exit and the FY26 price fall, with no disclosed selling. Buyback acceptance ratio exceeded 60% for retail participants.
Promoter verdict remains TRUSTWORTHY (no promoter exists; applies to professional management and board; 6 clean / 4 caution / 0 red; zero SEBI, criminal, tax or NCLT adverse findings).
---
## MM.13. OUTSTANDING BEFORE FTTCP
| # | Item | Owner | Priority |
|---|---|---|---|
| 1 | Correct `manifest.yaml` sector_cap_row | Claude Code | **Blocks Stage 11** |
| 2 [v2.1] | **Pin transaction-linked BLA as % of revenue.** Currently <10% on a weak secondary estimate. This is dominant variable 6 and it is unmeasured | Claude Code extraction | **High** |
| 3 [v2.1] | Verify the ALGO hardware-displacement thesis (2.4) — any filing, call or trade-press statement supporting vendor-agnostic software as a displacement route | Claude web, live | High |
| 4 [v2.1] | Verify the PSU renewal window end-2026 to 2028 and the 2018-2020 award cycle | Claude web, live | High |
| 5 | Verify Hitachi Payment Services acquisition of a competitor (flagged by Finvezto, absent from corpus; unlisted so invisible to the peer set) | Claude web, live | Medium |
| 6 | Verify Brink's / NCR Atleos ($6.6bn). NCR Atleos has installed 100,000+ ATMs in India incl. SBI — larger footprint than assumed. Kaul reportedly dismissed the threat on a call | Claude web, live | Medium |
| 7 | Verify whether 10-year ATM useful life is genuinely "in line with industry practice" | Claude web, live | Medium |
| 8 [v2.1] | Verify UPI monetisation bill status and implementation timeline (MM.10) | Claude web, live | Medium |
| 9 | Role 5.5 tracker rows in Notion DOWNSTREAM SIGNAL TRACKER | Claude web | Sequenced |
| 10 | Web handover dossier at `runs/cmsinfo-2026-08-29/inputs/research/web-handover-dossier.md` | Claude web | Sequenced |
| 11 | Peer set requires revision for valuation: RADIANTCMS/SIS/QUESS/UDS reflect the FROM archetype. Add contracted-infrastructure comparables. Global anchors: Brink's, Loomis, Euronet | Operator ruling | Before Stage 11 |
---
## MM.14. CORRECTIONS TO THE RUN RECORD
Log against `runs/cmsinfo-2026-08-29`:
1. **`outputs/reports/03-ardeep.md` is wrong on segment attribution.** It assigns the -7.8% decline to ATM Management Solutions. The MD&A tables are correctly placed (verified by rasterized read and by the Board's Report naming each figure to each platform). ATM Management **grew 5.3%** (12,840 → 13,515); **Retail & Currency Logistics fell 7.8%** (6,368 → 5,872). `04-bizmodel.yaml` and `business-narrative.md` had this right. The two blocks contradicted each other and no verifier caught it.
2. **Contingent liabilities: Gate 0 was correct.** ₹554.60m consolidated is the full FY26 figure, the sum of all nine sub-clauses. A secondary claim of "₹604 crore" was a unit error (₹604.39 **million** = ₹60.4 Cr) and the prior year. No rescore required.
3. **`manifest.yaml` sector_cap_row is wrong.** Same defect class as DIVGIITTS ("Agri processing"). Blocks Stage 11.
4. **Collector defect:** screener split CSVs are header-only for CMSINFO and all six peers — 42 empty files. Blocked four of twelve moat tests and the capex-embedded-growth calculation. Bug in `collect_to_repo.py`.
5. **Fabricated figure in `06-peers.md`:** QUESS "₹176 Cr one-time Labour Code pass-through" does not appear in the Feb-2026 or May-2026 transcripts. Actual ₹7 Cr. Caught by Verifier D, corrected at synthesis. Also an AGSTRA quote misattributed to the wrong call and wrong speaker.
6. **HAWKAI revenue resolved to ₹200 Cr.** The Directors' Report "₹200 million" is a typo. Test: Technology & Payment Solutions totals ₹3,735m (₹373.5 Cr), so ₹200 Cr fits inside it and ₹200 million cannot be its largest component.
7. **MD&A capex claim is false.** FY26 MD&A states the increase came "after 2 years of subdued capex averaging less than ₹1,000 million." Cash flows: FY24 ₹1,083.76m, FY25 ₹1,543.37m, average ₹1,313.57m — 31% above the claim. Separately, MD&A asset additions ₹3,520m vs cash flow ₹4,092.68m, a ₹572.68m gap. Verified unique to FY26.
8. **SBI mandate ATM count stated five ways:** ~10,000 (original, sole eligible bidder) → ~5,000 (Feb-2026 call, L1 of re-tender) → 5,000 (Finvezto) → 4,000 (FY26 MD&A p.52) → no count (Board's Report, CEO letter). The ₹1,000 Cr headline never moved while the volume fell ~60%.
9. [v2.1] **The Nautilus Hyosung relationship is absent from the corpus** yet is load-bearing for the machine-deployment capability. CMS entered ATM and recycler deployment in 2013 via this partnership and won a ₹255 Cr / 2,300-recycler SBI mandate in January 2015. Not mentioned in any of the four ARs read, the presentation, or the four calls. Add to the research brief.
### Analyst-side reversals during Halt 1 (logged for calibration)
- Claimed the MD&A segment tables were transposed. **Wrong.** Column-collapse artifact in the text extraction. Conclusion happened to be right; reasoning was not.
- Claimed an eight-year DSO drift from 73 to 131 days. **Wrong.** Secondary-source series. ARs show 140 → 115 → 100 → 116 → 116 → 126.
- Claimed Managed Services was a broken growth engine (+₹1,501m revenue, +₹0.27m profit). **Wrong.** Its internal bill rose ₹983m in the same year.
- Claimed Gate 0 may have mis-scored contingent liabilities. **Wrong.** Gate 0 was correct.
- Proposed the rental archetype, **withdrew it** on two secondary sources, then **reinstated it** on the PPE and lessor notes. The withdrawal was the error: secondary sources were allowed to override a balance-sheet question that had not yet been checked. The PPE note should have been read first.
- [v2.1] Stated the transition as asset-light to asset-owning. **Imprecise.** CMS has owned machines since 2013. The change is in pricing (per-transaction to per-month) and in model (supply-to-bank to own-and-lease). Corrected in 2.1.
---
## MM.15. SOURCE-TIER NOTE ON v2.1 [v2.1]
Seven amendments derive from ValuePickr thread 92804, pages 8-9, an overwhelmingly invested-holder forum. Tiering:
**[SECONDARY, independently verified]:** Nautilus Hyosung partnership and the 2015 ₹255 Cr / 2,300-recycler SBI mandate (Business Standard, siliconindia, CMS's own site). Brink's / NCR Atleos $6.6bn and NCR Atleos' 100,000+ Indian ATM installed base.
**[SECONDARY, unverified but internally consistent]:** the transaction-linked BLA depreciation-versus-revenue mechanism (2.3); the ALGO displacement thesis (2.4); the PSU renewal window; the FY25 guidance walk-down sequence; the 12% organic + 4% inorganic decomposition.
**[SECONDARY, weak]:** transaction-linked BLA at "<10% of revenue" — from a ChatGPT-assisted forum table. Treated as a placeholder pending extraction, not as a fact.
**Counter-weight, recorded deliberately.** The strongest posts in the thread are the sceptical ones and they are not dismissed here: terminal value is hard to assign to a segment that is 54% of revenue and shrinking; the market has always discounted cash prospects (P/E below 30 even at the 2024 peak); and even at FY30 guidance digital solutions remain roughly one quarter of the business. All three are consistent with the thin-spread conclusion in MM.5.
---
## MM.16. MENTAL MODEL RULING LOG
```
2026-08-30 | Keerti | MENTAL MODEL v2.1. Seven amendments from ValuePickr 92804 pp.8-9 integrated.
                      Transition RESTATED: not asset-light -> asset-owning (CMS has owned machines
                      since 2013) but per-transaction -> per-month, and supply-to-bank -> own-and-lease.
                      Transaction-linked BLA identified as the residue of the FROM archetype and the
                      source of the Q1 FY27 EBIT-vs-EBITDA divergence; added as dominant variable 6,
                      currently UNPINNED. ALGO reclassified from revenue line to hardware-displacement
                      wedge; added as dominant variable 7, tracked by installed base not revenue.
                      PSU renewal window end-2026 to 2028 and UPI monetisation added as unmodelled
                      upside (MM.10). Guidance record corrected to THREE consecutive years of
                      misses. Organic growth gate held at 15% as a deliberate stretch above
                      management's ~12% organic guide, with reasoning recorded.
                      All else per v2.0. Understanding-Gate remains PROCEED.
2026-08-30 | Keerti | MENTAL MODEL SIGNED v2.0. Archetype: contracted infrastructure operator.
                      Reading: NECESSITY EXECUTED FROM STRENGTH. Ugliness: ARTIFACT OF CLIMB with
                      named treadmill risk. Fragility: HIGH. Proof gate: consolidated post-tax ROCE
                      >22% by FY28, capital flat, capex at guide. FY28 is the test year, not FY27.
                      Segment-level attribution ruled permanently unusable, carried to Stage 11 as a
                      discount. Management B -> B-. Understanding-Gate: PROCEED.
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
*Note (per Mental Model MM.13 item 11): this peer set reflects the FROM archetype. For Stage 11 valuation it must be revised to add contracted-infrastructure comparables; the global anchors above stand.*
---
## 6. RULING LOG
*(Operator entries appended below. Newest first. Every ruling dated and signed.)*
```
2026-08-30 | Keerti | ROLE 1 P/E GATE RULED. Section 1B settled: base 16.0x x cash 1.15x = 18.4x raw, Amendment 20 trim to destination 17.0x (band 15.7-18.3x). Earnings basis FORWARD (entry FY27E, exit FY30E). Pillar 3 +0 (EM 23<25), strategic +0, UA none, NON-CONVERTER. Cash multiplier 1.15x (top band minus one notch for negative FY26 FCF). Do not re-derive.
2026-08-30 | Keerti | MENTAL MODEL v2.1. Seven ValuePickr 92804 pp.8-9 amendments. Transition RESTATED (per-transaction -> per-month, supply-to-bank -> own-and-lease; CMS has owned machines since 2013). Transaction-linked BLA added as dominant variable 6 (unpinned); ALGO reclassified as hardware-displacement wedge, variable 7. Guidance record corrected to three straight misses. Understanding-Gate remains PROCEED. Full log at MM.16.
2026-08-30 | Keerti | MENTAL MODEL SIGNED v2.0. Archetype: contracted infrastructure operator. Understanding-Gate: PROCEED. Halt 1 cleared. Manifest sector_cap_row correction required before Stage 11.
2026-08-29 | Keerti | SPEAR VERDICT: HIT. Enters heavy pipeline. Peer set approved as listed in Section 5.
```
---
## 7. GATE STATUS
| Gate | Requirement | Status |
|---|---|---|
| Spear | `Spear: HIT` line present | ✅ SET 29-Aug-2026 |
| Halt 1 | Stage 09b dossier + signed mental model + PROCEED | ✅ SIGNED 30-Aug-2026 (Mental Model v2.1, PROCEED) |
| Role 5.5 tracker | Tracker row proof-of-write logged here | ✅ WRITTEN 30-Aug-2026 (5 rows, all Case B; COMPANIES MASTER row created) |
| Handover | `runs/cmsinfo-<date>/inputs/research/web-handover-dossier.md` exists | ✅ FILED 30-Aug-2026 (`runs/cmsinfo-2026-08-29/inputs/research/web-handover-dossier.md`) |
| P/E gate | Operator rulings on Pillar 1 base, cash multiplier, growth premium, earnings basis | ✅ RULED 30-Aug-2026 (dest PE 17.0x fwd; cash 1.15x; Pillar 3 +0; basis FORWARD) |
| Amendment 16 | ROCE vs cost of capital crossing during projection | ✅ Assessed: ROCE 16.6% > r 13.5%, gate OPEN on ROCE; Pillar 3 +0 anyway (EM 23<25) |
| Amendment 17 | Converter classification per slice | ✅ Assessed: NON-CONVERTER; machinery not applied |
| Amendment 18 | Exit-basis symmetry, Option Resolution Calendar | ✅ Assessed: FORWARD both ends, horizon hold+1; no option slices (Calendar N/A) |
| Amendment 19 | FV path table, FV CAGR, return-source classification | ✅ Assessed: FV CAGR 13.8% -> HYBRID |
---
## 8. NEXT-QUARTER FALSIFICATION LINE
Q2 FY27 results, expected around November 2026.
The thesis is falsified, not merely dented, if **all three** of the following hold:
1. Services revenue comes in below ₹625 Cr, i.e. no sequential growth off the Q1 FY27 record despite the SBI, HDFC and FSS additions being live.
2. EBITDA margin falls back below 25%, breaking the recovery from the Q3 FY26 bottom and contradicting the raised ~27% FY27 guidance.
3. National cash fulfilment has recovered above 75% (per CATMi/IBA data) yet CMS revenue has still not responded — which would mean the revenue loss was never the external cash-supply issue management attributed it to.
Condition 3 is the decisive one. If fulfilment recovers and revenue does not, the "external shock" explanation fails and the business is structurally losing ground rather than waiting out a distribution problem.
---
## 9. RUN OUTCOME — FTTCP + Role 1 (2026-08-30)
**One-line thesis:** a cash-logistics leader repricing off a dying per-transaction model onto contracted fixed-fee machine rental; real transition, thin spread, unproven until the FY28 ROCE gate fires.
**Gate verdict:** PROCEED WITH CAVEATS (FLAG-CASH INDETERMINATE cap). Overall confidence 64.
**FTTCP:** composite +3, DEEP WATCH. ROCE forward RECOVERING, no uplift credited. Devil's advocate WEAKENED BUT ALIVE (all four dimensions weakened).
**Valuation decision (this run):** WATCHLIST. Destination PE 17.0x forward (band 15.7-18.3x). Three-year value ~Rs 555. Entry zone Rs 227 to Rs 284 (MoS Rs 227; note verifier C F6 — under the 18-24 month proof-gate window the evidence-scaled floor could be ~Rs 170). Hurdle Ratio 2.20 PASS. FV CAGR 13.8% -> HYBRID. CMP Rs 243 sits 14% below entry, 7% above MoS (buy-on-dips on price only). Position: Small on conversion; no position at WATCHLIST. Tier A. Decision Status is operator-only (set in Notion).
**Active flags:** FLAG-CASH INDETERMINATE (industry-event-induced), FLAG-PROMOTER TRUSTWORTHY (no promoter, positive), SHARED CATALYST (FY28 ROCE recovery + any future growth premium ride the same capex-fill event).
**Dominant variable 6 PINNED (this run):** transaction-linked BLA ~8-12% of revenue (FY25 AR donut chart 8%, management 12% Q1 FY27). Corrects MM.2.3's "NOT DISCLOSED in any filing" — it is in the FY25 AR. The 8%->12% rise is unexplained by the corpus (named contradiction, against the transition direction).
**Active tripwires (thesis-broken):**
1. FY28 consolidated post-tax ROCE stays below 20% with capex at the Rs 100-125 Cr guide and capital flat (transition falsifier).
2. 1-2yr overdue receivables bucket widens again while Cash Management revenue falls (FLAG-CASH hardens to structural).
3. National cash fulfilment recovers to 80-85%+ while CMS services revenue does not respond (decline is structural, not shock).
**Publish candidate (flagged, not written):** India ATM units grew 1.3% YoY while withdrawal VALUE fell ~7% (RBI/NPCI); CMS ATM Management grew 5.3%. Inverts the cash-is-dying read.
**Run folders:** runs/cmsinfo-2026-08-29 (spear + Phase 1 evidence + Phase 2 FTTCP + Phase 3 finalize).
