# Operating profit growth of analysed results (laptop LAPTOP-8LJ3MSL6)

Facts only. No web. No estimates. Built 17-Nov-2026.

## Files

| File | What it is |
|---|---|
| `universe.csv` | 338 analysed results: ticker, name, period, where the review lives |
| `growth.csv` | one row per result: figures as filed, operating profit both years, growth, label, results file and page |
| `names.md` | per period, the companies under each label, sorted by growth |
| `missing.md` | the 62 NO FILING rows, so the filings can be fetched |
| `check.md` | the 20-row recheck: 20 of 20 matched |
| `tools/` | the scripts and the reader brief |

## Universe rule

A result is in the universe when one of these holds:
- a repo quarterly folder exists for the company and period (names ending
  `-q4fy26`, `-q1fy27`, `-q2fy27`, `-h1fy27`; `-q2cy26` is counted under Q1 FY27);
- the local folder `Q2 FY27 Results` has a folder for the company;
- the earlier census (`retro/2026-11/census.csv`) has actuals for the period that
  come from a local or session review note;
- the census has actuals for the period and that period's results filing sits in
  a repo pipeline run (the result was an input to the run).

A census row whose figures are only a comparative column from another period's
review is not counted. Companies under two tickers or codes were merged in
`retro/2026-11/tools/companies.json`.

`C:\QuarterlyReviewer` is named in old sessions but is not on this laptop, so
its batch folders were not read.

## Method

- Figures were copied from the statement of results in the filing (the PDF or
  its extracted text), this period and the same period last year, from the same
  table. Review files were used only to locate the filing.
- Consolidated where filed, otherwise standalone (`basis` column).
- Operating profit before tax = profit before tax and exceptional items, minus
  other income. Share of associates and joint ventures is taken out where the
  filing includes it in that line.
- Operating profit after tax = operating profit before tax x (1 - 25.17%).
  Growth is the same before and after this flat rate.
- Lenders: profit before tax minus treasury or trading gains where the filing
  states them for both years; otherwise reported profit before tax, marked
  LENDER-REPORTED.
- `..._as_filed` columns hold the original figure in the unit the filing uses
  (`unit_as_filed`); `..._cr` columns are the same figure in Rs crore.
- Half-yearly reporters: half year against the same half last year
  (`period_type` = half).

## Labels

ABOVE 25%, 0 TO 25%, FELL, LOSS (operating loss this year), TURNAROUND (loss
last year, profit this year), LOW BASE (last year under Rs 1 Cr; growth still
shown), NO FILING, NOT COMPARABLE (reason in `notes`).

Two rows sit on the 25% line: INDIAMART Q2 (25.04%) and WORKMATES H1 (25.0%).
They are labelled ABOVE 25% by the arithmetic.

## Check

Twenty rows were drawn at random. A second reader re-read the PDF pages without
seeing the first numbers. All 20 gave the same growth (`check.md`). The other
261 extracted rows were read once.
