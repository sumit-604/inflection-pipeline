# Stage 9 — TAM / SAM / SOM: eMudhra Ltd (EMUDHRA)

Run date 2026-09-19. All figures Rs Cr unless marked USD. Exchange rate
used to convert USD market-report figures: Rs 84 = USD 1 (implied by the
Two95 acquisition disclosure, AR p.[page 279 marker], "INR 848.01 (USD
10.10 million)" -> Rs 83.96/USD, rounded to Rs 84). This is an
approximation, not a dated spot rate; flagged.

FY26 consolidated revenue from operations: **Rs 701.58 Cr** (INR
7,015.80 Mn, "Income from Operations", FY26 Audited Results, p.8 [text
marker "[page 8]"], year ended 31-Mar-2026; FY25 comparable INR 5,193.85
Mn = Rs 519.39 Cr, YoY growth 35.1%). This is REVENUE_CR / REVENUE_ANCHOR
for this stage.

Segment split (AR Note 49, "Segment Information", p.288-289, consolidated
FY26):
- Trust Services: INR 1,400.08 Mn = **Rs 140.01 Cr** (19.96% of revenue)
- Enterprise Solutions India: INR 1,240.00 Mn = **Rs 124.00 Cr**
- Enterprise Solutions Outside India: INR 4,375.72 Mn = **Rs 437.57 Cr**
- Enterprise Solutions total: **Rs 561.57 Cr** (80.04% of revenue)
- Segment margins: Trust Services 31.4%, Enterprise India 57.5%,
  Enterprise Outside India 21.9% (down from 26.0% FY25) — matches B04.
AR Enterprise Risk section (p.156-157) independently states the same
split rounded: "Trust Services : Enterprise Solutions = 20% : 80%" and
"India : International = 36% : 64%".

---

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

- **Product scope**: (a) Trust Services — licensed Digital Signature
  Certificate (DSC) issuance, eSign, SSL/TLS certificates, under India CCA
  licence and WebTrust accreditation; UAE QTSP licence pending. (b)
  Enterprise Solutions — owned software: PKI / Certificate Lifecycle
  Management (CertiNext/emCA, Cryptas/PrimeSign for EU qualified trust
  services), Identity and Access Management (SecurePass), eSignature
  workflow (emSigner), plus newly launched lines not yet separately
  disclosed in revenue (AI Cyberforge key/secrets management, PrivaTrust
  data consent, agentic-AI security). (c) Services — consulting/
  integration wrapped around (a) and (b); not sold as a standalone
  product (B04 revenue-stream table).
- **Geographic scope**: India (Trust Services core, Enterprise India) plus
  international — North America (US data centres in New Jersey and Salt
  Lake City), Europe/DACH (Cryptas/PrimeSign, Germany data centre),
  Middle East (UAE, Oman deals), Africa (Kenya), APAC (Indonesia,
  Philippines), CIS (Kazakhstan, Almaty office) — per AR p.147-149 and B04.
- **Customer scope**: BFSI, Healthcare & Pharma, Education, Government &
  Public Sector, Manufacturing (AR BRR Q17c, p.[marker near line 7643]),
  plus individual DSC holders via the CA-partner channel.
- **Channel scope**: Trust Services — CA-partner-led distribution ~70%,
  direct-to-consumer ~30% (Q4FY26 Investor Presentation p.8). Enterprise
  Solutions — direct enterprise sales plus partner network (AR p.55).
- **Price segment**: two very different tickets inside one company — DSC
  at Rs 1,500 / 2-year validity, SSL/TLS at USD 6-50/year (Q4FY26 deck
  p.8) at the low-ticket, high-volume end; Enterprise deals disclosed at
  USD 250k-700k (concall extraction, B06) at the mid-market enterprise-
  software end. Not one price segment; both ends included.
- **Explicit inclusions**: licensed CA DSC/SSL/eSign issuance; PKI-as-a-
  Service and CLM software; IAM software; eSignature workflow software;
  EU qualified trust services; the newer key/secrets-management,
  data-consent and agentic-AI-security lines (revenue not yet separately
  disclosed — included in scope, excluded from any revenue-based
  calculation below since no figure exists).
- **Explicit exclusions**: hardware tokens/USB dongles (third-party
  manufacture; the FIPS 140-3 recertification cycle disrupting that
  market, concall p.9, is a channel-destocking risk to eMudhra, not a
  market eMudhra itself sells into); the free-tier-commoditised DV-SSL
  segment (Let's Encrypt, AR p.169-172, explicitly named as commoditised
  and excluded from any premium-market sizing); broad "cybersecurity"
  categories eMudhra does not sell (endpoint, network security, SIEM,
  antivirus — QuickHeal's market, not eMudhra's); payments/UPI
  infrastructure; generic document storage/DMS without a signing
  workflow.

