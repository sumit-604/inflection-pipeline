# Stage 12B: Verifier B — Independent Concall Red-Flag Audit — CEIGALL

Run date: 2026-09-06 | Model: claude-opus-4-8 | Emits: B12b
Scope: 4 Ceigall transcripts (primary) + 12 peer transcripts (HGINFRA, KNRCON, PNCINFRA)
Artifacts audited: B05-concall.yaml (run 2), B06-peers.yaml (run 2),
05-concall.md (run 2), 06-peers.md (run 2)

METHOD. I read all four Ceigall transcripts end to end and built my own
red-flag list before opening any upstream artifact. I then targeted the peer
corpus on the specific claims my own pass raised (NHAI award pace, escalation
pass-through, HAM monetisation disclosure, working-capital granularity,
governance disclosure, solar ramp timing, order-book reconciliation practice).
Only after that did I open B05/B06. Every anchor below is the
`===== [PAGE N] =====` marker, which is the PDF page number. In the Nov-2025
and Aug-2026 files the printed "Page N of M" header runs exactly one page
behind the marker; I use the marker throughout and flag where upstream did not.

---

## PART 1: INDEPENDENT RED-FLAG LIST (built before reading B05/B06)

### 1.1 Repeated evasion (2+ quarters on the same question)

**IF-1. NHAI awarding pace, refused twice, third attempt lost.** CRITICAL
Feb-2026 p.8-9: Ketan (Avendus Spark) asks three times in one exchange how many
km NHAI and MoRTH have awarded. Answers: "any number specific, a specific number
discussing at this moment will not be correct"; then "there are a lot of
contracts available online"; then "I mean, it is not easy for us to do this. We
can check it on NHAI website and then we can update you, maybe you can share
your email with Kapil." May-2026 p.9-10: Dheeraj Kripalani (Avendus Spark) asks
twice for FY26 awarding in km and value; answer: "these are the figures which
NHAI has put on their own website," then the line is cut. Aug-2026 p.6: Krish
Bhatia begins the same question ("Highway projects to be awarded in FY27... how
much do you expect to be awarded within this year") and the line drops.
Peer contrast is decisive: PNCINFRA volunteers "NHAI's project awarding activity
remained subdued in Q1 FY2027 also, with only 107 kilometers awarded"
(PNCINFRA-Concall_Aug_2026_Transcript.txt, p.3) and "Awarding activity by
National Highways Authority of India stood at 3,124 km aggregate length, more
than 30% below the targeted length of 4,500 km"
(PNCINFRA-Concall_May_2026_Transcript.txt, p.4). KNRCON volunteers the same
class of figure every quarter. The number Ceigall calls impossible is in two
peers' prepared remarks, unprompted.

**IF-2. "Was the margin beat a one-off?" — asked in two consecutive quarters,
answered neither time.** CRITICAL
May-2026 p.9, Mahesh Patil (ICICI Securities): "if we see on Q4 compared to last
Q4, there has been significant increase. So is there any one-off or if this is
just because of the execution that we have." Kapil Aggarwal answers: "last year
if you look at, we have started four HAM projects which have majorly contributed
to the PAT margins" — an answer about PAT, not about the EBITDA one-off, and it
never says yes or no.
Aug-2026 p.7, Mahesh Patil again: "we have posted good margins of more than
around 13.5% this quarter against our guidance of around 11% to 12.5%... what led
to this improvement, and can we see similar margins in the upcoming quarters or
was there any one-off this quarter?" Kapil answers: "we have started 3 new
projects in this quarter. 2 are Maharashtra solar projects, MH1 and MH2, and road
projects, HAM projects in Indore-Ujjain." Starting three projects does not
explain a 90-240bp margin beat. The one-off question is again unanswered, and
guidance is reaffirmed at 11-12.5% without explaining why the margin should fall
back.
Same analyst, same question, two consecutive calls, a non-answer of the same
shape both times. This is the pattern the rubric grades CRITICAL, and it is
absent from B05's repeated-question tracker.

**IF-3. Segment margin bifurcation (renewables/T&D vs core EPC), four
quarters, never a number.** CRITICAL
Nov-2025 p.13 (Priyam Shah), Feb-2026 p.13 (Nimish Pandya), May-2026 p.7-8
(Tejpal Singh), Aug-2026 p.9 (Chetrika Deshpande). Four asks, zero splits.
Nimish Pandya's framing "do they match your historical 15% plus EBITDA margin
levels" is answered "Yes, yes, they'll match the historical EBITDA margin
levels" (Feb-2026 p.13) — the company's own guided band is 11-12.5%, so a 15%+
framing was accepted without correction.
Peer contrast: HGINFRA gives the split when asked — infra/rail/roads "about 14%
to 15%," battery and transmission "around 10% to 11%"
(HGINFRA-Concall_May_2026_Transcript.txt, p.14).

**IF-4. Total/pending equity requirement, asked every call, a new
unreconciled number every call.** CRITICAL
Nov-2025 p.10: Rs788cr HAM pending, plus "a little less than INR600 crores" for
solar and BESS (p.12). Feb-2026 p.9-10: Rs1,391cr HAM total, Rs395cr for two new
projects, "close to 810" for solar including T&D. May-2026 p.6: "in next three
years, we have to put close to INR2,000 crores, INR1,937 crores," split Rs800cr
renewable / rest HAM. Aug-2026 p.5-6: Rs253cr at IPO, Rs692cr cumulative today,
Rs859cr FY27, Rs744cr FY28. No call ever bridges to the previous call's figure.

### 1.2 Statements contradicted by the same call's own numbers

**IF-5. Feb-2026: "our growth is much more than [10-15%]" — false against the
same call's 9M figures.** MAJOR
Feb-2026 p.14: "We were always guiding 10% to 15%, our growth is much more than
that. Thank you." The same call's CFO reported 9M FY26 standalone revenue growth
of 7.6% and consolidated growth of 8.7% (p.5-6). Both are below the bottom of
the guided band, not "much more" than the top of it. Earlier in the same call
(p.7) the CMD had already said "we are targeting to achieve 10% to 15%, and we
are on track." The year did close inside the band on Q4 execution, but the
February claim was untrue when made and was never corrected.

**IF-6. May-2026: "EBITDA margin is stable, that's not decreasing... has grown
up as compared to the previous year."** MAJOR
May-2026 p.10, answering Maitri Shah on Slide 41. The same call's own opening
remarks state standalone FY26 EBITDA margin 12.6% versus 12.8% in FY25 (p.5).
The margin fell. Maitri Shah pressed three times before the CFO conceded that
FY24 and FY25 headline EBITDA carried bonus and royalty income ("we have INR20
crores royalty and bonus in FY '25"). The concession came only after the third
push, and it never produced the FY26 like-for-like comparable that would settle
the question.

**IF-7. May-2026: assets under a non-binding offer described as "already sold,"
twice, in the same call.** MAJOR
Prepared remarks, p.4: "For Bathinda-Dabwali and Jalbehra Shahbad, we have signed
non-binding offer and these are currently under due diligence." Q&A, p.6: "we
have already sold three assets to Neo in which first asset we are expecting it
should get executed in this month only." Q&A again, p.7: "we've sold three
assets, so more than INR400 crores will come from Neo also after selling those
assets." Two assets under due diligence cannot be "sold." The same pattern
appears in Feb-2026: "in-principle approved a binding offer" (p.4) versus "we
have already sold one HAM asset" (p.9). By Aug-2026, only one of the three has
completed and the other two are not mentioned at all.

**IF-8. Nov-2025: two different equity-infusion figures for the same three-month
window, in one call.** MAJOR
p.10, Ramneek Sehgal: "We are targeting to infuse about INR297 crores in coming
3 months." p.11, Kapil Aggarwal: "We are going to infuse close to INR200 crores
in the next 3 months in the VRK as well as the Ludhiana-Bathinda and Northern and
Southern Ayodhya projects." No bridge is offered between the two. (Note: the
Rs200cr line sits on PDF page 11, not page 12.)

**IF-9. Aug-2026: a nine-project equity list that sums to Rs567cr against a
stated Rs550cr, and 11 HAM projects against the same call's 10.** MAJOR
p.10, Kapil Aggarwal, after an analyst's own arithmetic came to Rs430-440cr:
53 + 61 + 53 + 97 + 139 + 38 + 60 + 50 + 16 = Rs567cr. He says "in totality, this
comes to INR550 crores." He also says the figure is "across all 11 of our HAM
projects" (p.9), while his own opening remarks list "10 HAM projects" in the
order book (p.4). Three different totals in one exchange, none reconciled.

**IF-10. Nov-2025: bid pipeline total does not equal its own components.** MINOR
p.6: "Ceigall has submitted totalling of INR1,43,200 million" with components
"INR88,860 million in the Road segment, INR48,960 million in the Railway segment,
and around INR6,000 million in the Renewable segment" — the components sum to
Rs14,382cr against a stated Rs14,320cr. On p.9 the same pipeline is "INR14,000
crores." An analyst says "nearly INR16,000 crores" (p.10) and is not corrected.

**IF-11. Nov-2025: revenue mix stated twice in one call, inconsistently.** MINOR
p.3: "renewable energy accounts for 22% of order book." p.14: "renewable is about
21%." The p.14 sector split sums to 98.9%; the delivery-model split on the same
page (HAM 45%, EPC 25%, tariff 24%, DBFOT 1%) sums to 95%.

**IF-12. Nov-2025: Ramban-Banihal figures incoherent inside one exchange.** MINOR
p.11: the analyst puts balance work at Rs385cr "for both the projects"; management
replies that "the other project... is totally INR369 crores," that "20% of the
tunnel work... would be around INR180 crores" (implying a ~Rs900cr tunnel scope),
and that the second project is "54% of the project completed and 45% financially."
None of these tie to each other.

### 1.3 Cross-call numbers that change without reconciliation

**IF-13. Order-book roll-forward fails in all three testable quarters.** MAJOR
I recomputed this independently before reading B05. Using consolidated revenue as
executed value:

| Quarter | Opening | + Inflow | − Revenue | = Implied | Actual | Gap |
|---|---|---|---|---|---|---|
| Q3 FY26 | 12,598 (Nov-25 p.3) | 1,403 (Feb-26 p.4) | 991 (Feb-26 p.5) | 13,010 | 13,295 (Feb-26 p.4) | **+285** |
| Q4 FY26 | 13,295 | 6,014 (May-26 p.4) | 1,386 (May-26 p.5) | 17,923 | 18,554 (May-26 p.3) | **+631** |
| Q1 FY27 | 18,554 | ~600 (Aug-26 p.7) | 970 (Aug-26 p.4) | 18,184 | 18,568 (Aug-26 p.4) | **+384** |

The three gaps are confirmed exactly as B05 states them. Average +Rs433cr;
2.1%, 3.4% and 2.1% of book. Always positive. Never explained on any call.
Basis note: on standalone revenue the gaps become +264 / +539 / +315 — the
direction and the unexplained residual survive either basis, so the finding is
robust to the choice. Peers reconcile this on request: when an analyst asked
PNCINFRA to reconcile a Rs22,000cr order book against a Rs15,000cr figure,
management walked through the additions on the call
(PNCINFRA-Concall_Aug_2026_Transcript.txt, p.13).

**IF-14. Feb-2026: 9M order inflow claimed at "close to INR8500 crores," which
the FY26 total contradicts.** MAJOR
Feb-2026 p.10: "last year we guided our investors that we will be getting
INR5000 crores. Against INR5000 crores, we have already got close to INR8500
crores." The same call reports Q3 inflow of "approximately INR1,403 crores"
(p.4), and H1 inflow was Rs3,747cr (Nov-2025 p.3) — 9M actual Rs5,150cr.
Independently, May-2026 reports FY26 inflow of Rs11,332cr with Q4 at Rs6,014cr
(p.4), implying 9M inflow of Rs5,318cr. The Feb claim is ~60% above what the
company's own annual figures support. The gap is the value of L1 positions
counted as won: Sahebganj Rs2,160cr + Jaipur Rail Rs918cr + Indore-Ujjain
Rs1,089cr + Surya Mitra Rs423cr = Rs4,590cr, which added to Rs3,747cr gives
Rs8,337cr. Feb-2026 states plainly that the Sahebganj LOA "is not received yet"
(p.7) and that Jaipur Rail is "still waiting for the LOA" (p.11).

**IF-15. Solar/BESS equity requirement rises 35% in one quarter on the same
scope.** MAJOR
Nov-2025 p.12: asked the equity requirement for the T&D projects, Ramneek Sehgal
answers "closer to a little less than INR600 crores," confirmed as "for both
solar and BESS combined." Feb-2026 p.9: "the equity will be close to INR750 to
INR800 crores in the solar projects," then p.10: "for solar it is close to 810,"
and, asked whether that includes T&D, "Yes, yes." Same scope, Rs600cr to Rs810cr
in one quarter, no explanation.

**IF-16. Cash is disclosed on a different basis every quarter.** MAJOR
Dec-2025: "Including FD it is INR225 crores" (Feb-2026 p.10). Mar-2026:
unencumbered cash Rs266cr and unencumbered FDR Rs146cr, corrected by written
erratum to Rs166cr and Rs75cr (May-2026 p.6). Jun-2026: "whatever FDs we have
close to almost INR320 crores FDs lying in the books of accounts" (Aug-2026
p.11). Three quarters, three definitions, no series a reader can build. The
Rs320cr figure does not appear in B05 at all.

