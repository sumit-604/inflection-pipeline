# STAGE 12, VERIFIER B: CONCALL RED FLAGS. JLHL (Jupiter Life Line Hospitals), run 2026-11-12

Model: claude-opus-5-5 (matches .claude/agents/verifier-b-redflags.md frontmatter, effort xhigh).
Rubric: prompts/12-verifiers-pipeline.md, VERIFIER B section.

## Inputs and method

- Main company, 4 transcripts, read in full from the page-marked .txt files before I opened B05 or B06:
  Feb26 = Q3 & 9M FY26 (call 2 Feb 2026), May26 = Q4 & FY26 (18 May 2026), Aug26 = Q1 FY27 (3 Aug 2026), Oct26 = Q2 & H1 FY27 (26 Oct 2026).
- Peers, 12 transcripts (KIMS, MEDANTA, YATHARTH x4 each). Coverage statement: I did not read every peer line. I read the sections that bear on JLHL and swept all 12 files by keyword. Sections read: KIMS Thane, Mumbai and Maharashtra passages in all four KIMS calls; insurance empanelment and the GIC common-empanelment passages; onco-drug margin cap and Supreme Court passages at all three peers; leverage-comfort passages; MEDANTA Indore and Mumbai passages. Sweeps: Thane, Mumbai, Jupiter, MMR, Maharashtra, Pune, Indore, Dombivli, Nashik; Supreme Court, margin cap, trade margin, NPPA, onco; standoff, cashless, GIC, common empanelment, insurer; seasonality words; leverage words.
- Then B05 (outputs/reports/05-concall.md) and B06 (outputs/reports/06-peers.md).
- Anchor form: (call, speaker, PDF page = the "[page N]" marker, .txt line). The printed page inside a transcript is the PDF page less one.
- Scope rule. Verifier A owns whether a number exists at its anchor. I judge signals, classification and weight. Where I touch a number, I mark my own arithmetic "derived".

## Part 1. Independent red-flag list (graded before comparison)

Severity scale: CRITICAL / MAJOR / MINOR. A repeated evasion (2+ quarters) is graded CRITICAL. A single thesis-relevant item is MAJOR. Tone shifts and small points are MINOR.

### Material items (CRITICAL + MAJOR)

