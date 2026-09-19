# STAGE 7 — EMERGING MOAT SCAN (22-CATEGORY + FAMILY I), eMudhra Ltd (EMUDHRA)

Run date: 2026-09-19. Pipeline mode, six sections in one pass. This is the
Emerging Competitive Advantages scan (Categories A1-R1, adjusted 0-90 scale
with the 20-Aug-2026 Family I addition). It is NOT FTTCP. FTTCP is a
separate, later synthesis inside the valuation stage.

Evidence taxonomy used throughout: 📄 DOCUMENTED (capex committed, contract
signed, product launched, regulatory filing), 🎙️ MANAGEMENT CLAIM (concall
or presentation, not yet backed by capital or a signed contract), 🔍 ANALYST
INFERENCE (pattern-based).

---

## CORRECTION (VERIFIER C), 2026-09-19

Verifier C (framework adherence, phase 1, opus, fresh context) reviewed
this stage against prompts/07-emerging-moat-pipeline.md and re-derived the
scorecard independently. Five findings applied to this stage. Each was
checked against the source documents before correcting; all five held up.

1. **E1 row (MAJOR, verifier finding 3).** Confirmed: E1 scored HH=4 at
   📄 1.0x (the maximum) but the write-up included an unanchored
   comparative claim — "positioning eMudhra in Central Asia ahead of most
   listed Indian identity/security peers" — with no source, and read the
   East Africa case study's "one of East Africa's first nations" language
   as evidence of eMudhra's own first-mover lead, when it describes the
   customer nation's status, not eMudhra's standing against peers.
   Corrected: E1 rescored MH=3 at 📄 1.0x = 3.0 (was 4.0), strength
   relabelled Moderate (was Strong). See Section 3 and Section 5.
2. **Section 2C / capex_embedded_growth_pct (MAJOR, verifier finding 4).**
   Confirmed: the original arithmetic applied a PP&E-only fixed asset
   turnover (5.43x, excludes goodwill/intangibles) to a numerator (Rs
   291.76 Mn) that included intangible assets under development — a
   basis mismatch. Corrected: the settled figure now uses the run's own
   consistent fixed-asset-turnover convention (B01-gate0 M3: FAT =
   Revenue / Net Block, screener-data basis, which includes PP&E + CWIP +
   goodwill + intangibles = 0.97x), applied to the same Rs 291.76 Mn
   numerator. Settled figure: **4.0%** (was 22.6%). The basis choice is
   genuinely open, so the range (4.0%-22.6%, three readings) is shown
   explicitly in Section 2C rather than collapsed to one number.
3. **R1 narrative/score inconsistency (MINOR, verifier finding 9).**
   Confirmed: Section 4C stated the shared, non-exclusive nature of the
   regulatory tailwinds "tempers R1's score" while the scorecard kept R1
   at the maximum HH=4. Corrected: the sentence is rewritten so the
   competitive-capture caveat is stated as a distinct question (for
   Role 2/FTTCP, not this scan) without claiming it lowers R1's own
   likelihood×impact read. R1 stays at HH=4 (📄, 1.0x = 4.0); no score
   change from this item.
4. **evidence_mix / None-Weak row count (MINOR, verifier finding 10).**
   Confirmed: the YAML evidence_mix documented count (24) did not
   reconcile to the Section 3 recount (19 items, no reconciliation shown),
   and the completionist paragraph said "14" None/Weak rows where 23 - 8
   active = 15. Both corrected: evidence_mix.documented set to 19
   (matching the recount exactly, no additional untallied items claimed);
   "14" corrected to "15" in Section 3.
5. **Section 1C estimated fill (MINOR, verifier finding 11).** Confirmed:
   Section 1C marked Services FY27 growth "NOT FOUND" then filled it with
   an assumed ~16.5% and derived FY27E Services and company-total figures
   from that assumption, breaking the NOT FOUND-only rule. Corrected: the
   assumed growth rate and every figure derived from it are removed;
   Services FY27E and the company FY27E total are now marked NOT FOUND.

**em_score restated: 22.1 / 92 (was 23.1). Classification unchanged: 12-24
band, MODEST MOAT DEVELOPMENT.** Both MAJOR findings move the score down;
none raised it. Gate 0 (B01) findings from the same verifier pass (Part 1
of the verifier report, CRITICAL/MAJOR items on B01 Block B/A) are a
separate REWORK routed to Stage 1, not corrected here. Section 6C/6D below
still read the B01-as-filed GOOD classification and should be re-read once
B01 is reworked, per the verifier's own routing note.

---

## SECTION 1: FUTURE PRODUCT & REVENUE STREAM ANALYSIS

### 1A. New products/services in pipeline

