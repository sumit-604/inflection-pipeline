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
| Credit-rating rationales, when the agency site is blocked | Bull AI indexes the exchange-filed press release under doc type `Credit Rating` | `search_company_documents` then `get_document_chunks` on the returned document_id |
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
| Credit ratings | no | yes, where the company filed the agency press release or letter with the exchange (third run got all three) | yes |
| Budget | 400 calls/day | 1,000 calls/month since the second run (was 100); searches, guidance pulls and page reads count, availability and usage do not | your login and tokens |

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

## Third run, 2026-09-16

Three operator picks, named in one message: Antelopus Selan Energy, IOL Chemicals and
Pharmaceuticals, RACL Geartech.

Verdicts: PROCEED to `/step1` on IOLCP. WATCH on RACLGEAR. PASS on ANTELOPUS.

The one-line reason per name:
- **IOLCP** is a commodity converter with a six-year documented mix shift out of ibuprofen,
  a single-rung R2 to R3 claim, no debt, and two quarters of margin ahead of guidance.
- **RACLGEAR** is the best operator of the three and the most fully priced: proof gate
  fired, ugliness an artifact of KTM's insolvency, and roughly 44 times FY26 standalone
  earnings against a nearest sector ceiling of 25x with FY27 guided at about 10 percent
  growth. EARNINGS-ONLY posture.
- **ANTELOPUS** has no quality-ladder climb on offer. It is an R1 commodity price-taker
  getting bigger. Q1 FY27 profit rose 42 percent on a falling sales volume, which is price
  doing the work. PRICED NARRATIVE posture.

**Name resolution note.** The operator's "antelopus selan enegy" resolves to Antelopus Selan
Energy Ltd, BSE 530075, NSE ANTELOPUS, ISIN INE818A01017, formerly Selan Exploration
Technology Ltd. Bull AI's `search_companies` does not match on "Selan Exploration
Technology"; searching "Selan" alone returns it.

**The corpus rule was bent again, under the same condition as 2026-09-08.** This session had
no egress: the proxy denied the CONNECT to docs.bull-ai.in, BSE, screener.in and
indiaratings.co.in with a gateway 403, logged in the proxy status at 2026-09-16T12:38Z. No
PDF could be downloaded and the collector could not run. The corpus was built from Bull AI's
chunk reader and its page-cited search, following the operator ruling recorded for the
second run. Every card cites a file and a page, and the page numbers are the source PDF's
own.

**Credit ratings were reachable this time, through Bull AI rather than the agency sites.**
Step 10 is populated on all three cards, against eight of nine NOT FOUND last run:
- ANTELOPUS: India Ratings press release, 09-Jun-2026, IND A/Stable/IND A1, full rationale
  read. It supplied the single most important fact of the run, that the PSCs for Bakrol,
  Karjisan and Lohar expire in 2030 and Cambay in 2029, and that 2P reserve reporting is
  clipped to those dates. Those assets carry 91 percent of production.
- RACLGEAR: CARE press release, 10-Oct-2025, CARE A-; Positive / CARE A2+, rationale read.
- IOLCP: PARTIAL. Only the company's reaffirmation letters are held (CARE A+; Stable and
  CARE A1+, reaffirmed 30-Jun-2026). The rationale press release is not indexed.

Bull AI budget: 21 calls used of 789 remaining on the 1,000-a-month plan. Breakdown: 5
company searches, 3 availability maps, 10 document searches, 3 guidance pulls, 1 chunk read
(the India Ratings rationale, pages 1 to 4). Availability maps and usage checks cost
nothing against the metered tools and were used freely.

Known limits of this run, all recorded in the per-company manifests:
- **No earnings call transcript exists for ANTELOPUS at any date.** Bull AI indexes an
  intimation record and no transcript. For a name whose thesis is a drilling schedule, the
  normal place to test the schedule is missing. Step 5 does not run on that card.
- No Q1 FY27 transcript for RACLGEAR. The call was held 25-Aug-2026 and is not indexed. Its
  FY27 guidance is read from the Q4 FY26 call, and the card names closing this gap as
  load-bearing fact 1.
- FY2026 annual reports are indexed for IOLCP (uploaded 2026-08-07) and RACLGEAR (uploaded
  2026-08-21) but neither surfaced in page-cited search, so FY2025 is the latest annual
  report in both corpora. ANTELOPUS has no FY2024 or FY2026 annual report indexed at all.
- **ROCE is NOT FOUND for RACLGEAR in every year**; the company's key-ratio note does not
  report it. NOT FOUND for IOLCP in FY25 and FY26. Disclosed for ANTELOPUS only to FY25
  (18.25 percent). Not estimated on any card.
- Promoter holding is filed and clean for RACLGEAR (42.68 percent, nil encumbrance) and for
  ANTELOPUS (69.94 percent for the acquirer and PACs, via the merger SAST disclosure). NOT
  FOUND for IOLCP.
- No market cap or CMP carries an as-of date. Bull AI's company record has none. Every
  recognition-gap line on every card says to verify the price live, and no card states a
  fair value or a target.
