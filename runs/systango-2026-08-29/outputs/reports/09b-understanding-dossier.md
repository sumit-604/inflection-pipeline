# HALT 1 UNDERSTANDING DOSSIER — Systango Technologies Ltd (SYSTANGO)
Run date: 2026-08-29 | Model: claude-sonnet-5 | Assembled from committed blocks B00-B09, verifier blocks B12a-B12d, confidence.yaml

This dossier assembles what the pipeline already found. It contains no valuation, no price, and no verdict. The kill/proceed decision belongs to the operator, made after reading this.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls
Two unique transcripts held (a third file is a duplicate):
- Concall_Jul_2023_Transcript.pdf — FY23 annual earnings call, held 7-Jul-2023, year ended 31-Mar-2023 (B00, B05).
- Concall_Nov_2023_Transcript_2.pdf — H1FY24 call, held 17-Nov-2023, half ended 30-Sep-2023 (B00, B05). Concall_Nov_2023_Transcript.pdf is a duplicate of this file (B00).

Most recent quarter covered by a transcript: H1FY24 (half ended 30-Sep-2023). The run date is 29-Aug-2026. Results filings in the corpus show the company reported an H1FY26 board outcome (Nov-2025) and FY26 audited full-year results (May-2026), so at least ten more quarters have plausibly reported since the last held transcript, and no transcript exists for any of them (B00, B05). B05 states plainly: "no concall exists in the corpus after 17-Nov-2023. The company appears to have stopped holding investor calls thereafter."

### 2. Annual reports
One AR file is held: `Annual_Report_2023.pdf`. Its filename is wrong. Stage 1, Stage 2, Stage 3 and verifier A all independently confirm, from the cover page and the auditor's report date (26-May-2025), that this is the 21st Annual Report, for FY2024-25 (year ended 31-Mar-2025), not FY2023 (B01, B02, B03, B12a). No FY2023 AR exists in the corpus. The AR carries FY24 comparatives, so two years of note-level detail are available (FY24, FY25), plus a wider 7-year revenue/PAT trend from screener data (FY20-FY26) that lacks balance-sheet granularity for the earlier years (B01). The latest completed FY is FY26 (per the May-2026 audited results). The FY26 Annual Report is NOT present. Only one AR-level document is held; three years of full AR-level disclosure are not.

### 3. Results filings
Two results filings held: SYSTANGO_07112025151948_OutcomeofBoardmeeting.pdf (H1FY26 board outcome, filed ~7-Nov-2025) and SYSTANGO_14052026200758_Intimation.pdf (FY26 audited full-year results plus H2, filed 14-May-2026, carrying the first-ever Rs 7/share interim dividend) (B00). The latest quarterly filing is the FY26 audited full-year results (14-May-2026). This is roughly eight months ahead of the latest AR held (FY25, signed 4-Sep-2025) — a full-FY quarter-gap between the newest results filing and the newest AR in the corpus (B00).

### 4. Investor presentations
One deck held (in two copies): Investor_Presentation_1.pdf, "Annual Update," dated June 2026, carrying FY26 headline financial and operating data (B00, B04).

### 5. Research / rating
None held. The rating/ folder is ABSENT and the research/ folder is ABSENT (a placeholder file only) (B00).

### 6. Corporate actions
No dedicated announcements/ folder exists. Reg-30-type intimations sit only inside the results/ and presentation/ folders (the FY26 results intimation and the H1FY26 board-meeting outcome) (B00). No standalone filing for a specific order win, JV, capex programme, or capital raise is held. The Tech Alchemy Ltd (UK) transaction — a real, signed asset/team acquisition per external web search at Stage 8 — has no exchange-filing counterpart anywhere in this corpus; the AR itself is silent on it (B03 Phase 6E, B08).

### 7. Freshness pair check
B00's `freshness_verdict` is CORPUS GAPPED-FRESHNESS. Two of the four defined pairs FAILED:
- Pair 1 (results → concall): trigger document = FY26 audited results (14-May-2026); mate expected = FY26/Q4 concall; status FAIL; missing document = FY26 concall transcript.
- Pair 4 (AR → latest audited annual): trigger document = FY26 audited annual results; mate expected = FY26 Annual Report; status FAIL; missing document = FY26 Annual Report (the AR held is FY25, one year behind the FY26 audited results).

Pairs 2 (rating bulletin → rationale) and 3 (SEBI order → order text) both PASS, because no trigger document exists for either (no rating bulletin, no referenced SEBI order) (B00).

### 8. Verdict line

**CORPUS GAPPED-FRESHNESS.**

Missing mates, named first, each classified:
- **FY26 concall transcript** — missing mate for the results→concall pair. Classification: **plausibly-nonexistent**. B05 finds no concall in the corpus after 17-Nov-2023 across roughly ten reportable quarters since; this reads as a discontinued practice, not a single-quarter gap, and is itself a data point on investor-engagement continuity (B05 rates "Investor engagement continuity: Weak").
- **FY26 Annual Report** — missing mate for the AR→latest-audited-annual pair. Classification: **freshness-pair / findable-missing**. A statutory annual report should follow the FY26 (31-Mar-2026) year-end within the normal AGM cycle; expected source: BSE/NSE company filings or the company IR page.

Other gaps, listed under this verdict per the Freshness Pair Check instruction:
- **Prospectus** — findable-missing; expected source BSE/NSE historical filings or company IR page; the company listed on NSE Emerge ~March 2023 (B00).
- **Rating** — plausibly-nonexistent; no rating agency coverage is evidenced anywhere in the corpus for this SME-Emerge-listed micro-cap; expected source: a rating agency site, if coverage exists at all (B00).
- **Dedicated announcements/corporate-action filings** — findable-missing; expected source BSE/NSE.
- **Shareholding pattern filing, post-31-Mar-2025** — findable-missing; expected source BSE/NSE. A Mar-2026 figure exists only as an operator-pasted, non-anchored screener lead (Promoter 72.17%, FII 0.47%, DII 1.69%, Public 25.67%, 2,637 holders), never a filed source (B00).
- **Research / broker notes** — plausibly-nonexistent; no institutional broker coverage is evidenced for a name at this scale.

