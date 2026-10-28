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

## Fourth run, 2026-10-18

Eight operator picks, screened in one session: Onward Technologies, Tips Music,
Marushika Technology, Oriental Hotels, DelaPlex, California Software, Mahamaya
Steel, JTL Industries.

**Verdicts.** PROCEED to `/step1` on ONWARDTEC. WATCH on TIPSMUSIC and DELAPLEX.
PASS on MARUSHIKA, ORIENTHOT, CALSOFT, MAHASTEEL and JTLIND. The run-wide
forward table is `screens/forward-view-2026-10-18.md`.

**The corpus rule held in full this time.** This session had egress. Every
document is a PDF on the operator's disk with a page-marked `.txt` beside it.
No Bull AI or Trendlyne call was made. Sources:
- screener.in collector (`screener_collect.py --output-dir --no-drive`, run
  under `py -3.14`; the default `py` lacks `python-dotenv` and `playwright`):
  FY25 and FY26 annual reports, up to four transcripts, the latest deck,
  Financials.xlsx.
- screener.in quarter links (`/company/source/quarter/<id>/<m>/<y>/`), which
  redirect to the BSE PDF; downloaded from `AttachLive/` or `AttachHis/`.
- NSE announcements API (`/api/corporate-announcements`, cookie from the home
  page first; `index=sme` for Emerge names): results, decks, transcripts,
  orders, rating letters and regulatory notices, filtered by subject.
- `fetch_ratings.py` for CARE, CRISIL and Infomerics PDFs. ICRA pages are
  script shells; the rationale PDF downloads plainly from
  `https://www.icra.in/Rating/ShowRationalReportFilePdfViewer/<Id>`.
- Prospectuses: Marushika (17-Feb-2026, from the SEBI filing page iframe) and
  DelaPlex (2024 RHP, NSE Emerge archive).
- Market cap and shareholding: screener.in company page, saved per company as
  `market-data-2026-10-18.md` and labelled a service record.
- Tesseract OCR (`C:\Program Files\Tesseract-OCR`, via pymupdf) for scanned
  pages, marked `[OCR]`. Analysts read OCR table digits from the page image.

BSE's own API answered Access Denied to every scripted call. The BSE archive
paths still serve PDFs.

### Findings worth carrying out of the cards

- **CALSOFT.** Qualified FY26 audit opinion: profit "overstated" by Rs 10.88
  crore of overdue receivables. Rs 20 crore of receivables reclassified as an
  advance for shares in a foreign company, with an emphasis of matter on
  recoverability. Six internal-control material weaknesses. The promoter holds
  86% of the partly paid shares with the Rs 7.50 call unpaid; the call closed
  9-Oct-2026 and what followed is NOT FOUND.
- **MAHASTEEL.** ICRA (B+) and CARE (BB+) both carry it as Non-Cooperating;
  Infomerics BBB and Brickwork BBB+ sit six notches higher, and the AR
  discloses only Brickwork. The pattern fits rating shopping.
- **JTLIND.** Rs 195 crore of related-party loans, all repayable on demand or
  without terms per CARO. Three years of negative operating cash flow
  (Rs -335 crore against Rs 315 crore of profit). An Income Tax Benami Act
  provisional attachment on promoter-held land (02-Mar-2026).
- **ORIENTHOT** is now a merger stub: 25 IHCL shares for 117 OHL shares,
  approved 24-Aug-2026, 25 days after shareholders approved a new 20-year IHCL
  management agreement. The valuation reports are not held.
- **MARUSHIKA.** A Rs 45.06 crore HFCL order announced 29-Apr-2026 and
  cancelled two days later. The certified order book is Rs 35.45 crore, while
  the AR claims Rs 108.56 crore "under execution".
- **DELAPLEX.** About 60% of FY25 revenue went to the promoter-family US parent
  at cost plus. NSE queried its results format twice.
- **TIPSMUSIC.** Related-party purchases from loss-making Tips Films rose to
  26.42% of purchases; AOC-2 shows the Rs 15.53 crore advance as NIL.
- **ONWARDTEC.** A Rs 2.93 crore R&D credit sits inside Q2 FY27 expenses and
  lifts the quarter's margin by 1.7 points; neither the press release nor the
  deck names it.

