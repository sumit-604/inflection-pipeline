# Results census 2026-11 (laptop: ETERNALLAPTOP)

Facts only, for the lessons review. Periods: Q4 FY26, Q1 FY27, Q2/H1 FY27.

- `census.csv`: one row per company per period (323 companies, 969 rows). Every number column has a matching `source:` column.
- `companies/<TICKER>.md`: the excerpts behind each row, with file names.
- `gaps.md`: companies with no baseline, no actuals, or files on one branch only; conflicts between files.
- `sources.md`: counts of branches, run folders, sessions and local files read; method; rules; limits.
- `sessions_index.tsv`: one line per session transcript scanned.
- `tools/`: the scripts. Second laptop: run `inventory.py`, `export_corpus.py`, `build_map.py`, `extract_sessions.py`, then extract per `AGENT_BRIEF.md`, then `assemble.py`.

`NOT FOUND` means no file read holds the fact. Nothing is estimated.
