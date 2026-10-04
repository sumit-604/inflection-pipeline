# STAGE 12 VERIFIER B: COMMUNICATION RED-FLAG AUDIT, KWICK FORENSIC SOLUTIONS LTD (KWICK)

Run date 2026-10-04. Model claude-opus-5-5. Mode: NO-CONCALL (manifest concalls_available: false). Per prompts/00-orchestrator.md NO-CONCALL MODE, this audit tests the communication analysis against the prospectus, the 30-Sep-2026 deck and the BSE filings instead of transcripts. Peer transcripts (11) were read for peer statements that bear on Kwick claims.

Unit note. The prospectus and deck report in Rs lakh. Anchors: "P.nn" = PDF page of KWICK-Prospectus-2026-08-31.txt; "Deck p.nn" = page marker in Investor_Presentation_1.txt (same file as announcement 20260930-4e7a525d); BSE filings by date. "Computed" = my arithmetic on the cited filed numbers.

Independence note. I read the raw sources and built my own list before I scored it against B05 and B06. Where my list and the pipeline agree, I say so. Where I found filed evidence the pipeline did not use, I quote the page.

## 0. SOURCES READ AND COVERAGE

Read in full: BSE filings 24, 26, 27, 28 and 30-Sep-2026 (both 30-Sep files); the deck (22 pages); prospectus MD&A P.256-270; objects of the offer P.86-100; risk factors P.22-36; business P.135-140 and P.145-164; NFIES text P.123-124; basis for issue price P.106-108; group entities P.212-214.
Read by targeted search with context: Audit Committee constitution (P.196); related-party schedule (P.250 and the summary schedule near prospectus line 4000); monitoring agency (P.100); every "dealer", "NFSU" and "Varanasi" hit in the prospectus; SEBI order of 18-Aug-2026 (18 hits on the charge list and the direction).
Not read: risk factors P.36-50; business P.130-134 and P.141-144; restated notes other than the related-party schedule; the product catalogue.
Peers: DSSL Q4 FY26 (02-Jun-2026) and Q1 FY27 (14-Aug-2026) read in full. The other 9 peer transcripts were read by targeted search on the claims B06 relies on (DSO, debtor days, gross margin, hardware margin, Q4 revenue, announcements and thresholds, price rises, police, forensic, BNSS, guarantees), with context reads around each hit. The two DSSL files have the same line count but are different calls.

## 1. INDEPENDENT RED-FLAG LIST (built from the raw sources)

Severity uses the shared scale. No item is CRITICAL. Rule 5 reserves CRITICAL for a missed repeated evasion over 2 or more quarters. No quarterly record exists in this mode, so no such evasion is possible.

