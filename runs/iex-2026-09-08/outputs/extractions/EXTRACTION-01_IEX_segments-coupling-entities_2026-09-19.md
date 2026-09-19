# EXTRACTION RESPONSE 1 — Segment revenue base, market coupling, entity map and share count
IEX | Indian Energy Exchange Ltd | run folder runs/iex-2026-09-08 | answered 2026-09-19
Corpus: branch run/iex-2026-09-08, corpus commit e6a917153d8657ebf0395371149e8a091c79f429 (inputs unchanged since)
Source text: page-marked extractions of the inputs/ PDFs (runs/iex-2026-09-08/work/*.txt, gitignored), plus inputs/shareholding/*.xml.

PAGE CONVENTION: every "p.N" is the "=== PAGE N ===" marker of the extracted file, i.e. the PDF page number.
It differs from the page number printed on the page (AR26 marker p.211 prints "207"). To verify, open the PDF at page N.

TIERS: [FILED] = annual report, results filing, exchange announcement, SEBI-filed prospectus, shareholding pattern.
[MGMT] = concall, presentation, press release, Reg 30 media release (Power Market Updates).
No web, no estimates, no reconciliation. Conflicts are reported side by side and marked CONFLICT.
Figures in Rs lakhs as printed unless the source prints another unit.

# IEX: P1 Part A extraction (segment volume, fee, revenue, market share, CERC fee disclosures)

Corpus-only. Source dir: `runs/iex-2026-09-08/work/` (page-marked text of filed PDFs). Page = the `=== PAGE n ===` marker in the text file, not the printed folio. The AR tables use tab separators; the quotes below replace tabs with single spaces and change nothing else. AR figures are Rs lakhs, as printed.

Tiers: [FILED] = AR, results filing. [MGMT] = concall, presentation, press release, and Power Market Update (PMU). Each PMU is a Reg 30 media release filed to BSE.

Short names:
- AR26 = `annual-report__Annual_Report_2026.txt` (FY26 AR, filed 14-Aug-2026)
- AR25 = `annual-report__Annual_Report_2025.txt` (FY25 AR, carries FY24 comparatives)
- RES-FY26 = `results__FY26_Q4_Audited_Results_2026-04-23.txt`
- RES-Q1 = `results__Q1FY27_Results_Unaudited_2026-07-23.txt`
- PR-FY26 = `announcements__FY26_Q4_Press_Release_2026-04-23.txt`
- PR-Q1 = `results__Q1FY27_Press_Release_2026-07-23.txt`
- PMU-FY26 = `announcements__Power_Market_Update_FY26_Q4FY26_Mar2026.txt` (dated 06-Apr-2026)
- PMU-Q1 = `announcements__Power_Market_Update_Q1FY27_Jun2026.txt` (dated 03-Jul-2026)
- PMU-Jul = `announcements__Power_Market_Update_Jul2026.txt` (dated 04-Aug-2026)
- PMU-Aug = `announcements__Power_Market_Update_Aug2026.txt` (dated 03-Sep-2026)
- PRES-Q4 = `presentation__Investor_Presentation_Q4FY26_2026-04-23.txt`
- PRES-AM = `presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt`
- CC-Nov = `other__Concall_Nov_2025_Q2FY26_Transcript.txt` (call 31-Oct-2025, transcript dated 07-Nov-2025)
- CC-Feb = `concalls__Concall_Feb_2026_Transcript.txt` (call 30-Jan-2026, transcript dated 05-Feb-2026)
- CC-Apr = `concalls__Concall_Apr_2026_Transcript.txt` (call 24-Apr-2026, transcript dated 30-Apr-2026)
- CC-Jul = `concalls__Concall_Jul_2026_Transcript.txt` (Analyst Meet 24-Jul-2026, transcript dated 31-Jul-2026)

---

## A1. Volume traded, by segment

### A1.1 Total electricity

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 102 BU | AR25 p.61 | "the increase was due to growth in electricity traded volume by 18.7% from 102 BU in FY24 to 121 BU in FY25" | [FILED] | Only filed FY24 total found. |
| FY25 | 121 BU | AR25 p.61 | same sentence as above | [FILED] | |
| FY25 | 121 BU | AR26 p.48 | "a 17% year-on-year increase over nearly 121 BUs traded in FY'25" | [FILED] | Consistent. |
| FY26 | 141 BU | AR26 p.48 | "In FY'26, IEX achieved its highest-ever electricity traded volume of 141 BU, a 17% year-on-year increase" | [FILED] | |
| FY26 | 141 BU | AR26 p.64 | "growth in electricity traded volume by 16.90 % from 121 BU in FY'25 to 141 BU in FY'26" | [FILED] | Growth printed as 16.90% here and as 17% on p.48. |
| FY26 | 141.1 BU | PR-FY26 p.2 | "Highest ever traded electricity volume of 141.1 BUs in FY'26, increase of 17% YoY." | [MGMT] | |
| FY26 | 141.1 BU; FY25 121 BU | PRES-Q4 p.7 | "Electricity Volume: FY26: 141.1 BU (+17.0%);FY25:121 BU (+18.7%)" | [MGMT] | |
| Q1FY27 | 37,534 MU | PMU-Q1 p.2 | "achieved electricity traded volume of 37,534 MU, marking a 15.9% year on year increase" | [MGMT] Reg 30 media release | |
| Q1FY27 | 37.5 BU | PR-Q1 p.2 | "Electricity volumes in Q1FY'27 at 37.5 BUs, increased 15.9% YoY." | [MGMT] | |

### A1.2 DAM (incl. HP-DAM)

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 53.3 BU | AR25 p.47 | "In FY'25, a total of 61.3 Billion Units (BU) were traded in the Day-Ahead Market (DAM), marking an increase of 15% compared with 53.3 BU traded in FY'24." | [FILED] | The AR25 sentence does not say "incl. HP-DAM". |
| FY25 | 61.3 BU | AR25 p.47 | same sentence | [FILED] | |
| FY25 | 61.31 BU | PMU-FY26 p.3 | "The Day-Ahead Market (DAM) including HPDAM, achieved 62.78 BU for FY'26, as compared to 61.31 BU in FY'25, registering an increase of 2.4% on YoY basis." | [MGMT] Reg 30 media release | |
| FY26 | 62.78 BU | PMU-FY26 p.3 | same sentence | [MGMT] Reg 30 media release | |
| FY26 | 62.8 BU | AR26 p.48 | "In FY'26, a total of 62.8 billion Units (BU) were traded in the Day-Ahead Market (DAM, including HP-DAM), an increase of 2.4% over FY'25." | [FILED] | |
| Q1FY27 | 13,344 MU (Q1FY26: 12,399 MU) | PMU-Q1 p.3 | "The Day-Ahead Market (DAM) including HPDAM achieved 13,344 MU volume in Q1 FY '27 as compared to 12,399 MU volume in Q1 FY '26, increase of 7.6% YoY." | [MGMT] Reg 30 media release | |
| HP-DAM alone, any period | NOT DISCLOSED | see closing list | | | Every source reports DAM "including HPDAM". |

### A1.3 RTM

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 30.1 BU | PRES-AM p.12 | Chart row "24.2 30.1 38.9 54.9 13.0 16.0" under axis "FY23 FY24 FY25 FY26 Q1 FY26 Q1 FY27", label "RTM Volume (BUs)" | [MGMT] | No filed FY24 RTM figure. AR25 p.47 gives only the growth: "trading nearly 39 Billion Units (BU), an increase in volume of 29% on year-on-year basis". |
| FY25 | nearly 39 BU | AR25 p.47 | "The Real-Time-Market (RTM) exhibited a strong positive trend in FY'25, trading nearly 39 Billion Units (BU), an increase in volume of 29% on year-on-year basis." | [FILED] | |
| FY25 | 38.90 BU | PMU-FY26 p.3 | "The Real-Time Electricity Market (RTM) achieved 54.85 BU for FY'26, as compared to 38.90 BU in FY'25, registering an increase of 41% on YoY basis." | [MGMT] Reg 30 media release | |
| FY26 | 54.85 BU | PMU-FY26 p.3 | same sentence | [MGMT] Reg 30 media release | |
| FY26 | 54.9 BU | AR26 p.48 | "The Real-Time Market (RTM) was the standout performer in FY'26, trading 54.9 BUs, a 41% year-on-year increase" | [FILED] | |
| Q1FY27 | 16,019 MU (Q1FY26: 12,975 MU) | PMU-Q1 p.3 | "The Real-Time Electricity Market (RTM) volume increased to 16,019 MU in Q1 FY '27 as compared to 12,975 MU in Q1 FY '26, increase of 23.5% YoY." | [MGMT] Reg 30 media release | |

### A1.4 TAM (incl. DAC / contingency / HP-TAM / long-duration contracts up to 90 days)

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 15 BU | AR25 p.47 | "The TAM segment including Day-Ahead-Contingency (DAC) witnessed a decline of 21% in overall volume to 11.8 Billion Units (BU) in FY'25 compared with 15 Billion Units (BU) in FY'24" | [FILED] | |
| FY25 | 11.8 BU | AR25 p.47 | same sentence | [FILED] | |
| FY25 | 11.77 BU | PMU-FY26 p.3 | "Day Ahead Contingency and Term-Ahead Market (TAM), comprising of HPTAM, contingency, daily & weekly and monthly contracts up to 3 months, traded 12.72 BU in FY'26, as compared to 11.77 BU in FY'25, registering an increase of 8.0% on YoY basis." | [MGMT] Reg 30 media release | |
| FY26 | 12.72 BU | PMU-FY26 p.3 | same sentence | [MGMT] Reg 30 media release | |
| FY26 | 12.7 BU | AR26 p.48 | "The Day-Ahead Contingency and Term-Ahead Market (TAM), comprising HP-TAM, contingency, daily, weekly, and monthly contracts up to 3 months, traded 12.7 BUs in FY'26, an increase of 8.0% year-on-year." | [FILED] | |
| Q1FY27 | 5,344 MU (Q1FY26: 4,348 MU) | PMU-Q1 p.3 | "Day Ahead Contingencyand Term-Ahead Market (TAM), comprising of HPTAM, contingency, daily & weekly and monthly contracts up to 3 months, traded 5,344 MU in Q1 FY '27 as compared to 4,348 MU in Q1 FY '26, increase of 22.9% YoY." | [MGMT] Reg 30 media release | |
| Sub-splits (DAC, HP-TAM, LDC separately) | NOT DISCLOSED | see closing list | | | Every source reports TAM as one aggregate. PRES-Q4 p.8 splits the FY26 mix into "TAM 6%" and "DAC 2%" as percentages only, with no volumes. |

### A1.5 Green market (G-DAM + G-TAM)

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 3.2 BU | AR25 p.47 | "The total volume traded in this market was 8.7 Billion Units (BU), compared with 3.2 BUs in FY'24." | [FILED] | |
| FY25 | 8.7 BU | AR25 p.47 | same sentence | [FILED] | |
| FY25 | 8.75 BU | PMU-FY26 p.4 | "IEX Green Market, comprising the Green Day-Ahead and Green Term-Ahead Market segments, achieved 10.78 BU, as compared to 8.75 BU in FY'25 an increase of 23% on YoY basis." | [MGMT] Reg 30 media release | |
| FY26 | 10.78 BU | PMU-FY26 p.4 | same sentence | [MGMT] Reg 30 media release | |
| FY26 | 10.8 BU | AR26 p.48 | "The Green Market, comprising the Green Day-Ahead Market (G-DAM) and the Green Term-Ahead Market (G-TAM), achieved 10.8 BUs of volumes in FY'26, an increase of 23% on a year-on-year basis." | [FILED] | |
| Q1FY27 | 2,827 MU | PMU-Q1 p.3 | "IEX Green Market, comprising the Green Day-Ahead and Green Term-Ahead Market segments, during Q1FY'27, achieved volume of 2,827 MU, an increase of 6.3% over Q1FY'26." | [MGMT] Reg 30 media release | The Q1FY26 base volume is not printed. |
| G-DAM vs G-TAM split, any period | NOT DISCLOSED | see closing list | | | |

### A1.6 AR26 segment summary table (FY25 vs FY26, rounded)

AR26 p.48 [FILED], table "IEX Electricity Volume Summary — FY'25 vs FY'26":
- "Day-Ahead Market (DAM, incl. HPDAM) 61 63 +2%"
- "Real-Time Market (RTM) 39 55 +41%"
- "Term-Ahead Market (TAM, incl. DAC) 12 13 +8%"
- "Green Market (G-DAM + G-TAM) 9 11 +23%"
- "Total Electricity Traded 121 141 +17%"
- Footnote: "Source: IEX. Note: Total may not match sum of segments due to rounding and adjustments."

Comment: these are rounded versions of the PMU-FY26 figures.

### A1.7 REC (certificates, lakh)

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | 75 lakh RECs | AR25 p.48 | "with 1.78 crore RECs traded in FY'25, representing nearly 17.8 BUs of electricity, compared to 75 lakh RECs traded in FY'24, equivalent to 7.5 BUs." | [FILED] | **CONFLICT** with the next row. |
| FY24 | 84 lakh certificates | AR25 p.61 | "and in certificate traded volume by 113% from 84 Lakh in FY24 to 179 Lakh in FY25" | [FILED] | "Certificate" volume here. The AR does not say whether it includes ESCerts. Not reconciled. |
| FY25 | 1.78 crore RECs | AR25 p.48 | see FY24 row | [FILED] | **CONFLICT** with the next row (178 vs 179 lakh). |
| FY25 | 179 lakh certificates | AR25 p.61 | see above | [FILED] | |
| FY25 | 178 lakh | PRES-Q4 p.7 | "Renewable Energy Certificates: FY'26: 187 Lakh (+5.0%); FY'25: 178 Lakh (+136%)" | [MGMT] | |
| FY26 | 187.20 lakh | AR26 p.49 | "Trading volumes of RECs remained strong in FY'26 with a total of 187.20 lakh (18.72 million) RECs traded, representing nearly 18.72 BUs of electricity, higher by 5% on a year-on-year basis." | [FILED] | |
| FY26 | 187.20 lakh | PMU-FY26 p.4 | "187.20 lac RECs were traded during FY'26. REC traded volume in FY'26 increased by 5% on YoY basis." | [MGMT] Reg 30 media release | |
| Q4FY26 | 71.70 lakh | PMU-FY26 p.4 | "71.70 lakh RECs were traded during Q4FY'26." | [MGMT] Reg 30 media release | **CONFLICT** with the next two rows. |
| Q4FY26 | 71.71 lakh | AR26 p.49 | "the last quarter ended very strong and saw 71.71 lakh RECs being traded." | [FILED] | |
| Q4 (labelled FY'25) | 71.71 lakh | PR-FY26 p.2 | "71.71 lac RECs traded during Q4FY'25, increase of 6.1%." | [MGMT] | The heading of this bullet group is "Q4FY'26". The quarter label inside the bullet reads Q4FY'25 as printed. |
| Q1FY27 | 9.77 lakh | PMU-Q1 p.3 | "A total of 9.77 lakh RECs were traded during Q1 FY'27, decline of 81.4% YoY." | [MGMT] Reg 30 media release | The Q1FY26 base is not printed. |

Post-quarter REC monthly data (context, [MGMT] Reg 30 media release): PMU-Jul p.2 "A total of 7.11 lakh RECs were traded in July '26, down 56.3% YoY." PMU-Aug p.2 "A total of 2.91 lakh RECs were traded in August '26, down 86.6% YoY due to lower participation."

### A1.8 ESCerts

| Period | Figure | Source, page | Verbatim | Tier | Comment |
|---|---|---|---|---|---|
| FY24 | NOT DISCLOSED | see closing list | | | |
| FY25 | 69,935 ESCerts | AR25 p.48 | "In FY'25, IEX traded a total of 69,935 ESCerts." | [FILED] | This is the only ESCert volume in the corpus. |
| FY26 | NOT DISCLOSED | AR26 p.49 | The ESCert section says only: "In FY'26, ESCerts were at a major juncture as India prepares to transition the high greenhouse gas-intensive sectors from the Perform, Achieve and Trade (PAT) scheme into the new Carbon Credit Trading Scheme (CCTS)." | [FILED] | No volume given. |
| Q1FY27 | NOT DISCLOSED | see closing list | | | |

### A1.9 Other segments (I-DAM integrated, HP-TAM alone, ancillary DAM-AS / RTM-AS, cross-border, intraday)

NOT DISCLOSED as separate volumes for any period. AR26 p.7 [FILED] lists these as market segments ("Ancillary Services (DAM-AS) since Jun'23", "Ancillary Services (RTM-AS) since Jun'23", "HP-DAM since Mar '23 • Segment within I-DAM on Day-Ahead basis", "High Price Term-Ahead Contracts since Oct'23") but prints no volumes. The one related figure is a ratio, not a volume. AR26 p.62 [FILED]: "Nearly 72% of the cleared volume in I-DAM are contributed by members using APIs."

### A1.10 Segment mix percentages (as printed; different bases, flagged)

| Source, page | Verbatim | Tier | Comment |
|---|---|---|---|
| AR26 p.48 | "DAM accounted for approximately 44% of total electricity volumes on IEX." | [FILED] | **CONFLICT** with AR26 p.62 in the next row: 44% vs 39% for the same FY26 DAM share. |
| AR26 p.62 | "Mitigation: The Day-Ahead Market (DAM) contributed 39% of IEX's total traded volumes in FY'26, compared with 44% in FY'25 and nearly 95% in FY'15" | [FILED] | |
| AR25 p.59 | "Mitigation: As of FY'25, the Day Ahead Market comprised 44% of total volumes of IEX." | [FILED] | |
| AR26 p.48 | RTM "accounting for approximately 39% of total electricity volumes traded on IEX"; TAM "accounted for approximately 9% of total electricity volumes"; Green "accounted for nearly 8% of total electricity traded on IEX" | [FILED] | **CONFLICT** with PRES-AM p.12 for RTM: 39% vs 34%. |
| PRES-Q4 p.8 | "DAM 39% RTM 34% TAM 6% DAC 2% Green 7% Certificates 12% FY'26 - Electricity Volumes: 141 BUs; Certificates: 187 Lakh" | [MGMT] | This mix includes certificates in the base. |
| PRES-AM p.12 | "RTM has Made Substantial Strides, Grew 41% YoY in FY'26 (~55 BU), Now 34% of Electricity Volumes"; pie "DAM 39% RTM 34% TAM 8% Green 7% Certificates 12% FY'26" | [MGMT] | The headline says "of Electricity Volumes" but the pie includes certificates. Not reconciled. |

---

## A2. Transaction fee per unit, per side, per segment

**No fee schedule is printed anywhere in the corpus.** No per-side rate, per-segment rate or per-member-category rate appears in either AR, either results filing, any PMU, either presentation or any concall. Pointer: the exchange's CERC-approved fee schedule (IEX Business Rules / fee circulars) would carry it, and none of these is in the corpus. The places a filed copy would sit are AR26 Note 28 (p.211) and the AR26 MD&A Business Review (pp.48-49). Neither carries a rate.

### A2.1 Filed description of how the fee is charged (no rate)

- AR26 p.190, Note 3.7.1 accounting policy [FILED]: "Transaction fee is charged based on the volume of transactions entered into by the respective member or client of trader/ professional member through the exchange. Fee charged in relation to transactions under the Day Ahead Market, Green Day Ahead Market, High Price- Day Ahead Market and the Renewable Energy Certificate segment, is accrued when the orders placed on the network are matched and confirmed by National Load Dispatch Centre."
  Comment: basis is volume; no rate.
- AR26 p.190 [FILED]: "The Company accounts for volume discounts and pricing incentives to customers by reducing the amount of revenue recognised at the time of services rendered. Revenues are shown net of goods and service tax and applicable discounts and allowances."
  Comment: confirms that volume discounts and incentives exist. Their size is in A4 (the "Reduction towards incentives/ discounts" line).
- AR26 p.172, Independent Auditor's Report, Key Audit Matter [FILED]: "The revenue earned by the Company in the form of transaction fee in respect of electricity traded on the exchange and related services is governed as per the terms and conditions/ rules framed by CERC."
  Comment: the auditor names CERC rules as the fee authority. The same wording appears in AR25 p.163.

### A2.2 Management verbal statements (all [MGMT])

| Source, page | Verbatim | Comment |
|---|---|---|
| CC-Feb p.10 (Satyanarayan Goel) | "No, in case of REC, the transaction fee is reduced to Rs. 20, in fact, for part of the year. This year for the full year, it is Rs. 20. And even out of that, also looking at the market conditions, we have to give incentives to the buyers and sellers , some amount of incentive. But otherwise, in case of electricity, I think it is around four paisa." | Electricity about 4 paise, and the speaker hedges ("I think"). REC Rs 20 per certificate. Neither statement says per side or both sides. |
| CC-Nov p.17 (Vineet Harlalka, CFO) | "if you can recall, last year in the month of August, we reduced our trans action fee on the certificate from Rs. 40 to Rs. 20. So, during the previous year quarter, the full Rs. 40 fees was being charged. And this quarter, it was Rs. 20." | Certificate fee cut from Rs 40 to Rs 20. The call was on 31-Oct-2025, so "last year" is as spoken. Per side not stated. |
| CC-Apr p.15 (Satyanarayan Goel) | "Against INR 0.04 (four paise), I think the margin is around (3.6 or 3.7 paisa) INR 0.036, INR 0.037. That's the kind of number. So we don't expect significant impact on the margin part of it, the transaction fees part." | This is said about the Term Ahead Market. It implies an effective TAM realisation of 3.6 to 3.7 paise against a 4 paise headline. Per side not stated. |
| CC-Feb p.10 (Satyanarayan Goel) | "Revenue also includes annual fees by the members." | Reply to an analyst's revenue-per-unit ratio. |
| CC-Jul p.42 (Satyanarayan Goel) | "I think there are fuel markets like in RECs and the Term Ahead Market, we give some incentive. Because Term Ahead contracts are for longer duration, some incentives are given in that." | REC and TAM carry incentives. No rate given. |
| CC-Jul p.41 (analyst, not management) | "if we take total volumes and divide it by the revenue on standalone basis the realization comes at around 0.4 Paisa per unit. Whereas, last quarter and year, Q1 FY26, it was around 3.7 Paisa per unit." | Analyst's own arithmetic, quoted for context only. Management did not confirm the number. Not a disclosure. |
| CC-Feb p.12 (analyst, citing news) | "there was this news article that mentioned that the tariffs like the exchange fees might be cut from four paise to whatever half of it on each side. What is your idea on that?" | This is the only "each side" wording in the corpus, and it comes from the analyst, not management. Management reply is in A6. |

Per side vs both sides: NOT DISCLOSED. No management statement or filed document says whether "four paise" is charged per side or in total.

Fee by member category (e.g. discoms vs OA vs traders): NOT DISCLOSED.

---

## A3. Transaction fee revenue by segment

**Only a two-way split is disclosed: Electricity vs Certificates.** No DAM / RTM / TAM / Green / REC / ESCert split exists in any filed or management document in the corpus.

| Period | Electricity | Certificates | Total transaction fees | Source, page | Tier |
|---|---|---|---|---|---|
| FY24 | 40,421.25 | 2,469.32 | 42,890.57 | AR25 p.203 (standalone Note 28); same figures AR25 p.263 (consolidated Note 27) | [FILED] |
| FY25 | 47,833.81 | 3,520.71 | 51,354.52 | AR25 p.203 / p.263; restated as comparative in AR26 p.211 / p.272-273 | [FILED] |
| FY26 | 55,851.37 | 2,545.07 | 58,396.44 | AR26 p.211 (standalone Note 28); AR26 p.273 (consolidated Note 27 disaggregation) | [FILED] |
| Q1FY27 | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | see closing list | |

Verbatim rows:
- AR26 p.211 standalone Note 28: "Electricity (comprising RTM, DAM, TAM, Green Segments) 55,851.37 47,833.81" / "Certificates (comprising REC, Escerts Segments) 2,545.07 3,520.71" / "Total 58,396.44 51,354.52"
- AR26 p.273 consolidated: identical three rows, introduced by "revenue from contract with customer with respect to transaction fee is disaggregated by the Group on the basis of nature of the product".
- AR25 p.203 standalone Note 28: "Electricity (comprising RTM, DAM, TAM, Green) 47,833.81 40,421.25" / "Certificates (comprising REC, Escerts) 3,520.71 2,469.32" / "Total 51,354.52 42,890.57"
- AR25 p.263 consolidated Note 27: the same three rows.

Comment: standalone and consolidated transaction fees are identical in all three years. Subsidiary revenue enters only through other lines (see A4).

Management directional statement, Q2FY26 (CC-Nov p.17, Satyanarayan Goel) [MGMT]: "On the electricity side, the increase in the revenue is 16%. On the certificate side, the increase in revenue is minus 53%. So, as a result of that, total revenue increase was only 10%." Comment: YoY growth only, no rupee figures.

---

## A4. Revenue split

### A4.1 Standalone, annual (Rs lakhs) [FILED]

| Line (as printed) | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Transaction fees | 42,890.57 | 51,354.52 | 58,396.44 | FY24/FY25: AR25 p.202-203 Note 28; FY26/FY25: AR26 p.211 Note 28 |
| Annual subscription fees | 1,939.29 | 2,064.90 | 2,282.34 | same |
| Membership, processing and transfer fees | 53.02 | 71.81 | 116.04 | same |
| Sub-total, sale of services | 44,882.88 | 53,491.23 | 60,794.82 | same |
| Amortisation of deferred settlement guarantee fund (other operating revenue) | 32.44 | 45.78 | 43.75 | same |
| Revenue from operations, total | 44,915.32 | 53,537.01 | 60,838.57 | same |
| Other income (Note 29) | 10,162.84 | 11,892.43 | 13,655.11 | AR25 p.203; AR26 p.211 |

Verbatim anchors:
- AR26 p.211: "Transaction fees * 58,396.44 51,354.52" / "Annual subscription fees 2,282.34 2,064.90" / "Membership, processing and transfer fees 116.04 71.81" / "60,794.82 53,491.23" / "Amortisation of deferred settlement guarantee fund 43.75 45.78" / "Total 60,838.57 53,537.01"
- AR25 p.202: "Transaction fees * 51,354.52 42,890.57" / "Annual subscription fees 2,064.90 1,939.29" / "Membership, processing and transfer fees 71.81 53.02" / "53,491.23 44,882.88" / "Amortisation of deferred settlement guarantee fund 45.78 32.44" / "Total 53,537.01 44,915.32"
- Other income totals: AR26 p.211 Note 29 "Total 13,655.11 11,892.43"; AR25 p.203 Note 29 "Total 11,892.43 10,162.84".

"Admission fee" as a separate revenue line: NOT DISCLOSED. The notes carry no "admission fee" revenue line. The accounting policy maps admission to "Membership fees". AR26 p.190: "Membership fees charged from a member of the exchange at the time of admission to the exchange is recognised on a pro-rata basis over the estimated period of time over which the services are expected to be provided." The MD&A lists admission fees as a revenue source (AR26 p.64: "The Company derives its revenues from transaction fees, annual subscription fees, admission fees, interest income, gains on sale of investments and other miscellaneous income."). No amount is attached.

Deferred subscription and admission fee income, standalone [FILED]:
- AR26 p.210 Note 25(a): "Invoices raised during the year 2,468.69 2,451.68" (FY26, FY25); "Balance as at the end of the year 1,336.51 1,373.03"
- AR25 p.202 Note 25(a): "Invoices raised during the year 2,451.68 2,167.89" (FY25, FY24); "Balance as at the end of the year 1,373.03 1,125.82"
- Comment: billings for subscription plus admission, before deferral. Not a revenue line.

### A4.2 Consolidated, annual (Rs lakhs) [FILED]

| Line (as printed) | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Transaction fees | 42,890.57 | 51,354.52 | 58,396.44 | AR25 p.263 Note 27; AR26 p.272 Note 27 |
| Annual subscription fees | 1,939.29 | 2,064.90 | 2,282.34 | same |
| Membership, processing and transfer fees | 53.02 | 142.06 | 467.04 | same |
| I-REC Issuance support fees | "-" | 118.97 | 375.13 | same |
| Sub-total, sale of services | 44,882.88 | 53,680.45 | 61,520.95 | same |
| Amortisation of deferred settlement guarantee fund | 32.44 | 45.78 | 43.75 | same |
| Revenue from operations, total | 44,915.32 | 53,726.23 | 61,564.70 | same |
| Other income (Note 28) | 10,169.52 | 12,010.46 | 13,130.47 | AR25 p.263; AR26 p.273 |

Verbatim anchors:
- AR26 p.272: "Membership, processing and transfer fees 467.04 142.06" / "I-REC Issuance support fees 375.13 118.97" / "61,520.95 53,680.45" / "Total 61,564.70 53,726.23"
- AR25 p.263: "Membership, processing and transfer fees 142.06 53.02" / "I-REC Issuance support fees 118.97 -" / "53,680.45 44,882.88" / "Total 53,726.23 44,915.32"
- Other income: AR26 p.273 "Total 13,130.47 12,010.46"; AR25 p.263 "Total 12,010.46 10,169.52".

Comment: consolidated other income for FY26 (13,130.47) is lower than standalone (13,655.11). The standalone figure includes "Dividend income 536.55" (AR26 p.211). The consolidated figure shows "Dividend income 4.65" (AR26 p.273).

### A4.3 Reduction towards incentives / discounts reconciliation [FILED]

| Line | FY24 | FY25 | FY26 | Source |
|---|---|---|---|---|
| Standalone contracted price | 45,986.86 | 54,860.91 | 62,441.13 | AR25 p.203; AR26 p.211 |
| Standalone reduction towards incentives/ discounts | (1,071.54) | (1,323.90) | (1,602.56) | same |
| Standalone revenue recognised | 44,915.32 | 53,537.01 | 60,838.57 | same |
| Consolidated contracted price | 45,986.86 | 55,050.13 | 63,167.26 | AR25 p.263; AR26 p.273 |
| Consolidated reduction towards incentives/ discounts | (1,071.54) | (1,323.90) | (1,602.56) | same |
| Consolidated revenue recognised | 44,915.32 | 53,726.23 | 61,564.70 | same |

Verbatim: AR26 p.211 "Contracted price 62,441.13 54,860.91" / "Reduction towards incentives/ discounts (1,602.56) (1,323.90)" / "Revenue recognised 60,838.57 53,537.01". AR25 p.203 "Contracted price 54,860.91 45,986.86" / "Reduction towards incentives/ discounts (1,323.90) (1,071.54)".

Segment split of the incentive reduction: NOT DISCLOSED. The notes give only the total. Management names REC and TAM as the segments that receive incentives (CC-Feb p.10, CC-Jul p.42, quoted in A2.2).

Single-customer concentration, same note [FILED]: AR26 p.211 "Revenue amounting to `9,862.24 (31 March 2025: `8,379.07) which is more than 10% of total revenue is attributable to single customer." AR25 p.203 gives FY24 as "7,408.55".

### A4.4 Quarterly: Q1FY27 (and the Q1FY26 comparative) [FILED]

| Line | Standalone Q1FY27 | Standalone Q1FY26 | Consolidated Q1FY27 | Consolidated Q1FY26 | Source |
|---|---|---|---|---|---|
| Revenue from operations | 15,592.97 | 13,998.81 | 15,787.67 | 14,175.14 | RES-Q1 p.4 (standalone), p.9 (consolidated) |
| Other income | 4,491.58 | 4,252.37 | 4,493.27 | 4,242.81 | same |
| Total income | 20,084.55 | 18,251.18 | 20,280.94 | 18,417.95 | same |

Verbatim: RES-Q1 p.4 "1 Revenue from operations 15,592.97 17,224.89 13,998.81 60,838.57" / "2 Other income 4,491.58 2,211.41 4,252.37 13,655.11". RES-Q1 p.9 "1 Revenue from operations 15,787.67 17,430.27 14,175.14 61,564.70" / "2 Other income 4,493 27 2,213.66 4,242_81 13,130.47". The OCR artefacts are as printed and read as 4,493.27 and 4,242.81.

Q1FY27 split of revenue from operations into transaction fees, subscription, membership and incentives: NOT DISCLOSED. The results filing prints only the face P&L. Segment note (RES-Q1 p.5): "The Company is a registered power exchange and the same constitutes a single operating segment. Therefore, there are no other reportable segments in terms of the requirements of Ind AS 108".

### A4.5 Q4FY26 quarter (context, from the FY26 results filing) [FILED]

RES-FY26 p.6 standalone: "1 Revenue from operations 17,224,89 14,390,45 14,125.69 60,838.57 53,537.01" / "2 Other income 2,211,41 3,742.01 3,098.43 13.655.11 11,892.43". Columns are Q4FY26, Q3FY26, Q4FY25, FY26, FY25. RES-FY26 p.15 consolidated: "1 Revenue from operations 17,430 27 14,566 80 14,224 82 61,564 70 53,726 23" / "2 Other income 2,213.66 3,739 68 3,234.66 13,130 47 12.010 46". The OCR separators are as printed.

### A4.6 Management percentage split [MGMT]

PRES-Q4 p.26, "Breakup of standalone revenues (%) Q4FY25 Q3FY26 Q4FY26 FY26":
- "Transaction Fees 78.7% 76.0% 85.4% 78.4%"
- "Admission and Annual Fees 3.2% 3.3% 3.2% 3.3%"
- "Other Income 18.1% 20.7% 11.4% 18.3%"

Comment: the base is total income, which includes other income. This split is not available for Q1FY27; PRES-AM carries no equivalent slide.

PRES-AM p.38, "Operating Revenue (INR Cr)": "401 449 535 608 140 156" for "FY23 FY24 FY25 FY26 Q1FY26 Q1FY27". "Total Income (INR Cr)": "474 551 654 745 183 201". Comment: the slide does not label these figures standalone or consolidated. It labels only the PAT panel "Consolidated". Not assigned here.

### A4.7 "Revenue" label conflict in press releases (flag)

- PR-FY26 p.2 [MGMT]: "Standalone Revenue at INR 744.9 crore in FY'26" and "Consolidated Revenue at INR 747.0 crore in FY'26".
- RES-FY26 p.6 / p.15 [FILED]: standalone "Total income (1+2) ... 74,493.68" and "Revenue from operations ... 60,838.57"; consolidated "Total income (1+2) ... 74,695.17" and "Revenue from operations 61,564 70".
- PR-Q1 p.2 [MGMT]: "Consolidated Revenue in Q1FY'27 at Rs 202.8 Crore, increased 10.1% from Rs 184.2 Crore in Q1FY'26."
- RES-Q1 p.9 [FILED]: "Total income (1+2) 20,280.94 ... 18,417.95"; "Revenue from operations 15,787.67 ... 14,175.14".
- **CONFLICT (label):** the press releases call "Revenue" a figure that sits on the "Total income" line of the filed results, not on the "Revenue from operations" line. Not reconciled here. AR26 p.64 [FILED] also uses "Total Revenue 74,493.68" alongside "Revenue from operation 60,838.57" and "Treasury Income 13,655.11".

---

## A5. IEX market share of exchange-traded electricity

### A5.1 Filed documents

IEX's own share of exchange-traded electricity: NOT DISCLOSED in either AR for FY24, FY25 or FY26. The filed documents give only the share of all power exchanges in the short-term market, sourced to CERC:
- AR26 p.47 [FILED]: "According to the Central Electricity Regulatory Commission (CERC), India's short-term power market volumes stood at approximately 302 BU in FY'26 compared with 238 BU in FY'25." and "Within the short-term market, power exchanges remained the dominant segment, facilitating 60% of short-term transactions, while bilateral transactions, including trades through energy traders and direct agreements between distribution companies contributed 26% to the market share. The Deviation Settlement Mechanism (DSM) accounted for 13%."
  Comment: denominator source stated as CERC. The share is for all exchanges, not IEX. The AR does not name the specific CERC report.
- AR25 p.46 [FILED]: "According to the Central Electricity Regulatory Commission (CERC), India's short-term power market witnessed significant growth, expanding to 238 BU in FY'25 from 218 BU in FY'24." and the same "60% ... 26% ... 13%" sentence.
  Comment: AR25 and AR26 print the same 60/26/13 shares for FY25 and FY26.
- AR25 p.60 and AR26 p.63, Market Risk [FILED]: "The Company's revenues could be adversely affected if its market share does not grow year-on-year". No number is given.

### A5.2 Management statements [MGMT]. No denominator source is stated in any of them.

| Period | Share | Source, page | Verbatim | Comment |
|---|---|---|---|---|
| Q2FY26 | Electricity 84%; certificates "a little above 50%"; overall about 75%; IDAM and RTM 99%; TAM 35% | CC-Nov p.18 (Rohit Bajaj) | "If I talk about Q2, so our electricity market share is 84% and certificate market share is a little above 50%. So overall is about 75%. But what we have seen in the past couple of years, product-wise, IDM and RTM is 100%, 99% precisely. And in the other TAM segments, it is 35%. Overall, as I said, electricity is 84%." | Denominator not stated. The segment shares are described as a "past couple of years" pattern. |
| 9MFY26 | Electricity 83%; REC about 50%; TAM 45-50%, "generally below 50%" | CC-Feb p.16 (Rohit Bajaj) | "So, electricity overall, we are around 83% in first nine months. And REC is about 50%. I do not have exact number for REC available right away, but electricity is 83% for sure." and "TAM, it varies between 45%, 50%. You have that? So, TAM is generally below 50%, but overall electricity is 83%." | The analyst suggested "Assume 99% for RTM and DAM". Management did not confirm that figure; it replied "83% number will help you arriving at the final." |
| Multi-year (no period) | 80-85% | CC-Jul p.7 (speaker introducing slides) | "Leading energy exchange for all these years , we have always been maintaining 80 -85% market share." | No period and no denominator. |
| TAM (no period) | "40%, 50%, 30%, 20%" across exchanges | CC-Apr p.15 (Satyanarayan Goel) | "in case of the Term Ahead Market, where the liquidity is practically uniform across all 3 exchanges, the share of all 3 exchanges is in that same range of, 40%, 50%, 30%, 20% kind of numbers." | Does not state IEX's own TAM share. |
| FY24, FY25, FY26 full year, IEX share | NOT DISCLOSED | see closing list | | |

Related, not market share of exchanges [MGMT]:
- CC-Jul p.7: "Last year we did 141 billion unit s (electricity) trade which is a little over 8% of the (country's) total consumption." Comment: this is IEX volume over national consumption, not a share of exchange trade.
- PRES-AM p.24: "Order issued in July 2025, violated process prescribed by PMR 2021 and only sought to re-distribute market share of IEX". Comment: this is IEX's argument against market coupling. No number is given.

---

## A6. CERC fee orders, the fee staff paper, and AR fee risk language

### A6.1 CERC transaction-fee order of 2023 (2 paise per side ceiling)

NOT DISCLOSED. No document in the corpus mentions a 2023 CERC fee order, a fee ceiling, "2 paise", or "per side". Searches of both ARs, both results filings, all four PMUs, both presentations and all four concalls found nothing. Pointer: the AR26 MD&A regulatory section (pp.61-62, "REGULATORY RISKS") and the AR25 regulatory developments section (pp.55-59) are where a filed disclosure would sit. Both discuss only market coupling, GNA, bidding oversight and carbon credit regulations. The auditor's KAM (AR26 p.172, AR25 p.163) refers only in general terms to fees "governed as per the terms and conditions/ rules framed by CERC".

### A6.2 Dec-2025 CERC staff paper on fee review

NOT DISCLOSED. No document in the corpus refers to a CERC staff paper on exchange fees. Every "staff paper" hit in the corpus concerns other subjects:
- AR25 p.59: "CERC issued a staff paper on market coupling on 21 st August 2023 and invited the views of stakeholders." [FILED]
- AR25 p.56: staff papers on GNA Regulations and on "an oversight on bidding behaviour in power exchanges" [FILED]
- CC-Feb p.10: "No that was the staff paper. That was on the staff paper that what are views on the staff paper." [MGMT]. This refers to market coupling.
- CC-Jul p.17: "For capacity market, again, a staff paper has been recently introduced by C ERC." [MGMT]

Pointer: the Q3FY26 concall (CC-Feb, 30-Jan-2026) is the first call after December 2025. Its only fee exchange is the one below. The AR26 regulatory risk section (pp.61-62) would be the filed location, and it carries nothing on fees.

### A6.3 Later CERC communication on fees, and management statements on fee risk

- CC-Feb p.12 [MGMT]. The analyst asks: "there was this news article that mentioned that the tariffs like the exchange fees might be cut from four paise to whatever half of it on each side. What is your idea on that? Do you see that happening?" Satyanarayan Goel replies: "I haven't heard any such thing. I mean, there are many news items, so I don't really pay any much attention to that. But as far as the Commission is concerned, we haven't heard anything like that from the Commission."
  Comment: management denied any CERC communication on a fee cut as of 30-Jan-2026. This is the only fee-cut exchange in the corpus.
- CC-Apr p.15 [MGMT], on the market coupling worst case: "Against INR 0.04 (four paise), I think the margin is around (3.6 or 3.7 paisa) INR 0.036, INR 0.037. That's the kind of number. So we don't expect significant impact on the margin part of it, the transaction fees part."
  Comment: management expects fee realisation to hold under competition, and cites TAM as the precedent.
- CC-Jul p.35 [MGMT]. The analyst asks whether market coupling fees "will that in the way force you to reduce your fee because price discovery has moved to the MCO". Satyanarayan Goel replies: "I think these are the issues which are flagged by the Grid India also in their comments to CERC and in addition to the point raised by you, there are many more issues, which needs to be answered. I think these things will be answered may be in the final regulations or in the procedure or subsequently by C ERC by their various orders ."
  Comment: the MCO fee allocation is unresolved in the draft coupling regulations. AR26 p.62 [FILED]: "On 17 April 2026, CERC issued the Draft Market Coupling Regulations. Final regulations are yet to be issued."
- CC-Nov p.18 [MGMT], on price wars after coupling: "Let the coupling happen. We will look at the market conditions and take a call based on that. I do not think we need to decide that thing today itself. I can tell you one thing, in the Term Ahead Market, all three exchanges are active. And there also, the price war is not there."

### A6.4 AR risk-factor language on fees, verbatim

Search terms "transaction fee", "fee", "paise", "tariff" were run over the risk sections of both ARs (AR26 pp.61-63; AR25 pp.58-60). The only fee language is the Market Risk paragraph. It is identical in both years:

AR26 p.63 [FILED], and the same text in AR25 p.60 [FILED]:
> "MARKET RISK
> The Company's revenues could be adversely affected if its market share does not grow year-on-year and the company does not put efforts to bring products commensurate with the changing market requirements.
> Mitigation: Revenues of IEX are majorly derived from transaction fees and annual subscription fees. The Company systematically engages with all the stakeholders in an attempt to increase the participant base and driving revenue growth. Over time the Company has taken many initiatives towards enhancing customer centricity and customer loyalty through several projects. Also, the Company is in regular discussion with policy makers and stakeholders towards creation of new market-friendly products."

Comment: neither AR names regulatory fee-rate risk (a CERC cap or cut) as a risk factor. "Tariff" and "paise" do not appear in either risk section. The regulatory risk text in both ARs is about market coupling only.

Related filed text outside the risk section:
- AR26 p.172 and AR25 p.163, Key Audit Matter: "The revenue earned by the Company in the form of transaction fee in respect of electricity traded on the exchange and related services is governed as per the terms and conditions/ rules framed by CERC. The Company also earns revenue by means of membership and subscription fee charged to its members."

---

## Incidental conflicts found while extracting (outside Part A scope, reported per Rule 4)

- G-DAM FY26 average price. AR26 p.48 [FILED]: "The average price in G-DAM for FY'26 was `4.36/unit, a decline of 10.6% compared with FY'25". PMU-FY26 p.4 [MGMT] Reg 30 media release: "The weighted average price in Green Day-Ahead Market (G-DAM) for FY'26 at Rs 3.59/unit declined 10.6% compared to FY'25." **CONFLICT**: Rs 4.36 vs Rs 3.59, with the same growth rate.

---

## CLOSING

### Documents quoted (filename, document date)

| Filename | Date |
|---|---|
| annual-report__Annual_Report_2026.txt | FY26 AR, filed BSE 14-Aug-2026 |
| annual-report__Annual_Report_2025.txt | FY25 AR (Annual Report 2024-25) |
| results__FY26_Q4_Audited_Results_2026-04-23.txt | 23-Apr-2026 |
| results__Q1FY27_Results_Unaudited_2026-07-23.txt | 23-Jul-2026 |
| announcements__FY26_Q4_Press_Release_2026-04-23.txt | dated 23-Apr-2026 |
| results__Q1FY27_Press_Release_2026-07-23.txt | dated 23-Jul-2026 |
| announcements__Power_Market_Update_FY26_Q4FY26_Mar2026.txt | dated 06-Apr-2026 |
| announcements__Power_Market_Update_Q1FY27_Jun2026.txt | dated 03-Jul-2026 |
| announcements__Power_Market_Update_Jul2026.txt | dated 04-Aug-2026 |
| announcements__Power_Market_Update_Aug2026.txt | dated 03-Sep-2026 |
| presentation__Investor_Presentation_Q4FY26_2026-04-23.txt | 23-Apr-2026 |
| presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt | 24-Jul-2026 |
| other__Concall_Nov_2025_Q2FY26_Transcript.txt | call 31-Oct-2025; filed 07-Nov-2025 |
| concalls__Concall_Feb_2026_Transcript.txt | call 30-Jan-2026; filed 05-Feb-2026 |
| concalls__Concall_Apr_2026_Transcript.txt | call 24-Apr-2026; filed 30-Apr-2026 |
| concalls__Concall_Jul_2026_Transcript.txt | Analyst Meet 24-Jul-2026; filed 31-Jul-2026 |

Not read, and outside the named scope: `announcements__Rumour_Verification_Reply_2026-04-20.txt` is in the work folder. Its content is unknown here. If the rumour it answers concerns fees, it bears on A6. The operator should decide whether to add it to a follow-up extraction.

### NOT DISCLOSED items, with pointers

1. HP-DAM volume alone, any period. It would sit in the PMU DAM paragraph or the AR26 MD&A Business Review p.48. Both report DAM "including HPDAM" only.
2. Separate volumes for TAM sub-segments (DAC, HP-TAM, LDC, daily/weekly/monthly), any period. They would sit in the PMU TAM paragraph (PMU-FY26 p.3, PMU-Q1 p.3) or AR26 p.48. Only the aggregate is printed. PRES-Q4 p.8 gives a DAC share of 2% but no volume.
3. G-DAM vs G-TAM volume split, any period. It would sit in the PMU Green Market paragraph (PMU-FY26 p.4, PMU-Q1 p.3) or AR26 p.48. Only the aggregate is printed.
4. I-DAM (integrated), ancillary DAM-AS / RTM-AS, cross-border and intraday volumes, any period. They would sit in AR26 p.7 (segment list, no volumes) or the MD&A Business Review pp.48-49.
5. RTM FY24 volume in a filed document. It would sit in AR25 MD&A p.47, which gives only "+29%". A [MGMT] figure exists: PRES-AM p.12 shows 30.1 BU.
6. ESCert volume for FY24, FY26 and Q1FY27. It would sit in the AR MD&A certificate segment (AR26 p.49; AR25 p.48, which gives FY25 only) or the PMU REC section. PMUs carry no ESCert line.
7. Fee schedule: per unit, per side, per segment, per member category. It would sit in IEX's CERC-approved Business Rules / fee circulars, which are not in the corpus. It is not in AR26 Note 28 p.211, the policy note p.190, or any concall. Management gives only verbal figures: about 4 paise for electricity, Rs 20 per REC, and 3.6-3.7 paise effective in TAM.
8. Whether "four paise" is per side or in total. No source says. The CC-Feb p.10 / p.12 and CC-Apr p.15 statements are silent on this.
9. Transaction fee revenue by individual segment (DAM / RTM / TAM / Green / REC / ESCert), all periods. It would sit in the AR26 Note 28 disaggregation table p.211 (and consolidated p.273). Only Electricity vs Certificates is given.
10. Q1FY27 Electricity vs Certificates fee split, and the Q1FY27 split into transaction, subscription and membership fees. It would sit in a results note or a Q1FY27 investor slide. RES-Q1 pp.4-10 prints the face P&L only. PRES-AM p.38 gives total operating revenue only. There is no Q1FY27 "Breakup of standalone revenues" slide equivalent to PRES-Q4 p.26.
11. Admission fee as a separate revenue amount, all periods. It would sit in AR Note 28 (standalone) or Note 27 (consolidated). The only line is "Membership, processing and transfer fees", and the policy (AR26 p.190) maps admission to membership fees.
12. Split of "Reduction towards incentives/ discounts" by segment, and the Q1FY27 amount. It would sit in AR26 Note 28 p.211 (total only). The Q1FY27 results filing has no revenue note.
13. IEX's own market share of exchange-traded electricity for FY24, FY25 and FY26 full year, overall and by segment, in any filed document. It would sit in the AR MD&A Short-Term Electricity Market section (AR26 p.47; AR25 p.46), which gives only the all-exchange 60% share sourced to CERC. The CERC Market Monitoring Report is not in the corpus. Management gives Q2FY26 (CC-Nov p.18) and 9MFY26 (CC-Feb p.16) figures, with no denominator stated.
14. CERC transaction-fee order of 2023 (2 paise per side ceiling). Not mentioned anywhere in the corpus. It would sit in the AR26 Regulatory Risks section pp.61-62 or the AR25 regulatory developments pp.55-59.
15. Dec-2025 CERC staff paper on fee review. Not mentioned anywhere in the corpus. It would sit in the AR26 Regulatory Risks section pp.61-62, or be raised in CC-Feb (the first call after December 2025). CC-Feb p.12 has only an analyst's news reference, which management denied.
16. Any later CERC communication on fees (2026). Not mentioned. The same pointers apply. The CC-Jul p.35 answer defers the MCO fee questions to the final coupling regulations.

---

# IEX extraction P1, Part B: market coupling as the company describes it

Corpus only. Source dir: `runs/iex-2026-09-08/work/`. Page anchor = the `=== PAGE n ===` marker in the extracted text (not the printed folio). Quotes are verbatim from the extracted text; line breaks joined, OCR spacing artefacts kept as found. Tiers: [FILED] = AR, results filing, exchange announcement; [MGMT] = concall, presentation, press release.

---

## B1. Filed passages: coupling, 8/SM/2025, 23-Jul-2025 order, 9-Jan-2026 corrigendum, 13-Feb-2026 APTEL judgment, 17-Apr-2026 draft Second Amendment, Supreme Court

### B1.1 FY25 AR (`annual-report__Annual_Report_2025.txt`; Board's Report dated 08-Aug-2025; filing cover letter dated 18-Aug-2025; FY25 financial statements signed 24-Apr-2025)

**(a) Chairman's Message to Shareholders, p.17 [FILED]**
> "Subsequent to the staff paper issued on market coupling in August 2023, and order in February 2024, Hon'ble CERC has now by order dated 23rd July 2025 decided to implement coupling in Day Ahead Market (DAM). The decision to implement market coupling in DAM is based on an insignificant increase in social welfare by 0.3% and volume increase by 0.2%. As per the total volumes traded at IEX in FY'25, Day Ahead Market comprised only 44% of total volumes. In a coupled scenario as well, IEX remains committed to enhancing the participants' experience and we are confident of sustaining our leadership through continued innovation and customer-centric initiatives. Further, with regard to coupling in Real Time Market (RTM) segment, coupling of RTM with Security Constrained Economic Dispatch (SCED) and Term Ahead Markets (TAM) of power exchanges, no decision has been taken. These will be examined separately."

Comment: first filed description of the 23-Jul-2025 order; frames DAM as 44% of FY25 volume; RTM/TAM "no decision".

**(b) MD&A, "MARKET COUPLING", p.55 [FILED]**
> "The CERC Power Market Regulations 2021 provides for introduction of market coupling of Power Exchanges as and when decided by the Hon'ble CERC through a separate regulation. In this regard, Ministry of Power shared a letter with CERC, which issued a staff paper on market coupling on 21 st August 2023 and invited views of stakeholders. Based on the suggestions received and the insignificant gains observed in simulations of coupling of DAM or RTM market, CERC issued an order in February 2024 to further analyse the case and directed for a Shadow Pilot by GRID-INDIA for various market coupling scenarios and submit its report to the Hon'ble CERC. Further, the CERC issued an order on 23 rd July 2025 for implementation of the coupling of Day-Ahead Market (DAM) of the power exchanges in a round-robin mode by January 2026. Under the round-robin mode, the power exchanges may act as the Market Coupling Operator (MCO) on a rotational basis, with Grid-India being the fourth MCO for backup and audit purposes. Additionally, as per the order, given the shorter time for bid submission and running the market clearing engine, the decision to implement the coupling of Real-Time Market (RTM) of the power exchanges shall be considered at a later stage after gaining operational experience from the coupling of DAM. The Commission also noted that there is a need to further examine the approach and methodology of the shadow pilot run of coupling of RTM with SCED adopted by Grid-India. The Commission additionally noted that the feasibility of coupling of the Term-Ahead Market (including Contingency Contracts) of the power exchanges will be examined by running a shadow pilot separately."

Comment: the only filed description of the July 2025 design (round-robin, exchanges as rotating MCO, Grid-India fourth MCO). Contrast with B1.2(b) and B1.2(e): the FY26 AR describes the 17-Apr-2026 draft as Grid-India as MCO.

**(c) MD&A, Risk management, "Regulatory Risks", p.59 [FILED]**
> "One of the key regulatory aspects which has direct bearing on the Exchange is Market Coupling. CERC issued a staff paper on market coupling on 21 st August [...]" (text continues as in (b)), then: "Mitigation: As of FY'25, the Day Ahead Market comprised 44% of total volumes of IEX. In a coupled scenario as well, we remain committed to enhancing our participants' experience and are confident of sustaining our leadership through continued innovation and customer-centric initiatives. [...] In RTM there are 48-half hourly auctions per day. We believe that implementation of RTM coupling will be very challenging."

Comment: coupling named as the key regulatory risk in FY25. The FY25 AR gives no impact number.

**(d) Board's Report, "Significant and Material Orders passed by the Regulators, Courts or Tribunals", p.80 (repeated verbatim at p.81; the extracted text carries the page twice) [FILED]**
> "During FY 2024–25, there were no significant or material orders passed by the Regulators, Courts, or Tribunals impacting the going concern status and the Company's operations. However, subsequent to the closure of FY 2024–25 and up to the date of this report, the Central Electricity Regulatory Commission (CERC) has issued a Suo-Moto Order dated July 23, 2025, in Petition No. 8/SM/2025, initiating the implementation of Market Coupling in DAM Segment of power exchanges by January 2026. This regulatory development signifies a proposed change in the market mechanism for the DAM segment. For further details, kindly refer to the Management Discussion and Analysis (MDA) Report forming part of this Annual Report."

Comment: first filed use of "Petition No. 8/SM/2025". It is a post-year-end item in the Board's Report dated 08-Aug-2025.

**(e) FY25 financial statement notes: NOT DISCLOSED.** The FY25 standalone and consolidated statements were signed 24-Apr-2025, before the 23-Jul-2025 order. No coupling note appears. Pointer: FY25 AR, standalone and consolidated notes (subsequent-events and contingent liability notes). The first note appears in FY26 (B1.2(e), (f)).

### B1.2 FY26 AR (`annual-report__Annual_Report_2026.txt`; Board's Report and MD&A signed 23-Jul-2026; filed on BSE with cover letter dated 14-Aug-2026)

**(a) Message to Shareholders (Chairman & Managing Director), p.32 [FILED]**
> "On market coupling, CERC issued draft regulations in April 2026 proposing Grid India as the Market Coupling Operator. We continue to engage actively with the regulator, and through the legal process where warranted, to ensure that any structural change strengthens, rather than dilutes, the price discovery and efficiency that competitive markets have delivered for participants."

**(b) MD&A, "MARKET COUPLING", p.58 [FILED]**
> "CERC vide its order dated 06 February 2024, directed Grid India to carry out pilot study to assess the impact of market coupling. As per the Grid India report, increase in economic surplus was 0.3% which is insignificant. Based on the submissions made by Grid-India, CERC, vide its order dated 23 July 2025, decided to initiate the process for implementing market coupling of the Day-Ahead Market (DAM) and directed staff of commission to frame procedure and regulation for the implementation of same. As per the order, with respect to the Real-Time Market (RTM), given the shorter time for bid submission and running the market clearing engine, the decision to implement the coupling of Real-Time Market (RTM) of the power exchanges shall be considered at a later stage after gaining operational experience from the coupling of DAM. Additionally, the feasibility of coupling the Term-Ahead Market (including Contingency Contracts) of the power exchanges shall be examined through a shadow pilot. The CERC Order of July 2025 was challenged before the Appellate Tribunal of Electricity (APTEL) by IEX on various points of its legality, transparency and on merits. In February 2026, APTEL dismissed the Appeal citing IEX is not a "person aggrieved" at this stage since market coupling to be implemented through regulations to be notified separately by CERC and the CERC Order of July 2025 is merely "administrative" and "tentative". APTEL further preserved IEX rights to appeal on merits after framing of the regulations by CERC. Subsequently, IEX filed a Civil Appeal with stay application in Supreme Court against the APTEL judgement on 10th April 2026. On 17th April 2026, CERC issued a draft amendment to PMR 2021 for implementation of market coupling with Grid-India as the MCO. Public hearings on the draft regulations concluded on 10th June 2026."

Comment: the only filed statement that the civil appeal carries a "stay application". It also says APTEL called the July 2025 order "administrative" and "tentative".

**(c) MD&A, Risk management, "REGULATORY RISKS", p.61 (continues to p.62) [FILED]**
p.61: > "One of the key regulatory aspects which has direct bearing on the Exchange is Market Coupling." (then repeats the 06-Feb-2024 / 23-Jul-2025 / RTM / TAM text of (b)).
p.62: > "IEX challenged the July 2025 Order before the Appellate Tribunal for Electricity (APTEL) on 28 August 2025. Subsequently, in its Order dated 13 February 2026, APTEL mentioned that as market coupling cannot be implemented without regulations, IEX was not an aggrieved party at that stage. As per the order, as and when final regulations are issued and if IEX is aggrieved by them, they have the liberty to challenge the regulations before an appropriate forum including all grounds raised in the appeal filed before APTEL. Subsequently, on April 10,2026, IEX filed an appeal against the APTEL order in the Supreme Court, and the hearing is scheduled for August 03, 2026. On 17 April 2026, CERC issued the Draft Market Coupling Regulations. Final regulations are yet to be issued."
p.62: > "Mitigation: The Day-Ahead Market (DAM) contributed 39% of IEX's total traded volumes in FY'26, compared with 44% in FY'25 and nearly 95% in FY'15, reflecting the growing contribution of other market segments to the overall product mix."
p.62: > "We believe that the impact of market coupling would be minimal."

Comment: the filed dates are APTEL appeal 28-Aug-2025, APTEL order 13-Feb-2026, SC appeal 10-Apr-2026, SC hearing "scheduled for August 03, 2026", draft 17-Apr-2026. **CONFLICT** on the next SC hearing: see B1.4(b), where the analyst meet says "Monday (27th July)".

**(d) Board's Report, "Significant and Material Orders passed by the Regulators, Courts or Tribunals", p.82 to p.83 [FILED]**
p.82: > "During FY'26, no significant or material orders were passed by any Regulators, Courts, or Tribunals which would have an impact on the going concern status or the operations of the Company."
p.83: > "However, the Central Electricity Regulatory Commission ("CERC"), issued a Suo Motu Order dated July 23, 2025, in Petition No. 8/SM/2025, initiating the process for implementation of market coupling for the Day Ahead Market (DAM) of power exchanges by January 2026. The Company challenged the aforesaid Order before the Appellate Tribunal for Electricity ("APTEL"). APTEL, vide its judgment dated February 13, 2026, held that the Company is not a "Person Aggrieved" at this stage, as market coupling can be implemented only upon the issuance of separate regulations by CERC. Aggrieved by the said judgment, the Company has filed a civil appeal before the Hon'ble Supreme Court of India on April 10, 2026. For further details, kindly refer to the Management Discussion and Analysis (MDA) Report forming part of this report."

Comment: second and last filed use of "8/SM/2025". The Board's Report places the matter under "no significant or material orders ... However". It does not name the 17-Apr-2026 draft.

**(e) Standalone Note 47, p.224 [FILED, STANDALONE]**
> "47. The Central Electricity Regulatory Commission ("CERC") vide its Suo Motu Order dated July 23, 2025, proposing the process for implementation of market coupling for the Day Ahead Market (DAM) of power exchanges by January 2026. The Company challenged the aforesaid CERC order before the Appellate Tribunal for Electricity (APTEL). The Hon'ble APTEL, vide its order held that the Company is not a "person aggrieved" at this stage, as market coupling can be implemented only once the separate Regulations are framed by the CERC. Against the Hon'ble APTEL order, the Company has filed a civil appeal before the Hon'ble Supreme Court of India. Subsequently, on April 17, 2026, CERC issued the draft CERC (Power Market) (Second Amendment) Regulations, 2026, proposing amendments to the existing CERC (Power Market) Regulations, 2021 for public consultation."

Comment: narrative only. No amount, no provision, no contingent-liability reference, no statement of financial impact. It gives no dates for the APTEL order or the SC filing. This is the only filed place that names the draft as the "CERC (Power Market) (Second Amendment) Regulations, 2026", together with (f) and B1.3.

**(f) Consolidated Note 53, p.291 [FILED, CONSOLIDATED]**
> "53. The Central Electricity Regulatory Commission ("CERC") vide its Suo Motu Order dated July 23, 2025, proposing the process for implementation of market coupling for the Day Ahead Market (DAM) of power exchanges by January 2026. The Company challenged the aforesaid CERC order before the Appellate Tribunal for Electricity (APTEL). The Hon'ble APTEL, vide its order held that the Company is not a "person aggrieved" at this stage, as market coupling can be implemented only once the separate Regulations are framed by the CERC. Against the Hon'ble APTEL order, the Company has filed a civil appeal before the Hon'ble Supreme Court of India. Subsequently, on April 17, 2026, CERC issued the draft CERC (Power Market) (Second Amendment) Regulations, 2026, proposing amendments to the existing CERC (Power Market) Regulations, 2021 for public consultation."

Comment: word for word the same as standalone Note 47.

**(g) Auditor's reports, Key Audit Matters: NOT DISCLOSED as a coupling item.** The standalone KAM (p.172) and the consolidated KAM (p.232) each name revenue recognition as the single key audit matter. No emphasis-of-matter paragraph on coupling was found. Pointer: FY26 AR, Independent Auditor's Reports, "Key Audit Matter" sections.

### B1.3 Exchange announcement: Rumour Verification Reply (`announcements__Rumour_Verification_Reply_2026-04-20.txt`; dated 20-Apr-2026; to BSE Surveillance; signed Vineet Harlalka, CFO, CS & Compliance Officer)

**p.1 [FILED]**
> "In reference to your email dated April 20, 2026, under Ref. No.: L/SURV/ONL/RV/SG/ (2026 -2027)/9, about Clarification/Confirmation on news item appearing in "https://www.moneycontrol.com dated 20th April 2026 captioned "IEX shares fall 6% after CERC releases draft notification on market coupling norms. ("News Article")."
> "In this regard, we would like to submit that the News Article pertains to a draft notification issued by the Central Electricity Regulatory Commission ('CERC') relating to the CERC (Power Market) (Second Amendment) Regulations, 2026, proposing amendments to the CERC (Power Market) Regulations, 2021. The said draft regulations have been issued for stakeholder consultation and are available in the public domain on CERC website at https://cercind.gov.in/Draft_reg.html."
> "We would like to further submit that CERC, vide its Su-Moto Order dated July 23, 2025, had issued directions for implementation of Market Coupling of power exchanges in the Day-Ahead Market (DAM) segment with effect from January 2026, the said CERC Order was duly intimated to the stock exchanges by the Company, in compliance with the SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015 ("SEBI Listing Regulations"). The present draft notification is in continuation of earlier CERC Order."

**p.2 [FILED]**
> "This is a regulatory consultative exercise initiated by the regulator, and not the outcome of any negotiations, arrangements, or events."
> "The movement in the share price appears to be market -driven based on publicly available information including the said draft regulations."
> "c) In case of regulatory/legal proceedings please provide the information on initiation / outcome of the proceedings. Not Applicable. The said News Article pertains to the draft notification issued by the CERC which is a consultative exercise, and is subject to stakeholder consultation, review, and final regulation/notifications may be dete rmined by CERC after stakeholder consultation."

Comment: the company says it intimated the 23-Jul-2025 order to the exchanges. That intimation is not in this corpus (see CLOSING). **CONFLICT**: on 20-Apr-2026 the reply answers "Not Applicable" to the query on regulatory/legal proceedings. The FY26 AR (B1.2(c), (d)) records a civil appeal filed in the Supreme Court on 10-Apr-2026, ten days earlier. The reply does not mention the APTEL order or the SC appeal. Both are reported. This file does not reconcile them.

### B1.4 Results filings

**(a) FY26 Q4 audited results (`results__FY26_Q4_Audited_Results_2026-04-23.txt`, dated 23-Apr-2026): NOT DISCLOSED.** Standalone notes 1 to 9 (pp.7 to 10) and consolidated notes 1 to 9 (pp.15 to 19) cover the balance sheet, cash flow, approval, Ind AS basis, single segment, ESOP, balancing figures, dividend, labour codes, and filing. None mentions coupling, APTEL, the Supreme Court, or the 17-Apr-2026 draft. The auditor's report shows no emphasis of matter on coupling. Caveat: pp.1 to 2 (cover letter) extracted as a character-shifted cipher (e.g. p.2: "Mcocnc!Oknnu!Eqorqwpf..."). Those pages are unreadable here. They look like the address block and signature. Pointer: filed PDF pp.1 to 2, results cover letter.

**(b) Q1FY27 unaudited results (`results__Q1FY27_Results_Unaudited_2026-07-23.txt`, dated 23-Jul-2026): NOT DISCLOSED.** Standalone notes 1 to 7 (p.5) and consolidated notes 1 to 7 (p.10) cover approval, Ind AS basis, single segment, ESOP, balancing figures, dividend, and filing. There is no coupling or litigation note. The 17-Apr-2026 draft and the SC appeal came before this filing, but only the FY26 AR notes (B1.2(e), (f)) carry them. Pointer: Q1FY27 results, "Notes (contd....)".

### B1.5 Named items never found in any filing

- **Corrigendum of 9-Jan-2026: NOT DISCLOSED.** It is not in the FY25 AR, FY26 AR, either results filing, or any announcement. The only "corrigendum" hits in both ARs refer to a "corrigendum dated 14 July 2017" in the accounting-policy notes, which is unrelated. No transcript or presentation mentions a January 2026 corrigendum or modification of the July order. Pointer: if it exists, look in the FY26 AR MD&A "MARKET COUPLING" (p.58) and Board's Report "Significant and Material Orders" (p.83), or in a Reg 30 intimation of Jan-2026. That intimation is not in the corpus.
- **Reg 30 intimation of the 23-Jul-2025 CERC order: NOT IN CORPUS.** The rumour reply (B1.3 p.1) says it was "duly intimated". Pointer: BSE/NSE announcements, about 23 to 24 Jul-2025.
- **Reg 30 intimations of the APTEL judgment (13-Feb-2026) or the SC civil appeal (10-Apr-2026): NOT IN CORPUS.** Pointer: BSE/NSE announcements, Feb-2026 and Apr-2026.
- **"Petition 8/SM/2025"** appears only in the Board's Reports (FY25 AR p.80/81; FY26 AR p.83). It does not appear in the financial statement notes, which say only "Suo Motu Order dated July 23, 2025".

---

## B2. Management statements: implementation date, segments covered, RTM, volume or fee impact

Chronological order. All [MGMT].

**Q2FY26 call, 31-Oct-2025 (`other__Concall_Nov_2025_Q2FY26_Transcript.txt`, transcript filed 07-Nov-2025)**

- p.5 to 6, opening remarks (speaker not labelled in this block; the call's management speakers are Satyanarayan Goel, CMD; Vineet Harlalka, CFO; Rohit Bajaj):
  > "CERC issued an order on implementing market coupling on 23rd July, in which regulator decided to initiate process of implementation of market coupling of the Day Ahead Market. This is to be done by January 2026. In the same order, it is mentioned that coupling of Real-Time Market RTM will be considered at a later stage. The order also talks about running a shadow pilot for coupling of Term Ahead Market and stakeholder consultation for RTM and SCED coupling. [...] IEX has filed an appeal against this order in Appellate Tribunal for Electricity, APTEL. The next date of hearing is scheduled on 28th of November."
- p.8 to 9, Satyanarayan Goel, answering Ketan Jain (Avendus Spark), who asked whether it would be implemented by Jan 2026:
  > "With regard to status of market coupling, we are not aware about any developments which have taken place so far . [...] Maybe those drafts will be issued for public consultation. So, to the best of our knowledge, so far, nothing like that has happened."
  > "See, we are not aware of any such, program about how they want to implement it and when they want to implement it."
- p.11, Satyanarayan Goel (RTM):
  > "And with regard to your question on coupling of RTM, if you look at the order, commission has not taken any view regarding implementation of RTM. So they have said that looking at the time constraints and based on the experience, it will be considered. So they will take a view separately on that if required."
- p.14 to 15, Satyanarayan Goel (clearing after coupling):
  > "So, there will be interexchange settlement also. So whatever volumes are cleared on IEX platform, we will do a settlement for that."
- p.16 to 17, Satyanarayan Goel, answering Archit Agarwal:
  > "No, why are you saying the after market coupling the revenue will decrease? We are making all efforts to ensure that we retain our market share and volumes are increasing every year."
  > "Gentlemen, please hold the line, coupling has not happened, okay? So, for coupling only order has been issued, coupling has not happened. So, there is no change in that. And volumes have increased by 16%."
- p.18, Satyanarayan Goel, answering Chirag Maroo on price wars:
  > "Let the coupling happen. We will look at the market conditions and take a call based on that. [...] in the Term Ahead Market, all three exchanges are active. And there also, the price war is not there. So, I do not see any such situation that after coupling, there will be a price war in the DAM market."

**Q3FY26 call, 30-Jan-2026 (`concalls__Concall_Feb_2026_Transcript.txt`, transcript filed 05-Feb-2026)**

- p.5, opening remarks:
  > "According to the order, this was to be done by January 2026. IEX has filed an appeal in Appellate Tribunal for Electricity, APTEL, and today, the hearing has concluded. We expect the final order to be released shortly."
- p.8, Satyanarayan Goel, answering Ketan (Avendus):
  > "Can't say, but it should happen within a month's time."
  > "First of all, why are you saying that if things don't go in our favour? Things will definitely go in our favour. In any case, even if they have to go with the coupling, lot of things have to be done yet. [...] they have to issue the draft regulations, invite comments on that and give statement of reason for that, why they want to do coupling."
- p.10 to 11, Satyanarayan Goel, answering Devesh Agarwal (IIFL):
  > "What we had challenged in the APTEL was that this order should be set aside because the order has not followed the due process of order making. The transparency was not ensured, and there was no merit in implementing market coupling. But during the discussions, it also emerged that CERC has mentioned that they will be doing this market coupling only after making the regulations."
- p.11 to 12, Satyanarayan Goel, answering Pranav Jain (RTM):
  > "Commission has already in the order mentioned that they will look at the experience of this and thereafter decide whether they want to go for the RTM or not. Because in case of RTM, the complications are more. You have to do it 48 times in a day [...]"
- p.12, Satyanarayan Goel, answering Pranav Jain on a news report of a fee cut from four paise:
  > "I haven't heard any such thing. [...] as far as the Commission is concerned, we haven't heard anything like that from the Commission."
- p.12, Satyanarayan Goel, answering Abhir Pandit (Old Bridge MF):
  > "No, no. Price discovery will be done on the round robin basis. Maybe for one month, one exchange will do. For next month, another exchange will do."
- p.14, Satyanarayan Goel, answering Vijay (Spark Capital), on timing:
  > "Can't say. It's a regulatory process, and we really cannot say how much time it will take."

**Q4FY26 call, 24-Apr-2026 (`concalls__Concall_Apr_2026_Transcript.txt`, transcript filed 30-Apr-2026)**

- p.5 to 6, opening remarks:
  > "Further, on April 17, 2026, CERC issued draft regulations for market coupling, according to which Grid India would act as the market coupling operator, that is the MCO. Also, Grid India would be responsible to frame detailed procedure s for implementation of market coupling. CERC has invited stakeholder comments on the draft till 16th May 2026."
  Comment: **CONFLICT** on the comment deadline. This call says 16-May-2026. The Analyst Meet presentation (below) says "June 5th 2026".
- p.10, Satyanarayan Goel, answering Sumit Kishore on timelines:
  > "Sumit, it's very difficult to say on that. I mean if you recall, this PMR 2021 was issued in February '21. But the draft of that came to best of my knowledge in 2019. So , I can't really say how much time they will take [...]"
- p.11 to 12, Satyanarayan Goel, answering Kunal Thanvi (Banyan Tree):
  > "And now they have changed their decision and in the draft regulations, they are talking about Grid India. So I think situation is still fluid. [...] So maybe in due course of time, they may review their own decision about the market coupling also and may not go ahead with this."
  > "Now Grid India will have to create the infrastructure and software for this, which will be additional costs."
  > "I fully agree with you that based on the studies done so far, there is no benefit of coupling."
  > "And exchanges will be again doing the physical and financial settlement. All that will be done still by the exchanges. Only the price discovery will be done by Grid India."
- p.14, Satyanarayan Goel, answering Nitin Shakdher (worst case):
  > "First of all, as far as market coupling itself is concerned, it won't be fair to assume that market coupling is going to happen. [...] So with that, I'm sure that we should, even after coupling also, we should be able t o retain a significant part of the market share in this DAM segment."
- p.15, Satyanarayan Goel (fees):
  > "in case of the Term Ahead Market, where the liquidity is practically uniform across all 3 exchanges, the share of all 3 exchanges is in that same range of, 40%, 50%, 30%, 20% kind of numbers. [...] Against INR 0.04 (four paise), I think the margin is around (3.6 or 3.7 paisa) INR 0.036, INR 0.037. That's the kind of number. So we don't expect significant impact on the margin part of it, the transaction fees part."
  Comment: the "40%, 50%, 30%, 20%" figures describe TAM market shares. They are not a coupling impact estimate.
- p.16, Satyanarayan Goel, answering Ravi Purohit (RTM in draft):
  > "As far as the draft guidelines are concerned, there is just an enabling provision that in the RTM to be done from a date to be notified in the future. If they decide to do something in future, then they can do that part of it. But there is no such decision as of now [...] So I have my own doubts about coupling in the RTM market."
  > "In case of coupling in the RTM market, if out of the 3 exchanges, if one exchange data does not get aggregated at the place, then you'll lose significant buy and sell volume. [...] it will definitely have a very, very adverse impact on the market."
  Comment: management confirms the 17-Apr-2026 draft carries an RTM enabling provision "from a date to be notified". The draft text is not in the corpus.

**Q4FY26 Investor Presentation (`presentation__Investor_Presentation_Q4FY26_2026-04-23.txt`, 23-Apr-2026): NOT DISCLOSED.** No coupling slide or text. Pointer: the full deck; the Analyst Meet deck carries the update instead.
**Press releases (`announcements__FY26_Q4_Press_Release_2026-04-23.txt`, `results__Q1FY27_Press_Release_2026-07-23.txt`): NOT DISCLOSED.** No coupling text.

**Q1FY27 Analyst Meet, 24-Jul-2026 (`concalls__Concall_Jul_2026_Transcript.txt`, transcript filed 31-Jul-2026)**

- p.4, Satyanarayan Goel, CMD, opening remarks:
  > "On the market coupling front, CERC has issued draft regulations in the month of April and they have proposed Grid India as the Market Coupling Operator (MCO). Following the submissions and comments, public hearing was held on 10th of June. [...] I would like to mention that we continue to engage actively with the policy makers and regulators and are also exploring the legal recourse available to us."
  > "So as of now, the intent is to do coupling in the Day Ahead Market. And in fact, in the Real-Time Market, (in light of the) discussion paper for Shortening the Scheduling, i.e. reducing the gate closure time from 75 to 50 minutes where RTM bidding time will be reduced from 15 to 5 minutes. I think coupling will become further difficult."
- p.4 to 5, Satyanarayan Goel, CMD, opening remarks (**the 20-40% remark**):
  > "So I am sure that even if coupling is implemented, it may not have significant impact as far as the market share is concerned. In fact, you know, there was a time 6 to 7 years back, that the Day-Ahead Market used to be almost about 95% of our total volume. In the last 5-6 years, after the introduction of Real-Time Market, and the G-DAM Market, the Day-Ahead Market share has been reduced to almost about 40%. In this market, (even) after coupling with the customer-centric activities done by us, even if there is an impact, it may be about 20, 30, 40% (in DAM) . So, as far as business is concerned, I do not think it is going to be significant."
  Comment: the transcript says "20, 30, 40%", with "(in DAM)" as a bracketed insertion. It does not say whether this is a share of DAM volume lost, share of DAM retained, or share of total volume. That is NOT DISCLOSED. Pointer: audio recording of the 24-Jul-2026 Analyst Meet (not in corpus).
- p.20 to 21, Rohit Bajaj, JMD (legal status):
  > "Then we went to the Supreme Court challenging this particular aspect of it that we are aggrieved then APTEL must go into the merit of it. Our case petition has been admitted, notice has been served and one hearing happened where the notice was served, and now on Monday (27th July) there is the second hearing ."
  Comment: **CONFLICT** with FY26 AR p.62: "the hearing is scheduled for August 03, 2026". Both texts carry the same date, 23 to 24 Jul-2026.
- p.21, Rohit Bajaj, JMD (draft scope, per Grid India comments):
  > "First, they (Grid India) said the scope is not clear. [...] So they are seeking clarification on whether it should be done for DAM or should it be done for all the three things"
  > "Earlier in the July order, it said exchanges would be running the algorithm on a round-robin basis. In the draft PMR, the draft changed the stand and are saying Grid India would be Market Coupling Operator (MCO). Now Grid India has reservations there. They said if we are MCO then there is a Single Point of Failure."
- p.32, Satyanarayan Goel, answering Analyst 3 (who bears the MCO cost):
  > "There is nothing free. All costs are passed on to the consumer. Directly or indirectly."
- p.34, Satyanarayan Goel, answering Analyst 5 (timeline):
  > "These things are going to take time. So, it will be difficult for me to give any timeline on this , I can only tell you one thing that sometime in 1994-95 when availability--based tariff was first discussed in the country. It was finally implemented in 2003. It took so much of time . This may not take that long, but then definitely it will take a long time."
- p.34 to 35, Amit Kumar, Executive Director:
  > "So, The MCO arrangement is only for price discovery and not for bidding. [...] But from the customer side the work that we have done in driving API integration that competitive advantage remains with us."
- p.35, Satyanarayan Goel, answering Analyst 6 (MCO fee and pressure on IEX fees):
  > "I think these are the issues which are flagged by the Grid India also in their comments to CERC [...] That is why I said that implementation will take longer time because all these issues one by one will have to be addressed."
- p.35, Satyanarayan Goel, answering Analyst 6 (market share loss if DAM is coupled in 1 to 2 years):
  > "With the kind of service which we have provided in the last 18 years, the kind of customer connect that we have today. I don't see any loss in market share. after the coupling. But let's see."
  Comment: **CONFLICT**. In the same meeting's opening remarks (p.5), Goel says "even if there is an impact, it may be about 20, 30, 40% (in DAM)". Here he says "I don't see any loss in market share". The earlier statements also differ in wording: Q4FY26 p.14 says "retain a significant part of the market share in this DAM segment", and FY26 AR p.62 says "the impact of market coupling would be minimal".

**Analyst Meet Investor Presentation (`presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt`, 24-Jul-2026)**

- p.24, "Market Coupling Update" (Source: IEX, CERC):
  > "CERC issued order dated July 23rd, 2025, on market coupling in which the regulator decided to initiate the process of implementation of market coupling of Day Ahead Market in January 2026"
  > "IEX challenged above order dated 28th August 2025 in APTEL primarily on the grounds of:"
  > "In its order issued on February 13th, 2026, APTEL mentioned that as market coupling cannot be implemented without regulations, IEX is not an aggrieved party at this stage. [...]"
  > "IEXfileda pleaagainsttheAPTELorderin theSupremeCourt,andourappealhasbeenadmittedforhearingin thismatter"
  > "CERC issued Draft Regulations on 17th April 2026 proposing Grid India as the Market Coupling Operator"
  > "Insignificant gains of coupling as per simulations of CERC & NLDC including price gains in few instances: as admitted in their own order and reports"
  > "Order issued in July 2025, violated process prescribed by PMR 2021 and only sought to re-distribute market share of IEX"
  > "Lack of transparency in the entire process : Market design concerns remained unresolved; shadow pilot report undisclosed; July'25 Order tainted by insider trading allegations"
- p.25, "Market Coupling Update":
  > "Clarification on Scope of Market Coupling is required. Regulation should clarify whether the scope is for the Day Ahead Market or Integrated DAM (DAM, G-DAM, HP-DAM)"
  > "Grid-India as sole MCO will lead to single point of failure. [...] Fall back regulatory mechanism of allowing power exchanges to carry out price discovery is suggested"
  > "CERC invitedstakeholdercommentson the Draft till June 5th 2026 and public hearingconductedon June 10th 2026"
  > "Grid India made following observations:" (the list that follows did not extract as text)
  Comment: **CONFLICT** on the comment deadline. The deck says June 5th 2026. The Q4FY26 call (p.5 to 6) says 16th May 2026. The deck gives no volume or fee impact number.

**Expected implementation date, summary as stated:** the July 2025 order said "by January 2026" (all sources). No management statement gives a new date after January 2026. The Q3 answer is "Can't say" (p.14). The Q4 answer is "very difficult to say" (p.10). The July 2026 answer is "difficult for me to give any timeline [...] it will take a long time" (p.34). A post-Jan-2026 implementation date is NOT DISCLOSED. Pointer: final CERC (Power Market) (Second Amendment) Regulations (not issued per FY26 AR p.62).

**Fee impact:** there is no quantified guidance. The only fee statements are these. Q4FY26 p.15: "we don't expect significant impact on the margin part of it, the transaction fees part" (by TAM analogy). Q3FY26 p.12: no fee-cut news heard "from the Commission". Q1FY27 p.32 and p.35: the MCO cost is "passed on to the consumer", and fee questions are "flagged by the Grid India". A fee-impact estimate is NOT DISCLOSED. Pointer: concall Q&A and MD&A "REGULATORY RISKS" (FY26 AR p.61 to 62).

---

## B3. SEBI interim order (Oct-2025) and insider-trading allegations tied to the coupling decision

- **SEBI interim order of Oct-2025: NOT DISCLOSED.** It does not appear in the FY25 AR, FY26 AR, any results filing, any announcement, any concall transcript, or either presentation. Grep for "interim order", "show cause", and SEBI plus order/investigation/notice found nothing relevant.
  - Pointer 1: FY26 AR Corporate Governance Report, "Details of Non-Compliance by the Listed Entity, Penalties or strictures imposed [...] by Stock Exchanges, SEBI or any statutory authority", p.120. It reads: > "FY'26 No Non-Compliance" (the FY25 and FY24 cells carry the same entry in extraction). [FILED]
  - Pointer 2: Annual Secretarial Compliance Report FY26 (`announcements__Secretarial_Compliance_Report_FY26_2026-05-15.txt`, dated 15-May-2026), p.6, item 11: > "No Action(s) has been taken against the listed entity/its promoters/directors/ subsidiaries either by SEBI or by Stock Exchanges [...]" with status "Yes None". p.5, item 10: > "The listed entity is in compliance with Regulation 3(5) & 3(6) of SEBI (Prohibition of Insider Trading) Regulations, 2015." "Yes None". The p.3 violations table reads "NONE/NIL". [FILED]
  - Comment: these filed statements cover actions against the listed entity, its promoters, directors and subsidiaries. They do not address a SEBI order against third parties. Whether an Oct-2025 order was directed at the company or at others is NOT DISCLOSED in the corpus.
- **Insider-trading allegations tied to coupling: one mention only, [MGMT].** Analyst Meet Investor Presentation, 24-Jul-2026, p.24: > "Lack of transparency in the entire process : Market design concerns remained unresolved; shadow pilot report undisclosed; July'25 Order tainted by insider trading allegations"
  - Comment: the phrase stands alone, with no named party, forum, date, or source. The 24-Jul-2026 transcript (Rohit Bajaj, pp.19 to 22) lists the APTEL grounds but does not say "insider" (grep: zero hits in all four transcripts). No filed document repeats the allegation.
- **Adjacent filed item, not linked by the company to coupling or SEBI** (reported for completeness; do not read it as the SEBI matter):
  - FY26 AR, standalone Note 46, p.224 [FILED, STANDALONE]: > "46. During the year, the Company received a whistle blower complaint relating to alleged conflict of interest and potential diversion of business involving certain officials. The Audit Committee has initiated an independent investigation, which remains ongoing as at the date of approval of the standalone financial statements by the Board, which do not have a material impact on the standalone financial statements. Hence, no adjustment has been considered necessary in the standalone financial statements."
  - FY26 AR, CARO annexure to the standalone auditor's report, clause (xi)(c), p.177 [FILED]: > "the Company has received a whistle blower complaint during the year, which has been considered by us while determining the nature, timing and extent of audit procedures. Further, such complaint in respect of which investigation is ongoing as on the date of our audit report do not have a material impact on the financial statements. Also, refer Note 46 [...]"
  - Comment: neither text names coupling, CERC, SEBI, or insider trading. Any link is NOT DISCLOSED. Pointer: FY26 AR Note 46 and the Audit Committee section of the Corporate Governance Report.

---

## B4. Contingent liability, legal-cost provision, or regulatory-matter note

- **Standalone Note 39 "Contingent liabilities", FY26 AR p.217 [FILED, STANDALONE]:**
  > "39. Contingent liabilities The Sales Tax Officer (Adjudicating Authority-GST Delhi) issued an order dated 28 August 2024 raising a demand of the Tax amount of `260.71 along with Interest of `216.97 and penalty of `26.08, against which the Company had filed an appeal before the Appellate Authority, Delhi – Goods and Service Tax. As on date, the matter is pending for hearing before Authority. While the ultimate outcome of the above-mentioned appeals cannot be ascertained at this time, based on current knowledge of the applicable law, management believes that matter raised by department is not tenable and highly unlikely to be retained and accordingly believe that no amount will be payable to the concerned authorities."
  Comment: the note holds only the GST matter (Rs lakh). It carries no coupling, APTEL, or Supreme Court item.
- **Consolidated Note 38 "Contingent liabilities", FY26 AR p.279 [FILED, CONSOLIDATED]:** the same GST text word for word ("38. Contingent liabilities The Sales Tax Officer (Adjudicating Authority-GST Delhi) issued an order dated 28 August 2024 [...]"). Note: the consolidated contingent note is numbered 38, not 39. It holds no coupling item.
- **Auditor's report, Rule 11(e)(i), standalone, p.174 [FILED]:** > "The Company, as detailed in note 39 to the standalone financial statements, has disclosed the impact of pending litigations on its financial position as at 31 March 2026;" Comment: the litigation reference points only to Note 39 (GST). It does not point to Note 47.
- **Regulatory-matter notes:** standalone Note 47 (p.224) and consolidated Note 53 (p.291) are quoted in full at B1.2(e) and (f). They are narrative only. They state no provision, no amount, no contingent-liability classification, and no financial-impact assessment. A provision or quantified exposure for coupling is NOT DISCLOSED. Pointer: FY26 AR Notes 47 and 53, and the provisions note.
- **Legal and professional expense [FILED]:**
  - Standalone Note 33 "Other expenses", p.212: > "Legal and professional * 1,210.26 628.88" (Rs lakh, FY26 vs FY25). The footnote (p.213) reads: > "* Include Payment to Auditor's as follows" with a total of 36.64 (FY25: 40.82).
  - Consolidated Note 32 "Other expenses", p.274: > "Legal and professional * 1,211.68 629.35".
  - MD&A, "Detail analysis of operating expenses", p.65: > "Other operating expenses increased by 43.42% from `1,625.91 lakh in FY'25 to `2,331.80 lakh in FY'26, mainly due to increase in legal & professional related expenses from `628.88 lakh in FY'25 to `1,210.26 lakh in FY'26. Legal & Professional related expenses were mainly incurred for business consultancy, Audit Fee, Listing related fee, legal & advisory service and other associated professional services etc."
  - Comment: the line nearly doubled, up Rs 581 lakh. The company attributes it to consultancy, audit, listing, and "legal & advisory service". It does not split out the APTEL or Supreme Court litigation cost. That split is NOT DISCLOSED. Pointer: FY26 AR standalone Note 33 and MD&A p.65.
- **Results filings:** no contingent-liability or legal-matter note in the FY26 Q4 or Q1FY27 results (see B1.4). NOT DISCLOSED. Pointer: results "Notes".

---

## CLOSING

**Documents quoted (filename, document date):**
- `annual-report__Annual_Report_2025.txt`: FY25 AR; Board's Report 08-Aug-2025; cover letter 18-Aug-2025; financial statements signed 24-Apr-2025. Pages 17, 55, 59, 80/81.
- `annual-report__Annual_Report_2026.txt`: FY26 AR; Board's Report and MD&A 23-Jul-2026; BSE cover letter 14-Aug-2026. Pages 32, 58, 61 to 62, 65, 82 to 83, 120, 174, 177, 212 to 213, 217, 224, 274, 279, 291.
- `announcements__Rumour_Verification_Reply_2026-04-20.txt`: 20-Apr-2026. Pages 1 to 2.
- `announcements__Secretarial_Compliance_Report_FY26_2026-05-15.txt`: 15-May-2026. Pages 3, 5, 6.
- `results__FY26_Q4_Audited_Results_2026-04-23.txt`: 23-Apr-2026. Checked; no coupling text. Pages 1 to 2 are unreadable (cipher).
- `results__Q1FY27_Results_Unaudited_2026-07-23.txt`: 23-Jul-2026. Checked; no coupling text.
- `other__Concall_Nov_2025_Q2FY26_Transcript.txt`: Q2FY26 call 31-Oct-2025, filed 07-Nov-2025.
- `concalls__Concall_Feb_2026_Transcript.txt`: Q3FY26 call 30-Jan-2026, filed 05-Feb-2026.
- `concalls__Concall_Apr_2026_Transcript.txt`: Q4FY26 call 24-Apr-2026, filed 30-Apr-2026.
- `concalls__Concall_Jul_2026_Transcript.txt`: Q1FY27 Analyst Meet 24-Jul-2026, filed 31-Jul-2026.
- `presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt`: 24-Jul-2026. Pages 24 to 25.
- Checked with no coupling text: `presentation__Investor_Presentation_Q4FY26_2026-04-23.txt`, `announcements__FY26_Q4_Press_Release_2026-04-23.txt`, `results__Q1FY27_Press_Release_2026-07-23.txt`, all `announcements__Power_Market_Update_*.txt`, SAST, IGX DRHP, ICX incorporation, Large Corporate, BRSR.

**Conflicts flagged (reported, not reconciled):**
1. Next SC hearing: "August 03, 2026" (FY26 AR p.62) vs "Monday (27th July)" (Analyst Meet p.21, Rohit Bajaj).
2. Draft comment deadline: "16th May 2026" (Q4FY26 call p.5 to 6) vs "June 5th 2026" (Analyst Meet deck p.25).
3. Impact: "may be about 20, 30, 40% (in DAM)" (Analyst Meet p.5, Goel) vs "I don't see any loss in market share" (Analyst Meet p.35, Goel) vs "retain a significant part of the market share in this DAM segment" (Q4FY26 p.14) vs "impact of market coupling would be minimal" (FY26 AR p.62).
4. Rumour reply of 20-Apr-2026 answers "Not Applicable" to legal proceedings, while the FY26 AR records an SC civil appeal filed 10-Apr-2026.
5. MCO design: round-robin with exchanges as rotating MCO (FY25 AR p.55; Q3FY26 p.12, Goel) vs Grid-India as sole MCO in the 17-Apr-2026 draft (FY26 AR p.58; Q4FY26 p.11). Management itself describes this as a CERC change of stance ("they have changed their decision"), so it may be a sequence rather than a contradiction. It is listed for completeness.

**NOT DISCLOSED, with pointers:**
- 9-Jan-2026 corrigendum: absent everywhere. Pointer: FY26 AR MD&A p.58, Board's Report p.83, Reg 30 announcements for Jan-2026 (not in corpus).
- Reg 30 intimations of the 23-Jul-2025 order, the 13-Feb-2026 APTEL judgment, and the 10-Apr-2026 SC appeal: not in corpus. Pointer: BSE/NSE announcement archive for those dates.
- Coupling notes in FY25 financial statements (signed before the order), the FY26 Q4 results, and the Q1FY27 results: absent. Pointer: the respective "Notes".
- Coupling as a KAM or emphasis of matter: absent. Pointer: FY26 AR auditor's reports (KAM = revenue recognition only).
- Implementation date after Jan-2026: absent. Pointer: final Second Amendment Regulations (not issued).
- Meaning of "20, 30, 40%": absent. Pointer: Analyst Meet audio, 24-Jul-2026.
- Quantified fee or volume impact: absent. Pointer: FY26 AR MD&A p.61 to 62; concall Q&A.
- SEBI interim order Oct-2025: absent. Pointer: FY26 AR CG Report p.120; Secretarial Compliance Report p.6 item 11 (both report no SEBI action against the entity, promoters, directors or subsidiaries).
- Source and detail of the "insider trading allegations": absent beyond the one deck phrase. Pointer: Analyst Meet deck p.24.
- Any link between the Note 46 whistle-blower complaint and coupling or SEBI: absent. Pointer: FY26 AR Note 46, p.224.
- Coupling provision, contingent liability, or quantified exposure: absent (Note 39 / consolidated Note 38 = GST only). Pointer: FY26 AR Notes 39, 38 (consolidated), 47, 53.
- Coupling litigation cost split out of Legal & professional (Rs 1,210.26 lakh standalone): absent. Pointer: FY26 AR Note 33, MD&A p.65.
- Text of the 17-Apr-2026 draft regulations and of Grid India's comments: not in corpus. The Analyst Meet deck p.25 list after "Grid India made following observations:" did not extract. Pointer: CERC website (live web, PENDING LIVE VERIFICATION) and the deck PDF p.25 image.

---

# IEX corpus extraction, PART C: entity map and share count

Corpus-only. No web. Source text dir: `runs/iex-2026-09-08/work/` (main checkout). Page = the `=== PAGE n ===` marker in the extracted text, not the printed folio. AR figures in Rs lakhs as printed. Tier: [FILED] = AR, results filing, exchange announcement, SEBI-filed prospectus, shareholding pattern; [MGMT] = concall, presentation, press release.

Short names used below:
- AR26 = `annual-report__Annual_Report_2026.txt` (FY26 AR, filed BSE 14-Aug-2026)
- AR25 = `annual-report__Annual_Report_2025.txt` (FY25 AR, cover letter dated August 18, 2025)
- Q1R = `results__Q1FY27_Results_Unaudited_2026-07-23.txt`
- Q4R = `results__FY26_Q4_Audited_Results_2026-04-23.txt`
- Q1PR = `results__Q1FY27_Press_Release_2026-07-23.txt`
- Q4PR = `announcements__FY26_Q4_Press_Release_2026-04-23.txt`
- DRHPI = `announcements__IGX_DRHP_Filing_Intimation_2026-07-15.txt`
- ICXL = `announcements__Indian_Coal_Exchange_Incorporation_2026-06-01.txt`
- IGXP = `prospectus__IGX_Draft_Abridged_Prospectus_2026-07.txt` (abridged prospectus, refers to the DRHP dated July 14, 2026)
- AM = `presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt`; P4 = `presentation__Investor_Presentation_Q4FY26_2026-04-23.txt`
- CC-Nov25 = `other__Concall_Nov_2025_Q2FY26_Transcript.txt`; CC-Feb26, CC-Apr26, CC-Jul26 = `concalls__Concall_{Feb,Apr,Jul}_2026_Transcript.txt`
- SHP-<date> = `.claude/worktrees/iex-extract/runs/iex-2026-09-08/inputs/shareholding/Shareholding_Pattern_<date>.xml`

---

## C1. Legal entities, IEX % holding, carrying value

### C1.1 Entity list (FY26 year-end and latest)

- AR26 p73 [FILED]: "As on March 31, 2026, your Company had one wholly owned subsidiary and one associate company. Further, no Company ceased to be subsidiary or associate or joint venture of the Company during FY'26."
  Comment: at 31-Mar-2026 there is 1 subsidiary (ICX) and 1 associate (IGX). No JV.
- AR26 p130 (BRSR, section V, item 23) [FILED]: "1. ICX Private Limited (formerly known as International Carbon Exchange Private Limited) Subsidiary 100% No / 2. Indian Coal Exchange Limited* Subsidiary 100% No / 3. Indian Gas Exchange Limited Associate 47.28% No" and "* This entity was incorporated after the close of FY'26, on June 1, 2026."
  Comment: this is the latest entity list in an annual filing. There are three entities.
- Q1R p8 (auditor review report, Annexure 1) [FILED]: "Subsidiaries 1) ICX Private Limited (formerly International Carbon Exchange Private Limited) 2) Indian Coal Exchange Limited (w.e.f 01 June 2026) Associate 1) Indian Gas Exchange Limited"
  Comment: this is the consolidation perimeter at 30-Jun-2026.
- Name as printed. AR26 p73 [FILED]: "the name of the Company was changed from International Carbon Exchange Private Limited to ICX Private Limited. This change was carried out pursuant to the approval granted by the Registrar of Companies, Ministry of Corporate Affairs, and became effective from February 18, 2026."
  Comment: the entity is "International Carbon Exchange Private Limited", renamed "ICX Private Limited" on 18-Feb-2026. It is not "Indian Carbon Exchange". Q1PR p3 [MGMT] still says "International Carbon Exchange (ICX)".

### C1.2 ICX Private Limited (subsidiary)

| Date | IEX % | Standalone carrying value (Rs lakh) | Source |
|---|---|---|---|
| 31-Mar-2024 | 100% (by implication of the wholly owned status; see quote) | 500.00 | AR25 p188 |
| 31-Mar-2025 | 100.00 | 500.00 | AR25 p83 (AOC-1), AR25 p188 |
| 31-Mar-2026 | 100.00 | 500.00 | AR26 p86 (AOC-1), AR26 p197 |
| 30-Jun-2026 | subsidiary (Q1R p8) | NOT DISCLOSED | see pointer |

- AR26 p197, Note 6 Investments [FILED]: "B) Investments in ICX Private Limited (Subsidiary) (formerly International Carbon Exchange Private Limited) Equity Instruments (Unquoted) 500.00 500.00 / 5,000,000 (31 March 2025: 5,000,000) shares of `10 each fully paid up"
  Comment: carried at cost. FY26 and FY25 are both Rs 500.00 lakh.
- AR25 p188, Note 6 [FILED]: "B) Investments in International Carbon Exchange Private Limited (Subsidiary) Equity Instruments (Unquoted) 500.00 500.00 / 5,000,000 (31 March 2024: 5,000,000) shares of ` 10 each fully paid up"
  Comment: FY24 is Rs 500.00 lakh.
- AR26 p86, AOC-1 Part A [FILED]: "4. Date since when subsidiary was acquired/incorporated December 27, 2022 ... 15. % of shareholding 100.00"
- AR25 p83, AOC-1 Part A [FILED]: "15. % of shareholding 100.00"
- AR25 p71 [FILED]: "International Carbon Exchange (ICX), a wholly owned subsidiary of Indian Energy Exchange Limited (IEX), was incorporated on December 27, 2022, with an authorized equity share capital of ` 10 Crores and a paid-up equity share capital of ` 5 Crores."
  Comment: the FY24 % is not printed as a number. It rests on the "wholly owned since incorporation" wording and on no change being reported.
- 30-Jun-2026 carrying value: NOT DISCLOSED. The Q1FY27 results (Q1R) carry no balance sheet. It would be in the H1FY27 results statement of assets and liabilities (not in corpus).

### C1.3 Indian Gas Exchange Limited (associate)

| Date | IEX % | Shares held | Standalone carrying value, cost (Rs lakh) | Consolidated equity-method carrying value (Rs lakh) |
|---|---|---|---|---|
| 31-Mar-2024 | 47.28% | 35,460,000 | 3,546.00 | 6,105.64 |
| 31-Mar-2025 | 47.28% | 3,54,60,000 | 3,546.00 | 7,574.70 |
| 31-Mar-2026 | 47.28% | 3,54,60,000 | 3,546.00 | 9,025.09 |
| DRHP date (Jul-2026) | 47.28 | 35,460,000 | NOT DISCLOSED | NOT DISCLOSED |

- AR26 p197, Note 6 [FILED]: "A) Investments in Indian Gas Exchange Limited (Associate) Equity Instruments (Unquoted) 3,546.00 3,546.00 / 35,460,000 (31 March 2025: 35,460,000) shares of `10 each fully paid up"
- AR25 p188, Note 6 [FILED]: "A) Investments in Indian Gas Exchange Limited (Associate) Equity Instruments (Unquoted) 3,546.00 3,546.00 / 35,460,000 (31 March 2024: 35,460,000) shares of ` 10 each fully paid up"
- AR26 p86, AOC-1 Part B [FILED]: "2. Date on which the Company became Associate: January 17, 2022 ... Number of Shares 3,54,60,000 / Amount of Investment in Associate (In ` Lakh) 3,546 / Extend of holding % 47.28%"
- AR25 p83, AOC-1 Part B [FILED]: "Number of Shares 3,54,60,000 / Amount of Investment in Associate (In ` Lakh) 3,546 / Extend of holding % 47.28%"
- AR25 p63 (MD&A) [FILED]: "As on March 31, 2025, Indian Energy Exchange holds 47.28% (previous year 47.28%) stake in Indian Gas Exchange."
  Comment: this is the FY24 holding anchor.
- AR26 p291, consolidated Note 54 [FILED]: "Indian Gas Exchange Limited (IGX) India 47.28% Equity 9,025.09 7,574.70 Gas Exchange" and "Opening balance 7,574.70 6,105.64 / Company's share in profit after tax of IGX for the year 1,979.53 1,463.15 / Distribution received from IGX (531.90) - / Company's share in other comprehensive income (net of tax) for the year 2.76 5.91 / Carrying amount of retained interest 9,025.09 7,574.70"
  Comment: the FY25 opening balance of Rs 6,105.64 lakh is the FY24 year-end equity-method carrying value.
- AR26 p246 (consolidated, corporate info) [FILED]: "IGX was subsidiary (52.21%) of Indian Energy Exchange Limited (IEX) till 16 Jan 2022. After 16 Jan 2022, IGX became an Associate (47.28%) of IEX."
  Comment: CONFLICT on the date. AOC-1 (AR26 p86) says it became an associate on "January 17, 2022". Note p246 says "After 16 Jan 2022". The two are compatible in substance. Reported as printed.
- IGXP p5 (pre-offer shareholding as at the DRHP date) [FILED]: "Indian Energy Exchange Limited# 35,460,000 47.28" and "Total 75,000,000 100.00"
  Comment: 47.28% at the DRHP date (July 14, 2026). This is the latest filed holding.
- AR26 p74 [FILED]: "Having reduced its shareholding in IGX to 47.28%, IEX continues to pursue the requisite dilution of its stake"
- CONFLICT (management rounding): CC-Feb26 p13 [MGMT]: "our holding in the gas exchange is 47.5%". CC-Nov25 p11 [MGMT] (analyst question): "IEX stake in IGX equity stake, which is around 47.5%". CC-Jul26 p5 [MGMT] and Q1PR p2 [MGMT]: "47.3%". Filed figure is 47.28%.
- IGX ESOS Trust (an IGX-level trust, not an IEX entity). IGXP p6 [FILED]: "7. IGX ESOS Trust 969,600 1.29"
- Other IGX holders at the DRHP date. IGXP p5-6 [FILED]: "NSE Investments Limited 18,562,500 24.75"; ONGC, GAIL, Torrent Gas, Adani Total Gas and IOC each "3,693,750 4.92".

### C1.4 Indian Coal Exchange Limited (coal-exchange vehicle)

- ICXL p1 [FILED]: "Indian Energy Exchange Limited ('IEX /The Company ') has incorporated a wholly owned subsidiary company in the name of "Indian Coal Exchange Limited " on June 01, 2026, having the Corporate Identity Number U66190DL2026PLC467125."
- ICXL p2, Annexure A, item 8 [FILED]: "100% shareholding of Indian Coal Exchange Limited is held by the Company."
- Holding at FY24, FY25, FY26: not applicable. The entity did not exist before 1-Jun-2026 (AR26 p130 footnote).
- Carrying value: NOT DISCLOSED. No standalone balance sheet after incorporation is in the corpus. It would appear in the H1FY27 standalone statement of assets and liabilities, or in the FY27 AR Note 6 Investments.

### C1.5 Other holdings and trusts

- IEX ESOP Trust. AR26 p186 [FILED]: "The IEX ESOP trust ("ESOP Trust") has been treated as an" [line continues on the same page] "... taken to the ESOP Trust reserve." AR26 p228, Note 51 [FILED]: "the Company allotted 606,572 number of equity shares of `10 each (post sub division equivalent to 6,065,720 of Rs 1 each) to IEX ESOP Trust ("ESOP Trust") which administers ESOP 2010 on behalf of the Company."
  Comment: the trust is consolidated into the standalone accounts. IEX's shares held by the trust are deducted from share capital (see C5). The trust holds no % of any subsidiary.
- Enviro Enablers India Private Limited (strategic investment, not a subsidiary or associate). AR26 p198, Note 6 [FILED]: "A) Investments in Enviro Enablers India Private Limited (Strategic investment) 10% Series Seed Compulsorily Convertible Preference shares (Unquoted) 122.22 122.22 / 439,310 (31 March 2025: 439,310) shares of face value of `10 each"
  Comment: FVTPL. Rs 122.22 lakh at FY26 and FY25. The IEX % holding is NOT DISCLOSED. It would be in the EEIPL cap table, which is not in corpus.
- Promoter. AR26 p206, Note 17(g) [FILED]: "Promoter shareholding as on 31 March 2026 is Nil (previous year : Nil)."

---

## C2. IGX financials and sell-down

### C2.1 Restated IGX standalone financials from the SEBI-filed abridged prospectus (Rs million)

IGXP p7, "Summary of Restated Financial Information" [FILED], columns FY26 / FY25 / FY24:
- "Equity Share capital 740.30 739.33 739.03"
- "Revenue from Operations(1) 610.05 488.01 348.49"
- "Profit After Tax (2) 420.22 307.93 230.50"
- "Total Equity(6) 1,790.34 1,477.12 1,166.56"
- "Net Worth(7) 1,790.34 1,477.12 1,166.56"
- "Return on Net Worth(9) (%) 23.47 20.85 19.76"
- "Total Borrowings - - -"

IGXP p8, KPI table [FILED]:
- "Total Income(2) ₹ in million 848.39 690.82 546.19"
- "Profit Before Tax(3) ₹ in million 558.25 403.04 307.17"
- "EBITDA Margin(7) % 96.07 94.44 97.33"

Comment: these are the only filed IGX figures that cover FY24, FY25 and FY26 on one basis. AM p32 [MGMT] repeats the PAT bars "230.50 307.93 420.22 ... FY24 FY25 FY26 PAT (in million)".

### C2.2 IGX figures from IEX filings

- AR26 p73 [FILED]: "IGX's total revenue for FY'26 stood at `79 Crores and a net profit after tax of `41.9 Crores. The share of profit of IGX considered in consolidation for FY'26 amounted to `19.8 Crores."
- AR25 p71 [FILED]: "IGX's total income for FY'25 stood at ` 6908.21 lakhs and a net profit after tax of ` 3094.66 lakhs. The share of profit of IGX considered in consolidation for FY'25 amounted to ` 1463.15 lakhs."
- AR26 p86, AOC-1 Part B [FILED]: "7. Net Worth attributable to Shareholding as per latest audited Balance Sheet (In ` Lakh) 8,464.81 / 8. Profit /(Loss) for the year (In ` Lakh) i. Considered in Consolidation 1,979.53 ii. Not Considered in Consolidation 2,207.30"
- AR25 p83, AOC-1 Part B [FILED]: "6. Net Worth attributable to Shareholding as per latest audited Balance Sheet (In ` Lakh) 7,035.70 / 7. Profit /(Loss) for the year (In ` Lakh) i. Considered in Consolidation 1,463.15 ii. Not Considered in Consolidation 1,631.51"
  Comment: the AOC-1 gives IEX's attributable net worth, not IGX total net worth. No computation is made here.
- AR26 p66 [FILED]: "During FY'26, the Company received a dividend from its associate company amounting to `531.90 lakh (previous year: Nil)."
- Q4PR p3 [MGMT]: "IGX recorded a profit after tax of INR. 41.9 Crore in FY'26, higher by 35% compared with INR. 30.9 Crore in FY'25."
- CONFLICT (IGX FY26 revenue). AR26 p73 gives "total revenue ... `79 Crores". IGXP p7-8 gives revenue from operations Rs 610.05 mn and total income Rs 848.39 mn. Neither IGXP figure equals Rs 79 crore as printed. Not reconciled.
- CONFLICT (IGX FY26 PAT). AR26 p73 and Q4PR p3 give Rs 41.9 crore (audited). IGXP p7 gives Rs 420.22 mn (restated). AM p40 [MGMT] gives "IGX FY26 PAT 42 Cr".
- CONFLICT (IGX FY25 PAT). AR25 p71 gives Rs 3,094.66 lakh (audited). IGXP p7 gives Rs 307.93 mn (restated).
- IGX FY24 revenue, PAT, net worth from IEX's own filings: NOT DISCLOSED in AR25 (it gives only the "previous year" share of profit, Rs 1,089.79 lakh, at AR25 p63). The pointer is the FY24 AR AOC-1 Part B, which is not in corpus. IGXP p7 covers FY24 (above).

### C2.3 IGX Q1FY27

- Q1PR p2 [MGMT]: "For Q1 FY'27 IGX recorded a profit after tax of Rs. 16.3 Crore, higher by 15.5% compared with Rs. 14.1 Crore in Q1FY'26."
- Q1R p9, consolidated [FILED]: "6 Share in profit of associate (net of tax) 771 88 441.39 668.26 1,979.53"
  Comment: the columns are Q1FY27 / Q4FY26 / Q1FY26 / FY26, in Rs lakh. The OCR prints "771 88", which reads as 771.88.
- IGX Q1FY27 revenue: NOT DISCLOSED. Q1PR p2 gives volume (27.5 million MMBtu) and PAT only. It would be in an IGX quarterly statement, or in an updated RHP/DRHP addendum. Neither is in corpus.
- IGX Q1FY27 net worth: NOT DISCLOSED. The same pointer applies.

### C2.4 PNGRB ceiling, timetable, DRHP, OFS

- Ceiling. AR26 p74 [FILED]: "in terms of the Gas Exchange Regulations, no single entity is permitted to hold more than 25% of the equity share capital of a Gas Exchange beyond five years from the date of authorization. Accordingly, IEX was required to reduce its shareholding in IGX to 25% on or before December 2, 2025."
- Authorisation date. AR26 p73 [FILED]: "IGX received authorization from the Petroleum and Natural Gas Regulatory Board ("PNGRB") on December 2, 2020, under Regulation 11 of the PNGRB (Gas Exchange) Regulations, 2020"
- Extension. AR26 p74 [FILED]: "PNGRB has granted an extension until December 31, 2026, to reduce IEX's shareholding to the prescribed limit of 25%."
- Post-IPO target. AR26 p74 [FILED]: "Upon completion of the IPO, IEX's shareholding in IGX will be reduced to 25%, in compliance with the applicable regulatory requirements."
- DRHP date and OFS size. DRHPI p1 [FILED]: "has filed a draft red herring prospectus dated July 14, 2026 ("DRHP"), with the Securities and Exchange Board of India and BSE Limited on July 14, 2026 ... The Offer comprise s of an offer for sale of up to 16,710,000 equity shares by IEX". DRHPI refers to a prior "intimation dated December 03, 2025", which is not in corpus.
- IGXP p1 [FILED]: "Offer for Sale of up to 16,710,000 Equity Shares of face value of ₹10 each aggregating up to ₹ [●] million". Fresh issue: "Not Applicable". IEX weighted average cost of acquisition: "10.00" Rs per share. Listing: "proposed to be listed on BSE Limited".
- OFS value and price band: NOT DISCLOSED. IGXP p1 and p5 print "[●]". These will appear in the RHP, which is not in corpus.
- OFS as %. Q1PR p2 [MGMT]: "The Offer comprises an offer for sale of 22.3% equity shares by IEX." CC-Jul26 p5 [MGMT]: "we took an extension of one year from the PNGRB. And therefore, to sell this 22.3% equity, we have offered that in the IPO."
- Earlier management statements. CC-Nov25 p11 [MGMT]: "As per the PNGRB regulations, we have to bring down the equity to 25% by December 2025. ... We have applied to PNGRB for extension of this time". AR25 p34 [FILED]: "IEX has to dilute its equity stake in IGX by the end of December 2025 and is exploring options for further divestment."

---

## C3. ICX: revenue, PAT, I-REC issuance

### C3.1 Revenue and PAT

| Period | Revenue | PAT | Source, tier |
|---|---|---|---|
| FY24 | NOT DISCLOSED | loss Rs 155.61 lakh | AR25 p63 [FILED] |
| FY25 | turnover Rs 189.22 lakh / "2.1 Crores" / "3.4 crore" (CONFLICT) | Rs (11.07) lakh | AR25 p83, AR25 p71 [FILED]; Q4PR p3 [MGMT] |
| FY26 | turnover Rs 726.13 lakh / total revenue Rs 7.71 crore | Rs 473.70 lakh / Rs 4.74 crore | AR26 p86, p73 [FILED] |
| Q1FY27 | Rs 2.1 crore | NOT DISCLOSED | Q1PR p3 [MGMT] |

- AR26 p86, AOC-1 Part A [FILED]: "5. Share capital 500.00 / 6. Reserves & Surplus 304.41 / 7. Total Assets 921.00 / 8. Total Liabilities 116.59 / 9. Investments 738.80 / 10. Turnover 726.13 / 11. Profit/Loss before Taxation 628.13 / 12. Provision for Taxation 154.43 / 13. Profit/Loss after Taxation 473.70"
- AR26 p73 [FILED]: "During FY'26, ICX delivered a good financial performance, generating total Revenue of `7.71 crore, with Profit After Tax amounting to `4.74 crore."
- AR26 p66 [FILED]: "During FY'26, ICX recorded profit amounting `473.70 lakhs against `11.07 lakhs loss for FY'25."
- AR25 p83, AOC-1 Part A [FILED]: "5. Share capital 500.00 / 6. Reserves & Surplus (172.52) / 7. Total Assets 574.87 / 8. Total Liabilities 247.39 / 9. Investments 112.58 / 10. Turnover 189.22 / 11. Profit/Loss before Taxation (30.57) / 12. Provision for Taxation (19.50) / 13. Profit/Loss after Taxation (11.07)"
- AR25 p63 [FILED]: "During current year FY'25, ICX incurred loss amounting ` 11.07 lakhs against ` 155.61 lakhs loss for FY24."
- AR25 p71 [FILED]: "ICX commenced IREC operations in the same month and, within seven months of FY 2024–25, generated ` 2.1 Crores in revenue, comprising ` 1.32 Crores from certificate issuance and ` 0.78 Crores from device registration."
- Q4PR p3 [MGMT]: "ICX made revenue of INR 7.7 crore in FY'26, as compared to INR 3.4 crore in FY'25, achieving growth of 126% YoY."
- Q1PR p3 [MGMT]: "ICX made revenue of Rs 2.1 crore in Q1FY'27, as compared to Rs 1.8 crore in Q1FY'26, achieving growth of 16.1% YoY."
- CC-Apr26 p8 [MGMT]: "Revenue for ICX during the quarter stood at INR 2.2 crores and INR 7.7 crores for the full year, respectively."
- CC-Feb26 p7 [MGMT]: "Revenue for ICX in Q3 FY '26 stood at Rs. 1.8 crores and Rs. 5.5 crores for the first nine-month period, respectively."
- CC-Nov25 p8 [MGMT]: "Revenue for ICX in Q2 FY '26 stood at Rs. 193 lakhs."
- AM p40 [MGMT]: "ICX FY26 PAT 5 Cr PAT-positive · 84% ROE"
- CONFLICT (ICX FY25 revenue). Three figures: AOC-1 turnover Rs 189.22 lakh (AR25 p83), "` 2.1 Crores in revenue" (AR25 p71), and "INR 3.4 crore in FY'25" (Q4PR p3). Not reconciled.
- CONFLICT (ICX FY26 revenue label). AOC-1 "Turnover 726.13" lakh (AR26 p86) against "total Revenue of `7.71 crore" (AR26 p73). The two may use different definitions (turnover against total revenue). Not reconciled.
- ICX FY24 revenue: NOT DISCLOSED. The pointer is the FY24 AR AOC-1 Part A, which is not in corpus. AR25 p71 says I-REC operations began in September 2024.
- ICX Q1FY27 PAT: NOT DISCLOSED. Q1PR p3 gives revenue and I-REC count only. Q1R has no subsidiary split. It would be in an ICX quarterly statement, which is not in corpus.

### C3.2 I-REC issuance

- FY25. AR25 p51 [FILED]: "In FY'25, a total of 59 lakh I-RECs were issued by ICX." AR25 p133 (BRSR) [FILED]: "around 59.27 Lakhs I-REC (E) in FY'25 after due verification".
- FY26. AR26 p53 [FILED]: "In FY'26, a total of 1.79 crore I-RECs were issued by ICX over 614 devices that have been registered and represent more than 9 GW (9,289 MW) of clean energy capacity." AR26 p53 [FILED]: "During FY'26, the redemption of 1.51 crore I-RECs". Q4PR p3 [MGMT]: "During FY'26, ICX issued 179 lakh I-REC, recording a growth of over 200% compared with FY'25."
- Q1FY27. Q1PR p3 [MGMT]: "In Q1FY'27 the International Carbon Exchange (ICX) issued 42.4 lakh I-RECs as compared to 44.4 lakh I-RECs in Q1FY'26."
- Quarterly FY26 [MGMT]. CC-Nov25 p8: "ICX, issued 38 lakhs I-RECs, adding to a cumulative of 82 lakh I-REC issuances in the first half of FY '26". CC-Feb26 p7: "ICX, issued 51 lakh I-RECs, higher by 219% compared with Q3 FY '25. For the first nine months of FY '26, cumulative 133 lakh I -RECs were issued". CC-Apr26 p8: "ICX issued 46 lakh I-RECs, higher by 29% compared with quarter four of financial year '25."
- CONFLICT (market against ICX issuance). AR26 p30 [FILED]: "the India I-REC(E) market recorded a 53% year-on-year increase in certificate issuances, rising from 12.01 million certificates in FY'25 to 18.41 million certificates in FY'26." Against this, ICX issued 59 lakh (FY25) and 1.79 crore (FY26) per AR25 p51 and AR26 p53. AR26 p135 says ICX "is the authorized local Issuer of International Renewable Energy Certificates (I-RECs) in India". Scope differences are not stated. Not reconciled.

---

## C4. Coal exchange

- Board in-principle approval. P4 p20 [MGMT]: "IEX Board accords in-principle approval to explore establishinga Coal Exchange, in line with proposed"Coal Regulations2025" issued by the Ministryof Coal." CC-Apr26 p8 [MGMT]: "the IEX Board has accorded in principle approval to explore establishing a coal exchange in line with the proposed Coal Regulations 2025 issued by the Ministry of Coal."
  Comment: the date of the board resolution is NOT DISCLOSED in corpus. ICXL p1 [FILED] cites "In continuation to our intimation dated March 18, 2026". That intimation is not in corpus. AR26 p104 [FILED] lists a Board meeting on "March 18, 2026". No filed text links that meeting to the coal resolution. Pointer: the IEX Reg 30 intimation dated March 18, 2026 (BSE/NSE), not in corpus.
- Incorporation. ICXL p1 [FILED]: incorporated "on June 01, 2026, having the Corporate Identity Number U66190DL2026PLC467125."
- Capital. ICXL p2, item 7 [FILED]: "The shares are subscribed at a face value of Rs. 10/- per equity share. Indian Coal Exchange Limited has been incorporated with an authorized share capital of Rs. 1,00,00,00,000/- (Rupees One Hundred Crores Only), divided into 10,00,00,000 (Ten Crore) equity shares of Rs. 10/- each." ICXL p2, item 6 [FILED]: "The consideration for subscription to the paid-up share capital of the incorporated entity shall be paid in cash."
- AR26 p74 [FILED]: "Indian Coal Exchange Limited has been incorporated with an authorized and paid up share capital of `100 crore, comprising 10 crore equity shares of face value `10 each."
  Comment: CONFLICT. ICXL (1-Jun-2026) states only the authorised capital of Rs 100 crore. The paid-up amount is not stated there. AR26 p74 states "authorized and paid up" of Rs 100 crore. Not reconciled. The actual cash subscribed by IEX to date is NOT DISCLOSED in a financial statement. The pointer is the H1FY27 standalone cash flow and investments, or the FY27 AR Note 6, which are not in corpus.
- Licence status. ICXL p2, item 5 [FILED]: "At the time of incorporation of Indian Coal Exchange Limited, no governmental or regulatory approvals were required. However, it will be required to obtain a license/registration from the designated Regulator once the Draft Coal Exchange Rules, 2025, proposed by the Ministry of Coal are notified and come into force".
- Regulator. AR26 p52 [FILED]: "As per these rules, the Coal Controller Organisation (CCO) shall act as the Regulator for Coal Exchanges."
- Application portal. AM p34 [MGMT]: "The Registration Portal for submitting the Coal Exchange License Application has been launched by the Ministry of Coal and the Coal Controller Organization on 15th July 2026". CC-Jul26 p26 [MGMT]: "on the 15th of July they (Ministry) have come out with the application process where the Coal exchanges can apply for the registration and licensing."
  Comment: whether IEX or Indian Coal Exchange Ltd has submitted an application is NOT DISCLOSED. No licence grant appears in corpus. The pointer is a future Reg 30 intimation, which is not in corpus.
- Rules notification date. AM p34 [MGMT]: "Ministry of Coal notified the Rules for Coal Exchange on 4th June 2026". CC-Jul26 p26 [MGMT]: "the Government come out with the notifications of the Rules on the 4th of June." AR26 p30 [FILED]: "The notification of the Coal Exchange Rules, 2026, following amendments to the Mines and Minerals (Development and Regulation) Act, has established the regulatory framework for exchange-based coal trading."
  Comment: CONFLICT (rule name and year across filings). AR26 p52 [FILED] says "provisions of Coal Exchange Rules, 2025" (proposed). ICXL p2 [FILED] says "Draft Coal Exchange Rules, 2025". AR26 p30 [FILED] says "Coal Exchange Rules, 2026" (notified). Only [MGMT] sources give the 4-Jun-2026 date. No filed document in corpus states the notification date.
- Transition clause. AM p34 [MGMT]: "existing E-Auction Platforms and Marketplaces are allowed to operate only upto 6 months from the operationalization of the 1st Coal Exchange."
- Operational timing. AR26 p53 [FILED]: "the Coal Trading Exchange is anticipated to be operational in FY'27". Management stated no capex or other capital commitment beyond the share capital. Any such commitment is NOT DISCLOSED. The pointer is the AR26 capital commitments / contingent liabilities note, where no coal item was found.

---

## C5. Share count, ESOPs, buyback, dividend, capital allocation

### C5.1 Shares outstanding (standalone, face value Rs 1)

| Date | Issued and paid up | Held by IEX ESOP Trust | Outstanding net of trust | Source |
|---|---|---|---|---|
| 31-Mar-2024 | 891,692,735 | 2,465,310 | 88,92,27,425 | AR25 p197 [FILED] |
| 31-Mar-2025 | 891,692,735 | 2,442,985 | 88,92,49,750 | AR25 p197, AR26 p205 [FILED] |
| 31-Mar-2026 | 891,692,735 | 23,92,445 (2,392,445) | 88,93,00,290 | AR26 p205 [FILED] |
| 30-Jun-2026 | 891,692,735 | 2,392,445 | NOT DISCLOSED as a count | SHP-30_JUN_2026 [FILED] |

- AR26 p205, Note 17 [FILED]: "891,692,735 Equity shares of face value of `1 each (31 March 2025: 891,692,735 Equity shares of face value of `1 each ) 8,916.93 8,916.93 / Less: 23,92,445* Equity shares of face value of `1 each (31 March 2025: 2,442,985* Equity shares of face value of `1 each) held by IEX ESOP Trust (7.98) (8.15) / 8,908.95 8,908.78" and "* Includes 1,594,964 shares (previous year: 1,628,657) bonus equity shares issued to IEX ESOP trust"
- AR26 p205, Note 17(a) [FILED]: "Outstanding at the beginning of the year (face value of `1 each)# 88,92,49,750 8,908.78 88,92,27,425 8,908.71 / Add: Option vested and exercised post bonus issue (refer note 17 (f)) 50,540 0.17 22,325 0.07 / Outstanding at the end of the year ... 88,93,00,290 8,908.95 88,92,49,750 8,908.78" and "# Excluding 2,392,445 shares held by IEX ESOP Trust (previous year 2,442,985 shares)"
- AR25 p197, Note 17 [FILED]: "891,692,735 Equity shares of face value of ` 1 each (31 March 2024: 891,692,735 Equity shares of face value of ` 1 each ) 8,916.93 8,916.93 / Less: 2,442,985* Equity shares ... (31 March 2024: 2,465,310* Equity shares of face value of ` 1 each) held by IEX ESOP Trust (8.15) (8.22)" and "Outstanding at the end of the year ... 88,92,49,750 8,908.78 88,92,27,425 8,908.71"
- CONFLICT (bonus shares held by the trust at FY25). AR25 p197 prints "Includes 1,621,215 shares (previous year: 1,643,540)". AR26 p205 prints the FY25 comparative as "(previous year: 1,628,657)". Not reconciled.
- AR26 p70 (Board's Report) [FILED]: "The paid-up equity shares capital of the Company stood at `8,916.93 Lakhs consisting of 89,16,92,735 equity shares of `1/- each as on March 31, 2026. There has been no change in paid up share capital of the Company during FY'26."
- SHP-31_MAR_2026 [FILED]: `<in-bse-shp:NumberOfShares contextRef="ShareholdingPattern_ContextI" ...>891692735<` and `<in-bse-shp:NumberOfShares contextRef="EmployeeBenefitsTrusts_ContextI" ...>2392445<`
- SHP-30_JUN_2026 [FILED]: `<in-bse-shp:DateOfReport contextRef="MainI">2026-06-30<`, `<in-bse-shp:NumberOfShares contextRef="ShareholdingPattern_ContextI" ...>891692735<`, `<in-bse-shp:NumberOfSharesOnFullyDilutedBasisIncludingWarrantsESOPAndConvertibleSecurities contextRef="ShareholdingPattern_ContextI" ...>891692735<`, and `<in-bse-shp:NumberOfShares contextRef="EmployeeBenefitsTrusts_ContextI" ...>2392445<`
- SHP-30_JUN_2025, SHP-30_SEP_2025 and SHP-31_DEC_2025 [FILED] also report a total NumberOfShares of 891692735 (30_JUN_2025 checked directly).
- Q1R p4 and p9 [FILED]: "Paid-up equity share capital (face value Z 1/- per share) 8,908.95" for Q1FY27. Q1R p5 [FILED]: "During the quarter ended 30 June 2026, no options have been exercised."
- Q1R p9 prints the Q1FY26 column as "/1,908.95" (OCR defect). The figure is not used.

### C5.2 ESOPs (IEX ESOP Scheme 2010, administered by the IEX ESOP Trust)

- Granted in year:
  - FY26. AR26 p229, Note 51(d) [FILED]: "Add: Options granted during the year 1,00,000 143.00". Grant date per AR26 p228: "4 29 July 2025 1,00,000 143".
  - FY25. AR26 p229 prior-year column and AR25 p220 [FILED]: nil granted ("Add: Options granted during the year - -").
  - FY24. AR25 p220 [FILED], FY24 column: "Add: Options granted during the year ... 50,000 149.00 / 60,000 131.00 / 50,000 140.00 / 11,44,000 141.00"
- Outstanding at year-end (including exercisable):
  - 31-Mar-2026. AR26 p229 [FILED]: "Options outstanding as at the end of the year (including exercisable) 40,000 140.00 ... 7,53,760 141.00 ... 1,00,000 143.00"
  - 31-Mar-2025. AR26 p229 / AR25 p220 [FILED]: "50,000 140.00" and "9,48,175 141.00" (and "-" at Rs 131).
  - 31-Mar-2024. AR25 p220 [FILED], FY24 column: "60,000 131.00 / 50,000 140.00 / 11,14,200 141.00"
- Exercisable at year-end:
  - 31-Mar-2026. AR26 p229 [FILED]: "Exercisable at the end of the year (included under option outstanding as well) 10,000 140.00 ... 3,56,510 141.00"
  - 31-Mar-2025. AR26 p229 [FILED], prior-year column: "10,000 140.00" and "2,58,550 141.00".
  - 31-Mar-2024. AR25 p220 [FILED]: the row prints "2,58,550 141.00 39,000 141.00 / 10,000 140.00". Read by column position, FY24 exercisable = 39,000 at Rs 141. The text extraction may lose column layout, so verify against the PDF.
- Exercised. AR26 p229 [FILED]: "For the financial year ended 31 March 2026, 50,540 share options (31 March 2025: 22,325) have been exercised."
- Remaining life. AR26 p229 [FILED]: "a weighted average remaining contractual life of 2.82 years (31 March 2025: 3.75 years)."
- Cost. AR26 p229 [FILED]: "Employee stock option expenses 80.59 164.65" (FY26 / FY25, Rs lakh). AR25 p220 gives FY24 as "5.64".
- RSU. AR26 p70 [FILED]: "Your Company has 'IEX RSU Scheme 2019' with a view to attract and retain key talents working in the capacity of Senior Management". RSU units outstanding at company level: NOT DISCLOSED in the AR26 notes (no RSU reconciliation in Note 51). AR26 p108 [FILED] shows "Outstanding Stock options (ESOP 2010) / (RSU 2019) (in Nos.) as at March 31, 2026 Nil Nil" for the two executive directors only. The pointer is the Regulation 14 SBEB disclosure at iexindia.com/investors/other-disclosures (AR26 p70), which is not in corpus.
- 30-Jun-2026 ESOPs outstanding: NOT DISCLOSED. Q1R p5 states only that no options were exercised in the quarter. The pointer is the FY27 AR Note 51.

### C5.3 Buyback

- Last buyback. AR26 p206, Note 17(d) [FILED]: "the Board of Directors of the Company, at its meeting held on 25 November 2022, approved the buyback of equity shares from the open market route ... amounting to `9,800 (maximum buyback size, excluding buyback tax) at a price not exceeding `200 per share ... completed on 16 March 2023. During this buyback period, the Company purchased and extinguished a total of 6,976,798 equity shares from the stock exchange at a weighted average buyback price of `140.45 per equity share comprising 0.78% of the pre buyback paid up equity share capital"
- Current authorisation: NOT DISCLOSED. No buyback authorisation for FY24 to Q1FY27 appears in the filed documents. AR26 p96 (secretarial audit) [FILED]: "The Securities and Exchange Board of India (Buyback of Securities) Regulations, 2018; (Not Applicable)". A future authorisation would appear in a Reg 30 board-outcome intimation, which is not in corpus.
- Management intent. CC-Apr26 p12 [MGMT], Vineet Harlalka: "buyback has become one of the good options for distributing money to the shareholders. We are definitely considering it." CC-Jul26 p29-30 [MGMT], S. N. Goel: "but buyback, yes definitely, we will consider it in future because now SEBI also has revised its rules for doing the buyback through the market."

### C5.4 Dividend policy and capital allocation

- AR26 p69 [FILED]: "Pursuant to Regulation 43A of SEBI Listing Regulations, your Company has a well-defined Dividend Distribution Policy that balances the dual objective of rewarding shareholders through dividends whilst also ensuring the availability of sufficient funds for the growth of the Company."
- AR26 p69 [FILED]: "The total dividend for the financial year ended March 31, 2026, amounts to `3.5/- per equity share equivalent to 350% of face value of `1/- each and would involve a total cash outflow of `31,209.25 Lakhs, resulting in a dividend payout of approx. 66% of the standalone profit after tax of the Company exceeding the defined dividend range in the Company's Dividend Distribution Policy."
- AR26 p69 [FILED]: interim "`1.50/- (150%) per equity share ... total payout was `13,375.39 Lakhs"; final "`2.00/- (200%) ... aggregates to `17,833.85 Lakhs".
- AR25 p66 [FILED]: "The total dividend for the financial year ended March 31, 2025, amounts to ` 3/- per equity share ... total cash outflow of ` 26,750.79 Lakhs, resulting in a dividend payout of approximately 65% of the standalone PAT of the Company exceeding the defined dividend range in the Company's Dividend Distribution Policy."
- The numeric "defined dividend range": NOT DISCLOSED in corpus. The pointer is the Dividend Distribution Policy PDF at the AR26 p69 web link (doc.iexindia.com/files/Dividend-Distribution-Policyy-LVwOFFFg-6bH.pdf), which is not in corpus.
- CC-Jul26 p27 [MGMT]: "As a policy, we are paying almost around more than 50%, 65% as dividend over the last many years."
- A separate capital-allocation policy (a document distinct from the dividend policy): NOT DISCLOSED. None was found in AR26, AR25, the presentations or the concalls. Pointer: AR26 Board's Report pp.67-80 (searched; not present). AR26 p79 [FILED] states the investment position only: "the Company's investments include `3,546 Lakhs in Indian Gas Exchange Limited (IGX), an associate company; `500 Lakhs in ICX Private Limited ... and approximately `122 Lakhs in Enviro Enablers India Private Limited (EEIPL)."

---

## C6. Ind AS 108 segment reporting

- Standalone FY26. AR26 p224, Note 44 [FILED]: "The Company is a power exchange. The entire operations are governed by similar set of risk and returns. ... Thus, the Company has only one operating segment, and no reportable segments in accordance with Ind AS 108 - Operating Segments."
- Consolidated FY26. AR26 p286, Note 44 [FILED]: "there is only one reportable segment in accordance with the requirements of Ind AS - 108- 'Operating Segments' and accordingly no disclosures have been made as required under Ind AS 108."
- FY25 and FY24 comparatives. AR25 p216 (standalone Note 44) [FILED]: "one operating segment, and no reportable segments in accordance with Ind AS 108 - Operating Segments." AR25 p276 (consolidated Note 44) [FILED]: "is only one reportable segment in accordance with the requirements of Ind AS - 108- 'Operating Segments' and accordingly no disclosures".
- Q4FY26 results. Q4R p9 [FILED]: "The Company is a registered power exchange and the same constitutes a single operating segment. Therefore, there are no other reportable segments in terms of the requirements of Ind AS 108". Q4R p18 (consolidated) [FILED]: "As per the requirements of Ind AS 108- "Operating Segments", there is only one reportable segment."
- Q1FY27 results. Q1R p5 (standalone note 3) and Q1R p10 (consolidated note 3) [FILED] repeat the same wording, although Indian Coal Exchange Ltd is now consolidated.
- IGX (its own segment position). IGXP p3 [FILED]: "We have one operating segment, and have no reportable segments in accordance with Ind AS 108 - Operating Segments."
- Revenue and result per segment: NOT DISCLOSED (single segment). The nearest filed split is a product disaggregation of transaction fees, not a segment report. AR26 p211, Note 28 [FILED]: "Electricity (comprising RTM, DAM, TAM, Green Segments) 55,851.37 47,833.81 / Certificates (comprising REC, Escerts Segments) 2,545.07 3,520.71 / Total 58,396.44 51,354.52" (FY26 / FY25, Rs lakh, standalone). No result (profit) split exists.
- The consolidated PAT contribution by entity is available as a Schedule III table, not a segment report. AR26 p292, Note 55 [FILED]: Holding company "47,370.79"; ICX "473.70"; IGX (associate) "1,979.53"; eliminations "(531.90)"; total "49,292.12" (FY26 share in profit, Rs lakh).

---

## CLOSING

Documents quoted, with dates:
- annual-report__Annual_Report_2026.txt: FY26 AR, filed BSE 14-Aug-2026. Board's Report AOC-1 signed July 23, 2026. Financial statements signed 23 April 2026.
- annual-report__Annual_Report_2025.txt: FY25 AR, cover letter August 18, 2025. AOC-1 signed 08 August 2025.
- results__Q1FY27_Results_Unaudited_2026-07-23.txt: Q1FY27 results, board meeting 23 July 2026.
- results__FY26_Q4_Audited_Results_2026-04-23.txt: FY26 audited results, 23 April 2026.
- results__Q1FY27_Press_Release_2026-07-23.txt: 23-Jul-2026.
- announcements__FY26_Q4_Press_Release_2026-04-23.txt: 23-Apr-2026.
- announcements__IGX_DRHP_Filing_Intimation_2026-07-15.txt: dated July 15, 2026.
- announcements__Indian_Coal_Exchange_Incorporation_2026-06-01.txt: dated June 01, 2026.
- prospectus__IGX_Draft_Abridged_Prospectus_2026-07.txt: Jul-2026, refers to the DRHP dated July 14, 2026.
- presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt: 24-Jul-2026. presentation__Investor_Presentation_Q4FY26_2026-04-23.txt: 23-Apr-2026.
- concalls__Concall_Feb_2026_Transcript.txt, concalls__Concall_Apr_2026_Transcript.txt, concalls__Concall_Jul_2026_Transcript.txt, other__Concall_Nov_2025_Q2FY26_Transcript.txt.
- Shareholding_Pattern_30_JUN_2025.xml, _31_MAR_2026.xml, _30_JUN_2026.xml (DateOfReport 2025-06-30, 2026-03-31, 2026-06-30). SEP_2025 and DEC_2025 were checked for the total only.

NOT DISCLOSED, with pointer:
1. ICX carrying value at 30-Jun-2026: H1FY27 standalone statement of assets and liabilities (not in corpus).
2. Indian Coal Exchange Ltd carrying value and cash actually subscribed: H1FY27 results or FY27 AR Note 6 (not in corpus).
3. IEX % in Enviro Enablers India Pvt Ltd: EEIPL cap table (not in corpus).
4. IGX FY24 revenue, PAT and net worth in IEX's own filings: FY24 AR AOC-1 Part B (not in corpus). IGXP p7 covers it.
5. IGX Q1FY27 revenue and net worth: an IGX quarterly statement or RHP update (not in corpus).
6. IGX OFS value and price band: the RHP (IGXP prints "[●]").
7. ICX FY24 revenue: FY24 AR AOC-1 Part A (not in corpus).
8. ICX Q1FY27 PAT: an ICX quarterly statement (not in corpus). Q1R has no entity split.
9. Coal board resolution date: IEX Reg 30 intimation dated March 18, 2026 (cited in ICXL p1, not in corpus).
10. Coal licence application submission and grant: a future Reg 30 intimation (not in corpus).
11. Coal Exchange Rules notification date in a filed document: only [MGMT] gives 4-Jun-2026 (AM p34, CC-Jul26 p26). Gazette notification not in corpus.
12. Coal capital commitment beyond share capital: AR26 commitments note (no coal item found).
13. RSU 2019 units outstanding company-wide: Reg 14 SBEB disclosure at iexindia.com/investors/other-disclosures (AR26 p70; not in corpus).
14. ESOPs outstanding at 30-Jun-2026: FY27 AR Note 51 (not in corpus).
15. Current buyback authorisation: none filed. A future Reg 30 board outcome would carry it.
16. Numeric dividend payout range: the Dividend Distribution Policy PDF (AR26 p69 link; not in corpus).
17. A standalone capital-allocation policy: none found in AR26 Board's Report pp.67-80, the presentations or the concalls.
18. Segment revenue and result: none (single reportable segment). AR26 p211 product split and AR26 p292 entity table are the nearest substitutes.

CONFLICTS flagged, not reconciled:
- IGX associate date: 17-Jan-2022 (AOC-1) against "after 16 Jan 2022" (Note, AR26 p246).
- IGX stake: 47.28% [FILED] against 47.5% / 47.3% [MGMT].
- IGX FY26 revenue: Rs 79 crore (AR26 p73) against RfO Rs 610.05 mn / total income Rs 848.39 mn (IGXP).
- IGX FY26 PAT: 41.9 crore against 420.22 mn. IGX FY25 PAT: 3,094.66 lakh against 307.93 mn.
- ICX FY25 revenue: Rs 189.22 lakh / Rs 2.1 crore / Rs 3.4 crore.
- ICX FY26 revenue: turnover Rs 726.13 lakh against total revenue Rs 7.71 crore.
- I-REC: India market 12.01 mn / 18.41 mn against ICX 59 lakh / 1.79 crore.
- Indian Coal Exchange capital: authorised Rs 100 crore (ICXL) against authorised and paid-up Rs 100 crore (AR26 p74).
- Coal rules: Draft 2025 (ICXL, AR26 p52) against notified 2026 (AR26 p30).
- ESOP trust bonus shares at FY25: 1,621,215 (AR25) against 1,628,657 (AR26 comparative).

---

## ORCHESTRATOR ADDENDUM (closes a gap flagged in Part A closing)

A6, rumour verification reply. The Part A reader did not open `announcements__Rumour_Verification_Reply_2026-04-20.txt`. The orchestrator searched it for "fee", "paise" and "transaction charge". Zero matches. The reply concerns only the 17-Apr-2026 draft coupling regulations; its text is quoted in Part B1. [FILED] Result for A6: no fee content in this document. The A6 answer stands: the corpus holds no disclosure of the 2023 CERC fee order or the Dec-2025 staff paper.
