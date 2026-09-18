# OnEMI Technology Solutions Ltd (Kissht) — shallow analysis

- Ticker KISSHT (NSE), BSE 544754. ISIN INE12F801023. Founded 2016, headquartered Mumbai. Listed on
  NSE and BSE on 8 May 2026. Sector: digital consumer lending. Lending subsidiary Si Creva Capital
  Services Private Limited, an RBI-registered NBFC, Middle Layer under the Scale Based Regulations.
- Analysed 2026-09-17 per `screens/SHALLOW_ANALYSIS_FRAMEWORK.md`, from the corpus in
  `screens/corpus/KISSHT/`. Every number cites a file and page. No forensics, no valuation, no price.
- Market cap Rs 6,068 crore on 2026-09-17, from Bull AI's identity record, not a filing. Against net
  worth of Rs 2,245 crore at June 2026 (IP p.7) that is about 2.7 times book. Verify live.
- **Archetype is Lender, so the quality ladder specialises.** Per CLAUDE.md, a lender's ladder runs on
  asset quality and return on assets, not product spec. This card declares a specialised rung set in
  step 6.
- **Four months listed.** The FY2026 annual report exists in Bull AI's inventory and was not opened in
  this shallow read.
- **CORRECTION, 2026-09-18.** This card originally recorded that falling Stage 3 provision coverage
  alongside falling impairment cost could not be separated from lighter provisioning. Deck pages 29
  and 31, which this shallow read did not open, separate them. Total provisioning rose. Steps 8 and 9
  are corrected below. The PROCEED verdict is unchanged and better supported.

## Business Understanding Narrative

Kissht lends small amounts of money to young Indians through a phone. Assets under management reached
Rs 8,001 crore at June 2026, of which Rs 7,384 crore, or 92.3%, is unsecured personal loans of up to
Rs 5 lakhs for up to five years, originated entirely digitally across 17,000-plus pin codes (IP p.11).
The remaining 7.7% is loan against property, ticket up to Rs 15 lakhs, ten-year tenure, 48% loan to
value, sold through 101 branches in eight states (IP p.11). The borrower is 32 years old on average,
53% self-employed, 78% in the top 100 cities, with a median CIBIL score of 746 (IP p.12).

Two things about how the money works. First, the loan is only half on the company's own books. At June
2026 the split was 53.6% on-book and 46.4% off-book, the off-book Rs 4,284 crore sitting on the books
of 45-plus lending partners under three structures: 100-0, co-lending and direct assignment
(IP p.33). Second, and this is the sentence that matters most on this card, the credit risk does not
fully travel with the loan: "Under the Group's business model, FLDG (First Loss Default Guarantee)
obligations are treated as financial guarantees and are typically based on the business arrangements
(maximum capped at 5%) of the disbursed portfolio by the lending Banks/NBFCs" (Prospectus p.352).
Kissht keeps the first 5% of losses on loans it has moved off its balance sheet.

The economics are high-yield and high-loss. Expressed against average assets under management, total
income ran 35.9% in the June quarter, funding cost 4.3%, operating expenses 18.0% and impairment cost
6.8%, leaving 6.8% pre-tax and 5.0% after tax (IP p.41). That is a business that charges a lot and
writes off a lot, and where a change in the loss rate moves everything.

What is changing is a deliberate attempt to make it less so. The CEO sets out a three-link mechanism:
"As AUM scales, both cost of borrowings and operating expenses (as % of average AUM) are expected to
reduce... Benefits of cost reduction to be passed on to customers which will lead to better customer
selection and reduced impairment cost", alongside a secured mix that went from 2.5% of assets in June
2025 to 7.7% in June 2026 (IP p.5).

Why now: the May 2026 listing put Rs 900 crore-odd of fresh equity into the business. Net worth went
from Rs 1,343 crore to Rs 2,245 crore in one quarter, capital adequacy from 25.28% to 40.19%, and debt
to equity from 1.78 times to 0.91 (IP p.7). The company is now over-capitalised for its book, which is
a temporary state and a deliberate one.

