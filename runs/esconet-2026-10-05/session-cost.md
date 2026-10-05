# Session cost: ESCONET 2026-10-05 (Phase 1, /step1 intake)

Per-stage ledger, one row per subagent run. Source: the Claude Code transcript
logs for this session (~/.claude/projects/<project>/<session>/subagents/*.jsonl),
usage summed once per API message id. in_tok = uncached input + cache_read +
cache_write. total_tok = in_tok + out_tok. wall = first to last transcript
timestamp. Stage 0 and step1 steps A-G ran inline on the orchestrator session
(claude-opus-5-5); the orchestrator total is in the close-out.

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 1 | gate0 | claude-sonnet-5-5 | medium | 1,970,182 | 1,847,698 | 122,434 | 21,164 | 1,991,346 | 5m03s | 1 |
| 2 | notes pass 1 | claude-sonnet-5-5 | default (high) | 2,181,503 | 2,002,672 | 178,793 | 21,459 | 2,202,962 | 6m36s | 1 |
| 2 | notes pass 2 | claude-sonnet-5-5 | default (high) | 4,846,167 | 4,569,529 | 276,580 | 65,949 | 4,912,116 | 14m30s | 1 |
| 2 | notes pass 3 | claude-sonnet-5-5 | default (high) | 595,481 | 509,045 | 86,418 | 2,805 | 598,286 | 2m31s | 1 |
| 3 | ardeep | claude-sonnet-5-5 | default (high) | 18,433,041 | 17,910,686 | 522,233 | 75,195 | 18,508,236 | 20m38s | 1 |
| 4 | bizmodel | claude-sonnet-5-5 | medium | 1,669,432 | 1,528,922 | 140,474 | 19,229 | 1,688,661 | 5m24s | 1 |
| 5 | concall | claude-sonnet-5-5 | default (high) | 1,854,669 | 1,669,494 | 185,145 | 20,693 | 1,875,362 | 6m35s | 1 |
| 8 | promoter (web) | claude-sonnet-5-5 | default (high) | 3,346,309 | 3,162,310 | 183,941 | 6,894 | 3,353,203 | 7m09s | 1 |
| 6 | peers | claude-sonnet-5-5 | medium | 2,053,038 | 1,757,370 | 295,644 | 17,951 | 2,070,989 | 8m25s | 1 |
| 7 | emoat | claude-sonnet-5-5 | default (high) | 4,098,711 | 3,862,573 | 236,084 | 21,986 | 4,120,697 | 8m22s | 1 |
| 9 | tam (web) | claude-sonnet-5-5 | default (high) | 1,050,847 | 928,231 | 122,588 | 14,314 | 1,065,161 | 6m00s | 1 |
| 12a | verifier A numerical | claude-sonnet-5-5 | high | 22,376,000 | 21,934,335 | 441,477 | 68,296 | 22,444,296 | 12m47s | 1 |
| 12b | verifier B red flags | claude-opus-5-5 | xhigh | 6,827,502 | 6,432,590 | 394,842 | 70,167 | 6,897,669 | 17m51s | 1 |
| 12c | verifier C (Gate 0 + EM half) | claude-opus-5-5 | xhigh | 2,797,485 | 2,601,832 | 195,601 | 60,555 | 2,858,040 | 14m05s | 1 |
| 12d | verifier D peers | claude-sonnet-5-5 | medium | 1,355,054 | 1,255,353 | 99,663 | 11,371 | 1,366,425 | 2m38s | 1 |
| 1 | gate0 (remediation) | claude-sonnet-5-5 | medium | 2,248,343 | 2,096,607 | 151,686 | 30,233 | 2,278,576 | 6m37s | 2 |
| 7 | emoat (scoped 6C-6E remediation) | claude-sonnet-5-5 | default (high) | 164,993 | 78,586 | 86,401 | 443 | 165,436 | 2m49s | 2 |
| 12a | verifier A numerical (re-audit) | claude-sonnet-5-5 | high | 5,676,630 | 5,475,260 | 201,272 | 29,122 | 5,705,752 | 7m27s | 2 |
| 12c | verifier C (Gate 0 + EM half, re-audit) | claude-opus-5-5 | xhigh | 3,378,041 | 3,174,056 | 203,933 | 43,321 | 3,421,362 | 11m27s | 2 |
| 13 | synthesis-lite | claude-opus-5-5 | high | 4,819,763 | 4,563,034 | 256,669 | 29,078 | 4,848,841 | 10m12s | 1 |
| 9b | halt1 dossier | claude-sonnet-5-5 | medium | 12,056,883 | 11,664,697 | 392,078 | 52,275 | 12,109,158 | 16m58s | 1 |

## Close-out summary (Phase 1)

Measured from the session transcript logs at close-out (usage summed once per
API message id). Two measures exist and they answer different questions:
- BILLED TOKENS: every token sent to and from the model, summed over every API
  call. Each call re-sends the cached context, so a stage with many tool calls
  re-reads the same context many times. This is the ledger above.
- HARNESS TOKENS: the single figure the Agent tool returns per subagent (the
  measure the KWICK ledger used). It tracks context size, not calls x context.

### Totals

| scope | API calls | uncached in | cache read | cache write | output | billed total |
|---|---|---|---|---|---|---|
| 21 pipeline subagent runs | 619 | 1,238 | 99,024,880 | 4,773,956 | 682,500 | 104,482,574 |
| orchestrator session (incl. step1 A-G, stage 0) | 108 | 220 | 25,637,317 | 442,256 | 101,129 | 26,180,922 |
| run total | 727 | 1,458 | 124,662,197 | 5,216,212 | 783,629 | 130,663,496 |

Harness-measure total, 21 subagent runs: 4,922,255 (run 1 of each stage
4,258,013; remediation runs 664,242).
Orchestrator figure is as of close-out; the final commit, push and report add a
few more calls.

### Cache use

- Pipeline subagents: 99,024,880 of 103,800,074 input tokens were cache reads
  (95.4%); 4,773,956 were cache writes (4.6%); 1,238 were uncached.
- Orchestrator: 25,637,317 of 26,079,793 input tokens were cache reads (98.3%);
  442,256 writes (1.7%); 220 uncached.
- Run: 124.7M of 130.0M input tokens read from cache (95.9%).
- Each subagent starts a fresh context, so it pays one cache write for its own
  prefix (system prompt, agent file, stage prompt, first reads), then reads it
  back on every later tool call. Stage cost therefore scales with tool calls
  times context size: verifier A run 1 (118 tool calls, 22.4M billed) and
  stage 3 (89 calls, 18.5M) lead.

### List-price equivalent (derived, not a bill)

Sonnet 5.5 $2/$10 and Opus 5.5 $4/$20 per MTok (orchestrator Section 8); cache
read priced at 0.1x input, cache write at 2x input (1-hour TTL, the upper
bound). Subagents about $55.3; orchestrator about $15.8; run about $71.1. The
operator is on a Max plan, so this is an API-equivalent figure, not a charge.
The orchestrator Section 8 estimate is $11-12 per run, so 2.5x is about $30.
This run's API-equivalent is about 2.4x that breaker line. The breaker was
not checked during the run: the ledger has no dollar column and no prior run
measured billed tokens, so the July estimate and this figure are not on the
same basis. Recorded as an open action.

### (a) Top five by tokens (billed, loop and retry runs summed)

- stage 12a (2 runs): 28,150,048 (21.5%)
- stage 3: 18,508,236 (14.2%)
- stage 9b: 12,109,158 (9.3%)
- stage 2 (3 passes): 7,713,364 (5.9%)
- stage 12b: 6,897,669 (5.3%)
Shares are of the 130,663,496 run total including the orchestrator. On the
subagent total alone (104,482,574) the shares are 26.9%, 17.7%, 11.6%, 7.4%, 6.6%.

### (b) Downshift failures

none (verifier A ran on claude-sonnet-5-5 in both runs, its frontmatter model)

### (c) Cost spikes

none (no prior ESCONET run)

### Versus KWICK 2026-10-04 (harness measure, run 1 of each stage)

| stage | ESCONET | KWICK | diff | diff % |
|---|---|---|---|---|
| 1 | 126,955 | 128,294 | -1,339 | -1% |
| 2 | 567,630 | 473,684 | +93,946 | +20% |
| 3 | 533,737 | 421,167 | +112,570 | +27% |
| 4 | 151,259 | 122,894 | +28,365 | +23% |
| 5 | 200,918 | 253,924 | -53,006 | -21% |
| 6 | 307,555 | 273,438 | +34,117 | +12% |
| 7 | 245,136 | 151,372 | +93,764 | +62% |
| 8 | 189,779 | 244,642 | -54,863 | -22% |
| 9 | 129,646 | 138,447 | -8,801 | -6% |
| 12a | 447,805 | 334,184 | +113,621 | +34% |
| 12b | 399,714 | 346,273 | +53,441 | +15% |
| 12c | 199,313 | 133,152 | +66,161 | +50% |
| 12d | 104,492 | 116,333 | -11,841 | -10% |
| 13 | 258,561 | 247,900 | +10,661 | +4% |
| 9b | 395,513 | 240,025 | +155,488 | +65% |
| total | 4,258,013 | 3,625,729 | +632,284 | +17% |

Plus 664,242 for the remediation cycle (stage 1 run 2 159,216; stage 7 run 2
90,474; 12a run 2 206,733; 12c run 2 207,819), which KWICK did not have.
Stage 5 ran in normal mode on 2 transcripts (KWICK ran no-concall mode), so
the LESSONS no-call stage 5 target is still unmeasured.

### (d) Operator snapshot

SESSION TOTAL (/cost)