### Corpus defects recorded

- **Screener quarter links are not reliable for the latest period.** For
  MAHASTEEL the Sep-2026 link served a Reg 74(5) certificate; for CALSOFT it
  served AGM voting results. Neither company has reported Sep-2026. For the two
  SME names every quarter link pointed at the wrong document; those were
  deleted and the NSE originals used. Check the period on page 1 before trusting
  a file name.
- **DELAPLEX FY26 annual report is truncated at source.** NSE serves 9,299,265
  bytes of a file whose linearisation header declares 9,681,762. No reader
  opens it. A `/step1` must get it from the company or BSE.
- **ONWARDTEC Q1 FY27 deck** is truncated (5,767,168 of 5,905,298 bytes). The
  Q2 FY27 deck supersedes it.
- Some PDFs carry a garbled embedded text layer and no `[OCR]` marker
  (ORIENTHOT q-2026-06 and q-2025-12, TIPSMUSIC q-2026-09, MARUSHIKA board
  outcome of 22-May-2026). The extractor only OCRs near-empty pages. Analysts
  read figures from page images.
- Marushika's FY26 AR is 106 MB, over the Read tool's limit; its image-only
  overview pages were rendered and read visually.
- Many filings are byte-identical duplicates of screener downloads.
- `Financials.xlsx` template sheets are empty for most names; data sits only
  in the Data Sheet.

### Known limits of this run

- Cards ran 2,478 to 2,878 words against the framework's 1,400 to 1,900,
  under a brief that asked for 1,900 to 2,600. Flagged rather than trimmed.
- MARUSHIKA and DELAPLEX report half-yearly; the proof test is a
  two-half-year test on both.
- Credit ratings are old or absent on five names: ONWARDTEC (ICRA withdrawn
  Nov-2023), TIPSMUSIC (CARE withdrawn Jan-2022), JTLIND (2021-2023 only),
  MARUSHIKA, DELAPLEX and CALSOFT (none found).
- No Q2 FY27 transcript was held for ONWARDTEC or TIPSMUSIC; both calls had
  just happened.

## Fifth run, 2026-10-18 (second batch)

Fourteen operator picks: Ratnaveer Precision, Jayaswal Neco, Mahamaya Steel,
Sagardeep Alloys, Silkflex Polymers, National Fittings, Sharvaya Metals, Aztec
Fluids & Machinery, Singer India, McLeod Russel, Solara Active Pharma,
Dhanlaxmi Bank, Monolithisch India, Valiant Laboratories. Mahamaya Steel had
been screened that morning from the same corpus (fourth run) and was not
repeated. Valiant's 2026-09-06 card was rewritten in full, with a "what
changed" section.

**Verdicts.** No PROCEED. WATCH on JAYNECOIND, DHANBANK, SILKFLEX, NATFITTING,
SOLARA, SINGERIND, MONOLITH and VALIANTLAB. PASS on RATNAVEER, SAGARDEEP,
SHARVAYA, AZTEC and MCLEODRUSS. Forward table:
`screens/forward-view-2026-10-18b.md`.

**Sources, as in the fourth run, plus two new routes.**
- **BSE-only names** (NATFITTING, SHARVAYA, AZTEC): BSE's API refuses scripted
  calls, but the same call made from the bseindia.com page in the in-app
  browser returns the announcement list (the date range must be 12 months or
  less). Attachments then download plainly from `AttachHis/` or `AttachLive/`.
  Bull AI `list_document_availability` (free) confirmed what exists.
- **India Ratings** pages are script shells. JAYNECOIND's 05-Feb-2026 release
  was rendered in the browser and saved verbatim as text.
- OCR now runs per page inside the extractor, so every OCR'd page carries
  `[OCR]`. Pages with a garbled native text layer still carry no marker;
  analysts read those figures from the page image.

### Findings worth carrying out of the cards

- **MCLEODRUSS.** Adverse audit opinion plus a going-concern paragraph. The
  Rs 1,288.95 crore debt write-back is booked but revocable until the NARCL
  restructuring agreement is signed. ICRA D, issuer not cooperating, since 2019.
- **JAYNECOIND.** Cheapest real earnings in the batch (about 11x forward), but
  the MD's conviction is under appeal, an ED attachment hearing is set for
  28-Oct-2026, and 99.87% of promoter shares are pledged to the NCD holders.
