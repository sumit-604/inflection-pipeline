# STAGE 12 VERIFIER B: CONCALL RED FLAGS (PHASE 1) - AWFIS

Run date: 2026-09-19. Model: claude-opus-5. Fresh context. Inputs read: 4 Awfis
transcripts (Nov-2025 Q2 FY26, Feb-2026 Q3 FY26, May-2026 Q4 FY26, Aug-2026 Q1 FY27),
12 peer transcripts (Smartworks x4, Indiqube x4, DevX x4), B05 report, B06 report.

Anchor convention: (call, speaker, PDF page) where PDF page = the `[page N]` marker in
the page-marked .txt beside each PDF. Awfis files: `runs/awfis-2026-09-19/inputs/concalls/Concall_<Mon>_<YYYY>_Transcript.pdf`.
Peer files: `runs/awfis-2026-09-19/inputs/peer-concalls/<PEER>-Concall_<Mon>_<YYYY>_Transcript.pdf`.
Arithmetic done by this verifier on transcript figures is labelled [INFERENCE].
Source-fidelity of individual numbers is Verifier A's domain; this stage judges
signal, weight and classification only.

---

## PART 1: INDEPENDENT RED-FLAG LIST (read from raw transcripts before opening B05/B06)

Severity per the Stage 12 scale. Material = CRITICAL + MAJOR.

### 1. [CRITICAL] Repeated evasion on unit realization and cohort economics (3 of 4 calls)
- Nov-2025: asked for mature vs new-centre margin split, Sumit Lakhani: "we are currently
  not sharing that data point. Probably we can look at sharing that data point on an annual
  basis" (Nov-2025, Lakhani, p.10). The annual call (May-2026) did not disclose it.
- Feb-2026: Yashowardhan Agarwal says depreciation per seat is up "versus our revenue per
  seat has been constant" and asks why margins are not rising (Feb-2026, p.16). Ravi Dugar
  answers only the depreciation half; revenue per seat is not addressed (Feb-2026, Dugar,
  p.16). The same analyst's new-seat occupancy arithmetic is met with "can you explain how
  you are figuring out the occupancy for the new seats?" (Feb-2026, Lakhani, p.15).
- Aug-2026: Shrenik Mehta notes chargeable area +68% vs revenue +65% over eight quarters and
  asks for per-seat pricing by year. Lakhani: "I don't have a clear number, but ... it would
  look very healthy" (Aug-2026, Lakhani, p.14).
- Meanwhile the premiumization thesis rests on an unquantified claim: new ultra-premium
  assets "expected to command pricing which is 30% to 50% higher" (Aug-2026, Ramani, p.4).
- Peer contrast: every peer answers the same question with a number. Smartworks Rs173/sqft
  (Aug-2025, Tapuriah, p.14), Rs175 vs Rs160-165 a year earlier (Nov-2025, Tapuriah, p.22),
  Rs181 vs Rs170 (Jul-2026, Tapuriah, p.13 and p.16); Indiqube Rs192 (May-2026, Das, p.15);
  DevX Rs7,500-8,000 per seat (Nov-2025, Uttamchandani, p.14).
- Why it is load-bearing: the transition thesis (value to premium rung) is a realization
  claim. The one metric that would prove it has been withheld three times, and one
  promised disclosure lapsed.

### 2. [MAJOR] Churn: denial in Feb, volunteered high run-rate in Aug
- Feb-2026: analyst computes 45,000 seats sold in 9M vs ~16,000 net occupied-seat gain and
  asks whether churn is high. Lakhani: "No, it is more of a function that most of the seats
  were added around in Q4 of last financial year" (Feb-2026, Lakhani, p.15-16).
- Aug-2026: Lakhani volunteers "in a business of our scale, 1.5% to 2% of inventory
  naturally churns every month" (Aug-2026, Lakhani, p.8). That is 18-24% a year [INFERENCE:
  x12].
- FY26: 58,000 seats sold (May-2026, Ramani, p.6) against occupied seats rising only ~20,800
  (135,000 x ~73% to 157,000 x 76%, occupancy on operational seats per May-2026, Lakhani,
  p.12; +300bps over four quarters per p.8) [INFERENCE]. Roughly 37,000 sold seats did not
  show up as net occupancy.
- Peer contradiction: Indiqube retention >95% and "attrition ... negative" (Feb-2026, Das,
  p.12; Aug-2026, Das, p.15); DevX 99.7% retention (May-2026, Uttamchandani, p.6). Awfis
  frames 1.5-2% a month as the natural state of the industry; two of three peers report
  the opposite.

### 3. [MAJOR] Cash-rent reconciliation asked in three calls, never fully answered
- Nov-2025: Chintan Sheth asks for the profit-share number "which typically I had asked on
  every quarter call" (Nov-2025, p.13). Dugar gives a combined Rs56cr variable figure
  mixing MA payouts, profit share and short leases (Nov-2025, Dugar, p.14).
