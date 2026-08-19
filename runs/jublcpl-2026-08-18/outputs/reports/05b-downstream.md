# Stage 5b: Downstream Signal Identification (Role 5.5) — JUBLCPL

Run folder: runs/jublcpl-2026-08-18
Company: Jubilant Agri and Consumer Products Ltd (JUBLCPL), CMP 2342, sector row "Specialty chemicals"
Mode: **DEGRADED** — B03 (AR Deep Dive), B04 (Business Model Decoder), B05 (Concall Analysis) and B06 (Peer Comparison)
blocks were NOT run for this folder; `runs/jublcpl-2026-08-18/outputs/` is empty (confirmed by directory
listing before starting). This is a genuine input_gap, not a rendering failure. This stage instead mines the
raw documents in `runs/jublcpl-2026-08-18/inputs/_extracted/` directly, per the instruction file's degraded-mode
fallback (Rule 8/9 of the operating rules).

Documents actually read (all via pre-extracted `.txt`, not PDF render):
- `593644c3-68a7-47e1-8955-1cabf256f448.txt` — FY26 Annual Report (249 pages; Board's Report, Segment note,
  Secretarial Audit, MD&A reference). NOTE: pages 2–42 of the source PDF (the graphics-heavy "Corporate
  Overview"/industry-narrative front matter) did not extract to text — likely image-only pages — so the
  standalone MD&A industry narrative was not recoverable from this file; segment facts were instead sourced
  from the Board's Report, Note 39 (segment reporting) and the investor presentation.
- `Investor_Presentation_1.txt` — Q1 FY27 earnings presentation (Aug 11, 2026), used for segment split,
  geography, capacity, brownfield SBR Latex expansion, demerger status.
- `202510141011_Jubilant_Agri_and_Consumer_Products_Limited.txt` — CARE Ratings press release (Oct 17, 2025),
  used only for discovery (raw-material and monsoon/subsidy risk language), not as a signal source (it is a
  rating opinion on the target company itself, not an external counterparty).
- `jubilant-agri-consumer-products-initiating-coverage-mncl-equity-research-report.txt` and the MNCL 4QFY26
  company update — READ FOR DISCOVERY ONLY (named customers, end markets). Per Step 3, broker research citing
  management is a REJECTED source type and is not used as a primary source for any signal below.
- `51b0b805-...txt`, `b0072041-...txt` — results/exchange filings, read for corroboration (demerger/NCLT
  timeline only; no new dependency found).
- Peer concalls (NOCIL, APCOTEXIND, BALAMINES, KRISHANA) were present but not needed once primary counterparty
  sources were found directly; not read in full (see Search Log).

## STEP 1 — Signal Discovery

JUBLCPL's FY26 revenue splits Performance Polymers & Chemicals (~73%, comprising Food Polymers/SPVA, VP Latex,
SBR Latex, Adhesives, Wood Finishes) and Agri Products (~27%, SSP fertilizer + Agri Nutrients, being demerged
into Jubilant Agri Solutions Ltd). Reading the AR segment note, the investor presentation, and the MNCL reports
(for discovery only) surfaces the following external, material dependencies:

1. **Global chewing gum manufacturers** (Food Polymers/SPVA end market) — MNCL names Perfetti, Mondelez and
   Wrigley as customers of JACPL's solid PVAc (SPVA), the input used as chewing-gum base. JACPL is the sole
   Indian and No.2 global producer.
2. **Global tyre / tyre-cord manufacturers** (VP Latex end market) — MNCL names SRF, Madura, Kordsa, Indorama,
   Continental and Michelin as customers of VP Latex ("Encord" brand), used to bond tyre-cord fabric to rubber.
   JACPL states it is No.1 in India and globally (ex-China) in VP Latex.
3. **Nutrient Based Subsidy (NBS) policy for P&K fertilizers** — the AR's segment note explicitly reports SSP
   under the "Phosphatic and Potassic (P&K) Fertilizers" segment per a Jan 2024 Dept. of Fertilizers office
   memorandum; the Note on trade receivables shows a large subsidy receivable (₹1,615.15 mn, up from ₹840.57
   mn); the CARE rating flags "policy-driven demand in the agri business" as a rating constraint.
4. **Monsoon/rainfall** — the Q1 FY27 investor presentation's own Agri Products "Outlook" states demand "may
   remain subdued in the near term due to weak and uneven monsoon" — a directly falsifiable external claim
   whose primary data (IMD) can be checked independently of management's framing.
