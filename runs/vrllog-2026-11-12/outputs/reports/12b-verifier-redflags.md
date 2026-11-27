# STAGE 12, VERIFIER B: CONCALL RED FLAGS. VRL Logistics Ltd (VRLLOG). Run 2026-11-12

Model: claude-opus-5-5. Fresh context. Inputs: 16 transcripts (4 VRL, 12 peer) and the B05 and B06 reports. Rubric: prompts/12-verifiers-pipeline.md, Verifier B section.

## Method and limits

- I read all four VRL transcripts end to end before I opened B05 or B06: Q3 FY26 (6 Feb 2026), Q4 FY26 (19 May 2026), Q1 FY27 (5 Aug 2026) and Q2 FY27 (5 Nov 2026).
- Peers, read before B05 and B06: TCIEXP all four calls end to end. TCI all four calls by keyword windows (LTL, freight, pricing, diesel, wage, competition, DFC), with the hit passages read in full. Delhivery Q3 FY26 and Q4 FY26 by keyword windows in the .txt. Delhivery Q1 FY27 and Q2 FY27 .txt files hold one word per line, so I read the PDF pages directly (Q1 FY27 PDF p.3, 4, 7, 9 to 12; Q2 FY27 PDF p.3, 23, 26, 28, 29). Other Delhivery pages were not read. A topic absent from those pages is "not found in pages read", not "absent".
- Anchor key: VRL and text-file peers use the `[page N]` marker of the .txt file. Delhivery Q1 FY27 and Q2 FY27 use the PDF page. The speaker is Sunil Nalavadi (CFO) on every VRL call unless named.
- This verifier owns judgment on red flags. It does not rule on whether a number exists at an anchor. Verifier A owns that question.
- DERIVED marks my own arithmetic. [INFERENCE] marks a reading that goes beyond the transcript words.

---

## SECTION 1. INDEPENDENT RED-FLAG LIST (graded before comparison)

Severity scale: CRITICAL (fabricated or materially wrong, would change a decision), MAJOR (thesis-relevant, decision likely survives), MINOR (imprecision, tone, cosmetic). No item reached CRITICAL. I tested the strongest candidate, R2 (fleet), against the "repeated evasion" bar. It fails that bar because the CFO answered the substance in both quarters (capacity is fully used; capacity will be added). What is missing is the status of a named programme that no analyst asked about by name. That is an omission, not a dodge.

### MAJOR (9)

**R1. FY27 volume guidance cut without acknowledgement, then misquoted. MAJOR.**
- Feb: "almost around 10% growth in tonnage in the next financial year" (Q3 FY26, CFO, [page 5]). Also "10% to 11%" and "11% revenue growth... INR3,600 crores... EBITDA... INR730 crores, INR740 crores" ([page 7]). He called it "a very conservative number" ([page 10]). Closing: "we remain confident on delivering around 10% volume growth" ([page 15]).
- May: "at least around 6% to 7% for the full year" (Q4 FY26, CFO, [page 6]). The CFO gives no reason for the cut and never mentions the 10-11%. Oil-linked commodity demand is cited generally ([page 6]-[page 7]). Alok Deora then says "7%, 8%" and the CFO does not correct him ([page 14]).
- Aug: "In last call, actually, I guided around 6% to 7%... we are expecting around 8%" (Q1 FY27, CFO, [page 10]).
- Nov: "initially, for the current financial year also, we expected our tonnage growth at around 8% at the beginning of the year" (Q2 FY27, CFO, [page 6]). This matches neither May (6-7%) nor Feb (10-11%).
- Why it matters: the outcome is fine (H1 about 10%). The guidance path is not: 10-11%, then 6-7%, then 8%, then 9-10%. The first cut was silent and the history was later restated. This bears on how far any forward basis can rest on management guidance.

**R2. Own-fleet model erodes while the fleet plan goes unreported. MAJOR.**
- Feb claim: "96%, 97% of the service we are providing through own vehicles and the further demand will also be through own vehicles, then definitely it will maintain our profitability margin of around 20%" (Q3 FY26, CFO, [page 11]). The 500-vehicle order equals a 10% capacity add to match 10% volume ([page 6]). 100 were delivered in January ([page 3]-[page 4]). The 20-tonne truck is preferred over the 28-tonne truck as "more efficient" ([page 14]).
- May: lorry hire up 1.73% of revenue ([page 4]). Fleet down from "6,100-plus" to "around 5,900" ([page 10]). "No, scrappage will not be there, but there will be addition of vehicles... the remaining 400 vehicles are going to be added till December" ([page 10]).
- Aug: "most of the vehicles have been scrapped in the last year as well as in this quarter... we felt some shortage in capacity... we engage outside vehicles. So, there is an increase in lorry service also" (Q1 FY27, CFO, [page 9]). This directly contradicts the May statement that there would be no scrappage. Q1 vehicle capex was Rs 18 Cr ([page 5]). Jainam Shah notes "now we are doing limited truck acquisition". The answer gives no number and no programme status ([page 11]).
- Nov: fleet 5,941 ([page 5]). Krupa Shankar notes more vehicles scrapped than added and asks when procurement starts. The answer: "further expansion in the fleet, basically on higher capacity vehicles going forward. The numbers will be less" ([page 10]-[page 11]). This reverses the Feb preference for 20-tonne trucks. The 500-vehicle programme is not mentioned in either answer.
- Debt-free share of fleet: 80% (Feb [page 5]), 77% (May [page 5]), 79% (Aug [page 5]), 76% (Nov [page 5]). Fully depreciated share: 15%, 14%, 13%, 11%.
- Nov closing presents own vehicles as the edge over peers who "are completely depending on the outside vehicle or hired vehicles" ([page 15]). [INFERENCE] VRL's own hired share rose over the same period. The claimed moat is weaker than the closing implies, and B05 trigger T6 rests on it.

