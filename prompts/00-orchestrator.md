# INFLECTION ALPHA PIPELINE ORCHESTRATOR v1.0
## Sonnet 5 Primary Pipeline with Claude Verification Layer

Replaces the Gemini (Jaimini) upstream pipeline. One model family end to end.
Valuation authority: Master Project Prompt v3.6, Section 1B layer set (v3.3
Amendments + v3.5.1 + v3.6; v3.6 governs overlaps) (Four-Pillar
Framework, RRM dual-track, Hurdle Ratio), FTTCP v2.1. No other exit PE source
is permitted anywhere in the pipeline.

---

## PHASES

The pipeline runs in three phases, split so the FTTCP go/no-go and the
operator's deliberation sit BETWEEN evidence gathering and the final
investment decision. Each phase is a separate command; the phases share
the run folder and hand off through files on disk.

**PHASE 1 — EVIDENCE (`/run-pipeline runs/<folder>`).** Stages 0 through
9, then verifiers A, B, D and the Gate 0 + Emerging Moat half of verifier
C (its valuation-adherence checks are deferred to phase 3, since B10/B11
do not yet exist). Then a synthesis-lite writes three files to
outputs/final/: `business-narrative.md`, `gate-recommendation.md` (the
FTTCP go/no-go per the verdict-selection rules, minus every
valuation-dependent element), and `verifier-summary.md`. Stages 10, 11,
verifier C's valuation half, and the full synthesis do NOT run in phase 1.
Phase 1 ends by handing off: "Phase 1 complete. Next: /fttcp
runs/<folder> for deliberation."

**PHASE 2 — DELIBERATION (`/fttcp runs/<folder>`).** Operator-led FTTCP
deliberation. It records the FTTCP ROCE forward verdict, confirms or
overrides the cash-conversion structural / growth-induced determination,
and captures every operator override, writing the deliberation record to
`outputs/final/fttcp-deliberation.md`.

**PHASE 3 — FINALIZE (`/finalize runs/<folder>`).** Refuses to start
until `outputs/final/fttcp-deliberation.md` exists (naming /fttcp as the
missing step). Then runs autonomously: stage 10 input assembly (now also
consuming the deliberation record), stage 11 valuation, stage 14 Role 2
investment thesis, stage 15 Role 3 devil's advocate, verifier C's
deferred valuation-adherence audit (extended to check Role 2's decision
rules and position sizing), then the full synthesis producing all four
deliverables (including `fttcp-handoff.md` as the archive dossier) and the
`outputs/final/notion-payload.md` save payload.

**Phase-3 authority rule.** The FTTCP deliberation conclusions recorded in
phase 2 are AUTHORITATIVE in phase 3. The deliberation-confirmed ROCE
forward verdict, the structural / growth-induced determination as the
operator confirmed or overrode it, and every recorded operator override
become authoritative inputs at stage 10 and flow through valuation,
thesis, and devil's advocate. Wherever a deliberation conclusion conflicts
with a determination the pipeline made earlier in phase 1, the
deliberation conclusion supersedes it, and the assembly anchors the value
to the deliberation record.

---

## 1. INPUT CONTRACT

Run folder structure (Google Drive, mirrored to local before run):

```
/inflection-alpha-runs/<ticker>-<YYYY-MM-DD>/
  manifest.yaml
  inputs/
    prospectus/       (0-2 PDF; DRHP / RHP. MANDATORY to attempt when the
                       company listed within ~3 years of run_date. Carries
                       promoter/group history, the full group-company map,
                       and restated pre-IPO financials that fill the backward
                       baseline.)
    annual-report/    (0-1 PDF)
    results/          (0-3 PDFs; if more than 3, use the 3 most recent)
    rating/           (0-1 PDF; if more than 1, use the most recent)
    concalls/         (0-3 PDFs, honoring concalls_available)
    peer-concalls/    (0-12 PDFs)
    announcements/    (0-N PDFs; exchange filings / SEBI Reg 30 material
                       events, last ~12 months: acquisitions, capital raises,
                       order wins, board changes, divestments. The 📄
                       documented-ACTION record for the intent-and-action
                       cross-check and for stages 5/7/8.)
    shareholding/     (0-N; latest quarterly shareholding pattern filing.
                       Closes the FII+DII UA qualifier and the promoter
                       holding/pledge trend.)
    research/         (0-N; sell-side / broker notes. NON-ANCHORED, leads and
                       management-intent cross-check only, never anchored
                       evidence — same status as COMPANY MEMORY.)
    screening/        (0-N; csv / txt / pdf / xlsx)
    presentation/     (0-N)
    other/            (0-N; preserved, never consumed)
  outputs/                            (created by pipeline)
    blocks/                           (YAML handoff blocks, one per stage)
    reports/                          (full stage outputs)
    final/                            (narrative, verdict, verifier summary)
```

