# Stage 12 Verifier B: Concall Red Flags (FABTECH)

Run date: 2026-09-26. Model: claude-opus-5-5. Independent context: this verifier read the raw
transcripts first, then B05 and B06. It did not see any other verifier output.

Anchor convention. Main-company anchors cite the `[page N]` marker in the page-marked .txt
beside each PDF (runs/fabtech-2026-09-26/inputs/concalls/). Peer anchors cite the line number
(L) in the peer .txt (runs/fabtech-2026-09-26/inputs/peer-concalls/). Call labels: Nov-25 =
Concall_Nov_2025 (Q1+Q2 FY26, held 10-Nov-2025); Feb-26 = Concall_Feb_2026 (Q3 FY26, held
10-Feb-2026); Apr-26 = Concall_Apr_2026 (Q4 FY26, held 28-Apr-2026); Aug-26 =
Concall_Aug_2026 (Q1 FY27, held 28-Jul-2026).

Coverage. The four main transcripts were read in full. SETL Nov-2025 and SETL Aug-2026 were
read in full. The other ten peer transcripts were read by targeted search (freight, shipping,
war, Middle East, Saudi, Africa, cancel, deferral, working capital, competitor) plus context
reads around every B06 citation. 16 transcripts in the run (4 main, 12 peer).

---

## 1. Independent red-flag list (from raw transcripts, before reading B05/B06)

Severity scale: CRITICAL / MAJOR / MINOR, graded before scoring.

