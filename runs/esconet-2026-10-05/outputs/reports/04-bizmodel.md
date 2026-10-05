# Stage 4: Business Model Decoder. Esconet Technologies Ltd (ESCONET), run 2026-10-05

Sources and conventions. AR26 = FY2025-26 Annual Report (page = PDF page marker; ₹ Lakhs on its face, 1 Cr = 100 Lakhs). PROSP = IPO prospectus dated 20 Feb 2024 (₹ Lakhs). Pres Jun26 = 22 Jun 2026 investor deck (₹ Cr). Pres Sep25 = Sep 2025 deck (₹ Cr and ₹ Lakhs as printed). B02 and B03 = prior stage blocks (used for facts they anchor; call transcript facts are quoted from B03 as CALL26). Consolidated figures unless "standalone" is stated. "Derived" = my arithmetic on anchored inputs. Missing data is NOT FOUND.

First verification priorities from the brief, answered up front:

| # | Priority | Answer from this stage's documents |
|---|---|---|
| 1 | Q1 FY27 margin jump: HexaData vs traded mix, services, cloud, cyber. Is revenue by line disclosed? | NOT disclosed anywhere in AR, prospectus or either deck. AR26 says one reportable segment (AR26 p.76). The only split is "Sales of IT products" 97.61% vs "Service charges" 2.39% of consolidated revenue (AR26 p.143, ₹ Lakhs; derived). HexaData, cloud and cyber revenue and margin: NOT FOUND, check concall or Q1 FY27 results. Two readings stay open (Section 3D, 4A). |
| 2 | Cash conversion and WC intensity | The model is working-capital heavy by construction: ~86.8% of each rupee of revenue is bought-in goods (derived, AR26 p.133), government buyers pay slowly and need FDR-funded guarantees (PROSP p.77). Cash conversion evidence is weak (B03 FLAG-CASH). Section 1D, 3B. |
| 3 | Governance items | Not a business-model topic, but two of them change how the model is read (Fluidech buy-in, Zeacloud intra-group sales). Carried as flags, Section 4A. |
| 4 | Guidance vs delivery; Singapore role | Deck says "not committing growth numbers" (Pres Jun26 slide 17). Singapore is a thin-margin trading arm, 13.8% of revenue at about 0.5% net margin (derived). Section 1C, 2B, 4D. |

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A One-line description

Esconet buys servers, storage, networking and software from big distributors and OEMs, assembles some of the servers under its own HexaData brand, installs and supports them for Indian government bodies and companies, and has small cloud and cybersecurity arms attached (AR26 p.14-19, p.75; Pres Jun26 slide 4). In revenue terms it is a hardware integrator and reseller: 97.61% of FY26 consolidated revenue is "Sales of IT products" (AR26 p.143, ₹ Lakhs; derived).

### 1B Money flow chain, per revenue stream

| Stream | Input | What the company does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| A. Traded and integrated hardware (branded OEM kit: Dell EMC, HPE, Cisco, NetApp, Hitachi Vantara, NVIDIA GPU systems) | Boxes bought from distributors (Ingram Micro 27.01% of FY23 purchases, Rashi, Redington, Tech Data, WPG) and OEMs; ~85% domestic, ~15% imported (PROSP p.142, p.139; FY23) | Quotes, bids on GeM and PSU tenders, procures, configures, ships, installs, commissions (PROSP p.146-148) | Working servers, storage, networks, GPU clusters at the client site | Government (NIC, ONGC, Indian Oil, Engineers India), PSUs, enterprises, universities (PROSP p.142-143; AR26 p.22 per B03) | Purchase order, then credit terms; government pays slowly and needs a performance bank guarantee or earnest money held as bank FDR (PROSP p.77) |
| B. HexaData own-brand servers, workstations, HPC and AI supercomputers | Components (chassis, PCB, memory, SSD, CPUs, GPUs, ASRock Rack and Chenbro boards) bought from suppliers, some imported (PROSP p.128, p.142) | Assembles and tests in its own facility; "capacity not applicable, our business is assembling and integration" (PROSP p.148); GPU access through NVIDIA Elite Partner tier (Pres Jun26 slide 11) | A branded server or cluster, sold as part of projects or alone | Same buyer pool; registered OEM on GeM (AR26 p.75; Pres Sep25 slide 12) | Same as A. Revenue and margin of this line: NOT FOUND |
| C. Service charges (integration, AMC, managed services, consulting) | Own engineers (~70 staff per Pres Sep25 slide 4) plus third-party service contractors (consolidated "Service Charges" expense 1,038.11 Lakhs, AR26 p.144) | Installs, supports, manages | Uptime and support | Same buyers | Contract fees. Revenue 847.30 Lakhs consolidated, 346.61 Lakhs standalone (AR26 p.143, p.114) |
| D. ZeaCloud (100% subsidiary): IaaS, BaaS, DRaaS, DaaS, private cloud | Rack space in third-party data centres, bandwidth from NTT, servers owned by ZeaCloud (PROSP p.130) | Hosts customer workloads | Cloud capacity per month | Enterprises, government (MeitY empanelment targeted, not obtained: Pres Jun26 slide 12) | Subscription. Revenue NOT FOUND as a line; PAT (10.04) Lakhs in FY26 (AR26 p.151) |
| E. Fluidech (70% subsidiary): cybersecurity consulting, SOC, GRC | Consultants (team build-out) | Audits, compliance, managed security | Reports, 24x7 monitoring | Enterprises, regulated entities | Project and retainer fees. Turnover 538.96 Lakhs, PBT (68.01) Lakhs (B02 rank 14; AR26 p.69) |
| F. Esconet Singapore (100%): international trading | Hardware bought abroad | Trades, "profitable in year one" (Pres Jun26 slide 14) | Goods to overseas customers | Customers NOT FOUND | Revenue about 13.8% of group (B03; AR26 p.69). Profit 25.57 Lakhs (AR26 p.151) |

Reading note. ZeaCloud and Fluidech revenue must sit inside the two consolidated revenue lines, but the AR does not say which. Service charges of 847.30 Lakhs consolidated minus 346.61 Lakhs standalone leaves 500.69 Lakhs from the subsidiaries (derived), against Fluidech turnover of 538.96 Lakhs alone (B02). So some subsidiary revenue is booked inside "Sales of IT products" or is intra-group. The line labels do not equal the business lines.

### 1C Revenue model classification

