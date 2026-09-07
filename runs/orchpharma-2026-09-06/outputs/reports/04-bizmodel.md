# Stage 4 — Business Model Decoder, Orchid Pharma Ltd (ORCHPHARMA)
Run date: 2026-09-06 | Model: claude-sonnet-5

## Scope note (read first)

Orchid Pharma runs two businesses inside one filing, on two different clocks. This report
decodes both separately, as the orchestrator instructed, and names which valuation method
suits which. It also corrects a mismatch Stage 1 flagged: its Gate 0 moat test M8 is written
for FMCG store networks; Orchid sells nothing through stores. Section 3A fixes that.

Primary source: Annual_Report_2025.pdf (FY2025, year ended 31-Mar-2025), the only annual
report in the corpus with a mostly-sound text layer. Its narrative pages (chairman/MD
letters, MD&A, business description, some ratio tables) are tagged [OCR:embedded] (clean).
Its financial statement pages (roughly p.174-224, p.232-300) are tagged
[OCR:embedded-CORRUPT]. Per the corpus rule, no number is taken from a CORRUPT-tagged page
in this report; every figure below carries the specific AR page it came from, and that page's
OCR tag was checked before use. The FY2024 AR is 305-of-318-pages corrupt and is not used for
any figure here, narrative corroboration only, not needed given the FY2025 AR's own two-year
comparatives.

The investor presentation is image-only and unusable (orchestrator instruction); it is not
cited anywhere below. Four own-company concall transcripts (Nov-2025 to Aug-2026) and the
Stage 5 report are used for everything past 31-Mar-2025, since no FY2026 annual report or
audited FY2026 filing exists in this corpus. Every FY2026/FY2027 figure below is
MANAGEMENT-STATED on a concall, not audited, and is labelled as such.

BINDING CORRECTION CARRIED FORWARD (orchestrator Correction 1): FY2026 revenue DECLINED
about 12% on every basis management stated, standalone Rs 811 cr vs Rs 922 cr, or restated-
combined Rs 1,233 cr vs Rs 1,398 cr. The screener's "+34% to Rs 1,233 cr" figure is a
consolidation-scope artifact of the retroactive Dhanuka Laboratories merger and is not used
anywhere in this report as a growth figure.

BINDING CORRECTION CARRIED FORWARD (orchestrator Correction 4): no per-share value, market
cap, or per-share multiple is stated in this run until the share count is resolved against a
primary filing. Where an AR-stated per-share figure (EPS) is unavoidable for this report's
own FY2025 narrative, the share count and its source are stated alongside it, and the
Optionally Convertible Debenture overhang is named every time.

---

## THE TWO ENGINES, IN ONE SENTENCE EACH

**Engine 1 (the business that earns money today):** a 100% Export Oriented Unit at Alathur,
near Chennai, that manufactures Cephalosporin antibiotic API (bulk active ingredient, oral
and sterile, all five generations) and a small, fast-growing Finished Dosage Form (FDF) line,
and sells both on a purchase-order basis to pharmaceutical formulators in 48 countries (AR
p.109), collecting a fixed price per kilogram with almost no pricing power of its own.

**Engine 2 (the business that costs money today and might earn a premium tomorrow):** a set
of funded, not-yet-earning projects, a 7-ACA backward-integration greenfield plant at Jammu
(disclosed total capex Rs 750 cr, Concall_Aug_2026_Transcript.pdf p.9), a Cefiderocol
fill-finish facility with Shionogi/GARDP (disclosed capex USD 20-25m, same source), the
globally-owned Enmetazobactam/Exblifep/Orblicef antibiotic molecule now being licensed
market by market, an oral API capacity expansion, and the Orchid AMS hospital-stewardship
division, plus the now-completed Dhanuka Laboratories merger.

---

# SECTION 1: THE BUSINESS MODEL IN PLAIN ENGLISH

## 1A. One-line description

Orchid Pharma makes and exports bulk antibiotic ingredient (mostly Cephalosporin API) to
drugmakers worldwide on a fixed-price, purchase-order basis, and is spending a large,
currently unprofitable sum trying to turn one plant, one patented molecule, and one hospital
service line into a business with real pricing power.

## 1B. Money flow chain, each revenue stream

**Cephalosporin API (the core business, 98.3% of segment revenue FY25, AR p.22):**
[Chinese/related-party 7-ACA and GCLE intermediates + own fermentation and chemistry] ->
[Orchid manufactures bulk oral and sterile Cephalosporin API at Alathur under USFDA/EMA/DCGI
approval] -> [ships in bulk to a formulator, mostly in Europe, UK, US, Japan and other
regulated/semi-regulated markets] -> [the formulator pays Orchid on invoice, on purchase-order
terms, before turning the API into pills or injections under its own brand] -> [payment is
cash/bank transfer against shipment, not royalty or revenue share].

**Cephalosporin FDF (1.7% of segment revenue FY25, AR p.22, growing off a small base, FY24
Rs 2.46 cr to FY25 Rs 15.09 cr):** [same API, taken one step further in-house into a finished
tablet, capsule, injectable or suspension] -> [Orchid manufactures and packages the finished
drug] -> [sold to formulation customers and marketing partners internationally] -> [invoice
payment, purchase-order basis].

**Enmetazobactam / Exblifep / Orblicef (small, early, growing):** [Orchid's own invented
molecule, a beta-lactamase inhibitor, now 100%-owned after the 2024/25 Allecra Therapeutics
asset acquisition, AR p.14] -> [Orchid manufactures/supplies API and, in India, markets the
finished drug jointly with Cipla under the brand Orblicef] -> [in India: hospitals via Cipla's
sales force and Orchid's own AMS team; ex-India: licensed to a country partner, e.g. Advanz
Pharma in Western Europe, a Russia licensee signed ~Jul-2026 for an estimated $178m over 10
years (Concall_Aug_2026_Transcript.pdf p.4)] -> [India: per-unit sale to hospital/pharmacy
channel; ex-India: upfront/milestone plus royalty licensing payments, structure not disclosed
in this corpus].

**Orchid AMS (Antimicrobial Stewardship, very early):** [Orchid's own clinical/commercial
team] -> [engages hospitals directly with stewardship programmes and antibiotic products,
targeting 2,500-3,000 hospitals, AR p.20] -> [delivers advisory/product access to hospital
pharmacies and physicians, >500 physicians engaged as of the FY25 AR, AR p.14] -> [hospitals
pay per product/service; AMS segment revenue was disclosed for the first time only in Q1 FY27
at Rs 5 cr for the quarter, drag down to Rs 0.5 cr/quarter, Concall_Aug_2026_Transcript.pdf].