Inputs are identified BY FOLDER, not by filename. Any filenames are
accepted inside each subfolder; the pipeline reads whatever PDFs (or
csv/txt/xlsx for screening/) a folder contains.

No input folder is required. Every folder holds 0-N files. The pipeline
inventories what exists per folder: prospectus (0-2), annual-report (0-1),
results (0-3, use the 3 most recent if more), rating (0-1, most recent if
more), concalls (0-3, honoring `concalls_available`), peer-concalls (0-12),
announcements, shareholding, research, screening, presentation, and other
(preserved, never consumed). Every absent document type is recorded in
`B00.input_gaps` and carried on every downstream block. Degraded stages run
per the DEGRADATION MAP below; the pipeline degrades gracefully rather than
gatekeeping input.

RECENTLY-LISTED PRIORITY: when the company listed within ~3 years of
run_date (derive from `manifest.listed_date` if present, else from the
prospectus/IPO evidence in inputs), the IPO prospectus is the foundational
document — it carries the promoter and group history, the group-company map
with business descriptions, and the restated pre-IPO financials that no
other input holds. If `inputs/prospectus/` is empty for such a company,
stage 0 records it as a HIGH-priority gap (not merely absent), because the
backward baseline, the promoter/group picture, and the related-party
trajectory will otherwise be built on fewer years and thinner evidence.

Concall quarter map: from filename if evident, else read each transcript's
first page; confirm chronology before stage 5.

manifest.yaml schema (filled by Keerti before triggering):

```yaml
company: Gem Aromatics Ltd
ticker: GEMAROMA
cmp: 412.50            # as of run date
market_cap_cr: 1240
run_date: 2026-07-09
run_type: full         # full | refresh | valuation-only
sector_cap_row: "Specialty chemicals"   # from Section 1B cap table
listed_date: ""        # optional YYYY-MM-DD; if within ~3y of run_date the
                       # IPO prospectus is a MANDATORY collect + HIGH gap
notes: ""              # free text, passed to synthesis
```

Stage 0 inventories this contract. It halts ONLY if `manifest.yaml` is
missing or unparseable, or the entire `inputs/` tree is empty. In every
other case the run proceeds: each absent document type is recorded in
`B00.input_gaps` and carried on every downstream handoff block under
`input_gaps`. No document count ever halts the run.

### NO-CONCALL MODE

Some companies hold no earnings calls. When `manifest.yaml` sets
`concalls_available: false`, the `inputs/concalls/` folder is not required
and the concall-dependent stages run in degraded mode:

- **Stage 5** runs in degraded mode: instead of transcripts it reads the
  annual report's MD&A, the chairman's letter, and the results
  commentary. It extracts stated guidance and checks delivery against the
  results PDFs. `credibility_grade` defaults to **C** and may rise to **B**
  only on documented AR-guidance-vs-results delivery evidence, never to
  **A**. The B05 block gains `no_concall_mode: true`.
- **Stage 6** runs only if `inputs/peer-concalls/` contains files;
  otherwise it is skipped, with `input_gaps` noting the skip.
- **Verifier B** audits the communication analysis against the AR and
  results sources instead of transcripts.
- **Stage 7's F2 test** uses capex-completion evidence across AR timeline
  statements in place of the promise-delivery record.

### DEGRADATION MAP

