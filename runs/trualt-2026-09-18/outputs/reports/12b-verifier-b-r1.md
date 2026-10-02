# Stage 12 Verifier B: Concall Red Flags. TRUALT, run 2026-09-18

Model: claude-opus-5. Fresh read of 16 transcripts: 4 main-company (Nov-2025 Q2FY26, Feb-2026 Q3FY26, May-2026 Q4FY26, Aug-2026 Q1FY27) and 12 peer transcripts (GULPOLY, BALRAMCHIN, TRIVENI). The instruction file expects 3 main-company transcripts. This run has 4, and all 4 were read. Page anchors use the PDF page number, shown as "[page N]" in each .txt file. "L" = line in the .txt, given so each quote can be found fast. I read B05 and B06 only after the independent list was complete.

Speakers: MD = Vijaykumar Murugesh Nirani; CFO = Anand Kishore.

## PART 1: INDEPENDENT RED-FLAG LIST (from the raw transcripts alone)

Severity scale: CRITICAL / MAJOR / MINOR. Status vs pipeline (B05 + B06): CAUGHT / PARTIALLY CAUGHT / MISSED.

### Material items (CRITICAL + MAJOR)

| # | Sev | Item | Anchor(s) | Pipeline status |
|---|---|---|---|---|
| 1 | CRITICAL | Repeated evasion over 2 quarters. The same analyst (Nitin Awasthi, InCred) asked for the feedstock split of volumes (grain vs sugar) twice. Management deferred both times: "allow me to have that sent to you over mail... I don't have that figure in hand" (Nov) and "We'll share it with you offline... I don't have right now" (May). A different analyst got the split in Aug (sugar 4.37 cr L, grain 3.92 cr L). The data point was given later, which reduces the harm. The 2-quarter deferral still meets the rule-5 definition. | Nov p15 L599-603; May p25 L962-966; resolved Aug p8 L284-287 | MISSED (B05 2E lists only the 15 cr L and retail questions) |
| 2 | MAJOR | Allocation figures contradict between calls. Nov: "34 crores liters from the government OMCs, about 4 crores... 1.8 crores... 8 crores ENA... total to 47"; "47 is a done deal". May: the PSU award was 26 cr L against a 72 cr L bid, and "in November they came around and decreased the allocation". The cut was known by Nov. Feb still said "fully stabilised platform... 5.5-6 crore litres per month" and kept the 36-37 cr L target. When pressed in May ("as an investor, it was not informed to us"), the MD answered "Even now, the mechanism hasn't changed". That answer is a dodge. | Nov p10 L403-404, p15 L595-598; Feb p4 L124-127, p11 L423-427; May p3-4 L129-138, p10-11 L396-407, p26 L1023 | PARTIALLY CAUGHT. B05 flags the 34% hit rate as disclosed only after the miss. It never notes that the Nov call stated 34 cr L of PSU allocation as a "done deal", or the May dodge. |
| 3 | MAJOR | Management told analysts different things about private-OMC pricing. Feb: private OMCs "usually... give a little higher than the government pricing... this year also... they have given us better realization." May: "INR60 point change was the price that we have offered to them"; analyst: "substantially discounted price to start with". Aug: "about INR60.50". PSU prices are Rs 64-71 for the relevant feedstocks. | Feb p21 L832-835; May p4 L140-142, p25-26 L984-999; Aug p22 L841; PSU prices May p28 L1079-1082 | MISSED |
| 4 | MAJOR | The stated cause of the shutdown changes, and the 15 cr L claim depends on it. Nov: "we had an intentional shutdown wherein about 14 odd crores litres... is pending"; "we have intentionally shut down three out of the four operating plants". Feb (court claim): "the reasons of delay were beyond our control and this falls under the force majeure condition... extreme rainfall". May and Aug go back to a planned shutdown for integration. The Rs 1,062-1,075 cr court claim rests on force majeure, but management's own investor calls call the shutdown intentional. | Nov p10 L396-398, p24 L946-947; Feb p11 L438-444; May p4-5 L150-159; Aug p23 L895-896 | MISSED |
| 5 | MAJOR | The SAF timeline slipped by about 1 year, and the FID condition was reversed. Nov: "revenue should start by FY 2028". Feb: complete "July to October of 2027... FY '28 we should start seeing revenues". May: "24 to 30 months is the target we hold to commission the plant. That's FY29." May: "As soon as we achieve a long-term offtake agreement along with the price, we make our final investment decision". Aug: capex will "begin as early as... the next two or three months", revenue "by end of 2028, that's in FY29". Aug also shows no offtake signed: "still in the working groups". | Nov p19 L762-764; Feb p9 L343-348; May p7 L258-259, p29 L1116-1122; Aug p7 L260-264, p9 L342-349 | MISSED. B05 states the opposite: "Aug-Oct 2027, revenue FY28 ... repeated Q4 FY26 and Q1 FY27 calls, unchanged"; 1C calls SAF "Strengthening"; the B05 kill signal ("FID delay beyond the FY28 revenue date") has already fired. |
| 6 | MAJOR | Margin quality. Headline Q1FY27 EBITDA was 23.5%. The CFO's breakdown: DDGS Rs 47.34 cr + CO2 Rs 1.89 cr + other Rs 8.73 cr + PLI/interest subvention "around INR22 crores". Core ethanol margin: "It should be about 9% to 9.5%". The Q1 margin came from maize stock bought at Rs 17-22/kg. "At INR25.50... It comes down to almost INR6 to INR7 a litre." That is a negative the CFO gave under questioning. | Aug p5 L175, p8 L294-301, p18 L692-704 | PARTIALLY CAUGHT. B05 scores Q1 EBITDA "Delivered/beat" and calls margin "Strengthening, delivered". The Rs 6-7/L figure appears only as a peer question. The 9-9.5% core margin is absent. |
| 7 | MAJOR | CBG economics attribution. The only operating CBG plant sits in Leafiniti Bioenergy (CFO: Leafiniti revenue Rs 42.84 cr, PAT Rs 18.07 cr). GAIL "holds 49% stake in Leafiniti" from March 2026. So the showcase plant is now 51% attributable. In May, the MD calls TGPL "a wholly-owned subsidiary", but the same call says Sumitomo is "a 49% JV partner" of TruAlt Gas. In Aug, the MD agrees "we will only report 51% of the gross revenue". That is wrong for a 51% subsidiary, which consolidates 100% with a minority interest. | May p6 L203-212, p9 L341-351, p20 L786-787; Aug p16 L605-607 | MISSED |
| 8 | MAJOR | Promoter pledge. In Nov, 26% of shares were "re-pledged" to the SBI/IREDA consortium as a sanction term just after listing. In Aug, the analyst asks when the pledge loan is repaid. The CFO gives a confused answer ("this loan is not against the pledged share, that is collateralized"). Release is "hopefully in this quarter". | Nov p17-18 L683-703; Aug p14-15 L555-569 | MISSED (no mention in B05) |
| 9 | MAJOR | Ind AS 8 prior-period restatement. The analyst (Shubh Gala) asked; the disclosure was prompted. Rs 10.5 cr GST Rule 43 reversal "supposed to be in the P&L account in the March quarter", booked to other equity. The MD calls it "an oversight from our the tax consultants" and says "We could have increased our PAT margin by INR4 crores... instead of INR89 crores... INR93 crores". A GST reversal is a cost, not a lost gain. The Rs 89 cr base matches neither FY26 PAT given in May (standalone Rs 80.26 cr, consolidated Rs 96.86 cr). | Aug p20 L761-775; May p9 L326-327, L370-372 | PARTIALLY CAUGHT (misclassified). B05 calls it an "unprompted" admission and the "clearest instance of unprompted accountability". It uses the item to keep the grade at C instead of D. It is a prompted, incoherent explanation of a prior-period error. |
| 10 | MAJOR | Related-party sourcing statements disagree, and the pipeline did not test them against the AR. May: group sourcing "less than 55%" and falling. Group-company payables "may go to two, three months". Aug: "access to our group company that can assure us 100% of the required raw material at a stable price". Spent wash and press mud for the Sumitomo JV come from TruAlt and the group sugar company. Bagasse for power also comes from a group company (Nov). B05 cites the AR's RPT purchases at 72.6% of FY26 purchases, and the May "<55%" figure needs to be checked against that. | Nov p16 L642-649; May p18-19 L708-729, p20-21 L785-797; Aug p24 L935-937 | MISSED. B05 says the reverse: "zero mention... of related-party feedstock concentration" and "none of these topics were asked by any analyst". Vinit Thakur asked in May. |
| 11 | MAJOR | The FY27 "44 cr L orders on hand" is in fact an assumption. In the same call the MD says "we have 44 crores litres of orders on hand" and "we are taking the base case. Whatever we got last year to be a base case". In May the book was 26 + 8 + 6 = 40. No reason is given for the 4 cr L rise. The MD also says the 44 excludes the 15 cr L. A peer (TRIVENI, Aug) says the Supreme Court status quo "has prevented the tender for allocation". | Aug p8 L306-309, p9 L335, L352-355; May p20 L757-759; TRIVENI Aug p6 L307-312 | MISSED and misreported. B05 3D says the 44 is "26 public OMC + 8 private OMC + 6 ENA + 15 court-ordered, netted against non-delivery of the 15 cr L tranche". The transcripts do not support that make-up. |
| 12 | MAJOR | Unsold inventory built up. At Dec there were 5.2 cr L of ethanol stock plus sales in transit. In May, "INR460 close to INR500 crores of inventory"; "the inventory we're unable to sell". In Aug, grain stocks were bought at Rs 18,000-21,000/t and carry a holding cost. The MD says Q1 margin rested on this stock. | Feb p18 L705-717; May p11 L408-410, p27 L1043-1053; Aug p18 L701-708 | PARTIALLY CAUGHT. B05 3C calls the inventory answer "coherent". It is not linked to the cash-conversion flag or listed as a red flag. |
| 13 | MAJOR | The 15 cr L court order slipped over 4 calls: Nov "work in progress", Feb "fight has just begun", May "by September / H1", Aug "not able to give a timeline". Aug also says "anytime now". TRIVENI reports a Supreme Court status quo on allocations. | Nov p10 L396-404; Feb p11-12 L445-457; May p11-12 L419-446; Aug p9 L335-338, p21 L799-801 | CAUGHT (B05 flag + repeated_evasions; B06 2E) |
| 14 | MAJOR | Retail stall: Nov "13 shortly", Feb "75 by calendar year", May "11 in three months, 76 taken slow", Aug still 7 open with "4 by end of quarter". | Nov p5 L128-131; Feb p5 L166-169; May p7 L263-268; Aug p4 L140-148 | CAUGHT |
| 15 | MAJOR | CBG commissioning slips on both JVs. Sumitomo: Nov "end of Q2 FY27"/"July 2026", Feb "June 2026", May "3 of 4, Q3/Q4 FY27", Aug "near commissioning, revenue Q4". GAIL: Feb "5 plants, Jan-Feb '27", May "6 plants, Q4 FY27", Aug "construction... August onwards, revenues Q1 next FY". | Nov p3 L103-104, p19 L752-754; Feb p18-19 L727-756; May p6 L205-219, p12 L469-485; Aug p3-4 L106-123 | CAUGHT (B05, GAIL leg partially) |
| 16 | MAJOR | FY26 volume missed: 36-37 cr L guided, 24 cr L delivered. | Feb p11 L423-427; May p10 L388-395 | CAUGHT |
| 17 | MAJOR | TruAlt's demand-supply view reversed between calls. Nov: "supply of close to... 1,800... demand of close to 1250... already an oversupply". Aug: "almost at par" with "no further capacity additions". Peers describe structural overcapacity. | Nov p22 L873-876; Aug p24 L918-932; TRIVENI Aug p10 L544-572 | CAUGHT (B06 Q4; the self-contradiction with Nov is not noted) |
| 18 | MAJOR | Peer: the Supreme Court status quo blocks all new allocations (BPCL challenge to the Karnataka HC ruling; AG proposal of 100 cr L). This conflicts with TruAlt's Aug confidence that the 15 cr L comes "anytime now". | TRIVENI Aug p6 L307-318; Aug p9 L335-338 | CAUGHT (B06 2E) |

