# screens/ — the shallow funnel

Where screener hits get a one-page read before anyone spends a full `/step1`
on them. Not the deep pipeline. A card says what the company does, the
transition management claims, the growth triggers with dates, whether the
numbers back it, what is missing, and a `/step1` verdict with the load-bearing
facts a deep run must verify first.

- `cards/<TICKER>.md` — one card per company, rewritten on each read.
- `corpus/<TICKER>/` — the documents themselves, held on disk, with a
  `MANIFEST.md` per company and a `.txt` beside every PDF carrying
  `===== PAGE n =====` markers so a card can cite a page you can open.

## The rule, after 2026-09-06

A card is written from documents held in `corpus/`. Cloud search is for
finding which documents exist and where; it is not the source of a card's
numbers. "Not found" on a card means not in the corpus, and the card says
where it was looked for.

## How the corpus is built

| Document | Source | Tool |
|---|---|---|
| Annual reports, concall transcripts, presentations, Financials.xlsx | screener.in, with the operator's login | `tools/collector/screener_collect.py <url> --output-dir <folder> --no-drive` |
| Credit-rating rationales | Agency pages linked from screener.in's Credit ratings block, no login | `tools/collector/fetch_ratings.py <url> --output-dir <folder>` |
| Credit-rating letters filed with the exchange | BSE announcement PDFs, no login | same script |
| Quarterly results, filings, and any document Bull AI indexes | `https://docs.bull-ai.in/d/<code>` serves the original PDF, no call cost | plain download; codes come from Bull AI search or chunk results |
| Quarterly results and filings Bull AI lacks | BSE announcements API (`AnnSubCategoryGetData/w`, `strCat=Result` or `-1`, with a bseindia Referer header) | plain download of `xml-data/corpfiling/AttachLive/<attachment>`; if that returns an 8 KB error page, the same name under `AttachHis/` serves it |
| India Ratings and Acuité "connect" pages | script shells; a plain fetch gets nothing | render in the browser, save the text |

Screener.in address quirk: ASM Technologies lives at its BSE code,
`/company/526433/`, not at its symbol. Try the symbol, fall back to the code.

## The three cloud services, honestly

| | Trendlyne MCP | Bull AI MCP | Local corpus |
|---|---|---|---|
| File on disk | no | no, but its links serve the PDF | yes |
| Page numbers | no | yes | yes |
| Knows what it holds | no | yes, free to ask | n/a |
| Credit ratings | no | no | yes |
| Budget | 400 calls/day | 100 calls/month on the current plan; searches and page reads count, availability and usage do not | your login and tokens |

Coverage seen on small caps: both services lagged on annual reports (FY25
only for Valiant and Ruby on Bull AI; screener.in had FY26 for all three),
neither had a transcript for Valiant or Ruby (none exist), and Bull AI's OCR
garbles financial tables, which is one more reason to hold the PDF.

## First run, 2026-09-06

Three operator picks from the Trendlyne 52-week-high and top-gainers screens:
VALIANTLAB, ASMTEC, RUBYMILLS, all under 150% year to date. Cards were first
written from Trendlyne snippets, then Bull AI snippets, then rewritten from the
held corpus. The corpus: 39 documents, about 1,650 PDF pages, both latest
quarterly results per company, the latest annual report per company, every
concall that exists, and credit ratings from CRISIL, ICRA, Acuité and India
Ratings. Bull AI calls used: 18 of 100.

