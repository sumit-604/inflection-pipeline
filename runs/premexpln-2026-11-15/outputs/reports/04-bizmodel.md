# Stage 4 Business Model Decoder: PREMEXPLN (Premier Explosives Ltd)
Run: premexpln-2026-11-15 | Model: claude-sonnet-5-5 | Sources: Annual_Report_2026.txt (46th AR), Investor_Presentation_1.txt (Q2 FY27, 12 Nov 2026), 20261112-Q2FY27-results.txt, B03 report.

Conventions. AR anchors: "AR p.N" = the "[page N]" marker in the .txt (printed page = N minus 3). MD&A figures print "Rs million" (mn); statements and notes print "INR lakhs" (L, 100 L = 1 Cr). Presentation anchors use the "[page N]" marker (the PDF page; the printed slide number is one lower). No unit is converted silently. "(derived)" marks my arithmetic on filed numbers. [INFERENCE] marks a link the filing does not state. Brief items and web leads are COMPANY MEMORY and are not used as evidence here.

---
## 0. SECTOR-CAP EVIDENCE FOR STAGE 0 (reported, no multiple chosen)

B00 reading (a) Defence / strategic 38x; reading (b) Specialty chemicals 35x. The separating observation named by B00 is the filed segment revenue and segment result split.

| Evidence | Figure | Anchor |
|---|---|---|
| FY26 revenue split | Defence & Space Rs 3,154 mn (81%); Commercial Explosives Rs 729 mn (19%); total Rs 3,883.4 mn | AR p.25 (MD&A 5.1, 5.2, 7) |
| FY26 split, BRSR basis | 81.22% / 18.78% | B03 report citing BRSR AR p.71 (not re-read here) |
| Q2 FY27 revenue split | Defence & Space Rs 1,246 mn; Commercial Explosives Rs 207 mn; total Rs 1,453 mn. Defence share 85.8% (derived); company prints 86% / 14% | Inv. Pres. p.7 and p.12 |
| H1 FY27 split | Defence & Space Rs 2,038 mn (82.2%, derived); Commercial Rs 440 mn (17.8%, derived); total Rs 2,478 mn | Inv. Pres. p.7 |
| Q2 FY26 split | Defence & Space Rs 632 mn (83.6%, derived); Commercial Rs 124 mn (16.4%, derived) | Inv. Pres. p.7 |
| Order book, May 2026 | Rs 15,690 mn: Defence about 95%, Explosives about 2%, Services about 3% | AR p.25 (MD&A 6) |
| Order book, Oct 2026 | Rs 16,420 mn (4.23x FY26 revenue): Defence 96%, Explosives 2%, Services 2% | Inv. Pres. p.8 |
| Services (O&M) revenue | "Sale of services" Rs 3,593.78 L = 9.3% of FY26 revenue (derived); the company folds O&M into the Defence & Space segment | AR p.133 (Note 21); AR p.25 (5.1) |
| Exports | Other countries Rs 5,168.78 L = 13.3% of FY26 revenue (derived); FY25 Rs 7,848.01 L | AR p.133 (Note 21) |
| Segment result or margin | NOT FOUND. One reportable segment under Ind AS 108, no segment profit, in the AR, the Q2 FY27 results filing and the presentation | AR p.113 (Note 2.2, per B03); Q2 results filing lines 255 and 510; Inv. Pres. p.6 to p.7 (no segment margin) |
| Company-level margin | EBITDA margin 10.0% FY26 (AR p.25); 11.9% Q2 FY27, 9.3% H1 FY27 (Inv. Pres. p.6) | as shown |

What the evidence says. Revenue and order book both lean to Defence (81% to 86% of revenue, 95% to 96% of order book). The segment result, the observation that separates the readings, does not exist in any filed document. So the filing does not show where the earnings come from. Two further facts bear on it. First, FY26 PAT was 64.8% non-recurring other income (B03, AR p.133, p.139), so operating earnings are thin. Second, Commercial Explosives order cover is short: about Rs 328 mn of Explosives order book (2% of 16,420, derived from rounded percentages) against Rs 729 mn of FY26 revenue, about 0.45x, so that revenue is mostly book-and-ship. Defence cover is about 4.7x its FY26 revenue (95% of 15,690 = 14,906 over 3,154, derived). No text states that Commercial Explosives earns a higher or lower margin than Defence. Hence the separating observation stays open. It stays open until the FY27 results carry a segment result, or a concall states the margin by segment. The Q2 FY27 concall transcript is absent (B00 gap).

