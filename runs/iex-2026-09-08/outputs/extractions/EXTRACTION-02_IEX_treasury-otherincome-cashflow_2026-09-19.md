# EXTRACTION RESPONSE 2 — Treasury, liabilities against it, other income, cash flow quality
IEX | Indian Energy Exchange Ltd | run folder runs/iex-2026-09-08 | answered 2026-09-19
Corpus: branch run/iex-2026-09-08, corpus commit e6a917153d8657ebf0395371149e8a091c79f429 (inputs unchanged since)
Source text: page-marked extractions of the inputs/ PDFs (runs/iex-2026-09-08/work/*.txt, gitignored), plus inputs/shareholding/*.xml.

PAGE CONVENTION: every "p.N" is the "=== PAGE N ===" marker of the extracted file, i.e. the PDF page number.
It differs from the page number printed on the page (AR26 marker p.211 prints "207"). To verify, open the PDF at page N.

TIERS: [FILED] = annual report, results filing, exchange announcement, SEBI-filed prospectus, shareholding pattern.
[MGMT] = concall, presentation, press release, Reg 30 media release (Power Market Updates).
No web, no estimates, no reconciliation. Conflicts are reported side by side and marked CONFLICT.
Figures in Rs lakhs as printed unless the source prints another unit.

# IEX P2 extraction, Parts A and B: treasury schedule and liabilities against it

Corpus only. No web. Figures in Rs lakhs as printed. Page = the "=== PAGE n ===" marker in the text file. Tabs in the source text are shown as spaces. Short names for the files:

- **AR26** = annual-report__Annual_Report_2026.txt (FY26 AR, filed BSE 14-Aug-2026). Standalone notes pp.193-230. Consolidated notes pp.240-292.
- **AR25** = annual-report__Annual_Report_2025.txt (FY25 AR). The extraction repeats some pages (for example, Note 6 appears on p.188/189 and again on p.190/191). The first occurrence is cited.
- **Q4R** = results__FY26_Q4_Audited_Results_2026-04-23.txt (audited results, 23-Apr-2026)
- **Q1R** = results__Q1FY27_Results_Unaudited_2026-07-23.txt (unaudited results, cover dated 23-Jul-2026)
- **CC-Feb** = concalls__Concall_Feb_2026_Transcript.txt (Q3FY26 call, cover dated 05-Feb-2026)
- **CC-Apr** = concalls__Concall_Apr_2026_Transcript.txt (Q4FY26 call. Cover dated 30-Apr-2026. Page header reads "April 24, 2026")
- **CC-Jul** = concalls__Concall_Jul_2026_Transcript.txt (Q1FY27 call, cover dated 31-Jul-2026)
- **CC-Nov** = other__Concall_Nov_2025_Q2FY26_Transcript.txt (Q2FY26 call, cover dated 07-Nov-2025)

**30-Jun-2026 position (applies to every question below):** NOT DISCLOSED. Q1R has only the statement of profit and loss (standalone p.4, consolidated p.9) and notes 1-5. It has no statement of assets and liabilities, no investment schedule, and no cash or liability detail. The Q1FY27 balance sheet would first appear in the H1FY27 (30-Sep-2026) results. Under SEBI LODR Reg 33, the half-yearly results carry the statement of assets and liabilities. That filing is not in the corpus. CC-Jul has no treasury balance figure either. The only hit for "cash" is p.28 line 1272, a qualitative line: "We have strong cash -flows which" [MGMT].

---

## A1. Non-current investments, instrument by instrument

### A1.1 Standalone, AR26 Note 6 (pp.197-198) [FILED]

Header (p.197): "6. Investments ... Non-current investments". Columns: As at 31 March 2026 | As at 31 March 2025.

| Category (as printed) | Instrument (verbatim) | 31-Mar-2026 | 31-Mar-2025 | Page |
|---|---|---|---|---|
| Investment carried at cost: Associate | "A) Investments in Indian Gas Exchange Limited (Associate) Equity Instruments (Unquoted)", "35,460,000 (31 March 2025: 35,460,000) shares of `10 each fully paid up" | 3,546.00 | 3,546.00 | 197 |
| Investment carried at cost: Subsidiary | "B) Investments in ICX Private Limited (Subsidiary) (formerly International Carbon Exchange Private Limited) Equity Instruments (Unquoted)", "5,000,000 ... shares of `10 each" | 500.00 | 500.00 | 197 |
| Amortised cost: A) Bonds (Quoted) | "7.11% Tax Free Bonds Power Finance Corporation Ltd." (Nil (31 March 2025: 5,134) units of FV `1,000) | - | 52.99 | 197 |
| same | "9.55% Tata Motors Finance Ltd" (200 units of FV `1,000,000) | 2,038.20 | 2,038.20 | 197 |
| same | "7.84% HDFC Bank Ltd" (20 units of FV `10,000,000) | 2,088.86 | 2,090.58 | 197 |
| same | "9.15% Adani Enterprises limited" (229,898 (31 March 2025: Nil) units of FV `1,000) | 2,447.67 | - | 197 |
| same | "8.75% Adani Enterprises limited" (187,142 (31 March 2025: Nil) units of FV `1,000) | 1,906.86 | - | 197 |
| Amortised cost: B) Target Maturity Funds (Unquoted) | "Kotak Nifty SDL Apr 2027 top 12 Equal Weight Index Fund Direct Plan Growth" | 619.95 | 583.15 | 197 |
| same | "Tata Nifty SDL Plus AAA PSU Bond Dec 2027 60: 40 Index Fund Direct Plan Growth" | 202.18 | 189.81 | 197 |
| same | "UTI CRISIL SDL Maturity April 2033 Index Fund - Direct Plan" | 202.78 | 190.21 | 197 |
| same | "Kotak Nifty SDL Apr 2027 top 12 Equal Weight Index Fund Direct Plan Growth*" | - | 1,780.15 | 197 |
| same | "Aditya Birla Sun Life Nifty SDL Apr 2027 Index Fund Direct Growth*" | - | 1,774.91 | 197 |
| same | "ICICI Prudential Nifty SDL Sep 2027 Index Fund - Direct Plan Growth*" | - | 1,184.26 | 197 |
| same | "Axis CRISIL IBX SDL May 2027 Index Fund*" | - | 1,767.55 | 197 |
| same | "HDFC Nifty G Sec Dec 2026 Index Fund Direct Growth*" | - | 3,522.19 | 197 |
| same | "Aditya Birla Sun Life CRISIL IBX GIL T Apr 2029 Index Fund Direct Growth" | - | 2,896.96 | 197-198 |
| same | "Kotak Nifty SDL Apr 2032 Top 12 Equal Weight Index Fund Direct Plan Growth*" | - | 2,307.56 | 198 |
| same | "UTI CRISIL SDL Maturity Apr 2033 Index Fund Direct Plan Growth" | - | 2,886.46 | 198 |
| same | "Aditya Birla Sun Life CRISIL IBX 60:40 SDL plus AAA PSU - Apr 2027 Index Fund Direct Growth*" | - | 2,871.37 | 198 |
| same | "Tata Nifty SDL Plus AAA PSU Bond Dec 2027 60:40 Fund Direct Growth Plan*" | - | 2,300.71 | 198 |
| Amortised cost: C) Fixed Maturity Plan (Quoted) | "SBI Fixed Maturity Plan (FMP)- Series 72 (1,239 Days) Direct Growth*" | - | 2,339.57 | 198 |
| same | "Axis Fixed Term Plan-Series 112 (1,133 Days)*" | - | 1,733.21 | 198 |
| same | "Axis Fixed Term Plan-Series 113 (1,228 Days)*" | - | 2,308.88 | 198 |
| FVTPL: A) Strategic investment | "Investments in Enviro Enablers India Private Limited (Strategic investment) 10% Series Seed Compulsorily Convertible Preference shares (Unquoted)" | 122.22 | 122.22 | 198 |
| FVTPL: B) Units of InvITs (Quoted) | "Indi Grid InvIT Trust Units" (1,867,452 (31 March 2025: 758,728) units) | 3,089.51 | 1,069.12 | 198 |
| FVTPL: C) Equity Index Mutual Fund (Quoted) | "HDFC Nifty 50 Index Fund" | 2,326.32 | 472.81 | 198 |
| same | "SBI Nifty 50 Index Fund - Direct Plan" | 2,420.15 | 1,523.26 | 198 |
| same | "UTI Nifty 50 Index Fund - Direct Plan" | 2,198.70 | - | 198 |
| same | "ICICI Prudential Nifty 50 Index Fund - Direct Plan" | 645.71 | - | 198 |
| **Total (printed)** | "Total" | **24,355.11** | **42,052.13** | 198 |

Footer rows, verbatim (AR26 p.198):
- "Aggregate book value of quoted investments carried at amortised cost 8,481.60 10,563.43"
- "Aggregate market value of quoted investments carried at amortised cost 8,498.14 10,623.60"
- "Aggregate book and market value of quoted investments measured at FVTPL 10,680.39 3,065.19"
- "Aggregate value of unquoted investments 5,193.12 28,423.51"
- "Aggregate amount of impairment in value of investments - -"
- "*Investments includes Nil (cost) [(31 March 2025: `3,199.33) (cost)] under lien with banks for overdraft facilities."

Comment: the FY26 fall in the non-current total came from TMF and FMP units. Those units left this note, and the three FMPs reappear under current investments (A2). Two Adani Enterprises bonds were added in FY26.

**Ratings, standalone non-current:** NOT DISCLOSED. Note 6 prints no credit rating for any bond. The credit-risk note (AR26 p.221) speaks only in general terms. It says the Company "generally invests in deposits with banks with high credit ratings assigned by domestic credit agencies". That sentence covers bank deposits only. Instrument ratings would appear in the Note 6 table or in Note 42 credit risk (p.221) if disclosed. They are not.

**Cross-check against AR25 Note 6 (pp.188-190), 31-Mar-2025 column [FILED]:** the Tata Motors Finance, HDFC Bank, PFC tax-free, TMF, FMP, Enviro, IndiGrid and equity index fund values match AR26. AR25 also shows these 31-Mar-2025 Nil rows under non-current bonds, with a 31-Mar-2024 value: "7.74% SBI Perpetual Bonds - 2,097.81", "9.30% Arka Fincap Pvt Ltd - 1,536.69" and the three 7.04% tax-free bonds (HUDCO 153.72, IRFC 121.38, NABARD 100.33). Also: "Power Grid InvIT Trust Units - 1,206.23" and "C) Market Linked Debentures (MLD) (Quoted) Arka Fincap Limited - 1,656.78" (AR25 p.189-190). AR25 total: "Total 42,052.13 44,814.18" (p.190). Comment: those instruments moved to current at 31-Mar-2025 (see A2).

### A1.2 Consolidated, AR26 Note 6 (pp.258-259) [FILED]

Consolidated Note 6 drops the two cost-basis lines (IGX associate, ICX subsidiary). The associate is shown on the balance sheet as "Investments accounted for using the equity method 54 9,025.09 7,574.70" (AR26 p.240). Every other row matches the standalone Note 6 above in instrument and amount. That covers the bonds (p.258: for example "9.15% Adani Enterprises limited 2,447.67 -", "8.75% Adani Enterprises limited 1,906.86 -", "9.55% Tata Motors Finance Ltd 2,038.20 2,038.20"), the TMFs, the FMPs (p.259), Enviro, IndiGrid and the equity index funds. Differences, verbatim:
- "Total 20,309.11 38,006.13" (p.259)
- "Aggregate value of unquoted investments 1,147.12 24,377.51" (p.259)
- Book and market value, FVTPL and impairment rows are the same as standalone. "Aggregate amount of impairment in value of investments - -" (p.259).
- The lien footnote is the same: "*Investments includes Nil (cost) [(31 March 2025: `3,199.33) (cost)] under lien with banks for overdraft facilities." (p.259)

Ratings: NOT DISCLOSED (same pointer, consolidated Note 6 pp.258-259 and credit risk p.282).

---

## A2. Current investments, instrument by instrument

### A2.1 Standalone, AR26 Note 10 (pp.199-202) [FILED]

Header (p.199): "10. Current investments ... Investments measured at amortised cost".

**A) Commercial Papers (Quoted)** (p.199). Face value per unit is `500,000 on every row.

| Instrument (verbatim) | Units 31-Mar-26 / 31-Mar-25 | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|---|
| "9.25% Trust Investment Advisors Private Limited" | Nil / 1000 | - | 4,862.51 |
| "8.70% Trust Investment Advisors Private Limited" | 500 / Nil | 2,487.51 | - |
| "8.75% Trust Investment Advisors Private Limited" | 1000 / Nil | 4,940.44 | - |
| "8.65% ECL Finance Ltd" | 1,500 / Nil | 7,388.74 | - |
| "8.35% Bombay Burmah Trading Corporation Ltd." | 1,000 / Nil | 4,935.15 | - |
| "9.41% Vivriti Capital Ltd" | 500 / Nil | 2,412.62 | - |
| "9.85% Navi Finserve Limited" | 500 / Nil | 2,451.76 | - |

**B) Commercial Papers (Unquoted)** (pp.199-200). Face value per unit is `500,000 on every row.

| Instrument (verbatim) | Units 31-Mar-26 / 31-Mar-25 | 31-Mar-2026 | 31-Mar-2025 | Page |
|---|---|---|---|---|
| "9.75% Muthoot Capital Services Limited" | Nil / 500 | - | 2,398.08 | 199 |
| "9.00% Angel One Limited" | Nil / 500 | - | 2,445.28 | 199-200 |
| "10.00% Navi Finserve Limited" | Nil / 500 | - | 2,458.23 | 200 |
| "10.10% Navi Finserve Limited" | Nil / 500 | - | 2,394.57 | 200 |
| "10.50% Navi Finserve Limited" | 500 / Nil | 2,432.88 | - | 200 |
| "10.25% Navi Finserve Limited" | 500 / Nil | 2,407.29 | - | 200 |
| "9.25% IIFL Finance" | Nil / 500 | - | 2,399.15 | 200 |
| "9.60% IIFL Samasta Finance" | Nil / 500 | - | 2,430.35 | 200 |
| "8.85% IIFL Samasta Finance" | 500 / Nil | 2,419.87 | - | 200 |
| "8.90% IIFL Finance" | 500 / Nil | 2,396.74 | - | 200 |
| "8.40% IIFL Finance" | 500 / Nil | 2,456.93 | - | 200 |
| "9.80% ECL Finance Ltd" | Nil / 1,000 | - | 4,913.75 | 200 |
| "9.50% Avendus Finance Pvt Ltd" | Nil / 500 | - | 2,399.95 | 200 |
| "9.40% Vivriti Capital Ltd" | 500 / Nil | 2,426.24 | - | 200 |
| "8.80% 5Paisa Capital" | 500 / Nil | 2,467.92 | - | 200 |
| "9.20% Oxyzo Financial services limited" | 500 / Nil | 2,497.00 | - | 200 |
| "8.82% Oxyzo Financial services limited" | 500 / Nil | 2,443.26 | - | 200 |
| "7.95% Sammaan Capital Limited" | 500 / Nil | 2,408.30 | - | 200 |
| "8.65% Alpha Alternatives Financial Services Pvt Ltd" | 500 / Nil | 2,480.88 | - | 200 |

CP subtotal: the Note 10 table prints no CP subtotal. A CP aggregate does appear in the interest-rate-risk profile, AR26 p.223: "Commercial papers 51,453.53 26,701.87" (31-Mar-2026 | 31-Mar-2025). Comment: this is the filing's own CP figure. It is quoted here as printed and was not recomputed from the rows.

**CP rating: NOT DISCLOSED** for every CP. **CP maturity date: NOT DISCLOSED** for every CP. Note 10 prints only the coupon or discount rate, the issuer, the units and the face value. Pointer: this detail would sit in AR26 Note 10 (pp.199-200) or Note 42 credit risk (p.221). Neither prints ratings or maturities. The corporate governance report item "xv. Credit ratings obtained by the entity ..." reads "Not Applicable" (AR26 p.119). That item concerns IEX's own ratings, not holdings.

**C) Bonds (Quoted)** (p.200)

| Instrument (verbatim) | Units / FV | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|---|
| "7.74% SBI Perpetual Bonds" | Nil (31 March 2025: 200) / `1,000,000 | - | 2,091.37 |
| "9.30% Arka Fincap Pvt Ltd" | Nil (31 March 2025: 1,50,000) / `1,000 | - | 1,536.69 |
| "7.04% Tax Free Bonds Housing and Urban Development Corporation Ltd." | Nil (15,058) / `1,000 | - | 153.72 |
| "7.04% Tax Free Bonds Indian Railway Finance Corporation Ltd." | Nil (11,757) / `1,000 | - | 121.40 |
| "7.04% Tax Free Bonds National Bank for Agriculture and Rural Development" | Nil (10,020) / `1,000 | - | 100.37 |
| "10.17% Manipal Healthcare Pvt Ltd" | 250 (31 March 2025: Nil) / `10,00,000 | 2,563.37 | - |

Bond rating: NOT DISCLOSED. Bond maturity: NOT DISCLOSED (same pointer). The perpetual SBI bond had no maturity by its nature, and the filing states none.

Interest-rate-risk aggregate, AR26 p.223 (verbatim): "Investments in bonds 11,044.95 8,185.31". Comment: this is the filing's combined non-current plus current bond figure. It was not recomputed.

**D) Fixed Maturity Plan (Quoted)** (p.201)

| Instrument (verbatim) | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| "SBI Fixed Maturity Plan (FMP)- Series 72 (1,239 Days) Direct Growth" | 2,483.56 | - |
| "Axis Fixed Term Plan-Series 112 (1,133 Days)" | 1,844.96 | - |
| "Axis Fixed Term Plan-Series 113 (1,228 Days)" | 2,460.87 | - |

Comment: the FMP tenor in days is printed in the scheme name. No maturity date is printed.

**Investments measured at FVTPL: A) Market Linked Debentures (MLD) (Quoted)** (p.201)
- "Arka Fincap Limited - 1,826.07". "Nil (31 March 2025: 150) units of face value of `1,000,000 each".

**B) Mutual funds (Unquoted)** (pp.201-202). The scheme type is as named in the filing. The filing gives no separate scheme-type column.

| Scheme (verbatim) | 31-Mar-2026 | 31-Mar-2025 | Page |
|---|---|---|---|
| "Aditya Birla Sun Life Money Manager Fund - Growth-Direct Plan*" | 2,916.55 | 2,734.36 | 201 |
| "Aditya Birla Sun Life Arbitrage Fund - Growth-Direct Plan*" | 10,491.42 | - | 201 |
| "Aditya Birla Sun Life Savings Fund - Growth-Direct Plan*" | 4,423.05 | 4,133.14 | 201 |
| "Axis Liquid Fund - Direct Growth" | 4,502.92 | 3,841.63 | 201 |
| "DSP Liquid Fund - Direct Growth" | 4,503.23 | 4,529.08 | 201 |
| "DSP Low Duration Fund - Direct Growth" | - | 2,535.62 | 201 |
| "HDFC Low Duration Fund - Direct Growth" | - | 2,507.06 | 201 |
| "HDFC Money Market Fund - Direct Growth" | - | 2,504.99 | 201 |
| "HDFC Liquid Fund - Direct Growth" | - | 2,504.96 | 201 |
| "ICICI Prudential Liquid Fund - Direct Growth" | - | 2,518.13 | 201 |
| "Axis Arbitrage Fund - Direct Growth*" | 9,514.95 | 3,762.20 | 201 |
| "Axis Arbitrage Fund - Direct Growth EAD" | 205.37 | 210.28 | 201 |
| "Edelweiss Arbitrage Fund- Direct Plan Growth- ATDG*" | 6,121.72 | 8,094.89 | 201 |
| "Invesco India Arbitrage Fund- Direct Plan Growth- AFD1*" | 11,163.63 | 5,683.04 | 201 |
| "Kotak Equity Arbitrage Fund - Direct Plan-Growth*" | 9,609.70 | 8,987.24 | 201 |
| "Kotak Equity Arbitrage Fund - Direct Plan-Growth" | 192.89 | 133.94 | 201 |
| "Kotak Low Duration Fund - Direct Growth" | - | 2,507.06 | 201 |
| "Kotak Overnight Fund - Direct Growth" | 3,001.01 | - | 201 |
| "Kotak Money Market Fund - Direct Growth" | 2,504.69 | 2,505.13 | 202 |
| "Nippon India Arbitrage Fund - Direct Growth Plan Growth Option*" | 4,828.06 | 5,778.33 | 202 |
| "Nippon India Liquid Fund - Direct Plan Growth Plan - Growth Option" | 4,507.83 | 2,014.28 | 202 |
| "SBI Liquid Fund- Direct Growth" | - | 3,012.67 | 202 |
| "SBI Arbitrage Opportunities Fund- Direct Plan- Growth" | - | 2.78 | 202 |
| "SBI Magnum Constant Maturity Fund Direct Growth" | - | 1,128.44 | 202 |
| "SBI Arbitrage Opportunities Fund- Direct Plan- Growth*" | 7,760.94 | 7,267.59 | 202 |
| "Tata Liquid Fund - Direct Plan Growth*" | 2,802.89 | 2,536.89 | 202 |
| "Tata Money Market Fund - Direct Plan Growth*" | 2,687.90 | 2,515.71 | 202 |
| "Tata Arbitrage Fund - Direct Plan Growth" | 247.85 | 171.26 | 202 |
| "UTI Arbitrage Fund - Direct Growth Plan CANSERVE*" | 6,152.62 | 1,003.88 | 202 |
| "Tata Arbitrage Fund - Direct Plan Growth*" | 10,291.41 | - | 202 |

Note 10 footer rows, verbatim (AR26 p.202):
- "Total 1,69,236.92 1,17,656.07"
- "Aggregate book value of quoted investments carried at amortised cost 33,968.99 8,866.06"
- "Aggregate market value of quoted investments carried at amortised cost 34,381.08 13,905.14"
- "Aggregate book and market value of quoted investments measured at FVTPL - 1,826.07"
- "Aggregate value of unquoted investments 1,35,267.92 1,06,963.92"
- "Aggregate amount of impairment in value of investments - -"
- "*Investments includes `34,323.06 (cost) [(31 March 2025: `32,205.62) (cost)] under lien with banks for overdraft and standby letter of credit (SBLC facilities)."

Price-risk aggregate, AR26 p.224 (verbatim): "Investments in Mutual funds 1,08,430.63 85,124.56", "Equity Index Mutual Fund 7,590.88 1,996.07", "Investments in Units of InvIT 3,089.51 1,069.12", "Investments in Market Linked Debentures (MLD) - 1,826.07". Interest-rate profile, p.223: "Target Maturity funds and Fixed Maturity Plan 7,814.30 30,636.93", "Bank deposits 7,178.31 10,768.21".

Fixed deposits: bank deposits are not in Note 10. They sit in Notes 7, 12 and 13 (see A3).

Other current instruments: none beyond the categories above appear in Note 10.

**Mutual fund scheme ratings: not applicable.** None are printed.

**CONFLICT, unit count only (AR26 p.202 vs AR25 p.193):** AR26 prints "Nippon India Liquid Fund ... 4,507.83 2,014.28" with units "66,840.923 (31 March 2025: 2,04,93,085.349)". AR25 prints the 31-Mar-2025 units as "31,736.524" (AR25 p.193, "Nippon India Liquid Fund ... 2,014.28 3,015.84 / 31,736.524 (31 March 2024: 51,038.643)"). The rupee value 2,014.28 agrees. The AR26 comparative unit figure repeats the Nippon Arbitrage unit count on p.202. Reported, not reconciled.

**CONFLICT, lien asterisk:** AR25 prints "SBI Arbitrage Opportunities Fund- Direct Plan- Growth 7,267.59 5,249.90" with no asterisk (AR25 p.193). AR26 prints the same 31-Mar-2025 holding with an asterisk: "SBI Arbitrage Opportunities Fund- Direct Plan- Growth* 7,760.94 7,267.59" (AR26 p.202).

**Cross-check, AR25 Note 10, 31-Mar-2025 column (pp.191-194) [FILED]:** the CP, bond, MLD and mutual fund rows and values match AR26's comparative column, apart from the unit and asterisk points above. The 31-Mar-2024 CPs, for reference: "8.85% Trust Investment Advisors Private Limited - 2,456.71", "8.70% Motilal Oswal Finvest Limited - 2,491.42", "8.80% Motilal Oswal Financial Services - 2,494.69", "9.20% Angel One Limited - 2,434.92", "9.25% Navi Finserve Limited - 2,491.35", "9.90% ECL Finance Ltd - 2,433.41", "8.75% JM Financial Services Ltd - 1,985.76", "9.00% Muthoot Capital Services Limited - 2,460.21", "9.55% Nuvama Wealth & Investment Limited - 4,934.82" (AR25 pp.191-192). The 31-Mar-2024 MLDs: "JM Financial ARC - 1,395.00", "JM Financial ARC Ltd - 114.48", "L&T Infra Credit Limited - 2,335.03", "IIFL Home Finance Ltd - 2,987.24", "IIFL Samasta Finance Limited - 2,472.73", "L&T Finance Limited - 2,247.71", "Piramal Enterprises Limited - 2,306.09" (AR25 p.192). AR25 total: "Total 1,17,656.07 86,167.36" (p.194).

### A2.2 Consolidated, AR26 Note 10 (pp.260-264) [FILED]

Every CP, bond, FMP and mutual fund row matches the standalone rows above in instrument and amount. The spelling differs: "9.85% Navi Finserv Limited 2,451.76 -" (p.260) and "10% Navi Finserv Limited - 2,458.23". Differences, verbatim:
- The FMPs carry the lien asterisk in the consolidated note: "SBI Fixed Maturity Plan (FMP)- Series 72 (1,239 Days) Direct Growth* 2,483.56 -", "Axis Fixed Term Plan-Series 112 (1,133 Days)* 1,844.96 -", "Axis Fixed Term Plan-Series 113 (1,228 Days)* 2,460.87 -" (p.262). The standalone Note 10 prints the same three with no asterisk (p.201). **CONFLICT** on lien marking. Reported, not reconciled.
- Extra rows that are not in standalone (subsidiary holdings): "Kotak Equity Arbitrage Fund - Direct Plan-Growth 135.76 112.58" and "Aditya Birla Sun Life Arbitrage Fund - Growth-Direct Plan 358.02 -" (p.263). Also "Tata Arbitrage Fund - Direct Plan Growth 245.02 -" (p.264).
- "Total 1,69,975.72 1,17,768.65" (p.264)
- "Aggregate book value of quoted investments carried at amortised cost 33,968.98 8,866.06" (p.264). Standalone prints 33,968.99. This is a 0.01 difference, reported as printed.
- "Aggregate value of unquoted investments 1,36,006.74 1,07,076.51" (p.264)
- "Aggregate amount of impairment in value of investments - -" (p.264)
- Lien footnote is the same as standalone: "`34,323.06 (cost) [(31 March 2025: `32,205.62) (cost)]" (p.264).
- Consolidated interest-rate profile, TMF and FMP line: "Target Maturity funds and Fixed Maturity Plan 7,814.29 30,636.93" (p.285). Standalone prints 7,814.30 (p.223).

Ratings and maturities: NOT DISCLOSED (consolidated Note 10 pp.260-264; credit risk p.282).

### A2.3 Balance-sheet totals, Q4R statement of assets and liabilities [FILED]

- Standalone (Q4R p.7): "(i) Investments 24,355.11 42,052,13" (non-current) and "(i) Investments 1,69,236.92 1,17,656 07" (current). These agree with AR26.
- Consolidated (Q4R p.16): "(i) Investments 20,309.11 38,006.13", "(i) Investments 1,69,975.72 1,17,768.65", and "Investments accounted for using the equity method 9,025.09 7,574.70". These agree with AR26.

---

## A3. Cash and bank balances: own funds vs settlement, margin and member deposits

### A3.1 Standalone [FILED]

AR26 Note 12, Cash and cash equivalents (p.203):
- "- in current accounts 1,341.79 2,236.53"
- "- in settlement accounts 2,309.93 4,424.75"
- "Bank deposits with original maturity of less than three months - 4,002.27"
- "Total 3,651.72 10,663.55"

AR26 Note 13, Bank balance other than cash and cash equivalents (p.203):
- "Bank Deposits having original maturity of more than three months and due to mature within twelve months of reporting date* 6,668.54 521.64"
- "In earmarked accounts - Current Accounts (unpaid dividend) # 113.71 79.44"
- "Total 6,782.25 601.08"

AR26 Note 7, Other financial assets, non-current (p.199): "Bank deposits due for maturity after twelve months from the reporting date* (refer note 13) 509.77 6,244.30".

"Details of bank deposits" (p.204): "Total 7,178.31 10,768.21".

Footnotes (p.204): "*Bank deposits includes `5,190.00 (31 March 2025: Nil) under lien with banks for overdraft facilities." and "#Restricted bank balances which are to be used for specified purposes." Note 7 footnote (p.199): "*Bank deposits includes Nil (31 March 2025: `5,190.00) under lien with banks for overdraft facilities." Comment: the 5,190.00 lien deposit moved from non-current (Note 7) at 31-Mar-2025 to current (Note 13) at 31-Mar-2026.

**Split into own funds vs member money: NOT DISCLOSED in the filing.** The notes separate only "current accounts", "settlement accounts" and the earmarked unpaid-dividend account. No note states which cash, deposits or investments are funded by settlement obligations, SGF deposits or trading margin deposits (the B1 liabilities). No note states which are shareholder funds. Pointer: this would appear in AR26 Notes 12/13 (pp.203-204), Note 53/54 (p.230) or Note 42 liquidity risk (p.222). None makes the split. The liquidity note says only: "its liquidity position, comprising total cash (including bank deposits under lien) and short-term investments and anticipated future internally generated funds from operations, will enable it to meet its future known obligations" (p.222).

Management statement [MGMT], CC-Feb p.14 (Q3FY26 call, answer by CFO Vineet Harlalka): "We have a total cash of around INR1,500 crores as on 31st of December. And out of that, the shareholder fund is around INR1,200 crores." Comment: this is the only corpus statement of an own-funds split. It is a rounded management figure at 31-Dec-2025 and has no filed counterpart.

AR25 standalone, 31-Mar-2025 and 31-Mar-2024 (AR25 Note 12/13, p.195): "- in current accounts 2,236.53 5,647.57", "- in settlement accounts 4,424.75 6,131.81", "Bank deposits with original maturity of less than three months 4,002.27 3,000.74", "Total 10,663.55 14,780.12". Also "Bank deposits having original maturity of more than three months but less than twelve months * 521.64 3,707.36" and "- Current Accounts (unpaid dividend) # 79.44 33.86". These agree with AR26 on 31-Mar-2025.

### A3.2 Consolidated [FILED]

AR26 consolidated Note 12 (p.265): "- in current accounts 1,425.87 2,266.36". The settlement-account row and the deposit row are the same as standalone: 2,309.93 | 4,424.75 and - | 4,002.27. "Total 3,735.80 10,693.38". Consolidated Note 13 (p.265): "Total 6,782.25 601.08", with the same deposit and unpaid-dividend rows and the same lien and restriction footnotes. Consolidated Note 7 (p.260): "Total 742.83 6,490.53". Own vs member split: NOT DISCLOSED (same pointer, consolidated pp.265, 283, 291).

Q4R check (p.7 standalone, p.16 consolidated): "(iii) Cash and cash equivalents 3,651.72 10,663 55" / "3,735.80 10,693.38". "(iv) Bank balance other than (iii) above 6,782.25 601 08". The standalone cash-flow note in Q4R (p.8) reads: "In settlement accounts 2,309.93 4,424,75".

### A3.3 Related asset: settlement obligation receivables [FILED]

AR26 Note 15, Other financial assets, current (p.204): "Secured, considered good / Settlement Obligation receivables 14,641.56 21,792.15". Other rows: "Security deposits 180.98 180.98", "Margin money held with broker firm - 0.04", and "Total 14,869.40 22,023.09". Consolidated Note 14 (p.266): the same settlement receivable, plus "Earnest money deposit - 300.00", with "Total 14,868.43 22,314.24".

---

## A4. Impairment, MTM loss, credit-loss provision or default on any investment (FY25, FY26, Q1FY27)

**FY26 and FY25 impairment [FILED]:** "Aggregate amount of impairment in value of investments - -" on AR26 p.198 (non-current), p.202 (current), p.259 and p.264 (consolidated). The same nil row appears on AR25 p.190 and p.194 for 31-Mar-2025 and 31-Mar-2024.

**Credit-loss provision [FILED], AR26 Note 42 credit risk (p.221):** "The Company has not experienced any significant impairment losses in respect of any of the investments. In respect of other financial assets including security deposit, the credit risk associated is relatively low. Accordingly, no provision for expected credit loss has been provided on such financial assets." Also: "The Company has assets where the counter- parties have sufficient capacity to meet the obligations and where the risk of default is very low. Hence, no impairment loss has been recognised during the reporting periods in respect of these assets." The same note says (p.221): "investment in target maturity funds, fixed maturity plans, market linked debentures are exposed to uncertainties as regards to fulfilment of obligations by counter-party." The consolidated note repeats this (p.283). AR25 has identical wording (p.213).

**MTM (fair value) line in the P&L [FILED]:** AR26 Note 29 Other income (p.211): "Fair value gain on investments measured at fair value through profit or loss (net) 3,397.39 4,123.64" (FY26 | FY25). Other rows: "Gain on sale of investments measured at fair value through profit or loss (net) 2,328.88 1,680.79", "Gain on sale of investments measured at amortised cost (net) 809.24 -" and "Total 13,655.11 11,892.43". Comment: the annual FVTPL line is a net gain in both years. No net MTM loss is printed for either full year.

**Default on any investment: NOT DISCLOSED as having occurred.** No note records a default. Pointer: this would sit in AR26 Note 42 (p.221) or Notes 6/10.

**Q1FY27: NOT DISCLOSED.** Q1R has no investment note, impairment line or MTM breakdown. Other income appears only as a total: "2 Other income 4,491.58 2,211.41 4,252.37 13,655.11" (Q1R p.4, standalone: Q1FY27 | Q4FY26 | Q1FY26 | FY26). Consolidated: "2 Other income 4,493 27 2,213.66 4,242_81 13,130.47" (p.9). Pointer: the Q1R notes (p.5 onward) carry no treasury item.

---

## A5. The one-time treasury MTM item

**Location finding:** the Q3FY26 call (CC-Feb, 05-Feb-2026) contains **no** reference to a one-time treasury gain, MTM or other income. A grep for mark-to-market, MTM, treasury, one-time, other income, gain, yield and fair value returned no treasury hit. Its only treasury content is the cash answer quoted in A3.1 (p.14). The item appears in the **Q4FY26 call (CC-Apr)**, where the CFO looks back at the December quarter. **CONFLICT with the request premise:** the item comes from the Apr-2026 call, not the Feb-2026 call.

CC-Apr p.9-10 [MGMT]. Question from Sumit Kishore (Axis Capital): "The other income seems to have slowed down versus the quarterly run rate over the last four-odd quarters, down about 29%. Anything to call out here?"
Answer from Vineet Harlalka (CFO), p.10: "Sumit the major reason was that if you look at the December quarter number, it was a significant increase over the treasury income because there was a one-time gain we got because the interest rates were there and the market was improving. And as you all know, because of the Iran conflict and rupee situation, there was a significant correction in the market during this month of March. So a bit of mark-to-market impacts were there. And that was reflecting in the numbers. And the previous quarter, there was onetime gains. Those were there. And as the market is recovering, we will see that the numbers going back to the earlier numbers." Follow-up (p.10), Kishore: "there are some non -recurring factors which have depressed ..." Harlalka: "Yes. Right."

- **Amount:** NOT DISCLOSED. Management gives no rupee figure for the Q3 one-time gain or the Q4 MTM impact.
- **Instrument:** NOT DISCLOSED. Management names none.
- **Accounting:** NOT DISCLOSED as a separate item.

**Filed search.** Q4R and AR26 do not name the item. What is filed:
- Q4R standalone p.6: "2 Other income 2,211,41 3,742.01 3,098.43 13.655.11 11,892.43" (Q4FY26 | Q3FY26 | Q4FY25 | FY26 | FY25). Consolidated p.15: "2 Other income 2,213.66 3,739 68 3,234.66 13,130 47 12.010 46". Comment: the quarterly swing the CFO described is visible only as the total. Q4R has no exceptional item and no note on treasury. Its notes 1-9 (pp.7-10) cover the balance sheet, approvals, Ind AS basis, segment, ESOP, balancing figures, dividend, labour codes and filing.
- Q4R cash-flow adjustments, full year only (p.8): "Fair value gain on investments measured at fair value through profit or loss (3,397.39) (4,123.64)", "Gain on sale of investments measured at fair value through profit or loss (net) (2,328.88) (1,680.79)", "Gain on sale of investments measured at amortised cost (net) (809.24)". Comment: the FY26 "gain on sale of investments measured at amortised cost" of 809.24 is new in FY26 (FY25: nil). Neither filing links it to the call's "one-time gain". Any link would be inference and is not drawn here.
- AR26 MD&A (p.64): "Treasury and other income of the Company stood at `13,655.11 lakh as compared to `11,892.43 lakh during the previous year, with a growth rate of 14.82% which was mainly due to increase in average investment from 1,363 cores in FY'25 to 1,595 crores in FY'26." Comment: no one-time or MTM item is named.
- AR26 ratio note (p.226): "Return on investments (in %) ... 8.41% 8.52% -1.27%". Consolidated (p.288): "8.40% 8.52% -1.38%".
- Quarterly MTM split: NOT DISCLOSED. The AR gives only annual figures. Pointer: a quarterly breakdown would sit in the Q3FY26 results (not in corpus) or the Q4 investor presentation (presentation__Investor_Presentation_Q4FY26_2026-04-23.txt, outside this request's file list and not read).

---

## B1. Other financial liabilities, other liabilities and provisions

### B1.1 Standalone [FILED]

AR26 Note 19, Other financial liabilities, non-current (p.208):
| Line (verbatim) | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| "Deposits towards settlement guarantee fund (refer note 53)" | 187.06 | 268.18 |
| "Deposit from employees" | 25.32 | 50.15 |
| "Total" | 212.38 | 318.33 |

AR26 Note 24, Other financial liabilities, current (p.210):
| Line (verbatim) | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| "Deposits towards settlement guarantee fund (refer note 53)" | 2,342.04 | 2,138.30 |
| "Trading margin deposits (refer note 54)" | 17,126.35 | 16,419.77 |
| "Deposit from employees" | 38.56 | 6.92 |
| "Creditors for capital goods - Total outstanding dues of micro enterprises and small enterprises (refer note 52)" | 6.38 | 70.14 |
| "- Total outstanding dues of creditors other than micro enterprises and small enterprises" | - | - |
| "Unpaid dividends" | 113.71 | 79.44 |
| "Employee related payables" | 727.98 | 799.73 |
| "Settlement obligation payable" | 75,313.88 | 75,430.63 |
| "Deposit from clearing and settlement bankers" | 1,800.00 | 1,800.00 |
| "Total" | 97,468.90 | 96,744.93 |

AR26 Note 25, Other liabilities, current (p.210):
| Line (verbatim) | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| "Deferred income settlement guarantee fund" | 26.25 | 37.99 |
| "Unamortised subscription and admission fee income [refer note 25(a) below]" | 1,184.67 | 1,176.41 |
| "Advance from customers" | 178.80 | 74.60 |
| "Statutory dues payables" | 1,254.82 | 1,024.14 |
| "Total" | 2,644.54 | 2,313.14 |

Note 25(a) (p.210): "Classified as Non-Current: 151.84 196.62". Comment: this is the non-current unamortised fee income. The non-current other-liabilities note itself was not read.

AR26 Note 20, Provisions, non-current (p.208): "Gratuity (refer note 36) 727.52 651.42", "Compensated absences 568.37 491.94", "Total 1,295.89 1,143.36".
AR26 Note 26, Provisions, current (p.210): "Gratuity (refer note 36) 18.33 6.80", "Compensated absences 14.34 22.36", "Total 32.67 29.16".
AR26 Note 27 (p.210): "Current tax liabilities (net) 742.06 767.00".

Q4R standalone check (p.7): "(ii) Other financial liabilities 212.38 318.33", "Provisions 1,295.89 1,143.36", "(iii) Other financial liabilities 97,468.90 96,744.93", "Other current liabilities 2,644.54 2,313.14", "Provisions 32.67 29 16". These agree with AR26.

AR25 standalone, 31-Mar-2024 comparatives (AR25 Note 24, p.201): "Deposits towards settlement guarantee fund (refer note 51) 2,138.30 2,001.29", "Trading margin deposits (refer note 52) 16,419.77 11,248.03", "Unpaid dividends 79.44 33.86", "Settlement obligation payable 75,430.63 56,008.82", "Deposit from clearing and settlement bankers 1,800.00 1,800.00", "Total 96,744.93 71,708.68". AR25 Note 19 (p.199): "Deposits towards settlement guarantee fund (refer note 51) 268.18 142.96". The 31-Mar-2025 values agree with AR26.

### B1.2 Consolidated [FILED]

AR26 consolidated Note 18 (p.269): "Deposits towards settlement guarantee fund (refer note 50) 187.06 268.18", "Deposit from employees 25.32 50.15", "Total 212.38 318.33".
Consolidated Note 23 (p.271). These rows are the same as standalone: SGF 2,342.04 | 2,138.30, trading margin 17,126.35 | 16,419.77, unpaid dividends 113.71 | 79.44, settlement obligation payable 75,313.88 | 75,430.63, clearing and settlement bankers 1,800.00 | 1,800.00, MSME capital creditors 6.38 | 70.14. These rows differ: "Deposit from employees 38.56 7.39", "Employee related payables 739.48 825.77", "Total 97,480.40 96,771.44".
Consolidated Note 24 (p.272): "Deferred income settlement guarantee fund 26.25 37.99", "Unamortised subscription and admission fee income ... 1,184.67 1,176.41", "Advance from customers 178.80 74.60", "Statutory dues payables 1,271.91 1,031.05", "Total 2,661.63 2,320.05".
Consolidated Note 25, Provisions, current (p.272): "Gratuity (refer note 35) 18.35 6.95", "Compensated absences 14.47 22.64", "Total 32.82 29.59". Consolidated Note 26: "Current tax liabilities(net) 746.51 767.00".
Consolidated provisions, non-current: Q4R p.16 prints "Provisions 1,310.38 1,180.64". The line-level consolidated Note 19 was not read. The total is taken from Q4R.
Q4R consolidated check (p.16): "(ii) Other financial liabilities 212.38 318.33", "(iii) Other financial liabilities 97,480.40 96,771.44", "Other current liabilities 2,661.63 2,320.05", "Provisions 32.82 29.59".

### B1.3 How the filing itself describes each line (quoted; no classification of my own)

- **SGF deposits:** "The members are required to contribute interest free margin money which forms part of the SGF. ... The margin money is refundable, subject to adjustments, if any." (AR26 Note 53, p.230. Consolidated Note 50, p.291)
- **Trading margin deposits:** "The Company receives trading margin deposits from the members corresponding to their average trading volume during last 7 days. Trading margin money is refundable, subject to adjustments, if any." (AR26 Note 54, p.230. Consolidated Note 51, p.291)
- **Settlement obligation payable:** no note defines it. The closest filed description is in the credit-risk note (AR26 p.221): "As a process, the Company collects the amounts from buyer for purchase of power, including transmission and other charges and exchange fees on or before the delivery and pays out the amount to seller for sale of power one day after delivery. Further, transmission charges etc. are paid to system operator on the next day from the day of trade." The filing does not label the payable "member money" or "own funds". A definition would sit in AR26 accounting policies (pp.186-192), which have no settlement-obligation policy text, or in Note 24 (p.210). Status: NOT DISCLOSED as a labelled classification.
- **Deposit from clearing and settlement bankers (1,800.00):** NOT DISCLOSED. No description or note reference appears anywhere in AR26 (pointer: Note 24 p.210, consolidated Note 23 p.271).
- **Unpaid dividends:** held in "In earmarked accounts - Current Accounts (unpaid dividend) #", with "#Restricted bank balances which are to be used for specified purposes." (AR26 pp.203-204)
- **Deposit from employees, employee payables, statutory dues, provisions:** no member-money description is given.
- **The filing's own "member money vs company's own" split of liabilities: NOT DISCLOSED** as a single statement.

---

## B2. Settlement Guarantee Fund

AR26 Note 53, verbatim (p.230) [FILED]:
"53. The Company had constituted a separate 'Settlement Guarantee Fund' ('SGF') in respect of the activities carried out in various contracts being traded at the exchange platform. The members are required to contribute interest free margin money which forms part of the SGF. However, as per CERC order dated 9 October 2018, the Company has to share 70% of the return earned on 'initial security deposits' with the Members. The margin money is refundable, subject to adjustments, if any. Such fund is also termed as Settlement Guarantee Fund. The Cash Margin Money forming part of SGF is `2529.10 (previous year `2,406.48) and same has been disclosed under note 24- Other current financial liabilities i.e. `2342.04 (previous year `2,138.30) under Deposits towards Settlement Guarantee Fund and note 19- Other non current financial liabilities- Deposits towards Settlement Guarantee Fund i.e. `187.06 (previous year `268.18). These balances have been accounted for on amortised cost basis. The Company had also collected non cash portion of the Settlement Fund comprising collateral such as bank guarantees, received from the members amounting to `25.00 (previous year `65.00) which does not form part of the Balance Sheet."

- **Size:** cash margin forming part of the SGF is 2,529.10 at 31-Mar-2026 and 2,406.48 at 31-Mar-2025. Non-cash bank guarantees are 25.00 and 65.00, off balance sheet. AR25 Note 51 (p.221) gives the prior year: "`2,406.48 (previous year `2,144.25)", with non-cash "`65.00 (previous year `175.00)".
- **Funding source:** per the note, member contributions ("interest free margin money"), with 70% of the return on initial security deposits shared with members. A Company-own contribution to the SGF: NOT DISCLOSED (pointer: Note 53 p.230, and the corporate governance report SGF committee item, p.114).
- **Where it is held:** NOT DISCLOSED. No note says whether SGF cash sits in investments, in a separate bank account or with the general treasury. Notes 10, 12 and 13 have no SGF-designated line (pointer: AR26 pp.199-204, 230).
- **Related lines:** "Deferred income settlement guarantee fund 26.25 37.99" (Note 25, p.210). Q4R cash-flow adjustments (p.8): "Interest expense on financial liabilities (settlement guarantee fund) measured at amortised cost 44.13 42.35" and "Amortisation of deferred settlement guarantee fund (43.75) (45.78)".
- **Governance (AR26 p.114):** "The Board has constituted Settlement Guarantee Fund (SGF) Management Committee as per Clause (i) of Regulation 27 (1) of CERC PMR 2021. The said Committee, inter-alia, monitors the adherence of regulatory directions in respect of Settlement Guarantee Fund (SGF), contribution of Members to the SGF, its investment, utilization and recoupment of SGF in case it is utilized to meet residual defaults ..."
- **Trading margin deposits, the related member-cash pool (Note 54, p.230):** "The Cash Margin Money forming part of trading margin deposits is `17,126.35 (previous year `16,419.77) ... The Company has also collected non cash portion of the trading margin deposits comprising collateral such as bank guarantees, received from the members amounting to `3,935.00 (previous year `2,230.00) which does not form part of the Balance Sheet."
- **Consolidated Note 50 (p.291)** is word for word the same as standalone Note 53, amounts included. **Cross-reference defect, flagged:** consolidated Note 50 still points to "note 24" and "note 19", but the consolidated notes carrying these lines are Note 23 (p.271) and Note 18 (p.269). Consolidated Note 51 also points to "note 24". Reported as printed.

---

## B3. Restrictions on cash or investments

[FILED], AR26 standalone. Consolidated notes carry the same text on pp.259, 264, 265.
1. **Lien on current investments (overdraft and SBLC):** "*Investments includes `34,323.06 (cost) [(31 March 2025: `32,205.62) (cost)] under lien with banks for overdraft and standby letter of credit (SBLC facilities)." (p.202). The instruments marked * in A2.1 are the ones under lien. AR25 (p.194) gives 31-Mar-2024: "`8,609.86".
2. **Lien on non-current investments:** "*Investments includes Nil (cost) [(31 March 2025: `3,199.33) (cost)] under lien with banks for overdraft facilities." (p.198). AR25 (p.190) gives 31-Mar-2024: "`18,177.99".
3. **Lien on bank deposits:** "*Bank deposits includes `5,190.00 (31 March 2025: Nil) under lien with banks for overdraft facilities." (Note 13, p.204). "*Bank deposits includes Nil (31 March 2025: `5,190.00) under lien with banks for overdraft facilities." (Note 7, p.199).
4. **Earmarked or restricted balance:** "In earmarked accounts - Current Accounts (unpaid dividend) # 113.71 79.44", with "#Restricted bank balances which are to be used for specified purposes." (pp.203-204)
5. **Facilities the liens secure (Note 42, p.222):** "Overdraft (including SBLC) facilities from banks* 29,500.00 29,500.00" (undrawn), "* the overdraft (including SBLC) facilities may be drawn at any time". Comment: the lien and SBLC facility is IEX's own. The filing does not say what the SBLC backs (pointer: Note 42 p.222, contingent liabilities note, not located in this pass).
6. **Regulatory earmarking of SGF or margin money in specific assets:** NOT DISCLOSED (see B2 pointer). The only related statement is the governance text on p.114 on the SGF committee monitoring "its investment".
7. **Escrow or pledge:** NOT DISCLOSED. A grep of AR26 for escrow and pledge found no treasury use. Pointer: AR26 Notes 7, 10, 12, 13 (pp.199-204).
8. **Lien marking conflicts:** see A2.1 (SBI Arbitrage asterisk, AR25 vs AR26) and A2.2 (FMP asterisk, consolidated vs standalone).

---

## CLOSING

**Documents quoted (filename, date):**
- annual-report__Annual_Report_2026.txt: FY26 Annual Report, filed BSE 14-Aug-2026 (per request). Pages cited: 64, 114, 119, 197-204, 208, 210-211, 221-224, 226, 230, 240, 258-266, 269, 271-272, 283, 285, 288, 291.
- annual-report__Annual_Report_2025.txt: FY25 Annual Report. Pages cited: 188-196, 199, 201-202, 213, 221.
- results__FY26_Q4_Audited_Results_2026-04-23.txt: audited FY26 results dated 23-Apr-2026. Pages 6-8, 15-16.
- results__Q1FY27_Results_Unaudited_2026-07-23.txt: cover dated 23-Jul-2026. Pages 4, 9.
- concalls__Concall_Feb_2026_Transcript.txt: cover dated 05-Feb-2026. Page 14.
- concalls__Concall_Apr_2026_Transcript.txt: cover dated 30-Apr-2026, page header "April 24, 2026". Pages 9-10.
- concalls__Concall_Jul_2026_Transcript.txt: cover dated 31-Jul-2026. Page 28 (a negative search result).
- other__Concall_Nov_2025_Q2FY26_Transcript.txt: cover dated 07-Nov-2025. No treasury content found.

**NOT DISCLOSED, with pointers:**
1. Every investment item at 30-Jun-2026. Q1R has no balance sheet. It would be in the H1FY27 results (30-Sep-2026), which are not in the corpus.
2. Credit rating of every bond and CP, non-current and current. It would be in AR26 Notes 6/10 (pp.197-202, 258-264) or Note 42 credit risk (pp.221, 282). It is not printed.
3. Maturity date of every CP and bond. Same pointer. FMP and TMF tenor appears only inside scheme names.
4. Split of cash and investments between own funds and member money. It would be in AR26 Notes 12/13 (pp.203-204), 53/54 (p.230) or 42 liquidity (p.222). Management gives only a rounded 31-Dec-2025 figure (CC-Feb p.14).
5. Quarterly MTM and one-time treasury item: amount, instrument and accounting. Not in Q4R (pp.6-10) or AR26 (p.211, p.64). Candidate sources outside this file list: Q3FY26 results and the Q4FY26 investor presentation.
6. Default on any investment in FY25, FY26 or Q1FY27. No note records one. Q1FY27 has no investment disclosure at all.
7. Definition of "Settlement obligation payable" and of "Deposit from clearing and settlement bankers". Pointer: AR26 Note 24 (p.210) and accounting policies (pp.186-192).
8. Where the SGF corpus is held, and any Company-own SGF contribution. Pointer: AR26 Note 53 (p.230) and p.114.
9. Escrow or pledge on treasury assets. Pointer: AR26 Notes 7, 10, 12, 13.

**CONFLICTS flagged (not reconciled):**
- (a) The request places the one-time treasury MTM item in the Feb-2026 call. It is in the Apr-2026 call (CC-Apr p.10).
- (b) Nippon India Liquid Fund 31-Mar-2025 unit count: AR26 p.202 vs AR25 p.193.
- (c) SBI Arbitrage Opportunities lien asterisk: AR26 p.202 vs AR25 p.193.
- (d) FMP lien asterisk: consolidated AR26 p.262 vs standalone p.201.
- (e) Consolidated Note 50/51 cross-references to notes 24/19, which should be 23/18 (AR26 p.291).
- (f) Aggregate amortised-cost book value: 33,968.99 standalone (p.202) vs 33,968.98 consolidated (p.264). TMF/FMP line: 7,814.30 (p.223) vs 7,814.29 (p.285).

---

# IEX P2 extraction, Parts C and D (other income, tax, treasury policy, cash flow quality)

Corpus-only. No web. Figures in Rs lakhs as printed. Page = the "=== PAGE n ===" marker number in the extracted text (not the printed folio). Source dir: runs/iex-2026-09-08/work/.

Abbreviations for sources:
- AR26 = annual-report__Annual_Report_2026.txt (FY26 AR, filed BSE 14-Aug-2026) [FILED]
- AR25 = annual-report__Annual_Report_2025.txt (FY25 AR, FY24 comparatives) [FILED]
- R-Q4 = results__FY26_Q4_Audited_Results_2026-04-23.txt [FILED]
- R-Q1 = results__Q1FY27_Results_Unaudited_2026-07-23.txt [FILED]
- CC-Apr = concalls__Concall_Apr_2026_Transcript.txt (cover letter "Dated: April 30, 2026"; Q4FY26 call) [MGMT]
- CC-Jul = concalls__Concall_Jul_2026_Transcript.txt (cover letter "Dated: July 31, 2026"; Q1FY27 / analyst meet) [MGMT]
- P-Q4 = presentation__Investor_Presentation_Q4FY26_2026-04-23.txt [MGMT]
- P-AM = presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt [MGMT]

---

## C1. Other income

### C1.1 Standalone, full-year split (annual notes) [FILED]

FY26 and FY25: AR26 p.211, Note 29 "Other income" (columns: FY26, FY25). FY24: AR25 p.203, Note 29 (columns: FY25, FY24).

| Row as printed | FY26 (AR26 p.211) | FY25 (AR26 p.211) | FY25 (AR25 p.203) | FY24 (AR25 p.203) | Requested bucket |
|---|---|---|---|---|---|
| Interest income from bank deposits | 508.80 | 367.99 | 367.99 | 340.58 | interest, deposits |
| Interest income from financial assets measured at amortised cost (security deposits) | 22.85 | 20.59 | 20.59 | 18.60 | interest, other |
| Interest income on investments measured at amortised cost | 5,750.97 | 5,453.53 | 5,453.53 | 4,232.49 | interest, bonds/CPs |
| Gain on sale of investments measured at amortised cost (net) | 809.24 | - | row not printed | row not printed | realised gain, amortised-cost book |
| Interest income on loans | 3.34 | 1.06 | 1.06 | - | interest, other |
| Dividend income | 536.55 | 18.71 | 18.71 | 29.99 | dividend |
| Gain on sale of investments measured at fair value through profit or loss (net) | 2,328.88 | 1,680.79 | 1,680.79 | 2,034.81 | MF / FVTPL gains realised |
| Fair value gain on investments measured at fair value through profit or loss (net) | 3,397.39 | 4,123.64 | 4,123.64 | 3,343.50 | FV gains unrealised |
| Provision/ liabilities no longer required written back | - | 1.71 | 1.71 | - | other |
| Business support services | 65.42 | 101.00 | 101.00 | 115.84 | other |
| Miscellaneous income | 231.67 | 123.41 | 123.41 | 47.03 | other |
| Total | 13,655.11 | 11,892.43 | 11,892.43 | 10,162.84 | |

Verbatim anchors:
- AR26 p.211: "Gain on sale of investments measured at fair value through profit or loss (net) 2,328.88 1,680.79" / "Fair value gain on investments measured at fair value through profit or loss (net) 3,397.39 4,123.64" / "Total 13,655.11 11,892.43". Comment: FY25 comparatives in AR26 match AR25 as printed.
- AR25 p.203: "Interest income on investments measured at amortised cost 5,453.53 4,232.49" / "Total 11,892.43 10,162.84".
- Comment on bucket mapping: the filing does not use the words "realised" or "unrealised" and does not name "mutual funds" in the caption. The mapping above is by caption only ("Gain on sale ..." = realised; "Fair value gain ..." = remeasurement). The FVTPL book composition is in AR26 p.224 (see C3: "Investments in Mutual funds 1,08,430.63", InvIT, Equity Index MF, MLD).
- MF-specific split of FVTPL gains: NOT DISCLOSED. Would be in AR26 Note 29 sub-analysis or Note 41 fair value measurement; not printed in either.

Treasury label in MD&A [FILED]: AR26 p.64 KPI table: "Treasury Income 13,655.11 11,892.43 14.82 13,130.47 12,010.46 9.33". Comment: the MD&A calls the whole Other income line "Treasury Income", including business support services and miscellaneous income.

AR26 p.64: "Treasury and other income of the Company stood at `13,655.11 lakh as compared to `11,892.43 lakh during the previous year, with a growth rate of 14.82% which was mainly due to increase in average investment from 1,363 cores in FY'25 to 1,595 crores in FY'26." Comment: no FY26 yield figure is printed.

AR25 p.61: "Treasury and other income of the Company stood at ` 11,892.43 lakh as compared to ` 10,162.84 lakh during the previous year, with a growth rate of 17.02% which was mainly due to increase in average investment from ` 1,227 cores in FY24 to ` 1,362 crores in FY25 and increase in yield on investment from 8.07% to 8.53%."
- CONFLICT: FY25 average investment is "1,362 crores" in AR25 p.61 and "1,363 cores" in AR26 p.64. Reported both, not reconciled.

### C1.2 Consolidated, full-year split (annual notes) [FILED]

FY26 and FY25: AR26 p.273, Note 28. FY24: AR25 p.263, Note 28.

| Row as printed | FY26 (AR26 p.273) | FY25 (AR26 p.273) | FY25 (AR25 p.263) | FY24 (AR25 p.263) |
|---|---|---|---|---|
| Interest income from bank deposits | 508.80 | 370.87 | 370.87 | 340.81 |
| Interest income from financial assets measured at amortised cost (security deposits) | 22.85 | 20.59 | 20.59 | 18.60 |
| Interest income on investments measured at amortised cost | 5,750.97 | 5,453.53 | 5,453.53 | 4,232.49 |
| Gain on sale of investments measured at amortised cost (net) | 809.24 | - | row not printed | row not printed |
| Dividend income | 4.65 | 18.71 | 18.71 | 29.99 |
| Gain on sale of investments measured at fair value through profit or loss (net) | 2,331.16 | 1,684.22 | 1,684.22 | 2,063.60 |
| Fair value gain on investments measured at fair value through profit or loss (net) | 3,415.36 | 4,126.22 | 4,126.22 | 3,346.54 |
| Provision/ liabilities no longer required written back | - | 1.71 | 1.71 | - |
| Business support services | 31.22 | 68.20 | 68.20 | 90.46 |
| Miscellaneous income | 256.22 | 266.41 | 266.41 | 47.03 |
| Total | 13,130.47 | 12,010.46 | 12,010.46 | 10,169.52 |

- AR26 p.273: "Dividend income 4.65 18.71" / "Total 13,130.47 12,010.46". Comment: consolidated FY26 dividend income is 4.65 against standalone 536.55. The associate dividend is kept out of consolidated income; see AR26 p.66 below.
- AR26 p.66 [FILED]: "During FY'26, the Company received a dividend from its associate company amounting to `531.90 lakh (previous year: Nil). In accordance with the equity method of accounting of Investment, this has been accounted against the carrying value of the investment in associate and is not included in the consolidated total income."
- No "Interest income on loans" row in the consolidated note (the standalone loan was to subsidiary ICX, eliminated).

### C1.3 Quarterly totals (results filings) [FILED]

Quarterly split by component: NOT DISCLOSED in any results filing in the corpus. Results filings print only the "Other income" total. A split would be in the quarterly limited-review notes, which do not carry it.

Standalone, R-Q4 p.6 (columns Q4FY26 | Q3FY26 | Q4FY25 | FY26 | FY25):
"2 Other income 2,211,41 3,742.01 3,098.43 13.655.11 11,892.43"
Comment: OCR prints "2,211,41" and "13.655.11"; R-Q1 p.4 prints the same Q4FY26 value as "2,211.41" and FY26 as "13,655.11".

Standalone, R-Q1 p.4 (columns Q1FY27 | Q4FY26 | Q1FY26 | FY26):
"2 Other income 4,491.58 2,211.41 4,252.37 13,655.11"

Consolidated, R-Q4 p.15 (columns Q4FY26 | Q3FY26 | Q4FY25 | FY26 | FY25):
"2 Other income 2,213.66 3,739 68 3,234.66 13,130 47 12.010 46"

Consolidated, R-Q1 p.9 (columns Q1FY27 | Q4FY26 | Q1FY26 | FY26):
"2 Other income 4,493 27 2,213.66 4,242_81 13,130.47"

| Period | Standalone | Consolidated | Source |
|---|---|---|---|
| Q1FY26 | 4,252.37 | 4,242.81 (printed "4,242_81") | R-Q1 p.4 / p.9 |
| Q2FY26 | NOT DISCLOSED | NOT DISCLOSED | Q2FY26 results filing (Oct/Nov-2025), not collected |
| Q3FY26 | 3,742.01 | 3,739.68 (printed "3,739 68") | R-Q4 p.6 / p.15 |
| Q4FY26 | 2,211.41 | 2,213.66 | R-Q4 p.6 / p.15; R-Q1 p.4 / p.9 |
| Q1FY27 | 4,491.58 | 4,493.27 (printed "4,493 27") | R-Q1 p.4 / p.9 |
| Q4FY25 (comparative) | 3,098.43 | 3,234.66 | R-Q4 p.6 / p.15 |

Q2FY26 not derived from FY26 less other quarters (rule 3: no computed subtotals).

Management commentary on the Q4FY26 drop [MGMT], CC-Apr p.9 (question): "The other income seems to have slowed down versus the quarterly run rate over the last four-odd quarters, down about 29%." CC-Apr p.10 (CFO Vineet Harlalka): "if you look at the December quarter number, it was a significant increase over the treasury income because there was a one-time gain we got because the interest rates were there and the market was improving." and "there was a significant correction in the market during this month of March. So a bit of mark-to-market impacts were there." Comment: management attributes Q3FY26 to one-time gains and Q4FY26 to MTM losses; the one-time gain is not quantified.

P-Q4 p.26 [MGMT]: "Other Income 18.1% 20.7% 11.4% 18.3%" (columns Q4FY25, Q3FY26, Q4FY26, FY26; share of standalone revenues).

P-AM p.38 [MGMT], total income chart, text as extracted: "73 102 119 137 43 45" and "401 449 535 608 140 156", legend "Operating Revenue / Treasury Income / Total Income (INR Cr) / Others", columns "FY23 FY24 FY25 FY26 Q1FY26 Q1FY27". Comment: the text extraction does not bind each number series to its legend label; values are quoted as extracted, INR crore.

### C1.4 Consolidated share of profit of associate (IGX) [FILED]

- R-Q4 p.15: "6 Share in profit of associate (net of tax) 441 39 417.33 422 86 1,979 53 1,463.15" (Q4FY26, Q3FY26, Q4FY25, FY26, FY25).
- R-Q1 p.9: "6 Share in profit of associate (net of tax) 771 88 441.39 668.26 1,979.53" (Q1FY27, Q4FY26, Q1FY26, FY26).
- AR26 p.68: "Share in profit of associate - - 1,979.53 1,463.15" (standalone FY26, FY25; consolidated FY26, FY25).
- AR25 p.61: "Share in profit of associate - - - 1,463.15 1,089.79 34.26" (consolidated FY25, FY24, growth %).
- AR26 p.66: "As on March 31, 2026, the company holds 47.28% (previous year 47.28%) stake in IGX. Share in profit of associate for FY'26 was `1,979.53 lakh (previous year `1,463.15 lakh)."

| Period | Share of associate | Source |
|---|---|---|
| FY24 | 1,089.79 | AR25 p.61; AR25 p.234 CF "(1,089.79)" |
| FY25 | 1,463.15 | AR26 p.68; R-Q4 p.15 |
| FY26 | 1,979.53 | AR26 p.68; R-Q4 p.15 |
| Q1FY26 | 668.26 | R-Q1 p.9 |
| Q2FY26 | NOT DISCLOSED | Q2FY26 consolidated results filing (Oct/Nov-2025), not collected |
| Q3FY26 | 417.33 | R-Q4 p.15 |
| Q4FY26 | 441.39 | R-Q4 p.15; R-Q1 p.9 |
| Q1FY27 | 771.88 | R-Q1 p.9 |

---

## C2. Tax on other income

Effective tax rate on other income as a separate figure: NOT DISCLOSED. Would sit in AR26 Note 34 (standalone) / Note 33 (consolidated) if split; neither splits by income type. The governing disclosure is the rate-reconciliation line below.

### Standalone [FILED]

AR26 p.213, Note 34(iii) "Reconciliation of tax expense and the accounting profit multiplied by India's domestic tax rate" (FY26, FY25):
- "Profit before tax 62,480.56 55,021.00"
- "Enacted tax rates in India 25.17% 25.17%"
- "Computed expected tax (expenses)/credit 15,726.36 13,848.79"
- "Non-deductible tax expenses 278.19 243.57"
- "Tax on exempt income (7.93) (8.94)"
- "Tax for earlier years (38.57) (3.37)"
- "Others including difference in tax rate on capital gain on sale on investments (848.28) (523.87)"
- "Tax expense 15,109.77 13,556.18"
Comment: the capital-gains rate difference is bundled into one "Others" line. It is not split from other items.

AR26 p.213, Note 34(i): "Current tax 15,714.48 13,168.22" / "Tax for earlier years (38.57) (3.37)" / "Origination and reversal of temporary differences (566.14) 391.33" / "Total tax expense charged to the statement of profit & loss 15,109.77 13,556.18".

AR25 p.205, Note 34(iii) (FY25, FY24):
- "Profit before tax 55,021.00 45,684.90"
- "Enacted tax rates in India 25.17% 25.17%"
- "Computed expected tax (expenses)/credit 13,848.79 11,498.89"
- "Non-deductible tax expenses 243.57 206.62"
- "Tax on exempt income (8.94) (10.88)"
- "Tax for earlier years (3.37) 51.81"
- "Others including difference in tax rate on capital gain on sale on investments (523.87) (205.60)"
- "Tax expense 13,556.18 11,540.84"
AR25 p.205 Note 34(i): "Origination and reversal of temporary differences 391.33 863.98".

MD&A ETR [FILED], AR26 p.65: "Effective tax rate in FY'26 is at 24.18% as compared with 24.64% in FY'25."

### Consolidated [FILED]

AR26 p.275, Note 33(iii) (FY26, FY25):
- "Profit before tax 64,556.32 56,453.60"
- "Enacted tax rates in India 25.17% 25.17%"
- "Computed expected tax expenses 16,248.83 14,209.37"
- "Non-deductible tax expenses 278.19 243.57"
- "Tax-exempt income (7.93) (8.94)"
- "Tax for earlier years (38.57) (3.37)"
- "Others including difference in tax rate on capital gain on sale on investments (1,216.32) (903.94)"
- "Tax expense 15,264.20 13,536.69"
Comment: consolidated PBT includes the share of associate (post-tax), so the consolidated "Others" line also carries that effect. The note does not split it out.

AR26 p.275 Note 33(i): "Current tax 15,843.54 13,169.73" / "Origination and reversal of temporary differences (540.77) 370.33" / "Total tax expense charged to P&L 15,264.20 13,536.69".

AR25 p.265, Note 33(iii) (FY25, FY24): "Profit before tax 56,453.60 46,614.33" / "Computed expected tax (expenses)/credit 14,209.37 11,732.83" / "Others including difference in tax rate on capital gain on sale on investments (903.94) (444.31)" / "Tax expense 13,536.69 11,536.07".

Quarterly tax [FILED]: R-Q4 p.6 standalone "Total tax expense 3,894.81 3,611.26 3,507.10 15,109.77 13,556.18"; "Deferred tax (credit) / charge (119 08) (386.57) (213 39) (566.14) 391.33". Comment: the filing does not state the driver of the quarterly deferred tax credit.

---

## C3. Treasury / investment policy

Written investment policy text (permitted instruments, rating floor, tenor, concentration limits): NOT DISCLOSED. The policy itself is not reproduced in AR26 or AR25. It would be the Board-approved Investment Policy document (company internal / website), not in the corpus.

Who approves [FILED], AR26 p.113, Board committees table: "1 Investment Committee ... Mr. Satyanarayan Goel (Chairperson) Chairman & Managing Director ... The Investment Committee approves the overall investment policy of the Company as well as any subsequent changes therein within the overall scope and framework of the policy and oversees the implementation of the policy." Members listed: "Mr. Rajeev Gupta (Member) Non- Executive Independent Director", "Mr. Gautam Dalmia (Member) Non-Executive Non-Independent Director", "Mr. Amit Garg (Member) Non-Executive Non-Independent Director", "Mr. Rohit Bajaj (Member) Joint Managing Director" (AR26 p.113). Same terms of reference at AR25 p.110.

Board's Report [FILED], AR26 p.79: "All investments made during FY'26 were duly approved and carried out in compliance with the provisions of Section 186 of the Companies Act, 2013." and "continues to follow a prudent approach in its financial and treasury operations."

Risk framework [FILED], AR26 p.220, Note 42: "The Board provides written principles for overall risk management, as well as policies covering specific areas, such as regulatory risk, compliance risk, technology related risk, IT risk, interest rate risk, credit risk, use of derivative financial instruments and non-derivative financial instruments, and investment of excess liquidity. The Company's risk management is carried out by an Enterprise Risk Management Committee under risk policy approved by the Board."

Credit risk of investments [FILED], AR26 p.221, Note 42:
"Credit risks on cash and cash equivalents and bank deposits is limited as the Company generally invests in deposits with banks with high credit ratings assigned by domestic credit agencies. Investments primarily include investments in mutual fund units, commercial papers, market linked debentures, infrastructure investment units, target maturity funds, fixed maturity plans and investment in bonds with fixed interest income. The management actively monitors the net asset value of investments in mutual funds, infrastructure investment units, interest rate and maturity period of investment in bonds and commercial papers. The Company does not expect the counterparty to fail in meeting its obligations. However, investment in target maturity funds, fixed maturity plans, market linked debentures are exposed to uncertainties as regards to fulfilment of obligations by counter-party. The Company has not experienced any significant impairment losses in respect of any of the investments."
Comment: "high credit ratings" is the only rating language; no numeric floor (e.g. AAA/A1+) is printed. Consolidated equivalent at AR26 p.282, Note 41.

Exposure [FILED], AR26 p.221: "Investments (Non current and current) 1,93,592.03 1,59,708.20" / "Cash and cash equivalents 3,651.72 10,663.55" / "Other Bank balance 6,782.25 601.08" (31-Mar-26, 31-Mar-25).

Interest-bearing book [FILED], AR26 p.223: "Investments in bonds 11,044.95 8,185.31" / "Commercial papers 51,453.53 26,701.87" / "Target Maturity funds and Fixed Maturity Plan 7,814.30 30,636.93" / "Bank deposits 7,178.31 10,768.21" / total "77,491.09 76,292.32".

Market-priced book [FILED], AR26 p.224: "Investments in Units of InvIT 3,089.51 1,069.12" / "Equity Index Mutual Fund 7,590.88 1,996.07" / "Investments in Enviro Enablers India Private Limited 122.22 122.22" / "Investments in Mutual funds 1,08,430.63 85,124.56" / "Investments in Market Linked Debentures (MLD) - 1,826.07" / total "1,19,233.24 90,138.04".
Sensitivity, AR26 p.224: "a 0.25% increase in prices would have led to approximately an additional ` 279.11 gain in the Statement of Profit and Loss (2024-25 `220.35 gain)" and "For investment in Equity Index Mutual Fund, a 5% increase in prices would have led to approximately an additional ` 379.54 gain in the Statement of Profit and Loss (2024-25: `99.80 gain)."
AR26 p.224: "The Company's fixed rate instruments are carried at amortised cost. They are therefore not subject to interest rate risk, since neither the carrying amount nor the future cash flows will fluctuate because of a change in market interest rates."
Comment: equity index MF exposure rose from 1,996.07 to 7,590.88. This is a policy-relevant observation; the policy limit for equity exposure is NOT DISCLOSED (pointer as above).

Tenor limits and concentration limits: NOT DISCLOSED (would be in the Investment Policy; AR26 Note 42 prints no maturity-bucket limit for investments).

---

## D1. CFO before and after working capital

### Standalone [FILED]

Sources: FY26 and FY25, AR26 p.183 (standalone cash flow). FY24, AR25 p.175. R-Q4 p.8 repeats FY26/FY25 identically.

| Row as printed | FY26 (AR26 p.183) | FY25 (AR26 p.183) | FY25 (AR25 p.175) | FY24 (AR25 p.175) |
|---|---|---|---|---|
| Profit before tax | 62,480.56 | 55,021.00 | 55,021.00 | 45,684.90 |
| Operating profit before working capital changes | 51,715.99 | 45,852.56 | 45,852.56 | 37,994.08 |
| Decrease / (increase) in trade receivables | 79.04 | (121.98) | (121.98) | (70.22) |
| Decrease / (increase) in other financial assets and other assets | 5,189.94 | (15,294.25) | (15,294.25) | (11,618.97) |
| Increase in trade payables, other financial liabilities, provisions and other liabilities | 1,180.77 | 25,616.12 | 25,616.12 | 14,317.64 |
| Cash generated from operating activities | 58,165.74 | 56,052.45 | 56,052.45 | 40,622.53 |
| Income tax paid (net of refund) | (15,701.32) | (13,092.88) | (13,092.88) | (10,607.58) |
| Net cash generated from operating activities | 42,464.42 | 42,959.57 | 42,959.57 | 30,014.95 |

Verbatim anchor (AR26 p.183): "Operating profit before working capital changes 51,715.99 45,852.56" / "Cash generated from operating activities 58,165.74 56,052.45" / "Net cash generated from operating activities 42,464.42 42,959.57". AR25 p.175 labels FY24 rows "(Increase) in trade receivables", "(Increase) in other financial assets and other assets", "Increased in trade payables, other financial liabilities, provisions and other liabilities".
Comment: all treasury income (interest, dividend, FVTPL gains, amortised-cost gains) is deducted above the working-capital line; interest and dividend received sit in investing activities. So "Operating profit before working capital changes" excludes other income.

Working-capital lines printed: only the three above. Settlement obligations, member margins and statutory dues are NOT separately printed in the cash flow. They are inside the combined lines. Balance-sheet components [FILED]:
- AR26 p.210, Note 24 Other financial liabilities, Current (31-Mar-26, 31-Mar-25): "Deposits towards settlement guarantee fund (refer note 53) 2,342.04 2,138.30" / "Trading margin deposits (refer note 54) 17,126.35 16,419.77" / "Settlement obligation payable 75,313.88 75,430.63" / "Deposit from clearing and settlement bankers 1,800.00 1,800.00" / "Total 97,468.90 96,744.93".
- AR25 p.201, Note 24 (31-Mar-25, 31-Mar-24): "Trading margin deposits (refer note 52) 16,419.77 11,248.03" / "Settlement obligation payable 75,430.63 56,008.82" / "Total 96,744.93 71,708.68".
- AR26 p.210, Note 25 Other liabilities, Current: "Statutory dues payables 1,254.82 1,024.14" / "Unamortised subscription and admission fee income [refer note 25(a) below] 1,184.67 1,176.41" / "Total 2,644.54 2,313.14". AR25 p.202: "Statutory dues payables 1,024.14 868.46".
- AR26 p.204, Note 15 Other financial assets, Current: "Settlement Obligation receivables 14,641.56 21,792.15". AR25 p.196: "Settlement Obligation receivables 21,792.15 8,548.26".
- AR25 p.62 MD&A: "The increase is primarily on account of Settlement obligation payable from ` 56,008.82 lakh to ` 75,430.63 lakh mainly due to non-clearing days (banking holiday) on March 30 and March 31, 2025 and increase in trading margin deposit from ` 11,248.03 lakh to ` 16,419.77 lakh". Comment: management ties the FY25 year-end payable build to a bank-holiday timing effect. That makes FY25 working capital calendar-sensitive.
- AR26 p.230, Note 54: "The Cash Margin Money forming part of trading margin deposits is `17,126.35 (previous year `16,419.77)" plus non-cash collateral "`3,935.00 (previous year `2,230.00) which does not form part of the Balance Sheet."
- AR26 p.230, Note 53: "as per CERC order dated 9 October 2018, the Company has to share 70% of the return earned on 'initial security deposits' with the Members."

### Consolidated [FILED]

Sources: FY26 and FY25, AR26 p.244. FY24, AR25 p.234.

| Row as printed | FY26 (AR26 p.244) | FY25 (AR26 p.244) | FY25 (AR25 p.234) | FY24 (AR25 p.234) |
|---|---|---|---|---|
| Profit before tax | 64,556.32 | 56,453.60 | 56,453.60 | 46,614.33 |
| Share in profit of associate (net of tax) | (1,979.53) | (1,463.15) | (1,463.15) | (1,089.79) |
| Intangible assets under development write off | - | 117.87 | 117.87 | - |
| Operating profit before working capital changes | 52,330.40 | 45,937.21 | 45,937.21 | 37,804.74 |
| Decrease / (increase) in trade receivables | 64.50 | (182.94) | (182.94) | (70.22) |
| Decrease / (increase) in other financial assets and other assets | 5,481.68 | (15,558.24) | (15,558.24) | (11,650.24) |
| Increase in trade payables, other financial liabilities, provisions and other liabilities | 1,198.59 | 25,651.48 | 25,651.48 | 14,369.35 |
| Cash generated from operating activities | 59,075.17 | 55,847.51 | 55,847.51 | 40,453.63 |
| Income tax paid (net of refund) | (15,797.92) | (13,122.39) | (13,122.39) | (10,607.59) |
| Net cash generated from operating activities | 43,277.25 | 42,725.12 | 42,725.12 | 29,846.04 |

Verbatim anchor (AR26 p.244): "Operating profit before working capital changes 52,330.40 45,937.21" / "Net cash generated from operating activities 43,277.25 42,725.12".

Quarterly or Q1FY27 cash flow: NOT DISCLOSED. Indian listed companies file cash flow half-yearly; the H1FY27 cash flow would be in the Q2FY27 results filing (Oct/Nov-2026), not yet in corpus. Q1FY27 filing (R-Q1) prints no cash flow.

---

## D2. Capex

### Cash flow capex line [FILED]

| Row as printed | FY26 | FY25 | FY24 | Source |
|---|---|---|---|---|
| Purchase of Property, plant and equipment and other intangible assets (standalone) | (1,476.77) | (782.60) | (1,395.98) | AR26 p.183 (FY26, FY25); AR25 p.175 (FY24) |
| Proceeds from sale of PP&E and other intangible assets (standalone) | 26.79 | 16.59 | 71.38 | same |
| Purchase of Property, plant and equipment and other intangible assets (consolidated) | (1,477.82) | (785.10) | (1,529.91) | AR26 p.244; AR25 p.234 |
| Proceeds from sale (consolidated) | 29.63 | 16.59 | 71.37 | same |

R-Q4 p.8 prints standalone FY26 as "(1,476,77)" (OCR comma).
Comment: the cash flow line combines PP&E and intangibles; CWIP / IAUD spend is not a separate cash flow line.

### Asset-note additions, standalone [FILED]

AR26 p.194, Note 4 PP&E and CWIP: FY26 "Additions/ Adjustments during the year ... 1,313.82 1,245.61" (total PP&E, CWIP); FY25 "... 352.69 336.14". Computer hardware additions FY26 "1,245.61", FY25 "247.84".
AR25 p.186, Note 4: FY24 "Additions/ Adjustments during the year ... 642.28 206.68" (total PP&E, CWIP).
AR26 p.195, Note 5 Intangibles and IAUD: FY26 "Additions during the year 987.53 - 987.53 1,104.48" (software, licence, total, IAUD); FY25 "Additions during the year 383.69 - 383.69 497.85".
AR25 p.187, Note 5: FY24 "Additions during the year 529.93 - 529.93 426.84".
AR26 p.195: "Software license with carrying amount of `4,712.87 (31 March 2025 : `5,487.89) as remaining useful life of 6.15 years".
IAUD closing: AR26 p.195 "As at 31 March 2026 ... 530.08"; FY25 "413.12".

IAUD projects overdue to original plan, AR26 p.196 (31-Mar-26): "Real Term Market (RTM) Re-architecture 306.79", "Temporary General Network Access (TGNA) 84.43", "LDC Back Office Automation 46.66", "Hot Standby Project 69.72", suspended "Automated Value RMS 7.40", "Unified Banking 15.08", total "530.08". AR26 p.196: "There are no projects as on 31 March 2026 and 31 March 2025 where the cost has exceeded its original plan."

Capital commitments: AR26 p.217, Note 38: "Estimated amount of contracts remaining to be executed on capital account and not provided for Nil (31 March 2025: `562.39)". AR25 p.208: "` 562.39 (31 March 2024: ` 26.50)".

### Disclosed capex plans

- Coupling-related systems [MGMT], CC-Apr p.15: question "What would be the rough estimate cost" of software re-engineering to forward bids to Grid-India; "Satyanarayan Goel: We have our own software team. And I'm sure our team will be able to do all these things." / "Nikunj Bajaj: So it will not have an additional cost, is it?" / "Satyanarayan Goel: No additional costs." Comment: management guides zero incremental coupling cost; no rupee figure given.
- Hot Standby / DC-DR [FILED], AR26 p.20: "During FY'26, IEX made significant progress towards implementing a Hot Standby architecture, with the aim of completing its implementation during the new financial year, to support High Availability, Fault Tolerance, and rapid scalability for the Risk Management System and Real-Time Bidding System". [MGMT] CC-Jul p.25: "we have also built a hot standby solution for the Real-Time market". Rupee budget: NOT DISCLOSED beyond the IAUD balance "Hot Standby Project 69.72" (AR26 p.196).
- Data centre capex: NOT DISCLOSED. "Data centres" appear in AR26 and concalls only as a power-demand driver (e.g. AR26 p.35), not as IEX capex. A plan would be in the Board's Report or MD&A technology section.
- New products / subsidiaries [FILED], AR26 p.74: "Subsequent to the close of FY'26, the Company incorporated a wholly owned subsidiary, Indian Coal Exchange Limited, on June 1, 2026. ... Indian Coal Exchange Limited has been incorporated with an authorized and paid up share capital of `100 crore, comprising 10 crore equity shares of face value `10 each." Comment: this is an equity commitment to a subsidiary, not PP&E capex; a standalone capex budget for the coal exchange is NOT DISCLOSED (would be in ICEL business plan / Board's Report).
- Forward capex guidance in rupees for FY27: NOT DISCLOSED in any of the four transcripts or two presentations.

---

## D3. Dividends, buybacks, capital allocation

### Cash flow dividend line [FILED]

| Row as printed | FY26 | FY25 | FY24 | Source |
|---|---|---|---|---|
| Dividend paid (net of dividend received [net of tax] by ESOP trust), standalone | (26,699.87) | (26,699.78) | (17,798.04) | AR26 p.184; AR25 p.176 |
| Same line, consolidated | (26,699.87) | (26,699.78) | (17,798.04) | AR26 p.245; AR25 p.235 |

Gross dividend declared and paid [FILED], AR26 p.207 Note 18(e): "Interim Dividend for the year ended 31 March 2026 of `1.5 per share (31 March 2025 is `1.5 per share) 13,375.39 13,375.39" / "Final Dividend for the year ended 31 March 2025 of `1.5 per share (31 March 2024 is `1.5 per share) 13,375.39 13,375.40" / "Total 26,750.78 26,750.79".
AR25 p.199 Note 18(e): "Interim Dividend for the year ended 31 March 2025 of ` 1.5 per share (31 March 2024 is ` 1 per share) 13,375.39 8,916.93" / "Final Dividend for the year ended 31 March 2024 of ` 1.5 per share (31 March 2023 is ` 1 per share) 13,375.40 8,916.93" / "Total 26,750.79 17,833.86".
Comment: the cash flow line is net of ESOP-trust receipts, so it is slightly below the Note 18(e) gross figure. Different basis, not a conflict.

Per-share declared for the year [FILED]:
- FY26: interim Rs 1.5 and final Rs 2.0. AR26 p.69: "The total dividend for the financial year ended March 31, 2026, amounts to `3.5/- per equity share ... would involve a total cash outflow of `31,209.25 Lakhs, resulting in a dividend payout of approx. 66% of the standalone profit after tax of the Company exceeding the defined dividend range in the Company's Dividend Distribution Policy." Proposed final: AR26 p.207 Note 18(f) "Final Dividend for the year ended 31 March 2026 of `2 per share ... 17,833.85".
- FY25: AR25 p.66: "The total dividend for the financial year ended March 31, 2025, amounts to ` 3/- per equity share ... total cash outflow of ` 26,750.79 Lakhs, resulting in a dividend payout of approximately 65% of the standalone PAT of the Company exceeding the defined dividend range in the Company's Dividend Distribution Policy."
- FY24: interim "` 1 per share" and final "` 1.5 per share" (AR25 p.199 Note 18(e) and p.197 Note 17). A FY24 total-per-share sentence is NOT printed in the corpus; it would be in the FY24 AR Board's Report (not collected).

Dividend Distribution Policy [FILED], AR26 p.69: "Pursuant to Regulation 43A of SEBI Listing Regulations, your Company has a well-defined Dividend Distribution Policy that balances the dual objective of rewarding shareholders through dividends whilst also ensuring the availability of sufficient funds for the growth of the Company. The policy is available on the website of the Company". The policy text and its "defined dividend range": NOT DISCLOSED in corpus; pointer is the policy PDF on the IEX website (doc.iexindia.com Dividend-Distribution-Policy), not collected. Comment: both AR25 and AR26 state payout exceeded the policy range, without printing the range.

Payout history [MGMT], P-AM p.39: "187 223 268 312" and "64 65 65 66", labels "Dividend Payout (INR Cr)" and "Payout % to PAT", columns "FY23 FY24 FY25 FY26".
CC-Jul p.27 [MGMT] (CMD): "As a policy, we are paying almost around more than 50%, 65% as dividend over the last many years."

Buybacks [FILED]: none in FY24, FY25, FY26. AR26 p.206 describes the last buyback: "The buyback of equity shares through the stock exchange commenced on 11 January 2023 and was completed on 16 March 2023. During this buyback period, the Company purchased and extinguished a total of 6,976,798 equity shares ... at a weighted average buyback price of `140.45 per equity share ... The buyback resulted in a cash outflow of `9,798.96". AR26 p.96 lists the SEBI Buyback Regulations as "(Not Applicable)" for FY26.
Buyback intent [MGMT]:
- CC-Apr p.12 (CFO): "So again, buyback has become one of the good options for distributing money to the shareholders. We are definitely considering it. And we are also waiting for the draft note with SEBI had come out with regards the open market route".
- CC-Jul p.29-30 (CMD): "but buyback, yes definitely, we will consider it in future because now SEBI also has revised its rules for doing the buyback through the market."
Comment: intent stated twice; no size, price or Board approval disclosed in corpus.

Capital allocation statement [FILED], AR26 p.224 Note 43: "The Company's objectives when managing capital are to safeguard their ability to continue as a going concern so that they can continue to provide returns to shareholders and benefits for other stakeholders, and maintain an optimal capital structure to reduce the cost of capital. The Company does not have any debt outstanding as on 31 March 2026 and 31 March 2025."
AR26 p.65 MD&A: "During FY'26 `26,750.78 (Final dividend for FY'25 `13,375.39 lakh; Interim dividend for FY'26 `13,375.39 lakh) ... was utilised from free reserves of the Company towards payment of dividend on Equity shares".

Other large investing outflow for context [FILED]: "Purchase of investments (net) (29,845.84) (21,039.51)" standalone FY26, FY25 (AR26 p.183); FY24 "(3,050.22)" (AR25 p.175).

---

## CLOSING

Documents quoted, with dates:
- annual-report__Annual_Report_2026.txt, FY26 AR, filed BSE 14-Aug-2026; financial statements signed 23 April 2026 (AR26 p.184).
- annual-report__Annual_Report_2025.txt, FY25 AR (FY24 comparatives).
- results__FY26_Q4_Audited_Results_2026-04-23.txt, audited Q4FY26/FY26 results, 23-Apr-2026.
- results__Q1FY27_Results_Unaudited_2026-07-23.txt, Q1FY27 unaudited results, 23-Jul-2026.
- concalls__Concall_Apr_2026_Transcript.txt, Q4FY26 call, cover letter dated 30-Apr-2026.
- concalls__Concall_Jul_2026_Transcript.txt, Q1FY27 call / analyst meet, cover letter dated 31-Jul-2026.
- presentation__Investor_Presentation_Q4FY26_2026-04-23.txt, 23-Apr-2026.
- presentation__Investor_Presentation_Analyst_Meet_2026-07-24.txt, 24-Jul-2026.
- Searched, nothing quotable for Parts C/D: concalls__Concall_Feb_2026_Transcript.txt, other__Concall_Nov_2025_Q2FY26_Transcript.txt, results__Q1FY27_Press_Release_2026-07-23.txt, announcements__FY26_Q4_Press_Release_2026-04-23.txt (dividend headline only).

NOT DISCLOSED, with pointer:
1. Q2FY26 other income, standalone and consolidated: Q2FY26 results filing (Oct/Nov-2025), not collected.
2. Q2FY26 share of associate: same Q2FY26 consolidated results filing, not collected.
3. Quarterly split of other income by component: not printed in any quarterly results filing; only full-year notes carry it.
4. MF-specific share of FVTPL gains; explicit realised/unrealised labels: AR26 Note 29 / Note 41, not printed.
5. FY26 treasury yield: AR26 MD&A p.64 gives average investment only (AR25 p.61 gave FY25 yield 8.53%).
6. Separate ETR on other income; separate capital-gains rate line: AR26 Note 34 / Note 33 bundle it into "Others".
7. Investment policy content (instruments, rating floor, tenor, concentration, equity limit): Board-approved Investment Policy, not in AR or corpus.
8. Quarterly and Q1FY27 cash flow: H1FY27 cash flow in Q2FY27 results filing (Oct/Nov-2026), not yet in corpus.
9. Separate cash flow lines for settlement obligations, margins, statutory dues: not printed; balances only in AR26 Notes 15, 24, 25.
10. Rupee capex plan for coupling, hot standby, data centre, coal exchange PP&E: not in AR26, AR25, the four transcripts or two presentations. Coupling guided "No additional costs" (CC-Apr p.15).
11. Dividend Distribution Policy text and "defined dividend range": policy PDF on IEX website, not collected.
12. FY24 total dividend per share sentence: FY24 AR Board's Report, not collected.
13. Buyback size, price or approval: none disclosed; intent only (CC-Apr p.12, CC-Jul p.29-30).

CONFLICTS flagged: FY25 average investment "1,362 crores" (AR25 p.61) vs "1,363 cores" (AR26 p.64). OCR-only print differences (for example "2,211,41" vs "2,211.41") are noted inline, not treated as conflicts.

---

## ORCHESTRATOR ADDENDUM (closes A5 against a corpus file outside the Part A/B reader's list)

A5. The request places the one-time treasury item in the Q3FY26 call. The corpus places it in the Q4FY26 call (CONFLICT with the request, as the reader flagged).

concalls__Concall_Apr_2026_Transcript.txt, p.10 (call held 24-Apr-2026), Vineet Harlalka, CFO, answering a question on the Q4 fall in other income: [MGMT]
> "if you look at the December quarter number, it was a significant increase over the treasury income because there was a one-time gain we got because the interest rates were there and the market was improving. And as you all know, because of the Iran conflict and rupee situation, there was a significant correction in the market during this month of March. So a bit of mark-to-market impacts were there. And that was reflecting in the numbers. And the previous quarter, there was onetime gains."

Comment: two items, a Q3FY26 one-time gain and a Q4FY26 MTM hit. Neither amount nor instrument is given.

presentation__Investor_Presentation_Q4FY26_2026-04-23.txt, p.26 (deck dated 23-Apr-2026), "Breakup of standalone revenues (%)": [MGMT]
> "Other Income 18.1% 20.7% 11.4% 18.3%" (columns Q4FY25, Q3FY26, Q4FY26, FY26)

Comment: the only corpus figure that shows the swing. It is a share of standalone total revenue, not an amount.

Amount, instrument and accounting line: NOT DISCLOSED. Pointer: the Q3FY26 results filing (Jan/Feb-2026, not collected) and the Q3FY26 investor presentation (not collected); in the FY26 AR the only place it could sit is standalone Note 29 (p.211), which prints full-year lines only.