**IF-17. The May-2026 erratum overstates liquidity by 71%, not 41.5%.** MAJOR
(computed independently; see Part 4 for the arithmetic dispute with B05)
May-2026 p.6, inside the sentence arguing "equity is not a problem with Ceigall,
we have amazing cash flow available with us": stated Rs266cr unencumbered cash
and Rs146cr unencumbered FDR (Rs412cr combined); the filed erratum corrects
these to Rs166cr and Rs75cr (Rs241cr combined). Cash alone was overstated 60.2%;
FDR alone 94.7%; combined 70.95%.

**IF-18. Consolidated EBITDA and consolidated PAT disappear in Aug-2026;
consolidated debt disclosure decays to nothing across four calls.** MAJOR
Nov-2025 p.5 gives both debt levels with a full loan-type breakdown. Feb-2026
p.5 gives aggregates only (standalone Rs552cr, consolidated Rs1,421cr — note
consolidated debt rose from Rs1,341cr at Sep-25 while the narrative is
"balance sheet optimization"). May-2026 p.4 gives ratios only (0.2x standalone,
0.6x consolidated), no rupee figures. Aug-2026 gives neither, at either level.
The same Aug-2026 call also drops consolidated EBITDA and consolidated PAT,
disclosing only consolidated revenue (p.4). Peers disclose the opposite way:
PNCINFRA gives standalone and consolidated net worth, debt, cash and net-cash
position in its Q1 FY27 prepared remarks
(PNCINFRA-Concall_Aug_2026_Transcript.txt, p.5).

**IF-19. Consolidated PAT sits below standalone PAT in H1 and 9M FY26.** MAJOR
H1 FY26: standalone Rs111.8cr, consolidated Rs107.5cr (Nov-2025 p.6-7). 9M FY26:
standalone Rs186cr, consolidated Rs180cr (Feb-2026 p.5). In both periods
consolidated EBITDA is above standalone (Rs222.7cr vs Rs185.3cr; Rs362cr vs
Rs305cr), so the SPV interest and depreciation load more than consumes the
uplift. FY26 flips by Rs4cr (Rs309cr vs Rs305cr). Never commented on. The one
quarter where this would next be testable, Q1 FY27, is the quarter the
consolidated P&L disclosure stopped.

### 1.4 Promises made and never revisited

**IF-20. HAM equity infusion pace: Rs297cr promised in three months, Rs2.4cr
delivered, Rs89cr over eight months.** MAJOR
Nov-2025 p.5: Rs515.4cr infused at Sep-2025, Rs603.2cr "as on date" (Oct-2025).
Nov-2025 p.10: Rs297cr targeted in the coming three months. Feb-2026 p.4:
Rs605.6cr infused at Dec-2025 — Rs2.4cr added. Aug-2026 p.5: cumulative Rs692cr
"as on today's date," i.e. Rs89cr added in eight months against a Rs297cr
three-month target. Never acknowledged, never asked about.

**IF-21. FY27 equity commitment Rs859cr against Q1 delivery of Rs23cr.** MAJOR
Aug-2026 p.5-6: "this year, our balance equity commitment is INR859 crores"
(Rs310cr solar, Rs550cr HAM, per p.6). Aug-2026 p.8: "INR23 crores we have
invested" in Q1. That is 2.7% of the annual plan in 25% of the year, against a
demonstrated run rate of Rs23-30cr per quarter and a required Rs279cr per quarter
for the remaining nine months. No analyst tested it.

**IF-22. Southern Ludhiana bypass land: 80% "by December" 2025 becomes 62% in
August 2026 — a regression, not a delay.** MAJOR
Nov-2025 p.7: "Land status in Southern bypass is very clear... Southern bypass, I
think we should get the 80% land cleared by December, and we'll start the work
full-fledged." Aug-2026 p.5: "But Ludhiana, the land is only 62% available with
us, so that is a challenge," and the year's execution is cut to "at least 15%"
from the 25-30% the analyst assumed. Neither intervening call flags the slip.

