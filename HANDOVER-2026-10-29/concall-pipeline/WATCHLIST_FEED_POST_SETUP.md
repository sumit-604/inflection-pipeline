# Watchlist Pulse — Discord Post Setup

## Why this exists

The Claude scheduled task `watchlist-feed-4h` can analyze PDFs but cannot post to Discord because:

1. **Discord webhooks are blocked** by the Claude sandbox HTTP proxy (returns `403 Forbidden`).
2. **wkhtmltopdf is Windows-only** — not installed in the Linux sandbox.

So the post step runs on your Windows host via `watchlist_feed_post.bat`, scheduled in Task Scheduler.

## End-to-end pipeline

| Time    | What runs                          | Where         | What it does                                                    |
|---------|------------------------------------|---------------|-----------------------------------------------------------------|
| xx:55   | `watchlist_feed_download.bat`      | Windows host  | Scrapes screener.in feed → saves PDFs to slot folder            |
| xx:00   | Claude task `watchlist-feed-4h`    | Claude sandbox| Triages PDFs, writes `analysis/feed_briefs/feed_<date>_<HHMM>.md` |
| **xx:30** | **`watchlist_feed_post.bat`**    | **Windows host**  | **Renders PDF + posts brief to Discord webhook**            |

Result: a Watchlist Pulse PDF lands in your Discord channel ~35 min after each 4-hour slot fires.

## One-time Task Scheduler setup

1. Open **Task Scheduler** (Win+R → `taskschd.msc`)
2. **Action** → **Create Basic Task**
3. Name: `Watchlist Feed Post`
4. Trigger: **Daily**, start `00:30`
5. After creating, right-click the task → **Properties** → **Triggers** tab → **Edit** the daily trigger → check **"Repeat task every"** = `4 hours`, **"for a duration of"** = `Indefinitely`. Save.
6. **Actions** tab: Program = `C:\ConcallPipeline\Daily Concall Intelligence\watchlist_feed_post.bat`
7. **General** tab: check **"Run whether user is logged on or not"** and **"Run with highest privileges"** if your other .bats use those. Match your existing setup.
8. **Settings** tab: check **"Run task as soon as possible after a scheduled start is missed"** (so a missed slot catches up).
9. Save. You'll be prompted for your Windows password.

Fire times: **00:30, 04:30, 08:30, 12:30, 16:30, 20:30** daily.

## Manual test

Open Command Prompt in the project folder and run:

```cmd
watchlist_feed_post.bat
```

Expected behavior:
- If today's newest brief already has a `Watchlist_Pulse_<date>_<HH-MM>.pdf` in the project root → logs "Already posted, skipping" and exits.
- Otherwise → renders PDF via wkhtmltopdf, posts to your `DISCORD_WEBHOOK_URL`, saves the PDF to project root, logs success.

Check `watchlist_feed_post.log` for the result.

## Dedup behavior

The .bat is **idempotent**. It checks for `Watchlist_Pulse_<date>_<HH-MM>.pdf` in the project root before posting:
- If the PDF exists → skip silently (treated as already posted).
- If you want to force a re-post, just delete the PDF first.

This means it's safe to:
- Run the .bat manually after editing a brief (delete the PDF first to force re-post)
- Have it fire on a missed-slot catchup without spamming Discord
- Run it more frequently than every 4 hours (e.g. hourly) — it will only post when something new is available

## Troubleshooting

**"wkhtmltopdf not found"** → install via `winget install --id wkhtmltopdf.wkhtmltopdf -e` or set `WKHTMLTOPDF_PATH` in `.env` to the actual install path.

**"No brief found for <date>"** → Claude task hasn't written the brief yet. Wait until xx:15 and re-run.

**"POST FAILED — exit code N"** → check Discord webhook URL in `.env`. Test with: `curl -X POST -H "Content-Type: application/json" -d "{\"content\":\"test\"}" %DISCORD_WEBHOOK_URL%`

**Discord shows duplicate posts** → two scheduled triggers may be configured. Verify only one "Watchlist Feed Post" task exists.

## What didn't change

- `watchlist_feed_download.bat` — unchanged
- `post_feed_to_discord.py` — unchanged
- `.env` — unchanged (still reads `DISCORD_WEBHOOK_URL`)
- Claude task `watchlist-feed-4h` SKILL.md — unchanged. Its Step 7 (post to Discord) will continue to fail silently in the sandbox; the Windows .bat picks up the slack. No conflict because the .bat dedup skips anything already-posted.
