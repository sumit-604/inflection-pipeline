# STAGE 12B: VERIFIER B — RED FLAGS (INDEPENDENT AUDIT) — KABRAEXTRU

**Company:** Kabra Extrusiontechnik Ltd (KABRAEXTRU) | **Run date:** 2026-09-05
**Verifier:** B (red flags) | **Model:** Opus 4.8 | **Emits:** B12b

## MODE AND SCOPE

This company holds no earnings calls. Per the orchestrator's NO-CONCALL MODE
adaptation, I audited the pipeline's communication analysis against the two
annual reports instead of against main-company transcripts.

What I read myself, fresh, before opening any pipeline output:

| Source | File | Coverage |
|---|---|---|
| AR FY2024-25 | `runs/kabraextru-2026-09-05/inputs/annual-report/Annual_Report_2025.txt` | Chairman's letter, Notice, Director's Report, all five Annexures, MD&A, Corporate Governance Report, targeted note reads |
| AR FY2025-26 | `runs/kabraextru-2026-09-05/inputs/annual-report/Annual_Report_2026.txt` | Same sections, plus Key Audit Matters, Notes 7, 9, 23, 24, 25, 38, 47, AOC-1, MR-3 |
| Investor deck, Dec-2023 quarter | `runs/kabraextru-2026-09-05/inputs/presentation/Investor_Presentation_1.txt` | All 32 pages |
| RAJOOENG Q4 FY23, 16-May-2023 | `.../peer-concalls/RAJOOENG-Concall_May_2023_Transcript.txt` | Full |
| RAJOOENG Q2 FY24, 6-Nov-2023 | `.../peer-concalls/RAJOOENG-Concall_Nov_2023_Transcript.txt` | Full |
| RAJOOENG Q4 FY24, 18-Apr-2024 | `.../peer-concalls/RAJOOENG-Concall_Apr_2024_Transcript.txt` | Full |
| RAJOOENG Q2 FY25, 22-Oct-2024 (filename mislabeled) | `.../peer-concalls/RAJOOENG-Concall_Nov_2025_Transcript.txt` | Full |
| HBLENGINE FY25 AGM, 25-Sep-2025 | `.../peer-concalls/HBLENGINE-Concall_Sep_2025_Transcript.txt` | Full |

Then I read B05 (`outputs/reports/05-concall.md`) and B06
(`outputs/reports/06-peers.md`). No other pipeline output was read.

**Anchor convention.** Every page anchor is the PDF page marker
(`===== PAGE n =====`) in the page-marked text twin. Financial-statement items
also carry the note number, which is source-stable.

**Scope note for the orchestrator.** The orchestrator's instruction placed
"notes" inside my audit scope for the B05 comparison. Several of my strongest
independent flags sit in the financial-statement notes rather than in the
narrative sections. If the orchestrator judges the notes to belong to B02/B04
rather than B05, five of my MISSED rows (numbers 3, 4, 5, 7, 10) move out of
B05's fair scope and the acceptance rate rises to 39%. I have not made that
judgement for the orchestrator. I report the strict number and the arithmetic
so the choice is visible.

---

## PART 1: INDEPENDENT RED-FLAG LIST

Thirty red-flag-grade items, from the raw sources alone.

### A. Internal contradictions inside a single document

**1. FY26 chairman's letter reports an EBITDA that the same report contradicts,
and omits the loss entirely.**
The letter says "EBITDA stood at ₹ 10 crores" (AR FY26 p.4). The MD&A Financial
Performance Snapshot in the same report says EBITDA ₹13.05 Cr (AR FY26 p.37).
The gap is 30% on the headline profit metric. The letter also drops PAT
altogether. The FY25 letter gave revenue, mix, EBITDA, EBITDA margin, PAT and
PAT margin (AR FY25 p.4). The FY26 letter gives revenue, mix and EBITDA only.
The words "loss", "PAT" and "profit after tax" do not appear in it. The company
reported a standalone net loss of ₹244.28 lakh that year (AR FY26 p.17).

**2. FY25 MD&A states three different PAT figures for the same year, two of
them on the same page.**
The Financial Performance Snapshot table gives PAT 34 and PAT margin 7.2%
(AR FY25 p.38). The prose immediately below the table says "KET's PAT stood at
₹ 32 crores. PAT margin stood at 6.8% during FY25" (AR FY25 p.38). The
chairman's letter says "profit after tax (PAT) stood at ₹33.9 crores, with a
PAT margin of 7.2%" (AR FY25 p.4). Three numbers, one year, one document.

**3. Prior-year comparatives were restated silently.**
The FY25 Director's Report gives standalone Employee benefits expense of
₹5,907.53 lakh and Other Expenses of ₹7,473.91 lakh (AR FY25 p.19; same figures
in the audited P&L at Notes 26 and 29). The FY26 Director's Report restates the
FY25 comparatives to ₹6,328.67 lakh and ₹7,052.77 lakh (AR FY26 p.17). The shift
is exactly ₹421.14 lakh, offsetting, in both the standalone and the consolidated
columns. Total expenses are unchanged at ₹45,639.87 lakh, so the restatement is
a reclassification between two expense heads. The only disclosure is boilerplate:
"Previous year's figures have been regrouped wherever considered necessary"
(AR FY26 standalone Note 47). No amount, no head, no reason. The effect matters:
FY26 employee cost reads as +20.4% against the restated base and +28.9% against
the base the company published a year earlier.

**4. An unexplained "Other" line inside other income determines the reported
loss.** CRITICAL.
Note 23 lists "Other ... 1,668.41" for FY26 against "22.91" for FY25 (AR FY26
p.95). That is ₹16.68 Cr, a 73x jump, with no label and no explanatory note. The
standalone loss before tax that year is ₹423.21 lakh (AR FY26 p.17). Without this
single unexplained line the loss would be roughly eight times larger. The same
note also shows "Provisions written back" of ₹370.29 lakh (FY26) and ₹610.09 lakh
(FY25), which flatter both years. The FY26 report states elsewhere that warranty
provisions against Hero Electric sales were reversed (AR FY26 p.88). Neither the
chairman's letter nor the MD&A mentions any of this. The reported loss is not
explicable from the disclosed operating figures alone.

**5. Receivable quality deteriorated sharply while the MD&A reported an
improvement.**
Note 9 ageing at 31-Mar-2026: gross ₹9,052.43 lakh, of which ₹471.76 lakh is
1-2 years overdue, ₹2,021.56 lakh is 2-3 years overdue and ₹1,935.36 lakh is more
than 3 years overdue (AR FY26 p.88). That is ₹4,428.68 lakh, 48.9% of gross
receivables, more than one year past due. The FY25 equivalent is 41.8%. Provision
against the over-three-year bucket is ₹455.13 lakh, 23.5% coverage, so ₹14.80 Cr
of receivables more than three years overdue is still carried as recoverable. The
MD&A's only comment on receivables is "Debtors Turnover 5.20%" with no reason and
no narrative (AR FY26 p.37).

