# Stage 9: TAM / SAM / SOM Market Sizing — Fabtech Technologies Ltd (FABTECH)
Run date: 2026-08-04 | Model: claude-sonnet-5

---

## SEARCH LOG

**Performed:**
1. "pharmaceutical cleanroom market size 2026 Middle East Africa forecast" (WebSearch) — returned Fortune Business Insights MEA cleanroom-HVAC figures.
2. WebFetch of fortunebusinessinsights.com cleanroom-HVAC page — **failed, HTTP 403**; worked around using the WebSearch snippet data instead (partial substitute, lower confidence on that one data point).
3. "pharmaceutical engineering EPC turnkey construction market size global 2026 CAGR" (WebSearch) — general EPC market CAGR benchmarks (no pharma-specific breakout found).
4. "'pharmaceutical cleanroom' market size billion 2025 2030 CAGR report" (WebSearch) — surfaced wide dispersion across Research & Markets / Grand View / Mordor / Fortune Business Insights vendor estimates ($5.8bn–$27.8bn for materially the same category), used as evidence that paid third-party reports are unreliable for this specific niche and should carry Low confidence.
5. "USD INR exchange rate August 2026" (WebSearch) — spot rate ≈ ₹95.4/$1 (4-Aug-2026), used for all $→₹ conversions in this report (flagged as a market-rate assumption, not a company-disclosed figure).
6. "Southeast Asia pharmaceutical manufacturing capex investment market size billion 2025 2029" (WebSearch) — found ASEAN pharma *product*-market and CDMO-market sizing, but **no SE Asia pharma facility/equipment capex figure** comparable to the CRISIL MEA/India capex data. Logged as a genuine gap (see input_gaps).

Document reads (not web searches, but exhaustive across all five injected source PDFs): Q1 FY27 Investor Presentation (20/20 pages), Aug-2026 concall transcript / Q1 FY27 earnings call (24/24 pages), Apr-2026 concall transcript / Q4-FY26 & FY26 earnings call (23/23 pages), FABTECH RHP/Prospectus Industry Overview section (pages 157–201 of the document, i.e. the full "Industry Overview" chapter) plus cover/TOC pages for navigation.

