# STAGE 12 VERIFIER B: CONCALL RED FLAGS — CAPILLARY

Run date: 2026-09-19. Model: claude-opus-5. Fresh context.

Inputs read:
- 3 company transcripts, read in full: Q3 FY26 (call 06-Feb-2026), Q4 FY26 (call 06-May-2026), Q1 FY27 (call 04-Aug-2026).
- 12 peer transcripts (NEWGEN x4, UNIECOM x4, INTELLECT x4). I read them by targeted search, not line by line. The claims B05 and B06 lean on were checked at source.
- B05 report `outputs/reports/05-concall.md` and B06 report `outputs/reports/06-peers.md`. I read these only after writing my independent list.

Anchor convention: (call, speaker, `[page N]` marker in the .txt, line L). For example, "Q1 FY27, Aneesh, [p11] L464-469" means the Aug-2026 .txt, page marker 11, lines 464-469.

Coverage limit: the INTELLECT May-2026 and Aug-2026 .txt files hold one word per line (13-15k lines each). Phrase search fails on them. I checked their load-bearing claims by single-token search ("60%"). I did not read them end to end.

---
## PART 1: INDEPENDENT RED-FLAG LIST (from raw transcripts only)

Severity uses the shared scale: CRITICAL, MAJOR, MINOR. Status comes from the Part 2 comparison.

