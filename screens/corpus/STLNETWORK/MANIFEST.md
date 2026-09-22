# STLNETWORK corpus manifest

Company: STL Networks Ltd (Invenia)
NSE: STLNETWORK | BSE: 544395 | ISIN: INE1VXE01018 | Demerged from Sterlite Technologies 31-Mar-2025
Screened: 2026-09-22

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency site.
The corpus is the Bull AI chunk reader, which returns page-numbered text of the
same filed PDFs. Page numbers are the source PDF's own. Nobody holds the
original file.

## Documents cited

**Read this column honestly.** Only three documents in the whole run were read as
full pages via `get_document_chunks`: TIRUPATIFL page 3, QLL pages 13 to 15, and
DICIND page 106. Every other page below was sourced from a
`search_company_documents` **snippet**, which carries the document id and the
page number but is a truncated extract, not the full page. The cites are real
and openable. They are not full-page reads.

| Document | Bull AI doc id | Pages cited | Filed / uploaded |
|---|---|---|---|
| Updates FY2027 Q2, Q1 FY27 standalone and consolidated results with notes | 54cb8f5b-70d7-43ee-8f23-2b9a66159f2d | 5, 10, 11, 12 | FY2027 Q2 |
| Outcome of Board Meeting FY2027 Q1, Q1 FY27 results | 117f4502-eacf-4c28-a20e-2afe249c79a7 | 5, 11, 12 | FY2027 Q1 |
| Change in Management FY2027 Q1, FY26 audited results and demerger note | 5ea0efb9-c6e8-4d35-8f4a-e20951e956a5 | 6, 17, 20 | FY2027 Q1 |
| Financial Results FY2026 Q4, audited FY26 consolidated | 2fcde620-bf1e-472a-a7f3-f38a6a2ab96c | 17 | 2026-05-07 |
| Preferential Issue, promoter warrant issue of Rs 108 crore | 46f222ab-d136-4355-a01f-131008cfaa60 | 17, 18 | FY2027 Q1 |
| SAST Reg. 29(2), Bandhan Mutual Fund sell-down | 10f63f43-f69d-40ac-8fc0-4c53ae98f6aa | 1, 3 | 2026-01-05 |
| General, CGST demand order intimation | 3ee06fea-aa68-4a84-8a12-5b4b85e85c01 | 1 | 2026-02-26 |
| Financial Results FY2026 Q3, debenture security-cover certificate | 5ae266e0-4a55-4a7c-b0ec-99deebd883c7 | 15, 16 | FY2026 Q3 |

## Known gaps

- **No order book disclosure at any date.** This is a project-execution business
  and the order book is its forward variable. It appears nowhere. Same defect the
  2026-09-21 run recorded for MARINE.
- **Cash flow statement NOT FOUND.** Cash conversion INDETERMINATE.
- **Note 3 on contract assets and receivables was truncated in the reader.** The
  note states Rs 155.74 crore of contract assets and Rs 151.41 crore of trade
  receivables at 30-Jun-2026, **identical to the rupee to the 31-Mar-2026
  figures**, described as "representing receivables from customers based on the
  terms and con..." with the text cut off. Rs 307.15 crore frozen across two
  reporting dates is the largest single risk on the card and the explanation was
  not read. A deep run must read note 3 in full.
- **Credit rating NOT FOUND.** Agency sites unreachable. Recorded as a PARTIAL
  substitute: a Debenture Trust Deed of 2-Dec-2025 with quarterly security-cover
  certificates audited by Price Waterhouse. That is compliance certification, not
  a credit opinion, and the cover ratio itself was not read.
- **Promoter holding percentage NOT FOUND.**
- **Zero management guidance records.** No presentation, no earnings call.
- The CGST demand amount from Haldia Commissionerate was not read.
