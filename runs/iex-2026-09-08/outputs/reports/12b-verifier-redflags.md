# Stage 12B: Verifier B — Independent Concall Red-Flag Audit
## Indian Energy Exchange Ltd (IEX) | Run date 2026-09-08 | Model: claude-opus-4-8

---

## PROCESS NOTE — READ THIS BEFORE THE ACCEPTANCE RATE

This measurement is **POST-REMEDIATION** and is **not comparable** to either
earlier verifier-B figure for this run.

- **Stage 5 is run 3.** Run 1 was measured at 38% by an earlier verifier-B
  pass. It was reworked in full to run 2, measured again at 36% strict and
  68% including partial catches. Run 3 is a targeted amendment written
  against that second pass's specific findings.
- **Stage 6 is run 2**, re-pointed because stage 5's `peer_questions[]`
  changed under it.

Both artifacts have therefore already absorbed two rounds of adversarial
findings. My 65% is a measurement of what an independent reader still
out-lists after that remediation, against a much harder residual set. It
must not be read as "the stage got 65% right." It must be read as: of 26
red-flag-grade items I independently derived, 17 were caught in full, 6 were
found but placed or weighted differently than I would place them, and 3 were
absent. Zero pipeline flags were NOT SUPPORTED.

The materiality read is at the end of this report and is the part that
matters more than the number.

---

## METHOD

I read the four IEX transcripts in full, first, forming my own list before
opening any stage output. I then read the Q1FY27 press release, the Q1FY27
and June-2026 Power Market Update, the July-2026 update and the August-2026
update to test whether call statements were borne out. Only then did I open
B05/05-concall and B06/06-peers. I spot-verified peer citations by grep in
the four peer transcripts named below.

Every anchor in this report is the `=== PAGE n ===` marker number in the
named file, confirmed by grep against the marker index of that file.

Files:
- `other__Concall_Nov_2025_Q2FY26_Transcript.txt` (Q2FY26, call 31-Oct-2025)
- `concalls__Concall_Feb_2026_Transcript.txt` (Q3FY26, call 30-Jan-2026)
- `concalls__Concall_Apr_2026_Transcript.txt` (Q4FY26/FY26, call 24-Apr-2026)
- `concalls__Concall_Jul_2026_Transcript.txt` (Q1FY27, Analyst Meet 24-Jul-2026)

---

## PART 1: MY INDEPENDENT RED-FLAG LIST

Twenty-six items, ordered by weight. Severity is my own, formed before I read
the stage outputs.

### Tier 1 — Would move a thesis

**IF-01. Same-call self-contradiction on the single largest thesis risk.**
In opening remarks Goel volunteers a quantified coupling impact for the first
time in four quarters: "even if there is an impact, it may be about 20, 30,
40% (in DAM)" (Jul-2026, p.5). In the Q&A of the same session, asked the
identical question by Analyst 6 — "what is the possible market share loss
that you're looking in case the DAM is coupled" — he answers "With the kind
of service which we have provided in the last 18 years... I don't see any
loss in market share. after the coupling" (Jul-2026, p.35). The two answers
cannot both be management's view. The one number in the corpus that lets an
analyst size the downside is withdrawn within two hours of being given.
**MAJOR.**

**IF-02. A confident prediction falsified in fourteen days.**
Asked what happens if APTEL rules against IEX, Goel refuses the premise:
"First of all, why are you saying that if things don't go in our favour?
Things will definitely go in our favour" (Feb-2026, p.8). APTEL's order of
13-Feb-2026 held IEX "is not an aggrieved party at this stage" and disposed
of the appeal on standing (recited in Apr-2026, p.5). CERC then issued draft
coupling regulations on 17-Apr-2026 naming Grid India as MCO (Apr-2026, p.5).
No later call revisits the prediction. **MAJOR.**

**IF-03. Fee realisation deflected in three of four calls, three different
answers, never a number.**
Nov-2025 (p.16-17): Harlalka attributes the revenue/volume gap to the REC
fee cut Rs40 to Rs20 plus lower certificate volume. Feb-2026 (p.10): Sumit
Kishore shows the paisa/unit ratio is still off after that adjustment; Goel
offers "Revenue also includes annual fees by the members," then "Maybe there
is a variation in the yearly fees" — no mechanism. Jul-2026 (p.42): Ishan
from Antique asks again; Goel answers "there are fuel markets like in RECs
and the Term Ahead Market, we give some incentive." Three quarters, three
different unquantified answers, no reconciliation. **MAJOR** (repeated
evasion, 2+ quarters).

**IF-04. The pricing question is never answered, twice.**
Nov-2025 (p.18): asked directly whether IEX would enter a price war after
coupling, Goel says "Why should we talk about war? Let us talk about peace."
Jul-2026 (p.34): Analyst 5 asks whether coupling "can lead to a more
competitive pricing between the exchanges... What we saw in the TAM segment."
Amit Kumar answers only the API/integration half (p.34-35); the pricing half
is never addressed by anyone in the session. Pricing is the mechanism by
which a coupled market erodes an exchange's economics. **MAJOR** (repeated
evasion, 2+ quarters).

