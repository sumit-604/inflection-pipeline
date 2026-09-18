# Amendment 21 forward run-rate earnings base — the 2026-09-17 eight

Produced 2026-09-18 on operator request. Operator: Keerti Kaushik.

## What this is, and what it is not

**This is not part of the shallow cards and it does not change them.** The shallow framework bars
valuation outright: "No Role 1 valuation and no price target. Shallow stops before the spear and
before `/step1`" (`screens/SHALLOW_ANALYSIS_FRAMEWORK.md`, line 16), and again in Rules that must not
break: "No valuation, no target price, no buy or sell instruction" (line 93). The eight cards comply
with that and are unchanged.

Forward earnings and forward P/E are required by the framework, but by a different part of it.
**Amendment 21 (Section 1B v3.9)** defines the forward run-rate earnings base. **Amendment 20, step
1C (Section 1B v3.8 and v3.9)** requires a live dated peer table carrying "trailing P/E, clean/forward
P/E, ROCE, growth, net debt, governance". Both are Role 1 / Stage 11 machinery. Stage 11 runs after
the spear gate, after Halt 1 and after `/fttcp`. None of the eight names has reached any of those
gates; none has a `companies/<TICKER>.md` file or a Spear line.

So this worksheet is the Amendment 21 base computed early, at the operator's instruction, sitting
outside the cards.

## The one rule this worksheet does not break

CLAUDE.md: "Never estimate a missing number. NOT FOUND is the only valid fill."

Every figure below is either a filed number or arithmetic on filed numbers. **Nothing here is a
forecast.** Amendment 21's base is "the latest reported quarter's run-rate, annualised, adjusted for
known one-offs", with the rule that "Seasonal or lumpy businesses use a trailing-4-quarter base in
place of a single-quarter annualisation. The worksheet declares which basis applies."

An annualised quarter answers "what would this business earn if the last quarter repeated four
times". That is not the same question as "what will FY27 be". A real FY27 projection runs off
Amendment 26.1's basis hierarchy and the Amendment 23 Expectation Ledger, neither of which exists for
these names. Where a company has guided to a number, the guidance is quoted below and attributed.
Where it has not, the column says so.

**Market capitalisations are Bull AI identity-record values dated 2026-09-17.** They are service
fields, not filings, and they are a day stale. Every multiple below moves with them. Verify live
before using any of it.

## The table

**Corrected 2026-09-18.** The Omnitech row below was revised after the Q4 FY26 deck resolved the FY26
base. See the note under the table.

All figures Rs crore. "TTM adj" is trailing four quarters adjusted for the one-offs named in the
notes. "Basis" is the Amendment 21 declaration.

| Ticker | Mcap | FY26 PAT | TTM adj | Q1 x4 | Basis declared | Governing fwd PE | PE on FY26 | Q1 PAT YoY |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| KISSHT | 6,068 | 281.0 | 316.2 | 380.0 | Single-quarter (not lumpy) | **16.0x** | 21.6x | +59% |
| SHAREINDIA | 4,293 | 324.4 | 364.4 | 497.6 | TTM (lumpy: prop desk) | **11.8x** | 13.2x | +47% |
| KROSS | 1,455 | 55.2 | 57.8 | 53.2 | TTM (seasonal: Q4 peak) | **25.2x** | 26.4x | +24% |
| RAPPID | 160 | 6.48 | n/a | n/a | FY26 (half-yearly reporter) | **24.8x** | 24.8x | NOT FOUND |
| MOTISONS | 1,909 | 63.7 | 66.7 | 44.2 | TTM (seasonal: Q3 is the year) | **28.6x** | 30.0x | +38% |
| RAMRAT | 4,922 | 108.6 | 127.9 | 140.8 | TTM (lumpy: copper, amalgamation) | **38.5x** | 45.3x | +121% |
| ALGOQUANT | 1,837 | 32.7 | 37.6 | 66.1 | TTM adj (lumpy: 89% trading gains) | **48.8x** | 56.1x | +263% |
| OMNI | 6,672 | 79.3 | 103.8 | 118.9 | RUN-RATE (corrected 18-Sep) | **56.1x** | 84.1x | +1.4% QoQ |

## Growth: what is actually guided, versus what is merely recent

Only one company in the eight has guided to a number for FY27.

| Ticker | Guidance filed for FY27 | Latest filed growth | Independent view |
|---|---|---|---|
| SHAREINDIA | **"around 20% growth during the current financial year"** (Concall p.4). The only numeric guidance in the set. | Q1 revenue +31.3%, PAT +47.2% | CRISIL A1+ on the CP programme, no rationale held |
| KROSS | None numeric. | Q1 revenue +32.3%, EBITDA +39.5%, PAT +24.4% | India Ratings expects revenue "to improve significantly FY27 onwards" and margins "13%-13.5% in the near term" (Rating p.3) |
| OMNI | Qualitative only: "well positioned to deliver healthy growth in FY27" (IP p.5) | Q1 revenue +61.5%, EBITDA +90.8% | Infomerics upgraded to IVR A/Stable, letter only, no rationale |
| KISSHT | None numeric. CEO names the mechanism: cost of borrowings and opex to fall as AUM scales, LAP secured mix to scale up (IP p.5) | AUM +61%, PAT +59%, but RoAAUM flat at 5.0% | A-/Stable on the NBFC, agency unnamed |
| RAMRAT | None. | Q1 revenue +88.6%, EBITDA +109%, PAT +121% | CARE A-/Stable, Sept 2025, FY25 basis, stale |
| RAPPID | Qualitative only: "a very bright financial year 2026-27, certainly" (Concall p.7) | Q1 revenue +28% (unaudited update). Order book +60% YoY | None. No rating of any kind |
| MOTISONS | None. Last earnings call was June 2024. | Q1 revenue +23.3%, PAT +37.6%. FY26 revenue grew 5.8% | None |
| ALGOQUANT | None. Last earnings call was August 2023. | Q1 revenue +42.9%, PAT +263% | None |