What must be true: cheaper funding must buy better borrowers, and better borrowers must show up as a
lower loss rate that holds.

What breaks it: the loss rate. Impairment cost of 6.8% of average AUM sits against pre-tax profit of
6.8% of average AUM (IP p.41). Those two numbers are the same size. A consumer credit cycle that
pushes losses up by half takes pre-tax profit down by half.

## 1. Corpus ledger
Held: the Q1 FY27 investor presentation, nine pages, giving the CEO's stated mechanism, the full
quarterly snapshot with asset quality, scale, profitability and capital, the product split, the AUM
journey since 2017, the borrower profile by segment, geography, age and credit score, the on-book and
off-book liability profile, and a full DuPont on average AUM across three quarters. The Q4 FY26 deck
for the FY26 comparatives and the glossary. Four pages of the prospectus and red herring prospectus
covering the FLDG accounting policy, the off-book partnership structures, the regulatory framework and
the financial risk management note.
Missing, and the first three are significant: the FY2026 annual report, which Bull AI holds and which
this shallow read did not open, leaving no audited balance sheet, related-party schedule or auditor's
report and weakening steps 4, 5 and 9. Deck pages 27 to 31 were read on 2026-09-18 and are now held;
pages 20 to 26, the Risk Management Framework section, remain unread. Two earnings call transcripts, so step 7 has no spoken guidance. Beyond
those: no asset-quality figures for the 46.4% of AUM that is off-book; no rupee quantification of the
FLDG exposure; no shareholding pattern, so promoter holding and pledge are NOT FOUND; no board list;
and no vintage or static-pool loss curves.

## 2. Business model and archetype
Originate a small unsecured loan through an app, price it at a yield that covers a high loss rate, and
place roughly half of it with a partner while keeping the first loss. Revenue is yield times assets;
profit is what survives credit cost and operating cost. The AUM journey: Rs 10 crore in 2017, Rs 300
crore 2019, Rs 400 crore 2022, Rs 1,268 crore 2023, Rs 2,604 crore 2024, Rs 4,087 crore 2025, Rs 8,001
crore at Q1 FY27 (IP p.10).

Archetype: **Lender**, and the framework variant applies. The dials are AUM growth, net interest
margin, asset quality and returns, and the corpus discloses all four properly. Note one wrinkle: the
off-book half makes this partly a **Platform/network** origination business too, earning a fee rather
than a spread, and the card treats that as a sub-model rather than a second archetype. Underwriting is
described as "Proprietary AI/ML underwriting using 7,200+ variables" (IP p.9).

## 3. Competitive advantages
Genuine candidates, none of them proven durable.
- **Underwriting data at scale.** 12.25 million customers served cumulatively and 3.49 million active
  (IP p.7). In consumer credit, repayment history on twelve million people is the asset. Whether it is
  a moat depends on whether it produces a lower loss rate than a competitor with less data, and the
  corpus does not test that.
- **The liability structure itself.** 45-plus lending partners and 8-plus off-book partners (IP p.33)
  let the company grow AUM faster than its own capital. That is a capability, and it also transfers
  balance sheet without transferring the first loss.
- **Distribution reach without branches** for 92.3% of the book: 17,000-plus pin codes, 100% digital
  (IP p.11).
- **A credit rating of A-/Stable** on the NBFC (IP p.9), which gives access to bank funding that
  smaller digital lenders do not have.
- **Brand.** Sachin Tendulkar came in as "strategic investor and brand ambassador" in 2024 (IP p.10).

Against: personal lending is the most contested product in Indian finance, the barriers are regulatory
licences rather than anything proprietary, and a 14.45% average cost of borrowings (IP p.33) says the
funding market does not yet treat this as a high-quality franchise.
**Verdict: forming, and the test is the loss rate.** Everything claimed as advantage should show up as
impairment cost falling and staying down. Step 8 examines whether it has.

