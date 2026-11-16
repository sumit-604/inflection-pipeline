# Operating profit growth test, 2026-11 (laptop: ETERNALLAPTOP)

Facts only. No web. Nothing estimated.

- `universe.csv`: one row per company per period where a review exists (774 rows, 316 companies).
- `growth.csv`: the figures, operating profit both years, growth, label, source file and page or table.
- `names.md`: companies under each label, per period, sorted by growth.
- `missing.md`: every NO FILING row.
- `tools/`: the scripts.

## Where the numbers come from (operator ruling during the run, 2026-11-17)

The operator chose speed over opening every results PDF. So figures were copied from our own files, not re-read from the filings:

1. Review ledgers (251 rows): the P&L tables in the Quarterly Reviewer `1-ledger-forensics-*.md` files and the repo `ledger_results_*`, `extract_results_*` and `*-results-*-structured.md` files. These are our transcriptions of the filing and carry its page number. Copied by reader agents; nothing computed by them.
2. Screener quarter tables saved in repo run folders (163 rows), used where no ledger exists (mostly Q4 FY26 and Q1 FY27 rows from full runs). Screener puts exceptional items inside other income, so PBT minus other income leaves both out. These files do not say consolidated or standalone.
3. Neither available: NO FILING. The results filing was not opened for these rows.

## Rules

- Operating profit before tax = profit before exceptional items and tax, minus other income. Share of associates and joint ventures is removed where the PBT line includes it. After tax = x (1 - 25.17%); growth is the same before and after tax.
- Lenders: PBT minus treasury gains where the file states them, else reported PBT, marked LENDER-REPORTED.
- Labels: ABOVE 25%, 0 TO 25%, FELL, LOSS, TURNAROUND, LOW BASE (last year under Rs 1 Cr), NOT COMPARABLE, NO FILING.
- A census row counts as analysed when it holds an actual figure for that period.
- Half-yearly reporters: half year against the same half last year; their Q4 FY26 row is H2 FY26.
- Calendar-year companies are matched by quarter end date.
- Original lakh or million figures are kept beside the crore figures.

## Check

20 random rows with a results PDF on this machine were compared with the PDF's P&L page (four figures each: PBT and other income, both years). 10 matched by text search, 10 were read from the page by eye (scanned pages). 20 of 20 matched.

Separately, 13 ledger rows also had a screener table: 12 agreed within 5%; GVPIL Q2 FY27 differs (ledger is continuing operations only).

## Limits

- Not every row was checked against its PDF. Rows whose source is a presentation, press release or OCR-damaged text say so in the note column.
- NOT COMPARABLE was set by hand on seven rows from the reader notes; other rows with acquisitions or restated comparatives keep their label and carry a note.