**R3. Bulk-fuel cost advantage reversed: the Feb margin bridge no longer holds. MAJOR.**
- Feb: fuel cost 24.8% of income against 26.4%, with about 40% of fuel bought in bulk from refineries. Captive pumps went from 7 to 8 (Q3 FY26, CFO, [page 4]). Lower fuel cost "has compensated with increase in the employee cost", worth "1.6% to 1.7%" ([page 8]). Plan: "another at least around 3 to 4 pumps in the next financial year" ([page 13]).
- May: refinery share 41% to 36% ([page 4]); "The bulk purchase is already lost" ([page 7]). Aug: "our bulk purchase has been completely stopped" ([page 6]); cost per litre Rs 83 to Rs 94 ([page 4]). Nov: bulk Rs 120-125 against pump Rs 98-100 ([page 12]).
- Why it matters: the cost offset behind Feb's "20% new normal" is gone. The margin is now held by price, which ties it to R4. The pump plan is not mentioned again.

**R4. The realisation jump is fuel-linked and reversible, and management dates the hikes three different ways. MAJOR.**
- May 19: "we have not increased the rate, but some of the selective routes" (Q4 FY26, CFO, [page 6]). Hidden levers in the same call: chargeable weight raised from 8 kg to 9 kg per cubic foot on some routes, loading and freight-on-value line items, and a fuel surcharge clause for account customers ([page 14]).
- Aug: the hike in the quarter was "around 5%". It came when bulk stopped "April end or beginning of the May", then again after the government raised fuel prices ([page 6]). "This is mainly on account of increase in the fuel rate" ([page 10]).
- Nov: "We did an increase at the beginning of the year from April 1st around 5% and in mid of May, we increased around 4%. There is a 9% increase in the freight rates" ([page 9]).
- Peers on timing: the pump hike came in mid-May, after it was held for the elections (TCIEXP Q1 FY27, Mukti Lal, [page 6]). Delhivery: "by about the end April to mid-May is when the discussions with customers on the contractual revisions had begun" (Delhivery Q1 FY27, Sahil Barua, PDF p.7). Peers on size: diesel up 6-7% means "about 1% to 2%, 3% max" on rates (TCI Q1 FY27, Vineet Agarwal, [page 10]). TCIEXP got "net-net... around 1.5%" (TCIEXP Q2 FY27, Mukti Lal, [page 8]). At Delhivery PTL, only 6 of 37 paisa of the yield gain came from fuel (Q1 FY27, PDF p.7).
- Why it matters: VRL's 9% realisation gain is the margin engine. Its own account of when and why the hikes happened changes from call to call. The April 1 date conflicts with VRL's own May call and with two peers.

**R5. Capex guidance reset three times, with a property tilt at a 10-12 year payback. MAJOR.**
- FY27 capex as stated: Rs 350 Cr (Feb [page 8]). Rs 300 Cr, then "INR300 crores to INR350 crores" (May [page 7]). Rs 220-240 Cr (Aug [page 7]). H1 Rs 158 Cr (Nov [page 5]) plus H2 "INR150 crores, INR160 crores" (Nov [page 7]) = Rs 308-318 Cr (DERIVED). Nov also says "we wish to continue with the capex, what we projected" ([page 12]).
- Inconsistent within the Aug call: property Rs 150-160 Cr plus vehicles about Rs 100 Cr ([page 7]), against vehicles Rs 120-140 Cr with the rest on property and Rs 200-240 Cr a year ([page 11]). Nov long-run figure: "at least around INR250 crores-INR300 crores every year" ([page 7]).
- Property mix: FY26 land and building Rs 165 Cr against vehicles Rs 101 Cr (May [page 5]). Feb said property capex is "only investment in the branches... other than the hubs" ([page 15]). Aug said "mainly the sorting centers" ([page 8]). Nov: Bangalore payback "10-12 years"; smaller buys "on a need basis... some variance will be there" ([page 10]).

