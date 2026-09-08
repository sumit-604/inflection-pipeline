# Stage 6 — Peer Concall Verification
Indian Energy Exchange Ltd (IEX) | Run date 2026-09-08 | RUN 2 (RE-POINTING) | Model: claude-sonnet-5

## Rework note
This is a re-pointing run, not a quality rework. Run 1's four claim
verdicts were sound work against Stage 5 run 1's peer_questions. Stage 5
was independently reworked since (run 2, credibility grade C reproduced
from a fuller reading), and its `peer_questions[]` list changed to six
different questions. Run 1's four verdicts are carried forward intact
below, and this run additionally answers all six of the CURRENT
`B05-concall.yaml` peer_questions from a fresh read of the same twelve
transcripts. Two coverage-map corrections identified by an audit of run 1
are folded in: CDSL's Nov-2025 transcript already carries an incremental
demat-share decline (93% to 82%) one quarter earlier than run 1 credited,
and BSE's Feb-2026 transcript already carries the smart-order-routing
bottleneck explanation run 1 dated only from May-2026. Both transcripts
move from CITED-ONLY to SUBSTANTIVE. Run 1's Part 3 summary line (which
read "8 substantive / 4 cited-only" against a table that itself listed 9
and 3) is corrected.

Peers: MCX (Multi Commodity Exchange), BSE Ltd, CDSL (Central Depository
Services). Four transcripts each, oldest first: Nov-2025, Feb-2026,
May-2026, Aug-2026 (12 transcripts total, all re-read in full this run via
targeted section reads plus corpus-wide grep passes for all six current
claim topics, the four carried-forward topics, and the unprompted
cross-read).

Page citations use the `=== PAGE n ===` marker number in each transcript
file, per task instruction, not the printed page footer.

---

## PART 1: CLAIM-BY-CLAIM VERIFICATION — CURRENT SIX QUESTIONS

### Q1 — Fee realisation trailing volume/activity growth, sector-wide?

**Claim tested**: IEX's revenue growth trails its volume growth in every
period on record; realisation fell from 4.33 to 4.16 paise/unit between
Q1FY26 and Q1FY27; management gave three different, unreconciled
explanations across three quarters. Do MCX, BSE and CDSL show the same
pattern, and is the CAUSE they give external/named or internal/unquantified?
Do they quantify net realisation after discounts, or refuse to?

**Verdict: PARTIALLY VERIFIED**

**Peer evidence**:
- The TOPIC is genuinely sector-wide: all three peers face direct analyst
  questions in this window about realisation, yield or margin compression.
