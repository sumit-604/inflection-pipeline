# ENTERO HEALTHCARE SOLUTIONS — HALT 1 PACKAGE (REVISED)
Prepared 29 August 2026 for operator sign-off.
Run folder: runs/entero-2026-07-27
Company record: companies/ENTERO.md
Notion COMPANIES MASTER page: 3abbb2b9-d3ab-81ee-bf38-ef32aab39417
This package supersedes the draft mental model in
outputs/reports/09b-understanding-dossier.md. Nothing here is written to
Notion or the repo until the operator signs.

Provenance: claude.ai live-verification layer, operator-ferried into the run
folder on 2026-08-29 as the FTTCP web-handover-dossier. Entity count: ONE
(Entero Healthcare Solutions Ltd, consolidated single Ind AS 108 segment).

SUPERSEDING CORRECTION (operator ruling 2026-08-30, governs this file):
Where PART 0 item 4, PART 2 B2, and PART 2 B5 below state the NET CASH OUTFLOW
per Rs 100 of acquired revenue is ~Rs 8, that is WRONG. Rs 8 is the GOODWILL
component only. The net cash outflow is the full Rs 24 (Rs 15-16 working
capital acquired + Rs 8 goodwill); the two-year payback applies to the Rs 8
premium, not the Rs 24. Pillar 1 ROCE ruled at 20-25% -> 19x on the
forward-capital basis (dissent 12x on standard EBIT/avg capital incl.
goodwill). Use the corrected reading; see companies/ENTERO.md operator ruling
2026-08-30.

---
## PART 0 — CORRECTIONS REGISTER
Eight corrections were made during this cycle. Recording them openly, per
the team workflow rule on corrections without ego.
| # | What I said | What is correct | Source |
|---|---|---|---|
| 1 | The entero folder existed only on a stranded branch | It is on main; the browser tab was sticky on the claude branch | Repo clone, verified |
| 2 | Keimed earns 5-6% EBIT margin, validating Entero's path | Keimed reports 3.1-3.4%; adjusted for Apollo preferential pricing it is 4.5-5.0% | Apollo disclosure; FY24 Keimed accounts |
| 3 | Entero's 5% margin may be unsustainable versus the market leader | Keimed's arms-length margin is the same 4.5-5.0%. Entero's 5% is normal, not anomalous | Same |
| 4 | The engine is multiple arbitrage, so the model is reflexive on the share price | Net cash outflow is ~Rs 8 per Rs 100 of acquired revenue after taking over Rs 15-16 of working capital. Two-year cash payback. Deals work at any multiple | Q4 FY24 concall, management |
| 5 | Gross margin expansion is the strongest evidence of transition | The Q1 FY27 print is contaminated twice, by the sub-distribution exit and by GLP-1 genericisation | Q1 FY27 concall; NPPA/generic launch dates |
| 6 | Organic growth is 13-14% | Latest print is 19.6%; four-quarter trailing average is ~15-16% | Q1 FY27 concall |
| 7 | There is no operating leverage in this business | IPM units grew 0.6% MAT against 8.6% value. Costs scale with units, revenue with value. Leverage is real, and was masked by acquisition-added cost base | PharmaTrac MAT Mar 2026 |
| 8 | Promise ledger reads 8 delivered, 4 partial, 0 missed | Against annual guidance packages: FY24 directional delivery with growth shortfall, FY25 clear miss on all three of growth, margin and OCF, FY26 clean beat | Walk-the-talk analysis, FY24-FY26 |
Two further items that were not corrections but were absent from the
pipeline entirely: trade margin rationalisation as a live regulatory
process, and the fact that IPM growth is almost entirely price and mix
rather than volume.

