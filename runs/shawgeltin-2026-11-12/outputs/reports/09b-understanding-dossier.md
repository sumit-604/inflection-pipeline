# Halt 1 Understanding Dossier: Narmada Gelatines Ltd (SHAWGELTIN, BSE 526739)

Run 2026-11-12. Stage 09b. Assembly from committed blocks B00 to B09, B12a to B12d, B13 and the stage reports with their ERRATA. Sections 1 to 5 add no new research and no new numbers. Section 4e carries labelled inference. Section 6 quotes the corpus directly. Units: AR and results print ₹ lakh; CARE and screener print ₹ crore. AR page anchors give the PDF page, then the printed page (printed = PDF minus 3). All AR quotes come from tesseract OCR of a scanned PDF; where OCR read a comma for a point, the quote keeps the OCR text and the comment gives the corrected figure checked by an earlier stage (B02, B03, B12a).

Standing ERRATA applied: B02 pass 2 "Total 282.62" is 134.03; B03 "41% of the term loan due in year one" is 44%; B04 closing clause on the 2027 bone cycle is withdrawn; B06 HPMC citation is Q4 FY26 p.17; B06 IGCL "NOT FOUND" lines describe the file before commit 6a2339a8. Verifier A corrected values bind: loans and other financial assets 183.88 lakh; salaries plus funds change -272.33 lakh; adjusted FCF 1,295.71 lakh; FY25 sitting fees 8.40 lakh (B12a).

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00-inputs, B00-intake (35 rows, all folder_match true).

