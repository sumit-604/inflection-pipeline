# Stage 12b: Verifier B, concall red flags (NO-CONCALL MODE). ANAWIL. Run 2026-11-12

## 0. Basis and method

**Mode.** The main company filed no transcript. The H1 FY27 call took place on 2026-11-09. The transcript is due within five working days (Ann 2026-11-09 p.1), so it is not in the corpus. Per the orchestrator rule, I audited the communication analysis against the results and filing sources in place of main-company transcripts.

**Order of work.** I read every main-company source first, then the 12 peer transcripts (targeted reads plus full reads of SUZ Q2FY27 and the INOX Q1FY27 opening and closing Q&A). I built and graded my independent list. Only then did I open B05 and B06. I grepped the prospectus. I did not read it whole.

**Main-company sources read.** H1 results outcome (all 8 pages); all 17 announcements; H1 FY27 deck (all 30 pages); listing deck (all 22 pages); CRISIL rationale (all 8 pages); prospectus by grep (Kutch, order book, OFS, unsecured loans, related parties, contingent liabilities, litigation, post-balance-sheet developments, LOI); one grep of the audited FY26 statements (OCR; no FY26 cash-flow line found there).

**Anchor key.** Page numbers are the `[page N]` markers in the .txt files.
- Pros p.N = prospectus/Prospectus_2026-08-06.txt (INR lakh). List p.N = presentation/Investor_Presentation_Listing_2026-08-10.txt. Pres p.N = presentation/Investor_Presentation_H1FY27_2026-11-08.txt (INR Cr).
- H1 p.N = results/H1FY27_Results_Outcome_of_Board_Meeting_2026-11-06.txt (INR lakh). PR(11-06) p.N = announcements/2026-11-06_ANAWIL_PRESS_RELEASE_FINAL.txt. PR(09-10) p.N = announcements/2026-09-10_NSE_Press_release_signed.txt. Order(09-10) p.N = announcements/2026-09-10_NSE_Order_signed.txt. Ann(date) p.N = the announcement of that date. MA p.N = the CARE monitoring agency report inside announcements/2026-11-07_NSE_Intimation.txt. CRISIL p.N = rating/CRISIL_Rating_Rationale_2026-08-19.txt.
- Peers: INOX Q2FY26/Q3FY26/Q4FY26/Q1FY27 = INOXWIND Nov_2025/Feb_2026/Jun_2026/Aug_2026. SUZ Q3FY26/Q4FY26/Q1FY27/Q2FY27 = SUZLON Feb_2026/Jun_2026/Aug_2026/Nov_2026. KPG H1FY25/H2FY25/H1FY26/H2FY26 = 544150 Dec_2024/May_2025/Nov_2025/May_2026.
- "Derived" means my arithmetic on anchored numbers. "[INFERENCE]" marks a reading the documents do not state.

---

## 1. Independent red-flag list (built before reading B05 and B06)

### 1A Main company, material (MAJOR)

