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
