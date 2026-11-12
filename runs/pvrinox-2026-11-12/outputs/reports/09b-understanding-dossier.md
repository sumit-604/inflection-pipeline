# PVR INOX (PVRINOX): Halt 1 understanding dossier, 2026-11-12

Stage 09b. Assembly from committed blocks B00 to B09 and verifier blocks B12a to B12d. No valuation, no price view, no decision. Section 2 is a DRAFT for operator sign-off. Section 6 is the Standing Extraction Annex.

Units: figures stay in the source unit. The annual report, results and presentation use Rs million. Calls, rating and screener use Rs Cr. Each figure states its basis: audited (Ind AS 116 reported) or company adjusted (Ind AS 116 adjusted, unaudited). Verifier A source-fidelity findings (B12a) bind: corrected figures are used (goodwill is 3.76x tangible equity, not 5x; FY24 capex Rs 634.4 Cr; four-stream revenue Rs 63,231 million).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00-inputs, B00-intake, and the stage blocks.

1. CONCALLS. Four PVR INOX transcripts are held (B00 concall_quarter_map). File names carry the month of the filing. Call dates come from the transcript headers.

| File | Quarter | Call date |
|---|---|---|
| Concall_Feb_2026_Transcript.pdf | Q3 FY26 | 5 Feb 2026 |
| Concall_May_2026_Transcript.pdf | Q4 FY26 | 11 May 2026 |
| Concall_Jul_2026_Transcript.pdf | Q1 FY27 | 24 Jul 2026 |
| Concall_Nov_2026_Transcript.pdf | Q2 FY27 | 28 Oct 2026 |

Peer transcripts: UFO x4, WONDERLA x4, CINELINE x0 (B00). The most recent quarter covered is Q2 FY27 (quarter ended 30 Sep 2026). Run date is 12 Nov 2026. Q3 FY27 ends 31 Dec 2026, so no later quarter has plausibly reported. No newer transcript is missing.

2. ANNUAL REPORTS. FY2025-26 (primary) and FY2024-25 (prior-year reference) are held (B00). The latest completed FY is present. Two years are held, not three. The FY2023-24 report is absent. The screener Data Sheet gives ten years of consolidated figures (B01), and the FY2024-25 report carries FY24 comparatives (B12a), which narrows the effect.

3. RESULTS FILINGS. Three are held: Q4 FY26 audited (11 May 2026), Q1 FY27 (23 Jul 2026), Q2 FY27 (28 Oct 2026) (B00). The latest results filing is Q2 FY27. The latest annual report covers FY26, so the two periods after it (Q1 and Q2 FY27) are both held. No quarter gap sits between the annual report and the latest results. The Q3 FY26 results filing (Dec 2025 quarter) is not held. The results PDFs are scanned images with an OCR text layer, so load-bearing figures are read at the PDF page (B00).

4. INVESTOR PRESENTATIONS. One is held: Investor_Presentation_1.pdf, the Q2 FY27 investor update tied to the 28 Oct 2026 call (B00). The Q1 FY27 presentation is not held. The Q1 split is derived as H1 less Q2 (B05 input_gaps).

5. RESEARCH / RATING. Rating: CRISIL rationale of 27 Feb 2026, held as text (B00). Broker or research notes: none (research/ is empty, B00). The India Ratings pages need a browser and were not captured (B00).

6. CORPORATE ACTIONS. 19 announcement files sit in inputs/announcements/, dated 26 Jan 2026 to 11 Nov 2026 (my count of the folder; B00 states 17 and does not reconcile the difference of two). Contents by date:
- 26 Jan 2026 and 29 Jan 2026: sale of Zea Maize (4700BC) to Marico.
- 11 May 2026: FY26 press release.
- 25 May 2026: resignation filing, senior management.
- 23 Jul 2026: change in directors.
- 31 Aug 2026: board outcome, buyback. 7 Sep 2026: buyback letter of offer. 5 Oct 2026: completion of extinguishment.
- 7 Sep 2026: company clarification on the news item about an internal probe.
- 28 Sep 2026: SAST 29(2) disclosure (Ajay Bijli). 3 Nov 2026: SAST 31(2) pledge release.
- 29 Sep 2026, 14 Oct 2026, 21 Oct 2026 (2 files), 28 Oct 2026 (2 files), 4 Nov 2026 (Jaipur 5-screen opening), 11 Nov 2026 (investor conference): routine Reg 30 and compliance filings (subjects of the 21 and 28 Oct files not opened in this stage).
Shareholding: NSE XBRL pattern for 30 Sep 2026, broadcast 9 Oct 2026, dumped to text (B00).

7. FRESHNESS PAIR CHECK. B00 freshness_verdict: FRESHNESS PAIRS OK. All four pairs pass: results to same-quarter concall (Q2 FY27 results and the 28 Oct call both held); rating bulletin to rationale (CRISIL full rationale held); SEBI order to order text (none referenced at stage 0); annual report to latest audited annual results (Q4 FY26 audited results and the FY26 annual report both held). No pair failed, so no freshness mate is missing.

Empty input folders and standing gaps, restated in full so the operator sees them. The empty-folder confirmation was suppressed under the /step1 autonomy contract with the standing answer to continue with the gaps (B00).
- research/ is empty.
- prospectus/ is empty and not expected (long-listed company, BSE 532689).
- Screener P&L, Balance Sheet, Cash Flow and Quarters CSVs are absent (empty export) for PVRINOX and CINELINE. Only the Data Sheet CSVs are populated.
- CINELINE has no concall transcripts.
- sector_cap_row is NOT FOUND in the Section 1B cap table. HIGH gap. The operator rules it at the /fttcp pillar gate.
- B08 (promoter) and B09 (market sizing) closed with status partial.
- India Ratings pages were not captured.
- Verifier A shadow was not run in this folder.

8. VERDICT LINE.

CORPUS GAPPED

Findable but missing (operator upload list):
- FY2023-24 annual report, company IR page or BSE. Third year of annual reports.
- Q1 FY27 investor presentation, company IR page or BSE.
- Q3 FY26 results filing and presentation (Dec 2025 quarter), BSE.
- India Ratings rating rationale, rating agency site (browser needed).
- Screener P&L, Balance Sheet, Cash Flow and Quarters exports for PVRINOX and CINELINE: open Financials.xlsx once, save, run collect_to_repo.py --push-again.
- Broker or research notes: operator upload; the company does not publish them.
- SEBI show-cause notice of 22 Nov 2016 to Ajay Bijli, outcome (B08 NOT FOUND), SEBI orders database.
- Merger scheme documents for the PVR-INOX combination (FY23 per B01), BSE filings and the tribunal order. Not in the corpus. Low materiality today.
- CINELINE (Cinelinx India) results and annual report, BSE and NSE. Only a Data Sheet is held.

Plausibly nonexistent (the company publishes no such document, itself a data point):
- CINELINE concall transcripts (screener holds none).
- A consolidated Ind AS 116 bridge from audited Rs 3,328 / 1,761 million to company adjusted Rs 3,868 / 2,306 million (B03, B02: NOT FOUND IN DOCUMENT).
- Unit economics and fee terms of asset-light, FOCO and SMART screens (B04, B07 NOT FOUND; promised "by the time we finish the year", Q1 FY27 call p.13 per B07).
- Basis of the Rs 190 million brand licence fee to the Chairman (B08 NOT FOUND IN DOCUMENT).
- A pledge statement in the annual report (B03: none printed; pledge found only in the NSE filing).

---

## SECTION 2: MENTAL MODEL DECLARATION

DRAFT - PENDING OPERATOR SIGN-OFF

This declaration is a draft. Nothing here is signed. Signing happens only in claude.ai after live-web stress-testing. Every statement traces to a block.

### PART A: THE FROM STATE

A1. ARCHETYPE.
- Movie exhibition line (tickets, F&B, advertising, convenience fees; about 96% of revenue, B04 streams): Brand/franchise consumer (volume growth, pricing power, distribution reach, gross margin, advertising efficiency). The fit is imperfect. Content is licensed from film owners, not owned, and the fixed lease cost sits under it (B04: asset intensity heavy, pricing power moderate, cyclical).
- Film production and distribution line (3.3% of revenue, B04): fits no known archetype. It is project-led with unpredictable income (B04 predictability L). It is too small to carry the model.

A2. THE SIMPLE ANALOGY. PVR INOX rents large halls in malls for years. It fills the halls with films it does not own. The film owner takes about 45 of every 100 rupees of ticket money (B04, film hire 45.3% of ticket sales in FY26). Rent falls due every month whether seats are full or empty. Popcorn and drinks bring extra money from the same visitors. When halls fill, profit grows faster than revenue. When halls empty, losses come fast: FY25 shows a loss when admissions fell 10% (B03). Today the chain is repairing its balance sheet while it adds new halls on other people's money.