**6. The "asset-light" Key Strength is contradicted by the company's own segment
note.**
MD&A Key Strength 5 is headed "Technology-Agnostic and Asset-Light Approach in
Energy Business" and says the approach works "without heavy capital investments"
(AR FY26 p.36). Note 38 shows Battery Division segment assets of ₹36,437.25 lakh,
50.1% of total segment assets of ₹72,775.30 lakh, against segment revenue of
₹13,610.84 lakh and a segment loss of ₹4,334.64 lakh (AR FY26 p.105-106). The
same MD&A page says roughly ₹250 Cr has gone into Geon (p.36). Asset turn on the
battery segment is 0.37x. The claim and the note cannot both stand.

**7. The mandatory Key Financial Ratios table is internally unreconcilable and
incomplete.**
The table reports "Interest Coverage Ratio 39.20%" for FY26 (AR FY26 p.37). The
table directly above it reports EBIT falling from ₹45 Cr to ₹7.16 Cr, and the
Director's Report shows finance cost rising from ₹1,117.31 lakh to ₹1,139.25 lakh
(AR FY26 p.17). No definition of interest coverage produces an improvement from
those two inputs. Separately, SEBI requires a reason for any change of 25% or
more. Interest Coverage (+39.20%) and Return on Capital Employed (−86.50%) both
clear that threshold and both have the "Reasons for Variation" cell left blank.

**8. A mandatory explanatory disclosure is factually wrong.**
The FY26 ratio table explains the inventory-turnover move as "Due to increase in
inventory and Lower sale" (AR FY26 p.37). Note 7 shows inventory FELL, from
₹29,014.77 lakh to ₹28,538.08 lakh (AR FY26 p.87). The sentence is copied
verbatim from the FY25 table, where it was true (AR FY25 p.38). It was carried
forward without being checked.

### B. Disclosure timing and governance

**9. The second credit downgrade contradicts the "no material changes"
statement, and the same silence occurred in both years.**
The Corporate Governance Report discloses that the long-term rating moved to
CRISIL A-/Stable and the short-term rating to CRISIL A2+ with effect from
13-May-2026, "Downgraded from" A/Negative and A1 respectively (AR FY26 p.51).
The Director's Report was signed on 28-May-2026, fifteen days later, and states
at item 12: "There are no material changes and commitments affecting the
financial position of your Company, which have occurred between the end of the
year and date of this report" (AR FY26 p.20). The prior downgrade is disclosed in
the FY25 report on the same pattern: long term A+/Negative to A/Negative with
effect from 5-Apr-2025, reason "Due to operating performance till December 31,
2024" (AR FY25 p.49). Neither year's chairman's letter or MD&A mentions a
downgrade. This is the same omission two reporting periods running, and the FY25
report carries the same structural defect at its own item 14, which asserts no
material changes on the very day the CEO of the Extrusion Division resigned
(AR FY25 p.20, p.22).

**10. The named BMS subsidiary has collapsed and disappeared from the
narrative.**
AOC-1 shows Varos Technology Pvt Ltd turnover falling from ₹372.99 lakh to
₹17.84 lakh, a 95% decline; loss after tax widening from ₹221.24 lakh to
₹291.49 lakh; and accumulated reserves of negative ₹557.17 lakh against share
capital of ₹1.00 lakh, that is, negative net worth (AR FY25 p.25; AR FY26 p.23).
Varos is the company that carries the battery-management-system claim. The
Dec-2023 deck lists "Acqui-hired Team from Varos Technologies" as an R&D pillar
(deck p.17). AR FY25 Key Strength 5 says "In FY22, KET fully acquired Varos
Technology, a Pune-based company specializing in the development of comprehensive
battery management systems ... cloud-powered AI analytics" (AR FY25 p.37). AR
FY26 does not mention Varos anywhere in the narrative.

**11. Heritage and scale claims were quietly shrunk, and contradict each other
inside the FY26 report.**
AR FY25 MD&A: "With over six decades of industry experience, a track record of
more than 15,000 successful installations" (AR FY25 p.36). AR FY26 MD&A: "With a
legacy of over four decades", and the installation count is gone (AR FY26 p.35).
The FY26 chairman's letter in the same document says the inverter launch is
"KET's first direct-to-consumer (D2C) venture in its 60-year journey"
(AR FY26 p.5). Four decades and sixty years, same report.

**12. A JV presented as a pillar of strength was divested and removed without
narrative comment.**
The Dec-2023 deck lists three technical collaborations under "Pillars of
Strength", including "Penta: A 50:50 JV with Penta SRL, Italy for auto-feeding
systems" (deck p.24). AR FY25's Technical Collaboration table lists only
Battenfeld-Cincinnati and Extron Mecanor (AR FY25 p.37). The divestment is
disclosed in the Director's Report and AOC-1, where the holding is stated as
49.94%, not 50:50 (AR FY25 p.21, p.25). The MD&A, where the claim originally
lived, never says the pillar was removed. AR FY26 drops the collaboration table
entirely, including the Battenfeld-Cincinnati tie-up dating to 1983.

**13. FY25 profit was materially flattered by a one-off that the chairman's
letter does not mention.**
FY25 standalone profit before exceptional items is ₹3,343.28 lakh. The reported
figure of ₹4,192.26 lakh includes an exceptional item of ₹848.98 lakh, the gain
on the Penta divestment (AR FY25 p.19). The chairman's letter reports "PAT stood
at ₹33.9 crores, with a PAT margin of 7.2%" with no mention that roughly a
quarter of pre-tax profit was a divestment gain (AR FY25 p.4). The FY26 report
then measures FY26 against that flattered base throughout.

**14. The FY26 secretarial audit records a statutory breach.**
Form MR-3 states that shares relating to unclaimed FY2017-18 dividend were
transferred to the IEPF Authority on 31-Oct-2025, and that "the said transfer was
made beyond the timelines prescribed under Section 124 of the Act read with Rule
6" (AR FY26 p.24). The Director's Report discloses it at item 23 (AR FY26 p.21).
This is the one clear volunteered negative in either report and it counts in
management's favour as well as against.

**15. An independent director was re-badged sixteen days after his independence
expired.**
Mr Bajrang Lal Bagra completed his second consecutive five-year term as
Independent Director on 26-Aug-2025 and was appointed Non-Executive
Non-Independent Director with effect from 11-Sep-2025 (AR FY26 p.18, p.25). The
FY26 board composition table lists him twice, once under each category
(AR FY26 p.39-40). The step is lawful. The optics are a flag.

**16. Customer concentration appears in the notes and in neither risk section.**
Note 38 discloses one customer at 19.11% of FY26 revenue, and two customers at
26.94% in FY25 (AR FY26 p.106). The MD&A Risks and Challenges sections in both
years list technology obsolescence, competition, imports, supply chain and
currency. Neither lists customer concentration or customer credit risk, in the
same reports that carry a ₹30.39 Cr receivable from an insolvent OEM.

### C. Claim drops, walkbacks and unanchored new claims