| Product | Status | Evidence | Expected launch / date | Revenue potential stated? | How different from current portfolio |
| --- | --- | --- | --- | --- | --- |
| ID Broker (federated identity brokering: OIDC/SAML/EBSI/ISO mDL, EUDI Wallet, UAE PASS, Nafath) | LAUNCHED-recent | 📄 (AR p.21-22, "eMudhra's Competitive Edge" p.10) | FY2025-26, in market | NOT FOUND (no per-deal or segment revenue disclosed) | New product pillar (sixth), not a variant of an existing one; sits between identity and applications |
| Data Discovery and Management Platform (branded "PrivaTrust" in later press material) | LAUNCHED-recent | 📄 (AR p.28-29; product named "PrivaTrust" in GLEIF press release 13-Sep-2026, inputs/announcements/20260913-8955c07b) | FY2025-26, "introduced recently" | NOT FOUND | Genuinely new category: data/privacy governance, not trust/signing infrastructure |
| Agentic AI Security Platform (cryptographic identity for AI agents) | LAUNCHED-recent | 📄 ("In February 2026, eMudhra introduced the Agentic AI Security Platform," AR p.20/33-34) | Feb-2026 | NOT FOUND; concall frames this as "early stage, hard to quantify" (B05 trigger 7, conviction L) | New object class (agent identity) layered on SecurePass, not a feature update |
| emSigner for SMEs | LAUNCHED-recent | 📄 (AR p.16; Reg 30 press release 17-Apr-2026, corrected 17-Apr-2026, inputs/announcements/20260417-8f60da77 and -42cf4e2a) | 17-Apr-2026, live | Priced from Rs 1,000; no revenue figure disclosed | Moves downmarket from enterprise to SME/CA-partner channel |
| emSigner for Retail Consumers | LAUNCHED-recent | 📄 (AR p.16) | FY2025-26 | NOT FOUND | Extends the same product to individual/retail use cases (property, education documents) |
| Post-Quantum Cryptography Advisory Services (expanded) | LAUNCHED-recent | 📄 (AR p.23; Reg 30 press release 23-Feb-2026, inputs/announcements/20260223-01b04755) | 23-Feb-2026 | NOT FOUND | Advisory/services line layered on emCA engineering, not a licensed product |
| GLEIF/LEIL Validation Agent role (LEI issuance/renewal embedded in onboarding) | ANNOUNCED | 📄 (Reg 30 press release 13-Sep-2026, inputs/announcements/20260913-8955c07b) | 10-Sep-2026 (post FY26 year-end; FY27 event) | NOT FOUND | New regulated-identity adjacency (Legal Entity Identifiers), first instance |
| UAE QTSP (Qualified Trust Service Provider) licence + in-country data centre | REGULATORY PENDING | 🎙️/📄 mixed: press release referenced but licence not yet granted; targeted "end of this quarter to beginning of next" (~Sep-Oct 2026) per Q1 FY27 call; CWIP Rs 185.84 Mn consolidated (AR p.150/Note 3b) | ~Sep-Oct 2026 | NOT FOUND | Extends the licensed-CA business model (India's core, 20% of revenue) into a second sovereign jurisdiction |
| GenAI features for emSigner, Remote Signing, emCA/CertiNext | UNDER DEVELOPMENT | 🎙️/📄 (AR p.148, "R&D and Product Development": "plan to develop GenerativeAI capabilities... Natural Language instruction, model context protocol, LLM Application") | FY2026-27 ("upcoming financial year") | NOT FOUND | Feature layer on existing products, not a standalone new product |

FPI (Foreign Portfolio Investor) DSC onboarding service — 📄 Reg 30 press
release 09-Feb-2026 (inputs/announcements/20260209-8e37cf4b): new
customer-segment access (FPIs registering in Indian capital markets), not a
new product per se, carried here as a new revenue-adjacent access point.

### 1B. Diversification direction

| Direction | Evidence | Timeline |
| --- | --- | --- |
| Product | Data Discovery/Privacy platform is a genuinely new category (trust infrastructure → data infrastructure), 📄 AR p.28 | FY2025-26, live |
| Customer | emSigner for SMEs/retail moves downmarket from enterprise-only via a CA/CS partner channel, 📄 AR p.16 | FY2025-26, live |
| Geographic | Almaty (Kazakhstan) office opened 📄 (Reg 30, 20-Feb-2026); UAE QTSP build 🎙️/📄 in progress; LankaPay (Sri Lanka) partnership 📄 (12-Feb-2026) | FY2025-26 through ~FY27 |
| Channel | Partner-led SME/CA-CS channel is a new go-to-market motion distinct from the existing 60% direct / 40% partner enterprise split (Q4FY26 Inv. Pres. p.19) | FY2025-26, live |
| Vertical integration | NOT FOUND (no evidence of moving up/down a physical supply chain; not applicable to this business model) | n/a |

### 1C. Revenue mix shift

FY26 actual base (MD&A p.151, Note 49, reconciled against B04's three-stream
read): Trust Services 20% (Rs 1,400.08 Mn), Enterprise Solutions software
59% (Rs ~4,139 Mn), Services 21% (Rs ~1,473 Mn). Revenue from operations
total Rs 7,015.80 Mn, +35.1% YoY (MD&A p.151).

FY27E shift for the two streams the company actually guided (🎙️, Q4 FY26
call, carried in B05): Trust Services ~20% growth → FY27E Rs 1,680.10 Mn
(19.4% of a two-stream sub-total); Enterprise Solutions software ~25-30%
growth (midpoint 27.5%) → FY27E Rs 5,277.64 Mn (60.8% of a two-stream
sub-total).

| Stream | FY26 % | FY26 Rs Mn | FY27E growth | FY27E Rs Mn | Source |
| --- | --- | --- | --- | --- | --- |
| Trust Services | 20.0% | 1,400.08 | ~20% (🎙️) | 1,680.10 | Q4 FY26 call, B05 |
| Enterprise Solutions (software) | 59.0% | ~4,139.32 | ~27.5%, midpoint of 25-30% (🎙️) | 5,277.64 | Q4 FY26 call, B05 |
| Services | 21.0% | ~1,473.32 | **NOT FOUND** | **NOT FOUND** | No company guidance found for this stream (corrected, Verifier C — the ~16.5% figure previously shown here was an unsourced assumption and has been removed, not estimated) |
| Total FY27E (all three streams) | 100% | 7,015.80 | **NOT FOUND** | **NOT FOUND** | Cannot be computed without the missing Services figure; not derived (corrected, Verifier C) |

FY28-FY29 stream-level growth rates: NOT FOUND. No company guidance exists
beyond FY27. Directionally, if the FY27 guided rates for Trust Services and
Enterprise Solutions persisted, Enterprise Solutions software share would
keep rising and Trust Services share would keep falling, but that is 🔍
inference, not a company forecast, and is not carried into any total.

Margin direction and profitability impact — the second-order finding
carried from B04: Trust Services segment margin is 31.4% FY26 (Note 49,
comparatively stable, licensed business). Enterprise Solutions margin is
NOT uniform: India 57.5% vs Outside-India 21.9% FY26, down from 26.0% FY25
even as international Enterprise Solutions revenue grew 38.3% (Note 49,
AR p.288). The stream growing fastest (Enterprise Solutions Global) is
also the one whose FY26 margin compressed, not expanded. This directly
qualifies the "operating leverage from mix shift" framing in company
memory: at the segment level, FY26 shows margin dilution from the
international mix shift, not leverage, even though the CONSOLIDATED
adjusted EBITDA margin rose (23.2% reported / ~25.7-25.8% adjusted per
Q4FY26 Inv. Pres. p.17) on overall opex scale. Both facts are true at
different levels of the P&L; a forward mix-shift table that assumes
margin accretion from Enterprise Solutions growth is not yet supported by
the FY26 segment note.

---

## SECTION 2: CAPACITY & CAPEX PIPELINE

### 2A. Capex programme table

| Project | Rs Mn (basis) | Funding source | Status | Expected commissioning | Capacity addition / % over current |
| --- | --- | --- | --- | --- | --- |
| UAE data centre (in-country, for QTSP licence compliance) | CWIP Rs 185.84 Mn consolidated / Rs 1.38 Mn standalone (AR p.150, Note 3b) | Operating cash flow, per MD&A p.153 ("balance was met out of operating cash flow") | Under construction | ~Sep-Oct 2026 (🎙️, Q1 FY27 call, aligned to QTSP licence grant) | NOT FOUND (no server/capacity metric disclosed) |
| US data centres (New Jersey, Salt Lake City) | Not separately costed in the AR; part of the Rs 213.21 Mn "Data Center and Server" MD&A line (p.156) | Operating cash flow / acquisitions (Ikon Tech, Two95) | Commissioned, operating (AR p.148: "the company has created Data Centers in New Jersey and Salt Lake City") | Live | NOT FOUND |
| Europe data centre (via Cryptas International GmbH) | Acquired, not separately costed (part of the Rs 1,101.35 Mn / Rs 629.03 Mn acquisition spend, see reconciliation below) | Acquisition consideration | Acquired 1-Jul-2025, operating | Live | NOT FOUND |
| Existing-product enhancement (capitalised) | Rs 124.62 Mn consolidated (MD&A p.156) | Operating cash flow | Ongoing | Continuous | n/a (product spend, not physical capacity) |
| New-product development (capitalised) | Rs 476.38 Mn consolidated (MD&A p.156) | Operating cash flow | Ongoing | FY2026-27 features (GenAI, PQC) | n/a |
| Cryptas / Two95 / AI Cyberforge acquisitions | Rs 1,101.35 Mn net of asset acquired, per MD&A p.156 investing-activities prose | Operating cash flow + Rs 82.87 Mn promoter/Chairman loans to two overseas subsidiaries (Note 16/44.2, first instance this year, B02 finding 9) | Completed (Cryptas/AI Cyberforge 1-Jul-2025; AI Cyberforge merged into eMudhra Inc 2-Feb-2026, Reg 30 20260202-4117a834) | Complete | n/a |

**Capex arithmetic — three different classifications in the same AR, shown
explicitly per the task instruction (they do not reconcile to each
other):**

1. **Cash-flow-statement basis (the authoritative figure for this stage
   and for Stage 9/11):** "Purchase of Property, plant and equipment and
   Intangible assets" = **Rs 1,853.68 Mn** FY26 (Rs 832.02 Mn FY25), AR
   p.218 (mupdf) / consol Cash Flow Statement line, cross-checked against
   the CFS heading in the AR text at line ~10619. Separately, the AR's own
   MD&A liquidity section (p.155) states: "acquisitions and capital
   expenditure aggregating to INR 2,482.71 Million" — this equals
   **Rs 1,853.68 Mn (capex) + Rs 629.03 Mn (acquisition payment)** almost
   exactly (Rs 1,853.68 + 629.03 = Rs 2,482.71 Mn), which is the figure
   this report and B01/B03 use.
2. **MD&A investing-activities prose basis (p.156):** existing-product
   Rs 124.62 Mn + new-product Rs 476.38 Mn + data centre/server
   Rs 213.21 Mn = **Rs 814.21 Mn**, plus "investment in Cryptas
   International GmbH, TWO95 International Inc., and AI Cyber Forge Inc"
   Rs 1,101.35 Mn net of asset acquired = **Rs 1,915.56 Mn** combined.
   This does NOT equal either the Rs 2,482.71 Mn total quoted one page
   later in the same AR, or the Rs 2,250.53 Mn total net cash used in
   investing activities (p.155 cash-flow table) — implying roughly
   Rs 335-567 Mn of investing-activity cash flow (e.g., FD/investment
   maturities, other financial-asset movements) sits outside this
   narrower narrative breakdown.
3. **Investor Presentation basis (Q4FY26, p.17):** "IP Investment —
   Organic" Rs 601 Mn (= Rs 124.62 Mn + Rs 476.38 Mn exactly, confirming
   this sub-total) + "IP — Acquisitive" Rs 762 Mn ("includes IP held in
   Cryptas books and product bolt-on acquisitions") = **Rs 1,363 Mn**
   combined IP investment, a third total that does not match either of
   the above.

**Settled figure used downstream (named field in the YAML block below):**
capex (PPE + intangible assets purchased) FY26 = **Rs 1,853.68 Mn**;
acquisition payment FY26 = **Rs 629.03 Mn**; combined = **Rs 2,482.71 Mn**,
all AR p.218/p.155 (mupdf), matching B01 (corrected) and B03. The MD&A
prose and Investor Presentation breakdowns are shown above as
supplementary context, not substitutes; B04 already flagged this
reconciliation gap and it is not resolved in this stage either — carried
as an input_gap.

### 2B. Utilisation trajectory per facility

NOT FOUND. eMudhra does not disclose server counts, transaction capacity,
or utilisation percentages for any data centre (India, US, Europe, or the
UAE build). This is consistent with the business being asset-light
(B04: asset_intensity "light"); "capacity" in this business is closer to
licence/contract capacity (customer count, transaction volume) than
physical throughput, and none of those are disclosed at a facility level
either.

### 2C. Growth embedded in capex — arithmetic corrected (Verifier C, MAJOR finding 4)

**Correction applied 2026-09-19.** The original reading applied a
PP&E-only fixed asset turnover (5.43x, excludes goodwill/intangibles) to a
numerator that included intangible assets under development — a basis
mismatch. Corrected below using the run's own consistent fixed-asset-
turnover convention, and the basis choice is shown as an open range rather
than collapsed into one number.

Run-consistent fixed asset turnover (B01-gate0 M3, screener-data Net Block
basis — Net Block includes PP&E + CWIP + goodwill + intangibles, the same
wide basis used elsewhere in this run): Revenue FY26 Rs 701.58 Cr ÷ Net
Block Rs 726.86 Cr = **0.97x** (outputs/reports/01-gate0.md, M3 Capital
Efficiency).

"Capex under execution" (unchanged from the original reading): CWIP
Rs 185.84 Mn (UAE DC) + intangible assets under development Rs 105.92 Mn
(consol) = **Rs 291.76 Mn** (AR p.216, Note 3b/5b).

Implied incremental revenue, run-consistent basis = Rs 291.76 Mn × 0.97x =
**Rs 283.1 Mn**, or **4.0%** of FY26 revenue (Rs 7,015.80 Mn). **This is
the settled figure carried to the YAML block below.**

The basis choice is genuinely open, so the range is named explicitly
rather than hidden behind one number:

| Reading | Numerator | Turnover multiplier | Multiplier basis | Implied revenue | % of FY26 revenue |
| --- | --- | --- | --- | --- | --- |
| **Run-consistent (settled)** | Rs 291.76 Mn (CWIP + intangibles under development) | 0.97x | Screener Net Block (PP&E + CWIP + goodwill + intangibles), same convention as B01 M3 | Rs 283.1 Mn | **4.0%** |
| PP&E-only numerator, PP&E-only turnover | Rs 185.84 Mn (UAE DC CWIP only, excludes intangibles) | 5.43x | Net PP&E only (AR p.216 Balance Sheet) | Rs 1,009.1 Mn | 14.4% |
| Original reading (superseded, basis-mismatched) | Rs 291.76 Mn (CWIP + intangibles under development) | 5.43x | Net PP&E only, applied against a numerator that includes non-PP&E intangibles | Rs 1,584.3 Mn | 22.6% (do not use) |

Applicability caveat (🔍 analyst note, not a company claim, unchanged in
substance): this methodology is built for capacity-constrained
manufacturing, where fixed asset turnover causally links a plant addition
to throughput. eMudhra is a licence/subscription software and
trust-services business; its fixed-asset base is overwhelmingly office and
data-centre infrastructure plus acquisition goodwill/intangibles, not a
revenue-generating capacity constraint in the manufacturing sense. Even on
the corrected, run-consistent 4.0% reading, this should be read as a
weak/low-confidence proxy, not a forecast. Applying the SAME
run-consistent 0.97x multiplier to the FULL FY26 capex figure (Rs 1,853.68
Mn, not just the under-execution slice) would imply Rs 1,798.1 Mn of
incremental revenue, 25.6% of FY26 revenue — still a large single-year
jump, and a reminder that most of FY26's capex was already spent/
commissioned this year, not "under execution." The framework transfers
poorly to an asset-light, acquisition-and-R&D-driven business model under
any of the three readings above.

### 2D. New geography or market entries

- Almaty, Kazakhstan office — 📄 Reg 30 press release 20-Feb-2026
  (inputs/announcements/20260220-6892c79f), "eMudhra Expands into Central
  Asia with Almaty Office."
- UAE QTSP licence / in-country data centre — 🎙️/📄, pending, targeted
  ~Sep-Oct 2026 (Q1 FY27 call; B05).
- Sri Lanka (LankaPay partnership) — 📄 Reg 30 press release 12-Feb-2026
  (inputs/announcements/20260212-944815c1), national digital-signature
  enablement with LankaPay (Sri Lanka's national payment network
  operator).
- East Africa (national PKI/emCA deployment, unnamed national regulatory
  authority) — 📄 AR case study, p.24-25: "one of East Africa's first
  nations to operate an internationally-interoperable, domestically-governed
  national CA infrastructure." (Note: this describes the CUSTOMER nation's
  status, not a documented claim about eMudhra's standing versus peers —
  see the E1 correction in Section 3.)