**7-ACA (Jammu, via wholly-owned subsidiary Orchid Bio-Pharma Ltd) and Cefiderocol
(pre-revenue, not a revenue stream yet):** capital is being spent now on a PLI-approved 1,000
MT/annum 7-ACA facility (AR p.33) and a Cefiderocol fill-finish line; neither earns revenue as
of the latest data in this corpus. Money flows OUT (capex, debt draw) with no matching inflow
yet.

## 1C. Revenue model classification table

| Stream | Type | Description | % of revenue, anchored | Predictability |
|---|---|---|---|---|
| Cephalosporin API | B2B bulk manufacturing, purchase-order | Sterile + oral bulk active ingredient, all 5 generations | 98.3% of segment revenue, Rs 894.05 cr FY25 vs Rs 812.66 cr FY24 (AR p.22) | M (repeat purchase orders on DMF-locked relationships, but price-taker on a cyclical, China-influenced cost curve) |
| Cephalosporin FDF | B2B finished-dose manufacturing | Tablets/capsules/injectables/suspensions, anti-infective | 1.7% of segment revenue, Rs 15.09 cr FY25 vs Rs 2.46 cr FY24 (AR p.22) | L (small base, early ramp, one year of data only) |
| Enmetazobactam / Orblicef (India) | Branded pharma + partnership | Cephalosporin-class combination drug, hospital channel, Cipla partnership | Not separately disclosed in AR; concall gives patient counts (~30,000 trailing 12m as of Q4 FY26) not rupee revenue | M (patent-protected, but too new and too small to size from filed numbers) |
| Enmetazobactam ex-India licensing | Licensing / out-licensing | Country-by-country rights sold for milestone + royalty economics | Russia deal ~$178m/10yr estimated (concall, signed); US/China undelivered after 4 quarters of "coming soon" language (Stage 5) | L (deal-dependent, binary, repeatedly slipped) |
| Orchid AMS | Hospital services/products | Antimicrobial stewardship engagement plus product sales | Rs 5 cr disclosed for Q1 FY27 only (concall); no FY total in this corpus | L (one data point, pre-breakeven) |
| 7-ACA (Jammu) | Not yet a revenue stream | Backward-integration KSM manufacturing, mostly captive use, some 3rd-party sale planned (80/20 split guided) | 0% currently; Rs 750 cr capex committed (concall) | N/A pre-commissioning |
| Cefiderocol | Not yet a revenue stream | Novel antibiotic, GARDP/Shionogi sub-license, fill-finish manufacturing | 0% currently; USD 20-25m capex committed (concall) | N/A pre-commissioning, launch slipped three times to Q3 FY28 (Stage 5) |

## 1D. Business model canvas (base business, Engine 1)

| Field | Answer |
|---|---|
| What they sell | Bulk Cephalosporin API (oral and sterile) and a small finished-dose line; ingredient, not a branded end product |
| Who buys | Pharmaceutical formulators, on purchase order, largely in Europe, UK, US, Japan and other regulated/semi-regulated markets; exports are 80.10% of turnover (AR p.109) across 48 countries |
| Why them | Broad regulatory dossier base (48 US DMFs, 15 European COS all approved, 8 Japan DMFs, AR p.31), one of only three USFDA-approved Cephalosporin sterile facilities the company claims exist worldwide (AR p.29), legacy since 1992 |
| How delivered | Manufactured at the Alathur EOU plant, exported by sea/air freight against purchase orders |
| Cost structure dominance | Raw material, 63.50% of revenue FY25 vs 64.48% FY24 (AR p.61); the single largest named input is GCLE, sourced almost entirely from a related party, Otsuka Chemicals (India) Pvt Ltd, Rs 230.72 cr FY25 (AR p.148) |
| Scarce resource | USFDA/EMA/DCGI facility approvals and the multi-decade DMF/COS/JDMF filing portfolio; not brand, not distribution |
| Pricing power source or absence | Weak; a price-taker. 7-ACA/Cephalosporin input pricing is set largely by three to four Chinese suppliers (concall); management's own words describe base-business gross margin as cyclical and pressured by "Chinese dumping" |
| Asset intensity | Heavy: Rs 612.9 cr net fixed assets FY25 on Rs 921.93 cr revenue (AR p.23), plus Rs 750 cr+ of incremental committed capex underway |
| WC intensity | High: working capital Rs 548.91 cr FY25 (AR p.26), roughly 59.5% of revenue; inventory turns 1.88x (~194 days), debtor turns 3.2x (~114 days) (AR p.62-63) |
| Regulatory moat or burden | Both. The approvals are the barrier that keeps new entrants out, and simultaneously the compliance cost (evolving US FDA quality-data rules, cited AR p.57) that every year demands fresh investment to keep |

## 1E. The chai-stall-uncle version

Imagine a spice-blend maker who never sells chai to a customer directly. He makes one very
specific, hard-to-copy spice mix in bulk sacks and sells it to hundreds of chai stalls around
the world, each of which brews and sells its own chai under its own name. He gets paid a fixed
price per sack, not a share of what the chai stalls earn, so if cheaper spice floods in from a
rival supplier, his price per sack falls even while global chai demand keeps rising. That is
Orchid's core business: it makes antibiotic "spice" (Cephalosporin API) in bulk and sells it,
mostly abroad, to drugmakers who put it into pills and injections under someone else's brand.
Right now Orchid is also trying to build a second, very different business. It owns one
specific magic spice recipe nobody else has (Enmetazobactam), and it is building an expensive
new kitchen (the Jammu plant) so it no longer has to buy a key raw spice from China. That
second business could one day be sold at a premium, like a chef's signature dish, but it costs
a great deal up front and earns nothing yet.

## Section 1 summary table

| Field | Base business (Engine 1) | Growth engine (Engine 2) |
|---|---|---|
| Business type | B2B bulk manufacturing/export, commodity converter | Pre-revenue project capex plus IP licensing/services, optionality |
| Revenue nature | Purchase-order, price-taker, cyclical | Not yet revenue (7-ACA, Cefiderocol); early and deal-dependent (Enmetazobactam, AMS) |
| Asset intensity | Heavy | Very heavy (single-project capex of Rs 750 cr+) |
| WC intensity | High | N/A pre-revenue; capex-funded |
| Pricing power | Weak, price-taker | Potentially strong if Enmetazobactam licensing and 7-ACA backward integration deliver, unproven today |

