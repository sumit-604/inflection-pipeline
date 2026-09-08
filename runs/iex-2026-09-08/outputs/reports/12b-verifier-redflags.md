# Stage 12B — Verifier B: Independent Concall Red-Flag Audit
Indian Energy Exchange Ltd (IEX) | Run date 2026-09-08 | Model: claude-opus-4-8
Audited artifacts: B05-concall (run 2, REWORK) and B06-peers (run 1, unchanged)

---

## PROCESS NOTE — READ THIS BEFORE THE ACCEPTANCE RATE

Three facts govern how the number at the bottom of this report should be read.

**1. This is a POST-REMEDIATION measurement of stage 5, not a first-pass score.**
The stage-5 artifact is run 2. An earlier verifier-B pass measured run 1 at 38
percent coverage. The orchestrator fed that verifier's findings back into a full
re-run before handing the result to me. I built my own flag list from the raw
transcripts before opening any stage output, so my list is independent, but my
denominator is not the same denominator run 1 was scored against. My 36 percent
and run 1's 38 percent are NOT comparable and must never be reported as a
trend. Different lists, different lists' sizes, different auditors.

**2. My reading of B06 IS a first-pass measurement.** B06 has not been
reworked.

**3. B06 was built against stage 5 run 1's peer questions.** Stage 5 run 2
raises six peer questions, of which only one is addressed by B06. The new
question the task names — is fee realisation trailing volume growth sector-wide
or company-specific — has been tested by no stage. I test it myself in Part 5.

---

## PART 1: MY INDEPENDENT RED-FLAG LIST

Built from the four IEX transcripts alone, before reading B05 or B06, then
cross-checked against the corroborating filings. Anchors are `=== PAGE n ===`
marker numbers.

### Cluster A — Unit pricing: the subject management will not discuss

**A1. Fee realisation trailing volume growth: asked three consecutive quarters,
three different unquantified answers.**
- Q2FY26 (Nov 2025 p.17): Aditya Raval asks why volume rose 16.1% but revenue
  10.42%. Harlalka answers with the REC fee cut (Rs40 to Rs20) and lower REC
  volume.
- Q3FY26 (Feb 2026 p.9): Sumit Kishore presses on paisa/unit. Goel: "Revenue
  also includes annual fees by the members," then "Maybe there is a variation in
  the yearly fees." An explicit guess, no mechanism.
- Q1FY27 (Jul 2026 p.41): Ishan (Antique) asks the identical question. Goel:
  "in RECs and the Term Ahead Market, we give some incentive." A third answer,
  again with no number.
Independently confirmed from the filings: standalone revenue from operations
Rs 15,592.97 lakh over 37,534 MU = 4.15 paise in Q1FY27, against Rs 13,998.81
lakh over 32,384 MU = 4.32 paise in Q1FY26. The decline is real.

**A2. Management has admitted to discounting its fee and never quantified it.**
Feb 2026 p.9: "looking at the market conditions, we have to give incentives to
the buyers and sellers, some amount of incentive." Jul 2026 p.41: "we give some
incentive." This is a volunteered negative on pricing power, and it sits
against Apr 2026 p.14, where Goel offers TAM as proof that "the margins are
intact." A business that discounts to hold volume in a market it claims 99%
share of is a different business from the one the narrative describes.

**A3. The fee-competition question has been dodged in two separate sessions,
and the second dodge is total.**
- Nov 2025 p.17, Chirag Maroo: "if market coupling goes forward... are we
  willing to go into price wars?" Goel: "Why should we talk about war? Let us
  talk about peace."
- Jul 2026 p.34, Analyst 5: "can that lead to a more competitive pricing
  between the exchanges... What we saw in the TAM segment." Amit Kumar answers
  the API/MCO integration half of the question. The pricing half is answered by
  nobody, and the moderator moves on.
Two quarters, same subject, no policy stated either time. Post-coupling fee
competition is the single variable that determines whether coupling is a
volume event or an earnings event.

### Cluster B — Segment deterioration visible in IEX's own filings, absent from the call