This verdict carries a mechanical downstream consequence, stated here as a fact about the pipeline's own gate mechanism, not as this dossier's judgment on the company: a failed Freshness Pair Check caps the phase-1 gate recommendation one level below what the evidence would otherwise support, and both missing mates (FY26 concall, FY26 AR) are named as the first upload priority at Halt 1 (per the orchestrator's gate-recommendation logic, B00). FY26 headline financials themselves are anchored (results filing, investor deck); it is the notes-level FY26 depth — CARO loan-book movement, related-party detail, consolidated cash flow, DBX Holdings identity, client concentration — that remains unresolvable until the FY26 AR is pushed (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.**

### PART A — THE FROM STATE

**A1. Archetype.** Single reportable business line (B03 Phase 4C: "single reportable operating segment disclosed"; B04). Archetype: **Outsourcing partner (CDMO/EMS/IT services)** — client concentration, wallet share, capacity fill, contract stickiness, price per unit (CLAUDE.md Archetype Library).

**A2. The simple analogy.** Systango is a small, Indore-based digital-engineering workshop. Foreign clients in London and New York hire its engineers by the month to build and run software, AI systems, and blockchain products. The workshop pays its craftsmen in rupees and bills its foreign clients in pounds and dollars, so every rupee of local wage buys more foreign revenue than it costs. It has begun selling a few of its own tools — an online-learning product, a wealth-management dashboard — instead of only renting out labour, but that side is still small and its size is not disclosed. The workshop's central exposure: about ten clients supply roughly two-thirds of its orders, and if two or three walk away, it feels the loss immediately (B04, paraphrasing the stage's own "chai-stall-uncle version").

### PART B — THE TRANSITION

**B1. FROM → TO.** FROM: **R2 COST-ADVANTAGED CONVERTER** — margin from cost position (India-delivery billed in GBP/USD), not from price, with a narrow, replicable moat (B04: "cost advantage… an industry-wide arbitrage, not company-specific"; B04 moat assessment scores every category Low-Moderate or None except cost advantage). This is a qualitative fit, not a numeric one: Systango's ROCE (27-33%, B01 Block A) sits well above R2's stated mid-teens band and closer to R4/R5 territory. That gap between a cost-arbitrage character and a high-ROCE number is an open tension this dossier flags rather than resolves. TO (claimed): **R3 VALUE-ADDED / SPEC'D SUPPLIER** — partial pricing power from spec-in and embedded-team switching costs, via a stated shift toward AI/ML/GenAI work and early solution licensing (B04, B05 trigger table: "Higher-value mix shift via hyperscaler partnerships and Rust/AI-ML specialisation," conviction MEDIUM).

**B2. The engine.** Two things must physically change: (1) the mix of technology-service-line revenue shifts toward AI/ML/Data/Cloud work at higher realisation per employee — revenue per employee rose from ~Rs 16.8 lakh (FY23) to ~Rs 29.4 lakh (FY26) while headcount barely moved, 312 to 308 (B04); (2) delivery moves from pure staff augmentation toward embedded product-team pods plus owned, licensable IP (Swotter, Shootih, Mi-VerifyQR, BaaS) that is not yet separately disclosed in size (B04).

**B3. The proof gate.** Two disclosed metrics, tested together, quarter by quarter: revenue per employee must keep rising from its ~Rs 29.4 lakh FY26 base, AND the AI/ML/Data/Cloud share of technology-service-line revenue must hold at or above its 46% FY26 level for at least two consecutive disclosed periods — with the rise not explained by headcount attrition alone (revenue growth must outpace headcount growth) (B04 must_track_metrics). Until both legs hold together, the mix-shift is a one-year readout, not a proven transition.

**B4. The recognition gap (open question, resolved at Stage 11).** Whether the market already prices in the claimed R3 destination is an open question this dossier does not answer. Stage 11 resolves it via the Section 1B destination-PE gap: if the current multiple already sits near the TO-tier neighbourhood, the re-rating engine may already be spent and only earnings growth would remain; if it sits nearer the FROM-tier neighbourhood, the gap stays open. No number or conclusion is stated here.

**B5. The ugliness test.** Classification: **STRUCTURAL-FEATURE.** The candidate "ugly optic" is a repeated pattern of ambitious forward claims that later go unconfirmed or are silently dropped, observed across at least three independent episodes in the corpus, not a single artifact of one hard climb: (i) the FY26 Rs 250cr/$25M revenue target and the FY24 growth guidance, cut from ~60% to 30% within four months and still missed by roughly 8% actual versus 30% guided (B05); (ii) an "institutional grade crypto derivative insights and analytics platform… probably three months away from the launch" (Q_FY23 call, 7-Jul-2023, p.4) that is never confirmed launched and is silently absent from every later document reviewed (B05, B07, verifier B MAJOR finding); (iii) the founders' letter's Tech Alchemy (UK) "binding acquisition agreement" claim, present in the AR's most visible page and absent from every operational section of the same document signed the same day (B03 Phase 6E). Countervailing evidence, held alongside this classification rather than erased by it: the one margin promise was kept and exceeded (37.6% FY26 vs >25% target, B05); Stage 8's web search shows the Tech Alchemy deal is real, signed with an unrelated counterparty, not abandoned — the AR's silence is a disclosure-consistency lapse within one document, not a fabricated claim (B08); and B06's peer cross-read gives partial, topic-specific support to the "sector-wide slowdown" framing for the blockchain-demand piece of the FY23-24 guidance cut. The classification names a recurring behavioural pattern (promise ahead of confirmed delivery, across products and across capital-allocation commitments), not proven fraud.