**IF-23. "By 31st March 2026, all our HAM projects will be under execution" —
abandoned without mention.** MAJOR
Nov-2025 p.7: VRK12 appointed date "any time before 31st December 2025,"
Southern bypass "before 31st December 2025," VRK11 "before 31st March 2026,"
and the blanket claim "I think by 31st March 2026, all our HAM projects will be
under execution." Feb-2026 p.7: VRK12 "around tomorrow or day after," Southern
"this month," both "before 31st March." May-2026: silent. Aug-2026 p.3:
"Subsequent to the quarter end, we received the appointed dates of VRK 11, VRK
12, Indore-Ujjain" — July or August 2026, a five-to-eight month slip. Southern
Ludhiana still has no appointed date. May-2026 p.9 concedes the general position
without naming the promise: "in HAM till the time 80% land is given clear to us,
it doesn't start."

**IF-24. Ramban-Banihal: three dated promises, then three calls of silence.**
MAJOR (B05 grades this LOW)
Nov-2025 p.11: tunnel "completing in the next 3 months"; "20% of the tunnel work,
which would be around INR180 crores would be completed before this March";
viaduct "by March '27" on redesigned steel girders. The project is never
mentioned again in Feb-2026, May-2026 or Aug-2026, and no analyst asks. This is
a difficult-terrain J&K project with a stated Rs385cr balance of work and a
publicly narrated redesign; three calls of total silence on it is not a low-grade
item.

**IF-25. May-2026 FY27 renewable-revenue guidance (20-25% of total) never
revisited or tested.** MAJOR
May-2026 p.4: "For Financial Year '27, we are guiding 15% minimum revenue growth
with renewable sector contributing close to 20% to 25% of the total revenue."
On a FY26 consolidated base of Rs4,022cr plus 15%, that is Rs925-1,156cr of
renewable revenue in FY27. Aug-2026 discloses no renewable revenue, no segment
split, and confirms Morena/BESS has neither PPA nor transmission tender ("Till
now only LOA is received, PPA is yet to be signed and even transmission line
tender is not even received," May-2026 p.11) and that Rewa still waits on
transmission (Aug-2026 p.5). Peer benchmark: PNCINFRA, at a comparable solar
stage, guides first revenue only in Q4 FY27 and completion across FY28-29
(PNCINFRA-Concall_Aug_2026_Transcript.txt, p.9 and p.14).

**IF-26. Aug-2026: Q1 standalone growth of 10.2% against a reaffirmed "minimum
15%," never addressed.** MAJOR
Aug-2026 p.4: standalone Q1 FY27 revenue Rs901cr versus Rs818cr, +10.2%.
Consolidated +15.7% is quoted; the standalone shortfall is not. p.8: "earlier we
used to say it should be between 10% to 15%. This year, it should be minimum
15%." The quarter is framed as "another encouraging quarter" (p.3). The same
pattern as Feb-2026 (IF-5): an in-year shortfall against guidance, restated as
being on track.

**IF-27. Malout-Abohar-Sadhuwali: no price on any of four calls, and an IRR
claim with no number.** MAJOR
Feb-2026 p.10: Parth Patel says "you completed a sale to, I think Neo Asset for
about INR177 crores" — neither confirmed nor corrected. May-2026 p.6: "more than
INR400 crores will come from Neo" for three assets. Aug-2026 p.3 confirms the
first monetisation completed, with no consideration disclosed, and p.9 asserts it
"has given much more the IRR what we committed or we guided our investors,"
again with no number. Peer contrast: HGINFRA states the enterprise value
(Rs3,584cr), equity invested (Rs767cr) and debt (Rs2,200cr) for its Neo
transaction and repeats the same figures across three calls
(HGINFRA-Concall_Aug_2025_Transcript.txt, p.5-6); PNCINFRA gives an enterprise
value of Rs630cr when asked.

**IF-28. Bathinda-Dabwali and Jalbehra-Shahbad divestments: "before September"
becomes Q2/Q3 FY27, then silence past the original deadline.** MAJOR
Feb-2026 p.12: "these two we are targeting to close it before September."
May-2026 p.7: Bathinda-Dabwali "in second quarter," Jalbehra Shahbad "in third
quarter." Aug-2026: neither is mentioned, and the Feb deadline has passed.

**IF-29. Nov-2025: "We have 1.5 years to dilute another 8% also" — never
explained, never repeated.** MAJOR
Nov-2025 p.12, dropped into an answer about solar project financing. For a
company listed in August 2024, a further ~8% dilution inside 1.5 years reads as
minimum-public-shareholding compliance and is a real equity overhang. It is
never mentioned again on any of the three later calls, and no analyst asks. In
Aug-2026 p.12 an analyst refers to "post-IPO and post-QIP type capital raises"
and the CFO neither confirms nor corrects the QIP premise.

**IF-30. Aug-2026: "we have 100% utilized the IPO proceeds in the last quarter of
the FY26," disclosed only as an aside.** MAJOR
Aug-2026 p.11, answering why other income fell from Rs15cr to Rs9.5cr: "Other
income... is primarily on account of royalty, which we were getting in the
earlier years. Right now, we are not charging royalty, and plus FDR... in the
previous financial year, we were having proceeds from IPO on which we were
getting returns... So, we don't have that surplus now. We have 100% utilized the
IPO proceeds in the last quarter of the FY26." Two structural facts arrive in one
Q&A answer: the IPO cash cushion is gone, and the royalty stream the CFO used in
May-2026 to defend margin optics has stopped. Neither is in any prepared remark.

### 1.5 Tone that does not match the arithmetic, and peer contradictions

**IF-31. Full escalation pass-through claimed; all three peers say partial and
time-boxed.** MAJOR
May-2026 p.9: "The increased cost is already compensated by the department; they
already come up with the circular for compensating the escalation part and
earlier it was linked to 3 months and now it has been linked to monthly basis. So
whatever increase in the cost, that we can that will be paid by the authority
ultimately to the EPC contractor."
PNCINFRA, same period: the mechanism is "expected to provide some relief margin
pressures... to certain extent" (PNCINFRA-Concall_May_2026_Transcript.txt, p.6),
and pressed later, "certainly, we cannot deny that there would not be any margin
pressure. Certainly, there will be pressure on our margins" (p.8). KNRCON frames
it as a faster pass-through cycle, not a guarantee. HGINFRA's Q4 FY26 standalone
EBITDA margin fell to 9.37%, with management attributing the quarter directly to
"higher commodity prices... cost escalation and profitability"
(HGINFRA-Concall_May_2026_Transcript.txt, p.6).

**IF-32. Ceigall's best-ever quarterly margin lands in the same quarter a peer's
margin collapses on unrecovered escalation.** MAJOR
Ceigall Q4 FY26 standalone EBITDA margin 14.1% (May-2026 p.5), up from 12.3% in
Q3, the highest of the four quarters. HGINFRA's Q4 FY26 standalone margin:
9.37%, explicitly attributed to unrecovered cost escalation. Ceigall's management
denies any input-cost impact at all in the same call. The direct question about a
one-off went unanswered (IF-2). This juxtaposition is not drawn anywhere upstream.

**IF-33. Nov-2025: "significant uptick in order awarding by NHAI" against a peer
set describing a multi-year downcycle.** MINOR
Nov-2025 p.5: "we expect a significant uptick in order awarding by NHAI." KNRCON,
one week later, describes bids "getting postponed," an order book at its lowest
road share in ten years, and asks openly "whether there is an upcycle at all in
the next few years" (KNRCON-Concall_Nov_2025_Transcript.txt, p.9-10). PNCINFRA in
May-2026: "there has been a very unhealthy competition for the last two to three
years, coupled with the low awarding activity by NHAI... there have been no major
orders during the last three years from NHAI"
(PNCINFRA-Concall_May_2026_Transcript.txt, p.9). Ceigall's Nov-2025 claim that
tightened net-worth norms mean "probability will be more for us" (p.14) sits
against a peer calling the competition unhealthy through the same window.

**IF-34. MoRTH FY27 budget figure differs from a peer's by 7%.** MINOR
Ceigall, Feb-2026 p.3: MoRTH "increased its budgetary allotment by around 8% to
approximately INR3.1 trillion for the year '26-'27." PNCINFRA, May-2026 p.5:
"INR 2.9 trillion for FY27, representing an increase of around 8% over the
previous year." Same metric, same year, same stated growth rate, two different
levels.

**IF-35. Romania: a Rs13,000cr bid on a company that says it takes "baby
steps."** MINOR (context, not a standalone flag)
May-2026 p.5: domestic tenders under evaluation "close to INR13,000 crores," and
a single 17km Romanian highway also "close to INR13,000 crores" — 70% of the
order book. Feb-2026 p.7 had said international work needs "no equity
requirement, but we'll be requiring only the BG limits." Aug-2026 p.11 reverts to
"we want to take baby steps there." The bid is never mentioned again.

### 1.6 Governance, disclosure and material events the calls never carry

**IF-36. Promoter's personal Rs20cr equity in the Bathinda-Dabwali HAM SPV, an
asset inside the divestment pipeline.** MAJOR
Feb-2026 p.6, Kapil Aggarwal, answering a question about a different SPV: "In
case of Bathinda-Dabwali, Ramneek sir, he has also contributed INR20 crores. So
being a promoter of the company, he has invested INR20 crores in Bathinda-
Dabwali." Bathinda-Dabwali is one of the three assets being sold to Neo (Feb-2026
p.10, May-2026 p.7). How a promoter's personal equity in an asset earmarked for
third-party sale is priced and exited is never addressed, and no analyst asks.

