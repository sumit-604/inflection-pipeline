# HALT 1 UNDERSTANDING DOSSIER — Indo Borax & Chemicals Ltd (INDOBORAX)

Run date: 2026-08-30 | Corpus commit: 9f2e03657fb0eb078d57d640d1ca162d844ad062

This dossier assembles what the pipeline has read. It states no price, no
multiple, and no action. It is the document the operator reads before
signing the Mental Model Declaration and choosing a path at Halt 1.

Three flag-type tags sit open in the committed blocks: FLAG-PROMOTER (B08,
verdict CONCERN), FLAG-CASH (B01/B03, treasury-reclassification distortion
in reported cash flow), and FLAG-GATE0 (B01, matrix-computed classification
overridden by a deal-breaker). B12/confidence.yaml records an overall
verifier-confidence score of 64, inside the 60-74 band the framework treats
as a trigger for a one-level downgrade on any later gate step. This dossier
does not itself apply that downgrade or name a gate outcome; it only carries
the fact forward for the operator.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** One transcript held: the Q4 & FY26 call, dated 02-Jun-2026
(B00 inventory `concalls: 1`; B05). Most recent quarter covered by a
transcript: Q4 FY26 (quarter ended 31-Mar-2026). The run date is
30-Aug-2026. A results filing for Q1 FY27 (quarter ended 30-Jun-2026) is
already in the corpus, so a Q1 FY27 concall has plausibly occurred and its
transcript is absent (B00 `freshness_pairs`, pair `RESULTS_to_CONCALL`,
status FAIL).

**2. Annual reports.** One AR held: FY2025-26, year ended 31-Mar-2026, 45th
AGM (filename carries a legacy "2023" label; content confirms FY26, B01/B03).
The latest completed FY is present. Fewer than three years of AR narrative
history are held (B00 `input_gaps: annual_report_fy24_fy25`); ten years of
numeric screener history exist back to FY17, but AR-level notes and
narrative depth run only one year deep.

**3. Results filings.** Two held: Q4/FY26 audited standalone and
consolidated results (period ended 31-Mar-2026) and Q1 FY27 unaudited
results (period ended 30-Jun-2026), the latter the most recent document in
the corpus (B00 inventory `results: 2`). No quarter-gap sits between the
latest results filing and the latest AR; the AR (filed 21-May-2026) predates
Q1 FY27 by construction.

**4. Investor presentations.** One held, Q4 FY26 (B00 inventory
`presentation: 1`). No later one is in corpus.

**5. Research / rating.** One rating action report held: India Ratings,
23-Jul-2026, assigning IND BBB+/Stable to bank loan facilities (rating.pdf;
B01). No independent broker research note is held (B00 `research: 0`,
severity NONE — the orchestrator records no anchored-evidence effect from
this absence at this company's size).

**6. Corporate actions.** Three announcements held, spanning 04-May-2026 to
20-Aug-2026 (B00 inventory `announcements: 3`): the Zenrock open offer post
advertisement (IIFL Capital, 04-May-2026) and the Kronox Lab Sciences SPA
board outcome plus press release (both 20-Aug-2026).

**7. Freshness pair check** (B00 `freshness_pairs`):
- RESULTS_to_CONCALL: **FAIL**. Trigger document: Q1 FY27 results (quarter
  ended 30-Jun-2026). Missing mate: Q1 FY27 concall transcript, if one was
  held.
- RATING_BULLETIN_to_RATIONALE: PASS. rating.pdf carries the full rationale
  alongside the rating action.
- SEBI_ORDER_to_ORDER_TEXT: PASS (n/a — no SEBI order referenced anywhere in
  the corpus).
- AR_to_LATEST_AUDITED_ANNUAL: PASS. The FY26 AR is not older than the FY26
  audited results it accompanies.

**8. VERDICT LINE: CORPUS GAPPED-FRESHNESS** (B00 `freshness_verdict`).
One pair failed: the newest results filing (Q1 FY27) has no matching
same-quarter concall transcript in the corpus. Per the orchestrator's own
Freshness Pair Check rule, a failed pair of this kind sets a floor under
any later gate step that a plain CORPUS GAPPED verdict would not set, and
this verdict line is never softened to a plain CORPUS GAPPED once a pair
has failed. This dossier does not itself name that floor or any gate
outcome; it states only that the mechanism exists and which document is
missing.

Other corpus gaps, carried under this verdict, all findable-but-missing
(not evidence the company declines to file such documents):
- **AR FY24 and FY25** — expected source: BSE / company IR page. Effect:
  limits capex, free-cash-flow and working-capital-day trend analysis to a
  two-year window (B01 Block B), and blocks independent multi-year
  confirmation of several spear facts.
- **Postal-ballot notices** — the Section 186 Rs 700 cr borrowing-limit
  ballot (08-Apr/12-May-2026) and the ESOP 2026 ballot (16,88,950 options,
  08-May-2026) — expected source: BSE. Effect: company-memory priority
  claims 3 ("Kronox funding, Rs246/397 cr"), 4 (Section 186 envelope) and 5
  (ESOP count, size confirmed but ballot voting margin not) stay
  filing-unconfirmed this run (B00 `priority_claims_status`).
- **Reg 31 shareholding filing** — expected source: BSE/NSE. Effect: the
  exact current sub-classification of the 38.41% promoter line into
  Zenrock's own stake versus the three co-acquirer AIFs, and the exact
  current pledge share count, are inferred by arithmetic reconciliation
  from the AR and the screener aggregate (B01 Block E1), not read directly
  off the filing itself.

**Priority claims lifted to filed tier this run** (B00
`priority_claims_status`): claim 1 (Kronox SPA terms), claim 2 (Kronox
consequential open offer), claim 6 (Zenrock open offer, May-2026), claim 9
(Q4 FY26 exceptional-item split), and claim 10 (FY26 closing cash before the
dividend payment, partially — the post-payment position is not in corpus).
**Claims remaining SECONDARY for claude.ai**: claim 3 (Kronox funding
structure), claim 4 (Section 186 Rs 700 cr envelope), and claim 5 (ESOP
voting margin — the option count itself is filed, AR p.34). Claims 7
(pledge count) and 8 (promoter sub-classification) are partial: the
aggregate and the rating-agency figure are filed, the exact Reg 31 split is
not.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing below is signed. Signing
happens only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE

**A1. Archetype.** Single reportable segment, boron chemicals manufacturing
(B03 Phase 4C: "single reportable segment... no segment-level disclosure
required or given"). Archetype: **Commodity converter** (Section 1B v3.7
Amendment 17 binds this archetype at later valuation stages; no valuation is
done here). Anchors: B04 classifies `asset_intensity: light`,
`wc_intensity: high`, `pricing_power: moderate`, `cyclicality: cyclical`,
with the one-line verdict "Domestic near-monopoly ore-pass-through business
now mid ownership transition." B01 Block F finds moat class THIN (4/60
points; only M3 Capital Efficiency scores as present; M7 Regulatory/Licence
scores 0 PEER DATA NEEDED, not present, despite the company's sole-India
IP-grade licence position). rating.pdf p.3 shows spread economics directly:
EBITDA per tonne fell from ~INR30,680/MT (FY25) to ~INR26,130/MT (FY26) as
raw-material consumption cost per tonne rose from INR54,762/MT to
INR67,187/MT, a cost-pass-through-lag pattern, not a price-setting one.

