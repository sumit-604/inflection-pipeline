# HALT 1 UNDERSTANDING DOSSIER
## Forbes Precision Tools & Machine Parts Ltd (TOTEM) | Run date 2026-09-09

This dossier assembles what stages 0 through 9 and the phase-1 verifiers
already found. It does not value the company. It does not recommend an
action. Stages 10 and 11 have not run: there is no destination PE, no
entry zone, no price, no decision here.

---

## READ THIS FIRST: WHAT THE PHASE-1 VERDICT MEANS

The phase-1 gate verdict is REWORK, forced by a confidence delta of 32
against a threshold of 60 (B13-synthesis; confidence.yaml). REWORK judges
the analysis, not the business.

Verifier A checked 87 material numbers across all nine stage reports.
It found zero mismatches and zero source-fidelity failures. The three
MAJOR and two MINOR items it did raise are presentation and
methodology-transparency notes, each explicitly marked
`source_fidelity: false` (B12a). The figures in this pack are sound.

What is incomplete is the reading of management communication (stage 5)
and the peer verdict discipline (stage 6). Verifier B found 47
red-flag-grade items on an independent read of the same filings; stages 5
and 6 caught 15 outright and partially caught 8. Five claims the reports
currently make are not supported by the sources (B12b, the
`pipeline_flags_not_supported` list, NS-1 through NS-5). Verifier D found
peer citation fidelity high (about 28 of 30 spot checks clean) but peer
coverage and verdict-discipline completeness gapped (B12d).

Three verifier cycles ran where the pipeline specifies one. Stages 5 and 6
were each rewritten twice. The loop stopped because the denominator kept
growing, not because the analysis was degrading: each fresh
out-of-family read mined deeper into a genuinely defect-rich set of
filings (B12b `orchestrator_note`). Carry this plainly. It is not a
verdict on the company.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

### 1. Concalls
None held. `manifest.concalls_available` is false; the company holds no
earnings calls. This is a declared absence, not a gap (B00). NO-CONCALL
MODE governs stage 5 and this run's whole read of management intent.

### 2. Annual reports
Three years held: Annual_Report_2026.pdf (FY2025-26, Fourth Annual
Report, 129p), Annual_Report_2025.pdf (FY2024-25, 111p),
Annual_Report_2024.pdf (FY2023-24, 105p, the first AR, covering the
demerger accounting). FY26 is the latest completed FY and is present.
Three years held, one more than the contract minimum of 0-1 (B00). The
company's full standalone history is only three years long: incorporated
2022, Scheme of Arrangement effective 1-Mar-2024 (appointed date
1-Apr-2023). A longer backward baseline exists only in the 2024
Information Memorandum's restated pre-demerger statements.

### 3. Results filings
Latest: FY27-Q1_Unaudited_Results_30Jun2026.pdf (quarter ended
30-Jun-2026), a scanned image with zero extractable text, read from
rendered PNGs at `work/pages/FY27-Q1_Unaudited_Results_30Jun2026/`. Also
held: FY26_Audited_Results_31Mar2026.pdf (year ended 31-Mar-2026) and
FY26-Q3_Unaudited_Results_31Dec2025.pdf (quarter ended 31-Dec-2025). No
quarter-gap exists between the latest results filing (Q1 FY27, filed
12-Aug-2026) and the latest AR (FY26, filed 2-Jul-2026); the AR precedes
the Q1 result.

### 4. Investor presentations
None held. The company publishes none: the FY26 AR states directly, "The
Company does not have a practice of making presentation to institutional
investors and analysts" (AR2026 p.52, quoted at B05). This is a
plausibly-nonexistent absence, itself a data point on communication
opacity, not a findable-but-missing gap.

### 5. Research / rating
Both empty. No broker note, no rating rationale (CRISIL/ICRA/CARE) held
or found at intake (B00). A stale IVR BBB/Stable rating dated 5-Dec-2024
is mentioned inside the AR itself (AR2026 p.54, per B12b) but no rating
rationale document is staged in the corpus. This matters: it is one of
two pieces of evidence that could independently settle the cash-conversion
question, and neither is available.

### 6. Corporate actions
Seven announcement filings held, dated Jan-2025 to Aug-2026: EGM notice
(9-Jan-2025), an AR corrigendum (3-Jun-2025), two Senior Management
Personnel filings (1-Aug-2025, resignation Apr-2026), the FY2026
Secretarial Compliance Report, and two Board Meeting outcome filings
(30-Oct-2025 for H1 FY26, 12-Aug-2026 for Q1 FY27). No JV, order-win, or
capital-raise announcement exists in this set.

### 7. Freshness pair check
`freshness_verdict: FRESHNESS PAIRS OK` (B00). All four pairs:
- RESULTS to CONCALL: SKIPPED. Trigger is the Q1 FY27 results filing; no
  concall mate is expected because `manifest.concalls_available` is
  false. Declared absence, not a failure.
- RATING BULLETIN to RATIONALE: PASS. No rating bulletin is staged in the
  corpus, so there is no trigger to fail against.
- SEBI ORDER to ORDER TEXT: PASS. No SEBI order is referenced in any
  staged filing.
- AR to LATEST AUDITED ANNUAL RESULTS: PASS. Annual_Report_2026.pdf is
  the Fourth Annual Report 2025-26 (p.1), the same year as the latest
  audited annual results (year ended 31-Mar-2026). The AR does not trail.

No pair failed. `CORPUS GAPPED-FRESHNESS` does not apply.

### The gaps, named plainly
- `inputs/rating/` is EMPTY. No public CRISIL/ICRA/CARE rationale exists
  for this name in the corpus. Expected source: rating agency site. This
  is the sharper of the two gaps: it is one of the two pieces of evidence
  that could independently settle the FY26 cash-conversion question
  (B00).
- `inputs/presentation/` is EMPTY, because the company publishes none
  (plausibly-nonexistent, AR2026 p.52).
- `inputs/research/` is EMPTY. No broker coverage found (plausibly
  reflects the company's small size and recent listing, not confirmed
  either way).
- Peer coverage is 2 of 3 selected peers (Kennametal India, Wendt India);
  Birla Precision Technologies has zero transcripts. The newest
  Kennametal call (15-Mar-2024) is roughly 2.5 years older than the run
  date; Wendt's one call (21-Jul-2025, misnamed by the screener as a
  Jul-2026 file) is the only in-window peer datapoint (B00, B06).
- The Q1 FY27 results filing is a scanned image, readable only from
  rendered PNGs, a container limitation rather than a filing defect
  (B00).
