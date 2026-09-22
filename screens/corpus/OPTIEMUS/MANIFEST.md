# OPTIEMUS corpus manifest

Company: Optiemus Infracom Ltd
NSE: OPTIEMUS | BSE: 530135 | ISIN: INE350C01017
Screened: 2026-09-22

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency site.
The corpus is the Bull AI chunk reader, which returns page-numbered text of the
same filed PDFs. Page numbers are the source PDF's own. Nobody holds the
original file.

## Documents read

| Document | Bull AI doc id | Pages read | Filed / uploaded |
|---|---|---|---|
| Investor Presentation FY2027 Q1 (Q1 FY27 results, takeaways, guidance) | fed50256-0492-4661-8a5d-0cc32fa1cba9 | 4, 15, 16, 17 | 2026-08-04 |
| Outcome of Board Meeting, Q1 FY27 standalone and consolidated results | c7744525-e1aa-49ea-b8f3-0e642d75cf15 | 2, 5, 10 | FY2027 Q1 |
| Investor Presentation FY2026 Q4 (EMS partnership wins, 3-year guidance) | 4c0cb9ed-2d58-4950-9347-42fd41e9b220 | 5, 7, 8, 9, 10, 11, 12, 13 | 2026-05-30 |
| Monitoring Agency Report, ICRA, issue proceeds to 30-Jun-2026 | 240f8bbd-bff0-44d5-a537-d2314cd2a0c8 | 9, 10, 13 | FY2027 Q2 |
| General, Nothing / CMF joint venture press release | c7fb7b39-aadf-48ef-89cb-c0de2c119dee | 2, 3 | 25-Sep-2025 |
| General, FY2025 annual report content (MD&A, governance, share capital) | cb3cfa90-5d2d-4bea-9945-b2ce1c3cc5ca | 54, 98, 113, 245 | FY2026 Q2 |
| Reg. 34(1) Annual Report FY2025 | 31e140c2-037e-48e4-942d-a02ec2f00b7a | 98, 113 | FY2025 Q4 |
| Investor Presentation FY2026 Q3 (EMS partnership) | a843e18d-3a9f-4eaa-8437-2435572852f3 | 10 | 2026-02-13 |
| Investor Presentation FY2026 Q2 (Nothing partnership) | ce763fec-093d-4cb4-9fee-3eaec0c29024 | 7 | 2025-11-14 |
| Certificate under Reg. 74(5), RTA confirmation | 422af187-2908-4368-871d-fb3f1073ffd6 | 2 | 2026-07-04 |

## Known gaps

- **FRESHNESS GAP ON THE LOAD-BEARING NEWS.** The operator reports the stock
  locked at 20% upper circuit on 22-Sep-2026 because CMF by Nothing and Optiemus
  expanded their partnership to end-to-end smartphone R&D in India. **That
  announcement is NOT FOUND in this corpus.** The latest document held is dated
  4 August 2026 and this container has no live web. The card reads the original
  September 2025 joint venture instead and says so. Retrieving the current
  announcement is the first action of any deep run.
- **Balance sheet and cash flow NOT FOUND.** For an EMS business that doubled
  revenue in a quarter, the working-capital position is the key unobserved
  variable.
- **Credit rating NOT FOUND.** Agency sites unreachable. ICRA appears only as
  monitoring agency for issue proceeds, which carries no credit opinion; this is
  recorded as a PARTIAL substitute on step 10.
- **Promoter holding percentage NOT FOUND.** No shareholding pattern indexed.
- **No FY2026 annual report** is indexed, and no earnings call transcript exists.
- Customer concentration is disclosed nowhere; no customer is named with a
  revenue share.
