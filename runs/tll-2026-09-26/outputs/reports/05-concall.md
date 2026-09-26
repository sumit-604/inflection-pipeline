# Stage 5 — Concall Analysis, Trident Lifeline Ltd (TLL), 2026-09-26
## NO-CONCALL MODE (manifest concalls_available: false) — REWORK ROUND (run 2)

No earnings-call transcript exists for TLL on BSE, Sep-2024 to Sep-2026
(B00.input_gaps, confirmed by company memory and step1 brief). This report
runs the degraded procedure: it reads the four investor decks (Nov-2025,
Jan-2026, May-2026, Aug-2026), the FY26 and FY25 Annual Reports (MD&A,
Chairman's Message, Directors'/Board's Report), the four results filings
(original and refiled H1 sets, H2/FY26 audited, Q1 FY27 unaudited), the
statement of deviation, and Reg 30 filings.

This is a REWORK run. The phase-1 gate returned REWORK on a 50% red-flag
acceptance rate (Verifier B). Eight items are assigned to this stage:
gate-recommendation.md items 2, 3, 5, 6, 7, 8, 9, 11. Each was re-checked
against the primary source myself, not taken on the auditor's word. All
eight are ACCEPTED; the source excerpts are quoted below. `credibility_grade`
is regraded from **C to D** on this run (item 11), for the reasons in the
CREDIBILITY GRADE section.

LOAD-BEARING FACT LBF3 (subsidiary build vs delivery) remains this stage's
first verification priority; nothing in the rework changes its status.

---

## REWORK RESOLUTION (items 2, 3, 5, 6, 7, 8, 9, 11)

**Item 2 (CRITICAL, gate-rec caught in part -> ACCEPT, corrected).**
Run-1 called the FY25 CFO/CFF restatement "not a deck matter". Wrong: the
decks themselves carry it, undisclosed. Nov-2025 deck p31: FY25 "Cash from
Operating Activities" **-349.31**, CFF **747.12** (20251113 deck line 669,
675). Jan-2026 deck p31: same figures repeated (20260120 deck carries the
identical table structure). May-2026 deck p31: FY25 CFO **+197.07**, CFF
**200.73**, no note (20260509 deck line 644, 650). The FY26 results
cash-flow statement shows why: "Add: Changes in Working Capital Facilities"
of **920.49 (FY26) / 545.38 (FY25)** is added inside "Cash Generated from
Operations" before "Net Cash Flow from Operating Activities" (20260507-FY26
-H2-results.txt p8, lines 373-389). Net Cash from Operating Activities FY25
= 197.07; FY25 CFO *before* that addback ~= 197.07 - 545.38 = **-348.31**,
matching the Nov/Jan decks' -349.31 within rounding. The two earlier decks
reported FY25 CFO on the basis *excluding* the working-capital-facilities
addback; the May-2026 deck switched, with no note, to the as-filed basis
that *includes* it. This is a within-company, undisclosed change of
cash-flow basis across two of TLL's own investor decks, not merely an
AR-level presentation question. It bears directly on the Pillar 2
cash-conversion input and on this stage's credibility grade. **ACCEPTED,
carried into the grade below.**

**Item 3 (MAJOR, gate-rec caught in part -> ACCEPT, corrected).**
Run-1 said the standalone-revenue mislabel ("Revenue from Operations" =
Total Income) was "silently corrected" in later documents. Wrong: the
mislabel is *repeated* in the FY26 Board's Report itself, the highest-
authority document in the corpus. May-2026 deck p28: "Revenue from
Operations stood at Rs 10,607.05 lakhs" (20260509 deck lines 562-563) --
the audited results show Sales/Income from Operations Rs 10,189.95 lakh +
Other Income Rs 417.10 lakh = Total Income Rs 10,607.05 lakh (20260507
results p7, "TOTAL INCOME 10,607.05", lines 5432-5436). The FY26 Board's
Report text states: "Your Company has revenue from operations of
Rs 10607.05 Lacs and EBITDA of Rs 2850.1 Lacs" (AR FY26 lines 1609-1614) --
the *same* mislabelled figure, filed four months after the May-2026 deck,
in the statutory report to shareholders. Separately, the Aug-2026 deck's
own "Income Statement" table (p32-33) correctly states standalone FY26
revenue from operations at Rs 101.9 Cr and shows *operating* EBITDA margin
**falling** from 25.8% to 23.9% (-187 bps) even as the May-2026 deck called
margins "stable at 27%" on the total-income basis (20260803 deck lines 723,
1008; 20260509 deck line 559). Run-1 found one instance and called it
corrected; there are at least three total-income-as-revenue instances
(Nov-2025 deck p29, Jan-2026 deck p29, May-2026 deck p28) plus the Board's
Report repeat, and the margin-direction effect (stable vs falling,
depending on basis) was missed entirely. **ACCEPTED, corrected and
expanded.**