**A2. The simple analogy.** Indo Borax buys boron ore from abroad —
Turkey, South America, North America — because India has none of its own
(B03 Phase 4A). It cooks the ore into boric acid at one factory in
Pithampur, Madhya Pradesh, and sells most of it to steel and refractory
makers, who use a small amount in every batch of furnace lining (concall,
Suresh Kalra, transcript p.16-17: "it is used in a very single-digit
percentage of the total product... the input cost versus the benefit they
get is completely in their favor"). It holds close to half the domestic
market for this one product (rating.pdf p.2) and near-monopoly status in a
higher-grade version used in pharma and personal care (sole India IP-grade
FDA-licensed manufacturer). For forty years one family, the Jains, owned
and ran it. In the last eight months a new family-backed sponsor bought
control, brought in professional managers, and is now trying to place more
of two smaller, higher-priced products — DOT (a fertiliser input) and Boron
Oxide (a still-uncommissioned product) — instead of just the one it has
always made.

### PART B — THE TRANSITION

**B1. FROM to TO.** FROM **R2 COST-ADVANTAGED CONVERTER** (mid-teens ROCE,
17.13% FY26 / 17.28% FY25, AR p.113 Note 45; margin moves with the ore-cost
cycle, B04). TO claimed **R3 VALUE-ADDED / SPEC'D SUPPLIER** — management's
stated direction is a mix-shift toward higher-realisation, spec'd boron
derivatives. Boron Oxide is priced "almost 2.5x to 3x of the price of Boric
Acid in general now" (Suresh Kalra, concall transcript p.8), and DOT already
carries a realisation premium (~Rs150/kg per Kalra, transcript p.18-19, vs
~Rs127-128/kg blended boric-acid realisation, Shashikant Bharuka, transcript
p.17). No number or conclusion on whether this migration is already priced
is stated here (see B4).

**B2. The engine.** Two things must physically change: (1) a product-mix
shift funded from the company's own debt-free balance sheet — Boric Acid
debottlenecking (+1,000-1,500 tonnes toward the 20,000 MTPA nameplate,
Kalra transcript p.5-6), a DOT volume ramp (980t FY26 to a stated 1,500t
FY27 target, transcript p.5, p.19), and a still-uncommitted Boron Oxide
facility. rating.pdf p.2 gives the only rupee-anchored capex figure in the
corpus for this: "the company plans to undertake a capex of around INR900
million over FY27-FY28, which would be funded entirely through internal
accruals. Of the total capex, around INR200 million has been earmarked for
setting up a 4,000 MT boron oxide capacity, and the balance is proposed for
establishing an additional 10,000 MT boric acid capacity. **Commercial
operations from the proposed facilities are expected to commence from
FY29.**" (2) Replacement of the 40-year Jain family promoter-operator with
a professional CEO (Suresh Kalra) and CFO, under a sponsor (Zenrock)
co-invested by three EAAA/Edelweiss AIFs (B08). **Material qualifier found
this run**: Zenrock itself is beneficially owned by the Malhotra family —
Sunil Malhotra, Non-Executive Director, is categorised as Promoter in the
AR's own skills-matrix table and is the disclosed beneficial owner of
Zenrock's entire Indo Borax shareholding; his son Harsh Malhotra is
Executive Director (AR p.45-46; B03 Phase 5A). The engine therefore
replaces one family-operator structure with a professionally-managed but
still family-beneficially-owned sponsor, layered with genuine institutional
co-investment (the three AIFs) — not a clean family-to-institution
transition.

**B3. The proof gate.** Exact metric and threshold: Boron Oxide capital
work-in-progress — currently frozen at Rs 112.52 lakh, an unrelated stale
residential-flat purchase advance (AR Note 2; B03 Phase 2A/6E) — must show
a new CWIP line greater than Rs 100 lakh tagged to the project, followed by
first commercial dispatch (B07 optionality register). **This run surfaces
a live, previously-unresolved conflict inside the corpus on the timing of
this gate**: on the 02-Jun-2026 call, Suresh Kalra states Boron Oxide will
see its "first lot in three to four quarters from now" (transcript p.8,
implying roughly Q4 FY27-Q1 FY28), while rating.pdf p.2 — dated seven weeks
later, 23-Jul-2026, and citing the same management as its source — states
"Commercial operations from the proposed facilities are expected to
commence from FY29." Until new CWIP appears in a filed balance sheet, the
gate has not fired under either timeline.

**B4. The recognition gap (open question, resolved at Stage 11).** Whether
the market's current pricing already reflects the claimed TO state — a
diversified, professionally-run, higher-margin boron-derivatives business —
or still prices the FROM state — a single-product, ore-pass-through
converter mid ownership transition — is not concluded here. Stage 11
resolves this via the Section 1B destination-multiple gap. If the TO state
is already priced, the re-rating component of any later valuation work is
absent and only earnings growth would remain relevant; this dossier states
no number either way.

**B5. The ugliness test.** Classification: **ARTIFACT-OF-CLIMB, with one
open sub-question.** Evidence for artifact: the Rs 62.02 cr non-arm's-length
asset sale and leaseback to the exiting Jain family (AR AOC-2, p.42; B08
Section 3A) and the 100% Zenrock share pledge (rating.pdf p.1, p.3-4) are
both features of the ownership handover itself, not of the underlying
factory economics. The pledge secures acquisition-level debt already
reduced by roughly 35% in its first year (Rs 390 cr to Rs 255 cr NCD
principal, rating.pdf p.4), and the RPT cluster was a one-time,
board-and-shareholder-approved clearing of legacy family claims ahead of
the sale of control (B08 Section 3A). **Open sub-question**: standalone PBT
before the Rs 10.15 cr exceptional item fell 3.75% year-over-year (AR P&L
face; B03 Phase 3C), driven by raw-material cost growing 39.74% against
22.93% revenue growth — a margin-compression pattern that predates and is
independent of the ownership transition. Three unrelated peers (DMCC,
Tanfac, Tata Chemicals) report a similar Middle-East-linked input-cost
squeeze in the same window (B06), which supports an external, not
company-specific, reading — but if this pattern persists past FY27
independent of any ore-cost normalisation, the classification should move
to STRUCTURAL-FEATURE.

**B6. The transition falsifier.** The transition thesis (not the business
itself — see C3) fails if, by the FY28 AR: (a) no Boron Oxide CWIP or first
dispatch has appeared under either the concall or the rating-agency
timeline (B03 monitorables; B07); AND (b) DOT volume has not cleared
roughly 1,400 tonnes (B05 kill_signal); AND (c) a new related-party or
inter-corporate-deposit transaction naming a Malhotra-family or
Zenrock-linked entity appears, repeating the extraction pattern of the
departed Jain family (B03 monitorables; B08 Section 6D) — this last item
would falsify specifically the professionalisation reading of the control
change, independent of whether the product-mix engine itself succeeds.

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2/B3):
1. **Boron Oxide capex-to-CWIP-to-dispatch conversion.** Current state:
   zero CWIP tagged to the project as at FY26 close; two conflicting
   verbal/rating-agency timelines, neither yet evidenced in a filing (B07,
   B03, rating.pdf p.2).
