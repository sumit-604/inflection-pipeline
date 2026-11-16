# Census extraction brief (read fully before starting)

You are extracting FACTS ONLY for a three-quarter results census of an Indian-equities
research repo. No lessons, no opinions, no web, no estimating. If a fact is not in a file,
write `NOT FOUND`. Never compute a number that is not in a file (exception: none).
Do not explain why a miss happened in your own words; only quote what a file says.

Working dir (all relative paths below are under it):
`C:\Users\sumit\AppData\Local\Temp\claude\5b6e9d24bbef4fc7\49ef43bc-53d7-4762-8768-8ccd6ae36f42\scratchpad\retro`

Periods (exact labels to use):
- `Q4 FY26` (quarter ended 31-Mar-2026, results published ~May 2026)
- `Q1 FY27` (quarter ended 30-Jun-2026, results ~Aug 2026)
- `Q2/H1 FY27` (quarter/half ended 30-Sep-2026, results ~Oct-Nov 2026)

## Your batch
Your batch file (given in the task prompt) lists ~15 companies. For each company it lists:
- `COMPANY_FILE` : copies of the repo's companies/<TICKER>.md (several versions = different branches)
- `RUN <folder>` : a run folder, with each exported file and, after `<=`, its true source
  reference `origin/<branch>:<path>`. ALWAYS cite the `origin/<branch>:<path>` reference, never the corpus path.
  Folder names ending in a date are full pipeline runs (date = analysis date). Names ending
  -q4fy26 / -q1fy27 / -q2fy27 / -h1fy27 are quarterly result reviews for that period.
- `QR_DIR` : local Quarterly Reviewer output folder(s) (Q2 FY27 season). Read `SIMPLE_BRIEF.md`
  first, then Grep `REVIEW.md` / `NARRATIVE.md` / `3-audit.md` as needed. Cite as
  `QuarterlyReviewer/reviews/<batch>/<TICKER>/<file>`. NEVER open `api_key.txt` or anything outside `reviews`.
- `SESSION_EXCERPTS` : excerpts from Claude Code session history for that company (if the file exists).
  Cite as `session:<date>|<file path given in the excerpt header>`.
Also Grep these for each company (ticker and name):
- `corpus/LESSONS_ARCHIVE.md` and `corpus/LESSONS.md` (cite `origin/main:LESSONS_ARCHIVE.md`)
- `C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results\*.md` (top-level md files only;
  cite `ConcallPipeline/Q2 FY27 Results/<file>`)

Files are big. Use Grep with line numbers to find the relevant parts, then Read only those
line ranges. Useful search terms: `base case|base-case|Base`, `FY27E|FY27 `, `guidance|guided`,
`verdict|PASS|WATCH|BUY|AVOID|REJECT|Halt`, `archetype`, `SME|Emerge|main board|half-yearly`,
`order book`, `beat|miss|in line|below|above our`, `devil|risk|red flag`, `overrul|override|operator ruling`.
Line numbers in corpus files equal the line numbers of the original repo file.

## What to record per company
Company-level fields:
- `ticker`, `name`
- `board`: `SME` or `main` (only if a file says so, e.g. "NSE Emerge", "BSE SME", "SME"; else NOT FOUND)
- `reporting`: `quarterly` or `half-yearly` (from the files: if the company files quarterly results -> quarterly;
  if files say half-yearly / H1 only -> half-yearly; else NOT FOUND)
- `archetype`: the archetype / business-model label the files assign (quote the label; else NOT FOUND)
- `first_analysis_date`: earliest dated analysis of this company in any source (run folder date,
  manifest run_date, review date). ISO date. Give its source.
- `verdict_at_first`: the verdict/recommendation/gate outcome recorded at that first analysis
  (short quote, with source). NOT FOUND if none.
- `framework_date`: `before` if first_analysis_date < 2026-09-08, else `after`.
- `projection_basis`: which basis OUR base-case projection used, one or more of:
  `run-rate`, `order book`, `capacity`, `guidance`, `historical`; only if the valuation/thesis text
  shows it (give source). `NOT FOUND` if there is no projection.

Then exactly THREE period rows per company (one per period label above), each with:
- `base_revenue`, `base_margin`, `base_profit`: OUR base-case numbers that cover this period, as written in
  a valuation / thesis / fttcp / review file. State units and what period the number is for
  (e.g. "FY27E revenue Rs 412 Cr"). If our base case is for the full year only, record it and say so in
  `base_period`. Use the base case that was current BEFORE that period's result came out (give the file date).
  If the only base case was written after that period's result, put it in `notes`, not here.
