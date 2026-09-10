# STAGE 12B: VERIFIER B — INDEPENDENT RED-FLAG AUDIT
## India Nippon Electricals Ltd (INDNIPPON) | Run date 2026-09-10 | NO-CONCALL MODE

Model: claude-opus-4-8. Fresh context. Sources read directly, upstream reports read after.

---

## 0. METHOD AND ITS LIMITS

This company holds no earnings calls. There are no subject-company transcripts. There is no
management-under-pressure behaviour anywhere in this corpus.

Therefore the following are **NOT ASSESSABLE** and I do not manufacture them from prepared text:
dodged questions, deflection, answer quality, tone under cross-examination, unusual analyst
insistence, contradictions between what management told different analysts.

What IS assessable, and what this audit judges on:
- **Annual report against investor deck.**
- **Deck against deck**, quarter to quarter.
- **This year's language against last year's.**
- **Claim against filed number**, meaning deck and MD&A assertions against the audited
  financial statements, the notes, and the Regulation 33 results filing.

The last of these produced most of what follows and is where the upstream work is thinnest.

**Sources read in full or in targeted depth:** AR2026 (chairman/MD letter, MD&A, BRSR Section A,
Directors' Report summary, standalone Notes 28e/29/30-37/42/43/44/45/47/51, consolidated Note 51);
AR2025 (financial snapshot, ratios, Notes on major customers, related parties, R&D, fair value);
Q1FY26, Q2FY26, Q4FY26, Q1FY27 investor decks in full; Q1FY27 Regulation 33 results filing with
the Deloitte limited review report; the four Reg-30 announcements; twelve peer transcripts by
targeted search on the load-bearing quotes.

**Coverage caveat, stated up front.** I audit B05 and B06 only. Several items I list as MISSED may
have been caught by B01, B02, B03 or B07, which I cannot see. B05 itself cites B02/B03 findings
(CFO/PAT 0.36x, receivables ageing, Lucas TVS at 32.2% of net worth, capex Rs 42.15 Cr). My
acceptance rate is therefore a measure of B05+B06 coverage, not of whole-pipeline coverage, and
should not be read as the latter.

---

## PART 1: INDEPENDENT RED-FLAG LIST

Twenty-four red-flag-grade items, formed from the sources before reading B05/B06. Ordered by
severity. Every number carries file and anchor. "Extracted line" refers to the page-marked text
file; the nearest confirmed `===== PAGE N =====` marker is given as the PDF page.

Document-defect findings of lesser weight are listed separately in Part 4 and are excluded from
the acceptance-rate denominator, so the rate is not inflated by trivia.

---

### V-01 [CRITICAL] Deck ROCE of 34.97% is 2.06x the audited ROCE of 17%, on an undisclosed definition

**Deck claim.** Q4FY26 deck (2026-06-01) p.19 and Q1FY27 deck (2026-08-21) p.18, chart "ROCE & ROE (%)":
ROCE FY23 25.10%, FY24 21.66%, FY25 26.37%, FY26 **34.97%**. No definition is given anywhere in any
of the five decks.

**Filed number.** AR2026 Note 51 Analytical Ratios, consolidated (extracted lines 19752-19781,
PDF p.297) and standalone (extracted lines 15507-15518, PDF p.235):

| Ratio | FY26 | FY25 |
|---|---|---|
| Return on capital employed** | **17%** | 14% |
| Return on equity** | 15% | 12% |
| Net profit ratio** | 10.40% | 9.74% |
| Return on investment* | 13% | 14% |

Definition, AR2026 extracted lines 19773-19776: "Return On Capital Employed | PBIT | (Tangible net
worth = Total assets - Intangible assets - Total liabilities) (though investments are not tangible,
they are generally included while computing tangible net worth)".
Footnote, extracted line 19781: "**Includes exceptional item".

**The gap.** Audited 17%. Deck 34.97%. Ex-exceptional the audited figure falls further: PBIT
14,653 lakhs (PBT 14,601 + finance cost 52) less exceptional 1,521 = 13,132 lakhs over tangible net
worth ~82,063 lakhs = **16.0%**.

**Reverse-engineering the deck number [INFERENCE, labelled].** EBIT excluding other income =
audited EBITDA 11,864 lakhs less depreciation 1,792 = 10,072 lakhs. Net worth 82,133 lakhs less
total investments 53,153 lakhs (AR2026 Note 47, extracted line 15220) = 28,980 lakhs.
10,072 / 28,980 = 34.75%, against the deck's 34.97%. The deck's capital-employed base therefore
appears to strip out the entire Rs 531.5 Cr investment book, which is 65% of equity, while the
audited definition explicitly includes it.

**Why this is CRITICAL.** ROCE is the Section 1B Pillar 1 input and the QUALITY LADDER rung is
defined by ROCE durability. The deck's 34.97% sits at R5 (BRAND/SCARCITY OWNER, ROCE >30%,
~24x neighbourhood plus strategic premium). The audited 17% sits at R2 (COST-ADVANTAGED CONVERTER,
~15-17x neighbourhood). That is a three-rung difference produced entirely by an undisclosed,
non-standard definition in a promotional deck. Both numbers, and the definition of each, must be
in front of Stage 11 before any destination PE is set.

**Anchors:** presentation__Investor_Presentation_2026-06-01_Q4FY26 p.19; presentation__Investor_
Presentation_2026-08-21_Q1FY27 p.18; annual-report__Annual_Report_2026 extracted lines 15507-15518
(PDF p.235) and 19752-19781 (PDF p.297).

---

### V-02 [CRITICAL] The FY26 margin-expansion claim does not survive the filed statements; deck EBITDA includes foreign-exchange gains

**Deck claim.** Every deck reports FY26 EBITDA margin 11.44% against FY25 11.27%, a 17 bps
expansion (Q4FY26 deck p.16 "EBITDA Margins (%) 11.44% / 11.27% / 17 Bps"; Q1FY27 deck p.16).
The MD&A builds the transition thesis on it: "Margin expansion followed this shift in mix.
Electronics-led products inherently command better realizations compared to commoditized
components" (AR2026 extracted lines 8091-8094, PDF p.124).

**Filed number, FY26.** Regulation 33 results filing 2026-08-07 p.4, "Year Ended 31-Mar-26"
(audited) column, Rs Lakhs: Revenue from operations 1,06,848; Total expenses 96,828; within which
finance costs 52 and depreciation and amortisation 1,792.

  EBITDA = 1,06,848 - (96,828 - 52 - 1,792) = 1,06,848 - 94,984 = **11,864 lakhs**
  Margin = 11,864 / 1,06,848 = **11.10%**

Deck says Rs 1,222 Mn = 12,220 lakhs. Gap = **356 lakhs**, which is the foreign-exchange gain of
**372 lakhs** that AR2026 Note 29 classifies inside Other Income ("Net gain on foreign currency
transactions 372", extracted line 14623, PDF p.218). The deck's own line "Operating Expenses 9,463"
is likewise ~350 lakhs below the audited expense base.

**Filed number, FY25.** AR2026 Directors' Report financial summary (extracted lines 4209-4214),
standalone column: "Profit before depreciation, exceptional items and taxes 12,324" for FY25.
Removing Other Income 2,979 (Note 29 FY25 column, extracted line 14629) and adding back finance
cost 39 (Note 35 FY25, extracted line 14699) gives EBITDA 9,384 lakhs on revenue 84,483 lakhs =
**11.11%**. The identical method reproduces FY26 exactly (14,872 - 3,060 + 52 = 11,864), so the
method is validated against the results filing.

**Result.**

| Basis | FY25 | FY26 | Change |
|---|---|---|---|
| Deck (Q4FY26 p.16) | 11.27% | 11.44% | **+17 bps** |
| Audited statements | 11.11% | 11.10% | **-1 bp** |

The FX gain rose from 102 lakhs (FY25, Note 29) to 372 lakhs (FY26), a 270 lakh swing worth 25 bps
on FY26 revenue. On the filed numbers the FY26 EBITDA margin was flat to marginally down, not up.

**Why this is CRITICAL.** The mix-shift-drives-margin story is the transition thesis. Its only
quantitative support in the entire corpus is this 17 bps move, and the 17 bps is a non-GAAP
construction the company never defines or reconciles. A margin bridge built on the deck series
would price a re-rating that the audited statements do not show.

**Anchors:** results__Q1FY27_Board_Outcome_and_Results_2026-08-07 p.4; annual-report__Annual_
Report_2026 extracted lines 4209-4214, 14613-14629 (PDF p.218), 14691-14699 (PDF p.220);
presentation__Investor_Presentation_2026-06-01_Q4FY26 p.16.

---

### V-03 [MAJOR] MD&A "Net Profit Margin 13.7%" contradicts the same report's audited "Net profit ratio 10.40%"

AR2026 MD&A, Details of Key Standalone Financial Ratios (extracted lines 8123-8131, PDF p.125):
Operating Profit Margin 9.4% (FY25 8.7%); **Net Profit Margin 13.7%** (FY25 12.2%); Return on Net
Worth 14.5% (FY25 12.3%).

AR2026 Note 51 (extracted line 19760, PDF p.297): **Net profit ratio 10.40%** (FY25 9.74%), defined
at extracted line 19772 as "PAT / Net sales".

The same table lists PAT of 11,126 lakhs and Net Sales of 1,05,292 lakhs (extracted lines 8118-8122),
which give 10.57%, not 13.7%.

**What 13.7% actually is [INFERENCE].** PBT 14,601 / Gross Sales 1,06,440 = 13.72%. FY25 test:
PBT 10,268 / 84,055 = 12.21%, against the claimed 12.2%. So the MD&A's "Net Profit Margin" is a
**pre-tax** margin that also **includes the Rs 1,521 lakh exceptional land item**. It is labelled
Net Profit Margin in a Schedule V key-ratio disclosure and overstates the real net margin by
330 bps.

The same table's "Operating Profit Margin 9.4%" is computed post-depreciation (10,072 / 1,06,440 =
9.46%) while listing Depreciation as a separate deduction line immediately beneath it, which reads
as though Operating Profit were pre-depreciation. Two ratios, two undeclared bases, one table.

