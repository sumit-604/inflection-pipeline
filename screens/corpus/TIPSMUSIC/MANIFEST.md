# TIPSMUSIC corpus manifest

Company: Tips Music Ltd (formerly Tips Industries Ltd). NSE TIPSMUSIC | BSE 532375 |
CIN L92120MH1996PLC099359. First screened 2026-10-18; card rewritten 2026-10-29 after the Q2 FY27
transcript arrived. Card: `screens/cards/TIPSMUSIC.md`.

Page numbers are PDF pages, which match the `===== PAGE n =====` markers in each .txt. Five pages in the
2026-10-29 BSE filings carry an `[OCR]` marker (see the table). One embedded text layer is garbled (see Defects).

## How it was built

- 2026-10-18 (first build): screener/ via `tools/collector/screener_collect.py https://www.screener.in/company/TIPSMUSIC/`
  (two annual reports, four transcripts, the Q2 FY27 deck, Financials.xlsx); results/ and filings/ from the NSE
  announcement archive under the company's own attachment names (`TIPSINDLTD_<ddmmyyyyhhmmss>_...`); credit-ratings/
  via `tools/collector/fetch_ratings.py` over the agency links on the screener.in page (three CARE PDFs, one CRISIL
  HTML); market-data-2026-10-18.md from the screener.in page.
- 2026-10-29 (top-up): filings/ from the BSE announcements API (`AnnSubCategoryGetData/w`, strCat -1), called from a
  bseindia.com page in the in-app browser because scripted calls to NSE and BSE returned Access Denied. Window
  15-Oct-2026 to 21-Oct-2026, six announcements listed in `bse-announcements-2026-10-29.json`, housekeeping
  categories dropped. Attachments downloaded from `xml-data/corpfiling/AttachLive/` with `curl -C -` and three
  retries. File name = filing date + BSE attachment name. market-data-2026-10-29.md from the screener.in page
  (28-Oct-2026 close).
- Text: PyMuPDF; Tesseract OCR on pages with under 40 characters of native text, tagged `[OCR]`.

## Integrity check

- 2026-10-29: all 49 PDFs (7 screener, 4 credit-ratings, 5 results, 33 filings) opened with PyMuPDF; page markers
  in each `.txt` match the PDF page count; every file ends with `%%EOF`; 5 new filing pages carry `[OCR]`. 11 md5
  duplicate sets, listed in `dup-sets-2026-10-29.json`. **No broken file.**
- 2026-10-18: all PDFs then held opened and page-counted; nine byte-identical pairs found with `cmp` (now inside
  the 11 md5 sets above).

## Documents held

