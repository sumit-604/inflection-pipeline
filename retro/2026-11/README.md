# Results census, Nov 2026 (laptop LAPTOP-8LJ3MSL6)

Facts only. No lessons, no opinions, no web. Built 16-Nov-2026.

Periods: Q4 FY26 (results May 2026), Q1 FY27 (Aug 2026), Q2/H1 FY27 (Oct-Nov 2026).

## Files

| File | What it is |
|---|---|
| `census.csv` | 732 rows: 244 companies x 3 periods, 28 columns |
| `companies/<TICKER>.md` | 244 files: the verbatim excerpts behind each company's rows, with file names and lines |
| `gaps.md` | companies with no baseline, no actuals, or files on one branch only |
| `sources.md` | counts of branches, run folders, sessions and local files read |
| `tools/` | the scripts, the company list and the reader brief |

## How to read `census.csv`

- A company is a group of run folders with the same ticker prefix (`tools/companies.json`).
- Every company has three rows. `NOT FOUND` means no file gives the value.
- `result against our base case` takes five values, not four:
  - `NO BASELINE`: no base case of ours predates the result.
  - `BEAT`, `IN LINE`, `MISS`: only where a file states the comparison, or where
    our base case and the actual cover the same period (then revenue at +/-5%).
  - `BASELINE NOT COMPARABLE`: a base case exists but for a different period
    length (annual base, quarterly actual) and no file states the comparison.
    Nothing was pro-rated.
- `classification caveat` says how firm a BEAT / IN LINE / MISS label is:
  - `none`: a file states the comparison against a numeric base case.
  - `NO NUMERIC REVENUE BASE`: the label rests on a threshold, tripwire or the
    file's own wording, not on a revenue projection.
  - `FILE SAYS MIXED; label chosen by reader`: the source calls the result mixed.
    The label is the reader's choice. Treat these rows as unclassified.
  - `COMPUTED same-period at +/-5%`: arithmetic on same-period figures.
- `framework date` is computed from `first analysis date` against 08-Sep-2026.
- File citations are repo-relative (`runs/...`, `companies/...`). The branch that
  holds each run folder is in the `run folders and branches` column. Citations to
  `retro/2026-11/excerpts/...` point to excerpt files kept on the laptop only. Where a cell still says
  "scratchpad" or "local_old", read it as `retro/2026-11/excerpts/local/`.

## How it was built

1. `git fetch --all`, then `tools/export_repo_text.py`: reads every `origin/*`
   branch with `git ls-tree` and `git cat-file`. Nothing was checked out. Where a
   path differs between branches, the copy on the newest branch was read.
2. `tools/build_companies.py`: groups run folders by ticker.
3. `tools/extract_session_excerpts.py`: streams every `.jsonl` under
   `%USERPROFILE%\.claude\projects\`, keeps user and assistant text only, tags
   each session with date and folder, and saves paragraphs that name a company
   and mention results, guidance, margin, delay, order book or a miss.
4. `tools/extract_local_excerpts.py`: the same for local `.md` files.
5. `tools/make_packets.py`: one reading list per company.
6. Reader agents (Claude sub-agents) followed `tools/READER_BRIEF.md`, one batch
   of companies each, and wrote three rows and an excerpt file per company.
7. `tools/assemble_census.py` and `tools/fix_paths.py`: build the CSV, `gaps.md`,
   `sources.md`.

## Second laptop

```
python tools/export_repo_text.py <repo> <work>/repo
python tools/build_companies.py <work>/repo <work>/tools/companies.json
python tools/tier.py <work>/repo <work>/tools/companies.json
python tools/extract_session_excerpts.py <work>/tools/companies.json <work>/sessions
python tools/extract_local_excerpts.py <work>/tools/companies.json <work>/local <local folder> [...]
python tools/make_packets.py <work>
#   readers follow tools/READER_BRIEF.md and write <work>/out/rows, <work>/out/companies
python tools/assemble_census.py <work> retro/2026-11 <laptop name>
python tools/fix_paths.py retro/2026-11 tools/READER_BRIEF.md
```
Copy the scripts into `<work>/tools/` first. Steps 3 and 4 are the laptop-specific
ones; the repo side should give the same result on both laptops.

## Public-repo scrub (17-Nov-2026)

- The per-company excerpt files (`excerpts/sessions/`, `excerpts/local/`) are not in the repo. They hold
  conversation text and private notes and stay on the laptop. A citation to
  `retro/2026-11/excerpts/...` therefore cannot be opened from the repo.
- `tools/scrub_public.py` replaced every clause in `census.csv` and `companies/*.md` that mentioned a
  holding, its cost or its size with `[holding detail removed]`, and replaced person names with
  "operator". Valuation outputs and verdict words were left as they were.

## Known limits

- Rows were extracted by reader agents from the files. Five cited lines were
  re-checked by hand against the source files and matched. The rest are unaudited.
- Q4 FY26: the repo starts in July 2026, so almost no base case predates that result.
- PDFs, audio and raw text extracts were not read. Actuals come from our review
  files, session text and local notes only.
- The "Quarterly Reviewer output folder" was not found under that name on this laptop.
- `d-dev-q1fy27` and `deedev-2026-11-15` are DEE Development Engineers (DEEDEV),
  a different company from DDev Plastiks (DDEVPLSTIK). They are separate rows.