| # | Item | Anchor (call, speaker, location) | Severity |
|---|---|---|---|
| 1 | FY27 growth guidance walked down three times: "30 to 40 percent... 30 is the target" to "approximately 25%" / "25 to 30%" to "20% to 25% organic". Never called a cut. | Feb-26 [page 14] Aasif Khan, Ashwani Singh; Apr-26 [page 3] Ashwani Singh, [page 9] Karan Doshi; Aug-26 [page 3], [page 9] | MAJOR |
| 2 | Conference-circuit targets (FY27 revenue Rs 530-600 Cr, FY28 PAT 12-14%) met with "difference of communication... consolidated and standalone" and "We're on track, I would say", while Karan Doshi gives PAT 9-11% in the same call and again in Aug. | Apr-26 [page 19] Rahil, [page 20] Aman Anavkar, [page 21] Karan Doshi; Aug-26 [page 19] Karan Doshi | MAJOR |
| 3 | Order book flat for eleven months: Rs 904.42 Cr (31-Jul-25), claimed "9% growth as of September 2025", Rs 926 Cr (31-Jan-26), "more than 900" (Mar-26), "over 900... ideally 920" (Jun-26). Apr promise "in coming quarters, you will see huge order booking" followed by Q1 FY27 inflow of Rs 96.5 Cr. | Nov-25 [page 5] Aman Anavkar; Feb-26 [page 6] Karan Doshi; Apr-26 [page 7], [page 13] Ashwani Singh; Aug-26 [page 8] | MAJOR |
| 4 | Order-book / segment composition refused in all four calls: segment revenue bifurcation (Nov), end-user breakup "no breakup as such" (Feb), geography split "I'll just pull up the data" never returned (Apr), vaccine/pharma split "we would not be able to give" and geography "we do not" (Aug). Repeated evasion, 4 quarters. | Nov-25 [page 11]; Feb-26 [page 12]; Apr-26 [page 14]; Aug-26 [page 13], [page 15] | CRITICAL |
| 5 | Founder admits discretionary revenue timing: "some of the quarter three also we pulled to quarter two"; "we really hold the shipment. Otherwise, the LC says, ship it, we can ship it, dump it there, we'll recognise our revenue". Management controls which quarter books revenue. | Feb-26 [page 12] Aasif Khan; repeated [page 19] | MAJOR |
| 6 | Revenue recognition described three ways: Aman "revenue recognition takes place on project progress" then Ashwani "complete revenue recognition is based on the bill of lading" (same answer, Apr); CEO "recognized against project milestones and customer approvals" vs Karan "revenues recognized on shipment bases... BL's" and Aman "milestone-based billing and upon BL" (Aug). | Apr-26 [page 16]; Aug-26 [page 3] Ashwani Singh, [page 8] Karan Doshi, [page 9] Aman Anavkar | MAJOR |
| 7 | Retention terms contradicted: "there is no retention over 6 months from installation or handing over of the project" (Feb) vs "typical retention period of one to two years... around 10 to 15%... that is where our receivables get stuck" (Aug). | Feb-26 [page 13] Aman Anavkar; Aug-26 [page 11] Karan Doshi | MAJOR |
| 8 | Receivable promise broken: "if you go with Q1 and Q2, the receivable will be reduced immediately" (Apr). Aug: receivables Rs 211 Cr to ~Rs 215 Cr. Saudi receivable Rs 72.57 Cr against Saudi Q1 revenue of Rs 17.14 Cr; one Saudi contract of ~Rs 120 Cr. | Apr-26 [page 18] Ashwani Singh; Aug-26 [page 3]-[page 4], [page 11] Karan Doshi | MAJOR |
| 9 | Hot-lead pipeline figure swings: "close to roughly around $455 million" (Feb) to "close to... 200 million odd USD with offers in the market" (Apr) to "hot leads worth over Rupees 3,800 crores" plus Rs 9,300 Cr inquiries (Aug). No reconciliation of the halving and recovery. | Feb-26 [page 7] Aasif Khan; Apr-26 [page 11] Aman Anavkar; Aug-26 [page 4], [page 7] | MAJOR |
| 10 | Win rate: "10 to 12 percent thus far... last three months, increased to 15%" (Feb) vs "It is now 11% and it is reaching... 16 to 17 percent" (Apr). | Feb-26 [page 9] Aasif Khan; Apr-26 [page 13] Ashwani Singh | MINOR |
| 11 | European acquisition slipped: "First quarter"; "could even surprise you if it happens before March 31st" (Feb) to "has yet not gone through" (Apr) to Italy "before the end of the current financial year" and "next two to three quarters" (Aug). | Feb-26 [page 13]-[page 14]; Apr-26 [page 15]; Aug-26 [page 5], [page 19] | MAJOR |
| 12 | SACE status contradicted: CEO says "incorporating Specialized Contracting Activities LLC... Fabtech Technologies LLC holding a 51% stake" and "our proposed acquisition in Italy and Saudi Arabia are progressing well... complete both before the end of the current financial year". CGO says "With the acquisition that we had" and "SACE, which we acquired majority of... first one we've already acted on". | Aug-26 [page 4]-[page 5] Ashwani Singh; [page 6], [page 19] Aman Anavkar; [page 14] Ashwani Singh "newly acquired company" | MAJOR |
| 13 | Related-party procurement understated: Apr "close to 11%... clean room panels from [FTCL]... air handling units... from an entity called Advantek and that would be another about 15%... total breakup of what we procured from our related entities" vs Aug "relative party transaction... for cleanroom panels, which is not more than 11%". | Apr-26 [page 17] Aman Anavkar; Aug-26 [page 19] Aman Anavkar | MAJOR |
| 14 | Margin promise broken: FY26 margins "Better than last year, for sure" (Nov). FY26 EBITDA Rs 55.56 Cr on Rs 431.33 Cr vs Rs 46.97 Cr on ~Rs 335 Cr, lower; Apr concedes "the margins have shrunk despite revenue increase". | Nov-25 [page 15] Aman Anavkar; Apr-26 [page 3], [page 8], [page 9] | MAJOR |
| 15 | Africa margin story reverses: Apr "Countries like Africa, there are slight pressure on the margins" and "market penetration strategy in cost-effective markets such as Africa"; Aug "Saudi Arabia, Africa, which is carrying the growth and they're doing so with better margins" (used to explain contribution margin 37.6% to 46.7%). Peer PRAJIND: construction-heavy Africa orders "the margins are not generally what we get in the international market". | Apr-26 [page 8]-[page 9] Karan Doshi, Aman Anavkar; Aug-26 [page 6] Aman Anavkar; PRAJIND-Concall_Mar_2026 L358-367; PRAJIND-Concall_Dec_2025 L657-663 | MAJOR |
| 16 | Cost impact and pass-through told differently to different analysts: Karan "the impact on cost could be very small... compensated... We do not see a material impact" vs Aman "RMC cost... grew up by close to 33%... execution cost... up to 43%" (same call); Aman "I would not say pass on the cost to the client" (Apr) vs "if there is an RMC increase of over 5%... there would be a passing over of the costs" then "Many situations we do, some situations we don't" (Aug). Peer SETL Aug-26: analyst cites shipping cost "increased by almost 4x"; SETL exports fell to 2-3%. | Apr-26 [page 10], [page 11], [page 21]; Aug-26 [page 16]-[page 17]; SETL-Concall_Aug_2026 L258-263 | MAJOR |
| 17 | Earnings quality: FY26 other income ~Rs 20-21 Cr, "around 12 crores of foreign income. Forex", balance ~Rs 7 Cr FD interest, against PAT Rs 38.36 Cr. Q3 FY26 other income Rs 7 Cr, "almost like 10% of the total revenue". | Apr-26 [page 18] Karan Doshi; Feb-26 [page 22] Girish, Karan Doshi | MAJOR |
| 18 | Quarter-end port inventory recurs: Rs 20.3 Cr / "20-22 crores of material lying at the port" (Q3 FY26) and "20-22 crores of our goods lying at the port" (Q1 FY27). | Feb-26 [page 6], [page 8]; Aug-26 [page 16] Karan Doshi | MINOR |
| 19 | Executive Chairman transition, framed as "should not be viewed as a return to the operation"; founder Aasif Khan leads the Feb call and is absent from Apr and Aug. | Apr-26 [page 4] Ashwani Singh; Feb-26 [page 2]; Apr-26 [page 2]; Aug-26 [page 2] | MAJOR |
| 20 | IPO monitoring agency "did not allow the 50 crores of working capital to be reimbursed"; deployment called "an active call", not a delay. | Apr-26 [page 15] Karan Doshi, Aman Anavkar | MAJOR |
| 21 | Percentage-of-completion switch: "we'll evaluate this situation in the next six months or a year" (Feb) to "we expect to see the changes in next few years" (Aug). | Feb-26 [page 18]; Aug-26 [page 20] Karan Doshi | MAJOR |
| 22 | Stock-price / investor-confidence questions deflected ("beyond the management's control"). | Feb-26 [page 14]-[page 15]; Apr-26 [page 8]; Aug-26 [page 10], [page 18] | MINOR |
| 23 | FY26 PAT Rs 38.36 Cr below the Rs 39-41 Cr guidance floor; framed via exceptional items, not as a miss. | Feb-26 [page 8] Aasif Khan; Apr-26 [page 4] Ashwani Singh | MAJOR |
| 24 | Execution tenor drift: "nine months to 18 months... going forward, we are speeding" (Feb) to "18 to 24 months" and greenfield "24 to 27 months" (Apr) to "12 to 24... 12 to 36 months" (Aug). | Feb-26 [page 7]; Apr-26 [page 12]; Aug-26 [page 9] | MINOR |
| 25 | Ticket-size unit confusion: "Earlier we used to do 30, $40 million. Today we have orders worth $70 million" then "30 to 40... few orders which are more than 50 crores, 60 crores" in the same call. | Apr-26 [page 6], [page 8] Karan Doshi | MINOR |
| 26 | CGO: "We have not been able to close any civil contracts"; CEO corrects: "10 days before, we acquired one civil order". | Aug-26 [page 14] | MINOR |
| 27 | Repeat-customer share ~10%, recast as "an active decision... to not depend on repeat customers"; Nov-25 sold repeat work as the moat ("makes us a preferred partner... when they expand"). | Aug-26 [page 13]-[page 14] Aman Anavkar, Karan Doshi; Nov-25 [page 6] Aman Anavkar | MAJOR |
| 28 | Scope drift: "not focused on the non-pharma segment" (Nov) to "diversification is always in the plans... data centers, semi-con... nuclear, aerospace" (Apr) to SACE taking Fabtech "beyond pharmaceutical cleanrooms EPC into the far larger built infrastructure" and "non-pharmaceutical HVAC MEP and civil" (Aug). | Nov-25 [page 12]; Apr-26 [page 17]; Aug-26 [page 4], [page 19] | MINOR |
| 29 | Feb dodges: FY23 revenue fall ("I don't know what happened in twenty-three"); "certain things which we would not be discussing in a forum"; "we refrain from talking about competition". | Feb-26 [page 22], [page 21], [page 8] Aasif Khan, Aman Anavkar | MINOR |
| 30 | Founder defensiveness: "may I request you to go through the transcript"; "it seems you're representing the entire investor community"; unprompted rebuttal of a website's "concern over our execution capability". | Feb-26 [page 7], [page 8], [page 23] Aasif Khan | MINOR |
| 31 | Unusual analyst insistence in the first call: five questioners (Sushant Shah twice, Akhut Prabhat, Shiladitya, Archit Agarwal) press for margin or growth ranges; management gives none ("we cannot over-commit"; vision to be "published in all leading newspapers"). | Nov-25 [page 4]-[page 5], [page 9]-[page 10], [page 15]-[page 16] | MINOR |