**R6. Wage-increment commitment reversed while peers report industry-wide labour inflation. MAJOR.**
- Feb: "till March '27, I don't think so there will be further incremental process". The Labour Code brings no extra liability (Q3 FY26, CFO, [page 13]).
- Aug: Karnataka minimum wage "the impact will not be much" (Q1 FY27, CFO, [page 9]).
- Nov: "we are examining again to consider the increment process. But shortly we will inform about it. As of today, there is no specific timeline" (Q2 FY27, CFO, [page 11]). Employee cost was 16.48% of income against 18% ([page 4]). The 21-22% margin guide on the same call names no wage step.
- Peers: "chronic labor shortages across the industry" and "changes to the statutory labour codes" (Delhivery Q1 FY27, Sahil Barua, PDF p.3). "There is no contractual pass-through clause for minimum wages" (Vivek Pabari, PDF p.10). Delhivery is "still waiting to see what happens exactly in Karnataka" (PDF p.11). "Labor cost is unproportionately increased for every logistic player" (TCIEXP Q4 FY26, Mukti Lal, [page 10]). TCIEXP booked a Rs 60 lakh labour-code gratuity charge (TCIEXP Q3 FY26, [page 13]-[page 14]). "Many states have announced minimum wage increases" (TCI Q4 FY26, Vineet Agarwal, [page 7]).

**R7. Related-party question answered in two words. MAJOR (governance).**
- Tanish Jain asks about the bus business and cargo moving on it: "So that is not arm's length, is it?" The answer: "No, nothing." The CFO adds only that "the promoter and another company is having the bus business" (Q4 FY26, [page 13]). No volume, no value, no basis. The question is not asked again.

**R8. Peers contradict VRL's "express companies are not direct competitors". MAJOR (competitive position).**
- VRL: "the Express cargo companies, they still -- they are not directly competitor to us" (Q4 FY26, CFO, [page 13]).
- TCI: "some of the express guys also moving towards the LTL business with their pricing strategy" (TCI Q3 FY26, Vineet Agarwal, [page 12]). Delhivery: demand is migrating "from what used to be slow PTL to fast PTL", and "there is not a very significant cost difference between Economy PTL and Express PTL" (Delhivery Q2 FY27, Sahil Barua, PDF p.29). Delhivery names "only two very large high-quality PTL players in India, which are Safexpress and Delhivery" (Delhivery Q3 FY26, [page 25]).
- Volume contrast in the same quarters: Delhivery PTL +23% (Q3 FY26, [page 4]), +20% (Q4 FY26, [page 4]), +18% (Q1 FY27, PDF p.3), +14.2% (Q2 FY27, PDF p.3). VRL -9% (Feb [page 3]), +3% (May [page 4]), +9% (Aug [page 4]), +11% (Nov [page 3]).

**R9. About 14-18% of tonnage leaves each year, which management calls structural. MAJOR (franchise quality).**
- Feb YoY: customers who left = 18% of tonnage, new = 15%, existing = -6% (Q3 FY26, CFO, [page 9]). "This loss in customer actually it will continue. On a sequential basis, around 5%, 6%, at least it will be there" ([page 9]).
- May YoY: left 14%, new 17%, existing +1% (Q4 FY26, [page 15]). Aug YoY: left 16-17%, new about 20%, existing +6% (Q1 FY27, [page 8]). The loss rate is still 16-17% after the CFO said rationalisation "completed in the last year" (Q1 FY27, [page 10]).
- Nov claims "there is no pressure of the freight rate on the customers" ([page 6]). [INFERENCE] Volume recovery comes from new-customer intake that outruns a steady 14-18% leakage. The share-of-wallet stickiness that a higher quality-ladder rung needs is not shown.

### MINOR (13)

