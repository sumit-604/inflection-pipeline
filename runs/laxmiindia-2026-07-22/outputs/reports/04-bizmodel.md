# STAGE 4: BUSINESS MODEL DECODER — Laxmi India Finance Ltd (LAXMIINDIA)
Run date: 2026-07-22 | Model: Sonnet 5 | Pipeline stage: B04-bizmodel

Lender lens applied throughout per task brief: revenue = interest income + fee/commission +
DA/co-lending gains; valuation lens is P/B and P/E on NIM/ROA/ROE/AUM-growth drivers.
Conventional operating-company ratios (asset turns, inventory, EBITDA margin, working-capital
cycle) are irrelevant and are listed as such in Section 3A.

Sources read: DRHP (prospectus, 2025-07-31) "Our Business" pp.182-211 and pp.28-32, 135-139,
167-171, 177-181; Investor Presentation (Q4/FY26, dated 2026-05-13), slides 1-47; FY26 Audited
Results filing ("Annual_Report_2024.pdf", filed 2026-05-13) pp.1-12. Operator-context.md used only
as non-anchored cross-check per its own status label; every number it supplied that appears below
has been re-anchored to a PDF the stage read directly (mostly the Investor Presentation, which
carries the same 9M/Q4 FY26 figures operator-context summarised).

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description
Laxmi India Finance is a Jaipur-headquartered, non-deposit-taking NBFC that lends small,
secured, cash-flow-underwritten loans (mostly against property, some against vehicles) to
underbanked small traders, MSMEs and vehicle owners across semi-urban and rural Rajasthan,
Gujarat, Madhya Pradesh, Chhattisgarh, Uttar Pradesh and (from FY26) Maharashtra, funding
those loans with borrowed money from banks and NBFCs and earning the spread (DRHP p.184;
Inv. Pres. slide 21).

### 1B. The money flow chain, one chain per revenue stream

**Stream 1 — Interest income (the core engine, ~93.6% of FY26 total income, Q4FY26 Results
filing p.7):**
[Company borrows from 47+ banks/NBFCs at ~10.80% average cost, FY26 (Inv. Pres. slide 8)] →
[branch relationship managers source, cash-flow-underwrite and disburse secured MSME/vehicle/
construction loans, average ticket ₹0.43-0.65 million (DRHP pp.187, 196)] → [borrower uses the
loan for working capital, property purchase/construction, or vehicle purchase] → [borrower pays
monthly EMIs over 19-84 months depending on product (DRHP pp.196-198)] → [company collects
via e-NACH/branch-led collections and keeps the spread between yield (~21.3% blended, FY26,
Inv. Pres. slide 8) and cost of borrowing (10.80%)].

**Stream 2 — Fee and commission income (~4.9% of FY26 total income, Q4FY26 Results filing
p.7):**
[Company originates/services loans, including a co-lending arrangement with a bank partner
(disbursement ratio ~90% Laxmi India / 10% partner bank, per FY26 Results filing p.5, Note 11)]
→ [company earns processing fees and a servicing/sharing fee on the co-lent or assigned book] →
[fee is booked upfront or over the servicing period] → [paid by the borrower (processing fee) or
netted from the assignee/co-lending partner (servicing fee)].

**Stream 3 — Net gain on direct assignment (DA) of loans (~0.7% of FY26 total income as a
separate P&L line, but a further ₹7.53 crore of upfront gain sits embedded inside the interest
income line itself, FY26 Results filing p.5, Note 12; ₹8.09 crore in FY25):**
[Company originates and seasons a pool of loans on its own book] → [company sells the pool
(direct assignment) to a bank/NBFC/ARC, retaining a minimum retention of beneficial economic
interest (MRR)] → [buyer pays upfront consideration plus ongoing servicing arrangement] →
[company recognises an upfront gain on de-recognition, boosting the quarter's NIM/PAT] → [buyer
pays the company a servicing fee to continue collecting from the underlying borrowers]. This is
the stream implicated in the Up Money Ltd DA-pool stress event (Q3-Q4 FY26; see Section 4A).

### 1C. Revenue model classification table

