# Corpus manifest: CREDENT

Collected 2026-11-04.

## Identity
- Company: Credent Connect N Care Ltd (screener.in /company/CREDENT/, standalone and /consolidated/ both resolve)
- NSE symbol: CREDENT (NSE SME only). BSE code: none. ISIN: INE1KPX01025 (from operator)
- Screener URL: https://www.screener.in/company/CREDENT/

## Documents held
| File | Document | Period | Filed | Pages | Text status |
|---|---|---|---|---:|---|
| inputs/screening/Financials.xlsx | Screener export | FY23-FY26 annual, quarters sheet | 2026-11-04 | n/a | binary |
| inputs/screening/Financials.txt | Tab-separated dump of every sheet of Financials.xlsx (written by this run) | same | 2026-11-04 | n/a | text; values are on the "Data Sheet" tab, other tabs are formula shells with no cached values |

No PDFs held.

## Known gaps
- Annual report FY26: NOT HELD. Screener link: https://archives.nseindia.com/annual_reports/SME_AR_31744_CREDENT_2025_2026_A_4289822_07092026182348.pdf (NSE returns HTTP 403 to curl and python requests; browser-based bypass was declined by the permission classifier).
- Last two results: NOT HELD (H1 FY27 filed 28-Oct-2026, H2 FY26 ~May 2026). H1 FY27 NSE links: https://nsearchives.nseindia.com/corporate/CREDENT_28102026190226_FinalOutcomeBM.pdf and .../CREDENT_28102026191521_PressFinal.pdf (403). Company is NSE-only, so the BSE announcements API does not apply. H2 FY26 link not on the screener page.
- Transcript: NOT HELD. Screener lists only intimation/audio-recording PDFs on nsearchives (CREDENT_24102026114001_Earning_call.pdf, CREDENT_29102026185245_Audio_Recording_Of_Earnings.pdf, both 403) and an mp3 link (https://ccreservations.com/recordings/data/10047705.mp3, not fetched, audio).
- Presentation: NOT HELD. https://nsearchives.nseindia.com/corporate/CREDENT_28102026210652_Investor_presentation.pdf (403).
- Credit rating: NOT FOUND. Screener page has no rating documents (looked on the screener page only).
- Shareholding: not in corpus as a document; only whatever the Financials.xlsx holds.
- Defect: screener_collect.py downloads AR/concall/presentation links with a plain requests session; links on this company point to nseindia.com, which returns 403, so the collector prints "Could not download annual reports" and "No concall transcripts found" (the latter is a misleading message: links exist, only the download fails). It also prints an empty "Company:" because get_company_name_from_html reads the first <h1>, which on this page has the name in a nested element (page <title> does hold it).
- Possible fix: operator downloads the six NSE PDFs in a normal browser and drops them in the matching inputs/ folders; then run extract_pdfs.py.