| # | Item | Anchor |
|---|---|---|
| R10 | Net debt rose from Rs 272 Cr (Dec 2025) to Rs 440 Cr (Mar 2026), +Rs 168 Cr in one quarter (DERIVED). The May call states the number with no explanation and no analyst asks. Feb had said net debt was falling "reflecting healthy cash generation". | Q3 FY26 [page 4]; Q4 FY26 [page 5] |
| R11 | Buyback (Rs 280 Cr at Rs 320, promoters not tendering) chosen over debt paydown. "Free cash flow" of Rs 480-500 Cr is quoted before capex. Nov says H2 cash goes to "reduction in our debt" and does not mention the buyback outflow. | Q1 FY27 [page 7], [page 11]-[page 12]; Q2 FY27 [page 5], [page 7] |
| R12 | Three margin statements in one call: "21%-22%" sustainable, "23% plus margin is sustainable", and "at least around 21% plus". | Q2 FY27 [page 6], [page 13], [page 15] |
| R13 | Medium-term volume given two ways in one Aug answer: 7-8% for 3-4 years, then 6-7% for 3-4 years. Nov says 9-10% is achievable medium term. | Q1 FY27 [page 10], [page 11]; Q2 FY27 [page 8] |
| R14 | Admin expense fell from 2.28% to 1.43% on "lower legal and professional expenses incurred in the last year". That is about 0.85 pt of the 3.67 pt YoY margin gain (DERIVED). The legal cost itself is never explained. | Q2 FY27 [page 4] |
| R15 | No ton-km data: "We do not provide that"; "unable to compute... trying". A lead distance of 270-280 km is given. | Q4 FY26 [page 8], [page 11] |
| R16 | Data-hygiene slips. Q4 customer flows 17 - 14 + 1 = 4 against "around 3%". "6,000 owned vehicles" against "around 5,900" in the same call. States/UTs given as 24/5, 24/4 and 23/5. Q3 property spend given as Rs 50 Cr and as "INR57 crores, INR58 crores". FY27 property given as Rs 160-170 Cr and as Rs 150-160 Cr. "In FY '26... 10% volume growth" (meant FY27). | Q4 FY26 [page 15], [page 3], [page 10]; Q3 FY26 [page 5], [page 4], [page 14], [page 8], [page 15], [page 11]; Q1 FY27 [page 3] |
| R17 | TCI on VRL: "perhaps a little lower pricing that they are offering other than the express companies". VRL May: in corporate accounts "our rates are more or less comparable with these express cargo companies". | TCI Q2 FY27 [page 14]; VRL Q4 FY26 [page 13] |
| R18 | Contradiction inside the Nov call on fuel cuts. "We will take a call and pass it on to the customer... We don't want to wish further make margin out of that". Against: "wherever we do not have much of a competition, we can retain our existing price". Bulk savings carry "no need to pass on that benefit". | Q2 FY27 [page 12], [page 15] |
| R19 | Rail threat to the core lane, volunteered and played down. Railways have set up a Surat facility and "want to supply all this textile material... It has to be through rail". Textiles are 16-18% of VRL tonnage. In May, DFC was "not directly linked" to VRL cargo. | Q1 FY27 [page 12]; Q3 FY26 [page 10]; Q4 FY26 [page 12], [page 15] |
| R20 | Unverified boasts: competitor claim ratio "10%-12%" against VRL's "hardly in decimal"; branch breakeven down to "five to six months". | Q2 FY27 [page 14]; Q1 FY27 [page 10] |
| R21 | October tonnage "+20%" is credited to festival demand. Base comparability is not addressed. | Q2 FY27 [page 14], [page 15] |
| R22 | Volunteered demand negatives: petrochemical and plastic goods demand "coming down" (May); a lower monsoon "may little bit impact" (Aug). | Q4 FY26 [page 6]-[page 7]; Q1 FY27 [page 16] |

Total listed: 22. Material (CRITICAL + MAJOR): 9.

---

## SECTION 2. COMPARISON AGAINST THE PIPELINE