When a document type is absent, the pipeline degrades rather than halts.
Each absent type is named in `B00.input_gaps` and the affected blocks
carry the gap.

- **No annual report.** Stages 2 and 3 are skipped; their blocks are
  emitted with `status: skipped` and the gap named. Stage 4 runs from the
  presentation and results commentary if either is available; if neither
  exists, stage 4 is skipped, block emitted with `status: skipped` and
  the gap named.
- **No results.** Gate 0 (stage 1) runs from screening data alone. Stage
  10 marks the latest-period fields `unresolved`.
- **No rating.** Stage 10 marks `rating_wc_quote` unresolved. Stage 11's
  Pillar 2 determination proceeds without rating evidence, defaulting
  conservative per the framework. INDETERMINATE handling follows the
  existing flag rules (FLAG-CASH, Section 4).
- **No screening data.** Gate 0 (stage 1) extracts from the results PDFs
  and the annual report financial statements.
- **No prospectus.** For a company listed within ~3 years, this is a HIGH
  gap (see RECENTLY-LISTED PRIORITY above): stages 2 and 3 build the notes
  and backward history from the annual report alone (fewer years); the
  FTTCP backward baseline runs on the post-listing years only and says so;
  stage 8 sources promoter/group background from web search and the AR
  governance section instead of the prospectus, and flags the group-company
  map as web-derived not filing-anchored. For a long-listed company the
  prospectus is not expected and its absence is not a gap.
- **No announcements.** Stages 5, 7, and 8 lose the documented-ACTION
  record (Reg 30 acquisitions, capital raises, order wins, divestments);
  the intent-and-action cross-check runs on concall/AR evidence only and
  cannot grade recent 📄 actions. Stage 8 relies on web search for material
  events. Note: FTTCP Step 0C already lists recent exchange announcements as
  a required input; its absence lowers confidence and is flagged.
- **No shareholding pattern.** Stage 10 marks FII+DII `unresolved`; stage 11
  cannot affirm the UA institutional-absence qualifier, so UA is withheld
  (the all-three-qualifier rule). Promoter holding/pledge trend falls back
  to the AR/last-known figure with the staleness noted.
- **No research.** No effect on anchored evidence (research is never
  anchored). The intent-and-action cross-check and synthesis lose a
  lead-generation and management-intent cross-check source only.

Verifiers audit only against sources that exist. Skipped stages never
fail the confidence delta; their absence flows to the synthesis instead
of counting as a verification miss. Research and prospectus/announcement
provenance rules: research notes are leads, never anchored figures;
prospectus and announcement facts ARE anchored evidence (they are filings)
and every number taken from them still carries its source anchor.

### REFRESH RUNS

When `manifest.yaml` sets `run_type: refresh`, stage 0 locates the most
recent prior run folder for the same ticker under `runs/` (the highest
`<ticker>-<YYYY-MM-DD>` date preceding this run) and passes its
`outputs/blocks/` and, if present, `outputs/final/fttcp-deliberation.md`
to every stage as **PRIOR RUN CONTEXT**. If no prior run folder exists,
the run proceeds as a normal `full` run and `B00.input_gaps` notes that no
prior run was found.

Stages must explicitly compare against the prior run where relevant:

- **Gate 0 (stage 1)** notes score movements per block (A..E, moat, grand)
  against the prior `B01-gate0`, naming the direction and cause of each
  material change.
- **Emerging Moat scan (stage 7)** notes which catalysts from the prior
  `B07-emoat.catalysts_12m[]` **fired, slipped, or died** since the prior
  run, each anchored.
- **Concall Analysis (stage 5)** checks the prior run's `B05-concall`
  guidance against the new period's delivery, anchored to the new results
  and transcripts.
- **Synthesis (stage 13)** adds a **WHAT CHANGED** section listing every
  material delta versus the prior run, each with an anchor.

Prior operator overrides from the deliberation record
(`fttcp-deliberation.md`) are surfaced, not silently inherited: synthesis
lists each prior override with the question "does the new evidence still
support this override?" and leaves the answer to Keerti.

---

## 2. STAGE SEQUENCE

