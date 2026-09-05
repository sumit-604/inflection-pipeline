# B00 — Input Validation (AEQUS 2026-09-05)

Orchestrator-run stage 0. Manifest parses (company Aequs Ltd, ticker AEQUS,
CMP Rs 242.0, market cap Rs 16,242 cr, run_type full, concalls_available
true, sector_cap_row "Defence / strategic"). inputs/ tree non-empty. No
mechanical halt.

## SPEAR GATE
PASS by recorded OVERRIDE. companies/AEQUS.md did not exist at run start.
The run folder is a /step1 intake product (step1-business-brief.md present;
manifest notes cite it). Step G of .claude/commands/step1.md (operator standing
ruling 2026-09-05: Step-1 intake replaces the web spear) was not executed by
the intake, so the orchestrator completed it: companies/AEQUS.md created from
companies/_template.md carrying
`Spear: OVERRIDE 2026-09-05 (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)`
plus the four load-bearing facts from the brief. Committed separately, before
any stage ran.

Load-bearing facts (first verification priority, carried to every stage):
1. GUIDANCE VS DELIVERY: FY27 aerospace revenue +25-30%, segment EBITDA
   margin above 20%, ~20% manufacturing ROCE. Verify against AR FY26, Q1 FY27
   presentation, concalls.
2. CONSUMER DRAG AND CAPITAL ALLOCATION: consumer segment EBITDA ~-24% in
   H1 FY26; ~Rs 500 cr of ~Rs 660 cr FY27 capex earmarked for it. Verify the
   segment EBITDA and capex split.
3. CASH CONVERSION AND BALANCE SHEET: net loss FY25 Rs 102 cr, FY26 wider,
   Q1 FY27 Rs 53 cr. Verify debt, interest, OCF vs capex, receivables and
   inventory trend. FLAG-CASH input.
4. ORDER BOOK AND VISIBILITY: USD 1,004 mn aerospace order book; 15-year
   Safran A320 wheel agreement, deliveries FY28. Verify from concall and
   presentation; check backlog-to-revenue cadence.

## FOLDER INVENTORY
- prospectus/      ABSENT. HIGH gap. Listed 10-Dec-2025 (AR FY26 states
                   "December 10, 2025"; brief agrees), 9 months before
                   run_date, inside the ~3y window. The RHP carries the
                   promoter/group history, the group-company map and the
                   restated pre-IPO financials. Stages 2/3 build from the AR
                   alone; stage 8 sources promoter/group from web + AR
                   governance and flags the map as web-derived.
- annual-report/   1 PDF. Annual_Report_2026.pdf = FY2025-26 (361 pages,
                   text layer good, 2 blank pages).
- results/         ABSENT. No results filings. Gate 0 runs from the screener
                   Data_Sheet plus AR financial statements. Q1 FY27 figures
                   reach the pipeline only via the Q1 FY27 investor
                   presentation and the Aug-2026 concall (filed documents,
                   anchored, but not the results filing itself).
- rating/          ABSENT. No rating rationale. Pillar 2 / FLAG-CASH runs
                   without rating evidence (Tipco/Rappid INDETERMINATE guard
                   applies if cash conversion deteriorates).
- concalls/        3 PDFs. Chronology oldest->newest for stage 5:
                     1. Concall_Feb_2026_Transcript.pdf  - Q3 FY26 call
                        (filed 04-Feb-2026), 28 pages
                     2. Concall_Jun_2026_Transcript.pdf  - Q4 FY26 / FY26
                        annual call (held 26-May-2026, filed 02-Jun-2026),
                        20 pages
                     3. Concall_Aug_2026_Transcript.pdf  - Q1 FY27 call
                        (held 29-Jul-2026), 20 pages
- peer-concalls/   9 PDFs across 3 peers: AZAD 4 (Nov-2025 Q2 FY26,
                   Feb-2026 Q3 FY26, May-2026 Q4 FY26, Aug-2026 Q1 FY27);
                   UNIMECH 4 (Feb-2026 Q3 FY26, May-2026 Q4 FY26, Jun-2026
                   post-Q4 call held 29-May-2026, Aug-2026 Q1 FY27);
                   DYNAMATECH 1 (Feb-2024 investor meeting transcript, 9
                   pages, ~30 months stale; the only Dynamatic document,
                   coverage for the closest commercial-aero comp is thin).