**Item 5 (MAJOR, gate-rec missed -> ACCEPT).**
Q1 FY27 results, standalone P&L note, shows "Depreciation and Amortization
Expenses" across four columns as **69.81 / 4.15 / 51.19 / 185.93** (20260729
results, line 124; read as Q1 FY27 / Q4 FY26 / Q1 FY26 / FY26 full year).
Q4 FY26 D&A of 4.15 sits against Q3 FY26's 71.23 (Jan-2026 deck p27, line
532) and Q1 FY27's own 69.81 -- a one-quarter collapse to near zero with no
note anywhere in the corpus. Separately, the Jan-2026 deck's 9M FY26 PBT of
**1,667.60** (20260120 deck line 565) does not equal H1 FY26 PBT of
1,110.46 (20251113 deck line 570) plus Q3 FY26 PBT of 592.39 (20260120 deck
line 534): 1,110.46 + 592.39 = 1,702.85, a gap of **35.25**. Run-1's
promise-delivery tracker cited the 9M figures without testing the
arithmetic. **ACCEPTED.**

**Item 6 (MAJOR, gate-rec missed -> ACCEPT).**
FY26 results note 8: "The Board of Directors have decided to Change the
Method of Consolidation of Financial Statements from Proportionate Method
to Equity Method as per AS-21. However, the change ... do[es] not have
material impact on the Audited Financial Statements" (20260507 results
lines 861-864). The Q1 FY27 results still describe consolidating "the
above-mentioned portion of Assets and Liabilities" of the five subsidiaries
(20260729 results lines 366-369), the language of proportionate
consolidation, not equity method. The Q1 FY27 auditor's review report cites
"Indian Accounting Standard 34 'Interim Financial Reporting'" (20260729
line 228) while the results themselves state preparation under "Indian
GAAP" (20260507 line 424-427; TLL is not an Ind AS filer). This basis
confusion sits under the consolidated margin story the AR's own MD&A tells:
cost of materials rose 68% against 48% revenue growth, taking gross margin
down 690 bps to 40.7%, "more than offset by operating leverage in
overheads, with employee benefits expense down 11% to Rs 10.8 crore and
other expenses down 5% to Rs 13.7 crore," lifting EBITDA margin 470 bps to
21.8% (AR FY26 MD&A, lines 1284-1291) -- even as the *standalone* operating
EBITDA margin fell 187 bps (Aug-2026 deck, above). A consolidated cost base
falling in absolute rupees while revenue rises 48% is consistent with a
change in which entities and what share of their costs get pulled into the
consolidated numbers; the company's own "no material impact" line has not
been tested by anyone in this pipeline. This is not settled here -- it is
a live, unresolved question for Stage 11/FTTCP, not an input to be waved
through on the "no material impact" assertion. **ACCEPTED.**

**Item 7 (MAJOR, gate-rec missed by stage 5 -> ACCEPT).**
AR FY26 consolidated Note 22 lists "Claim Income" of **541.05 (FY26) /
522.17 (FY25)** (lines 12437-12439), a line item separate from "Other
Income" (4.70 / 0.35, line 12434-12436). Against consolidated PBT of
2,719.28 (FY26) and 1,361.49 (FY25) (AR lines 13080-13083, 13172-13175 --
restated across the ratio tables), Claim Income is **19.9% of FY26 PBT and
38.4% of FY25 PBT**. The AR MD&A's own text: "Profit before tax doubled to
Rs 27.2 crore from Rs 13.6 crore" (AR FY26 MD&A, line 1292) never names
Claim Income, nor does the Chairman's Message. Run-1's Section 2D flagged
only the LLP corporate guarantees as a narrative gap; it did not find Claim
Income at all, despite the note sitting inside the same AR this stage
already read for other purposes. **ACCEPTED.**