| # | Stage | Prompt file | Model | Consumes | Emits block |
|---|-------|-------------|-------|----------|-------------|
| 0 | Input validation | (inline) | Haiku 4.5 | folder + manifest | `B00-inputs` |
| 1 | Gate 0 scorecard | 01-gate-0-pipeline.md | Sonnet 5 | screener-data / results PDFs | `B01-gate0` |
| 2 | Notes triple-pass | 02-notes-triple-pass-pipeline.md (3 calls) | Sonnet 5 | AR | `B02-notes` |
| 3 | AR Deep Dive | 03-ar-deep-dive-pipeline.md | Sonnet 5 | AR + B02 | `B03-ardeep` |
| 4 | Business Model Decoder | 04-business-model-pipeline.md | Sonnet 5 | AR + inv. pres. | `B04-bizmodel` |
| 5 | Concall Analysis (main) | 05-concall-pipeline.md | Sonnet 5 | 3 transcripts (oldest first) | `B05-concall` |
| 6 | Peer concall verification | 06-peer-concall-pipeline.md | Sonnet 5 | 12 peer transcripts + B05.peer_questions | `B06-peers` |
| 7 | Emerging Moat scan | 07-emerging-moat-pipeline.md | Sonnet 5 | AR + concalls + pres. + B01 | `B07-emoat` |
| 8 | Promoter check | 08-promoter-pipeline.md | Sonnet 5 + web search | web + AR governance | `B08-promoter` |
| 9 | TAM/SAM/SOM | 09-tam-pipeline.md | Sonnet 5 + web search | web + AR + B04 | `B09-tam` |
| 10 | Valuation input assembly | 10-input-assembly-pipeline.md | Haiku 4.5 | B01..B09 + results PDFs | `B10-valinputs` |
| 11 | Role 1 valuation (v3.6) | 11-valuation-pipeline.md | Opus 4.8 | B10 + Master Prompt v3.6 + Section 1B layers + FTTCP v2.1 | `B11-valuation` |
| 12a | Verifier A: numerical | verifier-a-numerical.md | Haiku 4.5 | all source PDFs + all reports | `B12a` |
| 12b | Verifier B: concall red flags | verifier-b-redflags.md | Opus 4.8 | 15 transcripts + B05 + B06 | `B12b` |
| 12c | Verifier C: framework adherence | verifier-c-framework.md | Opus 4.8 | B01, B07, B11 + framework docs | `B12c` |
| 12d | Verifier D: peer coverage | verifier-d-peers.md | Sonnet 5 | peer transcripts + B06 | `B12d` |
| 13 | Synthesis | 13-synthesis-pipeline.md | Opus 4.8 | everything | final outputs |

Stages 1 and 2 may run in parallel. Stages 4, 5, 8, 9 may run in parallel
after stage 3. Stage 6 requires stage 5. Stage 7 requires stage 1. Stages
12a-12d run in parallel after stage 11. Stage 13 requires all.

Chronology rule for stage 5: transcripts are passed oldest first and each
call is prefixed with an ordered list mapping filename to quarter. The stage
prompt anchors every promise/delivery pair to named quarters.

---

## 3. HANDOFF BLOCK SCHEMA

Every stage ends its output with a fenced YAML block. The orchestrator
extracts it to `outputs/blocks/`. Prose above the block is the full report
for `outputs/reports/`. The block is the handoff downstream stages read; the
prose report is the archive and Verifier A's source-fidelity audit target
(it must stay complete and anchored, never stripped). Reader-facing narrative
is written once, at stage 13, not at every stage. Common fields on every
block:

```yaml
stage: B01-gate0
company: GEMAROMA
run_date: 2026-07-09
model: claude-sonnet-5
status: complete          # complete | partial | failed
input_gaps: []            # carried forward from B00
flags: []                 # list of flag objects, see Section 4
analyst_note: ""          # optional, <=200 words (strict cap, excess
                          # truncated). Reasoning a downstream stage cannot
                          # reconstruct from the structured fields alone: why
                          # a flagged number matters, not just the number.
                          # Blank if nothing would otherwise be lost.
```

Stage-specific payload fields (the fields downstream stages actually read):