- MCX gives the most rigorous single answer found anywhere in the corpus.
  Asked to decompose a "68% yield compression" in Bullion Options (premium
  to notional falling from 1.03% to 0.35%) across four named candidate
  causes, management attributes it to ONE, quantified, external cause
  (volatility normalisation: "predominantly, it is a market factor...
  heightened volatility... has lowered... that is what actually
  contributed to this decline in the premium ratio," Praveen DG) and
  EXPLICITLY RULES OUT the two alternative mix-driven explanations by
  comparing premium levels ("almost at the same level... not significantly
  contributing") and open interest, which "remained stable" (MCX Concall
  Aug 2026 Transcript, p.11-12, Shrenik Mehta question, Praveena
  Rai/Praveen DG/Shivanshu Mehta answer). One cause, quantified, named,
  internally consistent within the same answer.
- BSE names a single external cause (volatility swings between quarters
  affecting "premium realization per contract," "compressing the
  margins") but does NOT quantify the compression itself or reconcile it
  to a number, and states plainly that "no future trend in this regard
  could be predicted" (BSE Concall Nov 2025 Transcript, p.10-11, S.
  Ramamurthy answering Amit Chandra). Named cause, unquantified, but a
  SINGLE consistent cause, not three different ones.
- CDSL's realisation pressure in this window is REGULATORY, not organic:
  SEBI-mandated KYC/KRA fee cuts (fetch charge Rs.35 to Rs.28, -20%;
  creation charge Rs.20 to Rs.5, -75%), named, quantified, and explicitly
  framed as "industry-wide... everybody has reduced their charges
  accordingly" (CDSL Concall Aug 2026 Transcript, p.7-8, Sunil Alvares).
  But asked the ONE question in this whole corpus that most directly
  mirrors what IEX was asked — whether the REALISABLE rate net of client
  discounts has fallen by the same quantum as the headline rate cut — CDSL
  refuses outright: "We do not discuss this in our investor calls" (same
  transcript, p.8, Sunil Alvares answering Swarnabh Mukherjee).

**Peers silent**: none, on the general topic. All three took a direct
realisation/margin-compression question in this window.

**Net read**: the PHENOMENON (analysts pressing exchanges on realisation
or margin compression) is sector-wide, confirming this part of the
question. IEX's specific FAILURE MODE — three different, unquantified,
mutually inconsistent internal explanations recycled across three
consecutive quarters, never bridged to a number — is not matched by any
peer. MCX is more rigorous (one quantified cause, alternatives tested and
ruled out in the same answer). BSE is less rigorous but still gives one
consistent named cause, not three shifting ones. CDSL is the most opaque
of all three, and its opacity is not "peers explain this too, imperfectly"
but a flat, quotable refusal to discuss net realisation after discounts —
the single closest peer analogue to IEX's own unresolved question, and it
resolves to silence rather than an answer, on either side. Partial, not
full, verification: the topic is sector-wide, the specific evasion pattern
is not.

---

### Q2 — MCX electricity derivatives vs. IEX's 18% power-exchange growth / 1% demand growth claim

**Claim tested**: IEX states power exchanges collectively grew 18% in FY26
against demand growth of just 1%. Does MCX's electricity derivatives
commentary corroborate this?

**Verdict: UNVERIFIABLE** (for the growth-rate claim itself)

**Peer evidence**: MCX's electricity derivatives segment is a financial
derivatives product settled against exchange (largely IEX) clearing
prices, structurally distinct from the spot DAM/RTM volumes the 18%/1%
claim describes. Across all four MCX transcripts, MCX discusses ITS OWN
electricity-futures ADT, open interest and market share against NSE
(reaching "about 55%... from a market share standpoint," MCX Concall Aug
2026 Transcript, p.16) but never once states or corroborates a
sector-wide power-EXCHANGE (spot) volume growth rate or a national power
DEMAND growth rate for FY26. No MCX transcript in this corpus addresses
the specific 18%-vs-1% comparison at all.
One ADJACENT, partial corroboration exists, of a different figure: MCX's
CFO/MD states "about 8% to 10% of electricity needs on a day-to-day basis
are really transacted through the spot exchanges" (MCX Concall Aug 2026
Transcript, p.17, Praveena Rai, answering Parikshit Gupta) — an
independent, unprompted figure that lands inside IEX's own stated CURRENT
baseline of "8-9% today" (B05 Q1FY27 p.32). This corroborates the STARTING
POINT of IEX's TAM claim (see Q3 below), not the 18%/1% GROWTH-RATE claim
this question asks about.

**Peers silent**: MCX, on the specific FY26 growth-rate comparison.

**Net read**: cannot be verified from MCX's commentary; MCX's electricity
business is the wrong instrument to test a spot-market growth-rate claim,
and MCX never states the figure either way. The one number MCX does give
(8-10% spot-exchange penetration of electricity needs) is a useful,
independent cross-check of IEX's CURRENT-STATE baseline, not of its growth
claim, and should not be read as validating the 18%/1% figure.

---

### Q3 — Long-dated addressable-market claims: sector-standard framing or IEX overreach?

**Claim tested**: IEX claims exchange volume reaches ~25% of national
generation from 8-9% today, over 5-6 years. Do BSE, CDSL or MCX make
comparably long-dated, quantified TAM claims for their own core segments,
and how have prior such claims held up?

**Verdict: UNVERIFIABLE** (no comparable peer claim exists to test)

**Peer evidence**: Across all twelve transcripts, none of BSE, CDSL or MCX
makes a claim of the same SHAPE as IEX's — a specific current percentage,
a specific target percentage, a specific multi-year horizon, anchored to a
named international comparator. What each peer offers instead:
- BSE's growth framing is retrospective and record-setting ("11th/12th/
  13th consecutive quarter" of records; market cap "5,000 crores when I
  joined... today... around 1.56 lakh crores," BSE Concall May 2026
  Transcript, p.19) or qualitative-aspirational ("a long way to go
  further," BSE Concall May 2026 Transcript, p.15) — never a numbered,
  dated forward target for a core segment's addressable share.
- CDSL frames growth as deliberately NOT quarter-bound ("we are an
  infrastructure company... not a quarter-on-quarter growth [story]... It
  is a long-term sustainable growth," CDSL Concall Aug 2026 Transcript,
  p.6) with no forward percentage or year attached.
- MCX's coal-exchange commentary is the closest analogue in SUBJECT (a new
  segment, framed as a large future opportunity) but gives NO market-size
  number, quantified or otherwise, in any of the four transcripts (see Q4
  below) — language stays at "a lot of opportunity for structuring,
  consolidation, common platform pan-India" (MCX Concall May 2026
  Transcript, p.17) and "transparent, efficient technology-driven national
  coal trading ecosystem" (MCX Concall Aug 2026 Transcript, p.6).