**17. The ~40% extrusion market share claim was dropped without a word.**
Claimed in the deck as "Industry leader with 40% market share (FY23)" (deck p.12,
p.24) and in AR FY25 as "~40% market share in its product category as on FY25"
(AR FY25 p.37). Absent from AR FY26; Key Strength 1 is reworded to "Established
Market Leadership in Core Business" with no number (AR FY26 p.36). Extrusion
segment revenue fell 13.2% that year, from ₹36,285.02 lakh to ₹31,488.99 lakh
(AR FY26 p.105).

**18. The R&D spend collapsed while the report claimed R&D acceleration.**
Extrusion R&D fell from ₹1,116.62 lakh to ₹367 lakh, down 67.1% (AR FY25 p.30;
AR FY26 p.28). Geon R&D fell from ₹866.78 lakh to ₹185.18 lakh, down 78.6%
(AR FY25 p.31; AR FY26 p.29). Combined, ₹1,983.40 lakh to ₹552.18 lakh, from 4.2%
to 1.2% of revenue. The same FY26 annexure that discloses the ₹185.18 lakh says
Geon "has accelerated its R&D" (AR FY26 p.28).

**19. The battery segment loss widened while the report promised
profitability.**
Note 38: Battery Division segment result moved from negative ₹2,553.28 lakh to
negative ₹4,334.64 lakh, a 69.8% wider loss, on segment revenue up 7.2% from
₹12,698.12 lakh to ₹13,610.84 lakh (AR FY26 p.105). The MD&A says "The battery
business is expected to move towards profitability as volumes scale up"
(AR FY26 p.38) and never reconciles the two.

**20. The India EV battery-pack market the FY26 report cites is smaller than
Geon's own plausible share of it.**
AR FY25 cites the India EV battery market at USD 2.22 bn in 2024 rising to
USD 13.89 bn by 2033 (AR FY25 p.5). AR FY26 cites the India EV battery pack
market at USD 39.39 mn in 2025, USD 53.76 mn in 2026, reaching USD 254.59 mn by
2031 (AR FY26 p.34). The two are roughly 100x apart. Worse: Geon's own FY26
revenue of ₹136.11 Cr is about USD 15 mn, which would be roughly 28% of the
entire Indian market as the FY26 report itself sizes it. The report cites a
market its own division could not plausibly fit inside. AR FY25 is also
internally inconsistent on the base year of the same figure: the chairman's
letter says USD 2.22 bn in 2024 (p.5) and the MD&A says USD 2.22 bn in 2023
(p.35).

**21. The plastic pipes market was restated downward by roughly 2.7x with no
acknowledgement.**
AR FY25 sizes the Indian PVC pipes and fittings market at approximately ₹450 bn
in 2024, "projected to exceed ₹500 billion by FY2025", CAGR 10.8% (AR FY25 p.4-5,
p.35). AR FY26 sizes the India plastic pipes market at USD 2.10 bn in 2025,
roughly ₹185 bn, growing at 6.30% to USD 3.65 bn by 2034, sourced to IMARC
(AR FY26 p.33). Same market, same year, figures 2.7x apart, source switched, no
reconciliation.

**22. The extrusion machinery market CAGR nearly doubled between consecutive
reports.**
AR FY25: USD 6.9 bn in 2024 to USD 10 bn by 2030, CAGR 3.9%, sourced to
imarcgroup and futuremarketinsights (AR FY25 p.4, p.34). AR FY26: USD 7.74 bn in
2025 to USD 8.24 bn in 2026 to USD 12.22 bn by 2032, CAGR 6.72%, sourced to
Research and Markets (AR FY26 p.4, p.33). The 2024 and 2025 base figures alone
imply 12% growth in one year against the 3.9% the company published a year
earlier.

**23. The two new quantified Geon claims are unanchored and mutually
implausible.**
"The Company has secured a ~INR 150 Crore order for execution in the upcoming
year" and "At optimal levels, the existing facility can generate INR 1,500+ crore
revenue" (AR FY26 p.37). No counterparty, no terms, no date, no utilisation rate.
Held against the same report's claim of "approximately 7 GWh" installed pack
capacity (AR FY26 p.5, p.36), the ₹1,500 Cr ceiling implies about ₹2,100 per kWh
of pack revenue, an order of magnitude below observed pack pricing. Against FY26
battery revenue of ₹136.11 Cr, the claimed ceiling implies about 9% utilisation.
The two claims do not sit together.

**24. Three consecutive years of revenue decline are never stated as such.**
The Dec-2023 deck reports FY23 consolidated revenue of ₹6,700 mn (deck p.7).
Revenue then runs ₹608 Cr (FY24), ₹477 Cr (FY25), ₹451 Cr (FY26) per the two
MD&A snapshots (AR FY25 p.37; AR FY26 p.37). That is −9.7%, −21.5%, −5.4%. Each
report compares only to the year before. Neither names the multi-year trend. The
FY26 letter calls the year "a transitional year for KET" (AR FY26 p.4).

**25. Certification and share claims from the deck were never repeated.**
The deck headlines "Battrixx was the first EV battery-pack manufacturer to be
accredited with ARAI certification under AIS 156 Amendment III Phase 2 ...
designed in-house strategically with Hero Electric's R&D team" and an
"IATF approved manufacturing facility" (deck p.16, p.22), and "Captured 18%
market share in the lithium-ion batteries in its segment (FY23)", up from ~10% in
FY22 (deck p.12, p.21). None of these appears in either annual report. Hero
Electric, the named co-development partner, entered insolvency in Dec-2024 and
became the company's largest impaired receivable.

**26. The Hero Electric receivable disclosure is stale and sits outside both
risk sections.**
₹3,039 lakh outstanding from Hero Electric Vehicle Pvt Ltd; NCLT admitted a CIRP
application on 20-Dec-2024 (AR FY26 p.87-88; AR FY25 trade receivables note). The
FY26 report still opens the note with "As at March 31, 2025", a full year stale
inside the FY26 annual report, with no refreshed balance or case status. Neither
MD&A Risks and Challenges section mentions it in either year.

### D. Peer evidence bearing on the main company's claims

**27. Peer market sizing does not support a ~40% share.**
Rajoo's Executive Director sizes the domestic industry: "the industry would be in
the clear region of 1500 crores putting all the extrusion and thermoforming in
products together" (RAJOOENG Q4 FY24, 18-Apr-2024, PDF p.11). Rajoo's MD sizes
its own addressable line market at "around Rs. 2,000 crores" (RAJOOENG Q2 FY25,
22-Oct-2024, PDF p.6). Rajoo also claims, for itself, "80% of market shares" in
horizontal sheet extrusion and thermoforming and "nearly 60% of the market share"
in blown film domestically (RAJOOENG Q4 FY24, PDF p.7), later "55% to 60% market
share in the domestic market" for blown films and "33% market share in India" on
PVC/CPVC installed capacity (RAJOOENG Q2 FY25, PDF p.11-12). KABRAEXTRU's FY26
extrusion segment revenue is ₹314.89 Cr. Against a ₹1,500-2,000 Cr domestic
market that is 16% to 21%, not ~40%. The peer evidence is quantified and testable,
not merely absent.