- May-2026: Shrinjana Mittal: normalized-P&L rent ~Rs350cr vs cash-flow rent ~Rs412cr, gap
  widened from ~Rs20cr in H1 despite an earlier assurance it would not widen. Rochlani:
  "We do have a reconciliation and we can connect on this one-on-one" (May-2026, Rochlani,
  p.19).
- Aug-2026: Shamit Ashar: rental payments Rs85cr to Rs130cr QoQ on 3,000-4,000 net seats.
  Answer: part of rent sits in other expenses and is flat; growth "in line with the growth
  in the indices" (Aug-2026, Rochlani, p.10-11).
- Same quarter, the company introduces cash EBITDA which "deduct[s] the actual cash lease
  rentals paid" (Aug-2026, Rochlani, p.10), a de-facto concession that the normalized basis
  overstated cash.

### 4. [MAJOR] Headline profit metric switched in the quarter the margin promise fell due
- Nov-2025: FY26 normalized margin "stable between 14% to 15%. Next financial year, we
  expect a kind of a positive upside on the margins" (Nov-2025, Lakhani, p.8). Delivered
  FY26 normalized 14.3% (May-2026, Rochlani, p.11).
- Aug-2026: cash EBITDA introduced "from this quarter onwards" (Aug-2026, Rochlani, p.9);
  FY27 guided only on cash EBITDA Rs190-200cr (Aug-2026, Ramani, p.7), implied ~10-11%.
  No FY27 normalized-basis figure is given. The Nov promise can no longer be tested on the
  metric it was made on.
- Size of the basis gap [INFERENCE]: Q1 FY26 normalized EBITDA = H1 Rs100cr minus Q2 Rs52cr
  = Rs48cr (Nov-2025, Dugar, p.6); Q1 FY26 cash EBITDA implied = Rs44cr / 1.34 = ~Rs33cr
  (Aug-2026, Rochlani, p.10). About 4 margin points separate the two bases.

### 5. [MAJOR] FY27 revenue guidance cut within one quarter, unacknowledged
- May-2026: coworking 25-27%, Transform 22-25%, total ~25-27% (May-2026, Ramani, p.15 and
  corrected text p.17). Aug-2026: coworking 23-25%, Transform ~20%, "past INR1,800 crores"
  (Aug-2026, Ramani, p.7). Rs1,493cr x 1.25 = Rs1,866cr; Rs1,800cr = +20.6% [INFERENCE].

### 6. [MAJOR] FY26 seat guidance cut twice, plus a specific exit-March miss
- 40,000 gross original to 32,000-33,000 (Feb-2026, Lakhani, p.13) to 30,000 gross / 22,000
  net delivered (May-2026, Ramani, p.14).
- Feb-2026: "The 1,52,000 seats will be closer to 1,66,000 seats at the exit of March '26"
  (Feb-2026, Ramani, p.11). Actual operational 157,000 (May-2026, Ramani, p.14).

### 7. [MAJOR] Centre-closure baseline broken twice
- Nov-2025: "every year, there could be two or three centers that will get closed down"
  (Nov-2025, Ramani, p.10); Q2 closures ~900 seats (Nov-2025, Dugar, p.12).
- FY26 actual: 8,000 seats closed (May-2026, Ramani, p.14). Then "5% is not the kind of a
  churn which we would look at" (May-2026, Lakhani, p.19).
- Q1 FY27: "approximately 4,600 gross seats against roughly 1,800 seats exited as part of
  our portfolio consolidation" (Aug-2026, Lakhani, p.8). 1,800 x 4 / 157,000 = 4.6%
  annualised [INFERENCE], i.e. the FY26 rate is repeating.

### 8. [MAJOR] Managed Aggregation stance changed three times
- "no change in terms of strategy", ~65% MA in pipeline (Nov-2025, Lakhani, p.7); "the MA
  straight lease mix, we don't anticipate changing ... 65-35" (Nov-2025, Ramani, p.12).
- 62% (Feb-2026, Kashyap question, p.13). "maintain the ratio in the 60-40 kind of a range"
  (May-2026, Ramani, p.15). 57% and "We are not fixated on the MA split" (Aug-2026, Ramani,
  p.11). MA is the asset-light basis of the ROCE claim.

### 9. [MAJOR] Occupancy and margin inflection deferred in every call
- Nov: margins improve "after maybe five or six quarters" (Dugar, p.12-13) vs "next
  financial year" (Lakhani, p.8), same call. Feb: blended and 12M+ occupancy up "in the next
  one or two quarters", 12M+ +100-150bps (Lakhani, p.9); margin "uptick in the coming
  quarters" (Dugar, p.16). May: 12M+ "a couple of 100 basis point increase over the next
  couple of quarters" (Lakhani, p.13); margin "serious kind of uptake" over 2-3 years
  (p.13). Aug: blended flat 76%, 12M+ down to 83% (Lakhani, p.8); "Q4 is one quarter where
  you will at least start seeing a meaningful difference" (Lakhani, p.16).