| ID | Sev | Type | Item | Anchors |
|---|---|---|---|---|
| I1 | CRITICAL | Repeated evasion, 4 calls | The CEO deflects every question on margin and forward economics. Feb26: consolidated ARPOB outlook "I have not really done too much modeling around it". Feb26: will costs above inflation squeeze margins against inflation-linked pricing? "we should catch up separately", then "Too much of astrology is difficult to do... I really don't have too many answers". May26: base growth above 10%? "in the current war situation, I don't want to take a guess". Aug26: "I don't model it on a unit-to-unit basis"; FY27 margin 20-21%? "you'll probably have to model it with those 2 inputs". Oct26: Supreme Court on markups, "I don't want to make comments"; 30% onco-drug margin cap, "very honestly, we have not done that modeling"; "we have never given financial guidance". Peer contrast: YATHARTH sized its onco-cap hit at "around 0.3%" of EBITDA on 4 Nov 2026. | Feb26 p.9 Ankit Thakker to Rishi Kapoor l.362-366; Feb26 p.13 to Amit Thawani l.511-518; May26 p.6 to Amey Chalke l.210-212; Aug26 p.4 to Dhvani Shah l.128; Aug26 p.5 to Dikshant Gupta l.202-205; Oct26 p.5 to Janargan l.205-212; Oct26 p.7 to Aryan Jain l.273-276; Oct26 p.11 to Janargan l.431; Oct26 p.12 to Maulik Varia l.467-468; YATHARTH Nov26 p.7 Yatharth Tyagi l.290-293 |
| I2 | CRITICAL | Repeated evasion, 3 calls | Dombivli unit economics are withheld while the loss figure is given. May26: "still very early days to talk about occupancy and numbers". Aug26: no unit-level model. Oct26: "we have not been giving unit-wise revenue numbers, so I would not have that accessible with me"; ARPOB ex-Dombivli, "I just have the blended numbers with me currently"; Dombivli payer mix, "I have a blended number". Peer contrast: KIMS gives new-unit revenue and loss on the call (Thane Q4 FY26 revenue Rs 47 Cr, loss Rs 5 Cr). | May26 p.5 to Kurpa Shah l.172-175; Aug26 p.4 l.128; Oct26 p.4 to Abin Benny l.148-149; Oct26 p.8 to Mohit Mital l.309-310; Oct26 p.12 to Mihir l.496-498; KIMS May26 p.8 Abhinay Bollineni l.285-287 |
| I3 | MAJOR | Unusual analyst insistence; dodge | The Dombivli Q2 swing does not reconcile, and four analysts pressed it in one call. Drag fell from Rs 9.5 Cr (Q1) to Rs 0.2 Cr (Q2). Fixed cost is Rs 6-7 Cr "for a month" (Aug), then Rs 6 to 8-odd Cr (Oct). Occupancy went from 25-30% to "mid-30s". Q2 ARPOB is diluted by medical mix. Derived: Q1 contribution (revenue less variable cost) = Rs 18-21 Cr fixed less Rs 9.5 Cr loss = about Rs 8.5-11.5 Cr. Q2 contribution = Rs 18-24 Cr fixed less Rs 0.2 Cr = about Rs 18-24 Cr. Contribution about doubles. Occupancy rose only about 17-40% (derived from 25-30% to 35%), at a lower ARPOB. An analyst says Dombivli revenue looked "a little flattish". Answers: "I can't answer that question"; "I wish I had a crystal ball"; "I really don't know". Two readings: (a) Q1 carried one-off launch costs; (b) Q2 costs were lower, shared or moved. Separating observation: the Q3 FY27 Dombivli drag, or any unit revenue figure. | Aug26 p.3 opening l.98; Aug26 p.4 to Dhvani Shah l.154; Aug26 p.6 to Amey Chalke l.225; Oct26 p.3 opening l.122-128; Oct26 p.4-5 to Kalkesh Jain l.169-184; Oct26 p.6 to Dhvani Shah l.246-255; Oct26 p.9 Abdulkader Puranwala l.365-372, reply p.9-10 l.373-388; Oct26 p.9 l.350-352 |
| I4 | MAJOR | Governance silence | The CFO left and no call says so. Feb26 and May26 list "Mr. Sivasis Sen, Chief Financial Officer". Aug26 and Oct26 list "Mr. Nitin Patodi, Head of Finance" and no CFO. The CEO title changes from "Joint Managing Director and CEO" to "Managing Director and CEO" without comment. In Aug the CEO twice cannot give the company's own debt: "I don't have the exact number"; "I don't know the exact number". | Feb26 p.2 l.72-77; May26 p.2 l.61-68; Aug26 p.2 l.64-71; Oct26 p.2 l.67-76; Aug26 p.8 l.317-319; Aug26 p.9 l.355 |
| I5 | MAJOR | Contradiction between calls | Pune South land was leased. In May the CEO said of every pipeline project: "we pretty much own all the real estate". In Oct he announced the board approved "the acquisition of the land currently leased for our Pune South hospital": Rs 150 Cr total, Rs 50 Cr deposit adjusted, Rs 100 Cr new cash. The landowner is not named. Construction began on the leased plot before the purchase (Feb26: excavation over, about Rs 45 Cr spent). | May26 p.4 Ankit Thakker opening l.133-136; Oct26 p.3 opening l.108-116; Feb26 p.4 to Manav Jain l.156-164 |
| I6 | MAJOR | Contradiction within one quarter | Debt timing changed in one quarter. May: "on a net basis, we are still cash positive", debt about Rs 500 Cr, cash about Rs 545 Cr. Aug: "internal accruals, the cash in hand should pretty much see us through for the next few years. And towards the end of that cycle, we may need some debt". Oct: a Rs 500 Cr term loan is secured; debt Rs 600 Cr, cash "400-plus", net debt "170-odd". Asked how the remaining Rs 400 Cr will be used: "We'll see." | May26 p.4 l.141-148; Aug26 p.8 to Abdulkader Puranwala l.297-302; Oct26 p.10 Abdulkader l.394-400; Oct26 p.11 to Janargan l.427-429 |
| I7 | MAJOR | Capital commitment ahead of a plan | BKC is a 400-bed quaternary project in a premium, non-residential location. In May the funding view was "back of the envelope" and "Detailed calculations, of course, we will do subsequently". 25% of the land was paid; the balance was due in FY27. In Oct BKC is "in the planning stage and will soon go into the regulatory clearance process". Derived: 1,700 beds x Rs 1.5 Cr = about Rs 2,550 Cr; 3x FY26 EBITDA of Rs 343.3 Cr = about Rs 1,030 Cr of debt room. | May26 p.3 l.117-121; May26 p.4 l.129-140, l.149-150; May26 p.6 to Amey Chalke l.224-235; Aug26 p.8 l.324-325; Oct26 p.3 l.119-120 |
| I8 | MAJOR | Shifting trigger; explanation conflicts | Indore. May: add the next phase "once the occupancy crosses 60% or near 60%". Aug, at about 50% occupancy: "we are getting ready for the next phase of expansion", with new doctor hires as the reason the Indore margin fell to about 12% (analyst figure). Oct: Indore revenue up about 18% with EBITDA flat; the trigger is now "mid-60s... not for the next couple of quarters". Two quarters of Indore margin pressure are explained by an expansion that keeps moving out. | May26 p.7 to Hetvi Sanghvi l.268-269; Aug26 p.3 to Dhvani Shah l.109-118; Oct26 p.6 Dhvani Shah l.223-237; Oct26 p.10 to Abdulkader l.391-393 |
| I9 | MAJOR | Timeline drift; peer contradiction | Dombivli cashless empanelment. May: "likely to happen between 6 to 12 months", tied to accreditation. Oct: "typically takes about a year. You need your NABH accreditation in place"; NABH applied, not received; GIPSA early is "a hope". Peer contradiction: KIMS says "NABH is not a prerequisite for empanelment with insurance company". KIMS "underestimated the time it takes to now get insurance empanelments". At 15 months KIMS Thane, in the same MMR market, still lacks "two, three major companies". Dombivli payer mix is "pretty much all self-paid". | May26 p.5 to Kurpa Shah l.176-179; Aug26 p.9 to Raj Mehta l.342-345; Oct26 p.9 to Ahmed Madha l.342-347; Oct26 p.12 to Maulik Varia l.483-484; KIMS Feb26 p.7 Abhinay Bollineni l.266-268; KIMS May26 p.9 l.322-341; KIMS Nov26 p.9 l.345-348 |
| I10 | MAJOR | Dismissive answer; growth source | Growth rests on price and the answer was dismissive. Feb26: asked about the first single-digit topline quarter, the CEO said "Nothing has happened. Thank you for bringing it to my notice. I have not noticed that." He then agreed that "almost entire 10% growth this quarter is from ARPOB" (ALOS 3.88 to 3.85 days). Feb26: insurer renewals are "Inflation linked". May26: FY26 ARPOB rose partly from renewals "which happened once in 2 years, so, some price increase that has kicked in after a 2-year period". The FY26 price step is biennial, so FY27 mature-unit ARPOB growth may not repeat it. | Feb26 p.8 to Amit Thawani l.294-303, l.318-321; Feb26 p.13 l.502-507; May26 p.7 to Hetvi Sanghvi l.274-277; May26 p.8 to Karan Sharma l.301-306 |
| I11 | MAJOR | Accounting change, surfaced only on a question | An analyst asked about "a change in accounting policy mainly due to the unbilled revenues" in Q2 FY26. The CEO: "it was a onetime factor because of change in policy last quarter... you saw a little higher bump in revenue because it was the first time we recognized unbilled". The size is not given. The bump sits in the FY26 base (9M FY26 total income +15.1%, FY26 +15.2%) that any historical growth cross-check uses. The CEO's "last quarter" also conflicts with the analyst's "last year in the Q2 numbers". | Aug26 p.4 Dhvani Shah and Ankit Thakker l.136-147; Feb26 p.4 l.141; May26 p.4 l.149 |
| I12 | MAJOR | Governance; partial answer | Pledge to Catalyst Trusteeship. The CEO answered after an "offline call": "not a promoter or a promoter group pledge. It is pledged by somebody else", the rise was a 5x split misreport, "to my understanding, the filing has also been corrected". The pledgor is not named. The analyst asked for the secured debt amount; it was not given. | Aug26 p.8 Janardan Sharma and Ankit Thakker l.304-319 |
| I13 | MAJOR | Peer statement against a company claim | JLHL: "high-quality supply will very easily get absorbed in Thane, Pune and Indore, even if more were to come". Peers are adding supply in JLHL markets. MEDANTA buys an 80-bed Indore hospital "under 500 meters from the existing Indore facility" and adds oncology. MEDANTA Mumbai has most approvals; piling to start. KIMS Thane runs with 75 beds not yet operational, and KIMS calls Bombay "pretty underserved" with room for "two, three players". Indore is JLHL's weakest unit at 45-58% occupancy. | Feb26 p.9 to Rishi Kapoor l.354-358; Feb26 p.10 to Ashutosh Nemani l.390-393; MEDANTA May26 p.6 l.247-251; MEDANTA Nov26 p.10 Pankaj Sahni l.405-411; KIMS Nov26 p.7 l.286; KIMS Feb26 p.17 l.679-681 |

