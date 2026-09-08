# Stage 5: Concall Analysis — Indian Energy Exchange Ltd (IEX)
Run date: 2026-09-08 | RUN 3 (TARGETED AMENDMENT) | Model: claude-sonnet-5

## Rework note
Run 2 read the monthly/quarterly volume filings only for the two metrics it
already suspected (fee realization, non-operating PBT share) and never
differenced those filings against the call narrative segment by segment. This
run builds that segment-by-segment table first (new Section 1D), then sets it
against what management said on the nearest call for every segment, and
reports every divergence. That procedure surfaced five MAJOR items run 2
missed or under-rated: the REC explanation names the wrong side of the market
(demand-side "confusion" answer against a filed supply-side collapse, sell
bids -86.1% YoY with clearing prices RISING — severity raised LOW-MEDIUM to
HIGH); the Apr-2026 CERC amendment on captive-plant REC trading was framed as
inventory-enhancing one quarter before REC sell bids collapsed; green market
growth decelerated from +23% (FY26) to +6.3% (Q1FY27) to -1.2% (June) with
the 24-Jul meet calling green "substantial" and never mentioning the
deceleration; market-share disclosure precision degrades in lockstep with the
coupling threat (84% full split -> 83% with an unexplained TAM restatement ->
no figure at all -> a bare 80-85% range); and day-ahead volume is in outright
decline in two of three most recent months (June -6.6%, July -7.7%, before a
partial August recovery to +15.0%), the exact segment coupling threatens,
which run 2 used only as background for the realization gap. Two further
evasion/falsification items are corrected: the fee-competition question was
evaded twice, not once (Nov-2025 "let us talk about peace"; the pricing half
of the identical Jul-2026 question was never answered by anyone); and
"things will definitely go in our favour" (Q3FY26) was falsified 14 days
later when APTEL dismissed IEX's own appeal for want of standing and CERC
then moved forward with draft coupling regulations — run 2's promise table
booked only the TIMING half of that answer as delivered and never booked the
substantive prediction anywhere, flattering the tally by one row. Three
classification errors are corrected: the "market coupling by January 2026"
line is removed from the MANAGEMENT promise tally (it is a CERC regulatory
timeline, not a company promise, as run 2's own prose already said); "no
significant margin impact" is reclassified out of the missed-promise tally
(Goel was answering a post-coupling hypothetical in response to a
worst-case-scenario question, and coupling has not happened — the realization
decline stands as its own finding, unchanged); and the M-Junction/MSTC
exclusion claim is downgraded from "regulatory fact sourced to the notified
rules" to management's own characterization, because the Coal Rules text is
not in the corpus (the same standard run 2 correctly applied to the APTEL
order). The ROE finding is kept but tempered: computed on AVERAGE standalone
equity rather than closing equity, the gap narrows (see 2D). One kept promise
run 2 omitted is added: the CFO's Apr-2026 treasury-income recovery
commitment, verified delivered from the filed results (Rs22.11cr Q4FY26 to
Rs44.92cr Q1FY27, standalone). Every citation below was verified by grep
against the "=== PAGE n ===" marker in the extracted text before use; several
of run 2's citations were off by one page against this system (e.g. the
"no significant margin impact" quote sits on Q4FY26 marker-page 15, not 14;
the Q3FY26 market-share figures sit on marker-page 16, not 9; the other-income
miss explanation sits on Q4FY26 marker-page 10, not 9); all are corrected
here. On the fuller evidence, this run's independent credibility grade is
**D**, down from run 2's C — see 4C for the full reasoning.

## Sources and quarter map
- Q2 FY26: `other__Concall_Nov_2025_Q2FY26_Transcript.txt` — call held
  31-Oct-2025, filed 07-Nov-2025. Guidance trail only, not one of the three
  primary quarters, per task instructions.
- Q3 FY26: `concalls__Concall_Feb_2026_Transcript.txt` — call held
  30-Jan-2026, filed 05-Feb-2026.
- Q4 FY26 / FY26: `concalls__Concall_Apr_2026_Transcript.txt` — call held
  24-Apr-2026, filed 30-Apr-2026.
- Q1 FY27: `concalls__Concall_Jul_2026_Transcript.txt` — IEX Analyst Meet
  2026, held 24-Jul-2026, filed 31-Jul-2026, IEX's sole Q1FY27 interaction.
- Segment delivery evidence, read in full this run: Power Market Update
  releases for FY26/Q4FY26/March'26 (filed 06-Apr-2026), Q1FY27/June'26
  (filed 03-Jul-2026), July'26 (filed 04-Aug-2026), August'26 (filed
  03-Sep-2026); Q1FY27 unaudited standalone and consolidated results
  (23-Jul-2026); Q1FY27 press release; FY26 Q4 audited results; the
  24-Jul-2026 Investor Presentation.

Every page citation below is the `=== PAGE n ===` marker number in the file
named, confirmed by grep against that marker before use, and nothing else
(not the printed page footer inside the document, which differs from the
marker by one or two pages in several places in this corpus).

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Every trigger management named

| Trigger | Type | Timeframe | Confidence | Specificity |
|---|---|---|---|---|
| GDP/electrification-linked power demand growth (EVs, data centers, ACs) | SECTORAL | long | aspirational | "6-7% GDP growth is doable," per-capita target 2,000 units/2030, 4,000/2047 (Q1FY27 p.12) |
| RTM growth from renewable variability | VOLUME | near/medium | committed (observed), now decelerating | FY26 +41% (Power Market Update FY26 p.2); forward "25 to 30 percent" stated once (Q1FY27 p.29), then falsified within weeks (see 1D) |
| Optimization/replacement of costly PPA power via exchange | VOLUME | medium | management view | AP saved Rs2,350cr (COVID), Telangana saved ~Rs700cr FY26 (Q1FY27 p.13); "up to 10% of power" replaceable (Q1FY27 p.11) |
| BESS merchant arbitrage | VOLUME | near/medium | committed (observed) | Juniper, ACME, Adani Green live on merchant basis; arbitrage FY24 Rs3.80, FY25 Rs5.03, FY26 Rs4.81/cycle (Q1FY27 p.15); management itself labels FY26 "an outlier year — very low prices, no demand increase, very good weather... probably we will not get similar year" (Q1FY27 p.15) |
| VPPA / Contract-for-Difference (SECI 500MW pilot) | VOLUME | medium | planned | CERC final VPPA guidelines Dec-2025; SECI CfD pilot approved but "not significant so far" uptake (Q4FY26 p.12) |
| Green RTM / Peak DAM / Peak RTM / 11-month TAM (4 pending petitions) | VOLUME/PRICE-MIX | near | planned, stalled | All four "order reserved" identically across Q2FY26, Q3FY26, Q4FY26, Q1FY27; TAM petition pending "more than two years" (Q1FY27 p.41) |
| Coal exchange | INORGANIC/REGULATORY-POLICY | medium | planned | Rules notified 4-Jun-2026, Indian Coal Exchange Ltd incorporated Jun-2026; opportunity size inconsistent (see 1C); the exclusion-of-incumbents claim is management's characterization of unseen rules, not verified rule text (see 1C, 2B) |
| Carbon/CCTS exchange | REGULATORY-POLICY | medium/long | aspirational, timeline pulled forward, materiality caveat dropped | Start date: "1-1.5 years" (Q2FY26 p.13) -> "FY27 or FY28" (Q3FY26 p.13) -> "within this calendar year... BEE wants 1-Oct-2026" (Q1FY27 p.5). The Q2FY26 caveat that sizes the actual opportunity — "If everybody is complying, then there's no trading" (Q2FY26 p.19) — is not repeated in any later call even as the start date is pulled in by roughly a year |
| ICX / I-REC issuance | VOLUME | near | committed but decelerating | Marketed as "200% growth" cumulative (Q4FY26 p.7) yet Q1FY27 issuance -4.5% YoY, 42.4 vs 44.4 lakh (press release p.3) |
| IGX gas exchange + IPO | VOLUME/INORGANIC | near | committed, status uncertain even to the CMD | DRHP filed 14-Jul-2026 (Q1FY27 p.5); asked directly about IGX IPO status on the very call reporting the DRHP filing, Goel answers "I'm not really fully aware about the exact status" (Q4FY26 p.12) — this against a hard PNGRB divestment deadline of 31-Dec-2026 |
| Long-term PPA routing through exchanges (draft National Electricity Policy) | REGULATORY-POLICY | long | aspirational | "Discussed since 2018 also" per Rohit Bajaj (Q1FY27 p.11); still draft |
| Capacity market (CERC staff paper) | REGULATORY-POLICY | medium/long | planned, running late | "Running a little late" self-admission (Q1FY27 p.12) |
| India Energy Stack / P2P local markets | VOLUME | long | aspirational | One pilot cited, no revenue model given (Q1FY27 p.30) |
| Mineral exchange | INORGANIC | long | aspirational | "Will be notified very shortly" (Q1FY27 p.5), boilerplate repeated without new detail |