**IF-37. Senior management churn across four calls, never explained; the IR
agency also changes without mention.** MAJOR
Nov-2025: CMD + CFO, moderated by Ernst & Young LLP. Feb-2026: CMD + Sudhir
Hoshing (Whole-Time Director, new, unintroduced) + CFO, moderated by Adfactors
PR. May-2026: CMD + A. Sarvanan (CEO, new) + CFO + Akshay Jain (VP Strategy);
Hoshing gone. Aug-2026: CMD + CFO + A. Saravanan now "Whole-Time Director and
CEO"; Akshay Jain gone. May-2026 p.5 also mentions "we have already appointed one
CEO International." Four calls, four different management line-ups, zero
commentary. Peers' analysts do ask this question: HGINFRA was pressed on "a
dramatic exit of 3 senior executives from the company"
(HGINFRA-Concall_Feb_2026_Transcript.txt, p.12).

**IF-38. Investor-presentation error admitted live.** MINOR
Feb-2026 p.5-6: Vaibhav Shah finds equity-invested figures on Slide 38 that do
not match the company's stated share. Ramneek Sehgal: "It's a mistake, but
otherwise entire equity has been put by the company only." A clean admission, but
the underlying defect is a disclosure error in a filed investor presentation.

**IF-39. A 10x number error left uncorrected in the same filed transcript that
carries a cash erratum.** MINOR
May-2026 p.12: "we have already got one INR21,160 crores project and one INR600
crores project of Zirakpur bypass." The project is Sahebganj at Rs2,160cr, named
correctly on p.3 of the same document. The company issued a written erratum for
the cash and FDR figures in this transcript and left a ten-fold order-value error
in it.

**IF-40. Feb-2026: "seven of our projects have completed ahead of schedule"
alongside a late project awaiting an EOT, then silence.** MINOR
Feb-2026 p.4 makes the early-completion claim; p.11 discloses that Jalbehra has
"an ROW problem... a flood problem," that the government "is planning to give us
an EOT," and that bonus eligibility cannot be stated until the EOT is in hand.
The EOT is never mentioned again in May-2026 or Aug-2026.

**IF-41. Aug-2026: Northern Ayodhya execution collapse answered with a denial,
a weather excuse and a concession, in one breath.** MAJOR (B05 rates this
"plausible and seasonal, not disputed")
Aug-2026 p.4-5, Vaibhav Shah: "In Northern Ayodhya bypass, the execution has
fallen in Q1 to almost INR42-odd crores. So, any particular reason, any issues we
are facing?" Answer: "No, no. I mean, it is going proper. There's nothing. Now,
from last 1.5 months, there's been rain. Otherwise, progress is steady. We've been
achieving all our milestones before ahead, before time. It's just — sometimes you
don't achieve the milestone, payment can only be made only once the milestone is
achieved." The answer denies a problem, blames rain, claims all milestones are
beaten, then concedes a missed milestone. Northern Ayodhya is one of the largest
HAM assets and carries Rs61cr of the FY27 equity plan (p.10).

**IF-42. Aug-2026: Rs100cr commercial paper justified only on a rate spread,
one quarter after the IPO cash was exhausted.** MINOR
Aug-2026 p.11-12: the CP is "carve[d] out from our working capital limits" at
6.8-7.0% versus WCDL at 7.5-7.8%, "which will give more benefits to the company
and visibility to the company." No analyst connects it to the exhausted IPO
proceeds (IF-30) or to the Rs859cr FY27 equity call (IF-21).

**IF-43. Never mentioned on any of the four calls.** MAJOR (transcript half
verified; the underlying events sit in B02/B03, outside my inputs)
No call contains any reference to a procurement fraud, a qualified internal
financial controls opinion, a GST search action, an NHAI termination of a
step-down SPV, a subsidiary auditor resignation, or contingent-liability growth.
I confirm the silence across all four transcripts. I cannot verify the events
themselves from my inputs.

---

## PART 2: COMPARISON AGAINST B05 (run 2) AND B06 (run 2)

Legend: CAUGHT = upstream carries the finding at comparable weight.
PARTIALLY CAUGHT = carried but under-weighted, mis-severitied, or the specific
arithmetic/contradiction is absent. MISSED = absent from both artifacts.

| # | Finding | Sev | Status | Where upstream / why not |
|---|---|---|---|---|
| IF-1 | NHAI award pace, repeated evasion | CRITICAL | CAUGHT | B05 2E row 1; B06 Q2 |
| IF-2 | "Was the margin beat a one-off?", 2 quarters unanswered | CRITICAL | **MISSED** | Not in B05 2E, not in 3C; Mahesh Patil appears nowhere in B05 |
| IF-3 | Segment margin bifurcation, 4 quarters | CRITICAL | CAUGHT | B05 2E row 3; B06 Q8 |
| IF-4 | Equity requirement, new number every call | CRITICAL | CAUGHT | B05 2E row 2, 2F.3 |
| IF-5 | Feb-26 "growth much more than 10-15%" false vs 7.6%/8.7% | MAJOR | **MISSED** | B05 records the reaffirmation, never tests it |
| IF-6 | May-26 "margin has grown up" vs 12.6% vs 12.8% | MAJOR | CAUGHT | B05 2B, 2C, 3C |
| IF-7 | "Already sold three assets" vs non-binding/DD, same call | MAJOR | CAUGHT | B05 4D MEDIUM row |
| IF-8 | Nov-25 Rs297cr vs Rs200cr, same call | MAJOR | CAUGHT | B05 1B, 2F.3 |
| IF-9 | Rs567cr list vs Rs550cr stated; 11 vs 10 HAM | MAJOR | CAUGHT | B05 2F.7 |
| IF-10 | Nov-25 bid total vs components | MINOR | **MISSED** | Absent |
| IF-11 | Nov-25 revenue mix inconsistent, sums to 95%/98.9% | MINOR | PARTIAL | B05 2F.5 tracks the 22%→19% series, not the intra-call 22/21 split |
| IF-12 | Ramban-Banihal figures incoherent in-call | MINOR | **MISSED** | B05 carries the promises, not the internal incoherence |
| IF-13 | Order-book roll-forward +285/+631/+384 | MAJOR | CAUGHT | B05 2F.1, arithmetic independently confirmed |
| IF-14 | Feb-26 "Rs8,500cr" 9M inflow vs Rs5,318cr implied | MAJOR | PARTIAL | B05 2F.2 raises the L1 question but never runs 11,332−6,014 against it |
| IF-15 | Solar/BESS equity Rs600cr → Rs810cr, same scope | MAJOR | PARTIAL | B05 lists both numbers; never names the 35% one-quarter step |
| IF-16 | Cash basis changes every quarter; Rs320cr absent | MAJOR | **MISSED** | Rs320cr (Aug-26 p.11) appears nowhere in B05 |
| IF-17 | Erratum = 71% overstatement | MAJOR | CAUGHT (flag) / WRONG (magnitude) | B05 4D and red_flags state 41.5%; see Part 4 |
| IF-18 | Consolidated debt and consolidated P&L disclosure decay | MAJOR | CAUGHT | B05 2F.4, 2F.6 |
| IF-19 | Consolidated PAT below standalone, H1 and 9M | MAJOR | CAUGHT | B05 2F.4 |
| IF-20 | Rs297cr promised, Rs2.4cr / Rs89cr delivered | MAJOR | CAUGHT | B05 2A, promise_delivery |
| IF-21 | Rs859cr FY27 plan vs Rs23cr Q1 | MAJOR | CAUGHT | B05 4D MEDIUM row |
| IF-22 | Southern Ludhiana 80% → 62% regression | MAJOR | CAUGHT | B05 2A |
| IF-23 | "All HAM under execution by 31-Mar-26" abandoned | MAJOR | PARTIAL | B05 tracks the AD slippage; the blanket Nov-25 claim itself is absent |
| IF-24 | Ramban-Banihal, three promises, three calls silent | MAJOR | PARTIAL | B05 carries it at LOW; I grade MAJOR |
| IF-25 | FY27 renewable revenue 20-25% guidance never tested | MAJOR | **MISSED** | Absent from B05's guidance table entirely |
| IF-26 | Q1 FY27 standalone +10.2% vs "minimum 15%" | MAJOR | **MISSED** | B05 records the reaffirmation, never tests the quarter |
| IF-27 | Malout sale price never given; IRR claimed without a number | MAJOR | CAUGHT | B05 2D, 4D; B06 Q3 |
| IF-28 | Divestment timeline slipped then dropped | MAJOR | CAUGHT | B05 2A, timeline_slippages |
| IF-29 | "1.5 years to dilute another 8%" | MAJOR | **MISSED** | Absent |
| IF-30 | IPO proceeds 100% utilised; royalty stopped | MAJOR | **MISSED** | Absent; B05 has the ROE question but not this |
| IF-31 | Full escalation pass-through claim | MAJOR | CAUGHT | B06 Q9 |
| IF-32 | 14.1% Ceigall Q4 vs 9.37% HGINFRA Q4 | MAJOR | PARTIAL | B06 Q9 uses HGINFRA's 9.37%; neither report juxtaposes Ceigall's own Q4 jump |
| IF-33 | "Significant uptick in NHAI awarding" vs peer downcycle | MINOR | PARTIAL | B06 2A covers the muted-award consensus; the competition-intensity contradiction is not drawn |
| IF-34 | MoRTH Rs3.1trn vs peer Rs2.9trn | MINOR | **MISSED** | Both figures appear in the two reports; never cross-checked |
| IF-35 | Romania Rs13,000cr vs "baby steps" | MINOR | CAUGHT | B05 1C, 3C |
| IF-36 | Promoter's Rs20cr in a sale-pipeline SPV | MAJOR | CAUGHT | B05 2D, 4D |
| IF-37 | Four-call management churn + IR agency change | MAJOR | PARTIAL | B05 catches the WTD/CEO change; not the four-call sequence or the E&Y→Adfactors switch |
| IF-38 | Slide 38 error admitted | MINOR | CAUGHT | B05 2B |
| IF-39 | "INR21,160 crores" 10x error uncorrected | MINOR | **MISSED** | Absent |
| IF-40 | Jalbehra EOT/bonus limbo vs "seven completed early" | MINOR | **MISSED** | Absent |
| IF-41 | Northern Ayodhya denial → rain → concession | MAJOR | PARTIAL | B05 2B rates it "plausible and seasonal, not disputed" |
| IF-42 | Rs100cr CP against exhausted IPO cash | MINOR | PARTIAL | B05 lists CP as a trigger; the juxtaposition is not made |
| IF-43 | Four-call silence on governance events | MAJOR | CAUGHT | B05 flags, 2D, 4D; B06 Q5 |

