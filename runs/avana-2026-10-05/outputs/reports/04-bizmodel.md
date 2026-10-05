# AVANA Stage 4: Business Model Decoder
Run date 2026-10-05. Model claude-sonnet-5-5. Company: Avana Electrosystems Ltd. Mode: NO-CONCALL (RECENTLY-LISTED PRIORITY: the RHP is the business-model baseline).

## Conventions
- Unit: INR lakh as printed on the AR and RHP faces (100 lakh = 1 Cr). Not converted; stage 10 converts once. "Derived" = arithmetic on printed figures, inputs shown.
- Anchors: "AR p<N>" and "RHP p<N>" = pdf page marker in the .txt files (RHP printed page = pdf - 5; AR printed = pdf - 11). B03 anchors reused where marked "per B03".
- Investor presentation: NOT PROVIDED (none exists). The RHP "Our Business" (RHP p152-178) and "Industry Overview" (RHP p124-151 region) replace it. The RHP is a December 2025 document; its mix, customer and order-book tables stop at H1 FY26 or 30-Nov-2025. Where FY26 has no filing, the line says NOT FOUND, check concall or presentation (none held).
- [INFERENCE] marks a reasoned link not stated in a document.

## Step 0. Load-bearing facts checked first (LBF2, LBF4)
| LBF | Finding for the business model | Anchor |
|---|---|---|
| LBF2 concentration | Top 5 customers 36.01% (FY23), 22.76% (FY24), 22.42% (FY25), 38.79% (H1 FY26); top 10 47.91%, 37.07%, 31.50%, 52.00% (RHP p169). Customers are anonymised "Customer 1..10" (RHP p171-172). The B2B buyer is mostly a private panel builder or EPC contractor: private players 73.16%, 81.54%, 82.22%, 76.24% of revenue (RHP p38-39, p167). Madhya Pradesh alone was 33.59% of FY25 revenue vs 16.35% in FY24 (RHP p168). FY26 top-5 share, identities and the FY26 customer-type mix: NOT FOUND, check concall or presentation. | RHP p38-39, p167-169, p171-172 |
| LBF4 mix and margin | Panels 57.99% / 48.05% / 48.94% / 60.26% of revenue and relays 42.01% / 51.95% / 51.06% / 39.74% for FY23 / FY24 / FY25 / H1 FY26 (RHP p152). FY26 product-wise revenue and gross margin by product: NOT FOUND. FY26 production: panels 886 (+69% on 523), relays 62,034 (-5.8% on 65,840) (AR p85). FY26 gross margin 40.61% vs 47.80% (B03; AR p100). The mix shift toward panels is the leading candidate for the margin fall, but with no product margin it stays a hypothesis. | RHP p152, p166; AR p85; B03 3C |

Why it matters: the panel line is a one-off, spec-by-spec build sold to EPC contractors at large ticket sizes. The relay line is a repeat, catalogue-style electronic product. The two have different working capital, margin and demand patterns, but the company reports one segment (reply to NSE 23-Jun-2026 item 2, per B00).

---
## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A One-line description
Avana designs and assembles the control rooms' "brains" for electricity substations (control and relay panels) and the protection relays that cut power when a fault occurs, selling them mostly to EPC contractors and panel builders that build substations for state utilities and private power projects (RHP p152-153, p159-161; AR p68).

### 1B Money flow chain, per revenue stream
| Stream | Input | What Avana does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| Control and relay panels (Unit II) | Numerical and electromechanical relays, annunciators, meters, switches, control cables, terminal blocks, MS/SS cubicles (RHP p172) | Takes a customer drawing, designs wiring and bill of materials, has the sheet-metal enclosure fabricated outside, then assembles, wires, tests, runs Factory Acceptance Test and site commissioning (RHP p164) | A custom-built panel for 11 kV to 220 kV (RHP p153); AR p68 says SCADA and automation up to 400 kV | EPC contractors, private panel builders, and (tender route) state utilities | Order-by-order contracts; payment terms NOT FOUND. Receivables 2,221.29 at 96.7 days, 13.8% over 6 months, retention money inside receivables (AR p113; RHP p113 per B03) |
| Numerical and electromechanical relays (Unit I) | Microcontrollers, ICs, diodes, passives, current and power transformers, brass parts, metal boxes (RHP p172) | In-house hardware, PCB and firmware design; assembles cards, calibrates and tests each relay (RHP p162-163) | Standard-style protection relay, IEC 60255, SCADA compatible (RHP p159) | Panel builders, OEMs, utilities, 6 dealers (RHP p174) | Orders from the order book; terms NOT FOUND |
| SCADA and substation automation | Relays, computers, communications hardware (RHP p160) | System design; 5 SCADA staff (RHP p175); approved SCADA vendor up to 220 kV for CSPTCL (Reg 30, 10-Feb-2026) | Automation panel and SCADA system for substations | EPC contractors on utility turnkey projects | NOT FOUND |
| Exports (Kuwait, one customer) | As above | As above | 46.28 of FY26 revenue (AR p115, per B03) | One foreign buyer | NOT FOUND |

The vendor-registration gate: on 10-Feb-2026 MPPTCL (a utility) registered Avana "as a new vendor for supply of 400 kV line C&R panel to the contractor" that holds the turnkey contract (Reg 30 filing). So the utility approves the supplier; the EPC contractor places the order. That is an approval, not an order (B00).