### 10. [MAJOR] Large client exit likely known at the May call but not disclosed
- Aug-2026: a client with ~3,000 seats across five centres consolidated into conventional
  office "in May 2026, following its acquisition by a multinational company roughly 15
  months ago" (Aug-2026, Lakhani, p.8).
- May-2026 call (25-May-2026): no mention; instead mature-cohort improvement of "a couple of
  100 basis point" promised (May-2026, Lakhani, p.13).
- Two readings. (a) Notice was served before 25-May; Smartworks says large clients carry a
  "six to eight-month notice period" (Smartworks Jan-2026, Sarda, p.14). Then the May promise
  was made knowing a ~2% occupancy hit was coming. (b) Notice was short and the exit landed
  after the call; Indiqube notice periods are "60 going up to 90 days" (Indiqube Aug-2026,
  Das, p.15). The separating observation: the date notice was served by that client. Ask
  the company (Claude web / operator), NOT FOUND in transcripts.

### 11. [MAJOR] Transform FY26 guidance affirmed, then missed one quarter later
- Nov-2025: "we remain confident of meeting our full year guidance" (Ramani, p.4); "this a
  little bit of a blip is more of a quarterly thing ... the guidance for the year remains
  the same" (Ramani, p.9); "fairly confident around on ... the whole annual numbers"
  (Lakhani, p.15). Feb-2026: "the design and build business ... is an area where the
  guidance is not going as per plan" (Lakhani, p.14-15).

### 12. [MAJOR] Capital intensity rising while the capital-light narrative intensifies
- Capex unchanged despite the seat cut 40k to 32k (Feb-2026, Telisara question and Lakhani
  answer, p.16). FY27: 22,000-25,000 gross seats at capex "almost on similar lines of FY '26"
  (May-2026, Lakhani, p.13), Rs200-210cr (Aug-2026, Ramani, p.12).
- Capex per gross seat: FY26 Rs208cr / 30,000 = ~Rs69,000 (May-2026, Rochlani, p.11);
  FY27 Rs200-210cr / 22,000-25,000 = ~Rs80,000-95,000 [INFERENCE]; +15% to +38%.
- Developer partnership sold as "materially lower net capital intensity" (May-2026, Ramani,
  p.5) and "low balance sheet drag" (Aug-2026, Ramani, p.5), yet "our capital contribution
  ranges from around 50-odd-percent of the overall fit-out value" (Aug-2026, Lakhani, p.13).

### 13. [MAJOR] Peer contradiction on the 2021-lease-reset margin excuse
- Awfis Aug-2026: H1 margin pressure because 2021-signed leases hit a "commercial reset ...
  after five years", with "three quarters to four quarters of a timing difference" before
  pass-through (Aug-2026, Lakhani, p.17).
- Smartworks treats the same 2020-21 vintage as an upside: clients "paying at a number which
  is below what others are paying" are repriced or churned by choice (Nov-2025, Sarda,
  p.17); "we were able to reprice some of the deals that were there in COVID" (Jan-2026,
  Sarda, p.12); "customers who came in 4-5 years ago at a slightly lower base ... we are
  going ahead and churning them out" (Jul-2026, Sarda, p.11).
- Indiqube: landlords 14-15% every 36 months vs clients 5-6% annually, a ~1 point margin
  tailwind (Nov-2025, Das, p.6 and p.11). DevX: landlord 4-5% on ~Rs40 rent vs client 5-6% on
  ~Rs110 revenue (Feb-2026, Uttamchandani, p.10).
- Awfis's own average client tenure is 37-38 months (May-2026, p.8; Aug-2026, p.8), so most
  2021 clients should already have rolled to current pricing [INFERENCE]. The excuse is
  company-specific at best.

### 14. [MINOR] Retail/hospitality expansion walked back and the earlier statement denied
- "The business now aims to expand beyond workplace design and build into new segments such
  as retail, hospitality and institutional projects" (Nov-2025, Ramani, p.4). Feb-2026: "I
  do not think we said that we would immediately move into these categories" (Lakhani,
  p.17).

### 15. [MINOR] Tenure figures inconsistent within and across calls
- Feb-2026: average client tenure 37 months, lock-in 26 (Lakhani, p.7) vs "the tenure for the
  overall portfolio is 32 months" (Ramani, p.10). >100-seat lock-in 30 months (Nov-2025, p.6)
  vs 37 months (Feb-2026, Ramani, p.10).

### 16. [MINOR] Transform margin quoted on shifting bases
- "close to 7% to 8% ... net margins" (May-2026, Rochlani, p.12) vs "15% gross margin ...
  18% to 20% ... 17% to 18%" (Aug-2026, Ramani, p.15). DevX's D&B subsidiary runs 7.2%
  EBITDA (DevX May-2026, p.6), which sits with the May figure.

### 17. [MINOR] Headline ROCE drifting down, basis never stated
- 65% annualised (Nov-2025, Dugar, p.7) to 60% (May-2026, Rochlani, p.11) to 55%
  (Aug-2026, p.4, p.10). Smartworks reports Ind AS ROCE 58% beside normalized 13%
  (Aug-2025, Sarda, p.3), later 21.5% normalized (Jul-2026, p.5). Indiqube 23% excluding
  lease liabilities (Feb-2026, p.3 and p.5). Awfis's figure sits at the Ind AS-inflated level.

