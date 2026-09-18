# Corpus manifest: CSM (CSM Technologies Ltd.)

Collected 2026-09-18 via Bull AI MCP (list_document_availability, search_company_documents,
get_document_chunks, get_company_guidance, get_company_classification). Operator: Keerti
Kaushik. Company resolved: CSM Technologies Ltd., BSE 544806, NSE CSM, ISIN
INE0ZK601013. Bull AI classification: Information Technology / IT Services / Software,
company_category "General".

## Method note
No egress to docs.bull-ai.in, BSE, screener.in or the rating agency sites in this
session; the proxy denies the CONNECT. No PDF is held. Files below are page-marked text
of the filed PDFs pulled through the Bull AI chunk reader (`get_document_chunks`,
marked `[CHUNK]` inside the file) and, where a broader chunk pull hit the tool's
response-size limit, through `search_company_documents` result snippets (marked
`[SNIPPET]`, shorter but still the tool's own retrieved page text, not a paraphrase).
CSM listed on NSE/BSE in 2026; no earnings-call transcript existed before Q4 FY26
(the Company's first call was 28 July 2026, its first as a listed company). No
investor-presentation doc_type was found for this company in Bull AI's inventory.

## Metered call count: 13 of 14
1. get_company_guidance (zero periods returned; no guidance documents indexed for CSM)
2. search_company_documents - business overview / revenue segments
3. search_company_documents - financial summary / EBITDA / PAT / ROCE
4. search_company_documents - credit rating CARE
5. search_company_documents - promoter shareholding / pledge
6. search_company_documents - order book / pipeline / growth
7. search_company_documents - related party / litigation / auditor
8. search_company_documents - quarterly results Q4 FY26
9. get_document_chunks batch (5 requests, RHP + General doc + Press Release) - FAILED,
   response too large; no data returned, still counted as metered.
10. get_document_chunks batch (5 requests, RHP shareholding pages 108-115) - only the
    first request's pages (108-115) came back; the other 4 requested ranges
    (KPI 149-153, credit rating 133-137, segment revenue 238-245, risk factors 60-65)
    were silently dropped from the response, likely the same size-limit behaviour.
    Those pages were separately recovered via search snippets in call 3-8's results
    or a later targeted search (call 13).
11. get_document_chunks (General doc pages 1-8 + RHP business overview pages 29-33) - OK
12. get_document_chunks (Press Release pages 1-6 + RHP financial summary pages 84-90) - OK
13. search_company_documents - ROCE / ROE / net worth / debt-equity ratio table
(list_document_availability and get_company_classification are free per Bull AI's
usage policy and are not counted in the 14-call cap.)

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/CSM-Concall-Q4FY26-2026-07-28.txt | Q4 & FY26 earnings call transcript, held 28 Jul 2026, filed 31 Jul 2026 (Company's first call, post-listing) | 1-8 (chunk read) | 50568a75-c4be-44cc-8f08-3fd4d51ccc22 |
| filings/CSM-PressRelease-Q1FY27-2026-08-14.txt | Q1 FY27 results press release, filed 14 Aug 2026 | 1-5, full document (chunk read) | 9458db94-b511-432d-a682-1c813fd218cb |
| filings/CSM-RHP-FY2027Q2-2026-07-02.txt | Red Herring Prospectus, filed 2 Jul 2026 (~500 pages; only headline sections pulled) | 29-33, 84-90, 108-115 (chunk read, full); 40-46, 60-65, 70, 133-137, 146, 149-153, 155, 238-245, 375, 421, 425 (search snippet, partial) | a2268144-316f-4e64-a195-7b3eba93bada |

## Documents available in Bull AI but NOT read (out of budget)
- DRHP (document_id 859d1f87-3254-484d-b3e5-8febeccf6122, filed 17 Jun 2026): an earlier
  draft of the same disclosures. Used only incidentally where search results surfaced it
  (e.g. Note 49 ratios, one year lagged); the RHP supersedes it and was preferred.
- PROSPECTUS (two document_ids, 49ced728... and 6c1ae8b9..., filed 2 Jul 2026): the
  listing prospectus, largely duplicative of the RHP; used only for the credit-rating
  table which matched the RHP's own page 135 exactly.
- Board Meeting outcome filings (Q1 FY27, Q4/FY26, Q2 FY27): not read; likely duplicate
  the Result and Press Release content already held.
- Company Update - "Awarding of order(s)/contract(s)" (1 document, FY27 Q2): not read.
  This may hold order-win detail beyond what the Q1 FY27 press release names (the World
  Bank Malawi contract). Priority for a deep run.
- Company Update - "Code of Conduct under SEBI (PIT) Regulations" (1 document): not
  read, standard compliance filing, low priority.
- Corp. Action - "Dividend" (1 document, filed 21 Jul 2026): not read; the Rs 0.5/share
  FY26 final dividend is already known from the concall (page 7 of the held transcript).
- Company Update - "Updates" (3 documents, FY27 Q2): not read.
- Result - "Financial Results" (1 document, FY26 Q4, filed 21 Jul 2026): the underlying
  results filing (as opposed to the press release/concall gloss on it) was not read
  directly; the standalone/consolidated P&L lines quoted in this corpus come from the
  concall transcript and the Q1 FY27 press release's comparative Q4 FY26 column, not
  from this primary filing. A deep run should read this document directly.

## Coverage gaps
- No investor presentation exists in Bull AI's inventory for this company at all
  (no `presentation` doc_type record). Recently listed; may not have published one yet.
- No annual report exists yet (FY26 would be the Company's first as a listed entity;
  none indexed in Bull AI).
- No credit-rating RATIONALE document (the reasoning behind CARE BBB/A3+). Only the
  rating grade itself, as reproduced in the RHP (page 135), is held. Looked for
  specifically via a "credit rating" search across all doc types; nothing beyond the
  RHP/Prospectus table came back. Also looked for on the CRISIL, ICRA, CARE and India
  Ratings agency sites directly, which this session cannot reach (network policy denies
  the connection). Step 10 is PARTIAL: the rating grade is known and unchanged
  2025-to-2026; the rationale behind it is NOT FOUND.
- The RHP is roughly 500 pages; this corpus holds page-marked text for well under a
  fifth of it (business overview, risk-factor highlights, restated financial
  statements, shareholding, credit rating table, ratio note, litigation summary, KPI
  table). Sections NOT read at all: full "Our Business" narrative (pages 227-302,
  referenced repeatedly but not pulled), Industry Overview (153+), full MD&A (378+),
  Related Party Transactions detail (only the risk-factor summary line was seen, not
  the full schedule), Board and Key Management Personnel bios, Objects of the Issue
  detail beyond the credit-rating/borrowings table, and the full Restated Notes.
- No standalone-only restated financial statements were read; the restated tables held
  here are CONSOLIDATED. Standalone Q1 FY27 and Q1 FY26 figures came only from the
  press release's standalone highlights box.
- Market cap and live CMP: not in the corpus (the brief gives ~Rs 530 cr per Bull AI
  screen; not independently verified here). Verify live.
- Two `get_document_chunks` calls did not fully deliver: one errored outright
  ("response exceeds its response limit") and a second returned only 1 of 5 requested
  page ranges without an error. Both are recorded above; the missing ranges were
  recovered via search snippets where possible, but this means some RHP pages in this
  corpus are shallower excerpts than a full chunk read would give.