| Stream | Type (standard taxonomy) | Description | % of FY26 total income | Source | Predictability |
|---|---|---|---|---|---|
| Interest income (net of finance cost = NII) | Spread/interest income | Yield on secured MSME (~80% of AUM), vehicle, construction and other loans, minus cost of borrowed funds | 93.60% (₹299.12 cr of ₹319.59 cr) | FY26 Results filing p.7 | Medium — recurring but rate- and credit-cycle sensitive; ~7.5 cr of this line is a one-off DA gain (Note 12, same filing, p.5), which lowers true recurring predictability |
| Fee and commission income | Fee income | Processing fees, co-lending/servicing fees | 4.86% (₹15.53 cr) | FY26 Results filing p.7 | Low-Medium — scales with disbursement volume and co-lending mix, discretionary in size |
| Net gain on fair-value changes (incl. assignment gains reported separately) | Other/trading-type gain | Fair value gains on investments and on loans measured at FVTPL, including DA/ARC sale gains not routed through interest income | 0.74% (₹2.37 cr) | FY26 Results filing p.7 | Low — event-driven, lumpy by quarter (Q4 FY26 DA sale alone contributed ~₹8.66 cr upfront profit into NIM per Inv. Pres. slide 5/6 read together with Note 12) |
| Other income | Other | Miscellaneous | 0.80% (₹2.56 cr) | FY26 Results filing p.7 | Low |

Memo — interest income by lending vertical (AUM-proportion proxy, not a direct P&L split; DRHP
does not disclose interest income by product separately from AUM):

| Vertical | % of AUM, FY25 (DRHP p.185) | % of AUM, FY26 (Inv. Pres. slide 35) |
|---|---|---|
| MSME (loan against property) | 76.34% | 79.85% |
| Vehicle finance (CV, 2W, tractor, EV) | 16.12% | 8.97% |
| Construction loans / LAP | 4.87% | 5.26% |
| Wholesale (on-lending to other NBFCs) | 1.49% | 3.26% |
| Business + personal loans (unsecured) | 1.19% | 2.66% |

### 1D. Simplified business-model canvas

| Element | Answer |
|---|---|
| What they sell | Secured, small-ticket credit (MSME/LAP, vehicle, construction, small unsecured business/personal, and wholesale on-lending) |
| Who buys | Small traders, self-employed MSME owners, vehicle owners/operators, salaried Tier-II/III customers, largely first-time formal borrowers (37.1% first-time, DRHP p.186) in semi-urban/rural Rajasthan-Gujarat-MP-Chhattisgarh-UP-Maharashtra |
| Why them (vs. a bank) | Fast, low-documentation, cash-flow-based underwriting for customers without clean income proof; branch-embedded relationship managers who know local cash flows and collateral values (Inv. Pres. slides 23, 27) |
| How delivered | 176-branch hub-and-spoke network (Inv. Pres. slides 5, 23), >90% direct/branch-led sourcing plus DSAs and the in-house "Laxmi Mitra" referral app |
| Cost structure dominance | Finance cost (interest expense, ₹137.34 cr, 43% of FY26 total expenses) and employee/operating cost (₹102.15 cr, FY26 Results/Inv. Pres. slide 15) — a "spread + opex + credit cost" cost structure, not a manufacturing cost structure |
| Scarce resource | Cost-effective, diversified wholesale funding access (47 lenders, credit rating) and branch-level local underwriting/collections relationships — not a product or technology moat |
| Pricing power source or absence | Weak-to-moderate: yield is largely a function of risk segment (MSME LAP 18-28% p.a., DRHP p.196) and competitive intensity from banks/other NBFCs/MFIs, not brand pricing power; the real lever is COST of funds, which the company controls via credit-rating improvement (A- to A/Stable, FY26, Inv. Pres. slide 5) |
| Asset intensity | Heavy — 98.6%+ of the balance sheet is financial assets (loans, ₹1,480.10 cr of ₹1,817.78 cr total assets, FY26 Results filing p.8); this is a "balance sheet is the product" business |
| WC intensity | Not applicable in the operating-company sense — a lender has no inventory or receivables cycle; its equivalent is capital adequacy and leverage (CRAR 26.12%, Debt/Equity 2.87x, FY26, Inv. Pres. slides 5, 10) |
| Regulatory moat or burden | Both — RBI NBFC registration, Scale Based Regulation (Middle Layer, per FY26 Results filing p.5, Note 4) is a genuine entry barrier for challengers but also a compliance burden (capital adequacy floors, ALM discipline, RBI directions on assignment/co-lending) |

### 1E. The chai-stall-uncle version
Imagine a moneylender who only lends against something solid — your shop, your tractor, your
truck — never a blank promise. Laxmi India is that moneylender scaled into a company: it borrows
money cheaply from big banks, then lends it out in small pieces (average ₹43,000-65,000 per loan)
to shopkeepers and vehicle owners in small-town Rajasthan and its neighbouring states, at a much
higher rate than it pays to borrow. The difference between what it pays the bank and what it
charges the shopkeeper is its profit — like a wholesaler buying rice cheap and selling it retail at
a markup, except the "rice" here is money itself. It occasionally also sells off a bundle of these
loans to another lender for an upfront fee (like sub-letting a rented shop), which is a smaller,
lumpier, second way it makes money — and one bundle sold to a weak partner (Up Money Ltd)
turned sour in FY26, which is the single biggest thing to watch.

### Section 1 summary table