**B1. The REC explanation is contradicted by IEX's own filing.** Asked at the
24-Jul-2026 meet why RECs were down 80% (Jul 2026 p.41), Goel gives a
demand-side answer: buyers are confused by a draft RPO buyout provision, "when
there is more clarity on this, the REC volumes would pick up." IEX's own Power
Market Update of 3-Jul-2026, filed three weeks earlier, says the opposite
mechanism: "Sell bids declined by 86.1% YoY, leading to a rise in clearing
prices during Q1FY27" (Q1FY27 update p.2). Volume collapsed while price ROSE.
That is a supply failure, not buyer hesitancy. Management named the wrong side
of the market, and the correct side is in its own document. Confirmed again in
the Jul-2026 update (p.2, sell bids -77.8%) and the Aug-2026 update (p.2,
-86.6%, "due to lower participation").

**B2. A supply-restricting REC regulation was framed as supply-positive one
quarter before supply collapsed.** Apr 2026 p.4: the CERC first amendment to
the REC Regulations 2026 bars captive plants from trading RECs to the extent of
self-consumption. Management presents the package as inventory-enhancing:
"These multipliers should help increase REC inventory going forward." The
following quarter, sell bids fell 86%.

**B3. The green market's growth collapsed and the analyst meet does not
mention it.** FY26 green volume +23% (Apr 2026 p.6). Q1FY27 +6.3%, and June
2026 -1.2% YoY (Q1FY27 update p.2). At the 24-Jul meet, green is described as
"substantial... about 7-8% of the product mix" (Jul 2026 p.11) with no
reference to the deceleration. The green/RCO leg is a stated growth pillar.

**B4. DAM, the segment market coupling actually threatens, is in absolute
decline, and nobody says so.** DAM including HP-DAM: June 2026 -6.6% YoY, July
2026 -7.7% YoY, Q1FY27 +7.6% against total volume +15.9% (Q1FY27 and Jul-2026
updates, p.2 each). The entire coupling defence rests on DAM franchise
durability. The segment is shrinking on its own, before coupling exists.

**B5. Market-share disclosure has become less precise as the threat has
grown.** Q2FY26 (Nov 2025 p.17): electricity 84%, certificates just above 50%,
overall 75%, DAM and RTM "100%, 99% precisely," TAM 35%. Q3FY26 (Feb 2026
p.15): electricity 83% for 9M, and TAM now "varies between 45%, 50%" — a jump
from 35% one quarter earlier, unexplained and unremarked. Q4FY26: no market
share figure given at all. Q1FY27 (Jul 2026 p.7): back to a range, "we have
always been maintaining 80-85% market share." The number that governs the
thesis got vaguer every quarter.

### Cluster C — Guidance and prediction failures

**C1. RTM forward guidance cut to 25-30% and then falsified within weeks.**
Jul 2026 p.29: "it will definitely grow at a rate of 25 to 30 percent in the
time to come," against FY26's delivered +41%. Delivered: July 2026 +10.2%,
August 2026 +10.6%.

**C2. "Things will definitely go in our favour" was falsified in fourteen
days.** Feb 2026 p.7, asked what happens if APTEL rules against IEX, Goel
refuses the premise: "First of all, why are you saying that if things don't go
in our favour? Things will definitely go in our favour." APTEL's order of
13-Feb-2026 dismissed IEX as not an aggrieved party (Apr 2026 p.5).

**C3. Three mutually inconsistent CMD answers on coupling market-share
impact.** Apr 2026 p.14: "we should be able to retain a significant part of the
market share." Jul 2026 p.4, scripted opening: "even if there is an impact, it
may be about 20, 30, 40% (in DAM)." Jul 2026 p.35, same session, asked
directly: "I don't see any loss in market share after the coupling." The only
quantified admission appears once, in prepared remarks, and is withdrawn under
questioning in the same room.

**C4. Coal exchange sizing inflated 50% in one quarter, inconsistent inside a
single session, with an unsupported target on top.** Apr 2026 p.8 and p.17:
"about 80 million tonnes," "80 to 90 million tonnes." Jul 2026 p.5 and p.31:
"almost about 120 million tonnes," twice. Same Jul session, Bajaj p.8 sizes the
incumbents at "70-80 million tonnes." Harlalka p.26 asserts "at least 100
million ton we are expecting at the exchange platform in the initial year."
Goel p.30 asserts the fee "will be definitely higher than what MSTC and
Mjunction are charging" — pricing power claimed in a market IEX has never
operated, with no licence yet granted.