Mix drift. Defence share of revenue: FY25 80.8% (3,374 of 4,174.5 mn, derived) to FY26 81.2% to Q1 FY27 77.3% (793 of 1,026, derived) to Q2 FY27 85.8%. No steady trend. The Commercial segment grew 39% in H1 FY27 (Inv. Pres. p.7).

---
## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A One line
Premier Explosives makes the explosive and fuel material inside missiles, rockets and flares for the Indian state and its contractors, plus mining explosives, and runs two government propellant plants for a fee (AR p.24 to p.25; Inv. Pres. p.12).

### 1B Money flow chain per revenue stream
| Stream | Input | What the company does | What it delivers | Who pays | How they pay |
|---|---|---|---|---|---|
| Defence products (propellants, igniters, rocket motors, chaff and flares, warheads) | Specialised chemicals, energetic inputs (AR p.24, p.26); supplier advances Rs 2,115.95 L (B03) | Mixes, casts, tests, integrates; customer inspects at milestones | Booster and sustainer grains, pyrogen igniters, countermeasures, assembled rocket motors (Inv. Pres. p.14, p.20) | BDL, DRDO, ASL, Brahmos Aerospace, defence PSUs; foreign buyers for exports (Inv. Pres. p.20, p.14) | Milestone and inspection based; customer advances Rs 6,622.26 L (17.1% of revenue, B03); receivables from PSUs (AR p.100 KAM, per B03) |
| Defence O&M services | Plant labour and process know-how | Runs the solid propellant plants at ISRO Sriharikota (since 2006) and ASL Jagdalpur (17 years) (Inv. Pres. p.14) | Operated plant, propellant output | ISRO, DRDO/ASL | Contract fee. Fee basis NOT FOUND, check concall. Revenue is on "output basis" (Note 2.5, per B03) |
| Commercial explosives | Ammonium-nitrate based inputs, detonator components (input detail NOT FOUND, check concall) | Makes bulk explosives, cast boosters, detonators, detonating fuse at Singrauli, Chandrapur, Godavarikhani, Manuguru, Peddakandukur (Inv. Pres. p.13, p.15) | Blast products to mines, infrastructure, cement; exports (Inv. Pres. p.13) | Mining and cement customers; tender-priced (AR p.24 3.4) | Customer name and credit terms NOT FOUND; one customer is 10% or more of total revenue, unnamed (AR p.133) |

### 1C Revenue model classification
| Stream | Type | Description | % of revenue (anchor) | Predictability |
|---|---|---|---|---|
| Defence products | Project and milestone-based, build-to-order | Delivery against government orders; revenue at point in time on delivery (B03 Note 2.5) | Defence & Space 81% includes O&M (AR p.25). Products alone: sale of products Rs 34,874.95 L = 89.8% of total, but this includes Commercial (AR p.133, derived) | Medium. MD&A says revenue "may remain uneven across quarters" (AR p.26). FY26 Q4 Rs 677 mn, 9M Rs 2,477 mn (B03 derived from AR p.12, p.25) |
| Defence O&M services | Contract services, recurring | Plant operation for ISRO and ASL | Sale of services 9.3% (Rs 3,593.78 L; AR p.133, derived); order book share 2% to 3% (AR p.25; Inv. Pres. p.8) | High [INFERENCE: long-running contracts since 2006, renewal terms NOT FOUND] |
| Commercial explosives | Repeat product sales, tender and spot | Mining and cement supply | 19% (Rs 729 mn; AR p.25); 14% in Q2 FY27 (Inv. Pres. p.12) | Low to medium. Order cover about 0.45x of annual revenue (derived above) |
| Exports (cuts across both) | Export orders, licence-gated | Defence and industrial exports | 13.3% of FY26 revenue (AR p.133). Share of order book NOT FOUND in filed documents | Low. Foreign revenue fell 34.1% in FY26 (B03 from AR p.133) |

Cross-check: sale of products 34,874.95 + traded goods 238.41 + services 3,593.78 + other operating 127.00 = 38,834.14 L (AR p.133).

