# STAGE 0 — INPUT VALIDATION AND CORPUS AUDIT

Run folder: runs/titanbio-2026-09-10
Company: Titan Biotech Ltd (TITANBIO), BSE 524717
Run date: 2026-09-16 (corpus collected 2026-09-10)
CMP Rs 437, market cap Rs 1,806 cr (manifest)
Sector cap row: Specialty chemicals (35x)

## SPEAR GATE

PASSED on a recorded override.

`companies/TITANBIO.md` carries: `Spear: OVERRIDE 2026-09-10 (operator standing
ruling 2026-09-05: Step-1 intake replaces the web spear)`.

The four load-bearing facts in that file are the run's first verification
priority. They are carried into every stage task message. All four are
accounting-structure questions:

1. Freight gross-up inside reported revenue (FY26 and Q1FY27).
2. Peptech Biosciences associate arithmetic that does not reconcile.
3. TM Media brand versus the Titan Media Ltd associate.
4. Rs 34.41 cr investing outflow that is mostly financial assets, not plant.

## MANIFEST

Parses. Fields present: company, ticker, cmp, market_cap_cr, run_date,
run_type (full), concalls_available (false), sector_cap_row, listed_date
("NOT FOUND", long-listed), notes.

## FOLDER INVENTORY

| Folder | Count | Status |
|---|---|---|
| prospectus/ | 0 | Not expected. Long-listed company, incorporated 1992. Not a gap. |
| annual-report/ | 3 | FY2026 (201 pp), FY2025 (195 pp), FY2024 (200 pp). Contract asks 0-1; three years held, FY2026 primary. |
| results/ | 4 | Q1FY27, FY26 audited, Q3FY26, Q2FY26. Contract uses the 3 most recent. |
| rating/ | 0 | GAP. No rating exists. |
| concalls/ | 0 | Declared absent. concalls_available false. NO-CONCALL MODE. |
| peer-concalls/ | 11 | ADVENZYMES 4, FERMENTA 4, VIDHIING 3. |
| announcements/ | 8 | Reg 30 filings, Feb-2025 to Sep-2026. |
| shareholding/ | 0 | GAP. BSE XBRL API did not serve. |
| research/ | 0 | No broker notes. No effect on anchored evidence. |
| screening/ | 24 | Company + 3 peers. Only Data_Sheet.csv populated (known collector defect). |
| presentation/ | 0 | GAP. The company publishes none. |
| other/ | 0 | Absent. |

Total 26 PDFs. All 26 open and carry a text layer. All are pre-extracted to
page-marked `.txt` under `work/extracted/`, mirroring the `inputs/` tree. No
unreadable file.

HALT CHECK: manifest parses and the inputs tree is not empty. The run proceeds.
No count-based halt applies.

## FRESHNESS PAIR CHECK

| # | Pair | Trigger | Mate | Status |
|---|---|---|---|---|
| 1 | Results to concall | Q1FY27 results, 13-Aug-2026 | Q1FY27 transcript | SKIPPED. concalls_available false; the absence is declared, not a gap. |
| 2 | Rating bulletin to rationale | None. rating/ is empty. | n/a | PASS. No trigger. |
| 3 | SEBI order to order text | None. A grep over every extracted filing found no SEBI adjudication, show-cause or settlement order reference. | n/a | PASS. No trigger. |
| 4 | AR to latest audited annual results | FY2025-26 audited results, 30-May-2026 | FY2025-26 annual report | PASS. The FY2026 AR is held. |

**freshness_verdict: FRESHNESS PAIRS OK.**

The gate recommendation is not capped by freshness.

## EMPTY-FOLDER CONFIRMATION

Asked and answered. The empty folders (rating, presentation, shareholding,
research, prospectus) were listed to the operator in the step-1 intake report
on 2026-09-10, with the reason for each. The operator answered "go" on
2026-09-16. Recorded as: proceed with these gaps. The question is not asked
again for the rest of this run.

## DEGRADATION APPLIED

- **NO-CONCALL MODE.** Stage 5 reads the AR MD&A, the Directors' Report and
  the results commentary instead of transcripts. credibility_grade defaults to
  C and may rise to B only on documented guidance-versus-delivery evidence.
  Never A. B05 carries `no_concall_mode: true`. Verifier B audits against AR
  and results sources. Stage 7's F2 test uses capex-completion evidence from
  AR timeline statements.
- **Stage 6 still runs.** peer-concalls/ holds 11 transcripts.
- **No rating.** Stage 10 will mark rating_wc_quote unresolved. Pillar 2 runs
  without rating evidence in phase 3.
- **No presentation.** Stage 4 runs from the annual report and results.
- **No shareholding filing.** FII+DII comes from the screener quarterly table,
  not a filing. Stage 11 must decide whether that source evidences the UA
  institutional-absence qualifier.

## COMPANY MEMORY

`companies/TITANBIO.md` exists and is carried into every stage task message as
COMPANY MEMORY. It holds the spear override, the four load-bearing facts, three
operator rulings dated 2026-09-10, and the run folder link. No prior run exists
for this ticker, so there is no PRIOR RUN CONTEXT. The business brief at
`runs/titanbio-2026-09-10/step1-business-brief.md` travels with it and carries
the same status: memory to weigh, never anchored evidence.

## SCAFFOLD

Created: `outputs/blocks/`, `outputs/reports/`, `outputs/final/`.
`inputs/research/.gitkeep` is present.