**Tally over 43 independent company red flags:**
- CAUGHT 20 (3 of 4 CRITICAL; 16 of 27 MAJOR; 1 of 12 MINOR)
- PARTIALLY CAUGHT 10
- MISSED 13 (1 CRITICAL, 6 MAJOR, 6 MINOR)

Note on the denominator: IF-1 through IF-43 are company-directed red flags only.
Three further findings I raise against the pipeline's own artifacts (Part 4) are
excluded from the coverage denominator, since coverage measures how much of the
company red-flag surface upstream had already reached.

### Pipeline flags I did not independently find

I found no B05 or B06 red flag that the transcripts do not support. Every
transcript-testable flag in both artifacts is SUPPORTED. Two qualifications:

- **B05 2F.5, renewable inflow (~Rs3,968cr) vs closing renewable book
  (Rs3,525cr), ~Rs443cr gap: SUPPORTED, soft.** The arithmetic is right
  (35.02% × 11,332 = 3,968; 19% × 18,554 = 3,525; 3,968 − 3,168 = ~800 implied
  Q4 renewable inflow vs a Rs357cr actual book increase). It rests on the
  assumption that "renewable" means the same thing in the inflow percentage and
  the order-book percentage, which no call states. B05 names this caveat itself,
  so the flag is not overstated.
- **B05's governance-silence flags (fraud, IFC qualification, GST search, NHAI
  SPV termination, auditor resignation, contingent liabilities, negative
  consolidated CFO): the transcript half is SUPPORTED — I confirm total silence
  across all four calls.** The existence and quantum of the underlying events
  come from B02/B03, which are outside my inputs; I neither confirm nor dispute
  them.

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS (6 checked, 6 confirmed, 0 wrong)

1. **FY26 revenue growth 10-15% → delivered.** Promise confirmed at Nov-2025 p.7
   ("about 10% to 15% from our last year performance"). Outcome confirmed at
   May-2026 p.5 (standalone Rs3,869cr, +14.3%; consolidated Rs4,022cr, +17.1%).
   I re-derived both from the quarterly prints: 818 + 787 + 970 + 1,294 = 3,869
   and 838 + 807 + 991 + 1,386 = 4,022. Direction CORRECT.
2. **Rs297cr HAM equity in three months → Rs2.4cr.** Promise at Nov-2025 p.10.
   Base Rs603.2cr at Oct-2025 (Nov-2025 p.5); outcome Rs605.6cr at Dec-2025
   (Feb-2026 p.4). Direction CORRECT. One refinement: the promise window is
   Nov-Jan and the measurement window is Oct-Dec, so the check is a two-month
   proxy; the Aug-2026 cumulative of Rs692cr (p.5) settles it — Rs89cr in eight
   months.
3. **Southern Ludhiana 80% land by December → 62%.** Promise at Nov-2025 p.7;
   outcome at Aug-2026 p.5. Direction CORRECT. B05's outcome anchor (p.6) is one
   page high; the quote is on PDF page 5.
4. **Malout sale proceeds before 31-Mar-2026 → completed in Q1 FY27.** Promise
   at Feb-2026 p.10 ("our target is we should get that money before 31st
   March"); May-2026 p.7 still expects it "in this month"; Aug-2026 p.3 confirms
   completion. Direction CORRECT on the transcript-testable half. The 16-Jun-2026
   completion date comes from B03 and is outside my inputs.
5. **VRK 11 / VRK 12 / Indore-Ujjain appointed dates → Jul/Aug-2026.** Promises
   at Nov-2025 p.7-8 and Feb-2026 p.7; outcome at Aug-2026 p.3. Direction
   CORRECT.
6. **11-11.5% EPC margin band held → FY26 standalone 12.6%.** Promise at
   Nov-2025 p.13; outcome at May-2026 p.5. Direction CORRECT, with a
   qualification B05 does not state: 12.6% is the headline standalone margin,
   FY25 was 12.8%, so the like-for-like direction across the two years is down,
   and the CFO's own position is that headline margin in earlier years carried
   bonus and royalty income the guided band excludes. The row is right; the
   "DELIVERED" framing is generous.

---

## PART 4: THE TWO NUMBERS THE TASK ASKED ME TO SETTLE

### 4.1 The May-2026 erratum: 71% is right, 41.5% is mislabelled

The erratum, May-2026 p.6, verbatim:
> "(It was erroneously mentioned that the unencumbered cash and unencumbered FDR
> stood at INR 266 crores and INR 146 crores, respectively. The actual figures
> should be read as INR 166 crores for unencumbered cash and INR 75 crores for
> unencumbered FDR.)"

Stated Rs266cr + Rs146cr = Rs412cr. Actual Rs166cr + Rs75cr = Rs241cr.
Difference Rs171cr.

- Overstatement relative to the truth: 171 ÷ 241 = **70.95%**, i.e. the stated
  figure was 71% above the real one.
- Cash line alone: 100 ÷ 166 = 60.2%. FDR line alone: 71 ÷ 75 = 94.7%.
- Restatement measured against the stated figure: 171 ÷ 412 = **41.5%**, i.e.
  the corrected figure is 41.5% below what was said.

Both statistics are arithmetically real; they answer different questions. "X was
overstated by Y%" conventionally means (stated − actual) ÷ actual, which is 71%.
B05 run 2 labels 41.5% as "a ~41.5% overstatement," which uses the wrong
denominator for that word.

B05's stated reason for the correction is also wrong. It says the 71% figure
"appears to conflate the FDR line's Rs71cr absolute rupee change with a
percentage." No conflation occurred: 171 ÷ 241 = 70.95% exactly. That the FDR
line happens to fall by Rs71cr is a coincidence, and it appears to be what led
stage 5 to the wrong diagnosis.

**Ruling: the earlier audit's ~71% was correct. B05 run 2's correction is wrong
on both the label and the reason.** The correct wording is either "overstated by
71%" or "the stated figure was cut by 41.5% on correction." B05's severity
upgrade to HIGH is sound and stands; only the magnitude sentence and the
orchestrator_note need fixing. This matters downstream because the sentence the
erratum sits inside is the one arguing "equity is not a problem with Ceigall, we
have amazing cash flow available with us."

### 4.2 The order-book roll-forward: B05's arithmetic is correct

