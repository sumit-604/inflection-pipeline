# STAGE 5: CONCALL ANALYSIS — KISSHT (OnEMI Technology Solutions Ltd)

Run date: 2026-09-19. Two transcripts only: Q4 FY26 (call 29-May-2026, filed
04-Jun-2026, first call after the 08-May-2026 listing) and Q1 FY27 (call
30-Jul-2026, filed 04-Aug-2026). No Q3 exists: the company was unlisted
before 08-May-2026 and has held only two calls, ever. This is a declared
short series, not a collection miss (B00-inputs.yaml, input_gaps). Every
cross-quarter statement below is checked against exactly two data points;
where a table calls for three quarters, the third column is marked N/A
(NO CALL HELD), not NOT FOUND.

Because the series is short, the RHP (OnEMI_RHP_2026-04-25.txt, dated
25-Apr-2026) is used as the earliest statement of intent, and the two
results filings, two presentation decks, the Q1 press release and the
three capital-raise announcements (14/17/18-Sep-2026) are used as delivery
evidence outside the calls themselves, per the injected brief. Units: Rs Cr
unless stated (concalls speak in Rs Cr; results filings are in Rs million;
no silent conversion below, source unit stated at first use per figure).

LOAD-BEARING FACTS — ANSWERED FIRST (per B00-inputs.yaml spear block)

LBF-1, the 150-DPD write-off statement. B02-notes and B03-ardeep both
independently confirmed NO numeric write-off trigger anywhere in the AR or
the RHP (B02-notes input_gaps; B03-ardeep input_gaps). This stage found the
exact transcript words. In the Q4 FY26 call, an individual investor (Abhi
Shah) asked directly why GNPA had "shot up from 0.79 to 2.9" over two
years. Krishnan Vishwanathan (CFO) answered:

"the reason why the GNPA shot up from 0.79 to 2.9 is more a technicality.
There was a time where we would write off earlier at 120. And basically,
after active discussion with our auditors, given the kind of recovery we
used to see before, our write-off period was extended to 150. So it was
more a technicality of when we write off the loan, which changed, that
caused the spikes that you see. It is not anything to do with the credit
quality improving or worsening... Now it has been 150 for now two years."
(Concall_Jun_2026_Transcript.pdf p.19-20)

This is the load-bearing admission the AR and RHP never make in numbers:
management itself states, on the record, that the GNPA percentage tracks a
disclosure-policy choice (write-off point moved from 120 DPD to 150 DPD),
not solely underlying credit behaviour, and frames a near-4x GNPA increase
as a "technicality." That framing is itself a claim requiring scrutiny (see
Section 2, tone and 2D). In the Q1 FY27 call, the same mechanic resurfaces
when Aditya Mundra (Mytemple Capital) asks why GNPA rose while credit cost
fell; Ranvir Singh answers: "gross NPA is a function of where I do the
write-off. I do the write-off for my personal book at 150-DPD. So in gross
NPA, what you will find is what is between 90-DPD and 150-DPD, but the
credit cost is coming from all the provisions that I have made plus the
write-off." (Concall_Aug_2026_Transcript.pdf p.20-21). This is FACT (a
disclosed accounting mechanic, confirmed by both officers across both
calls) layered with a MANAGEMENT VIEW (that the mechanic has no bearing on
"credit quality"). B02/B03's write-off-rate finding (~15.7% of average book
annually, +10.7% YoY, against 28.9% YoY growth in new Stage-3 inflow) is
the quantitative test of that view, and this stage does not find it fully
supported: a write-off period extension mechanically lowers the reported
GNPA ratio regardless of the trend in underlying inflow, and the transcript
gives no reconciliation of the two.

LBF-2, FLDG. Management confirms Off-book AUM carries FLDG (First Loss
Default Guarantee) "up to 5%" and, on direct question, "almost 100% of the
off-book AUM is covered by FLDG" (Ranvir Singh, Concall_Jun_2026 p.13).
Subhranshu Mishra (PhillipCapital) pressed on whether lenders "tweak the
IRR" if the 5% cap is breached; Krishnan Vishwanathan: "our exposure to
risk is to the extent of the FLDG provided... they may build in some
expectation if they are not convinced whether the FLDG is covered or not.
But from a structural and contractual perspective, the risk is capped at
5% and then it's an active negotiation" (p.13) — a MANAGEMENT VIEW that
concedes lenders price around FLDG adequacy, i.e. an unstated cost outside
the 5% cap is plausible but unquantified.

On accounting treatment, Aditya Mundra (Q1 FY27 call) directly tested
whether FLDG sits in opex/credit cost: Ranvir Singh confirms FLDG is
"part of your opex" when asked, then Krishnan adds he does not have the
quarter's FLDG-in-opex number "handy" but estimates "it'll probably add
about a percent or something" (Concall_Aug_2026 p.19-20). Ranvir then
clarifies the accounting split explicitly: "That doesn't include the
non-utilized FLDG portion... The non-utilized part... appears as the
capital that I have blocked, that of course doesn't appear in the overall
credit cost... It's only the utilized portion that one should take" as
part of credit cost (p.20). This is a FACT on mechanics (utilised FLDG
flows through credit cost/opex; unutilised FLDG is blocked capital, not a
P&L item) but an unquantified one: management could not give the specific
Rs Cr or bps figure live on the call, only a rough "about a percent"
estimate with no anchor to average AUM or off-book AUM. This directly
corroborates B02's red flag that FLDG cost "more than tripled group-wide
in FY26... outpacing revenue growth" while management's own live estimate
on the following call remains a guess, not a tracked KPI line.

LBF-3, FY27 guidance vs delivery. The Q4 FY26 call set FY27 guidance: AUM
growth "north of 40%"; GNPA "below 2.25%"; credit cost reduction "10%-15%"
YoY; RoAUM "4.5%-5%"; RoE "19-21%" (Ranvir Singh, Concall_Jun_2026 p.8-9).
One quarter later (Q1 FY27), delivery against each line:
- AUM: +61% YoY, +13% QoQ to Rs 8,001 Cr (press release
  20260729-74639f09 p.2; Concall_Aug_2026 p.3). Tracking well ahead;
  management explicitly claims to "overachieve" the 40% number (Tushar Q&A,
  Concall_Aug_2026 p.7).
