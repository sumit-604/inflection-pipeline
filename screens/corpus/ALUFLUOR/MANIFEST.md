# Corpus manifest: ALUFLUOR (Alufluoride Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Alufluoride Ltd., BSE 524634, NSE ALUFLUOR, ISIN INE058F01019.

## Method note
Per the shallow-analysis brief and the 2026-09-08 operator ruling recorded in
`screens/README.md`, the corpus is built from the Bull AI MCP (`list_document_availability`,
`search_company_documents`, `get_document_chunks`). No PDF is held on disk; the files below
are page-marked text pulled through Bull AI, using the source PDF's own page numbers so a
citation can be traced back.

## Files
| File | Source document | Pages held | Bull AI document_id |
|---|---|---:|---|
| annual_reports/ALUFLUOR-AnnualReport-FY2025-2025-03-31.txt | Reg. 34(1) Annual Report FY2024-25 (year ended 31-03-2025) | 1-15, 30-42 (full page text) | 533dc071-2377-4d02-a21d-cde2d3176a45 |
| results/ALUFLUOR-Results-FY2026Q4-2026-05-22.txt | Audited Standalone & Consolidated Financial Results, quarter and year ended 31-03-2026 | 1-9 (full page text) | 18a9cb74-e03f-4cf4-843b-6cb7c62a0bad |
| bullai-extracts.md | search_company_documents snippets against the FY2025 Annual Report and other filings (promoter shareholding, related party, CWIP, market price, credit-rating search) | selected pages: 43, 78, 97, 104, 134, 140, 157, 159 (partial, tool-generated excerpts, not full page reads) | 533dc071-2377-4d02-a21d-cde2d3176a45 (all) |

## What is NOT held
- **No earnings-call transcript exists.** `search_company_documents` with
  `doc_types: ["transcript"]` returned zero results. Confirmed against
  `list_document_availability`, which lists no transcript document type for this
  company at all. Step "concall" throughout the card is NOT FOUND; no transcript to cite.
- **No investor presentation exists.** `search_company_documents` with
  `doc_types: ["presentation"]` returned zero results. `list_document_availability`
  lists no presentation document type either.
- **No FY2026 Annual Report yet.** `list_document_availability` shows the latest
  Reg. 34(1) Annual Report as FY2025 (year ended 31-03-2025). The FY2026 annual report
  (year ended 31-03-2026) is not yet indexed in Bull AI as of the retrieval date.
- **No Q1FY27 (quarter ended 30 June 2026) results filing indexed.** Searched with
  `fiscal_year=2027, quarter=1` and without period filters; no such document returned.
  The latest indexed financial result is the audited FY2026 Q4/full-year result filed
  22 May 2026. The Q4FY26 vs Q3FY26 (unaudited) columns inside that one filing are used
  for the "last two quarters" comparison the framework's step 5 asks for.
- **No credit-rating rationale.** Searched "credit rating CRISIL ICRA CARE India
  Ratings Acuite" against the full Bull AI document set for this company; no rating
  document returned (see bullai-extracts.md for the search detail). This container has
  no live-web access to CRISIL, ICRA, CARE, India Ratings or Acuité sites, so those were
  not independently checked. Step 10 is NOT FOUND; looked for on Bull AI and named on
  the four agency sites, all unreachable.
- **No management guidance documents.** `get_company_guidance` returned zero records
  (`total_records: 0`). No forward guidance to cite from that tool.
- Consolidated financial statements beyond the balance sheet snippet on page 17 of the
  FY26 results filing (seen via the credit-rating search) were not separately pulled;
  the card relies on standalone figures, which for this company are close to
  consolidated (the wholly owned Singapore subsidiary appears small and largely dormant
  after the Jordan JV withdrawal).
- Annual Report pages 16-29 and 43 onward (financial statements, full notes, auditor's
  report, business responsibility report) were not read page by page; only the
  snippet-level citations in bullai-extracts.md cover selected pages in that range.

## Metered call count
14 metered Bull AI calls used (of the brief's 14-call hard cap):
1. search_company_documents, doc_types=[transcript] — confirmed no transcript.
2. search_company_documents, doc_types=[presentation] — confirmed no presentation.
3. search_company_documents, MD&A/chairman letter query, FY2025 annual_report — located AR document_id and MD&A page.
4. search_company_documents, credit rating query — confirmed none found.
5. get_company_guidance — confirmed zero guidance records.
6. search_company_documents, Q1FY27 company_update query — empty.
7. search_company_documents, general query for June 2026 quarter results — confirmed latest indexed result is FY26 Q4 (year end), no Q1FY27 filing yet.
8. get_document_chunks, AR pages 1-15.
9. search_company_documents, promoter shareholding/pledge query — located shareholding tables.
10. search_company_documents, expansion/capex query — located CWIP history and the Jordan JV withdrawal reference.
11. get_document_chunks, Results FY2026Q4 pages 1-9.
12. get_document_chunks, AR pages 30-42 — full MD&A text, governance, related-party list.
13. search_company_documents, related-party transactions query — located RPT tables.
(list_document_availability and get_company_classification were free and not counted.)

`list_document_availability` and `get_company_classification` used freely (free tier),
not counted in the 14.

## Market cap / CMP
NOT FOUND in the Bull AI corpus. Per the operator brief, market cap is ~Rs 384 cr per
Bull AI screen (micro cap); verify CMP live. The Annual Report page 43 snippet in
bullai-extracts.md carries FY2024-25 monthly high/low BSE prices, which is historical
trading range, not a current price.
