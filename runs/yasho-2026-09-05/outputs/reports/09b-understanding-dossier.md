# HALT 1 UNDERSTANDING DOSSIER — Yasho Industries Ltd (YASHO)
Run date: 2026-09-05 | Stage: B09b-dossier | Model: Sonnet 5

Assembly-only document. Built from committed blocks B00-B09 and verifier
blocks B12a-B12d, plus the source PDFs for Section 6 only. No new research,
no price or verdict-set language. The Mental Model Declaration in Section 2
is a DRAFT for operator sign-off in claude.ai.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

1. **CONCALLS.** Four transcripts held: Nov-2025 (Q2 FY26), Feb-2026 (Q3
   FY26), May-2026 (Q4 FY26), Aug-2026 (Q1 FY27) (B00). Most recent quarter
   covered: Q1 FY27 (quarter ended 30-Jun-2026). Given the run date
   (2026-09-05), the next quarter (Q2 FY27, ended Sep-2026) would not
   plausibly have reported or held a concall yet (Indian listed companies
   typically report 4-6 weeks after quarter end). No plausible gap.

2. **ANNUAL REPORTS.** Two years held: AR FY2026 (primary, latest audited)
   and AR FY2025 (backward baseline) (B00). The latest completed FY (FY2026,
   ended Mar-2026) is present. Only 2 years held, short of the 3-year
   preference; FY2021-FY2023 annual-report text is absent from the corpus
   (B01 input_gaps), which is why several Gate 0 sub-metrics (capex
   breakdown, trade payables, promoter-holding 3-year change) run on
   narrower FY2024-FY2026 or 1-year windows.

3. **RESULTS FILINGS.** None held (results folder empty, B00). Gate 0's
   latest-period figures come from screener-Data_Sheet.csv, the two ARs,
   and the Q1FY27 Investor Presentation, not an audited or filed quarterly
   result. Quarter-gap: no filed result exists for any quarter; the
   presentation is the only post-FY2026 source in the corpus.

4. **INVESTOR PRESENTATIONS.** One held: Q1FY27 Investor Presentation,
   filed to BSE/NSE 31-Jul-2026 (B00).

5. **RESEARCH / RATING.** None held. No broker note, no rating rationale
   PDF. The presentation states a CRISIL/ICRA upgrade from BBB+ to A-
   (pres. p.12 per B00), but that is presentation-sourced, not a rating
   agency document.