- announcements/   ABSENT. No Reg 30 record. The Safran engine-parts and
                   A320 wheel agreements (Jun-2026) and order-win claims are
                   verifiable only from concall/presentation statements.
                   Intent-and-action cross-check runs on concall/AR/
                   presentation only; recent documented ACTIONS cannot be
                   graded.
- shareholding/    ABSENT. FII+DII UA qualifier unresolved for stage 11;
                   promoter holding/pledge falls back to the AR (as at
                   31-Mar-2026) with staleness noted.
- research/        ABSENT. .gitkeep planted so the claude.ai
                   web-handover-dossier.md has a landing folder.
- screening/       24 CSVs (AEQUS + AZAD, DYNAMATECH, UNIMECH). Collector v3
                   defect present (LESSONS recurring pattern): Profit_Loss,
                   Balance_Sheet, Cash_Flow, Quarters and Customization CSVs
                   are header-only for all four names. Data_Sheet CSVs ARE
                   populated: annual P&L, BS, CF FY23-FY26 and 7 quarters
                   Dec-2024 to Jun-2026. Gate 0 uses Data_Sheet + AR.
- presentation/    1 PDF. Investor_Presentation_1.pdf = Q1 FY27 investor
                   presentation, 30 pages (3 image-only pages).
- other/           ABSENT. No effect.
- _textcache/      Orchestrator pre-extraction of every input PDF to
                   page-marked .txt (pypdf), one file per PDF under the same
                   subfolder name. Stages and verifiers may read either the
                   PDF or the .txt; anchors cite the PDF page number that the
                   "=== PAGE n of N ===" marker names.

Manifest defects: no listed_date field (listing date taken from AR + brief);
sector_cap_row "Defence / strategic" was set by the Step 1 brief over the
collector's auto-pick "Pharma / CDMO"; the business is commercial aerospace
(Airbus, Boeing, Safran) not defence, so phase 3 must confirm the row.

## EMPTY-FOLDER CONFIRMATION
Seven folders empty or absent: prospectus (HIGH), results, rating,
announcements, shareholding, research, other. The pause is SUPPRESSED: this
run folder is a /step1 intake product and the step1 AUTONOMY CONTRACT
(operator ruling 2026-09-05) sets the standing answer "proceed with the
gaps". Recorded here; not asked again this run. Upload list for Halt 1, in
priority order: RHP/DRHP (Dec-2025 IPO), Q1 FY27 and FY26 results filings,
Reg 30 announcements (Safran agreements, Jun-2026), latest shareholding
pattern (Jun-2026 quarter), any credit rating rationale.

## FRESHNESS PAIR CHECK
1. RESULTS -> CONCALL: inputs/results/ empty, so no trigger document. No
   pair failure (the absence is an input gap, recorded above, not a missing
   mate). PASS (no trigger).
2. RATING BULLETIN -> RATIONALE: inputs/rating/ empty, no trigger. PASS
   (no trigger).
3. SEBI ORDER -> TEXT: no SEBI order referenced in the AR (0 hits for
   "SEBI order", "order of SEBI", "adjudication"). Stages confirm on read.
   PASS (N/A).
4. AR -> LATEST AUDITED ANNUAL: AR FY26 present; the latest audited annual
   year in corpus is FY26 (Q4 FY26 call of 26-May-2026 discusses the audited
   FY26 numbers). PASS.
Verdict: FRESHNESS PAIRS OK. No freshness cap on the gate.

## COMPANY MEMORY
companies/AEQUS.md (created this run, spear override + load-bearing facts)
and runs/aequs-2026-09-05/step1-business-brief.md are carried to every stage
as COMPANY MEMORY: weighed, never anchored. Every figure a stage reports
comes from this run's inputs.

## ENVIRONMENT NOTE
Market cap ~Rs 16,242 cr sits above the strategy's small/micro-cap remit.
Not a halt; the operator's call at Halt 1.

