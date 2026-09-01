# STAGE 4: BUSINESS MODEL DECODER — Vinyas Innovative Technologies Ltd (VINYAS)
Run date: 2026-09-01 | Model: claude-sonnet-5 | Pipeline stage 4

Sources used: Annual Report FY2025-26 (AR), read in full (all statutory, MD&A, notes to
standalone and consolidated accounts). Investor Presentation H2 FY26, issued by the
company on 29-May-2026 (Inv. Pres.), read in full.

INPUT GAP: two additional PDFs sit in the presentation folder ("rpt 1.pdf", "rpt 2.pdf").
Both are third-party Substack blog posts (onetruthcapital.substack.com, dated 05-Jun-2026;
valueeducator.substack.com, dated 16-Oct-2025), not company-issued material. They contain
specific numeric claims the company itself never discloses (a "50/50 export/domestic split",
an "78% Defence & Aerospace / 18% Industrial / 1.7% Medical / 1.9% Others" FY25 revenue mix,
"112 days" debtor days, "185 days" net cash cycle, a named Israeli-defence-company joint
venture). None of these numbers trace to the AR or the official Inv. Pres. They are flagged
here as UNVERIFIED THIRD-PARTY CLAIMS, not used as anchors anywhere below, and are named so
the operator can task claude.ai with verifying or discarding them at Halt 1.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Vinyas builds electronic circuit boards, cable harnesses and fully assembled
electronic/electro-mechanical systems ("boxes") to the exact designs of defence,
aerospace, medical and industrial equipment makers, and increasingly also does some of
that design work itself.

### 1B. Money flow chain, each revenue stream

**Stream 1 — Build-to-Print (B2P) manufacturing.**
[Customer's own manufacturing data pack: circuit design, bill of materials, test
specs] → [Vinyas sources components, assembles PCBs, wires harnesses, tests to the
customer's spec at its NADCAP/AS9100/ISO-13485 certified Mysuru plant] → [Vinyas ships
finished boards, harnesses or sub-assemblies] → [the OEM customer, e.g. a defence
prime, medical device maker or industrial OEM] → [pays on invoice, standard 0-90 day
credit terms (AR Note 8.1(a), p.84), actual realisation running ~161 days, see 3B].
(AR "Build to Print (B2P)", p.10.)