2. **Raw-material cost as a share of revenue / pre-exceptional margin
   trajectory.** Current state: raw-material consumption cost grew 39.74%
   against 22.93% revenue growth in FY26; pre-exceptional PBT fell 3.75%
   year-over-year (B03 Phase 3C).
3. **DOT volume ramp toward the stated FY27 goal.** Current state: 980
   tonnes FY26 versus 600 tonnes two years prior; management states a
   goal of "increasing 50% of the business in a year's time" (Kalra,
   transcript p.20).
4. **New related-party or inter-corporate-deposit activity involving
   Malhotra-family or Zenrock-linked entities.** Current state: none
   disclosed in the FY26 AR ("no RPT with Zenrock disclosed anywhere in
   Note 40," B03 Phase 2B).

**C2. What the model rejects.** (a) India boric-acid total-addressable-
market sizing debates (the ~38-40kt to ~53kt-by-2030, ~50%-share claims).
B09's own bottom-up SOM shows the anchored, capacity-constrained growth
path implies only a ~7% revenue CAGR over three to five years, far below
management's stated 20-35% FY27 growth guide — and B09's `capacity_check`
already confirms existing nameplate capacity is sufficient for that SOM
without the unproven Boron Oxide capex. The binding constraint this model
tracks is capex-and-execution conversion, not market headroom. (b)
Named-competitor market-share verification. No true product-overlap peer
exists in the transcript set the pipeline could check this against (B06);
it remains a standing research item (Section 4d), not a variable this
model tracks quarter to quarter.

**C3. The business falsifier** (distinct from B6 — kills the FROM business
itself, not just the climb). Any of: (a) loss of the sole-India IP-grade
FDA licence or the BIS technical-grade certification that anchors the
FROM archetype's niche position (rating.pdf p.2); (b) a second unprovided
or impaired treasury exposure surfacing in FY27 alongside the Radius
Estates inter-corporate deposit (Rs 509.04 lakh, unprovided principal,
auditor Emphasis of Matter, AR p.72/113) — evidence of a systemic treasury
control failure rather than one legacy misjudgment; (c) raw-material cost
structurally and permanently outgrowing realisation, not cyclically,
pushing clean operating EBITDA margin below 20% for multiple consecutive
years (B04 `must_track_metrics` red-flag threshold) — converting the
business from a cost-advantaged converter into an unprotected price-taker.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

**What the products are and why they matter.** Indo Borax makes boron-based
chemicals at one factory in Pithampur, Madhya Pradesh: boric acid
(technical grade and a higher Indian Pharmacopoeia grade), borax, and DOT
(disodium octaborate tetrahydrate). Boric acid is the main product, roughly
90% of current volume (Kalra, transcript p.5). In steel and refractory
manufacturing, it goes into ramming mass and furnace linings, where it acts
as a heat-resistant bonding agent used in a very small dose per batch but
with a large effect on product quality (Kalra, transcript p.16-17;
rating.pdf p.2). The IP grade goes into pharmaceutical, personal-care and
FMCG applications, where the company is the sole India-based FDA-licensed
manufacturer (rating.pdf p.2). DOT is a micronutrient fertiliser input used
in fruit, vegetable, and tea cultivation (Kalra, transcript p.18-19).

**Who buys and why.** The customer base sits mainly in steel and
refractory manufacturing, concentrated in West Bengal, Rajasthan, and
Maharashtra (AR MD&A, p.70; B03 Phase 4B), with no percentage breakdown or
top-customer disclosure filed anywhere in the AR. Management describes the
top 10-15 customers as stable "for many years," with only two rank changes
inside that group, which it attributes to the product's technical
specification: "your product has the best technical specifications... the
input cost versus the benefits they get is completely in their favor"
(Kalra, transcript p.16-17). Procter & Gamble is named as an existing
Boric Acid IP-grade customer and a candidate for cross-selling new
applications (Kalra, transcript p.18) — a single named customer relationship,
not independently corroborated in this corpus.

**Why demand exists.** Boron chemistry has no domestic ore substitute in
India; every steel and refractory producer that needs this input must
procure finished boric acid from a manufacturer, since India holds no
commercially viable boron ore reserves (AR MD&A p.69; B03 Phase 4A). Indo
Borax holds roughly half the domestic market for the steel/refractory grade
(rating.pdf p.2) and, in the IP grade, faces no other India-based
FDA-licensed manufacturer that the corpus names. Demand is therefore
structurally tied to India's own steel, refractory, ceramics,
pharmaceutical, and agricultural output, none of which the company
controls.

**Why demand grows or does not.** Revenue grew 22.93% in FY26 (AR P&L
face), but the growth mix is unclear from the filed evidence: management
attributes it to "a mix of volume growth as well as the better price
realisations" (Bharuka, transcript p.17), and rating.pdf p.2 confirms both
legs moved together — boric acid volumes rose from 14,296 MT (FY25) to
15,365 MT (FY26) and blended realisation rose from ~INR117,168/MT to
~INR127,488/MT. Growth beyond debottlenecking (an incremental 1,000-1,500
tonnes) and the DOT ramp depends on two forward levers that are not yet
evidenced in a filing: Boron Oxide (no CWIP as at FY26 close) and export
markets (zero export revenue in both FY25 and FY26, AR p.33). B09's own
addressable-market analysis finds that even the anchored, capacity-limited
growth path implies roughly 7% revenue CAGR, well short of management's
stated 20-35% FY27 growth guide — a gap the guide itself attributes to
realisation and new products, not market-share capture.

**Where the competitive advantage sits, and where it does not.** The
advantage that is filed and specific: a sole-India FDA licence for
IP-grade boric acid, BIS certification for technical grade, roughly 45
years of operating history, and customer relationships management
describes as sticky on technical-specification grounds (rating.pdf p.2;
Kalra, transcript p.16-17). The advantage that is claimed but not yet
filed: pricing power beyond a pass-through lag. Clean operating EBITDA
margin swung from 26.18% (FY25) to 20.50% (FY26) on rising raw-material
cost per tonne (rating.pdf p.3-4), and standalone pre-exceptional PBT fell
3.75% year-over-year despite double-digit revenue growth (B03 Phase 3C) —
evidence of a cost-position advantage during favourable cost cycles, not
yet evidence of a price-setting advantage that survives an unfavourable
one. B01's own moat scorecard finds only one of twelve quantitative moat
tests present (Capital Efficiency), with the licence test itself scored
zero for lack of a counted peer figure, not for lack of qualitative
strength.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1 — Boron Oxide capex conversion.** The corpus establishes: a
management-stated intent (Rs 20 cr / 4,000 MTPA, MD&CEO letter, AR p.2), a
rating-agency-sourced rupee figure and date (Rs 90 cr FY27-28 total capex,
FY29 commercial-operations start, rating.pdf p.2), and zero matching CWIP
or PP&E movement as at FY26 close (AR Note 1/2; B03 Phase 6E). It cannot
establish: whether a board resolution or capital commitment yet exists
behind either figure, or which of the two conflicting timelines (concall
"three to four quarters" vs rating-agency FY29) management itself now
holds. Deciding questions: (1) Does a board-approved capex resolution with
a named rupee figure appear in an FY27 filing? (2) Does a CWIP line
tagged to this project appear in any quarterly balance sheet before FY29?
(3) Which of the two conflicting timelines does management repeat on the
next call?

**Vertical 2 — Raw-material cost / pre-exceptional margin.** The corpus
establishes: raw-material cost grew 39.74% against 22.93% revenue growth
in FY26, EBITDA per tonne fell from ~INR30,680/MT to ~INR26,130/MT, and
management states an expectation of 20-22% EBITDA margin "over the medium
term" (rating.pdf p.2-3; Kalra, transcript p.7). It cannot establish:
whether the FY26 compression is a one-year cost-inflation event (as three
unrelated peers also report in the same window, B06) or the start of a
structural pattern, since only a two-year trend is in corpus. Deciding
questions: (1) Does clean operating EBITDA margin recover toward the FY25
level (26.2%) or stabilise permanently near or below the FY26 level
(20.5%)? (2) Does the ore-cost pass-through lag shorten or lengthen? (3)
Does the company disclose any hedging or multi-sourcing policy beyond the
generic "monitoring foreign currency exposure" language (AR MD&A, p.69)?

**Vertical 3 — DOT volume ramp.** The corpus establishes: 980 tonnes FY26
volume (up from 600 tonnes two years prior, out of 6,000 MTPA nameplate),
a stated FY27 goal of 1,500 tonnes, and a current realisation of
~Rs150/kg (Kalra, transcript p.5, p.18-19). It cannot establish: whether a
named fertiliser-company distribution tie-up exists — management describes
only "a tie-up with the fertiliser company" and "we got benefit in price
and quality" without naming the counterparty (Bharuka, transcript p.19) —
or why a multi-year pattern of slow ramp (600 to 980 tonnes) should
suddenly accelerate to 1,500 tonnes. Deciding questions: (1) Does a named
counterparty or supply-volume disclosure appear in an FY27 filing? (2)
Does FY27 AR-reported DOT volume clear 1,400 tonnes? (3) Does DOT
realisation move materially from the ~Rs150/kg level management describes
as still being learned ("we are trying to learn more and try to see if
this realisation is correct," Kalra, transcript p.19)?

**Vertical 4 — New RPT/ICD activity with Malhotra-family or Zenrock-linked
entities.** The corpus establishes: none disclosed in the FY26 AR (B03
Phase 2B), and a clean legal/regulatory record for every named individual
in the incoming group (B08 Section 2). It cannot establish: whether the
absence continues once the new control group has a full year's operating
history, since the FY26 AR covers only a two-month stub of the new
ownership (23-Jan-2026 to 31-Mar-2026). Deciding questions: (1) Does the
half-yearly Reg 23 RPT filing or the FY27 AR Note 40 name any Malhotra-
family or Zenrock-linked counterparty? (2) Does the Rs 330 lakh commission
still payable to the departed MD (Sajal Jain) clear on the disclosed
post-AGM timeline? (3) Does the sale-leaseback rent to the departing family
escalate at the disclosed 5% per annum rate?

### 4b. Candidate signal table (expanding each B09 candidate)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| India steel & refractory production/capex (B09) | Sustained (2+ quarter) decline in JPC steel/refractory output with no offsetting realisation gain would undercut the 55-60% end-use demand link | Monthly | Ministry of Steel / Joint Plant Committee (JPC) production statistics |
| Eti Maden (Turkey) ore supply and pricing (B09) | A second Turkey-sourced disruption within 12 months, with no disclosed diversification, would falsify the resilience this run found relative to peer DMCC's own reported disruption | Quarterly | Eti Maden corporate disclosures / Turkish Ministry of Trade export data |
| DGCIS India boric acid & DOT import-export volumes (B09) | Import volumes rising faster than Indo Borax's own realisation-adjusted revenue would undercut the ~50%-share / import-substitution claim | Monthly | DGCIS (Ministry of Commerce) trade data portal |
| Kronox Lab Sciences Ltd standalone filings (B09) | SPA lapses or fails to complete within the disclosed "within 3 months of public announcement" indicative window, with no amended timeline filed | Quarterly | BSE/NSE corporate filings, Kronox quarterly results |
| SEBI/BSE Reg 30 and SAST filings — Indo Borax/Zenrock/Kronox (B09) | Delay, withdrawal, or amended consideration terms on the mandatory Kronox open offer, without a filed amendment | Event-driven | BSE/NSE Reg 30 & SAST filings |
| Unnamed fertiliser-company DOT tie-up (B09) | No named counterparty or supply-volume disclosure appears within FY27 despite the concall reference | Event-driven | Indo Borax's own Reg 30 disclosures (no independent named source found) |

**Additional candidates surfaced elsewhere in the evidence base, beyond
B09** (not counted in the B09 candidate total, carried for completeness):
Radius Estates NCLT resolution (further provisioning/write-off vs recovery,
event-driven, NCLT cause list / FY27 AR Note 6-47, B03); Boron Oxide
CWIP/capex disclosure (FY28 AR still showing no tagged CWIP, quarterly, FY27
results / AR Note 2, B07); new RPT/ICD activity with Zenrock-linked
entities (any new RPT naming such an entity within 24 months, event-driven,
Reg 23 filings / FY27 AR Note 40, B03/B08); sale-leaseback rent escalation
(escalation not applied at the disclosed 5% p.a. rate, annual, FY27 AR Note
40, B03); commission payable to Sajal Jain (payment date/amount diverging
from the disclosed Rs 330 lakh, event-driven, Q1/Q2 FY27 cash flow, B03).

### 4c. Fragility read

- **variable_count**: 5 — Boron Oxide capex conversion; raw-material
  cost/margin trajectory; DOT volume ramp; new-RPT non-repeat; export
  market entry (the longer-dated fifth lever named in B05/B07, held
  separate from the four C1 dominant variables because its own proof gate
  runs on a longer horizon).
- **verifiability_ratio**: "2 of 5 externally observable" — ore-import and
  steel-end-use data are checkable against DGCIS/JPC third-party trade and
  production statistics; the remaining three (Boron Oxide conversion, DOT
  ramp, RPT non-repeat) are verifiable only through the company's own
  subsequent filings, not an independent third-party source.
- **single_point_failure**: raw-material cost structurally outgrowing
  revenue. Standalone pre-exceptional PBT already fell 3.75% year-over-year
  on this driver alone (B03 Phase 3C); a continuation would erode the
  earnings base any product-mix transition is built on, independent of
  whether Boron Oxide or DOT succeed on their own terms.
- **fragility_verdict**: **FRAGILE**. Three of five variables are
  company-narrated only, one named single-point-failure exists, and the
  corpus already carries an unresolved timeline contradiction (concall
  "three to four quarters" vs rating.pdf "FY29") on the most capital-
  intensive lever.

### 4d. Research brief (live-web work the corpus cannot do)

1. Verify the India boric-acid TAM claim (38-40kt to ~53kt by 2030, 7-8%
   CAGR) against a named CRISIL/ICRA/Mordor/IMARC study; B09's own figure
   traces only to unnamed "reports."
2. Verify the ~50% boric-acid market-share claim and size the remaining
   ~50% by named competitor (B06 found no true product-overlap peer in the
   transcript set used this run).
3. Confirm whether Indo Borax's own H1 FY26/CY2025 ore deliveries were
   affected by the same Turkey-distributor disruption peer DMCC reports,
   and if not, why its supply chain proved more resilient (B06 analyst
   note, explicit ask).
4. Retrieve the postal-ballot notices (Section 186 Rs 700 cr limit,
   08-Apr/12-May-2026; ESOP 2026, 08-May-2026) to confirm voting margins
   and any minority dissent.
5. Retrieve the Reg 31 shareholding filing for the exact current
   Zenrock-versus-three-AIF sub-classification and the latest pledge count.
6. Cross-check DGCIS import/export volumes and JPC steel-production data
   against the ore-import-dependency and steel-demand-link assumptions.
7. Track Kronox Lab Sciences SPA completion against its disclosed
   "within 3 months of public announcement" indicative window (Kronox SPA
   Annexure A, 20-Aug-2026).
8. Independently verify the named Procter & Gamble Boric Acid I.P.-grade
   relationship, cited only in management's own concall remarks.
9. Verify whether a named fertiliser-company DOT tie-up exists; management
   names no counterparty on the call.
10. Search for independent proxy-advisory commentary (IiAS/InGovern/SES) on
    the RPT sale-leaseback and the Rs 256.30/Rs 157.27 open-offer pricing;
    B08's search located none.
11. Resolve the Boron Oxide commercialisation-date conflict between the
    concall's "three to four quarters" claim and rating.pdf's FY29
    commercial-operations date, both sourced to the same management.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Indo Borax makes boron chemicals — mainly boric acid — at one factory
   in Pithampur, Madhya Pradesh. It has run since 1980.
2. The company imports almost all its raw ore. India has no boron ore of
   its own.
3. It also makes DOT, a fertiliser input, and is trying to start Boron
   Oxide, a new higher-priced product that has not yet shipped.
4. Steel and refractory makers use most of the boric acid. They use it in
   furnace linings, in a small dose that still matters a lot to quality.
5. A smaller, higher grade goes to pharma and personal-care makers. Indo
   Borax is the only India-based maker with the FDA licence for this grade.
6. The top 10 to 15 customers have stayed the same for years, which
   management reads as evidence the product is hard to switch away from.
7. Demand grows when Indian steel, refractory, and pharma output grows.
   The company does not control any of those industries.
8. Revenue grew 23% last year. Raw-material cost grew faster, 40%, so the
   profit made before a one-time gain actually fell.
9. The one-time gain came from company property sold to the family that
   used to run the firm, right before that family gave up its shares.
10. A new owner, Zenrock, took control in December 2025. Zenrock is itself
    owned by another family, the Malhotras, with a professional CEO hired
    to run daily operations.
11. The mental model here is a climb: from a single-product, ore-price-
    driven business to a business with more higher-priced boron products,
    run by professional managers instead of the founding family.
12. That climb has not yet shown up in the numbers that would prove it: no
    new spending on the Boron Oxide plant has appeared in the accounts yet.
13. This reading is fragile. Several of the things that must go right can
    only be checked once the company itself files new figures. No
    independent source can check most of them yet.
14. The corpus available for this run does not include the last two years
    of annual reports, or the shareholder-vote notices for the new
    borrowing limit and employee share plan.
15. The biggest open questions: which timeline for the new Boron Oxide
    product is real, and whether the company that transferred assets to
    the old owning family will do anything similar with the new one.

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. UNITS

> "Boric acid sales volumes increased to around 15,365 MT in FY26 (FY25:
> 14,296 MT), while realisations improved to around INR127,749/MT
> (INR115,874/MT)." — rating.pdf, p.2, India Ratings, 23-Jul-2026.

> "The company also witnessed an increase in DOT volumes to around 983 MT
> in FY26 (FY25: 679 MT), supported by improved product acceptance and
> realisations. Consequently, blended realisations improved to around
> INR127,488/MT in FY26 (FY25: INR117,168/MT)." — rating.pdf, p.2.

> "IBCL's EBITDA/t declined to around INR26,130/metric tonnes (MT)" and
> "the increase in raw material consumption cost per tonne to around
> INR67,187/MT in FY26 (FY25: INR54,762/MT)" — rating.pdf, p.3.

> "Yes, EBITDA per Kg would be about Rs.28-29 and I would say
> percentage-wise, it should be 20%-21%." — Suresh Kalra, Concall_Jun_2026
> Transcript, p.7.

> "we are getting around Rs.127 to Rs.128 per Kg in this year as compared
> to last year of Rs.114 and Rs.115." — Shashikant Bharuka,
> Concall_Jun_2026 Transcript, p.17.

> "what we have is about Rs.150 a kilo of this product [DOT]." — Suresh
> Kalra, Concall_Jun_2026 Transcript, p.19.

Comment: these are the only per-unit figures printed anywhere in the
corpus; the AR and Investor Presentation carry no tonnes-sold or
rupee-per-kg line (B04 `input_gaps`). All figures cover a single product
(boric acid) or DOT specifically, except the rating-agency "blended
realisation" figure, which is a basket across boric acid and DOT (rating.pdf
p.2, "blended realisation"). No per-unit figure exists for Boron Oxide,
which has not yet shipped.