- **NATFITTING** is a change of control: Himgiri Castings and the Agarwal
  family bought 34.04% at Rs 130 and now merge two family companies into the
  listed one, issuing 78% new equity. The valuation report is not held.
- **SHARVAYA.** EBITDA margin fell from about 16% to 2.9% in H2 FY26, then the
  board approved a share swap with a family-owned die-caster at the SEBI floor
  price, with relatives classed as public taking almost half.
- **AZTEC.** A bank classed subsidiary Jet Inks as NPA from Aug-2025 to
  Mar-2026; the annual report does not mention it.
- **RATNAVEER** capitalised self-generated costs of Rs 179 crore over FY25 and
  FY26, 1.6x the profit of those years; FY26 operating cash flow was negative;
  promoters took none of the Rs 330 crore rights issue.
- **SOLARA.** The turnaround profit is untaxed. Strides, a promoter-group
  company, bought 24% of FY26 revenue. The ibuprofen review is due within 12
  weeks of 16-Oct-2026.
- **MONOLITH.** A Rs 157 crore take-or-pay quartzite block, 6.8x FY26 profit.
  The holding company is missing from the related-party list, and the company
  lent the Chairman Rs 1.55 crore without repayment terms.
- **SILKFLEX** is a licensed distributor of a Malaysian brand's textile inks
  and binders, not a hose maker; the brief had it wrong. The CFO could not
  reconcile the trading and manufacturing margins on the April 2026 call.
- **VALIANTLAB.** Three NSE queries in 12 months. India Ratings calls the
  Q1 FY27 margin "unlikely to sustain". Corrections to the first card include
  FY26 EBITDA of Rs 6.4 crore, not Rs 64 crore.

### Corpus defects recorded

- **Truncated downloads are the main defect of this run.** Found by analysts:
  MONOLITH FY26 annual report (re-fetched whole, 26.2 MB, card updated),
  NATFITTING price clarification (re-fetched whole, card updated), AZTEC FY26
  results, SHARVAYA 14-Oct-2026 acquisition filing, VALIANTLAB NSE reply of
  01-Jun-2026, MONOLITH Q1 press release, JAYNECOIND Q2 FY27 press release
  (NSE itself serves 2.26 MB of a declared 21.95 MB). The download loops
  accepted any file over 15 KB. **Fix for the next run:** open every PDF after
  download and re-fetch with resume (`curl -C -`) until it parses; where the
  file name carries a byte count (NSE annual reports do), check against it.
- NATFITTING's April 2026 default disclosure is listed by BSE but its archive
  serves an error page under both paths.
- NATFITTING's six Acuité rationale links return 404.
- Byte-identical duplicates across `screener/` and `filings/` on most names.
- Mislabelled files: JAYNECOIND "press release" files are full decks; SOLARA's
  `Investor_Presentation_1.pdf` is a press release; JAYNECOIND `RESULT_FINAL`
  holds EGM votes.

### Known limits of this run

- Cards ran 2,624 to 3,117 words, over the 1,900 to 2,600 the brief asked for.
- Half-yearly reporters, two-half proof test: SILKFLEX, SHARVAYA, AZTEC.
  MONOLITH reports quarterly by choice.
- No transcript exists in the corpus for JAYNECOIND, SAGARDEEP, NATFITTING,
  SHARVAYA, MCLEODRUSS or DHANBANK.
- Credit views are stale or absent on SAGARDEEP (CARE 2017), MCLEODRUSS (ICRA
  D since 2019), NATFITTING (links dead), AZTEC (no SEBI-registered rating)
  and MONOLITH (none).

**Integrity sweep, after both batches.** All 724 corpus PDFs across the 21
names were opened. Nine would not parse. Six were re-fetched whole with
resumed downloads and their `.txt` regenerated: MAHASTEEL Q3 FY26 results
(13-Feb-2026), MONOLITH H1 press release (16-Oct-2025), VALIANTLAB NSE reply
(01-Jun-2026) and Q4 FY26 outcome (14-May-2026), SHARVAYA acquisition filing
(14-Oct-2026), AZTEC FY26 results (29-May-2026). The cards were written
before this repair, from page-image recovery or other filings; the now
readable files are there for `/step1` to confirm against. Three stay broken
because the exchange serves them short: DELAPLEX FY26 annual report,
JAYNECOIND Q2 FY27 press release, ONWARDTEC Q1 FY27 deck.

