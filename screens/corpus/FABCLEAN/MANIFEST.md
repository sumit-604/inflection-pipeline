# FABCLEAN corpus manifest

Company: Fabtech Cleanrooms Ltd (filings also use Fabtech Technologies
Cleanrooms Limited)
BSE: 544332 (BSE SME platform), symbol FABTCLEAN | ISIN: INE0HSD01011
CIN L74999MH2015PLC265137.
Not Fabtech Technologies Ltd (NSE FABTECH, BSE 544558), which is a separate
listed group entity.
Screened: 2026-09-21

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Corporate announcement, order booking, month ended 30-Apr-2026 | e4e49b45-9808-4a26-80a6-485fb6883e1a | 1 | 2026-05-12 |
| Corporate announcement, order booking, month ended 31-May-2026 | d73ba674-3ec4-4a18-9180-5df392802275 | 1 | 2026-06-12 |
| Financial Results, half year and year ended 31-Mar-2026, consolidated | a7c53cc5-909a-4dc0-9160-507d0bd661c3 | 11 | FY2026 Q4 |
| Outcome of Board Meeting, same results | 696ba602-6f8f-4833-8ac3-da669c94da52 | 11 | FY2026 Q4 |
| General filing carrying the same consolidated results | 79008ed9-997a-435f-a036-12853f209009 | 11 | FY2027 Q1 |
| Investor Presentation, FY26 financial snapshot | 6e4b8b6b-4602-45cb-8b75-72498240b3d2 | 21 | FY2027 Q2 index |
| Investor Presentation FY2027 Q1 | 5b0fc449-450e-4feb-8e9f-ca1df2e49d9a | 13 | FY2027 Q1 |
| Investor Presentation FY2026 Q4 | 1c1856e2-5d93-475c-8617-c80c3f4772ce | 21 | FY2026 Q4 |
| Investor Presentation FY2026 Q2 (philosophy, leadership) | 821967a1-bc41-4fd7-95ec-5b0fae44c354 | 10, 23 | FY2026 Q2 |
| Red Herring Prospectus | ccd135ac-8438-4269-904a-bfed79f1e9e8 | 144, 145 | FY2025 Q4 |

## Held on disk, and useless

`runs/544332-2026-08-04/inputs/` holds four investor-presentation and IPO-note
PDFs collected on 2026-08-04, plus a `screening/` folder of screener.in CSV
exports. **The screener CSVs are empty.** `screener-Quarters.csv` and its
siblings contain the row labels and no data. They were not used. This is worth
fixing in the collector.

## Known gaps

- **Credit rating NOT FOUND.** No rating filing is indexed and the agency sites
  were unreachable. Step 10 is empty.
- Promoter holding and pledge NOT FOUND.
- The company is on the SME platform and reports **half-yearly**. The latest
  financial period ends 31 March 2026. The order-book announcements run to
  31 May 2026, so the forward evidence is fresher than the financial evidence.
- No order-book figure after 31 May 2026 was found. Four months are unobserved.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 588.43 crore at the screen date. Used only for the step 11 recognition-gap
read, never for a valuation.
