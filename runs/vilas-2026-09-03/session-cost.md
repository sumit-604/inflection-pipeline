# Session cost ledger — vilas-2026-09-03 (phase 1)

Per-stage token ledger. One line per subagent run.

| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |
|---|-------|-------|--------|--------|---------|-----------|------|------|
| 0 | input validation | orchestrator (opus-4-8) | n/a | n/a | n/a | n/a | n/a | 1 |
| 2 | notes triple-pass (pass 1) | claude-sonnet | default | n/a | n/a | 282810 | 7m40s | 1 |
| 1 | gate 0 (data-gap fail, results PDFs unreadable) | claude-sonnet | default | n/a | n/a | 87982 | 10m53s | 1 |
| 2 | notes triple-pass (pass 2) | claude-sonnet | default | n/a | n/a | 294324 | 6m11s | 2 |
| 1 | gate 0 (re-run, corrected inputs) | claude-sonnet | default | n/a | n/a | 75449 | 5m52s | 2 |
| 2 | notes triple-pass (pass 3, consolidation + B02) | claude-sonnet | default | n/a | n/a | 79768 | 5m15s | 3 |
| 7 | emerging moat scan | claude-sonnet | default | n/a | n/a | 528157 | 9m41s | 1 |
| 3 | AR deep dive | claude-sonnet | default | n/a | n/a | 499439 | 11m37s | 1 |
| 4 | business model decoder | claude-sonnet | default | n/a | n/a | 523998 | 7m21s | 1 |
| 5 | concall analysis | claude-sonnet | default | n/a | n/a | 238078 | 8m30s | 1 |
| 8 | promoter check (web, partial) | claude-sonnet | default | n/a | n/a | 319465 | 12m40s | 1 |
| 6 | peer concall verification | claude-sonnet | default | n/a | n/a | 681740 | 9m43s | 1 |
| 9 | TAM/SAM/SOM | claude-sonnet | default | n/a | n/a | 394119 | 14m28s | 1 |
| 12b | verifier B redflags | claude-opus-4-8 | default | n/a | n/a | 232166 | 5m53s | 1 |
| 12c | verifier C framework (phase-1) | claude-opus-4-8 | default | n/a | n/a | 93792 | 4m41s | 1 |
| 12a | verifier A numerical (haiku, first attempt) | claude-haiku-4-5 | default | n/a | n/a | 0 | fail: prompt-too-long | 1 |
| 12a | verifier A numerical (haiku, lean re-scope) | claude-haiku-4-5 | default | n/a | n/a | 83490 | 3m12s | 2 |
| 12d | verifier D peer coverage | claude-sonnet | default | n/a | n/a | 570855 | 6m23s | 1 |
| 13 | synthesis-lite (phase 1) | claude-opus-4-8 | default | n/a | n/a | 98273 | 4m42s | 1 |
| 09b | halt-1 dossier | claude-sonnet | default | n/a | n/a | 369507 | 8m56s | 1 |

## SESSION CLOSE-OUT (phase 1)

Total tokens across ledger rows: 5,083,906.

(a) TOP FIVE BY TOKENS (stage total, share of run):
1. Stage 6  peer concall verification    681,740  (13.4%)
2. Stage 2  notes triple-pass (3 passes)  656,902  (12.9%)
3. Stage 12d verifier D peer coverage     570,855  (11.2%)
4. Stage 7  emerging moat scan            528,157  (10.4%)
5. Stage 4  business model decoder        523,998  (10.3%)

(b) DOWNSHIFT FAILURES: none. The only mechanical stage that ran as a subagent
    (verifier A) ran on Haiku 4.5 as routed. Stage 0 validation was performed by
    the orchestrator by design, not a downshifted subagent.

(c) COST SPIKES: none. No prior VILAS run exists (this is the first run for the
    ticker), so there is no baseline to compare against.

(d) OPERATOR SNAPSHOT: operator to run /cost and /usage now and paste the cache
    hit ratio and the loop totals below.

### Operator snapshot
(pending operator paste)

### Run notes
- Verifier A first attempt failed prompt-too-long on Haiku's window (large injected
  base context this session); re-run lean on Haiku against the screener dataset and
  the FY26 sidecar. Both Verifier A MAJOR source-fidelity flags cleared at source
  (verifier arithmetic slips); see outputs/final/verifier-disagreement-log.md.
- FY26 audited results PDF (16.7 MB) exceeded the Read-tool media limit; extracted
  to a pypdf text sidecar. H1 FY26 results PDF is image-only (needs OCR), unverified.
- Section 6 ran under the operator's 2026-09-03 substitution: the ten Standing
  Extraction Annex questions were answered off-session and deferred; the five
  operator priority extractions were answered from corpus instead.