| # | Sev | Red flag | Anchors |
|---|---|---|---|
| R1 | MAJOR | **Kutch plant status contradicts itself across filings.** The prospectus says Kutch "commenced commercial operations only in March 2026" and "manufactured and supplied 16 towers from the facility during the year, generating revenue of approximately ₹877.74 lakhs" (Pros p.232). That is the plant's full monthly nameplate (16 a month, List p.12) in its first month. The listing deck shows 4,822.20 MT produced at Kutch in March 2026 (List p.9). On 2026-09-10 the CMD says "With the addition of our Kutch manufacturing facility, we have expanded" (PR(09-10) p.2). On 2026-10-05: "client approval and certification processes currently ongoing" (Ann 2026-10-05 p.3). On 2026-11-06: "Capacity expansion at Kutch, Gujarat, is nearing completion, with trial runs underway" (PR(11-06) p.3; Pres p.6). The same H1 deck still says "Operations commenced in March 2026" and counts 192 towers in the 612 installed (Pres p.18). Gujarat revenue was ₹8.78 Cr in FY26 (Pres p.23), which ties to the prospectus Kutch figure of ₹877.74 lakh, so the state split is the plant split. Gujarat revenue then fell to ₹3.23 Cr for all of H1 FY27 (Pres p.23). CWIP rose from 584.80 to 3,069.27 lakh (H1 p.7). Two readings: (a) a second Kutch phase is under construction and phase 1 runs but awaits customer approval for new orders; (b) phase 1 never stabilised and the March 2026 output was a one-month spike in the IPO year. Separating observation: plant-wise tower output for H2 FY27, or a management statement on what the "expansion" adds beyond the 192 towers already called installed. | Pros p.232; List p.9, p.12; PR(09-10) p.2; Ann 2026-10-05 p.3; PR(11-06) p.3; Pres p.6, p.18, p.23; H1 p.7 |
| R2 | MAJOR | **Management statement on IPO proceeds contradicts the monitoring agency.** CARE: "Deviation from the objects: Yes" next to "Range of Deviation: Not Applicable" (MA p.3). "Whether all utilization is as per the disclosures in the Offer Document? No" (MA p.4). Of the ₹115 Cr debt object, ₹2 Cr went to "repayment of working capital borrowings" (MA p.6). GCP machinery money was routed through the cash-credit account, "resulting in comingling of funds", and CARE "relied on management declarations and CA certificate" (MA p.6). ₹0.04 Cr "was with the selling shareholder due to excess amount transferred", returned on 2026-11-04 (MA p.3). The selling shareholder is the CMD (Pros p.6). The results note filed the same day says the money "ha[s] been utilised by the company for the purposes for which they were raised" (H1 p.5-6, note 10) and its table does not mention the amount held by the selling shareholder. Size is small (₹0.89 Cr commingled, ₹0.04 Cr excess). The signal is governance, not money. | MA p.3, p.4, p.6; H1 p.5-6; Pros p.6 |
| R3 | MAJOR | **FY27 guidance outruns capacity and the order book.** Guidance is ₹450 to 500 Cr revenue and ₹55 to 60 Cr PAT (PR(11-06) p.2-3; Pres p.7). H1 is ₹153.97 Cr revenue and ₹14.39 Cr PAT (H1 p.4). H2 then needs ₹296 to 346 Cr (derived), 2.9x to 3.4x H2 FY26 revenue of ₹101.90 Cr (H1 p.4). That is 75% to 87% of the ₹395.6 Cr confirmed book in five months (derived), while the deck says the book executes "by Q1FY28" (Pres p.21). Koppal's half-year nameplate is 210 towers (35 a month, Pres p.18); the record half is 148 towers (210 less 62, Pres p.18). | PR(11-06) p.2-3; Pres p.7, p.18, p.21; H1 p.4 |
| R4 | MAJOR | **Two FY26 cash-flow numbers in one deck; restated and audited FY26 differ.** Restated FY26 CFO is 1,843.94 lakh (List p.20). Audited FY26 CFO is 1,246.70 lakh (H1 p.8), 32% lower. Tax paid is 406.85 lakh restated (derived: 2,250.79 less 1,843.94, List p.20) against 851.19 lakh audited (H1 p.8). The H1 deck charts FY26 CFO as "18" (Pres p.25) and tabulates it as "12.5" (Pres p.28). PAT is 3,662.83 lakh restated (List p.19) against 3,595.25 lakh audited (H1 p.4). The audited statements were approved on 2026-06-13 and the restated set on 2026-06-19 (Pros p.237). No filing explains the cash gap. | List p.19, p.20; H1 p.4, p.8; Pres p.25, p.28; Pros p.237 |
| R5 | MAJOR | **Funding gap one quarter after a ₹142.69 Cr IPO.** H1 capex is 5,339.49 lakh against CFO of 2,828.40 lakh (H1 p.8). Cash is 19.61 lakh at 30 Sep 2026 (H1 p.7). The CMD lent ₹21.68 Cr at 6% (Pres p.8). His loan balance was 414.75 lakh at Mar-26 (Pros p.51). In August he received ₹3,512.16 lakh as the OFS selling shareholder (Pros p.2, p.6). No capex plan exists in any document. The IPO funded no capex (MA p.5). CRISIL projected gearing below 0.05x at Mar-27 (CRISIL p.1); Sep-26 gearing is 0.15x (derived: (27.0 + 6.6) / 226.3, Pres p.27). A ₹111.94 Cr proposed working-capital facility is rated (CRISIL p.3-4). | H1 p.7, p.8; Pres p.8, p.27; Pros p.2, p.6, p.51; MA p.5; CRISIL p.1, p.3-4 |
| R6 | MAJOR | **Prospectus-certified completion dates are slipping, and the communication does not say so.** The March 2026 book lists completion dates per line, certified by a peer-review auditor (Pros p.114). Matched by product description to the 31 Oct 2026 book (Pres p.21) [INFERENCE: customer letters were relabelled]: of 225 towers due by 31-12-2026 (₹185.14 Cr, derived), at least 182 (81%) were still open at 31-10-2026 (₹152.1 Cr). If the "SANY WTG 06 SCT" 16-tower line is part of the old Sany order, the figure is 198 (88%). The single Envision tower due 30-09-2026 is still open. Koppal can make about 70 towers in November and December (35 a month, Pres p.18). H1 execution went mainly to the line due 31-03-2027: "Wind Turbine Generator Components-Towers" fell from 34 towers and 10,760.44 lakh to 3 towers and ₹10.6 Cr, about ₹97 Cr executed (derived). The deck restates the whole book as "expected to execute the order book by Q1FY28" (Pres p.21). | Pros p.114; Pres p.18, p.21 |

### 1B Peers, material (MAJOR)

| # | Sev | Red flag | Anchors |
|---|---|---|---|
| R7 | MAJOR | **Peer OEMs report site-readiness slippage and repeated H2 guidance misses; Anawil's guidance carries no site risk.** INOX: "Many of the sites are not ready to the extent that it was planned" (INOX Q3FY26 p.6). INOX moved to revenue guidance because of "delay of sites" (INOX Q3FY26 p.16). An analyst insisted: "every con call, we have missed the guidance by some margin. And every con call, we have been 100% confident" (Rishabh Gupta, INOX Q1FY27 p.16). Management replied: "Yes, there were sudden slippages" (INOX Q1FY27 p.17). SUZ: about 3,900 MW delivered and pending installation, about 1,300 MW erected (Ajay Kapur, SUZ Q2FY27 p.16). Anawil's papers cite only monsoon seasonality (Pres p.22; Ann 2026-10-05 p.3). | INOX Q3FY26 p.6, p.16; INOX Q1FY27 p.16, p.17; SUZ Q2FY27 p.16; Pres p.22 |

