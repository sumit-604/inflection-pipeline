# Kross Ltd — shallow analysis

- Ticker KROSS (NSE), BSE 544253. ISIN INE0O6601022. Sector automotive
  components: trailer axles, suspensions, truck and tractor parts.
- Analysed 2026-09-10 per `screens/SHALLOW_ANALYSIS_FRAMEWORK.md`, from the
  corpus in `screens/corpus/KROSS/`. Every number cites a file and page. No
  forensics, no valuation, no price.
- Corpus caveat: no PDF is held on disk. The container had no egress all
  session. Text comes from Bull AI's page-numbered chunk reader, per the
  operator ruling of 2026-09-08. Bull AI's search tool was down throughout.
- Extraction warning: page 4 of the Q1 FY27 deck came back as fabricated
  placeholder text. It is not used. See the corpus manifest.
- **Section 1B note for `/step1`: do NOT classify this a CONVERTER.** Gross
  margin runs 44.8% (Deck Q1FY27 p8). That is a component maker, not a spread
  business. Amendment 17 does not bind.

## Business Understanding Narrative

Kross makes the parts that carry load under a truck or a trailer. Two lines
split the revenue: trailer axles and suspension assemblies at 41%, and
components at 59% (Deck Q1FY27 p6). The components go to medium and heavy
commercial vehicle makers, chiefly Tata Motors and Ashok Leyland, and to
tractor makers (Deck Q1FY27 p5). The trailer axles go to fabricators who build
the trailer around them. It forges, casts and machines steel in Jamshedpur. So
revenue is units times price, and profit is what survives after steel and
conversion cost.

What is changing is the process, not the product. Kross commissioned India's
first single-piece axle beam extrusion plant, replacing a fabricated welded
beam (Deck Q1FY27 p9). The company claims lower material cost, lighter weight
and better tyre life from it. It added high-tonnage forging presses, launched
hydraulic tipping jacks as a new product, and is building a Rs 167 crore
seamless tube plant to make its own tube instead of buying it (Guidance,
RZDgbv p2). Each step moves margin from the supplier to Kross.

Why now: the commercial vehicle cycle turned. Q4 FY26 revenue grew 22% and
Q1 FY27 grew 32.3% (Deck Q1FY27 p8). Management names "favourable
macroeconomic conditions and GST rationalization benefits" (Deck Q1FY27 p5).
The new capacity lands into a rising market rather than a flat one.

What must be true: three things. The extrusion plant must reach commercial
production and win share on cost. Exports must climb from 4.5% of revenue
toward the stated 8% (Deck Q1FY27 p6), because management says export work
runs at 20% to 22% EBITDA against a company average near 13% (Guidance,
RZDgbv p13). And the seamless tube plant must convert Rs 167 crore of capex
into the promised backward-integration saving of 3% to 4% of product cost
(Guidance, RZDgbv p10).

What breaks it: the capex outruns the demand. Kross spent its entire IPO
proceeds by FY26 (Deck FY26 p30), plans about Rs 125 crore more in FY27
(Guidance, epZKpK p8), and depreciation already rose 46.7% year on year while
PAT grew only 24.4% (Deck Q1FY27 p8). If the commercial vehicle cycle rolls
over before utilisation rises, the fixed cost stays and the volume does not.

## 1. Corpus ledger
Held: the Q1 FY27 result statement, pages 1 to 6, with the full P&L and the
board's governance decisions. The Q1 FY27 investor deck, pages 1 to 10, with
the income statement, revenue mix, and capacity updates. A guidance and
delivery ledger covering Q2 FY25 to Q1 FY27, drawn from five transcripts and
two decks, every quote page-cited.
Missing: no balance sheet, no cash-flow statement, no promoter holding, no
pledge figure, no related-party schedule, no annual report text, no credit
rating. Looked for the rating in the Bull AI availability map; no Credit Rating
subcategory exists for this company, and the agency sites were unreachable.
The gaps weaken step 4 almost entirely, and the leverage and cash-conversion
half of step 5.

## 2. Business model and archetype
One reported segment, "Motor vehicle parts & accessories" (Result Q1FY27 p6
note 3). No subsidiary, associate or joint venture as at 30 June 2026 (Result
Q1FY27 p6 note 5). Revenue mix Q1 FY27: trailer axles and suspension 41%,
components 59% (Deck Q1FY27 p6). Exports about 4.5% (Deck Q1FY27 p6). Gross
margin 44.8%, so the economic engine is conversion of bought steel into
engineered parts, with roughly 55 paise of every rupee of revenue left after
material.
Archetype from the library: **build-to-spec component maker**. Customer capex
cycle, design-win pipeline, content per unit and input-cost pass-through are
the right levers. Management confirmed the pass-through lever explicitly: "we
are looking at least another 1% or 2% increase further" on price (Guidance,
OUJxqr p10).