- GNPA: printed 2.25% for Q1 FY27 — exactly at the "below 2.25%" guided
  ceiling, having RISEN sequentially from 2.12% (Mar-26) to 2.25%
  (Jun-26), a 13 bps sequential increase in the very first quarter of the
  guidance year (Investor_Presentation_1.txt p.30, quarterly series Jun-25
  3.64% / Sep-25 2.92% / Dec-25 2.90% / Mar-26 2.12% / Jun-26 2.25%; also
  stated verbatim by Ranvir Singh, "very range bound," Concall_Aug_2026
  p.4). One quarter cannot confirm or deny an annual guidance band, but the
  DIRECTION is the wrong one relative to the FY26 close-quarter narrative
  of "further strengthening asset quality."
- Credit cost: 6.80% of average AUM in Q1 FY27, down from 7.02% in Q4 FY26
  and 8.85% in Q1 FY26 (Concall_Aug_2026 p.4). This is tracking toward,
  and management states it is "tracking well" against, the guided 10-15%
  reduction (same page).
- RoAE: 21.20% annualised in Q1 FY27 (press release p.2), at or fractionally
  above the top of the 19-21% guided band on one quarter of evidence.
- RoAUM: 5.05%, at the top of the 4.5-5% guided band (press release p.2).
Net read: three of five guided lines (AUM, credit cost, profitability
ratios) are tracking ahead or in-band after one quarter; the GNPA line is
tracking the wrong direction, on a metric management itself has just told
investors is materially a function of where the write-off line is drawn
(see LBF-1). One quarter of data cannot prove a trend break either way;
this is the single most important number for stage 6/11 to watch.

LBF-4, the Rs 832 Cr preferential raise four months post-IPO. Board
approved on 17-Sep-2026 (four months and nine days after the 08-May-2026
listing) a preferential issue of up to 2,64,93,882 equity shares at Rs
314.11 (Rs 313.11 premium), aggregating up to Rs 832.20 Cr, to 34 named
investors (Axis MF, HDFC MF, MIT, Ashoka WhiteOak, 360 One, Groww, Bandhan,
Citigroup Global Markets Hong Kong, Unity SFB and others) —
(20260917-acc1d37a p.1-5; press release 20260918-4643d424 p.2-3). At the
time of this raise the most recent published CRAR (Si Creva, consolidated
into the group capital picture) was 40.2% (Tier-1 39.2%), reported for
Q1 FY27 as of 30-Jun-2026 (press release 20260729-74639f09 p.2). No
transcript, no press release, and no board outcome filing in this container
explains WHY a lender already carrying more than 2.5x the RBI's 15%
minimum CRAR requirement for its NBFC subsidiary needed a further large
capital infusion within months of an Rs 850 Cr primary IPO raise, 75% of
which had already gone into the same subsidiary. The press release's own
stated rationale is forward-looking and general: "to further strengthen
its capital position and support its next phase of growth" and to position
for "multiple credit rating upgrades over the next two years" through
"strong capitalisation" (20260918-4643d424 p.2). This is a MANAGEMENT VIEW,
not a quantified need. The Monitoring Agency Report on the IPO proceeds
(CRISIL, for quarter ended 30-Jun-2026, filed 29-Jul-2026) shows the prior
Rs 850 Cr issue was 91% utilised (Rs 7,725.04 mn of Rs 8,500 mn) with no
deviation from stated objects (20260729-4997d936 p.5, p.8) — so the prior
raise was not sitting idle; the group was genuinely deploying capital into
onward lending at the pace its 61-73% AUM growth requires. Read alongside
B02/B03's guarantee finding (parent corporate guarantee to Si Creva's
lenders at 228% of parent net worth, FY26), a plausible but UNSTATED
reading is that the raise substitutes primary equity for a guarantee
structure the notes show is already stretched — but this is inference, not
something management said on either call or in the press release; no
transcript in this container addresses the raise (it postdates the Q1 FY27
call by seven weeks) and no filing gives a numeric capital-need rationale.
This gap is itself the finding: a raise this large, this soon, at a CRAR
this comfortable, with no numeric justification anywhere in the filed
record, is a genuine open question for the next call (whenever the FY27
Q2 call is held) and for stage 6/11.

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Growth triggers, catalysts, drivers (both calls)

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| AUM growth >40% FY27, driven by high-quality customer targeting | Volume | Near (FY27) | Committed (repeated both calls) | Specific number, no sub-drivers quantified |
| Shift to higher-quality/lower-yield customers | Price-mix | Ongoing | Committed | Qualitative ("deliberate strategy"); FOIR 30% vs 34% quantified once (Q4 FY26) |
| Cost-of-borrowing reduction from rating upgrades (A- to potential A) | Cost | Medium (FY27-28) | Planned/aspirational | 200 bps already realised (Q4 call); 100-150 bps further "if" upgrade (Q4 call); 100 bps H2 FY27 (Q1 call) |
| Operating leverage (opex/AUM 19.9% to 18.0% in one quarter) | Cost | Near-medium | Committed direction, no target date | Quantified once (Q1 FY27 call) |
| Credit cost reduction 10-15% YoY | Cost | FY27 | Committed | Specific range, reaffirmed Q1 FY27 ("we hold firmly") |
| LAP (secured) scale-up, 98 to 178+ branches planned | Volume/inorganic-adjacent | Near-medium | Planned (branch target given) | 80 more branches by FY27-end (Q4 call); reached 101 by Q1 FY27 (partial delivery, see 1C) |
| LAP branch breakeven "around Q3" of the branch's second year; book breakeven cited as "a year or two away" (Q4) then "Q3 of this year" for the business overall (Q1) | Margin | Near | Planned | Specific quarter named, two different framings across calls (see 1C) |
| Mutual fund distribution subsidiary (Invincible Minds, AMFI registered) | Revenue (fee) | Medium-long | Planned | Registered by Q1 FY27; no revenue target given |
| Insurance distribution (existing) plus MF as new fee lines | Revenue (fee) | Ongoing | Committed (already live) | No quantum given either call |
| Rate cycle / RBI FCNR(B) liquidity easing system-wide cost of funds | Sectoral | Near | Management view (not company-specific) | Qualitative only (Q1 FY27 call) |
| 5-year product roadmap: gold loan, business loan, education loan, auto loan, loan-against-MF, in that "pecking order" | Inorganic/volume | Long (5-10 years) | Aspirational | Order given, no dates (both calls) |
| AI/ML underwriting improvement (AUC 66% to 74%) | Volume+margin (risk-adjusted growth) | Ongoing | Committed, evidenced | Quantified metric, repeated both calls, consistent number |
| Reopening of paused pin codes (450 paused Q4 FY26; 180 of 450 reopened by Q1 FY27) | Volume | Near | Committed (data-driven) | Quantified, consistent narrative across both calls (see 1C) |

