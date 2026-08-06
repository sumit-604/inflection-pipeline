# Quarterly review run log — INDGN Q1 FY27

- Invoked: /run-quarterly INDGN --quarter Q1FY27
- Run date: 2026-08-06
- Quarter: Q1 FY27 (quarter ended 30 June 2026)

## Setup / prechecks
- Protocol files present: Quarterly_Results_Review_Protocol_v1_2.md, Quarterly_Concall_Analysis_Protocol_v1_1.md, Master_Project_Prompt_v3.3.md. OK.
- Toolchain: pdftotext/pdfinfo/pdftoppm/tesseract were MISSING at start; installed poppler-utils + tesseract-ocr (apt-get update fixed a stale-mirror 404 on poppler). All OK now (pdftotext 24.02.0, tesseract 5.3.4).
- Document class detection (from content, per orchestrator):
  - INDGN_Q1FY27_results.pdf -> RESULTS (10 pages). Reg 33 unaudited results, quarter ended 30 Jun 2026, limited review (085904ac, same filing consumed by the main pipeline run indgn-2026-08-03).
  - INDGN_Q1FY27_concall_transcript.pdf -> CONCALL (17 pages). Earnings call held 31 Jul 2026, transcript filed 06 Aug 2026 (INDGN/SE/2026-27/41). This is the Q1 FY27 concall the main pipeline run did NOT have.
  - INDGN_Q1FY27_investor_presentation.pdf -> PRESENTATION (22 pages). Q1 FY27 investor deck (Investor_Presentation_1).

## Company memory / Notion (passed inline to A3/A4)
- companies/INDGN.md exists (created at finalize of indgn-2026-08-03). Decision Status: pipeline recommendation BUY (on-dips); Notion Decision Status field left BLANK (operator to set). Entry Rs 534-668 (additive) / Rs 477-596 (RRM), MoS Rs 534. Tier B.
- Active tripwires (the monitoring spine to test this quarter against):
  1. PRIMARY: operating margin fails to expand sequentially two quarters from 16.4% (Q2-Q3 FY27) and near-20% H2 FY27 target not restated.
  2. Organic constant-currency ex-M&A growth at or below 12% YoY for two consecutive quarters (revenue FIRING->STARTING).
  3. Consolidated OCF/PAT below 1.0x with receivables ex-BioPharm outgrowing revenue ex-acquisition (FLAG-CASH growth-induced -> structural).
  4. Treasury deployability of ~Rs 1,100-1,337 cr; statutory ROCE recovery above 15%.
  5. Goodwill impairment on the 51.5%-of-net-worth base.
  6. Section 144B final-vs-draft tax contradiction; TCPA payout vs Rs 203 mn provision.
  7. New acquisition above Rs 500 cr rebloats capital (ROCE recovery -> STAGNANT).
- NOTE: this concall is the Q1 FY27 print; the main-run thesis said "the margin print is the whole thesis" and the falsifier keys off Q2 FY27. This quarterly review establishes the Q1 FY27 baseline against which those tripwires are watched.

## Sequence
A1 x3 (parallel) -> gate -> A2 x3 -> gate -> A3 x3 -> gate -> A4 (merged) -> A5 audit -> Notion -> commit.
