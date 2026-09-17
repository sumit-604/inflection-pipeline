# Corpus manifest: RAMRAT (Ram Ratna Wires Ltd)

Collected 2026-09-17. Operator: Keerti Kaushik.
Company resolved: Ram Ratna Wires Ltd., BSE 522281, NSE RAMRAT, ISIN INE207E01023.
CIN L31300MH1992PLC067802. Incorporated 1992, listed on BSE 1995. Part of the Mumbai-based RR Global
group. Three plants at Dadra Nagar Haveli plus a copper tube plant at Bhiwadi, Rajasthan.

## Method note, and why this card is different
This is the one name in the run with a real corpus on the operator's disk. A `/run-pipeline` full
collection ran on 2026-07-29 and its inputs are tracked in this repository at
`runs/ramrat-2026-07-29/inputs/`. The annual report, the investor presentation and the CARE rating
were read locally from those PDFs with `pdftotext -layout`, not through a cloud reader. Only the
Q1 FY27 deck, which postdates that collection, came through Bull AI.

| File | Source | Held how | Pages | Reference |
|---|---|---|---|---|
| ratings/RAMRAT-CARE-2025-09-30-extract.txt | CARE Ratings press release, 30 Sept 2025 | PDF in repo | 1-3 of 7 | runs/ramrat-2026-07-29/inputs/rating/202509120948_Ram_Ratna_Wires_Limited.pdf |
| presentations/RAMRAT-InvestorPresentation-Q4FY26-2026-05-27.txt | Investor Presentation Q4 & FY26, filed 2026-05-27 | PDF in repo | 32-page deck, sections extracted | runs/ramrat-2026-07-29/inputs/presentation/Investor_Presentation_1.pdf |
| presentations/RAMRAT-InvestorPresentation-Q1FY27.txt | Investor Presentation Q1 FY27, filed 2026-07-31 | Bull AI text only | 5, 6, 7 | document_id 52a601d0-9045-4936-8633-8d0d6e32fcc3, https://docs.bull-ai.in/d/lfUHxc |

Also held in the repository but NOT read in this shallow run, and available to a `/step1`:
- `runs/ramrat-2026-07-29/inputs/annual-report/Annual_Report.pdf`, 315 pages.
- `runs/ramrat-2026-07-29/inputs/results/` two results PDFs, 23 and 11 pages.
- `runs/ramrat-2026-07-29/inputs/peer-concalls/` five peer transcripts: Bhagyanagar India (Feb 2026,
  Jun 2026, Nov 2025) and Vidya Wires (Dec 2025, May 2026). A peer set already collected.

## Freshness warning on the independent check
The CARE rationale is dated 30 September 2025 and is built on FY25 figures. It predates the FY26
results of 27 May 2026 and the Q1 FY27 quarter. The framework's rule applies: today's filings win
over an older rating. Read step 10 with that in mind. Bull AI's inventory shows no newer rating
document for this company; the agency site is unreachable from this session.

## Document notes
- The deck's Net Debt/Equity ratio excludes current borrowings by its own printed definition. See the
  card, step 9.
- Equity share capital rose from Rs 22.0 crore to Rs 46.7 crore between FY25 and FY26. The held
  extracts do not state the cause. The GCPL amalgamation, effective 23 June 2025, and a bonus issue
  are both candidates. NOT FOUND, and named as a verify item.
- The prior run's `runs/ramrat-2026-07-29/manifest.yaml` records `sector_cap_row: "Pharma / CDMO"`
  with the note "Sector row auto-picked; verify". That is the wrong sector row for a copper winding
  wire converter and would corrupt a Section 1B run. Flagged to the operator.

## Coverage gaps
- The 315-page annual report was not opened in this shallow run. No related-party schedule, no CARO
  annexure, no auditor's report, no shareholding pattern on this card.
- Promoter holding percentage and pledge: NOT FOUND. Looked for in the deck, the rating and the run
  manifest.
- No Ram Ratna earnings call was collected in the July run; the manifest records
  `concalls_available: false`. Bull AI does hold one transcript, FY26 Q3, filed 2026-03-09, which was
  not pulled in this run.
- No segment-level profit. The deck splits revenue between wires, tubes and others but not margin.
  Segment economics come only from CARE's PBILDT per tonne figures, which are FY25.
- No FY26 capacity utilisation figure for either segment.
- No FY26 or Q1 FY27 volume in tonnes. For a converter this is the metric that matters, and its
  absence is the largest gap on this card.
- Market capitalisation on the card header comes from Bull AI's identity record dated 2026-09-17, a
  service field, not a filing.