### 18. [MINOR] CFO change announced, no reason given (Feb-2026, Ramani, p.3). No analyst asked.
### 19. [MINOR] Filed May transcript edits two guidance numbers mid-text (May-2026, p.17).
### 20. [MINOR] Capex guide recalled inconsistently: "around INR220 crores" vs initial 180-200 (Nov-2025, Dugar, p.15); "we had given a guidance of Rs.200 to Rs.210 crores" (Feb-2026, Dugar, p.12).
### 21. [MINOR] Seat arithmetic confusion over gross vs net (May-2026, Ramani/Lakhani, p.14).
### 22. [MINOR] GCC ecosystem revenue "$100 billion" (Aug-2026, Ramani, p.3) and "$100 million" (Aug-2026, Ramani, p.15) inside the same call; also "$100 million" in May-2026 (p.4).
### 23. [MINOR] Frame furniture: "next 3 to 6 months" (Nov-2025, p.11), "nascent" (Feb-2026, p.18), 2-3 mandates by H2 (May-2026, p.7), absent in Aug-2026.
### 24. [MINOR] Net debt/equity swings unexplained: -0.18 (Nov-2025, p.7), -0.06 (Feb-2026, p.8), -0.20 (May-2026, p.11), -0.08 (Aug-2026, p.7 and p.10).
### 25. [MINOR] FY27 cash EBITDA guide stated two ways in one call: Rs190-200cr (Aug-2026, Ramani, p.7) vs Rs195-200cr (Aug-2026, Lakhani, p.17).

Totals: 25 items. Material 13 (1 CRITICAL, 12 MAJOR). Minor 12.

---

## PART 2: COMPARISON AGAINST THE PIPELINE (B05, B06)

### 2A. My items vs pipeline

| # | Item | Sev | Status | Where the pipeline has it / gap |
|---|---|---|---|---|
| 1 | Realization / cohort-economics evasion (Nov, Feb, Aug) | CRITICAL | MISSED | B05 4A lists realization as a confirm signal but never flags the repeated refusals; 2E tracks MA and margin-timing only. B06 never contrasts peer Rs/sqft disclosure. |
| 2 | Churn denial (Feb) vs 1.5-2%/month admission (Aug); 58k sold vs ~21k net occupied | MAJOR | MISSED | B05 has the 3,000-seat exit and 8,000 closures, not the monthly churn statement or the Feb denial. B06 claim 4 lists peer churn but not Awfis's figure. |
| 3 | Cash-rent reconciliation, three calls | MAJOR | PARTIALLY CAUGHT | B05 2B and 3C capture May and Aug individually; not linked as repeated, absent from the 4D red-flag table. |
| 4 | Metric switch to cash EBITDA as margin promise fell due | MAJOR | PARTIALLY CAUGHT | B05 header separates the three metrics and 1B lists the cash guide; no flag that the Nov promise became untestable. |
| 5 | FY27 guide cut in one quarter | MAJOR | CAUGHT | B05 1C, 2A row 6, 4D HIGH. |
| 6 | FY26 seat guide cut twice | MAJOR | CAUGHT | B05 2A row 1, 4D MEDIUM (the 166k exit-March line not cited, immaterial). |
| 7 | Closure baseline broken | MAJOR | PARTIALLY CAUGHT | B05 2A row 7 and 4D MEDIUM, but the outcome evidence is the 3,000-seat client exit (an occupancy event), not the 1,800 seats exited (the closure event, Aug p.8). Nov "2-3 centres" baseline missed. |
| 8 | MA stance x3 | MAJOR | PARTIALLY CAUGHT | B05 1C, 2A row 8, 2E all correct; graded LOW in 4D, under-weighted for an LBF2 item. |
| 9 | Occupancy/margin inflection deferred every call | MAJOR | CAUGHT | B05 2A row 3, 2E row 2 ("Deflected every time"), 4D LOW. |
| 10 | Client exit likely known at May call | MAJOR | MISSED | B05 2B and 2C treat the Aug disclosure as "the strongest transparency evidence". The credit is overstated until the notice date is known. |
| 11 | Transform FY26 affirm-then-miss | MAJOR | CAUGHT | B05 2A row 2, 2B. |
| 12 | Capital intensity rising | MAJOR | PARTIALLY CAUGHT | B05 4A row 4 names "straight-lease capex intensity keeps rising" as a kill signal; no per-seat computation; developer-partnership 50% fit-out contribution not noted. |
| 13 | Peer contradiction on 2021 reset | MAJOR | PARTIALLY CAUGHT | B06 claim 4 cites Smartworks COVID-vintage repricing; claim 7 still returns UNVERIFIABLE and says no peer speaks to it. The facts were in hand; the verdict is wrong in direction. |
| 14 | Retail/hospitality walk-back | MINOR | MISSED | |
| 15 | Tenure inconsistency | MINOR | MISSED | |
| 16 | Transform margin basis shift | MINOR | MISSED | |
| 17 | ROCE drift and peer basis | MINOR | PARTIALLY CAUGHT | B05 flags undefined ROCE vs AR 11.87%; the downward drift and peer basis evidence are not used. |
| 18 | CFO change unexplained | MINOR | CAUGHT | B05 2D. |
| 19 | Transcript-edited guidance | MINOR | CAUGHT | B05 2C. |
| 20 | Capex recall drift | MINOR | CAUGHT | B05 1C. |
| 21 | Seat arithmetic confusion | MINOR | CAUGHT | B05 3C. |
| 22 | GCC $ statistic | MINOR | CAUGHT | B05 3B, B06 claim 1 (both in the Aug call itself, not only across calls). |
| 23 | Frame slip | MINOR | CAUGHT | B05 1C, 2A row 9. |
| 24 | Net debt/equity swings | MINOR | MISSED | |
| 25 | Cash EBITDA guide two ways | MINOR | MISSED | B05 1B quotes Rs195-200cr and attributes it to Ramani p.6; Ramani said Rs190-200cr (p.7). |

