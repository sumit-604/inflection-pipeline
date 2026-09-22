# TANAA corpus manifest

Company: Taneja Aerospace & Aviation Ltd
NSE: TANAA | BSE: 522229 | ISIN: INE692C01020
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
| Financial Results FY2026 Q4, audited year-end consolidated results and cash flow | 49529697-3b36-4c1b-aa37-6aafd3d94409 | 15, 16, 18 | 2026-05-12 |
| Outcome of Board Meeting FY2026 Q4, standalone results and auditor report | 87113be1-cd6c-4c1a-8ca6-6c00058511c3 | 7, 14, 16 | 2026-05-12 |
| Financial Results FY2026 Q2 | 6270b100-68e8-4b8b-b54f-3082b95a249a | 10 | 2025-11-06 |
| Reg. 34(1) Annual Report FY2025 (MD&A, performance table) | dc7485dd-ca25-4628-bdd8-58f0ec72e920 | 28 | FY2025 Q4 |
| Reg. 34(1) Annual Report FY2024 (revenue recognition, shareholding) | 96986a98-5af8-48fd-a191-1c3406dff178 | 29, 53, 97 | FY2024 Q4 |
| Reg. 34(1) Annual Report FY2023 (MD&A, performance, share reconciliation) | 2042942c-83fe-4d53-a75b-f64d5fd9d267 | 19, 101 | FY2023 Q4 |
| Reg. 34(1) Annual Report FY2022 (related parties, share reconciliation) | 4f9edc02-e18a-4c84-8ac7-0c73bb3e6e2f | 69, 101 | FY2022 Q4 |
| SAST Reg. 29(2), Asscher Enterprises promoter acquisition | 20b95782-ff0b-4a1e-987f-0d1b4fb58b6b | 2, 4 | FY2024 Q4 |
| Financial Results FY2024 Q3 | 44dbf093-6bbc-47f0-be62-fdf89b08e123 | 13 | 2023-11-07 |

## Reader defect recorded

**FY2026 consolidated cash flow statement, page 18 of document 49529697.** The
table does not internally reconcile through the reader. Profit before tax of Rs
2,250.91 lakh with the adjustments listed does not produce the stated operating
profit before working capital changes of Rs 330.42 lakh, and cash generated from
operations reads negative Rs 8.80 lakh. **No line from that page is used as
evidence on the card beyond flagging it**, and cash conversion is recorded
INDETERMINATE. A deep run must check the original PDF.

## Known gaps

- **FY2026 profit after tax NOT FOUND.** Only profit before tax of Rs 2,250.91
  lakh was located. The tax charge is not in this corpus, so step 13 is tier D
  and the forward PE is left blank rather than estimated.
- **FY2026 annual report NOT FOUND**, so the FY26 MD&A and related-party note
  are unavailable.
- **No Q1 FY27 result exists** in the index. The latest period ends 31-Mar-2026.
- **The MRO tenant is never named** in any document read, and the group contains
  several related aviation entities (TAAL Enterprises, TAAL Tech, First Airways).
  Whether the tenant is related is the single most important unanswered question.
- **Credit rating NOT FOUND.** Agency sites unreachable.
- **Zero management guidance records.** No presentation, no earnings call.
- **Three "Award of Order / Receipt of Order" filings indexed and NOT READ**
  (Jul-2024, Dec-2024, Mar-2025). They are the only documents that might contain
  a forward trigger.