**B6. The transition falsifier.** The AI/ML/Data/Cloud technology-line revenue share falls back toward, or below, its pre-FY26 level, and/or revenue per employee flattens or reverses over two consecutive disclosed periods — showing the claimed higher-value mix shift was a one-year statistical readout (client-mix noise, or a single large contract) rather than a structural repositioning (B04 must_track_metrics).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2/B3):
1. **Revenue per employee** (mix-shift proxy). Current state: rose from ~Rs 16.8 lakh (FY23) to ~Rs 29.4 lakh (FY26), consolidated (B04).
2. **AI/ML/Data/Cloud share of technology-service-line revenue.** Current state: 46% of FY26 revenue; prior-year split not disclosed anywhere reviewed (B04, B07 input gap).
3. **Top-3 / top-10 client concentration.** Current state: top-3 38-42% and top-10 65-72% of consolidated revenue every year FY23-FY26 (B04); a separate H1FY26 figure of 46-48% (Nov-2025 deck, spear brief) versus the June-2026 deck's FY26 full-year 42% is an unreconciled discrepancy (B04 flag).
4. **Standalone cash-conversion of the growth (CFO/PAT, receivable turnover).** Current state: CFO/PAT 0.348x-0.522x across all four standalone/consolidated × FY24/FY25 cells, all below the 0.7x flag threshold; standalone receivable turnover fell from 7.81x to 4.90x (B03 Phase 3A/2D).

**C2. What the model rejects.** Market-size questions are explicitly named as noise by the pipeline's own TAM work: B09 states SAM is roughly 5,454x current revenue and flags "do not read MASSIVE as a growth forecast," naming the execution-bounded SOM (10% conservative CAGR) as the governing figure instead. Aggregate global IT-spending macro citations in the AR are flagged as "entirely macro-level… largely copy-paste-able across any Indian IT-services AR" (B03 Phase 4C) and are rejected as decision-relevant on their own. Hiring/capacity constraints are also rejected as binding: B09's capacity check finds the model "sufficient (no capex constraint)," with hiring pace, not capital, the real limit. The model instead asks whether management executes and discloses honestly (credibility grade D, B05) and whether the claimed mix-shift converts to cash (C1.4), not whether the addressable market is large enough.