### PART B: THE TRANSITION

B1. FROM to TO (QUALITY LADDER, CLAUDE.md).
- Movie exhibition line. FROM: R1 COMMODITY PRICE-TAKER edge, where ROCE is cyclical around the cost of capital. The audited ROCE is about 7.1% for FY26 (B03), and Gate 0 records ROCE at 2.4% to 7.9% over FY23 to FY26 (B01). TO: R2 COST-ADVANTAGED CONVERTER, where margin comes from cost position and ROCE is durable in the mid-teens. Management's own measure (ex-lease, ex-merger goodwill) shows 10.2% for FY26 and 16.5% for the year to Sep 2026 (B01, B03). That measure is not the audited basis. The pre-COVID ROCE benchmark moved from 18% to about 13% between the February and October calls (B12b), so the TO claim rests on a moving yardstick. This is a one-rung claim. The draft does not claim R3.
- Film production and distribution line: no transition claimed.

B2. THE ENGINE. Two things physically change.
1. Occupancy against a fixed cost base. Occupancy moved from 26.2% in FY26 to 30.4% in Q2 FY27 (B04). The ex-Ind AS 116 EBITDA margin moved from 14.4% (FY26, standalone) to 22.3% in Q2 FY27 (B04), and management says the pre-COVID margin returns at 27-28% occupancy (B05 guidance). The mechanism is arithmetic: 1% of admissions is about 13.5% of adjusted profit before tax, and profit before tax breaks even near 139 million admissions against 150 million actual (B04, derived).
2. The mix of new screens. 55% of FY26 additions and 77% of H1 FY27 openings were capital-light, meaning asset-light or FOCO (B03, B05). Capital-light screens cut capex and rent per screen. The corpus does not show what these screens book in the P&L or the fee rate (B04, B07 NOT FOUND). The mechanism is therefore stated but unproven.

B3. THE PROOF GATE. The gate is binary and is read quarter by quarter. Both parts must hold.
- Part 1, volume: admissions grow year on year in each of Q3 FY27 and Q4 FY27, and ATP growth stays at or below admissions growth plus 5 points (B04 must_track healthy band). The base is Q3 FY26 admissions of 40.5 million and ATP of Rs 293 (B05 trigger 1).
- Part 2, margin: the FY27 full-year ex-Ind AS 116 EBITDA margin sits at or above 17%, the lower edge of the pre-COVID 17-18% band (B04), on full-year occupancy at or above 27%.
- Support condition: FY27 gross openings at or above 90 (B05).
Until this fires the transition is narrative and the name is research, not a trade. FTTCP (phase 2) tests this gate. State: NOT FIRED at this date (Q2 FY27 admissions +4% against ATP +14%, B04).

B4. THE RECOGNITION GAP (to be resolved at Stage 11). Open question: does the TO state (R2, durable mid-teens ROCE) already look reflected in market pricing? The corpus holds no market data (B09 input_gaps: current P/E NOT FOUND). This section does not conclude. Stage 11 confirms or denies it through the PE gap. If the TO state is already priced, the re-rating engine is gone and only earnings growth remains. The sector cap row is NOT FOUND (B00), so the operator must rule it first.

B5. THE UGLINESS TEST. Classification: ARTIFACT-OF-CLIMB (provisional, contested).
- Evidence for ARTIFACT: the loss years FY21 to FY25 trace to Covid, the INOX merger and post-merger lease depreciation (B01 depressors); borrowings less cash fell from Rs 9,522 million to Rs 1,619 million in FY26 (B03); gross debt reached about Rs 501 Cr as promised (B05); the Gate 0 core score of 37 on the reported basis rises to 44 on the ex-lease basis (B01).
- Evidence for STRUCTURAL: FY26 admissions of 150 million equal FY24's 151 million, so two years of growth is price (B03); H1 FY27 shows an implied share slip of about 1.8 points (B09, derived); goodwill is 77.7% of equity with no headroom shown (B02); the ex-lease 44 needs the Rs 195.2 Cr Zea Maize gain, and without it the core is 27 (B12c G0-51).
- Separating observation: Q3 FY27 admissions growth against ATP growth, with the industry above +20%. The classification carries into the Stage 13 value-trap test and Role 3. No trade verdict is given here.

B6. THE TRANSITION FALSIFIER. Any of these kills the arrow:
- Q3 FY27 admissions growth near +4% to +8% with ATP above +10% while industry gross box office grows above +20% (B04, B05, B06): price-led share loss.
- FY27 gross openings below 85, or another cut to the screen plan (B05 trigger 4 kill signal).
- Ex-Ind AS 116 EBITDA margin under the 17-18% band at occupancy of 27% or more (B04).
- The ROCE pre-COVID benchmark stays unreconciled and a filed FY19 or FY20 ROCE on the company definition lands near 13% or below (B12b).

### PART C: WHAT THE MODEL WATCHES

C1. DOMINANT VARIABLES (the Role 5.5 tracker signals). Four.
1. Admissions growth against ATP and SPH growth. State: Q2 FY27 admissions +4%, ATP +14%, SPH +14%, income +17.3% against industry GBOC +23% (B04, B05). Occupancy 30.4% (B04).
2. Fixed-cost leverage: rent and CAM growth against revenue growth, film hire share of ticket sales, and ex-Ind AS 116 margin. State: Q2 variable rent +11.6% against income +17.3% (B05 trigger 2); film hire 45.3% in FY26 (B04); margin 22.3% in Q2 (B04).
3. Gross screen openings net of exits, and capital-light unit economics. State: FY27 plan moved from about 150 to 90-100; H1 opened 24 and exited about 25; FY28 guided at 150-175 (B05); fee rate and booking not disclosed (B04).
4. Cash after leases, and the net cash definition. State: net cash Rs 1,407 million at 30 Sep 2026 excludes lease liabilities of Rs 58,079 million (B04); lease cash due in FY27 Rs 12,904 million against Rs 11,847 million paid (B03).
Governance (the kickback matter, pledge, audit chair exit) is carried as the Pillar 3 reader, not as a tracker variable (B08 CAUTION).

C2. WHAT THE MODEL REJECTS. Noise for this model:
- Market size questions. The binding constraint is execution, not the pool. Management's 45,000 screen claim implies a pool 3.41 times the conservative estimate, and screens are not demand (B09 mgmt_claim_ratio 3.41, 0.57 visits per head).
- Reported Ind AS 116 EBITDA margin and EV/EBITDA, P/B and ROE on goodwill, reported debt to equity, headline net debt, CFO to PAT, total screen count growth that includes FOCO screens, and Schedule III ROCE of 47.12% on a lease-excluded base (B04 irrelevant_ratios).
- The 10-year CAGR in profit, which hides five loss years (B01).

C3. THE BUSINESS FALSIFIER. Evidence that forces a re-declaration of the FROM business itself, separate from B6:
- Admissions fall below the fixed-cost break-even near 139 million (B04, derived) in two consecutive years, or admissions per screen fall below 80 thousand (B04 red flag), with price growth capped. The business is then a fixed-cost venue business with no operating leverage, not an occupancy-leverage consumer business.
- Capital-light screens grow to a majority of new revenue and book only management fees (a FOCO screen books fees only, per the Q2 FY27 call p.9, see Section 6 Q3), so revenue per screen is no longer comparable. The business is then partly a fee and franchise platform and the archetype must be re-declared.
- A goodwill impairment on the single-CGU test (B02, B03).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted from B01 to B09 as specified in prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE section. Stage 13's copy remains the final version.