- `B01-gate0`: core_score /100, moat_score /60, grand /160, blocks A..E,
  moats_confirmed /12, classification, deal_breakers[], data_years,
  history_downgrade (bool)
- `B02-notes`: accounting_quality /10, top_findings[] (max 15, each with
  note_ref and rating), red_flags[], questions_for_mgmt[]
- `B03-ardeep`: phase_verdicts{1..7}, overall_quality /10, kill_switch_notes[]
  (informational only, never halts), monitorables[]
- `B04-bizmodel`: business_type, revenue_streams[], wc_intensity,
  pricing_power, valuation_methods{primary, secondary, tertiary},
  irrelevant_ratios[], must_track_metrics[]
- `B05-concall`: triggers[] (each: name, type, timeframe, conviction,
  confirm_signal, kill_signal), guidance[], promise_delivery_score,
  credibility_grade (A/B/C/D), repeated_evasions[], peer_questions[]
- `B06-peers`: verified[], contradicted[], unverifiable[], peer_coverage_map
  (per peer: substantive | cited-only | unused)
- `B07-emoat`: em_score, em_classification, active_categories[],
  evidence_mix{documented, claim, inference}, catalysts_12m[],
  combined_assessment (with B01)
- `B08-promoter`: verdict (EXEMPLARY/TRUSTWORTHY/CAUTION/CONCERN/AVOID),
  deal_breakers[], transition_evidence[] (new mgmt, institutional entry,
  pledge reduction; or NONE FOUND), searches_performed[], searches_skipped[]
- `B09-tam`: tam_cr, sam_cr, som_3yr_cr, som_5yr_cr, runway_class,
  som_implied_revenue_cagr, mgmt_claim_ratio
- `B10-valinputs`: the full Role 1 input table, every value with source
  anchor, unresolved[] for fields no source could fill
- `B11-valuation`: destination_pe_track1_rrm, destination_pe_track2_additive,
  hurdle_ratio, hurdle_verdict (PASS/CONDITIONAL/STOP), fair_values
  {bear, base, bull} per track, entry_range, mos_price, decision
  (BUY/WATCHLIST/AVOID), one_line_thesis, cash_multiplier_used,
  structural_or_growth, ua_applied (bool), sector_cap_used
- `B12a..d`: findings[] (each: severity CRITICAL/MAJOR/MINOR, location,
  description), acceptance_rate (% of upstream claims verified clean)
- Final: see Section 6

---

## 4. FLAG RULES (leniency-calibrated, per Keerti 2026-07-09)

No stage output ever halts the pipeline on company-quality grounds. Flags
propagate; they never gate. The only halt conditions are mechanical (Section 7).

**FLAG-PROMOTER.** If B08.verdict is CONCERN or AVOID, synthesis must place
this block inside the verdict line itself, not an appendix:

```
⚠️ PROMOTER FLAG: [verdict]. Top findings: [1], [2].
Transition evidence: [items from B08.transition_evidence, or NONE FOUND].
```

FTTCP go/no-go remains whatever the analysis supports. The flag is
unmissable; the decision is Keerti's.

**FLAG-CASH.** If cash conversion is deteriorating (B01 Block B trend, B02
receivables findings, or B11 cash multiplier at 0.80x or below), synthesis
must make an explicit determination with citations:

```
⚠️ CASH CONVERSION FLAG: [metric and direction].
Determination: STRUCTURAL / GROWTH-INDUCED / INDETERMINATE.
Evidence: [rating rationale quote ref, capex commissioning timeline,
receivables composition, as available].
If GROWTH-INDUCED: PROCEED permitted; attach the single quarterly metric
that would falsify the determination (e.g., "debtor days above X in Q1
FY27 print").
If STRUCTURAL with no catalyst: recommend against PROCEED, state why.
If INDETERMINATE: verdict caps at PROCEED WITH CAVEATS; name the missing
evidence (usually rating rationale detail or receivables ageing).
```

INDETERMINATE never silently resolves to PROCEED. This is the
Kernex/Tipco/Rappid/Ind Swift guard.

