# Operating profit growth test (laptop: ETERNALLAPTOP)

Facts only. No web. No estimates. Periods: Q4 FY26, Q1 FY27, Q2/H1 FY27.

## Files
- `universe.csv`: every analysed result, one row per company per period, and where the review lives.
- `growth.csv`: the filed figures, operating profit for both years, growth, label, file name and page.
- `names.md`: for each period, the companies under each label, sorted by growth.
- `missing.md`: rows with no readable results filing on this machine.
- `check.md`: the 20-row check.
- `tools/`: the scripts and the two reader briefs.

## Universe rule
A row is in the universe when a review exists for that period in one of these places:
- a Quarterly Reviewer review folder (Q2/H1 FY27);
- a repo quarterly folder (`-q4fy26`, `-q1fy27`, `-q2fy27`, `-h1fy27`, and calendar-year equivalents);
- a full pipeline run whose `inputs/results/` holds the filing for that period;
- a company folder in the Concall pipeline `Q2 FY27 Results`.
A census row alone does not count. 398 census rows quote actuals for a period with no review folder; they are not in the universe.
IPCL and INVPRECQ are the same company and are merged under INVPRECQ.

## Method
- Operating profit before tax = profit before exceptional items and tax, minus other income.
- Where the filed PBT line already includes the share of associates or joint ventures, that share is removed.
- Operating profit after tax = operating profit before tax x (1 - 25.17%). Growth is the same on both.
- Lenders: PBT minus stated treasury or trading gains; where none is stated, reported PBT, marked LENDER-REPORTED.
- Quarterly reporters: the quarter against the same quarter last year. Half-yearly reporters: the half against the same half last year.
- Consolidated where the filing has it, otherwise standalone. The column says which.
- Figures are copied as printed. The crore figure sits beside the original lakh, million or crore figure.

## How the figures were read
- First read: from the extracted text of each filing (399 rows, less those with no filing).
- Second read: an independent reader took the figures from the PDF page images for every row whose text was image-only, garbled or flagged. It did not see the first read.
- `read check` column in `growth.csv`:
  - two independent reads agree: 163 rows
  - single read from extracted text: 154 rows
  - page-image read only (text unusable): 41 rows
  - two reads differ; page-image read used: 22 rows
  - no usable read: 17 rows
  - single read from extracted text; page-image reader could not confirm: 2 rows
- Where the two reads differ, the page-image read is used and the first read is kept in the notes.
- Rows marked "single read from extracted text" had clean text and were read once.

## Labels
ABOVE 25%, 0 TO 25%, FELL, LOSS (operating loss this year), TURNAROUND (loss last year, profit this year), LOW BASE (last year's operating profit before tax under Rs 1 Cr), NO FILING, NOT COMPARABLE (the filing has no same-period comparative, or says the comparative is not comparable).

## Limits
- Some first-time consolidated filings print the holding company's standalone figures as the comparative (for example DIVGIITTS Q2, E2E Q1, UTLSOLAR Q1, FLYSBS H1). The filing does not call them non-comparable, so they are scored. The notes say so.
- Other income is the line the filing prints. Gains that a company books inside other income are removed with it; gains booked elsewhere are not.
- A full pipeline run is counted for each period whose filing sits in its inputs. The run may not have reviewed that quarter on its own.
- No holdings, prices or position sizes are in these files.