Known gaps in the corpus: Valiant's IPO-proceeds monitoring report of August
2026 (Bull AI's link was empty; fetchable from the BSE archive path); ASM's
June-2026 result PDF is a scanned image (the quarter's numbers are taken from
the company's June-quarter presentation, which is held). Every other document
in the operator's list is on disk.

## Second run, 2026-09-08

Nine operator picks, screened in one session: Rossell Techsys, Forbes Precision Tools,
IKIO Technologies, Goodluck India, Laxmi Organic, Manorama Industries, Quadrant Future Tek,
Elantas Beck India, Bhansali Engineering Polymers.

Verdicts: PROCEED to `/step1` on ROSSTECH, GOODLUCK, LXCHEM and MANORAMA. WATCH on IKIO,
QUADFUTURE and BEPL. PASS on ELANTAS and FORBESPT.

**The corpus rule was bent, with an operator ruling.** This session had no egress: the
network policy denied the CONNECT to docs.bull-ai.in, BSE, screener.in and every rating
agency site, so no PDF could be downloaded and the collector could not run. On the
operator's ruling the corpus was instead built from Bull AI's chunk reader, which returns
clean page-numbered text of the same filed PDFs. Every card cites a file and a page, and
the page numbers are the source PDF's own, so a cite can still be opened. What is absent is
the PDF on disk. Since `.gitignore` excludes raw PDFs anyway, the tracked artifact is the
same shape as a normal run; the difference is that nobody holds the original.

**Credit ratings were unreachable.** Step 10 is NOT FOUND on eight of nine cards, with the
agency sites named as where it was looked for. MANORAMA is PARTIAL: its deck reports CARE
upgrading the bank facilities from A to A+, which is the agency's conclusion without its
rationale.

Bull AI budget: the run was planned against 40 remaining calls on the old 100-a-month plan.
The account moved to a 1,000-call plan mid-run and the cycle reset, so the constraint
dissolved. 18 calls were used in total, 10 chunk reads and 8 searches. Availability maps
cost nothing and were used freely to resolve identities and build corpus ledgers.

Known limits of this run, all recorded in the per-company manifests:
- No transcript exists at all for BEPL, ELANTAS or FORBESPT. No investor presentation
  exists for ELANTAS or FORBESPT.
- The Bull AI chunk reader returns empty for some indexed documents: the Q1FY27 decks of
  GOODLUCK and LXCHEM, the Q1FY27 transcript of IKIO, and one of BEPL's two Q1FY27 deck
  records. Where a second indexed copy existed it was found via search and used.
- QUADFUTURE's newest Bull AI transcript is labelled FY26 Q3 but serves the Q1FY26 call of
  July 2025. Its card carries a freshness warning and reads that transcript as claims whose
  outcomes are now knowable.
- ELANTAS reports to a 31 December year end; Bull AI's Indian fiscal labels are wrong for
  it. Its manifest carries a calendar-year warning.
- Cards ran 2,600 to 3,800 words against the framework's 1,400 to 1,900. Longer than
  specified, and flagged rather than trimmed.

## Third run, 2026-09-21

Sixteen operator picks, screened in one session: Indo Rama Synthetics, Filatex
India, Precot, Libas Consumer Products, Yaashvi Jewellers, BCC Fuba India
(partly paid line), Trident Lifeline, Zota Health Care, Symbiotec Pharmalab,
Hemant Surgical Industries, Fabtech Cleanrooms, QMS Medical Allied Services,
Marine Electricals, Rajputana Stainless, Shadowfax Technologies, AVT Natural
Products.

**Verdicts.** PROCEED to `/step1` on FILATEX, PRECOT, BCCPP, TLL, FABCLEAN,
QMSMEDI, SHADOWFAX and AVTNPL. WATCH on ZOTA, SYMBIOTEC and MARINE. PASS on
INDORAMA, HSIL and RSL. YAASHVI is a WATCH for documents, not a business
verdict: no financial statement of any kind exists for it in the corpus. LIBAS
got no card at all.

**The corpus rule was bent again, under the same operator ruling as 2026-09-08.**
This session had no egress: the network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency
site. No PDF could be downloaded and the collector could not run. The corpus is
Bull AI's chunk reader, which returns page-numbered text of the same filed
PDFs. Every card cites a file and a page, and the page numbers are the source
PDF's own. What is absent is the PDF on disk.

**Credit ratings were mostly unreachable again.** Step 10 is NOT FOUND on
eleven of the fifteen cards written, with the agency sites named as where it
was looked for. INDORAMA and FILATEX are complete: both filed India Ratings
intimations that Bull AI indexes, giving IND A-/Stable (outlook raised from
negative, 27-Jan-2026) and IND AA-/Stable (reaffirmed, 12-May-2026)
respectively. MARINE is PARTIAL: ICRA appears only as monitoring agency for its
issue proceeds, which carries no credit opinion. PRECOT is the frustrating one:
a Credit Rating Revision filing of 21-Mar-2026 is indexed as document
049528d0-0532-4412-900b-b2d26a4fc9de and the chunk reader returns empty for it.

**Two names could not be screened, for different reasons.**
- LIBAS is not in the Bull AI index. `search_companies` was run on both "Libas
  Consumer Products" and "Libas" and returned neither. With no egress there was
  no second route, and the identity was never resolved to a scrip code or ISIN.
  No card was written. Writing one would have breached the rule that every
  number traces to a file and a page.
- YAASHVI is in the index, but a complete untruncated availability check on its
  "Result" category returned an empty list. Only housekeeping filings exist: a
  Regulation 30(5) intimation, a Company Secretary change, a lease deed and a
  registrar certificate. Its card carries the ledger, the few facts those
  filings establish, and no business verdict. The card cannot tell a Bull AI
  coverage gap from a company that has not filed, and says so.

Bull AI budget: 48 calls used, 36 searches and 12 chunk reads, leaving 571 of
1,000 for the cycle. `search_companies` and `list_document_availability` cost
nothing and were used freely to resolve identities, including the four
ambiguous ones the operator flagged: HSIL is Hemant Surgical, not Hindustan
Sanitaryware; FABCLEAN is Fabtech Cleanrooms (BSE 544332), not Fabtech
Technologies (NSE FABTECH); BCCPP is the partly paid line of BCC Fuba India;
SYMBIOTEC listed three weeks before the screen.

### Findings worth carrying out of the cards

- **HSIL.** Revenue doubled to Rs 231 crore in FY26 while operating cash flow
  went to **negative Rs 32.02 crore** from positive Rs 4.59 crore, funded with
  Rs 39.27 crore of new short-term borrowing. Its audited standalone cash flow
  statement does not internally reconcile: the three section totals sum to
  negative Rs 38.50 crore against a reported net increase in cash of positive
  Rs 69.37 crore, and opening plus increase does not equal closing. Both years
  fail the same test. Recorded as a document finding, not a reader artefact,
  because the line items are legible and it is the totals that fail. Then the
  company spent Rs 19.98 crore on a pre-breakeven precision-oncology lab.
- **MARINE.** Going-concern emphasis of matter on its subsidiary Eltech
  Engineers Madras at 30-Jun-2026, an under-subscribed equity issue per the
  ICRA monitoring report, and **no published order book since 31-Mar-2025**,
  when it had fallen to Rs 524 crore against revenue of Rs 700 crore. For an
  order-book archetype the forward variable is simply missing.
- **FABCLEAN** publishes its order book monthly, by sector and by vertical,
  with the pipeline alongside. That is the best forward evidence in this run and
  very few small caps do it. The book grew 55% in one month to Rs 354.74 crore.
  The card's non-obvious point: the growth came by moving from pharma into
  renewable-energy capex, which may be a **quality downgrade** dressed as
  diversification. Sector-wise margin is the first thing a `/step1` must settle.
- **PRECOT** reports one segment while running two businesses, and its Q1 FY27
  EBITDA margin printed 20.6% against 13.0% for FY26 after the Hindupur closure
  and the technical-textile commissioning. One quarter, and the cleanest
  RE-RATING LIVE cell in the run.
- **QMSMEDI** moved its services mix from 24% to 41% of revenue in one year and
  published both segment margins on the call, 25% for services against 10% to
  12% for products. A Role 1 margin bridge can be built from the company's own
  disclosure, which is rare.
- **BCCPP** is the partly paid line, and its call money, call schedule and
  forfeiture terms are NOT FOUND because the Letter of Offer of 5-Mar-2026 was
  not retrieved. That must be resolved before any position work on the
  instrument the operator actually holds.
- **ZOTA's** EBITDA is the wrong metric and management said so on the call:
  under Ind AS 116 the store rent sits below it. FY26 depreciation of Rs 82.45
  crore against EBITDA of Rs 25.98 crore. Read profit before tax, which is
  negative and widening.

### Reader and collector defects recorded

- **MARINE**, Q1 FY27 profit and loss page: damaged figures through the reader,
  including a cell reading "2,5737.04", and expense lines that do not reconcile
  to the stated profit. No line from that page is used; the card works from the
  segment table.
- **ZOTA**, page 38 of the Q1 FY27 deck: an "Export Performance Highlights"
  table in metric tons listing FDA and EMA approvals, contradicting page 39 of
  the same deck. Treated as a reader artefact and not used.
- **SHADOWFAX**, page 12 of the FY26 deck: revenue, EBITDA, adjusted EBITDA and
  net profit figures interleaved so that the margin pairings are unreliable.
  Margins taken from the clean quarterly tables instead.
- **FILATEX**, document 2ff9d3d7 is indexed as "FY2027 Q2". It is the Q4 and
  FY26 call of 4 May 2026. Same class of fiscal-label error as QUADFUTURE in
  the second run.
- **Collector defect.** The screener.in CSV exports held at
  `runs/544332-2026-08-04/inputs/screening/` are **empty files**, carrying row
  labels and no data. They contributed nothing to the FABCLEAN card. Worth
  fixing in `tools/collector/`.

### Known limits of this run

- Cards ran 1,763 to 2,547 words against the framework's 1,400 to 1,900,
  excluding YAASHVI at 764. Shorter than the second run's 2,600 to 3,800, still
  over. Flagged rather than trimmed away.
- Promoter holding is NOT FOUND on nine of fifteen cards. Bull AI indexes SAST
  disclosures and annual reports unevenly, and without egress there was no
  second route to a shareholding pattern. This is the most systematic gap in
  the run.
- Four names report half-yearly, not quarterly: TLL, HSIL and FABCLEAN on the
  BSE SME platform, and MARINE's order book series annually. The framework's
  two-quarter proof test degrades to a two-half-year test on those, and the
  latest financial period for TLL, HSIL and FABCLEAN ends 31 March 2026, so six
  months are unobserved.
- Two names are read from a prospectus alone, SYMBIOTEC and RSL, because both
  listed recently and have filed no result yet that the index holds. Every
  competitive claim on those two cards is marked as an issuer claim.