- International footprint at year-end: 35+ countries, 16 mapped
  international office locations plus 5 India offices (AR p.9); this is
  existing scale, carried here for context, not itself new-this-year
  evidence.

---

## SECTION 3: THE 22-CATEGORY SCAN

Evidence allocation note: several items (e.g., LankaPay, MOSIP, GLEIF)
touch both a geography and a partnership. Each item below is assigned to
ONE category only (its primary mechanism) to avoid crediting the same
underlying fact through two mechanisms (house rule). The allocation is
stated explicitly so a reader can check it.

### FAMILY A — Product & Technology

**A1 rare manufacturing capability.** NO EVIDENCE FOUND. Not applicable —
eMudhra is a software/licensed-services business, not a manufacturer.

**A2 patent and IP pipeline.** NO EVIDENCE FOUND. The AR's only "patent"
reference is a compliance list entry ("The Patents Act, 1970," p. of
applicable-laws list); no patent filing, filing trend, or licensing
revenue is disclosed anywhere in the corpus searched. eMudhra's IP moat
runs through regulatory licence (CCA) and accreditation (WebTrust), not
patents.

**A3 process innovation.** NO EVIDENCE FOUND against the category's own
test (yield disclosures, unit cost declining with quality rising,
automation, waste-to-value). CMMI Maturity Level 5 appraisal is disclosed
(📄 AR p.36-39) but this is a process-quality certification, not a
disclosed yield or unit-cost trend; not force-fit into this category.

