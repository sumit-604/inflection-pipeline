# Corpus manifest: WENDT (Wendt (India) Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE WENDT. BSE 505412. ISIN INE274C01019.
Bull AI market cap field: Rs 1,651.16 cr (undated, verify live).
Operator: Keerti Kaushik.

## Collection status: BLOCKED (no document text held)

Two collection routes both failed this session.

1. Direct download. The container has no egress. The proxy answered 403 to
   CONNECT for docs.bull-ai.in, www.bseindia.com and www.screener.in.
   Verified 2026-09-10 10:22 UTC via `/__agentproxy/status`.
2. Bull AI text readers. `search_company_documents` returned
   "tool temporarily unavailable" on every attempt. `get_document_chunks`
   returned "did not complete before its deadline" on every attempt, by
   identifier+subcategory and by document_id alike.

Working Bull AI tools this session: `search_companies`,
`list_document_availability`, `get_company_guidance`,
`get_company_corporate_actions`, `get_company_counterparties`,
`get_mcp_usage`. These give metadata and management quotes, not document text.

`get_company_guidance` returned zero records for WENDT. Bull AI holds no
extracted management guidance or delivery quotes for this company.

## What Bull AI indexes (availability map, free call, 2026-09-10)

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Financial results | Financial Results | FY26 Q4 | 2026-04-24 |
| Financial results | Financial Results | FY24 Q1 - FY26 Q3 | to 2026-01-21 |
| Investor presentation | Investor Presentation | FY25 Q4 (7 docs) | 2025-05-03 |
| Investor presentation | Investor Presentation | FY25 Q3 (5 docs) | 2025-03-03 |
| Other | Acquisition | FY27 Q1 (2 docs) | 2026-06-23 |
| Other | Disclosure under SEBI Takeover Regulations | FY27 Q1 | 2026-06-19 |
| Other | Reply to Clarification - Financial results | FY26 Q4 | 2026-02-02 |
| Other | Retirement | FY27 Q1 (2 docs) | 2026-05-30 |
| Other | Change in Directorate / General | FY27 Q1-Q2 | to 2026-08-04 |
| Annual report | Annual Secretarial Compliance Report | FY24 Q1 | 2023-05-30 |

No earnings call transcript of any period is indexed. Investor presentations
stop at FY25 Q4 (May 2025), sixteen months before this read.

## Held on disk

Nothing. No guidance extract file, because Bull AI holds no guidance for WENDT.

## Gaps and which step each weakens

- No document text at all. Weakens every numeric step.
- FRESHNESS GAP. The newest indexed result is Q4 FY26, uploaded 2026-04-24.
  A Q1 FY27 result would have been filed around July 2026. It is absent from
  the Bull AI map. Step 5 and step 8 cannot see the latest quarter.
- No transcript exists in the index for any period. Step 6 has no management
  claim to quote. The framework's "KEEP where a transcript exists" does not
  fire.
- No Reg. 34(1) annual report in the map. Step 3 and step 4 lose their
  primary source.
- No credit rating indexed. Step 10 NOT FOUND. Looked for: Bull AI
  availability map. Agency sites unreachable (no egress).
- LIVE EVENT, unread. Two acquisition filings (2026-06-23) and a SEBI
  Takeover Regulations disclosure (2026-06-19). An acquisition or a change in
  control may be in progress. This is the single most load-bearing unread
  document for this name.
- An exchange clarification on the Q3 FY26 results was answered on
  2026-02-02. Surface it at step 9 once readable.