## Notes that change how each number reads

**KISSHT, 16.0x.** The cleanest base in the set. A lending book compounds rather than swinging, so
Amendment 21's single-quarter default applies without a seasonality override. The caution is the
denominator's direction: capital adequacy is 40.19% after the May listing, so the equity base is
roughly double what the book needs, and RoAE has already fallen 411 basis points to 21.20%. Q1 FY26
PAT of about Rs 59.75 crore is derived from the deck's disclosed "+59% YoY", not separately filed.

**SHAREINDIA, 11.8x.** The lowest multiple in the set, and the least reliable earnings base. About
half of profit is proprietary trading on management's verbal account, no filing splits it, and the
June quarter's EBITDA margin jumped 16.7 points sequentially. Annualising that quarter gives 8.6x,
which is why the TTM basis governs here. Against the company's own 20% guidance, the TTM base implies
FY27 PAT near Rs 389 crore and a multiple near 11.0x.

**KROSS, 25.2x.** The most stable base in the set: TTM, Q1 annualised and FY26 all land within Rs 5
crore of each other. Note that profit growth of 24.4% already lags EBITDA growth of 39.5% because of
depreciation, and Rs 167 crore of seamless tube capex has yet to capitalise. The PAT base should be
expected to lag revenue for several more quarters by arithmetic.

**RAPPID, 24.8x, and the forward base is NOT FOUND.** As an NSE Emerge SME listing it reports
half-yearly. No profit figure exists for any period after 31 March 2026. The Q1 FY27 business update
gives revenue of Rs 14.87 crore and no earnings line. H2 FY26 annualised gives Rs 6.20 crore and
25.9x, which is a worse basis than the full year because H2 was the deliberate bidding pause. The
next earnings number is H1 FY27, due around November 2026.

**MOTISONS, 28.6x.** Jewellery is violently seasonal and the June quarter is the weakest, so
annualising it gives a meaningless 43.2x. TTM governs. One distortion to note: the Rs 150 crore QIP
closed on 11 June 2026, so the market capitalisation reflects 113.75 crore shares while the TTM
earnings were largely produced on 100.18 crore. The multiple is overstated against the deployed
business and understated against the diluted one.

**RAMRAT, 38.5x.** Converter, and CARE says so: "The company is merely a converter." Section 1B v3.7
Amendment 17 binds any Stage 11 run on this name. The Q1 PAT growth of 121% is real and it sits on a
revenue base inflated by the copper price and by the Global Copper amalgamation effective 23 June
2025, so the year-on-year comparison is not like for like. Equity share capital also doubled from
Rs 22.0 crore to Rs 46.7 crore between FY25 and FY26 and the cause is not in the corpus, which
affects any per-share work.

**ALGOQUANT, 48.8x, and treat it as a coin flip.** Net gain on fair value changes was 88.9% of Q1
revenue. Annualising a trading quarter is not a forward base in any meaningful sense; it is a bet
that the desk repeats. The TTM figure is adjusted down by Rs 7.06 crore for the deferred-tax MAT
credit recognised in Q4 FY26, which was a one-off and took that quarter's total tax to Rs 0.34 crore
on Rs 16.22 crore of pre-tax profit. Unadjusted TTM gives 41.1x.

**OMNI, 56.1x. CORRECTED 2026-09-18.** This worksheet first marked the base unreliable because the
Q1 FY27 deck states FY26 revenue two ways. The Q4 FY26 deck, already in the corpus, resolves it: FY26
revenue Rs 5,113.0 million and FY26 profit after tax Rs 793.4 million, against FY25 of Rs 3,429.1
million and Rs 438.7 million (Q4 FY26 deck, p.5, p.7). The Q1 deck's "FY26" column is FY25 mislabelled.
Trailing P/E is therefore 84.1x, not 152.1x, and FY26 profit grew 80.9%. The depreciation point stands
and can now be sized: FY26 depreciation was Rs 481.6 million, about Rs 120 million a quarter, against
Rs 62.7 million in Q1 FY27, so roughly Rs 17 crore a year of pre-tax benefit flows into FY27 reported
profit. Read the growth as about 28% underlying rather than the 50% the reported numbers will show.

## What this does not answer

A forward P/E is one number. Amendment 20's step 1C requires it inside a live dated peer table of four
to six comparables with ROCE, growth, net debt and a governance flag on each row, and it explicitly
bars multiples carried from model memory. This session has no live web access, so no peer table can
be built here. Anything comparing these multiples to a peer group has to come from Claude web.

Nor is a low multiple a verdict. SHAREINDIA is cheapest in the table at 11.8x and half its earnings
are unverifiable; ALGOQUANT is near the dearest at 48.8x and its transition is running backwards. The
card verdicts stand on the evidence, not on these numbers.