| Field | Answer |
|---|---|
| Business type | Lending (NBFC) — not manufacturing/services/trading/platform |
| Revenue nature | Spread income (yield minus cost of funds) plus fee and one-off assignment gains |
| Asset intensity | Heavy (financial-asset balance sheet) |
| WC intensity | Not applicable (lender; balance-sheet leverage/CRAR is the analogous control) |
| Pricing power | Weak-to-moderate; real lever is cost of funds, not price to borrower |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Answer | Helps / Hurts / Neutral |
|---|---|---|
| Competition intensity | At least 7 listed peers directly comparable in the DRHP's own benchmarking (MAS Financial, Five Star Business Finance, SBFC Finance, UGRO Capital, CSL Finance, AKME Fintrade, Moneyboxx Finance — DRHP pp.178-181), plus banks, small finance banks and unlisted local NBFC/MFIs in the same geography | Hurts — crowded, fragmented small-ticket secured-lending space |
| Entry barriers | RBI NBFC registration + net-owned-fund thresholds + Scale Based Regulation compliance (FY26 Results filing p.5) create a real but not prohibitive barrier; the harder-to-replicate barrier is branch-level collections/underwriting density built over 119→176 branches across 13 years (DRHP p.192; Inv. Pres. slide 22) | Neutral-to-helps for an incumbent, but low enough that well-capitalised new entrants (fintech-NBFCs, SFBs) keep entering |
| Supplier power (lenders to the company) | The company's "suppliers" are its own lenders — 47 lenders (8 PSU banks, 10 private banks, 7 SFBs, 22 NBFC/FIs) as of March 2025 (DRHP p.189); top-5 lenders were 34.10% of total borrowings (DRHP p.189) | Hurts moderately — cost and availability of funds is the single biggest lever on profitability, and it depends on external rating agencies and bank credit committees, not on Laxmi India's own pricing power |
| Customer power / concentration | No single borrower concentration risk (average ticket ₹0.43-0.65 mn, DRHP pp.187, 196) but the customer base is largely first-time/underbanked, so has essentially no bargaining power on price; over time, "graduated" borrowers become more price-sensitive as they qualify for bank credit | Helps (diversified) on concentration; neutral-to-hurts on long-run pricing as best customers migrate to banks |
| Substitutes | Informal moneylenders (costlier but faster/no-documentation), banks (cheaper but stricter documentation), other MSME-focused NBFCs, and — for the better credit tier — formal bank/SFB credit as documentation and credit history formalise (DRHP p.189, CARE Report commentary) | Hurts at the margin as banking penetration deepens in semi-urban India |

### 2B. Competitive positioning map (peer set from DRHP CARE-Report benchmarking, FY25 figures,
pp.178-181)

| Company | AUM (₹ cr) | AUM growth | NIM | GNPA | RONW | ROA | Positioning read |
|---|---|---|---|---|---|---|---|
| Laxmi India Finance | 1,277.02 | 32.83% | 9.73% | 1.07% | 15.66% | 3.00% | Smallest AUM in this peer set but second-best RONW and best-in-class asset quality except CSL |
| MAS Financial Services | 12,099.80 | 19.50% | 5.46% | 2.44% | 14.71% | 3.08% | Much larger, lower NIM, weaker asset quality |
| Five Star Business Finance | 11,877.00 | 23.19% | 16.07% | 1.79% | 18.60% | 8.19% | Largest, richest NIM/ROA in the set — the scaled benchmark to aspire to |
| SBFC Finance | 8,747.00 | 28.22% | 9.94% | 2.74% | 11.39% | 4.34% | Comparable NIM, weaker asset quality |
| UGRO Capital | 12,003.00 | 32.67% | 4.29% | 2.30% | 8.68% | 1.96% | Larger, thinner spreads, weakest ROA |
| CSL Finance | 1,195.00 | 16.02% | 12.03% | 0.46% | 14.18% | 6.46% | Closest-sized peer; better asset quality and ROA than Laxmi India |
| AKME Fintrade | 618.61 | 53.23% | 11.31% | 2.77% | 11.09% | 6.04% | Smaller, faster-growing, weaker asset quality |
| Moneyboxx Finance | 927.00 | 26.99% | 13.30% | 6.61% | 0.53% | 0.14% | Smaller, weak asset quality and returns — cautionary comparable |

Read: Laxmi India sits at the small-scale, high-asset-quality, mid-NIM corner of this peer group.
Its edge is asset quality, not spread or scale — the FY26 GNPA event (Up Money DA pool) is
therefore a direct threat to its one clearly differentiated attribute (Inv. Pres. slides 5, 11).

### 2C. Moat assessment (eight standard types)