**IF-05. The REC explanation names the wrong side of the market.**
Feb-2026 (p.9) and Jul-2026 (p.41) both blame a buyer-side regulatory
"confusion" over the RPO buyout provision. The company's own Power Market
Update filed 03-Jul-2026, three weeks before the second instance, states:
"Sell bids declined by 86.1% YoY, leading to a rise in clearing prices during
Q1FY'27" (Q1FY27/Jun'26 update, p.3). Volume collapsing while price rises is
a seller shortage. The two accounts are incompatible. **MAJOR.**

**IF-06. Market-share disclosure precision falls as the coupling threat
rises.** Nov-2025 (p.17): "electricity market share is 84%... IDM and RTM is
100%, 99% precisely. And in the other TAM segments, it is 35%" — a full
product split. Feb-2026 (p.16): "around 83% in first nine months... TAM, it
varies between 45%, 50%" — the TAM figure moves 35% to 45-50% with no
explanation, and Bajaj adds "I do not have exact number for REC available
right away." Apr-2026: no percentage anywhere in the transcript, only "we
should be able to retain a significant part of the market share" (p.14).
Jul-2026 (p.7): a bare "we have always been maintaining 80-85% market share,"
no split, no period. **MAJOR.**

**IF-07. RTM, the star product, decelerating hard while forward guidance
rises.** Segment growth: FY26 +41% (Apr-2026, p.6); Q4FY26 +48.2%; Q1FY27
+23.5% (Q1FY27 update, p.2); Jul-2026 +10.2%; Aug-2026 +10.6%. Bajaj
volunteers "Similar is the situation in this Q1. We are up in RTM segment by
about 25%" (Jul-2026, p.12) and Goel then guides "it will definitely grow at
a rate of 25 to 30 percent in the time to come" (Jul-2026, p.29) — a forward
number set above the run rate already visible, and falsified by the company's
own next two monthly prints. **MAJOR.**