**C5. IGX divestment: 18 months requested, 12 granted, hard stop, and the CMD
did not know the status.** Nov 2025 p.11: deadline Dec-2025; extension sought;
"we have requested for one and a half years." Apr 2026 p.10: "PNGRB has given
us time up to 31st of December 2026." Same call, p.11, asked where the IPO
process stands: "I'm not really fully aware about the exact status of that."
A compliance deadline with no second extension assured, and the CMD is not
tracking it.

### Cluster D — Disclosure posture

**D1. Customer concentration surfaced as the last question of a two-hour
meet, then partly withdrawn.** Jul 2026 p.41: top buyers 50-60% of volume, top
10 sellers about 40%. "This 50-60 versus 40 has remained the same over the last
few years. I can't say that it has remained the same, but it is in that range."
The same answer volunteers seasonal churn — "one season there are new set of
buyers, another season those are not there at all" — which cuts directly
against the 18-years-of-loyalty defence used against coupling.

**D2. Non-operating income is a rising share of profit and nobody mentions
it.** Never raised by management or by any analyst across four transcripts.

**D3. Buyback stalled for two quarters after the stated blocker was removed.**
Apr 2026 p.11: "definitely considering it," waiting on SEBI's open-market route.
Jul 2026 p.29: Goel confirms "SEBI also has revised its rules for doing the
buyback through the market," then still says "we will consider that part of
it." The reason for waiting was gone and the answer did not change. The analyst
raising it says valuations are "at an all-time low"; management does not
dispute the characterisation.

**D4. "No additional costs."** Apr 2026 p.14, asked to estimate the cost of the
software re-engineering that MCO integration would force: Goel, unqualified,
"No additional costs." In the same call he says Grid India building the same
capability "will be additional costs," and in Jul (p.21) he relays Grid India's
own submission that the cost of running coupling must be weighed against the
claimed 0.3% benefit. An unexamined answer on a real integration cost.

**D5. Carbon timeline accelerated while the materiality caveat was dropped.**
Nov 2025 p.13: trading needs "another one and a half, maybe one to one and a
half year," with a caveat that decides whether the market exists at all: "If
everybody is complying, then there's no trading." Feb 2026 p.13: "FY '27 or
'28." Jul 2026 p.5: "within this calendar year... BEE has said that they want to
start it by 1st of October 2026." The date pulled in by roughly a year; the
caveat that governs the size of the opportunity has disappeared.

**D6. Management labels its own base year an outlier.** Jul 2026 p.15, Bajaj:
FY26 was "an outlier year - very low prices, no demand increase, very good
weather, everything was an outlier... probably we will not get similar year in
some times to come." Any run-rate projection built on FY26 is projecting a year
management has disowned.

### Cluster E — Internal numerical inconsistency

**E1. RTM and DAM share of mix stated three ways.** Feb 2026 p.5: RTM
"maintaining 40% share." Apr 2026 p.6: RTM "39% share in electricity volumes"
for FY26. Jul 2026 p.11, Bajaj: DAM "reduced to 39%," RTM "grown to as high as
34% by last year." Jul 2026 p.4, Goel, same session: DAM "reduced to almost
about 40%." Denominators are never stated, so the reader cannot reconcile them.

**E2. Two revenue figures for the same quarter and the same year inside one
presentation.** Jul 2026 p.5, Goel: FY26 consolidated revenue "13.6% at Rs.747
crore"; Q1FY27 "202.8 crore rupees." Jul 2026 p.26, Harlalka: "total revenue
was somewhere around Rs. 745 crore during the previous year"; "This quarter we
achieved almost around Rs.201 crores."

**Total independent red-flag-grade items: 22.**

---

## PART 2: COMPARISON TABLE

