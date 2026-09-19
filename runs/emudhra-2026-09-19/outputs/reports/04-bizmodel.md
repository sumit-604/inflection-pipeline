# STAGE 4: BUSINESS MODEL DECODER — eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19. Primary source: FY26 Annual Report (AR2026.txt, [page N]
markers = PDF page numbers). Secondary source: Q4FY26 Investor Presentation
(7-May-2026) and Q1FY27 Investor Presentation (30-Jul-2026). All rupee
figures are INR Million on the face of the AR and results filings unless
marked Cr (screener/company-memory convention); 10 INR Mn = 1 INR Cr.

---

## SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

### 1A. One-line description

eMudhra runs a government-licensed digital-identity factory in India and
sells owned cybersecurity software (signing, identity, certificate
management) to enterprises worldwide, and the software line is now growing
faster than the license line (AR p.55, p.90; Q4FY26 Inv. Pres. slide 6).

### 1B. Money flow chain, one chain per revenue stream

**Stream 1: Trust Services — Digital Signature Certificates (DSC) and eSign
(India-heavy)**
[Government CCA licence + verified identity data + emSign root certificate
accredited by WebTrust] → [eMudhra verifies an individual's or an
organisation's identity and issues a legally valid digital certificate
under its licensed Certifying Authority status] → [delivers a DSC/eSign
token or credential, 2-year validity is the standard product] → [an
individual or business that must sign tax filings, tenders, bank KYC or
contracts pays] → [one-time or 2-year fee, ~Rs 1,500 for a 2-year DSC,
paid mostly through CA-led partners (~70%) who take a 45-50% commission,
~30% direct-to-consumer] (AR p.147, p.156-157; Q4FY26 Inv. Pres. slide 8).

**Stream 2: Trust Services — SSL/TLS certificates (global)**
[WebTrust-accredited root, browser trust-store listing] → [eMudhra issues
website/device certificates under the CA/Browser Forum framework] →
[delivers a TLS/SSL certificate priced USD 6-50/year] → [website operators
and TLS resellers, mostly outside India, pay] → [annual subscription fee,
increasingly automated as certificate validity compresses toward 47 days
by 2029] (Q4FY26 Inv. Pres. slide 8; AR p.157).

**Stream 3: Enterprise Solutions — owned platform (emSigner, SecurePass,
CertiNext/emCA, emSign-as-a-service)**
[Proprietary software IP, 17 years of R&D, data centres in Bengaluru, New
Jersey, Salt Lake City and Europe] → [eMudhra licenses and deploys its
signing, identity/access-management and certificate-lifecycle-management
platform, on-premise, private cloud or public cloud] → [delivers an
integrated "one-stop-shop" platform rather than point products] →
[large enterprises in BFSI, government/defence and general enterprise, 240
new ones added in FY26] pay → [licence fee plus subscription, direct
(60%) or partner-led (40%), a mix of recurring and one-time licence
revenue] (AR p.55, p.86-89, p.148; Q4FY26 Inv. Pres. slide 6, 13).

**Stream 4: Services — consulting and integration**
[A US-based delivery bench, built via the Ikon Tech and Two95
International acquisitions] → [eMudhra consults on and integrates
digital-transformation programmes, often around its own or a client's
existing stack] → [delivers project-based consulting] → [enterprise
clients, mainly in the US, in Utilities, Education and Financial
Services] pay → [time-and-materials or project fee; flat, 0.1% YoY growth
in FY26] (AR p.90; Q4FY26 Inv. Pres. slide 6).

### 1C. Revenue model classification table