### 1B. Quantified guidance, by quarter said

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Electricity volume growth | 15-20% every year | ongoing | Q2FY26 p.6, repeated Q3FY26 p.11, Q4FY26 p.13 |
| RTM forward growth | "25 to 30 percent in the time to come" | medium-term | Q1FY27 p.29 |
| Gas exchange (IGX) volume growth | 25-30% | next 4-5 years | Q3FY26 p.13 |
| TAM long-duration product market size | additional 15-20 billion units | medium-term | Q3FY26 p.13 |
| Coal exchange opportunity size (first figure) | "about 80 million tonnes" e-auction | current | Q4FY26 p.5-6 |
| Coal exchange opportunity size (restated) | "almost about 120 million tonnes" | current | Q1FY27 p.5, restated p.31 |
| Coal exchange incumbents' own volume (Rohit Bajaj, same Q1FY27 session as the 120mn figure) | "70-80 million tonnes of coal in a year" | current | Q1FY27 p.7 |
| Coal opportunity by 2035 | 250-300 million tonnes | 2035 | Q1FY27 p.31 |
| Total exchange share of national generation | ~25% (from current 8-9%) | 5-6 years | Q1FY27 p.31-32 |
| API-driven cleared volume | "more than 70%" of cleared volume | current | Q4FY26 p.9 — unqualified, i.e. total cleared volume |
| API-driven cleared volume (restated, narrower base) | "more than 70%" of I-DAM cleared volume; "more than 50%" via back-office API | current | Q1FY27 p.23 — I-DAM only, a basis shift not flagged |
| Term Ahead Market blended margin | Rs0.036-0.037 (3.6-3.7 paise) vs Rs0.04 standard | current | Q4FY26 p.15, in answer to a post-coupling hypothetical, the only specific per-unit margin figure ever given |
| PNGRB IGX equity-reduction deadline | extended to 31-Dec-2026 | — | Q4FY26 p.11 (grant); original deadline Dec-2025 per Q2FY26 p.11, 12-month grant against an 18-month request (Q2FY26 p.11) |
| Dividend | Interim Rs1.5/share (150% face value); final Rs2/share (200% face value); "50%, 65% as dividend" payout policy | FY26, ongoing | Q3FY26 p.4-5; Q4FY26 p.6; Q1FY27 p.27 |
| Net worth, EPS, ROE | Net worth "around Rs.1,400 crores," EPS "5.33 rupees," "ROE we are maintaining around 42% to 44%... over the last 4-5 years" | ongoing | Q1FY27 p.27 (Vineet Harlalka) — does not fully reconcile even on average equity (see 2D) |
| Coal exchange initial-year target | "at least 100 million ton[nes]" onto the platform | FY27 initial year | Q1FY27 p.27 |
| No additional cost, IEX's own MCO integration re-engineering | "No additional costs" | current | Q4FY26 p.15, in the SAME call where Grid India's equivalent build is called "additional costs" (Q4FY26 p.11) |

### 1C. Trigger evolution and flags

- **Market coupling risk quantification volunteered once, never repeated.**
  Goel's "20, 30, 40%" DAM-impact range was given unprompted in opening
  remarks on 24-Jul-2026 (Q1FY27 p.5) but not restated, and effectively
  contradicted ("I don't see any loss in market share... let's see"), when
  Analyst 6 asked the identical question directly later in the same session
  (Q1FY27 p.35). It appears in no audited filing. **STRENGTHENING then
  CONTRADICTED within one call.**
- **REC as a growth trigger: quietly dropped, and the explanation given for
  its collapse names the wrong side of the market.** Through Q2FY26-Q4FY26,
  REC volume weakness is framed as temporary; by Q1FY27 volume has collapsed
  -81.4% YoY (press release p.3) and management's framing shifts to "too
  early to make any comments" plus a buyer-side "confusion" over the RPO
  buyout provision (Q1FY27 p.41). The company's OWN Power Market Update for
  Q1FY27/June'26, filed 03-Jul-2026 — three weeks BEFORE the 24-Jul-2026 call
  — states plainly that "Sell bids declined by 86.1% YoY, leading to a rise
  in clearing prices during Q1FY'27" (p.3), and June's clearing prices of
  Rs.400/Rs.395 per REC were themselves higher than March's Rs.340 (Power
  Market Update FY26 p.4). Rising price with collapsing volume is a SELLER
  shortage, not a buyer-confusion demand problem; the two things cannot both
  be true. See Section 2B for the credibility read. **DROPPED, and
  MISDIAGNOSED — severity raised to HIGH from run 2's LOW-MEDIUM.**