| # | Sev | Item | Anchors | Pipeline status |
|---|---|---|---|---|
| 1 | MAJOR | **The organic growth rate is unresolved and management gave three different numbers.** Q1 FY27 organic growth is 17% YoY. Management then put the currency benefit at "about 6% on it" (Q1 FY27, Anant, [p13] L545-550). An analyst worked Q1 organic out at ~11% (Sanjay, [p18] L727-731). Aneesh first said "we will do roughly a 20%-23% organic growth this year". He then corrected it: "23% growth including a currency impact of about 6%... about 17%-odd full-year organic" (L742-747). He also calls Capillary "a 15% to 20% organic growth business" ([p18-19] L757-758). The FY27 plan splits Rs 1,065 Cr into organic ~Rs 673 Cr and acquired ~Rs 390 Cr (Q1 FY27, Aneesh, [p11] L464-469; [p12] L476). The Q4 call put FY26 acquisition-linked revenue at Rs 80-100 Cr, "probably a little bit more", out of Rs 735 Cr (Q4 FY26, Aneesh, [p11] L463-465). [INFERENCE] That arithmetic puts FY26 organic at Rs 634-654 Cr and the FY27 organic plan at +3-6%. That does not fit the 17% claim. Reading A: the plan is deliberately conservative ("will definitely beat", [p24] L977). Reading B: underlying constant-currency organic growth sits near 11%, not 15-20%. The observation that separates them is an organic, constant-currency revenue figure for H1 FY27. | Q1 FY27 [p11-13], [p18-19]; Q4 FY26 [p11] | PARTIALLY CAUGHT |
| 2 | MAJOR | **The large healthcare customer story contradicts itself across calls.** Q3 FY26: the large US healthcare payer is "one of the top five clients". Its member base "actually gone up by roughly 50%", with "a good bump up on number of members and the revenue... through CY26" (Q3 FY26, Aneesh, [p10-11] L432-449). Q1 FY27: "one the largest customer we have" did not grow. Excluding it, NRR is 116% against a reported 111% (Q1 FY27, Aneesh, [p4] L166-167). "Q1 is a little bit of an aberration because this large healthcare customer we had didn't grow" ([p18] L744-745). No call reconciles the two. Nobody asked. Reading A: these are two different accounts. Anant's "largest healthcare customer or one of the largest healthcare pharmacy chain in the US" ([p21] L870) hints at a pharmacy chain, not the payer. Reading B: it is the same account, and the promised CY26 revenue bump did not arrive. The separating observation is management naming whether the flat Q1 account is the payer. | Q3 FY26 [p10-11]; Q1 FY27 [p4], [p18], [p21] | MISSED |
| 3 | MAJOR | **aiRA revenue sizing went backwards while the pipeline read it as "rising".** Q4 FY26: "We are a few million dollars now in revenues from the aiRA stack" (Aneesh, [p4] L155). "We probably at about 4%, 5% of our revenues coming from the AI stack. Now, not all of it is live" ([p17] L719-720). Q4 also said intelligence and action spaces have "traditionally been like less than 5% of our revenue" ([p7] L330). Q1 FY27: "$2 million, $2.5 million in terms of revenue run rates" (Aneesh, [p10] L393). "About USD2.5 million-ish in ARR" ([p19] L782). 26 of 150 customers live, "a little less than 10" paying ([p6] L239-240). [INFERENCE] 4-5% of FY26 revenue of Rs 734 Cr is Rs 29-37 Cr. Management's own pairing on the same call ("INR17-odd crores... $1.5 million or probably a couple of million", [p7] L279-281) implies $2.5M is about Rs 21-28 Cr. On Q1 ARR of Rs 1,026 Cr that is under 3%. Reading A: the Q4 4-5% counted signed but not-live AI contracts ("not all of it is live"). Reading B: the Q4 figure was overstated. The separating observation is a next-call split of contracted versus live aiRA ARR. | Q4 FY26 [p4], [p7], [p17]; Q1 FY27 [p6], [p10], [p19] | PARTIALLY CAUGHT |
| 4 | MAJOR | **SessionM's acquired base shrank from $35M to $32M without comment.** Q4 FY26: "a sizeable $35 million business, 40 plus logos" (Aneesh, [p5] L203). "The INR35 million [sic] that we bought from SessionM" ([p11] L468). Q1 FY27: "we had projected about a $32 million ARR... the entire $32 million have agreed to sign our paper" (Aneesh, [p7] L266-269). The customer count is "45-odd" ([p9] L364). Reading A: $35M was total revenue including non-recurring items, and $32M is recurring ARR, so the two bases differ. Reading B: about 9% of the acquired base fell away before or at close. The separating observation is the SessionM revenue contribution in the Q1 FY27 segment or notes data. | Q4 FY26 [p5], [p11]; Q1 FY27 [p7], [p9] | MISSED |
| 5 | MAJOR | **The SessionM price reconciliation does not close, and an analyst had to press for it.** Chintan Shah pointed out that the price was ~$17M, yet management now says Rs 17 Cr net (Q1 FY27, [p22] L907-910). Anant: "$20 million buy... adjusted for any net debt items at the time of closing... true-up on 30th April... down to about INR17 crores" (L911-919). Aneesh: "there is no debt on the SessionM entities... These are debt-free entities" (L920-921). [INFERENCE] The ~$18M adjustment is therefore something other than debt. Working capital or assumed liabilities such as customer prepayments and deferred revenue are likely candidates. It was not named. Aneesh builds the payback claim on the Rs 17 Cr net figure: "essentially spent $1.5 million... payback possibly within this year" ([p7] L279-285). If the adjustment is assumed service obligations, the economic price is far higher than Rs 17 Cr. The separating observation is the purchase-price allocation in the Q1/Q2 FY27 notes. | Q1 FY27 [p7], [p22] | PARTIALLY CAUGHT (misclassified as a transparency positive) |
| 6 | MAJOR | **The Kognitiv churn indemnity is a volunteered negative about the quality of an acquired book.** Q4 FY26: "one-time exceptional income of INR25 crores... compensation received under a churn indemnity clause in the Kognitiv acquisition, which was triggered because seller failed to meet certain agreed commitments" (Anant, [p9-10] L396-399). On the same call: "On the Kognitiv part, we've already started to see EBITDA getting accrued" (Aneesh, [p5] L209-211). Inorganic NRR moved from 96% (TTM Dec-25, Q3 FY26 [p8] L319-320) to 94% (FY26, Q4 FY26 [p4] L186-191). Kognitiv migration had not started by Aug-2026. The first customer was due 1-Sep-2026 (Q1 FY27 [p11] L437-438). The M&A engine assumes about 70% revenue retention (Q4 FY26 [p15-16] L684-687). A churn event big enough to trigger an indemnity tests that assumption. | Q4 FY26 [p4], [p5], [p9-10]; Q3 FY26 [p8] | PARTIALLY CAUGHT (logged only as a normalisation one-off, Low) |
| 7 | MAJOR | **The migration timeline lengthened across calls.** Q4 FY26: with the new AI upgrade platform, "integrations from acquisitions not taking a long time but happening in a 12-to-18-month type period" (Aneesh, [p6] L248-250). Q1 FY27: "an 18 to 24-month type upgrade cycle" (Aneesh, [p11] L454-455). For Kognitiv, the first customer goes live 1-Sep-2026, 16 months after the 1-May-2025 close, with completion "latest September of next year" (L437-458). For SessionM, "typically takes about two to three years for all the customers to get upgraded. So, we will not start any SessionM migrations till probably end of this year, early next year" ([p9] L359-362). | Q4 FY26 [p6]; Q1 FY27 [p9], [p11] | PARTIALLY CAUGHT (Kognitiv slippage flagged; the SessionM 2-3 year horizon and the generic 12-18 to 18-24 month shift were not) |
| 8 | MAJOR | **Gross margin statements contradict each other across calls.** Q3 FY26: "the Capillary platform is more at 69%-70% gross margin" (Aneesh, [p6] L245). "Our gross margins are around the 69%-70% now" ([p13] L558). Q4 FY26: migrated customers "move from the 30% gross margin to a 65% gross margin" ([p6] L239). Steady state is "70% gross margin" ([p11] L473). Q1 FY27: "Our organic gross margins are upwards of 75% now... consistently upwards of 75% for the last few quarters" (Aneesh, [p5] L197-198). Blended subscription gross margin is 66% (L195-196). The "last few quarters" at >75% organic overlap the Q3 quarter that was described as 69-70% for the platform. This is a direct input to the 26.2 margin bridge. | Q3 FY26 [p6], [p13]; Q4 FY26 [p6], [p11]; Q1 FY27 [p5] | MISSED (B05 2C calls the margin math "repeated identically") |
| 9 | MAJOR | **The new-ACV metric was re-based to produce growth.** Q3 FY26: 9M new order book Rs 66 Cr against Rs 53 Cr (Aneesh, [p5] L210-212). Q4 FY26: "new ACV of INR121 crores, similar to that of last year" (Anant, [p9] L390-391), i.e. flat. Aneesh gave "INR80-90 crores or a INR70 to INR80 crores of new business a year" ([p14] L592-594, L601). Q1 FY27: TTM new ACV "growth of about 75% year-on-year to about INR92 crores" only "if we exclude one large healthcare customer" from the base (Anant, [p8] L326-330). Kumar Saurabh challenged the flat-to-80% jump ([p23] L934-937). Akshay Jogani called the definitions "super confusing" ([p16] L645-650). The full-year guide is "at least 30%-40% more new ACV than last year", with the base not stated ([p23] L944-946). | Q3 FY26 [p5]; Q4 FY26 [p9], [p14]; Q1 FY27 [p8], [p16], [p23] | PARTIALLY CAUGHT (definitional complexity noted in 3C and analyst_note; the selective base exclusion is not flagged) |
| 10 | MAJOR | **Cyber-banking fraud: disclosure on the call was thin.** Q1 PAT was -Rs 9.5 Cr after an "exceptional loss... cyber-fraud incident and a one-time deferred tax liability" (Anant, [p8] L310-312). Insurance: "covered by insurance, but how much and when it would be recovered... we don't have clarity" ([p12-13] L508-517). The KPMG forensic audit was filed 31-Jul-2026 (announcement 20260731, L46-93) and was not mentioned on the 04-Aug call. | Q1 FY27 [p8], [p12-13]; filing 20260731 | CAUGHT |
| 11 | MINOR | Management declined to guide margin trajectory on two consecutive calls. Q3 FY26: "I definitely don't want to guide to any number" (Aneesh, [p15] L652). Q4 FY26: "Q4 is a sustainable number going forward", then "I don't want to comment on what the future might be given the large acquisition" (Anant, [p11] L449-459). A steady-state range (25-30%) was given, so neither is a full evasion. | Q3 FY26 [p15]; Q4 FY26 [p11] | MISSED |
| 12 | MINOR | The tax narrative shifts every quarter. Q3: "India standalone business is also profitable, we have started seeing tax expense" ([p8] L341-343). Q4: tax "continues to be negative and would continue to be negative given we have accumulated tax losses" ([p10] L418-420). Q1: "one-time deferred tax liability" ([p8] L311). | Q3/Q4/Q1 | MISSED |
| 13 | MINOR | ROCE "about 3%" was volunteered and immediately reframed as "cash return on invested capital... 22%" (Q4 FY26, Anant, [p10] L414-416). This is relevant to Section 1B Pillar 1. The reframing is management's, not an evidenced basis. | Q4 FY26 [p10] | MISSED |
| 14 | MINOR | Management disputes its own reported FY25 growth. The analyst's "13%" is "actually wrong, it's more closer to 20%, because we had done an accounting change". Revenue moved from gross to net for SMS/email pass-through (Q1 FY27, Aneesh, [p18] L733-742). The historical CAGR cross-check must use the net basis. | Q1 FY27 [p18] | MISSED |
| 15 | MINOR | Product-mix percentages do not add up. Loyalty ~90%, Engage 5-7%, Rewards 5-7%, AI stack 4-5% sum to more than 100% (Q4 FY26 [p4] L145-152; [p17] L719). Insights: aiRA "will... replace our Insights piece" (Q4 [p4] L155-156), yet "We don't monetize Insights" (Q1 [p3] L154-155). | Q4 FY26; Q1 FY27 | MISSED |
| 16 | MINOR | OCF/adjusted EBITDA ran above the "sustainable 105-110%" range. 9M FY26 was 142%, called an "anomaly" (Q3, Anant, [p9] L356-363). FY26 was Rs 150 Cr against Rs 107 Cr (Q4, Anant, [p10] L409-412). Q4 gave the reason: "we bill and collect money upfront in a healthy growing business" (L411-412). | Q3 FY26 [p9]; Q4 FY26 [p10] | CAUGHT (overweighted, see Part 2B) |
| 17 | MINOR | Every reported quarter carries a normalisation. Q3: gratuity Rs 1.6 Cr and IPO Rs 2 Cr. Q4: indemnity +Rs 25 Cr. Q1: fraud loss and DTL. (Q3 [p8] L329-332; Q4 [p9-10] L396-399; Q1 [p8] L310-312) | all three | CAUGHT |
| 18 | MINOR | SessionM margin claims escalated within one quarter. Q4: "break-even for year one and probably a little bit positive margins for year two. So, year three is when you will start seeing significant margins" ([p12] L497-500). Q1: "fully profitable", with evidence of Rs 5-6 Cr "free cash" in two months ([p7] L270-273), and a path of "break-even now... 15%-odd in a year... 35%-40%" ([p23] L964-966). In an upfront-billing business, two months of cash is not EBITDA evidence. | Q4 FY26 [p12]; Q1 FY27 [p7], [p23] | PARTIALLY CAUGHT (B05 scores it "delivered, ahead of schedule") |
| 19 | MINOR | **Peer contradiction on demand.** Capillary: "unlike a lot of the other folks where you're hearing about like new business slowing down, we are not seeing that as much" (Q3 FY26, Aneesh, [p12] L518-520). NEWGEN, same month: "larger enterprise deals are facing elongated decision cycles" and "slightly more deferment in large deals" tied to AI uncertainty (NEWGEN Jan-2026, Virender Jeet, L136-138, L222-223, L243, L469-471). The segments differ, so the contradiction is soft. | Q3 FY26; NEWGEN Jan-26 | CAUGHT (B06 2A/2E) |
| 20 | MINOR | **Peer parallel on NRR.** UNIECOM reports NRR "above 100%, excluding the churn of this we saw in the top 10 bucket" (UNIECOM May-2026, Kapil Makhija, L517-519; Aug-2026 L557-558). This is the same ex-one-client normalisation Capillary uses for its 116%. B06 reports UNIECOM as "100%+" and misses the exclusion. | UNIECOM May/Aug-26 | MISSED |
| 21 | MINOR | Peer: INTELLECT's Forge/CentralOne acquisition was "initially... margin neutral, but we are actually seeing a single digit margin business" (INTELLECT Feb-2026, Rajesh Saxena, L617-620). | INTELLECT Feb-26 | CAUGHT |
| 22 | MINOR | An analyst asked for the D&A split between acquisition intangibles and capitalised tech. The answer was only "majority of it is coming from Kognitiv", with no split (Q3 FY26, Rishi/Anant, [p11] L452-462). | Q3 FY26 [p11] | MISSED |
| 23 | MINOR | Management repeatedly mislabelled units and figures on the call. "INR 142 crores" for 142% (Q3 [p9] L363). "INR35 million" and "INR15 million type EBITDA" for USD (Q4 [p11-12] L468, L514-515). PAT and normalised PAT swapped (Q1 [p8] L336-337). This is cosmetic, but the numbers on the call cannot be taken verbatim. | all three | MISSED |
| 24 | MINOR | An analyst pressed on cost: headcount is flat but costs grow "almost in line" with revenue (Q4, Bharat Gulati, [p15] L613-616). The answer was a US sales ramp, with cost growth of 13-14% against revenue growth of 23% (L617-629). The answer is adequate. | Q4 FY26 [p15] | MISSED |
| 25 | MINOR | Customer concentration is never quantified on any call. "Top five" appears only in an analyst's question (Q3 [p10] L432-433). | all three | CAUGHT |