### 1B. Quantified guidance (both calls)

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| AUM growth | >40% | FY27 | Q4 FY26 call (Ranvir Singh, p.8); reaffirmed and expected to be exceeded, Q1 FY27 call (p.7) |
| Gross NPA | below 2.25% | FY27 | Q4 FY26 call (p.9) |
| Credit cost (impairment) reduction | 10%-15% YoY | FY27 | Q4 FY26 call (p.9); reaffirmed "we hold firmly," Q1 FY27 call (p.4, p.9) |
| Return on average AUM | 4.5%-5% | FY27 | Q4 FY26 call (p.9) |
| Return on average equity | 19%-21% | FY27 | Q4 FY26 call (p.9) |
| Cost of borrowing reduction (post rating upgrade already banked) | ~200 bps realised since Feb-2026 CRISIL A- upgrade | ongoing, FY27 | Q4 FY26 call (Krishnan Vishwanathan, p.8-9) |
| Cost of borrowing reduction (further, if one more notch upgrade) | 100-150 bps | later FY27 into FY28 | Q4 FY26 call (p.9) |
| Cost of borrowing reduction (near-term, irrespective of upgrade) | minimum 100 bps | next 3 quarters from Q1 FY27 | Q1 FY27 call (Krishnan Vishwanathan and Ranvir Singh, p.11-12) |
| Cost of borrowing reduction (3-year view, management's own words "our own view") | 200-300 bps cumulative | 3 years | Q1 FY27 call (Ranvir Singh, p.15) |
| Steady-state leverage, on-book | 2.5x-3.0x debt-to-equity | long run | Q4 FY26 call (Krishnan Vishwanathan, p.22) |
| Spread (yield minus cost of borrowing) | 18-19% near term, reducing longer term | near-to-long term | Q4 FY26 call (Krishnan Vishwanathan, p.16) |
| LAP branch expansion | at least 80 more branches (98 to 178+) | FY27 | Q4 FY26 call (Ranvir Singh, p.20); actual reached 101 by Q1 FY27 (see 1C) |
| Organic acquisition channel share, long-run target | 40-45% or 40-50% | unstated horizon | Q1 FY27 call (Ranvir Singh, p.15) |
| ROA/ROE target for LAP business specifically | ROE 20%+ | unstated horizon | Q1 FY27 call (Ranvir Singh, p.18) |
| Cumulative 3-year DuPont benefit (operating leverage + cost of funds + risk reduction) | ~8-9% reduction in revenue margin absorbed while holding 5%+ ROA | 3 years | Q1 FY27 call (Ranvir Singh, p.15-16) |

### 1C. Trigger evolution across the two quarters

Only two data points exist per trigger; "evolution" here is a two-point
direction, not a multi-quarter trend line. Marked accordingly.

- AUM growth guidance: STRENGTHENING. Set at ">40%" (Q4 FY26); one quarter
  later management states it expects to "overachieve" that number given
  13% QoQ already banked (Q1 FY27 call, Tushar Q&A, p.7).
- Credit cost guidance: UNCHANGED, reaffirmed. "10-15%" stated Q4 FY26;
  "we hold firmly with that" Q1 FY27 (p.16). Two data points is thin
  evidence for a full-year claim but the direction (6.80% vs 8.85% Q1 FY26)
  is consistent.
- GNPA guidance: WEAKENING in direction, though still inside the stated
  ceiling. 2.12% (Mar-26, at Q4 FY26 call) to 2.25% (Jun-26, at Q1 FY27
  call) is a sequential rise, the first since at least Sep-25 per the
  presentation's own 5-quarter series (Investor_Presentation_1.txt p.30).
  Management's own framing on the Q1 FY27 call calls this "very range
  bound" (p.4) rather than acknowledging directional reversal.
- Pin-code pause trigger: a genuine EVOLVING, DATA-CONSISTENT trigger.
  450 pin codes paused (Q4 FY26 call, p.4); 180 of the 450 reopened, "the
  signals have turned modestly positive" (Q1 FY27 call, p.3, p.8). This is
  one of the few triggers with a specific before/after number that ties
  together cleanly across both calls — a point in management's favour on
  granularity (see Section 2).
- LAP branch count: PARTIAL/SLIPPING against the stated pace. Q4 FY26 call
  guided "at least 80 more branches" beyond 98 by "end of this financial
  year" (i.e., a target of at least 178 by Mar-2027). By Q1 FY27 (one
  quarter later, three quarters still to go in FY27) the count stood at
  101 (Concall_Aug_2026 p.5) — only 3 branches added in the quarter. This
  is not yet a missed guidance (three quarters remain), but the run rate
  (3/quarter) is far short of what "80 more by FY27-end" (roughly 27/
  quarter average) implies, and neither call flags the gap.
