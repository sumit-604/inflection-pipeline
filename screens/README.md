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

## Third run, 2026-09-09

Eight operator picks, screened in one session: India Nippon Electricals, Graphite India,
Molbio Diagnostics, TAAL Tech, Delton Cables, Mangalore Refinery, Titan Bio-Tech,
Corona Remedies.

Verdicts: PROCEED to `/step1` on TAALTECH and DELTON. WATCH on CORONA, INDNIPPON, MOLBIO
and TITANBIO. PASS on GRAPHITE and MRPL.

**Revised 2026-09-10: GRAPHITE moved from PASS to WATCH.** The operator supplied
GrafTech's announcement of a minimum 30% electrode price rise for all open commercial
negotiations, confirmed by web search and following a March 2026 rise of USD 600 to
USD 1,200 per tonne. Graphite India rose as much as 18% to a 52-week high. The card had
named realisation per tonne rising at full utilisation as the single observation that
would change the view, and it fired. Steps 7, 8, 11, 12 and the PENDING FETCH section
were realigned in one edit; the archetype, the moat finding and the R1 rung were left
unchanged, because an industry price rise changes earnings and not the ladder. Source
tier is operator supplied and web confirmed, not corpus.

**The corpus rule was bent a second time, and further than on 2026-09-08.** That run had
no egress but could still read filed PDFs through Bull AI's chunk reader. This run could
not. `get_document_chunks` and `search_company_documents` timed out on every call, at
every page range, in both collections, for the whole session. Egress was GitHub only:
the proxy answered 403 to the CONNECT for docs.bull-ai.in, screener.in, bseindia.com and
every rating agency host, and WebFetch returned EGRESS_BLOCKED. No page of any filed
document was read by anyone this session.

On the operator's ruling of 2026-09-09 the cards were written anyway, from Bull AI's
structured endpoints, which stayed up: `list_document_availability`, `get_company_guidance`,
`get_company_counterparties`, `get_company_market_transactions`,
`get_company_corporate_actions` and `get_company_classification`. Each returns a document
code and a page, so a cite still opens. Every card carries **TIER: DEGRADED** at the top
and the whole method is written up once at `screens/corpus/_METHOD-2026-09-09.md`.

The epistemic step down is real and is stated on every card. On 2026-09-08 a quote was
text the session read. On 2026-09-09 a quote is a quote Bull AI reports, at a page Bull AI
names. Everything on these eight cards is PENDING SOURCE VERIFICATION.

What no card in this run could do:
- Step 5, financial trajectory: no balance sheet, no cash flow, no cash conversion, on any
  of the eight. Only the fragments management chose to state.
- Step 8, proof check: the last two quarters are not held for any name. NOT FOUND on all eight.
- Step 10, credit rating: NOT FOUND on all eight, agency sites named as where it was looked for.
- Step 4, promoters: no shareholding pattern or pledge for any name. Covered only where group
  companies and insider dealing surfaced, which was INDNIPPON, GRAPHITE and TITANBIO.

Per-name limits, all recorded in the manifests:
- MOLBIO listed in August 2026 and has filed only a DRHP, an RHP, a Prospectus and one board
  meeting outcome. Guidance and counterparties both returned zero. Its card carries no business
  numbers at all and says so; the next action is to fetch the RHP, not to run `/step1`.
- TITANBIO has no annual report, no presentation and no transcript indexed in any year, and
  returned zero guidance and zero counterparties. Same shape of verdict: fetch from BSE first.
- MRPL and TAALTECH returned zero guidance records. For MRPL that is notable because its
  transcripts are indexed through FY2026; Bull AI derived no guidance from documents it holds.
- GRAPHITE and DELTON were screened without a `list_document_availability` call, so their
  corpus ledgers are incomplete and step 1 says so on both cards.
- TAAL Tech resolves to ISIN INE524T01011, the entity formerly named TAAL Enterprises, which
  filed a change of name on 2025-11-04. One company, renamed.