**A4 product platform / modular architecture. MODERATE.** Four new
product-pillar items launched or introduced within FY2025-26, each
described as extending — not replacing — a shared architecture ("six
product pillars," "one architecturally coherent platform," AR p.10-14):
ID Broker (📄 AR p.21-22), Data Discovery/Privacy platform (📄 AR p.28-29),
Agentic AI Security Platform (📄 AR p.20/33-34, dated Feb-2026), emSigner
for SMEs (📄 AR p.16, Reg 30 17-Apr-2026). R&D headcount is disclosed
(200+, AR p.148) but not shown historically, so "SKU growth without
proportional R&D increase" cannot be verified either way. Time to
materialise: near (already launched, revenue contribution not yet
disclosed).

### FAMILY B — Supply Chain

**B1 backward integration and RM security.** NO EVIDENCE FOUND. Not
applicable to a software/licensed-services model.

**B2 qualification lock-in. MODERATE.** CertiNext case study: a Middle
East commercial bank brought 60,000+ certificates under a single governed
CertiNext inventory with 24-hour escalation SLAs (📄 AR p.27). Once an
enterprise of this scale automates its certificate estate on CertiNext,
switching cost rises with the certificate count and the automation
workflows built around it — a genuine, if company-specific, lock-in
mechanism. (The regulatory driver behind this dynamic — the CA/Browser
Forum's certificate-validity compression schedule — is scored once, under
R1 below, not duplicated here.) Time to materialise: near-medium (the
case study is a "results" claim, not yet a renewal-cycle data point).

**B3 supply chain network effect.** NO EVIDENCE FOUND. The CA-partner
channel (~70% of DSC volume per B04) is an existing distribution
relationship, not a two-sided marketplace connecting fragmented supply and
demand; no new evidence of a network-effect structure this year.

### FAMILY C — Customer

**C1 customer ecosystem / embedded relationships. MODERATE.** SecurePass
case study: a state government deployed SecurePass as a unified SSO fabric
across Treasury, Excise, Transport, Education and Health departments,
serving 60 million+ citizens (📄 AR p.22-23). Separately, two named
cross-sell wins were disclosed on the Q1 FY27 call using the Cryptas
relationship: a large German data-centre customer bought eMudhra's
CertiNext (not a third-party product) through the Cryptas channel, and an
Austrian city municipality bought emSigner integrated with PrimeSign Trust
Services (🎙️, Q1 FY27 call, lines 116-118 and 960-962). This is the
concrete first evidence behind B05's Priority-2 trigger ("Cryptas
cross-sell converts to profitability"), still early (2 named wins).

**C2 customer concentration improving. MODERATE.** 240 new enterprise
customers added in FY26 (📄 MD&A p.151); Enterprise Solutions customer
count 1,374 (Q4FY26 Inv. Pres. p.19). No top-5/10 concentration trend is
disclosed (B05 already flagged this silence across all three concalls),
so the category's core test — concentration DECLINING — cannot be
confirmed, only the customer-addition input to it.

### FAMILY D — Data & Digital

**D1 proprietary data asset.** WEAK / NO EVIDENCE FOUND against the
category's own test. Cumulative signature volume on emSigner crossed 200
million transactions (📄 AR p.12), a genuine scale figure, but there is no
disclosed claim that eMudhra trains a machine-learning model on this
signature/identity data, nor any replicability discussion. "AI-driven
certificate automation" is referenced generically (AR p.10) without
specifying a proprietary-data-trained model. Not scored, to avoid
force-fitting a volume metric into a data-asset category.

**D2 digital platform.** WEAK / NO EVIDENCE FOUND against the category's
own test. Scale exists (emSigner 200M+ signatures; SecurePass 60M+
citizens in one deployment) but participant growth, take rate, digital
revenue %, and platform-specific lock-in economics are not disclosed at
the platform level (only at the case-study level). Not scored.

### FAMILY E — Geographic & Access

**E1 geographic first-mover. MODERATE (corrected, Verifier C, MAJOR finding
3).** Three distinct 📄 items within FY2025-26 to FY2026-27: Almaty
(Kazakhstan) office opened (📄 Reg 30, 20-Feb-2026); East Africa National
PKI deployment, explicitly framed as a national first for the CUSTOMER
nation ("one of East Africa's first nations...", 📄 AR p.24-25); UAE
in-country data-centre build for QTSP compliance, CWIP Rs 185.84 Mn
already committed (📄 AR p.150/Note 3b), though the licence itself is
still pending. **Correction:** the original write-up additionally claimed
this positions eMudhra "ahead of most listed Indian identity/security
peers," a comparative claim with no source; removed. The three events
themselves are 📄 documented, but the category's defining attribute — a
first-mover ADVANTAGE over peers, specifically — is not itself evidenced;
the East Africa case study describes the customer nation's status, not
eMudhra's standing against competitors, and one of the three legs (UAE) is
a pending licence, not a completed entry. Rescored accordingly (Section 5).
Time to materialise: near (Almaty and East Africa are live; UAE is
near-term per the guided timeline, already once-slipped).

**E2 China+1 beneficiary.** NO EVIDENCE FOUND. Not applicable — this
category maps to manufacturing supply-chain diversification away from
China; eMudhra's business (digital trust/identity software) has no
China-exposure dynamic disclosed anywhere in the corpus.

### FAMILY F — Talent & Organisational

**F1 talent density.** WEAK / NO EVIDENCE FOUND against the completionist
guard. R&D team "of over 200+ people" is disclosed (📄 AR p.148) and a new
2025 ESOP/RSU scheme was adopted (📄 AR p.90-91, ~2.90% of paid-up capital)
but there is no PhD/specialist count, no historical headcount trend, and
no named senior-technical-hire detail beyond the standing EVP/MD
leadership quotes already counted elsewhere. A headcount count alone is a
hiring story, not density evidence; not scored, consistent with the I1
standard applied one level down.

**F2 execution moat.** WEAK / MIXED, cross-referenced against the injected
B05 promise-delivery record: 4 delivered, 2 partial, 2 missed, credibility
grade B. The two misses are directly relevant to this category: the UAE
data-centre/QTSP timeline slipped from an implied ~Apr-Jun 2026 to
~Sep-Oct 2026 with a silent Q4 FY26 call in between, and the stock-in-trade
cost drag (~Rs 3 Cr/quarter) was never revisited or confirmed resolved.
Revenue guidance and EBITDA-margin promises were delivered or beaten
(B05). On balance this is a mixed record, not a scoreable execution moat;
not scored.

### FAMILY G — Financial & Structural

**G1 war chest.** NO EVIDENCE FOUND — and the opposite signal is present
this year. Cash and cash equivalents FELL from Rs 1,885.54 Mn to
Rs 1,268.48 Mn (📄 AR p.153-154), and FY26 FCF turned negative (-Rs 52.52
Cr, AR p.218/B01 corrected). The company remains net-cash with near-zero
leverage (D/E 0.03x, B03), but "net cash growing while investing" is not
this year's pattern; not scored.

**G2 WC improvement trajectory.** NO EVIDENCE FOUND — again the opposite
signal. Trade payables +91% YoY and unbilled revenue +40.6% YoY, both
ahead of 35.1% revenue growth (📄 Note 18/8/42/48, B02 Pattern A); not
scored.

### FAMILY H — Ecosystem & External

**H1 industry consolidation beneficiary. MODERATE.** eMudhra is the
consolidator here, not simply a beneficiary of competitor exits: two
completed bolt-on acquisitions this year, Cryptas International GmbH
(Europe, PKI/digital trust, 📄 AR Note 4a(c)) and AI Cyberforge Inc. (US,
key/secrets management, 📄 Reg 30 merger completion 02-Feb-2026), both
consolidating fragmented identity/PKI capability under one platform. The
category's own definition names "bolt-on acquisitions" as qualifying
evidence. Integration is early (goodwill nearly tripled with no disclosed
impairment-test assumptions, B02 finding 3); scored Moderate, not Strong,
on that basis.

**H2 strategic partnerships. STRONG.** Three named, dated 📄 items within
the run window: LankaPay partnership for Sri Lanka national digital
signatures (📄 Reg 30, 12-Feb-2026); GLEIF/LEIL appointment of eMudhra as
a Validation Agent in the Global LEI System, one of "over 20 Validation
Agents globally" (📄 Reg 30, 13-Sep-2026); MOSIP certification enabling
population-scale DPI deployments across Africa (📄 Reg 30, 16-Feb-2026).
None has a disclosed revenue figure yet; all are early-stage partnership
mechanisms, carried to the Optionality Register for the revenue-conversion
leg.

**H3 ESG moat.** NO EVIDENCE FOUND against the category's own test
(renewables %, improving ratings trend, customer ESG mandates, SBTi, ZLD).
Three UNSOLICITED third-party ESG scores were disclosed this year — CFC
Finlease 76 (📄 Reg 30, 26-Feb-2026), Crisil ESG 60 (📄 Reg 30, 29-Jun-2026),
SES ESG 68.0 (📄 Reg 30, 06-Jul-2026) — none engaged by the company, no
trend shown (single-year scores only), and the BRSR Essential Indicator
for R&D/capex directed at environmental-social impact is answered "NA"
(AR p.169). Not scored.

### FAMILY I — Structural Asymmetries (20-Aug-2026)

**I1 talent asymmetry. Score 0**, per the operator ruling's own test.
Part (a) evidence found: R&D headcount 200+ (📄 AR p.148), general
technical-hiring/retention language (AR p.36-41 Great Place to Work). Part
(a) evidence NOT found: no named inventors traceable to patent filings (A2
above found none), no ex-DRDO/ex-HAL/ex-global-major concentration
verifiable, no remuneration-annexure comparison showing technical hires
paid above sector norms. Part (b) evidence (competitor-economics leg): NOT
FOUND — no PSU pay-scale ceiling comparison, no documented failed-poaching
or attrition commentary in a competitor's own concall. This is a hiring
story ("200+ R&D people," "Great Place to Work"), which the framework
explicitly scores 0.

**I2 cannibalization barrier. Score 0.** Working through each moat claimed
above: for the India CCA-licensed retail DSC business (Rs 1,000 emSigner
SME pricing), a global competitor (DigiCert, Entrust) entering at Indian
retail price points would have to accept a materially lower-margin
delivery model than its home-market pricing — a plausible configuration
barrier — but no 📄 source (a competitor's own filing, pricing disclosure,
or org structure) was found in this corpus to support the implausibility
at the top-band standard the category requires. For the CertiNext
lock-in (B2) and the East Africa/Almaty geographic entries (E1), the
honest answer to "what would the best-resourced competitor have to
destroy in its own P&L or org to copy this" is closer to "nothing
structural — it would have to execute faster," which the framework
explicitly classifies as execution lead, not configuration, and scores 0.

---

### Section 3 summary table (all 22 rows + R1)

| # | Category | Evidence? | Type | Strength | Time to materialise |
| --- | --- | --- | --- | --- | --- |
| A1 | Rare manufacturing capability | No | — | None | — |
| A2 | Patent and IP pipeline | No | — | None | — |
| A3 | Process innovation | No | — | None | — |
| A4 | Product platform / modular architecture | Yes | 📄 | Moderate | Near |
| B1 | Backward integration / RM security | No | — | None | — |
| B2 | Qualification lock-in | Yes | 📄 | Moderate | Near-medium |
| B3 | Supply chain network effect | No | — | None | — |
| C1 | Customer ecosystem / embedded relationships | Yes | 📄 + 🎙️ | Moderate | Near |
| C2 | Customer concentration improving | Yes | 📄 (addition only) | Moderate | Near |
| D1 | Proprietary data asset | Weak | — | Weak | — |
| D2 | Digital platform | Weak | — | Weak | — |
| E1 | Geographic first-mover | Yes | 📄 | Moderate (corrected, Verifier C; was Strong) | Near |
| E2 | China+1 beneficiary | No | — | None (not applicable) | — |
| F1 | Talent density | Weak | — | Weak | — |
| F2 | Execution moat | Weak/Mixed | — | Weak | — |
| G1 | War chest | No (negative this year) | — | None | — |
| G2 | WC improvement trajectory | No (negative this year) | — | None | — |
| H1 | Industry consolidation beneficiary | Yes | 📄 | Moderate | Near-medium |
| H2 | Strategic partnerships | Yes | 📄 | Strong | Near |
| H3 | ESG moat | No | — | None | — |
| I1 | Talent asymmetry | No (score 0 by design) | — | None | — |
| I2 | Cannibalization barrier | No (score 0 by design) | — | None | — |
| R1 | Regulatory & policy tailwinds | Yes | 📄 | Strong | Near-medium (see Section 4) |

**Count with Strong/Moderate evidence: 8 of 23 rows** (A4, B2, C1, C2, E1,
H1, H2, R1).

**Completionist guard check.** 📄 recount performed: 19 documented items
across 8 categories (A4: 4 — ID Broker, Data Discovery/PrivaTrust, Agentic
AI Security Platform, emSigner for SMEs; B2: 1 — CertiNext 60,000-cert
case study; C1: 1 — SecurePass state-government case study (the 2 Cryptas
cross-sell items are 🎙️, not counted here); C2: 1 — 240 new enterprise
customers; E1: 3 — Almaty office, East Africa NPKI, UAE DC CWIP; H1: 2 —
Cryptas acquisition, AI Cyberforge merger; H2: 3 — LankaPay, GLEIF/LEIL,
MOSIP; R1: 4 — CA/Browser Forum schedule, DPDP phased enforcement, RBI LEI
master direction, eIDAS 2.0/EUDI Wallet mandate). 8 active categories is
above the stated 3-6 base rate; this is explainable, not a red flag on
inspection: FY2025-26 was an unusually announcement-dense year for
eMudhra (2 completed bolt-on acquisitions, 4 new product pillars launched
within 12 months, and a cluster of dated regulatory deadlines landing in
the same window). Each of the 8 active rows rests on a dated, named 📄
item, not a reworded 🎙️ claim; none of the **15** (23 - 8) None/Weak rows
were force-fit upward to make the count look complete (corrected,
Verifier C — was misstated as 14), per rule 5 and the explicit "NO
EVIDENCE FOUND" calls above for A1, A2, A3, B1, B3, E2, G1, G2, H3, I1,
I2. E1's item count and evidence tier are unchanged by the Verifier C
correction above; only its likelihood×impact read (and therefore its
raw score) changed, since the underlying events remain 📄.

---

## SECTION 4: REGULATORY & POLICY TAILWINDS (Category R1)

### 4A. Regulatory approvals in pipeline

| Body | Status | Timeline | What it unlocks | Which competitors have it |
| --- | --- | --- | --- | --- |
| UAE regulator (QTSP licence) | Application in final stage (🎙️, Q1 FY27 call, Arvind Srinivasan: "we're essentially the final step of the process... towards the end of this quarter to beginning of next quarter") | ~Sep-Oct 2026 | UAE in-country Trust Services (Aadhaar-eSign equivalent, complements emSigner for UAE banks) | NOT FOUND (no named competitor UAE QTSP status in the corpus) |
| GLEIF/LEIL Validation Agent accreditation | Granted | 10-Sep-2026 (📄 Reg 30 13-Sep-2026) | LEI application/renewal embedded in eMudhra's identity-verification onboarding | "Over 20 Validation Agents globally" exist (📄 press release); named Indian competitors NOT FOUND |

### 4B. Government policy tailwinds

| Policy | Amount/duration | Enrolment status | Competitors share the benefit? | Source |
| --- | --- | --- | --- | --- |
| CA/Browser Forum SSL/TLS certificate-validity compression: 398→200 days (now, from 15-Mar-2026), →100 days (15-Mar-2027), →47 days (15-Mar-2029); domain-validation reuse compresses in step | Industry-wide mandate, no monetary amount | In force (200-day phase active) | Yes — DigiCert, Entrust, Sectigo, Venafi, Keyfactor, AppViewX all address this; not eMudhra-exclusive | 📄 AR p.25-27 |
| India DPDP Act phased enforcement: Phase 1 (Rules notified 13-Nov-2025), Phase 2 (Consent Manager registration + Significant Data Fiduciary obligations, 13-Nov-2026), Phase 3 (full compliance, 13-May-2027) | Statutory, no monetary amount | Phase 1 active | Yes — shared with any Indian privacy/GRC vendor (e.g., generic GRC tools); eMudhra's differentiator is bundling consent with its existing identity/signing stack | 📄 AR p.29 |
| EU eIDAS 2.0 / EUDI Wallet mandatory deployment (31-Dec-2026); NIS2 and DORA operational-resilience reporting | Statutory, no monetary amount | In force / approaching | Yes — shared with all EU-serving identity/PKI vendors; Cryptas/PrimeSign gives eMudhra an EU delivery foothold | 📄 AR p.21-22, Q4FY26 Inv. Pres. p.19/23 |
| India RBI master direction on Legal Entity Identifiers (Mar-2026), consolidating LEI requirements for specified financial-market transactions | Statutory, no monetary amount | In force | Yes in principle (any accredited Validation Agent), but eMudhra is a named first-mover appointee | 📄 GLEIF press release, 13-Sep-2026 |
| NIST PQC standards (FIPS 203/204/205) and CNSA 2.0 (US NSA mandate, 2025-2033 phased deadlines) | Statutory/standards-body mandate, no monetary amount | Standards finalised, migration windows open | Yes — global, shared by every PKI/identity vendor; eMudhra's edge is claimed early/comprehensive implementation (advisory practice launched Feb-2026), not exclusivity | 📄 AR p.28-32 |

### 4C. Regulatory moat assessment

Active vs emerging: the CA/Browser Forum schedule and DPDP phases are
already active (not purely emerging), but their FULL bite (47-day
certificates, DPDP Phase 3) lands 2027-2029 — squarely in this scan's
1-5 year window, which is why they are carried here rather than in a
backward Gate 0 read. Time to kick in: near (Phase 2 DPDP, Nov-2026) to
long (47-day TLS certificates, Mar-2029). Sustainability: these are
statutory/standards-body deadlines, not eMudhra-specific concessions, so
they are durable but NOT exclusive — every named competitor in the AR's
own competition table (DigiCert, Entrust, Sectigo, GlobalSign, Venafi,
Keyfactor, AppViewX) faces the identical compliance clock. eMudhra's
argument is a one-stop-shop platform position (AR p.10-11) plus
lower-cost Bangalore delivery (AR p.158, existing moat per B04), not
regulatory exclusivity.

**Correction (Verifier C, MINOR finding 9):** the previous text here said
this observation "tempers R1's score" while the scorecard kept R1 at the
maximum HH=4, an internal inconsistency. Corrected framing: R1's own
likelihood×impact read stays HH — the tailwinds themselves are High
likelihood (already active, dated, statutory) and High impact (span
multiple products and geographies), which is what this category scores.
Whether eMudhra specifically OUTCOMPETES named rivals in capturing that
shared tailwind is a separate question, addressed in Section 6B's risk
discussion and left for Role 2/FTTCP, not folded into this category's
score.

---

## SECTION 5: EMERGING MOAT SCORECARD

Scoring: raw score = likelihood × impact (HH=4, HM/MH=3, HL/MM/LH=2,
ML/LM=1, LL=1, no evidence=0), then × evidence-quality multiplier
(📄 1.0x, 🎙️ 0.7x, 🔍 0.5x).

**Correction (Verifier C, MAJOR finding 3):** the E1 row below is
rescored from HH/4/4.0 to MH/3/3.0. All other rows unchanged from the
original scan; only the total changes as a result.

| # | Category | Likelihood×Impact | Raw | Evidence tier | Multiplier | Adjusted score |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | Rare manufacturing capability | — | 0 | — | — | 0 |
| A2 | Patent and IP pipeline | — | 0 | — | — | 0 |
| A3 | Process innovation | — | 0 | — | — | 0 |
| A4 | Product platform / modular architecture | MH | 3 | 📄 | 1.0x | 3.0 |
| B1 | Backward integration / RM security | — | 0 | — | — | 0 |
| B2 | Qualification lock-in | MM | 2 | 📄 | 1.0x | 2.0 |
| B3 | Supply chain network effect | — | 0 | — | — | 0 |
| C1 | Customer ecosystem / embedded relationships | MH | 3 | 🎙️ (dominant tier for the forward/cross-sell piece) | 0.7x | 2.1 |
| C2 | Customer concentration improving | HL | 2 | 📄 | 1.0x | 2.0 |
| D1 | Proprietary data asset | — | 0 | — | — | 0 |
| D2 | Digital platform | — | 0 | — | — | 0 |
| E1 | Geographic first-mover | **MH (corrected, was HH)** | **3** | 📄 | 1.0x | **3.0 (corrected, was 4.0)** |
| E2 | China+1 beneficiary | — | 0 | — | — | 0 |
| F1 | Talent density | — | 0 | — | — | 0 |
| F2 | Execution moat | — | 0 | — | — | 0 |
| G1 | War chest | — | 0 | — | — | 0 |
| G2 | WC improvement trajectory | — | 0 | — | — | 0 |
| H1 | Industry consolidation beneficiary | MH | 3 | 📄 | 1.0x | 3.0 |
| H2 | Strategic partnerships | HM | 3 | 📄 | 1.0x | 3.0 |
| H3 | ESG moat | — | 0 | — | — | 0 |
| I1 | Talent asymmetry | — | 0 | — | — | 0 |
| I2 | Cannibalization barrier | — | 0 | — | — | 0 |
| R1 | Regulatory & policy tailwinds | HH | 4 | 📄 | 1.0x | 4.0 |
| **Total** | | | | | | **22.1 (corrected, was 23.1)** |

**I1/I2 contribution: 0.0** (both score 0 by design per the 20-Aug-2026
ruling; neither crosses a threshold here, so the REVIEW CHECKPOINT list
does not gain an entry from this run).

**em_score = 22.1 / 92 (corrected, Verifier C; was 23.1).**

**Classification: 12-24 → MODEST MOAT DEVELOPMENT (unchanged).** Bands are
absolute per the 20-Aug-2026 operator ruling (no rescale). The correction
moves eMudhra from 23.1 to 22.1, still comfortably mid-band and still
below the EM ≥25 UA qualifier either way. eMudhra sits mid-band: genuine,
dated, 📄-documented forward activity (new products, bolt-on acquisitions,
geographic entries, partnerships, a favourable regulatory calendar)
exists across 8 of 23 categories, but the two Financial & Structural rows
(G1, G2) are NEGATIVE this year (cash fell, FCF turned negative, WC
deteriorated), Talent (F1) and Execution (F2) evidence is thin-to-mixed,
and neither Family-I structural-asymmetry row clears its evidentiary bar.
This is a real but early-stage build, not an expansion already underway.

---

## OPTIONALITY REGISTER

Forward advantages that scored 0 or rest only on 🎙️/🔍 evidence. Watched,
never scored.

| Optionality (one line) | Converting 📄 evidence | Where it first appears | Conversion window |
| --- | --- | --- | --- |
| UAE QTSP licence and in-country Trust Services launch | Licence grant notice + first UAE eSign/QTSP transaction disclosed | Reg 30 filing / concall | ~Sep-Oct 2026 (already once-slipped, B05) |
| Cryptas cross-sell scaling beyond the 2 named FY27 wins | Named revenue contribution from cross-sold CertiNext/emSigner deals in the FY27 AR segment note or a Reg 30 order-win filing | FY27 AR Note 49 / Reg 30 filings | FY27-FY28 |
| I1 talent asymmetry (currently unevidenced) | Named inventor with traceable patent + ex-major-vendor concentration evidence + PSU/competitor pay-scale comparison | AR remuneration annexure / Espacenet-ipindia.gov.in / competitor concall | Not scheduled; operator-driven verification |
| I2 cannibalization barrier (currently unevidenced) | A competitor's own filing or pricing disclosure showing the specific sacrifice required to match eMudhra's India cost structure | Competitor (DigiCert/Entrust) 10-K or pricing disclosure | Not scheduled; operator-driven verification |
| Agentic AI Security Platform revenue | First paid, named agentic-AI-linked deal (B05 trigger 7, currently conviction L) | Reg 30 filing / concall | FY28, "early stage" per management |
| PrivaTrust (Data Discovery/Consent Platform) customer win | First named customer win (B05 trigger 8) | Reg 30 filing / concall | By Q3 FY27 call (B05 kill signal if absent) |
| SecurePass/IAM international expansion beyond India | First named international SecurePass deal (B05 trigger 6) | Reg 30 filing / concall | FY27 |
| Bolt-on AI-cybersecurity acquisition (dropped trigger, B05) | Signed acquisition agreement / Reg 30 filing | Reg 30 filing | Live in Q3 FY26 commentary, absent by Q1 FY27; unresolved |
| R&D intensity vs the company's own 15-20% global-peer benchmark (currently 7-8% estimated) | A disclosed multi-year R&D-to-revenue trend showing convergence toward the peer band | FY27/28 AR MD&A or BRSR | Not scheduled |
| FY27 free cash flow returning positive (G1/G2 reversal) | FY27 audited cash flow statement showing CFO > capex + acquisition spend | FY27 AR / quarterly results | FY27 year-end |
| eMudhra's own first-mover advantage over listed Indian peers in Central Asia/East Africa (E1 leg removed this correction) | A sourced peer-footprint comparison (e.g., a named competitor's absence from these markets) | Analyst/verifier cross-check, not disclosed by eMudhra itself | Not scheduled; operator-driven verification |