### 1C Revenue model classification
| Stream | Type (taxonomy) | Description | % of revenue (anchored) | Predictability |
|---|---|---|---|---|
| Control and relay panels | One-time project/transactional sale, build-to-order, point-in-time at delivery and acceptance (AR p103) | Custom panel per order and drawing | 57.99% FY23, 48.05% FY24, 48.94% FY25, 60.26% H1 FY26; FY26 NOT FOUND (RHP p152) | M. Backed by order book 3,417.61 in the top-10 panel orders at 30-Nov-2025 (RHP p172) but lumpy by customer |
| Relays | Repeat transactional product sale | Standard-family relays, repeat buyers | 42.01%, 51.95%, 51.06%, 39.74%; FY26 NOT FOUND (RHP p152) | M. Top-10 relay order book only 254.19 at 30-Nov-2025: short cycle, low visibility (RHP p171) |
| SCADA / automation | Project, embedded in panel orders | Not reported separately | NOT FOUND | L |
| After-sales / warranty service | Cost, not revenue | Warranty provision 322.15 at 31-Mar-2026 (AR p124) | n/a | n/a |

Whole company by channel: private players 82.22% (FY25) and 76.24% (H1 FY26), tender/government 16.38% and 22.90%, dealers 1.40% and 0.86% (RHP p167). Repeat customers: 163 of 367 customers in FY25, with revenue 4,381.17 = 71.3% of revenue (RHP p168-169; derived). No recurring or subscription revenue. Predictability of the whole book: medium. The order book was 5,223.65 at 30-Nov-2025, about 62% of FY26 revenue 8,385.88 (derived; RHP p171; B03 4C).

### 1D Business model canvas
| Block | Answer | Anchor |
|---|---|---|
| What they sell | Control and relay panels, numerical and electromechanical relays, SCADA/automation panels, test blocks, semaphores (7 product types) | RHP p159-161 |
| Who buys | EPC contractors and panel builders (private 76-82%), state utilities by tender (16-23%), 6 dealers (about 1%); 367 customers FY25 | RHP p167-168 |
| Why them | Customisation to utility drawings, in-house relay design (9 R&D staff), IEC testing, ISO 9001:2015, 15 years of operation | RHP p169-170 |
| How delivered | Direct supply from Bengaluru Peenya; panel fabrication outsourced; 4 sales staff in North, Central, West regions (RHP p170) | RHP p164, p170 |
| Cost structure | Materials dominate: net material cost 59.39% of FY26 revenue (52.19% FY25); employee 12.6%; other expenses 8.5% (derived from AR p100, p115-116, per B03 3C) | AR p100 |
| Scarce resource | Engineering time and tested designs. Not capital: plant net 46.24 only. The binding limit has been floor space (12,500 sq ft; "further capacity expansion is not possible") | RHP p170; AR p112 |
| Pricing power source | Partial: spec and design in. Against it: tender selection is "price competitiveness ... primary selection criterion" after technical clearance (RHP p174); gross margin fell 7.2 points in FY26 | RHP p174; AR p100 |
| Asset intensity | Light today: net fixed asset turnover 17.90x FY25 (RHP p166); steps up with the integrated unit (CWIP 466.79 plus commitments 1,094.99; AR p112, p119) | RHP p166 |
| Working capital intensity | High: cycle 176.8 days derived (inventory 164.4, receivables 96.7, payables 84.3) | AR p99, p113, p115 per B03 |
| Regulatory moat or burden | Utility vendor approvals and type tests (IEC, NABL labs) work as a gate. No licence. Quality Control Order exposure NOT FOUND | RHP p169; Reg 30 10-Feb-2026 |

### 1E The chai-stall-uncle version
Every substation has a control room. In it sit steel cabinets full of wiring and small devices that notice trouble and cut the power. Avana builds those cabinets one at a time to the buyer's drawing. It also makes the small devices, called relays, in its own electronics shop. The buyer is mostly a contractor who won a big utility project, so Avana is a supplier inside someone else's order. Think of a tailor who stitches suits to each customer's measurements and also sells ready-made shirts. The suits earn the big cheques and the shirts earn the repeat orders. The tailor's shop is full, so a bigger shop is being built, and the shop's lease and land permit make the move the key test.

### Section 1 summary table
| Item | Answer |
|---|---|
| Business type | Manufacturing (assembly and design); build-to-order panels plus relays |
| Revenue nature | Transactional and project-linked; mostly B2B sales to EPC contractors and panel builders; no recurring element |
| Asset intensity | Light today (net fixed asset turnover 17.90x FY25); rising with the new unit |
| WC intensity | High (176.8-day cycle, FY26 derived) |
| Pricing power | Moderate and unproven: design-in helps, tender price rule and 7.2 point gross-margin fall hurt |

---
## SECTION 2: INDUSTRY DYNAMICS AND COMPETITIVE POSITION

