# STAGE 4: BUSINESS MODEL DECODER. Supreme Power Equipment Ltd (SUPREMEPWR)

Run date 2026-10-06. Stage B04-bizmodel. Sonnet 5.5.

Units: AR statements and Notes are in Rs Lakhs. AR MD&A, presentations, press release and screener are in Rs Crore. This report uses Rs Cr unless a line says "lakh". 100 lakh = 1 Cr.

Anchor key: (AR p.N) is the page marker in Annual_Report_FY2025-26.txt. (MD&A p.N) is the same marker. (Pres-Q1 s.N) is the slide number printed on the Q1 FY27 presentation. (Pres-H2 s.N) is the H2 FY26 presentation. (Call-Aug L.N) and (Call-Jun L.N) are transcript line numbers, used only where the AR and presentation are silent. B02 and B03 are prior stage blocks. "DERIVED" means I computed it from anchored inputs. "[INFERENCE]" means reasoning, not a filed fact. "(operator)" is unanchored operator context.

Input status: AR present. Investor presentations (H2 FY26 and Q1 FY27) present. Input gaps carried from B00 are in the YAML. Two gaps bite this stage: the FY26 product-wise revenue chart (Pres-Q1 s.35, Pres-H2 s.36) has no machine-readable label order, and no peer financials were in my assigned inputs.

Archetype ruling (CLAUDE.md library). The best fit is ORDER-BOOK BUSINESS (EPC/capital goods), with BUILD-TO-SPEC COMPONENT MAKER as the secondary lens for the distribution line.

| Test | Order-book business | Build-to-spec component maker | Evidence |
|---|---|---|---|
| Revenue is booked as a signed order, then delivered over months | Yes | Partly | Order book Rs 590.06 Cr = 3.25x FY26 revenue (Pres-Q1 s.4; DERIVED); execution 7 to 17 months (Pres-Q1 s.4) |
| Each unit custom designed to the buyer's spec | Yes | Yes | "Products are custom-designed as per customer technical specifications" (Pres-Q1 s.14) |
| Key drivers are inflow, book-to-bill, execution pace, WC, margin on backlog | Yes | Weak | AR p.13 and Pres-Q1 s.14 name order inflow and execution as revenue drivers |
| Customer capex cycle with design-win pipeline | Utility and EPC tenders | Fits the distribution line only | Tender and EPC route (Pres-Q1 s.14); empanelments TANGEDCO, KSEB, KPTCL, TNPDCL (AR p.8) |
| Input cost pass-through | Yes, by clause | Yes | Price variation clause on 80 to 85% of book (Call-Aug L.351, L.413) |
| Not a commodity converter | Right | Right | Output price is set per order, not by a traded spread; the converter archetype (Amendment 17) does not fit. Stage 11 owns the final classification. |

Archetype metrics to watch therefore: order inflow, book-to-bill, execution pace, working capital, margin on backlog. These drive Sections 3 and 4.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A One line

Supreme Power designs and builds custom transformers (the large metal boxes that step electricity voltage up or down at power plants, substations and solar and wind farms), sells them to state utilities, EPC contractors and industrial buyers against signed orders, and has just opened a second plant to move from small distribution units to 200 MVA / 220 kV power transformers (AR p.4, p.9; Pres-Q1 s.9).

### 1B Money flow chain per revenue stream

| Stream | Input | What the company does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| 1. Distribution and energy-efficient transformers (Thirumazhisai, up to 25 MVA / 132 kV; also Danya Electric) | CRGO steel, copper, transformer oil, tanks (AR p.18; MD&A p.17) | Wins tenders and rate contracts, designs to utility spec, winds coils, assembles core and coil, tanks, tests (AR p.9) | Distribution transformers for last-mile networks; 9,750+ energy-efficient units supplied (AR p.7) | State utilities (TANGEDCO, TNPDCL, KSEB), via the group firm Danya for TNPDC orders (Pres-H2 s.25) | Utility payment cycles, "extended" per MD&A p.17; milestone terms NOT FOUND |
| 2. Power transformers (EPC and utility orders; 72% to 76% of order book) | Same inputs, larger volumes, longer material cycle (MD&A p.18) | Builds 20 MVA to 160 MVA units; the 200 MVA / 220 kV class sits at Kannur (AR p.9) | Power transformers for substations and evacuation | EPC contractors (Karnataka, Telangana, Maharashtra), utilities, private developers (Pres-Q1 s.4) | Advance and milestone terms NOT FOUND in assigned inputs; customer advances rose Rs 14.46 Cr in FY26 (B02 finding 2, lakh converted) |
| 3. Inverter duty, solar and windmill transformers (5% to 8% of book) | Same | Standard-spec units for renewable projects | Transformers for solar and wind sites (Siemens Gamesa, Vestas projects named, Pres-Q1 s.24) | Renewable developers, one unnamed Navratna PSE (Rs 60.90 Cr, AR p.6) | NOT FOUND |
| 4. Repair, erection, commissioning, testing services | Labour and spares | Services on installed units (AR standalone auditor KAM on revenue recognition; Pres-Q1 s.14 "Transformer Servicing Facility") | Service | Same buyers | NOT FOUND |
| 5. Transformer tanks and accessories | Steel plate | Fabricates tanks, used in-house and offered (AR p.7) | Tanks | In-house, others NOT FOUND | NOT FOUND |

Danya Electric (a 90% profit-share partnership, B02 finding 1) manufactures and executes orders and trades with SPEL in a loop: 61.3% of its turnover is sold to SPEL (B02).

### 1C Revenue model classification

| Stream | Type (standard taxonomy) | Description | % of revenue, anchored | Predictability |
|---|---|---|---|---|
| Transformer sales (all products) | Project/order-based, one-time sale | Revenue booked on delivery of each unit under a purchase order or rate contract (AR KAM, revenue recognition; AS 9) | Standalone sale of goods Rs 189.29 Cr of Rs 190.08 Cr = 99.6% (AR Note 20, lakh 18,928.97 of 19,007.73; DERIVED) | M: 3.25x book cover, but guidance cut three times in FY26 (B03 guidance table) |
| Services (repair, erection, testing) | Project-based service | Revenue as service rendered | Standalone Rs 0.79 Cr = 0.4% FY26, down from 5.2% in FY25 (AR Note 20: 78.75 and 754.90 lakh; DERIVED) | L |
| By product within sales | Product mix | Power vs distribution vs inverter duty vs other | FY26 revenue split NOT FOUND: the Pres-Q1 s.35 chart has ten percentages with no label order in the text layer; I will not guess. Order book split is anchored: power 72% (AR p.18; MD&A p.18), distribution 20%, inverter duty 7 to 8% at 27-May-2026; power about 76%, distribution about 18%, inverter duty 5.25% at 17-Aug (Call-Aug L.203) | Book mix H, revenue mix NOT FOUND |
| By customer type | Government vs non-government | Q1 FY27: Government and utilities Rs 20.66 Cr (40.32%), private Rs 30.58 Cr (59.68%) (Pres-Q1 s.14). FY26 (legend order read from Pres-Q1 s.35): government 67.86%, non-government 32.14%. FY25 65.55%, FY24 79.68%. | Q1 anchored; FY26 split carries the read-order caveat | M |