6. **CORPORATE ACTIONS.** None held (announcements folder empty, B00). No
   Reg 30 filing for the Feb-2025 Rs 125 cr preferential allotment, the
   promoter-group reclassification, or any order/JV/capex announcement
   exists in the corpus; what is known of these events comes from AR text
   (Directors' Report) or web search performed at Stage 8 (B08), not from
   a held announcement filing.

7. **FRESHNESS PAIR CHECK.** B00 `freshness_verdict`: FRESHNESS PAIRS OK.
   All four pairs PASS (none triggered): results-to-concall (no results
   filing to trigger the pair), rating-bulletin-to-rationale (no rating
   filing to trigger), SEBI-order-to-text (no order referenced), AR-to-
   latest-audited-annual (AR FY2026 is itself the latest annual result).
   No failed pair; the verdict line below is NOT capped at
   CORPUS GAPPED-FRESHNESS.

8. **VERDICT LINE: CORPUS GAPPED.**
   - results: no quarterly results PDFs — findable-but-missing (BSE/NSE
     filing archive, or company IR page).
   - rating: no rating rationale — findable-but-missing (CRISIL/ICRA
     websites).
   - announcements: no Reg 30 documented-action filings — findable-but-
     missing (BSE/NSE filing archive).
   - shareholding: no quarterly shareholding-pattern filing — findable-
     but-missing (BSE/NSE filing archive, or Trendlyne aggregation).
   - screening_csv_partial: YASHO P&L/Balance Sheet/Cash Flow/Quarters
     CSVs are header-only, a collector defect, not a company-side gap
     (B00); only Data_Sheet.csv populated.
   None of these read as plausibly-nonexistent; all are standard filings a
   long-listed company would have on the exchange archive. This is a
   corpus-completeness gap on the operator's Halt 1 upload list, not a
   company-opacity finding in itself.

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF.** This is a transition thesis, not a
signed model. It is signed only in claude.ai after live-web stress-testing.

### PART A — THE FROM STATE

**A1. Archetype.** Two revenue lines, both currently run as spec-driven
B2B ingredient supply (B04 revenue_streams, type "B2B manufactured-goods
sale, spec-driven ingredient supply" for both lines). The FROM archetype
for both lines is **build-to-spec component maker** (customer capex
cycle, design-win pipeline, content per unit, input-cost pass-through) —
the closest CLAUDE.md archetype to a chemical additive supplied against a
customer's formulation spec, funded in part by the customer's own capex
commitment on the Industrial line (B04 moats_present: "switching costs
(customer-funded 15-year MNC supply agreement)").
- Industrial Chemicals (rubber chemicals, lubricant additives,
  stabilisers): ~89% of FY26 revenue per the AR MD&A figure (B04; the
  AR's own About Us page states 87%, an internal inconsistency B04 flags
  and this dossier does not resolve).
- Consumer Chemicals (aroma/F&F, food additives, personal care, agro/
  pharma intermediates): ~11% of FY26 revenue (B04). Revenue in this line
  fell 20.3% YoY, moving in the opposite direction of the Industrial
  line's 27.1% growth (B02 finding 13).

**A2. The simple analogy.** Yasho buys petrochemical raw materials and
turns them into specialty additives: chemicals that go INTO other
companies' products rather than being sold as a finished product
themselves. A tyre maker adds Yasho's accelerators and antioxidants to
cure its rubber. An oil blender adds Yasho's lubricant additives to make
an engine oil perform. A fragrance house adds Yasho's aroma chemicals to
a scent formula. Today this is largely a volume-and-cost business: sell
more tonnes, at a spec the customer sets, at a price the market and raw-
material cycle largely dictate (B04 pricing_power: "moderate";
cyclicality: "cyclical").

### PART B — THE TRANSITION

**B1. From → To (Industrial Chemicals / MNC LTSA line).**
FROM: **R2 Cost-Advantaged Converter** (margin from cost position, not
price; durable mid-teens ROCE) — consistent with FY2026 audited ROCE of
11.34% and median 5-year ROCE of 12.87% (B01 Block A), and EBITDA margin
that moved only +0.96pp over 5 years (16.44%→17.40%, B01 M1).
TO: **R3 Value-Added / Spec'd Supplier** (spec-in and switching costs
give partial pricing power; ROCE 20-25% with stickiness) — the claimed
destination, evidenced on paper by the 15-year customer-funded MNC
supply agreement (B04) and the Q1FY27 EBITDA margin print of 24.2%
(B04, B05).
The Consumer Chemicals line shows no comparable engine and no B2-type
pillar (B07); its revenue is contracting (B02 finding 13), so this
declaration does not carry a TO tier for that line — it is flagged as a
line with **no active transition evidence** in the corpus, a finding in
itself.

**B2. The engine.** Two things physically change on the Industrial line:
(1) dedicated, customer-funded capacity at Pakhajan built specifically
for the MNC's 15-year lubricant-additive supply agreement, which locks
in a qualification-based relationship the customer has already paid to
help build (B04 moats_present; B03 guidance table: MNC project capex
Rs 85-90 cr, customer-funded); (2) a mix shift toward higher-value
Industrial chemistries and away from lower-margin/declining Consumer
lines, combined with rising capacity utilisation (~50%→~65% per B05
analyst_note) producing sharp operating-leverage on incremental revenue
(Q1FY27 incremental EBITDA margin ~38.2% vs FY26 full-year ~16.3%, B04
unit_economics).

**B3. The proof gate.** Three conjunctive, quarter-by-quarter conditions,
all named across B03/B05/B07/company memory: (i) MNC commercialisation
proceeds on schedule — equipment delivery Q2/Q3 FY27, trial Q4 FY27,
commercial supply Q1 FY28 (B05 triggers priority 1); (ii) EBITDA margin
holds above ~20% for 2-3 consecutive quarters, not reverting toward the
FY26 17-19% band (B05 triggers priority 2; B07 FLAG-EM-MARGIN-UNPROVEN);
(iii) working-capital days and DSCR do not re-widen — WC holding near or
below the ~143-175 day band and DSCR sustained above the current 1.04x
floor (B02 finding 7; B03 monitorables). Until all three fire together,
the transition is narrative, not demonstrated.

**B4. The recognition gap (open question, resolved at Stage 11).**
Whether the market already prices the TO state — a value-added, spec'd
supplier with a durable customer-funded contract — is an open question
this dossier does not answer. It is the question Stage 11 resolves via
the PE gap against the Section 1B destination multiple. No number, no
conclusion is stated here.

**B5. The ugliness test.** Today's ugly optic is Gate 0's mechanical
scorecard outcome: a triggered leverage/coverage deal-breaker (net debt/
EBITDA 3.74x, interest coverage 1.61x, FY2026 audited, B01 Block D) and a
growth-quality decoupling (revenue CAGR 18.22% vs PAT CAGR 3.30%,
FY21-26, B01 Block C). The evidence leans toward classifying this
**ARTIFACT-OF-CLIMB**: both trace to one dated event, the FY2024
Pakhajan capex cycle (Rs 336.99 cr in a single year, B01), and B03's
independent DuPont decomposition finds the FY26 recovery margin-driven,
not leverage-driven, with the leverage component itself declining. The
company-disclosed Q1FY27 net debt/EBITDA of 1.86x (down from 3.74x,
Investor Presentation) points the same direction. This classification
carries an explicit caveat: the Q1FY27 leverage figure could not be
reconciled to the audited FY2026 basis from the corpus (B01 FLAG-
LEVERAGE-DIVERGENCE), and a cluster of accounting-quality findings —
subsidiary receivables growing 78.7% against 15.9% sales growth to those
subsidiaries, a consolidation-adjustment line moving opposite direction,
recurring quarterly drawing-power variances of Rs 31.7-52.7 cr, and MSME
overdue payables up 327.6% (all B02) — are unresolved and could, on
verification, argue toward a STRUCTURAL reading instead. This is named
as an open verification item, not settled here.

**B6. The transition falsifier.** Any of: (a) further slippage of MNC
commercial-supply past Q1 FY28, or advance funding stalling or being
refunded (B05 kill_signal; already slipped once from an earlier "Q4FY27
operational" framing without being labelled a change, B05); (b) EBITDA
margin reverting toward the 17-19% multi-year band within the next 1-2
quarters (B05, B07 kill_signal); (c) the MNC advance figures failing to
reconcile at the next filing, leaving the audited Rs 29.52 cr as the
only substantiated number against the Rs 51.4 cr (AR MD&A) and Rs 98.12
cr (presentation) figures currently in tension (B02, B03, B12a).

### PART C — WHAT THE MODEL WATCHES

**C1. Dominant variables** (derived from B2/B3, not the static snapshot):
1. **MNC LTSA commercialisation timeline.** Equipment delivery guided
   Q2/Q3 FY27, trial Q4 FY27, commercial supply Q1 FY28; already slipped
   once from an earlier framing without being labelled a change (B05).
2. **EBITDA margin durability above ~20%.** Currently one quarter of
   print (24.2%, Q1FY27) against a multi-year 17-19% guided band (B05
   analyst_note; B07 FLAG-EM-MARGIN-UNPROVEN).
3. **Working-capital cycle and DSCR trajectory.** Company presentation
   states WC cut from 190 to 143 days (B04), but the audited year-end
   figures for FY24-26 actually worsened by 25.6 days (B01 Block B4);
   DSCR sits at 1.04x, near the 1.0x floor (B02 finding 7).
4. **MNC advance reconciliation.** Three different, internally
   unreconciled figures for the same claim exist in the corpus: audited
   Note 19/24/48 Rs 29.52 cr, AR MD&A Rs 51.4 cr, Q1FY27 presentation
   Rs 98.12 cr — all independently confirmed as genuinely printed by the
   B12a verifier (B02, B03, B12a).

**C2. What the model rejects.** Total addressable market size is not the
binding constraint: the underlying market Yasho sells into grows only
~4.9% blended (B09), the company's own SAM revenue headroom is ~27.4x
current share (B09 revenue_headroom_x), and the lubricant-additive full-
package market is a top-4 oligopoly with >85% share concentrated among a
few global players (B09 flags) — so market size is not what decides this
transition. Execution against the three proof-gate conditions above, and
the reconciliation of the advance figures, decide it, not sizing.

**C3. The business falsifier** (distinct from B6, kills the FROM
business, not just the arrow). If FY27 audited net debt/EBITDA and
interest coverage fail to durably clear the deal-breaker bands even
after the capex cycle completes (staying above 3x / below 1.5x), and the
cluster of accounting-quality findings named in B5 above proves
structural rather than one-off — subsidiary receivables/consolidation-
profit divergence, recurring drawing-power variance, MSME payable
stretch — that would indicate the base converter business itself carries
an unresolved cash-conversion and leverage problem independent of any
transition narrative (B01 Gate 0 mechanical scorecard result; B02 top
findings).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

*(Per prompts/13-synthesis-pipeline.md BUSINESS UNDERSTANDING NARRATIVE
spec — the five-question prose spec, drafted here from B01-B09 for Halt
1; Stage 13's copy is the version of record, updated by later stages.)*

**What it makes and why it matters.** Yasho manufactures two families of
specialty chemicals. Industrial Chemicals — rubber accelerators and
antioxidants for tyres, conveyor belts, latex gloves; lubricant
additives for hydraulic, engine and gear oils, greases and metalworking
fluids; and stabilisers for acrylics, inks and resins — made ~89% of
FY26 revenue per the AR's MD&A figure (B04; the About Us page states 87%
for the same period, an unresolved internal inconsistency, B04).
Consumer Chemicals — aroma chemicals for flavours and fragrances,
personal care, oral care, and agro/pharma intermediates — made the
remaining ~11% and contracted 20.3% YoY (B02 finding 13; B04). These are
functional additives that become part of a customer's own formulation,
not standalone branded products; that is the structural basis for
whatever switching-cost moat exists (B04).

**Who buys and why.** Customers are other manufacturers: tyre and rubber
goods makers, lubricant and oil blenders, and fragrance/personal-care
formulators (B04). No customer-concentration disclosure (top 1/5/10 %
of revenue) exists anywhere in the AR or presentation despite risk-
language citing diversification (B04 flag) — an evidence gap this
dossier cannot close. One customer is named without identity disclosure:
a global MNC under a 15-year lubricant-additive supply agreement,
expected to contribute roughly Rs 150 cr/year once commercial supply
starts, a material single-customer block that cannot be sized against
total revenue without concentration disclosure (B03 guidance table; B04
flag; B09 downstream_candidates).

**Why demand exists.** Rubber accelerators and antioxidants are required
wherever tyres and rubber goods are manufactured; lubricant additives
wherever industrial and automotive lubricants are blended; aroma
chemicals wherever flavour, fragrance or personal-care products are
formulated (B09 methods_used, bottom-up tyre-value cross-check). This is
formulation-input demand, not discretionary, but it moves with the end
industries' own cycles (B04 cyclicality: "cyclical").

**Why demand grows or does not.** The underlying market Yasho sells into
grows slowly — roughly 4.9% blended across its segments (B09 tam_growth
pct) — well below both management's guided 30-40% annual growth and the
peer set's low-single to low-double-digit sector volume growth (B06
industry_cross_read: demand). Nearly all of the growth the company
guides to must therefore come from taking market share and running new
capacity — the MNC line and the Pakhajan capacity build — not from the
market itself expanding (B09 flags; B06 analyst_note).

**Where the competitive advantage sits, per line.** On the Industrial
line, the evidence base names: switching costs via the customer-funded
15-year MNC agreement (medium-high durability, but concentrated in one
relationship, B04); REACH plus eight other international certifications
(medium durability, B04); and distribution via port-proximate plants and
two overseas subsidiaries, Yasho Industries Europe B.V. and Yasho Inc.
(medium durability, B04; Note 39 AR FY2026 p.144). B07's quantified
emerging-moat scan scores 17 (MODEST classification), resting almost
entirely on one strong category — B2, qualification lock-in from the
MNC contract (B07 em_score, active_categories). On the Consumer line, no
comparable pillar was found: no patents or named inventors (I1=0), no
documented talent or cost asymmetry (I2=0, B07 flags FLAG-EM-NO-TALENT-
IP-EVIDENCE), and the line's own revenue is contracting.

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per dominant variable, Section 2 Part C1)

**1. MNC LTSA commercialisation timeline.** What the corpus establishes:
equipment delivery guided Q2/Q3 FY27, trial Q4 FY27, commercial supply
Q1 FY28 (B05); the timeline already moved once, from an earlier "plant
operational Q4 FY27" framing (Q2 FY26 call) to "commercialisation Q1
FY28" (Q3 FY26 call onward), without being labelled a change (B05
timeline_slippages). What it cannot establish: the counterparty's
identity (NDA-bound, B03/B09), whether the counterparty has itself
disclosed the agreement in its own filings, or independent confirmation
that equipment procurement is on track. Questions: (i) Has the
counterparty's own capex/procurement disclosure corroborated equipment
delivery progress? (ii) Has any further slippage occurred since the
Aug-2026 call? (iii) What are the take-or-pay or minimum-offtake terms
the auditor's Key Audit Matter references but Note 48's own text never
states (B02 finding 1, questions_for_mgmt)?