Counts: CAUGHT 10, PARTIALLY CAUGHT 7, MISSED 8.
Material: 13 found; 4 fully caught + 6 partially caught = 10 held by the pipeline; 3 missed
(1 CRITICAL, 2 MAJOR).

### 2B. Pipeline flags I did not independently raise, or that I assess differently

| Pipeline flag | Assessment | Evidence |
|---|---|---|
| B05 4D HIGH: undefined 60%+ ROCE vs AR 11.87% | SUPPORTED (transcript half) | Headline repeated undefined in every call (item 17). The 11.87% is AR-sourced, outside this verifier's inputs. Peer corroboration: Smartworks' Ind AS ROCE 58% beside normalized 13% (Aug-2025, p.3). |
| B05 4D MEDIUM: 5% churn reassurance broken next quarter | SUPPORTED, mis-evidenced | Correct evidence is the 1,800 seats exited (Aug-2026, p.8), ~4.6% annualised. The 3,000-seat client exit is an occupancy event and does not remove seats. |
| B05 4D MEDIUM: GST SCNs and D&B transfer never raised | GST: SUPPORTED (absent from all four calls). D&B transfer: OVERSTATED | Subsidiarisation was volunteered (Nov-2025, Ramani, p.4), questioned on capital allocation and overhead split (Nov-2025, Choudhary/Ramani, p.8) and referenced again (Feb-2026, p.17). Only the consideration and valuation were never discussed. |
| B05 2C: Q1 FY27 client-exit disclosure = "strongest transparency evidence" | OVERSTATED | See item 10. Two readings; unresolved until notice date is known. |
| B05 4D LOW: MA stance; GCC stat; occupancy flat | SUPPORTED (MA under-weighted, see item 8) | |
| B06 claim 5 VERIFIED: Awfis cash margin "roughly half the peer band" | OVERSTATED (basis mismatch) | Smartworks "normalized EBITDA" and Indiqube "EBITDA" are post-rent, pre-depreciation, pre-ESOP-adjustment metrics. Their like-for-like at Awfis is normalized EBITDA 14.3% FY26 (May-2026, p.11), not cash EBITDA 10.1%. Indiqube's "we are at about 21%" is EBITDA (Nov-2025, Das, p.6); Indiqube cash EBIT was ~17% and differs from EBITDA through pre-operative rent capitalisation (Nov-2025, Agarwal, p.12). DevX IGAAP consolidated EBITDA 23.2% (Aug-2026, p.3). Like-for-like gap is ~2-9 points, and Awfis consolidates ~17% of revenue from D&B at 7-8% net (May-2026, p.12). The gap is real; "half" is a basis error that feeds LBF1 and Stage 11. |
| B06 claim 4 CONTRADICTED (occupancy) | SUPPORTED directionally | Smartworks operational 81% vs Awfis 76% is a 5-point gap, below B06's "6-16 points"; B06 mixes Smartworks committed and operational occupancy. |
| B06 claim 7 UNVERIFIABLE (lease-reset lag) | Should read CONTRADICTED (directional) | See item 13. |
| B06 claim 3: MA decline "reads like convergence" | OVERSTATED (soft) | Awfis itself says "This is not a shift from MA" (Aug-2026, p.12); no transcript frames the drift as convergence. A benign-reading label without evidence. |
| B06 claim 5 note: Indiqube Q3 cash EBIT "deferred to year-end per auditor" | MISATTRIBUTED | The deferral was OCF and capex, not cash EBIT (Indiqube Feb-2026, Agarwal, p.6 and p.8). |
| B06 2B, 2E (input costs, AI headcount risk not named by Awfis) | SUPPORTED | Awfis frames AI only as a tailwind (May-2026, p.3-4). |