Flag: the Q1 FY27 customer split sums to Rs 51.24 Cr. Reported consolidated revenue is Rs 48.23 Cr (Pres-Q1 s.6) and standalone Rs 51.06 Cr (Pres-Q1 s.7). The base matches neither (DERIVED, gap 0.18 Cr to standalone). Unreconciled.

Intra-group elimination: consolidated revenue is net of Rs 50.18 Cr "mutual owings" (AR consol Note 20: 5,017.91 lakh). Consolidated revenue of Rs 181.64 Cr is standalone revenue Rs 190.08 Cr (Pres-Q1 s.34) plus Danya's own sales, less trade between the two. Gross trade nets to about Rs 0.98 Cr in B03.

### 1D Simplified business model canvas

| Item | Answer | Anchor |
|---|---|---|
| What they sell | Power, distribution, inverter duty, solar, windmill, generator, converter, isolation transformers, and tanks (nine classes) | AR p.7; MD&A p.19 |
| Who buys | Five groups: state utilities, EPC contractors, renewable developers, industrial manufacturers, PSUs. 880 clients. | AR p.4, p.6; MD&A p.18 |
| Why them | Utility empanelments in Tamil Nadu, Kerala, Karnataka, Andhra Pradesh (Pres-Q1 s.22); claimed zero field failures (AR p.8; unverifiable here); fast delivery for EPC buyers (MD&A p.18) | as cited |
| How delivered | Orders from tenders, EPC and direct industrial buyers; designed to spec; made in-house; supplied and installed at site | Pres-Q1 s.14 |
| Cost structure | Raw material dominates: 74.5% of consolidated revenue in FY26 (135.40 / 181.64; DERIVED from Pres-Q1 s.36). Employees 2.5%, other expenses 4.9%. Standalone raw material 78.4% (149.08 / 190.08). Q1 FY27 consolidated: raw material 68.4% (33.01 / 48.23), employees 4.0% (1.92), other 9.3% (4.49) (Pres-Q1 s.6; DERIVED). The AR P&L also carries changes in inventories of Rs (30.56) Cr consolidated (lakh (3,055.54)); whether the presentation raw-material line is net of that is not stated. | as cited |
| Scarce resource | Qualified design and test capability for the larger classes, plus approved-vendor status with utilities. The AR says capacity alone is not it: "customer confidence must be earned through successful type testing, qualification, first-article approvals" (AR p.14). Type tests held only up to 25 MVA / 110 kV (B03 missing_risks, Board p.39). | AR p.14; B03 |
| Pricing power | Weak. Orders are tender-based; margin is protected by cost pass-through (80 to 85% of book has price variation clauses, Call-Aug L.351), not by premium pricing. CMD says larger power transformers add "1% or 2%" margin that overheads absorb (Call-Aug L.565). | as cited |
| Asset intensity | Medium and rising. Fixed assets Rs 24.67 Cr (FY24) to Rs 119.71 Cr (FY26); fixed asset turnover 1.52x | Pres-Q1 s.33, s.37 |
| WC intensity | High. Inventory Rs 62.10 Cr, receivables Rs 46.85 Cr, payables Rs 62.20 Cr (consolidated FY26). Standalone days: inventory 87.5, receivables 86.8, payables 126.3 (B02; Notes 16, 17, 10). 87.5 + 86.8 - 126.3 = 48.0 days, funded by suppliers and customer advances (DERIVED). | Pres-Q1 s.37; B02 |
| Regulatory moat or burden | Moat: vendor approvals and type-test certificates. Burden: BEE star labelling for distribution transformers from 1-Jan-2025 (MD&A p.18); Section 185 timing issue on the Danya guarantee (B03). | MD&A p.18; B03 |

Two plants. Unit 1, Thirumazhisai, about 2,500 MVA, up to 25 MVA / 132 kV, 17,876 sq m. Unit 2, Kannur, 6,000 to 6,500 MVA, up to 200 MVA / 220 kV, about Rs 100 Cr, commercial from Feb-2026 (Pres-Q1 s.20). Danya Electric is a third production source with a Rs 88.13 Cr order book at 13-Aug-2026 (Pres-Q1 s.25).

Utilisation: four readings do not agree. This is load-bearing fact 4.

| Reading | Number | Source | Note |
|---|---|---|---|
| AR key facts | 1,750 MVA actual of 9,000 MVA, "45 to 50%" | AR p.4 | 1,750 / 9,000 = 19.4% (DERIVED, B03). The 45 to 50% does not follow from the two numbers printed beside it. |
| Presentation, Unit 1 | 70 to 80% | Pres-Q1 s.20 | 1,750 / 2,500 = 70.0% (DERIVED). The 1,750 MVA actual matches Unit 1 alone. |
| CMD, Aug call | Unit 1 "utilised fully"; Unit 2 25 to 30% for FY27; earlier in the same call 20 to 25% "as of now" | Call-Aug L.391, L.225 | Operator context also gives 20 to 25% now and 30 to 50% by Q4 FY27 (operator). |
| Time-weighted hypothesis | 2,500 + 6,500 x 2/12 = about 3,580 MVA of capacity in FY26; 1,750 / 3,580 = about 49% | DERIVED | [INFERENCE] The "45 to 50%" may be a time-weighted figure with Kannur counted for about two months. Nothing filed says so. |

Reading for this stage: the 1,750 MVA of FY26 output came almost wholly from Unit 1, so FY26 revenue is a Unit 1 result. Kannur is unproven in revenue terms. The one observation that settles it: Kannur MVA produced and delivered in Q2 FY27, with the basis stated. Q1 FY27 Kannur output is NOT FOUND.

Second-order point [INFERENCE]: if Kannur truly ran at 20 to 25% of 6,500 MVA, that is 1,300 to 1,625 MVA a year, nearly all of FY26 output (1,750 MVA). Q1 FY27 standalone revenue annualises to about Rs 204 Cr, only 7% above FY26 Rs 190.08 Cr (51.06 x 4; DERIVED). Both can hold only if Kannur MVA is mostly work in progress (inventory +102% in FY26, B02) or if rupees per MVA fall sharply on large units. Check inventory and WIP, not revenue, to see Kannur.

### 1E The chai-stall-uncle version

Supreme Power is a made-to-order tailor for electricity. A buyer gives a drawing and a deposit. The firm buys copper and special steel, winds the coils, builds the box, tests it, and delivers months later. Most buyers are state power companies and contractors, and they pay slowly, so the firm leans on its own suppliers to keep cash flowing. The firm just rented a much bigger workshop that can stitch the large, expensive suits. Suppliers and deposits paid for most of it, and the big suits still need approval tests. Order books are full, but the new shop is barely a quarter used, and its rent (depreciation and interest) has already started.

