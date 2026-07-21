# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 1 OF 3 (FULL EXTRACTION)
Company: KCPSUGIND (K.C.P. Sugar and Industries Corporation Ltd)
Run date: 2026-07-21
Source document: runs/kcpsugind-2026-07-21/inputs/annual-report/Annual_Report.pdf
(FY2024-25 Annual Report, year ended 31.03.2025, 275 pages)

## STATUS: MECHANICAL FAILURE — SOURCE DOCUMENT NOT READABLE. PASS 1 NOT PERFORMED.

This is a mechanical/tooling failure, not a finding about the company or its
disclosures. Per operating rules, mechanical failures halt; no notes content
below is inferred, estimated, or fabricated to compensate.

### What was attempted

1. `Read` on `inputs/annual-report/Annual_Report.pdf` with `pages` parameter
   (tried `1`, `1-5`, `1-20`) → error every time:
   `pdftoppm is not installed. Install poppler-utils (e.g. `brew install
   poppler` or `apt-get install poppler-utils`) to enable PDF page rendering.`
2. `Read` on the same file with no `pages` parameter (whole-document path,
   which does not require pdftoppm) → error:
   `PDF file exceeds maximum allowed size of 20MB.`
3. Confirmed the paged-read failure is environment-wide and not
   file-specific: the same `pdftoppm is not installed` error occurs on a
   different, unrelated PDF in this run's `inputs/results/` folder when a
   `pages` range is requested.
4. Confirmed the whole-document path works for PDFs under the 20MB cap
   (tested successfully on the 7-page CARE ratings PDF, 202.5KB, and the
   44-page FY26 results PDF, 14MB, both in this run's inputs — both read
   without a `pages` parameter and without needing pdftoppm).
5. Confirmed via `Grep` that the PDF's internal byte stream is not
   plain-text-searchable (compressed object streams), so no fallback
   text-scrape of the notes is possible with the tools available to this
   subagent (Read, Write, Grep only — no Bash/shell tool in this context).
6. Searched the run folder and repo for a pre-extracted text cache of this
   annual report (other runs in this repo carry an `extracted/` or
   `inputs/_textcache/` folder with a `.txt` companion to large PDFs). No
   such cache exists for `runs/kcpsugind-2026-07-21/`.

### Root cause

`Annual_Report.pdf` is >20MB. The Read tool has two paths:
- No `pages` param: reads the whole PDF directly, but is capped at 20MB —
  this file exceeds that cap.
- `pages` param (required for any PDF over ~10 pages to select a range):
  renders each requested page via `pdftoppm` (poppler-utils) — and
  poppler-utils is not installed in this session's environment.

Both paths are closed for this specific file. This matches a documented,
recurring issue: LESSONS.md (line 18, "PROMOTED TO LAW" candidate) records
that poppler-utils/pdftoppm has been absent at session start before (KARNIKA
2026-07-11, OBSCP 2026-07-12) and the fix (`apt-get update && apt-get
install poppler-utils`) requires shell/Bash access, which this subagent
does not have (tool set for this stage: Read, Write, Grep only).

### What this blocks