**Peers silent**: all three, on a comparably specific long-dated,
quantified TAM claim for their own core segment.

**Net read**: the absence itself is the finding. IEX's ~25%-of-generation-
in-5-6-years framing, pinned to a specific percentage, a specific horizon
and a named comparator (European exchanges), is NOT the sector-standard
investor-relations style among these three peers in this corpus; none of
them puts a comparably specific number-and-date claim on the record for
its own core business, so there is no prior claim of this shape at any
peer whose track record could be checked. This should be read as
IEX-specific framing, not sector convention, though it is a finding by
absence rather than a tested and failed precedent.

---

### Q4 — MCX's own coal-exchange opportunity sizing, consistency check

**Claim tested**: IEX's coal-exchange opportunity moved from ~80 million
tonnes to ~120 million tonnes within six months, unbridged. Has MCX, which
has also filed for a coal-market play, sized the same opportunity
consistently?

**Verdict: UNVERIFIABLE** (MCX gives no size figure to be consistent or inconsistent with)

**Peer evidence**: grepped across all four MCX transcripts for any
tonnage, rupee, or other market-size figure attached to MCX's coal
exchange: none found. MCX's coal commentary across the full period:
- May-2026: coal exchange described as an independent subsidiary entity
  requiring SEBI approval, "a lot of opportunity for structuring,
  consolidation, common platform pan-India and so on" (MCX Concall May
  2026 Transcript, p.17) — no number.
- Aug-2026: "MCX Coal Exchange of India" incorporated, described as
  creating "a transparent, efficient technology-driven national coal
  trading ecosystem" (MCX Concall Aug 2026 Transcript, p.6) — no number.
  Elsewhere in the same call, management explicitly distinguishes the coal
  exchange from a derivatives product ("it's not a derivatives initiative
  at this point. It's a coal exchange," p.6) but again attaches no size
  figure to it.

**Peers silent**: MCX gives no market-size figure for coal in any of the
four transcripts, so there is nothing to compare IEX's 80mn/120mn/70-80mn
figures against.

**Net read**: cannot be verified either way; MCX has not sized the
opportunity at all, so "consistently" cannot be assessed. Worth noting as
a contrast in KIND, not degree: MCX's posture across two full quarters of
an incorporated coal-exchange subsidiary is to give qualitative framing
and withhold any number, where IEX gave a number early and then moved it
~50% without a bridge. Silence is a different failure mode from an
unreconciled revision, and this run does not treat MCX's silence as either
more or less credible than IEX's practice — only as offering no
independent sizing to check IEX's figures against.

---

### Q5 — Customer/counterparty concentration: do peers disclose more proactively?

**Claim tested**: IEX disclosed 50-60% buyer concentration and ~40%
top-ten seller concentration only at the final question of a two-hour
analyst meet, never on a quarterly call. Do BSE, CDSL or MCX disclose
comparable concentration metrics more proactively, and how does their
concentration compare?

**Verdict: CONTRADICTED** (peers are LESS forthcoming than IEX, not more)

**Peer evidence**:
- CDSL refuses concentration disclosure explicitly, twice, in different
  quarters and different framings. Asked directly whether any of its top
  20 new-account-opening clients had begun splitting business with the
  rival depository, CDSL's CEO answers: "We don't give any client-specific
  information" (CDSL Concall Nov 2025 Transcript, p.10, Nehal Vora
  answering Devish Agarwal). Asked in a later quarter for a size/quantum
  on a specific revenue-driving relationship (Search API), CDSL again
  declines to give the number (CDSL Concall Aug 2026 Transcript, p.8).
- MCX, asked directly how many of NSE's reported top-10 brokers by active
  clients also participate on MCX, declines to name any: "I cannot name
  any specific member by name" — and when the analyst reduces the ask to
  a bare count ("Like 3, 4, 7, 8, not the names, just the number"),
  management gives only a vague qualitative confirmation, "More or less,
  it would be similar" (MCX Concall Nov 2025 Transcript, p.16-17, Rishi
  Nathany answering Devesh Agarwal) — no actual percentage or count.
- BSE: grepped across all four transcripts for any member, broker or
  client concentration figure (revenue or volume share attributable to
  top members/clients); none found. BSE is silent on this topic entirely
  in this corpus, neither disclosing nor being asked for a concentration
  metric.

**Peers silent**: BSE entirely; CDSL and MCX are not silent but actively
decline to quantify when asked directly.