### Section 1 summary table

| Item | Answer |
|---|---|
| Business type | Manufacturing, order-book (made to customer spec) |
| Revenue nature | Project/order-based, one-time sale on delivery; 99.6% goods (AR Note 20) |
| Asset intensity | Medium, rising (fixed assets 24.67 to 119.71 Cr in two years) |
| WC intensity | High, supplier and advance funded |
| Pricing power | Weak; margin held by cost pass-through, not price |

---

## SECTION 2: INDUSTRY DYNAMICS AND COMPETITIVE POSITION

### 2A Five forces

| Force | Plain answer | Helps / hurts / neutral | Anchor |
|---|---|---|---|
| Competition count | Distribution: a "long tail of regional manufacturers". 220 kV and above: a "small group" of multinational and large domestic firms. Competitor count NOT FOUND. CMD says players at 220 kV are "less" (Call-Aug L.401). The AR says competition in the higher-rating segment "is strong" from makers with longer histories (AR p.14). The presentation says "lower competitive intensity" (Pres-Q1 s.21). The company's own documents disagree. | Hurts today; may help after qualification | MD&A p.18; AR p.14; Pres-Q1 s.21 |
| Entry barriers | The barrier is qualification, not capital: vendor approvals, type tests at accredited labs, a field record, "typically take years" (MD&A p.18). Kannur cost about Rs 100 Cr, so capital is a modest barrier. | Helps incumbents; SPEL is not type-tested above 25 MVA / 110 kV (B03) | MD&A p.18; B03 |
| Supplier power | CRGO steel is mostly imported; domestic output meets only 10 to 12% of demand; copper and oil are price-volatile (MD&A p.18). About 80 to 85% of the book has price variation clauses (Call-Aug L.351, L.413); the AR notes forward booking. | Hurts on availability and timing; neutral on price while clauses hold | MD&A p.18, p.20 |
| Customer power and concentration | Utilities buy by tender and pay late. Private and EPC buyers were 59.68% of Q1 FY27 revenue (Pres-Q1 s.14). Top-10 customers: 31.73% in FY26 on the chart as read (Pres-Q1 s.35). 880 clients (AR p.4). Q1 order wins: 10 orders, Rs 195.64 Cr, 8 of 10 from Hyderabad and Karnataka firms (Pres-Q1 s.4). | Hurts on price and payment; helped by dispersion | as cited |
| Substitutes | None for the product. Efficiency rules (BEE star labels) change the spec, not the need. | Neutral | MD&A p.18 |

### 2B Competitive positioning map

Named competitors in the AR and presentations: NOT FOUND. The documents say "established multinational and large domestic manufacturers" without names (AR p.14; MD&A p.18). The presentation SWOT admits "smaller scale compared to larger established transformer players" (Pres-Q1 s.39). Peers named in the corpus (not in my assigned inputs, no numbers taken): Shilchar Technologies, Danish Power, and Indotech Transformers (B00 corpus; the whole-time director began at Indotech, Pres-Q1 s.12). A numeric positioning map needs the peer transcripts and Data_Sheets; stage 5 and stage 11 own it.

| Dimension | SPEL position | Anchor |
|---|---|---|
| Voltage class | Type-tested up to 25 MVA / 110 kV; 220 kV plant built, qualification pending | AR p.9; B03 |
| Scale | Rs 181.64 Cr consolidated revenue; "smaller scale" | Pres-Q1 s.36, s.39 |
| Geography | Tamil Nadu, Kerala, Karnataka, Andhra Pradesh empanelled; first Maharashtra order in Q1 FY27 | Pres-Q1 s.4, s.22 |
| Customer mix | Moving from government (about 68% FY26) to private (59.68% in Q1 FY27) | Pres-Q1 s.14, s.35 |
| Balance sheet | CRISIL BBB/Stable. Short-term rating A3+ in the AR (p.6), A3 in the Q1 deck (s.10); unreconciled | AR p.6; Pres-Q1 s.10 |

### 2C Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | No | No brand pricing: tender-led; no premium evidenced | None |
| Switching costs | Weak | Utility empanelment and repeat EPC orders (Pres-Q1 s.26); a transformer is bought once per project, so repeat comes through relationship | Low to medium; regional |
| Network effects | No | n/a | None |
| Cost advantage (scale or process) | Weak, unproven | In-house integration "cost efficiency" (Pres-Q1 s.19) is a claim; consolidated gross margin FY26 25.5% (DERIVED), standalone 21.6% (DERIVED) | Low |
| Intangibles: type-test certificates and design validation | Partial, not yet at 220 kV | Type tests up to 25 MVA / 110 kV (B03); two 165 MVA units ordered by KPTCL (Call-Aug L.395), type test pending | Medium once obtained; zero today at 220 kV |
| Regulatory / licence | Yes, regional | Vendor approvals: TANGEDCO, KSEB, KPTCL, TNPDCL, AP (AR p.8; Pres-Q1 s.22) | Medium; each approval is state-specific and reviewable |
| Efficient scale | Weak | 9,000 MVA claimed; revenue potential Rs 500 to 550 Cr (Pres-Q1 s.21); 20 MVA is the modal order size in Q1 wins (Pres-Q1 s.4, 8 of 10) | Low |
| Customer relationships / distribution | Weak to medium | 880 clients, 20,800+ units supplied, 35+ sectors (AR p.4); Danya is a captive execution arm | Medium for utilities; low for EPC (price-led) |

Moats present: regional utility approvals (medium), type-test and design-validation record up to 25 MVA (medium, regional), captive partner capacity via Danya (low, governance-flagged). Net: a narrow, qualification-based moat that the 220 kV business has not yet earned.

### 2D Industry lifecycle and position

Indian transformer industry: growth phase, fragmented. Market about USD 3.25 bn in 2026 to USD 4.82 bn by 2031 at about 8.2% CAGR, distribution about 59% (MD&A p.18, citing Mordor; third-party estimate). The presentation says 8 to 10% CAGR (Pres-Q1 s.30). Drivers are an Rs 9.15 lakh Cr transmission plan to 2032 and about 43 GW of renewable additions in FY26 (MD&A p.17, p.18).

SPEL position: a regional distribution and small power transformer maker (consolidated revenue CAGR FY24 to FY26 26.5%, DERIVED from 113.46 and 181.64) attempting a one-step move into the EHV tier. Company growth ran ahead of the market CAGR. The market is not the constraint; qualification and execution are (AR p.14).

### 2E Key industry drivers

