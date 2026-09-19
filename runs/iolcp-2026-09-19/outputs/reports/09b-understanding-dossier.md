# HALT 1 UNDERSTANDING DOSSIER — IOL Chemicals & Pharmaceuticals Ltd (IOLCP)
Run date 2026-09-19 | Assembled from B00-B09, verifiers B12a-B12d, confidence.yaml,
B13-synthesis-lite. Assembly only. No new research, no valuation, no price, no verdict
vocabulary except the one scoped Part B4 exception named in the prompt.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. Concalls.** Four transcripts held: Q3 FY26 (Concall_Feb_2026_Transcript.pdf, filed
18-Feb-2026), Q4 FY26 (Concall_May_2026_Transcript.pdf, filed 28-May-2026), Q1 FY27
(Concall_Aug_2026_Transcript.pdf, filed 20-Aug-2026), and a business-update call on
capex, 11-Sep-2026 (Concall_Sep_2026_Transcript.pdf, filed 17-Sep-2026, not a quarterly
call) (B00). Most recent quarter covered: Q1 FY27 (Jun-2026 quarter), plus the
Sep-2026 business update as a fourth, non-quarterly data point. Q2 FY27 (Jul-Sep 2026)
results are not yet due at the 2026-09-19 run date (companies typically file ~45 days
after quarter end, so due around mid-Nov-2026); no more-recent quarterly transcript is
plausibly missing yet. Backward gap: Q2 FY26 (Nov-2025) results and its concall
transcript were not collected, outside the collector's 3-most-recent-quarter rule (B00
input_gaps).

**2. Annual reports.** FY26 (Annual_Report_2026.pdf, filed 07-Aug-2026, primary) and
FY25 (Annual_Report_2025.pdf, filed 31-Jul-2025, backward-baseline support) are held
(B00). The latest completed FY (FY26) is present. Only 2 years are held, not 3 or more.

**3. Results filings.** Latest quarterly filing: Q1 FY27 (20260810-Q1FY27-results.pdf,
10-Aug-2026). Q4 FY26 audited results (20260520-Q4FY26-audited-results.pdf, mostly
scanned/OCR) and Q3 FY26 (20260211-Q3FY26-results.pdf) are also held. No quarter-gap
between the latest results filing (Q1 FY27) and the latest AR (FY26, filed 07-Aug-2026,
five days before the Q1 FY27 print): the AR covers the FY that closed just before the
latest results quarter. The Q2 FY26 results gap named in Item 1 is the one quarter
missing from the run of quarterly filings.

**4. Investor presentations.** Latest held: Investor_Presentation_1.pdf, Q1 FY27 (filed
around 12-Aug-2026, per B09 stale_data check). Q4 FY26 (20260521) and Q3 FY26
(20260212) decks are also held.

**5. Research / rating.** No broker note or independent research report is held
(B00: "research: absent (no broker notes collected)"). Rating: a Reg 30 intimation of
the CARE reaffirmation letter dated 30-Jun-2026 is held (bulletin only, no rationale
text), plus the prior full rationale dated 04-Jul-2025. The Jun-2026 rationale text
itself is ABSENT — see Item 7.

**6. Corporate actions.** 34 of 105 BSE filings over 12 months kept after excluding
routine ads, trading-window notices, KYC and Reg 74(5) filings: 8 SAST 29(2)
disclosures, the Reg 30 capex intimation of 09-Sep-2026, the customs Order-In-Original
disclosure (09-May-2026), CEP/NMPA approval announcements, the 39th AGM voting-results
filing (02-Sep-2026), and WOS incorporation/strike-off notices, spanning Sep-2025 to
Sep-2026 (B00).

**7. Freshness pair check.** Per B00 `freshness_pairs`:
- results_to_concall: PASS (Q1 FY27 results paired with the Aug-2026 Q1 FY27 call).
- rating_bulletin_to_rationale: **FAIL**. Trigger document held: the Reg 30 intimation
  of the CARE reaffirmation letter dated 30-Jun-2026. Missing mate: the CARE Ratings
  rationale/press release for that same reaffirmation (careratings.com, expected
  Jun/Jul 2026). Only the 04-Jul-2025 rationale is held, one cycle old.
- sebi_order_to_text: PASS (no SEBI order referenced beyond the standard
  director-debarment certificate; not applicable).
- ar_to_latest_audited_annual: PASS (AR FY26 pairs with the FY26 audited results).

**8. VERDICT LINE: CORPUS GAPPED-FRESHNESS.**
Missing mate document (named first, per the rule): CARE Ratings rationale for IOL
Chemicals and Pharmaceuticals Limited, reaffirmation letter dated 30-Jun-2026
(careratings.com press release, Jun/Jul 2026 expected). This failed pair caps the
phase-1 gate recommendation at PROCEED WITH CAVEATS (B13/gate-recommendation.md) and is
never softened to plain CORPUS GAPPED.