**C3. The business falsifier** (distinct from B6, kills the FROM business's own credibility rather than the transition claim). Confirmation that DBX Holdings Ltd is controlled or co-directed by promoter Nilesh Rathi — the single highest-priority Halt-1 verification item named by B08 — would re-characterise the FROM business itself. Operating cash already flagged as extended to unnamed "Others" (Rs 5.30cr, B01/B02, CARO-confirmed, actively growing) sits alongside a fresh FY25 equity stake in a company that flipped from RPT customer to undisclosed investee the very same year (B03 Phase 2B). Together, if the Nilesh Rathi link is confirmed, this reads as a pattern of related-party capital extraction rather than an isolated disclosure gap, undermining the "clean, organic, non-leverage-driven ROE" read that the Gate 0 score currently rests on (B01, B03 DuPont finding: "ROE is organic/margin-driven, NOT leverage-driven").

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Systango builds and runs custom software, AI and generative-AI systems, and blockchain products for clients mainly in the UK and the US (B04). Its work sits in staff augmentation, time-and-materials project builds, managed and maintenance contracts, and a small, undisclosed-in-size solution-licensing and blockchain-as-a-service tail — the four service-linked streams tie revenue to a named client relationship, and only the licensing tail looks close to true product economics (B04). Clients cannot easily do without this work because Systango's engineers are embedded inside the client's own product team, so switching mid-project carries real cost, even if that cost is modest next to a true platform lock-in (B04). Customers are largely early-stage and growth-stage companies, with roughly 10% enterprise or public-sector accounts (B05); the business is heavily concentrated, with the top ten clients taking 65-72% of consolidated revenue every year from FY23 to FY26, and the top three taking 38-42% (B04). Demand today rests on the offshore wage-arbitrage model — Indian delivery billed in GBP and USD — and on Clutch "Top" rankings and niche reputation in Web3, GenAI, and cloud consulting that help win work in a crowded, fragmented global market (B04, B07). B09's downstream candidates tie this demand to a small number of externally checkable channels: AWS and Google Cloud partner-tier status, a newly entered Alibaba Cloud alliance, and UK and US enterprise IT-spending trends, since 65.65% of FY26 revenue originates in the UK and 28.04% in the US (B09, B04). Demand should grow, on management's own framing, if the mix keeps shifting toward AI/ML/Data/Cloud work — already 46% of FY26 technology-service-line revenue, up from an undisclosed prior-year split — and if hyperscaler partnerships and the Alibaba alliance convert into named client wins rather than remaining claim-tier items (B04, B07, B09). The clearest quality signal in the corpus is that revenue per employee nearly doubled, Rs 16.8 lakh to Rs 29.4 lakh, FY23 to FY26, while headcount barely moved, which points to a real mix and pricing upgrade rather than growth bought with bodies (B04). Set against this, B07's emerging-moat scan found no confirmed new moat (em_score 10, below its own 12-point floor for a positive classification) and rated two of its scored categories — customer concentration and working-capital trends — as documented deteriorations, not improvements, over FY23-FY26 (B07). Competitive advantage in the single reportable business line is narrow and not brand-driven: B04 finds a cost advantage that is industry-wide rather than company-specific, low-to-moderate switching costs from embedded teams, and no scored moat in scale, distribution, network effects, or efficient scale; B07's forward scan adds that every AI/GenAI/Alibaba claim currently sits at claim-tier evidence only, unconfirmed by a disclosed revenue line or signed contract. In short, the line has a real but narrow moat today (cost arbitrage plus some embedded-team stickiness) and no confirmed moat yet in the higher-value tier it says it is moving toward.

---

## SECTION 4: DOWNSTREAM DOSSIER

### a. Verticals framed (one per Section 2 dominant variable)

**Vertical 1 — Revenue-per-employee mix-shift.** What the corpus establishes: revenue per employee rose from ~Rs 16.8 lakh (FY23) to ~Rs 29.4 lakh (FY26) consolidated, alongside near-flat headcount (312 to 308) (B04). What it cannot establish: whether the rise reflects genuine pricing-power upgrade on AI/GenAI work, one or two large high-realisation contracts, or a currency/FX effect (GBP/USD versus INR movement is a two-way factor B04 names separately). Deciding questions: (1) What is the rupee split between staff augmentation, managed contracts, and licensing revenue, and what share is genuinely recurring? (2) Does per-head realisation keep rising if a top-3 client is added or removed? (3) How much of the increase is currency-driven versus mix-driven?

**Vertical 2 — AI/ML/Data/Cloud technology-line share.** What the corpus establishes: 46% of FY26 revenue by technology service line, from a June-2026 investor-deck pie chart (B04). What it cannot establish: the prior-year (FY23-25) split — B07 flags this as an input gap, so no trend exists yet, only a single data point. Deciding questions: (1) What was the AI/ML/Data/Cloud share in FY24 and FY25? (2) Is 46% growing, or is FY26 a one-off skew from a single large AI-classified engagement? (3) Does the FY26 AR, once published, disclose this split with audited backing rather than a deck chart?

**Vertical 3 — Client concentration.** What the corpus establishes: top-3 clients at 38-42% and top-10 at 65-72% of consolidated revenue every year FY23-FY26 (June-2026 deck) (B04); a separate 46-48% top-3 figure for H1FY26 from a Nov-2025 deck cited in the spear brief (B00). What it cannot establish: which basis (H1FY26 vs FY26 full-year) is correct, or whether concentration genuinely eased in H2FY26 as B04 speculates, or whether the two decks measure different scopes. No named client identities exist anywhere in the corpus (B03: "no segment/customer note exists in either standalone or consolidated notes"). Deciding questions: (1) Why do the two decks show different top-3 percentages for overlapping periods? (2) What is the renewal status of the top-3/top-10 clients entering FY27? (3) Has any single top client's revenue share moved materially in either direction?

**Vertical 4 — Cash-conversion of the growth.** What the corpus establishes: standalone CFO/PAT fell to 0.348x in FY25 from 0.506x FY24 even as PAT grew 42.9%; consolidated CFO/PAT sat at 0.522x/0.513x FY25/FY24; standalone receivable turnover fell from 7.81x to 4.90x (B03 Phase 3A, 2D). What it cannot establish: whether this is a temporary artifact of onboarding larger, slower-paying clients during the mix-shift (the WC-days data shows a swing that partly self-corrected: 45→69→82→48 days FY23-26, per B01 Block B4) or an emerging structural collection problem. Deciding questions: (1) Does standalone CFO/PAT recover toward 0.7x in FY26/FY27 quarterly disclosures? (2) Does DSO stabilise below ~75 days or continue rising toward 90+? (3) Is the receivables deterioration concentrated in the related-party book (Systango Inc USA owed Rs 353.46 lakh at FY25-end, per B04) or spread across third-party clients?

### b. Candidate signal table (expanded from B09 SECTION 6, unverified, for Role 5.5 to verify)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| AWS Partner Network tier status (Select Tier Services Partner) | Tier downgrade, non-renewal, or removal from the directory | Quarterly | AWS Partner Network directory |
| Google Cloud Partner status & GenAI specialisation | Certification lapses or is not renewed at the stated tier | Quarterly | Google Cloud Partner directory |
| Alibaba Cloud strategic alliance (entered FY26) | No named client win or attributable revenue line within 12-18 months | Event-driven | Alibaba Cloud partner announcements / NSE exchange filings |
| UK ICT/digital-services outsourcing spend | Sustained multi-quarter decline in UK ICT outsourcing spend | Quarterly | ONS ICT services statistics / techUK |
| US enterprise digital-transformation/IT spend | A material downgrade to forecast US IT/digital-transformation spend | Quarterly | Gartner IT spending forecast |
| Top-10 client revenue concentration (72% of FY26 revenue) | Concentration rises further above FY26 levels with no offsetting new-client disclosure | Quarterly | Company investor presentation / RPT disclosures |
| Tech Alchemy Ltd (UK) pending acquisition | Deal lapses, is withdrawn, or remains undisclosed in a filing beyond a further 12 months with no stated reason | Event-driven | NSE/BSE exchange filings, UK Companies House |

### c. Fragility read

- **variable_count:** 8 — (1) AI/GenAI revenue-mix shift continuing, (2) client concentration not worsening, (3) cash-conversion (CFO/PAT, receivables) recovering, (4) hyperscaler/Alibaba partnerships converting to disclosed revenue, (5) UK+US IT/digital spend macro tailwind holding, (6) SEZ tax-holiday sunset (Sec 10AA) not compressing PAT ahead of the mix-shift offsetting it, (7) forward-guidance credibility improving with no further large misses, (8) DBX Holdings/GreenLeaf TDG ownership resolving without an undisclosed related-party control finding.
- **verifiability_ratio:** "4 of 8 externally observable" — externally checkable: hyperscaler/Alibaba partner-directory status, UK/US macro IT-spend data, the statutory SEZ Sec 10AA schedule, and DBX Holdings/GreenLeaf ownership via UK Companies House. Company-narrated only: the AI/GenAI mix-shift trend, client concentration, cash-conversion recovery, and forward-guidance credibility.
- **single_point_failure:** "Loss of any one top-3 client (38-42% of consolidated revenue, B04) — no named replacement pipeline is disclosed anywhere in the corpus, so a single exit could by itself reverse the growth trajectory the transition depends on."
- **fragility_verdict:** **FRAGILE** — eight interlocking variables, half of them checkable only through company narrative, plus one named single-point-failure.

### d. Research brief (live-web work order for claude.ai)

1. Pull DBX Holdings Ltd (UK co. 15645030) officers/PSC record directly from Companies House to confirm or rule out a Nilesh Rathi control/co-director link (B08 highest-priority item).
2. Pull GreenLeaf TDG Ltd (UK co. 11489069) officers/PSC record to establish ownership % and any promoter connection (B08).
3. Pull Systango Ltd UK (co. 07912276) officers list to cross-check the claimed shared registered address / "mutual person" with DBX Holdings (B08).
4. Fetch the ValuePickr forum thread (forum.valuepickr.com/t/systango-technologies-ltd/150052) directly for community-sourced claims on DBX Holdings, loans-to-Others recipients, and promoter record (B00, B08 could not fetch it).
5. Fetch the NSE archive filings directly — the 3-Oct-2025 intimation and the 7-Nov-2025 board-meeting outcome — to rule in or out a CFO/Company Secretary resignation-and-withdrawal event (B08 unresolved).
6. Pull the FY26 Annual Report once published (BSE/NSE/company IR) to resolve DBX Holdings and GreenLeaf TDG ownership %, control basis, and business rationale; segment/customer concentration; consolidated Note 22 gaps; and CARO loan-book movement for FY26 (B00, B02, B03).
7. Confirm whether the company has resumed investor calls (any post-Nov-2023 concall or webcast), or whether the practice has genuinely lapsed (B05 CORPUS GAPPED-FRESHNESS).
8. Verify the Tech Alchemy Ltd (UK co. 10443169) transaction's current status (closed / still pending) and its funding source, given the deal size (~GBP 1.5M) exceeds the Rs 800L IPO acquisitions bucket shown at 0% utilisation (B03, B08).
9. Confirm the current promoter shareholding pattern and pledge status against a primary NSE filing, not the media-sourced screener figures carried as a non-anchored lead (B00, B08).
10. Where identifiable, check counterparty filings or public disclosures for the top-3/top-10 named clients to independently test the concentration and receivables-quality risk (B04, per Downstream_Source_Discovery_Protocol_v1_0).
11. Check AWS, Google Cloud, and Alibaba Cloud partner directories for Systango's current certification tier and any named co-sell activity (B09 candidates).
12. Search for any rating-agency coverage or broker/research note on Systango, given none is held in this corpus (Section 1, RESEARCH/RATING gap).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Systango is a small IT company based in Indore. It builds software, AI systems, and blockchain tools (B04).
2. It has about 300 people. Most of its work goes to clients in the UK and the US (B04).
3. It bills clients in pounds and dollars. It pays its own engineers in rupees. That gap is the core of its cost edge (B04).
4. Most clients are early-stage or growth-stage companies. About one in ten is a larger enterprise or public-sector client (B05).
5. Clients hire Systango to build or run digital products. Its teams often sit inside the client's own product group (B04).
6. Ten clients supply 65 to 72 percent of group revenue every year from FY23 to FY26. Three clients supply 38 to 42 percent (B04).
7. Revenue per employee nearly doubled, from about Rs 17 lakh in FY23 to about Rs 29 lakh in FY26, while headcount barely moved (B04).
8. Management says it is shifting work toward AI, machine learning, and cloud projects. This work was 46 percent of FY26 technology revenue (B04).
9. Management's own revenue targets have missed badly. It guided Rs 250 crore by FY26 and delivered about Rs 90 crore (B05).
10. Only one guided promise was kept: the EBITDA margin target. It guided above 25 percent and delivered 37.6 percent in FY26 (B05).
11. The company's main edge is cheap, skilled Indian engineers billed at UK and US rates. This edge is industry-wide, not unique to Systango (B04).
12. Embedded client teams create some cost to switch away from Systango. This is a soft edge, not a hard one. Pricing power stays weak to moderate (B04, B07).
13. The core bet is a climb: from a plain cost-arbitrage shop toward a stickier, higher-value specialist supplier. The proof has not shown up across enough quarters yet (Section 2).
14. This story depends on many things going right together, and about half of them can only be checked by trusting the company, not by an outside source. One lost top client could reverse the trend by itself. The fragility read is FRAGILE (Section 4).
15. The corpus has no FY26 Annual Report and no concall after November 2023. It cannot yet check FY26 loan-book movement, related-party detail, or client-name-level concentration (Section 1). The single biggest open question is whether promoter Nilesh Rathi controls or co-directs DBX Holdings, the UK company Systango's cash flowed into the same year it stopped being a customer (B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Filename and page anchor on every printed figure. NOT DISCLOSED given where the corpus does not carry it.

### 1. Units

No per-hour or per-project billing rate is printed anywhere in the corpus. The one printed per-engagement figure is average ticket size: **"$75,000 to $100,000"** — average project/ticket size, given as an ongoing figure, not tied to one product (basket-level, spanning the mixed service lines) (Concall_Jul_2023_Transcript.pdf, p.14, as reported in 05-concall.md Section 1B). No revenue-per-employee figure is printed as such in any single document either; it is a derived figure the pipeline computed from two disclosed lines: consolidated revenue (Investor_Presentation_1.pdf, "Historical Consolidated Income Statement") and headcount (Investor_Presentation_1.pdf, "Key Performance Metrics," "Employee Bifurcation" chart, technical + support). Comment: the business has no single physical unit of sale (it blends staff augmentation, project billing, managed contracts, and licensing); revenue-per-employee is the best available proxy, and it covers the whole basket, not one product (B04).

### 2. Segment capital and debt

No AS-17/Ind AS 108 segment note exists in either the standalone or consolidated financial statements — confirmed by direct read at Stage 3: "no AS-17/Ind AS 108 segment note exists in either standalone or consolidated financials (confirmed by direct read through both note sets in full)" (03-ardeep.md, Phase 4C, citing AR FY24-25). NOT DISCLOSED: segment-level assets, liabilities, capital employed, and segment-allocated borrowings, because the company discloses only one reportable operating segment. Total borrowings are unallocated by construction; quoting the total instead: consolidated Long-term borrowings **"6.26"** (Rs lakh) at FY26 year-end, against Total assets **"15,049.81"** (Rs lakh) (SYSTANGO_14052026200758_Intimation.pdf, consolidated balance sheet, as reported in 01-gate0.md Block D). For FY25/FY24: "**Zero bank/FI borrowings, standalone or consolidated. Immaterial residual balance at consolidated level only (Rs3.07L, likely a subsidiary vehicle/lease-adjacent obligation…)**" (03-ardeep.md, Phase 2F, citing AR FY24-25 notes and cash flow statement). Standalone total assets: Rs 10,873.62 lakh (FY25) vs Rs 8,464.13 lakh (FY24) (03-ardeep.md Phase 3B, citing AR FY24-25).

### 3. Guidance versus aspiration

| Claim | Classification | Period stated | Source |
|---|---|---|---|
| FY26 revenue target Rs 250cr+ / $25M | (a) guidance with a period | By FY26 | Concall_Jul_2023_Transcript.pdf p.13, reaffirmed Concall_Nov_2023_Transcript_2.pdf p.5/p.7 |
| FY24 revenue growth ~30% (cut from implicit ~60%) | (a) guidance with a period | FY24, closing Mar-2024 | Concall_Nov_2023_Transcript_2.pdf pp.4-5 |
| EBITDA margin >25%, "if not better" / "25% Plus" | (b) aspiration without a fixed terminal period (open-ended, numeric) | Ongoing | Concall_Jul_2023_Transcript.pdf p.13; Concall_Nov_2023_Transcript_2.pdf pp.3-4,6,9 |
| Client count target ~40 (from 25-30) | (a) guidance with a period | Within 1 year | Concall_Jul_2023_Transcript.pdf p.10 |
| Blue-chip enterprise customer, at least 1 | (a) guidance with a period | FY24 | Concall_Jul_2023_Transcript.pdf p.4: "get at least one of the blue chip customer this year" |
| Institutional-grade crypto derivatives insights and analytics platform | (a) guidance with an implied period | "probably three months away from the launch" | Concall_Jul_2023_Transcript.pdf p.4 (verbatim: "...one such product that I'm really excited about where we are in probably three months away from the launch is an institutional grade crypto derivative insights and analytics platform...") |
| UK JV/acquisition close | (a) guidance with a period, revised | 6-9 months (Jul-2023), revised to 6-12 months (Nov-2023) | Concall_Jul_2023_Transcript.pdf pp.10-11; Concall_Nov_2023_Transcript_2.pdf pp.7-8,10 |
| Dubai office | (a) guidance with a period | Within 6 months of Nov-2023 | Concall_Nov_2023_Transcript_2.pdf pp.2-3 |
| "We are confident we will hit the objective this year" (further acquisitions, an IPO object) | (a) guidance with a period | FY26 ("this year," from the AR's Sept-2025 signing date) | Annual_Report_2023.pdf (=FY24-25 AR), Founders' Note, p.13 |
| UK marketing team build-out; strengthened US business development | (c) capacity/capability only, no budget/headcount/milestone | FY26 | Annual_Report_2023.pdf, Founders' Note, p.13 |
| Freshers-hiring / young-talent narrative | (c) capacity/capability, claimed as already executed but not quantified | FY25 | Annual_Report_2023.pdf, Founders' Note, p.13 |

### 4. Concentration

- **Product/technology-line concentration (FY26):** AI/ML/Data/Cloud 46%, App Development 38%, Blockchain/Web3 16% (Investor_Presentation_1.pdf, "Company Overview" pie chart, "FY26 Services Revenue Breakup," as reported in 04-bizmodel.md).
- **Customer concentration:** top-3 clients 38-42% and top-10 clients 65-72% of consolidated revenue every year FY23-FY26 (Investor_Presentation_1.pdf, "Key Performance Metrics," chart "Revenue by Major Clients"). A separate, unreconciled figure of top-3 at 46-48% for H1FY26 appears in the spear brief, sourced to a Nov-2025 deck not held in this corpus (B00, B04 flag).
- **Geography concentration (FY26):** UK 65.65%, US 28.04%, Canada 2.92%, rest of world 3.39% (Investor_Presentation_1.pdf, "Geographical Presence").
- **Related-party revenue concentration:** "FY25 total related-party sales Rs1,972.03L = 32.2% of standalone revenue... FY24 Rs2,219.61L = 42.1%" (03-ardeep.md Phase 2B, citing AR FY24-25 Note 21C.8, p.89-91). Named counterparties: LLC USA, Isystango UK, Ltd UK, DBX Holdings, Inc USA (see Q8).
- Comment: no named-client identities exist anywhere in the corpus; concentration is disclosed only at the top-N aggregate level, and only in the investor deck, not in the AR (03-ardeep.md Phase 4B: "no external client-concentration disclosure exists at all").

### 5. Promise ledger

| Date made | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| 7-Jul-2023 | FY26 revenue target Rs 250cr+ / $25M | MISSED — delivered Rs 90.4cr (~64% shortfall) | Concall_Jul_2023_Transcript.pdf p.13, reaffirmed p.5/p.7 of Concall_Nov_2023_Transcript_2.pdf; delivery per SYSTANGO_14052026200758_Intimation.pdf (05-concall.md) |
| 17-Nov-2023 | FY24 revenue growth ~30% (cut from ~60%) | MISSED — actual ~8% | Concall_Nov_2023_Transcript_2.pdf pp.4-5 (05-concall.md) |
| 7-Jul-2023 | EBITDA margin >25% | DELIVERED / EXCEEDED — 37.6% FY26 | Concall_Jul_2023_Transcript.pdf p.13; delivery per Investor_Presentation_1.pdf p.30 (05-concall.md) |
| 7-Jul-2023 | Close UK JV/acquisition within 6-9 months | PARTIAL — still unclosed at Nov-2023, timeline extended | Concall_Jul_2023_Transcript.pdf pp.10-11; Concall_Nov_2023_Transcript_2.pdf pp.7-8,10 (05-concall.md) |
| 7-Jul-2023 | Land at least one blue-chip enterprise customer in FY24 | NOT FOUND — never referenced again after Jul-2023 | Concall_Jul_2023_Transcript.pdf p.4; silence confirmed against Concall_Nov_2023_Transcript_2.pdf (05-concall.md) |
| 7-Jul-2023 | Grow client count 25-30 → ~40 within one year | NOT FOUND — no client-count figure given in the Nov-2023 call | Concall_Jul_2023_Transcript.pdf p.10; silence confirmed against Concall_Nov_2023_Transcript_2.pdf (05-concall.md) |
| 7-Jul-2023 | Institutional-grade crypto derivatives platform, ~3 months from launch | NOT FOUND — never confirmed launched; absent from all later documents reviewed | Concall_Jul_2023_Transcript.pdf p.4 (verbatim quote above); absence confirmed against Concall_Nov_2023_Transcript_2.pdf, Annual_Report_2023.pdf, and Investor_Presentation_1.pdf (verifier B12b MAJOR finding) |
| Sept-2025 (AR signing) | "We are confident we will hit the objective this year" (further acquisitions, IPO object) | LOW credibility — Rs 800L acquisitions IPO bucket at 0% utilisation more than two years post-listing | Annual_Report_2023.pdf, Founders' Note p.13; Board's Report IPO-utilisation table pp.36-37 (03-ardeep.md Phase 2H) |
| 19-Jun-2025 (external) | Tech Alchemy Ltd (UK) acquisition, "in the process of signing a binding acquisition agreement" | AR-SILENT — real, signed deal per external web search (B08), but absent from the AR's own AOC-1, Board's Report, and subsequent-events sections | Annual_Report_2023.pdf, Founders' Note p.13 (claim); AOC-1, Board's Report Annexure-A, pp.40-43 (silence); external corroboration outside this corpus (B08) |

### 6. Restated bases

Prior-period comparatives carry only a generic, non-itemised regrouping statement: **"Figures for the previous year has been regrouped and/or rearranged wherever considered necessary"** (Annual_Report_2023.pdf, standalone Note 21C.2, p.~87-88, as quoted in 02-notes.md). No specific line item or amount is quantified anywhere against this statement — assessed as minor, boilerplate, not a substantive restatement (02-notes.md, 03-ardeep.md Pass 3 finding #3). Comparative figures as printed in the latest filing (FY25 column, FY24 comparative): standalone revenue from operations Rs 6,132.96 lakh (FY25) vs Rs 5,267.91 lakh (FY24); standalone PAT Rs 2,320.33 lakh (FY25) vs Rs 1,624.19 lakh (FY24) (Annual_Report_2023.pdf, P&L and Note 16, as reported in 03-ardeep.md Phase 3C). No substantive going-concern doubt language found; only the standard basis-of-preparation going-concern statement appears (Note 21B.1.2, per 02-notes.md).

### 7. Corporate-action clauses

No scheme, demerger, merger, preferential issue, or buyback is disclosed anywhere in the corpus documents held. The closest related item is the Tech Alchemy Ltd (UK) asset/team acquisition, but it is not a scheme under the Companies Act and its clause-level detail — definitions of undertaking, liability allocation, ratios, appointed and effective dates — is **NOT DISCLOSED in this corpus**: the AR's Founders' Note (p.13) names the counterparty only in a single narrative sentence, with no further mention anywhere else in the same document (03-ardeep.md Phase 6E: "Tech Alchemy Limited does not appear anywhere — not as a subsidiary, not as an associate, not as a post-balance-sheet event... not in the Board's Report's own narrative sections"). The transaction's actual terms — GBP 1,500,000, a Memorandum of Terms dated 19-Jun-2025, counterparty St Topco Limited — come from a web search conducted outside this corpus at Stage 8 (08-promoter.md), not from a filing held in the corpus. Filing to fetch: the NSE/BSE exchange intimation and the underlying Memorandum of Terms/agreement for the Tech Alchemy transaction, and the FY26 AR (once published) for AOC-1 subsidiary/associate treatment.

### 8. Related-party perimeter

FY25 related-party sales table, standalone, from AR Note 21C.8 (p.89-91), as reported in 03-ardeep.md Phase 2B:

| Related party | Nature | FY25 amount | FY24 amount |
|---|---|---|---|
| Systango LLC (USA) [liquidated 19-Dec-2024] | Services/sales | Rs 160.88L | Rs 1,803.13L |
| Isystango UK | Services/sales | Rs 131.42L | Rs 194.47L |
| Systango Ltd UK | Services/sales | Rs 521.92L | Rs 65.03L |
| DBX Holdings Ltd | Services/sales | NIL | Rs 156.98L |
| Systango Inc. USA | Services/sales (AOC-2 material contract, Board-approved 14-Nov-2024) | Rs 1,157.81L | NIL |
| A promoter HUF and a partnership firm | Named in the related-party list; exact entity names NOT FOUND in the material reviewed by any stage | (component of totals below) | (component of totals below) |

**Total FY25 related-party sales:** Rs 1,972.03L = 32.2% of standalone revenue. **Total FY24:** Rs 2,219.61L = 42.1% (03-ardeep.md Phase 2B). **Related-party receivables outstanding FY25:** Rs 618.06L = 38.7% of total standalone receivables (Rs 1,598.47L) (same source). Equity-stake investments in related/formerly-related entities (Consolidated Note 8, p.112): DBX Holdings Ltd, 19,500 shares of GBP 0.001 each, cost Rs 166.11L (Previous Year Nil); GreenLeaf TDG Ltd, 320 shares of GBP 1 each, cost Rs 35.88L (Previous Year Nil) — both confirmed present in Note 8 by verifier A against Stage 7's contrary NOT-FOUND claim (12a-verifier.yaml). Directors' remuneration, Vinita Rathi and Nilesh Rathi combined: Rs 179.72L (FY25) vs Rs 138.60L (FY24), = 7.75% of standalone PAT (03-ardeep.md Phase 5C, citing Consolidated Note 19).

### 9. Pledge and shareholding

Last-twelve-quarters shareholding pattern: **NOT DISCLOSED in this corpus.** The AR carries only annual snapshots at 31-Mar-2023, 31-Mar-2024, and 31-Mar-2025, not quarterly filings: **"71.96% (FY23) → 71.96% (FY24, unchanged) → 72.07% (FY25)"** (Annual_Report_2023.pdf, Notes 1D/1E, p.76, as quoted in 01-gate0.md Block E). Pledge: **"N/A (not in provided data)... This AR states SEBI LODR Schedule V Para C corporate-governance disclosures (which would normally carry pledge detail) do not apply because the company is listed on the SME Emerge platform"** (01-gate0.md Block E3, citing AR FY24-25 Board's Report corporate-governance note). No pledge percentage is printed in any corpus document; treated as NOT FOUND, not confirmed-zero. Institutional holding, latest: **NOT DISCLOSED** — "No FII/DII trend table located in this AR" (03-ardeep.md, 5D). A Mar-2026 figure (Promoter 72.17%, FII 0.47%, DII 1.69%, Public 25.67%, 2,637 holders) exists only as an operator-pasted screener lead, explicitly flagged non-anchored and never a filed source (B00).

### 10. Verification

Filenames and dates of every document quoted in this annex:
- `Annual_Report_2023.pdf` — actually the 21st Annual Report, FY2024-25, year ended 31-Mar-2025; auditor's report dated 26-May-2025; Founders' Note/Board's Report signed 4-Sep-2025.
- `Concall_Jul_2023_Transcript.pdf` — held 7-Jul-2023 (FY23 annual call).
- `Concall_Nov_2023_Transcript_2.pdf` — held 17-Nov-2023 (H1FY24 call).
- `SYSTANGO_14052026200758_Intimation.pdf` — filed 14-May-2026 (FY26 audited full-year results).
- `Investor_Presentation_1.pdf` — dated June 2026 ("Annual Update" deck, FY26 headline data).

**CORPUS COMMIT HASH: bd1fb48acf73463c37f111f712db0658dc44cd3e**

---

```yaml
stage: B09b-dossier
company: "SYSTANGO"
run_date: "2026-08-29"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - document: "FY26 concall transcript"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "FY26 Annual Report"
    expected_source: "BSE"
    kind: "freshness-pair"
  - document: "Prospectus"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Rating / rating rationale"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
  - document: "Dedicated corporate-action announcement filings"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Shareholding pattern filing, post-31-Mar-2025"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Research / broker notes"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Digital-engineering / IT services (single reportable segment)"
    archetype: "Outsourcing partner (CDMO/EMS/IT services)"
transition:
  - line: "Digital-engineering / IT services (single reportable segment)"
    from_tier: "R2 COST-ADVANTAGED CONVERTER (qualitative fit; ROCE 27-33% sits above R2's stated mid-teens band, an unresolved tension flagged not resolved)"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (claimed, via AI/GenAI mix-shift and embedded-team/licensing stickiness)"
    engine: "Technology-line revenue mix shifts toward AI/ML/Data/Cloud work at higher realisation per employee, plus delivery moving from pure staff augmentation toward embedded product-team pods and owned, licensable IP"
    proof_gate: "Revenue per employee keeps rising from its ~Rs29.4L FY26 base AND AI/ML/Data/Cloud technology-line share holds at/above its 46% FY26 level for 2+ consecutive disclosed periods, with revenue growth outpacing headcount growth"
    recognition_gap: "OPEN QUESTION, resolved at Stage 11 via the Section 1B destination-PE gap: does the current multiple already sit near the claimed R3 neighbourhood, or nearer the FROM R2 neighbourhood -- no number or conclusion stated here"
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "AI/ML/Data/Cloud technology-line share falls back toward or below its pre-FY26 level, and/or revenue per employee flattens or reverses over 2+ consecutive disclosed periods"
dominant_variables:
  - "Revenue per employee (mix-shift proxy): rose ~Rs16.8L (FY23) to ~Rs29.4L (FY26)"
  - "AI/ML/Data/Cloud share of technology-service-line revenue: 46% FY26, no prior-year trend disclosed"
  - "Top-3/top-10 client concentration: top-3 38-42%, top-10 65-72% FY23-FY26, with an unreconciled H1FY26 46-48% figure"
  - "Standalone cash-conversion (CFO/PAT, receivable turnover): CFO/PAT 0.348x-0.522x across all 4 cells, all below 0.7x; receivable turnover fell 7.81x to 4.90x"
business_falsifier: "Confirmation that DBX Holdings Ltd is controlled or co-directed by promoter Nilesh Rathi would re-characterise the FROM business's capital allocation as a pattern of related-party extraction (unnamed 'Others' loans plus a customer-to-equity-investee conversion the same year) rather than an isolated disclosure gap, undermining the organic, non-leverage-driven ROE read the Gate 0 score currently rests on"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 8
  verifiability_ratio: "4 of 8 externally observable"
  single_point_failure: "Loss of any one top-3 client (38-42% of consolidated revenue) with no named replacement pipeline disclosed"
  fragility_verdict: "FRAGILE"
candidate_count: 7
research_brief_items: 12
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "bd1fb48acf73463c37f111f712db0658dc44cd3e"
```
