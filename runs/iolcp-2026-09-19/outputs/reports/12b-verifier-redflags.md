# STAGE 12 VERIFIER B: CONCALL RED-FLAG AUDIT (B12b), IOLCP
Run date: 2026-09-19 | Phase 1 | Model: claude-opus-5 | Fresh context

Inputs read:
- Company transcripts, read in full: Concall_Feb_2026 (Q3 FY26, call 12-Feb-2026), Concall_May_2026
  (Q4 FY26, call 22-May-2026), Concall_Aug_2026 (Q1 FY27, call 13-Aug-2026), Concall_Sep_2026
  (business update call, 11-Sep-2026).
- Peer transcripts (12: AARTIDRUGS x4, GRANULES x4, LXCHEM x4). Read by targeted search on the
  topics where a peer can contradict IOL: ibuprofen, paracetamol pricing, acetyls spread,
  DCDA/metformin, Solara/SMS, IOL. Passages were read in context where a hit bore on IOL.
  Per-peer coverage belongs to Verifier D. This audit did not re-read every peer page.
- B05 report (05-concall.md) and B06 report (06-peers.md).

Anchor convention. "p.N" is the printed page label inside the transcript ("Page N of M"). The
.txt `[page K]` marker equals printed page N+1, because the cover letter is marker 1.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from the raw transcripts, before reading B05/B06 conclusions)

Severity is graded by the Verifier scale. The status column was filled in after the comparison
in Part 2.