No pipeline flag is NOT SUPPORTED outright. Three are OVERSTATED with decision weight
(B06 claim 5, B05 transparency credit, B05 D&B-transfer silence wording).

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| Row | Earlier call contains the promise? | Later call shows the outcome? | Verdict |
|---|---|---|---|
| 1: 40k seats FY26 | Yes, referenced as original guide (Feb-2026, Lakhani, p.13) | Yes, 30k gross / 22k net (May-2026, Ramani, p.14) | CONFIRMED |
| 3: occupancy +100-150bps mature in 1-2 qtrs | Yes (Feb-2026, Lakhani, p.9) | Yes, 12M+ ~84% flat, blended 76% (May-2026, Lakhani, p.8) | CONFIRMED |
| 4: FY26 capex Rs200-210cr | Yes (Feb-2026, Dugar, p.12; B05 cites p.11) | Yes, Rs208cr (May-2026, Rochlani, p.11) | CONFIRMED (anchor off by one page) |
| 5: normalized margin 14-15% FY26 | Yes (Nov-2025, Lakhani, p.8) | Yes, 14.3% (May-2026, Rochlani, p.11) | CONFIRMED |
| 7: "5% not the kind of churn" | Yes (May-2026, Lakhani, p.19) | The cited outcome (3,000-seat client exit) is not a closure; the right evidence is 1,800 seats exited (Aug-2026, p.8) | WRONG as written; direction survives on corrected evidence, one quarter only |
| 8: MA ~65:35 | Yes (Nov-2025, Lakhani p.7; Ramani p.12) | Yes, 57% (Aug-2026, Ramani, p.11) | CONFIRMED |

Checked 6, confirmed 5, wrong 1.

---

## PART 4: CREDIBILITY GRADE

B05 grade C (Mixed), weights 35/45/20. Verdict: would grade LOWER. The one offsetting
positive B05 relies on (proactive client-exit disclosure) is unresolved (item 10). B05 also
missed a three-quarter evasion on realization (item 1) and a Feb churn denial later
contradicted by management's own number (item 2). The balance-sheet strength B05 credits
is real but is not a credibility input. Stage 13 decides whether C-minus changes the 4D
weights; this verifier does not set them.

---

## PART 5: CONSOLIDATED FINDINGS

| ID | Sev | Finding | Anchor |
|---|---|---|---|
| F1 | CRITICAL | B05 missed a repeated (3-call) evasion on per-seat realization and cohort margins; one promised annual disclosure lapsed; peers all disclose. | Nov-2025 p.10; Feb-2026 p.15-16; Aug-2026 p.14; peers Smartworks Nov-2025 p.22, Jul-2026 p.13, Indiqube May-2026 p.15 |
| F2 | MAJOR | B05 missed the churn contradiction (Feb denial vs Aug 1.5-2%/month). | Feb-2026 p.15-16; Aug-2026 p.8; May-2026 p.6 |
| F3 | MAJOR | B05 missed the likely-known client exit at the May call and over-credits the Aug disclosure. | Aug-2026 p.8; May-2026 p.13; Smartworks Jan-2026 p.14; Indiqube Aug-2026 p.15 |
| F4 | MAJOR | B06 claim 5 compares peer post-rent EBITDA with Awfis cash EBITDA; like-for-like gap is ~2-9 points, not "half". | May-2026 p.11; Indiqube Nov-2025 p.6, p.12; Smartworks Jul-2026 p.3; DevX Aug-2026 p.3 |
| F5 | MAJOR | B06 claim 7 should be a directional contradiction; peers treat 2020-21 vintage as repricing upside. | Aug-2026 p.17; Smartworks Nov-2025 p.17, Jan-2026 p.12, Jul-2026 p.11; Indiqube Nov-2025 p.11 |
| F6 | MAJOR | Cash-rent questions across three calls not linked or elevated to 4D. | Nov-2025 p.13-14; May-2026 p.19; Aug-2026 p.10-11 |
| F7 | MAJOR | Metric switch to cash EBITDA not flagged; Nov FY27 margin promise now untestable on its own basis. | Nov-2025 p.8; Aug-2026 p.7, p.9-10 |
| F8 | MAJOR | MA stance change graded LOW; it underpins the asset-light ROCE claim (LBF2). | Nov-2025 p.7, p.12; May-2026 p.15; Aug-2026 p.11 |
| F9 | MAJOR | Closure-promise outcome mis-evidenced; Nov "2-3 centres a year" baseline missed. | Nov-2025 p.10; May-2026 p.14, p.19; Aug-2026 p.8 |
| F10 | MAJOR | Capex per gross seat rising 15-38% into FY27 and 50% fit-out share in developer deals not computed or flagged. | Feb-2026 p.16; May-2026 p.11, p.13; Aug-2026 p.12-13 |
| F11 | MINOR | B05 "D&B transfer never raised" overstated; subsidiarisation discussed Nov and Feb. | Nov-2025 p.4, p.8; Feb-2026 p.17 |
| F12 | MINOR | FY27 cash EBITDA guide misquoted as Ramani Rs195-200cr; Ramani said Rs190-200cr, Lakhani Rs195-200cr. | Aug-2026 p.7, p.17 |
| F13 | MINOR | B05 page anchors mix internal transcript pagination with PDF pages (Aug guidance p.6 is PDF p.7; May corrected guide p.16 is p.17; Nov capex p.13 is p.15; Feb capex p.11 is p.12). Verifier A should re-check. | as listed |
| F14 | MINOR | Retail/hospitality walk-back and denial missed. | Nov-2025 p.4; Feb-2026 p.17 |
| F15 | MINOR | Tenure inconsistencies missed. | Nov-2025 p.6; Feb-2026 p.7, p.10 |
| F16 | MINOR | Transform margin basis shift (7-8% net vs 17-18% gross) missed. | May-2026 p.12; Aug-2026 p.15 |
| F17 | MINOR | ROCE downward drift and peer basis evidence not used. | Nov-2025 p.7; May-2026 p.11; Aug-2026 p.4; Smartworks Aug-2025 p.3 |
| F18 | MINOR | Net debt/equity swings unremarked. | Nov-2025 p.7; Feb-2026 p.8; May-2026 p.11; Aug-2026 p.10 |
| F19 | MINOR | B06 claim 4 gap to Smartworks is 5 points, and committed/operational bases are mixed. | Smartworks Jul-2026 p.6 |
| F20 | MINOR | B06 attributes Indiqube's Q3 disclosure deferral to cash EBIT; it was OCF/capex. | Indiqube Feb-2026 p.6, p.8 |
| F21 | MINOR | GCC $ inconsistency occurs inside the Aug call itself, not only across calls. | Aug-2026 p.3, p.15 |