---
## PART 1 — CORPUS AUDIT
Claude Code's verdict: CORPUS GAPPED. Confirmed against the actual file
listing. I do not recommend accepting CORPUS CURRENT.
### Held and adequate
Five concall transcripts covering Aug-25 through the Q1 FY27 call. FY26
annual report, 276 pages, filed 27-Jul-2026. Q1 FY27 results and
presentation. India Ratings IND A-/Stable dated 03-Dec-2025, image-only
PDF readable via poppler. Four concalls each for MedPlus, Redington and
RPTech. Screener CSVs for all peers.
All four freshness pairs pass.
### Gaps, with sources
| Gap | Severity | Where to get it |
|---|---|---|
| IPO prospectus (DRHP dated 13-Sep-2023) | HIGH | Located. Hosted on enterohealthcare.com. Fetchable today. |
| FY25 annual report | HIGH | Overwritten during the 29-Aug upload under the same UUID filename. Recoverable from git history, or from the Entero IR page. |
| Reg 30 announcement PDFs | MEDIUM | BSE/NSE announcements. All CFO, CS and director-change facts currently rest on general web search. |
| Quarterly shareholding pattern, 12 quarters | MEDIUM | BSE/NSE Reg 31(4). Pledge percentage unconfirmed. |
| AGM scrutiniser report, 19-Aug-2026 | MEDIUM | BSE filing. Stage 8 used scanx.trade, a secondary source. |
| Research folder | LOW | Empty. Two broker notes misfiled in presentation/, correctly treated as leads only. |
### Unresolved data discrepancies
Q1 FY27 dating. ENTERO.md records the concall as 10-Aug-2026 and results
as 17-Aug-2026. The dossier has results 07-Aug-2026 and concall
17-Aug-2026. These are swapped relative to each other and need settling,
because concall-newer-than-results is the freshness rule.
Network reach counts. Three different sets of Q4 FY26 figures exist across
the dossier, the forum notes and the company deck. The metrics themselves
are unstable and should not carry a tracker row.
Leverage. Three non-reconciled figures: adjusted net D/E 0.02x to 0.23x,
consolidated D/E 0.09x to 0.31x, and standalone Note 57 ratio analysis at
0.06x.
ROCE. Company reports 21.1% for Q1 FY27. Balance-sheet-derived is ~10.5%.
A third-party trace shows below 2% in FY21 rising to ~10% in FY26 and
10.7% in FY25. The weight of evidence favours the lower figure. Pillar 1
cannot run until the denominator is settled.
### Structural finding
PR #111 merged only stages 00 through 05 to main. Stages 06, 07, 08, 09,
09b and all four verifier reports sit on branch
`claude/pipeline-run-entero-pchzpu` at commits 44750e7 through 7199bd8 and
are not on main. A second PR is required or every future session runs on a
half-finished Phase 1.
Separately, branch `claude/entero-pipeline-run-ndqp3v` carries a complete
July run through devil's advocate and finalize, ending AVOID, also
unmerged.

---
## PART 2 — SIGNED MENTAL MODEL (FOR OPERATOR SIGNATURE)
### A1. ARCHETYPE
A working-capital-financed distribution roll-up that has reached
self-funding scale, now layering a value-added MedTech business on top of a
maturing core.
The binding constraint is working capital, not capacity, not market size.
B09 sizes the incremental funding gap at Rs 1,000-1,100 crore by year
three. The self-funding threshold is specific: the business funds its own
growth up to roughly 15-16%. Above that the loop needs external capital.
This is not the Outsourcing-Partner archetype the draft proposed, and it is
not a multiple-arbitrage machine as I argued earlier.
### A2. THE SIMPLE ANALOGY
Entero buys medicines and medical devices in bulk from manufacturers and
moves them through leased warehouses to retail pharmacies and hospitals,
earning a thin percentage on each rupee moved. It grew by buying regional
distributors, and it is now adding a device and diagnostics line where it
gets paid for selling rather than merely delivering.
### B1. FROM AND TO
Important reframe. The first transition is complete.
| Metric | FY21/22 | FY26 | Q1 FY27 |
|---|---|---|---|
| EBITDA margin | 1.0% | 4.0% | 5.0% |
| Gross margin | 8.0% | 10.3% | 11.4% |
| Operating cash flow | negative | +Rs 96 Cr | positive |
| ROCE | ~1-2% | ~10-14% | 21.1% reported |
The climb from cash-burning sub-scale roll-up to self-funding scaled
distributor happened between FY22 and FY26, in public, quarter by quarter.
The market watched it. Median EV/EBITDA since listing is 24.2x.
FROM (today): a scaled, self-funding distributor at the top of the R2
band. Not R1. The R1 characterisation in the draft was drawn from the FY26
annual report, which is one quarter and one inflection stale.
TO (claimed): R3 value-added supplier, via MedTech mix rising from
~15% to ~20% of revenue and a growing share of commercial-role contracts.
The R4 claim is recorded separately as aspiration, not guidance.
Management guides ROCE of 25-30% within 3-4 years. The disclosed mechanism
supports R3. The number is R4. The rung-jump rule applies, and the ROCE
denominator is itself contested at 21.1% versus ~10.5%.
### B2. THE ENGINE
Four components, in order of contribution.
1. Scale-led procurement economies. Confirmed by the CEO as the primary
   driver of pharma gross-margin gains. Available to any scaled player,
   including Keimed.