### 1C Main company and peers, MINOR

| # | Sev | Red flag | Anchors |
|---|---|---|---|
| R8 | MINOR | Inox is building its own blade and tower plant in South India for Karnataka, Andhra Pradesh and Tamil Nadu sites (Sanjeev Agarwal). The plant is captive, so it removes a buyer more than it competes for Sany or Envision volume [INFERENCE]. | INOX Q2FY26 p.4 |
| R9 | MINOR | KP Green lists "onshore tubular tower" as a new vertical while it runs at 30% to 34% utilisation. | KPG H2FY26 p.4, p.10 |
| R10 | MINOR | The sequential fall goes unmentioned. PAT fell from 3,370.22 lakh in H2 FY26 to 1,438.69 lakh in H1 FY27, down 57% (H1 p.4). EBITDA per tower on a P&L basis fell from 34.5 lakh (derived: 5,108.87 / 148) to 33.7 lakh (derived: 3,608.24 / 107). The press release headline is "Robust EBITDA and PAT Performance" on YoY numbers (PR(11-06) p.2). YoY is the seasonally fair basis, so this is a completeness point only. | H1 p.4; PR(11-06) p.2; Pres p.18 |
| R11 | MINOR | "EBITDA per tower" of ₹32.82 lakh is not EBITDA. It is the cash-flow line "Operating Profit before Working Capital Changes", 3,511.65 lakh (H1 p.8), divided by 107. The FY26 base, 6,001.21 / 210 = 28.58 lakh (H1 p.8), reproduces the stated +14.8%. The company's own reported EBITDA is ₹36.08 Cr (PR(11-06) p.2), or 33.7 lakh a tower. | H1 p.8; PR(11-06) p.2-3 |
| R12 | MINOR | The order book mixes GST bases. The Oct 29 order sits at the GST-inclusive ₹58.3 Cr. The Sep 10 order sits ex-GST at ₹134.0 Cr. GST on wind components is 5% (INOX Q2FY26 p.4; 140.68 / 133.98, Order(09-10) p.1), so the book is overstated by about ₹2.78 Cr (derived). | Ann 2026-10-29 p.1-2; Pres p.21; Order(09-10) p.1 |
| R13 | MINOR | The "largest-ever order" of 2026-09-10 is the conversion of a Q1 FY27 LOI for 38 towers at ₹120 Cr. That LOI was marketed in the listing deck four days after the prospectus (List p.2, p.8) and in CRISIL (p.1). It is absent from the prospectus list of post-balance-sheet material events (Pros p.236-237). A prospectus grep for "LOI", "letter of intent" and "38 towers" returns no match. | PR(09-10) p.2; List p.2, p.8; CRISIL p.1; Pros p.236-237 |
| R14 | MINOR | The CS and Compliance Officer resigned. The letter is dated 01-10-2026 and gives "personal reasons" (Ann 2026-10-31 letter p.1). The filing body says "pre-occupation" (Ann 2026-10-31 p.1). Annexure-I says "To pursue career opportunities outside the organization" (Ann 2026-10-31 p.3). That is three reasons for one exit. The disclosure came 30 days after the letter date; the filing treats the board's noting on 2026-10-31 as the event. The revised filing (Ann 2026-11-03) adds only meeting times. The letter came 52 days after listing. | Ann 2026-10-31 letter p.1; Ann 2026-10-31 p.1, p.3; Ann 2026-11-03 p.1-3 |
| R15 | MINOR | The investor-meet intimations promise "no price sensitive information or forward-looking statement will be disclosed or discussed" (Ann 2026-09-21 p.1; Ann 2026-09-24 p.1). The conference outcome note then publishes forward-looking statements: "overall EBITDA margin is expected to moderate; however, EBITDA per tower is expected to increase" (Ann 2026-10-05 p.2). | Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2 |
| R16 | MINOR | The H1 deck has drafting defects. A "Net Profitability • Text" placeholder is left in (Pres p.7). The same page says 108 towers and +74%, against 107 and +72.6% (Pres p.7). FY26 ROE is 57% (Pres p.25) against RONW of 40.92% in the listing deck (List p.15), with no basis label. | Pres p.7, p.25; List p.15 |
| R17 | MINOR | CRISIL expects operating margin "around 40% over the medium term" (CRISIL p.1). That rationale is nine days after management's own deck put Model 3 at 14% to 16% and said margin % would fall (List p.16). H1 FY27 printed 23.4%. | CRISIL p.1; List p.16; PR(11-06) p.2 |
| R18 | MINOR | The two orders that make 48.6% of the book (₹134.0 Cr + ₹58.3 Cr of ₹395.6 Cr, derived) were filed with the counterparty withheld: "Domestic Client" and "CONFIDENTIAL". | Order(09-10) p.2; Ann 2026-10-29 p.2; Pres p.21 |
| R19 | MINOR | The H1 FY27 call took place on 2026-11-09. The audio is public and the transcript is due within five working days. The only management Q&A that could test R1, R3 and R6 exists but is outside the corpus. | Ann 2026-11-09 p.1; Ann 2026-11-04 p.1-2 |
| R20 | MINOR | Short-term loans and advances are ₹54.31 Cr (H1 p.7), up from ₹14.36 Cr at Mar-25 (List p.17). That is 17% of total assets, and no management document explains it. | H1 p.7; List p.17 |
| R21 | MINOR | Firm inflow outside the two announced orders is about zero for seven months. In towers: 379 (Pros p.114) + 38 (Order(09-10) p.2) + 10 (Ann 2026-10-29 p.2) less 107 (PR(11-06) p.2) = 320, which equals the Oct book (Pres p.21). In value: 359.82 + 133.98 + 58.32 less 153.97 = ₹398.15 Cr against ₹395.6 Cr (derived). The 44-tower LOIs (₹44.1 Cr) sit outside the book. [INFERENCE: the new small lines G and H, 28 towers, are re-scoped old lines; the tower arithmetic only closes on that reading.] | Pros p.114; Order(09-10) p.2; Ann 2026-10-29 p.2; PR(11-06) p.2; Pres p.21 |
| R22 | MINOR | Suzlon cut its FY27 EBITDA guidance from about 17% to 15% plus 1% on customer and scope mix and commodity (Raj Shah and Ajay Kapur). This is a peer margin walkback on the same mix logic Anawil uses. | SUZ Q2FY27 p.9-10 |
| R23 | MINOR | Peers say steel is "largely a pass-through other than maybe some PSU contracts" (SUZ Q4FY26 p.12; SUZ Q2FY27 p.7). Anawil never states a pass-through clause, although Model 3 (51% of the book, PR(11-06) p.3) puts steel on its books. | SUZ Q4FY26 p.12; SUZ Q2FY27 p.7; PR(11-06) p.3 |
| R24 | MINOR | Adani and JSW have entered wind with captive platforms (Ajay Kapur). Captive turbine makers may self-supply towers [INFERENCE]. | SUZ Q2FY27 p.7-8 |
| R25 | MINOR | The Oct book line "4XM, 12, ₹0.6 Cr" for Customer H (Pres p.21) matches Inox's 4X platform name (INOX Q1FY27 p.4). [INFERENCE] Inox may be a small existing customer, and it is building its own tower plant (R8). | Pres p.21; INOX Q1FY27 p.4; INOX Q2FY26 p.4 |

