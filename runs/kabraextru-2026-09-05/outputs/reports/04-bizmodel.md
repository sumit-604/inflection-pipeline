# STAGE 4: BUSINESS MODEL DECODER — Kabra Extrusiontechnik Ltd (KABRAEXTRU)
Run date: 2026-09-05 | Model: claude-sonnet-5 | Mode: NO-CONCALL

Source key: **AR26** = Annual_Report_2026.txt (FY2025-26, page = PDF page marker in the
text twin). **AR25** = Annual_Report_2025.txt (FY2024-25, same convention). **Deck** =
Investor_Presentation_1.txt, quarter ended 31-Dec-2023, filed 25-Jan-2024 — every figure
from it is dated Dec-2023 or FY23/9MFY24 and flagged STALE. No results, rating detail, or
concall exists in the input set beyond what the AR itself discloses; those gaps are carried
to the YAML block.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
KET runs two unrelated factories under one listed company: a 4-decade-old plastics
machine-tool maker that sells big engineered machines to pipe and film producers, and a
6-year-old battery-pack assembler that buys lithium-ion cells and builds them into packs
for electric two- and three-wheelers, both reported through the "KET" ticker.

### 1B. Money flow chain, by revenue stream

**Extrusion Machinery Division**
[Steel, motors, screws, electronic drives, castings] → [KET designs and assembles a
pipe/film/sheet/compounding extrusion line to the customer's spec, using in-house
engineering plus tie-ups such as the 1983 Battenfeld-Cincinnati technical collaboration
(AR26 p.36)] → [delivers a capital machine, installed at the buyer's plant] → [pipe/film/
packaging manufacturers pay, mainly in India, some export] → [milestone payments against
purchase order plus advance, i.e. a capital-goods sale, not a subscription] (AR26 p.35-36).

