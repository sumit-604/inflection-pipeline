# Corpus manifest: KRMAYURVED (KRM Ayurveda Ltd)

Collected 2026-09-11 via Bull AI MCP (get_document_chunks, get_company_market_transactions).
Operator: Keerti Kaushik.
Company resolved: KRM Ayurveda Ltd., NSE KRMAYURVED, ISIN INE1MTV01019. No BSE code.
CIN L24239DL2019PLC354658. Listed January 2026; the monitoring agency calls the issue an
SME IPO of Rs 77.49 crore, while Bull AI's screen flags the scrip nse_sme false. Not
resolved here; verify the segment live.
Market cap Rs 625 crore per the Bull AI company screen, 11-Sep-2026. Verify CMP live.

## Method note
No egress in this session; the proxy denied the CONNECT to docs.bull-ai.in, NSE and
screener.in (403). No PDF is held. The files below are page-marked text pulled through the
Bull AI chunk reader. Bull AI's `search_company_documents` tool was unavailable for the
whole session.

| File | Source document | Pages held | Bull AI document_id |
|---|---|---:|---|
| presentations/KRM-IP-FY26-2026-06-22.txt | Investor presentation FY26, filed 2026-06-22 | extract of 5-36 of 36 (every page read) | 822c6284-8cfc-406a-8caf-ca41d3841a95 |
| filings/KRM-NSE-clarification-2026-07-27.txt | Reply to NSE clarification on FY26 results, filed 2026-07-27, with the 13-May, 19-May and 18-Jun letters and the auditor working-capital certificate | 1-6 (complete) | 2bfcead0-e920-4a3c-b14f-ca1e10d33491 |
| filings/KRM-monitoring-agency-Q1FY27-2026-08-13.txt | CARE Ratings Monitoring Agency Report, quarter ended 30-Jun-2026, filed 2026-08-13 | 1-11 (all substantive) | 441e55ca-66ea-4073-baa7-a4a0e96b93b8 |
| market/KRM-market-transactions.txt | Exchange insider and bulk deals, latest 15 of 25 | n/a | n/a (tool output) |

## Reader defects found in this corpus
- The investor presentation pages 4 and 12 returned invented text from the Bull AI reader
  (a Nairobi-headquartered agriculture company; an unrelated Bangalore contact block).
  Recorded in the extract file, quoted nowhere, used nowhere.
- The FY26 earnings call transcript is indexed twice (document_id
  d908f605-7b2a-4e6f-bd3f-d1b18a83a7c4, filed 2026-05-11) but the reader returns zero
  chunks for it. No management Q&A is held. This is the same empty-document defect the
  2026-09-08 run recorded for other names.
- The "Change in Management" filing of 2026-08-31 (document_id
  18ff4c7b-6b10-42a7-b25e-2f11d956383a) also returns zero chunks. A management change six
  weeks ago is unread. Named as a gap on the card.

## Coverage gaps
- No quarterly results filing. Bull AI carries none for this company, so there is no
  June-2026 quarter and no half-yearly statement in the corpus. All FY26 figures come from
  the company's own presentation, cross-checked where possible against the auditor's
  working-capital certificate, which reconciles.
- No annual report, no shareholding pattern, no related-party schedule, no prospectus.
  The prospectus matters here: the deck's YouTube page attributes the "Karma Ayurveda"
  brand to a centre "Established in 1937", while the listed company was incorporated in
  2019. Who owns the brand, and on what terms the listed entity uses it, is NOT FOUND.
- No credit rating. CARE appears only as IPO monitoring agency, which is not a rating view
  on the business. Step 10 is served by the monitoring report instead, and that report is
  the most important document in this corpus.