| Stream | Type (standard taxonomy) | Description | % of revenue (anchor) | Predictability |
|---|---|---|---|---|
| Sales of IT products (A + B + Singapore trading, plus some subsidiary revenue) | Transactional, project-based product resale and light manufacturing (assembly) | One-off sales against purchase orders and tenders | 97.61% of consolidated FY26 (34,593.19 of 35,440.48 Lakhs, AR26 p.143; derived). FY25: 99.35% (22,879.43 of 23,029.80) | Low to Medium. No long contracts; order book value NOT FOUND (AR26 p.24 says "strong", no figure; Pres Sep25 slide 19 says "pipeline ₹100 Cr+", a pipeline not a backlog) |
| Service charges (C, parts of D and E) | Services, project and recurring mix | Integration, AMC, managed services | 2.39% FY26 (847.30 Lakhs), 0.65% FY25 (150.38 Lakhs); grew 5.6x (AR26 p.143; derived) | Medium |
| Of which HexaData own-brand | Product (manufacturing/assembly) | | NOT FOUND, check concall or investor presentation | Low to Medium |
| Of which cloud (ZeaCloud) | Subscription (SaaS-like usage) | | NOT FOUND; mgmt calls cloud "very small" (brief, CALL26) | Medium to High if recurring |
| Of which cybersecurity (Fluidech) | Services, project and retainer | | NOT FOUND as line; Fluidech turnover 538.96 Lakhs = 1.52% of consolidated revenue (B02; derived) | Medium |
| Of which Singapore trading | Transactional trading | | About 13.8% (B03; AR26 p.69). Singapore PAT 25.57 Lakhs on revenue 4,905.58 Lakhs = 0.52% net margin (B02; AR26 p.151; derived) | Low |

Customer type (prospectus years, latest disclosed): government 35.75% of FY23 revenue (20.58% FY22, 26.49% FY21), 32.59% in H1 FY24 (PROSP p.140). Top ten customers 53.72% of FY23 revenue (PROSP p.142-143). FY26 customer and government split: NOT FOUND (B03).

### 1D Business model canvas

| Item | Esconet |
|---|---|
| What they sell | Compute, storage and network boxes, GPU/AI systems, own HexaData servers, plus installation, support, cloud and security services (AR26 p.14-19) |
| Who buys | Government and PSU (NIC, ONGC, Indian Oil, BEL named), enterprises, universities (PROSP p.142-143; Pres Sep25 slide 6) |
| Why them | Price (the prospectus credits "competitive pricing" for FY22 share gain, PROSP p.77), one-stop integration, GeM OEM listing, NVIDIA Elite Partner access to scarce GPUs (Pres Jun26 slide 11, 15) |
| How delivered | Tender or quote, procure, assemble, install on site, support (PROSP p.146-148) |
| Cost structure | Dominated by bought-in goods: net purchases 86.81% of revenue (30,764.85 of 35,440.48 Lakhs, AR26 p.133; derived). Employees 2.63%, other expenses 8.07% (AR26 p.133; derived) |
| Scarce resource | Allocation of GPUs and constrained components through NVIDIA tier (Pres Jun26 slide 11); the HexaData brand; NCIIPC accreditation inside Fluidech (Pres Jun26 slide 13) |
| Pricing power | Mostly absent. Gross margin fell from 15.23% to 13.19% when component prices rose (derived from AR26 p.133; Pres Jun26 slide 8 shows ~15.2% to ~13.2%). Management says "some components rose 100%+" and about ₹7 Cr of gross profit was absorbed (Pres Jun26 slide 8): cost shock was not passed through in the year |
| Asset intensity | Low to medium. PP&E 4.75 Cr to 9.89 Cr (Pres Jun26 slide 9); ZeaCloud owns servers and calls itself asset-heavy per MD (CALL26 p.18 via B03), while the Chairman letter says "asset-light" (AR26 p.13). Two company statements conflict |
| WC intensity | High. Consolidated inventory 5,149.87 Lakhs vs 1,894.21 standalone prior year; standalone receivables 4,499.21 Lakhs with 19.9% over six months and no provision; OD debt 1,187.42 Lakhs rolling (B02, B03; AR26 p.110-113, p.141). Net working capital days FY25 41.42 (Pres Sep25 slide 18) |
| Regulatory moat or burden | GeM registration and PSU bidding rules (PROSP p.147-148); performance bank guarantees tie up cash (PROSP p.77). No licence moat. Data-residency and MeitY rules favour ZeaCloud only if empanelment arrives (Pres Jun26 slide 12) |

### 1E Chai-stall-uncle version

Think of a big computer shop in Okhla. It buys most of its boxes from the wholesalers, adds its own cables and cooling, and sells the whole set-up to government offices and companies. For a few products it builds the box itself and puts its own name on it, called HexaData. Wholesalers keep most of the price, so the shop keeps about 13 paise on each rupee it sells. Government customers pay late, so the shop must keep money tied up in stock and unpaid bills. When box prices jump, the shop either eats the cost or, if it bought stock early, makes a bonus. The big hope is that more of the sales come from its own boxes, its cloud and its security work, which keep far more per rupee.

### Section 1 summary table

| Item | Read |
|---|---|
| Business type | Hybrid: hardware integrator and reseller with light assembly, plus small cloud, cybersecurity and international trading arms |
| Revenue nature | Transactional, project and tender based. 97.61% product sales |
| Asset intensity | Light to medium (PP&E 9.89 Cr; ZeaCloud capex rising) |
| WC intensity | High |
| Pricing power | Weak to price-taker today; the thesis claims it is changing (own-brand, GPU access) |

---

## SECTION 2: INDUSTRY DYNAMICS AND COMPETITIVE POSITION

### 2A Five forces

| Force | Plain answer | Helps / hurts |
|---|---|---|
| Competition | Many integrators and resellers; the PROSP peer table uses E2E Networks and Netweb (PROSP p.? peer table near line 5927; Netweb PE-based comparison), and global OEMs (Dell, HPE, Cisco) sell direct and through partners. Count NOT FOUND in the documents | Hurts |
| Entry barriers | Low for reselling (GeM registration, OEM partner tiers). Higher for HPC/GPU supply (NVIDIA tier) and NCIIPC accreditation. Capacity is not a barrier: "capacity and capacity utilisation not applicable" (PROSP p.148) | Hurts for core, neutral for HexaData, helps for Fluidech |
| Supplier power | Strong. Five distributors and OEMs supplied 52.35% of FY23 purchases, Ingram Micro alone 27.01% (PROSP p.142; derived from the top-five lines: 27.01+9.17+7.35+5.98+3.64). Component prices rose and Esconet could not pass them through in FY26 (Pres Jun26 slide 8) | Hurts |
| Customer power and concentration | Strong. Government 35.75% of FY23 revenue, top ten 53.72% (PROSP p.140, p.142-143). Tenders go to the lowest qualified bid (PROSP p.147-148). FY26 figures NOT FOUND | Hurts |
| Substitutes | Public cloud (AWS, Azure) can replace on-premise servers; Esconet itself resells it (PROSP p.130). Sovereign-cloud rules slow that substitution (Pres Jun26 slide 16) | Neutral |

### 2B Competitive positioning map

