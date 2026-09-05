# Stage 8: Promoter & Key Management Background Check
## Visaka Industries Ltd (VISAKAIND) — BSE 509055 / NSE VISAKAIND / ISIN INE392A01013
Run date: 2026-09-05 | Model: claude-sonnet-5 | Mode: pipeline (web-search heavy)

Status note up front: inputs/announcements/ and inputs/shareholding/ were empty for
this run (degradation note). This check leaned on web search for the SEBI
shareholding pattern trend and the documented-action record. Several source
domains were blocked by the container's egress proxy (see SEARCH LOG). Where a
finding rests on a blocked-domain search snippet rather than a direct-read
primary document, this is marked. Status: **partial**.

---

## SECTION 1: PROMOTER IDENTITY & FAMILY MAPPING

### 1A. Family tree, roles, tenure, holdings, other directorships

| Person | Role at Visaka | DIN | Holding (31-Mar-2026) | Other directorships / roles |
|---|---|---|---|---|
| Dr. G. Vivek Venkatswamy Gaddam (also "G. Vivekanand") | Chairman, Non-Executive Promoter Director | 00011684 | 3,43,65,215 shares = 39.77% (AR FY26 p.181, Note 16C) | Non-exec director, Visaka Thermal Power Ltd (AR FY26 p.123). **Concurrently: Telangana Cabinet Minister for Labour, Employment Training & Factories, Mines & Geology, sworn in 8-Jun-2025** (Wikipedia "G. Vivekanand", cross-checked against Revanth Reddy ministry page); MLA, Chennur (SC), since Dec-2023; former Lok Sabha MP, Peddapalli (2009-14, Congress ticket); former President, Hyderabad Cricket Association (Telangana Today, Deccan Chronicle). ✅/📰 mixed tier, detailed in 1D and 4D. |
| Smt. G. Saroja Vivekanand (Saroja Gaddam) | Managing Director | 00012994 | 32,20,695 shares = 3.73% (same note) | Non-exec director, Visaka Thermal Power Ltd (AR FY26 p.123). Spouse of Dr. Vivek Venkatswamy; mother of G. Vamsi Krishna (AR FY26 p.124). |
| Shri G. Vamsi Krishna (Vamsi Gaddam) | Joint Managing Director | 03544943 | not separately disclosed as >5%/promoter individual in Note 16C | Founder, Atumobile Private Limited (EV venture) (The Weekend Leader profile). Son of Dr. Vivek Venkatswamy and Smt. Saroja. |
| Dr. G. Vritika (Vritika Gaddam) | Chief Business Strategist and Advisor to the Chairman (new FY26 paid role, w.e.f. 1-Apr-2025) | — | not disclosed as promoter shareholder | MBBS, MD (Dermatology); co-founder, NAVA Skin and Body Clinic (web search). Daughter of Smt. Saroja Vivekanand (AR FY26 Note 40, p.201). Remuneration FY26: Rs 25.88 lakh (Note 40). No prior corporate-strategy or building-materials background found. |
| Mrs. G.Vaishnavi | No executive role | — | holds public deposits, receives dividend (Note 40) | Daughter of Smt. Saroja Vivekanand. |
| Mr. G.Venkat Krishna | No executive role | — | small public-deposit holder | Son of Smt. Saroja Vivekanand (third child, per RPT note — distinct from Vamsi and Vritika). |
| Mrs. K.Vimala | No role | — | small public-deposit holder | Mother of Smt. Saroja Vivekanand. |

Two named promoter individuals together hold 43.50% (unchanged year on year, AR FY26 p.181). This is **materially below** the 53.24% "Promoters — Indian" category total in the Corporate Governance Report (AR FY26 p.132) — see 1B and Section 6D for the reconciliation, which is the single largest shareholding-disclosure finding of this check.

Board related-party disclosure (AR FY26 p.124, CG Report clause viii) confirms the family map cleanly: Chairman is spouse of the MD and father of the JMD; MD is mother of the JMD. No inter-se relationship concealment found.

### 1B. Promoter group entities

From Note 40 (Related Party Transactions), AR FY26 p.201, "Enterprises in which KMP and/or their relatives have control":

| Entity | Nature / activity found | Transactions with Visaka FY26 | Status |
|---|---|---|---|
| Visaka Thermal Power Limited | Power generation (unlisted); Chairman and MD both sit as non-exec directors | No P&L transaction disclosed in Note 40 FY26 | Active |
| Visaka Charitable Trust | CSR/charitable | Not itemised in FY26 transaction table | Active |
| VIL Media Private Limited | Media; family co-founded V6 News, a Telugu news channel (web search, unverified corporate link between VIL Media and V6 News specifically — ❓) | **Advertising expenses Rs 1,112.57 lakh (~Rs 11.13 Cr) paid by Visaka in FY26**, Rs 1,192.64 lakh in FY25 (Note 40) | Active — material RPT, no arm's-length benchmarking disclosed |
| V-Solar Roofing Private Limited | Solar-adjacent | No FY26 transaction shown | Active |
| G Vivekanand family trust | Family trust | Dividend received Rs 0.92 lakh | Active |
| SV family trust | Family trust | Dividend received Rs 0.39 lakh | Active |
| Arudra Roofings Private Limited | Roofing (unlisted); Vaishnavi Gaddam is a director (web search) | Rent expense Rs 24.00 lakh paid by Visaka; **dividend received by Arudra jumped from Rs 3.75 lakh (FY25) to Rs 14.20 lakh (FY26)** — at the constant Rs 0.50/share DPS disclosed in Note 36B, this implies Arudra's own Visaka shareholding roughly quadrupled between the two dividend record dates (from ≈7.5 lakh to ≈28.4 lakh shares, ≈0.9% to ≈3.3%) | Active — see 6D reconciliation |
| Atumobile Private Limited | EV venture founded by JMD Vamsi Krishna | Rental income Rs 10.08 lakh received by Visaka | Active |
| **Vigilance Security Services Private Limited** | Security services (registered name); Ramagundam/Hyderabad | See dedicated treatment below | Active — **the single most important entity in this check** |
| Visaka Green Private Limited | Subsidiary (100%), formerly Vnext Solutions | ICD outstanding Rs 650 lakh receivable; net worth ≈Rs 519.6 lakh (share capital 651.00 + reserves (131.45)) vs total assets 1,558.75 lakh (Form AOC-1, AR FY26 p.82) | Active, loss-making (PAT FY26 loss Rs 168.50 lakh) |
| Atum Life Private Limited | Subsidiary (100%) | See 1B/6 write-up below — **near-zero net worth against unimpaired Rs 779.50 lakh investment** | Active, loss-making |