Totals: 25 items listed. 10 material (0 CRITICAL, 10 MAJOR) and 15 MINOR.

No CRITICAL item. I found no question asked in two or more calls and evaded both times. I agree with B05 2E on that point. The closest candidate is item 11, and a steady-state margin range was given there.

---
## PART 2: COMPARISON AGAINST PIPELINE

### 2A. My items against B05/B06

| # | Status | Basis |
|---|---|---|
| 1 | PARTIALLY CAUGHT | B05 1B records Q1 organic +17% and the 6% currency figure in separate rows. It never flags that the 6% may sit inside the 17%. Its guidance row "Full-year organic growth 20-23% (incl. ~6% currency)" misreads the transcript: Aneesh's final statement is 23% including FX, which gives ~17% organic. The Rs 673 Cr organic plan arithmetic is absent. |
| 2 | MISSED | B05 3B cites the Q3 +50% member step-up. B05 3D cites the Q1 flat account. The two facts are never linked or flagged. |
| 3 | PARTIALLY CAUGHT | B05 flags a "basis inconsistency" (piloting versus paying) but reads the trajectory as "quantification rising each quarter". It misses the Q4 "4-5% of revenues" statement. On the numbers, sizing fell. |
| 4 | MISSED | B05 3D records "$32m ARR retained, no surprises". The Q4 $35M figure is not carried forward. |
| 5 | PARTIALLY CAUGHT | B05 records "$20m gross / Rs 17 Cr net after debt true-up". It scores this as a transparency positive in 2C. The transcript says the entities are debt-free, so "debt true-up" is wrong and the gap is unexplained. |
| 6 | PARTIALLY CAUGHT | The indemnity appears only inside the "recurring normalise-for-one-offs" flag, rated Low. The read on acquired-book churn is absent. |
| 7 | PARTIALLY CAUGHT | Kognitiv slippage appears in timeline_slippages. The SessionM 2-3 year and "not start till end of year" statements are absent. |
| 8 | MISSED | Not mentioned. B05 2C states the margin playbook numbers are "repeated identically across all three calls", which the transcripts contradict. |
| 9 | PARTIALLY CAUGHT | B05 3C and analyst_note flag metric complexity. B05 still carries "+75% ex one account" into trigger #6 unqualified. It also anchors the "30-40% more" guide to "FY26's Rs 121 Cr", a base the transcript does not state. |
| 10 | CAUGHT | B05 4D, rated Moderate-High. |
| 16, 17, 19, 21, 25 | CAUGHT | B05 4D / B06 2A, 2E, Q4. |
| 18 | PARTIALLY CAUGHT | Recorded as a delivery, not as an escalation of claims. |
| 11-15, 20, 22-24 | MISSED | All MINOR. |