2. MedTech mix shift. From ~15% toward ~20% over 2-3 years. Working the
   arithmetic from management's own figures, the full mix shift is worth
   roughly 35 basis points of EBITDA, against guidance of 50-75. Useful,
   not decisive.
3. Commercial-role and demand-generation contracts. Roughly 15% of sales.
   Entero deploys medical representatives to promote brands to doctors.
   Named relationships: Roche since June 2020 for four nephrology drugs,
   plus an MNC cardiac device arrangement.
4. Operating leverage via value-over-volume divergence. IPM value grew
   8.6% MAT while units grew 0.6%. Distributor revenue scales with value;
   distributor cost scales with volume. With acquisitions paused, Entero's
   own unit growth converges toward organic customer additions while value
   growth tracks 1.4-1.5x IPM. The gap is margin.
Correction to the draft engine description. The draft states neither change
requires new physical assets, citing organic PP&E additions of 2.4% of
revenue in FY26. That is wrong for the IVD portion. Management disclosed
that IVD requires placing machines at customer sites against five-year
revenue contracts, with correspondingly higher depreciation. As MedTech
scales, capex intensity rises.
### B3. THE PROOF GATE
Four legs, all testable in the Q2 FY27 print or the H1 FY27 balance sheet.
1. Consolidated EBITDA margin at or above 5.0% for two consecutive
   quarters. Touched once in Q1 FY27.
2. Gross margin continuing to expand on a clean basis. Q2 FY27 is the
   first quarter free of both the sub-distribution exit and the GLP-1
   genericisation mix effect.
3. OCF-to-EBITDA conversion reaching the guided 50%.
4. Minority interest falling from 38% of PAT toward the guided 25-27%,
   evidenced by actual subsidiary stake purchases.
Both cash legs matter because a margin gain that does not convert is
consistent with receivables outrunning revenue, which is already happening
at 1.7x.
### B4. THE RECOGNITION GAP — CLOSED, AND IT IS THE PROBLEM
The draft leaves this open for Stage 11. On the evidence assembled it can
be answered now.
The first transition is priced in. Median EV/EBITDA since listing is 24.2x.
Trailing P/E was 47.06x at Rs 1,345.60 on 10-Aug-2026, with P/B at 3.40x.
Screener flags a three-year average ROE of 6.04%. The stock then moved from
Rs 1,377.80 on 25 August, where 3P Investment bought 2.5% from the Prasid
Uno Family Trust, to roughly Rs 1,800 on 28 August. About 30% in three
days on a block trade.
The re-rating engine is largely spent. What remains is the second, smaller
transition and the earnings growth.
### B5. THE UGLINESS TEST — UNRESOLVED
Goodwill at ~44% of consolidated net worth. Forty of about 65 subsidiaries
carrying adverse or qualified CARO clauses, mostly Clause xvii cash losses.
Cumulative CFO of minus Rs 203 Cr against cumulative PAT of plus Rs 193 Cr
across FY20-FY26. Receivables growing 1.7x faster than revenue.
The draft classifies this provisionally as ARTIFACT-OF-CLIMB. I recommend
downgrading to genuinely UNRESOLVED. The CARO count is a single-year
snapshot with no prior-year comparable, and B03's own note says whether
that population shrinks determines the transition posture more than any
other number in the annual report. It cannot be resolved before the FY27
annual report, roughly twelve months away.
One mitigating fact the draft lacks. The goodwill overstates capital
deployed. On management's own deal arithmetic, buying Rs 100 of revenue at
6x EV/EBITDA costs Rs 24 of enterprise value, but Rs 15-16 of working
capital comes across with the business, so net cash outflow is about Rs 8.
The full Rs 24 sits in capital employed. That is why goodwill looks
alarming while the cash economics look sound. Both readings are real.
### B6. TRANSITION FALSIFIERS
The climb is falsified if any of these fire.
1. Blended gross margin fails to expand over 2-3 sequential quarters
   despite a rising claimed MedTech share.