**Anchor:** annual-report__Annual_Report_2026 extracted lines 8113-8131 (PDF p.125) against
extracted lines 19752-19781 (PDF p.297).

---

### V-04 [MAJOR] CFO cessation filed 07-Aug-2026 is absent from the 21-Aug-2026 investor deck, and the filing contradicts itself on what happened

The Regulation 30/33 board outcome of 2026-08-07 records, at item 2, that Mr Elango Srinivasan
ceases to be CFO from close of business on 30-Sep-2026 and becomes "Special Projects Head - Finance",
with Mr Saravana Kumar M appointed CFO from 01-Oct-2026 (results__Q1FY27_Board_Outcome_and_
Results_2026-08-07 pp.1-2, and Annexures C and D at pp.6-7).

Two findings.

**(a) Internal contradiction inside the filing.** Page 1, line 43: "A copy of the **resignation
letter** is enclosed as Annexure B". Annexure C, page 6, records the "Reason for change" as
"**Change in designation** of Senior Management Personnel". A resignation letter and a designation
change are not the same event. The Reg-30 disclosure records the softer of the two.

**(b) Omission from investor communication.** The Q1FY27 investor presentation was filed fourteen
days later, on 2026-08-21. I read all 21 pages. It does not mention the CFO transition anywhere.
The Operational Highlights page (p.14) has room for "Ranked #69 among India's Top 100 Great Places
to Work" and "Launched Total Productive Maintenance (TPM)" but not for the departure of the
signing CFO.

**Timing.** The same Elango Srinivasan signed the FY26 financial statements as Chief Financial
Officer on 28-May-2026 (AR2026 extracted lines 15538-15543 and 19801-19806). He exits the role four
months later.

This is a governance and communication red flag that no upstream stage carries.

**Anchors:** results__Q1FY27_Board_Outcome_and_Results_2026-08-07 pp.1-2, 6-7; presentation__
Investor_Presentation_2026-08-21_Q1FY27 (whole deck, absence); annual-report__Annual_Report_2026
extracted lines 15538-15543.

---

### V-05 [MAJOR] Three different employee counts across company documents, and the deck number is frozen

| Source | Figure |
|---|---|
| All five decks, "SNAPSHOT" p.3 | **1,605+ Employees** |
| AR2026 MD&A, Human Resources (extracted line 8286, PDF p.127) | "As of 31st March, 2026, the Company's employee base stood at **2,601**" |
| AR2026 HR category table (extracted lines 1894-1900, PDF p.35) | Supervisors/Managers 397 + Union 201 + Associates 1,600 + Contract 403 = **2,601** |
| AR2026 BRSR Section A (extracted lines 8465-8471) | Total employees 397 + Total workers 2,414 = **2,811** |

Three numbers for one workforce at one date, two of them inside the same annual report, 210 apart.
The deck's "1,605+" understates the MD&A figure by 38% and the BRSR figure by 43%, and appears to
count only the "Associates 1,600" line.

The deck figure is also **frozen**: "1,605+" appears identically in the Q1FY26 deck (2025-08-20),
Q2FY26 (2025-11-25), Q4FY26 (2026-06-01) and Q1FY27 (2026-08-21), across a year in which revenue
grew 26.5% and the company opened a third-phase production line at Rewari. The same snapshot page
updates market cap and the years-of-experience count each quarter; headcount alone does not move.

**Anchors:** presentation__Investor_Presentation_2025-08-20_Q1FY26 p.3; ..._2025-11-25_Q2FY26 p.3;
..._2026-06-01_Q4FY26 p.3; ..._2026-08-21_Q1FY27 p.3; annual-report__Annual_Report_2026 extracted
lines 1894-1900, 8284-8286, 8461-8471.

---

### V-06 [MAJOR] R&D spend was flat and R&D capex fell 42% in a year revenue grew 26%, against a technology narrative in every document

AR2026 Note 43, Research and Development Expenses (extracted lines 15137-15151, PDF p.228):

| Rs Lakhs | FY26 | FY25 | Change |
|---|---|---|---|
| Capital expenditure | 341 | 585 | **-41.7%** |
| Revenue expenditure (salaries, power, travel, misc) | 2,536 | 2,311 | +9.7% |
| **Total** | **2,877** | **2,896** | **-0.7%** |

Net sales grew from 83,194 to 1,05,292 lakhs (+26.6%). R&D intensity therefore fell from **3.48%**
to **2.73%** of net sales, a 75 bps decline. AR2025 shows R&D capex of 102 lakhs in FY24, so the
FY25 585 was the outlier year and FY26 gave 42% of it back.

Set against this, every deck carries "Thrust On Technology" (p.10, Key Strengths), a "Growing EV
Product Portfolio" growth strategy (p.11), and a "state-of-art Research Center" in the snapshot;
the MD&A describes a Tech Center "Staffed by over 100 engineers" managing development "from concept
through commercialization" (AR2026 extracted lines 8065-8076, PDF p.124). No deck discloses R&D
spend at all.

A company claiming a climb from component supplier to "integrated, system-level solutions provider"
(AR2026 extracted lines 8087-8089) held R&D flat in absolute rupees while revenue grew a quarter.
That is a claim contradicted by a filed number, and it is the cleanest available test of whether
the transition is being funded.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 15137-15151 (PDF p.228), 8065-8094
(PDF p.124); annual-report__Annual_Report_2025 extracted lines 59408-59414; all five decks pp.10-11.

---

### V-07 [MAJOR] Receivable from the 70.32% parent stretched from ~80 to ~108 days while the deck sells "aftermarket momentum"

AR2026 Note 42, related parties (extracted lines 15060-15061 and 15113, PDF pp.226-227):

| Lucas Indian Service Limited (holding company, 70.32%) | FY26 | FY25 | Change |
|---|---|---|---|
| Sale of products (Rs Lakhs) | 6,106 | 4,998 | +22.2% |
| Trade receivable outstanding (Rs Lakhs) | 1,805 | 1,089 | **+65.7%** |
| Implied days (receivable / sales x 365) | **108** | **80** | **+28 days** |

Receivables from the controlling shareholder grew three times faster than sales to it. No deck and
no narrative section mentions this.

**Why it matters to the thesis.** Lucas Indian Service is the group's aftermarket distribution arm.
The AR credits the aftermarket with 20% growth (extracted line 8054) and every deck gives the
aftermarket a product-portfolio column and a growth-strategy box. Sales to the parent, at
Rs 61.06 Cr, are 5.8% of net sales and are the only quantifiable proxy for aftermarket revenue in
the entire corpus. The channel that carries the aftermarket story is the controlling shareholder,
and its payment terms stretched by a month in FY26.

This is the related-party leg of the receivables question B02/B06 raise generally, and it is
specific, anchored, and absent from both.

**Anchor:** annual-report__Annual_Report_2026 extracted lines 15055-15123 (PDF pp.226-227).

---

### V-08 [MAJOR] Contract and apprentice labour carries 79% of the workforce and Rs 30.6 Cr routed through a related party, while labour-code risk is named in one clause and never quantified

Three filed facts that are never put together in any company document.

1. **BRSR** (AR2026 extracted lines 8468-8471): Permanent workers 201; **"Other than Permanent (G)
   2213"**; total workers 2,414. Non-permanent workers are **91.7% of workers** and 79% of the
   2,811 total workforce.
2. **Note 42** (extracted line 15083, PDF p.227): "Stipend to apprentices" paid to **TVS Educational
   Society, a related party**: Rs **3,059** lakhs FY26, Rs 2,414 lakhs FY25 (+26.7%), Rs 1,338
   lakhs FY24 per AR2025 (extracted line 59364). The line has grown 2.3x in two years.
3. **Employee benefits expense** (Note 34, extracted line 14690, PDF p.219): Rs 11,887 lakhs.

Total labour cost is therefore ~14,946 lakhs, of which **20.5% sits outside the employee-benefits
line and is paid to a related party**. Reported employee cost per head on the MD&A's 2,601 count is
Rs 4.6 lakhs, which is only coherent because most of the workforce is not on that line.

Against this, the MD&A risk table names the exposure in a single subordinate clause and never
returns to it: "and anticipated impacts arising from labor code reforms" (extracted line 8149,
PDF p.125). No quantification, no sensitivity, no mitigation specific to it.

**Peer contrast, which sharpens it.** All three peers quantified labour-code and minimum-wage cost
as a discrete item in the same period: Varroc a ~Rs 22.5 Mn exceptional (VARROC Feb 2026 p.4),
Minda ~Rs 4 Cr exceptional (MINDACORP Feb 2026, extracted line 218: "we had to account for INR 4
crores of exceptional items"), Pricol ~Rs 21 Cr annualised minimum-wage increase (PRICOLLTD Aug
2026 p.6). B06 lists this as a risk peers raise that INEL does not. It does not connect it to
INEL's own filed labour structure, which is what makes the exposure large.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 8461-8471, 14681-14690 (PDF p.219),
15079-15083 (PDF p.227), 8147-8157 (PDF p.125); annual-report__Annual_Report_2025 extracted line
59364; peer-concalls__MINDACORP-Concall_Feb_2026 extracted line 218.