### Minor items

| # | Item | Anchor(s) | Status |
|---|---|---|---|
| 19 | Refusal to give revenue or CBG outlook on every call ("not supposed to give", "company secretary... nudging me", "We cannot tell you the figure of FY2027"). Volume and price are then given with "do the math". This looks like a consistent policy, not a hidden fact. | Nov p19 L747-751; Feb p18 L720-723; May p19 L750; Aug p20 L783-785 | MISSED |
| 20 | FY26 volume totals do not reconcile: MD says 24 cr L, CFO says "26 crore litres" with Q4 about 6 cr L. The quarter sum is about 3.0-3.3 + 2.4 + 7.6/7.8 + 6, roughly 19-20 cr L. Q1FY27 is also given as 8.5 and 8.29 cr L. | May p10 L388-390, p25 L960-961; Nov p24 L936-944; Feb p8 L321, p14 L635; Aug p3 L85, p23 L890-891 | PARTIALLY CAUGHT (B05 LOW self-corrections) |
| 21 | Q1FY27 guidance missed and Q2 plan reversed. Feb: "80% capacity use for Q1"; "Q2 usually is our downtime. So 2 months is scheduled maintenance". Aug: "only operate at about 60%"; "we don't have plans to stop for maintenance". | Feb p13 L518-521; Aug p3 L91, p23 L889-892 | MISSED (not in the promise table) |
| 22 | Stock-in-trade question deflected ("I should have to ask the investor community"). | Feb p12 L458-464 | CAUGHT |
| 23 | DDGS Q4 guide of Rs 70-80 cr missed at Rs 28 cr. The Feb call had already softened it ("I may have missed out... would not be able to give the exact quantity"). The May figure was first stated as "78 crores", then corrected to 28. | Feb p10 L399-401, p16 L648-654; May p15 L607-609 | CAUGHT |
| 24 | Tone shift from triumphant (Nov "done deal", Feb "fully stabilized platform") to apologetic and hostile in May ("apologies... could not... demonstrate the growth that we had already promised"; "management has not been active"; "hanky-panky"; "oligarchy"). | May p15 L573, p20 L775-779, p25 L981, p29 L1128-1130 | PARTIALLY CAUGHT (B05 external-blame pattern) |
| 25 | Unusual analyst insistence: Deepak Poddar on volume math (Feb, May), Vedant Sarda on run-rate (May), Parth Shah on deleveraging and a share price "not going anywhere from the listing day" (Aug). | Feb p18 L699-718; May p26-27 L1016-1053; Aug p22-23 L853-880 | CAUGHT (B05 3C) |
| 26 | Deleveraging plan promised "in the next call or maybe in the next few days", with no numbers. | Aug p22 L856-857, p23 L878-880 | CAUGHT |
| 27 | Advertising was promised in May and had not started by Aug ("empanelled... media strategist... delays"). | May p23 L894-897; Aug p22 L862-866 | MISSED |
| 28 | Peer contradiction on blending. TruAlt May: "increasing the blending targets from 20% to 21%. The notification is already in"; "already increased by 1%". GULPOLY Aug: "blending beyond 20% may be delayed by 6 months to 1 year". TRIVENI Jun: talk of "slightly more than 20%... cannot certify". A live notification check is needed (PENDING LIVE VERIFICATION). | May p5 L177-178, p22 L858; GULPOLY Aug p7 L267-270; TRIVENI Jun p4 L192-195 | MISSED |
| 29 | CBG margin figures drift: Q2FY26 EBITDA 68.29% / PAT 49.85%, then 9M 63%/43%, then FY ">55%... 45%", then Q1FY27 PAT about 40%. The Q1 dip is first explained as "nothing driving this", then as employees plus one-time R&M. | Nov p6 L220-226; Feb p4 L129-131; May p5 L193-194; Aug p3 L103-105, p6 L227-233 | MISSED |
| 30 | Operating days in Q3FY26: MD says 58, CFO says 48-50. Three reasons are given: mid-Nov crushing start, farmer protests, and "30 days we lost". | Feb p3 L110, p5 L185, p8 L321-325, p11 L425 | MISSED |
| 31 | Nov: "we have already completed the COD, and all these plants have commenced". Feb: Unit 5 got its consent to operate only on 17-Dec-2025. | Nov p7 L263-265; Feb p4 L119-120 | MISSED |
| 32 | CFO calls higher depreciation and finance cost "a one-time fact" while CBG and SAF capex is ongoing. | May p9 L337-340 | MISSED |
| 33 | The SAF "IRR" answer mixes payback and IRR ("3.5 to 4 years... IRR will be close to 19%"). | Nov p21 L838-840 | MISSED |
| 34 | CBG plant sizes and capex drift: "four CBG plants of 20 tons each" vs "four plants of 80 TPD each" (Nov). May gives 162 TPD, but the plant counts add to 142. Aug gives 132 TPD additional. GAIL cost: Rs 60-65 cr per 12 TPD (Feb), then Rs 425 cr for 6 x 10 TPD (Aug). | Nov p12 L473-474, p19 L752-754; Feb p10 L381-386; May p6 L217-220; Aug p7 L254-256, p15 L594-595 | CAUGHT (B05 count inconsistency) |