**IF-08. Day-Ahead volume, the exact segment coupling targets, in outright
decline.** June-2026 -6.6% YoY, July-2026 -7.7% YoY, Q1FY27 +7.6% against
total +15.9% (Q1FY27/Jun'26 update p.3; Jul'26 update p.2). August rebounds
to +15.0% but on buy bids +61.7% (Aug'26 update, p.2), i.e. demand-pull, not
a mix reversal. Not named as a risk on any call. **MAJOR.**

**IF-09. Q1FY27 breaks the growth mechanism, in both regimes.**
Management runs two alternative engines. Regime A (Feb-2026, p.9): when
demand is flat, low prices drive optimisation volume — FY26 delivered +17%
on flat demand with DAM price -14%. Regime B (Jul-2026, p.13, Bajaj): "power
exchanges, all put together grew by 18% last year. Demand growth was just 1%.
So whatever incremental growth was there, majority of that came to exchanges."
Q1FY27 tested Regime B: national consumption +8.8%, DAM price +15.7%, RTM
price +13.8% (Q1FY27 press release, p.2) — and IEX volume grew +15.9%,
statistically the same as the flat-demand year. Then July-2026 broke it
outright: national consumption +10.9% against IEX volume +7.7% (Jul'26
update, p.2) — the first month in the corpus where IEX grew **slower** than
national demand. August confirms the constraint from the other side: DAM buy
bids +61.7% but DAM cleared volume only +15.0% with price +22% (Aug'26
update, p.2) — the platform is sell-side constrained in a high-price regime,
so the "we capture the incremental demand" claim underpinning the 8%-to-25%
penetration thesis (Jul-2026, p.33) fails exactly when demand arrives.
**MAJOR.**

**IF-10. Coal exchange TAM inconsistent across quarters and inside one
session.** Apr-2026 (p.8): "last year, the e-auction coal transaction was
about 80 million tonnes"; later (p.17) "80 million to 90 million tonnes."
Jul-2026 (p.6): Goel "almost about 120 million tonnes"; restated (p.31)
"almost about 120 million tonnes. Coal India alone did e-auctions of about 90
million tonnes." In the same session Bajaj sizes the incumbents at "70-80
million tonnes of coal in a year" (p.8) and Harlalka states "the initial
target of at least 100 million ton we are expecting at the exchange platform
in the initial year" (p.26). Four figures, one meeting, no bridge. The
load-bearing regulatory claim under all of them — that e-auction platforms
including Coal India's own are barred six months after the coal exchange
launches (p.6, p.8, p.31) — is management's characterisation; the Coal Rules
text is not in the corpus. **MAJOR.**

**IF-11. The 2023 product cohort failed, and the failure is never connected
to the pending cohort.** Bajaj, unprompted: "in 2023 we introduced the High
Price Day Ahead Market (HP-DAM), (High Price) Term Ahead Market and Ancillary
Market. Unfortunately, all these three markets are not doing very well
because liquidity is not there" (Jul-2026, p.12). ESCerts (2017) is separately
described as "not a very liquid market." That is the base rate for IEX
product launches — and the growth case rests on three further pending
launches (Green RTM, peak DAM/RTM, 11-month TAM). Management never draws the
line. **MAJOR** — this is the single best-evidenced check on the entire
optionality stack, and it is volunteered by management itself.

**IF-12. The 11-month TAM sizing is contradicted by management's own demand
admission.** Feb-2026 (p.12): "for long-duration contract, the market size can
be another 15 billion, 20 billion units." Jul-2026 (p.17), Bajaj sizes the
adjacent DEEP market at "about 30 odd billion units." But in the same July
meet Goel concedes the opposite on demand: "if you look at transactions in the
contracts which are beyond three months, those are not significant" (p.40),
and confirms "It's been more than two years since we have applied." A 15-20 BU
opportunity claim sits directly on top of an admission that the existing
analogue has no meaningful demand. **MAJOR.**

**IF-13. Nov-2025 "no developments" versus Jul-2026 "the four months period
they have run this pilot."** Nov-2025 (p.8), asked whether IEX had been
contacted to build coupling software: "we are not aware about any developments
which have taken place so far... to the best of our knowledge, so far, nothing
like that has happened." Jul-2026 (p.20), Bajaj: "we have done our own
simulation and precisely this is what is happening today. For the four months
period they (Grid India) have run this pilot, social welfare increase... has
happened for the seller not for the buyer and effectively the price has gone
up. And the price increase has been much more than 0.3%." Two problems. First,
a four-month Grid India pilot is a development, and the Nov-2025 answer reads
thinner against it — though in fairness Grid India's own comments describe the
pilot software as post-facto and unaudited (Jul-2026, p.21), so it may have
been an analytical exercise run after Nov-2025, and the contradiction is not
certain. Second, and firmer: IEX's counter-quantification rests entirely on
its own unpublished simulation, asserted as established fact in an investor
forum, in support of a live Supreme Court petition, while complaining that
the regulator's studies were never published. **MAJOR.**

### Tier 2 — Material, second order

**IF-14. Buyback stalled after its own stated blocker was removed.**
Apr-2026 (p.11), Harlalka: "We are definitely considering it. And we are also
waiting for the draft note with SEBI had come out with regards the open market
route, which they had disallowed earlier." Jul-2026 (p.29-30), asked by
Paresh Sanghani "given the valuations are at an all-time low," Goel: "buyback,
yes definitely, we will consider it in future because now SEBI also has revised
its rules for doing the buyback through the market." The blocker named in April
is gone by July and the answer is still "will consider." Against roughly
Rs1,500cr of cash (Feb-2026, p.14). **MAJOR.**

**IF-15. "No additional costs," asserted flatly, in the call that prices the
same work for someone else.** Asked what the re-engineering to feed bids to
Grid India would cost, Goel: "We have our own software team. And I'm sure our
team will be able to do all these things... No additional costs" (Apr-2026,
p.15). Four pages earlier in the same call, on Grid India doing the mirror-image
build: "Grid India will have to create the infrastructure and software for this,
which will be additional costs" (Apr-2026, p.11). By July, Amit Kumar confirms
IEX must integrate: "Grid India will publish the APIs which all three exchanges
will have to integrate" (Jul-2026, p.34). **MAJOR.**

**IF-16. The CMD does not know the status of a regulator-forced divestment.**
Asked about the IGX IPO, Goel: "I think IGX IPO process is we have initiated the
process. So I'm not really fully aware about the exact status of that, but I
think it is progressing well" (Apr-2026, p.12). The deadline is hard: PNGRB
granted an extension "up to 31st of December 2026" (Apr-2026, p.11), a
twelve-month grant against the eighteen months requested (Nov-2025, p.11). IEX
is a forced seller of 22.3% of IGX into a fixed date. **MAJOR.**

**IF-17. Customer concentration disclosed once, at the very end, then
half-retracted.** Last question of a two-hour meet: top buyers "almost about
50-60 percent," top-10 sellers "could be about 40 percent"; then "And this
50-60 versus 40 has remained the same over the last few years. I can't say
that it has remained the same, but it is in that range" (Jul-2026, p.41). The
same answer volunteers churn — "these buyers and sellers are not same. So, one
season there are new set of buyers, another season those are not there at all"
— which cuts directly against the "18 years of customer loyalty" defence used
against coupling risk everywhere else. **MAJOR.**

**IF-18. Carbon timeline accelerates by about a year while the caveat that
sizes it is dropped.** Nov-2025 (p.13): "all this process will need another
one and a half, maybe one to one and a half year," with the caveat that
actually sizes the market — "If everybody is complying, then there's no
trading" (p.19). Feb-2026 (p.13): "FY '27 or '28." Jul-2026 (p.6): "we are
expecting carbon trading to start within this calendar year. In fact, BEE has
said that they want to start it by 1st of October 2026." The caveat never
reappears. Every other timeline in this corpus slipped; this one accelerated.
**MAJOR.**