| Moat type | Evidence | Durability |
|---|---|---|
| Brand | Regional recognition in Rajasthan (widest branch reach among peers in Rajasthan per CARE Report, DRHP p.183) but no evidence of pricing power from brand | Low |
| Network effects | None — lending has no network effect; more borrowers do not make the product better for existing borrowers | None |
| Switching costs | Moderate — repeat-customer disbursements were 10.44% of MSME disbursements in FY25 (DRHP p.196), showing some retention, but borrowers can and do refinance elsewhere once formalised | Low-Moderate |
| Cost advantage | Improving — average cost of borrowing fell from 12.24% (FY23) to 10.80% (FY26) as rating improved from BBB+ to A/Stable (DRHP p.190; Inv. Pres. slides 5, 8) — a real, compounding advantage if sustained | Moderate, contingent on rating trajectory |
| Intangible assets / licenses | RBI NBFC registration (since 2011, DRHP p.184), Middle-Layer NBFC classification, 176-branch physical network — a real asset but not unique | Moderate |
| Efficient scale | AUM per branch rose from ₹57.71 mn (FY23) to ₹80.82 mn (FY25, DRHP p.188/193) — the hub-and-spoke model shows genuine operating leverage as branches season, but the company is still the smallest AUM among its listed peer set | Moderate, building |
| Regulatory/legal barriers | RBI Scale Based Regulation, capital adequacy floors (CRAR 26.12% vs. 15% minimum, FY26) act as a barrier to under-capitalised new entrants | Moderate |
| Process power / execution | Branch-embedded relationship-manager model, cash-flow underwriting for non-income-proof customers, family co-borrower/guarantor structure (Inv. Pres. slides 27-31; DRHP pp.190-192) — a genuine execution discipline, evidenced in best-in-class GNPA/NNPA prior to the Up Money event | Moderate, but the Up Money DA-pool stress shows the execution moat has a real gap in third-party/DA-partner due diligence |

### 2D. Industry lifecycle stage and company position
The MSME/semi-urban NBFC lending industry in India is in a growth phase, not maturity: rural
scheduled-commercial-bank credit rose from ₹7.26 trillion (Mar'20) to ₹13.76 trillion (Dec'24) and
semi-urban credit from ₹12.38 trillion to ₹24.46 trillion over the same period (DRHP p.192, CARE
Report), and India's overall credit-to-GDP ratio (93.6% as of Sep'24) remains well below developed
markets (140-200%, DRHP p.137) — headroom exists. NBFC MSME AUM specifically is projected to
grow at 20-22% CAGR to cross ₹6 trillion by FY27 (DRHP p.189, CARE Report). Within this growth
industry, Laxmi India is a small, regionally concentrated (80%+ of AUM in Rajasthan historically,
DRHP p.199) scale-up-stage player, expanding geographically (added Chhattisgarh FY24, UP FY25,
Maharashtra FY26 — Inv. Pres. slide 22) rather than a mature, diversified national player.

### 2E. Key industry drivers

| Driver | Direction | Impact on Laxmi India |
|---|---|---|
| Rural/semi-urban credit penetration | Rising (under-penetrated per CARE Report, DRHP p.192) | Positive — core addressable market expanding |
| NBFC MSME AUM growth (~20-22% CAGR projected to FY27) | Rising | Positive tailwind for the 80%-of-AUM MSME vertical |
| Interest rate cycle / cost of funds | Falling in FY23-FY26 (avg cost of borrowing 12.24%→10.80%) | Positive so far; a reversal would compress spreads given fixed-rate loan book |
| Bank/PSU credit competition for formalising MSMEs | Rising as documentation/Udyam registration formalises MSMEs (DRHP p.189) | Negative medium-term — best customers eventually qualify for cheaper bank credit |
| Regulatory tightening on co-lending/DA transactions (RBI directions cited in FY26 Results filing, Note 4/9/11) | Increasing scrutiny | Mixed — enables funding diversification but raises compliance/servicing obligations, as the Up Money episode shows |
| Passenger/commercial vehicle financing growth (4-6% CV growth FY26E, DRHP p.167) | Modest positive | Secondary — vehicle finance is now only ~9% of AUM (down from 16% in FY25) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these table