---

## SECTION 6: TIMELINE, RISKS & COMBINED ASSESSMENT

### 6A. Moat evolution timeline

- **Next 12 months (to Sep-2027... reading as "next 12m" from run date):**
  UAE QTSP licence grant and DC commissioning (targeted ~Sep-Oct 2026,
  already once-slipped — the key milestone to watch); DPDP Phase 2
  (Consent Manager registration, Significant Data Fiduciary obligations)
  effective 13-Nov-2026, first real test of PrivaTrust demand; Cryptas
  cross-sell scaling beyond the 2 named wins; EUDI Wallet mandatory
  deployment (31-Dec-2026) testing ID Broker's EU relevance.
- **12-24 months:** CA/Browser Forum certificate validity drops to 100
  days (15-Mar-2027), the next hard automation deadline for CertiNext;
  DPDP Phase 3 full compliance (13-May-2027); resolution (or not) of the
  dropped bolt-on-AI-cybersecurity-acquisition trigger (B05).
- **24-36 months:** Continued CertiNext-driven enterprise adoption ahead
  of the 2029 47-day deadline; Cryptas 2028-2030 49% put/call option
  window begins to approach, tying the earn-out mechanic (Rs 881.45 Mn,
  uncapped upside, B02) directly to whatever cross-sell/EBITDA trajectory
  Cryptas has produced by then.
