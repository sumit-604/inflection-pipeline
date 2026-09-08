# Session cost ledger — IEX 2026-09-08 (Phase 1)

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator-inline | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes pass 1 (rerun on extracted text) | claude-sonnet-5 | default | n/a | n/a | 198,798 | 6m30s | 2 |
| 1 | gate 0 scorecard (rerun, complete sources) | claude-sonnet-5 | default | n/a | n/a | 143,957 | 9m05s | 2 |
| 2 | notes pass 2 | claude-sonnet-5 | default | n/a | n/a | 171,948 | 8m32s | 1 |
| 2 | notes pass 3 (consolidation, pass1 absent) | claude-sonnet-5 | default | n/a | n/a | 130,357 | 8m18s | 1 |
| 2 | notes pass 3 (rerun, all 3 passes present) | claude-sonnet-5 | default | n/a | n/a | 123,372 | 6m12s | 2 |
| 3 | AR backward deep dive | claude-sonnet-5 | default | n/a | n/a | 291,043 | 13m12s | 1 |
| 4 | business model decoder | claude-sonnet-5 | default | n/a | n/a | 129,636 | 8m11s | 1 |
| 5 | concall analysis (4 calls) | claude-sonnet-5 | default | n/a | n/a | 211,929 | 9m03s | 1 |
| 8 | board/KMP check (web search) | claude-sonnet-5 | default | n/a | n/a | 146,912 | 8m21s | 1 |
| 6 | peer concall verification | claude-sonnet-5 | default | n/a | n/a | 196,845 | 10m33s | 1 |
| 7 | emerging moat 22-category scan | claude-sonnet-5 | default | n/a | n/a | 132,790 | 9m50s | 1 |
| 9 | TAM/SAM/SOM (web search) | claude-sonnet-5 | default | n/a | n/a | 150,040 | 13m40s | 1 |
| 12b | verifier B concall red flags | claude-opus-4-8 | default | n/a | n/a | 242,024 | 12m02s | 1 |
| 12d | verifier D peer coverage | claude-sonnet-5 | default | n/a | n/a | 85,637 | 3m55s | 1 |
| 5 | concall analysis (REWORK) | claude-sonnet-5 | default | n/a | n/a | 227,811 | 10m44s | 2 |
| 12a | verifier A numerical audit | claude-haiku-4-5 | default | n/a | n/a | 83,719 | 4m28s | 1 |
| 12c | verifier C framework (phase 1 scope) | claude-opus-4-8 | default | n/a | n/a | 132,933 | 9m46s | 1 |
| 12b | verifier B (post-remediation) | claude-opus-4-8 | default | n/a | n/a | 253,209 | 13m01s | 2 |
| 5 | concall analysis (targeted amendment) | claude-sonnet-5 | default | n/a | n/a | 197,847 | 14m26s | 3 |
| 6 | peer verification (re-pointed) | claude-sonnet-5 | default | n/a | n/a | 166,143 | 9m28s | 2 |
| 12b | verifier B (final, post-remediation) | claude-opus-4-8 | default | n/a | n/a | 276,426 | 14m24s | 3 |
| 12d | verifier D peer coverage (rerun) | claude-sonnet-5 | default | n/a | n/a | 107,437 | 5m13s | 2 |
| 13 | synthesis-lite (3 files) | claude-opus-5 | default | n/a | n/a | 158,118 | 6m43s | 1 |
| 09b | Halt 1 understanding dossier | claude-sonnet-5 | default | n/a | n/a | 164,087 | 6m11s | 1 |

---

## SESSION CLOSE-OUT

Run total across every ledger row: **4,565,753 tokens**, 25 subagent runs.
No per-stage input/output split is available: the harness reports a single
subagent_tokens figure per run, so in_tok and out_tok are recorded n/a
throughout and total_tok is the reported figure.

### (a) Top five by tokens

| # | Stage | Runs | Total tokens | Share of run |
|---|-------|------|--------------|--------------|
| 1 | 12b verifier B, concall red flags | 3 | 771,659 | 16.9% |
| 2 | 2 notes triple-pass | 5 | 700,815 | 15.3% |
| 3 | 5 concall analysis | 3 | 637,587 | 14.0% |
| 4 | 1 Gate 0 scorecard | 2 | 510,352 | 11.2% |
| 5 | 6 peer concall verification | 2 | 362,988 | 8.0% |

The top five are 65.4% of the run. Four of the five are there because they
ran more than once. Only stage 2, at five runs, was a planned multi-pass
stage; the other three repeats were remediation.

### (b) Downshift failures

**None.** The mechanical stages DISPATCH routes to haiku are stage 0
validation, stage 10 assembly and verifier A. Stage 0 ran inline in the
orchestrator at no subagent cost. Stage 10 does not run in phase 1.
Verifier A ran on claude-haiku-4-5 as specified, at 83,719 tokens, the
cheapest subagent in the run. No mechanical stage ran on Opus.

### (c) Cost spikes

**None measurable.** This is the first run for IEX, so no prior
runs/iex-<date>/session-cost.md ledger exists to compare against. The 1.5x
test cannot be applied. Recorded so the next IEX run has a baseline.

Two observations the next run should carry, neither a spike by the rule:
- Verifier B (opus) cost 771,659 tokens across three passes, more than any
  stage. An adversarial opus verifier reading sixteen transcripts will
  out-list a single-pass sonnet stage every time, which drove two rounds of
  stage-5 rework. The strict acceptance metric moved 38, then 36, then 65.
- The PDF page-render failure cost one wasted stage-2 run (76,340 tokens)
  before the standing LESSONS.md fix was applied. Pre-extracting every input
  PDF to page-marked text should be done at stage 0, before any stage runs,
  not after the first stage fails.

### (d) Operator snapshot

Keerti: run `/cost` and `/usage` now and paste the cache hit ratio and the
loop totals below. The orchestrator cannot read those interactive commands.

#### Operator snapshot

_(paste /cost and /usage output here)_