**28. Peer working-capital discipline is the opposite of the main company's.**
Rajoo's CFO: "we normally receive 35% to 40% advance whenever we finalize any
order for exports or domestic" (RAJOOENG Q2 FY24, 6-Nov-2023, PDF p.10). Rajoo's
MD: "the payment comes before the delivery. So in 95% cases there are always 100%
payment before we dispatch" (same call, PDF p.12). Rajoo's receivable days were
22 in H1 FY24 (same call, PDF p.11). KABRAEXTRU carries 48.9% of gross receivables
more than one year overdue (item 5 above). Same industry, same product cycle,
same order-based manufacturing model, opposite cash discipline.

**29. A battery peer states the exact economics KABRAEXTRU's segment is
reporting, and says it deliberately avoided them.**
HBL's chairman: "I knew six years ago that no one outside China can make a profit
from the production of lithium ion cells ... We chose a niche for defense"
(HBLENGINE AGM, 25-Sep-2025, PDF p.4), and "when everybody jumps on lithium and
everybody can import cells, there is no margin in it. So we are not participating"
(PDF p.17), citing Reliance, Exide, Amara Raja and Northvolt as cautionary cases
(PDF p.4). On its own chosen niche: "we would have invested perhaps 200 crores or
less. And we will make a profit from year one" (PDF p.4). KABRAEXTRU has put
roughly ₹250 Cr into Geon (AR FY26 p.36) for a division that lost ₹43.35 Cr in
FY26. The investment scale is comparable. The outcome is not.

**30. The nearest listed peer grew through the window the company calls an
industry problem.**
Rajoo FY24 revenue ₹197.35 Cr, up 23.51% year on year, EBITDA margin 13.52%, PAT
margin 10.65% (RAJOOENG Q4 FY24, PDF p.5); H1 FY25 revenue ₹107.68 Cr, up 27.07%
(RAJOOENG Q2 FY25, PDF p.4). KABRAEXTRU's revenue fell in FY24, FY25 and FY26.
Rajoo also states the domestic market is "extremely price sensitive" with net
margin of "4% to 5%" domestic against exports "nearly 30% to 35% more"
(RAJOOENG Q4 FY23, 16-May-2023, PDF p.20), and generates ₹200-250 Cr of revenue
from an asset block of ₹35 Cr (same call, PDF p.19).

### Sub-threshold observations (recorded, not scored)

- The Extron Mecanor JV, Kabra Mecanor Belling Technik, reports NIL turnover in
  both FY25 and FY26, with PAT moving from ₹1.74 lakh to negative ₹0.891 lakh
  (AR FY25 p.25; AR FY26 p.23).
- FY25 FADA EV figures were restated between the two reports from the same
  source: total 19,64,975 (AR FY25 p.36) versus 19,67,397 (AR FY26 p.35), with
  each of the four sub-categories changed.
- CSR arithmetic: AR FY25 records ₹6.91 lakh available for set-off (p.29); AR
  FY26 sets off ₹4 lakh (p.26). The FY26 preceding-three-years table shows
  ₹4.33 lakh and ₹6.06 lakh in its rows and "Nil" in its Total row (p.27).

---

## PART 2: COMPARISON AGAINST THE PIPELINE ANALYSES

### 2A. My items versus B05 and B06

| # | Independent item | Verdict | Where the pipeline stands |
|---|---|---|---|
| 1 | FY26 letter EBITDA ₹10 Cr vs MD&A ₹13.05 Cr; loss omitted from letter | PARTIALLY CAUGHT | B05 4D and 2C flag the EBITDA inconsistency at MEDIUM. It does not note that the letter drops PAT entirely after giving it in FY25, nor that the two figures differ by 30% on the headline metric in a loss year. Severity is under-rated. |
| 2 | FY25 three-way PAT contradiction, two figures on one page | MISSED | B05 found the FY26 EBITDA inconsistency and stopped there. The FY25 report has the same defect, one year earlier, on the same metric class. |
| 3 | Silent ₹421.14 lakh restatement of FY25 comparatives | MISSED | Not mentioned in B05 or B06. |
| 4 | Unexplained ₹1,668.41 lakh "Other" in other income | MISSED | Not mentioned. This item determines the size of the reported FY26 loss. |
| 5 | 48.9% of receivables more than one year overdue; ₹14.80 Cr over three years at 23.5% cover | MISSED | B05 quotes the MD&A "Debtors Turnover 5.20%" nowhere and does not open the ageing table. |
| 6 | "Asset-light" claim vs ₹364 Cr battery segment assets | MISSED | B05 uses Note 38 for revenue and result but not for segment assets. |
| 7 | Interest Coverage +39.20% unreconcilable; two ratios missing mandatory reasons | MISSED | Not mentioned. |
| 8 | Inventory-turnover reason factually wrong | MISSED | Not mentioned. |
| 9 | Downgrade of 13-May-2026 vs "no material changes" of 28-May-2026; same silence in FY25 | PARTIALLY CAUGHT | B05 flags the FY26 narrative silence at HIGH, correctly and with the right anchor. It does not catch the direct contradiction with Director's Report item 12, and it does not catch that the FY25 downgrade was equally undiscussed. That second leg makes this a repeated omission across two reporting periods. |
| 10 | Varos subsidiary collapse; BMS capability claim dropped | MISSED | B05's dropped-claim list covers the 40% share, the 18% share, and ARAI/IATF. It does not cover Varos, which carries the BMS claim. |
| 11 | "Six decades / 15,000 installations" shrunk to "four decades", vs "60-year journey" in the same report | MISSED | Not mentioned. |
| 12 | Penta JV removed from the strengths table; 50:50 vs 49.94% | MISSED | Not mentioned. |
| 13 | FY25 PAT flattered by ₹848.98 lakh exceptional gain, unmentioned in the letter | MISSED | Not mentioned. B05 measures FY26 against the flattered FY25 base without noting it. |
| 14 | FY26 IEPF secretarial audit exception | MISSED | Not mentioned. It cuts both ways and belongs in the record. |
| 15 | Bagra independence round-trip in 16 days; duplicate board rows | MISSED | Not mentioned. |
| 16 | Customer concentration absent from both risk sections | PARTIALLY CAUGHT | B05 3D reports the concentration and 2D reports the HEVPL risk-section omission. It does not join them into the general finding that neither risk section names customer risk at all. |
| 17 | ~40% share dropped | CAUGHT | B05 1C, 2A row 2, 4D. Anchors verified correct. |
| 18 | R&D collapse vs "accelerated R&D" | CAUGHT | B05 1B, 1C, 2A row 5, 4D at HIGH. All four figures verified verbatim. |
| 19 | Battery loss widening vs "moving towards profitability" | CAUGHT | B05 2A row 4, 2D, 4D at HIGH. Note 38 figures verified exactly. |
| 20 | EV battery-pack TAM inconsistency, and the FY26 TAM being smaller than Geon's own share implies | PARTIALLY CAUGHT | B05 1C and 3B catch the ~100x swing. Neither B05 nor B06 tests the FY26 figure against Geon's own revenue, which is the load-bearing half. |
| 21 | Pipes market restated 2.7x downward | MISSED, with an incorrect pipeline sub-finding | B05 3B states the FY25 and FY26 pipe-market citations are "internally consistent". They are not. Same market, same year, ₹500 bn versus roughly ₹185 bn. |
| 22 | Extrusion CAGR 3.9% to 6.72%, source switched | CAUGHT | B05 1C, 3B, 4D. Verified. |
| 23 | ₹150 Cr and ₹1,500 Cr claims unanchored and mutually implausible against 7 GWh | PARTIALLY CAUGHT | B05 1A/1B flag both as low-specificity and unanchored. Neither report tests the two claims against each other or against the capacity claim. |
| 24 | Three consecutive years of revenue decline never stated | PARTIALLY CAUGHT | B05 2A row 3 covers the FY26 decline. Neither report states the multi-year trend, which the Dec-2023 deck makes computable. |
| 25 | Deck certification and 18% share claims never repeated | CAUGHT | B05 1C and dropped_triggers. Verified. |
| 26 | HEVPL stale and outside both risk sections | CAUGHT | B05 2D, 4D. Verified, with one wording defect noted in 2B below. |
| 27 | Peer market sizing defeats the ~40% claim | PARTIALLY CAUGHT | B06 Claim 3 quotes exactly the right passages, then rules UNVERIFIABLE. The arithmetic against KABRAEXTRU's own ₹314.89 Cr segment revenue is available and was not done. The verdict should read PARTIALLY CONTRADICTED. |
| 28 | Peer working-capital contrast | MISSED | No B06 claim covers receivables, advances or working capital. This is the single clearest peer-versus-company contrast in the corpus and it was never asked. |
| 29 | HBL profit-from-year-one vs Geon loss at comparable investment scale | PARTIALLY CAUGHT | B06 Claims 7 and 8 quote the HBL passages and rule UNVERIFIABLE on segment mismatch. The mismatch reasoning is fair for cell economics. The ₹200 Cr / profit-from-year-one versus ₹250 Cr / ₹43 Cr loss contrast needs no segment match and was left on the table. |
| 30 | Peer grew 23.5% while the company shrank | CAUGHT | B06 Claim 1 and Part 2A, with the staleness caveat correctly and repeatedly stated. |

