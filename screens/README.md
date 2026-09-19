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

## Third run, 2026-09-18

Nine operator picks, screened in one session: Timex Group India, CSM Technologies,
Poonawalla Fincorp, Max India, Capillary Technologies, D.P. Abhushan, Supreme Petrochem,
Steel Strips Wheels, Alufluoride.

Verdicts: PROCEED to `/step1` on TIMEX and POONAWALLA. WATCH on CSM, MAXIND, CAPILLARY,
DPABHUSHAN, SPLPETRO, SSWL and ALUFLUOR. PASS on none.

**Same method as the second run.** No egress again: the proxy denied the CONNECT to
docs.bull-ai.in, BSE, screener.in and the rating agency sites. The corpus was built from
Bull AI's chunk reader and guidance tool under the 2026-09-08 ruling. Every card cites a
file and a page; no PDF is held on disk.

**Two names sit far above the small/micro-cap mandate.** POONAWALLA (~Rs 38,155 cr) and
SPLPETRO (~Rs 15,220 cr) were screened because the operator named them. Both cards say
so in the header.

**One verdict was aligned by the orchestrator.** The MAXIND agent draft said PROCEED while
its own step 11 posture read RESEARCH / WATCH. Step 12 was aligned to step 11: an R0 shell
that has not yet shown a consolidated operating profit, with FY26 revenue and EBITDA loss
disagreeing between the concall and the guidance tool, is a WATCH.

**Credit ratings were reachable this time for five of nine**, through rating releases and
rationales that Bull AI indexes as company filings: CARE (DPABHUSHAN, stale Jan 2026),
India Ratings (SSWL, SPLPETRO), CRISIL (SPLPETRO), and rating grades without a rationale
for CSM (in the RHP) and POONAWALLA (in the deck). NOT FOUND for TIMEX, MAXIND, CAPILLARY,
ALUFLUOR.

Bull AI budget: 109 metered calls for nine names, 46 chunk reads, 47 searches, 9 guidance
pulls, 7 classification lookups. One agent ran one call over its 14-call cap (CAPILLARY);
the manifest names the cause. 622 calls remain in the cycle to 2026-10-08.

Known limits of this run, all recorded in the per-company manifests:
- Documents that Bull AI indexes but returns empty: the Q4FY26 concall and deck of MAXIND,
  the Q1FY27 deck of SPLPETRO, the TIMEX transcript, and one CAPILLARY concall record.
- No transcript or presentation exists for ALUFLUOR. No Q1FY27 result is indexed for
  ALUFLUOR or TIMEX although both should have filed by now.
- Page 19 of the DPABHUSHAN Q1FY27 deck carries text that contradicts the rest of the
  corpus; it was excluded as extraction noise and is flagged in the manifest.
- Cards ran 1,900 to 2,004 words before step 5A and 2,097 to 2,237 after it, against
  the v1.1 framework's 1,400 to 2,100. Flagged, not trimmed.
- No promoter pledge figure was found for any of the nine. Every card marks it NOT FOUND
  and lists it as a load-bearing fact for `/step1`.

**Step 5A added on 2026-09-19 (operator ruling, framework v1.1).** The operator's standing
ask, FY27E revenue, FY27E PAT, FY27 PAT growth and forward P/S, was missing from the spec
and so from every card. All nine cards now carry it in the header and as step 5A, with the
basis letter named: (a) guidance for SPLPETRO and SSWL; (b) latest-quarter growth for CSM,
POONAWALLA, MAXIND, CAPILLARY and DPABHUSHAN; (c) CAGR or FY26 growth for TIMEX and
ALUFLUOR, which have no June-2026 quarter indexed. Three more Bull AI calls fetched TIMEX's
FY26 PAT and SPLPETRO's FY26 revenue and PAT.

| Ticker | FY27E revenue (Rs cr) | FY27E PAT (Rs cr) | PAT growth | Fwd P/S | Basis |
|---|---:|---:|---:|---:|---|
| TIMEX | 1,020 | 96 | +28% | 6.0x | c |
| CSM | 274 | 29 | +21% | 1.9x | b |
| POONAWALLA (NII) | 7,420 | 1,620 | +198% | 5.1x | b |
| MAXIND | 316 | loss | n.m. | 2.5x | b |
| CAPILLARY | 1,048 | 69 reported (104 normalised) | +31% | 3.4x | b |
| DPABHUSHAN | 6,425 | 485 | +129% | 0.47x | b |
| SPLPETRO | 5,820 | 357 | +9% | 2.6x | a |
| SSWL | 6,500 | 257 | +27% | 0.84x | a |
| ALUFLUOR | 232 | 27 | +12% | 1.7x | c |