### 2. SEGMENT CAPITAL AND DEBT

> "Segment analysis: single reportable segment (Boron products/Chemical
> Manufacturing); no segment-level disclosure required or given." — 03-
> ardeep.md, Phase 4C (paraphrasing the AR's own segment note; the AR
> itself, per Ind AS 108, states no reportable-segment split is required
> for a single-segment entity).

> "Total Borrowings: Nil" both years — AR, Note 43(D) Interest Rate Risk
> table, per 03-ardeep.md Phase 2F.

Comment: Indo Borax discloses one reportable segment. No segment-level
assets, liabilities, capital employed, or borrowings split exists, because
none is required under Ind AS 108 for a single-segment filer. Total company
borrowings are Nil in both FY25 and FY26 (AR Balance Sheet, p.84). The
100% pledge disclosed by the rating agency (rating.pdf p.1, p.3-4) sits at
the level of the acquirer entity (Zenrock), not as a company-level or
segment-level liability, and is not disclosed anywhere in the AR itself
(B03 Phase 5D: "NOT FOUND IN DOCUMENT" as an AR-level disclosure).

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a period:
> "we would easily be doing 25% to 30% more in the coming one and a half
> years or so... it can be anywhere between 20% to 35%, depending on the
> raw material inflation." — Suresh Kalra, Concall_Jun_2026 Transcript,
> p.6 (FY27 revenue growth guide).
> "It is close to 21%-22% in the last couple of quarters and we are
> confident of maintaining that or surpassing." — Suresh Kalra, transcript,
> p.7 (FY27 EBITDA margin guide).
> "we are planning to do about 1,500 tons of that product [DOT]." — Suresh
> Kalra, transcript, p.5 (FY27 DOT volume guide).
> "the company plans to undertake a capex of around INR900 million over
> FY27-FY28... Commercial operations from the proposed facilities are
> expected to commence from FY29." — rating.pdf, p.2 (a rating-agency-
> sourced, management-attributed figure, with a period; not stated in this
> form in the AR or on the concall itself).