- Five of six screener CSVs per company (subject and all three peers) are
  empty formula shells; only `<TICKER>-Data_Sheet.csv` holds data, a
  known collector defect (B00).

### 8. VERDICT LINE

    CORPUS CURRENT

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

This is a transition thesis, not a business description. It is a draft
for the operator to accept, amend or reject in claude.ai after live-web
stress-testing. Nothing here is signed.

### PART A: THE FROM STATE

**A1. Archetype.** TOTEM's manufactured finished-goods line (98.96% of
FY26 revenue, Note 21, B04) fits the **Brand/franchise consumer**
archetype from the CLAUDE.md ARCHETYPE LIBRARY, applied to an industrial
buyer rather than a retail one: a branded industrial consumable, sold on
distribution reach and repeat-purchase wear-replacement economics, not on
an order book or a converter spread. It is NOT an order-book business
(EPC/defence-style backlog disclosure does not exist here, B04) and it is
NOT a pure commodity converter (Amendment 17 does not bind it; the
company brands and application-qualifies its output rather than merely
converting a spread). The two smaller streams, traded goods (0.09%) and
service income (0.20%), are immaterial and carry no separate archetype
(B04).

**A2. The simple analogy.** Think of a cutting tool like the blade in a
barber's razor. It wears down every time it is used, and the buyer has to
rebuy it again and again. TOTEM makes those "blades" for factories, not
barbershops, shaped as drills, taps and cutters, under a 65-year brand
name. It does not sell direct; it sells through 200-odd distributors the
way a razor-blade maker sells through kirana stores, not door to door
(B04). Because the buyer keeps coming back when a tool wears out, the
base business should be steady. But the steel and carbide that go into
the blade are partly imported and their prices swing, so in a year metal
costs jump, TOTEM's margin per blade is squeezed until price catches up
(B04). That is where the business sits today: a legacy brand,
distribution-led, mid-squeeze on an input-cost cycle, with new capacity
just installed.

### PART B: THE TRANSITION

**B1. From-to.** FROM: **R2 COST-ADVANTAGED CONVERTER, shading toward
R3**. ROCE runs about 22% (Note 33.2, B01/B04), sitting at the R3
boundary (the ladder's R3 band is 20-25%), but FY26's own numbers argue
against calling the cost advantage durable: raw-material cost grew 25.3%
against 7.9% revenue growth and operating margin fell 18% to 16.39% (B01,
B04) — the opposite of a cost-advantaged converter's expected behaviour
in an input-cost cycle. TO (claimed): **R3 VALUE-ADDED / SPEC'D
SUPPLIER**. The evidence for the claim is real but partial: AS9100D and
IATF-grade certifications are documented across 2-3 consecutive ARs (B07
category B2, "Strong", DOCUMENTED), which is genuine spec-in evidence.
Weighed against the rung-jump base rate (one rung per 2-3 years, CLAUDE.md
QUALITY LADDER): TOTEM has held these certifications for roughly that
window, so an R2/R3-boundary to R3 climb is plausible in principle, not a
multi-rung leap. Set against that: the peer read complicates rather than
confirms it. Kennametal India's own structural migration (its calls
across Mar-2023 to Mar-2024) runs toward tungsten-carbide and CNC
product, explicitly excluding HSS and taps from its own commentary
(KENNAMET Mar-2023 p.7, B06). HSS is the family TOTEM's own single
delivered trigger, the drill-capacity capex, sits in (B05 trigger 1). The
peer evidence that would confirm TOTEM is climbing the same ladder rung
Kennametal already occupies does not cover TOTEM's actual product core.

**B2. The engine.** Two things physically change: (i) the FY26 capacity
investment — an Austempering furnace (+90MT) and CNC HSS drill capacity
(+~350,000 units), installed FY26 and independently corroborated via
screener quarterly data (B03 `strengths_top3`) — and (ii) the
certification base (AS9100D, IATF, ISO 26000 added FY26, B04) that opens
qualified accounts in aerospace, defence and auto. Together these are
meant to shift mix from commodity HSS toward higher-value carbide and
high-performance tooling, and to convert installed capacity into volume
at a better realised margin.

**B3. The proof gate.** Operating margin sustaining above 20% for two
consecutive quarters beyond Q1 FY27. This is exact and testable
quarter by quarter against filed results. It is not yet fired: Q1 FY27's
PBT margin of 17.6% already sits four points below Q4 FY26's 21.6%, so
the gain over the FY26 full year recomputes to 1.8 percentage points, not
the headline 16.1%-to-22.9% operating-margin jump's implied 6.8 points
(B12b, cross-checked against B01 LBF-1). Q1 FY26 was FY26's own trough
quarter. Until two consecutive quarters print above 20% on a basis
consistent with Q4 FY26, the transition is narrative, not a confirmed
shift.

**B4. The recognition gap — OPEN QUESTION, resolved at Stage 11.**
Whether the market already prices an R3 spec'd-supplier tier into TOTEM,
given the comparable-multiple peer set the corpus carries (Kennametal
India, Wendt India, Birla Precision Technologies, B04/B06), or whether
the destination-PE gap for an R2-to-R3 migration still sits open, is not
concluded here. Stage 11 resolves it via the PE gap. If the TO state is
already priced, the re-rating engine implied by the ladder migration is
spent and only earnings growth would carry the case forward.