---

### V-09 [MAJOR] Q1FY27 deck labels every table "CONSOLIDATED" after its own note says consolidation ceased

The Q1FY27 deck (2026-08-21) headers read "Q1-FY27 **Consolidated** Financial Performance" (p.13),
"QUARTERLY **CONSOLIDATED** FINANCIAL PERFORMANCE" (p.15), "**CONSOLIDATED** INCOME STATEMENT"
(p.16), "**CONSOLIDATED** BALANCE SHEET" (p.17).

The footnote to pp.15 and 16 says: "PT Automotive Systems Indonesia Ltd., the Company's wholly
owned subsidiary, was dissolved effective June 25, 2025. Accordingly, **from April 1, 2026, the
Company has no subsidiaries and has discontinued the preparation of consolidated financial
statements.**"

The filing confirms it: the 2026-08-07 board outcome approves "Unaudited **Standalone** financial
results" and the Deloitte review report covers the standalone statement only.

So p.16 places FY24, FY25 and FY26 consolidated columns beside a Q1-FY27 **standalone** column under
a single "CONSOLIDATED INCOME STATEMENT" header, with no basis note on the columns themselves. This
is a comparability trap for any stage that lifts a series off that page.

A second, smaller defect sits in the same note: the dissolution is dated 25-Jun-2025 but
consolidation is said to cease from 01-Apr-2026, nine months later, with no explanation.

**Anchors:** presentation__Investor_Presentation_2026-08-21_Q1FY27 pp.13, 15, 16, 17;
results__Q1FY27_Board_Outcome_and_Results_2026-08-07 pp.1, 3, 4 (Note 5 area, extracted lines
212-214).

---

### V-10 [MAJOR] Two chart errors in the deck series, one contradicting the same deck's own income statement

**(a) FY25 PAT shown as 1,112 instead of 823.** Q1FY27 deck p.17, "FINANCIAL GRAPHS", PAT chart
data reads "593 / 1,112 / 1,112 / 270" for FY24 / FY25 / FY26 / Q1FY27. The correct FY25 PAT is
**823**, as printed on p.16 of the same deck. The FY26 value is duplicated into the FY25 slot. The
margin line beneath it (8.19% / 9.74% / 10.41% / 8.87%) is correct, so the chart shows a PAT bar
inconsistent with its own margin label.

**(b) FY23 EBITDA margin shown as 8.81% on the overview page and 8.05% inside the same deck.**
Q2FY26 deck p.4 and Q4FY26 deck p.4 both print the FY23 EBITDA margin as **8.81%**. The income
statement pages of those same decks print **8.05%** (Q2FY26 p.17; Q4FY26 p.17 and p.19). The correct
figure is 8.05% (EBITDA 528 / revenue 6,563). The Q1FY26 deck p.4 had it right at 8.05%. The error
appeared at Q2FY26, survived three quarters uncorrected, and then FY23 was dropped from the Q1FY27
overview chart entirely.

These are the two most-viewed pages in an IR deck. Neither error was corrected across the series.

**Anchors:** presentation__Investor_Presentation_2026-08-21_Q1FY27 pp.16, 17;
..._2025-11-25_Q2FY26 pp.4, 17; ..._2026-06-01_Q4FY26 pp.4, 17, 19; ..._2025-08-20_Q1FY26 p.4.

---

### V-11 [MAJOR] Advertisement and sales promotion spend fell 31% while every deck claims constant brand-building

AR2026 Note 37, Other Expenses (extracted line 14745, PDF p.220): "Advertisement and sales promotion
expenses **267** [FY26] **386** [FY25]" Rs Lakhs, a **-30.8%** decline in a year revenue grew 26.6%.

Against this, the Aftermarket column of the Product Portfolio page, identical in all five decks
(p.7): "A dedicated team is focusing on aftermarket and several measures are taken to strengthen
brand image, product range, **constant sales promotion efforts** and distribution network to extract
maximum value for business."

The claim and the number point opposite ways, and the claim is repeated verbatim for five quarters
while the number falls.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 14722-14756 (PDF p.220); all five
decks p.7.

---

### V-12 [MAJOR] Single audited segment; the deck's revenue mix is unaudited, and general-purpose parts near-tripled with no narrative

The results filing states: "The operations of the Company relate to **only one segment** viz.
Electrical and Electronic products for two/three wheelers and engines" (results__Q1FY27_Board_
Outcome_and_Results_2026-08-07 p.4, extracted line 183).

Every mix figure in the decks is therefore management-reported and unaudited, including:

| Deck disclosure | FY25 (Q1FY26/Q2FY26 decks p.4-5) | FY26 (Q4FY26/Q1FY27 decks p.4-5) |
|---|---|---|
| 2 Wheelers | 91% | 85% |
| 3 Wheelers | 5% | 6% |
| **General purpose parts** | **4%** | **9%** |
| Domestic / Export | 96% / 4% | 92% / 8% |

General-purpose parts moved from 4% of Rs 8,448 Mn (~Rs 338 Mn) to 9% of Rs 10,685 Mn (~Rs 962 Mn),
roughly **2.8x in one year**, and 2W fell six points of mix. Not one Operational Highlights bullet
in any of the five decks mentions the general-purpose engine business growing. The only adjacent
disclosure is the Generac USA "Excellence in Innovation" award (Q1FY26 deck p.14) and the export
"3x YoY growth in H1" claim (Q2FY26 deck p.14).

A near-tripling of a revenue line, unexplained and unauditable, sitting under a mix-shift margin
narrative, is a gap that has to be named before any base-case revenue basis is set.

**Anchors:** results__Q1FY27_Board_Outcome_and_Results_2026-08-07 p.4; presentation__Investor_
Presentation_2025-08-20_Q1FY26 pp.4-5, 14; ..._2025-11-25_Q2FY26 pp.4-5, 14; ..._2026-06-01_Q4FY26
pp.4-5; ..._2026-08-21_Q1FY27 pp.4-5.

---

### V-13 [MAJOR] The Lucas TVS stake: 32.2% of net worth, Level 3, self-set 8x multiple, drives all OCI, and a Q1FY27 markdown reported with zero narrative

AR2026 Note 42 (extracted line 15122, PDF p.227): "Investments in Equity Shares accounted as fair
value through comprehensive income | **Lucas TVS Limited | 26,412 | 22,468**" Rs Lakhs.

AR2026 Note 47 (extracted lines 15286-15334, PDF pp.230-231):
- Unlisted equity at FVTOCI, **Level III**: 26,455 (FY26) / 22,511 (FY25). Lucas TVS is 26,412 of the
  26,455, i.e. **99.8%** of the Level 3 book.
- "(f) The Company has invested in the equity shares of Lucas TVS Limited. This investment is
  considered to be a level 3 fair valuation. Valuation technique used - Market Approach: Comparable
  companies Method ("CCM") (EV/EBITDA Multiple...)".
- "(g) Significant unobservable inputs - **EV/EBITDA Multiple at 8x** (Previous Year - EV/EBITDA
  Multiple at 8x)... A decrease in the multiple by 0.5x would result in a decrease in the fair value
  by Rs 1,651 Lakhs".

AR2025 records the multiple as 8x with "Previous Year - EV/EBITDA Multiple at **9x**" (extracted line
59684), so the multiple was cut a full turn in FY25 and held at 8x in FY26 while the carrying value
still rose 17.6%.

**Scale.** Rs 26,412 lakhs is **32.2% of net worth** (82,133 lakhs) and **49.7% of total investments**
(53,153 lakhs). Lucas TVS is a promoter-group company; INEL's holding company Lucas Indian Service
is 70.32% shareholder of INEL, and INEL received Rs 433 lakhs of dividend from Lucas TVS in FY26
(Note 42, extracted line 15071), which is 92% of its total dividend income of 470 lakhs (Note 29).

**Consequence the decks never state.** Other Comprehensive Income is essentially this one Level 3
mark. FY26 OCI +3,969 lakhs pre-tax; the Lucas TVS carrying value rose 3,944 lakhs. **Q1FY27 OCI was
-1,675 lakhs pre-tax** (results filing p.4), a ~6% markdown in one quarter, which is roughly a 0.5x
move in the self-selected multiple. The Q1FY27 deck reports the consequence as a single table row,
"Other Comprehensive Income (143)" and "Total Comprehensive Income 127, (45.7)%" (p.15), and says
nothing about it on the Operational Highlights page.

B05's Section 2D names the Lucas TVS disclosure gap and the 32.2% figure (crediting B02/B03). It does
not carry the valuation mechanism, the 8x input, the sensitivity, or the Q1FY27 markdown. Partially
caught; the mechanism is what makes it actionable.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 15107-15123 (PDF p.227), 15286-15334
(PDF pp.230-231), 14613-14629 (PDF p.218); annual-report__Annual_Report_2025 extracted lines
59678-59687; results__Q1FY27_Board_Outcome_and_Results_2026-08-07 p.4; presentation__Investor_
Presentation_2026-08-21_Q1FY27 pp.14, 15.

---

### V-14 [MAJOR] Customer concentration: the percentage basis contradicts "progressively reduced" more cleanly than the rupee basis B05 used

