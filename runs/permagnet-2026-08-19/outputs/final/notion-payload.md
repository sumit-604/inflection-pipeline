Execute via the claude.ai project; never overwrite Decision Status.

# NOTION SAVE PAYLOAD — PERMAGNET (Permanent Magnets Ltd)

This is a payload, not an action. Do not write to Notion from the session. When executed
in the claude.ai project, append a new dated section to the company page; NEVER overwrite the
Decision Status row property without operator confirmation. The verifier-disagreement-log
rows (this run: "none") append to the separate "Verifier Disagreement Log" page.

## PAGE TITLE
PERMAGNET - Permanent Magnets Ltd (run 2026-08-19)

## RUN SUMMARY
Evidence gate PROCEED WITH FLAGS. Valuation decision AVOID at CMP Rs 882 (market cap Rs 758
Cr, 20-Aug-2026). Priced on the v3.6 Damodaran basis (operator directed), SOTP shape. A
cash-generative mature magnet/meter-component/alloys core is being priced at ~38x forward
core earnings while it earns 12.54% on capital, below its cost of capital; the transformation
(latching relays, NdFeB rare-earth magnets, both ECMS-approved) is real but lives in two
small, pre-revenue, execution-uncertain option slices. FTTCP composite +1 (DEEP WATCH leaning
AVOID). Confidence 57 (redflag-coverage-bound; source-fidelity PASS).

## VERDICT
- Evidence gate: PROCEED WITH FLAGS (rule 3)
- Valuation decision: AVOID (on-valuation)
- Devil's advocate: SURVIVES (AVOID robust; fair-value point estimate weakened, see caveat)

## VALUATION
- Destination PE: 17.3x additive / 14.1x RRM (RRM governs, sets entry zone). Pillar 3 +0x.
- SOTP fair value (approved base): Rs 330 (RRM) / Rs 404 (additive); bear 268-330, bull 392-471.
- Devil-corrected fair value: Rs 450-614 (core-ROCE double-count caveat, see below); AVOID survives.
- Entry range Rs 118-169 (approved base); devil-corrected entry Rs 230-314. MoS Rs 118.
- Hurdle Tier A: STOP (HR 0.52). Prob-weighted 3yr CAGR -14.5%.
- ZONE REACHABILITY: MARKET-UNLIKELY. Entry top Rs 169 is 72.7% below the 52-week low Rs 619;
  even the devil-corrected Rs 314 is far below CMP. Classify DEEP WATCH, not actionable
  WATCHLIST. Price history beyond 52 weeks unavailable (no PERMAGNET screening CSV).

## LOAD-BEARING CAVEAT (devil's advocate)
The core multiple was set off CONSOLIDATED ROCE 12.54% while the SOTP already quarantines the
loss-making QMPL subsidiary into a separate slice with its debt in the bridge, a double-
penalty. Stripping QMPL, core operating ROCE is ~16% (above cost of capital), so the fair
value is ~35% understated and the Amendment 16 Pillar-3 gate could flip for the core. Decision
AVOID survives even the corrected ceiling Rs 614. Flagged for the operator to revisit the
core-ROCE input at the next refresh.

## ACTIVE FLAGS
FLAG-GATE0 (AVERAGE 57/160); FLAG-PROMOTER (CAUTION); FLAG-CASH (GROWTH-INDUCED); FLAG-
SUBSIDIARY (QMPL revenue -85.5%, Rs 47.81 Cr ECB, D/E +238%); FLAG-EXECUTION (relays + NdFeB
behind timelines); FLAG-GOING-CONCERN (2015 winding-up EoM; Rs 22.01 Cr excise contingency).

## THESIS-BROKEN / RE-ENGAGE TRIGGERS
Becomes investable only on the conjunction: a durable ROCE crossover above ~13.5% cost of
capital printing in audited financials (Module B2 turns growth-premium eligible) AND relay or
NdFeB revenue appearing in a filing AND price inside Rs 118-169 (or the devil-corrected
230-314). None has printed.

## MONITORING CHECKLIST
1. Q2FY27 standalone core operating PAT down YoY on positive revenue growth (falsification).
2. Consolidated ROCE stays below ~13.5% / STAGNANT (keeps Pillar 3 gated).
3. Relay: named customer qualification + revenue line by H2FY27; red if slips a second time.
4. QMPL NdFeB Phase 2 commissioned Q3FY27 + first sales Q4FY27; red if delayed / ~zero into FY28.
5. Cash: receivables growth <= revenue growth and consolidated FCF turns positive.
6. Net debt below ~Rs 27 Cr; red if full Rs 47.81 Cr ECB drawn or going-concern EoM persists.
7. Price enters Rs 118-169 (or 230-314 corrected) AND checklist otherwise green; no entry above.
8. 2015 winding-up EoM removed and Rs 22.01 Cr excise interest dispute closed with no liability.

