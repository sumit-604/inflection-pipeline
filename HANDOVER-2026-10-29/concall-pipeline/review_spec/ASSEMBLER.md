# Assembler: write the frame of the daily REVIEW.md

The company sections in `deep/out/*.md` are final. A script pastes them into REVIEW.md word for
word, so their depth is never lost. YOUR job is the frame around them and the order.
Style bar: `C:\ConcallPipeline\Daily Concall Intelligence\review_spec\STYLE_SAMPLE.md`. Read it first.

Inputs: every `deep/out/*.md` in the run folder (each company section starts with
`## <Company>: <headline>` and ends with a `<!-- DATA ... -->` block), `INDEX.md`, and
`deep/notes.md` if present (facts from the orchestrator). Read all of them in full.

Write three files into `<run folder>\deep\assembly\`:

## 1. order.json
```
{"material_in_master": ["<exact section heading company name>", ...],   // most decision-relevant first
 "brief_in_master": [...],
 "notable_not_in_master": [...],     // not in master but worth a proper read
 "routine_not_in_master": [...]}
```
Use the company name exactly as written after `## ` and before `:` in the section heading.
Every company section must appear in exactly one list.

## 2. front.md  (goes before the company sections)
- `# Watchlist review: <window>` and one opening paragraph: window, announcements, companies,
  how many are in COMPANIES MASTER, pages read, feed problems (wrong file behind a link,
  duplicate postings).
- `## Key documents`: annual reports, concall transcripts, investor presentations (page counts),
  then an "Upcoming investor meetings" table (company | date | format).
- The summary table for IN-MASTER companies, same order as order.json (material then brief):
  `| Company | Status on file | Entry / MoS | Latest price | What the filing does to the thesis |`
  built from the `table_row` lines. Tighten wording only. Keep each price exactly as the
  table_row gives it (price, read time, source, or PRICE NOT REFRESHED / STALE).
- Do NOT write a holdings price table. holdings_table.py builds it from the `levels:` lines
  and stitch_review.py places it at the top, under the title.

## 3. back.md  (goes after the company sections)
- `## Cross-links`: across the day. Merge analysts' cross_links and add any you see (same
  counterparty, same theme, same sector move, one company's event that changes another's thesis).
  Explain each link in 2-4 sentences, not a list of names.
- `## Unknowns`: "Resolved this session" and "Not resolved, and stated as the uncertainty of this read".
- `## Rulings needed`: numbered. Company, the gate or rule, the two readings, one or two sentences.
- `## Next action`: Claude Code never writes to Notion. The operator reads this report, then
  brainstorms and saves in Claude web (claude.ai). Write: "Read, then take this report to
  Claude web. Brainstorm there, and save to Notion from there. The proposed saves are below."
  Then a table: Company | Notion page link | Key Notes entry (first 15 words…) | Page body block
  | Tracker rows | Row changes. "Decision Status stays untouched on every row."
- `## Three things you did not ask about`: best three across all not_asked candidates, ranked by
  decision impact, each 2-4 sentences.
- `## PUBLISH CANDIDATE`: at most one, as a table like the sample, or "No publish candidate today."
  with one line why.
- `## Appendix A: Hand-over to Claude web (proposed Notion saves)`: open with one line telling
  Claude web: "These are proposals from the morning read. The source documents were read in
  full by Claude Code; do not re-read them. Treat each entry as a draft for the operator to
  confirm or change." Then, for each company with a notion_save: the company name, its Notion
  page link (from the work files' notion_page), the FULL Key Notes text, body block title,
  tracker rows, row changes, and the open rulings for that company. Self-contained: no
  "see above".
- `## Reading notes`: tool limits met (e.g. Notion query quota), facts taken from secondary
  sources (Trendlyne feed) rather than filings, corrections made to earlier quick cards.

Rules: plain simple English, short sentences, no em-dashes, no hedging filler. Keep every number
with its source. Never invent. Return only: the three paths, the counts per order list, and the
rulings list (one line each).
