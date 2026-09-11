# Corpus manifest: VENKEYS (Venky's (India) Ltd)

Collected 2026-09-11 via Bull AI MCP (get_document_chunks, get_company_market_transactions).
Operator: Keerti Kaushik.
Company resolved: Venky'S (India) Ltd., BSE 523261, NSE VENKEYS, ISIN INE398A01010.
Market cap Rs 2,403 crore per the Bull AI company screen, 11-Sep-2026. Verify CMP live.
Shares outstanding 1.409 crore (paid-up capital Rs 1,409 lakh at Rs 10 face value).

## Method note
No egress in this session; the proxy denied the CONNECT to docs.bull-ai.in, BSE and
screener.in (403). No PDF is held. The files below are page-marked text pulled through the
Bull AI chunk reader. Bull AI's `search_company_documents` tool was unavailable for the
whole session, so documents could be reached by category and period only.

| File | Source document | Pages held | Bull AI document_id |
|---|---|---:|---|
| results/VENKEYS-Results-Q4FY26-2026-05-14.txt | Audited results, quarter and year ended 31-Mar-2026, filed 2026-05-14 | 1-6 (complete) | 856d142b-ae4b-4398-809e-0362a0b7036f |
| concalls/VENKEYS-Concall-Q4FY26-2026-05-15.txt | Q4 FY26 earnings call, held 2026-05-15, filed 2026-05-21 | extract of 3-20 of 20 (all substantive pages read) | f3119216-8d4f-4a42-b2d7-dd10edcdbfff |
| market/VENKEYS-insider-transactions.txt | Exchange insider transactions, 6 records, all held | n/a | n/a (tool output) |

## Coverage gaps
- FRESHNESS GAP, and it is the important one. The newest results in this corpus are for the
  quarter ended 31-Mar-2026. Bull AI carries no FY2027 "Financial Results" document, so the
  June-2026 quarter is absent, four months after that quarter closed. The May-2026 call
  states that broiler realisation was falling from 10-11 May and that day-old chick prices
  had halved from Rs 55 to Rs 35. The quarter that tests those words is exactly the quarter
  this corpus does not hold. Step 8, the proof check, is weakened at its most load-bearing
  point.
- No investor presentation for FY26. The latest Bull AI presentation record is old and
  mislabelled (fiscal_year 2025 with a 2026-05-01 upload date). Not read.
- No credit-rating rationale. Bull AI carries none for Venky's and the agency sites are
  blocked. Step 10 is NOT FOUND. The results filing does state the company is not a Large
  Corporate borrower with NIL qualified borrowings, which is a fact, not a rating view.
- No annual report text. FY22 to FY25 reports are indexed but cannot be targeted without
  document search. Promoter holding, pledge, and the related-party schedule are NOT FOUND.
  This matters more than usual here: the CFO states receivables of Rs 544 crore "includes
  external as well as the group associates" and the oilseed division sells mostly to the
  group, so the related-party schedule is the document a deeper read must open first.
