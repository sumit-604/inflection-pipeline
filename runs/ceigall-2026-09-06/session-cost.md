# SESSION COST — CEIGALL 2026-09-06 (phase 1, evidence)

Per-stage token ledger. One line per subagent run, written and committed
with its own stage. A stage that loops or retries gets one line per run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus) | — | — | — | — | ~25m | 1 |
| 1 | gate 0 scorecard | claude-sonnet-5 | default | — | — | 54,376 | 5m06s | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet-5 | default | — | — | 138,673 | 8m55s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet-5 | default | — | — | 140,165 | 11m03s | 2 |
| 2 | notes triple-pass (pass 3, final) | claude-sonnet-5 | default | — | — | 133,457 | 5m09s | 3 |
| 3 | AR deep dive (8 phases) | claude-sonnet-5 | default | — | — | 233,649 | 13m19s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | — | — | 131,038 | 7m02s | 1 |
| 5 | concall analysis (3 transcripts) | claude-sonnet-5 | default | — | — | 126,037 | 7m11s | 1 |
| 8 | promoter check (web) | claude-sonnet-5 | default | — | — | 143,350 | 10m33s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | — | — | 166,182 | 10m43s | 1 |
| 7 | emerging moat 22-cat scan | claude-sonnet-5 | default | — | — | 239,049 | 9m46s | 1 |
| 9 | TAM/SAM/SOM (web) | claude-sonnet-5 | default | — | — | 142,716 | 10m41s | 1 |
| 12a | verifier A numerical | claude-haiku-4-5 | default | — | — | 101,771 | 3m11s | 1 |
| 12c | verifier C framework (phase 1) | claude-opus-4-8 | default | — | — | 101,498 | 7m31s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | — | — | 127,194 | 8m02s | 1 |
| 12a | verifier A numerical (coverage addendum) | claude-haiku-4-5 | default | — | — | 118,845 | 6m57s | 2 |
| 12b | verifier B red flags | claude-opus-4-8 | default | — | — | 275,560 | 14m53s | 1 |
| 5 | concall analysis (4 transcripts + reconciliation) | claude-sonnet-5 | default | — | — | 183,789 | 13m54s | 2 |
| 6 | peer verification (anchors + 3 new tests) | claude-sonnet-5 | default | — | — | 229,101 | 18m42s | 2 |
| 12b | verifier B red flags (recheck) | claude-opus-4-8 | default | — | — | 275,438 | 16m53s | 2 |
| 5 | concall analysis (targeted patch) | claude-sonnet-5 | default | — | — | 251,584 | 20m33s | 3 |
| 13 | synthesis-lite (phase 1) | claude-opus-4-8 | default | — | — | 149,968 | 9m25s | 1 |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | — | — | 196,608 | 7m14s | 1 |

Stage 0 ran in the orchestrator session, not as a subagent, so it has no
subagent metadata. Its wall time is dominated by a rejected OCR attempt on
the scanned annual report (see outputs/reports/00-input-validation.md 4.1).

---

## CLOSE-OUT SUMMARY (phase 1)

Run total across every ledger row: **3,660,048 tokens** over 19 subagent runs.
Stage 0 ran in the orchestrator session and carries no subagent metadata, so
it is excluded from the total and from the ranking.

### (a) TOP FIVE BY TOKENS

Loop and retry runs are summed into one stage total for the ranking.

| Rank | Stage | Runs | Total tokens | Share of run |
|---|---|---|---|---|
| 1 | 5, concall analysis | 3 | 561,410 | 15.3% |
| 2 | 12b, verifier B red flags | 2 | 550,998 | 15.1% |
| 3 | 2, notes triple-pass | 3 | 412,295 | 11.3% |
| 4 | 6, peer verification | 2 | 395,283 | 10.8% |
| 5 | 7, emerging moat scan | 1 | 239,049 | 6.5% |

The top four are all multi-run stages. Remediation, not analysis, is the
largest single cost in this run: stages 5, 6 and verifier B together account
for 1,507,691 tokens, 41.2% of the total, and would have been roughly
617,000 tokens at one run each.

### (b) DOWNSHIFT FAILURES

**DOWNSHIFT FAILURE: stage 0 input validation.** DISPATCH routes stage 0 to
haiku. It ran on the orchestrator session model (opus). This is not a
mis-set agent file: the /run-pipeline command instructs the orchestrator to
perform stage 0 itself ("VALIDATE (stage 0, do this yourself)"), which
conflicts with the DISPATCH routing. The conflict is structural and belongs
in a prompt fix, not a per-run correction. Logged to LESSONS.md.

Verifier A ran on claude-haiku-4-5 in both runs, correctly. Stage 10
assembly does not run in phase 1.

### (c) COST SPIKES

**None.** No prior run folder exists for CEIGALL, so there is no previous
ledger to compare against. This run becomes the baseline for the 1.5x test
on the next CEIGALL run.

### (d) OPERATOR SNAPSHOT

The orchestrator cannot read the interactive cost commands. Keerti: run
`/cost` and `/usage` now and paste the cache hit ratio and the loop totals
below.

#### Operator snapshot

_(to be filled by the operator)_