| # | Sev | Status | Where the pipeline has it | Gap |
|---|---|---|---|---|
| R1 | MAJOR | CAUGHT | B05 LB2 trail table; 2A row 3 "classified silence"; FLAG-GUIDANCE-TRAIL; red flag on the misquote | none material |
| R2 | MAJOR | PARTIALLY CAUGHT | B05 2A row 6 (Partial, open); dropped trigger "500-vehicle order count"; slippage "net plus 9"; 2E fleet row "answered eventually, partially"; trigger 7 kill signal on lorry hire | Missing: the May "no scrappage" against Aug "scrapped this quarter" contradiction; the Feb "96-97% own vehicles, further demand through own vehicles" claim against rising lorry hire and "shortage in capacity"; the reversal on vehicle size. B05 accepts management's own reason in 2A row 6. The item is absent from B05 4D. B06 Claim 5 marks own fleet as "UNVERIFIABLE" and never connects VRL's own lorry hire. |
| R3 | MAJOR | CAUGHT | B05 T12 "planned (Feb) now dormant"; 1C "Weakening, then dormant"; dropped trigger; 2D item 5; LB1 "fuel hit was recovered by price" | none material |
| R4 | MAJOR | CAUGHT | B05 LB1, T1, T15, 3C consistency flag (April 5% against the May call), 4D; B06 Claim 2 Part C, FLAG-REALISATION-ATTRIBUTION | magnitude in B06 overstated (see F10) |
| R5 | MAJOR | CAUGHT | B05 LB4 table, 2A row 17, FLAG-CAPEX-RECONCILIATION, property payback red flag | the Feb "branches not hubs" to Aug "sorting centres" shift is not noted (minor) |
| R6 | MAJOR | CAUGHT | B05 2A row 7, 2D item 12, 2E, 4D (Low-Medium); B06 Claim 8, FLAG-WAGE-NO-CUSHION | B05 weight Low-Medium is light; B06 restores it |
| R7 | MAJOR | CAUGHT | B05 LB3, FLAG-RELATED-PARTY, 4D Medium | none |
| R8 | MAJOR | PARTIALLY CAUGHT | B06 2D (TCI Q3 FY26 express into LTL), 2E risk list, Claim 7 (Delhivery list omits VRL), Claim 1 (Delhivery PTL growth) | Not framed against VRL's "not directly competitor" claim (Q4 FY26 [page 13]). The Delhivery Q2 FY27 slow-to-fast PTL migration with no big cost gap is not cited. B06 reads TCI's naming of VRL mainly as share-gain support. |
| R9 | MAJOR | PARTIALLY CAUGHT | B05 LB2 customer flows; 1C "unchanged, never sized" | The Feb statement that 5-6% sequential loss "will continue" is not cited. The flows are framed as recovery and not tested against "no pressure of the freight rate on the customers". |
| R10 | MINOR | MISSED | B05 LB4 starts the net-debt series at March 2026 | the Dec to Mar jump of +Rs 168 Cr is not noted |
| R11 | MINOR | CAUGHT | B05 LB4 funding arithmetic, pro forma, Nov answer omits the buyback | none |
| R12 | MINOR | CAUGHT | B05 LB1, 2C, FLAG-MARGIN-DEFINITION, 4D | none |
| R13 | MINOR | CAUGHT | B05 LB2 table "7-8% for 3-4 years (also stated as 6-7%)" | none |
| R14 | MINOR | CAUGHT | B05 LB1 "a base effect", 0.85 pt quantified | nature of the legal cost not queried |
| R15 | MINOR | CAUGHT | B05 2E, 2D item 9 | overstated as "deflected every time" (see F9) |
| R16 | MINOR | MISSED | not recorded (B05 notes only the H1 tonnage rounding) | cosmetic |
| R17 | MINOR | CAUGHT | B05 3A conflict note; B06 Claim 3 and 2D | none |
| R18 | MINOR | PARTIALLY CAUGHT | B05 2E fuel row ("consistent rule, margin consequence stated more favourably in Nov"); 3C "partly" | the in-call contradiction (pass on fully against retain price where competition is thin) is called a consistent rule |
| R19 | MINOR | PARTIALLY CAUGHT | B05 T11, 2E DFC row; B06 Claim 9, FLAG-DFC-FLEET-OWNERS | not tied to the Surat textile lane, VRL's largest commodity flow |
| R20 | MINOR | CAUGHT | B05 2C over-promotion; 1C breakeven | none |
| R21 | MINOR | CAUGHT | B05 LB2; B06 Claim 1 (October unverifiable) | none |
| R22 | MINOR | CAUGHT | B05 3B, 2A row 3 | none |

Tally: CAUGHT 15, PARTIALLY CAUGHT 5, MISSED 2.

### Pipeline flags not on my independent list

| Pipeline flag | Assessment | Basis |
|---|---|---|
| B05: headline margin includes other income (23.3% on total income; B03 ex other income 22.97%) | SUPPORTED | 226 / 967 = 23.37% (DERIVED). Q2 FY27 [page 3] names Rs 967 Cr as "total income". The Q1 margin of 193 / 885 = 21.8% (DERIVED) uses the same base (Q1 FY27 [page 4]). The 22.97% is a B03 figure outside my inputs and is not verified here. |
| B05: director resignation (7 Oct 2026) and promoter non-tender not addressed on the 5 Nov call | SUPPORTED as silence | The Nov transcript has no mention of either. The resignation date comes from an exchange announcement outside my inputs and is not verified here. Promoter non-tender is stated (Q1 FY27 [page 5]; Q2 FY27 [page 6]). The reason is never asked. |
| B06: FLAG-MARGIN-BASIS (own fleet against hired fleet, so EBITDA is not like for like) | SUPPORTED (labelled INFERENCE by B06) | VRL "96%, 97%" own vehicles (Q3 FY26 [page 11]); TCIEXP "we completely outsource our fleets" (Q3 FY26 [page 16]); TCI "we don't own any fleet" (Q2 FY27 [page 15]) |
| B06: FLAG-DFC-FLEET-OWNERS | SUPPORTED as a quote | TCI Q2 FY27 [page 15]: "the market impact could be substantial for fleet owners on certain routes". Applying it to an LTL fleet owner is inference. VRL says its cargo is not full-truckload (Q4 FY26 [page 15]). |
| B06: FLAG-PRECEDENT-FUEL-MARGIN (TCIEXP 2021-22, about 300 bp) | SUPPORTED as a flag; body text OVERSTATED | TCIEXP Q4 FY26 [page 11]: margin "jumped almost 300 basis points on a single year due to that arbitrage benefit". B06 Claim 4 and Part 4 say it "did not hold" and "later reversed". TCIEXP does not say that. It blames its later margin fall on revenue and on building new services (TCIEXP Q3 FY26 [page 16]). See F11. |

pipeline_flags_not_supported: none. Three are overstated (F9, F10, F11).

---

