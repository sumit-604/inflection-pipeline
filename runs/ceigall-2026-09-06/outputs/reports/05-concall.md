# Stage 5: Concall Analysis — Ceigall India Ltd (CEIGALL) — RUN 2

Run date: 2026-09-06 | Model: claude-sonnet-5

RUN 2 NOTE: this run replaces the earlier B05. An independent verifier found
the first run's red-flag coverage at 48%, below the pipeline's 60% floor,
with two causes: (1) the first run treated only three transcripts as
primary and opened the Nov-2025 call only to trace two promises, missing
seven findings that live in that call; (2) no explicit cross-call numeric
reconciliation pass was run, so ten arithmetic misses that only surface
when figures from different calls sit in one table were never caught.
Both are fixed here: all four transcripts are primary, oldest first, and a
dedicated cross-call reconciliation section (2F) is added. Nothing the
first run reported was wrong; this run keeps every finding it established
(guidance delivery, the silence pattern, the repeated-question tracker) and
adds to it. Every number below was independently re-verified against the
transcripts, not copied from the run brief or the first report.

Transcripts read, all PRIMARY, oldest first:
1. Concall_Nov_2025_Transcript.pdf — Q2 and H1 FY26, call 17-11-2025
2. Concall_Feb_2026_Transcript.pdf — Q3 and 9M FY26, call 13-02-2026
3. Concall_May_2026_Transcript.pdf — Q4 and FY26, call 12-05-2026
4. Concall_Aug_2026_Transcript.pdf — Q1 FY27, call 14-08-2026

CITATION CONVENTION: each transcript extract carries its own embedded page
marker (e.g. "[PAGE 5]"), stated by the extract header as the PDF page
number. All page citations below (filename, p.N) use that PDF page number,
independently re-derived by re-reading each transcript in full; where a
number quoted in the run brief's own page citation did not match what this
run found at that page, this run's own re-derived anchor is used and the
mismatch is noted once, rather than silently copied.

No results filing, rating, shareholding, or substantive-announcements
corpus exists for this run. Promise-versus-delivery and reconciliation
testing below runs transcript-against-transcript and against the FY26
annual report figures already anchored in B01/B02/B03; where a check would
normally use a results PDS or shareholding filing, that limit is stated at
the specific row.

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Every growth trigger, catalyst or driver mentioned

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| Order book scale-up (Rs12,598cr Sep-25 -> Rs13,295cr Dec-25 -> Rs18,554cr Mar-26 -> Rs18,568cr Jun-26) | VOLUME | Near-medium | Committed (delivered numbers each call) | High |
| HAM monetization / "execute-monetize-recycle" capital-recycling cycle | INORGANIC | Near-medium | Planned -> one deal (Malout-Abohar-Sadhuwali) confirmed closed by Aug-26 | Medium (price never given in any of four calls) |
| Renewables + T&D diversification (solar, BESS, substations) | SECTORAL/VOLUME | Medium | Planned/aspirational (margins asserted, not shown in a segment P&L) | Medium |
| NHAI/MoRTH policy tailwind: Rs3.1 lakh cr FY27 budget (+8%), tighter eligibility norms | REGULATORY-POLICY | Near | Committed (government data cited) | Medium |
| Monthly billing / monthly escalation-compensation notification, tied by management to an unnamed "war" | REGULATORY-POLICY | Near | Committed | Low (notification never named or dated precisely) |
| International expansion (Singapore, Dubai entities; Romania and UAE bids) | INORGANIC/SECTORAL | Long, aspirational | Aspirational ("baby steps," "very conservative") | Low |
| EBITDA margin resilience (11%-12.5% band, "plain vanilla EPC") | COST/PRICE-MIX | Near | Committed guidance | High |
| Debt reduction / balance-sheet optimisation | COST | Near | Committed, but disclosure quality collapsed across the four calls (see 2F.6) | Declining |
| AI/data tools in bidding and project monitoring | COST | Long | Aspirational | Low |
| Commercial paper issuance (Rs100cr), new in Aug-26 | COST | Near | Committed | Medium |