## 4. The promoters
Thin, because the annual report was not opened. Ranvir Singh is Chairman, Director and Chief Executive
Officer, and writes the shareholder letter (IP p.5). No other director is named anywhere in the held
corpus. There is no board list, no biography and no group structure on this card.

Promoter holding: **NOT FOUND.** Pledge: **NOT FOUND.** Looked for in both decks and the prospectus
extracts held. The FY2026 annual report and the prospectus both carry them and neither was opened.

Sachin Tendulkar is recorded as a "strategic investor and brand ambassador" from 2024 (IP p.10). His
holding is not disclosed in the held corpus.

Building, under the Rule G test, is well documented in outline: the founders registered an NBFC,
launched an app, and grew assets under management from Rs 10 crore in 2017 to Rs 8,001 crore in nine
years, through the 2022 regulatory reset that closed many digital lenders, and got the NBFC classified
Middle Layer under the Scale Based Regulations in 2023 (IP p.10). That is a decade of building a
regulated business under real constraint. The ledger cannot be completed and its Pillar 3 line cannot
be stated without the annual report and the shareholding pattern.

## 5. Financial trajectory
Rs crore unless stated (IP p.7; Q4 FY26 deck p.7, p.34; IP p.33, p.41):

| | FY25 | FY26 | Q1 FY26 | Q4 FY26 | Q1 FY27 |
|---|---:|---:|---:|---:|---:|
| AUM | 4,087 | 7,066 | NOT FOUND | 7,066 | 8,001 |
| Total income | NOT FOUND | 2,209 | NOT FOUND | NOT FOUND | 677 |
| PPOP | NOT FOUND | 836 | NOT FOUND | NOT FOUND | 256 |
| PAT | NOT FOUND | 281 | NOT FOUND | NOT FOUND | 95 |
| RoAAUM | NOT FOUND | 5.05% | 5.3% | 5.0% | 5.05% |
| RoAE | NOT FOUND | 23.97% | NOT FOUND | NOT FOUND | 21.20% |
| GNPA (Stage 3, on-book) | NOT FOUND | 2.12% | 3.64% | 2.12% | 2.25% |
| NNPA (on-book) | NOT FOUND | 0.29% | 0.34% | 0.30% | 0.36% |
| PCR (on-book) | NOT FOUND | 86.15% | 90.66% | 86.15% | 84.13% |
| Collection efficiency, DPD 30 | NOT FOUND | 97.01% | 97.15% | 97.15% | 96.82% |
| Net worth | NOT FOUND | 1,343 | NOT FOUND | 1,343 | 2,245 |
| Capital adequacy (NBFC) | NOT FOUND | 25.28% | NOT FOUND | 25.28% | 40.19% |
| Debt to equity | NOT FOUND | 1.78 | NOT FOUND | 1.78 | 0.91 |
| Secured (LAP) share of AUM | NOT FOUND | 7.3% | 2.5% | 7.3% | 7.7% |
| On-book share of AUM | 39.4% | 49.7% | 47.5% | 49.7% | 53.6% |

Some Q1 FY26 and Q4 FY26 entries above are derived from the year-on-year and quarter-on-quarter change
figures the decks print alongside the current value. They are arithmetic on disclosed deltas, not
separately filed numbers, and are marked as such here rather than treated as primary.

**The growth is real and it is fast.** AUM up 61% year on year and 73% in FY26. Total income up 45%
and 63%. Profit after tax up 59% and 75%. Active customers up 111% year on year to 3.49 million. Not
one of those is ambiguous.

**The DuPont is where the story lives** (IP p.41). Read it top to bottom, Q1 FY26 to Q1 FY27:
- Total income fell from 41.1% of average AUM to 35.9%, down 5.2 points. Yields are compressing.
- Finance cost fell from 5.2% to 4.3%, down 0.9.
- Operating expenses fell from 20.0% to 18.0%, down 2.0.
- Impairment cost fell from 8.8% to 6.8%, down 2.0.
- Profit before tax went 7.1% to 6.8%, and profit after tax 5.3% to 5.0%.