| # | Item | Anchor | Severity |
|---|---|---|---|
| R1 | Disclosure sequence. The company filed a conference intimation on 24-Sep, before the price query. On Sat 26-Sep it told BSE it was "not aware of any information, event, development or impending announcement". On Sun 27-Sep it filed a Reg 30 note on a third-party Rs 150 crore NFSU Varanasi campus: "well positioned to participate". The note names no Kwick order, tender or amount. The trading window closes from 01-Oct, the day after the 30-Sep conference. The 30-Sep deck does not mention Varanasi. The prospectus has zero hits for Varanasi. | 20260924 p.1; 20260926 p.1; 20260927 p.1; 20260928 p.1; Deck p.15; prospectus search. Weekdays computed (01-Jan-2026 is a Thursday) | MAJOR |
| R2 | Deck "130 Total no. of customers served" against the auditor-certified KPI of 95 (FY26), 124, 128. The deck gives no period for 130. | Deck p.6; P.164, P.259, RF2 P.23 | MAJOR |
| R3a | The dealer and vehicle-builder channel (kits for 95 vehicles, Rs 2,035.74 lakh) is explained in the business section only. MD&A credits FY26 growth to Physical Evidence (2.10x) and Cyber (2.34x). It is silent on the channel and on the Mobile CSI fall (Rs 1,640.66 lakh to Rs 1,056.76 lakh). The segment that books the kit revenue is not stated. | P.150, P.140, P.265, P.24 | MAJOR |
| R3b | The channel revenue equals two named-by-rank customers. Top Customer 2 (Rs 1,201.40 lakh) plus Top Customer 4 (Rs 834.35 lakh) = Rs 2,035.75 lakh (computed). Kit revenue is Rs 2,035.74 lakh. Their amounts match the Maharashtra (Rs 1,204.55 lakh, FY25 Rs 64.46 lakh) and Rajasthan (Rs 834.42 lakh, FY25 Rs 16.23 lakh) state totals. P.140 says the "local dealers" do vehicle procurement and fabrication, and "Vehicles are also subjected to pre-dispatch inspections by the client and following client acceptance procedures". [INFERENCE] | P.160, P.159, P.150, P.140 | MAJOR |
| R4 | The day counts sit on an unstated basis. The P.91 table labels debtor days "Revenue from Operations" and shows 83 / 89 / 74. The same section prints receivables / revenue of 39.54% / 30.43% / 21.64% (= 144 / 111 / 79 days at year end). The stated days reproduce on AVERAGE balances in all three years: 83.1 / 89.0 / 73.7 (computed; FY24 opening receivables Rs 180.79 lakh = Rs 1,193.58 lakh less the Rs 1,012.79 lakh change on P.93). P.92 then explains the FY25 89 days by Q4 = 51% of sales "inflating the outstanding receivables on the closing balance sheet date". That is a year-end mechanism used to explain an average-basis number. | P.91, P.92, P.93 | MAJOR |
| R5 | The payables fall has two incompatible explanations. P.91 says "conscious effort to settle payables faster, enabling it to negotiate more favorable credit terms and competitive pricing". P.94 says "intentional transition" that "positioned the company to command better pricing and cash discounts". P.98 says payables fell "primarily due to supplier requirements for partial advance payments". P.96 cites "limited bargaining power ... suppliers generally insist on shorter credit periods". In the same year COGS rose from 68.85% to 72.94% of revenue, so no pricing gain shows. P.98 explains the +91.79% rise in other current assets by tax, TDS and deposits only. It omits the supplier advances that P.98 itself says suppliers now require. | P.91, P.94, P.96, P.98, P.93, P.257 | MAJOR |
| R6 | The company presents E-Forensics as in-house work, but the software came from a related party. P.151: "From the start of F.Y 2025-26, our dedicated R&D team are developing ... E-Forensics". Deck p.12: "Powered by Kwick Forensics, 100% Made in India". The related-party schedule shows "Purchase of Asset (Software)" from Gostocks Fintech Pvt Ltd of Rs 58.70 lakh in FY25 and Rs 20.00 lakh in FY26. It also shows software programming fees to Gostocks of Rs 6.50 lakh (FY24), Rs 0.25 lakh (FY25) and Rs 3.00 lakh (FY26). Gostocks is a group entity where a director has significant influence. Its parent Gostocks Financial Services lists the promoter as a director. FY25 intangibles under development rose from nil to Rs 61.70 lakh, so Rs 58.70 lakh bought from Gostocks in that year was 95.1% of the new balance (computed). The FY25 purchase also predates the stated FY26 start. | P.151, Deck p.12, P.250 related-party schedule, P.213-214, Deck p.19 | MAJOR |
| R7 | The margin claims went against the outcome. P.153 says domestic sourcing aimed at "improving gross margins". P.140 says the dealer shift keeps "maintaining margins". Gross margin on revenue fell from 37.30% to 31.15% to 27.06% (100 less COGS of 62.70% / 68.85% / 72.94%). | P.153, P.140, P.257 | MAJOR |
| R8 | Domestic sourcing rose to 91.35%, but the product range is foreign-OEM and the award list calls Kwick a Thermo Fisher "Channel Partner" (2023, 2024) and an MH Service "Partner of the Year". [INFERENCE] The domestic share likely measures purchases of foreign-OEM goods through Indian entities. If so, the import cut is a change of form, not of value added. Separator: identity of Top Supplier 1 (Rs 3,268.40 lakh, 40.86% of purchases). | P.146-148, P.149, P.153, P.161; Deck p.8-10 | MINOR |
| R9 | Customers served fell 128 / 124 / 95 while revenue rose 3.5x. Revenue per customer went from Rs 23.6 lakh to Rs 111.3 lakh (computed). No filing explains the fall. | P.259, RF2 P.23 | MAJOR |
| R10 | The deck says "End-to-end development and manufacturing". The prospectus says "not a manufacturing unit" (P.158) and "not engaged in full manufacturing" (P.136), yet its own working-capital text speaks of "forensic equipment manufacturing" (P.91). | Deck p.11; P.158, P.136, P.91 | MINOR |
| R11 | Deck market blocks conflict with the prospectus. (a) Deck "Govt outlay of Rs 1,852 cr" for DNA and cyber, against Rs 18,528 lakh (Rs 185.28 Cr) in the prospectus. (b) The deck calls the Rs 200 Cr item a "National Forensic Data Centre ... at 7 CFSLs", while the prospectus calls it "Rs 20,000 lakhs out of Rs 2,08,050 lakhs for 20 States". (c) The deck says "over 1,000" mobile labs on p.16 next to "433 mobile forensic vans" on p.15. | Deck p.15-16; P.150, P.266-267 | MINOR |
| R12 | MD&A says "Our Company's business is not seasonal". The working-capital text says Q4 FY25 was 51% of yearly sales and cites "higher sales concentration in March" for FY26. | P.270, P.92, P.98 | MAJOR |
| R13 | The Audit Committee was constituted by Board resolution dated 04-Jul-2026. The KPIs are "approved by a resolution of our Audit Committee dated 25-05-2026", and that resolution is filed as material document 24. | P.196 (prospectus line 12207); P.256; prospectus line 24984 | MAJOR |
| R14 | IPO object sizing. The FY27 gap is Rs 4,442.00 lakh against a FY26 gap of Rs 3,587.13 lakh, an increment of Rs 854.87 lakh (computed). The IPO puts in Rs 3,142.00 lakh. The plan counts Rs 750 lakh of cash as a working-capital asset. P.96 calls a 31.1% rise in receivables "marginal". No monitoring agency is required (fresh issue under Rs 5,000 lakh). | P.90, P.96, P.100 | MAJOR |
| R15 | The FY27 plan contains a revenue signal in the company's own words. P.96: receivables of Rs 3,000 lakh are a "marginal increase ... in line with the projected growth in revenues". From Rs 2,288.07 lakh that is +31.1% (computed). P.95-96 add stock for "anticipated growth" and "anticipated increase in sales volumes". [INFERENCE] Management's working assumption sits near +31%, outside B05's derived +18% to +23% cluster. | P.95, P.96, P.90 | MAJOR |
| R16 | Employee cost rose 121% in FY25 and 27.49% in FY26 "mainly due to increase in the remuneration of Directors and KMP", described as "in line with industry standards". | P.266, P.267 | MINOR |
| R17 | MD&A credits FY26 revenue growth partly to a PIB release of 03-Jan-2026 on a Rs 30,000 crore plan "over the next five years". A plan announced in the last quarter of FY26, for future years, cannot explain FY26 revenue. | P.265 | MINOR |
| R18 | Pre-IPO placement holders held 14,34,360 shares after the bonus. They held 8,61,920 on 14-Aug-2026, so 5,72,440 shares (39.9%) moved before listing (computed). The CCV fund, which a BRLM director holds units in, went from 2,81,224 to 1,56,224. Buyers and prices are not disclosed. The move falls below the 5% threshold for secondary-transaction disclosure on P.107. | P.34, P.33, P.107 | MINOR |
| R19 | Risk factor 15 sits under the heading "Our BRLM is Subject to SEBI Regulations and general routine Inspections". The text then discloses a SEBI order barring new mandates for one month (stayed by SAT on 24-Aug-2026). The heading softens the content. | P.33; SEBI order (direction near line 814) | MINOR |
| R20 | Deck tenure and partnership claims overstate the prospectus. The deck says "Founded in 2005", "20+ Years Of Experience" and "12+ Global OEM Partnerships". The prospectus says forensic activity began in 2015 (RF7), cites experience "from a decade", deals with OEMs "on a deal-to-deal basis", and states "We have not entered into any technical or other collaboration". | Deck p.5-6; P.27, P.149, P.158 | MINOR |
| R21 | P.87 confirms "the activities which we have been carrying out till date are in accordance with the object clause". RF7 says forensic activity from 2015 was not aligned with the object clause until April 2025, and the ROC levied penalties of Rs 2.5 lakh in total. | P.87, P.27-28 | MINOR |
| R22 | The proof-of-concept lab runs its cyber tools on "demo licences for short periods as and when required". Four R&D employees sit at the branch, which the promoter leases to the company at Rs 1.75 lakh a month. The deck presents an "R&D Center & Private Forensic Lab Facility" and "DSIR-recognized R&D capabilities". | P.31, P.156, P.30-31; Deck p.5, p.11 | MINOR |
| R23 | P.140 dates the dealer shift "From mid of FY 25". FY25 was the record year for complete vans (47), and P.150 frames the shift as an FY26 change. | P.140, P.259, P.150 | MINOR |
| P1 | Peer margin levels. ADSL says a "player who is only doing the hardware business, they will have single-digit margins ... I am talking about gross margin". DSSL resale gross margin was "traditionally like 12-13%" (analyst figure, not disputed) and fell from 18% to 14% in Q4 FY26. Kwick earns 27.06% gross margin on revenue on a 91.08% goods mix. Kwick sits ABOVE the peer resale band, not inside it. | ADSL Feb-2026 (Q3 FY26), Nehal Shah, [page 13]; DSSL Jun-2026 (Q4 FY26), [page 8] and [page 11]; P.257, P.24 | MAJOR |
| P2 | Peer Q4 revenue shares are 26% to 34% (Zen FY25 Rs 325 Cr of Rs 973.6 Cr; DSSL FY26 Rs 402 Cr of Rs 1,424 Cr). Kwick's Q4 FY25 was 51%. | ZENTEC May-2026 transcript lines 270-303; DSSL Jun-2026 [page 5]; P.92 | MAJOR |
| P3 | The DSSL CFO says early payment to OEMs makes no sense unless it brings cost efficiency, and OEMs and distributors give "higher credit lines". Kwick claims faster payment wins pricing (P.94) while its margin fell. | DSSL Jun-2026 [page 11]; P.94 | MINOR |
| P4 | Peers file orders with buyer, value and a stated threshold. ADSL's threshold is "about 10% of our top line". Kwick's 27-Sep note names no order. | ADSL Feb-2026 lines 939-941; DSSL Aug-2026 [page 4], [page 17]; 20260927 p.1 | MINOR |
| P5 | Peers report hardware price rises of 25% to 50% and tender walk-aways. Kwick's filings carry no input-price risk for its cyber resale line (33.32% of FY26). | DSSL Aug-2026 [page 8]; ADSL May-2026 line 518, Aug-2026 line 428; P.24 | MINOR |

