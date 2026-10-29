# A3 FORENSIC NOTES: WEWORK q2fy27, doctype CONCALL (ASR machine transcript)

Company: WeWork India Management Ltd (WEWORK). Quarter: Q2 FY27 (quarter ended 30-Sep-2026; call 27-Oct-2026).
Inputs read: A1 structured `runs/wework-q2fy27/extracted/wework-concall-q2fy27-structured.md` (R001-R470), A1 fulltext `runs/wework-q2fy27/extracted/wework-concall-q2fy27-fulltext.md` (L1-L957, read in full), A2 ledger `runs/wework-q2fy27/work/ledger_concall_wework_q2fy27.md`.
Not read: source audio/transcript, anything under `inputs/`.
Prior-quarter fulltext: none. This is the first quarterly review of this name. Every quarter-over-quarter diff is UNTESTABLE and is marked so per check.
Monitoring checklist: no Notion page and no `companies/WEWORK.md` (PRE-THESIS READ). The F17 audit uses the operator's batch watch list (occupancy, desks, rent-to-revenue, net debt, Ind AS 116 lease liabilities, IGAAP-equivalent vs Ind AS) plus the results-filing points (other income, DTA, ESOP dilution, NCLT capital reduction, lease termination gains, Labour Code provision).
Evidence tier: every number below is management tier, spoken, ASR-transcribed, unverified. "Derived" marks arithmetic done by A3 on spoken figures.

## 0. LEDGER RECONCILIATION

- Ledger rows: 470 (R001-R470). Rows read at the cited fulltext line: 470. Reconciled: 100%.
- Category counts tie to the A2 count test: participants 13, turns 56 (incl. 19 questions), numbers 233, forward 60, hedges 46, dates 36, other entities 26. ZERO_STANDING 0.
- Anchor drift (A1 line cite off by +1; claim read at the true line, no content defect): R045, R046, R338, R339 (true L122, cited L123); R228 (true L882, cited L883); R229 (true L897, cited L898); R230 (true L909, cited L910); R231 (true L922, cited L923); R232, R327 (true L927, cited L928); R366 (true L926, cited L927); R367 (true L927, cited L928). Sentence-spanning cites R107, R199, R216 are acceptable. All findings below cite the true line.
- A2 flags honoured: renewal asked three times (R422 L304, R432 L526, R452 L848); pledge cluster (R229/R230, R323-R326, R414, R457-R460); R269 CUSTOMER_EXIT_RISK.

### ASR issues (transcription defects, NOT management misstatements; no finding is built on them alone)