2. EBITDA margin regresses toward 4% after touching 5%.
3. The organic growth multiple over IPM falls to 1.2x or below.
4. Minority interest fails to fall toward 25-27% of PAT, leaving
   attributable earnings materially below every forward projection.
### B7. BUSINESS FALSIFIERS — THREE-CHANNEL REGULATORY STRUCTURE
Distinct from B6. These break the underlying business, not just the climb.
Channel 1 — Direct trade margin capping on non-scheduled drugs.
Probability within three years: 15-20%, revised down twice during this
cycle. Impact if it fires: largest. A 100bps gross margin cut is Rs 81 Cr,
which is 20% of EBITDA.
Why lower than I first assessed. The prospectus puts the distributor
margin band at 8-15%, against manufacturers at 40-60%, retailers at 20-25%
and hospitals at 35-40%. The fat is not at the distributor layer. The
committee's own cited cases were drugs with MRPs of Rs 38,215 selling at
Rs 9,200, which is upstream pricing, not an 11% distributor spread. The
DoP has itself written down why distributor margin exists, citing logistics
costs, inventory carrying, expiry risk and weak credit access. MSME
resistance on rural supply has held TMR up since 2017. And the NPPA raises
prices as well as cutting them, granting one-time 50% increases in July
2021 and October 2024 where supply was at risk, plus a recent oncology
ceiling increase.
Channel 2 — Device scheduling of Entero's cardiology portfolio.
Probability within three years: 45%. Impact: moderate.
The parliamentary committee recommended incorporating high-volume
diagnostic and therapeutic devices, naming advanced pacemakers, ophthalmic
lenses and implantable pumps, into the DPCO scheduled list. Entero
distributes the Medtronic Quad CRT-P, which is a pacemaker. Coronary stents
and knee implants are already under NPPA ceiling prices, with the latest
knee implant extension running to 15 November 2026. Entero's MedTech
portfolio sits in exactly this space.
The existing device precedent is a 70% cap on price to distributor, set
against importers running 198% margins. Against a device distributor
earning perhaps 22%, that cap is not binding.
Channel 3 — Hospital and diagnostic price capping, transmitted upstream.
Probability within three years: 35%. Impact: moderate to severe, and
hardest to monitor.
The same committee recommended immediate formulation of a mechanism to
standardise and cap costs of essential treatments, diagnostics and routine
procedures across all private hospitals, with mandatory price transparency
and an ombudsman. Hospitals currently take 35-40%. Entero has the largest
hospital customer network among Indian pharma distributors at 3,600+, and
Anand Chemiceutics serves 1,500+ customers weighted to hospitals and
diagnostic labs. Capped hospitals push the squeeze up the chain.
Channel 4 — Manufacturer de-authorisation. 99.22% of revenue is sale of
traded goods contingent on distribution authorisation, with no
concentration figure disclosed. GLP-1 alone may be around 10% of revenue
across two foreign manufacturers, on my inference from Mounjaro running at
Rs 100 crore a month as the top-selling brand in India.
A structural defence worth recording. Manufacturer-paid commercial fees and
private label sit outside the price-to-distributor to MRP calculation that
TMR governs. As the commercial-role share rises, the share of margin
exposed to trade-margin capping falls. This is not a deliberate hedge but
it functions as one. The tension: it moves Entero out of one regulatory
line of fire and into the device-scheduling one.
### C1. DOMINANT VARIABLES (REVISED)
| # | Variable | Current state |
|---|---|---|
| 1 | Organic growth as a multiple of IPM | 1.42x Q1 FY27, compressed from 1.7x across three quarters |
| 2 | Blended gross margin | 11.4%, against a prospectus band ceiling of 15% |
| 3 | OCF to EBITDA conversion | Guided 50%. FY26 OCF Rs 96.2 Cr after six negative years |
| 4 | Minority interest as % of PAT | 38% in Q4 FY26, guided to 25-27% in FY27 |
| 5 | CARO-qualified subsidiary count | 40 of ~65, no prior-year comparable |
Removed from the draft list: network reach, because it is explained by the
sub-distribution divestment plus a reporting-basis change and the metrics
are unstable across three data sets; and MedTech mix as a standalone,
because it is unauditable under single-segment reporting and gross margin
is the working proxy.
### C2. WHAT THE MODEL REJECTS
TAM sizing debates. Runway is already STRONG at 39.9x revenue headroom
with SAM share at 2.5%.
The absolute IPM percentage in isolation. What matters is Entero's
multiple over whatever IPM prints.
The tech-platform framing. Entero Direct, Teqtic and HealthEdge serve
master data management, which serves inventory efficiency. Real value, but
an enabler, not a product with independent economics.
US-convergence framing. Management rejected it themselves. The US top
three hold 90-95%; the realistic Indian bound is CRISIL's 20-30% by FY28,
or even 15%, which still triples the organised pool.
### C3. THE MOAT — UPGRADED
Three components, and the first is the one the pipeline missed.
Master data management. When Entero acquires a distributor, the first
operation is mapping its product codes to Entero's centralized codes. That
gives visibility of the same SKU across 136+ warehouses and lets inventory
move from surplus to deficit locations. The ERP was built in-house from
inception, so the source code is owned and integration is unconstrained.
Management's own framing, offered in response to an analyst who observed
minimal physical automation at a warehouse: in distribution, information
velocity matters more than physical automation. This compounds with every
acquisition and cannot be bought with capital alone.
Exclusive sole-distributor arrangements, ~15% of sales. For many small and
mid-sized manufacturers Entero is the sole pan-India distributor, running
end-to-end customer development, service, equipment installation, network
creation and product launch. A full agency model. Gross margins are
materially better than fulfilment work.
MedTech principal relationships. Through the three FY26 acquisitions Entero
distributes for Abbott, Medtronic, Terumo, MED-EL, Asahi, BrainsWay and
Sechrist. Products include drug-eluting coronary stents, cochlear implants,
deep TMS neurostimulation, hyperbaric oxygen systems, and IVD platforms
including Abbott Alinity, BD BACTEC and Cepheid GeneXpert. These are
tier-one global principals that would take years to assemble organically.
Not a moat: pricing power on core pharma, where B04 scores price-taker;
technology as a product; regulatory protection, since exclusivity is
discouraged as it emerges.
Capability gap. Entero's warehouses have temperature monitoring systems,
not cold chain. Management states warehouse fit-out capex is Rs 30-40 lakh,
covering racks, cooling and basic IT. That does not buy validated cold
chain. Keimed operates 96 distribution centres with cold chain
infrastructure. This is a gap on biologics, insulins, vaccines and GLP-1
injectables.
### C4. COMPETITIVE POSITION — REFRAMED
Keimed did Rs 10,300 crore in FY24 growing 20% a year, with reported
EBITDA margin of 3.4% and adjusted arms-length margin of 4.5-5.0% after
allowing 1.0-1.5 points for preferential Apollo pricing.
Apollo group entities contributed 54% of Keimed's FY24 revenue, up from
49%. So Keimed is roughly Rs 5,600 Cr captive Apollo supply and Rs 4,700
Cr genuine third-party. Entero's Rs 6,591 Cr is essentially all
third-party.
Entero is arguably the largest genuinely independent third-party pharma
distributor in India. Apollo's "2x the nearest competitor" claim counts
captive volume. Independence is a real differentiator: independent
pharmacies resist buying from a competitor's supply arm, and manufacturers
wanting neutral national reach cannot use the Apollo-aligned option.
The counterweight: Apollo HealthCo, Apollo 24/7 and Keimed are merging,
with the composite scheme approved by shareholders on 24 June 2026, SEBI
clearance secured, NCLT awaited, and listing targeted by Q4 FY27. The
merged entity targets Rs 25,000 crore revenue at roughly 7% EBITDA. That
creates a listed comparable, ends Entero's only-listed-pure-play scarcity
premium, and produces a second well-funded listed acquirer competing for
the same regional distributors.