Totals: 29 items. 0 CRITICAL, 15 MAJOR, 14 MINOR.

### 1A. Depth on the four items the pipeline missed or under-weighted

R3b, the dealer channel (bears on LBF-1, the run's first verification priority).
- Fact (computed): Top Customer 2 + Top Customer 4 = Rs 2,035.75 lakh. The P.150 kit revenue is Rs 2,035.74 lakh. Rajasthan revenue (Rs 834.42 lakh) is almost all Top Customer 4 (Rs 834.35 lakh). Maharashtra revenue (Rs 1,204.55 lakh) is almost all Top Customer 2 (Rs 1,201.40 lakh).
- Fact: P.140 says the end client inspects each vehicle before dispatch and runs its acceptance procedure.
- [INFERENCE] Two counterparties carry the whole channel and 19.25% of FY26 revenue. The end users are most likely agencies in Maharashtra and Rajasthan, with a local dealer as the billed party. This favours B05's Reading A (a billing artefact). Suppose the channel revenue is counted back to government end users. Then the FY26 government share is (5,837.36 + 2,035.74) / 10,571.28 = 74.5% (computed), not the 55.22% printed on P.160. The LBF-1 "customer shift" from 86.98% then shrinks to about 12 points.
- Two readings. A: dealers are pass-through billing parties for state police buyers in two states. Collection risk then sits with a state payer behind a dealer. B: the two parties are real private buyers that pay 30% to 50% at delivery (P.92).
- Separator: the buyer class of Top Customers 2 and 4 and their receivables ageing. Halt 1 can ask for this as a filed-document extraction. Whether Maharashtra and Rajasthan police bought mobile forensic vans in FY26 is PENDING LIVE VERIFICATION.
- B05 states "Names of dealers, builders or any top-10 customer. Buyer class of this revenue. End-user state ... NOT FOUND" and "The filings give neither" for the separator. The match above was in the tables B05 cited.

R5, the payables story (bears on LBF-3, cash conversion).
- The company gives a voluntary reason (P.91, P.94) and a forced reason (P.96, P.98) for the same Rs 172.01 lakh fall. The voluntary version claims better pricing and cash discounts. Gross margin fell 4.09 points that year (P.257).
- [INFERENCE] The forced reading fits the numbers. A top supplier at 40.86% of purchases (P.161), up from 12.50% in FY24, now sets terms. That is supplier power over Kwick, not the reverse. It also explains why the FY27 plan cuts creditor days to 30 (P.95).
- B05 records only the P.98 reason and classes it as "external-blame". It does not flag the contradiction or the unsupported pricing claim.

R6, the in-house software claim (bears on the Quality Ladder rung and on any Pillar 3 or Entrepreneur Ledger credit for own IP).
- The filed related-party schedule shows Rs 58.70 lakh of software bought from Gostocks Fintech in FY25 and Rs 20.00 lakh in FY26. The prospectus text and the deck call the suite in-house and "100% Made in India".
- Two readings. A: Gostocks is a contract developer to Kwick's specification, and Kwick owns the code. B: the IP sits in a promoter-linked company, and Kwick capitalises a related-party purchase as development.
- Separator: the IP assignment terms in the Gostocks contract, and whether the intangible-under-development balance is ever commissioned into revenue.
- B05 wrote "prototypes outsourced to a related-group vendor" inside a kill signal with no anchor. Its body text and flags do not carry this, and P.152 calls the AI and LIMS vendor "a third party". The related-party source is the filed fact the pipeline left out.

R15, the FY27 revenue signal (bears on the Stage 11 26.1 base-revenue input).
- B05 calls its derived +18% to +23% cluster "the only forward revenue evidence in the filings". P.96 says the receivables build is "in line with the projected growth in revenues", which is +31.1% on the stated balances.
- Two readings. A: management works to roughly +31% revenue growth and sized the receivables to match. B: the sentence is loose drafting ("marginal" for +31%), and the day-count arithmetic is the better guide.
- Separator: H1 FY27 revenue and receivables, due after the trading window reopens (20260928 p.1).
- This does not make B05's arithmetic wrong. It means Stage 11 has three forward readings (+18-23% average basis, about +31% on the company's own words, +40% at year-end days), not one tight cluster.