**IF-19. ICX marketed on last year's growth in the same week its issuance
fell.** The Jul-2026 meet presents ICX as "You can see 200% growth that we have
registered last year" and "quite a promising segment going forward" (p.7-8).
The press release filed the day before states Q1FY27 issuance of 42.4 lakh
I-RECs "as compared to 44.4 lakh I-RECs in Q1FY'26" (press release, p.3) — a
YoY decline. The decline is never mentioned. **MAJOR.**

**IF-20. Management's own margin evidence undercuts the reassurance it is
offered for.** To argue coupling will not compress economics, Goel cites the
one segment where all three exchanges compete on level liquidity: "in the Term
Ahead Market... the share of all 3 exchanges is in that same range... Against
INR 0.04 (four paise), I think the margin is around (3.6 or 3.7 paisa)"
(Apr-2026, p.15). That is a 7.5-10% fee erosion in the contested segment,
produced as proof that contest does not erode fees. **MINOR** on its own
(the number itself is disclosed and useful), but the framing is the tell.

**IF-21. ROE claim not reconciled.** "ROE we are maintaining around 42% to 44%
ROE continuously over the last 4-5 years" (Jul-2026, p.27), stated beside a
net worth of "around Rs.1,400 crores" and consolidated PAT of "almost around
135 crore" for the quarter. No basis is given. **MINOR** on the transcript
alone; the arithmetic is stage 5's to compute.

### Tier 3 — Smaller, still worth the record

**IF-22. An outright refusal on the mitigation question.** Faisal Hawa asks
what technology changes IEX can make so it does not lose volume if coupling
happens; Goel: "I do not think on this call, it will be possible to elaborate
on those things" (Nov-2025, p.15). The question was answered properly only
nine months later, at the July analyst meet. **MINOR.**

**IF-23. The full-year results call ran without the JMD.** "Mr. Rohit Bajaj,
JMD and Mr. Amit Kumar, Head of Market Operations and Exchange Technology are
not available to join us today due to other official meetings" (Apr-2026,
p.3) — the FY26 results call, the one carrying the APTEL dismissal and the
CERC draft regulations. Both returned in July, and Amit Kumar had been
promoted to Executive Director by then, so this is a soft signal, not a
departure. **MINOR.**

**IF-24. Consolidated PAT presented additively across an associate.**
"We achieved Rs.493 crore of consolidated profit during the previous year...
IEX standalone was around 474 crores, IGX 42 crores and ICX though it's a small
beginning" (Jul-2026, p.27). 474 + 42 already exceeds 493, and IGX is a 47.3%
associate, equity-accounted. The presentation invites double counting. Also in
the same session: Goel gives FY26 revenue "Rs.747 crore" and Q1 "202.8 crore"
(p.5) against Harlalka's "around Rs. 745 crore" and "almost around Rs.201
crores" (p.27). **MINOR.**

### Tier 4 — Peer statements that contradict the main company

**IF-25. The loyalty defence is contradicted by the peer set.** Goel's
central defence is "Today you have NSE and BSE and in spite of that NSE has
retained the market share" (Jul-2026, p.35). BSE's own account of the same
rivalry is structural, not loyalty-based: cash-equity share "hovering around
7% to 8%... far away from what we wanted it to be," attributed to smart order
routing applications "still pending for more than six months at the other
exchange" (BSE Concall May 2026, p.16). CDSL claims loyalty in the middle of
a documented erosion — incremental demat share "peaked somewhere around 3Q FY
'25, when we had 93% market share... this quarter has come down to 82%," met
with "We've not been losing market" (CDSL Concall Nov 2025, p.9-10).
**MAJOR.**

**IF-26. An independent investor names IEX as the cautionary case.** At MCX's
May-2026 call, discussing a different company, Bharat Shah: "if you look at
IEX, the energy Exchange, out of the blue, the market coupling issue has come.
And that is very clearly derailed the situation because market price discovery
is the key function of an Exchange. And when that gets taken away... Exchange
becomes commoditized. And we are seeing how IEX is struggling with that issue."
He then uses the same NSE/BSE rivalry against the incumbency reading: BSE's
options share went from "just a shade above 0" to "almost about 37%, 38%" on
an incremental basis in "3, 3.5 years" (MCX Concall May 2026, p.13).
**MAJOR.**

---

## PART 2: COMPARISON TABLE