### Minor items

| ID | Sev | Item | Anchors |
|---|---|---|---|
| I14 | MINOR | Q1 Dombivli drag Rs 9.5 Cr = Rs 3.17 Cr a month (derived), above the Rs 2-3 Cr band, called "pretty much in line with anticipation". The band's 200-bed basis was stated only when asked in Aug. | Aug26 p.3 l.98-99; Aug26 p.4 to Palkesh Jain l.156-159 |
| I15 | MINOR | Mira Road. May: "excavation to begin by the end of the year". Oct: "currently in the regulatory stage... next phase of activities before the end of this financial year". About 3 months of slip; regulatory stage in all four calls. | Feb26 p.4 l.131-132; May26 p.3 l.114-116; Oct26 p.3 l.117-119 |
| I16 | MINOR | Thane brownfield approval. May: "sometime in this financial year". Oct: "not got the clearance yet, but we remain hopeful". Not yet due. | May26 p.7 l.249-252; Oct26 p.4 l.159-161 |
| I17 | MINOR | IV fluids plant: a hospital company buys a manufacturing unit (Rs 35-40 Cr line), "not our entry into becoming a pharma company". Oct: goodwill above the Rs 3.8 Cr equity price; acquired-company debt "INR7 crores, INR8 crores or something... or INR10 crores of debt, I don't know". Seller not named. Small in rupees. | Aug26 p.6-7 to Amey Chalke l.241-255; Oct26 p.6 to Dhvani Shah l.238-245 |
| I18 | MINOR | Labour Code one-time provision Rs 6.4 Cr; Q3 FY26 PAT -18.7%. Volunteered. | Feb26 p.4 l.133-140 |
| I19 | MINOR | Volunteered negative: "much higher depreciation load" and an EBITDA drag "for around the next 2 years". Credibility-positive. | Feb26 p.3 l.121-124 |
| I20 | MINOR | Doctor cost: "I don't have quantitative numbers", then 20-25%. One full-time doctor left, framed as "zero attrition". | Feb26 p.10 l.388-393 |
| I21 | MINOR | Aug: "Q1 and Q3, as I said earlier, these 2 quarters are relatively weaker". No earlier statement exists in the Feb or May calls. In Feb, asked about the weak Q3, the CEO gave no seasonal reason. | Aug26 p.7 to Amey Chalke l.259-261; Feb26 p.8 l.294-303 |
| I22 | MINOR | Dombivli breakeven guidance held after a near-breakeven Q2: "Positive surprises are welcome, but one must kind of... be conservative". Possible sandbagging. The direction is favourable. | Aug26 p.6 to Sakshi Pratap l.215-219; Aug26 p.7 l.284-288; Oct26 p.7 to Aryan Jain l.282-289 |
| I23 | MINOR | Dombivli fixed cost moves from Rs 6-7 Cr a month to Rs 6 to 8-odd Cr. In Oct an analyst says "per quarter" and the CEO does not correct it. More fixed cost is flagged ahead. | Aug26 p.4 l.154; Oct26 p.6 l.246-251; Oct26 p.9 l.350-352; May26 p.9 l.331-334 |
| I24 | MINOR | Same call, two numbers: Thane "occupancy is already high, 70%" and "it is around 75% now". Pune: "close to 65%" (May), "low 60% or mid-60%" (Aug), "close to 70%" (Oct). | Oct26 p.4 l.162-163; Oct26 p.9 l.360; May26 p.5 l.193; Aug26 p.4 l.132 |
| I25 | MINOR | Occupancy is on census beds, about 144 of 200 at Dombivli. Disclosed only when asked. | Oct26 p.8 to Ahmed Madha l.326-331 |
| I26 | MINOR | CGHS tone shift. Feb: "you will not see any impact on that at all". Aug: "with the revised pricing, we could consider it at some point". | Feb26 p.9 l.333-336; Aug26 p.9 l.360-361 |
| I27 | MINOR | Peer contrast on doctors. JLHL: "in the locations that we operate, it is not hard to find good doctors". KIMS: in Maharashtra "doctors are not fully aligned to having a full-time practice... it will always be a slow growth till the market matures". JLHL accepts visiting doctors, so the contrast is partial. | Feb26 p.10 l.384-385; Feb26 p.7 l.261-263; KIMS Aug26 p.13-14 l.485-510 |
| I28 | MINOR | Peer contrast on insurer friction. JLHL: no "unusual friction with the payer community". KIMS cites the FY26 industry "standoff" and GIC common-empanelment confusion. MEDANTA concedes "we could have been faster and more efficient". JLHL's existing units may have been unaffected. | Feb26 p.8 l.306-308; KIMS May26 p.9 l.333-341; MEDANTA Feb26 p.16 l.601-609 |

