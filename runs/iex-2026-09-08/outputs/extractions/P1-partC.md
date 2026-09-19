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
