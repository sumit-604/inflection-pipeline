---
description: STEP 1 intake. Name a company; Claude Code analyses the sector and business, picks peers, collects the corpus, pushes it, and runs Phase 1 to Halt 1. One trigger, no operator questions. Usage: /step1 <company name or ticker>
---
You are running STEP 1 (INTAKE) for the company:
$ARGUMENTS

Step 1 builds the shelf. It takes a company from a bare name to a committed
Phase 1 evidence pack that stops at Halt 1, so the operator's later mental-model
sessions pull ready analysis off a shelf instead of collecting per company. It
runs to completion in one go. It asks the operator NOTHING.

## WHY THIS COMMAND EXISTS (operator ruling 2026-09-05)

The old workflow ran a SPEAR pass in Claude web first, then collected the corpus
by hand. The web spear was inaccurate: it guessed value without the filings.
Inverted by operator ruling. Claude Code now does the first-pass analysis itself,
grounded in the corpus it is about to collect, across many companies up front.
The heavy vetting still happens later, at the operator's Halt 1 mental-model
exercise. Step 1 only has to make each company's evidence pack correct and
complete, never to reach a verdict.

## AUTONOMY CONTRACT (the point of the command)

- Ask the operator no questions. The two interactive pauses in the normal
  pipeline are SUPPRESSED here and replaced by standing defaults:
  - PEER SELECTION never pauses. Claude picks the peers and records why.
  - The Phase 1 EMPTY-FOLDER CONFIRMATION never pauses. The standing answer is
    "proceed with the gaps"; every absent document type is recorded in
    B00.input_gaps and the run degrades per the orchestrator DEGRADATION MAP.
- Stop at Halt 1. Never run /fttcp or /finalize from here. The Mental Model
  Declaration is left a DRAFT, unsigned; the operator signs it later.
- Nothing halts on company quality. Only mechanical failures halt (Section 7 of
  prompts/00-orchestrator.md). A weak-looking business is still shelved; the
  decision is the operator's at Halt 1.

## ENVIRONMENT

Claude Code desktop has live web (WebSearch/WebFetch) in this setup. Steps B and
C use it. If web is unavailable at run time, degrade: build the business read
from the collected annual report and presentation, and fall back to screener's
own Peers list for candidates, and say so in the brief. The collector and git
run locally:
- Collector folder: `C:\Users\SUMIT SHARMA\OneDrive\Desktop\screener_collector`
- Repo root:        `C:\Users\SUMIT SHARMA\repos\inflection-pipeline`
Run every Python invocation with `PYTHONUTF8=1` (the collector prints the rupee
sign and dies under Windows cp1252 when its output is redirected).

---

## A. RESOLVE IDENTITY

Resolve $ARGUMENTS to the screener ticker and URL. Search screener.in for the
name if a ticker was not given. VERIFY the URL returns HTTP 200 and the page
title is not "Error 404 Page Not Found" before trusting it. Prefer the
`/company/<TICKER>/consolidated/` URL when that page exists; fall back to the
standalone `/company/<TICKER>/`. Some names resolve only by BSE code, not symbol
(e.g. GEE Ltd = `/company/504028/`); use whatever URL actually loads. State the
resolved ticker, company name, and URL before continuing.

## B. ANALYSE SECTOR AND BUSINESS (web; this is the spear replacement)

Research the business the way an analyst reads a new name, not from a screener
label. Establish: what it makes and sells, the reporting segments and the
revenue mix, where the margin actually comes from, the customer and export
profile, and the ONE inflection or engine the thesis would rest on (a capex
ramp, a contract win, a mix shift). Pull the most recent quarter's print and
guidance. Write a short brief to
`runs/<ticker>-<YYYY-MM-DD>/step1-business-brief.md`: 10-15 lines, numbers first,
each material claim with its source URL. End the brief with 2-4 LOAD-BEARING
FACTS: the specific things a later stage must verify against the filings (a
guidance-vs-delivery pair, a related-party or governance item, a
concentration or cash-conversion figure). These become the run's first
verification priority, the same role a spear HIT's facts play.

## C. SELECT PEERS (no pause)

Pick THREE listed peers that mirror the ECONOMIC ENGINE from Step B, not the
generic sector basket. Match the segments and the margin/capex dynamics (for a
rubber-and-additives specialty maker, a rubber-chemicals leader and an additives
name beat a random "specialty chemicals" list). For each peer: verify the
screener URL loads (200, not 404), prefer `/consolidated/`, and write a
one-line "why it fits" into the brief. No lubricant/aroma pure-play listed? Say
so and take the closest structural comps. Do not ask the operator to confirm.

## D. PICK THE SECTOR CAP ROW (do not trust the collector)

Read the Section 1B Sector Cap Table in
`frameworks/Master_Project_Prompt_v3_6.md` and choose the row that matches the
business from Step B. The collector's auto-picker is unreliable (it defaults to
"Pharma / CDMO"); you will correct the manifest in Step F. State the chosen row
and its cap.