Other gaps, listed under this verdict:
- Q2 FY26 results and its Nov-2025 concall transcript — findable-but-missing, expected
  source BSE (outside the collector's 3-most-recent rule).
- MCA beneficial-ownership filings for Vasudeva Commercials Limited and G Consultants
  and Fabricators Pvt Ltd before their Oct-2025/Jun-2026 corporate actions — findable-
  but-missing, expected source MCA (B08 input_gaps).
- Molecule-level global market size for 9 of IOLCP's 11 named molecules — findable-but-
  missing, expected source industry market-research databases (B09 input_gaps).
- Inter-segment transfer-pricing basis for the Rs 237.72 Cr chemicals-to-pharma
  captive transfer — NOT FOUND IN DOCUMENT; not a collection gap, the company has not
  disclosed this basis anywhere in the AR (B02/B03/B04). Plausibly-nonexistent as a
  disclosed item; itself a data point on disclosure depth.
- Independent broker/analyst research on IOLCP — none found; plausibly-nonexistent
  (small-cap with thin sell-side coverage), itself a data point, not a document to chase.
- CDMO and specialty-chemicals-tolling counterparty identity and contract terms — NOT
  DISCLOSED by the company under a stated confidentiality clause (Reg 30, 09-Sep-2026,
  Annexure-2 item 7); plausibly will not become public before the customer chooses to
  disclose or a Reg 30 filing names them.
- Segment-level capital employed / segment borrowings — NOT FOUND IN DOCUMENT; only
  segment assets and liabilities are disclosed (Note 39), no segment-level ROCE
  possible (B04).

Empty folders confirmed at intake and repeated here per the task instruction: `research`
(empty) and `other` (empty); suppressed as a pause point by the /step1 autonomy
contract, standing answer "proceed with the gaps" (B00).

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT — PENDING OPERATOR SIGN-OFF.** This declaration is not signed. Signing happens
only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE

**A1. Archetype.**
- Pharma/API line (60.2% of FY26 revenue, Note 39 via B04): **Commodity converter**
  (Section 1B Amendment 17 territory). Pricing power is scored weak company-wide (B04);
  Ibuprofen alone, still priced off a global cost curve the company does not set, is
  ~37.9% of FY26 revenue on its own (B04 revenue_streams). The regulatory filing base
  (14 US DMFs, 21 EDQM CEPs) gives a secondary licence/scarcity trait that softens but
  does not replace the converter core.
- Chemicals line (39.8% of FY26 revenue): **Commodity converter**, explicitly.
  Amendment 17 binds this slice: margin swings on spread and utilisation, not price the
  company sets (B04, B00 sector_cap_row_evidence).

**A2. The simple analogy.** IOL cooks its own base sauces (acetic-acid family
chemicals), then uses most of that sauce to cook its main dish, bulk ibuprofen powder,
which it sells to drug companies worldwide. It sells extra sauce to outside buyers such
as paint and ink makers. Because it makes its own sauce, its dish costs less than a
rival who buys sauce elsewhere. But its two biggest items, ibuprofen and one type of
sauce (ethyl acetate), sell at world prices it cannot set, so profit tracks global
chemical prices more than its own selling skill (B04 Section 1E, paraphrased).

### PART B — THE TRANSITION

**B1. From-to (Pharma/API line only).** FROM **R2 COST-ADVANTAGED CONVERTER**
(backward-integration cost advantage; company-wide ROCE 9.70% FY26, Note 49, sits well
below the R2 mid-teens neighbourhood, but the Pharma segment result margin alone is
12.3% FY26, Note 39, the stronger of the two segments) TO **R3 VALUE-ADDED / SPEC'D
SUPPLIER** (partial pricing power from a diversifying molecule basket plus two new
spec'd, anchor-customer-dependent lines). The Chemicals line makes no transition claim
this run: it stays a converter, Amendment 17 binds it, R1/R2 neighbourhood.

**B2. The engine.** Two things physically change: (1) the pharma revenue mix shifts
away from ibuprofen toward a diversified API basket, non-ibuprofen share of pharma
revenue 36% (Q1 FY26) to 43% (Q1 FY27), +67% YoY (B00 LBF1; B05); (2) two new
pre-commercial lines add spec'd, contract-based revenue with named-but-undisclosed
anchor customers: a 1,500 million-tablet/year EU-GMP CDMO formulations plant (Rs 110 Cr)
and a single-customer specialty-chemicals tolling unit (Rs 35 Cr), both targeted
commercial in Q3 FY27 (B04, B05, Reg 30 09-Sep-2026).

**B3. The proof gate.** Quarter by quarter: non-ibuprofen share of pharma revenue
continuing to rise past 43% while margin stays at parity with ibuprofen at the product
level (B05 trigger 1 confirm_signal — margin parity is currently a company claim, not
independently confirmed); AND first commercial revenue disclosed from the CDMO and
tolling lines on or before Q3 FY27 (B04, B05, B07 catalysts_12m). Until both fire
together, the transition is narrative.

**B4. The recognition gap (open question, resolved at Stage 11).** Whether the TO state
(a diversified, partly spec'd API and CDMO supplier) already sits in the market's
pricing is an open question this dossier does not answer. The step-1 business brief
(weighed, not anchored) notes a trailing PE of 33.8x against a company-disclosed ROCE of
9.70% (Note 49) and a stock that rose roughly 170% in four months to Jul-2026 — a
combination that could mean the market has already moved ahead of the transition, or
that it is pricing the diversified TO state on forward earnings rather than trailing
ones. Stage 11 resolves this via the destination-PE gap; no number, no conclusion is
stated here.

**B5. The ugliness test.** UNRESOLVED at Halt 1, and stated as such rather than forced
into one class. Two candidate ugly optics exist and the corpus itself could not settle
their reading (B13 FLAG-CASH, determination INDETERMINATE):
- Rising debtor days (78.5 FY22 to 94.9 FY26, B01/screener) and gross receivables
  outrunning revenue (+17.7% vs +11.5% FY26, Note 10 p.152) could read
  ARTIFACT-OF-CLIMB (a heavy Q4 FY26 revenue quarter, +17.4% YoY, inflating year-end
  receivables; overdue-past-six-months share held flat at 1.6-1.7%, B02) or
  STRUCTURAL-FEATURE (payable days fell from ~100 to ~89 the same year IOL collected
  slower, loss-allowance coverage rose 0.51% to 0.76%, a five-year not a one-quarter
  pattern, B02/B03).
- Low absolute ROCE (9.70% FY26, Note 49) against a 25% CAGR-supporting return-profile
  requirement could read ARTIFACT-OF-CLIMB (new capacity, Paracetamol Unit-11 and the
  Rs 495 Cr dated tranche, not yet earning full-run-rate returns) or STRUCTURAL-FEATURE
  (a four-of-five-year sub-15% ROCE band, B01 Block A deal-breaker, following a
  FY19-FY21 pricing-supercycle peak that itself was not repeatable).
The missing evidence that would resolve this reading is the 30-Jun-2026 CARE rationale
(Section 1 Item 8) and the 30-Sep-2026 half-year balance sheet (B13's own falsification
metric names this).

**B6. The transition falsifier.** Non-ibuprofen share of pharma revenue plateaus or
reverses below 37% (the FY26 level), OR the margin-parity claim stays unconfirmed at
product level while the mix keeps shifting (B05 trigger 1 kill_signal); OR both new
pre-commercial lines slip past Q3 FY27 with anchor customers still described only as
"being finalized" rather than named (B07 optionality_register; B12c EM-2).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables.**
1. Non-ibuprofen share of pharma revenue (currently 43%, Q1 FY27; B05) — the mix engine
   itself.
2. CDMO/tolling first commercial revenue and named anchor customers (currently zero
   revenue, customers undisclosed; B04, Reg 30 Annexure-2 item 7) — the proof gate's
   second leg.
3. Debtor days / working-capital trend (78.5 to 94.9, B01) — the variable that decides
   the B5 ugliness classification.
4. Capex commissioning dates: the Rs 495 Cr dated tranche (ibuprofen +6,000 MTPA by
   Dec-2027, CDMO Q3 FY27, tolling Q3 FY27, Reg 30 09-Sep-2026) and the undated Rs
   1,200-1,400 Cr greenfield, still without a firm date across four consecutive call
   touchpoints (B05 FLAG-CAPEX).

**C2. What the model rejects.** Market-size questions. The realistic addressable
market (B09 SAM Rs 15,200 Cr) grows only ~5%/year and IOL already holds an estimated
15.3% of it; the binding constraint on the bull case is execution (mix delivery, new-line
commercialisation, working-capital discipline), not market size. Management's own
headline market slides (global API market cited at 153.5x the company-specific
estimate, B09 FLAG-MGMT-TAM-BROAD; two Indian specialty-chemicals market figures filed
five days apart differing by more than 2x, B09 FLAG-TAM-SOURCE-INCONSISTENCY) are
explicitly named as noise the model does not weight.

**C3. The business falsifier.** The Ibuprofen and Ethyl Acetate core (~72% of FY25
revenue, CARE rationale p.2, cited via B04) prints segment results below a
cost-of-capital return for two or more consecutive quarters with no mix offset visible
in the pharma segment result margin — evidence the FROM business itself (the commodity
core funding the whole diversification programme) is impaired, not merely that the
transition has stalled. Distinct from B6: B6 kills the arrow (the climb), C3 kills the
platform the climb is launched from.

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Drafted per the five-question spec at prompts/13-synthesis-pipeline.md (products and why
they matter; who the customers are; why demand exists; why demand grows; where the
competitive advantage sits per line). This is the same text already assembled at Stage
13-lite from B01-B09 (outputs/final/business-narrative.md); Stage 13's copy remains the
final, updatable version.

IOL makes bulk drug ingredients and industrial acetyl chemicals at one integrated site
in Barnala, Punjab. Ibuprofen, the painkiller molecule, is about 38% of sales, and IOL
runs a 12,000 tonne a year ibuprofen plant at about 95% utilisation, the largest single
ibuprofen line in the world. A basket of other APIs is about 22% of sales: paracetamol,
metformin, clopidogrel, pantoprazole and others, the active powders a generic drug maker
presses into tablets. Acetyl chemicals sold to outside buyers, mainly ethyl acetate and
acetic anhydride, are about 40% of sales and go into paints, inks, packaging, textiles,
food processing and drug making. The same chemical plant makes the intermediates that
feed IOL's own ibuprofen line, a captive transfer of Rs 238 Cr in FY26, so IOL makes in
house what a rival without that plant must buy.

The API buyers are generic formulators in more than 80 countries, and exports were 24%
of FY26 sales. A formulator names its API supplier's drug master file in its own product
filing, and IOL holds 14 US DMFs and 21 European CEPs, so a switch forces the buyer to
requalify; the run found no disclosure of how concentrated the top customers are. The
chemical buyers are industrial users who buy on price.

Demand today is generic drug volume, which the run will track through European and
global generic formulator offtake volumes and through the capacity status of the other
large ibuprofen makers, Solara Active Pharma, Shandong Xinhua and BASF. Input supply
matters as much as demand: most chemical feedstock comes from China, and metformin's key
input DCDA has no Indian supplier, so China DCDA export prices and the acetyl spread are
live signals.

Growth should come from three named steps: more non-ibuprofen APIs filling the new
paracetamol unit, a 1,500 million tablet contract manufacturing plant for European
anchor customers, and a tolling unit for one global chemical company, the last two due
in Q3 FY27. Each step has an outside check: USFDA DMF and EDQM CEP grants, the
paracetamol global spot price index, PLI bulk drug scheme disbursement, and the naming
of the CDMO European anchor customers. The market for this product basket grows about
5% a year, so IOL's growth must come from share and from new lines, not from the market.

The API line has a real but moderate advantage: backward integration and a large
regulatory filing base, which the emerging moat scan rates as a documented rare
manufacturing capability and documented process innovation. The acetyl chemicals line
has no moat; it is a converter that earns the spread between feedstock and product
price. The two new lines rest on partnerships and an ESG base that supports European
access, but both depend on unnamed customers, and the scan scored zero on talent
asymmetry and zero on cannibalisation barrier, so no rival would have to break its own
business to copy IOL.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 C1)

**Vertical 1 — Non-ibuprofen mix shift.** The corpus establishes the mix rose from 36%
(Q1 FY26) to 43% (Q1 FY27) of pharma revenue, +67% YoY (B00 LBF1, B05), that Paracetamol
Unit-11 (10,800 MTPA) is the swing asset, and that management targets 50-55% by FY29
with claimed margin parity to ibuprofen (B05 guidance table). The corpus cannot
establish product-level margin by molecule (B04 unit_economics: revenue/margin per unit
NOT FOUND), so the margin-parity claim is unverified at the product level, and it cannot
resolve a direct print conflict: the Q1 FY27 press release states paracetamol
utilisation at 65% while the Q1 FY27 call states about 55% (gate-recommendation.md gaps
table). Questions to decide it: (1) which of 65% or 55% utilisation was true for Q1
FY27, and does management reconcile the two prints; (2) does the margin-parity claim
hold at the product level once paracetamol crosses 60% utilisation; (3) does the mix
keep rising past 43% in Q2/Q3 FY27 without a stall.

**Vertical 2 — CDMO/tolling commercialisation.** The corpus establishes the capex
(Rs 110 Cr CDMO tablet plant, Rs 35 Cr tolling unit), the EU-GMP Hungarian certification,
the Q3 FY27 commercial target, and the exact rupee match between the Sep-2026 call and
the Reg 30 filing (B05 promise_delivery). It cannot establish customer identity, volume,
tenor, or cancellation terms — confidential by the company's own admission (Reg 30
Annexure-2 item 7) — and B12c (EM-2) found the underlying anchor-customer relationship
graded at the strongest evidence tier (DOCUMENTED, HH 1.0) is itself only a management
claim ("contracts being finalized"), not a filed contract. Questions to decide it: (1)
are any anchor customers named before Q3 FY27; (2) does first commercial revenue book on
schedule; (3) what share of each facility's capacity is contracted versus speculative.

**Vertical 3 — Working capital / debtor days.** The corpus establishes the trend
(78.5 to 94.9 days, receivables +17.7% vs revenue +11.5%, payable days falling, B01/B02)
and both competing readings (Section 2 B5), but cannot resolve which reading holds: the
30-Jun-2026 CARE rationale that would carry the rating agency's own working-capital view
is the missing freshness-pair document (Section 1 Item 8), and no top-customer
concentration data exists to test whether the receivables build sits with a few large,
low-risk buyers or is broad-based (B02/B05 input_gaps). Questions to decide it: (1) does
the 30-Sep-2026 half-year balance sheet show debtor days above or at/below 95 (B13's own
falsification metric); (2) does the CARE rationale, once obtained, characterise the
trend as a normal growth pattern or a liquidity concern; (3) is any term facility drawn
against the capex programme.

**Vertical 4 — Capex commissioning timeline.** The corpus establishes the dated Rs 495
Cr tranche (ibuprofen +6,000 MTPA by Dec-2027, Reg 30 09-Sep-2026) and that the
Rs 1,200-1,400 Cr greenfield has produced no firm commissioning date across four
consecutive call touchpoints (Feb, May, Aug, Sep 2026, B05 FLAG-CAPEX), with booked
capital commitments of only Rs 69.35 Cr against the combined guided scale (Note 35B
p.161, B02/B03). It cannot establish a funding mechanism beyond the phrase "internally
funded" (zero term debt, Note 42, B02/B03) or a product mix for the greenfield site.
Questions to decide it: (1) does the greenfield get a firm commissioning date at the
next touchpoint (the fifth, per B07's own kill-signal framing); (2) does capital
commitments in the next AR rise materially above Rs 69.35 Cr; (3) does any term-loan
sanction appear in BSE filings.

### 4b. Candidate signal table (expanded from B09 Section 6)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| European/global generic formulator offtake volumes (Ibuprofen, non-Ibuprofen APIs) | Offtake volumes flat or falling while IOL reports mix-shift revenue growth | Monthly | Trade/customs export-shipment data (Volza/Zauba-type records) |
| Ibuprofen competitor capacity status (Solara Active Pharma, Shandong Xinhua, BASF) | A competitor capacity restart or new entrant contradicts IOL's "surviving low-cost producer" framing | Event-driven | Competitor investor filings / press releases |
| Paracetamol global spot price index | Spot price falling while IOL claims a price-led (not mix-led) paracetamol gain | Monthly | ChemAnalyst / ICIS price index |
| China DCDA export/price data (Metformin key starting material) | A disclosed Indian DCDA alternative supplier emerges, removing the single-source risk | Monthly | China customs export data / ICIS China chemical reports |
| Acetyl spread (Ethyl Acetate/Acetic Anhydride vs Acetic Acid) | Spread narrows sharply while IOL's chemicals segment result keeps rising, implying volume/utilisation not spread is doing the work (or the reverse) | Monthly | ChemAnalyst / ICIS spread index |
| USFDA DMF / EDQM CEP filing status (Paracetamol, Pantoprazole, Metformin — Under Review) | A filing is withdrawn or rejected rather than granted | Event-driven | USFDA DMF database / EDQM CEP database |
| PLI bulk-drug scheme disbursement and molecule list | Disbursement stalls or IOL's molecules are not on the funded list | Quarterly | Dept of Pharmaceuticals PLI dashboard / PIB press releases |
| CDMO European anchor-customer identity and contract terms | No customer named by Q3 FY27, or a named customer's own filings show no matching capex/sourcing commitment | Event-driven | Reg 30 filings / next AR related-party or customer note |

candidate_count: 8 (all carried from B09 Section 6, none newly invented).

### 4c. Fragility read

- **variable_count: 7.** (1) non-ibuprofen mix keeps rising with margin parity; (2)
  CDMO/tolling anchor customers convert from "being finalized" to firm contracts and
  commercialise on time; (3) paracetamol utilisation clears 60% (with the 55%/65% print
  conflict resolved); (4) the Rs 1,200-1,400 Cr greenfield gets a firm date and funding
  without a term loan; (5) the working-capital trend resolves GROWTH-INDUCED rather than
  STRUCTURAL; (6) the Ibuprofen/acetyl pricing cycle stays favourable (peer transcripts
  already show one contradiction on paracetamol pricing, B06 FLAG-PRICING); (7) promoter-
  group consolidation (48.19% to 62.28%) does not further compress free float or minority
  standing in a way that triggers renewed institutional dissent (39th AGM: 91.34%
  institutional vote against a director reappointment, B08).
- **verifiability_ratio: 4 of 7 externally observable** (paracetamol utilisation,
  debtor days, capex commissioning dates, and Ibuprofen/acetyl pricing are all
  independently checkable against filings, peer transcripts, or price indices); **3
  company-narrated only** (CDMO/tolling customer identity and contract terms, kept
  confidential by the company itself; the margin-parity claim at product level; the
  rationale behind promoter-group consolidation, on which the company has never been
  asked and never volunteered, B05 FLAG-GOVERNANCE).
- **single_point_failure:** the CDMO and tolling anchor-customer relationships. B07
  found three of five active moat categories (C1 customer ecosystem, H2 strategic
  partnerships, H3 ESG moat) all trace to the same unconfirmed, unnamed European/global
  customer relationships; one conversion failure collapses the scan's strongest findings
  together, not independently (B07 top_moat_risks, flag FLAG-CONCENTRATION).
- **fragility_verdict: FRAGILE.** Seven variables is above a robust count, three of
  seven are verifiable only through company narration (not external filings), and a
  single named point (anchor-customer conversion) can break three of the five moat
  categories the emerging-moat scan currently credits at STRENGTHENING-adjacent tiers
  before the B12c correction (see 4e and Section 5 point 12 on the corrected MODEST
  score).

### 4d. Research brief (claude.ai live-web work order)

1. Obtain the CARE Ratings rationale for the 30-Jun-2026 reaffirmation
   (careratings.com press release, Jun/Jul 2026) and extract its working-capital and
   liquidity paragraphs — the single document that resolves FLAG-CASH and lifts the
   freshness cap. [from Section 4e Chain 2 PENDING LIVE VERIFICATION]
2. Search for the identity, financial health, and purchasing rationale of the CDMO
   "Anchor Customers" (European) and the specialty-chemicals tolling customer: EU-GMP
   contract-manufacturing tender records, the Hungarian GMP certificate registry for the
   named facility, and any counterparty press mentioning an Indian tablet-supply win in
   H2 2026. [from Section 4e Chain 1 PENDING LIVE VERIFICATION]
3. Pull MCA beneficial-ownership filings for Vasudeva Commercials Limited and G
   Consultants and Fabricators Pvt Ltd before their Oct-2025/Jun-2026 corporate actions,
   to close the one residual gap in B08's otherwise fully-traced promoter-consolidation
   chain.
4. Search for proxy-advisory (IiAS, SES, InGovern) commentary or any company statement
   explaining the 91.34% institutional vote against Kushal Kumar Rana's re-appointment
   at the 39th AGM (2-Sep-2026).
5. Verify against Aarti Drugs', Granules' and Laxmi Organic's live filings whether the
   Q4 FY26 paracetamol-pricing contradiction (B06 FLAG-PRICING: IOL claims a price
   increase, Granules states "no price increases... price erosion") persists into more
   recent quarters.
6. Verify the acetyl spread (ethyl acetate/acetic anhydride) trajectory against live
   ChemAnalyst/ICIS data, given Laxmi Organic's Aug-2026 transcript describes the spread
   as still above its 12-year average with a fresh "West Asia 2.0" disruption (B06
   FLAG-SPREAD), a live signal this static corpus cannot update.
7. Check for Q2 FY26 results and its Nov-2025 concall transcript on BSE, to close the
   one backward gap in the quarterly chronology.
8. Run the 9 remaining molecule-specific global-market-size searches (Metformin,
   Clopidogrel, Pantoprazole, Fenofibrate, Levetiracetam, Lamotrigine, Losartan,
   Minoxidil, Sitagliptin) that B09 skipped for effort budget, to complete the
   bottom-up TAM triangulation beyond Ibuprofen and Paracetamol.
9. Search for any term-loan sanction or bank facility announcement tied to the
   Rs 1,200-1,400 Cr greenfield, and for capital-commitments disclosure beyond
   Rs 69.35 Cr in any interim filing.
10. Resolve the Q1 FY27 paracetamol utilisation print conflict directly with the
    company or via the next call transcript: 65% (press release) versus ~55% (call).

research_brief_items: 10.

### 4e. Second-order stub (Master Prompt v3.7, Rule F — floor of 5, this stub carries 2)

```
CHAIN 1: Non-ibuprofen mix shift and CDMO/tolling entry converts the transition engine
[trigger: non-ibuprofen share of pharma revenue 36% (Q1 FY26) to 43% (Q1 FY27), +67%
YoY, B00 LBF1; B05]
Link 1 [DOCUMENTED]: Paracetamol Unit-11 (10,800 MTPA) is the swing asset; utilisation
  reported at 55% (Q1 FY27 call) or 65% (Q1 FY27 press release), a source conflict the
  corpus does not resolve (B04; gate-recommendation.md gaps table).
Link 2 [DOCUMENTED]: The Rs 110 Cr CDMO tablet plant (1,500mn tablets/yr, EU-GMP
  Hungary-certified) and the Rs 35 Cr specialty-chemicals tolling unit are dated and
  itemised in the Reg 30 filing of 09-Sep-2026, both targeted commercial Q3 FY27, both
  funded from the internally-accrued Rs 495 Cr tranche (B04, B05).
Link 3 [INFERENCE]: If both new lines commercialise on schedule and paracetamol
  utilisation clears 60%, the non-ibuprofen share should continue past 43% toward
  management's 50-55% FY29 target, converting a spot mix-shift into a structural
  margin-mix driver. This inference rests on the anchor-customer relationships actually
  converting from "being finalized" language (B12c EM-2 finding) to signed, disclosed
  contracts, which the corpus cannot verify either way.
Binding constraint: physical capacity is already built (Paracetamol Unit-11 10,800
  MTPA; CDMO plant 1,500mn tablets/yr) and financed inside the dated Rs 495 Cr tranche,
  not awaiting fresh capital (B04/B05).
Unsaid: the AR discloses zero customer names and zero contracted volume/tenor for the
  CDMO and tolling lines (Reg 30 Annexure-2 item 7, confidentiality clause). Separately,
  the R&D and new-product pipeline went unanswered across three consecutive quarterly
  calls (Feb, May, Aug 2026), a repeated evasion B12b rates CRITICAL and the maker stage
  (B05) missed entirely.
Who pays, and why now [PENDING LIVE VERIFICATION]: the identity, financial health, and
  purchasing rationale of the European CDMO "Anchor Customers" and the single specialty-
  chemicals tolling customer cannot be established from this corpus. Claude web should
  search EU-GMP contract-manufacturing tender records and press coverage for an Indian
  tablet-supply win in H2 2026, and check the Hungarian GMP certificate registry entry
  for the named facility.
Observation that confirms or breaks this chain, and confirm-by date: first disclosed
  commercial revenue line item from the CDMO or tolling line in the Q3 FY27 results, or
  a Reg 30 filing naming a customer before then. Confirm-by: 15-Feb-2027 (approximate
  Q3 FY27 results filing window).

CHAIN 2: The "internally funded" capex claim against a rising working-capital drag
[trigger: debtor days 78.5 (FY22) to 94.9 (FY26), gross trade receivables +17.7% YoY vs
revenue +11.5%, B01/B02; capex programme Rs 495 Cr dated plus Rs 1,200-1,400 Cr
undated, both called "internally funded," B00 LBF3]
Link 1 [DOCUMENTED]: FY26 free cash flow was only Rs 43.52 Cr after working capital
  absorbed Rs 73.34 Cr of cash, even though CFO/PAT (1.56x) and CFO/EBITDA (73.9%) both
  read healthy (B03; AR Cash Flow Statement p.136).
Link 2 [DOCUMENTED]: Zero term debt exists, gearing is N.A., and booked capital
  commitments are only Rs 69.35 Cr, under 14% of even the smaller guided tranche (Note
  35B p.161, Note 42 p.174-175, B02/B03).
Link 3 [INFERENCE]: If debtor days keep rising while capex commitments accelerate
  toward the guided Rs 495 Cr plus Rs 1,200-1,400 Cr scale, the "internally funded"
  claim will need either a term-loan draw (not yet disclosed anywhere in this corpus) or
  a working-capital release (a debtor/payable-days reversal), neither of which the
  corpus evidences today. The claim currently rests on FY26 FCF continuing to improve, a
  single year's trend, not a proven multi-year funding mechanism.
Binding constraint: FY26 FCF of Rs 43.52 Cr is the only internal-accrual evidence on
  record against a combined Rs 1,700-1,900 Cr programme; the corpus shows no committed
  external credit facility of any kind.
Unsaid: the Chairman's Message, MD's Message and Investment Case narrate the capex
  programme across the AR with zero rupee figure anywhere in that prose (B03
  FLAG-CAPEX); Note 35B's Rs 69.35 Cr commitment sits far below even the guided Rs 495
  Cr specific-project set, let alone the greenfield.
Who pays, and why now [PENDING LIVE VERIFICATION]: whether any bank has sanctioned or is
  in discussion for a term facility for the Rs 1,200-1,400 Cr greenfield, and whether
  the 30-Jun-2026 CARE rationale (the missing freshness-pair document, Section 1 Item 8)
  carries a funding-plan or liquidity view this corpus cannot see. Claude web should
  pull the CARE Ratings press release (careratings.com, Jun/Jul 2026) and check BSE for
  any subsequent term-loan sanction filing.
Observation that confirms or breaks this chain, and confirm-by date: debtor days on the
  30-Sep-2026 half-year balance sheet (Q2 FY27 results, BSE). Above 95 days with trade
  receivables again outgrowing half-year revenue reads STRUCTURAL (per B13's own
  falsification metric); at or below 95 days with revenue still growing reads
  GROWTH-INDUCED. Confirm-by: Q2 FY27 results filing, due mid-Nov-2026.
```

Stub carries 2 of the Rule F floor of 5. Chains 3 to 5 are built in claude.ai with live
web, before Role 2.

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. IOL makes bulk drug ingredients (APIs) and industrial acetyl chemicals at one site in
   Barnala, Punjab, and sells both worldwide.
2. Ibuprofen is its single biggest product: about 38% of FY26 revenue, made at the
   world's largest single ibuprofen plant, running near full capacity.
3. A second product, ethyl acetate (an industrial solvent), plus ibuprofen together made
   up about 72% of FY25 revenue, and both sell at world prices IOL does not set.
4. Buyers of the API basket are generic drug makers in more than 80 countries; a buyer
   that names IOL's regulatory filing in its own drug application faces real switching
   cost if it wants to change supplier.
5. Buyers of the plain industrial chemicals are paint, ink, textile and food-processing
   companies who mostly buy on price, not on switching cost.
6. Demand for the core business grows with global generic-drug volume, a slow and steady
   driver, not a fast one; the total addressable market grows only about 5% a year.
7. Growth beyond that slow core is meant to come from three new steps: a bigger share of
   non-ibuprofen APIs (up from 36% to 43% of pharma revenue in one year), a new
   contract-manufacturing tablet plant for named-but-undisclosed European customers, and
   a tolling deal with one undisclosed global chemical company.
8. The company's edge on APIs is real but moderate: it makes its own key chemical
   inputs in-house, which lowers cost, and it holds a large base of regulatory filings,
   which raises the cost for a customer to switch suppliers.
9. The plain chemicals business has no such edge; it earns the gap between feedstock
   cost and product price, a gap that widens and narrows with the market, not with
   anything IOL controls.
10. The whole growth story rests on a mental model still in draft: a shift from a
    commodity price-taker core to a partly spec'd, partly contract-based supplier, proven
    only if the mix keeps shifting with held margin and the two new lines start booking
    revenue on schedule.
11. That model is fragile by this dossier's own count: seven variables must go right,
    three of them can only be checked through what the company itself says, not through
    an outside filing, and one single point, the unnamed anchor customers behind the two
    new lines, can break three of the moat scan's five strongest findings at once.
12. The corpus itself found reasons for caution alongside the growth story: debtor days
    rose from 79 to 95 over five years even as the company calls its Rs 495 Cr plus
    Rs 1,200-1,400 Cr capex plan "internally funded" with zero term debt; a verifier
    corrected the emerging-moat score down from 26.3 (STRENGTHENING) to 23.4 (MODEST)
    once a scoring rule was applied correctly.
13. Promoter and promoter-group ownership rose from about 48% to about 62% in under two
    years, mostly through a traced merger of two entities that were public shareholders
    before the merger; the deal is filed and real, but who controlled those entities
    beforehand is not found anywhere in this corpus or the open web.
14. The corpus could not establish who IOL's top customers are, what price it charges
    per tonne for any single product, or the pricing basis for a Rs 238 Cr internal
    transfer between its two segments.
15. The two biggest open questions carried to Halt 1 are: does the rising receivables
    trend settle as ordinary growth or as a lasting cash squeeze, and do the two new,
    single-customer business lines convert from management narration into named,
    revenue-booking contracts by the third quarter of next fiscal year.

---

## SECTION 6: STANDING EXTRACTION ANNEX

Answered from corpus, quote-then-comment, for every question. Corpus commit hash and
filename/date verification are recorded in Question 10.

### 1. UNITS

Quote (Investor_Presentation_1.pdf, Q1 FY27, p.11 per page marker): "Diversified API
platform with 30,726 MTPA capacity". Quote (same deck, p.9-10 per page markers): "Ethyl
Acetate capacity increased to 1,20,000 MTPA", "Acetic Anhydride capacity increased to
32,000 MTPA", "Installed Triacetin Capacity of 6000 MTPA".
Comment: no blended per-unit (Rs/tonne or Rs/kg) realisation is printed anywhere in the
AR or Investor Presentation for any product (B04 unit_economics). These figures cover a
basket of different molecules and chemicals at very different price points, not one
product. In place of a per-unit figure, the volume line (30,726 MTPA API capacity,
1,82,400 MTPA specialty-chemicals capacity, IP p.11/9) and the revenue line (FY26 total
revenue Rs 2,319.06 Cr, B01) are the two lines from which one could be derived, but the
AR gives no product-level revenue split fine enough to isolate a single molecule's
realisation (product-level revenue NOT FOUND, B04).

### 2. SEGMENT CAPITAL AND DEBT

Quote (AR FY26 Note 39, Segment Information, p.168, standalone; figures as reported in
02-notes-pass2.md, primary-source read): Segment assets — Chemical Rs 534.85 Cr (FY25)
to Rs 578.66 Cr (FY26), +8.2%; Pharmaceutical Rs 1,381.71 Cr (FY25) to (FY26 figure per
same note). Segment liabilities — Chemical Rs 300.16 Cr to Rs 297.72 Cr (flat/down);
Pharmaceutical Rs 194.88 Cr to Rs 196.60 Cr (flat); Unallocated liabilities Rs 82.29 Cr
to Rs 162.02 Cr, +96.9%, not itemised in the note itself (B02/B03).
Comment: borrowings are NOT allocated by segment in Note 39; the company-wide position
is that term borrowings are effectively zero (debt-equity 0.08x, gearing ratio N.A.,
Note 42 p.174-175, as reported by B02/B03, not independently re-quoted verbatim this
pass). Note 39 discloses only segment assets and liabilities, not segment capital
employed, so a true segment-level ROCE or segment-level capital-employed figure is NOT
FOUND IN DOCUMENT (B04). Capital commitments (Note 35B, p.161) are company-wide, not
segment-split: Rs 25.42 Cr (FY25) to Rs 69.35 Cr (FY26), +172.8%.

### 3. GUIDANCE VERSUS ASPIRATION

All items sourced from B05's guidance table (concall transcripts, quote-then-comment as
extracted by the maker stage; this pass reuses the anchored table rather than re-reading):

| Item | Figure | Period | Classification |
|---|---|---|---|
| FY27 revenue growth | 15-20% (revised from 10-15%) | FY27 | (a) guidance, with period |
| FY27 EBITDA margin | 14-15% | FY27 | (a) guidance, with period |
| FY27 export contribution | 25-30% of revenue | FY27 | (a) guidance, with period |
| FY28 revenue growth | 15-20% | FY28 | (a) guidance, with period (B12b notes management qualified this with "we cannot predict for 28" in the same breath, May call) |
| FY28 EBITDA margin | 15-17% | FY28 | (a) guidance, with period |
| Paracetamol utilisation | 70-75% by FY27-end, full by FY28 | FY27/FY28 | (a) guidance, with period |
| Non-ibu contribution to API segment | 50-55%, margin parity with ibuprofen | FY29 | (b) aspiration, period named but distant and unquantified on the margin-parity half |
| Peak revenue at 100% utilisation of current assets | Rs 3,200-3,300 Cr | no date attached | (c) capacity/capability only |
| Ibuprofen expansion to 18,000 MTPA | commissioning Dec 2027 | dated | (a) guidance, with period |
| Combined three-initiative blended ROCE target | >15% company-wide | "once fully implemented," no date | (b) aspiration, no period |

Comment: the FY26 EBITDA margin guide was walked down twice within the Q3 FY26 call
itself (14-15% to 13% to 11-12%) before being met at 12.4% (B05 promise_delivery),
showing management will revise a stated guidance figure live under analyst pressure
rather than hold it silently to a miss.

### 4. CONCENTRATION

Quote/figure (AR FY26 Note 39 geographical information, p.168, via B04): domestic
75.7% / export 24.3% of FY26 revenue.
Product concentration: Ibuprofen alone ~37.9% of FY26 revenue (B04 revenue_streams,
computed from AR p.10 mix-shift disclosure and Note 39 segment revenue); the
non-ibuprofen API basket ~22.3%; Chemicals external sale ~39.8% (Note 39, Rs 922.81 Cr /
Rs 2,319.06 Cr).
Customer concentration: NOT DISCLOSED. No top-customer or top-5/top-10 percentage figure
was volunteered by management on any of the four call transcripts, and none is disclosed
in the AR (B05 input_gaps, B02/B04 input_gaps). This is a genuine disclosure gap, not a
search failure: no analyst asked for it either (B05).

### 5. PROMISE LEDGER

Table reused from B05's promise_delivery rows (maker stage's own quote-anchored table,
cross-checked by B12b, corrections applied per that verifier where noted):