Totals: 28 items. Material 13 (CRITICAL 2, MAJOR 11). Minor 15.

## Part 2. Comparison against the pipeline

| ID | Sev | Status | Where the pipeline has it, and the gap |
|---|---|---|---|
| I1 | CRITICAL | CAUGHT | B05 2E "Financial guidance, margin outlook... Deflected every time"; YAML repeated_evasions; 3C rows on margin and onco cap; 4D "Regulatory margin caps not modelled". B06 Q9 brings the YATHARTH 0.3 figure. |
| I2 | CRITICAL | CAUGHT | B05 2E "Dombivli revenue... deflected every time"; 2D item 9; 2C transparency; YAML repeated_evasions. B06 Q2: peers "give per-hospital figures". |
| I3 | MAJOR | PARTIALLY CAUGHT | B05 FLAG-SEASONAL-CAVEAT; 3C "Medium: cost fall vs revenue gain not separated"; 2D item 11. Under-weighted. B05 reads the same quarter as "Strengthening (better than band)" (1C) and marks the loss band DELIVERED (2A row 6). It does not test whether seasonality can close the gap, and it does not log that four analysts pressed the point. |
| I4 | MAJOR | CAUGHT | B05 2D item 1, 4D HIGH, FLAG-GOVERNANCE-SILENCE. B05 also found the resignation filing dates in the announcements, which are outside my inputs. |
| I5 | MAJOR | MISSED | B05 1C rates Pune South "Strengthening" and treats the land purchase as a new trigger ("control, certainty"). Neither report sets it against "we pretty much own all the real estate". Neither notes that the landowner is unnamed. |
| I6 | MAJOR | CAUGHT | B05 FLAG-FUNDING-DRIFT; 2A row 11; 2E row 3. |
| I7 | MAJOR | PARTIALLY CAUGHT | B05 2D items 5-6 (capex total about Rs 2,550 Cr never stated; BKC date); 1C BKC "Weakening"; 2A row 12. No 4D or YAML red flag for BKC. The "back of the envelope... Detailed calculations... subsequently" answer is not cited. |
| I8 | MAJOR | CAUGHT | B05 1C "Indore phase 2... WEAKENING"; 2A row 10; 2B rows 2-3; 4D MEDIUM. |
| I9 | MAJOR | PARTIALLY CAUGHT | B06 Q4 and FLAG-NABH-NOT-GATE carry the KIMS NABH line. Misclassified. B06 records "Claims contradicted: 0" and aims the KIMS line at B05's confirm signal, not at the CEO's own claim that cashless needs NABH first. B05 1C rates the move from "6 to 12 months" to "about a year" as "Unchanged". |
| I10 | MAJOR | PARTIALLY CAUGHT | B05 3C row 1 (single-digit quarter); 2C defensiveness 2; 3B renewals. B06 Q3: "Q4 is not a clean read of price". Not drawn: the biennial renewal step makes FY26 ARPOB growth a poor base for FY27. A defensiveness score of 2 is light for "Nothing has happened... I have not noticed that" together with "astrology" and "crystal ball". |
| I11 | MAJOR | MISSED | Neither report mentions the unbilled-revenue policy change (search of both reports: no hit for "unbilled" or "accounting policy"). |
| I12 | MAJOR | CAUGHT | B05 2B, 2D item 7, 3C, 4D LOW-MEDIUM. The weight is defensible while the filing check is pending. |
| I13 | MAJOR | CAUGHT | B06 Q10, FLAG-PEER-SUPPLY-IN-JLHL-MARKETS. |
| I14 | MINOR | CAUGHT | B05 2A row 6 ("just above band"); 2C accountability; 1B 200-bed basis. |
| I15 | MINOR | CAUGHT | B05 1C, timeline_slippages. |
| I16 | MINOR | CAUGHT | B05 2A row 15; 1C. |
| I17 | MINOR | CAUGHT | B05 2D item 8; 3C. |
| I18 | MINOR | CAUGHT | B05 2B row 1. |
| I19 | MINOR | CAUGHT | B05 2A row 4; 2D item 2. |
| I20 | MINOR | CAUGHT | B05 3A; B06 Q5. |
| I21 | MINOR | MISSED | B05 turns this claim into a May promise that was "DELIVERED" (2A row 8). See finding F4. |
| I22 | MINOR | PARTIALLY CAUGHT | B05 2B notes the conservative caution. But 1C, the slippage list and repeated_evasions read the held guidance as a slip and an evasion. See findings F3 and F7. |
| I23 | MINOR | CAUGHT | B05 2D item 11; 1B. |
| I24 | MINOR | CAUGHT | B05 3D. |
| I25 | MINOR | CAUGHT | B05 load-bearing fact 4; B06 Q2. |
| I26 | MINOR | MISSED | B05 1C and 3D treat CGHS as "Unchanged (low relevance)". |
| I27 | MINOR | CAUGHT | B06 Q5; FLAG-MAHARASHTRA-DOCTOR-MODEL. |
| I28 | MINOR | MISSED | B05 3B quotes "not unusual" friction. B06 lists the common-empanelment risk but does not set the peer standoff against JLHL's no-friction claim. |