| ref | line | as heard | reading |
|---|---|---|---|
| R041 / R204 | L121, L704 | "145.3,000 deaths" / "this 45,000 that you're seeing" | 145.3k desks; "45,000" drops the leading 1. 145.3k + 4.5k = 149.8k ties to "already at 150,000" (L701). |
| R068 / R167 | L134, L215 | "A plus rating" / "upgraded from an A- to A-" | rating endpoints garbled; tie to filed rating rationale. |
| R176 / R393 | L315 | "our 67% contracted escalations" | probably "6-7%". Not usable. |
| R153 / R131 / R140 / R144-R146 | L206, L187, L196, L197 | "237.7% this quarter", "162.9% gross", "65.8% growth" | unit "crores" rendered as %/"gross"/"growth". |
| R171 | L217-218 | "a loss of 4.2 crores in view 1" | comparative period unknown (Q1 FY27 or Q2 FY26). |
| R180 | L333 | "a motor really like 20 percent in just one quarter" | garbled; see A3-21. |
| R270 | L866 | "Embassy in Mani" | campus/developer name garbled; see A3-05. |
| R290 | L380 | "getting rid of our book clauses" | garbled; see A3-18. |
| R392 / R420 | L245 | hallucinated heading at 00:20:00 | first analyst name, firm and question opening lost. |
| R403 / R436 | L647 | "Her voice is breaking." | audio break 00:43:18-00:43:46; ROCE answer repeated L653-659. |
| (unflagged) | L310-311 | 00:24:24 -> 00:24:35, answer opens "And you'll see" | possible lost start of the first renewal answer; not flagged by A1. |
| (unflagged) | L374 | "we hope that there'll be fewer those" | context suggests "more of those"; unreliable. |
| R215 | L800, L803 | analyst "2.9x", management "That's right" | management said 2.7x at L156; the 2.9x is uncorrected on the call. |

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R442, R443, R201, R202, R275, R299, R301, R407 | L688-689; L701; L714-715 | "is there a chance of the earlier 155k, you know, not being met" / "we are already at 150,000" / "I don't think anything is changing in terms of the guidance" | FORWARD-SIGNAL | March-27 desk guide moved from a 155k point to a 150-155k range. The floor was reached on 5-Oct, so the range allows near-zero H2 net adds. Q3/Q4 desk counts against 155k are the test. |
| A3-02 | F6 | R161, R163, R232, R327, R328, R287, R288 | L211; L209; L927; L930; L372 | "between 500 odd crows of capex" / "larger cap expense than we expected, but it will be lower than the first half" | AMBIGUOUS | FY27 ~500 cr less H1 363.8 cr leaves ~136 cr for H2 (derived). Q2 alone was 175.8 cr, and the largest-ever deal needs "a significant amount of capex". Either FY27 capex overshoots ~500 cr or the deal spend slips into FY28. |
| A3-03 | F6 | R287, R351, R328 | L370-371; L929 | "we've signed one of probably our largest deal ever, which we'll announce in the next quarter" / "just got signed like a few months ago, a few weeks ago" | AMBIGUOUS | A signed, material contract is undisclosed: counterparty, size, revenue/rent and capex unknown. The signing date is self-corrected. It is a Q3 FY27 catalyst and a disclosure-timing question. |
| A3-04 | F6 | R269, R226, R227, R317, R318, R319, R365, R453 | L862-863; L865-868; L870-871; L153-154 | "one company that we have that might be moving out in the next year" / "we've known about this for a few years" / "No sector or customer dominates" | FORWARD-SIGNAL | A large customer of about seven years (ASR "Common World Bank of Australia") shifts to its own 1.2 (unit unheard) build-to-suit campus in FY28. Management knew for years, but the exit is absent from the prepared remarks and surfaced only under questioning. Revenue share, desks and timing are unquantified. |
| A3-05 | F6 | R270, R244, R269 | L866; L96 | "taken up a large bill to suit campus with Embassy in Mani" / "The backing of the embassy group" | AMBIGUOUS | If the campus is an Embassy development, the promoter group's developer arm captures a customer leaving the listed flex operator. This is a related-party / conflict question. The ASR garble prevents resolution. |
| A3-06 | F6 | R422, R432, R452, R401, R179, R224, R223, R433, R435 | L546-548; L560; L629-632; L851; L855 | "renewal escalations are definitely lower then the annual contracted escalation" / "even sometimes if it's like a flat renewal" / "we do give the customer of the benefit of the paid off, you know, CapEx" | FORWARD-SIGNAL | Renewal pricing runs below in-contract escalation, flat renewals are accepted, and managed-office second-cycle pricing hands the capex payback back to the customer. The analyst premise of 35-40% expiring a year with 80-85% renewal implies 5-8% of the contract base lost a year (derived). Management neither confirmed nor denied the premise. |
| A3-07 | F6 | R209, R309, R408, R410, R307, R137, R138 | L744; L778-779; L762-763; L188; L192 | "I don't think we give, you know, like really a percentage" / "think about it in this range of 20 to 23% for next year" | AMBIGUOUS | The FY28 EBITDA range floor (20%) sits below Q2's 21.2% and near Q1's 19.8%. The range allows margin compression while management says the margin is "structurally ... expanding". The range's basis (IGAAP-eq) is unstated. |
| A3-08 | F7 | R302, R303, R304, R305, R306, R358, R359, R444, R445 | L723-725; L728-730; L735-736 | "pretty much all of the rentals hitting in Q3" / "Between Q3 and Q4 you will see, hopefully, further margin expansion" / "I'm not exactly sure on like a percentage-wise YOY basis would be that much different" | FORWARD-SIGNAL | Rent-free periods expire and full rentals hit in Q3, a Q3 margin-pressure quarter. The H2 expansion is hedged ("hopefully", "maybe"), and the Q4 YoY margin gain is not committed. |
| A3-09 | F6 | R208, R207, R409, R265, R266, R267 | L748-750; L755-756 | "minimum wage increases ... for Karnataka was, you know, nearly 60%" / "backdated energy tariffs" / "closer to maybe like 23% just in this quarter" | AMBIGUOUS | The 23% "ex-hit" margin adds back a permanent wage step-up and an unquantified backdated tariff. The wage component recurs, so 23% is not a run-rate. The Labour Code provision is not named. Amounts in crores are not given. |
| A3-10 | F6 | R156, R199, R200, R298, R405, R406, R438, R440, R387 | L207; L665-666; L667-670; L677-679 | "range of between you know 1.2 to one and a half X" / "security deposits is definitely one factor" / "we actually take additional deposit purely on any expansion of seats" | FORWARD-SIGNAL | Q2 FCFO/EBITDA of 1.46x (derived, 237.7/162.9) sits at the top of the guided band. The excess is working-capital float (member deposits and upfront customization cash), and deposits grow only with seats. Conversion falls toward 1.2x when seat growth slows. |
| A3-11 | F6 | R191, R192, R294, R397, R399, R429 | L413-416; L419; L424-425; L668-669 | "we've now normalized any large lumpiness" / "coupled with maybe like one or two large ones" / "We also have started to really amortize the large customizations" | AMBIGUOUS | Customization revenue was 18 cr in Q2 against ~12 cr in Q1 (derived from 30 cr H1) and "flow[s] through down to EBITDA". The amortisation policy change date and its effect on comparatives are unstated. The rise may explain part of the 24.6 cr QoQ EBITDA rise (derived). |
| A3-12 | F17 | R170, R171, R238, R254, R372, R389, R390, R391, R148 | L34; L130; L217; L219-221 | "the financials we discussed today are on an iGAP-equivalent basis" / "Our recorded India's basis fact was 20.5 crores" | AMBIGUOUS | Filed Ind AS PAT of 20.5 cr is 31% of the 65.8 cr headline (derived; gap ~45.3 cr), attributed to Ind AS 116 and "brokerage". No analyst asked about it. The basis of the ROCE (34.5%, +590 bps QoQ) and of every guide is unstated. All headline figures must be tied to filed results before use. |
| A3-13 | F17 | R165, R066, R097, R254 | L213; L156; L219-220 | "We closed September with a net cash of 23.1 crores" / "lease accounting under India's 116" | AMBIGUOUS | The net-cash claim excludes lease liabilities. Ind AS 116 lease liabilities (watch-list item) are never quantified. The only lease-commitment figure is "1,421 crores of rent locked in". Balance-sheet leverage including leases is untested from this call. |
| A3-14 | F6 | R164, R165, R166, R158, R159 | L211; L213-214 | "left a surplus of 16 crores" / "net cash of 23.1 crores compared with a net debt of 310.5 crores a year ago" | AMBIGUOUS | The 333.6 cr net-debt swing (derived) is far larger than the 16 cr H1 FCFF surplus. The source of the remainder (H2 FY26 cash, equity, ESOP proceeds, deposits) is unexplained on the call. |
| A3-15 | F17 | R072, R120, R056, R060, R075 | L136; L181; L127-129 | "Revenue grew 30% to about 1466.7 crores" / "In H1 revenue from operations was 1453.8 gross" | AMBIGUOUS | H1 "revenue" exceeds revenue from operations by ~12.9 cr (derived), about 10.8% of H1 PAT of 119 cr: probably other income. The 21.2% margin computes on the 768.7 cr total (162.9/768.7). Other income's share of profit is not discussed. |
| A3-16 | F6 | R457, R458, R229, R230, R323, R324, R325, R326, R414, R459, R460 | L897; L904; L909-911; L916 | "maybe 50 lakh additional shares would be released shortly" / "We have no hurry to close it" / "right now it makes sense for us to kind of just stay status quo" / "We want to get done as soon as possible" | CONFIRMATORY-NEGATIVE | The Q1 indication of a 50 lakh share release (analyst's account) has no delivery reported. The answer contradicts itself ("no hurry" vs "as soon as possible"). The promise-vs-delivery tracker logs a miss. |
| A3-17 | F6 | R323, R324, R325, R414 | L901-903; L906-908 | "as long as our value market cap sort of like gets back to where it should be" / "or do a block at some point in time, but it's not something that we're looking at definitely at these pricing levels" | FORWARD-SIGNAL | The pledge release is tied to market-cap cover, so a price fall raises margin-call risk. A promoter block sale stays an option, ruled out only at current prices. This is a supply overhang on any rally. |
| A3-18 | F6 | R290, R291 | L378-384 | "we've embarked on this corporate option of getting rid of our book clauses or creating the ability for us to pay dividends or do buybacks" | AMBIGUOUS | This is probably the NCLT capital-reduction route (watch-list item). It is not named, has no filing or order date, and the ASR is garbled. Status "embarked" since Q1. |
| A3-19 | F6 | R292, R293 | L387; L399-400 | "We definitely want to invest into adjacent businesses" / "some amount of capital will go into investing into those new ideas and new-" | FORWARD-SIGNAL | Unquantified, undated capital moves to adjacent businesses outside the core desk model. The answer is cut at the time-block boundary. Capital-allocation drift risk. |
| A3-20 | F6 | R177, R178, R282, R394, R231, R462, R463 | L366-367; L923-925 | "the poor square foot CAPEX numbers have definitely increased, which is a good sign" / "it's fully driven by the capex spending" | FORWARD-SIGNAL | The 3x revenue/rent on new managed-office deals is bought with higher capex per sq ft. Revenue/rent then overstates the return gain. Capex intensity rises as the mix shifts to managed office. |
| A3-21 | F7 | R180, R184, R185, R186, R187, R053, R104 | L331-333; L337-338; L125 | "occupancy has moved up the way that it has" / "moved from about 15,000 seats to about 25,000 seats, but the members grew from about 10,000 to about 16,000" | AMBIGUOUS | Management's own counts imply growth-centre occupancy fell from 66.7% to 64.0% QoQ (derived), against the "moved up" narrative. Portfolio occupancy dipped 114 bps QoQ. The "20 percent" claim is ASR-garbled. |
| A3-22 | F17 | R372, R391 | L34; L221 | "The reconciliation to reported India's is in the presentation and our shareholder letter" / "The full reconciliation is set out on slides 29 to 32." | AMBIGUOUS | All results-filing points go to slides: DTA, ESOP dilution, lease termination gains, ETR, other income and Labour Code provision. None were discussed on the call (see the F17 table). Silence count is 1 quarter; earlier quarters are untestable. |
| A3-23 | F6 | R277, R342, R312, R313, R314, R363, R364, R211, R212, R412, R413 | L150; L842-843; L804; L808-809; L820-821 | "supply for FY28 and FY29 already under negotiation" / "we have no rush to sign up spaces that are necessarily coming in FY29 or FY28" / "because we don't wanna pay the deposit right now" | AMBIGUOUS | The two FY28 supply statements conflict. The "13" (unit unheard; signed plus LOI) is not lease-signed. Moving the 2 msf pipeline to LOI triggers landlord deposit outflows over the next two quarters. |
| A3-24 | F6 | R045, R046, R047, R338, R339, R340 | L122-123 | "about 4,500 more added in October, we have passed the 22,000 mark that we set out for in Q1" | NEUTRAL-FACT | The Q1-set FY27 desk-addition mark is met by October (per management; R047 is ASR-uncertain). This is a milestone confirmation for the Role 5 tracker. Verify against the filed deck. |
| A3-25 | F7 | R308, R324, R411, R303, R322, R317 | L772; L904; L806; L725; L891; L863 | "our endeavor in terms of new initiatives" / "Our endeavor is to close this" / "that are in discussion, evaluation" / "hopefully" / "it is not fully certain right now in terms of timing" | AMBIGUOUS | The hedge lexicon clusters on four items: margin path, pledge, unsigned supply and customer-exit timing. These are the items management will not commit to, and they become A4 question targets. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 | N.A. | Concall. A2 ZERO_STANDING count 0. There are no standing line items. |
| F2 | N.A. | No standalone vs consolidated figures on the call. |
| F3 | N.A. | No entity-level cost lines on the call. |
| F4 | N.A. | No auditor Other Matters on a concall. |
| F5 | N.A. | No EoM / going-concern paragraph. Prior quarter untestable in any case. |
| F6 | FINDING | 21 dateable or dateable-by-context commitments registered (section 3). Status changes: guidance reframed (A3-01), Q1 pledge release missed (A3-16), Q1 22k desk mark met (A3-24). Findings A3-01 to A3-07, A3-09 to A3-11, A3-14, A3-16 to A3-20, A3-23, A3-24. |
| F7 | FINDING | Concall hedges cluster on H2/FY28 margin, pledge, supply and churn timing (A3-08, A3-21, A3-25). Lexicon hits: "endeavor" L772, L904; "in discussion, evaluation" L806; "hopefully" L725, L891; "not fully certain" L863. No notes-style legal hedges (doctype). |
| F8 | N.A. | No tax line, ETR or deferred tax on the call. The silence is logged in F17. |
| F9 | N.A. | No OCI on the call. |
| F10 | N.A. | No share count or EPS on the call. ESOP dilution silence is logged in F17. |
| F11 | N.A. | No net worth or reserves on the call. |
| F12 | N.A. | Core/VAS/digital are revenue lines with no segment assets or liabilities. |
| F13 | N.A. | No board outcome on the call. |
| F14 | N.A. | No notes or auditor letter. ASR defects are tabled in section 0, not as drafting inconsistencies. |
| F15 | N.A. | No consolidation list. Prior quarter untestable. |
| F16 | N.A. | Presentation check. The deck is not in this run's inputs. The guidance reframing heard on the call is captured under F6 (A3-01). |
| F17 | FINDING | Watch-list and filing-point silence audit (section 4). Lease liabilities, other income, DTA, ESOP, lease termination gains and ETR were silent. NCLT, Labour Code and IGAAP-eq vs Ind AS were partial. Findings A3-12, A3-13, A3-15, A3-22. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line | status word |
|---|---|---|---|---|
| C01 | Reach 150-155k desks (range; earlier 155k point per analyst) | Mar-2027 | T02 L149; T29 L701-715 | underway (150k on 5-Oct) |
| C02 | Reach 190-200k seats | undated | T02 L149-150 | initiated |
| C03 | FY27 desk-addition "22,000 mark" set in Q1 | FY27 | T02 L122-123 | completed (per management, ASR-uncertain) |
| C04 | Supply for FY28/FY29 under negotiation | FY28-FY29 | T02 L150 | underway |
| C05 | Asset identification for next 12 months / next FY | next 12 months | T07 L256-259 | completed |
| C06 | Announce largest-ever deal (signed) | next quarter (Q3 FY27) | T11 L370-371; T51 L928-929 | completed (signing); announcement pending |
| C07 | FY28 desk rollout larger than FY27 | FY28 | T11 L356-362; T36 L837-841; T51 L931-932 | initiated |
| C08 | FY27 capex ~500 cr; H2 below H1 | FY27 | T51 L927-930 | underway |
| C09 | FY28 capex ~600 cr or slightly more, below cash generated | FY28 | T51 L933-935 | initiated |
| C10 | Finalise ~2 msf of unsigned supply | next two quarters (by Q4 FY27) | T36 L820-822 | initiated |
| C11 | Remove restriction to enable dividends / buybacks (probable NCLT route) | undated | T11 L378-384 | underway ("embarked", Q1) |
| C12 | Invest capital in adjacent businesses | undated | T11 L387-400 | initiated |
| C13 | FY28 EBITDA margin 20-23% (indicative) | FY28 | T34 L778-779 | initiated |
| C14 | H2 FY27 margin expansion, larger in Q4 | Q3-Q4 FY27 | T29 L725-731 | initiated |
| C15 | PAT margin 7-10% to continue | ongoing | T41 L882-883 | underway |
| C16 | FCFO/EBITDA 1.2-1.5x | ongoing | T24 L665, L673 | underway |
| C17 | Backfill and large contracts to offset the large-customer exit | FY28 | T39 L869-870 | underway |
| C18 | H1 opening cohort to cross mature-centre occupancy | next year | T09 L342-344 | initiated |
| C19 | Pledge reduction (Q1: ~50 lakh shares "shortly") | 3-year debt horizon | T43-T46 L897-916 | initiated (no progress stated) |
| C20 | Interest cost reduction to continue | ongoing | T41 L888-891 | underway |
| C21 | Customization at a normalised run-rate, amortised | ongoing | T15 L413-425 | underway |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

Consecutive-quarter counts start at 1. This is the first observed quarter; earlier quarters are untestable.

| item | source | addressed on call? | line | quarters of silence |
|---|---|---|---|---|
| Occupancy | watch list | YES: 83.7%, down 114 bps QoQ; mature 87.7% | L124-125, L167 | 0 |
| Desks | watch list | YES: 145.3k; 150k on 5-Oct | L121, L701-706 | 0 |
| Rent-to-revenue | watch list | YES, as revenue/rent 2.7x | L131, L156 | 0 |
| Net debt | watch list | YES: net cash 23.1 cr, excluding leases | L213 | 0 |
| Lease liabilities (Ind AS 116) | watch list | NO: named only as a reconciling item | L219-220 | 1 |
| IGAAP-eq headline vs reported Ind AS | watch list | PARTIAL: 4 lines of prepared remarks, no Q&A, guidance basis unstated | L34, L217-221 | 1 (partial) |
| Other income share of profit | filing point | NO | (none; see A3-15) | 1 |
| Deferred tax asset | filing point | NO | (none) | 1 |
| ESOP dilution | filing point | NO | (none) | 1 |
| NCLT capital reduction | filing point | PARTIAL: oblique, not named, no date | L378-382 | 1 (partial) |
| Lease termination gains | filing point | NO | (none) | 1 |
| Labour Code provision | filing point | PARTIAL: minimum-wage hikes only, Labour Code not named | L748-749 | 1 (partial) |
| Tax / ETR | implicit | NO | (none) | 1 |
| Renewal price spread vs new contracts | asked 3 times | NOT ANSWERED with a number | L304-310, L526-533, L848-852 | 1 |
| Expiry share (analyst: 35-40% a year) | analyst premise | NEITHER CONFIRMED NOR DENIED | L851, L854-861 | 1 |
| Large-customer revenue / desk share | arising | NOT QUANTIFIED | L862-868 | 1 |
| Q1 pledge release (50 lakh shares) | prior commitment (analyst) | YES: no delivery reported | L897-911 | n/a (miss) |
| Earlier 155k point desk guide | prior commitment (analyst) | YES: reframed to a range | L687-715 | n/a (reframed) |

## 5. FLAGS FOR A4 (question conversion)

FORWARD-SIGNAL: A3-01, A3-04, A3-06, A3-08, A3-10, A3-17, A3-19, A3-20.
AMBIGUOUS: A3-02, A3-03, A3-05, A3-07, A3-09, A3-11, A3-12, A3-13, A3-14, A3-15, A3-18, A3-21, A3-22, A3-23, A3-25.
CONFIRMATORY-NEGATIVE: A3-16. NEUTRAL-FACT: A3-24.

A4 should tie every spoken figure to the filed Q2 FY27 results and deck before any use. A3-12, A3-13 and A3-15 come first.

```yaml
stage: A3-forensics
company: "WEWORK"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/wework-q2fy27/work/forensics_concall_wework_q2fy27.md"
ledger_reconciled_pct: 100        # 470 / 470
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: N.A.
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "L688-689; L701; L714-715", classification: "FORWARD-SIGNAL", implication: "March-27 guide moved from a 155k point to a 150-155k range; floor met 5-Oct, so the range allows near-zero H2 net adds"}
  - {id: "A3-02", check: "F6", line: "L209; L211; L372; L927; L930", classification: "AMBIGUOUS", implication: "FY27 ~500 cr less H1 363.8 cr leaves ~136 cr for H2, below Q2 alone (175.8 cr), while the largest-ever deal needs significant capex; overshoot or FY28 slip"}
  - {id: "A3-03", check: "F6", line: "L370-371; L929", classification: "AMBIGUOUS", implication: "signed largest-ever deal undisclosed (size, counterparty, capex); signing date self-corrected; Q3 catalyst and disclosure-timing question"}
  - {id: "A3-04", check: "F6", line: "L862-863; L865-868; L870-871; L153-154", classification: "FORWARD-SIGNAL", implication: "large 7-year customer exits to own campus in FY28; known for years but omitted from prepared remarks; share unquantified"}
  - {id: "A3-05", check: "F6", line: "L866; L96", classification: "AMBIGUOUS", implication: "exiting customer's campus may be an Embassy (promoter-group) development; related-party conflict question; ASR garbled"}
  - {id: "A3-06", check: "F6", line: "L546-548; L560; L629-632; L851; L855", classification: "FORWARD-SIGNAL", implication: "renewal escalation below contracted escalation, flat renewals accepted, paid-off capex passed back; ~5-8% contract base lost a year (derived from analyst premise)"}
  - {id: "A3-07", check: "F6", line: "L744; L778-779; L188; L192", classification: "AMBIGUOUS", implication: "FY28 EBITDA range 20-23% has its floor below Q2 21.2%; range permits compression; basis unstated"}
  - {id: "A3-08", check: "F7", line: "L723-725; L728-730; L735-736", classification: "FORWARD-SIGNAL", implication: "full rentals and rent-free expiry hit Q3; H2 expansion hedged; Q4 YoY margin gain not committed"}
  - {id: "A3-09", check: "F6", line: "L748-750; L755-756", classification: "AMBIGUOUS", implication: "23% ex-hit margin adds back a permanent wage step-up plus an unquantified backdated tariff; not a run-rate; Labour Code not named"}
  - {id: "A3-10", check: "F6", line: "L207; L665-670; L677-679", classification: "FORWARD-SIGNAL", implication: "Q2 FCFO/EBITDA 1.46x at the band top is working-capital float tied to seat growth; normalises toward 1.2x when growth slows"}
  - {id: "A3-11", check: "F6", line: "L413-416; L419; L424-425; L668-669", classification: "AMBIGUOUS", implication: "customization 18 cr Q2 vs ~12 cr Q1, high flow-through, amortisation policy change undated; part of QoQ EBITDA rise"}
  - {id: "A3-12", check: "F17", line: "L34; L130; L217; L219-221", classification: "AMBIGUOUS", implication: "filed Ind AS PAT 20.5 cr is 31% of the 65.8 cr IGAAP-eq headline; ROCE and guidance basis unstated; tie to filing before use"}
  - {id: "A3-13", check: "F17", line: "L213; L156; L219-220", classification: "AMBIGUOUS", implication: "net cash 23.1 cr excludes Ind AS 116 lease liabilities, never quantified; lease-inclusive leverage untested"}
  - {id: "A3-14", check: "F6", line: "L211; L213-214", classification: "AMBIGUOUS", implication: "333.6 cr net-debt swing vs 16 cr H1 FCFF surplus; source of the remainder unexplained (equity, ESOP, deposits?)"}
  - {id: "A3-15", check: "F17", line: "L136; L181; L127-129", classification: "AMBIGUOUS", implication: "H1 revenue exceeds revenue from operations by ~12.9 cr (~10.8% of H1 PAT), probably other income inside the headline and margins; not discussed"}
  - {id: "A3-16", check: "F6", line: "L897; L904; L909-911; L916", classification: "CONFIRMATORY-NEGATIVE", implication: "Q1 indication of 50 lakh pledged-share release not delivered; answer self-contradicts (no hurry vs as soon as possible)"}
  - {id: "A3-17", check: "F6", line: "L901-903; L906-908", classification: "FORWARD-SIGNAL", implication: "pledge release tied to market cap (margin-call risk on a fall); promoter block sale an option, excluded only at current prices"}
  - {id: "A3-18", check: "F6", line: "L378-384", classification: "AMBIGUOUS", implication: "dividend/buyback enabling route (probable NCLT capital reduction) not named, no date; status embarked since Q1"}
  - {id: "A3-19", check: "F6", line: "L387; L399-400", classification: "FORWARD-SIGNAL", implication: "unquantified capital moves to adjacent businesses; capital-allocation drift risk"}
  - {id: "A3-20", check: "F6", line: "L366-367; L923-925", classification: "FORWARD-SIGNAL", implication: "3x revenue/rent on managed office is bought with higher capex per sq ft; revenue/rent overstates the return gain"}
  - {id: "A3-21", check: "F7", line: "L331-333; L337-338; L125", classification: "AMBIGUOUS", implication: "management's own counts imply growth-centre occupancy fell 66.7% to 64.0% QoQ against a 'moved up' narrative; portfolio -114 bps QoQ"}
  - {id: "A3-22", check: "F17", line: "L34; L221", classification: "AMBIGUOUS", implication: "DTA, ESOP dilution, lease termination gains, ETR, other income and Labour Code provision all deferred to slides; silent on the call"}
  - {id: "A3-23", check: "F6", line: "L150; L804; L808-809; L820-821; L842-843", classification: "AMBIGUOUS", implication: "FY28 supply 'under negotiation' vs 'no rush'; the 13 is LOI not lease; LOI conversion triggers landlord deposit outflows"}
  - {id: "A3-24", check: "F6", line: "L122-123", classification: "NEUTRAL-FACT", implication: "Q1-set 22k FY27 desk-addition mark met by October per management (ASR-uncertain); verify on the deck"}
  - {id: "A3-25", check: "F7", line: "L772; L904; L806; L725; L891; L863", classification: "AMBIGUOUS", implication: "hedge lexicon clusters on margin path, pledge, unsigned supply and exit timing; the uncommitted items become A4 targets"}
forward_signals: ["A3-01", "A3-04", "A3-06", "A3-08", "A3-10", "A3-17", "A3-19", "A3-20"]
ambiguous: ["A3-02", "A3-03", "A3-05", "A3-07", "A3-09", "A3-11", "A3-12", "A3-13", "A3-14", "A3-15", "A3-18", "A3-21", "A3-22", "A3-23", "A3-25"]
commitments:
  - {commitment: "Reach 150-155k desks (earlier 155k point)", implied_date: "Mar-2027", ref: "T02 L149; T29 L701-715", status_word: "underway"}
  - {commitment: "Reach 190-200k seats", implied_date: "undated", ref: "T02 L149-150", status_word: "initiated"}
  - {commitment: "FY27 desk-addition 22,000 mark set in Q1", implied_date: "FY27", ref: "T02 L122-123", status_word: "completed"}
  - {commitment: "Supply for FY28/FY29 under negotiation", implied_date: "FY28-FY29", ref: "T02 L150", status_word: "underway"}
  - {commitment: "Asset identification for next 12 months done", implied_date: "next 12 months", ref: "T07 L256-259", status_word: "completed"}
  - {commitment: "Announce signed largest-ever deal", implied_date: "Q3 FY27", ref: "T11 L370-371; T51 L928-929", status_word: "completed"}
  - {commitment: "FY28 desk rollout larger than FY27", implied_date: "FY28", ref: "T11 L356-362; T36 L837-841", status_word: "initiated"}
  - {commitment: "FY27 capex ~500 cr, H2 below H1", implied_date: "FY27", ref: "T51 L927-930", status_word: "underway"}
  - {commitment: "FY28 capex ~600 cr or more, below cash generated", implied_date: "FY28", ref: "T51 L933-935", status_word: "initiated"}
  - {commitment: "Finalise ~2 msf unsigned supply", implied_date: "by Q4 FY27", ref: "T36 L820-822", status_word: "initiated"}
  - {commitment: "Enable dividends/buybacks (probable NCLT capital reduction)", implied_date: "undated", ref: "T11 L378-384", status_word: "underway"}
  - {commitment: "Invest capital in adjacent businesses", implied_date: "undated", ref: "T11 L387-400", status_word: "initiated"}
  - {commitment: "FY28 EBITDA margin 20-23% (indicative)", implied_date: "FY28", ref: "T34 L778-779", status_word: "initiated"}
  - {commitment: "H2 FY27 margin expansion, larger in Q4", implied_date: "Q3-Q4 FY27", ref: "T29 L725-731", status_word: "initiated"}
  - {commitment: "PAT margin 7-10% to continue", implied_date: "ongoing", ref: "T41 L882-883", status_word: "underway"}
  - {commitment: "FCFO/EBITDA 1.2-1.5x", implied_date: "ongoing", ref: "T24 L665, L673", status_word: "underway"}
  - {commitment: "Backfill to offset large-customer exit", implied_date: "FY28", ref: "T39 L869-870", status_word: "underway"}
  - {commitment: "H1 cohort to cross mature-centre occupancy", implied_date: "next year", ref: "T09 L342-344", status_word: "initiated"}
  - {commitment: "Pledge reduction (Q1: ~50 lakh shares shortly)", implied_date: "3-year debt horizon", ref: "T43-T46 L897-916", status_word: "initiated"}
  - {commitment: "Interest cost reduction to continue", implied_date: "ongoing", ref: "T41 L888-891", status_word: "underway"}
  - {commitment: "Customization at a normalised, amortised run-rate", implied_date: "ongoing", ref: "T15 L413-425", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "The headline figures follow a management IGAAP-equivalent basis. Filed Ind AS PAT was 20.5 cr against the 65.8 cr headline (L130, L217). Margin, PAT and ROCE guides carry no stated basis. A4 should tie each spoken figure to the filed results first (A3-12, A3-13, A3-15). Three forward risks carry the most weight. First, renewal pricing runs below contracted escalation, and the number went unanswered across three asks. Second, a seven-year customer exits to a build-to-suit campus that may belong to the promoter's Embassy group (ASR garbled, L866). That exit was absent from the prepared remarks. Third, FY27 capex of ~500 cr cannot fit H1's 363.8 cr plus the largest-ever deal, so capex overshoots or the deal's spend slips to FY28. The desk guide moved to a range whose floor was met on 5-Oct. The Q1 pledge release was not delivered. The ASR conflicts (145.3k vs 45k, A- vs A plus, 67% escalations) are transcription defects, not misstatements. A1 anchors drift +1 line on 12 rows; quotes were read at the true line. Prior-quarter diffs are untestable."
```