Graded totals: 31 items. 1 CRITICAL, 20 MAJOR, 10 MINOR. Material (CRITICAL + MAJOR) = 21.

---

## 2. Comparison against B05 and B06

### 2A Independent items vs pipeline

| # | Severity | Status | Where the pipeline has it / what it missed |
|---|---|---|---|
| 1 | MAJOR | CAUGHT | B05 1C, 2A, 4D flag 2 |
| 2 | MAJOR | PARTIALLY CAUGHT | B05 3C/4D has the Rs 530-600 Cr gap and 2D notes "no bridge" to 12-14%. It misses that Karan gives 9-11% in the same call where Aman says "on track". |
| 3 | MAJOR | CAUGHT | B05 4D flag 1. The Apr "huge order booking" promise is not tracked, but the flag holds. |
| 4 | CRITICAL | PARTIALLY CAUGHT | B05 2E logs three quarters (Feb, Apr, Aug) and 2D notes it. B05 4D grades it LOW-MEDIUM, which under-weights a four-call evasion. Nov-25 refusal and the Apr "pull up the data" non-return are not logged. |
| 5 | MAJOR | MISSED | B05 treats POC deferral, not the founder's admission of discretionary timing. |
| 6 | MAJOR | MISSED | Not in B05 or B06. |
| 7 | MAJOR | MISSED | B05 4B adopts the Aug retention terms as fact in a peer question; the Feb contradiction is absent. |
| 8 | MAJOR | PARTIALLY CAUGHT | B05 2A row 7 and 3C note rising receivables. It misses the specific Apr promise and the Saudi receivable concentration. |
| 9 | MAJOR | MISSED | B05 1B quotes the Aug Rs 3,800 Cr figure only. |
| 10 | MINOR | PARTIALLY CAUGHT | B05 1C: "measurement basis shifts each call". The fall from 15% to 11% is not stated. |
| 11 | MAJOR | CAUGHT | B05 2A, timeline_slippages. |
| 12 | MAJOR | MISSED | B05 1B, 2A row 4, 3D and trigger 1 all state SACE "closed" as an acquisition. The CEO's own words describe an incorporation and a still-proposed Saudi acquisition. |
| 13 | MAJOR | PARTIALLY CAUGHT | B05 2D reports 11% + 15% but attributes both to FTCL (the 15% is via Advantek) and misses the Aug restatement to "not more than 11%". |
| 14 | MAJOR | MISSED | Not in B05 promise tracker. |
| 15 | MAJOR | PARTIALLY CAUGHT | B06 Part 5 uses PRAJIND's Africa construction-dilution point. B05 trigger 5 accepts the Aug geography-mix story. Neither names the Apr to Aug reversal. |
| 16 | MAJOR | PARTIALLY CAUGHT | B06 Q2 treats cost pressure as confirmed. The same-call contradiction and the pass-through reversal are not named. |
| 17 | MAJOR | MISSED | Not in B05 or B06. |
| 18 | MINOR | MISSED | B05 row 1 marks the Feb port delay Delivered and does not note the recurrence in Aug. |
| 19 | MAJOR | CAUGHT | B05 4D flag 5 |
| 20 | MAJOR | CAUGHT | B05 4D flag 6 (graded LOW-MEDIUM) |
| 21 | MAJOR | CAUGHT | B05 2E, 4D flag 4 |
| 22 | MINOR | CAUGHT | B05 2E |
| 23 | MAJOR | CAUGHT | B05 2A row 2 |
| 24 | MINOR | MISSED | Not in B05. |
| 25 | MINOR | MISSED | Not in B05. |
| 26 | MINOR | MISSED | B05 3D reports the civil order as a positive only. |
| 27 | MAJOR | PARTIALLY CAUGHT | B05 3D reports ~10% but adopts management's reframing: "this reframes what could otherwise read as weak customer retention". |
| 28 | MINOR | PARTIALLY CAUGHT | B05 notes data-centre dormancy; SACE non-pharma scope is treated as trigger 1 only. |
| 29 | MINOR | PARTIALLY CAUGHT | B05 3A has the competition refusal; FY23 and "not in a forum" dodges absent. |
| 30 | MINOR | CAUGHT | B05 2C defensiveness 4/5 |
| 31 | MINOR | MISSED | B05 uses Nov-25 only for LBF1 context. |

