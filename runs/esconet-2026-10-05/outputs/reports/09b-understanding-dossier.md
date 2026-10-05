# ESCONET (Esconet Technologies Ltd): Halt 1 understanding dossier

Run date 2026-10-05. Stage 09b, Sonnet 5.5. Assembly from committed blocks B00 to B09, B12a to B12d, confidence and B13, plus the final files. Sections 1 to 5 add no research. Section 6 reads corpus text for anchored quotes only.

Units. Corpus filings print INR Lakhs (100 Lakhs = ₹1 Cr). Screener prints INR Cr. Every figure carries its unit. Page anchors are the [page N] markers of the pre-extracted .txt beside each PDF, not the printed folio.

Assembly notes the operator should know before reading.

- Corrected figures used. Promoter and group held 89.18% before the IPO and 64.94% after it (PROSP p.21, p.35, p.182; B12a). Top five suppliers supplied 53.15% of FY23 purchases (PROSP p.32; B12a). ZeaCloud FY26 turnover is 534.43 Lakhs (AR26 p.69; B12a). The Netweb FY26 profit figure with the failed page cite is not used.
- Verifier B found three stage 5 and 6 readings overstated (B12b): the Q1 inventory build called small, the NVIDIA allocation premise, and the phrase "deflected every time" for the June 2025 leg. This dossier uses the corrected reading. The stock gain reading of the Q1 margin keeps equal standing with the mix reading.
- Open operator ruling carried from the confidence file. B12b states two bases: 90.9% counting partial catches, 54.5% counting full catches only. The 54.5% basis sits below the 60% line the framework sets for re-running stages. The orchestrator used the stated 90.9%. The operator rules on it at Halt 1.
- Date labels. B00 dates the two transcripts 20 Jun 2025 and 17 Aug 2026. Those are the dates of the company cover letters. The calls ran on 19 Jun 2025 and 13 Aug 2026 (cover letters, JUN25 p.1 and AUG26 p.1).
- File count. B00 prose says 33 Reg 30 filings were fetched. The task message says 30. The B00 manifest lists 28 announcement files (27 with extractable text, one scanned and corrupt). The three counts are not reconciled in the corpus.
- B08 quotes a market quotation range for the shares in its analyst note. It is not carried here.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

Inventory only. Source: B00 manifest and input_gaps, plus the stage blocks that name documents.

1. CONCALLS
   - Concall_Jun_2025_Transcript.pdf. FY2024-25 results investor call held 19 Jun 2025; cover letter 20 Jun 2025 (B00; JUN25 p.1).
   - Concall_Aug_2026_Transcript.pdf. Q1 FY2026-27 call held 13 Aug 2026; cover letter 17 Aug 2026 (B00; AUG26 p.1).
   - Not held: any H1 FY26 call (none was run; B00). The 22 Jun 2026 FY26 investor meet has a deck but no transcript, only a recording (B00).
   - Most recent quarter covered: Q1 FY27 (quarter to 30 Jun 2026).
   - Has a more recent quarter plausibly reported? No. Q2 FY27 (quarter to 30 Sep 2026) is due in the H1 FY27 print, expected by mid November 2026 (B13 falsification_metric). Today is 5 Oct 2026, so no newer transcript is plausibly missing. The September 2026 shareholding pattern is also not yet filed (B08).
   - Peer transcripts held for B06: 12 (NETWEB 4, ORIENTTECH 4, RPTECH 4; B00 manifest).
2. ANNUAL REPORTS
   - Annual_Report_2025.pdf (FY2024-25) and Annual_Report_2026.pdf (FY2025-26). The FY26 Board report and AOC forms are dated 12 Aug 2026; the audit report is dated 28 May 2026 (AR26 p.68, p.132).
   - Latest completed FY (FY26, year to 31 Mar 2026) is present: yes.
   - At least three years held: no. Two reports. The FY2023-24 AR was not collected (two-most-recent rule; B00). FY21 to FY23 come from the prospectus restated financials; FY24 comes from AR FY25 comparatives (B01).
3. RESULTS FILINGS
   - 2025-11-14 board outcome, H1 FY26 (half year to 30 Sep 2025).
   - 2026-05-28 board outcome, FY26 audited (year to 31 Mar 2026).
   - 2026-08-12 board outcome, Q1 FY27 (quarter to 30 Jun 2026). This is the latest. It was the first voluntary quarterly print (B00).
   - Gap to the latest AR: one quarter. The AR covers the year to 31 Mar 2026 and the latest results cover the quarter to 30 Jun 2026. The Q1 FY27 filing carries no balance sheet and no cash flow statement (B05).
4. INVESTOR PRESENTATIONS
   - Investor_Presentation_Jun_2026.pdf, for the 22 Jun 2026 investor meet (latest held).
   - Investor_Presentation_Sep_2025.pdf.
   - The Q1 FY27 deck shown on the 13 Aug 2026 call ("This slide presents...", AUG26 p.7) is not held. Whether it was filed as a separate document is not established in the corpus.
5. RESEARCH AND RATING
   - CRISIL rationale dated 2026-07-02, full text (inputs/rating .txt; HTML original in inputs/other).
   - CRISIL 2024 and 2025 rationales: not collected (B00).
   - research/ folder: empty. No broker or research note held.
6. CORPORATE ACTIONS
   - Reg 30 filings from 2025-09-01 to 2026-09-30 (28 files in the manifest). Content groups: orders (29 Sep 2025, 14 Oct 2025, 3 Mar 2026 ONGC, 13 Jul 2026 with the C-DAC order); ZeaCloud (7 Nov 2025 registered office change; 9 Feb 2026 investor talks); income tax summons (28 Feb 2026, intimation and press release); NVIDIA partner tier and warrant lapse (both 29 Apr 2026); promoter encumbrance declaration, scanned (19 May 2026); results press releases; CRO appointment (29 Jul 2026); XBRL clarification (27 Jul 2026); AGM notice and outcome (24 Aug, 25 Sep, 30 Sep 2026).
   - Before September 2025: not collected. This includes the 10 Jan 2025 Fluidech acquisition filing and the 3 Feb 2025 EGM notice that B08 could not reach.
   - Shareholding: only two quarters held, 31 Mar 2026 and 30 Jun 2026 (NSE SHP XBRL).
7. FRESHNESS PAIR CHECK. B00 freshness_verdict: FRESHNESS PAIRS OK. All four pairs PASS: Q1 FY27 results to the Aug 2026 transcript; CRISIL 2026-07-02 bulletin to the full rationale; SEBI order to order text (no order referenced in the corpus); FY26 AR to the FY26 audited results of 28 May 2026. No failed pair, so no freshness cap applies. One watch item: B08 found, by web search, a SEBI action on 18 Aug 2026 against the IPO lead manager Corporate Capital Ventures (Moneylife). No corpus document references it, so the pair did not trigger. The order text is not in the corpus. It goes to the research brief.
8. VERDICT LINE: **CORPUS GAPPED**

| Missing document | Expected source | Kind |
|---|---|---|
| FY2023-24 annual report | NSE annual report archive / company IR page | findable-missing |
| CRISIL rationales 2024 and 2025 | CRISIL ratings site | findable-missing |
| Reg 30 filings before Sep 2025, including 10 Jan 2025 Fluidech acquisition filing and 3 Feb 2025 EGM notice | NSE | findable-missing |
| Shareholding patterns for the other 10 of the last 12 quarters, and Sep 2026 when filed | NSE / BSE | findable-missing |
| Audited accounts of ZeaCloud, Fluidech and Esconet Singapore; Fluidech acquisition-date balance sheet | MCA21 / company | findable-missing |
| Q1 FY27 balance sheet and cash flow statement | NSE (H1 FY27 filing due mid Nov 2026) | not yet filed |
| Q1 FY27 earnings deck shown on the call | company IR page / NSE | findable-missing (existence not established) |
| 22 Jun 2026 investor meet transcript | company IR page (recording only) | plausibly-nonexistent as a transcript |
| H1 FY26 call transcript | none exists | plausibly-nonexistent |
| Broker and research notes (research/ empty) | none for an SME-board name | plausibly-nonexistent |
| SEBI order text on lead manager Corporate Capital Ventures (18 Aug 2026) | SEBI orders page | findable-missing |

Opacity data point for the kill decision. Esconet gives no order book model, no line revenue, no balance sheet in the quarterly print, and a Q1 deck not held. Peers Netweb and Orient disclose order books, and Netweb and Rashi disclose cash flow and working capital days (B06). The missing items are partly a disclosure choice.

Empty-folder confirmation was suppressed by the /step1 autonomy contract (standing answer: continue with the gaps). Empty at stage 0: research/ (B00). The gap list above is repeated in full for that reason.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** Sign-off happens only in claude.ai after live-web stress testing. This section is a draft for the operator to change or reject.

### PART A: THE FROM STATE

**A1. Archetype, per line.**