## SECTION 3. PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| B05 row | Promise in earlier call? | Outcome in later call? | Verdict |
|---|---|---|---|
| 1. Q4 FY26 tonnage +3-4% QoQ | Yes: "at least around 3% to 4% sequential growth... at least around 4%" (Q3 FY26 [page 5]; also [page 7]) | Direction holds, magnitude does not. B05 cites "+5.5%" from "daily tonnage crossed 11,500-plus" (Q4 FY26 [page 4]) against "crossed 10,900-plus" (Q3 FY26 [page 3]). Those are per-day thresholds, and Q4 has 90 days against Q3's 92. On quarterly volume: 11,500 x 90 / (10,900 x 92) - 1 = +3.2% (DERIVED). Total income +3% QoQ with realisation +0.4% QoQ points to about +3% (DERIVED). Q1 FY27 1,019 kt at -1.73% QoQ (Q1 FY27 [page 4], [page 5]) gives Q4 FY26 about 1,037 kt (DERIVED). | CONFIRMED (Delivered at the low end of 3-4%, below "around 4%"); the cited +5.5% is wrong (F8) |
| 6. 500 vehicles by Dec 2026 | Yes: order of 500, 100 delivered in January (Q3 FY26 [page 3]-[page 4]); "till December 2026" ([page 11]) | Yes: 400 more "till December" (Q4 FY26 [page 10]); fleet 5,941 (Q2 FY27 [page 5]); no later update | CONFIRMED (Partial, open) |
| 7. No wage increment before March 2027 | Yes (Q3 FY26 [page 13]) | Yes: "examining again... no specific timeline" (Q2 FY27 [page 11]) | CONFIRMED (Partial, likely reversal) |
| 10. At least 2% sequential tonnage growth each quarter of FY27 | Yes: "at least around 2% quarterly growth on a sequential basis" (Q4 FY26 [page 6]) | Yes: Q1 "-1.73%" (Q1 FY27 [page 5]; B05 cites p.4); Q2 1,079 / 1,019 = +5.9% (DERIVED; Q2 FY27 [page 3]) | CONFIRMED (Missed Q1, met Q2) |
| 17. FY27 capex Rs 220-240 Cr | Yes (Q1 FY27 [page 7]) | Yes: H1 Rs 158 Cr (Q2 FY27 [page 5]) plus H2 Rs 150-160 Cr ([page 7]) = Rs 308-318 Cr (DERIVED) | CONFIRMED (Missed) |

Checked 5, confirmed 5 on direction, wrong 0. One row has a wrong magnitude (row 1). Rescoring row 1 as "Delivered, low end" keeps the B05 tally at 11/4/3. Rescoring it "Partial" gives 10/5/3. Neither moves the grade.

---

## SECTION 4. CREDIBILITY GRADE

B05 grade: B (Good). I concur. Since May 2026, delivery on tonnage, realisation and margin has met or beaten guidance, and the buyback was executed as announced. That earns B under A26.4. The consistency defects keep it from A. These are: the silent Feb-to-May cut, the restated "8% at the beginning of the year", three different dates for the price hikes, the May "no scrappage" against the Aug "scrapped this quarter", the capex reset three times, and the wage-increment reversal. B05's Consistency score of 3 is generous. 2 fits the record better. That change does not move the letter grade.

---

## SECTION 5. FINDINGS (consolidated)

