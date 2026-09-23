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

### Full-page verification pass on the four live-verdict names, 2026-09-22

At the operator's instruction, QLL, AVIENCE, OPTIEMUS and METALIC were re-read
at full-page level via `get_document_chunks`, six calls in total. Every verdict
held. Five findings did not survive the first pass and are corrected on the
cards.

- **QLL.** The consolidated balance sheet exists, in the management discussion
  rather than the results filing. Group borrowings are Rs 92.97 crore and **net
  debt to EBITDA is about 3.0x**, which fires a tripwire the card set at 2.5x.
  Against that, the FY27 margin guidance turns out to be the delivered H2 FY26
  exit run-rate carried forward, not a step-change, so the growth case is
  stronger and the balance-sheet case weaker than the card first said. Full-year
  EBITDA margin was **flat** at 23.5% against 23.1%, not up from 23% to 24% as
  the deck claims; the deck and the press release disagree.
- **OPTIEMUS. FY26 revenue fell 6.4%**, from Rs 1,890.00 crore to Rs 1,768.62
  crore, and FY26 PAT grew 4.2%. The first pass never showed FY25 and implied a
  growth year. Further: **one customer, the AI+ partnership, was about 57% of Q1
  FY27 revenue**; Rs 14.44 crore of FY26 pre-tax profit was share of associate
  profit rather than operations, and just over half of Q4 FY26 pre-tax profit
  was; segment liabilities grew Rs 773 crore in one quarter; and the two company
  decks disagree on FY26 EBITDA by Rs 14.44 crore, unreconciled. The Cover Glass
  venture is a **70:30 joint venture with Corning International**, which the
  first pass recorded only as an unnamed incubation.
- **METALIC.** The promoter shareholding table **omits the Chairman and Managing
  Director**, who holds 26.72% and is the largest single holder; his shares sit
  inside the stated promoter total but his name is not in the table. Customer
  concentration is improving far faster than the first pass showed: top five fell
  from 63.49% to 45.35% in two years. Promoters voluntarily extended their own
  lock-in to three years, beyond the statutory one and two.
- **AVIENCE.** The 288-product target is 88 CDSCO approvals plus **200
  applications yet to be filed**, not 288 approvals. The first pass built the
  rung claim on an approval count that does not exist. The regulator, previously
  NOT FOUND, is CDSCO.

**Two more reader defects and one tool behaviour recorded.** Bull AI's chunk
reader returns **empty chunks** for AVIENCE prospectus 78f9e436 pages 366-368,
METALIC RHP 23039ecc pages 139-141 and METALIC prospectus 8ccee046 pages 287-288
and 319-322, on two attempts each. Separately, `get_document_chunks` honours
**only one page range per document per call**: a call requesting several ranges
of the same document silently returns the first and drops the rest with no
error. Three requests were lost that way before it was noticed.

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

### Step 13 added, 2026-09-21 (operator ruling)

The operator ranks on next-year bottom-line growth against forward
price-to-earnings. A card that stops at the verdict cannot be ranked, so
`SHALLOW_ANALYSIS_FRAMEWORK.md` gains **step 13, the forward view**, and every
card in this run carries it. The run-wide table is
`screens/forward-view-2026-09-21.md`.

The ruling keeps the three prohibitions: no target price, no buy or sell, and
no forward PE on a loss-maker. What it adds is a basis tier on every estimate,
A for guided down to D for no basis, so a cheap-looking multiple can be read
against how much is actually known.

Eight Bull AI guidance calls were spent building it. They corrected three
cards, which is the argument for running guidance before writing a card rather
than after:

- **FILATEX** — the capex programme adds **Rs 222-234 crore** of steady-state
  EBITDA, not the Rs 150 crore the card carried. A steam distribution platform
  worth Rs 60-65 crore was missing entirely. ECOSIS commissioning moved to
  October 2026 and its capacity is 26,750 TPA.
- **FABCLEAN** — FY25 profit after tax was **Rs 13.30 crore**, so FY26 profit
  grew 18.95% against revenue growth of 46.93%. The Kelvin holding is **60%**,
  not the prospectus figure of 33.33%.
