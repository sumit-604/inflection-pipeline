| agent | doc | model | total_tok | wall_s | run# |
|---|---|---|---|---|---|
| A1 | results | claude-sonnet-5-5 | 163209 | 1092 | 1 |
| A2 | results | claude-sonnet-5-5 | 79855 | 258 | 1 |
| A3 | results | claude-opus-5-5 | 214827 | 1625 | 1 |
| A1 | presentation | claude-sonnet-5-5 | 137920 | 426 | 1 (resumed after app restart; first attempt died, no output, token count not recoverable) |
| A2 | presentation | claude-sonnet-5-5 | 61115 | 154 | 1 |
| A3 | presentation | claude-opus-5-5 | 178468 | 607 | 1 |
| A1 | pressrelease | claude-sonnet-5-5 | 54098 | 147 | 1 |
| A2 | pressrelease | claude-sonnet-5-5 | 47100 | 85 | 1 |
| A3 | pressrelease | claude-opus-5-5 | 82688 (resume leg only; first leg died on network drop 18:47 IST, tokens not recoverable) | 58 | 1 (mechanical resume) |
| A1 | concall | claude-sonnet-5-5 | 106342 | 378 | 1 |
| A2 | concall | claude-sonnet-5-5 | 56483 | 104 | 1 |
| A3 | concall | claude-opus-5-5 | 149316 | 478 | 1 |
| A4 | merged | claude-opus-5-5 | 436627 | 1259 | 1 |
| A5 | audit | claude-opus-5-5 | 437973 | 1211 | 1 (INCOMPLETE: 2 FACTUAL, 6 MISSING, 2 CONTRADICTION, 11 STYLE) |
| LOOP1 A1 append | concall | claude-sonnet-5-5 | 12872 (cumulative 119214 minus base 106342) | 36 | loop 1 |
| LOOP1 A2 ledger add | concall | claude-sonnet-5-5 | 2786 (cumulative 59269 minus base 56483) | 19 | loop 1 |
| LOOP1 A3 addendum | presentation | claude-opus-5-5 | 49171 (cumulative 227639 minus base 178468) | 326 | loop 1 |
| LOOP1 A4 revise | merged | claude-opus-5-5 | 99932 (cumulative 536559 minus base 436627) | 559 | loop 1 |
| LOOP1 A5 re-audit | audit | claude-opus-5-5 | 145367 (cumulative 583340 minus base 437973) | 654 | loop 1 |
| LOOP2 A1 append | concall | claude-sonnet-5-5 | 7226 (cumulative 126440 minus 119214) | 43 | loop 2 |
| LOOP2 A2 ledger add | concall | claude-sonnet-5-5 | 4196 (cumulative 63465 minus 59269) | 19 | loop 2 |
| LOOP2 A4 revise | merged | claude-opus-5-5 | 143816 (cumulative 680375 minus 536559) | 962 | loop 2 |
| LOOP2 A5 re-audit | audit | claude-opus-5-5 | 78868 (cumulative 662208 minus 583340) | 468 | loop 2 (final: INCOMPLETE, F3 open) |
