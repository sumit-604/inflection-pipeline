# Prompt for the laptop session

Paste everything below the line into Claude Code on the laptop, in the
inflection-pipeline repo.

---

TASK: Finish the operating-profit growth table. A cloud session built it from
the repo. It could not see this laptop's folders. Fill the rows it left as
NO FILING, using files on this laptop. Facts only. No web. No estimates.

STEP 0. GET THE CLOUD WORK
Run: git fetch origin retro/2026-11-cloud
Read these with "git show origin/retro/2026-11-cloud:<path>" (no checkout):
- retro/2026-11/growth/README.md        (method, labels, what each source means)
- retro/2026-11/growth/universe.csv     (505 results, 318 companies)
- retro/2026-11/growth/growth.csv       (one row per result; 231 are NO FILING)
- retro/2026-11/growth/missing.md       (the NO FILING list)
- retro/2026-11/growth/tools/label_rows.py and tools/extraction_rules.md
Copy the whole retro/2026-11/growth/ folder into the working tree of the
existing laptop retro branch (retro/2026-11-ETERNALLAPTOP). Work there.

STEP 1. ROWS TO FILL
In growth.csv, column "number source":
a) LAPTOP ONLY (139 rows, all Q2/H1 FY27). The review is in
   C:\QuarterlyReviewer\QuarterlyReviewer\reviews\<batch>\<TICKER>\ or in
   C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results.
   universe.csv names the folder for each row.
b) NONE (92 rows). The review is in the repo but the results statement for the
   period, or its year-ago column, is missing or unreadable there. Look for
   the filing on this laptop: the Quarterly Reviewer folders, the Concall
   pipeline folders, and the run's inputs folder if the run exists locally.
c) Also add any company and period that has a review in the Quarterly Reviewer
   folders (all batch folders) or the Concall pipeline but is not in
   universe.csv. Add it to universe.csv first. Merge duplicates (same company
   under two tickers or codes).
Do not redo rows that already have numbers.

STEP 2. WHERE TO TAKE THE NUMBERS (operator ruling 2026-11-17, "option A")
For each row, in this order:
1. The table in our review file that was copied from the results filing
   (REVIEW.md, NARRATIVE.md, notion.md, review_*.md). Use it when it prints,
   for BOTH this period and the same period last year: profit before tax and
   exceptional items, other income, exceptional items, and reported profit
   after tax. Source label: REVIEW TABLE. Cite the review file and line.
2. If the review table lacks one of those lines, open the results filing in
   the same folder (the Reg 33 PDF or its extracted text) and take the lines
   from the statement. Source label: FILING TEXT, or PDF PAGE IMAGE if you
   read the page image. Cite the file name and page.
3. If neither has both years, the row stays NO FILING. Say why.
Never back-compute a year-ago number from a growth percentage. Never compute
PBT from EBITDA, PAT or margins. Never restore an unreadable digit by
arithmetic; write UNREADABLE and leave the row NO FILING.
Check the unit of every review table against the filing where you can. The
cloud check found one review table ten times too small.

STEP 3. COMPUTE, SAME METHOD AS THE CLOUD ROWS
- Quarterly reporters: the quarter against the same quarter last year.
  Half-yearly reporters (SME): the half year against the same half last year.
- Consolidated where filed, otherwise standalone. Say which.
- Operating profit before tax = profit before tax and exceptional items,
  minus other income. If share of profit of associates and joint ventures
  sits inside the PBT line, subtract it too.
- Operating profit after tax = operating profit before tax x (1 - 25.17%).
- Leave out exceptional items and one-off gains shown as their own line.
- Banks and lenders: PBT minus treasury or trading gains where the statement
  prints them for both years; otherwise reported PBT, mark LENDER-REPORTED.
- Growth = this year / last year - 1. Reported profit growth = reported PAT
  this year / last year - 1.
- Lakh, million or thousand: convert to crore and keep the original figures
  in the "original figures" column.
Use tools/label_rows.py so the arithmetic and labels match the cloud rows.
Labels: ABOVE 25% / 0 TO 25% / FELL / LOSS (operating loss this year) /
TURNAROUND (loss last year, profit this year) / LOW BASE (last year under
Rs 1 Cr; still show growth) / NO FILING / NOT COMPARABLE (merger, demerger,
changed year-end, first period with no year-ago column; say why).

STEP 4. WRITE BACK, SAME FILES AND COLUMNS
In retro/2026-11/growth/ on branch retro/2026-11-ETERNALLAPTOP:
- growth.csv: replace each filled row in place. Keep every column. Set
  "number source" to REVIEW TABLE, FILING TEXT or PDF PAGE IMAGE. Rows you
  could not fill stay NO FILING with the reason in "notes".
- universe.csv: add the rows from step 1c.
- names.md: rebuild. Per period, the companies under each label, plain lists,
  sorted by growth, highest first.
- missing.md: rebuild. Every row still NO FILING, ticker and period.
- README.md: update the counts and add a "Laptop pass" section: rows filled
  by source, rows still missing.

STEP 5. CHECK YOUR OWN WORK
Pick 20 of the rows you filled at random. Open the results PDF page for each
and recompute growth. Report how many matched. Fix any that did not, and say
which.

RULES
- Every number carries the file name and page (or review file and line).
- The repo is public. Do not write holdings, buy prices or position sizes.
  Do not commit raw session history or anything from outside the review and
  results files.
- Commit and push to retro/2026-11-ETERNALLAPTOP. Do not merge. End the
  report with the commit hash and "git log -1 --stat".
- If you have questions, put them in one list at the end with your
  recommended answer for each.

FINAL MESSAGE, in simple language:
- Universe: companies and results per period, after your additions.
- For each period: how many ABOVE 25%, 0 TO 25%, FELL, LOSS, TURNAROUND,
  LOW BASE, NO FILING, NOT COMPARABLE.
- The names of the ABOVE 25% companies for Q2/H1 FY27, with growth %.
- How many of those also grew above 25% in Q1 FY27.
- The result of the 20-row check.
