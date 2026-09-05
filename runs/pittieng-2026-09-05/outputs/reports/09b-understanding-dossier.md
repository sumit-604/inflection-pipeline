# HALT 1 UNDERSTANDING DOSSIER: Pitti Engineering Ltd (PITTIENG)

Run: pittieng-2026-09-05 | Run date: 2026-09-05 | Stage: 09b (assembly only, no new research)

This dossier assembles what stages B00-B09 and the phase-1 verifiers (B12a/B12b/B12c-partial/B12d)
already found. It states no price, no exit multiple, and no verdict. It is the package the operator
reads at Halt 1 to decide what happens next.

---

## SECTION 1: CORPUS COMPLETENESS AUDIT

**1. CONCALLS.** Four transcripts held: Q2 FY26 (Concall_Nov_2025_Transcript.pdf, call 10-Nov-2025,
passed to stage 7 and verifier B as extra, not one of the three primary quarters), Q3 FY26
(Concall_Feb_2026_Transcript.pdf, call 6-Feb-2026), Q4 FY26 (Concall_May_2026_Transcript.pdf, call
18-May-2026), Q1 FY27 (Concall_Aug_2026_Transcript.pdf, call 11-Aug-2026) (B00). The most recent
quarter covered is Q1 FY27 (quarter ended 30-Jun-2026). Against the 2026-09-05 run date, Q2 FY27
(quarter ending 30-Sep-2026) has not yet closed, so no more-recent quarter's transcript is plausibly
missing.

**2. ANNUAL REPORTS.** Only one year is held: FY2025-26 (Annual_Report_2026_2.pdf, 130 PDF pages,
filed 24-Aug-2026) (B00). This is the latest completed FY and it is present. Fewer than 3 years are
held; B03 and B08 both name "only one AR year in corpus" as a standing gap that limits every
multi-year trend read in this run to whatever the FY26 AR's own two-year comparatives carry.
Annual_Report_2026.pdf in the same folder is a 2-page weblink letter, not an AR, and was not used
(B00, B03).

**3. RESULTS FILINGS.** ABSENT. The results/ folder is empty for every quarter, including the three
quarters the concalls cover (B00, B01). FY26 audited results and the Q1 FY27 quarter are known only
through the investor presentation, the concalls, and the screener quarters row, never through a
results PDF itself (B00). No quarter-gap exists between the latest results reference (Q1 FY27, via
the concall and presentation) and the latest AR (FY26); the gap is a missing document type, not a
missing period.

**4. INVESTOR PRESENTATIONS.** One held: Q1 FY27, filed 10-Aug-2026, 30 slides
(Investor_Presentation_1.pdf) (B00). Prior-quarter presentations (Q2/Q3/Q4 FY26) are not in the
corpus.

**5. RESEARCH / RATING.** ABSENT as filed documents; the research/ and rating/ folders are both empty
(B00). A rating grade is nonetheless named inside the AR itself: India Ratings IND AA-/Stable / IND
A1+ on bank facilities (Corporate Governance Report, AR FY26, PDF p.54, per B03). The full rating
rationale document that would explain this grade is not in the corpus.

**6. CORPORATE ACTIONS.** No exchange announcement/Reg 30 filing PDFs are held; the announcements/
folder is empty (B00, B01). The substance of several corporate actions during the review period is
nonetheless disclosed inside the AR's own Directors' Report and notes: the July-2024 QIP, the
PCPL/PRECL share-swap merger made effective 24-Oct-2024, and the PIPL/DFPL merger scheme (board
approval 5-Feb-2026, NCLT dispensation order 10-Apr-2026, appointed date 1-Apr-2026) (B03, B08).
These are AR-sourced facts about the actions, not the underlying exchange filings themselves.

**7. FRESHNESS PAIR CHECK.** Per B00's `freshness_verdict` (FRESHNESS PAIRS OK) and `freshness_pairs[]`,
all four pairs PASS: results-to-concall (no results doc ingested to trigger the check), rating
bulletin-to-rationale (no rating bulletin ingested), SEBI order-to-text (no order referenced), and
AR-to-latest-audited-annual (the FY26 AR matches the FY26 audited results referenced on the Q4 FY26
call). No pair failed.

Verifier confidence components (read for evidence-quality facts only, per confidence.yaml): numerical
acceptance 98.1, red-flag coverage 30, framework adherence 92 (the Gate 0 and Emerging Moat portion;
the valuation portion is pending a later stage), peer utilisation 100.

**8.** CORPUS GAPPED: findable-but-missing, namely quarterly results PDFs for Q2 FY26 through Q1 FY27
(expected source: BSE/NSE exchange filings or the company IR page); the full India Ratings rationale
behind the IND AA-/Stable / IND A1+ grade named in the AR (expected source: India Ratings' own site or
the company IR page); Reg 30 announcement PDFs for the QIP, the PCPL/PRECL scheme, the PIPL/DFPL NCLT
scheme, and the Rs 290 Cr capex board approval (expected source: BSE/NSE); quarterly Shareholding
Pattern (Reg 31) filings across the last twelve quarters, including any promoter-pledge disclosure
(expected source: BSE/NSE); prior-year annual reports FY22 through FY25 (expected source: company IR
page or the BSE filing archive); prior-quarter investor presentations for Q2 through Q4 FY26 (expected
source: company IR page). Plausibly-nonexistent, not merely unfiled: a rupee-denominated product-line
revenue split (laminations vs castings vs machined components), a named-competitor disclosure, any
third-party market-share corroboration of the "largest manufacturer" claim, and a CGU-level goodwill
impairment note are all absent from the one AR this run does hold, which is itself evidence of a
disclosure choice the company makes rather than only a document this run failed to collect (B02, B04,
B07). The rest of this dossier calls this finding "the verdict above."

---

## SECTION 2: MENTAL MODEL DECLARATION

**DRAFT - PENDING OPERATOR SIGN-OFF**

