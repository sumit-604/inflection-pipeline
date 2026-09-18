# Stage 12 Verifier B: Concall Red Flags, TRUALT
Run date: 2026-09-18. Model: claude-opus-5. Fresh context.

Inputs read: 4 main-company transcripts (Q2 FY26 Nov-2025, Q3 FY26 Feb-2026,
Q4 FY26 May-2026, Q1 FY27 Aug-2026), 12 peer transcripts (GULPOLY x4,
BALRAMCHIN x4, TRIVENI x4), B05 report and block, B06 report and block. No
other output file opened. Anchors use the "[page N]" marker in each .txt,
which is the PDF page. Where the transcript prints a different "Page X of Y",
the PDF page governs.

Method. I read all four TruAlt transcripts end to end before opening B05 or
B06. I read GULPOLY x4, TRIVENI Aug and BALRAMCHIN Jun end to end, and read
the other peer transcripts by targeted search (allocation, tender, court,
private OMC, overcapacity, subvention, SAF, CBG, DDGS, maize, standalone,
diversion) with context. Then I compared.

Scope note. B05 cites three numbers from non-transcript artifacts (36.85%
pledge from the Jun-2026 SHP, 72.6% related-party purchases from the AR,
FY26 CFO of -Rs 296.15cr). These are outside my inputs. I do not assess them.

---

## PART 1: INDEPENDENT RED-FLAG LIST (from the transcripts alone)

Severity is graded before comparison. "MD" = Vijaykumar Nirani, "CFO" = Anand
Kishore.

### 1A. Main company (TruAlt), material items