## 3. Competitive advantages
Forming, not formed. The extrusion process is described as "India's first
Axle Beam Extrusion Plant, a pioneering single-piece extrusion process" (Deck
Q1FY27 p6). If that holds, it is a genuine process advantage in a segment where
rivals weld. Scale is real in the niche: Bull AI's peer summary calls Kross a
"dominant position in organized trailer axle manufacturing" (Bull AI peers).
Against that, switching costs look thin at the trailer end, where fabricators
buy assemblies, and pricing power is limited, since Kross must raise prices to
recover input cost rather than ahead of it. Gross margin actually fell 120
basis points year on year, from 46.0% to 44.8% (Deck Q1FY27 p8). A moat is
forming on process cost. It is not present on price.

## 4. The promoters
Largely NOT FOUND. No shareholding pattern, promoter holding percentage or
pledge figure appears in the held corpus. Looked for it in the Bull AI
availability map, which indexes no shareholding-pattern subcategory for Kross,
and in the Q1 FY27 result and deck, which carry none.
What is held: Sudhir Rai is Chairman and Managing Director, DIN 00512423
(Result Q1FY27 p6). Kunal Rai is Whole-Time Director and CFO and Sumeet Rai is
a Whole-Time Director, both speaking for the company on earnings calls
(Guidance, epZKpK p5). Anita Rai sits on a board committee (Result Q1FY27 p3).
Four Rai family members hold executive or board positions. The company listed
in September 2024 and had deployed 100% of IPO proceeds by FY26 (Deck FY26
p30), which is fast and, on the evidence held, into stated capex.

## 5. Financial trajectory

| Rs crore | Q1 FY26 | Q2 FY26 | Q4 FY26 | FY26 | Q1 FY27 |
|---|---:|---:|---:|---:|---:|
| Revenue | 139.4 | 130.9 | 225.4 | 673.2 | 184.3 |
| EBITDA | 16.2 | 14.8 | 33.6 | 87.9 | 22.6 |
| EBITDA margin | 11.6% | 11.3% | 14.9% | 13.06% | 12.2% |
| PAT | 10.7 | n/d | 22.5 | 55.2 | 13.3 |

Sources: Result Q1FY27 p5, Deck Q1FY27 p8, Deck FY26 p5, Guidance uX6xHm p5.
FY26 revenue grew 8.5% and PAT grew 15.0% (Deck FY26 p5). The year was two
halves: H1 revenue fell, H2 recovered hard. Derived from the filed statement,
equity at 31 March 2026 was Rs 489.8 crore and FY26 return on equity 11.3%.
Finance cost was Rs 8.07 crore against Rs 87.9 crore of EBITDA, so leverage is
light; management reported a debt-to-equity ratio of 0.1x after applying Rs 90
crore of IPO money to debt (Guidance, ziosap p3).
Classification: **margin-led in H2 FY26, volume-led in Q1 FY27**. Q1 FY27
revenue rose 32.3% on 34% higher axle and suspension volumes (Deck Q1FY27 p6)
while EBITDA margin rose only 63 basis points and gross margin fell. This is
units, not price. Cash conversion is INDETERMINATE: no cash-flow statement is
held for any period.

## 6. The transition and the quality ladder
FROM **R2, cost-advantaged converter**. TO **R3, value-added and spec'd
supplier**. The mechanism is the extrusion process, the tipping-jack product
launch, and export qualification with a European Tier-1 customer.
Management's claim, quoted once: "Commissioned India's first Axle Beam
Extrusion Plant, a pioneering single-piece extrusion process... Clear
Competitive Edge: Lower material cost (no welding), Lighter weight, Superior
technical performance leading to improved tyre life" (Deck Q1FY27 p9).
The ladder test is ROCE durability, and the evidence sits below the claim.
FY26 return on equity was 11.3%. R3 asks for 20% to 25% ROCE with stickiness.
Kross is not there. One rung in two to three years is the base rate, and the
climb has started, not landed.

## 7. Growth-trigger register

| Trigger | Date | Source | Status |
|---|---|---|---|
| Axle beam extrusion plant | Commissioned 27 Feb 2026 | Deck FY26 p11 | DELIVERED, commissioned |
| Extrusion commercial production | "soon in August 2026" | Deck Q1FY27 p5 | UNDERWAY, slipped from end Q3 FY26 |
| Tipping jacks facility | Commissioned FY26, 800 kits/month capacity | Deck FY26 p6 | DELIVERED |
| Tipping jacks 250-300 units by end Q1 FY27 | Q4 FY26 deck p5 | Deck Q1FY27 p6 | MISSED, 220 kits produced |
| High-pressure moulding line, doubles casting | September 2026 | Deck Q1FY27 p6 | STATED |
| Robotic forging axle shaft line | September 2026 | Deck Q1FY27 p6 | STATED |
| Seamless tube plant, Rs 167 crore | Q4 FY27 | Guidance uX6xHm p6 | UNDERWAY, shed done, mills in transit |
| Exports to 8% of revenue | FY27 | Deck Q1FY27 p6 | UNDERWAY, 4.5% in Q1 FY27 |
| Tractor and agri to about 15% of revenue | FY28 | Deck FY26 p5 | UNDERWAY, about 40% YoY growth in Q1 |
| Additional 1000-tonne press | ordered | Deck Q1FY27 p6 | STATED |