- `base_period`: `quarter` / `half` / `full-year FY27` / `full-year FY26` / NOT FOUND
- `base_source`: `origin/<branch>:<path>` + section heading (and line if you have it)
- `guidance_quote`: management guidance in force at the time (short quote <= 25 words) + `guidance_source`
- `catalysts`: promised catalysts with dates as the files record them (e.g. "new plant commissioning Q3 FY27") + source
- `actual_revenue`, `actual_margin`, `actual_profit`: the reported actuals for THIS period if any file has them
  (units; say standalone/consolidated if the file does) + `actual_source`
- `result_vs_base`: one of `BEAT`, `IN LINE`, `MISS`, `NO BASELINE`. Rules:
  1. If a file explicitly states the result against OUR estimate/base case/thesis (e.g. "beat us", "below our base
     case", "in line with thesis numbers"), use that and quote it in `result_basis`.
  2. Else if both a like-for-like base-case number (same period, same metric) and the actual exist in files:
     profit (or revenue if no profit base) more than 5% above base = BEAT, within +/-5% = IN LINE, more than 5% below = MISS.
     Put the two numbers and their sources in `result_basis`.
  3. Otherwise `NO BASELINE` (this includes: no base case at all; base case is full-year only and no file compares
     the period to it; base case written after the result). Say which in `result_basis`.
- `mgmt_reason`: management's stated reason for the result (quote/paraphrase strictly from file) + `reason_source`. NOT FOUND if none.
- `risk_flagged_before`: was the specific risk that showed up in this result flagged in OUR files BEFORE the result?
  `YES` / `NO` / `NOT FOUND`. If YES give `risk_flag_ref` = `origin/<branch>:<path>:<line>` and a <=20-word quote.
  Only YES when a dated-earlier file names the risk. If there was no adverse result or nothing to compare, NOT FOUND.
- `who_flagged`: which stage/role flagged it as the file shows (e.g. `devil's advocate (15-devil.md)`, `verifier 12b red flags`,
  `thesis`, `valuation`, `gate0`, `operator`, `quarterly review audit`). NOT FOUND otherwise.
- `overruled`: `YES` / `NO` / `NOT FOUND` - whether that flag was overruled/overridden/dismissed per the files
  (e.g. an operator ruling, a deliberation that set it aside, "OVERRIDE"). Give `overruled_ref` (file + line + short quote).
- `notes`: anything needed to read the row correctly (e.g. conflicting numbers between branches: list both with sources).

## Outputs (write both for every company in your batch, even if almost everything is NOT FOUND)
1. `out/<TICKER>.json` - exactly this shape (all values strings; use "NOT FOUND" where absent):
```json
{"ticker":"","name":"","board":"","board_source":"","reporting":"","reporting_source":"","archetype":"","archetype_source":"",
 "first_analysis_date":"","first_analysis_source":"","verdict_at_first":"","verdict_source":"","framework_date":"",
 "projection_basis":"","projection_basis_source":"",
 "branches_with_files":"<count and, if 1, the branch name>","on_main":"YES/NO/PARTIAL",
 "rows":[{"period":"Q4 FY26","base_revenue":"","base_margin":"","base_profit":"","base_period":"","base_source":"",
          "guidance_quote":"","guidance_source":"","catalysts":"","catalysts_source":"",
          "actual_revenue":"","actual_margin":"","actual_profit":"","actual_source":"",
          "result_vs_base":"","result_basis":"","mgmt_reason":"","reason_source":"",
          "risk_flagged_before":"","risk_flag_ref":"","who_flagged":"","overruled":"","overruled_ref":"","notes":""},
         {"period":"Q1 FY27", "...":"same keys"},{"period":"Q2/H1 FY27", "...":"same keys"}],
 "files_read":["origin/...:path or local path", "..."]}
```
2. `out_md/<TICKER>.md` - the excerpts behind the rows: for each fact used, a short verbatim excerpt
   (1-6 lines) under a heading giving the source reference (`origin/<branch>:<path>` + section/line, or local
   path). Group by: Identity & first analysis / Our base case / Guidance & catalysts / Actuals by period /
   Risk flags & rulings / Session-history excerpts. Verbatim excerpts only, no commentary of your own
   beyond one-line labels. If a company file exists on several branches with different content, note which.

Validate each JSON with `python -c "import json;json.load(open(r'out/<T>.json',encoding='utf-8'))"`.
Write files as UTF-8. Work through ALL companies in the batch; do not stop early. Heavy companies
(valuation/thesis/devil files present) deserve most of your reading; quarterly-only or QR-only companies
with no base case can be done quickly (actuals + guidance + NO BASELINE).

Final reply: one line per company: `TICKER | Q4:<result> Q1:<result> Q2:<result> | anything odd`. Nothing else.