## CONFIDENCE DELTA
Numerical 100 | Redflag-coverage 57 | Framework-adherence 96 | Peer-utilisation 100 | Overall 57.
Source-fidelity gate PASS (Verifier A 101 figures, 0 findings). Phase-3 valuation adherence 92%
(0 CRITICAL/0 MAJOR); destination PE applied faithfully, no silent re-derivation.

## PUBLISH CANDIDATE
Flagged. Teaching case: standalone accounts look healthy (PAT +36%, FCF positive) while
consolidated is dragged by a pre-revenue subsidiary that drew a Rs 47.81 Cr unsecured ECB the
same year its own revenue fell 85.5%. Consolidated reality overrides a flattering standalone
headline. Drafting deferred.

## LINKS
- Run folder: runs/permagnet-2026-08-19/
- Drive folder: NOT PROVIDED

---

## POST-HOC ADDENDUM PROVENANCE (2026-08-21)
Downstream Signal Candidates (stage 9 SECTION 6) and this tracker payload were added
post-hoc on 2026-08-21 after syncing the branch to origin/main (the 20-Aug framework
wiring: SECTION 6, Signal Gate, Downstream_Source_Discovery_Protocol_v1_0, tracker payload).
The committed valuation record (PROCEED WITH FLAGS / AVOID, SOTP fair value Rs 330-404,
Hurdle STOP) was NOT re-run and is unchanged. This is a signal-tracking addendum only.

## DOWNSTREAM SIGNAL TRACKER PAYLOAD (candidates for Role 5.5 verification)
Target database: DOWNSTREAM SIGNAL TRACKER, data_source_id
926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f. Write happens at Role 5.5 in claude.ai AFTER source
verification, NOT from this pipeline. demand_externally_verifiable: TRUE (6 candidates).

| Signal | Entity type | Demand link | Likely primary source (per registry) | Cadence | Shared | Falsifying observation (if stateable) |
|---|---|---|---|---|---|---|
| India RDSS smart-meter rollout progress | Regulatory | 185mn of 250mn RDSS target still to install; drives Segment A metering-component demand | Ministry of Power / REC (RDSS nodal agency) rollout dashboard + PIB | Monthly | SHARED | Monthly installed count stalls or falls below the run-rate needed to reach 250mn by 2028 |
| Genus Power Infrastructures Ltd (largest listed AMISP, ~30% share) | Counterparty | Order-book / installation run-rate is the closest listed proxy for India smart-meter component pull-through | Genus BSE/NSE announcements + concall transcripts + AR | Quarterly | — | Genus order-book or installation run-rate declines QoQ for 2 consecutive quarters |
| Global light-vehicle & EV production volumes (Western Tier-1 base) | Macro | PML supplies ~50% of tier-1 global auto makers; production proxies Segment B sensing demand | SIAM monthly data + S&P Global Mobility / LMC Automotive | Monthly | — | Global light-vehicle production prints negative YoY for 2+ months |
| China NdFeB rare-earth export-licence regime (MOFCOM) | Regulatory | China ~92% of NdFeB capacity; licence policy gates whether QMPL NdFeB line can ship | MOFCOM export-licence announcements, cross-checked Reuters/Argus/S&P Commodity Insights | Event-driven | — | Further MOFCOM tightening blocks QMPL input access (or easing removes the China+1 rationale) |
| REL Developments Ltd (UK) - latching-relay technology licensor | Counterparty | UK licensor whose IP/contract status gates PML's guided H2FY27 relay ramp | UK Companies House filings + REL Developments disclosures | Event-driven | — | Licensor insolvency, or licence lapse/dispute filed at Companies House |
| Top-3 global electricity-meter manufacturers (identity unconfirmed) | End-customer | PML's largest disclosed customer class; drives both Electricity Meters and CT revenue lines | Identity not named in filings; once identified, SEC EDGAR / foreign-listed OEM 10-K supplier commentary | Quarterly | SHARED | Not yet falsifiable until customer identity is discovered |

### AR first-disclosure rows (Step 10.5B feed for the Role 5.5 AR annual cross-check)
Derived from the committed B03 (B03 predates the ar_new_downstream_entities field; entities
extracted from the B03 report content). One row per entity: name | entity type | where in AR.

| Entity | Entity type | Where in AR |
|---|---|---|
| REL Developments Ltd (UK) | Counterparty (relay technology licensor) | AR-FY26 Strategic Priorities p.11; Chairman's letter |
| RDSS smart-meter programme (Ministry of Power / REC) | Regulatory / Macro | AR-FY26 MD&A p.15-19, p.28-29 (250mn target, 65mn installed Apr-2026) |
| Global NdFeB market / China ~92% capacity (Neo Performance Materials, US DOE data cited) | Macro | AR-FY26 p.15-19 (industry/market section) |
| NOTE: no specific meter or auto OEM customer is named in the AR | End-customer | Customer concentration NOT DISCLOSED (AR-FY26; B03 "No customer concentration disclosure found") |

This section is a payload, not an action. The pipeline never writes to the tracker; Role 5.5
does, after source verification. The operator executes the save in the claude.ai project.
