# STAGE 6: PEER CONCALL VERIFICATION. ESCONET (Esconet Technologies Ltd), run 2026-10-05

Model: claude-sonnet-5-5. Protocol 1.1. Claims tested: the 8 peer_questions in B05-concall.yaml.

## 0. Method, anchors, units

- Anchor format: (PEER, Q_ FY__ call, p.N, speaker). p.N is the "[page N]" marker in the extracted .txt, not the printed page number. The printed page is N minus 1 for all 12 files.
- Units: Netweb states financials in INR million (₹ mn) and orders in ₹ Cr as spoken. Rashi Peripherals (RPTECH) and Orient Technologies (ORIENTTECH) state ₹ Cr, except RPTECH Q2 FY26 (₹ mn). Each figure below names its unit.
- Esconet figures come from B05 (anchored there to Q1 FY27 board outcome and the Aug 2026 call, ₹ Lakhs). Nothing here is read from the Esconet corpus again.
- "Derived" marks arithmetic done here on two anchored figures. No other number is computed.

### Transcript identity check (own first page)

| File label | Issuer | Quarter and call date | Check |
|---|---|---|---|
| NETWEB Nov 2025 | Netweb Technologies India Ltd | Q2 FY26, 3 Nov 2025 | matches |
| NETWEB Jan 2026 | Netweb Technologies India Ltd | Q3 FY26, 19 Jan 2026 | matches |
| NETWEB May 2026 | Netweb Technologies India Ltd | Q4 FY26, 4 May 2026 | matches |
| NETWEB Aug 2026 | Netweb Technologies India Ltd | Q1 FY27, 29 Jul 2026 (filed 1 Aug) | file label says Aug, call was July |
| RPTECH Nov 2025 | Rashi Peripherals Ltd | Q2 FY26, 10 Nov 2025 | matches |
| RPTECH Feb 2026 | Rashi Peripherals Ltd | Q3 FY26, 4 Feb 2026 | matches |
| RPTECH May 2026 | Rashi Peripherals Ltd | Q4 FY26, 15 May 2026 | matches |
| RPTECH Aug 2026 | Rashi Peripherals Ltd | Q1 FY27, 5 Aug 2026 | matches |
| ORIENTTECH Aug 2025 | Orient Technologies Ltd | Q1 FY26, 14 Aug 2025 | matches |
| ORIENTTECH Nov 2025 | Orient Technologies Ltd | Q2 FY26, 14 Nov 2025 | matches |
| ORIENTTECH Feb 2026 | Orient Technologies Ltd | Q3 FY26, 19 Feb 2026 | matches |
| ORIENTTECH Aug 2026 | Orient Technologies Ltd | Q1 FY27, 13 Aug 2026 | matches |

All 12 files present. No peer file is missing.

### Does each peer's product chain fit Esconet?

- NETWEB: partial fit. It designs and builds own-brand HPC, private cloud and AI servers on NVIDIA, Intel and AMD silicon. This is the TO state for HexaData. Scale does not fit: Netweb revenue was ₹21,836 mn in FY26 (NETWEB, Q4 FY26, p.3), with 125 R&D staff (NETWEB, Q1 FY27, p.16). Netweb says it will not run data centres or cloud services (NETWEB, Q2 FY26, p.16). Esconet runs ZeaCloud, so Netweb is a poor comp for the cloud line.
- RPTECH: weak fit for server economics. It is a distributor with 3 to 4% EBITDA margin. It fits only as the FROM state (low-margin hardware flow), and it shows how the same price cycle looks to a percentage-markup business.
- ORIENTTECH: best structural fit for the legacy SI line (infrastructure sales plus managed services). It has no GPU-server own-brand line. Its AI revenue is small by its own account.
- No peer is a small-cap GPU-server integrator at Esconet scale. Weight peer margins as ladder rungs, not as point benchmarks.

## PART 1. CLAIM-BY-CLAIM VERIFICATION

### Q1. Hardware price inflation: inventory gain or cost shock; peer margin gain on stock; path to FY28

| Field | Content |
|---|---|
| Claim | MD credits hardware price volatility and rising inventory for Q1 FY27 margins and says analysts expect the trend into FY28. The FY26 press release called the same rise a cost shock above 100% (B05 peer_questions Q1; B05 flags FLAG-MARGIN-BASIS). Question: tailwind via stock at lower cost, or cost shock via fixed-price orders? |
| Verdict | PARTIALLY VERIFIED (peers split by pricing architecture; no peer quantifies a stock gain) |
| Peer evidence, cost shock side | ORIENTTECH, Q3 FY26 call, p.4-5 (Ajay Sawant): "we have to execute the contracts at the same price, which we have signed up earlier and this is there till 31st of March." Margin pressure followed. Q3 FY26 standalone revenue was ₹198.23 Cr, EBITDA ₹3.02 Cr (p.3). Consolidated EBITDA margin fell to 3.19% in Q4 FY26 (ORIENTTECH, Q1 FY27, p.6, Shailesh Mandani). He said "Margin pressures are definitely there" (Q3 FY26, p.7). This matches Esconet's FY26 cost shock. |
| Peer evidence, recovery side | ORIENTTECH, Q1 FY27 call, p.4: "The company continued to work closely with OEMs to ensure timely cost pass through with the impact of input cost movement being progressively reflected in pricing." EBITDA margin rose 438 bp to 7.57% in Q1 FY27 (p.6). Orient credits pass-through and repricing, not stock. |
| Peer evidence, stock-gain side | RPTECH, Q3 FY26 call, p.12 (Rajesh Goenka): price rise "has obviously helped us to improve not only our top line, but bottom line also to some extent." Same call p.10: "Normally, in distribution... the margins are more or less fixed. So we cannot have too much of extra margin." When asked for the inventory gain, p.16: "Can we take these numbers offline, Deepak, because these are specific numbers." RPTECH, Q1 FY27, p.15: channel partners hold stock bought at "Rs. 80 somewhere in April or May" and sell at the new price near 100. The gain sits with whoever holds low-cost stock. |
| Peer evidence, denial | NETWEB, Q1 FY27 call, p.8 (Sanjay Lodha), asked directly if inventory bought at lower memory prices lifted margin (Divyesh Mehta, p.7): "There is no question of some memory pricing or something because basically, we have the pricing power." p.13 (Sanjeev Sancheti): "there is no question of a significant change in the costing on what we got order on and what we are billing." Netweb says new orders are bid at current prices (p.13). Netweb calls its 110-day inventory "a hedge, not a risk" (Ankit Singhal, p.10), taken "deliberately" (p.13). NETWEB, Q4 FY26, p.13: Lodha declined to guide on inventory and margin when asked the same question (Sandeep Shah). |
| Magnitude | No peer states a rupee or basis-point inventory gain. RPTECH declined (Q3 FY26, p.16). Netweb denies one. Orient does not mention one. |
| Run-through to FY28 | RPTECH, Q1 FY27, p.3 (Kapal Pansari): "Independent forecasts expect this to persist through 2028 as well" (a third-party view). RPTECH, Q1 FY27, p.11: price-rise "speed should be half" in Q2. NETWEB, Q1 FY27, p.10 (Ankit Singhal): "we do not see a softening in next couple of quarters, maybe a year or so." ORIENTTECH, Q1 FY27, p.4 and Q3 FY26, p.6: shortage "throughout FY27". Only RPTECH reaches 2028, and it cites others. |
| Peers silent | None fully silent. ORIENTTECH is silent on any stock gain. |
| Net read | Both of Esconet's statements have a peer analogue. The shock matches Orient's fixed-price rate contracts (FY26 H2). The gain direction matches RPTECH ("to some extent") but not Netweb, which denies it. Orient's rebound has a third explanation: contracts rolling onto new prices. [INFERENCE] The separating observation for Esconet is the share of Q1 FY27 revenue billed under orders priced before the rise, against revenue priced at current cost. Esconet's inventory build (518.50 Lakhs per B05 FLAG-MARGIN-BASIS) is small, which weakens the stock-gain reading on size alone. FY28 persistence rests on one peer citing third parties. |