(b) Aspiration without a period:
> "we are open to it" [entering non-boron chemistry] — Suresh Kalra,
> transcript, p.15.
> "we will increase our investment in research and development to create
> specialised boron-based solutions" — MD&CEO letter, AR p.2 (contradicted
> by AR p.33's own Technology Absorption disclosure, per B03 Phase 6E).
> "we will expand our international footprint, with a particular focus on
> opportunities across South America and South-East Asia" — MD&CEO letter,
> AR p.2 (export revenue Nil both years, no base to expand from).

(c) Capacity or capability only:
> "We are expecting that we will be able to kind of getting our first lot
> in three to four quarters from now [Boron Oxide]." — Suresh Kalra,
> transcript, p.8 — a capability/timeline statement with no capex rupee
> figure attached on the call itself ("details of these will be shared
> post board approval," transcript p.2-3).
> "Boric Acid is fully utilised... it will still be sold out in that
> category" — Suresh Kalra, transcript, p.5 (capacity statement, no
> forward number beyond the +1,000-1,500 tonne debottlenecking range).

Comment: the FY27 revenue and margin guides are the clearest true guidance
in the corpus, both period-bound and reaffirmed to a second questioner
later on the same call (B05). The Rs 900 million/FY29 capex figure is the
single most specific forward number in the entire corpus, but it appears
only in the rating agency's report, not in the company's own AR or on its
own call — a provenance gap the operator should weigh.