I recomputed all three quarters from the transcripts before reading B05 (Part 1,
IF-13). All three gaps reproduce exactly: +Rs285cr, +Rs631cr, +Rs384cr, average
+Rs433cr, 2.1% / 3.4% / 2.1% of the closing book. Every input anchors:
Rs12,598cr (Nov-2025 p.3), Rs1,403cr and Rs991cr and Rs13,295cr (Feb-2026 p.4
and p.5), Rs6,014cr and Rs1,386cr and Rs18,554cr (May-2026 p.4, p.5, p.3),
"close to INR600" and Rs970cr and Rs18,568cr (Aug-2026 p.7, p.4, p.4).

One methodological refinement B05 should carry: the test uses consolidated
revenue against an order book whose basis the company never states. On standalone
revenue the gaps are +Rs264cr, +Rs539cr and +Rs315cr. The finding survives either
basis — same sign, same order of magnitude, same absence of explanation — so the
conclusion holds. B05's characterisation of the residual is fair, and the most
likely mechanism is the one B05 does not connect to it: the Nov-2025 order book
is explicitly stated to cover projects "under execution and at allotment stages"
(Nov-2025 p.3), and Feb-2026 counts L1 positions in a Rs8,500cr inflow claim that
the FY26 total contradicts (IF-14). The roll-forward gap and the L1-counting
problem are probably the same finding seen from two sides.

### 4.3 Three defects in the artifacts themselves

**D-1 (MAJOR). B05 run 2's citation anchors are one page high in the Nov-2025
and Aug-2026 transcripts.** The report opens by stating that all page citations
"use that PDF page number, independently re-derived by re-reading each transcript
in full." At least nine do not:

| B05 claim | B05 anchor | Actual PDF page |
|---|---|---|
| Rs200cr in "next 3 months" (Kapil) | Nov-25 p.12 | p.11 |
| Ramban-Banihal promises | Nov-25 p.12 | p.11 |
| "10 HAM projects" order-book line | Aug-26 p.5 | p.4 |
| Order book Rs18,568cr / consol revenue Rs970cr | Aug-26 p.5 | p.4 |
| Southern Ludhiana "only 62% available" | Aug-26 p.6 | p.5 |
| Rs253cr / Rs439cr / Rs692cr equity | Aug-26 p.6 | p.5 |
| Rs23cr Q1 FY27 infusion | Aug-26 p.9 | p.8 |
| "all 11 of our HAM projects" | Aug-26 p.10 | p.9 |
| "non-binding offer... under due diligence" | May-26 p.3 | p.4 |

The first eight are exactly the printed "Page N of M" header rather than the
`[PAGE N]` marker — the failure mode B06 wrote an 18-row correction log about.
B05's Feb-2026 and May-2026 anchors are mostly correct, so the method is
inconsistent within one report. Substance is unaffected in every case; a reader
following the anchor lands on the wrong page.

**D-2 (MINOR). B06 run 2 repeats the same off-by-one in the PNCINFRA Aug-2026
file**, the transcript carrying its only clean VERIFIED finding:
the rupee-level working-capital breakdown is on p.7, cited p.8; net working
capital 110 days is on p.8, cited p.9; the NHAI show-cause confirmation is on
p.9, cited p.10. (The Rs42 lakh/day penalty at p.12 and the 107km at p.3 are
correct.)

**D-3 (MAJOR). B06's Q4 comparative verdict overstates the peer contrast.**
B06 says two of three peers "reconcile cleanly" and HGINFRA shows only "a milder,
unexplained version" whose "mechanics are traceable." HGINFRA's own May-2026
prepared remarks do not reconcile: "the total equity requirements for these 11
HAM projects is around INR1,903 crores. As of March '26, INR1,210 crores being
infused. Of the remaining amount, INR414 crores is estimated for infusion in
FY27, followed by INR1,229 crores in FY28 and INR50 crores in FY29"
(HGINFRA-Concall_May_2026_Transcript.txt, p.6). Remaining is Rs693cr; the
schedule sums to Rs1,693cr — a Rs1,000cr internal gap in the same sentence. That
is not milder than Ceigall's failure; it is larger in rupees. The Q4 conclusion
that Ceigall's version is "more severe in degree" is not supported by this peer
set and should be softened.

Two lesser artifact notes: B06's report and YAML still describe Ceigall's
governance silence as "3-call" in five places, against a B05 that now covers four
calls; and B06 cites KNRCON's FY26 NHAI target of 7,500km and PNCINFRA's 4,500km
for the same year without noting the conflict (the awarded figures, 3,100km and
3,124km, do agree).

---

## PART 5: CREDIBILITY GRADE

**Concur with C, at the low end of C.**

The case against D is real and B05 states it correctly: revenue growth, order
inflow, the standalone deleveraging ratio and the margin band were all met or
beaten across four calls, and the company answers operational questions with
project-level numbers when asked. The case against B is what my own pass
reinforces. Two separate statements are false against the same call's own
arithmetic (Feb-2026 growth, May-2026 margin), not one. A second repeated evasion
runs alongside the four B05 already found — the same analyst asked whether the
margin beat was a one-off in two consecutive quarters and got a non-answer about
project starts both times. Two headline FY27 guidance items are never tested
against delivery anywhere: the 20-25% renewable revenue share and the minimum-15%
growth rate against a Q1 standalone print of 10.2%. And the single most
consequential structural disclosure of the year — that the IPO proceeds were
fully consumed in Q4 FY26, one quarter before a Rs859cr equity plan — arrives as
an aside in a Q&A answer about other income.

None of this moves the grade off C on its own, because the delivery record is
genuine. But the trajectory B05 names is right, and my pass adds to it rather
than softening it.

---

## PART 6: CONSOLIDATED FINDINGS

| # | Severity | Finding | Anchor |
|---|---|---|---|
| 1 | CRITICAL | MISSED repeated evasion: "was the margin beat a one-off?" asked by the same analyst in two consecutive quarters, answered both times with an unrelated list of newly started projects | Concall_May_2026 p.9; Concall_Aug_2026 p.7 |
| 2 | MAJOR | MISSED: Feb-2026 claim "our growth is much more than [10-15%]" is false against the same call's 9M growth of 7.6% standalone and 8.7% consolidated | Concall_Feb_2026 p.14 vs p.5-6 |
| 3 | MAJOR | MISSED: the May-2026 FY27 guidance that renewables contribute 20-25% of total revenue is absent from B05's guidance table and never tested against Aug-2026, where no renewable revenue is disclosed and two projects still lack PPA or transmission | Concall_May_2026 p.4; Concall_Aug_2026 p.5 |
| 4 | MAJOR | MISSED: Q1 FY27 standalone revenue growth of 10.2% against a "minimum 15%" FY27 guidance reaffirmed in the same call; only the 15.7% consolidated figure is quoted | Concall_Aug_2026 p.4, p.8 |
| 5 | MAJOR | MISSED: "We have 100% utilized the IPO proceeds in the last quarter of the FY26," plus the cessation of royalty income, disclosed only as an aside in a Q&A about other income | Concall_Aug_2026 p.11 |
| 6 | MAJOR | MISSED: cash disclosed on a different basis in each of three quarters (Rs225cr incl. FD, Rs241cr unencumbered corrected, Rs320cr FDs); the Rs320cr figure appears nowhere in B05 | Concall_Feb_2026 p.10; Concall_May_2026 p.6; Concall_Aug_2026 p.11 |
| 7 | MAJOR | MISSED: "We have 1.5 years to dilute another 8% also," an unexplained dilution or minimum-public-shareholding overhang stated once and never repeated across three later calls | Concall_Nov_2025 p.12 |
| 8 | MAJOR | B05 arithmetic wrong: the erratum is a 71.0% overstatement (171÷241), not 41.5% (171÷412, which is the restatement-down); B05's stated reason, that 71% conflates an absolute rupee change with a percentage, is false | Concall_May_2026 p.6; 05-concall.md 4D and B05 red_flags/orchestrator_note |
| 9 | MAJOR | B05 citation anchors are one page high in at least nine places in the Nov-2025 and Aug-2026 transcripts, matching the printed header the report states it avoided | See Part 4.3 table |
| 10 | MAJOR | B06 Q4 overstates the peer contrast: HGINFRA's own HAM equity schedule fails to reconcile by ~Rs1,000cr (Rs693cr remaining vs Rs1,693cr scheduled), so its drift is not "milder" than Ceigall's | HGINFRA-Concall_May_2026 p.6; 06-peers.md Q4 |
| 11 | MAJOR | Under-weighted: the Northern Ayodhya execution collapse to ~Rs42cr is answered with a denial, a weather excuse and a milestone concession in one breath; B05 rates it "plausible and seasonal, not disputed" | Concall_Aug_2026 p.4-5; 05-concall.md 2B |
| 12 | MAJOR | Under-weighted: Ceigall posts its best quarterly margin of the year (14.1% standalone, Q4 FY26) in the exact quarter HGINFRA's falls to 9.37% on unrecovered escalation, and denies any input-cost impact; the juxtaposition is not drawn in either artifact | Concall_May_2026 p.5, p.9; HGINFRA-Concall_May_2026 p.6 |
| 13 | MINOR | B06 repeats the printed-header off-by-one in the PNCINFRA Aug-2026 file at three anchors (p.8→7, p.9→8, p.10→9), the file carrying its only clean VERIFIED finding | PNCINFRA-Concall_Aug_2026 p.7, p.8, p.9 |
| 14 | MINOR | B06 report and YAML still describe Ceigall's governance silence as "3-call" in five places against a four-call B05 | 06-peers.md Q5, Part 4; B06 flags |
| 15 | MINOR | MISSED: Nov-2025 bid pipeline stated at Rs14,320cr while its own components sum to Rs14,382cr, quoted as Rs14,000cr elsewhere in the call, and an analyst's Rs16,000cr goes uncorrected | Concall_Nov_2025 p.6, p.9, p.10 |
| 16 | MINOR | MISSED: Ceigall's MoRTH FY27 allocation of ~Rs3.1 trillion against PNCINFRA's Rs2.9 trillion for the same year, both stated as +8% | Concall_Feb_2026 p.3; PNCINFRA-Concall_May_2026 p.5 |
| 17 | MINOR | MISSED: the May-2026 filed transcript carries "one INR21,160 crores project" (Sahebganj is Rs2,160cr, correct on p.3 of the same file) uncorrected, in the same document that carries a written cash erratum | Concall_May_2026 p.12 |
| 18 | MINOR | MISSED: Ramban-Banihal figures do not cohere inside one exchange (Rs385cr for both projects vs Rs369cr for one; 20% of tunnel = Rs180cr; 54% physical vs 45% financial) | Concall_Nov_2025 p.11 |
| 19 | MINOR | MISSED: Feb-2026 leaves an analyst's "INR3,500 crores order book of solar and BESS" uncorrected against the Rs3,168cr cumulative renewable orders stated in the same call | Concall_Feb_2026 p.4, p.9 |
| 20 | MINOR | MISSED: Feb-2026 claims "seven of our projects have completed ahead of schedule" while the same call discloses Jalbehra is late and awaiting an EOT with bonus eligibility unresolved; the EOT is never revisited | Concall_Feb_2026 p.4, p.11 |
| 21 | MINOR | MISSED: B06 uses KNRCON's 7,500km and PNCINFRA's 4,500km FY26 NHAI targets side by side without noting the conflict | KNRCON-Concall_Jun_2026 p.3; PNCINFRA-Concall_May_2026 p.4 |