| ID | Sev | Item | Anchor (call, speaker, page) |
|---|---|---|---|
| M1 | CRITICAL | Allocation "done deal" that was already cut. Nov: "47 is a done deal", built from "34 crores liters from the government OMCs" plus 4 + 1.8 private plus "potential to make up to 8 crores liters of extra neutral alcohol". The 47 included uncontracted ENA potential. May: PSU award "about 26 crore litres against a bid of 72". May, same call, a third figure: "30 crore litres was given to us". The MD dates the cut himself: "in November, they came around and decreased the allocation". So the Nov 13 claim and the Feb reaffirmation of 36-37 cr L both came after the cut. Asked in May why investors were not told: "Even now, the mechanism hasn't changed." Non-answer. Pattern spans three calls. | Nov, MD, [page 10], [page 15]; May, MD, [page 4], [page 10], [page 11], [page 26] |
| M2 | MAJOR | Shutdown cause told two ways. Nov: "intentional shutdown", "we have intentionally shut down three out of the four". Feb, to explain the court extension: "beyond our control... force majeure... extreme rainfall". Feb also: "unfortunately we delayed the setting up of the grain plants". | Nov, MD, [page 10], [page 24]; Feb, MD, [page 11] |
| M3 | MAJOR | FY26 volume guidance collapse with internal contradictions. Nov: target cut 41 to 36-37; same call, MD says Q3+Q4 "26 to 28 crores liters" while CFO says Q3+Q4 "around 22 crores". Feb: 36-37 held; when Deepak Poddar shows the math does not close, MD cites stock of "4 and a half 4.2, around 5 crores liters 5.2" and CFO adds "sale in transit". Actual: 24 (MD) or 26 (CFO). | Nov, MD/CFO, [page 18], [page 19], [page 22]; Feb, MD/CFO, [page 18]; May, MD [page 10], CFO [page 25] |
| M4 | MAJOR | Feb run-rate stated as present fact ("all ethanol plants are now fully operational with a monthly revenue run rate of approximately INR350 crores to INR400 crores"), after the allocation cut. May actual: "run rate of 2.2 crore litres... capacity utilization to less than 35%". Challenged by Vedant Sarda, MD recasts it as "potential". Closing apology: "could not... demonstrate the growth that we had already promised". | Feb, MD, [page 4]; May, MD, [page 5], [page 26]-[page 27], [page 29] |
| M5 | MAJOR | Private-OMC price told two ways, and contracts not honoured. Feb: private OMCs "give a little higher than the government pricing". May: TruAlt offered "INR60 point change"; OMCs "went back on the already executed purchase orders"; 1.6 of 8 cr L lifted; "almost become like an oligarchy". Aug: "about INR60.50". | Feb, MD, [page 21]; May, MD, [page 4], [page 12], [page 25]-[page 26]; Aug, MD, [page 22] |
| M6 | CRITICAL | 15 cr L court quantity, repeated slippage across four calls. Nov: "not... easily... work in progress". Feb: "I'm sure they will come through"; CFO "timeline will be difficult to tell". May: 90-day window lapsed, OMCs "in contempt", now "within September or H1". Aug: "not able to give a timeline". | Nov [page 10]; Feb [page 11]-[page 12]; May [page 11]-[page 12]; Aug [page 9], [page 21] |
| M7 | MAJOR | Retail rollout: the same near-term addition promised every call. Nov: 7 open, "six more are ready to commence shortly". Feb: "four additional stations underway", 75 by "31st March", CFO corrects to calendar year. May: 4 more "in the next three months". Aug: "another four to be commissioned hopefully by the end of this quarter". Still 7. | Nov [page 4]; Feb [page 5], [page 17]; May [page 7], [page 18]; Aug [page 4] |
| M8 | MAJOR | CBG timeline and count drift, including a construction-start contradiction. Nov: "construction has begun on three plants". Feb: "four more plants which began construction in December". Commission date: "end of Q2 FY'27" (Nov p.3), "July of 2026" (Nov p.19), "June 2026" (Feb p.19), Q3/Q4 FY27 (May, Aug). Counts: 17 more (Nov), 24 (Feb), 10 plus 4 (May). Sumitomo plants: 16 (Nov), 12 (Feb), 4 then 3 (May). Plant size: "20 tons each" vs "four plants of 80 TPD each" (Nov); GAIL 12 TPD (Feb, May) vs "10 TPDs each" (Aug). | Nov, MD, [page 3], [page 12], [page 19]; Feb, MD, [page 4], [page 9], [page 18]-[page 19]; May [page 6], [page 12]; Aug [page 7] |
| M9 | MAJOR | SAF slip and FID condition reversed. Feb: "investment strategy is structured based on offtake guarantees before we commit on ground investments". May: FID "as soon as we achieve a long-term offtake agreement"; commission "24 to 30 months... That's FY29". Aug: capex to "begin as early as... next two or three months", offtake still "in the working groups", land still to be procured. | Feb, MD, [page 15]; May, MD, [page 7], [page 29]; Aug, MD, [page 4], [page 7], [page 9] |
| M10 | MAJOR | Government incentives inside revenue and EBITDA. May CFO: "the operating income also included the production link incentive... add the PLI and interest subvention". Aug CFO: "interest subventions and PLI all together around INR22 crores"; core ethanol margin "about 9% to 9.5%". Nov: grant receivable "INR 107 crores... PLI and interest subvention to be receivable from the NABARD". | Nov, CFO, [page 9]; May, CFO, [page 13]; Aug, CFO, [page 18] |
| M11 | MAJOR | Q1 FY27 margin is an inventory gain. At current maize ~Rs 25.50, "margins come down drastically... INR6 to INR7 a litre" vs Rs 15-16 on stock bought at Rs 17-22. "Since we are still sitting on a lot of volumes... next quarter and hopefully Q3". Volunteered. | Aug, MD, [page 8], [page 18] |
| M12 | MAJOR | Prior-period restatement. Rs 10.5cr Rule 43 GST reversal under Ind AS 8, "an oversight from our the tax consultants". MD frames the cost as a lost gain ("could have increased our PAT margin by INR4 crores... INR89 crores... INR93 crores"). Prompted by Shubh Gala. | Aug, CFO/MD, [page 20] |
| M13 | MAJOR | Unsold inventory. "Inventory of almost about INR460 close to INR500 crores"; "having the inventory we're unable to sell". Set against "more than INR1,100 crores of capital in hand to secure feedstock". | May, MD, [page 11], [page 15], [page 27] |
| M14 | MAJOR | Stock-in-trade question dodged. Pratham Modi asks about "the recent increase in purchase of stock in trade" (an accounting line). MD answers as if about share price: "I should have to ask the investor community". The trading-purchase question stays open. | Feb, MD, [page 12] |
| M15 | MAJOR | Group sourcing told two ways, with long group payables. May: group "less than 55%", falling; payables to group "may go to two, three months". Aug: group "can assure us 100% of the required raw material". | May, MD/CFO, [page 18]-[page 19]; Aug, MD, [page 24] |
| M16 | MAJOR | Q1 FY27 utilisation promise missed; maintenance plan reversed. Feb: "80% capacity use for Q1"; "Q2 usually is our downtime. So 2 months is scheduled maintenance". Aug: "only operate at about 60%"; "we don't have plans to stop for maintenance". | Feb, MD, [page 13]; Aug, MD, [page 3], [page 23] |
| M17 | MAJOR | FY27 volume walk-down. Feb: "performance litmus test... 55 crores liters". May: "at least minimum 40 crore litres. And a bonus... 55"; CFO: "We cannot tell you the figure of FY 2027". Aug: "44 crores litres of orders on hand", said to include OMC, private, ENA, and to exclude the 15. 26 + 8 + 6 = 40, not 44. | Feb [page 19]; May [page 19], [page 23]; Aug [page 8], [page 9] |
| M18 | MAJOR | CBG ownership. GAIL took 49% of Leafiniti, which holds the one profitable plant. TGPL called "a wholly-owned subsidiary" in the same call Sumitomo is "a 49% JV partner". Aug: TruAlt will report "51%" of gross revenue. | May, MD, [page 6], [page 20]; Aug, MD, [page 16] |
| M19 | MAJOR | Promoter pledge. Nov: 26% re-pledged as a sanction term. Aug: CFO answer is circular ("this loan is not against the pledged share, that is collateralized... this share is given as a collateral against the loan"); release "hopefully in this quarter". | Nov, CFO, [page 17]-[page 18]; Aug, CFO/MD, [page 14]-[page 15] |
| M20 | MAJOR | De-leveraging promised without content. Finance cost ~Rs 180cr/yr raised by Parth Shah; MD: plan "in the next call or maybe in the next few days", repeated. Shareholder: "share price are not going anywhere from the listing day". No form (equity, asset sale) named. | Aug, MD, [page 22]-[page 23] |
| M33 | MAJOR | Feedstock split deferred twice to the same analyst. Nov (allocation split): "Allow me to have that sent to you over mail". May (volume split): "We'll share it with you offline"; CFO "I don't have right now". Given in Aug to Sanjay Manyal. | Nov, MD, [page 15]; May, MD/CFO, [page 25]; Aug, CFO, [page 8] |