### 4. CONCENTRATION

> "Our product is used in steel industry in a very small amount... the
> stickiness of our customer is very high. If you look at any of our
> customer list... the top 10 to 15 customers have been same for many
> years." — Suresh Kalra, Concall_Jun_2026 Transcript, p.16-17.

> "West Bengal, Rajasthan and Maharashtra" named as "key contributing
> markets" — AR MD&A, p.70, per 03-ardeep.md Phase 4B.

Comment: qualitative customer stickiness and a three-state geographic
concentration are disclosed; no percentage figure for top-customer share,
top-product share (beyond the 90%/8%/2% Boric Acid/DOT/other volume split
management gives verbally, transcript p.5), or top-geography share is
printed anywhere in the AR or Investor Presentation. Product concentration:
NOT DISCLOSED as a percentage of revenue (only a verbal volume split
exists). Customer concentration: NOT DISCLOSED as a percentage. Geographic
concentration: NOT DISCLOSED as a percentage.

### 5. PROMISE LEDGER

| Promise | Date made | Delivery status | Evidence anchor |
|---|---|---|---|
| FY27 revenue growth 20-35% | 02-Jun-2026 (concall) | Not yet due; no post-02-Jun-2026 concall in corpus to check against | Kalra, transcript p.6, p.24; B05 |
| FY27 EBITDA margin 20-22% | 02-Jun-2026 (concall) | Not yet due | Kalra, transcript p.7, p.24; B05 |
| DOT volume to 1,500t FY27 (from 980t) | 02-Jun-2026 (concall) | Not yet due | Kalra, transcript p.5, p.19; B05 |
| Boron Oxide first lot in 3-4 quarters from 02-Jun-2026 | 02-Jun-2026 (concall) | Not yet due by its own clock; conflicts with a FY29 date given by the same management to the rating agency seven weeks later | Kalra, transcript p.8; rating.pdf p.2 |
| Rs 20 cr / 4,000 MTPA Boron Oxide facility | 21-May-2026 (MD&CEO letter, AR) | Unproven as at FY26 close — zero matching CWIP or PP&E addition | AR p.2; B03 Phase 6E |
| Increased R&D investment | 21-May-2026 (MD&CEO letter, AR) | Contradicted in the same document | AR p.2 vs AR p.33; B03 Phase 6E |
| International expansion, South America/SE Asia | 21-May-2026 (MD&CEO letter, AR) | Unproven — zero export base in either FY25 or FY26 | AR p.2, p.33; B03 Phase 6E |

