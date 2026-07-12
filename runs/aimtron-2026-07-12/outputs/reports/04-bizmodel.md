# STAGE 4: BUSINESS MODEL DECODER — Aimtron Electronics Ltd (AIMTRON)
Run date: 2026-07-12 | Model: claude-sonnet-5

Primary source: Annual Report FY2024-25 (text extraction, "AR"). Secondary source: Investor Presentation H2 & FY2026, issued 29-Apr-2026 (text extraction, "Inv. Pres."). Both source PDFs exceeded the image-render size limit, so both were read as pre-extracted plain text; image-only charts/infographics inside the presentation may be under-read where the text layer did not carry the numbers (each such gap is marked NOT FOUND below). Screener.in's Data_Sheet FY26 P&L is flagged internally inconsistent by the operator and is NOT used; all FY25 figures are the audited AR, and FY26 figures are the company's own Investor Presentation disclosures (not yet confirmed against an audited FY26 annual report, which does not exist yet as of this run).

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Aimtron is a contract electronics manufacturer (EMS/ESDM) that takes a customer's circuit-board design or product idea and turns it into tested, delivered hardware — populated circuit boards, or entire boxed devices — for industrial, defence, medical, automotive, telecom and IoT customers who don't want to build and staff their own factory (AR p.4-5, "Who We Are").

### 1B. Money flow chain for each revenue stream

