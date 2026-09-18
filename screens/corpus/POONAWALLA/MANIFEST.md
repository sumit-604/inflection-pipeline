# Corpus manifest: POONAWALLA (Poonawalla Fincorp Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Poonawalla Fincorp Ltd., BSE 524000, NSE POONAWALLA,
ISIN INE511C01022.

## Method note
Corpus built from Bull AI's chunk reader (get_document_chunks) and search
(search_company_documents), per the 2026-09-08 operator ruling recorded in
screens/README.md. No PDF is held on disk. Files below are page-marked text
pulled through Bull AI, carrying the source PDF's own page numbers so a cite
can still be located.

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/POONAWALLA-Concall-Q1FY27-2026-07-17.txt | Q1 FY26-27 Earnings Conference Call transcript, held 17 July 2026, filed 23 July 2026 (Reg 30) | 1-18 (full transcript) | 08c36d14-3242-4579-b8b5-12516760163f |
| presentations/POONAWALLA-InvestorPresentation-Q1FY27-2026-07-17.txt | Q1FY27 Investor Presentation, dated 17 July 2026 (Reg 30) | 1-45 (full deck) | 0d120725-60f7-4ebc-a47c-a3e96d2bcaee |

## Metered call count
14-call budget. Calls made: 2 search_company_documents (transcript locate,
presentation locate), 1 get_company_guidance (14 records, FY26 Q4/Q2/Q4 and
context), 1 get_document_chunks attempt that exceeded the response-size limit
and returned no data (transcript pages 1-20 combined with presentation pages
1-25 in one multi-request call; split into smaller single-document calls
after this), then 5 successful get_document_chunks calls (transcript pages
1-10, transcript pages 11-18, presentation pages 1-15, pages 16-30, pages
31-45). list_document_availability is free and not counted.
Total metered calls used: approximately 9 of 14 (2 search + 1 guidance + 1
oversized/failed chunk request + 5 successful chunk requests, assuming the
failed request counted; 8 if it did not). Well under the cap.

## What is held
- Full Q1FY27 (quarter ended 30 June 2026) earnings call transcript,
  management prepared remarks and analyst Q&A, 18 pages.
- Full Q1FY27 investor presentation, 45 pages: financial highlights, product
  mix and AUM breakdown by line, capital and liquidity, credit rating (CRISIL
  and CARE, both AAA/Stable long-term and A1+ short-term), asset-quality
  trend with Stage 1/2/3 detail, borrowings composition, P&L, balance sheet,
  AI and digital initiative detail, board of directors, management team and
  second line, ESG, and shareholding pattern.
- get_company_guidance returned 14 records across Q4FY26, Q2FY26 and Q3FY25
  periods with management's own AUM/NIM/credit-cost/ROA delivery claims and
  forward guidance (35-40% AUM CAGR, 5-6x AUM aspiration over 5 years, ROA
  3-3.5% by June 2028 exit), each with document citation and page.

## Coverage gaps
- No annual report read (Bull AI lists Reg 34(1) annual reports through
  FY25; not pulled this run given the strength of the Q1FY27 transcript and
  deck. AR-based items — MD&A prose, chairman letter, detailed related-party
  schedule, full board committee composition, auditor's report and
  emphasis-of-matter, contingent liabilities, promoter pledge status — are
  NOT FOUND in this corpus).
- No promoter pledge figure. The deck's shareholding page (p.43) gives
  promoter holding 59.02% (down from 62.46% the prior quarter) with no
  pledge line and no breakdown by promoter entity. The ~340 bps drop is most
  likely the mechanical effect of the Rs 2,500 cr QIP in April 2026 (deck
  p.7) but the deck does not confirm this.
  Note: this NBFC's promoter is Adar Poonawalla / the Poonawalla / Cyrus
  Poonawalla group (Serum Institute); no separate promoter dig was done.
- No credit-rating rationale document. The deck (p.24) states the rating
  conclusion only: CRISIL and CARE both AAA/Stable long-term, A1+
  short-term, for Q1FY27, with no rationale narrative on leverage,
  concentration or the transition's sustainability. Not searched separately
  on Bull AI given the deck already carried the rating.
- No older-period concalls or presentations read (FY26, FY25 periods listed
  in list_document_availability but not pulled). Only Q1FY27, the latest
  quarter, is held.
- No peer, TAM, or independent penetration data. Out of scope for shallow
  analysis per framework.
- Market cap and CMP: not in this corpus. Operator-supplied market cap
  ~Rs 38,155 cr per Bull AI screen; verify live.

## Archetype note
Lender (framework variant applies to any deep run): AUM growth, NIM, asset
quality (GNPA/credit cost), RoA and RoE are the primary metrics. Section 1B
Amendment 17 (converter binding) does not apply; this is not a commodity
converter archetype.