- **TLL** — **domestic revenue reached 49% of FY26.** The export framing on the
  card was out of date.

Two names returned zero guidance records, which is itself a finding recorded on
both cards: **MARINE** and **AVTNPL**.

## Fourth run, 2026-09-22

Fourteen operator picks, screened in one session: Steamhouse India, Technocraft
Ventures, Cresto Techno, PCS Technology, Optiemus Infracom, STL Networks
(Invenia), IntraSoft Technologies, Indo-MIM, Avience Biomedicals, Qualitek Labs,
Tirupati Forge, Metalic Technoforge, Taneja Aerospace & Aviation, DIC India.

**Verdicts.** PROCEED to `/step1` on **QLL** alone, with caveats. WATCH on
**AVIENCE**, **OPTIEMUS** and **METALIC**. PASS on **ISFT**, **TIRUPATIFL**,
**TECHNOCRAF**, **INDOMIM**, **TANAA**, **DICIND** and **STLNETWORK**.
**STEAMHOUSE** is a WATCH for documents, not a business verdict: its Bull AI
corpus is empty. **CRESTO** and **PCS** got no card at all.

That is one PROCEED from fourteen names, the thinnest ratio of any run so far.
The reason is visible in the forward-view table: seven of the twelve names
screened carry a trailing or forward multiple above 30 times, and three above 85
times.

**The corpus rule was bent again, under the same operator ruling as 2026-09-08.**
This session had no egress: the network policy answered 403 to the CONNECT for
docs.bull-ai.in, www.bseindia.com, www.screener.in and every rating agency site.
No PDF could be downloaded and the collector could not run. The corpus is Bull
AI's chunk reader, which returns page-numbered text of the same filed PDFs. Every
card cites a file and a page, and the page numbers are the source PDF's own. What
is absent is the PDF on disk.

**Credit ratings were unreachable on all twelve cards.** Step 10 is NOT FOUND
everywhere, with the agency sites named as where it was looked for. Three cards
record a PARTIAL substitute and they are worth naming because each is a different
kind of independent evidence: **OPTIEMUS** has an ICRA monitoring-agency report
confirming Rs 216.86 crore of Rs 296.37 crore of issue proceeds deployed to
stated objects with no comments; **TECHNOCRAF** has no-objection certificates
from four banks (PNB, Kotak, ICICI, HDFC) dated June 2025; **STLNETWORK** has a
Debenture Trust Deed with quarterly security-cover certificates audited by Price
Waterhouse. None is a credit opinion.

**Three names could not be screened, for two different reasons.**
- **CRESTO** and **PCS** are not in the Bull AI company index. Three passes were
  run, ending with the operator supplying confirmed ISINs: Cresto Techno
  (formerly Silly Monks Entertainment, NSE CRESTO) **INE203Y01012**, and PCS
  Technology **INE834B01012**. Both return "No listed company was found" from
  `list_document_availability`, which is the lookup path that demonstrably
  resolves ISINs. Neither can be screened from this container at all; both need
  a live-web session. See `cards/_NOT_SCREENED-CRESTO-PCS.md`.
- **A pattern claimed in the first pass was wrong and is withdrawn.** The run
  record initially attributed both failures to "BSE-only listings with no NSE
  symbol". Cresto is NSE-listed as CRESTO and is still absent, so BSE-only-ness
  is not the cause. These two companies are simply not in the index.
- **STEAMHOUSE** resolved cleanly but a complete, untruncated availability check
  returned an empty document list. It listed 17 September 2026, five days before
  the screen, so the index has most likely not ingested it yet. Its card carries
  the ledger and no business verdict, the same shape as YAASHVI in the third run.

Bull AI budget: 39 paid calls used, 30 searches, 8 guidance calls and 1 chunk
read covering three documents. Identity and availability probes cost nothing.
`search_companies` and `list_document_availability` are free and were used
freely. 523 of 1,000 remained for the cycle at the close.

### Findings worth carrying out of the cards

