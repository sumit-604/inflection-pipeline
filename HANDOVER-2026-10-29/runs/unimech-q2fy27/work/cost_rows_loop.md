| Agent | Doc | Model | total_tok | Wall | Run # | Gate / note |
|---|---|---|---|---|---|---|
| A2 | concall (loop 1) | claude-sonnet-5-5 | 31,111 | 28.7 s | loop 1 | PASS; M1 fixed, questions 24 -> 25 (T57 Gaurav) |
| A3 | addendum deck R222 + call R244/R065 (loop 1) | claude-opus-5-5 | 97,034 | 342.3 s | loop 1 | PASS; D-A3-28 (C1), C-A3-26 (M2) |
| A4 | patch file (loop 1) | claude-opus-5-5 | 188,560 | 562.4 s | loop 1 | 34 replace patches, closes C1 M1-M5; applied by orchestrator script, all anchors unique; no verdict change |
| A5 | re-audit (loop 1) | claude-opus-5-5 | 184,368 | 543.5 s | loop 1 | COMPLETE; C1 M1-M5 CLOSED; drift PASS; 5 STYLE |