| ID | Sev | Stage | Finding | Evidence |
|---|---|---|---|---|
| F1 | MAJOR | B05, B06 | The own-fleet erosion (R2) is only partly caught. B05 records the 500-vehicle gap but accepts management's own reason. It misses the May "scrappage will not be there" against the Aug "scrapped... in this quarter" walkback. It misses the Feb claim that further demand would run on own vehicles, set against rising lorry hire and a stated capacity shortage. It misses the vehicle-size reversal. The item is not in B05 4D. B06 never links VRL's own lorry hire to the own-fleet claim. Trigger T6 (own fleet as edge) rests on this. | Q3 FY26 [page 11], [page 14]; Q4 FY26 [page 4], [page 10]; Q1 FY27 [page 9], [page 11]; Q2 FY27 [page 10]-[page 11], [page 15] |
| F2 | MINOR | B06 | Competitive contradiction R8 is partly caught. Express-into-LTL appears as a peer risk but is not set against VRL's "not directly competitor" claim. The Delhivery Q2 FY27 slow-to-fast PTL migration (no big cost gap) is not cited. | VRL Q4 FY26 [page 13]; Delhivery Q2 FY27 PDF p.29 |
| F3 | MINOR | B05 | Structural customer leakage R9 is recorded as flows but not weighed. The Feb "will continue, 5-6% sequential" is not cited. | Q3 FY26 [page 9]; Q2 FY27 [page 6] |
| F4 | MINOR | B05 | Missed: net debt Rs 272 Cr to Rs 440 Cr in Q4 FY26, unexplained on the May call. | Q3 FY26 [page 4]; Q4 FY26 [page 5] |
| F5 | MINOR | B05 | Missed: data-hygiene slips across calls (R16). | see R16 anchors |
| F6 | MINOR | B05 | The fuel-cut answer is called a "consistent rule". The Nov call holds both full pass-through and price retention where competition is thin (R18). | Q2 FY27 [page 12], [page 15] |
| F7 | MINOR | B05, B06 | The railway Surat textile facility is not tied to VRL's largest commodity lane (R19). | Q1 FY27 [page 12]; Q4 FY26 [page 12] |
| F8 | MINOR | B05 | 2A row 1 outcome "+5.5%" compares two per-day thresholds across quarters of different length. Quarterly tonnage growth is about +3.2% (DERIVED). Delivered at the low end, not above the range. | Q3 FY26 [page 3]; Q4 FY26 [page 4] |
| F9 | MINOR | B05 | The ton-km row "deflected every time (two answers, no figure)" is overstated. Lead distance was answered with "270 to 280 kilometres" and vehicle capacity "15 to 18 tons". Only ton-km was withheld. | Q4 FY26 [page 11] |
| F10 | MINOR | B06 | The realisation attribution is overstated in size. "About half not fuel" uses the Rs 8-9 pump rise. VRL's own cost per litre rose Rs 11-12 (Q1 FY27 [page 4]: Rs 83 to 94; Q2 FY27 [page 4]: Rs 85 to 97). On VRL's own rule of Rs 2 = 1%, that explains about 5.5-6% (DERIVED). The non-fuel part is closer to a third. The "contradicted" label rests on Delhivery's account of its own PTL yield, which cannot contradict VRL's account of VRL's yield. The stronger evidence is TCI's 1-3% (TCI Q1 FY27 [page 10]) and the peer timing of the mid-May hike (TCIEXP Q1 FY27 [page 6]; Delhivery Q1 FY27 PDF p.7). The direction of the flag holds. | as cited |
| F11 | MINOR | B06 | The TCIEXP 2021-22 precedent is described as a margin jump that "did not hold" and "later reversed". TCIEXP does not say this. It attributes its later margin decline to revenue and to investment in new services. | TCIEXP Q4 FY26 [page 11]; TCIEXP Q3 FY26 [page 16] |
| F12 | MINOR | B05 | Anchor and attribution slips. The anchor key promises `[page N]` markers, but several anchors use printed page numbers: Q1 sequential -1.73% is at Q1 FY27 [page 5] (B05 p.4); chargeable weight is at Q4 FY26 [page 14] (B05 p.13); the Bangalore payback is at Q2 FY27 [page 10] (B05 p.9); the Q4 customer flows are at Q4 FY26 [page 15] (B05 p.14). "New normal '20%, 21%'" is Alok Deora's phrase. The CFO replied "around 20%, you can say" (Q3 FY26 [page 8]). Verifier A owns the anchors; this is noted for coherence only. | as cited |

Counts: CRITICAL 0, MAJOR 1, MINOR 11.

---

## SECTION 6. SCORING

- Independent items listed: 22 (CRITICAL 0, MAJOR 9, MINOR 13).
- Material found (CRITICAL + MAJOR): 9. Fully caught: 6 (R1, R3, R4, R5, R6, R7). Partly caught: 3 (R2, R8, R9), scored as not caught. Missed: 0.
- acceptance_rate = 6 / 9 = 66.7%, rounded to 67. The denominator is 9, at least 4, so the rate applies. If partial catches counted, the rate would be 9 / 9 = 100%. Neither reading falls below the 60% REWORK line.
- No missed item is a repeated evasion. No CRITICAL fires.

---