- **TIRUPATIFL is the sharpest negative in four runs.** FY26 revenue rose 41% to
  Rs 162.48 crore and net profit **fell** 19.9% to Rs 6.30 crore. Q1 FY27 revenue
  rose 18% and net profit fell 13.6%. Two consecutive periods of rising revenue
  and falling profit. Then two more facts: **40% of FY26 pre-tax profit was
  foreign-exchange gain**, Rs 242.48 lakh of Rs 855.45 lakh; and the promoters
  approved **37,00,000 further warrants at Rs 58** in July 2026 on top of a
  1,17,60,000-warrant issue still converting. At Rs 924 crore of market
  capitalisation that is 147 times trailing earnings on shrinking profit.
- **QLL is the run's one PROCEED and its balance sheet is the reason it is
  capped.** Consolidated revenue grew 77% to Rs 124.52 crore and PAT 90% to Rs
  14.6 crore, with margin expanding, which is rare for acquired growth. But
  standalone borrowings went from Rs 28.22 crore to Rs 64.99 crore, operating
  cash was Rs 7.15 crore against Rs 38.72 crore of investing outflow, receivables
  grew 67% against 47% revenue growth, and **the consolidated cash flow statement
  is not in the corpus at all**. Cash conversion is INDETERMINATE, so the verdict
  caps at PROCEED WITH CAVEATS with the missing evidence named.
- **OPTIEMUS is the clearest case of fast growth that does not screen cheap.**
  Q1 FY27 revenue doubled to Rs 882.99 crore and the cost structure proves it was
  manufactured, not traded: cost of materials consumed went from Rs 149.84 crore
  to Rs 676.01 crore in a year. But EBITDA margin fell to 4.68% from 6.80%, and
  at 2.4% PAT margin a doubling of revenue still leaves a 50x to 60x forward
  multiple. **A thin-margin assembler is levered to margin, not to revenue.**
- **OPTIEMUS also carries the run's one freshness gap on load-bearing news.** The
  operator flagged the stock at 20% upper circuit on screen day because CMF by
  Nothing and Optiemus expanded their partnership to end-to-end smartphone R&D.
  That announcement is **NOT FOUND** in the corpus, whose newest document is
  4 August 2026. The card reads the original September 2025 joint venture instead
  and says so.
- **TANAA is not the business its sector label says.** The screen list calls it
  aerospace and MRO manufacturing. Its own MD&A says it "earns its revenue by
  providing technical support and leasing services" and has "leased hangar space
  and buildings to a Maintenance, Repair and Overhaul (MRO) organization". The
  settling number: **cost of materials consumed is 1.5% of revenue.** It is a
  landlord with an airstrip, which puts it at the R0/R1 boundary where the ladder
  directs NAV treatment rather than a destination PE. The MRO tenant is never
  named in any document, and the group contains related aviation entities.
- **STLNETWORK has Rs 307.15 crore of receivables that did not move in a
  quarter.** Contract assets of Rs 155.74 crore and trade receivables of Rs
  151.41 crore are identical **to the rupee** at 30 June 2026 and 31 March 2026.
  The explanatory note was truncated in the reader. Against annual revenue of Rs
  958.96 crore and a pre-tax loss of Rs 106.15 crore, that is the largest single
  unexplained item in the run.
- **INDOMIM is the best business screened and the price disqualifies it.** 28%
  EBITDA margin, 23.5% ROCE, NADCAP plus AS 9100 plus ISO 13485, top-ten customer
  concentration falling from 42.00% to 38.41% over two years while revenue grew,
  and domestic top-ten revenue rising from Rs 100.56 crore to Rs 591.68 crore in
  one year. Two facts sit against it: the UK acquisition **Conway Marsh & Garrett
  was impaired by Rs 71.13 crore of goodwill** in the year before listing, and
  the IPO was an offer for sale 6.6 times the size of the fresh issue, followed
  by Rs 329 crore of dividend in the listing quarter.
- **METALIC's own peer table is the most useful single page in the run.** It puts
  Metalic against Amic Forging, Tirupati Forge and Paramount Speciality on
  identical FY24 definitions: Metalic ROCE 37.01% against 16.84% for Tirupati
  Forge, on debt-equity of 1.40 and a current ratio of exactly 1.00. Two of this
  run's names appear in one issuer's comparison, and the comparison favours the
  one the operator has not heard of.