PVR INOX runs 1,797 cinema screens in 114 cities in India and Sri Lanka (B04). Movie tickets bring 53.1% of FY26 revenue and food and beverage brings 31.4% (B04). A ticket gives the viewer a seat for about two hours to see a film that the company does not own, and the film owner takes about 45% of ticket sales (B04). Food and drink earn on the same visit, and advertising at 7.0% and online convenience fees at 3.6% ride on the same seated audience (B04). The customers are moviegoers, and no single customer brings more than 10% of revenue (B13 narrative; AR Note 47). They respond to price. About 15% of FY26 tickets went through discount programmes such as Blockbuster Tuesdays, and the company now offers Rs 99, Rs 149 and Rs 79 value seats (B03, B05). Advertisers form a second customer class, and mall developers act as landlords and, in the asset-light and FOCO models, as partners (B04, B09). Demand today comes from the film slate. Industry gross box office rose 23% in Q2 FY27, with English films up 87%, while releases fell to 386 from 462 (B05, B09). The tracker candidates that follow this demand are the Ormax monthly India gross box office and admissions, the film release count and slate from UFO network data, and the Hollywood and pan-India tentpole release calendar (B09). Demand should grow because screen density is below the China, UK, France and US benchmarks and the country makes 0.57 cinema visits per head a year (B09). The run did not establish a fast market growth rate. The annual report's own chart gives 4.9% a year for CY15 to CY25, against the 7-8% in its text, and holding PVR share flat at 38.4% gives revenue growth of 6.6% and 5.9% a year over three and five years (B09). The forward signals a reader can check outside the company are the developer and mall pipeline behind 138 capital-light screens, competitor screen additions at Cinepolis India, Miraj and Mukta A2, and state ticket price caps, licence timelines and the CCI virtual print fee probe (B09, B05). In tickets and food the company holds a scale and location position of medium strength, a premium format brand on about 16% of screens, and a rent saving of Rs 609 million in FY26, but leases run only 5 to 7 firm years, so no durable moat shows (B04). The emerging moat scan scored 9.4 and classed NONE. Only the repaired balance sheet and the online booking fee line reached Moderate, and both are delivered results, not forming moats (B07). Advertising shows no moat: its income rose 1.3% in H1 FY27 while UFO's in-cinema ad revenue rose 33% in Q1 (B05, B06). Film production and distribution is project-led and no moat is evidenced (B04). No competitor is named in any document, so the rival-sacrifice test scored 0 (B07). The SMART format for Tier 3 and 4 towns is the one attempt at a new position, and with one cinema of four screens open, the run did not establish whether it works (B07, B05).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

One vertical for each dominant variable in Section 2 Part C1.

**Vertical 1: Admissions against price.**
- The corpus establishes: Q2 FY27 admissions +4%, ATP +14%, SPH +14% (B04); company ticket sales +18% against industry +23% (B04); FY26 admissions 150 million against 151 million in FY24 (B03); implied share slip of about 1.8 points in H1 FY27 (B09, derived); Wonderla cut ticket price (-3% in Q2) while footfall grew 6% (B06); ATP of Rs 280 is gross and 15% of tickets went through discount programmes (B03).
- The corpus cannot establish: net-of-discount ATP (B04 NOT FOUND); industry FY26 admissions (B09 NOT FOUND, CY25 832 million used as proxy); multiplex share of industry box office (B09 NOT FOUND); whether the gap to industry is content mix or share loss (B06 UNVERIFIABLE; no exhibitor peer).
- Deciding questions: (1) Does Q3 FY27 admissions growth exceed the Q2 pace of +4% on the 40.5 million base? (2) How much of ATP +14% is mix and how much is price? (3) What happens to admissions in a quarter with no tentpole film?

**Vertical 2: Fixed-cost leverage and margin.**
- The corpus establishes: the cost structure and unit economics (Rs 432 income and Rs 62 EBITDA per admission, standalone adjusted FY26, B04); film hire 45.3% of ticket sales (B04); variable rent growth of 11.6% against income growth of 17.3% in Q2 (B05); the useful-life change cut Q2 depreciation by Rs 211 million, 5.8% of Q2 PBT, with two readings of the annual effect (B05, B12b); a lease write-back of Rs 871 million is 31.6% of FY26 PBT before exceptional items (B02).
- Cannot establish: the consolidated bridge from audited to adjusted profit (B02 NOT FOUND); the normal tax rate once the loss shield ends (B04 question; B02 says about 25.4%).
- Deciding questions: (1) Does the ex-Ind AS 116 margin hold at or above 17% at occupancy near 27%? (2) Does film hire stay under 46%? (3) What does the Q3 FY27 depreciation note say about the effective date?

**Vertical 3: Screen delivery and capital-light economics.**
- The corpus establishes: FY27 gross screens about 150 (Feb), 120-odd (May), about 100 (Jul), 90-100 (Oct); H1 opened 24, exited about 25; net adds "nearly 80" cannot hold (100 less 25 is 75 at most) (B05); FY26 delivered 93 against 100-110 (B03); SMART delivered 1 cinema of 4 screens against 2 pilots and 28-30 screens (B05); the contracted pipeline moved from 149 to 138 and was not updated after May (B05).
- Cannot establish: what asset-light and FOCO screens book, the fee rate, who funds fit-out (B04 NOT FOUND in AR and presentation); the 16-screen count gap among 1,798, 1,789 and 1,782 (B03); the developer link to the unscoped probe (B08).
- Deciding questions: (1) Do FY27 gross openings reach 90 with single-digit exits in H2? (2) Is the pipeline restated against 138? (3) Do three or more SMART cinemas disclose ATP, occupancy and payback?

**Vertical 4: Cash after leases and the net cash label.**
- The corpus establishes: net cash Rs 1,407 million (company) against Rs 132.4 Cr from the balance sheet, Rs 8.3 Cr unreconciled (B01); lease liability Rs 58,079 million outside it (B04); at Mar 2026, supplier finance Rs 1,251 million, deferred consideration Rs 2,036 million and Rs 1,454 million of subsidiary cash sit around net debt (B02); lease cash due FY27 Rs 12,904 million (B03); H1 FY27 free cash Rs 6,035 million has no tax line (B04); the FY26 free cash headline of Rs 790 Cr likely includes Rs 226.8 Cr of sale proceeds (B12b); the buyback of Rs 300 Cr was paid (B08, B01).
- Cannot establish: cash tax in FY27; the covenant terms behind the FY25 waivers (B02); the second distribution under the 30% policy.
- Deciding questions: (1) What cash tax applies once the loss shield ends? (2) Does lease cash stay at or below Rs 12,904 million? (3) Does net debt to EBITDA stay within 0.5x after any distribution?

### 4b. CANDIDATE SIGNAL TABLE

UNVERIFIED. Verification and tracker writes happen at Role 5.5 in claude.ai. Candidates are the eight in B09 downstream_candidates. Source types are as classified in B09.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Ormax monthly India gross box office and admissions | Gross rises while admissions fall year on year for two months running (price-led industry); or industry growth falls below +10% in a quarter with the H2 slate | Monthly | Ormax Media monthly report; Sacnilk (B09) |
| Film release count and slate (UFO Moviez network release data) | Releases stay below the 386 of Q2 FY27 while PVR admissions stay near +4% | Quarterly | UFO Moviez quarterly concall and presentation, Type 1 listed (B09) |
| Cinema AdEx and UFO in-cinema ad revenue | PVR ad income grows in low single digits in Q3 FY27 while UFO ad revenue grows in double digits | Quarterly | Pitch Madison PMAR; UFO Moviez concall (B09) |
| CINELINE (only other listed exhibitor) results | CINELINE admissions or ticket revenue grow faster than PVR's on a lower ATP, which supports share loss | Quarterly | BSE and NSE results and annual report of Cinelinx India (B09) |
| Developer and mall pipeline (Brigade, DLF, other asset-light partners) | Contracted pipeline restated below 138 screens beyond normal conversions, or a named developer exits a signed deal | Event-Driven | Developer concalls and BSE announcements, Type 1; PVR Reg 30 opening filings (B09) |
| Competitor screen additions (Cinepolis India, Miraj, Mukta A2) | Competitor additions in PVR cities outpace PVR gross openings of 90-100, which would pull the 38.4% SAM share down | Event-Driven | Credit rating rationales and trade press, Type 2 unlisted (B09) |
| State ticket price caps, licence timelines and the CCI VPF probe | A cap in a state with a large PVR footprint; a repeat of licence delay that held Q1 FY27 openings to zero; a CCI final order that names executives | Event-Driven | State gazettes, CCI orders, GST Council, Type 5 regulator (B09) |
| Hollywood and pan-India tentpole release calendar | Ramayana Part 1, King or Avengers: Doomsday under-deliver, and Q3 FY27 admissions growth stays near +4% | Event-Driven | Studio earnings and release calendars, Type 3; Ormax (B09) |

### 4c. FRAGILITY READ

- variable_count: 5. The bull case needs: (1) industry content slate and box office strength, (2) admissions growing with price, (3) fixed-cost leverage holding (rent, film hire), (4) screen delivery with capital-light economics that work, (5) the developer and governance matter closing without damage.
- verifiability_ratio: 3 of 5 externally observable. Observable: industry box office (Ormax), admissions against price (company print cross-checked with Ormax), screen openings (Reg 30 filings). Company-narrated only: capital-light unit economics (undisclosed, B04) and the outcome of the kickback review (B08).
- single_point_failure: admissions volume. 1% of admissions is about 13.5% of adjusted PBT and break-even sits near 139 million against 150 million (B04, derived), and FY25 shows a loss when admissions fell 10% (B03). A volume fall alone can break the margin leg.
- fragility_verdict: FRAGILE. Under the Stage 09b rule, one single point of failure sets FRAGILE, and two of five variables are company-narrated only.