AR2026 Note 28(e), Information about major customers (extracted lines 14603-14612, PDF p.218):
"No of customers 2 / Amount involved 75,491 [FY26] 62,365 [FY25]".
AR2025 same note (extracted lines 58820-58831): "62,365 [FY25] 48,751 [FY24]", with total revenue
from operations 84,483 (FY25) and 72,408 (FY24).

| | FY24 | FY25 | FY26 |
|---|---|---|---|
| Two-customer revenue (Rs Lakhs) | 48,751 | 62,365 | 75,491 |
| Total revenue from operations (Rs Lakhs) | 72,408 | 84,483 | 1,06,848 |
| **Share** | **67.33%** | **73.82%** | **70.65%** |

The MD&A claim, repeated in the FY26 risk table: "The Company has also **progressively reduced its
dependency on key customers over the years**" (AR2026 extracted lines 8199-8201, PDF p.126).

Over the three years the AR's own note covers, the share went **up**, 67.33% to 70.65%. That is the
contradiction, and it is on the company's own preferred percentage measure.

**Where B05 is weaker.** B05's promise-delivery row rests on "two-customer concentration **up 21.1%
in absolute rupees**". Rupee concentration rises mechanically with revenue and is a weak rebuttal;
worse, on the year-on-year percentage basis the share **fell** 73.82% to 70.65%, which superficially
supports management. The conclusion survives, the stated reasoning does not. Logged as PARTIALLY
CAUGHT and as a MINOR finding against B05 in Part 3.

The customers are named in the BRSR, not in any deck: "Our major customers - TVS Motor Company
Limited, Hero MotoCorp Limited and Bajaj Auto Limited" (AR2025 extracted line 51586; AR2026 extracted
line 8443). No deck discloses concentration at all; p.6 of each deck is an unlabelled logo wall.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 14603-14612 (PDF p.218), 8188-8202
(PDF p.126), 8443; annual-report__Annual_Report_2025 extracted lines 51586, 58817-58831.

---

### V-15 [MAJOR] Rare-earth NdFeB magnet constraint named in five consecutive quarters, never quantified, and the disclosed mitigation is a materials downgrade

Present in every deck's Operational Highlights, p.14:
- Q1FY26 (2025-08-20): "Supply-side headwinds continue due to China's export licensing on rare earth magnets"
- Q2FY26 (2025-11-25): "production continues to be impacted by rare earth magnet supply disruptions"
- Q4FY26 (2026-06-01): "Supply constraint witnessed in NdFeB magnets due to geopolitical stance by China"
- Q1FY27 (2026-08-21): "Continued supply-side challenges in NdFeB magnets amid geopolitical developments and evolving China-related trade dynamics"

Five quarters, zero rupee or volume quantification, no resolution.

**The point B05 does not draw out.** The AR's named mitigation is "increased adoption of **ferrite
magnets** as an alternative to rare earth materials" (AR2026 extracted lines 8153-8156, PDF p.125).
Ferrite is a lower energy-density magnet than NdFeB. Substituting it into flywheel magnetos is a
product-specification change with implications for performance and price realisation that no
document addresses. **[INFERENCE]** A materials downgrade presented as a supply-risk mitigation, in
a company whose margin story rests on moving up the value ladder, is a tension that needs a
confirming observation: the AR's own milestone list separately cites "GPS sensors using **ferrite
magnet technology**" among new OEM nominations (extracted lines 851-855, PDF p.16), which suggests
the substitution is being designed in rather than merely tolerated. Peer Minda treats the same
substitution as an engineering achievement (MINDACORP Nov 2025 p.9, ferrite and magnet-less motors).
The reading is genuinely two-sided and the separating observation is a disclosed ferrite-substituted
share, which does not exist.

CAUGHT by B05 as a persistence flag; the materials-downgrade dimension is new here.

**Anchors:** four decks p.14 as dated; annual-report__Annual_Report_2026 extracted lines 8147-8157
(PDF p.125), 848-855 (PDF p.16).

---

### V-16 [MAJOR] The BorgWarner EFI-ECU slide is verbatim identical across five quarters, including the word "Recently"

The "Future Growth Strategies" page (p.10 or p.11) is word-for-word identical in the Q1FY26,
Q2FY26, Q4FY26 and Q1FY27 decks, including: "**Recently** entered into a Technical Licensing
partnership with Borg Warner, a globally leading automotive supplier, for the Control unit for
Electronic Fuel Injection (EFI ECU) which will enable to enter a new product segment of the EFI
system and serve customers for two and three-wheeler applications."

"Recently" in August 2026 describing the same event it described in August 2025 is the flag. No
milestone, no SoP date, no rupee value, no status change in a full year.

CAUGHT by B05, which also adds the AR's in-house pivot. See V-17 for the part B05 missed.

**Anchors:** presentation__Investor_Presentation_2025-08-20_Q1FY26 p.11; ..._2025-11-25_Q2FY26 p.11;
..._2026-06-01_Q4FY26 p.11; ..._2026-08-21_Q1FY27 p.11.

---

### V-17 [MINOR] There are three EFI/ECU partner stories in the corpus, not two, and none is reconciled

B05 identifies two threads (BorgWarner in the decks, in-house pivot in the AR) plus the unnamed MoU.
The AR carries a fourth name that B05 does not mention.

| Thread | Source |
|---|---|
| BorgWarner technical licence for EFI ECU | all five decks, p.11 |
| "**Partnership with Athena, Italy for EFI**" | AR2026 milestone timeline, extracted line 827, PDF p.16 |
| "Signed a MoU with a **technology partner** for ECU development", unnamed | Q4FY26 deck p.14 only, absent from Q1FY27 |
| "we **initiated in-house software development for EFI controllers**" | AR2026, extracted lines 1294-1299, PDF p.24 |

Counter-evidence that cuts the other way and that neither B05 nor I should suppress: the AR
milestone list records "**Secured business nominations from major OEMs for EFI ECU**, ISG systems,
GPS sensors using ferrite magnet technology, and crank position sensors" (extracted lines 851-855,
PDF p.16). That is a concrete commercial outcome for the EFI ECU line that the decks never state.
It makes B05's "MISSED / PIVOTED" verdict on the BorgWarner promise **harsher than the AR supports**:
the route is confused, the outcome is not obviously a miss. See Part 3, spot check SC2.

**Anchors:** annual-report__Annual_Report_2026 extracted lines 823-855 (PDF p.16), 1294-1301
(PDF p.24); presentation__Investor_Presentation_2026-06-01_Q4FY26 p.14.

---

### V-18 [MINOR] The leadership claim narrows from "ignition systems" to "Fly Wheel Magneto", with no source in either form

- Q1FY26 deck p.14: "Retained the **No. 1 position in ignition systems** for the last three years;
  outpaced industry growth during the quarter"
- Q4FY26 deck p.14: "Retained the No. 1 market position in the **Fly Wheel Magneto** segment"
- Q1FY27 deck p.14: "Maintained the No. 1 position in **Fly Wheel Magneto**, with further market
  share gains during the quarter"

The claim narrows from a product category to a single product between Q1FY26 and Q4FY26 and stays
narrow. No share percentage, no measuring body, no source is cited in any version. No peer transcript
across twelve calls names the flywheel magneto or ignition-system category at all, so there is no
external check available.

B05 lists the FWM No.1 claim as a trigger with "No % share ever given", which catches the
unquantification but not the narrowing. PARTIALLY CAUGHT.

**Anchors:** presentation__Investor_Presentation_2025-08-20_Q1FY26 p.14; ..._2026-06-01_Q4FY26 p.14;
..._2026-08-21_Q1FY27 p.14.

---

### V-19 [MINOR] Aftermarket growth decelerates 28% to 20% with no comment, and is never sized while peers size theirs

- Q1FY26 deck p.14: "Q1 sales up 21% YoY, with **aftermarket sales up 28%**"
- Q2FY26 deck p.14: "Aftermarket segment maintained strong momentum" (no number)
- AR2026 MD&A: "its aftermarket business registered a notable growth of **20%**" (extracted line
  8054, PDF p.124)
- AR2026 MD&A, same page: "The aftermarket segment, **though currently small**, is scaling quickly"
  (extracted line 8101)

Full-year 20% against Q1's 28% is a deceleration through the year that no document states. No deck
gives an aftermarket revenue figure in any period.

**Peer contrast.** Minda discloses aftermarket as a reported share of revenue every quarter, 8% in
Q1FY27 and ~10% in Q4FY26, with segment growth of 33% YoY (MINDACORP Aug 2026 extracted lines
256-257, 278; MINDACORP May 2026 extracted line 273). Varroc treats aftermarket as a named growth
pillar with its own commentary (VARROC Nov 2025 extracted lines 158-160).

B06's Q3 covers content-per-vehicle quantification generally. Neither B05 nor B06 runs the
aftermarket-sizing comparison specifically. PARTIALLY CAUGHT.

**Anchors:** presentation__Investor_Presentation_2025-08-20_Q1FY26 p.14; annual-report__Annual_
Report_2026 extracted lines 8048-8103 (PDF p.124); peer-concalls__MINDACORP-Concall_Aug_2026
extracted lines 254-279; peer-concalls__MINDACORP-Concall_May_2026 extracted line 273.

---

### V-20 [MINOR] Capital commitments rose 7.2x with no capex plan anywhere in the deck series

AR2026 Note 45 (extracted lines 15172-15174, PDF p.228): "Estimated amount of contracts remaining to
be executed on capital account and not provided, net of advance | **2,635** [FY26] | **367** [FY25]"
Rs Lakhs, a **+618%** move.

