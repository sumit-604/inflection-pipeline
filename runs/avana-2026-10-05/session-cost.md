# SESSION COST LEDGER — AVANA 2026-10-05 (Phase 1, /step1 intake)

Per-stage token ledger. One line per subagent run, from the subagent result
metadata. in_tok / cache splits are written n/a where the result does not
expose them (never estimated).

| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|
| 0 | input validation (orchestrator inline) | opus 5.5 (orchestrator) | session | n/a | n/a | n/a | n/a | n/a | n/a | 1 |
| 1 | Gate 0 scorecard | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 97,189 | 237s | 1 |
| 2 | Notes triple-pass, pass 1 of 3 (partial: AR notes image-only) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 117,640 | 238s | 1 |
| pre | corpus: transcribe AR pp.2-4, 99-112 page images | sonnet 5.5 | default | n/a | n/a | n/a | n/a | 154,825 | 136s | 1 |
| pre | corpus: transcribe AR pp.113-127 + Reg 31(4) page images | sonnet 5.5 | default | n/a | n/a | n/a | n/a | 159,354 | 132s | 1 |
| 1 | Gate 0 scorecard (resumed: E4 from AR notes, M2/M5/M9 peer sheets) | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 120,750 | 94s | 2 |
| 2 | Notes triple-pass, pass 1 of 3 (resumed over transcribed notes) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 199,035 | 287s | 2 |
| 2 | Notes triple-pass, pass 2 of 3 | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 180,401 | 522s | 1 |
| 2 | Notes triple-pass, pass 3 of 3 (synthesis, B02) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 72,268 | 103s | 1 |
| 3 | AR backward deep dive | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 424,227 | 963s | 1 |
| 4 | Business model decoder | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 151,378 | 313s | 1 |
| 5 | Communication and guidance (NO-CONCALL MODE, bounded) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 118,050 | 145s | 1 |
| 8 | Promoter and governance check (web; partial) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 176,078 | 493s | 1 |
| 6 | Peer verification (2 DANISH transcripts, 2 presentations) | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 142,219 | 179s | 1 |
| 7 | Emerging moat 22-category scan | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 110,242 | 231s | 1 |
| 9 | TAM SAM SOM (web; partial) | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 116,397 | 272s | 1 |
| 12a | Verifier A numerical | sonnet 5.5 | high | n/a | n/a | n/a | n/a | 416,814 | 609s | 1 |
| 12b | Verifier B red flags | opus 5.5 | xhigh | n/a | n/a | n/a | n/a | 441,546 | 978s | 1 |
| 12c | Verifier C framework (phase 1 scope) | opus 5.5 | xhigh | n/a | n/a | n/a | n/a | 162,120 | 658s | 1 |
| 12d | Verifier D peer coverage | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 71,906 | 77s | 1 |
| 13 | Synthesis-lite (phase 1 lite, 3 final files) | opus 5.5 | high | n/a | n/a | n/a | n/a | 170,276 | 533s | 1 |
| 09b | Halt 1 understanding dossier | sonnet 5.5 | medium | n/a | n/a | n/a | n/a | 210,710 | 479s | 1 |

Note: total_tok in the table above is the subagent_tokens figure the Agent
result reports (about the final context size of the run, not the cumulative
API tokens). The exact cumulative usage, read from the session transcripts,
follows. It is the authoritative count.

## EXACT USAGE FROM TRANSCRIPTS (cumulative API tokens per agent, incl. cache reads)

Prices (orchestrator Section 8, from 02-Oct-2026): Sonnet 5.5 $2 in / $10 out,
Opus 5.5 $4 in / $20 out per MTok; cache read 0.1x input, cache write 1.25x
input. Cost is API-equivalent; the account is on a Max plan, so nothing was
billed per token.

