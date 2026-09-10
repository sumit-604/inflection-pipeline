# Corpus manifest: EMIL (Electronics Mart India Ltd.)

Identity resolved 2026-09-10 via Bull AI `search_companies`.
NSE EMIL. BSE 543626. ISIN INE02YR01019.
Bull AI market cap field: Rs 7,023.59 cr (undated, verify live).
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
