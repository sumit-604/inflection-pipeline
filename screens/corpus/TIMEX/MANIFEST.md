# Corpus manifest: TIMEX (Timex Group India Ltd)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Timex Group India Ltd., BSE 500414, NSE TIMEX, ISIN INE064A01026.

## Method note
This container has no egress to docs.bull-ai.in, BSE, screener.in or rating-agency sites.
No PDF is held. Every file below is page-marked text pulled through the Bull AI
get_document_chunks / get_company_guidance tools, citing the source PDF's own page
numbers so a cite can be traced back to the filed document.

## Files

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| presentations/TIMEX-InvestorPresentation-Q4FY26-2026-05-26.txt | Investor Presentation, Q4 and FY 2025-26, filed 2026-05-26 | 1-51 (full document) | f7e02187-e732-47e1-a5fa-9ef657b75a27 |
| annual_reports/TIMEX-AnnualReport-FY2025-2025-03-31.txt | Reg. 34(1) Annual Report, FY2024-25 | 21, 40, 41, 55, 81, 108-112, 114 (targeted, not full ~114+ pp document) | 8eefd104-2836-4b8b-b942-ebfcbbe9105d |
| filings/TIMEX-Guidance-BullAI-2026-09-18.txt | get_company_guidance tool output, sourced from the above investor presentation plus two Covid-era FY21 concall-linked filings | n/a (tool citations preserved) | primary: f7e02187...; secondary FY21: ddb204e6-1174-45a0-9784-30cc75e82206, 45edc85d-8596-467a-9e3c-a3995093012a |

## Bull AI call count: 14 metered calls (plus 3 free list_document_availability /
get_company_classification-style lookups, which do not count against the cap)
1. get_company_classification (sector/industry)
2. search_company_documents, doc_types=[transcript], query "management commentary
   quarterly results" — 0 results, no transcript indexed under that filter
3. get_company_guidance — returned FY2026 and FY2021 periods
4. search_company_documents, fiscal_year 2025 quarter 4, query "earnings call transcript
   management discussion" — surfaced Annual Report FY2025 and Financial Results FY2025 Q4
   document_ids, no transcript
5. search_company_documents, doc_types=[annual_report], query "MD&A chairman letter
   segment revenue promoter shareholding" — surfaced AR FY2025, FY2024, FY2023 document_ids
6. search_company_documents, fiscal_year 2025 quarter 4, query "Management Discussion and
   Analysis industry overview business segments outlook" — no distinct MD&A section
   surfaced
7. search_company_documents, query "credit rating CRISIL ICRA CARE bank facilities" — no
   rating-agency document; surfaced AGM/OFS/general filings and one borrowings note page
8. search_company_documents, query "Q1 FY27 results revenue EBITDA quarter ended June
   2026" — no FY2027 Q1 document indexed; confirmed FY2026 Q4 (year ended 31 Mar 2026) is
   the latest filed period Bull AI holds
9. get_document_chunks, investor presentation pages 1-25 — succeeded, 20 chunks
10. get_document_chunks, annual report pages 1-25 + 95-114 in one multi-request call —
    ERRORED ("response exceeds limit"); no data returned, page ranges reduced on retry
11. get_document_chunks, investor presentation pages 21-40 — succeeded, 20 chunks
12. get_document_chunks, investor presentation pages 41-51 — succeeded, 11 chunks (end of
    document)
13. get_document_chunks, annual report pages 108-112 — succeeded, 5 chunks
14. get_document_chunks, identifier+category+subcategory form (attempt to fetch the
    Q4FY25 "Earnings Call Transcript" record directly) — REJECTED by input validation
    ("arguments do not match the public tool contract"); no transcript retrieved, budget
    exhausted at this point so not retried with a different call shape

## Coverage gaps
- No earnings-call transcript held. list_document_availability shows exactly one
  concall record (Company Update / Earnings Call Transcript, FY2025 Q4, filed
  2025-05-01), but two search attempts and one direct-fetch attempt did not retrieve it
  inside the 14-call budget. All management quotes in the card instead come from the
  Q4FY26 investor presentation (page-cited), which does carry the MD's own words.
- No FY2027 Q1 (quarter ended 30 June 2026) results or presentation found. The latest
  filed period this corpus holds is FY2025-26 full year / Q4 (board meeting 26 May 2026).
  Today is 2026-09-18; a Q1FY27 filing would normally be out by mid-August 2026 but is not
  indexed by Bull AI as of this run. Flagged as a gap, not assumed to be a delay.
- No credit-rating rationale. Searched explicitly; Bull AI carries none, and CRISIL, ICRA,
  CARE, India Ratings and Acuité sites are all unreachable from this container. Step 10 is
  NOT FOUND.
- Annual report FY2025 was read only at targeted pages (21, 40, 41, 55, 81, 108-114), not
  in full. No MD&A narrative, chairman's letter, related-party schedule, or promoter
  pledge disclosure was retrieved. The related-party and pledge gap weakens step 4 and
  step 9; the MD&A gap weakens step 2's non-financial detail (offset partly by the
  investor presentation's business-model slides).
- No standalone or consolidated profit and loss statement in full (only the summary
  income/EBITDA/PBT figures from the investor presentation and the retained-earnings
  roll-forward from the annual report notes). Balance sheet, cash flow statement and ROCE
  are NOT FOUND.
- Market cap: no explicit "Rs X cr" figure sourced in this corpus; the investor
  presentation gives market capitalisation by year-end (Mar-26: Rs 2,47,328 lakhs =
  Rs 2,473 cr) which does not match the brief's stated screen figure of ~Rs 6,171 cr.
  The card uses the brief's screen figure per instruction and flags the discrepancy
  against the corpus figure; live CMP must be verified.

## Addendum 2026-09-19 (step 5A)
| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---|---|
| results/TIMEX-Results-FY2026Q4-2026-05-26.txt | Audited FY26 results with the FY26 press release, uploaded 2026-05-26 | 10 | f5025c25-f53c-4303-91f5-4ff691246367 |
Two more metered calls (one search, one chunk read) to get FY26 PAT, Rs 7,544 lakh.
Bull AI still indexes no June-2026 quarter result for TIMEX as of 2026-09-19.