**Tally.** 25 items: 0 CRITICAL, 7 MAJOR, 18 MINOR. No repeated evasion over two quarters exists here: the Kutch date is missing from two communications (Oct and Nov), but no analyst asked twice on record.

---

## 2. Comparison with the pipeline (B05, B06)

| # | Sev | Status | Where the pipeline has it, and what is missing |
|---|---|---|---|
| R1 | MAJOR | PARTIALLY CAUGHT | B05 1C "WEAKENING", 2A row 4 "Partial", 2D row 1, timeline_slippages. B05 does not use Pros p.232 (16 towers, ₹877.74 lakh) or List p.9 (4,822.20 MT in March). It reads the March output as trials ("Kutch has run trials since March 2026", B05 peer question 5). So it frames a slow ramp, not documents that contradict each other on FY26 Kutch output. |
| R2 | MAJOR | PARTIALLY CAUGHT | B05 2A row 1 records "Deviation: Yes" but scores ✅ Delivered on size. It says the machinery money was "mixed with the debt repayment"; it was GCP money commingled in the CC account. It does not name "all utilisation as per offer document: No", the ₹2 Cr to working-capital borrowings, the ₹0.04 Cr excess transfer to the promoter selling shareholder, or the clash with results note 10. |
| R3 | MAJOR | CAUGHT | B05 HIGH flag FLAG-GUIDANCE-TOWERS and 2A guidance arithmetic. |
| R4 | MAJOR | CAUGHT | B05 load-bearing fact 3 and FLAG-CONSISTENCY (CFO ₹12.5 Cr and ₹18 Cr in one deck, carried from B03). |
| R5 | MAJOR | CAUGHT | B05 FLAG-PROMOTER-FUNDING and 1C promoter-loan row. The link to the CMD's ₹35.12 Cr OFS receipt is not drawn (nuance only). |
| R6 | MAJOR | PARTIALLY CAUGHT | B05 2A row 5 and timeline_slippages note the window moved to Q1 FY28. B05 says old and new orders "cannot be separated" and tower-level completion is NOT FOUND. The product descriptions match line by line, and they show at least 81% of the Dec-2026-due towers still open. |
| R7 | MAJOR | CAUGHT | B06 FLAG-OEM-H2-GUIDANCE-MISS-PATTERN, FLAG-SITE-READINESS-RISK-NOT-IN-ANAWIL-DECK, 2A. The INOX Q1FY27 analyst insistence is not quoted (nuance only). |
| R8 | MINOR | CAUGHT | B06 FLAG-INOX-IN-HOUSE-TOWER-SOUTH. |
| R9 | MINOR | CAUGHT | B06 FLAG-KP-TUBULAR-ENTRY. |
| R10 | MINOR | PARTIALLY CAUGHT | B05 2A and 2D hold the H2 FY26 numbers (PAT ₹33.70 Cr; 34.5 lakh a tower) but never compare the headline KPI sequentially. |
| R11 | MINOR | PARTIALLY CAUGHT | B05 found that ₹32.82 lakh does not tie to EBITDA but put the cause on the tower count ("implies 109.9 towers"). The count is right; the profit line is mislabelled. See finding F4. |
| R12 | MINOR | CAUGHT | B05 4D LOW (about ₹2.78 Cr, 0.7%). |
| R13 | MINOR | PARTIALLY CAUGHT | B05 has the "largest-ever" headline as over-promotion and the LOI as delivered. It does not note that the LOI is missing from the prospectus. |
| R14 | MINOR | MISSED | Not in B05 or B06. |
| R15 | MINOR | MISSED | Not in B05 or B06. |
| R16 | MINOR | PARTIALLY CAUGHT | B05 has the 107 versus 108 towers. It does not have the placeholder or the ROE basis. |
| R17 | MINOR | CAUGHT | B05 1B note and 4D LOW. |
| R18 | MINOR | PARTIALLY CAUGHT | B05 has the concentration (Customer A 36.6%). It does not note the withheld counterparty names. |
| R19 | MINOR | CAUGHT | B05 input_gaps and gaps section. |
| R20 | MINOR | CAUGHT | B05 2B and 2D (advances to unnamed vendors, via B03). |
| R21 | MINOR | PARTIALLY CAUGHT | B05 2A row 5 derives an inflow of 48 towers and ₹189.73 Cr, but does not see that 48 = 38 + 10, the two announced orders. |
| R22 | MINOR | PARTIALLY CAUGHT | B06 2B has the Suzlon WTG contribution fall (26.9% to 21.2%). It does not name the guidance cut. |
| R23 | MINOR | CAUGHT | B05 2D row 3; B06 Q7. |
| R24 | MINOR | CAUGHT | B06 Q12 and risks list. |
| R25 | MINOR | MISSED | Not in B05 or B06. |