**Skipped:** None outright skipped; one WebFetch attempt failed (403) and was worked around with search-snippet data (see #2). No independent broker/equity research was available to cross-check (input_gaps). Status is **complete**, not partial, because every planned line of inquiry was ultimately answered (directly or via an explicitly-flagged gap), not silently dropped.

---

## SECTION 1: MARKET DEFINITION

### 1A — Precise boundaries

**Product scope (in):** Turnkey EPC delivery of pharmaceutical/biotech/healthcare **facility infrastructure** — cleanrooms, HVAC, process utilities, MEP — plus **standalone process-equipment/machinery supply** (Process, Air, Water pillars), design-to-validation single-point-responsibility contracts. This is the CRISIL RHP's own category: "pharmaceutical turnkey engineering solutions" / "pharmaceutical capex solutions providers" (RHP p.179, p.194).

**Product scope (out):** (i) The pharmaceutical **product** market itself (drugs/APIs/formulations) — that is a $1,583bn global / $51bn MEA / Rs 4.5 trillion India market (CRISIL, RHP p.164, p.168, p.172) that Fabtech does not participate in; (ii) pure R&D capex (~20% of total pharma capex per CRISIL/PhRMA benchmark, RHP p.164–165, p.185); (iii) regulatory capex — licences, regulatory approvals, know-how/software (RHP p.178 capex taxonomy chart); (iv) land acquisition; (v) non-pharma cleanroom/EPC demand (semiconductor, data centre, solar) — management is explicit that this belongs to a **separate, non-listed group entity** (Fabtech Technologies Cleanrooms Ltd, "FTCL," India-only), not to the listed FABTECH entity being valued here (Aug-2026 concall, Aman Anavkar: "Fabtech Technologies Limited... only focused in the international design and build life sciences space... Fabtech Technologies Cleanrooms Limited is focused in the India cleanroom space... for data centers, solar, pharmaceuticals, life sciences").

**Geographic scope:** Primary — Middle East (GCC/Saudi/UAE), Africa (Kenya, Morocco, Botswana, wider MEA), and South/SE Asia, which per the task brief generate ~89% of FABTECH revenue; this matches the Q1 FY27 investor-presentation geography chart almost exactly (Rest of world 29.6% + UAE 27.9% + Saudi Arabia 18.2% + Kenya 9.6% + Morocco 4.8% = 90.1% non-India, India 10.0% — Investor Presentation p.5 "Geographic revenue mix," FY26 basis). **India is shown separately** per task instruction. Note: the same investor-presentation slide's own caption states "international revenue share of approximately 55%," directly contradicting its own chart (90%) — an internal inconsistency already flagged in B04 and repeated here as a document-quality caveat; this report uses the chart (90%, consistent with the 89% figure given in the task brief) as the operative number.

**Customer scope:** Pharma/biotech manufacturers, national vaccine institutes, DFI/donor-backed public-health programmes, governments building sovereign healthcare-manufacturing capacity, animal-health/veterinary facility owners (Aug-2026 concall, Aman Anavkar).

**Channel scope:** Private and government tenders (L1/T1 technical-commercial bid process) and negotiated turnkey contracts; excludes retail/distribution channels (not applicable to this B2B capital-goods business).

**Price segment:** Mid-to-large ticket EPC/equipment contracts, observed range ~$1mn (small equipment orders) to ~$14mn/₹120 Cr (single large Saudi contract, Aug-2026 concall) per project; typical disclosed deal sizes $7–52 Cr equivalent (Botswana vaccine facility ~Rs 30+ Cr; North Africa veterinary facility Rs 49–52 Cr; West Africa tablet-capsule facility $7.05mn — Apr-2026 concall).

**Explicit inclusions:** Greenfield and brownfield pharma/biotech/healthcare facility construction (cleanroom + HVAC + MEP + process utilities) and pharma process-equipment supply, across MEA + India + (nascent) SE Asia.

**Explicit exclusions:** Drug/API product revenue; R&D capex; regulatory/licensing capex; land; non-pharma cleanroom demand; India cleanroom market served by the separate FTCL entity.

### 1B — Management's own TAM claim (held for Section 2 comparison)

Source: Aug-2026 concall (earnings call held 28-Jul-2026, transcript filed 3-Aug-2026), in response to an investor question ("what is the market size of the industry"). Karan Doshi / Aman Anavkar, verbatim: *"market size is a multi-billion dollar industry in the next 10 years. It's been addressed as over north of $30 billion industry in the pharmaceutical emerging markets, be it Middle East, Africa, Southeast Asia, and the West is a different ballgame, more than $70 billion in the next 10 years."*

- **Date of claim:** 28-Jul-2026 (verbal, Q&A; not repeated in the Apr-2026 call, not in the Q1 FY27 Investor Presentation deck, and not anchored to any named report or footnote anywhere in the three documents read).
- **Their definition:** Not given. No stated base year, no stated whether $30bn is a stock (market size reached at some point within 10 years) or a cumulative 10-year flow, no stated whether it means the *total pharma industry* in those geographies or *Fabtech's specific addressable turnkey-EPC opportunity*, and no methodology or source citation (contrast with every other market figure in this report, all of which are CRISIL/IMF/WHO-sourced and dated in the RHP).
- **Independent corroboration:** Per the task brief, stage 6 peer verification found this claim **unattributed and untriangulated by any of the 4 comparable peers** (Anup Engineering, HLE Glascoat, Praj Industries, Ion Exchange) — none of them cite a comparable $30bn/$70bn figure for an adjacent capital-goods/EPC opportunity.
- **Credibility read: BROAD.** See Section 2 Triangulation Table for the quantitative comparison against this report's sourced estimates and against Fabtech's own commissioned CRISIL data (RHP, Aug-2025).

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

All $→₹ conversions use ₹95/$1 (spot, 4-Aug-2026, WebSearch; flagged as a market-rate assumption, not a company-disclosed figure).

### Method 1 — Top-down (CRISIL capex data, RHP Industry Overview, dated Aug-2025)

CRISIL's own capex taxonomy (RHP p.178) splits total pharma-industry capex into **Strategic Capex** (New Capex: Plant Upgradation/Greenfield, R&D, Equipment/Machinery/tools, Others; + Maintenance Capex) and **Regulatory Capex** (licences, approvals, know-how/software, + maintenance). Only the "Plant Upgradation/Greenfield" + "Equipment, Machinery and tools" + associated maintenance lines are addressable by a turnkey-EPC/equipment provider like Fabtech; R&D and Regulatory Capex are not.

| Region | Cumulative capex, source window | Avg $/yr (or ₹/yr) | Source |
|---|---|---|---|
| Global | $370–420bn (CY2020–24) → $500–550bn (CY2025–29P), ~1.3x | $74–110bn/yr | CRISIL, RHP p.183 |
| **MEA** | $9–10bn (CY2020–24) → **$11.5–12.5bn (CY2025–29P)**, ~1.3x | $2.3–2.5bn/yr (CY25-29P) | CRISIL, RHP p.186 |
| **India** | Rs 900–950bn (FY21–25) → **Rs 1,400–1,450bn (FY26–30P)**, ~1.5x | Rs 280–290bn/yr (FY26-30P) | CRISIL, RHP p.190 |

**Subtraction (each step explained):**
1. Remove R&D component: ~20% of total capex, benchmarked to the US/PhRMA figure cited in the same RHP section (~$101bn R&D in 2022 alone; "companies based in the US... earmarking ~20% of overall capex to R&D activities," RHP p.185) — applied here as a rough cross-region proxy since CRISIL does not give an MEA/India-specific R&D-share. **LOW confidence, flagged estimate.**
2. Remove Regulatory Capex + non-physical "Others": no explicit % disclosed by CRISIL; estimated 15–20% based on the taxonomy structure (Regulatory Capex is shown as a co-equal top-level bucket to Strategic Capex, implying non-trivial weight). **LOW confidence, flagged estimate.**
3. Net physical-infrastructure-and-equipment-addressable share ≈ **60–65%** of total capex.

**MEA addressable capex (CY2025–29P avg):** $2.3–2.5bn/yr × 60–65% = **$1.38–1.63bn/yr = Rs 13,110–15,485 Cr/yr**
**India addressable capex (FY26–30P avg):** Rs 280–290bn/yr × 60–65% = **Rs 16,800–18,850 Cr/yr**
**Combined MEA+India (Method 1 TAM, gross physical/equipment capex pool, 100%-capture basis):** **Rs 29,910–34,335 Cr/yr**
**SE Asia:** NOT FOUND — no CRISIL regional breakout in the read section, no reliable third-party facility-capex figure located (see Search Log #6). This is a real gap; SE Asia is folded into management's claim (1B) but is absent from this report's sourced estimate, meaning Method 1 above is likely a modest understatement of the full stated geographic scope.

This Rs 29,910–34,335 Cr/yr figure is the **entire underlying capex pool** — i.e., what a single EPC/turnkey provider could theoretically capture at 100% share of all pharma facility+equipment spend. It is **not** what turnkey-engineering providers actually capture (see Method 3), because most of this pool is spent via direct-to-manufacturer equipment purchase, in-house project teams, or local general contractors who never touch a formal turnkey/EPC intermediary.

### Method 2 — Bottom-up (constrained by data availability)

No independent facility-count / new-pharma-plant-starts dataset for MEA+India was found (search + document read); a true unit-economics build (facility count × avg ticket) is **NOT FOUND**. As a partial cross-check only, Fabtech's own disclosed sales funnel is used: Active enquiries Rs 9,300+ Cr and Hot leads Rs 3,800+ Cr (both as of 30-Jun-2026, Investor Presentation p.3 / Aug-2026 concall), representing **one company's** ~2-year forward visibility. Grossing this up by an assumed 15–25% single-player share of total market enquiries (Fabtech is a mid-sized, not dominant, player per Method 3 below) implies a total identified 2-year opportunity of Rs 37,200–62,000 Cr, i.e. **Rs 18,600–31,000 Cr/yr**. This sits in the same order of magnitude as Method 1 (Rs 29,910–34,335 Cr/yr), a useful but **LOW-confidence** triangulation since the 15–25% share-of-funnel assumption is itself unanchored, and Fabtech's own "active enquiries" are gross/multi-bidder RFQ responses converting at only ~10–17% historically (see Section 3 caveat).

### Method 3 — Peer revenue aggregation (CRISIL competitive-landscape table, RHP p.197, FY2025)

| Company | FY2025 Operating income (Rs Cr) | Scope |
|---|---|---|
| Azbil Corporation (Telstar) | 16,699.5 | **Global** consolidated (100+ countries, mfg Spain/China) — excluded from the MEA/India sum below; not MEA/India-specific, kept only as a global-scale reference |
| Fabtech Technologies Ltd | 328.6 | MEA/India/62 countries |
| Hvax Technologies Ltd | 131.0 | India + 15+ geographies, cleanroom-focused |

Disclosed organized-peer sum (ex-Azbil): **Rs 459.6 Cr**. Eight further named players (Airtech Systems, Avant Garde, Exyte GmbH, Fablab Engineering, Integrated Cleanroom Technologies/TTE Japan, Lotus Technicals, Nicomac Taikisha/Taikisha Group, Pharma Access — RHP p.194–195) have **no disclosed revenue** in the read section. Applying the prompt's standard convention (disclosed organized players ≈ 25–40% of the full organized-peer pool once undisclosed players are added, given 8 additional named, certified, multi-country competitors) → implied organized pool **Rs 1,149–1,838 Cr**. Adding a further unorganised-sector uplift (local/unlicensed contractors handling smaller HVAC/cleanroom scopes, ~40% per the prompt's India convention) → **Rs 1,915–3,063 Cr**.

**Method 3 total (current, FY2025 basis, MEA+India): ≈ Rs 1,900–3,100 Cr.**

**Divergence flag (not silently averaged):** Method 1 (Rs 29,910–34,335 Cr) is ~10–15x Method 3 (Rs 1,900–3,100 Cr). This is explained, not an error: Method 1 sizes the *entire underlying capex pool* (implying ~7–10% current turnkey-channel penetration of that pool, i.e. Method 3 ÷ Method 1), while Method 3 sizes only revenue actually captured by identified, branded, turnkey/cleanroom-engineering providers. **Fabtech's true addressable opportunity sits much closer to Method 3 than Method 1**, because most of the Method 1 capex pool never flows through a formal EPC/turnkey channel at all (direct-to-manufacturer equipment purchase, in-house execution, informal local contractors).

### Method 4 — Import substitution

Not directly applicable in the classic sense (Fabtech is itself an exporter of engineering services, not an import-substitution beneficiary), but the underlying demand driver is structurally identical: MEA governments are substituting **imported finished drugs** with **domestically-manufactured** ones (Vision 2030, AfDB's 2030 Continental Pharmaceutical & Vaccine Manufacturing Vision targeting $111bn of investment with $11bn earmarked for pharma development; Gavi's African Vaccine Manufacturing Accelerator ~$1.5bn; Jordan Country Partnership Framework ~$6.5bn — all RHP p.187–188, CRISIL). Each of these programmes requires new physical facility capacity — i.e., new demand for exactly Fabtech's turnkey-EPC scope. These are cited as directional/qualitative support for Method 1's capex-growth trajectory, not separately quantified into a standalone TAM figure (would double-count Method 1).

### Method 5 — Global benchmark (per-capita / regional comparison)

Global pharma capex (Method 1's source table) implies per-capita spend context: MEA pharma-**product**-market per capita is a fraction of developed-market levels (CHE and pharma-spend-per-capita tables, RHP p.161–163, most recent 2022 — **STALE**, >3 years old, direction-only). MEA per-capita current healthcare expenditure (CHE) in PPP terms: UAE $3,814, Saudi $3,102, vs. US $12,434, Germany $8,454 (2022, RHP p.162) — a 3–4x gap to developed-market levels, directionally supportive of continued MEA catch-up capex, but this table is too dated (2022, 4 years old as of run date) to anchor a headline number; used for direction only per the staleness rule.

Third-party pharma-cleanroom-technology reports (Search Log #4) show **extreme, unreliable dispersion** across vendors for effectively the same category: $5.8bn (2025) → $8.5bn (2035, 3.87% CAGR) per one vendor; $9.03bn (2025) → $27.8bn (2034, 11.9% CAGR) per another; $7.05bn (2025) → $19.10bn (2033, 12.3% CAGR) per a third. This 3–5x spread among paid vendor reports for the same nominal category is itself evidence that this niche is poorly measured externally; **these figures are not used as headline inputs**, only as confirmation that CRISIL's RHP-commissioned, methodologically-transparent data (Method 1/3 above) is the more defensible anchor available.

### Triangulation table

| Method | Estimate (MEA+India, Rs Cr/yr) | Confidence | Staleness |
|---|---|---|---|
| 1 — Top-down (CRISIL capex, physical/equipment-adjusted) | 29,910–34,335 | M (CRISIL-sourced base; L on the 60-65% subtraction assumption) | Fresh (CRISIL, Aug-2025) |
| 2 — Bottom-up (Fabtech funnel grossed up) | 18,600–31,000 | L (share-of-funnel assumption unanchored) | Fresh (Jun-2026 funnel data) |
| 3 — Peer revenue aggregation | 1,900–3,100 | M (2/3 named peers CRISIL-verified; unorganised multiplier L-confidence) | Fresh (CRISIL, FY2025) |
| 4 — Import substitution | Qualitative only (not separately quantified) | — | Fresh (2023–2024 programme dates) |
| 5 — Global benchmark | Directional only (per-capita gap 3–4x) | L | **STALE** (2022 CHE data, >3 yrs old) |
| Management's claim | ~$30bn "in the next 10 years," MEA+Africa+SEA | — | Undated methodology |

**TAM — conservative estimate (per CONSERVATIVE BIAS rule, take the lower, better-triangulated method): Rs 2,000 Cr/yr** (Method 3, low end, current annual, organized+unorganised turnkey-engineering-peer-capturable market, MEA+India).

**TAM — realistic estimate: Rs 4,400 Cr/yr** (Method 1's structural capex pool [Rs 29,910–34,335 Cr, midpoint ~32,100] with an estimated 12–15% turnkey-channel-penetration rate applied — i.e., assuming current ~7–10% penetration [Method 3 ÷ Method 1] rises modestly over the TAM window as the "single-point-responsibility" model CRISIL and management both describe as a structural trend gains share; 32,100 × 13.7% ≈ 4,400). **LOW-MEDIUM confidence — this bridges two methods that diverge 10-15x, and the penetration-rate assumption is not independently sourced.**

**Management's claim vs. the conservative estimate:** Management's $30bn figure (MEA+Africa+SEA, "in the next 10 years") converts, on the most conservative reading (10-year cumulative flow, not a future stock level), to ≈ $3.0bn/yr ≈ **Rs 28,500 Cr/yr**.
Ratio = 28,500 ÷ 2,000 ≈ **14.3x** → far above the >2x "likely inflated" threshold, on the *most conservative* possible reading of an ambiguous claim. (On the alternative, arguably more natural reading — that $30bn describes a market-size *level* reached within 10 years, i.e. an annual run-rate — the ratio would be closer to Rs 285,000 Cr ÷ Rs 2,000 Cr ≈ **142x**, which is not a serious comparison at all.)

**Read: INFLATED — but the more precise diagnosis is a TAM/SAM conflation, not necessarily a fabricated absolute number.** Cross-checked against Fabtech's *own* CRISIL-commissioned data (same RHP, filed within the last year): CRISIL's MEA-only total pharma capex (all categories, all players) for CY2025–29P is just $11.5–12.5bn cumulative; extrapolating the same ~1.3x/5-year growth trend to a full 10-year MEA-only window gives roughly $27–29bn cumulative — i.e., in the same order of magnitude as management's $30bn figure **if** that figure is read as "total industry capex, all categories, all competitors, MEA+Africa+SEA, over 10 years." Under that reading the raw number is not obviously fabricated. The dishonesty is procedural, not arithmetic: management presents this whole-market, whole-category, whole-competitor-set number in response to a direct "what's our opportunity" question, with **no SAM/SOM framing, no filters, no source citation**, and it was **unattributed and untriangulated by all 4 comparable peers** (stage 6 finding). This is exactly the pattern flagged in this framework's operating rule: *"Management claiming TAM = SAM = growth runway is being dishonest."*

---

## SECTION 3: SAM & SOM

### 3A — SAM (five filters applied to TAM realistic, Rs 4,400 Cr)

| Filter | Rationale | Cut | Running total (Rs Cr) |
|---|---|---|---|
| Start (TAM, realistic) | — | — | 4,400 |
| Product fit | Fabtech's turnkey+equipment scope covers nearly all of the addressable pool; narrow gap vs. pure-product cleanroom-equipment-only specialists | −5% | 4,180 |
| Geography | Fabtech's disclosed track record concentrates in GCC (UAE/Saudi), Kenya, Morocco, Botswana, India; large parts of MEA (Nigeria, South Africa, wider Francophone Africa) and most of SE Asia remain white space with no disclosed presence | −25% | 3,135 |
| Channel | Very large (>$50–100mn), multilateral/DFI-funded mega-tenders typically require balance-sheet scale (bonding/guarantee capacity) beyond Fabtech's current ~Rs 420 Cr net worth (Apr-2026 concall) | −15% | 2,665 |
| Customer | Flagship mega-plants of large multinational pharma majors more often route to global majors (Azbil/Telstar, Exyte) given scale/track record | −10% | 2,398 |
| Capability | Related-party equipment-procurement dependency (B04 flag) and current execution-capacity ceiling implied by an 18–24 month order-book visibility window | −10% | 2,158 |

**SAM ≈ Rs 2,150 Cr/yr. SAM as % of TAM (realistic): 2,150 ÷ 4,400 ≈ 49%.**

**Caveat on internal tension (flagged, not silently resolved):** Fabtech's own "hot leads" funnel (Rs 3,800 Cr, 30-Jun-2026, ~2-year visibility for ONE company) annualizes to ~Rs 1,900 Cr/yr — a strikingly large fraction (~88%) of this report's bottom-up SAM estimate for the *entire* MEA+India turnkey-provider market. Two explanations, both plausible, are held simultaneously: (a) this SAM estimate may still understate the true market given multiple undisclosed-revenue peers (Exyte, Airtech, Telstar's MEA-specific book) that are not captured in Method 3; or (b) Fabtech's self-reported "hot lead" classification is optimistic gross-funnel language typical of a newly-listed growth company, consistent with management's own disclosed ~10–17% historical proposal-to-order conversion rate (Aug-2026 concall: "conversion is now getting improved. It is now 11%... reaching and hitting to around 16 to 17 percent of the hot lead"). This tension is carried forward as a confidence caveat rather than forced into false precision.

### 3B — SOM at 3 and 5 years

**Current SAM share:** FY26 revenue Rs 431.33 Cr ÷ SAM Rs 2,150 Cr ≈ **20.1%**.

Share-gain rule applied: Fabtech is post-IPO with a largely-undeployed ~Rs 208 Cr cash balance, is actively pursuing two acquisitions (Saudi SACE JV — already completed 51% stake and a first civil order won; Italy/European target — in due diligence), and operates in a market where the Method 1 vs Method 3 gap (~10–15x) itself signals that a large, informal/non-turnkey share of capex is still "unformalised" — qualifying, per the standard share-gain rules, for the **faster-than-normal allowance** ("faster possible where unorganised share >40% is formalising"). Applied: **+4pp over 3 years** (aggressive tier, justified by capacity+execution — IPO capital, active M&A) and **+6pp over 5 years** (capped below the >5pp-only-on-acquisition ceiling since only partial credit is taken for the still-unclosed Italy deal).

SAM itself grows at the blended structural capex CAGR (MEA ≈5.7%/yr and India ≈9.9%/yr implied by the CRISIL 1.3x/1.5x five-year multiples; blended ≈**7%/yr**, LOW-confidence blend):

- SAM (3yr) ≈ Rs 2,150 Cr × 1.07³ ≈ **Rs 2,634 Cr**; share 20.1%+4pp = **24.1%** → **SOM 3yr ≈ Rs 635 Cr**
- SAM (5yr) ≈ Rs 2,150 Cr × 1.07⁵ ≈ **Rs 3,015 Cr**; share 20.1%+6pp = **26.1%** → **SOM 5yr ≈ Rs 787 Cr**

**Implied revenue CAGR (arithmetic, from FY26 base Rs 431.33 Cr):**
- 3yr: (635/431.33)^(1/3) − 1 ≈ **13.8%**
- 5yr: (787/431.33)^(1/5) − 1 ≈ **12.8%**

**FORMAL HANDOFF TO STAGE 11:** This SOM-implied CAGR band (**~13–14%**) sits **materially below** management's own stated FY27 guidance (20–25% organic growth, repeated across both concalls) and their disclosed long-term aspiration (Rs 1,000 Cr+ organic top line by 2030 — Aug-2026 concall, Karan Doshi — which implies a ~23.4% CAGR from the FY26 Rs 431.33 Cr base). Stage 11 should weigh this market-sizing-derived, share-gain-disciplined CAGR against management guidance and the order-book-based near-term visibility (which is more directly evidenced than this multi-step TAM/SAM chain) rather than defaulting to management's higher number unexamined.

### 3C — Capacity cross-check (B07.capex_embedded_growth_pct = 83%)

SOM 5yr (Rs 787 Cr) implies **+82.5% cumulative growth** over the FY26 base (787/431.33 = 1.825x) — this sits almost exactly at B07's disclosed capex-embedded growth ceiling of **83%**, i.e. the currently largely-undeployed IPO cash (~Rs 208 Cr, mostly in bank FDs per Q1 FY27 investor presentation "Idle capital still earns" slide) is roughly **right-sized for, not surplus to**, the SOM this report derives. **Capacity check: SUFFICIENT for the SOM case, with near-zero spare margin.**

Cross-checking against **management's own guidance** instead: 20–25% CAGR compounded over 5 years implies cumulative growth of +149% (low end, 1.20⁵) to +205% (high end, 1.25⁵) — i.e. FY31 revenue of **Rs 1,073–1,315 Cr**. Both figures **vastly exceed** the 83% capex-embedded ceiling.

**Gap, in ₹ Cr:** Rs 1,073 Cr (mgmt low case) − Rs 789 Cr (83%-ceiling-implied revenue, 431.33×1.83) = **≈ Rs 284 Cr shortfall**, widening to **≈ Rs 526 Cr** at the high end of guidance (Rs 1,315 Cr case).

**Which side is optimistic:** The SOM derived in this report (Section 3B) is the one that **aligns with disclosed capacity**. **Management's own 20–25% growth guidance is the optimistic side of this comparison** — it would require either (a) capital/capacity beyond the current IPO war chest (a further raise, materially higher debt, or a much faster working-capital cycle than the currently-disclosed 120-day cycle), or (b) the 83% capex-embedded figure itself under-stating true headroom (plausible, since much of the IPO capital sits undeployed pending the still-unclosed Italy acquisition — deploying that capital would raise the ceiling), or (c) genuine over-optimism in the growth guidance relative to currently-installed-plus-committed capacity.

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A — TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory/self-reliance tailwind (post-COVID localisation) | High | KSA Vision 2030 (raise domestic drug production share from 15-18% to 40%); AfDB's $111bn 2030 Continental Pharmaceutical & Vaccine Manufacturing Vision ($11bn earmarked for pharma development); Gavi's African Vaccine Manufacturing Accelerator (~$1.5bn); Jordan CPF (~$6.5bn) — all RHP p.186–188, CRISIL, dated 2023-2024 programme announcements |
| Geographic expansion / new applications | High | Fabtech's own Saudi SACE JV explicitly framed by management as unlocking "the far larger built infrastructure opportunities" beyond pure pharma cleanroom EPC (Aug-2026 concall); ~Rs 400 Cr PEB/civil-infrastructure bid pipeline already in motion in Africa/Middle East (same call) |
| Import substitution | Medium-High | India imports ~70% of API intermediaries from China (RHP p.177); MEA governments' localisation drive is the direct, quantified demand source for the CRISIL MEA capex growth trajectory (Method 1) |
| New applications (biologics/vaccines) | Medium | KSA National Biotechnology Strategy (2024); management cites "biologics and specialty pharma capex accelerating" and cell/gene-therapy demand as growth areas (Apr-2026, Aug-2026 concalls) |
| Regulatory tailwind (global) | Medium | Global pharma capex CY2025-29P projected at $500-550bn vs $370-420bn CY2020-24 (~1.3x), driven by patent expiries, generic-medicine growth, pricing pressure (RHP p.183) |
| Formalisation of unorganised capacity | Medium | Method 1-vs-Method 3 gap (~7-10% current turnkey-channel penetration) implies substantial headroom as the "single-point-responsibility" model (explicitly cited as a structural benefit in RHP p.180 "Key Benefits of Turnkey Engineering Solution Providers") displaces fragmented/self-performed execution |
| Demographics / chronic disease burden | Low-Medium (indirect) | Aging population share rising from 25.3% to 33.2% of MEA population by 2050P; non-communicable disease share of MEA deaths rose from 68% (2000) to 79% (2019) (RHP p.170-171) — drives underlying drug demand, which drives facility capex with a multi-year lag |

### 4B — TAM risks (with monitoring signals)

| Risk | Monitoring signal |
|---|---|
| Geopolitical disruption | Already materially impacting the UAE/FTS segment ("severe regional headwinds" from Middle East war, Q1 FY27 results); watch: order-conversion-timeline slippage, freight-cost spikes, project delays without cancellation |
| Donor/DFI funding-cycle risk | Management explicitly cites "donor and government funding cycles" delaying large-ticket order finalisation (Aug-2026 concall); watch: hot-lead-to-order conversion ratio (currently 11-17%, target improving) |
| Increasing localisation as a double-edged sword | CRISIL flags that MEA localisation "can discourage foreign MNCs because of exit barriers... and technological challenges" (RHP p.172, p.192) — a risk to any non-local turnkey provider, mitigated for Fabtech only to the extent its own localisation JVs (SACE Saudi) succeed |
| FX volatility | Currency devaluation risk explicitly named for Egypt-type scenarios (Apr-2026 concall); billing is USD/LC-backed, but client-side devaluation still a project-continuity risk |
| Execution/talent scarcity | CRISIL: "pharmaceutical turnkey engineering solution providers experience difficulties in recruiting and retaining skilled employees" (RHP p.181, p.192) |
| Consolidation by global majors | Exyte spun off from M+W Group (2023); TTE Japan acquired 100% of Integrated Cleanroom Technologies (2023) — signals MNC capital entering this specific niche, a competitive risk to smaller regional players over the TAM window |
| Saturation / cyclicality of underlying pharma capex | Global pharma capex growth (1.3x/5yr) is itself contingent on continued patent-expiry/generic dynamics; any slowdown in global pharma capex cycles (RHP p.183-185) flows through with a lag |

### 4C — Market structure

- **Competitor count:** At least 9 named players in the CRISIL competitive landscape (RHP p.194-197) serving the pharma turnkey-engineering/cleanroom niche relevant to Fabtech, plus an unquantified unorganised/local-contractor tail.
- **Top-3 concentration:** Cannot be precisely computed — only 3 of 9+ named players have disclosed revenue, and the largest (Azbil/Telstar, Rs 16,699.5 Cr) is a global figure not MEA/India-specific. Directionally: **fragmented**, no single player with a clearly dominant MEA+India share based on available disclosure.
- **Organised vs. unorganised split:** Implied ~7-10% organised/turnkey-channel penetration of total addressable capex (Method 3 ÷ Method 1), i.e. the large majority of underlying capex still flows through non-turnkey channels — a genuinely fragmented, largely-informal-or-self-performed market at the capex-pool level.
- **Consolidating or fragmenting:** Early signs of MNC consolidation at the top (Exyte spin-off, TTE Japan's 2023 acquisition of Integrated Cleanroom Technologies) while the broader base remains fragmented; Fabtech itself is pursuing consolidation (Saudi SACE, pending Italy deal) — a **consolidating-at-the-margin, fragmented-at-the-base** structure.
- **Price vs. differentiation competition:** CRISIL's own "Key Benefits of Turnkey Engineering Solution Providers" table (RHP p.180) frames the value proposition around project-management experience, expert oversight, and cost-overrun control — i.e. a **differentiation-led** model (single-point responsibility), though Fabtech's own RMC (raw-material-cost) variation-clause negotiations with clients (both concalls) indicate real price/cost sensitivity at the margin.
- **Entries/exits:** TTE Japan entry (2023, acquisition); Exyte corporate restructuring (2023); Fabtech's own IPO (Nov-2025) and subsequent Saudi/Italy M&A — an active, not static, competitive landscape.
- **Import share trend:** Directionally declining as a share of total (that is the entire premise of the MEA/India localisation drive underlying Method 1's capex growth), though no specific import-share-of-turnkey-services metric was found (NOT FOUND).

---

## SECTION 5: SUMMARY & RUNWAY

### 5A — Funnel diagram

```
TAM (conservative, Method 3-anchored) ............ Rs 2,000 Cr/yr
TAM (realistic, Method 1-bridged)  ................ Rs 4,400 Cr/yr
   ↓ (5 filters: product -5%, geography -25%, channel -15%, customer -10%, capability -10%)
SAM ................................................ Rs 2,150 Cr/yr  (≈49% of TAM realistic)
   ↓ (current share 20.1%, +4pp @ 3yr aggressive-tier gain, +6pp @ 5yr)
SOM (3yr) .......................................... Rs 635 Cr
SOM (5yr) .......................................... Rs 787 Cr
   ↓
FY26 actual revenue (base) ......................... Rs 431.33 Cr
```

### 5B — Runway assessment

- **Revenue headroom = SAM ÷ current revenue:** 2,150 ÷ 431.33 ≈ **5.0x**
- **TAM/SAM growth rate:** ≈ **7%/yr** (blended MEA ~5.7%/yr + India ~9.9%/yr structural capex CAGR, LOW-confidence blend)
- **Company CAGR vs. TAM:** FY26 actual revenue growth was +28.4% YoY (total income, RHP-anchored); FY27 management guidance is 20-25%; both are **far above** the ~7%/yr TAM growth rate, i.e. Fabtech is (on its own guidance) pursuing genuine share gain, not simply riding market growth. This report's own disciplined SOM-implied CAGR (~13-14%) sits between the TAM growth rate (~7%) and management's guidance (20-25%) — consistent with meaningful-but-not-extreme share gain.
- **Years to saturate SAM at current (management-guided) growth:** Using a net effective closure rate of ~22.5% (mgmt guidance) − 7% (SAM growth) ≈ 15.5%/yr against the current 5.0x headroom ratio: ln(5.0)/ln(1.155) ≈ **~11 years**.

### 5C — Runway classification: **STRONG**

Reasoning: ~5x revenue headroom, high-single-digit underlying structural TAM/SAM growth, an 11-year runway to saturation even at management's own aggressive guidance, and multiple real (not aspirational) SAM-expansion levers already in execution (5D). Not classified **MASSIVE** — headroom (~5x) and TAM growth rate (~7%) are moderate, not exceptional, and the market remains genuinely fragmented with real competitive/geopolitical risk (Section 4B). Not merely **GOOD/MODERATE** either — an 11-year runway with active, evidenced expansion levers and a structural (not merely cyclical) growth story (localisation, self-reliance capex, formalisation of an ~90%-informal channel) supports the stronger classification.

### 5D — SAM expansion levers actually being pursued

1. **Saudi localisation (SACE JV, 51% stake, already closed + first civil order won):** Management explicitly frames this as moving "beyond pharmaceutical cleanrooms EPC into the far larger built infrastructure opportunities" (Aug-2026 concall) — a genuine new-TAM adjacency (MEP/civil infrastructure), **not quantified by management** (NOT FOUND — no $ figure given for this adjacency).
2. **PEB (pre-engineered buildings)/civil-infrastructure scope:** ~Rs 400 Cr bid pipeline already active in Africa/Middle East (Aug-2026 concall) — a quantified, sourced, in-motion SAM addition.
3. **Africa deepening:** Morocco + Kenya already contributing Rs 27.94 Cr in a single quarter (Q1 FY27) from markets that were "not material contributors a year ago"; Botswana vaccine win as a stated wedge into further DFI-funded African vaccine-institute pipeline.
4. **Proposed Italy/European acquisition** (in due diligence, not yet closed): geographic + technology adjacency into a developed-market pharma-engineering segment.

**Revised SAM (illustrative, using only the quantified PEB pipeline as an incremental, near-term addition):** Rs 2,150 Cr + Rs 400 Cr ≈ **Rs 2,550 Cr**; revised headroom ≈ 2,550/431.33 ≈ **5.9x**. The Saudi MEP/civil adjacency and the Italy deal are directionally additive but **not quantified** by management or CRISIL, so are noted but not added to the revised-SAM arithmetic (NOT FOUND, not estimated).

### 5E — Final output card

- **TAM:** conservative Rs 2,000 Cr/yr | realistic Rs 4,400 Cr/yr (MEA+India; SE Asia not separately sourced — gap)
- **SAM:** Rs 2,150 Cr/yr (≈49% of TAM realistic)
- **SOM:** Rs 635 Cr (3yr) | Rs 787 Cr (5yr)
- **Current SAM share:** 20.1%
- **Revenue headroom:** 5.0x (5.9x if the quantified PEB pipeline is credited)
- **Runway class:** STRONG
- **Management's own TAM claim ($30bn/10yr MEA+Africa+SEA):** read as INFLATED relative to Fabtech's addressable opportunity — not necessarily arithmetically fabricated (it is roughly the right order of magnitude as *total, all-category, all-competitor* MEA capex extrapolated to a 10-year window using Fabtech's own commissioned CRISIL data), but presented with no SAM/SOM framing and unattributed/untriangulated by any of the 4 comparable peers — a TAM-presented-as-opportunity conflation.

**Valuation implication line:** At **~13% (3yr) to 13.8% (5yr, inverted — see note) revenue CAGR** implied by SOM — precisely, **~13.8% (3yr) / ~12.8% (5yr)** — with a margin trajectory of **EBITDA ~13-14% / PAT ~9-11%** (management's own stated targets, Apr-2026 concall, Karan Doshi: "at EBITDA level, our target is to do around 13 to 14%, and PAT level will be between 9 to 11%"; consistent with a broadly flat-to-modestly-improving margin path from the FY26 base), the earnings growth embedded here is approximately **13-16% CAGR** (revenue CAGR plus a modest operating-leverage tailwind management itself cites), which [**NOT FOUND — no current share price or trailing/forward P/E was provided as an input to this stage; stage 11 should complete this specific comparison once price/EPS data is available**] the current valuation of **__x P/E [NOT FOUND]**.

---

## KEY CROSS-STAGE FLAGS

1. **SOM-implied CAGR (~13-14%) is materially below management's 20-25% guidance and their Rs 1,000 Cr-by-2030 target (~23.4% CAGR).** Stage 11 should treat this as a formal, methodologically-disciplined cross-check, not simply defer to management guidance.
2. **Management's $30bn/$70bn TAM claim is unattributed, undated-methodology, and untriangulated by all 4 comparable peers** (stage 6 finding) — read as INFLATED / TAM-presented-as-SAM conflation, not used anywhere in this report's headline TAM/SAM/SOM figures.
3. **Capacity check:** SOM (5yr, +82.5% cumulative growth) sits almost exactly at the B07 capex-embedded ceiling (83%); management's own 20-25% growth guidance would **exceed** that ceiling by Rs 284-526 Cr, implying either further capital deployment is needed (the still-undeployed IPO cash, or a new raise) or the 83% figure understates true headroom once the Italy deal closes.
4. **This entire SAM/SOM chain rests on several LOW-to-MEDIUM confidence, explicitly-flagged assumptions** (R&D/regulatory capex split ~20%/15-20%, turnkey-channel penetration rate ~13.7%, unorganised-sector multiplier ~40%, blended TAM growth ~7%, single-player funnel-share 15-25%). Headline numbers should be treated as **directional, not precise**, and re-triangulated if independent broker/equity research becomes available (currently absent — input gap).
5. **SE Asia capex could not be independently sourced** despite being explicitly part of both the task's geographic scope and management's own claimed opportunity — a genuine, flagged data gap, not folded silently into the MEA figure.

---