- LAP breakeven timing: a TIMELINE THAT SHIFTED IN FRAMING, not
  necessarily in substance, worth flagging. Q4 FY26 call: LAP "has not
  reached breakeven... probably a year or two away from being at steady
  state ROA" (Krishnan Vishwanathan, p.14). Q1 FY27 call: "somewhere
  around Q3 of this year, it will only be delivering the desired ROE"
  (Ranvir Singh, p.17) — i.e. Q3 FY27, roughly two quarters away, a much
  nearer date than "a year or two away" stated one quarter earlier. Either
  the Q4 FY26 answer was conservative or the Q1 FY27 answer is optimistic;
  the calls give no bridge between the two statements. FLAGGED for the
  next call to reconcile.
- NEW trigger, mutual fund distribution subsidiary: appeared for the first
  time at the Q4 FY26 call in response to an analyst question about a
  press release the analyst had seen ("I just wanted clarity on one press
  release that came out about a whole new subsidiary" — Prithviraj Patil,
  p.10), not volunteered in the prepared remarks. By Q1 FY27, management
  had folded it into prepared remarks as an established initiative with
  AMFI registration secured (p.5). Reasonable evolution for a small,
  disclosed corporate action; no red flag, but noted as a trigger that
  appeared reactively to an analyst prompt rather than being pre-announced.
- No triggers were found to have QUIETLY DISAPPEARED between the two
  calls; both calls cover a near-identical set of themes (AUM, asset
  quality, LAP, technology/AI, funding cost, guidance). This is
  unsurprising with only one quarter's gap.

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker (the single most important table)

With only one inter-call gap, this tracker checks what was promised at the
Q4 FY26 call (29-May-2026) against the Q1 FY27 call (30-Jul-2026), one
quarter later, PLUS what the RHP (25-Apr-2026, pre-listing) promised
against both post-listing prints (Q4 FY26 and Q1 FY27), per the injected
instruction to test the RHP as the earliest statement of intent.

| Promised in | Promise | Outcome by next data point | Explanation given |
|---|---|---|---|
| Q4 FY26 call | AUM growth >40% FY27 | On track / ahead: +13% QoQ, +61% YoY in Q1 FY27 alone | Management credits customer-quality targeting and repeat-customer base (Concall_Aug_2026 p.3, p.7) — ✅ (early, one quarter of four) |
| Q4 FY26 call | Credit cost -10 to -15% YoY FY27 | On track: 6.80% Q1 FY27 vs 8.85% Q1 FY26 (-23% YoY on one quarter, ahead of the low end) | Attributed to high-quality customer shift (p.4, p.9) — ✅ (one quarter; full-year not yet provable) |
| Q4 FY26 call | GNPA below 2.25% FY27 | Printed exactly 2.25% Q1 FY27, up from 2.12% Mar-26 (sequential rise) | Called "very range bound," no acknowledgement of the sequential direction (p.4) — Partial: inside the stated ceiling but moving the wrong way, and framed without qualification |
| Q4 FY26 call | RoAUM 4.5-5%, RoAE 19-21% FY27 | RoAUM 5.05%, RoAE 21.20% Q1 FY27 — at or above top of both bands | No caveat offered on sustainability of being already above-band one quarter in — ✅, though a print above the top of a full-year guided band in quarter one invites the question of whether the band itself is conservative |
| Q4 FY26 call | 100-150 bps further cost-of-borrowing cut "if" a second ratings upgrade lands, more likely FY28 | Incremental borrowing in Q1 FY27 came in at 12.9% fully loaded, ~150 bps below FY26 average (Krishnan Vishwanathan, p.11) | No second upgrade confirmed yet by Q1 FY27; management flags active engagement continuing — Partial, too early to grade fully |
| Q4 FY26 call | LAP: at least 80 more branches (98 to 178+) by FY27-end | 101 branches by Q1 FY27 (+3 in the quarter) | No explanation offered for the slow run rate against the implied pace; not raised by any analyst either — ❌/Partial (three quarters remain; flag the pace) |
| Q4 FY26 call | LAP breakeven "a year or two away" | Reframed to "around Q3" of the current year (i.e. roughly 2 quarters away) | No reconciliation given for the accelerated timeline — Partial/inconsistency flag |
| Q4 FY26 call | 450 pin codes paused, to be reviewed on data | 180 of 450 (40%) reopened by Q1 FY27, "signals have turned modestly positive" | Explained with a specific, falsifiable number and a stated ongoing-monitoring process (p.3, p.8) — ✅, the strongest single example of specific, checkable follow-through in the entire two-call series |
| RHP (25-Apr-2026) | Objects of Fresh Issue: 75% to Si Creva capital base, 25% general corporate purposes | Confirmed delivered: ~Rs 637 Cr (75%) infused into Si Creva by 16-May-2026 (press release p.2; Q4 FY26 call, Chirag Jain, p.18); CRISIL Monitoring Agency Report for Q1 FY27 confirms Rs 6,368.03 mn of Rs 6,375 mn allocated to the subsidiary object fully utilised, no deviation from objects (20260729-4997d936 p.5, p.8) | ✅ Clean, verified delivery on IPO-proceeds objects, independently confirmed by a third-party monitoring agency, not just management's own claim |
| RHP | Diversified, balanced funding base as a stated strength ("Access to diversified and scalable funding sources") | B02/B03 independently found 99.8% of the NCD book (a large share of on-book funding) rests behind a single parent corporate guarantee that itself exceeds the parent's own net worth (228% FY26) — a concentration point never named in the RHP's own diversification framing | Not addressed on either call; no analyst asked about the guarantee structure on either transcript in this container — this is a genuine 2D silence, see below |

Tally (see B05 YAML `promise_delivery` block for the coded counts): of the
promises above capable of being graded on one quarter of evidence,
delivered/on-track = 6 (AUM, credit cost, RoAUM/RoAE, cost of borrowing
incremental, pin-code review, RHP IPO-proceeds objects); partial = 3 (GNPA
inside-ceiling-but-wrong-direction, second-rating-upgrade too early, LAP
breakeven timeline inconsistency); missed/unaddressed = 1 (LAP branch
count pace, and separately, the RHP diversification claim vs the
guarantee concentration finding is an unaddressed SILENCE, not a broken
numeric promise, carried in 2D rather than counted here).

### 2B. Excuse pattern analysis