## Sixth run, 2026-10-26

Two operator picks, screened one after the other in one session: Antelopus
Selan Energy (NSE ANTELOPUS, formerly SELAN; BSE 530075) and Kolte-Patil
Developers (NSE KOLTEPATIL; BSE 532924). Identities confirmed on screener.in;
`/company/SELAN/` now returns 404.

**Verdicts.** WATCH on both. No PROCEED.
- **ANTELOPUS: WATCH, posture EARNINGS-ONLY.** Volumes rose 50% year on year to
  1,656 boepd in Q2 FY27, October ran at 1,950, and H1 FY27 profit was
  Rs 111.61 crore against Rs 23.03 crore. Forward PE about 18.8x on an H1
  run-rate (Tier B, consistent with the Tier A EBITDA guide). Two things carry
  that profit: crude on a West Asia premium, and a ten-year amortisation
  extension booked from 1-Oct-2025 for licences that end in 2029-2030. The
  auditor put an emphasis of matter on it; India Ratings treats the extension
  as an upside trigger, not a given.
- **KOLTEPATIL: WATCH, posture PRICED NARRATIVE (TRAP).** Blackstone holds 40%
  with joint control (the open offer at Rs 329 drew 614 shares). Pre-sales
  fell from Rs 2,822 crore in FY24 to Rs 2,605 crore in FY26; the record
  Q2 FY27 is one launch (Rs 616 crore of Rs 1,019 crore). Four straight
  quarters with no earnings call. GST demands of about Rs 226 crore filed
  Apr-Jun 2026. Forward view Tier D: completed-contract accounting makes any
  run-rate meaningless and no guide exists, so the forward PE is blank.

**Sources.** As in the fourth and fifth runs: screener collector under
`py -3.14`, NSE corporate-announcements API for filings, screener-linked
CARE PDFs and CRISIL HTML rationales, and the BSE `AttachLive/` path for one
BSE-only reply. The India Ratings rationale for Antelopus came enclosed in its
exchange intimation, so no browser render was needed. No Bull AI or Trendlyne
call was made.

**Integrity check, the fix from 2026-10-18, applied.** Every PDF was opened
with PyMuPDF after download, every page's text extracted, page markers matched
to page count, and every file checked for `%%EOF` in its last 2 KB. Downloads
used `curl -C -` with retry. **No file stayed broken** in either corpus. No
file name in this set carries a byte count to check against.

**Corpus gaps.**
- ANTELOPUS: no concall transcript exists anywhere (NSE, screener.in, company
  site); the Q2 FY27 call took place after results on 26-Oct-2026. The
  private-equity owner behind Blackbuck Energy Investments is unnamed in the
  annual report. The independent reserve report is not filed.
- KOLTEPATIL: no transcript after Q1 FY26 because no call was held for Q2 FY26
  to Q1 FY27. Q2 FY27 financial results not yet filed (operational update
  only). No project-level margin disclosure. No FY27 profit guidance.

**Session note.** An earlier, interrupted session of this same scheduled task
had collected most of the ANTELOPUS corpus about ten minutes before this run
started. Those files were checked under the integrity rule above and reused,
not re-downloaded. NSE served the Kolte-Patil filings slowly (about one file a
minute late in the run).

**Known limits.** Cards ran 3,211 words (ANTELOPUS, tables included) and 2,981
words (KOLTEPATIL) against the brief's 1,900 to 2,600. Flagged, not trimmed.

## Seventh run, 2026-10-27

Two operator picks, screened in parallel by two agents in one session:
Accent Microcell (NSE SME ACCENTMIC, no BSE code) and Achyut Healthcare (BSE
543499, scrip ID ACHYUT, no NSE listing; BSE Main Board since 02-Jan-2026).