**Stream 1 — PCB Assembly (PCBA):**
[Customer supplies a PCB design/BOM, or Aimtron's design team creates one] → [Aimtron sources components globally and populates/solders the bare board on its SMT/THT lines, then inspects and tests it] → [delivers a finished, tested circuit-board assembly] → [industrial/medical/auto/defence OEM customer pays] → [invoice on delivery, standard trade-credit terms — but see WC flag in Section 3] (AR p.20-21, "Product Portfolio"; AR Note 19 Revenue Recognition, p.92-93).

**Stream 2 — Box Build:**
[Customer specifies an enclosure/full-system spec] → [Aimtron integrates the PCBA with cables, sheet metal, enclosures, magnetics and does full system-level functional testing and packaging] → [delivers a ready-to-use, market-ready electronic product/system] → [OEM pays] → [invoice on delivery; higher rupee value per order because far more bought-out material (enclosure, cabling, sub-assemblies) passes through Aimtron's books] (AR p.20-21; Inv. Pres. slide 10, "Vertically Integrated One-Stop Shop").

**Stream 3 — ODM / Design-to-Delivery ("End to End Solutions"):**
[Customer brings only a concept or a performance need] → [Aimtron's 150+ design engineers do product design, firmware/embedded software, BOM optimisation, prototyping and certification support (FCC/CE/UL etc.)] → [delivers a certified, production-ready design/prototype, typically followed by a manufacturing contract for the same product] → [OEM pays milestone/service fees now, and captures downstream PCBA/Box Build manufacturing revenue later] (AR p.22-23, "ODM Product Development"; Inv. Pres. slide 11).

### 1C. Revenue model classification (anchored)

| Stream | Type (taxonomy) | Description | % of revenue | Predictability |
|---|---|---|---|---|
| PCBA | Contract manufacturing — unit-based product sale, point-in-time revenue recognition | Populate and test bare circuit boards to spec | 69.3% (FY25, standalone) → 28.6% (FY26, standalone) (AR p.76-77, Industry-Wise/Segment-Wise table; Inv. Pres. slide 33) | Medium (order-book driven, but board-level orders can be lumpy) |
| Box Build | Contract manufacturing — unit-based product sale, point-in-time | Full system integration: PCBA + enclosure + cable + test + packaging | 27.2% (FY25) → 68.8% (FY26) (AR p.76-77; Inv. Pres. slide 33) | Medium (larger, longer programs; became the dominant stream in one year — see flag below) |
| ODM / End-to-End Solutions | Design & engineering services — milestone/contract revenue | Concept-to-prototype design, firmware, certification support | 3.5% (FY25) → 2.6% (FY26) (AR p.76-77; Inv. Pres. slide 33) | Low-Medium (project-based, smallest and most skill-intensive slice, but the seed for future manufacturing contracts) |
| — memo: product vs service split | — | Sale of products vs sale of services (standalone) | Products 92.6% / Services 7.4% (FY25) (AR Standalone Notes, Note 19, "Revenue from Operations") | n/a |

**FLAG:** the PCBA/Box-Build mix inverted completely within one fiscal year (PCBA 69%→29%, Box Build 27%→69%, standalone). This is a structural change in the revenue model, not noise — see Section 3 on why blended gross margin is not comparable year-over-year without adjusting for this.

### 1D. Simplified business model canvas

| Element | Aimtron's position |
|---|---|
| What they sell | Assembled circuit boards, boxed electronic systems, and (small, growing) product-design services (AR p.20-23) |
| Who buys | OEMs and program owners across industrial, IoT/robotics, medical/healthcare, automotive/EV, aerospace & defence, telecom/power, gaming — 500+ customers globally claimed (AR p.4-5); no customer-concentration disclosure found (NOT FOUND, check concall) |
| Why them | Vertically integrated "one-stop shop" (design + PCBA + box build + cable/sheet-metal in-house) plus a widening certification stack (ISO 13485, IATF 16949, AS9100D in progress, CDSCO, RDSO in progress) that lets it serve regulated verticals competitors without those approvals cannot touch (AR p.10-11; Inv. Pres. slide 17) |
| How delivered | Two India facilities (Bengaluru, Vadodara) plus a new Texas subsidiary and the newly acquired Decatur, Illinois facility (Aimtron International Controls/ICS) (AR p.6-7; Inv. Pres. slide 12-13) |
| Cost structure dominance | Cost of materials (COGS/bought-out components) — 65-73% of revenue across FY22-FY26; employee costs are small by comparison but rising fast (AR p.76-77; Inv. Pres. slide 35-36) |
| Scarce resource | Qualified capacity (SMT lines, box-build lines) plus regulatory approvals/certifications, which take years to earn and are the real gate to high-value verticals (medical, defence, rail, auto) |
| Pricing power source or absence | Stated "value-based pricing" (AR p.19) but the company itself names "intense competition from global and local ESDM players" as a threat (AR p.75, SWOT) — moderate, concentrated in the regulated/high-mix niches, weak in commodity PCBA |
| Asset intensity | Medium — net PP&E has grown from Rs 226 Mn (FY24) to Rs 309 Mn (FY25) to Rs 627 Mn (FY26), i.e. roughly 19-24% of revenue (Inv. Pres. slide 37) |
| WC intensity | High and rising — see Section 3; trade receivables turnover collapsed from 9.28x to 3.07x in FY25 alone (AR Consolidated Notes, Note 37, p.144-145) |
| Regulatory moat or burden | Both: certifications are a genuine barrier to entry for regulated verticals, but they are also a continuous compliance cost and a source of risk if lapsed (AR p.44-45, "Compliance Risk") |

### 1E. The chai-stall-uncle version
Think of Aimtron like a master tailor's shop, but for electronics. Customers — big companies who don't want to run their own factory — either bring a finished pattern (a circuit design) or just an idea for an outfit (a product concept). Aimtron buys the "fabric" (electronic components, sourced from India, China, the US, Taiwan and more) and stitches it together on precision machines (SMT lines) into a finished circuit board. Some customers just want the shirt (the bare board — that's PCBA); others want the whole suit, buttons, lining, packaging and all (that's Box Build, which uses much more "fabric" per order, so it looks like a bigger bill even if the tailoring skill is the same). And now Aimtron is also starting to design brand-new outfits from a client's rough sketch (ODM design services) — the smallest, hardest and best-paid part of the shop today, but the one management is betting will grow the most. The tailor doesn't own the fabric mill or the store selling the finished suits — it just does the skilled stitching in the middle, for a fee.

### Section 1 summary table

| Business type | Revenue nature | Asset intensity | WC intensity | Pricing power |
|---|---|---|---|---|
| Manufacturing (contract electronics manufacturing/EMS-ODM, with a small and growing design-services component) | Transactional/order-book driven, point-in-time on delivery; ~93% product sale, ~7% service fee (AR Note 19) | Medium (~20-24% of revenue in net PP&E and rising with capacity expansion) | High and rising (receivables turnover fell from 9.28x to 3.07x in one year) | Moderate — value-based pricing claimed, but real power sits only in regulated/high-mix niches; commodity PCBA is competitive and price-taking |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Plain read | Helps / Hurts / Neutral |
|---|---|---|
| Competition count | "Intense competition from global and local ESDM players" and specifically named European competitors as a margin-pressure risk (AR p.75-77) | Hurts |
| Entry barriers | Certifications (ISO 13485, IATF 16949, AS9100D pending, CDSCO, RDSO pending), multi-year customer qualification cycles for medical/auto/defence programs, and capex for SMT/box-build lines (AR p.10-11; Inv. Pres. slide 17) | Helps (in regulated verticals only) |
| Supplier power | Sources critical components from India, China, USA, UK, Hong Kong, Singapore, Taiwan, Ireland, Thailand — deliberately diversified to avoid dependency on any one supplier/region (AR p.32-33) | Neutral-to-helps (diversification reduces but does not eliminate component-shortage risk, named explicitly as a Weakness in the AR's own SWOT: "Dependency on key suppliers for critical components," AR p.75) |
| Customer power and concentration | No top-customer or top-10-customer disclosure found anywhere in the AR or Investor Presentation (NOT FOUND, check investor presentation or concall). Order book is described as "spread across various sectors and regions" (Inv. Pres. slide 30) but this is qualitative, not quantified | Hurts (opacity itself is a governance/diligence gap) |
| Substitutes | In-house manufacturing by large OEMs, or larger EMS players (global scale) offering the same one-stop-shop capability | Hurts (only mitigated by Aimtron's niche certifications and relationships) |

### 2B. Competitive positioning map
No named competitors or market-share figures appear in the AR or Investor Presentation (NOT FOUND, check investor presentation or concall). One Advisory Board bio references prior experience "at Kaynes Technology" (AR p.[Advisory Board section], not independently a competitor disclosure). For context only (analyst general knowledge, not sourced from company documents, and explicitly NOT anchored): India's listed EMS/ODM peer set commonly includes Kaynes Technology, Syrma SGS Technology, Dixon Technologies, Avalon Technologies and Cyient DLM — none of these are named or benchmarked by Aimtron in the provided documents, and no relative-scale or relative-margin comparison can be made from what was read.

### 2C. Moat assessment (eight standard types)

| Moat type | Evidence | Durability |
|---|---|---|
| Switching costs | Once qualified as a vendor for a medical/auto/aerospace/rail program, re-qualifying a new EMS vendor is costly and slow for the customer; AR states "long-term, established customer relationships" and multi-year program wins (AR p.10-11, 24; Inv. Pres. slide 24, 30) | Medium-High, but unproven at scale — no repeat-customer-revenue % disclosed |
| Network effects | None identified | Absent |
| Economies of scale | Some evidence via the ICS acquisition thesis — "faster time-to-market... building similar infrastructure organically would have taken 24-36 months" (Inv. Pres. slide 13), and utilisation ramp economics (54%→90% over 3 years on existing footprint) | Medium, emerging |
| Cost advantages | Not evidenced; employee costs grew faster than revenue in H2FY26 (313.5% YoY vs 75.9% revenue YoY) (Inv. Pres. slide 35), suggesting the company is hiring ahead of scale, not yet harvesting a cost edge | Weak/absent currently |
| Brand | Regional industry awards (ELCINA 2023-24, Karnataka Innovation Leadership 2022) but no evidence of pricing power from brand recognition (AR p.51) | Weak |
| Regulatory/licensing moat | ISO 13485 (medical), IATF 16949 (automotive), AS9100D (aerospace/defence, in progress), CDSCO (medical device market access), RDSO (Indian Railways, in progress), CSA (Canada) — a genuinely wide and still-expanding certification stack (AR p.10-11; Inv. Pres. slide 17) | Medium-High — years to replicate, but held by many peers too |
| Intangible assets/IP | Limited; this is largely work-for-hire/design-service engineering, not proprietary product IP. One exception: PLI/ECMS application for Optical Transceivers (SFP) under Aimtron Mechatronics — application submitted, approval pending (Inv. Pres. slide 22) | Weak today, optionality if PLI/ECMS approval comes through |
| Efficient scale (niche too small for many entrants) | Ruggedized/harsh-environment electronics niche via the ICS acquisition (agritech, mining, fire & safety, defence) with "specialised infrastructure ready" (Inv. Pres. slide 13) | Medium, unproven — one quarter of financial data (Feb-Mar 2026) available |

### 2D. Industry lifecycle stage and Aimtron's position
India's ESDM/EMS sector is explicitly described by the company as early-to-mid growth: targeted electronics manufacturing output of USD 500 Bn by 2030, requiring a "5x increase in production" (AR p.68-71; Inv. Pres. slide 39). Global EMS is more mature (forecast USD 1,145 Bn by 2026, moderate CAGR) while India's EMS market is described as "mirror[ing] where [Taiwan/Vietnam/Singapore/China] stood a decade ago" (AR p.70-71) — i.e. an early, policy-subsidised build-out phase. Aimtron itself is a small, fast-scaling participant (Rs 158 Cr FY25 revenue standalone, guided to more than double by FY26) riding this early-industry tailwind rather than competing as an established incumbent.

### 2E. Key industry drivers

| Driver | Direction | Impact on Aimtron |
|---|---|---|
| China+1 supply-chain diversification | Positive, structural | Directly cited as driving "three long-term programs from North American and European customers pivoting their sourcing to India" (AR p.14-15) |
| PLI / Electronics Component Manufacturing Scheme (ECMS) and Semicon India | Positive, policy-driven | Aimtron Mechatronics' SFP transceiver application under ECMS is pending approval (Inv. Pres. slide 22); broader PLI cited as a tailwind (AR p.12-13) |
| India-EU/UK FTA and tariff rationalisation | Positive | Cited as enabling entry into European automotive customers and reducing trade friction (AR p.12-13; Inv. Pres. slide 31) |
| Defence/aerospace indigenisation ("Make in India") | Positive | AS9100D certification in progress; RDSO (Railways) approval in progress; defence share of standalone revenue rose from 0% (FY24) to 5.3% (FY25) (AR p.76-77) |
| Global EMS competitive intensity / component cost inflation | Negative | Named explicitly as risks (Commodity Price Risk, Competition Risk) (AR p.76-77) |
| FX volatility | Mixed/negative | Company has both import cost exposure and export receivables; states it uses forward contracts and natural hedges (AR p.44-45, 76-77) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these / track-these

| Commonly tracked ratio | Why it is misleading or irrelevant here |
|---|---|
| Price-to-Book (P/B) | The FY25 equity base jumped from Rs 517 Mn to Rs 1,550 Mn largely because of one-time IPO share-premium capital (Inv. Pres. slide 37), not retained earnings from operations; book value doesn't reflect the design/engineering capability that actually drives future orders |
| Dividend yield | Board explicitly "does not recommend any dividend" (AR p.[Board's Report, Dividend section]) — by design, 100% reinvestment for the stated 40-50% CAGR target; yield is structurally zero and tells you nothing |
| Gross margin % (blended, YoY, unadjusted) | PCBA, Box Build and ODM have structurally different bought-out-material intensity. The mix inverted from 69%/27%/3.5% to 29%/69%/2.6% (PCBA/Box-Build/ODM) in one year (AR p.76-77; Inv. Pres. slide 33), which alone explains most of the swing in blended gross margin from 38.2% (FY24) to 27.1% (FY25) to 29.1% (FY26, consolidated) — comparing this ratio YoY without normalising for mix will misread execution quality |
| Same-store-sales / like-for-like growth | Retail metric; Aimtron is a project/order-book driven contract manufacturer, not a store network |
| Net Interest Margin / banking-style spread ratios | Not applicable; industrial manufacturer, not a lender |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| Order book / book-to-bill | Forward revenue visibility | ≥1.5x trailing-12m revenue (closing order book was ~1.7x FY26 revenue, Inv. Pres. slide 30/34) | Investor Presentation, quarterly order book slide | Book-to-bill <1x for two straight quarters |
| Revenue growth (segment mix) | Whether growth is broad-based or concentrated | Growth across ≥3 of the top verticals simultaneously | AR MD&A Industry-Wise Performance table; Inv. Pres. Revenue Breakdown slide | A single vertical (e.g. Telecom, which went from 0% to 22.3% of FY26 standalone revenue) driving all incremental growth |
| RFQ pipeline conversion | Whether the demand funnel is turning into firm orders | Rising RFQ pipeline alongside rising order book | Inv. Pres. slide 30/34 (~Rs 9,000-9,500 Mn standalone RFQ pipeline) | RFQ pipeline flat/declining while order book growth decelerates |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| EBITDA margin | Underlying operating profitability net of mix effects | 20-25% (FY22-FY26 range was -2.3% to 25.4%; FY26 consolidated 21.8%) | AR MD&A Financial Performance table; Inv. Pres. Income Statement | Sustained sub-18% without a corresponding jump in scale |
| Employee cost as % of revenue | Whether hiring is ahead of or behind volume | Growing roughly in line with or slower than revenue growth | AR/Inv. Pres. income statement lines | Employee cost growth persistently outpacing revenue growth (H2FY26: employee costs +313.5% YoY vs revenue +75.9% YoY, Inv. Pres. slide 35) |
| ROCE / ROE | Capital efficiency through the growth phase | Consolidated FY25: ROCE 20.73%, ROE 24.80% (AR Consolidated Notes, Note 37) | AR Ratio Analysis note | Consistent multi-quarter decline (FY24 ROCE was 30.58%, ROE 31.26% — already declining as the equity/capital base grew faster than earnings) |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| Trade receivables turnover (Debtors turnover) | Cash conversion quality | ≥6x (~60 days) | AR Consolidated Notes, Note 37, Ratio Analysis | <4x — already breached: fell from 9.28x (FY24) to 3.07x (FY25) |
| Inventory turnover | Component procurement/obsolescence efficiency | ≥4x | Same note | <3x |
| Net capital turnover ratio | Capital intensity of growth | ≥1.5x | Same note | <1x — fell from 2.25x (FY24) to 1.32x (FY25), already trending toward the flag |
| Debt-Equity and Interest Coverage | Leverage introduced to fund the FY26 capex/M&A wave | D/E manageable (<0.5x); interest coverage >10x | AR Note 37 (FY25: D/E 0.00, coverage 135.72x); Inv. Pres. slide 37 shows FY26 long-term borrowings of Rs 548.2 Mn newly raised | D/E rising materially alongside falling interest coverage as the new debt is drawn down and utilised |

### 3C. Industry-specific non-financial KPIs

| KPI | Where to find |
|---|---|
| Number of SMT/THT/box-build lines and utilisation rate | AR p.6-7 (9 SMT, 37 THT, 3 box-build lines, India); Inv. Pres. slide 13 gives ICS utilisation ramp target (~54% to ~90% over 3 years) |
| Design engineer headcount | AR p.4-5 / Inv. Pres. slide 5 (150+ design engineers) — a proxy for ODM/engineering capability scale-up |
| Certifications held/pending | AR p.10-11; Inv. Pres. slide 17 (ISO 13485, ISO 14001, EN ISO 9001, IATF 16949, CDSCO, CSA, AS9100D "in progress", RDSO "in progress") |
| Facility footprint and greenfield progress | Inv. Pres. slide 31 (new Vadodara greenfield facility, 6 SMT lines, phased rollout, Aug 2025 onward) |
| Order book value and bifurcation by sector/geography | Inv. Pres. slide 30, 34 |
| Customer concentration (top-5/top-10 %) | NOT FOUND anywhere in AR or Investor Presentation — check investor presentation or concall |
| Export vs domestic revenue mix | AR p.76-77 (Geography-wise table); Inv. Pres. slide 33 (FY26: India 74.3% vs FY25: India 58.3% — see flag below) |
| New certification/vertical entries | AS9100D (aerospace, in progress), RDSO (Railways, entered FY26), PLI/ECMS SFP application (Inv. Pres. slide 21-22, 34) |

### 3D. Unit economics — the physics of the business
Aimtron does not disclose a standardised "unit" (e.g. average revenue per board or per box-build project), so the cleanest available proxy is capacity: a production line (SMT or box-build cell) is the marginal unit of output.

| Element | Value | Anchor |
|---|---|---|
| Unit | One production line/cell (SMT, THT, or Box Build) at the India facilities, or the ICS Decatur facility as a whole for the clearest disclosed case | AR p.6-7; Inv. Pres. slide 13 |
| Revenue per unit | Not disclosed at line level. Best available proxy: ICS's existing 58,000 sq ft facility is guided to generate "up to USD 25-30 million p.a. (~Rs 280-300 crore)" in long-term revenue potential from utilisation ramping "~54% to ~90% over ~3 years," against only ~Rs 10-12 crore of incremental capex (ERP, AI, digitisation, working capital) | Inv. Pres. slide 13 |
| Cost per unit | NOT FOUND at a granular (per-board/per-project) level | — |
| Volume drivers | New customer program wins, order book conversion, new SMT/box-build line commissioning (e.g. new Vadodara greenfield, 6 lines phased) | Inv. Pres. slide 31 |
| Price drivers | Mix (Box Build carries far more pass-through material value per order than PCBA), vertical mix (defence/medical/IoT called out as "high-margin segments," AR p.19) | AR p.18-19 |
| Cost drivers | Component/material cost (65-73% of revenue historically) is by far the largest cost line; employee cost is small but rising fast as capacity scales ahead of volume | AR/Inv. Pres. income statements |
| Incremental margin / operating leverage | High, once fixed capacity is in place — the ICS case (54%→90% utilisation on an already-built facility, ~Rs 10-12 cr incremental capex against ~Rs 280-300 cr revenue potential) is the clearest evidence of strong incremental drop-through as utilisation climbs; the flip side is that under-utilised new capacity (new Vadodara lines) will drag margins until it fills | Inv. Pres. slide 13 |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item to deteriorate |
|---|---|---|
| Revenue model | Undisclosed customer concentration; a single large program win/loss could swing results materially (e.g. the Rs 975.5 Mn ODM contract with a "Leading US Infrastructure Firm," H1FY26, Inv. Pres. slide 30) | Orders executed vs opening order book; sudden order-book decline in a single reporting quarter |
| Margin | Structural mix shift toward Box Build (materials-pass-through heavy) compresses blended gross margin even without execution problems; if it also compresses EBITDA margin (not just gross margin) that is the real signal | EBITDA margin falling below 18-19% sustained across two+ quarters |
| Balance sheet | Working capital stretch — trade receivables turnover collapsed 9.28x→3.07x in FY25 even as revenue grew; inventory also rose sharply in FY26 (Rs 350.8 Mn→Rs 1,031.8 Mn, Inv. Pres. slide 37) | Trade receivables turnover (Debtors turnover) falling further, or DSO crossing 120+ days |
| Execution | New debt-funded capex (Rs 548.2 Mn long-term borrowings first drawn in FY26) for greenfield Vadodara and ICS integration — execution/absorption risk on newly commissioned lines | Interest coverage ratio declining from its current extreme (135.72x FY25) as debt service grows faster than EBIT; PP&E additions outpacing revenue growth for more than one year |
| Structural | Heavy reliance on continuing policy tailwinds (PLI, China+1, FTA) and on newly entered verticals (Telecom went from 0% to 22.3% of FY26 standalone revenue in one year) that have no multi-year track record yet | Order book growth decelerating sharply quarter-on-quarter, or a newly entered vertical's revenue share reversing |
| (memo) Governance/related-party | Material related-party balances with "Aimtron Corporation, USA" (a company under common management, not a subsidiary) — debit balance of Rs 2,152.54 lakh at FY25-end vs Rs nil at FY24-end (AR Consolidated Notes, Note 34) | Related-party balances growing disproportionately to arm's-length trade balances; watch AGM resolution on material RPT approval with Aimtron Corporation, USA |

### 4B. Valuation method applicability (handoff to Role 1 valuation stage)

| Method | Applicable? | Rationale |
|---|---|---|
| EV/EBITDA | **PRIMARY** | Normalises for the FY26 debt introduction (new long-term borrowings), capex-heavy expansion phase, and volatile "Other Income"/effective tax rate swings that distort P/E; EBITDA margin (20-25% historically) is the cleanest read on underlying operating profitability across the PCBA/Box-Build mix shift |
| P/E relative to growth (PEG) | **SECONDARY** | EPS is the headline metric management and the market track (EPS grew from Rs 9.06 FY24 to Rs 22.47 FY26, consolidated); useful cross-check once Section 1B v3.3's exit-multiple framework is applied at the valuation stage — this stage does not set an exit PE |
| EV/Sales | **TERTIARY** | Useful only during the current capacity-ramp phase (new Vadodara lines, ICS integration) when EBITDA margin is still normalising and understates steady-state earnings power |
| DCF | Not applicable now | Short listed history (IPO June 2024), a stated 40-50% CAGR target with no independent track record yet, and a business still inflecting its capacity/mix — terminal-value assumptions would dominate and be unreliable |
| Dividend Discount Model | Not applicable | Company pays no dividend by design (100% reinvestment) |
| Asset-based / NAV | Not applicable | Not an asset-heavy or financial company; book value materially understates the design/engineering capability driving future orders |
| Sum-of-the-parts | Not applicable today | US subsidiary (Aimtron Electronics LLC/Aimtron International Controls) disclosure is too thin (partial-period data only, Feb-Mar 2026) to separate India-standalone from US-subsidiary economics robustly — revisit as ICS discloses a full year |

Cycle stage that matters for valuation: **early-stage capacity build-out within a policy-subsidised, early-cycle domestic ESDM industry** — valuation should weight forward order-book visibility and utilisation ramp economics more heavily than trailing reported margins, which are currently mix-distorted.

### 4C. Quarterly monitoring checklist (10-15 items)

1. Order book value and book-to-bill ratio (Inv. Pres. quarterly slide)
2. RFQ pipeline value and conversion rate to firm orders
3. Segment mix — PCBA vs Box Build vs ODM % of revenue (watch for further swings)
4. Industry-vertical mix — especially Telecom's sustainability at ~22% after a zero-base entry
5. EBITDA margin (consolidated), and whether it is stable/rising as Box-Build mix normalises
6. Trade receivables turnover / DSO — is it recovering from 3.07x or deteriorating further
7. Inventory turnover / days — watch for component-obsolescence buildup
8. Long-term borrowings level and interest coverage ratio (post first-time debt draw in FY26)
9. Capex vs plan (Vadodara greenfield SMT-line commissioning schedule)
10. ICS/AIC utilisation rate progress against the 54%→90% three-year guided ramp
11. Related-party balances with Aimtron Corporation, USA and other common-management entities
12. Employee cost growth rate vs revenue growth rate
13. Geography mix — India vs USA/North America/Europe share (jumped to 74.3% India in FY26 from 58.3% in FY25)
14. New certification milestones (AS9100D completion, RDSO approval, PLI/ECMS SFP approval)
15. Any customer-concentration disclosure appearing for the first time (would materially improve diligence quality)

### 4D. Highest-value questions for management

1. What is customer concentration (top-5/top-10 as % of revenue), and how much of FY26's 89% revenue growth came from repeat vs brand-new customers? *Reassures:* diversified, no single customer above ~15%. *Worries:* one or two customers/programs driving the bulk of growth.
2. Trade receivables turnover fell from 9.28x to 3.07x even as revenue grew — is this a timing artefact of large year-end shipments/milestone billing, or a sign of extended credit terms used to win large orders? *Reassures:* timing-driven, already normalising in FY26 quarters. *Worries:* structurally looser credit terms, rising bad-debt risk.
3. With Box-Build share rising from ~27% to ~69% of standalone revenue in a single year, do the underlying contracts carry cost-pass-through/escalation clauses on components, or is pricing fixed? *Reassures:* cost pass-through protects margin. *Worries:* fixed pricing leaves EBITDA margin exposed to component-cost inflation.
4. What is the committed order book supporting the new greenfield Vadodara facility (6 SMT lines) relative to its planned capacity, and what is the expected utilisation timeline? *Reassures:* firm orders already match new capacity. *Worries:* capacity being built ahead of demand, execution/absorption risk.
5. Is the ICS acquisition's "EPS accretive from Year 1" claim net of integration costs and the guided ~Rs 10-12 crore incremental investment, and how does actual utilisation today compare with the 54%→90% three-year ramp plan? *Reassures:* on or ahead of plan. *Worries:* accretion driven by one-time items, integration behind schedule.
6. What is the commercial nature of the related-party balances with Aimtron Corporation, USA (a common-management, non-subsidiary entity), and are these arm's-length, board-approved transactions? *Reassures:* transparent distribution/agency relationship with proper RPT approval. *Worries:* an opaque related-party channel used to route revenue or receivables.
7. Given the stated 40-50% CAGR target over 3-5 years, what is the funding plan (further debt, further equity/warrant conversion, or internal accruals) for the capex and working capital this growth requires? *Reassures:* funded from IPO/warrant proceeds and improving internal cash generation with minimal further dilution. *Worries:* recurring equity or debt raises needed because working-capital-heavy growth consumes cash faster than it is generated.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

| | |
|---|---|
| **Company** | Aimtron Electronics Ltd (AIMTRON), NSE Emerge, IPO June 2024 |
| **Business type** | Contract electronics manufacturing (EMS/ODM), with a small, fast-growing design-services component |
| **One-line description** | Turns customer PCB designs or product concepts into tested, delivered circuit boards or boxed electronic systems for industrial, medical, defence, auto, telecom and IoT OEMs |
| **Revenue streams (FY25 standalone → FY26 standalone)** | PCBA 69.3%→28.6%; Box Build 27.2%→68.8%; ODM/End-to-End 3.5%→2.6% (AR p.76-77; Inv. Pres. slide 33) |
| **Geography mix (FY25→FY26 standalone)** | India 58.3%→74.3%; USA/North America ~37.7%→19.0%; Spain 4.0%→3.3%; new: Australia 1.6% (AR p.76-77; Inv. Pres. slide 33) |
| **Asset intensity** | Medium — net PP&E ~19-24% of revenue, rising with capacity expansion |
| **WC intensity** | High and rising — receivables turnover fell 9.28x→3.07x in FY25 |
| **Pricing power** | Moderate — real power confined to regulated/certified niches; commodity PCBA is competitive |
| **Cyclicality** | Cyclical end-markets (auto/industrial/power capex cycles) currently overridden by secular policy tailwinds (PLI, China+1, FTAs) |
| **Key moats** | Certification/regulatory stack (ISO 13485, IATF 16949, AS9100D pending, CDSCO, RDSO pending) and switching costs in qualified programs; weak brand/cost-advantage moats |
| **FY22-FY26 revenue (consolidated/standalone as noted, Rs Mn)** | 263.2 → 835.1 → 929.8 → 1,591.8 (restated, consol.) / 1,583.1 (AR, standalone) → 3,011.6 (consol.) |
| **FY22-FY26 EBITDA margin** | (2.3)% → 26.2% → 25.4% → 21.3-21.5% → 21.8% |
| **FY22-FY26 EPS (Rs)** | (5.16) → 8.25 → 9.06 → 13.14-13.19 → 22.47 |
| **Order book (FY26 close)** | Rs 5,212 Mn, ~1.7x FY26 revenue, +175.8% YoY |
| **Debt-Equity** | 0.00 (FY25) → new Rs 548.2 Mn long-term borrowings drawn (FY26) |
| **Primary valuation method** | EV/EBITDA |
| **Secondary valuation method** | P/E relative to growth (PEG); exit multiple per Section 1B v3.3 to be applied at valuation stage, not here |
| **Biggest single flag** | Trade receivables/working-capital stretch coinciding with a full inversion of the PCBA/Box-Build revenue mix in one year — cash-conversion quality needs independent confirmation before this can clear PROCEED without caveats |

---

## Input gaps (carried and stage-specific)

- Credit rating: absent (no rating agency data provided to this stage).
- Both the Annual Report and Investor Presentation PDFs exceeded the image-render size limit for this run; both were read from pre-extracted plain text. Image-only charts/infographics inside the Investor Presentation (in particular any figures embedded purely as pie-chart images without accompanying text labels) may be under-read — all revenue-mix percentages used here were confirmed present in the extracted text and anchored; any percentage not found in text was marked NOT FOUND rather than estimated.
- Customer concentration (top-5/top-10 customer % of revenue): NOT FOUND in either document.
- Named competitor benchmarking / market share: NOT FOUND in either document.
- FY26 figures are company-disclosed (Investor Presentation) but not yet confirmed against an audited FY26 Annual Report, which does not exist as of this run date; FY25 AR figures are the audited anchor per the operator's data caution on screener.in's FY26 P&L.