| Commonly tracked ratio | Verdict for this company | Why |
|---|---|---|
| Inventory turnover / days inventory | Irrelevant | Lender has no inventory |
| Asset turnover (revenue/fixed assets) | Irrelevant | 98.6% of assets are loans, not fixed assets; the meaningful "turnover" concept is yield on AUM, already captured separately |
| EBITDA margin | Irrelevant | Financing cost is a core operating cost for a lender, not a below-the-line item; EBITDA structurally overstates a lender's profitability and is not how the industry, regulator or the company itself reports (P&L is Interest Income − Finance Cost − Opex − Provisions = PAT) |
| Working capital cycle / receivable days | Irrelevant | No trade receivables/payables cycle; the analogous concept is Asset-Liability Management (ALM) gap, which the company does track (surplus at every bucket, FY26, Inv. Pres. slide 13) |
| Current ratio / quick ratio | Irrelevant | Liquidity is managed via ALM and CRAR, not current-asset/current-liability ratios |
| Gross margin | Irrelevant | No cost-of-goods-sold concept; use Net Interest Margin (NIM) and Spread instead |
| Revenue growth alone (without AUM/NIM context) | Misleading in isolation | FY26 revenue growth is partly inflated by a ~₹7.53 cr embedded DA-assignment gain inside interest income (FY26 Results filing p.5, Note 12) — revenue growth must be read alongside NIM-ex-one-offs |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range (sector) | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| AUM growth (YoY) | Underlying loan book scale-up | 20-35% for a scale-up-stage MSME NBFC (peer set ranged 16-53% in FY25, DRHP p.178) | Inv. Pres. slide 7; DRHP p.185 | Below 15% (loses scale-economics momentum) or above 50% sustained (credit-quality risk from rapid, unseasoned growth) |
| Disbursement growth | Forward-looking proxy for AUM growth | Should track or lead AUM growth | Inv. Pres. slide 7 | Disbursement growth persistently below AUM growth (signals slowing originations, AUM growth from assignment/DA accounting only) |
| Branch/AUM-per-branch growth | Operating leverage evidence | AUM/branch should rise each year as branches season | DRHP pp.188, 193 | Flat or falling AUM/branch despite new branch additions (new branches diluting, not adding) |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range (sector) | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| Net Interest Margin (NIM) | Core spread economics | 9-13% for secured MSME/vehicle NBFCs (peer range 4.3-16.4%, DRHP p.178) | Inv. Pres. slide 8; FY26 Results filing p.7 | Below 8% (spread compression) or NIM growth driven mainly by one-off DA gains rather than yield/cost-of-funds trends |
| Return on Assets (ROA) | Overall profitability per rupee lent | 2.5-4% for this peer tier (FY26 was 3.08%, Inv. Pres. slide 9) | Inv. Pres. slide 9 | Below 2% |
| Cost-to-income / Opex ratio | Scale economics | Should decline as AUM/branch and AUM/employee rise | Inv. Pres. slide 6 (Opex ₹ cr); DRHP pp.187-188 (AUM per branch/employee) | Opex ratio rising faster than AUM (new branches not seasoning) |
| Cost of borrowing | Funding efficiency, rating-dependent | Should track or beat rating-cohort average; fell from 12.24% (FY23) to 10.80% (FY26) | Inv. Pres. slide 8; DRHP p.190 | Reversal/increase despite a stable or improving rating (signals lender concentration or negotiating-power loss) |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range (sector) | Where to find it | Red-flag threshold |
|---|---|---|---|---|
| GNPA / NNPA (reported AND ex-stressed-partner) | Underlying asset quality | GNPA <2% is best-in-class for this peer set (Laxmi India was 1.07% FY25, DRHP p.191); FY26 GNPA 2.13% reported / 0.80% ex-Up Money (Inv. Pres. slide 11) | Inv. Pres. slide 11 | Reported GNPA rising while "ex-one-off" GNPA is used to obscure a broader deterioration; PCR on Stage 3 falling below ~45% |
| CRAR / Debt-to-Equity | Capital cushion and leverage headroom | CRAR well above 15% regulatory floor (26.12% FY26); D/E of 2-4x typical for this cohort (2.87x FY26, down from 4.41x FY25 post-IPO, Inv. Pres. slide 10) | Inv. Pres. slides 5, 10 | CRAR approaching 15% floor, or D/E re-levering back above 4x without matching capital raise |
| Security cover / ALM surplus at each bucket | Liquidity and collateral protection | Positive cumulative surplus at every maturity bucket (confirmed FY26, Inv. Pres. slide 13); security cover >100% (107.09% Mar'25, DRHP p.206) | Inv. Pres. slide 13; DRHP p.206 | Any negative cumulative gap in the up-to-1-year buckets |

### 3C. Industry-specific non-financial KPIs

| KPI | Relevance | Where to find it |
|---|---|---|
| Number of active customers / repeat-customer % | Franchise depth and cross-sell traction | DRHP pp.184-186, 196; Inv. Pres. slide 7 |
| Average ticket size and LTV by product | Underwriting discipline / risk appetite | DRHP pp.187, 196-198 |
| % first-time borrowers | Financial-inclusion depth vs. graduation risk | DRHP p.186; Inv. Pres. slide 33 |
| Collection efficiency % | Real-time asset-quality health, ahead of NPA recognition | DRHP p.190 (98.92%/96.69%/96.76% FY23-25) |
| Sourcing mix (direct/DSA/digital) | Cost of acquisition, quality control | DRHP pp.192, 201 |
| Employee/relationship-manager productivity (customers per RM) | Execution capacity as branches scale | DRHP p.200 (7 customers/RM/month) |
| District-level penetration % | Runway within existing states before diminishing returns | DRHP p.193 (30% average district penetration) |

### 3D. Unit economics — the physics of the business

**Unit chosen: ₹1 lakh of average AUM outstanding** (the natural unit for a lender; a "per loan
account" unit would obscure the wide ticket-size range across products, ₹0.04mn to ₹15.71mn
average by product, DRHP pp.197-199).

| Line | FY26 value | Source |
|---|---|---|
| Revenue per unit (yield on average portfolio) | ~21.30% | Inv. Pres. slide 8 |
| Cost per unit — cost of borrowed funds | ~10.80% | Inv. Pres. slide 8 |
| Cost per unit — operating expense (opex ÷ average AUM, ₹102.15 cr ÷ ~₹1,451.6 cr) | ~7.0% | Computed from Inv. Pres. slides 6-7 |
| Cost per unit — credit cost (total provisions ÷ average AUM, ₹14.05 cr ÷ ~₹1,451.6 cr) | ~1.0% | Computed from Inv. Pres. slide 11 |
| Margin per unit (pre-tax residual) | ~2.5-3.1%, consistent with reported ROA of 3.08% (Inv. Pres. slide 9) | Inv. Pres. slide 9 |

**Volume drivers:** branch count (176, +18 YoY) and district penetration (30% average, DRHP
p.193) inside existing states; disbursement growth (₹821.44 cr FY26, +14.3% YoY, Inv. Pres.
slide 7).

**Price drivers:** product mix shift (MSME LAP, the highest-ticket, ~22% yield product, rising to
~80% of AUM) versus lower-yield secured vehicle/wholesale loans; and macro rate environment.

**Cost drivers:** external credit rating trajectory (A- → A/Stable in FY26, driving cost of
borrowing down 68 bps YoY to 10.80%, Inv. Pres. slides 5, 8) and lender-mix diversification (PSU
banks, private banks, SFBs, NBFC/FIs, NCDs — Inv. Pres. slide 14).

**Incremental margin / operating leverage:** genuine — AUM per branch rose from ₹57.71 mn
(FY23) to ₹80.82 mn (FY25, DRHP pp.188, 193), meaning each new branch's fixed cost (credit
manager, RM team, premises) is spread over a growing loan book as the branch matures (vintage
curve). This is the single clearest structural driver of the ROA improvement from 2.29% (FY23) to
3.08% (FY26, Inv. Pres. slide 9) — provided credit quality holds as new, unseasoned branches
season.

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Reliance on lumpy DA/assignment gains to hit reported NIM/PAT growth (₹7.53 cr embedded gain in FY26 interest income, FY26 Results filing p.5, Note 12; a further ~₹8.66 cr one-off from a Q4 FY26 DA sale per Inv. Pres. context) | Net gain on fair-value changes / "gain on derecognition of assigned loans" line, and the gap between reported NIM and NIM-ex-one-offs |
| Margin | Cost-of-borrowing reversal if rating momentum stalls or rates rise, against a largely fixed-rate loan book | Spread (yield minus cost of borrowing), Inv. Pres. slide 8 |
| Balance sheet | Third-party/co-lending/DA-partner credit risk (Up Money Ltd pool, ~₹19 cr exposure, GNPA jump to 2.40% in Dec'25 before settling at 2.13% Mar'26, Inv. Pres. slides 5, 11) | Gross NPA %, Provision Coverage Ratio (Stage 3) |
| Execution | Branch-vintage dilution as network nearly triples (119→176 branches in 3 years) faster than local underwriting talent/collections infrastructure can season | AUM per branch, disbursement per branch per month (DRHP p.188) |
| Structural | Geographic concentration (Rajasthan was 80%+ of AUM historically, DRHP p.199) despite recent diversification into UP/Maharashtra; a state-level shock (agri distress, local competition, regulatory change) would hit disproportionately | State-wise AUM %, GNPA by state (not separately disclosed — a monitoring gap) |

