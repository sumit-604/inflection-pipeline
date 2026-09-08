# Stage 6 — Peer Concall Verification
Indian Energy Exchange Ltd (IEX) | Run date 2026-09-08 | Model: claude-sonnet-5

Peers: MCX (Multi Commodity Exchange), BSE Ltd, CDSL (Central Depository
Services). Four transcripts each, oldest first: Nov-2025, Feb-2026,
May-2026, Aug-2026 (12 transcripts total, all present and read in full via
targeted section reads plus corpus-wide grep passes for the four claim
topics and the unprompted cross-read).

Task: triangulate the four B05 `peer_questions[]` against what MCX, BSE and
CDSL actually told their own analysts across the same period. Peers have no
reason to support IEX's narrative, which is what makes them useful.

---

## PART 1: CLAIM-BY-CLAIM VERIFICATION

### Claim 1 — Regulator-driven market-structure change and fee-income impact

**Claim tested**: IEX's reassurance precedents (the TAM-market
margin-resilience analogy, ~7-10% compression under 4 years of 3-exchange
competition; and the one-off 20-40% DAM impact range) should be consistent
with how comparable market-infrastructure fee-compression episodes actually
played out at peers.

**Verdict: PARTIALLY VERIFIED**

**Peer evidence**:
- BSE underwent a genuine, dated, regulator-driven market-structure change
  in this exact window: the shift of BSE's weekly index-options expiry day
  to Thursday, described as "eight months" old as of the May-2026 call
  (BSE Concall May 2026 Transcript, p.18, Devesh Agarwal question). This is
  the closest peer analogue in the corpus to a regulator redesigning market
  structure around an exchange's core product.
- The REALISED outcome was expansionary, not compressive: BSE reported
  "seen the market share increase in the option derivative segment" (BSE
  Concall Nov 2025 Transcript, p.9, Mohit Mangal question) and a record
  average daily premium turnover of Rs. 19,523 crores in FY26 vs Rs. 8,978
  crores in FY25, +118% YoY, explicitly linked to "broadening of the
  liquidity profile" post-transition (BSE Concall May 2026 Transcript,
  p.5-6). The direction is the opposite of IEX's implicit worst case.
- No BSE call in this corpus gives a PRE-transition quantified impact
  estimate to set against the realised outcome — the transition predates
  the Nov-2025 opening of the corpus window. The specific "estimate given
  at the time vs. realised impact" comparison the question asks for is
  therefore not constructible from these transcripts.
- MCX was asked a directly parallel hypothetical (clearing-corporation
  interoperability between equities and commodities) and gave an
  unquantified reassurance: "Liquidity does not just go away due to
  interoperability... We have sticky liquidity" (MCX Concall May 2026
  Transcript, p.18, Rishi Nathany, answering Amit Chandra) — structurally
  identical in form to IEX's own defence, but the event has not happened,
  so there is no realised outcome to check it against.
- CDSL discloses no comparable regulator-driven fee-structure or
  market-design event in this corpus window (grepped for BSDA, fee caps,
  fee-waiver mandates: no matches).

**Peers silent**: CDSL entirely, on any realised market-structure/fee
event. MCX, on any REALISED (as opposed to hypothetical) coupling or
interoperability event.

**Net read**: the one real precedent in the peer set (BSE's expiry-day
reallocation) argues AGAINST the fear IEX is defending against — a
SEBI-driven market redesign expanded, rather than compressed, the affected
exchange's fee income and share. That complicates IEX's implicit worst-case
framing usefully, but it is not the same mechanism as market coupling (it
reallocated a scarce trading day between rival index-options products; it
did not force multiple exchanges to compete for a single unified order
book the way DAM coupling would). No peer offers the specific "estimate
then vs. outcome now" comparison the claim needs, so full verification is
not possible.

---

### Claim 2 — Non-operating income share of PBT/PAT and analyst attention

**Claim tested**: IEX's rising non-operating share of consolidated PBT
(23.4% FY26 to 29.8% Q1FY27), never raised by any analyst or by IEX
management on any call, is a sector-wide pattern among cash-rich,
no-promoter market-infrastructure names, not an IEX-specific disclosure
gap.

**Verdict: VERIFIED**