**Stream 2 — Build-to-Specification (B2S) manufacturing with in-house design.**
[Customer need, not a finished design] → [Vinyas's own engineering team designs the
product under its "Integrated Product Development Process", builds prototypes, tests,
then manufactures at series volume] → [Vinyas delivers a qualified, ready-to-deploy
product] → [same OEM customer types] → [pays on invoice/milestone terms]. (AR "Build
to Specification (B2S)", p.10-11.) No revenue split between Stream 1 and Stream 2 is
disclosed anywhere in the AR or Inv. Pres. — NOT FOUND, check investor presentation or
concall.

**Stream 3 — Services (small).**
[Testing, engineering and after-sales support work billed separately from product
sale] → [Vinyas engineering/quality teams] → [deliverable is a service, not a
shipped good] → [same customer base] → [pays on invoice]. Disclosed as "Revenue from
Services" Rs 605.77 Lakh in FY26 vs Rs 1,072.04 Lakh in FY25 (AR Note 18, p.91) — this
stream actually SHRANK 43.5% in absolute terms even as total revenue grew ~30%.

### 1C. Revenue model classification (anchored)

| Stream | Type | Description | % of FY26 revenue | Predictability |
|---|---|---|---|---|
| Sale of products (B2P + B2S combined, split undisclosed) | Contract manufacturing / EMS, hardware sale | PCBAs, cable harnesses, sub-systems, box-builds | 100.76% of revenue from operations (Rs 51,823.51 Lakh of Rs 51,432.37 Lakh, AR Note 18 p.91) | Medium — order book of Rs 1,309.06 Cr as at 31-Mar-26 covers 2.5x FY26 revenue (Inv. Pres. p.6), but customer concentration is NOT DISCLOSED |
| Services (testing/engineering/after-sales) | Fee-for-service | Engineering, testing, support billed separately | 1.18% (Rs 605.77 Lakh, AR Note 18 p.91), shrinking | Low — no recurring-service disclosure, base is small and falling |
| Unbilled revenue movement (net) | Accounting timing item, not a true stream | Reversal of prior-year unbilled revenue | -1.94% (Rs -996.91 Lakh, AR Note 18 p.91) | N/A — timing/accrual effect |

Note: AR Note 34 states "The Company has only one geographical segment, hence [segment]
reporting is not provided" (AR p.104). This directly contradicts the ~50% export claim
in the run brief context and in the third-party blogs — that claim is a management
assertion elsewhere (not traced to AR text read) and is NOT corroborated by the
Company's own segment note. Flagged as unresolved.

Defence & Aerospace is stated qualitatively as "over half of our revenues" (AR "Our
Customer Base", p.13) — no exact percentage given anywhere in company material.
Medical Electronics is stated as "a modest share of overall revenue" (AR p.13).
Industrial Electronics has no quantification at all. Exact end-market revenue split:
NOT FOUND in AR or Inv. Pres.

### 1D. Simplified business model canvas

| Element | Answer |
|---|---|
| What they sell | Circuit board assemblies, cable harnesses, electro-mechanical sub-systems, and complete "box-build" systems, mostly to customer-supplied designs |
| Who buys | Defence PSUs/primes, global aerospace/defence OEMs, medical device OEMs, industrial electronics OEMs — 100+ customers (Inv. Pres. p.1); no single customer or top-N concentration disclosed anywhere |
| Why them | NADCAP AC7120 (electronics/PCB assemblies, achieved June 2025), AS9100-D, ISO 13485, IATF 16949, Defence Industrial License — a certification stack few small Indian EMS players hold (AR p.15-17) |
| How delivered | Single 150,000 sq ft facility in Mysuru, Karnataka (AR p.1, Inv. Pres. p.4) |
| Cost structure dominance | Materials: Rs 40,576.99 Lakh of Rs 51,432.37 Lakh revenue = 78.90% of revenue in FY26 (AR Note 20, p.91) — this is a materials-dominated cost structure, not a labour- or overhead-dominated one |
| Scarce resource | The certification stack itself (18-36 month qualification cycles per industry norm) plus 25 years of qualified-supplier relationships with defence primes |
| Pricing power source or absence | Weak on raw pass-through economics (material cost ratio worsened from 72.98% to 78.90% of revenue year on year, AR Note 20 vs Note 18); moderate switching-cost stickiness once a component is qualified into a customer's certified program |
| Asset intensity | Medium — net PP&E Rs 63.86 Cr against FY26 revenue of Rs 514.32 Cr (12.4% of revenue), single-site plant (AR Note 2, p.81) |
| WC intensity | High — receivable days ~161 (computed from AR Note 8.1/Note 18), raw material inventory +88.1% YoY (AR Note 7, p.83), operating cash flow NEGATIVE Rs 32.29 Cr in FY26 despite PAT of Rs 30.86 Cr (AR Standalone Cash Flow, p.70) |
| Regulatory moat or burden | Moat: Defence Industrial License (since 2016) and NADCAP/AS9100 create real entry barriers. Burden: same certifications require continuous compliance spend and audit readiness (AR p.16-17) |

### 1E. The chai-stall-uncle version

Imagine a tailor who doesn't design clothes — customers bring their own patterns, and
the tailor's job is to stitch them perfectly, on time, every time, using the right
thread and fabric. Vinyas is that tailor, but for electronics that go into fighter
jets, tanks, radars and dialysis machines. Most of the time (build-to-print),
customers hand Vinyas the exact "pattern" — circuit diagrams and parts lists — and
Vinyas assembles it with zero-defect precision because a bad solder joint in a missile
guidance system is not like a loose stitch. Increasingly, Vinyas is also learning to
design some of these patterns itself (build-to-spec), which pays better but is a newer
skill. The tailor buys most of the cloth (components) itself, so raw material cost is
by far the biggest expense — nearly 79 paise of every revenue rupee in FY26. And
because defence customers pay slowly and Vinyas has to stock components for months
before it gets paid, the business needs a lot of cash tied up in unpaid bills and
warehouse stock even while it is growing fast and profitably on paper.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Manufacturing (contract electronics manufacturing / EMS, with a growing design-and-build layer) | Mostly one-time product sale on purchase orders against a rolling order book, not subscription/recurring | Medium | High | Moderate (switching-cost driven, not price-setting) |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces (plain answers)

| Force | Answer | Effect |
|---|---|---|
| Competition count | Not disclosed by name in AR/Inv. Pres. beyond generic "global OEMs and Tier-1 partners" framing (AR p.5). India's defence/aerospace EMS space includes listed peers such as Data Patterns, Paras Defence, Azad Engineering and larger contract manufacturers like Dixon/Kaynes/Syrma in adjacent segments — none named by Vinyas itself | Neutral-to-hurts (fragmented but visibility on rivals is thin) |
| Entry barriers | High for the certified segment — NADCAP, AS9100-D, ISO 13485, Defence Industrial License, IATF 16949 all held (AR p.15); qualification and audit cycles are long | Helps |
| Supplier power | High — materials are 78.9% of revenue (AR Note 20) and include semiconductors/specialised substrates; RM inventory jumped 88.1% YoY (AR Note 7), suggesting the Company is stockpiling against supply risk, i.e. suppliers/lead-times have leverage | Hurts |
| Customer power and concentration | Customer concentration NOT DISCLOSED anywhere — no top-5/top-10 customer % in AR or Inv. Pres. "100+ Customers" is stated (Inv. Pres. p.1) but says nothing about concentration among them. Defence PSUs and large global primes typically have strong negotiating leverage on price and payment terms (161-day receivables is consistent with this) | Hurts |
| Substitutes | Low near-term substitution risk for certified defence/aerospace/medical electronics manufacturing — these are qualified, safety-critical supply chains, not commodity assembly | Helps |

### 2B. Competitive positioning map

Not constructible with anchored data — the AR names customers (Elbit Systems, Fresenius
Kabi, Schneider Electric, Bharat Electronics, IAI, Larsen & Toubro, Forbes Marshall,
Alpha Design Technologies, LLS, HAL — AR p.14) but names NO competitors anywhere.
NOT FOUND, check investor presentation or concall for a named competitor set.

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | No | No brand-driven pricing evidence; company sells B2B into technically-qualified programs, not brand-purchased | N/A |
| Network effects | No | Not a platform business | N/A |
| Switching costs | Yes | Once a component/assembly is qualified into a customer's certified program (aerospace/defence/medical), re-qualifying an alternate vendor is costly and slow (industry norm; not separately quantified by Vinyas in AR) | Medium-High while the qualified program runs |
| Cost advantage | Not evidenced | Material cost ratio WORSENED YoY (72.98% → 78.90% of revenue, AR Note 20/18) — the opposite of a demonstrated cost advantage | Low, unproven |
| Regulatory/licensing | Yes | NADCAP AC7120, AS9100-D, ISO 13485, IATF 16949, Defence Industrial License (since 2016), Defence Offset Program membership (2011) — all AR p.7, 15-17 | High — multi-year re-certification cycles create durability |
| Scale | No | Explicitly a "low-medium volume, high-mix" EMS model (AR "Why Vinyas", p.5), the opposite of a scale-cost strategy | N/A |
| IP/patents | No | B2P model means customer owns the design IP; even B2S design work is delivered to the customer, no evidence of Vinyas-retained IP in AR | N/A |
| Data/toll-gate | No | Not applicable to this business | N/A |

### 2D. Industry lifecycle stage
Growth stage, policy-tailwind driven (India defence indigenisation / "Make in India",
plus global supply-chain diversification away from single-country sourcing —
management commentary, AR p.19). Vinyas is a small, sub-scale, niche-certified player
inside a growing but still concentrated (few certified domestic EMS players) segment
of that industry.

### 2E. Key industry drivers

| Driver | Direction | Impact on Vinyas |
|---|---|---|
| Defence indigenisation / offset policy | Positive, structural | Order book Rs 1,309 Cr, order inflow Rs 960.38 Cr in FY26 (Inv. Pres. p.6) |
| Global OEM supply-chain diversification ("China+1") | Positive | Cited explicitly by MD as a tailwind and also as a source of "short-term supply chain disruptions" (AR p.19) |
| Vertical expansion into medical/industrial | Positive but unquantified | Company states intent to expand medical device and commercial aerospace supply chains (AR "Our Objectives", p.5) but gives no revenue targets |
| Raw material / component price and lead-time volatility | Negative | RM inventory +88.1% YoY, gross margin (Revenue less Materials) fell from 27.0% to 21.1% YoY (computed from AR Note 18/20) |
| Working capital cycle length (defence payment terms) | Negative | Receivable days ~161; operating cash flow negative in FY26 despite profit growth (AR Cash Flow Statement, p.70) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these

| Commonly tracked ratio | Verdict | Why |
|---|---|---|
| Gross margin in isolation | MISLEADING | It swings with B2P/B2S mix and single-order pass-through pricing, neither of which is disclosed; FY26 gross margin fell (27.0%→21.1%, computed) even as EBITDA margin rose (11.09%→12.50%, AR/Inv. Pres. p.10) because of a "Changes in Inventories of WIP" swing — see 3D. Read gross margin only alongside the WIP-change line, never alone |
| Price-to-book | MISLEADING | Vinyas doesn't own the IP behind most of what it builds (customer-supplied designs under B2P); book value understates the qualified-relationship and order-book value that actually drives worth |
| Revenue growth rate alone | MISLEADING | Revenue growth (29.67% YoY, AR Note 18) is lumpy and order-execution driven; must be read against order book growth (Rs 863 Cr → Rs 1,309 Cr, Inv. Pres. p.6) and against cash conversion, not standalone |
| PAT / PAT growth alone | MISLEADING | PAT grew 58.92% YoY (AR MD&A, p.65) while operating cash flow went NEGATIVE Rs 32.29 Cr (AR Cash Flow Statement, p.70). Profit growth without cash-conversion context is actively dangerous here |
| Dividend yield | IRRELEVANT | No dividend history disclosed; capital is being reinvested/raised (Rs 61.25 Cr of share warrants issued in FY26, AR Note 11(v), p.88) |

### 3B. Must-track metrics

**Growth**

| Metric | Tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Revenue growth vs order inflow growth | Whether growth is backed by real new demand or is drawing down backlog | Order inflow growing faster than or in line with revenue | AR MD&A p.65, Inv. Pres. p.6 | Order inflow growth persistently below revenue growth (backlog depletion) |
| Order book / trailing revenue (book-to-bill cover) | Revenue visibility | >1.5-2x for an order-driven manufacturer | Inv. Pres. p.6 (Rs 1,309.06 Cr / Rs 514.32 Cr = 2.5x, computed) | Falling below 1.0-1.5x |

**Profitability and efficiency**

| Metric | Tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Material cost as % of revenue | Whether the Company can pass through / control its dominant cost line | Stable or falling | AR Note 20 vs Note 18 (78.90% FY26 vs 72.98% FY25, computed) | Rising trend without matching EBITDA-margin protection |
| EBITDA margin, read WITH the "changes in inventory" P&L line | True operating profitability, not an inventory-accounting artefact | Consistency across quarters | AR Note 21, p.91 (FY26 WIP change Rs 6.04 Cr vs FY25 Rs 33.26 Cr — a large swing factor in the FY26 margin improvement) | Margin gains disappearing once WIP swings normalise |
| Cash conversion (Operating cash flow / EBITDA) | Whether paper profit becomes real cash | Positive, ideally >60-70% | AR Standalone Cash Flow Statement, p.70 (FY26: -Rs 32.29 Cr / Rs 64.77 Cr EBITDA = negative) | Negative or persistently well below 50% |

**Balance sheet and risk**

| Metric | Tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Trade receivable days | Customer payment discipline / concentration leverage | <90-120 days for a diversified industrial book | AR Note 8.1 + Note 18 (~161 days FY26, computed) | Rising trend or >180 days |
| Debt-Equity and DSCR | Balance sheet cushion funding the WC cycle | D/E <1x, DSCR >2x | AR Note 35 Analytical Ratios, p.104 (D/E 0.55x, DSCR 4.15x, both improved YoY) | D/E rising while OCF stays negative — currently the WC gap is being plugged by fresh equity/short-term debt, not operations |
| Related-party revenue ceiling vs total revenue | Whether future growth is genuinely third-party or routed through minority-owned associates | RPT revenue ceiling well below total revenue, arm's-length pricing independently verified | AR AGM Notice Items 6-7 and Annexure, p.2-3 (Nexus Rs 400 Cr ceiling [26%-owned associate] + UVT Rs 150 Cr ceiling [49%-owned associate] = Rs 550 Cr, against FY26 total revenue of Rs 514 Cr) | RPT actuals growing toward the approved ceiling without independent pricing verification |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find | Status here |
|---|---|---|
| Certifications held (NADCAP, AS9100-D, ISO 13485, IATF 16949, Defence License) | AR p.15-17 | All held; NADCAP newly achieved June 2025 |
| Customer count | Inv. Pres. p.1 | 100+ (no concentration breakdown) |
| New customer/program "logos" added per year | Inv. Pres. p.6 | 4 Defence & Aerospace, 3 Industrial, 1 Medical device logo added in FY26 |
| Order book and order inflow | Inv. Pres. p.6 | Rs 1,309.06 Cr book; Rs 960.38 Cr inflow FY26 |
| Headcount and gender mix | AR Annexure IV p.64, AR Statutory Report p.54 | 413 permanent employees; Male 251 / Female 162 |
| Manufacturing footprint | AR p.1, Inv. Pres. p.4 | Single site, 150,000 sq ft, Mysuru; a further 25,000 sq ft Class 3 facility planned (Inv. Pres. p.6) |
| Credit rating trajectory | Inv. Pres. p.4 | CRISIL A2 (short-term) / BBB+ Stable (long-term) |

### 3D. Unit economics — the physics of the business

- **Define one unit:** the cleanest disclosed unit is Rs 1 of revenue recognised on a
  shipped/executed order, since Vinyas does not disclose per-board or per-assembly
  pricing.
- **Revenue per unit:** not disclosed at product level; only aggregate revenue (Rs
  51,432.37 Lakh, AR Note 18) is available.
- **Cost per unit:** of every Rs 1 of FY26 revenue, materials consumed ~79 paise (AR
  Note 20), employee cost ~5.8 paise (AR Note 22: Rs 2,976.25 Lakh / Rs 51,432.37 Lakh),
  finance cost ~3.0 paise (AR Note 23), other expenses ~2.3 paise (AR Note 25),
  leaving an EBITDA margin of ~12.5 paise (AR/Inv. Pres. p.10).
- **Volume drivers:** number of qualified programs won and their execution pace
  against the Rs 1,309 Cr order book (Inv. Pres. p.6); NOT the number of end-units
  shipped, which is undisclosed.
- **Price drivers:** largely cost-plus/market-linked contract pricing per program (AR
  RPT pricing basis language, p.2); no evidence of Vinyas-side pricing power beyond
  what certification-driven switching costs allow.
- **Cost drivers:** component/raw-material cost and lead time dominate (78.9% of
  revenue); working capital carrying cost (finance costs rose to Rs 1,559.16 Lakh in
  FY26 from Rs 1,336.58 Lakh, AR Note 23, funding the receivables/inventory build).
- **Incremental margin and operating leverage:** genuinely hard to isolate here. The
  disclosed FY26 EBITDA-margin improvement (11.09%→12.50%) coincided with a
  deteriorating gross margin (27.0%→21.1%, computed), meaning the visible margin gain
  is substantially explained by a smaller "Changes in Inventories of WIP" expense
  swing (Rs 6.04 Cr FY26 vs Rs 33.26 Cr FY25, AR Note 21) rather than by demonstrated
  operating leverage on fixed cost. This is an accounting-timing effect, not proven
  unit economics improvement, and should be watched, not assumed, next year.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item to watch |
|---|---|---|
| Revenue model | Undisclosed customer concentration in a defence-PSU-heavy book; a single lost program could be material | Revenue from operations QoQ vs order book decline (AR Note 18-equivalent in quarterlies) |
| Margin | Material cost pass-through failing (72.98%→78.90% of revenue YoY) while FY26 EBITDA-margin gain is partly a WIP-accounting artefact | Cost of Materials Consumed / Revenue from operations ratio (AR Note 20/18 equivalents) |
| Balance sheet | Working capital funded by fresh equity/short-term debt, not operating cash — FY26 operating cash flow was -Rs 32.29 Cr against PAT of +Rs 30.86 Cr | Net cash from operating activities (Standalone Cash Flow Statement) |
| Execution | 88.1% YoY raw-material inventory build (AR Note 7) ahead of revenue recognition — execution/conversion risk if orders slip | Inventory (Raw Materials) as % of trailing revenue |
| Structural | Two related-party associates (Nexus, 26%-owned; UVT, 49%-owned) approved for RPT ceilings totalling Rs 550 Cr against FY26 revenue of Rs 514 Cr — future "growth" could be substantially related-party in nature | RPT actual revenue disclosed in subsequent AR Note 33 / quarterly RPT filings, tracked against the approved ceiling |

### 4B. Valuation method applicability (handoff to Role 1)

| Method | Applicable? | Notes |
|---|---|---|
| EV/EBITDA (peer multiple) | Yes — PRIMARY | Standard for a profitable, leveraged, order-book-driven contract manufacturer; cross-checkable against listed Indian defence-electronics/EMS peers. Section 1B governs the exit multiple; this stage only flags method suitability |
| DCF anchored to order-book execution | Yes — SECONDARY | Rs 1,309 Cr book at 2.5x trailing revenue gives a bottom-up revenue-visibility anchor for a 3-5 year cash flow build, but must explicitly model the working-capital drag shown in the FY26 cash flow statement, not just P&L profit |
| EV/Sales | Yes — TERTIARY | Useful cross-check specifically BECAUSE cash conversion and margin quality are currently unproven (negative FY26 OCF); a sales-based cross-check avoids over-relying on an EBITDA/PAT figure with a known accounting-timing distortion |
| P/B (Price-to-Book) | Not applicable | Book value doesn't capture qualified-relationship/order-book value; B2P model means limited owned IP sits on the balance sheet |
| Dividend discount model | Not applicable | No dividend history; reinvestment-stage SME |
| SOTP/NAV | Not applicable | Single-site, single-segment operating business; no material non-operating assets disclosed |
| Cycle stage that matters for valuation | Growth/order-execution stage — the business is scaling on a genuine order book but has NOT yet proven it can convert that growth into cash; valuation should discount for the working-capital/cash-conversion gap until at least 2 more quarters of evidence |

### 4C. Quarterly monitoring checklist (max 15)

1. Revenue from operations QoQ and YoY vs order book change — good: both rising together; trouble: revenue rising while order book flat/falling
2. Order inflow vs order book (book-to-bill) — good: >1x; trouble: <1x for two consecutive quarters
3. Material cost as % of revenue — good: stable or falling; trouble: continuing above ~79%
4. EBITDA margin AND the WIP/inventory-change P&L line together — good: margin holds even as WIP swing normalises; trouble: margin falls back toward 11% once the WIP base effect fades
5. Operating cash flow (not just PAT) — good: turning positive; trouble: further negative quarters
6. Trade receivable days — good: trending down from ~161; trouble: rising further or >180 days
7. Raw material inventory level and growth rate — good: growth decelerating in line with revenue; trouble: continued outsized build
8. Short-term borrowings/cash credit utilisation — good: stable or falling as % of revenue; trouble: rising to fund receivables/inventory
9. Debt-Equity ratio and DSCR — good: D/E <0.6x, DSCR >3x sustained; trouble: reversal of the FY26 improvement
10. Related-party transaction actuals (Nexus, UVT) disclosed each quarter — good: small, transparently priced, independently benchmarked; trouble: rising fast toward the Rs 550 Cr combined ceiling
11. New "logos"/programs won by segment (Defence, Industrial, Medical) — good: continued diversification; trouble: concentration in one segment/customer
12. Segment/export revenue disclosure — good: Company finally discloses a geographic/segment split; trouble: continued single-segment reporting despite an export claim
13. Credit rating (CRISIL) — good: stable/upgraded; trouble: downgrade or outlook change
14. Capex utilisation (PP&E additions, CWIP) vs named signed programs — good: tied to contracted orders; trouble: speculative capacity build
15. Employee cost and headcount growth vs revenue growth — good: cost growth below revenue growth; trouble: cost growth outpacing revenue (margin erosion signal)

### 4D. Highest-value questions for management

1. What is the top-5 and top-10 customer share of FY26 revenue, and what is the single largest customer's share? Reassures: top-5 <40%, no customer >25%. Worries: concentration undisclosed or one customer >25-30%.
2. What is the FY26 revenue split between Build-to-Print and Build-to-Spec, and where is that mix headed? Reassures: rising, quantified B2S share with margin uplift evidence. Worries: still overwhelmingly B2P (low value-add) with no design-fee capture shown.
3. Why did material cost rise from 72.98% to 78.90% of revenue even as EBITDA margin improved? Reassures: a specific, temporary, order-mix explanation with a credible reversal plan. Worries: a structural pricing-power problem management can't explain.
4. What is the expected revenue timeline from Nexus Advanced Technologies (26%-owned) and United Vinyas Technologies Inc (49%-owned), and how will arm's-length pricing be independently verified given approved ceilings of Rs 550 Cr combined against Rs 514 Cr of FY26 revenue? Reassures: concrete near-term milestones and third-party pricing benchmarks already in place. Worries: vague, open-ended answers that suggest RPT revenue could substitute for genuine external demand.
5. What is driving the ~161-day receivable cycle and the 88.1% raw-material inventory build, and when does management expect operating cash flow to turn positive? Reassures: specific defence-PSU payment-term explanation with a collection catch-up plan and a stated OCF-positive quarter target. Worries: no clear plan, continued reliance on external financing.
6. What exactly is the FY26 export vs domestic revenue split, given Note 34 discloses only a single geographic segment? Reassures: a granular, auditable breakdown is provided. Worries: continued non-disclosure despite a stated ~50% export claim elsewhere.
7. What is the expected utilisation and payback of the recent capex (Rs 30.89 Cr PP&E additions, Rs 4.50 Cr CWIP) and the planned 25,000 sq ft Class 3 facility? Reassures: tied to named, signed programs. Worries: capacity built ahead of demonstrated demand.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

| Field | Value |
|---|---|
| Company | Vinyas Innovative Technologies Ltd (NSE Emerge: VINYAS) |
| Business type | Manufacturing — contract electronics manufacturing (EMS), build-to-print + build-to-spec, transitioning toward system integration/box-build |
| Archetype (per CLAUDE.md library) | PRIMARY: Outsourcing partner (CDMO/EMS/IT services) — client concentration undisclosed, wallet share undisclosed, capacity fill/order-book based, contract stickiness via certification lock-in, price per unit undisclosed. SECONDARY/transitional overlay: Build-to-spec component maker — company is explicitly climbing from pure board-stuffing toward design-and-test (B2S) and full system integration (AR "Our Objectives", p.5). Also touches the Order-book business (EPC/defence/capital goods) archetype given order inflow/book-to-bill/WC as the operative variables |
| Revenue nature | Order-book-driven product sale, ~99% goods/~1% services (computed, AR Note 18) |
| FY26 revenue / EBITDA / PAT | Rs 514.32 Cr / Rs 64.77 Cr (12.50% margin) / Rs 30.86 Cr (6.00% margin) (AR p.65, Note 18/26/etc.) |
| Order book / order inflow | Rs 1,309.06 Cr / Rs 960.38 Cr FY26 (Inv. Pres. p.6) |
| Asset intensity | Medium — net PP&E Rs 63.86 Cr (12.4% of revenue) |
| WC intensity | High — receivable days ~161, RM inventory +88.1% YoY, FY26 operating cash flow NEGATIVE Rs 32.29 Cr despite profit growth |
| Pricing power | Moderate (certification switching-cost driven), NOT demonstrated on gross margin (material cost ratio worsened YoY) |
| Cyclicality | Cyclical/order-execution driven, inside a structurally growing (defence indigenisation) segment |
| Key moat | Regulatory/licensing (NADCAP, AS9100-D, ISO 13485, IATF 16949, Defence Industrial License) — durable, multi-year re-qualification cycles |
| Biggest single flag | Rs 550 Cr combined RPT ceiling approved for two minority/near-majority-owned associates (Nexus 26%, UVT 49%) against Rs 514 Cr FY26 total revenue — a structural question over how much of future growth is genuinely third-party demand |
| Primary valuation method | EV/EBITDA peer multiple (Section 1B governs the actual exit multiple) |
| Secondary valuation method | DCF anchored to order-book execution, explicitly modelling the working-capital drag |
| Tertiary valuation method | EV/Sales (cross-check given unproven cash conversion) |