Tally: caught 18, partially caught 5, missed 5. Material: caught 7, partially caught 4, missed 2.

### Pipeline flags I did not raise myself

| Pipeline flag | Assessment | Basis |
|---|---|---|
| B05: H1 FY27 PAT -7.4%, not explained on the calls | SUPPORTED | H1 FY26 PAT = 9M FY26 Rs 143.9 Cr less Q3 FY26 Rs 42.5 Cr = Rs 101.4 Cr (derived, Feb26 p.4 l.139-143). H1 FY27 PAT Rs 93.9 Cr (Oct26 p.4 l.137-138). No D&A or finance-cost number is given in Aug or Oct. Partial explanation exists: the Feb depreciation warning (Feb26 p.3 l.121-124), which B05 2D item 2 notes, and an analyst citing higher finance cost (Aug26 p.9 l.351-354). |
| B05: receivables rise never discussed | SUPPORTED as to the calls | No transcript mentions receivables. The closest is Janargan on EBITDA-to-cash after working capital, answered with "around 70%" (Oct26 p.10 l.405-418). The rupee figures come from the presentation, outside my inputs. |
| B05: "24 months" and "on budget" unverifiable or contradicted | SUPPORTED for the transcript part; contradiction not assessed | Claims at Feb26 p.3 l.107-111 and May26 p.3 l.106-109. The contradiction rests on B03 AR evidence outside my inputs. |
| B05: director resignation | NOT ASSESSED | Rests on an announcement file outside my inputs. The CFO part is supported by the management lists (I4). |
| B05 timeline_slippages and 1C: "Dombivli breakeven wording: end of year 2 to 1.5-2 years, hard to predict" (range "widened") | NOT SUPPORTED | In Aug the analyst calls the guidance "1.5 to 2 years" and the CEO says "No, the guidance still holds" (Aug26 p.6 l.215-219). In Oct he repeats "one and a half year, some will take two" and declines to revise upward (Oct26 p.7 l.282-289). A 1.5-2 year range is not later than "end of year 2". The sign is reversed. |
| B05 repeated_evasions: "Will the Dombivli breakeven guidance be revised: deflected every time" | OVERSTATED | Each answer is direct: the guidance holds, it will be reviewed after 1-2 quarters (Aug26 p.6 l.219; Aug26 p.7 l.284-288; Oct26 p.7 l.282-289). Declining to raise a guidance is not an evasion. |
| B05 2A row 4 and 2D item 4: "Q4 FY26 drag Rs 9.4 Cr" | OVERSTATED | The call says only "The INR9.4 crores from the Dombivli unit that is completely baked in, in the quarter 4 results" (May26 p.7 l.259-261). It does not say loss or revenue. In Oct an analyst attaches "INR9.4 crores or INR9.5 crores" to Q1 (Oct26 p.4 l.169-170). The drag reading is plausible, not stated. |
| B05 2C: "exact" debt not given "every call"; "Aug and Oct" | OVERSTATED | The "exact number" disclaimer appears only in Aug, twice (Aug26 p.8 l.318; p.9 l.355). May (p.4 l.143-144) and Oct (p.11 l.427-429) give approximate figures without it. |
| B06 FLAG-LEVERAGE-CEILING-ABOVE-PEERS | SUPPORTED | KIMS: a healthy net debt to EBITDA "should be 1 is to 2" (garbled; reads as about 2x) (KIMS May26 p.18 l.661-663; p.19 l.679-680). YATHARTH: "2x of the trailing last 12 months EBITDA" (YATHARTH Aug26 p.18 l.772-775). JLHL: 3x (May26 p.5 l.183-185). B06's "1-2x" band label is loose; both peers point to about 2x. |
| B06 FLAG-PAT-LAG-PATTERN | SUPPORTED as a hypothesis | Peer figures not re-derived here; numbers are Verifier A's domain. |
| B06 FLAG-CAPEX-PER-BED-ESCALATION | SUPPORTED as derived by B06 | Not re-derived here. |
| B06 FLAG-CONFIRMED-NO-NAMED-PEER-MENTION | SUPPORTED | My sweep found no Jupiter, Dombivli or Pune hit in the 12 peer files. |
| B06 Q8: "KIMS shows the opposite in Q2 FY27" | OVERSTATED | KIMS group ARPOB per operating bed includes ramping new units, so a +2.3% sequential rise does not test JLHL's medical-mix mechanism. "Not corroborated" is the supported wording. |