- Core integration and resale line (97.61% of FY26 consolidated revenue is product sales, B04; includes traded hardware, integration and Singapore trading). Nearest archetype: Outsourcing partner (CDMO/EMS/IT services). The fit is partial. Client concentration, wallet share and price per unit apply (B03, B04). Contract stickiness does not: the MD describes a 60 to 90 day order cycle with no order book model (AUG26 p.15). Margin follows component pass-through, not capacity fill.
- HexaData own-brand servers, workstations and storage (inside the product line; share not disclosed). Archetype: Build-to-spec component maker. The variables are customer capex cycle, content per unit and input cost pass-through (B04, B06).
- ZeaCloud (cloud hosting, 534.43 Lakhs FY26 turnover, B03) fits no known archetype yet. Asset-heavy hosting is its present state (AUG26 p.18). The Licence/scarcity archetype would apply only after a MeitY empanelment, which it does not hold (B05).
- Fluidech (cybersecurity consulting, 538.96 Lakhs FY26 turnover, B03). Nearest archetype: Outsourcing partner (IT services).

**A2. The simple analogy.** Esconet works like a large computer shop that also builds a small range of its own branded computers. It gets servers, storage and network gear from big distributors and makers, then sets them up and supports them at the customer site. Most orders come through tenders where the lowest qualified bid wins, so the shop earns a thin margin on each ₹100 of sales: 13.19% gross and 2.49% before other income in FY26 (B04). Government bodies and public sector firms give a large share of orders and pay slowly. Next to the shop sit a small cloud business, a small cybersecurity consultancy, and a trading office in Singapore that carries a large share of recent revenue at almost no margin (B04, B09). This is where the arrow starts.

### PART B: THE TRANSITION

**B1. From and to, on the QUALITY LADDER.**

| Line | FROM | TO (claimed) | Note |
|---|---|---|---|
| Core integration plus HexaData mix shift | R1 COMMODITY PRICE-TAKER: weak pricing power, 13.19% gross margin, ROCE 11.96% in FY26 (B04, B01) | R3 VALUE-ADDED / SPEC'D SUPPLIER: own-brand AI and GPU systems, Red Hat certified server, backup appliance (B04, B05) | A two-rung claim. The framework base rate is one rung per 2 to 3 years, so a two-rung claim is itself a warning. The TO rung is the dossier's reading of management's "Sovereign Stack" and "better business mix" language (AUG26 p.8). Management names no rung. |
| ZeaCloud and Fluidech credentials | R1 (sub-scale, loss-making: ZeaCloud PAT (10.04) Lakhs, Fluidech PBT (68.01) Lakhs, B05) | R3 only if MeitY empanelment and NCIIPC accreditation convert to revenue (B07) | Together about 1,073 Lakhs of FY26 turnover (534.43 + 538.96, B03) against 35,440.48 Lakhs consolidated (B04). A minor line today. |

**B2. The engine.** Two things must physically change.

1. Product content per order. The share of own-brand HexaData systems, with local content and bundled software or appliances, must rise against resold third-party boxes. Management states HexaData gross margin at 10% to 15% and legacy integration at 7% to 8% (JUN25 p.12; B05). The Q1 FY27 standalone gross margin of 29.16% cannot come from that mix. HexaData at 35% of sales would need about 69% margin (B07). So the mechanism is unproven, and the engine rests on a mix that no document measures.
2. Credential conversion. ISO certificates, then a MeitY application of at least three to four months, then empanelment for ZeaCloud (AUG26 p.14); NCIIPC accreditation turning into contract revenue for Fluidech (B05, B07). These unlock government hosting and critical-infrastructure work. Neither has produced revenue yet (B05).

**B3. The proof gate.** The hard binary, as the committed blocks set it (B05 trigger 1; B07 optionality register; B03 and B04 monitorables). The operator fixes the final binary at sign-off. FTTCP tests it quarterly from the H1 FY27 print (mid November 2026).

- Primary metric: standalone gross margin at or above 20% in Q2 FY27 and again in Q3 FY27, with stock replaced at current cost, and HexaData revenue and gross margin disclosed by line for both quarters (Q1 FY27 29.2%; FY26 13.7%; B05, B07).
- Companion condition on earnings: consolidated EBITDA excluding other income at or above 5% for two straight quarters (Q1 FY27 7.03%; FY26 2.49%; B03, B04).
- Companion condition on cash: CFO excluding fixed deposit movements positive, CFO to PAT above 0.7, and receivables older than six months below 10% (FY26 19.9%; B03, B04).
- Until the primary metric fires, the transition is narrative and the name is research (B13: proof gate NOT FIRED).

**B4. The recognition gap (to be resolved at Stage 11).** Open question only. Does the TO state, a value-added own-brand supplier, already look reflected in the market pricing of the shares? Stage 11 resolves it through the PE gap. This file states no number, no conclusion and no verdict. If the TO state is already reflected, the re-rating engine is gone and only earnings growth remains.

**B5. The ugliness test.** The ugly optic: FY26 profit fell 23% while revenue grew 54%, operating cash flow was negative, inventory tripled, and old receivables rose with no provision (B13, B02, B01).

Draft classification: **STRUCTURAL-FEATURE**, on today's evidence. The operator makes the final call. Evidence for the draft:

- Cumulative CFO from FY21 to FY26 is (798.86) Lakhs against PAT of 2,234.14 Lakhs, a ratio of -0.36. CFO was negative in four of six years, including FY21, FY23 and FY24, which are not the transition years (B01).
- Receivables older than six months rose from 3.8% to 12.6% to 19.9% of the parent book with no provision (B02).
- Return on capital fell from 60.6% in FY23 to 11.96% in FY26. The worst cash year is the latest year, so this is not a post-IPO rebase (B01; gate recommendation text).
- Government customers pay slowly and need guarantees funded by bank deposits (PROSP p.77 via B04). That is a feature of the channel, not of one year.

Evidence against (the ARTIFACT-OF-CLIMB reading):

- Revenue grew 54% in FY26 and inventory grew with it, which fits a growth build (B13, B01). Net cash, 8.3 times interest cover and debt to equity of 0.17 are sound (B01).
- No Q1 FY27 balance sheet or cash flow exists, so the latest quarter cannot be tested (B05). Cash conversion is INDETERMINATE (B13).

The separating observation is the H1 FY27 CFO excluding fixed deposit movements, with receivables ageing by customer.

**B6. The transition falsifier.** Evidence that kills the arrow:

- Q2 FY27 standalone gross margin back near the FY26 level of 13.7% (B13 falsification_metric). At that level the Q1 profit step was a stock and price gain, or a one-time repricing, and the margin transition has no evidence (B05, B06).
- Or no HexaData revenue and margin by line after the Q2 FY27 print (B04 red-line item).
- Or a Q2 FY27 gross margin fall as high-cost stock turns while peers hold their band (B06 cross-peer hypothesis).

### PART C: WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from the engine and the proof gate; these become the Role 5.5 tracker signals).

1. Standalone gross margin after stock replacement. Q1 FY27 29.16%, FY26 13.72% (B07). Three live readings: HexaData mix, a one-time stock and price gain, fixed-price contracts repricing as at Orient (B06).
2. HexaData revenue and margin by line, and the revenue base ex-Singapore. Not disclosed. Singapore was 5,332.02 Lakhs of the Q1 consolidated 11,632.69 Lakhs at a net profit of 29.67 Lakhs (Q1 BM p.10, p.7; B12b). The MD gives an order book guess of ₹20 to 25 Cr (AUG26 p.15).
3. Cash conversion: CFO excluding fixed deposits, inventory build and old receivables. FY26 consolidated CFO (882.50) Lakhs; inventory 1,894.21 to 5,149.87 Lakhs; 2,428.94 Lakhs of inventory outside the parent is unreconciled (B02).
4. Credential conversion: MeitY empanelment for ZeaCloud and Fluidech's path to break-even. Empanelment timing has moved from "a little far away" (JUN25 p.4) to within FY27 (AUG26 p.14). Fluidech turnover 538.96 Lakhs against a guided ₹15 to 20 Cr (B05).

**C2. What the model rejects as noise.**

- Market size. The serviceable market is about 70 times Esconet's India revenue (B09). The binding limit is working capital and execution, not demand. B09 itself says market size is not the binding limit.
- Spot-year ROCE and reported EBITDA margin on total income. Company EBITDA includes other income, 28.0% of FY26 EBITDA (B04, B02).
- Reported ratio tables in the AR. DSCR 0.47x cannot be rebuilt (B02).
- Pipeline claims. The ₹100 Cr pipeline is a pipeline, not a contracted order book (B04). The ₹500 Cr vision carries no period (Sep 2025 deck p.19).
- Consolidated revenue growth by itself. Singapore trading carries a large share at a 0.5% net margin (B09).

**C3. The business falsifier.** Evidence that forces re-declaring the FROM business itself, kept apart from B6:

