# Corpus manifest: KROSS (Kross Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE KROSS. BSE 544253. ISIN INE0O6601022.
Bull AI market cap field: Rs 1,416.63 cr (undated, verify live).
Operator: Keerti Kaushik.

## Collection status: BLOCKED (no document text held)

Two collection routes both failed this session.

1. Direct download. The container has no egress. The proxy answered 403 to
   CONNECT for docs.bull-ai.in, www.bseindia.com and www.screener.in.
   Verified 2026-09-10 10:22 UTC via `/__agentproxy/status`.
2. Bull AI text readers. `search_company_documents` returned
   "tool temporarily unavailable" on every attempt. `get_document_chunks`
   returned "did not complete before its deadline" on every attempt, by
   identifier+subcategory and by document_id alike. Tried 6 times.

Working Bull AI tools this session: `search_companies`,
`list_document_availability`, `get_company_guidance`,
`get_company_corporate_actions`, `get_company_counterparties`,
`get_mcp_usage`. These give metadata and management quotes, not document text.

## What Bull AI indexes (availability map, free call, 2026-09-10)

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Annual report | Reg. 34 (1) Annual Report | FY26 | 2026-08-20 |
| Annual report | Reg. 34 (1) Annual Report | FY25 | 2025-03-31 |
| Earnings call transcript | Earnings Call Transcript | FY27 Q1 | 2026-07-29 |
| Earnings call transcript | Earnings Call Transcript | FY26 Q1-Q4 | to 2026-05-16 |
| Earnings call transcript | Earnings Call Transcript | FY25 Q2-Q4 | to 2025-05-01 |
| Investor presentation | Investor Presentation | FY27 Q1 | 2026-07-25 |
| Investor presentation | Investor Presentation | FY25 Q2 - FY26 Q4 | to 2026-05-12 |
| Financial results | Financial Results | FY27 Q1 | 2026-07-24 |
| Financial results | Financial Results | FY25 Q1 - FY26 Q4 | to 2026-05-12 |
| Monitoring agency report | Monitoring Agency Report | FY27 Q1 | 2026-05-12 |
| Other | RHP | FY27 Q1 | 2026-04-10 |
| Other | Resignation of Director | FY27 Q2 | 2026-07-24 |
| Other | Shareholders meeting | FY27 Q2 | 2026-08-31 |

Coverage is the best of the six names. Transcripts, presentations and results
all run to Q1 FY27. The FY26 annual report is indexed.

## Held on disk

Nothing. `bullai-guidance.md` holds page-cited management quotes from
`get_company_guidance`. That is management claim evidence, not document text.

## Gaps and which step each weakens

- No document text at all. Weakens every step that needs a number:
  step 5 financial trajectory, step 4 promoters (holding and pledge),
  step 9 flags (related-party, auditor, dilution), step 2 revenue mix.
- No credit-rating rationale indexed by Bull AI. Step 10 is NOT FOUND.
  Looked for: Bull AI availability map, subcategory "Credit Rating". Absent.
  Agency sites unreachable (no egress).
- RHP dated FY27 Q1 (2026-04-10) is later than the September 2024 listing.
  Treat the date as an index artefact, not a fresh offer document.