**Counts.** Caught 12. Partially caught 10. Missed 3, all MINOR. Material: 7 found; 4 caught, 3 partially caught, 0 missed.

---

## 3. Pipeline flags I did not find in my independent read

| Pipeline flag | Verdict | Basis |
|---|---|---|
| B05 MEDIUM: "no ongoing tax litigation" (Ann 2026-10-24 p.3) against a pending ₹367.25 lakh direct-tax demand | SUPPORTED | Pros p.26 lists one direct-tax case of ₹367.25 lakh. The litigation chapter describes a 143(1)(a) demand order dated 2026-07-17 for AY 2025-26, with a 115BAB rectification "currently pending" (Pros litigation chapter, B05 anchor p.240-241). Ann 2026-10-24 p.3 says "no Ongoing Tax Litigations or Disputes". No filing shows the rectification was granted before 30 Sep 2026. I read the governance filing but did not cross-check it against the prospectus. B05 is right. |
| B05 MEDIUM, part of FLAG-METRIC-REFRAME: "headline metric does not reproduce on the stated tower count" | OVERSTATED | It reproduces exactly on 107 towers on the cash-flow operating-profit line (R11). The reframing half of the flag (EBITDA per tower made the KPI on 2026-08-10, List p.16) is SUPPORTED. |
| B05 MEDIUM: FY27 guidance first issued with the H1 print known | OVERSTATED | Issuing first guidance with a results print is routine. B05's own arithmetic shows the H2 share it needs (66% to 69%) is below every past H2 share. The flag adds no signal beyond FLAG-GUIDANCE-TOWERS. |
| B05 LOW: H1 FY27 utilisation omitted; tower-market figure dropped | SUPPORTED | Pres p.18 prints utilisation % only for FY24 to FY26. The "~12,500+ future tower market" (List p.3) is absent from Pres p.10. |
| B06 FLAG-H2-RANGE-TOP | SUPPORTED | Peer H1 shares: INOX "H2 generally being 70%" (INOX Q2FY26 p.3); SUZ "about 35, 40 in H1 versus 60, 65 in H2" (SUZ Q1FY27, file line 188). Anawil's history is 70.5% to 80.2% in H2 (List p.7). |
| B06 FLAG-WC-ABOVE-PEERS | OVERSTATED | It sets CRISIL's gross current asset days (292, CRISIL p.2) against peer net cycles: INOX working capital "200-210 days" (INOX Q3FY26 p.7) and KP cash conversion of 86 days (KPG H2FY25) and about 150 days (KPG H2FY26). On a net basis Anawil's Mar-26 working capital is 6,970.57 lakh (derived from H1 p.7, Mar-26 column: inventories, receivables, short-term loans and advances, other current assets, less payables, other current liabilities, short-term provisions). That is about 178 days of FY26 revenue of 14,326.69 lakh (H1 p.4), inside the peer range. |
| B06 FLAG-TOWER-SUPPLY-UNTESTED | SUPPORTED | A coverage flag. No peer transcript discusses tubular tower prices, vendor counts or plant approval (my reads agree). |
| B06 cross-peer hypothesis (sites, not fabrication, bind; tower supply is loose) | SUPPORTED as [INFERENCE] | Labelled as inference, with a stated test and failure condition. |

No pipeline flag is NOT SUPPORTED. No flag invents a signal.

**Anchor spot checks on B06.** INOX Q2FY26 p.3 "H2 generally being 70%" (file line 86): confirmed. SUZ Q1FY27 "35, 40 in H1 versus 60, 65 in H2" (file line 188): confirmed. INOX Q3FY26 "200-210 days" (file line 268, p.7): confirmed. The Inox South India tower plant is cited as INOX Q2FY26 [page 3]. It sits on [page 4] (file lines 107-111). That is a one-page anchor error (finding F7).