- An audited Singapore balance sheet, customer list or stock location showing the Singapore revenue (45.8% of Q1 consolidated, derived, B12b) is thin pass-through trade or non-arm's-length. The FROM state would then read as a trading business with a small Indian integrator inside it.
- Any write-down or non-existence finding on the unreconciled 2,428.94 Lakhs of subsidiary inventory (B02). That would move the FROM state toward an accounting-driven earnings base.
- An income tax or SEBI finding that ties IPO-era pre-IPO placements to promoters (B08 analyst note). That would change what business the shareholders own.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted at Halt 1 from B01 to B09 as specified in prompts/13-synthesis-pipeline.md, BUSINESS UNDERSTANDING NARRATIVE section. Stage 13's copy remains the final version.

Esconet supplies servers, storage, network gear and NVIDIA GPU systems from distributors and makers, then configures, installs and supports them at the customer site (B04). It also assembles servers under its own HexaData brand, including AI and GPU systems, and its September 2025 deck counts more than 6,000 HexaData servers and workstations delivered since 2018 (B04). Product sales were 97.61% of FY26 consolidated revenue of ₹354 Cr and service charges were 2.39%, and no filing, deck or call splits HexaData from traded hardware (B04, B05). Beside the core sit ZeaCloud, a cloud subsidiary with ₹5.34 Cr of FY26 turnover, Fluidech, a 70% owned cybersecurity firm with ₹5.39 Cr, and a Singapore trading arm at about 13.8% of FY26 revenue (B03, B04). A customer needs a vendor that delivers working compute and sits on the tender lists, and many resellers clear that bar (B04). The customers are government bodies and public sector firms such as NIC Services, ONGC, Indian Oil and C-DAC, enterprises, universities, and the Indian Army on a long secure cloud engagement (B03, B07). In FY23 the top five clients gave 41.35% of revenue and government gave 35.75%, and the MD puts government at 40% to 45% for FY26 (B03, B05). These customers award orders through tenders, place purchase orders with no long contracts, pay slowly and ask for guarantees funded by bank deposits (B04). Present demand comes from AI compute spending and government digitisation, and the run ties it to three downstream signals: IndiaAI Mission GPU tenders, the ₹25.74 Cr C-DAC order with other GeM awards, and NVIDIA data centre results with the memory price trend (B09). Part of the rupee demand is component price, because memory and storage prices rose two to three times without adding units, and the run did not establish how much of Esconet's growth is units and how much is price (B06). Forward growth rests on the 20,000 GPUs announced under IndiaAI Mission 2.0, a MeitY cloud empanelment for ZeaCloud, and NCIIPC and CERT-In directives for Fluidech, each visible in a public notice (B09). The quarterly results and order books of Netweb, Rashi Peripherals and Orient Technologies show the same customers' demand before Esconet reports (B06, B09). The serviceable market of Indian enterprise and government servers outside hyperscale is about ₹21,139 Cr and Esconet holds about 1.4% of it, so the run treats market size as a minor limit (B09). No business line shows a moat in the margin, and traded hardware has none, since its gross margin fell from 15.23% to 13.19% when component prices rose in FY26 (B04). HexaData has weak signs, a Red Hat certified server and a launched backup appliance, but R&D is under 2% of revenue and its NVIDIA Elite tier is a reseller credential its own filing ties to no material financial impact (B07, B12b). ZeaCloud has flat revenue, a loss and no empanelment, and Fluidech rests on an NCIIPC accreditation the run did not see on file (B05, B07). The emerging moat scan scored 5.5 with no category at Moderate, and rows I1 and I2 scored zero (B07).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed

**Vertical 1: Standalone gross margin after stock replacement.**
- The corpus establishes: Q1 FY27 standalone gross margin 29.16% (revenue 6,107.71, purchases 4,845.14, stock change +518.50 Lakhs) against 13.72% for FY26; a fall back to 13.72% on Q1 revenue removes 943.10 Lakhs of gross profit against a Q1 standalone PBT of 935.67 Lakhs (B07; Q1 BM p.4). The MD credits execution, hardware price volatility and inventory, and will not size them (AUG26 p.10, p.12; B05). Peers split: Netweb denies any memory price gain, Orient's EBITDA rebound came from fixed-price contracts ending 31 Mar 2026, Rashi allows a stock gain "to some extent" (B06).
- It cannot establish: line revenue and margin; the stock gain share of Q1; the consolidated gross margin trend (no peer states a gross margin level, B06).
- Deciding questions: (1) What is the Q2 FY27 standalone gross margin after stock is replaced at current cost? (2) What share of Q2 revenue is billed on orders priced before the component rise? (3) What are HexaData revenue and gross margin by line?

**Vertical 2: HexaData mix and the revenue base ex-Singapore.**
- Establishes: one reportable segment (AR26 p.76, p.137); products 34,593.19 and service charges 847.30 Lakhs (AR26 p.143); HexaData about 35% of FY25 revenue per the MD (JUN25 p.9; B05), with the split refused in Aug 2026 (AUG26 p.15). Singapore was 5,332.02 Lakhs of the Q1 consolidated 11,632.69 Lakhs (Q1 BM p.10, p.7). Standalone Q1 revenue sat 18% below the FY26 quarterly average (B05). FY27 revenue "not significantly bigger" (AUG26 p.16) against a Q1 annualised run-rate of about ₹465 Cr (B09).
- Cannot establish: HexaData order book, GPU order value, Singapore customers and stock location, a contracted backlog (MD guess ₹20 to 25 Cr).
- Deciding questions: (1) Q2 revenue split into standalone, Singapore and the rest. (2) HexaData revenue and gross margin by line. (3) What does Esconet Singapore supply, to whom, and where is its stock?

**Vertical 3: Cash conversion and working capital.**
- Establishes: cumulative CFO to PAT -0.36 over FY21 to FY26 (B01); FY26 consolidated CFO (882.50) Lakhs; standalone CFO 1,568.45 includes 1,745.95 Lakhs of fixed deposit liquidation, so ex-FDR about (177.50) (B02); inventory 1,894.21 to 5,149.87 Lakhs (AR26 p.132); receivables over six months 893.06 of 4,499.21 Lakhs, 19.9%, no provision (B02); delayed supplier payment interest 30.63 against 1.15 Lakhs (B02). The FY26 balance sheet differs between the results filing and the AR: receivables 1,963.93 against 4,426.93 Lakhs (B01).
- Cannot establish: Q1 FY27 balance sheet and cash flow; the 20.2 debtor days claim; receivables by customer; Singapore stock.
- Deciding questions: (1) What is H1 FY27 CFO excluding fixed deposits? (2) What is the ageing by customer and by government against private? (3) Which FY26 balance sheet is the filed truth, and why do the two differ by 2,463.00 Lakhs?

**Vertical 4: Credential conversion (ZeaCloud and Fluidech).**
- Establishes: ZeaCloud turnover 534.43 against 525.13 Lakhs, +1.8%, and PAT 110.82 to (10.04) Lakhs (B05). Fluidech turnover 538.96 Lakhs and PBT (68.01) Lakhs against a June 2025 estimate of ₹15 to 20 Cr and a 25% to 30% operating margin (B05; JUN25 p.6, p.9). Empanelment timing slipped across three statements (B05 timeline_slippages). No NCIIPC letter, GeM listing document or ISO certificate is in the corpus (B07).
- Cannot establish: whether ISO certificates are held, whether a MeitY application was filed, any Fluidech contract value.
- Deciding questions: (1) Are the ISO certificates issued and the MeitY application filed, and when? (2) What are Fluidech's contracted values? (3) What is ZeaCloud's third-party revenue and asset base?

### 4b. Candidate signal table (UNVERIFIED; Role 5.5 in claude.ai verifies and writes the tracker)

Source column draws on the B09 likely_source field. Mapping to Downstream_Source_Discovery_Protocol_v1_0 is confirmed at Role 5.5.

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| IndiaAI Mission GPU tenders, empanelment rounds, Mission 2.0 20,000 GPU additions | No GPU tender or award notice for two straight quarters, or awards that exclude domestic integrators | Event-Driven | MeitY / IndiaAI Mission portal, PIB |
| MeitY cloud empanelment status and ISO certificates for ZeaCloud | ISO certificates not issued by Dec 2026, or empanelment slips past FY27 (B05 kill signal) | Event-Driven | MeitY empanelled CSP list; Esconet Reg 30 on NSE |
| NVIDIA data centre revenue, India partner allocation commentary, memory and storage price trend | Component contract prices fall while Esconet holds high-cost stock (B05 kill signal) | Quarterly | NVIDIA 10-Q and call; peer concalls (Netweb, RPTECH, Orient) |
| Netweb, RPTECH, Orient quarterly results and order books | Peers report margin compression or a falling order book while Esconet reports expansion | Quarterly | Peer exchange filings and transcripts |
| C-DAC order ₹25.74 Cr (ex-GST) billing and collection; PSU tender awards on GeM | No billing by the Q3 FY27 print, or receivables over six months rise above 19.9% (B03) | Event-Driven | Esconet Reg 30 orders; GeM portal |
| NCIIPC and CERT-In directives; DSCI spend data | Fluidech PBT still negative in FY27 with no stated revenue (B05) | Event-Driven | CERT-In and NCIIPC notices; DSCI reports |
| USD INR rate and RBI policy | Sustained rupee move that lifts landed cost while Esconet gross margin falls and peers hold | Monthly | RBI reference rate; RBI policy statements |