**Peer evidence** (three independent peers, same pattern):
- BSE: analysts ask repeatedly for the absolute rupee value and
  quarter-on-quarter driver of "other income," "investment income" and
  "treasury income" — e.g., Nov-2025 opening remarks disclose "Treasury
  income from clearing and settlement funds has decreased by 32% to
  Rs. 42 crores from Rs. 63 crores" (BSE Concall Nov 2025 Transcript, p.6);
  Aug-2026, Madhukar (JP Morgan) asks specifically why "other income has
  also picked up quite significantly" quarter on quarter (BSE Concall Aug
  2026 Transcript, p.17). In neither case, nor anywhere else in the four
  BSE transcripts, does an analyst ask what SHARE of PBT this line
  represents or whether that share is TRENDING up.
- CDSL: the pattern repeats across all four calls — Nov-2025 (Devish
  Agarwal, p.9, requests the eCAS/e-voting/investment-income breakup of a
  Rs. 59cr other-income line), Feb-2026 (similar breakdown requests),
  Aug-2026 (Hiral Parekh, p.6, asks for "a broad split across eCAS,
  e-voting, income from unlisted companies and pledge income and also any
  one-off... how much of this was driven by MTM gains"). Every question is
  about composition and quarter-on-quarter movement; none asks about the
  share of PBT/PAT this represents or its multi-quarter trend.
- MCX: Bunty Chawla (Aug-2026 call, p.16) asks about "a drastic growth"
  in other income sequentially and YoY and its drivers — again, magnitude
  and driver, not share-of-profit framing. Management's answer
  ("we've had extremely sharp growth in Q4... while it moderates, it
  consolidates") does not volunteer a share-of-PBT figure either.

**Peers silent**: no peer, across 12 transcripts, discloses or is asked
for the SHARE of PBT/PAT attributable to non-operating/treasury income, or
for its trend across quarters.

**Net read**: this is a real, corroborated finding, not an artefact of
IEX-specific inattention. Sell-side coverage of Indian market-infrastructure
names routinely interrogates the absolute size and quarterly driver of
"other income" lines but does not track the metric IEX's own rising share
(23.4% to 29.8% of PBT in three quarters) would call for: the SHARE of
bottom line coming from float/treasury rather than the core transaction-fee
engine. IEX's silence on this is real, but it sits inside a wider,
verified sector-wide blind spot rather than standing out as an IEX-specific
anomaly.

---

### Claim 3 — Associate stake sale / subsidiary IPO valuation disclosure practice

**Claim tested**: IEX's total silence on IGX OFS valuation and expected
proceeds — across the Jul-2026 call held ten days after the DRHP filing —
is standard market-infrastructure practice, or an IEX-specific gap.

**Verdict: UNVERIFIABLE**

**Peer evidence**: none. Neither BSE nor CDSL discloses, or is asked
about, an associate-entity stake sale, subsidiary IPO, or OFS with a
comparable valuation/proceeds dimension anywhere in these eight
transcripts. BSE names its associate/subsidiary businesses (India INX,
Hindustan Power Exchange (HPX), BSE E-Agricultural Markets (BEAM)) once, in
generic prepared-remarks language ("BSE is committed to these new areas...
working with partners," BSE Concall Nov 2025 Transcript, p.7) with no
valuation, stake-sale, or IPO event attached. The one adjacent topic — a
shareholder asking BSE to INCREASE its stake in the BSE EbiX Insurance
platform (BSE Concall Nov 2025 Transcript, p.15-16) — is the opposite
transaction type (a stake increase, not a sale) and produces no valuation
figure either way. CDSL discloses no comparable event for any subsidiary
(CDSL Ventures, Centrico Insurance Repository) in any of its four
transcripts.

**Peers silent**: both BSE and CDSL, entirely, on this specific topic.

**Net read**: the question cannot be answered from this peer set because
no analogous event occurred at either peer in this window. This is a gap
in the available precedent, not a finding about IEX's disclosure practice
either way. Do not read the absence of contrary peer evidence as
confirmation of IEX's practice; it is simply untestable here.

---

### Claim 4 — Customer stickiness / integration as a defence against share loss

**Claim tested**: Goel's NSE-vs-BSE analogy ("Today you have NSE and BSE
and in spite of that NSE has retained the market share") and the general
customer-loyalty defence are credible when checked against how such claims
held up for peers.

**Verdict: CONTRADICTED**

**Peer evidence**:
- CDSL is the cleanest, most direct test in the corpus. At the May-2026
  call, CEO Nehal Vora explicitly attributes CDSL's ~85%+ market share of
  new demat-account openings to "the commitment and loyalty towards CDSL
  platform" (CDSL Concall May 2026 Transcript, p.7) and separately calls
  "the loyalty, which we continue to enjoy, the commitment we continue to
  enjoy [and] the market share of new account openings we continue to
  enjoy" an "intangible" moat (same call, p.9-10). At the VERY NEXT call
  (Aug-2026), an analyst discloses that CDSL's own incremental demat
  market share had DROPPED 420 basis points since March, to 81.4% in
  June-2026, attributed by name to a competitor's reduced onboarding
  friction from tech changes aimed at fintech brokers (CDSL Concall Aug
  2026 Transcript, p.6, Hiral Parekh). Management's response does not
  quantify or rebut the erosion; it repeats the same value-proposition
  language used to make the original loyalty claim ("we are an
  infrastructure company... not a quarter-on-quarter growth [story]," same
  page). This is a real, within-corpus, one-quarter-later contradiction of
  a stickiness claim by the same company that made it. A softer, earlier
  version of the same erosion was already visible and downplayed at the
  Feb-2026 call: "the incremental market share has dropped... there has
  been no significant drop as I would see it as of now" (CDSL Concall Feb
  2026 Transcript, p.10, Nehal Vora, answering Sanketh Godha) — a
  reassurance not defended six months later, structurally similar to
  IEX's own recycled REC-market excuse pattern flagged in Stage 5.
- BSE's own account of its cash-equity market share complicates, rather
  than confirms, the "incumbent retains loyalty" reading Goel invokes.
  BSE's CEO states cash-equity market share "has been hovering around 7%
  to 8% compared to 5% to 6% when I joined... far away from what we
  wanted it to be," and attributes the stagnation NOT to customers
  favouring the incumbent out of loyalty but to a structural, unresolved
  regulatory bottleneck: smart order routing applications "pending for
  more than six months at the other exchange," which keeps clients from
  being "exchange agnostic" (BSE Concall May 2026 Transcript, p.16,
  answering Satyam Chaurasiya). An earlier call had described the same
  initiative more optimistically ("early signs are positive... share of
  BSE volumes rising," BSE Concall Nov 2025 Transcript, p.7) — another
  instance of an early positive claim not holding up over two quarters.
  BSE's own explanation for NSE's durable lead is regulatory/
  infrastructural friction, not customer loyalty — a materially different
  mechanism from the one Goel's analogy implies.
- A genuinely independent, third-party data point complicates Goel's
  analogy further. At the MCX May-2026 call, investor Bharat Shah invokes
  IEX BY NAME as a cautionary precedent and then cites the OPTIONS segment
  of the same NSE-vs-BSE relationship Goel uses, with the opposite lesson:
  "the share of BSE was next to nothing... today, in about 3, 3.5 years,
  it has climbed to, on an incremental basis, to almost about 37%, 38%...
  that kind of a change is truly a dramatic one" (MCX Concall May 2026
  Transcript, p.13). Selecting the CASH segment supports "incumbents keep
  their lead"; selecting the OPTIONS segment of the identical rivalry
  supports "dramatic share reallocation happens." Goel's analogy is true
  for one segment and false for the other of the very comparison he
  invokes, which weakens its use as a general reassurance.
- MCX itself makes an unquantified "moat" claim of its own, of the same
  rhetorical shape as Goel's, in response to a live competitive threat
  ("some competitive actions on sort of expiry date change... we are
  reviewing the impact... technological progress and the moat that we
  have would be a key enabler to protect your market share" — MCX Concall
  Aug 2026 Transcript, p.18-19). This is the final call in the MCX series
  in this corpus, so there is no later data to test it against; it is
  presented here as a same-pattern peer claim, not as further evidence
  either way.

**Peers silent**: none of the three peers is silent on this topic; all
three make some form of stickiness or moat claim in this window.

**Net read**: the single cleanest test available (CDSL, claim then
data one quarter later) falsifies the "loyalty protects share" framing in
its own words. The BSE and MCX evidence complicates rather than confirms
Goel's specific NSE-vs-BSE analogy: it is segment-selective, and where
BSE's management explains its own stuck segment, the explanation is
regulatory/infrastructural friction, not customer stickiness. Taken
together, the peer set does not support using "18 years of customer
loyalty" as a load-bearing defence against a genuine market-structure
change; it is the single largest complication the peer set adds to IEX's
narrative.

---

## PART 2: UNPROMPTED CROSS-READ

### 2A Demand environment
All three peers report a strongly positive demand backdrop across the same
Nov-2025 to Aug-2026 window: BSE's operational revenue +44% to +63% YoY
across quarters, "12th/13th consecutive quarter" of record top and bottom
line (BSE Concall May 2026 Transcript, p.16); CDSL's demat accounts
reaching "18.01 crore" with continued account-opening growth (CDSL
Concall May 2026 Transcript, p.4); MCX's ADT and profit growing ~29-32%
YoY in the earliest call in the set (MCX Concall Nov 2025 Transcript,
p.4) and describing FY26 as "a strong year" (MCX Concall May 2026
Transcript, p.5). This is a consensus positive-demand read across the peer
set for the same period IEX's own volume growth ran below its 15-20%
guidance band in June (+12.5%) and July (+7.7%) 2026. Against a broadly
buoyant peer backdrop, IEX's specific monthly misses read somewhat more
company/segment-specific (REC, DAM-mix related) than macro-driven —
worth weighing against Stage 5's "weather" explanation for the same
misses.

### 2B Pricing and input costs
BSE explicitly documents margin compression driven by volatility swings —
"the receipt of premium by us... is a function of multiple things,
including volatility... making the premium realization per contract
different... thus compressing the margins... these events, being
uncontrollable and unpredictable" (BSE Concall Nov 2025 Transcript, p.11).
The same unpredictability shows up in "other income"/treasury income at
all three peers (BSE treasury income -32% QoQ tied to fund yields; CDSL
other income swinging on mark-to-market; MCX flagging "drastic growth" in
other income tied to "macro environmental factors"). This is a genuine,
sector-wide pattern of volatile, weather-like non-core income that
resembles IEX's own rising-and-volatile non-operating income line — it
does not, on its own, validate or invalidate IEX's specific 23.4%-to-29.8%
TREND, since no peer discloses the equivalent trend figure (see Claim 2),
but it does show the underlying mechanism (float/treasury income tied to
market volatility) is structurally common to the whole market-
infrastructure peer group, not an IEX quirk.

### 2C Capex cycle
All three peers are expanding capex and technology spend simultaneously —
this is an industry-wide capacity race, not a lone expander. BSE: ~Rs. 300
crore-plus capital work in progress over six months (BSE Concall Nov 2025
Transcript, p.13-14) plus explicit technology-expense growth "in a healthy
fashion" (BSE Concall Aug 2026 Transcript, p.17). CDSL: technology cost
"4x over the last 3 years," now exceeding employee cost on a consolidated
basis (CDSL Concall May 2026 Transcript, p.11). MCX: continued investment
in new products, member/FPI onboarding and risk systems across all four
calls, with management naming "operational risk" management itself as "a
hidden lever" requiring continuous investment (MCX Concall May 2026
Transcript, p.13). None of the three signals a maturing, cost-cutting
posture; all three read as still building out capacity and defensive
technology moats against a rising competitive-intensity backdrop.

### 2D Competitive mentions
IEX is named directly, twice, by MCX-side participants (not MCX
management itself):
- MCX Concall Feb 2026 Transcript, p.18 — investor Parikshit Gupta: "We
  all know what is happening with IEX, although we are governed by a
  different regulatory body. But do you anticipate any similar risks..."
- MCX Concall May 2026 Transcript, p.13 — investor Bharat Shah: "if you
  look at IEX, the energy Exchange, out of the blue, the market coupling
  issue has come. And that is very clearly derailed the situation...
  we are seeing how IEX is struggling with that issue." (Full quote and
  its use against the NSE-vs-BSE analogy is under Claim 4 above.)