- **DICIND's whole management changed in CY2026.** The MD and CEO resigned
  2 June 2026 and left 29 August; a parent nominee became MD on 1 September; a
  new whole-time director and a new deputy CEO were appointed in July. Read
  correctly this is **the Japanese parent taking direct executive control**, not a
  governance failure. The company earns a 4.05% return on equity on a debt-free
  balance sheet, which is an asset and parent-action case, not a GARP transition.

### Reader and collector defects recorded

- **TANAA**, page 18 of document 49529697, FY26 consolidated cash flow: the table
  does not internally reconcile through the reader. Profit before tax of Rs
  2,250.91 lakh with the listed adjustments does not produce the stated operating
  profit before working capital changes of Rs 330.42 lakh, and cash generated from
  operations reads negative Rs 8.80 lakh. No line from that page is used as
  evidence beyond flagging it.
- **STLNETWORK**, note 3 on contract assets, truncated mid-sentence in the reader
  on both the Q1 FY27 filings. The frozen Rs 307.15 crore is visible; the reason
  is not.
- **DICIND** reports to a **31 December** year end and Bull AI's Indian fiscal
  labels are wrong for it throughout. Same defect class as ELANTAS in the second
  run. Every period on that card is restated as a calendar year.
- **DICIND**, page 6 of document 8d0ce5d9: the reader returns the literal string
  "UNREADABLE" inside the notes, and page 3 of document 94f1b7ae returns the
  results table as headings with no figures.
- **Bull AI identity resolution fails on some micro-caps regardless of
  exchange.** CRESTO and PCS failed across fifteen query forms in three passes,
  including a fifty-result name sweep, the former name "Silly Monks
  Entertainment", both confirmed ISINs and the NSE symbol. Both are absent from
  the company index.
- **`search_companies` does not match ISINs, despite its own description.** Its
  documentation says it searches by "company name, NSE symbol, BSE code, or
  ISIN". Control: `search_companies("INE303A01010")` returns **zero results**
  while DIC India is fully indexed under that exact ISIN. The same ISIN resolves
  correctly through `list_document_availability`. **Recommendation for the
  collector, superseding the earlier one: resolve identities with
  `list_document_availability(identifier=<ISIN>)`, which accepts ISINs, returns
  the resolved company block, and is free.**
- **The Bull AI identifier resolver silently substitutes a wrong company.**
  `list_document_availability` with the nonsense identifier `999999` returned a
  full, confident document map for **Balaji Amines Ltd, BSE 530999**, flagged
  `"single_company": true`, with no warning. Separately, both `535043` and the
  adjacent unused `535044` return "Multiple companies match", so that message is
  noise and never evidence a company exists. **Control: read the `company` block
  echoed in every response and confirm the name before using any figure.** Every
  call used in this run was checked that way and every one resolved to the
  intended company.
- **Snippets are not page reads.** Thirty `search_company_documents` calls
  returned page-cited but truncated extracts. Only one `get_document_chunks`
  call was made, covering three documents and five pages. The manifests were
  corrected from "Pages read" to "Pages cited" and each carries the caveat. The
  cites are real and openable; they are not full pages.
- **Operator data conflict on METALIC.** The screen list carries "revenue TTM ~Rs
  343 cr (Jul-2026 data)". The company's restated FY26 revenue from operations is
  **Rs 95.55 crore**. The operator figure appears to belong to another entity and
  is flagged at the head of that card for confirmation.

### Known limits of this run

- Cards ran 1,135 to 3,044 words against the framework's 1,400 to 1,900,
  excluding the two-name not-screened note at 639. **Longer than specified on ten
  of twelve cards, and flagged rather than trimmed**, the same defect the second
  and third runs recorded. The overrun is worst on the names with the most
  documents, which suggests the spec needs either a raise or an explicit
  compression rule for rich corpora.