Totals (all 31): CAUGHT 9, PARTIALLY CAUGHT 10, MISSED 12.
Material subset (21): CAUGHT 7, PARTIALLY CAUGHT 7, MISSED 7.

### 2B Pipeline red flags assessed against the transcripts

| Pipeline flag | Verdict | Basis |
|---|---|---|
| B05: order book flat 904 to 926 to 900+ | SUPPORTED | Nov-25 [page 5]; Feb-26 [page 6]; Apr-26 [page 7]; Aug-26 [page 8] |
| B05: FY27 guidance cut three times | SUPPORTED | Item 1 anchors |
| B05: Rs 530-600 Cr unreconciled | SUPPORTED | Apr-26 [page 19]-[page 20] |
| B05: POC transition pushed out | SUPPORTED | Feb-26 [page 18]; Aug-26 [page 20] |
| B05: Executive Chairman transition without detail | SUPPORTED | Apr-26 [page 4] |
| B05: IPO monitoring agency Rs 50 Cr | SUPPORTED | Apr-26 [page 15] |
| B05: Rs 1,000 Cr by 2030 new | SUPPORTED | Aug-26 [page 18] Karan Doshi |
| B05: order-book split never numeric | SUPPORTED (under-weighted, see item 4) | Item 4 anchors |
| B05 2D: Company Secretary resignation "never mentioned in any transcript" | OVERSTATED | The resignation (24-Sep-2026) post-dates the last call (28-Jul-2026). Silence is not a disclosure failure. |
| B06 Q2 / flags: "magnitude gap, 33%/43% cost inflation vs PRAJIND 1-1.5%" | NOT SUPPORTED | Apr-26 [page 21]: "the RMC cost, which grew up by close to 33%, and... the execution cost, which was up to 43%"; [page 9]: RMC "rose faster than the revenue". These are rupee growth rates against revenue growth of ~28%, not price-inflation rates. PRAJIND's 1-1.5% is a margin impact. The comparison is between two different quantities. B05 3B makes the same misread ("Input-cost inflation"). |
| B06 2E(i): "Fabtech's calls attribute delay only to war/donor-funding, never to routine client-side inspection or acceptance slippage" | NOT SUPPORTED | Feb-26 [page 12]: "they are not ready with their buildings"; Apr-26 [page 12]: "order conversion timelines are more variable on the client side, dependent on civil infrastructure readiness"; Apr-26 [page 19]: "delay challenges because the civil aspect got impacted"; Aug-26 [page 7]: "site readiness, and customer approvals". |
| B06 Q3 VERIFIED: "delay, not cancellation" in MENA/Africa, "meaningfully de-risks LBF1" | OVERSTATED | HLEGLAS deferral is domestic CDMO/agrochemical (HLEGLAS-Concall_Jun_2026 L588-596). PRAJIND's delays are domestic CBG (PRAJIND-Concall_Jun_2026 L162-165), and its engineering deferral was Praj's own choice on raw-material uncertainty (L188-190, L306-309). Only SETL May-2026 is export and war-linked (SETL-Concall_May_2026 L443). One relevant anchor, not three. The conclusion that it de-risks Fabtech's MENA order-book stagnation does not follow. |
| B06 Q6 CONTRADICTED: "no Indian peer" framing | OVERSTATED | Fabtech's claim covers turnkey pharma-plant design-build (Aug-26 [page 18]; Apr-26 [page 19] "no direct or indirect listed peers"). SETL and HLEGLAS describe competitive sets for process equipment, a different product. B06 itself says the contradiction is partial. UNVERIFIABLE is the right verdict. |
| B06 Q4: SETL "220 to 240 days" working-capital cycle | Misattributed (MINOR) | The figure is the analyst's premise in SETL Aug-2026 (L558-559), not May-2026. SETL management said "last year 320 days" (L563). |
| B06 2E(ii): Fabtech never ties cost to delay duration | Partly supported | Apr-26 [page 9], [page 21] tie execution cost to "remobilization" amid disruption, which is close to a delay-duration mechanism. |