| # | My item | Status | Where B05/B06 handles it | Severity of the gap |
|---|---|---|---|---|
| A1 | Realisation trailing volume, 3 quarters, 3 answers | **CAUGHT** | B05 red flag 1 (HIGH), 2B, 2E, 4A trigger 2; paisa figures independently computed | — |
| A2 | Admitted, unquantified fee incentives contradicting "margins intact" | **PARTIALLY CAUGHT** | Folded into A1 as one of three deflection answers; not raised as a standalone pricing-power finding | MINOR |
| A3 | Fee-competition question dodged Nov-2025 and Jul-2026 | **PARTIALLY CAUGHT** | B05 2C quotes "Let us talk about peace" as defensiveness; the Jul-2026 leg is not identified and the pair is not booked in repeated_evasions | MAJOR |
| B1 | REC explanation contradicted by IEX's own 3-Jul filing | **MISSED** | B05 flags the recycled excuse (LOW-MEDIUM) but not that the stated mechanism is wrong on the company's own data | MAJOR |
| B2 | Apr-2026 REC regulation framed as supply-positive before supply collapse | **MISSED** | Absent | MAJOR |
| B3 | Green market +23% to +6.3%, June -1.2%, undisclosed on the call | **MISSED** | Absent | MAJOR |
| B4 | DAM in absolute decline, the coupling-exposed segment | **PARTIALLY CAUGHT** | Cited inside 2B only as mix evidence for the realisation gap; never raised as its own flag | MAJOR |
| B5 | Market-share disclosure degrading; TAM 35% to 45-50% unexplained | **MISSED** | Absent | MAJOR |
| C1 | RTM 25-30% falsified within weeks | **CAUGHT** | B05 red flag 2 (HIGH), promise_delivery row; both monthly legs exact | — |
| C2 | "Things will definitely go in our favour" falsified in 14 days | **PARTIALLY CAUGHT** | 2B flags it as over-promotion; the promise table books only the TIMING leg of the same answer, as DELIVERED, and never books the substantive prediction as a miss | MAJOR |
| C3 | Three inconsistent answers on coupling share impact | **CAUGHT** | B05 1C and red flag; within-call contradiction correctly identified | — |
| C4 | Coal sizing 80 to 120mn, internally inconsistent, 100mn target | **CAUGHT** | B05 1C, 2E, guidance rows, red flag; strongest single piece of work in the artifact | — |
| C5 | IGX 18-vs-12 month extension, CMD unaware of IPO status | **PARTIALLY CAUGHT** | Guidance row records the 18-vs-12 gap explicitly; the CMD's unawareness is not flagged | MINOR |
| D1 | Concentration disclosed last, self-contradicted, churn undercuts loyalty | **CAUGHT** | B05 red flag and 3D, including the churn/loyalty tension | — |
| D2 | Non-operating share of PBT rising, unremarked | **CAUGHT** | B05 red flag (LOW), computed; B06 Claim 2 tests it against peers | — |
| D3 | Buyback stalled after blocker removed | **CAUGHT** | B05 1C, promise_delivery row; does not note the blocker was removed | — |
| D4 | "No additional costs" unqualified | **MISSED** | Absent | MINOR |
| D5 | Carbon timeline pulled in, materiality caveat dropped | **PARTIALLY CAUGHT** | Timeline shift caught in timeline_slippages; the dropped caveat is not | MINOR |
| D6 | Management labels FY26 an outlier year | **PARTIALLY CAUGHT** | 2D covers the adjacent point (cheap-power thesis not revisited); the explicit outlier label is not carried forward as a base-rate warning | MINOR |
| E1 | RTM/DAM mix stated three ways | **MISSED** | Absent | MINOR |
| E2 | Two revenue figures in one presentation | **MISSED** | Absent | MINOR |
| — | I-REC Q1FY27 -4.5% undisclosed while "200% growth" presented | **CAUGHT** | B05 1A row and red flag | — |

**Tally: 8 CAUGHT, 7 PARTIALLY CAUGHT, 7 MISSED, out of 22.**

### The shape of what was missed

The seven full misses are not scattered. Five of them (B1, B2, B3, B5, and the
DAM half of B4) are one gap with one name: **stage 5 read the monthly Power
Market Updates for the two metrics it already suspected — RTM growth and the
REC headline — and did not difference the filings against the call narrative
segment by segment.** Had it done so, green (+23% to +6.3%), DAM (two
consecutive negative months), REC's sell-side mechanism, and the market-share
series would all have surfaced from documents already in the corpus and already
open on the desk. Two more (E1, E2) are internal-consistency sweeps of the
transcripts that were not run.