**2. EBITDA margin durability above ~20%.** What the corpus establishes:
FY26 full-year EBITDA margin 17.4%, Q1FY27 24.2% (B04, B05); management's
mechanism explanation (utilisation 50%→65%, mix, 10-12% margin premium
on new products) was given under skeptical direct questioning (B05
analyst_note). What it cannot establish: whether the print repeats for
2-3 more quarters, or whether peer-set evidence of margin COMPRESSION
in the same RM-inflation window (NOCIL, CAMLINFINE, B06) undercuts the
mix-driven explanation. Questions: (i) Does Q2/Q3 FY27 margin hold above
20%? (ii) Does the peer-confirmed magnitude of RM inflation (peers
report 70-100% vs Yasho's stated 10-15%, B06) eventually pressure
Yasho's own input costs? (iii) How much of the incremental margin is
operating leverage (reversible if utilisation growth slows) versus
genuine pricing power (B04 analyst_note)?

**3. Working-capital cycle and DSCR trajectory.** What the corpus
establishes: audited FY24-26 WC days worsened from 127 to 153 (B01 Block
B4), even as the company's own presentation claims a cut from 190 to 143
days (B04) — two different bases that do not reconcile in the corpus;
DSCR 1.04x FY26 vs 1.08x FY25 (B02 finding 7); a peer verifier (B12b)
separately found management's own words attribute part of the WC
improvement to "a genuine supply issue" (forced RM shortage), not pure
discipline. What it cannot establish: which basis (audited year-end vs
company trailing-quarter) is the operative one going forward, or whether
the next audited year-end print confirms the trailing improvement.
Questions: (i) Does the FY27 audited year-end WC-days figure confirm or
contradict the 143-day trailing claim? (ii) Does DSCR clear 1.15x per
B03's monitorable threshold? (iii) Is the WC improvement structural
(process change) or a one-off inventory effect, as B12b's missed finding
suggests?

**4. MNC advance reconciliation.** What the corpus establishes: three
different figures for the same underlying claim, all independently
verified as genuinely printed in their respective source documents by
B12a — audited Note 19/24/48 Rs 29.52 cr, AR MD&A Rs 51.4 cr, Q1FY27
presentation Rs 98.12 cr (B02, B03, B12a). Note 48, the subject of the
auditor's own Key Audit Matter, contains zero rupee figures (B02 finding
1). What it cannot establish: which figure, if any, is the operative
one, or whether the gap reflects a later quarter, a different entity-
level cut, or a revised estimate (B02 questions_for_mgmt). Questions:
(i) Which of the three figures does management stand behind at the next
filing? (ii) Does the FY27 quarterly/annual note finally reconcile
Note 48 to a rupee figure? (iii) Does the gap correlate with any change
in the contract's minimum-supply-commitment or penalty terms?