Contingent liabilities in the same note: disputed income tax demands 1,490 (FY26) against 1,034
(FY25), **+44.1%**; disputed GST 130 flat; service tax 3 flat.

Rs 26.35 Cr of contracted, unexecuted capex is a forward commitment larger than the FY26 capex
itself, and no deck states a capex figure, a project, a capacity number, or a commissioning date.
B06's Q9 establishes the peer disclosure norm and B05's peer question 9 cites B03's Rs 42.15 Cr
capex figure, so capex opacity is CAUGHT in general; the committed-forward-capex leg and the
tax-dispute build are not. PARTIALLY CAUGHT.

**Anchor:** annual-report__Annual_Report_2026 extracted lines 15162-15179 (PDF p.228).

---

### V-21 [MAJOR] Growth claims are systematically unquantified across the deck series

Confirmed independently across four decks read in full. "Secured new business across ISG Controllers,
DC-DC Converters, Sensors, Actuators and Controllers" (Q1FY27 p.14), "Secured new premium business in
high-efficiency systems and flywheel magneto" (Q1FY26 p.14), "Secured high-volume model business from
a West-based customer" (Q2FY26 p.14), "Commenced SoP for the Super-Premium 2-wheeler segment" (Q1FY27
p.14), "further market share gains during the quarter" (Q1FY27 p.14): none carries a rupee value, a
unit count, a customer name, or a date. The exceptions across five quarters are "~2 million units"
of flywheel magneto (Q1FY27 p.14) and the named Generac USA award (Q1FY26 p.14).

CAUGHT by B05 (4D) and independently corroborated by B06's Q3 peer benchmark.

---

### V-22 [MAJOR] Industry growth comparator is unsourced and the Q1FY27 denominator sits below peer readings

INEL cites 2W industry growth of 11% (Q2FY26 p.14), 19% (Q4FY26 p.14) and 20% (Q1FY27 p.14) with no
source named in any deck. For Q1FY27 the peer set reads higher: Pricol's MD states on the record
"All the industry put together weighted average grew by **22%**. We grew by 26%" (PRICOLLTD Aug 2026,
extracted line 631, verified verbatim). B06 adds Varroc 22.8% and Minda 23% for the same quarter.

CAUGHT by B06 (Q1), verified.

---

### V-23 [MAJOR] Disclosure practice on pass-through mechanism, content-per-vehicle and capex sits well below the standard three direct peers set

CAUGHT by B06 (Q2, Q3, Q9). I verified the load-bearing quote in the receivables leg and the Pricol
industry-growth leg; the remainder is consistently anchored to peer, date and page and I found no
overstatement in it.

---

### V-24 [MAJOR] EV content accrues to EV-native product lines, making rising 2W EV penetration a content-destruction risk for a magneto-led ICE supplier

CAUGHT by B06 (Q5). Two sharpenings from my own read that B06 does not carry:

- Peers now quantify the EV revenue share they have already captured: Varroc "in the last quarter in
  India, about **14% of revenues came from EV**" (VARROC Jun 2026, extracted line 306); Minda "EV
  percentage as revenue is close to **10%**... At Flash Electronics, the EV revenue constitutes to
  about **30%**... At Minda Corporation Group level, it is close to about **14%**" (MINDACORP Aug
  2026, extracted lines 158-161). INEL discloses **no EV revenue figure at all**, in any deck or in
  the AR, while running "Growing EV Product Portfolio" as growth strategy number two for five
  consecutive quarters.
- INEL's own EV-penetration framing is internally inconsistent. The Q2FY26 deck p.14 says "EV
  penetration remains at 7%". The AR2026 MD&A says "Overall EV adoption across categories reached a
  record **8.5%** by the end of 2025-26" (extracted line 7766, PDF p.121) and, three pages later,
  "EV penetration neared **10%** of total sales by late 2025" (extracted line 8019, PDF p.124). Two
  figures for the same variable in one MD&A.

---

## PART 2: COMPARISON TABLE

Twenty-four independent flags. CAUGHT means B05 or B06 found it and weighted it correctly.

| # | Item | Severity | Verdict | Where upstream |
|---|---|---|---|---|
| V-01 | Deck ROCE 34.97% vs audited Note 51 ROCE 17% | CRITICAL | **MISSED** | — |
| V-02 | FY26 margin expansion does not survive filed numbers; deck EBITDA includes FX gains | CRITICAL | **MISSED** | — |
| V-03 | MD&A "Net Profit Margin 13.7%" vs audited "Net profit ratio 10.40%" | MAJOR | **MISSED** | — |
| V-04 | CFO cessation filed 07-Aug, absent from 21-Aug deck; filing self-contradictory | MAJOR | **MISSED** | — |
| V-05 | Employee count 1,605+ / 2,601 / 2,811, deck figure frozen 5 quarters | MAJOR | **MISSED** | — |
| V-06 | R&D flat, R&D capex -41.7%, intensity -75 bps, vs technology narrative | MAJOR | **MISSED** | — |
| V-07 | Parent-company receivable stretched ~80 to ~108 days on +22% sales | MAJOR | **MISSED** | — |
| V-08 | 91.7% non-permanent workers; Rs 30.6 Cr apprentice stipend to related party; labour-code risk unquantified | MAJOR | **MISSED** | — |
| V-09 | Q1FY27 deck labelled CONSOLIDATED after consolidation ceased | MAJOR | **MISSED** | — |
| V-10 | Deck chart errors: FY25 PAT 1,112; FY23 EBITDA margin 8.81% vs 8.05% same deck | MAJOR | **MISSED** | — |
| V-11 | Advertising and sales promotion -30.8% vs "constant sales promotion efforts" boilerplate | MAJOR | **MISSED** | — |
| V-12 | Single audited segment; unaudited mix; GP parts 4% to 9% unexplained | MAJOR | **MISSED** | — |
| V-13 | Lucas TVS Level 3 stake, 8x self-set multiple, drives all OCI, Q1FY27 markdown unnarrated | MAJOR | **PARTIALLY CAUGHT** | B05 2D (gap named, mechanism absent) |
| V-14 | Customer concentration contradiction on the percentage basis (67.33% to 70.65%) | MAJOR | **PARTIALLY CAUGHT** | B05 2A (rupee basis, weaker) |
| V-15 | NdFeB constraint 5 quarters; ferrite substitution is a materials downgrade | MAJOR | **CAUGHT** (persistence) / partial (downgrade) | B05 1C |
| V-16 | BorgWarner slide verbatim for 5 quarters including "Recently" | MAJOR | **CAUGHT** | B05 1C, 4D |
| V-17 | Three EFI/ECU partner names, not two (Athena, Italy) | MINOR | **PARTIALLY CAUGHT** | B05 1C |
| V-18 | Leadership claim narrows from ignition systems to flywheel magneto | MINOR | **PARTIALLY CAUGHT** | B05 1A |
| V-19 | Aftermarket 28% to 20% deceleration, never sized; peers size theirs | MINOR | **PARTIALLY CAUGHT** | B05 1A / B06 Q3 |
| V-20 | Capital commitments +618%; tax disputes +44% | MINOR | **PARTIALLY CAUGHT** | B06 Q9 |
| V-21 | Systematic unquantification of growth claims | MAJOR | **CAUGHT** | B05 4D |
| V-22 | Industry comparator unsourced; Q1FY27 20% below peer 22-23% | MAJOR | **CAUGHT** | B06 Q1 |
| V-23 | Disclosure practice below peer standard on pass-through, content, capex | MAJOR | **CAUGHT** | B06 Q2/Q3/Q9 |
| V-24 | EV content accrues to EV-native lines; content-destruction risk | MAJOR | **CAUGHT** | B06 Q5 |

**Tally: CAUGHT 7. PARTIALLY CAUGHT 5. MISSED 12.**

**acceptance_rate = 7 / 24 = 29%.**

### Reading the rate honestly

The rate is low and it should not be read as B05 and B06 being poor reports. Both are strong within
their scope. The pattern in the misses is a single, clean scope gap:

