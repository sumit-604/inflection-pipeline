# Sources

Laptop: LAPTOP-8LJ3MSL6. Built 2026-11-16.

## A. Repo

- Remote branches read (after `git fetch --all`): 315
  - run/*: 58; claude/*: 229; main: 1; other prefixes: 27
- Run folders found across all branches: 306 (106 on main, 200 not on main)
- Quarterly folders (name ends -q4fy26, -q1fy27, -q2fy27, -h1fy27, -q2cy26): 154
- Companies (run folders grouped by ticker): 244
- Company memory files (companies/*.md, any branch): 117
- Text files exported and available to readers: 9375 (via `git cat-file`, nothing checked out)
- LESSONS_ARCHIVE.md and LESSONS.md: read (grepped per company)

## B. Claude Code session history

- .jsonl session files read: 2594 in 43 project folders
- Date range of sessions: 2026-09-04 to 2026-11-16
- Session files with at least one kept excerpt: 1333
- Companies with session excerpts: 160
- Only user and assistant text was read; tool calls, tool results and thinking were skipped.

## C. Local folders

- C:\ConcallPipeline\Daily Concall Intelligence: found
  - .md files read: 10422; with at least one kept excerpt: 3750
  - Companies with local excerpts: 226
  - PDFs, audio and raw .txt extracts were not read.
- Quarterly Reviewer output folder: NOT FOUND under that name (searched the user profile, Documents, Desktop, Downloads, OneDrive and C:\ two levels deep). The folder "Q2 FY27 Results" inside the Concall folder was read as part of C.

## Census

- Rows: 732 (244 companies x 3 periods)
- Company excerpt files: 244
- result_vs_base counts (rows): BASELINE NOT COMPARABLE 67; BEAT 37; IN LINE 38; MISS 73; NO BASELINE 517
