# Corpus manifest: MERCURYEV (Mercury Ev-Tech Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE MERCURYEV. BSE 531357. ISIN INE763M01028.
Bull AI market cap field: Rs 713.16 cr (undated, verify live).
Operator: Keerti Kaushik.

NAME FLAG. Bull AI carries the short name "Mercury Metals" against the full
name "Mercury Ev-Tech Ltd." on the same ISIN. The company was renamed. Read
the pre-rename history as a different business before crediting any EV record.

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

`get_company_guidance` returned zero records for MERCURYEV.
`get_company_counterparties` returned zero records. Bull AI holds no
extracted management guidance, delivery quotes, or disclosed customers and
suppliers for this company.

## What Bull AI indexes (availability map, free call, 2026-09-10)

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Annual report | Reg. 34 (1) Annual Report | FY25 | 2025-03-31 |
| Annual report | Reg. 34 (1) Annual Report | FY24 | 2024-03-31 |
| Annual report | Reg. 34 (1) Annual Report | FY23 | 2023-03-31 |
| Financial results | Financial Results | FY26 Q4 | 2026-05-31 |
| Financial results | Financial Results | FY23 Q3 - FY26 Q3 | to 2026-02-12 |
| Monitoring agency report | Monitoring Agency Report | FY27 Q2 | 2026-08-14 |
| Monitoring agency report | Monitoring Agency Report | FY25 Q4 - FY27 Q1 | to 2026-05-15 |
| Other | Outcome of Board Meeting | FY27 Q2 | 2026-08-31 |
| Other | Updates | FY27 Q2 | 2026-08-13 |
| Corp. Action | Record Date | FY27 Q2 | 2026-08-31 |
| Other | General (company updates) | FY27 Q1 (6 docs) | 2026-06-25 |
| AGM/EGM | Postal Ballot | FY26 Q4 (3 docs) | 2026-02-13 |

No earnings call transcript of any period is indexed. No investor
presentation of any period is indexed.

## Held on disk

Nothing. No guidance extract file, because Bull AI holds no guidance for
MERCURYEV.

## Gaps and which step each weakens

- No document text at all. Weakens every numeric step.
- No transcript and no presentation, ever. Steps 6 and 7 have no management
  claim to quote and no dated trigger to register.
- FRESHNESS GAP. The newest indexed result is Q4 FY26, uploaded 2026-05-31.
  A Q1 FY27 result would have been filed around August 2026. It is absent
  from the Bull AI map, although an Outcome of Board Meeting dated 2026-08-31
  and an Update dated 2026-08-13 are indexed. Step 8 cannot see the latest
  quarter.
- No FY26 annual report. The newest is FY25.
- No credit rating indexed. Step 10 NOT FOUND. Looked for: Bull AI
  availability map. Agency sites unreachable (no egress).
- UNREAD SIGNALS. A continuous run of Monitoring Agency Reports from FY25 Q4
  to FY27 Q2. A monitoring agency reports on the use of raised funds. This
  company has been raising and deploying capital across the whole window.
  Load-bearing for steps 4, 5 and 9. Three postal ballots in FY26 Q4 point
  to shareholder approvals in the same window.
