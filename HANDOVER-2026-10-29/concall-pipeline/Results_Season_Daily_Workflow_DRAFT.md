# Results-season daily workflow (DRAFT, 24-Oct-2026)

Status: draft for the operator. Nothing here is in force. Items marked **RULING NEEDED** change a framework gate. They need an operator ruling and a framework PR before any run uses them.

Basis: the Q2 FY27 batch of 23-24 Oct 2026. 11 names cost about 25.7M subagent tokens, a floor, or about 2.3M per name. Per-agent figures from that batch: A1 50k-160k per document, A2 45k-110k, A4 300k-440k, A5 270k-330k, each correction loop 0.1M-1.1M. Crashes, duplicate sessions and second loops added several million.

## 1. Daily rhythm

| Time (IST) | Step | Who | Cost |
|---|---|---|---|
| 08:30 | Morning download (existing `morning_download.bat`) | Script | None |
| 19:30 | Evening download (existing `evening_download.bat`). Most late decks and press releases are filed by then. | Script | None |
| 19:45 | Triage: one results card per watchlist name with new filings | One cheap agent | Low |
| 20:00 | Operator picks FULL, LIGHT or SKIP per name | Operator | None |
| 20:15 | Queue runs, 3 at a time | One coordinator session | See section 3 |
| Next morning | Read the combined briefs file. Approve Notion payloads. | Operator | None |

Rule: never fetch for a name before the 19:30 window. Cybertech filed its deck at 17:18 IST on 23-Oct, after the fetch, and the first review missed it.

## 2. Triage card (new, cheap)

One Sonnet agent reads only page 1-3 of each new results filing and the deck's summary slide. It writes one card per name to `Q2 FY27 Results\_triage_<date>.md`:

- Revenue, EBITDA, PAT: this quarter, a year ago, last quarter.
- One line: beat, in line or miss against the last brief or the thesis trigger in `companies/<TICKER>.md`.
- Documents held and documents still expected (deck, call date, transcript).
- A suggested tier: FULL, LIGHT or SKIP, with a one-line reason.

The card makes no forecast and no verdict. It only routes.

## 3. Three tiers

| Tier | When | Documents | Agents | Expected tokens |
|---|---|---|---|---|
| FULL | Held names. Names with a fired or near trigger. A miss on a thesis name. | Results, deck, call | Current `/run-quarterly`, A1-A5, one loop | 1.5M-2.5M (batch range) |
| LIGHT | Watchlist names with no trigger in play | Results, deck. Call only if a filed transcript exists. | A1 per document, then A4, then one A5 pass. No loop unless A5 finds a FACTUAL item that moves a headline number. **RULING NEEDED** (skips A2 and A3) | About 0.8M (A1 x2 ~0.2M + A4 ~0.3M + A5 ~0.3M, from batch figures) |
| SKIP | No change worth a read | None | Triage card only | Low |

Every FULL and LIGHT run ends with the operator brief: 10 to 12 plain points, FY27 and FY28 revenue and PAT with basis, and forward PE. The coordinator adds each brief to one daily file.

## 4. Concall handling

- Wait for the filed transcript. Most companies file within 1-3 working days. Run the call as a separate concall pass when it lands.
- Machine transcription (faster-whisper) only for FULL names whose transcript has not appeared by day 3. Run one transcription at a time on this machine.
- Mark every machine transcript as ASR. Treat its numbers as management-tier, unverified.

## 5. Running rules (from this batch)

1. One coordinator session. It starts at most 3 company sessions at a time. It starts the next only when one finishes. The 14-at-once start failed: 8 sessions never started.
2. A failed start is restarted in place, never re-created as a new session. Re-creating made duplicate threads.
3. Subagents run in the foreground. A background agent that dies sends no report. On 23-Oct a network drop left four sessions waiting for hours.
4. Stall check by full timestamp (date and time) of the newest file in the run folder. If nothing is written for 30 minutes during an agent step, restart that step.
5. One correction loop by default (Point 9). A second loop only for an A5 item tagged FACTUAL or CONTRADICTION that moves a verdict-card number. Wording and label items stay logged.
6. Fetch once, after 19:30. Check the BSE announcements page for filings after the fetch time before A4 starts.
7. Close the machine only between runs. A shutdown kills every running agent.

## 6. Daily budget guide

| Day type | Names | Mix | Expected subagent tokens |
|---|---|---|---|
| Light day | 3 | 1 FULL, 2 LIGHT | About 3.5M-4M |
| Heavy day | 8 | 2 FULL, 4 LIGHT, 2 SKIP | About 6M-8M |

These are guides from one batch, not measured limits. Track each day's actual total in the run folders' `session-cost.md` and compare after one week.

## 7. Open decisions for the operator

1. **RULING NEEDED:** approve the LIGHT tier (A2 and A3 skipped for watchlist names with no trigger).
2. Approve the 3-at-a-time cap as a standing rule.
3. Approve the narrowed second-loop rule in section 5, item 5.
4. Decide whether the triage card runs on Haiku 5.5 or Sonnet 5.5. CLAUDE.md bars Haiku from extraction stages, so Sonnet is the safe default.
5. If approved, the repo change goes as a framework PR (prompts/quarterly-00-orchestrator.md and CLAUDE.md), separate from run outputs, with `tools/dry_check.sh` run first.