## 2. COMPARISON AGAINST THE PIPELINE (B05, B06)

| # | Severity | Status | Where the pipeline has it, or what it lacks |
|---|---|---|---|
| R1 | MAJOR | CAUGHT | B05 LBF-4, FLAG-DISCLOSURE-CONDUCT, 4D. Balanced two readings. B05's sequence starts at the 25-Sep query and does not use the 24-Sep conference intimation, a minor gap |
| R2 | MAJOR | CAUGHT | B05 1C, 4D (HIGH) |
| R3a | MAJOR | CAUGHT | B05 FLAG-CHANNEL-OMISSION, 4D (HIGH) |
| R3b | MAJOR | MISSED | B05 LBF-1 says buyer class, end-user state and separator are not in the filings. The P.160 + P.159 match and P.140 text were not used |
| R4 | MAJOR | CAUGHT | B05 LBF-2, FLAG-GUIDANCE-BASIS. B05 says FY24 83 "cannot be tested"; it can (P.93), and it reproduces |
| R5 | MAJOR | PARTIALLY CAUGHT | B05 2B and LBF-3 carry the P.98 reason only, classed "external-blame". The P.91/P.94 voluntary version and the pricing claim are absent |
| R6 | MAJOR | PARTIALLY CAUGHT | B05 timeline_slippages catches the CWIP date. The related-party purchase appears only as an unanchored phrase in trigger 6's kill signal |
| R7 | MAJOR | CAUGHT | B05 2A row 2b MISSED |
| R8 | MINOR | PARTIALLY CAUGHT | B05 3A notes Kwick is "a channel for principals". Row 2a is scored DELIVERED without the form-versus-substance caveat |
| R9 | MAJOR | CAUGHT | B05 FLAG-CUSTOMER-COUNT, 4D |
| R10 | MINOR | CAUGHT | B05 1C, 4D. P.91's own "manufacturing" wording not cited |
| R11 | MINOR | CAUGHT | B05 3B, 4D, PENDING LIVE VERIFICATION. The Rs 200 Cr re-description is not noted |
| R12 | MAJOR | CAUGHT | B05 4D, 3C |
| R13 | MAJOR | CAUGHT | B05 LBF-4 conduct items, 4D |
| R14 | MAJOR | CAUGHT | B05 1B, 4D |
| R15 | MAJOR | PARTIALLY CAUGHT | B05 1B derives FY27 revenue but misses the P.96 sentence and overstates "only forward evidence" |
| R16 | MINOR | MISSED | Not in B05 |
| R17 | MINOR | MISSED | Not in B05 |
| R18 | MINOR | MISSED | B05 notes only that the BRLM-linked fund held shares. Governance, route to stage 8 |
| R19 | MINOR | MISSED | Not in B05 |
| R20 | MINOR | MISSED | Not in B05 |
| R21 | MINOR | PARTIALLY CAUGHT | B05 2B catches RF7; the P.87 statement that contradicts it is not noted |
| R22 | MINOR | PARTIALLY CAUGHT | B05 catches "demonstration only"; demo licences and staffing not noted |
| R23 | MINOR | MISSED | Not in B05 |
| P1 | MAJOR | PARTIALLY CAUGHT | B06 Q3 catches the mix mechanism. Its level read is inverted (see finding F5) |
| P2 | MAJOR | CAUGHT | B06 Q4, FLAG-Q4-LOADING-OUTLIER |
| P3 | MINOR | CAUGHT | B06 cross_peer_hypothesis, FLAG-SUPPLIER-CREDIT-DIVERGENCE |
| P4 | MINOR | CAUGHT | B06 Q8 |
| P5 | MINOR | CAUGHT | B06 FLAG-INPUT-COST-NOT-IN-B05 |