Every cost line moved exactly the way the CEO said it would. The yield fell faster than all three
combined, so the return on assets went slightly down. That is not a failure. It is what "benefits of
cost reduction to be passed on to customers" means in practice, and the company said it would happen.
The open question is whether the better customers it is meant to buy arrive.

**Capital.** The listing moved net worth 67% in a quarter to Rs 2,245 crore, took capital adequacy to
40.19% and halved gearing (IP p.7). At 40% capital adequacy the NBFC carries roughly twice the capital
the regulator requires. Return on equity fell 411 basis points to 21.20% for that reason alone, and
will stay suppressed until the book grows into the capital.

**Inflection classification: EARNINGS-LED with a flat return profile.** Cash conversion is not the
right test for a lender; the framework's cash-conversion caveat maps here onto whether reported profit
survives credit cost, which step 8 tests. Return on assets has been flat at 5.0% to 5.3% for five
quarters.

## 6. The transition and the quality ladder
The lender-specialised rungs, declared here as CLAUDE.md permits, running on asset quality, funding
cost and return durability rather than product spec:
FROM **L1, HIGH-YIELD MONOLINE.** A single unsecured product at 92.3% of assets, charging 35.9% of AUM
in income to absorb 6.8% in credit cost, funded at 14.45%, with no deposit franchise and returns
hostage to the consumer credit cycle. That is where this company is today.
TO **L2, DIVERSIFIED SECURED-AND-UNSECURED LENDER.** A rising secured book, funding cost falling with
rating upgrades, credit cost structurally lower because the borrower is better, and a return on assets
that survives a downturn.
Mechanism, and it is unusually well specified for a shallow read. **Management's claim, quoted once:**
"As AUM scales, both cost of borrowings and operating expenses (as % of average AUM) are expected to
reduce. Benefits of cost reduction to be passed on to customers which will lead to better customer
selection and reduced impairment cost. Secured mix: LAP AUM contributes 7.7% of AUM as of Jun-26 (vs
7.3% in Mar-26 and 2.5% in Jun-25), with scale-up expected to continue" (IP p.5).
**Ladder ruling: one rung, with a stated causal chain of three links, each of which is separately
measurable in the DuPont the company publishes quarterly.** That is a high-quality transition claim.
The honest caution is that the secured book is 7.7% of assets and grew only 40 basis points in the
most recent quarter, against 480 basis points over the three before it. At that pace the mix shift
takes many years.

## 7. Growth-trigger register

| Trigger | Date | Source | Status |
|---|---|---|---|
| Listing on NSE and BSE | 8 May 2026 | IP p.10 | DELIVERED |
| AUM past Rs 8,000 crore | Q1 FY27 | IP p.5 | DELIVERED, Rs 8,001 crore |
| Cost of borrowings to fall as AUM scales | ongoing | IP p.5 | DELIVERED, 5.2% to 4.3% of avg AUM YoY |
| Operating expenses to fall as AUM scales | ongoing | IP p.5 | DELIVERED, 20.0% to 18.0% of avg AUM YoY |
| Impairment cost to fall on better customer selection | ongoing | IP p.5 | DELIVERED so far, 8.8% to 6.8% of avg AUM YoY |
| LAP secured mix to scale up "through the remaining quarters of FY27, and beyond" | FY27 | IP p.5 | UNDERWAY, 2.5% to 7.3% to 7.7% |
| On-book share of AUM to rise | ongoing | IP p.33 | UNDERWAY, 39.4% at Mar-25 to 53.6% at Jun-26 |
| 101 LAP branches across 8 states | Q1 FY27 | IP p.11 | DELIVERED |
| AI-led underwriting deployed across workflows | 2025 | IP p.10 | DELIVERED |
| Credit rating A-/Stable on the NBFC | current | IP p.9 | DELIVERED |