### 1D Business model canvas
| Element | Answer | Anchor |
|---|---|---|
| What they sell | Energetic materials and devices for missiles, rockets, countermeasures, mining | AR p.24 to p.25 |
| Who buys | Defence and space PSUs (BDL, DRDO, ISRO, Brahmos Aerospace), mining, cement, export buyers | Inv. Pres. p.13, p.14, p.20 |
| Why them | Spec-in on named missile programmes (Akash, MRSAM, LRSAM, Astra, Agni, Brahmos); only qualified Indian company for countermeasures (company claim); about 100 engineers and scientists; PESO and DPIIT licences | Inv. Pres. p.12, p.20; AR p.25 |
| How delivered | Six plants in Telangana, Madhya Pradesh, Maharashtra; on-site O&M | Inv. Pres. p.15 |
| Cost structure | Material 57.65% of revenue, employee 17.74%, other 14.48% (FY26, B03 derived from AR p.110); materials dominate | B03 3C |
| Scarce resource | Licences, qualified processes, trained handlers (about 550 trained in propellant and pyrotechnics), sites that pass safety rules | AR p.25, p.27 |
| Pricing power source | Programme qualification and customer spec lock-in. Mix of negotiated defence contracts and tender-priced commercial sales. Margin evidence is weak: variable-consideration deductions fell from 9.37% to 5.99% of contract price, then margin still fell (B03, AR p.133) | AR p.24 3.4 |
| Asset intensity | Medium to heavy: PPE Rs 17,907 L plus CWIP Rs 2,639 L on Rs 38,834 L revenue (B03 3B). Asset turnover 0.764x (B03) | B03 |
| WC intensity | High and lumpy. Net receivable days 50 vs 33 (FY25); inventory Rs 10,301 L; customer advances fund part (B03). CFO FY26 Rs (144) L vs PAT Rs 4,583 L | B03 3A |
| Regulatory moat or burden | Both. Licences keep rivals out. Licences also close plants after accidents (TGPCB order 7 May 2025; Peddakandukuru consent expires 31 Oct 2026; renewal NOT FOUND) | B03 A.5, A.6 |

### 1E The chai-stall-uncle version
Think of a firm that makes the "fuel" inside government rockets. The Army and the space agency order it, but pay in steps, only after an inspector says "pass". So some months look empty and some look full. The firm also runs two rocket-fuel kitchens for ISRO and DRDO, and charges a fee to run them. A smaller shop sells blasting powder to mines. Its big risk is the kitchen itself, since one accident can shut a plant for months. Last year it also booked a big one-time gift from a supplier, so profit looked better than the business did.

### Section 1 summary table
| Item | Answer |
|---|---|
| Business type | Manufacturing with a services arm (hybrid) |
| Revenue nature | Lumpy, milestone-based project revenue; small recurring O&M fee base; short-cover commercial sales |
| Asset intensity | Medium to heavy |
| WC intensity | High |
| Pricing power | Moderate and unproven: spec-in on programmes, but gross material margin flat and variable deductions unexplained |

---
## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A Five forces
| Force | Plain answer | Helps / hurts / neutral | Anchor |
|---|---|---|---|
| Competition count | Defence: company says it is the only qualified Indian company for countermeasures and the first private maker of solid propellants for missiles (company claim). Named rivals NOT FOUND in the AR or presentation. Commercial: "competitive and sensitive to tender pricing" | Helps (defence), hurts (commercial) | Inv. Pres. p.14; AR p.24 3.4 |
| Entry barriers | Licences (PESO, DPIIT), programme qualification, testing, safety record | Helps | Inv. Pres. p.12; AR p.26 (8) |
| Supplier power | Specialised chemicals with "price and availability volatility"; one supplier settlement worth Rs 3,417.80 L and an auditor-qualified procurement control (B03) | Hurts | AR p.26; B03 1A |
| Customer power and concentration | Few state buyers; order book 95% to 96% defence; one unnamed customer at 10% or more of revenue; receivables 29.61% past 180 days | Hurts | AR p.25, p.133; B03 1B |
| Substitutes | NOT FOUND in documents for defence. Mining side: other explosives makers (NOT FOUND by name) | Neutral | no filed evidence |

### 2B Competitive positioning map
Named competitors in the AR and presentation: none NOT FOUND in the filed text. The brief lists peers (SOLARINDS, BDL, ASTRAMICRO) as COMPANY MEMORY, not anchored here. BDL appears in the filing as a customer (Akash, MRSAM, LRSAM, Astra), not a rival (Inv. Pres. p.20). Apollo Micro Systems is the incoming promoter (Inv. Pres. p.10). Peer positioning: NOT FOUND, check peer concalls (SOLARINDS, ASTRAMICRO transcripts are in the corpus; they are for stage 8/10).