### 4b. Candidate signal table

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Global tyre production volumes and majors' capex plans (Michelin, Bridgestone, Goodyear, Continental, MRF, Apollo, CEAT) | Sustained YoY decline in global/India tyre production, or a capex freeze among tyre majors, undercutting the rubber-chemicals end-demand read | Quarterly | Tyre majors' quarterly results/investor days; IRMRA data (B09) |
| Undisclosed MNC counterparty on the 15-year supply agreement | No Reg 30 filing corroborating order/equipment progress by the guided dates, or a filing disclosing termination/renegotiation | Event-driven | Company Regulation 30 filings (BSE/NSE) — NDA-bound (B09) |
| China rubber/lube-additive/aroma-chemical export pricing | Chinese export pricing falling further or staying flat while Yasho's stated 10-15% RM-inflation figure (already below the peer-confirmed 70-100% magnitude, B06) fails to track actual cost pressure | Monthly | ICIS pricing / Chinese customs export data (B09) |
| ECHA REACH registration status/renewals | Any REACH registration lapse, rejection, or non-renewal blocking EU market access | Event-driven | ECHA REACH database (B09) |
| Global lubricant consumption volumes | Global lubricant consumption volumes flat or declining, undercutting the lube-additive demand story | Quarterly | Kline & Company / S&P Global Lubes'n'Greases (B09) |
| Global F&F/personal-care majors' quarterly results (Givaudan, IFF, Symrise) | F&F/personal-care majors reporting flat or declining volumes, undercutting the Consumer division demand read | Quarterly | Givaudan, IFF, Symrise quarterly results (B09) |