## 8. Proof check
The last two quarters move the way the volume triggers claim and against the
margin claim.
Proof point, positive: Q4 FY26 revenue up 22% and Q1 FY27 up 32.3%, with axle
and suspension volumes up 34% year on year (Deck Q1FY27 p6, p8). The capacity
built is being sold.
Proof point, negative: management guided "Between 14% to 15% margin... for the
further quarters as well" in May 2026 (Guidance, epZKpK p9). Q1 FY27 delivered
12.2% (Deck Q1FY27 p8). Gross margin fell 120 basis points. Depreciation rose
46.7%, and management attributes the profit shortfall to it (Deck Q1FY27 p8).
Absence: no cash-flow statement, so whether the growth is funded by working
capital cannot be tested here.
Verdict on proof: **volume proven, margin not yet**.

## 9. Flags from the documents
- **Two senior resignations at one board meeting, 24 July 2026.** Mr. Mukesh
  Kumar Agarwal resigned as Independent Director with immediate effect, and
  Mr. Dhirendra Jena, Head (Accounts & Finance), was relieved on 31 July 2026
  (Result Q1FY27 p2). A finance head and an independent director leaving
  together is worth a question, not a conclusion.
- **Guidance slippage is repeated, not one-off.** Extrusion commercial
  production moved from end Q3 FY26 to August 2026. Tipping jacks came in at
  220 against 250 to 300. Export share is 4.5% against an 8% full-year target.
- **Auditor is a small regional firm.** S. K. Naredi & Co LLP, Jamshedpur, with
  branches at Kolkata, Bhubaneswar and Ranchi (Result Q1FY27 p4). The review
  conclusion is unmodified.
- **Family concentration on the board.** Four Rai family members hold executive
  or committee positions (Result Q1FY27 p2, p3, p6).
- Related-party exposure: NOT FOUND, no schedule held.
- Contingent liabilities and litigation: NOT FOUND, no annual report text held.

## 10. Independent check: the credit rating
NOT FOUND. Bull AI indexes no Credit Rating document for Kross. Checked the
full availability map on 2026-09-10. Agency sites (CRISIL, ICRA, CARE, India
Ratings, Acuité) were unreachable because this container has no egress. A
Monitoring Agency Report series runs to Q1 FY27 in the index, which tracks IPO
fund use rather than creditworthiness, and was not read.
The step therefore contributes nothing here. Treat the balance-sheet read as
unverified by any outside party.

## 11. Posture: Transition Decision Matrix
- **Proof gate: PARTIALLY FIRED.** Volume and revenue fired. The margin gate
  did not. Under the framework's binary this reads NOT FIRED, because the
  claimed mechanism is cost and margin, and margin fell short of guidance.
- **Ugliness: ARTIFACT-OF-CLIMB.** The margin dip traces to depreciation on
  capacity that is commissioned but not yet at commercial production, and to
  65% utilisation (Deck FY26 p5). That is a climbing cost, not a decaying one.
- **Recognition gap: INDETERMINATE.** Bull AI reports market cap of
  Rs 1,416.63 crore, undated and unverified. No live price is available to this
  container. Resolve at Stage 11.
- **Posture: RESEARCH / WATCH**, per the Proof NOT FIRED plus ARTIFACT row.
  The narrative is coherent and the capex is real. The gate is the margin.

## 12. Verdict card
**PROCEED to `/step1`.**
This is the strongest of the six names screened on 2026-09-10. A real process
change, a real product launch, a turning end-market, light leverage, and a
management team that gives dated numeric guidance and can be marked against it.
The margin miss is a reason to verify, not to pass.

Load-bearing facts a deep run must verify first:
1. Promoter holding and pledge. Entirely absent from this corpus.
2. Cash conversion. No cash-flow statement was held for any period. The
   Kernex guard applies until operating cash flow is seen.
3. Whether extrusion commercial production actually started in August 2026,
   and what it did to gross margin in Q2 FY27.
4. The 24 July 2026 resignations of the Independent Director and the Head of
   Accounts and Finance.
5. ROCE on the enlarged capital base, since FY26 return on equity of 11.3% sits
   two rungs below the claimed destination.

What would change the view: gross margin recovering above 46% with extrusion
running would confirm the cost mechanism and fire the proof gate. A second
quarter below 13% EBITDA margin with depreciation still climbing would turn
the ugliness from artifact to structural, and the posture to DEEP WATCH.
No price, no position. This decides only that Kross earns a full `/step1`.