### 2C Moat assessment
| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Switching costs | Yes, moderate | 100% of solid propellant requirement for MRSAM, LRSAM, Astra; pyrogen igniters for all Agni stages (Inv. Pres. p.20) | Medium to high while programmes run; programme-linked |
| Regulatory / licence | Yes | PESO, DPIIT licences (Inv. Pres. p.12); but licence suspension risk after accidents (B03) | Medium: also a burden |
| Intangible (technology, qualification) | Yes | DSIR-recognised, NABL labs; collaboration with IIT Madras, BITS Pilani (AR p.26) | Medium to high |
| Cost advantage | Not evidenced | Material cost 57.65% vs 57.23% (B03); no cost-curve data | Low |
| Scale | Weak | Revenue Rs 388 Cr; six plants | Low |
| Network effects | No | n/a | n/a |
| Brand | Weak | Not a retail brand | Low |
| Efficient scale / geography | Partial | Single-source for several programmes; "only qualified" claim is unverified | Medium |

### 2D Lifecycle stage
Industry: growth, policy-driven. Defence production Rs 1.78 lakh Cr (+15.6%), exports Rs 38,424 Cr (+62.66%) in FY26 (AR p.24; Inv. Pres. p.24). The company: early scale-up from a small base, order book up from Rs 3,890 mn (Mar 22) to Rs 16,420 mn (Oct 26) (Inv. Pres. p.8), but revenue flat (Rs 3,883 mn FY26 vs Rs 4,175 mn FY25; AR p.25). Orders have outrun deliveries.

### 2E Key industry drivers
| Driver | Direction | Impact on company | Anchor |
|---|---|---|---|
| Defence capital budget (Rs 7.85 lakh Cr FY27, +15.2%) | Up | Positive, indirect | Inv. Pres. p.24 |
| Indigenisation lists, 75% domestic capital procurement | Up | Positive | Inv. Pres. p.24 |
| Defence exports and licences | Up for industry; company foreign revenue down 34.1% FY26 | Mixed | AR p.24, p.133 |
| Coal, mineral and infrastructure activity | NOT FOUND as a number | Commercial segment | AR p.24 3.4 |
| Raw-material prices and availability | Volatile | Margin | AR p.26 |
| Electric detonator production stopped in FY26 | Down | Commercial segment; detonators 4.56 mn vs 10.36 mn pieces (B03 from DR p.28) | AR p.24 |

---
## SECTION 3: FINANCIAL METRICS THAT MATTER

### 3A Ignore these, track these
| Ratio | Why misleading or irrelevant here |
|---|---|
| Reported PAT, PAT margin, EPS, ROE, EBIT margin (17.8%) | Include Rs 4,214.49 L other income; 64.8% of PBT is one-off (B03). Use EBITDA before other income, 10.0% (AR p.25) |
| Spot-quarter revenue and margin | Milestone-based; FY26 Q4 Rs 677 mn vs 9M avg higher (B03). Use trailing four quarters and delivered order book |
| Current ratio and cash balance | Cash is partly customer advances (Rs 6,622.26 L); net of advances company holds Rs (641.57) L (B03) |
| Debt/equity and net cash | 0.13x; borrowing is not the risk, working capital is |
| Order book alone | 4.2x revenue but FY25 book of 1.8x did not convert (B03 4C); conversion is the test |
| Segment margin | Not filed; do not infer a mix-based margin |
| P/B | Book value includes land (39.2% of PPE, B03); not a franchise measure |

### 3B Must-track metrics
| Group | Metric | Tells you | Healthy range | Where | Red flag |
|---|---|---|---|---|---|
| Growth | Revenue delivered vs guide | Order conversion | NOT FOUND as an industry range; company guide Rs 600 to 700 Cr FY27 is COMPANY MEMORY. H1 FY27 Rs 2,478 mn (Inv. Pres. p.5) | Quarterly results | Run rate below guide path by Q3 |
| Growth | Order book / trailing revenue and order inflow | Visibility | Book 4.23x (Inv. Pres. p.8); healthy if book falls as delivered | Presentation | Book rising while revenue flat for a second year |
| Growth | Defence share of revenue and book | Mix | 80% to 86% now | Presentation | Mix swing from loss of a plant |
| Profitability | EBITDA margin before other income | Operating earning power | FY25 13.9%, FY26 10.0%, Q2 FY27 11.9% (AR p.25; Inv. Pres. p.6) | Results | Below 10% for H2 FY27 |
| Profitability | Material cost / revenue | Input pass-through | 57.65% FY26; Q2 FY27 65.1% (946.1/1452.8, derived, Inv. Pres. p.6) | P&L | Above 62% on a full-year basis |
| Profitability | Other income / PBT | Earnings quality | Under 15% | P&L note | Above 40% |
| Balance sheet | CFO / EBITDA | Cash conversion | Above 70% over two years | Cash flow | Negative again |
| Balance sheet | Receivable days and share past 180 days | Collection risk | 33 to 50 days; 29.61% past 180 days is already high (B03) | Notes | Past-180 share above 30% |
| Balance sheet | Customer advances and payables days | Whether growth is financed by customers | Advances 17.1% of revenue, DPO 88 (B03) | Notes, BRSR | Advances falling with receivables rising |

