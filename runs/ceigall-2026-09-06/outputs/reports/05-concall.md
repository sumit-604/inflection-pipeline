# Stage 5: Concall Analysis — Ceigall India Ltd (CEIGALL) — RUN 3 (TARGETED PATCH)

Run date: 2026-09-06 | Model: claude-sonnet-5

RUN 3 NOTE: this is a targeted patch on RUN 2, not a rebuild. Run 2 raised red-flag
coverage from 48% to 70% and that work stands. A second independent audit named a
short list of specific residual gaps plus one arithmetic error. This run closes
those gaps and re-emits the complete block. What changed from run 2:

1. ARITHMETIC CORRECTED. Run 2 recomputed the May-2026 filed erratum on unencumbered
   cash and FDR as a ~41.5% overstatement and said the original ~71% figure "conflates
   an absolute rupee change with a percentage." That diagnosis was wrong. The original
   ~71% is the correct reading. Run 2's 41.5% answers a different question (the
   restatement-down percentage against the pre-correction figure). Full arithmetic
   shown at 2F.9 below. Severity stays HIGH.
2. ONE MISSED CRITICAL REPEATED EVASION added: Mahesh Patil (ICICI Securities) asked
   in two consecutive quarters whether the margin beat was a one-off; both times the
   answer was an unrelated list of newly started projects, never a yes or a no. This
   bears on whether the FY26 margin is a sustainable valuation base, so it is added to
   Section 2E and to repeated_evasions[], not filed as a tone note.
3. MISSED GUIDANCE ITEMS added and tested: the FY27 renewable-revenue guidance
   (20-25% of total revenue) against a Q1 FY27 call that discloses zero renewable
   revenue; the Q1 FY27 standalone growth print (10.2%) against the "minimum 15%"
   FY27 guidance reaffirmed in the same call.
4. MISSED DISCLOSURES added as red flags: 100% IPO-proceeds utilisation plus royalty
   cessation, disclosed as an aside one quarter before an Rs859cr FY27 equity plan;
   cash disclosed on three different bases in three quarters (the Rs320cr FD figure
   was absent from run 2); an unexplained "1.5 years to dilute another 8%" comment and
   an uncorrected "post-QIP" analyst premise; a false "we were always guiding 10% to
   15%, our growth is much more than that" claim against the same call's own 9M
   growth figures.
5. TWO ITEMS RE-WEIGHED: the Northern Ayodhya revenue collapse (a deny-then-concede
   answer, not "plausible and seasonal, not disputed"); Ceigall's "fully compensated"
   escalation-cost claim, now checked against a peer transcript and Stage 6's finding
   that all three peers describe the same MoRTH mechanism as partial and time-boxed.
6. MINOR ITEMS added: a bid-pipeline figure that does not sum to its own components
   and coexists with two other uncorrected totals in the same call; a 10x typo in the
   Sahebganj project value left uncorrected in the filed transcript; an intra-call
   Ramban-Banihal arithmetic inconsistency; an uncorrected analyst solar/BESS figure;
   "seven projects ahead of schedule" sitting next to an unresolved Jalbehra EOT.
7. CITATION RULE ENFORCED. Run 2's page citations mixed the PDF's own `[PAGE N]`
   marker with the transcript's printed "Page N of M" header, which runs consistently
   one page behind the marker in all four files (page 1 of each PDF is the unpaginated
   BSE/NSE cover letter, so printed header N corresponds to marker N+1). This run
   re-derived every citation touched by a fix directly from the marker, and corrected
   roughly 30 further carried-forward citations found to have the same one-page
   offset during that pass (listed inline where corrected; substance in every case was
   already right, only the page number moves). No claim in run 2 is withdrawn.

Everything else run 2 established — the four-call primary read, the cross-call
reconciliation section (now 2F.1-2F.9), the promise-delivery tracker, the tone
ratings, the silence findings — stands and is carried forward.

Transcripts read, all PRIMARY, oldest first:
1. Concall_Nov_2025_Transcript.pdf — Q2 and H1 FY26, call 17-11-2025 (15 pages)
2. Concall_Feb_2026_Transcript.pdf — Q3 and 9M FY26, call 13-02-2026 (14 pages)
3. Concall_May_2026_Transcript.pdf — Q4 and FY26, call 07-05-2026 (11 pages)
4. Concall_Aug_2026_Transcript.pdf — Q1 FY27, call 10-08-2026 (13 pages)

CITATION CONVENTION: every citation below is the PDF's own `[PAGE N]` marker,
verified in this run by locating the quoted text directly under that marker, not by
reading the printed "Page N of M" header inside the page. Where a page number
differs from run 2's, this run's number is the one independently re-derived from the
marker.

No results filing, rating, shareholding, or substantive-announcements corpus exists
for this run. Promise-versus-delivery and reconciliation testing runs
transcript-against-transcript and against the FY26 annual report figures already
anchored in B01/B02/B03. One peer transcript (HGINFRA-Concall_May_2026_Transcript.txt)
and B06-peers.yaml are used in this run for the margin/escalation re-weighing (FIX 5),
per the run brief's instruction to read them for context.

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Every growth trigger, catalyst or driver mentioned

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| Order book scale-up (Rs12,598cr Sep-25 -> Rs13,295cr Dec-25 -> Rs18,554cr Mar-26 -> Rs18,568cr Jun-26) | VOLUME | Near-medium | Committed (delivered numbers each call) | High |
| HAM monetization / "execute-monetize-recycle" capital-recycling cycle | INORGANIC | Near-medium | Planned -> one deal (Malout-Abohar-Sadhuwali) confirmed closed by Aug-26 | Medium (price never given in any of four calls) |
| Renewables + T&D diversification (solar, BESS, substations) | SECTORAL/VOLUME | Medium | Planned/aspirational; the FY27 guided 20-25%-of-revenue share (May-26 call, p.5) has zero disclosed renewable revenue behind it one quarter in (Aug-26 call) — see 1B and red flags | Medium, weakening after Q1 FY27 |
| NHAI/MoRTH policy tailwind: Rs3.1 lakh cr FY27 budget (+8%), tighter eligibility norms | REGULATORY-POLICY | Near | Committed (government data cited) | Medium |
| Monthly billing / monthly escalation-compensation notification, tied by management to an unnamed "war" | REGULATORY-POLICY | Near | Committed, but the "fully compensated" framing is contradicted by peer evidence — see 2F.9 and red flags | Low (notification never named or dated precisely) |
| International expansion (Singapore, Dubai entities; Romania and UAE bids) | INORGANIC/SECTORAL | Long, aspirational | Aspirational ("baby steps," "very conservative") | Low |
| EBITDA margin resilience (11%-12.5% band, "plain vanilla EPC") | COST/PRICE-MIX | Near | Committed guidance, but sustainability of the beat is a repeated evasion — see 2E | High |
| Debt reduction / balance-sheet optimisation | COST | Near | Committed, but disclosure quality collapsed across the four calls (see 2F.6) | Declining |
| AI/data tools in bidding and project monitoring | COST | Long | Aspirational | Low |
| Commercial paper issuance (Rs100cr), new in Aug-26 | COST | Near | Committed | Medium |

