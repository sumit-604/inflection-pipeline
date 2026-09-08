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