Every extraction category in the Pass 1 instructions (accounting policies,
related party transactions, contingent liabilities, trade receivables,
inventory, investments, borrowings, trade payables, provisions, deferred
tax, revenue details, and all "other critical notes" items) requires reading
the Notes to Financial Statements inside this specific PDF. None of it can
be extracted, confirmed, or ruled out from the documents this subagent could
successfully open (the CARE ratings press release and the FY26 results PDF
cover only summary financials, segment data, and the FY26 audit report/CARO
annexures — not the FY25 AR's notes to accounts). Using the FY26 results PDF
as a substitute for the FY25 AR notes would violate the "only what is in the
document" and "no estimation" rules for this stage, since it is a different
reporting period's summary financial statement, not the FY25 notes.

### Extraction categories — all NOT FOUND IN DOCUMENT (document inaccessible)

1. Accounting policies & changes — NOT FOUND IN DOCUMENT (source unreadable)
2. Related party transactions — NOT FOUND IN DOCUMENT (source unreadable)
3. Contingent liabilities — NOT FOUND IN DOCUMENT (source unreadable)
4. Trade receivables / ageing — NOT FOUND IN DOCUMENT (source unreadable)
5. Inventory — NOT FOUND IN DOCUMENT (source unreadable)
6. Investments (subsidiaries, JVs, ICDs) — NOT FOUND IN DOCUMENT (source unreadable)
7. Borrowings — NOT FOUND IN DOCUMENT (source unreadable)
8. Trade payables / MSME ageing — NOT FOUND IN DOCUMENT (source unreadable)
9. Provisions — NOT FOUND IN DOCUMENT (source unreadable)
10. Deferred tax — NOT FOUND IN DOCUMENT (source unreadable)
11. Revenue details / disaggregation — NOT FOUND IN DOCUMENT (source unreadable)
12. Other critical notes (exceptional items, goodwill, commitments, hedging,
    segment reporting, EPS gap, subsequent events, CSR, ESOP, reserves) —
    NOT FOUND IN DOCUMENT (source unreadable)

### Context worth carrying forward (not from the FY25 AR notes; from other
readable inputs in this run — flagged as non-anchored-to-notes, do not treat
as satisfying any Section 12 item above)

- The CARE Ratings press release (07 Oct 2025, `inputs/rating/...pdf`,
  fully read) and the FY26 audited results filing (27 May 2026,
  `inputs/results/731297df-...pdf`, fully read) both cover FY25/FY26
  standalone and consolidated summary financials, but neither is a
  substitute for the FY25 AR's notes to accounts. Figures from those two
  documents belong in other stages' evidence base (e.g., B00 inventory,
  stage on results/ratios), not in this notes-pass report.
- Both documents flag items that the FY25 AR's notes would likely detail
  further if read: pending tax/GST/EPF litigation (Annexure A to the FY26
  auditor's report lists disputed statutory dues across VAT, EPF, A.P.E.D
  Act, and GST, some multi-year and pending before tribunals/High
  Court/Supreme Court); managerial remuneration paid below Schedule V
  minimum-profit threshold for a fourth consecutive year (FY26 report,
  Note 51 cross-reference); investments concentrated in FVTPL equity and
  mutual funds; one unaudited-by-principal-auditor subsidiary in the
  consolidated results. These are FY26-dated observations from FY26
  documents, not verified against the FY25 AR notes referenced in this
  stage's brief, and must not be cited as this stage's findings.

## PASS 1 SUMMARY

Top 10 significant findings: NONE PRODUCED. Pass 1 could not be executed
because the source document (`inputs/annual-report/Annual_Report.pdf`) could
not be opened by any tool available to this subagent (Read tool blocked by
file size >20MB on the no-`pages` path and by missing poppler-utils/pdftoppm
on the `pages` path; Grep cannot read compressed PDF streams; no Bash tool
available to install poppler-utils or pre-extract text; no cached text
extraction exists for this run).

## REQUIRED ACTION BEFORE THIS STAGE CAN RE-RUN

1. An agent/environment with shell access must run
   `apt-get update && apt-get install -y poppler-utils` (see LESSONS.md
   line 18) and verify with a real paged `Read` call, OR
2. Pre-extract the annual report's notes-to-accounts pages to a `.txt` file
   under this run's `inputs/` (as done for other tickers in this repo, e.g.
   `runs/prizor-2026-07-12/inputs/_textcache/Annual_Report_2025.txt`) and
   re-point this stage at that file, OR
3. Split `Annual_Report.pdf` into <20MB chunks so the no-`pages` Read path
   can be used.

This stage should be re-invoked only after one of the above is done. Do not
proceed to Pass 2/3 or emit a B02-notes YAML block on this run; the required
accounting_quality score and top_findings would have no evidentiary basis.