There is exactly one clear MISS-with-explanation in the two-call series:
the GNPA "technicality" answer (LBF-1). Classification: this sits between
HONEST-ADMISSION and DEFLECTION. It is honest in that management
volunteers the mechanical cause (write-off period moved from 120 to 150
DPD) rather than denying the number moved. It leans toward deflection in
framing the near-4x rise purely as "a technicality" and "not anything to
do with the credit quality improving or worsening" — a characterisation
this stage does not find fully supported once B02/B03's write-off-rate
finding (write-offs growing 10.7% YoY against 28.9% YoY growth in new
Stage-3 inflow) is weighed in. No instance in either transcript of
management saying "we made a mistake" or of external-blame-heavy language
(no blaming RBI, competitors, or macro for a company-specific miss). The
LAP branch-count pace and the LAP-breakeven-timeline shift are both SILENT
misses/inconsistencies: neither was raised by management proactively, and
no analyst pressed on either in the two calls available. Pattern check: on
the two data points available, management does not blame externals for
company-specific shortfalls (there are almost no shortfalls to explain
away with two quarters of consistently ahead-of-guidance numbers); the
one real test case (GNPA/write-off mechanic) is answered directly and
promptly when an individual investor asked, not evaded — but the answer's
framing is more reassuring than the underlying B02/B03 evidence supports.
Hard topics (write-off mechanics, FLDG accounting) were raised by
ANALYSTS/INDIVIDUAL INVESTORS, not volunteered by management in prepared
remarks on either call; management did not proactively flag the 228%
guarantee-to-net-worth ratio or the FLDG cost escalation on any call.

### 2C. Tone ratings (1-5, with evidence)

- Transparency: 3/5. Specific numbers are given readily on operational
  metrics (AUC, pin-code counts, branch counts, yields, spreads) and the
  write-off mechanic is disclosed when asked directly. But structurally
  important items (parent guarantee scale, FLDG cost trend, exact
  utilised-FLDG bps) are either not raised at all or answered with "I
  don't have it handy" (Krishnan Vishwanathan on FLDG-in-opex quantum,
  Concall_Aug_2026 p.19).
- Specificity: 4/5. Management gives precise figures readily (AUC 66% to
  74%, FOIR 30% vs 34%, 450/180/270 pin-code counts, 98/101 branches,
  29-30% PL yield, 21.8% LAP yield) — well above generic-guidance norms for
  a two-call-old listed company.
- Consistency: 3/5. Core guidance (AUM, credit cost, ROA/ROE) is repeated
  identically across both calls. But the LAP-breakeven timeline
  inconsistency (1C) and the "technicality, not credit quality" framing of
  a GNPA move that B02/B03 partially attribute to a write-off-rate
  mechanic sitting alongside GENUINE underlying improvement (the two are
  not mutually exclusive, but management presents only the reassuring
  half) both cost a point.
- Accountability: 3/5. Management does answer the hardest question
  (GNPA "shoot-up") directly rather than deflecting to a vague answer, and
  volunteers when the exact number is not "handy" rather than guessing
  confidently (FLDG opex quantum). But no LAP branch-pace shortfall or
  guarantee-concentration point is acknowledged unprompted.
- Defensiveness: 2/5 (lower is better; scored here as observed
  defensiveness, so 2 = mostly not defensive). One moment of mild
  irritation is visible: when Aditya Mundra pressed repeatedly on FLDG
  accounting, Ranvir Singh's tone shifts ("Hey, Aditya, you are asking a
  very simple accounting question... cannot ever be part of the total
  opex or credit cost", Concall_Aug_2026 p.20) — a short, slightly
  impatient response to a legitimate, repeated clarifying question, though
  he does still answer it.
- Over-promotion: 3/5. Language runs consistently aspirational ("we keep
  time in decades," "technology company that does lending, not the other
  way around," "building for the next decade") across both calls. This is
  standard IPO-era investor-relations register for a newly listed growth
  fintech, not unusual, but it is present on both calls without variation
  and sits alongside genuinely specific operational data, so it reads as
  polish layered on substance rather than substance replaced by polish.

### 2D. What they are NOT saying

- The parent corporate guarantee to Si Creva's lenders, at 228% of the
  parent's own net worth (FY26, per B02/B03, independently confirmed via
  CARO Annexure A) and backing 99.8% of the subsidiary's NCD book, is
  NEVER mentioned on either call. Given this is the single largest
  quantified structural finding in the corpus and the RHP's own
  "diversified funding" framing implicitly speaks to exactly this
  concentration risk, its complete absence from both calls — not raised by
  management, not asked by any of the twelve-plus analysts across the two
  calls — is a notable silence. Likely reason: this is a technical,
  balance-sheet-structure question that sell-side analysts covering a
  newly listed fintech may not yet have dug into the AR's notes deeply
  enough to ask; it also is not the kind of story management would
  volunteer given the RHP's contrary framing.