### PART A: THE FROM STATE (the anchor, not the model)

**A1. Archetype.** Pitti is not one archetype; B04 names the split as the single most load-bearing
finding for downstream stages (B04's archetype-split finding). Loose laminations and raw castings
behave as a COMMODITY CONVERTER (Section 1B Amendment 17 binds this slice only); value-added
assemblies and machined components behave as a BUILD-TO-SPEC COMPONENT MAKER (B04). No document gives
the rupee split between the two slices, only physical-volume proxies showing the build-to-spec share
growing faster (value-added lines +21.8% to +37.1% volume versus slower loose-lamination growth) (B04).

**A2. The simple analogy.** Pitti turns electrical steel, iron and steel scrap into the laminated
metal discs, castings and machined shafts that sit inside a motor, generator or locomotive: the part
that spins and carries current, not the finished machine itself (B04, AR PDF p.7, p.11). Some of what
it sells is a plain commodity, cut and stamped sheet that anyone with a stamping mill could make; the
company's own words call this tier "engineering commodities" (B04, AR PDF p.11). Increasingly it welds,
machines and assembles that sheet into a near-finished part before it ships, which earns more per
tonne and is harder for a customer to walk away from once that customer has spent years testing and
approving it (B04). Buyers are equipment makers across railways, power generation, industrial motors,
mining, renewables and data centres, not consumers (B04, AR PDF p.7-8).

### PART B: THE TRANSITION (the model)

Two lines transition differently, per the archetype split in A1 (CLAUDE.md QUALITY LADDER rungs).

**Line 1: loose laminations & raw castings (the converter slice).**
- **B1. From-to.** FROM R1 COMMODITY PRICE-TAKER (no pricing power, cost-of-capital-adjacent ROCE) TO
  R2 COST-ADVANTAGED CONVERTER (margin from cost position and scale, not price, with durable mid-teens
  ROCE) (CLAUDE.md; B01, B04).
- **B2. The engine.** Fixed-cost absorption from rising utilisation (76% sheet metal, 81% machining,
  71% casting, FY26, AR PDF p.4) and a stated quarterly steel-price pass-through mechanism, defending
  a cost position rather than earning a spec premium (B04, AR PDF p.20).
- **B3. The proof gate.** Adjusted EBITDA margin on the blended base holds at or above roughly 15-18%
  through a full steel-price cycle even without help from the value-added mix shift (B04
  must_track_metrics); the company does not disclose this slice separately, so the gate cannot yet be
  tested at the slice level on its own (B04 input_gaps).
- **B4. The recognition gap (open question, resolved at Stage 11).** Whether the market already prices
  this slice as a durable cost-advantaged converter, or still prices it as a plain cyclical
  price-taker, is not concluded here; Stage 11 resolves it via the destination-multiple gap.
- **B5. The ugliness test.** The FY26 inventory build (+20.0% consolidated) that partly funds this
  slice's steel buffering reads as ARTIFACT-OF-CLIMB: management states plainly that the cost of
  carrying extra inventory against an electrical-steel supply shortfall is "the price of dependability"
  (AR PDF p.4, per B03 4C), a deliberate, owned choice rather than a sign of decay.
- **B6. The transition falsifier.** Adjusted EBITDA margin falls back toward or below the FY23 level of
  roughly 13.8% while utilisation stays high, showing the cost position itself has eroded, not just
  cycled (B04 must_track_metrics red-flag threshold).

**Line 2: value-added assemblies & machined components (the build-to-spec slice).**
- **B1. From-to.** FROM R2 COST-ADVANTAGED CONVERTER TO R3 VALUE-ADDED / SPEC'D SUPPLIER (spec-in and
  switching costs giving partial pricing power, ROCE in the 20-25% band with stickiness) (CLAUDE.md;
  B01, B04).
- **B2. The engine.** The OEM "Qualify-Deliver-Expand-Integrate" qualification cycle (AR PDF p.15) plus
  the Rs 290 Cr castings/machined-components capex on top of the ongoing Rs 150 Cr brownfield
  programme, aimed at named-OEM demand (Caterpillar, Voith, Progress Rail, Siemens Mobility, Medha
  Servo) (B03, B04, AR PDF p.14).
- **B3. The proof gate.** Two legs, both must hold: value-added tonnage keeps rising as a share of total
  volume quarter over quarter, AND the realisation premium per tonne over loose lamination does not
  keep narrowing. The premium has already narrowed from roughly 1.47x to roughly 1.29x between the Q2
  FY26 and Q4 FY26 calls, an independently-found risk to this gate (B12b MAJOR finding), so the gate
  has not fired cleanly as of this run.
- **B4. The recognition gap (open question, resolved at Stage 11).** Whether the market already prices
  the value-added mix shift as delivered, leaving only earnings growth to carry forward, or still
  prices Pitti as the plain converter it was, is an open question Stage 11 resolves via the
  destination-multiple gap; this dossier states no number and no conclusion.
- **B5. The ugliness test.** The FY26 net-debt rise (+26.3% consolidated) and the working-capital-days
  rise (54.85 to 68.31, FY25 to FY26) sit mostly on this slice, since it funds the capex programme
  (B01, B02). Read as ARTIFACT-OF-CLIMB on balance: CWIP ageing is clean with nothing over two years
  (B02), CFO stayed strongly positive (Rs 204.91 Cr, CFO/PAT 1.74x, B03), and the FY26 PAT dip traces to
  a tax-timing reversal, not an operating problem (B02 finding 1). That read is contested, not settled:
  the original inventory/net-debt normalisation promise has been missed and restated across three
  consecutive calls (B05, B12b), and consolidated ROCE has fallen for three straight years (18.39% FY24
  peak to 13.75% FY26, B01) with what B12b calls a serial-capex drag with no stated exit. The
  operator should treat the ARTIFACT read as the better-evidenced one today, not as a closed question.