This matters for how the orchestrator should read the score. Run 1's problem,
per the note I was given, was breadth. Run 2's residue is not breadth: it is one
identifiable, cheap, mechanical procedure that was not performed. A third full
re-run is not obviously the right instrument. A targeted amendment that (a)
performs the segment-level filing-versus-call difference, (b) books B1 and
upgrades the REC flag from LOW-MEDIUM to HIGH, and (c) adds B2, B3 and B5,
would close most of the gap. That call is the orchestrator's; I record the
measurement and the diagnosis.

---

## PART 3: PIPELINE FLAGS I DID NOT INDEPENDENTLY FIND

Rule: SUPPORTED / OVERSTATED / NOT SUPPORTED.

| Pipeline flag | Assessment | Basis |
|---|---|---|
| CFO's 42-44% ROE does not reconcile (computed 35.2% consolidated, 36.3% standalone) | **SUPPORTED**, with one unstated caveat | Harlalka does state both legs in one breath (Jul 2026 p.26). Arithmetic checks. Caveat B05 does not address: ROE is conventionally computed on AVERAGE equity, and with a 50-65% payout the average is materially below the Rs 1,400cr closing figure, which narrows the gap; and "42% to 44%... over the last 4-5 years" may be a historical average, not an FY26 claim. The finding stands; its force is slightly overstated. |
| Non-operating share of PBT 23.4% FY26 to 29.8% Q1FY27 | **SUPPORTED** | I reproduced the inputs independently. Consolidated other income Rs 131.30cr FY26 and Rs 44.93cr Q1FY27 match the filed results. The associate legs check out exactly: IGX FY26 PAT Rs 41.9cr x 47.3% = Rs 19.8cr; IGX Q1FY27 PAT Rs 16.3cr x 47.3% = Rs 7.71cr against B05's Rs 7.72cr. Well constructed. |
| Three 2023 launches (HP-DAM, HP-TAM, Ancillary) are admitted failures | **SUPPORTED** | Verbatim at Jul 2026 p.11: "all these three markets are not doing very well because liquidity is not there." One complication B05 does not note: TAM including HP-TAM was +111.3% YoY in Aug-2026, so the aggregate has since moved, though HP-TAM alone is not broken out. |
| Coupling "ordered by January 2026" counted as a MISSED promise | **OVERSTATED as a management miss** | The fact is true and B05 attributes the promiser honestly to the CERC order rather than to IEX. But B05's own 2B calls this delay "genuinely external." Carrying it as a row in a MANAGEMENT promise-delivery tally inflates the missed count with an item management neither promised nor controlled. |
| M-Junction/MSTC exclusion is "a regulatory fact... credible, sourced to the notified rules" | **OVERSTATED** | It rests entirely on management's characterisation; the Coal Rules text is not in the corpus. B05's own analyst_note applies exactly the opposite and correct standard to the APTEL order. The same standard should apply here. |
| B06 Claim 4 CONTRADICTED via CDSL | **SUPPORTED**, anchor verified | I checked the load-bearing anchor directly: CDSL Aug 2026, Hiral Parekh, "for our incremental demat market share, we have lost about 420 bps since close of March. So, we're standing at 81.4% in June '26." B06 quotes it accurately and the one-quarter-later structure of the contradiction is real. |
| B06 Claim 2 VERIFIED | **SUPPORTED**, but note the logic | The verdict rests on peer SILENCE. That is legitimate here only because the claim itself is a claim about absence (that no peer tracks share-of-PBT either). B06 states this openly. Acceptable, and B06 correctly refuses to upgrade Claim 3 on the same basis. |

**No pipeline flag in either artifact was NOT SUPPORTED. No signal was
invented.** Across three independent arithmetic reconstructions (paisa/unit,
associate-profit share, other income) B05's computed figures reproduced. This is
the strongest thing I can say about the artifact and it should not be lost
behind the coverage number.

---

## PART 4: PROMISE-DELIVERY SPOT CHECKS

Five checks. For each: does the earlier call actually contain that promise, and
does the later document actually show that outcome?