---

# SECTION 2: INDUSTRY DYNAMICS & COMPETITIVE POSITION

## 2A. Five forces, plainly

| Force | Answer | Effect |
|---|---|---|
| Competition count | Domestically, management names only three Cephalosporin API players: Orchid, Aurobindo Pharma, Covalent Labs (Concall_Feb_2026_Transcript.pdf p.14). Globally, generic Cephalosporin API supply is far more fragmented, with Chinese suppliers a large factor | Helps domestically (oligopoly), hurts globally on price |
| Entry barriers | High: USFDA/EMA/DCGI facility approval, a 48-DMF/15-COS/8-JDMF portfolio built over decades (AR p.31), heavy capital ( Rs 750 cr for one new intermediate plant alone) | Helps |
| Supplier power | High and concentrated: the key 7-ACA/GCLE intermediate comes from "three to four" named Chinese suppliers (Sinopharm Weiqida, Zhuhai United, Yili Pharmaceutical, Livzon Pharma, Concall_Aug_2026_Transcript.pdf p.6), and the domestic GCLE supply comes from a single RELATED PARTY, Otsuka Chemicals (India) Pvt Ltd, "the only approved source" (AR p.148), Rs 230.72 cr FY25, two Orchid directors are members/director of Otsuka | Hurts, materially |
| Customer power / concentration | AR names "Customer Concentration and Relationship Risk" as a top business risk (AR p.58-59) but discloses no customer-count or top-customer % figure in this corpus | Hurts (risk named), magnitude NOT FOUND |
| Substitutes | Other antibiotic classes exist (macrolides, fluoroquinolones) but Cephalosporins hold specific clinical niches (AR p.28-29); rising antimicrobial resistance is a structural long-run demand driver for novel combinations like Enmetazobactam | Neutral-to-helps long-run; hurts near-term on generic-API commodity substitution among suppliers |

## 2B. Competitive positioning map

Named domestic peers on Cephalosporin API: Aurobindo Pharma, Covalent Labs
(Concall_Feb_2026_Transcript.pdf p.14). The pipeline's own peer set for cross-checks is
NEULANDLAB, GRANULES, KOPRAN. Orchid differentiates from pure-generic peers on two counts not
common in the peer set: it holds a company-invented, globally-approved NCE (Enmetazobactam),
and it claims to be one of only three USFDA-approved sterile Cephalosporin facilities in the
world (AR p.29, unverified independently in this corpus). It differs from peers on leverage
and unproven capex: the Rs 750 cr 7-ACA bet is the single largest capital commitment in the
company's history and has already slipped once on timeline (Stage 5).

## 2C. Moat assessment (eight standard types)

| Moat type | Present? | Evidence | Durability |
|---|---|---|---|
| Brand | No (base business) / emerging (Orblicef in India) | Base business is an ingredient supplier with no end-consumer brand; Orblicef is a named India hospital brand via Cipla (AR p.14) | Low (base) / unproven (Orblicef) |
| Switching costs | Moderate | A customer's own regulatory dossier is tied to Orchid's specific DMF/COS filing; changing supplier requires re-filing, a real but not insurmountable cost | Moderate |
| Network effects | None | Not applicable to bulk API supply | N/A |
| Cost advantages | Claimed, unproven | 7-ACA backward integration is explicitly designed to cut input cost and reduce China dependence (AR p.20); not yet commissioned | Unproven pre-commissioning |
| Intangible assets / IP | Yes, narrow | Enmetazobactam is a company-invented NCE with USFDA, EMA and DCGI approval (AR p.19), "the first NCE from India" to reach both agencies | High on the molecule, small relative to total revenue today |
| Regulatory license / scarcity | Yes, claimed | One of only three USFDA-approved sterile Cephalosporin facilities worldwide per company claim (AR p.29); 48 DMFs, 15 COS (all approved), 8 JDMFs (AR p.31) | High if independently verified; not corroborated against a third party in this corpus |
| Efficient scale | Limited evidence | No filed capacity-vs-demand data beyond concall utilization claims (~60%, down from ~80% two years ago, Stage 5) | Not established |
| Data / technology | Not applicable | Bulk chemistry manufacturing, not a data-driven model | N/A |

## 2D. Industry lifecycle stage and Orchid's position

The base Cephalosporin API business sits in a mature, currently cyclically-depressed segment:
India antibiotic export quantity fell 26% YoY in Q2 FY26 (Stage 5, Concall_Nov_2025 p.3), and
Orchid's own oral segment saw 12% price and 10% quantity erosion in 9M FY26 (Stage 5). Against
that backdrop, Orchid is attempting an early-stage transition into scarcer, higher-value
supply (backward-integrated 7-ACA, a patented novel antibiotic, a hospital-services line), a
transition that is funded and underway but has not yet produced revenue or proven the cost
claims it rests on.

## 2E. Key industry drivers

| Driver | Direction | Impact |
|---|---|---|
| Antimicrobial resistance (AMR) as a global health priority | Secular tailwind | Positive, long-run demand support for novel/newer-generation antibiotics (cited repeatedly by management as the rationale for Enmetazobactam and Cefiderocol) |
| Chinese cost-curve/oversupply dynamics | Cyclical headwind | Negative, near-term pricing pressure on generic Cephalosporin and 7-ACA, cited by management as "dumping" (Stage 5) |
| India PLI scheme for KSM manufacturing | Policy tailwind | Positive, direct incentive of up to Rs 600 cr through FY2028-29 tied to the 7-ACA project (AR p.33) |
| US tariff risk on pharmaceutical imports | Policy headwind | Negative, named explicitly as a risk in the FY25 AR (AR p.57) |
| Evolving US FDA quality-data guidelines | Compliance cost driver | Negative on cost, named as a risk (AR p.57) |
| Russia/CIS geopolitical disruption | Regional headwind | Negative, cited as the driver of a regulated-market mix dip in Q3 FY26 (Stage 5) |

---

# SECTION 3: FINANCIAL METRICS THAT MATTER FOR THIS BUSINESS MODEL

## 3A. Ignore-these, track-these

This directly corrects Stage 1's Gate 0 moat test M8, which is framed for FMCG store
distribution. Orchid has no stores, dealers or consumer-facing distribution network at all in
its core business; it is a purchase-order B2B exporter.