---

## 4. Promise-delivery spot checks (B05 2A)

| B05 row | Earlier document holds the promise? | Later document shows the outcome? | Direction | Verdict |
|---|---|---|---|---|
| 1. IPO use: ₹115.00 Cr debt, ₹3.64 Cr GCP, ₹24.05 Cr issue cost | Yes. The offer-document costs are restated in MA p.5. | Yes. 115.00, 3.69 and 23.87 (H1 p.6; MA p.6-7). | Delivered on amount. The CARE qualitative findings are under-weighted and mis-described (R2, F2). | CONFIRMED |
| 2. LOI 38 towers, ₹120 Cr, Q1 FY27 | Yes. List p.2, p.8. | Yes. Order for 38 towers at ₹133.98 Cr ex-GST (Order(09-10) p.1-2). +11.7% is derived correctly. | Delivered | CONFIRMED |
| 3. Margin % moderates; EBITDA per tower rises | Yes. List p.16; Ann 2026-10-05 p.2. | Yes. 23.4% against 42.7% (Pres p.9). ₹32.82 lakh against ₹28.58 lakh FY26 (H1 p.8, derived). | Delivered on direction. B05's "magnitude unreconciled" caveat is resolved by R11. | CONFIRMED |
| 4. Kutch commenced March 2026, adds 16 towers a month | Yes. List p.12; Pros p.232 also says 16 towers were supplied from Kutch in FY26. | Yes. Gujarat (Kutch) revenue ₹3.23 Cr in H1 against ₹8.78 Cr in March 2026 alone (Pres p.23). Status "nearing completion, trial runs underway" (PR(11-06) p.3). | B05 says "Partial". The outcome is a regression from one month at nameplate to trial runs, and output fell. It reads MISSED or REGRESSED, not partial. | WRONG |
| 5. March book completes 30-09-2026 to 31-03-2027 | Yes. Pros p.114 gives per-line dates. | Yes. At least 182 of 225 Dec-2026-due towers still open on 31-10-2026 (Pres p.21, by description match). | Partial (slipping) is the right direction. B05's "cannot separate" is too cautious (R6). | CONFIRMED |

**Checked 5, confirmed 4, wrong 1.** Re-scored, the B05 tracker reads 3 delivered, 2 partial, 1 missed, not 3, 3 and 0.

---

## 5. Credibility grade

B05 grade: C (NO-CONCALL default; B not earned). **Concur, at the floor of C.** The delivery record still supports C: 3 delivered, 2 partial, 1 missed. Four written-disclosure defects push against C: the Kutch contradiction (R1), results note 10 against CARE (R2), the tax-litigation statement (B05 flag, supported), and the slip of prospectus-certified dates (R6). If the H1 transcript or the H2 FY27 print confirms R1 or R6, D is the grade the evidence supports.

---

## 6. Findings (consolidated)

| # | Sev | Location | Finding | Evidence |
|---|---|---|---|---|
| F1 | MAJOR | B05 2A row 4; promise_delivery row 4; peer_questions item 5 | The Kutch promise is scored "Partial". It should be MISSED or REGRESSED. B05 did not use the prospectus statement that Kutch supplied 16 towers in March 2026, or the 4,822.20 MT March output, so it missed that the filings contradict each other. | Pros p.232; List p.9; PR(11-06) p.3; Pres p.18, p.23 |
| F2 | MAJOR | B05 2A row 1; promise_delivery row 1 | The CARE deviation is scored ✅ Delivered and mis-described. Missing: "all utilisation as per offer document: No", ₹2 Cr of the debt object to working-capital borrowings, the ₹0.04 Cr excess transfer to the promoter selling shareholder, and the clash with results note 10. | MA p.3, p.4, p.6; H1 p.5-6 |
| F3 | MAJOR | B05 2A row 5; timeline_slippages | Order-book slippage is under-weighted. Line-level matching shows at least 182 of 225 towers due by 31-12-2026 still open at 31-10-2026, and one tower past its 30-09-2026 date. "Cannot separate old from new" does not hold. | Pros p.114; Pres p.21 |
| F4 | MINOR | B05 2A reproduction check; FLAG-METRIC-REFRAME; input_gaps | Overstated. ₹32.82 lakh = 3,511.65 lakh (cash-flow operating profit before working-capital changes) / 107. The FY26 base 6,001.21 / 210 = 28.58 lakh gives +14.8%. Withdraw "implies 109.9 towers" and "tower count behind ₹32.82 lakh: NOT FOUND". The real defect is the label: the company calls a cash-flow subtotal "EBITDA", ₹0.97 Cr below its own ₹36.08 Cr. | H1 p.8; PR(11-06) p.2 |
| F5 | MINOR | B05 FLAG-FIRST-GUIDANCE | Overstated. First guidance issued with results is routine and adds no signal beyond FLAG-GUIDANCE-TOWERS. | PR(11-06) p.2; B05 2A arithmetic |
| F6 | MINOR | B06 FLAG-WC-ABOVE-PEERS | Overstated: gross current asset days compared with peer net cycles. Anawil's net cycle is about 178 days at Mar-26 (derived), inside the 86 to 210 day peer range. | CRISIL p.2; INOX Q3FY26 p.7; H1 p.7 |
| F7 | MINOR | B06 Q3 and Q9; flags; coverage map | Anchor error. The Inox South India tower plant quote is on INOX Q2FY26 [page 4], not [page 3]. | INOX Q2FY26 file lines 107-111 |
| F8 | MINOR | B05 (absent) | Missed: CS and Compliance Officer exit with three different reasons and a 30-day gap from letter to disclosure. | Ann 2026-10-31 letter p.1; Ann 2026-10-31 p.1, p.3 |
| F9 | MINOR | B05 (absent) | Missed: the "no forward-looking statement" undertaking is followed by forward-looking margin statements in the outcome note. | Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2 |
| F10 | MINOR | B06 (absent) | Missed: the "4XM" order-book line likely ties Inox (4X platform) as a small customer that is insourcing towers [INFERENCE]. | Pres p.21; INOX Q1FY27 p.4 |
| F11 | MINOR | B05 1C LOI row; 2A row 2 | Under-weighted: the Q1 FY27 LOI is absent from the prospectus post-balance-sheet events but was used to market the listing four days later. | Pros p.236-237; List p.2, p.8 |
| F12 | MINOR | B05 2A row 5 | Under-weighted: the derived inflow of 48 towers equals the two announced orders exactly, so firm inflow outside them is about zero for seven months. | Pros p.114; Order(09-10) p.2; Ann 2026-10-29 p.2; Pres p.21 |
| F13 | MINOR | B05 2C consistency; 3D | Under-weighted: deck placeholder "Text" (Pres p.7), ROE 57% against RONW 40.92% unlabelled (Pres p.25; List p.15), and withheld names on the two orders that make 48.6% of the book. | Pres p.7, p.21, p.25; List p.15; Order(09-10) p.2; Ann 2026-10-29 p.2 |
| F14 | MINOR | B06 2B | Under-weighted: the Suzlon FY27 EBITDA guidance cut (about 17% to 15% plus 1%) on mix is not named. | SUZ Q2FY27 p.9-10 |
| F15 | MINOR | B05 2A, 2C | Under-weighted: no sequential comparison of the headline KPI or PAT (H2 FY26 to H1 FY27: PAT down 57%; EBITDA per tower 34.5 to 33.7 lakh, P&L basis). | H1 p.4; Pres p.18 |

