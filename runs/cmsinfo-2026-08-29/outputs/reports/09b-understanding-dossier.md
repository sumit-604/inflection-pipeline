# CMS Info Systems Ltd (CMSINFO) — Halt 1 Understanding Dossier
Run: cmsinfo-2026-08-29 | CMP Rs243 (context only, not used in this document) | Assembled from committed blocks B00-B09, B12a-d, confidence.yaml, B13-lite. No new research in Sections 1-5. Section 6 opens named corpus text for anchored quotes per the Annex Exception.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** Four transcripts held: Concall_Nov_2025 (Q2 FY26), Concall_Feb_2026 (13-Feb-2026, Q3 FY26), Concall_May_2026 (Q4 FY26), Concall_Aug_2026 (Q1 FY27, quarter ended 30-Jun-2026) (B00, B05 quarters_analysed). Most recent quarter covered: Q1 FY27. Given run date 2026-08-29, the next quarter (Q2 FY27, ending 30-Sep-2026) has not yet closed and cannot plausibly have reported. No concall gap.
2. **ANNUAL REPORTS.** One AR PDF held: filename `Annual_Report_2023.pdf`, confirmed at p.2/147 to be the FY2025-26 Annual Report (collector mislabel, resolved) (B00 collect_defects, B03). This is the latest completed FY (year ended 31-Mar-2026) and it is present. Fewer than 3 years of AR PDFs are held — only FY26. Multi-year FY18-26 figures exist only via the screener Data_Sheet (aggregator tier, B01), not via prior-year AR PDFs.
3. **RESULTS FILINGS.** Two filings held: results/05f75e67 (14-May-2026, audited FY26 + Q4 results, 24pp) and results/e21eec72 (10-Aug-2026, Q1 FY27 results, 12pp) (B00). Latest results filing: 10-Aug-2026 (Q1 FY27). No quarter-gap to the AR: the AR covers the year ended 31-Mar-2026, matching the FY26/Q4 results filing.
4. **INVESTOR PRESENTATIONS.** One held: Investor_Presentation_1.pdf, Q1 FY27 deck (24pp, image-heavy, thin text extraction) (B00, B04). Latest available presentation.
5. **RESEARCH / RATING.** One rating rationale held: ICRA rationale (rating/142128.pdf), dated 31-Mar-2026, [ICRA]AA+ (Stable)/A1+ (B00). No CRISIL or CARE rationale in corpus (company memory gap G-6, unresolved — presence/absence of other agency coverage not established). Two non-anchored research items also present but out of Section 1-5 scope: an operator announcements digest and an operator web-leads note (ValuePickr thread), plus a misfiled broker "Weekly Wealth" BUY/HOLD/SELL note (91190-...pdf) filed under presentation/ by the collector (B00 collect_defects) — non-anchored, not used for any anchored claim in this dossier.
6. **CORPORATE ACTIONS.** Zero filed Reg-30 PDFs (B00: `announcements: 0`). The documented-action record for this run is reconstructed from concalls, results filings, and the investor presentation, anchored where the report reports a page/transcript-line cite, cross-checked against an operator-ferried non-anchored announcements digest. Reconstructed actions span roughly Jul-2025 (Securens first acquisition tranche) through Aug-2026 (Q1 FY27 call, most recent).
7. **FRESHNESS PAIR CHECK.** All four pairs PASS (B00 `freshness_verdict: FRESHNESS PAIRS OK`): results-to-concall (both Q4 FY26 and Q1 FY27 pairs), rating-bulletin-to-rationale (ICRA), SEBI-order-to-order-text (n/a, none referenced), AR-to-latest-audited-annual-results. No failed pair to name.
8. **VERDICT LINE: CORPUS GAPPED.**
   - Prospectus — absent — **plausibly-nonexistent** (IPO Dec-2021, >4.7y before run date; long-listed company, prospectus not expected in scope) (B00).
   - Filed Reg-30 announcement PDFs — absent — **findable-missing**, expected source: BSE/NSE exchange filings page. Reconstructed from concalls/results/presentation this run (B00).
   - Filed shareholding pattern (SHP) PDF — absent, screener-tier aggregator table substituted — **findable-missing**, expected source: BSE/company IR page (SHP is a mandatory quarterly filing) (B00).
   - Screener split financial CSVs (P&L/Balance Sheet/Cash Flow/Quarters, own + 6 peers) — populated with labels only, all figures empty — **findable-missing**, a collect_to_repo v3 collector defect; expected source: re-export from screener.in (B00, B01).
   - Prior-year Annual Report PDFs (FY23, FY24, FY25) — absent, only FY26 AR PDF held — **findable-missing**, expected source: company IR page / BSE filings archive. Needed to corroborate the Data_Sheet-only FY18-25 trend line with primary AR text and to test tone-drift year over year (B03 6D: "FY25 AR is not part of this run's inputs, so a direct prior-year tone comparison cannot be made").
   - CRISIL/CARE rating rationale (if any exists) — status unconfirmed — **findable-missing possibility**, expected source: rating agency site. Only ICRA is confirmed present in corpus (company memory gap G-6).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This section is a transition thesis, assembled from blocks. It is not signed here and cannot be signed until claude.ai stress-testing completes.

### PART A — THE FROM STATE