```yaml
stage: B12b
company: "VRLLOG"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 22
caught: 15
partially_caught: 5
missed:
  - {severity: "MINOR", item: "Net debt rose Rs 272 Cr (Dec 2025) to Rs 440 Cr (Mar 2026), +Rs 168 Cr in one quarter, stated without explanation on the May call; B05 net-debt series starts at March", anchor: "Q3 FY26 call [page 4]; Q4 FY26 call [page 5]"}
  - {severity: "MINOR", item: "Data-hygiene slips: Q4 customer flows 17-14+1=4 vs 'around 3%'; '6,000 owned vehicles' vs 'around 5,900' in one call; states/UTs 24/5, 24/4, 23/5; Q3 property Rs 50 Cr vs Rs 57-58 Cr; FY27 property Rs 160-170 Cr vs Rs 150-160 Cr", anchor: "Q4 FY26 [page 15], [page 3], [page 10]; Q3 FY26 [page 4], [page 14], [page 8], [page 15]; Q1 FY27 [page 3]"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur: B holds on delivery since May 2026 (tonnage, realisation, margin met or beaten; buyback executed); the silent Feb-to-May guide cut, three dates for the price hikes, May-to-Aug scrappage reversal and capex reset three times keep it from A; B05 Consistency 3 should read 2, letter unchanged"
findings:
  - {id: F1, severity: "MAJOR", stage: "B05, B06", issue: "Own-fleet erosion only partly caught: May 'scrappage will not be there' vs Aug 'scrapped... in this quarter' walkback, Feb claim that further demand runs on own vehicles vs rising lorry hire and stated capacity shortage, and vehicle-size reversal all missed; not in B05 4D; B06 never links VRL lorry hire to the own-fleet edge that trigger T6 rests on", anchor: "Q3 FY26 [page 11], [page 14]; Q4 FY26 [page 4], [page 10]; Q1 FY27 [page 9], [page 11]; Q2 FY27 [page 10]-[page 11], [page 15]"}
  - {id: F2, severity: "MINOR", stage: "B06", issue: "Express and fast-PTL encroachment listed as a peer risk but not set against VRL's 'not directly competitor' claim; Delhivery slow-to-fast PTL migration with no big cost gap not cited", anchor: "VRL Q4 FY26 [page 13]; DELHIVERY Q2 FY27 PDF p.29; TCI Q3 FY26 [page 12]"}
  - {id: F3, severity: "MINOR", stage: "B05", issue: "Customer leakage of 14-18% of tonnage a year recorded as flows but not weighed; Feb 'will continue, 5-6% sequential' not cited against Nov 'no pressure of the freight rate on the customers'", anchor: "Q3 FY26 [page 9]; Q4 FY26 [page 15]; Q1 FY27 [page 8]; Q2 FY27 [page 6]"}
  - {id: F4, severity: "MINOR", stage: "B05", issue: "Missed Q4 FY26 net debt jump Rs 272 Cr to Rs 440 Cr, unexplained", anchor: "Q3 FY26 [page 4]; Q4 FY26 [page 5]"}
  - {id: F5, severity: "MINOR", stage: "B05", issue: "Missed cross-call data-hygiene slips (see missed list)", anchor: "see missed list"}
  - {id: F6, severity: "MINOR", stage: "B05", issue: "Fuel-cut answer called a consistent rule though the Nov call holds both full pass-through and price retention where competition is thin, and keeps bulk savings", anchor: "Q2 FY27 [page 12], [page 15]"}
  - {id: F7, severity: "MINOR", stage: "B05, B06", issue: "Railway Surat textile facility not tied to VRL's largest commodity lane (textiles 16-18% of tonnage)", anchor: "Q1 FY27 [page 12]; Q3 FY26 [page 10]; Q4 FY26 [page 12]"}
  - {id: F8, severity: "MINOR", stage: "B05", issue: "2A row 1 outcome '+5.5%' compares per-day thresholds across quarters of 92 and 90 days; quarterly tonnage about +3.2% (DERIVED); Delivered at the low end of 3-4%, below 'around 4%'", anchor: "Q3 FY26 [page 3], [page 5]; Q4 FY26 [page 4]"}
  - {id: F9, severity: "MINOR", stage: "B05", issue: "Ton-km row 'deflected every time, no figure' overstated: lead distance answered 270-280 km and capacity 15-18 tonnes; only ton-km withheld", anchor: "Q4 FY26 [page 11]"}
  - {id: F10, severity: "MINOR", stage: "B06", issue: "Realisation attribution overstated in size: VRL cost per litre rose Rs 11-12, so on its own Rs 2 = 1% rule fuel explains about 5.5-6% of the 9% (DERIVED), non-fuel about a third not half; 'contradicted' rests on Delhivery's own-book attribution; TCI 1-3% and mid-May peer timing are the stronger evidence; direction holds", anchor: "Q1 FY27 [page 4]; Q2 FY27 [page 4]; TCI Q1 FY27 [page 10]; TCIEXP Q1 FY27 [page 6]; DELHIVERY Q1 FY27 PDF p.7"}
  - {id: F11, severity: "MINOR", stage: "B06", issue: "TCIEXP 2021-22 300 bp precedent described as a jump that 'did not hold' and 'later reversed'; TCIEXP does not say so and blames its later margin fall on revenue and new-service investment", anchor: "TCIEXP Q4 FY26 [page 11]; TCIEXP Q3 FY26 [page 16]"}
  - {id: F12, severity: "MINOR", stage: "B05", issue: "Anchor key promises [page N] markers but several anchors use printed page numbers (Q1 FY27 -1.73% at [page 5] not p.4; chargeable weight Q4 FY26 [page 14] not p.13; Bangalore payback Q2 FY27 [page 10] not p.9; Q4 customer flows Q4 FY26 [page 15] not p.14); 'new normal 20%, 21%' is the analyst's phrase, CFO said 'around 20%'", anchor: "Q3 FY26 [page 8]; as listed"}
critical_count: 0
major_count: 1
minor_count: 11
material_found: 9
material_caught: 6
acceptance_rate: 67
coverage_basis: "9 material (0 CRITICAL, 9 MAJOR) of 22 listed; 6 fully caught, 3 partially caught (R2 fleet, R8 express competition, R9 customer leakage) scored as not caught, 0 missed; 6/9 = 67% (9/9 if partials count; neither reading crosses the 60% REWORK line)"
```
