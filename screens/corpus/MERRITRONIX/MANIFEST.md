# MERRITRONIX corpus manifest

Company: Merritronix Ltd (formerly Merritronix Pvt Ltd; some filings and the
deck spell it "Meritronix")
BSE: 544773, deck symbol MRTX | ISIN: INE1RQS01010 | NSE: none
CIN U32100TG1988PLC155611. Registered office C-22, Electronic Complex,
Kushaiguda, Hyderabad.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Corporate Presentation (Reg 30(6) filing, 18-Jul-2026) | db3c0efc-92e4-4d18-99a1-7264df0e4bc0 | 1 to 32 | indexed FY2027 Q2 |
| Red Herring Prospectus (uploaded 19-May-2026) | aedf4bf2-f11d-40eb-95e7-dec0fae042b2 | 35 to 37, 55 to 62, 92, 93, 149 to 160, 206, 210, 274 to 276, 293 (search snippets and chunk reads) | indexed FY2027 Q1 |
| General: outcome of investor meet, 24-Jul-2026 | 7696b639-633e-4d9a-92be-8f1dfed57dff | 1, 2 (snippet) | FY2027 Q2 |
| General: IR agency appointment, 01-Jul-2026 | 806ab63c-5897-403f-a8e4-6bd9b80badc1 | 1 (snippet) | FY2027 Q2 |
| Others: investor meet schedule, 17-Jul-2026 | 718a2755-fe1c-4829-82f8-b949b269a582 | 1 (snippet) | FY2027 Q2 |
| Management guidance records (get_company_guidance) | points to db3c0efc, page 25 | n/a | FY2027 Q1 |

Availability map (free) lists only: one investor presentation, three general
filings, one "Others" filing, the RHP and the DRHP (26-Mar-2026). No results
filing, no transcript, no annual report, no credit rating.

## Known gaps

- **No post-listing financial result.** The latest financial period is FY26,
  ended 31-Mar-2026, from the restated RHP accounts. Six months are
  unobserved.
- **Listing platform and cadence unresolved.** The deck says the company
  "Successfully listed on BSE SME Platform" in 2025 (deck page 7). The RHP
  says "This being an initial public issuing of the Equity Shares of our
  Company, the Equity Shares are not listed on any Stock Exchanges" (RHP
  page 293). Whether it reports half-yearly or quarterly is NOT FOUND.
- Issue price, listing date and gross proceeds NOT FOUND. The RHP carries
  "[●]" (RHP page 92).
- Credit rating NOT FOUND in the index; agency sites unreachable.
- Pledge NOT FOUND. Promoter holding is from the deck only (62.28%, deck
  page 31).
- Customer names are anonymised in the order book table (RHP page 158).
- No concall transcript exists in the index.

## Reader and document defects

- Deck page 4 is generic template text (board committees, "Digital
  Transformation") with no company content. Reader or deck artefact. Not used.
- Deck page 24 returns an image description of the Empire State Building.
  Reader artefact. Not used.
- Deck page 9 (product split) and page 10 (industry split) disagree with the
  RHP tables on pages 36, 37 and 155. Example: FY24 obsolescence revenue is
  Rs 329.51 lakh on the deck and Rs 1,092.33 lakh in the RHP; FY26 job work
  and trading sales are swapped. The RHP tables are used throughout.
- Deck page 27 gives FY26 EBITDA Rs 2,721.68 lakh; deck page 29 gives
  Rs 2,757.32 lakh. The gap is other income. The card uses page 29.
- A multi-document chunk request returned only the first request's pages.

## Price basis

Not a corpus document. Bull AI company record read 2026-09-28, market
capitalisation Rs 765.40 crore. The deck gives Rs 664.51 crore at Rs 380.04
and 1,74,84,854 shares as of 14-Jul-2026 (deck page 31).

## Bull AI calls

9 billable: 1 guidance, 5 searches, 3 chunk reads.
