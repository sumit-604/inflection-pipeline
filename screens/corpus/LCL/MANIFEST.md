# LCL corpus manifest

Company: Lohia Corp Ltd (formerly Kanpur Packaging Machines Ltd; the resulting
company of the demerger from Lohia Trade Services Ltd, formerly Lohia Corp Ltd)
NSE: LCL | BSE: 544839 | ISIN: INE0QJW01029
CIN U28261UP2023PLC183476. Registered office Panki Industrial Estate, Kanpur.
Listed 30-Jul-2026.
Screened: 2026-09-28

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Outcome of Board Meeting, Q1 FY27 consolidated and standalone results, 19-Aug-2026 | 79fc12a6-5d3b-4df3-8585-e207b9f3e2d8 | 1 to 10 | indexed FY2027 Q2 (chunks say FY2026) |
| Investor Presentation Q1 FY27, second indexed copy | 8ee9e3ed-3739-4d8c-b2fe-e2aeb27e7359 | 28, 30 to 38 | indexed FY2027 Q1 |
| Investor Presentation, first indexed copy | f0f1600b-b67e-42c7-9f98-bc8dd9179869 | none: reader returned empty | indexed FY2027 Q2 |
| Red Herring Prospectus | 7b89f9ad-90e0-41dc-8993-c8036d5dd564 | 31, 58, 79, 84, 92, 205 to 213, 416, 423, 429 | FY2027 Q2 |
| Prospectus (filed 30-Jul-2026) | debb2e94-dd67-4353-996d-caf0dafd9524 | 31, 40, 84, 92, 116 to 121, 423 | FY2027 Q2 |
| Draft Red Herring Prospectus | af495cb9-26f1-4be3-b3fc-58849b730c1c | 56, 188, 189, 247, 396 (snippets) | FY2027 Q2 |
| General: earnings call intimation (15-Aug-2026) and audio link (20-Aug-2026) | 42354659-f72f-4357-8ab8-efd48ef49549, 4295f699-5547-4f2d-866a-5a02c1e06cc3 | 1 (snippets) | FY2027 Q2 |
| Management guidance records (get_company_guidance) | none returned | n/a | n/a |

## Known gaps

- **Zero guidance records.** The Q1 FY27 earnings call of 20-Aug-2026 exists
  as an audio link only. No transcript is indexed.
- Credit rating NOT FOUND in the index; agency sites unreachable.
- FY26 related-party transactions as a percentage of revenue NOT FOUND. FY25
  is 33.36% (DRHP page 56).
- FY23 margin for the demerged business NOT FOUND. FY23 revenue is known
  (DRHP page 56).
- Customer concentration NOT FOUND.

## Reader and document defects

- **Empty deck.** The first indexed deck record (f0f1600b) returns no chunks,
  by selector and by document id. The same deck is indexed a second time as
  8ee9e3ed, labelled FY2027 Q1, and that copy reads cleanly. Same class of
  defect as GOODLUCK and LXCHEM in the second run.
- **Fiscal-label error.** The Q1 FY27 results filing is labelled FY2027 Q2 by
  the selector and FY2026 period 2 in its chunk metadata. It is the June 2026
  quarter.
- Q1 FY27 consolidated results header labels the Q1 FY26 column "Year ended
  30 June 2025" (results page 5). It is a quarter.
- RHP page 205 prints FY25 revenue as 13,678.72 million in the peer table;
  every other page gives 13,768.72 million. The latter is used.
- RHP page 211 India market forecast table is garbled: segment rows are
  interleaved with years. Only the header total row is used.
- A multi-request chunk call on the RHP returned empty for both requests.
  One billable call was lost.

## Price basis

Not a corpus document. Bull AI company record read 2026-09-28, market
capitalisation Rs 6,289.34 crore. IPO price Rs 425 (results page 6);
105.65 million shares (results page 5).

## Bull AI calls

14 billable: 1 guidance, 6 searches, 7 chunk reads (three returned empty).