**Net read**: the question's implicit premise — that peers might be more
proactive on concentration disclosure than IEX's reactive, last-question
pattern — is CONTRADICTED by the evidence. IEX, however late and
reluctant, DID eventually give real percentages (50-60% buyer, ~40%
top-10 seller) when pressed. CDSL and MCX, asked comparably direct
questions, gave flat refusals or vague non-answers with no number at all,
in every instance found across eight transcripts. BSE never faced the
question and never volunteered a figure. On the narrow test of "does a
number eventually appear on the record," IEX's practice is not the
sector's worst; it is arguably the only one of the four names in this
comparison set that actually produced a quantified concentration figure
anywhere in this corpus.

---

### Q6 — BSE's own market-share record vs. NSE, testing the IEX analogy

**Claim tested**: IEX repeatedly invokes "NSE has retained the market
share" despite BSE's existence, to argue coupling will not erode its own
position. Does BSE's own concall record address its market-share
trajectory against NSE in a way that tests this analogy? [Carries forward
and strengthens run 1's Claim 4, which covered the same underlying
question against IEX's original phrasing of it.]

**Verdict: CONTRADICTED**

**Peer evidence**:
- BSE's OWN account of its cash-equity segment complicates the "incumbent
  retains loyalty" reading Goel invokes. As of May-2026, CEO Ramamurthy
  states cash-equity market share "has been hovering around 7% to 8%
  compared to 5% to 6% when I joined... far away from what we wanted it to
  be," and attributes the stagnation to a STRUCTURAL, unresolved
  regulatory/technical bottleneck — smart order routing applications
  "pending for more than six months at the other exchange" — not to
  customer loyalty toward the incumbent (BSE Concall May 2026 Transcript,
  p.16, answering Satyam Chaurasiya). The SAME structural explanation
  (algo/SOR approval bottlenecks keeping clients from being "exchange
  agnostic") is already present a full quarter earlier, in the Feb-2026
  transcript (BSE Concall Feb 2026 Transcript, p.13) — this is a
  consistent, repeated, non-loyalty account of why BSE's cash share stays
  low, not a one-off remark.
- By Aug-2026, BSE reports the stuck segment beginning to move: "our
  institutional volumes and cash market share are creeping up... maybe by
  the beginning of the calendar year 2027, we should have touched at least
  a very meaningfully double-digit market share in cash market" (BSE
  Concall Aug 2026 Transcript, p.14, answering Prayesh Jain) — an
  improvement BSE itself does not attribute to any weakening of NSE's
  customer loyalty, but to its own multi-year regulatory-advocacy and
  infrastructure effort.
- BSE explicitly treats its DIFFERENTIATED derivatives product
  (Sensex-linked) as a different case from the DIRECTLY-COMPETING cash
  segment: "our market share is 100% because our product is unique...
  we've never been tracking the market share part of it with regard to
  the derivative" (BSE Concall Nov 2025 Transcript, p.10-11, S.
  Ramamurthy). This means BSE's own record contains BOTH a stuck,
  structurally-explained segment (cash) AND a segment where the
  "market-share" frame does not even apply the way Goel's analogy assumes
  (differentiated derivatives) — a materially more complicated picture
  than "NSE kept its lead despite BSE" implies.