**A1. Archetype (per line).**
- ATM Management Solutions (~54% of revenue, B04) and Retail Solutions & Currency Logistics (~24%, B04): **Outsourcing partner** (cash-logistics/CIT managed service; long-tenor bank contracts, four-to-ten years, per B04/B03). Licence/scarcity elements also present (national CIT network, 97% geographic coverage) but the dominant economics are outsourcing-partner (client wallet share, contract stickiness), not pure scarcity rent.
- Technology & Payment Solutions (~15% of revenue and rising, HAWKAI Vision AI / ALGO / cards, B04): hybrid of **Outsourcing partner** and **Platform/network** — recurring, SaaS-like economics layered on the existing physical footprint, not yet a standalone platform business.
- Product/hardware trading (~7%, B04): fits no archetype in the library — pass-through trading, no moat, immaterial to the transition thesis.
- **Flag for operator ruling:** the manifest auto-picked sector row is "Platform / SaaS / IT services" (B00 collect_defects). This is likely WRONG. CMS is ~85% non-SaaS by revenue (B04 irrelevant_ratios); the correct FROM archetype is Outsourcing partner (business-services/cash-logistics platform), not pure SaaS. This sets the Section 1B cap at Stage 11 and must be re-ruled by the operator before valuation.

**A2. The simple analogy.** CMS is the company banks pay to move and refill their cash. It drives armoured vans, refills ATMs, guards cash in transit, and counts retail cash so banks and retailers do not have to run that operation themselves. On top of that older, physical business, CMS is layering cameras and software (HAWKAI, ALGO) that watch ATMs and bank branches remotely and hand banks data and alerts instead of just moving money.

### PART B — THE TRANSITION