**FLAG-GATE0.** Gate 0 AVERAGE or deal-breaker overrides do not cap
anything. The flag records why the backward score is low and whether the
depressors are historical (post-IPO rebase, legacy cleanup, restructuring).
Position sizing logic in Role 2 already handles the override; the pipeline
only surfaces it.

**REWORK is about the analysis, not the company.** If Verifier A finds any
CRITICAL numerical finding (fabricated or materially misread figure), or any
verifier's acceptance_rate falls below 60%, the synthesis verdict is REWORK
regardless of company quality: the analysis cannot be trusted. This gate
stays hard because it judges the pipeline, not the stock.

**SOURCE FIDELITY IS A HARD, NON-OVERRIDABLE GATE.** Verifier A (Haiku) is the
sole final authority on whether a number exists in the source. No downstream
step may clear, downgrade, or reason around a Verifier A source-fidelity
finding (any B12a finding with `source_fidelity: true` — MISMATCH, ANCHOR NOT
FOUND, or material UNANCHORED). A flagged number may not enter any downstream
computation, verdict card, or Notion save as if valid: it is corrected against
the source with the correct anchor shown, or removed. A MISMATCH on a
verdict-card or Section 1B pillar input still forces REWORK per the rule above.
Verifier C's re-derivations and the synthesis narrative are SUBORDINATE to
Verifier A on the existence-of-a-number question; they own judgment and
framework, never source fidelity. The only thing that clears a source-fidelity
flag is re-reading the source PDF and showing the number does exist at a
correct anchor, and that clearance is logged as a disagreement (below). The
cross-family placement is the point: Haiku is the only out-of-family read on
the numbers, so it is the one that binds.

**LOG EVERY VERIFIER DISAGREEMENT (from day one).** A disagreement is any point
where a downstream step's conclusion conflicts with a Verifier A source-fidelity
finding: a Verifier C re-derivation that relied on a flagged number, a synthesis
inclination to keep a figure Verifier A flagged, or a source re-check that
CLEARED a Verifier A flag. Collect every one into a disagreement set. It is NOT
a REWORK trigger by itself; it is the standing evidence that, over months, shows
whether Haiku catches what the Opus verifiers miss or whether the disagreements
are noise. Synthesis writes the set to `outputs/final/verifier-disagreement-log.md`
and the Notion save appends each row to the "Verifier Disagreement Log" page.
One row per disagreement, fixed shape:

```
| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor |
  Downstream step + its position | Disposition | Note |
```
Disposition is one of: GATE HELD — figure corrected at source (correct anchor
shown) | GATE HELD — figure removed | GATE HELD — forced REWORK | FLAG CLEARED
— source re-check found the number at a correct anchor (record who re-checked).
Never resolve a disagreement silently; if there are none this run, write "none".

---

## 5. CONFIDENCE DELTA

Before synthesis, the orchestrator computes from B12a-d:

```
confidence_delta:
  numerical_acceptance: %      # from B12a
  redflag_coverage: %          # B12b: share of verifier-found flags already caught upstream
  framework_adherence: %       # B12c
  peer_utilisation: %          # B12d: peers used substantively / peers provided
  overall: min of the four
```

Interpretation bands for synthesis: overall ≥ 90 high confidence; 75-89
normal, note specifics; 60-74 PROCEED verdicts downgrade one level; < 60
forced REWORK.

---

## 6. SYNTHESIS OUTPUTS (stage 13)

Four files in `outputs/final/`:

1. `business-narrative.md`: 10 to 12 lines, plain English, Keerti's written
   voice per anti-ai-writing-style.md (no em-dashes, no AI vocabulary,
   numbers first, symmetric bull-bear, no landing lines). Opens with the
   6-7 word ultra-short headline.
2. `fttcp-recommendation.md`: verdict from the set
   {PROCEED, PROCEED WITH CAVEATS, PROCEED WITH FLAGS, REWORK,
   INSUFFICIENT EVIDENCE}, with all applicable flag blocks inline, the
   confidence delta table, and the falsification metric for any
   GROWTH-INDUCED determination. No STOP verdict exists.