- CDSL is the cleanest same-mechanism test of a stickiness/loyalty claim
  in the corpus, and it fails within one quarter of being made. As early
  as Feb-2026, CDSL's CEO downplays a softening incremental share with "no
  significant drop as I would see it as of now" (CDSL Concall Feb 2026
  Transcript, p.10, Nehal Vora answering Sanketh Godha) — but the softening
  was already visible and quantified a quarter earlier still: incremental
  demat-account market share had peaked at 93% in Q3 FY25 and had already
  fallen to 82% by the Nov-2025 call (CDSL Concall Nov 2025 Transcript,
  p.9-10, Devish Agarwal's question, Nehal Vora's "we've not been losing
  market [share]... you have to look at the absolute numbers" response).
  By May-2026, CDSL's CEO makes an explicit "loyalty"/"commitment" claim
  underpinning its new-account market share as an "intangible" moat (CDSL
  Concall May 2026 Transcript, p.7, p.9-10). By Aug-2026, an analyst
  discloses a further, named 420bps incremental-share loss to a
  competitor's reduced onboarding friction, and management's response
  repeats the same value-proposition language rather than engaging the
  number (CDSL Concall Aug 2026 Transcript, p.6). The full CDSL arc — a
  quantified softening visible from Nov-2025, downplayed through Feb-2026,
  followed by an explicit loyalty claim in May-2026, followed by disclosed
  further erosion in Aug-2026 — is now four quarters long, not two, and
  the loyalty claim sits in the MIDDLE of a documented decline, not before
  it.
- An independent third party complicates the analogy further. At MCX's
  May-2026 call, investor Bharat Shah invokes IEX by name as a cautionary
  precedent, then cites the OPTIONS segment of the same NSE-vs-BSE
  relationship Goel uses, with the opposite lesson: BSE's options share
  went from "next to nothing" to "almost about 37%, 38%" incrementally in
  "3, 3.5 years" (MCX Concall May 2026 Transcript, p.13). The identical
  NSE-vs-BSE comparator supports "incumbents keep their lead" in cash and
  "dramatic reallocation happens" in options, within the same rivalry.

**Peers silent**: none of the three peers is silent on this topic.

**Net read**: BSE's own multi-quarter record does not support using "NSE
retained its market share against BSE" as a general reassurance. The
segment where BSE stayed stuck (cash) is explained by BSE itself as a
structural/regulatory bottleneck now easing, not customer loyalty; the
segment where BSE gained dramatically (options) directly contradicts the
"incumbents keep their lead" reading of the same rivalry; and the
differentiated-product segment (Sensex derivatives) sits outside the
market-share frame Goel's analogy assumes altogether. Layered on CDSL's
own loyalty claim failing within the same run of calls that first showed
the erosion it later claimed not to have, this is the single largest
complication the peer set adds to IEX's narrative.

---

## PART 1B: CARRIED FORWARD FROM RUN 1 (not among the current six questions, still hold)

These three findings answered Stage 5 run 1's peer_questions, which no
longer appear verbatim in the current B05 handoff. They are preserved here
per task instruction because the underlying peer evidence and verdicts
still stand; nothing in Stage 5's rework touched these topics.

### Carried-forward A — Regulator-driven market-structure change and fee-income impact

**Verdict: PARTIALLY VERIFIED.** BSE's SEBI-mandated weekly index-options
expiry-day reallocation to Thursday ("eight months" old as of May-2026,
BSE Concall May 2026 Transcript, p.18) is the one real peer precedent in
this corpus for a regulator-driven redesign of an exchange's core market
structure. Its realised outcome was EXPANSIONARY, not compressive: "seen
the market share increase in the option derivative segment" (BSE Concall
Nov 2025 Transcript, p.9) and average daily premium turnover +118% YoY
(BSE Concall May 2026 Transcript, p.5-6) — the opposite direction from
IEX's implicit worst case for DAM coupling. This complicates rather than
confirms IEX's reassurance framing, but it is not the same mechanism (a
scarce-day reallocation between rival index-options products, not a
forced shared order book across multiple exchanges for one product), so it
is not a reassurance either. No BSE call gives a pre-transition quantified
estimate to compare against the realised outcome (the transition predates
this corpus's Nov-2025 opening), so full verification is not possible.

### Carried-forward B — Non-operating income share of PBT/PAT and analyst attention

**Verdict: VERIFIED.** IEX's rising non-operating share of consolidated
PBT (23.4% FY26 to 29.8% Q1FY27), never raised by any analyst or by
management, sits inside a genuine, corroborated, SECTOR-WIDE analyst blind
spot, not an IEX-specific failure. All three peers face detailed analyst
questions about the absolute size and quarter-on-quarter driver of "other
income"/treasury income (BSE Concall Nov 2025 Transcript, p.6, treasury
income -32% QoQ; CDSL Concall Aug 2026 Transcript, p.6, Hiral Parekh
requesting a full income-source breakup; MCX Concall Aug 2026 Transcript,
p.16, Bunty Chawla on "drastic growth" in other income) — but across all
twelve transcripts, not one analyst asks for the SHARE of PBT/PAT this
income represents, or its multi-quarter trend.

### Carried-forward C — IGX associate stake sale / subsidiary IPO disclosure practice

**Verdict: UNVERIFIABLE.** Neither BSE nor CDSL discloses, or is asked
about, a comparable associate-entity stake sale, subsidiary IPO, or OFS
with a valuation/proceeds dimension anywhere in these eight transcripts.
BSE names its associate businesses (India INX, HPX, BEAM) once in generic
prepared-remarks language with no valuation or transaction attached (BSE
Concall Nov 2025 Transcript, p.7); the one adjacent topic is a shareholder
asking BSE to INCREASE its stake in BSE EbiX Insurance (BSE Concall Nov
2025 Transcript, p.15-16) — the opposite transaction type, with no
valuation figure either. This is a gap in available precedent, not a
finding about IEX's disclosure practice; the absence of contrary peer
evidence should not be read as confirmation of IEX's practice.

---

## PART 2: UNPROMPTED CROSS-READ