### Q2. Gross margin on AI/GPU server mix versus legacy SI; peer gross and EBITDA margins ex other income

| Field | Content |
|---|---|
| Claim | Esconet cites 7 to 8% gross margin on legacy SI and 10 to 15% on HexaData (Jun 2025, B05 guidance row). Q1 FY27 standalone gross margin was 29.2% (B05 promise_delivery, derived from Q1 BM p.4, ₹ Lakhs). Test: structural mix or outlier? |
| Verdict | PARTIALLY VERIFIED (margin ladder confirmed; no peer discloses gross margin by AI versus legacy mix; no peer shows anything near 29% gross) |
| Peer evidence, own-brand OEM | NETWEB, Q1 FY27, p.5 (Ankit Singhal): operating EBITDA ₹1,205 mn on revenue ₹8,197 mn, margin 14.7%; PAT margin 10.3%. AI was ₹5,105.70 mn, 62% of revenue (p.3, Lodha). Guide is 13 to 14% EBITDA (NETWEB, Q4 FY26, p.7, Ankit Singhal). Large "strategic" AI orders carry margins "150 to 200 basis points lower at PBT level" (NETWEB, Q2 FY26, p.7, Ankit Singhal; repeated Q3 FY26, p.9). So the AI mix at Netweb does not carry a higher margin than its base. Netweb gross margin is not stated on any call (NOT FOUND). |
| Peer evidence, SI | ORIENTTECH, Q1 FY26, p.8 (Ajay Sawant): infrastructure products and solutions "around 8% to 10% margin"; services LOB "15% to 20%"; cyber services above 20%. The basis (gross or EBITDA) is not stated. Mix was 65% infrastructure, 35% services (p.8). Q1 FY27 consolidated EBITDA margin 7.57% on revenue ₹201.92 Cr (ORIENTTECH, Q1 FY27, p.6). Sawant, Q1 FY27, p.10: "To survive in the market, I think 5-6% is the minimum gross margin that we need to earn." |
| Peer evidence, distributor | RPTECH, Q1 FY27, p.5 (Himanshu Shah): consolidated EBITDA ₹173 Cr on revenue ₹5,102 Cr, margin 3.38%; PAT margin 2.05%. Same call, p.14: gross margin "is outcome of the product mix"; the PES segment is lower margin than LIT. PAT range for the industry is 1.5 to 1.75% (RPTECH, Q4 FY26, p.15). RPTECH gross margin level is not stated (NOT FOUND). |
| Esconet position on this ladder | Esconet standalone EBITDA ex other income was 12.75% and consolidated 7.03% in Q1 FY27 (B05 FLAG-MARGIN-BASIS, Q1 BM p.4). Standalone sits inside Netweb's 13 to 14% own-brand band. Consolidated sits at Orient's 7.57%. [INFERENCE] The parent behaves like a Netweb-tier OEM this quarter and the group like an SI. Esconet's own 7 to 8% legacy SI gross figure sits near Orient's 8 to 10% (basis mismatch noted). |
| Peers silent | None silent on margin. No peer split gross margin by AI versus legacy. |
| Net read | Peers confirm three rungs: distributor near 3.4% EBITDA, SI near 7.6%, own-brand OEM near 14.7%. They do not confirm that a 29.2% gross margin is structural, because no peer reports gross margin. The one peer with a large AI mix (Netweb) says AI mix lowers margin at the large-order end. The 29.2% remains unbenchmarked and the B05 reading A versus B split stands open. |

### Q3. Peer debtor days, inventory days, OCF to PAT, order book and book-to-bill

| Field | Content |
|---|---|
| Claim | Esconet says it has no formal order book (60 to 90 day order cycle, 30 to 90 day collection), guesses ₹20 to 25 Cr, gave no cash flow, and the 20.2 debtor days is NOT FOUND (B05 guidance, flags). |
| Verdict | PARTIALLY VERIFIED (cycle and collection ranges corroborated; the no-disclosure position is not a peer norm; 20.2 days cannot be tested) |
| NETWEB working capital | Q1 FY27 (p.5): receivable 78 days, inventory 110 days, cash conversion cycle 96 days. Q4 FY26 (p.5): receivable 86, inventory 86, cycle 84. Q3 FY26 (p.4): cycle 69. Q2 FY26 (p.4): receivable 117, inventory 72, cycle 120. Guide: cycle "90 to 110" (Q4 FY26, p.8 and p.16). |
| NETWEB cash conversion | FY26 operating cash flow ₹1,715 mn (Q4 FY26, p.5) against FY26 PAT ₹2,058 mn (p.4): 83% (derived). 9M FY26 operating cash flow ₹134 Cr (Q3 FY26, p.9, Sancheti) against 9M PAT ₹1,352 mn (p.4): about 99% (derived). |
| NETWEB order book | Q1 FY27 (p.4): order book ₹25,069.35 mn, L1 position ₹8,480.47 mn, pipeline ₹104,100 mn (as spoken, corrected on the call). Order book is 3.06 times Q1 revenue ₹8,197 mn (derived). Order cycle was "8 to 12 weeks", now "16 to 20 weeks" (p.11, Lodha). Earlier: "order execution cycle is somewhere around 8 weeks to 16 weeks" and "my order book doesn't give you a clear indication" (Q2 FY26, p.6 and p.20, Lodha). So Netweb shares Esconet's short cycle and still discloses order book and pipeline. |
| RPTECH working capital | Q1 FY27 (p.6): inventory 55, debtors 41, creditors 40, working capital 56 days. Q4 FY26 (p.5): 56, 46, 44, 58. Q3 FY26 (p.5): 56, 47, 43, 60. Q2 FY26 (p.5): receivables 46, payables 44, inventory 59, working capital 61. |
| RPTECH cash conversion | FY26 operating cash flow ₹514 Cr (Q4 FY26, p.5) against consolidated PAT ₹282 Cr (p.5): 182% (derived). 9M FY26 operating cash flow ₹34 Cr (Q3 FY26, p.5) against 9M PAT ₹196 Cr (p.5): 17% (derived). An analyst says only two of ten years had positive operating cash flow (Q3 FY26, p.13, Madhur Rathi; analyst statement, not company). |
| ORIENTTECH order book | Q1 FY27 (p.5): ₹375.43 Cr against ₹200 Cr guided at Q4 FY26; consolidated Q1 revenue ₹201.92 Cr (p.6), so 1.86 times (derived). Billing "between Q3 and Q4" (p.9). Debtor days, inventory days and cash flow are not on any Orient call (NOT FOUND). |
| Where Esconet sits | Peer receivable days run 41 (RPTECH) to 78 (NETWEB) in Q1 FY27. Esconet's 30 to 90 day collection range spans both. The 20.2 debtor-day figure would sit under the lowest peer (41). It stays NOT FOUND and untestable. |
| Peers silent | ORIENTTECH on days and cash flow. RPTECH on order book (distributor, not applicable). |
| Net read | Two peers confirm a 30 to 90 day collection range. One peer (Netweb) confirms the short order cycle. Netweb and Orient both disclose an order book, and Netweb, RPTECH report days and cash flow, so Esconet's gaps are a disclosure choice, not an industry norm. Peer cash conversion is volatile (RPTECH 17% to 182%), so a single-quarter cash flow figure from Esconet would not settle quality either way. |