3. `verifier-summary.md`: all four verifier findings tables, sorted by
   severity, each finding with location anchor.
4. `fttcp-handoff.md`: the self-sufficient input package for manual FTTCP
   v1.2 deliberation in a separate Opus session with no source PDFs. The
   four transition data series, catalyst inventory, all flags with full
   underlying findings, credibility grade with the guidance-vs-delivery
   table, the scorecards and market sizing, valuation pillar detail from
   both tracks if stage 11 ran, and a gaps ledger. Density over brevity;
   every figure carries its source anchor.

Plus one Notion save to COMPANIES MASTER (data_source_id
345bb2b9-d3ab-8032-9b46-000ba16ab827) per Notion_Save_Instructions.docx:
fetch live page first if the company exists; never overwrite Decision
Status from a pipeline run; append the run summary and link the Drive
folder.

---

## 7. MECHANICAL HALT AND RETRY RULES

- Stage returns malformed or missing YAML block: one retry with the
  addendum "Your previous output omitted or malformed the required YAML
  handoff block. Re-emit the complete output ending with the block."
  Second failure: run halts, stage named.
- API error / timeout: 3 retries, exponential backoff (30s, 120s, 480s).
- stop_reason refusal: log, retry once on Opus 4.8, then halt with reason.
- Web-search stages (8, 9): if search quota or tool errors force skips,
  stage completes with searches_skipped[] populated; B08/B09 status =
  partial; synthesis must mention partial status in the verdict block.
- Cost circuit breaker: if cumulative run cost exceeds 2.5x the estimate
  in Section 8, halt before the next stage and report per-stage spend.

---

## 8. CACHING LAYOUT AND COST

Every stage prompt is ordered: [framework and rules, stable] then
[company inputs, variable]. Stable prefixes are marked for prompt caching.
Across a 20-run month the framework text (Gate 0 tables, Section 1B, the
22-category moat scan, FTTCP v2.1) is paid once and read at 10% thereafter.

Per-run estimate at July 2026 prices (Sonnet 5 $2/$10 intro, Opus 4.8
$5/$25, Haiku 4.5 $1/$5): $11-12 first run, $8-9 cached steady state,
roughly ₹700-1,000. Web search adds ~$0.30-0.60 on stages 8-9.

---

## 9. WHAT THE ORCHESTRATOR NEVER DOES

- JIT context is law: task messages carry file PATHS and small YAML blocks
  only, never document contents; subagents read sources themselves. Curated
  tables (B10) exist so downstream stages consume summaries, not archives.
- Never lets any stage assume a number from conversation memory: stage 10
  is the only assembler of valuation inputs, and it must anchor every value.
- Never lets any exit PE enter from outside the Section 1B layer set (v3.3
  Amendments + v3.5.1 + v3.6; v3.6 governs overlaps).
- Never conflates the Emerging Moat scan (stage 7) with FTTCP: FTTCP runs
  inside stage 11's framework inputs as final synthesis, per project
  taxonomy.
- Never treats low institutional ownership as a risk. UA qualifiers are
  checked in stage 11 exactly per Amendment 3 ordering:
  min(Raw × 1.25, Sector Cap).
- Never writes X posts. Publish candidates are flagged in synthesis with a
  📤 PUBLISH CANDIDATE block or the explicit line "No publish candidate
  this analysis." Drafting happens in the Dhruva Research Public project.

---

## 10. SESSION HYGIENE (prompt cache)

- Run /clear between company analyses. Never carry one company's context
  into the next; each company starts from a clean session so no prior
  company's sources, blocks, or narrative can leak into its evidence or
  bias its verdict.
- @-mention the stable project files this orchestrator session itself reads
  (the relevant prompts/ stage files, a frameworks/ doc when it must be
  cited, the active LESSONS.md) rather than issuing a mid-conversation Read:
  the @-mention attaches the file to the first message and puts it in cache
  from turn one. This applies to the orchestrator's OWN reads only.
  Per-company source documents still reach subagents as file PATHS in the
  task message, never pasted (JIT law, section 9); @-mention is not a route
  to inline a PDF into a subagent.