---

## 3. Promise-delivery spot checks (B05 2A)

| B05 row | Earlier call has the promise? | Later call shows the outcome? | Result |
|---|---|---|---|
| Feb-26: Rs 20-22 Cr Q3 slip shows in Q4 | Yes. Feb-26 [page 5]: "Deferred revenues are expected to be recognised in Q4"; [page 6] Rs 20.3 Cr | Yes. Apr-26 [page 3]: Q4 total income Rs 168.24 Cr, +22% YoY; [page 7] "highest sales in the month of March" | CONFIRMED (note: the same Rs 20-22 Cr at port recurs at Q1 FY27 end, Aug-26 [page 16]) |
| Feb-26: FY26 revenue Rs 380-400 Cr, PAT Rs 39-41 Cr, outcome Partial | Yes. Feb-26 [page 8] | Yes. Apr-26 [page 3]: total income Rs 431.33 Cr, net profit Rs 38.36 Cr | CONFIRMED (basis note: Rs 431.33 Cr is total income including ~Rs 20-21 Cr other income, Apr-26 [page 18]) |
| Feb-26: European acquisition within 6 months, outcome Missed | Yes. Feb-26 [page 13]-[page 14]: "First quarter"; "before March 31st" | Yes. Apr-26 [page 15]: "The acquisition has yet not gone through" | CONFIRMED |
| Apr-26: "Two acquisitions (Europe + Saudi) in next 2-3 quarters", outcome Partial (SACE closed) | No. Apr-26 [page 15] speaks only of due diligence on "our JBN acquisition in the West". "Next two to three quarters" is Aug-26 [page 19] wording for the European deal. | No. Aug-26 [page 4]: SACE was "incorporat[ed]"; [page 4]-[page 5]: "our proposed acquisition in Italy and Saudi Arabia... complete both before the end of the current financial year". Neither acquisition has closed on the CEO's account. | WRONG |
| Nov-25: "Working capital efficiency... will support cash flow and deleveraging", outcome Delivered | No. Nov-25 [page 7]: Chirag Doshi promised receivable-cycle improvement only; no deleveraging promise. | The receivable promise failed (Apr-26 [page 3] Rs 204.34 Cr; Aug-26 [page 11] Rs 211 to ~215 Cr). B05 row 7 marks the same Nov promise Missed; row 10 marks it Delivered. | WRONG |
| Apr-26: FY27 PAT margin 9.9-10.5%, "Aug restated as 9-11% (a lower ceiling)" | Yes. Apr-26 [page 4]; but Apr-26 [page 21] Karan also gives "PAT level will be between 9 to 11%" | Aug-26 [page 19]: "9 to 11% PAT". 11% is a higher ceiling, not lower. | WRONG (misstatement; the inconsistency itself is real) |

Checked 6, confirmed 3, wrong 3. Corrected B05 tally: Delivered 1 (Q4 recovery), Partial 3, Missed 5, one row void (Apr "two acquisitions" has no Apr source). The Nov-25 order-book row ("9% growth per quarter") reads as Missed, not Partial: Jan-26 Rs 926 Cr sits below the ~Rs 985 Cr that "9% growth as of September 2025" implies (Nov-25 [page 5]).

---

## 4. Credibility grade

B05 grade: C (Mixed). This verifier would grade LOWER, C to D. The reasons:

- Seven material items are missed. Five are management contradicting itself or its earlier
  call: retention terms, revenue-recognition method, hot-lead pipeline size, SACE status,
  and the Nov-25 margin promise. The other two are the founder's admission of discretionary
  shipment timing and forex-heavy other income.
- Two B05 promise rows credit deliveries that did not happen (the SACE acquisition and
  Nov-25 "deleveraging"). Corrected, the tally moves from 2 delivered / 4 partial / 4 missed
  to 1 / 3 / 5.
- A four-call evasion on order-book composition sits at LOW-MEDIUM in B05 4D.

Symmetric note (Rule J). Three items cut the other way. FY26 revenue growth of ~28% was real.
The Q3 FY26 port slip did convert in Q4. Q1 FY27 contribution margin of 46.7% is a
reported number, not a promise. Management also volunteered bad news: the UAE drag
(Aug-26 [page 6]) and the receivable rise (Apr-26 [page 3]). The downgrade rests on
consistency of statements, not on business performance.

---

## 5. Scoring