**Tally: 30 independent red-flag-grade items. CAUGHT 7. PARTIALLY CAUGHT 9.
MISSED 14.**

Acceptance rate on the prompt's formula, caught divided by independent flags
found: 7 / 30 = **23%**. Including the three sub-threshold observations in the
denominator gives 7 / 33 = 21%, so the result is not sensitive to my scoping
choice. Excluding the five note-based items on a narrow reading of B05's scope
gives 7 / 18 = 39%. All three are below the 60% REWORK threshold.

### 2B. Pipeline flags I did not independently generate

Every red flag in B05 and B06 that I could test against the sources holds up. I
found no invented signal in either report. The failure mode here is
under-inclusion, not fabrication.

| Pipeline flag | Assessment | Note |
|---|---|---|
| B05: CRISIL two-step downgrade undiscussed (HIGH) | SUPPORTED | Ratings, dates and the generic reason verified at AR FY26 p.51. See my item 9 for the two additions. |
| B05: R&D cut vs "accelerated" claim (HIGH) | SUPPORTED | All four figures verified verbatim. The "accelerated its R&D" phrase sits in Annexure-4 at AR FY26 p.28, not p.29 as cited. Substance correct. |
| B05: 40% share dropped (MEDIUM-HIGH) | SUPPORTED | Verified in all three documents. |
| B05: battery segment negative leverage (HIGH) | SUPPORTED | Note 38 figures reproduce exactly. |
| B05: stale HEVPL disclosure (MEDIUM) | SUPPORTED, one wording defect | The core finding is right: the FY26 note still opens "As at March 31, 2025" and refreshes neither balance nor case status. B05 says the text is "identical, word-for-word, in both years' notes". It is not. The FY26 version adds a sentence on the warranty-provision reversal (AR FY26 p.88). MINOR overstatement. |
| B05: same-document EBITDA inconsistency (MEDIUM) | SUPPORTED, under-rated | Verified. I would raise it: 30% divergence on the headline metric in a loss year. |
| B05: senior-management churn (MEDIUM) | SUPPORTED | Every date verified. Subhabrata Ghosh, COO-Geon, appointed 01-Aug-2025 and ceased 16-Feb-2026 (AR FY26 p.44). Yogesh Deo, CEO-Extrusion, appointed 16-May-2025 (same table). Daulat Jain resigned as CFO 27-Apr-2026 (AR FY26 p.3, p.44). |
| B05: no order-book total disclosed (MEDIUM) | SUPPORTED | Neither report gives an order-book figure for either segment. |
| B05: market-size citations swing (LOW-MEDIUM) | SUPPORTED, under-rated | Should be MEDIUM-HIGH. See my items 20 and 21. |
| B05: Q1 FY27 screener loss; capex ₹61.81 Cr to ₹29.51 Cr; Note 41(b) ₹3,177.38 lakh | NOT ASSESSED | The screener CSV is outside my input set and I did not reach Note 41(b) in my read. Not disputed, not confirmed. |
| B06: Claim 1 CONTRADICTED, external-blame framing | SUPPORTED | Rajoo growth and order-book figures verified at every cited anchor. The 18-month staleness caveat is correctly and repeatedly attached. |
| B06: Claim 5 CONTRADICTED, export weakness | SUPPORTED | Export share rising to 73-74% of H1 FY25 verified (RAJOOENG Q2 FY25, PDF p.12). |
| B06: Claim 6 CONTRADICTED, capex cycle | SUPPORTED | All four capex citations verified. |
| B06: Claim 2 PARTIALLY VERIFIED, CAGR | SUPPORTED | Rajoo's 4.6%/4.2% and 8.33 bn to 11.6 bn citations verified. |
| B06: Claim 3 UNVERIFIABLE, 40% share | OVERSTATED toward caution | See my item 27. The peer supplies quantified market sizing that is testable. UNVERIFIABLE understates what the corpus supports. |
| B06: Claims 7-9 UNVERIFIABLE, HBL segment mismatch | SUPPORTED in part, OVERSTATED in part | Fair for cell-level economics and for the market-size question. Not fair for the investment-versus-outcome comparison in my item 29. |
| B06: "carbon extrusion" as a mistranscription of "Kabra Extrusion" | SUPPORTED as hedged | I concur that no Indian extrusion-machinery maker of that name exists and that Rajoo named exactly two domestic competitors (RAJOOENG Q4 FY24, PDF p.9). I would not raise the confidence above B06's. |
| B06: Part 5 export-mix hypothesis | SUPPORTED as a hypothesis | Correctly labelled as such, correctly made testable. |

**pipeline_flags_not_supported: none.**

---

## PART 3: PROMISE-DELIVERY SPOT CHECKS

Five of B05's five scored rows checked in both directions: did the earlier
document contain the promise, and does the later document show the stated
outcome.