### 1B. Quantified guidance, by quarter stated

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Revenue growth | 10%-15% YoY | FY26 | Nov-25 call, p.7; reaffirmed Feb-26 call, p.7 ("we are on track") |
| Revenue growth | Minimum 15% YoY | FY27 | May-26 call, p.4; reaffirmed Aug-26 call, p.8-9 |
| EBITDA margin | 11%-12.5% ("plain vanilla EPC") | FY26/FY27 | Nov-25 call p.9 (11-11.5%); May-26 call p.4/p.7; reaffirmed Aug-26 call, p.7 |
| Order inflow | Rs5,000cr | FY26 | Nov-25 call, p.9-10; reiterated Feb-26 call, p.10-11 |
| Order inflow (actual) | Rs11,332cr (2.27x the guided figure) | FY26 | May-26 call, p.3-4 |
| Order inflow guidance | "Around INR5,800 crores" ("incremental of 15%" over the original Rs5,000cr FY26 guide, not over the Rs11,332cr actually delivered) | FY27 | Feb-26 call, p.10-11 |
| Order inflow guidance (restated) | "Minimum INR5,500 crores" | FY27 | May-26 call, p.4 |
| Order inflow guidance (restated again) | "INR6,000 crores" | FY27 | Aug-26 call, p.7-8 — third distinct FY27 order-inflow figure inside 6 months, no acknowledgment of any change |
| Order inflow (Q1 FY27 actual) | "Close to INR600cr" against the Rs6,000cr FY27 target | Q1 FY27 | Aug-26 call, p.7-8 |
| Standalone debt | Rs614.8cr (Sep-25) -> Rs552cr (Dec-25) -> D/E only, no Rs figure (Mar-26) -> not disclosed at all (Q1 FY27) | Nov-25 to Aug-26 | See 2F.6 for the full degrading trail |
| Consolidated debt | Rs1,341.2cr (Sep-25) -> Rs1,421cr (Dec-25) -> D/E only, no Rs figure (Mar-26) -> not disclosed at all (Q1 FY27) | Nov-25 to Aug-26 | See 2F.6 |
| Capex | Rs25-30cr FY26; Rs30-35cr FY27 | FY26/FY27 | Feb-26 call, p.11; Aug-26 call, p.8 |
| Cash incl. FD | Rs225cr | Dec-25 | Feb-26 call, p.11 |
| Unencumbered cash / FDR (Mar-26) | Stated Rs266cr / Rs146cr; corrected in the filed transcript to Rs166cr / Rs75cr | Mar-26 | May-26 call, p.6 (written erratum in the filed document) |
| HAM equity infusion pace target | Rs297cr in "coming 3 months" (whole HAM book) | Nov-25 -> ~Feb-26 | Nov-25 call, p.10 |
| HAM equity infusion, same call, different subset | Rs200cr in "next 3 months," named as VRK 11/12 + Ludhiana-Bathinda + Northern/Southern Ayodhya only | Nov-25 -> ~Feb-26 | Nov-25 call, p.12 — no bridge offered between this and the Rs297cr figure on p.10 of the same call |
| HAM equity infused (cumulative) | Rs603.2cr (Oct-25) -> Rs605.6cr (Dec-25), a ~Rs2.4cr addition against the ~Rs297cr targeted for that window | Q3 FY26 | Nov-25 call p.5; Feb-26 call, p.4 |
| HAM equity total commitment | Rs1,391cr (existing HAM) + Rs395cr (two new HAM) + ~Rs810cr (solar/T&D) = ~Rs2,596cr | Q3 FY26 | Feb-26 call, p.9-10 |
| Pending equity commitment (revised) | Rs1,937cr over next 3 years (Rs800cr renewable, ~Rs1,137cr HAM/roads) | FY26 call | May-26 call, p.6 |
| Equity infused, cumulative (post-IPO basis) | Rs253cr at IPO + Rs439cr more = Rs692cr "as on today" | Q1 FY27 | Aug-26 call, p.6 |
| Equity infused, Q1 FY27 alone | Rs23cr | Q1 FY27 | Aug-26 call, p.9 |
| Balance equity commitment | Rs859cr (Rs310cr solar + Rs550cr HAM) FY27; Rs744cr (Rs300cr solar + Rs444cr HAM) FY28 | FY27/FY28 | Aug-26 call, p.6-7 |
| Per-project HAM equity list (Aug-26) | Nine named projects sum to Rs567cr against a stated total of Rs550cr | FY27 | Aug-26 call, p.10-11 — see 2F.7, does not close |
| HAM project count | "All 11 of our HAM projects" (Q&A) vs "10 HAM projects" in the same call's own order-book table | Q1 FY27 | Aug-26 call, p.5 (10 HAM) vs p.10 (11 HAM) — see 2F.7 |
| Malout-Abohar-Sadhuwali sale price | NEVER STATED in any of the four transcripts; an analyst-quoted ~Rs177cr (Feb-26 call, p.11) neither confirmed nor denied | — | — |
| Malout-Abohar-Sadhuwali sale status | "In-principle approved a binding offer" (Feb-26) -> "binding document...validates our execute-monetize-recycle framework" (May-26) -> "successful monetization...completed" (Aug-26) | Feb-26 to Aug-26 | See 2F below and Section 2B |
| Bathinda-Dabwali / Jalbehra-Shahbad divestment close | "Before September" 2026 | Feb-26 call, p.12-13 |
| Bathinda-Dabwali / Jalbehra-Shahbad divestment close (revised) | Q2 FY27 / Q3 FY27 | May-26 call, p.8 — then zero mention in Aug-26, past the original "before September" deadline |
| Renewable share of order inflow | 35.02% of FY26 total order inflow | FY26 | May-26 call, p.3 |
| Renewable share of order book | 22% (Sep-25, of Rs12,598cr) -> ~23.8% (Dec-25, of Rs13,295cr, Rs3,168cr absolute) -> 19% (Mar-26, of Rs18,554cr, Rs3,525cr absolute) | Nov-25 to May-26 | Nov-25 p.3; Feb-26 p.4; May-26 p.3, p.6 — see 2F.5, does not close against the inflow claim |
| International order-inflow target | "At least 10 to 15%" of FY27 order inflow | FY27 | Feb-26 call, p.11 — never repeated in May-26 or Aug-26 |
| Ramban-Banihal (J&K) tunnel completion | "In the next 3 months" (i.e. ~Feb-26) | Nov-25 -> ~Feb-26 | Nov-25 call, p.12 — never mentioned again |
| Ramban-Banihal billing | ~Rs180cr (20% of the tunnel work) billed "before this March" 2026 | Nov-25 -> Mar-26 | Nov-25 call, p.12 — never mentioned again |
| Ramban-Banihal viaduct completion | "By March '27," using redesigned steel girders | Nov-25 -> Mar-27 | Nov-25 call, p.12 — never mentioned again |
| Southern Ludhiana bypass land | "Very clear...80% land cleared by December" 2025 | Nov-25 call, p.7-8 |
| Southern Ludhiana bypass land (later) | "Only 62% available with us, so that is a challenge" | Aug-26 call, p.6 — a regression against the earlier 80%-by-December promise, not merely a delay |
| NHAI awarding, FY26, km and Rs value | NEVER GIVEN a company number (twice deflected to "check the NHAI website") | — | Feb-26 call, p.8-9; May-26 call, p.9-10 |
| Q1 FY27 consolidated EBITDA / consolidated PAT | NOT DISCLOSED — only consolidated revenue (Rs970cr, +15.7%) given; both figures were disclosed in the two prior calls | Q1 FY27 | Aug-26 call, p.5, checked against the full Q&A too |

### 1C. Trigger evolution across all four quarters