## Part 3. Promise-delivery spot checks (B05 2A)

| Row | Promise as B05 states it | Earlier call has the promise? | Later call shows the outcome? | Result |
|---|---|---|---|---|
| 1 | Dombivli launch by Q1 FY27; inaugurated 15 Feb | Yes. "ahead of its planned launch in Q1 of FY '27"; "slated to be inaugurated on February 15" (Feb26 p.3 l.106-118) | Yes. "we beat that and opened ahead of schedule" (May26 p.3 l.102-106) | CONFIRMED. B05 cites "May p.2"; the text is on PDF p.3. |
| 6 | Dombivli loss Rs 2-3 Cr a month, FY27 average | Yes. "between INR2 crores to INR3 crores a month on an average for the whole year" (May26 p.8 l.288) | Yes. Q1 Rs 9.5 Cr (Aug26 p.3 l.98); Q2 Rs 0.2 Cr (Oct26 p.3 l.123-124). H1 Rs 9.7 Cr = Rs 1.6 Cr a month (derived) | CONFIRMED in direction. But it is a full-year promise and only H1 has passed. Under B05's own rule ("Counts cover items already due") it is on track, not delivered. |
| 8 | "Q1 weaker, Q2 and Q4 stronger", promised in Q4 FY26 (May) | No. The May call has no seasonality statement (search for weak, season, stronger: no hit; the one "season" hit is about renewals, l.303). The Feb call has none either. The first statement is Aug26 p.7 l.259-261, and it claims an antecedent ("as I said earlier") that does not exist. | Q1 margin 19.3% and Q2 23.4% are consistent with seasonality, but there was no promise to test. | WRONG. The row has no source promise and is counted in "delivered 6". |
| 9 | Mira Road excavation "by the end of the year" | Yes (May26 p.3 l.114-116) | Yes, softened: "regulatory stage... next phase of activities before the end of this financial year" (Oct26 p.3 l.117-119) | CONFIRMED (softened, not yet due). B05 labels it "not yet due" but still counts it as a partial. |
| 10 | Indore phase 2 at about 60% occupancy | Yes. "Once the occupancy crosses 60% or near 60%" (May26 p.7 l.268-269) | Yes. "We would like to be in mid-60s" (Oct26 p.10 l.391-393) | CONFIRMED. The condition has not been met, so it is not yet due either. |

Checked 5. Confirmed 4. Wrong 1.

Recount under B05's due-only rule (derived): delivered rows 1, 3, 4, 7 = 4; partial rows 2, 11 = 2 (3 if the Indore threshold move counts as a partial); missed 0. B05 reports 6 / 4 / 0.

## Part 4. Credibility grade

B05 grades B (Good). I concur at the low end of B. Zero hard misses holds after the recount (4 delivered, 2 partial, 0 missed). Dombivli opened early and its loss band is beaten so far. Against that: the Pune leased-land statement was proven wrong within two quarters; the funding line moved in one quarter; unit economics and margin questions are deflected in every call; and Aug claimed a prior seasonality disclosure that does not exist. These sit on the disclosure axis, not the delivery axis. They do not break a B that rests on delivery. They do put it at the floor of the band. One more contradiction of the I5 type, or a Q3 FY27 Dombivli drag above Rs 3 Cr a month, would move me to C.

## Part 5. Consolidated findings

