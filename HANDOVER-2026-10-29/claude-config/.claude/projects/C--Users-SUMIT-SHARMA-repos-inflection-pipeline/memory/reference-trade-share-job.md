---
name: reference-trade-share-job
description: "Where the morning contract-note -> Discord trade post job lives, and its known failure mode"
metadata:
  node_type: memory
  type: reference
  originSessionId: fa2f53fc-c1be-4396-ac14-af6a196938d3
  modified: 2026-10-10T02:01:34.781Z
---

Morning job that reads broker contract notes from Gmail and posts trades to Discord lives OUTSIDE this repo at `C:\Users\SUMIT SHARMA\repos\trade_share` (trade_share.py, run_trade_share.bat, output\log.txt). Run by Windows Task Scheduler tasks "TradeShare 7am" and "TradeShare 7-30 catch-up" (--catchup). It was built in a chat that is not in any Claude Code session on this machine.

Known failure (fixed 2026-09-30): emoji in the message crashed print() under cp1252; fix is `set PYTHONIOENCODING=utf-8` in the .bat. Crashes happen before emails get the "TradeShare-Done" label, so a later good run posts the missed notes. Check output\log.txt first when it misbehaves.

"Task completed but nothing on Discord" usually means the script held the post on purpose: any note that fails to parse blocks the whole post and emails "Trade log NOT posted". Second known failure (fixed 2026-10-08): Angel One note where pdfplumber split the header into its own 1-row table; fix carries the last header to a same-width headerless table (backup trade_share.py.bak-2026-10-08). Diagnose with `--dry-run --debug` (no post, no label, no email).

Third failure (fixed 2026-10-10): log said "Python was not found". On 2026-10-09 21:37 the WindowsApps python.exe alias was re-registered as the Store stub; user PATH lists WindowsApps before %LOCALAPPDATA%\Python\bin (Python install manager, real core in pythoncore-3.14-64). The .bat now calls "%LOCALAPPDATA%\Python\bin\python.exe" by full path. Trigger a test with Start-ScheduledTask "TradeShare 7am".