**B1. From → to (per line, Quality Ladder).**
- Cash logistics core (ATM Management + Retail/Currency Logistics, ~78% of FY26 revenue, B04): **FROM R2 (Cost-Advantaged Converter)** — margin from route density and national scale, not price power, ROCE historically mid-20s but cyclical (B01: ROCE 25.2%→16.6% FY25→FY26) — **TO R3 (Value-Added / Spec'd Supplier)** — multi-year integrated bank contracts (SBI, ICICI, HDFC) and a shift from transaction-fee to fixed-price contracts (CEO letter, "now on fixed-price contracts") give partial pricing power and switching costs.
- Technology & Payment Solutions (HAWKAI/ALGO/cards, ~15%-16% of services revenue FY26, up from 12% FY25 and ~7% FY22, AR p.31/147): **FROM R2/R3** (nascent, embedded inside core client relationships) — **TO R4 (Franchise / Share-of-Wallet Leader)** — recurring SaaS-like revenue, a proprietary 16-year route/incident dataset (B07 D1), national deployment (50,000+ HAWKAI sites, CEO letter).

**B2. The engine.** Two things physically change: (1) contract mix shifts from transaction-linked/variable-fee arrangements to fixed-price, multi-year managed-service contracts across the three largest bank relationships (B04 revenue_streams; B05 trigger 2); (2) recurring technology revenue (HAWKAI/ALGO) is layered onto the already-built physical CIT/ATM network without proportional new fixed cost (B04 unit_economics key_lever).

**B3. The proof gate.** Technology & Payment Solutions crossing >20% of services revenue by end Q4 FY27 (from 16% FY26, management-guided, B05) **AND** EBITDA margin holding at or above ~26.5-27% for a full year, not one quarter (B05 trigger 3; currently one printed quarter at 27.2%, Q1 FY27). Until both print — not merely guide — the transition is narrative, not evidenced. Not yet fired: only one Tech-share data point (16% FY26) and one margin data point (27.2%, Q1 FY27 only) exist in corpus.

**B4. The recognition gap — OPEN QUESTION, not resolved here.** Does the market already price the shift toward Technology & Payments and fixed-price contracts into the current share price, or does the multiple still anchor to the legacy cash-logistics rung? This is stated as a question only; no number, no fair-value conclusion, is offered. Stage 11 resolves it via the Section 1B destination-PE gap.

**B5. The ugliness test.** FY26's ugly optic: post-tax ROCE fell from ~25% to 16.6% (B01, B03), the 1-2yr overdue receivables bucket grew 8.5x consolidated / 16.2x standalone while the standalone loss allowance was released 14.1% (B02, B03), core Cash Management segment external revenue fell 4.5-6.6% and segment result fell 25% (B02), and DSO rose 116→126 days.
   **Classification: UNRESOLVED — evidence genuinely supports both readings; this is exactly what B13's FLAG-CASH INDETERMINATE names, and it is preserved here rather than forced to a premature call.**
   - ARTIFACT-OF-CLIMB case: capex nearly tripled (Rs154 Cr→Rs409 Cr, B01) to build ~21,000 ATM units for the SBI/ICICI/HDFC/IPPB ramp; order book ~Rs1,400 Cr as of Dec-2025 (B05; ICRA rationale). ICRA's own rationale (31-Mar-2026) attributed the H1 FY26 receivable rise to delayed MSP payments with a securing arrangement in place and expected moderation to FY25 levels by fiscal year-end.
   - STRUCTURAL-FEATURE case: the audited full-year FY26 ageing shows the opposite of ICRA's forecast — the bucket did not moderate, it grew 8.5x. Two direct peers (RADIANTCMS, SIS) improved DSO in the identical window, removing the industry-wide excuse (B06 contradicted). The standalone provision was released against a 16.2x ageing surge in the same segment that is contracting, not the segment that is growing (B02/B03). One overdue receivable was converted into a distressed three-year secured term loan (B02/B03 Note 7/48).
   - This question is explicitly named in the gate recommendation as unresolved in Phase 1 and deferred to Stage 11 / claude.ai verification.

**B6. The transition falsifier.** If Technology & Payments' share of services revenue stalls or declines for two consecutive quarters, or if EBITDA margin reverts toward 24-25% once Q1 FY27's one-off tailwinds (ATM useful-life extension +Rs47.65m, ESOP cost swing -87.3%) roll off (B04 must_track_metrics; B05 trigger 3 kill_signal), the transition thesis is falsified — the arrow toward R3/R4 has not moved.

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables (derived from B2 engine and B3 proof gate).**
1. Technology & Payment Solutions % of services revenue (16% FY26; target >20% by Q4 FY27, B05).
2. EBITDA margin sustaining ~27% for a full year, not one quarter (currently one printed quarter, B05).
3. Core Cash Management segment revenue and result trajectory — recovery toward FY25 levels vs further decline (B02/B03).
4. Receivables ageing / DSO / loss-allowance coverage — moderation vs continued widening (B02/B03/B06).

**C2. What the model rejects.** Market-size questions are noise here: B09 already establishes a STRONG runway (9.1x revenue headroom, TAM Rs17,850-27,000 Cr) and materially revises the spear pass's "small pond" read upward for two of three platforms. The binding constraint is execution (contract ramp discipline, receivables quality, segment-reporting transparency), not addressable market. The model also rejects promoter-alignment questions as a signal source — no promoter exists (B08, structural, not a disclosure failure) — and rejects reading the FY26 ROCE/DSO deterioration purely as sector-wide cyclicality without weighing the peer contradiction (B06: RADIANTCMS and SIS both improved DSO in the same window).

**C3. The business falsifier** (distinct from B6 — kills the FROM business, not the arrow). A structural, multi-year decline in national cash usage — currency-in-circulation growth reversing, or UPI/digital substitution outpacing cash-ATM growth for several consecutive years (B09 downstream candidate) — combined with the core Cash Management segment's contraction proving permanent even after the currency-supply shock passes (B05 trigger 1 kill_signal: "fulfilment recovers but CMS revenue does not respond, falsifying the external-shock framing") would force a re-declaration of the FROM business itself, not merely the transition.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

CMS Info Systems moves and manages physical cash for banks and retailers across India. Its largest line, ATM Management Solutions, is about 54% of revenue (B04). This line replenishes ATMs, moves cash in transit, and runs brown label ATMs and banking automation for banks. Banks outsource this work because armoured fleets, vaults, and cash reconciliation are costly and risky to run in house. The second line, Retail Solutions and Currency Logistics, is about 24% of revenue and collects and carries retail cash and bullion (B04). The third line, Technology and Payment Solutions, is about 15% of revenue and sells HAWKAI Vision AI remote monitoring, ALGO ATM software, and payment cards, mostly on recurring terms (B04).

Customers are named banks: State Bank of India, HDFC Bank, Axis Bank, ICICI Bank, Punjab National Bank, and Hitachi Payment Services (B04). They buy through managed-service contracts that run four to ten years, which raises switching costs. Revenue concentrates in three large bank contracts and a handful of large customers: two customers together were 16% of Group revenue and a third was 10% in FY26 (AR Note 38, see Section 6 Q4).

Demand today rests on cash still in use. The signals to track are RBI currency in circulation, the total India ATM count with its outsourced share, and the national cash fulfilment rate (B09). Demand should grow as banks outsource more ATMs, as ATM penetration rises in semi-urban and rural areas, and as the AGS Transact insolvency vacates market share (B07, B09). The verifiable forward signals are the AGS Transact CIRP resolution, the SBI/ICICI/HDFC/IPPB contract ramp, and non-BFSI Vision AI tender wins (B09). UPI transaction volume is the counter-signal: digital-payment growth is the structural threat to cash volume (B09).

Competitive advantage sits unevenly across the lines. ATM Management holds the clearest moat: a national cash-in-transit network with about 97% geographic coverage and a 16-year route and incident dataset across 150,000+ touchpoints (B04, B07). Technology and Payment Solutions carries an emerging moat that is live and scaling but not yet dominant (B07: em_score 23, MODEST). Retail and Currency Logistics is mostly fixed-fee logistics with thin differentiation, and it fell about 8% in FY26 (B03 MD&A 5.1). The hardware-trading slice has no moat and is pass-through (B04).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**1. Technology & Payment Solutions % of services revenue.**
- Established (with cites): 16% of services revenue FY26, up from 12% FY25 and ~7% FY22 (AR Directors' Report, p.31/147); management guidance >20% by end Q4 FY27 (B05).
- Cannot establish: HAWKAI/ALGO standalone revenue and margin — declined by management every quarter asked (B05 repeated_evasions; B07 flags). The Tech segment revenue base is internally unreconciled across two consecutive concalls (Rs271 Cr Nov-2025 vs Rs216 Cr implied base Feb-2026, a Rs55 Cr gap, B12b MINOR finding, not flagged by B05 itself).
- Questions: (1) What is HAWKAI/ALGO standalone revenue and margin, not only a blended %? (2) Does the Tech segment revenue base reconcile across Nov-2025 to Feb-2026? (3) Is the >20% target organic, or does it lean on the FSS acquisition (guided ~4% of FY27 services revenue, Board's Report p.51/147)?

**2. EBITDA margin sustaining ~27% for a full year.**
- Established: Q1 FY27 printed 27.2% (B05); guidance raised to ~27% the same quarter FY27 revenue guidance was cut (LBF-3, B05).
- Cannot establish: whether Q1 FY27's tailwinds (ATM useful-life extension +Rs47.65m, ESOP cost swing -87.3%) recur in Q2-Q4, or whether EBIT (post-depreciation) margin — which compressed to 10.3% from 14.1% YoY even as EBITDA rose (B12b MAJOR finding) — recovers alongside EBITDA.
- Questions: (1) Does EBIT margin track EBITDA's improvement, or is the gap widening on depreciation? (2) Do Q2-Q4 FY27 margins hold at/above 26.5-27% once one-off items roll off? (3) How much of the margin raise is route automation/pricing discipline versus favourable accounting-estimate timing?

**3. Core Cash Management segment trajectory.**
- Established: external services revenue fell 4.5% SA / 6.6% CON and segment result fell 25% (Note 19/38, B02/B03); MD&A's own alternative-view segmentation shows ATM Management Solutions revenue -7.8% (B03 4C); segment-level profitability disclosure was retired coincident with the weakness (B05 flag).
- Cannot establish: whether the FY27 recovery management guides actually materialises, since forward segment-level P&L transparency has been foreclosed.
- Questions: (1) Will management restore segment-level disclosure? (2) Does the currency-supply-shock framing (LBF-2) hold up against independent CATMi/RBI fulfilment data? (3) Does the SBI/ICICI/HDFC/IPPB ramp offset the legacy segment's organic decline, or merely mask it at the Group level?

**4. Receivables ageing / DSO / loss-allowance coverage.**
- Established: 1-2yr overdue bucket +8.5x CON / +16.2x SA; SA loss allowance released 14.1% the same year; DSO 116→126 days; two direct peers (RADIANTCMS, SIS) improved DSO in the same window (B02/B03/B06).
- Cannot establish: management's own explanation — never given, deflected every quarter asked (B05 repeated_evasions); whether the MSP-securing arrangement ICRA cited actually resolved (ICRA's own forecast of moderation to FY25 levels by fiscal year-end was not borne out in the audited full-year figures, per the gate recommendation).
- Questions: (1) What specifically drives the 1-2yr overdue bucket growth — MSP delays, direct customer distress, or something else? (2) Does Q1-Q2 FY27 ageing disclosure show moderation or further widening? (3) Is the SA loss-allowance release justified by a documented ECL-methodology change, or is the book under-reserved?

### 4b. Candidate signal table (expanded from B09 downstream_candidates)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| RBI currency-in-circulation (CIC) | CIC growth reverses or flattens for 2+ consecutive quarters while CMS still claims cash-volume tailwind | Monthly | RBI Weekly Statistical Supplement / RBI DBIE |
| Total India ATM count and outsourced-vs-self-managed split | Outsourced share stalls or the self-managed conversion pool shrinks faster than CMS/peers can capture it | Quarterly | RBI DBIE / CATMi |
| AGS Transact Technologies CIRP resolution proceedings | Resolution awards the vacated ~90,000-ATM book to a well-capitalised new entrant rather than incumbents, contesting the AGS-share-capture thesis (B07 top_moat_risks) | Event-driven | NCLT Mumbai / IBBI / AGS exchange filings |
| SBI/ICICI/HDFC/IPPB contract ramp status | Any of the three signed contracts shows unexplained execution slippage beyond the already-disclosed SBI scope-halving (10,000→5,000 ATMs) | Quarterly | Company Reg-30 filings, quarterly investor calls |
| National cash fulfilment rate (indented vs received) | Fulfilment recovers to normal levels but CMS services revenue does not respond in lockstep, falsifying the external-shock framing (B05 trigger 1) | Monthly | CATMi press releases / IBA data |
| UPI transaction volume and value growth | UPI growth accelerates materially faster than CIC growth for several consecutive quarters, evidencing structural cash substitution | Monthly | NPCI monthly statistics |
| Non-BFSI Vision AI RFP/tender wins | Pipeline conversion stalls or a new entrant undercuts on price, per B07 top_moat_risks on D1 durability | Event-driven | Company Reg-30 filings / trade press |

### 4c. Fragility read

- **variable_count:** 6 — the four Section 2 C1 dominant variables plus two external/execution variables the bull case also needs: the currency-supply shock proving transitory, and the SBI/ICICI/HDFC/FSS contract ramp executing on schedule.
- **verifiability_ratio:** 3 of 6 externally observable — EBITDA margin (audited quarterly filings), receivables/DSO (audited AR/quarterly balance sheet), and the currency-supply-fulfilment rate (third-party CATMi/RBI/IBA data, B09) are externally checkable. Technology & Payments % (HAWKAI/ALGO standalone figures repeatedly declined, B05), core Cash Management segment trajectory (segment-level disclosure retired, B05), and contract-ramp execution detail (exact revenue contribution not disclosed) are company-narrated only.
- **single_point_failure:** none — failure requires conjunction, though receivables/DSO deterioration is the variable closest to a single-point kill switch given the sector precedent: AGSTRA's chronic, unresolved receivable-days drift preceded its Aug-2025 CIRP filing in this same industry (B06). On its own it would not close a zero-debt, cash-rich balance sheet, but combined with continued core-segment contraction it could compound quickly.
- **fragility_verdict:** MODERATE — six variables, half externally verifiable and half company-controlled disclosure (with two items management has actively declined to disclose), no clean single point of failure but a plausible compounding pathway through the receivables/DSO thread.

### 4d. Research brief (live-web work for claude.ai)

1. Confirm HAWKAI standalone revenue: Rs200 million (Directors' Report, AR p.31/147) vs ~Rs200 Cr (CEO letter, AR p.5/147; Investor Presentation slide 20) — a 100x internal AR discrepancy — via Reg-30 filing, exchange clarification, or IR contact.
2. Confirm SBI contract tenure (9yr MD&A vs 10yr Directors' Report) and HDFC tenure (3yr MD&A vs 5yr Investor Presentation) via a primary BSE filing or IR confirmation.
3. Verify national ATM cash-fulfilment data (CATMi's cited ~57% April-2026 national low) and RBI currency-in-circulation trend independently of CMS's own transcript, to test the LBF-2 external-shock framing.
4. AGS Transact CIRP resolution status (NCLT Mumbai / IBBI filings) — how much of the ~90,000-ATM book is being awarded, and to whom.
5. FSS Rs115 Cr acquisition: confirm completion status, funding source for the Rs550m balance payment, and actual revenue contribution beyond the ~Rs20 Cr Q1 FY27 accrual.
6. Fetch prior-year Annual Reports (FY23-FY25) from BSE/company IR to corroborate the Data_Sheet-only FY18-25 trend line with primary AR text, and to test tone drift year over year.
7. Fetch a filed SHP PDF (not the screener aggregator) for the most recent quarter(s) to confirm institutional/public holding precisely and check for any pledge disclosure beyond the screener table.
8. Track Q1 FY27 EBIT margin (not only EBITDA) into Q2 FY27 — confirm whether the 10.3% vs 14.1% YoY compression persists or reverses.
9. Seek any bank counterparty or MSP-side disclosure corroborating or rebutting the delayed-payment arrangement ICRA references, to independently test the growth-induced reading of receivables.
10. Search for a CRISIL or CARE rating rationale, if one exists, to cross-check ICRA's rationale and its (unmet) receivable-moderation forecast against an independent rating agency read.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. CMS Info Systems moves and manages physical cash for India's banks. It refills ATMs, drives armoured cash-in-transit vans, and counts retail cash.
2. Its biggest line, ATM Management, is 54% of revenue. It replenishes ATMs and runs banking automation for banks.
3. A newer line, Technology and Payment Solutions, sells cameras and software (HAWKAI, ALGO) that watch ATMs and bank sites and send data back to banks. It is 15% of revenue and growing.
4. Customers are named banks: SBI, HDFC, ICICI, Axis, PNB, and Hitachi Payment Services. Contracts run four to ten years.
5. Banks buy this service because running their own cash fleets and vaults costs more and carries more risk than paying CMS to do it.
6. Demand today depends on cash staying in use. UPI and digital payments are the counter force that could shrink it over time.
7. Demand can still grow because many ATMs remain self-managed by banks, not yet outsourced to CMS or a peer, and because a rival, AGS Transact, went into insolvency and vacated market share.
8. The corpus shows a large runway: CMS holds about 11% of its addressable market and about 9 times revenue headroom remains, if the plan executes.
9. CMS's moat is strongest in ATM Management: a network covering 97% of India's geography and 16 years of route and incident data. It is weaker in retail cash logistics and absent in hardware trading.
10. The emerging technology moat, built on HAWKAI and the data platform, is real but not yet dominant. It scored 23 of 60, just under the level this framework calls strengthening.
11. The mental model is a transition: CMS is trying to move from a cash-logistics business paid for volume to a platform paid on fixed contracts plus technology. Whether that shift has cleared its proof gate is not yet settled.
12. The fragility read is moderate. About six things must go right for the growth case, and only half of them are checkable from outside the company.
13. The corpus could not establish HAWKAI's standalone revenue for certain: one part of the annual report says Rs200 million, another part says roughly Rs200 crore, a 100 times gap.
14. The corpus could not establish exact segment-level profit for Technology and Payments going forward, because segment-level disclosure was pulled back the same year the legacy cash segment weakened.
15. The two biggest open questions: does the receivables and returns-on-capital weakness in FY26 fade as a one-year effect of heavy capex, or does it mark a real slowdown in the core cash business? And has the market already priced in the shift toward technology revenue, or is that shift still unrecognised?

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. UNITS

Quote (AR p.14/147, Business Overview market-map infographic): "Revenue: ~2.2 Lakh/ATM/p.a." (currency-outsourced, bank-owned ATM band); "Revenue: ~4.5 Lakh/ATM/p.a." (Brown Label ATM band); "Revenue: ~0.6 Lakh/ATM/p.a." and "Revenue: ~5 Lakh/ATM/p.a." (further bands on the same market-sizing chart, White Label / other categories per B04).
Comment: these are printed as **industry-wide reference bands** inside a market-sizing infographic — explicitly stated by B04 as "not CMS-specific actuals." No CMS-specific per-unit realisation (e.g., CMS's own realised revenue per managed ATM) is printed anywhere in the corpus. From the volume and revenue lines a blended figure can be derived, not read: FY26 ATM Management Solutions segment revenue was Rs5,872m (MD&A 5.1, AR p.52/147) against 70,000+ ATMs managed (Board's Report, AR p.31/147), implying roughly Rs8.4 lakh per managed ATM per annum on a blended basis across BLA, banking automation, and WLA — this is a derivation, not a disclosed unit figure, and mixes categories the printed bands keep separate.

### 2. SEGMENT CAPITAL AND DEBT

Quote (AR Note 38, Consolidated, p.132-133/147): "III Segment Assets — Cash Management services 10,421.75 / 10,562.80; Managed Services 13,158.42 / 9,437.78; Cards 352.04 / 267.98; Unallocated corporate assets 8,449.45 / 10,930.68; Total Segment Assets 32,381.66 / 31,199.24" and "IV Segment Liabilities — Cash Management services 3,597.99 / 3,229.63; Managed Services 3,841.08 / 4,647.60; Cards 98.27 / 128.36; Unallocated corporate Liabilities 520.90 / 528.51; Total Segment Liabilities 8,058.24 / 8,534.10" (Rs million, FY26 / FY25).
Comment: capital employed (Assets − Liabilities) by segment: Cash Management ~Rs6,823.76m (FY26) vs Rs7,333.17m (FY25); Managed Services ~Rs9,317.34m (FY26) vs Rs4,790.18m (FY25); Cards ~Rs253.77m (FY26) vs Rs139.62m (FY25). **Borrowings are not allocated by segment because there are effectively none to allocate:** SA CARO clause (ix) confirms no loans/borrowings from any lender during the year (NA); CON carries only a short-term borrowing of Rs271.46m drawn and fully repaid within the year, with zero closing balance (B03 2F). Group borrowings at year-end are effectively nil.

### 3. GUIDANCE VERSUS ASPIRATION

| Claim | Classification | Quote / figure | Source |
|---|---|---|---|
| FY27 total revenue Rs2,750-2,850 Cr | (a) guidance, period FY27 | "FY27 total revenue... Rs2,750-2,850 Cr" | AR MD&A Section 6 (B03) |
| FY27 services revenue Rs2,650-2,750 Cr (cut from Rs2,700-2,800 Cr) | (a) guidance, period FY27 | Q1 FY27 call, Aug-2026 (LBF-3) | B05 |
| FY27 EBITDA margin ~27% (raised from 25-26%) | (a) guidance, period FY27 | Q1 FY27 call, Aug-2026 | B05 |
| FY27 capex Rs100-125 Cr (down from FY26's ~Rs350 Cr) | (a) guidance, period FY27 | Q1 FY27 call, Aug-2026 | B05 |
| FY30 services revenue CAGR 13-14% to Rs3,750-3,950 Cr | (a) guidance with a period (FY30), but no interim checkpoints disclosed | AR MD&A / Q4 FY26 call, May-2026 | B03/B05 |
| Segment-level FY30 CAGRs: ATM Mgmt ~11%, Retail/CIT ~11%+, T&PS ~20%+ | (a) guidance with a period (FY30), segment-specific, no interim checkpoints | AR MD&A | B03 |
| Tech & Payments crossing >20% of services revenue by end Q4 FY27 | (a) guidance, period Q4 FY27 | Q1 FY27 call, Aug-2026 | B05 |
| "No competitor can replicate this in five years or ten" | (c) capacity/capability only, no period | CEO letter, AR front matter | AR (quote confirmed in corpus) |
| "97% of India's geography" coverage | (c) capacity/capability only | Board's Report, AR p.31/147 | AR |

### 4. CONCENTRATION

Quote (AR Note 38, Consolidated, p.133/147): "Revenue for the period ended March 31, 2026 includes revenue from two customer of the Group relating to Cash management services and Managed service segments amounting to H 3,994.52 million representing 16% and another customer amounting to H 2,526.18 million representing 10% of the Group's total revenue." FY25 comparative, same note: "revenue from two customer of the Group... amounting to H 5911.95 million representing 24% and another customer amounting to H 2,464.46 million representing 10% of the Group's total revenue."
Comment: top disclosed customer concentration = two customers together ~16% plus a third at ~10% of FY26 Group revenue (~26% combined), customers identified by number, not by name. Concentration eased YoY (FY25 was 24%+10% = 34%). Product/segment concentration is implicit in the Note 38 revenue split (Cash Management ~64%, Managed Services ~42%, Cards ~3% of gross segment revenue before elimination — self-computed from the Total Segment Revenue rows) but is not disclosed as a standalone % metric. Geography concentration: NOT DISCLOSED as a segment — CMS reports no separate geographic segment; the only geography-related quote found is a coverage claim, not a revenue-by-region breakdown: "operates across 97% of India's geography" (Board's Report, AR p.31/147).

### 5. PROMISE LEDGER

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 (Nov-2025) | FY26 services revenue growth 8% | Actual 6% | Q4 FY26 call (B05) |
| Q2 FY26 (Nov-2025), reaffirmed Q3/Q4 | FY27 services revenue Rs2,700-2,800cr | Cut to Rs2,650-2,750cr | Q1 FY27 call (B05, LBF-3) |
| Q2 FY26 (Nov-2025), reaffirmed Q3 FY26 | ATM count 74,000-75,000 by March/April 2026 | Still ~70,000 as of Q1 FY27 call; silently dropped | B05 |
| Q3 FY26 (Feb-2026) | Q3 margin bottom; Q4 +150-170bps; FY27 25-26% | Q4 +280bps delivered; Q1 FY27 further +170bps to 27.2%; guidance raised | B05 |
| Q3 FY26 (Feb-2026) | DSOs back to normal by end of March 2026 | Never mentioned again; external evidence shows deterioration | B05 |
| Q2 FY26 (Nov-2025) | SBI RFP, Rs500cr incremental over 10 years | Contracted Dec-2025; scope revealed as ~5,000 ATMs (L1 of a re-bid), not the original 10,000-ATM award; headline Rs500cr held | B05; Concall_Feb_2026 p.12/19 (see quote below) |
| Q2 FY26 (Nov-2025) | Margins trend back to FY25 level (~26.1%) by fiscal year end | FY26 full-year margin ~24.0-24.1%, still below FY25; Q4 alone reached 25.6% | B05 |
| Q2 FY26 (Nov-2025) | October retail recovery to sustain, driving H2 sequential improvement | Q3 FY26 growth only 4% QoQ; Q4 6% QoQ, helped by GST 2.0 | B05 |
| Q3 FY26 (Feb-2026) | FSS deal (Rs100-125cr) close by March-end 2026 | Slipped to end of Q1 FY27; confirmed closed with ~Rs20cr Q1 revenue accrual | B05 |

SBI-scope quote (Concall_Feb_2026, [[PAGE 12/19]]): Analyst: "for the SBI order, there were talks of 10,000 ATMs that were in freight for the outsourcing. But the announcement that we made is it pertaining to 5,000 ATMs." Management (Anush Raghavan): "the total order is 10,000 in terms of what SBI wants to award... in the first version of the outsourcing process, we were the only eligible participant... But unfortunately, with that getting scrapped and then coming out with a new RFP, of that, we were the L1 participant. So we got about 5,000 of those volumes with rest going to other industry participants."

### 6. RESTATED BASES

Quote (AR CON Note 37, p.131/147, footnote): "During the year, Group has presented provision for ATM cash shortage and claim instead of loss allowance for the ATM cash replenishment business which is dislosed under provisions (refer note 17)." The comparative "Transfer to cash loss provision considered separately" line moves Rs577.49m out of the SA loss-allowance roll-forward (SA Note 37, p.99/147) and Rs662.80m out of the CON roll-forward (CON Note 37, p.131/147), for the FY25 comparative.
Comment: this reclassification breaks like-for-like YoY comparability of the loss-allowance/provisioning trend (B02 red flag) — a reader comparing FY25-to-FY26 loss allowance without adjusting for this transfer would misread the direction of the provisioning trend.

Second restatement, quote (AR Note 14, SA, p.90/147): "188,000,000 (March 31, 2025 - 173,000,000) equity shares of H 10 each ... 1,880.00 / 1730.00" and "Nil (March 31, 2025 - 1,500,000) 0.01% Optionally convertible cumulative redeemable preference shares of H 100 each ... - / 150.00".
Comment: authorised share capital reclassified from 173,000,000 to 188,000,000 equity shares (+Rs150.00m) at FY25 close, offsetting the cancellation of 1,500,000 OCCRPS (Rs150.00m). Mechanical capital-structure change, not an earnings restatement (B02).

### 7. CORPORATE-ACTION CLAUSES

**(a) Securens acquisition.** Quote (Board's Report, AR p.33/147): "the Company completed the acquisition of 100% equity share capital of Securens Systems Private Limited ("Securens") in a phased manner between July 2025 and March 2026. Securens, a pioneer in AIoT-enabled remote monitoring and Vision AI surveillance solutions, became a wholly-owned subsidiary of the Company effective March 9, 2026, upon the successful closure of the final tranche." Consideration: "Securens in July 2025 for H75 Cr" (CEO letter, AR front matter). B07 flags an unreconciled internal inconsistency (Rs75cr letter figure vs a ~Rs80cr infographic elsewhere in the AR).

**(b) FSS acquisition.** Quote (AR Note 31(b), SA, p.96/147): "Nil Capital commitment for the year ended March 31, 2026 (March 31, 2025 H93.63)." Quote (AR Note 10, SA, p.89/147, per B03): FSS agreement Rs1,150m total, Rs600m paid 30-Mar-2026, Rs550m balance on completion. This Rs550m forward obligation is absent from the capital-commitments note despite the signed binding agreement — a disclosure-completeness gap (B02 WATCH finding), not a narrative concealment (the deal is separately and prominently narrated in the Board's Report and CEO letter). Appointed/effective date for full completion: NOT FOUND in this AR — guided for H1 FY27 but not yet crystallised.

**(c) Buyback.** Quote (Board's Report, "Material Changes and Commitments," AR p.31/147): "The Board of Directors at its meeting held on May 14, 2026, has approved a proposal for buyback of up to 4,939,126 fully paid-up equity shares of face value of H 10 each from the existing members of the Company on a proportionate basis through the Tender Offer route. The buyback is being undertaken at a price of H 340 per equity share for an aggregate consideration not exceeding H 1679.30 million, in accordance with the provisions of Sections 68, 69, and 70 of the Companies Act, 2013, and the SEBI (Buy-Back of Securities) Regulations, 2018." Executed 19-Jun-2026 (B02/B08), ~3% of equity.

No demerger, merger, or preferential issue found anywhere in this corpus; NOT APPLICABLE this run.

### 8. RELATED-PARTY PERIMETER

Quote (AR Note 30, SA, p.86/147, intra-group "Service charges," latest year FY26 vs FY25): CMS Marshall Limited Rs1,220.89m→Rs1,523.22m (+24.8%); Securitrans India Pvt Ltd Rs201.50m→Rs404.03m (+100.5%, unreconciled divergence per B03); CMS Securitas Limited Rs273.59m→Rs294.20m (+7.5%); Hemabh Technology Rs166.99m→Rs126.66m (-24.2%). Sum of major service-charge RPTs ≈Rs2,439.35m against SA revenue Rs22,721.92m ≈ 10.7% of revenue. Corporate guarantees (Note 31(a), SA, p.96/147): Rs600m to Securitrans lenders + Rs200m customer vaulting facility = Rs800m contingent exposure. Loan to subsidiary Securens (CARO clause iii): Rs58.5m advanced / Rs45.28m outstanding. Board's Report affirms (p.48/147, per B03): "no materially significant related party transaction" during the year, all RPTs at arm's length.
Comment: all named entities are Group subsidiaries/step-down entities. No promoter-group entity exists to receive RPT flow, since no promoter has existed since Apr-2025 (B08).

### 9. PLEDGE AND SHAREHOLDING

Twelve-quarter table (source: screener.in quarterly shareholding pattern, operator-ferried 2026-08-29, aggregator tier, not a filed SHP PDF):

| Quarter | Promoters | FIIs | DIIs | Public |
|---|---|---|---|---|
| Sep 2023 | 26.69 | 23.76 | 23.98 | 25.56 |
| Dec 2023 | 26.69 | 23.76 | 23.43 | 26.13 |
| Mar 2024 | 0.00 | 36.34 | 29.01 | 34.65 |
| Jun 2024 | 0.00 | 40.21 | 28.40 | 31.40 |
| Sep 2024 | 0.00 | 39.99 | 26.66 | 33.35 |
| Dec 2024 | 0.00 | 37.95 | 27.03 | 35.01 |
| Mar 2025 | 0.00 | 37.80 | 26.45 | 35.77 |
| Jun 2025 | 0.00 | 36.96 | 26.61 | 36.42 |
| Sep 2025 | 0.00 | 33.15 | 28.69 | 38.14 |
| Dec 2025 | 0.00 | 28.20 | 32.61 | 39.18 |
| Mar 2026 | 0.00 | 24.97 | 35.17 | 39.87 |
| Jun 2026 | 0.00 | 22.70 | 36.00 | 41.29 |

Comment: promoter category has been 0.00% since Mar-2024 (Sion/Advent-Baring exited Feb-2024, declassified promoter-to-public wef 2-Apr-2025) — structural, not a disclosure failure. Institutional holding latest (Jun-2026): FII 22.70% + DII 36.00% = 58.70% combined. Pledge: AR Board's Report Section 7(c) confirms "no promoter/promoter-group category exists" and B03 5D independently confirms "no pledge disclosed anywhere" in the shareholding pattern. This table is aggregator-tier, sufficient to close the FII/DII trend and confirm no-promoter status, per B00 input_gaps; not a substitute for a filed SHP PDF.

### 10. VERIFICATION

Documents quoted in this annex:
- `Annual_Report_2023.pdf` — mislabeled by the collector; confirmed at p.2/147 to be the FY2025-26 Annual Report, signed 14-May-2026 (work/txt/annual-report/Annual_Report_2023.txt)
- `05f75e67-7f39-4b02-b881-c6635b448b71.pdf` — audited FY26 + Q4 results, 14-May-2026 (work/txt/results/)
- `e21eec72-688c-4d1b-8735-d95491b67fc3.pdf` — Q1 FY27 results, 10-Aug-2026 (work/txt/results/)
- `142128.pdf` — ICRA rating rationale, 31-Mar-2026, [ICRA]AA+ (Stable)/A1+ (work/txt/rating/)
- `Concall_Nov_2025_Transcript.txt` — Q2 FY26 earnings call, Nov-2025 (work/txt/concalls/)
- `Concall_Feb_2026_Transcript.txt` — Q3 FY26 earnings call, 13-Feb-2026 (work/txt/concalls/)
- `Concall_May_2026_Transcript.txt` — Q4 FY26 earnings call, May-2026 (work/txt/concalls/)
- `Concall_Aug_2026_Transcript.txt` — Q1 FY27 earnings call, Aug-2026 (work/txt/concalls/)
- `Investor_Presentation_1.pdf` — Q1 FY27 investor deck (inputs/presentation/)
- `shareholding-pattern-screener-quarterly.txt` — screener.in quarterly shareholding pattern, operator-ferried 2026-08-29 (inputs/shareholding/)

CORPUS COMMIT HASH: 09d50d8888e3ce9ec7b51b9396405450c8bfb90b