- **Green market, the segment described as "substantial" on the call, was
  already decelerating in the company's own prior monthly filing and the
  deceleration was not mentioned.** FY26 green growth +23% (Power Market
  Update FY26 p.2); Q4FY26 quarterly +26.5% (p.2); Q1FY27 +6.3%, with June
  2026 alone at -1.2% YoY (Power Market Update Q1FY27/Jun'26 p.2-3) — filed
  03-Jul-2026. On the 24-Jul-2026 call, three weeks later, Goel describes
  green/TAM together as "again become substantial... about 7-8% of the
  product mix" (Q1FY27 p.12) without naming the deceleration visible in the
  company's own most recent filing at the time of the call. Green then
  partly recovered in July (+0.9%) and August (+17.3%) per the later monthly
  filings (see 1D) — but that recovery post-dates the call and does not
  change what the June filing already showed when the call was held.
  **WEAKENING AT THE TIME OF THE CALL, UNDISCLOSED.**
- **Day-ahead volume, the segment market coupling directly threatens, is in
  outright year-on-year decline in two of the three most recent months.**
  June -6.6% YoY, July -7.7% YoY (Power Market Update Q1FY27/Jun'26 p.3; Jul'26
  p.2), before a partial August recovery to +15.0% YoY (Power Market Update
  Aug'26 p.2) driven by a demand spike (buy bids +61.7% YoY) rather than a
  reversal of the underlying mix shift. Cumulative Q1FY27 DAM growth of only
  +7.6% YoY trails both total volume growth (+15.9%) and RTM growth (+23.5%)
  by a wide margin. Run 2 used this only as background evidence for the
  realization gap; it deserves its own standing as the clearest leading
  indicator of exactly the exposure coupling threatens. **NEW STANDALONE
  FLAG, see 4D.**
- **Market-share disclosure precision degrades step by step as the coupling
  threat rises, across all four transcripts, with no acknowledgment of the
  pattern.** Q2FY26 (Nov-2025, p.17): "electricity market share is 84%...
  IDM and RTM is 100%, 99%... TAM segments, it is 35%" — a full product
  split. Q3FY26 (Feb-2026, p.16): "electricity overall, we are around 83% in
  first nine months... TAM, it varies between 45%, 50%" — the TAM figure
  moved from 35% to 45-50% with no explanation for the change, and the
  headline slipped from 84% to 83%. Q4FY26 (Apr-2026): no percentage figure
  is given anywhere in the transcript; only qualitative language ("we should
  be able to retain a significant part of the market share," p.14). Q1FY27
  (Jul-2026, p.6): a bare, unattributed "80-85% market share" range with no
  product split and no stated period. The single most competitively
  sensitive disclosure IEX makes is becoming LESS precise exactly as the
  coupling threat becomes MORE concrete (draft regulations issued
  17-Apr-2026, Supreme Court proceedings live by Q1FY27). **DEGRADING IN
  STEP WITH RISK — raised to its own MAJOR flag, see 4D.**
- **Coal exchange opportunity size: unexplained ~50% upward revision, and
  the exclusion mechanism itself rests only on management's own
  characterization of rules not in this corpus.** "About 80 million tonnes"
  (Q4FY26 p.5-6) becomes "almost about 120 million tonnes" twice in the
  Q1FY27 session (p.5, p.31) — yet in the same Q1FY27 session, Rohit Bajaj's
  own prepared presentation sizes the incumbent platforms (M-Junction, MSTC)
  at "70-80 million tonnes" (p.7). No bridge or acknowledgment of the change
  is given anywhere in the corpus. Separately, the claim that incumbents will
  be barred from e-auctions within six months of the coal exchange's launch
  is stated three times (Q1FY27 p.5, p.7, p.31) as "the rule" notified by the
  Ministry of Coal, but the Coal Rules text itself is not in the corpus (see
  input_gaps) — this is management's characterization of a regulatory fact,
  not independently verified text, the same standard applied to the APTEL
  order in this report. **INCONSISTENT AND UNVERIFIED, flag for Section 4.**
- **TAM long-duration contract (3->11 months): timeline slipping.** First
  mentioned as awaiting CERC approval in Q2FY26; by Q1FY27, an analyst notes
  "it's been 2 years now since we have applied," which Goel confirms ("You
  are right") without giving a new timeline (Q1FY27 p.41). **SLIPPING.**
- **Green RTM / Peak DAM / Peak RTM petitions: identical "order reserved"
  language across all four transcripts** with no forward date ever given.
  **SLIPPING, unchanged status for at least three quarters running.**
- **Buyback: raised, never decided.** "We are definitely considering it"
  (Q4FY26 p.11) becomes "we will consider it in future" (Q1FY27 p.30) — a
  restated non-answer, not new information. **STALLED.**
- **Coal exchange itself (the entity, not the opportunity size) is a
  genuinely NEW and delivered trigger**: rules notified 4-Jun-2026,
  Indian Coal Exchange Ltd incorporated the same month, application process
  opened 15-Jul-2026 (Q1FY27 p.5-6, p.27). This is the one trigger that moved
  from "planned" to "operational entity" on a credible regulatory track —
  but its stated market size and its incumbent-exclusion mechanism are both
  the items that moved inconsistently or rest unverified (above).

### 1D. Segment-by-segment volume reconciliation (new this run)

Built from the four Power Market Update filings, differenced against the
nearest call's narrative. Units: BU/MU electricity volume unless stated;
REC in lakh certificates.

| Segment | FY26 (YoY) | Q1FY27 (YoY) | June'26 (YoY) | July'26 (YoY) | August'26 (YoY) |
|---|---|---|---|---|---|
| Day-Ahead Market (incl. HP-DAM) | 62.78 BU, +2.4% | 13,344 MU, +7.6% | 4,304 MU, **-6.6%** | 5,087 MU, **-7.7%** | 5,517 MU, +15.0% |
| Real-Time Market | 54.85 BU, +41.0% | 16,019 MU, +23.5% | 5,420 MU, +25.7% | 5,631 MU, +10.2% | 5,565 MU, +10.6% |
| Term-Ahead Market (incl. HP-TAM, contingency, up to 3mo) | 12.72 BU, +8.0% | 5,344 MU, +22.9% | 1,533 MU, +58.7% | 1,774 MU, +93.4% | 1,765 MU, +111.3% |
| Green Market (G-DAM + G-TAM) | 10.78 BU, +23.0% | 2,827 MU, +6.3% | 953 MU, **-1.2%** | 1,035 MU, +0.9% | 1,091 MU, +17.3% |
| REC | 187.20 lakh, +5.0% | 9.77 lakh, **-81.4%** | 2.49 lakh, **-92.3%** | 7.11 lakh, **-56.3%** | 2.91 lakh, **-86.6%** |
| Total electricity | 141 BU, +17.0% | 37.5 BU, +15.9% | 12.2 BU, +12.5% | 13.53 BU, +7.7% | 13.94 BU, +20.2% |

Sources, all `=== PAGE n ===` markers verified: FY26 column —
`announcements__Power_Market_Update_FY26_Q4FY26_Mar2026.txt` p.2 (headline),
p.3 (DAM/RTM/TAM), p.4 (Green, REC). Q1FY27 and June'26 columns —
`announcements__Power_Market_Update_Q1FY27_Jun2026.txt` p.2-3 (all segments).
July'26 column — `announcements__Power_Market_Update_Jul2026.txt` p.2 (all
segments). August'26 column — `announcements__Power_Market_Update_Aug2026.txt`
p.2 (all segments).

**What this table shows, set against the 24-Jul-2026 call narrative (the
nearest call to five of these six data points):**
- TAM is the fastest-growing segment by far (+58.7% to +111.3% YoY in the
  three most recent months) and is also the segment priced at the LOWEST
  per-unit fee (3.6-3.7 paise vs the ~4 paise blended standard, Q4FY26 p.15).
  This mix shift is the mechanically obvious driver of the fee-realization
  compression tracked in Section 2, yet management's three separate answers
  to the realization question (Section 2B) never name it.
- DAM, the segment coupling targets first, shrank outright in June and July
  and grew only 7.6% for the full quarter — a segment growing at half the
  company average is not what "we should be able to retain a significant
  part of the market share in this DAM segment" (Q4FY26 p.14) implies is
  happening today, independent of what coupling itself will do.
  August's rebound to +15.0% is demand-driven (buy bids +61.7% YoY on a heat
  spike, Power Market Update Aug'26 p.2), not a reversal of the RTM/TAM mix
  shift, and does not undo the fact that the deceleration was live and
  unaddressed at the time of the 24-Jul-2026 call.
- REC's collapse is not "too early to make any comments" (Q1FY27 p.41): four
  consecutive months of Power Market Updates before and after the call show
  an unbroken pattern of collapsing sell bids and rising clearing prices, a
  supply story that predates the call by at least one full quarter.
- Green decelerated sharply into the quarter the call covered and the call
  did not name it; it recovered only after the call, in data management did
  not have or did not cite when it called green "substantial."

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker

| Promised in | Promise | Outcome | Explanation given |
|---|---|---|---|
| Q3FY26 (p.7) | APTEL verdict "should happen within a month's time" | Delivered on TIMING — APTEL order issued 13-Feb-2026, roughly two weeks later | — |
| Q3FY26 (p.7), same answer, substantive half | "Things will definitely go in our favour" | **Missed / falsified** — APTEL's 13-Feb-2026 order held IEX "is not an aggrieved party at this stage" and dismissed the appeal on standing (Q4FY26 p.5-6); CERC then issued DRAFT COUPLING REGULATIONS on 17-Apr-2026 naming Grid India as market coupling operator (Q4FY26 p.6) — the process moved forward, not IEX's way | No acknowledgment in any later call that the confident prediction did not hold; the timing half is celebrated, the substantive half is never revisited |
| Q4FY26 (p.13) | Volume growth "15% to 20%" for FY27 | Delivered on the headline — Q1FY27 landed at +15.9% (press release p.2), inside the band | Volume delivered; but revenue growth (+10.1%) again trailed volume, the same pattern flagged every prior quarter |
| Q3FY26 (p.4-5), Q4FY26 (p.6) | Dividend policy: interim then final dividend, ~50-65% payout | Delivered — Rs1.5 interim, Rs2 final declared as stated | — |
| Q4FY26 (p.10) | CFO treasury-income recovery: "as the market is recovering, we will see that the numbers going back to the earlier numbers" | **Delivered** — standalone other income Rs22.11cr (Q4FY26) to Rs44.92cr (Q1FY27), per filed standalone results (`results__Q1FY27_Results_Unaudited_2026-07-23.txt` p.4) | Specific, checkable, verified against the filed statement this run |
| Q3FY26 (p.12) | IGX IPO "we plan to do it in this year" | Partial — DRHP filed 14-Jul-2026 (Q1FY27 p.5); not yet listed; and on the very call reporting the DRHP filing (Q4FY26), Goel says of the IPO process "I'm not really fully aware about the exact status" (Q4FY26 p.12), against a hard 31-Dec-2026 PNGRB deadline | Process "progressing well" (Q4FY26 p.11), no listing timeline given even at Q1FY27 |
| Q3FY26 (p.7-8) | REC volume: "by the end of the year, we will be able to still do better than what we did last year" | Partial — FY26 REC volume +5% YoY (Power Market Update FY26 p.2), barely ahead | Compliance-deadline shift and buyout-provision "confusion" cited (Q3FY26 p.8) |
| CERC order 23-Jul-2025, cited on every call since Q2FY26 | Market coupling of the Day-Ahead Market implemented "by January 2026" | **Reclassified, removed from the management tally.** This is a CERC regulatory deadline, not a company commitment; as of Q1FY27 still in draft-regulation/stakeholder-comment stage, Grid India itself raising new operational objections (Q1FY27 p.18-20) | External to management; tracked in timeline_slippages, not scored as a promise |
| Q1FY27 opening remarks (p.29) | RTM "will definitely grow at a rate of 25 to 30 percent in the time to come" | Missed, within weeks — Jul-2026 RTM +10.2% YoY, Aug-2026 +10.6% YoY (Power Market Update Jul'26 p.2, Aug'26 p.2), against FY26's own +41% | No explanation offered; guidance not revisited in any later document in the corpus |
| Q4FY26 (p.15) | "We don't expect significant impact on the margin part of it" (TAM benchmark 3.6-3.7 paise vs 4 paise) | **Reclassified, removed from the missed-promise tally.** This answered a direct worst-case-post-coupling hypothetical ("if the worst-case scenario was to come around"), and coupling has not been implemented; it is not a forward promise about the realization decline already underway | The realization decline (Section 2B, 4D) stands on its own evidentiary footing, unconnected to this answer |
| Q3FY26 (p.8) reasserted Q1FY27 (p.41) | REC volume weakness is transitory, "confusion will clear" | Missed, worsening, AND misdiagnosed — Q1FY27 -81.4% YoY, Jun-2026 -92.3%, Aug-2026 -86.6% YoY, driven by a SELL-side collapse per the company's own filings (see 1C, 1D) | Same buyer-side "confusion" excuse recycled a second time against a trend the company's own supply-side data contradicts |
| Q4FY26 (p.11) | Buyback "we are definitely considering it" | Missed — Q1FY27 restates "we will consider it in future" (p.30), no decision, no new information | SEBI rule uncertainty cited both times |

**Tally: 4 delivered, 2 partial, 4 missed** (of 10 scored promise/outcome
pairs). Two items from run 2's table (market coupling "by January 2026," "no
significant margin impact") are reclassified out of the management tally per
the corrections above; one falsified prediction ("things will definitely go
in our favour") and one delivered promise (CFO treasury-income recovery) are
added. The raw ratio is marginally better than run 2's 3/2/5, but the
qualitative severity of what remains and what is newly flagged in 1C/1D/2B
(REC misdiagnosis, market-share disclosure degradation, day-ahead decline,
repeated fee-competition evasion, dual revenue figures) is materially worse
— see 4C for how this resolves into the grade.

### 2B. Excuse pattern analysis

- **Fee/realization divergence — pure deflection, three different answers,
  never reconciled, and the mechanical driver sits unnamed in the company's
  own filed volume data.** Q2FY26: Vineet Harlalka attributes the gap to a
  REC fee cut (Rs40->Rs20) and lower REC volume (p.16-17, marker pages per
  this file's own numbering). Q3FY26: when Sumit Kishore points out the
  paisa/unit ratio is still below four paise even after adjusting for the
  REC fee cut, Goel offers "Maybe there is a variation in the yearly fees"
  (p.9), an answer that names no mechanism. Q1FY27: asked again, Goel says
  "we give some incentive" on TAM and REC contracts (p.41-42) — a third,
  different, still-unquantified explanation, immediately followed in the
  same session by "asset light high-margin platform business" framing
  (p.28) that sits uneasily beside an admitted, unquantified incentive
  regime. The structural driver — TAM volume (priced at 3.6-3.7 paise, below
  the ~4 paise blended rate) growing far faster than DAM (TAM +22.9% Q1FY27,
  +93.4% Jul-2026, +111.3% Aug-2026, while DAM fell -7.7% Jul-2026, see 1D) —
  is never named by management in any of the three answers.
  **Classification: DEFLECTION, textbook.**
- **REC decline — external-blame, recycled, and this run's evidence shows it
  is also a factual misdiagnosis.** Both instances (Q3FY26 p.8, Q1FY27 p.41)
  blame a buyer-side regulatory "confusion" (the RPO buyout provision) rather
  than the seller-side collapse the company's own Power Market Updates show
  (sell bids -86.1% YoY with clearing prices RISING, filed three weeks before
  the second instance of the excuse). Rising price with collapsing volume
  cannot be a demand problem. **Classification: EXTERNAL-BLAME, recycled,
  AND CONTRADICTED BY THE COMPANY'S OWN FILED DATA — raised to HIGH.**
- **Fee-competition / price-war question — evaded twice, across two
  quarters, not once.** Q2FY26 (p.18): asked directly whether IEX would
  "go into price wars" post-coupling, Goel answers, "I do not see any such
  situation that after coupling, there will be a price war in the DAM
  market. Why should we talk about war? Let us talk about peace." Q1FY27
  (p.34, question; p.34-35, response): asked whether tighter API integration
  could lead "to a more competitive pricing between the exchanges," Amit
  Kumar answers only the technical integration half ("the MCO arrangement is
  only for price discovery... through APIs we have done tighter integration
  with the customers... competitive advantage remains with us") — the
  pricing half of the identical question is never addressed by anyone in
  that session. **Classification: DEFLECTION, recycled across quarters —
  new MAJOR item this run, see 2E.**
- **Market coupling delay — genuinely external, but self-serving framing
  layered on top, and the substantive prediction on top of it was
  falsified.** The regulatory delay itself is a fair external attribution.
  But Goel's Q3FY26 response to a direct "what if it doesn't go our way"
  question ("Why are you saying that... Things will definitely go in our
  favour," p.7) is over-promotion rather than a balanced risk answer, and
  the prediction did not hold (see 2A). **Classification: EXTERNAL-BLAME
  with OVER-PROMOTION layered on, AND FALSIFIED.**
- **Coal opportunity-size shift — silence.** No acknowledgment anywhere in
  the corpus that the cited market size moved from ~80mn to ~120mn tonnes,
  or that the exclusion mechanism rests on rules not in evidence in this
  corpus. **Classification: SILENCE.**
- **Market-share disclosure — silence on a visible pattern.** No
  acknowledgment anywhere that the product-level split disclosed in Q2FY26
  and Q3FY26 stopped being offered in Q4FY26 and Q1FY27, or that the TAM
  figure moved from 35% to 45-50% between those two quarters with no stated
  reason. **Classification: SILENCE.**
- **Other income slowdown (Q4FY26) — the one honest, specific admission
  found, and the one forward promise this run independently verifies as
  DELIVERED.** Vineet Harlalka attributes the 29% quarter-on-quarter fall in
  other income to a one-time December treasury gain not repeating plus
  mark-to-market losses from the Iran conflict and rupee volatility (Q4FY26
  p.10), a specific, checkable, non-deflecting answer, and the recovery he
  forecast is verified in the Q1FY27 filed results (see 2A).
  **Classification: HONEST-ADMISSION.**
- **Two different revenue figures for the same quarter and the same year
  inside one presentation.** Goel's opening remarks state FY26 consolidated
  revenue at "Rs.747 crore" (Q1FY27 p.4) and Q1FY27 consolidated revenue at
  "202.8 crore rupees" (Q1FY27 p.4); Harlalka's closing remarks in the SAME
  call state FY26 total revenue "was somewhere around Rs. 745 crore" and
  this quarter "almost around Rs.201 crores" (Q1FY27 p.27), and the
  Investor Presentation slide shows the same "745" / "201" figures (slide
  p.38). Cross-checked against the filed unaudited results, Goel's figures
  (747, 202.8) match the filed CONSOLIDATED TOTAL INCOME line exactly
  (Rs746.95cr FY26, Rs202.81cr Q1FY27, `results__Q1FY27_Results_Unaudited_
  2026-07-23.txt` p.9); Harlalka's rounded "745"/"201" is directionally
  consistent but not identical. Not a large discrepancy in magnitude, but a
  specificity failure: the CMD and CFO cite two different numbers for the
  same two figures, in the same call, without reconciliation.
  **Classification: SILENCE/CARELESSNESS on internal consistency.**
- **Pattern check.** No instance of "we made a mistake" or an equivalent
  admission of company error was found across four transcripts. Hard topics
  are raised proactively only once (the DAM-impact range, opening remarks
  Q1FY27) and are not sustained when tested directly in the same session.
  Customer concentration surfaced only when an analyst asked it, as the
  literal last question of a two-hour meet. The fee-realization question has
  been raised by analysts, unprompted by management, in three consecutive
  quarters; the price-war question, in two.

### 2C. Tone ratings (1=poor, 5=excellent, except defensiveness and
over-promotion where 1=low/good and 5=high/bad)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 1/5 | Coal opportunity size, the API cleared-volume base, the ROE math, and now the market-share product split all shift, blur, or disappear without being flagged as changes; concentration held back to the last question of a two-hour session; two different revenue figures inside one presentation |
| Specificity | 2/5 | Guidance is persistently banded ("15-20%," "25-30%") and never bridged to unit economics; three separate answers to the paisa/unit question, none with a number attached; the CMD is on record "not really fully aware" of the status of the company's own IGX IPO |
| Consistency | 1/5 | Coal TAM 80mn->120mn tonnes with no bridge; REC excuse recycled while the company's own filed data shows the opposite mechanism; market-share disclosure precision degrades quarter over quarter as risk rises; RTM's 25-30% forward statement is contradicted by the company's own data within two months; DAM-impact range volunteered once then effectively denied in the same call |
| Accountability | 2/5 | No instance of ownership of a miss found; misses on REC, fee realization, RTM growth, and the "things will go in our favour" prediction are attributed to external "confusion," unspecified fee mix, or simply not revisited, never to a company decision |
| Defensiveness | 4/5 | CMD pushes back on pointed questions ("Why are you saying...," "Let us talk about peace" on the price-war question twice across quarters) and does not resolve the underlying question either time |
| Over-promotion | 4/5 | "18 years of customer loyalty," repeated NSE/BSE analogy, "asset-light high-margin platform" framing sit beside an unreconciled realization decline, an unreconciled ROE figure, and an admitted-but-unquantified incentive regime |

### 2D. What they are not saying

- **No bridge, ever, for revenue growth trailing volume growth** — asked in
  three consecutive quarters (Q2FY26 p.9, Q3FY26 p.9, Q1FY27 p.41), answered
  three different ways, the underlying mix driver (TAM's lower per-unit fee
  growing far faster than DAM, quantified in Section 1D) never named.
- **No acknowledgment that the REC explanation contradicts the company's own
  filed data** (see 1C, 2B) — a demand-side "confusion" story persists
  across two quarters against a filed supply-side collapse.
- **No acknowledgment that market-share disclosure has become less precise
  as the coupling threat has become more concrete** (see 1C) — the full
  product split offered in Q2FY26/Q3FY26 is simply not offered again.
- **Non-operating share of consolidated PBT rising (23.4% FY26 -> 29.8%
  Q1FY27, computed from filed results, see 4D) is never raised by management
  or by any analyst** across all four transcripts, despite feeding directly
  into the EPS and ROE figures management does volunteer.
- **No revisiting of the "cheap power drives volume growth" thesis** after
  DAM prices reversed higher: Q1FY27 DAM price +15.7% YoY, Aug-2026 +22% YoY
  (press release p.2; Power Market Update Aug-2026 p.2) — yet management
  continues to credit FY26's volume growth to the low-price optimization
  story without addressing what happens to that driver when prices rise, and
  explicitly labels FY26 itself "an outlier year" (Q1FY27 p.15) without
  drawing the connection through to the growth guidance built on it.
- **The coal opportunity-size shift is not addressed by management or asked
  about by any analyst**, despite the same session containing an internally
  inconsistent figure from a colleague, and despite the exclusion mechanism
  resting on rules not in this corpus.
- **No CFO reconciliation of the ROE claim** against the company's own
  reported net worth and PAT on either the standalone or consolidated basis.
  This run's own reproduction, tempered against run 2's: computed on
  CLOSING standalone equity, ROE is 36.3% (PAT Rs473.71cr / equity
  Rs1,306.7cr, `results__Q1FY27_Results_Unaudited_2026-07-23.txt` p.4);
  computed on AVERAGE standalone equity (opening Rs1,098cr FY25-close plus
  closing Rs1,307cr FY26-close, divided by two — Investor Presentation
  p.38), ROE is 39.4%. Average-equity ROE is the conventional basis, and
  with a 50-65% payout ratio the closing-versus-average distortion is real
  but modest; it narrows the gap to the stated 42-44% without closing it.
  **Finding kept, force tempered as instructed.**
- **No read-through offered from the three admitted 2023 product failures**
  (HP-DAM, HP-TAM, Ancillary Market — "not doing very well because liquidity
  is not there," Q1FY27 p.12) to the credibility of the three further pending
  product launches the bull case leans on.

### 2E. Repeated question tracker

| Question | Quarters asked | Responses | Classification |
|---|---|---|---|
| Why does revenue growth trail volume growth (fee/realization per unit)? | Q2FY26 (p.9), Q3FY26 (p.9), Q1FY27 (p.41) | Q2: REC fee cut Rs40->Rs20 plus lower REC volume. Q3: "Maybe there is a variation in the yearly fees" — no mechanism named. Q1FY27: "we give some incentive" on Term Ahead contracts — a third, different, unquantified answer | **DEFLECTED EVERY TIME — answer changed between quarters, never reconciled to a number** |
| When will market coupling actually be implemented / what is the timeline? | Q2FY26 (p.7-8), Q3FY26 (p.7, p.10-11), Q4FY26 (p.10-16), Q1FY27 (p.34-35) | Consistently "can't say," "let's see," "it's a regulatory process," with the goalposts moving each time (round-robin -> Grid India as MCO -> Grid India's own objections) | **DEFLECTED EVERY TIME across all four transcripts** |
| Would IEX compete on price / go into a price war if coupling happens? | Q2FY26 (p.18), Q1FY27 (p.34-35) | Q2FY26: "Why should we talk about war? Let us talk about peace" — no substantive answer. Q1FY27: the technical-integration half of the identical question is answered; the pricing half is never addressed by anyone in the session | **DEFLECTED EVERY TIME — new item this run, was previously logged only once as a single-call defensiveness quote** |
| Why is REC volume falling and when will it recover? | Q3FY26 (p.8), Q1FY27 (p.41) | Both times: a regulatory "confusion" (RPO buyout provision, a buyer-side story) is blamed and recovery is asserted, against the company's own filed data showing a seller-side collapse and worsening trend | **ANSWERED EVENTUALLY IN FORM, BUT THE ANSWER IS CONTRADICTED BY THE COMPANY'S OWN FILINGS AND THE UNDERLYING TREND WORSENS — severity raised this run** |
| What is the coal exchange opportunity size? | Q4FY26 (p.5-6), Q1FY27 (p.5, p.31) | Q4FY26: "about 80 million tonnes." Q1FY27: "almost about 120 million tonnes," twice, with no acknowledgment of the change; a colleague's own presentation in the same session cites "70-80 million tonnes" for the incumbents | **ANSWER CHANGED BETWEEN QUARTERS, AND WITHIN THE SAME SESSION, WITH NO EXPLANATION** |
| What is IEX's product-level market share? | Q2FY26 (p.17), Q3FY26 (p.16), Q4FY26 (none given), Q1FY27 (p.6) | Q2: 84% electricity, full product split, TAM 35%. Q3: 83%, TAM restated to 45-50% with no explanation. Q4: no figure of any kind given. Q1FY27: bare 80-85% range, no split | **PRECISION DEGRADES EVERY QUARTER AS THE COUPLING THREAT RISES — new item this run** |

---

## SECTION 3: COMPETITIVE INTELLIGENCE FROM CONCALLS

### 3A. Competitor commentary and credibility check

- **HPX, PXIL** (the other two power exchanges): referenced only
  structurally, via the Term Ahead Market's roughly stable three-way split
  ("40%, 50%, 30%, 20% kind of numbers," Q4FY26 p.15) offered as evidence
  that post-coupling margin erosion will be limited. A single data point
  extrapolated to a much larger, structurally different market (DAM);
  credibility check: **weak analogy, not independently verified in this
  corpus.**
- **M-Junction, MSTC** (coal e-auction incumbents): management states they
  will be excluded from the coal market within six months of the coal
  exchange's launch, citing rules notified by the Ministry of Coal (Q1FY27
  p.5, p.7, p.31). This is stated with a specific mechanism and repeated
  three times, but the Coal Rules text is not in this corpus (input_gaps:
  no coal-rules document collected). **Credibility check: DOWNGRADED this
  run from "credible, sourced to the notified rules" to management's own
  characterization of a regulatory fact not independently verified in this
  corpus** — the same standard this report applies to the APTEL order gloss
  below.
- **NSE/BSE analogy**: "Today you have NSE and BSE and in spite of that NSE
  has retained the market share... only time will decide" (Q1FY27 p.35),
  offered in direct response to a market-share-loss question, with no
  supporting data on why IEX's position is structurally similar to NSE's.
  **Credibility check: rhetorical reassurance, not evidenced.**
- **MCX**: named only as a settlement-revenue-share counterparty for
  electricity derivatives ("negligible" revenue, Q2FY26 p.17) and as a filer
  for a coal exchange license (Q4FY26 p.17) — no competitive commentary
  offered either way.

### 3B. Industry and market intelligence

- Power-exchange-wide volume grew 18% in FY26 against demand growth of just
  1.1% (Power Market Update FY26 p.2), i.e. nearly all incremental demand
  routed to exchanges (Q1FY27 p.12).
- BESS VGF-discovered prices collapsed from Rs10.83 lakh/MW/month down to
  under Rs2 lakh (Q1FY27 p.10).
- DISCOM financial health improving: AT&C losses down to 15% nationally;
  DISCOMs rated A+/A rose from 16 (FY24) to 31 (FY25) (Q1FY27 p.9).
- LPSC rule drove ~8 billion units of previously un-requisitioned central
  generator power onto the exchange in FY26 (Q1FY27 p.17-18), with 3 billion
  units already in Q1FY27 alone.
- Draft National Electricity Policy and Electricity Amendment Bill both
  pending Cabinet approval, expected "maybe in the month of August-September"
  2026 as of the Jul-2026 meet (p.2).
- Un-requisitioned surplus power on the sell side rose from ~7% to ~9-10% of
  volume between Q2FY26 and Q3FY26 (Q3FY26 p.14).

### 3C. Toughest analyst questions

| Question | Response | Satisfactory? | Real risk? |
|---|---|---|---|
| Fee/realization divergence (asked 3x) | Three different, unquantified answers, never reconciled | No | Yes — the core unit economics of the growth story are unexplained |
| Would IEX price-compete post-coupling? (asked 2x) | "Let us talk about peace" (Q2FY26); pricing half of the identical question simply unaddressed (Q1FY27) | No | Yes — pricing is the mechanism by which a coupled market erodes margin, and it is the one question nobody answers |
| Worst-case market-share loss from coupling (Q4FY26, Q1FY27) | Reassurance via customer loyalty and the NSE/BSE analogy; the one quantified range (20-40%) given once and then effectively withdrawn when asked directly | Partially | Yes — the Supreme Court appeal is live and unresolved |
| Top-client concentration (last question of the Jul-2026 meet) | Numbers given (50-60% buy side, ~40% top-10 sell side) only when asked directly, at the very end, with a stability claim asserted then partly withdrawn in the same answer | Partially | Yes — concentrated flow sits directly in the path of the coupling threat |
| REC collapse (Q3FY26, Q1FY27) | A buyer-side "confusion" excuse recycled against a trend the company's own filings attribute to a seller-side collapse | No | Yes — REC and the adjacent I-REC product are both weakening, and management's own diagnosis does not match its own filed evidence |
| Coal exchange logistics/competencies (Q4FY26 p.12-13) | Candid ("we had no expertise when we started... don't worry, we will do it here too") | Yes, on candor; no, on specifics | Moderate — logistics genuinely unresolved for a heterogeneous commodity |
| Devesh Agarwal's process-vs-merits question on the APTEL appeal (Q3FY26 p.10-11) | Detailed, informative, but ultimately "let us see" | Partially | Yes — the regulatory theory of the case is genuinely uncertain |

### 3D. Customer and order-book signals

- Top buyers: 50-60% of volume. Top 10 sellers: ~40%. Both disclosed only at
  the last question of the 24-Jul-2026 meet (p.42).
- Seasonal buyer churn admitted in the same answer: "one season there are new
  set of buyers, another season those are not there at all" (Q1FY27 p.42) —
  this cuts against the "18 years of customer loyalty" defense used
  repeatedly against coupling risk.
- 9,000+ registered participants; 5,000+ industrial consumers (Q1FY27 p.7,
  p.17-18). No discrete named customer win or loss anywhere in the corpus.
- API integration: >70% of I-DAM cleared volume via bidding API, >50% via
  back-office API (Q1FY27 p.23) — up from an unqualified ">70% of cleared
  volume" cited in Q4FY26 (p.9), a narrower, restated base with no
  acknowledgment of the change.
- No pricing renegotiation with any named customer segment is discussed in
  any transcript.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list

| Priority | Trigger | Type | Timeframe | Conviction | Confirms | Kills |
|---|---|---|---|---|---|---|
| 1 | Market coupling resolution (Supreme Court) | REGULATORY-POLICY | near/medium | M | SC ruling favorable to IEX, or coupling implemented on terms that preserve margin | Adverse SC ruling combined with unfavorable coupling implementation terms |
| 2 | Day-ahead volume stabilization | VOLUME | near | L | DAM YoY growth returns and holds above the company's own total-volume growth rate for two consecutive months | Continued or resumed DAM outright decline while RTM/TAM keep growing, confirming the mix shift into coupling's crosshairs |
| 3 | Fee/realization stabilization | PRICE-MIX | near | L | Paisa/unit stabilizes above 4.2 with a named, quantified reason | Continued drift toward the TAM blended rate of 3.6-3.7 paise |
| 4 | RTM volume growth sustaining | VOLUME | near | L | RTM growth returns to 20%+ in a subsequent monthly print | Sub-15% RTM growth persists for two or more consecutive months (already the case: Jul +10.2%, Aug +10.6%) |
| 5 | REC market recovery on the seller side | VOLUME | near | L | Sell bids in a subsequent monthly REC session recover materially and clearing prices normalize | Sell-bid collapse persists another two monthly sessions with rising clearing prices |
| 6 | Coal exchange monetization | INORGANIC/REGULATORY-POLICY | medium | L | Coal exchange license awarded to the IEX subsidiary with a credible volume ramp toward the initial 100mn-tonne target, and the incumbent-exclusion rule text becomes independently verifiable | Delayed regulations, a shared/denied license, or the opportunity size proving closer to the 70-80mn-tonne incumbent figure than the 120mn cited |
| 7 | BESS arbitrage-driven volume | VOLUME | near/medium | M | Continued merchant BESS capacity additions at the observed 4-5 rupee/cycle arbitrage | Arbitrage compresses faster than management's stated 3-5 year window, or FY26's own "outlier year" self-label proves to be the high-water mark |
| 8 | IGX IPO monetization | INORGANIC | near | L | Successful listing at a reasonable valuation, cash realized on the 22.3% sell-down, ahead of the 31-Dec-2026 PNGRB deadline | IPO delayed past the PNGRB deadline or priced at a steep discount to carrying value |
| 9 | Green RTM / Peak DAM/RTM / 11-month TAM product approvals | REGULATORY-POLICY | near/medium | L | CERC issues an approval order on any of the four pending petitions | Continued multi-year delay with no new order |
| 10 | Structural volume growth (GDP/electrification/EV/data centers) | SECTORAL | long | M | Sustained 15%+ volume growth over multiple quarters | Sub-10% volume growth for two or more consecutive quarters |

### 4B. Questions for peer verification (handoff to Stage 6)

1. **Do MCX, BSE, and CDSL show a similar pattern of fee realization
   trailing reported volume/activity growth, and if so, how do their
   managements explain the mix or price gap?** Why: tests whether IEX's
   three-times-unreconciled realization decline is a sector-wide fee
   pressure or an IEX-specific, unexplained issue. Check peers: MCX, BSE,
   CDSL.
2. **Does MCX's own commentary on its electricity derivatives segment
   (settlement tied to IEX's clearing price) corroborate IEX's claim that
   power exchanges collectively grew volume 18% in FY26 against demand
   growth of 1.1%?** Why: cross-checks a headline sectoral growth-rate claim
   against an independent source. Check peers: MCX.
3. **Do BSE, CDSL, or MCX managements make comparably long-dated TAM claims
   for their own core segments, and how have any prior such claims held up
   against delivery?** Why: tests whether IEX's ~25%-of-generation
   long-horizon framing is a sector-wide investor-relations pattern or IEX-
   specific overreach. Check peers: BSE, CDSL, MCX.
4. **Has MCX, which has also filed for a coal-market play, sized the same
   coal-exchange opportunity consistently in its own disclosures, and does
   it characterize the incumbent-exclusion mechanism the same way IEX does?**
   Why: an unreconciled ~50% market-size revision, resting on rules not in
   this corpus, is a specificity and verification red flag. Check peers: MCX.
5. **Do BSE, CDSL, or MCX disclose customer/counterparty concentration more
   proactively (in filings or on calls), and what do their numbers look like
   by comparison?** Why: calibrates whether IEX's 50-60%/40% concentration
   and reactive-only disclosure are unusual for a market-infrastructure
   platform. Check peers: BSE, CDSL, MCX.
6. **Does BSE's own concall record address its market-share trajectory
   versus NSE, the comparator IEX repeatedly invokes to argue coupling will
   not erode its position?** Why: the analogy is asserted without supporting
   data in this corpus. Check peers: BSE.
7. **Do any of the three peers disclose product-level or segment-level
   market share with degrading precision when a competitive or regulatory
   threat becomes more concrete, the way IEX's TAM/overall market-share
   disclosure narrowed between Q2FY26 and Q1FY27?** Why: an independent
   pattern-check on whether reduced disclosure precision under threat is a
   sector norm or an IEX-specific signal. Check peers: BSE, CDSL, MCX.

### 4C. Management quality verdict

| Criterion | Assessment |
|---|---|
| Guidance discipline | Mixed on the headline (volume 15-20% delivered every quarter shown), but two specific forward statements were falsified within weeks to months: RTM's "25-30%" (Jul/Aug prints at ~10%) and "things will definitely go in our favour" on APTEL (dismissed on standing 14 days later). |
| Transparency on adverse trends | Weak to poor. Fee realization: three unreconciled answers. REC: a buyer-side excuse contradicted by the company's own filed seller-side data. Market share: disclosure precision falling as the coupling threat rises. One genuine candid exception (other income miss, Q4FY26), independently verified delivered this run. |
| Consistency across quarters | Poor. Coal opportunity size moved ~50% unexplained; REC excuse recycled against a trend the company's own filings contradict; a risk range volunteered once was not sustained under direct questioning in the same call; two different revenue figures for the same period inside one presentation. |
| Handling of hard questions | Engages rather than refuses outright, but rarely resolves; the price-war/fee-competition question has now been evaded twice across quarters; concentration and realization data are extracted only under repeated or late-session pressure, never volunteered early. |
| Proactive disclosure | Weak. The single instance of genuinely proactive risk disclosure (the DAM-impact range) was not sustained; customer concentration was the literal last question of a two-hour session; green market deceleration, live in the company's own prior filing, was not mentioned on the call describing green as "substantial." |

**Overall grade: D (Poor).** Revised down from run 2's C on this run's
fuller, segment-by-segment reading.

**Basis**: Run 2 correctly found a genuinely mixed record — volume guidance
and dividend policy delivered, one miss (other income) explained candidly and
now independently verified as a kept promise. That evidence still stands.
What changes the grade is what the segment-by-segment differencing procedure
surfaced this run: the REC explanation is not merely an excuse, it is a
buyer-side story that directly contradicts the company's OWN filed
seller-side data (sell bids -86.1% YoY, clearing prices rising) available to
management three weeks before the call where the excuse was repeated — this
is either a material gap in management's own grasp of its own market, or a
selective account, and either reading is disqualifying for a company whose
core product IS price discovery. Layered onto that: market-share disclosure,
the single most competitively sensitive number IEX reports, becomes LESS
precise in lockstep with the coupling threat becoming MORE concrete across
all four transcripts, with no acknowledgment of the pattern. Day-ahead
volume — the exact segment coupling threatens — was in outright decline for
two of the three most recent months and was not named as its own risk on any
call. The fee-competition/price-war question has now been evaded twice
across two quarters, the second time by simply not answering the pricing
half of the question at all. A specific, confident prediction ("things will
definitely go in our favour" on APTEL) was falsified within fourteen days,
and the record before this run gave management credit only for the timing
half of that same answer while omitting the substantive half entirely — a
tally-flattering omission this run corrects. Two different revenue figures
for the same two periods appear side by side inside one presentation. None
of this is fraud, and none of it is disputed by hard numbers management
refuses to publish — the raw promise/delivery ratio (4/2/4) is not
dramatically worse than run 2's (3/2/5). But grading is on the
promise-delivery evidence, not the ratio alone, and the qualitative pattern
here — disclosure precision falling exactly where risk is rising, an excuse
that inverts supply and demand on the company's own numbers, and a
repeated refusal to answer the one pricing question that matters most to
the thesis — is a POOR record on the dimensions Section 1B of the Master
Framework asks this grade to measure. This independently reproduces the
segment-differencing procedure requested for this run, not a prior grade.

### 4D. Red flags

| Flag | Severity |
|---|---|
| REC decline explanation names the wrong side of the market: management's buyer-side "confusion" story (Q3FY26 p.8, Q1FY27 p.41) directly contradicts the company's own filed Power Market Update three weeks before the second instance ("Sell bids declined by 86.1% YoY, leading to a rise in clearing prices," Q1FY27/Jun'26 filing p.3); rising price with collapsing volume is a seller shortage, not buyer confusion | HIGH |
| Market-share disclosure precision degrades every quarter as the coupling threat becomes more concrete: 84% full product split (Q2FY26 p.17) -> 83% with an unexplained TAM restatement from 35% to 45-50% (Q3FY26 p.16) -> no figure of any kind (Q4FY26) -> a bare unattributed 80-85% range (Q1FY27 p.6) | HIGH |
| Day-ahead volume, the segment market coupling directly threatens, in outright YoY decline in two of the three most recent months (June -6.6%, July -7.7%, Power Market Update filings) and growing at less than half the company average even in the quarter that did grow (Q1FY27 DAM +7.6% vs total +15.9%) | HIGH |
| Fee-competition / price-war question evaded twice across two quarters: "Let us talk about peace" (Q2FY26 p.18) with no substantive answer; the pricing half of the identical question left unaddressed entirely (Q1FY27 p.34-35) | HIGH |
| "Things will definitely go in our favour" (Q3FY26 p.7) falsified 14 days later when APTEL dismissed IEX's appeal for want of standing and CERC then issued draft coupling regulations naming Grid India as MCO; the promise-delivery record before this run credited only the timing half of the same answer | HIGH |
| Fee realization compression (computed: 4.16 paise/unit Q1FY27 vs 4.33 paise/unit Q1FY26, standalone revenue from operations Rs15,592.97 lakh / 37.5 BU vs Rs13,998.81 lakh / 32.4 BU) unreconciled across three quarters of direct questioning, with the mechanical driver (TAM's faster growth at a lower per-unit fee) quantified in this run's segment table but never named by management | HIGH |
| RTM growth guidance ("25 to 30 percent," Q1FY27 p.29) falsified within weeks by the company's own July (+10.2%) and August (+10.6%) Power Market Updates | HIGH |
| Coal exchange opportunity size revised ~50% upward (80mn -> 120mn tonnes) within six months with no bridge given, internally inconsistent within the same session (colleague cites 70-80mn), and the incumbent-exclusion rule itself rests only on management's characterization of a text not in this corpus | MEDIUM |
| CFO's ROE claim (42-44%) does not fully reconcile with the company's own reported numbers even on the conventional average-equity basis: 39.4% on average standalone equity (PAT Rs473.71cr / avg of Rs1,098cr and Rs1,307cr), 36.3% on closing standalone equity; the EPS figure quoted (Rs5.33) is standalone basic EPS, cited in the same breath as consolidated PAT figures | MEDIUM |
| Two different revenue figures for the same FY26 and Q1FY27 periods inside one presentation: CMD cites Rs747cr FY26 / Rs202.8cr Q1FY27 (matching filed consolidated total income of Rs746.95cr / Rs202.81cr); CFO and the investor presentation slide cite Rs745cr / "almost around Rs201cr" for the same two periods | MEDIUM |
| Customer concentration (50-60% buyer, ~40% top-10 seller) disclosed only at the final question of a two-hour analyst meet, paired with a stability claim asserted then partly withdrawn in the same answer, and a seasonal-churn admission that cuts against the "customer loyalty" defense used elsewhere against coupling risk | MEDIUM |
| DAM coupling worst-case impact (20-40% of DAM share) volunteered once in opening remarks, not repeated or effectively denied ("I don't see any loss") when an analyst asked the identical question directly later in the same session; appears in no audited filing | MEDIUM |
| Green market growth decelerated from +23% (FY26) to +6.3% (Q1FY27) to -1.2% (June, filed three weeks before the call), and the 24-Jul-2026 call describes green as "again become substantial" without naming the deceleration visible in the company's own most recent filing at the time | MEDIUM |
| Non-operating share of consolidated PBT rose from 23.4% (FY26, computed: other income Rs131.30cr + share of associate profit Rs19.80cr = Rs151.10cr of Rs645.56cr PBT) to 29.8% (Q1FY27, computed: Rs44.93cr + Rs7.72cr = Rs52.65cr of Rs176.80cr PBT), never raised by management or by any analyst in four transcripts | LOW |
| Admitted-but-unquantified fee incentives on TAM and REC contracts (Q1FY27 p.41-42) sit beside "asset light high-margin platform business" framing (Q1FY27 p.28) in the same call, without reconciliation | LOW |
| Three 2023 product launches (HP-DAM, HP-TAM, Ancillary Market) are management-admitted failures for want of liquidity (Q1FY27 p.12), a fact never connected by management to the credibility of the three further pending product launches the growth case leans on | LOW |