- **B6. The transition falsifier.** Value-added tonnage share stops rising relative to loose-lamination
  volume for two consecutive quarters, or the Rs 290 Cr capex commissioning slips beyond Q1 FY30, or the
  realisation premium keeps narrowing toward parity with loose-lamination pricing (B04
  first_deterioration_signals; B12b).

### PART C: WHAT THE MODEL WATCHES (derived from the transition)

**C1. Dominant variables.**
1. Value-added tonnage mix share and the realisation premium per tonne over loose lamination: rising in
   volume, but the premium has narrowed from roughly 1.47x to roughly 1.29x (B04, B12b).
2. Consolidated net debt and the working-capital glide path toward the company's own repeatedly
   restated inventory/net-debt normalisation path: still rising through FY26, missed against its
   original schedule (B02, B03, B05).
3. Rs 290 Cr castings/machined-components capex execution and its commissioning date: Q1 FY30 per the
   AR and all three concalls, Q1FY29 per one presentation slide, unresolved; named-OEM demand
   visibility is not yet backed by any disclosed firm order figure (B03, B04).
4. Consolidated ROCE trend: 18.39% FY24 peak to 13.75% FY26, three straight years of decline; B12b
   treats this as a presently unresolved, high-severity risk to the transition thesis rather than the
   lower severity B05 first assigned it (B01, B05, B12b).

**C2. What the model rejects.** Market-size questions are not the binding constraint here: B09's own
sizing shows years of headroom at the present pace (a runway class read as GOOD, revenue headroom of
roughly 6.3x current revenue, B09), and management's most visible market-size citation (a global
railroad market figure) is a whole-of-industry number roughly 130 times this run's own conservative
component-level sizing, never tied by management to Pitti's own addressable slice (B09 finding on the
market-claim breadth). The model treats "is the market big enough" as noise; the binding questions are
execution questions (mix, debt, capex timing, ROCE), named in C1.

**C3. The business falsifier.** Distinct from the transition falsifier (B6 above, which kills the
climb): any of the following would force a re-declaration of the underlying manufacturing business
itself. Capacity utilisation falling below 60% across sheet metal, machining or casting for two or
more quarters while new capex is still being committed (B04 must_track_metrics); the loss of one of
the two unnamed customers making up 25.2% of consolidated revenue (B02, Note 25.6c); or a CGU-level
impairment charge against the Rs 136.09 Cr goodwill (13.79% of consolidated net worth) signalling that
the acquired subsidiary businesses behind roughly a fifth of consolidated revenue are not sound (B02
finding 6).

---

## SECTION 3: BUSINESS UNDERSTANDING NARRATIVE

Pitti Engineering makes the electrical-steel laminated cores, iron and steel castings, and machined
shafts, gear cases and housings that sit inside a motor, generator or locomotive, then increasingly
welds and assembles them into a near-finished part before it ships (B04). Traction motor and railway
components are the largest single stream at 33% of FY26 revenue, followed by power generation at 15%
and industrial and commercial motors at 13% (B04, AR PDF p.8); a customer cannot easily switch away
from a qualified part because the OEM has spent years testing, auditing and validating that specific
supplier's output before approving it for use (B04, AR PDF p.15). Buyers are equipment makers, not
consumers: Indian Railways production units and global rail original-equipment makers, generator and
alternator makers, industrial-motor makers, mining and off-highway equipment makers, and data-centre
backup-power makers (B04). Individually named counterparties appear mostly through demand-visibility
and award disclosures rather than through a stated revenue share: Caterpillar, Voith, Progress Rail,
Siemens Mobility and Medha Servo are named as the demand behind the new Rs 290 Cr capex (B03), and
Wabtec appears only as a past award-grantor and a 2017 deal reference, never as a named source of a
current revenue percentage (B04). Two unnamed customers make up 25.2% of consolidated revenue and
three unnamed customers make up 40.7% of standalone revenue, a real concentration the company
discloses only in aggregate (B02, Note 25.6c). Present demand rests on international rail and metro
programmes offsetting a domestic railway capex environment the AR itself calls "moderated" this year,
on a China-plus-one/global-diversification tailwind, and on an early-stage data-centre backup-power
stream that added two new clients in FY26 (B04, B09). B09's own downstream candidates tie this demand
to externally checkable series: Indian Railways production-unit output counts, named global rail OEMs'
own capex and order intake, Caterpillar and Cummins power-systems shipment data, and India data-centre
capacity-addition trackers (B09). Forward demand should grow on the same names plus Union Budget
railway-capex allocations and CEA/MNRE generation-capacity data, though management's own broadest
market-size citation, a global railroad-market figure, is a whole-of-industry number roughly 130 times
this run's own component-level sizing and is never tied by management to Pitti's own addressable slice
(B09). Competitive advantage sits only on the value-added and machined-component lines, where the OEM
qualification barrier gives moderate-to-high switching-cost protection and where B07's emerging-moat
scan finds six categories at Moderate or better, all clustering around the same mix-shift and
customer-widening story rather than sitting as independent sources of advantage (B04, B07). It does
not sit on the loose-lamination and raw-casting lines, which the company's own materials call
"engineering commodities" and which compete on cost position and utilisation, with no brand, patent,
network effect or licence behind them anywhere in either primary document (B04). The one marketed
capability claim on this front does not hold up against the company's own statutory disclosure: an
investor-presentation slide markets "R&D and Tooling Expertise," while the AR's own Technology
Absorption annexure states research and development effort and expenditure were both "Nil" for the
year (B07, AR PDF p.29).

---

## SECTION 4: DOWNSTREAM DOSSIER

### 4a. Verticals framed (one per Section 2 Part C1 dominant variable)