### 1B Management's own TAM claim(s)

No single company-stated $/Rs TAM figure for eMudhra's own addressable
niche exists anywhere in the injected corpus. Three adjacent claims
found, held for the Section 2 triangulation:

1. **AR MD&A Business Outlook** (p.144, text marker "[page 147]"–"[page
   148]"), dated with the FY26 AR (board meeting 06-May-2026): "Global
   cybersecurity spending reached $213 billion in 2025... Gartner
   projects global cybersecurity spending will reach $240 billion in
   2026, a 12.5% increase." This is the WHOLE global cybersecurity
   industry, not eMudhra's PKI/IAM/digital-trust niche. Definition: none
   given (no eMudhra-specific carve-out stated). Date: Gartner figure as
   cited in the FY26 AR (2026). **Credibility read: BROAD** — placed in
   the AR immediately ahead of eMudhra's own strategy section, which
   creates an implicit "this is our opportunity" framing the number does
   not actually support. Flagged for Section 2.
2. **Q4FY26 Investor Presentation** (07-May-2026, p.6-8): "Industry
   growth: Global Trust Services 13.0% (FY26-FY28)" and "Industry growth
   rate: Global Cyber Security and Paperless Transformation 21.2%
   (FY2026-FY2028)." Source cited: Frost & Sullivan, 2024 data. Definition:
   growth rate only, no absolute $ TAM stated. Date: F&S 2024 (STALE —
   2 years old at run date). **Credibility read: SPECIFIC** — a named,
   dated, sourced growth rate that independently corroborates against
   external web-search figures in Section 2 (Mordor Intelligence's global
   PKI CAGR of 20.76% sits almost exactly on the F&S 21.2% figure).
3. **Q4FY26 Investor Presentation** (p.8): "~38% market share by value
   (Frost & Sullivan, 2024)" for eMudhra in the India DSC market.
   Definition: DSC-only, India, by value. Date: F&S 2024 (STALE, same
   flag). **Credibility read: SPECIFIC** — a checkable, self-reported
   share claim; used directly as Method 2's bottom-up anchor below.

eMudhra does not claim TAM = SAM = its own growth runway anywhere in the
corpus — a rare restraint worth naming. The AR's MD&A framing (claim 1)
is the one place a careless reader could conflate the whole
cybersecurity industry with eMudhra's addressable slice; Section 2
treats it accordingly.

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

Because eMudhra spans a narrow licensed India market (Trust Services)
and a global enterprise-software category (Enterprise Solutions), this
stage sizes them **separately** as Market A and Market B, then combines,
per the instruction to show global and India components separately.

### Market A — India licensed Trust Services (DSC, SSL/TLS, eSign)

**Method 1, top-down.** Two generic market-research reports found via
web search (2026-09-19), both flagged LOW-M confidence (SEO-style market-
report vendors, not the IBEF/CRISIL/ICRA/CARE/Mordor/Ken tier the
instructions prefer, though the specific-firm names used below are
mid-tier, named firms):
- Grand View Research: India digital signature market USD 163.4M (2024)
  -> USD 1,401.6M (2030), stated CAGR 44.4% (2025-2030). Forward-computed
  to 2026 at the implied 43.1% CAGR: ~USD 334M.
- Fortune Business Insights: India market ~USD 0.41B (2026) directly
  stated.
These two diverge only ~23% from each other (USD 334M vs USD 410M) — a
reasonable band. STALE flag on the GVR 2024 base year.
USD 334-410M x Rs 84 = **Rs 2,806 - 3,444 Cr**.

**Method 2, bottom-up (management-share-anchored).** Unit = one
commercially-issued India DSC/eSign/SSL. eMudhra Trust Services FY26
revenue Rs 140.01 Cr (AR Note 49) / eMudhra's own disclosed ~38% share
by value (F&S 2024, Q4FY26 deck p.8) = **implied India DSC market of
Rs 368 Cr** (140.01 / 0.38). Flag: this mixes an FY26 revenue numerator
with a 2024-vintage share denominator — a methodological seam, not a
clean same-year calculation.

**Method 3, peer aggregation (directional only).** AR p.157-158 names
~20 licensed India CAs (eMudhra, Safecrypt, IDRBT, (n)Code Solutions,
CDAC, Capricorn, Protean, V Sign/Verasys, Indian Air Force, CSC, RISL,
Indian Army, ID Sign, CDSL Ventures, Pantasign, Xtra Trust, ProDigiSign,
Sign X, Care4Sign, IGCAR); Q4FY26 deck states "24 CAs in India, 10
actively issuing DSCs." Most non-eMudhra names are captive/government
issuers (Air Force, Army, RISL, IGCAR, CSC), not commercial competitors
at scale. No individual peer DSC revenue is disclosed in the corpus
(B06 does not cover a pure-play India CA peer), so this method cannot
independently compute a number — it only corroborates that the
**commercial** (non-captive) DSC market is small, consistent with
Method 2's order of magnitude rather than Method 1's.

