# Model routing proposal, October 2026

Date: 2026-10-03. Report only. No agent file is edited until the operator rules.

## Basis

- Current model and effort come from each `.claude/agents/*.md` frontmatter on main at `c3bf379` (PR #176 moved the family to 5.5).
- Effort defaults when a file sets none: Sonnet 5.5 runs at `high`, Opus 5.5 at `medium`. Every Opus agent file sets `effort: high` explicitly, so none runs at the Opus default. Haiku 4.5 takes no effort setting.
- List prices per million tokens, input/output: Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 4.5 $1/$5. Opus and Sonnet charge the same $0.20 for cache reads. A Sonnet-to-Opus move therefore doubles every token class except cache reads.
- Token figures come from the 14 run ledgers `runs/*/session-cost.md` (266 stage rows, July to September 2026). "Median" is the median over runs of a stage's first, non-void run. "Latest" is the most recent run that has the stage. No ledger splits input from output or cache-read tokens (every in_tok and out_tok cell is blank), so savings are ranges, not measurements.
- Phase 3 stages (10, 11, 14, 15, Verifier C valuation half) have one measured run each: ENTERO 2026-07-27, on Opus 4.8 and Haiku 4.5.
- Quarterly agents A1 to A5 have no ledger in any of the 13 quarterly run folders. Their rows say "not measured".
- Model and effort are set per agent file only. No row asks for a model or effort change inside a running session. Sessions that run commands inline (stage 0, `/fttcp`) take their model and effort at session start.

## Effort assumptions behind the estimates (unmeasured, to be confirmed by the token meter)

- `high` to `medium` on a Sonnet 5.5 extraction or assembly stage: 10% to 25% fewer tokens (fewer tool calls and less thinking).
- `high` to `xhigh` on an Opus 5.5 judgment stage: 15% to 35% more tokens.
- `high` to `low` on a pure extraction stage: 15% to 35% fewer tokens.
- A model move changes the price per token, not the token count.

## Routing table

| Stage | Agent file | Current model / effort | Proposed model / effort | Reason | Last measured tokens | Estimated saving per run |
|---|---|---|---|---|---|---|
| 0 Input validation | none (inline) | orchestrator session model | no change | Runs inline by design. The ledger and close-out text that call it a haiku stage are audit item CMD-RP-01. | not ledgered (inline) | 0 |
| 1 Gate 0 scorecard | stage-01-gate0 | Sonnet 5.5 / high (default) | Sonnet 5.5 / medium | Table-driven extraction and scoring. Verifier A checks the numbers, Verifier C checks the framework. | median 134,317; latest SYNGENE 134,317 | 13k to 34k tokens |
| 2 Notes triple-pass (3 calls) | stage-02-notes-pass | Sonnet 5.5 / high | **Opus 5.5 / high** | Forensic accounting (session default). Biggest Phase 1 stage. RULING. | median 180,039 per pass; 460,610 per run (all passes); latest SYNGENE 483,401 | 0 tokens; cost up, about 2x on non-cache tokens |
| 3 AR backward deep dive | stage-03-ardeep | Sonnet 5.5 / high | **Opus 5.5 / high** | Forensic accounting (default). RULING. | median 250,525; latest SYNGENE 268,914 | 0 tokens; cost up |
| 4 Business model decoder | stage-04-bizmodel | Sonnet 5.5 / high | Sonnet 5.5 / medium | Structured decode of filed disclosures. Its output feeds Halt 1, where the operator reads it. | median 164,103; latest SYNGENE 159,864 | 16k to 41k tokens |
| 5 Concall analysis | stage-05-concall | Sonnet 5.5 / high | **Opus 5.5 / high** | Concall credibility (default). Verifier B on Opus already re-audits red flags. RULING. | median 151,024; latest SYNGENE 155,072 | 0 tokens; cost up |
| 6 Peer concall verification | stage-06-peers | Sonnet 5.5 / high | Sonnet 5.5 / medium | Checks B05 claims against peer transcripts. Verifier D audits it. | median 183,002; latest SYNGENE 184,349 | 18k to 46k tokens |
| 7 Emerging moat scan | stage-07-emoat | Sonnet 5.5 / high | no change | 22-category judgment scan. Not mechanical, not on the Opus list. Keep the Sonnet default. | median 155,518; latest SYNGENE 148,077 | 0 |
| 8 Promoter check | stage-08-promoter | Sonnet 5.5 / high | **Opus 5.5 / high** | Promoter checks (default). Web-dependent: see audit item PR-01. RULING. | median 164,724; latest SYNGENE 235,906 | 0 tokens; cost up |
| 9 TAM SAM SOM | stage-09-tam | Sonnet 5.5 / high | no change | Web sizing with judgment. Keep the Sonnet default. | median 147,547; latest SYNGENE 169,656 | 0 |
| 09b Halt 1 dossier | stage-09b-dossier | Sonnet 5.5 / high | Sonnet 5.5 / medium | Assembly from committed blocks, plus two scoped prose sections. | median 186,614; latest SYNGENE 176,696 | 19k to 47k tokens |
| 10 Valuation input assembly | stage-10-assembly | Haiku 4.5 | no change (deviates from default) | Copy and anchor only. Haiku is the cheapest model, and Verifier A rechecks every number. Moving to Sonnet low would double its price for no quality the stage needs. | 66,061 (ENTERO, only run) | 0 |
| 11 Role 1 valuation | stage-11-valuation | Opus 5.5 / high | **Opus 5.5 / xhigh** | Role 1 valuation (default). RULING. | 140,280 (ENTERO, Opus 4.8) | adds 21k to 49k tokens |
| 13 Synthesis | stage-13-synthesis | Opus 5.5 / high | no change | Final narrative and verdict card. High is enough for writing from verified blocks. | median 100,486 (lite); latest SYNGENE 205,997; finalize 135,519 (ENTERO) | 0 |
| 14 Role 2 thesis | stage-14-thesis | Opus 5.5 / high | no change | Not on the xhigh list. | 102,055 (ENTERO) | 0 |
| 15 Role 3 devil's advocate | stage-15-devil | Opus 5.5 / high | **Opus 5.5 / xhigh** | Role 3 (default). RULING. | 122,272 (ENTERO) | adds 18k to 43k tokens |
| 12a Verifier A numerical | verifier-a-numerical | Haiku 4.5 | **Sonnet 5.5 / low** | Source fidelity (default). Hard gate on fabricated numbers. Haiku 4.5 is the prior generation with no effort control. RULING. | median 98,032; latest SYNGENE 80,190 (run 2: 100,853) | 0 to 11k tokens; cost up about 2x on 112k tokens |
| 12b Verifier B red flags | verifier-b-redflags | Opus 5.5 / high | **Opus 5.5 / xhigh** | Verifier B (default). RULING. | median 163,223; latest SYNGENE 315,616 | adds 24k to 57k tokens |
| 12c Verifier C framework | verifier-c-framework | Opus 5.5 / high | **Opus 5.5 / xhigh** | Verifier C (default). Runs twice per company (Phase 1 half, Phase 3 half). RULING. | median 84,302 (Phase 1); latest SYNGENE 125,408; valuation half 94,852 (ENTERO) | adds 27k to 63k tokens over both halves |
| 12d Verifier D peers | verifier-d-peers | Sonnet 5.5 / high | Sonnet 5.5 / medium | Coverage audit against a list. RULING (verifier). | median 160,370; latest SYNGENE 137,859 | 16k to 40k tokens |
| Q-A1 extractor | quarterly-a1-extractor | Sonnet 5.5 / high | Sonnet 5.5 / low | Mechanical page extraction with page-coverage proof. | not measured | 15% to 35% of the stage |
| Q-A2 enumerator | quarterly-a2-enumerator | Sonnet 5.5 / high | Sonnet 5.5 / medium | Enumeration with a count test. | not measured | 10% to 25% of the stage |
| Q-A3 forensics | quarterly-a3-forensics | Opus 5.5 / high | no change | Forensic notes checklist. Already matches the default. | not measured | 0 |
| Q-A4 analyst | quarterly-a4-analyst | Opus 5.5 / high | no change | Role 4 and Role 5 analysis. | not measured | 0 |
| Q-A5 adversary | quarterly-a5-adversary | Opus 5.5 / high | **Opus 5.5 / xhigh** | Adversarial audit, the quarterly analogue of Role 3. RULING. | not measured | adds 15% to 35% of the stage |
| /fttcp deliberation | command, runs in the session | session model; the command pins `model: claude-opus-5-5`, no effort | start the session on Opus 5.5 at xhigh; delete the command's `model:` line | FTTCP deliberation (default). A command-level model line switches the session model mid-session when the two differ (audit LEAD-01). RULING. | not ledgered (inline) | n/a |
| /run-pipeline, /finalize, /step1 orchestrator | session | session model, chosen at start | Opus 5.5 / high at session start | Dispatch and gate logic. The heavy work runs in subagents at their own settings. | not ledgered | n/a |

## Per-run effect (Phase 1 measured medians, 2.61M tokens over the stages above)

The cost index weights tokens by list price (Sonnet = 1, Opus = 2, Haiku = 0.5). It ignores the equal cache-read price, so it overstates any Sonnet-to-Opus increase.

| Package | Phase 1 token change | Phase 1 cost-index change |
|---|---|---|
| Effort changes only (medium on 1, 4, 6, 09b, D; xhigh on B, C) | 4k to 189k fewer (0% to 7%) | 5% lower to 3% higher |
| Effort changes plus Verifier A to Sonnet low | 4k to 200k fewer (0% to 8%) | 4% lower to 5% higher |
| Full session defaults (also stages 2, 3, 5, 8 to Opus high) | 4k to 200k fewer (0% to 8%) | 33% to 42% higher |
| Phase 3 xhigh on stages 11, 15 and Verifier C valuation half | 54k to 125k more (8% to 19% of 661k) | up by the same share |

Plain reading: the defaults are a quality move, not a saving. Effort tuning alone saves at most about 7% of Phase 1 tokens. Moving the four forensic stages to Opus raises Phase 1 cost by about a third.

## Larger saving outside routing (measured)

The ledgers show re-runs cost more than any routing change saves:

- SYNGENE 2026-09-15: one correction cycle re-ran stages 1, 5, 6, 7 and all four verifiers. That cost about 1.6M tokens, 35% of the 4.58M run. One void pass added 104k when another session switched the shared checkout.
- TAALTECH 2026-09-10: 150k tokens lost to one void pass (shared checkout) and one Verifier A run on a wrong path.

Worktree isolation per run addresses the shared-checkout loss (LESSONS_ARCHIVE.md, TAALTECH entry, notes that `git worktree add` needs an operator permission). Absolute verifier paths address the wrong-path run. The token meter mod (`/stage-cost`) lets the next run measure the effort assumptions above instead of guessing them.