| # | My item | Verdict | Where the pipeline has it |
|---|---|---|---|
| IF-01 | Same-call coupling contradiction | **PARTIALLY CAUGHT** | B05 red_flags at MEDIUM; report 1C and 4D. Facts and anchors exact. Severity should be HIGH — this is the only sizing of the thesis's largest risk, and it is withdrawn in the same session |
| IF-02 | "Definitely go in our favour" falsified in 14 days | CAUGHT | B05 red_flags HIGH; promise row added this run |
| IF-03 | Fee realisation deflected 3 quarters | CAUGHT | B05 red_flags HIGH; repeated_evasions row |
| IF-04 | Price-war question evaded twice | CAUGHT | B05 red_flags HIGH; repeated_evasions row |
| IF-05 | REC excuse names the wrong side | CAUGHT | B05 red_flags HIGH. Mildly overstated, see F-09 |
| IF-06 | Market-share disclosure degrading | CAUGHT | B05 red_flags HIGH |
| IF-07 | RTM decelerating vs raised guidance | CAUGHT | B05 red_flags HIGH; promise row "missed" |
| IF-08 | DAM in outright decline | CAUGHT | B05 red_flags HIGH; trigger 2 |
| IF-09 | Q1FY27 breaks the growth mechanism in both regimes | **PARTIALLY CAUGHT** | B05 has the DAM decline, the August buy-bid detail, and 2D "no revisiting of the cheap-power thesis." It does not state that July IEX volume (+7.7%) grew **slower than national demand** (+10.9%), the first such month, nor that August's +61.7% buy bids against +15.0% cleared volume shows a sell-side cap. That is the direct falsification of the penetration thesis |
| IF-10 | Coal TAM inconsistent | CAUGHT | B05 red_flags MEDIUM; guidance rows carry all four figures |
| IF-11 | 2023 product cohort failed | **PARTIALLY CAUGHT** | B05 red_flags at LOW; report 2D. Should be MAJOR: it is the observed base rate for the pending-product optionality the bull case rests on |
| IF-12 | 11-month TAM sizing vs "not significant" | **PARTIALLY CAUGHT** | Both halves present (guidance row for 15-20 BU; timeline_slippages for the 2-year pendency and the quote). The contradiction between them is never drawn |
| IF-13 | Nov "no developments" vs Jul "four-month pilot"; own-simulation asserted as fact | **MISSED** | Absent from B05 entirely |
| IF-14 | Buyback stalled after blocker removed | CAUGHT | B05 promise row "missed" + timeline_slippages. The blocker-removal nuance is mine to add, not a separate finding |
| IF-15 | "No additional costs" asymmetry | CAUGHT | B05 guidance row states the asymmetry explicitly. Not promoted to red_flags — see F-05 |
| IF-16 | CMD unaware of IGX IPO status vs hard deadline | CAUGHT | B05 1A row, promise row, trigger 8 |
| IF-17 | Concentration disclosed last, half-retracted | CAUGHT | B05 red_flags MEDIUM; 3D carries the churn admission |
| IF-18 | Carbon timeline accelerating, caveat dropped | CAUGHT | B05 dropped_triggers + analyst_note |
| IF-19 | ICX sold on last year's growth as issuance falls | CAUGHT | B05 1A row quotes both figures |
| IF-20 | TAM margin evidence undercuts its own claim | **PARTIALLY CAUGHT** | The 3.6-3.7 paise number is captured and used as trigger 3's kill signal. The self-undercutting quality of using it as reassurance is not drawn; and the row was reclassified out of the missed-promise tally, which I accept on its own terms |
| IF-21 | ROE unreconciled | CAUGHT | B05 red_flags MEDIUM, tempered to both bases |
| IF-22 | Outright refusal on mitigation (Nov-2025) | **MISSED** | Absent; the adjacent price-war row is a different question |
| IF-23 | FY26 results call without the JMD | **MISSED** | Absent |
| IF-24 | 474+42 additive across an associate | **PARTIALLY CAUGHT** | The 747/745 and 202.8/201 pair is caught at MEDIUM; the additive PAT build is not |
| IF-25 | Peer set contradicts the loyalty defence | CAUGHT | B06 Q6, its single most consequential finding. Anchors verified exact |
| IF-26 | Investor names IEX as the cautionary case | CAUGHT | B06 2D and Q6. Anchor verified exact (MCX May 2026 p.13) |

**Tally: 17 CAUGHT, 6 PARTIALLY CAUGHT, 3 MISSED, of 26.**
**Strict acceptance rate 17/26 = 65%. Including partials, 23/26 = 88%.**

---

## PART 3: PIPELINE FLAGS I DID NOT INDEPENDENTLY FIND

| Pipeline flag | Assessment |
|---|---|
| Fee realisation 4.16 vs 4.33 paise/unit, computed from filed standalone revenue and volume (B05 HIGH) | **SUPPORTED.** I did not compute it, but the direction is corroborated independently: Q1FY27 consolidated revenue +10.1% against volume +15.9% (press release, p.2) |
| ROE 42-44% not reconciling; 36.3% closing, 39.4% average standalone (B05 MEDIUM) | **SUPPORTED**, and properly tempered. Both bases disclosed, the average-equity basis named as conventional |
| Non-operating share of consolidated PBT 23.4% FY26 to 29.8% Q1FY27 (B05 LOW) | **SUPPORTED** as a computation, with one internal tension, see F-08 |
| Apr-2026 CERC REC amendment framed as inventory-enhancing one quarter before sell bids collapsed | **SUPPORTED.** The Apr-2026 transcript (p.5) does frame source-based multipliers as "should help increase REC inventory going forward" alongside the captive-plant trading restriction, one quarter before -86.1% sell bids. Good catch — but it never reaches red_flags[], see F-05 |
| Two different revenue figures inside one presentation (B05 MEDIUM) | **SUPPORTED**, verified in transcript at Jul-2026 p.5 and p.27 |
| Green market deceleration undisclosed on the call (B05 MEDIUM) | **SUPPORTED**, verified: FY26 +23%, Q1FY27 +6.3%, June -1.2%, filed 03-Jul-2026 |
| B06 Q5, peers are LESS forthcoming on concentration than IEX (CONTRADICTED verdict) | **SUPPORTED.** CDSL's "We don't give any client-specific information" verified verbatim (CDSL Nov 2025, p.10) |
| B06 Q1, MCX's single quantified cause for yield compression | **SUPPORTED**, verified (MCX Aug 2026, p.12) |