- FIU-IND "High Risk Financial Institution" classification / PMLA
  show-cause-notice history (disclosed in the RHP, per B03) is never
  mentioned on either call, and no analyst asks about it. Likely reason:
  the matter predates the RHP's own filing date and was resolved before
  listing (per B03's input_gaps), so it may be regarded internally as
  closed and not call-relevant; but its complete non-mention, including
  the absence of any forward-looking compliance commentary, is notable
  given the company operates in a segment (unsecured digital PL) that
  regulators scrutinise closely.
- The exact FLDG-in-opex/credit-cost bps figure for the quarter, though
  directly asked (Aditya Mundra, Q1 FY27 call), was not available "handy"
  and no follow-up commitment to disclose it was made on the call itself,
  though management did later commit to starting to disclose product-wise
  NIM/yield "from next quarter" when asked a related question (Krishnan
  Vishwanathan, p.21).
- The rationale for the Rs 832 Cr preferential raise (17-Sep-2026,
  postdating both calls) obviously could not be addressed on either
  transcript in this container, but is flagged here as the single most
  important open question for whichever call follows it.
- Neither call addresses competitive intensity from well-capitalised bank-led
  digital lenders in quantified terms (e.g., market share trend, pricing
  compression from banks entering digital PL) beyond a qualitative
  "we have built... in the same competitive environment" (Ranvir Singh, Q4
  FY26 call, p.17-18); this is thin given personal-loan pricing competition
  is a frequently cited sector risk (per peer_questions below).

### 2E. Repeated question tracker

NO REPEATED UNANSWERED QUESTIONS FOUND. With only two calls, "repeated
across two or more quarters" requires the identical question to appear at
both the Q4 FY26 and Q1 FY27 calls. No analyst question in the Q1 FY27
call repeats a Q4 FY26 question verbatim or in substance without having
first been answered; the closest candidate — pin-code pause count — was
answered specifically at Q4 FY26 (450 paused) and followed up with a new,
more granular question at Q1 FY27 (Abhishek Murarka asking for the
reconciliation of the "40% reopened" figure against 17,000 total pin
codes), which management answered fully and specifically (450 of the
11,000 pin codes driving 98% of business; 180 reopened, 270 still paused —
Concall_Aug_2026 p.7-8). This is progression, not evasion.

---

## SECTION 3: COMPETITIVE INTELLIGENCE FROM CONCALLS

### 3A. What management says about competitors

Management names Bajaj (Finance) and Chola (Cholamandalam) explicitly as
personal-loan and LAP competitors "as we have mentioned in our RHP also"
(Ranvir Singh, Q4 FY26 call, p.17). The competitive claim made is
qualitative: Kissht's edge is "demonstrated credit performance" (AI/ML
models, collections infrastructure) and "large base of customers"
enabling repeat-customer targeting (same page). Credibility check: this is
a MANAGEMENT VIEW, not independently evidenced in either transcript with a
market-share number, win-rate, or comparative pricing data point against
either named competitor. The AUC improvement (66% to 74%) and the 2.5x
risk-separation-over-bureau-only claim are internally consistent across
both calls, which lends some credibility to the underwriting-quality
claim specifically, but says nothing about competitive POSITION relative
to Bajaj or Chola (neither of whose models are benchmarked).

### 3B. Industry and market intelligence dropped in the calls

- Q1 FY27 call: management describes an industry-wide "divergence beneath
  a calm surface" — "headline asset quality looks benign, yet beneath the
  surface, stress is building, concentrated in... small ticket loans or
  instances of borrowers carrying debt across several lenders at once"
  (Ranvir Singh, p.3). This is presented as bureau-level industry
  observation, distinct from Kissht's own book, and is a genuinely useful,
  specific piece of sector colour (worth checking against SBICARD,
  Poonawalla, Ugro concall commentary — see peer_questions).
  "45% of our customers will have another personal loan outside of our
  personal loan" — a specific multi-lender-exposure disclosure about
  Kissht's own customer base (Krishnan Vishwanathan, Q4 FY26 call, p.13),
  consistent with and corroborating the industry-level divergence claim
  made a quarter later.
- RBI's FCNR(B) deposit push, cited as easing system liquidity and lowering
  system-wide cost of funds (Ranvir Singh, Q1 FY27 call, p.3) — a
  macro/policy observation, not company-specific, offered without
  quantification of Kissht's own expected benefit.
- Management flags "AI... reshaping certain salaried profiles," meaning
  some salaried applicants may show stale EPFO (salary) credit signals
  because they have lost employment, and states tightened underwriting in
  response (Ranvir Singh, Q1 FY27 call, p.16-17) — a specific, technically
  detailed observation not found in the Q4 FY26 call, i.e. a genuinely NEW
  and reasonably specific risk observation, not boilerplate.
- LTV discipline on LAP held at ~48% and explicitly stated as unlikely to
  rise (Ranvir Singh, Q4 FY26 call, p.12) — a specific, checkable
  underwriting parameter.

### 3C. Toughest analyst questions across both calls

1. GNPA "shoot-up" from 0.79% to 2.9% (Abhi Shah, individual investor, Q4
   FY26 call, p.19). Response satisfactory on mechanics (clear, specific
   answer given, per LBF-1) but not fully satisfactory on framing (see
   2B); the underlying risk (write-off-masked asset quality) is real per
   B02/B03 and not resolved by the "technicality" answer alone.
2. Reconciling the pin-code reopening with weaker collection
   efficiency/higher bounce (Abhishek Murarka, HSBC, Q1 FY27 call, p.7-8).
   Response satisfactory and specific: management ties the apparent
   contradiction to credit cost (the metric it says matters most) trending
   down and to seasonal (Q1) bounce patterns, with numbers given for both.
   This is a real risk worth continued monitoring (bounce/collection
   efficiency vs credit cost divergence), not fully resolved by one
   quarter's reassurance.
3. FLDG accounting treatment, pressed three times in succession by Aditya
   Mundra (Q1 FY27 call, p.19-20). Answer is directionally clear (utilised
   FLDG in credit cost/opex; unutilised FLDG is blocked capital) but the
   exact quantum was not available, and management's tone showed mild
   impatience under repeated questioning (2C). The concern (FLDG cost
   escalation, per B02) is a real, evidenced risk not resolved by this
   exchange.
4. Cost of borrowing appearing to rise QoQ despite a guided decline
   (Abhishek Murarka, Q1 FY27 call, p.9-10). Resolved satisfactorily:
   management explains a methodology change (monthly-average to
   daily-average debt AUM) caused the optical increase, with the
   underlying trend actually down ~10 bps on a consistent daily-average
   basis, and reiterates the forward-looking 100+ bps H2 FY27
   improvement. A reasonable, specific, checkable explanation.

### 3D. Customer and order book signals

- Customer base: 60 million registered users cited Q4 FY26 (Ranvir Singh,
  p.3), rising to 74.6 million registered users by Q1 FY27 (+33% YoY,
  Ranvir Singh, p.2) — a large jump in registered-user count in one
  quarter that is not fully reconciled with the more modest growth in
  "unique customers served" (11.76 million to 12.25 million, +26% YoY over
  the same window per the press release), i.e. registered users (top of
  funnel, includes non-borrowers) and served customers (actual borrowers)
  are two different, correctly distinguished metrics, but the gap between
  a 33% YoY jump in one and a 26% YoY jump in the other, both quoted in the
  same breath, is not explained on either call.