**Item 8 (MAJOR, gate-rec caught in part -> ACCEPT, corrected).**
AR FY26 MD&A: registrations by region are Africa 64%, Asia 21%, Latin
America / CIS the balance (AR lines 404-405, 419), described near AR p17
(lines 782-791) as the company's own clearest read of future revenue. The
*export revenue* region split for FY26 is the inverse: "Asia became the
largest [export destination] at roughly 57% of export revenue, followed by
Africa at 25% and South America at 17%, a change from FY25 when South
America led" (AR lines 1263-1267). Domestic sales, which need no export
registration at all, rose from 30% to approximately 49% of total revenue
and are credited in the same paragraph to "widening sales and marketing
reach" (AR lines 1263-1272), not to the registration pipeline. Registered
products rose by only 30 in the six months from Sep-2025 (1,061) to
Mar-2026 (1,091) (Nov-2025 deck p5; May-2026 deck p5). Run-1's Section 1C
noted the domestic-mix shift and called the strategic-priorities slide
"templated" but never set the registration-by-region split against the
export-revenue-by-region split, which is the direct test of the "clearest
indicator" framing, and the test fails: the region where registrations are
concentrated (Africa, 64%) is not the region driving revenue (Asia is the
largest export destination, and domestic -- needing no registration --
drove the actual FY26 growth). **ACCEPTED, added as a new finding.**

**Item 9 (MAJOR, gate-rec missed -> ACCEPT).**
Nov-2025 deck p15: "ointments being the second largest category which
accounts for 36% of the revenue" (toothpaste/mouthwash/ointments, line
278-279). May-2026 deck p15: "Tablets are by far the largest product
category, accounting for 67% of the revenue," with a second category (read
in context as capsules) at "30% of the revenue" (lines 273-277), and states
in the same breath: "The product mix has remained fairly-stable over the
years with tablets contributing the highest revenue" (lines 287-288). AR
FY26 MD&A: "The product mix has stayed broadly stable over recent years,
with tablets consistently the leading category" (AR lines 1293-1295). The
Aug-2026 deck's own consolidated segment chart shows Capsules rising from
Rs 6.8 Cr to Rs 30.6 Cr (+350% cumulative per the chart labels) and
"Others" (the toothpaste/mouthwash/ointment/suspension/syrup bucket)
falling from Rs 49.0 Cr to Rs 30.1 Cr (-38%) (20260803 deck lines 816-828).
A category moving from 36% of standalone revenue to roughly 1% (per run-1's
own 4A/4C reading of the same Aug-2026 deck slide, now cross-checked) while
another rises 350% is not "fairly stable" or "broadly stable" by any
reading, and the claim is repeated three times (two decks plus the AR)
against the company's own segment data each time. Run-1 never set the
"stable" language against the segment chart. **ACCEPTED.**

**Item 11 (Credibility grade -> REGRADED C to D, with basis).**
See CREDIBILITY GRADE AND RATIONALE below.

**No peer_questions[] change.** None of items 2, 3, 5, 6, 7, 8, 9 or 11
surfaces a new claim that requires a peer cross-check the existing six
questions do not already cover (debtor days / registration-conversion /
injectable-ramp / pricing / industry-growth questions stand, and stage 6
already consumed this list). Item 8 (registration-thesis vs export-region
mismatch) is an internal-consistency finding, not a peer-verifiable one, so
it does not generate a seventh question. **peer_questions[] unchanged from
run 1.**

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Every growth trigger / catalyst named across the four decks and two ARs

| Trigger | Type | Timeframe | Confidence | Specificity | Classification |
|---|---|---|---|---|---|
| "Triple our consolidated business over the next three years" | Both | Long (FY26 base to ~FY29) | Aspirational | Numeric target, no path/milestone schedule given | SECTORAL/VOLUME |
| TNS Pharma peak revenue Rs 40 Cr, 80% utilisation, 30% steady-state EBITDA, 20% PAT | Both | Not dated | Aspirational | Numeric but undated | VOLUME/COST |
| Trident Mediquip peak revenue Rs 70 Cr, 85% utilisation, 24% EBITDA, 13% PAT | Both | Not dated | Aspirational | Numeric, undated | VOLUME/COST |
| TLL Parenterals peak revenue Rs 200 Cr, 90% utilisation, 27% EBITDA, 19% PAT; revenue from FY27 | Both | FY27 start, peak undated | Committed on timing, aspirational on peak | Numeric, partially dated | VOLUME |
| TLL Wellness peak revenue Rs 10 Cr; commercialisation from FY27 | Both | FY27 start | Committed on timing, aspirational on peak | Numeric, partially dated | VOLUME |
| TLL Elements peak revenue Rs 20 Cr | Revenue | Not dated | Aspirational | Numeric, undated | VOLUME |
| 300-400 additional product registrations each year | Volume | Annual, ongoing | Planned (verbatim in all 4 decks) | Numeric, specific | REGULATORY-POLICY/VOLUME |
| Registration pipeline as the driver of "future revenue" | Volume | Ongoing | Management-asserted, contradicted by the region test (item 8) | Qualitative claim, tested and failed against the company's own region data | REGULATORY-POLICY |
| Cephalosporin ("TLL Cefa") facility "planning underway" | Capacity | Not dated | Aspirational | Named but no capex/date | INORGANIC |
| Main-board migration to BSE/NSE (postal ballot outcome 17-Jul-2026) | Structural | Not yet effective | Committed (shareholder-approved) | Dated milestone, effective date not yet in corpus | REGULATORY-POLICY |
| Domestic mix shift as growth driver (30% FY25 to 49% FY26) | Volume/mix | Realised, ongoing | Committed (delivered), but credited to "sales reach" while its own promoter-LLP counterparties are unnamed (Stage 8/B12b item 4, not re-litigated here) | Numeric, audited | VOLUME/PRICE-MIX |
| Consolidated EBITDA margin +470bps to 21.8% (chairman: "operating leverage") | Margin | FY26, delivered on a stated basis | Committed (stated), but the basis includes a consolidation-method change management calls immaterial (item 6, unresolved) | Numeric, but basis-dependent | COST |

