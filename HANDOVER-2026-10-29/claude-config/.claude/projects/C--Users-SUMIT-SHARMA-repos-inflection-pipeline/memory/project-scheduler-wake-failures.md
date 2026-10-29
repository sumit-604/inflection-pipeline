---
name: project-scheduler-wake-failures
description: Why Windows scheduled jobs fail after a long sleep/travel; timezone auto-flip to UTC-4 and stop-on-battery kills (seen 2026-10-28)
metadata:
  node_type: memory
  type: project
  originSessionId: 95b3fe2d-b545-4a8d-86ad-ee58c7b49372
  modified: 2026-10-28T01:00:00.841Z
---

Seen 2026-10-28 after the operator's flight (26 Oct 21:00 IST to 28 Oct 05:50 IST):

- Windows auto time zone flips the laptop between IST and "SA Western Standard Time" (UTC-4). Kernel-General event 22 logged 7 flips 25-28 Oct. Some triggers carry an explicit -04:00 offset (Chartink collector 11:30-04:00 = 21:00 IST), others are bare local times (TradeShare 07:00, Concall Newsletter, Concall Discord Evening), so those drift 9.5 h whenever the zone is wrong. Scripts using datetime.now() also pick the wrong date (Chartink brief header said "written 2026-10-27").
- Most tasks have StopIfGoingOnBatteries=True. A power-source change at wake (Kernel-Power 105) killed the catch-up runs with 0x8007042B; Chartink wrote 1 of 34 files. Fix is just to re-run on mains.
- Every catch-up fires at once at wake, so the brief / review read data before the collector / fetch finishes (see [[project-chartink-breadth-pipeline]] missed-night race).
- Cloud routines (Tracker check, AI trade check) run regardless; check with RemoteTrigger list_runs.
- Cloud routines for morning/evening concall and announcement analysis are all disabled; the analysis\*.md briefs that post_to_discord.py needs had no 27 Oct files.

**How to apply:** after any trip or long sleep, check the zone first (Get-TimeZone), then task LastTaskResult for 0x8007042B, then re-run in order: collector -> brief; morning download -> evening download (never both at once, they share the Screener login).