**B5. The ugliness test — UNRESOLVED, presented as open.** The ugly optic
is the FY26 inventory build (Rs 31.93cr to Rs 56.42cr, +76.7%) and the
46.3% CFO fall (Rs 51.32cr to Rs 27.55cr, B01/B02). The evidence that
would settle ARTIFACT-OF-CLIMB against STRUCTURAL-FEATURE does not exist
in the filings: there is no inventory ageing schedule, no NRV write-down,
no obsolescence-provision movement anywhere in the 44 notes, despite the
company's own accounting policy (Note 2B(v)) naming obsolescence a
critical judgement, and despite full ageing tables being given for the
comparable working-capital lines, receivables (Note 5) and payables (Note
19) (B02, `LBF-2` final verdict). The one piece of external support the
run initially gave the "abnormal commodity prices" explanation (the
MD&A's own claimed cause, AR2026 p.25) does not survive the company's own
three-year CIF import series: FY26 is only 1.23% above FY24, the last
normal year; FY25 was the depressed outlier (B05, B02). That withdrawal
makes the build's cause MORE open, not less. Two readings remain live and
neither is evidenced over the other: (a) pre-positioned raw material and
WIP for the FY26 capex ramp converting into Q1 FY27 volume — an
ARTIFACT-OF-CLIMB reading; (b) unsold or slow-moving stock from a
demand-forecasting miss, funded by stretching MSME suppliers (payables
nearly doubled, Rs 7.41cr to Rs 14.32cr, B02) — a STRUCTURAL-FEATURE
reading. The sole Key Audit Matter is revenue recognition, not inventory
(B02 P3-2), which is evidence the audit found no matter rising to KAM
significance, but is explicitly not an inventory-quality disclosure and
does not resolve the question either way.

**B6. The transition falsifier.** Operating margin reverts to sub-17% for
two consecutive quarters after Q1 FY27, confirming the Q1 FY27 gain was
a soft-base and opex-compression artifact (net material cost 36.1% of
revenue in Q1 FY27 versus 32.2% in FY26, +430bp, while other expenses
fell 5% in absolute terms on revenue +28.9% and permanent headcount fell
481 to 420, B12b) rather than a capex-and-certification-driven mix shift.
Combined with continued zero product-line disclosure separating carbide
from HSS revenue (Note 21/38 remain silent, B02/B04), this would kill the
transition thesis specifically, without necessarily killing the
underlying FROM business.

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2 the engine and B3 the proof
gate):
1. Operating margin trajectory against the 20%-for-two-quarters proof
   gate. Current state: Q1 FY27 PBT margin (17.6%) sits below Q4 FY26
   (21.6%); the gate has not fired (B01, B12b).
2. Raw-material-cost-to-sales ratio against the 32-35% FY24-25 band.
   Current state: 37.2% FY26; 36.1% in Q1 FY27, still elevated (B04,
   B12b).
3. Inventory ageing / write-down disclosure. Current state: absent
   throughout the corpus; genuinely unresolved (B02 LBF-2 final verdict).
4. Product-line (HSS versus carbide) or segment revenue disclosure.
   Current state: absent throughout; single reportable segment confirmed
   (Note 38, B02, B04, B07).

**C2. What the model rejects.** Total-addressable-market sizing debate is
noise here: B09's SOM-implied revenue CAGR (20.7-22.1%) already runs
below the strategy's 25% CAGR hurdle on the most evidenced path, and a
~Rs 180cr yr3 gap exists between that SOM and the capex-embedded organic
growth signal of 3.3% pa (B07/B09) — the binding constraint is
single-plant execution capacity, not market size. Peer-sourced
market-share sizing is also rejected as a load-bearing input: the peer
set's product coverage excludes TOTEM's HSS-and-taps core (Kennametal
explicitly excludes HSS and taps from its own commentary, KENNAMET
Mar-2023 p.7; Wendt makes neither HSS nor carbide cutting tools, B06), so
peer-derived share or pricing conclusions cannot be read onto TOTEM's
actual product mix without that caveat attached every time.

**C3. The business falsifier** (distinct from B6 — this kills the FROM
business itself, not only the climb). A single-plant disruption at
Chhatrapati Sambhajinagar (the company's only site, no second plant, B04)
or enforcement of the 94.4%-pledged promoter block (100% of SPCPL's own
69.71% direct stake) following the live SPCPL group refinancing crisis
(CareEdge downgraded Goswami Infratech NCDs BB- to B+ in May-2026, with
repayment deadlines slipping through Jun-2026, B08) would remove the
certified-account relationships and distributor-brand base the whole FROM
business rests on, independent of whether the transition itself is real.
The pledge meets the framework's own deal-breaker threshold (pledge
>40%, B08 `deal_breakers`) and is a group-financing fact layered on an
otherwise clean operating subsidiary (TOTEM itself has zero loans, ICDs
or guarantees flowing to the promoter group, B08 Section 3A), not
evidence of TOTEM-level misconduct.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

**What the products are and why they matter.** TOTEM makes and brands
metal cutting tools: taps, dies, drills, thread mills, end mills, burrs
and spring lock washers (B04). These are wear items. A drill or a tap
dulls with use inside a customer's own machine and must be replaced to
keep the machine cutting to tolerance, so the product is not a one-time
sale but a recurring, machine-usage-linked rebuy (B04). This single
manufactured-goods line is 98.96% of FY26 revenue, so it is effectively
the whole business; the other four revenue lines, traded goods, service
income, export incentives and scrap sales, together make up 1.04% and
carry no separate strategic weight (Note 21, B04).

**Who the customers are.** The buyers sit in India's auto and
auto-component, aerospace, defence, railways, oil and gas, and general
engineering factories (B04). Most purchases route through a
distributor network, over 200 partners across 12 divisional and regional
sales offices as of the 2024 listing document, not re-disclosed in the
FY26 AR so its currency is unverified, with some direct sales to auto
OEM accounts (B04). No customer, distributor or geography concentration
figure is disclosed anywhere in the corpus; the company reports a single
segment (Note 38) and gives no product-line or customer-industry
breakdown in Note 21 (B02, B04, B07).

**Why demand exists.** Demand exists because cutting tools are
consumables, not durables: they wear out on a cycle set by how much a
customer's machines run, not by a discretionary buying decision (B04).
A qualified account, once it has application-tested and approved a
TOTEM tool for a specific job, faces a real switching cost to requalify
a competitor's tool, which is the mechanism behind the "switching
costs" moat entry TOTEM carries (B04, B07 category B2). The 65-year
TOTEM brand and its aerospace/defence/auto-grade certifications (AS9100D,
IATF, plus ISO 26000 added FY26) are the credibility markers that get a
tool onto a qualified-supplier list in the first place (B04).

**Why demand grows, or does not.** FY26 revenue grew 7.9%, inside the
company's own stated recent trend, but raw-material cost grew 25.3% in
the same year, so the growth did not yet convert fully into profit;
operating margin fell from 18% to 16.39% (B01, B04). Management's own
explanation for the cost spike, "commodity prices... increased
abnormally" (AR2026 p.25), does not survive the company's own three-year
import-cost series (FY26 only 1.23% above FY24, B05, B02), which reopens
rather than settles the question of what actually drove the year's
working-capital stress. New capacity (furnace, CNC drill lines) installed
in FY26 is the company's own stated growth driver going forward, and Q1
FY27 shows an early margin gain, but a verifier found that gain runs
largely on a soft year-earlier comparison base and on falling headcount
rather than on proven yield or mix improvement (B12b). Whether demand
growth continues depends on whether the new capacity converts to
qualified-account volume at a durable margin, not yet established either
way (B03, B07).