- **Promoter holding is NOT FOUND on eight of twelve cards**: OPTIEMUS, ISFT,
  STLNETWORK, QLL, DICIND, TIRUPATIFL, INDOMIM and STEAMHOUSE. Four are known
  precisely, all from offer documents: METALIC 61.00% post-issue, TECHNOCRAF
  68.01% post-offer, AVIENCE 64.59% post-issue, TANAA 51.85% from a SAST filing.
  **Bull AI indexes SAST disclosures and offer documents but not shareholding
  patterns**, so recently listed names have this datum and long-listed ones do
  not. This is now the third consecutive run with the same systematic gap.
- **Balance sheet or cash flow is NOT FOUND on nine of twelve cards.** Cash
  conversion is recorded INDETERMINATE on QLL, TECHNOCRAF, TANAA, DICIND and
  STLNETWORK, which caps each verdict per the framework rule with the missing
  evidence named.
- **Four names are read from offer documents alone**: TECHNOCRAF, METALIC,
  INDOMIM and AVIENCE, all listed between June and August 2026. Every competitive
  claim on those four cards is marked as an issuer claim. Same limitation the
  third run recorded for SYMBIOTEC and RSL.
- **Five names have no post-listing or recent result at all.** STEAMHOUSE (no
  documents), METALIC and TECHNOCRAF (listed, nothing filed yet in the index),
  TANAA (latest period 31-Mar-2026), DICIND (latest period 31-Dec-2025).
- **Documents indexed but not read**, each named on its card and manifest for the
  deep run to retrieve: TIRUPATIFL's price-movement query and its "Action(s)
  initiated or orders passed" filing; TANAA's three order-receipt filings;
  DICIND's May 2026 warrant allotment and its litigation-pendency stream; ISFT's
  exchange clarification reply; AVIENCE's FY26 Q4 earnings call transcript;
  INDOMIM's Q1 FY27 profit and loss table on pages 6 to 9 of document 70ca2fe3.

## Fifth run, 2026-09-23

Fourteen operator picks, screened in one session: Advance Agrolife, NOCIL,
South Indian Bank, Jindal Supreme (India), Cubex Tubings, Mukand, Scoda Tubes,
TruAlt Bioenergy, Kavveri Defence & Wireless, Sunflag Iron & Steel, Steel
Exchange India, Pearl Global, KDDL, Premier Polyfilm. The operator supplied NSE
symbol, BSE code and ISIN for each. All fourteen resolved through
`list_document_availability` on the ISIN, and every echoed company block was
checked against the operator's name.

**Verdicts.** PROCEED to `/step1` on **ADVANCE** alone, with caveats. WATCH on
**SOUTHBANK**, **SUNFLAG** and **SCODATUBES**. PASS on **NOCIL**, **PGIL**,
**KDDL**, **TRUALT**, **STEELXIND**, **MUKANDLTD**, **PREMIERPOL**, **JSIPL**,
**CUBEXTUB** and **KAVDEFENCE**. Forward view: `forward-view-2026-09-23.md`.

**Why so few pass the screen.** Three reasons repeat across the ten PASS cards.
1. **Reported profit is not operating profit on three names.** MUKANDLTD's FY26
   PAT of Rs 604.15 crore includes a Rs 554.31 crore land surplus; PBT excluding
   other income was negative in FY26 and in Q1 FY27. CUBEXTUB's other income was
   Rs 8.22 crore against PBT of Rs 9.64 crore. KAVDEFENCE's other income exceeded
   its PBT and its Q1 FY27 revenue was Rs 0.44 crore.
2. **The multiple already pays for the growth on four names.** NOCIL, PGIL, KDDL
   and PREMIERPOL sit at 23x to 45x forward on 10% to 47% growth.
3. **Guidance failed its own test on two names.** TRUALT delivered about 24
   crore litres of ethanol against 37 crore litres guided in February, and the
   change in the allocation mechanism was not disclosed to investors. STEELXIND
   said volumes double "from next quarter"; Q1 FY27 total income fell 11.2%.

**ADVANCE is the one name that screens well without a reversing flag.** Q1 FY27
PAT was Rs 22.54 crore against Rs 8.94 crore, on revenue up 96%. FY27E PAT of Rs
48.9 crore to Rs 56.3 crore gives 12.4x to 14.2x forward. The caveat is the
posture: the proof gate for the climb from formulator to technical maker is the
Unit-4 plant at Gidani, which slipped from Q2 FY27 to Q3 FY27. The transition
matrix reads RESEARCH / WATCH until it fires, so `/step1` is research, not a
position.

