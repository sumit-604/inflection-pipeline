# Corpus manifest: DPABHUSHAN (D.P. Abhushan Ltd)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: D.P. Abhushan Limited, BSE 544161, NSE DPABHUSHAN, ISIN
INE266Y01019. Sector Consumer Discretionary / Jewelry Retail (gold, silver, diamond),
per `get_company_classification`.

## Method note
This session had egress to the Bull AI MCP only (no docs.bull-ai.in, BSE, screener.in
or rating-agency web access). All files below are page-marked text pulled through
`get_document_chunks`, using the source PDF's own page numbers where the tool returned
them page-by-page.

## Metered call count: 13 of the 14-call budget
1 `get_company_classification` free call (not counted) + `list_document_availability`
free call (not counted), then:
1-5: `search_company_documents` x5 (transcript locate, presentation locate, credit
rating locate, SSSG/store-metrics locate, MD&A/chairman-letter locate)
6: `get_company_guidance`
7-8: `get_document_chunks`, Q1FY27 transcript pages 1-10, then 11-18
9: `get_document_chunks`, Q1FY27 transcript pages 19-20
10: `get_document_chunks`, credit rating pages 1-6
11: `get_document_chunks`, AR FY25 pages 1-10
12: `get_document_chunks`, Q1FY27 investor presentation pages 1-20
13: `search_company_documents`, promoter shareholding/pledge query
(One earlier batched `get_document_chunks` call, and one retry, both failed with
"response exceeds limit" before any content returned and are not counted as they
returned no chunks.)

## Files held

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/DPABHUSHAN-Concall-Q1FY27-2026-07-28.txt | Q1FY27 earnings call, held 22 Jul 2026, filed 28 Jul 2026 | 1-20 (full) | c9896be0-e335-493e-80fa-1e961bb4f8fc |
| presentations/DPABHUSHAN-Presentation-Q1FY27-2026-07-21.txt | Q1FY27 investor presentation, filed 21 Jul 2026 | 1-20 (full) | e99a8d4f-d85c-4b02-9bff-dab9a5682dec |
| filings/DPABHUSHAN-CreditRating-CARE-2026-01-09.txt | CARE Ratings press release, dated 8 Jan 2026, filed 9 Jan 2026 | 1-6 (full) | de2615b1-a814-4759-a65d-c58495d43a7c |
| annual_reports/DPABHUSHAN-AnnualReport-FY25-2025-03-31.txt | 8th Annual Report FY2024-25, filed 5 Sep 2025 | 1-10 (front matter, Chairman's message, showroom list) | cd2006d0-6828-4bba-b5e5-6d4d5f94f9e8 |

`get_company_guidance` also returned quotable, page-cited management statements drawn
from documents NOT held whole in this corpus (only their guidance/delivery snippets are
captured, via the tool's own citations): Q4FY26 results concall (doc 39bee5b5, filed
around May 2026), Q4FY26 investor presentation (doc 775a240d), Q3FY26 investor
presentation with the QIP/8-store guidance (doc 0c7325e3), H1FY26 presentation (doc
0c7325e3, page 33), Q4FY25 concall (doc 3d23bc4b), Q1FY26 concall (doc ZAoBdV /
underlying doc), Q2FY24 presentation (doc f63316a6). Per the framework's rule, every
number sourced this way is cited on the card as `(guidance)` with the quarter and
speaker named, not as a corpus file and page; these underlying documents were not
separately fetched and saved as full-text files within this session's budget.

## Data quality flag, held document
Investor Presentation page 19 ("Company Overview") is very likely OCR/extraction noise:
it claims 1980s founding, UAE/Singapore/USA flagship stores, and "pioneered lab-grown
diamonds," none of which appear anywhere else in this corpus and all of which
contradict the company's own 1940 founding, 86-year legacy, and 12-store MP/Rajasthan/
Gujarat-only footprint stated on every other page of the same deck, the transcript and
the annual report. Marked in the presentation file and excluded from the card as a
source.

## Coverage gaps
- No FY26 or FY27 balance sheet, cash flow statement, or shareholding pattern table
  with percentage holdings. Promoter pledge status is inferred from three separate
  SEBI takeover-regulation "no encumbrance" declarations (Renu Kataria, Santosh
  Ratanlal Kataria HUF, Sanjay Kataria) filed April 2026 covering FY2025-26; exact
  promoter shareholding percentage NOT FOUND.
- AR FY25 held only for front matter (pages 1-10). The Management Discussion and
  Analysis Report (source page 126 onward) and the financial statements were not
  fetched; ROCE, total debt, and the full cash-flow statement are therefore NOT FOUND
  from the annual report (the credit rating's brief-financials table substitutes for
  the balance-sheet ratios that are available: gearing, interest coverage, TD/GCA,
  inventory turnover, operating cycle, current ratio).
- No FY26 annual report in Bull AI's inventory as of this session (only FY24 and FY25
  Reg. 34(1) annual reports listed).
- No standalone ROCE, RoE or RoIC figure found in any held document or guidance
  extract. NOT FOUND; looked for in the transcript, presentation, annual-report front
  matter, and credit rating.
- Credit rating dated 8 January 2026, based on FY25 and H1FY26 numbers. It predates the
  May 2026 gold import duty hike and the full Q1FY27 quarter. Treated as the
  agency's most recent independent view, not as current; the card says so explicitly.
- No market cap or live CMP in the corpus. Market cap ~Rs 3,043 cr per the operator's
  Bull AI screen figure, supplied outside this corpus; verify live.