| # | B05 row | Promise present? | Outcome as stated? | Verdict |
|---|---|---|---|---|
| 1 | "15-20% volume growth for FY27" → delivered, +15.9% | YES — Apr 2026 p.13, Goel: "we should be able to maintain this volume growth of 15% to 20%" | YES — Q1FY27 press release p.2, 37.5 BU, +15.9% | **CONFIRMED.** Unnoted: July 2026 monthly was +7.7%, below the band. B06 catches this at 2A; B05 does not. |
| 2 | "REC to end FY26 better than FY25" → partial, +5% | YES — Feb 2026 p.9, "by the end of the year, we will be able to still do better than what we did last year" (B05 cites p.8, marker is p.9) | YES — Apr 2026 p.6, "187 lakh RECs were traded, recording a 5% increase" | **CONFIRMED.** The promise as worded was met; "delivered" would have been equally defensible. Conservative grading, not an error. |
| 3 | "RTM 25-30%" → missed, Jul +10.2%, Aug +10.6% | YES — Jul 2026 p.29, verbatim | YES — Jul update p.2 (5,631 vs 5,109 MU, +10.2%); Aug update p.2 (5,565 vs 5,029 MU, +10.6%) | **CONFIRMED**, both legs exact. |
| 4 | "No significant margin impact" → missed, 4.16 vs 4.33 paise | YES — Apr 2026 p.14, verbatim | Arithmetic reproduced: 4.154 and 4.323 paise from the filed standalone revenue and volumes | **CONFIRMED on both legs, but the LINK is overstated.** Goel was answering a post-coupling hypothetical, not making a present-tense margin commitment. Coupling has not happened. Scoring a conditional statement as a missed promise against a realisation decline from an unrelated cause (mix and incentives) is a classification stretch. |
| 5 | "APTEL verdict within a month" → delivered | YES — Feb 2026 p.7, "it should happen within a month's time" | YES — Apr 2026 p.5, order issued 13-Feb-2026, roughly two weeks | **CONFIRMED** on direction. But on the same transcript page Goel also predicted the SUBSTANCE ("Things will definitely go in our favour"), which failed. The table books the timing leg as a delivery and books the substantive leg nowhere. |

**Checked 5, confirmed 5, wrong 0.** Direction is correct on every row I tested
and no promise was fabricated. Two rows carry classification problems (4 and 5)
rather than factual ones.

**Separate omission:** the one promise management KEPT that B05 does not book —
Apr 2026 p.9, the CFO on treasury income, "as the market is recovering, we will
see that the numbers going back to the earlier numbers." Delivered: standalone
other income Rs 22.11cr in Q4FY26 to Rs 44.92cr in Q1FY27, back above Q1FY26's
Rs 42.52cr. B05 praises this same answer as its one HONEST-ADMISSION in 2B but
never scores the follow-through. Adding it would make the tally 4 delivered / 2
partial / 5 missed. The omission works against management, not for it, so it is
not a self-serving gap — but the table is incomplete.

---

## PART 5: THE UNTESTED PEER QUESTION

Stage 5 run 2 asks whether fee realisation trailing volume growth is sector-wide
or company-specific. No stage has tested it. B06 answers run-1's questions. I
tested it directly against the twelve peer transcripts.

**The peer transcripts DO answer it, partially, and the answer cuts both ways.**

**The phenomenon is sector-wide.** All three peers show fee realisation moving
against activity in this same window.
- MCX, Aug 2026 p.11-12. Shrenik Mehta puts a 68% yield compression to
  management: bullion options premium-to-notional from 1.03% to 0.35%, and asks
  it decomposed across four named buckets.
- CDSL, Aug 2026 p.7. Sanketh Godha puts IEX's exact structural question to
  CDSL: folio count growing 17% YoY, annual charges revenue growing 12%.
- BSE, Nov 2025 p.11. Management volunteers that volatility made "the premium
  realization per contract different... thus compressing the margins."

**The causes at peers are external and named; IEX's is neither.**
- CDSL's compression is a SEBI-mandated, industry-wide fee cut, quantified
  exactly on the call by Sunil Alvares: KYC fetch Rs35 to Rs28, a 20% decline;
  creation Rs20 to Rs5, a 75% decline (Aug 2026 p.7).
- MCX's is volatility normalisation, and management works the decomposition:
  move from ADT to ADV to strip the price effect, attribute predominantly to
  volatility, and explicitly rule out contract mix and participation shift
  ("Contract mix is not where we are seeing the big play" — Praveena Rai;
  "there's no shift in the participation or... the contract mix" — Praveen DG),
  Aug 2026 p.11-12.