### Q4. Government and PSU share, PSU receivables, sovereign and Make in India demand

| Field | Content |
|---|---|
| Claim | Esconet says government was 40 to 45% of FY26 revenue and is lower in FY27; sovereign stack is the stated theme (B05 guidance). |
| Verdict | PARTIALLY VERIFIED (share and sovereign driver confirmed by Netweb only; PSU receivable days UNVERIFIABLE) |
| Share evidence | NETWEB, Q4 FY26, p.13 (Lodha): "50% is government, 50% is enterprise." Q2 FY26, p.10: that quarter 60% enterprise and 40% government. ORIENTTECH government and PSU share: 12.29% in Q1 FY27 (p.6), 19.19% in Q3 FY26 (p.3), 19.65% in Q2 FY26 (p.3), 15.88% in Q1 FY26 (p.4). Esconet's 40 to 45% sits at Netweb's level and well above Orient's. |
| Sovereign demand | NETWEB, Q1 FY27, p.3 (Lodha): "Sovereign AI compute... has become a strategic national imperative." Q4 FY26, p.9 (Lodha): GPU target moved from 10,000 to 25,000 and "now they are even ready to go up to 100,000 GPUs." Q3 FY26, p.7 (Hirdey Vikram): the on-prem government procurement "is yet to start". Q1 FY27, p.11: on-prem demand now in pipeline. RPTECH, Q4 FY26, p.8: "Make in India is still very limited" for its own components. ORIENTTECH, Q3 FY26, p.8: government investment in data centres favours "managing those data centers" for firms like Orient. |
| PSU receivables | No peer gives PSU or government receivable days. The only figure is an analyst's assertion of "3 to 4 months" (NETWEB, Q2 FY26, p.12, Vibhor Singhal). Netweb's strategic AI orders were not placed by government directly but through "empanelled organizations", backed by advances and letters of credit (Q2 FY26, p.12-13). Netweb overall receivable days were 114 at Dec 2025 (Q4 FY26, p.5). UNVERIFIABLE as a PSU number. |
| Peers silent | ORIENTTECH on sovereign server demand; both on PSU days. |
| Net read | Netweb corroborates both the 40 to 50% government share and the sovereign driver. Orient does not, because its mix is lower. The AI Mission leg that matters most to a server maker has two parts, and Netweb says the government's own-premises part had not started by Jan 2026. PSU collection days stay open for Esconet. |

### Q5. Industry growth rates: AI infrastructure, sovereign cloud, cybersecurity

| Field | Content |
|---|---|
| Claim | Esconet's calls cite AI, data sovereignty, cloud and cyber demand without numbers (B05 peer_questions Q5). |
| Verdict | PARTIALLY VERIFIED (AI, data centre and cloud directions confirmed with numbers; sovereign cloud and cyber growth NOT stated by any peer) |
| Peer evidence | NETWEB, Q1 FY27, p.16 (Sancheti): "a 38% CAGR at the national level" for the AI product line over the next 4 years. Same call p.9: world AI compute demand for "at least next 1.5 to 2 years." NETWEB, Q2 FY26, p.20: HPC total market near ₹4,000 Cr, Netweb's addressable near ₹1,000 Cr, Netweb share 30 to 35% of that. ORIENTTECH, Q1 FY27, p.7: an analyst cites CRISIL data of 30 to 35% data centre CAGR and 22 to 28% public cloud growth; Sawant answers "data center, cloud are going to grow exponentially" and gives no rate. RPTECH: IT hardware market "10% to 12% annually" (Q2 FY26, p.3); India PC market 15.9 million units in CY2025, +10.2% (Q4 FY26, p.3); IDC sees a 5 to 10% unit dip in CY2026 (Q4 FY26, p.4). |
| Contra evidence | ORIENTTECH, Q1 FY26, p.9: "agentic AI, Gen AI and all those things... not able to materialize in terms of revenue perspective." Q2 FY26, p.8: "hardly customers are moving on AI for production environment." By Q1 FY27 (p.10) Sawant says AI is "a major revenue source for Orient" but gives no figure. |
| Peers silent | No peer gives a cybersecurity or sovereign cloud growth rate. |
| Net read | AI hardware demand is confirmed at 38% a year by one peer and by order books. Data centre and cloud rates come to Orient only via an analyst. Cyber and sovereign cloud rates are not in the peer set. Enterprise AI software demand was still proof-of-concept at Orient in late 2025. The demand claim is strong for compute hardware and unproven for the services lines. |

### Q6. Market share gain in Indian server OEM