**pipeline_flags_not_supported: none.** No flag in either artifact is
invented, and none rests on evidence I could not locate. This is the single
most important result in this audit and it is why the 65% must not be read as
a quality score.

---

## PART 4: PROMISE-DELIVERY SPOT CHECKS

Five checks. Did the earlier call actually contain the promise, and does the
later call or filing actually show that outcome?

**SC-1. Volume guidance 15-20%.** Promise present: Goel, "for the remaining
period also, we expect reasonably good growth. We should be able to maintain a
growth of 15% to 20%" (Nov-2025, p.9). Outcome present: "In the full year FY26,
electricity volumes touched 141 billion units, higher by 17%" (Apr-2026, p.5).
**CONFIRMED — direction correct.**

**SC-2. "Things will definitely go in our favour."** Promise present at
Feb-2026 p.8 (verified verbatim by grep, line 304). Outcome present at
Apr-2026 p.5: "APTEL mentioned that as market coupling cannot be implemented
without regulations, IEX is not an aggrieved party at this stage."
**CONFIRMED — direction correct.**

**SC-3. REC to end FY26 ahead of FY25.** Promise present: "by the end of the
year, we will be able to still do better than what we did last year"
(Feb-2026, p.9). Outcome present: "during the full year, a total of 187 lakh
RECs were traded, recording a 5% increase over the last year" (Apr-2026, p.5).
**CONFIRMED.** B05 scores this "partial"; on the letter of the promise it was
delivered. Marginally harsh grading, not an error.

**SC-4. IGX Q1FY27 flat.** Promise present: "my estimate is that maybe in the
first quarter, we may not get any growth with respect to the last year's first
quarter. But from second quarter onwards, we should be able to achieve growth"
(Apr-2026, p.10). Outcome present: "IGX traded gas volumes of 27.5 Million
MMBtu in Q1 FY'27, a growth of 11.9%... profit after tax of Rs. 16.3 Crore,
higher by 15.5%" (press release, p.2). **CONFIRMED — the guidance was beaten.**
This row is **absent from B05's promise table**, and its absence runs against
management, which is the opposite of the tally-flattering omission run 3
corrected. See F-07.

**SC-5. Treasury income recovery.** Promise present: "as the market is
recovering, we will see that the numbers going back to the earlier numbers"
(Apr-2026, p.10, verified marker page). Outcome as B05 reports it (Rs22.11cr to
Rs44.92cr standalone) is in the filed statements, not in my read set; the
consolidated picture in the press release is consistent with a recovery.
**CONFIRMED on the transcript half; not independently re-verified on the
statement half.**

**Checked 5, confirmed 5, wrong 0.** Every promise-delivery direction I tested
held. One row that should exist does not.

---

## PART 5: CITATION-ANCHOR AUDIT (the one systematic defect)

Stage 5's report states: "Every citation below was verified by grep against
the `=== PAGE n ===` marker in the extracted text before use," and lists three
specific run-2 anchors it corrected. I sampled roughly 35 of its anchors
against the marker index of each file. Roughly two-thirds are exact. The rest
drift by one to three marker pages, and two quotes are attributed to the wrong
call.

Correct (sample): Apr-2026 other-income p.10; Apr-2026 TAM margin p.15;
Apr-2026 Grid India cost p.11; Apr-2026 CMD-unaware p.12; Apr-2026 PNGRB p.11;
Feb-2026 market share p.16; Jul-2026 "20, 30, 40%" p.5; Jul-2026 "I don't see
any loss" p.35; Jul-2026 RTM 25-30% p.29; Jul-2026 REC "too early" p.41;
Jul-2026 API I-DAM p.23; Jul-2026 product failures p.12; Nov-2025 price-war
p.18; Nov-2025 market share p.17; Nov-2025 carbon caveat p.19.

Drifted (sample, with the true marker):
- Nov-2025 volume guidance 15-20%: cited p.6, true marker **p.9**
- Feb-2026 "definitely go in our favour": cited p.7, true marker **p.8**
- Feb-2026 REC buyout answer: cited p.8, true marker **p.9**
- Feb-2026 "variation in the yearly fees": cited p.9, true marker **p.10**
- Feb-2026 volume guidance: cited p.11, true marker **p.13**
- Apr-2026 volume guidance FY27: cited p.13, true marker **p.14**
- Apr-2026 coal 80mn tonnes: cited p.5-6, true marker **p.8**
- Jul-2026 "80-85% market share": cited p.6, true marker **p.7**
- Jul-2026 coal 120mn tonnes (first): cited p.5, true marker **p.6**
- Jul-2026 "70-80 million tonnes": cited p.7, true marker **p.8**
- Jul-2026 "at least 100 million ton": cited p.27, true marker **p.26**
- Jul-2026 FY26 revenue Rs747cr: cited p.4, true marker **p.5**
- Jul-2026 Grid India objections: cited p.18-20, true marker **p.21-22**
- Jul-2026 "18% vs 1%" growth claim: cited p.12, true marker **p.13**