| ID | Severity | Type | Finding | Anchor |
|---|---|---|---|---|
| F1 | MAJOR | MISSED (I5) | Pune South land was leased. This contradicts the May statement "we pretty much own all the real estate". The Rs 150 Cr purchase (Rs 100 Cr new cash) is graded "Strengthening" with no contradiction flag. The landowner is unnamed in the call. | May26 p.4 l.133-136; Oct26 p.3 l.108-116 |
| F2 | MAJOR | MISSED (I11) | The Q2 FY26 unbilled-revenue policy change and its one-time revenue bump are absent from B05 and B06. The bump inflates the FY26 growth base. Its size is NOT FOUND in the calls. | Aug26 p.4 l.136-147 |
| F3 | MAJOR | NOT SUPPORTED | B05 lists "Dombivli breakeven wording: end of year 2 to 1.5-2 years" as a timeline slippage and says the range "widened". The transcripts show the same 1.5-2 year guidance held in Aug and Oct, with an upward revision deferred. The analysis invented a negative signal. | Aug26 p.6 l.215-219; Oct26 p.7 l.282-289 |
| F4 | MAJOR | SPOT CHECK WRONG (I21) | B05 2A row 8 credits a May promise ("Q1 weaker, Q2 and Q4 stronger") as DELIVERED. No such statement exists in the May or Feb calls. The Aug claim "as I said earlier" has no antecedent, and that is itself a red flag. The row inflates the delivered count. | May26 full text (no hit); Aug26 p.7 l.259-261 |
| F5 | MAJOR | PARTIALLY CAUGHT (I3) | The Dombivli Q2 swing is read as "Strengthening" with only a seasonal caveat. Derived arithmetic: contribution about doubles against a 17-40% occupancy rise at lower ARPOB, so seasonality alone does not close the gap. Four analysts pressed it and got "I can't answer" or "I really don't know". The second reading (cost timing or allocation) is not named. B05's own kill signal should add: Q3 FY27 drag above Rs 2 Cr a month without a named one-off. | Oct26 p.4-6 l.169-184, l.246-255; Oct26 p.9-10 l.365-388 |
| F6 | MINOR | Internal inconsistency | B05 2A states "Counts cover items already due" but counts rows 6 (full-year FY27), 9 (end CY26) and 10 (condition unmet), none of them due. A due-only recount gives 4 / 2 / 0, not 6 / 4 / 0. The grade survives. | B05 2A, lines 100 and 123 |
| F7 | MINOR | OVERSTATED | B05 lists "Dombivli breakeven guidance revision" as a repeated evasion. Each answer was direct; it declines an upward revision. | Aug26 p.6 l.219; Oct26 p.7 l.282-289 |
| F8 | MINOR | OVERSTATED | B05 states a "Q4 FY26 drag Rs 9.4 Cr". The call says "INR9.4 crores from the Dombivli unit... baked in" without saying loss or revenue. | May26 p.7 l.259-261; Oct26 p.4 l.169-170 |
| F9 | MINOR | OVERSTATED | B06 Q8 says KIMS "shows the opposite" on Q2 medical-mix ARPOB. KIMS group ARPOB mixes in ramping units, so it is not a clean test. | B06 Q8 |
| F10 | MINOR | PARTIALLY CAUGHT (I7) | BKC carries no red-flag row although its funding was "back of the envelope" with "Detailed calculations... subsequently". | May26 p.6 l.224-230 |
| F11 | MINOR | PARTIALLY CAUGHT (I9) | B06 records "contradicted: 0" although KIMS ("NABH is not a prerequisite for empanelment") contradicts the JLHL CEO ("You need your NABH accreditation in place"). B05 1C calls the move from 6-12 months to about a year "Unchanged". | KIMS Feb26 p.7 l.266-268; Oct26 p.9 l.342-344 |
| F12 | MINOR | PARTIALLY CAUGHT (I10) | The biennial insurer-renewal step behind FY26 ARPOB growth is not carried into the FY27 mature-unit read. A defensiveness score of 2 is light. | May26 p.7 l.274-277; Feb26 p.8 l.296-299 |
| F13 | MINOR | MISSED (I26) | CGHS stance shift from "no impact at all" to "could consider it". | Feb26 p.9 l.333-336; Aug26 p.9 l.360-361 |
| F14 | MINOR | MISSED (I28) | Peer insurer-standoff contrast with JLHL's no-friction claim is not drawn. | KIMS May26 p.9 l.333-341; Feb26 p.8 l.306-308 |
| F15 | MINOR | OVERSTATED | "'Exact' debt [refused] every call" and "in Aug and Oct": only Aug has the disclaimer. | Aug26 p.8 l.318; p.9 l.355; Oct26 p.11 l.427-429 |
| F16 | MINOR | Anchor imprecision (route to Verifier A) | Several B05 May, Aug and Oct cites are one page low (they match the printed page, not the PDF page that B05 says it uses). Examples: May opening cited p.2 (PDF p.3); May funding p.3 (PDF p.4); May loss band p.7 (PDF p.8); May empanelment p.4 (PDF p.5); May Indore 60% p.6 (PDF p.7); Aug debt "towards the end" p.7 (PDF p.8); Oct term loan p.9 (PDF p.10); Oct net debt p.10 (PDF p.11). Verifier A owns anchors. I list these only so they reach that check. | B05 2A, 1B, 1C |

Counts: CRITICAL 0, MAJOR 5, MINOR 11.

No CRITICAL finding stands against the pipeline. Both repeated evasions I graded CRITICAL (I1, I2) were caught.

## Part 6. Scoring

- Independent items: 28. Material (CRITICAL + MAJOR): 13.
- The pipeline found 11 of the 13 material items: 7 in full, 4 partially (found but under-weighted or misclassified). It missed 2, both MAJOR (I5, I11).
- acceptance_rate = 11 / 13 = 84.6%, reported as 85. The rubric defines material_caught as items "the pipeline already had". A partial catch is one the pipeline found, so I count it.
- For transparency, the full-catch-only rate is 7 / 13 = 53.8%. I do not score on it. I state it so the orchestrator can see the size of the partial set.
- The denominator is 13, above the 4-item floor, so the rate is reported, not null.