Why M33 is MAJOR, not CRITICAL. The deferral is real and repeated. But the
data was given in Aug, and a peer withholds the same split as policy (TRIVENI
Nov, Tarun Sawhney: "I'm afraid we don't give a breakup of what we've got,
maize v/s rice", [page 10]). Thesis weight is lower than M1 or M6.

### 1B. Main company, minor items

| ID | Sev | Item | Anchor |
|---|---|---|---|
| M21 | MINOR | Mid-call number corrections: H1 volume "9 crores" then "5.7"; DDGS "78 crores" then "INR28 crores"; Q3 volume 7.6 vs 7.8; Q1 8.5 vs 8.29. | Nov [page 22]; May [page 15]; Feb [page 8], [page 16]; Aug [page 3], [page 23] |
| M22 | MINOR | CBG margin figures inconsistent in one call: 68.29% EBITDA (CFO), "60% to 65% minimum" (CFO), "40% to 45%" (MD), "55% to 60%" (CFO). | Nov [page 6], [page 21]-[page 22] |
| M23 | MINOR | Revenue-mix answer flips mid-answer: "70%-odd... 20%-odd to 25%" then "No, sorry. 85 and 15". | Nov, MD, [page 24] |
| M24 | MINOR | Nov CFO: shut plants "already operational from Q3... we have already completed the COD". Feb: Unit 5 CTO only on 17-Dec-2025, 58 operating days, "almost about 30 days we lost during the start of Q3". | Nov [page 7]; Feb [page 3]-[page 4], [page 11] |
| M25 | MINOR | Disclosure policy used selectively. "I've been advised... we are not allowed to project... My company secretary sitting next to me is nudging me", after and before giving detailed volume, margin and capex numbers. | Feb, MD, [page 18]; May, CFO, [page 19] |
| M26 | MINOR | Demand-supply framing reversed on the same numbers: "already an oversupply" (Nov) vs "almost at par" (Aug). | Nov [page 22]; Aug [page 24] |
| M27 | MINOR | Retail PAT-margin question answered with CBG hiring and finance cost. Retail margin 2% (Feb CFO) vs "EBITDA of about 5%" (May MD). | Aug [page 10]; Feb [page 17]; May [page 7] |
| M28 | MINOR | CBG utilisation "85% plus" (May) to "about 78%" (Aug). EBITDA dip: CFO "there is nothing driving this", then employee cost and a one-time R&M. | May [page 5]; Aug [page 6], [page 10] |
| M29 | MINOR | May promises of more investor interaction and marketing; Aug follow-up shows advertising not started ("certain delays"). | May [page 20], [page 23]; Aug [page 22] |
| M30 | MINOR | ENA plan 6 cr L at Rs 62-63; price fell to Rs 55-56; actual about 3 cr L. | May [page 4], [page 14]-[page 15] |
| M31 | MINOR | DDGS Q4 guide Rs 70-80cr (softened same call) vs about Rs 28cr. | Feb [page 10], [page 16]; May [page 23] |

### 1C. Peer statements that bear on the main company

| ID | Sev | Item | Anchor |
|---|---|---|---|
| P1 | MAJOR | The ESY 25-26 allocation shortfall was public before TruAlt's Nov 13 "done deal". TRIVENI: "1,776 that was tendered for the OMCs against the 1,048" and pressure on "standalone distillers, especially processing maize". GULPOLY (11-Nov): 17.5 cr L received vs 23 cr L capacity. | TRIVENI Nov, Tarun Sawhney, [page 5]-[page 6]; GULPOLY Nov, Aditi Pasari, [page 8]-[page 9] |
| P2 | MAJOR | Peers keep incentives out of EBITDA or book them only on receipt. BALRAMCHIN CFO: "incentives are largely in the form of capital subsidy and interest subvention. So, both these items are below EBITDA". GULPOLY: subsidies booked "on receipt basis only", none in Q1 FY27 P&L; ISS "not received... more than one and a half years", provision reversed. TruAlt carries about Rs 22cr of subvention plus PLI in Q1 FY27 ethanol EBITDA and a Rs 107cr grant receivable. TruAlt's 20-23% EBITDA is not like-for-like with peers, and accrual collectability is a live risk. | BALRAMCHIN Jun, Pramod Patwari, [page 10]; GULPOLY Aug, Rajiv Gupta, [page 14]; GULPOLY Feb, Aditi Pasari, [page 13]; TruAlt Aug [page 18], Nov [page 9] |
| P3 | MAJOR | Sugary-feedstock diversion may be restricted in ESY 26-27. BALRAMCHIN: "it is reasonable to assume that there will be no diversion allowed towards B and juice". TRIVENI: allocation of sugary feedstocks as "one additional lever", grain to sugar "3:1" next year. TruAlt Q1 FY27: 4.37 of 8.29 cr L sugar-based, 3.35 cr L B-molasses; two monofeed units; plan to run all five plants "on syrup for 100 days". TruAlt never raises this risk and guides 44 cr L plus. | BALRAMCHIN Aug, Vivek Saraogi, [page 4]; TRIVENI Aug, Tarun Sawhney, [page 5]-[page 7]; TruAlt Aug [page 8], May [page 16] |
| P6 | MAJOR | Standalone distilleries at 20-50% utilisation face solvency stress as interest moratoriums expire. TruAlt runs a standalone distillery model at 35-60% utilisation and never applies this to itself. | TRIVENI Aug, Tarun Sawhney, [page 11]; BALRAMCHIN Feb analyst, [page 6] |
| P4 | MINOR | GULPOLY: private refiners "always are looking at getting the cheapest ethanol". This contradicts TruAlt's Feb claim that private OMCs pay above government price and supports its May/Aug Rs 60-60.50. | GULPOLY Nov, Aditi Pasari, [page 8] |
| P7 | MINOR | Maize rise magnitude disputed: TRIVENI "not been even double-digit... medium, single digit"; GULPOLY Rs 23-25 now; TruAlt Rs 17-22 to 25.50. | TRIVENI Aug [page 12]; GULPOLY Aug [page 9]; TruAlt Aug [page 8] |
| P8 | MINOR | GULPOLY can hold only 30-45 days of grain at 3,000 t/day. TruAlt claims cheap grain bought Oct-Feb will carry margins into Q2-Q3 FY27. The claimed stock depth is unusual and ties to the Rs 460-500cr inventory. | GULPOLY Aug [page 8]-[page 9]; TruAlt Aug [page 18] |
| P9 | MINOR | Peer view split on SAF readiness: GULPOLY "technology for SAF... has yet not been established"; TRIVENI notes ATF norms now include ethanol-to-jet. | GULPOLY Feb [page 11]-[page 12]; TRIVENI Jun [page 7] |
| P10 | MINOR | GULPOLY says its dedicated-ethanol status gives "priority allocation" and got 78%. TruAlt claims LTOA status ("already under a long-term offtake engagement") yet got 26 of a 72 cr L bid. TruAlt's bid used 365-day capacity; its own operating capacity is 55-60. The 34% hit rate is not like-for-like with peers. | GULPOLY May [page 3], [page 14]; TruAlt May [page 4], Aug [page 12] |
| P11 | MINOR | The Karnataka litigation stalled national tender cycles 2-4 (TRIVENI Feb, Jun). TruAlt frames the year as "unfair allocation" only; the same litigation also blocked the extra cycles that could have lifted its volume. | TRIVENI Feb [page 5]; TRIVENI Jun [page 4] |

Totals: 42 items. Material (CRITICAL + MAJOR): 25 (2 CRITICAL, 23 MAJOR).
Minor: 17.

---

## PART 2: COMPARISON AGAINST B05 AND B06

### 2A. My items vs the pipeline

| ID | Sev | Status | Pipeline location / gap |
|---|---|---|---|
| M1 | CRITICAL | PARTIALLY CAUGHT | B05 4D [HIGH], 2B, 1C. Under-weighted: rated HIGH, not CRITICAL. Misses the MD's own May statement that the cut came "in November" (so the done-deal claim post-dated the cut), the third allocation figure (30 cr L), and that the 47 included 8 cr L of uncontracted ENA potential. |
| M2 | MAJOR | CAUGHT | B05 4D [HIGH], 2B. |
| M3 | MAJOR | CAUGHT | B05 2A rows, 4D [LOW-MEDIUM] 24 vs 26, 3C Deepak Poddar. The Nov CFO 22 vs MD 26-28 contradiction is not named, but the miss and the stock-math answer are. |
| M4 | MAJOR | CAUGHT | B05 3C (Vedant Sarda). |
| M5 | MAJOR | CAUGHT | B05 4D [HIGH], 3C, 3D. |
| M6 | CRITICAL | CAUGHT | B05 2E, 2A, timeline_slippages, trigger 1 kill signal. |
| M7 | MAJOR | CAUGHT | B05 2E, 2A. |
| M8 | MAJOR | PARTIALLY CAUGHT | B05 1B, 1C, 2A cover date slip, count drift and TPD drift. Missing: Nov "construction has begun on three plants" vs Feb "began construction in December". |
| M9 | MAJOR | CAUGHT | B05 4D [HIGH]. B05 anchors the offtake-first condition to May only; Feb [page 15] states it first. |
| M10 | MAJOR | CAUGHT | B05 4D [MEDIUM], 1B. |
| M11 | MAJOR | CAUGHT | B05 4D [MEDIUM], analyst note. |
| M12 | MAJOR | CAUGHT | B05 4D [MEDIUM]. |
| M13 | MAJOR | CAUGHT | B05 4D [MEDIUM]. |
| M14 | MAJOR | PARTIALLY CAUGHT | B05 2C, 3C, 4C name the deflection but it is absent from the 4D red-flag list and the YAML red_flags. |
| M15 | MAJOR | CAUGHT | B05 4D [MEDIUM]. |
| M16 | MAJOR | CAUGHT | B05 4D [MEDIUM], 2A. |
| M17 | MAJOR | CAUGHT | B05 4D [MEDIUM], dropped_triggers. |
| M18 | MAJOR | CAUGHT | B05 4D [MEDIUM-HIGH]. |
| M19 | MAJOR | CAUGHT | B05 4D [MEDIUM]. |
| M20 | MAJOR | CAUGHT | B05 1A, 1C. |
| M33 | MAJOR | CAUGHT | B05 4D [CRITICAL], 2E. |
| P1 | MAJOR | CAUGHT | B06 Q1 net read (TRIVENI Nov data before TruAlt's done deal). |
| P2 | MAJOR | PARTIALLY CAUGHT | B06 Q6 treats schemes as a sector-wide dependency. It never states that BALRAMCHIN classifies subvention below EBITDA or that GULPOLY books on receipt, so the EBITDA comparability and accrual-risk contrast is missing. B06 also attributes GULPOLY's "below 5%" ISS line to BALRAMCHIN (see 2C). |
| P3 | MAJOR | MISSED | Not in B05 or B06. |
| P6 | MAJOR | CAUGHT | B06 2E, risks_peers_raise. |
| M21 | MINOR | CAUGHT | B05 4D [LOW]. |
| M22 | MINOR | MISSED | |
| M23 | MINOR | MISSED | |
| M24 | MINOR | MISSED | |
| M25 | MINOR | MISSED | |
| M26 | MINOR | CAUGHT | B05 4D [LOW]; B06 Q4. |
| M27 | MINOR | MISSED | |
| M28 | MINOR | MISSED | |
| M29 | MINOR | MISSED | |
| M30 | MINOR | MISSED | B05 3D gives ENA 3 cr L at Rs 62 as data but not the plan miss or price fall. |
| M31 | MINOR | CAUGHT | B05 2A, 4D. |
| P4 | MINOR | PARTIALLY CAUGHT | B06 Q2 quotes GULPOLY but keeps UNVERIFIABLE. The line contradicts TruAlt's Feb claim directly. |
| P7 | MINOR | CAUGHT | B06 2B. |
| P8 | MINOR | MISSED | |
| P9 | MINOR | MISSED | |
| P10 | MINOR | MISSED | B06 Q1 compares hit rates without noting TruAlt's 365-day bid denominator or its LTOA claim. |
| P11 | MINOR | CAUGHT | B06 2A, 2E. |

Counts. All 42 items: 25 caught, 5 partially caught, 12 missed. Material
25: 20 caught, 4 partially caught, 1 missed.

### 2B. Pipeline red flags I assessed against the transcripts

All B05 4D flags appear in my list except the utilisation-denominator item,
which I assessed separately.

| Pipeline flag | Assessment |
|---|---|
| B05 [CRITICAL] grain/sugar split evasion | SUPPORTED on facts. Severity OVERSTATED: data given in Aug; TRIVENI withholds the same split as policy. MAJOR fits. |
| B05 [LOW] utilisation on three bases | SUPPORTED. The 95%/60% pair is reconciled in the same Feb passage ([page 4]); the <35% is the May run-rate ([page 5]). |
| B05 [MEDIUM-HIGH] 51% revenue consolidation | SUPPORTED. The analyst said "report 51% of the gross revenue" and the MD confirmed "51%" ([page 16]). B05's Ind AS reading is an inference; the MD may mean attributable share. Keep it as a question to resolve. |
| B05 1C "162 TPD vs 142 TPD" | SUPPORTED. 10 + 3x20 + 6x12 = 142 for the 10 plants named; 162 needs the disputed 4th Sumitomo plant. |
| B06 Q4 demand-supply CONTRADICTED | SUPPORTED. TRIVENI Aug [page 10]-[page 11], TRIVENI Nov [page 6], BALRAMCHIN Jun [page 11], and GULPOLY May [page 15] ("more than 2,000 crore liters") all describe excess capacity. |
| B06 Q1, Q3 PARTIALLY VERIFIED | SUPPORTED. |
| B06 Q2, Q5 UNVERIFIABLE | Q5 SUPPORTED. Q2 is conservative; see P4. |
| B05 36.85% pledge, 72.6% RPT, CFO -296cr | Outside transcript scope. Not assessed. |

No pipeline red flag is NOT SUPPORTED as an invented signal. Two supporting
attributions are wrong (2C).

### 2C. Anchor and attribution errors found during the comparison

- B06 Q6: "BALRAMCHIN references NABARD-linked interest subvention as the
  reason its long-term debt carries an effective rate below 5%". The line is
  GULPOLY's CFO Rajiv Gupta (GULPOLY May [page 6]). No BALRAMCHIN transcript
  says "below 5%". The relevant BALRAMCHIN statement (subvention below EBITDA,
  Jun [page 10]) is not used.
- B06 "corrects" the BALRAMCHIN overcapacity quote from p.11 to p.10. The
  quote sits under the [page 11] marker (printed "Page 10 of 12"). By the
  pipeline's PDF-page rule, p.11 was right.
- B06 Q3 cites GULPOLY Aug "p.4 and p.8" for the 10-11% guide. The first
  instance is at [page 5].
- B05 1C: "Raised only after an analyst push (Tanmay Javeri)" for
  de-leveraging in May. Tanmay Javeri asked about CBG funding mix and
  one-on-one meetings (May [page 20]). De-leveraging was raised by Parth Shah
  in Aug only.
- B05 page anchors one page off: Feb 36-37 cr L exchange is [page 11], not
  p.10; May "49% JV partner" and GAIL "as of March 2026" are [page 6], not
  p.5; Nov 80-85% utilisation is [page 18], not p.17.

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (B05 section 2A)

| # | B05 row | Earlier call contains promise? | Later call shows outcome? | Verdict |
|---|---|---|---|---|
| 1 | FY26 volume 36-37 cr L, Missed | Yes. Feb, MD, [page 11] ("revised production of about 36 to 37"); also Nov [page 22]. | Yes. May: 24 (MD [page 10]), 26 (CFO [page 25]). | Direction CONFIRMED. Anchor p.10 should be p.11. |
| 2 | Q4 DDGS Rs 70-80cr, Missed | Yes. Feb, MD, [page 10]. | Yes. May, MD, [page 23]: "about INR28 crores" (asked for FY26 and Q4). With Q3 at Rs 18cr (Feb [page 10]), Q4 is about Rs 10cr if 28 is the full year. | CONFIRMED. |
| 3 | Q1 FY27 utilisation 80%, Missed | Yes. Feb, MD, [page 13]. | Yes. Aug, MD, [page 3]: "about 60%". | CONFIRMED. |
| 4 | 4 Sumitomo plants by June 2026, Missed | Yes. Feb, MD, [page 19]. | Yes. May [page 12] 3 of 4; Aug [page 3]-[page 4] "near commissioning". | CONFIRMED. |
| 5 | GAIL infusion in February, Partial | Yes. Feb, MD, [page 4]. | Yes. May, MD, [page 6]: "as of March 2026". | CONFIRMED. Anchor p.5 should be p.6. |
| 6 | Q3+Q4 26-28 cr L, Missed, "actual roughly 18-20" | Yes. Nov, MD, [page 18]. | Q3 7.6-7.8 (Feb [page 8], [page 16]); Q4 "around 6 crore litres" (May CFO [page 25]). Sum about 13.6-13.8. | Direction CONFIRMED. Magnitude WRONG: 18-20 comes from subtracting H1 from a disputed full-year figure and does not match the quarterly figures. Also the promise was production and the outcomes are sales. |

Checked 6, direction confirmed 6, direction wrong 0. One magnitude error and
two page-anchor errors.

---

## PART 4: CREDIBILITY GRADE

B05 grade: D. I concur. On my check, 8 of 11 tracked promises were missed and
2 were partial. The MD dates the allocation cut to November while the Nov and
Feb calls sold a settled volume. The same shutdown was "intentional" to
investors and "force majeure" to a court. The positives are operational
(multi-feed delivered, CBG plant economics, VGF secured, a straight answer on
the 9-9.5% core margin). They do not offset the disclosure record.

---

## PART 5: CONSOLIDATED FINDINGS

| Sev | Finding |
|---|---|
| MAJOR | MISSED: sugary-feedstock diversion restriction risk for ESY 26-27 (BALRAMCHIN Aug [page 4]; TRIVENI Aug [page 5]-[page 7]). About 53% of TruAlt Q1 FY27 volume was sugar-based, two units are monofeed, and FY27 guidance assumes 100 syrup days. Neither B05 nor B06 carries it. |
| MAJOR | M1 under-weighted: "done deal" allocation rated HIGH, should be CRITICAL. Add the MD's own May [page 26] dating of the cut to November, the 30 cr L third figure (May [page 10]), and the 8 cr L ENA potential inside the 47. |
| MAJOR | P2 partially caught: peers keep subvention below EBITDA (BALRAMCHIN) or book incentives on receipt (GULPOLY). TruAlt's EBITDA includes about Rs 22cr/quarter of subvention plus PLI. Peer EBITDA comparisons in later stages must adjust. The Rs 107cr accrued receivable carries the collection risk GULPOLY describes. |
| MINOR | M8 partial: Nov "construction has begun on three plants" vs Feb "began construction in December" not named. |
| MINOR | M14 partial: stock-in-trade deflection named in B05 prose but missing from the red-flag list and YAML. |
| MINOR | P4 partial: GULPOLY's private-refiner statement contradicts TruAlt's Feb pricing claim; B06 leaves Q2 UNVERIFIABLE. |
| MINOR | B05 severity overstated: grain/sugar split evasion rated CRITICAL; MAJOR fits (data given in Aug; peer TRIVENI withholds the same split). |
| MINOR | B06 Q6 attributes GULPOLY's "below 5%" ISS statement to BALRAMCHIN. |
| MINOR | B05 1C attributes a May de-leveraging push to Tanmay Javeri; not in the transcript. |
| MINOR | B05 2A row "26-28 cr L... actual roughly 18-20" does not match the quarterly figures (about 13.6-13.8). |
| MINOR | Page-anchor errors: B05 Feb p.10 to p.11, May p.5 to p.6 (twice), Nov p.17 to p.18; B06 BALRAMCHIN overcapacity p.10 to p.11, GULPOLY Aug 10-11% p.4 to p.5. |
| MINOR | 11 minor items missed: M22, M23, M24, M25, M27, M28, M29, M30, P8, P9, P10. |

critical 0, major 3, minor 9.

Acceptance: material_found 25, material_caught 24 (20 caught plus 4 partial,
same convention as run r1, which counted 10 of 18 with partials). Rate 96.0%.
Strict rate on outright catches only: 20 of 25 = 80.0%. Both clear the 60%
floor.

```yaml
stage: B12b
company: "TRUALT"
run_date: "2026-09-18"
model: "claude-opus-5"
status: complete
independent_flags_found: 42
caught: 25
partially_caught: 5
missed:
  - {severity: "MAJOR", item: "Sugary-feedstock (B-heavy and juice) diversion may be restricted in ESY 26-27; TruAlt Q1 FY27 volume about 53 percent sugar-based, two monofeed units, 100 syrup days planned; never raised by TruAlt, B05 or B06", anchor: "BALRAMCHIN Aug Vivek Saraogi [page 4]; TRIVENI Aug Tarun Sawhney [page 5]-[page 7]; TRUALT Aug [page 8], May [page 16]"}
  - {severity: "MINOR", item: "CBG margin figures inconsistent within one call (68.29, 60-65, 40-45, 55-60 percent)", anchor: "TRUALT Nov MD/CFO [page 6], [page 21]-[page 22]"}
  - {severity: "MINOR", item: "Revenue-mix answer flips mid-answer from 70/20-25 to 85/15", anchor: "TRUALT Nov MD [page 24]"}
  - {severity: "MINOR", item: "Nov CFO says shut plants operational from Q3 with COD done; Feb shows Unit 5 CTO 17-Dec-2025, 58 operating days, 30 days lost", anchor: "TRUALT Nov CFO [page 7]; Feb MD [page 3]-[page 4], [page 11]"}
  - {severity: "MINOR", item: "Not-allowed-to-project line used selectively while detailed numbers are given", anchor: "TRUALT Feb MD [page 18]; May CFO [page 19]"}
  - {severity: "MINOR", item: "Retail PAT-margin question answered with CBG and finance-cost reasons; retail margin 2 percent (Feb) vs 5 percent (May)", anchor: "TRUALT Aug MD [page 10]; Feb CFO [page 17]; May MD [page 7]"}
  - {severity: "MINOR", item: "CBG utilisation 85 percent plus to 78 percent; CFO says nothing driving the EBITDA dip, then cites employee cost and one-time R&M", anchor: "TRUALT May [page 5]; Aug [page 6], [page 10]"}
  - {severity: "MINOR", item: "Investor-engagement and advertising promises from May not delivered by Aug", anchor: "TRUALT May [page 20], [page 23]; Aug [page 22]"}
  - {severity: "MINOR", item: "ENA plan 6 cr L at Rs 62-63; price fell to Rs 55-56; actual about 3 cr L", anchor: "TRUALT May MD [page 4], [page 14]-[page 15]"}
  - {severity: "MINOR", item: "Peer can hold only 30-45 days of grain; TruAlt claims months of cheap grain stock carrying margin into Q2-Q3 FY27", anchor: "GULPOLY Aug [page 8]-[page 9]; TRUALT Aug [page 18]"}
  - {severity: "MINOR", item: "Peer view split on SAF technology readiness (GULPOLY not established; TRIVENI ATF norms include ethanol-to-jet)", anchor: "GULPOLY Feb [page 11]-[page 12]; TRIVENI Jun [page 7]"}
  - {severity: "MINOR", item: "TruAlt claims LTOA status yet got 26 of a 72 cr L bid sized on 365-day capacity; GULPOLY gets priority allocation at 78 percent; hit rates not like-for-like", anchor: "GULPOLY May [page 3], [page 14]; TRUALT May [page 4], Aug [page 12]"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "concur - D; 8 of 11 promises missed, allocation done-deal claim post-dated the cut by the MD's own May words, same shutdown told as intentional and as force majeure; positives are operational only"
findings:
  - {severity: "MAJOR", location: "B05 and B06 (absent)", finding: "Missed peer-flagged risk that B-heavy and juice diversion is restricted in ESY 26-27; about half of TruAlt volume and two monofeed units exposed", anchor: "BALRAMCHIN Aug [page 4]; TRIVENI Aug [page 5]-[page 7]; TRUALT Aug [page 8]"}
  - {severity: "MAJOR", location: "B05 4D HIGH allocation done-deal", finding: "Under-weighted; should be CRITICAL. Missing the MD's own dating of the cut to November, the 30 cr L third figure, and 8 cr L ENA potential inside the 47", anchor: "TRUALT May [page 10], [page 26]; Nov [page 15]"}
  - {severity: "MAJOR", location: "B06 Q6", finding: "Peer accounting contrast not drawn: BALRAMCHIN keeps subvention below EBITDA, GULPOLY books incentives on receipt; TruAlt EBITDA includes about Rs 22cr per quarter of subvention plus PLI and a Rs 107cr accrued receivable", anchor: "BALRAMCHIN Jun [page 10]; GULPOLY Aug [page 14], Feb [page 13]; TRUALT Aug [page 18], Nov [page 9]"}
  - {severity: "MINOR", location: "B05 1B/1C/2A CBG", finding: "Construction-start contradiction not named (Nov three plants begun vs Feb began in December)", anchor: "TRUALT Nov [page 3]; Feb [page 18]-[page 19]"}
  - {severity: "MINOR", location: "B05 4D and YAML red_flags", finding: "Stock-in-trade purchase question deflection named in prose but absent from the red-flag list", anchor: "TRUALT Feb [page 12]"}
  - {severity: "MINOR", location: "B06 Q2", finding: "GULPOLY private-refiner statement contradicts TruAlt Feb pricing claim; verdict left UNVERIFIABLE", anchor: "GULPOLY Nov [page 8]; TRUALT Feb [page 21]"}
  - {severity: "MINOR", location: "B05 4D CRITICAL grain/sugar split", finding: "Supported on facts, severity overstated; data given in Aug and peer TRIVENI withholds the same split; MAJOR fits", anchor: "TRUALT Nov [page 15], May [page 25], Aug [page 8]; TRIVENI Nov [page 10]"}
  - {severity: "MINOR", location: "B06 Q6", finding: "Below-5 percent ISS debt-cost statement attributed to BALRAMCHIN; it is GULPOLY CFO Rajiv Gupta", anchor: "GULPOLY May [page 6]"}
  - {severity: "MINOR", location: "B05 1C de-leveraging row", finding: "May de-leveraging push attributed to Tanmay Javeri; he asked about CBG funding and one-on-ones", anchor: "TRUALT May [page 20]"}
  - {severity: "MINOR", location: "B05 2A row Q3+Q4 26-28 cr L", finding: "Actual stated as roughly 18-20 cr L; quarterly figures sum to about 13.6-13.8 cr L; promise was production, outcome sales", anchor: "TRUALT Feb [page 8], [page 16]; May [page 25]"}
  - {severity: "MINOR", location: "B05 and B06 anchors", finding: "Page anchors off by one: B05 Feb p.10 to p.11, May p.5 to p.6, Nov p.17 to p.18; B06 BALRAMCHIN Jun overcapacity p.10 to p.11, GULPOLY Aug guide p.4 to p.5", anchor: "PDF page markers in each .txt"}
  - {severity: "MINOR", location: "B05 and B06 (absent)", finding: "Eleven minor items missed (M22, M23, M24, M25, M27, M28, M29, M30, P8, P9, P10); see missed list", anchor: "see missed list"}
critical_count: 0
major_count: 3
minor_count: 9
material_found: 25
material_caught: 24
acceptance_rate: 96.0
coverage_basis: "25 material of 42 listed (2 CRITICAL, 23 MAJOR); 20 caught outright, 4 partially caught, 1 missed; rate counts partial catches as caught, same convention as run r1; strict outright rate 20 of 25 = 80.0 percent"
```
