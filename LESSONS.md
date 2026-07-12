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

- [2026-07-12] TATVA phase 2 (fttcp): verdict DEEP WATCH, composite +3/8 (revenue FIRING, margin STARTING, ROCE RECOVERING, cash DECLINING), Kernex cap engaged on cash. Sector cap corrected to Specialty chemicals 35x (manifest had Pharma/CDMO 38x). Operator pushed three times to lift the valuation by hand: credit Pillar 3b/3c for R&D and large TAM (declined; EM 19.2 is the evidence-weighted audited score and 3c pays only for documented long-tenor contracts per Amendment 4.2, not TAM), then set the destination PE to 15x and then 50x (declined; round-number exit PE violates the sole-authority "no round-number defaults, ever" rule, and 50x breaches the absolute 35x cap). Held the line and showed no legal multiple passes the hurdle at CMP (even the 35x ceiling gives HR 0.86 vs 1.953; the passing multiple is ~80x). Operator signed off the analysis as it stands; no override adopted. Lesson: the exit multiple is not an operator-override field; overrides are on inputs (ROCE, cash determination, sizing), and finalize will re-price a hand-set multiple to STOP against CMP anyway.
- [2026-07-12] TATVA phase 1: verdict PROCEED WITH CAVEATS, confidence 86. FLAG-CASH determined INDETERMINATE (capped the verdict at CAVEATS, not FLAGS): the FY26 rebound and Dahej/Jolva capex cycle point growth-induced, but no rating PDF was provided so the CRISIL working-capital rationale quote is NOT FOUND; rating rationale detail and receivables ageing are the named phase-3 dependencies. Resolving metric handed off: FY27 receivable days falling from ~185 with OCF/EBITDA positive = growth-induced; above 185 on rising revenue = structural.
- [2026-07-12] TATVA phase 1: Stage 6 (peer verification) died on the API 32MB request limit rendering 15 peer PDFs as images. Fixed by pre-extracting every transcript (plus AR, results, main concalls) to text with poppler pdftotext and pointing Stage 6 and all verifiers at the .txt files; re-ran clean. Proactively giving Verifier A text extracts also prevented the KARNIKA-style haiku false-degradation (it checked 35 numbers, 0 CRITICAL). Recommend making text-extraction the default for peer-heavy and verifier stages, or capping per-Read page ranges.
- [2026-07-12] TATVA phase 1: collect_to_repo v3 defects recurred (also seen KARNIKA 2026-07-11). AR file named Annual_Report_2022.pdf was actually the FY2024-25 report (verified from the 26 Aug 2025 submission letter); sector_cap_row "Pharma / CDMO" is wrong for a specialty-chemicals maker (SDA/PTC/electrolyte/PASC); screener P&L/BS/CF/Quarters/Customization CSVs exported as empty templates with only Data_Sheet.csv carrying values; 15 peer transcripts supplied against the 0-12 contract cap (all 15 used, text-extracted). All recorded in B00.input_gaps.
- [2026-07-12] TATVA phase 1: Gate 0 first pass returned a false AVOID (core 38) because Block E (promoter holding, pledge, contingent liabilities) was absent from the empty screener export and the abbreviated Reg-33 results PDFs. Recomputed Block E from the FY25 AR per the DEGRADATION MAP (promoter 72.02%, contingent-liab/net-worth 0.71%; E2/E3 still N/A, quarterly SHP filings not provided) to AVERAGE (core 48). Orchestrator must check whether a low Gate-0 classification rests on a fillable data gap before propagating it.
- [2026-07-12] TATVA phase 1: Stage 8 emitted a FLAG-PROMOTER on a CAUTION verdict; Section 4 reserves FLAG-PROMOTER for CONCERN/AVOID only. Orchestrator instructed synthesis to drop the flag and carry the promoter items (revoked GPCB Ankleshwar closure, KMP pay +27.9% vs PAT -81%, partial web search) as caveats/monitorables instead.
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

- [2026-07-12] frameworks/Section_1B_v3.3_Amendments.md — Amendment 4.5 (v3.5), Normalized-ROCE anchor for TEMPORARILY DEPRESSED + RECOVERING verdicts. Root cause: Pillar 1 anchors on the trough ROCE (current + FY[Y+2] blend), which prices a capital-cycle trough as permanent and drives the destination PE and entry zone far below any price the market has paid, systematically missing transition setups (the operation's own strategy). Caught on TATVA when the operator put the weekly chart next to the model: model entry Rs 121 / MoS Rs 97 vs a four-year market floor of Rs 590; normalizing ROCE to the evidenced pre-capex 15-20% recomputed fair value to Rs 350-600, matching the market. Fix: a 📄-gated third ROCE anchor (median pre-depression cycle ROCE, capped at the evidenced level, requiring a named unwind catalyst), blended per recovery probability, self-withdrawing if the recovery does not print. The decision discipline is unchanged: even under 4.5 TATVA stays AVOID-on-valuation at Rs 1,326 because the market prices it at fair value, not at a 25% discount.