- BSE Concall May 2026 Transcript, p.19 — investor Rushabh Doshi
  compares BSE's payout ratio unfavourably to "other exchanges, let's say
  like IEX or NSE" (a minor, payout-policy-only mention).

These are high-value because they are unprompted, third-party (buy-side)
observations from OUTSIDE IEX's own investor base, made while discussing a
different company entirely. They corroborate that IEX's market coupling
exposure is viewed externally as a serious, "derailed the situation"
level risk, not an overblown worry confined to IEX's own skeptics — a
finding that CONFIRMS the severity Stage 5 already flagged, from an
independent source.

### 2E Risks peers discuss that IEX does not
- SEBI restructuring its own internal commodity-derivatives oversight
  ("independent teams within MRD... work on the commodity segment") with
  an uncertain effect on MCX's "open" regulatory items (position limits,
  co-location) (MCX Concall Aug 2026 Transcript, p.19). IEX's own
  regulatory-engagement cadence with CERC is well covered in Stage 5; a
  parallel account of SEBI's internal reorganisation and its effect on
  open items has no IEX-side equivalent in this corpus.
- RBI regulation on bank-guarantee funding of clearing-corporation margin
  money, with an acknowledged, not-yet-fully-realised impact ("we cannot
  be drawing solace from the fact there has not been much of a visible
  impact at this point of time... some of the bank guarantees may mature
  and may not get re-issued," BSE Concall Aug 2026 Transcript, p.16-17;
  also raised at MCX Concall May 2026 Transcript, p.18). IEX's own
  filings in this corpus disclose no equivalent funding-structure
  regulatory risk.
