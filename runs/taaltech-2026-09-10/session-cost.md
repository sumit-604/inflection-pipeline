# SESSION COST LEDGER — TAALTECH 2026-09-10 (Phase 1, /step1 intake)

Per-stage token ledger. One line per subagent run, written and committed with
its own stage. Loops and retries each get their own line with a run counter.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| pre | corpus: transcribe scanned results filings | sonnet | default | - | - | 150,132 | 182s | 1 |
| 0 | input validation (orchestrator inline) | opus (orchestrator) | default | - | - | - | - | 1 |
| 1 | Gate 0 scorecard | sonnet | default | - | - | 151,373 | 685s | 1 |
| 2 | Notes triple-pass, pass 1 of 3 | sonnet | default | - | - | 205,300 | 562s | 1 |
| 2 | Notes triple-pass, pass 2 of 3 (FAILED, branch switched out by a concurrent session) | sonnet | default | - | - | 106,763 | 392s | 1 |
| 2 | Notes triple-pass, pass 2 of 3 (re-run in isolated worktree) | sonnet | default | - | - | 153,066 | 625s | 2 |
| 2 | Notes triple-pass, pass 3 of 3 (synthesis) | sonnet | default | - | - | 87,142 | 269s | 1 |
| 3 | AR backward deep dive | sonnet | default | - | - | 237,484 | 669s | 1 |
| 4 | Business model decoder | sonnet | default | - | - | 83,082 | 280s | 1 |
| 5 | Communication and guidance (NO-CONCALL MODE) | sonnet | default | - | - | 140,466 | 302s | 1 |
| 8 | Promoter and governance check (web) | sonnet | default | - | - | 146,025 | 950s | 1 |
| 6 | Peer concall verification (11 transcripts, 3 peers) | sonnet | default | - | - | 278,875 | 514s | 1 |
| 7 | Emerging moat 22-category scan | sonnet | default | - | - | 119,149 | 541s | 1 |
| 9 | TAM SAM SOM (web; WebSearch 20/20 failed) | sonnet | default | - | - | 105,881 | 757s | 1 |
| 12a | Verifier A numerical (FAILED: wrong checkout, 7 false CRITICALs) | haiku | default | - | - | 43,277 | 154s | 1 |
| 12a | Verifier A numerical (re-invoked, absolute paths) | haiku | default | - | - | 108,214 | 246s | 2 |
| 12b | Verifier B red flags | opus | default | - | - | 319,065 | 1239s | 1 |
| 12c | Verifier C framework (phase 1 scope) | opus | default | - | - | 120,742 | 577s | 1 |
| 12d | Verifier D peer coverage | sonnet | default | - | - | 154,809 | 549s | 1 |
| 13 | Synthesis-lite (phase 1 lite, 4 final files) | opus | default | - | - | 181,815 | 782s | 1 |
| 09b | Halt 1 understanding dossier | sonnet | default | - | - | 191,065 | 609s | 1 |

---

## SESSION CLOSE-OUT — TAALTECH 2026-09-10 (Phase 1 complete, Halt 1 reached)

Run total across every subagent invocation: **3,083,725 tokens** over 20 runs
(18 stage/verifier runs, 2 of them re-runs after a mechanical failure, plus the
pre-stage scanned-filing transcription).

### (a) TOP FIVE BY TOKENS
Loop and retry runs are summed into one stage total for the ranking.

| Rank | Stage | Total tokens | Share of run |
|---|---|---|---|
| 1 | Stage 2, notes triple-pass (4 runs: p1, failed p2, re-run p2, p3) | 552,271 | 17.9% |
| 2 | Verifier B, red flags | 319,065 | 10.3% |
| 3 | Stage 6, peer concall verification (11 transcripts) | 278,875 | 9.0% |
| 4 | Stage 3, AR backward deep dive | 237,484 | 7.7% |
| 5 | Stage 09b, Halt 1 understanding dossier | 191,065 | 6.2% |

Stage 2 leads because the 164-page annual report is the only management-authored
document in this corpus. With no earnings call and no investor presentation, the
notes carry the whole disclosure burden and the triple pass had to work them
harder than usual.

### (b) DOWNSHIFT FAILURES
**none.** Verifier A ran on haiku, both invocations. Stage 10 assembly does not
run in phase 1. Stage 0 validation ran inline in the orchestrator session, as
run-pipeline.md step 1 requires, so it is not a dispatched mechanical stage.

### (c) COST SPIKES
**none.** No prior run exists for this ticker, so there is no 1.5x comparator.

Two re-runs cost the run 150,040 tokens and neither was a model or prompt
defect:
- Stage 2 pass 2 (106,763 tokens) failed mechanically. A concurrent Claude Code
  session checked out run/indnippon-2026-09-10 in the shared working tree and
  deleted every TAALTECH working file mid-pass. No commit was lost. The run
  moved to an isolated git worktree at .claude/worktrees/taaltech.
- Verifier A invocation 1 (43,277 tokens) resolved relative paths against the
  main checkout, reached one stale leftover file, and returned seven false
  CRITICAL ANCHOR NOT FOUND findings. Re-invoked once with absolute paths per
  the orchestrator's standing Verifier A rule. Both events are in
  outputs/final/verifier-disagreement-log.md.

### (d) OPERATOR SNAPSHOT
Keerti: run /cost and /usage now and paste the cache hit ratio and the loop
totals below. The orchestrator cannot read those interactive commands.

**Operator snapshot**

_(paste /cost and /usage output here)_