| Peer (from step 1 brief and PROSP) | What it is | Where Esconet sits against it | Anchor |
|---|---|---|---|
| Netweb Technologies | Own-brand HPC/AI server maker, NVIDIA partner; the TO state of the HexaData claim | Esconet's HexaData is a small own-brand line inside a mostly traded book. Own-brand share NOT FOUND | PROSP peer table (Netweb listed as peer); brief |
| Rashi Peripherals | IT hardware distributor; the FROM state. Also Esconet's supplier (9.17% of FY23 purchases) | Esconet's traded book looks like this, one step closer to the customer | PROSP p.142; brief |
| Orient Technologies | Listed IT infrastructure integrator, closest structural comp | Same model; comparison of margins and WC days is a Role 1 job | brief |
| E2E Networks | Cloud infrastructure; the ZeaCloud comparator | ZeaCloud is far smaller and loss-making in FY26 | PROSP peer table; AR26 p.151 |
| Ingram Micro, Redington, Tech Data | Distributors and suppliers | Supplier and competitor in one | PROSP p.142 |

Peer financials are not in my input set and I do not estimate them. Market share: NOT FOUND.

### 2C Moat assessment (eight standard types)

| Moat type | Evidence | Strength | Durability |
|---|---|---|---|
| Switching costs | Integration and AMC create some stickiness; seven-year Army cloud engagement (AR26 p.22 via B03). But 97.61% of revenue is one-off product sales, no recurring base disclosed | Weak | Low |
| Network effects | None evidenced | None | n/a |
| Cost advantage / scale | None. FY26 gross margin fell 2.0 points and purchases grew 58% vs revenue 54% (Pres Jun26 slide 8). Distributors and OEMs hold the cost advantage | None | n/a |
| Intangible assets (brand, accreditation) | HexaData brand (6,000+ units sold since 2018, Pres Sep25 slide 4); Red Hat certified HD-RS2200 (AR26 p.75); NCIIPC accreditation, "India's first" (Pres Jun26 slide 5, 13); NVIDIA Elite Partner (Pres Jun26 slide 5) | Weak to Moderate | Moderate for NCIIPC; partner tiers can be re-graded, so Low to Moderate |
| Efficient scale | Not applicable; no capacity limit | None | n/a |
| Regulatory | GeM OEM listing, MeitY empanelment only targeted (Pres Jun26 slide 12) | Weak | Low until empanelment is won |
| Supply access | NVIDIA Elite tier "privileged allocation of scarce GPUs" (Pres Jun26 slide 11). Management claim; no filed volume or margin evidence | Weak to Moderate (unproven) | Low to Moderate, depends on GPU cycle |
| Relationships / distribution | 500+ clients, 20+ sectors (Pres Sep25 slide 4); government panel access | Moderate | Moderate, but tenders reset every cycle |

Verdict: narrow. No moat is proven in the margin line today. The one test that would show a real moat is a sustained gross margin above the 13% to 15% traded level after component prices settle.

### 2D Industry lifecycle stage

| Item | Read |
|---|---|
| Industry stage | Growth, driven by AI and GPU compute: India data-centre systems spend +20.5% in 2026 (USD 9,385 Mn), IT services +11.1% (AR26 p.75) |
| Company position | Small participant in a fast-growing market, growing about 54% (consolidated revenue 23,029.80 to 35,440.48 Lakhs, AR26 p.133) with margins falling, i.e. growth is bought with margin and WC so far |
| Where growth comes from | Hardware price inflation as well as volume (Pres Jun26 slide 8, CALL26 via B03). Volume versus price split of revenue growth: NOT FOUND |

### 2E Key industry drivers

| Driver | Direction | Impact on Esconet |
|---|---|---|
| AI / GPU demand | Up | Revenue up, supply access matters; also lifts input prices (Pres Jun26 slide 8, 16) |
| Component price inflation | Up in FY26, management expects it to run through FY27 and maybe FY28 (CALL26 via B03) | Hurts margin if passed through slowly; can lift margin through inventory gain if stock was bought earlier |
| Data localisation and sovereign cloud | Up | Helps ZeaCloud if MeitY empanelment arrives (Pres Jun26 slide 12, 16) |
| Government digitisation | Up | Volume tailwind, slow payment headwind (PROSP p.77) |
| Cybersecurity and compliance spend (SEBI CSCRF) | Up | Helps Fluidech, still loss-making (Pres Sep25 slide 10; AR26 p.69) |
| Enterprise refresh cycles | Cyclical | Drives box volumes (Pres Jun26 slide 16) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A Ignore these, track these

| Common ratio | Why misleading or irrelevant here |
|---|---|
| EBITDA margin as reported (3.42% FY26) | Includes other income of 343.62 Lakhs (28.0% of EBITDA); ex other income the margin is 2.49% (AR26 p.76, p.133; B03). Always name the basis |
| Headline ROE and ROCE (Pres Sep25 slide 17 shows 21.90% and 16.63% for FY24 and FY25 on consolidated basis) | On a 2% to 3% margin business, ROCE is driven by asset turns, not quality; goodwill 851.11 Lakhs untested (B02) and FDR cash blur capital employed |
| Reported ratio table in the notes (DSCR 0.47x, current ratio) | DSCR not reproducible, ROE 0.39 impossible (B02 rank 13) |
| P/Sales or EV/Sales | A 97% resale business at 2% margin: sales is mostly someone else's product |
| Gross margin on its own, quarter to quarter | Moves with component prices and inventory timing; needs inventory-gain test (B03 FLAG-MARGIN-BASIS) |
| Headcount and revenue per employee | Pres Sep25 shows "70 people" (slide 4) and an employee chart of 40/50/60 (slide 18) that do not agree; pay is partly promoter family (B02) |
| Order pipeline "₹100 Cr+" | A pipeline, not a signed backlog (Pres Sep25 slide 19) |
| Operating cash flow as printed | FY26 standalone CFO 1,568.45 Lakhs includes 1,745.95 Lakhs FDR liquidation; ex-FDR it is (177.50) (B02 FLAG-CASH) |

### 3B Must-track metrics

Growth

| Metric | What it tells you | Healthy range (this industry) | Where to find | Red flag |
|---|---|---|---|---|
| Revenue by line (HexaData / traded / services / cloud / cyber) | Whether the mix shift is real | Own-brand plus services share rising each quarter | Concall, quarterly deck. Currently NOT FOUND | Management still does not disclose by line after the Q2 FY27 print |
| Services revenue share | Quality of revenue | Above 5% and rising (FY26: 2.39%) | Revenue note (AR26 p.143) | Flat or falling |
| Order book / backlog in ₹ | Visibility | Stated in rupees, with book-to-bill | Concall, deck. NOT FOUND | Never disclosed |
| Volume vs price split of growth | Real demand vs inflation | Volume growth positive | Concall. NOT FOUND | Growth is price only |