**Method 4/5**: SKIPPED. Import substitution does not apply cleanly (DSC
issuance is a licensed domestic activity, not an import-substitutable
good). Global per-capita benchmarking has no natural comparator for a
licence-capped Indian market. Both stated, not silently omitted.

**Triangulation, Market A:**

| Method | Estimate (Rs Cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down (GVR/FBI) | 2,806 - 3,444 | L-M | STALE (GVR base 2024) |
| 2. Bottom-up (mgmt share) | 368 | M | STALE (F&S 2024 share) |
| 3. Peer aggregation | directional only, corroborates ~Method 2 scale | L | n/a |

Divergence ~8-9x between Method 1 and Method 2. Read: the top-down
reports almost certainly price a broader "digital signature" category
(including signing SOFTWARE, not just CCA-licensed certificate issuance)
than the narrow, licence-scoped market eMudhra's own 38%-share claim
describes. Per Rule 6 (conservative bias, take the lower), **Market A
conservative = Rs 368 Cr**; realistic is set by an explicit analyst
bridge (not a silent average) at **Rs 800 Cr**, splitting the difference
toward Method 1 to allow for the fact that Trust Services revenue also
includes some eSign/SSL software-adjacent elements beyond pure DSC
issuance.

### Market B — Global PKI-as-a-Service / CLM / IAM-adjacent enterprise
software (Enterprise Solutions)

**Method 1, top-down.** Web search (2026-09-19), global PKI market:
- Research and Markets: USD 6.65B (2026) -> USD 13.64B (2030), CAGR 19.7%.
- Mordor Intelligence: USD 8.96B (2026) -> USD 22.99B (2031), CAGR 20.76%.
Per Rule 6, take the lower: **USD 6.65B (Rs 55,860 Cr), global, 2026**.
Adjacent categories also sized but not summed (double-counting risk):
global e-signature platform market USD 4.08-13.09B (2026, wide spread
across sources, LOW confidence); global IAM market USD 24.56-29.7B
(2026); global CLM software market USD 1.52-6.19B (2026, widest spread
of all, LOW confidence — three sources gave USD 1.52B, 5.23B and 3.5B
for overlapping years).

**Method 3, peer revenue aggregation.** Named global competitors from
AR p.157-159 (Digital Trust Services / PKI / IAM table): DigiCert,
Entrust, Sectigo, GlobalSign, Microsoft, IBM, Ping Identity, Okta,
SailPoint, Ilantus, Saviynt, Thales, Broadcom, Keyfactor, Nexus Group,
AppViewX, Venafi. Revenue found (web search, 2026-09-19) for the three
most PKI-specific named pure-plays: DigiCert ~USD 420M (Owler estimate,
FY2025), Keyfactor ~USD 100M ARR (Feb-2024 press release, "$100M ARR in
under 5 years"), Venafi ~USD 150M ARR (at 2024 CyberArk acquisition,
USD 1.54B deal). Adding eMudhra's own Enterprise Solutions Outside India
revenue (Rs 437.57 Cr = USD 52.1M): **DigiCert + Keyfactor + Venafi +
eMudhra = USD 722.1M**. Applying a 30% uplift for the unnamed long tail
(GlobalSign, Sectigo, Entrust's PKI-specific slice, AppViewX, Nexus
Group, regional players — none individually sized in the corpus or
web search): **USD 938.7M = Rs 7,885 Cr**.

**Method 2, bottom-up.** Addressable unit would be "one enterprise
account"; per-account ACV is NOT FOUND anywhere in the corpus (B04:
"per-deal ACV NOT FOUND"). Per the never-estimate-a-missing-number rule,
this method is not computed for Market B — stated as a gap, not
fabricated.

**Triangulation, Market B:**

| Method | Estimate | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down, global PKI (conservative of 2 sources) | USD 6.65B = Rs 55,860 Cr | M | current (2026 reports) |
| 3. Peer aggregation (named pure-plays + 30% long-tail) | USD 938.7M = Rs 7,885 Cr | M | current |
| 2. Bottom-up | NOT FOUND (no ACV disclosed) | n/a | n/a |

