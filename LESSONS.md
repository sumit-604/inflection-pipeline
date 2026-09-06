# LESSONS — Inflection Alpha Pipeline (ACTIVE)

Working operational memory. Hard budget: under 1,500 tokens. This file
carries only what fires on every new run: the named failure catalogue,
recurring patterns, promoted-to-law fixes, and open actions. The full dated
run history lives in LESSONS_ARCHIVE.md (never deleted).

Read at start by /run-pipeline, /fttcp, /finalize, /compost. New dated run
entries append to LESSONS_ARCHIVE.md, never here. When /compost promotes a
pattern into this file, one old active lesson is reviewed for archiving: the
budget is fixed, not an unlimited append.

## NAMED FAILURE CATALOGUE
_Companies whose failure mode is a standing pattern-match on every new name.
The rule is codified in prompts/00-orchestrator.md FLAG-CASH (the
"Kernex/Tipco/Rappid/Ind Swift guard") and the CLAUDE.md NEVER rule:
INDETERMINATE cash conversion never silently resolves to PROCEED._
- **Kernex** — cash conversion DECLINING with catalyst NONE caps the FTTCP
  disposition at DEEP WATCH (the "Kernex cap").
- **Tipco / Rappid Valves / Ind Swift** — INDETERMINATE cash that must not
  be waved through to PROCEED; the verdict caps at PROCEED WITH CAVEATS with
  the missing evidence (rating rationale / receivables ageing) named.
  Per-company post-mortems not yet written; the live rule is the orchestrator
  guard above.

## RECURRING PATTERNS
_Seen across more than one run; fire on every new company. /compost mines
LESSONS_ARCHIVE.md for 2+ occurrences and promotes qualifying patterns here._
- Operator text pasted as chat attachments arrives empty; screenshots,
  direct chat-box text, and .md/.txt uploads work. (6+ times.)
- PDF tooling absent at session start: the Read tool needs poppler-utils
  (pdftoppm) and pypdf's cffi backend is often broken. Fix: apt-get update
  then install poppler-utils, pip install --force-reinstall cffi, verify
  with a real Read. Reliable default: pre-extract every input PDF to
  page-marked .txt up front and point every stage/verifier at the .txt, so
  no stage hits the ~20-32MB image-render wall.
- Verifier A (haiku) first pass mislabels severity, inventing false
  CRITICALs that would force REWORK (a matched figure, a faithfully
  transcribed company anomaly, or a screener-vs-AR basis difference is not a
  finding). Orchestrator sanity-checks every Verifier A CRITICAL against its
  own source_truth column, then re-invokes once with the severity-semantics
  plus coverage addendum.
- collect_to_repo v3 defects recur: wrong sector_cap_row (defaults to
  "Pharma/CDMO"), mislabeled AR year, empty screener P&L/BS/CF/Quarters CSVs
  (only Data_Sheet populated), broker notes misfiled as company
  presentations. Record each in B00.input_gaps, override to the
  evidence-maximizing default, flag sector_cap for phase-3 confirmation.
- Stage-0 operator pause (AskUserQuestion) sometimes closes its stream in
  remote sessions; when it does, proceed on documented evidence-maximizing
  defaults and record in B00. It sometimes delivers, so it is not always
  undeliverable.
- Foundational filings for recently-listed names (IPO prospectus, Reg 30
  announcements) carry the promoter/group history and restated pre-IPO
  financials; their absence thins the backward baseline. The input contract
  now carries the folders (see PROMOTED TO LAW).

## PROMOTED TO LAW
_Written into a prompt/framework file so it cannot recur._
- [2026-08-26] frameworks/Section_1B_v3_9_Amendments.md — Amendment 20, new
  step 1C Relative Valuation Cross-Check. After the pillar build, before the
  verdict card: Claude web supplies a live peer table (4-6 peers; trailing P/E,
  clean/forward P/E, ROCE, growth, net debt, governance), clusters on normalised
  earnings, places the subject with stated adjustments, rules bear/base/bull
  exit multiples. Pillar destination >30% below the adjusted peer base = the
  relative multiple governs (bounded by the sector cap), pillar shown as a
  cross-check. Sector caps reviewed annually against live peer medians. Peer
  multiples must be live and dated; memory-pulled multiples are barred. Caught
  on MANINDS: pillar output 8.1-12.6x vs peer quality cluster ~30x; stale
  multiples in Claude web's memory caused Correction 6. Web-side ferry:
  docs/team_workflow_amendments_maninds_2026-08-26.md.
- [2026-07-12] frameworks/Section_1B_v3.3_Amendments.md — Amendment 4.5,
  Normalized-ROCE anchor for TEMPORARILY DEPRESSED + RECOVERING verdicts: a
  document-gated third ROCE anchor (median pre-depression cycle ROCE, capped
  at the evidenced level, a named unwind catalyst required), blended by
  recovery probability and self-withdrawing if the recovery does not print.
  Stops Pillar 1 from pricing a capital-cycle trough as permanent and
  missing transition setups. Caught on TATVA. Now superseded by the
  Section_1B_v3.5.1 route-selection guard.
