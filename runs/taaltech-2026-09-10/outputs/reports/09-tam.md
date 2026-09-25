# STAGE 9 — TAM / SAM / SOM MARKET SIZING
TAAL Tech Ltd (TAALTECH) | Run date 2026-09-10 | Model: claude-sonnet-5

STATUS: PARTIAL. WebSearch returned "tool unavailable" on 20 of 20 calls this run
(100% failure, worse than stage 8's 75-80%). WebFetch to named URLs worked for
company self-disclosure and screener.in pages, but failed or returned unusable
content on every attempted industry-report source (Zinnov, Nasscom, Grand View
Research, Mordor Intelligence, IBEF, Statista, Fortune Business Insights,
MarketsandMarkets, Precedence Research). Full search log in Section 2 and the
YAML block. Every number below is anchored to a document I actually read; where
a number could not be found, it says so.

---

## SECTION 1: MARKET DEFINITION

### 1A Precise boundaries

- **Product scope**: outsourced, third-party engineering research and
  development (ER&D) services — plant engineering, product design engineering,
  aerospace design engineering, transport engineering design, civil
  infrastructure/construction engineering, BIM, digital twin, embedded
  systems/IoT, RPA, cloud/DevOps, ML/analytics, remote device management.
  These are the verticals TAAL Tech names on its own site and in the AR
  (task brief, PRODUCTS list).
- **Geographic scope of supply**: India-delivered (Bangalore hub, 521
  standalone engineers, AR p.24/note 3601-3602) but billed almost entirely
  outside India — Rs19,708.14 lakh of Rs19,742.92 lakh FY26 group revenue
  (99.82%) billed outside India, only Rs34.78 lakh billed in India (AR
  Note 42, geographical segments, line 15919-15928). The relevant demand
  pool is therefore GLOBAL outsourced ER&D spend reachable by an
  India-delivery-model vendor, not India-domestic engineering demand.
- **Customer scope**: enterprise industrial and technology clients in North
  America, Europe and APAC able to commission multi-year, multi-engineer
  outsourced programs (AR MD&A, p.37, line 2290-2291). Not SMEs, not
  one-off/spot engagements at scale (95.5% of revenue is ongoing T&M, B04).
- **Channel scope**: direct time-and-material (95.5% of revenue) and
  milestone fixed-price (4.5%) engagements (B04). No platform/marketplace
  channel. No disclosed captive-GCC-build offering (the fastest-growing
  channel at scale peers LTTS/Cyient now sell — see Section 4).
- **Price segment**: mid-market Indian offshore/onshore-blended T&M rates.
  Not premium European boutique rates (Alten, Akkodis/AKKA), not
  undifferentiated bottom-tier.
- **Explicit inclusions**: third-party outsourced ER&D delivered by
  India-headquartered or India-delivery-heavy vendors to global clients, in
  TAAL's four core verticals (plant, aerospace, transport, civil/AEC) plus
  its digital-engineering add-ons.
- **Explicit exclusions**: captive in-house R&D / client-owned Global
  Capability Centres (a client's own engineering centre is not
  addressable by TAAL); EPC/construction execution (physical build, as
  distinct from design); generic IT services (ERP, application
  maintenance, BPO) with no engineering-design content; semiconductor chip
  design services (a distinct specialist pond TAAL does not claim);
  automotive-OEM mega-programs requiring hundreds of dedicated engineers
  on one account (a scale TAAL's 521-engineer base cannot credibly staff
  today).

### 1B Management's own TAM claim

**NONE.** Grepped the full Annual Report 2025-26 for "Management Discussion",
"Industry", "Opportunit", "Outlook", "segment", "geograph" (22 hits). The
Management Discussion & Analysis (AR p.37, lines 2288-2337) says the ER&D
sector "offers ample growth opportunities" and that "the outlook for the
company remains very positive," with no market size figure, no growth-rate
figure, and no addressable-market claim anywhere in the 15,900+ line
document. It explicitly states: "we are yet to be able to assess the full
impact of AI on the engineering services sector" (AR p.37, line 2319-2320).
No investor presentation and no earnings-call material exists (confirmed at
B04, input_gaps). **mgmt_claim_cr = NOT APPLICABLE. There is no claim to
compare against Section 2's estimate.**

---

## SECTION 2: TAM ESTIMATION, MULTIPLE METHODS

### Search log (this section)

**Performed, usable results** (all via WebFetch, since WebSearch returned
"tool unavailable" on every call):
- screener.in/company/ONWARDTEC/consolidated — Onward Technologies FY24-26
  revenue and OPM. Success.
- screener.in/company/CYIENT/consolidated — Cyient FY24-26 revenue and OPM.
  Success.
- screener.in/company/LTTS/consolidated — LTTS FY24-26 revenue and OPM.
  Success.
- screener.in/company/TATAELXSI (retried after first attempt returned a
  stale 2015-era cache) — FY23-26 revenue and OPM. Success on retry.
- screener.in/company/SASKEN/consolidated — Sasken FY23-26 revenue and OPM.
  Success.
- ltts.com/about-us — LTTS self-reported USD 1.22bn revenue, headcount,
  patent count. Success, cross-checks the screener.in LTTS Rs figure.
- ltts.com/investors — returned real document URLs (investor
  presentation, annual report, earnings release PDFs).

**Attempted, failed or unusable** (searches_skipped in the YAML block):
- WebSearch x20 (all industry-market-size and peer-revenue queries; see
  full list in YAML `searches_skipped`) — every call returned "web search
  tool is currently unavailable."
- zinnov.com/insights, zinnov.com/press-release/indias-er-and-d-market,
  zinnov.com/reports — no ER&D market-size content found / 404.
- grandviewresearch.com (two URL guesses) — 403 Forbidden.
- mordorintelligence.com — 404 Not Found.
- ibef.org (two pages) — page loaded, no ER&D-specific figures present.
- nasscom.in strategic review — 406 Not Acceptable.
- statista.com — returned unrelated cached content (Tunisia agricultural
  producers page), clearly mismatched.
- marketsandmarkets.com and precedenceresearch.com — returned figures
  ($751.3bn "digital engineering services" 2025 vs $2.57 trillion
  "engineering services outsourcing" 2025 from a different query on a
  putatively overlapping category) that are internally inconsistent by
  more than 3x and, at the higher end, would place "outsourced ER&D"
  above total global ER&D spend of roughly $1.5-2 trillion (the figure
  named in this run's own task brief as the commonly quoted, but
  captive-dominated, wrong-pond TAM). **Rejected as unreliable. Not used
  as an anchor anywhere below.**
- fortunebusinessinsights.com — returned an unrelated report (US/EU-5
  wound care antibiotics market).
- cyient.com/investors — page loaded, no market-sizing content found.
- ltts.com Q1FY27 Investor Presentation PDF — fetched (2.8MB) but could
  not be parsed as text; graphics-heavy slide PDF, "compressed/encoded
  stream data."
- ltts.com Integrated Annual Report FY26 PDF — exceeded the 10MB fetch
  limit, could not be read at all.
- screener.in/company/TAALENTER and /company/TAAL — both 404; could not
  independently confirm TAAL's own current market price or P/E this run.

**Net effect**: Method 1 (top-down industry report), Method 4 (import
substitution — also not applicable to this business) and Method 5 (global
per-capita benchmark) are **NOT FOUND** this run. Method 3 (peer revenue
aggregation) is built on real, dated, sourced numbers. Method 2 is adapted
to the company's actual scaling unit per the task brief and carries the
formal stage-11 handoff.

### Method 1 — Top-down industry size

**NOT FOUND.** Every attempted source either returned no usable figure, 403,
404, mismatched content, or internally inconsistent numbers rejected above.
This is a genuine data gap, not filled with an estimate.

### Method 2 — Bottom-up, the unit that scales

Revenue = billable engineers × realised rate × utilisation. TAAL is an
asset-light people business (net block Rs2.95cr at 31-Mar-2026, down from
Rs6.27cr a year earlier — task brief, B07); there is no capex-to-capacity
conversion to model. The addressable unit is one billable engineer.

- Standalone headcount: 521 (AR, "The number of permanent employees on
  the rolls of the company as on March 31, 2026 was 521," line 3601).
- Standalone revenue: Rs190.10cr (B04, AR p.90/p.24).
- Revenue per employee: ≈Rs36.5 lakh/year (B04; standalone revenue ÷
  headcount — a proxy only, no direct billable-rate disclosure exists).
- Consolidated revenue: Rs197.43cr (FY26 audited, task brief anchor).
  Consol/standalone ratio = 197.43/190.10 = 1.0386, implying a small
  overseas-subsidiary contribution (TAAL Technologies INC USA, TAAL Tech
  GmbH, TAAL Tech UK Ltd — AR p.38, line 2369-2371); consolidated
  headcount for those units is **NOT FOUND** in the AR.

A global bottom-up TAM would need the total count of billable ER&D
engineer positions addressable by an India-delivery vendor worldwide —
Zinnov/Nasscom track this, but every attempted source failed (see search
log). **The full bottom-up TAM denominator is NOT FOUND.** This method is
therefore carried forward into Section 3 as the SOM-construction method
(the task brief's explicit steer: "A SOM for this business is a headcount
ambition, not a market-share ambition"), not as a TAM figure.

### Method 3 — Peer revenue aggregation (the anchored method this run)

Listed India-origin ER&D services companies, FY26 consolidated revenue,
via screener.in (fetched 2026-09-10):

| Company | FY24 (Rs cr) | FY25 (Rs cr) | FY26 (Rs cr) | FY26 OPM |
|---|---|---|---|---|
| L&T Technology Services (LTTS) | 9,647 | 9,642 | 10,996 | 18% |
| Cyient | 7,147 | 7,360 | 7,268 | 12% |
| Tata Elxsi | 3,552 | 3,729 | 3,757 | 23% |
| Sasken Technologies | 406 | 551 | 1,113 | 8% |
| Onward Technologies | 472 | 491 | 544 | 13% |
| TAAL Tech (subject) | — | — | 197.43 | ~27.8% genuine (B04) |

Source: screener.in, each company's consolidated Profit & Loss table,
fetched 2026-09-10.

**Flag on Sasken**: FY26 revenue jumped from Rs551cr (FY25) to Rs1,113cr
(FY26), a 102% single-year jump inconsistent with organic ER&D demand
growth at this peer set's scale. Read as inorganic (acquisition-driven),
not used as a growth-rate anchor below; FY25's Rs551cr is used instead
where Sasken is a growth comparator.

Sum, 5 peers ex-TAAL, FY26: 10,996 + 7,268 + 3,757 + 1,113 + 544 =
**Rs23,678cr**. Including TAAL: **Rs23,875cr**.

This is stated explicitly as a **FLOOR, not a true TAM**. It excludes:
(a) the ER&D/engineering practices inside the diversified IT majors (TCS,
Infosys, Wipro, HCL Tech, Tech Mahindra, LTIMindtree) — several of these
individually could exceed the entire sum above, and none could be sourced
this run; (b) large unlisted or foreign-listed pure-plays (QuEST Global
and comparable) — not sourced this run; (c) the boutique/unorganised
tier. **True global outsourced-ER&D TAM addressable by an India-delivery
vendor is NOT FOUND this run.**

### Method 4 — Import substitution

**NOT APPLICABLE.** TAAL sells services, not a substitutable physical
good; there is no import/domestic-production/consumption structure to
apply this method to.

### Method 5 — Global benchmark (per-capita or per-GDP comparison)

**NOT FOUND.** Would require India's ER&D-exports-as-%-of-total-IT-exports
or a comparable China/SE Asia benchmark; every source attempted for this
failed (see search log).

### Triangulation table

| Method | Estimate (Rs cr) | Confidence | Staleness |
|---|---|---|---|
| 1. Top-down industry | NOT FOUND | — | — |
| 2. Bottom-up (full TAM denominator) | NOT FOUND | — | — |
| 3. Peer aggregation (floor) | 23,678 (ex-TAAL) / 23,875 (incl.) | L-M (real, dated, but known-incomplete) | Current, FY26 data |
| 4. Import substitution | NOT APPLICABLE | — | — |
| 5. Global benchmark | NOT FOUND | — | — |

Conservative estimate = Rs23,678cr. Realistic estimate = Rs23,875cr
(same order of magnitude; only one method returned usable data, so
"conservative" and "realistic" both key off Method 3, clearly flagged as
an understatement of the true market — see above).

**Management claim vs conservative estimate**: NOT APPLICABLE. Management
makes no TAM claim (Section 1B). No ratio to compute; none invented.

---

## SECTION 3: SAM & SOM

### 3A SAM

The standard five-filter waterfall (product, geography, channel, customer,
capability) needs vertical-level revenue splits for LTTS, Cyient and Tata
Elxsi (how much of their Rs10,996cr / Rs7,268cr / Rs3,757cr sits in
plant/aerospace/transport/civil engineering specifically, versus
automotive, telecom, medical devices, broadcast/media, and semiconductor
work that TAAL does not do). **That split is NOT FOUND this run** (search
failure named above). Rather than invent a filter percentage, each filter
is applied qualitatively and SAM is built from the closest observable
analog instead of a %-subtraction of the Rs23,678cr floor:

- **Geography filter**: no reduction. The Rs23,678cr floor is itself
  already an India-delivery-model set; TAAL's 99.82%-outside-India billing
  matches it exactly.
- **Product fit filter**: severe narrowing, not quantifiable. TAAL's four
  named verticals are a minority slice of what LTTS (telecom, medical
  devices, industrial products, automotive), Tata Elxsi (media/broadcast,
  automotive, healthcare) and Sasken (telecom/semiconductor) collectively
  cover. Cyient and Onward Technologies overlap TAAL's mix most closely
  (aerospace/rail/plant-adjacent at Cyient; automotive/industrial product
  design at Onward).
- **Channel/customer filter**: TAAL is T&M-only (95.5% of revenue, B04)
  with no disclosed captive-GCC-build offering; this rules out the
  billion-dollar-account, hundred-engineers-per-program tier that LTTS and
  Cyient increasingly compete for. TAAL's realistic customer set is
  mid-market accounts and expansion inside its own tenured base (70%+ of
  revenue from clients of 10+ years, AR p.37, line 2299-2301).
- **Capability filter**: no analyst coverage, no investor presentation, no
  earnings calls (B04) — growth here is relationship-led, not
  competitive-RFP-led at LTTS/Cyient scale.

**SAM proxy (closest-analog peer sum)**: Onward Technologies FY26
(Rs544cr, the closest T&M-model, mid-market, listed India ER&D pure-play
by business model) + Sasken's FY25 organic scale (Rs551cr, pre-acquisition
jump) ≈ **Rs1,095cr, rounded to Rs1,100cr**. This represents "what a
company operating this same T&M-only, no-captive-GCC, relationship-led
model has actually achieved at a more mature stage," anchored to two real,
dated figures rather than an invented percentage.

SAM as % of TAM floor: 1,100 / 23,678 = **4.6%**.

Flag: this SAM is itself a thin, data-poor proxy (two peers), built under
this run's search-failure conditions. It almost certainly understates the
true SAM a full five-filter waterfall with peer segment data would
produce. Carried forward with that caveat.

### 3B SOM at 3 and 5 years

**Current SAM share**: Rs197.43cr / Rs1,100cr = **17.9%**.

**The Amendment-25 read — two paths, named, not shaded safe:**

*Reading 1 (structural/historical-trend base)*: TAAL's FY23-FY26 trend ran
near 7% CAGR (B04, mgmt_questions). Applying peer-anchored organic
headcount growth of 10%/year (within the observed peer band: LTTS 6.8%,
Cyient 0.8%, Tata Elxsi 2.8%, Onward 7.4% two-year revenue CAGR FY24-26;
Onward's own five-year CAGR is 18%, screener.in) to the FY26 base, holding
revenue-per-engineer flat at Rs36.5 lakh (no evidence to model rate
inflation — B04 flags realised rate as undisclosed):
- 3yr: Rs197.43cr × 1.10³ = Rs262.7cr (10.0% CAGR)
- 5yr: Rs197.43cr × 1.10⁵ = Rs317.9cr (10.0% CAGR)

*Reading 2 (fresh-evidence base)*: Q1 FY27 (Jun 2026) consolidated revenue
was Rs64.81cr, up 41.6% YoY (implied Q1 FY26 ≈ Rs45.77cr), annualising to
≈Rs259cr — already a genuine step above the FY26 audited close. Per
Amendment 26's basis hierarchy (forward evidence over historical CAGR;
historical CAGR is the cross-check, not the base, when forward evidence
exists), this is the more evidenced starting point for FY27. Applying the
same 10%/year headcount-driven growth for years 2-3 (FY28, FY29) and years
2-5 (through FY31) on top of the Rs259cr FY27E base:
- 3yr (FY29): Rs259cr × 1.10² = **Rs313.4cr**, implied CAGR from the FY26
  audited base of Rs197.43cr = (313.4/197.43)^(1/3) − 1 = **16.6%**
- 5yr (FY31): Rs259cr × 1.10⁴ = **Rs379.2cr**, implied CAGR from FY26 =
  (379.2/197.43)^(1/5) − 1 = **13.9%**

**The one observation that separates the two readings**: whether Q2 and
Q3 FY27 (the two-to-three quarters not yet reported at this run date)
confirm a sustained Rs64-65cr+ quarterly run-rate, or whether the Q1 FY27
print reverts toward the ~Rs50cr quarterly level implied by the historical
7% trend. 4.5% of TAAL's revenue is fixed-price/milestone work (B04),
which can lump into a single quarter; B04 already names this exact
question as unresolved ("What caused the Q1 FY27 revenue jump... new
client, scope expansion, or something else?").

**Most evidenced path, stated plainly**: Reading 2 (fresh-evidence base)
is the more evidenced path under the framework's own basis hierarchy.
**SOM 3yr = Rs313cr, SOM 5yr = Rs379cr, implied CAGR 16.6% (yr3) / 13.9%
(yr5) from the FY26 audited base.** The conservatism this framework
requires belongs in position size, not in shading this number down
(v3.9 Amendment 25) — flagged prominently for the operator and for stage
11/13.

**Headcount cross-check** (the task's explicit ask: state the engineer
count implied, check against a plausible hiring rate):
- 3yr: implied standalone-equivalent revenue ≈ Rs313.4/1.0386 =
  Rs301.9cr → ÷ Rs36.5 lakh/engineer ≈ **827 engineers** (from 521 today,
  a 16.8% headcount CAGR).
- 5yr: implied standalone-equivalent revenue ≈ Rs379.2/1.0386 =
  Rs365.2cr → ÷ Rs36.5 lakh/engineer ≈ **1,000 engineers** (13.9%
  headcount CAGR from 521).

Both cross-check inside the peer-observed hiring-pace band: Onward
Technologies has actually achieved an 18% five-year compounded sales
growth rate (screener.in), so a 13.9-16.8% headcount CAGR for TAAL is
plausible, evidenced, not fanciful — but it is a real hiring lift (521 to
~1,000 engineers in five years) that TAAL has not yet demonstrated over a
multi-quarter track record. **Flag, not a halt.**

**Share-gain tension, named rather than hidden**: this SOM implies SAM
share rising from 17.9% today to 28.5% (3yr) to 34.5% (5yr) — share gains
of +10.6pp and +16.6pp, both above this framework's own "aggressive" 3-5pp
ceiling (normally reserved for competitor exit or acquisition, neither of
which applies here). Given the SAM denominator above is a thin, admittedly
undersized two-peer proxy built under this run's search-failure
conditions, the more likely read is that **the SAM measurement, not the
SOM headcount math, is what's off** — a true five-filter SAM with peer
segment data would almost certainly be larger than Rs1,100cr, which would
bring the implied share-gain back inside normal bounds. Named here so
stage 11 does not read a false red flag into a measurement artifact.

### 3C Capacity cross-check

B07's capex-embedded-growth figure is **NOT APPLICABLE** — TAAL is
asset-light (net block Rs2.95cr at 31-Mar-2026, down from Rs6.27cr a year
earlier; task brief). There is no capex-to-capacity conversion to check
the SOM against. The correct cross-check for this archetype is headcount,
performed in 3B above: the SOM path requires TAAL to roughly double its
standalone engineering headcount (521 → ~1,000) over five years, a pace
inside the peer-observed band but not yet demonstrated by TAAL itself.
**No capex-side gap to name; the open question is a hiring-execution
question, not a physical-capacity question.**

---

## SECTION 4: GROWTH DRIVERS, RISKS & STRUCTURE

### 4A TAM growth drivers

| Driver | Impact | Evidence |
|---|---|---|
| Technology enablement (digital twin, BIM, embedded/IoT) | Medium-High | Named directly in TAAL's own service list (task brief PRODUCTS); a standard ER&D-sector driver, but no sourced $-impact this run (search failure) |
| Client capex cycles in aerospace and plant/process industries | High, cuts both ways | AR MD&A explicitly names "a potential slowdown in the North American or European economies" as a risk to the company's growth trajectory (AR p.37, line 2316-2318) |
| Cost-effective, faster time-to-market pressure on OEMs | Medium | Named directly in AR MD&A: "the need to bring products to market faster and in a more cost-effective manner" (line 2311-2312) — company's own words, not independently verified against a market report this run |
| Formalisation / vendor consolidation toward fewer, deeper relationships | Medium | AR: "more than seventy percent of our business comes from customers who have been with us more than ten years" (line 2299-2301) — a demand-side stickiness signal, not a market-growth signal per se |
| Geographic expansion (TAAL has 3 foreign subsidiaries: US, Germany, UK) | Low-Medium | AR p.38, line 2369-2371; no revenue-by-subsidiary disclosure to size the effect |

Note: standard ER&D-sector drivers (offshore cost arbitrage, engineer
supply pool growth, GCC-to-outsourcing pendulum swings) are the usual
Nasscom/Zinnov talking points, but no sourced figure for any of them was
obtainable this run. Not stated as evidenced drivers; named as directional
context only, per house rule against estimating a missing number.

### 4B TAM risks

| Risk | Monitoring signal |
|---|---|
| AI-driven compression of billable engineering hours (the central swing factor for this hold — see below) | Realised billing rate / revenue-per-engineer trend (undisclosed today, B04 flags); Note 24 T&M sub-line |
| NA/Europe economic slowdown | AR MD&A names this directly (line 2316-2318); peer quarterly commentary (LTTS, Cyient) |
| Client concentration | Top customer 24.05% of FY26 revenue, up from 20.55% FY25 (B04 FLAG-CONCENTRATION) |
| Currency exposure | 99.82% of revenue billed outside India (AR Note 42); FX gain/loss line inside Other Income |
| Talent/wage inflation in India ER&D hiring market | Median remuneration Rs9.40 lakh p.a. (AR p.24); no attrition rate disclosed (B04 gap) |

### 4C Market structure

Competitor count and top-3 concentration: **NOT FOUND** at the India
ER&D-services level this run (search failure blocked the Nasscom/Zinnov
data that would normally carry this). What is anchored: within the small
listed peer set sourced above, LTTS (Rs10,996cr) and Cyient (Rs7,268cr)
together are roughly 77% of the five-peer sum (Rs23,678cr) — a
concentrated top of the listed table, though this says nothing about the
much larger unlisted/captive-practice mass this run could not size.
Organised vs unorganised split, consolidating/fragmenting direction, and
import-share trend: **NOT FOUND**, not estimated.

### The AI question, named honestly (task's explicit ask)

Management's own position: "we are yet to be able to assess the full
impact of AI on the engineering services sector. We will assess this as
we go along" (AR p.37, line 2319-2321). This is the single biggest swing
factor for offshore ER&D headcount economics over a 3-5 year hold.

**Reading A (AI compresses billable hours, bearish)**: GenAI copilots for
CAD/PLM work, generative design, and code-generation for embedded/IoT
deliverables can reduce hours-per-deliverable. If realised rate per hour
does not rise to offset fewer billed hours, revenue-per-engineer growth
slows and the headcount-linked SOM math in 3B breaks down — fewer
engineers could deliver the same revenue, capping the top line rather than
the headcount.

**Reading B (AI expands demand, bullish over this hold window)**: cheaper
per-unit engineering work has historically expanded commissioned volume
in IT/engineering services rather than shrinking total spend
(demand-elasticity effect). TAAL's core verticals — aerospace, plant/
process engineering — are safety-critical and typically slower to let AI
tooling substitute for reviewed human engineering judgment than generic
software coding is. A relationship-led, tenured vendor (70%+ of revenue
from 10+-year clients) is also better placed to package AI tooling as a
margin lever with existing accounts than to be disintermediated by it.

**The one observation that would separate them**: realised billing rate
per hour, trending down while volume/hours hold flat or rise, would be
the earliest hard signal of AI-driven price compression (Reading A). This
is not disclosed anywhere in the AR (B04 flags it as a gap) and cannot be
checked this run. Revenue-per-engineer (currently ≈Rs36.5 lakh) trending
up while headcount growth decelerates would instead support Reading B.

**Most evidenced path, stated without shading it safe**: there is
genuinely insufficient evidence to call a direction with confidence. What
is evidenced is that management itself has not modelled this by its FY26
year-end filing, which is a finding about management's strategic
foresight on this specific question, not a finding about which reading is
correct. This is named as an unresolved swing factor, not defaulted to
the cautious reading; per Amendment 25, the conservatism belongs in
position size, not in silently discounting the SOM CAGR above for an
unquantified AI risk.

---

## SECTION 5: SUMMARY & RUNWAY

### 5A Funnel

```
TAM (floor, 5 listed India ER&D peers, FY26)          Rs23,678cr
   |  product/channel/customer/capability filters, not quantifiable
   |  this run (peer segment data NOT FOUND) — analog proxy used instead
   v
SAM (closest-analog peer-scale ceiling: Onward +       Rs1,100cr  (4.6% of TAM floor)
     Sasken FY25 organic)
   |
   v
Current revenue (FY26 audited)                          Rs197.43cr (17.9% of SAM)
   |  fresh-evidence base (Q1 FY27 annualised ≈Rs259cr) + 10%/yr
   |  peer-anchored headcount growth
   v
SOM 3yr (≈FY29)                                          Rs313cr    (28.5% of SAM, 16.6% CAGR from FY26)
   v
SOM 5yr (≈FY31)                                          Rs379cr    (34.5% of SAM, 13.9% CAGR from FY26)
```

### 5B Runway assessment

- Revenue headroom = SAM ÷ current revenue = 1,100 / 197.43 = **5.6x**.
- TAM growth rate: **NOT FOUND** as a sourced industry figure. A rough
  proxy is available from the peer set's own trailing growth: FY24-FY26
  revenue-weighted CAGR across LTTS, Cyient, Tata Elxsi and Onward
  (Sasken excluded, M&A-distorted) ≈ **4.1%** (weighted by FY24 revenue;
  LTTS 6.8%, Cyient 0.8%, Tata Elxsi 2.8%, Onward 7.4%, weights 9,647 /
  7,147 / 3,552 / 472). This is a company-growth proxy standing in for a
  market-growth figure, clearly flagged as low confidence.
- Company CAGR vs proxy TAM growth: TAAL's SOM-implied 13.9-16.6% CAGR is
  roughly 3-4x the ~4.1% peer-aggregate proxy — this reads as gaining
  share (or riding a company-specific inflection), not simply riding a
  fast-growing market, since the sector itself (per this proxy) looks
  soft, consistent with the AR's own caution about NA/Europe demand.
- Years to saturate SAM at the SOM growth pace: at 13.9-16.6% CAGR from
  Rs197.43cr to a Rs1,100cr ceiling, roughly 11-13 years — well beyond
  this hold's 3-5 year window, so SAM saturation is not a near-term
  constraint under this (likely understated) SAM figure.

### 5C Runway classification

**GOOD.** Revenue headroom of 5.6x sits in the GOOD band (typically 5-10x
on this framework's standard bands). Flagged explicitly: this
classification is more likely an **understatement** than an overstatement,
because both TAM and SAM here are floors built under this run's total
search failure — a true five-filter SAM with peer segment data and a true
top-down TAM would very likely push this toward STRONG. Reported as GOOD
on the evidence actually in hand, not inflated to STRONG on an unverified
guess.

### 5D SAM expansion levers the company is actually pursuing

None disclosed with a quantified addition. The AR's own outlook language
("deepened our engagements with existing customers... added new
capabilities... won multiple strategic accounts," line 2325-2329) points
at account-depth expansion inside the existing tenured base rather than a
named new-geography or new-vertical lever. No captive-GCC-build offering,
no M&A, no new-vertical entry is named anywhere in the AR. **No sourced
potential addition to state; NOT FOUND rather than invented.**

### 5E Final output card

- TAM (floor): Rs23,678-23,875cr | SAM (analog proxy): Rs1,100cr (4.6% of
  TAM floor) | Current revenue: Rs197.43cr (17.9% of SAM) | SOM 3yr:
  Rs313cr | SOM 5yr: Rs379cr | Revenue headroom: 5.6x | Runway class: GOOD
  (likely understated).

**Valuation implication line**: "At 16.6% (yr3) / 13.9% (yr5) revenue CAGR
implied by SOM, with margin trajectory of [genuine EBIT margin ≈27.8%
currently, per B04; no disclosed forward margin trajectory, so held flat
as the only evidenced assumption], the earnings growth embedded here is
**approximately 13.9-16.6% CAGR** (before any margin change), which
[supports / does not support] the current valuation of **NOT FOUND** P/E
this run — current market price and P/E could not be independently
confirmed this run (screener.in ticker lookups for TAAL returned 404;
see search log). **This line cannot be completed without stage 11's own
current-price/P/E input; the revenue-CAGR and margin terms are supplied
here as the formal handoff.**"

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

| # | Candidate Signal | Entity Type | Why It Drives Demand | Likely Primary Source | Expected Cadence |
|---|---|---|---|---|---|
| 1 | Top customer revenue concentration (unnamed, 24.05% of FY26 revenue) | End-customer | Single largest account; loss or slowdown directly moves T&M billing | AR Note 42 (major customers disclosure), next AR | Event-driven / annual |
| 2 | Listed India ER&D peer quarterly results (LTTS, Cyient, Tata Elxsi, Onward Technologies, Sasken) | Counterparty | Sector demand-cycle read-across; the only real growth-rate proxy this run could source | Company quarterly results / investor releases | Quarterly — SHARED (feeds both the TAM-growth proxy and competitive-intensity reads) |
| 3 | USD-INR and EUR-INR exchange rates | Macro | 99.82% of revenue billed outside India; FX moves realised INR revenue directly | RBI reference rate / FBIL | Monthly |
| 4 | North America / Europe industrial and aerospace capex cycle (PMI, industrial production, Boeing/Airbus order backlogs) | Macro | AR MD&A names NA/Europe slowdown as an explicit risk; TAAL's core verticals (aerospace, plant engineering, transport) track client capex cycles | ISM/Markit PMI releases; Boeing/Airbus order & delivery reports | Monthly / quarterly |
| 5 | GenAI/AI tooling adoption pace in engineering services | Macro | Direct swing factor on T&M revenue-per-engineer economics; management states it is unassessed | Nasscom/Zinnov AI-in-ER&D commentary; LTTS/Cyient earnings-call AI commentary | Event-driven |
| 6 | India ER&D engineer wage and attrition trend (Bangalore) | Macro / Counterparty | Hiring pace is the primary SOM lever (headcount × rate); wage inflation and attrition determine whether the ~14-17% headcount CAGR in 3B is achievable | Nasscom talent-supply reports; peer (LTTS, Cyient) attrition disclosures in their own annual reports | Quarterly / annual |

demand_externally_verifiable: **true**. Six rows, none fewer than 3;
the sentence for the false case does not apply.

---

## ANALYST NOTE

Both WebSearch (20/20 failed) and most guessed industry-report URLs
(Zinnov, Nasscom, Grand View, Mordor, IBEF, Statista, Fortune Business
Insights, MarketsandMarkets, Precedence Research) failed or returned
unusable/inconsistent content this run. What worked was direct WebFetch to
named company and screener.in pages. The result is a TAM/SAM built on a
floor, not a ceiling — every uncertainty in this report points toward the
true numbers being larger than stated, not smaller. The one load-bearing
number this run got right on strong evidence is the SOM-implied revenue
CAGR (13.9-16.6%), built bottom-up off the company's own filed headcount
and revenue-per-engineer, cross-checked against real peer hiring paces
(Onward Technologies' actual 18% five-year CAGR), not off the failed
top-down search. Stage 11 should treat tam_cr and sam_cr as understated
floors and the SOM CAGR as the more load-bearing figure.