Divergence ~7.1x between Method 1 and Method 3. Read (per Rule 5, explain
rather than average): the generic "global PKI market" figure almost
certainly blends embedded/OEM PKI spend bundled inside larger
cybersecurity platforms (Microsoft, IBM, Broadcom security suites) that
never appears as a discrete PKI-vendor revenue line, plus hardware
security module (HSM) and broader "digital trust platform" spend
(DigiCert self-describes as a "digital trust platform," not a pure PKI
vendor). The peer-aggregation figure only captures revenue that shows up
against named, PKI-labelled vendors — the category eMudhra actually
competes in and was named a leader of by Frost & Sullivan. Per Rule 6,
**Market B conservative = Rs 7,885 Cr** (peer aggregation, the lower and
better-scoped figure). Realistic is set, by explicit analyst bridge, at
**2x conservative = Rs 15,770 Cr** — still far below the USD 6.65-8.96B
top-down ceiling, reflecting that the newer product lines (AI Cyberforge,
PrivaTrust, agentic-AI security) widen eMudhra's served categories beyond
pure PKI, without asserting the company can address the full top-down
figure.

Growth rate for Market B: F&S 2024 (mgmt deck, claim 2 above) states
21.2% for "Global Cyber Security and Paperless Transformation
(FY26-FY28)"; independently, Mordor Intelligence's global PKI CAGR is
20.76% (2026-2031) and Research & Markets' is 19.7% (2026-2030). These
three, from two independent lines of evidence (company-cited F&S vs.
web-search Mordor/R&M), **converge tightly around 20-21%** — unlike the
absolute TAM-size estimates, the growth RATE triangulates well.

### Combined TAM

| | Market A (Rs Cr) | Market B (Rs Cr) | Combined (Rs Cr) |
|---|---|---|---|
| Conservative | 368 | 7,885 | **8,253** |
| Realistic | 800 | 15,770 | **16,570** |

**tam_cr: conservative Rs 8,253 Cr, realistic Rs 16,570 Cr.**

Blended TAM growth rate, weighted by conservative-TAM component
(Market A 4.5% weight at 13.0% growth, Market B 95.5% weight at ~20.8%
growth): **~20.8%** (0.045x13.0 + 0.955x21.0 approx = 20.8%), taking the
F&S/Mordor-corroborated Market B rate as dominant given its 95%+ weight.

### Management claim vs conservative estimate

Using AR MD&A claim 1 ($240B global cybersecurity spend, 2026, Gartner-
sourced) as the only quantified $ figure management's own filed
documents put next to their opportunity framing: USD 240B x Rs 84 =
**Rs 20,16,000 Cr**. Ratio to conservative combined TAM (Rs 8,253 Cr) =
**244x**. Per the standard read (>2x likely inflated), this reads as
INFLATED — but the honest characterisation is a **denominator mismatch**,
not a fabricated company-specific claim: management cited the entire
world cybersecurity industry, not its own niche, and never itself states
a TAM number for its own addressable market. The genuinely testable
management claim (the 38% India DSC share, claim 3) is not independently
testable against the combined TAM because it was used to construct
Method 2 itself — flagged as circular, not scored a second time.

**mgmt_claim_cr: 2,016,000 ; mgmt_claim_ratio: 244 ; mgmt_claim_read:
inflated (with the denominator-mismatch caveat above).**

---

## SECTION 3: SAM & SOM

### 3A SAM — five filters applied to conservative TAM (Rs 8,253 Cr)

**Market A (Rs 368 Cr):**
1. Product fit x0.90 (excludes the commoditised free-tier DV-SSL slice,
   AR p.169-172) = Rs 331 Cr
2. Geography x1.00 (already India-scoped by definition) = Rs 331 Cr
3. Channel x0.95 (minor cut for large-government-captive-CA business
   eMudhra structurally cannot win, e.g. Indian Air Force/Army/RISL
   in-house CAs) = Rs 315 Cr
4. Customer x0.90 (large in-house/self-build enterprises) = Rs 283 Cr
5. Capability x1.00 (Trust Services capability proven — 38% share,
   WebTrust-accredited, licence renewed) = **Rs 283 Cr**

**Market B (Rs 7,885 Cr):**
1. Product fit x0.85 (excludes hardware/HSM-only and browser-commodity
   slices) = Rs 6,702 Cr
2. Geography x0.40 (eMudhra's actual disclosed footprint — India, US,
   DACH/Europe via Cryptas, UAE/Middle East, Indonesia/Philippines,
   Kazakhstan — is a fraction of the "35+ countries" nominally reached,
   AR p.150, vs. the full global category) = Rs 2,681 Cr