**Vigilance Security Services Pvt Ltd — the load-bearing entity.**
✅ VERIFIED (CIN U45100TG1989PTC010383, incorporated 24-Aug-1989, Hyderabad — Zaubacorp/Tracxn/InstaFinancials, cross-checked). Only added as a *disclosed* Companies Act related party "w.e.f. 07th December 2023" (AR FY25, p.183 equivalent, Note 40) — **16 days after** a 21-Nov-2023 Enforcement Directorate/Income Tax search that publicly identified Vigilance Security Services as the counterparty in a Rs 8 crore transfer from Dr. Vivek Venkatswamy's personal account under investigation (see Section 2B). The company's own related-party disclosure of this entity therefore appears to have followed, not preceded, law-enforcement exposure of the relationship — a disclosure-timing red flag (❓/📰, single-thread but corroborated by the AR's own effective date and the raid date being 16 days apart).

Per a web search snippet of an NSE corporate disclosure (nsearchives.nseindia.com, blocked for direct fetch by this container's proxy — see SEARCH LOG), Vigilance Security Services Pvt Ltd holds 41,69,120 equity shares of Visaka Industries (4.83% of paid-up capital) and **"has become a member of the promoter group under Regulation 2(pp)(iv)(B) of SEBI (ICDR) Regulations, 2018"** during the period covered by this run. Vigilance Security Services is itself 93.55% owned by Yeshwanth/Yeshwant Realtors Pvt Ltd (web search), which ED investigators separately describe as majority-owned by a foreign national (see Section 2B). 📰 MEDIA/EXCHANGE-REPORTED, corroborated across two independent search results and internally consistent with the AR's own numbers (see 6D).

Red flags on the 1B set: (i) entity count and structure (multiple family trusts, a media company, a security-services company with negligible declared operating revenue holding a meaningful listed-company stake, an EV startup, a thermal power company) is disproportionate for a mid-cap building-materials manufacturer; (ii) Vigilance Security Services' declared "revenue from operations" was reported by ED as ~Rs 20 lakh against ~Rs 64 crore of assets, "primarily long-term loans/advances" (thesouthfirst.com, taxscan.in — 📰); (iii) VIL Media's Rs 11-12 crore/year advertising spend from Visaka is priced with no disclosed benchmarking.

### 1C. Education and professional background

- Dr. G. Vivek Venkatswamy Gaddam: MBBS, Osmania University (web search, Wikipedia "G. Vivekanand"); non-executive Chairman since stepping back from an executive role, consistent with holding concurrent public office.
- Smt. G. Saroja Vivekanand: no independently verifiable professional/educational credential found beyond her role tenure; AR does not disclose qualifications in the CG report bio table (this table does not carry bios at all — a general AR format gap, not unique to Visaka).
- Shri G. Vamsi Krishna: entrepreneurial background evidenced by founding Atumobile Private Limited (EV) (The Weekend Leader) — an operating credential distinct from inherited role.
- Dr. G. Vritika: MBBS, MD (Dermatology); co-founder of a skin/dermatology clinic. No disclosed background in business strategy, building materials, or corporate finance — the "Chief Business Strategist and Advisor to the Chairman" title does not map to a verifiable prior competency. ❓ flag for role-fit, not for the credential's authenticity.

### 1D. History before the current company

Company founded 1981; multiple sources (The Weekend Leader, on Vamsi Gaddam) describe it as founded by "his grandfather... and his father G Vivekanand" — i.e., Dr. Vivek Venkatswamy Gaddam is second-generation, not the founder himself in the strict sense, though AR materials and most financial media describe him as "Chairman" without founder/inheritor distinction. This is a minor factual reconciliation item, not a red flag.

Separately and materially: Dr. Vivek Venkatswamy Gaddam has run a fourteen-year political career in parallel with chairing Visaka — MP (2009, Congress) → TRS/BRS → BJP (9-Aug-2019) → Congress (1-Nov-2023) → MLA Chennur (Dec-2023) → Telangana Cabinet Minister (8-Jun-2025). One Telugu-media commentary piece (Tupaki, translated) characterises this as "changed six parties in 14 years, joined the same party four times." 📰 This pattern, while a matter of political record rather than corporate wrongdoing, is a relevant character signal under this check's remit (see Section 4D and 6A).

---

## SECTION 2: LEGAL & REGULATORY RECORD

### 2A. SEBI actions
No SEBI adjudication order, SAT appeal, insider-trading action, LODR non-compliance order, market ban, or consent order against Visaka Industries or its promoters was found in searches (SEBI enforcement-order search, CaseMine search). **Clean record on this specific sub-area** — stated per the "clean record is a finding" rule. Absence of a hit is not proof of absence given search-engine indexing limits, but no credible source surfaced anything. ✅ (by absence)

### 2B. Criminal cases — the dominant finding of this entire check
✅/📰 VERIFIED-and-MEDIA-REPORTED, corroborated across at least six independent outlets (Deccan Chronicle, Deccan Herald, The Federal, NewsMeter, The South First, TaxScan, Siasat, TheHansIndia, IANS), all reporting the same core facts with consistent details:

- **21-Nov-2023**: The Enforcement Directorate (ED), acting on a Telangana Police reference, conducted search operations at multiple locations (reported variously as four and as nine locations across different outlets) including Dr. Gaddam Vivek Venkatswamy's residences in Hyderabad (Somajiguda) and Mancherial, **the Visaka Industries Ltd corporate office in Begumpet, Hyderabad**, and the office of Vigilance Security Services Pvt Ltd in Ramagundam. One outlet (Siasat/IANS) states the searches were conducted under the **Prevention of Money Laundering Act (PMLA), 2002**; other outlets frame the probe as a **FEMA (Foreign Exchange Management Act)** case. Both statutes appear to be in play (ED frequently invokes PMLA search powers while investigating a FEMA-predicate matter).
- Trigger: a Rs 8 crore transfer from Dr. Vivek Venkatswamy's personal bank account to Vigilance Security Services Pvt Ltd, alleged by investigators to be a "circuitous" transfer "with no real business rationale," with suspicion the funds were destined to be converted to cash for election-related use (searches occurred 9 days before the 30-Nov-2023 Telangana Assembly poll, in which Dr. Vivek Venkatswamy was the Congress candidate for Chennur).
- ED's stated findings (The South First, TaxScan): Dr. Vivek Venkatswamy and his wife (Smt. Saroja, Visaka's MD) hold **"indirect" control** over Vigilance Security Services; cumulative transactions between the couple/Visaka Industries and Vigilance Security Services were put at **"over Rs 100 crore"** by one outlet and **"suspicious/unaccounted transactions worth Rs 200 crore"** by another; Vigilance Security Services' own balance sheet reportedly showed ~Rs 20 lakh of "revenue from operations" against ~Rs 64 crore of assets, mostly long-term loans/advances.
- Alleged FEMA contraventions: by Vigilance Security Services and its parent Yeshwant Realtors Pvt Ltd (majority shares reportedly held by a foreign national), and separately in the incorporation of an entity by Dr. Vivek Venkatswamy in a foreign tax-haven jurisdiction (South First/TaxScan). None of these specifics were independently verifiable beyond the media reporting in the time available; treat as 📰 MEDIA REPORTED, not ✅ VERIFIED, pending a primary ED order.
- Search extended to a premises of Gaddam Vinod (Dr. Vivek Venkatswamy's brother, a Congress candidate and former Hyderabad Cricket Association president), described as being used as an office for companies controlled by Dr. Vivek Venkatswamy.
- **No confirmed resolution found**: no chargesheet, no confirmed asset attachment under PMLA, no confirmed closure report, and no exchange (BSE/NSE) material-event disclosure of the raid was located in this run's searches. This is a genuine, unresolved evidentiary gap — the case's current (Sep-2026) status is NOT FOUND.
- **The company continued and deepened its relationship with the exact counterparty named in the raid, after the raid**: Vigilance Security Services was formally added as a disclosed related party effective 7-Dec-2023 (16 days post-raid); it began receiving disclosed dividends from FY25; in FY26 it extended a **Rs 21.00 crore ICD facility to Visaka Industries at 8% p.a.** (Rs 5.25 crore outstanding, Rs 48.64 lakh interest payable at 31-Mar-2026 — Note 40, AR FY26 p.205), and was **formally reclassified into the SEBI-defined "promoter group"** during FY26 (Section 6D). This sequence — investigation, then deepening of financial and disclosed-ownership ties with the flagged entity — is the single most serious finding of this check.

Separately, **Dr. Vivek Venkatswamy personally extended round-trip loans to the company in two of the three years examined**: FY24 (Rs 500 lakh from him + Rs 800 lakh from Smt. Saroja Vivekanand, both received and fully repaid within FY24, interest Rs 3.99 lakh and Rs 10.12 lakh respectively — AR FY25 p.187, Note 40 prior-year column) and FY26 (Rs 1,303.00 lakh from Dr. Vivek Venkatswamy alone, received and repaid within FY26, interest Rs 16.33 lakh — AR FY26 p.204, Note 40). FY25 had none. This is a recurring practice, not a one-off, and its economic purpose (why does a company with Rs 2,418.98 lakh of cash and cash equivalents and Rs 1.68 billion of "other current assets" need same-year round-trip promoter loans) is not explained in either AR.

### 2C. Tax and revenue
- Income Tax assessment order for AY2024-25 with a Rs 92.80 lakh demand, under appeal at CIT(A), Hyderabad (Note 38 contingent liabilities and CARO vii(b), AR FY26 pp.153, 203; also confirmed independently via scanx.trade). Routine tax-dispute scale for a company this size; not a red flag by itself.
- Numerous smaller VAT/GST/excise/service-tax disputes across Orissa, Uttar Pradesh, Tamil Nadu, West Bengal, Bihar spanning 2005-2025 assessment years, aggregating Rs 660.24 lakh in the CARO vii(b) table (AR FY26 pp.152-153) — normal multi-state manufacturer tax-dispute footprint, no search-and-seizure or benami finding disclosed by the auditor (CARO i(e): no benami proceedings pending — AR FY26 p.150).
- No DRI, SFIO, or benami action found in web search.
- The Nov-2023 ED search (2B above) was accompanied by simultaneous Income Tax department searches at the same premises (Siasat: "I-T officials raid... following an Rs 8 crore transfer from Visaka Industries," verifying ITRs, investments, purchase/sale reports, bank statements at the Visaka Industries Begumpet office). This sits at the boundary of 2B/2C; recorded once here for completeness.

### 2D. Other regulators
- No RBI, IRDAI, TRAI, MCA compounding/disqualification, NCLT oppression petition, CCI, or NGT-specific order against Visaka Industries or its promoters was found in this run's searches.
- Historical, dated ESG-adjacent item: a 2012-vintage dispute over a No Objection Certificate for a Visaka asbestos-cement plant in Sambalpur district, Odisha (Parmanpur village), which local residents won at the district-administration level (asbestosfreeindia.org, downtoearth.org.in). This predates the current run's evidence window by well over a decade and is noted for completeness under industry-reputation (4E), not scored as a live legal risk.
- The company's core product (cement roofing sheets, 53% of FY26 standalone revenue per the BRSR general disclosures, AR FY26 p.99) sits within an industry (asbestos-cement) that carries ongoing national-level regulatory and NGT attention on phase-out policy (NGT/asbestosfreeindia.org, Nov-2025 item) — an industry-wide structural risk, not promoter-specific, flagged for context only.

### 2E. Civil litigation
- **Hyderabad Cricket Association (HCA) arbitration**: a 2004 sponsorship agreement between Visaka Industries and HCA (naming/advertisement rights, Rajiv Gandhi International Cricket Stadium) led to a 2016 arbitral award of Rs 25.92 crore plus 18% p.a. interest in Visaka's favour. HCA's challenges were dismissed by the Commercial Court, Hyderabad (19-Jul-2024), the Telangana High Court (25-Jun-2025), and the Supreme Court (SLP dismissed 6-Oct-2025); the award (now ~Rs 68.73 crore with accrued interest) remains unpaid by HCA as of the most recent report found. Dr. Vivek Venkatswamy — who was **himself a former President of HCA** at a time overlapping the original sponsorship relationship — publicly rejected allegations from the Telangana District Cricket Association (TDCA) that the transfer/award involved misappropriation, and TDCA separately sought a BCCI probe into HCA's Rs 70 crore transfer obligation to Visaka. 📰 The self-dealing optics (former association president's own company benefiting from an arbitral award against that same association) are worth noting even though the underlying legal process has been upheld at every level including the Supreme Court — this is a conflict-of-interest texture point, not a finding against the legal merits of the award.
- No family partition suit, oppression petition, or JV dispute touching Visaka's assets was found.

### 2F. Legal red flag summary table

| Sub-area | Finding | Severity |
|---|---|---|
| 2A SEBI | Clean (no hit found) | ✅ |
| 2B Criminal/economic offence | ED/IT search Nov-2023 at company premises, unresolved FEMA/PMLA probe into promoter-controlled entity now a lender and promoter-group member | 🔴 |
| 2C Tax | Routine multi-state disputes + one AY24-25 demand under appeal; simultaneous I-T search alongside 2B | ⚠️ |
| 2D Other regulators | Clean on RBI/MCA/NCLT/CCI/NGT for the company; asbestos-industry structural context noted | ✅ (company-specific), ⚠️ (industry context) |
| 2E Civil litigation | HCA arbitration won on the merits through the Supreme Court, but chairman's own former HCA presidency creates conflict-of-interest optics | ⚠️ |

---

## SECTION 3: BUSINESS CONDUCT & ETHICAL TRACK RECORD

### 3A. RPT history
- **VIL Media Private Limited**: Rs 1,112.57 lakh (FY26) / Rs 1,192.64 lakh (FY25) advertising expense paid by Visaka to a promoter-family media entity, no arm's-length benchmarking disclosed in either AR.
- **Arudra Roofings Private Limited**: Rs 24.00 lakh/year rent paid by Visaka (flat FY25→FY26); Arudra's own Visaka shareholding appears to have roughly quadrupled year on year based on dividend-received math (Section 1B) — a competing-or-affiliated roofing entity increasing its stake in the listed roofing company it does business with is worth the operator's independent verification.
- **Vigilance Security Services Pvt Ltd**: Rs 21.00 crore ICD facility extended TO Visaka in FY26 at 8% p.a. (Rs 5.25 crore outstanding, Rs 48.64 lakh interest payable at year end); Rs 20.85 lakh dividend received; now a disclosed 4.83% promoter-group shareholder. See Section 2B for the entity's regulatory-scrutiny history.
- **Loans to/from promoters** (round-trip, same-year): Rs 13 crore in FY24 (Chairman Rs 5 Cr + MD Rs 8 Cr), Rs 13.03 crore in FY26 (Chairman alone). No FY25 activity.
- **Credit-impaired ICDs to unrelated (non-RPT-disclosed) counterparties**: Bhagyanagar Hotels (Rs 150 lakh outstanding, 12% p.a., due 31-Mar-2025, now fully provided) and Galvanizz Projects Private Limited (Rs 550 lakh outstanding, 12% p.a., due 31-Mar-2025, now fully provided) — combined Rs 700 lakh (Rs 7.00 crore) **loss allowance recognised in full in FY26** (Note 12, AR FY26 p.179; CARO iii(c)/(d), AR FY26 pp.150-151). Neither entity appears in the Note 40 related-party list, meaning the company itself does not classify them as related parties, yet it extended unsecured ICDs to them that are now fully written off with no public explanation of the underlying commercial rationale in either AR.
- **Sreenidi-Deccan Football Club Private Limited**: Rs 600 lakh (Rs 6.00 crore) ICD granted in FY26 at **18% p.a.**, "repaid within due date" (Note 12, AR FY26 p.179) — a materially higher rate than the 10-12% charged on the subsidiary/related-party ICDs in the same note, extended to a Hyderabad-based football club with no disclosed business rationale for a fibre-cement/synthetic-yarn manufacturer. Web search found no confirmed ownership link between the Gaddam/Visaka family and Sreenidi Deccan FC (club is reported as owned by "Sreenidhi Group," a distinct entity per Wikipedia — ❓ unconfirmed, do not treat as an established related-party link, but the transaction's rationale remains unexplained and its 18% rate is anomalous within the company's own ICD book).
- Guarantees: none extended to related or third parties (CARO iii(a), AR FY26 p.150-151).

### 3B. Capital allocation behaviour
- **Executive remuneration disclosure inconsistency — a direct, internal contradiction inside the FY26 AR itself.** Note 40 (RPT disclosure, p.201) shows Smt. Saroja Vivekanand's remuneration rising from Rs 206.09 lakh (FY25) to Rs 324.71 lakh (FY26), a **+57.6% (≈58%) increase**, and Shri G. Vamsi Krishna's rising from Rs 142.64 lakh to Rs 295.91 lakh, a **+107.5% (≈107%) increase**. The statutory Rule 5(1) remuneration annexure (Annexure-6, AR FY26 p.97), signed by Dr. G. Vivek Venkatswamy as Chairman on 18-May-2026, states the "percentage increase in remuneration" for both the MD and JMD as **"Nil,"** and separately states in prose: **"There is no increase in remuneration of Executive Directors."** These two disclosures, both inside the same annual report, cannot both be correct given the underlying rupee figures are drawn from the audited financial statements. This is a disclosure-integrity red flag, not merely a rounding or timing artefact — the magnitude (58% and 107%) is far too large to be a presentation quirk. ✅ VERIFIED as an internal AR inconsistency (both figures come directly from the AR text, not from an external source).
- The FY26 remuneration rise coincides with a **Rs 59.70 crore exceptional gain from land sales** (Ahmedabad, Gujarat: Rs 36.74 crore; Kanchipuram, Tamil Nadu: Rs 22.96 crore — per scanx.trade and Prysm Finance reporting of the FY26 results, cross-checked against the AR's PAT jump from Rs 14.38 lakh FY25 to Rs 8,783.24 lakh FY26, Note 41). Since executive commission is profit-linked (5% of net profit ceiling per the Nomination & Remuneration Policy, AR FY26 p.90), a one-off asset-sale gain flowing through to materially higher promoter-family cash compensation, while the company's own statutory annexure asserts no increase occurred, is a governance-quality concern independent of whether the commission calculation itself is technically within the Companies Act ceiling.
- Dividend: Rs 0.50/share paid in both FY25 and FY26 (on profit bases of Rs 14.38 lakh and Rs 8,783.24 lakh respectively — i.e., a flat payout despite a ~600x swing in reported profit); FY26 proposed final dividend (payable in FY27) raised to Rs 1.20/share (60% of face value), reflecting the FY26 exceptional gain (Note 36B, AR FY26 p.201).
- No preferential allotment, warrant issue/lapse, or buyback in the period reviewed (CARO x(a)/(b), AR FY26 p.152).

### 3C. Promoter share transactions
- Pledge: **0% currently** (see Section 6D/pledge fields). Historically, per a 2009 Business Standard report, G. Vivekanand had pledged 16.76 lakh shares (10.55%) and Saroja Vivekanand 1.10 lakh shares (0.69%) — both since released; current status confirmed by a FY26 non-encumbrance declaration referenced in a scanx.trade summary ("Chief Promoter Dr. Vivek Venkatswamy Gaddam submitted a declaration covering nine promoter entities... Promoters and promoter group members did not encumber any company shares during FY26"). 📰 (direct scanx.trade page fetch blocked by proxy; relying on the search-engine summary of that page, corroborated by a second independent search result reporting "no shares pledged" as of June 2026).
- Creeping/reclassification into the promoter category: see Section 6D — the dominant explanation is Vigilance Security Services' formal SEBI ICDR promoter-group reclassification (41,69,120 shares, 4.83%), not open-market creeping acquisition by the named individuals (whose holdings are unchanged to the share).
- No sales timed ahead of bad news or suspicious pre-announcement trades were found; named individual promoters made zero share transactions in either year reviewed.

### 3D. Minority treatment
- No SCORES complaint volume disclosed in the AR beyond generic ODR-portal boilerplate (AR FY26 p.140 equivalent) — the standard investor-complaint count table was not located in the extracted pages reviewed; treat as NOT FOUND rather than clean.
- No proxy-advisory (IiAS/InGovern/SES) report on Visaka Industries was found in web search — NOT FOUND, not evidence of a clean record either way.
- No delisting attempt, and the one large recent RPT expansion (Vigilance Security Services' ICD facility and promoter-group entry) does not appear to have required a minority-shareholder vote disclosure that this run's search could locate — this is itself worth the operator's independent check of the FY26 RPT-approval AGM/postal-ballot record, since a Rs 21 crore ICD facility from a newly-classified promoter-group entity would ordinarily need Audit Committee and (depending on materiality thresholds) shareholder approval under SEBI LODR Regulation 23.

### 3E. Auditor relationship
- Statutory auditor: **Price Waterhouse & Co Chartered Accountants LLP** (FRN 304026E/E300009), Hyderabad — a Big-4-network firm, appointed for a five-year term from the 40th AGM to the 45th AGM (2027) (AR FY26 p.76). No resignation, no qualification beyond the standard CARO-level observations on overdue ICDs and multi-state tax disputes (Section 2C/3A). Cost auditor: M/s. Sagar & Associates, reappointed FY26-27 at a modest fee, no issues raised under Section 143(12) (AR FY26 p.76). **This is the cleanest dimension of the entire check.** ✅

---

## SECTION 4: REPUTATION & PUBLIC PERCEPTION

### 4A. Media reputation
Media coverage of Visaka Industries and its Chairman splits into two nearly disconnected streams: (i) routine business-press coverage of results, the Tonk (Rajasthan) plant expansion, and product launches (ALMM solar certification, V-Next, ATUM) — neutral to positive; (ii) politics-and-investigation coverage of Dr. Vivek Venkatswamy Gaddam personally, dominated by the Nov-2023 ED/IT search story and the HCA arbitration controversy, both of which name Visaka Industries directly. 📰 The two streams rarely cross in the financial press (i.e., business coverage of VISAKAIND stock rarely mentions the ED matter), which is itself a finding: an investor reading only sell-side/exchange-adjacent coverage would not encounter the promoter's most serious governance risk.

### 4B. Employee reputation
Glassdoor aggregate ratings (India): 3.4/5 work-life balance, 3.5/5 culture and values, 3.6/5 career opportunities, 3.5/5 compensation and benefits; 72% of reviewers would recommend the company to a friend. Qualitative themes: "very supportive promoters" and good work-life balance cited positively; low engineer salaries and limited career growth cited negatively; job security noted as a relative strength. No pattern of ethics complaints, family-favouritism callouts, or senior-attrition commentary surfaced in the review snippets found. AmbitionBox-specific data could not be isolated from the search results (the search returned AmbitionBox's own Glassdoor employer page, not its reviews of Visaka). ⚠️ moderate/thin evidence, no red flag but no strong positive signal either.

### 4C. Investor and analyst perception
- CARE Ratings reaffirmed Long-Term Bank Facilities and Fixed Deposit ratings at **CARE A+ with a Negative outlook** in FY26 (AR FY26 p.130) — reaffirmed, not downgraded, but the Negative outlook itself is a caution signal on the credit/business trajectory that the operator should weigh alongside the promoter findings.
- No short-seller report or organised activist campaign found.
- Institutional ownership is thin and shrinking, not entering: Foreign Portfolio Investors fell from 0.45% (31-Mar-2025) to 0.10% (31-Mar-2026); Mutual Funds (0.05% FY25) folded into a combined "Banks/FI/Insurance/MF" line at 0.02% FY26 (CG Report categories of shareholders, AR FY26 p.132; AR FY25 p.117). This is the **opposite** of an institutional-entry transition signal (see Section 6D).

### 4D. Political and government connections
This is the largest single qualitative finding of the check, treated in full because of its direct relevance to "dependence is the concern":
- Dr. G. Vivek Venkatswamy Gaddam, Chairman of Visaka Industries, is **concurrently a sitting Telangana Cabinet Minister** — Minister for Labour, Employment Training & Factories, Mines & Geology, in office since 8-Jun-2025 (Wikipedia "G. Vivekanand," cross-checked against the Revanth Reddy ministry list). **His ministerial portfolio (Factories; Mines & Geology) directly overlaps the regulatory domain his own company operates in** (Visaka runs multiple factories and sources mineral/fibre inputs for cement-based products). Neither AR discloses this concurrent public office in the board-composition biography table (AR FY26 pp.123-125), even though it is public information and directly relevant to related-party and conflict-of-interest assessment.
- Fourteen-year record of six party changes (Congress → TRS/BRS → BJP → Congress), the most recent switch on 1-Nov-2023, 29 days before a state election in which he stood as the Congress candidate — an opportunism pattern independently remarked upon in Telugu media (Tupaki).
- Declared assets of ~Rs 606 crore and liabilities of ~Rs 41 crore in his 2023 election affidavit (myneta.info, an ADR/affidavit-aggregation source — ✅ VERIFIED as a filed public disclosure, though the affidavit's own accuracy is self-reported).
- Family-owned media: co-founder of V6 News, a Telugu news channel, which is plausibly (not confirmed with certainty) connected to VIL Media Private Limited, the RPT entity receiving Rs 11-12 crore/year in advertising spend from Visaka Industries (see 3A). A promoter with a media outlet used partly for his own political messaging, funded in part by advertising fees from his listed company, is a dependence-and-self-dealing combination the operator should weigh.
- Former President, Hyderabad Cricket Association — see Section 2E for the arbitration self-dealing optics.
- No disproportionate government contract or land allotment specific to Visaka Industries' business (as distinct from the promoter's general political and land-record controversies, e.g. the Velugu/Revenue Department allegations, which concern government administration generally and were not linked in search results to a benefit conferred on Visaka Industries specifically) was found.

### 4E. Industry peer reputation
Visaka is one of India's larger cement fibre-roofing manufacturers; the asbestos-cement segment as a whole carries a well-documented, industry-wide (not Visaka-specific) reputational and regulatory overhang tied to asbestos health effects, most recently reflected in a Nov-2025 NGT reiteration of a phase-out policy direction (asbestosfreeindia.org). This is background context for the sector, not a promoter-quality finding.

### 4F. Philanthropy beyond mandatory CSR
Visaka Charitable Trust exists as a promoter-family vehicle (Note 40); the AR discloses CSR spend of Rs 107.68 lakh against a Rs 55.48 lakh FY26 obligation, with a large brought-forward CSR credit from prior over-spending (Board's Report, AR FY26 p.73). No evidence of philanthropy materially beyond the mandatory CSR framework was found in web search; NOT FOUND rather than a negative finding.

---

## SECTION 5: CXO & BOARD QUALITY

### 5A. CXO turnover
| Role | Person | Tenure | Exit reason (disclosed) |
|---|---|---|---|
| CEO | Abinash Mishra (external hire; IIT Bombay + Olin Business School; 27 years' cement/building-materials/construction-chemicals experience) | 14-Apr-2025 → 22-Aug-2025 (≈4 months) | "Personal reasons" (Board's Report, AR FY26 p.76; corroborated by Wegro/TradingView/MarketScreener news items) |
| COO & Whole-Time Director | J. Pruthvidhar Rao | Executive Director 2015-2023, then COO/WTD; exited 25-May-2025 | Completion of tenure as Whole-Time Director (natural term completion, not a mid-term resignation) |
| CFO | S. Shafiulla | Appointed 9-Sep-2020; **retired end of May-2026 upon reaching retirement age** (web search, post-FY26-close event) | Age-based retirement, not a resignation under a cloud |
| Company Secretary | K. Ramakanth Kunapuli | ≈3.8 years in role at time of search; stable, small annual raises (5.40%/5.74% FY26, Rule 5(1) table) | No exit; stable |
| Independent Director | P. Srikar Reddy | Exited 24-Jul-2025 | Completion of second and final term (natural, statutory maximum reached) |

A reputable outside CEO hire lasting only four months, with no public elaboration beyond "personal reasons," directly following a period of intensifying promoter-family financial dealings (the FY26 round-trip Chairman loan and the Vigilance Security Services ICD facility both fall within his short tenure window), is a pattern the operator should weigh, though no direct causal link between the CEO's exit and the RPT activity was found or should be assumed from timing alone (❓ correlation noted, causation not established). CFO and Company Secretary continuity through the same period is a partial offset.

### 5B. Board quality
- Board of 8 as at 31-Mar-2026: Chairman (promoter, non-exec), MD (promoter, exec), JMD (promoter, exec), one non-exec non-independent director (Gusti Jall Noria), and four independent directors (Vanitha Datla, Gogineni Appnender Babu, Sanjay Vijay Singh Jesrani, Pravin Chelluri) (AR FY26 p.123).
- Independent directors carry real outside credentials: Vanitha Datla is an independent director of Cyient DLM Ltd (listed) and MD/WTD of Elico entities; Sanjay Vijay Singh Jesrani is an independent director and Audit Committee chair at Zen Technologies Ltd (listed). This is a genuine positive — these are not obviously accommodation appointments. ✅
- Board met 5 times in FY26 with full attendance from all continuing directors (AR FY26 p.124); D&O insurance in place; one Independent Directors-only meeting held (24-Mar-2026).
- Promoter family (Chairman, MD, JMD) occupies 3 of 8 board seats (37.5%), a normal proportion for an Indian promoter-controlled company of this scale, not by itself a red flag.
- The board's biography disclosures do not mention the Chairman's concurrent ministerial office (5B/4D overlap, noted once).

### 5C. Key-person risk and succession
Succession to the third generation is visibly under way: JMD Vamsi Krishna (operational, EV-venture credential) and now Dr. Vritika Gaddam in a newly created advisory role. Key-person risk is concentrated in the Chairman given his simultaneous political office (time and attention split) and in the newly hired-then-departed CEO experiment, which suggests the family has not yet successfully institutionalised a non-family top operating executive layer beneath the JMD.

---

## SECTION 6: PROMOTER QUALITY VERDICT

### 6A. Scorecard (10 dimensions, rated strictly on Sections 1-5 findings)

| # | Dimension | Rating | Basis |
|---|---|---|---|
| 1 | SEBI/legal-regulatory record | 🔴 | Nov-2023 ED/IT search at company premises; unresolved FEMA/PMLA probe (2B) |
| 2 | RPT conduct | 🔴 | Vigilance Security Services deepened post-raid (lender + promoter-group entry); Rs 7 Cr ICD write-off to undisclosed-related counterparties; anomalous 18% ICD to a football club; large undisclosed-arm's-length media ad spend (3A) |
| 3 | Capital allocation / remuneration integrity | 🔴 | Direct internal AR contradiction: Rule 5(1) annexure states "Nil" increase while Note 40 shows +58%/+107% (3B) |
| 4 | Promoter shareholding & pledge | ⚠️ | Pledge is 0% (clean) but the +4.82pp promoter-category jump is opaque in both ARs and resolves (on the evidence found) to a promoter-group reclassification of the ED-flagged entity, not a clean creeping acquisition (6D) |
| 5 | Board independence & quality | ⚠️ | Genuine outside-credentialed independent directors (positive) but Chairman's undisclosed concurrent Cabinet-Minister office is a live conflict-of-interest gap in board disclosure (5B/4D) |
| 6 | Auditor relationship | ✅ | Big-4-network auditor, no resignation, unmodified opinion, standard CARO items only (3E) |
| 7 | CXO/key-management turnover | 🔴 | Outside CEO hire lasted 4 months, unexplained beyond "personal reasons," inside a window of intensifying RPT activity (5A) |
| 8 | Disclosure quality / minority treatment | 🔴 | RPT entity disclosed only after law-enforcement exposure; remuneration-increase misstatement in a signed statutory annexure; no proxy-advisory or SCORES data located (3D, 3B) |
| 9 | Reputation (media/employee) | ⚠️ | Decent employee sentiment; media coverage split between neutral business press and serious unresolved investigation coverage that does not reach most investors (4A/4B) |
| 10 | Political/regulatory dependence | 🔴 | Chairman is a sitting state Cabinet Minister with a portfolio (Factories, Mines) overlapping the company's own regulatory environment; documented serial party-switching; family media entity funded via company RPT spend (4D) |

**Scorecard tally: clean = 2, caution = 3, red = 5** (of 10).

### 6B. Classification
**CONCERN.** The record does not meet a formal deal-breaker threshold as strictly defined (Section 6C), but the combination of an unresolved ED/PMLA investigation touching the company's own premises, a related-party entity that the company has continued to deepen ties with (as lender and now promoter-group member) despite that entity being the specific subject of the investigation, a signed statutory annexure that appears to misstate a material remuneration increase, and a Chairman who is simultaneously a sitting Cabinet Minister with directly overlapping regulatory responsibility, together represent one of the more serious promoter risk profiles this check format can surface short of a confirmed deal-breaker. The operator should treat this as a CONCERN at the severe end of the tier, not a mild one.

### 6C. Deal-breaker checks (recorded, not enforced)
| Deal-breaker | Triggered? | Basis |
|---|---|---|
| SEBI market ban | No | No SEBI order found |
| Economic offence conviction | No | Investigation/search only; no conviction found |
| Live SFIO | No | Not found |
| PMLA with attached assets | **Not confirmed** | PMLA-cited search occurred (21-Nov-2023); no confirmed asset attachment found in this run's searches — this is the closest the record comes to a formal deal-breaker, and the operator should independently verify current ED case status before relying on "not triggered" |
| Auditor resignation within 3 years | No | PwC LLP continuous, no resignation |
| Pledge >40% | No | 0% currently |
| Multiple mid-term independent exits within 3 years | No | The one FY26 independent-director exit was a natural term-completion (statutory maximum), not mid-term |
| Restatement cutting past profits >10% | No | Not found |

No formal deal-breaker is confirmed triggered. **deal_breakers: []** in the YAML reflects this strictly, but the PMLA item above should not be read by downstream stages as "cleared" — it is unresolved, not absent.

### 6D. Transition evidence scan
Searched specifically for signs of improvement. Result: **NONE FOUND**, and on two dimensions the evidence points the opposite way:
- No new professional CEO/CFO from outside the family who has stayed: the one outside CEO hire (Abinash Mishra) departed after 4 months; the CFO transition (Shafiulla's retirement, May-2026) is age-based, not a governance upgrade, and his successor was not identified in this run.
- No institutional investor entry: FPI holding **fell** from 0.45% (FY25) to 0.10% (FY26); MF/Bank/FI holdings are negligible and shrinking. This is the inverse of a transition signal.
- No exit of a problematic family member: the family footprint expanded in FY26 with Dr. Vritika Gaddam's new paid advisory role.
- No governance overhaul: the auditor (PwC) is unchanged (already Big-4, so no upgrade available); no new independent directors were added in FY26; two independent-director/WTD exits were natural term completions, not a deliberate refresh with stronger appointees disclosed.
- Pledge reduction: not applicable — pledge was already at 0% before this run's evidence window (historical 2009 pledge fully released well before the period reviewed), so there is no reduction trend to credit as recent transition evidence.
- **On the explanation for the promoter-category jump** (48.42% → 53.24%, +4.82pp / 41,69,120 shares): the evidence assembled points to a reclassification, not fresh acquisition — Vigilance Security Services Pvt Ltd's 41,69,120-share stake (4.83%) was newly classified into the SEBI ICDR "promoter group" definition during the period, an amount that reconciles almost exactly with the category-level increase. This is disclosed as the most probable explanation on the balance of evidence found, not as a certainty (the underlying SEBI shareholding-pattern filings that would show the category-by-category roll-forward were not in the corpus and could not be directly fetched — see SEARCH LOG). It is not creeping acquisition by the named individual promoters, whose holdings are unchanged to the share, and it is not a positive governance signal — reclassifying the ED-flagged entity's existing stake into the formal promoter group, rather than divesting from or curtailing dealings with it, is the opposite of transition evidence.

**transition_evidence: []**

### 6E. Final output card

```
PROMOTER QUALITY VERDICT: CONCERN (severe end of tier)
Decisive basis: Nov-2023 ED/IT search at company premises over a Rs 8 Cr
promoter-to-Vigilance-Security-Services transfer, unresolved as of this run;
the company has since made Vigilance Security Services a Rs 21 Cr lender and
a formally disclosed 4.83% promoter-group member. A signed FY26 statutory
annexure states "Nil" remuneration increase for the MD/JMD while the AR's
own RPT note shows +58%/+107%. Chairman is a sitting Telangana Cabinet
Minister (Factories, Mines & Geology) overlapping the company's own
regulatory domain.
Mitigants: 0% promoter pledge; Big-4 auditor with clean, continuous
opinions; genuinely credentialed independent directors; HCA arbitration
award upheld on the merits through the Supreme Court; decent employee
sentiment; no SEBI action, no conviction, no confirmed asset attachment.
Transition evidence: NONE FOUND (institutional ownership is shrinking, the
family footprint is expanding, and the flagged RPT entity's ties have
deepened, not reduced).
Operator action recommended: independently verify current status of the
ED/PMLA matter (a fast-moving fact pattern this pipeline cannot track
live) before any position-sizing decision; treat the RPT web around
Vigilance Security Services as the single highest-priority verification
item carried forward from this stage.
```

---

## SEARCH LOG

**searches_performed** (representative list; all executed via WebSearch, several cross-checked with WebFetch where not blocked):
1. Visaka Industries promoter shareholding pattern 2026 BSE NSE
2. Visaka Industries promoter pledge shares
3. Visaka Industries Arudra Roofings Private Limited
4. Visaka Industries Vigilance Security Services Private Limited
5. Sreenidi Deccan FC owner Gaddam Visaka
6. "Visaka Industries" "Vigilance Security Services" promoter group Regulation 2(pp)
7. Visaka Industries Arudra Roofings promoter group Gaddam family
8. Visaka Industries Abinash Mishra CEO resigned August 2025
9. Visaka Industries land sale exceptional gain FY26 crore
10. Visaka Industries Vivek Venkatswamy Gaddam political FICCI CII chairman
11. Visaka Industries SEBI order adjudication
12. Visaka Industries Glassdoor AmbitionBox employee reviews
13. Visaka Industries Joginapalli Pruthvidhar Rao COO exit
14. "Visaka Industries" IiAS OR InGovern OR SES proxy advisory
15. G Vivekanand Telangana Cabinet Minister Labour Employment Factories Mines Congress 2024
16. Vivek Venkata Swamy Peddapalli MP BJP Congress switch
17. G Vivekanand Chennur MLA criminal cases affidavit assets
18. "Vivek Venkatswamy" controversy corruption land allotment Telangana
19. Visaka Industries Sreenidi Deccan Football Club sponsorship Gaddam Vamsi
20. "V6 channel" Vivek Venkatswamy ED case owner media
21. Yeshwant Realtors foreign national shareholder Vigilance Security FEMA
22. Gaddam Vivekanand ED case attachment PMLA 2025 2026
23. Visaka Industries stock exchange disclosure IT ED raid November 2023 material event
24. Gaddam Vivekanand ED case latest news 2026
25. Visaka Industries asbestos health litigation NGT ban
26. Visaka Industries NCLT oppression mismanagement family dispute
27. Visaka Industries short seller report activist investor
28. "Vritika Gaddam" Visaka Industries education background
29. Visaka Industries CFO Shafiulla Company Secretary Ramakanth tenure years
30. Supreme Court Visaka Industries 25.92 crore arbitration case ruling
31. G Vivekanand HCA arbitration award misappropriation allegations reject
32. ED FEMA case Gaddam Vivekanand Visaka Industries Rs 8 crore vigilance security 2023

**searches_skipped** (WebFetch attempts blocked by the container's egress proxy; EGRESS_BLOCKED returned for each domain — relied on WebSearch snippets of these pages instead, marked 📰/❓ accordingly, not ✅):
1. nsearchives.nseindia.com (NSE insider-trading/promoter-group disclosure — primary source for the Vigilance Security Services promoter-group reclassification)
2. bsmedia.business-standard.com (BSE announcement PDF, 04-Sep-2025, Chief Promoter declaration)
3. scanx.trade (multiple articles — FY26 non-encumbrance declaration, FY26 results, ED tax-order coverage)
4. trendlyne.com (shareholding-pattern trend page)
5. www.screener.in (shareholding-pattern quarterly trend, consolidated page)
6. telanganatoday.com (G Vivekanand's direct rebuttal statement on the HCA misappropriation allegation)

Status is **partial** because of these six skipped direct-source fetches, even though WebSearch summaries provided substitute (lower-tier) evidence for each. Where a finding rests only on a skipped-domain's search-engine summary, it is marked 📰 or ❓ in the body text above, never ✅.

---

```yaml
stage: B08-promoter
company: "VISAKAIND"
run_date: "2026-09-05"
model: claude-sonnet-5
status: partial               # 6 WebFetch attempts blocked by egress proxy (see searches_skipped)
input_gaps:
  - "inputs/announcements/ empty: no documented-action/exchange-filing corpus; relied on web search"
  - "inputs/shareholding/ empty: no quarterly SEBI shareholding pattern in corpus; relied on web search"
  - "results absent (carried from B00)"
  - "rating rationale absent (carried from B00)"
  - "research absent (carried from B00)"
  - "main concalls stale, newest Q1 FY24 Aug-2023 (carried from B00)"
  - "presentation stale (carried from B00)"
  - "only 1 of 3 peers has transcripts (carried from B00)"
  - "no primary ED/PMLA order located; case status as of run date is NOT FOUND (media reporting only, no chargesheet/attachment/closure confirmed)"
  - "SEBI shareholding-pattern filings (category-level roll-forward) not directly fetchable; promoter-category reconciliation rests on search-snippet evidence, not a primary filing read"
flags:
  - type: FLAG-PROMOTER
    verdict: "CONCERN"
    top_findings:
      - "Nov-2023 ED/IT search (FEMA/PMLA) at Visaka Industries' own Begumpet office and the Chairman's residences, over an Rs 8 Cr transfer from the Chairman's personal account to Vigilance Security Services Pvt Ltd; unresolved as of this run, no confirmed chargesheet/attachment/closure found"
      - "Vigilance Security Services Pvt Ltd (the entity named in the ED probe) has since been deepened as a related party: disclosed as RPT from 7-Dec-2023 (16 days post-raid), extended a Rs 21.00 Cr ICD facility to Visaka in FY26 at 8% p.a. (Rs 5.25 Cr outstanding), and was formally reclassified into the SEBI ICDR promoter group in FY26 (41,69,120 shares, 4.83%) -- an amount that reconciles almost exactly with the AR's unexplained +4.82pp promoter-category jump (48.42% to 53.24%)"
      - "FY26 statutory Rule 5(1) remuneration annexure, signed by the Chairman, states 'Nil' / 'no increase' in Executive Director remuneration, while the AR's own Note 40 shows the MD's and JMD's remuneration rising 58% and 107% respectively, coincident with a Rs 59.70 Cr exceptional land-sale gain"
      - "Chairman Dr. G. Vivek Venkatswamy Gaddam is concurrently a sitting Telangana Cabinet Minister for Labour, Employment Training & Factories, Mines & Geology (since 8-Jun-2025), a portfolio directly overlapping the company's own regulatory environment; undisclosed in the AR board-composition table; documented six-party-switch, 14-year political history"
      - "Recurring same-year round-trip promoter loans to the company (Rs 13 Cr FY24, Rs 13.03 Cr FY26) with no disclosed economic rationale; Rs 7.00 Cr of ICDs to two undisclosed-related counterparties (Bhagyanagar Hotels, Galvanizz Projects) fully written off in FY26; a Rs 6.00 Cr ICD at an anomalous 18% p.a. to a football club with no disclosed business rationale"
      - "Outside CEO hire (Abinash Mishra, strong external credentials) resigned after ~4 months citing personal reasons, during the same window as the intensified RPT activity"
verdict: "CONCERN"
scorecard: {clean: 2, caution: 3, red: 5}
deal_breakers: []             # recorded, never enforced here; PMLA-cited search occurred (21-Nov-2023) but no
                               # confirmed asset attachment found -- treat as UNRESOLVED, not cleared
adverse_findings:
  - {finding: "Nov-2023 ED/IT search under FEMA/PMLA at Visaka Industries' Begumpet office and Chairman's residences, over Rs 8 Cr transfer to Vigilance Security Services Pvt Ltd; unresolved", evidence_tier: "MEDIA REPORTED", source: "Deccan Chronicle, Deccan Herald, The Federal, NewsMeter, The South First, TaxScan, Siasat, IANS (cross-corroborated)", date: "2023-11-21 (reported); status as of 2026-09-05 unresolved"}
  - {finding: "Vigilance Security Services Pvt Ltd reclassified into SEBI ICDR promoter group in FY26, holding 41,69,120 shares (4.83%), reconciling with the promoter-category jump from 48.42% to 53.24%", evidence_tier: "MEDIA/EXCHANGE REPORTED", source: "NSE corporate disclosure (nsearchives.nseindia.com, fetch blocked -- via search snippet)", date: "on/around 2026-06-09"}
  - {finding: "Rule 5(1) statutory annexure states 'Nil' remuneration increase for MD and JMD while Note 40 shows +58% and +107% respectively", evidence_tier: "VERIFIED", source: "AR FY26 p.97 (Annexure-6) vs AR FY26 p.201 (Note 40)", date: "AR signed 2026-05-18"}
  - {finding: "Chairman is concurrently a sitting Telangana Cabinet Minister for Labour, Employment Training & Factories, Mines & Geology, portfolio overlapping the company's regulatory environment; not disclosed in AR board bios", evidence_tier: "VERIFIED", source: "Wikipedia 'G. Vivekanand' cross-checked against Revanth Reddy ministry list", date: "in office since 2025-06-08"}
  - {finding: "Recurring same-year round-trip promoter loans: Rs 13 Cr (FY24, Chairman + MD), Rs 13.03 Cr (FY26, Chairman alone), no disclosed rationale", evidence_tier: "VERIFIED", source: "AR FY25 p.187 and AR FY26 p.204, Note 40", date: "FY24 and FY26"}
  - {finding: "Rs 7.00 Cr ICDs to Bhagyanagar Hotels and Galvanizz Projects Private Limited (not disclosed as related parties) fully provided for / written off in FY26", evidence_tier: "VERIFIED", source: "AR FY26 p.179 (Note 12), pp.150-151 (CARO iii)", date: "FY26"}
  - {finding: "Rs 6.00 Cr ICD to Sreenidi-Deccan Football Club Private Limited at an anomalous 18% p.a., no disclosed business rationale; no confirmed promoter ownership link to the club established", evidence_tier: "VERIFIED (transaction) / UNVERIFIED (ownership link)", source: "AR FY26 p.179, Note 12; web search found club attributed to 'Sreenidhi Group', link to Gaddam family not confirmed", date: "FY26"}
  - {finding: "Vigilance Security Services only disclosed as a Companies Act related party w.e.f. 7-Dec-2023, 16 days after the ED/IT raid publicly named it", evidence_tier: "VERIFIED", source: "AR FY25 Note 40 (effective-date footnote)", date: "2023-12-07"}
  - {finding: "Outside CEO Abinash Mishra (IIT Bombay, Olin Business School, 27 yrs experience) resigned after ~4 months, 'personal reasons'", evidence_tier: "VERIFIED", source: "AR FY26 p.76 Board's Report; corroborated by MarketScreener/TradingView news", date: "2025-08-22"}
  - {finding: "HCA arbitration self-dealing optics: Chairman was a former HCA president whose own company (Visaka) won a Rs 25.92 Cr (now ~Rs 68.73 Cr) arbitral award against HCA, upheld through the Supreme Court (6-Oct-2025); TDCA sought a BCCI probe and Chairman publicly denied misappropriation allegations", evidence_tier: "MEDIA REPORTED", source: "Telangana Today, Deccan Chronicle, scanx.trade", date: "award 2016; SC dismissal 2025-10-06"}
  - {finding: "FPI holding fell from 0.45% (FY25) to 0.10% (FY26); institutional ownership shrinking, not entering", evidence_tier: "VERIFIED", source: "AR FY25 p.117 and AR FY26 p.132, Categories of Shareholders", date: "31-Mar-2025 vs 31-Mar-2026"}
  - {finding: "VIL Media Private Limited (promoter-family media entity, plausibly linked to V6 News) received Rs 11.13 Cr (FY26) / Rs 11.93 Cr (FY25) in advertising fees from Visaka, no arm's-length benchmarking disclosed", evidence_tier: "VERIFIED (transaction) / UNVERIFIED (V6 News link)", source: "AR FY26 p.204, Note 40", date: "FY25 and FY26"}
transition_evidence: []       # NONE FOUND; institutional ownership shrank (FPI 0.45%->0.10%), family footprint
                               # expanded (new paid role for Chairman's daughter), and the ED-flagged RPT
                               # entity's ties deepened rather than reduced -- the opposite of transition evidence
pledge_pct_latest: 0
pledge_trend: "stable at zero. Historical 2009 pledge (G. Vivekanand 16.76 lakh shares/10.55%; Saroja Vivekanand 1.10 lakh shares/0.69%, per Business Standard 2009) fully released; a FY26 non-encumbrance declaration by the Chief Promoter, covering nine promoter entities, confirms zero pledge as of FY26 (media-reported, scanx.trade summary, direct filing fetch blocked)"
searches_performed:
  - "Visaka Industries promoter shareholding pattern 2026 BSE NSE"
  - "Visaka Industries promoter pledge shares"
  - "Visaka Industries Arudra Roofings Private Limited"
  - "Visaka Industries Vigilance Security Services Private Limited"
  - "Sreenidi Deccan FC owner Gaddam Visaka"
  - "Visaka Industries Vigilance Security Services promoter group Regulation 2(pp)"
  - "Visaka Industries Arudra Roofings promoter group Gaddam family"
  - "Visaka Industries Abinash Mishra CEO resigned August 2025"
  - "Visaka Industries land sale exceptional gain FY26 crore"
  - "Visaka Industries Vivek Venkatswamy Gaddam political FICCI CII chairman"
  - "Visaka Industries SEBI order adjudication"
  - "Visaka Industries Glassdoor AmbitionBox employee reviews"
  - "Visaka Industries Joginapalli Pruthvidhar Rao COO exit"
  - "Visaka Industries IiAS OR InGovern OR SES proxy advisory"
  - "G Vivekanand Telangana Cabinet Minister Labour Employment Factories Mines Congress 2024"
  - "Vivek Venkata Swamy Peddapalli MP BJP Congress switch"
  - "G Vivekanand Chennur MLA criminal cases affidavit assets"
  - "Vivek Venkatswamy controversy corruption land allotment Telangana"
  - "Visaka Industries Sreenidi Deccan Football Club sponsorship Gaddam Vamsi"
  - "V6 channel Vivek Venkatswamy ED case owner media"
  - "Yeshwant Realtors foreign national shareholder Vigilance Security FEMA"
  - "Gaddam Vivekanand ED case attachment PMLA 2025 2026"
  - "Visaka Industries stock exchange disclosure IT ED raid November 2023 material event"
  - "Gaddam Vivekanand ED case latest news 2026"
  - "Visaka Industries asbestos health litigation NGT ban"
  - "Visaka Industries NCLT oppression mismanagement family dispute"
  - "Visaka Industries short seller report activist investor"
  - "Vritika Gaddam Visaka Industries education background"
  - "Visaka Industries CFO Shafiulla Company Secretary Ramakanth tenure years"
  - "Supreme Court Visaka Industries 25.92 crore arbitration case ruling"
  - "G Vivekanand HCA arbitration award misappropriation allegations reject"
  - "ED FEMA case Gaddam Vivekanand Visaka Industries Rs 8 crore vigilance security 2023"
searches_skipped:
  - "WebFetch nsearchives.nseindia.com -- EGRESS_BLOCKED (NSE promoter-group disclosure primary source)"
  - "WebFetch bsmedia.business-standard.com -- EGRESS_BLOCKED (BSE Chief Promoter declaration PDF)"
  - "WebFetch scanx.trade -- EGRESS_BLOCKED (FY26 non-encumbrance declaration and results articles)"
  - "WebFetch trendlyne.com -- EGRESS_BLOCKED (shareholding-pattern trend page)"
  - "WebFetch www.screener.in -- EGRESS_BLOCKED (shareholding-pattern quarterly trend)"
  - "WebFetch telanganatoday.com -- EGRESS_BLOCKED (Chairman's direct rebuttal statement on HCA allegation)"
verdict_basis: "Unresolved Nov-2023 ED/IT (FEMA/PMLA) search at the company's own premises over promoter-to-Vigilance-Security-Services fund transfers, compounded by the company deepening ties with that same flagged entity in FY26 (as an 8% lender and as a newly reclassified 4.83% promoter-group member) rather than curtailing them, alongside a signed statutory annexure that misstates a 58%/107% executive remuneration increase as 'Nil'."
analyst_note: "The ED/PMLA matter is a live, fast-moving fact pattern this container cannot verify beyond Nov-2023 media reports; no primary ED order, chargesheet, or closure was locatable, so its current status is genuinely NOT FOUND rather than resolved either way -- flag this explicitly to the operator as the top verification priority carried forward, alongside independent confirmation of the Vigilance Security Services promoter-group filing (direct NSE/BSE fetch was blocked here). The Rule 5(1) remuneration misstatement is the one finding in this report that required no web search at all -- it is a straight internal contradiction inside the FY26 AR between Annexure-6 and Note 40, and should be checked against the signed original rather than dismissed as an extraction error."
```