Comment: no promise in this ledger has reached a delivery date yet, since
only one concall exists in the corpus and no later results filing carries a
management commentary section to check against (B05 `promise_delivery`:
delivered 0, partial 0, missed 0 — structurally, not because performance
was clean).

### 6. RESTATED BASES

> "Screener CFO/PAT for FY25-FY26 are consolidated (verified exact match
> to AR consolidated P&L/CF... FY17-FY24 predate the subsidiary
> (IndoBorax Infrastructure Pvt Ltd, incorporated later) so
> standalone = consolidated for those years. Basis is continuous." —
> B01-gate0.yaml `data_notes`.

Comment: no restatement of prior-period comparatives for any
reorganisation, transfer, or reclassification is disclosed in the FY26 AR
(B02/B03 find no `restatements_found`, empty list). The only basis change
across the ten-year screener series is the natural appearance of a
subsidiary (Indoborax Infrastructure Pvt Ltd) partway through the window,
which does not restate any prior year, since standalone equalled
consolidated before the subsidiary existed.

### 7. CORPORATE-ACTION CLAUSES

**Deal 1 — INBOUND (Zenrock/EAAA acquired Indo Borax).**
> "Share Purchase Agreement dated 15-Dec-2025" in which "Zenrock Chemicals
> Pvt Ltd + India Special Assets Fund III + ISAF III Onshore Fund +
> Special Situation India Fund acquired 1,63,00,230 shares (50.80% of
> equity) from the erstwhile Jain-family promoter group, followed by an
> open offer for up to 83,43,400 shares (26.00%) of which 24,44,534 were
> actually tendered and acquired (04-May-2026)." — 01-gate0.md, quoting AR
> p.32, Note 49.

Comment: appointed date (SPA execution) 15-Dec-2025; effective date (board
reconstitution / change of control) 23-Jan-2026 (AR p.28); open-offer price
Rs 256.30/share; open-offer completion 04-May-2026, ~29% take-up of the
offer size. Ratio: acquired stake 50.80% (SPA) plus up to 26.00% (open
offer, ~9.3% points actually taken up).

**Deal 2 — OUTBOUND (Indo Borax acquiring Kronox Lab Sciences Ltd).**
> "The Board approved the execution of a share purchase agreement ('SPA')
> by and amongst the Company, the Sellers... and Zenrock Chemicals Private
> Limited ('ZCPL') for the acquisition of 2,38,44,000... equity shares...
> representing 64.26%... of the share capital of the Target Company...
> from the promoters of the Target Company, namely, Mr. Ketan Vinodchandra
> Ramani, Mr. Pritesh Vinodchandra Ramani and Mr. Jogindersingh Gianchand
> Jaswal... at a price of ₹103.22 per Sale Share, for an aggregate
> consideration of ₹246,11,77,680.00." — 2026-08-20_Board_Outcome_Kronox_
> SPA.pdf, p.1.

> "Since, pursuant to consummation of the SPA Transaction, the Company
> shall acquire control and voting rights in excess of 25%... the Company
> along with ZCPL... shall make a mandatory open offer... for acquisition
> of up to 95,70,000... equity shares... representing approximately
> 25.79%... at such offer price as may be determined in accordance with
> the SAST Regulations." — same filing, p.2.

> "The Open Offer is being made at ₹157.27... per Equity Share." — same
> filing, Annexure A, p.4.

> "Indicative time period for completion of the acquisition: Within 3
> (three) months of public announcement." — same filing, Annexure A, p.3.

> "No, the transaction is not a related party transaction and none of the
> promoter/promoter group/group companies have any interest in the entity
> being acquired." — same filing, Annexure A, p.3.

Comment: board approval and SPA execution date 20-Aug-2026; no appointed/
effective date beyond the disclosed indicative 3-month completion window
(not yet closed at run date); acquisition price Rs 103.22/share (Rs 105.87
inclusive of consultancy fees to sellers under Regulation 8(7) of the SAST
Regulations); open-offer price Rs 157.27/share; aggregate SPA consideration
Rs 246.12 cr. This deal has not yet closed; if it does not complete within
the disclosed window, that is itself a tracked signal (Section 4b).

### 8. RELATED-PARTY PERIMETER

| Entity | Nature of transaction | Amount (FY26) |
|---|---|---|
| Sajal Jain, Sreelekha Jain, Saumya Jain (residential property sale) | Non-arm's-length asset sale | Rs 42.50 cr |
| Sreelekha Jain, Pranika Jain (office premises sale) | Non-arm's-length asset sale | Rs 14.00 cr |
| Sreelekha Jain, Pranika Jain (office leaseback) | Rent, 3-year term, 5% p.a. escalation | Rs 55 lakh/yr base (Rs 27.50 lakh, partial-year FY26) |
| Sajal Jain, Pranika Jain, Sreelekha Jain (3 vehicles) | Non-arm's-length asset sale | Rs 5.52 cr |
| Sajal Jain (departed MD & CFO) | Commission payable at year-end | Rs 3.30 cr |
| Radius Estate Projects Pvt Ltd (formerly Vishwaroop Realtors) | Inter-corporate deposit, unprovided, counterparty under IBC insolvency | Rs 5.09 cr (no connection found to either promoter group) |