Profitability and efficiency

| Metric | What it tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Gross margin (consolidated; FY25 15.23%, FY26 13.19%, derived) | Pricing power vs input cost | Above 15% sustained after inventory is repriced | P&L: revenue less purchases plus inventory change (AR26 p.133) | Back below 13% |
| EBITDA margin ex other income (FY26 2.49%; Q1 FY27 7.03% per B03) | Real operating profit | Above 5% for two straight quarters (B03 monitorable) | Quarterly results | Q2 FY27 below 5% |
| Opex growth vs gross profit growth | Operating leverage | Opex grows slower than GP. FY26: GP +33.3%, employee plus other expenses +51.8% (derived from AR26 p.133) | P&L | Opex growing faster again |
| Other income share of PBT (FY26: 343.62 of 861.80 Lakhs = 39.9%; derived) | Earnings quality | Below 15% | Note 2.18 | Above 25% |

Balance sheet and risk

| Metric | What it tells you | Healthy range | Where to find | Red flag |
|---|---|---|---|---|
| Inventory days on net purchases (consolidated about 61 days FY26; derived: 5,149.87 / 30,764.85 x 365) | Stock bet size and price-gain risk | Falling or flat while revenue grows | Inventory note (AR26 p.141) | Rises with no matching order growth |
| Receivable days and over-six-month share (standalone 55.1 days; 19.9% over six months, B02) | Collection | Over six months below 10% | Ageing note 2.13.1 (AR26 p.112) | Above 20%, any first provision |
| CFO excluding FDR movements vs PAT | Cash conversion | CFO/PAT above 0.7 (B03) | Cash flow statement | Negative |
| Net debt including OD and FDR (debt 53.01 to 1,324.33 Lakhs, B03) | Funding strain | Debt falls as revenue grows | Notes 2.3, 2.5 | OD rolled again; delayed-payment interest above 5 Lakhs a half (30.63 Lakhs FY26) |

### 3C Industry-specific non-financial KPIs (system integrator / IT hardware)

| KPI | Why | Where to find |
|---|---|---|
| Order inflow and book-to-bill in ₹ | Visibility for a tender business | Concall, order-win filings. NOT FOUND in AR |
| Government vs private share of revenue | Drives payment delay and margin | Prospectus gave it to FY23 (35.75%); AR26 gives none |
| Top-10 customer and top-5 supplier share | Concentration | FY23 only (PROSP p.142-143); FY26 NOT FOUND |
| HexaData units shipped and average price | Own-brand traction | 6,000+ since 2018 (Pres Sep25 slide 4); annual units NOT FOUND |
| GPU allocation / NVIDIA tier status | Supply access | Pres Jun26 slide 5, 15; filing of 29 Apr 2026 (brief) |
| ZeaCloud utilisation, MeitY empanelment status | Cloud path | Pres Jun26 slide 12; NOT FOUND in numbers |
| Fluidech headcount, billing utilisation, NCIIPC-linked mandates | Cyber path | Pres Jun26 slide 13; NOT FOUND in numbers |
| Singapore customers, and goods location | Quality of 13.8% of revenue | NOT FOUND |

### 3D Unit economics

Unit: ₹100 of consolidated FY26 revenue (the business has no single unit price; the box differs per tender). Derived from the consolidated P&L (AR26 p.133, p.144).

| Line | FY25 (₹ per ₹100) | FY26 (₹ per ₹100) | Anchor |
|---|---|---|---|
| Revenue from operations | 100.00 | 100.00 | AR26 p.133 |
| Net bought-in goods (purchases less stock build) | 84.77 | 86.81 | purchases 19,988.85 / 31,591.57 less stock build 467.31 / 826.72 Lakhs |
| Gross profit | 15.23 | 13.19 | 3,508.26 / 4,675.63 Lakhs |
| Employees | 2.42 | 2.63 | 557.04 / 933.32 Lakhs |
| Other expenses (incl. outsourced service charges 2.93, sales and marketing 1.37, director pay incl. incentive 0.70 in FY26) | 8.43 | 8.07 | 1,941.62 / 2,860.70 Lakhs; AR26 p.144 |
| EBITDA excluding other income | 4.38 | 2.49 | 1,009.60 / 881.61 Lakhs |
| Other income | 1.28 | 0.97 | 295.29 / 343.62 Lakhs |
| Depreciation | 0.70 | 0.69 | 161.21 / 245.30 Lakhs |
| Finance cost | 0.35 | 0.33 | 81.53 / 118.13 Lakhs |
| PBT | 4.61 | 2.43 | 1,062.14 / 861.80 Lakhs |

- Volume drivers: government and enterprise refresh and AI capex, tender wins, GPU allocation.
- Price drivers: component prices, distributor margins, tender competition, the share of own-brand and service content.
- Cost drivers: bought-in goods (86.8%), service contractors, sales team, ZeaCloud depreciation (depreciation +52% in FY26).
- Incremental margin and operating leverage in FY26: revenue +12,410.68 Lakhs, gross profit +1,167.37 Lakhs (9.4% incremental gross margin), opex +1,295.36 Lakhs, so ex-other-income EBITDA fell 127.99 Lakhs. Leverage was negative in FY26 (derived from AR26 p.133). The Jun26 deck attributes about ₹7 Cr of gross profit to component inflation, plus Fluidech build-out and ZeaCloud depreciation (Pres Jun26 slide 8).
- Physics: every rupee of revenue brings 13 paise of gross profit, so a 1 point change in gross margin on ₹354 Cr of revenue is about ₹3.5 Cr of EBITDA against reported EBITDA ex other income of ₹8.8 Cr. Margin is therefore the whole story; volume matters little unless the mix changes.
- Q1 FY27: standalone gross margin 29.2% vs 13.7% FY26, consolidated ex other income EBITDA 7.03% (B03 monitorables, FLAG-MARGIN-BASIS). Two readings. (1) Structural: own-brand HexaData, services and AI systems carry far higher gross margin, and they are now a bigger part of sales. (2) Transitory: stock bought before the component price jump is being sold at the new, higher prices, a holding gain that stops when stock is replaced; MD links part of the margin to hardware price volatility and inventory (CALL26 p.10, p.12 via B03). One observation separates them: gross margin by line (HexaData revenue and margin disclosed), or Q2 FY27 gross margin after stock replaced at new prices. A deliverable-based test: does the 29.2% hold when inventory days stay flat. I state the evidenced path as unresolved, and the conservatism belongs in position size, not in this input.

---

## SECTION 4: RISKS, VALUATION APPROACH AND MONITORING

### 4A Risks and first deteriorating line