| Promised in | Promise | Outcome | Anchor |
|---|---|---|---|
| Q3 FY26 call | Q4 FY26 revenue ~Rs 600 Cr | DELIVERED (beat): Rs 619 Cr, +17.4% YoY | Q4 FY26 call financials |
| Q3 FY26 call | Q4 FY26 EBITDA margin ~11% | DELIVERED (large beat): 15.2% | Q4 FY26 call; B12b notes part of this beat was an inventory valuation gain, denied in May, admitted in Aug (see credibility note below) |
| Q3 FY26 call | FY26 EBITDA margin, walked down live 14-15% to 13% to 11-12% | PARTIAL: met the revised 11-12% guide (actual 12.4%); original 14-15% guide missed | Management's own sequence |
| Q3 FY26 call | FY26 capex ~Rs 150 Cr (trimmed to Rs 130-135 Cr) | DELIVERED: Rs 160 Cr actual | Q4 FY26 call financials |
| Q3 FY26 call | Minoxidil commercial API launch by Q1 FY27 | DELIVERED early | Q4 FY26 call |
| Q4 FY26 call | Greenfield project in 4-6 to 6-8 quarters from May 2026 | **OPEN / NOT YET DUE** (corrected by B12b; the maker stage's original "MISSED" label is wrong in direction: the window has not elapsed as of this run) | Q4/Q1 FY27/Sep-2026 calls |
| Q4 FY26 call | Paracetamol utilisation 55% to 70-75% by FY27-end | PARTIAL/PENDING, target date not yet due | Q1 FY27 call still ~55% (or 65% per press release, see Section 6 Item 3) |
| Q4/Q1 FY27 calls | FY27 revenue +15-20%, EBITDA margin 14-15% | PARTIAL/ON TRACK: Q1 FY27 print revenue +37%, margin 14.6%, ahead of pace, guide not raised | Q1 FY27 call |
| Q1 FY27 call | Export contribution 25-30% of FY27 revenue | DELIVERED early, upper end: 28.5% | Q1 FY27 call |
| Sep-2026 business update | Capex breakdown Rs 350 Cr + Rs 110 Cr + Rs 35 Cr = Rs 495 Cr | DELIVERED, matches the Reg 30 filing exactly | Reg 30, 09-Sep-2026 |

Comment (credibility, carried per operator ruling need): B12b independently found
management denied a Q4 FY26 inventory valuation gain on the May call and admitted one on
the August call, meaning part of the 15.2% Q4 margin beat above was inventory-driven,
not purely operational. B12b puts the credibility grade at the B/C line versus the maker
stage's B; this is named as an operator ruling item, not resolved here (B13
halt1_rulings_needed).