Totals: 15 caught, 7 partially caught, 7 missed (29). Material (15): 10 caught, 4 partially caught, 1 missed.

### 2A. Pipeline flags not on my independent list

| Pipeline flag | Assessment | Evidence |
|---|---|---|
| B05 4D LOW: MD&A FY26 financing text calls the repayment "proceeds" and lists a long-term repayment that fell in FY25; deck PBT 1,921.45 | SUPPORTED | P.268 "proceeds from short-term borrowings of Rs 325.61 Lakhs" against the borrowing going to nil (Deck p.19); long-term borrowings nil at FY25 end (Deck p.19). Deck p.20 total income 10,580.34 less total expenses 8,758.90 = 1,821.44 (computed) |
| B05 minor consistency items: purchases Rs 7,446.06 lakh vs P&L Rs 7,998.16 lakh; provisions 429.69 vs 492.69; "Fresh Offer ... Rs 5,077.44 lakh"; supplier FY25 total "100.00" | SUPPORTED | P.31-32, P.264; P.98 vs P.90; P.87 (45,61,600 x Rs 90 = Rs 4,105.44 lakh, computed); P.162 |
| B06 FLAG-PEER-STRUCTURAL-ONLY | SUPPORTED | Search of the peer transcripts: no forensic, BNSS, FSL, GeM or guarantee hits |
| B06 FLAG-SUPPLIER-CREDIT-DIVERGENCE | SUPPORTED | DSSL Jun-2026 [page 10] payables "134 days" (analyst figure), [page 11] net WC 14 to 17 days; Kwick creditor days 44 to 30 (P.95-96) |
| B06 FLAG-INPUT-COST-NOT-IN-B05 | SUPPORTED | DSSL Aug-2026 [page 8] "30%, 50%"; ADSL May-2026 line 518 "25%, 30%" |

pipeline_flags_not_supported: none. No B05 or B06 red flag invents a signal.