```yaml
stage: B12b
company: "JLHL"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 28
caught: 18
partially_caught: 5
missed:
  - {severity: "MAJOR", item: "Pune South land was leased, contradicting May 'we pretty much own all the real estate'; Rs 150 Cr purchase (Rs 100 Cr new cash) announced Oct; landowner not named; B05 grades it 'Strengthening'", anchor: "May26 PDF p.4 Ankit Thakker l.133-136; Oct26 PDF p.3 opening l.108-116; Feb26 PDF p.4 l.156-164"}
  - {severity: "MAJOR", item: "Q2 FY26 unbilled-revenue accounting policy change gave a one-time revenue bump; size not given; inflates FY26 growth base; absent from B05 and B06", anchor: "Aug26 PDF p.4 Dhvani Shah / Ankit Thakker l.136-147"}
  - {severity: "MINOR", item: "Aug 'Q1 and Q3, as I said earlier, are relatively weaker' has no antecedent in Feb or May calls; B05 recast it as a delivered May promise", anchor: "Aug26 PDF p.7 Ankit Thakker l.259-261; Feb26 PDF p.8 l.294-303"}
  - {severity: "MINOR", item: "CGHS stance shift: Feb 'you will not see any impact on that at all' to Aug 'with the revised pricing, we could consider it'; B05 calls it unchanged", anchor: "Feb26 PDF p.9 l.333-336; Aug26 PDF p.9 l.360-361"}
  - {severity: "MINOR", item: "Peer contrast not drawn: KIMS cites FY26 industry insurer standoff and GIC common-empanelment confusion; MEDANTA 'could have been faster'; JLHL said no unusual payer friction", anchor: "Feb26 PDF p.8 l.306-308; KIMS May26 PDF p.9 l.333-341; MEDANTA Feb26 PDF p.16 l.601-609"}
pipeline_flags_not_supported:
  - "B05 timeline_slippages and 1C: 'Dombivli breakeven wording: end of year 2 to 1.5-2 years, hard to predict' (range 'widened'). Aug26 PDF p.6 l.215-219: analyst states guidance as '1.5 to 2 years', CEO 'the guidance still holds'; Oct26 PDF p.7 l.282-289 repeats 1.5-2 years and defers an upward revision. No slip; sign reversed."
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "concur at B, low end: zero hard misses holds, but a due-only recount is 4 delivered / 2 partial / 0 missed (row 8 has no source promise; rows 6, 9, 10 not due), and the Pune leased-land contradiction belongs in the basis"
findings:
  - {id: F1, severity: MAJOR, type: MISSED, item: "Pune South leased land vs 'we pretty much own all the real estate'; landowner unnamed", anchor: "May26 p.4 l.133-136; Oct26 p.3 l.108-116"}
  - {id: F2, severity: MAJOR, type: MISSED, item: "Unbilled-revenue policy change, one-time Q2 FY26 revenue bump, unsized", anchor: "Aug26 p.4 l.136-147"}
  - {id: F3, severity: MAJOR, type: NOT_SUPPORTED, item: "B05 lists Dombivli breakeven wording as a timeline slippage; guidance held at 1.5-2 years in Aug and Oct", anchor: "Aug26 p.6 l.215-219; Oct26 p.7 l.282-289"}
  - {id: F4, severity: MAJOR, type: SPOT_CHECK_WRONG, item: "B05 2A row 8 seasonality 'promise' from May does not exist in May or Feb; counted as delivered", anchor: "May26 (no hit); Aug26 p.7 l.259-261"}
  - {id: F5, severity: MAJOR, type: PARTIALLY_CAUGHT, item: "Dombivli Q2 swing (Rs 9.5 Cr to Rs 0.2 Cr) read as Strengthening; derived contribution about doubles vs 17-40% occupancy rise at lower ARPOB; four analysts pressed; cost-timing reading not named", anchor: "Oct26 p.4-6 l.169-184, l.246-255; p.9-10 l.365-388"}
  - {id: F6, severity: MINOR, type: INTERNAL_INCONSISTENCY, item: "B05 counts not-yet-due rows 6, 9, 10 against its own due-only rule; recount 4/2/0", anchor: "B05 2A"}
  - {id: F7, severity: MINOR, type: OVERSTATED, item: "Breakeven-guidance revision listed as a repeated evasion; answers were direct", anchor: "Aug26 p.6 l.219; Oct26 p.7 l.282-289"}
  - {id: F8, severity: MINOR, type: OVERSTATED, item: "'Q4 FY26 drag Rs 9.4 Cr': call does not say loss or revenue", anchor: "May26 p.7 l.259-261"}
  - {id: F9, severity: MINOR, type: OVERSTATED, item: "B06 Q8 'KIMS shows the opposite' on Q2 medical-mix ARPOB; KIMS group ARPOB not a clean test", anchor: "B06 Q8"}
  - {id: F10, severity: MINOR, type: PARTIALLY_CAUGHT, item: "BKC 'back of the envelope' funding with no red-flag row", anchor: "May26 p.6 l.224-230"}
  - {id: F11, severity: MINOR, type: PARTIALLY_CAUGHT, item: "B06 'contradicted: 0' despite KIMS NABH line contradicting the JLHL CEO; B05 calls empanelment drift Unchanged", anchor: "KIMS Feb26 p.7 l.266-268; Oct26 p.9 l.342-344"}
  - {id: F12, severity: MINOR, type: PARTIALLY_CAUGHT, item: "Biennial renewal step behind FY26 ARPOB not carried to FY27; defensiveness 2 is light", anchor: "May26 p.7 l.274-277; Feb26 p.8 l.296-299"}
  - {id: F13, severity: MINOR, type: MISSED, item: "CGHS stance shift", anchor: "Feb26 p.9 l.333-336; Aug26 p.9 l.360-361"}
  - {id: F14, severity: MINOR, type: MISSED, item: "Peer insurer-standoff contrast not drawn", anchor: "KIMS May26 p.9 l.333-341"}
  - {id: F15, severity: MINOR, type: OVERSTATED, item: "'exact' debt refused 'every call' / 'Aug and Oct'; only Aug", anchor: "Aug26 p.8 l.318; p.9 l.355"}
  - {id: F16, severity: MINOR, type: ANCHOR_IMPRECISION, item: "Several B05 May/Aug/Oct cites one page low (printed vs PDF page); route to Verifier A", anchor: "B05 2A, 1B, 1C"}
critical_count: 0
major_count: 5
minor_count: 11
material_found: 13
material_caught: 11
acceptance_rate: 85
coverage_basis: "13 material (2 CRITICAL, 11 MAJOR) of 28 listed; pipeline had 11 (7 caught in full, 4 partially caught = found but under-weighted or misclassified); 2 MAJOR missed (I5 Pune leased land, I11 unbilled revenue). 11/13 = 84.6%. Full-catch-only rate 7/13 = 53.8%, shown for transparency, not scored. Peer transcripts read by JLHL-relevant sections plus keyword sweeps, not line by line; main-company transcripts read in full."
```