### 1B. Quantified guidance, by quarter stated

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Revenue growth | 10%-15% YoY | FY26 | Nov-25 call, p.7; reaffirmed Feb-26 call, p.7 ("we are on track") |
| Revenue growth | Minimum 15% YoY | FY27 | May-26 call, p.5; reaffirmed Aug-26 call, p.8-9 |
| Revenue growth (standalone, actual) | Q1 FY27 standalone revenue grew 10.2% YoY (Rs901cr vs Rs818cr) against the "minimum 15%" FY27 guide reaffirmed in the SAME call; only the 15.7% consolidated figure was volunteered | Q1 FY27 | Aug-26 call, p.5 (actual), p.8-9 (guidance reaffirmed) — NEW in this run, see red flags |
| Renewable share of total revenue | "Close to 20% to 25%" of FY27 total revenue | FY27 | May-26 call, p.5 — NEW in this run; Aug-26 call discloses zero renewable revenue line one quarter in, see red flags |
| EBITDA margin | 11%-12.5% ("plain vanilla EPC") | FY26/FY27 | Nov-25 call p.14 (exact "11-11.5%" phrase; corrected from run 2's p.9, which found only a looser "11.5%" mention); May-26 call p.5/p.7; reaffirmed Aug-26 call, p.7-8 (corrected from p.7) |
| Order inflow | Rs5,000cr | FY26 | Nov-25 call, p.9-10; reiterated Feb-26 call, p.11 (tightened from p.10-11 — the quote sits only on p.11) |
| Order inflow (actual) | Rs11,332cr (2.27x the guided figure) | FY26 | May-26 call, p.4 |
| Order inflow guidance | "Around INR5,800 crores" ("incremental of 15%" over the original Rs5,000cr FY26 guide, not over the Rs11,332cr actually delivered) | FY27 | Feb-26 call, p.11 |
| Order inflow guidance (restated) | "Minimum INR5,500 crores" | FY27 | May-26 call, p.5 (corrected from run 2's p.4) |
| Order inflow guidance (restated again) | "INR6,000 crores" | FY27 | Aug-26 call, p.8 (tightened from p.7-8 — the quote sits only on p.8) — third distinct FY27 order-inflow figure inside 6 months, no acknowledgment of any change |
| Order inflow (Q1 FY27 actual) | "Close to INR600cr" against the Rs6,000cr FY27 target | Q1 FY27 | Aug-26 call, p.8 (tightened from p.7-8) |
| Standalone debt | Rs614.8cr (Sep-25) -> Rs552cr (Dec-25) -> D/E only, no Rs figure (Mar-26) -> not disclosed at all (Q1 FY27) | Nov-25 to Aug-26 | See 2F.6 for the full degrading trail |
| Consolidated debt | Rs1,341.2cr (Sep-25) -> Rs1,421cr (Dec-25) -> D/E only, no Rs figure (Mar-26) -> not disclosed at all (Q1 FY27) | Nov-25 to Aug-26 | See 2F.6 |
| Capex | Rs25-30cr FY26; Rs30-35cr FY27 | FY26/FY27 | Feb-26 call, p.11; Aug-26 call, p.8 |
| Cash incl. FD | Rs225cr | Dec-25 | Feb-26 call, p.11 |
| Unencumbered cash / FDR (Mar-26) | Stated Rs266cr / Rs146cr; corrected in the filed transcript to Rs166cr / Rs75cr | Mar-26 | May-26 call, p.6 (written erratum in the filed document) — see 2F.9 for the corrected arithmetic |
| FDs on the books | Rs320cr | Jun-26 | Aug-26 call, p.11 — a THIRD, non-comparable cash basis; NEW in this run, see red flags |
| HAM equity infusion pace target | Rs297cr in "coming 3 months" (whole HAM book) | Nov-25 -> ~Feb-26 | Nov-25 call, p.11 (corrected from run 2's p.10) |
| HAM equity infusion, same call, different subset | Rs200cr in "next 3 months," named as VRK 11/12 + Ludhiana-Bathinda + Northern/Southern Ayodhya only | Nov-25 -> ~Feb-26 | Nov-25 call, p.12 — no bridge offered between this and the Rs297cr figure on p.11 (corrected) of the same call |
| HAM equity infused (cumulative) | Rs603.2cr (Oct-25) -> Rs605.6cr (Dec-25), a ~Rs2.4cr addition against the ~Rs297cr targeted for that window | Q3 FY26 | Nov-25 call p.5; Feb-26 call, p.4 |
| HAM equity total commitment | Rs1,391cr (existing HAM) + Rs395cr (two new HAM) + ~Rs810cr (solar/T&D) = ~Rs2,596cr | Q3 FY26 | Feb-26 call, p.7 (Rs1,391cr, Rs395cr split), p.10 (Rs810cr solar figure) — corrected from run 2's p.9-10 |
| Pending equity commitment (revised) | Rs1,937cr over next 3 years (Rs800cr renewable, ~Rs1,137cr HAM/roads) | FY26 call | May-26 call, p.7 (corrected from p.6) |
| Equity infused, cumulative (post-IPO basis) | Rs253cr at IPO + Rs439cr more = Rs692cr "as on today" | Q1 FY27 | Aug-26 call, p.6 |
| Equity infused, Q1 FY27 alone | Rs23cr | Q1 FY27 | Aug-26 call, p.9 |
| Balance equity commitment | Rs859cr (Rs310cr solar + Rs550cr HAM) FY27; Rs744cr (Rs300cr solar + Rs444cr HAM) FY28 | FY27/FY28 | Aug-26 call, p.6-7 |
| Per-project HAM equity list (Aug-26) | Nine named projects sum to Rs567cr against a stated total of Rs550cr | FY27 | Aug-26 call, p.10-11 — see 2F.7, does not close |
| HAM project count | "All 11 of our HAM projects" (Q&A) vs "10 HAM projects" in the same call's own order-book table | Q1 FY27 | Aug-26 call, p.5 (10 HAM) vs p.10 (11 HAM) — see 2F.7 |
| Malout-Abohar-Sadhuwali sale price | NEVER STATED in any of the four transcripts; an analyst-quoted ~Rs177cr (Feb-26 call, p.12, corrected from p.11) neither confirmed nor denied | — | — |
| Malout-Abohar-Sadhuwali sale status | "In-principle approved a binding offer" (Feb-26) -> "binding document...validates our execute-monetize-recycle framework" (May-26) -> "successful monetization...completed" (Aug-26) | Feb-26 to Aug-26 | See 2F below and Section 2B |
| Bathinda-Dabwali / Jalbehra-Shahbad divestment close | "Before September" 2026 | Feb-26 call, p.12-13 |
| Bathinda-Dabwali / Jalbehra-Shahbad divestment close (revised) | Q2 FY27 / Q3 FY27 | May-26 call, p.9 (corrected from p.8) — then zero mention in Aug-26, past the original "before September" deadline |
| Renewable share of order inflow | 35.02% of FY26 total order inflow | FY26 | May-26 call, p.4 (corrected from p.3) |
| Renewable share of order book | 22% (Sep-25, of Rs12,598cr) -> ~23.8% (Dec-25, of Rs13,295cr, Rs3,168cr absolute) -> 19% (Mar-26, of Rs18,554cr, Rs3,525cr absolute) | Nov-25 to May-26 | Nov-25 p.4 (corrected from p.3); Feb-26 p.4; May-26 p.4 (corrected from p.3), p.6 — see 2F.5, does not close against the inflow claim |
| International order-inflow target | "At least 10 to 15%" of FY27 order inflow | FY27 | Feb-26 call, p.11 — never repeated in May-26 or Aug-26 |
| Ramban-Banihal (J&K) tunnel completion | "In the next 3 months" (i.e. ~Feb-26) | Nov-25 -> ~Feb-26 | Nov-25 call, p.12 — never mentioned again |
| Ramban-Banihal billing | ~Rs180cr (20% of the tunnel work) billed "before this March" 2026 | Nov-25 -> Mar-26 | Nov-25 call, p.12 — never mentioned again; does not cohere with other figures in the same exchange, see 2F.8 (NEW) |
| Ramban-Banihal viaduct completion | "By March '27," using redesigned steel girders | Nov-25 -> Mar-27 | Nov-25 call, p.12 — never mentioned again |
| Southern Ludhiana bypass land | "Very clear...80% land cleared by December" 2025 | Nov-25 call, p.8 (tightened from p.7-8) |
| Southern Ludhiana bypass land (later) | "Only 62% available with us, so that is a challenge" | Aug-26 call, p.6 — a regression against the earlier 80%-by-December promise, not merely a delay |
| NHAI awarding, FY26, km and Rs value | NEVER GIVEN a company number (twice deflected to "check the NHAI website") | — | Feb-26 call, p.8-9; May-26 call, p.9-10 |
| Q1 FY27 consolidated EBITDA / consolidated PAT | NOT DISCLOSED — only consolidated revenue (Rs970cr, +15.7%) given; both figures were disclosed in the two prior calls | Q1 FY27 | Aug-26 call, p.5, checked against the full Q&A too |
| Nov-25 bid pipeline | Stated total Rs14,320cr, own segment components sum to Rs14,382cr, Rs14,000cr used twice more in the same call, an analyst's Rs16,000cr left uncorrected | H2 FY26 | Nov-25 call, p.6 (total + components), p.10, p.14 (Rs14,000cr), p.11 (analyst's Rs16,000cr) — NEW in this run, see 2F.8 and red flags |
| Sahebganj project value, restated | "One INR21,160 crores project" — a 10x typo for the Rs2,160cr Sahebganj-Areraj-Bettiah HAM award, left uncorrected in the filed transcript | FY26 | May-26 call, p.12 — NEW in this run, see red flags |
| Solar/BESS order book | Rs3,168cr (management, cumulative renewable orders) vs Rs3,500cr (analyst figure, uncorrected) | Q3 FY26 | Feb-26 call, p.4 (Rs3,168cr) vs p.7 (Rs3,500cr, analyst, uncorrected) — NEW in this run |
| Projects completed ahead of schedule | "Seven of our projects have completed ahead of schedule" | To date, as of Feb-26 | Feb-26 call, p.5 — sits against Jalbehra, named later in the SAME call as delayed and awaiting an EOT (p.12), bonus eligibility unresolved and never revisited — NEW in this run |

### 1C. Trigger evolution across all four quarters

- **Order book / diversification**: STRENGTHENING every quarter in absolute size (Rs12,598cr -> Rs13,295cr -> Rs18,554cr -> Rs18,568cr). Renewable share of order book fell from 22% (Sep-25) to 19% (Mar-26) even as the renewable rupee figure grew (Rs2,772cr to Rs3,525cr) — a share dip on a bigger base, not itself alarming, but see 2F.5 for a genuine arithmetic gap between the renewable order book and the renewable inflow claim.
- **HAM monetization**: STRENGTHENING in narrative terms across all four calls (one deal narrated from "in-principle" through "binding" to "sold"/"successful monetization"), but the sale price has never been disclosed in any of four calls, and the "before September" 2026 target for the next two deals (Feb-26) was pushed to Q2/Q3 FY27 by May-26, then dropped without any update in Aug-26, past the original deadline.
- **International expansion**: UNCHANGED in stated caution ("baby steps," "very conservative") across all four calls, but the underlying pipeline claim swung wildly — a Romania bid quoted at ~Rs13,000cr for one 17km project (May-26, ~65-70% of the entire order book by the analyst's own math) — then went unmentioned in Aug-26 next to a new, never-identified excuse ("this war situation," Aug-26, p.12, tightened from p.11-12). The 10-15%-of-inflow international target set in Feb-26 was never repeated.
- **NHAI awarding pace**: management declined to quantify twice (Feb-26, May-26), each time citing the NHAI website — UNCHANGED (evasive both times); a third attempt at the question in Aug-26 was lost to a dropped call, not a clean data point either way.
- **Margins**: management's stated position STRENGTHENED in specificity only after repeated analyst pressure — the May-26 call finally clarified that FY24/FY25 headline EBITDA included one-off bonus/royalty income the FY26/FY27 guided band strips out, but only on the third round of one analyst's questioning. Separately and more directly, whether the margin BEAT itself is sustainable was asked twice by name (Mahesh Patil, May-26 and Aug-26) and answered both times with a list of newly started projects, never yes or no — see 2E, NEW in this run and treated as a valuation input, not a tone finding. Segment-level (renewable/T&D) margin bifurcation was asked in all four calls and answered with a number in none (see 2E).
- **Renewables revenue guidance**: NEW STRAIN visible one quarter in. May-26 guided renewables at 20-25% of FY27 total revenue; Aug-26 (Q1 FY27) discloses zero renewable revenue line at all, and neither Morena (PPA now signed, Aug-26 p.4, but land/transmission status for the BESS not updated in this call) nor Rewa (PPA and land done, transmission still pending, Aug-26 p.6) has started billing. One quarter of zero delivery does not kill an annual guide, but it is the first data point against it and nobody on the call connects the two — see red flags.
- **Standalone revenue growth**: Q1 FY27 print of 10.2% YoY standalone sits well under the "minimum 15%" FY27 guide reaffirmed in the SAME call (Aug-26, p.8-9); only the 15.7% consolidated figure was volunteered in the opening remarks, and no analyst raised the standalone shortfall against the guide. Too early in the year to call a miss, but the gap is real and unaddressed — NEW in this run, see red flags.
- **NEW in Aug-26, no forward reference in the three earlier calls**: commercial paper issuance (Rs100cr) against working-capital limits; the ROE (14%)-versus-ROCE(~19-20%) divergence question; 100% utilisation of IPO proceeds and cessation of royalty income (p.11), disclosed only as an aside — see red flags.
- **DROPPED, no update or follow-up in any later call**:
  - Jaipur Rail Corporation project (Rs918cr, L1 status announced Feb-26, p.4) — never mentioned again; LOA status unresolved (contrast with Sahebganj-Areraj-Bettiah, also L1 in Feb-26, which DID convert to a confirmed LOA by the May-26 call).
  - Ramban-Banihal (J&K) tunnel: three specific, time-bound promises made in Nov-25 (tunnel in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027) — none mentioned again in Feb-26, May-26 or Aug-26, despite management having called the project "a great learning" and "an amazing job." No analyst asked either. The three figures given in that same Nov-25 exchange also do not cohere with each other — see 2F.8, NEW in this run.
  - Working-capital-day target asked in Nov-25 (p.11) — never given a number; a similar-spirit question in Aug-26 (p.10, tightened from p.9-10) again got only a qualitative "definitely there will be an improvement," no number.
  - Consolidated debt disclosure: full loan-type breakdown (Nov-25) -> aggregate Rs figure only (Feb-26) -> D/E ratio only, no Rs figure (May-26) -> nothing at all (Aug-26). See 2F.6.
- **NEVER APPEARING in any of the four calls, despite being current-year, audited, material events**: the Rs89.65m procurement fraud, the qualified IFC opinion (both levels), the DGGI GST search action, the NHAI termination of the step-down SPV (Ceigall Ludhiana Rupnagar Greenfield Highway), the associated subsidiary auditor resignation, the contingent-liability rise to 83.7% of standalone net worth, and any leadership-change explanation (see Section 2 below).

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker (chronological, all four calls)

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| Nov-25 call | FY26 revenue growth 10%-15% | DELIVERED — FY26 standalone revenue growth 14.3%, consolidated 17.1% (May-26 call, p.5, tightened from p.4-5) | N/A (delivered) |
| Nov-25 / Feb-26 calls | FY26 order inflow guided at Rs5,000cr | DELIVERED/BEATEN — FY26 actual order inflow Rs11,332cr, "significantly surpassing" guidance (May-26 call, p.4, corrected from p.3-4) | N/A (beaten) |
| Nov-25 / Feb-26 calls | Continued standalone deleveraging | DELIVERED — standalone D/E fell to 0.2x by Mar-26 vs 0.3x (Sep-25) vs 0.4x (FY25); note the Rs-figure trail behind this ratio thinned to nothing by Aug-26 (see 2F.6) | N/A (delivered on the ratio; disclosure quality behind it declined) |
| Nov-25 call | 11-11.5% EPC margin band, no compromise on margin for growth | DELIVERED — FY26 standalone EBITDA margin 12.6% (May-26 call, p.5, tightened from p.4-5), within/above the "plain vanilla EPC" band each quarter | N/A (delivered) |
| May-26 call | Ambala-Chandigarh-Zirakpur HAM progressing toward concession | DELIVERED — concession agreement signed in Q1 FY27 (Aug-26 call, p.4, corrected from p.3) | N/A (delivered) |
| Nov-25 call | HAM equity infusion pace: Rs297cr targeted in "coming 3 months" | MISSED — cumulative HAM equity rose only from Rs603.2cr (Oct-25) to Rs605.6cr (Dec-25), ~Rs2.4cr, against the ~Rs297cr targeted for the window | No explanation offered; no analyst raised the shortfall in the Feb-26 call |
| Nov-25 call | Southern Ludhiana bypass land: "very clear...80% land cleared by December" 2025 | MISSED, a regression not merely a delay — by Aug-26 (Q1 FY27), management states the land is "only 62% available," below even the pre-December baseline framing, and names it directly as "a challenge" | No explanation for why the promised 80%-by-December milestone was not met, and no intervening call (Feb-26, May-26) flagged the slip before it surfaced in Aug-26 |
| Nov-25 call | Ramban-Banihal tunnel completion in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027 | CANNOT BE VERIFIED — never mentioned again in any of the three subsequent calls; no delivery evidence, no miss acknowledgment, simply dropped. The three figures do not cohere with each other in the original exchange either — see 2F.8 | No explanation; no analyst re-asked |
| Feb-26 call | Malout-Abohar-Sadhuwali sale proceeds "before 31st March" 2026 | PARTIAL — SPA signed 3-Jun-2026, completed 16-Jun-2026 per AR (B03), ~2.5 months late; May-26 call still described it as a "binding document," not yet executed; only confirmed as done ("successful monetization") in the Aug-26 call | Timing slip never acknowledged as a slip; described in May-26 as "expecting it should get executed in this month" with no reference back to the original March target |
| Nov-25 / Feb-26 calls | VRK 11, VRK 12, Indore-Ujjain appointed dates, targeted Dec-25 through Mar-26 | MISSED/PARTIAL — appointed dates for VRK 11, VRK 12 and Indore-Ujjain arrived "subsequent to the quarter end" of Q1 FY27, i.e. Jul/Aug-26, a 4-8 month slip; no mention of these appointed dates at all in the May-26 call | No explanation for the slip beyond routine land/forest-clearance commentary in the Feb-26 call; the slip itself is never named as a slip. (Southern Ludhiana is correctly excluded from this group — its appointed date has still not arrived as of Aug-26; it is tracked separately above as its own missed promise.) |
| Feb-26 call | Bathinda-Dabwali and Jalbehra-Shahbad HAM divestments "targeting to close before September" 2026 | MISSED, silently revised then dropped — May-26 call pushed the same two deals to Q2 FY27 (Jul-Sep) and Q3 FY27 (Oct-Dec); Aug-26 call gives no update at all, past the original September deadline | Revision never flagged as a change from the earlier "before September" target |
| Every call | "Cash flow will not be a challenge," "equity is not a problem," "amazing cash flow available" (May-26, p.6 and p.8, corrected from a blanket p.6-7) | Cannot be graded delivered/partial/missed against a results filing that does not exist in this corpus; tested instead against B03's audited figures: consolidated CFO was negative in both FY25 (Rs -515.6cr) and FY26 (Rs -91.3cr) | Never reconciled on any call; the assertion of comfortable cash flow is never squared with the negative consolidated CFO in the audited accounts. Not counted in the tallies below (no results filing to grade it against), but carried into red_flags and the credibility grade as the single most consequential finding |

**Counts: delivered 5, partial 2, missed 3** (11 testable rows; the cash-flow narrative and the Ramban-Banihal tunnel row are tracked but excluded from the count for the reasons stated in each row — unchanged from run 2; this patch adds no new testable promise-delivery row because the new items in this run are guidance items too young to grade (renewables revenue, Q1 FY27 standalone growth), not delivered/missed promises).

### 2B. Excuse pattern analysis

- Northern Ayodhya bypass revenue collapse to ~Rs42cr (Aug-26 call, p.5-6, corrected from p.4-5): RE-WEIGHED this run. Vaibhav Shah asks directly why Q1 execution fell to ~Rs42cr. Ramneek Sehgal's answer, read in full, is a DENIAL followed by an EXTERNAL EXCUSE followed by a MILESTONE-MISS CONCESSION, all in one breath: "No, no. I mean, it is going proper. There's nothing. Now, from last 1.5 months, there's been rain. Otherwise, progress is steady. We've been achieving all our milestones before ahead, before time. It's just -- sometimes you don't achieve the milestone, payment can only be made only once the milestone is achieved." The flat "there's nothing" denial is contradicted by the final clause's own admission that a milestone was in fact missed. Run 2 called this "plausible and seasonal, not disputed"; on the actual quote, it is a DEFLECTION-THEN-CONCESSION, the same pattern already identified for the margin-optics exchange below, and is treated here as a genuine credibility item, not a tone note (see red flags).
- Southern Ludhiana bypass land shortfall (Aug-26 call, p.6): attributed to land availability at 62% — EXTERNAL-BLAME (department-side); the underlying number is itself a genuine regression against the Nov-25 "80% by December" framing, not merely a restated delay (see 2A).
- ROE decline to 14% vs stable ROCE ~19-20% (Aug-26 call, p.12): attributed entirely to post-IPO/QIP equity-base expansion — plausible, standard attribution, not independently verifiable in this corpus (no shareholding/ratio corpus). Note: the analyst's own premise names a "post-QIP" raise that management does not correct either way — see red flags (NEW).
- Margin "decline" in Slide 41 optics (May-26 call, p.10-11): initially answered "EBITDA margin is stable, that's not decreasing... has grown up as compared to the previous year," then, on a second and third round of the same analyst's questioning, corrected to acknowledge FY24/FY25 EBITDA included one-off bonus/royalty income — DEFLECTION on the first two passes, HONEST-ADMISSION only after repeated pressure. This first answer is directly contradicted by the same call's own reported numbers: standalone FY26 EBITDA margin was 12.6% against 12.8% in FY25 (May-26 call, p.5, tightened from p.4-5) — margin fell, not grew. See 2F below.
- Margin SUSTAINABILITY (NEW, distinct from the margin-optics item above): Mahesh Patil (ICICI Securities) asks directly, in TWO CONSECUTIVE quarterly calls, whether the margin beat is a one-off. May-26 call, p.10: "is there any one-off... are we seeing any impact [of] the iron ore cost inflation" — answered with "we have started four HAM projects which have majorly contributed to the PAT margins," a list of newly started projects, no yes or no. Aug-26 call, p.7-8: "what led to this improvement, and can we see similar margins in the upcoming quarters or was there any one-off this quarter?" — answered with "we have started 3 new projects in this quarter... This will basically improve the numbers as well going forward in future," again a project list, again no yes or no. DEFLECTED both times by the identical device (a list of newly started projects, not an answer to the one-off question asked). See 2E; this bears directly on whether the FY26/Q1 FY27 margin can be treated as a durable base for valuation.
- Escalation-cost "full compensation" claim (May-26 call, p.10, corrected from p.9): RE-WEIGHED this run using peer evidence. Ramneek Sehgal states plainly, "The increased cost is already compensated by the department; they already come up with the circular for compensating the escalation part... whatever increase in the cost, that we can that will be paid by the authority ultimately to the EPC contractor" — a categorical, unqualified claim of full pass-through. In the identical quarter (Q4 FY26, Jan-Mar 2026), peer HGINFRA's standalone margin fell to 9.37% with management directly attributing the fall to "geopolitical uncertainties, prolonged monsoon, higher commodity prices... cost escalation" (HGINFRA-Concall_May_2026_Transcript.txt, p.6), and Stage 6 (B06-peers.yaml) independently finds all three peers describe the same MoRTH notification as PARTIAL and TIME-BOXED, not a full guarantee. Ceigall's claim is not merely unverified; it is CONTRADICTED by sector evidence for the same mechanism in the same quarter. This moves from a tone note to a red flag (see below).
- PPT slide-38 equity-invested error (Feb-26 call, p.6): management directly said "It's a mistake, but otherwise entire equity has been put by the company only" — a rare, clean HONEST-ADMISSION.
- Cash/FDR figure correction (May-26 call, p.6): handled as a silent written erratum appended to the filed transcript rather than a live correction or any subsequent-call acknowledgment — closer to SILENCE than honest-admission, given the scale is a ~71% overstatement of the exact liquidity figure used to support the funding narrative (see 2F.9, corrected this run).
- Fraud, IFC qualification, NHAI termination, auditor resignation, leadership churn, contingent-liability growth: SILENCE across all four calls — never raised proactively, never asked, never addressed.
- Segment margin bifurcation (renewables/T&D vs core EPC): asked, in some form, in all four calls (Nov-25 p.14, corrected from p.13; Feb-26 p.13; May-26 p.7-8; Aug-26 p.10, tightened from p.9-10) and answered with an actual number in NONE — see 2E, a four-quarter repeated evasion.
- Pattern check: management readily and proactively raises OPERATIONAL wins (order wins, appointed dates, margin beats) but never proactively raises the governance/compliance/cash-flow items the audited accounts carry as top findings. When pressed on a genuinely uncomfortable number or claim (margin optics, Northern Ayodhya revenue, margin sustainability, escalation compensation), the pattern is consistent: an initial deflection or denial, softening only under repeated pressure or only in the final clause of the same answer. No instance across four calls of management naming a compliance or governance issue unprompted.

### 2C. Tone ratings (1-5, evidence-based)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | Granular operational numbers volunteered freely, but total silence on fraud, IFC qualification, NHAI termination, leadership churn, and contingent liabilities across four calls; a material cash/FDR figure required a written post-hoc correction of ~71% (2F.9); consolidated debt and consolidated P&L disclosure both thinned to nothing by the fourth call; 100% IPO-proceeds utilisation and royalty cessation surfaced only as an aside inside an other-income answer (Aug-26, p.11) |
| Specificity | 4/5 | Project-by-project equity figures, appointed-date timelines, and margin bridges given in detail whenever asked, even where the figures themselves later fail to reconcile (see 2F.7, 2F.8) |
| Consistency | 1/5 | HAM/renewable equity-commitment totals quoted on different, unreconciled bases in every call; FY27 order-inflow guidance restated three times (Rs5,800cr -> Rs5,500cr -> Rs6,000cr) without acknowledgment; a nine-line per-project equity list in Aug-26 does not sum to its own stated total; the same call states both "10 HAM projects" (order book table) and "all 11 of our HAM projects" (Q&A); the Nov-25 bid pipeline stated total does not sum to its own components and coexists with two other figures for the same quantity in the same call (2F.8); cash disclosed on three non-comparable bases in three consecutive quarters |
| Accountability | 2/5 | One clean admission on a PPT typo; no admission of the HAM equity-infusion pace miss, the Southern Ludhiana land regression, the appointed-date slippage, the divestment-timeline slippage, the Ramban-Banihal silence, or the Northern Ayodhya deny-then-concede answer; zero acknowledgment of the governance/compliance items named in the audited accounts |
| Defensiveness | 2/5 (low-moderate) | Mostly cooperative; occasional curt dismissals ("No, we don't have any project for Punjab fencing," "I don't understand your question") and one flat denial that a milestone problem existed before conceding one in the same breath (Northern Ayodhya, Aug-26); not combative when pressed on margins, eventually clarifies |
| Over-promotion | 4/5 | Frequent unqualified superlatives ("amazing cash flow," "fantastic," "validates," IRR "much more than committed") without the underlying number that would let an investor check the claim; the CFO's "margin has grown up" claim (May-26) is directly contradicted by that call's own 12.6%-vs-12.8% figure; the "fully compensated" escalation claim is contradicted by peer disclosure in the identical quarter |

### 2D. What they are NOT saying

- The Rs89.65m procurement fraud and the qualified IFC opinion (both standalone and consolidated) — a finding severe enough that the auditors themselves flagged it, never mentioned. Likely reason: reputational, 18 months post-IPO.
- The NHAI termination of the step-down SPV project and the sister-SPV auditor resignation — never mentioned. Likely reason: would raise direct execution-risk questions about the HAM portfolio the entire "capital recycling" narrative depends on.
- The DGGI GST search action on IPO-related expenses — never mentioned. Likely reason: compounds the fraud disclosure, both adverse compliance events in the same year.
- Contingent liabilities at 83.7% of standalone net worth, and the unreconciled standalone/consolidated bank-guarantee gap — never mentioned, never asked. Likely reason: no analyst appears to track this ratio; management has no incentive to introduce it.
- The consolidated CFO being negative in FY25 and FY26 — never mentioned even as management repeatedly asserts comfortable cash flow. Likely reason: the "cash is not a problem" framing is central to the entire equity-funding narrative for HAM/solar/T&D capex; a negative CFO figure would puncture that framing.
- The identity and continuity implications of the CEO/WTD change (Sudhir Hoshing out, A. Sarvanan/Saravanan in between the Feb-26 and May-26 calls) — never mentioned, never asked.
- The Malout-Abohar-Sadhuwali sale consideration — never given a number in any of four calls despite being cited repeatedly as proof of the capital-recycling thesis.
- The promoter's personal Rs20cr equity stake in the Bathinda-Dabwali HAM SPV (disclosed only as an aside answering a different question, Feb-26 call, p.6) — an asset that is itself inside the divestment pipeline (targeted for sale to third-party buyers per the same call, p.12-13). Management never returns to explain how a promoter's personal equity in an asset earmarked for third-party sale is to be treated, priced, or exited, and no analyst asks.
- Consolidated debt figures and consolidated EBITDA/PAT, both progressively withdrawn from disclosure across the four calls, culminating in zero consolidated-debt disclosure and zero consolidated-EBITDA/PAT disclosure in the Aug-26 call — never flagged by management as a disclosure change, never asked about by any analyst.
- 100% utilisation of IPO proceeds by Q4 FY26 and the cessation of royalty income (NEW, this run) — surfaced only as an aside inside an answer about the fall in other income (Aug-26 call, p.11: "We have 100% utilized the IPO proceeds in the last quarter of the FY26... Right now, we are not charging royalty"), never flagged as a standalone funding-capacity item even though it lands one quarter before management commits to an Rs859cr FY27 equity plan (Aug-26 call, p.6-7). Likely reason: an item that narrows funding optionality is easier to bury inside a routine other-income answer than to volunteer as a headline.
- The "1.5 years to dilute another 8%" comment (Nov-25 call, p.13, NEW this run) — made once, in passing, inside an answer about T&D equity funding timelines, never repeated, never explained (what triggers it, whether it is an MPS-compliance dilution or a fresh capital raise), and never revisited even when an Aug-26 analyst's question is built on a "post-QIP" premise that management leaves uncorrected (Aug-26 call, p.12). Likely reason: an unexplained future dilution overhang is not a number management volunteers to elaborate.

### 2E. Repeated question tracker

| Question | Quarters asked | Responses | Classification |
|---|---|---|---|
| "What was NHAI's awarding pace in FY26, in kilometres and in rupees?" | Feb-26 (Ketan, Avendus Spark, p.8-9); May-26 (Dheeraj Kripalani, Avendus Spark, p.9-10) | Feb-26: "any number specific... will not be correct... we can check it on NHAI website." May-26: "these are the figures which NHAI has put on their own website" (moderator then cut the line before a number was given) | Deflected every time |
| "What is the total/pending equity requirement across HAM, solar and T&D, and how does it reconcile with the figure given last quarter?" | Nov-25 (p.11-13, corrected from p.10-13, Rs788cr HAM pending + ~Rs600cr T&D); Feb-26 (p.7 and p.10, corrected from p.9-10, ~Rs2,596cr total); May-26 (p.7, corrected from p.6-7, Rs1,937cr pending); Aug-26 (p.6-7, Rs692cr cumulative + Rs859cr FY27 + Rs744cr FY28) | A new absolute figure is given every call, on a shifting scope (HAM-only vs HAM+solar+T&D; "pending" vs "total" vs "post-IPO"; different base dates), with no bridge ever offered between the previous quarter's number and the new one; no analyst has ever asked management to reconcile the two | Answer changed between quarters, never reconciled |
| "Do the renewable/T&D order book segments carry margins in line with, above, or below core EPC — can you bifurcate?" | Nov-25 (Priyam Shah, p.14, corrected from p.13, vague "yes...but we keep EPC margin 11-11.5%"); Feb-26 (Nimish Pandya, p.13, accepted a "15% plus" framing without correction); May-26 (Tejpal Singh, p.7-8, explicit refusal: "plain vanilla EPC would be minimum between 11% to 12.5%," no bifurcation given); Aug-26 (Chetrika Deshpande, p.10, tightened from p.9-10, "we have guided the same kind of margin... trying to achieve better," again no bifurcation) | See left column | Deflected every time — a four-quarter repeated evasion |
| "Was the margin beat this quarter a one-off, or is it sustainable?" (NEW this run, CRITICAL, valuation-relevant) | May-26 (Mahesh Patil, ICICI Securities, p.10); Aug-26 (Mahesh Patil, ICICI Securities, p.7-8) | May-26: "is there any one-off or if this is just because of the execution... are we seeing any impact [of] the iron ore cost inflation etcetera?" -> Kapil Aggarwal: "we have started four HAM projects which have majorly contributed to the PAT margins... going forward, we are guiding our investor between 11% to 12.5%." Aug-26: "what led to this improvement... was there any one-off this quarter?" -> Kapil Aggarwal: "we have started 3 new projects in this quarter... 2 are Maharashtra solar projects... This will basically improve the numbers as well going forward in future." | Deflected every time, by the same analyst, in two consecutive quarterly calls, with the same device (a list of newly started projects substituted for a yes/no answer). Directly bears on whether the FY26/Q1 FY27 margin is a sustainable base rather than a one-off, so this is a valuation input, not a tone finding |
| "What is the working-capital-day target/timeline for improvement?" | Nov-25 (Balasubramanian, p.11, explanation given for the rise but no target number); Aug-26 (Chetrika Deshpande, p.10, tightened from p.9-10, "definitely there will be an improvement," again no number) | See left column | Deflected every time |

### 2F. CROSS-CALL NUMERIC RECONCILIATION

**2F.1 Order-book roll-forward (opening + inflow - revenue executed = closing), every testable quarter**

| Quarter | Opening book | + Inflow | - Revenue executed (consol.) | = Implied closing | Actual closing | Gap |
|---|---|---|---|---|---|---|
| Q3 FY26 | Rs12,598cr (Sep-25, Nov-25 call p.4/p.7, corrected from p.3/p.6) | Rs1,403cr (Feb-26 call, p.4, corrected from p.3-4) | Rs991cr (Feb-26 call, p.5) | Rs13,010cr | Rs13,295cr (Feb-26 call, p.4, corrected from p.3-4) | DOES NOT CLOSE, +Rs285cr |
| Q4 FY26 | Rs13,295cr (Dec-25) | Rs6,014cr (May-26 call, p.4) | Rs1,386cr (May-26 call, p.5) | Rs17,923cr | Rs18,554cr (May-26 call, p.4) | DOES NOT CLOSE, +Rs631cr |
| Q1 FY27 | Rs18,554cr (Mar-26) | ~Rs600cr ("close to," Aug-26 call, p.8, imprecise) | Rs970cr (Aug-26 call, p.5) | ~Rs18,184cr | Rs18,568cr (Aug-26 call, p.5) | DOES NOT CLOSE, ~+Rs384cr (imprecise inflow figure widens the uncertainty band) |
| FY26 full year | Not disclosed in any of the four transcripts | Rs11,332cr | Rs4,022cr | Cannot compute | Rs18,554cr | CANNOT BE TESTED — Mar-25 opening order book never stated in these four calls |

The gap is persistently POSITIVE (closing book larger than the roll-forward implies) in all three testable quarters, averaging ~Rs433cr, ~2-3.4% of book size each quarter. No management commentary in any call explains this residual.

**CONFIRMED INDEPENDENTLY on a standalone-revenue basis (NEW this run, strengthens the finding).** Re-running the same roll-forward using standalone revenue executed instead of consolidated revenue produces the SAME persistent positive gap, of a different but still material size in every quarter: Q3 FY26, Rs12,598cr + Rs1,403cr - Rs970cr (standalone revenue, Feb-26 call, p.5) = Rs13,031cr implied vs Rs13,295cr actual, gap +Rs264cr. Q4 FY26, Rs13,295cr + Rs6,014cr - Rs1,294cr (standalone revenue, May-26 call, p.5) = Rs18,015cr implied vs Rs18,554cr actual, gap +Rs539cr. Q1 FY27, Rs18,554cr + ~Rs600cr - Rs901cr (standalone revenue, Aug-26 call, p.5) = Rs18,253cr implied vs Rs18,568cr actual, gap +Rs315cr. The gap survives the choice of revenue basis, which weakens the "scope difference between consolidated and standalone recognition" explanation and strengthens the alternative explanations already named: price-escalation/variation additions counted into the book without being reported as fresh "inflow," or the order book being stated at a broader (e.g. lifetime/O&M-inclusive) basis than either revenue line captures.

**2F.2 Order inflow claimed against guidance, tested against L1 positions without a Letter of Award**

Two projects went L1 in the Feb-26 call: Sahebganj-Areraj-Bettiah (Rs2,160cr, Bihar HAM) and Jaipur Rail Corporation (Rs918cr). Feb-26 explicitly states the LOA for Sahebganj was "not received yet" (p.8) and Jaipur Rail was "still waiting for the LOA" (p.12). By the May-26 call, Sahebganj is confirmed converted: "the LOA of Sahebganj–Areraj–Bettiah corridor...the total project cost is INR2,160 crores" (p.4), and it is referenced as the single biggest project the company has received. (Note: the SAME May-26 call, in a separate Q&A exchange, restates this project's value as "one INR21,160 crores project" — a 10x typo, uncorrected, on p.12; see 2F.8 for the pattern this fits.) Jaipur Rail Corporation, however, is NEVER mentioned again in either the May-26 or Aug-26 call — its LOA status is unresolved three quarters after the L1 announcement. If Jaipur Rail's Rs918cr contributed to the Rs8,500cr 9M FY26 order-inflow figure claimed in the Feb-26 call, or to the FY26 full-year Rs11,332cr claimed in May-26, a portion of the headline "order inflow beat" would rest on a preferred-bidder position that never converted into a binding award and has since gone silent. The transcripts do not state explicitly whether L1 wins are counted before LOA, so this cannot be confirmed as a misstatement — but the asymmetry (Sahebganj converts and is celebrated; Jaipur Rail does not convert and disappears) is itself a finding worth a direct verification question to management.

**2F.3 HAM/renewable/T&D equity committed vs equity actually infused, call by call, on a consistent scope**

CANNOT BE FULLY TESTED on a consistent scope: the basis changes every call (Nov-25: HAM-only "pending" Rs788cr, separately T&D ~Rs600cr; Feb-26: HAM total Rs1,391cr + Rs395cr new + Rs810cr solar/T&D = ~Rs2,596cr; May-26: three-year forward "pending" Rs1,937cr, Rs800cr renewable + rest HAM/roads; Aug-26: cumulative-since-IPO Rs692cr, plus FY27/FY28 forward commitments Rs859cr/Rs744cr). Directionally the trend is plausible (infused amounts step up call over call: Rs603.2cr -> Rs605.6cr -> "more than Rs400cr post-IPO" -> Rs692cr cumulative), but no single call offers a bridge from the prior quarter's number to its own, and this run could not reconstruct an exact tie-out across all four calls on one consistent scope. The two intra-Nov-25-call figures (Rs297cr vs Rs200cr "next 3 months") also do not reconcile with any bridge offered — Rs200cr is named for a named subset of projects (VRK 11/12, Ludhiana-Bathinda, Northern/Southern Ayodhya) that could plausibly sum to less than the broader Rs297cr HAM-wide figure, but management never states this explicitly, so it stands as an unreconciled internal inconsistency rather than a confirmed contradiction.

**2F.4 Consolidated vs standalone revenue, EBITDA and PAT, and any period where consolidated PAT sits below standalone PAT while consolidated EBITDA sits above it**

| Period | Standalone EBITDA | Consol. EBITDA | Standalone PAT | Consol. PAT | Anomaly? |
|---|---|---|---|---|---|
| H1 FY26 (Nov-25 call, p.7, tightened from p.6-7) | Rs185.3cr | Rs222.7cr (higher) | Rs111.8cr | Rs107.5cr (LOWER) | CONFIRMED — consol. PAT below standalone PAT despite consol. EBITDA above standalone EBITDA |
| 9M FY26 (Feb-26 call, p.5-6) | Rs305cr | Rs362cr (higher) | Rs186cr | Rs180cr (LOWER) | CONFIRMED — same anomaly persists |
| FY26 full year (May-26 call, p.5, tightened from p.4-5) | Rs487cr | Rs585cr (higher) | Rs305cr | Rs309cr (marginally HIGHER, by only Rs4cr) | Anomaly REVERSES for the full year — implied Q4-alone consol. PAT (Rs129cr) exceeds Q4 standalone PAT (Rs119cr) by enough (Rs10cr) to overcome the Rs6cr 9M shortfall, a razor-thin flip |
| Q1 FY27 (Aug-26 call, p.5) | Rs121cr | NOT DISCLOSED | Rs75cr | NOT DISCLOSED | CANNOT BE TESTED — the very quarter where this comparison would next be checkable is the quarter management stopped disclosing consolidated EBITDA and PAT entirely |

This is a genuine, precisely anchored finding: for two consecutive disclosed periods (H1 and 9M FY26), the group's below-EBITDA items (HAM SPV interest, depreciation, minority interest) consumed more than the entire consolidated EBITDA uplift over standalone, consistent with B03's audited-account finding of negative consolidated CFO in both FY25 and FY26. The full-year number only avoids the same pattern by a Rs4cr margin. The one quarter where this could next be tested (Q1 FY27) is exactly the quarter the disclosure disappeared.

**2F.5 Renewable order inflow for the year against the closing renewable order book, given near-zero renewable execution**

FY26 renewable order inflow claimed: 35.02% of Rs11,332cr = ~Rs3,968cr (May-26 call, p.4, corrected from p.3). Renewable order book: Rs2,772cr (22% of Rs12,598cr, Sep-25, Nov-25 call p.4, corrected from p.3) -> Rs3,168cr ("cumulative orders," Dec-25, Feb-26 call, p.4) -> Rs3,525cr (19% of Rs18,554cr, Mar-26, May-26 call, p.6). Given B03's finding that named renewable SPVs sat at pre-construction/early-construction stage all year (near-zero renewable revenue recognition), a roll-forward with near-zero execution should show the closing renewable book approximately equal to cumulative renewable inflow. Instead: Rs3,968cr of claimed FY26 renewable inflow against a Rs3,525cr closing renewable book is a shortfall of ~Rs443cr (~11% of the claimed inflow, ~13% of the closing book) — DOES NOT CLOSE. The same gap appears using the Dec-25-to-Mar-26 bridge alone (implied Q4 renewable inflow of ~Rs800cr against an actual Q4 renewable-book increase of only ~Rs357cr). Possible explanations not excluded by the transcripts: some renewable "inflow" counted at L1 stage was later reclassified or did not firm into an order-book position, or the two headline percentages (35.02% of inflow, 19% of book) use different scope definitions for what counts as "renewable" versus adjacent T&D/industrial-infrastructure buckets that shifted across calls. No management commentary in any call addresses this gap. The Aug-26 call adds a fresh, related data point: zero renewable revenue is disclosed one quarter into FY27, the first year this book was guided to deliver 20-25% of total revenue — see 1B and red flags.

**2F.6 Consolidated debt across calls, and whether disclosure became less complete**

| Call | Standalone debt disclosure | Consolidated debt disclosure |
|---|---|---|
| Nov-25 (p.5) | Full breakdown: Rs614.8cr total (equipment term loan Rs13.6cr, term loans Rs270.2cr, WC loans Rs331cr); D/E 0.3x | Full breakdown: Rs1,341.2cr total (equipment term loan Rs60.4cr, term loans Rs277.7cr, HAM term loan Rs672cr, WC loans Rs331cr); D/E 0.7x |
| Feb-26 (p.5, p.12) | Aggregate only: Rs552cr, no loan-type breakdown; D/E 0.28x given only in Q&A | Aggregate only: Rs1,421cr, no loan-type breakdown; no consolidated D/E given at all |
| May-26 (p.4) | Ratio only: D/E 0.2x; NO absolute Rs figure given | Ratio only: D/E 0.6x; NO absolute Rs figure given |
| Aug-26 | NOT DISCLOSED — no debt figure or ratio of any kind, at either level, in prepared remarks or Q&A | NOT DISCLOSED |

CONFIRMED: a clean, four-call progressive degradation from a full loan-type breakdown at both levels (Nov-25) to zero disclosure of any kind (Aug-26). This is not noise — each successive call drops one more layer of granularity (breakdown, then absolute Rs figure, then even the ratio), and it lands on the same call (Aug-26) that also drops consolidated EBITDA and consolidated PAT (2F.4) and the same call where 100% of IPO proceeds are disclosed as exhausted (2D, red flags). Taken together, the most recent call is the least verifiable of the four on exactly the dimensions (leverage, consolidated profitability, funding headroom) most relevant to testing the "cash flow is not a problem" claim repeated in the same period.

**2F.7 Per-project equity lists and project counts**

Aug-26 call (p.10-11): pressed by an analyst whose own math (~Rs430-440cr) did not match management's stated Rs550cr FY27 HAM equity figure, Kapil Aggarwal lists nine named projects: Ludhiana-Bhatinda Rs53cr, Northern Ayodhya Rs61cr, Southern Ayodhya Rs53cr, VRK 11 Rs97cr, VRK 12 Rs139cr, Southern Ludhiana bypass Rs38cr, Indore-Ujjain Rs60cr, Sahebganj (Bihar) Rs50cr, Zirakpur Rs16cr. These nine figures sum to Rs567cr, not the Rs550cr total stated in the same breath — DOES NOT CLOSE, a ~Rs17cr (~3%) gap, on top of the analyst's own independent ~Rs110-120cr shortfall estimate. Three different totals for the same claim now exist in one exchange (analyst's ~Rs430-440cr, management's stated Rs550cr, the list's actual sum of Rs567cr), and none is reconciled.

Separately, and independently: the same call's own order-book table (p.5) states "10 HAM projects." In the same call's Q&A (p.10), Ramneek Sehgal states the Rs550cr equity figure is "across all 11 of our HAM projects." A project count that disagrees with the order book, inside a single call — CONFIRMED, not reconciled.

**2F.8 Intra-call arithmetic that does not cohere, beyond the equity-list case above (NEW this run)**

Two further instances, both single-call, both independent of the cross-call reconciliation logic above:

*Nov-25 bid pipeline.* Ramneek Sehgal states the total bid submission as "Ceigall has submitted totalling of INR1,43,200 million," i.e. Rs14,320cr, and immediately gives its own segment breakdown: "INR88,860 million in the Road segment [Rs8,886cr], INR48,960 million in the Railway segment [Rs4,896cr], and around INR6,000 million in the Renewable segment [Rs600cr]" (p.6). These three components sum to Rs14,382cr, not the Rs14,320cr stated a sentence earlier — a small (~0.4%) but real gap in the company's own numbers. The same call then uses "INR14,000 crores" twice more for what appears to be the same bid figure (p.10, p.14), and an analyst separately quotes "nearly INR16,000 crores kind of range" for the bidding pipeline (p.11, Balasubramanian) — management's answer addresses the segment split without correcting the Rs16,000cr number. Four figures (Rs14,320cr, Rs14,382cr implied, Rs14,000cr repeated twice, Rs16,000cr from an analyst) sit for the same underlying quantity in one call, none reconciled.

*Nov-25 Ramban-Banihal figures.* In a single exchange (p.12), Ramneek Sehgal states the tunnel is on track to complete "in the next 3 months," that "20% of the tunnel work, which would be around INR180 crores would be completed before this March" (implying a total tunnel value of roughly Rs900cr), that the viaduct will complete "by March '27," and, in the same breath, that a separate related project is "totally INR369 crores and almost, I think, 54% of the project is completed and 45% financially is completed." The physical-completion (54%) and financial-completion (45%) percentages for that second project are given without reconciliation, and neither the implied ~Rs900cr tunnel value nor the Rs369cr other-project figure is checked against Vaibhav Shah's own framing of "balance work is INR385 crores for both the projects" moments earlier in the same exchange. None of these figures is individually implausible, but taken together they do not cohere, and none is revisited in any of the three later calls (this project then disappears entirely from the record, see 1C).

**2F.9 Cash/FDR erratum arithmetic — CORRECTED this run**

The May-26 call (p.6) contains a written erratum in the filed transcript: "It was erroneously mentioned that the unencumbered cash and unencumbered FDR stood at INR 266 crores and INR 146 crores, respectively. The actual figures should be read as INR 166 crores for unencumbered cash and INR 75 crores for unencumbered FDR."

Combined stated (as originally spoken on the call): Rs266cr + Rs146cr = **Rs412cr**.
Combined corrected (per the erratum, the true figure): Rs166cr + Rs75cr = **Rs241cr**.
Absolute overstatement: Rs412cr - Rs241cr = **Rs171cr**.
Overstatement as a percentage of the TRUE (corrected) figure: Rs171cr / Rs241cr = **70.95%**, i.e. ~71%.

This is the correct way to state an overstatement: the stated figure was ~71% larger than the true figure. Run 2 instead computed Rs171cr / Rs412cr = 41.5% and reported that as the overstatement, which answers a different question — how much smaller the corrected figure is relative to the ORIGINAL stated figure (a restatement-down percentage), not how much the original figure overstated the true one. Both arithmetic operations are valid computations of different quantities; only the ~71% figure answers "by what percentage was the stated cash/FDR figure overstated," which is the question this finding is about. Severity stays HIGH: this is a ~71% overstatement of the exact liquidity figure Ramneek Sehgal uses, in the same sentence, to argue "equity is not a problem with Ceigall, we have amazing cash flow available with us" (May-26 call, p.6), corrected only via a silent written erratum with no live acknowledgment on any subsequent call.

---

## SECTION 3: COMPETITIVE INTELLIGENCE FROM CONCALLS

### 3A. Competitor commentary

Management makes almost no named-competitor commentary across the four calls. The only comparative claims are generic and self-referential: "if you compare us with the peers in the market...the number of verticals and geography-wise we have grown" (Feb-26 call, p.13-14) and "our Return on Equity would be great as compared to the peers in the market" (Aug-26 call, p.9) — both asserted without a number or a named peer. Credibility check: unverifiable as stated; peer-verification stage should test the vertical/geography spread and RoE claims directly against HGINFRA/KNRCON/PNCINFRA disclosures. (Stage 6, now complete, finds Ceigall's RoE claim is not tested against a like-for-like peer figure in this corpus; see B06-peers.yaml.)

### 3B. Industry and market intelligence dropped in the calls

- MoRTH FY27 budgetary allocation raised ~8% to ~Rs3.1 lakh crore (Feb-26 call, p.3).
- NHAI overall pipeline cited at "close to Rs2 lakh crore" (May-26 call, p.9); a list of 124 NHAI/MoRTH projects worth ~Rs2 trillion cited as approved (Nov-25 call, p.6, corrected from p.5-6).
- Tightening of technical/financial bidding eligibility (higher net worth requirement, additional performance securities, greater PPP emphasis) said to favour established players — repeated in Nov-25 and May-26 calls, used consistently to support Ceigall's own positioning.
- New MoRTH notifications on monthly billing (vs milestone billing) and monthly escalation-cost compensation (vs quarterly) — cited as a direct margin/cash-flow tailwind in the May-26 call (p.7-8, p.10), attributed to "this war" happening, without ever naming which conflict or notification number, in either the May-26 or the Aug-26 call. Management's framing of this mechanism as FULL compensation is contradicted by peer evidence — see 2B and red flags.
- Renewable order-inflow composition: 35.02% of FY26 total order inflow came from renewables (May-26 call, p.4, corrected from p.3); renewables were 19% of the FY26-end order book (May-26 call, p.6) versus 22% of the smaller H1FY26 book (Nov-25 call, p.4, corrected from p.3) — a share dip on an expanding base that management does not itself flag, and which does not fully reconcile with the absolute inflow claim (see 2F.5).
- An analyst's Rs3,500cr figure for the solar-and-BESS order book (Feb-26 call, p.7, Vaibhav Shah) is left uncorrected against the Rs3,168cr renewable "cumulative orders" figure management itself gave earlier in the same call (Feb-26 call, p.4) — a ~10% gap between an analyst's stated number and management's own, unaddressed.
- "Seven of our projects have completed ahead of schedule" (Feb-26 call, p.5, corrected from p.4), an unqualified track-record claim, sits in the same call as the Jalbehra project being named as delayed by an ROW problem and a flood, awaiting an EOT before management "will be in a position to tell the investors about the bonus" (Feb-26 call, p.12, corrected from p.11) — an open item never revisited in any of the three later calls.

### 3C. Toughest analyst questions

| Question | Response | Satisfactory? | Real risk? |
|---|---|---|---|
| Maitri Shah (May-26 call, p.10-11): why are consolidated EBITDA margins on Slide 41 trending down despite guidance | Initial answer denied any decline ("EBITDA margin is stable...has grown up"); only on the third round did the CFO concede FY24/FY25 included bonus/royalty income skewing the comparison | Eventually yes, after unnecessary friction, and the initial answer was directly contradicted by the same call's own 12.6%-vs-12.8% figures | Real but resolved: the underlying operating margin is roughly stable; the initial deflection, stated against the call's own numbers, is the bigger tell |
| Mahesh Patil (May-26 call, p.10, NEW this run): is the Q4 margin beat a one-off, and is there any iron-ore/input-cost impact ahead | Answered with a list of four newly started HAM projects that "majorly contributed to the PAT margins"; the direct one-off question and the input-cost question were both left unanswered on their own terms | No — a list of projects is not a yes/no answer to either question asked | Yes — this is the question that determines whether FY26's margin beat is a durable base or a one-off; asked again in Aug-26 with the same non-answer, see below |
| Mahesh Patil (Aug-26 call, p.7-8, NEW this run): what led to the >13.5% Q1 FY27 margin, can it continue, was there a one-off this quarter | Answered with a list of 3 newly started projects (2 Maharashtra solar, 1 HAM); guidance reaffirmed at 11-12.5% only when Mahesh Patil re-asked directly | Partially — the guidance reaffirmation is a number, but the one-off question itself was never answered directly either time it was asked | Yes — a two-quarter repeated evasion on the exact question a valuation model needs answered (see 2E) |
| Vaibhav Shah (Aug-26 call, p.4-5, NEW this run): why did Northern Ayodhya execution fall to ~Rs42cr in Q1 | Denial ("there's nothing"), then a rain excuse, then a concession in the final clause that a milestone was in fact missed, all in one answer | No — the answer contradicts itself within a single response | Moderate — the size of the drop and the deny-then-concede pattern both matter more than run 2's "plausible and seasonal" read suggested |
| Ishita Lodha (May-26 call, p.8-9): trade payables jumped 79 to 138 days and unbilled revenue 94 to 133 days | Attributed to the FY24 Atmanirbhar-scheme withdrawal shifting billing to milestone-linked cycles, plus an April-26 catch-up payment of ~Rs300cr to creditors | Partially — plausible mechanism, but this is exactly the working-capital build Gate 0/B02 flag as the core cash-conversion problem, and it was raised only when asked | Yes, real and unresolved — this is the same 71%-of-revenue contract-asset build B02 names as the top audit matter |
| Yash Parkar (Aug-26 call, p.12): ROE fell to 14% in FY26 while ROCE stayed ~19-20% — genuine capital-efficiency decline or just equity-base dilution | Attributed entirely to the larger post-IPO/QIP equity base | Reasonably, on its face | Low-medium — plausible mechanically, not independently verified in this corpus; the analyst's "post-QIP" premise is itself left uncorrected — see red flags |
| Vaibhav Shah (May-26 call, p.6-7): Romania bid worth ~Rs13,000cr for one 17km project, ~65-70% of the current order book — is this too concentrated a risk | "very conservative bid," compared per-km cost inflation in the EU versus India | Reasonably | Low — the bid appears never to have progressed further per the Aug-26 call's silence on it |
| Vaibhav Shah (Aug-26 call, p.10-11): analyst's own math (~Rs430-440cr) does not match management's Rs550cr FY27 HAM equity figure | Management supplies a nine-project list that itself sums to Rs567cr, not Rs550cr (see 2F.7) | No — the clarification introduces a third, unreconciled number rather than resolving the discrepancy | Yes — a genuine, quantifiable disclosure-consistency problem on the exact figure the analyst was trying to pin down |
| No analyst asked about the fraud, IFC qualification, NHAI termination, auditor resignation, leadership churn, or contingent-liability growth in any of the four calls | N/A | N/A | The absence of these questions from the analyst community across four consecutive quarters is itself a finding, not a comfort |

### 3D. Customer and order book signals

- Single largest project to date: Sahebganj-Areraj-Bettiah (NH 139W, Bihar), Rs2,160cr, L1 in Feb-26 call, LOA confirmed and reaffirmed as "the biggest project Ceigall has received till date" by May-26 call. (Note: the same May-26 call also restates its value once as "one INR21,160 crores project," a 10x typo left uncorrected — see 2F.8.)
- Jaipur Rail Corporation (Jaipur Metro), Rs918cr, L1 status announced Feb-26 call — never mentioned again in May-26 or Aug-26 calls (dropped, LOA status unresolved; see 2F.2).
- Ambala-Chandigarh-Zirakpur HAM and one Rs600cr Zirakpur bypass project: L1/progress noted May-26 call; concession agreement signed by Aug-26 call (delivered on schedule).
- Arunachal highway project, L1 as part of a joint venture — new in Aug-26 call, no prior mention.
- Velgaon 400kV substation (T&D): consistent progress reporting across all four transcripts, the most consistently and specifically tracked non-EPC-road vertical.
- Customer concentration: HAM projects are "all from NHAI" except one from MPRDC (May-26 call, p.8); renewable customers named for the first time in the annual report (Rewa Ultra Mega Solar, MP Urja Vikas Nigam, MSEDCL per B03) but not named on any of the four calls themselves.
- International order book: zero revenue-generating orders across all four calls; only tenders "under evaluation" (Romania, Dubai/Sobha), both silent by the Aug-26 call.
- Northern Ayodhya bypass: revenue collapsed to ~Rs42cr in Q1 FY27, the sharpest single-project drop named on any call this run tracked, and the only explanation offered was internally contradictory (deny, then excuse, then concede) — see 2B, 3C, red flags.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (ranked by earnings impact)

| Priority | Trigger | Type | Timeframe | Conviction | Confirms | Kills |
|---|---|---|---|---|---|---|
| 1 | HAM monetization / capital-recycling cycle | INORGANIC | Near-medium | Medium | Disclosed sale price and a second/third completed HAM divestment with disclosed consideration and IRR | Further divestments stall, or a disclosed consideration shows value destruction vs equity invested |
| 2 | Order book scale and diversification (Rs18,568cr, 4.8x book-to-bill) | VOLUME | Near-medium | High, but see the roll-forward gap in 2F.1 (now confirmed on both a consolidated and a standalone basis) | Continued execution translating book into billed revenue at guided margins, and a closed roll-forward gap | Contract assets/unbilled revenue keep rising faster than billed revenue (tests the existing 71%-of-revenue KAM); the order-book roll-forward gap widens further |
| 3 | EBITDA margin resilience (11-12.5% band) | COST/PRICE-MIX | Near | Medium, DOWNGRADED this run from Medium-High given the repeated, twice-deflected question on whether the margin beat is a one-off (2E) | FY27 actual margin holds within or above the guided band, on a like-for-like basis excluding bonus/royalty, AND management gives a direct yes/no answer to the one-off question when next asked | Margin compresses below 11% for two consecutive quarters, or the "not a one-off" claim is contradicted by a subsequent quarter's margin drop right after the newly started projects referenced in both non-answers mature |
| 4 | Renewables/T&D vertical ramp (35% of FY26 order inflow; 20-25% of FY27 revenue guided) | SECTORAL/VOLUME | Medium | Low, DOWNGRADED this run — the ~Rs443cr renewable inflow-vs-book gap (2F.5), the four-quarter margin-bifurcation evasion (2E), AND zero disclosed renewable revenue one quarter into the guided FY27 window (Aug-26 call) | First disclosed renewable-segment revenue/EBITDA line showing margins in line with core EPC, and a closed reconciliation between renewable inflow and renewable order book | Renewable segment margins disclosed materially below the 11-12.5% EPC band, the inflow-vs-book gap persists unexplained, or FY27 ends with renewable revenue well short of the guided 20-25% share |
| 5 | NHAI/MoRTH policy tailwind and billing-notification cash-flow relief | REGULATORY-POLICY | Near | Medium, DOWNGRADED this run — Ceigall's claim of FULL escalation-cost compensation is contradicted by peer evidence in the identical quarter (2B, 2F.9-adjacent finding, B06-peers.yaml) | Payable-days and unbilled-revenue-days actually improve in FY27 as promised, AND Ceigall's margin holds up better than peers facing the same input-cost pressure, with the mechanism named | No improvement in FY27 despite the cited monthly-billing notification, or Ceigall's margin comes under the same escalation pressure peers describe |
| 6 | International expansion | INORGANIC/SECTORAL | Long, aspirational | Low | Any signed international order with disclosed EBITDA/IRR terms | Continued zero execution for another 2+ years, or the "war situation" excuse recurs without ever being named |

### 4B. Questions for peer verification (handoff to Stage 6)

1. {question: "What is your consolidated operating cash flow trend over FY25-FY26, and does management's tone on calls acknowledge or omit a negative CFO figure?", why: "Tests whether Ceigall's 'cash flow is not a problem' narrative despite negative consolidated CFO is a sector-wide messaging pattern or company-specific.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
2. {question: "What NHAI award pace (km and Rs value) do peer managements cite for FY26 when asked directly, versus Ceigall's refusal to quantify and deflection to the NHAI website?", why: "Benchmarks whether Ceigall's evasion on this specific, repeatable question is unusual or standard industry reticence.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
3. {question: "What HAM-asset or InvIT monetization considerations (sale price, equity IRR realised) have peers disclosed for completed transactions?", why: "Benchmarks whether Ceigall's total non-disclosure of the Malout-Abohar-Sadhuwali sale price is industry-standard opacity or a specific red flag.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
4. {question: "Do peer HAM equity-commitment figures reconcile cleanly quarter to quarter on a consistent scope, or do they also shift base and definition the way Ceigall's do?", why: "Tests whether Ceigall's unreconciled, shifting equity-commitment totals reflect a company-specific disclosure-quality problem.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
5. {question: "Do peer managements proactively address fraud, IFC qualifications, subsidiary auditor resignations, or leadership churn on calls, or only when compelled by a regulatory filing?", why: "Benchmarks Ceigall's total silence on governance events across four consecutive calls against sector disclosure culture.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
6. {question: "What working-capital-day trends (receivables, unbilled revenue, payables) have peers reported since the FY24 Atmanirbhar-scheme withdrawal, and do they show a comparable deterioration to Ceigall's payable-days jump from 79 to 138 and unbilled-revenue-days jump from 94 to 133?", why: "Tests whether Ceigall's working-capital stretch is regulatory/sector-wide or company-specific.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
7. {question: "What margin-guidance bands do peers give, and how do they treat one-off bonus/royalty income relative to headline EBITDA margin across periods?", why: "Tests whether Ceigall's practice of folding bonus/royalty income into some periods' headline EBITDA, then guiding a lower like-for-like band, is standard sector practice or a specific optics issue.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
8. {question: "Do peer companies disclose separate segment-level EBITDA margins for renewables/T&D versus core road EPC, and where those margins land relative to the core band?", why: "Tests whether Ceigall's refusal to bifurcate segment margins across four consecutive quarters, alongside an unchallenged '15% plus' framing for new verticals, is unusual disclosure opacity or sector norm.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}
9. {question: "Do peer EPC companies confirm the same monthly (vs quarterly) escalation-cost compensation notification cited by Ceigall as a margin/cash-flow tailwind, and do they report it fully offsetting input-cost inflation?", why: "Tests whether Ceigall's claim of full escalation pass-through, tied to an unnamed 'war situation,' is verifiable sector-wide policy or a company-specific and possibly overstated claim. NOTE: Stage 6 has since answered this — CONTRADICTED. All three peers describe the mechanism as partial and time-boxed, and HGINFRA's own margin fell to 9.37% in the identical quarter on unrecovered escalation (B06-peers.yaml). This is now carried as a confirmed red flag rather than an open question, see Section 2B and 4D.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}

### 4C. Management quality verdict table

| Dimension | Verdict |
|---|---|
| Guidance delivery (revenue, margin, order inflow, standalone debt ratio) | Strong — every headline guidance figure fully testable here was met or beaten across the four calls; but two guidance items that entered the record this run (FY27 renewables at 20-25% of revenue; FY27 minimum-15% standalone growth) are both showing early strain one quarter in |
| Numeric specificity when asked | High — granular, project-level answers on nearly every operational question, though the granularity itself sometimes fails to reconcile (2F.7, 2F.8) |
| Reconciliation and internal consistency | Weak — HAM/renewable equity totals, FY27 order-inflow guidance (three different figures), a per-project equity list, a HAM project count, a bid-pipeline total, and an intra-call project figure (Ramban-Banihal) all fail to reconcile within or across calls |
| Disclosure completeness over time | Deteriorating — consolidated debt and consolidated P&L disclosure both progressively thinned across the four calls and disappeared entirely in the most recent one (Aug-26); the SAME call discloses, as an aside, that IPO proceeds are 100% spent and royalty income has ceased, one quarter before an Rs859cr FY27 equity ask |
| Disclosure of adverse/governance events | Very weak — total silence, across all four calls, on the fraud, the qualified IFC opinion, the NHAI SPV termination, the auditor resignation, the leadership churn, and the contingent-liability growth that the audited FY26 accounts carry as top findings |
| Handling of a live cash-figure error | Weak — corrected only via a written erratum in the filed transcript (a ~71% overstatement, confirmed this run), no live acknowledgment |
| Candour under direct, repeated pressure | Weak, WORSE than run 2 found — beyond the one deflect-then-concede sequence on margin optics, a second and more consequential question (is the margin beat a one-off) was asked twice by name and deflected identically both times with an unrelated project list; a claim of full escalation-cost compensation is contradicted by peer evidence in the identical quarter; and a Q1 revenue collapse (Northern Ayodhya) was met with a denial that contradicted itself within the same answer |
| Self-consistency within a single call | Weak, NEW finding this run — a bid-pipeline total that does not sum to its own stated components, an intra-call set of Ramban-Banihal figures that do not cohere, and a "we were always guiding 10-15%, our growth is much more" claim (Feb-26) directly contradicted by the same call's own 9M growth figures (7.6% standalone, 8.7% consolidated) |

**Overall grade: C, at the low end of the band, one step from D.** Basis: operational and financial guidance (revenue growth, order inflow, margin, standalone deleveraging ratio) was genuinely delivered or beaten across all four calls, which argues against a D. But this run's additional findings do not lift the grade; they tighten it toward the bottom of C. Two are load-bearing and NEW: (1) a repeated, valuation-relevant evasion — whether the FY26/Q1 FY27 margin beat is sustainable, asked twice by the same analyst, answered both times with an unrelated project list, never a yes or a no; and (2) a clean, quantifiable FALSE statement, not merely an evasion — the Feb-26 claim "we were always guiding 10% to 15%, our growth is much more than that," directly contradicted by the SAME call's own 9M FY26 growth prints of 7.6% standalone and 8.7% consolidated, both below the low end of the range management claims to be beating. These sit alongside everything run 2 already established: total four-call silence on the fraud, the qualified IFC opinion, the NHAI SPV termination, the leadership churn, and the contingent-liability growth; a widening set of unreconciled figures; a disclosure-completeness trend that got WORSE across the four calls, reaching zero consolidated-debt and zero consolidated-EBITDA/PAT disclosure in the most recent call, in the SAME call that discloses 100% IPO-proceeds utilisation and royalty cessation as an aside, one quarter before an Rs859cr FY27 equity commitment; and a cash/FDR erratum now correctly measured at ~71% overstatement (not run 2's 41.5%) of the exact liquidity figure used to argue funding is not a constraint.

What would move this to D: another quarter of continued zero disclosure on consolidated debt/EBITDA/PAT; a second outright false statement (not merely an evasion) against the company's own previously disclosed numbers; or the margin-sustainability question resolving into a confirmed one-off that was not flagged in advance.

What would move this to B: full consolidated debt and P&L disclosure restored for two consecutive quarters; a direct, specific answer (not a project list) the next time the margin-one-off question is asked; and reconciliation of the shifting equity-commitment and order-inflow-guidance figures onto one consistent basis across at least two consecutive calls.

### 4D. Concall red flags

| Severity | Flag |
|---|---|
| HIGH | Total silence across four consecutive calls on the Rs89.65m procurement fraud and the qualified IFC opinion at both standalone and consolidated levels; no analyst asked either |
| HIGH | Total silence across four consecutive calls on the NHAI termination of a step-down SPV project and the associated sister-SPV auditor resignation |
| HIGH | Management repeatedly asserts strong/"amazing" cash flow and states "equity is not a problem" (May-26, p.6) and "cash flow will not be a challenge" (May-26, p.8) while consolidated CFO was negative in FY25 (Rs -515.6cr) and FY26 (Rs -91.3cr per B03); never reconciled by management or raised by any analyst |
| HIGH | Consolidated debt disclosure and consolidated EBITDA/PAT disclosure both progressively degraded across four calls to zero disclosure of any kind in the most recent call (Aug-26), removing the two metrics most relevant to testing the company's own "cash is not a problem" claim in the same period (2F.4, 2F.6) |
| HIGH | Written erratum in the filed May-26 transcript corrects unencumbered cash/FDR from a stated combined Rs412cr to an actual combined Rs241cr — a ~71% overstatement (Rs171cr / Rs241cr = 70.95%, arithmetic shown at 2F.9; CORRECTED this run from run 2's 41.5%, which computed a different quantity) of exactly the liquidity metric used, in the same sentence, to argue "equity is not a problem" |
| HIGH (NEW this run) | A valuation-relevant question — whether the FY26/Q1 FY27 margin beat is a one-off — was asked by the same analyst (Mahesh Patil, ICICI Securities) in two consecutive quarterly calls (May-26 call, p.10; Aug-26 call, p.7-8) and answered both times with an unrelated list of newly started projects, never a yes or a no. This bears directly on whether the current margin can be treated as a sustainable valuation base |
| MEDIUM-HIGH (NEW this run) | Management discloses, as an aside inside an other-income answer, that "we have 100% utilized the IPO proceeds in the last quarter of the FY26" and that royalty income has ceased (Aug-26 call, p.11) — one quarter before committing to an Rs859cr FY27 equity plan (Aug-26 call, p.6-7), at the same call where consolidated debt and cash-flow disclosure have gone dark, materially narrowing the visible funding cushion behind the "equity is not a problem" narrative |
| MEDIUM-HIGH | No acknowledgment on any call of the WTD/CEO change between the Feb-26 call (Sudhir Hoshing, WTD) and the May-26 call (A. Sarvanan, CEO), consistent with B02/B03's five KMP/Board changes in ~14 months |
| MEDIUM-HIGH (NEW this run) | Ceigall's claim of FULL escalation-cost compensation ("whatever increase in the cost... will be paid by the authority ultimately to the EPC contractor," May-26 call, p.10) is contradicted by peer evidence in the identical Q4 FY26 quarter: HGINFRA's standalone margin fell to 9.37% with management attributing the drop to unrecovered cost escalation (HGINFRA-Concall_May_2026_Transcript.txt, p.6), and Stage 6 finds all three peers describe the same MoRTH mechanism as partial and time-boxed (B06-peers.yaml) |
| MEDIUM-HIGH (NEW this run) | Feb-26 call claim "we were always guiding 10% to 15%, our growth is much more than that" (p.14) is a clean, quantifiable FALSE statement against the SAME call's own 9M FY26 growth figures: standalone 7.6% (p.5) and consolidated 8.7% (p.6), both below the low end of the claimed range |
| MEDIUM (NEW this run) | Cash/liquidity disclosed on three different, non-comparable bases across three consecutive quarters: Rs225cr "including FD" (Dec-25, Feb-26 call, p.11), Rs241cr "unencumbered cash+FDR" post-correction (Mar-26, May-26 call, p.6), Rs320cr "of FDs" (Jun-26, Aug-26 call, p.11); no quarter's figure is defined against the prior quarter's basis, and no analyst has asked for a consistent number |
| MEDIUM (NEW this run) | Northern Ayodhya bypass revenue collapsed to ~Rs42cr in Q1 FY27; management's answer denies any issue ("there's nothing"), cites rain, and concedes a missed milestone in the same breath (Aug-26 call, p.5-6) — reweighed up this run from run 2's "plausible and seasonal, not disputed" given the size of the project and the deny-then-concede pattern |
| MEDIUM | Order-book roll-forward (opening + inflow - revenue executed) does not close in any of the three testable quarters on a consolidated basis (persistent positive gap averaging ~Rs433cr/quarter, ~2-3.4% of book size), and the same-direction gap survives independently on a standalone-revenue basis (+Rs264cr / +Rs539cr / +Rs315cr) — CONFIRMED on two revenue bases this run, never explained by management (2F.1) |
| MEDIUM | Renewable FY26 order inflow claimed (~Rs3,968cr, 35.02% of total) does not reconcile with the closing renewable order book (Rs3,525cr, 19% of total), a ~Rs443cr shortfall, against a segment B03 shows had near-zero execution all year; and FY27 renewables-revenue guidance (20-25% of total) shows zero disclosed delivery one quarter in (2F.5, Aug-26 call) |
| MEDIUM | Aug-26 per-project HAM equity list sums to Rs567cr against a stated total of Rs550cr, and the same call states both "10 HAM projects" (order-book table) and "all 11 of our HAM projects" (Q&A) — two unreconciled internal disagreements in one call (2F.7) |
| MEDIUM | Malout-Abohar-Sadhuwali HAM sale consideration never disclosed in any of four calls despite being cited repeatedly as proof of the capital-recycling thesis; an analyst-quoted figure of ~Rs177cr (Feb-26 call, p.12) neither confirmed nor denied |
| MEDIUM | The same call's prepared remarks describe the Malout-Abohar-Sadhuwali/Bathinda-Dabwali/Jalbehra-Shahbad divestments as "binding document" (one asset) or "non-binding offer...under due diligence" (two assets) (May-26, p.4, corrected from p.3), while the Q&A of the SAME call states "we have already sold three assets to Neo" (p.7, corrected from p.6) — a completed-sale framing for assets the prepared remarks, moments earlier, describe as not yet closed. The equivalent pattern also appears in the Feb-26 call: "in-principle approved a binding offer" (p.5, corrected from p.4) versus "we have already sold one HAM asset" (p.10, corrected from p.9) in Q&A |
| MEDIUM | Segment margin bifurcation for renewables and T&D asked in some form in all four calls and answered with an actual number in none — a four-quarter repeated evasion (2E) |
| MEDIUM | Q1 FY27 standalone revenue grew only 10.2% YoY (Aug-26 call, p.5) against the "minimum 15%" FY27 guidance reaffirmed in the SAME call (Aug-26 call, p.8-9); only the 15.7% consolidated growth figure was volunteered, and no analyst connected the two |
| MEDIUM | Promoter's personal Rs20cr equity in the Bathinda-Dabwali HAM SPV (Feb-26, p.6), an asset simultaneously targeted for third-party divestment (Feb-26, p.12-13); never explained on any call, never asked |
| MEDIUM | Southern Ludhiana bypass land status regressed rather than merely slipped: "very clear...80% by December" (Nov-25) versus "only 62% available" (Aug-26), a genuine reversal not surfaced or explained on any intervening call |
| MEDIUM | FY27 balance HAM/solar equity commitment of Rs859cr against only Rs23cr actually infused in Q1 FY27 (2.7% of the annual target in the first quarter), now sharpened by the same-call disclosure that IPO proceeds are fully spent and royalty income has stopped — too early to call a miss, but a pacing and funding-capacity concern worth watching each subsequent quarter |
| MEDIUM (NEW this run) | An unexplained "we have 1.5 years to dilute another 8% also" (Nov-25 call, p.13), made once, never repeated or explained on any later call; an Aug-26 analyst's question premised on a "post-QIP" capital raise (p.12) was also left uncorrected by management, so it is unclear whether an unannounced dilution event has occurred |
| LOW-MEDIUM | Contingent liabilities at 83.7% of standalone net worth, and the standalone/consolidated bank-guarantee inconsistency, never mentioned on any call nor asked by any analyst |
| LOW | Ramban-Banihal (J&K) tunnel: three specific, time-bound promises (tunnel in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027) made in the Nov-25 call, never mentioned again in any of the three subsequent calls, and never asked about; the figures given in that same exchange also do not cohere with each other (2F.8, NEW this run) |
| LOW (NEW this run) | Nov-25 bid pipeline stated at a total of Rs14,320cr, while its own segment components sum to Rs14,382cr and Rs14,000cr is used elsewhere in the same call, with an analyst's Rs16,000cr left uncorrected (2F.8) |
| LOW (NEW this run) | "One INR21,160 crores project" (May-26 call, p.12) is a 10x typo for the Rs2,160cr Sahebganj-Areraj-Bettiah award, left uncorrected in the same filed transcript that carries the written cash erratum |
| LOW (NEW this run) | An analyst's Rs3,500cr solar-and-BESS order-book figure (Feb-26 call, p.7) is left uncorrected against the Rs3,168cr renewable figure management itself stated earlier in the same call (Feb-26 call, p.4) |
| LOW (NEW this run) | "Seven of our projects have completed ahead of schedule" (Feb-26 call, p.5) sits against Jalbehra, named later in the same call as delayed and awaiting an EOT with bonus eligibility unresolved (Feb-26 call, p.12); never revisited on any later call |
| LOW | FY27 order-inflow guidance restated three times inside six months (~Rs5,800cr Feb-26 -> "minimum Rs5,500cr" May-26 -> "Rs6,000cr" Aug-26) with no acknowledgment of any of the changes |
| LOW | Working-capital-day target asked twice (Nov-25, Aug-26) and answered with only qualitative language ("definitely there will be an improvement") both times, never a number |
| LOW | International order-inflow target ("at least 10-15%" of FY27 inflow, set Feb-26) dropped without mention in either the May-26 or Aug-26 call |
| LOW | The reason given for international caution shifts from routine conservatism (Nov-25 through May-26) to an unnamed "war situation" (May-26 and again Aug-26, p.12) that is never identified or explained, and no analyst asks what it refers to |

---

## Analyst note

This run closed the gaps a second independent audit named on run 2: one arithmetic
error (the cash/FDR overstatement is ~71%, not 41.5%; run 2's number answered a
different question), one missed critical repeated evasion (Mahesh Patil's twice-asked,
twice-deflected margin-sustainability question, now a valuation input in 2E and a HIGH
red flag), a set of missed guidance and disclosure items (renewables-revenue guidance
under early strain, standalone growth trailing its own guide, IPO-proceeds exhaustion
plus royalty cessation buried in an aside, a three-basis cash disclosure, an unexplained
dilution comment, and a demonstrably false "10-15%, growing much more" claim), two
re-weighed items (Northern Ayodhya's deny-then-concede answer; the escalation-cost
claim now contradicted by peer evidence via Stage 6), and a set of minor intra-call
arithmetic items (a bid pipeline that does not sum to its own parts, a 10x typo, an
incoherent Ramban-Banihal exchange, an uncorrected analyst figure, an unrevisited
schedule claim). None of these, individually, would move the grade off C; run 2's
finding that the case for delivered guidance is real still holds. But two of them
together — a repeated evasion on the exact question that determines whether the
margin is a sustainable valuation base, and an outright false statement inside a
single call — are different in KIND from run 2's reconciliation-gap findings, which
were at most ambiguous or unexplained rather than actively contradicted or false. That
is why this run holds the grade at C but states explicitly that it sits at the bottom
of the band, one step from D, rather than presenting a flat C that reads the same as
run 2's. The citation-rule fix (marker page, not printed header) touched roughly 30
carried-forward citations in addition to the ones named in the six fixes; in every
case the underlying claim was already correct, only the page number moves, so no
finding from run 2 is withdrawn or weakened by this pass.