### 2B. Pipeline flags I assessed (including those outside my list)

| Pipeline flag | Assessment | Evidence |
|---|---|---|
| B05: fraud and KPMG forensic audit under-detailed on the Q1 call | SUPPORTED | Q1 FY27 [p8] L310-312, [p12-13] L495-517; filing 20260731 L46-93 (KPMG named). "Deepfake" wording comes from filing 20260706 L44-47 ("impersonate our KMPs"), not from the call. |
| B05: OCF/EBITDA ~140% "never reconciled" | OVERSTATED | Q4 FY26, Anant, [p10] L409-412 gives the reason: upfront billing in a growing business. The Q3 105-110% remark described a norm. It was not a promise. OCF above EBITDA is a favourable cash outcome. The open question is whether acquisitions add deferred revenue (see item 5). Calling it "Missed" is the wrong direction. |
| B05: aiRA metric basis inconsistent | SUPPORTED, but understated | See item 3. The bigger issue is the size regression, not the bucketing. |
| B05: concentration never named | SUPPORTED | Item 25. |
| B05: normalisation pattern | SUPPORTED | Item 17. |
| B06: Capillary "less candid" on AI risk than peers | OVERSTATED | Capillary named the disrupted segments: "system of engagement and the system of intelligence are definitely seeing... radical change", plus SMB exposure and seat-based pricing (Q3 FY26, Aneesh, [p9-10] L387-422). That is the same segmented defence B06 credits to NEWGEN. |
| B06 2E / risks_peers_raise: build-it-yourself (vibe-coding) risk "not named as a risk category anywhere in Capillary's own concalls" | NOT SUPPORTED | Q1 FY27, Achint: "can a AI-native company create what you have?" Aneesh answered at length on the moat ([p17-18] L694-717). Chintan Shah asked about in-house builds and Anant answered ([p21] L888-906). The risk was raised and rebutted on Capillary's own call. |
| B06 Q4 flag: M&A margin bridge "lands at single-digit margin, not 65-75%" (INTELLECT) | OVERSTATED (basis mismatch) | INTELLECT's "single digit margin business" (Feb-2026 L619-620) is an operating margin. Capillary's 65-75% is gross margin, and its stated post-migration contribution margin is 45% (Q4 [p12] L511). The quote is right. The comparison crosses bases. |
| B06 2E: NEWGEN Qatar claim "volunteered on-call" | OVERSTATED (minor) | An analyst raised it (NEWGEN Nov-2025, Sanjay Gupta, L621-625). Management then answered. |
| B06 Q6: INTELLECT "-60% development effort... major risk for the industry" | SUPPORTED | INTELLECT Aug-2026 L11815-11843 (token-per-line file). |
| B06 Q2: UNIECOM NRR "100%+" framed as routine | SUPPORTED, incomplete | UNIECOM May-2026 L517-521. B06 omits the "excluding the churn... top 10" qualifier (item 20). |
| B06 Q3: NEWGEN headcount -6% YoY | SUPPORTED | NEWGEN May-2026 L649. |
| B06 Q7: Capillary ~9-month deal cycle, 3-7 month go-live | SUPPORTED | Q1 FY27 [p23] L940; Q3 FY26 [p11] L481-482. |