**Verdicts.** WATCH on ACCENTMIC, PASS on ACHYUT. No PROCEED.
- **ACCENTMIC: WATCH, posture PRICED NARRATIVE (TRAP).** H1 FY27 revenue
  Rs 174.83 crore and PAT Rs 31.12 crore; EBITDA margin 25.11% against 19.02%.
  Trailing PE about 27.9x. Forward PE about 25.5x on an H1 run-rate (Tier B).
  The margin step-up coincides with a 92% fall in bought-in stock while both
  plants already ran full; Unit III has missed three start dates; a Rs 17 crore
  inter-corporate deposit has no named counterparty; promoter holding fell from
  55.47% to 51.40% with no sale filing found. CARE A- (upgraded) against CRISIL
  BB- Issuer Not Cooperating.
- **ACHYUT: PASS, posture PRICED NARRATIVE (TRAP).** A merger stub: the board
  approved its merger into Zenith Healthcare (BSE 530665) on 14-Jul-2026 at
  119 Zenith shares for 50 Achyut. No valuation report is filed. The plant date
  moved from January 2025 to January 2026 and was reprinted after it passed;
  CWIP is Rs 31.62 crore. Pure trading today; H1 FY27 revenue fell 15%.
  Forward PE about 457x.

**Sources.** Screener collector under `py -3.14` for annual reports; the NSE
SME announcements API for ACCENTMIC; the BSE announcements API for ACHYUT,
called from the in-app browser because scripted calls returned Access Denied,
with PDFs from `AttachLive/` or `AttachHis/`; CARE and CRISIL rationales for
ACCENTMIC; the 2022 SME prospectus for ACHYUT. No Bull AI or Trendlyne call.

**Integrity check.** All 44 ACCENTMIC and 225 ACHYUT PDFs open, page markers
match page counts, every file ends with `%%EOF`. ACCENTMIC's annual-report
byte counts match their file names. No broken file.

**Orchestrator spot check.** Five figures per card were checked against the
cited page text. All ten matched.

**Corpus gaps.**
- ACCENTMIC: no H1 FY27 call held by 27-Oct-2026; the Dec-2023 IPO prospectus
  NOT FOUND on screener.in, the NSE IPO APIs or the Emerge archive; no
  product revenue split; wind-turbine order value not disclosed.
- ACHYUT: no credit rating ("Not Applicable" in the AR); no transcripts or
  decks exist; the merger valuation report, fairness opinion, BSE observation
  letter and NCLT status are not filed; Zenith's accounts not held; the
  commission payee (Rs 63.94 lakh in FY26) is not named.

**Known limits.** Cards ran 2,999 words (ACCENTMIC, by wc) and 2,652 words
(ACHYUT) against the brief's 1,900 to 2,600. Flagged, not trimmed.

## Eighth run, 2026-10-29

Eight operator picks, screened in parallel by eight agents in one session:
Piramal Pharma (PPLPHARMA), Poojaa Precision Engg (BSE SME 544844, scrip ID
PPEL, listed 04-Aug-2026), Zenith Health Care (BSE 530665 only), Sudarshan
Colorants India (SUDARCOLOR, formerly Heubach Colorants India, formerly
Clariant Chemicals India), Shree Pushkar Chemicals & Fertilisers (SHREEPUSHK),
Jyoti Structures (JYOTISTRUC), ESAF Small Finance Bank (ESAFSFB), and Tips
Music (TIPSMUSIC), which was screened on 2026-10-18 and was rewritten in full
with a "what changed" section, the Q2 FY27 transcript now held. The operator
wrote "Pooja Precision" and "Sudarshan Colorants"; both resolved on
screener.in search.

**Verdicts.** PROCEED to `/step1` on SUDARCOLOR. WATCH on ESAFSFB, SHREEPUSHK,
POOJAAPREC and TIPSMUSIC. PASS on JYOTISTRUC, ZENITHHE and PPLPHARMA. The
run-wide forward table is `screens/forward-view-2026-10-29.md`.

**Two step 13 additions, at the operator's request of 2026-10-29.** Every card
carries, inside step 13 under "Operator additions, 2026-10-29": an FY28
expected PAT and FY28 forward PE on the same tier rules (usually one notch
weaker than FY27), and a confidence band on each year, defined as the
probability that actual PAT lands within 15% of the estimate (HIGH about 70%
or better, MEDIUM about 50%, LOW under 40%), with the one observation that
would move the band. The framework text is unchanged; promoting the additions
needs an operator ruling and a framework PR of its own.