**Vertical 1: value-added tonnage mix and realisation premium.** The corpus establishes physical
volume growth by product tier (value-added assemblies +21.8%, shaft/stator-frame assemblies +31.9%,
versus slower loose-lamination growth, B04, AR PDF p.4) and an independently found narrowing of the
per-tonne realisation premium, from roughly 1.47x to roughly 1.29x over loose lamination between the
Q2 FY26 and Q4 FY26 calls (B12b). It cannot establish the rupee revenue split between commodity and
value-added output (NOT FOUND in either primary document, B04), nor a per-tonne margin figure by tier
(NOT FOUND, B04). Open questions: (1) What is the rupee, not tonnage, split between loose laminations,
value-added assemblies, castings and machined components? (2) Is the narrowing premium a steel-price
pass-through timing effect or a genuine competitive squeeze on the value-added tier? (3) Does per-tonne
profitability on the value-added tier keep rising even as the premium narrows?

**Vertical 2: net debt and working-capital glide path.** The corpus establishes that consolidated net
debt rose 26.3% in FY26 (B02), that inventory rose 20.0% while TReDS-financed payables nearly doubled
(B02), and that management has stated, missed and re-based the same normalisation promise across three
consecutive calls (B05, B12b). It cannot establish whether the promised H1 FY27 release actually
materialises, since that falls in a quarter this corpus does not yet cover, and it cannot establish
whether the TReDS-embedded payables balance keeps growing beyond the Rs 83.85 Cr already disclosed
(B02). Open questions: (1) Does net debt fall sequentially in Q1/Q2 FY27? (2) Does the TReDS balance
keep growing? (3) Is the BIS Korea/Japan steel-supply position genuinely easing, given that B06 found
a peer's own call evidence contradicts, not confirms, that reading?

**Vertical 3: Rs 290 Cr capex execution and commissioning date.** The corpus establishes real FY26
execution: gross PP&E additions of Rs 175-200 Cr with a clean CWIP-ageing profile (B02), and a
named-OEM demand-visibility disclosure in the AR itself (B03). It cannot establish any firm purchase
order or order-book figure behind the five named OEMs (B03, B04), a single cumulative capex-programme
total (B02), or which of two stated commissioning dates is correct: Q1 FY30 per the AR and all three
concalls, or Q1FY29 per one investor-presentation slide (B04). Open questions: (1) Which commissioning
date is correct? (2) Is there a firm order or order-book figure behind the named-OEM demand visibility?
(3) What is the combined rupee total of the Rs 150 Cr and Rs 290 Cr programmes together?