- CDSL's fintech-onboarding-friction competitive erosion, quantified in
  real time (420bps incremental share loss, CDSL Concall Aug 2026
  Transcript, p.6) — a live, numbered competitive-erosion metric of a
  kind IEX does not disclose for its own DAM/TAM monthly share by
  competitor.
- BSE's core-SGF (Settlement Guarantee Fund) contribution policy, flagged
  by management itself as a source of "sudden spurts... having sudden
  impact on the quarterly earnings" that a new 5%-of-revenue policy is
  designed to smooth (BSE Concall Nov 2025 Transcript, p.10-11). IEX's
  corpus in this run does not describe an equivalent settlement-guarantee
  capital-buffer mechanic.

---

## PART 3: PEER COVERAGE MAP

| Peer | Quarter | Used how | Key contribution |
|---|---|---|---|
| MCX | Q2 FY26 (Nov 2025) | CITED-ONLY | Transaction-charge/float-income bookkeeping only; establishes baseline, decided no Part 1/2 finding on its own |
| MCX | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Investor names IEX directly re: market coupling as a monopoly-risk precedent (2D) |
| MCX | Q4 FY26 (May 2026) | SUBSTANTIVE | "Sticky liquidity" interoperability defence (Claim 1); Bharat Shah's IEX-named, BSE-options counter-precedent to the NSE-vs-BSE analogy (Claim 4, 2D) |
| MCX | Q1 FY27 (Aug 2026) | SUBSTANTIVE | "Moat" claim against competitive expiry-date actions (Claim 4); other-income growth question (Claim 2); SEBI commodity-department restructuring (2E) |
| BSE | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Treasury income decline disclosure (Claim 2); lot-size/same-day-expiry competitive question (Claim 1 context); SGF policy volatility (2E); early optimistic smart-order-routing read (Claim 4 arc) |
| BSE | Q3 FY26 (Feb 2026) | CITED-ONLY | Clearing-corp market-share convergence discussion; general context, not decisive to any Part 1 verdict |
| BSE | Q4 FY26 (May 2026) | SUBSTANTIVE | Thursday-expiry-day transition and its expansionary outcome (Claim 1); cash-equity market-share stagnation and its structural (not loyalty) explanation (Claim 4) |
| BSE | Q1 FY27 (Aug 2026) | SUBSTANTIVE | Other-income/technology-expense bookkeeping pattern (Claim 2); bank-guarantee/RBI regulation uncertainty (2E) |
| CDSL | Q2 FY26 (Nov 2025) | CITED-ONLY | Other-income line-item breakdown; bookkeeping only |
| CDSL | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Early, downplayed incremental market-share softness — the first leg of the Claim 4 arc |
| CDSL | Q4 FY26 (May 2026) | SUBSTANTIVE | Explicit "loyalty"/"commitment" claim underpinning ~85%+ new-account market share (Claim 4, foundational) |
| CDSL | Q1 FY27 (Aug 2026) | SUBSTANTIVE | Confirmed 420bps incremental market-share erosion, directly contradicting the prior quarter's loyalty claim (Claim 4); other-income breakdown (Claim 2) |