**Battery Division (Geon, erstwhile Battrixx)**
[Lithium-ion cells bought globally — KET does not manufacture cells] → [Geon designs the
pack architecture, battery management system (BMS) and mechanical housing, and assembles
the pack at its ~7 GWh Chakan, Pune facility] → [delivers a finished battery pack or BMS
module] → [EV OEMs (two/three-wheeler, and now four-wheeler/off-road), plus a new FY26
direct-to-consumer inverter-battery line] pay → [OEM supply contracts / purchase orders;
D2C is retail cash sale, KET's "first D2C venture in its 60-year journey" launched FY26]
(AR26 p.4-5, p.36).

### 1C. Revenue model classification

| Stream | Type | Description | % of FY26 revenue (anchored) | Predictability |
|---|---|---|---|---|
| Extrusion Machinery Division | Capital-goods sale (engineer-to-order) | Pipe, blown-film, sheet, compounding lines and auto-feeding systems, sold as one-off equipment plus after-sale parts/service | 69.8% (Rs 314.89 Cr / Rs 450.998 Cr, AR26 consolidated Note 38 p.160-161; matches chairman's "70:30" mix, AR26 p.4) | Medium — order-linked, but exposed to government infra-spend timing (JJM disbursement) and export FX (AR26 p.36, p.38) |
| Battery Division (Geon) | Component/pack assembly, contract manufacture for OEMs + nascent D2C retail | Li-ion battery packs, BMS, IoT modules for EV OEMs; expanding into BESS/telecom/solar/C&I and D2C inverter batteries | 30.2% (Rs 136.11 Cr / Rs 450.998 Cr, AR26 consolidated Note 38 p.160-161) | Low — segment loss widened for a second year, one customer relationship (Hero Electric/HEVPL) already failed into NCLT, D2C is unproven (AR26 p.36; Note 9 p.87-88) |

Minor line inside the above: consolidated "Sale of Services" was Rs 5.65 Cr (564.76 lakh,
1.25% of revenue, AR26 Note 22 p.149) — not segment-disaggregated in the AR.

### 1D. Simplified business-model canvas

| Field | Extrusion Machinery | Battery Division (Geon) |
|---|---|---|
| What they sell | Engineered plastics-processing machines | Assembled lithium-ion battery packs / BMS |
| Who buys | Pipe, film and flexible-packaging manufacturers, India + 100+ export countries (Deck slide 11, STALE Dec-2023 for the country count) | EV OEMs (2W/3W/LCV/off-road), and from FY26 retail D2C buyers of inverter batteries (AR26 p.4-5) |
| Why them (claimed) | 4-decade legacy, "leadership position," ~40% market share claim — **but this number appears only in AR25 p.37 ("~40% market share... as on FY25") and is ABSENT from AR26**; AR26 uses only qualitative "leadership position" language (AR26 p.4, p.35) | Early mover, technology-agnostic design/assembly, 100+ engineer R&D team (AR26 p.34, p.36) |
| How delivered | Direct sale of capital equipment, engineer-to-order | Direct OEM supply contract; capacity at one plant (Chakan) |
| Cost structure dominance | Materials (steel, drives, castings) — consolidated cost of materials consumed net of inventory change was Rs 280.37 Cr against Rs 451.05 Cr revenue, 62.2% (AR26 Note 24/25 p.147-148); segment-level cost split is NOT FOUND (AR discloses segment revenue and result only, not segment cost lines) | Same consolidated cost line; segment-level split NOT FOUND. Key cost is the imported/sourced cell, which KET does not manufacture (AR26 p.36) |
| Scarce resource | Engineering know-how, 4-decade installed base | 100+ engineer R&D team, ARAI-type certification claimed only in the STALE deck (see 2C) |
| Pricing power source or absence | Claimed leadership but consolidated gross margin fell from 38.9% to 35.64% and EBITDA margin from 10.9% to 2.9% FY25→FY26 (AR26 p.37) — the evidence contradicts strong pricing power | None evidenced; segment result margin worsened from -20.1% to -31.9% of segment revenue even as segment revenue grew 7.2% (computed from Note 38 revenue/result, AR26 p.160-161) — a sign of negative operating leverage, not scale economics |
| Asset intensity | Standalone PP&E rose from Rs 192.13 Cr to Rs 234.92 Cr FY25→FY26 while capital work-in-progress fell from Rs 50.35 Cr to Rs 9.12 Cr — capex substantially completed and capitalised in FY26 (AR26 standalone balance sheet p.66) | Same balance sheet; the ~7 GWh Chakan facility cost "nearly USD 30 million (INR 250 Crores)" (AR26 p.36) — this is NOT an asset-light business despite management calling the model "asset-light" (AR26 p.36, Key Strength 5) |
| WC intensity | High — see Section 3 | High — see Section 3 |
| Regulatory moat or burden | None named in either AR | None named in AR26/AR25. Deck-era ARAI/AIS-156 certification claim (slide 22) does not appear in either annual report — treat as unconfirmed for FY26 |

### 1E. The chai-stall-uncle version
Picture a family that has run a well-known machine-repair shop for 40 years — everyone in
the neighbourhood knows them, and they build the big machines that make plastic pipes.
Six years ago they opened a second stall next door selling battery packs for electric
rickshaws. This year the old machine shop had a quiet year and made less money than last
year. The new battery stall sold a bit more stuff than last year, but it lost even more
money than the year before — every extra rickshaw battery it sold, it lost more on. One of
its biggest customers (Hero Electric) stopped paying and went to bankruptcy court, so the
family had to write off a chunk of cash it will probably never see. Meanwhile the bank that
lends them working capital moved them down two rating notches in one year. The family says
next year will be better because a big new order is coming — but they have not named who
placed it (AR26 p.4, p.34-38, p.51; Note 9 p.87-88).

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Hybrid: engineer-to-order capital-goods manufacturer (Extrusion) + component/pack assembly manufacturer (Battery) | Mixed — one-off machine sales + OEM pack supply + nascent D2C | Medium-to-heavy (PP&E growing, Rs 250 Cr sunk into Geon capacity) | High (see Section 3) | Weak and eroding — claimed leadership not visible in margin trend |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Extrusion Machinery | Battery Division | Net effect |
|---|---|---|---|
| Competition (rivalry) | No named competitor in AR26 or AR25; company describes itself only as holding a "leadership position" (AR26 p.4, p.35) — no anchored comparative data | Deck-era description: "E2W/E3W industry is highly fragmented and is expected to remain fragmented" (Deck slide 22, STALE, sourced to a third-party 2022 report, not in either AR) | NEUTRAL-to-HURTS — cannot be scored with confidence from documents provided; margin trend (below) argues HURTS |
| Entry barriers | Moderate: capex, engineering depth, 4-decade relationships, technical tie-ups (Battenfeld-Cincinnati since 1983, JV with Extron Mecanor Finland and, until Feb-25, Penta SRL Italy) (AR26 p.36; Note 39 p.104) | Low-to-moderate: KET explicitly does not manufacture cells and calls its model "technology-agnostic" and "asset-light" (AR26 p.36) — the same feature that lowers KET's own capex also lowers the barrier for a new entrant to copy the assembly model | HELPS Extrusion, HURTS Battery |
| Supplier power | Not flagged as a specific risk in AR26 MD&A | High: lithium-ion cells are "sourced globally" (AR26 p.36) and MD&A explicitly flags "supply chain risks, particularly in the battery segment, where key components are sourced globally... price volatility, or dependency on external suppliers could impact operations and margins" (AR26 p.38) | HURTS Battery |
| Customer power / concentration | One customer accounted for 19.11% of FY26 revenue from operations (previous year: two customers, 26.94%) — AR does not say which segment this customer sits in (AR26 consolidated Note 38 p.160-161) | HEVPL (Hero Electric) receivable of Rs 30.39 Cr (3,039 lakh) went into NCLT insolvency proceedings (order dated 20-Dec-2024); KET had to provide for it and reverse related warranty provisions (AR26 standalone Note 9 p.87-88) | HURTS — concentrated and, in one proven case, credit-risky customer base |
| Substitutes | Limited direct substitute for extrusion-line capital equipment (different process technology) | MD&A flags "rapid technological advancements in battery technologies... necessitate continuous investment... to remain competitive and avoid obsolescence" and "increasing competition across both the extrusion and energy segments" (AR26 p.38) | NEUTRAL Extrusion, HURTS Battery |

### 2B. Competitive positioning map
Named competitors: **NOT FOUND** in AR26, AR25 or the investor deck — the company does not
name a single rival in any of the three documents provided. AR25 (p.37) claimed "~40%
market share in its product category as on FY25" for Extrusion and the Deck (slide 11,
Dec-2023, STALE) claimed "40% market share (FY23)" for Extrusion and "18% market share...
in its segment (FY23)" for Battrixx/Geon — both are company self-estimates ("As per the
Company's estimates," Deck slide 11 footnote), neither is repeated in AR26, and neither can
be cross-checked against a named competitor list. Treat as unconfirmed and stale.

### 2C. Moat assessment (eight standard types)

| Moat type | Evidence in AR26/AR25/Deck | Durability |
|---|---|---|
| Network effects | Deck (STALE, Dec-2023) claimed a data-flywheel: "90%+ of customer now use Battrixx designed products as compared to less than 40% a year ago" from fleet data feedback (Deck slide 19) — **this claim does not appear in AR26 or AR25**; unconfirmed for the current business | NONE confirmed |
| Switching costs | Not evidenced for Battery (HEVPL relationship failed; >10% customer count fell from two to one). Possibly moderate for Extrusion given "long-standing customer relationships" language (AR26 p.35), but no churn/retention data given | WEAK, unquantified |
| Cost advantage | Not evidenced; consolidated gross margin fell 326 bps (38.9%→35.64%) and EBITDA margin fell from 10.9% to 2.9% FY25→FY26 (AR26 p.37) | NONE |
| Intangible assets (brand/patents/licences) | Kolsite/KET brand has real vintage (43rd AGM, over four decades, AR26 p.4) but no patents disclosed in AR26. Deck-era ARAI/AIS-156 certification and IATF-approved facility claims (Deck slides 16, 22) are ABSENT from both annual reports | WEAK / unconfirmed |
| Efficient scale | AR25 (p.37) and Deck (slide 11) claimed ~40% domestic share, which if true could support an efficient-scale argument, but the number is absent from AR26 and unverifiable against named rivals | UNCONFIRMED |
| Brand | Same 4-decade brand point as above; not evidenced by pricing power (margins fell) | WEAK |
| Distribution / access | "100+ countries," "15,000+ installations" cited (AR26 p.36, standalone auditor's report p.64/67 reference to "more than 15,000 installations"), but export revenue is only Rs 57.52 Cr of Rs 450.998 Cr, 12.8% of FY26 revenue (Note 38 geography split, AR26 p.160-161) — reach has not converted into material export revenue share | WEAK |
| Regulatory / licence | None named in either AR | NONE |

**Bottom line: no moat is evidenced with FY26 primary-source data.** Every claimed edge
(market share, ARAI certification, design-win share, data network effect) either does not
appear in AR26/AR25 at all, or appears only as a company self-estimate in the 2.5-year-stale
Dec-2023 deck.

### 2D. Industry lifecycle stage
- **Extrusion Machinery:** Mature, low-single-digit-to-mid-single-digit global growth.
  Global plastic extrusion machinery market projected at 6.7% CAGR 2026-32 (AR26 p.4, p.30);
  India plastic pipes market projected at 6.3% CAGR 2025-34 (AR26 p.31). KET's own segment
  revenue in this mature market FELL 13.2% in FY26 (Rs 314.89 Cr vs Rs 362.85 Cr, Note 38
  p.160-161), attributed to "slower execution and fund disbursement under... Jal Jeevan
  Mission (JJM)... delays in infrastructure spending by state governments, and weakness in
  export markets" (AR26 p.36).
- **Battery Division:** Early growth/emerging stage industry-wide — India EV retail sales
  grew 24.6% YoY in FY26 to 2.45 million units (AR26 p.32-33, table sourced to FADA). KET's
  own Battery segment revenue grew only 7.2% in the same year (Rs 136.11 Cr vs Rs 126.98 Cr,
  Note 38 p.160-161) — **the company's growth engine is growing at under a third of its own
  cited industry growth rate**, a gap not addressed anywhere in the MD&A.

### 2E. Key industry drivers

| Driver | Direction | Impact on KET | Anchor |
|---|---|---|---|
| Government infra spend (Jal Jeevan Mission, Smart Cities) | Positive long-term, but FY26 execution slower than expected | Extrusion revenue miss FY26 | AR26 p.36, p.34 |
| India EV retail adoption | Strongly positive (+24.6% YoY units) | Should help Geon, but Geon underperformed the trend | AR26 p.32-33 |
| Global/India battery cell pricing and localisation (PLI-ACC) | Mixed — falling cell costs help affordability, but KET does not make cells so is a price-taker on its largest input | Margin risk for Battery | AR26 p.32-33, p.38 |
| Export market conditions (currency, geopolitics) | Negative in FY26 | Extrusion export weakness cited explicitly | AR26 p.36 |
| Credit rating trajectory | Negative — CRISIL downgraded KET twice within FY26 | Higher cost/availability of working-capital debt | AR26 p.51 |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these, track-these

| Commonly tracked ratio | Verdict | Why |
|---|---|---|
| Consolidated blended EBITDA margin as a single number | MISLEADING | It nets a profitable, shrinking Extrusion segment (result margin 16.1% of segment revenue, down from 19.3%) against a loss-making, worsening Battery segment (result margin -31.9%, down from -20.1%) (computed from Note 38, AR26 p.160-161). The blended 2.9% FY26 EBITDA margin (AR26 p.37) hides that direction is diverging, not converging |
| Trade receivables turnover ratio in isolation | MISLEADING | Standalone disclosed ratio actually IMPROVED (5.22x vs 4.97x, +5.2%, AR26 Note 43 p.112) even though the receivables ageing schedule shows large amounts overdue 2-3 years and beyond 3 years (AR26 standalone Note 9 p.87-88). The ratio improved partly because the receivable base shrank (HEVPL written off), not because collections genuinely sped up — a classic ratio-vs-ageing mismatch |
| Net capital turnover ratio (Sales / Working Capital) | MISLEADING | Rose to 2.67x from 2.37x (+12.9%, AR26 Note 43 p.112) — this looks like efficiency but a shrinking net working-capital base while sales also fell can produce the same number; read alongside current ratio (down to 1.55 from 1.67) and the cash position (below), which point the other way |
| P/E on trailing EPS | IRRELEVANT this year | FY26 standalone EPS is negative, Rs (0.70) (AR26 p.37); consolidated basic EPS is Rs (1.53) (AR26 consolidated P&L p.122). No trailing P/E is computable |
| Dividend yield / payout | IRRELEVANT | Proposed dividend FY26 is Nil (AR26 p.4/Notice section p.4 dividend table); FY26 cash outflow of Rs 8.74 Cr (874.32 lakh) was payment of the FY25 final dividend, not a new declaration (AR26 standalone Note, p.87 dividend disclosure) |
| Consolidated debt-service coverage ratio taken at face value | MISLEADING | Disclosed DSCR actually rose (14.36x vs 10.32x, +39.2%, AR26 Note 43 p.112) with the AR's own stated reason "due to generate lower net operating income" — a confusing, arguably mis-stated rationale in the filing itself; do not read this ratio as a sign of improving debt safety without checking the underlying cash flow (CFO nearly halved, see 3B) |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| Battery segment revenue growth vs India EV industry unit growth | Whether Geon is gaining or losing share in its own stated growth market | Segment growth should track or beat the ~20-25% industry unit growth cited in the same AR | AR26 Note 38 (segment revenue) vs MD&A EV sales table, p.160-161 & p.32-33 | Segment growth persistently under half of industry growth (FY26: 7.2% vs 24.6%) |
| Extrusion segment revenue vs JJM/infra disbursement commentary | Whether the "temporary" government-spend explanation for the FY26 decline (-13.2%) actually reverses | Return to positive growth within 1-2 years if the MD&A explanation is correct | AR26 Note 38 p.160-161; MD&A p.36, p.38 | A second consecutive year of decline after JJM/infra spend "recovers" per government data |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| Battery segment result / segment revenue | Whether the loss-making growth engine is actually converging to breakeven, as MD&A claims | Loss margin narrowing year on year | AR26 Note 38 p.160-161 | Loss margin widening (it went from -20.1% to -31.9% FY25→FY26) |
| Extrusion segment result / segment revenue | Health of the cash-generating legacy business funding the transition | Stable-to-improving mid-to-high-teens margin | AR26 Note 38 p.160-161 | Margin below ~10% of segment revenue, or two consecutive years of decline (it fell from 19.3% to 16.1% FY26) |
| ROCE (company-wide, as disclosed) | Capital efficiency across both segments combined | High single digits or better for a capital-goods/component manufacturer | AR26 standalone Note 43 (Ratios to be disclosed) p.112 | Sub-3% (FY26 disclosed at 1.20%, down from 8.90%) |
| Inventory turnover (disclosed) | Whether inventory is being worked down as sales slow | Turnover holding steady or rising as sales normalise | AR26 Note 43 p.112 | Turnover falling while inventory rupee-value stays flat (1.79x→1.55x FY26, -13.1%, while inventory value was essentially flat at Rs 285-286 Cr both years) |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| Cash and cash equivalents | Liquidity buffer independent of borrowing lines | Multiple months of fixed costs in hand | AR26 standalone balance sheet p.66 (Note 10) | Cash below Rs 5 Cr against Rs 451 Cr revenue (FY26: Rs 1.97 Cr standalone, Rs 2.04 Cr consolidated) |
| Current investments (mutual funds) drawdown | Whether the company is liquidating its liquid investment buffer to fund operations | Stable or growing balance | AR26 standalone/consolidated Note 8 p.87/p.141 | Balance nearly halving year on year (Rs 53.49 Cr → Rs 22.59 Cr FY26) |
| Total borrowings | Reliance on debt to fund working capital as the battery segment burns cash | Debt-equity holding steady | AR26 standalone Note 17 / balance sheet p.66, p.87-88 | Borrowings rising while equity and cash both fall (Rs 125.79 Cr → Rs 141.09 Cr total borrowings, +12.2%, D/E 0.27x→0.32x, +16.7% per Note 43 p.112) |
| CRISIL long-term/short-term rating | Independent third-party read on credit quality | Stable or improving rating, no negative outlook | AR26 Corporate Governance Report p.51 | Any further downgrade after two already occurred within FY26 (CRISIL A+/Negative → A/Negative → A-/Stable; short-term CRISIL A1 → A2+, "basis performance reported for Quarter 3," AR26 p.51) |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find it | Note |
|---|---|---|
| Battery pack installed capacity (GWh) and utilisation | AR MD&A (approx. 7 GWh installed at Chakan, AR26 p.34, p.36) | FY26 utilisation figure not disclosed in the AR; only cumulative "400,000+ packs deployed" since 2020 is given, not an FY26 unit count |
| Order book / order inflow (both segments) | AR MD&A "Strong Order Visibility" callout (AR26 p.37) | Only one number is disclosed: a "~INR 150 Crore order for execution in the upcoming year" (FY27) for the energy business — no customer named, no total order book value given for either segment |
| Number of >10% customers and their combined revenue share | AR consolidated/standalone Note 38 (Segment revenue with major customers) p.160-161, p.105-106 | Fell from two customers (26.94% of revenue) to one customer (19.11%) FY25→FY26 — direction of concentration is improving on this specific metric even as receivable quality (ageing) worsens |
| Employee headcount | AR26 MD&A Human Capital, p.38 | 665 total (workers, staff, executives) as at 31-Mar-2026 |
| R&D headcount (Battery only) | AR26 p.34, p.36 | "100+ engineers" cited; no rupee R&D spend disclosed in AR26 (NOT FOUND) |
| ARAI/AIS-156 certification, IATF facility approval, design-win share | Deck slides 16, 19, 22 (Dec-2023, STALE) | **Absent from AR26 and AR25** — cannot be confirmed as current-state facts; do not carry forward as evidenced moats |

### 3D. Unit economics — the physics of the business

| | Extrusion Machinery | Battery Division (Geon) |
|---|---|---|
| Define one unit | One engineered extrusion line/machine (pipe, blown-film, sheet, compounding, or auto-feed system) | One lithium-ion battery pack (or BMS module) |
| Revenue per unit | NOT FOUND — AR discloses only aggregate segment revenue (Rs 314.89 Cr, Note 38), no unit count or average selling price by machine type | NOT FOUND — AR discloses cumulative "400,000+ packs deployed" since 2020 but no FY26 unit count or per-pack ASP |
| Cost per unit | NOT FOUND at segment level — only consolidated cost of materials (62.2% of total revenue, Note 24/25 p.147-148) is disclosed; no segment cost split | NOT FOUND at segment level; the qualitative driver is clear — cells are the dominant, externally-sourced cost (AR26 p.36) |
| Volume drivers | Government infra capex cycle (JJM), pipe/film capacity additions by customers, export demand | EV OEM production volumes, D2C sell-through (new in FY26), diversification into BESS/telecom/solar |
| Price drivers | Machine specification/automation level, steel and component input costs (pass-through unclear — not disclosed) | Cell chemistry/cost, competitive pricing pressure from a fragmented OEM-supplier market (Deck slide 22, STALE context only) |
| Cost drivers | Materials (largest line), employee cost (consolidated Rs 78.65 Cr, 17.4% of revenue, Note 26 p.148), depreciation now rising as capex is capitalised | Imported/sourced cells, and a fixed-cost base (the ~7 GWh Chakan plant, ~Rs 250 Cr invested) that is loss-absorbing at current volumes |
| Incremental margin / operating leverage | Segment margin FELL as revenue fell (19.3%→16.1% of segment revenue) — some fixed-cost drag as volume declined | Segment margin FELL as revenue ROSE (-20.1%→-31.9% of segment revenue) — this is the opposite of normal operating leverage: more volume produced a wider loss ratio, which directly contradicts the MD&A's own statement that the business "is expected to move towards profitability as volumes scale up" (AR26 p.38) |

**Implied capacity utilisation cross-check (own calculation, not an AR-stated figure):**
FY26 Battery segment revenue of Rs 136.11 Cr against management's own stated "optimal
levels" ceiling of "INR 1,500+ crore revenue" for the existing facility (AR26 p.37) implies
utilisation of roughly 9% of the claimed ceiling. This is arithmetic derived from two
AR-disclosed data points, not a figure the company discloses directly, and it is offered
only to size the gap between the current run-rate and the stated long-run claim.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Battery segment revenue growth (7.2% FY26) continues to trail the cited India EV industry growth (24.6% FY26) — share loss inside a segment management calls the growth engine | Battery Division segment revenue, Note 38, next AR/quarterly filing |
| Margin | Battery segment loss ratio widened even as revenue grew — negative, not positive, operating leverage | Battery Division segment result as % of segment revenue (Note 38); watch specifically whether the loss ratio narrows or widens next |
| Balance sheet | Cash near-zero (Rs ~2 Cr) with the mutual-fund liquidity buffer nearly halved in one year and borrowings up 12.2%, against a second credit-rating downgrade in the same year | Cash and cash equivalents (Note 10); current investments (Note 8); total borrowings (Note 17); CRISIL rating action |
| Execution | A ~Rs 150 Cr FY27 order for the energy business is cited with no customer named and no contract terms disclosed; a Rs 1,500+ Cr "optimal" revenue ceiling for the existing facility implies roughly 9x the current Battery run-rate | Battery Division segment revenue realised in FY27 vs the Rs 150 Cr claim; capacity utilisation disclosure if the company ever provides one |
| Structural | Technology-agnostic, no-cell-manufacturing model means KET does not control its largest battery input cost and faces supplier price/FX risk on globally sourced cells | Cost of materials consumed as % of Battery segment revenue, if ever disaggregated; consolidated gross margin (currently blended and already falling, 38.9%→35.64%) |

### 4B. Valuation method applicability

| Method | Applicable? | Notes |
|---|---|---|
| Sum-of-the-parts (SOTP) | **PRIMARY** | Two segments with fundamentally different economics (a mature, historically profitable capital-goods business vs an early-stage, loss-widening component assembler) sit inside one consolidated P&L that a blended multiple would badly distort. Note 38 gives clean segment revenue, result, assets and liabilities for both, making a segment-level build achievable |
| EV/EBITDA on a normalised/mid-cycle basis, Extrusion segment only | **SECONDARY** | Extrusion is a cyclical capital-goods business (JJM/infra-linked) that just printed a margin trough (segment result 16.1% of segment revenue, down from 19.3%); a mid-cycle EV/EBITDA cross-check on this segment alone avoids letting the Battery loss distort the read on the legacy business |
| EV/Sales, Battery segment only | **TERTIARY** | Battery/Geon is loss-making at the EBITDA line (segment result -31.9% of segment revenue), so P/E and EV/EBITDA are not usable for this segment; an EV/Sales or replacement-cost-of-capacity lens (the disclosed ~Rs 250 Cr sunk into the ~7 GWh Chakan facility) is the only workable cross-check until profitability is demonstrated |
| P/E (consolidated) | NOT APPLICABLE | Consolidated and standalone FY26 EPS are both negative (Rs (1.53) consolidated, Rs (0.70) standalone, AR26 p.122, p.37) |
| Dividend discount model | NOT APPLICABLE | Proposed dividend FY26 is Nil; the cash paid out in FY26 was settlement of the FY25 final dividend, not a new declaration |
| PEG | NOT APPLICABLE | No positive, comparable growth-adjusted earnings base exists this year |
| Cycle stage that matters for valuation | Extrusion segment: near a cyclical margin trough tied to government infra-spend timing. Battery segment: pre-profitability, capacity-build phase — valuation must not extrapolate FY26's negative operating leverage forward without evidence the loss ratio has turned |

### 4C. Quarterly monitoring checklist (10-15 items)

1. Battery Division segment revenue vs prior quarter and vs the India EV industry growth rate — good: closing the growth gap; trouble: gap persisting or widening.
2. Battery Division segment result (loss narrowing or widening) — good: loss ratio narrowing quarter on quarter; trouble: further widening.
3. Extrusion Division segment revenue — good: sequential recovery as JJM/infra disbursement normalises; trouble: a second consecutive declining year.
4. Cash and cash equivalents — good: rebuilding above a token balance; trouble: staying near-zero.
5. Current investments (mutual fund) balance — good: stabilising; trouble: continued drawdown to fund operations.
6. Total borrowings and debt-equity ratio — good: flat or declining; trouble: continued rise alongside falling equity.
7. Trade receivables ageing (specifically the >1 year and >3 year buckets) — good: shrinking; trouble: growing.
8. CRISIL (or any rating agency) rating action — good: stable outlook, no further downgrade; trouble: any additional downgrade.
9. Customer concentration (>10% customers and their combined %) — good: diversifying without losing revenue; trouble: concentration rising again or the remaining large customer showing credit stress.
10. Progress and disclosure detail on the ~Rs 150 Cr FY27 order (customer name, delivery schedule, revenue recognised) — good: named counterparty and phased delivery evidence; trouble: continued vagueness or slippage.
11. Any disclosed capacity utilisation figure for the Chakan facility — good: rising utilisation with a credible path toward the Rs 1,500+ Cr ceiling; trouble: utilisation still undisclosed or evidently stuck near current run-rate.
12. Inventory value vs sales trend — good: inventory declining in line with or faster than sales; trouble: inventory flat/rising while sales fall.
13. Trade payables turnover — good: stable; trouble: continued stretching of supplier payment terms as a substitute for cash.
14. Consolidated vs standalone gross margin trend — good: recovering toward the FY25 38.9% level; trouble: further compression below 35.64%.

### 4D. Highest-value questions for management

1. **The Battery segment loss widened from Rs 25.53 Cr to Rs 43.35 Cr even as segment revenue grew 7.2% — what specific, quantified factors (volume, pricing, provisions, one-offs) explain this, given the MD&A states the business is "expected to move towards profitability as volumes scale up"?** Reassuring answer: a clear per-unit cost bridge showing the widening was driven by identifiable one-off items (e.g., D2C launch costs, warranty reversal timing) that will not repeat. Worrying answer: continued generic "scale-up" language with no numbers.
2. **Who is the counterparty and what is the delivery schedule for the ~Rs 150 Cr FY27 order cited in the MD&A?** Reassuring: a named OEM/BESS counterparty with a binding purchase order and phased delivery milestones. Worrying: an unnamed or non-binding letter of intent.
3. **CRISIL downgraded KET's long-term rating twice within FY26 (A+/Negative → A/Negative → A-/Stable) and the short-term rating once (A1 → A2+), both stated as "basis performance reported for Quarter 3" — what specific covenant or performance metric triggered this, and is the rating now stable into FY27?** Reassuring: a specific, resolved trigger and confirmation of no further watch/negative outlook. Worrying: a vague answer or an unresolved covenant risk.
4. **What is the current utilisation of the ~7 GWh Geon capacity, and what incremental capex (if any) is needed to reach the claimed Rs 1,500+ Cr revenue ceiling?** Reassuring: a disclosed utilisation number with a credible multi-year ramp plan and limited further capex need. Worrying: utilisation remaining undisclosed, or a large incremental capex ask with no funding plan.
5. **Following the Rs 30.39 Cr HEVPL/Hero Electric receivable write-off under NCLT, what credit-vetting process now applies to new EV-OEM and D2C customers?** Reassuring: credit insurance, advance-heavy payment terms, or a diversified, credit-checked customer base. Worrying: a repeat pattern of concentrated exposure to a single financially weak EV OEM.
6. **Customer advances fell from Rs 73.22 Cr to Rs 59.39 Cr (18.9%) — is this a demand slowdown or a collections/phasing issue, and how does it square with inventory staying flat while receivables aged into multi-year overdue buckets?** Reassuring: a specific, verifiable phasing explanation. Worrying: confirmation that working-capital quality is structurally deteriorating.
7. **Extrusion segment result fell from Rs 70.14 Cr to Rs 50.75 Cr (-27.7%) on a 13.2% revenue decline — is the margin compression from temporary JJM funding delays, or from competitive pricing pressure that would persist even after infra-spend normalises?** Reassuring: evidence the compression is temporary and tied to a specific, recoverable government funding cycle. Worrying: acknowledgement of structural pricing pressure with no recovery visibility.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
┌─────────────────────────────────────────────────────────────────────────┐
│ KABRA EXTRUSIONTECHNIK LTD (KABRAEXTRU)  |  FY26  |  Run: 2026-09-05     │
├─────────────────────────────────────────────────────────────────────────┤
│ BUSINESS TYPE: Hybrid — engineer-to-order capital-goods manufacturer    │
│ (Extrusion Machinery) + component/pack assembly manufacturer            │
│ (Battery Division / Geon)                                               │
├─────────────────────────────────────────────────────────────────────────┤
│ REVENUE MIX (FY26, Note 38, AR26 p.160-161):                            │
│   Extrusion Machinery ......... 69.8%  (Rs 314.89 Cr, -13.2% YoY)       │
│   Battery Division (Geon) ..... 30.2%  (Rs 136.11 Cr, +7.2% YoY)        │
├─────────────────────────────────────────────────────────────────────────┤
│ SEGMENT RESULT (Note 38):                                                │
│   Extrusion: Rs 50.75 Cr (16.1% of segment revenue), down from Rs 70.14 │
│              Cr (19.3%) FY25                                             │
│   Battery:   Rs (43.35) Cr (-31.9% of segment revenue), down from       │
│              Rs (25.53) Cr (-20.1%) FY25 — loss WIDENED as % of revenue │
├─────────────────────────────────────────────────────────────────────────┤
│ CONSOLIDATED: Revenue Rs 451.05 Cr (-5.45%) | EBITDA margin 2.9%        │
│ (was 10.9%) | PAT Rs (5.37) Cr consol / Rs (2.44) Cr standalone         │
│ (AR26 p.37, p.122)                                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ ASSET INTENSITY: Medium-to-heavy — PP&E rose Rs 192 Cr→Rs 235 Cr FY26;  │
│ ~Rs 250 Cr sunk into Geon's ~7 GWh Chakan capacity (AR26 p.36, p.66)    │
├─────────────────────────────────────────────────────────────────────────┤
│ WC INTENSITY: High and worsening — cash ~Rs 2 Cr, mutual-fund buffer   │
│ nearly halved (Rs 53 Cr→Rs 23 Cr), borrowings +12.2%, D/E 0.27x→0.32x, │
│ current ratio 1.67x→1.55x, receivables aged into 2-3yr/>3yr buckets    │
│ (AR26 Notes 8, 9, 10, 17, 43, p.66-88, p.112)                           │
├─────────────────────────────────────────────────────────────────────────┤
│ PRICING POWER: Weak and eroding — claimed "leadership"/"~40% share"    │
│ (AR25 only, absent from AR26) contradicted by margin compression       │
│ (gross margin 38.9%→35.64%, EBITDA margin 10.9%→2.9%)                   │
├─────────────────────────────────────────────────────────────────────────┤
│ MOATS: NONE confirmed with FY26 primary-source evidence. Every claimed │
│ edge (market share, ARAI/AIS-156, IATF, "90% design-win," data network │
│ effect) sits ONLY in the 2.5-yr-stale Dec-2023 investor deck and does  │
│ NOT appear in AR26 or AR25                                              │
├─────────────────────────────────────────────────────────────────────────┤
│ CREDIT: CRISIL downgraded twice within FY26 (LT: A+/Neg→A/Neg→A-/Stable;│
│ ST: A1→A2+), rationale stated only as "basis performance reported for  │
│ Quarter 3" (AR26 p.51)                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│ KEY CUSTOMER EVENT: Hero Electric (HEVPL) receivable Rs 30.39 Cr,      │
│ under NCLT insolvency since Dec-2024, provided for and written off     │
│ (AR26 Note 9, p.87-88)                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│ PRIMARY VALUATION METHOD: Sum-of-the-parts (segment-level, per Note 38)│
│ SECONDARY: Mid-cycle EV/EBITDA, Extrusion segment only                 │
│ TERTIARY: EV/Sales or capacity replacement cost, Battery segment only  │
│ NOT APPLICABLE: P/E, DDM, PEG (all require positive current earnings   │
│ or a dividend that does not exist this year)                            │
├─────────────────────────────────────────────────────────────────────────┤
│ ONE-LINE VERDICT: A profitable, shrinking legacy machine business is   │
│ subsidising a loss-widening battery bet that is growing slower than    │
│ its own cited market and has already lost one major customer to NCLT. │
└─────────────────────────────────────────────────────────────────────────┘
```

---

```yaml
stage: B04-bizmodel
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps: ["investor-presentation-stale-2.5yr-Dec2023", "results", "rating-detail-beyond-AR-disclosure", "announcements", "shareholding", "research", "prospectus-not-expected", "peer-concall-windsor", "peer-concall-mislabel-stale", "screener-csv-defect", "sector_cap_row-flagged-phase3"]
flags:
  - "Battery segment loss ratio WIDENED (-20.1% to -31.9% of segment revenue) even as segment revenue GREW 7.2%, directly contradicting MD&A claim that the business 'is expected to move towards profitability as volumes scale up' (AR26 Note 38 p.160-161 vs AR26 p.38)"
  - "AR25's '~40% market share' claim (AR25 p.37) and all Deck-era moat claims (ARAI/AIS-156 certification, IATF-approved facility, '90%+ design-win' share, data network effect) are ABSENT from AR26 and cannot be treated as current evidence"
  - "CRISIL downgraded both long-term and short-term ratings within FY26 with rationale disclosed only as 'basis performance reported for Quarter 3' (AR26 p.51) — no further detail available in the provided documents"
  - "Cash near-zero (~Rs 2 Cr) with mutual-fund liquidity buffer nearly halved and borrowings up 12.2% in the same year (AR26 Notes 8, 10, 17)"
  - "HEVPL (Hero Electric) receivable Rs 30.39 Cr under NCLT insolvency, a realised customer-concentration/credit-quality failure, not a hypothetical risk (AR26 Note 9 p.87-88)"
  - "Battery segment revenue growth (7.2%) ran at under a third of the cited India EV industry unit growth (24.6%) in the same fiscal year (AR26 Note 38 vs AR26 p.32-33) — an implied share-loss signal not addressed in the MD&A"
business_type: "hybrid"
revenue_streams:
  - {name: "Extrusion Machinery Division", type: "capital-goods sale (engineer-to-order)", pct_of_revenue: 69.8, predictability: "M"}
  - {name: "Battery Division (Geon, erstwhile Battrixx)", type: "component/pack assembly manufacturing for OEMs + nascent D2C retail", pct_of_revenue: 30.2, predictability: "L"}
asset_intensity: "medium"
wc_intensity: "high"
pricing_power: "weak"
cyclicality: "cyclical"
moats_present: []
valuation_methods:
  primary: {method: "Sum-of-the-parts (segment-level, per Note 38)", why: "Two segments with fundamentally different economics (mature, historically profitable capital goods vs early-stage, loss-widening battery assembly) sit in one consolidated P&L that a blended multiple would badly distort; Note 38 gives clean segment revenue/result/assets/liabilities to build it"}
  secondary: {method: "Mid-cycle EV/EBITDA, Extrusion segment only", why: "Extrusion is a cyclical, government-infra-linked capital-goods business at a margin trough (16.1% of segment revenue, down from 19.3%); a normalised cross-check isolates it from the Battery loss"}
  tertiary: {method: "EV/Sales or capacity-replacement-cost, Battery segment only", why: "Battery segment is loss-making at EBITDA (-31.9% of segment revenue), so earnings multiples do not work; EV/Sales or the disclosed ~Rs 250 Cr sunk capacity cost is the only workable cross-check pre-profitability"}
  not_applicable: ["P/E (consolidated and standalone EPS both negative FY26)", "Dividend discount model (proposed dividend Nil FY26)", "PEG (no positive comparable growth-adjusted earnings base)"]
irrelevant_ratios:
  - {ratio: "Blended consolidated EBITDA margin", why: "Nets a shrinking-but-profitable Extrusion segment against a growing-but-more-loss-making Battery segment, hiding that the two are diverging, not converging"}
  - {ratio: "Trade receivables turnover ratio", why: "Improved (4.97x to 5.22x) mainly because the receivable base shrank after the HEVPL write-off, while the ageing schedule shows growing multi-year overdue amounts"}
  - {ratio: "Net capital turnover ratio", why: "Rose (2.37x to 2.67x) in a way that can reflect a shrinking working-capital base as much as genuine efficiency; contradicted by a falling current ratio and near-zero cash"}
  - {ratio: "Trailing P/E", why: "Not computable; FY26 standalone and consolidated EPS are both negative"}
  - {ratio: "Disclosed debt-service coverage ratio at face value", why: "Rose (10.32x to 14.36x) with the filing's own stated reason ('due to generate lower net operating income') internally inconsistent with an improving-safety reading; check underlying CFO, which nearly halved"}
must_track_metrics:
  - {metric: "Battery Division segment result as % of segment revenue (Note 38)", healthy: "loss ratio narrowing toward breakeven", red_flag: "loss ratio widening further (went from -20.1% to -31.9% FY25 to FY26)"}
  - {metric: "Cash and cash equivalents + current investments buffer", healthy: "stable or rebuilding", red_flag: "continued drawdown (cash ~Rs 2 Cr, mutual funds halved Rs 53 Cr to Rs 23 Cr FY26)"}
  - {metric: "Total borrowings and debt-equity ratio", healthy: "flat or declining", red_flag: "continued rise alongside falling equity (0.27x to 0.32x FY26)"}
  - {metric: "Trade receivables ageing, >1yr and >3yr buckets", healthy: "shrinking overdue balances", red_flag: "growing overdue balances despite an improving turnover ratio"}
  - {metric: "CRISIL (or successor rating agency) rating trajectory", healthy: "stable outlook, no further downgrade", red_flag: "any additional downgrade after two already occurred in FY26"}
unit_economics:
  unit: "Extrusion: one engineered extrusion line/machine. Battery: one lithium-ion battery pack/BMS module"
  revenue_per_unit: "NOT FOUND — AR discloses only aggregate segment revenue, no unit counts or ASP for either segment"
  margin_per_unit: "NOT FOUND at unit level — segment result margin is disclosed (Extrusion 16.1% of segment revenue FY26 down from 19.3%; Battery -31.9% of segment revenue FY26 down from -20.1%), but not per-unit"
  key_lever: "Extrusion: government infra-capex cycle (JJM) timing. Battery: utilisation of the ~7 GWh Chakan capacity against a management-claimed Rs 1,500+ Cr revenue ceiling (implied ~9% utilisation on FY26 segment revenue of Rs 136.11 Cr, a computed cross-check, not an AR-stated figure)"
first_deterioration_signals:
  - {risk: "Revenue model: Battery segment growth trailing its own cited industry growth", first_signal: "Battery Division segment revenue (Note 38) growth rate vs disclosed EV industry unit growth"}
  - {risk: "Margin: negative operating leverage in Battery segment", first_signal: "Battery Division segment result as % of segment revenue, next reporting period"}
  - {risk: "Balance sheet: cash near-zero, rising debt, falling liquidity buffer", first_signal: "Cash and cash equivalents (Note 10) and current investments (Note 8) balances"}
  - {risk: "Execution: unnamed ~Rs 150 Cr FY27 order and unquantified capacity utilisation", first_signal: "Battery Division segment revenue realised in FY27 vs the Rs 150 Cr claim"}
  - {risk: "Structural: no captive cell supply, exposed to global cell price/FX", first_signal: "Consolidated/segment gross margin trend if cost data is ever disaggregated by segment"}
mgmt_questions:
  - "Battery segment loss widened Rs 25.53 Cr to Rs 43.35 Cr on 7.2% revenue growth — what quantified factors explain this against the MD&A's 'moving towards profitability as volumes scale up' claim?"
  - "Who is the counterparty and what is the delivery schedule for the ~Rs 150 Cr FY27 order cited in the MD&A?"
  - "What specific metric triggered the two CRISIL downgrades within FY26, and is the rating now stable into FY27?"
  - "What is current utilisation of the ~7 GWh Geon capacity, and what incremental capex is needed to reach the claimed Rs 1,500+ Cr revenue ceiling?"
  - "Following the Rs 30.39 Cr HEVPL/NCLT write-off, what credit-vetting process now applies to new EV-OEM and D2C customers?"
  - "Customer advances fell 18.9% while inventory stayed flat and receivables aged into multi-year overdue buckets — is this demand softness or a collections problem?"
  - "Is the Extrusion segment's 27.7% profit decline from temporary JJM funding delays, or from structural competitive pricing pressure?"
one_line_verdict: "Profitable shrinking machine business is subsidising a loss-widening battery bet growing slower than its own market."
analyst_note: "Every moat claim tested (market share, ARAI/AIS-156, IATF, design-win share, data network effect) traces only to the 2.5-year-stale Dec-2023 deck or to AR25; none appears in AR26. The single most load-bearing contradiction in this filing is that Battery segment revenue grew 7.2% while its loss ratio widened from -20.1% to -31.9% of segment revenue — the opposite of the operating-leverage story management tells in the same MD&A paragraph. Segment-level cost data (materials, employee cost by segment) is not disclosed, so unit economics and the margin-compression driver cannot be isolated between the two businesses; this is a genuine document gap, not an estimation opportunity."
```
