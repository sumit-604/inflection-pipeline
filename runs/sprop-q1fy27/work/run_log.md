# Run Log — SPROP Q1FY27 Quarterly Review

- Invoked: /run-quarterly SPROP --docs (results, presentation, press release)
- Run date: 2026-08-12
- Quarter detected: Q1FY27 (quarter ended June 30, 2026)
- Ticker: SPROP (Shriram Properties Limited; NSE SHRIRAMPPS / BSE 543419)

## Toolchain precheck
- pdftotext, pdfinfo, pdftoppm, tesseract: installed (poppler-utils + tesseract-ocr via apt).

## Protocol-file check
- Quarterly_Results_Review_Protocol_v1_2.md: PRESENT
- Quarterly_Concall_Analysis_Protocol_v1_1.md: PRESENT (no concall supplied this run)
- Master_Project_Prompt_v3.3.md: PRESENT

## Document-class detection (by content, not filename)
- results_sprop_q1fy27.pdf (10 pp): Reg 30 & 33 Board Outcome + "Unaudited Financial
  Results (Standalone and Consolidated), quarter ended June 30, 2026" + Limited Review
  Report -> class = RESULTS.
- presentation_sprop_q1fy27.pdf (26 pp): "Investor Presentation" on the unaudited
  results -> class = PRESENTATION.
- pressrelease_sprop_q1fy27.pdf (4 pp): "Press Release / MEDIA RELEASE" — management
  narrative + operational metrics + forward statements. No concall supplied. Enumerated
  under the PRESENTATION recipe (narrative claims + every number + dropped-disclosure
  logic); labeled press release so A3/A4 treat content as management narrative, not audited.

## Company memory / Notion
- companies/SPROP.md: ABSENT (no prior per-company memory file).
- Notion: fetch attempted live below.

## Page-count note
- Upload notice cited 24/54/4 pp; pdfinfo (authoritative for extraction) reports
  10/26/4 pp. File sizes consistent. A1 page-coverage gate keyed to pdfinfo.

## Live Notion thesis (fetched 2026-08-12, page https://app.notion.com/p/345bb2b9d3ab8012869de1c0bddbd5d3)
- Decision Status: AVOID. Gate 0: Core 31/100, Grand Total 36/160, Moat 5/60.
- No formal investment thesis / projections / thesis-broken conditions / quarterly monitoring
  checklist on the page (Gate 0 stub + one Q4 FY26 QER). Role 4 reconciliation is against
  the AVOID deal-breakers and the Step 8 watch-conditions, not thesis projections.
- Deal-breakers behind AVOID: structurally thin ROCE (~8.8% FY26, below ~13% CoE) from the
  asset-light JDA/JV model; tax-flattered PAT (FY26 ₹100.8 Cr crossed ₹1bn only via ₹22.9 Cr
  DTA credit; normalised ~flat YoY); JV income turned negative (−₹2.6 Cr FY26 vs +₹23.5 Cr FY25);
  operating EBITDA margin −540 bps; net FCF −₹148 Cr and net debt +34% in a record-revenue year.
- Step 8 watch-conditions (de-facto tripwires) for reopening the pipeline:
  1. Gate 0 rescore Core >60/100 (needs ROCE >15% and cash conversion healing).
  2. Concrete Kolkata (Uttarpara) land monetisation plan — ~272 acres freed after 42.37-acre
     GoWB settlement; disclosed structure, acreage, price, timeline.
  3. FY27 actual sales value >₹3,300 Cr AND gross margin >28% AND operating EBITDA margin >16%.
- Management FY27 guidance (from Q4 FY26): sales value ₹3,300-3,500 Cr (+40-49%), volume
  5.0-5.5 msf (+20-33%), collections ₹2,100-2,200 Cr (+26-32%), handovers 3,750-3,800 units (+8-10%).
- This context is passed inline to A3 and A4. Subagents do not call Notion themselves.