---
## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 2A)

| # | B05 row | Earlier call contains the promise? | Later call shows the outcome? | Verdict |
|---|---|---|---|---|
| 1 | Q4: SessionM break-even Y1, positive Y2 → "Delivered, ahead of schedule" | Yes (Q4 [p12] L497-501) | Partly. "Fully profitable... break-even", with Rs 5-6 Cr free cash in 2 months (Q1 [p7] L270-273). The direction holds. "Ahead of schedule" overstates it: break-even was the Y1 promise, and 2 months of cash in an upfront-billing model is not EBITDA. | CONFIRMED (direction), with the qualifier overstated |
| 2 | Q4: Q1 FY27 margin softness from salary hikes → "Delivered, better than guided" | Yes (Q4 [p11] L447-450) | Softness did occur. Adjusted EBITDA margin went from ~19% in Q4 FY26 (Q4 [p6] L250-251) to 17% in Q1 FY27 (Q1 [p8] L316). B05 compares against Q1 FY26 (~10%), a YoY base the promise never used. | WRONG (the outcome matched the guide; it was not "better than guided") |
| 3 | Q3: OCF/EBITDA normalises to 105-110% → "Missed / unreconciled" | No promise. The Q3 statement describes a norm ([p9] L361-363). | FY26 ratio ~140%, with a reason given (Q4 [p10] L409-412) | WRONG (a non-promise scored as a miss; reason was given) |
| 4 | Q4: Kognitiv AI-led upgrade "12-to-18-month" → "Partial" | Yes, as a generic statement (Q4 [p6] L248-250) | First go-live Sep-2026, completion Sep-2027, and the generic cycle restated as "18 to 24-month" (Q1 [p11] L437-458) | CONFIRMED |
| 5 | Q4: FY27 revenue Rs 1,000-1,050 Cr → "On track / reaffirmed and sharpened" | Yes (Q4 [p12] L520-522) | "We will definitely beat our INR1,065 crores" (Q1 [p24] L977-979) | CONFIRMED |

Result: 5 checked, 3 confirmed, 2 wrong. Both wrong rows push B05's tally toward a harsher grade in one case (#3 adds a false "miss") and a kinder one in the other (#2 adds a false "beat"). The net effect on the B grade is small. The pattern still shows the tracker compares against bases the promise never used.

---
## PART 4: CREDIBILITY GRADE

B05 grades management B. **I would grade lower (B- to C+).** Management is consistent on direction and playbook. It is numerically loose across calls. Four material figures moved between calls without acknowledgement: aiRA size (item 3), SessionM ARR (item 4), platform gross margin (item 8), and organic growth (item 1). Two KPIs were re-based to show growth: ACV excluding one customer (item 9) and NRR excluding one customer (item 2). The track record is three quarters. The operator should weight the organic-growth and aiRA claims as asserted, not evidenced, until H1 FY27 filings split organic revenue at constant currency.

---
## PART 5: CONSOLIDATED FINDINGS