**The screen result, read honestly.** The operator asked for names cheap on
forward earnings with high probability. None is both. The three cheapest
(ESAFSFB 6.6x, SUDARCOLOR 11.1x, JYOTISTRUC 15.8x) are all LOW confidence,
each on one period annualised over a structural event. The two HIGH-confidence
names (POOJAAPREC, TIPSMUSIC) sit at about 38x. SHREEPUSHK at 16.5x is the
MEDIUM-confidence middle.

**Sources.** Screener collector under `py -3.14` for annual reports,
transcripts, the latest deck and Financials.xlsx. **Both NSE and BSE refused
scripted announcement calls this time** (Access Denied on the NSE
corporate-announcements API that worked on 18-Oct and 26-Oct). All filings for
all eight names came from the BSE announcements API called from a bseindia.com
page in the in-app browser, in windows of 12 months or less, with PDFs from
`AttachLive/` falling back to `AttachHis/`. Ratings via `fetch_ratings.py`
(CARE and Brickwork PDFs; ICRA and CRISIL HTML). The Poojaa red herring
prospectus (22-Jul-2026, 374 pages) came from the lead manager's site after a
web search, with BSE listing notice 20260803-8 confirming the SME segment.
Market cap and shareholding from screener.in, saved as
`market-data-2026-10-29.md` per name. No Bull AI or Trendlyne call.

**Integrity check.** All 541 PDFs across the eight corpora open with PyMuPDF,
page markers match page counts, every file ends with `%%EOF`, every downloaded
filing's byte size matches the exchange ledger's declared size, and a
zero-page check passes. Md5 duplicate sets are recorded per corpus in
`dup-sets-2026-10-29.json`. Filings of the same date and byte size as one
already downloaded were not downloaded again and are marked so in the ledger.

**Orchestrator spot check.** Five figures per card, plus two more on each of
the two cards revised mid-run, were checked against the cited page: 44 of 44
matched, eleven of them read from the page image where the text layer is a
scan or garbled.

### Findings worth carrying out of the cards

- **SUDARCOLOR.** H1 FY27 PAT doubled to Rs 44.49 crore in the first half
  under Sudarshan Chemical's control, at 11.1x forward, with operating cash
  flow of minus Rs 24.11 crore and related parties on both sides of the trade
  (24.5% of FY26 sales, 32% of purchases; related-party pricing is the
  auditor's key audit matter). Five board exits or role changes plus the CFO in
  15 months. A Rs 3.87 crore GST order was disclosed four months late and BSE
  queried the delay. The parent holds a filed right to restructure after
  October 2027. The only PROCEED, and a conditional one.
- **ESAFSFB.** A Rs 625 crore technical write-off intimated 1-Oct-2026 is not
  yet in a filed result. Gearing 18.18x and tangible net worth below the
  pre-stress level per CARE, with all three downgrade triggers within one
  point. Gold is 42% of the book; Kerala is 71% of deposits. The forward PAT
  is the credit-cost call and nothing else.
- **JYOTISTRUC.** Rs 159.39 crore a year of NCD accretion charged to reserves,
  not the P&L; nil current tax; legacy receivables of Rs 2,223 crore, 76% of
  assets, under an auditor emphasis of matter; FY26 operating cash flow minus
  Rs 269 crore; four tribunal rulings since Aug-2024 and still no non-fund bank
  limits. Rs 2,288 crore of orders won in October 2026. CEO, chairman and CFO
  all changed between May and October 2026.
- **PPLPHARMA.** H1 FY27 tax of Rs 138.53 crore on profit before tax of
  Rs 74.18 crore while eleven other-audited overseas subsidiaries lost
  Rs 245.59 crore. Carlyle's 17.95% is fully pledged. Executive pay rose 74%
  in a loss year. Net debt to PBILDT 4.28x against CARE's 3.5x trigger.
- **POOJAAPREC.** 3.35x the IPO price in twelve weeks. Customer 1 is 31.75% of
  sales. Promoter-group foundries supply about Rs 35 crore a year of alloy
  under Rs 50 crore annual limits each. The AR states FY26 ROCE as 36% on one
  page and 26.38% on another.
- **SHREEPUSHK.** The FY27 revenue guide moved from Rs 1,500 crore to
  Rs 1,250-1,300 crore to Rs 1,350-1,400 crore in nine months; the FY26 PAT
  guide was missed by 11%. The subsidiary merger was withdrawn at NCLT on
  21-Sep-2026. The CMD's son replaced the only non-promoter non-executive.
- **ZENITHHE.** Director pay is 24x profit before tax, with a 100% increment
  clause passed in 2026. Rs 1.63 crore of loans to unnamed borrowers equal 22%
  of net worth. A Rs 100 crore related-party window with Achyut was passed by
  5.8% of public shares. After the merger today's holders keep 8.55%.
- **TIPSMUSIC.** The growth is volume at a flat 5-paise rate; the yield thesis
  the card was built on has not fired. Receivables rose 41% against revenue up
  28%. The CEO seat has been vacant since April 2026. The YouTube Shorts deal is
  four months late.

### Corpus defects recorded

- **Pagination bug in the browser-side BSE fetch.** For names fetched in two
  12-month windows, the second window stopped after its first page of 50 rows,
  because the page loop compared the cumulative row count against the second
  window's total. Two analysts found the hole (SUDARCOLOR and JYOTISTRUC, no
  filings from mid-Oct-2025 to Mar-2026). Both windows were refetched, 32
  filings added (Q2 and Q3 FY26 results among them), both cards and manifests
  revised; neither verdict changed. ZENITHHE and POOJAAPREC were checked and
  were complete.
