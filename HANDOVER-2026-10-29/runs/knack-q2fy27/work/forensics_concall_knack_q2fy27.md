# A3 FORENSIC NOTES: KNACK Q2 FY27 (doctype: concall)

Source tier: ASR machine transcript (faster-whisper small.en). Management tier. Every number is unverified and may be misheard. Speakers inside Q&A are not identified. A number carrying A1's ASR_DOUBT flag is tagged [ASR_DOUBT]. Other numbers are tagged [ASR]. Derived figures are arithmetic on stated numbers. They carry the weakest input's tier and are labelled DERIVED. No misheard number is resolved by guessing.

Inputs read: A1 structured (R001-R934), A1 fulltext lines 39-595 (read in full), A2 ledger (934 rows, 26 questions). Prior-quarter extract: none (first quarterly review). Monitoring checklist: coordinator watch list (PRE-THESIS READ; no Notion page, no companies/KNACK.md). Nothing under inputs/ was opened.

## LEDGER RECONCILIATION

- Rows in ledger: 934. Rows whose cited fulltext line was read: 934 (the cited lines run from 39 to 593, and all of lines 39-595 were read). Reconciled: 100%.
- Questions read at their turns: 26 of 26.
- Discrepancies found while reading (A2's ledger is not edited, only noted here):
  1. T10-Q3 ("what would be our capacity by next October", line 433) is coded NUMBER (69-72,000 MT). In T10, management never answers India capacity. The only capacity in the T10 reply is Mexico: "installed capacity is like a 400 ton metric ton" (line 462). The 69-72,000 figure comes from T06 (line 234). In T10 the question was effectively DEFLECTED. It was re-asked in T11 (lines 492-499), and the answer there gave a date ("October 27") but no tonnage.
  2. T11-Q2 (lost margin recovery, lines 476-477) is coded HEDGED. The answer (lines 478-487) moves to the Mexico greenfield ("installed capacity is only 400, 400 metric ton per month", line 482). It may answer a different entity. See C-A3-10.
  3. T05-Q4 is coded CONFIRMED (Q2 EBITDA/kg 36 vs 51.52). T12-Q3 has management stating Q1 54 and Q2 45 (lines 564-565). Management assented to two different Q2 baselines. See C-A3-02.
  4. Two A1 context strings cite input-line numbers, not file lines: R678 "reply line 348" means file line 386, and R928 "lines 373-374" means file lines 411-412. The row anchors themselves are correct.

## FINDINGS TABLE

| id | check | ledger row ref | line / turn | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| C-A3-01 | F6 | R662, R915, R663, R666, R918, R688 (T02, T03, T14) | 66-67, 94, 110-111, 588 | "we expect this to reflect in our realization from quarter 3 FI27 onwards subject to market condition stabilization" | FORWARD-SIGNAL | Q3 FY27 margin recovery is the call's one dated test. It is said four times, and conditions sit around it. The CFO's own lag is "a log of 1 or 2 water [quarter]" (line 110), which allows slippage to Q4. Polymer is "right now ... on peak" (line 539) at "160 rupees" (line 390) [ASR_DOUBT]. The biggest customer reprices quarterly on the prior quarter's average (lines 279-281), so the Q3 price reflects the Q2 average and not the Rs 160 spot. Tracker: score Q3 gross margin vs Q1, not vs Q2. |
| C-A3-02 | F6 / F14 | R685 (T12-Q3); R136-R138 (T05-Q4) | 570; 172-174; 562-565 | "54 can be achieved in the next two quarters" vs "currently 36 rupees versus last quarter we were doing at 51.52 rupees. Is it correct sir?" / "Yes, I am absolutely right" | AMBIGUOUS | The baseline for the one numeric margin commitment is unstable. Management assented to a Q2 EBITDA/kg of 36 (T05) and of 45 (T12). DERIVED: 49.77 cr / 11,252 MT = Rs 44.2/kg [ASR_DOUBT inputs]. The Rs 54/kg target means +22% from 45 or +50% from 36. A4 should ask which EBITDA definition and which tonnage the Rs 54/kg uses, and the Q1 and Q2 figures on that basis. |
| C-A3-03 | F14 | R053, R055, R071, R072, R095, R097 (T03) | 107-108, 113, 124 | "The Ibita margin was 16.35 percent against 19.25% a year ago" / "the pack margin for quarter was 8.22% compared with 10.34%" | AMBIGUOUS | DERIVED: both Q2 margins tie to a base of about Rs 304.4 cr (49.77/16.35% = 304.40; 25.02/8.22% = 304.38). Q2 revenue is Rs 294 cr (line 101). The H1 PAT margin ties to revenue (55.55/9.76% = 569.2 vs 569.11). So the Q2 margins appear to use total income, about Rs 10 cr above revenue (Q2 FY26 about Rs 6 cr). Two readings: (a) the reported Rs 49.77 cr EBITDA includes about Rs 10 cr other income (possibly treasury income on unspent IPO money), so the operating EBITDA margin is about 13.5%, not 16.35%; (b) the margins are a misheard pair. The separating observation is the other-income line in the results filing. Reading (a) also reconciles C-A3-02: Rs 44.2/kg less about Rs 9/kg of other income gives about Rs 35/kg, close to the 36 at line 173. |
| C-A3-04 | F14 | R105, R122, R169, R270 (11,252 stated four times); R179 [ASR_DOUBT]; R107, R156, R277 | 138-139, 232, 189, 376 | "this quarter we closed 11,252" / "we are at installed capacity of 42,000 metric tons annually" / "plant is almost utilized 90-91% capacity" | AMBIGUOUS | DERIVED: 11,252 MT x 4 = 45,008 MT annualised, which is 107% of 42,000 MT. At 90-91% of 42,000 MT, the quarterly figure would be about 9,500 MT. The candidate reconciling items are: the 5,040 MT added in August (line 142), the rented plant (line 495), outsourced or traded volume inside the sales figure, or a misheard 42,000. The utilisation denominator is unknown, so there is no basis for any headroom calculation. Ask: installed capacity at 30-Sep-2026 by plant, and whether sales tonnage includes bought-out or job-work volume. |
| C-A3-05 | F6 | R669, R683, R932, R684, R673, R674, R689 (T05, T06, T11, T14) | 142, 494-499, 229-237, 376, 589-590 | "October is our deadline for the expansion capacity in October 27" / "we have a limitation of our quantity because we are almost 89-91% we are utilizing" | FORWARD-SIGNAL | Until Oct 2027, tonnage headroom is only the 5,040 MT added in August [ASR_DOUBT unit] and a rented plant "in next one or two months" (line 496). The 30-32k MTPA expansion to "69 to 72,000" MT [ASR_DOUBT] lands in Oct 2027, with pinch machines on a 1-1.5 year delivery (line 236). Volume growth for H2 FY27 and H1 FY28 is capped. The interim lever is mix (PLWPP to pinch bottom, lines 378-379), not tonnes. Capex amount and funding were not stated. |
| C-A3-06 | F17 | R046, R272, R274, R127, R268 (T03, T05, T09) | 102, 363, 365-367, 166, 356 | "So the major chunk of price hike which is driving the revenue growth this quarter, right?" / "Right." | FORWARD-SIGNAL | DERIVED: revenue +52.5% YoY [ASR_DOUBT] on volume +13.3% YoY (11,252 vs 9,927 MT [ASR_DOUBT]). Realisation is Rs 261/kg vs Rs 195/kg, +34% YoY, and +4% QoQ against Q1 (10,940 MT, about Rs 275 cr). Most of the headline growth is polymer pass-through. It reverses when polymer falls, and underlying growth then converges on tonnage, which C-A3-05 caps. Management did not volunteer realisation per kg or the price/volume split. The analyst drew it out. |
| C-A3-07 | F6 | R031-R035, R301-R318 (RESTATED), R928, R691 (T02, T09-Q5) | 88-89, 398, 402-412 | "a new order and 3-year contract renewal worth about 150 crore per year" / "this is our existing customer" / "It is a minimum 150 crores" / "this is a three year contract" | AMBIGUOUS | The prepared remarks frame it as a new order. In Q&A it is an existing customer, earlier extended by one year, now for three. It was restated mid-answer from "150 crores every month" to "every year". The incremental revenue over the current run-rate is NOT DISCLOSED. DERIVED: a Rs 150 cr/yr floor is about 13% of H1-annualised revenue (569.11 x 2 = 1,138 cr). That is single-customer concentration (watch item 8). The customer may be the "biggest customer" on quarterly price revision (line 279); not confirmed. Ask: FY26 revenue from this customer; whether the minimum is value or volume; the pricing formula. |
| C-A3-08 | F6 | R680, R681, R931, R668, R075, R099 (T03, T10-Q2) | 114-115, 125-127, 454-456, 462-465 | "quarter four is our targeted to achieve this win-win situation, but not very committed" | FORWARD-SIGNAL | Mexico JV share of loss is Rs 2.62 cr in Q2 and Rs 6.06 cr in H1 [ASR_DOUBT]. DERIVED: the implied Q1 loss is Rs 3.44 cr, and the drag is about 10.5% of Q2 consolidated PAT. Breakeven needs about 120-130 MT/month against 400 MT installed. Q2 averaged about 80 MT/month (line 463). The same milestone carries two dates: Q3 "almost" (line 455) and Q4 "not very committed". Log Q4 FY27 as the dated test. A JV drag above 10% of PAT needs an F4 check on auditor scope in the results filing. |
| C-A3-09 | F7 | R927, R298, R933, R114, R922, R113 (T05, T09, T12) | 157, 386, 395, 551-553, 558-559 | "99 percent, we covered this everything" vs "in our cross margin there is an impact of the 7%" and "it is not 100% we can get it" | FORWARD-SIGNAL | The pass-through claim contradicts the reported 7% gross-margin hit [ASR_DOUBT] on a 26% RM rise [ASR_DOUBT]. Management's own illustration implies partial recovery: "i want to increase like a five percent but we can get the three percent or four percent" and "25 rupees per kg but they may be negotiate ... 22 20 rupees" (lines 551-553). That is 60-88% of the ask. At elevated polymer, percent gross margin is unlikely to return fully to Q1 levels. On conservative bias, read this as bear on the size of the Q3 recovery. |
| C-A3-10 | F7 | R679, R682 (T11-Q2) | 476-487 | "third quarter is definitely comes with the loss recovery of the very small portion, not much more as we expected" | AMBIGUOUS | The question was whether the lost (India) margin is recovered. The answer moves to the Mexico greenfield (400 MT/month, interest cost, lines 481-485). The size of the India margin recovery was asked three times (T09-Q4, T11-Q2, T12-Q2) and never quantified. A4 should ask again with a numeric frame: Q3 gross margin per kg vs Q1. |
| C-A3-11 | F7 | R158, R163, R148-R154, R194-R198 (T06-Q1 to Q4; T06-Q3 declined) | 186, 190-191, 209-210, 214-215, 241 | "We cannot say exactly what is the percentage of utilization of tinge water?" | AMBIGUOUS | Pinch bottom is the named margin lever ("increasing the share of value added", line 95). Its utilisation was given only as "60-65-70%" [ASR_DOUBT], then declined. Its capacity is called non-separable at the finishing stage (lines 209-210), yet later "32,000 out of 72,000" MT (line 241) [ASR_DOUBT]. Revenue share is 21% vs "17 or 18" last year (line 186) [ASR_DOUBT]. Without a pinch-bottom tonnage line, the mix-upgrade claim cannot be tracked. Ask for pinch-bottom tonnes per quarter. |
| C-A3-12 | F17 | R320-R330 (T10-Q1) | 425-441 | "the receivable cycle of this export is larger compared to domestic, so 55 crores investment is already increased" | FORWARD-SIGNAL | H1 OCF fell from Rs 39 cr to Rs 22 cr [ASR_DOUBT]. Inventory rose Rs 26.9 cr [ASR_DOUBT] and receivables Rs 55 cr [ASR_DOUBT]. Management's own cause (export share rising, export receivable cycle longer) is structural, not seasonal. The analyst asked "should this normalize" (line 428). No normalisation date was given. Expect working-capital intensity to rise with export mix. Receivable and inventory DAYS were not stated (watch item 7). |
| C-A3-13 | F8 | R332, R333, R334, R929, R930 (T10-Q1) | 442-449 | "effective tax rate is 25% so tax impact is similarly same" / "the IPO expense around ... 28 crores. So that has been eliminated from the security premium and that is also around the deferred tax consideration" | AMBIGUOUS | ETR 25% [ASR_DOUBT] is about equal to the statutory 25.17% (22% new regime plus surcharge and cess). There is no ETR anomaly. The analyst's "huge tax impact" on OCF (line 427) stays unexplained. An IPO cost charged to securities premium would normally lower cash tax through amortised deductions, not raise it. Ask: H1 cash tax paid vs P&L tax charge, and the deferred-tax entry taken through equity on the Rs 28 cr. |
| C-A3-14 | F17 | R092-R102, R910 (T03, T00) | 54-55, 117-118, 127-128 | "Key ratios about our balance" (line 127, sentence breaks off; line 128 is the moderator opening Q&A) | NEUTRAL-FACT | ASR/VAD gaps lose content. 00:01:22 to 00:01:55 (line 54) loses the Q2 headline. 00:09:18 to 00:09:56 (line 117) loses H1 EBITDA. At lines 127-128, the CFO's balance-sheet and key-ratio section is cut, and the moderator line runs 30 s for one sentence. 00:15:14 to 00:15:51, 00:26:15 to 00:26:50 and 00:29:55 to 00:30:33 are also lost. Silence on balance-sheet items (debt, cash, WC days, IPO proceeds) may be a transcript artefact, not management silence. Use the company-filed transcript before scoring any F17 row as confirmatory negative. |
| C-A3-15 | F17 | watch list items 2, 4, 6, 7, 8, 9 vs full transcript | 78, 82, 119-121, 436-439, 589 | "Our export market contributed a significant part of our revenue" (line 78, no figure) | AMBIGUOUS | Six watch items are unquantified on the call (table below). The count is 1 quarter each because this is the first review. Not yet a sustained-silence negative. Each becomes an A4 question. |
| C-A3-16 | F17 | R912, R062-R066, R088-R091 (T02, T03) | 55, 112, 122 | "all on year-on-year basis" (line 55) | NEUTRAL-FACT | Management framed every figure YoY. DERIVED: Q1 PAT = 55.55 - 25.02 = Rs 30.53 cr, so Q2 PAT is -18% QoQ on revenue +7% QoQ (about Rs 275 cr to Rs 294 cr) [ASR_DOUBT inputs]. The QoQ PAT fall was not discussed. A4 should carry the QoQ base into the results cross-check. |
| C-A3-17 | F6 | R686, R934 (T12) | 575-577 | "whatever we propose yearly is almost we can achieve it ... our target is we are on the track" | AMBIGUOUS | Management invokes an annual target but never quantifies it on the call (it may sit in the RHP or earlier commentary). An unquantified target cannot enter the promise-vs-delivery tracker. Ask for the FY27 target figure and its metric (revenue, volume or EBITDA). |

## CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall; A2 ZERO_STANDING = 0; no line-item template. |
| F2 Standalone vs consolidated | N.A. | Call gives consolidated only (R917, line 100). No standalone figures to decompose. JV share noted under C-A3-08 (about 10.5% of Q2 PAT, DERIVED). Run at the results filing. |
| F3 Shell-entity detection | N.A. | No standalone vs consolidated cost lines on a call. |
| F4 Unaudited contribution ratio | N.A. | No auditor Other Matters on a call. Flag for the results-filing A3: the Mexico JV share of loss is about 10.5% of Q2 PAT (C-A3-08), above the 10% line if it rests on unreviewed numbers. |
| F5 Going concern / EoM scope | N.A. | No EoM paragraph on a call; no prior quarter. |
| F6 Forward-commitment mining | FINDING | 17 commitments registered. Findings C-A3-01, 02, 05, 07, 08, 17. |
| F7 Hedge phrase mining | FINDING | "subject to market condition stabilization" (67), "under discussion" (152), "not very committed" (456), "not 100% we can get it" (559), "cannot say exactly" (214). Findings C-A3-09, 10, 11. |
| F8 Tax forensics | FINDING | ETR 25% matches statutory 25.17%. The OCF tax explanation does not tie (C-A3-13). |
| F9 OCI forensics | N.A. | No OCI on the call. |
| F10 Share count and dilution | N.A. | One EPS figure only (2.07, line 116 [ASR_DOUBT]); no basic vs diluted. DERIVED implied shares about 12.1 cr (25.02/2.07), for the A4 cross-check only. |
| F11 Reserves and net worth | N.A. | No net worth stated. ROE 19.11% and ROCE 28.76% (lines 118-119 [ASR_DOUBT]) only; the key-ratio section is lost (C-A3-14). |
| F12 Segment forensics | N.A. | No segment data. Pinch-bottom 21% revenue share is product mix, handled under C-A3-11. |
| F13 Board outcome | N.A. | No board items on the call. |
| F14 Drafting / internal inconsistencies | FINDING | Applied to internal consistency of the call: margin base (C-A3-03), volume vs capacity (C-A3-04), EBITDA/kg baseline (C-A3-02). Minor, ASR-likely and not findings: CFO named three ways (lines 46-47, 53, 98); SKUs "3974 ... up from ... 13500" (lines 76-77); "25 plus" vs "27" industries (lines 71, 304); 75 vs "more than 72" countries (lines 79, 297). |
| F15 Entity list diffs | N.A. | No consolidation list on a call; no prior quarter. JV name garbled ("SionNag TV" line 97, "STYM-9 JV" line 125). |
| F16 Presentation dropped/reframed | N.A. | Concall, not a deck; no prior call to diff. |
| F17 Silence audit | FINDING | Six watch items unquantified (C-A3-15); transcript gaps qualify the audit (C-A3-14); C-A3-06, 12, 16. |

## COMMITMENT REGISTER (F6)

First quarter on record, so no status transitions can be scored. Status words come from the transcript where the call uses one. "stated" means the call gives no status word.

| # | commitment | implied date | ref (turn / line / row) | status word |
|---|---|---|---|---|
| 1 | Cost pass-through reflects in realisation from Q3 FY27, "subject to market condition stabilization" | Q3 FY27 (Dec-2026 qtr) | T02 / 64-67 / R662, R915 | initiated ("initiated cost pass-through", line 66) |
| 2 | Restore EBITDA margin as pricing adjustments flow through | from Q3 FY27 | T02 / 94 / R663; T03 / 110-111 / R666; T14 / 588 / R688 | initiated |
| 3 | EBITDA per kg back to Rs 54 [ASR_DOUBT] (baseline disputed, C-A3-02) | Q4 FY27 ("next two quarters") | T12 / 570 / R685 | stated |
| 4 | Yearly target achievable, "on the track" (target not quantified) | FY27 | T12 / 575-577 / R686, R934 | stated |
| 5 | Improve margin further via higher value-added (pinch-bottom) share, cost control | FY27 onward, undated | T02 / 95-96 / R664 | stated |
| 6 | Q3 better in quantity, production and sales on the 5,040 MT [ASR_DOUBT] added in August | Q3 FY27 | T05 / 142-145 / R669 | completed (addition, Aug-2026); underway (ramp, "just starting to ramp up") |
| 7 | Q3 more commercial pinch-bottom sales, rice season orders | Q3 FY27 | T06 / 199-203 / R671, R672; T09 / 380-384 | underway ("increasing continuously") |
| 8 | Q3 and Q4 volume growth continues on contracted orders, incl. renewed international contract | H2 FY27 | T14 / 586-587 / R687; T09 / 374 / R676 | stated |
| 9 | Rented plant adds new capacity | Nov-Dec 2026 ("next one or two months") | T11 / 494-496 / R683, R932 | underway ("already into the ramp") |
| 10 | Expansion (+30-32k MTPA [ASR_DOUBT]) takes capacity to 69-72k MT [ASR_DOUBT]; "October is our deadline" | Oct-2027 | T06 / 229-234 / R673; T11 / 497-499 / R684 | underway ("good phase of the expansion level") |
| 11 | Two new pinch machines into production | Oct-2027 ("next year, October") | T06 / 236-237 / R674 | stated (delivery lead time 1-1.5 years) |
| 12 | Pinch-bottom at 25-30k MT of 72k [ASR_DOUBT], "later on 28" [ASR_DOUBT] | FY28 [ASR_DOUBT] | T06 / 241 / R675 | stated |
| 13 | New Gujarat plant: timely completion and utilisation the primary focus | through 2027 | T14 / 589-590 / R689 | stated |
| 14 | Mexico JV: Q3 near break-even (about 120 MT/month); Q4 target "not very committed" | Q3 FY27 / Q4 FY27 | T02 / 97 / R665; T10 / 454-465 / R680, R681, R931 | underway ("scale-up phase", line 125) |
| 15 | JV break-even reverses the drag on consolidated PAT margin | on JV break-even | T03 / 126-127 / R668 | stated |
| 16 | ROE and ROCE improve as IPO funds are deployed | "coming quarters" | T03 / 119-121 / R667, R920 | underway ("progressively deployed") |
| 17 | International contract: minimum Rs 150 cr/yr [ASR_DOUBT], 3 years; customer may add countries and varieties | signed 2-Oct-2026; runs about to FY30 | T02 / 88-89; T09 / 402-416 / R033, R301-R318, R691 | completed (contract signed) |

## WHAT WAS NOT DISCUSSED (F17 silence audit vs coordinator watch list)

Caveat C-A3-14: the transcript loses about 3.5 minutes across six gaps, including the CFO's balance-sheet section. Silence below is silence in the TRANSCRIPT. Consecutive quarters counts 1 for every row because this is the first review.

| watch item | on the call? | what was said / missing | consecutive quarters silent |
|---|---|---|---|
| 1 Volume (tonnes) | Addressed | 11,252 MT Q2; 10,940 MT Q1; 9,927 MT Q2 FY26 (lines 138, 166, 356) [ASR_DOUBT]. Only in Q&A, not in the prepared remarks. | 0 |
| 2 Realisation per kg | NOT DISCUSSED | No Rs/kg realisation and no price-hike % (asked lines 147-150; reply gives no figure). DERIVED only (C-A3-06). | 1 |
| 3 Polymer pass-through | Addressed | Contract share 45-50% (line 64), 1-1.5 month production lag, monthly/quarterly revision (lines 278-287), polymer path Rs 92 to 160 (lines 388-390). | 0 |
| 4 Export share | NOT DISCUSSED (quantum) | "significant part of our revenue" (line 78); "significantly higher export volume" (line 82); no %. | 1 |
| 5 Capacity utilisation | Addressed, base unclear | 90-91% overall (lines 139, 189); pinch bottom 60-70%, exact figure declined (lines 191, 214). Denominator conflict C-A3-04. | 0 |
| 6 New-capacity timeline (Units 4 and 5) | Partly | Oct-2027 deadline (line 499), 69-72k MT (line 234). Units 4 and 5 not named; capex amount, funding and spend to date not stated. | 1 (capex quantum) |
| 7 Receivable and inventory days | NOT DISCUSSED (days) | Rupee changes only: inventory +26.9 cr, receivables +55 cr (lines 436-439). No days. | 1 |
| 8 Customer concentration | NOT DISCUSSED | No top-customer or top-10 share. Implied single-customer floor about 13% of revenue (C-A3-07, DERIVED). | 1 |
| 9 IPO proceeds use | NOT DISCUSSED (quantum) | "funds where progressively deployed" (line 120); IPO expense 28 cr (line 447). No amount deployed, unspent balance or monitoring-agency status. | 1 |

Also absent from the transcript, outside the watch list: net debt or cash, H1 capex, other income (see C-A3-03), H1 EBITDA (lost in the gap at line 117).

```yaml
stage: A3-forensics
company: "KNACK"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/knack-q2fy27/work/forensics_concall_knack_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: FINDING
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "C-A3-01", check: "F6", line: "66-67, 94, 110-111, 588", classification: "FORWARD-SIGNAL", implication: "Q3 FY27 margin recovery is the dated test, conditioned on market stabilisation; CFO lag of 1-2 quarters and polymer at peak Rs 160 allow slippage to Q4."}
  - {id: "C-A3-02", check: "F6", line: "570; 172-174; 562-565", classification: "AMBIGUOUS", implication: "Rs 54/kg EBITDA target in two quarters has an unstable baseline: mgmt assented to Q2 of 36 and of 45; derived 44.2. Definition needed before tracking."}
  - {id: "C-A3-03", check: "F14", line: "107-108, 113, 124", classification: "AMBIGUOUS", implication: "Q2 margins tie to ~Rs 304 cr base, not Rs 294 cr revenue; EBITDA may include ~Rs 10 cr other income, so operating margin could be ~13.5% not 16.35%."}
  - {id: "C-A3-04", check: "F14", line: "138-139, 232, 189, 376", classification: "AMBIGUOUS", implication: "11,252 MT/qtr annualises to 107% of stated 42,000 MT; utilisation denominator unknown; headroom math has no basis."}
  - {id: "C-A3-05", check: "F6", line: "142, 494-499, 229-237, 376, 589-590", classification: "FORWARD-SIGNAL", implication: "Tonnage capped until Oct-2027 expansion; interim growth only from Aug 5,040 MT, rented plant and pinch-bottom mix."}
  - {id: "C-A3-06", check: "F17", line: "102, 363, 365-367", classification: "FORWARD-SIGNAL", implication: "Revenue +52.5% YoY on volume +13%: ~34% realisation, mostly polymer pass-through that reverses when polymer falls."}
  - {id: "C-A3-07", check: "F6", line: "88-89, 398, 402-412", classification: "AMBIGUOUS", implication: "Rs 150 cr/yr 3-year contract is a renewal of an existing customer; incremental revenue not disclosed; implies ~13% single-customer concentration."}
  - {id: "C-A3-08", check: "F6", line: "114-115, 125-127, 454-456, 462-465", classification: "FORWARD-SIGNAL", implication: "Mexico JV drag ~10.5% of Q2 PAT; break-even Q3 'almost', Q4 'not very committed'; log Q4 FY27 as test; F4 scope check at results filing."}
  - {id: "C-A3-09", check: "F7", line: "157, 386, 395, 551-553, 558-559", classification: "FORWARD-SIGNAL", implication: "'99 percent covered' contradicts 7% GM hit; mgmt illustration implies 60-88% of hikes realised; percent margin unlikely to fully restore."}
  - {id: "C-A3-10", check: "F7", line: "476-487", classification: "AMBIGUOUS", implication: "India margin-recovery question answered with Mexico content; asked three times, never quantified."}
  - {id: "C-A3-11", check: "F7", line: "186, 190-191, 209-210, 214-215, 241", classification: "AMBIGUOUS", implication: "Pinch-bottom utilisation declined and capacity framed two ways; the named margin lever cannot be tracked without tonnes."}
  - {id: "C-A3-12", check: "F17", line: "425-441", classification: "FORWARD-SIGNAL", implication: "H1 OCF 39 to 22 cr on receivables +55 cr and inventory +26.9 cr; mgmt cause (export cycle) is structural; no days, no normalisation date."}
  - {id: "C-A3-13", check: "F8", line: "442-449", classification: "AMBIGUOUS", implication: "ETR 25% matches statutory; the OCF tax hit is unexplained by the IPO-expense deferred-tax answer; need cash tax vs P&L tax."}
  - {id: "C-A3-14", check: "F17", line: "54-55, 117-118, 127-128", classification: "NEUTRAL-FACT", implication: "ASR gaps cut the CFO balance-sheet section and H1 EBITDA; silence may be a transcript artefact; use filed transcript before scoring silence."}
  - {id: "C-A3-15", check: "F17", line: "78, 82, 119-121, 436-439, 589", classification: "AMBIGUOUS", implication: "Six watch items unquantified (realisation/kg, export %, capex, WC days, concentration, IPO use); silence count 1; each an A4 question."}
  - {id: "C-A3-16", check: "F17", line: "55, 112, 122", classification: "NEUTRAL-FACT", implication: "All framing YoY; derived Q2 PAT -18% QoQ (30.53 to 25.02 cr) on revenue +7% QoQ, not discussed."}
  - {id: "C-A3-17", check: "F6", line: "575-577", classification: "AMBIGUOUS", implication: "Annual target invoked as 'on the track' but never quantified; cannot enter the promise tracker."}
forward_signals: ["C-A3-01", "C-A3-05", "C-A3-06", "C-A3-08", "C-A3-09", "C-A3-12"]
ambiguous: ["C-A3-02", "C-A3-03", "C-A3-04", "C-A3-07", "C-A3-10", "C-A3-11", "C-A3-13", "C-A3-15", "C-A3-17"]
commitments:
  - {commitment: "Pass-through reflects in realisation from Q3 FY27, subject to market stabilisation", implied_date: "Q3 FY27", ref: "T02 L64-67 R662", status_word: "initiated"}
  - {commitment: "Restore EBITDA margin as pricing flows through", implied_date: "from Q3 FY27", ref: "T02 L94 R663; T03 L110 R666; T14 L588 R688", status_word: "initiated"}
  - {commitment: "EBITDA/kg back to Rs 54 (baseline disputed)", implied_date: "Q4 FY27", ref: "T12 L570 R685", status_word: "stated"}
  - {commitment: "Yearly target on track (unquantified)", implied_date: "FY27", ref: "T12 L575-577 R686", status_word: "stated"}
  - {commitment: "Raise value-added (pinch-bottom) share to lift margin", implied_date: "undated", ref: "T02 L95 R664", status_word: "stated"}
  - {commitment: "Q3 better quantity on 5,040 MT added in August", implied_date: "Q3 FY27", ref: "T05 L142-145 R669", status_word: "underway"}
  - {commitment: "Q3 more pinch-bottom sales, rice season", implied_date: "Q3 FY27", ref: "T06 L199-203 R671 R672", status_word: "underway"}
  - {commitment: "Q3-Q4 volume growth on contracted orders incl. renewed contract", implied_date: "H2 FY27", ref: "T14 L586 R687", status_word: "stated"}
  - {commitment: "Rented plant adds capacity", implied_date: "Nov-Dec 2026", ref: "T11 L494-496 R683", status_word: "underway"}
  - {commitment: "Expansion to 69-72k MT; October deadline", implied_date: "Oct-2027", ref: "T06 L229-234 R673; T11 L499 R684", status_word: "underway"}
  - {commitment: "Two new pinch machines into production", implied_date: "Oct-2027", ref: "T06 L236-237 R674", status_word: "stated"}
  - {commitment: "Pinch-bottom 25-30k MT of 72k", implied_date: "FY28 [ASR_DOUBT]", ref: "T06 L241 R675", status_word: "stated"}
  - {commitment: "New Gujarat plant timely completion and utilisation", implied_date: "through 2027", ref: "T14 L589-590 R689", status_word: "stated"}
  - {commitment: "Mexico JV break-even: Q3 near, Q4 not very committed", implied_date: "Q3-Q4 FY27", ref: "T10 L454-465 R680 R681 R931", status_word: "underway"}
  - {commitment: "JV break-even reverses consolidated PAT margin drag", implied_date: "on break-even", ref: "T03 L126-127 R668", status_word: "stated"}
  - {commitment: "ROE/ROCE improve as IPO funds deployed", implied_date: "coming quarters", ref: "T03 L119-121 R667", status_word: "underway"}
  - {commitment: "Rs 150 cr/yr minimum 3-year international contract", implied_date: "signed 2-Oct-2026, 3 years", ref: "T02 L88-89; T09 L402-412 R033 R310", status_word: "completed"}
gate_a3: pass
blank_checks: []
analyst_note: "First review: no prior call, so no promise-vs-delivery diff, and every silence count is 1. All numbers are ASR tier. The call's dated test is Q3 FY27 margin recovery (lines 66, 94, 110, 588). Management's own words undercut it: a 1-2 quarter lag (110), 'not 100%' (559), hikes of 3-4% realised against 5% asked (551), and polymer 'on peak' at Rs 160 (539). Two baselines must be settled before A4 logs targets. First, the Q2 margins tie to a ~Rs 304 cr base, not Rs 294 cr revenue, so EBITDA may carry ~Rs 10 cr other income. That reading also reconciles the 36 vs 45 Rs/kg EBITDA figures management assented to. The Rs 54/kg target needs the definition. Second, 11,252 MT annualises to 107% of the stated 42,000 MT, so the 90-91% utilisation base is unknown. Revenue growth is mostly price (+52.5% on +13% volume), and tonnes stay capped until Oct 2027. The Mexico JV drag is ~10.5% of Q2 PAT; check auditor scope at the results filing (F4). A2's T10-Q3 is a deflection, not a number. Transcript gaps (lines 54, 117, 127) may hide balance-sheet remarks."
```