5. **Construction-sector activity** (new SBR Latex / construction-chemicals line) — the presentation's
   brownfield capex slide states the ₹50 cr, 30,000 MTPA SBR Latex expansion (Phase-2, commissioning end
   Q3-FY27) targets "construction chemicals — a high-growth end market beyond the existing adhesives base",
   with active trials with "leading paint and cement manufacturers" per MNCL (discovery only). Broad
   construction/infrastructure activity is a plausible external leading indicator for this new revenue line.
6. **Export markets / geopolitical-logistics disruption** — both the Q1 FY27 presentation ("Export volumes
   impacted by geopolitical disruptions and logistics challenges in key international markets") and the CARE
   note flag export/FX/logistics risk; 15% of FY26 revenue is export (Brazil, USA, Mexico, Colombia, Middle
   East, Russia, China, EU, etc. per the presentation's geography slide).

Count of distinct external dependencies identified: **6** (comfortably above the 3-dependency floor).
`thesis_externally_verifiable` is therefore **true**, subject to Step 3 source verification below (dependency
6, export/logistics, could not be reduced to one verifiable primary-source cadence signal in the time available
— see Search Log — so it is recorded as a dependency but does not itself produce a verified Step-3/4 signal row).

## STEP 2 — Signal-to-Thesis Mapping

| Dependency | Bull thesis element it tests | Bear thesis element it would confirm | Falsifying observation |
|---|---|---|---|
| Global chewing-gum majors (Mondelez, Perfetti, Wrigley) buying SPVA | Sticky, multi-decade-qualified demand for JACPL's Food Polymers segment supports steady margin annuity | Global gum category is structurally slow (~3% CAGR) and demand could stall, capping SPVA volume growth | Two consecutive quarters of negative organic revenue growth in a named customer's gum/candy category |
| Global tyre majors (Continental, Michelin) and tyre-cord fabric makers (SRF) buying VP Latex | Tyre-industry replacement-cycle growth (OEM approvals create switching costs) underwrites JACPL's Latex volumes and its bid for share in SBR/construction latex | A cyclical downturn in global tyre production/replacement demand would directly compress VP Latex offtake, the largest profit pool cited by MNCL | Two consecutive quarters of declining Tires-segment sales (Continental) or declining Technical Textiles segment revenue (SRF), or a swing to negative replacement-tire volume growth (Michelin) |
| Nutrient Based Subsidy (NBS) policy for P&K fertilizers (SSP) | Government subsidy keeps SSP economics viable and supports Agri Nutrients "higher double-digit growth" outlook management has guided to | A subsidy cut or delayed disbursement (subsidy receivable already grew ~92% YoY in FY26) would compress realizations/working capital right as the Agri unit is being demerged | A season-on-season cut to the notified NBS rate for P/S nutrients, or a further build in subsidy receivable days |
| Monsoon / IMD rainfall | Agri demand recovers once monsoon normalises, supporting the segment ahead of the demerger record date | A second consecutive weak/uneven monsoon season would confirm management's own "subdued near term" language and push Agri Nutrients growth below guidance | Cumulative all-India rainfall closing the Aug–Sep 2026 half of the season below 90% of LPA (i.e., no meaningful narrowing of the deficit IMD reported as of mid-Aug 2026) |
| Construction/infrastructure activity (cement, core-industries index) | New SBR Latex/construction-chemicals line (30,000 MTPA, Phase-2 commissioning Q3-FY27) has a genuine external demand pull, de-risking the ₹50 cr brownfield capex | Weak construction activity would mean the new capacity ramps into soft demand, since the segment has zero JACPL revenue history to date | Two consecutive months of India Index of Core Industries cement-production growth decelerating below 3% YoY, alongside no disclosed SBR Latex customer wins by Q3-FY27 commissioning |
| Export markets / geopolitical-logistics disruption | Export diversification (15% of revenue, 20+ countries) provides a growth lever independent of the Indian cycle | Company's own Q1 FY27 outlook already flags continued near-term export volatility from geopolitics/logistics | Not reduced to a single trackable primary-source series in the time available (see Search Log); recorded as a dependency, not carried to a Step 3/4 signal row |

No B05 trigger cross-reference is possible: B05 (Concall Analysis) was not run for this folder (input_gap), so
there is no `triggers[]` array to check signals against. `b05_triggers_without_signal` is therefore left empty
with a note, not populated with a false "none downgraded" reading.

## STEP 3 — Signal Source Verification

Source discipline: MNCL broker research is used only in Step 1 for discovery (named customers). No signal
below cites MNCL as its `primary_source_url`; each is traced to the counterparty's or the regulator's own
primary release. The target company's own AR/presentation is never used as a downstream signal source below;
it appears only in Step 1/2 as the origin of the dependency claim being tested.

| Signal name | Primary source URL | Cadence | Current value + date | Verification result |
|---|---|---|---|---|
| Continental AG Tires segment sales | https://www.continental.com/en/press/press-releases/results-first-half-2026/ | Quarterly | Tires segment sales €3.3bn in Q2 2026 (organic +0.3% YoY), adj. EBIT margin 15.3% vs 12.1% Q2 2025; released 27 Jul 2026 | VERIFIED (counterparty's own IR release) |
| Michelin Group replacement tire volumes/sales | https://www.michelin.com/en/investors/presentation-events/results-sales | Quarterly (semi-annual detail) | H1 2026 revenue €12.7bn (+0.5% constant FX); PC/LT replacement demand +1%, group volumes +0.8%; released 27 Jul 2026 | VERIFIED (counterparty's own IR release) |
| SRF Limited Technical Textiles segment revenue (tyre-cord fabric + belting) | https://www.srf.com/news/srf-limited-delivers-robust-q1fy27-results-driven-by-strong-performance-across-businesses | Quarterly | Segment revenue ₹597 cr Q1 FY27 vs ₹467 cr Q1 FY26 (+28% YoY), operating profit +186% YoY; released 22 Jul 2026 | VERIFIED (counterparty's own press release) |
| Mondelez International Gum & Candy category organic revenue growth | https://ir.mondelezinternational.com/news-releases/news-release-details/mondelez-international-reports-q2-2026-results | Quarterly | Gum & Candy organic growth +7.6% Q2 2026 (qtr ended 30 Jun 2026), YTD +5.3%; released 28 Jul 2026 | VERIFIED (counterparty's own IR portal release) |
| Dept. of Fertilizers Nutrient Based Subsidy (NBS) rate, P&K/SSP | https://www.pmindia.gov.in/en/news_updates/cabinet-approves-nutrient-based-subsidy-nbs-rates-for-kharif-season-2026-from-01-04-2026-to-30-09-2026-on-phosphatic-and-potassic-pk-fertilizers/ (also PIB: pib.gov.in/PressReleasePage.aspx?PRID=2211384) | Event-driven (biannual, Kharif/Rabi Cabinet notification) | Kharif 2026 NBS rates raised ~12% YoY (P nutrient ₹52.76/kg, S ₹3.16/kg) to offset international fertilizer prices; Rabi 2025-26 SSP subsidy was ₹7,408/MT; latest notification dated ~Mar/Apr 2026 (Kharif 2026 season) | VERIFIED (Government of India, PMO/PIB primary release) |
| IMD Southwest Monsoon cumulative rainfall (% of LPA) | https://mausam.imd.gov.in/responsive/rainfall_statistics.php and https://mausam.imd.gov.in/responsive/monsooninformation.php | Monthly (in-season) | All-India cumulative rainfall 1 Jun–12 Aug 2026 at −12% of LPA (below normal); IMD forecasts below-normal rainfall for Aug–Sep 2026 half | VERIFIED (Government of India, IMD primary data) — directly corroborates JACPL's own Q1 FY27 "weak and uneven monsoon" language with an independent source |
| DPIIT Index of Core Industries — cement production | https://eaindustry.nic.in/eight_core_infra/eight_infra.pdf | Monthly | Cement production +9.8% YoY, June 2026; combined core-industries index +5.0% YoY June 2026 (cumulative Apr-Jun 2026 +3.6%); published ~end-Jul 2026 | VERIFIED (Government of India, DPIIT/Office of the Economic Adviser primary data) |
| ATMA (Automotive Tyre Manufacturers' Association) India tyre production/export data | atmaindia.org.in (site itself) | Would be Monthly/quarterly bulletins | NOT FOUND (primary) — atmaindia.org.in was blocked by the network egress proxy on direct fetch; web search returned only stale/undated aggregate figures ("200mn+ tyres/yr", "~25% exported") with no date-stamped current value | ATTEMPTED, NOT VERIFIED — dropped from the signal set; does not count toward the floor |
| DGCI&S / Ministry of Commerce export data for JACPL's relevant HS codes (PVAc resins, VP Latex, SSP) | Not located within time budget | Monthly | NOT FOUND (primary) | SKIPPED — see Search Log |

Seven dependencies were traced to primary sources; **six are fully verified with a dated current value** and
carried forward as signals in Step 4. ATMA and DGCI&S export data are recorded as attempted/not-found and do
not count toward the floor (per Step 3 rule: a signal whose only available source is unreachable/rejected is
recorded but does not count).

## STEP 4 — Workup Signal Set (tracker handoff)

| Signal name | Case A/B (likely) | Signal type | Cadence | Bull thesis element | Falsifying observation |
|---|---|---|---|---|---|
| Continental AG Tires segment sales | B (new — JACPL not previously covered in tracker to our knowledge) | Counterparty Filing | Quarterly | Tyre-industry demand underwrites VP Latex offtake | 2 consecutive quarters of declining Tires-segment sales |
| Michelin Group replacement tire volumes | B | Counterparty Filing | Quarterly | Replacement-cycle growth supports Latex volumes | 2 consecutive halves of negative replacement volume growth |
| SRF Limited Technical Textiles segment revenue | B | Counterparty Filing | Quarterly | Indian tyre-cord fabric demand (proxy for VP Latex pull-through) | 2 consecutive quarters of YoY segment revenue decline |
| Mondelez Gum & Candy organic revenue growth | B | Counterparty Filing | Quarterly | Chewing-gum category growth supports SPVA volume | 2 consecutive quarters of negative organic growth |
| Dept. of Fertilizers NBS rate (P&K/SSP) | B | Sector-Macro Proxy | Event-driven (biannual) | Subsidy support keeps SSP economics viable pre-demerger | A season-on-season NBS rate cut for P/S nutrients |
| IMD monsoon cumulative rainfall (% LPA) | B | Sector-Macro Proxy | Monthly (in-season) | Monsoon normalisation would lift Agri Nutrients growth | Season closes below 90% of LPA with no narrowing of deficit |
| DPIIT Index of Core Industries — cement production | B | Sector-Macro Proxy | Monthly | Construction activity de-risks the new SBR Latex ramp | 2 consecutive months of cement growth below 3% YoY |

All seven rows are likely Case B (new tracker entries) since JACPL/JUBLCPL is a newly-listed micro-cap (demerged
from Jubilant Industries in 2024) unlikely to already have rows in the consolidated Downstream Signal Tracker;
this is a judgement call for the operator to confirm at /finalize, not verified against the actual Notion
tracker from this stage.

## STEP 5 — Workup Output (forward handoff)

- **FTTCP (valuation stage):**
  - Revenue transition — anchored by 5 of 7 signals: Continental, Michelin, SRF (VP Latex/Performance Polymers
    growth), Mondelez (Food Polymers/SPVA growth), DPIIT cement index (new SBR Latex/construction-chemicals
    line). All are Quarterly/Monthly cadence, feeding both the 3-6 month window and, cumulatively, the 12-month
    window.
  - Margin transition — anchored by 1 signal: Dept. of Fertilizers NBS rate (Agri segment realization/subsidy
    receivable risk), Event-driven/biannual cadence, feeds the 12-month window.
  - Cash transition — **NO anchoring signal identified.** Any forward catalyst framed around working-capital or
    cash-conversion improvement is capped at MODERATE magnitude by the FTTCP Signal Gate.
  - ROCE transition — **NO anchoring signal identified.** Any forward catalyst framed around ROCE improvement
    (e.g., post-demerger capital efficiency) is capped at MODERATE magnitude by the FTTCP Signal Gate.
  - IMD monsoon is a Sector-Macro Proxy that also feeds Revenue (near-term Agri Nutrients growth), Monthly
    cadence, 3-6 month window.
- **Role 1 Pillar 3:** the six verified signals support a "mostly 📄 documented evidence" growth-visibility
  claim for the Performance Polymers & Chemicals segment specifically (Latex + Food Polymers, ~73% of revenue).
  The Agri segment's growth visibility is weaker: only two signals (NBS, monsoon) exist and one (monsoon) is
  currently reading bearish, so the Agri growth claim should NOT be graded "mostly documented" without that
  caveat, and the segment is mid-demerger in any case.
- **Role 2 Section 3B:** cannot be executed — B05 (Concall Analysis) triggers[] were never produced for this
  run (degraded mode), so there are no growth triggers to check against these signals. This is recorded as an
  input_gap, not a "zero triggers downgraded" finding.
- **Role 3 Section 8:** the seven falsifying observations above (Step 2/4 tables) are the early-warning
  thresholds; the monsoon one is already reading toward the bear side as of the run date (12 Aug 2026 cumulative
  rainfall −12% of LPA), which should be flagged prominently to the operator as a live tripwire, not a
  hypothetical one.

## Search Log

Searches performed (7 successful web searches + 2 attempted WebFetch calls that were blocked by egress proxy):
1. Department of Fertilizers NBS rates 2026 SSP — successful, multiple PIB/PMO primary hits.
2. Continental AG Q2 2026 tire segment investor relations — successful, Continental IR primary release found.
3. SRF Limited Q1 FY27 Technical Textiles segment — successful, SRF's own press release found.
4. Mondelez International 10-Q 2026 SEC filing — successful (led to Mondelez IR portal as better/accepted
   source than the SEC htm, which was separately blocked on direct fetch — see below).
5. ATMA India tyre production data 2026 — successful search, but returned only undated aggregate figures; the
   ATMA site itself could not be fetched (egress blocked) to pull a dated current value, so the signal is
   recorded as NOT FOUND (primary) and dropped, per instructions this makes status partial.
6. Michelin Group H1 2026 sales/replacement tire volumes — successful, Michelin's own results release found.
7. IMD monsoon 2026 cumulative rainfall — successful, mausam.imd.gov.in primary hit.
8. Mondelez Q2 2026 "Gum & Candy" category-specific figure — successful, sourced to Mondelez's own IR portal.
9. India DPIIT Index of Core Industries / cement production June 2026 — successful, eaindustry.nic.in primary
   source identified.

Attempted but blocked (network egress proxy, domain-level block, not a search failure):
- WebFetch atmaindia.org.in/overview — EGRESS_BLOCKED.
- WebFetch sec.gov (Mondelez 10-Q htm) — EGRESS_BLOCKED; worked around via Mondelez's own IR portal release,
  which is in any case the preferred accepted source type over a third-party SEC mirror.

Searches skipped (not attempted, time/scope budget):
- DGCI&S / Ministry of Commerce Export-Import Data Bank for HS codes specific to PVAc resin, VP Latex and SSP
  (would have produced an "Exports data" type signal for dependency 6, export markets/geopolitical-logistics
  risk). Not located within the run's time budget.
- Kordsa (Turkey, BIST-listed) and Indorama Ventures (Thailand, SET-listed) quarterly filings — both are named
  JACPL customers per MNCL but were not pursued once four other tyre/gum-chain signals (Continental, Michelin,
  SRF, Mondelez) were already verified; would have added redundant Revenue-transition coverage rather than new
  transition coverage.
- SRF-specific commentary tying its Technical Textiles growth explicitly to VP Latex volumes (not disclosed by
  SRF; the link is inferential — SRF is a tyre-cord fabric maker and a named JACPL customer per MNCL, not proof
  that SRF's growth is specifically JACPL-sourced volume).

These skips are why `status: partial` even though thesis_externally_verifiable is true — the ATMA and DGCI&S
gaps are named explicitly, not silently dropped.

## Degraded-Mode Input Gaps

- B03 (AR Deep Dive): NOT RUN — outputs/blocks and outputs/reports both empty for this run folder (confirmed
  by directory listing). Compensated for by direct AR reading in this stage, but AR-Deep-Dive-specific analysis
  (e.g., 5-year trend tables, related-party detail) is not available to cross-check against.
- B04 (Business Model Decoder): NOT RUN. Compensated for by segment-note and investor-presentation reading.
- B05 (Concall Analysis): NOT RUN. No triggers[] exists; Step 2/Step 5 cross-referencing to B05 triggers could
  not be performed (see Step 5, Role 2 Section 3B note).
- B06 (Peer Comparison): NOT RUN. Peer concall transcripts (NOCIL, APCOTEXIND, BALAMINES, KRISHANA) exist in
  inputs/_extracted/ and were available but not required once direct counterparty/regulatory sources were
  found; not read in full for this stage (peer positioning is B06's job, not B05b's).
- Annual report pages 2-42 (source PDF) did not extract to text (likely image-only "Corporate Overview" pages)
  — flagged UNREADABLE for that specific page range, not the whole document, which was otherwise fully usable.

## Signal Gate Effect

Two of the four FTTCP transitions (Cash, ROCE) have zero anchoring signal from this stage's discovery. This is
NOT a "zero signals, DEEP WATCH" case — six signals were verified, well above the floor, and Revenue/Margin
transitions are anchored — but any forward catalyst framed specifically around Cash conversion or ROCE
improvement (both plausible narratives given the pending Agri demerger, which the company frames as sharpening
focus on the higher-margin/higher-ROCE polymers business) is capped at MODERATE magnitude by the Signal Gate
until a Cash- or ROCE-specific external signal is found (e.g., a named customer's own capex disclosure that
would pull through JACPL working capital, or an independent index of tyre-industry receivable/payable cycles).