### 4B. Valuation method applicability table (formal handoff to Role 1 / Stage 11)

| Method | Applicable? | Why |
|---|---|---|
| P/E | Applicable | Standard for a profitable, growing NBFC; must be read alongside ROE trajectory since earnings quality includes one-off DA gains |
| P/B (Price-to-Book) | **PRIMARY** | The standard valuation anchor for lenders — book value (net worth ₹465.47 cr, FY26, Inv. Pres. slide 5) is the capital being levered to generate ROE, and P/B vs. sustainable ROE is how this entire peer set (DRHP pp.178-181) is benchmarked |
| P/E on normalised (ex-one-off) EPS | **SECONDARY** | Cross-check against headline P/E once DA/assignment gains are stripped out of PAT, given the FY26 quality-of-earnings caveat in Section 4A |
| DCF / DDM on dividend or FCFE | Not applicable as primary | Lenders' "free cash flow" is dominated by loan-book growth funded by fresh borrowing, making a conventional unlevered FCF DCF structurally misleading; a residual-income or Gordon-growth-on-ROE-vs-COE model is a more defensible variant if used at all |
| EV/EBITDA | **Not applicable** | Finance cost is a core operating cost for a lender, not a financing add-back; EBITDA is not a meaningful metric here (see 3A) |
| Sum-of-the-parts / segment valuation | Not applicable | Company discloses a single reportable segment — lending (FY26 Results filing p.5, Note 3) |
| Asset-based / liquidation value | Tertiary, context-only | Relevant only as a downside floor check (net worth minus embedded one-off gains), not a going-concern valuation method |