Cross-call mis-attribution:
- "we had no expertise when we started... don't worry about that. So, we will
  do it here too" is attributed in 3C to **Q4FY26 p.12-13**. It is in the
  **Q1FY27** Analyst Meet, marker p.39. The Q4FY26 anchor is right for the coal
  logistics *question*, wrong for the quote given.
- "5,000+ industrial consumers" is attributed in 3D to **Q1FY27 p.17-18**. It
  is in the **Q4FY26** call, marker p.17.

Stage 6 shows the same drift on one transcript:
- MCX Aug 2026 "about 55%... market share standpoint": cited p.16, true
  marker **p.14**
- MCX Aug 2026 "8% to 10% of electricity needs... spot exchanges": cited p.17,
  true marker **p.14**
- MCX Aug 2026 "it's not a derivatives initiative at this point": cited p.6,
  true marker **p.10**
Stage 6's other sampled anchors are exact: MCX May 2026 p.13; MCX Feb 2026
p.18; CDSL Nov 2025 p.9-10; BSE May 2026 p.16; MCX Aug 2026 p.12.

**Every quote and every number I traced exists, in the file named, in the
substance claimed.** Nothing is fabricated. This is a precision defect and a
process-claim defect, not an evidence defect. It matters because a downstream
reader who follows a wrong anchor may conclude the quote is absent, and
because the report asserts a verification procedure it did not fully complete.

---

## PART 6: CREDIBILITY GRADE

**B05 grade: D (Poor). I concur, at the lower boundary of the range.**

Supporting D: two specific forward statements falsified within weeks (RTM
25-30%, "definitely go in our favour"); three quarters of unreconciled
realisation answers; a twice-evaded pricing question; a REC diagnosis that
inverts supply and demand against the company's own filing; market-share
disclosure precision falling as risk rises; a same-call self-contradiction on
the largest thesis risk; a coal TAM that carries four different figures.

Pulling the other way: headline volume guidance delivered in every period
shown, including FY26 at +17% and Q1FY27 at +15.9%; dividend delivered as
stated; one genuinely candid, specific, checkable admission on other income,
and its forward promise kept; IGX Q1 guidance beaten; and every figure
management gave that I could trace to a filing traced exactly (Rs747cr /
Rs202.8cr match the filed consolidated total income line). There is no
evidence of accounting manipulation anywhere in this corpus.

I would place this at D or a low C and would not disturb D. The distinction
that decides it is real: this management deflects and over-promotes, but it
does not misstate its numbers.

---

## PART 7: MATERIALITY READ

Would the residual gap change an investment decision? **No, with one
qualification.**

Of my 26 items, 3 are absent from the pipeline and 6 are present but placed
or weighted differently. Of the 3 absent, two (IF-22 the Nov-2025 refusal,
IF-23 the JMD absence) are texture, not thesis. The third (IF-13) is a real
finding but sits inside a risk the pipeline already flags at its highest
severity across seven separate rows; nothing about the coupling verdict moves
because of it.

The qualification is IF-09 and IF-11. IF-09 is the sharpest available test of
the growth thesis — July 2026 is the first month in the corpus where IEX
volume grew slower than national demand, and August shows cleared volume
capped by sell-side liquidity while buy bids ran +61.7%. The pipeline holds
every component fact and does not assemble them into that statement. IF-11 is
the observed base rate for IEX product launches (three of the 2023 cohort
failed for want of liquidity, admitted by management) and it is filed at LOW
when it is the cleanest discount on the pending-product optionality. Both are
about how much growth to underwrite, not about whether a red flag exists.
Stage 11 should be handed both explicitly.

Set against that: **zero pipeline flags are unsupported**, every load-bearing
monthly-filing number I re-derived matched exactly, and every promise-delivery
direction I tested held. The residual is overwhelmingly the residue of an
adversarial reader out-listing a single-pass stage after two rounds of
remediation have already stripped the easy findings. The one defect I would
insist on fixing before this record is cited downstream is the anchor drift in
Part 5, because the report claims a grep verification it did not complete, and
because two quotes are attributed to the wrong call.

---

## FINDINGS