| Stream | Type | Description | % of FY26 revenue (anchor) | Predictability |
|---|---|---|---|---|
| Trust Services (DSC/eSign, domestic) | Licensed-transaction fee | Per-certificate/per-signature fee under a Government of India CA licence | 20% (AR p.55, "By line of business"; consol Rs 1,400.08 Mn of Rs 7,015.80 Mn, AR p.288 Note 49) | Medium-High (recurring renewal need, but exposed to single-regulator/single-geography risk, AR p.156) |
| Trust Services — SSL/TLS (global) | Subscription fee | Annual certificate fee, USD 6-50 | Sub-component of the 20% above; separately reported as "6% of FY26 Trust Revenue" (Q4FY26 Inv. Pres. slide 8) | Medium (commoditised at the low end by free issuers such as Let's Encrypt, Q4FY26 Inv. Pres. slide 8) |
| Enterprise Solutions (owned platform) | Software licence/subscription | emSigner, SecurePass, CertiNext/emCA sold globally | 59% (AR p.55, Q4FY26 Inv. Pres. slide 6; +55% YoY, of which organic +23 pts / inorganic +32 pts, Q4FY26 Inv. Pres. slide 6 footnote) | Medium (65% of total company revenue is described as "recurring," Q4FY26 Inv. Pres. slide 5, but per-contract renewal terms are NOT FOUND in this corpus) |
| Services (consulting/integration) | Project/time-and-materials | Digital-transformation consulting via US bench | 21% (AR p.55; +0.1% YoY, Q4FY26 Inv. Pres. slide 6) | Low (flat, project-lumpy by nature) |

Cross-check: the AR's Ind AS 108 segment note (Note 49, AR p.288) reports
only two segments — Trust Services and Enterprise Solutions — because it
folds the investor-presentation's "Services" line into "Enterprise
Solutions" ("Enterprise solutions includes emSigner, emAS, emCA and other
development services," AR p.288). The 59%/20%/21% split is an investor
presentation convenience, not a statutory segment; anchor accordingly.

### 1D. Simplified business model canvas

| Dimension | Reading |
|---|---|
| What they sell | A licensed identity credential (DSC/eSign/SSL) in India and abroad, plus an owned software platform for signing, identity/access management and certificate lifecycle |
| Who buys | Individuals and SME/retail (DSC), enterprises in BFSI/government/defence globally (platform), and mid-market clients via the US services bench |
| Why them | "One-stop shop": five/six capabilities (issue, sign, authenticate, manage certificate lifecycle, govern data privacy) from one architecturally coherent platform vs. rivals who specialise (AR p.13, "Competitors specialise. eMudhra integrates") |
| How delivered | On-premise, private cloud or public cloud; own data centres in Bengaluru, New Jersey, Salt Lake City and (via Cryptas) Europe (AR p.148) |
| Cost structure dominance | Employee costs (19.46% of consolidated revenue, AR p.152) and "cost of goods sold" — a bundle of commission expense, direct personnel cost and third-party stock-in-trade (46.2% of consolidated revenue FY26, AR p.151-152) |
| Scarce resource | The Government of India Controller of Certifying Authorities (CCA) licence, renewed every 5 years, plus WebTrust accreditation and browser root-store listing — only 24 licensed Indian CAs exist, 10 actively issuing (Q4FY26 Inv. Pres. slide 8) |
| Pricing power source or absence | Present but segment-specific: switching costs for enterprises with PKI/CLM wired into critical systems (67% of FY26 revenue from existing customers, AR p.55); largely absent at the DSC commodity end (24 competing Indian CAs, AR p.157-158) |
| Asset intensity | Light on the organic core (data centres, capitalised R&D); now acquisition-heavy — goodwill nearly tripled to Rs 2,940.46 Mn FY26 from Rs 1,254.60 Mn FY25 (B02 finding 3, Note 4a/2.5a) |
| WC intensity | High and worsening in FY26: FCF turned negative (Rs -525.19 Mn / -Rs 52.5 Cr, AR p.155-156 cash-flow table; B03), trade payables +91% YoY and unbilled revenue +40.6% YoY, both ahead of 35.1% revenue growth (B02 Pattern A) |
| Regulatory moat or burden | Both. Moat for the licensed Trust Services slice (20% of revenue); burden for cross-border expansion, which needs a fresh in-country trust licence per geography (UAE QTSP application pending with TDRA as of Q1FY27, Q1FY27 Inv. Pres. slide 12) |

### 1E. The chai-stall-uncle version

Think of eMudhra as two shops sharing one counter. One shop is a
government-licensed stamp-and-notary window: it verifies who you are and
sells you a digital ID card (a DSC), the way a notary stamps a document,
except it is one of only 24 shops in India allowed to do this. That shop
is steady but its prices are fixed by competition among the 24. The
second shop, next door, sells software subscriptions that let big
companies sign documents, manage passwords and issue certificates
worldwide, the way a locksmith sells a whole security system instead of
one lock. That second shop is growing faster, especially abroad, because
eMudhra just bought a European locksmith (Cryptas) and an American one
(AI Cyberforge) to get into new countries quickly. The notary window pays
the rent while the software shop tries to become the bigger business.

**Section 1 summary table**

| Field | Value |
|---|---|
| Business type | Hybrid: licensed trust-services utility (20% of revenue) + owned enterprise-security software platform (59%) + project consulting (21%) |
| Revenue nature | Mixed: renewal-fee (Trust), subscription/licence (Enterprise Solutions), project-fee (Services); company states 65% of total revenue is "recurring" (Q4FY26 Inv. Pres. slide 5) |
| Asset intensity | Light organically; heavier and rising post-acquisition (goodwill/intangibles) |
| WC intensity | High, deteriorating in FY26 (negative FCF, payables/unbilled revenue outrunning sales) |
| Pricing power | Present in Enterprise Solutions (switching costs, IP); weak-to-absent in commodity DSC/SSL |

---

## SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

### 2A. Five forces, plainly

| Force | Reading | Helps / Hurts / Neutral |
|---|---|---|
| Competition count | High per product silo: SSL/TLS (DigiCert, Entrust, Sectigo, GlobalSign); IAM (Microsoft, IBM, Ping, Okta, Sailpoint, Saviynt, Thales, Broadcom); PKI/cert discovery (Thales, HID, Keyfactor, Entrust, Nexus, AppViewX, Venafi); eSignature (Adobe, OneSpan, DocuSign, WISeKey) — all named global players (AR p.157-158). In India, 24 licensed CAs, 10 actively issuing (Q4FY26 Inv. Pres. slide 8) | Hurts on any single product line; helps on the combined "one-stop shop" positioning, where the AR states "very few competitors globally... none of them have the one-stop shop positioning" (AR p.86) |
| Entry barriers | High for Trust Services: CCA licence (5-year renewal, yearly audit), WebTrust accreditation, browser root-store acceptance (AR p.147, p.157). Moderate for Enterprise Solutions: 17 years of accumulated IP and EAL 4+/CMMI L5/ISO certifications, but global vendors with larger R&D budgets compete directly (AR p.13, p.157-158) | Helps (Trust); Neutral-to-hurts (Enterprise, where scale of R&D spend matters and eMudhra spends 7-8% of revenue vs. 15-20% at global software peers, Q4FY26 Inv. Pres. slide 9) |
| Supplier power | Dependent on cloud infrastructure providers (AWS, Google, named as competitors/suppliers in the same table, AR p.158) and hardware security module vendors (Thales, HID); ultimately dependent on continued browser-root-store acceptance of its own certificate root | Hurts (a single point of failure: loss of browser trust-store listing would be existential for the CA business) |
| Customer power / concentration | Top 5 customers fell from 32% (FY24) to 22% (FY26) of revenue; top 10 customer concentration also declining; customers contributing >Rs 5 Cr rose from 12 (FY24) to 25 (FY26); 67% of FY26 revenue from existing customers (AR p.57, "Revenue concentration") | Helps (diversifying, reduces single-customer leverage) |
| Substitutes | Real substitute risk at the commodity end: any of the other 23 Indian CAs for a basic DSC, or a free/low-cost global SSL issuer (Let's Encrypt named explicitly, Q4FY26 Inv. Pres. slide 8); lower substitute risk once an enterprise is wired into the PKI/CLM stack (switching cost argument, AR p.55, 67% existing-customer revenue) | Hurts (Trust commodity end); Helps (embedded Enterprise accounts) |

### 2B. Competitive positioning map (named competitors from the documents)

| Category | Named global competitors | eMudhra's stated positioning |
|---|---|---|
| SSL/TLS certificates | DigiCert, Entrust, Sectigo (all USA), GlobalSign (Belgium) | Lower-cost Bangalore delivery base vs. higher-cost global players (AR p.158) |
| Digital Signature Certificates | DigiCert, Entrust (USA), GlobalSign (Belgium) | "Only Indian CA" WebTrust-accredited and listed in major browser trust stores (Q1FY27 Inv. Pres. slide 11) |
| IoT device certificates | DigiCert, Entrust (USA), GlobalSign (Belgium) | Same PKI stack reused across use cases (product breadth) |
| Identity and Access Management | Microsoft, IBM, Ping Identity, Okta, Sailpoint, Ilantus, Saviynt, Broadcom (all USA), Thales (France) | Converged identity fabric (SecurePass) bundled with certificate issuance, not sold standalone (AR p.158) |
| PKI / certificate discovery | Thales, HID Global, Keyfactor (hardware); Entrust, Nexus Group, DigiCert, Sectigo, AppViewX, Venafi (software) | Owns both certificate issuance (emCA) and lifecycle/discovery (CertiNext) under one roof (AR p.158) |
| Cloud infrastructure | Google, AWS (USA) | Infrastructure dependency, not a competitor in the product sense, but named in the same risk table (AR p.158) |
| Paperless transformation / eSignature workflow | Adobe, OneSpan, DocuSign (USA), Alpha Trust (USA), WISeKey (Switzerland) | emSigner processes 300,000-500,000+ signing workflows/day (figures differ between the two investor decks, see Section 3C note); G2 "Leader" in Small Business eSignature, Asia (Q1FY27 Inv. Pres. slide 11) |
| Indian licensed CA market | Safescrypt, IDRBT, (n)Code Solutions, CDAC, Capricorn, Protean, V Sign, CDSL Ventures, Pantasign, ProDigiSign, Care 4 Sign, IGCAR and others (AR p.158 table) | Claims market leadership by value (~38% share, Frost & Sullivan 2024, Q4FY26 Inv. Pres. slide 8) |

The step-1 peer set (NEWGEN, QUICKHEAL, PROTEAN) does not appear inside
the AR's own named-competitor tables; it is a screener-based proxy set for
listed comparables, not the company's stated competitive set. Company
memory correctly flags no listed Indian pure-play PKI/CA peer exists.

### 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | Partial | "Only Indian CA" WebTrust-accredited (Q1FY27 slide 11); G2 Leader, IDC #1 of 42 vendors in India Identity & Digital Trust (Q1FY27 slide 11); niche brand, not mass-market | Medium |
| Switching costs | Yes | 67% of revenue from existing customers (AR p.55); PKI/CLM wired into critical government/banking systems; customer concentration falling suggests broadening, not churning, base (AR p.57) | High |
| Network effects | Not evidenced | Trust-store/browser relationship is a regulatory dependency, not a two-sided network effect on revenue | Low / not present |
| Cost advantage | Yes, partial | Bangalore delivery centres explicitly cited as lower cost than global rivals (AR p.158) | Medium (labour-cost arbitrage can erode) |
| Intangible assets (licence/IP) | Yes, segment-specific | CCA licence (5-year renewal), WebTrust accreditation, EAL 4+/CMMI L5/ISO certifications (AR p.147, p.157); protects the 20% Trust Services slice strongly, protects the 80% Enterprise+Services slice more weakly (software IP, not licensed) | High (Trust); Medium (Enterprise) |
| Efficient scale | Partial | Niche global category (PKI-as-a-service) with few integrated players; Frost & Sullivan names eMudhra a "Competitive Strategy Leader" (Q4FY26 Inv. Pres. slide 15) | Medium |
| Data advantage | Not evidenced | NOT FOUND in this corpus | N/A |
| Distribution / channel | Yes, partial | CA-led partner distribution ~70% for DSC (commission 45-50%) vs. direct 60% / partner-led 40% for Enterprise Solutions (AR p.55; Q4FY26 Inv. Pres. slide 8) | Medium |

**Moat class read (cross-check against B01):** Gate 0 (B01) independently
scored moat_score 17/20, moat_class STRONG, moats_confirmed 4. This
stage's qualitative read is consistent: switching costs and the
licence/IP moat are the strongest, durable pillars; cost advantage and
distribution are real but softer.

### 2D. Industry lifecycle stage and eMudhra's position

Global cybersecurity spend: $213 Bn (2025) to a projected $240 Bn (2026),
+12.5% (Gartner, cited AR p.144). Global Cyber Security and Paperless
Transformation industry growth: 21.2% FY26-FY28 (Frost & Sullivan, Q4FY26
Inv. Pres. slide 7). Global Trust Services growth: 13.0% FY26-FY28 (Frost
& Sullivan 2024, Q4FY26 Inv. Pres. slide 8). Global PKI-as-a-Service
market growing above 30% annually (Frost & Sullivan 2025 Best Practices
report, Q1FY27 Inv. Pres. slide 11). Reading: the industry sits in a mid
secular-growth phase, accelerating rather than maturing, driven by AI
agentic-identity, post-quantum migration and shortening certificate
validity (47 days by 2029). eMudhra's own position: Trust Services
(mature, India-led, growing near the slower 13% Trust Services industry
rate at 32.3% in FY26, i.e. taking share) alongside Enterprise Solutions
(growing faster than the 21.2% industry rate at 55% reported / 23%
organic, i.e. also taking share, partly via acquisition).

### 2E. Key industry drivers

| Driver | Direction | Impact on eMudhra |
|---|---|---|
| AI-driven machine identity growth (agents, APIs, workloads) exceeding human identity count | Accelerating | Positive: core rationale for the "Agentic AI Security Platform" pitch (AR p.13; Q1FY27 Inv. Pres. slide 7) |
| Certificate validity compression, 398 days toward 47 days by 2029 (CA/Browser Forum) | Structural, mandated | Positive: forces automation, benefits CertiNext/CLM adoption (AR p.153; Q1FY27 Inv. Pres. slide 8) |
| Post-quantum cryptography migration deadlines (2029 critical infra, 2030 high-priority enterprise, India DST) | Structural, mandated | Positive: crypto-agility a stated R&D focus area across all four platforms (Q4FY26 Inv. Pres. slide 9) |
| NIS2/DORA (Europe) and DPDP (India)/GDPR compliance mandates | Regulatory tailwind | Positive: drives Cryptas/Primesign cross-sell in Europe and the in-development PrivaTrust data-privacy product (Q1FY27 Inv. Pres. slide 8, 12) |
| CCA distribution-model change (July 2024) forcing per-end-customer invoicing | Regulatory, one-off disruption already absorbed | Negative, transitional: caused the DSC stock-repurchase charge that inflated standalone COGS in FY25/FY26 (AR p.151); recurrence risk flagged, first signal in Section 4A |
| Global growth slowdown (IMF: 3.2% 2025 to 3.1% 2026) | Modest headwind | Neutral-to-negative on enterprise IT budgets generally, not eMudhra-specific (AR p.144) |

---

## SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

### 3A. Ignore-these-track-these

| Commonly tracked ratio | Verdict | Why it misleads here |
|---|---|---|
| Inventory turnover / days inventory | IRRELEVANT | "Stock-in-trade" is CA-partner pass-through inventory (DSC tokens), not a manufacturing input; the CCA-mandated business-model change in July 2024 already forced a one-off repurchase distortion in this line (AR p.151) |
| Gross margin vs. pure-SaaS peers | MISLEADING | Reported COGS (46.2% of consolidated revenue, AR p.151) bundles commission expense, direct personnel cost, stock-in-trade purchase and inter-company transfer pricing; not comparable to a hosting-only SaaS cost stack |
| Reported P/E alone | MISLEADING | Company reports both PAT and "Adjusted PAT" (which strips ESOP provisioning and notional interest on acquisition liability, e.g. Rs 1,100 Mn vs Rs 1,218 Mn FY26, AR p.55); using unadjusted PAT alone overstates the swing from one-off M&A accounting noise |
| Debt/Equity, interest coverage | IRRELEVANT AS A RISK SIGNAL | Net cash position, D/E 0.03x (B01); the real leverage to watch is the off-balance-sheet-style contingent consideration and put/call option (Rs 881.45 Mn, uncapped upside), not funded debt |
| Receivable days in isolation | MISLEADING | Receivable days alone look stable-to-improving (92-96 days, AR p.57), but read together with unbilled revenue (+40.6% YoY) and trade payables (+91% YoY), both outrunning 35.1% revenue growth, the true cash-conversion picture is deteriorating (B02 Pattern A, B03 FLAG-CASH) |
| Fixed asset turnover, FY26 vs. FY25 | MISLEADING (post-acquisition distortion) | Fixed assets roughly doubled (screener Rs 419 Cr to Rs 727 Cr) almost entirely from Cryptas/AI Cyberforge goodwill and intangibles, not from organic capacity build; any turnover ratio computed FY26 vs. prior years compares two different asset bases |

### 3B. Must-track metrics

**Growth**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Enterprise Solutions organic growth (ex-Cryptas/AI Cyberforge) | Whether the core software platform is winning share on its own, not just via M&A | FY27 guide 15-18% organic (company memory, NOT in this AR text); FY26 disclosed split was organic +23 pts / inorganic +32 pts of the 55% total (Q4FY26 Inv. Pres. slide 6) | Quarterly results press release / concall (not itemised in the AR MD&A) | Organic growth below ~10-12%, i.e. materially under guide |
| Order book (Enterprise Solutions only) | Forward revenue visibility | Rs 2,380 Mn, +24.8% YoY, "mix of recurring + license revenue" (Q4FY26 Inv. Pres. slide 24) | Investor presentation "FY2027 stats and assumptions" slide | Growth below ~15% or flat/declining book |
| Recurring revenue % of total | Revenue-quality proxy for a platform business | 65% of FY26 total revenue (Q4FY26 Inv. Pres. slide 5) | Investor presentation performance highlights | Falling below ~55-60% |
| International revenue growth | Tests the core transition thesis (India CA to global software vendor) | +38.7% FY26, 64% of revenue (AR p.90, p.147) | AR MD&A, Board's Report | Growth decelerating toward domestic (27.6%) rate or below |

**Profitability and efficiency**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Segment operating margin, Enterprise Solutions Outside India | Whether the international expansion is actually profitable yet, or still subsidised | FY26: 21.9% (Rs 957.98 Mn / Rs 4,375.72 Mn); FY25: 26.0% (Note 49, AR p.288) | AR Note 49, Segment Information | Sustained decline below ~15-18% for more than two quarters |
| Segment operating margin, Enterprise Solutions India | Benchmark for what the international book should eventually reach | FY26: 57.5% (Rs 712.92 Mn / Rs 1,240.00 Mn); FY25: 51.1% (Note 49, AR p.288) | AR Note 49 | A widening (not narrowing) gap to the international margin over 2-3 years |
| Consolidated EBITDA margin | Blended profitability across the whole mix shift | FY26: 23.2%; FY25: 23.8% (comparable quarter read, Q1FY27 Inv. Pres. slide 19); Q1FY27: 26.2% | AR/results highlights | Margin compression below ~20% for two consecutive quarters |
| Effective tax rate | Geography-mix dependent, a swing factor for EPS | FY26 consolidated 16.2% vs. 25.5% standalone (AR p.152) | AR MD&A "Provision for tax" | A jump toward the 25.17% statutory rate without an explained cause (jurisdiction mix shift) |
| R&D capitalisation vs. amortisation | Tests whether R&D spend is being expensed honestly or parked on the balance sheet | Organic IP investment Rs 601 Mn FY26 (~8.4% of revenue, Q4FY26 Inv. Pres. slide 5), vs. the useful-life extension to 10 years that cut FY26 amortisation by ~Rs 39.96 Mn (B02 finding 7, Note 5a(iii)(a)) | AR cash-flow investing activities; Note 5 | A repeat estimate-change that further softens amortisation while capitalisation keeps rising |

**Balance sheet and risk**

| Metric | What it tells you | Healthy range | Where to find it | Red flag threshold |
|---|---|---|---|---|
| Free cash flow (CFO minus capex) | Cash-earnings quality through the acquisition/capex cycle | FY26: Rs -525.19 Mn (Rs -52.5 Cr), first negative print in the two years shown; capex +122.8% YoY vs. CFO +30.8% (AR p.155-156; B03) | AR cash-flow statement | A second consecutive negative FCF year |
| Goodwill + contingent consideration as % of net worth | Size of the acquisition-accounting tail risk | Goodwill Rs 2,940.46 Mn = 32.3% of net worth; contingent consideration Rs 881.45 Mn (Note 4a/17a, B02/B03) | AR Note 4a, 17a, Balance Sheet | Any impairment charge, or the contingent-consideration liability growing faster than Cryptas' own disclosed EBITDA trajectory |
| MSME overdue payables | A frozen statutory-compliance signal, small but persistent | Rs 21.61 Mn unchanged across two ARs, 100% of the >3-year overdue bucket (Note 40/43, B02) | AR MSME note | A third consecutive year unresolved |
| Net cash / working-capital-funded growth | Whether growth is self-funding or eating cash | Net cash Rs 1,268.48 Mn (AR p.155); but payables (+91%) and unbilled revenue (+40.6%) both outrun 35.1% revenue growth (B02 Pattern A) | AR cash-flow statement, Notes 8/18 | Net cash position shrinking while WC growth continues to outrun revenue growth |

### 3C. Industry-specific non-financial KPIs

| KPI | FY26 / latest value | Where to find it |
|---|---|---|
| Licensed CAs in India (competitive set size) | 24 total, 10 actively issuing | Q4FY26 Inv. Pres. slide 8 |
| DSC market share by value | ~38% (Frost & Sullivan, 2024 estimate) | Q4FY26 Inv. Pres. slide 8 |
| Enterprise customer count | 1,374 | AR p.55 |
| Customers contributing >Rs 5 Cr revenue | 25 (FY26), 18 (FY25), 12 (FY24) | AR p.57 |
| Existing vs. new customer revenue split | 67% existing / 33% new | AR p.55 |
| New enterprise customers added | 240 in FY26 | AR p.90 |
| Offices / countries served | 15 offices, 35+ countries | Q1FY27 Inv. Pres. slide 5 |
| Group headcount | 850+ (Q1FY27 Inv. Pres. slide 5) vs. 861 reported as "the Company's" (standalone) employees, up from 851 (AR p.152) — NOTE: these two figures are not on a like-for-like consolidated basis; treat the AR figure as standalone-entity headcount only, flagged, not reconciled here |
| emSigner daily signing volume | "500,000+ signing workflows a day globally" (Q1FY27 Inv. Pres. slide 5) vs. "300,000+ workflows completed per day in India" (Q4FY26 Inv. Pres. slide 6/9) — two different scopes (global vs. India), not a discrepancy once read carefully |
| WebTrust / browser trust-store status | Ongoing accreditation, "only Indian CA listed in major browser trust stores" | AR p.147; Q4FY26 Inv. Pres. slide 15 |
| R&D headcount | 200+ people | AR p.149 |
| Order book (Enterprise Solutions) | Rs 2,380 Mn, +24.8% YoY | Q4FY26 Inv. Pres. slide 24 |

### 3D. Unit economics — the physics of the business

eMudhra genuinely runs two different unit economics. Both are stated
because averaging them would hide the story.

**Unit A: one 2-year Digital Signature Certificate (Trust Services, India retail)**

| Item | Value | Source |
|---|---|---|
| Unit | One 2-year-validity DSC | Q4FY26 Inv. Pres. slide 8 |
| List price to end customer | ~Rs 1,500 | Q4FY26 Inv. Pres. slide 8 |
| Cost to deliver | CA-partner commission 45-50% of the fee where sold through the ~70% partner channel; lower cost where sold direct (~30%) | Q4FY26 Inv. Pres. slide 8 |
| Volume driver | eSignature/DSC volume growth (Trust Services +32.3% YoY FY26, "due to higher eSignature volumes," AR p.90); B2G filing mandates and Registration Bill-driven C2C eSign adoption (Q4FY26 Inv. Pres. slide 8) |
| Price driver | Largely regulated/competitive among 24 CAs; company does not describe price increases as a growth lever |
| Cost driver | Partner commission rate (45-50%) is the single biggest determinant of unit contribution margin |
| Incremental margin / operating leverage | High at the margin once the licence/infrastructure is in place (segment operating margin on the whole Trust Services line was 31.4% FY26, 36.4% FY25, on Note 49 data) — but note the *trend* is down, not up, as commission-heavy partner mix and CCA-model disruption costs weigh |

**Unit B: one enterprise Enterprise Solutions account (global platform)**

| Item | Value | Source |
|---|---|---|
| Unit | One enterprise customer contract (deal size/ACV not disclosed) | NOT FOUND — no per-deal ACV, contract length or net-revenue-retention figure is disclosed anywhere in the AR or the two investor presentations |
| Revenue per unit | NOT FOUND at per-account granularity; only aggregate revenue per bucket (customers >Rs 5 Cr = 25 accounts, AR p.57) |
| Volume driver | New enterprise customer adds (240 in FY26, AR p.90); order book conversion (2.2-2.3x next-year revenue per company memory, NOT FOUND directly in this AR text) |
| Price driver | Platform breadth ("one-stop shop") supports premium pricing per the company's own claim (AR p.13); no disclosed price realisation metric |
| Cost driver | Employee cost (19.46% of consolidated revenue, up from 17.6%, "due to addition of senior management resources in overseas geographies," AR p.152) is the main incremental cost of international expansion |
| Incremental margin / operating leverage | Segment data shows this is NOT yet high-leverage internationally: Outside-India Enterprise segment margin compressed from 26.0% (FY25) to 21.9% (FY26) even as revenue grew 38.3%, the opposite of the operating-leverage story the "mix shift" thesis implies for FY26 specifically (Note 49, AR p.288) |

---

## SECTION 4: RISKS, VALUATION APPROACH & MONITORING

### 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | Regulatory/channel disruption in the licensed Trust Services line, as already happened once (CCA distribution-model change, July 2024, forcing a partner stock-repurchase charge, AR p.151) | Trust Services segment revenue growth (Note 49) turning negative, or a repeat stock-repurchase/other-expenses spike in COGS |
| Margin | International Enterprise Solutions expansion stays structurally lower-margin than the India book, or takes longer to close the gap than priced in (segment margin already compressed 26.0% to 21.9% FY26, Note 49) | Outside-India Enterprise Solutions segment operating margin (Note 49), quarter over quarter |
| Balance sheet | Cryptas/AI Cyberforge contingent consideration (Rs 881.45 Mn, uncapped on the EBITDA upside) or the 2028-2030 49% put/call option crystallises well above the current fair value (B02/B03 red flag) | The "Interest on contingent consideration" finance-cost line (Note 29) and the Note 17a liability balance, quarter over quarter |
| Execution | Acquisition integration underperforms, as already happened once with the smaller Two95 earn-out (partial miss, Rs 13.01 Mn upside-bonus reversal, Note 53(a), B02 finding 12) | Any disclosed movement in Cryptas actual EBITDA vs. the implicit 10x contingent-consideration target (B03 monitorable) |
| Structural | Loss of, or a qualification to, WebTrust accreditation or browser root-store listing, which underwrites the entire Trust Services franchise and the "only Indian CA" claim | Any qualified WebTrust audit opinion, or a browser vendor distrust/removal notice (not disclosed as having occurred; a tripwire, not a current fact) |

### 4B. Valuation method applicability

| Method | Applicable? | Reasoning |
|---|---|---|
| P/E (on reported and adjusted PAT) | **PRIMARY** | Profitable every year since FY19 (B01), clean core cash-earnings quality (CFO/PAT >1x both years, B03), EPS-driven strategy already tracked by the company itself via its own "Adjusted PAT" disclosure (AR p.55) |
| DCF | **SECONDARY** | Multi-year revenue visibility from the order book (Rs 2,380 Mn, +24.8% YoY, Enterprise Solutions only, Q4FY26 Inv. Pres. slide 24) and the stated 65% recurring-revenue base support a forward cash-flow build; the FY26 FCF dip (capex/M&A driven, B03) means near-term free cash flow needs normalising, not extrapolating, before DCF is applied |
| EV/Sales (Enterprise Solutions slice only) | **TERTIARY** | Useful as a cross-check specifically on the higher-growth, still-thin-margin international Enterprise Solutions segment against global cybersecurity/IAM peers named in Section 2B, none of which are Indian-listed and comparable on a whole-company basis |
| Sum-of-the-parts / SOTP | NOT APPLICABLE | Two Ind AS 108 segments exist (Note 49) but no standalone segment financial statements or clean peer multiples exist for the Trust Services slice alone; the licensed-CA "peer" universe (24 CAs) has almost no listed comparables |
| Dividend discount model | NOT APPLICABLE | Payout is modest (Rs 1.25/share proposed FY26, AR p.55) against a growth-and-reinvestment strategy; dividend is not the return driver |
| Asset-based / replacement value | NOT APPLICABLE | Core value is IP, licence and customer relationships, not replaceable physical assets; goodwill/intangibles from recent M&A make book value a poor proxy for economic value |

**Which cycle stage matters for valuation:** eMudhra is not commodity-cyclical.
It is mid-transition on its own quality ladder, from a licence-protected,
India-concentrated Trust Services base toward a globally-sold software
platform. Valuation should be anchored to the *destination* segment
economics (the India Enterprise Solutions segment's 51-58% margin as the
plausible steady state, not the currently-dilutive 22-26% international
segment margin, Note 49), not to the FY26 acquisition-year trough. Per
CLAUDE.md, the actual exit multiple is a Section 1B determination
downstream of this stage; this handoff names method and cycle-stage
context only.

### 4C. Quarterly monitoring checklist (10-15 items)

1. Enterprise Solutions revenue growth, organic vs. total (split not disclosed quarterly in the AR text; requires results/concall triangulation) — good: organic tracking or beating the 15-18% FY27 guide; trouble: organic materially below guide while total growth is propped up by Cryptas/AI Cyberforge comps rolling through the base.
2. Order book (Enterprise Solutions) — good: growth sustaining near or above the 24.8% FY26 print; trouble: flat or declining book.
3. Segment operating margin, Outside-India Enterprise Solutions (Note 49, annual disclosure; approximate quarterly from results segment data if provided) — good: narrowing gap to the India segment margin; trouble: further widening.
4. Consolidated EBITDA margin — good: holding at or above the 23.2% FY26 level, ideally trending toward the 26.2% Q1FY27 print; trouble: sustained compression.
5. Free cash flow (CFO minus capex) — good: return to positive; trouble: a second consecutive negative year.
6. Trade payables and unbilled revenue growth vs. revenue growth (Notes 8/18, annual; monitor via results balance sheet quarterly) — good: converging back toward the revenue growth rate; trouble: continuing to outrun it.
7. Cryptas contingent consideration balance (Note 17a) and the "Interest on contingent consideration" finance-cost line (Note 29) — good: growth in line with disclosed Cryptas EBITDA; trouble: growth ahead of any disclosed operating performance.
8. Goodwill impairment-test disclosure — good: FY27 AR finally discloses discount rate/growth rate/headroom; trouble: another year of silence, or any impairment charge.
9. MSME overdue payables (Note 40/43) — good: the frozen Rs 21.61 Mn finally resolved; trouble: a third consecutive frozen year.
10. 3i Infotech claim status (Note 36(f)/38(e)) — good: formally dropped or capped; trouble: escalation to a civil suit or SEBI complaint (per company memory load-bearing fact 3).
11. Effective tax rate — good: stable near 16-18% consolidated; trouble: unexplained drift toward the 25.17% statutory rate.
12. Recurring revenue % of total — good: holding near or above 65%; trouble: declining, implying more one-time/project mix.
13. Customer concentration (top 5/top 10) — good: continuing the FY24-FY26 declining trend; trouble: reversing upward.
14. R&D capitalisation vs. amortisation policy — good: no further useful-life extensions without disclosed justification; trouble: another estimate change that flatters margin in an acquisition year.
15. Promoter-family board composition and KMP remuneration (CFO pay +42.4% FY26, unexplained, B03 FLAG-GOVERNANCE) — good: explained and normalised; trouble: further unexplained increases alongside the April-2026 promoter-family board expansion.

### 4D. Highest-value questions for management

1. **Cryptas/AI Cyberforge organic split.** What exact revenue did Cryptas and AI Cyberforge contribute to FY26 and Q1FY27 growth, so organic growth can be cleanly separated from acquired growth? *Reassures:* a clean number matching the FY27 organic guide of 15-18%. *Worries:* an evasive answer, or a number inconsistent with the segment note.
2. **The India-vs-international Enterprise margin gap.** Note 49 shows India Enterprise Solutions margin at 57.5% and Outside-India at 21.9% in FY26. What is the specific plan and timeline to close that gap? *Reassures:* a concrete cost/scale roadmap. *Worries:* "scale will fix it" with no specifics.
3. **Contingent-consideration sensitivity.** What EBITDA/revenue trajectory for Cryptas is embedded in the Rs 881.45 Mn contingent-consideration fair value, and is there any ceiling on the mechanic? *Reassures:* disclosed discount rate and scenario bands. *Worries:* continued refusal to disclose Level 3 sensitivity.
4. **FY27 free cash flow path.** Is the FY26 capex spike (product development plus data-centre build) now largely behind the company, or does capex of this scale recur? *Reassures:* capex guided down as a % of revenue for FY27. *Worries:* capex guided flat or up again without a named driver.
5. **The frozen MSME balance.** Why has the Rs 21.61 Mn MSME payable sat overdue and unchanged across two consecutive annual reports? *Reassures:* a specific, named dispute with a resolution path. *Worries:* no explanation offered.
6. **Definition of "recurring revenue."** What contractual basis defines the 65% "recurring revenue" figure — is it subscription/licence revenue under multi-year contract, or does it include repeat-but-not-contracted project revenue? *Reassures:* a tight, auditable definition. *Worries:* a loose definition that overstates revenue quality.
7. **Promoter-family board and CFO pay.** Why were two promoter-family members added to the board effective just after FY26 year-end, and why did CFO remuneration rise 42.4% YoY, well above the 7.1% median-employee increase? *Reassures:* a specific, disclosed rationale tied to responsibility change. *Worries:* no rationale offered (B03 FLAG-GOVERNANCE).

---

## SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
+---------------------------------------------------------------------+
| eMudhra Ltd (EMUDHRA) — BUSINESS MODEL SUMMARY CARD                 |
+---------------------------------------------------------------------+
| ONE-LINE: Licensed Indian digital-identity issuer funding a global  |
| enterprise security-software platform bet; the software line is    |
| now bigger and growing faster than the licence line.                |
|                                                                       |
| BUSINESS TYPE:      Hybrid (licensed trust utility + owned software |
|                      platform + project services)                   |
| REVENUE STREAMS:     Trust Services 20% | Enterprise Solutions 59%  |
|                      | Services 21% (AR p.55)                       |
| RECURRING REVENUE:   65% of total (Q4FY26 Inv. Pres. slide 5)       |
| ASSET INTENSITY:     Light organically; rising fast post-M&A        |
|                      (goodwill Rs 2,940.46 Mn, +134% YoY)            |
| WC INTENSITY:        High, deteriorating (FY26 FCF -Rs 52.5 Cr)     |
| PRICING POWER:       Segment-split — moderate/strong in Enterprise  |
|                      Solutions (switching costs); weak at the       |
|                      commodity DSC end (24 competing Indian CAs)    |
| CYCLICALITY:         Secular-growth (AI/agentic identity, PQC       |
|                      migration, shortening cert validity are all    |
|                      structural tailwinds, not cyclical demand)     |
|                                                                       |
| TOP 3 MOATS:         1. Switching costs (67% existing-customer      |
|                         revenue) — HIGH durability                  |
|                      2. Licensed-CA regulatory moat (Trust Services |
|                         20% of revenue) — HIGH durability, narrow   |
|                         scope                                       |
|                      3. Bangalore cost-of-delivery advantage vs.    |
|                         global rivals — MEDIUM durability           |
|                                                                       |
| KEY RISK:            Contingent consideration (Rs 881.45 Mn,        |
|                      uncapped on EBITDA upside) + goodwill (32.3%   |
|                      of net worth) with no disclosed impairment     |
|                      sensitivity                                     |
| VALUATION METHOD:    PRIMARY P/E | SECONDARY DCF | TERTIARY EV/Sales|
|                      (Enterprise Solutions slice only)               |
| FIRST WATCH ITEM:    Outside-India Enterprise Solutions segment     |
|                      margin (21.9% FY26, down from 26.0% FY25)      |
+---------------------------------------------------------------------+
```

---

## Anchoring and gap notes carried from prior stages

- Sector cap row: B00 set "Platform / SaaS / IT services" and flagged the
  "Cybersecurity / VAD" row (distribution with vendor certifications) as
  wrong for this name. This stage's own evidence supports the B00 read:
  eMudhra owns its PKI/identity/signing IP outright (AR p.13, "Our
  technology is fully in-house and proprietary," AR p.158) rather than
  distributing third-party-certified security products, and the combined
  Enterprise Solutions + Services lines (80% of revenue, Note 49) are
  software/services, not resale. The 21% Services line (consulting via
  the US bench) is the one piece that reads closer to project services
  than owned-IP software; it does not, on its own, justify a distribution
  classification for the whole company. CONFIRMED, not contested.
- Load-bearing fact 1 (organic vs. acquired growth): this stage adds a
  cleaner, AR/investor-presentation-anchored split than the company
  memory estimate. FY26 Enterprise Solutions growth was +55% YoY,
  disclosed as organic +23 points and inorganic +32 points (Q4FY26 Inv.
  Pres. slide 6, footnote). That is a segment-level split, not a
  whole-company split; whole-company organic growth for FY26 or Q1FY27 is
  NOT directly disclosed in this corpus and remains a concall/company-memory
  estimate (~19% FY26, ~15% Q1FY27 per company memory), not verified here.
- Load-bearing fact 2 (cash conversion): fully addressed in Section 3B/4A
  and cross-checked against B02/B03; FY26 FCF is confirmed negative
  (Rs -525.19 Mn) directly from the AR cash-flow statement (AR p.155-156),
  resolving the B01 discrepancy noted in that stage's analyst_note.
- Load-bearing fact 4 (asset build): addressed in Section 1D and 3B; the
  AR's own investing-activities note (AR p.155-156) splits FY26 capex into
  existing-product enhancement (Rs 124.62 Mn), new product development
  (Rs 476.38 Mn), data centre/server (Rs 213.21 Mn) and acquisitions net
  of assets acquired (Rs 1,101.35 Mn) — a materially different breakdown
  from the total capex figure carried in B01/B03 (Rs 1,853.68 Mn PPE +
  intangibles), because the two do not use the same line-item boundary.
  Flagged for reconciliation, not resolved in this stage.
- Investor presentation was provided (both Q4FY26 and Q1FY27 decks); no
  input_gaps for Section 4B's "primary source is the AR" rule.