Ten triggers, seven delivered, and five of them measured in the company's own quarterly DuPont. The
register is specific and it is auditable quarter by quarter, which is rare.

## 8. Proof check
**The mechanism is firing. The outcome is not, yet.** That distinction is the whole card.

**Firing.** All three cost links the CEO named moved the right way year on year, and each is separately
disclosed: funding cost down 0.9 points of average AUM, operating expenses down 2.0, impairment cost
down 2.0 (IP p.41). Gross non-performing assets improved 139 basis points year on year to 2.25%
(IP p.7). On-book share rose from 39.4% at March 2025 to 53.6% at June 2026 (IP p.33, Q4 FY26 deck
p.34), meaning the company is keeping more of what it originates, which is what a lender does when it
believes its own underwriting.

**Not firing.** Return on average AUM is 5.05%, against 5.05% in FY26 and 5.3% a year ago (IP p.7,
p.41). Five quarters of falling costs have produced no improvement in the return, because the yield
fell faster. Return on equity fell to 21.20%.

**Three counter-signals in the asset quality, all small and all pointing the same way.** Gross
non-performing assets rose 13 basis points sequentially. Net non-performing assets rose 6 basis points
sequentially and 2 year on year, so the net number is not improving even as the gross number does.
Collection efficiency at DPD 30 slipped 33 basis points both sequentially and year on year, to 96.82%.

**One combination looked concerning and resolves the right way.** Stage 3 provision coverage fell from
90.66% a year ago to 84.13% at June 2026, 653 basis points, while impairment cost also fell. That
pairing is consistent with better assets and equally with lighter provisioning. **Deck page 31
separates them and the answer is better assets.** Stage 2 ECL coverage rose from 59.1% to 80.4% across
the same five quarters. The management overlay rose from Rs 122 crore to Rs 136 crore. Combined
provision coverage plus overlay on Stage 2 and Stage 3 assets rose from 137% to 150% (IP p.31). Total
provisioning went up. The Stage 3 coverage decline is a mix effect: Stage 3 assets fell from 3.6% to
2.2% of the book (IP p.31), and a shrinking Stage 3 stock carries newer, less-aged exposures.

**And the off-book blind spot is narrower than this card first said.** Page 29 carries bounce rate,
first-EMI-to-DPD-90 and collection efficiency, and states "The above information is for overall AUM",
so those three cover the off-book 46.4% as well. First EMI to DPD 90, the cleanest available read on
new origination quality, fell from 1.6% at June 2025 to 0.7% and held there for three quarters
(IP p.29). Bounce rate was flat at 13.5% to 13.6%. What remains undisclosed for the off-book half is
Stage 3 and net NPA specifically, not asset quality altogether.

**The proof point, named: impairment cost as a percentage of average AUM, read together with provision
coverage and net non-performing assets.** Not one of the three alone.

**The proof gate has NOT FIRED.** The inputs have moved for five quarters and the output, return on
assets, has not.

## 9. Flags from the documents
- **The first loss stays with the company.** "FLDG obligations are treated as financial guarantees and
  are typically based on the business arrangements (maximum capped at 5%) of the disbursed portfolio
  by the lending Banks/NBFCs" (Prospectus p.352). Off-book AUM was Rs 4,284 crore at June 2026
  (IP p.33). **[INFERENCE]** At the 5% cap that is roughly Rs 214 crore of contingent first-loss
  exposure, about 9.5% of net worth. The inference assumes the cap applies across the whole off-book
  book and that none has already been called; neither is verifiable from the corpus. The rupee amount
  is not disclosed anywhere held.