## E. WRITE companies.txt

Write the collector's `companies.txt` (overwrite it) with the main line and the
three peer lines, exactly:

```
<TICKER>:<main URL>
PEER:<TICKER>:<peer1 URL>
PEER:<TICKER>:<peer2 URL>
PEER:<TICKER>:<peer3 URL>
```

## F. COLLECT THE CORPUS (stage locally, then repair, then commit)

From the collector folder run the collector in DRY-RUN so it stages into the
repo without pushing:

```
PYTHONUTF8=1 py collect_to_repo.py --dry-run
```

It downloads the main company and the three peers, classifies the PDFs into
`runs/<ticker>-<YYYY-MM-DD>/inputs/{annual-report,concalls,peer-concalls,presentation,screening,...}`,
and writes `manifest.yaml`. Then REPAIR the known collector defects (see
LESSONS.md) before anything is committed:
- Correct `manifest.yaml` `sector_cap_row` to the Step D row if it differs.
- Confirm `inputs/annual-report/` holds the latest year's AR (the regex and
  two-most-recent rule now capture BSE-hosted reports; if the newest year is
  still missing, fetch it from the screener documents page / BSE and drop it in).
- Confirm the screening CSVs are not just Data_Sheet; note any empty
  P&L/BS/CF/Quarters CSV as a gap for B00.
- Verify each staged PDF opens (pypdf); name any unreadable file.

## G. SATISFY THE SPEAR GATE (auto-override, recorded)

Create `companies/<TICKER>.md` from `companies/_template.md`. Under `## SPEAR`
write, above the Mental Model block:

```
Spear: OVERRIDE <YYYY-MM-DD> (operator standing ruling 2026-09-05: Step-1 intake replaces the web spear)
```

Immediately below it, list the Step B load-bearing facts as the run's first
verification priority, and link the brief. Record one operator ruling line:
"<date>: Step-1 intake run; peers auto-selected; empty folders accepted as
gaps." This is the deliberate inversion from WHY THIS COMMAND EXISTS, not a gate
breach: the gate is satisfied by the recorded override, so the Phase 1 SPEAR
GATE check passes.

## H. RUN PHASE 1 TO HALT 1

Now run Phase 1 EXACTLY as `.claude/commands/run-pipeline.md` and
`prompts/00-orchestrator.md` define it, on `runs/<ticker>-<YYYY-MM-DD>`:
stage 0 inventory (with the freshness pair check and B00.input_gaps), stages 1-9
in dependency order, verifiers A/B/D and the Gate 0 + Emerging Moat half of
verifier C, the confidence delta, synthesis-lite (the three outputs/final files),
and the 09b Halt 1 dossier, with the per-stage session-cost ledger and the
close-out block. Carry the Step B brief and its load-bearing facts into every
stage task message as COMPANY MEMORY, alongside companies/<TICKER>.md. Obey the
orchestrator's rules verbatim: JIT context (paths not pasted PDFs), verifier
independence, per-stage validate-then-commit, model dispatch from the agent
frontmatter. The ONLY deviations are the two suppressed pauses from the AUTONOMY
CONTRACT above. Do NOT run stages 10-11, verifier C's valuation half, or the
full synthesis; those are Phase 3.

## I. PUSH AND REPORT (then stop)

Keep the whole intake on one run branch `run/<ticker>-<YYYY-MM-DD>`: the corpus,
the brief, companies/<TICKER>.md, and the Phase 1 outputs. Commit the corpus and
Phase 1 outputs as separate commits (corpus first, then "phase 1 (evidence):
<ticker> <date>"), each report ending with its commit hash and `git log -1
--stat` per FERRY AND COMMIT HYGIENE. Push the branch. `gh` is not installed;
print the `https://github.com/sumit-604/inflection-pipeline/pull/new/run/<ticker>-<YYYY-MM-DD>`
link for the operator to open the PR. Then print the Halt 1 message exactly as
run-pipeline.md step 7 specifies (dossier path, the three operator decisions, the
KILL / SHALLOW WATCH / PROCEED choice) and STOP. Do not proceed past Halt 1.

Append the dated one-line run note to LESSONS_ARCHIVE.md at close ("clean run" if
nothing broke), never to the active LESSONS.md.

## WHAT STEP 1 NEVER DOES

- Never asks the operator a question. If a real blocker appears (identity cannot
  be resolved, the entire corpus fails to download, a mechanical stage halts
  twice), STOP and report the specific failure; do not guess around it.
- Never signs the Mental Model Declaration and never runs /fttcp or /finalize.
- Never treats its own Step B brief as anchored evidence inside a stage; every
  stage number still comes from that run's filings, verified against the PDFs.
  The brief is COMPANY MEMORY, weighed, never a source.
- Never pushes run inputs straight to main; the intake lands on its run branch
  and a PR.
