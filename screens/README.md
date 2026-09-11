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

## Third run, 2026-09-11

Four operator picks, screened in one session: Awfis Space Solutions, The Ugar Sugar Works,
Venky's (India), KRM Ayurveda.

Verdicts: PROCEED to a spear pass on AWFIS. WATCH on UGARSUGAR. PASS on VENKEYS as a
transition alpha name, WATCH as a sum of the parts situation. PASS on KRMAYURVED.

**Two constraints, not one.** As on 2026-09-08 the network policy denied the CONNECT to
docs.bull-ai.in, BSE, screener.in and every rating agency site, so no PDF could be
downloaded and the collector could not run. The corpus was again built from Bull AI's chunk
reader on the operator's standing ruling; every card cites a file and a page, and the page
numbers are the source PDF's own.

New this run: Bull AI's `search_company_documents` tool returned "temporarily unavailable"
on every call, for the whole session. Documents could be reached only by category and
period, never by query. That is why no annual report appears in any of the four manifests:
a 250 page report cannot be targeted without search, and blind paging is not affordable.
The cost is concentrated and identical on all four cards: promoter holding, pledge, and the
related party schedule are NOT FOUND everywhere. `list_document_availability`,
`get_document_chunks` and `get_company_market_transactions` all worked normally.

`get_company_market_transactions` partly filled the promoter gap and earns a place in the
standard kit. It gave the Peak XV exit on AWFIS, promoter family buying on UGARSUGAR and
KRMAYURVED, and confirmed that the only Venky's insider records are 2023 inter-promoter
transfers.

Bull AI budget: 840 calls remained at the start of the run on the 1,000 a month plan; about
40 were used. The constraint is not binding.

Known limits of this run, all recorded in the per-company manifests:
- UGARSUGAR is the thinnest corpus the funnel has produced. Bull AI carries no results
  filing, no transcript and no presentation for the company, in any year. The card runs
  almost entirely on one CareEdge rating rationale, which happens to be an unusually good
  document, and has no management voice at all.
- VENKEYS has a freshness gap at the load-bearing point. The newest document is dated May
  2026 and the June 2026 quarter is absent, in a name whose May call describes prices
  falling as it speaks.
- KRMAYURVED's earnings call transcript and its 31-Aug-2026 "Change in Management" filing
  are both indexed and both return zero chunks. The same empty-document defect as last run.
- The Bull AI reader returned invented content for two pages of the KRM presentation: a
  Nairobi-headquartered agriculture profile on page 4 and an unrelated Bangalore contact
  block on page 12. Recorded in the manifest, quoted nowhere. Read every reader page for
  plausibility before citing it.
- Cards ran 2,100 to 2,600 words against the framework's 1,400 to 1,900. Shorter than the
  2,600 to 3,800 of the last run, still long, and flagged rather than trimmed.

One framework note for the operator. AWFIS has no archetype in the CLAUDE.md library. The
closest entry is the outsourcing partner, but the engine is a spread between a nine year
rent commitment and a 26 month customer lock-in, which is nearer the LEVERED ANNUITY
BUILDER archetype the operator declared for CLEANMAX. A ruling is needed before any Section
1B work on flexible workspace.