### 3C Non-financial KPIs
| KPI | Why | Where |
|---|---|---|
| Plant status, licence status (PESO, TGPCB consent) at Katepally and Peddakandukur | One closure removes revenue | AR p.94 BRSR; announcements |
| Safety incidents and fatalities | FY26 fatalities 5 (B03, BRSR p.85) | BRSR, DR |
| Order inflow by customer and export share; export licence cover | Export book is licence-gated | Presentation, concall |
| Capacity added vs CWIP (Rs 2,639.23 L) | Whether growth capex lands | Notes |
| Share of O&M contract renewals (ISRO, ASL) | Recurring base | Concall |
| Detonator and bulk explosive volumes | Commercial segment health (bulk 9,592 t FY26, B03) | DR |

### 3D Unit economics
| Item | Content |
|---|---|
| Unit | One rupee of delivered order book (defence); the product mix is too varied for a per-tonne unit. Per-unit price and volume data: NOT FOUND, check concall. |
| Revenue per unit | Rs 1.00 of order delivered; FY26 revenue 3,883 mn vs order book 15,690 mn = 24.7% turnover of the book (derived) |
| Cost per unit | Material 57.65 paise, employee 17.74, other 14.48, giving EBITDA 10.0 paise before other income (B03 3C; AR p.25) |
| Volume drivers | Inspection clearances, plant availability, input supply, customer schedules (AR p.26) |
| Price drivers | Contract price less variable consideration (9.37% in FY25, 5.99% in FY26; AR p.133); tender price in commercial |
| Cost drivers | Energetic chemicals; employee cost jumped 290 bps in FY26 (B03). Procurement control is qualified (B03 1A) |
| Incremental margin / operating leverage | Q2 FY27 revenue +Rs 697 mn YoY (1,452.8 vs 755.8) lifted EBITDA +Rs 106 mn (172.3 vs 66.1): 15.2% incremental margin (derived, Inv. Pres. p.6). Only one comparison; fixed staff cost Rs 188.6 mn per quarter is flat, so leverage is high. H1 FY27 EBITDA fell 15.9% on +13.8% revenue (Inv. Pres. p.6), so the lever works one way only when material cost stays flat |

---
## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A Risks and first-deteriorating line
| Category | Risk | First line item to deteriorate |
|---|---|---|
| Revenue model | Orders do not convert; milestone slippage; export licence refusals | Revenue vs prior quarter; order book/revenue; foreign revenue (down 34.1% in FY26) |
| Margin | Material cost pass-through; FX loss (Rs 591.64 L FY26) ; employee cost | Material cost / revenue (65.1% in Q2 FY27) |
| Balance sheet | WC absorbs cash; receivables past 180 days; advances unwind | Receivables ageing, CFO, customer advances |
| Execution | Plant accidents, licence suspension, capex delays | Production volume and plant licence status; CWIP not capitalised |
| Structural | Control change to Apollo; procurement control weakness; independent board count after resignation; one 10% customer | Related-party notes; auditor IFC opinion; board composition |

### 4B Valuation method applicability (formal handoff to Role 1)
| Method | Applicable? | Why |
|---|---|---|
| P/E on normalised earnings | Yes, PRIMARY | Profitable, asset-medium, order-backed. Earnings must exclude other income Rs 4,214.49 L (FY26). Section 1B governs the exit multiple; this row names method, not multiple |
| EV/EBITDA | Yes, SECONDARY | Capex-heavy plants and net cash make EV a cleaner cross-check; use EBITDA before other income (Rs 3,882.18 L FY26) |
| Order-book conversion DCF / reverse DCF | Yes, TERTIARY | Revenue is visible through the book; margin and WC are the unknowns |
| P/B, ROE | Limited | Book includes land and customer-advance cash; ROE inflated by one-offs |
| EV/Sales | No | Margin gap between segments unknown |
| Sum of parts | Not applicable now | No segment profit filed (Section 0) |
| Dividend yield | No | Rs 0.50 per share (B03) |
| NAV / asset value | No | Not an asset play |
| PEG | Weak | Growth guidance not yet delivered |