**Cycle stage that matters for valuation:** the company is in an AUM/branch-scaling phase within
a structurally growing but competitively crowded MSME-NBFC industry (see Section 2D) — P/B
should be benchmarked against where sustainable, ex-one-off ROE is heading (management's own
medium-term target: ROA 3.50-3.75%, ROE 13.50-14.00%, Inv. Pres. slide 18), not against the
FY26 reported ROE of 13.73% which includes the DA-gain boost.

**not_applicable list:** EV/EBITDA, unlevered FCF DCF, sum-of-the-parts.

### 4C. Quarterly monitoring checklist (10-15 items)

1. AUM growth QoQ/YoY vs. 30-35% medium-term guidance (Inv. Pres. slide 18) — good: in range; trouble: persistent miss or overshoot funded by DA "AUM" rather than on-book growth
2. NIM, headline vs. ex-one-off (strip out any disclosed DA/assignment gain) — good: gap narrows or stays small; trouble: gap widens
3. GNPA/NNPA, reported AND ex-stressed-DA-partner (as the company itself now discloses, Inv. Pres. slide 11) — good: both converging downward; trouble: divergence widening
4. Provision Coverage Ratio on Stage 3 — good: holding near/above ~49%; trouble: falling meaningfully
5. Cost of borrowing (QoQ trend) — good: flat-to-declining; trouble: rising despite stable rating
6. CRAR and Debt/Equity — good: CRAR comfortably above 20%, D/E disciplined re-levering; trouble: CRAR drifting toward 15% floor
7. AUM per branch and per employee — good: rising; trouble: flat/falling despite new branch adds
8. Disbursement growth vs. AUM growth — good: disbursement growth tracks or leads; trouble: AUM growth outpacing disbursements (accounting-driven, not origination-driven)
9. Status of Up Money Ltd DA pool recovery (recognition as servicer, actual cash recovered) — good: recovery materialising; trouble: further write-offs
10. Any NEW DA/co-lending partner defaults or delinquencies — good: none; trouble: any recurrence signals systemic partner-diligence gap
11. Collection efficiency % — good: at or above ~97%; trouble: declining
12. Product mix shift (MSME % of AUM) — good: diversifying per stated strategy; trouble: concentration continuing to rise unchecked
13. New-state (UP, Maharashtra) AUM and asset-quality trajectory — good: seasoning in line with core states; trouble: materially worse asset quality in new geographies
14. Top-5/Top-10 lender concentration of borrowings — good: stable or diversifying; trouble: concentration rising
15. ALM cumulative surplus at each maturity bucket (Inv. Pres. slide 13 format) — good: surplus maintained at every bucket; trouble: any bucket turning negative

### 4D. Highest-value questions for management

1. **Q:** What is the actual recovery timeline and expected loss on the Up Money Ltd DA pool, and what specific new due-diligence controls have been added for DA/co-lending partners going forward?
   **Reassures:** ring-fenced, one partner only, servicer-transfer underway, recovery visible in the next 1-2 quarters, ex-partner GNPA already at 0.80% (Inv. Pres. slide 11).
   **Worries:** vague timeline, no named control changes, or signs the same DA/co-lending channel is being scaled further without added safeguards.

2. **Q:** How much of FY26 (especially Q4) NIM/PAT growth came from one-off DA/assignment gains versus core lending spread?
   **Reassures:** one-offs quantified and small relative to core PAT growth.
   **Worries:** management unable/unwilling to isolate the one-off, or the one-off is a growing share of a widening PAT-growth base.

3. **Q:** With cost of borrowing down from 12.42% (FY23) to 10.80% (FY26), how much further compression is realistically available, and how exposed is NIM to a rate-cycle reversal given the largely fixed-rate loan book?
   **Reassures:** clear roadmap (ECB access, further rating upgrades, bank-mix consolidation per Inv. Pres. slide 18) with modelled sensitivity.
   **Worries:** cost of funds treated as a one-way ratchet with no downside stress-test.