- Concentration: 45% of Kissht's own active customers already carry
  another personal loan (Krishnan Vishwanathan, Q4 FY26 call, p.13),
  typically of larger ticket size from "a larger institution." This is a
  DISCLOSED, SPECIFIC signal about portfolio risk that management gave
  proactively when asked, not something volunteered unprompted.
- Off-book AUM share rising: 49.7% (implied, "almost 50%," Q4 FY26 call
  p.7) to 53.6% (Q1 FY27 call, p.3 and press release), a genuine mix shift
  toward the FLDG-guaranteed, capital-light model, cited by management
  itself as a driver of margin compression (p.4). This is FACT, disclosed
  clearly and consistently, and directly relevant to the FLDG cost
  escalation flagged in B02/B03.
- No customer losses, renewals, or geographic-spread changes beyond the
  pin-code pause/reopen mechanic (already covered in 1C/3C) are disclosed
  on either call.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list (ranked by earnings impact)

1. AUM growth sustaining >40%, priority HIGH, type VOLUME, timeframe near
   (FY27), conviction M-H (one quarter already ahead of guidance).
   Confirms: continued 13%+ QoQ prints through FY27. Kills: a QoQ AUM
   deceleration below ~8-9% (implied quarterly run-rate for 40% annual)
   without a stated reason.
2. Credit cost trajectory (10-15% YoY reduction guided), priority HIGH,
   type COST, timeframe FY27, conviction M (one data point of six
   guided quarters). Confirms: continued sequential decline below 6.80%.
   Kills: any quarter where credit cost rises sequentially without a
   clearly explained seasonal or one-off cause.
3. GNPA direction (guided below 2.25%, printed exactly 2.25% and rising
   sequentially), priority HIGH, type flag (asset quality), timeframe
   immediate (next quarter is the tell), conviction L (the one guided
   metric currently moving the wrong way). Confirms: a sequential GNPA
   decline back toward or below 2.12% in Q2 FY27. Kills: a further
   sequential rise past 2.25%, which would break the stated ceiling and
   contradict the "range bound" characterisation given on the Q1 FY27
   call.
4. Cost-of-borrowing decline from rating upgrade cycle, priority MEDIUM,
   type COST, timeframe FY27-28, conviction M. Confirms: a confirmed
   second-notch upgrade from CRISIL or India Ratings within FY27.
   Kills: no upgrade materialising by end-FY27 despite the stated "active
   discussion."
5. LAP scale-up pace (branches, breakeven), priority MEDIUM, type VOLUME/
   MARGIN, timeframe FY27, conviction L (given the branch-count slippage
   and breakeven-timeline inconsistency flagged in 1C). Confirms: branch
   count catching up toward the ~178 FY27-end target and Q3 FY27
   breakeven actually landing. Kills: continued sub-pace branch adds with
   no explanation, or a further pushed-out breakeven date.
6. Rationale and terms of the Rs 832 Cr preferential raise, priority
   HIGH (governance, not earnings), type REGULATORY-POLICY/CAPITAL,
   timeframe immediate (next call must address this), conviction: NOT YET
   RATEABLE (post-dates both calls in this container). Confirms: a clear,
   numeric capital-need rationale given at the next call. Kills: continued
   silence on why Rs 832 Cr was needed at 40.2% CRAR, which would sustain
   the LBF-4 question as an open governance flag.
7. Fee-income diversification (insurance, mutual fund distribution),
   priority LOW (immaterial to earnings so far), type REVENUE, timeframe
   long, conviction L (no revenue quantum given either call). Confirms:
   a disclosed fee-income contribution in a future quarter. Kills:
   continued non-disclosure of quantum after several quarters, suggesting
   immateriality.

### 4B. Questions for peer verification (handoff to stage 6)

Peers: SBICARD (SBI Cards), POONAWALLA (Poonawalla Fincorp), UGROCAP (Ugro
Capital).

- {question: "Is the 'divergence beneath a calm surface' industry
  narrative — headline unsecured PL delinquencies improving while stress
  concentrates in small-ticket, multi-lender-exposed borrowers — echoed in
  SBICARD, Poonawalla, or Ugro's own Q1 FY27 (or most recent) concall
  commentary on the unsecured credit cycle?", why: "Kissht cites this as
  an industry-wide bureau-level pattern (Ranvir Singh, Concall_Aug_2026
  p.3), not company-specific; if peers describe the same divergence
  independently it corroborates a real sector inflection, if not it may be
  Kissht-specific commentary framed as sector-wide.", check_peers:
  [SBICARD, POONAWALLA, UGROCAP]}
- {question: "Do any peers disclose a specific DPD write-off trigger
  (e.g. 90/120/150 DPD) for unsecured personal loans, and has any peer
  changed that trigger in the last three years the way Kissht extended
  120 to 150 DPD?", why: "Tests whether a 150-DPD write-off point is
  industry-standard practice (in which case Kissht's GNPA framing is less
  unusual) or an outlier extension that flatters the headline ratio more
  than peers' equivalent numbers.", check_peers: [SBICARD, POONAWALLA,
  UGROCAP]}
- {question: "What FLDG/DLG rates and off-book AUM shares do Poonawalla
  and Ugro run in their co-lending/DA books, and how do they describe
  FLDG cost trend and accounting treatment (opex vs credit cost) on their
  own calls?", why: "Kissht's FLDG cost reportedly tripled group-wide in
  FY26 per B02/B03; peer commentary tests whether this is a company-
  specific escalation or a system-wide co-lending/FLDG repricing trend as
  off-book models scale across the sector.", check_peers: [POONAWALLA,
  UGROCAP]}
- {question: "What cost-of-funds trajectory and rating-upgrade commentary
  do peers give for FY27, and does the sector broadly expect 100+ bps of
  funding-cost relief from the FCNR(B)-driven liquidity easing Kissht
  cites?", why: "Tests whether Kissht's guided cost-of-borrowing
  improvement is a company-specific rating-upgrade story or a system-wide
  liquidity tailwind all NBFC lenders should be citing.", check_peers:
  [SBICARD, POONAWALLA, UGROCAP]}
