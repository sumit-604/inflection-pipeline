# LESSONS — Inflection Alpha Pipeline

Operational memory. Every session reads this file at start. Every
/run-pipeline, /fttcp, and /finalize session appends one dated entry at
close: what broke or dragged this run, in one line each; write "clean run"
if nothing. Entries are never deleted. When a lesson is promoted into a
prompt file so it cannot recur, note it under PROMOTED TO LAW.

Dated entries, newest first within each section. Date format YYYY-MM-DD.
/compost reads this file to find patterns appearing 2+ times and proposes
the prompt-file edits that would make each recur-proof.

## RECURRING PATTERNS
_Patterns seen across more than one run. This is the section /compost mines
for 2+ occurrences._

- Operator pastes of text as chat attachments arrive empty; screenshots and direct chat-box text always work; .md/.txt file uploads work. (Observed 6+ times.)

## WHAT BROKE AND THE FIX
_A mechanical failure or wrong output this run, and what resolved it._

- [2026-07-12] AZAD phase 3 (finalize): framework gap surfaced, not a mechanical break. The Section 1B four-pillar output is a 3-year, quality-anchored EXIT multiple with a Hurdle Ratio anchored to CURRENT PE, so it functions as a 25%-sleeve entry screen, not an intrinsic valuation: it structurally prints AVOID on every already-discovered compounder (AZAD earned a ~21x destination while trading ~121x -> AVOID with an entry zone ~45% below the stock's lowest tested price since listing), truncates long-runway compounding at 3 years, and never tests what the price implies (a reverse-DCF shows the market pricing ~31% EPS CAGR for 10 years). Also: ROCE-anchored Pillar 1 is fragile for capex-cycle names (statutory 8.8% / operational 12% / mgmt-adjusted 20.7% swung the destination 3-5x and forced a per-run operator override to strip idle QIP capital). Fix drafted as two PROPOSED (non-operative) Section 1B amendments pending Keerti sign-off: P1 mandatory reverse-DCF + DCF intrinsic cross-check (entry authority unchanged), P2 mid-cycle operational-ROCE anchor for capex-cycle archetypes (codifies the AZAD ROCE override as a standing rule). For /compost to weigh.
- [2026-07-11] KARNIKA phase 2 (fttcp): clean run. Operator delegated the entire deliberation ("every judgment call yours") rather than the section-by-section stop cadence, so it ran end to end. Verdict DEEP WATCH leaning AVOID (composite +2/8): revenue FIRING, margin/cash/ROCE all STAGNANT. Two data gaps constrained the ROCE and cash engines and are the main phase-3 dependencies: FY26 ROCE is NOT FOUND (only FY25 22% anchored, Note 37) and FY26 debtor-days were never disclosed; both must be anchored at stage 10.
- [2026-07-11] KARNIKA phase 1: Verifier A (haiku) first pass silently ran degraded, concluding source PDFs were "not accessible" and verifying by cross-report consistency instead; it produced 5 false CRITICALs including a bogus TAM 10x-unit claim that was its own arithmetic error, which would have force-triggered REWORK. Re-invoked once with an explicit "PDFs render via the Read pages parameter, double-check your own unit conversions, and distinguish legitimate basis differences from misreads" addendum; the source-grounded re-run returned 0 CRITICAL and 89.5% acceptance. Orchestrator must sanity-check a verifier's coverage_note for a silent source-access failure before propagating its acceptance_rate/REWORK.
- [2026-07-11] KARNIKA phase 1: PDF tooling absent at session start. The Read tool needs poppler-utils (pdftoppm) to render PDFs and it was not installed; pypdf was present but its cryptography/cffi backend was broken. Fixed with apt-get install poppler-utils (after apt-get update; one mirror 404'd) plus pip force-reinstall cffi. Verify PDF rendering with a real Read call, not just pypdf, at stage 0.
- [2026-07-11] KARNIKA phase 1: auto-collector (collect_to_repo v3) manifest data-quality defects. concalls_available was false while two genuine FY26 earnings transcripts sat in inputs/concalls (ran NORMAL concall mode using them); sector_cap_row was "Pharma / CDMO" for an apparel/kidswear company with apparel peers (flagged for phase 3). Both recorded in B00.input_gaps and surfaced in the gate recommendation. The single stage-0 operator pause could not be asked (AskUserQuestion stream closed in this remote session), so proceeded on documented evidence-maximizing defaults.
- [2026-07-11] Repo tasks are not done at 'pushed' — they are done at 'merged.' Unmerged branches are invisible to every new session. After any repo task: push, then immediately merge, then proceed.
- [2026-07-10] Changelog entries must be written by the session that made the change, never pre-supplied by the operator or planner — a pre-supplied changelog claimed the RRM clarification existed when the task had been skipped. Caught by session cross-check; fixed as Amendment 4.4.
- [2026-07-10] Documents added to a local run folder after the initial push do not exist for cloud sessions until --push-again runs. Cost: half a phase-1 re-run on AKUMS (AR, results, rating all local-only). Promoted to law: stage-0 empty-folder pause.
- [2026-07-10] Sessions started before a command-file merge run the OLD rules for their whole life. Fix: after merging any .claude/commands change, kill or finish pre-merge sessions before relying on the new behavior.
- [2026-07-09] Background launch-and-wait stalls silently (2 hours on APEXECO stage 1-2). Promoted to law: foreground execution discipline in run-pipeline.
- [2026-07-09] Interactive section-by-section deliberation frustrates the operator; jargon-dense drafts get rejected. Promoted to law: fttcp autonomous plain-language draft with year-wise tables.
- [2026-07-09] openpyxl read_only leaves Windows file handles open, making staging undeletable and polluting git. Fixed in collect_to_repo v3.1 (wb.close + gitignore _download).
- [2026-07-09] Notion text properties reject < and → characters; EM Classification select lacks NONE, Promoter Verdict select lacks CAUTION. Workaround: clean characters, verdicts to text fields; consider adding select options.

## SLOW SPOTS
_Stages or steps that dragged: where wall-clock or attention went._

(none yet)

## PROMOTED TO LAW
_Lessons written into a prompt file so they cannot recur. Each entry names
the file and the change._

(none yet)

- [2026-07-12] AZAD phase 1: large annual report (249-page, 8.5MB) crashed stage 3 with a 32MB request error from rendering too many PDF pages as images. Fixed by extracting a page-anchored plain-text cache (pypdf, "===== PDF PAGE n =====" markers) for every input PDF and routing all text-reading stages to it, PDF Read-pages kept only as small-range visual fallback. Printed AR page = PDF sheet minus 3. Poppler-utils was again absent at start (one apt mirror 404'd; fixed after apt-get update) plus pypdf/cffi force-reinstall. Consider promoting the text-cache step to a stage-0 preprocessing law for any AR over ~150 pages. Clean run otherwise: verdict PROCEED WITH FLAGS, FLAG-CASH GROWTH-INDUCED + FLAG-GATE0, confidence 92 high; manifest sector_cap_row 'Pharma / CDMO' wrong again (precision aerospace/energy engineering), flagged for phase 3.

- [2026-07-12] AZAD phase 2 (fttcp): clean run. Autonomous plain-language draft accepted; composite +4/8 DEEP WATCH leaning BUY-ON-DIPS (Revenue FIRING, Margin STAGNANT, Cash STARTING, ROCE RECOVERING). Two operator overrides on valuation inputs: (1) ROCE on operational basis, strip idle QIP capital (cash+CWIP+advances), lifting FY26 ROCE from statutory 8.8% to operational ~12% and Pillar 1 base to ~14.3x; (2) Strategic Premium given and raised 2x->3x on strong OEM relationships (declined the +4-6x monopoly tier: sole-supplier claim company-informed, peers could not verify, 81% three-OEM concentration is customer power). Destination PE ~21.9x additive. Operator moved straight to /finalize as sign-off. Sector_cap_row "Pharma / CDMO" wrong again, overridden to precision-engineering 25x for phase 3.