Primary: P/E on normalised earnings. Secondary: EV/EBITDA. Cycle stage that matters: order-conversion stage, early scale-up on a defence upcycle with a control change pending. Re-rating cannot be judged until a full year of margin above 10% exists without other income.

### 4C Quarterly monitoring checklist
| # | Item | Good | Trouble |
|---|---|---|---|
| 1 | Revenue vs prior-year quarter | Rising, tracking guide path | Below Q2 FY27 run (Rs 1,453 mn) |
| 2 | EBITDA margin before other income | Above 12% | Below 10% |
| 3 | Material cost / revenue | Below 60% | Above 65% (Q2 FY27 65.1%) |
| 4 | Other income / PBT | Under 15% | Over 40% |
| 5 | Order book and Defence share | Book converts; new inflow | Book up, revenue flat |
| 6 | Commercial vs Defence revenue | Stable split | Sharp swing |
| 7 | Receivables, share past 180 days | Under 25% | Over 30% |
| 8 | CFO (half-year) | Positive and near EBITDA | Negative |
| 9 | Customer advances | Stable | Falling |
| 10 | Plant and licence status | Katepally and Peddakandukur running | Fresh suspension or refusal |
| 11 | Export revenue and licence cover | Rising | Cancelled orders |
| 12 | Employee cost per quarter | Flat at about Rs 189 mn | Rising faster than revenue |
| 13 | Related-party transactions after close | Small | Large transfers to Apollo group |
| 14 | Auditor IFC remarks | Resolved | Repeated |

### 4D Management questions
| # | Question | Reassuring answer | Worrying answer |
|---|---|---|---|
| 1 | What are segment margins for Defence & Space, O&M and Commercial Explosives? | A number per segment, with Defence higher | "We do not disclose", or Commercial higher |
| 2 | What converts the Rs 16,420 mn book into H2 revenue, by plant and month? | Dated deliveries and inspection slots | General "momentum" |
| 3 | What licences are live at Katepally and Peddakandukur, and when does the Peddakandukuru consent renewal land? | Dated renewals on file | Pending, no date |
| 4 | What was the Rs 3,417.80 L supplier settlement, and does the whistle-blower complaint touch procurement? | Named, one-time, controls fixed | Cannot say |
| 5 | What share of the book is export, and which exports await licences? | Share stated, licences in hand | Large unlicensed share |
| 6 | What does Apollo plan on related-party sales, non-compete and board changes after close? | Arm's-length policy filed | Open-ended |
| 7 | Why did receivables past 180 days rise to 29.61%? | Named PSU payers with dated receipts | No collection plan |

---
## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

| Field | Entry |
|---|---|
| Company | Premier Explosives Ltd (NSE PREMEXPLN) |
| Business type | Manufacturing with services arm (hybrid) |
| Revenue streams | Defence & Space 81% FY26 (86% Q2 FY27), of which O&M services about 9.3% (sale of services); Commercial Explosives 19% FY26 (14% Q2 FY27); exports 13.3% (AR p.25, p.133; Inv. Pres. p.12) |
| Revenue nature | Lumpy, milestone-based |
| Asset intensity | Medium to heavy |
| WC intensity | High |
| Pricing power | Moderate, unproven |
| Cyclicality | Secular-growth industry, lumpy delivery (policy-driven) |
| Moats | Switching costs (medium to high), licence (medium), technology qualification (medium to high) |
| Primary valuation method | P/E on normalised earnings (ex other income) |
| Secondary / tertiary | EV/EBITDA; order-book conversion DCF |
| Top 5 must-track | (1) Revenue delivered vs path; (2) EBITDA margin before other income; (3) Material cost / revenue; (4) CFO / EBITDA; (5) Receivables past 180 days |
| Sector-cap evidence | Revenue and order book lean Defence; segment result NOT FOUND, so the earnings source is unproven |
| Biggest unknowns | Segment profit; plant licence status; post-close related parties |

Input gaps carried from B00: shareholding fully pulled; Q2 FY27 concall transcript absent; screener sheets empty; BDL peer transcripts absent; research empty; OCR layer on results scans; SPA terms not in the AR. Presentation was provided.