### 1B. Quantified guidance table

| Claim | Number | Timeframe | Stated in |
|---|---|---|---|
| Triple consolidated business | 3x revenue | Next 3 years from FY26 base | Aug-2026 deck p5; NOT restated in FY26 AR's own MD&A/Outlook filed one month later (AR pp 16-17, 28) |
| TNS Pharma / Mediquip / Parenterals / Wellness / Elements peak revenue | Rs 40 / 70 / 200 / 10 / 20 Cr | Undated | Aug-2026 deck pp 11-15; introduced for the first time in that deck, after the FY26 AOC-1 subsidiary shortfalls were already known internally |
| Product registrations added each year | 300-400 | Annual, ongoing | All 4 decks, verbatim |
| Consolidated revenue Rs 129.0 Cr FY26; standalone Rs 101.9 Cr FY26 | Delivered | FY26 | AR FY26 MD&A p27; Aug-2026 deck p27-32 (consistent across both) |
| Standalone FY26 "Revenue from Operations" mislabel | Rs 10,607.05 lakh stated as revenue, is Total Income (Rs 10,189.95 lakh revenue + Rs 417.10 lakh other income) | FY26, repeated | May-2026 deck p28; FY26 AR Board's Report lines 1609-1614 (item 3, corrected finding: the AR repeats it, not corrects it) |
| Consolidated Claim Income | Rs 541.05 lakh FY26 / Rs 522.17 lakh FY25, unnamed against "PBT doubled" | FY26 / FY25 | AR FY26 consolidated Note 22 (item 7) |
| Registration IPO allocation utilised | Rs 51.87 lakh (Jun-2025) rising to Rs 75.81 lakh (Mar-2026) of Rs 513.66 lakh allocated | IPO to date | Statement of Deviation 28-Jul-2025; AR FY26 line 1677-1681 |
| Working-capital facilities addback (undisclosed basis change across decks) | Rs 920.49 lakh (FY26) / Rs 545.38 lakh (FY25) | FY26/FY25 CFO | 20260507 results p8; decks restate FY25 CFO from -349.31 (Nov/Jan) to +197.07 (May) with no note (item 2) |

### 1C. Trigger evolution across the four decks

- **Registrations**: registered count rose by only 30 in six months (1,061
  to 1,091) while the "clearest indicator" framing stays unchanged across
  the AR and decks; the region test (item 8) shows the framing does not
  match where FY26 revenue actually came from (domestic, and Asia exports,
  not the Africa-heavy registration base). STRENGTHENING (pipeline depth,
  verbatim claim), but the claim itself is now a tested-and-failed one, not
  merely unverified.
- **"Triple in three years" and subsidiary peaks**: appear for the first
  time in the Aug-2026 deck, never restated in the FY26 AR's own, more
  measured Outlook filed a month later. NEW, unwalked-back, not tested by
  a second document from the same management.
- **TLL Parenterals commissioning**: "Under Construction" (Nov/Jan/May
  decks) to "Commercial implementation ... 2026" (Aug-2026 deck p10), with
  Rs 0 revenue in Q1 FY27 and nil turnover in the FY26 AOC-1.
- **Cash-flow basis**: undisclosed change from an ex-working-capital-
  facilities basis (Nov/Jan decks) to the as-filed, facilities-inclusive
  basis (May deck) for the *same* FY25 comparative figure (item 2). This is
  a genuinely new, materially different finding from run 1, which called
  this "not a deck matter."
- **Revenue-from-operations basis**: Total Income mislabelled as Revenue
  from Operations recurs in three decks and the FY26 Board's Report itself
  (item 3), not "silently corrected."
- **Product mix**: called "fairly stable"/"broadly stable" in the May-2026
  deck and the FY26 AR while the company's own segment chart shows Capsules
  +350% and the toothpaste/ointment/other bucket -38% (item 9).