1. CONCALLS. None held for NGL: the company holds no earnings calls (B00 concalls_available false). Most recent quarter covered: not applicable. A more recent quarter has reported (Q1 FY27 on 12-Aug-2026) and Q2 FY27 is due on the run date, 12-Nov-2026, but no transcript exists for either because no call is held. Peer transcripts held (not NGL documents): Natural Capsules Q4 FY25 (call 04-Jun-2025), Q2 FY26 (call 17-Nov-2025), Q4 FY26 (call 02-Jun-2026) (B06). Nitta Gelatin and IGCL hold no calls (B00).
2. ANNUAL REPORTS. Held: FY2025-26 (annual-report/NGL-Annual-Report-FY2025-26.pdf; BSE cover letter 21-Jul-2026; Board's Report dated 25-May-2026; scanned, 131 of 133 pages re-read by OCR) and FY2024-25 (other/NGL-Annual-Report-FY2024-25.pdf; BSE cover letter 28-Aug-2025; scanned, no OCR text; held but not consumed by stages) (B00-intake). The latest completed FY (FY2026) is present. Fewer than 3 years are held: two. FY2023-24 is ABSENT. Backward history beyond FY25 comes from screener standalone tables (B00).
3. RESULTS FILINGS. Latest: Q1 FY27 (quarter ended 30-Jun-2026), filed 12-Aug-2026 (results/20260812-Q1FY27-results.pdf; P&L only, no balance sheet or cash flow, B03). Also held: Q4 FY26 audited, 25-May-2026; Q3 FY26, 12-Feb-2026; Q2 FY26 in other/, 12-Nov-2025. Quarter gap between the latest results filing (Jun-2026) and the latest AR (Mar-2026): one quarter. Q2 FY27 (Sep-2026) is ABSENT; the board meeting to approve it is the run date (BSE intimation 02-Nov-2026) (B00).
4. INVESTOR PRESENTATIONS. ABSENT. None on BSE or screener (B00 input_gaps).
5. RESEARCH / RATING. CARE press release 06-Mar-2026 (rating/CARE-Narmada-Gelatines-2026-03-13.pdf; filename date not used, page date 06-Mar-2026), carrying the full rationale. CARE press release 08-Apr-2025 (other/CARE-Narmada-Gelatines-2025-04-14.pdf; page date 08-Apr-2025; outside the named stage inputs, B12b). No broker or research note held (B00).
6. CORPORATE ACTIONS. 14 announcement files, 19-Nov-2025 to 02-Nov-2026 (B00-intake): Reg 30 board circular 19-Nov-2025; postal ballot notice 21-Nov-2025 and outcome 25-Dec-2025; CARE rating intimation 06-Mar-2026; change of RTA 13-May-2026; dividend record date 25-May-2026; secretarial compliance cover 26-May-2026; AGM notice 21-Jul-2026; AGM outcome and scrutinizer report 19-Aug-2026; KYC communication 21-Sep-2026; trading window closure 28-Sep-2026; RTA certificate 09-Oct-2026; board meeting intimation 02-Nov-2026. No file names an order, joint venture, capex, raise or guidance change (B05). Duplicate filings of Q1 FY27 results, Q4 FY26 results and the FY26 AR were not copied in (B00).
7. FRESHNESS PAIR CHECK. B00 freshness_verdict: FRESHNESS PAIRS OK. Results to concall: SKIPPED (no-call company). Rating bulletin to rationale: PASS. SEBI order to order text: PASS (no order found in inventoried pages). AR to latest audited annual results: PASS (FY2025-26 AR present). No failed pair.
8. VERDICT LINE: **CORPUS GAPPED**.
   - Findable but missing (operator upload list): (a) Q2 FY27 results with H1 balance sheet and cash flow, BSE 526739, due 12-Nov-2026; (b) AGM 19-Aug-2026 recording, CDSL webcast via the company, where the MD and CFO answered members' questions (B12b); (c) AR FY2023-24, BSE; (d) NGL Reg 30 filing of 4-Dec-2024 on the IGCL investment, IGCL Letter of Offer (Mar-2025) and IDC fairness recommendation, and the NGL DLOF of 19-Jun-2023 (B08 read them only through web copies or summaries); (e) public shareholding sub-category detail (BSE).
   - Plausibly nonexistent: NGL concall transcripts and investor presentations (the company publishes neither; that is itself a data point on opacity for the kill decision); broker research (none found); prospectus (long-listed).
   - Empty folders, repeated per the /step1 autonomy contract (standing answer: continue with the gaps): concalls (declared, no-call company), presentation, prospectus (not expected), research.
   - Other corpus conditions (B00): Playwright collector failed; the corpus was repaired by direct download of public BSE and CARE filings. No screener Excel export; screener HTML tables held as text, rounded to whole ₹ Cr. IGCL peer screener table was repaired in commit 6a2339a8 (B06 ERRATA).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Nothing in this section is signed. Signing happens only in claude.ai after live-web stress tests.

### PART A: THE FROM STATE

**A1. ARCHETYPE.** Gelatine line: Commodity converter. DCP line: Commodity converter. B04 finds a price-taker on both products, with margin set by bone cost, coal and DCP realisation, and no filed evidence of build-to-spec (B04 FLAG-ARCHETYPE). The operator rules the sector row and the converter treatment at the /fttcp pillar gate (B00 sector_cap_row; B13 open item 11). One company, one plant, one reportable segment (AR MD&A PDF p.11; Note 45).

**A2. THE SIMPLE ANALOGY.** NGL is a flour mill that is paid for the flour and for the bran. The "grain" is crushed animal bone. The mill grinds it into gelatine, a clear protein that capsule makers use for pills. The bran is DCP, a mineral powder sold as animal feed. The mill does not set the rate for either product. It makes money on the gap between what bone costs and what gelatine and DCP fetch, and on how efficiently it runs its boilers. In FY26 that gap widened a lot (B03, B04). One plant near Jabalpur makes everything (B03 missing_risks).

### PART B: THE TRANSITION

**B1. FROM to TO.**
- Gelatine line: FROM R1 COMMODITY PRICE-TAKER, TO R2 COST-ADVANTAGED CONVERTER. B04 reads the line as R1 moving to R2. Margin comes from cost position, not from price. FY26 ROCE 27.9% against 4% to 12% in FY16 to FY22 (B03). The ladder places R2 at durable mid-teens ROCE; whether the FY26 level is durable is the open point.
- DCP line: stays R1. No transition is claimed. DCP ASP rose 17.17% in FY26 on a spot market and is the reversal risk (B03, B05).
- One rung only. No multi-rung leap is claimed.

**B2. THE ENGINE.** Two physical changes carry the margin, and a third is pending (B03, B04, B05):
1. Materials cost. Materials plus inventory change fell from 58.1% to 53.0% of revenue, 511 bp, in FY26 and reached 50.6% in Q1 FY27. Raw material consumed fell 147.29 lakh on 2,649.08 lakh more revenue (B02 rank 3). The notes do not separate price, yield and mix. The AR gives no quantified cause (B03).
2. Power and fuel. 10.8% of revenue against 13.0%, 217 bp, from a 2.15 MW solar plant (₹8.89 Cr), a UF plant that replaces an evaporator, and lower coal cost (AR Annexure III PDF p.19; B03). MD&A credits coal; the saving is credited once (B05, B07).
3. Capacity (pending, rater view): +600 MT gelatine from 2,400 MT and +1,500 MT DCP from 10,600 MT, ₹33.00 Cr, ₹25 Cr term loan, commercial production from Jan-2027 (CARE 06-Mar-2026 p.2; B05). It appears in no AR page and in no company statement (B03 FLAG-CAPEX-UNDISCLOSED; B12b noted the company filed CARE's text on BSE itself).
Net price effect was only about +84 lakh of the 1,540 lakh PBT rise (DCP +918, gelatine -834, computed from MD&A rates, B03). The reset is cost-led, not price-led.

**B3. THE PROOF GATE.** Metric and threshold from the committed blocks: standalone operating margin before other income at or above 18%, with materials plus inventory change at or below 52% of revenue, in the Sep-2026 quarter (filed 12-Nov-2026) and in the next quarter, while IGCL's materials ratio does not rebound (B03 monitorables; B04 must_track_metrics; B05 trigger 2; Q1 FY27: 20.79% and 50.6%). The two-quarter hold is a drafting choice for the operator to confirm or change. Until the gate fires, the transition is narrative and the name is research. FTTCP tests this gate.

**B4. THE RECOGNITION GAP (to be resolved at Stage 11).** Open question: does the TO state, R2 with a durable 18% to 20% margin, already show in how the market prices the stock today? This dossier does not answer it. Stage 11 confirms or denies it through the PE gap. If the TO state is already reflected, the re-rating engine is spent and only earnings growth remains. No number, no conclusion here.

**B5. THE UGLINESS TEST.** Classification (draft): ARTIFACT-OF-CLIMB for the visible ugly optic, which is the cash lag (CFO/PAT 86.4% against 99.0%) together with the margin sitting above NGL's own ten-year band.
- For: B13 and B02 read the cash lag as GROWTH-INDUCED plus a one-time supplier payables unwind (MSME payables 951.86 to 477.18 lakh, payable days 56.3 to 38.6, B02); receivables overdue share fell 23.1% to 13.4% (B02); three-year CFO/PAT 0.95 against twelve-year 0.78 (B01). CARE forecast the bone cost fall in Apr-2025 before it showed in the accounts (B12b).
- Against: CARE calls the operating cycle "elongated at 113 days in FY25" (CARE p.2); adjusted CFO is 79.7% of PAT (B03, B12a); inventory is 156 days of materials cost; Nitta's margin moved about 3 points in the same period, so part of the gain may be a cycle (B04 FLAG-CYCLE).
- Separate from this test: the IGCL stake and Pioneer Jellice flows are governance tripwires, not climb optics (B08). The operator declares the classification. No trade verdict here.

**B6. THE TRANSITION FALSIFIER.** The Sep-2026 quarter or the one after prints operating margin before other income below 16.4% (the Q1 FY26 level) or materials plus inventory change above 53% of revenue, with gelatine ASP flat and IGCL's ratio rising with NGL's (B13 falsification line; B05 trigger 2 kill signal; B06 cross-peer hypothesis kill). A second path: no Reg 30 commissioning notice by 2027-03-31, or cost above ₹33 Cr funded by debt taking gearing above 0.5x (B05 trigger 1; CARE negative trigger).

### PART C: WHAT THE MODEL WATCHES

**C1. DOMINANT VARIABLES.**
1. Materials plus inventory change as % of revenue. FY26 53.0%; Q1 FY27 50.6%; FY25 58.1%; healthy at 52% or lower, warning level above 56% (B03, B04). IGCL fell 727 bp in FY26 (B03).
2. Power and fuel as % of revenue. FY26 10.8%; Q4 FY26 8.9%; Q1 FY27 11.9%; Q1 FY26 12.7% (B03).
3. Capacity expansion delivery. CWIP 528.97 lakh, capital commitments 1,205.00 lakh, term loan 728.65 lakh with an implied FY26 draw of about 125.57 lakh; Q1 FY27 filing has no balance sheet (B03, B05).
4. Cash conversion. CFO/PAT 86.4% (FY25 99.0%); inventory 155.9 days on materials cost; receivables over six months 28.63 lakh against 2.03 (B02).
These are the Role 5.5 tracker signals. The IGCL stake (4,115.31 lakh, 29.1% of equity) and Pioneer Jellice flows (1,517.52 lakh, 7.04% of revenue) stay as named tripwires, not transition variables (B02, B08).

**C2. WHAT THE MODEL REJECTS.**
- Market size as the binding constraint. The market has room (B09 runway class GOOD, about 7% of the serviceable market), but the binding constraint is plant capacity of 2,400 MT and execution: three-year obtainable revenue of ₹339 Cr exceeds the ₹263 Cr the expanded plant makes at flat realisation (B09).
- Management's global gelatine market claim (USD 3.60 bn), which is a scope mismatch against an India figure (B09 mgmt_claim_read).
- Spot-year ROCE, consolidated PAT and EPS (they include non-cash IGCL profit), the current ratio, Note 48 ratios, R&D intensity of 0.07%, and dividend payout percentage (FY23 payout 396% under the prior owner) (B04 irrelevant_ratios).

**C3. THE BUSINESS FALSIFIER.** Evidence that would force a re-declaration of the FROM business, distinct from B6: (a) a filed contract term, qualification period or sole-source clause showing the gelatine line is spec-in rather than a price-taker, which moves the archetype to build-to-spec (B04 FLAG-ARCHETYPE; B07 optionality row on customer lock-in); (b) a scheme or transaction that combines NGL operations with IGCL, which B08 reading A allows, and which would change the starting business. B6 kills the arrow. This one changes the thing the arrow starts from.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE (draft; stage 13 holds the final)

Narmada Gelatines crushes animal bone at one plant near Jabalpur and makes two products from it (B03, B04). Gelatine is 70.62% of FY26 revenue and is the protein capsule makers use to form gelatine capsules, in pharma and edible grades (B04). DCP, di-calcium phosphate, is 29.08% of revenue; it is a mineral by-product of the same bone, sold as an animal feed ingredient at spot rates to local customers (B04, CARE p.2). Gelatine customers are capsule makers such as Geltec, ACG Associated Capsules and Fortcaps, who give repeat orders; the top ten customers took about 42% of FY25 sales, up from 39% (B03, B07). The run did not establish any contract term, qualification period or sole-source position, so switching cost is unproven (B04, B07). One capsule maker imports 18% to 20% of its gelatine duty free and uses that access as a check on local prices (B06). Present demand comes from capsule volumes, which a listed capsule maker puts at about 6% a year in India and 4% abroad, so hard-capsule maker volumes and gelatine purchasing is the first signal to track (B06, B09). DCP demand follows poultry and animal feed production, which is the poultry and animal feed production volumes signal (B09). Forward growth rests on three drivers. First, a ₹33 Cr expansion adds 600 MT to 2,400 MT of gelatine and 1,500 MT to 10,600 MT of DCP from January 2027; only the rating agency describes it, and a Reg 30 commissioning notice would confirm it (B05). Second, a BIS IS 5470 mandatory standard for feed-grade DCP, dated 1-Apr-2027 by a secondary source, could move DCP volume toward compliant producers (B09). Third, gelatine volume rose 16.17% in FY26 against a market near 6%, and India HS 3503 gelatine imports and peer capacity commissioning at IGCL and Nitta will show whether the share gain holds (B03, B06, B09). DCP has no moat: it is a spot commodity and NGL takes the market rate (B04). In gelatine, the one evidenced edge is cost, where the solar plant, the UF plant and lower coal cut power and fuel from 13.0% to 10.8% of revenue (B03, B07). The Emerging Moat scan scored 11.7, 0.3 under the 12 line, with no category rated Strong or Moderate and zero on talent asymmetry and the cannibalisation barrier (B07). EDQM, Kosher and Halal certifications are table stakes (B07). The group know-how that CARE credits runs through a related party whose pricing is undisclosed (B07 FLAG-RELATED-PARTY-CARRIES-THE-MOAT-CLAIM). Bone supply cost sets cost for both lines and sits outside the company's control, and the run holds no bone cost series (B03, B06).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. VERTICALS FRAMED

**Vertical 1: Materials plus inventory change ratio (bone and gelatine spread).**
- Corpus establishes: ratio 58.1% to 53.0% (-511 bp) in FY26, 50.6% in Q1 FY27 (B03); IGCL's ratio fell 727 bp, 47.07% to 39.80% (B03); gelatine ASP -5.20% (B03); the customer-side peer says gelatine prices fell about 4% in FY25 and 4% to 5% in H1 FY26 and had been soft for six quarters (B06, B12d); Nitta's quarterly OPM 18% (Mar-25) to 28% (Sep-26), screening data (B06); CARE forecast the bone cost fall in Apr-2025 (B12b).
- Cannot establish: any bone or crushed-bone cost series, yield %, tonnage, whether FY26 imports occurred (AR Note 43 p.77 says raw material is domestic with no foreign currency exposure; FX outgo has no raw material line; CARE says imports started) (B03, B12b).
- Questions that decide it: (1) Do NGL's and IGCL's materials ratios rise together in Q2 and Q3 FY27? (2) Is there a raw-material import line in the FY27 AR or a rise in Pioneer Jellice purchases? (3) Does NGL's gelatine ASP hold while the ratio holds?

**Vertical 2: Power and fuel ratio.**
- Corpus establishes: 13.00% to 10.83%; power and fuel -4.98% (2,333.26 vs 2,455.65 lakh) on revenue +14.02%; depreciation +29%; IGCL's ratio rose 87 bp, so the lever is company-specific (B03, B05). Quarterly: Q1 FY26 12.7%, Q3 FY26 10.1%, Q4 FY26 8.9%, Q1 FY27 11.9% (B03).
- Cannot establish: how much of the saving is solar against coal price; MD&A credits coal, Annexure III credits solar (B03, B05); solar output data.
- Questions that decide it: (1) Does the ratio stay at or below 11% with coal flat? (2) Why did Q4 FY26 reach 8.9% and not repeat? (3) Is the UF plant saving visible in steam and electricity use?

**Vertical 3: Capacity expansion delivery.**
- Corpus establishes: CWIP 528.97 lakh (all under one year; Note 4 says no cost overrun or time delay), commitments 1,205.00 gross, term loan 728.65 at 7.95% to 8.20%, 320.56 due in a year (B02, B03 ERRATA: 44%); gearing 0.03 (B02); the plan moved between CARE releases: Apr-2025 ₹33.30 Cr over FY25 and FY26 including solar with an ₹18 Cr loan, Mar-2026 ₹33.00 Cr excluding solar, ₹25 Cr loan, production from Jan-2027 (B12b); CWIP plus commitments was 1,933.03 lakh at Mar-2025 and 1,723.03 at Mar-2026, so the sum is not progress evidence (B12b).
- Cannot establish: project name, sanction terms, covenants, progress after 31-Mar-2026, utilisation of the existing 2,400 MT, whether the extra tonnes are pre-sold (B03, B04).
- Questions that decide it: (1) Does the H1 FY27 balance sheet show CWIP and a new term-loan draw rising? (2) Does a Reg 30 notice arrive by Jan-2027? (3) What did the MD and CFO say at the AGM on capex (webcast, B12b)?

**Vertical 4: Cash conversion.**
- Corpus establishes: CFO 2,455.67 vs PAT 2,843.82 lakh (86.4%); working-capital outflow 846.85 vs 126.62; payables unwind 483.31; adjusted CFO about 2,267.42 lakh (79.7% of PAT), adjusted FCF 1,295.71 (B12a corrected) (B02, B03); inventory 4,879.49 lakh (+4.8%), 155.9 days on materials cost, 82.7 days on sales (B03); CARE: fund-based limits of ₹20 Cr used about 14% on average (CARE p.2); FY23 payout 396% before the 2023 sale (B01, B03).
- Cannot establish: inventory in tonnes, write-down or NRV amounts, ECL matrix (token 2.81 lakh), nature of 46.44 lakh sundry write-offs (B02).
- Questions that decide it: (1) H1 FY27 CFO/PAT at or above 90% or below 80%? (2) Do receivables over six months stay below 30 lakh? (3) Does inventory stay near 156 days as volume grows?

### 4b. CANDIDATE SIGNAL TABLE (UNVERIFIED; verification and tracker writes at Role 5.5 in claude.ai)

Likely sources come from B09 downstream_candidates; the match to Downstream_Source_Discovery_Protocol_v1_0 registry entries is for Role 5.5 to confirm.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Hard-capsule maker volumes and gelatine purchasing (ACG, Geltec, Fortcaps, Natural Capsules) | Capsule maker volume growth falls below 4% a year, or a named customer cuts gelatine procurement, while NGL volume growth stays above 10% | Quarterly | Listed capsule makers' exchange filings and concall transcripts (B09) |
| India HS 3503 gelatine import value and volume | Import volume or value rises while NGL gelatine ASP is flat or down, showing import competition capping the rate | Monthly | Commerce ministry trade statistics (DGCI&S) by HS code (B09) |
| Peer capacity commissioning (IGCL 2,000 to 2,700 MT, Nitta expansion) | IGCL or Nitta commissions capacity before NGL's Jan-2027 date into the same capsule-maker base | Event-Driven | BSE/NSE announcements and annual reports of IGCL and Nitta (B09) |
| Poultry and animal feed production volumes | Feed output growth turns negative while DCP revenue share holds near 29% only through a higher DCP rate | Quarterly | Feed industry association data and poultry trade press (B09) |
| BIS IS 5470 mandatory standard for feed-grade DCP (enforcement date 1-Apr-2027 per a secondary source) | Notification delayed, diluted, or NGL DCP not shown compliant | Event-Driven | BIS notifications and DGFT/ministry orders (B09) |
| Bone and crushed-bone supply cost (domestic and imported); serves both lines | NGL materials ratio above 53% with IGCL's ratio rising, or a bone cost series turning up | Quarterly | Trade data on raw-bone imports and peer annual reports (B09) |

### 4c. FRAGILITY READ

- variable_count: 8. The eight: (1) gelatine output rate against bone cost spread; (2) DCP rate and volume; (3) capsule-maker demand; (4) peer capacity additions; (5) power and fuel saving durability; (6) capex delivery on time and cost; (7) cash conversion; (8) related-party and IGCL capital allocation.
- verifiability_ratio: 4 of 8 externally observable: variables 1 to 4 can be read from peer filings, government trade data or capsule-maker filings (variable 1 through peer proxy only, since no bone series exists, B06, B09). Variables 5 to 8 rest on NGL's own filings, which carry no yield, utilisation, tonnage or pricing basis and where the AR contradicts its own notes in several places (B02, B03, B12b).
- single_point_failure: the materials plus inventory change ratio reversing. 511 bp of the 6.2 point margin move sits here and IGCL moved the same way (B03, B04). Reversal on this one line breaks the reset thesis alone.
- fragility_verdict: **FRAGILE**. One kill-switch exists, and half the variables are company-narrated.

### 4d. RESEARCH BRIEF (live-web work for claude.ai)

Items 1 to 6 are the PENDING LIVE VERIFICATION links raised by the 4e chains.
1. PENDING (Chain 1, link 1). Pioneer Jellice India Private Limited: latest filed financial statements and any filing that says what raw material it supplies to NGL (₹1,481.92 lakh in FY26; product NOT FOUND, B08). Open the company's MCA21 filing set or the web equivalent.
2. PENDING (Chain 1, link 1). Nitta Gelatin India Ltd (BSE 506532) Q2 FY27 results: quarterly materials or gross margin and OPM against the 28% Sep-26 figure on screener (B06).
3. PENDING (Chain 1 and 2). India Gelatine and Chemicals Ltd (BSE 531253) Q2 FY27 results: materials ratio against 39.80% in FY26; plus its capacity commissioning notices (2,000 to 2,700 MT, B09).
4. PENDING (Chain 1). Indian customs or trade records for crushed-bone and ossein imports: volume and unit value since Oct-2025.
5. PENDING (Chain 2, link 1). Latest filed financial statements and any rating rationale for Geltec Private Limited, ACG Associated Capsules Pvt Ltd and Fortcaps Healthcare Limited, the customers named in CARE p.2: capsule volume growth, gelatine sourcing, payment health.
6. PENDING (Chain 2). Natural Capsules (BSE 524654) Q2 FY27 earnings call transcript: gelatine price direction after Nov-2025 (B06 notes no statement after Jun-2026).
7. Build Chain 3 (Rule F floor): IGCL associate. Trigger: ₹41.15 Cr placed in IGCL on 5-Dec-2024, the day the promoter bodies signed for control (B08). Needs the IGCL post-offer position and H1 FY27 Reg 23 filings.
8. Build Chain 4: DCP rate, feed demand and the BIS IS 5470 standard. Needs primary BIS notification and feed output data.
9. Build Chain 5: working capital, supplier stretch and customer payment health (Natural Capsules shows consolidated loss and thin liquidity, B06).
10. Pull Q2 FY27 results with the H1 balance sheet and cash flow from BSE 526739 and test the four dominant variables (B13 monitorables 1 to 5).
11. Request the AGM 19-Aug-2026 CDSL webcast and note the members' questions and the MD and CFO answers on capex (B12b).
12. Verify the BIS IS 5470 enforcement date of 1-Apr-2027 from the primary notification; B09 has a secondary source only.
13. Refresh the India HS 3503 import series; B09's figures are dated 2015 and 2023.
14. Verify source URLs and dates of the B09 market sizing inputs (Mordor, MRF, MnM, RBI rate 95.2492 on 06-Nov-2026); Verifier A could not check them (B12a).
15. Run the searches B08 could not reach: MCA21 and RoC charge registers for Pioneer Jellice, Ashok Matches and Asia Match Co; eCourts, NCLT, SFIO; SEBI SCORES.
16. Read at source the IGCL Letter of Offer and IDC fairness recommendation, the NGL Reg 30 filings of 4-Dec-2024 and of the KMP exits (28-Jun-2024, 7-Jan-2025), and the NGL DLOF of 19-Jun-2023. Verifier A could not check the SEBI-document figures (SPA rate ₹408.90, 39.42%, 46.98%, 61.12%) (B12a).
17. Settle the MD's age at source: 78 per the AGM notice PDF p.128, 79 per the Q4 FY26 results filing PDF p.17 (B13 open item 13).
18. Check the audit chair's link to Asia Match Co Pvt Ltd, marked UNVERIFIED by B08.

### 4e. SECOND-ORDER STUB (Master Prompt v3.7, Rule F)

```
CHAIN 1: NGL's materials plus inventory change fell from 58.1% to 53.0% of revenue (-511 bp) in FY26 (B02 rank 3) while gelatine ASP fell 5.20% (B03 MD&A) and IGCL's ratio fell 727 bp (B03).
Link 1 [PENDING LIVE VERIFICATION]: Who supplies the bone, and who bears the cost change, and why now. Counterparty evidence is out of reach here. Claude web opens: Pioneer Jellice India Private Limited's latest filed financial statements and any supply disclosure (the company that sold NGL ₹1,481.92 lakh of raw material, product undisclosed, B02 rank 2, B08); Nitta Gelatin Q2 FY27 results; IGCL Q2 FY27 results; India crushed-bone import records.
Link 2 [FILED, B12b, B03]: AR Note 43 p.77 says major raw material is sourced from domestic suppliers and there is no foreign currency exposure at the reporting dates. AR Annexure III p.19 shows foreign exchange outgo of spare parts 31.88, travel 3.34 and subscriptions 7.87 lakh and no raw material line. CARE 06-Mar-2026 p.2 says NGL "has started importing some part of its raw material requirement". The FY26 cost relief therefore cannot rest on imported bone.
Link 3 [INFERENCE]: The cost relief came from domestic bone cost falling, a move IGCL shared and exceeded, so the main margin line follows an industry bone cycle that NGL does not set. If any imports run through Pioneer Jellice, that channel's pricing sets how the gain divides between NGL's minority holders and the promoter group. Either way, the ratio can reverse without any change inside NGL.
Binding constraint: Raw material is 53.0% of revenue (B02); NGL is a price-taker with a single plant (B03, B04); no bone cost series exists in the corpus (B06).
Unsaid: The MD&A says material consumed "increased by 1.29%" while Note 28 shows a 1.29% fall (B03). The AR does not say what Pioneer Jellice supplies (B08). No yield % and no tonnage are printed (B03). Nitta's margin also rose, which the company does not mention (B06).
Observation that confirms or breaks this chain, and confirm-by date: Confirms if Q2 FY27 materials plus inventory change is at or below 52% of revenue (Q1 FY27 50.6%) while IGCL's ratio does not rebound; breaks if above 53% with gelatine ASP flat. Read at the Q2 FY27 filing, 2026-11-12, and at the Q3 FY27 filing (Q3 FY26 was filed 2026-02-12, B00-intake), expected about mid-Feb-2027.
```

```
CHAIN 2: CARE 06-Mar-2026 p.2 sets out a ₹33.00 Cr plan to add 600 MT of gelatine and 1,500 MT of DCP from Jan-2027 (B05 trigger 1); AR notes show CWIP 528.97 lakh and capital commitments 1,205.00 lakh at 31-Mar-2026 (B03).
Link 1 [PENDING LIVE VERIFICATION]: Who takes the extra tonnes, and why now. Claude web opens: latest filed financial statements and any rating rationale for Geltec Private Limited, ACG Associated Capsules Pvt Ltd and Fortcaps Healthcare Limited (customers named by CARE p.2), and the Natural Capsules Q2 FY27 transcript, to see whether capsule makers plan to raise gelatine intake or to lean on duty-free imports.
Link 2 [FILED, B12b, B05]: The plan moved between CARE releases. Apr-2025: ₹33.30 Cr over FY25 and FY26 including solar, term loan ₹18 Cr. Mar-2026: ₹33.00 Cr excluding the ₹8.89 Cr solar plant, term loan ₹25 Cr, production from Jan-2027. AR Note 4 p.61 says no cost overrun or time delay. Term loan fell 798.08 to 728.65 lakh, implied FY26 draw about 125.57 lakh against ₹25 Cr planned (B03). CWIP plus commitments was 1,933.03 lakh at Mar-2025 and 1,723.03 at Mar-2026 (B12b), so the sum does not show progress.
Link 3 [INFERENCE]: The extra tonnes land in a customer base where the top ten take about 42% of sales, up from 39%, one customer imports 18% to 20% of its gelatine duty free, and IGCL plans its own capacity increase (B06, B07, B09). FY26 volume growth of 16.17% was part-funded by running finished goods down by 276 lakh (B04), and three-year obtainable revenue of ₹339 Cr is above the ₹263 Cr the expanded plant can make at flat realisation (B09). So volume growth above the 2,400 MT base before Jan-2027 is stock-sourced or capped, and the new tonnes compete on the cost spread, not on a lock-in.
Binding constraint: Plant capacity of 2,400 MT gelatine and 10,600 MT DCP (CARE p.3); the term loan draw and the commissioning date; inventory already at 155.9 days on materials cost (B03). Gearing is 0.03 against CARE's 0.5x negative trigger (B02, CARE p.1).
Unsaid: The AR carries no capex plan, size, funding or date, and the Outlook section gives no number (B05). The company never acknowledged the CARE restatement (B12b). Utilisation is not printed (B09). The AGM question content is not recorded (B12b).
Observation that confirms or breaks this chain, and confirm-by date: Confirms if the H1 FY27 balance sheet (filed with Q2 FY27 results, 2026-11-12) shows CWIP above 528.97 lakh with a new term loan draw, and a Reg 30 commissioning notice reaches BSE by 2027-01-31. Breaks if no notice by 2027-03-31, or if cost passes ₹33 Cr and gearing passes 0.5x (B05 trigger 1 kill signal).
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Narmada Gelatines crushes animal bone at one plant near Jabalpur and makes gelatine and DCP from it (B03, B04).
2. Gelatine is 70.62% of FY26 revenue. DCP, a mineral feed ingredient from the same bone, is 29.08% (B04).
3. The company is old. It dates from 1961 and has held no earnings calls and issued no investor presentations (B00, CARE p.3).
4. Capsule makers such as Geltec, ACG and Fortcaps purchase the gelatine. DCP goes to local feed customers (CARE p.2).
5. The top ten customers took about 42% of FY25 sales, up from 39% (B03). The run found no contract term or lock-in (B07).
6. Capsule demand grows about 6% a year in India (B06). NGL's gelatine volume rose 16.17% in FY26, so it took share or built stock (B03, B04, B09).
7. Growth could come from a ₹33 Cr expansion from January 2027, a feed standard for DCP, and more share. Only the rating agency describes the expansion (B05, B09).
8. Operating margin went from 13.0% to 19.2% in FY26 and was 20.8% in Q1 FY27. Cost explains it. Net price effect was only about ₹84 lakh of a ₹1,540 lakh profit rise (B03, B05).
9. The moat sits in cost, partly. Power and fuel fell from 13.0% to 10.8% of revenue. DCP has no moat, and the Emerging Moat score is 11.7, just under the line for a modest moat (B03, B07).
10. The mental model, in draft: a commodity converter claims a climb from price-taker to cost-advantaged converter, one rung. Two proof checks: margin at 18% or more and materials at 52% or less of revenue, held for two quarters (B03, B04).
11. The fragility verdict is FRAGILE. Eight outside variables must go right, only four can be seen from outside, and a reversal in the bone-to-gelatine spread alone breaks the thesis (B03, B04, B09).
12. The corpus could not establish the cause of the margin move, tonnage, yield, utilisation, bone cost, customer shares, or the terms of the Pioneer Jellice purchases (₹1,481.92 lakh). The IGCL stake sits at ₹41.15 Cr with no test (B02, B03, B08).
13. The corpus lacks the Sep-2026 quarter results, due on the run date, the AGM recording and the FY2023-24 annual report (B00, B12b).
14. The biggest open question is whether the fall in bone cost lasts. IGCL's materials ratio fell even more, which points to an industry cycle (B03). The Sep-2026 quarter is the first test.
15. The second open question is delivery. The company's own report says nothing about the expansion, and the plan changed between two rating releases without comment (B05, B12b).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Filename and page anchor on every number. NOT DISCLOSED with a reason where the corpus lacks the item. Standing ERRATA in the header apply. File short names: AR = inputs/annual-report/NGL-Annual-Report-FY2025-26.pdf; CARE = inputs/rating/CARE-Narmada-Gelatines-2026-03-13.pdf; Q1 = inputs/results/20260812-Q1FY27-results.pdf; SH = inputs/shareholding/.

### 1. UNITS

No per-unit figure (realisation per tonne) is printed anywhere in the corpus.
- Quote (AR PDF p.12, printed 9, MD&A): "Sales volume of gelatine and DCP increased by 16.17% and 11,35 % respectively. ... price of gelatine decreased by 5.20% but DCP increased by 17.17% as compared to last year," (two words, "Average selling", omitted before "price"). Comment: percentage changes only; no tonnes and no rupees per tonne. OCR "11,35" is 11.35 (B03, checked on the page image). Gelatine is a basket of pharma and edible grades; DCP is one animal-feed grade product (B04).
- Quote (AR PDF p.68, printed 65, Note 26): "Gelatine 15,212.47 14,027.83", "DCP - animal feed grade 6,264.24 4,809.26", "Bone meal products 21.16 24.94", "NET SALES 21,541.15 18,892.07" (₹ lakh, FY26 then FY25). Comment: these are the revenue lines. The MD&A prints the share as 70.77% and 29.15% (AR PDF p.12); Note 26 gives 70.62% and 29.08% (B04). The two differ by about 0.15 points.
- Quote (CARE PDF p.3): "NGL has a manufacturing capacity of 2400 MT per annum for Gelatine and 10,600 MT per annum of DCP." Comment: capacity, not sales volume. Derivation available: B04 divides Note 26 revenue by this capacity to get a floor of ₹6.34 lakh a tonne for gelatine and ₹0.59 lakh a tonne for DCP; this is an arithmetic floor at stated capacity, not a printed realisation (B04). Tonnes sold are NOT DISCLOSED in the AR (B03).

### 2. SEGMENT CAPITAL AND DEBT

Segment assets, segment liabilities and capital employed by segment are NOT DISCLOSED: the company reports one segment.
- Quote (AR PDF p.78, printed 75, Note 45): "Since all these segments meet the aggregation criteria as per the requirements of Ind AS 108 on 'Operating segments', the management considers these as a single reportable segment, Accordingly, no further disclosure is required to be furnished." Same text in Q1 PDF p.2, note 3: "the management considers these as a single reportable segment."
- Quote (AR PDF p.11, printed 8, MD&A): "The Company is engaged in only one segment, namely, manufacture and sale of gelatine and related products like ossein and di-calcium phosphate (DCP)".
- Entity totals as printed (AR PDF p.49, printed 46, balance sheet, ₹ lakh, 31-Mar-2026 then 31-Mar-2025): "TOTAL ASSETS 17,497.05 15,933.68"; "Total Equity 14,130.66 11,944.26"; "Borrowings 18 408.09 603,08" (non-current); "Borrowings 21 380,99 669.12" (current). Quote (AR PDF p.65, printed 62, Note 18): "Term Loan* 728,65 798,08" and "Less: Current Maturities of Long term borrowings (320.56) (195,00)". Comment: borrowings are unallocated, held at entity level; total 789.08 (FY25 1,272.20) is the sum of the two lines (B02). Capital employed as equity plus borrowings is a derivation, not a printed figure: 14,919.74 (FY25 13,216.46) [COMPUTED].

### 3. GUIDANCE VERSUS ASPIRATION

Company numeric guidance: NOT DISCLOSED; the AR Outlook gives no company number (B05; AR PDF p.11).

| Item | Class | Quote and anchor |
|---|---|---|
| Indian gelatine market growth | (b) aspiration without a period, industry claim | "The Indian gelatine market is expected to register a CARG of around 7.5% over the next few years" (AR PDF p.11) |
| Global gelatine market | Industry projection with a period (2034), not management guidance | "projected to grow from USD 3.60 billion in 2026 to USD 6.58 billion by 2034, registering a CARG of 7.83%" (AR PDF p.11) |
| Raw material import | (c) capability, no number | "This opportunity is being utilized to import/purchase raw material, which will help import raw material at Competitive price" (AR PDF p.11) |
| SAP implementation | (c) capability, no date | "Implementation of SAP is currently underway and progressing as planned" (AR PDF p.19, Annexure III) |
| Better yield and utilisation | (c) capability claim, no metric | "Growth led by better yield and lower consumption of power and fuel" (AR PDF p.12) |
| Capacity and capex (attributed by the rater, not stated by the company in the AR) | (c) capacity, with a dated start | "estimated cost of ₹33. 00 crore over two year ... term loan of ₹25 crore ... Gelatine by 600MT and DCP by 1,500MT ... commercial production is envisaged from Jan 2027" (CARE PDF p.2) |
| Margin (rater view) | (b) no firm period, rater not management | "CareEdge Ratings believes NGL to sustains PBILDT margin 18-20% in near term" (CARE PDF p.1) |
| FY26 sales growth (rater view) | (a) with a period, rater not management | "For FY26, TOI is envisaged to grow by over 15% over FY25." (CARE PDF p.2) |
| FY26 cash accruals (rater view) | (a) with a period, rater not management | "envisaged GCA of ₹29-30 crore" (CARE PDF p.2) |

Comment: no filed management statement fits class (a). The rater items carry periods but the company did not adopt them in a filing (B05).

### 4. CONCENTRATION

- Product. Quote (AR PDF p.68, Note 26): "Gelatine 15,212.47", "DCP - animal feed grade 6,264.24" of "NET SALES 21,541.15" (₹ lakh). Top product share: gelatine 70.62% (B04); MD&A prints 70.77%. Comment: two products, one plant.
- Customer. Top single-customer share: NOT DISCLOSED; no customer above 10% of revenue is disclosed anywhere in the AR (B03). Quote (CARE PDF p.2): "top 10 customers have contributed ~42% of total sales for FY25. (39% for FY24)." Quote (AR PDF p.76, printed 73, Note 43): "The Company's concentration of risk with respect to trade receivables is low, as its customer's base is widely spread across the length and breadth of the country". Comment: the two statements are not reconciled in the corpus (B03).
- Geography. Quote (AR PDF p.19, Annexure III): "FOB value to exports: 214,93 lakhs 47.99 lakhs". Comment: OCR comma reads 214.93 lakh (B03); about 1.0% of FY26 revenue (B04). Domestic split by region NOT DISCLOSED. CARE p.2: "DCP is sold to local customers."

### 5. PROMISE LEDGER

| # | Promise | Date made | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | Solar plant commissioned (₹8.89 Cr) and UF plant installed to cut power and fuel | AR dated 25-May-2026 (Annexure III) | Delivered | Power and fuel 2,333.26 vs 2,455.65 lakh; ratio 10.83% vs 13.00% (AR PDF p.12, p.19, p.50; B05) |
| 2 | Growth from better yield and optimum capacity utilisation | AR dated 25-May-2026 (MD&A) | Partial | Volume +16.17% and +11.35% shown; yield % and utilisation % NOT DISCLOSED (AR PDF p.12; B05) |
| 3 | Raw material imported at competitive cost | AR dated 25-May-2026 (MD&A p.11); CARE 06-Mar-2026 | Partial, unverified | FX outgo has no raw material line; Note 43 p.77 says domestic (AR PDF p.19, p.77; B12b) |
| 4 | Capacity +600 MT gelatine, +1,500 MT DCP, ₹33 Cr, from Jan-2027 | CARE 06-Mar-2026 (earlier plan CARE 08-Apr-2025: ₹33.30 Cr, FY25 to FY26, incl. solar) | Pending; scope and date changed between releases | CWIP 528.97 lakh; commitments 1,205.00 (AR PDF p.61, p.72; CARE PDF p.2; B12b) |
| 5 | Margin 18% to 20% near term (rater) | CARE 06-Mar-2026 | Met by filings, rater not management | FY26 19.18%; Q1 FY27 20.79% (AR PDF p.50; Q1 PDF p.2; B03) |
| 6 | FY26 sales growth over 15% (rater) | CARE 06-Mar-2026 | Near miss, rater not management | Revenue +14.02% (AR PDF p.12) |
| 7 | SAP implementation on plan | AR dated 25-May-2026 | Untestable, no date | AR PDF p.19 |

Comment: B05 grade is C by default in no-concall mode; B12b concurs (B05, B12b).

### 6. RESTATED BASES

No restatement for a reorganisation or transfer. A general regrouping note exists with no amounts.
- Quote (AR PDF p.80, printed 77, Note 50): "Previous year's figures have been re-grouped / re-classified wherever required to conform to current years' classification." Comment: no amounts and no line named; B02 notes staff welfare and salaries sub-heads swing inside Note 30 (715.25 vs 53.43; salaries 1,360.72 to 1,147.35) and consolidated FY25 CSR differs from standalone (B02 restatements_found).
- Quote (Q1 PDF p.2, note 4): "The Consolidated results include proportionate share of profit of India Gelatine and Chemicals Limited (IGCL), an associate of the Company." Comment: consolidation began with the IGCL associate on 05-12-2024; consolidated history is FY25 and FY26 only (B00).
- Comparatives as printed in the latest filing (Q1 PDF p.2, standalone, ₹ lakh): Q1 FY27 revenue "5,637"; Q1 FY26 revenue "4,577"; year ended 31-Mar-2026 "21,541"; Q1 FY26 profit before tax "667"; Q1 FY27 "1,095". Comment: comparatives tie to the FY26 AR (revenue 21,541.15, AR PDF p.68).

### 7. CORPORATE-ACTION CLAUSES

No scheme, demerger, merger, preferential issue or share repurchase by NGL is in the corpus.
- Quote (AR PDF p.47, printed 44, CARO clause 3(x)(b)): "The Company has not made any preferential allotment or private placement of shares or fully or partly convertible debentures during the year or in the recent past". The secretarial audit (AR PDF p.17) lists the SEBI share repurchase regulations as not applicable for the period.
- Corporate transactions that exist: (a) the 2023 change of control, 75% of NGL bought by Pioneer Jellice and Ashok Matches from Alfamont (Mauritius) under an SPA of 9-Jun-2023 at ₹229 a share, with an open offer at ₹303, a promoter-level event read from SEBI web copies (B08); (b) NGL's purchase of 14.14% of IGCL. Quote (AR PDF p.6, Board's Report): "During the Previous Financial year 2024-25, Narmada Gelatines Limited acquired a 14.14% equity stake in India Gelatine and Chemicals Limited (IGCL)". Quote (AR consolidated Note 1, PDF p.89): "India Gelatine and 14.14% Manufacture and sale of 05-12-2024" with "Ossein and Gelatine" on the next line. Cost 4,115.31 lakh for 10,03,000 shares (B03).
- Ratios, definitions of undertaking, liability allocation and appointed dates: NOT DISCLOSED in the corpus because no scheme exists. Filings to fetch: NGL DLOF 19-Jun-2023 and IGCL DPS 12-Dec-2024 and post-offer advertisement 17-Apr-2025 (SEBI, read by B08 from web copies, outside the corpus); NGL Reg 30 of 4-Dec-2024 and IGCL Letter of Offer Mar-2025 (BSE).

### 8. RELATED-PARTY PERIMETER

- Quote (AR PDF p.72, printed 69, Note 37): "Pioneer Jellice India Private Limited Associate Co," and "Ashok Matches and Timber Industries Private Limited Associate Co,". Holdings (AR PDF p.64, Note 17a): Pioneer Jellice 2,423,321 shares 40.06%; Ashok Matches 2,113,870 shares 34.94%. Comment: together 4,537,191 shares, matching the BSE promoter row.
- Quote (AR PDF p.73, printed 70, Note 37, FY26 then FY25, ₹ lakh): "Pioneer Jellice India Private Limited: Purchase of raw material 1,481.92 1,524.64 (Including GST)"; "Technical Consultancy Service 24.00"; "Lease Rent 11,60" (OCR comma, 11.60); "Sales Commission - 6.72"; outstanding "Trade Payables 83.53 99.21". Comment: 1,517.52 lakh in FY26 is 7.04% of revenue (B02). Ashok Matches: no transaction listed. The note says "All related party transactions entered during the year were in ordinary course of the business and are on arm's length basis" and gives no benchmark (B02, B08).
- KMP remuneration, same note: Mr. Ashok K Kapur 99.16 (FY25 66.26); Mr. Arun Jaiswal 20.45; Ms. Mahima Patkar 5.74; payables 26.00, 0.45, 0.45. Sitting fees: Annamalai 1.55, Maheswaran 1.10, Vijayadurai 2.45, Thangamani 2.15, Krishnamoorthy 2.45 (FY26); FY25 sums to 8.40 (B12a). Comment: Annexure IV prints MD pay +10.41% against +49.7% in this note (B03).
- Outside the table: IGCL, the 14.14% associate, is not in the RPT table. Quote (AR PDF p.68, Note 27): "Dividend Income from an associate 50.15". Carrying 4,115.31 lakh against share of IGCL net worth 2,737.02 (B02; AOC-1 PDF p.21).

### 9. PLEDGE AND SHAREHOLDING

Promoter pledge, as filed: Sep-2026 only is in the corpus.
- Quote (SH/BSE-shareholding-summary-Sep2026.html): "Whether any shares held by promoters are encumbered under Non - Disposal Undertaking ?" "No"; the pledge and other-encumbrance questions on the same statement carry "No". Promoter row: "(A) Promoter & Promoter Group", 2 holders, "45,37,191", "75.00". Grand Total "7,718" holders, "60,49,587" shares. Comment: pledge for the eleven earlier quarters is NOT DISCLOSED in the corpus (B08 "earlier quarters not read at source"); the screener file carries no pledge row.
- Holding as filed, screener trend (SH/screener-shareholding-trend-to-Sep2026.txt), promoters %: Dec-2023 77.65; Mar-2024 77.65; Jun-2024 77.65; Sep-2024 75.00; Dec-2024 75.00; Mar-2025 75.00; Jun-2025 75.00; Sep-2025 75.00; Dec-2025 75.00; Mar-2026 75.00; Jun-2026 75.00; Sep-2026 75.00. Public %: 22.34, 22.34, 22.34, 24.99, 24.99, 25.00, 25.00, 24.99, 24.99, 25.00, 24.99, 25.01. Holders: 7,569; 7,515; 7,378; 7,864; 7,547; 7,560; 7,615; 7,809; 7,559; 7,312; 7,723; 7,718.
- Institutional, latest (Sep-2026): "DIIs ... 0.01%"; FII nil (B00). Comment: public sub-category names NOT DISCLOSED in the held files.

### 10. VERIFICATION

Documents quoted, with dates:
- inputs/annual-report/NGL-Annual-Report-FY2025-26.pdf (BSE cover 21-Jul-2026; Board's Report 25-May-2026; OCR text inputs/annual-report/NGL-Annual-Report-FY2025-26.txt)
- inputs/rating/CARE-Narmada-Gelatines-2026-03-13.pdf (press release dated 06-Mar-2026; filename date not used)
- inputs/results/20260812-Q1FY27-results.pdf (dated 12-Aug-2026; page 2 read on the page image)
- inputs/shareholding/BSE-shareholding-summary-Sep2026.html (quarter ended Sep-2026; fetched 2026-11-12)
- inputs/shareholding/screener-shareholding-trend-to-Sep2026.txt (Dec-2023 to Sep-2026; fetched 2026-11-12)
- Facts relied on from stage blocks and reports and not re-read here: B00 to B09, B12a to B12d, B13, and CARE 08-Apr-2025 (inputs/other/CARE-Narmada-Gelatines-2025-04-14.pdf) through B12b.

CORPUS COMMIT HASH: b091934be3b5088c72d5b942924050279a2e8c55