Totals: 34 items listed. 18 material (1 CRITICAL, 17 MAJOR) and 16 MINOR.

## PART 2: COMPARISON AGAINST PIPELINE FLAGS

### 2A. Pipeline flags I did not raise in the same form

| Pipeline flag | Source | Assessment | Basis |
|---|---|---|---|
| [HIGH] Utilisation on three denominators "describing the same operating period", "never reconciled" | B05 4D, YAML flags | OVERSTATED | The MD gives both the 95%-on-operating-days and the ~60% gross figures in the same Feb opening (Feb p4 L123-124), so they were reconciled. The "<35%" is the Apr-May 2026 sales run-rate (May p5 L172-174), which is a different period. |
| [HIGH] "Zero mention across all four calls of standalone CFO, DSCR, or related-party purchase concentration"; "none of these topics were asked by any analyst" | B05 2D, 4D, YAML | PARTLY NOT SUPPORTED | DSCR is stated: 1.36 (Aug p5 L191) and Leafiniti 4.25 (May p9 L356). Group sourcing and group payables were asked by Vinit Thakur and answered (May p18-19 L708-729). Aug p24 L935-937 also covers it. Only the operating-cash-flow silence holds. |
| SAF date "unchanged", SAF trigger "Strengthening" | B05 1B, 1C | NOT SUPPORTED | Item 5. The date moved from FY28 to FY29 (May p29, Aug p7). |
| GST restatement as "unprompted accountability", "PAT understatement" | B05 2B, 3C, 4C, credibility_basis | NOT SUPPORTED | Item 9. An analyst prompted it, and the explanation does not add up. |
| FY27 order book "44 cr L = 26+8+6+15 netted" | B05 3D | NOT SUPPORTED | Item 11. The 44 excludes the 15 (Aug p9 L335). The make-up is not in any transcript. |
| Q1FY27 EBITDA "Delivered/beat vs 15-22% range guided" | B05 2A | NOT SUPPORTED as a promise row | No Q1FY27 margin promise exists. The real Q1FY27 promise (80% utilisation, Feb p13) was missed. See Part 3. |
| Q3: maize-margin claim "CONTRADICTED", "the single most consequential finding" | B06 Q3, Part 4 | NOT SUPPORTED | B06 restates TruAlt's claim as compression "through FY26". TruAlt made a point-in-time sensitivity: Q1 used stock bought at Rs 17-22/kg, and at today's Rs 25.50 the contribution falls to Rs 6-7/L (Aug p8 L294-301). GULPOLY supports the direction. Q1 was "exceptional" because "raw material prices were very conducive". It sees "temporary pressure on margins... owing to higher grain prices". It can stock only 30-45 days and guides 10-11% consolidated (GULPOLY Aug p4 L124-128, p6 L235-245, p8 L310-321). GULPOLY's Rs 9 per litre is tied to "ease off on the raw material prices" (GULPOLY Feb p10). No peer gives a per-litre figure at Rs 23-25/kg maize. The magnitude cannot be verified; the direction is corroborated. |
| TruAlt "never describe the Supreme Court stay mechanism" | B06 2E | OVERSTATED | May p11 L426-429: "the Supreme Court has directed the OMCs that unless that matter is fully heard and disposed of, not to do any new allocation." TruAlt did not name BPCL or the AG proposal; that part holds. |
| FY26 volume miss; 15 cr L slippage; retail stall; CBG count drift; DDGS miss; self-corrections | B05 | SUPPORTED | Items 13-16, 20, 23, 34 |
| Q1 allocation shortfall sector-wide; Q4 overcapacity framing; Q5 scheme dependency; Q6 FCI price | B06 | SUPPORTED | Peer quotes check out at the cited pages (GULPOLY Feb p10; TRIVENI Aug p6, p10-11) |