| Category | Risk | First line item to deteriorate |
|---|---|---|
| Revenue model | Project-based, tender-based sales with no disclosed backlog; government and top-ten customer concentration (FY23: 35.75%, 53.72%) | Revenue per quarter and order inflow; first sign is sales falling quarter on quarter, and standalone revenue already -18% vs the FY26 quarterly average in Q1 FY27 (B03) |
| Revenue model | Intra-group sales: parent sold 568.79 Lakhs to ZeaCloud, 106.4% of ZeaCloud turnover, with no profit elimination (B02) | Consolidated revenue quality; parent sales to Zeacloud as % of Zeacloud turnover |
| Margin | Component price swings and inventory gain reversal (Pres Jun26 slide 8; CALL26 via B03) | Gross margin line (revenue less purchases plus stock change) |
| Margin | Price-taker in tenders (PROSP p.77 "competitive pricing") | Gross margin in government-heavy quarters |
| Margin | Subsidiary drag: Zeacloud PAT 110.82 to (10.04) Lakhs, Fluidech PBT (68.01) Lakhs (AR26 p.69; B03) | Depreciation and employee cost |
| Balance sheet | Slow government receivables, 893.06 Lakhs (19.9%) over six months, no provision (B02) | Over-six-month ageing bucket, then provision |
| Balance sheet | Inventory build funded by OD; inventory 2,428.94 Lakhs consolidated gap unreconciled (B02) | Inventory change; OD balance; delayed-payment interest (30.63 Lakhs FY26) |
| Balance sheet | Goodwill 851.11 Lakhs with no impairment test; Fluidech loss-making (B02) | Impairment charge in AR27 |
| Execution | MeitY empanelment for ZeaCloud and Fluidech breakeven are plans, not facts (Pres Jun26 slide 12-13, 17) | ZeaCloud and Fluidech quarterly loss |
| Execution | Funding gap: 552.69 Lakhs of warrant money not received, use of proceeds cut (B02) | Cash and OD |
| Structural | Distributor and OEM supplier power (Ingram 27.01% of FY23 purchases, PROSP p.142); OEMs can sell direct | Purchases growth vs revenue growth (FY26: +58% vs +54%, Pres Jun26 slide 8) |
| Structural | Disclosure gaps: no segment data, no line revenue, summons and tax demand not in AR (B03 flags) | Next AR notes |

### 4B Valuation method applicability

| Method | Applicable? | Why |
|---|---|---|
| P/E on normalised earnings | Yes, PRIMARY | Profitable, cash-generating enough to have positive PAT (FY26 PAT 6.16 Cr, AR26 p.76). Must use ex-other-income, destination-mix margin (Section 1B governs the exit PE) |
| EV/EBITDA ex other income | Yes, SECONDARY | Cross-check against Orient Technologies, Rashi, Netweb for the same business model; strips capital-structure noise from OD |
| EV / gross profit | Cross-check only | Reseller models are compared on gross profit; useful until margin basis settles |
| SOTP (hardware core, ZeaCloud, Fluidech, Singapore) | TERTIARY, only when line disclosure exists | Needs HexaData, cloud and cyber revenue and margin, all NOT FOUND today |
| DCF | Not applicable now | CFO ex-FDR negative on six-year basis; no reliable free cash flow (B02, B03) |
| P/B or net worth | Not applicable | Goodwill 851.11 Lakhs untested, net worth overstated about 209 Lakhs on derived basis (B02); not an asset play |
| EV/Sales or P/S | Not applicable | 97% resale at 2% to 3% margin |
| DDM | Not applicable | No dividend policy evidence |
| NAV or replacement cost | Not applicable | |

Primary: P/E on normalised earnings. Secondary: EV/EBITDA excluding other income. Tertiary: SOTP, once line disclosure exists. Cycle stage that matters: the component price cycle and GPU capex cycle, because gross margin follows them. Value on mid-cycle gross margin, not on Q1 FY27.

Sector cap row (manifest "Cybersecurity / VAD", 25x). My read supports this row as the nearest existing row. Reasons: 97.61% of revenue is resale and integration of third-party hardware, which is value-added reseller economics (AR26 p.143); cybersecurity is only Fluidech, 1.52% of revenue and loss-making (B02; derived). The cap table has no hardware-integrator row. "Platform / SaaS / IT services" 45x is not supported: services are 2.39% of revenue (AR26 p.143). "Data centers / cloud infrastructure" 30x applies only to a ZeaCloud slice that is not separately disclosed. "Telecom equipment" 30x does not fit: HexaData is a small own-brand line, not an equipment maker at scale. The row stays as a ceiling; with margins at 2.5% to 7%, the pillar-built PE, not the cap, is likely to bind. The manifest is not changed by me.

### 4C Quarterly monitoring checklist (10-15 items)

| # | Item | Good | Trouble |
|---|---|---|---|
| 1 | Gross margin, consolidated and standalone | Holds above 20% standalone after stock replaced (B03: Q1 29.2%) | Falls back toward 13% |
| 2 | EBITDA ex other income | At or above 5% in Q2 FY27 (B03) | Below 5% |
| 3 | Other income and the 184.23 Lakhs forfeiture treatment | Named and below 5% of total income | Unexplained, large |
| 4 | Revenue by line (HexaData, services, cloud, cyber) | Disclosed, with own-brand and services share rising | Still NOT FOUND |
| 5 | Order inflow and backlog in ₹ | Disclosed and book-to-bill above 1 | Only "strong pipeline" language |
| 6 | Inventory days and quarterly stock change | At or below 60 days; no build above 500 Lakhs (B03) | Large build without orders |
| 7 | Receivables over six months | Below 10%; first provision made | Above 20% |
| 8 | CFO ex-FDR | Positive; CFO/PAT above 0.7 | Negative |
| 9 | Debt and delayed-payment interest | Debt falls; interest under 5 Lakhs a half-year | OD rolled; interest keeps rising |
| 10 | Fluidech PBT | Breakeven | Loss widens |
| 11 | ZeaCloud PAT and MeitY empanelment | PAT above zero; empanelled | PAT negative; no empanelment |
| 12 | Parent sales to ZeaCloud | Below 50% of ZeaCloud turnover | Above 100% again |
| 13 | Singapore: revenue, margin, audited total assets | Reconciled (553.64 vs about 2,465 Lakhs, B03) | Still unreconciled |
| 14 | Government share and top-ten customers | Disclosed | Not disclosed |
| 15 | Summons follow-up and s.156 demand status | No new filing; disclosed | New Reg 30 filing |

### 4D Questions for management

