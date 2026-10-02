# MARINE corpus manifest

Company: Marine Electricals (India) Ltd
NSE: MARINE | ISIN: INE01JE01028 | not BSE listed
CIN L31907MH2007PLC176443. Andheri East, Mumbai.
Screened: 2026-09-21

## Corpus rule deviation (operator ruling 2026-09-08 applies)

No egress this session. The corpus is the Bull AI chunk reader over the same
filed PDFs. Page numbers are the source PDF's own. Nobody holds the original.

## Documents read

| Document | Bull AI doc id | Pages read | Period |
|---|---|---|---|
| Consolidated results, quarter ended 30-Jun-2026, with segment table and auditor report | 05671c97-bf13-48ac-9375-cf0039300e56 | 8, 9, 10 | FY2027 Q2 index |
| Outcome of Board Meeting, FY25 results with segment table | d4d4e707-b784-46a6-a2b3-5404bc466188 | 19 | FY2026 Q1 |
| Annual Report FY2025 (Reg. 34(1)), MD&A | f151a013-5829-4482-bb43-5214d78e828d | 82, 83 | FY2025 Q4 |
| Investor Presentation FY2026 Q3 | 4579dffe-0e73-426c-88d5-58f303957970 | 17 | FY2026 Q3 |
| Investor Presentation FY2025 Q1 | f4a97f14-b0ec-48e8-90ee-4a55bc6e75aa | 15, 30 | FY2025 Q1 |
| ICRA Monitoring Agency Report on issue proceeds | 356c3123-6fc1-4b73-b592-fc8af2a34ed6 | 4, 8, 10 | June 2026 |

## Reader artefact warning

Page 9 of the Q1 FY27 results filing, the consolidated profit and loss table,
returned damaged figures through the reader. One cell reads "2,5737.04", and
the expense lines as read do not reconcile to the stated profit before tax.
**No profit and loss line from page 9 is used in this card.** All profit
figures are taken from the segment-wise table on page 10, which is internally
consistent. Revenue and the expense captions from page 9 are used only where
they match page 10.

## Known gaps

- **Credit rating NOT FOUND** as a rating filing. ICRA appears in the corpus
  only as monitoring agency for the issue proceeds, which is a different
  mandate and carries no opinion on creditworthiness. Step 10 is served
  partially and the card says so.
- **No order book figure after 31 March 2025.** The FY25 annual report carries
  a multi-year order book series; nothing newer was found. For an order-book
  business this is the most important gap on the card.
- Promoter holding and pledge NOT FOUND.
- No FY26 annual report is indexed.

## Price basis

Not a corpus document. Bull AI company record, market capitalisation
Rs 5,306.69 crore at the screen date. Used only for the step 11
recognition-gap read, never for a valuation.