| Driver | Direction | Impact on SPEL | Anchor |
|---|---|---|---|
| Transmission build-out (Rs 9.15 lakh Cr to 2032) | Up | Positive, but reachable only after 220 kV qualification | MD&A p.17 |
| Renewable additions and evacuation | Up | Positive for inverter duty and step-up units | MD&A p.17 |
| Distribution reforms (RDSS) | Steady; scheme period ended FY26 | Positive base load; follow-on scheme NOT FOUND | MD&A p.18 |
| Data centre power | Up, no order yet | Zero today: "FY27 we will not get" (Call-Aug L.398); type certificate needed | Call-Aug |
| CRGO and copper prices | Volatile | Margin neutral while pass-through holds on 80 to 85% | MD&A p.18; Call-Aug |
| Utility payment cycle | Slow | Negative for WC | MD&A p.18 |
| Power capex cycle | Uneven year to year | Negative lumpiness risk (Pres-Q1 s.28 names it) | MD&A p.18 |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A Ignore these, track these

| Common ratio | Verdict | Why, for SPEL |
|---|---|---|
| Spot ROCE and ROE (FY26: ROCE 18.76% vs 27.60% FY24; ROE 17.49%, Pres-Q1 s.38) | MISLEADING now | Rs 100 Cr of Kannur sits in capital employed and earns almost nothing yet. A falling ROCE here mostly measures the build, not the old plant. Track the Kannur ramp until Kannur is loaded. |
| Debt to equity (0.42x) | MISLEADING | Payables Rs 62.20 Cr exceed borrowings Rs 49.98 Cr (Pres-Q1 s.37). Supplier credit is the larger leverage. Use total external funding (borrowings plus payables plus advances), not D/E. |
| Current ratio (1.28x FY26) | MISLEADING | Advances (up Rs 14.46 Cr) and payables (up Rs 24.9 Cr; lakh 2,489.23, B02) inflate current liabilities while inventory inflates assets. |
| Debtors turnover (3.95x, "94 days") | MISLEADING | Year-end loading: Q4 balance jumped 33.5% and over-one-year receivables rose to 588.04 lakh with nil provision (B02 finding 9). The AR headline 94 days and the Note 17 figure 86.8 days use different bases. |
| Headline consolidated EBITDA margin (18.1%) | MISLEADING | Consolidated 18.1% against standalone 15.1% is mostly a denominator effect from removing Rs 50.18 Cr of pass-through trade (B03 analyst note; check below). |
| Fixed asset turnover (1.52x) | IRRELEVANT for now | Capacity just commissioned; the denominator jumped in Feb-2026. |
| Reported "capacity utilisation %" | MISLEADING | Four readings exist (1D). Use MVA produced and delivered with a stated basis. |
| Quarterly YoY revenue growth | Weak | Delivery-timed, lumpy. Use order inflow and book-to-bill, over trailing four quarters. |
| Trailing P/E | Misleading as the sole read | Earnings carry depreciation and interest that are still stepping up; use forward earnings with the D+I run-rate. |
| Dividend yield | IRRELEVANT | Capex phase; no payout evidence in assigned inputs. |
| Spot-year ROCE and rupee WC trends into Section 1B or FTTCP | Do not use | Rupee WC trends mislead as scale doubles; use days. Amendment 17 binds converters; this stage does not class SPEL as a converter. |

Check on the margin gap: standalone operating EBITDA ex other income = 30.99 - 2.34 = 28.65 Cr = 15.1% of 190.08. Consolidated = 33.29 - 0.46 = 32.83 Cr = 18.1% of 181.64 (Pres-Q1 s.34, s.36; DERIVED). Consolidated EBITDA exceeds standalone by Rs 4.18 Cr, Danya's contribution, on Rs 8.44 Cr lower revenue.

### 3B Must-track metrics