### 2A Five forces
| Force | Plain answer | Helps / hurts / neutral | Anchor |
|---|---|---|---|
| Competition | RHP names two competitors: Danish Power Ltd (FY25 revenue 42,670.98, consolidated) and Aartech Solonics Ltd (3,635.22). The RHP also says "many of our competitors have a substantially large capital base" and the industry has "intense competition" with global giants and local players. Avana FY25 revenue was 6,148.58. Number of panel and relay makers overall: NOT FOUND | Hurts | RHP p119, p174-175 |
| Entry barriers | Moderate. Utility vendor approvals and IEC type tests take time; assembly capital need is low (plant net 46.24). Barriers rest on approvals, not on capital or scale | Neutral | RHP p169; AR p112 |
| Supplier power | Top 5 suppliers 42.62% of FY25 purchases, top 10 58.83%; 98.3% to 99.4% domestic; imports only from Germany (1.69% H1 FY26) | Neutral to hurts: copper, aluminium and component price shifts show up in gross margin; the MD&A names them but does not tie them to the fall | RHP p168, p172; AR p79-82 |
| Customer power and concentration | High. Private panel builders and EPC contractors are 76-82% of revenue; top 5 up to 38.79% in H1 FY26; three states (MP, Maharashtra, Karnataka) 48.33% to 66.42% of revenue; tender price rule | Hurts | RHP p38-39, p168-169, p174 |
| Substitutes | Low for protection functions. The change from electromechanical to numerical relays and to digital substations is a product upgrade inside Avana's range. A larger OEM (switchgear or relay major) entering the Indian small-panel space is the real threat: NOT FOUND in the documents | Neutral | RHP p159; AR p68-69 |

### 2B Competitive positioning map
| Competitor | Scale (FY25 revenue, lakh) | Overlap | Where Avana differs | Anchor |
|---|---|---|---|---|
| Danish Power Ltd (DANISH) | 42,670.98 consolidated; P/E 22.07; RoNW 18.00% | Transformers plus protection and control panels, substation automation, renewable evacuation | Avana is a panel and relay specialist at about 1/7 of the revenue; no transformers | RHP p119; step1 brief |
| Aartech Solonics Ltd | 3,635.22 consolidated; P/E 66.86; RoNW 8.74% | Named by RHP as significant competitor; detail NOT FOUND | NOT FOUND | RHP p119, p175 |
| Shivalic Power Control (SPCL), Marine Electricals | Not named in the RHP; held in corpus as peers (B00) | Panels up to 33 kV (SPCL) and switchboards (Marine) | Lower voltage or different end-market; stage 6 owns the comparison | B00 corpus_manifest |
| Protection-relay pure play | None listed (B00 input_gaps) | Relays about 40-51% of Avana revenue | No direct peer | B00 |

Avana's position: a small specialist with a relay design capability that most panel assemblers lack. Avana FY25 NAV 38.13, EPS 4.76 (RHP p119). Market share: NOT FOUND, check presentation. Not estimated.

### 2C Moat assessment (eight standard types)
| Moat type | Evidence | Durability |
|---|---|---|
| Switching costs | Utility vendor registration and type-tested designs make a customer's change of vendor costly mid-project; repeat customers gave 71.3% of FY25 revenue (RHP p168-169; derived) | Medium: project orders are re-bid; repeat is not contract-locked |
| Intangible assets (approvals, certifications) | MPPTCL vendor registration (400 kV), CSPTCL SCADA approval (220 kV), ISO 9001:2015, IEC 60255 compliance, NABL tests (Reg 30 10-Feb-2026; RHP p159, p169) | Medium: approvals are state by state and can lapse |
| Cost advantage | None evidenced. Gross margin fell 47.80% to 40.61% (AR p100) | Absent |
| Network effects | None | Absent |
| Efficient scale | None; Avana is far smaller than DANISH; floor space has capped output | Absent today; the integrated unit is the test |
| Brand | Weak; company says it aims to provide "branded, standardized" products (RHP p175) with no brand metric | Weak |
| Proprietary technology | In-house relay hardware and firmware; 9 R&D staff; R&D salaries 33.53 in FY25 = 0.55% of revenue (derived; RHP p170). Patents: NOT FOUND | Low to medium |
| Regulatory or distribution | Only 6 dealers; no regulatory licence moat | Absent |

Moats present: switching costs/approvals (medium), proprietary relay design (low to medium).

### 2D Industry lifecycle
Growth phase for the end market: the AR cites the Indian electric control panel market at US$486 million in 2025 rising to US$790 million by 2031 at 8.4% a year (AR p70, per B03), a third-party estimate. Avana's FY26 growth of 36.4% is over 4 times that rate, so it is gaining share or riding a few big orders; the filings do not separate the two. Production of "relays, aux. relays and timers" in the IEEMA national data was 2,711,128 units in 2024-25, down 0.09% (RHP p148), so the standard relay category was flat. Avana sits in the early-scale phase of a growing, fragmented niche, as a minor player.

### 2E Key industry drivers
| Driver | Direction | Impact on Avana | Anchor |
|---|---|---|---|
| State discom and transmission capex (RDSS, substation build) | Up | Direct: panels and SCADA for utility substations | AR p70-82 per B03 |
| Renewable evacuation substations | Up | Direct: panels for solar and wind projects | RHP p153 |
| Move to numerical relays, IEC 61850 and digital substations | Up | Positive for relay and SCADA content | AR p68-69 |
| Copper, aluminium and component prices | Uncertain | Pressure on gross margin; pass-through evidence NOT FOUND | AR p79-82 |
| Procurement model: utilities buying through EPC contractors rather than directly | Shift | Tender share fell from 26.71% (FY23) to 16.38% (FY25), moving the buyer to private EPC | RHP p167 |
| Floor space and new KIADB unit | Pending | Capacity is the binding constraint; delivery risk per B03 | RHP p170; B03 |