Source for all rows: AR AOC-2 Annexure III (p.42) and Note 40 (p.108-109),
per 08-promoter.md Section 3A, cross-verified line-by-line against the
per-party breakdown in Note 40. Comment: no related-party transaction with
Zenrock Chemicals Private Limited or any Malhotra-family entity is
disclosed anywhere in Note 40 for FY26 (B03 Phase 2B, verified as an
absence within this document's scope).

### 9. PLEDGE AND SHAREHOLDING

> "100% of the promoter shareholding is pledged to secure Zenrock's
> acquisition debt, comprising outstanding non-convertible debentures
> (NCD) principal worth around INR2,550 million and a bullet repayment due
> in FY31." — rating.pdf, p.1.

> "The acquisition was funded through the issuance of secured NCDs worth
> INR3,900 million and compulsorily convertible preference shares worth
> INR750 million at the promoter level [ZCPL]." — rating.pdf, p.3.

Shareholding trend (screener-shareholding-pattern.txt, SECONDARY tier,
quarterly):

| Quarter | Promoters | FIIs | DIIs | Public |
|---|---|---|---|---|
| Sep 2023 - Dec 2025 | ~50.79-52.07% (Jain family) | ~0-0.5% | ~0-0.02% | ~47.9-49.2% |
| Mar 2026 | 30.80% (Zenrock only, AIFs declassified) | 0.45% | 2.19% | 66.56% |
| Jun 2026 | 38.41% (Zenrock post-open-offer) | 0.13% | 0.04% | 61.43% |

Comment: only twelve most-recent quarters are in the corpus (Sep-2023 to
Jun-2026), matching the annex's own 12-quarter ask exactly. The exact split
of the 38.41% Jun-2026 promoter line between Zenrock's own stake and any
residual AIF classification, and the exact current pledge share count, are
NOT DISCLOSED at Reg 31 filing precision in this corpus — the figures above
are the screener aggregate and the rating agency's own summary; the Reg 31
filing itself is an input gap (Section 1). Institutional (FII+DII) holding
is under 3% throughout the twelve quarters shown.

### 10. VERIFICATION

Documents quoted in this annex, with filename and date:
- rating.pdf — India Ratings and Research, "India Ratings Assigns Indo
  Borax & Chemicals's Bank Loan Facilities 'IND BBB+'/Stable," 23-Jul-2026.
- Concall_Jun_2026_Transcript.pdf — Indo Borax & Chemicals Q4 & FY26
  earnings call transcript, 02-Jun-2026.
- Annual_Report_2023.pdf (content: FY2025-26 Annual Report, 45th AGM, year
  ended 31-Mar-2026, filed 21-May-2026).
- 2026-08-20_Board_Outcome_Kronox_SPA.pdf — Indo Borax & Chemicals Ltd,
  Regulation 30 outcome of board meeting, 20-Aug-2026.
- c98b4ce9-6850-49b3-87b6-cd571db84098.pdf — Q4/FY26 audited standalone and
  consolidated results filing, period ended 31-Mar-2026.
- screener-shareholding-pattern.txt — screener.in shareholding table,
  operator-provided, 2026-08-30 (SECONDARY tier).

**CORPUS COMMIT HASH: 9f2e03657fb0eb078d57d640d1ca162d844ad062**

---

```yaml
stage: B09b-dossier
company: "INDOBORAX"
run_date: "2026-08-30"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED-FRESHNESS"
corpus_gaps:
  - {document: "AR FY24 and FY25", expected_source: "BSE / company IR page", kind: "findable-missing"}
  - {document: "Q1 FY27 concall transcript", expected_source: "BSE / company IR page", kind: "freshness-pair"}
  - {document: "Postal-ballot notices (Sec 186 Rs700cr, ESOP 2026)", expected_source: "BSE", kind: "findable-missing"}
  - {document: "Reg 31 shareholding filing", expected_source: "BSE/NSE", kind: "findable-missing"}
archetypes:
  - {line: "Boron chemicals manufacturing (single reportable segment)", archetype: "Commodity converter"}
transition:
  - line: "Boron chemicals manufacturing (single reportable segment)"
    from_tier: "R2 COST-ADVANTAGED CONVERTER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER"
    engine: "Product-mix shift into DOT/Boron Oxide via debottlenecking and a still-uncommitted capex plan (rating.pdf: ~INR900mn FY27-28, FY29 commercial start), paired with replacement of the 40-year Jain family promoter-operator by a professional CEO/CFO under sponsor Zenrock (itself Malhotra-family beneficially owned) plus three EAAA/Edelweiss AIF co-investors"
    proof_gate: "Boron Oxide CWIP >Rs100 lakh tagged to the project appears in a filed balance sheet, followed by first commercial dispatch; corpus holds two conflicting management timelines (concall '3-4 quarters' vs rating.pdf FY29), neither yet evidenced"
    recognition_gap: "Open question, not concluded here: does current market pricing already reflect the claimed diversified, professionally-run TO state, or still the single-product FROM state? Resolved at Stage 11 via the PE gap."
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "By the FY28 AR: no Boron Oxide CWIP/dispatch under either timeline, AND DOT volume still below ~1,400t, AND a new RPT/ICD naming a Malhotra-family or Zenrock-linked entity repeating the departed Jain family's extraction pattern"
dominant_variables:
  - "Boron Oxide capex-to-CWIP-to-dispatch conversion"
  - "Raw-material cost as % of revenue / pre-exceptional margin trajectory"
  - "DOT volume ramp toward the stated FY27 goal (980t to 1,500t)"
  - "New RPT/ICD activity involving Malhotra-family or Zenrock-linked entities"
business_falsifier: "Loss of the sole-India IP-grade FDA licence/BIS certification; OR a second unprovided/impaired treasury exposure beyond the Radius Estates ICD signaling systemic treasury-control failure; OR raw-material cost structurally (not cyclically) outgrowing realisation, pushing clean operating EBITDA margin below 20% for multiple consecutive years"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 5
  verifiability_ratio: "2 of 5 externally observable"
  single_point_failure: "raw-material cost structurally outgrowing revenue (pre-exceptional PBT already fell 3.75% YoY on this driver)"
  fragility_verdict: "FRAGILE"
candidate_count: 6
research_brief_items: 11
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "9f2e03657fb0eb078d57d640d1ca162d844ad062"
```