8 SUBSTANTIVE, 4 CITED-ONLY, 0 UNUSED. Every transcript in the corpus was
read and contributed at least a citation; no peer file was ignored.

---

## PART 4: TRIANGULATION SUMMARY

- Claims verified: 1 of 4 (Claim 2, fully). 1 partially verified (Claim 1).
  1 contradicted (Claim 4). 1 unverifiable (Claim 3, no comparable peer
  event exists in this corpus).
- Claims contradicted: 1 (Claim 4 — the customer-stickiness/NSE-vs-BSE
  defence). Priority item for synthesis.
- **Single most consequential contradiction**: CDSL's own May-2026
  "loyalty" claim for its ~85%+ new-account market share was followed, one
  quarter later, by a disclosed 420bps incremental-share loss to a
  fintech-onboarding competitor, with management's response repeating the
  same unquantified value-proposition language rather than engaging the
  number. This is a close structural match to IEX's own "18 years of
  customer loyalty" defence of its DAM incumbency, and it did not hold up
  for a same-mechanism peer within one quarter.
- **Single strongest independent confirmation**: two separate MCX-side
  investors, discussing a different company on a different call, name IEX
  directly and independently characterise its market coupling exposure as
  a severe, "derailed the situation" level risk — external corroboration,
  from outside IEX's own investor base, that Stage 5's top red flag is
  taken seriously by market participants who watch adjacent exchanges.
