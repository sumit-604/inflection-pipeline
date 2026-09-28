# NAMOEWASTE corpus manifest

Company: Namo eWaste Management Ltd
NSE NAMOEWASTE (NSE Emerge SME platform) | ISIN INE08NZ01012
CIN L74140DL2014PLC263441. Listed 11-Sep-2024.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

The corpus is the Bull AI chunk reader over the filed PDFs. Page numbers are
the source PDF's own. No PDF is held on disk.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Investor Presentation, H2 and FY26 | 37cd3824-a171-4cdb-942e-a193b981cc0d | 1 to 26; 30, 31 (search snippets) | FY2026 Q4, filed 22-May-2026 |
| Earnings call transcript, H2 FY26, 25-May-2026 | 6363a957-75b9-4dfc-9748-44b7f5cc8f3c | 2 to 25 | FY2026 Q4, filed 28-May-2026 |
| Annual Report FY25, shareholding note 3-B and 3-C | 3f723a9a-5f1f-492c-a81d-766e6a9b52ad | 98 (search snippet) | FY2025 |
| Analyst meet intimations, May and June 2026 | 4c79cbde, 1d1055d4, 63ef99df, 56216a99 | 1 (search snippets) | FY2027 Q1 |
| SEBI Takeover Regulations disclosure | 0c71a279-8427-4f55-af05-2fa5f322d14c | chunk reader returned empty | FY2027 Q1, filed 21-May-2026 |
| Bull AI guidance records | from 37cd3824 and 6363a957 | pages as cited on the card | FY26 Q4 |

## Known gaps

- **Half-yearly reporter.** The latest financial period ends 31-Mar-2026. Six
  months (Apr to Sep 2026) are unobserved. H1 FY27 results fall due after this
  screen.
- **Audited FY26 results filing NOT FOUND.** The complete Result category map
  holds one document, H1 FY25. FY26 figures come from the company's deck and
  call.
- FY26 annual report indexed (uploaded 19-Aug-2026) but searches returned only
  FY25 AR pages. Promoter holding at 31-Mar-2026 NOT FOUND.
- Takeover-regulation disclosure of 21-May-2026: chunk reader returned empty.
- Credit rating NOT FOUND.

## Reader and label defects

- Deck page 2: text about a "$50M" investment, "AI-Based Sorting $8M" and
  tonnage targets of 10,000 tons. None of it matches the company. Treated as a
  reader hallucination. Not used.
- Deck page 16: a phone number with a +27 (South Africa) prefix. Reader
  artefact. Not used.
- Deck page 31 is headed "STATEMENT OF PROFIT AND LOSS - H2 FY 25" and carries
  the half year ended 31-Mar-2026. A label error in the deck or the reader.
- Deck pages 23 and 24 give conflicting capacity and timing: Hyderabad
  "Expected Operational Date Q2 FY26" on page 23, "47,00+ MTPA, expanding to
  72,000 MTPA by Q2 FY26-27" on page 24, against 82,000 MTPA installed on
  page 22. The card uses the call's figures.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 750.05 crore, read 2026-09-28.
