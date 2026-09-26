# STAGE 4: BUSINESS MODEL DECODER — Avience Biomedicals Ltd (AVIENCE)
Run date: 2026-09-26 | Model: claude-sonnet-5

Primary sources: RHP business chapter (RHP_Avience_Biomedicals_Jun2026.txt, cited as "RHP p.__" using the printed page number shown as "[page N]" in the text), FY26 AR (referenced via B01-B03 blocks where the AR itself was not re-opened this stage; anchors marked "AR" trace to B02/B03), H2 FY26 concall transcript (Concall_Jul_2026_Transcript.txt, cited "call p.__"), H2 FY26 investor deck (Investor_Presentation_1.pdf, cited "Inv. Pres. slide __" by PDF page; image-only slides read from PNG renders). Input gap: the investor deck's text layer covers only 6 of 29 pages; 23 pages were read as rendered PNGs per the task brief.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

Avience makes and sells the reagents, test kits and analysers a hospital or lab uses to test blood and other samples (in vitro diagnostics, "IVD"), and separately resells a global brand's (Mindray's) diagnostic equipment and reagents as its regional distributor, with most of its own instruments given away free and paid for through the reagents that run on them.

### 1B. Money flow chains, one per revenue stream

1. **Traded reagents & consumables (59.83% of FY26 turnover, call p.7)**
   [Buys finished Mindray reagents/consumables] -> [Avience resells/distributes them as Mindray's regional channel partner for Delhi NCR + eastern UP] -> [delivers to hospitals, labs, diagnostic centres] -> [hospital/lab pays] -> [pays on invoice, RHP shows government-linked receivables run 90-120 days per management (call p.5); no rupee AR/RHP ageing figure ties to this stream alone].

2. **Traded instruments (12.55%, call p.7)**
   [Buys Mindray analysers/instruments] -> [Avience sells ~10-15% of all instruments outright, or PLACES ~80-85% of them free at the customer site under a reagent-rental contract, typically 5 years (call p.6-7)] -> [instrument installed at hospital/lab] -> [customer pays only if bought outright; if placed, no separate instrument revenue is booked (call p.7)] -> [one-time payment on outright sale; on placement, the instrument itself earns nothing directly and is recovered through the reagent stream below].

3. **Manufactured reagents & consumables (14.62%, call p.7) + rapid cards (9.15%, call p.7)**
   [Buys raw chemicals/plastics] -> [Avience manufactures under 88 CDSCO product licences at its rented Noida facility (call p.3; RHP)] -> [delivers under its own brand to hospitals, labs, government tenders (B2B/B2C/B2G, RHP p.161)] -> [customer pays, standard trade terms] -> [collection 30-90+ days depending on channel, longer for government (call p.5)].

4. **Manufactured instruments (3.21%, call p.7)**: oxygen concentrators, biochemistry and haematology machines built in-house -> sold outright or placed -> same reagent-rental logic as (2) applies once placed.

5. **Reagent-rental recurring stream (embedded inside streams 1 and 3, not separately broken out)**: [Instrument placed free at customer site, 5-year term] -> [customer is contractually tied to buy that instrument's reagents/consumables from Avience at agreed prices, 80-90% of the reagent business is this "closed system" (call p.6)] -> [recurring monthly/periodic reagent purchase] -> [rental-model margins run 40-60% vs manufacturing margins of 30-70% by product, per management (call p.6-7)]. This is the economic engine sitting underneath streams 1 and 3.

6. **Service income (AMC/CMC, balance of turnover, call p.7)**
   [Instrument warranty expires] -> [customer pays for Annual/Comprehensive Maintenance Contract] -> [Avience's service team repairs/maintains, targets 4-hour response (call p.3)] -> [customer pays annual fee] -> [was negligible through FY24, growing as the installed base ages (RHP p.165-166)].

### 1C. Revenue model classification table

| Stream | Type (taxonomy) | Description | % of FY26 revenue (anchor) | Predictability |
|---|---|---|---|---|
| Traded reagents/consumables | Distribution/resale, partly recurring closed-loop | Mindray-sourced consumables resold, 80-90% closed-system (call p.6) | 59.83% (call p.7) | M — recurring on placed base, but single-supplier dependent |
| Traded instruments | One-time distribution sale (10-15% of units) / capex placement (85-90%) | Mindray equipment, mostly placed free, not directly monetised | 12.55% (call p.7) | L — lumpy, order-driven (e.g. the ~Rs 47 Cr Uttarakhand order, call p.5) |
| Manufactured reagents/consumables | Manufacturing, own brand, partly recurring | In-house IVD reagents under 88 CDSCO licences | 14.62% (call p.7) | M — recurring but small base today |
| Manufactured rapid cards | Manufacturing, transactional | Pregnancy, dengue, HIV etc. rapid test kits | 9.15% (call p.7) | L/M — event/outbreak-linked in parts (COVID-era history) |
| Manufactured instruments | Manufacturing, one-time/capex | Oxygen concentrators, biochemistry/haematology analysers | 3.21% (call p.7) | L — lumpy |
| Service (AMC/CMC) | Recurring service fee | Post-warranty maintenance contracts | ~0.64% residual (derived; call p.7 does not sum to 100%; NOT FOUND as an explicit named %) | M — grows with installed-base age (RHP p.165-166) |

### 1D. Simplified business model canvas

| Dimension | Reading |
|---|---|
| What they sell | IVD reagents, rapid test kits, analysers/instruments; own-brand manufactured plus third-party (Mindray) traded goods |
| Who buys | Hospitals, private labs, diagnostic centres (B2C, 45.17% of standalone 10M-FY26 revenue), other businesses/distributors (B2B, 45.30%), government (B2G, 7.77%), export (1.76%) (RHP p.161) |
| Why them | Regulatory head start (88 CDSCO licences, 9-12 month approval cycle, Inv. Pres. slide 13), regional Mindray channel-partner status (call p.4), 4-hour service-response commitment (call p.3) |
| How delivered | Direct sales force plus pan-India distribution network (Inv. Pres. slide 5); instruments installed on-site, reagents replenished on a recurring basis |
| Cost structure dominance | Purchase of stock-in-trade (traded goods) is the single largest cost line: Rs 2,698.36 lakh of Rs 4,032.92 lakh total FY26 consolidated expenses, ~67% (Inv. Pres. slide 26) |
| Scarce resource | CDSCO manufacturing licences (88 held, 200+ in pipeline, 9-12 month approval lead time, Inv. Pres. slide 13) and the regional Mindray channel-partner allocation (call p.4) |
| Pricing power source or absence | Weak on the traded 72% of revenue (non-exclusive regional distributor of someone else's brand, call p.4); moderate on the closed-loop reagent-rental base (customer is contractually locked to Avience's reagents for the placement term, call p.6-7); largely absent on rapid cards (commodity IVD category, many licensed competitors) |
| Asset intensity | Rising: PPE + CWIP grew from Rs 1,757.83 lakh to Rs 2,876.92 lakh FY25-FY26 consolidated (Inv. Pres. slide 27); 72% of standalone net PPE is instruments held at third-party (customer) sites (B02 FLAG-DISCLOSURE, CARO (i)(b)) |
| WC intensity | High and rising: consolidated debtor days 146, inventory days 218 (B00 LBF4); FCF negative three years running (B01) |
| Regulatory moat or burden | Both: CDSCO licensing is a genuine barrier to new entrants (Inv. Pres. slide 13, "strong regulatory entry barrier") but also a burden — 9-12 months per licence gates Avience's own pipeline expansion (200+ products in process, call p.3) |

### 1E. The chai-stall-uncle version

Avience is like a chai stall that also happens to be the local dealer for a big kettle brand. Most days, it sells its own tea leaves and cups (manufactured reagents), which it makes itself and keeps most of the profit on. But most of its turnover today, seven out of every ten rupees, comes from selling someone else's branded kettles and refills (Mindray's instruments and reagents) on commission as the regional dealer (call p.6-7). The clever bit: instead of selling the kettle, the stall often just gives the kettle away free to a good customer, and signs them up for five years of buying tea leaves only from this stall (the reagent-rental model, call p.6-7). That is a good deal once it works, but it means the stall now owns a lot of kettles sitting in other people's kitchens, paid the kettle-maker up front, and waits months to collect on the tea leaves it delivers, especially from government canteens.

### Section 1 summary table

| Field | Reading |
|---|---|
| Business type | Hybrid: manufacturing + distribution/agency, with an embedded equipment-placement (razor-and-blade) model |
| Revenue nature | Mixed transactional (traded goods, ~72% of turnover) and semi-recurring closed-loop (reagent-rental on placed instruments, 80-90% of reagent/consumable revenue is closed-system per call p.6) |
| Asset intensity | Rising / medium-heavy (CWIP for new plant, plus growing off-balance-location instrument base) |
| WC intensity | High (debtor days 146, inventory days 218, B00 LBF4) |
| Pricing power | Weak on the traded 72%, moderate on the closed-loop placed base, weak on rapid cards |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Reading | Helps/Hurts/Neutral |
|---|---|---|
| Competition count | Named leading players in India's IVD market: Roche, Abbott, Siemens Healthineers, Transasia, Beckman Coulter (Inv. Pres. slide 20, "Leading Players"); domestic peers in this run's set: QLINE (Q-Line Biotech), MOLBIO, TARSONS (step1 brief). No count of total licensed IVD manufacturers found in the corpus | Hurts — Avience is small next to Roche/Abbott/Siemens/Transasia/Beckman Coulter |
| Entry barriers | CDSCO manufacturing licence process takes 9-12 months average, per the company's own deck (Inv. Pres. slide 13); 88 licences already held is cited as a "strong regulatory entry barrier" by management itself | Helps, but see caveat below — the same barrier gates Avience's own 200+ pending approvals |
| Supplier power | Mindray supplied 63.0% of purchases 10M-FY26 (66.3% FY25, 72.7% FY24, 68.85% FY23, RHP p.36/163), a NON-exclusive regional arrangement (call p.4) that Mindray could reallocate or narrow | Hurts — a single trading/raw-material supplier holds two-thirds of Avience's purchases |
| Customer power and concentration | Top 10 customers are over 50% of revenue and unnamed for confidentiality (RHP p.34); named accounts on the call are Max Healthcare, Sarvodaya Hospital, Dr. Lal PathLabs (call p.3) | Hurts — concentrated, unnamed book |
| Substitutes | Rapid test cards face many licensed competitors (commodity IVD category); reagent-rental locks in the customer for the placement term (5 years, call p.7), reducing substitution risk on that specific slice | Mixed — hurts on rapid cards, helps on the closed-loop placed base |

### 2B. Competitive positioning map

| Player | Position vs Avience |
|---|---|
| Roche, Abbott, Siemens Healthineers, Beckman Coulter (named, Inv. Pres. slide 20) | Global multinational IVD majors; Avience competes for the same hospital/lab customers at a fraction of the scale; no revenue/market-share comparison in the corpus |
| Transasia | Named by Avience's own deck as "No.1 Diagnostic Company in India" (Inv. Pres. slide 20) — the domestic scale leader Avience is furthest from |
| Mindray Medical India | Not a competitor — Avience's own principal/supplier for the traded 72% of revenue (call p.4) |
| QLINE (Q-Line Biotech) | Peer selected for this run: Lucknow IVD maker/distributor, same North India geography, same manufacturing+trading mix (step1 brief) — closest direct mirror |
| MOLBIO Diagnostics | Peer selected as the destination-model mirror: closed-loop platform + captive consumables, the model Avience says it is moving toward (step1 brief) |
| TARSONS Products | Peer selected for the capex-to-utilisation-ramp comparison (new Panchla plant), mirroring Avience's YEIDA ramp (step1 brief) |

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Network effects | No | Not found in corpus | n/a |
| Switching costs | Partial | Reagent-rental locks the customer to Avience's reagents for the 5-year placement term (call p.7); AMC/CMC contracts add a maintenance dependency (RHP p.165-166) | Moderate — bounded by contract term, and the concall itself describes a PLANNED move to true closed-loop (barcoded, incompatible-with-third-party reagents) as not yet built (call p.4, "the proposed system would be designed") |
| Brand | Weak on own brand ("Avienbio"); borrowed on the traded side from Mindray's brand, which Avience does not own | Low durability — a distribution arrangement, non-exclusive, at state/regional level (call p.4) |
| Cost advantage | Not evidenced; no cost-curve or scale data in corpus | NOT FOUND |
| Regulatory/licence | Yes | 88 CDSCO manufacturing licences, 9-12 month approval cycle cited as a barrier by management (Inv. Pres. slide 13) | Moderate — real barrier to a new entrant, but does not stop Roche/Abbott/Transasia, who already clear it at far larger scale |
| Scale | No — Avience is small versus named majors | n/a | n/a |
| Data/IP | Not evidenced | NOT FOUND | n/a |
| Distribution/relationships | Yes, partial | Regional Mindray channel-partner status for Delhi NCR + eastern UP (call p.4); named institutional accounts (Max Healthcare, Sarvodaya, Dr. Lal PathLabs, call p.3) | Weak-moderate — the Mindray relationship is explicitly non-exclusive and could be reallocated; the OEM/private-label and exclusivity discussions are unsigned (call p.4) |

**Net moat read**: two soft, partial moats (switching-cost via reagent-rental; licence/regulatory), neither yet strong enough on its own to explain durable pricing power. This differs from B01's automated moat scoring (moats_confirmed: 4, moat_class STRONG), which used the fixed-formula scorecard on financial proxies; this qualitative pass finds the underlying economic moats thinner and more contract-term-bounded than that score implies. Flagging the gap for Role 2 to resolve, not overriding either number.

### 2D. Industry lifecycle stage

India's diagnostics market is in a mid-growth phase: from Rs 675.8 billion (FY20) to a projected Rs 1,964.3 billion by FY30, ~11.5-11.7% CAGR through the period, with IVD contributing ~57% of the total diagnostics market in FY25 (Inv. Pres. slide 18, source cited on-slide as "Lattice Analysis"). Avience itself is a small, recently-listed (Jun-2026) sub-scale player inside this growing market, currently mid-transition from a trading-heavy to a manufacturing-heavier mix (27:72 manufacturing:trading today, targeting ~50:50, call p.6).

### 2E. Key industry drivers

| Driver | Direction | Impact on Avience |
|---|---|---|
| Rising disease burden (TB, diabetes, cancer, cardiovascular) | Positive, structural | Grows the addressable testing volume industry-wide (Inv. Pres. slide 18) |
| Health insurance penetration rising (25% -> 51% cited) | Positive | Improves affordability, indirectly supports volumes (Inv. Pres. slide 18) |
| Government initiatives (NHM, free diagnostics) and Tier-2/3 chain expansion | Positive | Feeds the B2G channel (7.77% of standalone revenue) and the stated government-tender growth push (call p.4, p.8) |
| Rapid adoption of molecular diagnostics, AI/digital reporting | Neutral-to-positive, unproven for Avience specifically | Avience holds "Molecular Diagnostics" as a named category (Inv. Pres. slide 7) but no revenue-share figure for it was found separate from the broader manufactured-reagent line |
| Import substitution / Make in India push | Positive, cited by management | New YEIDA facility "designed with WHO prequalification requirements in mind" for export ambitions (call p.8); central/state medical-device-park subsidies named (concessional land, ~Rs 3.50/unit power, ~7% interest subsidy on eligible plant/machinery funding, call p.8) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these

| Commonly tracked ratio | Misleading/Irrelevant here | Why |
|---|---|---|
| Gross margin (single blended number) | Misleading | Blends a ~40-60% reagent-rental margin business with 30-70% manufacturing margins and a lower-margin pure-trading slice (call p.6-7); a single blended gross margin hides which engine is actually driving the change |
| Revenue growth alone (no mix disclosure) | Misleading | A 60%+ FY27 growth number (call p.3) driven mostly by one ~Rs 47 Cr Uttarakhand equipment order (largely traded/instrument-heavy per B02's flagged concern) reads very differently from the same growth number driven by manufactured-reagent volume |
| Standard manufacturer inventory-turn benchmarks | Misleading | 218 days of consolidated inventory (B00 LBF4) partly reflects placed-instrument-linked reagent stocking and a genuine finished-goods build (+80.9% YoY, B02 flag); comparing this to a pure-play manufacturer's inventory norm overstates the concern without splitting placement stock from sell-through stock |
| PPE turnover / fixed-asset turnover | Misleading | 72% of net standalone PPE sits at third-party customer sites as placed instruments (B02 flag, CARO (i)(b)); a standard asset-turnover ratio conflates revenue-generating owned manufacturing assets with reagent-rental placement assets that earn indirectly |
| Days payable outstanding, taken alone as a "strength" | Misleading | MSME trade payables grew +314% standalone (B02 finding #10); a rising payable-days number here may reflect supplier-financing stretch, not negotiating power |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range (this business) | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Manufacturing:Trading revenue mix | Whether the margin-accretive shift management guides to is actually happening | Moving from ~27:72 toward ~50:50 (call p.6) on schedule | Half-yearly results/AR segment note | Mix stuck near 27:72 past FY27 |
| Order-to-delivery conversion on the ~Rs 47 Cr Uttarakhand order | Tests whether guided growth is real or promotional | Delivered within the stated "3-4 months" (Inv. Pres. slide 24) with no Reg 30 order-confirmation filing gap | Reg 30 filings, half-yearly results | No Reg 30 filing ever appears (per B00, none exists since listing) |
| Export revenue (FOB) | Tests FY27 Rs 5-7 Cr export guidance credibility | Growth off the true FY25 base (Rs 5.24 Cr, RHP), not the artificially depressed FY26 base (Rs 53.11 lakh, B02 flag) | AR export note, RHP p.161 | Export stays near FY26's Rs 53 lakh level |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| EBITDA margin, split by segment if ever disclosed | Whether the mix shift is margin-accretive as claimed | Improving from 28.45% FY26 (call) toward management's stated aspiration | Half-yearly results | Margin flat or falling despite the guided mix shift |
| Reagent-rental gross margin (if ever separately disclosed) | Direct test of the 40-60% figure management cites | 40-60% sustained (call p.6-7) | NOT currently disclosed as a separate line; request at future calls | Falls materially below 40% |
| Cash conversion (CFO/EBITDA or CFO/PAT) | Whether reported profit growth is translating to cash | Should climb toward/above 0.70x | Half-yearly results cash flow statement | Sub-0.70x for a third straight year (already 0.478x FY25, 0.675x FY26 consolidated per B03) |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Debtor days, split traded vs manufactured if possible | Tests whether the government/traded-order growth is dragging collections | Should stabilise or fall from 146 days | Half-yearly results, AR ageing note | Continued rise past 146 days, or aged (>6 month) receivables share continuing past the 38.9% standalone level already seen (B02) |
| Net PPE held at third-party sites, as % of total net PPE | Tracks the size and control risk of the placed-instrument base | Growing in line with reagent-rental revenue, ideally with improved verification disclosure | AR Note 12(b)/13(b), CARO Annexure | Continued growth with no improvement in physical-verification coverage (currently excluded per CARO (i)(b), B02) |
| YEIDA CWIP-to-PPE capitalisation and SIDBI debt service timing | Tests execution on the single biggest capex bet | Capitalised to PPE and commercial by Oct-2026 per guidance | AR PPE/CWIP notes, Reg 30 filings | Commissioning slips while SIDBI repayment (already begun, B03) continues |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find it |
|---|---|
| Number of CDSCO product licences held / in pipeline (88 held, 200+ pipeline, targeting 175 by end-FY27, call p.5) | Investor deck (Inv. Pres. slide 13-14), concall |
| Installed instrument base under reagent-rental placement, and its renewal schedule | NOT FOUND as an absolute count in this corpus; only percentages (80-85% of instruments placed, call p.7) |
| Capacity utilisation by product line: Rapid Test 84.12%, Reagents & Consumables 85.23%, Analysers/Instruments 80.57%, Culture Media 74.53% (10M FY26, standalone) | RHP p.157-158/163-164 |
| Repeat-customer counts by channel (B2B/B2C/B2G/Export) | RHP p.230-231 (customer table, "Repeated Customers") |
| YEIDA plant commissioning milestones (substantially complete by Sept, production from Oct-2026) | Concall p.3, Inv. Pres. slide 6/12 |
| Mindray channel-partner territory scope and exclusivity status (currently non-exclusive, regional; OEM/private-label discussion unsigned) | Concall p.4 |

### 3D. Unit economics — the physics of the business

Because Avience runs at least three different unit economics inside one P&L, the closest useful "unit" is the placed instrument plus its attached reagent stream, since that is the engine the transition thesis rests on (companies/AVIENCE.md thesis line).

| Element | Reading |
|---|---|
| One unit | One placed diagnostic instrument (analyser) under a 5-year reagent-rental contract |
| Revenue per unit | NOT FOUND at the per-instrument level (no average contract value or reagent run-rate per placed unit disclosed anywhere in the corpus) |
| Cost per unit | NOT FOUND (no per-unit fully-loaded cost, including the free-instrument capex, disclosed) |
| Volume drivers | Number of instruments placed (function of hospital/lab wins, government tender wins, and the new YEIDA plant's capacity from Oct-2026, call p.6-7) |
| Price drivers | Reagent pricing set at placement, "agreed prices" over the 5-year term (call p.7); limited re-pricing power mid-contract |
| Cost drivers | Mindray purchase cost for traded reagents (63% of purchases run through one supplier, RHP p.36); raw-material cost for manufactured reagents; the up-front capital cost of the free-placed instrument, recovered only through the reagent tail |
| Incremental margin / operating leverage | Management states manufacturing margins scale with utilisation as the YEIDA plant ramps ("expect margins to improve as manufacturing scale and utilisation increase," call p.6); FY27 utilisation is guided at only 15-20% (call p.6), so near-term operating leverage on the new capacity is limited by design |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item to deteriorate |
|---|---|---|
| Revenue model | Mindray narrows or reallocates the regional channel-partner territory (non-exclusive arrangement, call p.4) | Traded reagents/instruments revenue line (72% of turnover, call p.7) |
| Revenue model | The ~Rs 47 Cr Uttarakhand order (no Reg 30 filing exists confirming it, B00) slips or is smaller than guided | FY27 half-yearly revenue vs the >=60% growth guidance (call p.3) |
| Margin | Manufacturing:trading mix shift to ~50:50 stalls, keeping the lower-value-add traded slice dominant | EBITDA margin (28.45% FY26, call) flattening or falling despite revenue growth |
| Margin | YEIDA plant ramps slower than the guided 15-20% FY27 utilisation | Depreciation/finance cost (already accruing on CWIP and SIDBI debt, B02/B03) rising ahead of matching revenue |
| Balance sheet | Cash conversion stays below 0.70x CFO/PAT for a third year | Operating cash flow line vs reported PAT (already 0.478x FY25, 0.675x FY26 consolidated, B03) |
| Balance sheet | Receivables ageing continues to deteriorate, especially on government/large-order collections (call p.5 cites 90-120 day cycles) | Trade receivables >6-month aged bucket (already 38.9% standalone, up from 10.2%, B02) |
| Execution | Placed-instrument base (72% of net PPE, B02) grows faster than the company's own physical-verification and reagent-collection discipline | CARO qualification language in the next audit report; provisioning coverage on aged receivables (already fallen 15.8% to 8.3%, B02) |
| Execution | Auditor transition (Haribhakti & Co. LLP retiring, M.A.M and Associates incoming, B03) coincides with the first full year of the YEIDA ramp | Any restated or revised results filing (one such revision already occurred in FY26, B00 LBF2) |
| Structural | The traded 72% of revenue is close to pure distribution economics; if the manufacturing mix shift does not materialise, the business is structurally closer to a lower-multiple trading/agency model than a regulated manufacturer | Gross margin on the traded segment specifically, if ever disclosed separately |

### 4B. Valuation method applicability (formal hand-off to Role 1)

| Method | Applicable? | Notes |
|---|---|---|
| DCF | Applicable, with caution | Requires resolving the sector-cap/archetype question below first; cash-flow forecast must reconcile the FCF-negative history (B01) against the guided FY27-28 ramp |
| Comparable company multiples (P/E, EV/EBITDA) | Applicable, secondary | QLINE, MOLBIO, TARSONS are the run's selected peers (step1 brief); QLINE is the closest structural mirror (same trading+manufacturing mix, same geography); MOLBIO is the destination-model comparator, not a like-for-like peer today |
| Sum-of-the-parts (SOTP) | Live question, flagged for operator | B00 already raises this: 72% of FY26 revenue is traded, so a SOTP splitting a "Distribution/trading" slice (Section 1B v3.7 Amendment 27.2's 20x row) from a "Pharma/CDMO" manufacturing slice (38x row) is a real candidate, though the traded slice carries a service layer (AMC/CMC, reagent rental) that Amendment 27.4's "pure buy-and-sell" boundary text says does not cleanly qualify as trading. Operator must confirm at /fttcp per B00 |
| Asset-based / replacement cost | Not applicable | Not a capital-intensive fixed-asset story in the sense that would make replacement cost meaningful; the placed-instrument base is a working asset, not a valuation floor |
| Dividend discount | Not applicable | No stated dividend policy found; recently listed, growth-stage |
| **PRIMARY**: {method: "DCF anchored to the Section 1B destination-PE cross-check", why: "The thesis is explicitly a multi-year mix-shift and margin-transition story (manufacturing 27%->50% of turnover); DCF is the only method that can carry that path explicitly, provided Section 1B governs the terminal/exit multiple per CLAUDE.md"} | | |
| **SECONDARY**: {method: "Peer multiple triangulation via QLINE (closest structural mirror) and MOLBIO (destination-model mirror)", why: "Anchors the multiple to real, recently-listed Indian IVD comparables rather than a generic sector average"} | | |
| **TERTIARY**: {method: "SOTP (trading slice vs manufacturing slice)", why: "Live per B00's Amendment 27.2/27.4 question; only becomes primary/secondary if the operator rules the traded 72% should be split out and separately capped at the Distribution/trading row rather than carried inside the Pharma/CDMO row"} | | |
| Cycle stage that matters for valuation | Early-transition, pre-proof: FY26 is the last full year on the old ~27:72 mix; FY27 is the first test year of both the YEIDA ramp and the guided mix shift. Valuation should treat FY27-28 as the proof window, not yet a steady state. | |

### 4C. Quarterly (half-yearly, SME filer) monitoring checklist

1. Manufacturing:trading revenue split — good: moving toward 50:50; trouble: stuck near 27:72 past H1 FY27.
2. Reagent-rental disclosure (any new granularity on rental margin or placed-unit count) — good: management discloses a per-unit or segment figure; trouble: continues as a percentage-only, undisclosed-base claim.
3. Uttarakhand order execution and any Reg 30 filing confirming it — good: a filing appears; trouble: continued silence past the "3-4 month" execution window (Inv. Pres. slide 24).
4. Consolidated CFO/PAT ratio — good: >=0.70x; trouble: below 0.70x a third year running.
5. Trade receivables >6-month aged share — good: reversal toward FY25's ~10-18% level; trouble: further rise past ~40%.
6. Provisioning coverage on aged receivables — good: recovers toward 15.8%; trouble: stays near or below 8.3%.
7. Finished-goods inventory growth vs revenue growth — good: inventory growth converges with revenue growth; trouble: continues outpacing it (was +80.9% vs +16-22% revenue, B02).
8. YEIDA CWIP-to-PPE capitalisation and commissioning date — good: capitalised and commercial by Oct-2026; trouble: slippage while SIDBI debt service continues.
9. Export FOB value — good: growth off the true FY25 ~Rs 524 lakh base; trouble: stays near the FY26 ~Rs 53 lakh trough.
10. Top-supplier (Mindray) concentration % of purchases — good: stable or diversifying; trouble: rises back toward FY24's 72.7%.
11. Top-10 customer concentration — good: any disclosed reduction; trouble: continues undisclosed and rising.
12. MSME trade payables growth vs total payables — good: moderates; trouble: continues outpacing (was +314% standalone, B02).
13. CARO qualifications in the next audit report, especially clause (ii)(b) (bank stock-statement discrepancy, undisclosed rupee amount per B03) — good: resolved and quantified; trouble: repeats or widens.
14. New auditor (M.A.M and Associates) first opinion — good: clean, matches prior year's substance; trouble: any new qualification in year one of the transition.

### 4D. Highest-value questions for management

1. "What is the average reagent revenue per placed instrument, and how many instruments are currently placed under active rental contracts?" Reassuring: a disclosed, growing per-unit figure. Worrying: management cannot or will not give even an approximate count.
2. "Is the ~Rs 47 Cr Uttarakhand order confirmed in writing, and why has no Reg 30 order-win filing been made since listing?" Reassuring: a signed purchase order or LOI exists and a filing follows shortly. Worrying: the order remains verbal/in-principle with no paper trail as FY27 progresses.
3. "What is the reagent-rental margin and manufacturing margin split, quarter by quarter, as the manufacturing mix rises?" Reassuring: rental and manufacturing margins hold or improve as mix shifts. Worrying: blended margin improvement is coming mostly from the traded side (e.g., a favourable large order), masking no real change in the underlying mix economics.
4. "What is the exact rupee amount of the CARO clause (ii)(b) bank stock-statement discrepancy, and has it recurred in H1 FY27?" (carried from B02/B03). Reassuring: a small, one-off, fully explained figure. Worrying: unquantified again, or recurring.
5. "How much of FY26's finished-goods inventory build (+80.9%) has actually sold through in H1 FY27?" Reassuring: most of it has moved. Worrying: it remains largely unsold, suggesting the FY26 growth included channel stuffing ahead of a plant transition.
6. "Is the Mindray arrangement moving toward the discussed exclusivity/OEM private-label deal, and on what timeline?" Reassuring: a term sheet or signed MOU exists. Worrying: the discussion remains informal a year on, leaving the 63-73%-of-purchases dependency fully exposed to Mindray's discretion.
7. "What is the expected FY27 collection period specifically on the Uttarakhand and other government-linked orders, and is working capital funding (the Rs 35-40 Cr requirement management itself flagged at Rs 100 Cr revenue, call p.5) already arranged?" Reassuring: facilities are sanctioned, not just "discussed with bankers." Worrying: funding remains only preliminary as the order scales.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
COMPANY: Avience Biomedicals Ltd (AVIENCE)                    RUN DATE: 2026-09-26
================================================================================
ONE-LINE MODEL: IVD manufacturer (88 CDSCO licences) + regional Mindray
distribution partner, monetising ~72% of turnover through traded goods and an
embedded reagent-rental (razor-and-blade) model on placed instruments.

BUSINESS TYPE:        Hybrid — manufacturing + distribution/agency +
                       equipment-placement recurring-consumable model
ARCHETYPE FIT (CLAUDE.md library): No single library archetype fits cleanly.
  - Closest partial fits: "Outsourcing partner" (client/principal concentration
    dynamics apply in reverse — Avience depends on Mindray as PRINCIPAL, not
    as a service client) and "Licence/scarcity business" (CDSCO licensing).
  - The reagent-rental placement engine (free instrument, locked-in
    consumables) is NOT explicitly named in the library; it behaves like a
    razor-and-blade variant nested inside the distribution stream.
  - FLAG for Role 2: name this explicitly as a library gap, do not force-fit.

REVENUE MIX (FY26, call p.7):
  Traded reagents/consumables .......... 59.83%
  Traded instruments .................... 12.55%
  Manufactured reagents/consumables ..... 14.62%
  Manufactured rapid cards ............... 9.15%
  Manufactured instruments ............... 3.21%
  Service (AMC/CMC, residual) ........... ~0.64% (derived, not a named %)

ASSET INTENSITY:      Medium, rising (YEIDA CWIP; 72% of net PPE held at
                       third-party sites as placed instruments, B02)
WC INTENSITY:         High (debtor days 146, inventory days 218, B00 LBF4)
PRICING POWER:        Weak on the traded 72%; moderate, contract-bound on the
                       closed-loop reagent-rental base; weak on rapid cards
CYCLICALITY:          Secular-growth industry (India IVD ~11%+ CAGR to FY30,
                       Inv. Pres. slide 18) riding on a company-specific
                       execution/capex cycle (YEIDA ramp)

MOATS PRESENT:
  - Regulatory/licence (88 CDSCO licences, 9-12mo approval cycle) — MODERATE
  - Switching cost (5-year reagent-rental lock-in) — MODERATE, contract-bound
  - Distribution relationship (Mindray regional partner) — WEAK, non-exclusive

SECTOR CAP QUESTION (B00, live): Pharma/CDMO (38x) is the nearest row for the
manufacturing engine; a Distribution/trading (20x) SOTP slice is arguable for
the 72% traded revenue. Operator must rule at /fttcp (Amendment 27.2/27.4).

TOP 5 MUST-TRACK METRICS:
  1. Manufacturing:trading mix (target ~50:50 from ~27:72)
  2. Consolidated CFO/PAT ratio (target >=0.70x, currently 0.675x FY26)
  3. Trade receivables >6-month aged share (was 38.9% standalone FY26)
  4. YEIDA CWIP-to-PPE capitalisation / commissioning (guided Oct-2026)
  5. Mindray purchase concentration (63.0% of purchases, 10M FY26)

VALUATION HAND-OFF:
  PRIMARY:   DCF anchored to Section 1B destination-PE cross-check
  SECONDARY: Peer multiples (QLINE closest mirror, MOLBIO destination mirror)
  TERTIARY:  SOTP (trading slice vs manufacturing slice) — live, operator-gated

ONE-LINE VERDICT: A small, growing IVD hybrid whose margin story depends on a
mix shift not yet proven, funded so far by working capital and capex, not cash.
================================================================================
```

---

## Input gaps carried into this stage

- Investor deck text layer covers only 6 of 29 pages; 23 pages read as PNG renders per the task brief (all cited slides in this report were verified visually).
- No per-instrument reagent revenue, no absolute count of instruments currently placed under active rental contracts, and no separately disclosed rental-segment margin exist anywhere in the corpus (RHP, AR, deck, or call) — all only given as ranges/percentages by management (call p.6-7).
- No Reg 30 filing confirms the ~Rs 47 Cr Uttarakhand order (B00 LBF1); it rests entirely on the concall and deck.
- No top-10-customer names disclosed (RHP p.34, confidentiality).
- AR's own MD&A/Business Performance narrative sections were not independently re-read this stage (B03 already characterises them as boilerplate); this stage relies on B02/B03 anchors for AR-sourced figures rather than re-citing AR page numbers directly.