| # | Severity | Location | Description |
|---|---|---|---|
| F-01 | MAJOR | B05 (missed) | IF-13. Nov-2025 p.8 "we are not aware about any developments" versus Jul-2026 p.20 "for the four months period they (Grid India) have run this pilot," plus IEX's own unpublished simulation asserted as established fact in support of a live Supreme Court petition. Absent from B05 |
| F-02 | MAJOR | B05 report 1D/2D, B05 red_flags | IF-09 partially caught. B05 holds the DAM decline, the +61.7% August buy bids and the "cheap power" observation but never states that July-2026 IEX volume (+7.7%) grew slower than national consumption (+10.9%), the first such month, nor that August's cleared volume was sell-side capped. This is the direct falsification of the 8%-to-25% penetration thesis (Jul-2026 p.13, p.33) |
| F-03 | MAJOR | B05 red_flags (LOW) | IF-11 under-weighted. Management's own admission that all three 2023 launches (HP-DAM, HP-TAM, Ancillary) failed for want of liquidity (Jul-2026 p.12) is the observed base rate for the three pending launches the growth case rests on. Filed at LOW; should be MAJOR |
| F-04 | MAJOR | B05 report/YAML | IF-12 connection not drawn. The 15-20 BU sizing for the 11-month TAM contract (Feb-2026 p.12) is contradicted by Goel's own "transactions in the contracts which are beyond three months, those are not significant" (Jul-2026 p.40). Both facts are recorded separately; neither row references the other |
| F-05 | MAJOR | B05 YAML red_flags[] | Two self-declared MAJOR findings never reach the handoff flag list and so will not reach stage 11 or 13: the Apr-2026 CERC REC-amendment framing (named MAJOR in B05's own rework_note, absent from red_flags[] and from report 4D) and the "No additional costs" asymmetry (report 1B only). A finding recorded in prose but omitted from red_flags[] is functionally missed downstream |
| F-06 | MAJOR | B05 report, ~1/3 of sampled anchors; B06, MCX Aug-2026 | Citation-anchor drift of one to three marker pages on roughly a third of sampled anchors, plus two cross-call quote mis-attributions (the "no expertise" quote is Q1FY27 p.39, cited as Q4FY26 p.12-13; "5,000+ industrial consumers" is Q4FY26 p.17, cited as Q1FY27 p.17-18). B05 asserts every citation was grep-verified against the marker index; that claim is not sustained. All substance verified correct — no fabrication. Full list in Part 5 |
| F-07 | MINOR | B05 promise_delivery | Missing row that favours management: Apr-2026 p.10 guided IGX Q1FY27 to "not get any growth"; actual was +11.9% volume and +15.5% PAT (press release p.2). Omitted from a 4/2/4 tally |
| F-08 | MINOR | B05 red_flags + promise_delivery | Internal tension: the CFO's treasury-income recovery is booked as a DELIVERED promise, while the rising non-operating share of PBT that recovery mechanically produces is booked as a red flag. They are the same event; neither row notes the other |
| F-09 | MINOR | B05 report 1D | Mild overstatement. "Four consecutive months of Power Market Updates before and after the call show an unbroken pattern of collapsing sell bids and rising clearing prices" — the Aug-2026 update reports no sell-bid figure, attributes the fall to "lower participation," and shows clearing prices of Rs370/Rs350, down from Rs400/Rs395 in June. The Q1FY27 and July filings do support the claim; August does not |
| F-10 | MINOR | B05 red_flags (MEDIUM) | IF-01 severity. The same-call coupling contradiction (Jul-2026 p.5 versus p.35) is the only sizing of the largest thesis risk anywhere in the corpus, given and withdrawn within one session. Filed at MEDIUM; should be HIGH |
| F-11 | MINOR | B05 (missed) | IF-22. Outright refusal on the coupling-mitigation question: "I do not think on this call, it will be possible to elaborate on those things" (Nov-2025 p.15). Distinct from the price-war evasion already tracked |
| F-12 | MINOR | B05 (missed) | IF-23. FY26 results call held without the JMD or the Head of Market Operations (Apr-2026 p.3), on the quarter carrying the APTEL dismissal and the CERC draft regulations. Soft signal; both returned in July |
| F-13 | MINOR | B05 red_flags (MEDIUM) | IF-24 half-caught. The 747/745 and 202.8/201 discrepancy is captured; the additive PAT presentation ("standalone was around 474 crores, IGX 42 crores" against Rs493cr consolidated, with IGX a 47.3% associate) is not |

**CRITICAL: 0. MAJOR: 6. MINOR: 7.**

No CRITICAL. The rubric's CRITICAL trigger is a missed repeated evasion across
2+ quarters. I tested for one: the pending-product-approval timeline is
deflected in Feb-2026 (p.12) and Jul-2026 (p.40), but B05 records that pattern
under `timeline_slippages` and in 1C rather than under `repeated_evasions[]` —
found and reclassified, not missed. All six evasion patterns I identified are
in B05's tracker.

---

## HANDOFF

```
stage: B12b
company: IEX
run_number: 3
post_remediation: true
independent_flags_found: 26
caught: 17
partially_caught: 6
missed: 3
pipeline_flags_not_supported: none
promise_delivery_spot_checks: checked 5, confirmed 5, wrong 0
credibility_grade_concur: concur with D, at the lower boundary
acceptance_rate: 65 (strict) / 88 (including partials)
```