**The three WATCH names are three different kinds of WATCH.**
- **SOUTHBANK** is a lender whose asset quality is fixed (GNPA 4.50% to 1.43%
  in eight quarters) but whose earnings quality is not: FY26 operating profit
  excluding treasury fell 4.4%, and Q1 FY27 RoA fell to 1.05%. It sits at 7.1x
  to 7.8x forward. Its market capitalisation of Rs 11,855 crore is above the
  strategy's usual band.
- **SUNFLAG** is a holding-company discount, not a transition. Its standalone
  investments, mostly Lloyds Metals & Energy shares, were Rs 7,695 crore at 31
  March 2026. Its market capitalisation is Rs 6,404 crore.
- **SCODATUBES** has two forward answers: 15.6x to 16.7x on reaffirmed guidance,
  36.4x on the Q1 FY27 run-rate. Q2 FY27 separates them.

**Open action 5 applied, and only partly met.** Full-page reads were run for
all four live verdicts. ADVANCE met all four requirements (two years on one
page, PBT build, leverage, shareholding summing to 100.00%). SOUTHBANK and
SUNFLAG met three; neither shareholding pattern is in the corpus. SCODATUBES met
one fully; its PBT build and shareholding were not read. Each card states which.

**The corpus rule was bent again, under the operator ruling of 2026-09-08.** No
egress: the network policy answered 403 to docs.bull-ai.in, www.bseindia.com,
www.screener.in and the rating agency sites. The corpus is Bull AI's chunk
reader. Every card cites a document id and page; manifests mark which pages
were read whole and which came from search snippets.

**Credit ratings.** Read on two names only: SUNFLAG (Crisil AA-, from its own
large-corporate disclosure) and PREMIERPOL (Crisil BBB+/Stable and A2,
reaffirmed 10 August 2026, under a filing labelled "Revision"). TRUALT filed a
new rating in April 2026; it was listed and not read. Step 10 is NOT FOUND on
the rest.

**How the cards were written.** The orchestrator read the corpus, fixed every
verdict, posture and step-13 number in one decisions file, and wrote one facts
file with document ids and pages. Four writer subagents drafted the cards from
those two files in parallel, with an instruction to write NOT FOUND for any
fact not in the facts file. The orchestrator then checked each card's numbers
against the facts file. Every decimal on every card was matched against the facts,
guidance and decisions files by script; the 26 that did not match were all
labelled derivations and were rechecked by hand. Twelve cites that the writers
left without a page were traced to their filed page and fixed. Cards run 1,528
to 1,937 words; six sit slightly above the 1,900 target.

Bull AI budget: 45 paid calls: 14 guidance calls, 26 searches and 5 chunk calls
covering 12 documents. Identity and availability probes cost nothing. 472 of
1,000 remained for the cycle at the close.

### Findings worth carrying out of the cards

- **Bull AI period labels follow the upload quarter, not the reporting
  quarter.** Five decks and transcripts labelled "FY2027 Q2" carried Q4 FY26 or
  Q3 FY26 content (NOCIL, SOUTHBANK, PGIL, TRUALT, STEELXIND). Read the period
  from the page, never from the label.
- **Filed totals that do not add up.** SUNFLAG's audited FY26 results print a
  Q4 total tax line equal to Q4 PAT, and the Q1 FY27 filing prints FY26 total
  tax as Rs 108.45 crore while its own components sum to Rs 98.45 crore. PAT ties
  only to the component sum.
- **A lapsed certificate list on an exporter's own slide.** SCODATUBES' Q1 FY27
  deck lists PED, AD 2000 and ISO certificates with validity dates that expired
  before the deck was filed. Either the slide is stale or the approvals lapsed.
  A deep run checks the certificate numbers first.
- **A GNPA fall with almost no provision.** SOUTHBANK cut GNPA by Rs 1,300 crore
  in Q4 FY26 while NPA provisions for the quarter were Rs 15 crore. The likely
  reading is a technical write-off of a fully provided book; the annual report
  note decides it.