3. Channel x0.95 (minor cut for hyperscaler-bundled/framework-only deals
   eMudhra's scale cannot access) = Rs 2,547 Cr
4. Customer x0.90 (largest enterprises that self-build rather than buy,
   corroborated by Gartner's fragmentation note in the Q1FY27 deck p.5-6:
   "most organisations are still assembling, rather than buying
   off-the-shelf") = Rs 2,292 Cr
5. Capability x0.70 (genuine current delivery-capacity gap against
   DigiCert/Entrust/Microsoft/Okta scale, evidenced by the Outside-India
   Enterprise segment's compressed 21.9% margin vs India's 57.5%,
   Note 49) = **Rs 1,605 Cr**

**SAM = Rs 283 Cr + Rs 1,605 Cr = Rs 1,888 Cr.**
**SAM as % of conservative TAM = 1,888 / 8,253 = 22.9%.**

### 3B SOM at 3 and 5 years

Current share of SAM = FY26 revenue / SAM = 701.58 / 1,888 = **37.2%**.
This is already a high current share — the SAM filters (especially the
geography and capability cuts) have already carved the market down to
close to eMudhra's present footprint, leaving eMudhra already dominant
within its own realistically-served pool rather than a marginal player
chasing a vast open field.

Share-gain tier selected: **AGGRESSIVE (3-5pp in 3 years)**, justified by
(a) demonstrated capacity/execution — three acquisitions in ~18 months
(Cryptas, Two95, AI Cyberforge) plus Rs 248.27 Cr of FY26 capital
deployment (Section 3C below); (b) the Gartner "assembling, not buying"
fragmentation note above, which is the closest available evidence of an
unorganised/self-build share >40% formalising toward vendor purchase —
the framework's named condition for faster-than-normal share gain.
**+4pp by Year 3, +6pp by Year 5** (a continuation, not a second one-off
jump, so it stays inside the aggressive band rather than requiring the
>5pp competitor-exit justification).

Arithmetic, using the 20.8% blended TAM growth rate to grow SAM forward:

- **Year 3**: SAM = 1,888 x (1.208)^3 = 1,888 x 1.7628 = **Rs 3,328 Cr**.
  Share = 37.2% + 4pp = 41.2%. SOM = 41.2% x 3,328 = **Rs 1,371 Cr**.
  Implied 3-year revenue CAGR = (1,371 / 701.58)^(1/3) - 1 = **25.1%**.
- **Year 5**: SAM = 1,888 x (1.208)^5 = 1,888 x 2.5723 = **Rs 4,857 Cr**.
  Share = 37.2% + 6pp = 43.2%. SOM = 43.2% x 4,857 = **Rs 2,098 Cr**.
  Implied 5-year revenue CAGR = (2,098 / 701.58)^(1/5) - 1 = **24.5%**.

**som_3yr_cr: 1,371 ; som_5yr_cr: 2,098 ; som_implied_revenue_cagr: yr3
25.1%, yr5 24.5%.**

**FORMAL HANDOFF vs load-bearing fact 1**: the SOM-implied CAGR (~24.5-
25.1%) sits materially ABOVE the company's own FY27 ORGANIC growth guide
of 15-18% (company memory, load-bearing fact 1). The gap is explained by
what SOM includes and organic guidance excludes: continued bolt-on M&A
at a pace similar to FY26 (three acquisitions) and the aggressive
share-gain tier. If FY27+ M&A activity stops, the achievable path
collapses toward the organic guide, well below the SOM figures above —
named explicitly, not silently assumed away. Stage 11 should treat the
SOM CAGR as an M&A-inclusive ceiling case, not an organic base case.

### 3C Capacity cross-check

Injected capex figure (B07, AR p.[marker near line 7063]/[page 155-156]):
FY26 purchase of PPE and intangibles INR 1,853.68 Mn (Rs 185.37 Cr) plus
acquisition payment INR 629.03 Mn (Rs 62.90 Cr) = **Rs 248.27 Cr** total
FY26 capital deployment, against FY26 revenue of Rs 701.58 Cr — a
35.4% capex+M&A/revenue ratio, an unusually heavy year (B04 flags this
capex figure does not fully reconcile to the AR's own p.150 investing-
activities breakdown; not re-resolved here, carried as an open flag).

eMudhra is asset-light (B04); the binding capacity constraint for the
SOM path is less physical plant and more (a) delivery/support headcount,
(b) data-centre footprint (New Jersey, Salt Lake City, Germany via
Cryptas), and (c) continued acquisition cadence. Stripping the
acquisition-specific outlay leaves **organic capex of Rs 185.37 Cr
(26.4% of FY26 revenue)** — a substantial but not physically-impossible
organic reinvestment rate for a software business.

**Verdict**: no hard physical-capacity gap in the sense of a factory
that cannot produce more units. The real gap is that Rs 1,371-2,098 Cr
of SOM revenue over 3-5 years requires the M&A engine (Rs 62.90 Cr in a
single year, FY26) to keep running at a similar cadence, not a one-off.
If FY27+ acquisition spend reverts to zero, **the SOM is the optimistic
side of this cross-check**; the organic-only capacity path tracks closer
to the 15-18% guide than to the 24-25% SOM-implied CAGR.

**capacity_check: "no physical-plant gap (asset-light); SOM's ~24-25%
CAGR is contingent on continued bolt-on M&A at a FY26-like pace (Rs 62.9
Cr/yr acquisition outlay demonstrated); SOM is the optimistic side if
FY27+ M&A stops."**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Regulatory tailwind | High | EU NIS2/DORA compliance mandates (concall, B06); UAE Trust Service Provider Guidelines requiring in-country data centres (concall, B06); India FIPS 140-3 recertification deadline Sep-2026 (concall p.9); 2-year India DSC renewal cycle; SSL certificate lifespan cut to 47 days by 2029, a CLM-automation tailwind (Q4FY26 deck p.8) |
| Technology enablement | High | Post-quantum cryptography transition (AR intro); AI/agentic-AI security demand — WEF Global Cybersecurity Outlook 2026 names AI the top driver of change per 94% of surveyed leaders (AR p.144); machine identity "growing faster than human identity" (Q1FY27 deck p.5-6, Gartner-sourced, paraphrased) |
| New applications | Medium | Newly launched AI Cyberforge (key/secrets management) and PrivaTrust (data consent) lines target the machine-identity/AI-driven category; management itself calls revenue "still pretty early stage... hard to quantify" (concall report, Kaushik Srinivasan, Q1 FY27) — a real driver, unquantified |
| Geographic expansion | Medium | UAE QTSP licence pending; EU deepening via Cryptas/PrimeSign (FY27 focus, Q4FY26 deck p.12); Kazakhstan/CIS entry (Almaty office, AR p.186); Philippines/Malaysia penetration (AR) |
| Formalisation | Medium | Paperless transformation push in BFSI/Capital Markets (AR); Gartner's "assembling, not buying off-the-shelf" note (Q1FY27 deck) implies a self-build-to-buy formalisation runway for machine identity/secrets tooling specifically |
| Penetration/macro | Low-Medium | IMF Oct-2025 WEO: emerging/developing economies growing ~4% vs advanced economies ~1.5% (AR p.144) — a macro backdrop, not eMudhra-specific |

### 4B TAM risks

| Risk | Monitoring signal |
|---|---|
| Disruption (commoditisation) | DV-SSL segment commoditised by free Let's Encrypt (AR p.169-172, explicit) — watch SSL/TLS revenue mix (currently 6% of Trust Services, Q4FY26 deck p.8) |
| Regulatory headwind | CCA licence renewed every 5 years; repeat of the July-2024 CCA model change that already hit stock-in-trade once (B04); WebTrust accreditation or browser root-store distrust event (B04 first-deterioration signal) |
| Global competition | DigiCert, Entrust, Sectigo, GlobalSign, Microsoft, IBM, Okta, SailPoint, Thales, Broadcom all named as direct competitors with materially larger scale (AR p.157-159) |
| Cyclical/geopolitical | Middle East war-driven large-deal deferral, independently corroborated by both NEWGEN and PROTEAN in the same quarters eMudhra's own concalls flag delay (B06, strongest unprompted peer corroboration this run) |
| AI-driven deal deferral | NEWGEN names AI-driven customer uncertainty as an explicit, repeated large-deal deferral cause; eMudhra's own concalls never raise this for its own pipeline — a monitoring gap (B06) |
| Channel destocking | India FIPS 140-3 recertification forcing token-manufacturer recertification, causing temporary channel destocking ahead of Sep-2026 (concall p.9) |

### 4C Market structure

- **Competitor count**: India Trust/CA space — ~24 licensed CAs, 10
  actively issuing DSCs (Q4FY26 deck); most non-eMudhra names are
  captive/government issuers, not commercial competitors at scale. Global
  Enterprise Solutions space — large and fragmented at the long tail
  (Gartner: "landscape of specialised vendors rather than a single
  consolidated category," Q1FY27 deck p.5-6), with big-platform players
  (Microsoft, IBM, Google) at one end and specialist PKI/CLM/IAM vendors
  at the other.
- **Top-3 concentration**: India DSC — eMudhra alone claims ~38% by value
  (F&S 2024); next-largest named commercial peer's share NOT FOUND in the
  corpus. Global PKI-as-a-service — combined top-3 concentration NOT
  FOUND; not estimated.
- **Organised vs unorganised**: the closer analogue here is build-vs-buy,
  not formal-vs-informal retail — Gartner's own framing (Q1FY27 deck)
  that most enterprises still assemble rather than buy off-the-shelf
  machine-identity tooling functions as an "unorganised" (self-build)
  segment likely above the framework's 40% formalisation threshold,
  though no precise % is disclosed (NOT FOUND, used qualitatively only
  in 3B).
- **Consolidating or fragmenting**: consolidating at the top — CyberArk
  acquired Venafi for USD 1.54B (2024); Palo Alto Networks completed its
  USD 25B acquisition of CyberArk (11-Feb-2026); eMudhra itself made
  three bolt-ons in ~18 months. Long tail stays fragmented per Gartner.
- **Price vs differentiation**: DV-SSL is price-competed (commoditised,
  free-tier pressure); enterprise PKI/CLM/IAM competes on
  differentiation — compliance depth, regional data residency, WebTrust
  accreditation, "one-stop-shop" positioning (AR p.157).
- **Entries and exits**: the two large 2024-2026 consolidations above; no
  India CA licence exits found in the corpus.
- **Import-substitution analogue**: eMudhra explicitly frames itself as
  "the Only Indian player to have the range of capabilities in our
  space" (AR p.157) against an entirely US/Europe-headquartered
  competitor set (DigiCert, Entrust, Sectigo, GlobalSign, Microsoft,
  Okta, SailPoint, Thales, Broadcom) — the closest available analogue to
  Method 4's import-substitution frame, though a full
  consumption/production/import breakdown is NOT FOUND at this
  granularity and was not estimated.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
TAM (conservative)  Rs 8,253 Cr   |  TAM (realistic)  Rs 16,570 Cr
        |  5 filters (product, geography, channel, customer, capability)
        v
SAM                 Rs 1,888 Cr   (22.9% of conservative TAM)
        |  current revenue Rs 701.58 Cr = 37.2% of SAM already captured
        v
SOM  Yr3            Rs 1,371 Cr   (25.1% implied revenue CAGR)
SOM  Yr5            Rs 2,098 Cr   (24.5% implied revenue CAGR)
```

### 5B Runway assessment

- Revenue headroom = SAM / current revenue = 1,888 / 701.58 = **2.69x**.
- TAM growth rate (blended) = **~20.8%** (F&S 21.2%/13.0% mgmt-cited,
  corroborated independently by Mordor Intelligence's 20.76% global PKI
  CAGR).
- Company CAGR (FY26 actual, 35.1%) vs TAM growth (~20.8%): the company
  is growing faster than its market — **gaining share, not merely riding
  the market** — though FY26's 35.1% includes acquired (Cryptas/Two95/AI
  Cyberforge) as well as organic growth (B04 flags the organic/acquired
  split is only disclosed at segment level, not company-wide).
- Years to saturate SAM at current growth: solving 701.58 x
  (1.351)^n = 1,888 x (1.208)^n gives **n approx 8.9 years** — shown
  arithmetically as the mechanical answer; not a forecast, since holding
  FY26's M&A-boosted 35.1% growth rate constant for 8-9 years is
  implausible on its face.

### 5C Runway classification

Using standard headroom bands (MASSIVE >10x, STRONG 5-10x, GOOD 3-5x,
MODERATE 1.5-3x, LIMITED <1.5x) stated explicitly since the instruction
file does not repeat exact cut-offs: **revenue_headroom_x = 2.69x places
this at MODERATE**, near the top of that band and close to the GOOD
boundary. This reading is driven by the SAM filters — particularly the
40% geography cut and 70% capability cut on Market B — which reflect
genuine current execution-capacity constraints against globally larger
rivals (DigiCert, Entrust, Microsoft, Okta), not a lack of underlying
market growth (TAM growth ~20.8% is healthy).

**runway_class: MODERATE.**

### 5D SAM expansion levers actually being pursued

| Lever | Status | Potential addition |
|---|---|---|
| UAE QTSP licence | Pending (concall, B06) | NOT FOUND ($, not disclosed) |
| EU deepening via Cryptas/PrimeSign | Active, named FY27 focus (Q4FY26 deck p.12) | Already inside Market B/current revenue; incremental $ NOT FOUND |
| AI Cyberforge / PrivaTrust / agentic-AI security | Launched, revenue not yet separately disclosed; management itself calls it "hard to quantify" (concall) | NOT FOUND |
| Continued bolt-on M&A | Explicitly named FY27 strategic focus (Q4FY26 deck p.11: "selective bolt-on product acquisitions") | NOT FOUND (no target list disclosed) |

Revised headroom: **not computed** — every lever above lacks a
disclosed $ figure; per the never-estimate rule, this is stated as a gap
rather than filled with an assumed number.

### 5E Final output card

- TAM (conservative / realistic): **Rs 8,253 Cr / Rs 16,570 Cr**
- SAM: **Rs 1,888 Cr (22.9% of conservative TAM)**
- SOM Yr3 / Yr5: **Rs 1,371 Cr / Rs 2,098 Cr**
- SOM-implied revenue CAGR Yr3 / Yr5: **25.1% / 24.5%**
- Current SAM share: **37.2%**
- Revenue headroom: **2.69x**
- Runway class: **MODERATE**
- Management claim read: **INFLATED (denominator mismatch — whole-industry
  figure cited, not a company-specific claim)**

**Valuation implication line**: At approximately 24-25% revenue CAGR
implied by SOM (25.1% at 3 years, 24.5% at 5 years), with an observed
margin trajectory that is roughly flat to mildly compressing — operating
margin 19.4% FY26 versus 20.9% FY25 (FY26 Audited Results p.8; Note 49
shows the compression is driven by the lower-margin international
Enterprise mix, not margin expansion — the opposite of an "operating
leverage" story for FY26 specifically, corroborating B04's finding) —
the earnings growth embedded here is **NOT FOUND** (a forward margin/EPS
bridge is Stage 11's Section 1B task, built on the destination-mix
bridge, not something Stage 9 should assert), which cannot yet be
assessed against the current valuation of **NOT FOUND x P/E** (no market
price was injected into this stage's inputs). Stage 11 should read the
SOM CAGR (24-25%) alongside the explicit caveat in 3B/3C that it is an
M&A-inclusive ceiling case, materially above the company's own 15-18%
organic guide.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | CCA (Controller of Certifying Authorities, MeitY) licensing/model changes | Regulatory | Governs DSC licence renewal (5-yr cycle) and fee/model structure; the July-2024 CCA model change already caused a stock-repurchase charge (B04) — a repeat is a direct Trust Services revenue risk | MeitY / CCA government portal | Event-driven |
| 2 | CA/Browser Forum + browser root-store vendors (Google Chrome, Microsoft, Mozilla, Apple) | Regulatory | WebTrust audit result and browser root-store listing are existential for SSL/TLS issuance; loss = distrust event (B04 first-deterioration signal) | CA/Browser Forum public records; browser-vendor security blogs | Event-driven |
| 3 | UAE Telecommunications and Digital Government Regulatory Authority (TDRA) | Regulatory | Governs the pending QTSP licence and the in-country-data-centre mandate named in concalls (B06 unverifiable claim) that gates eMudhra's UAE Trust Services expansion | TDRA government portal | Event-driven |
| 4 | EU NIS2/DORA regulatory implementation (ENISA, national regulators) | Regulatory / Macro | Named structural driver of European PKI/qualified-trust-service demand for Cryptas/PrimeSince (concall-named, peer-unverifiable per B06); SHARED — drives both Trust-adjacent qualified-trust revenue and Enterprise Solutions Europe revenue | ENISA / EU Official Journal publications | Quarterly / event-driven |
| 5 | Large India public-sector and BFSI customers (named defence agency, unnamed PSU bank, InCommon US university consortium) | End-customer | Direct order-book and large-deal signal for both Trust Services (B2G filing) and Enterprise Solutions | Customer/counterparty public procurement disclosures, press releases | Event-driven |
| 6 | Gartner / IDC global cybersecurity and PKI-as-a-Service spend trackers | Macro | The macro demand backdrop management itself cites in the AR MD&A and investor decks (claims 1-2, Section 1B) | Gartner/IDC published forecast updates (press-release summaries) | Quarterly |
| 7 | Named global PKI/IAM competitors (DigiCert, Keyfactor, Venafi/CyberArk, Entrust) | Counterparty (competitor-as-signal) | Competitor revenue growth and consolidation (CyberArk-Venafi, Palo Alto-CyberArk) is an indirect read on total category demand and eMudhra's relative share trend | Company press releases; private-company revenue aggregators (Owler/Craft) | Event-driven |

**demand_externally_verifiable: true** (7 candidate rows, within the
3-8 range; SHARED flag applied to row 4).

---

## SEARCH LOG

**Searches performed** (all 2026-09-19):
1. India digital signature certificate market size 2025 2026 report
2. Global PKI (public key infrastructure) market size 2026 2030 CAGR
3. Global e-signature market size 2026 forecast billion
4. Identity and access management (IAM) market size 2026 global billion CAGR
5. Certificate lifecycle management market size 2026 global
6. India cybersecurity market size 2026 CRISIL IBEF billion
7. Controller of Certifying Authorities India digital signature certificates issued per year 2025
8. Frost & Sullivan PKI-as-a-Service market India eMudhra 2025 best practices
9. Machine identity management market size 2026 Gartner billion
10. DigiCert annual revenue 2025, Keyfactor revenue, Venafi ARR, CyberArk acquisition

**Searches skipped / no usable result**:
- CRISIL/IBEF specific India cybersecurity or PKI report — queried inside
  search 6; results returned Mordor Intelligence and Coherent Market
  Insights instead, no CRISIL/IBEF-specific PKI or DSC report surfaced.
- Official CCA/MeitY annual DSC issuance statistics (search 7) — no
  usable public data point found; a third-party claim that eMudhra "has
  issued more than one million certificates" surfaced but is unanchored
  (likely eMudhra's own marketing site, not filed evidence) and was not
  used in any calculation.
- India-specific IAM or CLM market size was not separately searched;
  Market B uses global figures filtered through the disclosed India/
  international revenue split instead (status: partial, stated as a
  scoping choice, not a silent gap).

Status: **complete** (all planned methods executed or explicitly marked
SKIPPED with reason; no method silently dropped).