4. **Q:** As MSME AUM concentration rises toward 80%, what is the concrete plan and timeline to diversify the product mix, and what specific counterparty controls exist for the wholesale (on-lending to other NBFCs) book, given its much larger ticket size (up to ₹5 crore, DRHP p.199)?
   **Reassures:** specific diversification targets and wholesale-counterparty screening criteria.
   **Worries:** wholesale book framed purely as a growth lever with no counterparty-risk framework disclosed.

5. **Q:** With branches nearly tripling in three years (119→176), what does the branch-vintage productivity curve look like — are newer branches seasoning at the same pace as the FY23-25 cohort?
   **Reassures:** disclosed, favourable vintage curve.
   **Worries:** management cannot or will not disclose branch-cohort productivity.

6. **Q:** What is the funding-diversification roadmap (ECBs, further bank consolidation) and target leverage, given Debt/Equity fell to 2.87x post-IPO (from 4.41x) — how fast will leverage re-build, and to what ceiling?
   **Reassures:** disciplined, rating-linked re-leveraging plan consistent with the stated ROE target.
   **Worries:** leverage targeted to rebuild aggressively without corresponding capital-quality safeguards.

7. **Q:** How is underwriting discipline being maintained as the company enters new states (UP, Maharashtra) where its core relationship-based, local-cash-flow underwriting edge (built over 13+ years in Rajasthan) is unproven?
   **Reassures:** phased entry, small initial branch counts, early asset-quality data comparable to home-state cohorts.
   **Worries:** rapid branch rollout in new states without comparable early asset-quality disclosure.

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
================================================================================
 LAXMI INDIA FINANCE LTD (LAXMIINDIA) — BUSINESS MODEL SUMMARY CARD
================================================================================
 Business type:        Lending (NBFC) — MSME/LAP-led, secured, semi-urban/rural
 One-line thesis:       Small-ticket, secured, relationship-underwritten NBFC
                        lender scaling branch density in Rajasthan-adjacent
                        states; edge is asset quality and improving cost of
                        funds, not pricing power or scale
--------------------------------------------------------------------------------
 Revenue mix (FY26):    Interest income 93.6% | Fee/commission 4.9% |
                        Net FV/assignment gains 0.7% | Other 0.8%
                        (FY26 Results filing p.7)
 AUM mix (FY26):        MSME 79.9% | Vehicle 9.0% | Construction/LAP 5.3% |
                        Wholesale 3.3% | Business/personal 2.7%
                        (Inv. Pres. slide 35)
--------------------------------------------------------------------------------
 Asset intensity:       Heavy (balance sheet = the product)
 WC intensity:          N/A — lender; CRAR/leverage is the analogue
 Pricing power:         Weak-to-moderate; real lever is cost of funds
 Cyclicality:           Cyclical on asset quality/credit cycle, secular-growth
                        on addressable market (rural/semi-urban credit
                        under-penetration)
--------------------------------------------------------------------------------
 Primary valuation:     P/B vs. sustainable ROE
 Secondary valuation:   P/E on normalised (ex-one-off) earnings
 Not applicable:        EV/EBITDA, unlevered FCF DCF, sum-of-the-parts
--------------------------------------------------------------------------------
 Top 5 must-track:      NIM (ex-one-offs) | GNPA/NNPA (reported vs. ex-partner) |
                        Cost of borrowing | AUM/disbursement growth |
                        CRAR / Debt-Equity
--------------------------------------------------------------------------------
 #1 flag:               Up Money Ltd DA-pool default (~₹19 cr exposure) —
                        the one clear crack in an otherwise best-in-class
                        asset-quality track record; recovery status is the
                        single most important thing to track quarterly
================================================================================
```

---

## INPUT GAPS AND FLAGS

- Interest income by lending vertical is not separately disclosed in the DRHP or FY26 results;
  the vertical mix shown in Section 1C is an AUM-proportion proxy, not an exact P&L split. Flagged
  as an estimation caveat (not an estimated number itself — the AUM percentages are exact and
  anchored; only the read-across to revenue mix is approximate).
- State-wise GNPA/asset-quality breakdown is NOT FOUND in the documents read — a genuine
  monitoring gap given rising geographic diversification into unseasoned states.
- The rating-agency PDF (inputs/rating/ratings.pdf) referenced in operator-context.md as
  scanned/image-only was not part of this stage's injected inputs; the FY26 rating action
  (A- Positive → A/Stable) used above is anchored instead to Investor Presentation slide 5, which
  independently confirms the same fact.
- Investor presentation was available (not absent) — no input_gaps triggered on that count.

---
