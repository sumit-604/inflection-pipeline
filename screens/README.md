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

## Third run, 2026-09-10

Six operator picks, screened in one session: Kross, Panorama Studios
International, Mercury EV-Tech, Electronics Mart India, Wendt India, Spice
Lounge Food Works.

Verdicts: PROCEED to `/step1` on KROSS and EMIL. WATCH on PANORAMA. PASS on
WENDT, MERCURYEV and SPICELOUNGE.

**Both collection routes failed at the start, and only one came back.** The
network policy again denied CONNECT to docs.bull-ai.in, BSE and screener.in, so
no PDF could be downloaded and the collector could not run. WebFetch uses the
same proxy and was blocked too. On top of that, both Bull AI text readers were
down: `search_company_documents` returned "tool temporarily unavailable" for
the entire session, and `get_document_chunks` returned deadline-exceeded for
about 40 minutes before recovering.

The session ran in two halves. In the first, only metadata tools worked, and
six corpus ledgers were committed with no cards (commit `15afff8`). In the
second, `get_document_chunks` recovered and documents were reached by
identifier plus subcategory plus fiscal year and quarter, since search was
still down. That identifier route is the workaround to remember: it resolves a
document without needing a document_id from search.

**Bull AI's extractor fabricates content for image-heavy slides.** Page 4 of
the Kross Q1 FY27 deck came back as a "Key Financial Metrics" table of
"$X.XX billion" values with North America, Europe and Asia-Pacific geography
splits. Kross reports one segment and sells mainly in India. Page 2 of the same
deck returned image descriptions and the token "NO_CONTENT". Rule: treat any
chunk carrying round placeholder values or non-Indian geographies as extraction
noise, not disclosure, and say so on the card.

**`get_company_guidance` is the tool worth the subscription, and it only covers
companies that talk.** It returned a full page-cited guidance-and-delivery
ledger for KROSS (five period blocks, Q2 FY25 to Q1 FY27) and EMIL (four
blocks). It returned zero records for WENDT, PANORAMA, MERCURYEV and
SPICELOUNGE. Three of those four have no transcript and no presentation indexed
at any period. Bull AI adds nothing on a microcap that runs no investor
relations, which is exactly where a screener needs the most help.

Bull AI budget: about 30 calls used. Availability maps and usage checks cost
nothing and were used freely. The metered counter did not move during the
session, so it appears to lag; check the dashboard rather than trusting it.

Known limits of this run:
- No credit rating for five of six names. Only EMIL has one indexed: India
  Ratings, 11 December 2025, IND A affirmed with the outlook cut from Positive
  to Stable. Agency sites were unreachable.
- Promoter holding and pledge are NOT FOUND on all six. Bull AI indexes no
  shareholding-pattern subcategory for any of them, and the search tool that
  would have found the pages in annual reports was down.
- Freshness gaps: WENDT has no Q1 FY27 result (newest is Q4 FY26, April 2026),
  and MERCURYEV has none either (newest is Q4 FY26, May 2026). SPICELOUNGE is
  missing FY26 Q2 and Q4 results from the index entirely, and its Q1 FY27
  filing carries no FY26 full-year comparative.
- No balance sheet or cash-flow statement for KROSS, PANORAMA or SPICELOUNGE.
  Cash conversion is INDETERMINATE on those three, which caps any downstream
  verdict per the CLAUDE.md rule.
- MERCURYEV's audited FY26 results fail an internal arithmetic check: revenue
  plus other income does not equal the printed total revenue, in three separate
  columns. The card recommends an operator ruling on whether that becomes a
  named failure-catalogue pattern.
- Two framework gaps surfaced. The archetype library has no retail entry (EMIL)
  and no media or content entry (PANORAMA). The Section 1B cap table has no
  consumer-retail row; the nearest precedent is the open ENTERO action on
  distribution rows.
- Cards ran 2,244 to 2,594 words against the framework's 1,400 to 1,900.
  Shorter than the second run's 2,600 to 3,800, still long, and flagged rather
  than trimmed.
