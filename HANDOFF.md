# HANDOFF — framework and housekeeping state

Read by the main session at session start. Subagents do not read it. Update it
at each milestone and before a session ends; delete an item once it is closed.
Keep it under 1,500 words. Run status lives in companies/<TICKER>.md and the
run's manifest.yaml, not here.

Last updated: 2026-10-11 (framework/oct-11-housekeeping).

## Open PRs

Framework and tools:
- #212 framework/oct-11-housekeeping: items 1-8 of the 11-Oct housekeeping
  list and three extras, all landed. Run tools/dry_check.sh, then merge.
- #185 framework/ar-section-index, DRAFT. DO NOT MERGE before a measured run;
  evaluate against runs/kwick-2026-10-04/session-cost.md first.
- #202 tools/macro-direction: monthly cross-asset direction model and backtest.
- #210 tools/macro-regime-metals: asset read rows in the Pine table; RBI source.

Run PRs (Phase 1 to Halt 1, waiting on operator Halt 1 decisions):
- #177 TRUALT 2026-09-18 · #199 IOLCP 2026-09-19 · #204 MMP 2026-10-04 ·
  #206 ESCONET 2026-10-05 · #207 SSWL 2026-09-19 · #208 ACCORD 2026-10-06 ·
  #209 SUPREMEPWR 2026-10-06.

## Pending amendments

- PR #212 (11-Oct housekeeping): complete on its branch; waits on merge.
- Section 1B skill fixes from CAPILLARY /finalize (chunk 15 A20.5 clause,
  chunk 06/08 text) and KISSHT (chunk 06 l.39/l.89, chunk 08 l.38). Own branch.
- Standing operating-ROCE rule (CAPILLARY O1): CLAUDE.md OPERATOR RULINGS and
  section-1b chunk 01. Own branch.
- OR-11 (SYNGENE): approved 2026-09-28; framework text and chunk 07 unwritten.
- KISSHT: stage 11 priced under uncommitted v3.11; merge it.
- Stage 13 Notion payload spec and stage 14 position_size "none" value
  (CAPILLARY /finalize rows 6, 8).
- Canary rewrite on `claude -p` (PR #162).

## Open operator decisions

- AVOID (Role 2 Section 7) vs WATCHLIST (Gate 0 below 60) verdict conflict,
  recurring after KISSHT and CAPILLARY.
- TAALTECH de-escalation trigger: proposed, not approved (17d3254a).
- 1B cap rows: Sugar/Agri cyclical (KCPSUGIND); Distribution commodity,
  value-added, blended (ENTERO). Both run ad hoc today.
- A14 fade guard (ENTERO); A6 range rounding; OR-9 starter size under A24/A25.
- Stage 5 to Opus 5.5 high if Verifier B overturns grades in two runs.
- Audit deferrals in audits/RULINGS_2026-10.md: items 41, 43, 45, 71, 85-88, 108.
- Verifier A shadow (item 8c): after the next Phase 1, read
  runs/<run>/shadow/verifier-a-comparison.md and rule on Haiku 5.5 for Verifier A.
- Subagent cache 1h (item 1): judge on the re-read multiple in the next
  run's session-cost.md.
- LESSONS.md is over its 1,500-token budget (about 1,710 by a chars/3.6
  estimate). Run /compost to archive old lessons.
- Verifier A tier tag: B12a findings carry no tier field, so the shadow
  comparison's input column is "?" for findings only Sonnet found. Decide
  whether Verifier A should tag tier (a prompts/12 change).

## Gotchas

- Full checkout is about 4.9 GB under runs/ and 3.8 GB of .git. Run
  tools/sparse_session.sh runs/<folder> first in a pipeline session.
- More than 100 remote branches. audits/BRANCH_AUDIT_2026-10.md lists them;
  110 branch-only markdown records should land on main in one PR before the
  71 deletes. Run audits/BRANCH_DELETIONS_2026-10.md from a local clone: the
  cloud proxy refuses remote branch deletes.
- The cloud network policy blocks screener.in. /step1 identity and the
  collector run on the operator's machine.
- An Android signing key sits in history under runs/voepl-2026-07-18. Treat it
  as exposed.
- The auto-mode permission classifier refuses edits under .claude/ as
  self-modification. Switch the session to Accept edits mode before a
  framework change there.
- .claude/shadow.yaml is armed. The next /run-pipeline flips it to spent.
- RE-COLLECT pending: KRONOX FY2024-25 AR; KOPRAN FY2024-25 and FY2025-26
  ARs; AKUMS peer PPLPHARMA Q2 FY26 transcript.
- fetch_bse_announcements untested on the live BSE API (PR #167).