All six candidates are UNVERIFIED at Halt 1; verification and tracker
writes happen at Role 5.5 in claude.ai per
Downstream_Source_Discovery_Protocol_v1_0.

### 4c. Fragility read

- **variable_count:** 4 (the Section 2 Part C1 dominant variables: MNC
  LTSA timeline, EBITDA margin durability, WC/DSCR trajectory, MNC
  advance reconciliation).
- **verifiability_ratio:** 1 of 4 carries an external verification path
  (MNC LTSA timeline, via counterparty Reg 30 disclosure and the tyre-
  volume/lube-consumption downstream candidates in 4b). The other three
  — EBITDA margin durability, WC/DSCR trajectory, MNC advance
  reconciliation — are observable only inside Yasho's own quarterly and
  audited disclosures, with no independent corroboration path found in
  the corpus.
- **single_point_failure:** MNC LTSA commercialisation slipping again, or
  the advance funding stalling or being refunded. B07's own analyst note
  states the emerging-moat score would likely fall below the meaningful
  threshold if the MNC contract were stripped out (B07 analyst_note); B05
  names the same contract as trigger priority 1 with an explicit kill
  signal.
- **fragility_verdict:** FRAGILE. Three of four dominant variables are
  company-narrated only with no external check in the corpus, and one
  single variable (the MNC contract) can independently break both the
  growth guide and the emerging-moat case (B07 FLAG-EM-SINGLE-PILLAR).

### 4d. Research brief (claude.ai live-web work order)

1. Confirm the MNC counterparty's identity and any Reg 30 filing tracking
   equipment-delivery or commercial-supply milestones (B03, B09 gap:
   NDA-bound, undisclosed in corpus).
2. Pull the GST Gujarat High Court and Supreme Court judgment texts
   directly — indiankanoon.org and taxreply.com were blocked by this
   session's egress proxy (B08 gap).
3. Pull the NSE 30-Jul-2025 change-in-management filing content directly
   (B08 gap: URL surfaced, content not fetched this run).
4. Query the SEBI enforcement-order database and MCA/RoC registry
   directly for the company and the Jhaveri promoters (B08 gap: no direct
   tool access this session).
5. Verify quarterly promoter pledge and shareholding pattern for the
   last twelve quarters directly from BSE/NSE filings (B00 gap:
   shareholding folder empty in corpus, only presentation- and web-
   search-sourced figures available).
6. Obtain the next quarterly results filing (Q2 FY27, when available)
   and its same-quarter concall to test the three proof-gate conditions
   (B00 results gap).
7. Obtain a primary rating rationale document from CRISIL/ICRA, not just
   the presentation-stated A- upgrade (B00 rating gap).
8. Corroborate global/India tyre-production and lubricant-consumption
   volume trends from Kline & Company, S&P Global Lubes'n'Greases, or
   IRMRA data (B09 downstream candidate 1 and 5).
9. Corroborate China rubber-chemical/lube-additive export pricing from
   ICIS or Chinese customs data (B09 downstream candidate 3; B06 flags a
   large magnitude gap versus peer-quantified RM inflation).
10. Check ECHA REACH registration status and renewal dates for Yasho's
    EU-bound products (B09 downstream candidate 4; B04 moat-evidence
    gap).
11. Attempt a usable AmbitionBox/Glassdoor employee-reputation read for
    Yasho Industries specifically; this run's searches returned only
    unrelated same-named entities (B08 gap).
12. Corroborate the $12-15bn lube-additive/adjacent-chemistry market-size
    claim and check whether a 15-year, fully customer-funded capex supply
    agreement is a recognised structure elsewhere in Indian specialty
    chemicals (B06: unverifiable against the peer set provided; B09
    analyst_note).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Yasho Industries makes specialty chemicals: rubber accelerators and
   antioxidants, lubricant additives, and aroma chemicals (B04).
2. It runs two divisions. Industrial Chemicals made about 89% of FY26
   revenue. Consumer Chemicals made about 11% (B04). The annual report's
   own pages differ slightly on this split (89/11 vs 87/13), a small
   unresolved inconsistency (B04).
3. The company has two plants, at Pakhajan and Vapi in Gujarat, and
   exports to more than 50 countries (step1-business-brief; B04).
4. Its customers are other manufacturers. They buy Yasho's chemicals as
   ingredients: for tyres and rubber goods, for industrial and engine
   oils, and for fragrance and personal-care products (B04).
5. One buyer stands out. A global company signed a 15-year deal for
   lubricant additives. Once supply starts, management expects about
   Rs 150 crore a year in revenue from this one contract (B03).
6. The corpus does not say what share of total revenue any single
   customer holds, including this one. Nobody can size how much this
   contract will matter next to total sales without that number (B04).
7. Demand for these chemicals grows slowly at the market level. The
   wider market Yasho sells into grows only about 4.9% a year (B09).
8. Yasho's own growth guide is 30-40% a year, far above that. Almost all
   of the growth it guides to must come from taking market share and
   running new capacity, not from the market itself growing (B09, B06).
9. Where a competitive edge exists, it sits mostly in one place: the
   customer-funded MNC contract, because that customer has already paid
   to help qualify Yasho's plant for its own supply chain (B04, B07).
10. Outside that one contract, the company holds export certifications
    and has plants close to ports, but no patents, no named scientists,
    and no proven cost or technology edge over competitors (B07).
11. The plan is a move up in quality: from a chemical maker earning
    mostly on cost position, toward one with locked-in, spec'd customer
    relationships. The proof for that move rests almost entirely on one
    contract and one strong quarter of margin (B07, B05).