### 2A Demand environment
All three peers report a strongly positive demand backdrop across the same
Nov-2025 to Aug-2026 window: BSE's operational revenue +44% to +63% YoY
across quarters, "12th/13th consecutive quarter" of record top and bottom
line (BSE Concall May 2026 Transcript, p.16); CDSL's demat accounts
reaching "22.4 crore" (CDSL Concall May 2026 Transcript, p.4) with
continued account-opening growth; MCX's ADT and profit growing ~29-32%
YoY in the earliest call in the set (MCX Concall Nov 2025 Transcript,
p.4) and describing FY26 as "a strong year" (MCX Concall May 2026
Transcript, p.5). Against this broadly buoyant peer backdrop, IEX's
specific monthly misses (June +12.5%, July +7.7%, against a 15-20%
guidance band) read as more company/segment-specific (REC, DAM-mix
related) than macro-driven — worth weighing against Stage 5's "weather"
explanation for the same misses.

### 2B Pricing and input costs
BSE explicitly documents margin compression driven by volatility swings
(BSE Concall Nov 2025 Transcript, p.10-11, quoted in Q1 above). The same
unpredictability recurs in "other income"/treasury income at all three
peers. This is a genuine, sector-wide pattern of volatile, weather-like
non-core income that resembles IEX's own rising-and-volatile
non-operating income line (Carried-forward B) — it does not, on its own,
validate or invalidate IEX's specific 23.4%-to-29.8% TREND, since no peer
discloses the equivalent trend figure, but it shows the underlying
mechanism (float/treasury income tied to market volatility) is
structurally common to the whole market-infrastructure peer group.

### 2C Capex cycle
All three peers are expanding capex and technology spend simultaneously —
an industry-wide capacity race, not a lone expander. BSE: ~Rs.300 crore-
plus capital work in progress over six months (BSE Concall Nov 2025
Transcript, p.13-14) plus rising technology expense (BSE Concall Aug 2026
Transcript, p.17). CDSL: technology cost "4x over the last 3 years," now
exceeding employee cost on a consolidated basis (CDSL Concall May 2026
Transcript, p.11). MCX: continued investment in new products, member/FPI
onboarding and risk systems across all four calls, including the
newly-incorporated coal exchange (MCX Concall Aug 2026 Transcript, p.6).
None of the three signals a maturing, cost-cutting posture.

### 2D Competitive mentions
IEX is named directly, three times, all by MCX-side or BSE-side investors
(not by peer management):
- MCX Concall Feb 2026 Transcript, p.18 — investor Parikshit Gupta: "We
  all know what is happening with IEX, although we are governed by a
  different regulatory body. But do you anticipate any similar risks..."
- MCX Concall May 2026 Transcript, p.13 — investor Bharat Shah: "if you
  look at IEX, the energy Exchange, out of the blue, the market coupling
  issue has come. And that is very clearly derailed the situation... we
  are seeing how IEX is struggling with that issue." (Also the source of
  the BSE-options counter-precedent used in Q6 above.)
- BSE Concall May 2026 Transcript, p.19 — investor Rushabh Doshi compares
  BSE's payout ratio unfavourably to "other exchanges, let's say like IEX
  or NSE" (a minor, payout-policy-only mention).
Two of these three are unprompted, third-party (buy-side) observations
made while discussing a different company entirely, and independently
corroborate that IEX's market-coupling exposure is viewed externally as a
severe, "derailed the situation" level risk — confirming the severity
Stage 5 already flagged, from an independent source.

### 2E Risks peers discuss that IEX does not
- SEBI restructuring its own internal commodity-derivatives oversight,
  with an uncertain effect on MCX's open regulatory items (position
  limits, co-location) (MCX Concall Aug 2026 Transcript, p.19). No IEX-side
  equivalent account of CERC's internal reorganisation appears in this
  corpus.
- RBI regulation on bank-guarantee funding of clearing-corporation margin
  money, with an acknowledged, not-yet-fully-realised impact (BSE Concall
  Aug 2026 Transcript, p.16-17; MCX Concall May 2026 Transcript, p.18). No
  IEX-side equivalent funding-structure regulatory risk is disclosed.
- CDSL's fintech-onboarding-friction competitive erosion, quantified in
  real time (420bps incremental share loss, CDSL Concall Aug 2026
  Transcript, p.6) — a live, numbered competitive-erosion metric IEX does
  not disclose for its own DAM/TAM monthly share by competitor.
- BSE's core-SGF (Settlement Guarantee Fund) contribution policy, flagged
  by management itself as a source of "sudden spurts... having sudden
  impact on the quarterly earnings," addressed via a new 5%-of-revenue
  smoothing policy (BSE Concall Nov 2025 Transcript, p.13). IEX's corpus
  in this run does not describe an equivalent settlement-guarantee
  capital-buffer mechanic.