Counts: CRITICAL 1, MAJOR 11, MINOR 9.

---

## COVERAGE ARITHMETIC

Independent company red flags found: **43** (IF-1 to IF-43). Findings against the
pipeline's own artifacts (D-1, D-2, D-3 in Part 4.3) are excluded from this
denominator; they appear in Part 6 as findings but not as coverage items.

- CAUGHT 20 → **acceptance_rate = 20 ÷ 43 = 47%**
- CAUGHT + PARTIALLY CAUGHT = 20 + 10 = 30 →
  **redflag_coverage = 30 ÷ 43 = 70%**
- MISSED 13

By severity: CRITICAL 3 of 4 caught (75%), 4 of 4 surfaced (100%).
MAJOR 16 of 27 caught (59%), 24 of 27 surfaced (89%).
MINOR 1 of 12 caught (8%), 3 of 12 surfaced (25%).
CRITICAL + MAJOR only: 19 of 31 caught (61%), 28 of 31 surfaced (90%).

The two rates differ because they answer different questions. acceptance_rate
follows the rubric literally (caught ÷ independent flags found) and gives no
credit for a finding upstream reached but under-weighted. redflag_coverage
follows the task's definition — the share of my findings upstream had already
surfaced — and counts a PARTIALLY CAUGHT item as surfaced, because it is on the
page and a reader would meet it.

Judgement on the 60% floor. The strict 47% is dominated by the MINOR tail: I
enumerated twelve minor items and B05 carries one of them. On the flags that
carry thesis weight the picture is different — 61% of CRITICAL and MAJOR flags
are caught outright and 90% are at least surfaced, against 48% at the last audit.
The remediation worked. What did not clear is the one CRITICAL miss (a second
repeated evasion, two quarters, same analyst, same question) and two untested
FY27 guidance items, which are the specific gaps to close rather than a reason to
re-run the whole stage.

---