---
## PART 3 — DEMAND CHAIN MAPS
Per Downstream Source Discovery Protocol v1.0 Part 1. One map per material
revenue stream. To be saved to the Notion company page.
### Map A — Core pharma distribution, fulfilment role (~85% of revenue)
| Field | Content |
|---|---|
| Product | Prescription and OTC medicines, per pack, from ~3,000 manufacturers, 83,400+ SKUs |
| Delivered by | Entero parent plus 48 subsidiaries |
| Service scope | Takes inventory ownership, extends 30-90 day credit, delivers. Does not create demand. |
| Direct customer | Retail pharmacies and hospitals |
| Demand driver | IPM value growth plus share gain from ~65,000 unorganised distributors |
| Chain dependencies | 1. Manufacturer authorisation, no concentration disclosed. 2. State drug licences, five-yearly, state-varying. 3. NPPA ceiling prices on NLEM drugs. 4. NPPA trade margin policy on non-scheduled. 5. GST rates. 6. Retail pharmacy solvency. |
| Verification points | Confirms: IPM MAT holding above 10% with Entero multiple stable or widening. Falsifies: multiple to 1.0x, or a TMR notification covering non-scheduled formulations. |
### Map B — MedTech and device distribution (~15% of revenue)
| Field | Content |
|---|---|
| Product | Cardiology devices, IVD, ENT, CNS, wound management, surgical consumables, homecare devices |
| Delivered by | Ace Cardiopathy (60%), Bioaide Technologies (80%), Anand Chemiceutics (51.51%) |
| Service scope | Full commercial role. In IVD, places capital equipment at customer sites against five-year revenue contracts. |
| Direct customer | Hospitals, corporate chains, standalone and chain diagnostic labs, sub-distributors. Anand alone serves 1,500+. |
| Demand driver | Hospital capex, diagnostics volume, device penetration from a low base. Indian device market USD 14-16bn growing 12-14%, Entero at ~0.5% share. |
| Chain dependencies | 1. Hospital chain capex cycles. 2. CDSCO device registration. 3. NPPA device pricing, TMR already applied to six categories. 4. Import dependency, so customs and currency. 5. Five-year IVD contracts as both lock-in and capital commitment. |
| Verification points | Confirms: diagnostics chain expansion, MedTech crossing Rs 1,000 Cr organically. Falsifies: device scheduling covering Entero's cardiology categories, or hospital occupancy below ~65%. |
### Map C — Demand generation and exclusive arrangements (~15% of sales, overlapping A and B)
| Field | Content |
|---|---|
| Product | Sole national distribution plus commercial partnership for manufacturers without field forces |
| Service scope | Widest. Medical representatives promoting to doctors, marketing strategy, channel management, product launch, equipment installation. |
| Named relationships | Roche, since June 2020, four nephrology drugs. An MNC cardiac device arrangement. |
| Demand driver | Small and mid-sized manufacturers outsourcing rather than building distribution |
| Chain dependencies | 1. The manufacturers, mostly unlisted. 2. Regulatory attitude to exclusivity, currently discouraging. 3. Keimed and Ascent offering the same service. |
| Verification points | Confirms: the 15% share rising. Falsifies: regulatory action on exclusive distribution, or the share stalling. |
### Shared dependencies (counted once in FTTCP composite probability)
1. NPPA pricing and trade margin policy. Appears in all three maps. The
   largest correlated exposure in the thesis.