### 4d. RESEARCH BRIEF (the claude.ai work order)

Live-web work the corpus cannot do. Items 1 and 2 are the PENDING LIVE VERIFICATION links raised by the 4e chains. Items 3 to 5 are the chains still to be built to reach the Rule F floor of five. Source URLs must be opened and checked in claude.ai before use.

1. PENDING LIVE VERIFICATION (Chain 1, Link 1): open the Ormax Media India box office monthly reports for October 2026 to January 2027 (admissions and gross by language, by month) and the UFO Moviez Q3 FY27 release data. Read who is paying the higher ticket price and whether industry admissions are rising or falling.
2. PENDING LIVE VERIFICATION (Chain 2, Link 1): open the latest quarterly investor presentation and concall of Brigade Enterprises and DLF, and any exchange filing by the developers of the six H1 FY27 openings (Pres p.24), for the fit-out contribution, the lease or revenue-share terms with PVR INOX, and the status of each cinema anchor deal.
3. Build Chain 3 (advertising): UFO ad revenue +33% in Q1 FY27 against PVR H1 +1.3% (B06, B05). Open the Pitch Madison PMAR and the UFO Q3 FY27 call for ad revenue growth, the exhibitor share of ad revenue, and whether advertisers book film by film. Name the advertiser-side document to open.
4. Build Chain 4 (lease and landlord): lessor claims of Rs 964 million (+34%), CWIP impairment of Rs 78 million on a landlord dispute, and lease cash due of Rs 12,904 million (B03, B02). Open the rating rationales of two large mall developers for rent-escalation behaviour and exit-clause use.
5. Build Chain 5 (content supply and film hire): releases 386 against 462 and film hire at 45.3% against a 46% red line (B09, B04). Open producer or distributor filings for the revenue-share terms on the H2 slate (Ramayana Part 1, King, Avengers: Doomsday).
6. Kickback matter: open every BSE and NSE announcement after 7 Sep 2026 and the FY27 annual report for a named, scoped review report or an audit committee statement (B08, gate items). Check whether any developer named in the 138 pipeline is linked.
7. Promoter searches B08 could not run: SEBI orders database, SAT, eCourts, NCLT, MCA and RoC (ATC Logistical Solutions, INOX Infrastructure), and ED, PMLA, income-tax and SFIO checks. Close the 22 Nov 2016 SEBI show-cause outcome.
8. Pledge: pledge levels for 2023 and 2024, the source of funds for the 2 Nov 2026 release, and the pledgee on the remaining 2,122,344 shares (B08 NOT FOUND).
9. Chairman brand fee of Rs 190 million: basis and approval; proxy-advisor views (IiAS, SES, InGovern) on this fee and on the 561x pay ratio (B08).
10. ROCE benchmark: a filed FY19 or FY20 ROCE on the company definition, or an investor-relations reconciliation of 18% (Feb p.18) against about 13% (Nov p.4) (B12b).
11. Market sizing gaps: multiplex share of industry box office, industry FY26 admissions, MovieMax and Carnival screen counts, and dated counts for Cinepolis (496), Miraj (172) and Mukta A2 (73) from rating rationales (B09). Verify the web-sourced items B12a did not check: the 832 million CY25 admissions, the PMAR Rs 877 Cr, and the dentsu-e4m Rs 306 Cr.
12. Exhibitor peer: CINELINE results and annual report from BSE and NSE; competitor rating rationales (B06, B09).
13. Policy: Karnataka ticket cap court outcome, state price caps, the CCI virtual print fee DG report, and licence timelines (B08, B09).
14. Peer gaps: UFO Q2 FY27 ad revenue growth and its Q1 FY26 base (B06 NOT FOUND); Wonderla Q2 FY27 existing-park ATP excluding Chennai (B12d).

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

Two chains drafted from the corpus. Facts carry block cites. Inference is labelled. No counterparty fact is written without a source document.

```
CHAIN 1: Q2 FY27 admissions +4% against ATP +14%, SPH +14%, company income +17.3% and industry gross box office +23% (B04, B05, B09)
Link 1 [PENDING LIVE VERIFICATION]: Who pays, and why now. The payer is the moviegoer, who pays a higher gross ATP while value seats at Rs 99, Rs 149 and Rs 79 were introduced (B05). Counterparty evidence is not in this container. Claude web should open the Ormax Media monthly India box office reports for October 2026 to January 2027 and the UFO Moviez Q3 FY27 release data, to see industry admissions and ATP by month. No counterparty fact is stated here.
Link 2 [VERIFIED filing, corpus]: What binds. A fixed cost base. Profit before tax breaks even near 139 million admissions against 150 million actual (B04, derived). Lease cash due in FY27 is Rs 12,904 million against Rs 11,847 million paid (B03). Film hire runs at 45.3% of ticket sales with a 46% red line (B04). Occupancy rose 170 bps on admissions +4%, which implies capacity fell about 2% (B04 [INFERENCE] carried from the stage). FY25 shows a loss when admissions fell 10% (B03).
Link 3 [INFERENCE]: If ATP keeps growing faster than admissions while industry admissions are flat to down (B09 shows CY25 admissions of 832 million, press-reported down 6%, with gross +13%), then profit rises through price and mix, and the margin gain does not come from filling more seats. A price ceiling, shown by the new value seats, would then cut the margin gain without a drop in occupancy. The Q2 FY27 margin of 22.3% would be read as a price effect, and the proof gate (volume part) would stay unfired.
Binding constraint: net-of-discount ATP is not disclosed (B04 NOT FOUND), so the real price gain cannot be separated from gross ATP. The depreciation change adds 5.8% to Q2 PBT (B05), which masks the operating read.
Unsaid: 15% of FY26 tickets, about 22 million, went through discount programmes (B03, AR MD&A p.89), and no call gave net ATP. H1 FY27 advertising grew only 1.3% against admissions +6% (B05), which the calls blamed on the slate while UFO's ad revenue grew 33% (B06).
Observation that confirms or breaks this chain, and confirm-by date: Q3 FY27 results and investor update, due February 2027. Chain holds if admissions growth is between +4% and +8% on the 40.5 million base with ATP growth above +10% on the Rs 293 base, while industry gross box office grows above +20% (B05 trigger 1, B06 hypothesis). Chain breaks if admissions grow near +15% with ATP growth falling.
```

