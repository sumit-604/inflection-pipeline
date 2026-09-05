# Session cost ledger — pittieng-2026-09-05 (phase 1)

Per-stage token ledger. One line per subagent run. Token counts are taken
from the Agent tool result metadata where the harness reports them; "n/a"
where it does not.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation + corpus audit | orchestrator (claude-fable-5-1) | n/a | n/a | n/a | n/a | ~12m | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 283170 | 8m31s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 148436 | 8m57s | 2 |
| 1 | gate 0 scorecard | claude-sonnet | default | n/a | n/a | 180950 | 18m33s | 1 |
| 2 | notes triple-pass (pass 3, consolidation + B02) | claude-sonnet | default | n/a | n/a | 80693 | 5m22s | 3 |
| 3 | AR deep dive | claude-sonnet | default | n/a | n/a | 369769 | 13m07s | 1 |
| 4 | business model decoder | claude-sonnet | default | n/a | n/a | 170183 | 11m11s | 1 |
| 8 | promoter check (web, partial: 2 fetches proxy-blocked) | claude-sonnet | default | n/a | n/a | 245445 | 11m46s | 1 |
| 5 | concall analysis | claude-sonnet | default | n/a | n/a | 163199 | 14m26s | 1 |
| 6 | peer concall verification | claude-sonnet | default | n/a | n/a | 361695 | 9m41s | 1 |
| 7 | emerging moat scan (report + B07 block complete on disk; agent cut by API 429 while returning, so token metadata lost) | claude-sonnet | default | n/a | n/a | n/a | n/a | 1 |
| 12b | verifier B red flags (FAILED: API 429 session limit after independent read) | claude-opus | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage (FAILED: API 429 session limit at launch) | claude-sonnet | default | n/a | n/a | n/a | n/a | 1 |
| 12d | verifier D peer coverage (retry) | claude-sonnet | default | n/a | n/a | 326482 | 6m04s | 2 |
| 12c | verifier C framework (phase-1 scope: Gate 0 + EM only) | claude-opus | default | n/a | n/a | 131382 | 10m37s | 1 |