2. State drug licences. Maps A and B.
3. Retail and hospital customer credit health. Maps A and C, and where the
   1.7x receivables growth lives.

---
## PART 4 — TRACKER ROWS FOR ROLE 5.5
Fourteen rows for the DOWNSTREAM SIGNAL TRACKER
(data_source_id 926b65ce-ddd2-4d8b-8eae-05e66b6f6c9f), each linked to the
COMPANIES MASTER row. These are PAYLOADS; claude.ai executes the writes and
records the row-URL proof (the FTTCP Role 5.5 tracker gate needs those URLs).
### Tier 1 — thesis-deciding
1. NPPA trade margin rationalisation, drug channel. Source rank 1.
   Event-driven, monthly. Next check 30 Sep 2026. Falsifier: any
   notification extending TMR to non-scheduled formulations. Source:
   nppa.gov.in; DoP action-taken reply to the 33rd Report.
2. NPPA device scheduling, MedTech channel. Source rank 1. Event-driven,
   monthly. Next check 30 Sep 2026. Falsifier: pacemakers/implantable
   pumps/cardiology devices added to DPCO schedule. Source: nppa.gov.in.
3. Hospital and diagnostic price capping, transmitted channel. Rank 1 when
   it fires, currently unsourced. Open item: needs a named primary source.
4. Q2 FY27 proof gate. Quarterly. Next check Nov 2026. Falsifier: EBITDA
   <5.0%, or OCF/EBITDA <50%, or continued refusal to disclose quarterly
   cash flow. Source: enterohealthcare.com results.
