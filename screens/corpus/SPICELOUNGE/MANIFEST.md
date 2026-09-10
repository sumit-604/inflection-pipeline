# Corpus manifest: SPICELOUNGE (Spice Lounge Food Works Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
BSE 539895. No NSE listing. ISIN INE631E01024.
Bull AI market cap field: Rs 2,083.70 cr (undated, verify live).
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

`get_company_guidance` returned zero records for SPICELOUNGE.
`get_company_corporate_actions` returned zero records. Bull AI holds no
extracted management guidance and no recorded corporate action for this
company, although the filing index shows a Change of Name in FY26 Q2.

## What Bull AI indexes (availability map, free call, 2026-09-10)

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Annual report | Reg. 34 (1) Annual Report | FY25 | 2025-03-31 |
| Financial results | Financial Results | FY27 Q1 (2 docs) | 2026-08-14 |
| Financial results | Financial Results | FY26 Q3 | 2026-02-14 |
| Financial results | Financial Results | FY26 Q1 | 2025-08-14 |
| Financial results | Financial Results | FY23 Q2 - FY25 Q4 | to 2025-05-28 |
| Other | Change of Name | FY26 Q2 | 2025-08-08 |
| Other | Change in Registered Office Address | FY26 Q2 | 2025-07-30 |
| Other | Change in Directorate | FY26 Q2 | 2025-09-19 |
| Other | Resignation of Managing Director | FY23 Q1 | 2022-05-19 |
| Other | General (company updates) | FY27 Q1 (5 docs) | 2026-06-02 |
| AGM/EGM | EGM | FY26 Q1 (4 docs) | 2025-06-30 |
| Insider Trading / SAST | Disclosures under Reg. 29(2) SAST | FY26 Q1 (2 docs) | 2025-06-24 |
| Other | Revision of outcome | FY26 Q3 | 2025-11-15 |

No earnings call transcript of any period is indexed. No investor
presentation of any period is indexed.

## Held on disk

Nothing. No guidance extract file, because Bull AI holds no guidance for
SPICELOUNGE.

## Gaps and which step each weakens

- No document text at all. Weakens every numeric step.
- No transcript and no presentation, ever. Steps 6 and 7 have no management
  claim to quote and no dated trigger to register.
- QUARTERS MISSING FROM THE INDEX. The Financial Results run shows FY26 Q1
  and FY26 Q3 but not FY26 Q2 or FY26 Q4. Either the filings are absent or
  Bull AI did not index them. Step 5 cannot build a continuous quarterly line
  without checking BSE directly.
- No FY26 annual report. The newest is FY25.
- No credit rating indexed. Step 10 NOT FOUND. Looked for: Bull AI
  availability map. Agency sites unreachable (no egress).
- UNREAD SIGNALS, and they cluster. A Change of Name (2025-08-08), a change
  of registered office (2025-07-30), a change in directorate (2025-09-19),
  four EGM filings (to 2025-06-30) and two SAST Reg. 29(2) disclosures
  (2025-06-24) all fall inside four months of 2025. A renamed shell, a
  control change, or a reverse merger all produce this pattern. Nothing here
  confirms which. Load-bearing for steps 2, 4 and 9.
- SIZE FLAG. Bull AI reports a market cap of Rs 2,083.70 cr against a company
  with no investor presentation, no transcript, no credit rating and no NSE
  listing. Confirm the market cap live before any further work.