- **Stage 3 and net NPA cover only the on-book half, though other asset-quality metrics do not.**
  Every GNPA, NNPA and PCR figure carries the footnote "Pertains to the subsidiary NBFC... and is
  based on on-book portfolio" (IP p.7), which at June 2026 is 53.6% of AUM. **But bounce rate,
  first-EMI-to-DPD-90 and collection efficiency are disclosed for overall AUM** (IP p.29), so the
  off-book half is not dark. The specific gap is Stage 3 and net NPA for the off-book portion, which
  is also the portion carrying the first-loss guarantee.
- ~~Provision coverage is falling while impairment cost falls.~~ **RESOLVED 2026-09-18 and withdrawn
  as a flag.** Stage 2 ECL coverage rose 59.1% to 80.4%, the management overlay rose Rs 122 crore to
  Rs 136 crore, and combined Stage 2 plus Stage 3 coverage including the overlay rose 137% to 150%
  (IP p.31). Total provisioning increased.
- **Net non-performing assets are not improving.** Up 2 basis points year on year and 6 sequentially,
  while gross improved 139 basis points (IP p.7).
- **Collection efficiency slipped**, 33 basis points both sequentially and year on year (IP p.7).
- **Yield compression is running ahead of cost reduction**, 5.2 points against 4.9 combined (IP p.41).
- **92.3% of assets are unsecured personal loans** (IP p.11), in a product the RBI has repeatedly
  tightened. The prospectus itself lists "Tech & overregulation risk" among the sector's key
  challenges (RHP p.175).
- **Cost of borrowings is 14.45%** on-book (IP p.33), up from a stated range of 11.50% to 14.25% at
  March 2026 (Q4 FY26 deck p.34). The average cost appears to have risen, not fallen, in rupee terms
  even as it fell as a share of AUM.
- **The secured mix barely moved last quarter**, 7.3% to 7.7% (IP p.5), after 2.5% to 7.3% over the
  three before.
- **Regulatory dependence is explicit.** Co-lending now requires the partner to retain at least 10% of
  each loan under the RBI (Co-Lending Arrangements) Directions, 2025, and the first-loss cover is
  capped at 5% (RHP p.171). Both caps are regulatory and both can change.
- **Four months listed, no annual report read, promoter holding NOT FOUND.**
- **A table artefact, not a company error.** The Credit Rating row on the snapshot slide prints the
  Capital Adequacy Ratio row's basis-point changes.

## 10. Independent check: the credit rating
**PARTIAL, and thinner than it looks.** The deck reports a long-term credit rating of A-/Stable for
the subsidiary NBFC, Si Creva Capital Services Private Limited (IP p.7, p.9). That is the whole of it.
**No agency is named.** No rating letter and no press release appears in Bull AI's inventory for this
company, and the agency sites are unreachable from this session. Looked for in the availability map
across all categories, in both decks and in the prospectus extracts held.

An A- for an NBFC whose book is 92.3% unsecured personal loans is a reasonable grade and consistent
with a 14.45% cost of borrowings: the rating is investment grade but not strong enough to command
cheap money. The framework's substitute for the cut machinery is therefore only half available here.
For a lender, where an agency's view of asset quality is the single most useful outside opinion
available, a rating with no name and no rationale does not do the job the step exists to do.

## 11. Posture: the Transition Decision Matrix
- **Proof gate: NOT FIRED.** Step 8. Five quarters of the stated mechanism working on every input, with
  return on assets flat at 5.0%.
- **Ugliness: ARTIFACT-OF-CLIMB, and unusually clearly so.** Return on equity fell 411 basis points in
  the June quarter for one reason: the IPO put Rs 900 crore-odd of equity in and capital adequacy went
  to 40.19% (IP p.7). Capital raised and not yet deployed depresses return on equity by arithmetic.
  That is the cost of the climb, not decay, and it reverses as the book grows.
- **Recognition gap: OPEN.** About 2.7 times book and, on the June quarter annualised, roughly 16 times
  earnings, for a lender compounding assets at 61% with a 21.2% return on equity and 40% capital
  adequacy. The market is not paying a franchise multiple. It is pricing in the unsecured
  concentration, the regulatory exposure and the four-month listing history, which is rational, and it
  leaves room if the transition works.