| # | B05 row | Earlier document contains the promise? | Later document shows the outcome? | Direction |
|---|---|---|---|---|
| 1 | Row 1, Geon to enter E-LCV and E-4W in FY26 | YES. AR FY25 p.5: "Having entered the E-3 Wheelers market and Battery Swapping in FY25, Geon is actively pursuing new segments, including E-Low Commercial Vehicles, E-4 Wheelers etc. in the upcoming fiscal year." Repeated at p.38. | YES, with the nuance B05 itself discloses. AR FY26 p.36 lists "3-wheelers, 4-wheelers, and high-voltage applications" as existing diversification but describes no FY26 entry. The Geon narrative substitutes RESS, inverter D2C and e-bus packs (p.28). | CONFIRMED |
| 2 | Row 2, ~40% share maintained | YES, verbatim. AR FY25 p.37: "KET enjoys market leadership status in the extrusion market with ~40% market share in its product category as on FY25." | YES. No "40%" anywhere in AR FY26; Key Strength 1 reworded (p.36). Segment revenue −13.2% and segment result −27.6% verified from Note 38 (p.105). | CONFIRMED. Note: this is a positioning claim, not a forward promise. Scoring it as a missed promise is defensible but mildly inflates the missed count. |
| 3 | Row 3, "well-positioned to capitalize on anticipated growth" | YES. AR FY25 p.38: "the company is well-positioned to capitalize on anticipated growth in the pipe industry." | YES, every figure verbatim. AR FY26 p.37: revenue 477 to 451 (−5.45%), EBITDA 52 to 13.05 (−74.88%), PAT 34 to (2.44) (−107.21%). Nil dividend at AR FY26 p.17, cited by B05 as p.18. One-page anchor slip, no effect on the finding. | CONFIRMED |
| 4 | Row 4, Geon to become a key player in BESS | YES. AR FY25 p.38: "Geon aspires to be a key player in the BESS arena in the coming years." | YES, both halves. Product delivery is real and verified at AR FY26 p.28 (RESS with solar-integrated hybrid inverter, utility-scale BESS capability, HV liquid-cooled e-bus packs). Segment loss widening verified at Note 38 p.105. | CONFIRMED. B05's "Partial" is the right call, not a downgrade in disguise. |
| 5 | Row 5, continued R&D investment | YES. AR FY25 p.30 "₹1116.62 Lakhs" and p.31 "₹866.78 Lakhs", verbatim. | YES. AR FY26 p.28 "Rs. 367 Lakhs" and p.29 "Rs. 185.18 Lakhs", verbatim. The "accelerated its R&D" phrase is at p.28, cited by B05 as p.29. One-page anchor slip, no effect. | CONFIRMED |

**Spot checks: 5 checked, 5 confirmed, 0 wrong.** Two one-page anchor slips, both
MINOR, neither changing a finding. B05's promise-delivery table is directionally
sound. Its weakness is not accuracy. Its weakness is that it stops at five rows
drawn from the narrative sections and never opens the notes.

---

## PART 4: CREDIBILITY GRADE CONCURRENCE

B05 grades management credibility **D**, over the no-concall default of C, and
flags the interpretive question for the orchestrator in its analyst_note.

**I concur with D. I would not grade higher.**

My independent read finds more against management than B05 did, not less. Five
findings B05 did not reach each cut the same way: an unexplained ₹16.68 Cr line
inside other income that determines the size of the reported loss; a silent
₹4.21 Cr restatement of the prior year's published expense split; 48.9% of
receivables more than a year overdue while the MD&A reports a turnover
improvement; an "asset-light" claim contradicted by the company's own segment
note; and a mandatory ratio table that is both internally unreconcilable and
missing two required explanations. Add the rating-downgrade silence occurring in
both years rather than one, and a Director's Report asserting no material changes
fifteen days after a downgrade took effect.

Two things weigh the other way and should be recorded. The FY26 report states the
loss, the nil dividend and the extrusion demand causes plainly in the Director's
Report. The FY26 secretarial audit exception on the IEPF transfer is a genuine
volunteered negative that neither B05 nor B06 credits. Neither is enough to move
the grade. Both are mandatory-disclosure compliance rather than candour.

The degraded-mode ceiling question B05 raises is real and belongs to the
orchestrator. My input to it: the delivery evidence supports D on its own terms,
and the additional evidence in this report does not weaken that.

---

## PART 5: WHAT A REWORK SHOULD TARGET

The acceptance rate trips the REWORK threshold. The gap is specific and narrow,
so a rework should be surgical rather than a re-run.

1. **B05 never opened the financial-statement notes for red flags.** Five of the
   fourteen MISSED items sit in Notes 7, 9, 23, 38 and 47. The single most
   material one, the ₹1,668.41 lakh unlabelled other-income line, changes how the
   FY26 loss should be read. A rework should extend the no-concall procedure to
   read the notes for communication defects, not only for figures.
2. **B06 never asked a working-capital question.** The peer corpus contains a
   direct, quantified contrast on advances, receivable days and payment terms that
   no claim in B06 covers.
3. **B06 stopped one step short on two claims.** Claim 3 and Claims 7-8 quote the
   right peer passages and then decline to do the arithmetic those passages
   support. Both verdicts should be re-derived.
4. **One B05 sub-finding is wrong on the facts.** Section 3B calls the FY25 and
   FY26 plastic-pipe market citations "internally consistent". They differ by
   about 2.7x for the same market in the same year. That sentence should be
   corrected.
5. **Severity re-rating, not new work,** on three existing B05 flags: the
   same-document EBITDA inconsistency, the market-size swings, and the ~40% share
   drop now that peer arithmetic bears on it.

---