```
orchestrator                             opus   in=      174 cr= 16,412,047 cw=  314,029 out=  72,699 tot= 16,798,949 $   9.59
Transcribe AR pages part 1               sonnet in=        8 cr=    308,196 cw=  154,142 out=   2,502 tot=    464,848 $   0.47
Stage 6 peer verification AVANA          sonnet in=       14 cr=    510,241 cw=  138,199 out=   9,224 tot=    657,678 $   0.54
Stage 8 promoter check AVANA             sonnet in=       44 cr=  2,221,341 cw=  171,782 out=  13,406 tot=  2,406,573 $   1.01
Stage 3 AR deep dive AVANA               sonnet in=       88 cr=  9,920,517 cw=  420,226 out=  57,294 tot= 10,398,125 $   3.61
Stage 2 notes pass 3 AVANA               sonnet in=        6 cr=     77,789 cw=   67,449 out=     441 tot=    145,685 $   0.19
Verifier A numerical AVANA               sonnet in=      146 cr= 17,701,369 cw=  413,721 out=  53,127 tot= 18,168,363 $   5.11
Verifier D peer coverage AVANA           sonnet in=       22 cr=    507,672 cw=   70,921 out=   5,083 tot=    583,698 $   0.33
Stage 5 no-concall comms AVANA           sonnet in=       16 cr=    524,559 cw=  114,399 out=   3,278 tot=    642,252 $   0.42
Stage 2 notes pass 2 AVANA               sonnet in=       42 cr=  2,252,876 cw=  175,555 out=  55,596 tot=  2,484,069 $   1.45
Stage 09b Halt 1 dossier AVANA           sonnet in=       60 cr=  3,632,557 cw=  208,473 out=  22,467 tot=  3,863,557 $   1.47
Verifier B red flags AVANA               opus   in=       92 cr= 11,479,776 cw=  437,676 out=  65,742 tot= 11,983,286 $   8.10
Stage 2 notes pass 1 AVANA               sonnet in=       52 cr=  2,322,087 cw=  191,823 out=  14,451 tot=  2,528,413 $   1.09
Stage 7 emerging moat AVANA              sonnet in=       24 cr=    740,280 cw=  105,939 out=  12,965 tot=    859,208 $   0.54
Synthesis-lite phase 1 AVANA             opus   in=       46 cr=  2,271,790 cw=  169,324 out=  17,475 tot=  2,458,635 $   2.11
Stage 4 business model AVANA             sonnet in=       40 cr=  1,750,684 cw=  147,698 out=  10,366 tot=  1,908,788 $   0.82
Transcribe AR pages part 2               sonnet in=       12 cr=    547,417 cw=  158,967 out=   2,889 tot=    709,285 $   0.54
Stage 9 TAM SAM SOM AVANA                sonnet in=       42 cr=  1,506,908 cw=  111,797 out=   7,763 tot=  1,626,510 $   0.66
Verifier C phase-1 scope AVANA           opus   in=       58 cr=  1,951,338 cw=  159,102 out=  42,785 tot=  2,153,283 $   2.43
Stage 1 Gate 0 AVANA                     sonnet in=       52 cr=  1,625,575 cw=  118,541 out=  17,060 tot=  1,761,228 $   0.79
---
TOTAL opus   in=370 cache_read=32,114,951 cache_write=1,080,131 out=198,701 total=33,394,153 $22.22
TOTAL sonnet in=668 cache_read=46,150,068 cache_write=2,769,632 out=287,912 total=49,208,280 $19.03
GRAND total_tokens=82,602,433 cost=$41.26
```

Orchestrator row covers this whole session up to the close-out (Step 1 intake,
corpus repair, stage 0, dispatch, close-out). Stage 1 and stage 2 pass 1 rows
include their resumed runs.

---

## SESSION CLOSE-OUT — AVANA 2026-10-05 (Phase 1 complete, Halt 1 reached)

Run total: 82,602,433 tokens (orchestrator 16,798,949; subagents 65,803,484),
API-equivalent $41.26 (about Rs 3,660 at Rs 88.79/USD). Opus $22.22, Sonnet $19.03.
95% of tokens are cache reads.

### (a) TOP FIVE BY TOKENS (subagent stages; loops and retries summed)

| Rank | Stage | Total tokens | Share of subagent total |
|---|---|---|---|
| 1 | Verifier A, numerical (sonnet 5.5) | 18,168,363 | 27.6% |
| 2 | Verifier B, red flags (opus 5.5) | 11,983,286 | 18.2% |
| 3 | Stage 3, AR deep dive | 10,398,125 | 15.8% |
| 4 | Stage 2, notes triple-pass (p1 incl. resume, p2, p3) | 5,158,167 | 7.8% |
| 5 | Stage 09b, Halt 1 dossier | 3,863,557 | 5.9% |

Pre-stage transcription of 32 image-only AR pages and the Reg 31(4) filing
cost 1,174,133 tokens ($1.01).

### (b) DOWNSHIFT FAILURES
none (Verifier A ran on its frontmatter model, Sonnet 5.5).

### (c) COST SPIKES
none (no prior AVANA run).

### (d) OPERATOR SNAPSHOT
SESSION TOTAL (/cost)