**Posture: RESEARCH / WATCH.** Proof not fired, ugliness a clear artifact, gap open. Watch the gate.
The gate is the DuPont, and it is published quarterly.

## 12. Verdict card

**PROCEED to `/step1`.**

This is the best-disclosed company in the run. It publishes a quarterly DuPont on average assets, a
gross and net non-performing asset series with provision coverage, a collection efficiency figure, an
on-book and off-book split with the cost of borrowings on each, a borrower profile down to the CIBIL
distribution, and a dedicated eleven-page risk management and asset quality section this shallow read
did not even open. It states its transition as a three-link causal chain, and every link is separately
measurable in its own numbers. Whatever the answer turns out to be, this company can be analysed.

It earns the deep run because the central question is sharp and testable: **does cheaper funding buy
better borrowers fast enough to offset the yield it gives away?** Five quarters of evidence say the
costs are falling exactly as promised, and that the yield is falling slightly faster. One more year of
the same DuPont settles it.

The bear case at the same bar. 92.3% of assets are unsecured personal loans in the product the RBI
watches most closely. Impairment cost of 6.8% of average assets is the same size as pre-tax profit, so
the margin for error is one bad cycle wide. Reported asset quality covers only the on-book 53.6%, while
the company retains up to 5% first loss on the off-book 46.4%. Provision coverage has fallen 653 basis
points year on year while impairment cost fell, and the corpus cannot say which caused which. Net
non-performing assets are not improving. And the secured mix, the structural fix, is 7.7% of assets
and slowed to a crawl last quarter.

**Load-bearing facts a deep run must verify first:**
1. **Off-book Stage 3 and net NPA.** Bounce rate, first-EMI-to-DPD-90 and collection efficiency are
   given for overall AUM (IP p.29); gross and net non-performing assets are not. Get the loss rate on
   the 46.4% sitting with partners.
2. **The FLDG exposure in rupees**, at each balance-sheet date, how much has been called historically,
   and how it is provided for. The policy caps it at 5%; the amount is not stated.
3. ~~Why provision coverage fell 653 basis points.~~ **RESOLVED**, see step 8. Confirm the Rs 136
   crore management overlay and the 150% combined coverage against the audited FY26 accounts.
4. Static-pool or vintage loss curves by origination cohort, which is the only honest way to tell
   better underwriting from a growing book masking losses.
5. The FY2026 annual report, held by Bull AI and unopened here: audited balance sheet, related-party
   schedule, auditor's report, shareholding pattern.
6. Promoter holding, pledge, and the post-IPO cap table including Sachin Tendulkar's stake.
7. Which agency rates the NBFC A-/Stable, and the rationale behind it.
8. The two earnings call transcripts, for management's own answers on the LAP ramp and the yield
   compression.
9. Regulatory exposure: what the RBI's 2025 Digital Lending Directions and the Co-Lending Directions
   would do to this model if the 5% first-loss cap or the 10% retention rule changed again.

**What would change the view.** To a strong PROCEED: two or three quarters where return on average AUM
rises above 5.3% with provision coverage stable or rising, plus the secured mix past 12%. To WATCH:
impairment cost flattening or rising while yield keeps falling, which would mean the pass-through is
buying growth rather than quality. To PASS: any evidence that off-book asset quality is materially
worse than on-book, or a called FLDG large enough to matter against net worth.

**Gate note.** `companies/KISSHT.md` does not exist, so there is no Spear line and no company memory.
Under the SPEAR GATE in CLAUDE.md, `/run-pipeline` and `/fttcp` on this name must STOP until a spear
pass runs on live web with Claude web and a HIT or an operator OVERRIDE line is written.

**This is not a position.** No valuation, no target price, no entry zone. The shallow read decides only
that a full `/step1` is worth running on this name.