- **Overall**: the peer set complicates IEX's narrative more than it
  supports or cleanly undercuts it. It VERIFIES that IEX's silence on the
  rising non-operating share of profit sits inside a genuine, sector-wide
  analyst blind spot, not an IEX-specific failure. It CONTRADICTS, or at
  minimum badly complicates, the customer-loyalty defence Goel leans on
  most heavily, using a same-mechanism peer (CDSL) whose identical claim
  did not survive one quarter, and an independent third party's counter-
  reading of the very NSE-vs-BSE precedent Goel invokes. It leaves the
  IGX-OFS-silence question genuinely untestable (no comparable peer event
  exists), and it complicates rather than confirms the market-coupling
  fee-compression fear, since the one real peer precedent for a
  regulator-driven market redesign (BSE's expiry-day reallocation) had an
  expansionary, not compressive, outcome — though it is not the same
  mechanism as coupling and should not be read as a reassurance either.

---

## PART 5: CROSS-PEER HYPOTHESIS

No single peer states this, but the pattern across all three is visible
only when the calls are read together: BSE, CDSL and MCX each carry a
material, quarter-volatile "other income"/treasury income line (BSE
treasury income -32% QoQ in one call; CDSL other income swinging sharply
on mark-to-market gains/losses; MCX flagging "drastic growth" in other
income tied to "macro environmental factors"), and across all 12
transcripts, every analyst question on this line asks for its absolute
size or its quarter-on-quarter driver — never for its SHARE of PBT/PAT or
its multi-quarter TREND. This is not one company's disclosure gap; it
recurs identically at three separate, unrelated regulated
market-infrastructure businesses covered by three different analyst
communities.

**Hypothesis**: Indian market-infrastructure names — cash-rich,
low-marginal-cost, holding large client margin money and settlement
guarantee funds as a structural byproduct of their core license — generate
a treasury/float income stream that mechanically grows alongside AUM,
margin balances and settlement volumes, largely independent of the core
transaction-fee growth story the sell-side actually underwrites these
stocks on. Because this income is framed by management (and accepted by
analysts) as a "bonus" on top of the "clean" operating thesis rather than
as a distinct earnings-quality variable, NEITHER side tracks its growing
SHARE of the bottom line as a quality-of-earnings signal, even though the
mechanism (float on a compounding balance) means that share should
structurally drift upward over time for any of these four names, not just
IEX.

**Testable**: track each peer's (other income + treasury/investment
income + share of associate profit) as a percentage of consolidated PBT
over the next 4-6 quarters, alongside IEX's own trend. If the hypothesis
holds, BSE's and CDSL's non-operating shares should also drift upward over
multi-quarter windows even where volume/transaction-fee growth is healthy,
and it should continue to go unasked on their calls until a name's
absolute rupee move gets large enough (as at IEX, Rs.151cr to Rs.53cr in a
single quarter) to force the question.

---
