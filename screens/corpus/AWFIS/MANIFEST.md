# Corpus manifest: AWFIS (Awfis Space Solutions Ltd)

Collected 2026-09-11 via Bull AI MCP (get_document_chunks, get_company_market_transactions).
Operator: Keerti Kaushik.
Company resolved: Awfis Space Solutions Ltd., BSE 544181, NSE AWFIS, ISIN INE108V01019.
Market cap Rs 1,788 crore per the Bull AI company screen, 11-Sep-2026. Verify CMP live.

## Method note
No egress in this session. The proxy denied the CONNECT to docs.bull-ai.in, screener.in,
BSE and every rating agency site (403). No PDF is held. The files below are page-marked
text pulled through the Bull AI chunk reader; the page numbers are the source PDF's own,
so a citation can still be opened. This follows the operator ruling recorded for the
2026-09-08 run in screens/README.md.

Second constraint, new to this run: Bull AI's `search_company_documents` tool returned
"temporarily unavailable" on every attempt, for the whole session. Documents could
therefore only be reached by category and period, not by query. Long documents such as
annual reports could not be targeted at all.

| File | Source document | Pages held | Bull AI document_id |
|---|---|---:|---|
| presentations/AWFIS-IP-Q1FY27-2026-08-13.txt | Investor presentation Q1 FY27, filed 2026-08-13 | extract of 5, 7, 8, 9, 12, 13, 14, 19, 20, 21, 23, 24, 26, 30, 33 of 38 | 64308dba-6e9f-46a9-bd51-246e5e76dbe6 |
| concalls/AWFIS-Concall-Q1FY27-2026-08-13.txt | Q1 FY27 earnings call, held 2026-08-13, filed 2026-08-19 | extract of 3-17 of 17 (all substantive pages read) | a6d85ed8-3fdb-4ad9-baaf-6286b78bbef1 |
| market/AWFIS-insider-transactions.txt | Exchange insider transactions, 2 records | n/a | n/a (tool output) |

Every page of both documents was read. The files hold the load-bearing passages, not the
full text; picture pages and boilerplate were dropped.

## Coverage gaps
- No annual report. Bull AI holds FY26 (filed 2026-08-27) but without document search a
  250-plus page report cannot be targeted, and blind paging is not affordable. This is the
  single largest gap: it removes promoter holding, pledge, the related-party schedule,
  auditor commentary, and the full cash flow statement. Steps 4 and 9 are weakened.
- No credit-rating rationale. The presentation states an A+ (Stable) rating from Fitch
  India (page 8, page 24), upgraded from A in May 2025, but the rationale itself is not in
  Bull AI and the agency sites are blocked. Step 10 is PARTIAL: a grade without a rationale.
- No standalone quarterly results filing. The numbers come from the company's own
  presentation and call, both of which carry the MSKA agreed upon procedures note for the
  cash EBITDA reconciliation.
- No shareholding pattern, so promoter holding and institutional holding are NOT FOUND.
