# ROLEXRINGS corpus manifest

Company: Rolex Rings Ltd
NSE: ROLEXRINGS | BSE: 543325 | ISIN: INE645S01024
CIN L28910GJ2003PLC041991. Rajkot, Gujarat. Listed 9-Aug-2021.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Investor Presentation, August 2026 (Q1 FY27) | 79666f45-d3bf-4518-a49a-a0da4f3d136b | 1 to 22 | FY2027 Q1 |
| Investor Presentation, Q4 and FY26 | 7318f76d-0d04-492f-a9e9-2a5a60542b5d | 15 to 20 | FY2026 Q4 |
| Earnings call transcript, Q4 FY26, call of 18-May-2026 | 0ace52c0-2bc1-4e68-bcf8-3ba8f6f9f384 | 3 to 20 | FY2026 Q4 |
| Unaudited results, quarter ended 30-Jun-2026 (Outcome of Board Meeting, 5-Aug-2026) | 795bed3c-fb86-4c4f-957e-770a9e26aacb | 2, 3 (search snippet) | FY2027 Q1 |
| India Ratings rating action, filed 19-Jun-2026 | 8dd4e6f3-2b7d-4210-8ff6-e77af749546f | 1 to 6 | FY2027 Q1 |
| Buyback Letter of Offer | 16ceb2ca-4aca-49b4-a970-9741c3db9431 | 20, 22, 25 (search snippets) | FY2027 Q2 |
| Buyback postal ballot notice, 23-Apr-2026 | 5deeacd0-21d8-41ad-a3c8-4e88b9f3cee9 | 20, 21 (search snippets) | FY2027 Q1 |
| Bull AI guidance record (get_company_guidance) | cites 79666f45, 7318f76d, 0ace52c0 | n/a | FY26, FY27 |

## Bull AI calls

8 billable: 1 guidance, 5 chunk reads, 2 searches. Availability maps were free.

## Reader and document defects

- Q1 FY27 deck page 1: the reader invents "premium brand association with
  Rolex" and "aerospace" positioning. Not in any other page. Not used.
- Transcript page 7 is a reader-written summary table, not verbatim text. Its
  FY26 segment split (domestic bearing 386, domestic auto 170, export bearing
  154, export auto 350, scrap 71, incentives 13) reconciles to Rs 1,143 crore
  and to the verbatim FY25 split on page 11, so it is used and marked.
- Post-Buyback Public Announcement (48df94f9-163b-4528-8464-f749dd8a19d4) page 2
  returns another company's details: a different CIN, an Ahmedabad office, a
  2020 record date, "rolerings.com". Not used.
- Fiscal label: document 51cc5ff6-f265-4da1-9248-b4fa7534dd46 is indexed
  "Investor Presentation FY2027 Q2" and serves the Q4 FY26 deck.
- **Company-side contradictions** (document findings, not reader artefacts):
  - The CMD letter says "We delivered 15% revenue growth YoY" for FY26 (Q4 deck
    page 15). The P&L on page 18 shows revenue down 1.0%.
  - The CFO says "Domestic revenue grew by 50%" (transcript page 4). The
    segment split gives Rs 556 crore against Rs 506 crore, which is +9.9%.
  - FY26 geography: Q4 deck page 17 says exports 56%, domestic 44%. Q1 deck
    pages 8 and 21 and Ind-Ra say exports 44%.
  - Net debt table (Q1 deck page 20) shows FY26 gross debt Rs 367 crore and
    net debt Rs 38 crore, against "fully debt-free with over Rs 367 crores of
    net cash" on Q4 deck page 15 and nil debt per Ind-Ra. Treated as a
    column error. Not used.
  - FY26 ROCE: 20.1% (Q4 deck page 17), 18.0% (Q1 deck page 20), 17% (Ind-Ra).
  - Working-capital days FY26: 158 (Q1 deck page 20), 195 (Q4 deck page 17),
    188 (Ind-Ra).

## Known gaps

- No Q1 FY27 earnings call transcript is indexed.
- Annual report: FY25 latest indexed. FY26 annual report NOT FOUND.
- Q2 FY26 and Q3 FY26 standalone quarters NOT FOUND separately.
- Promoter pledge NOT FOUND. Final post-buyback promoter holding NOT FOUND
  (Letter of Offer gives "may increase to 54.23%" on full acceptance).
- Balance of US tariff refunds NOT FOUND in rupees.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 5,124.68 crore, read 2026-09-28.