- {question: "How do SBICARD, Poonawalla, and Ugro frame competitive
  intensity in digital/unsecured personal loans from bank-led digital
  lenders and fintech NBFCs, and do any name Kissht, Bajaj, or Chola as
  specific share-gaining or share-losing competitors?", why: "Kissht names
  Bajaj and Chola as competitors but gives no market-share evidence;
  peer commentary on the same competitive set tests the credibility of
  Kissht's 'demonstrated credit performance as our edge' claim.",
  check_peers: [SBICARD, POONAWALLA, UGROCAP]}
- {question: "Have any peers recently raised large preferential/QIP
  capital shortly after an IPO or at a CRAR comfortably above regulatory
  minimums, and if so what numeric capital-need rationale did they give?",
  why: "Directly tests whether Kissht's unexplained Rs 832 Cr raise at
  40.2% CRAR four months post-IPO (LBF-4) is unusual sector behaviour or a
  recognised pattern among fast-growing NBFC lenders positioning for
  scale ahead of a rating cycle.", check_peers: [POONAWALLA, UGROCAP]}

### 4C. Management quality verdict table

| Dimension | Rating | Basis |
|---|---|---|
| Guidance specificity | Good | Numeric bands given for AUM, GNPA, credit cost, RoA, RoE at the first post-listing call, reaffirmed the next |
| Delivery on guidance (2 quarters) | Good, with one flag | 4 of 5 guided lines tracking ahead/in-band; GNPA line technically inside ceiling but moving the wrong direction |
| Handling of hard questions | Mixed | Direct, specific answers given (GNPA mechanic, cost-of-borrowing methodology change); one flash of impatience under repeated FLDG questioning; one unquantified "not handy" answer |
| Proactive disclosure of structural risk | Weak | Parent guarantee (228% of net worth), FLDG cost escalation trend, and the Rs 832 Cr raise rationale are all either never raised on-call or (for the raise) not yet addressed in any call in this container |
| Consistency of narrative across calls | Good, with one gap | Core guidance and technology/AI narrative stable and specific across both calls; LAP-breakeven timeline showed an unreconciled shift |
| Overall grade | **C** | See credibility_basis below |

Grading logic: two clean, specific, verifiable delivery quarters against
company-issued guidance would ordinarily support a B. This stage grades C
because the framework requires grading "on the promise-delivery evidence,
not on tone or charm," and the one substantive credibility test available
(the GNPA write-off mechanic, LBF-1) produced a management framing
("technicality... not anything to do with credit quality") that this
stage, cross-checked against B02/B03's independently derived write-off-
rate evidence, does not find fully supported. Combined with the complete,
unprompted silence on the single largest quantified structural risk in the
corpus (the 228%-of-net-worth parent guarantee) across both calls, and the
unexplained scale/timing of the Rs 832 Cr raise, the credibility grade is
capped at C: management is specific and mostly forthright on operating
metrics, but the asset-quality narrative and the capital-structure picture
this stage can independently verify are each less complete than
management's own framing suggests. This is a call to raise position-size
caution (per the framework's Amendment 25 discipline), not a verdict on
whether the business itself is good or bad.

### 4D. Concall red flags

- {severity: HIGH, flag: "The single largest quantified structural risk in
  the corpus (parent corporate guarantee at 228% of net worth backing
  99.8% of Si Creva's NCD book) is never mentioned on either call, and no
  analyst across two calls and roughly twenty analyst/investor
  interactions asks about it."}
- {severity: MEDIUM, flag: "Management's own framing of the GNPA
  'shoot-up' as purely 'a technicality... not anything to do with credit
  quality improving or worsening' is not fully supported once cross-
  checked against the independently derived write-off-rate acceleration
  finding (B02/B03): the framing may be more reassuring than the evidence
  supports."}
- {severity: MEDIUM, flag: "FLDG-in-opex quantum could not be given on
  request ('not readily available... handy') on the Q1 FY27 call, despite
  FLDG cost having reportedly tripled group-wide in FY26 per B02/B03 — a
  material, escalating cost line management cannot cite to the basis
  point on request."}
- {severity: LOW-MEDIUM, flag: "LAP branch count added only 3 in the
  quarter (98 to 101) against an implied ~27/quarter pace needed to hit
  the stated 'at least 80 more by FY27-end' target, with no explanation
  offered or sought."}
- {severity: LOW, flag: "LAP breakeven timeline reframed from 'a year or
  two away' (Q4 FY26 call) to 'around Q3' of the current year (Q1 FY27
  call, roughly two quarters away) with no bridge given between the two
  statements."}

---

## SUMMARY FOR DOWNSTREAM STAGES

Two-call series, both clean transcripts, no scanned-text issues. Guidance
is unusually specific for a two-quarter-old listed company and mostly
tracking ahead. The credibility grade is capped at C not because
management lies or evades under direct questioning, but because (a) the
one hard question this stage could independently check (GNPA/write-off)
produced a management answer more reassuring than the underlying evidence
fully supports, and (b) the corpus's largest quantified structural risk
(parent guarantee) and largest open capital-structure question (the
Rs 832 Cr raise) are both completely absent from the call record, one
because no analyst has asked and one because it postdates the available
calls. Stage 6 should press peers hardest on the industry-divergence
claim, the FLDG cost trend, and precedent for post-IPO capital raises at
comfortable CRAR levels. Stage 11 should treat the GNPA line, not the AUM
line, as the asset-quality tripwire to watch quarterly.

analyst_note (verbatim, see YAML): The credibility grade sits at the C/B
boundary. It would move to B on ONE further clean quarter where GNPA
resumes its downward path AND management proactively addresses either the
guarantee structure or the raise rationale without being asked. It would
move toward D only if a future call repeats the "technicality" framing on
a further asset-quality miss without engaging the underlying write-off-
rate mechanic B02/B03 have now made visible to any analyst who reads the
filed notes.