5. Organic growth multiple over IPM. Quarterly. Next check Nov 2026.
   Current 1.42x. Falsifier: multiple to 1.2x or below. Source: Entero
   concall + PharmaTrac.
6. IPM unit growth versus value growth. Monthly. Next check 30 Sep 2026.
   Current 0.6% units vs 8.6% value MAT. Source: PharmaTrac.
7. Blended gross margin, clean basis. Quarterly. Next check Nov 2026.
   Falsifier: flat/declining GM without a divestment/acquisition reason.
8. Minority interest as % of PAT. Quarterly. 38% Q4 FY26 -> guided 25-27%.
   Falsifier: >32% at H1 FY27.
### Tier 2 — competitive and structural
9. Keimed revenue, margin and Apollo captive share. Quarterly at Apollo.
10. Apollo HealthCo demerger and listing. Event-driven, Q4 FY27 target.
11. Ascent scale and funding. Annual. Source: rating rationales, MCA.
12. GLP-1 India performance and tirzepatide patent status. Quarterly.
    Source: SEC EDGAR Lilly/Novo; EDGAR full-text search "Entero".
13. Hospital occupancy at major chains. Quarterly. Apollo 70% at 30-Jun.
14. Diagnostic chain capacity expansion. Quarterly. Agilus/Metropolis/Dr Lal.
### Tier 3 — slow moving
15. CARO-qualified subsidiary count. Annual. Next check Jul 2027. 40 of ~65.
16. Price trigger. Entry Rs 1,240. MoS Rs 995.

---
## PART 5 — VALUATION FRAME AND ENTRY ZONE
Not a Role 1 valuation. Entry-price anchor for the WATCHLIST decision, to be
superseded when Stage 11 runs.
### Base case build
15% organic growth, no new M&A. EBITDA margin 5.0% -> 5.9% by FY30.
PAT/EBITDA 53% -> 58%. 4.35 crore diluted shares.
| Year | Revenue | EBITDA margin | EBITDA | PAT | EPS |
|---|---|---|---|---|---|
| FY27 | Rs 8,107 Cr | 5.0% | Rs 405 Cr | Rs 215 Cr | Rs 49 |
| FY28 | Rs 9,323 Cr | 5.3% | Rs 494 Cr | Rs 272 Cr | Rs 63 |
| FY29 | Rs 10,721 Cr | 5.6% | Rs 600 Cr | Rs 339 Cr | Rs 78 |
| FY30 | Rs 12,329 Cr | 5.9% | Rs 727 Cr | Rs 422 Cr | Rs 97 |
Bear: 12% organic, margin 5.0%, minority ~32%. FY30 EPS ~Rs 68.
Bull: 20% organic, margin 6.4%, minority 25%. FY30 EPS ~Rs 138.
### Entry price at each exit multiple (3-year horizon to FY30, entry = FY30 price / 1.25^3)
| Exit PE | FY30 price | Entry for 25% CAGR | Entry for 30% CAGR |
|---|---|---|---|
| 20x (framework hard cap) | Rs 1,940 | Rs 993 | Rs 883 |
| 25x | Rs 2,425 | Rs 1,242 | Rs 1,104 |
| 30x | Rs 2,910 | Rs 1,490 | Rs 1,325 |
Open item for the operator. Section 1B has no pharma/MedTech distribution
sector-cap row. July run set 15.0x by operator ruling; collector's Pharma/CDMO
38x corrected to Cybersecurity/VAD 25x. Market evidence: median EV/EBITDA
since listing 24.2x. Recommendation: a row at 18-20x, entry near Rs 993-1,120.
### Recommended zone
Entry zone: Rs 1,000 to Rs 1,240 (20x to 25x exit). MoS price: Rs 995 (20%
below the 25x entry). Current price: approximately Rs 1,806. 3P Investment
bought at Rs 1,377.80 on 25-Aug-2026.
### Cross-check
Independent base case: FY28 attributable EBITDA Rs 383 Cr on 22% growth,
5.2% margin. At 18x: EV ~Rs 6,890 Cr, equity ~Rs 6,550 Cr, ~Rs 1,505/share
by FY28. From Rs 1,806 negative. At 24x (historical median): ~Rs 2,035, or
4% CAGR. Two independent builds land in the same place: the business can
deliver what management promises and the return from Rs 1,806 is still poor.