### 2B. Scoring summary

- Material items (CRITICAL + MAJOR): 18. CAUGHT 6 (items 13, 14, 15, 16, 17, 18). PARTIALLY CAUGHT 4 (items 2, 6, 9, 12). MISSED 8 (items 1, 3, 4, 5, 7, 8, 10, 11).
- Minor items: 16. CAUGHT 5 (items 22, 23, 25, 26, 34). PARTIALLY CAUGHT 2 (items 20, 24). MISSED 9 (items 19, 21, 27, 28, 29, 30, 31, 32, 33).
- Whole list: CAUGHT 11, PARTIALLY CAUGHT 6, MISSED 17. Total 34.
- acceptance_rate uses the material subset. The pipeline "had" CAUGHT + PARTIALLY CAUGHT = 10 of 18 = 55.6%. On CAUGHT alone the rate is 6 of 18 = 33.3%. Both are below 60%. The denominator is 18, so rule 7 does not apply.

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| Row | Earlier call contains promise? | Later call shows outcome? | Verdict |
|---|---|---|---|
| 80-85% utilisation Q3/Q4 FY26 | Yes, Nov p18 L705-706 | Yes, ~60% gross Q3 (Feb p4 L123) | CONFIRMED |
| 26-28 cr L Q3+Q4 FY26 | Yes, Nov p18 L722-723 | Yes. Q3 was 7.6 (Feb p8 L321). FY is 24 (May p10) or 26 (May p25). Q3+Q4 comes to about 18-20. | CONFIRMED (the size depends on which unreconciled FY total is used; item 20) |
| FY26 36-37 cr L | Yes, Feb p11 L426-427 | Yes, 24 (May p10 L388-390) | CONFIRMED |
| Q4 DDGS Rs 70-80 cr | Yes, Feb p10 L399-401 | Yes, Rs 28 cr (May p23 L904-907) | CONFIRMED. The Feb call softened this in the same call (p16 L648-654). |
| 4 Sumitomo plants by June 2026 | Yes, Feb p18-19 L729-738 | Yes, 3 of 4 (May p12 L473-485) | CONFIRMED |
| SAF VGF Rs 150 cr delivered | Yes, Feb p4 L154-155 | Yes, "successfully achieve" (Aug p4 L128-129) | CONFIRMED |
| Q1FY27 EBITDA "delivered/beat vs 15-22% guided" | No. No Q1FY27 margin promise exists. The 15-16% was an ethanol "trend" (Nov p23 L921-923) and 20-22% was a Q4FY26 target (Feb p11 L429). The Q1FY27 promise that does exist is 80% utilisation (Feb p13 L518-519). | That promise was missed: ~60% (Aug p3 L91). The 23.5% print was helped by inventory (item 6). | WRONG |