**Vertical 4: consolidated ROCE trend.** The corpus establishes ROCE fell from an 18.39% FY24 peak to
13.75% in FY26 (B01), a decline B12b treats as an unresolved, high-severity risk rather than the lower
severity first assigned (B05 originally, B12b's correction). It cannot establish whether ROCE
stabilises once the new capacity reaches the company's own disclosed 1.0x-1.2x asset-turn figure at
full ramp-up, since no interim milestone or date is given for that figure (B04, AR PDF p.14). Open
questions: (1) Does ROCE stabilise or keep falling through FY27-28? (2) What specific capex-ramp
milestone would management point to as the floor? (3) Is B06's cross-peer read fair, that Pitti's
debt-funded capex pattern sits closer to one peer's margin-compressing playbook than to the two peers
that funded growth from internal cash?

### 4b. Candidate signal table (expanded from B09 SECTION 6, unverified, for Role 5.5 verification)

| Candidate Signal | Draft Falsifier | Draft Cadence | Likely Source |
|---|---|---|---|
| Indian Railways production-unit (CLW/ICF/BLW) rolling-stock and traction-equipment output counts | Output counts flat or falling for two-plus consecutive quarters while Pitti's own railway revenue share also keeps falling | Quarterly | Ministry of Railways Annual Report / Indian Railways Production Unit statistics |
| Global rail OEM capex, order intake and delivery counts (Wabtec, Alstom, Siemens Mobility, Progress Rail) | Named OEMs' own capex/order commentary shows deceleration despite Pitti's claim of a widening customer roster | Quarterly | Company quarterly filings / earnings calls (Wabtec, Alstom, Siemens Mobility) |
| Caterpillar and Cummins power-systems/genset segment shipment data | Shipment growth stalls or reverses for two-plus quarters while Pitti's data-centre/power-gen revenue share is still guided up | Quarterly | Company quarterly filings (Caterpillar, Cummins segment reports) |
| India data-centre capacity addition trackers | Tracked capacity additions flatten or fall while Pitti's data-centre revenue share is still guided up | Quarterly | CBRE India / JLL India Data Centre Market reports |
| CEA monthly generation-capacity-addition report and MNRE renewable-capacity data | Monthly additions plateau while Pitti's power-generation/renewables revenue share is still guided up | Monthly | Central Electricity Authority monthly executive summary; MNRE |
| DGCIS import-volume data for CRNGO electrical steel and the BIS approved-producer licence list | Import volumes or the licence count shrink (tightening the input deficit) while Pitti's own inventory/working-capital case assumes supply keeps easing | Monthly | DGCIS; Bureau of Indian Standards licence database |
| Union Budget railway capex allocation and PIB rail-infrastructure updates | The next Union Budget railway capex allocation is flat or cut while Pitti's railway growth case leans on international, not domestic, programmes to offset a "moderated" domestic environment | Event-driven | Union Budget documents (Ministry of Finance); PIB India Portal |

### 4c. Fragility read

- **variable_count:** 4 (the Section 2 Part C1 dominant variables).
- **verifiability_ratio:** 2 of 4 externally observable from filed financial statements (the net-debt/
  working-capital path via quarterly BSE filings once results resume, and ROCE via the financial
  statements themselves); the other 2 of 4 (the value-added tonnage/realisation-premium disclosure, and
  firm-order backing for the Rs 290 Cr capex) are presently company-narrated only, since no filed
  rupee-level product split or purchase-order figure exists (B04, B03).
- **single_point_failure:** none named that alone breaks the transition thesis by conjunction rule; the
  nearest single-name exposure is customer concentration (two unnamed customers at 25.2% of
  consolidated revenue), which this dossier carries separately as the Part C3 business falsifier rather
  than as a transition kill-switch (B02).
- **fragility_verdict:** FRAGILE. Half the dominant variables are told only by the company itself, the
  concall credibility grade is C (B05), and an independent re-check found 2 CRITICAL and 18 MAJOR
  items, several of them under-weighting risk on exactly these same variables (net debt/inventory
  normalisation missed three times, the ROCE decline, the narrowing value-added premium) (B12b).

### 4d. Research brief (live-web work for claude.ai; not doable from this corpus)

1. Locate the primary BSE Reg 29(2)/31 filing for the 12-Dec-2024 Akshay Pitti share sale, presently
   known only through two secondary aggregators (B08).
2. Confirm the twelve-quarter promoter shareholding and pledge trend from BSE Shareholding Pattern
   filings; the AR carries only a single 31-Mar-2026 snapshot (B03, B08).
3. Obtain the independent valuer/fairness-opinion detail for the PCPL/PRECL share-swap merger into the
   listed company; the AR confirms a share-exchange ratio was approved and 21,88,772 shares were
   allotted, without stating the ratio itself or naming a valuer (B08).
4. Verify active/struck-off status for the un-corroborated promoter-family private entities (Hyderabad
   Lamination & Stamping, Pitti Components Ltd, Pitti Holdings Pvt Ltd, Akshva Ispat Pvt Ltd, Aa Plus
   Infotech Pvt Ltd, Uttaranchal Metal Powder Pvt Ltd, Pitti Trade and Investment Pvt Ltd) via MCA/
   Zaubacorp (B08).
5. Find the reason for the simultaneous September-2024 exit of three independent directors plus one
   non-independent director; it falls outside this run's single-AR corpus (B08).
6. Directly check whether BIS-certified electrical steel from Korean and Japanese mills is now reliably
   available; B06 found a peer's own call evidence contradicts, not confirms, Pitti's reading.
7. Obtain the full India Ratings rationale behind the IND AA-/Stable / IND A1+ grade named in the AR
   (B00, B03).
8. Verify whether a firm purchase order or order-book figure exists behind the five named OEMs cited as
   demand visibility for the Rs 290 Cr capex (B03, B04).
9. Check the latest exchange filings or results for the Q1/Q2 FY27 net-debt and working-capital trend
   against the company's own repeatedly restated glide path (B00).
10. Cross-check the identity of the two or three unnamed customers behind the 25.2%/40.7% revenue
    concentration via any available counterparty-side disclosure (B02).
11. Confirm the correct Rs 290 Cr capex commissioning date, Q1FY29 per one presentation slide or Q1
    FY30 per the AR and all three concalls, via a direct exchange filing or an updated presentation
    (B04).
12. Check for any CGU-level goodwill impairment disclosure or independent commentary on the Rs 136.09
    Cr goodwill (B02).

---

## SECTION 5: PLAIN-LANGUAGE SUMMARY

1. Pitti Engineering makes the metal parts that go inside motors, generators and locomotives, not the
   finished machine itself.
2. It stamps electrical steel into laminated cores, casts iron and steel, and machines shafts, gear
   cases and housings.
3. It is climbing from selling simple stamped sheet toward selling finished, assembled parts that earn
   more per tonne.
4. Its buyers are equipment makers, not consumers: Indian Railways production units, global rail
   companies, generator makers, industrial-motor makers, mining-equipment makers and data-centre
   backup-power makers.
5. Buyers must test and approve a part before they use it, a process that can take years, so once a
   customer signs off, it tends to stay.
6. Two or three unnamed customers make up between a quarter and two-fifths of revenue, depending on
   which set of accounts is read.
7. Demand is supported by railway and metro programmes abroad, a China-plus-one diversification
   tailwind, and new data centres, even as domestic railway capex "moderated" this year.
8. The company's own market-size checks show years of room to grow into at the present pace.
9. The edge sits in the newer, harder-to-make parts: the customer-approval process there keeps out new
   entrants and keeps existing customers in place.
10. The edge does not sit in the older, simpler parts, which compete on cost position with no brand, patent
    or licence behind them; the company's own marketed research-capability claim is contradicted by its
    own statutory filing, which states research spending and effort were both nil this year.
11. The mental model is a climb up the quality ladder, funded by two capex programmes and a shift in
    what gets sold, not yet complete.
12. On this run's own evidence, the case depends on several things moving together, and half of them
    are still told only by the company itself, not by any outside filing.
13. This run's documents cannot say the rupee split between commodity output and value-added output,
    only the tonnage split.
14. This run's documents cannot say which of two stated dates the new plant actually finishes on, nor
    who the concentrated customers actually are.
15. The two questions that matter most next: does the promised debt and inventory reduction actually
    show up in the next two quarters, and does the value-added product keep earning a bigger premium
    per tonne, since that premium has already narrowed once.

---

## SECTION 6: STANDING EXTRACTION ANNEX

**1. UNITS.** Quote: "Consolidated lamination and assembly volumes grew 10.3% to 69,517 tonnes, while
high value-added assemblies grew 21.8%... Casting and machined component volumes rose 15.4% to 12,012
tonnes." (Annual_Report_2026_2.pdf, PDF p.4). Comment: this covers physical volume across the whole
lamination/assembly basket and the whole casting/machined basket, not one product. No company-disclosed
rupee-per-tonne figure exists anywhere in the corpus for either basket. A blended figure can be derived
only by dividing consolidated "Revenue from operations" (Rs 1,91,280.36 lakh, Annual_Report_2026_2.pdf,
PDF p.114, Note 25.6a) by the combined tonnage above, which masks a wide spread since the AR itself
states value-added tiers earn a higher realisation per tonne than loose laminations (B04). A tier-level
figure does exist for one slice, from a concall, not a filing: "INR80,000 to INR1 lakh per ton" for
machine castings' EBITDA and "INR30,000, INR35,000 per ton" for raw castings' EBITDA
(Concall_May_2026_Transcript.pdf, PDF p.20). Comment: this is a profitability-per-tonne figure for one
sub-tier, not a revenue-per-tonne figure, and not a company-audited disclosure.

**2. SEGMENT CAPITAL AND DEBT.** Quote: "The operating segment of the Group is identified to be
manufacturing of 'Engineering Products of Iron and Steel' and the CODM reviews business performance at
an overall Group level as one segment. Hence no separate disclosure is provided."
(Annual_Report_2026_2.pdf, PDF p.83 standalone / PDF p.114 consolidated, Note 25.6). Comment: no
segment-level capital-employed or borrowings breakdown exists anywhere in the corpus; only a
geography split for revenue and assets is given. Quote (assets, geography split): "TOTAL 2,05,603.93"
lakh standalone and "TOTAL 2,13,777.93" lakh consolidated, both as at 31st March 2026
(Annual_Report_2026_2.pdf, PDF p.83 standalone / PDF p.115 consolidated, Note 25.6b). Borrowings are
not allocated by segment; the total is quoted instead. Quote: "Closing Balance 69,884.67" lakh (as at
31st March 2026) against "Closing Balance... 57,844.68" lakh (as at 31st March 2025), consolidated
Note 10A/13A (Annual_Report_2026_2.pdf, PDF p.108). Comment: Rs 698.85 Cr FY26 versus Rs 578.45 Cr
FY25, an identical figure standalone and consolidated per B03, confirming zero subsidiary-level
external debt.

**3. GUIDANCE VERSUS ASPIRATION.**
(a) Guidance with a stated period. Quote: "If I start from current year, I would look at an EBITDA of
roughly ₹370-odd crores based on current outlook. For the next year, we should be looking at a turnover
above about ₹2,500 crores if we don't do the Capex... at a 90,000 ton operating level, we should be
looking at a ₹2,500 crores turnover and an EBITDA margin of about 17%-17.2%." (Concall_Aug_2026_
Transcript.pdf, PDF p.16, Akshay S. Pitti). Comment: this is Company Memory's load-bearing fact 1,
confirmed here as dated guidance on the Q1 FY27 call; it does not appear anywhere in the FY26 AR
itself (B03). Quote: "we had approximately INR500 crores worth of inventory, and we expect this
inventory to go down to our historic levels of about INR300 crores worth of inventory. So, about a
INR200 crores reduction in raw material is what we are looking at over the next 3 months."
(Concall_Feb_2026_Transcript.pdf, PDF p.7, Akshay Pitti). Comment: an inventory figure with a period
(by roughly April 2026), not a net-debt figure; missed against its own schedule per the promise ledger
(B05). Quote: "Planned for commissioning by Q1 2029-30, the expansion will increase casting capacity to
36,000 MT and machining capacity to 10.8 Lakh machine hours." (Annual_Report_2026_2.pdf, PDF p.14)
against "expected to commissioned by Q1FY29" (Investor_Presentation_1.pdf, PDF p.11). Comment: two
different dated commissioning claims for the same Rs 290 Cr programme from two primary sources this
run holds, unreconciled by either document (B04).
(b) Aspiration without a firm period. Quote: "we expect a meaningful release of working capital by end
of H1 2026-27. Combined with internal accruals, this release will..." (Annual_Report_2026_2.pdf, PDF
p.4). Comment: a qualitative release claim tied to a half-year, not a number; FY26's own year-end
figures move the opposite direction from this claim (B02, B03).
(c) Capacity or capability only. Quote: "At full ramp-up, the expanded capacity is expected to deliver
asset turns of 1.0x to 1.2x." (Annual_Report_2026_2.pdf, PDF p.14). Comment: no date is attached to
"full ramp-up," so this is a capability figure, not guidance with a period.

