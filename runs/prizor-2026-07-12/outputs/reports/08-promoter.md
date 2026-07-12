# Stage 8 — Promoter Background Check
## Prizor Viztech Limited (NSE: PRIZOR, ISIN INE0V9N01017)
Run date: 2026-07-12 | Model: claude-sonnet-5

Sector note: the collection manifest tags this company "Pharma / CDMO." That is a
`collect_to_repo` metadata defect. Prizor Viztech is a video-surveillance /
security-electronics business (CCTV cameras, DVR/NVR, AI video, TVs, touch
panels), listed on NSE SME (main-board migration not yet confirmed) on
22 July 2024. This report treats it as such throughout.

Evidence taxonomy used below: ✅ VERIFIED (official source: AR, MCA/RoC-derived
registry aggregators, exchange filings) | 📰 MEDIA REPORTED | 💬 FORUM/SOCIAL |
❓ UNVERIFIED (single/dubious source).

---

## SECTION 1: PROMOTER IDENTITY & FAMILY MAPPING

### 1A. Family tree, roles, tenure, holdings, other directorships

The promoter group is a two-person team, surname Gauswami:

| Name | DIN | Role | Age (per AR, FY25) | Shareholding at 31-Mar-2025 |
|---|---|---|---|---|
| Ms. Mitali Dasharathbharthi Gauswami | 07712190 | Chairman & Managing Director | 35 | 48,30,000 shares / 45.18% |
| Mr. Dasharathbharthi Gopalbharthi Gauswami | 07712175 | Whole-Time Director & CFO | 34 | 24,69,968 shares / 23.10% |

Combined promoter + promoter group holding at FY25-end: 72,99,989 shares /
68.28% ✅ (Annual_Report_2025.txt, Related Party / Shareholding Pattern notes,
lines 3775–3781, 4362).

**DIN disambiguation (resolves the injected-input flag).** The AR text cache
contains several OCR-garbled lines that appear to drop "Mitali" and attach
DIN 07712190 to a bare "Dasharathbharthi Gauswami" (e.g. lines 195, 210). Cross-
checked against every clean occurrence in the same document — item-3/item-4
explanatory statements (lines 874, 993), audited-financials signature blocks
(lines 3429–3436, 4346–4368, 4921–4928) and the shareholding-pattern table
(lines 3775–3781) — the mapping is unambiguous and consistent throughout:
**DIN 07712190 = Ms. Mitali Dasharathbharthi Gauswami (CMD); DIN 07712175 =
Mr. Dasharathbharthi Gopalbharthi Gauswami (WTD & CFO).** ✅ VERIFIED. The
garbled lines are drafting/OCR artifacts (the AR's item-4 explanatory
statement also mis-genders him as "her remuneration" at line 1031 — a
copy-paste error, not a substantive discrepancy), not a real identity
conflict.