## 3. PROMISE-DELIVERY SPOT CHECKS (B05 Section 2A)

| Row | Promise in the source? | Outcome in the source? | Verdict |
|---|---|---|---|
| 1 Reduce Bihar and Gujarat dependence | Yes, P.152 strategy 5 | Bihar 34.53% / 21.80% / 9.02%; Gujarat 22.77% / 20.07% / 29.39% (P.23, P.159) | CONFIRMED (PARTIAL) |
| 2a Raise domestic sourcing | Yes, P.153 | 65.42% / 85.72% / 91.35% (P.153, P.28) | CONFIRMED (DELIVERED) in form. Substance caveat R8 |
| 2b Domestic sourcing improves gross margin | Yes, P.153 "improving gross margins" | COGS 62.70% / 68.85% / 72.94% of revenue (P.257) | CONFIRMED (MISSED) |
| 4 Debtor days fall via private mix and 30% to 50% advance | Yes, P.92, P.97 | 89.0 to 73.7 average, 111 to 79 year end (computed from P.90-93) | CONFIRMED (PARTIAL) |
| 5 Improved collections repaid all borrowings | Yes, P.266 | Short-term borrowings Rs 325.61 lakh to nil (Deck p.19); D/E 0.12 to 0 (P.257) | CONFIRMED (DELIVERED). B05's caveat that the repayment "came from cash held" is not supported (finding F6) |
| 7 Better inventory planning, order-basis buying | Yes, P.266 | 756.63 / 4,477.15 x 365 = 61.7 days; 1,043.71 / 7,711.08 x 365 = 49.4 days (computed from P.90, P.264) | CONFIRMED (DELIVERED) |

Checked 6, confirmed 6 on direction, wrong 0.

## 4. CREDIBILITY GRADE

Concur with C. NO-CONCALL mode defaults to C, and only documented delivery evidence can lift it to B. Nothing here supports B. The evidence sits at the low end of C. Four items B05 did not weigh push that way: the payables contradiction (R5), the related-party source behind the in-house software claim (R6), the P.96 revenue sentence (R15), and the dealer channel concentration in two counterparties (R3b). The 35 / 45 / 20 weights B05 passes to Stage 11 follow from C and do not change.

## 5. CONSOLIDATED FINDINGS (against the pipeline's analysis)

| # | Severity | Location | Finding | Anchor |
|---|---|---|---|---|
| F1 | MAJOR | B05 LBF-1, 2D, 3C; B05 YAML input_gaps | Missed filed evidence that narrows LBF-1. Kit revenue equals Top Customers 2 + 4 (Rs 2,035.75 lakh vs Rs 2,035.74 lakh), which match the Maharashtra and Rajasthan totals. P.140 says the end client inspects before dispatch. B05 says the filings hold no separator; they hold a strong one for Reading A. Government share re-attributed: about 74.5%, not 55.22% (computed) | P.160, P.159, P.150, P.140 |
| F2 | MAJOR | B05 2B, LBF-3 | Payables contradiction not flagged. Voluntary (P.91, P.94: better pricing, cash discounts) against forced (P.96, P.98: supplier advances, limited bargaining power), with the gross margin down 4.09 points. B05 classes it "external-blame" from P.98 alone | P.91, P.94, P.96, P.98, P.257 |
| F3 | MAJOR | B05 trigger 6 kill signal; timeline_slippages; 2D | The related-party software source is not surfaced. Gostocks Fintech (group entity) sold Rs 58.70 lakh (FY25) and Rs 20.00 lakh (FY26) of software against an in-house, "100% Made in India" claim. B05's "related-group vendor" phrase is unanchored and missing from flags and red_flags | P.250 related-party schedule; P.151; Deck p.12, p.19; P.213-214 |
| F4 | MAJOR | B05 1B [INFERENCE 3]; analyst_note; NOTES FOR LATER STAGES | "Only forward revenue evidence" overstated. P.96 ties the +31.1% receivables build to "the projected growth in revenues". Stage 11 should carry three forward readings (+18-23%, about +31%, +40%) with the H1 FY27 separator, not one cluster | P.96, P.95, P.90 |
| F5 | MAJOR | B06 Q3 verdict and net read; B06 input_gaps; B05 2A row 2b label | B05 labels the KPI margin "gross margin on COGS". P.257 prints COGS as % of revenue, so 27.06% is gross margin on REVENUE. B06 inherited the label, converted 27.06% to "about 21.3% of revenue" and concluded Kwick "sits inside the peer resale band". With the correct basis Kwick sits above it: ADSL hardware-only gross margin single digits; DSSL resale 12-13% and 14% to 18%. The mechanism verdict stands. The "rough range" verdict does not. Consequence for Stage 11: a bear case should test convergence toward peer resale margins. (Verifier A owns the number; this row is the interpretive consequence.) | P.257, P.24; ADSL Feb-2026 [page 13]; DSSL Jun-2026 [page 8], [page 11] |
| F6 | MINOR | B05 2A row 5; B05 YAML promise_delivery row 6 | The caveat "repayment came from cash held ... built by the Rs 9.48 Cr net FY25 placement" is not supported. FY26 cash rose from Rs 1,206.79 lakh to Rs 1,316.32 lakh. FY26 CFO of Rs 762.30 lakh covered investing (Rs 273.17 lakh) and financing outflows (Rs 379.60 lakh). The DELIVERED verdict stands | P.268; Deck p.20 |
| F7 | MINOR | B05 LBF-2 | "FY24 83 cannot be tested" is wrong. Opening FY24 receivables are Rs 180.79 lakh (P.93), and the average basis gives 83.1 days. The flag gets stronger: 3 of 3 years reproduce | P.93, P.91 |
| F8 | MINOR | B05 2A row 2a | DELIVERED is scored on form only. The award list (Thermo Fisher channel partner) and the foreign-OEM range suggest the domestic share measures purchases of imported goods from Indian entities [INFERENCE]. Separator: identity of Top Supplier 1 | P.146-149, P.153, P.161 |
| F9 | MINOR | B05 overall | Six minor items missed: director and KMP pay as the driver of employee cost growth (P.266-267); FY26 growth credited to a Jan-2026 forward plan (P.265); 39.9% of pre-IPO placement shares moved before listing (P.34); softened RF15 heading (P.33); deck tenure and partnership claims (Deck p.5-6 vs P.27, P.149, P.158); dealer shift dated mid-FY25 (P.140) | as listed |
| F10 | MINOR | B06 Part 1 Q4 and Part 4 vs flags and analyst_note | Internal inconsistency in the peer Q4 range: "26% to 34%" in the text, "26% to 33%" in the flag (Zen FY25 33.4% computed) | B06 report |
| F11 | MINOR | B05 FLAG-CHANNEL-OMISSION | "Explained only in business strategy p.150" is imprecise. P.140 (business overview) also describes the channel and dates it from mid-FY25 | P.140 |