| # | Question | Answer that reassures | Answer that worries |
|---|---|---|---|
| 1 | Revenue and gross margin of HexaData, services, cloud and cybersecurity for FY26 and Q1 FY27? | Numbers given, own-brand mix up | Refuses or gives only growth rates |
| 2 | How much of the Q1 FY27 gross margin of 29.2% is stock bought before the price rise, and what is the margin on stock replaced at new prices? | Replaced-stock margin near Q1 level | Margin depends on old stock |
| 3 | What is signed order backlog in ₹ and how much is government? | Backlog above one quarter of revenue, private share rising | No number; government above 35% |
| 4 | What does Esconet Singapore sell, to whom, where is its stock, and why does its audited total assets differ from the AOC-1 value? | Named customers, reconciled balance sheet | No customer data; reconciliation absent |
| 5 | Pres Jun26 slide 8 says vendors were paid on time, but the AR shows delayed-payment interest of 30.63 Lakhs (vs 1.15) and 17.65 Lakhs on statutory dues (AR26 p.115). Which is right? | Items dated and one-off | Recurring |
| 6 | ZeaCloud: the Chairman says asset-light (AR26 p.13), the MD says asset-heavy (CALL26 p.18). What is its capex plan, utilisation and revenue outside the parent? | Third-party revenue above 50%, capex staged on contracts | Parent still above 100% of turnover |
| 7 | Guidance: the deck gives no growth number (slide 17). What revenue and margin are management working to for FY27, and how did FY26 compare with the June 2025 outlook? | Numeric, dated target | Only direction words |

---

## SECTION 5: ONE-PAGE SUMMARY CARD

```
+--------------------------------------------------------------------------+
| ESCONET TECHNOLOGIES LTD (ESCONET)                      run 2026-10-05   |
+--------------------------------------------------------------------------+
| Business type     Hybrid: hardware integrator/reseller + light assembly  |
| Revenue nature    Transactional, tender-based; 97.61% product sales,     |
|                   2.39% services (AR26 p.143, ₹ Lakhs)                   |
| Asset intensity   Light to medium (PP&E 9.89 Cr; ZeaCloud capex rising)  |
| WC intensity      High (inventory, slow govt receivables, OD funding)    |
| Pricing power     Weak / price-taker today; own-brand claim unproven     |
| Cyclicality       Cyclical (component price cycle, GPU capex cycle)      |
| Moat              Narrow: NVIDIA tier, NCIIPC, HexaData brand, GeM       |
| Line mix          HexaData / cloud / cyber revenue: NOT FOUND            |
| Gross margin      15.23% FY25 -> 13.19% FY26 (derived, AR26 p.133)       |
+--------------------------------------------------------------------------+
| PRIMARY valuation   P/E on normalised (ex other income) earnings         |
| SECONDARY           EV/EBITDA ex other income vs Orient, Rashi, Netweb   |
| TERTIARY            SOTP, only once line disclosure exists               |
| Sector cap row      Cybersecurity / VAD 25x: supported as nearest row    |
+--------------------------------------------------------------------------+
| TOP 5 TRACK:  1 gross margin after stock replaced (hold above 20% sa.)   |
|               2 EBITDA ex other income (5% or more)                      |
|               3 revenue by line / own-brand and services share           |
|               4 CFO ex-FDR and receivables over 6 months (below 10%)     |
|               5 inventory days (60 or fewer) and OD/delay interest       |
+--------------------------------------------------------------------------+
| VERDICT  A thin-margin hardware integrator that claims a mix shift the   |
|          documents do not yet let anyone measure.                        |
+--------------------------------------------------------------------------+
```

Analyst conclusion on the load-bearing question. The business is a 97.61% product-resale model with 13.19% gross margin in FY26. The AR, both decks and the prospectus give no revenue or margin by HexaData, cloud or cybersecurity. Therefore the Q1 FY27 margin jump cannot be assigned to mix from these documents. A mix reading and an inventory-gain reading both fit; management itself ties part of the margin to price volatility and stock (CALL26 p.10, p.12 via B03). The separating observation is line-level disclosure or Q2 FY27 gross margin after stock replacement.

Contradictions between company documents that the reader should hold in mind: (1) "asset-light" ZeaCloud (AR26 p.13) vs "asset-heavy depreciation" (Pres Jun26 slide 8); (2) "vendors paid on time" (Pres Jun26 slide 8) vs interest on delayed supplier payment 30.63 Lakhs (AR26 p.115); (3) "inventory backed by demand" (Pres Jun26 slide 9) vs unreconciled inventory gap 2,428.94 Lakhs (B02); (4) "ZeaCloud healthy operations" (Pres Jun26 slide 12) vs PAT (10.04) Lakhs (AR26 p.151). The receivable fall of ₹8.5 Cr (Pres Jun26 slide 9) does match the standalone ageing totals (5,343.98 to 4,499.21 Lakhs, B02).