| Path | Type | Period | Pages | Use |
|---|---|---|---|---|
| filings/20261021_b0ec0085-a8d1-42af-b81a-4a6d3ffd59bf.pdf | Q2 FY27 earnings-call transcript, call of 15-Oct-2026, filed 21-Oct-2026 | Q2 FY27 | 15 | NEW 2026-10-29. Read in full. PDF page = printed page plus one. Cited as CC-Oct26 |
| screener/Annual_Report_2026.pdf | Annual report FY26 (filed 8-Aug-2026) | FY26 | 173 | Read in full on 2026-10-18; re-read 2026-10-29 for every cited page (5, 19-22, 25, 33, 35-37, 48, 80, 100-101, 106, 134, 138, 142, 157-158) |
| screener/Annual_Report_2025.pdf | Annual report FY25 (filed 7-Jul-2025) | FY25 | 177 | Skimmed: chairman's letter, RPT notice, director profiles, CARO |
| screener/Concall_Oct_2025_Transcript.pdf | Q2 FY26 call, 15-Oct-2025 | Q2 FY26 | 17 | Read in full; cited pages re-read |
| screener/Concall_Jan_2026_Transcript.pdf | Q3 FY26 call, 19-Jan-2026 | Q3 FY26 | 15 | Read in full; p.3 re-read |
| screener/Concall_Apr_2026_Transcript.pdf | Q4 FY26 call, 23-Apr-2026 | Q4 FY26 | 19 | Read in full; cited pages re-read (public performance claim is p.14, corrected from p.13) |
| screener/Concall_Jul_2026_Transcript.pdf | Q1 FY27 call, 22-Jul-2026 | Q1 FY27 | 14 | Read in full; cited pages re-read |
| screener/Investor_Presentation_1.pdf | Q2 FY27 deck, 15-Oct-2026 | Q2 FY27 | 24 | Read in full; pp.4, 6, 7, 11, 13, 14, 16-19 re-read |
| screener/Financials.xlsx / .txt | screener.in export | FY17-FY26 | n/a | Service record; cross-check only, never cited |
| results/q-2026-09.pdf | Q2 FY27 results, limited review, filed 15-Oct-2026 | Q2 FY27 | 6 | Read in full. p.2 text layer garbled; numbers read from the column stream and checked against IP-Q2 p.17. p.3 note 3 (buyback: 6,71,946 shares, Rs 4,514.50 lakh outflow) read from the OCR-like stream |
| results/q-2026-06.pdf | Q1 FY27 results, limited review | Q1 FY27 | 5 | Read in full; p.3 carries the clean FY26 audited column used for FY26 cost lines |
| results/q-2026-03.pdf | Q4 and FY26 audited results | FY26 | 10 | Read pp.2-4; p.2 text layer partly garbled, FY26 figures taken from AR26 p.35 and R-2026-06 p.3 |
| results/q-2025-12.pdf | Q3 FY26 results (board outcome) | Q3 FY26 | 4 | Skimmed; figures from later comparative columns |
| results/q-2025-09.pdf | Q2 FY26 results | Q2 FY26 | 6 | Skimmed; figures from later comparative columns |
| filings/TIPSINDLTD_15102026140402_TIPSMUSIC_Q2PRESS_RELEASEP.pdf | Q2 FY27 press release | Q2 FY27 | 3 | Read in full. Cited as PR-Q2 |
| filings/20261015_0e733e5e-dfa3-40b4-a6ea-fdeb84d73085.pdf | BSE copy of the Q2 FY27 press release | Q2 FY27 | 3 | NEW 2026-10-29. DUP of PR-Q2 (md5) |
| filings/20261015_45390b7d-4123-4d00-b8e3-7125d77fa1ba.pdf | BSE copy of the Q2 FY27 deck | Q2 FY27 | 24 | NEW 2026-10-29. DUP of screener/Investor_Presentation_1.pdf (md5). 3 pages [OCR] |
| filings/20261015_cae1b916-8a83-4059-a7bf-9cde83cffb37.pdf | BSE copy of the board outcome with Q2 FY27 results (interim dividend Rs 6.50, record date 22-Oct-2026) | Q2 FY27 | 6 | NEW 2026-10-29. DUP of results/q-2026-09.pdf (md5). 1 page [OCR] |
| filings/20261015_50fabef7-acdf-4e70-abe3-1e8cec450829.pdf | BSE copy of the Q2 FY27 results, filed under "Financial Results" | Q2 FY27 | 6 | NEW 2026-10-29. Held (the ledger's "not downloaded separately" note is superseded); DUP of results/q-2026-09.pdf (md5). 1 page [OCR] |
| filings/20261015_fe2f2ebf-61c6-4e68-acf4-109d85060635.pdf | Audio link intimation for the Q2 FY27 call | Q2 FY27 | 1 | NEW 2026-10-29. Read in full; housekeeping, carries the mp3 link only |
| filings/TIPSINDLTD_22072026142132_TIPSMUSICIPP.pdf | Q1 FY27 deck | Q1 FY27 | 24 | Skimmed |
| filings/TIPSINDLTD_23042026142103_TIPSMUSICQ4InvestorPresentationP.pdf | Q4 FY26 deck | FY26 | 25 | Skimmed |
| filings/TIPSINDLTD_19012026133904_TIPSMUSICq3IPp.pdf | Q3 FY26 deck | Q3 FY26 | 25 | Skimmed |
| filings/TIPSINDLTD_15102025135026_TIPSMUSICIRp.pdf | Q2 FY26 deck | Q2 FY26 | 25 | Skimmed |
| filings/TIPSINDLTD_22072026141511_TIPSMUSICQ1PressReleaseP.pdf | Q1 FY27 press release | Q1 FY27 | 3 | Skimmed |
| filings/TIPSINDLTD_23042026141010_TIPSMUSICQ4PressReleaseP.pdf | Q4 FY26 press release | FY26 | 3 | Skimmed |
| filings/TIPSINDLTD_19012026133109_TIPSMUSICq3PRP.pdf | Q3 FY26 press release | Q3 FY26 | 3 | Skimmed |
| filings/TIPSINDLTD_15102025134146_TIPSMUSICPRp.pdf | Q2 FY26 press release | Q2 FY26 | 3 | Skimmed |
| filings/TIPSINDLTD_22072026135035_TIPSMUSICoutcomePf.pdf | Q1 FY27 board outcome (buyback deferred, internal auditor) | Jul-2026 | 5 | Read in full. DUP of results/q-2026-06.pdf |
| filings/TIPSINDLTD_05082026132551_TIPSMUSICOutcome_BBP.pdf | Buyback approval, open market, up to Rs 44.50 crore at up to Rs 750 | Aug-2026 | 4 | Read in full; pp.1-2 re-read |
| filings/TIPSINDLTD_02092026132442_TIPSMUSIC_30AGM_RESULTSp.pdf | 30th AGM voting results | Aug-2026 | 17 | Read items 3-5 (Tips Films RPT passed 99.993%, p.15) |
| filings/TIPSINDLTD_18022026161604_TIPSMUSICssP.pdf | GST search intimation | Feb-2026 | 1 | Read in full |
| filings/TIPSINDLTD_21022026131253_TIPSMUSICsscP.pdf | GST search concluded, no adverse finding | Feb-2026 | 2 | Read in full |
| filings/TIPSINDLTD_05052026122620_TIPSMUSICnpP.pdf | Denial of promoter stake-sale news | May-2026 | 1 | Read in full |
| filings/TIPSINDLTD_07062026185411_TIPSMUSICr30P.pdf | NSE volume clarification | Jun-2026 | 1 | Read in full |
| filings/TIPSINDLTD_20012026151530_TIPSMUSICnpP.pdf | Newspaper advertisement of Q3 results | Jan-2026 | 3 | Skimmed (housekeeping) |
| filings/team_sandeshc_11052026110731_Disclsoure.pdf | SAST Reg 31(4) no-encumbrance declarations, FY26 | Apr-2026 | 11 | Read pp.1-6; rest same form |
| credit-ratings/01-CARE.pdf | CARE withdrawal, 14-Jan-2022 | 2022 | 3 | Read in full |
| credit-ratings/02-CARE.pdf | CARE BBB+ placed on Credit Watch (demerger), 19-May-2021 | 2021 | 5 | Read in full |
| credit-ratings/03-CARE.pdf | CARE upgrade to BBB, 4-Mar-2020 | 2020 | 4 | Skimmed |
| credit-ratings/04-CRISIL.html | CRISIL BB issuer not cooperating, withdrawn, 30-Apr-2019 | 2019 | n/a | Read in full (no page markers) |
| bse-announcements-2026-10-29.json | BSE announcement ledger, 15-Oct to 21-Oct-2026 | 2026 | n/a | Six entries; maps each 2026-10-29 filing to its category and headline |
| dup-sets-2026-10-29.json | md5 duplicate sets, 11 | 2026 | n/a | Orchestrator output |
| market-data-2026-10-29.md | screener.in page: market cap Rs 10,095 crore at Rs 794, PE 44.4, shareholding | 28-Oct-2026 close | n/a | Service record, not filed; cited only as MD |
| market-data-2026-10-18.md | screener.in page of the first screen (market cap Rs 9,498 crore) | 18-Oct-2026 | n/a | Superseded; kept for the "What changed" comparison |

## Duplicate sets (md5, 2026-10-29; `dup-sets-2026-10-29.json`)

1. filings/20261015_0e733e5e = filings/TIPSINDLTD_15102026140402_TIPSMUSIC_Q2PRESS_RELEASEP.pdf
2. filings/20261015_45390b7d = filings/TIPSINDLTD_15102026141908_TIPSMUSIC_IPQ2P.pdf = screener/Investor_Presentation_1.pdf
3. filings/20261015_50fabef7 = filings/20261015_cae1b916 = filings/TIPSINDLTD_15102026134723_TIPSMUSIC_Q2RESULTSp.pdf = results/q-2026-09.pdf
4. filings/TIPSINDLTD_15102025125759_TIPSMUSICresultsP.pdf = results/q-2025-09.pdf
5. filings/TIPSINDLTD_19012026131052_TIPSMUSICbmP.pdf = results/q-2025-12.pdf
6. filings/TIPSINDLTD_21102025082709_TIPSMUSICP.pdf = screener/Concall_Oct_2025_Transcript.pdf
7. filings/TIPSINDLTD_22072026135035_TIPSMUSICoutcomePf.pdf = results/q-2026-06.pdf
8. filings/TIPSINDLTD_23012026215541_TIPSMUSICtranscriptP.pdf = screener/Concall_Jan_2026_Transcript.pdf
9. filings/TIPSINDLTD_23042026135558_TIPSMUSICresultQ4p.pdf = filings/TIPSINDLTD_23042026135813_TIPSMUSICresultQ4p.pdf = results/q-2026-03.pdf
10. filings/TIPSINDLTD_28072026161018_TIPSMUSICecTP.pdf = screener/Concall_Jul_2026_Transcript.pdf
11. filings/TIPSINDLTD_30042026135203_TIPSMUSICq4TP.pdf = screener/Concall_Apr_2026_Transcript.pdf

The company files its results, deck and press release on both exchanges and the BSE copy under two categories, so
the 2026-10-29 top-up added one substantive document (the transcript) and five duplicates.

## Gaps (NOT FOUND, with where it was looked for)

- **Platform-wise revenue split.** Management gave only "25%-30%" for Warner (CC-Oct26, p.14) and declined the
  rest (CC-Oct25, p.12; CC-Apr26, pp.7, 18). Searched AR26 notes 28 and 37(9)(B), pp.142, 159, and BRSR p.80.
  Weakens steps 3 and 9.
- **Volume versus price split of growth.** Declined (CC-Apr26, p.18); the Q2 call gave "primarily volume-driven"
  and no number (CC-Oct26, p.11). Weakens step 8.
- **Warner distribution and minimum-guarantee contract terms.** Not filed; the term runs four years with renewal
  in FY28 (CC-Oct25, p.13; CC-Oct26, p.14).
- **YouTube Shorts renewal terms.** "Still under negotiation" (CC-Oct26, p.4); no filing to 29-Oct-2026.
- **Any credit rating after 14-Jan-2022.** None exists to fetch; the company is debt-free and asked for withdrawal.
  Step 10 rests on the 2021 rationale.
- **Tips Films Ltd annual report and the external valuer reports** on each Tips Films music-rights deal. Not in
  the BSE list or on screener.in for Tips Music.
- **The Sep-2026 shareholding pattern filing itself.** Promoter holding taken from AR26 p.25 (64.15% at
  5-Aug-2026) and the screener record (64.32% at Sep-2026).

## Defects found

- results/q-2026-09.pdf, p.2 (and its three duplicates): the embedded text layer is scrambled OCR. It misreads the
  heading as "September 30, 2025" and "Ma( 17,2026", and column order is lost. The number stream is intact and was
  matched to IP-Q2 p.17 (revenue 12,006.35 lakh, PAT 6,573.95 lakh, tax 2,230.03 lakh). p.3 note 3 and p.5 cash
  flow are in the same state; cash flow taken from IP-Q2 p.19.
- results/q-2026-03.pdf, p.2: same garbling; FY26 cost lines taken from the clean FY26 column of R-2026-06 p.3.
- screener/Financials.xlsx: template sheets empty; data sits only in "Data Sheet".
- credit-ratings/04-CRISIL.txt has no page markers (HTML source).
- filings/team_sandeshc_11052026110731_Disclsoure.pdf: file name misspelt "Disclsoure"; Renu Taurani's
  declaration is dated "April 01, 2025" in the text layer while covering FY2025-26 (p.3; not checked against the image).
- bse-announcements-2026-10-29.json: the "Financial Results" entry says the attachment was not downloaded
  separately; it was, as filings/20261015_50fabef7, and it is md5-identical to the board-outcome copy.
- Disclosure inconsistency inside AR26: AOC-2 (p.48) shows advances to Tips Films "NIL"; Note 16 (p.138) and the
  RPT note (p.157) show Rs 15.53 crore.
- AR26 p.5 (chairman's letter) states FY26 "revenues of Rs 394.3 crores" and "19.6% revenue growth"; that is
  total income. The card uses revenue from operations, Rs 375.51 crore and 20.87%, from p.35.