---
## PART 6 — HALT 1 DECISION
SHALLOW WATCH (claude.ai recommendation).
Not KILL: business case genuinely decent, improved this cycle; clean
two-year cash payback; real moat incl. master data capability; tier-one
MedTech principals; 0.5% share of a device market growing 12-14%; IPM
verified; FY26 clean beat.
Not PROCEED (claude.ai view): transition priced in (re-rating spent); price
~45% above the entry zone after a 30% three-day block-trade move; pivot
facts (CARO trend, audited MedTech split) 12 months away or never disclosed.

NOTE (repo): operator OVERRODE this SHALLOW WATCH to PROCEED on 2026-08-29
and authorised the full pipeline on the signed model. See companies/ENTERO.md.

---
## PART 6 (SECTION 6) — GATE PRE-RULINGS (for the P/E BASE CARD)
- Sector cap row: NO clean Section 1B row for pharma/MedTech distribution.
  Dossier recommendation 18-20x. Market median EV/EBITDA since listing 24.2x.
  July operator ruling (non-binding this run): Cybersecurity/VAD 25x.
- Pillar 1 ROCE: CONTESTED. Company-reported 21.1% (Q1 FY27) vs
  balance-sheet-derived ~10.5% vs third-party trace ~10% FY26 / 10.7% FY25.
  Weight of evidence favours the lower figure. Pillar 1 cannot run until the
  denominator is settled; treat as [ESTIMATE] until then.
- Pillar 2 cash multiplier: INDETERMINATE (FCF uncomputable, no consolidated
  capex line). Caps disposition at PROCEED WITH CAVEATS.
- Pillar 3 growth/emerging-moat premium: MODEST (EM 19, understated pending a
  B07 recheck for master data management + 15% exclusive tie-ups).
- Earnings basis: operator to decide at the gate (forward vs trailing).
- Recognition gap: CLOSED per dossier B4 (re-rating largely spent).

---
## PART 7 — PASTE-READY BLOCK FOR companies/ENTERO.md
(Recorded in companies/ENTERO.md on 2026-08-29; see that file for the signed
version, including the operator override to PROCEED.)

---
## PART 9 — STORY AFTER READING EVERYTHING
Entero spent seven years doing something unglamorous and did it well. It
bought fifty regional pharmacy distributors, mapped every one of their
product codes onto a single in-house system, and turned a collection of
family businesses into a network that can tell you where any of 83,400
products is sitting across 136 warehouses. That mapping work is the real
asset. It does not show up on the balance sheet, and it is why the company
can move stock from a warehouse with surplus to one with a shortage while
its competitors cannot.
The financial transformation is finished and it was real. EBITDA margin
went from 1% to 5%. Gross margin went from 8% to 11.4%. Operating cash flow
turned positive after six negative years. A business that burned cash now
funds itself up to about 15% growth.
The problem is that everyone watched it happen. The stock has traded at a
median of 24 times EBITDA since listing. When Prashant Jain's fund bought
2.5% in August, the market marked the shares up 30% in three days. The
seller was a holder who had been reducing for a year. That is not a market
that has missed something.
What remains is a second, smaller climb. Medical devices from 15% of
revenue to 20%, worth perhaps a third of a percentage point of margin. A
market where rupees grow 13% while boxes grow not at all, which quietly
hands a distributor operating leverage it did not have while it was buying
companies. Those are real, and over five years they compound into
something.
But three regulatory processes are pointed at the margin line, forty of
sixty-five subsidiaries carry auditor warnings that nobody can trend until
next July, and free cash flow still cannot be computed because no
consolidated capex line exists.
At Rs 1,240 this is a good business at a fair price. At Rs 1,806 it is a
good business at someone else's price. The proof arrives in November. The
better price usually follows a disappointment, and this company has
disappointed before.

---
## PUBLICATION CHECK
PUBLISH CANDIDATE. Post type: framework illustration plus counter-intuitive
observation. Hook: IPM grew 8.6% in value and 0.6% in units last year; for a
distributor, revenue scales with value and cost with volume, so that gap is
the whole operating-leverage story and it is invisible in the headline
growth rate. Position status: WATCHLIST, not held. No conflict. Do not name
the entry price or internal framework mechanics.