- Independent items: 31 (1 CRITICAL, 20 MAJOR, 10 MINOR).
- Material: 21. CAUGHT 7, PARTIALLY CAUGHT 7, MISSED 7.
- material_caught counts CAUGHT plus PARTIALLY CAUGHT (the pipeline found the item but
  under-weighted it): 14 of 21 = 67%. On CAUGHT-only the rate is 7 of 21 = 33%. Both are
  stated so the orchestrator can apply either reading.
- No MISSED item is a repeated evasion. The one repeated evasion (item 4) was partially
  caught, so no CRITICAL finding stands.

---

```yaml
stage: B12b
company: "FABTECH"
run_date: "2026-09-26"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 31
caught: 9
partially_caught: 10
missed:
  - {severity: "MAJOR", item: "Founder admits discretionary revenue timing: Q3 revenue pulled into Q2, shipments held even when the LC permits shipping", anchor: "Concall_Feb_2026 [page 12], Aasif Khan"}
  - {severity: "MAJOR", item: "Revenue recognition described three different ways by different speakers (project progress, bill of lading, milestones and customer approvals)", anchor: "Concall_Apr_2026 [page 16] Aman Anavkar vs Ashwani Singh; Concall_Aug_2026 [page 3] Ashwani Singh vs [page 8] Karan Doshi vs [page 9] Aman Anavkar"}
  - {severity: "MAJOR", item: "Retention terms contradicted across calls: 'no retention over 6 months' (Feb) vs 'retention period of one to two years, 10 to 15%' (Aug)", anchor: "Concall_Feb_2026 [page 13] Aman Anavkar; Concall_Aug_2026 [page 11] Karan Doshi"}
  - {severity: "MAJOR", item: "Hot-lead pipeline figure swings: USD 455m (Feb) to 'close to 200 million odd USD' (Apr) to Rs 3,800 Cr hot leads plus Rs 9,300 Cr inquiries (Aug)", anchor: "Concall_Feb_2026 [page 7] Aasif Khan; Concall_Apr_2026 [page 11] Aman Anavkar; Concall_Aug_2026 [page 4], [page 7]"}
  - {severity: "MAJOR", item: "SACE described by the CEO as an incorporation with the Saudi acquisition still 'proposed', but by the CGO as 'acquired'; B05 credits a closed acquisition", anchor: "Concall_Aug_2026 [page 4]-[page 5] Ashwani Singh vs [page 6] and [page 19] Aman Anavkar"}
  - {severity: "MAJOR", item: "Nov-2025 margin promise 'better than last year, for sure' broken; FY26 EBITDA margin fell and management conceded margins shrank", anchor: "Concall_Nov_2025 [page 15] Aman Anavkar; Concall_Apr_2026 [page 3], [page 9]"}
  - {severity: "MAJOR", item: "Earnings quality: FY26 other income ~Rs 21 Cr of which ~Rs 12 Cr forex, against PAT Rs 38.36 Cr; Q3 FY26 other income Rs 7 Cr ~10% of revenue", anchor: "Concall_Apr_2026 [page 18] Karan Doshi; Concall_Feb_2026 [page 22] Karan Doshi"}
  - {severity: "MINOR", item: "Rs 20-22 Cr of goods at the port at quarter end recurs (Q3 FY26 and Q1 FY27)", anchor: "Concall_Feb_2026 [page 6], [page 8]; Concall_Aug_2026 [page 16] Karan Doshi"}
  - {severity: "MINOR", item: "Execution tenor drifts: 9-18 months 'speeding' (Feb) to 18-24 and 24-27 months (Apr) to 12-36 months (Aug)", anchor: "Concall_Feb_2026 [page 7]; Concall_Apr_2026 [page 12]; Concall_Aug_2026 [page 9]"}
  - {severity: "MINOR", item: "Ticket-size unit confusion: '30, $40 million... orders worth $70 million' vs '30 to 40... more than 50 crores, 60 crores' in the same call", anchor: "Concall_Apr_2026 [page 6] and [page 8] Karan Doshi"}
  - {severity: "MINOR", item: "CGO says no civil contract closed; CEO corrects him in the same answer", anchor: "Concall_Aug_2026 [page 14]"}
  - {severity: "MINOR", item: "Unusual analyst insistence on margin/growth guidance (five questioners) met with refusals in the first listed call", anchor: "Concall_Nov_2025 [page 4]-[page 5], [page 9]-[page 10], [page 15]-[page 16]"}
pipeline_flags_not_supported:
  - "B06 Q2/flags: 'magnitude gap, Fabtech RMC +33%/execution +43% cost inflation vs PRAJIND 1-1.5%'. The transcript says RMC cost 'grew up by close to 33%' and 'rose faster than the revenue' (revenue +28%): a rupee growth figure, not a price-inflation rate. The order-of-magnitude comparison rests on a misread (Concall_Apr_2026 [page 9], [page 21])."
  - "B06 2E(i) / risks_peers_raise: 'Fabtech's calls attribute delay only to war/donor-funding, never to routine client-side slippage'. Fabtech cites client civil-readiness and customer approvals repeatedly (Concall_Feb_2026 [page 12]; Concall_Apr_2026 [page 12], [page 19]; Concall_Aug_2026 [page 7])."
promise_delivery_spot_checks: {checked: 6, confirmed: 3, wrong: 3}
credibility_grade_concur: "lower: C to D. Seven material contradictions were missed, and two promise rows credit deliveries that did not happen (SACE acquisition, Nov-2025 deleveraging)."
findings:
  - {severity: "MAJOR", location: "B05 overall", item: "MISSED: founder admission of discretionary shipment/revenue timing", anchor: "Concall_Feb_2026 [page 12]"}
  - {severity: "MAJOR", location: "B05 overall", item: "MISSED: contradictory revenue-recognition descriptions across speakers and calls", anchor: "Concall_Apr_2026 [page 16]; Concall_Aug_2026 [page 3], [page 8], [page 9]"}
  - {severity: "MAJOR", location: "B05 4B peer question 4", item: "MISSED: retention terms contradiction; B05 adopts the Aug version as fact", anchor: "Concall_Feb_2026 [page 13]; Concall_Aug_2026 [page 11]"}
  - {severity: "MAJOR", location: "B05 1B", item: "MISSED: hot-lead pipeline figure swings USD 455m to USD ~200m to Rs 3,800 Cr", anchor: "Concall_Feb_2026 [page 7]; Concall_Apr_2026 [page 11]; Concall_Aug_2026 [page 4]"}
  - {severity: "MAJOR", location: "B05 1B, 2A row 4, 3D, trigger 1", item: "MISSED contradiction and misread: SACE incorporated per CEO, Saudi acquisition still proposed; B05 states 'closed'", anchor: "Concall_Aug_2026 [page 4]-[page 5] vs [page 6], [page 19]"}
  - {severity: "MAJOR", location: "B05 2A", item: "MISSED broken promise: FY26 margins 'better than last year, for sure'", anchor: "Concall_Nov_2025 [page 15]; Concall_Apr_2026 [page 9]"}
  - {severity: "MAJOR", location: "B05 overall", item: "MISSED: forex-heavy other income (~Rs 12 Cr of ~Rs 21 Cr) against PAT Rs 38.36 Cr", anchor: "Concall_Apr_2026 [page 18]"}
  - {severity: "MAJOR", location: "B05 4D", item: "UNDER-WEIGHTED: order-book/segment split refused in all four calls (repeated evasion) graded LOW-MEDIUM; Apr 'I'll just pull up the data' never delivered", anchor: "Concall_Nov_2025 [page 11]; Concall_Feb_2026 [page 12]; Concall_Apr_2026 [page 14]; Concall_Aug_2026 [page 13], [page 15]"}
  - {severity: "MAJOR", location: "B05 2D", item: "PARTIAL: related-party procurement 11% FTCL panels plus ~15% AHU via Advantek (Apr) restated as 'not more than 11%' (Aug); B05 misattributes the 15% to FTCL and misses the Aug understatement", anchor: "Concall_Apr_2026 [page 17]; Concall_Aug_2026 [page 19]"}
  - {severity: "MAJOR", location: "B06 Part 1 Q2, flags", item: "NOT SUPPORTED: 33%/43% read as cost inflation; it is rupee cost growth vs revenue +28%", anchor: "Concall_Apr_2026 [page 9], [page 21]"}
  - {severity: "MAJOR", location: "B06 Part 2E(i), risks_peers_raise", item: "NOT SUPPORTED: claim that Fabtech never cites client-side slippage", anchor: "Concall_Feb_2026 [page 12]; Concall_Apr_2026 [page 12], [page 19]; Concall_Aug_2026 [page 7]"}
  - {severity: "MAJOR", location: "B06 Part 1 Q3 VERIFIED", item: "OVERSTATED: HLEGLAS deferral is domestic CDMO/agro; PRAJIND delays are domestic CBG plus Praj's own deferral on RM-cost uncertainty; only SETL May-2026 is export/war-linked. 'Meaningfully de-risks LBF1' does not follow", anchor: "HLEGLAS-Concall_Jun_2026 L588-596; PRAJIND-Concall_Jun_2026 L162-165, L188-190, L306-309; SETL-Concall_May_2026 L443"}
  - {severity: "MAJOR", location: "B05 2A row 4", item: "PROMISE ROW WRONG: 'Apr-2026: two acquisitions in next 2-3 quarters' is not in the Apr call; outcome 'Saudi closed' contradicts CEO", anchor: "Concall_Apr_2026 [page 15]; Concall_Aug_2026 [page 4]-[page 5], [page 19]"}
  - {severity: "MAJOR", location: "B05 2A row 10", item: "PROMISE ROW WRONG: Nov-2025 promised receivable improvement only, not deleveraging; row marks Delivered while row 7 marks the same Nov promise Missed", anchor: "Concall_Nov_2025 [page 7]; Concall_Apr_2026 [page 3]"}
  - {severity: "MINOR", location: "B05 2A", item: "PARTIAL: Apr promise 'Q1 and Q2 the receivable will be reduced immediately' broken (Rs 211 to 215 Cr); Saudi receivable Rs 72.57 Cr vs Saudi Q1 revenue Rs 17.14 Cr, one ~Rs 120 Cr contract", anchor: "Concall_Apr_2026 [page 18]; Concall_Aug_2026 [page 3]-[page 4], [page 11]"}
  - {severity: "MINOR", location: "B05 trigger 5, B06 Part 5", item: "PARTIAL: Africa called margin-dilutive (Apr) then a higher-margin growth driver (Aug); PRAJIND says construction-heavy Africa orders dilute margin", anchor: "Concall_Apr_2026 [page 8]-[page 9]; Concall_Aug_2026 [page 6]; PRAJIND-Concall_Mar_2026 L358-367"}
  - {severity: "MINOR", location: "B05 3B, B06 Q2", item: "PARTIAL: same-call contradiction on cost impact ('very small... compensated' vs RMC +33%, execution +43%) and on pass-through (Apr 'I would not say pass on' vs Aug '>5% passing over')", anchor: "Concall_Apr_2026 [page 10], [page 11], [page 21]; Concall_Aug_2026 [page 16]-[page 17]; SETL-Concall_Aug_2026 L258-263"}
  - {severity: "MINOR", location: "B05 2D", item: "PARTIAL: FY28 PAT 12-14% 'we're on track' (Aman) vs Karan's PAT 9-11% target in the same call", anchor: "Concall_Apr_2026 [page 20], [page 21]"}
  - {severity: "MINOR", location: "B05 3D", item: "PARTIAL: repeat-customer share ~10% accepted as a 'deliberate strategy' reframe; it cuts against the Nov-2025 repeat-client moat narrative", anchor: "Concall_Aug_2026 [page 13]-[page 14]; Concall_Nov_2025 [page 6]"}
  - {severity: "MINOR", location: "B06 Part 1 Q6", item: "OVERSTATED: CONTRADICTED verdict rests on equipment makers' competitive sets; none operates in turnkey pharma-plant EPC", anchor: "Concall_Aug_2026 [page 18]; SETL-Concall_Nov_2025 L263-273"}
  - {severity: "MINOR", location: "B05 2A row 6", item: "Misstatement: 9-11% is a higher ceiling than 9.9-10.5%, not lower; Apr call itself also gives 9-11%", anchor: "Concall_Apr_2026 [page 4], [page 21]"}
  - {severity: "MINOR", location: "B05 overall", item: "MISSED: recurring Rs 20-22 Cr quarter-end port inventory", anchor: "Concall_Feb_2026 [page 6]; Concall_Aug_2026 [page 16]"}
  - {severity: "MINOR", location: "B05 overall", item: "MISSED: execution-tenor drift 9-18 to 12-36 months", anchor: "Concall_Feb_2026 [page 7]; Concall_Aug_2026 [page 9]"}
  - {severity: "MINOR", location: "B05 3D", item: "MISSED: ticket-size unit confusion (USD vs Rs Cr)", anchor: "Concall_Apr_2026 [page 6], [page 8]"}
  - {severity: "MINOR", location: "B05 3D", item: "MISSED: CGO/CEO contradiction on civil contracts", anchor: "Concall_Aug_2026 [page 14]"}
  - {severity: "MINOR", location: "B05 overall", item: "MISSED: Nov-2025 analyst insistence on guidance", anchor: "Concall_Nov_2025 [page 4]-[page 5], [page 15]-[page 16]"}
  - {severity: "MINOR", location: "B05 1C", item: "PARTIAL: win rate 15% (Feb) falls to 'now 11%' (Apr); noted only as 'basis shifts'", anchor: "Concall_Feb_2026 [page 9]; Concall_Apr_2026 [page 13]"}
  - {severity: "MINOR", location: "B05 trigger 1", item: "PARTIAL: scope drift from 'not focused on non-pharma' (Nov) to non-pharma MEP/civil via SACE (Aug) treated as positive trigger only", anchor: "Concall_Nov_2025 [page 12]; Concall_Aug_2026 [page 4], [page 19]"}
  - {severity: "MINOR", location: "B05 2C", item: "PARTIAL: FY23 revenue-fall question dodged and 'not discussing in a forum' not logged", anchor: "Concall_Feb_2026 [page 21], [page 22]"}
  - {severity: "MINOR", location: "B05 2D", item: "OVERSTATED: Company Secretary resignation (24-Sep-2026) post-dates every call; its absence from transcripts is not a disclosure failure", anchor: "Concall_Aug_2026 cover letter dated 03-Aug-2026"}
  - {severity: "MINOR", location: "B06 Part 1 Q4, Part 3", item: "Misattribution: 220-240 days is the analyst's figure in SETL Aug-2026 (not May-2026); SETL management said 320 days last year", anchor: "SETL-Concall_Aug_2026 L558-566"}
  - {severity: "MINOR", location: "B05 1B", item: "Nov-2025 '120 to 150 days' was a market-average receivable range, not the company WC cycle", anchor: "Concall_Nov_2025 [page 7]"}
critical_count: 0
major_count: 14
minor_count: 18
material_found: 21
material_caught: 14
acceptance_rate: 67
coverage_basis: "31 independent items listed (1 CRITICAL, 20 MAJOR, 10 MINOR); 21 material. Of the 21: 7 CAUGHT, 7 PARTIALLY CAUGHT, 7 MISSED. material_caught counts CAUGHT plus PARTIALLY CAUGHT (found, under-weighted) = 14, so 67%. On CAUGHT-only the rate is 7/21 = 33%. Across all 31 items: 9 caught, 10 partial, 12 missed. 16 transcripts read (4 main in full, SETL Nov-2025 and Aug-2026 in full, other 10 peers by targeted search plus context reads)."
```