- **3-5 years:** CA/Browser Forum 47-day certificate validity becomes
  mandatory (15-Mar-2029), the terminal automation forcing-function for
  the whole industry; Agentic AI identity maturing (per management) from
  "early stage, hard to quantify" (B05) toward a named paid product line,
  if it gets there.

### 6B. Risks to each top-scoring emerging moat

| Top-scoring moat | Risk | Early warning sign |
| --- | --- | --- |
| E1 Geographic first-mover | UAE QTSP has already slipped once (Apr-Jun 2026 implied → Sep-Oct 2026, with a silent intervening call, B05); the "first-mover" framing itself rests on documented EVENTS but not a documented peer-lead claim (corrected this pass) | Further slippage past Q3 FY27 without a firm new date (B05's own kill signal); or a named peer matching/pre-empting one of the three geographic entries |
| H2 Strategic partnerships | LankaPay, GLEIF/LEIL, and MOSIP are all early-stage, unquantified in revenue terms | No disclosed revenue contribution from any of the three within 12 months |
| R1 Regulatory tailwinds | Shared industry-wide (DigiCert, Entrust, Venafi, Protean, Newgen all face the same PQC/DPDP/eIDAS clocks); eMudhra's edge is execution speed and one-stop-shop breadth, not exclusivity | A named competitor announces an equivalent automation/PQC capability and converts a paid deal before eMudhra does |
| A4/C1 New products and cross-sell | Cryptas cross-sell (2 named wins) is running against a Rs 881.45 Mn UNCAPPED contingent-consideration liability tied to Cryptas EBITDA (Note 17a, B02); if cross-sell stalls, both the platform thesis and the earn-out economics are exposed together | Cryptas FY27 full-year PAT stays near breakeven (B05 Priority-2 kill signal) with no further named cross-sell wins |

### 6C. Combined Gate 0 + Emerging Moat table

| Block | Value | Source |
| --- | --- | --- |
| Gate 0 core score | 71 | B01-gate0 (as filed; under separate REWORK per Verifier C Part 1 — see note below) |
| Gate 0 existing moat count / class | 4 moats confirmed, STRONG | B01-gate0 (as filed) |
| Gate 0 grand total | 88 | B01-gate0 (as filed) |
| Gate 0 classification | GOOD (capped — Block B <8, deal-breaker) | B01-gate0 (as filed) |
| Emerging Moat score | **22.1 / 92 (corrected, Verifier C; was 23.1)** | This stage |
| Emerging Moat classification | MODEST MOAT DEVELOPMENT | This stage |

**Note on B01 status:** Verifier C's Part 1 (Gate 0) found a CRITICAL
rule-misapplication in B01's Block B/M12 (a false "data unextractable"
premise on consolidated payables that, once corrected, flips the
classification to GOOD+ under the stage's own n=2-window convention). That
finding is routed to Stage 1 REWORK and is NOT corrected in this pass —
this stage's scope is B07 only. The 71/88/GOOD figures above are the
current B01-as-filed values; 6C and 6D should be re-read once B01 is
reworked.

### 6D. Combined classification

**Combined assessment: GOOD** (backward GOOD as filed, forward MODEST —
read together below; provisional pending the B01 REWORK noted in 6C).

Reasoning: the instruction names a fixed 8-tier combined label set
(EXCEPTIONAL / EXCELLENT+ / HIGH POTENTIAL / GOOD+ / GOOD / TURNAROUND /
AVERAGE / AVOID) but the literal backward×forward lookup table was not
found in the corpus available to this stage (frameworks/ and prompts/
were both searched; only the Gate 0 stage's OWN backward-only matrix
[Core score × moat class → EXCELLENT/GOOD+/GOOD/AVERAGE/AVOID] was
located, in prompts/01-gate-0-pipeline.md). Verifier C's own Part 2 review
(rule E20) independently confirms this gap was searched for and not
found, and did not fail the stage on it. This is carried as an input_gap
below, not silently resolved. Applied from first principles per the
instruction's own stated logic — "GOOD or AVERAGE backward scores with
EXPANSION forward scores are exactly the transition setups this operation
hunts" — eMudhra's backward score (GOOD) qualifies as a transition-eligible
base, but the forward score is MODEST, not EXPANSION. This is explicitly
NOT the flagship HIGH POTENTIAL / TURNAROUND setup the strategy hunts:
HIGH POTENTIAL and TURNAROUND rows are reserved (per the instruction) for
cases pairing a modest/weak backward score with an EXPANSION-tier forward
score, or a strong backward score compounding with one; neither applies
here. With backward GOOD and forward MODEST (neither STRENGTHENING nor
EXPANSION), the combined read stays at the backward tier, unchanged by the
forward scan: **GOOD**. Stage 9/13 should verify this against the
authoritative combined matrix if one exists outside this stage's
accessible corpus, AND should re-derive this label once B01's Block B
REWORK resolves (a shift from GOOD to GOOD+ at the backward level would
directly change this line).

### 6E. Final output card

**Moat evolution map (existing → emerging, per family):**

- **Existing (Gate 0, backward):** switching costs (67% existing-customer
  revenue), licensed-CA regulatory moat (CCA + WebTrust, narrow scope),
  Bangalore cost advantage, CA-partner distribution, niche brand (WebTrust
  "only Indian CA," G2/IDC recognition) — all per B04.
- **Emerging (this stage, forward):** Family A → a sixth-and-growing
  product pillar (ID Broker, PrivaTrust, Agentic AI) built on the same
  shared architecture as the existing five (A4). Family B → the existing
  regulatory licence moat gains a forward lock-in leg as enterprises
  automate certificate estates on CertiNext ahead of the 2029 deadline
  (B2). Family C → the existing embedded-relationship moat gains a
  cross-sell leg via the Cryptas acquisition, still early (C1, C2).
  Family E → the existing single-jurisdiction (India) licensed-CA model
  is being replicated abroad (UAE, East Africa, pending), on documented
  events, though not yet on a documented lead over peers (E1, corrected).
  Family H → the existing partner-channel distribution gains three new
  named partnership arrangements (LankaPay, GLEIF/LEIL, MOSIP) that could
  become distribution channels in their own right (H2), alongside
  inorganic consolidation of fragmented identity/PKI vendors (H1).

**Catalysts to watch, next 12 months:** UAE QTSP licence grant (~Sep-Oct
2026, already once-slipped); DPDP Phase 2 (13-Nov-2026) testing PrivaTrust
demand; Cryptas cross-sell scaling past the 2 named wins; EUDI Wallet
mandatory deployment (31-Dec-2026).

**Biggest risk to the emerging moats:** the FY26 cash and working-capital
signals moved the wrong way (FCF -Rs 52.52 Cr, cash down Rs 617.06 Mn, AR
p.153-154) in the same year the emerging-moat product and geography build
accelerated. The forward bet (6 product pillars, 2 acquisitions, 3 new
regulatory jurisdictions) is not yet self-funding from operations at the
pace it is being built, and the largest single forward liability in the
corpus (the Rs 881.45 Mn uncapped Cryptas contingent consideration, B02)
is directly tied to the same cross-sell thesis this scan scores as its
strongest customer-side evidence (C1). If Cryptas cross-sell stalls, the
emerging-moat thesis and the earn-out economics are exposed at the same
time, not independently.

---

## INPUT GAPS (this stage)

- R&D-to-revenue historical trend not disclosed on a comparable
  multi-year basis (carried from B01); the single FY27 "estimated 7-8% of
  revenue, vs 15-20% for global peers" figure (Q4FY26 Inv. Pres. p.24) is
  the only R&D-intensity data point found, and it is a company ESTIMATE,
  not an audited figure.
- Capex reconciliation gap (Section 2A arithmetic) not resolved: three
  different AR/Investor-Presentation classifications of "capex-like"
  spend (Rs 1,853.68 Mn CFS line; Rs 1,915.56 Mn MD&A prose; Rs 1,363 Mn
  Investor Presentation "IP Investment") do not sum to each other;
  carried from B04, not resolved here.
- No patent search was possible beyond full-text keyword search of the
  AR; Espacenet/ipindia.gov.in verification (per the I1 evidence
  hierarchy) is PENDING LIVE VERIFICATION (no live web access in this
  container).
- The literal 8-tier combined backward×forward classification lookup
  table (Section 6D) was not found in frameworks/ or prompts/ accessible
  to this stage; the GOOD label above is derived from first principles
  per the instruction's own stated transition-setup logic, not read off
  an explicit table. Flagged for Stage 9/13 verification; independently
  confirmed absent by Verifier C (Part 2, rule E20).
- Facility-level utilisation/capacity metrics (Section 2B) are NOT FOUND
  for any data centre (India, US, Europe, UAE); consistent with an
  asset-light business model where this disclosure gap may be structural
  rather than a corpus gap.
- Section 1C: FY27E growth for the Services revenue stream and the
  company-wide FY27E total are NOT FOUND (no company guidance exists for
  the Services stream specifically); an earlier draft of this report
  filled this gap with an assumed rate, corrected out per Verifier C
  finding 11.
- B01 (Gate 0) is under a separate CRITICAL REWORK per Verifier C Part 1
  (Block B/M12 WC-days false-premise finding); Section 6C/6D of this
  report currently read the B01-as-filed GOOD classification and will
  need re-reading once that REWORK closes, since the corrected B01 read
  (GOOD+) would change 6D's combined label.

## FLAGS (this stage)

- FLAG-CASH: the emerging-moat forward build (6 product pillars, 2
  completed acquisitions, 3 new regulatory jurisdictions in flight) is
  running in the same year Gate 0 (B01) found FY26 FCF turning negative
  (-Rs 52.52 Cr) and cash falling Rs 617.06 Mn. The forward build is not
  yet self-funded from operations.
- FLAG-LIABILITY (cross-reference B02/B03): the C1 cross-sell evidence
  (Cryptas customer wins) and the single largest unresolved forward
  liability in the corpus (Rs 881.45 Mn uncapped Cryptas contingent
  consideration) are the same underlying bet; a stall in one is a stall
  in the other.
- FLAG-REGULATORY-DEPENDENCY: the E1 geographic first-mover score leans
  partly on the still-pending UAE QTSP licence, which has already slipped
  once (B05). If it slips again past the B05 kill-signal date (Q3 FY27
  without a firm date), the E1 row's evidentiary basis weakens further.
- FLAG-VERIFIER-DEPENDENCY (new this correction): Section 6C/6D of this
  report inherit B01's classification as filed (GOOD). B01 is under a
  separate CRITICAL REWORK (Verifier C Part 1) that could move it to
  GOOD+. If that REWORK closes with GOOD+, Section 6D's combined label in
  this report should be re-read, not assumed unchanged.