- Bull AI's classification for TITANBIO ("Seeds and Biotechnology Products", "Agriculture")
  could not be confirmed against any document and is flagged as possibly miscoded.

Two findings worth carrying forward regardless of tier:
- DELTON book value per share went from Rs 105 to Rs 397 in FY26 on a land revaluation under
  Ind AS. Nothing was earned. It is the first thing a deep run must open.
- INDNIPPON FY26 net profit was Rs 1,112 Mn against EBITDA of Rs 1,222 Mn. Profit at 91% of
  EBITDA is not reachable from operations after depreciation and tax, so non operating income
  is material and unquantified.

Bull AI budget: 923 calls remaining at the start against a 1,000 call cycle to 2026-10-08.
About 40 calls were used. Timed-out calls consumed no quota, so the two dead endpoints cost
nothing but the corpus.

Cards ran 1,362 to 2,876 words against the framework's 1,400 to 1,900. MOLBIO came in short
because there was nothing to say. The rest ran long. Flagged rather than trimmed, as in the
2026-09-08 run.

### 2026-09-09, later the same session: PENDING FETCH sections added

Bull AI's document readers were retried six times across the session, spread over
roughly an hour. Still down at close. One retry was informative: passing an ambiguous
identifier to `search_company_documents` returned "Multiple companies match the supplied
identifier" immediately, so identifier resolution is fast and healthy. Passing a unique
identifier then timed out. The fault is in document retrieval, not in company lookup.
Timed-out calls consumed no quota.

The collection route was checked and is empty. `collect_to_repo.py` pushes into this repo
at `runs/<ticker>-<date>/inputs/`, and run folders are not gitignored, so 1,780 PDFs are
already tracked. None belongs to any of the eight names. The cable runs were checked
specifically, in case Delton had been collected as a peer: `fincables-2026-08-12` used KEI,
RR Kabel and Paracables, and `birlacable-2026-08-20` used HFCL, STL and Paracables. The
collector cannot run in session; it needs screener.in egress and `tools/collector/.env`,
and its REPO_ROOT is a Windows path.

Open web search does work, through Firecrawl and WebSearch, because both run remotely.
WebFetch is egress blocked and no scrape tool exists, so search returns snippets and never
a page. **The post 2026-09-06 rule was applied strictly: search was used to establish which
documents exist, never as a source of a card number.** That rule earned its keep. A single
search for India Nippon's Q1FY27 returned three sources saying revenue was about Rs 304 cr
and one saying Rs 3,045 cr, a tenfold units error. A Delton search returned one headline
saying FY26 profit rose 28% and another saying it fell 28%.

On the operator's instruction, a **PENDING FETCH** section was appended to all eight cards.
Each names the documents proven to exist and unreadable, marks anything web indicated as
unverified, says which step it unblocks, and gives the fetch address. No web derived number
was written into any step. A grep for the specific figures search returned confirms none
appears on any card.

One correction surfaced by the check, recorded on the TAALTECH card: Bull AI reported a
market cap of Rs 1,410 cr and screener.in showed a materially lower figure the same day.
One is wrong. The card now carries a market capitalisation warning. No step depended on it,
because no valuation was performed.

Fetch block for `tools/collector/companies.txt`, ordered by value, PASS names omitted:

```
TAALTECH:https://www.screener.in/company/539956/
DELTON:https://www.screener.in/company/504240/
INDNIPPON:https://www.screener.in/company/INDNIPPON/
CORONA:https://www.screener.in/company/CORONA/
MOLBIO:https://www.screener.in/company/MOLBIO/
TITANBIO:https://www.screener.in/company/524717/
```

TAALTECH, DELTON and TITANBIO use BSE codes. TAAL Tech needs the code because the company
was renamed in November 2025. Titan Bio-Tech's annual report is not indexed by Bull AI in
any year and must come from BSE scrip 524717 directly.