```yaml
stage: B00-inputs
company: AEQUS
run_date: 2026-09-05
model: orchestrator
status: complete
input_gaps:
  - prospectus (ABSENT; HIGH gap; listed 10-Dec-2025, inside ~3y window; RHP carries promoter/group history and restated pre-IPO financials)
  - results (ABSENT; no results filings; Gate 0 from screener Data_Sheet + AR; Q1 FY27 via presentation + concall only)
  - rating (ABSENT; no rating rationale; Pillar 2 / FLAG-CASH without rating evidence)
  - announcements (ABSENT; no Reg 30 record; Safran agreements Jun-2026 verifiable only from concall/presentation)
  - shareholding (ABSENT; FII+DII UA qualifier unresolved; promoter holding/pledge from AR at 31-Mar-2026)
  - research (ABSENT; .gitkeep planted)
  - other (ABSENT; no effect)
  - screening (collector v3 defect: Profit_Loss/Balance_Sheet/Cash_Flow/Quarters/Customization CSVs header-only for AEQUS and all 3 peers; Data_Sheet populated FY23-FY26 + 7 quarters to Jun-2026)
  - peer-concalls (DYNAMATECH single transcript Feb-2024, ~30 months stale; AZAD 4 and UNIMECH 4 current)
  - manifest (no listed_date; sector_cap_row set by Step 1 brief to "Defence / strategic" over collector auto-pick "Pharma / CDMO"; commercial-aerospace business, phase 3 confirms row)
freshness_pairs:
  - pair: results_to_concall
    trigger_doc: none (inputs/results/ empty)
    mate_expected: n/a
    status: PASS
    missing_doc: none (results absence is an input gap, not a missing mate)
  - pair: rating_bulletin_to_rationale
    trigger_doc: none (inputs/rating/ empty)
    mate_expected: n/a
    status: PASS
    missing_doc: none
  - pair: sebi_order_to_text
    trigger_doc: none referenced in AR FY26
    mate_expected: n/a
    status: PASS
    missing_doc: none
  - pair: ar_to_latest_audited_annual
    trigger_doc: annual-report/Annual_Report_2026.pdf (FY2025-26)
    mate_expected: latest audited annual year = FY26
    status: PASS
    missing_doc: none
freshness_verdict: FRESHNESS PAIRS OK
spear_gate: OVERRIDE 2026-09-05 (step1 standing ruling; companies/AEQUS.md created by orchestrator this run)
spear_load_bearing_facts:
  - fy27_guidance_aero_growth_25_30pct_segment_ebitda_above_20pct_roce_20pct
  - consumer_segment_ebitda_negative_vs_rs500cr_of_rs660cr_fy27_capex
  - net_loss_fy25_fy26_q1fy27_debt_interest_ocf_vs_capex_wc_trend
  - order_book_usd1004mn_safran_a320_wheel_15yr_deliveries_fy28_conversion_cadence
concall_map:
  - Concall_Feb_2026_Transcript.pdf: Q3 FY26 (filed 04-Feb-2026)
  - Concall_Jun_2026_Transcript.pdf: Q4 FY26 / FY26 annual (held 26-May-2026)
  - Concall_Aug_2026_Transcript.pdf: Q1 FY27 (held 29-Jul-2026)
empty_folder_pause: SUPPRESSED (step1 AUTONOMY CONTRACT standing answer "proceed with the gaps"; run folder is a step1 intake product)
market_cap_note: Rs 16,242 cr above small/micro-cap remit; operator call at Halt 1
flags: []
analyst_note: >
  No results filings, no prospectus, no announcements, no shareholding, no
  rating. The corpus is AR FY26 + three concalls + Q1 FY27 presentation +
  screener Data_Sheet + 9 peer transcripts. Every Q1 FY27 number is anchored
  to the presentation or the Aug-2026 transcript, never to a results filing.
  The prospectus gap is HIGH: a Dec-2025 listing with a two-segment group
  (aerospace + loss-making consumer) needs the RHP group map and restated
  financials that the AR alone does not carry.
```