---
## SECTION 3: FINANCIAL METRICS THAT MATTER

### 3A Ignore these, track these
| Common ratio | Why misleading for Avana |
|---|---|
| Spot ROCE and ROE as printed | IPO cash 2,103.98 unspent inflates the denominator; printed FY25 ROCE 57.52% uses long-term debt only; stage 10 should use the 27.9% stated-definition and 40.5% ex-cash side by side (AR p127; B03 3B) |
| Current ratio 3.34x | 2.40x excluding IPO cash (B03 3B); liquidity is issue money, not operations |
| Debt/equity, interest cover | Debt is 76.14 (0.013x); the MD&A's printed 0.05x cover is an error (19.4x derived; AR p74; B03). Ratios say nothing about quality here |
| Revenue growth alone | A single large panel order moves a period; use order book and repeat-customer revenue |
| EV/Sales | Margins and working capital differ widely across panel makers and relay makers; sales multiples hide that |
| Book value / P/B | Equity is inflated by the IPO raise; asset-light operating base |
| Spot working-capital days | Period-end snapshot; product mix (panels vs relays) shifts it by period. Track at least two period-ends |
| Capacity utilisation (as stated) | Panels 886 produced vs 600 stated capacity (148%): the stated basis is unreliable (AR p85; RHP p165) |

### 3B Must-track metrics
**Growth**
| Metric | What it tells you | Healthy for this model | Where to find | Red flag |
|---|---|---|---|---|
| Order book and book-to-bill | Forward revenue; 5,223.65 at 30-Nov-2025 was about 62% of FY26 revenue (derived) | Order book at 50%+ of next-year revenue, not falling two periods | Reg 30, results, AR (not disclosed in MD&A; NOT FOUND for FY26) | Order book NOT disclosed again, or book-to-bill below 1 |
| Product-wise revenue (panels vs relays) | Mix drives margin | Disclosed each half-year | NOT FOUND in FY26 | Still undisclosed at H1 FY27 |
| Revenue from repeat customers | Stickiness: 71.3% of FY25 | Above 65% | RHP-style KPI; AR NOT FOUND | Below 55% or top 5 above 40% |
| Customer concentration (top 5, top 10, state share) | Dependence on a few EPC buyers | Top 5 at or below 25-30% | NOT FOUND for FY26 | Top 5 above 38.79% |

**Profitability and efficiency**
| Metric | What it tells you | Healthy | Where | Red flag |
|---|---|---|---|---|
| Gross margin | Mix and input-cost pass-through | At or above 40.6%; H2 FY26 36.61% | Results (derived from materials and inventory change) | Below 36.6% again |
| EBITDA margin excl other income | Exit rate | At or above 18.1% (H2 FY26) | H1 FY27 results | Below 18.1% |
| Warranty additions % revenue | Whether the margin is real: 0.50% FY26 vs 3.72% FY25 | 2.1% or more is reversion (B03 midpoint) | Provision note | Below 0.75% for a second period without evidence of fewer failures |
| CFO / EBITDA | Cash backing: 48.7% FY26 | Above 70% | Cash flow | Below 50% |
| Inventory days (RHP definition) | 164.4 FY26; plan 150 | At or below 150 | Balance sheet | Above 170, or finished goods and stock in transit keep rising (690.47, 263.44) |

**Balance sheet and risk**
| Metric | What it tells you | Healthy | Where | Red flag |
|---|---|---|---|---|
| Receivable days and over-6-month share | 96.7 days; 13.8% over 6 months, no provision | At or below 100 days and 13.8% | AR Note 14 | Over 15% or any provision |
| Retention money and bank stock-statement variances | Hidden receivable risk | Disclosed; small | AR p125; RHP p113 | Variance above books each quarter (already true) |
| IPO capex used vs 1,155.38 plan | Delivery | Trending to plan | Auditor utilisation certificate | Still at 275.83 after the KIADB date |
| Lease and land status (KIADB 26-Oct-2026; operating-unit leases Jul/Aug-2026) | Continuity | Renewal or relocation filed | Reg 30 | Silence after 26-Oct-2026 |

### 3C Industry KPIs (standard sector list for capital goods and electrical equipment, applied to Avana)
| KPI | Why | Where | Status |
|---|---|---|---|
| Order inflow and order book | Visibility | Reg 30 and results | Only RHP 30-Nov-2025 held |
| Capacity and utilisation, by product | The expansion case | AR p85, RHP p165 | Basis unreliable (886 vs 600) |
| Output per day per unit | Productivity: panels 1.74 FY25 and 2.07 H1 FY26; relays 219.47 and 222.85 (RHP p166-167) | RHP | Not updated for FY26 in the AR |
| Tender share vs private share | Buyer mix | RHP-style KPI | 22.90% tender in H1 FY26 |
| Vendor approvals by utility | Pipeline | Reg 30 | MPPTCL (400 kV) and CSPTCL (SCADA 220 kV): approvals, not orders |
| Warranty claims | Quality | AR note | Provision 322.15, accrual falling |
| R&D spend | Product pipeline | RHP KPI | 33.53 in FY25 (0.55% of revenue), FY26 NOT FOUND |
| Export revenue | Diversification | AR p115 | 46.28 = 0.55% of FY26 revenue |