```yaml
stage: B12b
company: "CEIGALL"
run_date: "2026-09-06"
model: claude-opus-4-8
status: complete
independent_flags_found: 43
caught: 20
partially_caught: 10
missed:
  - {severity: "CRITICAL", item: "Repeated evasion, 2 consecutive quarters: 'was the margin beat a one-off?' asked by Mahesh Patil (ICICI Securities) and answered both times with an unrelated list of newly started projects, never yes or no", anchor: "Concall_May_2026_Transcript.txt p.9; Concall_Aug_2026_Transcript.txt p.7"}
  - {severity: "MAJOR", item: "Feb-2026 claim 'we were always guiding 10% to 15%, our growth is much more than that' is false against the same call's 9M FY26 growth of 7.6% standalone and 8.7% consolidated", anchor: "Concall_Feb_2026_Transcript.txt p.14 vs p.5-6"}
  - {severity: "MAJOR", item: "May-2026 FY27 guidance that renewables contribute 20-25% of total revenue is absent from B05's guidance table and never tested; Aug-2026 discloses no renewable revenue and Morena/Rewa still lack PPA or transmission", anchor: "Concall_May_2026_Transcript.txt p.4, p.11; Concall_Aug_2026_Transcript.txt p.5"}
  - {severity: "MAJOR", item: "Q1 FY27 standalone revenue growth of 10.2% against a 'minimum 15%' FY27 guidance reaffirmed in the same call; only the 15.7% consolidated figure is quoted, the shortfall never addressed", anchor: "Concall_Aug_2026_Transcript.txt p.4, p.8"}
  - {severity: "MAJOR", item: "'We have 100% utilized the IPO proceeds in the last quarter of the FY26' plus cessation of royalty income, disclosed only as an aside answering a question about other income, one quarter before a Rs859cr FY27 equity plan", anchor: "Concall_Aug_2026_Transcript.txt p.11"}
  - {severity: "MAJOR", item: "Cash disclosed on a different basis in each of three quarters: Rs225cr including FD (Dec-25), Rs241cr unencumbered after erratum (Mar-26), Rs320cr FDs (Jun-26); the Rs320cr figure appears nowhere in B05", anchor: "Concall_Feb_2026_Transcript.txt p.10; Concall_May_2026_Transcript.txt p.6; Concall_Aug_2026_Transcript.txt p.11"}
  - {severity: "MAJOR", item: "'We have 1.5 years to dilute another 8% also' — an unexplained dilution or minimum-public-shareholding overhang stated once and never repeated on any of three later calls; an Aug-2026 analyst's 'post-QIP' premise also left uncorrected", anchor: "Concall_Nov_2025_Transcript.txt p.12; Concall_Aug_2026_Transcript.txt p.12"}
  - {severity: "MINOR", item: "Nov-2025 bid pipeline stated at Rs14,320cr while its own components sum to Rs14,382cr, quoted as Rs14,000cr elsewhere in the same call, and an analyst's Rs16,000cr left uncorrected", anchor: "Concall_Nov_2025_Transcript.txt p.6, p.9, p.10"}
  - {severity: "MINOR", item: "Ceigall's MoRTH FY27 allocation of ~Rs3.1 trillion against PNCINFRA's Rs2.9 trillion for the same year, both stated as +8%", anchor: "Concall_Feb_2026_Transcript.txt p.3; PNCINFRA-Concall_May_2026_Transcript.txt p.5"}
  - {severity: "MINOR", item: "The May-2026 filed transcript carries 'one INR21,160 crores project' (Sahebganj is Rs2,160cr, correct on p.3 of the same file) uncorrected, in the same document that carries a written cash erratum", anchor: "Concall_May_2026_Transcript.txt p.12"}
  - {severity: "MINOR", item: "Ramban-Banihal figures do not cohere inside one exchange: Rs385cr balance for both projects vs Rs369cr for one alone; 20% of tunnel work = Rs180cr; 54% physically vs 45% financially complete", anchor: "Concall_Nov_2025_Transcript.txt p.11"}
  - {severity: "MINOR", item: "Feb-2026 leaves an analyst's 'INR3,500 crores order book of solar and BESS' uncorrected against the Rs3,168cr cumulative renewable orders stated in the same call", anchor: "Concall_Feb_2026_Transcript.txt p.4, p.9"}
  - {severity: "MINOR", item: "Feb-2026 claims 'seven of our projects have completed ahead of schedule' while the same call discloses Jalbehra is late awaiting an EOT with bonus eligibility unresolved; the EOT is never revisited in May-2026 or Aug-2026", anchor: "Concall_Feb_2026_Transcript.txt p.4, p.11"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "concur with C, at the low end — the delivered guidance record genuinely argues against D, but two separate claims are false against their own call's arithmetic (Feb-2026 growth, May-2026 margin), not one, and a second two-quarter repeated evasion runs alongside the four B05 found"
findings:
  - {severity: "CRITICAL", location: "B05 2E repeated-question tracker", claim: "MISSED repeated evasion: margin one-off question asked in two consecutive quarters, non-answer both times; Mahesh Patil appears nowhere in B05", anchor: "Concall_May_2026 p.9; Concall_Aug_2026 p.7"}
  - {severity: "MAJOR", location: "B05 2A / 2C", claim: "MISSED: Feb-2026 growth claim false against the same call's 9M figures", anchor: "Concall_Feb_2026 p.14 vs p.5-6"}
  - {severity: "MAJOR", location: "B05 1B guidance table", claim: "MISSED: FY27 renewable revenue guidance of 20-25% of total absent entirely and never tested", anchor: "Concall_May_2026 p.4"}
  - {severity: "MAJOR", location: "B05 1B / 2A", claim: "MISSED: Q1 FY27 standalone +10.2% against reaffirmed minimum-15% guidance, gap never addressed", anchor: "Concall_Aug_2026 p.4, p.8"}
  - {severity: "MAJOR", location: "B05 2D / 4D", claim: "MISSED: IPO proceeds 100% utilised in Q4 FY26 and royalty income ceased, disclosed only as a Q&A aside", anchor: "Concall_Aug_2026 p.11"}
  - {severity: "MAJOR", location: "B05 1B guidance table", claim: "MISSED: cash basis changes every quarter; the Rs320cr Jun-2026 FD figure is absent from B05", anchor: "Concall_Aug_2026 p.11"}
  - {severity: "MAJOR", location: "B05 4D", claim: "MISSED: 'We have 1.5 years to dilute another 8% also', an unexplained dilution/MPS overhang never repeated", anchor: "Concall_Nov_2025 p.12"}
  - {severity: "MAJOR", location: "B05 4D red flag row 5; B05 red_flags; B05 orchestrator_note", claim: "Arithmetic wrong: the erratum is a 71.0% overstatement (171/241), not 41.5% (171/412 is the restatement-down); the stated reason, that 71% conflates an absolute rupee change with a percentage, is false — 171/241 = 70.95% exactly. The earlier audit's 71% was correct; the severity upgrade to HIGH stands", anchor: "Concall_May_2026 p.6"}
  - {severity: "MAJOR", location: "05-concall.md citation convention paragraph", claim: "At least nine B05 anchors are one page high in the Nov-2025 and Aug-2026 transcripts, matching the printed 'Page N of M' header rather than the [PAGE N] marker the report says it used", anchor: "See report Part 4.3 table"}
  - {severity: "MAJOR", location: "06-peers.md Q4", claim: "Peer contrast overstated: HGINFRA's own May-2026 HAM equity schedule fails to reconcile by ~Rs1,000cr (Rs1,903cr total less Rs1,210cr infused = Rs693cr remaining, against Rs414 + Rs1,229 + Rs50 = Rs1,693cr scheduled), so its drift is not 'milder' than Ceigall's", anchor: "HGINFRA-Concall_May_2026 p.6"}
  - {severity: "MAJOR", location: "B05 2B excuse pattern", claim: "Under-weighted: the Northern Ayodhya collapse to ~Rs42cr is answered with a denial, a rain excuse and a milestone concession in one breath; B05 calls it 'plausible and seasonal, not disputed'", anchor: "Concall_Aug_2026 p.4-5"}
  - {severity: "MAJOR", location: "B05 4D / B06 Q9", claim: "Under-weighted: Ceigall's best quarterly margin of the year (14.1% standalone Q4 FY26) lands in the quarter HGINFRA's falls to 9.37% on unrecovered escalation, with any input-cost impact denied; neither artifact juxtaposes the two", anchor: "Concall_May_2026 p.5, p.9; HGINFRA-Concall_May_2026 p.6"}
  - {severity: "MINOR", location: "06-peers.md Q10, Q6, Q5", claim: "B06 repeats the printed-header off-by-one in the PNCINFRA Aug-2026 file at three anchors (p.8 should be p.7, p.9 should be p.8, p.10 should be p.9)", anchor: "PNCINFRA-Concall_Aug_2026 p.7, p.8, p.9"}
  - {severity: "MINOR", location: "06-peers.md Q5 / Part 4 / B06 flags", claim: "B06 still describes Ceigall's governance silence as '3-call' in five places against a four-call B05 run 2", anchor: "06-peers.md Q5, Part 4"}
  - {severity: "MINOR", location: "B05 Section 1", claim: "MISSED: Nov-2025 bid total Rs14,320cr vs components summing Rs14,382cr; Rs14,000cr elsewhere; analyst's Rs16,000cr uncorrected", anchor: "Concall_Nov_2025 p.6, p.9, p.10"}
  - {severity: "MINOR", location: "B05 3B / B06 2A", claim: "MISSED: MoRTH FY27 allocation Rs3.1trn (Ceigall) vs Rs2.9trn (PNCINFRA), both stated as +8%, never cross-checked", anchor: "Concall_Feb_2026 p.3; PNCINFRA-Concall_May_2026 p.5"}
  - {severity: "MINOR", location: "B05 2B", claim: "MISSED: a 10x order-value error ('INR21,160 crores') left uncorrected in the same filed transcript that carries a written cash erratum", anchor: "Concall_May_2026 p.12"}
  - {severity: "MINOR", location: "B05 2A Ramban-Banihal row", claim: "MISSED: the Ramban-Banihal figures do not cohere within the Nov-2025 exchange itself", anchor: "Concall_Nov_2025 p.11"}
  - {severity: "MINOR", location: "B05 2F.5", claim: "MISSED: Feb-2026 leaves an analyst's Rs3,500cr solar/BESS order-book figure uncorrected against Rs3,168cr stated in the same call", anchor: "Concall_Feb_2026 p.4, p.9"}
  - {severity: "MINOR", location: "B05 2A", claim: "MISSED: 'seven projects completed ahead of schedule' alongside Jalbehra's unresolved EOT and bonus, never revisited", anchor: "Concall_Feb_2026 p.4, p.11"}
  - {severity: "MINOR", location: "06-peers.md 2A / Part 3", claim: "MISSED: KNRCON's 7,500km and PNCINFRA's 4,500km FY26 NHAI targets used side by side without noting the conflict (awarded figures 3,100km and 3,124km do agree)", anchor: "KNRCON-Concall_Jun_2026 p.3; PNCINFRA-Concall_May_2026 p.4"}
critical_count: 1
major_count: 11
minor_count: 9
acceptance_rate: 47
redflag_coverage: 70
coverage_note: "Denominator for both rates is 43 independent company-directed red flags (IF-1 to IF-43), built from the four Ceigall transcripts and targeted peer cross-checks BEFORE any upstream artifact was opened. Three findings against the artifacts themselves (B05 anchor errors, B06 anchor errors, B06 Q4 overstatement) are excluded from the denominator because coverage measures how much of the company red-flag surface upstream reached, not artifact hygiene; they appear in findings. acceptance_rate = CAUGHT / 43 = 20/43 = 47%, following the rubric literally (no credit for partial). redflag_coverage = (CAUGHT + PARTIALLY CAUGHT) / 43 = 30/43 = 70%, following the task definition of 'already surfaced', where PARTIALLY CAUGHT means upstream carries the item but under-weighted, mis-severitied, or without the specific arithmetic. By severity: CRITICAL 3/4 caught, 4/4 surfaced; MAJOR 16/27 caught, 24/27 surfaced; MINOR 1/12 caught, 3/12 surfaced. CRITICAL+MAJOR alone: 19/31 caught (61%), 28/31 surfaced (90%). The strict 47% is dominated by a twelve-item MINOR tail of which B05 carries one; on thesis-weight flags the remediation clearly worked, up from the 48% measured at the last audit. The residual gaps are specific and fixable: one CRITICAL repeated evasion (the margin one-off question, May-2026 p.9 and Aug-2026 p.7), two untested FY27 guidance items (renewable revenue share, minimum-15% growth vs a 10.2% Q1), and the IPO-proceeds-exhausted disclosure. On the two numbers the task asked me to settle: the May-2026 erratum is a 71.0% overstatement (171/241), so the earlier audit was right and B05 run 2's 41.5% is the restatement-down mislabelled, with a false diagnosis attached; and B05's order-book roll-forward gaps of +Rs285cr, +Rs631cr and +Rs384cr reproduce exactly on independent recomputation (the finding also survives a standalone-revenue basis at +264/+539/+315)."
```
