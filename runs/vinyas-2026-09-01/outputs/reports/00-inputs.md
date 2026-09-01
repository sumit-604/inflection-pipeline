# B00 — Input Validation (VINYAS 2026-09-01)

Orchestrator-run stage 0. Manifest parses. inputs/ tree non-empty. No
mechanical halt.

## SPEAR GATE
PASS. companies/VINYAS.md carries `Spear: OVERRIDE 2026-09-01 (operator)`.
Load-bearing facts (first verification priority, carried to every stage):
1. Customer concentration (NOT DISCLOSED FY23-FY26).
2. Cost of materials as % of revenue (design-and-test vs build-to-print).
3. Repeat vs new revenue (share of FY26 from programs held in FY24).
4. Root cause of 161-day receivables.
Plus the margin puzzle: OPM 9% to 12.5% during ~30% compound growth.

## FOLDER INVENTORY
- prospectus/      ABSENT. Not a HIGH gap: long-listed (CIN 2001;
                   AR-2015 present), well beyond ~3y window.
- annual-report/   3 PDFs. Primary = FY26 (SME_AR_..2025_2026..). Backward
                   baseline also from FY25 (..2024_2025..) and FY2015.
- results/         2 PDFs. FY26 audited (28-May-2026) + H1 FY26 (06-Nov-2025).
- rating/          2 PDFs (rating 1, rating 2). CRISIL. SCANNED IMAGE PDFs
                   (~8 pages each, no extractable text layer): subagents must
                   read via rendering, not grep.
- concalls/        4 files, 3 distinct calls. Nov_2025 and Nov_2025_2 are the
                   SAME H1 FY26 call (10-Nov-2025); _2 is a duplicate, dropped.
                   Chronology oldest->newest for stage 5:
                     1. Concall_Jun_2025_Transcript.pdf  — FY25 annual (07-Jun-2025)
                     2. Concall_Nov_2025_Transcript.pdf  — H1 FY26 (10-Nov-2025)
                     3. Concall_Jun_2026_Transcript.pdf  — FY26 annual (03-Jun-2026)
- peer-concalls/   28 PDFs across CENTUM, CYIENTDLM, AVALON, KAYNES, SYRMA,
                   ASTRAMICRO, DATAPATTNS. Stage 6 uses up to 12, keyed to
                   B05.peer_questions and the approved peer set.
- announcements/   ABSENT (folder). Partial substitute: operator-ferried
                   6-month event timeline at inputs/downstream/, tier
                   [OPERATOR-FERRIED], weighed not anchored.
- shareholding/    ABSENT (folder). Partial substitute: operator-ferried
                   quarterly shareholding pattern in the same downstream note.
- research/        ABSENT. .gitkeep planted.
- screening/       42 CSVs (VINYAS screener + 6 peers full sets).
- presentation/    3 PDFs (Investor_Presentation_1, rpt 1, rpt 2).
- downstream/      1 file (operator-ferried 6-month update + shareholding).
                   Non-contract folder, preserved, weighed as downstream
                   signal only.
- other/           ABSENT.

## FRESHNESS PAIR CHECK
1. RESULTS -> CONCALL: newest results FY26 (28-May-2026) has same-quarter
   concall (03-Jun-2026 FY26 call). PASS.
2. RATING BULLETIN -> RATIONALE: two multi-page CRISIL reports present (full
   rationale, not one-line bulletins). PASS (stage confirms on read).
3. SEBI ORDER -> TEXT: none referenced. PASS (N/A).
4. AR -> LATEST AUDITED ANNUAL: FY26 AR present; latest audited annual = FY26.
   PASS.
Verdict: FRESHNESS PAIRS OK. No gate cap from freshness.

## COMPANY MEMORY
companies/VINYAS.md read and carried to every stage as COMPANY MEMORY
(spear memory only; not anchored evidence).

```yaml
stage: B00-inputs
company: VINYAS
run_date: 2026-09-01
model: orchestrator
status: complete
input_gaps:
  - prospectus (absent; NOT high, long-listed)
  - announcements (folder absent; operator-ferried downstream substitute present)
  - shareholding (folder absent; operator-ferried downstream substitute present)
  - research (absent)
  - other (absent)
freshness_pairs:
  - pair: results_to_concall
    trigger_doc: results/VINYAS_28052026..OutcomeBM280526final.pdf (FY26 audited)
    mate_expected: concalls/Concall_Jun_2026_Transcript.pdf
    status: PASS
    missing_doc: none
  - pair: rating_bulletin_to_rationale
    trigger_doc: rating/rating 2.pdf
    mate_expected: full rationale in same PDF
    status: PASS
    missing_doc: none
  - pair: sebi_order_to_text
    trigger_doc: none referenced
    mate_expected: n/a
    status: PASS
    missing_doc: none
  - pair: ar_to_latest_audited_annual
    trigger_doc: results FY26 audited
    mate_expected: annual-report FY26
    status: PASS
    missing_doc: none
freshness_verdict: FRESHNESS PAIRS OK
spear_load_bearing_facts:
  - customer_concentration_not_disclosed
  - material_cost_pct_revenue
  - repeat_vs_new_revenue
  - receivables_161d_root_cause
  - margin_puzzle_9_to_12_5_pct
flags: []
analyst_note: >
  Rating PDFs are scanned images; read by rendering. Announcements and
  shareholding folders absent but operator ferried a 6-month event timeline
  and the quarterly shareholding pattern (downstream tier). UA already NOT
  ELIGIBLE (FII+DII 7.02% > 3%), so the missing filed shareholding does not
  change UA. Two Nov-2025 concall files are duplicates.
```