Healthy ranges for the industry are NOT FOUND in the assigned documents. Thresholds below are company-specific (from this company's history and guidance) and say so.

**Growth**

| Metric | What it tells | Healthy range | Where | Red flag |
|---|---|---|---|---|
| Order inflow and book-to-bill | Whether the book refills as it burns | Inflow at least 1.0x quarterly revenue; FY26 inflow Rs 437+ Cr vs consolidated revenue Rs 181.64 Cr = 2.4x (DERIVED) | Reg 30 order filings, presentation | Book under 2.0x trailing revenue; Q1 FY27 195.64 / 48.23 = 4.1x fading toward 1x |
| Order book and conversion | Visibility | Rs 377 Cr due before March 2027 (Call-Aug L.239) vs guide 250 to 300 Cr | Presentation, call | Revenue under Rs 55 Cr in Q2 (B03 floor for the 250 guide) |
| Kannur MVA produced and delivered | Is the new plant real | Basis disclosed; rising each quarter | Call, presentation | Still 20 to 25% by Q3, or no MVA disclosed |
| Power-transformer share of revenue | Mix shift | Rising toward the 72 to 76% of book | Presentation | Revenue stays distribution-led while the book says power |

**Profitability and efficiency**

| Metric | What it tells | Healthy | Where | Red flag |
|---|---|---|---|---|
| Gross margin (revenue less raw material) | Pass-through working | Consolidated 25.5% FY26; Q1 FY27 31.6% (DERIVED; an analyst quotes 28.82%, basis unreconciled, Call-Aug L.172) | Quarterly results | Below 24% with price variation claimed |
| EBITDA margin, standalone and consolidated | Operating leverage | Guide 15 to 18% (MD&A p.19) vs CMD 18 to 20% (Call-Aug L.189) | Results | Below 15% consolidated |
| Share of EBITDA gain absorbed by D+I | Does revenue reach PAT | At most 50% (B03 monitorable). Q1 FY27: D+I rose 1.52 Cr vs EBITDA rose 2.16 Cr = 70.4% (DERIVED; B03 quotes 69.7%, basis differs) | Results | Above 70% for a second quarter |
| Incremental EBITDA and PBT margin | The physics (3D) | Incremental EBITDA at or above 18% | Results | Q1 FY27 incremental PBT 4.9% (DERIVED) |

**Balance sheet and risk**

| Metric | What it tells | Healthy | Where | Red flag |
|---|---|---|---|---|
| CFO vs capex and FCF | Self-funding | CFO at least 100% of PAT | Cash flow | FY26 CFO 25.90 vs capex about 57 (Pres-Q1 s.37); FCF negative two years |
| Payable days, advance balance | Float that can reverse | Payables 59.54 Cr, advances 17.10 Cr standalone (B03) | Balance sheet | Advances under 10 Cr with payables above 59 Cr |
| Inventory days and WIP | Unbilled Kannur build | Consolidated 124.8 days FY26 (B02) | Notes | Above 125 days without matching dispatch |
| Danya trade with SPEL; guarantee | Related-party loop | Gross trade at most Rs 50.2 Cr; guarantee Rs 14.70 Cr | RPT disclosure | Guarantee moving toward the Rs 25 Cr authority |
| Receivables over one year | Collection tail | At most Rs 5.88 Cr standalone | Note 17 | Provision introduced |

### 3C Non-financial KPIs

| KPI | Where to find |
|---|---|
| Order book (Rs Cr, by product, government vs private, Danya share) | Presentation, call |
| Order cover vs next 12-month revenue | DERIVED from presentation and call |
| MVA produced, MVA delivered, by plant | Not disclosed by plant; ask on call (AR p.4 gives one total) |
| Type-test and design-validation certificates by rating | Reg 30 filings, call |
| Vendor approvals (new state utilities) | AR p.8; Pres-Q1 s.22 |
| Percent of book with price variation clause | Call (80 to 85%, Call-Aug L.351) |
| Delivery performance and liquidated damages | Notes; call |
| Skilled headcount at Kannur | Three figures: 112 staff (B03, Board report), team size 250 (Pres-Q1 s.10), 250 to 300 deployed (Call-Aug L.566). Unreconciled. |
| Field-failure and rejection record | AR p.8 (claim; unverifiable) |

### 3D Unit economics

Unit: one MVA of transformer shipped. (A transformer is the physical unit, but MVA is the capacity unit management reports and the right base for Kannur.) Standalone FY26: revenue Rs 190.08 Cr; MVA produced 1,750 (AR p.4).

| Item | Value | Basis |
|---|---|---|
| Revenue per MVA | about Rs 10.9 lakh | 190.08 Cr / 1,750 MVA (DERIVED). Caveat: standalone revenue includes goods bought from Danya, whose output may not be in the 1,750 MVA. |
| Raw material per MVA | about Rs 8.5 lakh | 149.08 Cr / 1,750 (DERIVED); 78.4% of revenue |
| Operating EBITDA per MVA | about Rs 1.64 lakh | 28.65 Cr / 1,750 (DERIVED); 15.1% |
| Implied revenue per MVA at the stated potential | about Rs 6.1 lakh | Rs 550 Cr / 9,000 MVA (MD&A p.18; DERIVED) |

Tension: management's own peak revenue (Rs 550 Cr, MD&A p.18) divided by 9,000 MVA is Rs 6.1 lakh per MVA, 44% below FY26's Rs 10.9 lakh. Either large units sell for far less per MVA than distribution units, or the 9,000 MVA is not the revenue-relevant capacity. [INFERENCE] Large transformers carry less rupee value per MVA, so capacity multiples (3.5x) will not map to revenue multiples (550 / 190 = 2.9x, DERIVED). The observation that separates the two readings: revenue and MVA delivered for a Kannur-built unit above 100 MVA. Not available. Note also that 20 MVA, the modal Q1 order size (Pres-Q1 s.4), is below the 25 MVA ceiling Unit 1 already serves.

Volume drivers: orders won, delivery slots, Kannur loading, qualification gates. Price drivers: LME copper and CRGO via price variation clauses; tender L1 pressure; mix. Cost drivers: raw material (about 74% of revenue), then skilled labour, depreciation and interest.

Operating leverage, measured from filed numbers (consolidated, Rs Cr):

| Period | Revenue change | EBITDA change | PBT change | PAT change | Incremental margin |
|---|---|---|---|---|---|
| FY26 vs FY25 | +32.92 | +4.22 | +2.47 | +1.75 | EBITDA 12.8%, PBT 7.5% (DERIVED from Pres-Q1 s.36) |
| Q1 FY27 vs Q1 FY26 | +13.16 | +2.16 | +0.64 | +0.43 | EBITDA 16.4%, PBT 4.9%, PAT 3.3% (DERIVED from Pres-Q1 s.6) |

Operating leverage has been negative to date: costs ran ahead of revenue. In Q1 FY27 employees rose 0.81 to 1.92 (+1.11) and other expenses 1.47 to 4.49 (+3.02). Together (+4.13 Cr) they took 65% of the +6.32 Cr gross profit gain (15.22 vs 8.90; DERIVED, raw material line as presented). That left EBITDA +2.16 Cr. Depreciation (0.17 to 0.80) and finance cost (0.41 to 1.30) rose +1.52 Cr together and took 70% of the EBITDA gain, leaving PBT +0.64 Cr. Depreciation and interest have further to go: B03 estimates a run-rate depreciation near Rs 1.26 Cr per quarter against 0.80 in Q1. Operating leverage turns positive only through revenue, not margin: the CMD concedes a 1 to 2% margin gain on large units is absorbed by overheads (Call-Aug L.565). The presentation's "Margin Expansion Ahead" (Pres-Q1 s.8) and "high-margin segment" (Pres-Q1 s.21) are not backed by management's own call answer.

---

## SECTION 4: RISKS, VALUATION APPROACH AND MONITORING

### 4A Business-model-specific risks and the first line item that moves

| Category | Risk | First financial line item to deteriorate |
|---|---|---|
| Revenue model | Guided revenue not delivered. FY26 guided 225, 200, 190, delivered 181.64; Q1 FY27 guided 50 to 60, delivered 48.23; FY27 guide 275 to 300 in the AR, 250 to 300 on the Aug call (load-bearing fact 1; B03 guidance table; Call-Aug L.219) | Quarterly consolidated revenue vs the Rs 55 and 65 Cr Q2 thresholds |
| Revenue model | Book is lumpy: Rs 377 Cr "due before March" against a Rs 250 to 300 Cr guide (Call-Aug L.239) means late customer pull or slipped execution | Order-book roll (opening + inflow - revenue = closing) vs reported book |
| Revenue model | Danya loop: a BB-/A4+ partnership firm sells 61.3% of its turnover to SPEL; Rs 88.13 Cr of the book is Danya's, about 15% (Pres-Q1 s.25; DERIVED) | Gross SPEL-Danya trade; guarantee beyond Rs 14.70 Cr |
| Margin | Fixed-cost step-up: D+I took 70.4% of Q1 EBITDA gain; staff and other expenses up two to three times | Share of EBITDA gain absorbed by D+I; other expenses as % of revenue (9.3% in Q1) |
| Margin | Pass-through fails on the 15 to 20% of book without price variation clauses, or claims are disputed (price variation is recognised only when "reasonable certainty", AR KAM) | Gross margin; unbilled price-variation receivable |
| Balance sheet | Supplier and customer funded WC reverses; no undrawn facilities (B02/B03) | CFO ex advances; standalone advances and payables |
| Balance sheet | Debt service tightens: DSCR 2.44x (company definition) vs 10.47x; ICICI is 97.2% of term debt; covenants NOT FOUND | DSCR; current maturities Rs 10.95 Cr (lakh 1,095.48, B02) |
| Execution | Kannur ramp and 220 kV type test slip; 165 MVA type test pending (Call-Aug L.393). The book is 72 to 76% power transformers that depend on this | Kannur MVA delivered; inventory and WIP days |
| Execution | Skilled people: a "recognised cost pressure" (MD&A p.20); design-experienced NED resigned 13-Aug-2026 (B03) | Employee cost per quarter; resignation filings |
| Structural | Customer-mix shift changes the WC profile: government share 40% in Q1 FY27 vs about 68% FY26 (Pres-Q1 s.14, s.35) | Receivable days by customer type; over-one-year tail |
| Structural | CRGO import dependence (MD&A p.18) | Gross margin spike or inventory write-down |

### 4B Valuation method applicability

The Section 1B destination PE governs the exit multiple. This table selects method; it does not set a multiple.

| Method | Applicable? | Why |
|---|---|---|
| P/E on forward earnings | PRIMARY | Profitable (PAT Rs 20.68 Cr), growing, order-book visible; build earnings from the order book and the D+I run-rate, not trailing PAT |
| EV/EBITDA | SECONDARY cross-check | Debt rose Rs 18.74 to 49.98 Cr; D+I are stepping up, so PAT is a moving base; EBITDA is cleaner. Use standalone and consolidated both because of the 3pp margin gap. |
| P/B with ROE | TERTIARY, floor check | Book Rs 47.30 per share (Pres-Q1 s.33); ROE fell 20.46% to 17.49% on a build year; capital-heavy phase |
| DCF | Not applicable for primary use | FCF negative two years (CFO 25.90 vs capex about 57); terminal assumptions would rest on an unproven Kannur ramp |
| EV/Sales | Not applicable | Margins differ widely by mix and by consolidation; the Rs 50.18 Cr elimination distorts revenue |
| EV per MVA / replacement cost | Not applicable | Rs 100 Cr for 6,000 to 6,500 MVA (Pres-Q1 s.20) is a cost, not a value; no peer per-MVA data in assigned inputs |
| EV/order book | Not applicable | Orders are not equal-margin; sanity check only |
| SOTP | Not applicable | Single reportable segment (MD&A p.19); Danya is a consolidation issue, not a separate business |
| Dividend yield | Not applicable | Capex phase |

Cycle stage that matters for valuation: the power-capex order cycle and the Kannur ramp stage (build year, FY26 to FY27). Value on the FY28 to FY29 earnings the book and ramp support, discounted back, and put the conservatism in position size (v3.10 Amendment 26.3). The earnings basis at entry and at exit must match (Amendment 18).

### 4C Quarterly monitoring checklist (12 items)

| # | Item | Good | Trouble |
|---|---|---|---|
| 1 | Consolidated revenue vs guide | At least Rs 55 Cr in Q2, 65 Cr for the 275 case | Under 55 Cr: the 250 guide needs a second-half hockey stick |
| 2 | Order inflow and book | Book above Rs 550 Cr after revenue burn | Book falling while guide is held |
| 3 | Kannur MVA produced and delivered, basis stated | Disclosed and rising | No number, or 20 to 25% persists into Q3 |
| 4 | Gross margin | 25% or better | Below 24% |
| 5 | D+I share of EBITDA gain | At most 50% | Above 70% |
| 6 | Other expenses % of revenue | Falls from 9.3% | Rises |
| 7 | Employee cost and headcount | Grows slower than revenue | Faster, with no new MVA delivered |
| 8 | Standalone advances and payables | Advances near Rs 17.10 Cr, payables near 59.54 Cr | Advances under 10 Cr with payables above 59 Cr |
| 9 | CFO vs capex; tank plant capex Rs 20 to 22 Cr on a term loan (operator) | CFO above capex ex tank plant | Gap funded by new debt again |
| 10 | Danya gross trade and guarantee | Flat at Rs 50.2 Cr and 14.70 Cr | Rising |
| 11 | Type-test or qualification at 220 kV | Any filing | None by Q4 FY27 |
| 12 | Receivables over one year; provision | At most Rs 5.88 Cr, no new provision | Over Rs 5.88 Cr |

### 4D Questions for management

| # | Question | Answer that reassures | Answer that worries |
|---|---|---|---|
| 1 | Give Kannur MVA produced and delivered in Q1 FY27 and the utilisation basis. Why does the AR say 45 to 50% when 1,750 / 9,000 = 19.4%? | A stated basis, MVA by plant, ties to the AR | "Approximately", or no MVA by plant |
| 2 | FY26 guidance was cut 225, 200, 190 and delivered 181.64. Why is the FY27 range 250 to 300 now, vs 275 to 300 in June? Which Rs 377 Cr is due before March? | Order-by-order delivery dates and customer pull confirmed | No schedule; "customers place orders a year ahead" |
| 3 | Larger power transformers add 1 to 2% margin and overheads absorb it. What is the Kannur EBITDA margin at 50% and 90% utilisation, and why does the deck say "high-margin segment"? | A unit economics table with fixed cost named | Margin stays 15 to 18% at full load |
| 4 | When is the 165 MVA type test, who runs it, and what is the date for 220 kV qualification? | Dated test slot and lab | "Soon"; no lab or date |
| 5 | State the Danya deed terms, the share of its output sold to SPEL, and how transfer prices are set. Is the Rs 88.13 Cr Danya book all TNPDC distribution? | A written pricing benchmark and a plan to cut the loop | No benchmark; guarantee authority used |
| 6 | Customer advances rose Rs 14.46 Cr and payables Rs 24.9 Cr in FY26. How much of each pays for Kannur capex, and when does it unwind? | A schedule, with the unwind covered by warrant money (Rs 15.81 Cr by 27-Feb-2027, B03) | Unwind date unknown |

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
+----------------------------------------------------------------------------------+
| SUPREME POWER EQUIPMENT LTD (SUPREMEPWR), NSE SME. Run date 2026-10-06           |
+----------------------------------------------------------------------------------+
| ARCHETYPE     | Order-book business; build-to-spec lens for the distribution line |
| BUSINESS TYPE | Manufacturing, made to customer spec, delivered over 7-17 months   |
| REVENUE NATURE| Project/order-based; goods 99.6% (AR Note 20)                      |
| ORDER BOOK    | Rs 590.06 Cr (13-Aug-2026), 3.25x FY26 revenue; power ~76%,        |
|               | distribution ~18%, inverter duty ~5%; Danya Rs 88.13 Cr            |
| ASSET INTENS. | Medium, rising: fixed assets Rs 24.67 Cr to 119.71 Cr in two years |
| WC INTENSITY  | High, supplier and customer-advance funded (payable days 126.3)    |
| PRICING POWER | Weak. Tender-led; 80-85% of book has price variation clauses       |
| CYCLICALITY   | Secular-growth demand (Rs 9.15 lakh Cr T&D plan); lumpy order      |
|               | timing and power-capex exposure named by the company               |
| MOATS         | Regional utility approvals (medium); type-test record to 25 MVA    |
|               | (medium); 220 kV moat not yet earned                               |
| PRIMARY VALN  | P/E on forward earnings. Secondary EV/EBITDA. Tertiary P/B-ROE.   |
|               | DCF not used (negative FCF).                                       |
| TOP 5 METRICS | 1 Kannur MVA delivered (basis stated)                              |
|               | 2 Order inflow, book-to-bill, book roll                            |
|               | 3 D+I share of EBITDA gain (at most 50%)                           |
|               | 4 CFO vs capex; advances and payables                              |
|               | 5 Danya gross trade and guarantee                                  |
| UNIT ECON.    | FY26 standalone ~Rs 10.9 lakh revenue/MVA, ~Rs 1.64 lakh op. EBITDA|
|               | /MVA (DERIVED). Stated peak implies Rs 6.1 lakh/MVA.               |
| FACT CHECKS   | Utilisation: 19.4% / 45-50% / 70-80% / 20-25%, unreconciled        |
|               | Q1 FY27: revenue +37%, EBITDA +32%, PBT +10%, PAT +10%             |
+----------------------------------------------------------------------------------+
```

### Closing read on the four load-bearing facts

| # | Fact | What this stage adds |
|---|---|---|
| 1 | Guidance vs delivery | Three FY26 cuts and a Q1 miss, on a business that books revenue on delivery, mean the guide measures execution, not demand. The Rs 377 Cr "due before March" against a Rs 250 to 300 Cr guide (Call-Aug L.239) is unresolved. |
| 2 | Danya loop | Danya is the execution arm for distribution orders. Its Rs 88.13 Cr book is about 83% of the roughly Rs 106 Cr distribution book (18% of 590.06; DERIVED, assumes Danya's book is all distribution). The loop is a business-model fact, not a footnote. [INFERENCE] |
| 3 | CFO 25.90 vs capex 57.48 | The standalone cash cycle of 48 days is financed because payables run 126.3 days. The model needs that float to continue. |
| 4 | Q1 revenue +37% vs PAT +10% | Revenue grew into Unit 1's capacity; Kannur costs (D+I, staff, other expenses) arrived first. Management's own words give no margin lift from larger units. |

---

```yaml
stage: B04-bizmodel
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "COLLECTOR: BSE scrip code not found on the screener page, so announcements/ is empty. This is a collector gap, not evidence that the company files nothing. (Filled by hand from the NSE API: 17 filings Mar-Sep 2026; Oct-2025 to Feb-2026 order intimations not pulled under the operator cap.)"
  - "COLLECTOR: shareholding/ is empty: no source is automated yet. (Filled by hand: NSE SHP XBRL 31-Mar-2026; the Sep-2026 half-year pattern is not yet filed as of 2026-10-06.)"
  - "COLLECTOR: screener export sheets came out EMPTY (formulas with no cached values): screener/INDOTECH/531201/DANISH Profit & Loss, Quarters, Balance Sheet, Cash Flow, Customization. ABSENT documents. Data_Sheet CSVs carry FY23-FY26 raw values and are present."
  - "COLLECTOR: no results PDFs (screener has none). (Filled by hand: Q1 FY27 and FY26 audited results from NSE.)"
  - "COLLECTOR: no rating PDF. (Filled by hand: CRISIL full rationale 20-Mar-2026 as text.)"
  - "HIGH: prospectus/ empty. Company listed Dec-2023, within 3 years of run_date. Not pulled: operator 12-document cap 2026-10-06 (inputs/operator-notes.md). Backward baseline runs on FY23-FY26 AR/screener only; promoter and group map from AR and web."
  - "research/ empty (non-anchored; no effect on evidence)."
  - "Peer INDOTECH: no transcripts on screener; peer-concalls cover SHILCHAR (4) and DANISH (2) only."
  - "No Q2 FY27 business update filed as of 2026-10-06 (NSE announcement list checked through 26-Sep-2026)."
  - "Operator document cap: Q3 FY26 transcript (concalls/Concall_Feb_2026) and the shareholding XBRL are over the 12-document cap, kept because stage 5 requires three transcripts and the UA qualifier needs the SHP; flagged for operator ruling."
  - "Results PDFs carry an OCR-quality text layer (e.g. 'R, Lakhs'); read the page before taking a number."
  - "STAGE 4: investor presentations present. FY26 product-wise revenue mix (Pres-Q1 s.35, Pres-H2 s.36) is a chart with ten percentages and no label order in the text layer; PDF page rendering unavailable (no poppler). Product-wise revenue split is NOT FOUND; only the order-book mix is anchored."
  - "STAGE 4: peer financials and named competitor positioning NOT FOUND in assigned inputs (AR names none)."
flags:
  - {type: FLAG-UTIL, reason: "Four utilisation readings do not agree: AR p.4 45-50% on 1,750 of 9,000 MVA (19.4% derived); presentation Unit 1 70-80% (1,750/2,500 = 70.0%); CMD Unit 1 'fully', Unit 2 20-25% then 25-30%; time-weighted hypothesis about 49% is an inference. FY26 output of 1,750 MVA is Unit 1."}
  - {type: FLAG-MARGIN-NARRATIVE, reason: "Presentation says 'Margin Expansion Ahead' and 'high-margin segment' (Pres-Q1 s.8, s.21); CMD says larger power transformers add 1-2% margin absorbed by overheads (Call-Aug L.565). Q1 FY27 incremental PBT margin 4.9%."}
  - {type: FLAG-GUIDE, reason: "FY26 guide 225>200>190 vs 181.64; Q1 FY27 guide 50-60 vs 48.23; FY27 guide 275-300 (AR) vs 250-300 (Aug call); Rs 377 Cr due before March vs 250-300 guide."}
  - {type: FLAG-DANYA-LOOP, reason: "Danya Rs 88.13 Cr book about 15% of Rs 590.06 Cr; about 83% of the roughly Rs 106 Cr distribution book if Danya's book is all distribution (DERIVED, inference). 61.3% of Danya turnover is SPEL (B02). Model needs this execution arm."}
  - {type: FLAG-CASH, reason: "Carried from B02/B03: CFO 25.90 vs capex about 57 Cr; payables 126.3 days and customer advances fund the 48-day standalone cash cycle."}
  - {type: FLAG-SEGMENT-BASE, reason: "Q1 FY27 customer split sums to Rs 51.24 Cr; reported consolidated revenue 48.23 and standalone 51.06; unreconciled. Headcount also varies: 112 (B03), 250 (Pres-Q1 s.10), 250-300 (Call-Aug)."}
  - {type: FLAG-PRODMIX-NOT-FOUND, reason: "FY26 product-wise revenue split not machine-readable; no estimate made."}
business_type: manufacturing
revenue_streams:
  - {name: "Transformer sales, all products (goods)", type: "project/order-based, one-time sale on delivery", pct_of_revenue: 99.6, predictability: "M"}
  - {name: "Services: repair, erection, commissioning, testing", type: "project-based service", pct_of_revenue: 0.4, predictability: "L"}
  - {name: "Product split (power vs distribution vs inverter duty)", type: "NOT FOUND for revenue; order book power 72-76%, distribution 18-20%, inverter duty 5-8%", pct_of_revenue: 0, predictability: "H for book, NOT FOUND for revenue"}
asset_intensity: medium
wc_intensity: high
pricing_power: weak
cyclicality: "secular-growth demand with lumpy order timing and capex-cycle exposure (Pres-Q1 s.28; MD&A p.18)"
moats_present:
  - "Regional utility vendor approvals TANGEDCO, KSEB, KPTCL, TNPDCL, AP: medium durability, state-specific"
  - "Type-test and design-validation record up to 25 MVA / 110 kV: medium, regional; 220 kV unproven"
  - "Captive execution partner Danya Electric: low, governance-flagged"
valuation_methods:
  primary: {method: "P/E on forward earnings", why: "Profitable and growing with order-book visibility; build earnings from the order book and D+I run-rate, entry and exit on the same earnings basis"}
  secondary: {method: "EV/EBITDA", why: "Debt rose 18.74 to 49.98 Cr and D+I are stepping up; EBITDA is the cleaner cross-check; show standalone and consolidated"}
  tertiary: {method: "P/B with ROE", why: "Floor check on a build year; ROE 20.46% to 17.49%"}
  not_applicable: ["DCF as primary (FCF negative two years)", "EV/Sales (Rs 50.18 Cr elimination distorts)", "EV per MVA / replacement cost (no peer data)", "EV/order book", "SOTP (single segment)", "Dividend yield"]
irrelevant_ratios:
  - "Spot ROCE and ROE: Kannur capital sits in the base before it earns"
  - "Debt to equity 0.42x: payables 62.20 Cr exceed borrowings 49.98 Cr"
  - "Current ratio 1.28x: advances and payables inflate it"
  - "Debtors turnover 3.95x / 94 days: year-end loading, over-one-year tail 588.04 lakh with nil provision"
  - "Consolidated EBITDA margin 18.1% vs standalone 15.1%: denominator effect from Rs 50.18 Cr elimination"
  - "Fixed asset turnover 1.52x: plant commissioned Feb-2026"
  - "Reported utilisation %: four unreconciled readings; use MVA delivered"
  - "Quarterly YoY revenue growth: delivery-timed and lumpy"
must_track_metrics:
  - {metric: "Kannur MVA produced and delivered, with basis", healthy: "Disclosed by plant and rising each quarter", red_flag: "No MVA disclosed, or still 20-25% in Q3 FY27"}
  - {metric: "Order inflow, book-to-bill and book roll", healthy: "Book above Rs 550 Cr after burn; inflow at least 1.0x quarterly revenue", red_flag: "Q2 revenue under Rs 55 Cr or book falling while guide held"}
  - {metric: "D+I share of EBITDA gain", healthy: "At most 50%", red_flag: "70.4% in Q1 FY27; above 70% again"}
  - {metric: "CFO vs capex; standalone advances and payables", healthy: "CFO above capex ex tank plant; advances near 17.10 Cr, payables near 59.54 Cr", red_flag: "Advances under 10 Cr with payables above 59 Cr"}
  - {metric: "Danya gross trade with SPEL and SPEL guarantee", healthy: "Flat at Rs 50.2 Cr and Rs 14.70 Cr", red_flag: "Guarantee moves toward the Rs 25 Cr authority"}
unit_economics:
  unit: "1 MVA of transformer shipped (standalone FY26, 1,750 MVA produced, AR p.4)"
  revenue_per_unit: "about Rs 10.9 lakh (190.08 Cr / 1,750 MVA, DERIVED; stated peak Rs 550 Cr / 9,000 MVA implies Rs 6.1 lakh)"
  margin_per_unit: "about Rs 1.64 lakh operating EBITDA (28.65 Cr / 1,750 MVA, DERIVED), 15.1% standalone; consolidated 18.1%"
  key_lever: "Kannur loading: delivered MVA and gross margin on large units against the fixed D+I, staff and other-expense step-up; CMD says larger units add only 1-2% margin"
first_deterioration_signals:
  - {risk: "Guided revenue not delivered", first_signal: "Q2 FY27 consolidated revenue under Rs 55 Cr"}
  - {risk: "Danya loop and guarantee", first_signal: "Gross SPEL-Danya trade above Rs 50.2 Cr or guarantee above Rs 14.70 Cr"}
  - {risk: "Fixed-cost step-up eats EBITDA gain", first_signal: "D+I share of EBITDA gain above 70%; other expenses above 9.3% of revenue"}
  - {risk: "Pass-through fails on 15-20% of book", first_signal: "Gross margin below 24%"}
  - {risk: "Supplier and advance float reverses", first_signal: "Standalone advances under Rs 10 Cr with payables above Rs 59 Cr"}
  - {risk: "Debt service tightens", first_signal: "DSCR below 2.0x on company definition"}
  - {risk: "Kannur ramp and 220 kV qualification slip", first_signal: "No MVA disclosed by plant; inventory and WIP days above 125; no type-test filing by Q4 FY27"}
  - {risk: "Collection tail", first_signal: "Receivables over one year above Rs 5.88 Cr standalone, or provision introduced"}
mgmt_questions:
  - "Kannur MVA produced and delivered in Q1 FY27 and the utilisation basis; why AR p.4 says 45-50% when 1,750/9,000 = 19.4%"
  - "FY26 guide cut 225>200>190 to 181.64; why FY27 is 250-300 vs 275-300; which Rs 377 Cr is due before March"
  - "Kannur EBITDA margin at 50% and 90% utilisation; why the deck says high-margin segment when larger units add 1-2%"
  - "Date, lab and 220 kV qualification path for the 165 MVA type test"
  - "Danya deed terms, share sold to SPEL, transfer-price benchmark; is the Rs 88.13 Cr Danya book all TNPDC distribution"
  - "How much of the Rs 14.46 Cr advance rise and Rs 24.9 Cr payables rise pays for Kannur capex, and the unwind date"
one_line_verdict: "An order-book transformer maker with a full book and a new plant it has paid for but not loaded, where Q1 shows revenue growing into old capacity while Kannur costs arrive first."
analyst_note: "Three reads a later stage cannot rebuild. (1) FY26 output of 1,750 MVA equals Unit 1 at 70% of 2,500 MVA, matching the presentation's 70-80%. FY26 is a Unit 1 result and Kannur is unproven in revenue; the AR's 45-50% fits only a time-weighted capacity, an inference. If Kannur really ran 20-25%, it would be WIP (inventory +102%), since revenue annualises only 7% above FY26. (2) Management's stated peak (Rs 550 Cr on 9,000 MVA = Rs 6.1 lakh/MVA) is 44% below FY26's Rs 10.9 lakh/MVA, so capacity multiples will not map to revenue multiples. (3) The deck says margin expansion; the CMD says 1-2% extra margin on large units is absorbed by overheads. Danya's Rs 88.13 Cr book is about 83% of the distribution book (derived), so the loop is part of the model. FY26 product revenue split is NOT FOUND."
```