- Two document defects are carried rather than silently corrected. The ANTELOPUS Q1 FY27
  deck prints a crude inventory build as "6,500 bopd", a rate where a stock is meant, and
  the India Ratings working-capital figures are inconsistent in magnitude with revenue. The
  RACLGEAR Q4 FY26 transcript states FY26 EBITDA as "229.16 crores" where Rs 129.16 cr is
  correct.
- Sector cap rows do not fit any of the three. Oil and gas exploration and production has
  no row; the nearest for ANTELOPUS is Mining and mineral exploration at 20x. Auto
  components has no row; the nearest for RACLGEAR is Cables and industrial products at 25x.
  For IOLCP neither Pharma and CDMO at 38x nor Specialty chemicals at 35x describes a
  bulk-API converter with a 40 percent solvents leg. **Three operator rulings are needed
  before any of these names reaches Stage 11.**
- Cards ran 2,550 to 3,450 words against the framework's 1,400 to 1,900. Longer than
  specified, and flagged rather than trimmed, as in the second run. The framework's word
  budget has now been missed on two consecutive runs and is worth revisiting.

### Third run, addendum of 2026-09-17

The operator asked for FY27 top line, bottom line and forward PE on all three names. Each
card now carries an `Addendum: FY27 top line, bottom line and forward PE` after step 12.
**The shallow framework does not provide for this**; it stops before any forward estimate.
The addenda state no fair value, no exit PE and no target price, Section 1B is not run and
no Mental Model is signed. The framework is worth amending to say whether a forward
estimate belongs on a shallow card at all.

**Live prices were reachable after all, through WebSearch rather than the container.** The
egress block is on the container's own network: curl and WebFetch are both refused by the
proxy, including WebFetch against the BSE attachment path. WebSearch runs server-side and
returned dated quotes. This is worth remembering for every future shallow run, because it
turns "no market cap with an as-of date" from a hard gap into a solvable one.

| Name | Price | As of | Market cap | Bull AI's undated figure |
|---|---:|---|---:|---:|
| ANTELOPUS | Rs 961.80 | 07-Sep-2026 | Rs 3,365.57 cr | Rs 3,712.26 cr |
| IOLCP | Rs 196.58 | 01-Sep-2026 | Rs 5,763 cr | Rs 5,267.35 cr |
| RACLGEAR | Rs 1,756.7 | 13-Sep-2026 | Rs 2,071 cr | Rs 2,066.33 cr |

Bull AI's undated market cap was 10 percent low on IOLCP, 9 percent high on ANTELOPUS and
within half a percent on RACLGEAR. It is not safe to reason about a recognition gap from it.

**One card was corrected, not just extended.** ANTELOPUS read the recognition gap as CLOSED
on a trailing 41 times taken from the undated market cap. On a dated price and the forward
paths the multiple runs 10.9 to 30.8 times depending on the realised price per barrel, so
the gap is indeterminate and the posture moves from PRICED NARRATIVE (TRAP) to
RESEARCH / WATCH. The PASS verdict is unchanged, because it rests on the absence of a rung
climb and on the PSCs expiring in 2029 and 2030, neither of which depends on the multiple.

**FY27 summary, most-evidenced path per name.** Full derivations and scenario tables are on
the cards.

| Name | FY27 top line | FY27 bottom line | Forward PE | Basis |
|---|---:|---:|---:|---|
| IOLCP | 2,667-2,783 | 205-238 | 24.2-28.1x | Guided revenue growth and EBITDA margin |
| RACLGEAR | 537-593 | 51-60 | 34.6-40.6x | Guided revenue; PBT margin derived |
| ANTELOPUS | 649 | 309 | 10.9x | No guidance; built from Q1 actuals, volume ramp mine |

Rs crore. Only IOLCP guides both lines, and even there the bottom line is derived. RACLGEAR
guides revenue alone. ANTELOPUS guides neither and gives only an exit volume of 2,500 boepd,
so its whole table is a projection and swings by a factor of 2.8 on the barrel price.

**A material fact surfaced that post-dates the corpus.** IOL Chemicals announced a capital
expansion of about Rs 495 cr on or about 09-Sep-2026: ibuprofen capacity from 12,000 to
18,000 MTPA for about Rs 350 cr by December 2027, a CDMO formulations unit of about 1,500
million tablets a year for about Rs 110 cr in Q3 FY2027, and a specialty chemicals plant. It
is marked **PENDING LIVE VERIFICATION** on the card: the BSE attachment of 09-Sep-2026 is
unreachable from here, Bull AI has not indexed it, and the figures come from trade press. A
business update call was held on 11-Sep-2026 and its transcript is not in the corpus. If
confirmed, it cuts both ways, and the IOLCP card now carries it as load-bearing fact 5. A 50
percent capacity addition in ibuprofen is a bet on the old core, and it contradicts the Q3
FY25 call statement that no new ibuprofen plant had been ordered anywhere.

Three sector cap rows are now logged in LESSONS.md OPEN ACTIONS: Oil and Gas E&P, Auto
components, and a ruling for a bulk-API converter with a commodity-solvents leg.

Cards now run 3,380 to 4,300 words. The addenda widened an overrun that was already flagged.