| # | Sev | Item | Anchors (call, speaker, page) | Status |
|---|---|---|---|---|
| 1 | CRITICAL | **Inventory-gain handling: a dodge, then a denial, then a reversal across three calls.** Feb: the analyst asks for the value of the inventory markdown. The CFO answers with total inventory ("around INR350 crores"), not the markdown. May: an analyst asks directly whether the Q4 gross-margin jump was an inventory gain. Abhay: "I don't think that we were having any meaningful inventory gain in that quarter". Aug: Abhay concedes "we might be having little bit inventory gain during the later part of the last quarter around 10 to 15 days". Mahajan confirms: "Yes... in the March quarter... for few days we get the inventory valuation benefit". The Q4 FY26 15.2% margin was partly the valuation gain that management denied in May. | Feb p.13 (Hemant; Khanna; Rana "API inventory has been gone down"); May p.4 (Jainam Ghelani; Abhay); Aug p.7 (Jainam; Abhay); Aug p.9 (Maulik Varia; Mahajan) | PARTIALLY CAUGHT. B05 3C records the Aug exchange as "Explicit denial both times... consistent, specific denial". The transcript shows an admission that reverses the May denial. |
| 2 | CRITICAL | **The R&D and new-product pipeline goes unanswered in three straight quarters.** Feb: "as and when... we will let you know" (twice). No names, no timelines. May: "the R&D is basically relating to the process, it's not the product development R&D". Then "a very great pipeline, but normally, we announce the product when we decide". Asked "any exciting products this year?", the answer is "I think we can expect." Aug: asked what commercial opportunities come from the Rs26 Cr R&D spend, management answers "not allocated to any specific development of any product" and lists XRD/LCMS/GCMS purchases. Backward-integration KSMs and CMO both get the reply "once we have proof of concept". All 3 patents are non-commercial (Feb). The benign reading is that Indian API makers routinely withhold pipeline names. The separating observation: does any call ever name a product before its capex is filed? None did in the four calls (Sep's three projects surfaced only at the Reg 30 filing). | Feb p.12 (Hemant; Rana, Abhay); Feb p.13-14 (Vruddhi Vora; Rana); Feb p.12 (patents; Rana); May p.11 (Sachin Kasera; Abhay); Aug p.7 (Santosh; Abhay, Rana); Aug p.11 (Nimish Verma; Rana); Aug p.12 (Shaikh Mohammed; Rana) | MISSED. B05 logs the patent drop (dropped_triggers) and R&D spend. It never logs the pipeline question as a repeated evasion. 2E has only price/volume, competitor assets and greenfield. |
| 3 | MAJOR | **CDMO formulations: an earlier denial, then an evasive reply four weeks before an EU-GMP facility was disclosed.** Feb: forward integration is "not the formulations, but CMO model... CMO for API only". Aug 13: asked about the CMO opportunity, Rana says "once we have very clear cut proof-of-concept ready with us, definitely, we'll let you know". Sep 11: "we have established a new CDMO facility... 1,500 million tablets... received the EU GMP certification". Also: "Around 30% of overall funding requirements has already been incurred". An EU-GMP-certified tablet plant does not go from proof of concept to certification in four weeks. The facility existed or was near completion at the Aug call. | Feb p.7 (Surabhi; Abhay); Aug p.12 (Shaikh Mohammed; Rana); Sep p.2 (Abhay opening); Sep p.3 (Abhay) | PARTIALLY CAUGHT. B05 1C names the Feb-to-Sep pivot and gives the generous and the sceptical reading. It misses the Aug "proof-of-concept" answer and keeps the item out of 4D red flags and the credibility grade. |
| 4 | MAJOR | **Margin drivers explained three different ways to different analysts on one call (Aug).** Khanna: "also some improvements in the finished product prices". Later: "higher volumes along with better pricing of our established products... passing the increased cost to customers". Abhay: "better product mix". Mahajan: "there is no major product mix change... not primarily through the external factors". | Aug p.5 (Pahel Sharma; Khanna); Aug p.7 (Jainam; Abhay); Aug p.8 (Soumya; Mahajan); Aug p.9 (Maulik Varia; Khanna) | PARTIALLY CAUGHT. B05 2E logs the price/volume split as "deflected every time". It does not log that the speakers contradict each other. |
| 5 | MAJOR | **Acetyls spread: two versions given to two analysts on the May call.** Mahajan to Sachin Kasera, asked whether ethyl acetate margins in April-May run much better than in the March quarter: "It is absolutely correct." Abhay to Vignesh Iyer: "the spread, I think, is more or less same, or might be a little bit increased... the spread is not much." LXCHEM's call on the same product puts the April spread at about $250, against about $130 in Jan-Feb (LXCHEM May p.7, Rajan Venkatesh). The peer backs Mahajan's version. Abhay understated a price-driven gain that the same call attributes to "efficiency". | May p.7 (Sachin Kasera; Mahajan); May p.9 (Vignesh Iyer; Abhay); LXCHEM-Concall_May_2026 p.7 | MISSED. B05 3B treats the spread as a consistent management claim. |
| 6 | MAJOR | **Ibuprofen pressure is flatly denied, and a new competitor is conceded in passing.** Feb: "we are not facing any problem... any surplus", then "we are not facing any such situation, which you have heard from other peers". May: "No, not at all". In the same May call, Mahajan explains the earlier weak demand as "overstocking... in 2023 and 2024... and entrance of new product -- new peer also in the market". Sep: capacity goes up 50% (12,000 to 18,000 MTPA) against a 3-4% market growth rate. Rana declines to say how much of it has customer backing: "we would not be in a position to share you the correct number". | Feb p.4 (Jay; Mahajan); Feb p.13 (Hemant; Mahajan); May p.6 (Maulik Varia; Mahajan); May p.8 (Sachin Kasera; Abhay); Sep p.10 (Suhani Singh; Rana) | PARTIALLY CAUGHT. B05 3C logs the denial as "asserted, not proven", and 3B/1C log the overstocking claim and the undisclosed customers. The new-entrant admission and its tension with the denials are not logged. |
| 7 | MAJOR | **Paracetamol, the lead non-ibu driver, was sold on price to fill capacity.** Feb: pharma EBIT fell 10.5% to 9.7% because of "the prices of paracetamol and underutilization of para capacity... around 60%". Khanna: "we are focusing mainly on volume... in future, we will be focusing on the pricing also". The analyst's "offered slight more lower pricing... to increase the volume?" goes unrefuted. Utilisation then prints 55% in Q4 FY26 and 55% in Q1 FY27. Granules independently reports "some amount of price erosion also in paracetamol" in the same quarter. Aug names paracetamol as the main contributor to the non-ibu rise. | Feb p.9 (Maulik; Mahajan, Khanna); May p.12 (Abhay, 55%); Aug p.4 (Abhay, 55%); Aug p.10 (Khanna); GRANULES-Concall_Jan_2026 p.12 (Priyanka Chigurupati) | MISSED. B05 1C covers only the 60%/55% basis change. |
| 8 | MAJOR | **Guidance numbers are not the "near-verbatim" repetition B05 scores.** May, one call: Khanna says "15% growth in top line... 1%, 2% more or less... EBITDA margin... 14%". Abhay says "Around 16% to 18%", then "mid to high-teen", then "mid-teen" to a later analyst, and "14% to 14.5%". Aug: formal 15-20% / 14-15%, then Khanna "around 20%". Khanna's FY28 "15% to 20%... EBITDA to 15% to 17%" is disowned in the next breath: "Actually, we cannot predict for '28 at this time". Abhay adds: "Suppose... in next six-month scenario got changed, then what we are saying may not be possible." | May p.5 (Jainam; Abhay, Khanna); May p.6 (Maulik Varia; Abhay); May p.15 (Ruchi; Abhay); Aug p.4 (Khanna); Aug p.9 (Maulik Varia; Khanna, Abhay) | PARTIALLY CAUGHT. B05 flags Abhay's "16-18%" as unreconciled. It enters FY28 15-20% / 15-17% into the guidance table and YAML without the disclaimer, and rates Consistency 4/5. |
| 9 | MAJOR | **Greenfield site: timeline and product never firm.** The Rs1,200-1,400 Cr, 4-5 year programme has had no product named and no firm commissioning date across four touchpoints. | Feb p.7 (Varun Mishra; Rana); May p.4, p.11 (Jainam, Sachin Kasera; Abhay); Aug p.11 (Nimish Verma; Rana, Abhay); Sep p.8 (Maulik; Abhay) | CAUGHT (B05 FLAG-CAPEX, 2E). The "MISSED" promise row is wrong in direction (see Part 3). |
| 10 | MAJOR | **FY26 margin guidance walked down live (14-15% to 13% to 11-12%), and the H2 13-14% target was missed.** | Feb p.4 (Jainam; Khanna); Feb p.11 (Shaikh Mohammad Ayaz; Abhay) | CAUGHT |
| 11 | MAJOR | **Capex keeps rising while "entirely internal accruals" is asserted each time.** Greenfield runs Rs200-250 Cr/yr. Sep adds Rs495 Cr over FY27-28 at the existing site, separate from the greenfield. FY26 PAT was Rs138 Cr. | May p.3 (Khanna); May p.4 (Abhay); Sep p.3 (Abhay); Sep p.11 (Khanna); Sep p.13 (Abhay, "It's different") | CAUGHT (B05 FLAG-CASH, 3C) |
| 12 | MAJOR | **A peer contradicts IOL on paracetamol price.** IOL says prices rose "across all the products, chemicals and API... in India and also outside". Granules, asked about paracetamol and metformin pricing, says: "Definitely, there were no price increases we wish we had". | May p.16 (Sheikh Mohammad; Abhay); GRANULES-Concall_May_2026 p.7 (K.P. Chigurupati; call dated 29-Apr-2026) | CAUGHT (B06 Q4, FLAG-PRICING) |
| 13 | MAJOR | **Asset turn on the Rs350 Cr ibuprofen capex walked down within the call.** "It's about 1.75x", then "1.75x to 2x", then "1.5x to 1.75x... this is not the firm number you can take from here". The peak-revenue range therefore runs about Rs525-700 Cr, not the Rs600-620 Cr the analyst took. | Sep p.3 (Disha; Abhay); Sep p.12 (Rishabh Malik; Abhay) | PARTIALLY CAUGHT. B05 records "~1.75-2.0x" only. |
| 14 | MINOR | Sep, one call: ibuprofen feedstock effect "neutralised for us". Later, when an analyst asks "we are looking at a probable margin expansion?", Abhay answers "Yes, that's correct". | Sep p.7 (Subrata Sarkar; Abhay); Sep p.13 (Rishabh Malik; Abhay) | MISSED |
| 15 | MINOR | Minoxidil: the plant was "announced... by the end of the December" and slipped. Final API was re-promised "by the first quarter of next financial year". | Feb p.7-8 (Varun Mishra; Abhay) | PARTIALLY CAUGHT. B05 promise row 5 scores it "DELIVERED (early)" and omits the Dec slip. |
| 16 | MINOR | FY26 capex was trimmed to Rs130-135 Cr in Feb. The actual came in at Rs160 Cr, an overshoot. | Feb p.7 (Abhay); May p.3 (Khanna) | PARTIALLY CAUGHT. B05 row 4 says "DELIVERED". |
| 17 | MINOR | The non-ibu export share figures drift. Feb: "15% to 17%", "around 15% coming from regulated market". May: "around 20% export share". Aug: "around 21% to 20%... not having the exact bifurcations of regulated and non-regulated". | Feb p.6 (Surabhi; Abhay); May p.11 (Sachin Kasera; Abhay); Aug p.6 (Surabhi Sutaria; Abhay) | MISSED |
| 18 | MINOR | Pass-through claims conflict. Aug: margins "impacted due to... passing the increased cost... because we already tied up some prices to big customers". Sep: "in every contract, we have a clause of price adjustment". | Aug p.9-10 (Maulik Varia; Mahajan); Sep p.10 (Shaikh Mohd Ayaz; Abhay) | MISSED |
| 19 | MINOR | Asked for a US FDA inspection update, management says "not necessary for U.S. FDA to visit us". No recent inspection is stated. | May p.16 (Maulik Varia; Abhay) | CAUGHT (B05 3B, unverifiable) |
| 20 | MINOR | No promoter, MD or CEO speaks on any of the four calls. The spokesperson is the Company Secretary. | All four calls, management lists p.1 | CAUGHT (B05 header) |
| 21 | MINOR | Chemicals utilisation stated as "near 200%". | Feb p.6 (Maulik; Khanna) | CAUGHT |
| 22 | MINOR | The company-level ROCE target after all projects is "more about 15%". B05 transcribes it as ">15%", a slight upward drift. | Sep p.10 (Suhani Singh; Mahajan) | PARTIALLY CAUGHT |
| 23 | MINOR | Solara ibuprofen asset question: "No comments there." | May p.13 (Kenil; Abhay) | CAUGHT |
| 24 | MINOR | Triacetin is called "recent commissioning" on 22-May. In Aug: "we have started production in May -- after May... only 1 month of production". | May p.3 (Abhay); Aug p.13 (Rana) | MISSED |

Totals: 24 items. Material: 13 (2 CRITICAL, 11 MAJOR). Minor: 11.

---

## PART 2: COMPARISON AGAINST THE PIPELINE

### 2A My items versus the pipeline

| Status | Material (C+M) | Minor | All |
|---|---|---|---|
| CAUGHT | 4 (#9, #10, #11, #12) | 4 (#19, #20, #21, #23) | 8 |
| PARTIALLY CAUGHT | 6 (#1, #3, #4, #6, #8, #13) | 3 (#15, #16, #22) | 9 |
| MISSED | 3 (#2, #5, #7) | 4 (#14, #17, #18, #24) | 7 |

### 2B Pipeline flags I did not raise independently, or that make a factual claim

| Pipeline claim | Location | Assessment | Basis |
|---|---|---|---|
| Silence on promoter shareholding, Vasudeva stake, RPT purchases | B05 4D row 2, FLAG-GOVERNANCE | SUPPORTED | No mention in any of the four transcripts. B05 is correct that the silence is two-sided. |
| "Internally funded" claim untested against receivables | B05 4D row 3, FLAG-CASH | SUPPORTED | No debtor or WC discussion in any call. |
| Tolling unit built on one unnamed customer | B05 4D row 6 | SUPPORTED on the single customer ("one of our renowned customer", Sep p.6; "a leading global chemical company", Sep p.2). The "confidentiality obligations" wording is not in the transcript. It may come from the Reg 30 filing, which this audit did not check. | |
| **Inventory-gain question in Q1 FY27: "Explicit denial both times... consistent, specific denial"** | B05 3C row 3 | **NOT SUPPORTED** | Aug p.7 (Abhay): "we might be having little bit inventory gain during the later part of the last quarter". Aug p.9 (Mahajan): "Yes... in the March quarter... we get the inventory valuation benefit". The Aug call admits the Q4 gain that May denied. B05 turned the signal around. |
| **Ethyl acetate spread "spiked to $200+... stabilised to $150-160... management cites specific dollar figures across three calls consistently... 'neutralised' by Sep 2026"** | B05 3B bullet 4; carried into B05 peer_questions Q3 | **NOT SUPPORTED** | The dollar figures are the analyst's premise (May p.7, Sachin Kasera: "$110, $120... $200 plus... $150, $160"). No IOL manager states a dollar spread on any call. Mahajan answers with capacity (110,000 to 120,000 T) and "a little bit" of margin. "Neutralised" is Abhay on ibuprofen feedstock after the Middle East shock (Sep p.7), not on acetyls. Aug p.4 (Mahajan) says only that the ethyl acetate delta "will remain constant". |
| **B06 contradiction: "Acetyls spread pressure was 'neutralised' by Sep 2026", contradicted by LXCHEM** | B06 Q3, FLAG-SPREAD, contradicted[1] | **NOT SUPPORTED** | Built on the misattribution above: IOL made no such acetyls claim. Also, LXCHEM-Concall_Aug_2026 is dated 30-Jul-2026, before IOL's 13-Aug call, not after as B06 states. Its "higher than an average 12-year spread" refers to March and April (p.7), not to the current quarter. On Q2 it says "too early to say". B06 Part 4's count of "2 contradicted" should read 1. |
| Granules contradicts the IOL paracetamol price claim | B06 Q4, FLAG-PRICING | SUPPORTED | GRANULES May-2026 file (call 29-Apr-2026) p.7; GRANULES Jan-2026 p.12. Correction: the Granules call date is 29-Apr-2026, not May. It still covers the Jan-Mar quarter and the start of April. |
| Greenfield promise row 6 "MISSED / SLIPPING... walked back to 'probably not in this FY'" | B05 2A row 6 | OVERSTATED | See spot check S4. |

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| # | B05 row | Earlier call contains the promise? | Later call shows the outcome? | Verdict |
|---|---|---|---|---|
| S1 | Row 1: Q4 FY26 revenue ~Rs600 Cr, DELIVERED Rs619 Cr | Yes. Feb p.11 (Khanna): "We expect INR600 crores revenue in the fourth quarter." | Yes. May p.3 (Khanna): "INR619 crores". | CONFIRMED |
| S2 | Row 2: Q4 EBITDA margin ~11%, DELIVERED 15.2% | Yes. Feb p.11 (Abhay): "approximately 11%, a little better than". | Yes. May p.3: "EBITDA margin improved by 251 basis points to 15.2%". Part of the beat was the inventory valuation gain, conceded Aug p.9 (item #1). | CONFIRMED (direction). Beat quality overstated. |
| S3 | Row 5: Minoxidil by Q1 FY27, DELIVERED early | Yes. Feb p.8: "by the first quarter of next financial year, we will be starting". The same passage admits the earlier end-December commercialisation target slipped. | Yes. May p.2: "the launch of Minoxidil". | CONFIRMED on the re-promise. B05 omits the earlier slip (item #15). |
| S4 | Row 6: Greenfield "4-6 to 6-8 quarters from May 2026", MISSED / SLIPPING | Yes. May p.4: "next six to eight quarters, or maybe four to six quarters". | No miss has occurred. 4-6 quarters from May 2026 lands in Q2-Q4 FY28, so Aug's "probably not in this FY" (Aug p.11) agrees with the promise and does not walk it back. The one dated sub-promise was May p.11: "in the next three to four months, we will be able to secure most of them". Sep p.8 (3.7 months later) says "Most of the approvals are already secured and initial base work is also started." That sub-promise was substantially delivered. | **WRONG**. Should read OPEN / NOT YET DUE. The flag "no firm commissioning date" stands. The miss does not. |
| S5 | Row 7: Paracetamol 55% to 70-75% by FY27-end, PARTIAL/PENDING | Yes. May p.6 (Mahajan) "from 55% to 75%"; May p.12 (Abhay) "70% to 75%... in FY 2027". | Aug p.4 (Abhay): "around 55%... by the end of this financial year, will be reaching to around 70%". The target is quietly trimmed from 70-75% to ~70%. | CONFIRMED (pending). Minor target trim unlogged. |

Checked 5, confirmed 4, wrong 1. Effect of S4 on B05's tally: delivered 5 / partial 4 / missed 1 becomes delivered 5 / partial 4 / open 1 / missed 0. Row 4 (capex Rs130-135 Cr guide versus Rs160 Cr actual) is better labelled an overshoot than "DELIVERED". It is not counted in the spot checks.

---

## PART 4: CREDIBILITY GRADE

B05 grades B. **I would grade lower: the B/C boundary.** The delivery record is real: Q4 revenue and margin beat, FY26 met the cut guide, Q1 FY27 ran ahead. Candor is weaker than B05 scores it. The May denial of an inventory gain was reversed in Aug. Three speakers gave three margin-driver stories on one call. Two speakers gave opposite spread answers on another. The CDMO reply of "proof of concept" came four weeks before an EU-GMP plant was announced. The product pipeline went unanswered in three quarters. B05 rates Consistency 4/5 and Transparency 4/5. On this evidence both fit 3/5 at most. Hold B only if the synthesis names these candor items as the caveat. The 4D weights key off this grade, so the operator should rule on it at Halt 1.

---

## PART 5: CONSOLIDATED FINDINGS

| Sev | Finding | Location | Fix |
|---|---|---|---|
| CRITICAL | MISSED repeated evasion (3 quarters): R&D and new-product pipeline (item #2) | B05 2E, repeated_evasions | Add a 2E row and a repeated_evasions entry. Weigh against the benign reading named in #2. |
| MAJOR | NOT SUPPORTED: inventory-gain answer read as "consistent denial". It was an admission reversing the May denial (item #1). | B05 3C row 3 | Restate as denial (May p.4) then admission (Aug p.7, p.9). Add to 4D. Mark the Q4 15.2% beat as partly valuation-driven. |
| MAJOR | NOT SUPPORTED: spread dollar figures and "neutralised" attributed to IOL management | B05 3B bullet 4; peer_questions Q3 | Re-attribute the figures to the analyst premise. "Neutralised" refers to ibuprofen feedstock. |
| MAJOR | NOT SUPPORTED: B06 "neutralised by Sep 2026" contradiction; LXCHEM Aug call date misstated | B06 Q3, FLAG-SPREAD, contradicted[1], Part 4 | Strike the second contradiction. Contradicted count becomes 1. |
| MAJOR | Promise row 6 (greenfield) direction wrong: MISSED should be OPEN / NOT YET DUE | B05 2A row 6, promise_delivery | Correct row and tally. Keep FLAG-CAPEX on the undated timeline. |
| MAJOR | MISSED: May spread answers contradict each other across analysts; LXCHEM backs the higher-spread version (item #5) | B05 2B/2C/3B | Add. It bears on whether the Q4/Q1 margins are price-led. |
| MAJOR | MISSED: paracetamol price concession for volume, corroborated by Granules (item #7) | B05 1C, 4A trigger 2 | Add to the trigger 2 kill-side evidence. |
| MAJOR | PARTIALLY CAUGHT: CDMO Feb denial and Aug "proof-of-concept" answer before the Sep EU-GMP disclosure (item #3) | B05 1C, 4D, credibility basis | Move to 4D. Cite Aug p.12. |
| MAJOR | PARTIALLY CAUGHT: ibuprofen "no pressure" denials versus the May new-entrant admission, with a 50% capacity add (item #6) | B05 3C row 2, 3B | Add the May p.6 admission beside the denials. |
| MAJOR | PARTIALLY CAUGHT: FY28 guidance entered without management's same-breath disclaimer; May FY27 numbers inconsistent (item #8) | B05 1B, guidance YAML, 2C Consistency | Tag FY28 rows "disowned same call (Aug p.9)". Lower Consistency. |
| MINOR | PARTIALLY CAUGHT: Aug inter-speaker margin-driver contradiction (item #4) | B05 2E row 1 | Note the contradiction beside the deflection. |
| MINOR | PARTIALLY CAUGHT: ibuprofen asset turn recorded as 1.75-2.0x; management's final range was 1.5-1.75x, "not the firm number" (item #13) | B05 1B, guidance YAML | Record 1.5-2.0x with the disclaimer. |
| MINOR | MISSED: Sep "neutralised" versus "margin expansion, yes" (item #14) | B05 Supplementary | Note. |
| MINOR | PARTIALLY CAUGHT: minoxidil Dec slip omitted (item #15) | B05 2A row 5 | Note the slip. |
| MINOR | PARTIALLY CAUGHT: FY26 capex overshoot labelled DELIVERED (item #16) | B05 2A row 4 | Relabel as overshoot. |
| MINOR | MISSED: non-ibu export share drift and the lost regulated split (item #17) | B05 3D | Note. |
| MINOR | MISSED: pass-through statements conflict, Aug versus Sep (item #18) | B05 2B | Note. |
| MINOR | PARTIALLY CAUGHT: ROCE "more about 15%" transcribed as ">15%" (item #22) | B05 1B, Supplementary | Correct wording. |
| MINOR | MISSED: Triacetin commissioning timing (item #24) | B05 1A | Note. |

Counts: CRITICAL 1, MAJOR 9, MINOR 9.

Acceptance basis. 13 material items listed. 4 fully CAUGHT, 6 PARTIALLY CAUGHT, 3 MISSED. `material_caught` counts CAUGHT plus PARTIALLY CAUGHT (the pipeline had the item and under-weighted or misclassified it, per rule 3), so 10 of 13 = 77%. On a strict CAUGHT-only count the rate is 4 of 13 = 31%. Both are shown so the orchestrator can apply the one its rule intends.

---

```yaml
stage: B12b
company: "IOLCP"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 24
caught: 8
partially_caught: 9
missed:
  - {severity: "CRITICAL", item: "R&D / new-product pipeline unanswered in three straight quarters; R&D stated as process-only; all 3 patents non-commercial", anchor: "Feb p.12-14 (Rana, Abhay); May p.11 (Sachin Kasera; Abhay); Aug p.7, p.11, p.12 (Santosh, Nimish Verma, Shaikh Mohammed; Abhay, Rana)"}
  - {severity: "MAJOR", item: "May call: Mahajan confirms ethyl acetate margins 'much better' Apr-May ('absolutely correct'); Abhay tells another analyst the spread is 'more or less same'; LXCHEM puts April spread ~$250 vs ~$130 Jan-Feb", anchor: "May p.7 (Mahajan); May p.9 (Abhay); LXCHEM-Concall_May_2026 p.7"}
  - {severity: "MAJOR", item: "Paracetamol sold on price to fill capacity (pharma EBIT 10.5% to 9.7%, 'focusing mainly on volume'); utilisation then flat at 55%; Granules reports paracetamol price erosion same quarter", anchor: "Feb p.9 (Mahajan, Khanna); Aug p.4 (Abhay); GRANULES-Concall_Jan_2026 p.12"}
  - {severity: "MINOR", item: "Sep: ibuprofen feedstock effect 'neutralised for us' vs 'probable margin expansion... Yes, that's correct'", anchor: "Sep p.7, p.13 (Abhay)"}
  - {severity: "MINOR", item: "Non-ibu export share drifts 15-17% to 20% to 21-20%; regulated split given in Feb, 'not having exact bifurcation' in Aug", anchor: "Feb p.6; May p.11; Aug p.6 (Abhay)"}
  - {severity: "MINOR", item: "Aug margin hit blamed on prices already tied up with big customers vs Sep 'in every contract, we have a clause of price adjustment'", anchor: "Aug p.9-10 (Mahajan); Sep p.10 (Abhay)"}
  - {severity: "MINOR", item: "Triacetin 'recent commissioning' (22-May) vs 'started production... after May'", anchor: "May p.3 (Abhay); Aug p.13 (Rana)"}
pipeline_flags_not_supported:
  - "B05 3C row 3: Q1 FY27 inventory-gain answer described as 'explicit denial both times... consistent'. Aug p.7 (Abhay) and Aug p.9 (Mahajan) admit a March-quarter inventory valuation gain, reversing the May p.4 denial. MAJOR."
  - "B05 3B / peer_questions Q3: ethyl acetate spread '$200+ to $150-160' and 'neutralised by Sep 2026' attributed to IOL management 'across three calls'. The figures are analyst Sachin Kasera's premise (May p.7); 'neutralised' is Abhay on ibuprofen feedstock (Sep p.7). MAJOR."
  - "B06 Q3 / FLAG-SPREAD / contradicted[1]: 'Acetyls spread neutralised by Sep 2026' contradicted by LXCHEM. IOL made no such claim; the LXCHEM Aug transcript is dated 30-Jul-2026 (before IOL's 13-Aug call), and its above-average spread refers to Mar/Apr. Contradicted count should be 1, not 2. MAJOR."
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "lower: B/C boundary. Delivery supports B, but the May-denied / Aug-admitted inventory gain, contradictory margin and spread answers across analysts, the CDMO 'proof-of-concept' reply 4 weeks before an EU-GMP plant, and a 3-quarter pipeline non-answer cut Consistency and Transparency to 3/5 at most; operator ruling needed at Halt 1 since 4D weights key off the grade"
findings:
  - {severity: "CRITICAL", location: "B05 2E / repeated_evasions", finding: "MISSED repeated evasion (Feb, May, Aug): R&D / new-product pipeline never answered", anchor: "Feb p.12-14; May p.11; Aug p.7, p.11, p.12"}
  - {severity: "MAJOR", location: "B05 3C row 3", finding: "NOT SUPPORTED: inventory-gain exchange read as consistent denial; transcript shows admission reversing the May denial; Q4 15.2% beat partly valuation-driven", anchor: "May p.4 (Abhay); Aug p.7 (Abhay); Aug p.9 (Mahajan)"}
  - {severity: "MAJOR", location: "B05 3B bullet 4; peer_questions Q3", finding: "NOT SUPPORTED: analyst's spread figures and ibuprofen 'neutralised' remark attributed to IOL management as an acetyls claim", anchor: "May p.7 (Sachin Kasera); Sep p.7 (Abhay); Aug p.4 (Mahajan)"}
  - {severity: "MAJOR", location: "B06 Q3, FLAG-SPREAD, Part 4", finding: "NOT SUPPORTED: second contradiction rests on a claim IOL never made; LXCHEM Aug call dated 30-Jul-2026, not after IOL's call", anchor: "LXCHEM-Concall_Aug_2026 p.7; Sep p.7"}
  - {severity: "MAJOR", location: "B05 2A row 6 / promise_delivery", finding: "Greenfield MISSED is wrong in direction: 4-6/6-8 quarter window not elapsed; 'not in this FY' agrees with it; the 3-4 month approvals sub-promise was substantially met. Should be OPEN / NOT YET DUE", anchor: "May p.4, p.11; Aug p.11; Sep p.8"}
  - {severity: "MAJOR", location: "B05 2B/2C/3B", finding: "MISSED: contradictory spread answers to two analysts on the May call; peer backs the higher-spread version", anchor: "May p.7, p.9; LXCHEM-Concall_May_2026 p.7"}
  - {severity: "MAJOR", location: "B05 1C / 4A trigger 2", finding: "MISSED: paracetamol price concession for volume, peer-corroborated", anchor: "Feb p.9; GRANULES-Concall_Jan_2026 p.12"}
  - {severity: "MAJOR", location: "B05 1C / 4D", finding: "PARTIALLY CAUGHT: CDMO formulations denied in Feb, 'proof-of-concept' answer in Aug, EU-GMP plant with ~30% funding incurred disclosed in Sep", anchor: "Feb p.7; Aug p.12; Sep p.2-3"}
  - {severity: "MAJOR", location: "B05 3C row 2 / 3B", finding: "PARTIALLY CAUGHT: ibuprofen 'no pressure' denials vs May admission of a new peer entrant, alongside 50% capacity add with unquantified customer backing", anchor: "Feb p.4, p.13; May p.6, p.8; Sep p.10"}
  - {severity: "MAJOR", location: "B05 1B / guidance YAML / 2C", finding: "PARTIALLY CAUGHT: FY28 15-20% / 15-17% entered without the same-breath 'we cannot predict for 28'; May FY27 numbers vary 15%+/-2 to 16-18% to mid-teen; Consistency 4/5 overstated", anchor: "May p.5, p.6, p.15; Aug p.9"}
  - {severity: "MINOR", location: "B05 2E row 1", finding: "PARTIALLY CAUGHT: Aug margin drivers contradict across Khanna, Abhay, Mahajan", anchor: "Aug p.5, p.7, p.8, p.9"}
  - {severity: "MINOR", location: "B05 1B / guidance YAML", finding: "PARTIALLY CAUGHT: ibuprofen asset turn walked to 1.5-1.75x, 'not the firm number'; B05 records 1.75-2.0x", anchor: "Sep p.3, p.12"}
  - {severity: "MINOR", location: "B05 Supplementary", finding: "MISSED: 'neutralised' vs 'margin expansion, yes' within Sep call", anchor: "Sep p.7, p.13"}
  - {severity: "MINOR", location: "B05 2A row 5", finding: "PARTIALLY CAUGHT: minoxidil end-Dec target slip omitted", anchor: "Feb p.7-8"}
  - {severity: "MINOR", location: "B05 2A row 4", finding: "PARTIALLY CAUGHT: FY26 capex Rs160 Cr vs Rs130-135 Cr guide labelled DELIVERED", anchor: "Feb p.7; May p.3"}
  - {severity: "MINOR", location: "B05 3D", finding: "MISSED: non-ibu export share drift", anchor: "Feb p.6; May p.11; Aug p.6"}
  - {severity: "MINOR", location: "B05 2B", finding: "MISSED: pass-through statements conflict", anchor: "Aug p.9-10; Sep p.10"}
  - {severity: "MINOR", location: "B05 1B / Supplementary", finding: "PARTIALLY CAUGHT: ROCE 'more about 15%' transcribed as '>15%'", anchor: "Sep p.10 (Mahajan)"}
  - {severity: "MINOR", location: "B05 1A", finding: "MISSED: Triacetin commissioning timing", anchor: "May p.3; Aug p.13"}
critical_count: 1
major_count: 9
minor_count: 9
material_found: 13
material_caught: 10
acceptance_rate: 77
coverage_basis: "24 items listed; 13 material (2 CRITICAL, 11 MAJOR); of those 4 CAUGHT, 6 PARTIALLY CAUGHT, 3 MISSED. material_caught counts CAUGHT + PARTIALLY CAUGHT = 10/13 = 77%; strict CAUGHT-only = 4/13 = 31%. Company transcripts read in full; peers read by targeted search on IOL-contradiction topics (per-peer coverage is Verifier D's)."
```
