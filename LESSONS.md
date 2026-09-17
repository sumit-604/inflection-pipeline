# LESSONS — Inflection Alpha Pipeline (ACTIVE)

Working operational memory. Hard budget: under 1,500 tokens. This file
carries only what fires on every new run: the named failure catalogue,
recurring patterns, promoted-to-law fixes, and open actions. The full dated
run history lives in LESSONS_ARCHIVE.md (never deleted).

Read at start by /run-pipeline, /fttcp, /finalize, /compost. New dated run
entries append to LESSONS_ARCHIVE.md, never here. When /compost promotes a
pattern into this file, one old active lesson is reviewed for archiving: the
budget is fixed, not an unlimited append.

Tags. A lesson that applies to one sector or archetype ends with
[sector: <exact Section 1B sector cap row>] or [archetype: <CLAUDE.md
ARCHETYPE LIBRARY name>], or both. Untagged lessons apply to every run. The
LESSONS PRE-READ in /run-pipeline, /fttcp and /finalize matches on these tags.

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
_Written into a prompt/framework file so it cannot recur. One line each; the
full text of each promotion is in LESSONS_ARCHIVE.md under its date._
- [2026-07-12] frameworks/Section_1B_v3.3_Amendments.md — Amendment 4.5,
  normalized-ROCE anchor for TEMPORARILY DEPRESSED + RECOVERING (TATVA). Now
  governed by the v3.5.1 route-selection guard.
- [2026-08-19] input contract expanded to four folders (prospectus,
  announcements, shareholding, research) plus manifest listed_date, so
  recently-listed names are worked from primary filings (AIMTRON).
- [2026-08-25] run-pipeline.md stage-0 scaffold + runs/_template — .gitkeep in
  inputs/research/, and the /fttcp input gate reports it separately from a
  missing dossier (PERMAGNET, INDIAGLYCO).
- [2026-08-25] 00-orchestrator.md + 09b + run-pipeline.md — Freshness Pair
  Check: a filing without its companion filing sets CORPUS GAPPED-FRESHNESS
  and caps the gate at PROCEED WITH CAVEATS, the missing document named first
  in gate-recommendation.md (MANINDS; a late concall moved a signed variable).
- [2026-08-26] frameworks/Section_1B_v3_9_Amendments.md — Amendment 20,
  Step 1C relative valuation cross-check: live dated peer table, clusters on
  normalised earnings, and where the pillar destination sits >30% below the
  adjusted peer base the relative multiple governs, bounded by the sector cap.
  Memory-pulled peer multiples are barred (MANINDS, Correction 6).
- [2026-09-15] .claude/skills/section-1b/ — Section 1B v3.3 to v3.10, FTTCP
  v2.3, Debt Capacity v1.0, Market-Implied v1.0 and the macro sheet resolved
  into 17 chunks; stage 11 preloads the skill and cites the chunk beside each
  pillar row, multiplier, cap and ruling; Verifier C check 15 compares a cited
  chunk with its source (PR #163, PR #164).
- [2026-09-16] LESSONS discipline — LESSONS PRE-READ at the start of
  /run-pipeline, /fttcp and /finalize; /finalize step 8c writes the dated
  close-out table to the archive; the session-start hook runs the
  deferred-work check (PR #165).

## OPEN ACTIONS
_Pending framework edits Keerti maintains._
- Add a Steel / Integrated Metals row to the Section 1B cap table (SHYAMMETL
  ruled 20x ad hoc; MANINDS line pipe ruled 20x ad hoc on that precedent
  2026-08-25; no dedicated row exists). [archetype: Commodity converter]
- Add a Sugar / Agri-commodity cyclical row to the Section 1B cap table
  (KCPSUGIND ruled Agri-processing 20x ad hoc; no dedicated row exists).
  [sector: Agri processing] [archetype: Commodity converter]
- Add an Oil & Gas E&P row to the Section 1B cap table (ANTELOPUS shallow
  screen 2026-09-16; no row exists, nearest is Mining/mineral exploration 20x).
  Note PSC/RSC validity bounds the reserve base and so the terminal value.
- Add an Auto components row to the Section 1B cap table (RACLGEAR shallow
  screen 2026-09-16; no row exists, nearest is Cables/Industrial products 25x).
  [archetype: Build-to-spec component maker]
- Rule the cap row for a bulk-API converter with a commodity-solvents leg
  (IOLCP shallow screen 2026-09-16; neither Pharma/CDMO 38x nor Specialty
  chemicals 35x describes it). [archetype: Commodity converter]
- Add Distribution rows to the Section 1B cap table (ENTERO 2026-08-30, ruled
  18-20x ad hoc). Operator proposal: Distribution-commodity 18-19x;
  Distribution-value-added 25-26x; blended by revenue share. Any distributor.
- Amendment 14 fade guard (ENTERO 2026-08-30): where the TAM stage's
  SOM-implied growth is materially above the faded projection (fade 10% vs
  SOM-implied 26.4%), flag the fade for operator ruling rather than applying
  it silently. For /compost to promote into a prompt/framework fix.
- Canary (canary/verifier.py) needs an Anthropic API key; none is configured,
  so it has never run (checked 2026-09-15). Rewrite it to call Claude Code
  headless (`claude -p`) so it runs on the Max subscription. PR #162.
- fetch_bse_announcements in tools/collector/collect_to_repo.py is UNTESTED
  against the live BSE API. This container has no web access, so the first
  run that uses it is the first test. Check announcements/ after that run,
  then confirm and close this action. PR #167.
- PENDING FOR THE NEXT PROMPT BRANCH (2026-09-15):
  1. prompts/10-input-assembly-pipeline.md rule 3, line 22 still says "put the
     more conservative one in the table".
  2. Amendment 6 range rounding: the rule says nearest 0.5x, its own example
     rounds the top down (37x -> 34-39.5x). section-1b chunk 06 copies both.
     Operator ruling needed, then align chunk 06.
  3. OR-9 (proposed): Amendment 24 caps size at starter when the residual
     exceeds 25% of CMP; Amendment 25 permits a starter only at 25% or less.
     Reading A: size zero. Reading B: a 2-3% starter. Operator ruling needed.