### 6. RESTATED BASES

Quote (AR FY26, Note 53 standalone / Note 50 consolidated, as extracted by B02, primary
read of the notes): "previous year figures have been regrouped/recasted/rearranged
wherever necessary" — a generic boilerplate sentence, with no quantified instance named
anywhere in the note set. Quote (Statement of Changes in Equity, p.134): the template
column "Restated balance at the beginning of the current reporting year" is present, but
the "Changes... due to prior period errors" column is blank/Nil in both years.
Comment: no restatement found. This is boilerplate structure required by Schedule III,
not evidence of an actual restatement (B02).

### 7. CORPORATE-ACTION CLAUSES

Two corporate actions are in the corpus, both feeding LBF2 (promoter reclassification),
reconstructed by B08 from primary filings:
- **Demerger**: NCLT (Chandigarh Bench), order CP(CAA)10/CHG/PB/2025, dated 25-Sep-2025
  (formal order issued 09-Oct-2025). Demerged company: Vasudeva Commercials Limited
  (non-promoter, per its own Reg 29(2) filing statement: "Whether the acquirer belongs
  to Promoter/Promoter group: No", SAST-29-2-8, 01-Oct-2025). Resulting company:
  Synthorix Trading Limited (newly created). Ratio/allocation: 1,15,78,195 shares
  (3.94% at the time) moved to Synthorix Trading; Vasudeva retained 1,17,41,100 shares
  (4.00%).
- **Amalgamation**: Regional Director (Northern Region-II), Chandigarh, Order Nos.
  RDNR/233/AC3630802/2026/426-428, sanctioned 24-Jun-2026. Amalgamating companies: G
  Consultants and Fabricators Private Limited and Synthorix Trading Limited (both
  confirmed public/non-promoter, "Bodies Corporate" category, in the BSE XBRL
  shareholding pattern for the quarter ended 31-Mar-2026). Amalgamated into: NM
  Merchantiles Limited (promoter entity). Shares moved: 29,05,000 + 1,11,78,195 =
  1,40,83,195 shares (4.80% of capital), effective 25-Jun-2026 (SAST-29-2-4,
  26-Jun-2026).
Comment: this is a two-step, filing-confirmed demerger-then-amalgamation sequence that
raised promoter/promoter-group holding from 57.48% (31-Mar-2026) to 62.28%
(30-Jun-2026), a genuine +4.80pp increase (B08). Beneficial control of Vasudeva
Commercials and G Consultants before these transactions is NOT FOUND (B08 input_gaps);
this is the item named in the research brief (4d item 3).

### 8. RELATED-PARTY PERIMETER

Quote/figures (AR FY26 Note 40, p.169-171, as extracted by B02/B08): FY26 purchases of
goods/services from three trading promoter entities totalled Rs 131.94 Cr: Mayadevi
Polycot Limited Rs 69.42 Cr, NCVI Enterprises Limited Rs 40.00 Cr, NM Merchantiles
Limited Rs 22.52 Cr (+205.4% YoY for NM Merchantiles alone, the same year its own equity
stake rose 13.08% to 17.08%, +4.00pp within the AR year). Rent paid to promoter entities:
Rs 0.34 Cr, flat YoY. NCVI Enterprises also gave the group a Rs 27.65 Cr customs-bond
surety (Note 40C(iii), p.170), a promoter entity extending credit support to the company,
not the reverse. Quote (Note 40C(i), p.171): transactions stated as "made in the
ordinary course of business and on terms equivalent to arm's length."
Comment: Board's Report Section 22 (p.57) states "no material transaction... AOC-2 not
applicable," technically correct under the Section 188(1) threshold test but understates
the RPT book's visible scale against Note 40 (B02/B03). All RPTs were approved by an
independent-majority Audit Committee, 3 of 4 members independent (B03/B08 mitigating
fact).

### 9. PLEDGE AND SHAREHOLDING

Quote (BSE XBRL shareholding pattern, item 7 of the Declaration table, every quarter
Sep-2024 through Jun-2026): "Whether any shares held by promoters are encumbered under
'Pledge'? No." Pledge: 0% across all 8 quarters examined (B08 pledge_trend). Comment: the
corpus holds only 8 quarters (Sep-2024 to Jun-2026), not the twelve quarters the question
asks for; this is a corpus-depth limit, named here rather than filled.
Latest shareholding (30-Jun-2026, SHP-June-2026.txt, direct read this pass): Promoter
and Promoter Group 62.28% (5 holders: Varinder Gupta 2.04% personal, plus Varinder
Gupta HUF 0.00%, Mayadevi Polycot Limited 21.79%, NM Merchantiles Limited 21.88%, NCVI
Enterprises Limited 16.58%). Public 37.72%, split: Institutions (Domestic) 0.43% (Mutual
Funds 0.02%, Alternative Investment Funds 0.41%); Institutions (Foreign) 4.87% (FPI
Category I 3.65%, FPI Category II 1.22%); Non-institutions 32.42% (Resident individuals
up to Rs 2 lakh 21.86%, above Rs 2 lakh 5.08%, NRIs 1.42%, Bodies Corporate 2.44%,
others 1.60%). Comment: FII/FPI holding rose from 1.72% (31-Mar-2026) to 4.87%
(30-Jun-2026), nearly tripling in one quarter, coinciding with the reported +170%
four-month stock rally (B08). Later-quarter shareholding files (Jun-2025 onward) carry
full institutional sub-category detail despite B00's summary describing them as
"category summaries only"; entity-level promoter detail (individual promoter-group
holder names) is present in every quarter examined, including Jun-2026, confirmed by
this pass's direct read.

### 10. VERIFICATION

Documents quoted in this annex, with filename and date:
- Investor_Presentation_1.pdf (Q1 FY27, filed ~12-Aug-2026) — Section 6 Item 1.
- Annual_Report_2026.pdf (FY26, filed 07-Aug-2026), Notes 39, 40, 42, 35B, 49, 53,
  Statement of Changes in Equity — Section 6 Items 2, 6, 7, 8.
- Concall_Feb_2026_Transcript.pdf, Concall_May_2026_Transcript.pdf,
  Concall_Aug_2026_Transcript.pdf, Concall_Sep_2026_Transcript.pdf — Section 6 Items 3,
  5.
- 20260909-... Reg 30 capex intimation (09-Sep-2026) — Section 6 Items 3, 7.
- SAST-29-2-8 (01-Oct-2025), SAST-29-2-4 (26-Jun-2026) — Section 6 Item 7.
- SHP-June-2026.txt, SHP-March-2026.txt (BSE XBRL shareholding patterns) — Section 6
  Items 7, 9.

CORPUS COMMIT HASH: fdef8985eb1f31bb7db83492927b9d8d3c644c75

---

END OF DOSSIER.