- Input contract expanded to four folders (prospectus, announcements,
  shareholding, research) plus manifest listed_date, so recently-listed
  names are worked from primary filings, not third-party reconstructions.
  Caught on AIMTRON.
- [2026-08-25] run-pipeline.md stage-0 scaffold + runs/_template: inputs/research/
  absent on PERMAGNET and INDIAGLYCO runs; cause is git not tracking empty
  directories; fix is a .gitkeep planted by the scaffold. The /fttcp handover
  input gate now reports "inputs/research/ missing" as distinct from
  "dossier missing".
- [2026-08-25] corpus completeness (MANINDS) — Freshness Pair Check into
  00-orchestrator.md + 09b + run-pipeline.md. A present filing can hide an
  absent companion filing; the count passes and Halt 1 runs blind. Rule: the
  newest results filing needs its same-quarter concall; a rating bulletin its
  full rationale; a referenced SEBI order its text; the AR must not trail the
  latest audited annual results. A missing mate sets CORPUS GAPPED-FRESHNESS
  and caps the gate at PROCEED WITH CAVEATS, missing document named the first
  line of gate-recommendation.md. Caught on MANINDS: Q1FY27 results in corpus,
  Q1FY27 concall (filed to BSE three days before the run) absent; 09b listed it
  as a gap but the gate did not block, operator found it several Phase 2 turns in.
  MANINDS coda (2026-08-25): the kill line was already breached when the model
  was signed — the Q1FY27 concall disclosed India standalone at Rs2,200-2,300cr
  (below the ~Rs2,500cr kill) only after Halt 1 sign-off; the freshness check
  exists for this. A late primary filing can move a signed decision variable,
  not just fill a gap.
- [2026-08-26] Relative Valuation Cross-Check (MANINDS) — Section 1B v3.8
  Amendment 20 (Step 1C). MANINDS pillar output 8.1-12.6x vs a live peer
  quality cluster ~30x (Welspun ROCE 23% net cash, Ratnamani); the pillar was
  correct on its own terms yet priced the converter far below where the market
  prices the peer set, and no step forced that gap to be seen before the
  verdict card. Rule: after the pillar build and before the verdict card, a
  live dated peer table (4-6 peers) with quality/value clusters on normalised
  earnings; place the subject with named adjustments; rule bear/base/bull exit
  multiples; where the pillar destination sits more than 30% below the adjusted
  peer base, the relative multiple governs and the pillar is shown as a
  cross-check (both on the card). Sector cap and single-credit still bind; the
  decision rules are unchanged. Correction 6: stale multiples in Claude web's
  memory (a peer multiple recalled, not live-fetched) is a recording error, not
  a peer input; Step 1C now bars it. Sector caps reviewed annually vs live peer
  medians.

- Stage 0 downshift conflict (CEIGALL 2026-09-06): DISPATCH routes stage 0 to
  haiku, but /run-pipeline instructs the orchestrator to run stage 0 itself,
  so it always executes at the session model. Every run logs a DOWNSHIFT
  FAILURE that no agent-file edit can fix. Needs a prompt reconciliation.
- Input-contract concall cap (CEIGALL 2026-09-06): the contract caps
  inputs/concalls/ at 3 while collectors now routinely deliver 4. Stage 5 was
  given 3, and verifier B traced 7 missed findings to the transcript withheld.
  Remediation cost 3 stage-5 runs and 2 stage-6 runs, 41% of the run's tokens.
  Where a fourth transcript exists it should be passed as primary.

## OPEN ACTIONS
_Pending framework edits Keerti maintains._
- Add a Steel / Integrated Metals row to the Section 1B cap table
  (SHYAMMETL ruled 20x ad hoc; MANINDS line pipe ruled 20x ad hoc on the
  SHYAMMETL precedent 2026-08-25; no dedicated steel/line-pipe row exists).
- Add a Sugar / Agri-commodity cyclical row to the Section 1B cap table
  (KCPSUGIND was ruled Agri-processing 20x ad hoc; no dedicated row exists).
- Add Distribution rows to the Section 1B cap table (ENTERO 2026-08-30, ruled
  18-20x ad hoc; no pharma/MedTech distribution row exists). Operator proposal,
  derived: Distribution-commodity (pure fulfilment) 18-19x; Distribution-
  value-added (agency/commercial) 25-26x; blended by revenue-share of each
  mode. Applies to any distributor.
- Amendment 14 fade guard (ENTERO 2026-08-30): the automatic revenue fade-to-10%
  on MODEST EM can contradict a consolidation thesis the same run relies on.
  Where the TAM stage's SOM-implied growth is materially above the faded
  projection (Entero: fade 10% vs SOM-implied 26.4%), flag the fade for operator
  ruling rather than applying it silently. For /compost to promote into a
  prompt/framework fix.