```
CHAIN 2: FY27 gross screen plan cut from about 150 to 90-100, H1 FY27 opened 24 and exited about 25, FY28 guided at 150-175 a year, and the plan runs on 138 contracted capital-light screens while an unscoped developer kickback allegation sits with a growth executive who resigned on 4 May 2026 (B05, B04, B08)
Link 1 [PENDING LIVE VERIFICATION]: Who pays, and why now. In asset-light and FOCO models the developer or franchise owner funds part of the cinema build, and the developers are the same class of counterparty named in the allegation (B08). Counterparty evidence is not in this container. Claude web should open the latest quarterly presentation and concall of Brigade Enterprises and DLF, and exchange filings on the six H1 FY27 openings (Pres p.24), for the fit-out contribution, the lease or revenue-share terms and the status of each anchor deal. No counterparty fact is stated here.
Link 2 [VERIFIED filing, corpus]: What binds. H1 openings were held to zero in Q1 by licence delay (B05). The H2 need is 66 to 76 openings for 90 to 100 (B04). FY27 capex is now Rs 300-320 Cr (B05). Lessor and developer claims are Rs 964 million, up 34%, with a CWIP impairment of Rs 78 million on a landlord dispute (B03). Deposits to lessors are Rs 4,210 million and recovery on closed sites is NOT FOUND (B02). FY26 delivered 93 gross openings against a range of 100-110 (B03).
Link 3 [INFERENCE]: FY28 at 150-175 a year is about 1.6 to 1.9 times the FY26 delivery of 93 (derived from B05, B03). If the contracted pipeline depends on developer relationships and the allegation is unscoped, a fall in the restated pipeline below 138, or a slip in H2 openings, would be the first sign that the capital-light model depends on a counterparty set under question. If openings come in at or above 90, the reading that licence delay alone caused the cut gains weight.
Binding constraint: the contracted pipeline count moved from 149 to 138 and was not updated after May (B05 dropped_triggers), and what asset-light and FOCO screens book is NOT FOUND in the annual report and presentation (B04).
Unsaid: neither the resignation of the growth head nor the audit chair's exit on 24 Jul 2026 was raised on any call, and the 7 Sep 2026 clarification followed a news report (B05, B08). The footnote that matters: the cut from 150 to 90-100 was never named on any call (B05).
Observation that confirms or breaks this chain, and confirm-by date: (a) Reg 30 opening filings and the Q3 FY27 presentation, February 2027, show cumulative FY27 gross openings with the pipeline restated against 138; (b) FY27 gross openings at or above 90 with single-digit exits in H2, read at the Q4 FY27 results and call, April to May 2027. Below 85, or a further cut, breaks the chain (B05 trigger 4).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. PVR INOX is India's largest multiplex chain, with 1,797 screens in 114 cities (B04).
2. It earns 53.1% of revenue from movie tickets and 31.4% from food and drink. Advertising, online fees and film distribution make up the rest (B04).
3. It rents halls for years and pays the film owner about 45% of ticket money. Rent is due even when halls are empty (B04, B03).
4. Moviegoers pay for tickets and food. No single customer brings more than 10% of revenue (B13 narrative). Advertisers and mall developers are the other counterparties (B04, B09).
5. Moviegoers react to price. About 15% of FY26 tickets went through discount programmes, and the company added Rs 99, Rs 149 and Rs 79 seats (B03, B05).
6. Demand today follows the film slate. Industry box office rose 23% in Q2 FY27, led by English films, while the number of releases fell (B05, B09).
7. In Q2 FY27 the company's admissions rose only 4% while ticket price and food spend per head each rose 14% (B04). FY26 admissions equal FY24 (B03).
8. The market grows slowly on the annual report's own chart, at 4.9% a year. More growth needs more screens or more share (B09).
9. The company has a medium moat from scale, location and premium formats, but its leases run only 5 to 7 firm years (B04). The emerging moat scan scored 9.4 and found none (B07).
10. Advertising and film distribution show no moat. UFO's ad revenue grew 33% in Q1 while the company's grew 1.3% in H1 (B05, B06).
11. The mental model, as drafted: a fixed-cost cinema chain moves from a cyclical, low-return operator toward a cost-advantaged one as occupancy rises and new screens come on other people's money. The proof is volume growth with a margin of at least 17% at 27% occupancy. It has not fired yet (Section 2).
12. Fragility is FRAGILE under the stage rule. A fall in admissions alone can break the margin gain, and two of five conditions rest on the company's own word (Section 4c).
13. The corpus could not establish what capital-light screens book in the P&L, the net-of-discount ticket price, the multiplex share of industry box office, or any listed exhibitor peer test. The promoter and market sizing reviews were partial (B04, B09, B08, B06).
14. Open question one: is the recovery footfall, or price and content mix? Q3 FY27 admissions against ticket price decides it (B05, B06).
15. Open question two: does the unscoped developer kickback matter touch the capital-light pipeline? A named, scoped review report would separate the two readings (B08, B12b).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Answered from the corpus in quote-then-comment form. Page anchors are PDF page markers in the page-marked .txt beside each PDF unless the stage report already carried the anchor. Quotes keep the figures as printed; spacing artefacts of the text layer are closed up. NOT DISCLOSED states the reason.

### 1. UNITS

Quotes:
- Annual_Report_2026.pdf p.94 (MD&A, standalone table, Rs million except operating numbers): "Admits (Mn) 150 150 137 137 10%"; "Gross ATP 280 280 259 259 8%"; "Gross SPH 147 147 134 134 10%"; "Occupancy % 26.2% 26.2% 23.0% 23.0% +312 bps".
- Annual_Report_2026.pdf p.28 (CFO letter): "Admissions reached 150.1 Mn, ATP stood at a record INR 280, F&B spend per head reached a record INR 147". Same figures on p.29.
- Investor_Presentation_1.pdf p.8 (Q2 and H1 FY27, text layer scrambles label order, so values are read in pairs and assigned per B04 and B12a): Q2 "262 298", "134 153", "44.5 46.3", occupancy "28.7% 30.4%"; H1 "259 287", "140 156", "78.5 82.9", occupancy "25.4% 27.9%".

Comment: ATP is a gross figure for one product (the ticket) across a basket of all films, formats and screens (B03: gross, 15% of tickets in discount programmes; net-of-discount ATP is NOT FOUND, B04). SPH is F&B revenue per admission, one basket. Q2 FY27 ATP moved Rs 262 to Rs 298 (+13.7%, derived) and SPH Rs 134 to Rs 153 (+14.2%, derived) against admissions 44.5 to 46.3 million (+4.0%, derived). No revenue per case or per tonne applies. Revenue per admission can be derived from FY26 standalone adjusted lines: Rs 432 total income (B04, derived from AR p.94-95).

### 2. SEGMENT CAPITAL AND DEBT

Quote: Annual_Report_2026.pdf p.302 (Note 47, consolidated, Rs million, FY26 then FY25):
- "Allocated Assets 147,321 153,278 | 2,710 1,948 | - 692 | 150,031 155,918" (Movie exhibition | Movie production and distribution | Others | Total).
- "Unallocated assets 6,092 6,706". "Total Assets 156,123 162,624".
- "Allocated liabilities 81,551 91,578 | 785 147 | - 353 | 82,336 92,078". "Total liabilities 82,336 92,090".
- "Capital Employed (allocable) 65,770 61,700 | 1,925 1,801 | - 339 | 67,695 63,840". "Capital Employed (unallocable) 6,092 6,694".
- "Capital expenditure 2,500 3,250 | 87 57 | - - | 2,587 3,307".

Comment: borrowings are not split by segment in Note 47. The note allocates total liabilities only. Total borrowings are Rs 7,586 million at 31 Mar 2026 (4,592 non-current plus 2,994 current) and Rs 14,908 million at 31 Mar 2025 (9,198 plus 5,710), and lease liabilities are Rs 60,205 million (52,634 plus 7,571) against Rs 62,838 million (derived sum), all from the consolidated balance sheet at Annual_Report_2026.pdf p.239. Segment liabilities of Rs 81,551 million are almost the whole liability total, so lease liabilities appear to sit inside them, but the note does not say so. The Q2 FY27 interim segment table sits in the scanned results PDF and was not extracted in this stage.

### 3. GUIDANCE VERSUS ASPIRATION

Classes: (a) guidance with a period, (b) aspiration without a period, (c) capacity or capability only. Call page numbers follow the [page N] markers in the page-marked text.

| Item | Quote | Class | Anchor |
|---|---|---|---|
| FY27 gross screens (Feb) | "next year, we are looking at about 150-odd screens to open" | (a) | Concall_Feb_2026 p.7 (5 Feb 2026) |
| FY27 capex (Feb) | "between Rs. 350 crores to Rs. 400 crores of CAPEX outlay that we are planning for next year" | (a) | Concall_Feb_2026 p.7 |
| ATP growth | "every year we are looking at about 3.5%, 4% increase in ATP" | (b) | Concall_Feb_2026 p.8 |
| SMART pilots | "by July 15 ... at least 2 of them are open, and we're hoping to open close to 28 to 30 screens under this model" ... "this financial year" | (a) | Concall_May_2026 p.8 (11 May 2026) |
| Gross debt | "we intend to bring it down to about INR500 crores levels" | (b) | Concall_May_2026 p.16 |
| Net debt to zero | "While I would not like to comment on the exact timeline, but in near term, it's definitely on the horizon" (analyst proposed 1H FY27) | (b) | Concall_May_2026 p.16 |
| FY27 gross screens (Jul) | "we are on track to add about 90 to 100 gross screens" | (a) | Concall_Jul_2026 p.8 (24 Jul 2026) |
| FY27 net adds | "On a net basis, I think we will be around nearly 80 net screens additions during the financial year '27" | (a) | Concall_Jul_2026 p.8 |
| FY27 capex (Jul) | "Overall, it will be in the ballpark of INR350 crores for the year" | (a) | Concall_Jul_2026 p.8 |
| FY27 gross screens (Oct) | "We remain on track to open up 90 to 100 new screens in FY27 with the bulk of the openings in the second half" | (a) | Concall_Nov_2026 p.5 (28 Oct 2026) |
| SMART cinemas | "We expect to open two or three more SMART Cinemas this fiscal" | (a) | Concall_Nov_2026 p.5 |
| Capital return | "net debt-to-EBITDA remaining within 0.5x after any distribution" ... "we expect to return around 30% of our annual surplus cash flow to shareholders through dividends, buybacks or a combination of the two, with the timing and quantum at the Board's discretion" | (b) | Concall_Nov_2026 p.5 (printed Page 4 of 15) |
| FY28 openings | "150, 175 is a number that we could achieve from next fiscal every year, could be even more"; "roughly 500 screens ... Yes. Yes." | (b) | Concall_Nov_2026 p.8 |
| FY27 capex (Oct) | "this year, we will do around INR300 crores to INR320 crores, INR330 crores in that range, overall capex" ; "next year ... likely to be more than INR350 crores" | (a) | Concall_Nov_2026 p.10 |
| Digital pay-per-eyeball ads | "this is about 8 to 10 months away" | (a) soft period (about mid FY28 per B05) | Concall_Nov_2026 p.9 |
| Depreciation effect | "the depreciation, therefore, is now lower between INR35 crores to INR40 crores a year" | not forward guidance (accounting effect; does not reconcile, B05) | Concall_Nov_2026 p.10 |
| Pre-COVID margin at occupancy | pre-COVID margin at 27-28% occupancy | (a) FY27 | Q4 FY26 call p.13 (per B05; quote not re-read here) |
| F&B cost share | FHC 45% to 45.5% | (a) FY27 | Q1 FY27 call p.15 (per B05; quote not re-read here) |
| Screens FY27 (AGM Notice) | 100-110 | (a) | Annual_Report_2026 p.15 (per B03; quote not re-read here) |
| Premium screens | "20% of network over the next few years" | (b) | FY25 AR (per B03); not restated in FY26 |
| Contracted capital-light pipeline | 138 screens (52 FOCO, 86 asset-light) over 18 months | (c) pipeline capacity | Q4 FY26 call p.9 (per B05) |
| SMART market | "~300 cities and ~1,000 screens" | (c) opportunity size | Investor_Presentation_1 p.25 |
| FY27 revenue, margin, PAT | none given | NOT GUIDED | B05, B03 |

Comment: the screen guide moved 150, then 120-odd, then about 100, then 90-100, and the cut was never named (B05). Net adds of "nearly 80" cannot hold against 25 H1 exits (B05). One finding relevant to B04 and B07: the Q2 FY27 call answered what asset-light and FOCO screens book. Concall_Nov_2026 p.9, Gaurav Sharma: "on the asset-light, we account the entire P&L in our books, the revenue as well as the cost of the cinema operating cost of the cinema. On the franchise, we just account the management fees, which is a share of the property's revenue only." The fee rate, fit-out funding and unit economics are still not disclosed.

### 4. CONCENTRATION

Quotes:
- Customer: Annual_Report_2026.pdf p.303 (Note 47): "The Group does not have revenue more than 10% of total revenue from a single customer."
- Geography: Annual_Report_2026.pdf p.303: "Group mainly caters to the needs of the domestic market and the overseas turnover is not material. Hence, Geographical segment has not been disclosed."
- Product (Rs million, consolidated FY26, p.303): "Income from sale of movie tickets - 35,301 millions", "Sale of food and beverages - 20,884 millions", "Advertisement income - 4,636 millions", "Convenience fees - 2,410 millions", "Income from movie production and distribution - 2,224 millions". Revenue from operations 66,462 (p.302).
- Screen footprint: Investor_Presentation_1.pdf p.26: "Regional Distribution of 1,797 screens": South 34%, North 27%, West 20%, Central 11%, East 8%; Metro 49%, Tier I 29%, Tier II 13%, Tier III 9%.

Comment: tickets are the top product at 53.1% of revenue (B04, 35,301 of 66,462, derived). No top customer is disclosed beyond the 10% statement. Content concentration sits in the film slate: three films carried a large part of FY26 industry box office (Dhurandhar Rs 947 Cr, Dhurandhar The Revenge Rs 922 Cr, Kantara Chapter 1 Rs 724 Cr, B03, MD&A p.85-86), and the risk section lists mitigants only (B03). The company-specific share of any single film is NOT DISCLOSED.

### 5. PROMISE LEDGER

Dates: Q3 FY26 call 5 Feb 2026; Q4 FY26 call 11 May 2026; Q1 FY27 call 24 Jul 2026. Status as scored in B05, with Verifier B's label note (B12b): D15 and D19 should read "tracking to miss" while FY27 is open.

| Date made | Promise | Status | Evidence anchor |
|---|---|---|---|
| 5 Feb 2026 | About 96 gross screens in FY26 | Partial | 93 gross, 18 exits; Q4 FY26 call p.4; AR range 100-110 missed (B05) |
| 5 Feb 2026 | About 150 screens in FY27 | Missed (tracking to miss) | Cut to 120, 100, then 90-100; Feb p.7, May p.5, Jul p.4, Nov p.5 (B05) |
| 5 Feb 2026 | Exits negligible, gross about equal to net | Missed | 18 exits FY26, 25 in H1 FY27 (B05) |
| 5 Feb 2026 | FY27 capex Rs 350-400 Cr | Partial | Now Rs 300-320 Cr; Nov p.10 |
| 5 Feb 2026 | Net debt to negligible level by FY26-end | Delivered | Rs 161.9 Cr at Mar 2026; net cash Rs 80.7 Cr at Jun (B05) |
| 5 Feb 2026 | Advertising marginal growth | Delivered | FY26 ad income +4%, Q4 +15% (PR 11 May p.2, B05) |
| 5 Feb 2026 | ATP +3.5-4% a year | Delivered | FY26 +8%, Q2 FY27 +14%; base case was low (B05) |
| 5 Feb 2026 | ROCE double digits very soon | Delivered | 10.2% FY26, 16.5% TTM, adjusted basis (B05); benchmark dispute in B12b |
| 5 Feb 2026 | Employee cost growth 7-8% | Delivered | H1 +6.8%, Q2 +5.1% (B05) |
| 5 Feb 2026 | Electricity cost falling, solar to accelerate | Partial | Q2 +7.0% (B05) |
| 11 May 2026 | Gross debt Rs 760 Cr to about Rs 500 Cr | Delivered | Rs 501 Cr at 30 Sep 2026 (B05) |
| 11 May 2026 | Net debt zero on the horizon | Delivered | Net cash at 30 Jun (B05) |
| 11 May 2026 | 55-60% of FY27 openings capital-light | Delivered | H1 77% (64% asset-light plus 13% FOCO); Pres p.24 |
| 11 May 2026 | 2 SMART pilots by 15 Jul, 28-30 screens in FY27 | Missed (tracking to miss) | First opened 4 Sep, 4 screens; 2-3 more cinemas; Pres p.24; Nov p.5 |
| 11 May 2026 | Advertising on projected path, no deviation | Missed | H1 +1.3%, Q1 about -2.1% derived (B05) |
| 11 May 2026 | Occupancy only goes up, 27%+ in FY27 | Delivered | H1 27.9%, Q2 30.4% (B05) |
| 11 May 2026 | Pre-COVID margin at 27-28% occupancy | Delivered | H1 18.7% at 27.9%; Q2 22.3% at 30.4% (B05) |
| 11 May 2026 | Toxic and Jana Nayagan released in FY27 | Delivered | Both released in Q2 FY27 (B05) |
| 24 Jul 2026 | Net adds nearly 80 in FY27, closures mostly done in Q1 | Missed (tracking to miss) | H1 exits 25, net -1; 100 gross less 25 is 75 at most; Jul p.8 |
| FY25 AR | Over 50% of FY26 additions capital-light | Delivered | 55% (51 of 93); AR26 MD&A p.91 (B03) |
| FY25 AR | Admissions rebound in FY26 | Delivered | 136.9 to 150.1 million, but FY24 was 151.4 (B03) |
| FY25 AR | JV opens 7-9 food courts in FY26 | Missed | 3 delivered (B03) |
| FY25 AR | Rooftop solar in 47 cinemas in FY26 | Missed (immaterial) | Commissioned at 3 (B03) |
| FY25 AR | Premium screens to 20% of network | Low credibility | 15% to 16%; goal not restated (B03) |

Comment: B05 scores 11 delivered, 3 partial, 5 missed across the 19 call promises, grade B. Verifier B places the grade at the B and C boundary (B12b) for the ROCE benchmark move and the FY26 free cash headline. Financial promises were kept and expansion promises were not.

### 6. RESTATED BASES

Quotes:
- Annual_Report_2026.pdf p.294 (Note 41): "the comparative consolidated statement of profit and loss and consolidated statement of cash flows for the year ended March 31, 2025 has been re-presented to show the discontinued operation, separately from continuing operations."
- Annual_Report_2026.pdf p.258 (Note 2A(ii), supplier finance): "the amount aggregating to H 1,251 millions (March 31, 2025 : H 1,635 million) previously classified under head Trade Payables have been reclassified to Other Financial Liabilities."
- Annual_Report_2026.pdf p.303 (Note 47): "Since, the operations relating to Zea Maize Private Limited ... has been disposed off in the current year ... the food court income is no more considered to be separate segment. Accordingly, the information relating to food court income is disclosed along with movie exhibition segment ... in all the financial periods presented."
- Annual_Report_2026.pdf p.28 chart footnote: "FY'25 numbers have been restated after removing the financials of Zea Maize Pvt Ltd which was divested on 29th Jan 2026".
- Comparative as printed in the latest filing, Note 47 p.302 (Rs million): "Revenue from operations 66,462 56,999"; "Operating profit including share in net loss of joint venture 2,752 (3,582)"; "Profit/(Loss) after tax from continuing operations 1,761 (2,648)"; "Profit/(Loss) after exceptional items and tax from discontinued operations 1,567 (161)".

Comment: the FY25 comparatives are restated for the Zea Maize discontinued operation, and trade payables are reclassified for supplier finance. Verifier A binds on the second: FY24 payables of Rs 6,511 million are as originally filed and include supplier finance, while FY26 payables of Rs 5,948 million exclude Rs 1,251 million (B12a). The FY24 to FY26 change in payable days is on two bases and must not be read like for like. B02 also records that the FY25 contract asset of Rs 131 million was not re-presented, and that the covenant-waiver sentence in the FY25 consolidated note was dropped from the FY26 consolidated note (B02 restatements_found).

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger, merger or preferential issue is in the corpus. Two actions are: the sale of Zea Maize and the Rs 300 Cr buyback.

Zea Maize (4700BC) sale. Quotes:
- 20260126-divestment-5f9b6a89.pdf p.1: "approved the sale of its entire shareholding in its subsidiary, Zea Maize Private Limited ('ZMPL'), which owns the brand '4700BC' (consisting of 93.27% of the paid-up equity share capital of ZMPL), to Marico Limited."
- Same filing p.2, Annexure A: "Consideration received from such sale/disposal; Rs. 226.8 Cr."; "The Buyer is not related to any promoter/promoter group/group companies."; "Whether the sale, lease or disposal of the undertaking is outside Scheme of Arrangement? ... Not applicable".
- 20260129-divestment-update-ccf82b67.pdf: sale "completed on January 29, 2026 and consequently ZMPL has ceased to be a subsidiary".
- Annual_Report_2026.pdf p.294 (Note 41): "consideration of Rs. 2,221 million (net of expenses)"; "carrying value of net assets of the subsidiary as on date of sale was Rs. 269 million"; "excess of consideration received over net assets, which is Rs. 1,952 million is disclosed as 'Exceptional Item' as part of discontinued operations".
Comment: a share sale, so no undertaking definition and no liability allocation clause applies. Agreement date 26 Jan 2026, completion 29 Jan 2026. Turnover Rs 98.66 Cr (1.71%) and net worth Rs 29.53 Cr (0.42%) of the company in the last year (p.2). The Rs 2,036 million deferred consideration on the balance sheet has an unnamed counterparty (B02 question); NOT DISCLOSED in the filings held.

Buyback. Quotes from 20260907-buyback-letter-of-offer-739d7f51.pdf:
- p.1: buyback of equity shares "at a price of ₹ 1,450/- per Equity Share", through the tender offer process.
- p.2: "AN AGGREGATE MAXIMUM AMOUNT NOT EXCEEDING ₹ 300,00,00,000/- ... EXCLUDING THE TRANSACTION COSTS ... THE BUYBACK SIZE REPRESENTS 4.09% AND 4.07% OF THE AGGREGATE OF THE FULLY PAID-UP EQUITY SHARE CAPITAL AND FREE RESERVES".
- p.2 entitlement: "9 Equity Shares for every 157 Equity Shares held on the Record Date" (reserved category for small shareholders); "21 Equity Shares for every 1,108 Equity Shares held on the Record Date" (general category); actual entitlements 5.7330888703% and 1.8953355370%.
- p.5: Board meeting 31 Aug 2026; public announcement 1 Sep 2026; record date 4 Sep 2026; opening 10 Sep 2026; closing 17 Sep 2026; extinguishment by 6 Oct 2026.
- p.6: "up to a maximum of 20,68,965 ... Equity Shares"; p.18: "up to 2.11% of the total number of Equity Share[s] ... as of March 31, 2026".
- p.20: "the following Promoters and Promoter Group ... have expressed their intention vide letters dated Monday, August 31, 2026, to participate in the Buyback and tender up to an aggregate of 5,69,584".
- 20261005-51260852 filing p.1: the company "has extinguished 20,68,965 fully paid-up Equity Shares"; issued capital before extinguishment "9,81,99,962". 20260928 SAST 29(2) filing p.1 (EAA61B68...pdf): "95,907 equity shares of PVR INOX Limited ... held by me, were accepted in the buyback" (Ajay Bijli).
Comment: the full 20,68,965 shares were bought back and extinguished, so shares outstanding fell to 96,130,997 (derived, matches B08). The promoter group held 2,70,34,066 shares (27.53%) before the offer (letter of offer p.19). B08 records that promoters tendered 502,200 shares in the buyback (SAST 29(2)); the single SAST 29(2) letter held here shows 95,907 shares accepted for Ajay Bijli, so the 502,200 total is the sum across promoters and needs the other filings to confirm. The PVR-INOX merger scheme (FY23 per B01) is not in the corpus. Fetch: the BSE scheme filing and the tribunal order from Feb to Mar 2023.

### 8. RELATED-PARTY PERIMETER

Quote: Annual_Report_2026.pdf pp.300-301 (Note 46, consolidated, Rs million, FY26 then FY25). Related parties named:
- Key management and relatives: Ajay Kumar Bijli (MD), Sanjeev Kumar (ED), Pavan Kumar Jain (Chairman), Siddharth Jain, Renuka Ramnath, independent directors, Gaurav Sharma (CFO), Murlee Manohar Jain (CS), and relatives Nayana Bijli, Niharika Bijli, Aamer Krishan Bijli.
- Joint venture: Devyani PVR INOX Private Limited (51% Devyani International, 49% PVR INOX).
- Enterprises with significant influence: PVR Nest, Bijli Realty Private Limited, Shardul Amarchand Mangaldas & Co. (till 21 Oct 2024), INOX India Limited, GFL Limited, Multiples Alternate Asset Management Private Limited, Dhruva Advisors LLP.

| Entity | Nature | FY26 | FY25 |
|---|---|---|---|
| Ajay Kumar Bijli | Remuneration paid | 255 | 235 |
| Sanjeev Kumar | Remuneration paid | 137 | 127 |
| Independent directors (Harris, Kanabar, Baijal, Chandiok) | Sitting fees and commission | 2 each | 0 to 2 |
| Bijli Realty Private Limited | Rent expense | 47 | 48 |
| Bijli Realty Private Limited | Security deposit given | 17 | 17 |
| Aamer Krishan Bijli | Professional fees | 3 | 3 |
| Nayana Bijli | Professional fees | 3 | 3 |
| Niharika Bijli | Professional fees | 3 | 2 |
| Pavan Kumar Jain | Brand licence fees | 190 | 175 |
| Pavan Kumar Jain | Trade payable outstanding | 190 | 175 |
| PVR Nest | CSR expenditure | 14 | 10 |
| PVR Limited Employees Group Gratuity Cum Life Assurance Scheme | Post-employment benefit | 70 | 60 |
| Devyani PVR INOX Private Limited | Investment during the year | 17 | 15 |
| Devyani PVR INOX Private Limited | Investment in equity share capital (balance) | 32 | 15 |
| Remuneration payable | Bijli 132 (122); Kumar 71 (66) | | |

Quote on terms (p.301, note d): "All transactions with related parties are made on terms equivalent to those that prevail in arm's length transactions and within the ordinary course of business. Outstanding balances at the year end are unsecured and settlement occurs in cash."
Comment: GFL Limited, INOX India Limited, Multiples and Dhruva Advisors show no FY26 flows (only a nil-rounded receivable with PVR Nest and Multiples). GFL Limited is the largest promoter-group holder at 16.13% (letter of offer p.19). The Chairman's brand fee of Rs 190 million is fully payable at year end, and its basis is NOT DISCLOSED (B08). Executive pay of Rs 391.38 million is 14.2% of PBT before exceptional items and 561 times the median (B08). The notes exclude expenses reimbursed (note b).

### 9. PLEDGE AND SHAREHOLDING

Quotes: PVRINOX-shareholding-pattern-30Sep2026-NSE-XBRL.txt, NSE master series, "promoter and promoter group %", twelve quarters:

| Quarter end | Promoter and group % | Pledge as filed in the corpus |
|---|---|---|
| 31 Dec 2023 | 27.84 | NOT DISCLOSED (no pattern with pledge held) |
| 31 Mar 2024 | 27.84 | NOT DISCLOSED |
| 30 Jun 2024 | 27.84 | NOT DISCLOSED |
| 30 Sep 2024 | 27.49 | NOT DISCLOSED |
| 31 Dec 2024 | 27.49 | NOT DISCLOSED |
| 31 Mar 2025 | 27.53 | NOT DISCLOSED |
| 30 Jun 2025 | 27.53 | NOT DISCLOSED |
| 30 Sep 2025 | 27.53 | NOT DISCLOSED as a quarter figure; events below |
| 31 Dec 2025 | 27.53 | NOT DISCLOSED as a quarter figure; events below |
| 31 Mar 2026 | 27.53 | NOT DISCLOSED (AR carries no pledge statement, B03) |
| 30 Jun 2026 | 27.53 | NOT DISCLOSED |
| 30 Sep 2026 | 27.02 | 2,944,444 shares |

The master series also lists "01-OCT-2026 | promoter and promoter group % = 27.6". For 30 Sep 2026 the XBRL facts read: "NumberOfSharesEncumberedUnderPledged [ShareholdingOfPromoterAndPromoterGroup_ContextI] = 2944444"; "EncumberedSharesHeldAsPercentageOfTotalNumberOfShares ... = 0.111"; "NumberOfShares ... = 26531866"; "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged ... = true". Pledge events by Ajay Bijli, 20260907-buyback-letter-of-offer p.20: 9 Sep 2025 "5,32,000 ... Pledge Release"; 11 Sep 2025 "3,26,000 ... Pledge Creation"; 30 Oct 2025 "2,50,630 ... Pledge Release"; 31 Oct 2025 "2,50,630 ... Pledge Creation"; 24 Dec 2025 "4,00,444 ... Pledge Creation". Release of 184,300 and 637,800 shares on 2 Nov 2026 (SAST 31(2), 8A020A52...pdf, 3 Nov 2026).

Institutional holding, 30 Sep 2026 (XBRL, share of total shares): mutual funds 28.21%; insurance companies 4.34%; domestic institutions 33.56%; foreign portfolio investors category one 17.11% and category two 2.02%, total foreign institutions 19.12%.

Comment: the pledge belongs to one borrower, Ajay Bijli, who pledged 2,944,444 of his 5,351,298 shares, 55.02% of his holding and 11.1% of the promoter group's (B08). The 2 Nov 2026 release cut it to 2,122,344 shares (-27.9%, derived), 8.0% of promoter holding (B08). The 27.02% promoter figure at 30 Sep 2026 is a denominator artefact. The SAST view shows 27.60% on 96,130,997 shares after the buyback (B08). Pledge levels by quarter before Sep 2025 are NOT DISCLOSED in any document held (B08 NOT FOUND). A derived balance: the 11 Sep 2025 creation of 326,000 shares appears in the letter of offer but not in B08's event table; the B08 pre-24 Dec 2025 balance of about 2,544,000 holds either way, so the balance before 9 Sep 2025 is about 2,750,000 (derived: 2,544,000 + 532,000 - 326,000). The quarter-by-quarter pledge series needs the 12 NSE shareholding patterns, a findable-missing item at BSE or NSE.

### 10. VERIFICATION

Documents quoted, with filename and date:
- Annual_Report_2026.pdf, FY2025-26, approved 11 May 2026 (pp.28, 29, 94, 239, 258, 294, 300 to 303).
- Concall_Feb_2026_Transcript.pdf, Q3 FY26, call 5 Feb 2026 (pp.7, 8).
- Concall_May_2026_Transcript.pdf, Q4 FY26, call 11 May 2026 (pp.8, 16).
- Concall_Jul_2026_Transcript.pdf, Q1 FY27, call 24 Jul 2026 (p.8).
- Concall_Nov_2026_Transcript.pdf, Q2 FY27, call 28 Oct 2026 (pp.5, 8, 9, 10).
- Investor_Presentation_1.pdf, Q2 FY27 investor update, call date 28 Oct 2026 (pp.8, 24, 25, 26).
- 20260126-divestment-5f9b6a89.pdf, 26 Jan 2026; 20260129-divestment-update-ccf82b67.pdf, 29 Jan 2026.
- 20260907-buyback-letter-of-offer-739d7f51.pdf, 7 Sep 2026 (pp.1, 2, 5, 6, 18, 19, 20).
- 20261005-51260852-2044-4845-a773-ca269b43f01d.pdf, 5 Oct 2026.
- EAA61B68_19A1_49C6_91DF_6DA2A9785081_101021.pdf, 28 Sep 2026 (SAST 29(2), Ajay Bijli).
- 8A020A52_79D7_49E5_A1C8_CA010D96901C_164230.pdf, 3 Nov 2026 (SAST 31(2) pledge release).
- PVRINOX-shareholding-pattern-30Sep2026-NSE-XBRL.txt, quarter ended 30 Sep 2026, broadcast 9 Oct 2026.
- Not re-opened for the annex, cited through stage blocks: Annual_Report_2025.pdf, the three results PDFs (scanned), the CRISIL rationale of 27 Feb 2026, and the stage reports B01 to B09.

Rows marked "per B05" or "per B03" in Q3 carry the stage block's anchor, and the quote was not re-read in this stage.

CORPUS COMMIT HASH: 495275190a97df9f2f99acde6f9c4ab722fdcffd

---

```yaml
stage: B09b-dossier
company: "PVRINOX"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "FY2023-24 annual report (third year of annual reports; only FY2024-25 and FY2025-26 held)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Q1 FY27 investor presentation"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Q3 FY26 results filing and presentation (Dec 2025 quarter)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "India Ratings rating rationale (pages need a browser)"
    expected_source: "rating agency site"
    kind: "findable-missing"
  - document: "Screener P&L, Balance Sheet, Cash Flow and Quarters exports for PVRINOX and CINELINE (empty export)"
    expected_source: "screener.in export, operator re-run of collect_to_repo.py --push-again"
    kind: "findable-missing"
  - document: "Broker or research notes (research/ empty)"
    expected_source: "operator upload; the company does not publish them"
    kind: "findable-missing"
  - document: "SEBI show-cause notice of 22 Nov 2016 to Ajay Bijli, outcome; SEBI orders database search"
    expected_source: "SEBI orders database"
    kind: "findable-missing"
  - document: "PVR-INOX merger scheme documents and tribunal order (FY23)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "CINELINE (Cinelinx India) results and annual report"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "CINELINE concall transcripts"
    expected_source: "BSE"
    kind: "plausibly-nonexistent"
  - document: "Consolidated Ind AS 116 bridge from audited to company adjusted profit (3,328 / 1,761 to 3,868 / 2,306 Rs million)"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Unit economics and fee terms of asset-light, FOCO and SMART screens; basis of Chairman brand licence fee"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Movie exhibition (tickets, F&B, advertising, convenience fees)"
    archetype: "Brand/franchise consumer"
  - line: "Film production and distribution"
    archetype: "fits no known archetype"
