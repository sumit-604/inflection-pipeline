# Sources - results census 2026-11 (ETERNALLAPTOP)

## A. Repo

- Remote branches listed after `git fetch --all`: 315 (run/*: 58, claude/*: 229, other: 28)
- Run folders found across all branches: 306 (excluding runs/_template); on main: 106; not on main: 200
- companies/*.md files across all branches: 117 paths
- Text files exported for reading with git cat-file (no checkout): 2578
- Files kept per full run: manifest.yaml, run-log.md, step1-business-brief.md, outputs/final/*.md, outputs/qa/*.md, outputs/reports for stages 10 and later (assembly, valuation, synthesis, thesis, devil's advocate). Per quarterly folder: review, audit, ledger, notion payload, run log, SOURCES.md. Excluded: PDFs, CSVs, YAML blocks, full-text extracts, forensic notes, stage 01-09 reports.
- LESSONS_ARCHIVE.md and LESSONS.md read from origin/main.

## B. Claude Code session history

- .jsonl files read: 1075; with user/assistant text: 1042; with company excerpts: 632
- Excerpts saved: 1963. Script: extract_sessions.py (user and assistant text only; tool calls and tool results skipped). Per-session list: sessions_index.tsv

## C. Local folders

- Quarterly Reviewer: C:\QuarterlyReviewer\QuarterlyReviewer\reviews, 13 batch folders, 188 company folders, 156 companies
- Concall pipeline: C:\ConcallPipeline\Daily Concall Intelligence\Q2 FY27 Results (top-level .md files searched per company)

## Files cited by the per-company extraction (files_read lists)

- repo (origin/...): 1155
- Quarterly Reviewer: 356
- session history: 277
- other local: 97
- Concall pipeline: 59

## Census size

- Companies: 322
- Rows: 966 (three periods per company)
- Rows by result: MISS 49, BELOW BASE 20, IN LINE 27, BEAT 66, NO BASELINE 804
- Companies with at least one row of each result (NO BASELINE counts only companies with no other result): MISS 42, BELOW BASE 18, IN LINE 24, BEAT 56, NO BASELINE 195

## Method

1. `tools/inventory.py` lists every file under runs/ and companies/ on every remote branch (git ls-tree, no checkout).
2. `tools/export_corpus.py` reads the kept text files with git cat-file into a temporary folder. Nothing was checked out.
3. `tools/build_map.py` groups run folders, company files and Quarterly Reviewer folders by company and builds name aliases.
4. `tools/extract_sessions.py` scans session history and saves per-company excerpts.
5. Per-company facts were extracted by reader agents (22 batches of about 15 companies) under `tools/AGENT_BRIEF.md`. Each wrote one JSON record and one excerpt file per company.
6. `tools/assemble.py` builds census.csv, companies/, gaps.md and sources.md from those records.

## Rules used for "result vs our base case" (operator rulings on PR 245, 2026-11-17)

- A file's own statement against our base case, thesis line or pre-committed test is used first. The `basis of result call` column quotes it.
- Else a like-for-like number comparison: profit (or revenue) more than 5% above base is BEAT, within 5% is IN LINE, more than 5% below is BELOW BASE. The 5% band is kept by operator ruling.
- MISS: the file puts a key metric below bear (or below stress, a red line or a floor). MISS is also kept where a pre-committed test or tripwire failed and the file gives no bear/base placing; those rows start with "[MISS on a failed pre-committed test or tripwire ...]" in `basis of result call`.
- BELOW BASE: the file puts the result between bear and base, or below base, with no key metric below bear. Twenty rows carry this label; `tools/assemble.py` lists them.
- NO BASELINE: no base case; a full-year base that no file compares to the period; or a base case written after the result.
- PRO-RATED in the `base comparison` column: the scored row compares the period with a full-year or multi-year base scaled to the period (halved, annualised, pace, or percent of the base). The mark comes from a text match on the base-period and basis fields. NOT PRO-RATED rows rest on a same-period base, a pre-committed quarterly test, or a statement with no scaling words. Check the basis line where it matters.
- Reviewer-only companies with no thesis stay in the census as NO BASELINE.
- Many scored rows are mixed (for example profit above base, cash below bear). BEAT and IN LINE labels follow the file's headline wording and were not re-ruled.
- Two labels were withdrawn at assembly because they rested on arithmetic no file contains: KMCSHIL Q1 FY27 and SUPREMEPWR Q2/H1 FY27.
- 544186 and TOTEM (Forbes Precision Tools) are merged under TOTEM.

## Limits

- Line numbers are those of the repo file on the cited branch. Local Quarterly Reviewer files are cited as `REVIEW.md:<line>`.
- Half-yearly filers: the Q4 FY26 row holds H2 FY26 or full-year FY26 where the files have only that; the Q1 FY27 row has no result. The row notes say so.
- Calendar-year reporters (ABB, HEXT, RSYSTEMS) are mapped to the nearest period; the row notes give the mapping.
- "Our base case" often comes from a Notion thesis quoted inside a review file. The Notion pages themselves were not read (no web).
- Extraction was done by model readers. The audit at assembly checked every BEAT, IN LINE and MISS basis line, not every number. Numbers should be spot-checked against the cited file before a lesson is drawn from them.
- This census covers one laptop (session history and local folders). The second laptop can rerun the tools and add its rows.

## What is not in this folder

- The raw per-company session-history excerpts are not in this repository (operator ruling, 2026-11-17: keep them local). They are on the laptop in `retro/2026-11/_local_session_excerpts/` (git-ignored). The excerpts a row relies on are quoted in `companies/<TICKER>.md`.
