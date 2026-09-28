# CURIS corpus manifest

Company: Curis Lifesciences Ltd
NSE CURIS (NSE Emerge SME platform) | ISIN INE1BZN01016
CIN L24230GJ2016PLC086559. Listed 14-Nov-2025.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

The corpus is the Bull AI chunk reader over the filed PDFs. Page numbers are
the source PDF's own. No PDF is held on disk.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Reply to exchange clarification, carrying the audited H2 and FY26 results, balance sheet, cash flow, IPO utilisation | 944b602b-ef47-4683-a567-8e3b928e9b76 | 1 to 10 | FY26, results dated 30-May-2026, reply 03-Jul-2026 |
| Investor Presentation | 067e665c-ed3e-4561-b803-966ba6543d03 | 1 to 23 | H1 FY26 figures, filed 11-Mar-2026 |
| Investor meet transcript, Valueportal, 22-Jan-2026 | 37c11395-9058-4d9d-85fc-214bb4e16543 | 1 to 11 | filed 29-Jan-2026 |
| Red Herring Prospectus | 7c098d21-d8d6-4904-8769-b53ac8fcbab5 | 53, 72, 74, 256 (search snippets) | Nov 2025 |
| Acquisition disclosure, Uninova Lifesciences 51% | 37984852-252b-462e-9b30-5e8d10ab6e22 | 3, 4 (search snippets) | filed 30-Mar-2026 |
| Agreements disclosure, Curosun Pharmaceutical Nig Ltd 49.95% | 3e137398-3d56-462a-951b-3fbc93fa3de0 | 2, 3 (search snippets) | filed 13-Aug-2026 |
| Change in management, independent director resignation | 0691738f-a289-4510-b1b1-d7167509ef37 | 2 (search snippet) | 03-Jul-2026 |
| Integrated Filing, Financial | 716f7595-1f0c-4082-a4d5-251ee34d9a78 | chunk reader returned empty | filed 30-May-2026 |

## Known gaps

- **No management guidance of any kind.** get_company_guidance returned zero
  records. No revenue or profit number for FY27 was found in any document.
- **Half-yearly reporter.** The latest period ends 31-Mar-2026. Six months are
  unobserved.
- The Result category availability map is empty. The audited FY26 results
  were found only inside the reply-to-clarification filing.
- No earnings call exists for H2 FY26. The only transcript is an investor
  meet of 22-Jan-2026, which Bull AI labels "Earnings Call Transcript".
- Promoter holding after the IPO NOT FOUND in a filing. The card derives it
  from the RHP pre-issue table and the post-issue share capital, and labels
  it as arithmetic.
- No annual report indexed. Related-party schedule NOT FOUND.
- Credit rating NOT FOUND.

## Reader and label defects

- Investor meet transcript pages 5 and 6: garbled figures, "EBITDA margin is
  $876", "EBITDA was 0.21, means at 21.46%", "PAT was 15.09". Not used; the
  card takes H1 FY26 figures from the deck page 20 instead.
- Deck page 16: the "India's Geopolitical Boost" bullet repeats the
  outsourcing bullet word for word. A deck or reader duplication.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 180.81 crore, read 2026-09-28.
