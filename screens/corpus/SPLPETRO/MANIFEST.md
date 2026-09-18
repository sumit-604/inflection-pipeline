# Corpus manifest: SPLPETRO (Supreme Petrochem Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Supreme Petrochem Ltd., BSE 500405, NSE SPLPETRO, ISIN INE663A01033.

## Method note
This session had Bull AI MCP access with no PDF egress. All text below is page-marked text
pulled through Bull AI's `get_document_chunks` (and one `get_company_guidance` call), keyed to
the filed PDF's own page numbers so a citation can be traced to a real page even without the PDF
on disk.

## Metered call count: 9

1. `get_company_guidance` (identifier SPLPETRO) — 1 call. Returned guidance and self-reported
   deliveries across Q3FY24, Q1FY25, FY25 (annual), Q1FY26, Q4FY26, Q1FY27.
2. `get_document_chunks` (subcategory "Earnings Call Transcript", FY2027 Q1) — 1 call. Returned
   the full Q1FY27 concall transcript, pages 1-14 (whole document, no further pages exist).
3. `get_document_chunks` (subcategory "Investor Presentation", FY2027 Q1) — 1 call. Returned
   zero chunks; document exists in Bull AI (document_id cd3b0461-526c-4968-aea6-fca1c83c323d,
   filed 2026-07-27) but carries no extractable text.
4. `search_company_documents` (query "credit rating CRISIL ICRA CARE India Ratings") — 1 call.
   Found two live ratings: CRISIL (FY26 Q4) and India Ratings (FY26 Q3).
5. `get_document_chunks` (bundled requests: CRISIL rationale pages 1-4, India Ratings rationale
   pages 1-4, Investor Presentation FY2027 Q1 pages 1-20 retried) — 1 call. IP retry again
   returned zero chunks.
6. `search_company_documents` (query "promoter shareholding pattern pledge board of directors
   related party", doc_types annual_report) — 1 call.
7. `search_company_documents` (query "management discussion and analysis outlook risk styrene
   demand", doc_types annual_report) — 1 call.
8. `get_document_chunks` (bundled requests: FY25 Annual Report pages 42-50, and an attempted
   150-151 request that the server dropped from the bundle) — 1 call.
9. `get_document_chunks` (FY25 Annual Report, page 150 only, promoter shareholding table) — 1
   call.

`list_document_availability` (free, not counted) was run first to build the ledger below.

## Table of files held

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/SPLPETRO-Concall-Q1FY27-2026-08-04.txt | Q1 FY27 earnings call, held 29-Jul-2026, filed 04-Aug-2026 | 1-14 (full) | 56c5ebe3-8a2e-4480-b19d-518666e5509d |
| filings/SPLPETRO-CreditRating-CRISIL-FY26Q4-2026-02-28.txt | CRISIL Ratings rationale, 27-Feb-2026 | 1-4 (full) | 1cc04adc-d44a-43c4-b3ca-a91c37b2e66a |
| filings/SPLPETRO-CreditRating-IndiaRatings-FY26Q3-2025-12-17.txt | India Ratings press release, 16-Dec-2025 | 1-4 (full) | 5317690a-1896-4918-aee3-3ad5bc4cd56d |
| annual_reports/SPLPETRO-AnnualReport-FY25-MDA-Governance-2025-03-31.txt | Annual Report FY2024-25 (Reg 34(1)) | 42-50, 150 | d3e5abca-63c0-4304-ae72-0ef0333ff509 |
| filings/SPLPETRO-Guidance-BullAI-2026-09-18.txt | Bull AI guidance/delivery synthesis, spanning Q3FY24-Q1FY27 filings | n/a (cross-document) | multiple, see file |

## Coverage gaps

- **No investor presentation held.** Bull AI carries the Q1FY27 IP record (document_id
  cd3b0461-526c-4968-aea6-fca1c83c323d, filed 2026-07-27) and several earlier-period IPs, but the
  chunk reader returns zero text for the Q1FY27 one on two attempts. No deck of any period was
  pulled. Weakens step 1 and any slide-level detail (segment revenue split, spread charts).
- **No Q4FY26 concall transcript full text.** Only guidance/delivery snippets via the guidance
  tool (pages 3, 4, 6, 8-10, 12-13 of that transcript, document_id 115bd94b-18d5-4228-9984-
  cecfa6a49d1c) were captured, not the full page-by-page transcript. A dedicated
  get_document_chunks pull was not made to stay within budget; the Q1FY27 call already covers the
  most current operating narrative.
- **No FY26 annual report.** Bull AI's latest annual report on file is FY25 (period ended
  31-Mar-2025). FY26 has not yet been filed as of this run.
- **No full financial statements, cash flow statement, or segment note.** Only the Key Financial
  Ratios table (AR p.45) and the promoter shareholding note (AR p.150) were pulled from the notes
  to accounts. Balance sheet, cash flow statement, and the related-party transaction schedule
  (Note 46, referenced but not read) are NOT FOUND in this corpus.
- **No pledge disclosure captured.** AR p.150 (Note 19.5, promoter shareholding) carries no
  pledge column in the pulled extract. Pledge status is NOT FOUND, not confirmed nil.
- **Concall pages beyond what exists were not an issue** — the Q1FY27 transcript is only 14
  pages and all 14 were retrieved.
- No market cap or CMP held in the corpus (per framework, this is never sourced from the corpus).
  Market cap ~Rs 15,220 cr is given directly by the calling brief, sourced to the Bull AI screen,
  not to a document in this corpus; verify live.