- No trigger visibly DROPPED between decks; the strategic-priorities slide
  repeats near-verbatim across all four, a mild negative on its own
  (templating), now compounded by the region and product-mix contradictions
  above.

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| FY25 AR Outlook | Generic, "sustainable growth," no numeric target | Directional pass: FY26 consolidated revenue +48%, EBITDA +89%, PAT +84% | No target to test |
| H1 FY26 deck | "Outlook ... strong ... grow at both standalone and consolidated levels" | Delivered directionally (revenue +50.3% standalone, +48.4% consolidated for FY26); but the deck's own EBITDA-margin claim rests on a basis this stage now finds unreliable (item 3) | None given |
| Q3 FY26 deck | "Outlook for the remaining year & coming year remains strong" | Delivered on revenue; the cited 9M PBT figure does NOT reconcile with H1+Q3 (item 5, gap Rs 35.25 lakh), untested by run 1 | None; the gap itself was never flagged by the company |
| H2/FY26 deck | "Foundation for continued growth ... FY27 remains robust" | Not yet testable; qualitative | Qualitative |
| Aug-2026 deck | "Triple ... in 3 years"; Parenterals/Wellness revenue from FY27 | Not yet resolved; Q1 FY27 shows no subsidiary revenue line; the deck itself was never restated in the AR's more measured Outlook | None |
| Statement of Deviation | Registration-capital allocation (Rs 5.14 Cr) central to the thesis | Underdelivered: ~10.1% utilised at Jun-2025, ~14.8% by Mar-2026 (AR FY26 line 1677-1681, updating run 1's stale Jun-2025-only figure) | Boilerplate ("balance amount ... required to be utilised") |
| FY26 AR Board's Report | "Revenue from operations of Rs 10607.05 Lacs" | This figure is Total Income, not revenue from operations (item 3); the statutory report itself repeats the deck's error rather than correcting it | None; no acknowledgement anywhere in the corpus |
| FY26 AR MD&A ("PBT doubled to Rs 27.2 crore") | Claim Income of Rs 5.41 Cr (19.9% of consolidated PBT) is folded into that PBT, unnamed | Undisclosed composition of the reported result (item 7) | None |

**Tally**: delivered = 3 (revenue growth directional passes), partial = 2
(FY27 outlook qualitative, registration capital underdelivered but
accelerating), missed = 3 (9M PBT reconciliation, revenue-from-operations
mislabel repeated in the statutory filing, Claim Income unnamed against a
PBT-doubled claim). This tally is materially worse than run 1's
delivered=4/partial=2/missed=1; the rework items move three items that run
1 scored delivered or left untested into missed.

### 2B. Excuse pattern analysis

No missed-target explanation of substance exists anywhere in the corpus.
Where a gap exists (subsidiary peaks vs actuals, registration-capital
underspend, the revenue mislabel, the 9M PBT gap, Claim Income, the
"stable" mix claim, the registration-region mismatch), the company's own
documents either say nothing (silence) or repeat the same imprecise
framing in a later, higher-authority document without correction (the
Board's Report repeating the deck's mislabel is the clearest instance).
This is **SILENCE**, not external-blame; the run-1 finding that one candid
admission exists (subsidiary utilisation "modest," AR p17) still stands and
is a genuine, if isolated, positive. Revised classification: **silence-
heavy, with the one candour instance outweighed on this run by five
newly-confirmed items of unacknowledged imprecision across the decks and
the statutory Board's Report.**

### 2C. Tone ratings (1-5, revised)

| Dimension | Rating (run 2) | Evidence |
|---|---|---|
| Transparency | **2/5** (down from 3) | The revenue-from-operations mislabel repeats in the Board's Report itself (item 3); Claim Income is unnamed against a "PBT doubled" claim (item 7); the cash-flow basis change is undisclosed across two decks (item 2) |
| Specificity | 4/5 (unchanged) | Decks carry granular numeric detail quarter to quarter; the "triple" and subsidiary-peak claims remain the undated exception |
| Consistency | **2/5** (down from 3) | The 9M PBT figure does not reconcile with H1+Q3 (item 5); the consolidation-method basis is inconsistent between the FY26 note and the Q1 FY27 note (item 6); "stable" product-mix language is repeated three times against contradicting segment data (item 9) |
| Accountability | 2/5 (down from 3) | No instance found of management naming and owning any of the seven items above after the fact |
| Defensiveness | N/A | No analyst Q&A exists in this mode |
| Over-promotion | 3/5 (unchanged) | "Triple," Rs 80 Cr "intrinsic value," named peak-revenue figures for pre-revenue subsidiaries sit well ahead of the audited base |

### 2D. What they are NOT saying (revised)

- No quantified milestone path from Rs 129 Cr (FY26) to the "triple in
  three years" target.
- **No naming of Claim Income** (Rs 5.41 Cr, 19.9% of FY26 consolidated PBT)
  anywhere the "PBT doubled" claim is made (item 7, new this run).
- **No naming of the consolidation-method change** (proportionate to
  equity) or its interaction with the 470bps consolidated margin expansion
  claim, despite the standalone margin falling over the same period (item
  6, new this run).
- **No reconciliation of the 9M PBT figure**, nor any note on the near-zero
  Q4 D&A (item 5, new this run).
- **No acknowledgement that the registration pipeline's regional
  concentration (Africa 64%) does not match where FY26 revenue growth
  actually came from** (domestic, and Asia exports) despite the registration
  pipeline being framed as the clearest read of future revenue (item 8, new
  this run).
- No mention of the auditor's KAM, the goodwill jump, the Section 197
  breaches, or the LLP corporate guarantees anywhere in investor-facing
  material (carried from run 1, B02/B03).

### 2E. Repeated question tracker

NO REPEATED UNANSWERED QUESTIONS FOUND (unchanged; no analyst Q&A exists in
this corpus).

---

## SECTION 3: COMPETITIVE INTELLIGENCE (unchanged from run 1 except item 8 cross-reference)

### 3A. Competitors
Not found; no competitor is named in any deck or AR.

### 3B. Industry and market intelligence
Unchanged from run 1: global pharma CAGR ~7.1% (2024-2030), India pharma
exports ~USD 31.11 Bn FY26, domestic pharma sector growth 7-9%, PLI/API/
Biopharma SHAKTI schemes (AR FY26 MD&A p24-25).

### 3C. Toughest questions
Not applicable; no analyst Q&A exists in this mode.

### 3D. Customer and order-book signals (revised per item 8)
- Export destination mix: Asia (57%) overtook South America as the largest
  FY26 export destination, followed by Africa (25%) and South America
  (17%) (AR FY26 lines 1263-1267). **This directly contradicts the region
  where the registration pipeline is concentrated (Africa 64%, item 8)**, a
  finding run 1 did not test.
- Domestic mix rose from 30% to 49% of revenue, credited to "widening
  sales and marketing reach," with no mention that a material share of
  that domestic growth runs through promoter-interest LLPs (Talon, Tench;
  Stage 8/B12b item 4, not re-litigated here, but load-bearing for reading
  this claim).
- No customer wins, losses, renewals, or pricing renegotiations named in
  any document.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (revised)

| Priority | Trigger | Type | Timeframe | Conviction | Confirms | Kills |
|---|---|---|---|---|---|---|
| 1 | TLL Parenterals begins commercial revenue | Volume | FY27 (in progress) | M | Any Parenterals revenue line > Rs 0 in FY27 results/AOC-1 | FY27 AOC-1 shows Rs 0 again, or delay reported |
| 2 | Consolidated revenue trajectory toward "triple in 3 years" | Volume | 3 years (FY26-FY29) | **L, downgraded**: the consolidated margin story this target implicitly rests on already carries an unresolved consolidation-method question (item 6) | FY27 consolidated revenue growth holds at/above ~48-56% CAGR AND the consolidation basis is clarified with no material restatement | FY27 growth decelerates, or the equity-method change is later shown to have flattered FY26 |
| 3 | Product-registration IPO capital deployment accelerates | Regulatory | Ongoing | L (14.8% deployed by Mar-2026, updated from run 1's 10.1%) | Step-up in utilisation in the next deviation statement | Allocation remains substantially unutilised |
| 4 | Registration-region and revenue-region alignment | Regulatory/Volume | Ongoing | **L, new this run**: the registration-drives-revenue framing already fails the region test (item 8) | Africa-region revenue (export or domestic) rises to match the 64% registration concentration | The mismatch persists or widens |
| 5 | Claim Income line explained and its recurrence tracked | Cost/governance | FY27 AR | M, new this run | FY27 Note 22 (or equivalent) names the counterparty/nature and the line shrinks as a share of PBT | Claim Income recurs near 20-40% of PBT, unexplained |
| 6 | 9M/annual PBT and D&A reconciliation | Governance | Next results cycle | M, new this run | Company issues a note reconciling the 9M FY26 gap or the near-zero Q4 D&A | No note, and a similar unreconciled interim figure recurs |
| 7 | Cash-flow-statement basis (Changes in Working Capital Facilities) restored/disclosed | Cash/governance | FY27 AR | M | Line explained with a note, or removed | Line recurs unexplained, or a further basis change appears across decks with no note |

### 4B. QUESTIONS FOR PEER VERIFICATION (unchanged from run 1; stage 6 already consumed this list -- see REWORK RESOLUTION above for why no seventh question was added)

- {question: "What debtor days / receivable-ageing profile do RoW distributors in Africa, LatAm and CIS typically carry for a registration-led exporter, and how does 208 days (TLL FY26) compare?", why: "Tests whether TLL's debtor-day jump is company-specific or sector-standard for these markets", check_peers: ["CAPLIPOINT", "SENORES", "INNOVACAP"]}
- {question: "What ramp timeline and margin profile did your own injectable-plant commissioning show in the first 2-4 quarters after start-up, and how does that compare to TLL Parenterals' claimed 90% peak utilisation and 27% steady-state EBITDA margin for a facility that has not yet booked revenue?", why: "TLL's Parenterals claims are aspirational and undated; peer evidence is the only cross-check on plausibility", check_peers: ["CAPLIPOINT", "SENORES"]}
- {question: "In your own transition from loan-licence/contract manufacturing to owned-plant manufacturing, what EBITDA-margin uplift did you actually realise per vertical, and over what timeframe?", why: "Tests TLL's central thesis against a peer that has already made the same transition", check_peers: ["INNOVACAP", "CAPLIPOINT"]}
- {question: "How many new product registrations do you add per year, and what share of your registration pipeline converts to revenue within 1.5-3 years?", why: "Sanity-checks TLL's registrations-to-revenue claim, the deck's core value driver", check_peers: ["CAPLIPOINT", "SENORES", "INNOVACAP"]}
- {question: "What device-segment pricing trends and competitive intensity have you seen in RoW markets over the last four quarters?", why: "Tests Trident Mediquip's device-margin claims; partial cross-check only", check_peers: ["INNOVACAP"]}
- {question: "Have you cited any specific industry growth rate on your own calls, and does it match or diverge from the Frost & Sullivan / IBEF figures TLL's AR cites?", why: "Cross-checks whether TLL's AR macro citations are consistent with comparable exporters", check_peers: ["CAPLIPOINT", "SENORES", "INNOVACAP"]}

### 4C. Management quality verdict table (revised)

| Dimension | Verdict | Basis |
|---|---|---|
| Guidance specificity | Mixed | Highly specific on registrations/countries/financial bridges; aspirational and undated on "triple"/peak claims |
| Guidance-vs-AR consistency | Weak | "Triple"/peaks never restated in the AR's own, more measured Outlook |
| Investor-document accuracy | **Weak, downgraded** | Revenue-from-operations mislabel repeats in the statutory Board's Report (item 3); 9M PBT does not reconcile (item 5); Claim Income unnamed against "PBT doubled" (item 7) |
| Narrative-vs-data consistency | **Weak, new this run** | "Stable"/"broadly stable" product mix asserted three times against a segment chart showing a 350% swing (item 9); registration-drives-revenue framing fails the region test (item 8) |
| Candour on shortfalls | Mixed | One unprompted admission ("modest" subsidiary utilisation, AR p17); silence on every other item above |
| Filing integrity (refilings) | Positive, narrower than run 1 stated | No substantive figure changed in either refiling; the same trade-payable bifurcation defect was flagged by BSE twice (H1 FY25 and H1 FY26), a process-repeat run 1 did not name |
| Financial-reporting quality (carried) | Weak | Undisclosed CFO reclassification, unexplained goodwill jump, Section 197 breaches, LLP guarantees outside consolidation |
| **Overall grade** | **D** | See below |

### 4D. Concall-mode red flags (revised, additive to B02/B03/B12b)

- **FLAG-DISCLOSURE (revised, upgraded)**: Total Income mislabelled as
  "Revenue from Operations" recurs in three decks (Nov-2025, Jan-2026,
  May-2026) AND in the FY26 Board's Report itself. Severity: **MODERATE**
  (upgraded from run 1's MINOR-to-MODERATE; the statutory-filing repeat is
  the material change).
- **FLAG-CASHFLOW (new, this run)**: FY25 standalone CFO is presented on
  two different bases with no note across three decks: -349.31 (Nov, Jan)
  vs +197.07 (May), the difference being the undisclosed working-capital-
  facilities addback. Severity: **MAJOR** (this is a Pillar 2 cash input,
  not a cosmetic deck issue).
- **FLAG-RECONCILIATION (new, this run)**: 9M FY26 PBT (1,667.60, Jan-2026
  deck) does not equal H1 + Q3 (1,702.85), a gap of Rs 35.25 lakh; Q4 FY26
  D&A (4.15) is near zero against Q3 (71.23) and Q1 FY27 (69.81), unnoted.
  Severity: **MINOR-to-MODERATE** (small absolute amounts, but signals weak
  interim-figure control).
- **FLAG-CONSOLIDATION (new, this run)**: the FY26-to-equity-method change
  is called immaterial while the Q1 FY27 filing's own language still
  describes proportionate consolidation, and the consolidated margin story
  (470bps expansion) runs opposite to the standalone margin (187bps
  contraction) over the same period. Severity: **MAJOR**, unresolved,
  flagged for Stage 11/FTTCP rather than settled here.
- **FLAG-DISCLOSURE (new, this run)**: consolidated Claim Income (Rs 5.41
  Cr FY26, 19.9% of PBT) is unnamed against the "PBT doubled" claim.
  Severity: **MODERATE**.
- **FLAG-NARRATIVE (new, this run)**: registration-pipeline regional
  concentration (Africa 64%) does not match FY26's actual revenue drivers
  (domestic, and Asia exports). Severity: **MODERATE**.
- **FLAG-NARRATIVE (new, this run)**: "fairly stable"/"broadly stable"
  product-mix language, repeated across two decks and the AR, contradicts
  the company's own segment chart (Capsules +350%, other categories -38%).
  Severity: **MODERATE**.
- **FLAG-GOVERNANCE (carried, contextualised)**: "triple in three years"
  and subsidiary peaks introduced only in the Aug-2026 deck, after the
  FY26 audited subsidiary shortfalls were known, never carried into the
  AR's own Outlook. Severity: MODERATE.
- **FLAG-PROCESS (carried, corrected)**: Lorem ipsum placeholder text in
  the Aug-2026 Reg 30 deck; BSE flagged the same trade-payable bifurcation
  defect in both H1 FY25 and H1 FY26 refilings, a repeat run 1 scored
  cleanly Positive without naming. Severity: MINOR.

---

## CREDIBILITY GRADE AND RATIONALE

**Grade: D** (regraded from C on this run; item 11).

NO-CONCALL MODE rule: `credibility_grade` defaults to C; it may rise to B
only on documented AR-guidance-vs-results delivery evidence; it never
rises to A; it may go **lower** than C on the evidence. Run 1 held the
grade at C. This run finds that the weight of newly-confirmed evidence
takes the grade below C:

1. The revenue-from-operations mislabel is not an isolated deck slip; it
   recurs in the FY26 **Board's Report**, the statutory document signed by
   the directors, four months after the first deck instance. A mislabel
   that survives into the statutory filing is a materially different
   finding from a deck typo later fixed.
2. The FY25 CFO figure is presented on two incompatible bases across three
   decks with no note, and the difference is exactly the disclosed-but-
   unexplained working-capital-facilities addback that B02/B03 already
   flagged at the AR level. The decks carrying this too means the
   inconsistency is not confined to one filing; it is a pattern across the
   whole investor-communication set.
3. Interim figures do not reconcile (9M PBT gap, near-zero Q4 D&A), and the
   consolidation basis is described two different ways across two
   consecutive results filings, underpinning a margin-expansion claim that
   runs opposite to the standalone-basis result over the same period.
4. Claim Income (19.9%-38.4% of PBT across the two years shown) is never
   named against a headline "PBT doubled" claim.
5. The registration-pipeline narrative is directly contradicted by where
   FY26 revenue actually came from, and the "stable product mix" claim is
   directly contradicted by the company's own segment chart, each restated
   multiple times without correction.

Against this: one genuine, unprompted candour instance (subsidiary
utilisation "modest," AR p17), and clean refiling arithmetic (no
substantive figure changed on either refiling, though the same BSE defect
recurred twice). These two positives do not offset five independently
sourced, repeated instances of unacknowledged inconsistency across the
decks and the statutory Board's Report inside a single twelve-month
window. The mode's rule requires the grade to be earned on delivery
evidence; the net evidence this run adds is negative, and material enough
to cross from C ("mixed") into D ("poor") rather than merely holding C.

The grade feeds Role 1 probability weights at **Poor (45/40/15)** per the
framework table (Master Prompt v3.3), not Mixed (35/45/20).

---

## INPUT GAPS CARRIED FORWARD (unchanged from run 1)

- concalls/: EMPTY, DECLARED (no-concall mode; B00).
- shareholding/: filed pattern absent; screener aggregation used, weighed
  not anchored (B00).
- rating/: EMPTY, not a gap (company holds no credit rating).
- research/: EMPTY, no broker notes.
- No analyst-meet transcript exists in the corpus (16-Sep-2026 Arihant
  Capital conference intimation, outcome not yet filed).
