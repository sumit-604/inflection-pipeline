# Corpus manifest: SSWL (Steel Strips Wheels Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Steel Strips Wheels Ltd., BSE 513262, NSE SSWL, ISIN INE802C01033.
Bull AI classification: sectors Auto Components, Automotive Manufacturing; industries
Steel Wheels, Alloy Wheels.

## Method note
This session has no egress to docs.bull-ai.in, BSE, screener.in or the rating agency
sites; the proxy denies the CONNECT (per the 2026-09-08 operator ruling in
screens/README.md). No PDF is held. Every file below is page-marked text pulled through
the Bull AI chunk reader (`get_document_chunks`) or, where noted, `search_company_
documents` snippets and `get_company_guidance` quotes. Page numbers are the source
PDF's own.

## Metered Bull AI calls: 12 of 14 (cap)
- `list_document_availability`: 1 call, free (not counted against the cap).
- `search_company_documents`: 5 calls (transcript Q1FY27 discovery; presentation
  Q1FY27 discovery; annual report FY25 MD&A/promoter discovery; credit rating
  discovery; promoter shareholding/pledge discovery).
- `get_company_guidance`: 1 call.
- `get_document_chunks`: 6 calls (transcript Q1FY27 pages 1-14; presentation Q1FY27
  pages 1-20; presentation Q1FY27 pages 21-27; credit rating pages 1-5; annual report
  pages 27-31; annual report pages 71-74).
Two attempted bundled 5-request calls were rejected by the tool as exceeding its
response size limit and are not counted; only the successful single-document calls
above are counted.

## Files held

| File | Source document | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/SSWL-Concall-Q1FY27-2026-07-16.txt | Q1 FY27 Results Conference Call, held 16.07.2026, filed 21.07.2026 | 1-14 | 01af1498-cdc6-496a-a3af-7b830fa843a8 |
| presentations/SSWL-Presentation-Q1FY27-2026-07-15.txt | Q1 FY27 Investor Presentation, filed 15.07.2026 | 1-27 (full deck) | e973ac7c-6a5f-4086-9ae3-b7f62a7894ec |
| filings/SSWL-CreditRating-IndiaRatings-2026-02-18.txt | India Ratings and Research press release/intimation, 18.02.2026 | 1-5 (full document) | fe46b412-9945-43b6-84b0-33f9e453baff |
| annual_reports/SSWL-AnnualReport-FY25-excerpts.txt | Reg. 34(1) Annual Report FY2025 | 27-31, 71-74, plus search snippets from pages 33, 181, 219 | 14645600-32b5-40fe-9b2c-7dc5cb163de3 |
| filings/SSWL-Guidance-and-Ratios-multi-period.txt | Bull AI `get_company_guidance` output (multiple underlying FY26 annual release and prior-period concall/press-release documents) plus one `search_company_documents` ratios snippet from the FY26 Q3 and Q2 investor presentations | various, cited page-by-page inline | 5a3ffce9-63d0-47d0-91e2-3b8f5e56a3e9 (FY26 annual release, primary); others named inline; ratios snippet from 4a5a7187-94bc-4c36-b56e-30ea58744971 (FY26 Q3 IP) |

## Coverage gaps
- **No full annual report business narrative.** The AR's actual Management Discussion
  and Analysis prose (business overview, segment discussion, risk factors, outlook) was
  not retrieved; only the page carrying its heading (p.27) was read, and the Bull AI
  chunk on that page returns board/HSE/KMP content, not the MD&A body. The chairman's
  letter and full related-party rupee figures (p.219 table, amounts truncated) were
  not read within budget. This weakens step 2 (business model, beyond what the concall
  and presentation already give) and step 9 (flags, beyond what is captured from the
  page 219 party-name list).
- **No promoter pledge figure found.** The shareholding-pattern table (AR p.74) carries
  no pledge/encumbrance column. NOT FOUND is recorded on the card; the AR's separate
  pledge disclosure section (if any, typically a distinct table) was not located within
  the pages read.
- **CFO change not explained.** FY25 AR (as at 31.03.2025 and report date) names Naveen
  Sorot as CFO; the Q1FY27 concall of July 2026 names Rahul Kumar as CFO. No document
  in this corpus records the date or reason for the change. NOT FOUND.
- **No FY26 or FY27 annual report.** Bull AI's newest indexed Reg. 34(1) Annual Report
  is FY2025 (year ended 31.03.2025); FY26's has not been filed/indexed yet as of this
  pull (consistent with a September AGM cycle).
- **No standalone Q4FY26 (Jan-Mar 2026) quarter-level concall or results deck was read.**
  Only full-year FY26 P&L (from the investor presentation's historical table) and 9MFY26
  figures (from the credit rating) are held; the discrete Q4FY26 quarter is not
  isolated in this corpus, which weakens the "last two quarters" proof-check test in
  step 8 (only one clean quarter, Q1FY27, is held at quarter granularity).
- **No consolidated financials.** All P&L figures pulled are standalone (the investor
  presentation and concall are explicitly standalone; the credit rating and AR notes
  reference consolidated basis in places but no consolidated P&L table was pulled).
- Related-party transaction rupee amounts (AR p.219) were truncated in the retrieved
  snippet; only the list of related-party entity names was captured.
- Segment-wise (steel vs alloy) EBITDA/wheel split: management explicitly declined to
  disclose this on the Q1FY27 call ("proprietary information"), so it is NOT FOUND
  anywhere, not just in this corpus.
- No X post / promoter web-check equivalent run (out of scope for shallow analysis by
  framework definition).