Checked 7, confirmed 6, wrong 1.

## PART 4: CREDIBILITY GRADE

B05 grade: C. My grade would be lower (D). The one positive holding the grade at C (GST restatement "unprompted accountability") does not survive the transcript. Four material contradictions between calls are unscored: allocation "done deal" vs 26 cr L, private-OMC "higher than government" vs Rs 60, "intentional shutdown" vs force majeure, and the SAF FID/date reversal. The capex-execution positives B05 credits are real: multi-feed capex delivered, CBG plant #1 economics, VGF secured.

## PART 5: CONSOLIDATED FINDINGS

| Sev | Finding |
|---|---|
| CRITICAL | F1. Missed repeated evasion (item 1): feedstock-split data deferred in Nov and May to the same analyst. Resolved in Aug, which reduces the harm. Rule 5 still classes it CRITICAL. |
| MAJOR | F2. Allocation contradiction (Nov 34 cr L PSU "done deal" vs May 26 cr L; May dodge) is under-weighted (item 2). |
| MAJOR | F3. Private-OMC pricing contradiction missed (item 3). |
| MAJOR | F4. Shutdown cause missed: "intentional" on calls vs force majeure in court (item 4). Legal risk to the Rs 1,062 cr claim. |
| MAJOR | F5. SAF FY28 to FY29 slip and FID-condition reversal missed. B05 states the date is unchanged (item 5). |
| MAJOR | F6. Core ethanol margin 9-9.5% and inventory-driven Q1 margin under-weighted (item 6). |
| MAJOR | F7. CBG attribution (Leafiniti 49% GAIL; TGPL "wholly-owned"; "report 51% of revenue") missed (item 7). |
| MAJOR | F8. 26% promoter pledge and the confused release answer missed (item 8). |
| MAJOR | F9. GST prior-period restatement misclassified as an unprompted accountability positive. It props the C grade (item 9). |
| MAJOR | F10. B05 "zero mention of DSCR/RPT, never asked" is not supported. The group-sourcing figures (<55% vs "100%" vs AR 72.6%) were never tested (item 10). |
| MAJOR | F11. The "44 cr L orders on hand" is really a base-case assumption. B05's make-up of it has no transcript support (item 11). |
| MAJOR | F12. Rs 460-500 cr unsold inventory not linked to the cash-conversion flag (item 12). |
| MAJOR | F13. B06 Q3 "CONTRADICTED" is not supported. It misframes TruAlt's claim, and GULPOLY supports the direction. It is carried to Halt 1 as the top priority and would misdirect verification. |
| MINOR | F14. B05 utilisation-denominator HIGH flag overstated. |
| MINOR | F15. B06 2E "never describe the SC stay mechanism" overstated (May p11 L426-429). |
| MINOR | F16. Q1FY27 80% utilisation promise missed and Q2 maintenance plan reversed; neither is in the promise table (item 21). |
| MINOR | F17. FY26 volume totals do not reconcile: 24 vs 26 vs a quarter sum of about 19-20 (item 20). |
| MINOR | F18. Blending: TruAlt says "E21 notification already in", peers say beyond-E20 is delayed (item 28). PENDING LIVE VERIFICATION of the notification. |
| MINOR | F19. Other minor misses: CBG margin drift, operating-days conflict, Unit 5 CTO vs "COD complete", "one-time" depreciation, SAF IRR/payback mix-up, advertising promise, outlook refusals (items 19, 27, 29-33). |
| MINOR | F20. B05 promise row "Q1FY27 EBITDA delivered" is not a promise-delivery item (Part 3). |