| Commonly tracked ratio | Why it is MISLEADING or IRRELEVANT here |
|---|---|
| Same-store-sales growth, dealer/distributor network size, footfall | IRRELEVANT. Orchid sells B2B on purchase order to a concentrated set of formulator customers, not through stores, dealers or footfall-driven channels. This is the direct correction to Stage 1's FMCG-framed M8 test |
| Brand recall, consumer NPS, advertising-spend ratio | IRRELEVANT for the base business. The end patient never sees "Orchid" on a package; the customer is a pharma manufacturer, not a consumer. Narrowly applicable only to the small, new Orblicef/AMS India hospital brand |
| Inventory turnover benchmarked to retail/FMCG norms (8-12x) | MISLEADING. Bulk API manufacturing with regulated-market QC/release cycles structurally carries long inventory; Orchid's 1.88x turnover (~194 days, AR p.63) looks poor against retail norms but is intrinsic to this archetype, not evidence of poor management |
| Receivable days benchmarked to cash-and-carry retail | MISLEADING. ~114 days (AR p.62) is ordinary for export purchase-order B2B pharma supply, not a red flag by retail standards |
| Gross margin benchmarked to branded/generic formulation companies (60-70%+) | MISLEADING. Orchid is a bulk converter with material cost 63.50% of revenue (AR p.61); a structurally lower gross margin than a branded formulator is the correct shape for this archetype, not a sign of weak differentiation |
| P/E or EV/Sales benchmarked to branded consumer pharma multiples | IRRELEVANT for the base business; a commodity/converter multiple band applies to Engine 1 (Section 1B of the framework governs the exact destination multiple, not decided here). Only the Enmetazobactam licensing stream, if it scales, could ever approach consumer-pharma multiples |
| FY2026 YoY revenue growth read at face value from the screener | MISLEADING, specifically right now. The screener's "+34% to Rs 1,233 cr" mixes a standalone FY25 base against a merger-restated combined FY26 figure; on every basis management stated, FY26 revenue fell ~12% (Correction 1) |
| ROE alone, without a segment-level ROCE | MISLEADING here specifically, because a large and growing slug of FY26/27 capital (7-ACA, Cefiderocol) sits in progress and earns nothing yet, and because Orchid reports a SINGLE operating segment under Ind AS 108 (AR notes, "the operations of the Company falls under a single operating segment"), so no filed number separates the base business's returns from the growth engine's drag |

## 3B. Must-track metrics

### Growth
| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| Organic revenue growth, same consolidation basis only (standalone-vs-standalone or restated-combined-vs-combined, never mixed) | Whether the base business is actually growing or shrinking | Management's own FY27 target: 10-15% (Concall_Jun_2026_Transcript.pdf) | Concalls (AR figures lag by a year; no FY26 AR exists) | Any repeat of the FY26 organic decline of ~12% |
| Oral vs Sterile volume (MT) | Whether growth is volume-led or price-led | Positive volume growth without matching price give-up | AR segment table, annual (AR p.55); concall, quarterly commentary | Volume flat/down with price also down, the pattern seen in 9M FY26 (12% price erosion, 10% volume erosion, Stage 5) |
| Regulated-market mix, % of revenue | Realization quality; regulated markets carry a materially better margin | Historical average ~30% (concall) | Concall only; not disclosed in AR at this granularity | Sustained fall below ~25%, as happened in Q3 FY26 on Russia/CIS disruption |

### Profitability and efficiency
| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| EBITDA margin, base business | Cyclical health of the core converter business | FY25 16.86% (AR p.26); management's own FY27 target ~12% | AR MD&A (annual), concall (quarterly) | Sub-8% for two consecutive quarters, near the FY26 lows of ~6% (Stage 5) |
| Material cost, % of revenue | Direct exposure to 7-ACA/GCLE input cost and China cost-curve swings | FY25 63.50% (AR p.61) | AR MD&A | Sustained move above ~68-70%, signalling structural margin squeeze from input pricing power |
| Interest coverage ratio | Whether operating cash flow still comfortably covers debt cost | FY25 10.69x (AR p.63) | AR MD&A | This figure PRE-DATES the 7-ACA/Cefiderocol debt drawdown; watch for a fall below ~3x once the Rs 450 cr 7-ACA facility is fully drawn against still-ramping EBITDA |