---

## PART 3: PEER COVERAGE MAP

| Peer | Quarter | Used how | Key contribution |
|---|---|---|---|
| MCX | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Concentration refusal re: top-10 NSE brokers (Q5, p.16-17); electricity-derivative-vs-NSE market-share question frames Q2's context (p.14-15) |
| MCX | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Investor names IEX directly re: market coupling as monopoly-risk precedent (2D, p.18) |
| MCX | Q4 FY26 (May 2026) | SUBSTANTIVE | Coal-exchange qualitative framing, no size figure (Q4, p.17); "sticky liquidity" interoperability defence (Carried-forward A); Bharat Shah's IEX-named BSE-options counter-precedent to the NSE-vs-BSE analogy (Q6, 2D, p.13) |
| MCX | Q1 FY27 (Aug 2026) | SUBSTANTIVE | 68% yield-compression decomposition, single quantified external cause (Q1, p.11-12); electricity futures 55% market share and 8-10% spot-exchange penetration (Q2, p.16-17); coal exchange incorporated, still no size figure (Q4, p.6); "moat" claim vs competitive expiry-date actions (Q6 context); SEBI restructuring (2E, p.19) |
| BSE | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Premium-realization-per-contract compression, single named external cause, unquantified (Q1, p.10-11); "100% market share because unique," derivatives not tracked (Q6, p.10-11); treasury income decline disclosure (Carried-forward B, p.6); SGF policy volatility (2E, p.13) |
| BSE | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Smart-order-routing bottleneck explanation for stuck cash-segment share, one quarter earlier than previously credited (Q6, p.13) |
| BSE | Q4 FY26 (May 2026) | SUBSTANTIVE | Thursday-expiry-day transition and its expansionary outcome (Carried-forward A); cash-equity market-share stagnation (7-8%) and its structural, non-loyalty explanation (Q6, p.16) |
| BSE | Q1 FY27 (Aug 2026) | SUBSTANTIVE | Cash market share "creeping up," double-digit aspiration by early 2027 (Q6, p.14); other-income/technology-expense bookkeeping pattern (Carried-forward B); bank-guarantee/RBI regulation uncertainty (2E) |
| CDSL | Q2 FY26 (Nov 2025) | SUBSTANTIVE | Incremental demat market share already down from 93% (3Q FY25 peak) to 82%, with a deflecting response, one quarter earlier than previously credited (Q6, p.9-10); "we don't give any client-specific information" concentration refusal (Q5, p.10) |
| CDSL | Q3 FY26 (Feb 2026) | SUBSTANTIVE | Softening incremental market share downplayed ("no significant drop"), second leg of the Q6 arc (p.10) |
| CDSL | Q4 FY26 (May 2026) | SUBSTANTIVE | Explicit "loyalty"/"commitment" claim underpinning ~85%+ new-account market share, made in the MIDDLE of an already-visible decline (Q6, p.7, p.9-10) |
| CDSL | Q1 FY27 (Aug 2026) | SUBSTANTIVE | Confirmed 420bps incremental market-share erosion (Q6, p.6); flat refusal to discuss net realisation after client discounts (Q1, p.7-8); SEBI-mandated fee cuts, quantified and named "industry-wide" (Q1, p.7-8) |

**12 SUBSTANTIVE, 0 CITED-ONLY, 0 UNUSED.** All three transcripts run 1
marked CITED-ONLY (MCX Nov-2025, BSE Feb-2026, CDSL Nov-2025) upgrade to
SUBSTANTIVE on this run's fuller reading against the current six
questions: each carries evidence that materially informs at least one
Part 1 verdict above, not just a citation. This corrects run 1's Part 3
summary line, which stated "8 substantive and 4 cited-only" against a
table that itself listed 9 SUBSTANTIVE and 3 CITED-ONLY; the correct run 1
count was 9/3, and this run's fuller pass moves all three CITED-ONLY
entries to SUBSTANTIVE, for 12/0/0.

---

## PART 4: TRIANGULATION SUMMARY

Across the nine distinct claims this run has a verdict for (the six
current B05 peer_questions plus three carried-forward findings from run 1
whose topics do not appear in the current six):

- **Verified: 1 of 9** (Carried-forward B, non-operating income silence
  as a sector-wide blind spot).
- **Partially verified: 2 of 9** (Q1, fee-realisation pattern; Carried-
  forward A, fee-compression precedent).
- **Contradicted: 2 of 9** (Q5, concentration disclosure — peers are LESS
  forthcoming, not more; Q6, customer-loyalty/NSE-vs-BSE analogy).