```yaml
stage: B12b
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-opus-4-8
status: complete
independent_flags_found: 30
caught: 7
partially_caught: 9
missed:
  - {severity: "CRITICAL", item: "Unexplained 'Other' line of Rs 1,668.41 lakh inside other income (FY25: Rs 22.91 lakh), unlabelled and unexplained, which determines the size of the reported FY26 standalone loss of Rs 423.21 lakh before tax; without it the loss is roughly 8x larger", anchor: "AR FY26 Note 23, p.95; loss at AR FY26 p.17"}
  - {severity: "MAJOR", item: "FY25 MD&A states three different PAT figures for FY25, two of them on the same page: table PAT 34 / margin 7.2%, prose 'PAT stood at Rs 32 crores. PAT margin stood at 6.8%', chairman's letter Rs 33.9 crores / 7.2%", anchor: "AR FY25 p.38 (table and prose, same page); AR FY25 p.4 (letter)"}
  - {severity: "MAJOR", item: "Silent restatement of FY25 comparatives: standalone employee benefits expense 5,907.53 -> 6,328.67 lakh and other expenses 7,473.91 -> 7,052.77 lakh, an exactly offsetting Rs 421.14 lakh reclassification in both standalone and consolidated columns, covered only by boilerplate 'regrouped wherever considered necessary'", anchor: "AR FY25 p.19 (Notes 26, 29); AR FY26 p.17; AR FY26 standalone Note 47"}
  - {severity: "MAJOR", item: "Receivable ageing deterioration: Rs 4,428.68 lakh of Rs 9,052.43 lakh gross receivables (48.9%) more than one year overdue at 31-Mar-2026, up from 41.8%; Rs 1,935.36 lakh over three years carried with only Rs 455.13 lakh provision (23.5% cover); MD&A reports only 'Debtors Turnover 5.20%' with no reason", anchor: "AR FY26 Note 9 ageing tables, p.88; MD&A ratio table p.37"}
  - {severity: "MAJOR", item: "'Technology-Agnostic and Asset-Light Approach in Energy Business' Key Strength contradicted by own segment note: Battery Division segment assets Rs 36,437.25 lakh, 50.1% of total segment assets, on segment revenue Rs 13,610.84 lakh (0.37x asset turn) and a Rs 4,334.64 lakh segment loss, with ~Rs 250 Cr stated as invested", anchor: "AR FY26 p.36 (claim); Note 38, p.105-106 (contradiction)"}
  - {severity: "MAJOR", item: "Key Financial Ratios table internally unreconcilable and incomplete: Interest Coverage Ratio reported as +39.20% in a year the same report shows EBIT falling Rs 45 Cr to Rs 7.16 Cr and finance cost rising 1,117.31 to 1,139.25 lakh; both Interest Coverage (+39.20%) and ROCE (-86.50%) exceed the 25% threshold and carry blank 'Reasons for Variation'", anchor: "AR FY26 p.37 (ratio and EBIT tables); AR FY26 p.17 (finance cost)"}
  - {severity: "MAJOR", item: "Varos Technology Pvt Ltd, the subsidiary carrying the battery-management-system capability claim, collapsed: turnover 372.99 -> 17.84 lakh (-95%), loss 221.24 -> 291.49 lakh, reserves negative 557.17 lakh against Rs 1.00 lakh capital (negative net worth); named as a Key Strength in AR FY25 and in the Dec-2023 deck, absent from all AR FY26 narrative", anchor: "AOC-1 at AR FY25 p.25 and AR FY26 p.23; claim at AR FY25 p.37 and deck p.17"}
  - {severity: "MAJOR", item: "FY25 profit flattered by a Rs 848.98 lakh exceptional gain on the Penta divestment (PBT before exceptional 3,343.28 lakh vs reported 4,192.26 lakh); the chairman's letter reports PAT Rs 33.9 Cr at 7.2% margin without mentioning that ~25% of pre-tax profit was a one-off, and FY26 is then measured against that base throughout", anchor: "AR FY25 p.19 (expense table); AR FY25 p.4 (letter)"}
  - {severity: "MAJOR", item: "Peer working-capital contrast never tested by B06: Rajoo takes 35-40% advance on order finalisation, '95% cases there are always 100% payment before we dispatch', receivable days 22 in H1 FY24; KABRAEXTRU carries 48.9% of receivables over one year overdue. No B06 claim covers receivables, advances or working capital", anchor: "RAJOOENG Q2 FY24, 6-Nov-2023, PDF p.10, p.11, p.12; AR FY26 Note 9, p.88"}
  - {severity: "MAJOR", item: "Indian plastic pipes market restated downward ~2.7x between the two ARs for the same market and same year (Rs ~500 bn by FY2025 per AR FY25 vs USD 2.10 bn, roughly Rs 185 bn, for 2025 per AR FY26), source switched to IMARC, no reconciliation; B05 Section 3B incorrectly calls these two citations 'internally consistent'", anchor: "AR FY25 p.4-5, p.35; AR FY26 p.33; B05 report Section 3B"}
  - {severity: "MINOR", item: "FY26 inventory-turnover explanation factually wrong: 'Due to increase in inventory and Lower sale' when Note 7 shows inventory fell from 29,014.77 to 28,538.08 lakh; sentence copied verbatim from the FY25 table where it was true", anchor: "AR FY26 p.37 (ratio table); AR FY26 Note 7, p.87; AR FY25 p.38"}
  - {severity: "MINOR", item: "Heritage and scale claims quietly shrunk and self-contradictory: 'over six decades of industry experience, a track record of more than 15,000 successful installations' (AR FY25) becomes 'a legacy of over four decades' with no installation count (AR FY26), while the FY26 chairman's letter in the same report says 'its 60-year journey'", anchor: "AR FY25 p.36; AR FY26 p.35; AR FY26 p.5"}
  - {severity: "MINOR", item: "Penta JV, listed as one of three technical-collaboration 'Pillars of Strength' in the Dec-2023 deck as a '50:50 JV with Penta SRL, Italy', removed from the AR FY25 collaboration table with no narrative comment (AOC-1 records the holding as 49.94%, not 50:50); AR FY26 drops the whole collaboration table including the 1983 Battenfeld-Cincinnati tie-up", anchor: "deck p.24; AR FY25 p.37, p.21, p.25; AR FY26 p.36"}
  - {severity: "MINOR", item: "FY26 secretarial audit exception not recorded by the pipeline: shares for FY2017-18 unclaimed dividend transferred to IEPF on 31-Oct-2025, 'beyond the timelines prescribed under Section 124'; a genuine volunteered negative that also evidences a compliance lapse", anchor: "AR FY26 MR-3, p.24; Director's Report item 23, p.21"}
  - {severity: "MINOR", item: "Governance optics: Mr Bajrang Lal Bagra completed his second five-year Independent Director term on 26-Aug-2025 and was appointed Non-Executive Non-Independent Director w.e.f. 11-Sep-2025, sixteen days later; the FY26 board composition table lists him twice, once under each category", anchor: "AR FY26 p.18, p.25, p.39-40"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 5, wrong: 0}
credibility_grade_concur: "concur with D; my independent read finds more against management than B05 did, not less, and the two mitigating items I found (plain disclosure of the loss and nil dividend, and the volunteered IEPF secretarial exception) are mandatory-disclosure compliance rather than candour"
findings:
  - {severity: "CRITICAL", location: "B05 report, Sections 2D and 4D (red flags); source AR FY26 Note 23, p.95", description: "MISSED: unexplained Rs 1,668.41 lakh 'Other' line in other income (FY25 Rs 22.91 lakh) that determines the size of the reported FY26 loss; neither B05 nor B06 opens the other-income note"}
  - {severity: "MAJOR", location: "B05 report, Section 2C/4D; source AR FY25 p.38 and p.4", description: "MISSED: FY25 AR states three different PAT figures for FY25, two on the same page; B05 caught only the analogous FY26 EBITDA inconsistency"}
  - {severity: "MAJOR", location: "B05 report, Section 2A/2D; source AR FY25 p.19 vs AR FY26 p.17, Note 47", description: "MISSED: silent, exactly offsetting Rs 421.14 lakh restatement of FY25 employee-benefit and other-expense comparatives, disclosed only by regrouping boilerplate"}
  - {severity: "MAJOR", location: "B05 report, Section 3D (customer and order book signals); source AR FY26 Note 9, p.88", description: "MISSED: 48.9% of gross receivables more than one year overdue, Rs 14.80 Cr over three years at 23.5% provision cover, against an MD&A that reports only a debtor-turnover improvement"}
  - {severity: "MAJOR", location: "B05 report, Section 2A row 4; source AR FY26 p.36 vs Note 38, p.105-106", description: "MISSED: 'Asset-Light' Key Strength contradicted by Battery Division segment assets of Rs 36,437.25 lakh, 50.1% of segment assets, at 0.37x asset turn"}
  - {severity: "MAJOR", location: "B05 report, Section 2C/4D; source AR FY26 p.37 and p.17", description: "MISSED: Interest Coverage Ratio disclosed as +39.20% is not reconcilable to the company's own EBIT and finance-cost figures; Interest Coverage and ROCE both exceed the 25% threshold with blank mandatory 'Reasons for Variation'"}
  - {severity: "MAJOR", location: "B05 report, dropped_triggers list; source AOC-1 at AR FY25 p.25 and AR FY26 p.23", description: "MISSED: Varos Technology, the subsidiary carrying the BMS capability claim, at negative net worth with turnover down 95%, and dropped entirely from AR FY26 narrative"}
  - {severity: "MAJOR", location: "B05 report, Section 2A row 3; source AR FY25 p.19 and p.4", description: "MISSED: FY25 base flattered by a Rs 848.98 lakh exceptional divestment gain not disclosed in the chairman's letter, and FY26 is measured against that base"}
  - {severity: "MAJOR", location: "B06 report, Part 1 claim set; source RAJOOENG Q2 FY24, PDF p.10-12", description: "MISSED: no B06 claim tests working capital, where the peer corpus supplies a direct quantified contrast (35-40% advances, payment before dispatch in 95% of cases, 22 receivable days) against the main company's overdue receivable profile"}
  - {severity: "MAJOR", location: "B05 report, Section 3B, second bullet", description: "INCORRECT SUB-FINDING: B05 states the FY25 and FY26 plastic-pipe market citations are 'internally consistent'; they differ by roughly 2.7x for the same market in the same year (Rs ~500 bn vs USD 2.10 bn, roughly Rs 185 bn)"}
  - {severity: "MAJOR", location: "B06 report, Claim 3 verdict; source RAJOOENG Q4 FY24 PDF p.7, p.11 and Q2 FY25 PDF p.6, p.11-12", description: "UNDER-CALLED: Claim 3 ruled UNVERIFIABLE although the peer supplies quantified domestic market sizing (Rs 1,500-2,000 Cr) that puts KABRAEXTRU's Rs 314.89 Cr extrusion revenue at 16-21% share, not ~40%; verdict should be PARTIALLY CONTRADICTED"}
  - {severity: "MAJOR", location: "B05 report, Section 1C and 3B; source AR FY26 p.34 vs Note 38, p.105", description: "PARTIALLY CAUGHT: the ~100x EV battery-pack TAM swing was found, but not that the FY26 figure cited (USD 53.76 mn for all India in 2026) is smaller than Geon's own revenue implies, at roughly 28% of that market"}
  - {severity: "MAJOR", location: "B05 report, Section 2D and 4D; source AR FY26 p.51 and p.20, AR FY25 p.49", description: "PARTIALLY CAUGHT: the FY26 downgrade silence was found; missed that the 13-May-2026 downgrade contradicts the 28-May-2026 Director's Report item 12 'no material changes' statement, and that the FY25 downgrade was equally undiscussed, making it a repeated omission across two reporting periods"}
  - {severity: "MINOR", location: "B05 report, Section 4D; source AR FY26 p.37 and Note 7, p.87", description: "MISSED: mandatory inventory-turnover explanation is factually wrong, copied verbatim from the prior year, in a year when inventory fell"}
  - {severity: "MINOR", location: "B05 report, dropped_triggers; source AR FY25 p.36 vs AR FY26 p.35 and p.5", description: "MISSED: 'six decades / 15,000 installations' walked back to 'four decades', against a '60-year journey' claim in the same FY26 report"}
  - {severity: "MINOR", location: "B05 report, dropped_triggers; source deck p.24, AR FY25 p.37", description: "MISSED: Penta JV removed from the technical-collaboration pillar table without narrative comment; deck says 50:50, AOC-1 says 49.94%"}
  - {severity: "MINOR", location: "B05 report, Sections 2B and 2D; source AR FY26 p.24 and p.21", description: "MISSED: FY26 secretarial audit exception on the late IEPF transfer, both a compliance lapse and the one clear volunteered negative in either report"}
  - {severity: "MINOR", location: "B05 report, Section 2D; source AR FY26 p.18, p.25, p.39-40", description: "MISSED: independent director re-badged as Non-Executive Non-Independent sixteen days after his second term ended; duplicate rows in the board composition table"}
  - {severity: "MINOR", location: "B05 report, Section 2C transparency row; source AR FY26 p.4", description: "PARTIALLY CAUGHT: the EBITDA inconsistency was found but under-rated at MEDIUM; the FY26 chairman's letter also drops PAT entirely after giving it in FY25, and never uses the word loss"}
  - {severity: "MINOR", location: "B05 report, Sections 2D and 3D; source AR FY26 Note 38, p.106", description: "PARTIALLY CAUGHT: concentration reported and the HEVPL risk-section omission reported, but not joined into the finding that neither year's Risks and Challenges section names customer or customer-credit risk at all"}
  - {severity: "MINOR", location: "B05 report, Sections 1A and 1B; source AR FY26 p.37, p.36, p.5", description: "PARTIALLY CAUGHT: the Rs 150 Cr order and Rs 1,500+ Cr ceiling flagged as unanchored, but never tested against each other or against the claimed ~7 GWh capacity, which they do not fit"}
  - {severity: "MINOR", location: "B06 report, Claims 7 and 8; source HBLENGINE AGM PDF p.4, p.17; AR FY26 p.36 and Note 38 p.105", description: "PARTIALLY CAUGHT: segment-mismatch reasoning is fair for cell economics, but the peer's 'perhaps 200 crores or less ... profit from year one' against Geon's ~Rs 250 Cr and Rs 43.35 Cr loss needs no segment match and was left undrawn"}
  - {severity: "MINOR", location: "B05 report, Section 2A row 3; source deck p.7, AR FY25 p.37, AR FY26 p.37", description: "PARTIALLY CAUGHT: the FY26 decline is covered, but neither report states that revenue has now fallen three years running (-9.7%, -21.5%, -5.4% from the deck's FY23 base)"}
  - {severity: "MINOR", location: "B05 report, Section 2D and 4D, HEVPL row", description: "OVERSTATED WORDING: B05 says the HEVPL note is 'identical, word-for-word' across both ARs; the FY26 version adds a warranty-reversal sentence. The core finding (still dated 'As at March 31, 2025', balance and case status not refreshed) is SUPPORTED"}
  - {severity: "MINOR", location: "B05 report, Section 2A row 5 and row 3 anchors", description: "ANCHOR IMPRECISION: the 'accelerated its R&D' phrase is at AR FY26 p.28, cited as p.29; the nil-dividend statement is at AR FY26 p.17, cited as p.18. Neither slip changes a finding"}
  - {severity: "MINOR", location: "Sub-threshold observations, this report Part 1 closing section", description: "RECORDED, NOT SCORED: dormant Kabra Mecanor JV (nil turnover two years); FY25 FADA EV figures restated between the two ARs from the same source; CSR set-off and preceding-year table arithmetic inconsistencies"}
critical_count: 1
major_count: 12
minor_count: 13
acceptance_rate: 23
```
