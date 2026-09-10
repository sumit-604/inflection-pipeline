# Corpus manifest: PANORAMA (Panorama Studios International Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE PANORAMA. BSE 539469. ISIN INE258R01028.
Bull AI market cap field: Rs 1,240.41 cr (undated, verify live).
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

`get_company_guidance` returned zero records for PANORAMA. Bull AI holds no
extracted management guidance or delivery quotes for this company.

## What Bull AI indexes (availability map, free call, 2026-09-10)

| Document | Subcategory | Latest period | Uploaded |
|---|---|---|---|
| Annual report | Reg. 34 (1) Annual Report | FY25 | 2025-03-31 |
| Annual report | Annual Disclosure by a Large Corporate: Annexure B2 | FY24 | 2023-05-15 |
| Annual report | Annual Disclosure by a Large Corporate: Annexure B2 | FY23 | 2022-05-14 |
| Financial results | Financial Results | FY27 Q1 | 2026-08-14 |
| Financial results | Financial Results | FY24 Q1 - FY26 Q4 | to 2026-05-30 |
| Other | Outcome of Board Meeting | FY27 Q1 | 2026-08-14 |
| Insider Trading / SAST | Disclosures under Reg. 29(2) SAST | FY26 Q3 (4 docs) | 2025-12-17 |
| AGM/EGM | EGM | FY26 Q3 (3 docs) | 2025-11-26 |
| Other | Reg. 32 (1),(3) Deviation & Variation | FY26 Q1 | 2025-06-02 |
| Other | Meeting Updates | FY26 Q3 | 2025-11-19 |

No earnings call transcript of any period is indexed. No investor
presentation of any period is indexed. The only annual report indexed is FY25.

## Held on disk

Nothing. No guidance extract file, because Bull AI holds no guidance for
PANORAMA.

## Gaps and which step each weakens

- No document text at all. Weakens every numeric step.
- No transcript and no presentation, ever. Steps 6 and 7 have no management
  claim to quote and no dated trigger to register. The transition step cannot
  be run from management's own words.
- The FY26 annual report is not indexed. The newest annual report is FY25,
  while results run to Q1 FY27. Step 3 reads a year behind the numbers.
- No credit rating indexed. Step 10 NOT FOUND. Looked for: Bull AI
  availability map. Agency sites unreachable (no egress).
- UNREAD SIGNALS. Four SAST Reg. 29(2) disclosures on 2025-12-17 and three
  EGM filings in FY26 Q3. Reg. 29(2) fires on a substantial acquisition of
  shares. A holding change may have occurred. Load-bearing for step 4.
- The Large Corporate Annexure B2 filings (FY23, FY24) mark the company as an
  identified Large Corporate borrower in those years. Load-bearing for
  leverage in step 5.