12. The company's own documents disagree on how much money that MNC
    customer has paid so far: Rs 29.52 crore in the audited financial
    notes, Rs 51.4 crore in the same annual report's own management
    discussion, and Rs 98.12 crore in the investor presentation (B02,
    B03, B12a).
13. This makes the setup fragile. If the MNC deal slips again, or the
    advance funding stalls, both the growth story and the one strong
    competitive-edge case lose their main support (B05, B07).
14. The corpus could not establish a per-tonne price for any product, a
    customer-concentration percentage, or three full years of working-
    capital and free-cash-flow history; several figures cover only one
    or two years (B04, B01).
15. The two biggest open questions: does the 24.2% margin seen in one
    quarter hold for two or three more, and which of the three MNC
    advance figures management will confirm as correct (B05, B02, B03).

---

## SECTION 6: STANDING EXTRACTION ANNEX

Ten standing questions, answered from corpus in quote-then-comment form.
Filenames and page anchors given on every quoted figure. NOT DISCLOSED
recorded where the corpus does not carry an item.

### 1. UNITS

Quote (unit_economics field, B04, drawn from AR/presentation review):
"revenue_per_unit: NOT FOUND - company discloses % volume growth, not
absolute tonnage or per-tonne realization" (B04). Direct text search of
Annual_Report_2026.pdf.txt for "per tonne" / "per unit" / "realisation"
found no per-unit rupee figure anywhere in the document.

Comment: NOT DISCLOSED. Reason: the company reports percentage volume
growth (e.g., "Q1FY27 volume +42% YoY," B05 promise_delivery) and
percentage revenue growth, never absolute tonnage or a per-tonne/per-kg
realisation figure, in either the AR or the four concalls. This applies
to both divisions (Industrial and Consumer) as a single basket; no
per-product breakout exists. The volume and revenue lines from which a
figure could in principle be derived, if tonnage were disclosed: FY2026
consolidated revenue Rs 830.03 cr (screener-Data_Sheet, per B01 Block
C); Q1FY27 revenue Rs 307.74 cr (step1-business-brief, Investor
Presentation p.15-16). No absolute tonnage exists in the corpus to
divide by.

### 2. SEGMENT CAPITAL AND DEBT

Quote (Annual_Report_2026.pdf.txt, Note 47, standalone financial
statements, printed page ~134, line 6620-6622; consolidated equivalent
line 9316-9318): "The Company is primarily engaged in the business of
manufacture of rubber chemicals which in the context of Indian
Accounting Standard (Ind AS) 108 on Operating Segments constitutes a
single reportable segment. The relevant information regarding secondary
segment reporting (by geographical segment) is presented as follows:"