### 3D Unit economics (the physics)
- Unit: one control and relay panel (project unit) and one relay (catalogue unit). Revenue per produced unit, derived as segment revenue / units produced (RHP p152, p165; AR p85). Caveat: the RHP's MD&A cites relay sales of 73,621 units in FY24 against 58,501 produced (RHP p271 vs p165), so sold and produced units differ; per-unit figures are indicative.

| Item | Panel | Relay | Anchor |
|---|---|---|---|
| Revenue FY25 (lakh) | 3,008.96 | 3,139.62 | RHP p152 |
| Units produced FY25 | 523 | 65,840 | RHP p165 |
| Revenue per produced unit FY25 | 5.75 lakh | Rs 4,769 | derived |
| Revenue H1 FY26 | 2,154.28 | 1,420.43 | RHP p152 |
| Units produced H1 FY26 | 313 | 33,650 | RHP p165 |
| Revenue per produced unit H1 FY26 | 6.88 lakh | Rs 4,221 | derived |
| Units produced FY26 | 886 (+69%) | 62,034 (-5.8%) | AR p85 |
| Margin per unit by product | NOT FOUND | NOT FOUND | only a company-level gross margin exists |
| Product-wise revenue FY26 | NOT FOUND | NOT FOUND | |

- Volume drivers: panels follow utility substation tenders and EPC award timing; relays follow panel demand (relays also go into Avana's own panels) and repeat orders from builders. Price drivers: per-order specification (voltage class, number of bays, SCADA content); H1 FY26 panel revenue per unit is up 19.7% on FY25 while relay revenue per unit fell 11.5% (derived), so the price per unit moved in opposite directions. Cost drivers: bought-in relays, meters and cubicles for panels; ICs and transformers for relays; labour charges (+38.7% in FY26, B03 3C); fabrication is outsourced.
- Incremental margin FY26 vs FY25, derived from AR p100: revenue +2,237.30; gross profit +466.25 (20.8% incremental gross margin); EBITDA excl other income +380.77 (17.0% incremental margin) against a 20.36% base. Operating leverage came from employee cost (+19.6% vs revenue +36.4%) and other expenses (-11.0%), not from gross margin. Gross margin is the line to watch; the other cost lines may not fall again.
- Capacity: relays 70,000 and panels 600 stated; the new unit is planned at 1,75,000 relays and 1,500 panels (B03 guidance table). Panels already ran at 886 vs 600 (AR p85), so either the stated capacity was narrow or part of the work went to outside labour (labour charges +38.7%). Cause NOT FOUND.

---
## SECTION 4: RISKS, VALUATION APPROACH AND MONITORING

### 4A Business-model-specific risks
| Category | Risk | Evidence | First line item to deteriorate |
|---|---|---|---|
| Revenue model | Buyer concentration (EPC, three states, top 5 38.79%) and loss of one large panel order | RHP p38-39, p168-169 | Revenue from operations in the half after the loss; customer top-5 share |
| Revenue model | Utilities buy through EPC contractors, so Avana carries EPC credit and price pressure | RHP p167 | Receivable days and over-6-month share |
| Margin | Gross margin falls on mix (panels up) or copper/component price | AR p100; RHP p166 | Gross margin (materials consumed plus inventory change over revenue) |
| Margin | Warranty accrual 0.50% vs 3.72% is lifting FY26 margin | AR p124 (B03) | Warranty additions in the H1 FY27 provision note |
| Balance sheet | Working capital stays high; finished goods and stock in transit rise | AR p113 | Inventory days; CFO/EBITDA below 50% |
| Balance sheet | Receivables above books in bank statements every quarter; no ECL | AR p125, p113 | Over-6-month receivables; bank-statement variance |
| Execution | KIADB unit unbuilt; 26-Oct-2026 deadline; both operating-unit leases expire Jul/Aug-2026 per RHP, renewal NOT FOUND | RHP p36-37, p43-44, p179; AR p112 | CWIP and capex used; Reg 30 on commercial production |
| Execution | Capacity measure unreliable (886 vs 600); planned +150% capacity with no stated order cover | AR p85; RHP p165 | Panel output per half; order book |
| Structural | Larger peers and global OEMs; tender price rule; vendor approval is state by state | RHP p174-175 | Tender share and gross margin on tender orders |
| Structural | Governance flags: independents 47% attendance, promoter pay +56.1% fixed, family fees 78.00 | B03 Phase 5 | Promoter pay vs PAT; attendance |

### 4B Valuation method applicability (formal handoff to Role 1)
| Method | Applicable? | Reason |
|---|---|---|
| P/E on forward earnings | Yes. PRIMARY | Profitable, asset-light, net-cash, growing; earnings basis comparable to entry; Section 1B destination PE governs the exit multiple, sector cap row Cables / Industrial products (B00) |
| EV/EBITDA | Yes. SECONDARY | Strips out the IPO cash (net cash 2,706.64) and the 2,103.98 unspent issue money; cross-checks P/E against the operating margin (EBITDA excl other income 19.5% FY26) |
| Reverse DCF / FCF-based | Yes, tertiary | FCF was 45.21 in FY26 after KIADB capex; a full DCF depends on unit delivery, so use it to test what growth the CMP implies, not to set value |
| EV/Sales | No | Margin gap between peers; relay and panel economics differ |
| P/B and ROE-based | No (cross-check only) | Equity inflated by IPO cash; ROE moves with the deployment of that cash |
| SOTP | No | Single reportable segment; product-wise margin NOT FOUND |
| NAV / asset value | No | Light-asset; land 345.75 is not the value |
| Dividend yield | No | Dividend is not the thesis |
| PEG | Cross-check only | Growth is lumpy; use after Role 1 has a forward growth basis |

Primary: P/E on forward earnings, fed by the Role 1 forward revenue basis (26.1) and margin bridge (26.2). Secondary: EV/EBITDA. Tertiary: reverse DCF. Cycle stage that matters: the utility T&D and renewable-evacuation capex cycle, and the transition from two leased units to one integrated unit (execution stage). Not applicable: EV/Sales, SOTP, NAV, dividend yield, P/B as primary. Archetype note for the operator's Mental Model: Build-to-spec component maker (panels: customer capex cycle, design-win pipeline, content per unit) with an Order-book overlay for the panel line; relays are closer to a repeat-product line. The operator declares it; not set here.

### 4C Half-yearly monitoring checklist
SME files half-yearly; use H1 FY27 results and Reg 30 filings.
| # | Item | Good | Trouble |
|---|---|---|---|
| 1 | KIADB unit status (Reg 30 by 26-Oct-2026) | Commercial production filed, or a dated extension letter | Silence after the date |
| 2 | Order book disclosure | Disclosed, at or above 5,223.65 | Not disclosed; falling |
| 3 | Gross margin | At or above 40.6% | Below 36.6% |
| 4 | EBITDA margin excl other income | At or above 18.1% | Below 18.1% |
| 5 | Warranty additions % revenue | Near 2.1% or evidence for the lower rate | Below 0.75% twice |
| 6 | Product-wise revenue | Panels and relays shown | Still undisclosed |
| 7 | Top 5 customer share | At or below 38.79% | Higher; any one state above 33% |
| 8 | Receivable days; over 6 months | At or below 100 days; at or below 13.8% | Above 110 days; provision |
| 9 | Inventory days and finished goods | At or below 150; falling FG | Above 170 |
| 10 | CFO / EBITDA | Above 70% | Below 50% |
| 11 | IPO capex used cumulative | Trending to 1,155.38 | Stays near 275.83 |
| 12 | Tender share | Stable at 16-23% | Rising price-led tender dependence |
| 13 | New vendor approvals turning into orders (MPPTCL 400 kV, CSPTCL SCADA) | Named orders | Approvals only |
| 14 | Lease renewals of both units | Renewed or relocated | Not disclosed |
| 15 | Promoter pay and independents' attendance | Pay in line with PAT; above 75% | Pay outpaces PAT |

### 4D Questions for management
| # | Question | Reassuring answer | Worrying answer |
|---|---|---|---|
| 1 | What are FY26 revenue and gross margin by product (panels vs relays), and which line drove the 7.2 point gross-margin fall? | Revenue and margin by product given; the fall is mix with unchanged product margins | Cannot or will not split; or the fall is price cuts |
| 2 | Who are the top 5 customers in FY26 (EPC, panel builder, utility) and what share are they? | Top 5 at or below 25-30%, naming utilities as the end users | Above 38.79% or one customer or state above 33% |
| 3 | What is the order book today, the share of panels, and the delivery schedule against 886 panels in FY26? | At or above 5,223.65, with schedule beyond 12 months | Falling or undisclosed |
| 4 | Why did warranty additions fall from 3.72% to 0.50% of revenue? | Evidence of fewer field failures or a changed claim basis | No change in product, no data |
| 5 | Panels were 886 against a stated capacity of 600: what is the true installed capacity and how much is outsourced? | Capacity restated with the outsourcing share named | Output unit definition differs; unexplained |
| 6 | What are the KIADB status, extension date and lease status of both current units? | Dated KIADB letter; units renewed | No letter; deadline passes without filing |
| 7 | What are the payment terms, retention money and bank-stock-statement variance with EPC customers? | Terms disclosed; retention small and falling | Retention rising; variances persist |

---
## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD
```
+--------------------------------------------------------------------------+
| AVANA ELECTROSYSTEMS LTD (AVANA)    Run 2026-10-05    Stage 4 B04       |
+--------------------------------------------------------------------------+
| ONE LINE: Makes control and relay panels and protection relays for       |
| substations; sells mostly to EPC contractors and panel builders.         |
+--------------------------------------------------------------------------+
| Business type     | Manufacturing (assembly, build-to-order + relays)    |
| Revenue nature    | Project and repeat transactional; no recurring       |
| Mix (H1 FY26)     | Panels 60.26% / Relays 39.74% (RHP p152); FY26 NF    |
| Customer mix      | Private 76.24%, tender 22.90%, dealers 0.86% (H1)    |
| Concentration     | Top 5 38.79% H1 FY26 (22.42% FY25); FY26 NOT FOUND   |
| Asset intensity   | Light now; rises with KIADB unit                     |
| WC intensity      | High, 176.8 days FY26 (derived)                      |
| Pricing power     | Moderate, unproven: gross margin 47.80% to 40.61%    |
| Cyclicality       | Secular growth, lumpy on utility capex timing        |
| Moats             | Approvals/switching (medium); relay design (low-med) |
+--------------------------------------------------------------------------+
| PRIMARY VALUATION: P/E forward (Section 1B governs exit).                |
| SECONDARY: EV/EBITDA. TERTIARY: reverse DCF.                             |
+--------------------------------------------------------------------------+
| TOP 5 MUST-TRACK                                                         |
| 1 Order book and product-wise revenue                                    |
| 2 Gross margin (floor 36.6%) and EBITDA margin ex OI (floor 18.1%)       |
| 3 Warranty additions % revenue (0.50% FY26 vs 3.72%)                     |
| 4 Top 5 customer share and state share (38.79% H1 FY26)                  |
| 5 CFO/EBITDA (48.7%) with inventory days (164.4) and IPO capex used      |
+--------------------------------------------------------------------------+
| KEY FLAGS: product-wise margin NOT FOUND; FY26 concentration NOT FOUND;  |
| KIADB date 26-Oct-2026; panel output 886 vs 600 stated capacity.         |
+--------------------------------------------------------------------------+
```

## Evidence gaps carried (not filled)
Product-wise FY26 revenue and margin; FY26 top-5 and customer identities; FY26 customer-type mix; order book after 30-Nov-2025; payment terms; patents; market share; competitor financial detail beyond RHP p119; true capacity basis. Voltage range wording differs: RHP says panels 11-220 kV (RHP p153), the AR says SCADA and automation up to 400 kV (AR p68), and the Reg 30 filing of 10-Feb-2026 shows a 400 kV panel vendor registration.

```yaml
stage: B04-bizmodel
company: "AVANA"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "Investor presentation NOT PROVIDED (none exists); RHP Our Business and Industry Overview used instead; RHP stops at H1 FY26 (mix, customers) and 30-Nov-2025 (order book)"
  - "No concalls (NO-CONCALL MODE); FY26 product-wise revenue and margin, FY26 top-5 customers and identities, FY26 customer-type mix, order book after 30-Nov-2025, payment terms, patents, market share: NOT FOUND"
  - "Carried from B00/B03: AR pp.99-127 are image transcriptions; screener export sheets empty; no rating document; only FY2025-26 AR exists; RHP is the pre-listing baseline"
  - "RHP/AR conflicts: panel voltage 11-220 kV (RHP p153) vs SCADA up to 400 kV (AR p68) and MPPTCL 400 kV vendor registration; relay sold units 73,621 (RHP p271) vs produced 58,501 (RHP p165) for FY24"
flags:
  - {type: FLAG-MIX, reason: "Mix shifted to panels 48.94% FY25 to 60.26% H1 FY26 while FY26 gross margin fell 47.80% to 40.61%; no product-wise margin, so cause stays a hypothesis (RHP p152; AR p85, p100)"}
  - {type: FLAG-CONCENTRATION, reason: "Top 5 customers 38.79% H1 FY26 vs 22.42% FY25, private players 76-82%, MP 33.59% of FY25; FY26 NOT FOUND (RHP p38-39, p168-169)"}
  - {type: FLAG-CAPACITY-BASIS, reason: "Panels 886 produced vs 600 stated capacity (AR p85; RHP p165); stated capacity unreliable for the +150% expansion case"}
  - {type: FLAG-EXECUTION, reason: "KIADB unit unbuilt, 26-Oct-2026 deadline, operating-unit leases Jul/Aug-2026 per RHP (carried from B03)"}
business_type: "manufacturing"
revenue_streams:
  - {name: "Control and relay panels (custom, 11-220 kV; SCADA/automation embedded)", type: "project-linked one-time transactional sale", pct_of_revenue: 60.26, predictability: "M"}   # H1 FY26 (RHP p152); FY25 48.94; FY26 NOT FOUND
  - {name: "Protection relays (numerical and electromechanical)", type: "repeat transactional product sale", pct_of_revenue: 39.74, predictability: "M"}   # H1 FY26 (RHP p152); FY25 51.06; FY26 NOT FOUND
  - {name: "SCADA / substation automation", type: "project, not reported separately", pct_of_revenue: 0, predictability: "L"}   # NOT FOUND separately; inside panels
asset_intensity: "light"
wc_intensity: "high"
pricing_power: "moderate"
cyclicality: "secular-growth"
moats_present:
  - "switching costs and utility vendor approvals (MPPTCL 400 kV, CSPTCL SCADA 220 kV): medium durability"
  - "proprietary relay hardware and firmware design (9 R&D staff, patents NOT FOUND): low to medium durability"
valuation_methods:
  primary: {method: "P/E on forward earnings (Section 1B destination PE governs exit)", why: "profitable, asset-light, net-cash, growing; matches entry earnings basis"}
  secondary: {method: "EV/EBITDA on EBITDA excl other income, net of cash", why: "removes 2,103.98 unspent IPO cash; cross-checks P/E against operating margin"}
  tertiary: {method: "reverse DCF on FCF", why: "FCF 45.21 FY26 after capex; test the growth the price implies, not set value"}
  not_applicable: ["EV/Sales", "SOTP (single segment, no product margin)", "NAV / asset value", "dividend yield", "P/B as primary (equity inflated by IPO cash)"]
irrelevant_ratios:
  - "spot ROCE and ROE as printed: IPO cash 2,103.98 and printed FY25 long-term-debt-only base distort them"
  - "current ratio 3.34x: 2.40x ex IPO cash"
  - "debt/equity and interest cover: debt 76.14; MD&A 0.05x cover is wrong (19.4x derived)"
  - "EV/Sales: product mix and margin differ widely"
  - "P/B: net worth inflated by IPO proceeds"
  - "stated capacity utilisation: panels 886 vs 600 stated capacity"
must_track_metrics:
  - {metric: "order book and product-wise revenue (panels vs relays)", healthy: "order book at or above 5,223.65 (30-Nov-2025), about 62% of FY26 revenue; product split disclosed", red_flag: "order book undisclosed or falling; no product split at H1 FY27"}
  - {metric: "gross margin and EBITDA margin excl other income", healthy: "gross at or above 40.6%; EBITDA ex OI at or above 18.1%", red_flag: "gross below 36.6% or EBITDA ex OI below 18.1%"}
  - {metric: "warranty additions % of revenue", healthy: "near 2.1% or evidence for a lasting lower rate", red_flag: "below 0.75% twice with no failure-rate evidence (FY26 0.50%, FY25 3.72%)"}
  - {metric: "top 5 customer share and largest state share", healthy: "top 5 at or below 25-30%; no state above 33%", red_flag: "top 5 above 38.79%; MP-like single-state dependence"}
  - {metric: "CFO/EBITDA with inventory days and IPO capex used", healthy: "CFO/EBITDA above 70%; inventory days at or below 150; capex used trending to 1,155.38", red_flag: "CFO/EBITDA below 50% (FY26 48.7%); inventory above 170 days; capex used stuck near 275.83"}
unit_economics:
  unit: "one control and relay panel (project unit) and one relay (catalogue unit)"
  revenue_per_unit: "FY25 panel 5.75 lakh (3,008.96 / 523), relay Rs 4,769 (3,139.62 / 65,840); H1 FY26 panel 6.88 lakh, relay Rs 4,221; derived on produced units (RHP p152, p165)"
  margin_per_unit: "NOT FOUND by product; company-level gross margin 40.61% FY26 (H2 36.61%), incremental EBITDA margin excl OI 17.0% FY26 (derived)"
  key_lever: "panel-to-relay mix and input-cost pass-through (gross margin); then warranty accrual and capacity from the KIADB unit"
first_deterioration_signals:
  - {risk: "buyer concentration (EPC, 3 states)", first_signal: "top 5 share above 38.79% or revenue drop after a large order ends"}
  - {risk: "gross margin falls on panel mix or input cost", first_signal: "gross margin below 36.6% in H1 FY27"}
  - {risk: "warranty accrual understated", first_signal: "warranty additions below 0.75% of revenue a second period"}
  - {risk: "working capital and EPC credit", first_signal: "receivable days above 110 or over-6-month share above 15%; CFO/EBITDA below 50%"}
  - {risk: "KIADB unit and lease continuity", first_signal: "no Reg 30 commercial-production filing after 26-Oct-2026; capex used still near 275.83"}
  - {risk: "capacity basis unreliable", first_signal: "panel output stays above 600 with no capacity restatement"}
mgmt_questions:
  - "FY26 revenue and gross margin by product, and which line drove the 7.2 point gross-margin fall?"
  - "Who are the FY26 top 5 customers (EPC, panel builder, utility) and what share are they?"
  - "Order book today, panel share, delivery schedule?"
  - "Why did warranty additions fall from 3.72% to 0.50% of revenue?"
  - "True installed capacity and outsourced share, given 886 panels vs 600 stated?"
  - "KIADB status, extension date, and lease status of both current units?"
  - "Payment terms, retention money and bank-stock-statement variance with EPC customers?"
one_line_verdict: "A build-to-spec panel and relay maker selling through EPC contractors with real design-in gates, but concentration, product margin and capacity basis are undisclosed; value it on forward P/E with margin and order-book disclosure as the tests."
analyst_note: "Mix is the lever that matters and the filings do not give it for FY26. Panel share rose from 48.94% (FY25) to 60.26% (H1 FY26) while production shows panels +69% and relays -5.8% for FY26 (AR p85); gross margin fell 7.2 points. [INFERENCE] If panels carry lower gross margin than relays, mix explains most of the fall; if not, input cost or pricing does. The one observation that separates the two readings: H1 FY27 product-wise revenue and gross margin. The utility approves the vendor, the EPC buys (Reg 30 10-Feb-2026), so end-customer risk sits with state utilities while credit risk sits with EPCs. Per-unit revenue uses produced, not sold, units; RHP shows FY24 relay sold 73,621 vs produced 58,501."
```
