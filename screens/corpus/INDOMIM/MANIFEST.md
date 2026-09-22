# INDOMIM corpus manifest

Company: INDO-MIM Ltd
NSE: INDOMIM | BSE: 544837 | ISIN: INE084101034 | Listed 30-Jul-2026, IPO at Rs 485
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
| RHP | f2f9e106-5c97-4fd6-ac4b-11c3cb013eab | 23, 198, 202, 357, 360, 376 | 2026-07-23 |
| PROSPECTUS | 9c4972f0-4353-4fdc-8588-11a4cd881c17 | 137, 202, 357, 376 | 2026-07-30 |
| DRHP | fe9448aa-d932-440d-95c5-73041046975f | 117, 175, 178, 314, 317 | 2026-07-17 |
| Financial Results FY2027 Q1 (notes, auditor caveats, dividend, IPO terms) | 70ca2fe3-b734-48d5-950d-646abd1b27e3 | 5, 10, 11 | 2026-08-17 |

## Known gaps

- **Q1 FY27 revenue and profit figures NOT READ.** The result document is held
  and pages 5, 10 and 11 were read, which carry the notes, the auditor's caveats,
  the dividend detail and the IPO terms. **The profit and loss table on pages 6
  to 9 was not retrieved.** This is a named gap, not an absence: a deep run
  should read document 70ca2fe3 pages 6 to 9 first. The card therefore treats
  FY26 as the last fully observed period.
- **FY2026 balance sheet and cash flow NOT FOUND.** Net debt to EBITDA of 1.15
  and debt to net worth of 0.57 are FY2025 figures from the DRHP ratio table.
- **Credit rating NOT FOUND.** Agency sites unreachable. No monitoring agency
  report, bank letter or debenture trustee filing was located.
- **Promoter holding percentage NOT FOUND.** The pages read did not carry the
  shareholding table and no post-listing SAST disclosure is indexed.
- **Zero management guidance records.** No forward number in any document.
- **MARKET CAPITALISATION REQUIRES LIVE VERIFICATION.** The Bull AI service
  record puts market capitalisation at Rs 57,537.80 crore, which against about
  48.24 crore shares implies roughly Rs 1,192 per share against an IPO price of
  Rs 485 on 30-Jul-2026, a 2.46-fold rise in under two months. The card's PASS
  verdict rests entirely on that number and flags it for live confirmation.