Comment: Segment assets, segment liabilities, capital employed, and
borrowings allocated by division (Industrial vs Consumer) are NOT
DISCLOSED, because Ind AS 108 treats the whole company as one reportable
operating segment (B04 flags this explicitly: "Industrial vs Consumer
divisional profitability (margin, ROCE) is not separately audited or
disclosed"). Only geographic secondary-segment revenue is broken out.
Total borrowings are unallocated (single company-wide figure): Rs 557.93
cr, lease-inclusive, FY2026 (B01 Block D, cross-checked to AR Notes
15/16/20/21 total of Rs 55,793.24 lakhs).

### 3. GUIDANCE VERSUS ASPIRATION

(a) Guidance with a stated period (from B05 guidance table, sourced to
named concalls):
- "FY26 revenue INR800-850 cr" — Q2 FY26 call.
- "FY26 EBITDA margin 17-19%" — Q2 FY26 call.
- "Debt-to-EBITDA 3.0-3.5x by FY27" — Q2 FY26 call.
- "WC/inventory days 160-175 by March 2026" — Q2 FY26 call.
- "MNC LTSA plant operational Q4 FY27" — Q2 FY26 call (later revised to
  "commercialisation Q1 FY28," Q3 FY26 call onward, without being
  labelled a change, B05).
- "FY27 capacity utilisation target >75%" — Q4 FY26 call.
- "FY27 capex plan INR250 cr" — Q1 FY27 call (revised up from an
  original INR125 cr, Q4 FY26 call).
- "FY28 revenue >INR1,600 cr" — Q1 FY27 call (revised up from an
  earlier ~INR1,500 cr figure stated at the Q3 FY26 call).
- "Annual revenue growth 30-40%, next few years" — Q1 FY27 call.

(b) Aspiration without a stated period: the "$12-15bn" global addressable
market figure management cited was "given with zero segment/geography
definition" (Aug 2026 concall, per B09 flags) — no period, no basis
stated.

(c) Capacity or capability only, explicitly declined: "New Pakhajan-
building peak capacity (Rs250 Cr FY27 capex) undisclosed - management
explicitly declined to state it (Aug 2026 concall)" (B09 input_gaps).

Comment: The FY28 revenue figure and the 30-40% annual growth figure
rose at every concall across the three quarters tracked, on thinning
multi-quarter proof (B05 red_flags), which is why the credibility grade
sits at B rather than higher (B05 credibility_grade).

### 4. CONCENTRATION

Quote/finding (B04 flags, an absence-of-disclosure finding, cross-
checked against the AR and Investor Presentation text): "No customer-
concentration disclosure (top 1/5/10 customer % of revenue) anywhere in
AR or Investor Presentation, despite risk mitigation language citing
customer diversification."

Comment: NOT DISCLOSED for customer concentration. Product concentration
is disclosed with an internal inconsistency: MD&A states Industrial 89%
/ Consumer 11% (AR printed p.29), while the About Us page states
Industrial 87% / Consumer 13% for the same period (AR printed p.5) (B04
flag). Geography concentration: export/international revenue was 62% at
the Q4 FY26 call and 69% at the Q1 FY27 call, against a management
target of ~70% (B05 promise_delivery row); domestic mix ~31% at Q1FY27
(step1-business-brief).

### 5. PROMISE LEDGER

| Promised in | Promise | Outcome | Evidence anchor |
|---|---|---|---|
| Q2 FY26 call | FY26 revenue INR800-850 cr | Delivered | FY26 actual INR830 cr per Q4 FY26 call (B05) |
| Q2 FY26 call | FY26 EBITDA margin 17-19% | Delivered | FY26 actual 17.4%, low end of band (B05) |
| Q2 FY26 call | Debt/EBITDA 3.0-3.5x by FY27 | Delivered | 3.75x at FY26 close, then 1.86x by Q1 FY27 (B05) |
| Q2 FY26 call | Inventory/WC days 160-175 by March (FY26 year-end) | Missed | 190 days reported at Q4 FY26 call; miss not directly acknowledged (B05) |
| Q2 FY26 call | Export mix ~70% within 6-18 months | Delivered (near, behind interim pace) | 62% at Q4 FY26 (behind pace), 69% at Q1 FY27 (on target) (B05) |
| Q2 FY26 call | MNC LTSA plant operational Q4 FY27 | Partial/slipped | Q3 FY26 call reframes to commercialisation Q1 FY28; not flagged as a change (B05) |
| Q2 FY26 call (implied ~INR100cr FY26 capex) | FY26 capex plan | Partial | Actual INR75 cr; deferred balance citing tariff uncertainty, explained (B05) |
| Q4 FY26 call | WC days 170-175 in 6-12 months | Delivered | 143 days at Q1 FY27, beaten within 3 months (B05) |
| Q4 FY26 call | Debt/EBITDA comfort zone 2.5x | Delivered | 1.86x at Q1 FY27, corroborated by CRISIL/ICRA upgrade to A- (B05) |
| Q4 FY26 call | FY27 volume growth 35-45% | Delivered | Q1 FY27 volume +42% YoY (B05) |

Comment: 7 delivered, 2 partial, 1 missed of 10 tracked promises (B05
promise_delivery: delivered 7, partial 2, missed 1). Credibility grade B
(B05 credibility_grade), tempered by plant-level utilisation withheld
under repeated questioning and the FY28/margin figures rising every
quarter (B05 red_flags).

### 6. RESTATED BASES

Quote (Annual_Report_2026.pdf.txt, Note 55, consolidated financial
statements, printed page ~213, line 6716-6718): "During the current
period, the Company has reviewed the presentation of certain items in
the Statement of Profit and Loss to enhance the relevance and
consistency of financial statement presentation. Consequently, certain
comparative figures relating to the previous period have been regrouped
wherever considered appropriate, to conform to the current period
presentation."

Quote (same note, line 6720-6722): "Such regrouping represents only a
change in presentation and does not affect the total revenue, total
expenses, profit before tax, earnings per share, total comprehensive
income or shareholders' equity for the previous period."

Comment: The company asserts no P&L or equity impact but does not name
which line items were regrouped (B02 restatements_found). The only other
reclassification event in the corpus is the Rajnikant Desai / Kalpana
Desai / HUF promoter-to-public shareholding reclassification (Note
14A(vii)), which carries no accounting P&L or balance-sheet effect (B02
Pass 3 synthesis).

### 7. CORPORATE-ACTION CLAUSES

No scheme, demerger, merger, or buyback appears anywhere in the corpus
(announcements folder empty, B00). The one capital-raising corporate
action found — a Feb-2025 preferential allotment of 6,57,895 shares at
Rs 1,890/share raising Rs 125 cr to Malabar India Fund Limited, Ashoka
India Equity Investment Trust PLC, and WhiteOak Capital ELSS Tax Saver
Mutual Fund — is sourced only to web search at Stage 8 (B08
transition_evidence, MEDIA REPORTED tier), not to a held Reg 30 filing
or shareholder resolution text in the corpus.

Quote (Annual_Report_2026.pdf.txt, Directors' Report, printed page ~30,
line 1487-1489), the one corporate-action-adjacent clause with dates
found directly in the AR text: "Accordingly, Mr. Rajanikant Desai, Mrs.
Kalpana Desai and Rajnikant Desai HUF stand reclassified as a 'Public'
shareholder with effect from February 06, 2026."

Comment: This is a SEBI Reg 31A shareholder-classification change (Board
approval 06-Nov-2025, exchange NOCs 12-Dec-2025, shareholder postal
ballot 09-Feb-2026 per B08), not a scheme/demerger/merger, and carries no
liability-allocation clause. The preferential allotment's own filing
(BSE/NSE Reg 30 announcement, board resolution, and shareholder
resolution/postal-ballot notice) is the document to fetch; it is not in
the corpus (B00 announcements gap).

### 8. RELATED-PARTY PERIMETER

Quote (Annual_Report_2026.pdf.txt, Note 39(A), standalone financial
statements, printed page ~144, line 6256-6279 — "39 RELATED PARTY
TRANSACTIONS / (A) List Of Related Parties Where Control Exists And
Relationships"): the note lists 20 named parties: Mr. Vinod H. Jhaveri
(Promoter & Director), Mr. Parag V. Jhaveri (Promoter & Director), Mr.
Yayesh V. Jhaveri (Promoter & Director), Mr. Dishit P. Jhaveri (Son of
Parag Jhaveri), Ms. Risha Y. Jhaveri (Daughter of Yayesh Jhaveri), Yasho
Industries Europe B.V. (Wholly Owned Subsidiary), Yasho Inc. (Wholly
Owned Subsidiary), Dr. Prakash Bhate / Mr. U. R. Bhat / Mr. Anurag Surana
/ Mrs. Sudha Navandar (Independent Directors), Yayesh V. Jhaveri HUF,
Parag V. Jhaveri HUF, Mrs. Neha Parag Jhaveri (Spouse of Parag Jhaveri),
Mrs. Payal Yayesh Jhaveri (Spouse of Yayesh Jhaveri), Mr. Rajnikant Desai
(Father-in-Law of Yayesh Jhaveri), Mrs. Kalpana Desai (Mother-in-Law of
Yayesh Jhaveri), Rajnikant Desai HUF, Mr. Chirag Shah (CFO), Ms. Rupali
Verma (Company Secretary & Compliance Officer).

Quote (same AR, printed page ~144, line 6240-6262, FY2026 amounts):
"Loans taken from KMP 4,700.01" (Rs lakh, vs Rs 4,850.53 lakh FY2025);
"Trade Payables [to subsidiaries] 974.88" (vs Rs 1,484.95 lakh FY2025);
"Trade Receivables [from subsidiaries] 3,297.05" (vs Rs 1,846.00 lakh
FY2025); "Sales [to subsidiaries] 4,122.79" (vs Rs 3,556.67 lakh
FY2025); "Rent paid 27.13" (vs Rs 29.48 lakh FY2025); "Dividend Paid
13.66" (vs Rs 11.37 lakh FY2025); "Investment in Equity [of
subsidiaries] 42.83" (vs Rs 87.08 lakh FY2025); "Other Payables [to
related parties] 15.94" (unchanged YoY).

Comment: The perimeter is family-and-subsidiary-centred, with the two
wholly-owned foreign subsidiaries as the only non-family, non-KMP
related parties. Interest paid to KMP on the director-loan balance was
Rs 452.88 lakh FY26 (B08, AR line 6230), an effective rate of ~9.6%
against secured bank tranches priced 7.5-8.5%; the AR states all RPTs
are at arm's length (line 6247-6248) but never discloses a contractual
% rate on the director loans (B02 finding 9). The MNC contract itself is
explicitly disclosed as having no promoter/promoter-group interest and
is not treated as an RPT (B08 transition_evidence).

### 9. PLEDGE AND SHAREHOLDING

Quote (Annual_Report_2026.pdf.txt, "Shareholding Pattern as on March 31,
2026," printed page ~30, line 2091-2098): "Indian promoters 81,88,115
67.91 / Sub-total [A] 81,88,115 67.91."

Comment: Promoter holding latest (FY2026 year-end, filed AR basis) =
67.91%. AR FY2025's own shareholding pattern shows 67.99% one year
earlier (B01 Block E). The Q1FY27 Investor Presentation shows 67.94% as
of 30-Jun-2026 (B01 Block E), consistent but presentation-sourced, not a
filing. A full 12-quarter series is NOT DISCLOSED. Reason: no
shareholding-pattern filing folder is populated in this corpus (B00
gap); only these three points exist — AR FY2025 (67.99%), AR FY2026
(67.91%), and the Q1FY27 presentation (67.94%) — a 1-year filed window
plus one presentation-sourced quarter, not the 3-year window Gate 0
otherwise needed (B01 E2 input gap, marked N/A rather than estimated).

Pledge: no promoter-share pledge or encumbrance disclosure was found
anywhere in the AR FY2026 full-text search on "pledge"/"encumb" (B01 E3)
— an absence-of-disclosure inference read as 0%, not an explicit stated
percentage. B08's web-search-sourced finding corroborates 0% pledge,
"stable... via the FY26 Reg 31(4) filing" (B08 pledge_pct_latest,
pledge_trend), but that Reg 31(4) filing itself is not held in this
corpus (MEDIA REPORTED tier, not primary).

Institutional holding, latest (30-Jun-2026, Investor Presentation p.18-
19 per B00 folder inventory, presentation-sourced not a filing):
Promoters 67.94%, Public 24.11%, FII 5.74%, DII 2.21%.

### 10. VERIFICATION

Documents quoted in this annex: Annual_Report_2026.pdf.txt (FY2026
audited, standalone Notes pp.108-155, consolidated Notes pp.168-215,
Directors' Report/MD&A pp.1-55 region, Shareholding Pattern p.30 region)
— corpus file inputs/annual-report/Annual_Report_2026.pdf.txt. Concall
transcripts referenced by finding (not directly re-quoted verbatim in
this annex beyond what B05 already anchored): Concall_Nov_2025_
Transcript.pdf.txt (Q2 FY26), Concall_Feb_2026_Transcript.pdf.txt (Q3
FY26), Concall_May_2026_Transcript.pdf.txt (Q4 FY26), Concall_Aug_2026_
Transcript.pdf.txt (Q1 FY27). Investor_Presentation_1.pdf.txt (Q1FY27,
filed 31-Jul-2026), referenced via B00/B01/B04 for presentation-sourced
figures (pp.12, 15-19 region), not independently re-opened this stage.
Stage reports drawn on for citation and quote retrieval: 00-inputs.md,
01-gate0.md, 02-notes.md, 03-ardeep.md, 04-bizmodel.md, 05-concall.md,
06-peers.md, 07-emoat.md, 08-promoter.md, 09-tam.md, and verifier
reports 12a-12d.

CORPUS COMMIT HASH: 016a7caf9f05bdf62aa29b63873ce00308011e49