- No regulator cut IEX's fees. IEX's stated causes are voluntary incentives and
  product mix, and it has quantified neither in three quarters of being asked.

**One point genuinely favours IEX.** Refusing to quantify realisation net of
discounts has clear peer precedent. CDSL, Aug 2026 p.7, asked by Swarnabh
Mukherjee whether the realisable rate after volume discounts fell as far as the
rack rate: "We do not discuss this in our investor calls." BSE, May 2026 p.11,
asked about pricing strategy, gives an equally generic answer ("appropriate
amounts at appropriate points of time"). Opacity on net realisation is a sector
norm, not an IEX invention. Note also that CDSL's own answer to the
volume-versus-revenue question is a single line ("If you compare on
quarter-on-quarter basis, yes"), so thin answers to this specific question are
not unique to IEX either.

**Verdict for the record: PARTIALLY ANSWERED.** The phenomenon is sector-wide.
IEX's cause is not explained by the sector, because IEX had no mandated fee cut
and no volatility mechanism to point at. Its refusal to quantify is
sector-normal. The correct downstream read is therefore narrower than stage 5's
framing: the DISCLOSURE criticism should be softened, and the ECONOMIC finding
— an unexplained, self-inflicted, unquantified realisation decline at a claimed
99%-share monopoly — should be kept at full weight.

**Coverage gap, stage 6.** Only 1 of B05 run 2's 6 peer questions (question 6,
the BSE-versus-NSE trajectory, via Claim 4) is addressed by B06. Questions 1
through 5 are untested. This is not a defect in B06's own work — the inputs
changed underneath it — but it is a live pipeline state. Verifier D's rule 5
(every claim in the injected peer_questions list receives a verdict) will fail
against the current B05 unless B06 is re-pointed at the run-2 questions. Part 5
above discharges question 1; questions 2 through 5 remain open.

---

## PART 6: ANCHORING

B05 states it cites `=== PAGE n ===` markers and warns it "may differ by one
from the printed page footer." In practice the convention is mixed: many
citations are printed-page numbers, off by one from the marker, and at least
three are off by two — "Q2FY26 p.7" for the 15-20% guidance (marker p.9),
"Q2FY26 p.9" for the realisation question (marker p.17, and cited as "p.16-17"
elsewhere in the same report), "Q3FY26 p.11" for the 15-20% and IGX guidance
(marker p.13).

**Every item I traced exists in the transcript at or near the cited page.** This
is a locatability defect, not a fidelity defect, and I make no source-fidelity
call — that authority is Verifier A's alone. Graded MINOR.

---

## PART 7: CREDIBILITY GRADE

**B05 grades management C (Mixed). I concur, at the bottom of the C band.**

Every additional item I found cuts the same direction: selective framing of
segment-level deterioration that is already public in IEX's own monthly filings
(REC's sell-side mechanism, green at +6.3%, DAM negative for two months, market
share disclosed ever more vaguely). That is a heavier pattern than B05's
evidence alone supports, and it argues for the low end of the band rather than a
different band. I would not move it a full grade, because the countervailing
evidence B05 records is real: volume guidance met at the quarter level, dividend
policy delivered as stated, the treasury-income miss explained specifically and
then actually corrected, and an IGX Q1 guidance that proved too conservative
rather than too generous.

---

## PART 8: FINDINGS SUMMARY

Critical 0 | Major 8 | Minor 13.

No CRITICAL. The rule that would fire one — a MISSED repeated evasion across
2+ quarters — does not fire: the fee-competition evasion (A3) is the only
candidate, and B05 saw and quoted its Nov-2025 leg, so it is PARTIALLY CAUGHT
rather than MISSED. The classification failure is real and graded MAJOR.

No pipeline flag was NOT SUPPORTED in either artifact.

**acceptance_rate: 36% (8 caught / 22 independent flags).** Applying the rubric
formula strictly, which counts only full catches. Caught plus partially caught
is 15 of 22, or 68%. Both numbers are stated because the strict figure, on its
own, misdescribes an artifact whose principal weakness is under-weighting
evidence it had already found, not failing to find it. This is a
post-remediation measurement of stage 5 and is not comparable to run 1's 38%.
The stage-6 reading is a first-pass measurement.
