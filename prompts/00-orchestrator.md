# INFLECTION ALPHA PIPELINE ORCHESTRATOR v1.0
## Sonnet 5 Primary Pipeline with Claude Verification Layer

Replaces the Gemini (Jaimini) upstream pipeline. One model family end to end.
Valuation authority: Master Project Prompt v3.3, Section 1B v3.3 (Four-Pillar
Framework, RRM dual-track, Hurdle Ratio), FTTCP v1.2. No other exit PE source
is permitted anywhere in the pipeline.

---

## 1. INPUT CONTRACT

Run folder structure (Google Drive, mirrored to local before run):

```
/inflection-alpha-runs/<ticker>-<YYYY-MM-DD>/
  manifest.yaml
  inputs/
    annual-report-FY<XX>.pdf          (exactly 1, required)
    concall-Q<N>-FY<XX>.pdf           (exactly 3, main company, required)
    results-Q<N>-FY<XX>.pdf           (exactly 3, required)
    rating-<AGENCY>-<YYYY>.pdf        (exactly 1, required)
    screener-data.txt                 (optional but strongly recommended)
    investor-presentation.pdf         (optional)
    peer-concalls/
      <PEERTICKER>-Q<N>.pdf           (up to 12)
  outputs/                            (created by pipeline)
    blocks/                           (YAML handoff blocks, one per stage)
    reports/                          (full stage outputs)
    final/                            (narrative, verdict, verifier summary)
```

manifest.yaml schema (filled by Keerti before triggering):

```yaml
company: Gem Aromatics Ltd
ticker: GEMAROMA
cmp: 412.50            # as of run date
market_cap_cr: 1240
run_date: 2026-07-09
run_type: full         # full | refresh | valuation-only
sector_cap_row: "Specialty chemicals"   # from Section 1B cap table
notes: ""              # free text, passed to synthesis
```

Stage 0 validates this contract. Missing required files: run halts with a
named list of what is missing. Missing optional files: run proceeds, gap
recorded in every downstream handoff block under `input_gaps`.

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
| 11 | Role 1 valuation (v3.3) | 11-valuation-pipeline.md | Opus 4.8 | B10 + Master Prompt v3.3 Section 1B + FTTCP v1.2 | `B11-valuation` |
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
for `outputs/reports/`. Common fields on every block:

```yaml
stage: B01-gate0
company: GEMAROMA
run_date: 2026-07-09
model: claude-sonnet-5
status: complete          # complete | partial | failed
input_gaps: []            # carried forward from B00
flags: []                 # list of flag objects, see Section 4
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

Three files in `outputs/final/`:

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
20-category moat scan, FTTCP v1.2) is paid once and read at 10% thereafter.

Per-run estimate at July 2026 prices (Sonnet 5 $2/$10 intro, Opus 4.8
$5/$25, Haiku 4.5 $1/$5): $11-12 first run, $8-9 cached steady state,
roughly ₹700-1,000. Web search adds ~$0.30-0.60 on stages 8-9.

---

## 9. WHAT THE ORCHESTRATOR NEVER DOES

- Never lets any stage assume a number from conversation memory: stage 10
  is the only assembler of valuation inputs, and it must anchor every value.
- Never lets any exit PE enter from outside Section 1B v3.3.
- Never conflates the Emerging Moat scan (stage 7) with FTTCP: FTTCP runs
  inside stage 11's framework inputs as final synthesis, per project
  taxonomy.
- Never treats low institutional ownership as a risk. UA qualifiers are
  checked in stage 11 exactly per Amendment 3 ordering:
  min(Raw × 1.25, Sector Cap).
- Never writes X posts. Publish candidates are flagged in synthesis with a
  📤 PUBLISH CANDIDATE block or the explicit line "No publish candidate
  this analysis." Drafting happens in the Dhruva Research Public project.
