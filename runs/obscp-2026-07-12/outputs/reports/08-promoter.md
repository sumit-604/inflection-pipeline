# Stage 8 — Promoter & Management Background Check
## OBSC Perfection Limited (NSE: OBSCP) | CIN L27100DL2017PLC314606
Run date: 2026-07-12 | Model: claude-sonnet-5 | Status: **PARTIAL** (see Search Log)

---

### PREFATORY NOTE ON SOURCE MATERIAL

Two independent input problems shaped this report and are recorded here rather than
buried in footnotes:

1. **AR file defect.** `runs/obscp-2026-07-12/inputs/annual-report/Annual_Report_2025.pdf`
   has a genuine font-encoding corruption on pages 2-59 (cover letter on p.1 is fine).
   This is not an extraction artifact of this tool — every element on those pages
   (headings, body text, tables) renders as scrambled glyphs, confirmed across three
   separate page-range reads (pp.1-15, 16-30, 31-45, 46-59). This range covers the
   **Board's Report, MGT-9 extract, Corporate Governance Report, and the detailed
   Related Party Transactions schedule** — none of it could be read. Pages 60-77
   (Independent Auditor's Report, CARO Annexure A/B, Balance Sheet, P&L, Cash Flow,
   Notes 1-5) render cleanly and were read in full. Pages 78-101 are separately
   confirmed blank/truncated per the run brief. Net effect: the AR could not supply
   family-tree, board-composition, or RPT-quantum detail; it did supply audited
   financials, the auditor's unqualified opinion, and the true list of directors who
   signed the FY25 accounts (which turned out to differ from the promoter name
   supplied in the task brief — see Section 1).
2. **WebFetch blocked (HTTP 403) on 10 of 12 attempted document fetches**, including
   both the DRHP and RHP (NSE archives and obscperfection.com and a broker mirror),
   screener.in, zaubacorp.com, Glassdoor, the CARE ratings PDF, and SEBI's filings
   page. WebSearch (which aggregates and quotes these same sources) remained
   available throughout and is the basis for most findings below; direct primary-text
   confirmation of a few items (DRHP litigation section, exact RPT rupee values,
   Glassdoor rating) was not possible this run. Each such gap is marked NOT FOUND.

---

## SECTION 1: PROMOTER IDENTITY & FAMILY MAPPING

**Correction to task brief:** the brief's injected promoter identity ("Narang family,
Asha Narang as key signatory") describes only one node of a materially larger,
multi-family promoter group. The FY25 audited financial statements (Balance Sheet,
P&L, signed 16 May 2025) are signed by **Saksham Lekha (Managing Director, DIN
07389575)**, **Ashwani Lekha (Director, DIN 07389860)**, **Sanjeev Verma (CFO/Director,
DIN 00296825)**, and **Mudit Johri (Company Secretary, ACS 67471)** — not by Asha
Narang, who instead signs routine exchange correspondence in her capacity as
**Non-Executive Director and Chairperson** (✅ VERIFIED — AR p.1 cover letter and FY25
Balance Sheet/P&L signature blocks, Annual_Report_2025.pdf; corroborated 📰 by
multiple director-registry aggregators for board-title attribution).

### 1A. Family tree, roles, tenure, holdings, other directorships

| Name | DIN | Role at OBSCP | Other directorships found |
|---|---|---|---|
| Asha Narang | 00296714 | Non-Exec Director & Chairperson | Widow/successor of Omega Bright Steel founder Satya Pal Narang; director in ~10 companies per aggregator count (exact list NOT FOUND) |
| Saksham Leekha | 07389575 | Managing Director | Akshat Alloys Private Limited (active, Delhi, basic-iron-&-steel manufacture) |
| Ashwani Leekha | 07389860 | Executive Director | Akshat Alloys Private Limited (active) |
| Sanjeev Verma | 00296825 | CFO & Director | NOT FOUND (no other directorships surfaced) |
| Rajni Verma | NOT FOUND | Promoter (individual, non-board) | NOT FOUND |
| Sandeep Narang | NOT FOUND | Promoter (individual, non-board) | NOT FOUND |
| Mudit Johri | ACS 67471 | Company Secretary (KMP, not promoter) | — |
| Ravikumar R. Khandelwal | NOT FOUND | Independent Non-Exec Director (pre-existing) | NOT FOUND |
| Pradeep Harikishan Chabra | NOT FOUND | Independent Non-Exec Director (pre-existing) | NOT FOUND |
| Saurabh Priya Singh | NOT FOUND | Independent Non-Exec Director (appointed via postal ballot, effective ~31 Mar 2026) | NOT FOUND |
| Mohit Bhardwaj | NOT FOUND | Additional Non-Exec Independent Director (effective ~27 May 2026, pending shareholder approval) | NOT FOUND |