**Where the competitive advantage sits, and where it does not.** On the
manufactured-goods line, the advantage that holds up under scrutiny is
brand recognition plus distributor reach plus account-qualification
switching costs (B04, B07), all rated Medium durability, not High: the
distributor count is stale (2024 data), and no renewal-rate or
account-retention figure exists to size the switching-cost moat (B04).
The advantage that does NOT hold up is cost or scale advantage: FY26
shows raw-material cost outrunning revenue and margin contracting, the
opposite of what a durable cost-advantaged position should show in an
input-cost cycle (B01, B04, B07). An independent emerging-moat scan
found only 3 of 23 tested categories carry Strong or Moderate evidence,
and even those two "Strong" categories, process technology and
qualification lock-in, are catch-up moves matching what global majors
like Kennametal already hold, not a lead TOTEM has opened (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Operating margin durability.** What the corpus establishes:
FY24-26 operating margin ran 17-19% then fell to 16.39% in FY26 (B04);
Q1 FY27 shows 22.9% against a 16.1% year-earlier base, but the PBT-margin
read (17.6% versus Q4 FY26's 21.6%) shows the full-year gain is smaller,
1.8pp not 6.8pp (B01, B12b). What it cannot establish: whether the Q1
FY27 gain is durable (capex/mix-driven) or transient (base-effect and
headcount-driven); the corpus holds no product-line margin split to test
this directly (B02, B04). Questions that decide it: (1) does operating
margin print above 20% for a second consecutive quarter in Q2 FY27; (2)
does net material cost as a percentage of revenue fall back toward the
32-35% band or stay elevated; (3) does headcount stabilise or continue
falling, which would argue for cost-cutting over mix shift as the driver.

**Vertical 2: Raw-material cost pass-through.** What the corpus
establishes: FY26 raw-material cost grew 25.3% against 7.9% revenue
growth (B04); the three-year CIF import series shows FY26 only 1.23%
above FY24, undermining the company's own "abnormal" framing (B05); one
peer (Kennametal, Mar-2023) claims unhedged full pass-through is
achievable for a well-positioned player (B06). What it cannot establish:
what specifically drove FY26's cost pressure if not an abnormal
commodity spike, since price and volume cannot be separated from the CIF
value series alone (B12b NS-4). Questions that decide it: (1) does the
raw-material-cost-to-sales ratio fall back below 35% in FY27 quarters;
(2) does any peer FY26 commentary (once a fresher transcript exists)
confirm or deny an industry-wide cost event; (3) does the company ever
disclose a volume-versus-price breakdown of its raw-material bill.

**Vertical 3: Inventory quality.** What the corpus establishes: inventory
rose 76.7% in FY26 with no ageing, write-down or obsolescence-provision
disclosure anywhere in 44 notes, despite the company's own policy naming
obsolescence a critical judgement (B02 LBF-2). The build was financed
largely through MSME payables growth (+93.3%) and a mutual-fund drawdown
(-47.2%), not fresh borrowing (B02). What it cannot establish: whether
this is ramp stock for the FY26 capex or unsold/slow-moving stock from a
demand-forecasting miss; no rating rationale or ageing table exists to
settle it (B00, B02). Questions that decide it: (1) does the FY27 AR add
an ageing or NRV write-down disclosure; (2) does inventory as a
percentage of revenue normalise toward FY25 levels; (3) does CFO recover
toward the FY25 CFO/PAT ratio of 1.78x.

**Vertical 4: Product-mix / segment disclosure.** What the corpus
establishes: single reportable segment confirmed (Note 38); zero
product-line (HSS versus carbide), customer-industry or geography
breakdown in Note 21 across all three ARs (B02, B04, B07). What it
cannot establish: the actual mix shift the transition thesis needs to
test directly; every read of "which product line is driving growth" is
necessarily indirect (B02). Questions that decide it: (1) does the
company ever begin voluntary segment or product-line disclosure; (2)
does any FY27 filing name a specific carbide or aerospace-linked revenue
figure; (3) does any peer disclosure (once fresher transcripts exist)
allow an indirect read of TOTEM's likely mix via its named competitors.

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| IMTMA machine-tool production/consumption/import data | Consumable-demand growth decouples from the 12-15 month capex-lead lag Kennametal describes (B09) | Quarterly | IMTMA press releases / Ministry of Heavy Industries Annual Report |
| SIAM automotive production/sales volumes | Auto-sector production falls or flattens while TOTEM revenue keeps growing, breaking the named largest end-market link (B04) | Monthly | SIAM monthly production/sales data |
| Kennametal India quarterly results | Kennametal's own margin or demand commentary diverges sharply from TOTEM's without a stated reason, undercutting the "industry cross-read" (B06) | Quarterly | Kennametal India BSE/NSE quarterly filings |
| US and Mexico tariff policy on Indian exports | Tariff policy eases and TOTEM's export FOB figure still fails to recover above the FY24 baseline (Rs 3,834.10 lakh, B05) | Event-driven | USTR / Indian Ministry of Commerce trade notifications, financial press |
| HSS/tungsten-carbide raw-material import prices (Europe/China) | Import prices fall while TOTEM's raw-material-cost-to-sales ratio stays above 37%, ruling out an input-price explanation for margin pressure (B04, B09) | Monthly | Steel/tungsten price indices, Ministry of Commerce import data |
| Defence and Aerospace procurement budget / Make in India tooling initiatives | AS9100D certification (B04, B07) produces no disclosed aerospace/defence revenue linkage after 2-3 more annual cycles | Event-driven | Ministry of Defence / PIB Union Budget documents |

These six are the B09 candidates, unverified drafts. Verification and
tracker writes happen at Role 5.5 in claude.ai.

### 4c. Fragility read

- **variable_count:** 5. The bull case needs: (1) operating margin
  sustaining above the proof-gate threshold; (2) raw-material cost
  stabilising back toward the 32-35% band; (3) the FY26 inventory
  build resolving as ramp stock, not dead stock; (4) product-mix or
  segment evidence eventually surfacing to confirm the HSS-to-carbide
  shift; (5) the promoter pledge not converting into a forced sale or
  loss-of-control event tied to the SPCPL group refinancing crisis.
- **verifiability_ratio:** 3 of 5 externally observable. Operating margin
  (1) and the raw-material ratio (2) are both readable from quarterly
  BSE filings, and the promoter pledge (5) is readable from quarterly
  shareholding filings, all independent of company narrative. Inventory
  quality (3) and product-mix evidence (4) are, as things stand,
  company-narrated only: no independent ageing disclosure or segment
  disclosure exists to check either against (B02, B04).
- **single_point_failure:** promoter pledge enforcement / a forced sale
  of the 94.4%-pledged block, tied to the live, currently-downgraded
  SPCPL group refinancing crisis (CareEdge B+, slipping Jun-2026
  deadlines, B08). This variable can break the case independent of how
  the operating engine performs.
- **fragility_verdict:** FRAGILE. Three of five variables are externally
  verifiable, which argues for MODERATE, but the proof-gate variable
  itself is already contested by an independent verifier read (B12b
  shows the headline Q1 FY27 gain overstates the underlying move), two
  variables are company-narrated only with no independent check
  available, and a genuine single point of failure exists outside the
  operating business entirely. The conjunction of these three facts
  moves the verdict from MODERATE to FRAGILE.

### 4d. Research brief (claude.ai work order)

1. PENDING LIVE VERIFICATION (Chain 1, Section 4e): pull TOTEM's Q2 FY27
   BSE results filing and any accompanying exchange announcement when
   filed (due ~Nov 2026), and check for any voluntary product-mix or
   customer commentary that would show which end-customers are absorbing
   the FY27 volume gain, and at what realised price.
2. PENDING LIVE VERIFICATION (Chain 2, Section 4e): search for a
   CRISIL/ICRA/CARE/IVR rating rationale on TOTEM (none exists in this
   container's corpus) and for any FY27 exchange announcement or press
   coverage naming a specific order, contract or distributor sell-through
   figure that would bear on the FY26 inventory build's quality.
3. Verify the "about Rs 290 cr" FY26 revenue figure used in 06-peers.md
   Part 2D against the audited Rs 251.01 cr (Note 21); Verifier A did not
   adjudicate this cell, so it remains open on the rework list (B12a,
   B12b finding NS-5).
4. Search for an update on the SPCPL/Goswami Infratech group refinancing
   programme past the Jun-2026 deadline referenced in B08 (has it been
   met, further extended, or defaulted), given its bearing on the
   business falsifier in Section 2 C3.
5. Pull current IMTMA and SIAM data to cross-check B09's TAM inputs,
   which rest on 2022-2024-vintage stale datapoints (B09
   `stale_data_flags`).
6. Search for any FY27 investor communication, trademark-registration
   status update, or plant-disruption news, closing the three unresolved
   items named in the 2024 Information Memorandum (trademark pending,
   registered office not company-owned, promoter FCL-level pledge, B04).
7. Retrieve and re-read Kennametal's Mar-2024 p.24 market-share answer in
   full; it quotes a 250-300 basis point three-year market-share gain
   that verifier D found was surfaced only for its refusal clause and
   never used (B12d).
8. Retrieve and re-read Wendt's AGM transcript p.23 in full: it discloses
   a market-share range and a defence/aerospace revenue-mix percentage
   that verifier D found unused and directly relevant to stage 6's own
   claim that peers never quantify defence demand (B12d).
9. Check Forbes & Company Limited's own current pledge status
   post-demerger; the 2024 Information Memorandum establishes a
   pre-demerger baseline but no live 2026 check exists in the corpus
   (B08 `searches_skipped`).
10. Once a fresher Kennametal or a first Birla Precision transcript
    becomes available, re-run the peer cross-read on the "abnormal
    commodity prices" question (B05 Q1) and the pass-through question
    (B05 Q2), both currently resting on transcripts 1-2.5 years stale
    relative to FY26 (B00, B06).

### 4e. Second-order stub (Rule F, Master v3.7)

Two chains, drafted from corpus, off the two dominant variables the
evidence base can carry furthest: the operating-margin proof gate and the
inventory/raw-material story behind it.

```
CHAIN 1: Q1 FY27 operating margin printed 16.1% to 22.9% year on year
(B01 LBF-1, independently corroborated via screener quarterly data, B03
analyst_note), but the PBT-margin read shows Q1 FY27 (17.6%) sits below
Q4 FY26 (21.6%), and the full-year gain recomputes to 1.8pp, not 6.8pp
(B12b).
Link 1 [DOCUMENTED]: FY26 capacity investment (Austempering furnace
+90MT, CNC HSS drill capacity +~350,000 units) was installed FY26,
independently corroborated via screener quarterly data (B03
strengths_top3).
Link 2 [DOCUMENTED]: In Q1 FY27, net material cost rose to 36.1% of
revenue against 32.2% in FY26 (+430bp), while other expenses fell 5% in
absolute terms on revenue +28.9%, and permanent headcount fell 481 to 420
(-12.7%) during FY26 (B12b). This arithmetic, not a stated yield or mix
gain, is the driver of the year-on-year margin comparison.
Link 3 [INFERENCE]: If the FY27 margin gain runs primarily on opex
compression against higher volume rather than on the capex-enabled shift
toward carbide/high-performance tooling, the proof gate (Section 2 B3,
20% sustained for two quarters) could fire on a volume-and-cost-cutting
basis without the underlying R2-to-R3 quality migration, pricing power
from spec-in accounts, actually having occurred. The metric and the
thesis it is meant to test could decouple.
Link 4 [PENDING LIVE VERIFICATION]: who is paying, and why now. Which
end-customers (auto OEM, aerospace/defence, or export) are absorbing the
FY27 volume gain, and are they paying a higher realised price (mix
shift) or simply buying more at a flat price (volume only)? This cannot
be answered from the corpus: single reportable segment (Note 38), zero
customer disclosure (Note 21). Claude web should open TOTEM's Q2 FY27
BSE results filing and any accompanying exchange announcement when
filed, and check for any voluntary investor communication, none of which
existed as of this run.
Binding constraint: single-plant capacity (B04, no second site) and the
~Rs 180cr yr3 gap between B09's SOM and the capex-embedded organic
growth signal of 3.3% pa (B07/B09) cap how much further volume growth is
even available to sustain a compression-driven read.
Unsaid: the FY26 AR gives zero product-line (HSS versus carbide) revenue
split and zero capacity-utilisation disclosure (B04 input gap), and Note
31's gratuity data shows active members fell 14.8% while average pay
roughly doubled, unexplained (B02 CONFLICT 1) — the corpus cannot itself
distinguish "mix shift into carbide" from "volume growth on existing
lines with fewer, higher-paid staff."
Observation that confirms or breaks this chain, and confirm-by date: Q2
FY27 results (due on or around Nov 2026, B07 catalysts_12m) showing
operating margin sustained above ~20% on a basis consistent with Q4
FY26, together with any voluntary product-mix commentary. Confirm-by
2026-11-30.

CHAIN 2: FY26 inventory rose Rs 31.93cr to Rs 56.42cr (+76.7%), CFO fell
Rs 51.32cr to Rs 27.55cr (-46.3%), and the FY26 MD&A's own stated cause
("commodity prices... increased abnormally," AR2026 p.25) does not
survive the company's own three-year CIF import series (FY26 only +1.23%
over FY24, the last normal year, B05/B02).
Link 1 [DOCUMENTED]: no inventory ageing schedule, NRV write-down, or
obsolescence-provision movement is disclosed anywhere in the 44 notes,
despite the company's own accounting policy (Note 2B(v)) naming
obsolescence a critical judgement, and despite full ageing tables being
given for the comparable receivables (Note 5) and payables (Note 19)
lines (B02).
Link 2 [DOCUMENTED]: the build was funded largely through the
liabilities side, not cash: MSME trade payables nearly doubled (Rs
7.41cr to Rs 14.32cr, +93.3%, Note 19), while a Rs 23.23cr mutual-fund
book was drawn down 47.2% over the same year (B01, B02).
Link 3 [INFERENCE]: if the inventory build is pre-positioned raw
material and WIP for the FY26 capex ramp converting into Q1 FY27 volume,
financing it via suppliers and investments rather than fresh borrowing
is a rational, moderate-risk bridge. If instead it is unsold
finished-goods stock from a demand-forecasting miss, the same
MSME-payables financing choice reads as the company stretching small
suppliers to carry an undisclosed problem. The corpus cannot distinguish
these two readings, and the direction chosen flips the entire read of Q1
FY27's margin recovery from "capex paying off" to "cost compression
masking unresolved stock risk."
Link 4 [PENDING LIVE VERIFICATION]: who is paying, and why now. Is the
FY26 inventory build being absorbed by confirmed customer orders or
sitting unsold? Claude web should search for any FY27 exchange
announcement naming a large order, contract, or distributor sell-through
figure, and separately search for a CRISIL/ICRA/CARE/IVR rating
rationale on TOTEM, which is currently absent from the corpus (B00) and
would independently assess inventory and receivable quality.
Binding constraint: no rating rationale and no distributor-level
sell-through data exist anywhere in this container's reach (B00); the
sole Key Audit Matter is revenue recognition, not inventory (B02 P3-2),
which bears on audit risk assessment, not stock quality directly.
Unsaid: the company's own Note 33.2 ratio-table commentary marks a
19.35% fall in inventory turnover as "No Major Change" (B02), a
soft-pedal in the company's own required variance-explanation column
that the notes do not otherwise contradict or confirm.
Observation that confirms or breaks this chain, and confirm-by date: an
inventory ageing or write-down table appearing in an interim filing, or
inventory days and CFO recovering toward FY25 levels in the FY27 AR (due
~May-Aug 2027, B07 catalysts_12m). Confirm-by the FY27 AR filing date, or
sooner if an interim ageing disclosure appears.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in
claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Forbes Precision Tools and Machine Parts Ltd (TOTEM) makes cutting
   tools, taps, dies, drills, thread mills, end mills, burrs and spring
   lock washers, at one plant in Chhatrapati Sambhajinagar (B04).
2. It sells under the 65-year TOTEM brand, demerged from Forbes &
   Company Limited in 2023 and listed on the BSE since June 2024 (B04,
   B08).
3. Almost all revenue, 98.96% in FY26, comes from selling these
   manufactured tools; a small remainder is trading, service and
   export-incentive income (B04).
4. Buyers are mostly distributors: over 200 partners and 12 sales
   offices reached customers as of the last disclosed count in 2024;
   some direct sales go straight to auto-parts makers (B04, currency of
   the count unverified against FY26).
5. Customers rebuy because the tools wear out inside their own
   machines, the way a razor blade wears out; demand repeats on a
   machine-usage cycle the company does not control (B04).
6. Named end markets are auto and auto-components, aerospace, defence,
   railways, oil and gas, and general engineering, but the company
   discloses no split by industry or customer anywhere (B04, B07).
7. Revenue grew 7.9% in FY26, but raw-material cost grew 25.3% in the
   same year, so growth did not turn fully into profit (B01, B04).
8. Management names new capacity, a heat-treatment furnace and CNC
   drill lines installed in FY26, as its reason to expect more volume;
   Q1 FY27 shows an early margin gain (B03, B07).
9. A verifier found that gain runs largely on a soft year-earlier
   comparison base and on falling headcount, not yet on proven yield or
   mix improvement (B12b).
10. The moat, brand plus distributor reach plus certified qualification
    with defence and auto accounts, is real but thin: an independent
    scan found only 3 of 23 tested categories carry strong or moderate
    evidence (B07).
11. Cost advantage, the other possible moat, does not hold up: raw
    material cost outran revenue in FY26 and margin fell, the opposite
    of what a durable cost edge should show (B01, B04).
12. The mental model is a brand-and-distribution industrial consumable
    business trying to climb from a cost-advantaged tier toward a
    spec'd-supplier tier, and the climb is not yet proven (Section 2).
13. The bull case needs several things to go right at once, and two of
    them, inventory quality and the product-mix behind the margin gain,
    are things only the company can currently confirm; this makes the
    case fragile, not robust (Section 4c).
14. The filings disclose no product-line revenue split, no customer
    concentration, no per-unit price, no capacity utilisation and no
    inventory ageing; these gaps sit exactly where the transition story
    needs proof (B02, B04, B07).
15. The two biggest open questions are whether the FY26 inventory build
    is ramp stock or unsold stock, and whether the promoter's
    94.4%-pledged holding, tied to a live group refinancing crisis,
    stays stable or moves (B02, B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

### 1. Units

No per-unit price or cost figure (revenue per tool, cost per tool, or
per kg) is printed anywhere in the corpus.

> "Due to the nature of our product, the installed capacity is only an
> opinion of the management and the output would be determined by the
> size and complexity of the final product which defines the production
> time required." (Information_Memorandum_2024.pdf p.58)

Comment: the company itself cautions against relying on its own
capacity figures because output per unit varies by product complexity.
The only physical-volume figures anywhere in the corpus are 2024,
management-estimated, per-product-line installed capacities (units per
year, not revenue), stale relative to this run:

> "Particulars Installed Capacity (Units): HSS Taps 48,00,000; Carbide
> Tools 26,000; CST Taps 48,00,000; Dies/DN 6,00,000; Rotary Burrs
> 72,0000; HSS Drills 52,00,000; Carbide RM 18,0000; Hand tools
> 24,00,000." (Information_Memorandum_2024.pdf p.58, table as printed;
> OCR renders two figures with an extra digit, "72,0000" and "18,0000",
> as printed in the source extraction)

Comment: this table gives no price, so no per-unit revenue or cost can
be derived from it. The only basket-level figures available are total
revenue from manufactured finished goods (Rs 248.41 cr FY26, Note 21,
Annual_Report_2026.pdf p.101) and total raw-material consumption (Rs
93.32 cr FY26, Note 23A, Annual_Report_2026.pdf p.102); dividing either
by any single installed-capacity line would mix a basket revenue figure
against a single-product volume figure and is not a valid derivation.
NOT DISCLOSED: any per-unit price or per-unit cost figure, in any filed
document.

### 2. Segment capital and debt

> "The company manufactures precision cutting tools and related
> components. Based on management analysis, the company has only one
> operating segment, so no separate segment report is provided. The
> principal geographical area in which the company operates is India."
> (Annual_Report_2026.pdf, Note 38, p.126)

Comment: TOTEM discloses a single reportable segment. No segment assets,
segment liabilities, capital employed or segment-allocated borrowings
exist because no second segment exists to allocate against. Total
borrowings are disclosed unallocated (necessarily, given one segment):
Note 33.1 (Annual_Report_2026.pdf) states total borrowings fell from Rs
1,968.29 lakh to Rs 1,487.07 lakh FY25 to FY26 (per B12b, cross-checked
against Debt-Equity ratio 0.10x, B04). NOT DISCLOSED: any segment-level
capital or debt split, because the company reports only one segment.

### 3. Guidance versus aspiration

No forward revenue, margin, capex-timeline, or capacity-number guidance
exists anywhere in the three MD&A sections (B05 `guidance_table`). What
is stated, classified:

(a) Guidance with a period:
> "Labour settlement agreement... valid to end of 2028" (AR2025 p.22,
> reconfirmed AR2026 p.28) — multi-year commitment, dated.

(b) Aspiration without a period:
> "Our business remains aligned with emerging opportunities in India's
> Defence, Railways, and electronic industries" (recycled near-verbatim
> AR2024 p.16, AR2025 p.19, AR2026 p.25) — no period, no number, no
> named order.
> "enhancing our market share domestically" (AR2024 p.16, AR2025 p.19,
> AR2026 p.25 area) — no number, no competitor named, repeated three
> consecutive years.

(c) Capacity or capability only:
> Drill-capacity capex (CNC lines, robotic flute grinding, spring-washer
> furnace) named as installed FY26 (Board's Report, AR2026 p.24-26) —
> a completed capability statement, not a forward numeric target.

Comment: a company with no earnings calls also gives itself almost no
numeric forward commitment to be held to in an annual report; this
absence is itself a credibility-relevant fact (B05 `credibility_grade:
C`).

### 4. Concentration

> "The company manufactures precision cutting tools and related
> components... has only one operating segment... The principal
> geographical area in which the company operates is India."
> (Annual_Report_2026.pdf, Note 38, p.126)

Comment: no product, customer, or geography concentration figure is
printed. Top product share and top customer share are both NOT
DISCLOSED. The only concentration-adjacent figure filed is export
revenue: FOB exports Rs 3,189.46 lakh FY26 against total revenue Rs
25,101.13 lakh, roughly 12.7% (Board's Report Annexure, Annual_Report_
2026.txt p.42-43, cross-checked at B12b), which bounds geography exposure
only at the export-versus-domestic level, not by destination country.

### 5. Promise ledger

| Promised in | Promise | Delivery status | Evidence anchor |
|---|---|---|---|
| AR2024 MD&A | Full price pass-through protects margin | Delivered | consumption-matched gross margin +~212bp FY26 (B05, confirmed) |
| AR2024/AR2025 MD&A | Carbide Taps portfolio broadening via new technology | Missed | carried two annual cycles, silently dropped from AR2026, no delivery statement (B05) |
| AR2025 MD&A | "Improving trend in export business performance" | Missed | AR2025's own FOB figure (Rs 3,791.05 lakh) is below AR2024's (Rs 3,834.10 lakh), same report (B05) |
| AR2025 Finance section | "Relentless focus on inventories and receivables" keeps borrowing low | Partial | true in FY25; inventory build and debtor-days rise arrive in the same or next cycle (B05) |
| AR2026 MD&A | "Commodity prices increased abnormally," justifying margin pressure | Missed | three-year CIF series shows FY26 only 1.23% above FY24 (B05, B02) |
| AR2026 Board's Report p.30 | "Total amount spent... Rs 39.78 Lakhs" (CSR) | Missed / misleading | that was the FY25 carry-forward; FY26's own Rs 53.83 lakh obligation was 100% unspent (B05) |
| AR2024 Board's Report p.14 | Headline EPS Rs 110.63, no caveat | Missed (disclosure quality) | the decision-useful Rs 5.76 figure sits only in a note; AR2025's comparative implies a false ~95% EPS collapse (B05) |
| AR2024 p.15 | "Precision Tools business achieved 12% year-on-year growth" | Missed / unverifiable | no filed comparable base; AR2024's own table shows FY22-23 as nil, not comparable (B05) |
| AR2025 debtor-days table | Mandatory 25%-plus change explanation | Missed | cites 31-03-2023, a year not in the two-year comparison table (B05) |

Comment: tally across ten tested claims is 1 delivered, 2 partial, 7
missed (B05 `promise_delivery_score`).

### 6. Restated bases

> "42. Previous period figures have been re-classified/ re-arranged/
> regrouped, wherever necessary, to correspond with the current period's
> classification/ disclosure." (Annual_Report_2026.pdf, Note 42, p.126)

Comment: boilerplate, no quantified item named. Separately, a real
comparative-presentation issue exists in Note 3 (PPE roll-forward): the
"Previous Year" table mislabels the FY25 opening gross block as NIL and
re-dates the Scheme-of-Arrangement transfer (already recorded in the
FY24 AR) into FY25; closing balances tie out both years, so this is a
presentation artifact, not a numbers restatement (Annual_Report_2026.pdf
Note 3, p.88, cross-checked against Annual_Report_2024.pdf Note 3/38,
per B02 finding rank 10). No restatement cutting past profits by more
than 10% was found anywhere in the corpus (B08 deal-breaker check,
"not triggered").

### 7. Corporate-action clauses

The Scheme of Arrangement (demerger of the Precision Tools business from
Forbes & Company Limited into TOTEM) is fully in the corpus
(prospectus/Court_Order_Scheme_of_Arrangement.pdf, 48p; also summarised
in the Information Memorandum).

Definition of the undertaking transferred:
> "'Demerged Undertaking' means the Precision Tools business of the
> Demerged Company, carried on anywhere in India either by itself or
> through its subsidiaries, inter alia, including the business activity
> of manufacturing & trading of cutting tools, HSS Taps, HPT, Rotary
> Burrs, CST Drills, CST Dies, Spring Washer, Threading Tools and
> Carbide Tools..." (Court_Order_Scheme_of_Arrangement.pdf, Clause 1.7,
> p.33 of extraction)

Liability allocation clause:
> "For the purpose of this Scheme, the liabilities pertaining to the
> Demerged Undertaking means and includes: i. all liabilities (including
> contingent liabilities) arising out of the activities or operation of
> the Demerged Undertaking...; ii. specific loans and borrowings raised,
> if any, incurred and utilized solely for the activities or operations
> of the Demerged Undertaking; iii. liabilities other than those
> referred to in sub-clauses (i) and (ii) above being the amounts of
> general or multipurpose borrowings, if any, of the Demerged Company be
> allocated to the Demerged Undertaking in the same proportion in which
> the value of the assets transferred under this clause bears to the
> total value of the assets of the Demerged Company immediately before
> the Appointed Date..." (Court_Order_Scheme_of_Arrangement.pdf, Clause
> 1.7(e), p.34 of extraction)

Ratio:
> "4 (Four) fully paid up equity shares of INR 10/-each of the Resulting
> Company shall be issued and allotted to the equity shareholders of the
> Demerged Company for every 1 (One) fully paid up equity shares of INR
> 10/- each held by them in the Demerged Company as on the Record Date"
> (Court_Order_Scheme_of_Arrangement.pdf, p.5 of extraction)

Appointed and effective dates:
> "'Appointed Date' means 1st April 2023 or such other date as may be
> fixed or approved by National Company Law Tribunal, Mumbai Bench."
> "'Effective Date' means the date on which the certified copy of the
> order sanctioning this Scheme... is filed with the Registrar of
> Companies, Mumbai by the Demerged Company and the Resulting Company"
> (Court_Order_Scheme_of_Arrangement.pdf, Clauses 1.2 and 1.4, p.32-33 of
> extraction)

Comment: the appointed date (1-Apr-2023) is confirmed elsewhere in the
same document as fixed by the NCLT ("The Appointed Date is 1st April,
2023," p.25 of extraction); the effective date is separately established
in company disclosure as 1-Mar-2024 (B00, B08). Both dates and the 4:1
ratio are exact and printed, not derived.

### 8. Related-party perimeter

Per Note 30 (Annual_Report_2026.pdf, cross-checked in 08-promoter.md
Section 3A), FY26 transactions with promoter-group entities:

| Entity | Nature | FY26 (Rs lakh) | FY25 (Rs lakh) |
|---|---|---|---|
| Forbes & Company Ltd + Campbell Properties | Rent (expense) | 145.73 | 151.48 |
| FCFL, Forvol, Sterling & Wilson Renewable Energy | Travelling & conveyance (expense) | 236.13 | 287.98 |
| SPCPL | Legal and professional charges (expense) | 93.04 | 91.40 |
| FCL, Forbes Bradma | Repairs and maintenance (expense) | 125.30 | 139.25 |
| SPCPL 1,798.36 + FCFL 106.50 | Dividend paid | 1,904.86 | — |
| Mahesh Tahilyani (MD) | Remuneration | 464.00 | 265.52 |
| FCL | Rent and amenities (income) | 67.17 | 85.54 |

Comment: no loans, inter-corporate deposits, or guarantees flow between
TOTEM and any promoter entity in either year (Note 40(v), explicit
negative disclosure both years, B02/B08). The nature of the Rs 93.04
lakh "legal and professional charges" paid to SPCPL is not itemised
further anywhere in the AR (B08). Sixty-plus additional SP-Group
promoter-group entities are named in the shareholding filings at zero
shares held and zero transactions (shareholding__SHP_30Jun2026.txt); none
of them transact with TOTEM (B08 Section 1B).

### 9. Pledge and shareholding

Twelve quarters of shareholding history were requested; the corpus holds
three (Jun-2025, Mar-2026, Jun-2026), a run-level input gap (B00).

> "Whether any shares held by promoters are encumbered under 'Pledged'?
> Yes" (shareholding__SHP_30Jun2026.txt, declaration page, p.2 of
> extraction)

| Filing date | Pledged shares | % of promoter holding (73.85%) | Promoter holding % |
|---|---|---|---|
| 30-Jun-2025 | 35,967,172 | 94.4% | 73.85% (SPCPL 72.56% + FCFL 1.29%) |
| 31-Mar-2026 | 35,967,172 | 94.4% | 73.85% (SPCPL 69.71% + FCFL 4.14%) |
| 30-Jun-2026 | 35,967,172 | 94.4% | 73.85% (SPCPL 69.71% + FCFL 4.14%) |

Comment: the pledged share count is stable at 35,967,172 across all
three filings, and equals 100% of SPCPL's own direct 69.71% stake;
Forbes Campbell Finance Limited's 4.14% stake carries zero pledge (B08
`pledge_trend`). During FY26, SPCPL moved its only unpledged block,
1,470,000 shares, to Forbes Campbell Finance Limited, but the pledge
percentage on the combined promoter group did not change (B05, B08).
Institutional (FII+DII) holding: not separately re-extracted for this
annex; qualifies the UA multiplier per B01/B00, latest filing 30-Jun-2026.

### 10. Verification

Every document quoted in this annex, filename and date:
- Annual_Report_2026.pdf (Fourth Annual Report, FY2025-26, filed
  2-Jul-2026)
- Annual_Report_2025.pdf (FY2024-25, filed 2025) — cited via B02/B05
  extraction, not independently re-quoted in this annex
- Annual_Report_2024.pdf (FY2023-24, first AR) — cited via B02/B05
  extraction, not independently re-quoted in this annex
- Information_Memorandum_2024.pdf (dated 3-Jun-2024, 182p)
- Court_Order_Scheme_of_Arrangement.pdf (NCLT Mumbai order, 48p)
- shareholding__SHP_30Jun2026.txt (Shareholding Pattern as at
  30-Jun-2026)
- shareholding__SHP_31Mar2026.txt (Shareholding Pattern as at
  31-Mar-2026), shareholding__SHP_30Jun2025.txt (Shareholding Pattern as
  at 30-Jun-2025) — figures cross-checked, not independently re-quoted in
  this annex

CORPUS COMMIT HASH: 01a871f993b54818f5ea51e161ad3581f8baca7e
