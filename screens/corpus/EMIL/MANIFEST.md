# Corpus manifest: EMIL (Electronics Mart India Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE EMIL. BSE 543626. ISIN INE02YR01019.
Bull AI market cap field: Rs 7,023.59 cr (undated, verify live).
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

## What Bull AI indexes (availability map, free call, 2026-09-10)

Filtered to category "Company Update". Results and annual report categories
were not separately mapped this session.

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Earnings call transcript | Earnings Call Transcript | FY27 Q1 | 2026-05-27 |
| Earnings call transcript | Earnings Call Transcript | FY24 Q1 - FY26 Q4 | to 2026-05-01 |
| Investor presentation | Investor Presentation | FY27 Q1 | 2026-08-07 |
| Investor presentation | Investor Presentation | FY24 Q2 - FY26 Q4 | to 2026-05-22 |
| Credit rating | Credit Rating | FY26 Q3 (2 docs) | 2025-12-11 |
| Credit rating | Credit Rating | FY25 Q2 (2 docs) | 2024-08-08 |
| Credit rating | Credit Rating | FY24 Q2 (2 docs) | 2023-07-06 |
| Other | Reg. 32 (1),(3) Deviation & Variation | FY25 Q4 | 2025-02-10 |
| Concall transcript (analyst meet) | Transcript of Analysts/Inst. Investor Meet | FY23 Q3 | 2022-11-15 |
| Annual report | Annual Secretarial Compliance Report | FY24 Q1 | 2023-05-29 |

Coverage is the second best of the six. Transcripts and decks run to Q1 FY27.
A credit-rating document exists, dated 2025-12-11. This is the only one of the
six names where step 10 has a source indexed.

## Held on disk

Nothing. `bullai-guidance.md` holds page-cited management quotes from
`get_company_guidance`. That is management claim evidence, not document text.

## Gaps and which step each weakens

- No document text at all. Weakens step 5 financial trajectory, step 4
  promoters, step 9 flags, step 2 revenue mix by category.
- The credit-rating document is indexed but unreadable this session, so step
  10 is PENDING, not NOT FOUND. Looked for: Bull AI `get_document_chunks`
  on the Credit Rating subcategory. Reader down.
- The Reg. 34(1) annual report was not confirmed in this map, because the map
  was filtered to Company Update. Re-map before the next read.
