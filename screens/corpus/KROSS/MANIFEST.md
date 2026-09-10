# Corpus manifest: KROSS (Kross Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE KROSS. BSE 544253. ISIN INE0O6601022.
Bull AI market cap field: Rs 1,416.63 cr (undated, verify live).
Operator: Keerti Kaushik.

## Collection status: PARTIAL (page-cited text held, no PDF on disk)

Collection failed first, then partly recovered on 2026-09-10.

1. Direct download stayed blocked all session. This container has no egress.
   The proxy answered 403 to CONNECT for docs.bull-ai.in, www.bseindia.com and
   www.screener.in, verified 10:22 UTC via `/__agentproxy/status`. WebFetch
   uses the same proxy and was blocked too. No PDF is held on disk.
2. Bull AI's `search_company_documents` was down for the whole session. It
   returned "tool temporarily unavailable" on every attempt.
3. Bull AI's `get_document_chunks` timed out for about 40 minutes, then
   recovered. With search still down, documents were reached by identifier plus
   subcategory plus fiscal year and quarter. The extracts in this folder come
   from that route.

The operator ruling of 2026-09-08 governs. With no egress, Bull AI's
page-numbered chunk text stands in for the PDF. Page numbers are the source
PDF's own, so every cite can be opened later. What is absent is the PDF itself.

CORPUS QUALITY WARNING. Bull AI's extractor fabricates generic content for
image-heavy presentation slides. It invented a dollar-denominated financial
table and North America / Europe / Asia-Pacific geography splits for page 4 of
the Kross Q1 FY27 deck. Any chunk carrying round placeholder values or
non-Indian geographies is extraction noise, not disclosure.

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