**Severity counts (findings): CRITICAL 0, MAJOR 3, MINOR 12.**

---

## 7. Scoring basis

- Independent list: 25 items. Material (CRITICAL + MAJOR): 7, all MAJOR.
- Material caught: 7 of 7. That is 4 CAUGHT and 3 PARTIALLY CAUGHT. I count PARTIALLY CAUGHT as caught because the rubric defines `material_caught` as items "the pipeline already had". All three were found by B05; the dispute is weighting, and it is carried as the three MAJOR findings F1 to F3. On a strict reading that counts only fully caught items, the rate would be 4 of 7 (57%). I report the rubric reading in the block.
- acceptance_rate: 100 (7 / 7). Denominator is 7, so rule 7 (null below 4) does not apply.
- Coverage limits: no main-company transcript. The 2026-11-09 call is the first upload item and should re-open R1, R3 and R6. I did not read the prospectus whole or the audited FY26 statements beyond one grep. The prospectus page for the litigation chapter is taken from B05 (p.240-241); the text matches at file lines 15300 to 15330.

```yaml
stage: B12b
company: "ANAWIL"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
independent_flags_found: 25
caught: 12
partially_caught: 10
missed:
  - {severity: "MINOR", item: "CS and Compliance Officer resignation: letter dated 2026-10-01 ('personal reasons') disclosed 2026-10-31; filing body says 'pre-occupation', Annexure-I says 'to pursue career opportunities outside the organization'; letter 52 days after listing", anchor: "Ann 2026-10-31 KMP letter p.1; Ann 2026-10-31 NSE intimation p.1, p.3; Ann 2026-11-03 p.1-3"}
  - {severity: "MINOR", item: "Investor-meet intimations promise no forward-looking statement; the 2026-10-05 outcome note publishes forward-looking margin and EBITDA-per-tower statements", anchor: "Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2"}
  - {severity: "MINOR", item: "Order-book line '4XM, 12, Rs 0.6 Cr' (Customer H) matches Inox's 4X platform; [INFERENCE] Inox may be a small existing customer that is building its own South India tower plant", anchor: "Pres p.21; INOX Q1FY27 p.4; INOX Q2FY26 p.4"}
pipeline_flags_not_supported: []
promise_delivery_spot_checks: {checked: 5, confirmed: 4, wrong: 1}
credibility_grade_concur: "concur: C holds on the delivery record (re-scored 3 delivered, 2 partial, 1 missed) but sits at its floor; the under-weighted Kutch contradiction, CARE deviation versus results note 10, the tax-litigation statement and the 81% slip of Dec-2026-due towers point to D if the H1 transcript or H2 print confirms them"
findings:
  - {severity: "MAJOR", location: "B05 2A row 4; promise_delivery row 4; peer_questions item 5", finding: "Kutch promise scored Partial; evidence reads MISSED or REGRESSED. B05 did not use the prospectus statement that Kutch supplied 16 towers (Rs 877.74 lakh) in March 2026 or the 4,822.20 MT March output, so it missed the cross-filing contradiction with 'nearing completion, trial runs underway'", evidence: "Pros p.232; List p.9; PR(11-06) p.3; Pres p.18, p.23"}
  - {severity: "MAJOR", location: "B05 2A row 1; promise_delivery row 1", finding: "CARE 'Deviation: Yes' scored Delivered and mis-described as machinery mixed with debt repayment; omits 'all utilisation as per offer document: No', Rs 2 Cr of the debt object to working-capital borrowings, Rs 0.04 Cr excess transferred to the promoter selling shareholder, and the clash with results note 10", evidence: "MA p.3, p.4, p.6; H1 p.5-6; Pros p.6"}
  - {severity: "MAJOR", location: "B05 2A row 5; timeline_slippages", finding: "Order-book slip under-weighted: by product-description match at least 182 of 225 towers (81%) due by 2026-12-31 remain open at 2026-10-31 and one tower is past its 2026-09-30 date; 'cannot separate old from new' does not hold", evidence: "Pros p.114; Pres p.18, p.21"}
  - {severity: "MINOR", location: "B05 2A reproduction check; FLAG-METRIC-REFRAME; input_gaps", finding: "Overstated: Rs 32.82 lakh reproduces exactly as cash-flow operating profit before working-capital changes 3,511.65 lakh / 107 towers (FY26 base 6,001.21 / 210 = 28.58 lakh, +14.8%); withdraw 'implies 109.9 towers'; the defect is the EBITDA label, Rs 0.97 Cr below reported EBITDA of Rs 36.08 Cr", evidence: "H1 p.8; PR(11-06) p.2"}
  - {severity: "MINOR", location: "B05 FLAG-FIRST-GUIDANCE", finding: "Overstated: first guidance issued with a results print is routine; no signal beyond FLAG-GUIDANCE-TOWERS", evidence: "PR(11-06) p.2; B05 2A"}
  - {severity: "MINOR", location: "B06 FLAG-WC-ABOVE-PEERS", finding: "Overstated: CRISIL gross current asset days (292) compared with peer net cycles; Anawil net working capital about 178 days at Mar-26 (derived), inside the 86-210 day peer range", evidence: "CRISIL p.2; INOX Q3FY26 p.7; H1 p.4, p.7"}
  - {severity: "MINOR", location: "B06 Q3, Q9, flags, coverage map", finding: "Anchor error: Inox South India tower plant quote is on INOX Q2FY26 [page 4], not [page 3]", evidence: "INOXWIND-Concall_Nov_2025 file lines 107-111"}
  - {severity: "MINOR", location: "B05 (absent)", finding: "Missed CS and Compliance Officer exit with three reasons and a 30-day letter-to-disclosure gap", evidence: "Ann 2026-10-31 letter p.1; Ann 2026-10-31 p.1, p.3"}
  - {severity: "MINOR", location: "B05 (absent)", finding: "Missed: no-forward-looking-statement undertaking followed by forward-looking margin statements", evidence: "Ann 2026-09-21 p.1; Ann 2026-09-24 p.1; Ann 2026-10-05 p.2"}
  - {severity: "MINOR", location: "B06 (absent)", finding: "Missed: '4XM' order-book line likely ties Inox as a small customer that is insourcing towers [INFERENCE]", evidence: "Pres p.21; INOX Q1FY27 p.4"}
  - {severity: "MINOR", location: "B05 1C LOI row; 2A row 2", finding: "Under-weighted: Q1 FY27 LOI absent from prospectus post-balance-sheet events, then used to market the listing four days later", evidence: "Pros p.236-237; List p.2, p.8; CRISIL p.1"}
  - {severity: "MINOR", location: "B05 2A row 5", finding: "Under-weighted: derived inflow of 48 towers equals the two announced orders (38 + 10), so firm inflow outside them is about zero for seven months", evidence: "Pros p.114; Order(09-10) p.2; Ann 2026-10-29 p.2; Pres p.21"}
  - {severity: "MINOR", location: "B05 2C consistency; 3D", finding: "Under-weighted: deck placeholder 'Text', ROE 57% vs RONW 40.92% unlabelled, counterparty names withheld on the two orders that make 48.6% of the book", evidence: "Pres p.7, p.21, p.25; List p.15; Order(09-10) p.2; Ann 2026-10-29 p.2"}
  - {severity: "MINOR", location: "B06 2B", finding: "Under-weighted: Suzlon FY27 EBITDA guidance cut from about 17% to 15% plus 1% on mix not named", evidence: "SUZ Q2FY27 p.9-10"}
  - {severity: "MINOR", location: "B05 2A, 2C", finding: "Under-weighted: no sequential comparison (H2 FY26 to H1 FY27 PAT down 57%; EBITDA per tower 34.5 to 33.7 lakh on P&L basis); YoY is the seasonally fair basis, so completeness only", evidence: "H1 p.4; Pres p.18"}
critical_count: 0
major_count: 3
minor_count: 12
material_found: 7
material_caught: 7
acceptance_rate: 100
coverage_basis: "7 material (0 CRITICAL, 7 MAJOR) of 25 listed; 4 caught, 3 partially caught (counted as caught: the pipeline already had them; weighting disputed in 3 MAJOR findings), 0 material missed; 3 MINOR missed. Strict caught-only reading would be 4 of 7 (57%)."
```
