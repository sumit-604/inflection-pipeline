# Corpus manifest: MAXIND (Max India Ltd.)

Collected 2026-09-18 via Bull AI MCP. Operator: Keerti Kaushik.
Company resolved: Max India Ltd., BSE 543223, NSE MAXIND, ISIN INE0CG601016.
Classification (Bull AI): sectors Healthcare, Investment Holding; industries Senior
Living, Assisted Care.

## Method note
This session used the Bull AI MCP chunk reader only (per the 2026-09-08 operator
ruling recorded in screens/README.md). No PDF is held on disk. Files below are
page-marked text pulled through get_document_chunks. Metered Bull AI calls used
this session: 10 (of the 14-call cap). Breakdown: 1 get_company_guidance,
2 search_company_documents, 7 get_document_chunks (2 of which, on the Q4FY26
concall and Q4FY26 investor presentation, returned zero chunks — see gaps below).
get_company_classification and list_document_availability are free and used freely.

| File | Source PDF | Pages held | Bull AI document_id |
|---|---|---:|---|
| concalls/MAXIND-Concall-Q1FY27-2026-08-12.txt | Q1 FY27 earnings call, held 2026-08-12, filed 2026-08-19 | 1-17 (full transcript) | 288f2472-c400-4c59-8592-a7dadb106524 |
| presentations/MAXIND-IP-Q1FY27-2026-08-11.txt | Q1 FY27 Investor Release, filed 2026-08-11 | 1-30 (full deck; page 26 OCR unusable, see note in file) | ee8b6d7e-ffd4-4362-ae07-6ba3b5ef0c99 |

Additional evidence used but NOT saved as standalone corpus files (captured only
as cited snippets in the card, per the metered-call budget):
- get_company_guidance tool output: 9 periods of guidance and self-reported delivery
  quotes, FY23 to FY27 Q2, drawn from documents GYXTCA (ee8b6d7e, Q2FY27 IP),
  e5rDix (288f2472, Q1FY27 concall, same as above), O7CIEr (0464b094, Q4FY26/FY27
  outcome doc), U1Ujm2 (baa161d3, Q4FY26 investor presentation), 6lYY0a (13d6a55d),
  1i7pf6 (bb51f229), DjFJUF (1205ead9, Q4FY25/Q1FY26 concall). These are management
  self-reported claims per the tool's own guardrail: "not independently verified and
  must not be used to confirm whether earlier guidance targets were met." Cited in
  the card as (guidance, <document label>, page).
- search_company_documents snippet, AR FY2025 (Reg. 34(1) Annual Report, document_id
  1c8901a5-7f13-468c-a72e-4893b5043cc8), pages 330-338: AGM Notice text on the
  preferential warrant issue, pre-issue shareholding pattern (promoter 50.14% as of
  1 Aug 2025), promoter identity (Max Ventures Investment Holdings Pvt Ltd; ultimate
  beneficial owners Analjit Singh BAS Family Trust, Tara Singh Vachani, Piya Singh,
  Veer Singh), and the Antara Senior Living / Contend Builders Pvt Ltd (Logix Infra
  Developers JV) related-party item for the Noida project. Read directly via
  get_document_chunks, pages 330-338.
- search_company_documents snippet, Monitoring Agency Report FY2027 Q2 (document_id
  9dff559d-c345-4b0b-9877-46d97c43b766): CARE Ratings Ltd acting as Monitoring Agency
  on use of preferential-issue proceeds. This is NOT a credit rating rationale; it is
  a SEBI-mandated proceeds-utilisation check. No credit rating document was found.

## Coverage gaps
- No credit-rating rationale. Searched Bull AI for "credit rating CRISIL ICRA CARE
  India Ratings"; the only hit was the CARE Ratings Monitoring Agency Report on
  preferential-issue proceeds, not a rating opinion on debt or the entity. Step 10 is
  NOT FOUND. Not searched on agency websites (CRISIL, ICRA, CARE, India Ratings,
  Acuité) because this session has no live-web egress; those sites are where it was
  looked for and blocked.
- Q4FY26 earnings call transcript (document_id 0464b094-c8fc-4193-ad99-2ceff6338027)
  and the Q4FY26 investor presentation (document_id baa161d3-3610-44ad-861d-b04ddfd48000)
  both returned zero chunks from Bull AI's reader despite being indexed (both are the
  source of several get_company_guidance citations, which still work through that
  separate tool). Full-year FY26 commentary is held only through the guidance tool's
  extracted quotes, not the primary transcript text. This is the same failure mode
  the 2026-09-08 run saw on other companies' Q1FY27 decks.
- No FY26 annual report MD&A / chairman's letter read (filed 2026-07-28, available
  in Bull AI but not pulled this session; budget was spent on the Q1FY27 concall and
  deck, which carry more current and complete detail).
- No board/director profile pages, no auditor's report, no full related-party
  schedule beyond the one AGM Notice item captured above.
- No market cap or live CMP held in corpus; the brief states ~Rs 792 cr per Bull AI
  screen. Verify live.
- Two figures for FY26 full-year consolidated revenue and EBITDA loss conflict
  between the directly-read Q1FY27 concall transcript (revenue Rs 175/145/190 cr for
  FY24/25/26; EBITDA loss Rs 57/139/121 cr) and a guidance-tool delivery quote from
  document O7CIEr (revenue Rs 164 cr FY25 to Rs 213.4 cr FY26, up 30%; EBITDA loss
  Rs 99 cr FY25 to Rs 83 cr FY26). Both are cited in the card; the discrepancy is
  flagged, not resolved. O7CIEr itself returns zero chunks on direct read (see above),
  so its full context could not be checked.