**4. CONCENTRATION.** Quote: "Revenue from three customers of the Company, having more than 10% of the
total revenue aggregating to ₹64,746.24 lakhs (previous year two customers ₹68,792.97 lakhs)."
(Annual_Report_2026_2.pdf, PDF p.83, standalone Note 25.6c). Quote: "Revenue from two customers of the
Group, having more than 10% of the total revenue aggregating to ₹48,173.62 lakhs (previous year two
customers ₹68,792.97 lakhs)." (Annual_Report_2026_2.pdf, PDF p.115, consolidated Note 25.6c). Comment:
against the segment-note revenue totals in question 2, this is 40.7% of standalone revenue and 25.2%
of consolidated revenue, falling year on year on both bases (B02); no customer name or end-market label
is attached to either figure anywhere in the corpus. Product and geography concentration: revenue is
disclosed only by end market (33% Traction/Railways, the largest line, AR PDF p.8) and by geography
(India versus Outside India, same Note 25.6 tables above), never by product type in rupees (B04).

**5. PROMISE LEDGER.**

| Promise (date made) | Delivery status | Evidence anchor |
|---|---|---|
| FY26 revenue Rs 1,900-2,000 Cr (Q3 FY26 call) | Delivered | Actual Rs 1,953 Cr (Concall_May_2026_Transcript.pdf, per B05) |
| Rs 150 Cr capex fully operational by end FY27 (Q3 FY26 call) | Delivered | Sheet metal capacity 108,000 t confirmed (Concall_Aug_2026_Transcript.pdf, per B05) |
| Casting debottleneck to ~24,000-24,600 t by H1 FY27 (Q3/Q4 FY26 calls) | Delivered | Confirmed at 24,000 t (Concall_Aug_2026_Transcript.pdf, per B05) |
| Inventory Rs 500 Cr to Rs 300 Cr by April 2026 (Q3 FY26 call, quoted above) | Missed | Actual ~Rs 390-400 Cr as of the Q4 FY26 call; reframed rather than acknowledged (B05) |
| Net debt to fall via BIS Korea/Japan steel deals (Q3 FY26 call) | Missed near-term | Rose to ~Rs 570 Cr (Q4 FY26 call) before falling to ~Rs 491 Cr (Q1 FY27 call), short of the interim marker given (B05) |
| FY27 EBITDA margin ~17% +/-50bps (Q3 FY26 call) | Missed | Q4 FY26 actual 16.6%, Q1 FY27 actual 16.8% (B05) |
| Tax rate ~33% "at least a couple of years" (Q4 FY26 call) | Reversed | Revised to ~25% three months later without reconciling the prior claim (Concall_Aug_2026_Transcript.pdf, per B05) |
| Net debt ~Rs 250 Cr by FY28/29 ex-capex (Q4 FY26 call) | Softened | Management declined to reaffirm a number when asked again (Concall_Aug_2026_Transcript.pdf, per B05) |
| Maharashtra subsidy start, open FY27-or-FY28 (Q4 FY26 call) | Slipped | Hardened to a confirmed FY28-only start (Concall_Aug_2026_Transcript.pdf, per B05) |

