# B09 SECTION 6 ADDENDUM — Downstream Signal Candidates
Permanent Magnets Ltd (PERMAGNET) | Run date: 2026-08-19
Surgical addendum on the newly-merged framework stack. Sections 1-5 of B09
(TAM/SAM/SOM, dated 2026-08-19) are NOT re-run and NOT changed by this
addendum; no committed B09 figure is recomputed. This document runs ONLY
Section 6 of prompts/09-tam-pipeline.md against the already-committed B09
report (runs/permagnet-2026-08-19/outputs/reports/B09-tam.md) and B04
business-model block, per frameworks/Downstream_Source_Discovery_Protocol_v1_0.md
PART 2 (Source Registry) and PART 3 (source hierarchy).

Method note: candidates below are NAMED per the registry's entity-type ->
likely-primary-source map. No URL verification and no web search was
performed for this addendum — that happens later at Role 5.5 per the
protocol. Where an entity's precise identity is not independently disclosed
in the source documents (the top-3 global meter OEMs), that gap is flagged
rather than a name invented.

---

## SECTION 6: DOWNSTREAM SIGNAL CANDIDATES

Six entities were extracted from the B09 TAM decomposition and the B04
revenue-mix block: two regulatory/policy entities, two counterparties, one
macro proxy, and one unnamed end-customer class. All six clear the
minimum-3 bar for external observability, so the "demand not externally
verifiable" fallback does not apply.

| # | Candidate Signal | Entity Type | Why It Drives Demand (<=20 words) | Likely Primary Source (per registry) | Expected Cadence | SHARED |
|---|---|---|---|---|---|---|
| 1 | India RDSS smart-meter rollout progress | Regulatory | 185mn of the 250mn RDSS target still to install (Apr-2026 base); direct driver of Segment A metering-component demand | Ministry of Power / REC (RDSS nodal agency) official rollout dashboard + PIB releases — registry Type 4 (SPV/parent-programme website, PIB, "what's new" page) | Monthly | true |
| 2 | Genus Power Infrastructures Ltd (India's largest listed AMISP, ~30% smart-meter share) | Counterparty | Its order-book and installation run-rate is the closest listed proxy for India smart-meter component pull-through PML rides | Genus BSE/NSE corporate announcements + concall transcripts + annual report — registry Type 1 (Indian listed company) | Quarterly | false |
| 3 | Global light-vehicle & EV production volumes (Western Tier-1 OEM base) | Macro | PML supplies ~50% of tier-1 global auto manufacturers; production volumes proxy demand for Segment B current/torque-sensing assemblies (23% of revenue) | SIAM monthly production data (India) + global trackers (S&P Global Mobility, LMC Automotive) — registry Type 7 (industry-association-type source) | Monthly | false |
| 4 | China NdFeB rare-earth export-licence regime (MOFCOM) | Regulatory | China holds ~92% of NdFeB capacity; licence policy directly gates whether Quantum Magnetics' pre-revenue NdFeB line can ship at all | MOFCOM export-licence announcements, cross-checked via credible trade press (Reuters, Argus Media, S&P Global Commodity Insights) — no China regulator entry exists in registry Type 5; trade-press fallback per Part 3 rank 5 | Event-driven | false |
| 5 | REL Developments Ltd (UK) — latching-relay technology licensor | Counterparty | UK licensor whose IP/contract status gates PML's guided H2FY27 relay commercial ramp, already stated behind original timelines | UK Companies House filings (unlisted-foreign-counterparty equivalent of registry Type 2 MCA filings) + REL Developments corporate/press disclosures | Event-driven | false |
| 6 | Top-3 global electricity-meter manufacturers (identity unconfirmed in filings) | End-customer | PML's largest disclosed customer class by its own claim ("top 3 global electricity meter manufacturers"); drives both Electricity Meters and CT revenue lines | Identity not independently named in AR-FY26 or B09 — a prerequisite research step, not yet a trackable source. Once identified: registry Type 3 (SEC EDGAR / foreign-listed OEM 10-K or annual-report supplier commentary, IR decks) | Quarterly | true |

### Notes on falsifying observations (already stateable)

- **#1 RDSS:** Falsifies if the cumulative-installed count on the RDSS
  dashboard stalls or grows materially below the run-rate implied by the
  Mar-2028 extended completion date (already extended once from the
  original target per B09 4B — a second slip would be a confirming
  negative).
- **#2 Genus Power:** Falsifies if Genus's own order book or quarterly
  installation disclosures decelerate sharply against the RDSS run-rate,
  signalling AMISP-side execution risk that would flow through to PML's
  component orders.
- **#3 Auto/EV production:** Falsifies if Western Tier-1 OEM production
  volumes decline while Chinese-OEM share gains accelerate — the risk
  already flagged in B09 Section 4B (AR-FY26 p.4-5) as pressuring PML's
  core Western customer base.
- **#4 China NdFeB export regime:** Falsifies (for the optionality thesis)
  if restrictions persist or tighten with no licence relief; confirms if
  any relaxation or India-specific carve-out is announced. Already
  producing a negative print: FY26 predecessor-line revenue was zero
  (AR-FY26 p.4/p.19).
- **#5 REL Developments relay licence:** Falsifies if no confirmed
  commercial relay launch occurs by H2FY27 as guided, or if a further
  delay is announced (management has already stated the programme is
  "behind original timelines," AR-FY26 p.4).
- **#6 Top-3 meter OEMs:** Not yet falsifiable — identity must be
  established first (via trade press, customs/shipment data, or a Western
  meter OEM's own filings naming an Indian shunt/CT supplier) before a
  dated verification point can be written.

### SHARED dependency flags

Two candidates are flagged SHARED because they touch more than one B04
revenue line (Electricity Meters 40% + CT 9%, both grouped as "Segment A"
in B09): **#1 RDSS rollout** and **#6 Top-3 meter OEMs**. Per the
protocol, these are correlated catalysts and FTTCP counts the RDSS/meter-
OEM demand chain once, not as two independent triggers, even though it
surfaces at two entity points in this table.

### Entity extracted but NOT converted into a candidate row

- **Copper / alloy input costs** — named in the run context as a macro
  variable, but it is a cost-side (margin) driver, not a demand-side
  driver of PML's TAM/SAM/SOM; Section 6 scopes to entities that drive
  demand, so this was excluded rather than mis-tagged.
- **DISCOMs / AT&C-loss health** — subsumed into candidate #1 (RDSS);
  listing separately would double-count the same underlying regulatory
  programme as a second independent trigger, which the SHARED-flag rule
  above exists to prevent.

---

## DEMAND EXTERNALLY VERIFIABLE: TRUE

Six candidate rows clear the minimum of 3 externally observable demand
drivers spanning regulatory, counterparty, and macro entity types (#6 has
a confirmed likely-source category even though the specific OEM identity
still needs a discovery step). The fallback sentence ("DEMAND IS NOT
EXTERNALLY VERIFIABLE...") does not apply.