### 4c. Fragility read

- variable_count: 8. The bull case needs these external variables to go right: (1) component price level and repricing lag; (2) government and PSU tender flow including C-DAC and GeM; (3) IndiaAI Mission GPU tenders; (4) MeitY empanelment for ZeaCloud; (5) NCIIPC and CERT-In directives for Fluidech; (6) HexaData mix and margin by line; (7) NVIDIA channel allocation and supply; (8) collection timing of government receivables.
- verifiability_ratio: 5 of 8 externally observable (variables 1 to 5). Three are company-narrated only: HexaData mix and margin (no line disclosure, B04), NVIDIA allocation benefit (the company's own filing says no immediate material financial impact, B12b), and receivable collection by customer (no ageing by customer, B13).
- single_point_failure: yes. Standalone gross margin reverting to the FY26 level of 13.7% breaks the margin leg alone (B13 falsification_metric; B07 shows reversion removes 943.10 Lakhs of gross profit against Q1 PBT of 935.67 Lakhs).
- fragility_verdict: **FRAGILE**. One kill-switch, and three of eight variables rest on company narration.

### 4d. Research brief (claude.ai work order)

Items 1 to 4 are the PENDING LIVE VERIFICATION links raised by the Section 4e chains. Items 5 to 7 are the chains still to be built to reach the Rule F floor of five.

1. PENDING (Chain 1): the GeM bid, award letter and contract for the ₹25.74 Cr C-DAC order (Reg 30, 13 Jul 2026, Annexure A item 6). Read the price variation clause and bid validity period. This shows who bears a component price rise.
2. PENDING (Chain 1): the latest published DRAM and NAND contract price report from a price tracker for Jul to Sep 2026. Read the direction of component prices, since a falling series with high-cost stock on hand is the B05 kill signal.
3. PENDING (Chain 2): C-DAC payment terms and the funding source for the C-DAC order (C-DAC annual report; MeitY and IndiaAI Mission fund release notices on PIB). This shows who pays and when.
4. PENDING (Chain 2): government receivable ageing in the latest annual reports of Netweb and Orient (B06 found no PSU receivable days in any peer transcript). This gives an external read on government payment cycles.
5. Build Chain 3: the IPO conduct chain. ITD s.131(1A) summons outcome (NSE Reg 30 filings); SEBI order of 18 Aug 2026 on Corporate Capital Ventures (SEBI orders page; Moneylife article 81393); the pre-IPO allottee list in the prospectus against promoter ties.
6. Build Chain 4: the Fluidech related-party chain. NSE 10 Jan 2025 acquisition filing and 3 Feb 2025 EGM notice (consideration basis, valuer, audit committee and RPT approval); Gaurav Gupta MCA records.
7. Build Chain 5: the ZeaCloud and sovereign stack chain. ISO certificates, MeitY application status, MeitY empanelled CSP list; the Merino Consulting Services link (Merino Consulting Services Ltd appears as a customer in FY22, PROSP p.143, and is the intermediary in the 9 Feb 2026 ZeaCloud investment talks; identity not verified).
8. Esconet Singapore: ACRA filings, customers, stock location, and the three total asset values (AOC-1 SGD 33,89,867; auditor 553.64 Lakhs; Q1 limited review 67.09 Lakhs).
9. CRISIL 2024 and 2025 rationales for the working capital trend (CRISIL ratings site).
10. NSE and BSE shareholding patterns for the missing quarters, the Sep 2026 pattern when filed, and any Reg 29 or PIT filing for the 1,36,000 promoter shares gone since 30 Jun 2026 (derived from the AGM voting table; B08).
11. Source URL verification for every B09 downstream candidate against the Downstream Source Discovery Protocol; tracker writes at Role 5.5.
12. NVIDIA partner tier documents. Confirm what the Solution Provider Elite tier gives on allocation (B12b: company filing says no immediate material financial impact; MD says stock comes "from the NVIDIA channel").
13. Policy status. IndiaAI Mission 2.0 20,000 GPU addition (B09), CERT-In and NCIIPC directives for Fluidech.
14. Customer-health reads from counterparty filings for the named customers (NIC Services, ONGC, Indian Oil, C-DAC, Indian Army engagement) where listed filings exist.
15. Forum archaeology on the Fluidech acquisition and the warrant allottees (Wichita Enterprises Private Limited, Top Filings India Private Limited), as B08 left open.
16. Peer Q2 FY27 results and calls when filed (Netweb, RPTECH, Orient), to test the cross-peer hypothesis in B06 against Esconet's Q2 print.

### 4e. Second-order stub (Master Prompt v3.7, Rule F)

Tier tags used below: FILED (company filing), MGMT CLAIM (call or deck), PEER (peer transcript), DERIVED (arithmetic in a block). Every INFERENCE is labelled. No new number appears.

```
CHAIN 1: Q1 FY27 standalone gross margin 29.16% against FY26 13.72% (B07; Q1 BM p.4);
the MD says hardware price volatility "has played some role" and inventory
"contributed to some extent" (B05; AUG26 p.10, p.12)
Link 1 [PEER]: Memory, storage and CPU prices are up, RAM two to three times, with no
  easing seen for about a year. The margin effect splits by contract architecture:
  markup distributors gain, own-brand makers stay in band, fixed-price integrators took
  a shock and then a rebound as contracts repriced (B06; ORIENTTECH Q1 FY27 p.4, p.6).
Link 2 [FILED]: Consolidated inventory rose 1,894.21 to 5,149.87 Lakhs in FY26 and the
  Q1 FY27 stock change was +518.50 Lakhs (AR26 p.132; Q1 BM p.4). Advances to suppliers
  rose 14.49 to 155.32 Lakhs with no description (B02 rank 12).
Link 3 [INFERENCE]: If Esconet purchased or prepaid stock before the price rise and
  billed after it, the Q1 margin holds a holding gain that lasts only while pre-rise
  stock lasts. If its contracts repriced as Orient's did, the margin resets to a new
  level that persists. If HexaData mix did it, the margin persists and line disclosure
  follows. Q2 gross margin separates the three readings.
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web opens (a) the GeM bid, award
  letter and contract for the ₹25.74 Cr C-DAC order (Reg 30, 13 Jul 2026, Annexure A
  item 6) for the price variation clause and bid validity, and (b) the latest published
  DRAM and NAND contract price report for Jul to Sep 2026. No counterparty fact is
  stated here.
Binding constraint: Working capital. Inventory build is funded by short-term borrowing
  of 1,208.85 Lakhs in FY26 and an overdraft of 1,187.42 Lakhs that rolls (B02 rank 6;
  B07 cash warning). Contracts on capital account are NIL (AR26 p.117, p.145), so capex
  does not bind. The FY26 inventory build took 26.2% of incremental revenue (B09
  capacity_check, derived).
Unsaid: The call did not size the stock effect. Consolidated inventory outside the parent
  is 2,428.94 Lakhs and unreconciled in the notes (B02 rank 9). Singapore total assets
  carry three values (AOC-1 SGD 33,89,867; auditor 553.64 Lakhs; Q1 limited review 67.09
  Lakhs; B12b). The footnote that implies unmentioned demand: advances to suppliers rose
  more than tenfold (B02 rank 12), which fits forward purchasing that nobody described.
Observation that confirms or breaks this chain, and confirm-by date: In the H1 FY27
  results (mid November 2026, B13), Q2 FY27 standalone gross margin at or above 20% with
  the quarterly stock change at or below 500 Lakhs confirms the persistent readings.
  Q2 gross margin near the FY26 level of 13.7%, or a stock build above 500 Lakhs
  without orders, breaks the chain (B03 monitorables; B05 trigger 1).
```

```
CHAIN 2: C-DAC order of ₹25.74 Cr ex-GST (Reg 30, 13 Jul 2026; B07 catalysts) and
government at 40% to 45% of FY26 revenue (AUG26 p.17; B05)
Link 1 [FILED]: Government projects come through the GeM marketplace. They need
  performance bank guarantees or earnest money in the form of bank fixed deposits, which
  blocks working capital (PROSP p.77, via B04; the prospectus states the same for the
  FY23 jump in government revenue share from 20.58% to 35.75%).
Link 2 [FILED]: Receivables over six months rose 3.8% (FY24), 12.6% (FY25) and 19.9%
  (FY26) of the parent book, with no provision (B02). Standalone FY26 CFO of 1,568.45
  Lakhs includes 1,745.95 Lakhs of fixed deposit liquidation (B02 rank 4).
Link 3 [INFERENCE]: A large government order lifts revenue and gross profit when it
  bills, and also lifts two cash users together: receivables until collection, and
  guarantee deposits. If collection runs past the 30 to 90 days the MD describes (AUG26
  p.15), the order raises reported profit while CFO stays negative. The same order
  therefore tests the cash conversion test and the margin leg in the same quarter.
Who pays, and why now: PENDING LIVE VERIFICATION. Claude web opens (c) C-DAC payment
  terms and the funding source for the order (C-DAC annual report; MeitY and IndiaAI
  Mission fund release notices on PIB) and (d) government receivable ageing in the latest
  annual reports of Netweb and Orient, since B06 found no PSU receivable days in any peer
  transcript. No counterparty fact is stated here.
Binding constraint: Guarantee lines and working capital. Overdraft 1,187.42 Lakhs rolling
  and secured on directors' property (B02 rank 6) sits beside a CRISIL statement that the
  7.50 Cr working capital facility is unused (CRISIL rationale 2026-07-02, line 31, quoted
  in the gate file). The two do not reconcile in the corpus. FY26 capex of 797.13 Lakhs and
  goodwill of 851.11 Lakhs were funded by short-term borrowing and equity (AR26 p.134;
  B07).
Unsaid: The parent sold 568.79 Lakhs of goods to its own subsidiary ZeaCloud, 106.4% of
  ZeaCloud's FY26 turnover of 534.43 Lakhs, with no profit elimination in Schedule III
  (B02 rank 8; AR26 AOC-2 p.68). That is intra-group demand nobody mentioned on the call.
  The June 2026 deck says vendors were paid on time while the AR shows delayed supplier
  interest of 30.63 against 1.15 Lakhs (B04 deck-versus-filing warning).
Observation that confirms or breaks this chain, and confirm-by date: The H1 FY27 filing
  (mid November 2026) is the first with a balance sheet and cash flow since the FY26 AR.
  CFO excluding fixed deposit movements positive, CFO to PAT above 0.7, and receivables
  over six months below 10% confirm collection; receivables over six months at or above
  20%, or a first provision, break it (B03 monitorables; B04 must_track_metrics). C-DAC
  billing and collection shows in the Q3 FY27 print; no block states that print date.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Esconet is a Delhi firm that supplies servers, storage and network gear and sets them up at the customer site (B04).
2. It also builds its own HexaData servers, including AI servers with NVIDIA chips (B04).
3. It owns a small cloud business, a small cybersecurity firm and a trading office in Singapore (B03, B04).
4. Government bodies, public sector firms, large companies and universities place the orders (B03, B07).
5. They award work through tenders, pay slowly and ask for guarantees backed by bank deposits (B04).
6. Demand today comes from AI computing spend and government digital projects (B09).
7. Part of the rise in rupee sales is higher component prices, not more units. The run could not split the two (B06).
8. Growth could come from IndiaAI GPU tenders, a cloud approval called MeitY empanelment, and cyber rules for critical systems (B09). Each one has public signals.
9. The moat is weak. Traded hardware has none, and its gross margin fell to 13.19% in FY26 (B04). HexaData and the credentials are early and unproven (B07).
10. The mental model, in draft: a thin margin hardware integrator that claims to climb to a value added own-brand supplier. The proof so far is one quarter of margin, and nobody has shown the cause (B05, B13).
11. The fragility read is FRAGILE. One variable, the standalone gross margin, can break the thesis alone. Three of eight needed variables rest on company statements (Section 4c).
12. The corpus could not show revenue or margin by business line, a Q1 FY27 balance sheet or cash flow, an order book beyond a guess, or the Singapore books (B04, B05, B02).
13. The corpus holds two annual reports and two calls. Many dated filings, rating papers and shareholding quarters are missing (Section 1).
14. Biggest open question one: is the Q1 FY27 margin a mix gain, a one-time stock gain, or fixed-price contracts repricing? Q2 FY27 gross margin decides it (B06).
15. Biggest open question two: does profit turn into cash? Six-year cash flow from operations is negative against positive profit, and the tax summons on the IPO is still open (B01, B08).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Quote-then-comment. Quotes are as printed. Anchors are the .txt [page N] markers, as stated in the assembly notes. Amounts in the filings are INR Lakhs unless the quote shows otherwise. The annex states no valuation or verdict.

### 1. UNITS

- Quote: "6,000+ HEXADATA SERVERS & HIGH-PERFORMANCE WORKSTATIONS SOLD SINCE 2018" (Investor_Presentation_Sep_2025.pdf p.4). Also on the same page: "~28 Petabytes OF VARIED DATA STORAGE SYSTEMS INSTALLED" and "60,000+ ETHERNET PORTS ALREADY DELIVERED ACROSS DATA CENTRES AND CAMPUS NETWORKS."
- Quote: "a single deal can go as up high up as five up to 500 servers also." (Concall_Jun_2025_Transcript.pdf p.4).
- Quote: "Sales of IT products 34,593.19 22,879.43 ... Service Charges 847.30 150.38 ... Total 35,440.48 23,029.80" (Annual_Report_2026.pdf p.143, consolidated, INR Lakhs, FY26 then FY25).
- Quote: "Do you have any kind of breakup of Hexa data versus non-Hexa data business, what we did? Ready at hand? ... No, sir." (Concall_Aug_2026_Transcript.pdf p.15).
- Comment: No per-unit figure (rate per server, revenue per case) is printed anywhere in the corpus. The unit counts are cumulative since 2018 and cover a basket (servers plus workstations). HexaData revenue is not disclosed. A per-unit rate therefore cannot be derived. The two lines that exist are the cumulative unit count and the product revenue line above. B04 uses ₹100 of consolidated revenue as the unit.

### 2. SEGMENT CAPITAL AND DEBT

- Quote: "The Company operates exclusively within the Information Technology Services domain ... thereby constituting a single reportable business segment. Consequently, primary and secondary reporting disclosures for business or geographical segment as envisaged in AS-17 stand as inapplicable to the Company." (Annual_Report_2026.pdf p.76). Repeated at p.107 and p.137, and in "the Company operates in a single reportable business segment. Accordingly, separate segment information has not been disclosed." (results 2026-08-12 p.8).
- Quote, consolidated balance sheet, INR Lakhs, 31 Mar 2026 then 31 Mar 2025 (Annual_Report_2026.pdf p.132): "Long-term Borrowings 104.99 42.52 ... Short-term borrowings 1,219.34 10.49 ... Total 15,565.08 11,686.90."
- Quote, entity level, AOC-1: "Total assets 14,84,31,495 6,74,97,000 33,89,867 ... Total Liabilities 14,84,31,495 6,74,97,000 33,89,867" for ZeaCloud and Fluidech (INR) and Esconet Singapore (SGD) (Annual_Report_2026.pdf p.69).
- Quote: "Group's share of total assets of Rs. 67.09 Lakhs as at June 30, 2026" for Esconet Singapore (results 2026-08-12 p.10).
- Comment: Segment assets, segment liabilities, capital employed and borrowings by segment are NOT DISCLOSED, because the company reports one segment. Borrowings are unallocated. Total consolidated borrowings were 1,324.33 Lakhs at Mar 2026 and 53.01 Lakhs at Mar 2025 (sum of the printed lines; B03). The AOC-1 entity totals above are not segment capital, and the Singapore total assets carry three different values (AOC-1 SGD 33,89,867; auditor 553.64 Lakhs per B02; Q1 limited review 67.09 Lakhs). The Q1 FY27 filing carries no balance sheet, so the latest two periods are Mar 2026 and Mar 2025.

### 3. GUIDANCE VERSUS ASPIRATION

Classes: (a) guidance with a period; (b) aspiration without a period; (c) capacity or capability only.

| # | Quote (file, page) | Class |
|---|---|---|
| 1 | "in the current year I feel easily we should be seeing a growth of around 50 to 60 percent in terms of revenues." ZeaCloud (Concall_Jun_2025 p.6) | (a) FY26 |
| 2 | "They should be able to clock easily approximately around 15 to 20 crores this year. That's what my estimate is." Fluidech (Concall_Jun_2025 p.6) | (a) FY26 |
| 3 | "This year, I am eyeing somewhere around 8 - 8.5 crores from Zeacloud, approximately around 15 - 20 crores from Fluidech." (Concall_Jun_2025 p.9) | (a) FY26 |
| 4 | "approximately around 30 to 40 percent, at least bare minimum for the next upcoming three to four years' time." ZeaCloud and Fluidech growth (Concall_Jun_2025 p.9) | (a) three to four years |
| 5 | "it should sustain at approximately around 20 to 25 percent operating margin ... the Fluidic operating margin should also be similar, 25 to 30 percent operating margin." (Concall_Jun_2025 p.9) | (b) no period in the quote; B05 reads it as FY26 |
| 6 | "30 percent approximately the total employee cost will go up. ... Next year, it may not increase at that rate." (Concall_Jun_2025 p.9) | (a) FY26; FY27 direction only |
| 7 | "in the current year, margins will definitely improve ... may or may not be exceeding last year's margin ... for next year ... we would be exceeding that, those margin percentages by far." (Concall_Jun_2025 p.7) | (a) FY26 and FY27, no number |
| 8 | "we feel that these margins are pretty much sustainable and the coming quarters will also reflect similar sentiments." (Concall_Aug_2026 p.10) | (a) FY27, no number |
| 9 | "Top line should be better. And bottom lines, I expect at the end of the quarter should be like what Q1 could be with a small variation here and there." (Concall_Aug_2026 p.11) | (a) Q2 FY27 |
| 10 | "It could be 7 percent, it could be 6 percent, it could be 5 percent, it could be 10 percent also." (Concall_Aug_2026 p.16) | (a) FY27 range |
| 11 | "We are not expecting anything much significantly bigger than what we did last year." (Concall_Aug_2026 p.16) | (a) FY27, no number |
| 12 | "expecting an increase in revenue to Rs 370-400 crore" (CRISIL_Esconet_Rating_Rationale_2026-07-02.txt line 26, per B12a; the HTML has no page numbers) | (a) FY27, third-party record of a company expectation; no company primary source in the corpus |
| 13 | "Last year, we did almost like 5-5.5 crores in Zeacloud and this year also, we are expecting similar kind of numbers in Zeacloud." (Concall_Aug_2026 p.18) | (a) FY27 |
| 14 | "in the current financial year, there are no plans to raise any funds." (Concall_Aug_2026 p.14) | (a) FY27 |
| 15 | "by September end, I hope that we should get all our ISO certifications done. Once those are done, we shall apply with Meity, which is a process of at least three to four months ... So, within this financial year, we should get that good news" (Concall_Aug_2026 p.14) | (a) FY27 |
| 16 | "Current order book in pipeline ₹ 100 Cr+ ... A Vision to build a ₹500 Cr+ company" (Investor_Presentation_Sep_2025 p.19). On the call: "if it is 100 CR value ... But that may not be anytime soon." (Concall_Aug_2026 p.16) | (b) no period |
| 17 | "3 to 5 years, we would be there. We would continue to grow." (Concall_Aug_2026 p.15), after "I would not want to comment today on that." | (b) no number, no period |
| 18 | "We are not committing growth numbers." (Investor_Presentation_Jun_2026 p.17) | states no guidance |
| 19 | "we have invested in capacity expansion for the manufacturing facility for Hexadata." (Concall_Jun_2025 p.4); "We have expanded the capacity to almost like 3x." ZeaCloud (Concall_Jun_2025 p.11) | (c) capacity |
| 20 | "If it continues to grow at same rate we might achieve sales of around ₹14,000" (EsconetTechnologies_PROSP.pdf p.76, FY24; B03 reads Lakhs and records actual 13,747.50 Lakhs) | (a) FY24 |

Comment: the single revenue range in the corpus (₹370 to 400 Cr) sits in a rating paper, not in a company document. The MD declines to give a number on the call. The ₹500 Cr vision and the ₹100 Cr pipeline carry no period.

### 4. CONCENTRATION

- Quote: "Our top five clients contribute approximately 41.35 %, 37.93% and 32.91% of our revenues from operations for the year ended March 31, 2023, March 31, 2022 and March 31, 2021 respectively." (EsconetTechnologies_PROSP.pdf p.28).
- Quote: "Government 3,384.39 35.75% 1,411.06 20.58% 1,168.90 26.49%" for FY23, FY22, FY21, INR Lakhs (PROSP p.29); H1 FY24 "Government 2,322.8 32.59%" (PROSP p.140).
- Quote, top client FY23: "National Informatics Centre Services INC 1480.68 15.64%", and "National Informatics Centre 596.68 6.30%" listed separately (PROSP p.142 to p.143).
- Quote, top supplier FY23: "Ingram Micro India Pvt Ltd. 2,055.49 27.01% ... Total 4,044.52 53.15%" for the top five suppliers (PROSP p.32).
- Quote: "Till last year, our government revenue was typically around 40 to 45 percent ... Current year, government business has been lower" (Concall_Aug_2026 p.17).
- Quote, product: "Hexadata revenue for us is still approximately around 35 percent. It is one third of our business." (Concall_Jun_2025 p.9). In Aug 2026 the split was not given (AUG26 p.15, above).
- Quote, geography: "90-95% of our business is still happening in India." (Concall_Jun_2025 p.6). Singapore: "Revenue from Singapore is approximately 53 crores." (Concall_Aug_2026 p.15, no period stated). Esconet Singapore FY26 turnover "67,46,372" SGD (AR26 p.69). Q1 FY27 Singapore "total revenue of Rs. 5332.02 Lakhs" (results 2026-08-12 p.10).
- Comment: Top client share is 15.64% (FY23). FY26 top client, top five, top ten and the government share in rupees are NOT DISCLOSED in the AR26 (B03). Product share is a management statement from June 2025, and the geography statement of June 2025 sits against a Q1 FY27 quarter where Singapore is 45.8% of consolidated revenue (derived, B12b). The numbers do not reconcile with each other without a period for the 53 crore figure.

### 5. PROMISE LEDGER

Rows come from B05 promise_delivery (13 rows: 3 delivered, 5 partial, 5 missed). Each row is a delivery test against the filed record. The last four rows are open.

| # | Date made | Promise | Status | Evidence anchor |
|---|---|---|---|---|
| 1 | 19 Jun 2025 | FY26 margins will definitely improve ("margins will definitely improve", JUN25 p.7) | MISSED | FY26 consolidated gross margin 13.19% against 15.23%; EBITDA margin 3.46% against 5.67% (FY26 press release 2026-05-28; B03) |
| 2 | 19 Jun 2025 | ZeaCloud revenue up 50% to 60% in FY26 (JUN25 p.6) | MISSED | Turnover 534.43 against 525.13 Lakhs, +1.8%; PAT 110.82 to (10.04) Lakhs (AR26 p.69). MD admits flat revenue (AUG26 p.18) |
| 3 | 19 Jun 2025 | Fluidech FY26 revenue ₹15 to 20 Cr (JUN25 p.6, p.9) | MISSED | Turnover 538.96 Lakhs (AR26 p.69) |
| 4 | 19 Jun 2025 | Fluidech operating margin 25% to 30% (JUN25 p.9) | MISSED | Fluidech PBT (68.01) Lakhs (AR26 p.69) |
| 5 | 19 Jun 2025 | Employee cost up about 30% in FY26 (JUN25 p.9) | MISSED | Consolidated 933.32 against 557.04 Lakhs, +67.5%, mixed basis (AR26 p.133). B12b: standalone 795.39 against 557.04, +42.8%; the direction stands |
| 6 | 19 Jun 2025 | HexaData unified backup appliance launched in FY26 (JUN25 p.4) | DELIVERED | ResQ launch, Reg 30 filing 2025-09-01. Revenue NOT FOUND |
| 7 | 19 Jun 2025 | No acquisitions under consideration (JUN25 p.8) | DELIVERED | No acquisition in the Reg 30 record Sep 2025 to Sep 2026; earlier months not collected |
| 8 | 19 Jun 2025 | FY26 to continue the same growth path (JUN25 p.6) | DELIVERED on top line only | Total income 23,325.09 to 35,784.11 Lakhs; PAT 615.50 against 799.79 Lakhs (AR26 p.133; B05) |
| 9 | 19 Jun 2025 | Own HPC cluster stack, branding almost done (JUN25 p.4) | PARTIAL | Version 1 ready, POCs done, "may have already shipped already to one or two customers" (AUG26 p.17); no order disclosed |
| 10 | 19 Jun 2025 | Own indigenous cloud platform (JUN25 p.4) | PARTIAL | Orchestration layer in production, observability module pending (AUG26 p.17) |
| 11 | 19 Jun 2025 | MeitY empanelment, "a little far away" (JUN25 p.4) | PARTIAL | Not achieved; ISO certificates then 3 to 4 months, within FY27 (AUG26 p.14) |
| 12 | 19 Jun 2025 | FY27 margin to exceed FY24 "by far" (JUN25 p.7) | PARTIAL | One quarter: Q1 FY27 standalone gross margin 29.16%, consolidated EBITDA 8.55% on total income (Q1 BM p.4, p.7; B05). Standalone against consolidated basis noted by B12b |
| 13 | 17 Nov 2025 | ONGC project cost booked in H1, revenue in the next two quarters, margin reversal in H2 (H1 FY26 press release p.2) | PARTIAL | H2 consolidated EBITDA 4.33% against H1 2.20%, but FY26 3.46% against 5.67% (B05) |
| 14 | 13 Aug 2026 | Q2 FY27 revenue better, profit similar (AUG26 p.11) | OPEN, due in the H1 FY27 print, mid Nov 2026 | none yet |
| 15 | 13 Aug 2026 | ISO certificates by end Sep 2026, MeitY application, empanelment in FY27 (AUG26 p.14) | OPEN | No certificate in the corpus |
| 16 | 13 Aug 2026 | No fundraising in FY27 (AUG26 p.14) | OPEN | The Reg 30 filings to 30 Sep 2026 show none |
| 17 | 13 Aug 2026 | Quarterly reporting every quarter from FY27 (AUG26 p.5, per B05) | OPEN | Q1 FY27 was the first voluntary print (results 2026-08-12 p.5) |

Comment: 3 of 13 closed promises were delivered, 5 partial and 5 missed (B05). All four quantified segment and cost forecasts missed. B12b adds that the deck and press release claims of "strengthening operational cash flows" and of inventory backed by customer orders are contradicted by the filings (B12b).

### 6. RESTATED BASES

- Quote, AR26 notes: "Previous year figure have been regrouped/rearranged wherever necessary to render them comparable with current year figures." (Annual_Report_2026.pdf p.118, standalone Note 15; p.147, consolidated). Q1 FY27: "Previous period/year figures have been regrouped, reclassified and rearranged wherever considered necessary" (results 2026-08-12 p.8).
- Quote, FY25 operating cash flow as first printed: "Net Cash from Operating Activities 5.10 (185.00)" (Annual_Report_2025.pdf p.86, standalone, FY25 then FY24, INR Lakhs).
- Quote, FY25 comparative as printed in the latest filing: "Net Cash from Operating Activities 1568.45 -1,751.68" (Annual_Report_2026.pdf p.104, standalone, FY26 then FY25).
- Quote, FY26 balance sheet in two filings. Results filing: "Trade Receivables 1963.93 5,255.06 ... Total Assets 13102.08 11,686.90" (results 2026-05-28 p.14). Annual report: "Trade receivables 2.13 4,426.93 5,255.06 ... Total 15,565.08 11,686.90" (Annual_Report_2026.pdf p.132).
- Quote, perimeter: "The date when subsidiary was acquired or Incorporated ... 5th September 2023 / 16th April 2025 / 17th September 2024" for ZeaCloud, Fluidech, Esconet Singapore (Annual_Report_2026.pdf p.69).
- Comment: There is no restatement note for a reorganisation. The FY25 standalone CFO moved from +5.10 to (1,751.68) Lakhs, because fixed deposits moved out of cash. The AR describes it only as "regrouped" (B03). The FY26 consolidated base now includes Fluidech from 16 Apr 2025 while the FY25 comparative does not, so cost lines mix bases (B12b). The same FY26 balance sheet has two printed versions, 2,463.00 Lakhs apart on receivables, payables and total assets (B01). The ZeaCloud date in the AOC-1 (5 Sep 2023) does not match the incorporation date of 11 May 2022 that B01 takes from the prospectus. Not reconciled in the corpus.

### 7. CORPORATE-ACTION CLAUSES

No scheme of arrangement, demerger, merger or share repurchase is in the corpus. The filings to fetch for any such item would be the NSE Reg 30 outcome and the scheme document; none is referenced in the 28 filings held. The items that exist:

- Preferential issue. Quote, in print order: "at an issue price of H 345 per equity share/warrant (including a premium of H 335 per unit) completed allotment of 7,34,000 equity shares and 2,13,600 warrants on 24 th October 2024 ... to persons within the Non-Promoter/Non-Promoter Group category." (Annual_Report_2026.pdf p.52; the extract prints the rupee sign as "H"). Approval: "Extra-Ordinary General Meeting held on 13th October 2024" (Reg 30 filing 2026-04-29, forfeiture, p.1).
- Warrant lapse. Quote: "the said warrants have lapsed upon expiry of the exercise period, i.e., with effect from 25th April 2026 ... The total amount forfeited by the Company aggregates to ₹1,84,23,000/-" (Reg 30 filing 2026-04-29, forfeiture, p.1). Allottees: Samir Satish Goenka 27,200; A. Gotham Chand 1,00,000; Wichita Enterprises Private Limited 61,600; Top Filings India Private Limited 4,800; Aahana Bhatia 20,000 (same filing, p.1 to p.2). Annexure A: "Number of warrants exercised Nil" (p.3). Ratio: one warrant to one equity share; 25% upfront, balance "H 258.75 per warrant" (AR26 p.52).
- Revised use of proceeds. Quote: "Total (Net Proceeds) 3,269.22 2,216.53 2,716.53 500.00", columns original allocation, funds utilised, modified allocation, funds unutilised, INR Lakhs (AR26 p.122). The AR Board report states "there has been no variation(s) in the use of proceeds" (AR26 p.52).
- Fluidech share swap. Quote: "The Company allotted 1,02,238 equity shares of face value H10 each at a share premium of H 400.72 per share as per the Share Swap arrangement between Fluidech IT Services Pvt Ltd and Esconet Technologies Limited" (AR26 p.108). Allotment date: "Preferential Allotment 7th April 2025 1,02,238 10,22,380" (AR26 p.54). Acquisition date: "16th April 2025", extent "70%" (AR26 p.69). Cash leg: "Purchase of Shares of FISPL 842.82" to Mr. Gaurav Gupta (AR26 p.147). Investment in subsidiary: "Investment in Subsidiary (Fluidech IT Services) 1532.68" (AR26 p.112).
- Not in the corpus: the share purchase agreement, the acquisition-date liability allocation clauses and the definition of any undertaking. The filings to fetch are the NSE 10 Jan 2025 acquisition filing and the 3 Feb 2025 EGM notice (B08 could not reach either).
- ZeaCloud equity infusion (proposed). Quote: "may result in dilution of the Company's shareholding in the subsidiary" and "No binding agreement, term sheet or commitment has been executed as on date." (Reg 30 filing 2026-02-09, p.1 and p.2). Intermediary: Merino Consulting Services Limited. The MD said the company has no intent to part with any ZeaCloud stake "as of now" (AUG26 p.14).
- IPO. Fresh issue of 33,60,000 equity shares, "₹ 2,822.40" Lakhs (PROSP p.1; issue price ₹84 at PROSP p.2). Listing on NSE SME 23 Feb 2024 per AR25 Note 1 (B01). Exact listing date is not in the corpus text read.
- Comment: Appointed and effective dates exist for the swap, the preferential issue and the warrants, as quoted. Ratios other than the warrant one-to-one do not exist in the corpus. The consideration basis for the Fluidech swap price of 410.72 per share is NOT FOUND (B02).

### 8. RELATED-PARTY PERIMETER

Latest year FY26. INR Lakhs. Source: consolidated Note 15 (Annual_Report_2026.pdf p.146 to p.147), standalone Note 14 (p.117 to p.118) and AOC-2 (p.68).

Quote of the named entity list, line breaks shown as "/": "2. Statutory Body / Zeacloud Services Private Limited (Subsidiary) / Esconet Singapore Pte Ltd ( Foreign Subsidiary) / Abro Intrade LLP (Directors are partner)" (consolidated Note 15, p.146).

| Party | Relationship | Nature | FY26 amount (FY25) |
|---|---|---|---|
| Santosh Kumar Agrawal | MD, promoter | Remuneration; Rent; Incentive | 54.00 (36.00 consolidated, 43.20 standalone); 54.00 (54.00); 33.25 (nil) |
| Sunil Kumar Agrawal | WTD, promoter | Remuneration; Incentive | 54.00 (36.00 consolidated, 43.20 standalone); 33.25 (nil) |
| Vineet Agrawal | WTD, promoter | Remuneration | 7.80 consolidated, 6.00 standalone (6.00 consolidated, 1.80 standalone) |
| Gaurav Gupta | Director in subsidiary | Remuneration; share purchase of Fluidech | 60.00 (60.00); 842.82 (nil) |
| Amit Gupta | Director in subsidiary | Remuneration | 3.00 (2.00) |
| Manoj Chugh Advisory LLP | Firm of independent director | Consultancy fees | 12.00 (nil) |
| Manoj Chugh, Mukesh Chand Jain, Ashi Jain | Independent directors | Sitting fees | 1.96; 1.98; 1.80 |
| Keshav Pareek; Rajnish Pandey | CFO; Company Secretary | Salary | 24.89; 15.77 |
| Zeacloud Services Pvt Ltd | Subsidiary | Sale of goods; Loan given | 568.79 (512.25); 500.00 (nil) |
| Fluidech IT Services Pvt Ltd | Subsidiary | Purchase of services; sale of service to ZeaCloud | 1.80; 22.38 |
| Abro Intrade LLP | "Directors are partner" | No transaction line in either note | none printed |
| Esconet Singapore Pte Ltd | Subsidiary | No transaction line in either note | none printed |

AOC-2 amounts in rupees (p.68): Santosh Kumar Agrawal "Remuneration Paid 54,00,000; Repayment of Loan 1,37,82,094; Rent Paid 54,00,000; Incentive Paid 32,52,559"; Sunil Kumar Agarwal "Remuneration Paid 54,00,000; Repayment of Loan 22,15,865; Incentive Paid 32,52,559"; ZeaCloud "Sale of Goods 5,68,79,011; Loan Given 5,00,00,000"; Fluidech "Purchase of Services 1,80,000".

Comment: Other promoter group holders in the AR26 shareholding table (Anil Kumar Agrawal, Abha Agrawal, Savitri Devi Agrawal, Pooja Gupta, Monita Agrawal, Shubhangi Agrawal, p.109) carry no related-party line. The note incentive of 33.25 each differs from the AOC-2 figure of 32,52,559 rupees each (B02 rank 11). The FY25 column for the same director differs between the standalone and consolidated notes. The loan repayments of 137.82 and 22.16 Lakhs in the FY26 AOC-2 also occurred in FY25 (B02). The Abro Intrade LLP relationship has no object, filing or transaction in the corpus (B08 searches skipped it).

### 9. PLEDGE AND SHAREHOLDING

Promoter and promoter group, as filed. The corpus holds two quarterly patterns and two annual points. The other quarters are NOT DISCLOSED in the corpus (not collected).

| Date | Promoter and group | Source |
|---|---|---|
| Feb 2024, post-IPO | "Post this Issue, our Promoters and Promoter Group will collectively own 6 4.94% of our post issue equity share capital" | PROSP p.35 |
| 31 Mar 2025 | 80,26,196 shares, 61.29% | AR26 p.109 |
| 31 Mar 2026 | 79,42,196 shares, 60.19% (SHP: 7942196, 0.6019) | AR26 p.109; SHP_1650865 extract |
| 30 Jun 2026 | 7942196 shares, 0.6019; locked-in 2472000 (0.3112 of promoter group) | SHP_1693906 extract |
| 19 Sep 2026 (AGM record date) | 78,06,196 promoter shares in the voting table; 59.15% derived on 13,196,238 shares | AGM outcome 2026-09-30 p.6; B08 (derived) |

- Pledge. Quote: "WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged | false" for 31 Mar 2026 and 30 Jun 2026, and the same for non-disposal undertakings and other encumbrance (SHP extracts, lines 6 to 11). The prospectus states "none of the shares held by our Promoters/ Promoter Group are pledged" at its date (PROSP p.72). B08 read the scanned 2026-05-19 Reg 31(4) declaration dated 3 Apr 2026 as a no-encumbrance statement. Pledge history for the quarters between is NOT DISCLOSED in the corpus.
- Institutional holding, latest (30 Jun 2026): "InstitutionsForeignPortfolioInvestorCategoryTwo_ContextI | NumberOfShares | 16000" and 0.0012, which is 0.12% of the shares. No mutual fund, insurer or domestic institution line appears in the extract (SHP_1693906). Public holding 39.81% (5,254,042 shares).
- Comment: Promoter and group fell from 64.94% after the IPO to 59.15% on the record date, about 5.8 points, and the last step, 1,36,000 shares since 30 Jun 2026, is derived from voting data with no counterparty or filing found (B08). The fetch list for the missing quarters is NSE and BSE shareholding patterns for Mar 2024, Jun 2024, Sep 2024, Dec 2024, Mar 2025 (the SHP pattern), Jun 2025, Sep 2025, Dec 2025 and Sep 2026.

### 10. VERIFICATION

Documents quoted in this annex, with dates. All sit under runs/esconet-2026-10-05/inputs/.

| File | Date / period |
|---|---|
| annual-report/Annual_Report_2026.pdf | FY2025-26; Board report and AOC forms dated 12 Aug 2026; balance sheet dated 28 May 2026 |
| annual-report/Annual_Report_2025.pdf | FY2024-25 |
| results/2026-08-12-ESCONET_12082026174006_Outcome_BM_12082026.pdf | Q1 FY27, 12 Aug 2026 |
| results/2026-05-28-ESCONET_28052026185515_Outcome_BM_28052026.pdf | FY26 audited, 28 May 2026 |
| concalls/Concall_Jun_2025_Transcript.pdf | call 19 Jun 2025; cover letter 20 Jun 2025 |
| concalls/Concall_Aug_2026_Transcript.pdf | call 13 Aug 2026; cover letter 17 Aug 2026 |
| presentation/Investor_Presentation_Sep_2025.pdf | Sep 2025 |
| presentation/Investor_Presentation_Jun_2026.pdf | 22 Jun 2026 investor meet |
| prospectus/EsconetTechnologies_PROSP.pdf | dated 20 Feb 2024 |
| announcements/2026-04-29-ESCONET_29042026120311_ESC_INT_Forfiture_29042026.pdf | 29 Apr 2026 |
| announcements/2026-02-09-ESCONET_09022026135228_NSE_Intimation_ZSPL_Reg_30.pdf | 9 Feb 2026 |
| announcements/2026-09-30-ESCONET_30092026132657_Revised_Outcome_14_AGM_ETL_2026.pdf | AGM 25 Sep 2026; outcome filed 30 Sep 2026 |
| shareholding/SHP_1650865_14042026063352_WEB_extract.txt | quarter to 31 Mar 2026 |
| shareholding/SHP_1693906_16072026124525_WEB_extract.txt | quarter to 30 Jun 2026 |
| rating/CRISIL_Esconet_Rating_Rationale_2026-07-02.txt (quoted through B12a) | 2 Jul 2026 |

Other quotes come from stage reports already holding the anchor (B02, B03, B05, B12a, B12b). The B00 manifest records corpus_commit 17a4d6a7 from stage 0. The commit supplied for this stage is below.

CORPUS COMMIT HASH: f2564198362ac19889f2cf6e3aa6371623d52783

```yaml
stage: B09b-dossier
company: "ESCONET"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "FY2023-24 annual report"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "CRISIL rating rationales 2024 and 2025"
    expected_source: "rating agency site"
    kind: "findable-missing"
  - document: "NSE Reg 30 filings before Sep 2025, including 10 Jan 2025 Fluidech acquisition filing and 3 Feb 2025 EGM notice"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Shareholding patterns for the other 10 of the last 12 quarters, and Sep 2026 when filed"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Audited accounts of ZeaCloud, Fluidech and Esconet Singapore; Fluidech acquisition-date balance sheet"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Q1 FY27 balance sheet and cash flow statement (not yet filed; H1 FY27 print due mid Nov 2026)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Q1 FY27 earnings deck shown on the 13 Aug 2026 call"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "SEBI order text on lead manager Corporate Capital Ventures, 18 Aug 2026"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "22 Jun 2026 investor meet transcript (recording only)"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "H1 FY26 call transcript (no call held)"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
  - document: "Broker and research notes (research/ empty)"
    expected_source: "rating agency site"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Core integration and resale (97.61% of FY26 consolidated revenue is product sales)"
    archetype: "Outsourcing partner (CDMO/EMS/IT services)"
  - line: "HexaData own-brand servers, workstations and storage"
    archetype: "Build-to-spec component maker"
transition:
  - line: "Core integration plus HexaData mix shift"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER (two-rung claim; dossier reading of management language)"
    engine: "Own-brand HexaData content share rises against resold boxes (mechanism unproven: stated sub-line margins of 10 to 15 percent cannot produce the 29.16 percent Q1 FY27 standalone gross margin); ZeaCloud MeitY empanelment and Fluidech NCIIPC accreditation convert to revenue"
    proof_gate: "Standalone gross margin at or above 20 percent in Q2 FY27 and Q3 FY27 after stock replaced at current cost, with HexaData revenue and margin disclosed by line; companions: consolidated EBITDA ex other income at or above 5 percent for two straight quarters, and CFO ex-FDR positive with CFO to PAT above 0.7 and receivables over six months below 10 percent"
    recognition_gap: "Open question for Stage 11 via the PE gap: does the TO state already look reflected in market pricing. No number or conclusion here."
    ugliness: "STRUCTURAL-FEATURE"
    transition_falsifier: "Q2 FY27 standalone gross margin back near the FY26 level of 13.7 percent, or no HexaData line disclosure after the Q2 FY27 print"
dominant_variables:
  - "Standalone gross margin after stock replacement (Q1 FY27 29.16 percent vs FY26 13.72 percent)"
  - "HexaData revenue and margin by line, and revenue base ex-Singapore (not disclosed)"
  - "Cash conversion: CFO ex-FDR, inventory build, receivables over six months (FY26 CFO negative; 19.9 percent over six months)"
  - "Credential conversion: ZeaCloud MeitY empanelment and Fluidech break-even (timelines slipping)"
business_falsifier: "An audited Singapore balance sheet or customer list showing thin pass-through trade, a write-down of the unreconciled 2,428.94 Lakhs subsidiary inventory, or a tax or SEBI finding tying pre-IPO placements to promoters"
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 8
  verifiability_ratio: "5 of 8 externally observable"
  single_point_failure: "standalone gross margin reverting to the FY26 level of 13.7 percent"
  fragility_verdict: "FRAGILE"
candidate_count: 7
second_order:
  chains_drafted: 2
  pending_live_links: 4
  confirm_by_observations: 2
research_brief_items: 16
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "f2564198362ac19889f2cf6e3aa6371623d52783"
```