Comment: B05 grades overall credibility C on this ledger (5 delivered, 4 partial, 3 missed); B12b's
independent re-check finds one row's sign inverted (the FY27 lamination "raise" restores a previously
cut base rather than upgrading it) and adds further under-weighted items, without changing the
C grade (B12b).

**6. RESTATED BASES.** Quote: "The previous year figures have been regrouped/rearranged to the extent
necessary to be in line with the current period's classification. All the numbers have been rounded
off to the nearest lakhs." (Annual_Report_2026_2.pdf, PDF p.90, standalone Note 25.19). Quote: "The
Previous year figures have been regrouped/rearranged to the extent necessary to Conform with the
current period's classification." (Annual_Report_2026_2.pdf, PDF p.120, consolidated Note 25.17).
Comment: the company's own wording frames this as a presentation reclassification, not a restatement;
no restated P&L or balance-sheet figure was found anywhere in the financial notes (B02).

**7. CORPORATE-ACTION CLAUSES.** Quote: "The Board of Directors, at its meeting held on 15th June 2023,
approved a Scheme of Amalgamation between Pitti Castings Private Limited (PCPL), Pitti Rail and
Engineering Components Limited (PRECL), and Pitti Engineering Limited (PEL). The Scheme was sanctioned
by the Hon'ble National Company Law Tribunal (NCLT), Hyderabad Bench, on 3rd October 2024 and became
effective upon filing with the Registrar of Companies on 24th October 2024. The appointed date for the
amalgamation is 1st April 2023. Pursuant to the Scheme and in accordance with the approved share
exchange ratio, 21,88,772 equity shares of PEL were allotted to the eligible shareholders of PCPL on
13th November 2024." (Annual_Report_2026_2.pdf, PDF p.76). Comment: the AR confirms the scheme's
approval, sanction, appointed date and the number of shares allotted, but does not itself state the
numeric exchange ratio; the "1 share per 55 PCPL shares" ratio and any independent valuer's name are
web-sourced only (B08), not confirmed in this document. Quote (separate, pending scheme): "The Board of
Directors, at its meeting held on 5th February 2026... approved the Scheme of Amalgamation... providing
for the amalgamation of Pitti Industries Private Limited (formerly Bagadia Chaitra Industries Private
Limited)... Upon receipt of the requisite approvals, the Scheme shall become effective from the
appointed date of 1st April 2026." (Annual_Report_2026_2.pdf, PDF p.25). Comment: a joint NCLT
application sought dispensation of member/creditor meetings (order dated 10-Apr-2026) and a second
motion petition was filed 23-Apr-2026, both still pending as of the AR's date (same page).

**8. RELATED-PARTY PERIMETER.** Quote (FY26, consolidated, in lakh): "1 Remuneration... 844.99... 54.67
899.66 / 2 Rent / Lease Expenses... 126.25 225.76 352.01 / 3 Rent / Lease Income... 1.91 1.91 / 4
Purchases of goods 426.78... 256.09 682.87 / 5 Amount payable at the year end 152.35 324.30 3.81
480.46" (Annual_Report_2026_2.pdf, PDF p.119, Note 25.8). Comment: the "Entity having Significant
Influence" column is Pitti Electrical Equipment Private Limited (28.45% holding entity, B03); "Other
related parties" includes Pitti Trade and Investment Private Limited and family members Sharad B Pitti
and Madhuri S Pitti (B03, B08); Key Management Personnel remuneration and the Rs 126.25 lakh / Rs
225.76 lakh lease rentals to the Chairman and his spouse are the two largest lines. All FY26 related-
party transactions are self-classified "not at arm's length: NIL" in the AOC-2 disclosure
(Annual_Report_2026_2.pdf, PDF p.31, per B03), meaning the company itself asserts every transaction
above is at arm's length.

**9. PLEDGE AND SHAREHOLDING.** Quote (category table, as at 31st March 2026): "Promoters & Promoter
group 2,03,99,999 54.18 / Individuals 63,57,268 16.88 / Mutual Funds 53,55,173 14.22 / Insurance
Companies 15,13,162 4.02... Foreign Portfolio Investors 4,19,417 1.11" (Annual_Report_2026_2.pdf, PDF
p.56). Quote (demat/pledge-adjacent): "The Company confirms that the entire Promoter's holdings are in
electronic form and the same is in line with the directions issued by SEBI." (Annual_Report_2026_2.pdf,
PDF p.57). Comment: this is a single 31-Mar-2026 snapshot; the AR contains no explicit promoter-pledge
percentage table, and no prior-year promoter-holding row for a trend read. The twelve-quarter pledge
and holding series NOT DISCLOSED IN CORPUS: the shareholding/ folder is empty (B00); the filing to
fetch is the quarterly Shareholding Pattern (Reg 31 SEBI LODR) filed on BSE/NSE. A 0.00% pledge figure
and a roughly -5.12 percentage point three-year promoter-holding trend are reported in this run only as
web-sourced, media-reported findings (B08), not as corpus-filed facts, and are not repeated here as
corpus evidence.