Open items for Claude web (PENDING LIVE VERIFICATION, not reachable here):
- Notice date served by the ~3,000-seat client that exited in May 2026 (resolves F3).
- Any Awfis per-seat or per-sqft realization series in investor presentations (tests F1).

```yaml
stage: B12b
company: "AWFIS"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 25
caught: 10
partially_caught: 7
missed:
  - {severity: "CRITICAL", item: "Repeated 3-call evasion on per-seat realization and cohort margins; promised annual disclosure lapsed; all peers disclose Rs/sqft", anchor: "Nov-2025 Lakhani p.10; Feb-2026 Dugar/Lakhani p.15-16; Aug-2026 Lakhani p.14"}
  - {severity: "MAJOR", item: "Feb churn denial vs Aug volunteered 1.5-2% monthly churn (18-24%/yr); 58k seats sold vs ~21k net occupied gain FY26", anchor: "Feb-2026 Lakhani p.15-16; Aug-2026 Lakhani p.8; May-2026 Ramani p.6"}
  - {severity: "MAJOR", item: "3,000-seat client exit (May 2026) not disclosed at 25-May call while mature-cohort gain promised; two readings, separated by notice date", anchor: "Aug-2026 Lakhani p.8; May-2026 Lakhani p.13; Smartworks Jan-2026 p.14; Indiqube Aug-2026 p.15"}
  - {severity: "MINOR", item: "Retail/hospitality expansion stated then denied", anchor: "Nov-2025 Ramani p.4; Feb-2026 Lakhani p.17"}
  - {severity: "MINOR", item: "Tenure figures inconsistent within Feb call and vs Nov", anchor: "Nov-2025 p.6; Feb-2026 p.7, p.10"}
  - {severity: "MINOR", item: "Transform margin 7-8% net (May) vs 17-18% gross (Aug)", anchor: "May-2026 Rochlani p.12; Aug-2026 Ramani p.15"}
  - {severity: "MINOR", item: "Net debt/equity swings -0.18/-0.06/-0.20/-0.08 unexplained", anchor: "Nov-2025 p.7; Feb-2026 p.8; May-2026 p.11; Aug-2026 p.10"}
  - {severity: "MINOR", item: "FY27 cash EBITDA guide stated Rs190-200cr and Rs195-200cr in same call", anchor: "Aug-2026 Ramani p.7; Lakhani p.17"}
pipeline_flags_not_supported:
  - {status: "OVERSTATED", flag: "B06 claim 5 VERIFIED: Awfis cash margin roughly half peer band", reason: "basis mismatch; peers' post-rent EBITDA compares to Awfis normalized 14.3%, not cash 10.1%; like-for-like gap ~2-9 pts", anchor: "May-2026 p.11; Indiqube Nov-2025 p.6, p.12; Smartworks Jul-2026 p.3; DevX Aug-2026 p.3"}
  - {status: "OVERSTATED", flag: "B05 2C/2B: Q1 FY27 client-exit disclosure is strongest transparency evidence", reason: "exit likely known at May call; unresolved until notice date known", anchor: "Aug-2026 p.8; May-2026 p.13"}
  - {status: "OVERSTATED", flag: "B05 4D: D&B business transfer never raised on calls", reason: "subsidiarisation volunteered and questioned; only consideration/valuation absent", anchor: "Nov-2025 p.4, p.8; Feb-2026 p.17"}
  - {status: "WRONG VERDICT", flag: "B06 claim 7 UNVERIFIABLE (lease-reset lag)", reason: "peers describe 2020-21 vintage as repricing upside and escalation spreads as tailwind; directional contradiction", anchor: "Smartworks Nov-2025 p.17, Jan-2026 p.12, Jul-2026 p.11; Indiqube Nov-2025 p.11"}
promise_delivery_spot_checks: {checked: 6, confirmed: 5, wrong: 1}
credibility_grade_concur: "lower - C leans on a client-exit transparency credit that is unresolved, and misses a 3-call realization evasion and a contradicted churn denial"
findings:
  - {id: F1, severity: CRITICAL, finding: "B05 missed repeated realization/cohort-margin evasion across Nov, Feb, Aug", anchor: "Nov-2025 p.10; Feb-2026 p.15-16; Aug-2026 p.14"}
  - {id: F2, severity: MAJOR, finding: "B05 missed churn denial vs 1.5-2%/month admission", anchor: "Feb-2026 p.15-16; Aug-2026 p.8"}
  - {id: F3, severity: MAJOR, finding: "B05 missed likely-known client exit at May call; over-credits Aug disclosure", anchor: "Aug-2026 p.8; May-2026 p.13"}
  - {id: F4, severity: MAJOR, finding: "B06 claim 5 cash-margin comparison on mismatched bases", anchor: "May-2026 p.11; Indiqube Nov-2025 p.6, p.12"}
  - {id: F5, severity: MAJOR, finding: "B06 claim 7 verdict should be directional contradiction", anchor: "Aug-2026 p.17; Smartworks Nov-2025 p.17, Jul-2026 p.11"}
  - {id: F6, severity: MAJOR, finding: "Cash-rent questions in three calls not linked or elevated to 4D", anchor: "Nov-2025 p.13-14; May-2026 p.19; Aug-2026 p.10-11"}
  - {id: F7, severity: MAJOR, finding: "Metric switch to cash EBITDA not flagged; Nov FY27 margin promise untestable", anchor: "Nov-2025 p.8; Aug-2026 p.7, p.9-10"}
  - {id: F8, severity: MAJOR, finding: "MA stance change under-weighted as LOW", anchor: "Nov-2025 p.7, p.12; May-2026 p.15; Aug-2026 p.11"}
  - {id: F9, severity: MAJOR, finding: "Closure-promise outcome mis-evidenced; Nov baseline missed", anchor: "Nov-2025 p.10; May-2026 p.19; Aug-2026 p.8"}
  - {id: F10, severity: MAJOR, finding: "Rising capex per gross seat and 50% developer fit-out share not computed", anchor: "May-2026 p.11, p.13; Aug-2026 p.12-13"}
  - {id: F11, severity: MINOR, finding: "D&B transfer silence overstated", anchor: "Nov-2025 p.4, p.8; Feb-2026 p.17"}
  - {id: F12, severity: MINOR, finding: "Cash EBITDA guide misquoted/misattributed", anchor: "Aug-2026 p.7, p.17"}
  - {id: F13, severity: MINOR, finding: "B05 anchors mix internal and PDF pagination; Verifier A to re-check", anchor: "Aug-2026 p.7; May-2026 p.17; Nov-2025 p.15; Feb-2026 p.12"}
  - {id: F14, severity: MINOR, finding: "Retail/hospitality walk-back missed", anchor: "Nov-2025 p.4; Feb-2026 p.17"}
  - {id: F15, severity: MINOR, finding: "Tenure inconsistencies missed", anchor: "Feb-2026 p.7, p.10"}
  - {id: F16, severity: MINOR, finding: "Transform margin basis shift missed", anchor: "May-2026 p.12; Aug-2026 p.15"}
  - {id: F17, severity: MINOR, finding: "ROCE drift and peer basis evidence unused", anchor: "Nov-2025 p.7; Aug-2026 p.4; Smartworks Aug-2025 p.3"}
  - {id: F18, severity: MINOR, finding: "Net debt/equity swings unremarked", anchor: "Feb-2026 p.8; Aug-2026 p.10"}
  - {id: F19, severity: MINOR, finding: "B06 claim 4 Smartworks gap 5 pts; mixed occupancy bases", anchor: "Smartworks Jul-2026 p.6"}
  - {id: F20, severity: MINOR, finding: "B06 misattributes Indiqube Q3 deferral to cash EBIT", anchor: "Indiqube Feb-2026 p.6, p.8"}
  - {id: F21, severity: MINOR, finding: "GCC $ inconsistency occurs within Aug call itself", anchor: "Aug-2026 p.3, p.15"}
critical_count: 1
major_count: 9
minor_count: 11
material_found: 13
material_caught: 10
acceptance_rate: 77
coverage_basis: "13 material of 25 listed; 4 fully caught + 6 partially caught = 10 held; 3 missed (1 CRITICAL, 2 MAJOR). Strict full-catch rate 4/13 = 31%."
```