- **Unverifiable: 4 of 9** (Q2, MCX electricity growth-rate corroboration;
  Q3, long-dated TAM comparability; Q4, MCX coal sizing consistency;
  Carried-forward C, IGX OFS disclosure practice).

**Single most consequential contradiction**: the Q6 finding, strengthened
this run. CDSL's own May-2026 "loyalty" claim for its ~85%+ new-account
market share was made in the MIDDLE of an already four-quarter-long,
disclosed erosion arc (93% peak, Q3 FY25; 82% by Nov-2025; downplayed
Feb-2026; loyalty claimed May-2026; further 420bps loss disclosed
Aug-2026) — a closer, more damaging structural match to IEX's own
"18 years of customer loyalty" defence than run 1 had established, now
that the arc's first leg is documented one quarter earlier. Layered on
BSE's own structural (not loyalty) explanation for its stuck cash segment
and an independent investor's options-segment counter-reading of the same
NSE-vs-BSE rivalry, this is the largest single complication the peer set
adds to IEX's narrative.

**Single strongest independent confirmation**: two separate MCX-side
investors, discussing a different company on a different call, name IEX
directly and independently characterise its market coupling exposure as a
severe, "derailed the situation" level risk — external corroboration,
from outside IEX's own investor base, that Stage 5's top red flag is
taken seriously by market participants who watch adjacent exchanges.

**Overall**: the peer set complicates IEX's narrative more than it
supports or cleanly undercuts it, on both the original run 1 questions and
the current six. It VERIFIES that IEX's silence on rising non-operating
profit share sits inside a genuine, sector-wide analyst blind spot. It
CONTRADICTS the premise that peers disclose customer/counterparty
concentration more proactively than IEX — CDSL and MCX both refuse
outright when asked comparably direct questions, and IEX is arguably the
only name of the four to have produced an actual concentration number on
the record, however late. It CONTRADICTS the customer-loyalty defence via
a now four-quarter CDSL arc, BSE's own structural explanation for its
stuck segment, and an independent investor's counter-reading of the
NSE-vs-BSE precedent Goel invokes. It leaves the coal-exchange sizing and
long-dated TAM comparability questions genuinely untestable — MCX
discloses no coal size figure at all, and no peer makes a comparably
specific long-dated TAM claim for its own core segment. It leaves the
IGX-OFS-silence question untestable for want of a comparable peer event.
And it PARTIALLY VERIFIES the fee-realisation pattern: the topic recurs at
all three peers, but none matches IEX's specific unreconciled, shifting
internal-explanation failure mode — MCX is more rigorous, BSE is
consistent but unquantified, and CDSL simply refuses to discuss the one
number (net realisation after discounts) that would answer the same
question IEX itself never resolved.

---

## PART 5: CROSS-PEER HYPOTHESIS

No single peer states this, but the pattern is visible only when the
calls are read together, and it sharpens with this run's fuller pass: all
three peers, asked a version of "what did the compression cost you," give
one of exactly three responses — quantify and decompose it with alternative
causes tested and ruled out (MCX, Q1); name a single external cause without
quantifying the compression itself (BSE, Q1); or refuse to discuss the
net number at all (CDSL, Q1 and, separately, on client-specific
concentration, Q5). The SAME three-way split recurs on concentration
(MCX and CDSL refuse; BSE is never asked) and on long-dated TAM framing
(none of the three volunteers a comparably specific claim to IEX's, Q3).

**Hypothesis**: Indian market-infrastructure exchanges/depositories
appear to have converged on an unwritten disclosure NORM that treats unit
economics under pressure (realisation per unit, net-of-discount pricing,
concentration) as either a MARKET-FACTOR narrative to be explained with a
single external cause (volatility, regulation) or a NON-DISCLOSURE
category to be declined outright — but never as a company-specific,
internally-debated number that gets revised or reconciled across
quarters in front of analysts. IEX's pattern (three different,
unreconciled, unquantified internal explanations for the same question
across three quarters) is the OUTLIER against this norm not because it
discloses too little, but because it attempts to explain without
committing to either the "external, single-cause" script MCX and BSE use
or the flat refusal CDSL uses — leaving a paper trail of inconsistency
that a cleaner "we don't discuss this" would have avoided.

**Testable**: track whether IEX's next unit-economics answer (fee
realisation, concentration) converges toward one of the two peer scripts —
a single, quantified, external cause, or an explicit refusal — rather than
continuing to offer new, unreconciled internal explanations. If the
hypothesis holds, sell-side pressure over time pushes market-infrastructure
management teams toward one of these two low-inconsistency-risk postures,
and IEX's current in-between pattern is a transitional state, not a stable
equilibrium.

---