### Balance sheet and risk
| Metric | What it tells you | Healthy range | Where to find | Red flag threshold |
|---|---|---|---|---|
| Net debt / EBITDA, on a clean comparable basis | Overall leverage risk during the capex build | Below ~2x for a capex-heavy transition story | Primary filing needed; currently NOT FOUND on a comparable basis (Correction 2: Stage 1's 4.46x figure mixes consolidation scopes) | Above ~4x, already flagged unverified by Stage 1/Correction 2 |
| Capital work in progress, as % of gross block | Whether the capex build is converting to commissioned, earning assets on schedule | Rising in line with disclosed capex and guided commissioning dates | AR notes (FY25 breakdown NOT FOUND, on CORRUPT-tagged pages); future ARs | CWIP growing while commissioning dates keep slipping, which already happened once (7-ACA Sept-2026 target slipped to March-2027, Stage 5) |
| Related-party raw material concentration (Otsuka/GCLE) | Governance and supply-chain concentration risk in the single largest input | Stable or falling % of material cost, alternate qualified sources in development | AR related-party note (AR p.148 gives FY25 only, Rs 230.72 cr; a trend needs multiple years) | Rising % from the sole related-party source with no alternate supplier named; a direct analyst question on this trend was deflected on the Q1 FY27 call (Stage 5) |

## 3C. Industry-specific non-financial KPIs

| KPI | Value | Where to find |
|---|---|---|
| US DMF count (cumulative) | 48 (30 Cephalosporin, 18 NPNC) | AR p.31, annually |
| European COS count | 15, all approved | AR p.31, annually |
| Japan JDMF count | 8, all Cephalosporin | AR p.31, annually |
| ANDA count (generic formulations) | 6 | AR p.31, annually |
| Capacity utilization | ~60% as of Q3 FY26, down from ~80% two years earlier; management states the plant "can do >Rs 1,200 cr turnover without further capex" | Concall only, quarterly; not disclosed in AR at this granularity |
| 7-ACA project milestones | Mechanical completion and commercial-production dates, most recently reaffirmed March 2027 | Concall opening remarks, every quarter |
| Enmetazobactam licensing geography count | India (Cipla), Europe (Advanz Pharma), Russia (signed ~Jul-2026); US and China "in discussion," no date | Concall, quarterly |
| AMS hospital/physician reach | >500 physicians engaged (AR p.14); target 2,500-3,000 hospitals (AR p.20); ~30,000 patients treated trailing 12m as of Q4 FY26 (concall) | AR narrative (annual), concall (quarterly) |
| USFDA inspection status | Establishment Inspection Report issued with "VAI" status, 2025 (AR p.14) | AR chairman/MD letter; future USFDA postings |

## 3D. Unit economics, base business

**Unit defined:** 1 kilogram of Cephalosporin API sold (the saleable unit of the core
business).

| Category | FY25 | FY24 | Change |
|---|---|---|---|
| Oral volume (MT) | 421.33 | 379.25 | +11.1% (AR p.55) |
| Oral value (Rs cr) | 646.98 | 620.29 | +4.3% (AR p.55) |
| Oral realization (Rs/kg, computed from the above) | ~1,536 | ~1,636 | -6.1% |
| Sterile volume (MT) | 154.94 | 106.76 | +45.1% (AR p.55) |
| Sterile value (Rs cr) | 246.10 | 191.36 | +28.6% (AR p.55) |
| Sterile realization (Rs/kg, computed from the above) | ~1,588 | ~1,792 | -11.4% |

The realization-per-kg figures are computed here from the AR's own volume-and-value data
(AR p.55, a clean OCR page); the AR itself does not state a per-kg price. The finding: even in
FY25, a reported "growth" year on revenue, per-kg realization FELL on both product lines while
volume rose. This precedes and is consistent with the sharper price erosion management later
described for 9M FY26 (12% price, 10% volume erosion on the oral line, Stage 5).

- **Revenue per unit:** ~Rs 1,536-1,588/kg blended FY25 (computed, see table).
- **Cost per unit:** NOT FOUND at the segment level; only a company-wide material cost ratio
  is disclosed, 63.50% of revenue FY25 (AR p.61).
- **Volume drivers:** capacity utilization (60% at Q3 FY26 per concall), regulated-market
  demand recovery, new product launches (Ceftaroline/ORTARO, a Teflaro generic, Ceftolozane-
  Tazobactam, per Stage 5).
- **Price drivers:** the global 7-ACA/Cephalosporin cost curve, set largely by three to four
  Chinese suppliers; regulated vs non-regulated mix (regulated markets carry a materially
  better margin, a 40-65% gross margin band was cited once on a call, Stage 5); rupee/yuan FX.
- **Cost drivers:** 7-ACA/GCLE input price, exposed both to the Chinese cost curve and to the
  single related-party domestic GCLE supplier (Otsuka); utility and compliance cost; export
  freight and logistics.
- **Incremental margin / operating leverage:** HIGH and asymmetric between the two engines.
  Management states the EXISTING base-business plant can do more than Rs 1,200 cr of turnover
  without further capex, against ~Rs 811-922 cr actually achieved (concall, Stage 5), implying
  real operating leverage on any base-business volume recovery, before the 7-ACA capacity even
  comes online. The second engine currently shows the opposite: zero revenue against Rs 750 cr+
  of committed capex, meaning fixed interest and depreciation cost with no offsetting income
  until commissioning, exactly the mechanical path from EBITDA to a collapsed PBT that
  Correction 1 describes as INFERRED (management has never itself discussed PBT on any call).

---

# SECTION 4: RISKS, VALUATION APPROACH & MONITORING

## 4A. Business-model-specific risks

| Category | Risk | First financial line item that would deteriorate |
|---|---|---|
| Revenue model | China oversupply/dumping depresses generic Cephalosporin pricing further | Oral segment price-erosion %, and the material-cost-to-revenue ratio (AR p.61 baseline 63.50%) |
| Margin | Concentrated raw material supply, both the Chinese 7-ACA supplier group and the sole related-party domestic GCLE source (Otsuka, AR p.148) | Material cost % of revenue rising above the FY25/FY24 band |
| Balance sheet | 7-ACA/Cefiderocol capex overrun or further timeline slip while the plants earn nothing | CWIP growth outpacing the disclosed Rs 750 cr capex schedule; or continued non-disclosure of total debt/cash (already dropped from the concall record since Q3 FY26, Stage 5) |
| Execution | Repeated commissioning-date slips: 7-ACA mechanical completion moved from an earlier AR-stated December 2026 (AR p.15) to a concall-stated September 2026 target (Q3 FY26 call) and then back out to March 2027 (Q4 FY26 call); Cefiderocol commercial launch has slipped three times to Q3 FY28 (Stage 5) | Any further slip past the newly reaffirmed March 2027 / Q3 FY28 dates at the next concall |
| Structural | Single reportable operating segment under Ind AS 108; no filed split of capital employed or ROCE between the earning base business and the pre-revenue growth engine | Continued absence of segment-level capital-employed/ROCE disclosure in the next annual report |

Note on the 7-ACA date: the FY2025 AR itself (Board's report dated 26-May-2025) states
"mechanical completion expected by December 2026 and commercial production targeted for March
2027" (AR p.15). The Q3 FY26 concall (Feb-2026) then gave a MORE aggressive September 2026
mechanical-completion target than the AR's own December 2026, before the Q4 FY26 concall
revised back out to "Q1 CY2027" (~March 2027), converging back near the AR's original date.
This is an internal chronology inconsistency across sources, flagged here, not resolved.

Note on 7-ACA capex: the AR itself cites Rs 600 crore total investment in the Jammu greenfield
facility (AR p.20). The Q1 FY27 concall discloses total project capex of Rs 750 crore
(Concall_Aug_2026_Transcript.pdf p.9), a roughly 25% increase over the figure stated in the
FY2025 annual report. This is a capex overrun on the company's own numbers and is flagged as
such.

## 4B. Valuation method applicability

This is a formal handoff to the Stage 11 valuation. The two engines cannot be valued on the
same method or the same multiple.

| Method | Applicability | Notes |
|---|---|---|
| **PRIMARY: Sum-of-the-parts** | Applicable, and the only defensible top-level approach | Engine 1 (base business, commodity converter) needs a cyclical-normalized EV/EBITDA or P/E, at the destination multiple Section 1B of the framework governs, not invented here. Engine 2 needs a DCF/NPV on the disclosed 7-ACA project economics (cost-saving/backward-integration case) PLUS a risked, probability-weighted option value for Enmetazobactam ex-India licensing and Cefiderocol (both regulatory- and deal-timing-dependent, binary in nature). Blending the two into one multiple misprices both, and Amendment 17 forbids feeding spot-year converter-business ROCE or rupee working-capital trends into Section 1B for a CONVERTER-classified name, reinforcing SOTP over a single blended read |
| **SECONDARY: Replacement/build-cost cross-check** | Applicable to the 7-ACA project specifically | Rs 750 cr disclosed capex (concall) is a hard, checkable number against any DCF-implied value for the backward-integration project, a useful sanity check on whether the market is pricing it above or below what it cost to build |
| **TERTIARY: Peer EV/EBITDA** | Applicable, base business only, as a market cross-check | Peer set: Aurobindo Pharma, Covalent Labs (named domestically on concall); NEULANDLAB, GRANULES, KOPRAN (pipeline peer set). Kept tertiary because peers differ materially in scale, ROCE and product mix from Orchid's base business |
| **NOT APPLICABLE: Dividend Discount Model** | Not applicable | No dividend recommended for FY25 or FY24; the Board explicitly retains profits to fund capex (AR p.32); no dividend history exists to model |
| **NOT APPLICABLE: Any per-share (P/E, EPS-multiple) method** | Not applicable until resolved | Correction 4: the post-merger share count does not reconcile (5.07 cr AR-standalone vs 5.99 cr implied by market cap/price vs 9.53 cr pre-merger-plus-allotment), and up to ~14.3 crore further shares can convert at Rs 10 par from the promoter's Zero Coupon OCDs. No per-share valuation method can be applied until this is resolved against a primary filing |
| **NOT APPLICABLE: A single blended EV/EBITDA multiple across both engines** | Not applicable | Conflates an operating, cyclical, price-taking business with pre-revenue project capex and deal-dependent optionality; produces a number that is wrong for both parts |

Cycle stage for valuation purposes: the base business is currently MID-DOWNCYCLE, recovering
from a trough. FY26 organic revenue fell ~12% (Correction 1), but Q1 FY27 delivered +15% YoY
on a restated-combined basis with gross margin improving from 30% to 33% (concall, Stage 5).
Valuation should use a normalized, mid-cycle earnings base for Engine 1, not the FY26 trough
print, and not an unadjusted extrapolation of one strong recovery quarter.

## 4C. Quarterly monitoring checklist

1. Revenue YoY, ONLY on a consistent basis (standalone-vs-standalone or restated-combined-vs-
   combined); confirm the basis before comparing.
2. Oral/Sterile volume (MT) and computed realization (Rs/kg), annual from AR, directional from
   concall.
3. Material cost, % of revenue.
4. EBITDA margin, base business, isolated from Dhanuka-combined figures where possible.
5. PBT/PAT, a disclosure never once given on any of the four concalls to date; watch for
   reintroduction.
6. Total debt and cash, dropped from disclosure after Q3 FY26; watch for reintroduction, red
   flag if it stays dropped through a leverage-building period.
7. 7-ACA mechanical completion / commercial production status against the March 2027 target.
8. 7-ACA total capex against the disclosed Rs 750 cr figure; any further increase is a red
   flag.
9. Cefiderocol commissioning and India launch date against the Q3 FY28 target.
10. Enmetazobactam ex-India licensing deal count, beyond Russia; any newly signed deal in the
    quarter.
11. AMS quarterly EBITDA/drag, trending toward the FY27 breakeven guidance.
12. Regulated-market mix, % of revenue.
13. Otsuka Chemicals (India) related-party transaction value and % of material cost.
14. Capacity utilization, %.
15. Dhanuka merger synergy realization, in bps of EBITDA margin, once combined reporting
    stabilizes.

## 4D. Highest-value questions for management

| Question | Answer that reassures | Answer that worries |
|---|---|---|
| What is PBT/PAT for the quarter, and how much of the EBITDA-to-PBT gap is interest/depreciation from pre-revenue 7-ACA/Cefiderocol capex versus the base business? | A clean bridge, EBITDA to PBT, with capex-related items isolated | Continued refusal to give the number, as on all four calls to date |
| What is total debt and cash as of this quarter-end, and net debt/EBITDA on a comparable basis? | A stated, comparable figure with 7-ACA facility utilization tracked | Another quarter of no disclosure during a leverage-building phase |
| What is the trend in Otsuka Chemicals (India) GCLE purchases as a % of material cost over five years, and what alternate sources exist? | A declining or capped %, with named alternate suppliers in qualification | A rising % with no alternate source named, as on the deflected Q1 FY27 question |
| Beyond Russia, is there a second signed Enmetazobactam ex-India licensing deal? If not, why has the timeline slipped four consecutive quarters? | A signed deal, or a specific, held date | Continued vaguer language with no date |
| Has the 7-ACA total capex figure of Rs 750 crore changed since first disclosed, and is the March 2027 commercial-production date still firm? | Capex unchanged, date reaffirmed with an interim milestone met | A further capex increase or a further date slip |
| What is the post-merger issued and paid-up share count, and what are the conversion terms and current holder intent for the Rs 143 crore Zero Coupon OCDs? | A clear, filed share count and a stated intent/lock-up on the OCDs | Continued ambiguity, or a signal of near-term conversion at par |
| What capital employed and ROCE apply to the base API/FDF business alone, separate from the 7-ACA/Cefiderocol/Enmetazobactam capital pool, given the company reports only one operating segment? | A voluntary internal split | Continued refusal, leaving no way to judge whether the base business's own returns justify its own capital, let alone the growth engine's |

---

# SECTION 5: ONE-PAGE BUSINESS MODEL SUMMARY CARD

```
ORCHID PHARMA LTD (ORCHPHARMA) — BUSINESS MODEL SUMMARY CARD

BUSINESS TYPE:        Manufacturing (B2B bulk API/FDF exporter), with an early,
                       pre-revenue second engine (licensing + hospital services + KSM
                       backward integration)

WHAT THEY SELL:        Bulk Cephalosporin API (oral + sterile), a small FDF line, and,
                       emerging, a patented antibiotic (Enmetazobactam) plus hospital
                       stewardship services (AMS)

WHO BUYS:              Pharmaceutical formulators worldwide, purchase-order basis;
                       80.10% of turnover is exports, 48 countries (AR p.109)

REVENUE MIX (FY25):    Cephalosporin API 98.3% | Cephalosporin FDF 1.7% (AR p.22)
                       [Enmetazobactam / AMS: too small/new to size from filed numbers]

ASSET INTENSITY:       Heavy (Rs 612.9 cr net fixed assets FY25, AR p.23, plus Rs 750 cr+
                       of committed incremental capex)

WC INTENSITY:          High (working capital ~59.5% of revenue FY25, AR p.26; inventory
                       ~194 days, receivables ~114 days, AR p.62-63)

PRICING POWER:         Base business: weak, price-taker, set by 3-4 Chinese suppliers on
                       the key input. Growth engine: potentially strong (patent,
                       backward-integration cost edge) if and when it delivers, unproven

CYCLICALITY:           Cyclical. FY26 organic revenue fell ~12% on every basis
                       management stated (Correction 1); Q1 FY27 shows early recovery

TOP MOATS:             Regulatory dossier depth (48 US DMFs, 15 COS, 8 JDMFs, AR p.31),
                       moderate/durable. Enmetazobactam NCE patent, high but narrow.
                       Claimed 1-of-3 USFDA sterile facility status, high if verified

TOP RISKS:             Related-party/China concentration on the key raw material
                       (Otsuka GCLE, sole source, Rs 230.72 cr FY25, AR p.148); 7-ACA
                       capex already up ~25% (Rs 600cr AR to Rs 750cr concall) and one
                       timeline slip; PBT/debt disclosure dropped since Q3 FY26 (Stage 5)

VALUATION METHOD:      PRIMARY: sum-of-the-parts (converter multiple for Engine 1 per
                       Section 1B + DCF/risked-option value for Engine 2).
                       SECONDARY: replacement-cost cross-check on the Rs 750 cr 7-ACA
                       capex. TERTIARY: peer EV/EBITDA, base business only.
                       NOT APPLICABLE: DDM; any per-share method until the share count
                       reconciles (Correction 4); a single blended multiple

ONE-LINE VERDICT:      Two businesses in one filing: a price-taking API exporter is
                       funding an unproven premium bet, and the filings do not yet let
                       an investor see either one clearly on its own.
```

---

```yaml
stage: B04-bizmodel
company: "ORCHPHARMA"
run_date: "2026-09-06"
model: claude-sonnet-5
status: complete
input_gaps:
  - "results: no quarterly or annual results filing in corpus"
  - "rating: no credit rating bulletin or rationale in corpus"
  - "announcements: no exchange / Reg 30 filings in corpus"
  - "shareholding: no quarterly shareholding pattern in corpus"
  - "research: no broker notes in corpus (non-anchored; no evidence effect)"
  - "screening: Profit_Loss, Balance_Sheet, Cash_Flow, Quarters CSVs are empty templates (collect_to_repo v3 defect); Data_Sheet used in their place"
  - "presentation: image-based, 3124 chars over 14 pages; unusable, treated as not provided"
  - "FY2026 primary filings absent: no FY2026 annual report and no FY2026 audited annual results filing"
  - "annual report PDFs carry a corrupt OCR text layer across the financial statements"
flags:
  - "Base business and growth engine are structurally different and must not be valued on one blended multiple; Section 4B gives the sum-of-the-parts handoff"
  - "Stage 1 Gate 0 moat test M8 is written for FMCG store distribution; Orchid has no store/dealer network at all, it is a purchase-order B2B exporter (Section 3A)"
  - "Otsuka Chemicals (India) Pvt Ltd is a RELATED PARTY and the sole approved source of GCLE, a key raw material, Rs 230.72 cr FY25 (AR p.148); a direct analyst question on this trend was deflected on the Q1 FY27 concall (Stage 5)"
  - "7-ACA disclosed total capex rose from Rs 600 cr (AR p.20) to Rs 750 cr (Q1 FY27 concall), a ~25% increase on the company's own numbers"
  - "7-ACA mechanical-completion date is internally inconsistent across sources: AR states December 2026 (AR p.15), Q3 FY26 concall stated a more aggressive September 2026, Q4 FY26 concall revised back out to ~March 2027"
  - "Orchid reports a SINGLE operating segment under Ind AS 108; no filed split of capital employed or ROCE exists between the earning base business and the pre-revenue growth engine"
  - "No per-share value, market cap or per-share multiple is used anywhere in this report; where FY25 AR-stated EPS (Rs 20.99) is cited, the share count (5.07 cr, AR p.23, pre-merger standalone) and the OCD overhang are stated alongside it per Correction 4"
business_type: "manufacturing"
revenue_streams:
  - {name: "Cephalosporin API", type: "B2B bulk manufacturing, purchase-order", pct_of_revenue: 98.3, predictability: "M"}
  - {name: "Cephalosporin FDF", type: "B2B finished-dose manufacturing", pct_of_revenue: 1.7, predictability: "L"}
  - {name: "Enmetazobactam / Orblicef (India + ex-India licensing)", type: "Branded pharma + IP licensing", pct_of_revenue: 0, predictability: "L"}
  - {name: "Orchid AMS (hospital stewardship)", type: "Services/products, hospital channel", pct_of_revenue: 0, predictability: "L"}
asset_intensity: "heavy"
wc_intensity: "high"
pricing_power: "price-taker"
cyclicality: "cyclical"
moats_present:
  - {moat: "Regulatory dossier depth (48 US DMFs, 15 COS, 8 JDMFs, 6 ANDAs)", durability: "moderate-high"}
  - {moat: "Enmetazobactam NCE patent, USFDA/EMA/DCGI approved", durability: "high on the molecule, narrow relative to total revenue"}
  - {moat: "Claimed 1-of-3-worldwide USFDA-approved sterile Cephalosporin facility status", durability: "high if independently verified, unverified in this corpus"}
  - {moat: "7-ACA backward-integration cost advantage", durability: "unproven, pre-commissioning"}
valuation_methods:
  primary: {method: "Sum-of-the-parts: converter-multiple EV/EBITDA or P/E (Section 1B destination multiple) for the base business, plus DCF/NPV and risked-option value for the growth engine", why: "The two engines have fundamentally different earnings bases, one operating and cyclical, one pre-revenue and deal-dependent; blending them misprices both, and Amendment 17 forbids feeding spot-year converter metrics into a blended read"}
  secondary: {method: "Replacement/build-cost cross-check on the disclosed Rs 750 cr 7-ACA capex", why: "A hard, management-disclosed capital figure gives a sanity check on what the market should pay for the backward-integration project alone"}
  tertiary: {method: "Peer EV/EBITDA (Aurobindo Pharma, Covalent Labs domestically; NEULANDLAB, GRANULES, KOPRAN pipeline peer set), base business only", why: "Market cross-check only; peers differ materially in scale, ROCE and mix so this stays tertiary"}
  not_applicable:
    - "Dividend Discount Model: no dividend recommended FY25 or FY24, profits retained for capex (AR p.32)"
    - "Any per-share (P/E, EPS-multiple) method until the post-merger share count and OCD overhang are resolved against a primary filing (Correction 4)"
    - "A single blended EV/EBITDA multiple across both engines: conflates an operating cyclical business with pre-revenue project capex"
irrelevant_ratios:
  - {ratio: "Same-store-sales growth / dealer network size", why: "Orchid has no store or dealer distribution; it sells B2B on purchase order (direct correction to Stage 1's FMCG-framed M8 test)"}
  - {ratio: "Brand recall / consumer NPS / advertising-spend ratio", why: "No consumer ever sees the Orchid brand on the core API/FDF product; the customer is a pharma manufacturer"}
  - {ratio: "Inventory turnover vs retail/FMCG norms (8-12x)", why: "Bulk regulated API manufacturing structurally carries ~194 days inventory (1.88x turns, AR p.63); this is intrinsic to the archetype, not mismanagement"}
  - {ratio: "Receivable days vs cash-and-carry retail norms", why: "~114 days (AR p.62) is ordinary for export purchase-order B2B pharma, not a red flag by retail standards"}
  - {ratio: "Gross margin vs branded/generic formulation companies (60-70%+)", why: "Orchid is a bulk converter with material cost 63.5% of revenue (AR p.61); a lower gross margin is structurally correct for this archetype"}
  - {ratio: "FY2026 YoY revenue growth taken from the screener aggregate at face value", why: "Mixes a standalone FY25 base against a merger-restated combined FY26 figure; organic FY26 revenue actually fell ~12% on every basis management stated"}
must_track_metrics:
  - {metric: "Material cost, % of revenue", healthy: "below ~65% (FY25 63.5%, AR p.61)", red_flag: "sustained above ~68-70%"}
  - {metric: "Net debt / EBITDA, comparable basis", healthy: "below ~2x", red_flag: "above ~4x (Stage 1's 4.46x is unverified, scope-mixed per Correction 2)"}
  - {metric: "7-ACA commissioning-date adherence", healthy: "March 2027 met or beaten", red_flag: "any further slip"}
  - {metric: "Regulated-market mix, % of revenue", healthy: "above ~30%", red_flag: "sustained below ~25%"}
  - {metric: "PBT/PAT quarterly disclosure", healthy: "given each quarter with a capex/interest bridge from EBITDA", red_flag: "continued non-disclosure, as on all four calls to date"}
unit_economics:
  unit: "1 kilogram of Cephalosporin API sold"
  revenue_per_unit: "~Rs 1,536/kg oral, ~Rs 1,588/kg sterile, FY25 blended (computed from AR p.55 volume-and-value data; both realizations FELL from FY24 despite volume growth)"
  margin_per_unit: "NOT FOUND at segment level; company-wide material cost is 63.50% of revenue FY25 (AR p.61)"
  key_lever: "Capacity utilization on a largely fixed base-business plant: management states >Rs 1,200 cr turnover is achievable without further capex against ~Rs 811-922 cr actually achieved, implying high operating leverage on any volume recovery, before the 7-ACA capacity even comes online"
first_deterioration_signals:
  - {risk: "China oversupply/dumping depresses generic Cephalosporin pricing further", first_signal: "Oral segment price-erosion %, and material cost as % of revenue rising above the FY25/FY24 band"}
  - {risk: "Concentrated raw material supply (China + sole related-party Otsuka GCLE source)", first_signal: "Material cost % of revenue rising above the FY25/FY24 baseline"}
  - {risk: "7-ACA/Cefiderocol capex overrun or further timeline slip while pre-revenue", first_signal: "CWIP growth outpacing the disclosed Rs 750 cr schedule, or continued non-disclosure of total debt/cash"}
  - {risk: "Repeated commissioning-date slips", first_signal: "Any further slip past the newly reaffirmed March 2027 (7-ACA) / Q3 FY28 (Cefiderocol) dates"}
  - {risk: "No segment-level capital-employed/ROCE split under single-segment reporting", first_signal: "Continued absence of a base-business-only ROCE disclosure in the next annual report"}
mgmt_questions:
  - "What is PBT/PAT for the quarter, and how much of the EBITDA-to-PBT gap is interest/depreciation from pre-revenue 7-ACA/Cefiderocol capex versus the base business?"
  - "What is total debt and cash as of this quarter-end, and net debt/EBITDA on a comparable basis?"
  - "What is the five-year trend in Otsuka Chemicals (India) GCLE purchases as a % of material cost, and what alternate sources exist?"
  - "Beyond Russia, is there a second signed Enmetazobactam ex-India licensing deal, and if not, why has the timeline slipped four consecutive quarters?"
  - "Has the 7-ACA total capex figure of Rs 750 crore changed since first disclosed, and is the March 2027 commercial-production date still firm?"
  - "What is the post-merger issued and paid-up share count, and what are the conversion terms and current holder intent for the Rs 143 crore Zero Coupon OCDs?"
  - "What capital employed and ROCE apply to the base API/FDF business alone, given the company reports only one operating segment?"
one_line_verdict: "A price-taking API exporter is funding an unproven premium bet, and neither is visible alone in the filings."
analyst_note: "Two internal inconsistencies are worth carrying into Stage 11 and 13. First, 7-ACA capex rose from Rs 600 cr (AR p.20, mid-2025) to Rs 750 cr (Q1 FY27 concall, Aug-2026), a ~25% overrun on the company's own numbers, not previously flagged elsewhere in this pipeline. Second, the AR's own December-2026 mechanical-completion target (AR p.15) was briefly superseded by a MORE aggressive September-2026 target on the Q3 FY26 call before slipping back out to March 2027, an internal chronology conflict across AR and concall sources that is flagged, not resolved. Third, Orchid reports a single operating segment under Ind AS 108, so no filed number anywhere in this corpus separates the earning base business's capital employed and ROCE from the pre-revenue growth engine's; every ROCE figure Stage 1 or Stage 11 uses is necessarily a blended, whole-company number until management volunteers a split. Unit economics computed in 3D (Rs/kg realization) are MY OWN calculation from AR-stated MT and value figures on a clean page, not a company-stated per-kg price, flagged as computed throughout."
```