| Field | Content |
|---|---|
| Claim | Esconet implies share gain in AI servers and says it competes case by case with Cisco, HP, Lenovo and Dell (B05 peer_questions Q6). |
| Verdict | UNVERIFIABLE (no peer reports share gain or loss in Indian server OEM for any vendor) |
| Peer evidence | NETWEB, Q1 FY27, p.7 (Lodha), asked for market share: "you can see basically how numbers are speaking. Basically, 62% of revenue came from the AI." No figure. Q2 FY26, p.16: "I don't say that I have a monopolistic situation." Only share figure: HPC 30 to 35% of an addressable ₹1,000 Cr (Q2 FY26, p.20). RPTECH, Q1 FY27, p.7 and p.18: about 10% of its growth came from "improved market share", but in distribution, not servers. RPTECH adds Dell commercial (about 5% of Q1 FY27 revenue, p.10) and says four distributors carry Dell in India (Q2 FY26, p.15). ORIENTTECH, Q3 FY26, p.6: a hyperscale customer "moved lots of barrels from us to directly on the hyperscaler vendor." Q1 FY27, p.13: Orient declined an 18-week delivery-penalty deal that a competitor took (₹400 Cr against Orient's ₹97 Cr, per an analyst). |
| Peers silent | Netweb and Orient name no rival server OEM share. |
| Net read | Silence. The pool is growing, so absolute gain for a small vendor is possible. The largest sovereign AI tenders went to the larger design-and-build OEM (NETWEB, Q4 FY26, p.19: ₹1,600 Cr strategic orders). [INFERENCE] The visible winners of large AI orders in this peer set have scale and design capability Esconet is not shown to have. This is not a share-loss statement. |

### Q7. Customer AI and data-centre capex: accelerating or digesting; GPU allocation constraints or cancellations

| Field | Content |
|---|---|
| Claim | NVIDIA Elite status is cited as privileged access to scarce supply; MD cites pipeline strength and force majeure risk (B05 peer_questions Q7). |
| Verdict | VERIFIED (two peers: acceleration and partner allocation hold; constraints sit in memory, storage and lead times; no cancellations) |
| Acceleration | NETWEB, Q1 FY27, p.9-10 (Lodha): AI demand "for at least next 1.5 to 2 years"; "data center equipment is under shortage"; order book plus L1 ₹33,550 mn (derived from p.4). RPTECH, Q4 FY26, p.10 (Rajesh Goenka): "funnels of almost INR20,000 crores, INR25,000 crores" of AI data centre projects. RPTECH, Q1 FY27, p.13: "good pipeline of these projects, which will continue to be there for next three quarters at least." |
| Allocation | NETWEB, Q2 FY26, p.8 (Lodha): "we have sufficient allocations", as an NVIDIA OEM partner. RPTECH, Q1 FY27, p.9 (Goenka): "so far, we have been able to get good allocation... this is an orange alert for us. We track it on a weekly basis." |
| Constraint evidence | NETWEB, Q1 FY27, p.11: order cycle stretched from 8-12 to 16-20 weeks. RPTECH, Q3 FY26, p.16: "we are not getting price confirmation valid for 6 months or 9 months because of the price volatility." RPTECH, Q1 FY27, p.15: entry-level laptops have "almost 50% shortage." ORIENTTECH, Q1 FY27, p.13: "The delivery is not happening in 14 or 16 weeks." |
| Digestion signals | RPTECH deprioritised large AI data-centre deals for working-capital reasons (Q1 FY27, p.13-14: debt ratio near 0.5 "will go at least 2x"). NETWEB, Q3 FY26, p.7: government on-prem leg not started. A search of all 12 files finds one customer withdrawal, at Orient (Q1 FY27, p.10, contingent liability from telecom customers), and no GPU order cancellation. |
| Peers silent | None. |
| Net read | Acceleration and privileged supply for partner-status vendors are confirmed by Netweb and RPTECH. Both are interested parties on their own allocation, so this does not prove Esconet's tier of access. The force majeure risk in Esconet's language is real in the peer record, as lead times and price validity have shortened. |

### Q8. MeitY empanelment, sovereign cloud ramp, asset intensity

| Field | Content |
|---|---|
| Claim | ZeaCloud MeitY empanelment is the stated growth engine and has slipped; ZeaCloud is asset-heavy with a depreciation drag (B05 peer_questions Q8). |
| Verdict | UNVERIFIABLE (no peer mentions MeitY empanelment or its timeline; adjacent adverse evidence recorded) |
| Peer evidence | A text search of all 12 files finds no "MeitY", no "sovereign cloud" and no mention of ZeaCloud. The only hit for "empanel" is Netweb's note that AI Mission orders came via "empanelled organizations" (NETWEB, Q2 FY26, p.12), which is not cloud empanelment. NETWEB, Q2 FY26, p.16: "we don't want to get into setting up data centers or providing cloud services directly." |
| Adjacent, sovereign adoption | ORIENTTECH, Q1 FY26, p.10, asked about Indian sovereign platforms: "Still I don't see so much of adoption happening, still there is a time." And "I don't see, they will be able to give the entire value, which probably AWS or Azure is able to give you." This is 14 months old and about private customers. |
| Adjacent, asset intensity and slippage | ORIENTTECH SOC build: property "more than Rs.10 crore", infrastructure "Rs.6 to Rs.7 crores", about ₹2 Cr a year of skill cost (Q1 FY26, p.7). Operational by 30 Sep 2025 (p.6); revenue "latter half of Q3" (Q2 FY26, p.5); builder delay (Q2 FY26, p.9); ramp "next 24 to 36 months" (Q3 FY26, p.8); revenue still "single-digit percentage" (Q1 FY27, p.10). ORIENTTECH DaaS: IPO money "Rs. 45 crores deployed against... Rs. 80 crores budgeted" (an analyst's figures; Sawant says ₹35 Cr remains, Q1 FY27, p.6). |
| Peers silent | Netweb and Orient on MeitY. |
| Net read | No peer data on the empanelment date or the government cloud ramp. The only peer with a comparable build (Orient SOC) shows the same pattern as ZeaCloud: capex first, revenue dates moving, ramp measured in years. That is pattern evidence only. |

## PART 2. UNPROMPTED CROSS-READ

### 2A Demand environment
- Split, not consensus. The compute hardware peers report a boom: Netweb revenue +172.1% YoY to ₹8,197 mn (NETWEB, Q1 FY27, p.3) and RPTECH +62% to ₹5,102 Cr (RPTECH, Q1 FY27, p.5). The services-led SI is flat: ORIENTTECH Q1 FY27 revenue ₹201.92 Cr against ₹212.56 Cr in Q1 FY26 (Q1 FY26, p.3), down 5.0% (derived; bases assumed alike, not stated).
- Esconet's framing is a growth demand story. Its standalone Q1 FY27 revenue was below the FY26 quarterly average (B05 FLAG-GUIDANCE-INCONSISTENCY). That pattern resembles the SI peer, not the AI OEM.
- RPTECH adds a caution: units fall about 10% while price lifts value (Q1 FY27, p.6) and consumer demand is price-limited.

### 2B Pricing and input costs
- Consensus on direction: memory, storage and CPU prices are up. RAM is "2x or even 3x" and other components 50 to 100% (RPTECH, Q3 FY26, p.6 and p.13). Netweb sees no easing for "a year or so" (Q1 FY27, p.10).
- Peers do not agree on the margin effect. Percentage-markup distributors see absolute margin rise (RPTECH, Q4 FY26, p.16). The own-brand OEM reports margin inside its band and denies a pricing gain. The fixed-price SI took a loss first, then recovered (Orient 3.19% to 7.57%).
- This matches Esconet's two-phase record (FY26 shock, Q1 FY27 gain) most closely at Orient.

### 2C Capex cycle
- No peer is expanding capacity. Netweb has "no capex expansion" beyond routine ₹20 to 25 Cr (NETWEB, Q4 FY26, p.7) and runs at 65 to 70% utilisation (p.11). RPTECH grows through acquisition (VDA, 67% stake) and a JV, and adds branches (RPTECH, Q1 FY27, p.4-5). Orient is slow on its IPO-funded capex.
- Verdict: working capital, not plant, is the industry constraint. Netweb took an enabling resolution for capital "for working capital" (NETWEB, Q1 FY27, p.14-15). RPTECH leverage would double on large projects.
- Esconet is a lone expander into asset-heavy cloud. Netweb refuses the model (NETWEB, Q2 FY26, p.16), RPTECH stays distribution-led, and Orient's SOC ramp is slow.

### 2D Competitive mentions
- No peer mentions Esconet, HexaData, ZeaCloud or Fluidech (search of all 12 files; nothing to quote).
- Closest relevant statements: Netweb calls itself "India's only full-stack domestic provider for high-end computing systems" (NETWEB, Q4 FY26, p.3) and says it has an NVIDIA OEM partnership held by "less than 10 people in the world" with supply priority (Q2 FY26, p.8). Orient says Dynacons is "a good friend" and not a competitor (ORIENTTECH, Q3 FY26, p.8). None describes a small GPU-server rival.
- The silence is informative at the margin: the large AI orders and the share talk in this set involve Netweb, Dell-via-RPTECH and global OEMs, and a small vendor does not register.

### 2E Risks peers discuss that Esconet does not
- Customer disintermediated by OEM-direct (ORIENTTECH, Q3 FY26, p.6).
- Fixed-price rate contracts against rising input cost (ORIENTTECH, Q3 FY26, p.4-5).
- Delivery penalties on long lead times: "I am not ready to get into that kind of engagement" (ORIENTTECH, Q1 FY27, p.13).
- Component shortage tracked weekly as an "orange alert" (RPTECH, Q1 FY27, p.9). Supplier price validity of only weeks (RPTECH, Q3 FY26, p.16).
- Supplier exit from a product line: Micron's Crucial brand end of life (RPTECH, Q3 FY26, p.12).
- Consumer affordability and unit decline (RPTECH, Q4 FY26, p.14; Q1 FY27, p.6).
- Channel stock build: "inventory is high but it is not a very big concern" (RPTECH, Q1 FY27, p.10).
- Large-order receivable delay: Yotta ₹280 Cr collected late (RPTECH, Q2 FY26, p.15).
- Growth funding and quarter-end short-term borrowing (NETWEB, Q4 FY26, p.16-17; Q1 FY27, p.14-15).
- Contingent liabilities: GST show-cause notices (RPTECH, Q1 FY27, p.16-17); ₹4.4 Cr AWS-related reversal (ORIENTTECH, Q1 FY27, p.10).
- GPU substitutes (ASIC, TPU) and Chinese open models (NETWEB, Q3 FY26, p.9-10; Q1 FY27, p.11).
- Inventory valuation policy change restating prior balance sheet (NETWEB, Q1 FY27, p.17).
- Forex: mark-to-market loss in expenses, hedge gain in other income (NETWEB, Q4 FY26, p.5). Relevant to how Esconet's other income of 193.21 Lakhs (B05 analyst_note) is read.

## PART 3. PEER COVERAGE MAP

| Peer | Quarter | Used how | Key contribution |
|---|---|---|---|
| NETWEB | Q2 FY26 (3 Nov 2025) | SUBSTANTIVE | Strategic AI orders 150 to 200 bp lower margin; cash cycle 120 days; LC-backed government-linked orders; refuses cloud services |
| NETWEB | Q3 FY26 (19 Jan 2026) | SUBSTANTIVE | 9M operating cash flow ₹134 Cr against PAT; memory pricing aligned at order date; on-prem AI leg not started |
| NETWEB | Q4 FY26 (4 May 2026) | SUBSTANTIVE | FY26 operating cash flow ₹1,715 mn; 13 to 14% EBITDA guide; declined to link inventory to margin; 50/50 government mix |
| NETWEB | Q1 FY27 (29 Jul 2026) | SUBSTANTIVE | Denies memory-price margin gain; 78 receivable days; 110 inventory days; order book and 38% AI CAGR |
| RPTECH | Q2 FY26 (10 Nov 2025) | SUBSTANTIVE | Working-capital days; Yotta receivable delay; shortage as a named risk |
| RPTECH | Q3 FY26 (4 Feb 2026) | SUBSTANTIVE | "To some extent" bottom-line help from price; refused inventory-gain number; price validity of weeks |
| RPTECH | Q4 FY26 (15 May 2026) | SUBSTANTIVE | FY26 operating cash flow ₹514 Cr; margins intact; AI deal funnel ₹20,000 to 25,000 Cr |
| RPTECH | Q1 FY27 (5 Aug 2026) | SUBSTANTIVE | EBITDA 3.38%; channel stock bought at 80 sold near 100; price-rise speed halving; allocation "orange alert" |
| ORIENTTECH | Q1 FY26 (14 Aug 2025) | SUBSTANTIVE | SI margin ladder 8 to 10% and 15 to 20%; sovereign platform adoption weak; AI not in revenue |
| ORIENTTECH | Q2 FY26 (14 Nov 2025) | CITED-ONLY | AI still proof-of-concept; SOC revenue date moved (also in other Orient calls) |
| ORIENTTECH | Q3 FY26 (19 Feb 2026) | SUBSTANTIVE | Fixed-price rate contracts to 31 Mar; customer moved to OEM-direct; shortage through FY27 |
| ORIENTTECH | Q1 FY27 (13 Aug 2026) | SUBSTANTIVE | Margin 3.19% to 7.57% via pass-through; order book ₹375.43 Cr; delivery-penalty refusal |

## PART 4. TRIANGULATION SUMMARY

- Claims verified: 1 of 8 (Q7).
- Claims partially verified: 5 of 8 (Q1, Q2, Q3, Q4, Q5).
- Claims unverifiable: 2 of 8 (Q6, Q8).
- Claims contradicted: 0. Nothing goes to synthesis as a formal contradiction. Two peer-split items go as priority flags, below.
- Most consequential tension (not a formal contradiction): the Q1 FY27 margin mechanism. Esconet credits price volatility and stock. Netweb says "There is no question of some memory pricing" (NETWEB, Q1 FY27, p.8) and denies any gain. Orient, the closest structural peer, shows the same FY26 shock and Q1 FY27 rebound and credits pass-through repricing (ORIENTTECH, Q1 FY27, p.4). Only RPTECH allows a stock gain, "to some extent", and will not size it. The stock-gain reading has the weakest peer support of the three readings.
- Strongest independent confirmation: partner-status vendors get GPU and component allocation while memory and storage tighten. Netweb (Q2 FY26, p.8) and RPTECH (Q1 FY27, p.9) both say so, and both show lead times and price validity shortening.
- Overall: the peer set complicates the narrative. Direction on demand for AI compute, a 38% AI CAGR at Netweb, and the shock-then-recovery margin shape all match Esconet's story. But no peer supports a 29% gross margin as a norm, the one large-AI peer says AI mix carries lower margin at the large-order end, peers disclose order books and cash flow that Esconet does not, and nothing in the set speaks to MeitY, sovereign cloud ramp, or small-vendor share. The services lines (cloud, cyber) have the thinnest peer support. Neither side of the bull-bear case gains clean cover from these three peers.

### Part 5. Cross-peer hypothesis

cross_peer_hypothesis: "In this memory-price cycle, margin outcome splits on contract-repricing lag, not on business model. Fixed-price books (Orient until 31 Mar 2026; Esconet in FY26 per B05) took a shock in FY26 H2. Captive-supply and percentage-markup peers (Netweb, RPTECH) held margin. No peer says this. Orient says it had fixed-price rate contracts (Q3 FY26, p.4-5) and later pass-through (Q1 FY27, p.4). RPTECH says price-rise speed will halve in Q2 (Q1 FY27, p.11) and Orient says pricing is more stable (Q1 FY27, p.4). Together they imply Orient's 3.19% to 7.57% rebound (Q1 FY27, p.6) and Esconet's Q1 FY27 jump are a one-time reset as contracts reprice, not expansion. Test: if price-rise speed halves, Orient and Esconet Q2 FY27 margins should hold or fall back toward the repriced level, while Netweb and RPTECH stay in band. Any Esconet standalone gross margin above the repriced level needs stock bought before the rise, and that fades as stock turns."

[INFERENCE] label: the whole hypothesis is an inference from combined peer statements.

## OPERATOR NOTES (data quality)

- RPTECH Q1 FY27 transcript conflicts with itself: Kapal Pansari says EBITDA ₹155 Cr, up 50% (p.4); the CFO says ₹173 Cr, up 55%, margin 3.38% (p.5). The CFO's margin matches ₹173 Cr on ₹5,102 Cr (3.39%, derived). This report uses the CFO figure.
- ORIENTTECH Q3 FY26 transcript is inconsistent on the Digital India Corporation contract: "around Rs. 15 crores" over three years (p.3) against "Rs. 15 crores repeated every quarter, so yearly... Rs. 60 crores" (p.5). Not used for any verdict.
- NETWEB Q1 FY27 transcript corrects pipeline from "INR10,401 million" to "INR104,100 million" on the call (p.4). The corrected figure is used.
- NETWEB Q1 FY27 (p.17): prior-period balance sheet restated for an inventory valuation change. Prior-quarter days in this report are as stated on each earlier call, not restated.

```yaml
stage: B06-peers
company: "ESCONET"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
input_gaps:
  - "BSE scrip code not found on screener page; announcements/ empty. REPAIRED by /step1: 33 NSE Reg 30 filings Sep 2025 to Sep 2026; filings before Sep 2025 not collected."
  - "shareholding/ empty (no automated source). REPAIRED by /step1: NSE SHP XBRL Mar-2026 and Jun-2026 plus text extracts."
  - "screener export sheets EMPTY (P&L, Quarters, Balance Sheet, Cash Flow, Customization); Data_Sheet.csv populated; screener history FY2023-FY2026 plus Q1 FY27 only."
  - "no results PDFs from screener. REPAIRED by /step1: H1 FY26, FY26 audited, Q1 FY27 board outcomes."
  - "no rating PDF. REPAIRED by /step1: CRISIL rationale 2026-07-02 as text; 2024 and 2025 rationales not collected."
  - "only 2 concalls. OVERRIDDEN by /step1: concalls_available true on 2 transcripts (Jun 2025, Aug 2026); 22 Jun 2026 investor meet has deck but no transcript; no H1 FY26 call."
  - "annual-report: FY2023-24 AR not collected (two-most-recent rule); prospectus covers pre-IPO years."
  - "research/ empty, no broker notes."
  - "prospectus: final prospectus held; near-identical RHP moved to inputs/other/."
  - "announcements: SAST disclosure 2026-05-19 scanned; .txt corrupt, OCR failed; read PDF page directly."
  - "shareholding and rating XBRL/HTML originals kept beside text extracts, committed by hand by /step1."
  - "listed_date: exact NSE Emerge listing date NOT FOUND in corpus (AR Note 1 p.105 says 23 Feb 2024; prospectus dated 2024-02-20)."
  - "EMPTY-FOLDER CONFIRMATION suppressed by /step1 AUTONOMY CONTRACT; standing answer proceed with gaps. Empty at stage 0: research/."
  - "pass1 gap: FY24 AR not read, so FY24 purchases and FY24 payable days NOT FOUND; FY24 receivable days taken from FY25 AR comparatives."
  - "pass1 gap: consolidated ageing tables (Notes 2.13.1 and 2.6.1 cited on p.142 and p.140) NOT FOUND IN DOCUMENT."
  - "pass2 gap: Fluidech acquisition-date balance sheet and purchase agreement NOT FOUND; goodwill working, consolidation method and swap/cash price valuation basis NOT FOUND."
  - "pass2 gap: Zeacloud and Singapore stand-alone accounts not in corpus (Singapore audited by other auditors, FY26 AR p.127); Singapore total assets conflict: AOC-1 SGD 33,89,867 (about 2,465 Lakhs at 72.72) vs auditor 553.64 Lakhs."
  - "pass2 gap: preferential issue allottee list, lender list for the 247.95 repayment object, OD facility rate/limit/covenants, FDR lien and maturities, advance tax paid in FY26: all NOT FOUND."
  - "pass2 note: FY25 AR and the Reg 30 filing of 28 Feb 2026 were read for cross-reference only; no figure from them enters the Pass 1 base."
  - "stage3: Q1 FY27 other income split and the accounting of the 184.23 Lakhs warrant forfeiture NOT FOUND in the results filings read (note says only interest income, gain on sale of PPE and miscellaneous income)."
  - "stage3: Fluidech s.156 income tax demand of 235.16 Lakhs (AY 2021-22, per prospectus) current status NOT FOUND; not in FY26 AR."
  - "stage3: per-director Board and committee attendance NOT FOUND (extract lost the Present markers); other directorships NOT FOUND."
  - "stage3: HexaData, services, cloud and cybersecurity revenue and margin NOT FOUND; FY26 customer concentration NOT FOUND; order book value NOT FOUND."
  - "stage3: NSE PDF vs XBRL EPS discrepancy not verifiable from the AR; one EPS mismatch between filings found (standalone FY25 basic 5.26 vs 5.43)."
  - "stage5: only two transcripts exist (19 Jun 2025 FY25 call; 13 Aug 2026 Q1 FY27 call). No H1 FY26 call. The 22 Jun 2026 FY26 investor meet has a deck only; deck claims are labelled deck, not transcript. Trailing-four-quarter delivery test therefore rests on one forward call (Jun 2025) and the filed record, not on a quarterly call chain."
  - "stage5: Q1 FY27 results carry no balance sheet and no cash flow statement; the 20.2 debtor-day claim in the step1 brief is in neither transcript nor the Q1 filing text read. NOT FOUND; cannot be tested."
  - "stage5: CFO statement of operating cash flow as '5% of revenue' is garbled in the transcript (base and period unclear); no cash flow statement filed for Q1. NOT FOUND."
  - "stage5: Singapore revenue 'approximately 53 crores' (AUG26 p.15) has no stated period; Q1 or FY26 ambiguous. NOT FOUND."
  - "stage5: Fluidech FY25 and FY26 segment revenue comes from B03 (AR26 p.69), not from a call; HexaData versus non-HexaData split NOT DISCLOSED on the Aug 2026 call (single AS-17 segment)."
  - "stage6: all 12 peer transcripts present; none missing. No peer mentions Esconet, HexaData, ZeaCloud, Fluidech or MeitY."
  - "stage6: no peer reports gross margin as a level (NETWEB, RPTECH gross margin NOT FOUND); ORIENTTECH debtor days, inventory days and cash flow NOT FOUND; PSU receivable days NOT FOUND in any peer; cyber and sovereign cloud growth rates NOT FOUND in any peer."
  - "stage6: peer_questions answered on 3 peers only; Esconet's 20.2 debtor days remains NOT FOUND and sits below the lowest peer (RPTECH 41 days)."
flags:
  - {type: FLAG-PEER-SPLIT-MARGIN-MECHANISM, reason: "Esconet credits price volatility and stock for Q1 FY27 margin. NETWEB denies any memory-price gain (Q1 FY27 p.8, p.13); ORIENTTECH attributes its Q4 FY26 3.19% to Q1 FY27 7.57% EBITDA rebound to pass-through repricing after fixed-price rate contracts ended 31 Mar 2026 (Q3 FY26 p.4-5; Q1 FY27 p.4, p.6); only RPTECH allows a stock gain 'to some extent' and refused to size it (Q3 FY26 p.12, p.16). Stock-gain reading has the weakest peer support."}
  - {type: FLAG-NO-PEER-GROSS-MARGIN-BENCHMARK, reason: "No peer states a gross margin level. Esconet standalone 29.2% gross cannot be benchmarked. EBITDA ladder: RPTECH 3.38% (Q1 FY27 p.5, Cr basis), ORIENTTECH 7.57% (Q1 FY27 p.6), NETWEB 14.7% (Q1 FY27 p.5, INR mn basis). Esconet standalone 12.75% and consolidated 7.03% ex other income (B05) sit at the Netweb band and the Orient level."}
  - {type: FLAG-NETWEB-AI-MIX-LOWER-MARGIN, reason: "The one large-AI peer says strategic AI orders carry 150 to 200 bp lower PBT margin than its base (NETWEB Q2 FY26 p.7; Q3 FY26 p.9). Does not support a higher margin for AI/GPU mix over legacy at the large-order end."}
  - {type: FLAG-PEER-SCALE-MISMATCH, reason: "No peer is a small-cap GPU-server integrator. NETWEB revenue INR 21,836 mn FY26 with 125 R&D staff and a refusal to run cloud; RPTECH is a distributor; ORIENTTECH has no own-brand GPU line. Weight as ladder rungs."}
  - {type: FLAG-ESCONET-DISCLOSURE-GAP-VS-PEERS, reason: "NETWEB and ORIENTTECH disclose order book; NETWEB and RPTECH disclose receivable and inventory days and operating cash flow. Esconet's missing order book, cash flow and 20.2 debtor days are a disclosure choice, not an industry norm."}
  - {type: FLAG-CLOUD-ASSET-HEAVY-LONE-EXPANDER, reason: "Esconet is a lone expander into asset-heavy cloud. NETWEB refuses cloud services (Q2 FY26 p.16). ORIENTTECH SOC build shows capex first, revenue dates moving (Q1 FY26 p.6-7; Q2 FY26 p.5, p.9; Q3 FY26 p.8; Q1 FY27 p.10). Pattern evidence only; no peer data on MeitY."}
  - {type: FLAG-PEER-TRANSCRIPT-INCONSISTENCY, reason: "RPTECH Q1 FY27 gives EBITDA INR 155 Cr, +50% (p.4) and INR 173 Cr, +55%, 3.38% (p.5). ORIENTTECH Q3 FY26 gives the Digital India Corporation contract as about INR 15 Cr (p.3) and INR 15 Cr per quarter (p.5). CFO figures used for RPTECH; Orient contract not used."}
peers_provided: 12
verified:
  - {claim: "Q7 Customer AI and data-centre capex accelerating; partner-status vendors keep GPU and component allocation; no cancellations; constraints in memory, storage, lead time", peers: ["NETWEB", "RPTECH"], anchor_count: 8}
partially_verified:
  - {claim: "Q1 Hardware price inflation as inventory gain versus cost shock; peer stock gain; run-through to FY28 (cost shock confirmed at ORIENTTECH, stock gain only RPTECH 'to some extent', NETWEB denies, no peer sizes a gain, FY28 only via RPTECH citing third parties)", peers: ["ORIENTTECH", "RPTECH", "NETWEB"]}
  - {claim: "Q2 Gross margin on AI/GPU mix versus legacy SI; peer gross and EBITDA margins (EBITDA ladder 3.38% / 7.57% / 14.7% confirmed; no peer gross margin; AI mix lower margin at large-order end)", peers: ["NETWEB", "RPTECH", "ORIENTTECH"]}
  - {claim: "Q3 Peer debtor days, inventory days, OCF to PAT, order book (collection range 41 to 78 days and short order cycle confirmed; peers disclose order book and cash flow; Esconet 20.2 days untestable)", peers: ["NETWEB", "RPTECH", "ORIENTTECH"]}
  - {claim: "Q4 Government/PSU share and sovereign demand (Netweb 40 to 50% government, sovereign driver confirmed; Orient 12 to 20%; PSU receivable days not given by any peer)", peers: ["NETWEB", "ORIENTTECH"]}
  - {claim: "Q5 Industry growth rates for AI, sovereign cloud, cyber (Netweb 38% AI CAGR; Orient data centre 30 to 35% and cloud 22 to 28% via analyst quoting CRISIL; no sovereign cloud or cyber rate)", peers: ["NETWEB", "ORIENTTECH", "RPTECH"]}
contradicted: []
unverifiable:
  - {claim: "Q6 Market share gain in Indian server OEM against Cisco, HP, Lenovo, Dell", peers_checked: ["NETWEB", "ORIENTTECH"]}
  - {claim: "Q8 MeitY empanelment timelines, sovereign cloud ramp and asset intensity (no peer mentions MeitY; Orient Q1 FY26 p.10 adverse on sovereign platform adoption, adjacent only)", peers_checked: ["ORIENTTECH", "NETWEB"]}
peer_coverage_map:
  - {peer: "NETWEB", quarter: "Q2 FY26 (3 Nov 2025)", usage: "SUBSTANTIVE", contribution: "Strategic AI orders 150 to 200 bp lower PBT margin; cash cycle 120 days; LC-backed orders; refuses cloud services"}
  - {peer: "NETWEB", quarter: "Q3 FY26 (19 Jan 2026)", usage: "SUBSTANTIVE", contribution: "9M operating cash flow INR 134 Cr vs PAT; memory pricing aligned at order date; on-prem AI leg not started"}
  - {peer: "NETWEB", quarter: "Q4 FY26 (4 May 2026)", usage: "SUBSTANTIVE", contribution: "FY26 operating cash flow INR 1,715 mn; 13 to 14% EBITDA guide; declined to link inventory to margin; 50/50 govt mix"}
  - {peer: "NETWEB", quarter: "Q1 FY27 (29 Jul 2026)", usage: "SUBSTANTIVE", contribution: "Denies memory-price margin gain; 78 receivable and 110 inventory days; order book INR 25,069 mn; 38% AI CAGR"}
  - {peer: "RPTECH", quarter: "Q2 FY26 (10 Nov 2025)", usage: "SUBSTANTIVE", contribution: "Working-capital days; Yotta receivable INR 280 Cr delay; shortage named as risk"}
  - {peer: "RPTECH", quarter: "Q3 FY26 (4 Feb 2026)", usage: "SUBSTANTIVE", contribution: "Price helped bottom line 'to some extent'; refused inventory-gain number; supplier price validity of weeks"}
  - {peer: "RPTECH", quarter: "Q4 FY26 (15 May 2026)", usage: "SUBSTANTIVE", contribution: "FY26 operating cash flow INR 514 Cr vs PAT INR 282 Cr; margins intact; AI funnel INR 20,000 to 25,000 Cr"}
  - {peer: "RPTECH", quarter: "Q1 FY27 (5 Aug 2026)", usage: "SUBSTANTIVE", contribution: "EBITDA 3.38%; channel stock bought at 80 sold near 100; price-rise speed to halve; allocation orange alert"}
  - {peer: "ORIENTTECH", quarter: "Q1 FY26 (14 Aug 2025)", usage: "SUBSTANTIVE", contribution: "SI margin ladder 8 to 10% and 15 to 20%; sovereign platform adoption weak; AI not in revenue"}
  - {peer: "ORIENTTECH", quarter: "Q2 FY26 (14 Nov 2025)", usage: "CITED-ONLY", contribution: "AI still proof-of-concept; SOC revenue date moved (repeated in other Orient calls)"}
  - {peer: "ORIENTTECH", quarter: "Q3 FY26 (19 Feb 2026)", usage: "SUBSTANTIVE", contribution: "Fixed-price rate contracts to 31 Mar 2026; customer moved to OEM-direct; shortage through FY27"}
  - {peer: "ORIENTTECH", quarter: "Q1 FY27 (13 Aug 2026)", usage: "SUBSTANTIVE", contribution: "EBITDA 3.19% to 7.57% via pass-through; order book INR 375.43 Cr; delivery-penalty refusal"}
industry_cross_read:
  demand: "Split: compute hardware peers boom (Netweb +172.1% YoY, RPTECH +62%) while the services SI is flat (Orient Q1 FY27 INR 201.92 Cr vs INR 212.56 Cr, derived -5%); Esconet standalone looks like the SI pattern."
  pricing_inputs: "Memory, storage, CPU prices up (RAM 2x to 3x); no easing seen for about a year; margin effect splits by contract-pricing architecture: markup distributor up in rupees, own-brand OEM in band, fixed-price SI shock then rebound."
  capex_cycle: "No peer expands capacity; working capital is the constraint (Netweb INR 1,200 Cr enabling resolution, RPTECH leverage to 2x on projects). Esconet is a lone expander into asset-heavy cloud, not a capacity race."
peer_mentions_of_company: []
risks_peers_raise:
  - "Customer disintermediated by OEM-direct sale (ORIENTTECH Q3 FY26 p.6)"
  - "Fixed-price rate contracts against rising input cost (ORIENTTECH Q3 FY26 p.4-5)"
  - "Delivery-penalty terms on 16 to 18 week lead times (ORIENTTECH Q1 FY27 p.13)"
  - "Component shortage tracked weekly; supplier price validity of weeks (RPTECH Q1 FY27 p.9; Q3 FY26 p.16)"
  - "Supplier product-line exit, Micron Crucial (RPTECH Q3 FY26 p.12)"
  - "Consumer affordability and unit decline of 5 to 10% (RPTECH Q4 FY26 p.14)"
  - "Channel stock build (RPTECH Q1 FY27 p.10, p.15)"
  - "Large-order receivable delay, Yotta INR 280 Cr (RPTECH Q2 FY26 p.15)"
  - "Growth working-capital funding and quarter-end short-term borrowing (NETWEB Q4 FY26 p.16-17; Q1 FY27 p.14-15)"
  - "Contingent liabilities: GST notices (RPTECH Q1 FY27 p.16-17); INR 4.4 Cr AWS reversal (ORIENTTECH Q1 FY27 p.10)"
  - "GPU substitutes ASIC/TPU and Chinese open models (NETWEB Q3 FY26 p.9-10; Q1 FY27 p.11)"
  - "Inventory valuation policy change restating prior period (NETWEB Q1 FY27 p.17)"
net_narrative_effect: "complicates"
cross_peer_hypothesis: "In this memory-price cycle, margin outcome splits on contract-repricing lag, not on business model. Fixed-price books (Orient to 31 Mar 2026; Esconet FY26 per B05) took a FY26 H2 shock; captive-supply and markup peers (Netweb, RPTECH) held margin. Orient's 3.19% to 7.57% rebound (Q1 FY27 p.6) and Esconet's Q1 FY27 jump are then a one-time reset as contracts reprice, not expansion. Test: with price-rise speed halving (RPTECH Q1 FY27 p.11) and Orient pricing stable (Q1 FY27 p.4), Orient and Esconet Q2 FY27 margins should hold or fall toward the repriced level while Netweb and RPTECH stay in band. Any Esconet gross margin above that level needs pre-rise stock, which fades as stock turns. [INFERENCE]"
analyst_note: "Three readings of the Q1 FY27 margin now exist. A: structural HexaData mix (B05 reading A). B: stock gain plus other income (B05 reading B). C: fixed-price contracts rolling onto new prices, as at Orient. Peers give B the weakest support: Netweb denies it, RPTECH will not size it, Esconet's own inventory build is small (518.50 Lakhs). Separating observation: Q2 FY27 standalone gross margin and the share of Q2 revenue billed on orders priced before the rise. No peer reports gross margin, so 29.2% stays unbenchmarked; on EBITDA ex other income Esconet standalone 12.75% sits in Netweb's 13 to 14% band and consolidated 7.03% sits at Orient's 7.57%. Stage 6 does not test the Esconet corpus again; Esconet inputs are B05 figures. Zero formal contradictions; read the verdict count with the peer-split flag, not instead of it."
```