Exact family relationships between the Leekha/Narang/Verma individuals (e.g., is
Ashwani Leekha married into the Narang family; is Sandeep Narang Asha Narang's son;
is Rajni Verma Sanjeev Verma's spouse) were **not independently confirmable** from
public sources this run — flagged as ❓ UNVERIFIED, not asserted as fact. What is
independently confirmed: DIN registries and IPO-era shareholding disclosures group
all of them as "promoters" of OBSC Perfection Limited (📰 multiple aggregator sources
cross-checked: thecompanycheck.com, scanx.trade, choiceindia.com).

An extended promoter-group list (from shareholding disclosures aggregated by search)
also names **Anupma Leekha, Baldev Raj Leekha, Uma Chhabra, Aarshi Jaggi**, and other
Leekha/Vohra/Jain/Verma-surnamed individuals — consistent with a large,
multi-generation, intermarried family shareholding pool rather than a two-person
promoter pair. This is a wide promoter headcount for a ~₹220 crore-revenue company
(1B red-flag test: "entity/individual count disproportionate to business size") —
noted as a CAUTION item, not a red flag, since the underlying business (Omega Bright
Steel) has a genuine 45-year operating history that plausibly accumulated this many
family shareholders organically.

### 1B. Promoter group entities

| Entity | Status | Role |
|---|---|---|
| Omega Bright Steel & Components Private Limited | ✅ Active, credit-rated (CARE/India Ratings history found) | Promoter group's core operating business; OBSCP's primary raw-material (bright-bar steel) supplier |
| Omega Bright Steel Private Limited | ✅ Active | Sold cold-forging assets to OBSCP in Nov 2025 (related-party transaction, see 3A) |
| Akshat Alloys Private Limited | ✅ Active (CIN U27107DL2008PTC178156, inc. 2008) | Leekha-family-controlled basic iron & steel manufacturer, Delhi. Not confirmed as formally listed in OBSCP's disclosed promoter-group entity list — flag for operator to confirm no undisclosed potential-competing entity |
| ESS U Enterprises Private Limited | Listed as promoter in shareholding filings | Nature of business NOT FOUND |
| Bluwat AG | ✅ Active, Swiss entity (Zug), issued LEI | Listed as promoter alongside individuals Richard, Adrianne, Pascal and Simon Blum; exact role (technical JV partner vs. legacy shareholder) NOT FOUND |

No struck-off, dormant, or opaque-jurisdiction entities were identified among the
named promoter-group companies in this search round (Switzerland/Bluwat AG is a
disclosed, LEI-registered, non-opaque jurisdiction). This is a genuine clean finding,
not an omission — but it rests on aggregator data, not an exhaustive MCA/RoC search
of every individual promoter's full directorship list, so treat as directional.

### 1C. Education and professional background

- **Asha Narang**: no formal education record found; professional record is
  well-documented — she has run Omega Bright Steel since ~1972 after her husband and
  company founder Satya Pal Narang fell ill, cited as one of India's first women
  entrepreneurs in the (male-dominated) steel industry (📰 MEDIA REPORTED /
  company-sourced, omegabrightsteel.com "Leadership" page, undated but consistent
  across sources). This is a positive, verifiable reputational anchor.
- **Saksham Leekha**: aggregator bios cite a BTech in Mechanical Engineering with an
  attribution ("Delhi Public School, Dwarka, 2014-2017") that is internally
  inconsistent — a school is cited as if it conferred an engineering degree. Treated
  as ❓ UNVERIFIED / low-confidence data-scrape artifact, not a fact.
- **Ashwani Leekha, Sanjeev Verma, Rajni Verma, Sandeep Narang**: no independently
  verifiable education or pre-OBSCP professional history found. NOT FOUND.

### 1D. History before the current company

OBSC Perfection Limited (incorporated 17 March 2017) is best read as a
**backward-integrated downstream extension of the Narang family's Omega Bright Steel
business** (bright-bar steel manufacturing since 1971) rather than a standalone
first-generation startup. The Leekha family runs day-to-day operations (Saksham
Leekha as MD) while the Narang matriarch holds the non-executive Chair — this reads
as an **in-progress, apparently orderly generational handoff** already substantially
executed (not an unresolved succession dispute; no dispute evidence found either way).
No unexplained career gaps or founder/inheritor conflict signals were found.

---

## SECTION 2: LEGAL & REGULATORY RECORD

**2A. SEBI actions**: No SEBI adjudication orders, SAT appeals, insider-trading
proceedings, LODR non-compliance penalties, market bans, or consent orders were found
against the company or any named promoter/director. SEBI's public-filings index page
for the company's IPO was located but its content (observation letter, if any) could
not be retrieved (WebFetch blocked) — recorded as NOT FOUND, not asserted clean.

**2B. Criminal cases**: none found. Targeted searches on "Satya Pal Narang" and
"Sandeep Narang" litigation returned only unrelated namesake cases (e.g., Satya Pal
Anand v. State of M.P.), confirmed as non-matches on facts and parties.

**2C. Tax and revenue**: no IT search-and-seizure, undisclosed-income, transfer
pricing, benami, DRI, or SFIO references found for the company or promoters. The
FY25 statutory auditor's CARO report explicitly states: no benami proceedings
initiated or pending against the company; company not declared a wilful defaulter by
any bank/FI; no fraud by or on the company noticed or reported during the year (✅
VERIFIED — P.K. Chand & Co., Annexure A to Auditor's Report, dated 16 May 2025).

**2D. Other regulators**: no RBI, IRDAI, TRAI, MCA-compounding/disqualification,
NCLT oppression-petition, CCI, or NGT matters found for the company or promoters.

**2E. Civil litigation**: the company's DRHP/RHP contains a standard "Outstanding
Litigation and Material Developments" section (indexed at p.235 in one aggregator's
table of contents) whose actual content **could not be retrieved** — every attempted
fetch of the DRHP/RHP PDF (NSE archives, obscperfection.com, and a broker mirror)
returned HTTP 403. This is recorded as **NOT FOUND, explicitly not "clean,"** since
the section was never read. This is the single largest evidence gap in Section 2.

**2F. Legal red-flag summary table**

| Sub-area | Finding |
|---|---|
| SEBI | Clean (search-based); observation letter unread |
| Criminal | Clean |
| Tax/revenue | Clean (auditor-confirmed) |
| Other regulators | Clean |
| Civil litigation | **NOT FOUND — DRHP section unread** |

Overall Section 2 read: no adverse findings surfaced anywhere searches reached, but
confidence is medium rather than high because the one section purpose-built to
disclose litigation (DRHP p.235) was inaccessible this run.

---

## SECTION 3: BUSINESS CONDUCT & ETHICAL TRACK RECORD

**3A. RPT history**: OBSC Perfection's primary raw material (high/low-carbon steel
bright bars) is sourced from **Omega Bright Steel & Components Private Limited**, a
disclosed promoter-group entity and, per the company's own investor materials, a
"strategically co-located" primary supplier (📰 VERIFIED via multiple aggregator
citations of company disclosures). In **November 2025**, OBSC Perfection announced
the acquisition of cold-forging assets (₹12.45 crore, ~6,000 TPA incremental
capacity, Sector 69 IMT Faridabad) from **Omega Bright Steel Private Limited** — the
company's own investor release explicitly frames this as a related-party transaction
(source: NSE corporate filing "OBSCP Forging Machinery Acquisition Investor
Release," 15 Nov 2025; content summary via WebSearch, primary PDF not retrieved).
Whether an independent valuer/fairness opinion was obtained for this RPT, and the
exact FY25 rupee quantum and pricing basis of the ongoing raw-material RPT, are
**NOT FOUND** — the AR's RPT schedule sits in the unreadable page range (2-59) and/or
the truncated range (78-101). The company's own RHP discloses, as a risk factor, that
**it has not entered into non-compete agreements with its promoters or promoter-group
entities** — a self-disclosed structural risk given Akshat Alloys (Leekha-controlled
steel manufacturer) and the Omega Bright Steel entities operate in adjacent segments
of the same value chain. This combination (structural RPT dependency for a critical
input + a recent RP asset purchase + no non-compete cover) is the most significant
governance watch-item in this report, though nothing found indicates unfair pricing
or minority harm — it is a structural exposure, not a proven abuse.

**3B. Capital allocation behaviour**: FY25 cash-flow statement shows a ₹5,715.92 lakh
increase in share capital & premium, consistent with the October 2024 IPO (₹66 crore
raised) rather than a promoter-favouring preferential allotment. No dividend was paid
in FY25; profit was retained to fund a new Chakan Unit IV and the cold-forging
acquisition — a reasonable capital-allocation pattern for a growth-stage manufacturer,
not evidence of cash hoarding alongside high promoter salary (promoter salary data:
NOT FOUND). No warrant-lapse or value-destructive-acquisition pattern found.

**3C. Promoter share transactions**: Promoter shareholding stood at **73.48%** as of
the most recent disclosure found (January 2026). The company's Regulation 31(4)
disclosure explicitly states the promoter group **created no new encumbrances on its
shares during FY26** (✅ VERIFIED, NSE filing, referenced via WebSearch). No pledge
was found at any point since listing. No creeping-acquisition or suspicious
pre-announcement trading pattern surfaced in available sources.

**3D. Minority treatment**: No proxy-advisory (IiAS/SES/InGovern) report specific to
OBSC Perfection was found — unsurprising for a company only ~18 months past its SME
listing and likely below most proxy advisors' coverage thresholds; this is a coverage
gap, not a clean finding. No AGM controversy reported. SEBI SCORES complaint data was
not directly queryable with the tools available this run — **NOT FOUND**, not
asserted clean.

**3E. Auditor relationship**: **P.K. Chand & Co., Chartered Accountants** (FRN
512371C; signing partner Prashant Kumar Chand, M.No. 091046), based in Noida,
established 1993. FY25 opinion (dated 16 May 2025) is **unmodified/unqualified**, no
key-audit-matters flagged (not required for an unlisted-at-audit-date company under
SA 701 — note: opinion letter is dated before the company's status changes were
fully reflected; audit relates to the company as OBSC Perfection Ltd, erstwhile OBSC
Perfection Pvt Ltd). CARO report explicitly confirms **no resignation of the
statutory auditor during the year** (✅ VERIFIED). One minor, non-qualifying
observation: the auditor noted certain accounting vouchers were amended without full
compliance with the mandatory audit-trail (edit-log) feature, attributed by the
auditor to accounting staff being unfamiliar with the software rather than to fraud
or concealment — a common, immaterial finding across many FY25 Indian company audits
following the MCA's audit-trail mandate, not scored as a red flag here. No
whistleblower complaints were received by the auditor during the year (per CARO), no
restatement, and no evidence of non-audit-fee dominance was found.

---

## SECTION 4: REPUTATION & PUBLIC PERCEPTION

**4A. Media reputation**: Coverage located is almost entirely IPO-listing and
quarterly-results reporting from financial-news aggregators (scanx.trade,
businesstoday.in, marketsmojo.com etc.), with no adverse investigative journalism
found. The most recent analyst commentary (MarketsMojo, 20 May 2026) rates the stock
"Hold" on **valuation** grounds (price near-doubling against earnings growth), not
promoter-quality grounds.

**4B. Employee reputation**: A Glassdoor company page exists for OBSC Perfection but
its rating/review-count content could not be retrieved (WebFetch blocked); an
AmbitionBox-specific rating was not retrieved either. **NOT FOUND**, not asserted
clean or adverse.

**4C. Investor and analyst perception**: No activist campaigns or short-seller
reports found. **CRISIL assigned CRISIL BBB+/Stable** to the company's bank
facilities (Cash Credit ₹45.25 cr, Term Loan ₹33.08 cr, proposed fund-based limits
₹21.67 cr) on 3 July 2026 (✅ VERIFIED, CRISIL rating rationale) — an investment-grade,
independently validated credit opinion, a positive institutional-credibility signal.

**4D. Political and government connections**: none found (no donations, land
allotments, or contract-favour signals surfaced in search).

**4E. Industry peer reputation**: Omega Bright Steel is described across trade
sources as a north-Indian leader in bright-bar steel manufacturing with a 45-year
operating history and relationships with 700+ automotive ancillary units — a credible
industrial reputation that underpins OBSC Perfection's own credibility as a
backward-integrated precision-component supplier to OEMs including ZF Group, Tenneco
Inc., and JTEKT (📰 company/investor-presentation sourced, cross-referenced across
multiple independent aggregators).

**4F. Philanthropy**: FY25 CSR spend of ₹18.04 lakh (per CARO report, matching the
statutory Section 135(5) requirement) was routed through **Swachh Paryavaran Trust**,
an independent, Delhi-based environmental trust with no evidence found linking it to
the promoter family — appears to be an arm's-length CSR implementing partner, not a
related-party CSR vehicle. CSR spend sits at the statutory minimum, not "beyond
mandatory" — a neutral rather than a positive signal.

---

## SECTION 5: CXO & BOARD QUALITY

**5A. CXO turnover (5 years)**: No CFO resignation found — Sanjeev Verma signed the
FY25 accounts as CFO/Director without any noted change. No Company Secretary
resignation found — Mudit Johri (ACS 67471) signed the FY25 accounts and remains in
role per the most recent filings found. **No independent-director mid-term exit was
found.** To the contrary, the board **added** two independent directors in 2026:
Saurabh Priya Singh (effective ~31 March 2026, via postal ballot) and Mohit Bhardwaj
(Additional Non-Executive Independent Director, effective ~27 May 2026, subject to
shareholder approval), alongside the pre-existing independent directors Ravikumar
Ramniranjan Khandelwal and Pradeep Harikishan Chabra — this is board **expansion**,
not attrition (✅ VERIFIED via NSE corporate announcements referenced in search
results).

**5B. Board quality**: The board combines family executives (Saksham Leekha – MD;
Ashwani Leekha – Executive Director; Sanjeev Verma – CFO/Director) with a
family non-executive Chairperson (Asha Narang) and, post-expansion, four independent
directors. Cross-membership with a promoter entity exists and is structural, not
concealed: Saksham and Ashwani Leekha also direct Akshat Alloys Private Limited.
Audit-committee composition and whether it includes a designated financial expert
could not be confirmed — **NOT FOUND** (AR governance pages unreadable).

**5C. Key-person risk and succession visibility**: **High but visible, not opaque.**
Saksham Leekha, a young next-generation promoter, holds hands-on operational control
as MD, and the company's core input supply chain runs structurally through
promoter-controlled Omega Bright Steel. The generational handoff from the
Narang founding generation to the Leekha operating generation appears
substantially complete and orderly (Narang matriarch retained as non-executive
Chair rather than removed), which mitigates — but does not eliminate — the
concentration risk of a single young MD holding both operational control and a
critical related-party supply relationship.

---

## SECTION 6: PROMOTER QUALITY VERDICT

### 6A. Scorecard (10 dimensions, rated strictly on Sections 1-5 findings)

| # | Dimension | Rating | Basis |
|---|---|---|---|
| 1 | Family/ownership transparency | ✅ | Family tree substantially mapped; some pairwise relationships unconfirmed |
| 2 | Promoter-group entity quality (no shells/struck-off) | ✅ | All named entities active/operating; not exhaustively MCA-verified |
| 3 | Education/background verifiability | ⚠️ | Thin/single-source or internally inconsistent bios for several individuals |
| 4 | SEBI/regulatory record | ✅ | Clean across searched sources; observation letter unread |
| 5 | Criminal/tax record | ✅ | Clean; auditor-confirmed no benami/fraud/wilful-default |
| 6 | Civil litigation | ⚠️ | DRHP litigation section (p.235) not retrieved — genuine gap, not confirmed clean |
| 7 | RPT conduct | ⚠️ | Structural raw-material RPT + recent RP asset purchase + no non-compete cover; pricing fairness unverified |
| 8 | Capital allocation / dilution / pledge | ✅ | Zero pledge, IPO-funded growth, no adverse dilution pattern |
| 9 | Auditor/board stability | ✅ | No auditor, CFO, or CS resignation; board being strengthened |
| 10 | Reputation (media/employee/investor) | ⚠️ | No adverse media, but employee-sentiment data unread; institutional ownership thin (2.94%) |

**scorecard: clean 6, caution 4, red 0**

### 6B. Classification

**CAUTION.** No red flags were found anywhere this run's searches reached: no SEBI
action, no criminal or tax matter, no pledge, no auditor or CFO/CS resignation, and
the board is actively adding independent directors rather than losing them. That
would ordinarily support TRUSTWORTHY. The classification is held at CAUTION instead
because four of ten scorecard dimensions rest on **genuine evidence gaps rather than
confirmed-clean findings** — the DRHP litigation section, the AR's detailed RPT
schedule, and employee-sentiment data were all inaccessible this run — combined with
a real, structural related-party dependency (promoter-controlled raw-material supply,
no non-compete agreement, a recent related-party asset purchase) that has not been
shown to be mispriced but has also not been shown to be fairly priced.

### 6C. Deal-breaker checks (recorded, not enforced)

None triggered: no SEBI market ban; no economic-offence conviction; no live SFIO;
no PMLA with attached assets; no auditor resignation within 3 years; pledge is 0%
(well under the 40% threshold); no multiple mid-term independent-director exits
(board is adding, not losing, independent directors); no restatement found.

### 6D. TRANSITION EVIDENCE SCAN

- **Governance overhaul in progress**: two new independent directors added in 2026
  (Saurabh Priya Singh, effective ~31 Mar 2026; Mohit Bhardwaj, effective ~27 May
  2026), expanding the independent bench from 2 to 4 — source: NSE corporate
  announcements, 2026.
- **New independent credit validation**: CRISIL BBB+/Stable assigned 3 July 2026 —
  first third-party credit-rating anchor found for the company — source: CRISIL
  rating rationale.
- **Pledge discipline**: explicit "no new encumbrances" disclosure for FY26 under
  Reg 31(4) — source: NSE filing.
- **Public-market discipline newly introduced**: October 2024 IPO converted a
  wholly family-owned private company into a listed entity with 23.58% public float
  and 2.94% institutional float — a first step toward external scrutiny, though no
  named institutional investor of size has yet been identified (institutional
  entry itself is NOT a red flag per project convention; noted here only as a
  transition marker, not scored as a risk).

Not found: no exit of a problematic family member; no stake sale to a credible
strategic; no new professional (non-family) CEO/CFO brought in from outside the
family — the MD, Executive Director, and CFO roles remain family-held.

### 6E. Final output card

- **Company**: OBSC Perfection Limited (NSE: OBSCP)
- **Verdict**: CAUTION
- **Deal-breakers triggered**: none
- **Pledge**: 0%, stable/falling-to-zero since listing, no new encumbrances FY26
- **Transition evidence**: present (board expansion, new credit rating, no-pledge
  discipline) — this is a CAUTION with visible positive momentum, not a static
  CAUTION
- **Single largest unresolved item for the operator**: raw-material RPT dependency
  on promoter-controlled Omega Bright Steel, absent a non-compete agreement, layered
  with a recent related-party asset acquisition — pricing/fairness unverified this
  run; AR's own RPT schedule and the DRHP litigation section should be sourced
  cleanly (a non-corrupted AR copy, or direct DRHP/RHP access) before this verdict is
  finalized to TRUSTWORTHY or downgraded to CONCERN.

---

## SEARCH LOG

### searches_performed
1. OBSC Perfection Limited promoters Saksham Lekha Ashwani Lekha
2. OBSC Perfection Ltd IPO promoter shareholding pattern
3. OBSC Perfection Ltd SEBI order OR SAT OR NCLT OR litigation
4. "Saksham Leekha" OR "Saksham Lekha" OBSC Perfection background education career
5. "Ashwani Leekha" OR "Ashwani Lekha" director companies
6. "Omega Bright Steel" company OBSC Perfection
7. OBSC Perfection related party transactions royalty rent promoter entities annual report
8. "Asha Narang" "Sandeep Narang" OBSC Perfection director relationship
9. Bluwat AG Blum OBSC Perfection promoter
10. "Akshat Alloys Private Limited" Leekha
11. OBSC Perfection forging machinery acquisition Omega Bright Steel related party investor release
12. "Omega Bright Steel" Narang founder history bright bars Mandi Gobindgarh
13. OBSC Perfection Ltd IiAS OR proxy advisory OR SES governance
14. OBSC Perfection Ltd Glassdoor OR AmbitionBox employee reviews
15. "Ashwani Leekha" "Narang" relation family son-in-law OBSC
16. Bluwat AG Switzerland precision engineering OBSC Perfection technical partner
17. OBSC Perfection Ltd auditor change OR CFO resignation OR independent director resign
18. OBSC Perfection Ltd promoter pledge encumbrance shares
19. OBSC Perfection Ltd fraud OR scam OR concern OR short seller
20. "OBSC Perfection" institutional investor OR mutual fund stake entry 2025 2026
21. "OBSC Perfection" "Khandelwal" OR "Chabra" independent director resign OR cessation
22. OBSC Perfection Limited promoter group family tree Narang Leekha Verma stake percentage
23. OBSC Perfection Ltd credit rating CARE OR Acuite OR India Ratings 2025
24. "OBSC Perfection" "outstanding litigation" OR "no material litigation" DRHP
25. OBSC Perfection Limited GIDC Gujarat land OR government contract subsidy incentive
26. OBSC Perfection Limited investor complaints SCORES SEBI grievance
27. "OBSC Perfection" chittorgarh review promoter risk
28. "P K Chand & Co" auditor Noida chartered accountants track record
29. OBSC Perfection Limited board of directors independent directors list 2025
30. "Satya Pal Narang" OR "Sandeep Narang" litigation court case
31. "OBSC Perfection" AmbitionBox rating employees reviews
32. "Swachh Paryavaran Trust" CSR promoter related

### searches_skipped (WebFetch blocked HTTP 403 / tool errors; not attempted via WebSearch snippet substitution beyond what's above)
- DRHP PDF direct read: nsearchives.nseindia.com/emerge/corporates/content/OBSCPerfectionLimited_DRHP.pdf
- RHP PDF direct read: obscperfection.com/wp-content/uploads/2024/10/OBSC_RHP.pdf
- RHP mirror direct read: unistonecapital.com/wp-content/uploads/2024/10/OBSC_RHP.pdf
- screener.in/company/OBSCP/ (shareholding trend, quality flags)
- zaubacorp.com company/director pages (director cross-directorship detail)
- girishnotes.substack.com/p/obsc-perfection-limited (independent analyst notes)
- CARE Ratings PDF on Omega Bright Steel Private Limited
- glassdoor.co.in Working-at-OBSC-Perfection page (employee ratings)
- sebi.gov.in public-issue filing page for OBSC Perfection (observation letter)
- nsearchives.nseindia.com Investor Presentation / Outcome-of-Board-Meeting PDFs (board composition, family relationships)
- SEBI SCORES database — not directly queryable with tools available this run
- MCA/RoC direct filing search for exhaustive promoter-individual directorship lists — not directly queryable with tools available this run