```yaml
stage: B04-bizmodel
company: "ESCONET"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "BSE scrip code not found on screener page; announcements/ empty. REPAIRED by /step1: 33 NSE Reg 30 filings Sep 2025 to Sep 2026; filings before Sep 2025 not collected."
  - "shareholding/ empty (no automated source). REPAIRED by /step1: NSE SHP XBRL Mar-2026 and Jun-2026 plus text extracts."
  - "screener export sheets EMPTY (P&L, Quarters, Balance Sheet, Cash Flow, Customization); Data_Sheet.csv populated; screener history FY2023-FY2026 plus Q1 FY27 only."
  - "no results PDFs from screener. REPAIRED by /step1: H1 FY26, FY26 audited, Q1 FY27 board outcomes."
  - "no rating PDF. REPAIRED by /step1: CRISIL rationale 2026-07-02 as text; 2024 and 2025 rationales not collected."
  - "only 2 concalls. OVERRIDDEN by /step1: concalls_available true on 2 transcripts (Jun 2025, Aug 2026); 22 Jun 2026 investor meet has deck but no transcript; no H1 FY26 call."
  - "annual-report: FY2023-24 AR not collected (two-most-recent rule); prospectus covers pre-IPO years."
  - "research/ empty, no broker notes."
  - "prospectus: final prospectus held; near-identical RHP moved to inputs/other/."
  - "announcements: SAST disclosure 2026-05-19 scanned; .txt corrupt, OCR failed; read PDF page directly."
  - "shareholding and rating XBRL/HTML originals kept beside text extracts, committed by hand by /step1."
  - "listed_date: exact NSE Emerge listing date NOT FOUND in corpus (AR Note 1 p.105 says 23 Feb 2024; prospectus dated 2024-02-20)."
  - "EMPTY-FOLDER CONFIRMATION suppressed by /step1 AUTONOMY CONTRACT; standing answer proceed with gaps. Empty at stage 0: research/."
  - "pass1 gap: FY24 AR not read, so FY24 purchases and FY24 payable days NOT FOUND; FY24 receivable days taken from FY25 AR comparatives."
  - "pass1 gap: consolidated ageing tables (Notes 2.13.1 and 2.6.1 cited on p.142 and p.140) NOT FOUND IN DOCUMENT."
  - "pass2 gap: Fluidech acquisition-date balance sheet and purchase agreement NOT FOUND; goodwill working, consolidation method and swap/cash price valuation basis NOT FOUND."
  - "pass2 gap: Zeacloud and Singapore stand-alone accounts not in corpus (Singapore audited by other auditors, FY26 AR p.127); Singapore total assets conflict: AOC-1 SGD 33,89,867 (about 2,465 Lakhs at 72.72) vs auditor 553.64 Lakhs."
  - "pass2 gap: preferential issue allottee list, lender list for the 247.95 repayment object, OD facility rate/limit/covenants, FDR lien and maturities, advance tax paid in FY26: all NOT FOUND."
  - "pass2 note: FY25 AR and the Reg 30 filing of 28 Feb 2026 were read for cross-reference only; no figure from them enters the Pass 1 base."
  - "stage3: Q1 FY27 other income split and the accounting of the 184.23 Lakhs warrant forfeiture NOT FOUND in the results filings read (note says only interest income, gain on sale of PPE and miscellaneous income)."
  - "stage3: Fluidech s.156 income tax demand of 235.16 Lakhs (AY 2021-22, per prospectus) current status NOT FOUND; not in FY26 AR."
  - "stage3: per-director Board and committee attendance NOT FOUND (extract lost the Present markers); other directorships NOT FOUND."
  - "stage3: HexaData, services, cloud and cybersecurity revenue and margin NOT FOUND; FY26 customer concentration NOT FOUND; order book value NOT FOUND."
  - "stage3: NSE PDF vs XBRL EPS discrepancy not verifiable from the AR; one EPS mismatch between filings found (standalone FY25 basic 5.26 vs 5.43)."
  - "stage4: investor presentations provided (Jun 2026 and Sep 2025); neither gives revenue or margin by HexaData, cloud or cybersecurity. AR26 reports one segment (AR26 p.76). Only the products vs service-charges split exists (AR26 p.143)."
  - "stage4: Q1 FY27 results filing and Aug 2026 concall transcript not in this stage's inputs; concall facts are carried from B03 (CALL26) and labelled as such."
  - "stage4: Singapore customers, goods location and share of inventory NOT FOUND; FY26 government share, top-ten customers, supplier concentration NOT FOUND (prospectus covers to FY23 and H1 FY24 only)."
  - "stage4: peer financials (Netweb, Rashi, Orient, E2E) not in this stage's inputs; no peer margin or multiple stated."
flags:
  - {type: FLAG-MIX-NOT-DISCLOSED, reason: "Q1 FY27 margin jump cannot be assigned to HexaData, services, cloud or cyber mix: no line revenue or margin in AR26, decks or prospectus. Only products 97.61% vs service charges 2.39% (AR26 p.143, Lakhs; derived). Two readings carried: structural mix, or inventory/price holding gain. Separating observation: line disclosure or Q2 FY27 gross margin after stock replaced."}
  - {type: FLAG-DECK-VS-FILING, reason: "Four company statements conflict with filed numbers: vendors paid on time (Pres Jun26 slide 8) vs delayed-supplier interest 30.63 vs 1.15 Lakhs (AR26 p.115); ZeaCloud asset-light (AR26 p.13) vs asset-heavy (Pres Jun26 slide 8; CALL26 p.18); ZeaCloud healthy (slide 12) vs PAT (10.04) Lakhs (AR26 p.151); inventory backed by demand (slide 9) vs 2,428.94 Lakhs unreconciled inventory gap (B02)."}
  - {type: FLAG-MODEL-WC, reason: "Net purchases 86.81% of revenue, gross margin 13.19% falling from 15.23% (derived, AR26 p.133). FY26 operating leverage negative: gross profit +1,167.37 Lakhs, opex +1,295.36 Lakhs, ex-other-income EBITDA 1,009.60 to 881.61 Lakhs. Government buyers pay slowly and need FDR-funded guarantees (PROSP p.77)."}
  - {type: FLAG-SINGAPORE-THIN, reason: "Singapore is about 13.8% of revenue at 0.52% net margin (PAT 25.57 on revenue 4,905.58 Lakhs; B02, AR26 p.151, derived); customers, stock location and total-assets reconciliation NOT FOUND."}
  - {type: FLAG-SECTOR-ROW, reason: "Manifest row Cybersecurity / VAD 25x is supported as the nearest existing row (97.61% resale and integration; cyber is Fluidech, 1.52% of revenue, loss-making). No hardware-integrator row exists. Platform/SaaS/IT services 45x not supported (services 2.39%). Cap is a ceiling; margins are likely to bind first. Manifest unchanged."}
business_type: hybrid
revenue_streams:
  - {name: "Sales of IT products (traded and integrated hardware, HexaData own-brand, Singapore trading; line split NOT FOUND)", type: "transactional, project/tender-based product resale with light assembly", pct_of_revenue: 97.61, predictability: "Low to Medium (AR26 p.143, consolidated FY26: 34,593.19 of 35,440.48 Lakhs; derived)"}
  - {name: "Service charges (integration, AMC, managed services, parts of cloud and cyber)", type: "services, project and recurring mix", pct_of_revenue: 2.39, predictability: "Medium (AR26 p.143: 847.30 of 35,440.48 Lakhs; FY25 0.65%)"}
  - {name: "HexaData own-brand (inside products line)", type: "product / assembly", pct_of_revenue: "NOT FOUND, check concall or investor presentation", predictability: "Low to Medium"}
  - {name: "ZeaCloud and Fluidech (inside the two lines above)", type: "subscription and services", pct_of_revenue: "NOT FOUND as line; Fluidech turnover 538.96 Lakhs = 1.52% of consolidated revenue (B02; derived)", predictability: "Medium"}
asset_intensity: medium
wc_intensity: high
pricing_power: weak
cyclicality: cyclical
moats_present:
  - "Intangible: HexaData brand, Red Hat certification of HD-RS2200 (AR26 p.75), 6,000+ units since 2018 (Pres Sep25 slide 4). Strength weak to moderate; durability low to moderate"
  - "Accreditation: Fluidech NCIIPC, India's first (Pres Jun26 slide 5, 13). Moderate; durability moderate"
  - "Supply access: NVIDIA Elite Partner tier, privileged GPU allocation (Pres Jun26 slide 11). Management claim, unproven in margin; durability low to moderate"
  - "Relationships and government panel access: 500+ clients (Pres Sep25 slide 4), GeM OEM listing (AR26 p.75). Moderate; resets every tender cycle"
  - "Overall verdict: narrow; no moat proven in the margin line (gross margin 13.19% FY26, AR26 p.133)"
valuation_methods:
  primary: {method: "P/E on normalised earnings (ex other income, mid-cycle gross margin; Section 1B governs the exit PE)", why: "Positive PAT (FY26 6.16 Cr, AR26 p.76) and a margin-driven model; FCF and book value are not reliable"}
  secondary: {method: "EV/EBITDA excluding other income vs Orient Technologies, Rashi Peripherals, Netweb", why: "Same-model cross-check that removes OD and other-income noise; EV/gross profit as supporting view"}
  tertiary: {method: "SOTP (hardware core, ZeaCloud, Fluidech, Singapore)", why: "Only when line revenue and margin are disclosed; all NOT FOUND today"}
  not_applicable:
    - "DCF: six-year CFO negative, FY26 CFO ex-FDR (177.50) Lakhs (B02)"
    - "P/B or net worth: goodwill 851.11 Lakhs untested, derived overstatement about 209 Lakhs"
    - "EV/Sales or P/S: 97% resale at 2.5% margin"
    - "DDM: no dividend evidence"
    - "NAV or replacement cost"
irrelevant_ratios:
  - "Reported EBITDA margin 3.42%: includes other income 28.0% of EBITDA; ex other income 2.49%"
  - "Headline ROE and ROCE: asset-turn driven at 2% to 3% margin; goodwill and FDR cash blur capital employed"
  - "Notes ratio table (DSCR 0.47x, ROE 0.39): not reproducible"
  - "EV/Sales and P/S: mostly someone else's product"
  - "Single-quarter gross margin: moves with component prices and inventory timing"
  - "Revenue per employee: headcount figures conflict across the Sep 2025 deck (70 vs 40/50/60 chart)"
  - "Order pipeline of 100 Cr+: a pipeline, not a signed backlog"
  - "Reported CFO: FY26 standalone includes 1,745.95 Lakhs FDR liquidation"
must_track_metrics:
  - {metric: "Gross margin after stock replaced at new prices (standalone and consolidated)", healthy: "Consolidated above 15%; standalone Q1 FY27 29.2% holds above 20% (B03)", red_flag: "Back toward 13% (FY26 13.19%) or depends on old stock"}
  - {metric: "EBITDA margin excluding other income", healthy: "5% or more for two straight quarters (FY26 2.49%; Q1 FY27 7.03%)", red_flag: "Q2 FY27 below 5%"}
  - {metric: "Revenue by line: HexaData, services, cloud, cyber (and order backlog in rupees)", healthy: "Disclosed; services above 5% of revenue and rising (FY26 2.39%)", red_flag: "Still NOT FOUND after Q2 FY27"}
  - {metric: "CFO excluding FDR movements, and receivables over six months", healthy: "CFO/PAT above 0.7; over six months below 10%", red_flag: "CFO ex-FDR negative; over six months above 20% (FY26 19.9%); any first provision"}
  - {metric: "Inventory days and OD/delayed-payment interest", healthy: "Inventory days at or below 60; delay interest under 5 Lakhs a half-year", red_flag: "Stock build above 500 Lakhs a quarter without orders; delay interest above FY26 30.63 Lakhs run-rate"}
unit_economics:
  unit: "₹100 of consolidated revenue (no single product unit; tenders differ)"
  revenue_per_unit: "100.00"
  margin_per_unit: "FY26: gross profit 13.19, ex-other-income EBITDA 2.49, PBT 2.43 per ₹100 (AR26 p.133, p.144, Lakhs; derived). FY25: 15.23, 4.38, 4.61"
  key_lever: "Gross margin mix and pricing: 1 point on about ₹354 Cr revenue is about ₹3.5 Cr EBITDA vs ex-other-income EBITDA of ₹8.8 Cr. FY26 operating leverage was negative (GP +1,167.37 Lakhs vs opex +1,295.36 Lakhs)"
first_deterioration_signals:
  - {risk: "Revenue model: project/tender sales, no disclosed backlog, government and top-ten concentration", first_signal: "Quarterly revenue and order inflow; standalone revenue already -18% vs FY26 quarterly average in Q1 FY27 (B03)"}
  - {risk: "Margin: component price swings, inventory gain reversal", first_signal: "Gross margin line (revenue less purchases plus stock change)"}
  - {risk: "Balance sheet: slow government receivables, OD-funded stock", first_signal: "Over-six-month receivables bucket (893.06 Lakhs, 19.9%) and delayed-payment interest"}
  - {risk: "Execution: ZeaCloud, Fluidech and MeitY plans not delivered", first_signal: "Subsidiary losses and depreciation; ZeaCloud PAT (10.04) Lakhs, Fluidech PBT (68.01) Lakhs"}
  - {risk: "Structural: supplier power of distributors and OEMs", first_signal: "Purchases growing faster than revenue (FY26 +58% vs +54%, Pres Jun26 slide 8)"}
  - {risk: "Quality: intra-group sales and goodwill", first_signal: "Parent sales to Zeacloud vs Zeacloud turnover (568.79 Lakhs = 106.4%); goodwill 851.11 Lakhs impairment"}
mgmt_questions:
  - "What are FY26 and Q1 FY27 revenue and gross margin for HexaData, services, cloud and cybersecurity?"
  - "How much of the Q1 FY27 standalone gross margin of 29.2% is stock bought before the price rise, and what is the margin on stock replaced at new prices?"
  - "What is the signed order backlog in rupees, and how much is government?"
  - "What does Esconet Singapore sell, to whom, where is its stock, and why do audited total assets (553.64 Lakhs) differ from AOC-1 (about 2,465 Lakhs)?"
  - "The June 2026 deck says vendors were paid on time; the AR shows 30.63 Lakhs delayed-payment interest and 17.65 Lakhs on statutory dues. Which is right?"
  - "ZeaCloud: asset-light (Chairman) or asset-heavy (MD)? Capex plan, utilisation, third-party revenue?"
  - "What numeric revenue and margin is management working to for FY27, given the deck gives no growth number, and how did FY26 compare with the June 2025 outlook?"
one_line_verdict: "A thin-margin hardware integrator (97.61% product resale, 13.19% gross margin) whose claimed shift to own-brand, cloud and cyber mix cannot be measured from any document in the corpus."
analyst_note: "Sector cap: the manifest row Cybersecurity / VAD 25x is supported as the nearest existing row, because 97.61% of revenue is resale and integration; cyber is Fluidech, 1.52% of revenue and loss-making. No hardware-integrator row exists, so no better row is available. The cap is a ceiling: with margins between 2.5% and 7%, the pillar-built PE will likely bind first. Q1 FY27 margin: the evidenced path is unresolved. Reading one is structural mix; reading two is a stock-gain from pre-inflation inventory (MD ties part of margin to price volatility and stock, CALL26 p.10, p.12 via B03). Separating observation: revenue and gross margin by line, or Q2 FY27 gross margin after stock replacement. Put the conservatism in position size, not in the input. Gross margin (not volume) drives value: 1 point is about ₹3.5 Cr EBITDA."
```
