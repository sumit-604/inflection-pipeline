---
name: chartink-market-read
description: Writes the nightly Indian market breadth brief, a plain-language story with 30+ points, from the Chartink facts sheet per tools/chartink/BREADTH_BRIEF_FRAMEWORK.md.
---

Write tonight's Market Breadth Brief for Sumit Sharma.

REPO: C:\Users\SUMIT SHARMA\repos\inflection-pipeline
All paths below are relative to REPO.

STEP 1. Read the framework in full. It is the specification and it governs everything below:
  tools\chartink\BREADTH_BRIEF_FRAMEWORK.md

STEP 2. Read the facts sheet in full:
  data\chartink\analysis\facts\latest.md
Every number you use comes from this sheet. It was computed at 21:00 from the 34 Chartink table CSVs for the latest trade date. Note the trade date in its heading and the "Files present: N of 34" line.

STEP 3. Read the previous brief for voice and continuity:
  data\chartink\analysis\briefs\latest.md
Match its register: a story in plain words, numbers only where they carry the point. It is context, never evidence. What it said to watch should be checked against tonight's sheet. If it does not exist, say so in the opening note and continue.

STEP 4. If you need the history of a breadth line (the last shock, how long the base has held), read:
  data\chartink\analysis\market_breadth_daily.csv
One row per date. Do not read the 34 raw CSVs or the per-dashboard folders.

STEP 5. Check freshness.
- If the facts sheet is missing, or says fewer than 20 of 34 files are present, write only the front matter, the top heading, and an opening note stating what is missing. Stop and report.
- If the facts sheet's trade date equals the previous brief's trade date (market shut, or the download did not advance), still write, and open with "Same trade date as the previous brief: <date>."
- If 20 to 33 files are present, write the full brief and say in words, in each affected section, which file was missing.

STEP 6. Write the brief exactly to the structure in the framework section 4: front matter, "# Market read, <D Month YYYY>", opening note, then the headings The picture in one paragraph / Where the market stands / What the sectors say / What is leading / Who is buying / Thirty points (For the trader, For the investor, at least 15 each, numbered straight through, each a bold title sentence plus two to four plain sentences) / What would change this read. 3,000 to 5,000 words of prose. No tables. No bullet lists of metrics.

VOICE, the operator's standing ruling: explain the market to a smart friend who does not trade. Plain words, one idea per sentence, active voice, no em-dashes or en-dashes, no hedging filler, no AI tells. One rounded number only where it carries the point; no percentiles, no 1d/5d/20d triples in the prose. The operator rejected a numbers-dense brief as "too complex" and a short digest as "shallow" on the same day. Long and plain.

Rules that must not break:
- Every number used traces to the facts sheet or the history CSV. NOT FOUND stays NOT FOUND. Never estimate. Never carry an older number forward as current.
- Describe. No buy, sell, hold, target or stop instruction on any named stock. Name a stock only as the example that makes a group visible.
- Never invent a news reason. You have no web access; say so once in the opening note.
- Zero-prior shareholding rows are named as such once and never counted as a rise.

STEP 7. Save it.
  Write to:  data\chartink\analysis\briefs\<TRADE DATE>.md     for example 2026-09-04.md
  Copy over: data\chartink\analysis\briefs\latest.md
  Appendix:  copy data\chartink\analysis\facts\latest.md to data\chartink\analysis\briefs\<TRADE DATE>-appendix.md, replacing its first line with "# Market Breadth Brief: Data Appendix, <TRADE DATE>". The opening note of the brief links to it as <TRADE DATE>-appendix.html.

STEP 8. Put the picture into the digest page. Open data\chartink\analysis\digest\<TRADE DATE>.md. It ends with the marker line <!-- market-read -->. Replace everything below the marker with "## Market read", then the "The picture in one paragraph" text verbatim, then one line "Full brief: briefs/<TRADE DATE>.html". Never edit anything above the marker. Copy that file over data\chartink\analysis\digest\latest.md. If the digest file does not exist, skip and say so.

STEP 9. Render:
  python tools\chartink\render_html.py
It must print a briefs/ line naming the trade date you wrote. If it does not, STEP 7 did not land. Fix it and render again.

STEP 10. Push. Operator ruling 2026-10-01: the brief task pushes its own output the moment it exists, so a late brief never waits for the next night. Run exactly this one command and nothing else for git:
  cmd /c "C:\Users\SUMIT SHARMA\repos\inflection-pipeline\tools\chartink\push_data.bat"
The script commits only data\chartink, in its own worktree that tracks origin/main, and pushes to main. It never touches the branch the main checkout sits on. Do not run git commit, git push, git add or any other git command yourself. Exit 0 with "pushed <hash> to main" or "nothing new" is success. Any other exit code: do not retry and do not fix git; report the code. Nothing is lost, because the 22:15 "Chartink Data Push" job runs the same script as a safety net.

STEP 11. Report in five lines: the trade date, the files-present count, the word count and the number of points, the briefs/ line render_html.py printed, and the push_data line (or the exit code if it failed).