**10. VERIFICATION.** Documents quoted in this annex: Annual_Report_2026_2.pdf (FY2025-26, filed
24-Aug-2026); Concall_Feb_2026_Transcript.pdf (Q3 FY26, call 6-Feb-2026); Concall_May_2026_
Transcript.pdf (Q4 FY26, call 18-May-2026); Concall_Aug_2026_Transcript.pdf (Q1 FY27, call
11-Aug-2026); Investor_Presentation_1.pdf (Q1 FY27, filed 10-Aug-2026).

CORPUS COMMIT HASH: 1b96777065b25fd4b4dc52887a749ece04722ec3

```yaml
stage: B09b-dossier
company: "PITTIENG"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
corpus_verdict: "CORPUS GAPPED"
corpus_gaps:
  - document: "Quarterly results PDFs (Q2 FY26 through Q1 FY27)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Full India Ratings rationale behind the IND AA-/Stable / IND A1+ grade"
    expected_source: "rating agency site"
    kind: "findable-missing"
  - document: "Reg 30 announcement PDFs (QIP, PCPL/PRECL scheme, PIPL/DFPL NCLT scheme, Rs 290 Cr capex board approval)"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Quarterly Shareholding Pattern (Reg 31) filings, last 12 quarters, incl. pledge"
    expected_source: "BSE"
    kind: "findable-missing"
  - document: "Prior-year annual reports FY22-FY25"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Prior-quarter investor presentations (Q2-Q4 FY26)"
    expected_source: "company IR page"
    kind: "findable-missing"
  - document: "Rupee-denominated product-line revenue split, named competitors, third-party market-share corroboration, CGU-level goodwill impairment note"
    expected_source: "company IR page"
    kind: "plausibly-nonexistent"
archetypes:
  - line: "Loose laminations & raw castings"
    archetype: "Commodity converter (Section 1B v3.7 Amendment 17 binds)"
  - line: "Value-added assemblies & machined components"
    archetype: "Build-to-spec component maker"
transition:
  - line: "Loose laminations & raw castings (converter slice)"
    from_tier: "R1 COMMODITY PRICE-TAKER"
    to_tier: "R2 COST-ADVANTAGED CONVERTER"
    engine: "Utilisation-driven fixed-cost absorption (76% sheet metal / 71% casting, FY26) and a quarterly steel-price pass-through mechanism defending cost position, not a spec premium (B04)."
    proof_gate: "Adjusted EBITDA margin on the blended base holds ~15-18% through a full steel-price cycle without help from the value-added mix shift; not separately disclosed so untestable at the slice level this run (B04)."
    recognition_gap: "Open question, resolved at Stage 11 via the destination-multiple gap: does the market already price this slice as a durable cost-advantaged converter, or still as a plain cyclical price-taker."
    ugliness: "ARTIFACT-OF-CLIMB"
    transition_falsifier: "Adjusted EBITDA margin falls back toward or below the FY23 level (~13.8%) while utilisation stays high, showing the cost position itself has eroded (B04)."
  - line: "Value-added assemblies & machined components (build-to-spec slice)"
    from_tier: "R2 COST-ADVANTAGED CONVERTER"
    to_tier: "R3 VALUE-ADDED / SPEC'D SUPPLIER"
    engine: "OEM qualification barrier (Qualify-Deliver-Expand-Integrate cycle) plus the Rs 290 Cr and Rs 150 Cr capex raising this slice's ceiling, aimed at named-OEM demand (B03, B04)."
    proof_gate: "Value-added tonnage share keeps rising quarter over quarter AND the per-tonne realisation premium over loose lamination does not keep narrowing; the premium has already narrowed ~1.47x to ~1.29x (B12b), so the gate has not fired cleanly this run."
    recognition_gap: "Open question, resolved at Stage 11 via the destination-multiple gap: does the market already price the value-added mix shift as delivered, leaving only earnings growth to carry forward."
    ugliness: "ARTIFACT-OF-CLIMB, contested: clean CWIP ageing and strongly positive CFO argue for it; three consecutive missed inventory/net-debt promises and a three-year ROCE decline with no stated floor argue for caution before treating the read as settled (B02, B03, B05, B12b)."
    transition_falsifier: "Value-added tonnage share stops rising for two consecutive quarters, or the Rs 290 Cr capex slips beyond Q1 FY30, or the realisation premium keeps narrowing toward parity (B04, B12b)."
dominant_variables:
  - "Value-added tonnage mix share and its per-tonne realisation premium over loose lamination (rising in volume, premium narrowing ~1.47x to ~1.29x, B04/B12b)"
  - "Consolidated net debt and working-capital glide path toward the company's own repeatedly restated normalisation path (still rising through FY26, B02/B03/B05)"
  - "Rs 290 Cr capex execution and commissioning date (Q1 FY30 vs Q1FY29, unresolved; no firm order figure yet, B03/B04)"
  - "Consolidated ROCE trend (18.39% FY24 peak to 13.75% FY26, three straight years down, B01/B12b)"
business_falsifier: "Capacity utilisation below 60% across sheet metal, machining or casting for two-plus quarters while new capex is still being committed; OR loss of one of the two unnamed customers making up 25.2% of consolidated revenue; OR a CGU-level impairment charge against the Rs 136.09 Cr goodwill signalling the acquired subsidiary businesses are not sound (B02, B04)."
mental_model_status: "DRAFT - PENDING OPERATOR SIGN-OFF"
fragility:
  variable_count: 4
  verifiability_ratio: "2 of 4 externally observable from filed financial statements; 2 of 4 company-narrated only"
  single_point_failure: "none named by conjunction rule - customer concentration (2 customers = 25.2% of consolidated revenue) is the nearest single-name exposure, carried as the Part C3 business falsifier instead"
  fragility_verdict: "FRAGILE"
candidate_count: 7
research_brief_items: 12
plain_summary_points: 15
annex:
  present: true
  questions_answered: 10
  corpus_commit_hash: "1b96777065b25fd4b4dc52887a749ece04722ec3"
```