- **B05 audited the narrative layer** (deck prose against AR prose, this year's language against last
  year's) and did it well. Every one of its own flags survived my check.
- **B06 audited the peer layer** and did it well. Its crux quote is verbatim accurate and it correctly
  reported zero peer mentions of the company.
- **Neither audited the deck's numbers against the audited financial statements.** All twelve MISSED
  items come from that one operation: Note 51 against the deck charts, the results filing against the
  deck income statement, the notes against the MD&A ratios, the BRSR against the snapshot page.

Two of the twelve are CRITICAL and both change decisions: V-01 moves the quality-ladder rung by three
steps, V-02 removes the only quantitative support for the margin-expansion thesis. Those two alone
justify the REWORK trigger regardless of the arithmetic of the rate.

**Caveat repeated:** B01, B02, B03 and B07 are not in my inputs. B05 cites B02/B03 for CFO/PAT,
receivables ageing, the Lucas TVS 32.2%, and the Rs 42.15 Cr capex, so the upstream evidence layer
clearly does read the notes. Whether V-01, V-02 or V-03 were caught there, I cannot say. The
orchestrator should check B01/B02/B03 before routing rework, and should route it to whichever stage
owns deck-versus-audited-statement reconciliation.

---

## PART 3: PIPELINE FLAGS I DID NOT FIND INDEPENDENTLY

Assessed as SUPPORTED / OVERSTATED / NOT SUPPORTED per rule 3.

| Pipeline flag | Source | Verdict | Basis |
|---|---|---|---|
| Working-capital-days contradiction: AR letter claims 42 to 40, decks show 40 to 42 | B05 4D, flags | **SUPPORTED** | AR2026 extracted lines 420-424 (PDF p.9) verbatim: "we have successfully reduced our working capital days from 42 to 40 days". Q4FY26 deck p.19 and Q1FY27 deck p.18 charts both read FY23=57, FY24=42, FY25=40, FY26=42. Contradiction confirmed on both legs. I did not find this independently because I had not read the chairman's letter before reading B05; it is a genuine B05 catch. |
| AR2026 reports an in-house EFI pivot the decks never disclose | B05 1C, 4D | **SUPPORTED as to fact, OVERSTATED as to verdict** | AR2026 extracted lines 1294-1299 (PDF p.24) verbatim: "we initiated in-house software development for EFI controllers". The pivot is real. But the same AR records "Secured business nominations from major OEMs for EFI ECU" (extracted lines 851-855, PDF p.16) and a separate "Partnership with Athena, Italy for EFI" (line 827). Calling the EFI-ECU promise "MISSED / PIVOTED" is harsher than the AR's own evidence supports. Downgrade to PARTIAL with the confusion of routes as the flag, not the outcome. |
| Note 51 self-discloses that the exceptional item inflates ROE/ROCE/Net Profit | B05 2C (via B02) | **SUPPORTED** | AR2026 extracted line 19781: "**Includes exceptional item", footnoted against Return on equity, Net profit ratio and Return on capital employed. A genuine self-disclosed caveat. |
| Varroc denied any receivable-days change in Q1FY27 | B06 Q4, contradicted[] | **SUPPORTED, verbatim** | VARROC Aug 2026 extracted lines 623-628: "Neha Garg: ...has there any change in the receivable days from OEM customers or it's mainly from the inventory side? / Mahendra Kumar: Yes. there is no change receivable days. Yes, inventory went up to some extent, largely in preparation to the peak season". B06's bracketed "[in]" insertion is honest transcription repair. |
| No peer names India Nippon Electricals (peer_mentions_of_company: []) | B06 2D, YAML | **SUPPORTED** | Searched all twelve transcripts for Nippon / Lucas / magneto / ignition / flywheel. The only "Nippon" hit is **Nippon Seiki**, a Japanese cluster maker, in PRICOLLTD Aug 2026 extracted line 618. B06 correctly did not claim it. No magneto, ignition or flywheel reference exists in any peer call. |
| Pricol cited 22% weighted-average industry growth in Q1FY27 | B06 Q1 | **SUPPORTED, verbatim** | PRICOLLTD Aug 2026 extracted line 631. |
| Customer-concentration reasoning ("up 21.1% in absolute rupees") | B05 2A | **OVERSTATED reasoning, correct conclusion** | See V-14. On the percentage basis the FY25-to-FY26 share **fell** (73.82% to 70.65%), so the rupee argument is the weakest available and is vulnerable to a management rebuttal. The valid contradiction is the FY24-to-FY26 arc, 67.33% to 70.65%. Logged as a MINOR finding against B05, not against the company. |
| CFO/PAT deterioration to 0.36x, never mentioned in any narrative document | B05 4D (via B01/B03) | **NOT INDEPENDENTLY TESTED, direction corroborated** | The cash flow statement is outside my source set, so I cannot verify 0.36x. The direction is corroborated by the AR letter's own admission of "increased working capital requirements arising from higher business volumes, export growth, and strategic inventory build-up" (AR2026 extracted lines 414-419) and by the 41% rise in raw-material closing stock (4,881 to 6,872 lakhs, Note 30, extracted lines 14635-14639). Verifier A owns the number itself. |

**pipeline_flags_not_supported: none.** No B05 or B06 flag failed my read of the sources. Two carry
reasoning defects (the EFI verdict severity, the concentration argument basis) and are logged as MINOR
findings against the reports, not as invented signals.

---

## PART 4: PROMISE-DELIVERY SPOT CHECKS

Rule 4 requires 3 to 5. Six run, both legs of each checked against the source.

| # | Promise leg | Outcome leg | Verdict |
|---|---|---|---|
| SC1 | AR2026 letter p.9 claims WC days reduced 42 to 40 | Q4FY26 deck p.19 and Q1FY27 deck p.18 both show FY26 = 42, up from FY25 = 40 | **CONFIRMED**, both legs verbatim |
| SC2 | Decks promise EFI-ECU via BorgWarner licence, all 5 quarters | AR2026 reports in-house EFI software development initiated; AR also reports OEM business nominations secured for EFI ECU, and a separate Athena Italy EFI partnership | **CONFIRMED WITH CAVEAT** — the route contradiction is real, the "MISSED" outcome label is too harsh (see Part 3) |
| SC3 | "Progressively reduced dependency on key customers", AR2026 risk table | Note 28(e): 67.33% (FY24) to 73.82% (FY25) to 70.65% (FY26) | **CONFIRMED** on direction over the period; B05's stated rupee reasoning is the weak form. FY25 AR repetition of the identical sentence NOT VERIFIED by me (AR2025 extraction is character-fragmented in the MD&A prose region) |
| SC4 | Q4FY26 deck p.14 announces an unnamed ECU-development technology-partner MoU | Q1FY27 deck p.14 contains no such bullet; no naming, no cancellation | **CONFIRMED**, both legs |
| SC5 | BorgWarner paragraph identical, word-for-word, across the deck series | Verified identical in Q1FY26 p.11, Q2FY26 p.11, Q4FY26 p.11, Q1FY27 p.11 | **CONFIRMED** on 4 of 5 legs; Q3FY26 deck not read by me |
| SC6 | B06's crux: Varroc denies receivable-days change, Q1FY27 | VARROC Aug 2026 extracted lines 623-628 | **CONFIRMED**, verbatim |

**checked 6, confirmed 6, wrong 0.** The promise-delivery table's direction is sound. One severity
label (SC2) is too harsh and one line of reasoning (SC3) is weaker than the evidence available.

---

## PART 5: SUPPLEMENTARY DOCUMENT DEFECTS

Real, anchored, but below red-flag grade. Excluded from the acceptance-rate denominator so the rate is
not inflated by trivia. All MISSED upstream unless noted.

1. **Exceptional item is 71% interest, not land value.** Results filing p.4, Note 6 (extracted lines
   209-211): "compensation on compulsory acquisition of land in 2010 amounting to Rs. 445 lakhs
   **along with interest thereon amounting to Rs. 1,076 lakhs**", aggregating to Rs 1,521 lakhs. The
   Q4FY26 deck p.14 describes it only as "exceptional income of INR 15.2 crore towards land
   compensation from the Haryana government". Fifteen years of accrued interest recognised in one
   quarter, described as land compensation. **[MINOR]**
2. **Q1FY26 comparatives silently restated between decks.** Q1FY26 deck p.15 reported EBITDA 235,
   margin 10.46%, Other Income 113, PAT 232, Taxes 73, EPS 10.26. The Q2FY26 deck p.15 shows EBITDA
   234, margin 10.41%, Other Income 114. The Q1FY27 deck p.15 shows PAT 233, Taxes 72, EPS 10.30. No
   restatement note anywhere. **[MINOR]**
3. **Three FY26 revenue bases.** Audited revenue from operations Rs 1,06,848 lakhs (results filing
   p.4); MD&A table Gross Sales Rs 1,06,440 and Net Sales Rs 1,05,292 (extracted lines 8118-8119);
   MD&A prose "highest-ever turnover of Rs 1,068 Crores" (extracted lines 8050-8051), which matches
   the audited figure and neither line of its own table. The MD&A key ratios are computed on Gross
   Sales, which is Rs 408 lakhs below the audited revenue. **[MINOR]**
4. **Three FY26 ROE figures, no basis stated on any.** Note 51: 15% (average shareholders' equity,
   includes exceptional). MD&A: Return on Net Worth 14.5%. Deck p.19: ROE 13.58% (closing net worth).
   **[MINOR]**
5. **Deck EPS 49.14 against AR Note 44 EPS 49.18.** Not an error: 49.14 is consolidated (Directors'
   Report consolidated PAT 11,117 / 2,26,21,424 shares) and 49.18 is standalone (Note 44, extracted
   lines 15158-15161). Neither document cross-references the other. A basis trap for any stage that
   picks an EPS off a page. **[MINOR]**
6. **Return on investment fell to 13% from 14%** (Note 51) on an investment book of Rs 531.5 Cr that is
   50% of total assets. Never mentioned in any document. **[MINOR]**
7. **Gratuity expense +291.8%** (Rs 85 to 333 lakhs, Note 34) and **commission to directors +109.8%**
   (Rs 143 to 300 lakhs, Note 37) against PAT growth of 35.6%. Neither explained. **[MINOR]**
8. **Management fees to Lucas TVS rose to Rs 832 lakhs** (FY24 648, FY25 726, FY26 832; Note 42) with
   no description of the services anywhere. **[MINOR]**
9. **Snapshot "3 Year Revenue CAGR 17.64%" is no longer verifiable inside the Q1FY27 deck**, which
   dropped FY23 from its income statement (p.16). It checks out against the Q4FY26 deck (6,563 to
   10,685 = 17.63%). **[MINOR]**
10. **Raw-material closing stock +40.8%** (Rs 4,881 to 6,872 lakhs, Note 30) against revenue +26.6%,
    consistent with the magnet stockpiling named once in Q3FY26 but never quantified. Corroborates
    B05's cash-conversion flag. **[MINOR]**

---

## PART 6: CREDIBILITY GRADE

**B05 assigned C. I would grade lower: D.**

B05's C rests on genuine execution evidence (Rewari third-phase line, Hosur SoP) offsetting two
narrative contradictions. That balance holds if the contradictions are confined to narrative. My read
shows they are not. The two headline quality metrics an investor takes off the deck, ROCE and EBITDA
margin, are both non-GAAP constructions that the company never defines and that differ from its own
audited note by 18 percentage points and by the entire direction of the margin trend. Add a
SEBI-mandated MD&A ratio labelled "Net Profit Margin" that is a pre-tax margin including a one-off,
three employee counts, a frozen headcount figure, two uncorrected chart errors, and a CFO transition
omitted from the deck filed fourteen days after the board approved it.

That is not a company with thin disclosure. It is a company whose investor-facing numbers are
systematically more flattering than its audited ones, on every metric where the two can be compared.
The execution evidence is real and I do not dismiss it. It does not offset this.

I do not raise this to a governance verdict. Per the pipeline rules, flags propagate and the decision
stays human.

---

## PART 7: WHAT I DID NOT ASSESS

Stated so no downstream stage reads silence as clearance.

- **Evasion, deflection, answer quality, tone under pressure, analyst insistence, contradictions
  between answers to different analysts.** NOT ASSESSABLE. No Q&A exists for the subject company. The
  AGM Outcome filing (2026-07-30) records that queries were answered and discloses no content. I did
  not manufacture any of this from prepared text, and B05 correctly did not either.
- **CFO/PAT, receivables ageing buckets, ECL, capex rupee totals.** Outside my source set (cash flow
  statement and ageing notes not read). Owned by B01/B02/B03 and by Verifier A on the numbers.
- **AR2025 MD&A prose.** The extraction for that file is character-fragmented in the narrative region,
  so year-on-year language comparison against FY25 prose is only partly possible. AR2025 numeric notes
  extracted cleanly and were used.
- **Q3FY26 deck.** Not in my provided source list; four of the five quarterly decks were read in full.
- **Whether any MISSED item was caught by B01, B02, B03 or B07.** Not in my inputs.

---

```yaml
stage: B12b
company: "INDNIPPON"
run_date: "2026-09-10"
model: claude-opus-4-8
status: complete
no_concall_mode: true
independent_flags_found: 24
caught: 7
partially_caught: 5
missed:
  - {severity: "CRITICAL", item: "Deck ROCE 34.97% (FY26) is 2.06x the audited Note 51 ROCE of 17%, on an undisclosed definition that appears to strip the entire Rs 531.5 Cr investment book out of capital employed. Moves the QUALITY LADDER rung from R2 to R5.", anchor: "presentation__Investor_Presentation_2026-06-01_Q4FY26 p.19 and ..._2026-08-21_Q1FY27 p.18 vs annual-report__Annual_Report_2026 Note 51, extracted lines 15507-15518 (PDF p.235) and 19752-19781 (PDF p.297)"}
  - {severity: "CRITICAL", item: "FY26 EBITDA margin expansion (11.27% to 11.44%, +17bps) does not survive the filed statements. Audited-basis margin was 11.11% (FY25) to 11.10% (FY26), flat to down. Deck EBITDA includes FX gains (Rs 372L FY26 vs Rs 102L FY25) that Note 29 classifies inside Other Income. Removes the only quantitative support for the mix-shift margin thesis.", anchor: "results__Q1FY27_Board_Outcome_and_Results_2026-08-07 p.4 (FY26 col: revenue 1,06,848; expenses 96,828; finance 52; depn 1,792) + annual-report__Annual_Report_2026 extracted lines 4209-4214, Note 29 line 14623, Note 35 line 14699 vs deck p.16"}
  - {severity: "MAJOR", item: "MD&A key-ratio table reports 'Net Profit Margin 13.7%' while audited Note 51 reports 'Net profit ratio 10.40%' for the same year. The 13.7% is PBT/Gross Sales including the Rs 1,521L exceptional item, overstating net margin by 330bps in a Schedule V disclosure.", anchor: "annual-report__Annual_Report_2026 extracted lines 8113-8131 (PDF p.125) vs 19752-19781 (PDF p.297)"}
  - {severity: "MAJOR", item: "CFO cessation (Elango Srinivasan, effective 30-Sep-2026) filed 07-Aug-2026 is absent from the Q1FY27 investor deck filed 21-Aug-2026. The filing itself is self-contradictory: p.1 encloses 'a copy of the resignation letter' while Annexure C records the reason as 'Change in designation'. He signed the FY26 accounts as CFO on 28-May-2026.", anchor: "results__Q1FY27_Board_Outcome_and_Results_2026-08-07 pp.1-2, 6-7; presentation__Investor_Presentation_2026-08-21_Q1FY27 (absence, whole deck); annual-report__Annual_Report_2026 extracted lines 15538-15543"}
  - {severity: "MAJOR", item: "Three employee counts: all five decks say '1,605+', MD&A says 2,601, BRSR says 397 employees + 2,414 workers = 2,811. The deck figure is frozen unchanged from Aug-2025 to Aug-2026 while the same snapshot page updates market cap each quarter.", anchor: "five decks p.3; annual-report__Annual_Report_2026 extracted lines 1894-1900 (PDF p.35), 8284-8286 (PDF p.127), 8461-8471"}
  - {severity: "MAJOR", item: "R&D total spend was flat (Rs 2,877L FY26 vs Rs 2,896L FY25, -0.7%) and R&D capex fell 41.7% (Rs 341L vs Rs 585L) in a year net sales grew 26.6%. R&D intensity fell 75bps to 2.73%. Contradicts 'Thrust On Technology' in every deck and the MD&A's system-level-solutions transition claim. No deck discloses R&D spend.", anchor: "annual-report__Annual_Report_2026 Note 43, extracted lines 15137-15151 (PDF p.228); MD&A extracted lines 8065-8094 (PDF p.124); all five decks pp.10-11"}
  - {severity: "MAJOR", item: "Trade receivable from the 70.32% holding company Lucas Indian Service rose 65.7% (Rs 1,089L to Rs 1,805L) on sales to it of +22.2%, implying a stretch from ~80 to ~108 days. LIS is the aftermarket distribution channel and those sales are the only quantifiable proxy for aftermarket revenue (5.8% of net sales). Never mentioned in any deck or narrative section.", anchor: "annual-report__Annual_Report_2026 Note 42, extracted lines 15055-15123 (PDF pp.226-227)"}
  - {severity: "MAJOR", item: "Labour structure: BRSR reports 2,213 of 2,414 workers as 'Other than Permanent' (91.7%); apprentice stipends of Rs 3,059L (+26.7% YoY, 2.3x since FY24) are paid to related party TVS Educational Society and sit outside employee-benefits expense, which is 20.5% of true labour cost off-line. The MD&A names 'anticipated impacts arising from labor code reforms' in one subordinate clause with zero quantification, while all three peers quantified labour-code cost as a discrete item.", anchor: "annual-report__Annual_Report_2026 extracted lines 8461-8471, 14681-14690 (PDF p.219), 15079-15083 (PDF p.227), 8147-8157 (PDF p.125); peer-concalls__MINDACORP-Concall_Feb_2026 extracted line 218"}
  - {severity: "MAJOR", item: "Q1FY27 deck labels every table CONSOLIDATED while its own footnote states consolidation was discontinued from 01-Apr-2026 and the underlying filing is standalone and limited-reviewed as standalone. Page 16 places FY24-FY26 consolidated columns beside a standalone Q1FY27 column under one header. Secondary defect: dissolution dated 25-Jun-2025 but consolidation ceasing 01-Apr-2026, unexplained.", anchor: "presentation__Investor_Presentation_2026-08-21_Q1FY27 pp.13, 15, 16, 17; results__Q1FY27_Board_Outcome_and_Results_2026-08-07 pp.1, 3, 4"}
  - {severity: "MAJOR", item: "Two uncorrected deck chart errors. (a) Q1FY27 deck p.17 PAT chart shows FY25 PAT as 1,112 (the FY26 value duplicated) against the correct 823 printed on p.16 of the same deck. (b) FY23 EBITDA margin printed as 8.81% on p.4 of the Q2FY26 and Q4FY26 decks against 8.05% on pp.17/19 of those same decks; correct value 8.05% (528/6,563). Error persisted three quarters, then FY23 was dropped from the chart.", anchor: "presentation__Investor_Presentation_2026-08-21_Q1FY27 pp.16-17; ..._2025-11-25_Q2FY26 pp.4, 17; ..._2026-06-01_Q4FY26 pp.4, 17, 19"}
  - {severity: "MAJOR", item: "Advertisement and sales promotion expense fell 30.8% (Rs 386L to Rs 267L) in a year revenue grew 26.6%, while the Aftermarket column identical in all five decks claims 'constant sales promotion efforts' to 'strengthen brand image'.", anchor: "annual-report__Annual_Report_2026 Note 37, extracted line 14745 (PDF p.220); all five decks p.7"}
  - {severity: "MAJOR", item: "The company reports a single audited segment, so every deck mix figure is unaudited. General purpose parts moved from 4% to 9% of revenue (approx Rs 338 Mn to Rs 962 Mn, ~2.8x) and 2W fell six points of mix, with no Operational Highlights bullet in any of five decks explaining it. The mix-shift margin narrative rests on splits that cannot be verified.", anchor: "results__Q1FY27_Board_Outcome_and_Results_2026-08-07 p.4 (segment note); decks pp.4-5 as dated"}
pipeline_flags_not_supported: []
pipeline_flags_reasoning_defects:
  - {flag: "B05 promise-delivery: EFI-ECU via BorgWarner graded MISSED / PIVOTED", severity: "MINOR", note: "Pivot fact SUPPORTED verbatim (AR2026 extracted lines 1294-1299). Verdict too harsh: the same AR records 'Secured business nominations from major OEMs for EFI ECU' (extracted lines 851-855, PDF p.16) and a separate 'Partnership with Athena, Italy for EFI' (line 827) that B05 does not mention. Downgrade to PARTIAL; the flag is route confusion across three partner names plus an in-house pivot, not a delivery miss."}
  - {flag: "B05 promise-delivery: customer concentration rebutted on 'up 21.1% in absolute rupees'", severity: "MINOR", note: "Conclusion correct, reasoning weak. Rupee concentration rises mechanically with revenue, and on the percentage basis the FY25-to-FY26 share FELL (73.82% to 70.65%), which superficially supports management. The valid contradiction is the FY24-to-FY26 arc, 67.33% to 70.65%, on the company's own preferred measure."}
promise_delivery_spot_checks: {checked: 6, confirmed: 6, wrong: 0}
credibility_grade_concur: "would grade lower: D not C. B05's C balances real execution evidence against narrative contradictions; that balance breaks once the two headline quality metrics an investor lifts from the deck (ROCE, EBITDA margin) are both shown to be undefined non-GAAP constructions differing from the company's own audited notes by 18 percentage points and by the direction of the margin trend."
findings:
  - {severity: "CRITICAL", location: "B05/B06 scope gap; deck ROCE vs AR2026 Note 51", description: "Deck ROCE 34.97% vs audited 17%, undisclosed definition, three-rung QUALITY LADDER implication. Not surfaced by B05 or B06."}
  - {severity: "CRITICAL", location: "B05/B06 scope gap; deck EBITDA vs Regulation 33 results filing", description: "FY26 margin expansion of 17bps is an artefact of FX gains netted into operating expenses; audited-basis margin was flat to down. Removes the quantitative support for the mix-shift thesis. Not surfaced by B05 or B06."}
  - {severity: "MAJOR", location: "AR2026 MD&A p.125 vs Note 51", description: "'Net Profit Margin 13.7%' is a pre-tax margin including a one-off; audited net profit ratio is 10.40%. 330bps overstatement inside one annual report."}
  - {severity: "MAJOR", location: "results filing 2026-08-07 vs Q1FY27 deck 2026-08-21", description: "CFO cessation omitted from the deck filed 14 days later; the filing itself calls the same event both a resignation and a designation change."}
  - {severity: "MAJOR", location: "five decks p.3 vs AR2026 MD&A and BRSR", description: "Three employee counts (1,605+ / 2,601 / 2,811); the deck figure is frozen across five quarters."}
  - {severity: "MAJOR", location: "AR2026 Note 43 vs deck technology narrative", description: "R&D flat and R&D capex down 41.7% while revenue grew 26.6%; intensity fell 75bps. The transition claim is not funded in the filed numbers."}
  - {severity: "MAJOR", location: "AR2026 Note 42", description: "Parent-company receivable stretched ~80 to ~108 days on +22% related-party sales; the aftermarket channel is the 70.32% shareholder."}
  - {severity: "MAJOR", location: "AR2026 BRSR + Note 34 + Note 42 + MD&A risk table", description: "91.7% of workers non-permanent; Rs 30.6 Cr apprentice stipend routed to a related party and off the employee-benefits line; labour-code risk named in one clause and never quantified while all three peers quantified it."}
  - {severity: "MAJOR", location: "Q1FY27 deck pp.13-17", description: "Every table labelled CONSOLIDATED after the company's own note says consolidation ceased; consolidated FY24-FY26 columns sit beside a standalone Q1FY27 column under one header."}
  - {severity: "MAJOR", location: "Q1FY27 deck p.17; Q2FY26 and Q4FY26 decks p.4", description: "Two uncorrected chart errors, one contradicting the same deck's own income statement page."}
  - {severity: "MAJOR", location: "AR2026 Note 37 vs deck p.7 boilerplate", description: "Advertising and sales promotion down 30.8% against a verbatim five-quarter claim of constant sales promotion and brand building."}
  - {severity: "MAJOR", location: "results filing segment note vs deck pp.4-5", description: "Single audited segment; deck mix splits unaudited; general purpose parts near-tripled to 9% of revenue with no narrative anywhere."}
  - {severity: "MAJOR", location: "B05 Section 2D, under-weighted", description: "Lucas TVS Level 3 stake at 32.2% of net worth, valued on a self-set 8x EV/EBITDA, is the whole of OCI; the Q1FY27 markdown of Rs 1,675L pre-tax is reported as a table row with no narrative while TCI fell 45.7%. B05 names the gap, not the mechanism."}
  - {severity: "MAJOR", location: "B05 Section 2A, reasoning basis", description: "Customer-concentration contradiction is cleaner on the percentage basis (67.33% FY24 to 70.65% FY26) than on the rupee basis B05 used, which is vulnerable to rebuttal."}
  - {severity: "MINOR", location: "AR2026 milestone timeline p.16", description: "A third EFI partner (Athena, Italy) exists alongside BorgWarner and the unnamed MoU; B05 reconciles two of four threads."}
  - {severity: "MINOR", location: "deck series p.14", description: "Leadership claim narrows from 'No. 1 in ignition systems' (Q1FY26) to 'No. 1 in Fly Wheel Magneto' (Q4FY26 onward); no source or share % in either form; no peer transcript references the category at all."}
  - {severity: "MINOR", location: "Q1FY26 deck vs AR2026 MD&A", description: "Aftermarket growth decelerated from 28% (Q1) to 20% (full year) with no comment and is never sized; peers disclose aftermarket at 8-10% of revenue with segment growth."}
  - {severity: "MINOR", location: "AR2026 Note 45", description: "Capital commitments up 618% (Rs 367L to Rs 2,635L) and disputed income tax up 44.1%, with no capex plan or project named in any deck."}
  - {severity: "MINOR", location: "Q4FY26 deck p.14 vs results filing Note 6", description: "Exceptional item is Rs 445L compensation plus Rs 1,076L interest (71% interest); the deck describes it only as land compensation."}
  - {severity: "MINOR", location: "deck series p.15", description: "Q1FY26 comparatives silently restated between decks (EBITDA 235 to 234, margin 10.46% to 10.41%, PAT 232 to 233, EPS 10.26 to 10.30) with no restatement note."}
  - {severity: "MINOR", location: "AR2026 MD&A p.124-125 vs results filing p.4", description: "Three FY26 revenue bases (audited Rs 1,06,848L; MD&A Gross Rs 1,06,440L; MD&A Net Rs 1,05,292L); the MD&A prose figure matches neither line of its own table."}
  - {severity: "MINOR", location: "AR2026 Note 51 vs MD&A vs deck p.19", description: "Three FY26 ROE figures (15% / 14.5% / 13.58%) with no basis stated on any."}
  - {severity: "MINOR", location: "deck p.16 vs AR2026 Note 44", description: "Deck EPS 49.14 is consolidated, AR Note 44 EPS 49.18 is standalone; neither cross-references the other. Basis trap for valuation."}
  - {severity: "MINOR", location: "AR2026 MD&A pp.121 and 124", description: "Two EV-penetration figures in one MD&A ('8.5% by end of 2025-26' and 'neared 10% of total sales by late 2025'); deck separately says 7%."}
  - {severity: "MINOR", location: "AR2026 Notes 34, 37, 42, 51", description: "Gratuity expense +291.8%, directors' commission +109.8%, Lucas TVS management fees risen to Rs 832L with no service description, Return on investment down to 13% from 14% on a book that is 50% of assets. None explained."}
critical_count: 2
major_count: 15
minor_count: 12
acceptance_rate: 29
acceptance_rate_note: "7 CAUGHT of 24 independent red-flag-grade items. The 12 MISSED items all come from one operation neither B05 nor B06 performed: reconciling deck and MD&A claims against the audited notes and the Regulation 33 results filing. B05's narrative-layer work and B06's peer-layer work are both sound and every one of their own flags survived my check (see pipeline_flags_not_supported: []). B01, B02, B03 and B07 are NOT in my inputs and B05 cites B02/B03 for note-level findings, so some MISSED items may be caught elsewhere in the pipeline. The orchestrator should check B01/B02/B03 before routing rework, and route it to whichever stage owns deck-versus-audited-statement reconciliation. The two CRITICAL items independently justify the trigger regardless of the rate."
not_assessable:
  - "Evasion, deflection, answer quality, tone under pressure, analyst insistence, and contradictions between answers to different analysts. No Q&A exists for the subject company in any period. The AGM Outcome filing (2026-07-30) records that queries were answered and discloses no content. Not manufactured from prepared text here, and correctly not manufactured by B05."
  - "CFO/PAT ratio, receivables ageing buckets, ECL adequacy, capex rupee totals: cash flow statement and ageing notes outside my source set. Owned by B01/B02/B03 and by Verifier A on the numbers."
  - "AR2025 MD&A prose year-on-year language comparison: that file's extraction is character-fragmented in the narrative region. AR2025 numeric notes extracted cleanly and were used."
  - "Q3FY26 deck: not in the provided source list. Four of five quarterly decks read in full."
```