transition:
  - line: "Movie exhibition"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R2 COST-ADVANTAGED CONVERTER"
    engine: "Occupancy against a fixed cost base (26.2% FY26 to 30.4% Q2 FY27; ex-Ind AS 116 margin 14.4% to 22.3%) and a capital-light screen mix (77% of H1 FY27 openings) whose P&L economics are not disclosed"
    proof_gate: "Admissions up year on year in Q3 and Q4 FY27 with ATP growth at or below admissions growth plus 5 points, and FY27 ex-Ind AS 116 EBITDA margin at or above 17% on occupancy at or above 27%, with FY27 gross openings at or above 90"
    recognition_gap: "Open question: does the TO state (R2, durable mid-teens ROCE) already look reflected in market pricing? No market data in corpus; Stage 11 resolves via the PE gap"
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Q3 FY27 admissions growth near +4% to +8% with ATP above +10% while industry box office grows above +20%; or FY27 gross openings below 85 or another cut; or margin under the 17-18% band at occupancy of 27% or more"
dominant_variables:
  - "Admissions growth against ATP and SPH growth"
  - "Fixed-cost leverage: rent and CAM growth, film hire share, ex-Ind AS 116 margin"
  - "Gross screen openings net of exits, and capital-light unit economics"
  - "Cash after leases and the net cash definition"
business_falsifier: "Admissions below the fixed-cost break-even near 139 million for two consecutive years, or admissions per screen below 80 thousand with price growth capped; or capital-light screens becoming a majority of new revenue booked as management fees only, which re-declares the business as a fee and franchise platform"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 5
  verifiability_ratio: "3 of 5 externally observable"
  single_point_failure: "Admissions volume: 1% of admissions is about 13.5% of adjusted PBT, break-even near 139 million against 150 million, and FY25 shows a loss when admissions fell 10%"
  fragility_verdict: "FRAGILE"
candidate_count: 8
second_order:
  chains_drafted: 2
  pending_live_links: 2
  confirm_by_observations: 2
research_brief_items: 14
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "495275190a97df9f2f99acde6f9c4ab722fdcffd"
```