| Sev | Location | Finding |
|---|---|---|
| MAJOR | B05 1B guidance row; 4A trigger | Organic growth misreported ("20-23% incl. 6% currency" against the transcript's 23% incl. FX, i.e. ~17%). The Q1 ~11% constant-currency reading and the Rs 673 Cr organic plan arithmetic are absent (item 1). |
| MAJOR | B05 3B/3D | Healthcare customer contradiction between Q3 (+50% members, CY26 revenue bump) and Q1 (largest customer flat) not linked or flagged (item 2). |
| MAJOR | B05 1C, 2A | aiRA sizing read as rising. The Q4 "4-5% of revenues" statement is omitted. The numbers show a regression (item 3). |
| MAJOR | B05 3D | SessionM $35M (Q4) to $32M (Q1) not caught (item 4). |
| MAJOR | B05 1C, 2C | SessionM Rs 17 Cr "after debt true-up" contradicts the "debt-free entities" statement. The unexplained adjustment is scored as a transparency positive (item 5). |
| MAJOR | B05 4D | Kognitiv churn indemnity treated only as a normalisation item. The acquired-book retention signal is missed (item 6). |
| MAJOR | B05 2C | Gross margin contradiction across calls (69-70% platform in Q3 against organic >75% "for the last few quarters" in Q1) missed. B05 asserts the numbers were "repeated identically" (item 8). |
| MAJOR | B05 4A #6; 1B | New ACV +75% carried unqualified despite the single-customer base exclusion. The "30-40% more than FY26's Rs 121 Cr" anchor is not in the transcript (item 9). |
| MAJOR | B06 2E / risks_peers_raise | NOT SUPPORTED: the build-it-yourself AI risk was raised and rebutted on Capillary's Q1 FY27 call ([p17-18], [p21]). |
| MINOR | B05 timeline_slippages | SessionM 2-3 year migration horizon and the 12-18 to 18-24 month generic shift missing (item 7 residual). |
| MINOR | B05 2A row (Q1 margin softness) | Direction wrong: guided softness occurred (19% to 17%), so "better than guided" is wrong. |
| MINOR | B05 2A row, 4D flag (OCF/EBITDA) | Overstated. The Q4 call gave a reason, and the 105-110% remark was a norm, not a promise. |
| MINOR | B05 2A row (SessionM) | "Ahead of schedule" overstated. The evidence is 2 months of cash, not EBITDA (item 18). |
| MINOR | B06 flag 1 | AI-candour gap overstated. Capillary's Q3 answer names the disrupted segments. |
| MINOR | B06 Q4 / flag 3 | INTELLECT operating margin compared against Capillary gross margin (basis mismatch). |
| MINOR | B06 2E | NEWGEN Qatar claim was analyst-raised, not volunteered. |
| MINOR | B06 Q2 | UNIECOM NRR "ex top-10 churn" qualifier omitted. It parallels Capillary's ex-one-customer NRR (item 20). |
| MINOR | B05 (absent) | Margin-guide refusals on two calls (item 11). |
| MINOR | B05 (absent) | Tax narrative shifts every quarter (item 12). |
| MINOR | B05 (absent) | ROCE ~3% volunteered and reframed as CROIC 22% (item 13). |
| MINOR | B05 (absent) | FY25 growth disputed; gross-to-net accounting change (item 14). |
| MINOR | B05 (absent) | Product-mix shares exceed 100%; Insights monetisation statements conflict (item 15). |
| MINOR | B05 (absent) | D&A split question answered without the split (item 22). |
| MINOR | B05 (absent) | On-call unit and label errors (item 23). |
| MINOR | B05 (absent) | Headcount against cost-growth challenge (item 24). |

Counts: CRITICAL 0, MAJOR 9, MINOR 16.

---
## PART 6: SCORING

- Independent items: 25. Material (CRITICAL + MAJOR): 10. MINOR: 15.
- Status across all 25: CAUGHT 6, PARTIALLY CAUGHT 7, MISSED 12.
- Material items: CAUGHT 1 (#10), PARTIALLY CAUGHT 6 (#1, #3, #5, #6, #7, #9), MISSED 3 (#2, #4, #8).
- Counting rule for `material_caught`: the rubric defines PARTIALLY CAUGHT as "found but under-weighted or misclassified", so a partial counts as "already had". material_caught = 7, and acceptance_rate = 7/10 = 70%.
- Strict alternative, for the operator: count only items the pipeline flagged as a concern (CAUGHT plus the partials placed in a red-flag, slippage or caution note: #3, #7, #9). That gives 4/10 = 40%. Three of the six partials (#1, #5, #6) were recorded neutrally or framed as positive. The misclassifications carry their own MAJOR finding rows above, so they are not lost under the 70% figure.

```yaml
stage: B12b
company: "CAPILLARY"
run_date: "2026-09-19"
model: "claude-opus-5"
status: complete
independent_flags_found: 25
caught: 6
partially_caught: 7
missed:
  - {severity: "MAJOR", item: "Large healthcare customer contradiction: Q3 FY26 top-5 payer member base +50% with CY26 revenue bump vs Q1 FY27 largest (healthcare) customer did not grow, NRR 111% vs 116% ex it; never reconciled, identity unconfirmed", anchor: "Q3 FY26 Aneesh [p10-11] L432-449; Q1 FY27 Aneesh [p4] L166-167, [p18] L744-745; Anant [p21] L870"}
  - {severity: "MAJOR", item: "SessionM acquired base restated from $35M business / 40+ logos (Q4) to $32M ARR / 45-odd customers (Q1) without comment", anchor: "Q4 FY26 Aneesh [p5] L203, [p11] L468; Q1 FY27 Aneesh [p7] L266-269, [p9] L364"}
  - {severity: "MAJOR", item: "Gross margin statements contradict: Capillary platform 69-70% (Q3) vs organic >75% consistently for last few quarters (Q1); B05 says margin numbers repeated identically", anchor: "Q3 FY26 Aneesh [p6] L245, [p13] L558; Q1 FY27 Aneesh [p5] L195-198"}
  - {severity: "MINOR", item: "Margin trajectory guide declined on two consecutive calls (steady-state range given)", anchor: "Q3 FY26 Aneesh [p15] L652; Q4 FY26 Anant [p11] L456-459"}
  - {severity: "MINOR", item: "Tax narrative shifts each quarter (tax expense started / losses keep it negative / one-time DTL)", anchor: "Q3 FY26 [p8] L341-343; Q4 FY26 [p10] L418-420; Q1 FY27 [p8] L311"}
  - {severity: "MINOR", item: "ROCE about 3% volunteered, reframed as cash ROIC 22%", anchor: "Q4 FY26 Anant [p10] L414-416"}
  - {severity: "MINOR", item: "Management disputes reported FY25 growth (13% 'wrong', ~20% on net basis after gross-to-net accounting change)", anchor: "Q1 FY27 Aneesh [p18] L733-742"}
  - {severity: "MINOR", item: "Product-mix shares exceed 100% (loyalty ~90, Engage 5-7, Rewards 5-7, AI 4-5); Insights monetisation statements conflict", anchor: "Q4 FY26 [p4] L145-156, [p17] L719; Q1 FY27 [p3] L154-155"}
  - {severity: "MINOR", item: "UNIECOM NRR 100%+ is ex top-10 client churn, same ex-one-client normalisation Capillary uses; B06 omits qualifier", anchor: "UNIECOM May-2026 Kapil Makhija L517-519; Aug-2026 L557-558"}
  - {severity: "MINOR", item: "D&A split (acquisition intangibles vs capitalised tech) asked, answered without split", anchor: "Q3 FY26 Rishi/Anant [p11] L452-462"}
  - {severity: "MINOR", item: "On-call unit/label slips (142% as INR 142 crores; USD as INR million; PAT vs normalised PAT swapped)", anchor: "Q3 FY26 [p9] L363; Q4 FY26 [p11-12] L468, L514; Q1 FY27 [p8] L336-337"}
  - {severity: "MINOR", item: "Analyst challenge: headcount flat but costs growing near revenue; answered by US sales ramp", anchor: "Q4 FY26 Bharat Gulati/Aneesh [p15] L613-629"}
pipeline_flags_not_supported:
  - "B06 2E / risks_peers_raise: build-it-yourself (vibe-coding) AI risk 'not named as a risk category anywhere in Capillary's own concalls' - raised and rebutted on Q1 FY27 call (Achint [p17-18] L694-717; Chintan/Anant [p21] L888-906)"
promise_delivery_spot_checks: {checked: 5, confirmed: 3, wrong: 2}
credibility_grade_concur: "lower (B- to C+): direction and playbook consistent, but aiRA size, SessionM ARR, platform gross margin and organic growth moved between calls unacknowledged, and ACV/NRR re-based by excluding one customer; 3-quarter record"
findings:
  - {severity: "MAJOR", location: "B05 1B guidance row, 4A", claimed: "full-year organic growth 20-23% incl ~6% currency; Q1 organic +17%", source_truth: "Aneesh final: 23% incl ~6% FX = ~17% organic (Q1 FY27 [p18] L742-747); analyst ~11% Q1 organic (L727-731); FY27 plan organic ~Rs 673 Cr vs FY26 acquisition-linked Rs 80-100 Cr of 735 implies +3-6% [INFERENCE] (Q1 [p11] L464-469; Q4 [p11] L463-465)", note: "organic growth rate unresolved; separating observation = H1 FY27 constant-currency organic revenue"}
  - {severity: "MAJOR", location: "B05 3B/3D", claimed: "healthcare member step-up (Q3) and flat large account (Q1) cited separately", source_truth: "Q3 FY26 [p10-11] L432-449 vs Q1 FY27 [p4] L166-167, [p18] L744-745", note: "contradiction not linked or flagged; identity of account unconfirmed"}
  - {severity: "MAJOR", location: "B05 1C, 2A aiRA", claimed: "quantification rising each quarter", source_truth: "Q4: few million $ and 4-5% of revenues from AI stack, not all live (Q4 [p4] L155, [p17] L719-720); Q1: $2-2.5M run-rate, <10 paying (Q1 [p10] L393, [p19] L782, [p6] L239-240)", note: "sizing regressed; Q4 4-5% of Rs 734 Cr = Rs 29-37 Cr vs ~Rs 21-28 Cr implied by management's own Rs17Cr=$1.5-2M pairing [INFERENCE]"}
  - {severity: "MAJOR", location: "B05 3D", claimed: "SessionM $32m ARR retained, no surprises", source_truth: "Q4 FY26: $35 million business, 40 plus logos ([p5] L203)", note: "restatement not caught; benign reading = revenue vs ARR basis"}
  - {severity: "MAJOR", location: "B05 1C, 2C", claimed: "$20m gross / Rs 17 Cr net after debt true-up; transparency positive", source_truth: "Anant: adjusted for net debt items; Aneesh: no debt, debt-free entities (Q1 FY27 [p22] L911-921)", note: "~$18M non-debt adjustment unexplained; payback claim rests on Rs 17 Cr ([p7] L279-285)"}
  - {severity: "MAJOR", location: "B05 4D", claimed: "Kognitiv indemnity income = one of recurring normalisations, Low", source_truth: "churn indemnity Rs 25 Cr triggered as seller failed agreed commitments (Q4 FY26 Anant [p9-10] L396-399); inorganic NRR 96% to 94%", note: "acquired-book retention signal missed"}
  - {severity: "MAJOR", location: "B05 2C", claimed: "margin playbook numbers repeated identically across all three calls", source_truth: "platform GM 69-70% (Q3 [p6] L245) vs organic >75% for last few quarters (Q1 [p5] L197-198)", note: "direct input to 26.2 margin bridge"}
  - {severity: "MAJOR", location: "B05 4A trigger 6, 1B", claimed: "new ACV +75% ex one account; FY27 30-40% more than FY26 Rs 121 Cr", source_truth: "FY26 ACV Rs 121 Cr similar to LY (Q4 [p9] L390-391); +75% only ex one customer (Q1 [p8] L326-330); 30-40% guide base unstated (Q1 [p23] L944-946)", note: "selective base exclusion not flagged; Rs 121 Cr anchor not in transcript"}
  - {severity: "MAJOR", location: "B06 2E, risks_peers_raise", claimed: "vibe-coding/build-it-yourself risk not named anywhere in Capillary concalls", source_truth: "Q1 FY27 Achint/Aneesh [p17-18] L694-717; Chintan/Anant [p21] L888-906", note: "NOT SUPPORTED"}
  - {severity: "MINOR", location: "B05 timeline_slippages", claimed: "Kognitiv slippage only", source_truth: "SessionM upgrades 2-3 years, not starting till end of year (Q1 [p9] L359-362); generic cycle 12-18 to 18-24 months (Q4 [p6] L248-250; Q1 [p11] L454-455)", note: "partial capture"}
  - {severity: "MINOR", location: "B05 2A Q1 margin softness row", claimed: "delivered, better than guided", source_truth: "adj EBITDA margin ~19% Q4 FY26 (Q4 [p6] L250-251) to 17% Q1 FY27 (Q1 [p8] L316)", note: "guided softness occurred; YoY base misapplied"}
  - {severity: "MINOR", location: "B05 2A row, 4D flag OCF/EBITDA", claimed: "missed / never reconciled", source_truth: "Q4 FY26 Anant: bill and collect upfront in growing business ([p10] L409-412); Q3 105-110% was a norm, not a promise", note: "OVERSTATED"}
  - {severity: "MINOR", location: "B05 2A SessionM row", claimed: "delivered, ahead of schedule", source_truth: "break-even was the Y1 promise (Q4 [p12] L497-501); evidence is Rs 5-6 Cr cash in 2 months (Q1 [p7] L270-273)", note: "cash not EBITDA in upfront-billing model"}
  - {severity: "MINOR", location: "B06 flag 1, Q6", claimed: "Capillary less candid on AI risk than peers", source_truth: "Q3 FY26 Aneesh names disrupted segments, SMB, seat-based pricing ([p9-10] L387-422)", note: "OVERSTATED"}
  - {severity: "MINOR", location: "B06 Q4, flag 3", claimed: "INTELLECT playbook lands at single-digit margin, not 65-75%", source_truth: "INTELLECT single-digit is operating margin (Feb-2026 L619-620); Capillary 65-75% is gross, 45% contribution (Q4 [p12] L511)", note: "basis mismatch"}
  - {severity: "MINOR", location: "B06 2E NEWGEN Qatar", claimed: "volunteered on-call", source_truth: "raised by analyst Sanjay Gupta (NEWGEN Nov-2025 L621-625)", note: "OVERSTATED"}
  - {severity: "MINOR", location: "B06 Q2", claimed: "UNIECOM NRR 100%+", source_truth: "above 100% excluding churn of top-10 client (UNIECOM May-2026 L517-519)", note: "qualifier omitted; parallels Capillary ex-one-customer NRR"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "margin-guide refusals Q3 [p15] L652, Q4 [p11] L456-459", note: "item 11"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "tax narrative Q3 [p8] L341-343; Q4 [p10] L418-420; Q1 [p8] L311", note: "item 12"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "ROCE ~3% / CROIC 22% Q4 [p10] L414-416", note: "item 13"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "FY25 growth disputed, gross-to-net Q1 [p18] L733-742", note: "item 14"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "mix >100% Q4 [p4] L145-156, [p17] L719", note: "item 15"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "D&A split unanswered Q3 [p11] L452-462", note: "item 22"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "unit/label slips Q3 L363; Q4 L468, L514; Q1 L336-337", note: "item 23"}
  - {severity: "MINOR", location: "B05 absent", claimed: "", source_truth: "headcount vs cost challenge Q4 [p15] L613-629", note: "item 24"}
critical_count: 0
major_count: 9
minor_count: 16
material_found: 10
material_caught: 7
acceptance_rate: 70
coverage_basis: "10 material (0 CRITICAL, 10 MAJOR) of 25 listed; material: 1 caught, 6 partially caught (counted as caught per rubric 'found but under-weighted or misclassified'), 3 missed = 7/10. Strict alternative (only partials the pipeline flagged as a concern: #3, #7, #9) = 4/10 = 40%. 3 company transcripts read in full; 12 peer transcripts searched; INTELLECT May/Aug .txt are one-word-per-line, token search only."
```