**Relationship between the two promoters.** Indian/Gujarati patronymic naming
convention places [given name] [father's given name] [surname]. Mr.
Dasharathbharthi Gopalbharthi Gauswami's own middle name ("Gopalbharthi")
names his father, not Ms. Gauswami. Ms. Mitali's middle name
("Dasharathbharthi") matches Mr. Gauswami's given name. Combined with the
one-year age gap (35 vs 34) and post-marriage-name convention common in
Gujarat/Rajasthan (wife takes [husband's given name] as her own middle name),
the far more probable reading is **husband and wife**, not father–daughter.
❓ UNVERIFIED — this is inference from naming convention and age, not from an
explicit AR or registry statement of marital relationship; the AR itself
never states the relationship in words. Flagged, not asserted as fact.

**Founder history.** Per the company's own "About Us" marketing copy: "In
2017, she started Prizor Viztech Limited with ₹50,000, with no big office, no
legacy backing, and no shortcuts." 💬 FORUM/SOCIAL tier (self-published,
unverifiable rupee figure) — but consistent with the AR's incorporation date
(company AGM count implies FY2017-18 incorporation; CIN
L26401GJ2017PLC095719 confirms 2017 incorporation) ✅. This is a **founder**
promoter pair, not an inheritor situation — no succession dispute risk
category applies.

Other directorships (promoter group), per registry aggregator search
(ZaubaCorp/FileSure snippets, 📰/❓ tier — direct WebFetch to these registries
was blocked, see Search Log):
- Prizor Viztech Limited — CMD / WTD&CFO (subject company)
- Prizor Aitech India Limited — both serve as directors of this 51%-owned
  subsidiary (see 1B)
- Prizor Snacks Private Limited (CIN U52609GJ2019PTC111003, incorporated
  25-Dec-2019, Ahmedabad) — both listed as directors ✅ (search-engine-cached
  ZaubaCorp snippet)
- "Smartvis Technologies Private Limited" appears under the **identical CIN**
  U52609GJ2019PTC111003 in a separate search result — indicating this entity
  was renamed (Smartvis Technologies → Prizor Snacks, or the reverse) at some
  point. ❓ UNVERIFIED direction/date of the rename; flagged as a naming-history
  item worth registry confirmation.

### 1B. Promoter group entities — red flag screen

| Entity | Status | Relationship | Notes |
|---|---|---|---|
| Prizor Aitech India Limited | Active, 51% subsidiary of Prizor Viztech (acquired 09-Oct-2024) | Subsidiary | ✅ FY25 (part-year, Oct'24–Mar'25): turnover ₹0, loss after tax ₹41,970 (in thousands, i.e. ~₹0.42 lakh loss), share capital ₹10 lakh, total assets ₹10.17 lakh (AR AOC-1, lines 2015–2034). **Zero-revenue, shell-scale entity as of FY25-end** — not yet an operating business. Not itself a red flag at this stage (7-month-old subsidiary) but warrants a watch: capital committed to a non-revenue-generating related entity. |
| Prizor Snacks Private Limited (aka Smartvis Technologies Pvt Ltd, same CIN) | Active per registry snippet (last AGM 30-Dec-2023 per one source) | "Group Company" (named as such in AR RPT note, line 4150) | ⚠️ **Unrelated-business diversification**: a snacks/food business under the same promoter pair and the "Prizor" brand umbrella, apparently renamed from a technology-sounding name. AR discloses it as a related party but the OCR-garbled RPT transaction table does not cleanly show which line items belong to this entity (see 3A). Entity-count-vs-business-size flag: modest but present. |
| Om Security Solutions | Not independently confirmed as promoter-owned | Listed under "Related Entities" (AR RPT note, line 4151) | ❓ UNVERIFIED nature. AR shows a "Sale of Goods" type transaction of ₹3.55 crore (35,482.60, in thousands) with this entity in FY24 and ₹0 in FY25, plus an outstanding balance of ₹95,500 (in thousands is inconsistent with the note format — treat the absolute rupee value as ❓ pending clean-table verification) at FY24-end. Web search could not identify a specific "Om Security Solutions" entity in Ahmedabad linked to the Gauswami family (multiple same-named entities exist elsewhere in India, none matched). **This is the single largest-rupee related-party item found and its ownership/control relationship to the promoters is not established either way** — flagged for operator follow-up via direct MCA/RoC search, not asserted as adverse. |

No RoC strike-offs, no offshore/opaque-jurisdiction entities, and no evidence
of shell entities beyond the zero-revenue Prizor Aitech subsidiary were
found. Entity count (2 group companies + 1 subsidiary + 1 unclear related
entity) is on the higher side for an 8-year-old company that only listed in
2024, but not extreme.

### 1C. Education and professional background

**Ms. Mitali Dasharathbharthi Gauswami** — per AR explanatory statement (aged
35) and company/LinkedIn sources (📰/❓ tier, WebFetch to prizor.in and
LinkedIn blocked, relying on search-engine snippets):
- B.Pharma, Krantiguru Shyamji Krishna Verma Kachchh University, Gujarat
- MBA (Operations Management), IGNOU
- Ph.D., **Frankford International University**

❓ **FLAG**: Frankford International University could not be verified as an
accredited institution in this search session (no UGC/AICTE recognition, no
US regional-accreditation record found, and it did not appear in standard
diploma-mill watchlists either — search returned no specific information on
the institution at all, which is itself a mild signal for an obscure/online
"university"). This is a credential-verifiability flag, not a proven
diploma-mill finding — record as ❓ UNVERIFIED and note it explicitly rather
than treating the Ph.D. as fact or as fraud.

**Mr. Dasharathbharthi Gopalbharthi Gauswami** — per AR (aged 34) and search
snippets:
- B.Com., Hemchandracharya North Gujarat University, Patan, Gujarat (2010)
- MBA, Krantiguru Shyamji Krishna Verma Kachchh University, Gujarat (2012)

Both credentials from mainstream Indian state universities — no
verifiability concern on his side. Combined industry experience: AR/search
snippets claim "9+ years" (Mitali) and "11+ years" (Dasharathbharthi) in the
tech/security-electronics space, consistent with the 2017 founding plus
pre-incorporation experience; not independently verifiable beyond the AR's
own claim (❓ tier).

### 1D. History before the current company

Founder situation (see 1A) — no inheritance, no succession dispute, no
unexplained career gap surfaced in search. Prizor Viztech is effectively the
promoters' first and only substantial operating venture; Prizor Snacks and
Prizor Aitech are subsequent, smaller offshoots under the same umbrella.

---

## SECTION 2: LEGAL & REGULATORY RECORD

Search was conducted across SEBI, criminal/economic-offence, tax/revenue,
other-regulator and civil-litigation categories using promoter names, company
name, and "fraud/FIR/arrest/SEBI/NCLT/SFIO" combinations (see Search Log).

**2A. SEBI actions**: No adjudication orders, SAT appeals, insider-trading
cases, consent orders, or LODR-non-compliance penalties against Prizor
Viztech or either promoter were found. SEBI's own public-issues filing page
for the company shows the standard IPO filing record, nothing adverse. **CLEAN
RECORD** ✅ (limited by: this is a company listed only since July 2024, so the
population of possible SEBI actions is inherently small).

**2B. Criminal cases**: No FIR, arrest, PMLA/ED, Companies Act
prosecution, or economic-offence report found for either promoter under
either name variant searched. **CLEAN RECORD** ✅ (search coverage caveat:
Indian court-record search engines are fragmented; absence of a hit is not
equivalent to a certified clean record, but multiple search angles turned up
nothing).

**2C. Tax and revenue**: No IT search-and-seizure, DRI, SFIO, or benami
reports found. **CLEAN RECORD** ✅ (same caveat as above).

**2D. Other regulators**: No RBI/IRDAI/TRAI/CCI/NGT/consumer-forum/labour
action found. No MCA disqualification or NCLT oppression petition found
against either promoter personally. (Note: an unrelated company literally
named "Nakoda Limited" — different CIN, polyester/GDR fraud, later under
NCLT insolvency — surfaced in search; this is **not** the same entity as
"Nakoda Group of Industries Limited," the Nagpur-based food-processing SME
where independent director Dahyalal Prajapati also sits — confirmed distinct
via business description and listing history. Flagging the disambiguation
explicitly so it is not mis-linked downstream.)

**2E. Civil litigation**: The DRHP contains boilerplate risk-factor language
("the company has certain outstanding litigation against it, an adverse
outcome of which may adversely affect its business") that is standard SME-IPO
disclosure text; the specific litigation schedule could not be retrieved (DRHP
PDF fetch was blocked, see Search Log). The FY25 Annual Report's Board's
Report and CFO certification both explicitly state: **"the Company does not
have any pending litigations which would impact its financial position"**
✅ VERIFIED (Annual_Report_2025.txt, lines 2921, 4621, standalone and
consolidated). This post-listing statement is more current and more
authoritative than the pre-IPO DRHP boilerplate; treat the DRHP language as
generic and the AR statement as the operative finding, with a residual ❓ for
not having seen the DRHP litigation schedule itself.

**2F. Legal red flag summary table**

| Sub-area | Finding |
|---|---|
| SEBI actions | ✅ Clean |
| Criminal cases | ✅ Clean |
| Tax/revenue | ✅ Clean |
| Other regulators | ✅ Clean |
| Civil litigation | ✅ Clean (per FY25 AR; DRHP litigation schedule not independently reviewed — ❓ residual) |

---

## SECTION 3: BUSINESS CONDUCT & ETHICAL TRACK RECORD

### 3A. Related-party transaction history

From AR Note 31 (Related Party Disclosure, AS-18), FY25 vs FY24, ₹ in
thousands (OCR reflow makes exact line-to-line mapping imperfect; figures
below are as extracted, flagged ❓ where mapping is uncertain):

- Director remuneration: Dasharathbharthi ₹1,200.00 (FY25) / ₹1,200.00 (FY24);
  Mitali ₹1,200.00 (FY25) / ₹1,200.00 (FY24) — i.e. ₹12 lakh/year each through
  FY25, **stepping up to ₹2.5 lakh/month (₹30 lakh/year) each from 1-Jul-2025**
  per the AGM special resolution (item 3 & 4, lines 874–1078). A 150% hike.
- Loans received from directors (promoter-to-company): Dasharathbharthi
  ₹10,239.99k and ₹25,751.19k in two tranches in FY25 (₹nil FY24); Mitali
  ₹2,361.80k and ₹9,156.50k in FY25 (₹nil FY24).
- Loans repaid to directors: Dasharathbharthi ₹12,064.86k (FY25) /
  ₹27,576.06k outstanding-type figure (FY24 column); Mitali ₹4,655.13k /
  ₹11,449.83k; further lines show ₹50.30k/₹170.20k (Mitali) and
  ₹6,152.97k/₹11,051.10k (Dasharathbharthi).
- Om Security Solutions: ₹35,482.60k "Sale of Goods"-type transaction in FY24,
  ₹0 in FY25; outstanding balance ₹95.50k in FY24, ₹0 FY25. Nature/ownership
  of this counterparty is ❓ UNVERIFIED (see 1B).
- Prizor Aitech India Limited: ₹510.00k / ₹490.00k "Investment"-type entries
  in FY25 for the 51% subsidiary acquisition, consistent with AOC-1.
- Relative of KMP: "Gauswami Badrubharathi G" received ₹105.00k in FY24
  (₹0 FY25) — a family member payment, small in size, disclosed.
- Company Secretary: Ms. Hetaxiben Umang Bhatt appointed 07-May-2024
  (coincident with IPO preparation); no resignation found.
- **No loans or advances were made by the company TO promoters/directors/KMP**
  ✅ (explicit auditor statement, line 4154) — the loan flow runs the other
  way (promoters lending working capital to the company), which is a
  supportive rather than extractive RPT pattern for a growth-stage company.

**3B. Capital allocation behaviour**

- No dividend declared in FY25 despite a profitable year (FY25 PAT ≈ ₹10.15
  crore on revenue ≈ ₹71.1 crore per the financial-statements notes — the
  Board's Report headline figures of "₹7,11,387.02" and "₹1,01,526.31" are
  unit-unlabelled in the narrative text but reconcile to the ₹-thousands
  figures used throughout the financial notes) ✅ reasonable for a
  recently-listed, rapidly growing SME reinvesting cash; not flagged as
  cash-hoarding given IPO-stage capital needs.
- Bonus issue of 66,00,003 shares on 09-May-2024, immediately pre-IPO —
  standard SME-IPO capital-structuring step, not inherently adverse.
- **A ₹40 lakh loan-to-equity conversion (4,00,000 shares) occurred during
  the year**, alongside the bonus issue and IPO allotment. The net effect:
  Mitali's stake fell from 90.00% (pre-IPO) to 45.18% (post-IPO/bonus/
  conversion), while Dasharathbharthi's stake **rose** from 9.99% to 23.10%
  — i.e., the loan-to-equity conversion appears to have disproportionately
  benefited one promoter's post-listing ownership share relative to the
  other. ⚠️ **FLAG**: this is a capital-allocation item worth explicit
  operator attention — it is not proven to be improper (could simply reflect
  which promoter's loan balance was converted), but the asymmetric effect on
  relative ownership between spouses/co-promoters is the kind of item that
  merits a direct question rather than a pass-through.
- Remuneration hike (150%, see 3A) is proportionate to FY26 profit growth
  (PAT +104.5% YoY, revenue +108.1% YoY per FY26 results reported in market
  coverage 📰) — **not** a case of salary rising through performance decline.

**3C. Promoter share transactions**

- Combined promoter holding: 90%+9.99% pre-IPO → 68.28% at FY25-end
  (31-Mar-2025) → ~67.9–68.6% as of mid-2026 per aggregator search snippets
  (Angel One/Trendlyne/Screener, 📰 tier, direct fetch blocked) — broadly
  **stable**, consistent with minimum public shareholding dilution from the
  IPO itself rather than an active creeping-acquisition or sell-down pattern.
- **Pledge**: NOT FOUND in verifiable form. The FY25 Annual Report does not
  reproduce the SEBI-format shareholding-pattern table with an encumbrance
  column (searched for "encumbrance"/"pledge"/"Table II" — no hits). A CARO
  clause (line 3132–3134) states the *company* has not raised loans against
  pledge of *subsidiary* securities — this does not speak to whether the
  *promoters* have pledged their *own* Prizor Viztech shares. Direct
  WebFetch to shareholding-pattern aggregators (Trendlyne, MarketsMojo,
  Screener) returned HTTP 403 in this session and could not be retrieved;
  WebSearch snippets on pledge specifically returned no percentage. **Record
  pledge as NOT FOUND rather than assumed zero** — this should be verified
  against the company's quarterly SEBI (SAST/SDD) shareholding-pattern filing
  before the operator relies on a "no pledge" assumption.
- No suspicious pre-announcement trades, warrant lapses, or sale-timed-to-
  highs pattern found (no such history exists yet — a July 2024 SME listing
  gives too short a track record for this sub-item to be meaningfully
  assessed).

**3D. Minority treatment**

No proxy-advisory (IiAS/SES/InGovern) adverse recommendation, no AGM
controversy, no SCORES complaint, and no unfair-delisting or selective-
disclosure finding surfaced in search. All RPTs described above are
disclosed in the AR per standard AS-18/Companies Act requirements. **CLEAN
RECORD** ✅, with the caveat that a company listed just under two years has
had only one AGM cycle in which proxy advisors would plausibly weigh in, and
none of the major Indian proxy advisory firms appear to cover an SME-platform
micro-cap of this size.

**3E. Auditor relationship**

M/s. M B Jajodia & Associates, Chartered Accountants (FRN 139647W), Ahmedabad
— appointed at the AGM held 30-Apr-2024 (i.e., concurrent with IPO
preparation) for a five-year term ✅. No resignation during the year (explicit
auditor statement, line 3191) ✅. Statutory audit opinion: unqualified,
adequate ICFR ✅. Secretarial Auditor (M/s Insiya Nalawala and Associates):
**no qualification, reservation, adverse remark, or disclaimer** ✅ (line
1591, 1601). No whistleblower complaints reported to the auditor (line 3154)
✅. Audit fee ₹2.00 lakh (FY25) plus ₹37.96 lakh for "Professional Services"
(FY25, versus ₹0 FY24) — the professional-services fee is roughly 19x the
statutory audit fee in FY25, which is a **non-audit-fee-dominance pattern**
worth noting (⚠️), though this is very plausibly IPO-related professional
services (a one-off, non-recurring cost tied to the July 2024 listing) rather
than an ongoing independence concern — flagged for context, not treated as
adverse without the FY26 figure to confirm it was one-off.

---

## SECTION 4: REPUTATION & PUBLIC PERCEPTION

**4A. Media reputation**: Coverage is almost entirely IPO-tracker /
share-price-aggregator in nature (Chittorgarh, Groww, Zerodha, Angel One,
Moneycontrol-style trackers), consistent with a small, recently-listed SME.
One IPO-review source (Chittorgarh's dedicated review page, title captured
via search as **"Prizor Viztech NSE SME IPO review (Avoid)"**) appears to
have carried an "Avoid" recommendation ahead of the July 2024 listing — the
underlying rationale could not be retrieved (WebFetch to chittorgarh.com
blocked, 403). 📰 MEDIA REPORTED, incomplete — flagged because a pre-IPO
"Avoid" call from a widely-used retail IPO-review source is a signal worth
the operator chasing down directly (typically such calls cite thin listed
track record, small issue size, and valuation, not necessarily promoter
conduct — but the specific reasoning is unverified here).

**4B. Employee reputation**: No Glassdoor or AmbitionBox reviews found for
Prizor Viztech specifically (searches returned only unrelated results for
"AmbitionBox.com" itself as a company). Consistent with a company too small
and too newly listed to have accumulated review volume — **not a finding
either way**, recorded as a coverage gap rather than a clean record.

**4C. Investor and analyst perception**: No activist campaign, short-seller
report, or analyst coverage initiation found — expected for an NSE SME-
platform micro-cap. FII holding is reported around 1.17%, DII 0%, at a
recent date (📰 aggregator snippet) — negligible institutional presence,
consistent with the company's size and listing venue rather than a red flag
in isolation.

**4D. Political/government connections**: None found in search.

**4E. Industry peer reputation**: Not separately assessed beyond the above;
no adverse peer commentary surfaced.

**4F. Philanthropy/CSR beyond mandate**: Not found in the AR extract or
search; CSR provisions were not separately located in the text cache
excerpt reviewed (company may be below the CSR-applicability threshold given
its FY25 profit level — not confirmed either way, NOT FOUND).

---

## SECTION 5: CXO & BOARD QUALITY

**5A. CXO turnover (5 years)**: Company has been public for under two years;
CFO role is held by Whole-Time Director Dasharathbharthi Gauswami himself
(promoter-CFO, not an independent hire) — this is itself worth noting as a
**key-person-risk** item rather than a turnover item: there is no
professional, non-family CFO. Company Secretary Ms. Hetaxiben Umang Bhatt was
appointed 07-May-2024 (pre-IPO) with no subsequent resignation found. No
internal-audit-head change history available (too short a public track
record).

**5B. Board quality**: Five-member board — two executive promoters (Mitali,
Dasharathbharthi) and three independent directors (Dahyalal Bansilal
Prajapati DIN 09592327, Preety Priya Ghosh DIN 09811959, Brahma Ghosh Raval
DIN 10523186), i.e. 60% independent — compliant with LODR minimums for an
executive-chairman board. Audit Committee: 2 independent + 1 executive
(Mitali), independent chairman (Prajapati) — two-thirds-independent LODR
threshold is met.

All three independent directors hold **recently-issued DINs (09xxx/10xxx
range, consistent with first directorship allotment around 2023–2024)** and
were appointed concurrent with the IPO — i.e., **none have a pre-existing,
multi-year track record with this specific company's board**; their
independence tenure effectively starts at listing.

Cross-membership / "professional independent director" pattern (⚠️ flag):
- **Dahyalal Bansilal Prajapati** currently also serves as an independent/
  board director of **Nakoda Group of Industries Limited** (Nagpur-based
  food-processing SME, NSE-listed) and **Greenleaf Envirotech Limited**, and
  **resigned mid-term from DMR Hydroengineering & Infrastructures Limited on
  11-Mar-2025**, citing "increasing other professional commitments" (📰/❓
  tier, search-engine-cached snippet, source document not independently
  fetched). This is a mid-term independent-director exit — but **at a
  different listed company, not at Prizor Viztech** — and is presented here
  as base-rate context on the individual's bandwidth, not as an adverse
  finding against Prizor's own governance.
- **Preety Priya Ghosh** appears as a director on other private entities
  (Amserve Hospitality Services Pvt Ltd, Biopol Chemicals Ltd) per registry
  search snippets — multi-board pattern, not independently confirmed as
  Prizor-specific concern.

This overall pattern — independent directors serving across several small/
SME boards simultaneously, appointed en bloc at IPO time — is a well-known
structural feature of the Indian SME-IPO ecosystem (a limited pool of
"professional" independent directors serves many small issuers for fee
income) rather than something specific to Prizor's promoters. It is recorded
as a board-quality caution (thin per-company engagement bandwidth is
plausible) rather than a promoter-conduct red flag.

**5C. Key-person risk and succession visibility**: High key-person
concentration — both the CMD and the WTD/CFO are the founding promoters, no
non-family C-suite hire has been identified (no professional/external CFO,
COO, or CEO distinct from the promoter pair). No succession plan disclosure
found. For a company at this stage (2 years public, founder-run) this is
normal rather than alarming, but it is a structural dependency worth
tracking as the company scales (FY26 revenue already ₹148 crore, +108% YoY).

---

## SECTION 6: PROMOTER QUALITY VERDICT

### 6A. Scorecard (10 dimensions, strictly from Sections 1–5 findings)

| # | Dimension | Rating | Basis |
|---|---|---|---|
| 1 | Family/promoter identity clarity | ⚠️ | AR text-cache DIN garbling required cross-check to resolve (resolved); relationship (husband-wife) never explicitly stated, inferred only |
| 2 | Promoter group entity structure | ⚠️ | Unrelated-business group company (snacks) under apparent rename; zero-revenue subsidiary; one related entity (Om Security Solutions) of unclear ownership with the largest single RPT rupee value found |
| 3 | Legal & regulatory record | ✅ | No SEBI/criminal/tax/other-regulator adverse finding across all search angles; AR affirmatively states no pending litigation |
| 4 | RPT conduct | ⚠️ | Loan-to-equity conversion during the year had an asymmetric effect on the two promoters' relative post-IPO ownership; Om Security Solutions relationship unclear |
| 5 | Capital allocation / remuneration | ✅ | Remuneration hike proportionate to strong, verified profit growth; no dividend but reasonable at this growth stage; no value-destructive related-party acquisition found |
| 6 | Share pledge / transactions | ⚠️ | Pledge could not be verified either way (NOT FOUND, not assumed zero); promoter holding otherwise stable since listing |
| 7 | Minority treatment | ✅ | No proxy-advisory adverse call, no AGM controversy, no SCORES complaint found |
| 8 | Auditor relationship | ✅ | Clean, unqualified, no resignation, no secretarial-audit qualification; non-audit fee spike plausibly IPO-related one-off |
| 9 | Reputation & public perception | ⚠️ | Unverifiable Ph.D. credential (Frankford International University); a retail IPO-review source reportedly rated the IPO "Avoid" pre-listing (rationale unconfirmed) |
| 10 | CXO & board quality | ⚠️ | All independent directors appointed at IPO with recent-vintage DINs; multi-board "professional independent director" pattern typical of SME-IPO ecosystem; promoter also holds the CFO seat (no external CFO) |

**Scorecard: clean = 5, caution = 5, red = 0**

### 6B. Classification

**CAUTION.** No verified legal, regulatory, or criminal adverse finding
against either promoter — the legal/regulatory record (Section 2) is
genuinely clean across every search angle used. What keeps this out of
TRUSTWORTHY is an accumulation of **unresolved, non-trivial ❓/⚠️ items**
typical of a very recently listed SME promoter group: an unverifiable
doctoral credential, an unclear large related-party counterparty, an
asymmetric loan-to-equity conversion between the two promoters, unverified
pledge status, and a board whose independence is fresh-minted rather than
tested. None of these rises to CONCERN on its own; together they warrant
caution and specific operator follow-up rather than a clean pass.

### 6C. Deal-breaker checks (recorded, not enforced)

| Deal-breaker | Triggered? |
|---|---|
| SEBI market ban | No |
| Economic-offence conviction | No |
| Live SFIO probe | No |
| PMLA with attached assets | No |
| Auditor resignation within 3 years | No |
| Pledge >40% | Not established either way (NOT FOUND) |
| Multiple mid-term independent-director exits within 3 years (at this company) | No — the one mid-term ID exit found (Prajapati, DMR Hydroengineering) was **at a different company**, not Prizor |
| Restatement cutting past profits >10% | No |

No deal-breakers triggered at Prizor Viztech itself.

### 6D. Transition evidence scan

Searched specifically for: new professional CEO/CFO from outside the family,
institutional investor entry, pledge reduction trend, exit of a problematic
family member, governance overhaul, stake sale to a credible strategic.

**TRANSITION EVIDENCE: NONE FOUND.**

Context: this scan is designed to distinguish a *static* adverse promoter
situation from one that is actively improving. Prizor Viztech does not fit
either template cleanly — it is a **freshly listed (July 2024) founder-run
company with no prior public "distressed promoter" baseline to transition
away from**. There is no professional outside CFO (the WTD is the CFO), no
disclosed institutional-investor stake build-up beyond the negligible
~1.17% FII figure noted in 4C, no pledge-reduction trend to point to (pledge
status itself unverified), and no family-member exit. The relevant read for
synthesis is not "CONCERN improving" but "CAUTION, first two years public,
governance not yet stress-tested."

### 6E. Final output card

```
PROMOTER: Gauswami family (Mitali D. Gauswami, CMD; Dasharathbharthi G.
Gauswami, WTD & CFO) — Prizor Viztech Limited (PRIZOR)
VERDICT: CAUTION
LEGAL/REGULATORY RECORD: Clean (no SEBI/criminal/tax/other-regulator
findings; verified via multi-angle search)
KEY CAUTIONS: (1) unverifiable Ph.D. credential; (2) unclear large related
party (Om Security Solutions); (3) asymmetric loan-to-equity conversion
between co-promoters pre-IPO; (4) pledge status not verifiable this
session; (5) independent board is IPO-fresh, not tenure-tested; (6)
promoter holds the CFO seat directly (key-person concentration)
TRANSITION EVIDENCE: None found (not applicable — no prior baseline;
company listed July 2024)
DECISION: Stays with the operator; this is not a halt condition.
```

---

## SEARCH LOG

**searches_performed** (queries run this session):
1. "Prizor Viztech promoter Mitali Gauswami background"
2. "Prizor Viztech Dasharathbharthi Gauswami CFO"
3. "Prizor Viztech" SEBI OR litigation OR fraud OR investigation
4. "Prizor Viztech" IPO SME NSE listing 2024 promoter
5. Frankford International University PhD diploma mill unaccredited
6. "Prizor Viztech" outstanding litigation DRHP prospectus details
7. "Om Security Solutions" Ahmedabad Gauswami proprietorship
8. "Prizor Snacks" Private Limited Gauswami
9. Mitali Dasharathbharthi Gauswami director profile (FileSure attempt)
10. "Dasharathbharthi Gopalbharthi Gauswami" DIN 07712175 director companies
11. "Smartvis Technologies" Prizor Snacks name change struck off
12. Prizor Viztech Glassdoor OR AmbitionBox employee reviews
13. Prizor Viztech share price manipulation OR circuit OR SME IPO controversy grey market
14. "PRIZOR" NSE compliance OR show cause OR penalty OR non-compliance regulation
15. ambitionbox.com Prizor Viztech Limited reviews rating
16. "Prizor Viztech" institutional investor OR FII OR mutual fund stake
17. "Dahyalal Bansilal Prajapati" DIN 09592327 director
18. "Preety Priya Ghosh" DIN 09811959 independent director
19. "Brahma Ghosh Raval" OR "Brahma Raval" DIN 10523186 director
20. "Nakoda Group of Industries" SEBI OR fraud OR NCLT OR default
21. Gauswami Prizor Viztech promoter criminal case OR police OR FIR OR arrest
22. "Prizor Viztech" quarterly results FY26 revenue profit
23. "Nakoda Group of Industries Limited" business SME NSE listed
24. "Prizor Viztech" promoter pledge shares percentage shareholding pattern
25. WebFetch attempts: NSE letters (PVL/038/2025-26, PVL/022/2026-27), DRHP
    PDF, ZaubaCorp (2 companies), FileSure, thecompanycheck, Screener,
    Trendlyne, MarketsMojo, prizor.in (group-company, management pages),
    Chittorgarh IPO review page

**searches_skipped** (blocked/could not complete — HTTP 403 from proxy on
every attempt, not a quota exhaustion; recorded so this is visibly partial
on these specific items):
- NSE corporate-announcement letters PVL/038/2025-26 (09-Oct-2025) and
  PVL/022/2026-27 (28-May-2026) — content unknown, could contain compliance
  or other disclosures relevant to Section 2/3
- Full DRHP litigation/promoter-group schedule (prizor.in-hosted PDF)
- ZaubaCorp full director/company listing for both promoters and for
  Smartvis Technologies / Prizor Snacks (rename history, other directorships)
- FileSure director profile (Mitali Gauswami, DIN 07712190) — would have
  given a complete associated-companies list
- Screener.in, Trendlyne, MarketsMojo shareholding-pattern pages — would
  have given a verifiable pledge percentage and trend
- Chittorgarh's dedicated IPO-review page carrying the "(Avoid)" title —
  rationale for that call not retrieved
- prizor.in "group-company" and "management" pages (official company
  description of Prizor Snacks and full management bios)

Given the volume and specificity of these blocked fetches — several of which
bear directly on Section 3 (pledge %) and Section 1B/5B (entity/board
verification) — this report is issued as **status: partial**.