Counts: 0 CRITICAL, 5 MAJOR, 6 MINOR.

## 6. SCORING

Material independent items (CRITICAL + MAJOR): 15 of 29 listed. Of those, 10 fully CAUGHT, 4 PARTIALLY CAUGHT, 1 MISSED.
Rule used for material_caught: full catches only. A partial catch here means the pipeline lacked the red-flag element itself (the contradiction, the related-party source, the company's own sentence, the correct margin basis), so it is not counted as "already had". On this rule the acceptance rate is 10 / 15 = 66.7%. If partial catches counted, it would be 14 / 15 = 93.3%. The denominator is 15, so rule 7 does not apply and the rate is reported.

No REWORK trigger from this verifier. No CRITICAL, and the rate is above 60%. The five MAJOR findings are fixes for the Halt 1 dossier and the Stage 11 inputs: F1 and F3 for LBF-1 and the Pillar 3 or Entrepreneur Ledger reading, F2 for LBF-3, F4 for the 26.1 base, F5 for the margin bridge.

```yaml
stage: B12b
company: "KWICK"
run_date: "2026-10-04"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 29
caught: 15
partially_caught: 7
missed:
  - {severity: "MAJOR", item: "Dealer/vehicle-builder kit revenue (Rs 2,035.74 lakh) equals Top Customer 2 + Top Customer 4 (Rs 1,201.40 + 834.35 = 2,035.75 lakh, computed), matching Maharashtra (1,204.55) and Rajasthan (834.42) state totals; p.140 says the end client does pre-dispatch inspection and acceptance. Favours Reading A of LBF-1; government share re-attributed about 74.5% vs 55.22% printed", anchor: "Prospectus p.160, p.159, p.150, p.140"}
  - {severity: "MINOR", item: "Employee cost growth attributed mainly to Director and KMP remuneration in FY25 (+121%) and FY26 (+27.49%)", anchor: "Prospectus p.266, p.267"}
  - {severity: "MINOR", item: "MD&A credits FY26 revenue growth to a 03-Jan-2026 PIB forward five-year Rs 30,000 crore plan", anchor: "Prospectus p.265"}
  - {severity: "MINOR", item: "Pre-IPO placement holders moved 5,72,440 of 14,34,360 post-bonus shares (39.9%, computed) before 14-Aug-2026; CCV fund (BRLM-director-linked) 2,81,224 to 1,56,224; buyers and prices undisclosed, below 5% threshold", anchor: "Prospectus p.34, p.107"}
  - {severity: "MINOR", item: "Risk factor 15 headed 'general routine Inspections' discloses a SEBI one-month ban order on the BRLM", anchor: "Prospectus p.33"}
  - {severity: "MINOR", item: "Deck 'Founded in 2005', '20+ Years', '12+ Global OEM Partnerships' vs forensic activity from 2015, 'a decade', deal-to-deal OEM terms and 'no technical or other collaboration'", anchor: "Deck p.5-6; Prospectus p.27, p.149, p.158"}
  - {severity: "MINOR", item: "Dealer shift dated 'from mid of FY 25' on p.140 while FY25 was the record complete-van year (47) and p.150 frames the shift as FY26", anchor: "Prospectus p.140, p.259, p.150"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "concur: C is the no-concall default and nothing documents delivery strong enough for B; evidence sits at the low end of C (payables contradiction, related-party source of the in-house software, two-counterparty dealer channel)"
findings:
  - {severity: "MAJOR", location: "B05 LBF-1, 2D, 3C, input_gaps", finding: "Missed filed evidence narrowing LBF-1: kit revenue = Top Customers 2+4, matching MH and RJ state totals; p.140 end-client pre-dispatch inspection. B05 states no separator exists in the filings", anchor: "Prospectus p.160, p.159, p.150, p.140"}
  - {severity: "MAJOR", location: "B05 2B, LBF-3", finding: "Payables fall explained as voluntary for better pricing and cash discounts (p.91, p.94) and as supplier-forced with limited bargaining power (p.96, p.98); gross margin fell 4.09 points. B05 records only p.98 as external-blame", anchor: "Prospectus p.91, p.94, p.96, p.98, p.257"}
  - {severity: "MAJOR", location: "B05 trigger 6 kill signal, timeline_slippages, 2D", finding: "Related-party software purchase from group entity Gostocks Fintech (Rs 58.70 lakh FY25, Rs 20.00 lakh FY26) behind an in-house, 100% Made in India E-Forensics claim is not surfaced; B05 phrase 'related-group vendor' is unanchored", anchor: "Prospectus p.250 related-party schedule, p.151, p.213-214; Deck p.12, p.19"}
  - {severity: "MAJOR", location: "B05 1B INFERENCE 3, analyst_note, notes for later stages", finding: "'Only forward revenue evidence' overstated: p.96 ties the +31.1% receivables build to projected revenue growth; Stage 11 needs three forward readings (+18-23%, about +31%, +40%) with the H1 FY27 separator", anchor: "Prospectus p.96, p.95, p.90"}
  - {severity: "MAJOR", location: "B06 Q3 verdict and net read, B06 input_gaps; B05 2A row 2b label", finding: "Gross margin mislabelled 'on COGS'; 27.06% is on revenue (p.257). B06 conversion to 21.3% and 'inside the peer resale band' are inverted: Kwick sits above ADSL hardware-only single digits and DSSL 12-18%. Mechanism verdict stands; range verdict does not", anchor: "Prospectus p.257, p.24; ADSL Feb-2026 [page 13]; DSSL Jun-2026 [page 8], [page 11]"}
  - {severity: "MINOR", location: "B05 2A row 5, promise_delivery row 6", finding: "Caveat that repayment came from cash held is not supported: FY26 cash rose 1,206.79 to 1,316.32 lakh; CFO 762.30 covered investing 273.17 and financing 379.60. Verdict DELIVERED stands", anchor: "Prospectus p.268; Deck p.20"}
  - {severity: "MINOR", location: "B05 LBF-2", finding: "FY24 83 days is testable: opening receivables 180.79 lakh from p.93; average basis gives 83.1, so 3 of 3 years reproduce", anchor: "Prospectus p.93, p.91"}
  - {severity: "MINOR", location: "B05 2A row 2a", finding: "Domestic sourcing scored DELIVERED in form only; channel-partner awards and foreign-OEM range suggest imported goods bought from Indian entities [INFERENCE]; separator Top Supplier 1 identity", anchor: "Prospectus p.146-149, p.153, p.161"}
  - {severity: "MINOR", location: "B05 overall", finding: "Six minor items missed (R16 to R20, R23): KMP pay, Jan-2026 plan attribution, pre-listing share transfers, RF15 heading, deck tenure and partnership claims, mid-FY25 dealer-shift date", anchor: "Prospectus p.266-267, p.265, p.34, p.33, p.27, p.140; Deck p.5-6"}
  - {severity: "MINOR", location: "B06 Part 1 Q4 and Part 4 vs flags", finding: "Peer Q4 range stated as 26-34% in text and 26-33% in the flag", anchor: "B06 report"}
  - {severity: "MINOR", location: "B05 FLAG-CHANNEL-OMISSION", finding: "'Explained only in business strategy p.150' is imprecise; p.140 also describes the channel and dates it from mid-FY25", anchor: "Prospectus p.140"}
critical_count: 0
major_count: 5
minor_count: 6
material_found: 15
material_caught: 10
acceptance_rate: 66.7
coverage_basis: "15 material of 29 listed (0 CRITICAL, 15 MAJOR); 10 fully caught, 4 partially caught, 1 missed. Rate counts full catches only (14/15 = 93.3% if partials counted). Sources: 5 BSE filings and 22-page deck in full; prospectus MD&A p.256-270, objects p.86-100, risk factors p.22-36, business p.135-140 and p.145-164 in full, plus targeted reads (p.33-34, p.87, p.106-108, p.124, p.196, p.212-214, p.250); risk factors p.36-50 not read. Peers: DSSL Q4 FY26 and Q1 FY27 in full; 9 others by targeted search with context."
```
