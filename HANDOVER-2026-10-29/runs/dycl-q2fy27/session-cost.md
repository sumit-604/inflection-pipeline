# Session cost: DYCL Q2 FY27 quarterly review (/run-quarterly, 29 Oct 2026)

## Document review summary row (shared baseline)

`ticker | date | doctype | pages | a1_extracted_text_tok | total_run_tok | loop_iterations`

`DYCL | 2026-10-29 | results+pressrelease+concall(ASR)+governance(A1 only) | 5+3+6 pages, 418 call lines (115 turns) | ~26,600 | 1,579,875 (excl. A5 loop 0, not recorded) | 1`

- a1_extracted_text_tok: the four A1 fulltexts at about 4 characters per token: results ~11,200 (44,683 chars); press release ~2,200 (8,811); concall ~10,100 (40,533); governance ~3,000 (12,195).
- total_run_tok: base run 1,076,143 plus correction loop 503,732. Agent tokens as reported by the harness per subagent. Orchestrator session tokens are not in this figure.
- A5 loop 0 tokens are NOT RECORDED. The orchestrator session restarted after A5 wrote its files (05:08-05:09) and before its completion notice arrived. A Knack-size A5 is about 0.38M, so the true total is likely about 1.95M.
- The press release got its own chain. It is a separate document from the results filing, not an annexure copy.
- The governance filing (BSE fine) got A1 only, by the coordinator's document note; A4 read its structured file directly.

## Per-agent ledger (base run)

| Agent | Document | Model | total_tok | Wall | Run # |
|---|---|---|---|---|---|
| A1 extractor | results | claude-sonnet-5-5 | 91,841 | 263 s | 1 |
| A1 extractor | press release | claude-sonnet-5-5 | 51,960 | 103 s | 1 |
| A1 extractor | concall (ASR) | claude-sonnet-5-5 | 71,070 | 180 s | 1 |
| A1 extractor | governance (BSE fine) | claude-sonnet-5-5 | 48,297 | 87 s | 1 |
| A2 enumerator | results | claude-sonnet-5-5 | 48,932 | 60 s | 1 |
| A2 enumerator | press release | claude-sonnet-5-5 | 41,250 | 33 s | 1 |
| A2 enumerator | concall | claude-sonnet-5-5 | 75,568 | 195 s | 1 |
| A2 enumerator | concall cost-check diagnosis (resume, one question) | claude-sonnet-5-5 | 76,754 | 9 s | 1 (resume) |
| A3 forensics | results | claude-opus-5-5 | 120,677 | 366 s | 1 |
| A3 forensics | press release | claude-opus-5-5 | 65,762 | 234 s | 1 |
| A3 forensics | concall | claude-opus-5-5 | 99,344 | 246 s | 1 |
| A4 analyst | merged | claude-opus-5-5 | 284,688 | 736 s | 1 |
| A5 adversary | audit (loop 0) | claude-opus-5-5 | NOT RECORDED | NOT RECORDED | 1 |
| **Base subtotal (recorded)** | | | **1,076,143** | **2,512 s** | |

A2 cost check: results 48,932 < 91,841 and press release 41,250 < 51,960 pass. Concall 75,568 > 71,070 (+6%) MISSED. Diagnosed before A3: A2 opened nothing under inputs/; it read the A1 fulltext about twice to grade the 33 answers. No breach. The A1 concall was cheap because the source is a small text file. The diagnosis itself cost 76,754 tokens, because a resume re-reads the agent's whole context.

## Correction loop (own rows; loop_iterations = 1)

| Agent | Scope | Model | total_tok | Wall | Iteration |
|---|---|---|---|---|---|
| A2 enumerator | press release: M3 (F-05) | claude-sonnet-5-5 | 31,236 | 17 s | loop 1 (fresh) |
| A2 enumerator | concall: M06-M10 (F-05) | claude-sonnet-5-5 | 30,618 | 23 s | loop 1 (fresh) |
| A3 forensics | six new rows only, addendum file | claude-opus-5-5 | 65,367 | 192 s | loop 1 (fresh) |
| A4 analyst | F-01..F-07, own -233 bps slip, full rewrite | claude-opus-5-5 | 161,287 | 570 s | loop 1 (fresh) |
| A5 adversary | re-audit with drift check | claude-opus-5-5 | 215,224 | 463 s | loop 1 (fresh) |
| **Loop subtotal** | | | **503,732** | **1,265 s** | |

Loop 0 findings: FACTUAL 3, MISSING 3, CONTRADICTION 1, STYLE 8. Loop 1 result: all seven closed; one new FACTUAL wording item (N-01, Z-group "year" undefined) left open under batch instruction 4, since it moves no verdict-card number. STYLE 14 logged, not looped. No verdict-card number, verdict or forward figure moved in the loop.

## Notes for the next run

- Fresh loop agents given only the gap lines cost 0.50M for the whole loop, against 1.0M for Knack's resumed loop. Fresh A4 (161k) cost 36% of Knack's resumed A4 (447k).
- Do not resume an agent to ask a one-line question. Diagnose a cost-check miss from the written files.
- A5 loop-0 wording seeded the N-01 error it then caught. A5 gap text that proposes replacement wording should mark conditions it has not verified.