- **Order book / diversification**: STRENGTHENING every quarter in absolute size (Rs12,598cr -> Rs13,295cr -> Rs18,554cr -> Rs18,568cr). Renewable share of order book fell from 22% (Sep-25) to 19% (Mar-26) even as the renewable rupee figure grew (Rs2,772cr to Rs3,525cr) — a share dip on a bigger base, not itself alarming, but see 2F.5 for a genuine arithmetic gap between the renewable order book and the renewable inflow claim.
- **HAM monetization**: STRENGTHENING in narrative terms across all four calls (one deal narrated from "in-principle" through "binding" to "sold"/"successful monetization"), but the sale price has never been disclosed in any of four calls, and the "before September" 2026 target for the next two deals (Feb-26) was pushed to Q2/Q3 FY27 by May-26, then dropped without any update in Aug-26, past the original deadline.
- **International expansion**: UNCHANGED in stated caution ("baby steps," "very conservative") across all four calls, but the underlying pipeline claim swung wildly — a Romania bid quoted at ~Rs13,000cr for one 17km project (May-26, ~65-70% of the entire order book by the analyst's own math) — then went unmentioned in Aug-26 next to a new, never-identified excuse ("this war situation," Aug-26, p.11-12). The 10-15%-of-inflow international target set in Feb-26 was never repeated.
- **NHAI awarding pace**: management declined to quantify twice (Feb-26, May-26), each time citing the NHAI website — UNCHANGED (evasive both times); a third attempt at the question in Aug-26 was lost to a dropped call, not a clean data point either way.
- **Margins**: management's stated position STRENGTHENED in specificity only after repeated analyst pressure — the May-26 call finally clarified that FY24/FY25 headline EBITDA included one-off bonus/royalty income the FY26/FY27 guided band strips out, but only on the third round of the same analyst's questioning; segment-level (renewable/T&D) margin bifurcation was asked in all four calls and answered with a number in none (see 2E).
- **NEW in Aug-26, no forward reference in the three earlier calls**: commercial paper issuance (Rs100cr) against working-capital limits; the ROE (14%)-versus-ROCE(~19-20%) divergence question.
- **DROPPED, no update or follow-up in any later call**:
  - Jaipur Rail Corporation project (Rs918cr, L1 status announced Feb-26, p.4) — never mentioned again; LOA status unresolved (contrast with Sahebganj-Areraj-Bettiah, also L1 in Feb-26, which DID convert to a confirmed LOA by the May-26 call).
  - Ramban-Banihal (J&K) tunnel: three specific, time-bound promises made in Nov-25 (tunnel in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027) — none mentioned again in Feb-26, May-26 or Aug-26, despite management having called the project "a great learning" and "an amazing job." No analyst asked either.
  - Working-capital-day target asked in Nov-25 (p.11) — never given a number; a similar-spirit question in Aug-26 (p.9-10) again got only a qualitative "definitely there will be an improvement," no number.
  - Consolidated debt disclosure: full loan-type breakdown (Nov-25) -> aggregate Rs figure only (Feb-26) -> D/E ratio only, no Rs figure (May-26) -> nothing at all (Aug-26). See 2F.6.
- **NEVER APPEARING in any of the four calls, despite being current-year, audited, material events**: the Rs89.65m procurement fraud, the qualified IFC opinion (both levels), the DGGI GST search action, the NHAI termination of the step-down SPV (Ceigall Ludhiana Rupnagar Greenfield Highway), the associated subsidiary auditor resignation, the contingent-liability rise to 83.7% of standalone net worth, and any leadership-change explanation (see Section 2 below).

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker (chronological, all four calls)

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| Nov-25 call | FY26 revenue growth 10%-15% | DELIVERED — FY26 standalone revenue growth 14.3%, consolidated 17.1% (May-26 call, p.4-5) | N/A (delivered) |
| Nov-25 / Feb-26 calls | FY26 order inflow guided at Rs5,000cr | DELIVERED/BEATEN — FY26 actual order inflow Rs11,332cr, "significantly surpassing" guidance (May-26 call, p.3-4) | N/A (beaten) |
| Nov-25 / Feb-26 calls | Continued standalone deleveraging | DELIVERED — standalone D/E fell to 0.2x by Mar-26 vs 0.3x (Sep-25) vs 0.4x (FY25); note the Rs-figure trail behind this ratio thinned to nothing by Aug-26 (see 2F.6) | N/A (delivered on the ratio; disclosure quality behind it declined) |
| Nov-25 call | 11-11.5% EPC margin band, no compromise on margin for growth | DELIVERED — FY26 standalone EBITDA margin 12.6% (May-26 call, p.4-5), within/above the "plain vanilla EPC" band each quarter | N/A (delivered) |
| May-26 call | Ambala-Chandigarh-Zirakpur HAM progressing toward concession | DELIVERED — concession agreement signed in Q1 FY27 (Aug-26 call, p.3) | N/A (delivered) |
| Nov-25 call | HAM equity infusion pace: Rs297cr targeted in "coming 3 months" | MISSED — cumulative HAM equity rose only from Rs603.2cr (Oct-25) to Rs605.6cr (Dec-25), ~Rs2.4cr, against the ~Rs297cr targeted for the window | No explanation offered; no analyst raised the shortfall in the Feb-26 call |
| Nov-25 call | Southern Ludhiana bypass land: "very clear...80% land cleared by December" 2025 | MISSED, a regression not merely a delay — by Aug-26 (Q1 FY27), management states the land is "only 62% available," below even the pre-December baseline framing, and names it directly as "a challenge" | No explanation for why the promised 80%-by-December milestone was not met, and no intervening call (Feb-26, May-26) flagged the slip before it surfaced in Aug-26 |
| Nov-25 call | Ramban-Banihal tunnel completion in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027 | CANNOT BE VERIFIED — never mentioned again in any of the three subsequent calls; no delivery evidence, no miss acknowledgment, simply dropped | No explanation; no analyst re-asked |
| Feb-26 call | Malout-Abohar-Sadhuwali sale proceeds "before 31st March" 2026 | PARTIAL — SPA signed 3-Jun-2026, completed 16-Jun-2026 per AR (B03), ~2.5 months late; May-26 call still described it as a "binding document," not yet executed; only confirmed as done ("successful monetization") in the Aug-26 call | Timing slip never acknowledged as a slip; described in May-26 as "expecting it should get executed in this month" with no reference back to the original March target |
| Nov-25 / Feb-26 calls | VRK 11, VRK 12, Indore-Ujjain appointed dates, targeted Dec-25 through Mar-26 | MISSED/PARTIAL — appointed dates for VRK 11, VRK 12 and Indore-Ujjain arrived "subsequent to the quarter end" of Q1 FY27, i.e. Jul/Aug-26, a 4-8 month slip; no mention of these appointed dates at all in the May-26 call | No explanation for the slip beyond routine land/forest-clearance commentary in the Feb-26 call; the slip itself is never named as a slip. (Southern Ludhiana is correctly excluded from this group — its appointed date has still not arrived as of Aug-26; it is tracked separately above as its own missed promise.) |
| Feb-26 call | Bathinda-Dabwali and Jalbehra-Shahbad HAM divestments "targeting to close before September" 2026 | MISSED, silently revised then dropped — May-26 call pushed the same two deals to Q2 FY27 (Jul-Sep) and Q3 FY27 (Oct-Dec); Aug-26 call gives no update at all, past the original September deadline | Revision never flagged as a change from the earlier "before September" target |
| Every call | "Cash flow will not be a challenge," "equity is not a problem," "amazing cash flow available" (May-26, p.6-7) | Cannot be graded delivered/partial/missed against a results filing that does not exist in this corpus; tested instead against B03's audited figures: consolidated CFO was negative in both FY25 (Rs -515.6cr) and FY26 (Rs -91.3cr) | Never reconciled on any call; the assertion of comfortable cash flow is never squared with the negative consolidated CFO in the audited accounts. Not counted in the tallies below (no results filing to grade it against), but carried into red_flags and the credibility grade as the single most consequential finding |

**Counts: delivered 5, partial 2, missed 3** (11 testable rows; the cash-flow narrative and the Ramban-Banihal tunnel row are tracked but excluded from the count for the reasons stated in each row).

### 2B. Excuse pattern analysis

- Northern Ayodhya bypass execution slowdown (Aug-26 call, p.4-5): attributed to monsoon rain — EXTERNAL-BLAME, plausible and seasonal, not disputed.
- Southern Ludhiana bypass land shortfall (Aug-26 call, p.6): attributed to land availability at 62% — EXTERNAL-BLAME (department-side); the underlying number is itself a genuine regression against the Nov-25 "80% by December" framing, not merely a restated delay (see 2A).
- ROE decline to 14% vs stable ROCE ~19-20% (Aug-26 call, p.12): attributed entirely to post-IPO/QIP equity-base expansion — plausible, standard attribution, not independently verifiable in this corpus (no shareholding/ratio corpus).
- Margin "decline" in Slide 41 optics (May-26 call, p.10-11): initially answered "EBITDA margin is stable, that's not decreasing... has grown up as compared to the previous year," then, on a second and third round of the same analyst's questioning, corrected to acknowledge FY24/FY25 EBITDA included one-off bonus/royalty income — DEFLECTION on the first two passes, HONEST-ADMISSION only after repeated pressure. This first answer is directly contradicted by the same call's own reported numbers: standalone FY26 EBITDA margin was 12.6% against 12.8% in FY25 (May-26 call, p.4-5) — margin fell, not grew. See 2F below.
- PPT slide-38 equity-invested error (Feb-26 call, p.6): management directly said "It's a mistake, but otherwise entire equity has been put by the company only" — a rare, clean HONEST-ADMISSION.
- Cash/FDR figure correction (May-26 call, p.6): handled as a silent written erratum appended to the filed transcript rather than a live correction or any subsequent-call acknowledgment — closer to SILENCE than honest-admission, given the scale (see 2F for the corrected magnitude).
- Fraud, IFC qualification, NHAI termination, auditor resignation, leadership churn, contingent-liability growth: SILENCE across all four calls — never raised proactively, never asked, never addressed.
- Segment margin bifurcation (renewables/T&D vs core EPC): asked, in some form, in all four calls (Nov-25 p.13; Feb-26 p.13; May-26 p.7-8; Aug-26 p.9-10) and answered with an actual number in NONE — see 2E, a four-quarter repeated evasion.
- Pattern check: management readily and proactively raises OPERATIONAL wins (order wins, appointed dates, margin beats) but never proactively raises the governance/compliance/cash-flow items the audited accounts carry as top findings. When pressed on a genuinely uncomfortable number (margin optics), the first response deflects before a later, more honest answer emerges only under repeated questioning. No instance across four calls of management naming a compliance or governance issue unprompted.

### 2C. Tone ratings (1-5, evidence-based)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | Granular operational numbers volunteered freely, but total silence on fraud, IFC qualification, NHAI termination, leadership churn, and contingent liabilities across four calls; a material cash/FDR figure required a written post-hoc correction; consolidated debt and consolidated P&L disclosure both thinned to nothing by the fourth call |
| Specificity | 4/5 | Project-by-project equity figures, appointed-date timelines, and margin bridges given in detail whenever asked, even where the figures themselves later fail to reconcile (see 2F.7) |
| Consistency | 1/5 | HAM/renewable equity-commitment totals quoted on different, unreconciled bases in every call; FY27 order-inflow guidance restated three times (Rs5,800cr -> Rs5,500cr -> Rs6,000cr) without acknowledgment; a nine-line per-project equity list in Aug-26 does not sum to its own stated total; the same call states both "10 HAM projects" (order book table) and "all 11 of our HAM projects" (Q&A) |
| Accountability | 2/5 | One clean admission on a PPT typo; no admission of the HAM equity-infusion pace miss, the Southern Ludhiana land regression, the appointed-date slippage, the divestment-timeline slippage, or the Ramban-Banihal silence; zero acknowledgment of the governance/compliance items named in the audited accounts |
| Defensiveness | 2/5 (low-moderate) | Mostly cooperative; occasional curt dismissals ("No, we don't have any project for Punjab fencing," "I don't understand your question") rather than open hostility; not combative when pressed on margins, eventually clarifies |
| Over-promotion | 4/5 | Frequent unqualified superlatives ("amazing cash flow," "fantastic," "validates," IRR "much more than committed") without the underlying number that would let an investor check the claim; the CFO's "margin has grown up" claim (May-26) is directly contradicted by that call's own 12.6%-vs-12.8% figure |

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

### 2E. Repeated question tracker

| Question | Quarters asked | Responses | Classification |
|---|---|---|---|
| "What was NHAI's awarding pace in FY26, in kilometres and in rupees?" | Feb-26 (Ketan, Avendus Spark, p.8-9); May-26 (Dheeraj Kripalani, Avendus Spark, p.9-10) | Feb-26: "any number specific... will not be correct... we can check it on NHAI website." May-26: "these are the figures which NHAI has put on their own website" (moderator then cut the line before a number was given) | Deflected every time |
| "What is the total/pending equity requirement across HAM, solar and T&D, and how does it reconcile with the figure given last quarter?" | Nov-25 (p.10-13, Rs788cr HAM pending + ~Rs600cr T&D); Feb-26 (p.9-10, ~Rs2,596cr total); May-26 (p.6-7, Rs1,937cr pending); Aug-26 (p.6-7, Rs692cr cumulative + Rs859cr FY27 + Rs744cr FY28) | A new absolute figure is given every call, on a shifting scope (HAM-only vs HAM+solar+T&D; "pending" vs "total" vs "post-IPO"; different base dates), with no bridge ever offered between the previous quarter's number and the new one; no analyst has ever asked management to reconcile the two | Answer changed between quarters, never reconciled |
| "Do the renewable/T&D order book segments carry margins in line with, above, or below core EPC — can you bifurcate?" | Nov-25 (Priyam Shah, p.13, vague "yes...but we keep EPC margin 11-11.5%"); Feb-26 (Nimish Pandya, p.13, accepted a "15% plus" framing without correction); May-26 (Tejpal Singh, p.7-8, explicit refusal: "plain vanilla EPC would be minimum between 11% to 12.5%," no bifurcation given); Aug-26 (Chetrika Deshpande, p.9-10, "we have guided the same kind of margin... trying to achieve better," again no bifurcation) | See left column | Deflected every time — a four-quarter repeated evasion, not surfaced by the first run |
| "What is the working-capital-day target/timeline for improvement?" | Nov-25 (Balasubramanian, p.11, explanation given for the rise but no target number); Aug-26 (Chetrika Deshpande, p.9-10, "definitely there will be an improvement," again no number) | See left column | Deflected every time |

### 2F. CROSS-CALL NUMERIC RECONCILIATION (new in this run)

**2F.1 Order-book roll-forward (opening + inflow - revenue executed = closing), every testable quarter**

| Quarter | Opening book | + Inflow | - Revenue executed (consol.) | = Implied closing | Actual closing | Gap |
|---|---|---|---|---|---|---|
| Q3 FY26 | Rs12,598cr (Sep-25, Nov-25 call p.3/p.6) | Rs1,403cr (Feb-26 call, p.3-4) | Rs991cr (Feb-26 call, p.5) | Rs13,010cr | Rs13,295cr (Feb-26 call, p.3-4) | DOES NOT CLOSE, +Rs285cr |
| Q4 FY26 | Rs13,295cr (Dec-25) | Rs6,014cr (May-26 call, p.3-4) | Rs1,386cr (May-26 call, p.4-5) | Rs17,923cr | Rs18,554cr (May-26 call, p.3-4) | DOES NOT CLOSE, +Rs631cr |
| Q1 FY27 | Rs18,554cr (Mar-26) | ~Rs600cr ("close to," Aug-26 call, p.7-8, imprecise) | Rs970cr (Aug-26 call, p.5) | ~Rs18,184cr | Rs18,568cr (Aug-26 call, p.5) | DOES NOT CLOSE, ~+Rs384cr (imprecise inflow figure widens the uncertainty band) |
| FY26 full year | Not disclosed in any of the four transcripts | Rs11,332cr | Rs4,022cr | Cannot compute | Rs18,554cr | CANNOT BE TESTED — Mar-25 opening order book never stated in these four calls |

The gap is persistently POSITIVE (closing book larger than the roll-forward implies) in all three testable quarters, averaging ~Rs433cr, ~2-3.4% of book size each quarter. No management commentary in any call explains this residual. Plausible mechanisms not excluded by the transcripts: price-escalation/variation additions to existing contracts counted into the book without being reported as fresh "inflow," or a scope difference between "order book" (possibly stated at total/lifetime contract value, including O&M/annuity value for tariff-based assets) and "revenue executed" (which may only capture EPC/construction-phase recognition). This is a genuine, quantifiable, unexplained finding, not a rounding artefact — the same-direction gap every quarter argues against pure noise.

**2F.2 Order inflow claimed against guidance, tested against L1 positions without a Letter of Award**

Two projects went L1 in the Feb-26 call: Sahebganj-Areraj-Bettiah (Rs2,160cr, Bihar HAM) and Jaipur Rail Corporation (Rs918cr). Feb-26 explicitly states the LOA for Sahebganj was "not received yet" (p.8) and Jaipur Rail was "still waiting for the LOA" (p.12). By the May-26 call, Sahebganj is confirmed converted: "the LOA of Sahebganj–Areraj–Bettiah corridor...the total project cost is INR2,160 crores" (p.4), and it is referenced as the single biggest project the company has received. Jaipur Rail Corporation, however, is NEVER mentioned again in either the May-26 or Aug-26 call — its LOA status is unresolved three quarters after the L1 announcement. If Jaipur Rail's Rs918cr contributed to the Rs8,500cr 9M FY26 order-inflow figure claimed in the Feb-26 call, or to the FY26 full-year Rs11,332cr claimed in May-26, a portion of the headline "order inflow beat" would rest on a preferred-bidder position that never converted into a binding award and has since gone silent. The transcripts do not state explicitly whether L1 wins are counted before LOA, so this cannot be confirmed as a misstatement — but the asymmetry (Sahebganj converts and is celebrated; Jaipur Rail does not convert and disappears) is itself a finding worth a direct verification question to management (see peer_questions and analyst_note).

**2F.3 HAM/renewable/T&D equity committed vs equity actually infused, call by call, on a consistent scope**

CANNOT BE FULLY TESTED on a consistent scope: the basis changes every call (Nov-25: HAM-only "pending" Rs788cr, separately T&D ~Rs600cr; Feb-26: HAM total Rs1,391cr + Rs395cr new + Rs810cr solar/T&D = ~Rs2,596cr; May-26: three-year forward "pending" Rs1,937cr, Rs800cr renewable + rest HAM/roads; Aug-26: cumulative-since-IPO Rs692cr, plus FY27/FY28 forward commitments Rs859cr/Rs744cr). Directionally the trend is plausible (infused amounts step up call over call: Rs603.2cr -> Rs605.6cr -> "more than Rs400cr post-IPO" -> Rs692cr cumulative), but no single call offers a bridge from the prior quarter's number to its own, and this run could not reconstruct an exact tie-out across all four calls on one consistent scope. The two intra-Nov-25-call figures (Rs297cr vs Rs200cr "next 3 months") also do not reconcile with any bridge offered — Rs200cr is named for a named subset of projects (VRK 11/12, Ludhiana-Bathinda, Northern/Southern Ayodhya) that could plausibly sum to less than the broader Rs297cr HAM-wide figure, but management never states this explicitly, so it stands as an unreconciled internal inconsistency rather than a confirmed contradiction.

**2F.4 Consolidated vs standalone revenue, EBITDA and PAT, and any period where consolidated PAT sits below standalone PAT while consolidated EBITDA sits above it**

| Period | Standalone EBITDA | Consol. EBITDA | Standalone PAT | Consol. PAT | Anomaly? |
|---|---|---|---|---|---|
| H1 FY26 (Nov-25 call, p.6-7) | Rs185.3cr | Rs222.7cr (higher) | Rs111.8cr | Rs107.5cr (LOWER) | CONFIRMED — consol. PAT below standalone PAT despite consol. EBITDA above standalone EBITDA |
| 9M FY26 (Feb-26 call, p.5-6) | Rs305cr | Rs362cr (higher) | Rs186cr | Rs180cr (LOWER) | CONFIRMED — same anomaly persists |
| FY26 full year (May-26 call, p.4-5) | Rs487cr | Rs585cr (higher) | Rs305cr | Rs309cr (marginally HIGHER, by only Rs4cr) | Anomaly REVERSES for the full year — implied Q4-alone consol. PAT (Rs129cr) exceeds Q4 standalone PAT (Rs119cr) by enough (Rs10cr) to overcome the Rs6cr 9M shortfall, a razor-thin flip |
| Q1 FY27 (Aug-26 call, p.5) | Rs121cr | NOT DISCLOSED | Rs75cr | NOT DISCLOSED | CANNOT BE TESTED — the very quarter where this comparison would next be checkable is the quarter management stopped disclosing consolidated EBITDA and PAT entirely |

This is a genuine, precisely anchored finding, not surfaced by the first run: for two consecutive disclosed periods (H1 and 9M FY26), the group's below-EBITDA items (HAM SPV interest, depreciation, minority interest) consumed more than the entire consolidated EBITDA uplift over standalone, consistent with B03's audited-account finding of negative consolidated CFO in both FY25 and FY26. The full-year number only avoids the same pattern by a Rs4cr margin. The one quarter where this could next be tested (Q1 FY27) is exactly the quarter the disclosure disappeared.

**2F.5 Renewable order inflow for the year against the closing renewable order book, given near-zero renewable execution**

FY26 renewable order inflow claimed: 35.02% of Rs11,332cr = ~Rs3,968cr (May-26 call, p.3). Renewable order book: Rs2,772cr (22% of Rs12,598cr, Sep-25, Nov-25 call p.3) -> Rs3,168cr ("cumulative orders," Dec-25, Feb-26 call, p.4) -> Rs3,525cr (19% of Rs18,554cr, Mar-26, May-26 call, p.6). Given B03's finding that named renewable SPVs sat at pre-construction/early-construction stage all year (near-zero renewable revenue recognition), a roll-forward with near-zero execution should show the closing renewable book approximately equal to cumulative renewable inflow. Instead: Rs3,968cr of claimed FY26 renewable inflow against a Rs3,525cr closing renewable book is a shortfall of ~Rs443cr (~11% of the claimed inflow, ~13% of the closing book) — DOES NOT CLOSE. The same gap appears using the Dec-25-to-Mar-26 bridge alone (implied Q4 renewable inflow of ~Rs800cr against an actual Q4 renewable-book increase of only ~Rs357cr). Possible explanations not excluded by the transcripts: some renewable "inflow" counted at L1 stage was later reclassified or did not firm into an order-book position, or the two headline percentages (35.02% of inflow, 19% of book) use different scope definitions for what counts as "renewable" versus adjacent T&D/industrial-infrastructure buckets that shifted across calls. No management commentary in any call addresses this gap.

**2F.6 Consolidated debt across calls, and whether disclosure became less complete**

| Call | Standalone debt disclosure | Consolidated debt disclosure |
|---|---|---|
| Nov-25 (p.5) | Full breakdown: Rs614.8cr total (equipment term loan Rs13.6cr, term loans Rs270.2cr, WC loans Rs331cr); D/E 0.3x | Full breakdown: Rs1,341.2cr total (equipment term loan Rs60.4cr, term loans Rs277.7cr, HAM term loan Rs672cr, WC loans Rs331cr); D/E 0.7x |
| Feb-26 (p.5, p.12) | Aggregate only: Rs552cr, no loan-type breakdown; D/E 0.28x given only in Q&A | Aggregate only: Rs1,421cr, no loan-type breakdown; no consolidated D/E given at all |
| May-26 (p.4) | Ratio only: D/E 0.2x; NO absolute Rs figure given | Ratio only: D/E 0.6x; NO absolute Rs figure given |
| Aug-26 | NOT DISCLOSED — no debt figure or ratio of any kind, at either level, in prepared remarks or Q&A | NOT DISCLOSED |

CONFIRMED: a clean, four-call progressive degradation from a full loan-type breakdown at both levels (Nov-25) to zero disclosure of any kind (Aug-26). This is not noise — each successive call drops one more layer of granularity (breakdown, then absolute Rs figure, then even the ratio), and it lands on the same call (Aug-26) that also drops consolidated EBITDA and consolidated PAT (2F.4). Taken together, the most recent call is the least verifiable of the four on exactly the two dimensions (leverage, consolidated profitability) most relevant to testing the "cash flow is not a problem" claim repeated in the same period.

**2F.7 Per-project equity lists and project counts**

Aug-26 call (p.10-11): pressed by an analyst whose own math (~Rs430-440cr) did not match management's stated Rs550cr FY27 HAM equity figure, Kapil Aggarwal lists nine named projects: Ludhiana-Bhatinda Rs53cr, Northern Ayodhya Rs61cr, Southern Ayodhya Rs53cr, VRK 11 Rs97cr, VRK 12 Rs139cr, Southern Ludhiana bypass Rs38cr, Indore-Ujjain Rs60cr, Sahebganj (Bihar) Rs50cr, Zirakpur Rs16cr. These nine figures sum to Rs567cr, not the Rs550cr total stated in the same breath — DOES NOT CLOSE, a ~Rs17cr (~3%) gap, on top of the analyst's own independent ~Rs110-120cr shortfall estimate. Three different totals for the same claim now exist in one exchange (analyst's ~Rs430-440cr, management's stated Rs550cr, the list's actual sum of Rs567cr), and none is reconciled.

Separately, and independently: the same call's own order-book table (p.5) states "10 HAM projects." In the same call's Q&A (p.10), Ramneek Sehgal states the Rs550cr equity figure is "across all 11 of our HAM projects." A project count that disagrees with the order book, inside a single call — CONFIRMED, not reconciled.

---

## SECTION 3: COMPETITIVE INTELLIGENCE FROM CONCALLS

### 3A. Competitor commentary

Management makes almost no named-competitor commentary across the four calls. The only comparative claims are generic and self-referential: "if you compare us with the peers in the market...the number of verticals and geography-wise we have grown" (Feb-26 call, p.13-14) and "our Return on Equity would be great as compared to the peers in the market" (Aug-26 call, p.9) — both asserted without a number or a named peer. Credibility check: unverifiable as stated; peer-verification stage should test the vertical/geography spread and RoE claims directly against HGINFRA/KNRCON/PNCINFRA disclosures.

### 3B. Industry and market intelligence dropped in the calls

- MoRTH FY27 budgetary allocation raised ~8% to ~Rs3.1 lakh crore (Feb-26 call, p.3).
- NHAI overall pipeline cited at "close to Rs2 lakh crore" (May-26 call, p.9); a list of 124 NHAI/MoRTH projects worth ~Rs2 trillion cited as approved (Nov-25 call, p.5-6).
- Tightening of technical/financial bidding eligibility (higher net worth requirement, additional performance securities, greater PPP emphasis) said to favour established players — repeated in Nov-25 and May-26 calls, used consistently to support Ceigall's own positioning.
- New MoRTH notifications on monthly billing (vs milestone billing) and monthly escalation-cost compensation (vs quarterly) — cited as a direct margin/cash-flow tailwind in the May-26 call (p.7-8, p.10), attributed to "this war" happening, without ever naming which conflict or notification number, in either the May-26 or the Aug-26 call.
- Renewable order-inflow composition: 35.02% of FY26 total order inflow came from renewables (May-26 call, p.3); renewables were 19% of the FY26-end order book (May-26 call, p.6) versus 22% of the smaller H1FY26 book (Nov-25 call, p.3) — a share dip on an expanding base that management does not itself flag, and which does not fully reconcile with the absolute inflow claim (see 2F.5).

### 3C. Toughest analyst questions

| Question | Response | Satisfactory? | Real risk? |
|---|---|---|---|
| Maitri Shah (May-26 call, p.10-11): why are consolidated EBITDA margins on Slide 41 trending down despite guidance | Initial answer denied any decline ("EBITDA margin is stable...has grown up"); only on the third round did the CFO concede FY24/FY25 included bonus/royalty income skewing the comparison | Eventually yes, after unnecessary friction, and the initial answer was directly contradicted by the same call's own 12.6%-vs-12.8% figures | Real but resolved: the underlying operating margin is roughly stable; the initial deflection, stated against the call's own numbers, is the bigger tell |
| Ishita Lodha (May-26 call, p.8-9): trade payables jumped 79 to 138 days and unbilled revenue 94 to 133 days | Attributed to the FY24 Atmanirbhar-scheme withdrawal shifting billing to milestone-linked cycles, plus an April-26 catch-up payment of ~Rs300cr to creditors | Partially — plausible mechanism, but this is exactly the working-capital build Gate 0/B02 flag as the core cash-conversion problem, and it was raised only when asked | Yes, real and unresolved — this is the same 71%-of-revenue contract-asset build B02 names as the top audit matter |
| Yash Parkar (Aug-26 call, p.12): ROE fell to 14% in FY26 while ROCE stayed ~19-20% — genuine capital-efficiency decline or just equity-base dilution | Attributed entirely to the larger post-IPO/QIP equity base | Reasonably, on its face | Low-medium — plausible mechanically, not independently verified in this corpus |
| Vaibhav Shah (May-26 call, p.6-7): Romania bid worth ~Rs13,000cr for one 17km project, ~65-70% of the current order book — is this too concentrated a risk | "very conservative bid," compared per-km cost inflation in the EU versus India | Reasonably | Low — the bid appears never to have progressed further per the Aug-26 call's silence on it |
| Vaibhav Shah (Aug-26 call, p.10-11): analyst's own math (~Rs430-440cr) does not match management's Rs550cr FY27 HAM equity figure | Management supplies a nine-project list that itself sums to Rs567cr, not Rs550cr (see 2F.7) | No — the clarification introduces a third, unreconciled number rather than resolving the discrepancy | Yes — a genuine, quantifiable disclosure-consistency problem on the exact figure the analyst was trying to pin down |
| No analyst asked about the fraud, IFC qualification, NHAI termination, auditor resignation, leadership churn, or contingent-liability growth in any of the four calls | N/A | N/A | The absence of these questions from the analyst community across four consecutive quarters is itself a finding, not a comfort |

### 3D. Customer and order book signals

- Single largest project to date: Sahebganj-Areraj-Bettiah (NH 139W, Bihar), Rs2,160cr, L1 in Feb-26 call, LOA confirmed and reaffirmed as "the biggest project Ceigall has received till date" by May-26 call.
- Jaipur Rail Corporation (Jaipur Metro), Rs918cr, L1 status announced Feb-26 call — never mentioned again in May-26 or Aug-26 calls (dropped, LOA status unresolved; see 2F.2).
- Ambala-Chandigarh-Zirakpur HAM and one Rs600cr Zirakpur bypass project: L1/progress noted May-26 call; concession agreement signed by Aug-26 call (delivered on schedule).
- Arunachal highway project, L1 as part of a joint venture — new in Aug-26 call, no prior mention.
- Velgaon 400kV substation (T&D): consistent progress reporting across all four transcripts, the most consistently and specifically tracked non-EPC-road vertical.
- Customer concentration: HAM projects are "all from NHAI" except one from MPRDC (May-26 call, p.8); renewable customers named for the first time in the annual report (Rewa Ultra Mega Solar, MP Urja Vikas Nigam, MSEDCL per B03) but not named on any of the four calls themselves.
- International order book: zero revenue-generating orders across all four calls; only tenders "under evaluation" (Romania, Dubai/Sobha), both silent by the Aug-26 call.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (ranked by earnings impact)

| Priority | Trigger | Type | Timeframe | Conviction | Confirms | Kills |
|---|---|---|---|---|---|---|
| 1 | HAM monetization / capital-recycling cycle | INORGANIC | Near-medium | Medium | Disclosed sale price and a second/third completed HAM divestment with disclosed consideration and IRR | Further divestments stall, or a disclosed consideration shows value destruction vs equity invested |
| 2 | Order book scale and diversification (Rs18,568cr, 4.8x book-to-bill) | VOLUME | Near-medium | High, but see the roll-forward gap in 2F.1 | Continued execution translating book into billed revenue at guided margins, and a closed roll-forward gap | Contract assets/unbilled revenue keep rising faster than billed revenue (tests the existing 71%-of-revenue KAM); the order-book roll-forward gap widens further |
| 3 | Renewables/T&D vertical ramp (35% of FY26 order inflow) | SECTORAL/VOLUME | Medium | Low-Medium, given the ~Rs443cr renewable inflow-vs-book gap (2F.5) and four-quarter margin-bifurcation evasion (2E) | First disclosed renewable-segment revenue/EBITDA line showing margins in line with core EPC, and a closed reconciliation between renewable inflow and renewable order book | Renewable segment margins disclosed materially below the 11-12.5% EPC band, or the inflow-vs-book gap persists unexplained |
| 4 | NHAI/MoRTH policy tailwind and billing-notification cash-flow relief | REGULATORY-POLICY | Near | Medium-High | Payable-days and unbilled-revenue-days actually improve in FY27 as promised | No improvement in FY27 despite the cited monthly-billing notification |
| 5 | EBITDA margin resilience (11-12.5% band) | COST/PRICE-MIX | Near | Medium-High | FY27 actual margin holds within or above the guided band, on a like-for-like basis excluding bonus/royalty | Margin compresses below 11% for two consecutive quarters |
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
9. {question: "Do peer EPC companies confirm the same monthly (vs quarterly) escalation-cost compensation notification cited by Ceigall as a margin/cash-flow tailwind, and do they report it fully offsetting input-cost inflation?", why: "Tests whether Ceigall's claim of full escalation pass-through, tied to an unnamed 'war situation,' is verifiable sector-wide policy or a company-specific and possibly overstated claim.", check_peers: [HGINFRA, KNRCON, PNCINFRA]}

### 4C. Management quality verdict table

| Dimension | Verdict |
|---|---|
| Guidance delivery (revenue, margin, order inflow, standalone debt ratio) | Strong — every headline guidance figure tested here was met or beaten across the four calls |
| Numeric specificity when asked | High — granular, project-level answers on nearly every operational question, though the granularity itself sometimes fails to reconcile (2F.7) |
| Reconciliation and internal consistency | Weak, and worse than the first run found — HAM/renewable equity totals, FY27 order-inflow guidance (three different figures), a per-project equity list, and a HAM project count all fail to reconcile within or across calls |
| Disclosure completeness over time | Deteriorating — consolidated debt and consolidated P&L disclosure both progressively thinned across the four calls and disappeared entirely in the most recent one (Aug-26); this is a trend, not a one-off gap |
| Disclosure of adverse/governance events | Very weak — total silence, across all four calls, on the fraud, the qualified IFC opinion, the NHAI SPV termination, the auditor resignation, the leadership churn, and the contingent-liability growth that the audited FY26 accounts carry as top findings |
| Handling of a live cash-figure error | Weak — corrected only via a written erratum in the filed transcript, no live acknowledgment |
| Candour under repeated pressure | Mixed — one clean admission (PPT slide error); one deflect-then-concede sequence (margin optics, where the initial denial was directly contradicted by the call's own numbers); a segment-margin question deflected identically in all four calls; otherwise silence rather than either denial or admission on the harder topics |

**Overall grade: C** (Mixed). Basis: operational and financial guidance (revenue growth, order inflow, margin, standalone deleveraging ratio) was genuinely delivered or beaten across all four calls, which argues against a D. But credibility is capped below B by: the total, four-call silence on the fraud, the qualified IFC opinion, the NHAI SPV termination, the leadership churn, and the contingent-liability growth that the same-year audited accounts carry as top findings; a widening set of unreconciled figures (equity commitments, order-inflow guidance restated three times, a per-project equity list that does not sum to its own total, a HAM project count that disagrees with the order book); a cash-liquidity figure that required a written post-hoc correction; and a persistent, unexplained order-book roll-forward gap every testable quarter. The trajectory across the four calls is a material aggravating factor this run adds to the record: disclosure completeness (consolidated debt, consolidated EBITDA, consolidated PAT) got WORSE, not better, culminating in zero disclosure of any of these three items in the most recent (Aug-26) call, at the same time as the company continues to assert cash flow is "not a challenge." If this trajectory continues into the next reporting quarter, the credibility grade would be at real risk of falling to D regardless of continued operational delivery, because a grade this framework assigns is a test of what can be verified, not only of what was promised and met.

### 4D. Concall red flags

| Severity | Flag |
|---|---|
| HIGH | Total silence across four consecutive calls on the Rs89.65m procurement fraud and the qualified IFC opinion at both standalone and consolidated levels; no analyst asked either |
| HIGH | Total silence across four consecutive calls on the NHAI termination of a step-down SPV project and the associated sister-SPV auditor resignation |
| HIGH | Management repeatedly asserts strong/"amazing" cash flow and states "equity is not a problem" (May-26, p.6-7) while consolidated CFO was negative in FY25 (Rs -515.6cr) and FY26 (Rs -91.3cr per B03); never reconciled by management or raised by any analyst |
| HIGH | Consolidated debt disclosure and consolidated EBITDA/PAT disclosure both progressively degraded across four calls to zero disclosure of any kind in the most recent call (Aug-26), removing the two metrics most relevant to testing the company's own "cash is not a problem" claim in the same period (2F.4, 2F.6) |
| HIGH (upgraded from MEDIUM) | Written erratum in the filed May-26 transcript corrects unencumbered cash/FDR from a stated combined Rs412cr to an actual combined Rs241cr — a ~41.5% overstatement (this run's own recomputation; the ~71% figure sometimes quoted for this item appears to conflate the FDR line's Rs71cr absolute rupee change with a percentage) of exactly the liquidity metric used, in the same sentence, to argue "equity is not a problem." Given the magnitude, the load-bearing role of the sentence, and the compounding negative-CFO context, this run assesses HIGH rather than MEDIUM severity |
| MEDIUM-HIGH | No acknowledgment on any call of the WTD/CEO change between the Feb-26 call (Sudhir Hoshing, WTD) and the May-26 call (A. Sarvanan, CEO), consistent with B02/B03's five KMP/Board changes in ~14 months |
| MEDIUM | Order-book roll-forward (opening + inflow - revenue executed) does not close in any of the three testable quarters, with a persistent positive gap averaging ~Rs433cr per quarter (~2-3.4% of book size), never explained by management (2F.1) |
| MEDIUM | Renewable FY26 order inflow claimed (~Rs3,968cr, 35.02% of total) does not reconcile with the closing renewable order book (Rs3,525cr, 19% of total), a ~Rs443cr shortfall, against a segment B03 shows had near-zero execution all year (2F.5) |
| MEDIUM | Aug-26 per-project HAM equity list sums to Rs567cr against a stated total of Rs550cr, and the same call states both "10 HAM projects" (order-book table) and "all 11 of our HAM projects" (Q&A) — two unreconciled internal disagreements in one call (2F.7) |
| MEDIUM | Malout-Abohar-Sadhuwali HAM sale consideration never disclosed in any of four calls despite being cited repeatedly as proof of the capital-recycling thesis; an analyst-quoted figure of ~Rs177cr (Feb-26 call) neither confirmed nor denied |
| MEDIUM | The same call's prepared remarks describe the Malout-Abohar-Sadhuwali/Bathinda-Dabwali/Jalbehra-Shahbad divestments as "binding document" (one asset) or "non-binding offer...under due diligence" (two assets) (May-26, p.3), while the Q&A of the SAME call states "we have already sold three assets to Neo" (p.6) — a completed-sale framing for assets the prepared remarks, moments earlier, describe as not yet closed. The equivalent pattern also appears in the Feb-26 call: "in-principle approved a binding offer" (p.4) versus "we have already sold one HAM asset" (p.9) in Q&A |
| MEDIUM | Segment margin bifurcation for renewables and T&D asked in some form in all four calls and answered with an actual number in none — a four-quarter repeated evasion, confirmed independently in this run (2E) |
| MEDIUM | Promoter's personal Rs20cr equity in the Bathinda-Dabwali HAM SPV (Feb-26, p.6), an asset simultaneously targeted for third-party divestment (Feb-26, p.12-13); never explained on any call, never asked |
| MEDIUM | Southern Ludhiana bypass land status regressed rather than merely slipped: "very clear...80% by December" (Nov-25) versus "only 62% available" (Aug-26), a genuine reversal not surfaced or explained on any intervening call |
| MEDIUM | FY27 balance HAM/solar equity commitment of Rs859cr against only Rs23cr actually infused in Q1 FY27 (2.7% of the annual target in the first quarter) — too early to call a miss, but a pacing red flag worth watching each subsequent quarter |
| LOW-MEDIUM | Contingent liabilities at 83.7% of standalone net worth, and the standalone/consolidated bank-guarantee inconsistency, never mentioned on any call nor asked by any analyst |
| LOW | Ramban-Banihal (J&K) tunnel: three specific, time-bound promises (tunnel in 3 months, ~Rs180cr billed before March 2026, viaduct by March 2027) made in the Nov-25 call, never mentioned again in any of the three subsequent calls, and never asked about |
| LOW | FY27 order-inflow guidance restated three times inside six months (~Rs5,800cr Feb-26 -> "minimum Rs5,500cr" May-26 -> "Rs6,000cr" Aug-26) with no acknowledgment of any of the changes |
| LOW | Working-capital-day target asked twice (Nov-25, Aug-26) and answered with only qualitative language ("definitely there will be an improvement") both times, never a number |
| LOW | International order-inflow target ("at least 10-15%" of FY27 inflow, set Feb-26) dropped without mention in either the May-26 or Aug-26 call |
| LOW | The reason given for international caution shifts from routine conservatism (Nov-25 through May-26) to an unnamed "war situation" (May-26 and again Aug-26) that is never identified or explained, and no analyst asks what it refers to |

---

## Analyst note

Two things changed the shape of this finding set versus the first run. First, reading the Nov-25 call as a full primary transcript rather than a two-fact lookup surfaced seven items that were structurally invisible to a partial read: the intra-call Rs297cr/Rs200cr HAM equity inconsistency, the unanswered working-capital target, the Ramban-Banihal promises and their total subsequent silence, the Southern Ludhiana "80% by December" baseline that only reveals its own regression when set against the Aug-26 "62%" figure, and the original H1 FY26 consolidated-vs-standalone PAT/EBITDA anomaly that turns out to recur in 9M FY26 and only narrowly reverses at FY26 year-end. None of these are visible from three transcripts; each needs the Nov-25 call as an equal, not a footnote. Second, the explicit cross-call reconciliation pass (2F) caught findings that no single-call read could catch by construction: an order-book roll-forward gap that repeats every quarter in the same direction, a renewable inflow-versus-book gap of the same shape, a debt-disclosure trail that thins to nothing exactly as the consolidated P&L does, and a per-project equity list that does not sum to its own stated total in the same breath a project count contradicts the order book. None of these individually would move the credibility grade off C, because none rises to the level of the governance-silence findings B02/B03 already carry. Together, though, they describe a company whose disclosure quality is moving in the wrong direction over four quarters, which this run treats as the load-bearing addition to the record: the grade holds at C on delivered guidance, but the basis text names the trajectory explicitly so Stage 11 and the operator do not read a flat C the same way across two runs that found very different things.