- **A resumed BSE download produced a full-size file with an empty page tree**
  (SUDARCOLOR, 20250716_47755654): the first downloader was killed mid-file and
  the second resumed it with `curl -C -` against a path that re-served the file
  from byte zero. The orchestrator's integrity pass accepted it (0 markers = 0
  pages). Fixed by deleting and refetching without resume; the file is now
  byte-identical to its duplicate. **Fix for the next run:** never resume a BSE
  download, and treat a zero-page PDF as broken.
- **Scanned result pages that carry a signature text block** (JYOTISTRUC) have
  more than 40 characters of native text, so the per-page OCR threshold skips
  them and the `.txt` holds only the signature. Analysts read the page image.
  The threshold should become "fewer than 40 characters, or fewer than 200
  characters on a page whose image is mostly ink".
- Garbled native text layers with no `[OCR]` marker, as in earlier runs:
  SUDARCOLOR Q2 FY27 p.3 (44.49 read as ^449), SHREEPUSHK result statements,
  ZENITHHE FY26 results p.7, an IDC recommendation scan. Figures read from the
  page image in every case and so marked in the manifests.
- BSE files the same PDF under several categories with different attachment
  names. One copy per date and byte size was downloaded; the rest are marked
  "same date and byte size as" in the ledger. Md5 confirmed the ones checked.
- The orchestrator's task messages carried wrong framing that the analysts
  corrected from the filings: POOJAAPREC is a BSE SME half-yearly reporter,
  not a main-board quarterly one; the JYOTISTRUC and SUDARCOLOR "every quarter
  held" claims were untrue until the pagination fix.

### Known limits of this run

- Cards ran 2,596 to 4,348 words against the brief's 1,900 to 2,600
  (PPLPHARMA and POOJAAPREC inside the band; JYOTISTRUC 4,348 and ESAFSFB
  3,658 the longest, both carrying long citation keys and tables). Flagged,
  not trimmed.
- Q2 FY27 results were not yet filed for ESAFSFB, SHREEPUSHK and JYOTISTRUC,
  so their two-quarter proof tests run on Q4 FY26 and Q1 FY27. PPLPHARMA's Q2
  FY27 call transcript (28-Oct-2026) is not yet filed.
- No transcript or deck exists for ZENITHHE, SUDARCOLOR or JYOTISTRUC.
- Credit views: none for ZENITHHE, SHREEPUSHK (one-page ICRA intimation only)
  and JYOTISTRUC; SUDARCOLOR's four CARE files are Clariant-era 2017-2019;
  PPLPHARMA's ICRA captures are site shells with no rationale.
- PPLPHARMA is a Rs 30,994 crore large cap, outside the small/micro-cap
  mandate; screened because the operator named it.