```yaml
stage: B12b
company: "TRUALT"
run_date: "2026-09-18"
model: "claude-opus-5"
status: complete
independent_flags_found: 34
caught: 11
partially_caught: 6
missed:
  - {severity: "CRITICAL", item: "Repeated evasion over 2 quarters: feedstock (grain vs sugar) volume split deferred to the same analyst in Nov and May, given only in Aug to another analyst", anchor: "Nov p15 L599-603; May p25 L962-966; Aug p8 L284-287"}
  - {severity: "MAJOR", item: "Private-OMC pricing told two ways: higher than government pricing (Feb) vs Rs 60-60.50 discounted contract (May, Aug)", anchor: "Feb p21 L832-835; May p4 L140-142, p26 L992-999; Aug p22 L841"}
  - {severity: "MAJOR", item: "Shutdown called intentional on investor calls but force majeure (rainfall) in the court claim behind the 15 cr L / Rs 1,062 cr order", anchor: "Nov p10 L396-398, p24 L946-947; Feb p11 L438-444; Aug p23 L895-896"}
  - {severity: "MAJOR", item: "SAF revenue slipped FY28 to FY29 and FID moved from after signed offtake (May) to capex in 2-3 months with no offtake (Aug); B05 says date unchanged", anchor: "Feb p9 L343-348; May p7 L258-259, p29 L1116-1122; Aug p7 L260-264, p9 L342-349"}
  - {severity: "MAJOR", item: "CBG attribution: showcase plant sits in Leafiniti, now 49% GAIL; TGPL called wholly-owned though Sumitomo holds 49%; MD says only 51% of revenue is reported", anchor: "May p6 L203-212, p9 L341-351, p20 L786-787; Aug p16 L605-607"}
  - {severity: "MAJOR", item: "26% promoter shares re-pledged to SBI/IREDA after listing; confused CFO answer on release in Aug", anchor: "Nov p17-18 L683-703; Aug p14-15 L555-569"}
  - {severity: "MAJOR", item: "Group sourcing stated as under 55% (May) and as 100% assured (Aug), group payables stretched to 2-3 months; never tested against the AR 72.6% RPT purchase share", anchor: "May p18-19 L708-729; Aug p24 L935-937; Nov p16 L642-649"}
  - {severity: "MAJOR", item: "FY27 44 cr L called orders on hand and also a base-case repeat of last year; up from 40 in May with no reason given; peer says the Supreme Court status quo blocks tenders", anchor: "Aug p8 L306-309, p9 L335, L352-355; May p20 L757-759; TRIVENI Aug p6 L307-312"}
  - {severity: "MINOR", item: "Revenue and CBG outlook refused on every call while volume and price are given with do-the-math", anchor: "Nov p19 L747-751; Feb p18 L720-723; May p19 L750; Aug p20 L783-785"}
  - {severity: "MINOR", item: "Q1FY27 80% utilisation promise missed (about 60%); Q2 two-month maintenance plan reversed", anchor: "Feb p13 L518-521; Aug p3 L91, p23 L889-892"}
  - {severity: "MINOR", item: "Advertising promised in May, not started by Aug", anchor: "May p23 L894-897; Aug p22 L862-866"}
  - {severity: "MINOR", item: "TruAlt says E21 notification is in; GULPOLY and TRIVENI say beyond-E20 is delayed or uncertified; PENDING LIVE VERIFICATION", anchor: "May p5 L177-178; GULPOLY Aug p7 L267-270; TRIVENI Jun p4 L192-195"}
  - {severity: "MINOR", item: "CBG margin figures drift across calls; Q1 dip explained as nothing, then as one-time costs", anchor: "Nov p6 L220-226; Feb p4 L129-131; May p5 L193-194; Aug p6 L227-233"}
  - {severity: "MINOR", item: "Q3FY26 operating days 58 (MD) vs 48-50 (CFO), three different causes given", anchor: "Feb p3 L110, p5 L185, p8 L321-325, p11 L425"}
  - {severity: "MINOR", item: "Nov says all plants commenced with COD complete; Unit 5 consent to operate only on 17-Dec-2025", anchor: "Nov p7 L263-265; Feb p4 L119-120"}
  - {severity: "MINOR", item: "CFO calls higher depreciation and finance cost a one-time effect", anchor: "May p9 L337-340"}
  - {severity: "MINOR", item: "SAF IRR answer mixes payback years and IRR", anchor: "Nov p21 L838-840"}
pipeline_flags_not_supported:
  - "B05 HIGH flag: zero mention of DSCR or related-party concentration and never asked; DSCR stated Aug p5 L191 and May p9 L356, group sourcing asked and answered May p18-19 L708-729 (only the cash-flow silence holds)"
  - "B05 1B/1C: SAF commissioning Aug-Oct 2027 and FY28 revenue unchanged across Q4 FY26 and Q1 FY27; transcripts say FY29 (May p29 L1116-1122, Aug p7 L260-264)"
  - "B05 2B/3C/credibility_basis: GST restatement as an unprompted accountability admission and PAT understatement; it was analyst-prompted and the explanation does not add up (Aug p20 L761-775)"
  - "B05 3D: 44 cr L order book composed as 26+8+6+15 netted; Aug p9 L335 says the 44 excludes the 15 cr L"
  - "B06 Q3: TruAlt maize-margin claim CONTRADICTED by peers; misframes a point-in-time sensitivity as FY26 compression, and GULPOLY Aug p4 L124-128, p6 L235-245 supports the direction"
  - "OVERSTATED, not scored as unsupported: B05 HIGH utilisation-denominator flag (Feb p4 L123-124 gives both figures; under 35% is a different period, May p5 L172-174); B06 2E that TruAlt never described the Supreme Court stay (May p11 L426-429)"
promise_delivery_spot_checks: {checked: 7, confirmed: 6, wrong: 1}
credibility_grade_concur: "lower; would grade D, because the GST positive that holds B05 at C does not survive the transcript and four material cross-call contradictions (allocation, private-OMC price, shutdown cause, SAF FID/date) are unscored"
findings:
  - {severity: "CRITICAL", finding: "Missed repeated evasion: feedstock split deferred in Nov and May to the same analyst", anchor: "Nov p15 L599-603; May p25 L962-966"}
  - {severity: "MAJOR", finding: "Allocation contradiction under-weighted: Nov 34 cr L PSU called a done deal vs May 26 cr L award; May dodge on why investors were not informed", anchor: "Nov p10 L403-404, p15 L595-598; May p10-11 L396-407, p26 L1023"}
  - {severity: "MAJOR", finding: "Private-OMC pricing contradiction missed", anchor: "Feb p21 L832-835; May p26 L992-999"}
  - {severity: "MAJOR", finding: "Intentional shutdown vs force majeure court claim missed", anchor: "Nov p10 L396-398; Feb p11 L438-444"}
  - {severity: "MAJOR", finding: "SAF FY28 to FY29 slip and FID reversal missed; B05 states the date unchanged", anchor: "May p29 L1116-1122; Aug p7 L260-264"}
  - {severity: "MAJOR", finding: "Core ethanol EBITDA about 9-9.5% ex co-products and subsidies, Q1 margin from cheap stock; under-weighted as delivered", anchor: "Aug p8 L294-301, p18 L692-697"}
  - {severity: "MAJOR", finding: "CBG attribution to minority partners and wrong consolidation statements missed", anchor: "May p6 L203-212, p20 L786-787; Aug p16 L605-607"}
  - {severity: "MAJOR", finding: "26% promoter pledge missed", anchor: "Nov p17-18 L683-703; Aug p14-15 L555-569"}
  - {severity: "MAJOR", finding: "GST prior-period restatement misclassified as an accountability positive that holds the C grade", anchor: "Aug p20 L761-775"}
  - {severity: "MAJOR", finding: "B05 zero-mention DSCR and RPT flag not supported; group-sourcing inconsistency untested", anchor: "Aug p5 L191; May p18-19 L708-729; Aug p24 L935-937"}
  - {severity: "MAJOR", finding: "44 cr L order book is an assumption; B05 composition has no transcript support", anchor: "Aug p8 L306-309, p9 L335, L352-355"}
  - {severity: "MAJOR", finding: "Rs 460-500 cr unsold inventory not linked to the cash-conversion flag", anchor: "Feb p18 L705-717; May p11 L408-410, p27 L1043-1053"}
  - {severity: "MAJOR", finding: "B06 Q3 CONTRADICTED verdict on maize margin not supported; carried to Halt 1 as the top priority", anchor: "Aug p8 L294-301; GULPOLY Aug p4 L124-128, p6 L235-245, p8 L310-321"}
  - {severity: "MINOR", finding: "B05 utilisation-denominator HIGH flag overstated", anchor: "Feb p4 L123-124; May p5 L172-174"}
  - {severity: "MINOR", finding: "B06 2E overstated; TruAlt did describe the Supreme Court no-new-allocation direction", anchor: "May p11 L426-429"}
  - {severity: "MINOR", finding: "Q1FY27 80% utilisation promise and Q2 maintenance reversal missing from the promise table", anchor: "Feb p13 L518-521; Aug p3 L91, p23 L889-892"}
  - {severity: "MINOR", finding: "FY26 volume totals do not reconcile (24 vs 26 vs quarter sum about 19-20)", anchor: "May p10 L388-390, p25 L960-961"}
  - {severity: "MINOR", finding: "E21 notification claim contradicted by peers; PENDING LIVE VERIFICATION", anchor: "May p5 L177-178; GULPOLY Aug p7 L267-270"}
  - {severity: "MINOR", finding: "Other minor misses: CBG margin drift, operating-days conflict, Unit 5 CTO, one-time depreciation, SAF IRR, advertising, outlook refusals", anchor: "see report Part 1 items 19, 27, 29-33"}
  - {severity: "MINOR", finding: "B05 promise row Q1FY27 EBITDA delivered is not a promise-delivery item", anchor: "Nov p23 L921-923; Feb p11 L429; Feb p13 L518-519"}
critical_count: 1
major_count: 12
minor_count: 7
material_found: 18
material_caught: 10
acceptance_rate: 55.6
coverage_basis: "18 material (1 CRITICAL, 17 MAJOR) of 34 listed; 6 caught plus 4 partially caught = 10 counted as caught; 8 missed; on fully caught alone the rate is 33.3%"
```
