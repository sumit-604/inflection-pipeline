| agent | doc | model | total_tok | tool_uses | wall_s | run# |
|---|---|---|---|---|---|---|
| A1 | presentation | sonnet-5-5 | 135616 | 25 | 305 | 1 |
| A1 | results | sonnet-5-5 | 132976 | 30 | 356 | 1 |
| A2 | presentation | sonnet-5-5 | 46203 | 13 | 95 | 1 |
| A2 | results | sonnet-5-5 | 85498 | 20 | 206 | 1 |
| A3 | presentation | opus-5-5 | 175251 | 10 | 442 | 1 |
| A1 | pressrelease | sonnet-5-5 | 52487 | 10 | 102 | 1 |
| A2 | pressrelease | sonnet-5-5 | 40801 | 6 | 38 | 1 |
| A3 | results | opus-5-5 | 162292 | 12 | 542 | 1 |
| A3 | pressrelease | opus-5-5 | 63460 | 7 | 209 | 1 |
| A1 | egm | sonnet-5-5 | 76408 | 12 | 145 | 1 |
| A1-addendum | presentation p17/p27 render check | sonnet-5-5 | 34255 | 5 | 30 | 1 |
| A1 | esop | sonnet-5-5 | 54211 | 15 | 113 | 1 |
| A4 | merged | opus-5-5 | 388239 | 24 | 925 | 1 |
| A5 | audit | opus-5-5 | 313262 | 34 | 1097 | 1 |

**Correction loop 1**

| agent | doc | model | total_tok | tool_uses | wall_s | run# |
|---|---|---|---|---|---|---|
| A2 (resume) | presentation | sonnet-5-5 | 65692 | 7 | 59 | loop 1 |
| A4 (resume) | merged | opus-5-5 | 479128 | 10 | 500 | loop 1 |
| A5 (resume) | loop-1 re-audit | opus-5-5 | NOT REPORTED (process restart) | | | loop 1 |
