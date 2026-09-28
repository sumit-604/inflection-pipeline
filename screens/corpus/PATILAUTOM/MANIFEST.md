# PATILAUTOM corpus manifest

Company: Patil Automation Ltd (formerly Patil Automation Private Limited)
NSE Emerge (SME platform): PATILAUTOM | ISIN: INE17GV01016 | BSE code: none in Bull AI
CIN L29299PN2015PLC155878. Listed on NSE Emerge in June 2025.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Investor Presentation, H2 FY26 and FY26 | a8945f0b-2dd2-413b-80bb-baa45e2d92cc | 2 to 38 | FY26 (indexed FY2026 Q4; chunk metadata says FY2027 Q1) |
| Earnings call transcript, H2 FY26, call of 12-May-2026 | 7cb9de07-6e2b-482d-8c54-04a217ff5e17 | 1 to 20 | FY26 (indexed FY2026 Q2: fiscal-label error) |
| Outcome of Board Meeting, 9-Sep-2026: preferential issue and IPO-proceeds variation | b7e97fb8-a30a-4a17-a405-0591c13e6819 | 1 to 7 | FY2027 Q2 |
| Outcome of Board Meeting, Mii Robotics stake 60% to 70% | 1f68dd3d-f2c1-45f5-8867-7131e827f129 | 2 (search snippet) | FY2027 Q2 |
| General Updates, EGM notice letter, 10-Sep-2026 | 72ccb2bc-1de4-49d5-8936-79e800f26a7c | 1, 2 (search snippet) | FY2027 |
| AGM proceedings summary, 24-Sep-2026 | b619d2ee-0d40-43bc-acda-ad42505c276b | 1 (search snippet) | FY2027 Q2 |
| Corporate governance non-applicability, 10-Jul-2026 | 0a9ca470-a066-4d69-aa90-5c312c1aa924 | 1 (search snippet) | FY2027 Q2 |
| Bull AI guidance record (get_company_guidance) | cites 7cb9de07 and a8945f0b | n/a | FY26 |

## Bull AI calls

12 billable: 1 guidance, 8 chunk reads (one returned "response too large" and is
counted), 3 searches. Availability maps were free.

## Reader defects

- Transcript page 14 comes back as a reader-written "Discussion Summary", not
  verbatim text. The working-capital cycle and the Rs 12 crore defence order are
  taken from it and marked as reader summary on the card.
- Deck page 37: the share-price table repeats a looping pattern of prices and
  volumes. Not used. The shareholding line on the same page (promoter 69.29% at
  31-Mar-2026) is used.
- The "Awarding of order(s)/contract(s)" filing of 19-Jun-2026
  (1111590c-6a5b-41a5-af95-b10246238f1a) returns zero chunks. Order value NOT FOUND.
- Fiscal labels: the FY26 call transcript is indexed FY2026 Q2. The FY26 deck
  is indexed FY2026 Q4 in availability and FY2027 Q1 in chunk metadata.

## Known gaps

- **No results filing in the index.** The "Result" category is empty. FY26
  numbers come from the investor deck. Consolidated revenue from operations is
  NOT FOUND; only consolidated total income (Rs 172.79 crore) is disclosed.
- SME platform, **half-yearly** reporting. Latest financial period ends
  31-Mar-2026. H1 FY27 (to 30-Sep-2026) is not yet reported.
- Annual report: FY25 only (Reg 34 filing). FY26 annual report NOT FOUND.
- Consolidated cash flow and consolidated balance sheet NOT FOUND. The deck
  gives standalone only.
- **Credit rating NOT FOUND.** No rating filing indexed.
- Pledge NOT FOUND.
- Order book after 12-May-2026 NOT FOUND.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 768.20 crore, read 2026-09-28. The record predates the preferential
allotment approved 9-Sep-2026 (EGM 3-Oct-2026).
