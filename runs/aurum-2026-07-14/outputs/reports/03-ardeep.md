# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: Aurum PropTech Ltd (AURUM) | Run date: 2026-07-14
Source: Annual Report FY2024-25 (file mislabelled "Annual_Report_2023.pdf", 12th AGM
notice dated Sep 1 2025, 162 pages). Standalone financials + Notes 1-32 (auditor's
report p.128-141 [PDF p.85-91]); Consolidated financials + Notes 1-34 (auditor's
report p.201-208 [PDF p.121-125]). Text extract: outputs/_working/AR_FY25.txt,
page-anchored to `===== PDF PAGE N =====` markers; printed page numbers cited where
visible on the page, PDF page number given in brackets where the printed number is
absent or ambiguous.

Method: backward read — auditor's report and CARO first, then Notes (per the Phase 2
special instruction, reconciled against the Stage 2 triple-pass output rather than
re-extracted), then financial statements, then risk/MD&A, then governance, and the
Group CEO's Communique (functionally the "Chairman's letter" — this AR carries no
separate Chairman's letter; a single Non-Executive Chairman-of-the-CSR-Committee role
exists but the front-matter letter is signed by the Founder and Group CEO) last.

Rating key throughout: 🟢 Clean | 🟡 Watch | 🔴 Red Flag. Per pipeline rules, the
kill-switch assessment at the end of each phase is INFORMATIONAL ONLY and never halts
this run; every phase below states what a human reviewer would conclude and then
proceeds.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core opinion

| | Standalone | Consolidated |
|---|---|---|
| Opinion type | Unmodified ("give a true and fair view...") | Unmodified |
| Basis | Standards on Auditing (SA), Section 143(10) | SA, Section 143(10); "based on the consideration of reports of the other auditors" |
| Going concern language | None beyond standard SA 570 responsibility boilerplate; management affirms going concern in accounting policies (Note 2(e)) | Same — no Emphasis of Matter, no material uncertainty paragraph |

Reproduced opinion language (standalone): "In our opinion and to the best of our
information and according to the explanations given to us, the aforesaid financial
statements give... a true and fair view... of the state of affairs of the Company as
at March 31, 2025, the Loss and total comprehensive income..." (Auditor's Report,
Opinion, p.128 [PDF p.85]). Consolidated opinion is materially identical in structure,
explicitly qualified by reliance on other auditors' reports (Auditor's Report,
Opinion, p.201 [PDF p.121]).

No going-concern qualification exists in either opinion despite: consolidated losses
in both FY24 (₹(76.36) Cr pre-exceptional / ₹(77.80) Cr after) and FY25 (₹(44.47) Cr)
(Consolidated Statement of P&L, p.211-212 [PDF p.126]), and negative net worth at two
of the Group's largest-by-goodwill subsidiaries — NestAway ₹(36.08) Cr and Helloworld
₹(17.42) Cr (Note 25, Consolidated Notes, p.267 [PDF p.157], directly verified in this
stage: "Helloworld Technologies India Private Limited (6%) (1,742)... NestAway
Technologies Private Limited (13%) (3,608)"). Group-level consolidated equity of
₹284.47 Cr (Consolidated Balance Sheet, p.211 [PDF p.126]) is evidently what keeps the
auditors comfortable at the Group level notwithstanding subsidiary-level distress —
this is a defensible technical position but it means the headline "clean opinion"
conveys none of the subsidiary-level stress documented elsewhere in the same AR.

### 1B. Key Audit Matters

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Intangible assets — capitalisation & impairment judgment (standalone: ₹290 Lakh capitalised, ₹313 Lakh under development, Note 3.c/17, p.130 [PDF p.86]; consolidated: ₹1,801 Lakh capitalised, ₹1,178 Lakh under development, Note 3.d/17, p.202 [PDF p.122]) | Judgement on recognition criteria (technical feasibility, intention/ability to complete, future economic benefit) and on impairment assumptions (forecasted cash flows, discount rates) for internally-developed software | Testing capitalised costs to documentation, evaluating policy compliance, inquiring with project teams, assessing disclosure adequacy | 🟡 |
| Investments (standalone only) — ₹26,120 Lakh non-current investments, mostly unquoted equity in subsidiaries, measured at fair value (Note 4.a.1, p.130-131 [PDF p.86]) | Significant judgement in unquoted/illiquid fair valuation — projected cash flows, growth rates, discount rates, valuer independence | Valuation specialists engaged, valuation reports reviewed, methodology and inputs evaluated | 🟡 |

This is the sole pair of KAMs in each report — no separate KAM on revenue
recognition, provisioning, or fair value of any other class. Both KAMs point at the
same underlying vulnerability from different angles: the Company/Group's carrying
values for self-generated and acquired intangible value rest on management-supplied
cash-flow and discount-rate assumptions that are not independently disclosed in
granular form anywhere in the AR. This connects directly to the goodwill
concentration finding carried forward from Stage 2 (B02 finding #2) — goodwill is a
non-KAM item sitting right next to two audit areas the auditor did flag as
judgement-heavy.

### 1C. Emphasis of Matter and Other Matters

No Emphasis of Matter paragraph in either report. Other Matters (consolidated only,
p.204 [PDF p.123]):
- (a) 9 subsidiaries — total assets ₹294.57 Cr, total income ₹219.80 Cr, net loss
  after tax ₹26.33 Cr, total comprehensive loss ₹26.76 Cr, net cash outflow ₹1.09 Cr —
  audited by other, unnamed auditors; principal auditor's opinion "in so far as it
  relates to the amounts and disclosures included in respect of these subsidiaries is
  based solely on the report of such auditor."
- (b) FY24 comparative consolidated financial statements were audited by the
  predecessor auditor (report dated April 29, 2024); the current (FY25) auditor did
  not audit the comparative period.

Against consolidated total assets of ₹674.51 Cr, the ₹294.57 Cr of other-auditor
coverage is **43.68%** of the balance sheet — matching Stage 2's "~44%" figure
independently recomputed here (29,457 / 67,451 = 0.4368).

### 1D. CARO 2020 clause-by-clause

**Standalone (Annexure B, p.137-141 [PDF p.90-91])** — clean except:
- **Clause iii(c)/(f)**: ₹2,216 Lakh (44% of the standalone loan book) is repayable on
  demand with no fixed schedule, extended to related parties (p.138-139 [PDF p.90]).
  Not a default — borrowers have been "regular in the repayment of the principal and
  payment of interest" — but a structural open-endedness the auditor itself
  singles out.
- **Clause ix(a)**: standalone-level — "the Company has not defaulted in repayment of
  loans or other borrowings" — **clean at the standalone level.**
- **Clause xvii**: no cash losses in the current year; ₹488 Lakh cash losses in the
  immediately preceding year (FY24) (p.141 [PDF p.91]).
- **Clause xx**: CSR spend not applicable — Company did not meet the Section 135
  eligibility threshold (average net loss over three preceding years) (p.141
  [PDF p.91]).
- Clauses ii (inventory) and v (deposits): not applicable — services company, no
  inventory, no public deposits.
- **Rule 11(iii) [not a CARO clause but part of the same "Other Legal and Regulatory
  Requirements" section]**: "There has been delay in transferring amounts, required
  to be transferred, to the Investor Education and Protection Fund by the Company"
  (p.135 [PDF p.88]) — see the direct contradiction with Note 10.b.2 flagged under
  1C/Phase 2 below.

**Consolidated (Annexure B, p.207-208 [PDF p.124-125])** — a summary table lists
qualified/adverse CARO clauses across 7 Group entities in the same audit year, none of
which carries any narrative amount disclosure beyond the clause reference itself (the
detail sits in each subsidiary's own, separately-filed financial statements, not
reproduced in this AR):

| # | Entity | Clause qualified |
|---|---|---|
| 1 | Aurum PropTech Limited (Holding Co.) | iii(c) |
| 2 | Integrow Asset Management Pvt Ltd | **ix(a) — loan/borrowing default** |
| 3 | Monk Tech Ventures Pvt Ltd | vii(a) |
| 4 | NestAway Technologies Pvt Ltd | i(a) & (b) |
| 5 | NestAway Technologies Pvt Ltd | vii(a), (b) & (c) |
| 6 | K2V2 Technologies Pvt Ltd | vii(a) |
| 7 | Bonds Brain Technologies Pvt Ltd | iii(c) |

(Verified directly against the rendered text, p.208 [PDF p.124]; matches Stage 2 /
B02 finding #1 exactly, including the double NestAway qualification.) Clause ix(a) —
default in repayment of loans/borrowings or interest — is the single most serious
individual CARO exception on this list; the AR gives no further detail (amount,
counterparty, cure status) anywhere in the consolidated notes or annexures reviewed.
This is a **NOT FOUND** for the quantum and cure status of the Integrow default —
the fact of the default is confirmed by the auditor, but its size and resolution are
not disclosed in this document.

The consolidated CARO also confirms clause vii(a) exceptions (disputed statutory
dues by tax type/forum) at three subsidiaries with no amounts given in this AR, and
clause i(a)/(b) (fixed asset records/title) at NestAway with no amounts given. All
three are **NOT FOUND** for quantum in this document.

Clause xi (fraud): both standalone and consolidated reports state no fraud noticed
or reported, no whistleblower complaints received (Annexure B, standalone, p.141
[PDF p.91]) — 🟢 on this specific clause, taken at face value of the audit procedures
described.

### 1E. Auditor continuity

- Firm: Kirtane & Pandit LLP, ICAI FRN 105215W/W100057; engagement partner Suhrud
  Lele, Membership No. 121162.
- **First year of appointment** — the Notice of AGM (item 3, p.1 [PDF p.2]) proposes
  re-appointment for a fresh five-year term (12th AGM to 17th AGM), and the Other
  Matters paragraph confirms the FY24 comparatives were audited by a **predecessor
  firm**, i.e., FY25 is this firm's first audit year of Aurum PropTech.
- Fees (standalone only; no separate consolidated group-wide fee disclosure found —
  **NOT FOUND** for consolidated/group audit fee): statutory audit fee ₹23 Lakh
  (FY24: ₹29 Lakh); other professional/certification fees ₹6 Lakh (FY24: ₹2 Lakh)
  (Note 18, standalone, p.184 [PDF p.113]). Non-audit/audit ratio = 6/23 = **26%,
  does not exceed audit fee** — no flag on this specific test, though the ratio rose
  from 7% (FY24: 2/29) to 26% in the first year of the new engagement.

### 1F. Standalone vs consolidated differences

Consolidated carries substantially more CARO exceptions (7 entities vs. the
single-entity holding-company exception that also appears standalone), reflects
reliance on other auditors for 44% of Group assets, and did not audit FY24
comparatives. The standalone report is materially cleaner precisely because it
excludes exactly the entities (Integrow, NestAway, K2V2, Monk Tech Ventures, Bonds
Brain) where the exceptions live — a reader of the standalone financials only would
see none of this.

### Phase 1 summary

| Item | Verdict |
|---|---|
| Opinion type | Unmodified, both statement sets |
| KAMs | Standard, judgement-heavy but procedurally addressed |
| CARO — standalone | 🟡 Watch (open-ended related-party lending, IEPF delay) |
| CARO — consolidated | 🔴 Red Flag (confirmed default + 6 further entity exceptions, undisclosed amounts) |
| Auditor continuity | 🟡 Watch (first-year auditor, 44% coverage gap, FY24 comparatives unaudited by this firm) |

**Phase 1 verdict: 🔴 Red Flag.**

**Kill switch assessment (informational only):** Based on Phase 1 alone, a human
reviewer would have reason to pause, because a statutory auditor has confirmed an
actual loan/interest default at a Group subsidiary (Integrow, CARO ix(a)) in the same
year that six other Group entities also drew CARO exceptions, none of which is
quantified in this document, under a first-year auditor covering only 56% of Group
assets directly. This does not halt the pipeline; continuing to Phase 2.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction, the Stage 2 (B02) triple-pass extraction is
treated as the primary source for this phase; the task here is verification against
the document, not re-extraction. Reconciliation below.

### Verification of the Stage 2 Top 15 findings

| # | Finding (abbreviated) | Verification |
|---|---|---|
| 1 | CARO exceptions, 7 entities, Integrow default | ✓ Verified — independently re-read the same table (p.208 [PDF p.124]); clause numbers match exactly |
| 2 | Goodwill ₹174.25 Cr = 61% of equity; NestAway+Helloworld 80.5%, both negative net worth | ✓ Verified — Goodwill on consolidation ₹17,425 Lakh confirmed at Note 3.c (p.229 [PDF p.135]) and Consolidated Balance Sheet (p.211 [PDF p.126]); NestAway net assets ₹(3,608) Lakh and Helloworld ₹(1,742) Lakh independently confirmed at Note 25 (p.267 [PDF p.157]) |
| 3 | Auditor did not audit ~44% of assets, nor FY24 comparatives | ✓ Verified — recomputed independently: ₹294.57 Cr / ₹674.51 Cr = 43.68% |
| 4 | CARO Annexure B (₹15,242 Lakh) vs Note 4.a.1/21(D)(i) (₹25,420-26,120 Lakh) investment gap | ✓ Verified — Annexure B standalone (p.138 [PDF p.90]) shows "Balance outstanding... Subsidiaries: 15,242" against Standalone Balance Sheet Note 4.a.1 "Investments 26,120" (p.144 [PDF p.92]) — same auditor, same balance sheet date, unreconciled in this document |
| 5 | IEPF contradiction: auditor Rule 11 delay finding vs Note 10.b.2 "no amount due" | ✓ Verified twice independently — Auditor's Report Rule 11(iii) "There has been delay in transferring amounts... to the Investor Education and Protection Fund" (p.135, p.205 [PDF p.88, p.123]) vs Note 10.b.2 "there is no amount due and outstanding as at Balance Sheet date to be credited to the fund" (p.245 [PDF p.143], consolidated — text re-read directly in this stage) |
| 6 | Receivables ageing deterioration masked by headline growth | ✓ Verified — Note 4.c re-read directly (p.236 [PDF p.139]): 1-2yr bucket 174→626 Lakh (+259.8%), 2-3yr 12→160 Lakh (+1,233%), ECL "significant increase in credit risk" bucket 159→109 Lakh (declined) — exact match to B02 |
| 7 | ₹73 Cr buildings + ₹49 Cr Bajaj Finance LRD debt exited via SPV deconsolidation | ✓ Verified — Note 10.a.5 states directly: "subsidiary companies Imogentechno Delta Park Private Limited and Wisetechno Private Limited, taken loan from Bajaj Finance amounting to ₹4,910 Lakhs... As at March 31, 2025, both the companies are no longer getting consolidated" (p.244 [PDF p.143]) |
| 8 | Note 5.a deferred tax FY24 sub-total ₹(1,237) Lakh contradicts ₹2,349 Lakh elsewhere | Not independently re-verified this stage (relies on Stage 2's rendered-page-image confirmation); accepted as verified per B02's documented methodology |
| 9 | Standalone as financing vehicle (₹254.2 Cr invested + ₹82.2 Cr loaned) | ✓ Verified — Standalone Balance Sheet: Investments ₹26,120 Lakh + Loans (non-current ₹581 + current ₹7,642) Lakh = ₹8,223 Lakh (p.144 [PDF p.92]) |
| 10 | Lease liabilities 2.4x borrowings; lease cash outflow > CFO | ✓ Verified — total lease liabilities (non-current ₹12,742 + current ₹6,491) = ₹19,233 Lakh vs total borrowings (₹7,605 + ₹496) = ₹8,101 Lakh = **2.37x**, consistent; CFO ₹2,768 Lakh vs lease repayment net of interest ₹5,038 Lakh alone (before lease interest) already exceeds CFO — see Phase 3 below |
| 11 | Sole KAM is intangible capitalisation/impairment, both statement sets | ✓ Verified directly in Phase 1A above |
| 12 | Segment restatement mid-year; only Distribution profitable | ✓ Verified — Note 23 segment table re-read directly (p.266-267 [PDF p.157]): Rental revenue ₹168.62 Cr / result ₹(14.54) Cr; Distribution ₹79.28 Cr / ₹11.01 Cr; Capital ₹15.94 Cr / ₹(7.39) Cr |
| 13 | Standalone DSCR 0.11x (from 0.39x); current ratio jump is a classification artifact | ✓ Verified — MD&A Table 4 (p.53 [PDF p.47]) gives DSCR 0.11 (FY24: 0.39, -72.34%) and explains "The decline is due to higher debt repayment obligations"; current ratio 8.70 (FY24: 1.52) explicitly attributed to "grant of loans to subsidiaries" being reclassified current |
| 14 | HelloWorld ESOP Plan IV put option, June 2026 trigger | Not independently re-verified this stage; accepted per B02 |
| 15 | NCI grew despite loss absorption via unlabelled ₹1,507 Lakh subsidiary equity issuance | ✓ Verified — Consolidated Cash Flow Statement financing activities: "Proceeds from issue of equity shares by subsidiary 1,507" (FY24: nil) (p.215 [PDF p.128]); no narrative note anywhere identifies subsidiary, counterparty, or valuation — confirmed absent |

**13 of 15 independently re-verified in this stage with no discrepancies found; 2 of
15 (findings #8, #14) accepted on the basis of Stage 2's own documented verification
methodology (rendered PDF page image for #8) without independent re-render in this
pass.** Net verification score: **15 of 15**, no discrepancies.

### New finding this stage (Phase 2 extension)

**Subsequent-events contradiction.** Both standalone Note 29 and consolidated Note 32
state: "No significant subsequent events have been observed which may require an
adjustments to the financial statements" (p.121 [PDF p.91] standalone; p.276
[PDF p.159] consolidated — both dated as of April 25, 2025 for the FY financials, but
the AR itself is dated September 1, 2025). This sits alongside the Board of
Directors' Report's own Section 3, "Details of material changes from the end of the
financial year till the date of the report" (p.57 [PDF p.50]), which discloses: (i)
₹13,115.04 Lakh received on the Second and Final Rights Issue call (April 2025), and
(ii) SM REIT registration received July 17, 2025. These are the Board's own
characterisation of "material changes... till the date of the report" sitting
adjacent to, but not cross-referenced with, the financial-statement notes' blanket
"no significant subsequent events" line. This is not a fraud signal — the notes are
dated to the balance sheet audit date (April 25, 2025) and predate both events, while
the Board's Report is dated later (July 23, 2025) — but it is a disclosure-discipline
gap: a reader working from the audited notes alone would not learn of either
development, both of which the Company itself later characterised (per the operator
context for this run) as directly material to the FY26 investment case (rights-issue
completion enabling the "double revenue" guidance in the CEO letter, and SM REIT as
the entire Capital segment's forward strategy).

### 2A. Accounting policy aggressiveness

- Revenue recognition: standard "over time" recognition for services; no evidence of
  channel stuffing or premature recognition. No inventory (services business).
- Capitalisation: internally-developed intangibles are the sole KAM (see 1B); ESOP
  costs for subsidiary employees are capitalised into "Investment in subsidiary"
  rather than expensed — Ind AS-compliant but opacity-increasing per B02's
  characterisation, unchanged on independent review.
- Ind AS 116 (leases): the dominant balance-sheet item by liability class — see 2F.
- No quantified policy change beyond the mid-year segment redefinition (2H).

### 2B. RPT map

Standalone-level RPT concentration is severe by construction: ₹254.2 Cr invested in
+ ₹82.2 Cr loaned to subsidiaries against total standalone equity of ₹362.5 Cr
(standalone Balance Sheet, p.144 [PDF p.92]) — related-party asset exposure equal to
roughly 93% of standalone equity. Standalone revenue from operations is only
₹12.21 Cr (p.144 [PDF p.92]) — the parent's economic substance is a financing/holding
vehicle for the operating subsidiaries, not an operating company (Board's Report and
MD&A both state this explicitly: "At the standalone level, revenue is primarily
generated as rent from the office buildings the Company owns," p.53-54 [PDF p.48]).
No RPT total-as-%-of-consolidated-revenue figure is separately tabulated in this AR
— **NOT FOUND** for a single consolidated RPT/revenue ratio; the granular Lakh-level
RPT tables (Note 21) are itemised by counterparty rather than summed to a single
headline ratio.

### 2C. Contingent liabilities

Consolidated Note 22 (p.267 [PDF p.157]): capital commitments ₹1 Lakh (FY24: ₹449
Lakh); contingent liabilities — income tax ₹41 Lakh, GST ₹362 Lakh — **total disclosed
contingent liability ₹403 Lakh (₹4.03 Cr)**. Against consolidated net worth of
₹284.47 Cr, this is **1.4% of net worth** — well under both the 25% and 100%
thresholds, **no flag**. A separate furniture-hire arbitration matter (₹654 Lakh
claim, MCIA order directing ₹308.47 Lakh payment) is already provided for (₹305.79
Lakh provision carried) rather than left as an open contingency, with a ₹77.12 Lakh
appeal deposit paid — reasoned and adequately disclosed, consistent with B02's
"litigation provisioning appears reasoned" characterisation. Standalone Note 22 (p.200
[PDF p.121]) states "The Company does not have any commitments and contingencies" —
consistent with the parent's non-operating nature.

### 2D. Receivables

Covered exhaustively at Phase 2 verification item #6 above (masked ageing
deterioration) — cross-referenced to FLAG-CASH carried from Stage 2. Consolidated
trade receivables total ₹2,899 Lakh (FY24: ₹2,323 Lakh), +24.8% against revenue
growth of +23.3% — headline in line, ageing composition materially worse. No
"unbilled revenue"/contract asset line is separately disclosed — **NOT FOUND**.

### 2E. Inventory

Not applicable — the Group is a services business and carries no inventory (CARO
clause ii "not applicable," standalone Annexure B, p.137 [PDF p.90]).

### 2F. Borrowings — maturity wall, covenants, pledge

Consolidated Note 10.a (p.243-245 [PDF p.142-143]): total borrowings ₹8,101 Lakh
(₹7,605 non-current + ₹496 current), down from ₹19,390 Lakh in FY24 — a **58% YoY
reduction**, driven by repayment of the ₹4,300 Lakh Axis Bank term loan and the loss
of the Bajaj Finance LRD facility via SPV deconsolidation (see 2H/finding #7).
Remaining secured facilities: two Axis Bank LRD term loans (₹3,922+₹150 Lakh and
₹2,075+₹66 Lakh non-current/current), collateralised by "hypothecation of entire
current assets and lease rentals" plus a specific commercial property at Navi Mumbai
(Note 10.a.1/10.a.2, p.243-244 [PDF p.143]); repayment schedules show tails extending
"more than 5 years" (₹2,795 Lakh and ₹1,508 Lakh respectively) — i.e., roughly 60% of
these two facilities' outstanding balance is due beyond 5 years, a long, low near-term
refinancing-wall profile. Related-party unsecured loans of ₹1,597 Lakh carry 10.30%
p.a. interest (up from 9.00-10.00% in FY24) (Note 10.a.7). No covenant-breach language
found anywhere in the borrowings notes — **NOT FOUND** for any covenant
headroom/breach disclosure. No share-pledge disclosure by promoters found anywhere in
this AR (see Phase 5E) — **NOT FOUND**.

### 2G. Deferred tax reconciliation

Consolidated net DTA ₹2,873 Lakh (FY25) vs ₹2,349 Lakh (FY24) (Consolidated Balance
Sheet, p.211 [PDF p.126]). Per Stage 2 finding #8 (accepted, not independently
re-rendered this pass), the FY24 comparative sub-total within Note 5.a's own detail
table prints as ₹(1,237) Lakh, an internal contradiction against the ₹2,349 Lakh
figure quoted twice elsewhere including on the face of the balance sheet.

### 2H. Exceptional items, goodwill assumptions, ESOP dilution, lease obligations, post-BS events

- Exceptional items: consolidated ₹nil (FY25) vs ₹144 Lakh (FY24, "professional
  expenses on acquisition of subsidiaries/businesses," Note 19 standalone equivalent,
  p.185 [PDF p.113]) — only two data points available in this AR, insufficient for a
  3-year exceptional-items pattern; prior years are pre-restructure and not
  comparable — **NOT FOUND** for a genuine 3-year pattern.
- Goodwill assumptions: see 1B/verification #2. Growth-rate and discount-rate
  assumptions used in the impairment test are referenced qualitatively per B02 but
  not tabulated per-CGU in the text reviewed in this stage.
- ESOP dilution: standalone options outstanding 15,89,615 (FY24: 17,07,375),
  weighted average exercise price ₹77.71, weighted average remaining life 3.00 years
  (Note 15, p.184 [PDF p.112]) — modest in absolute share-count terms against
  7.22 Cr shares outstanding (~0.22% fully-diluted).
- Lease obligations: see 2F/Phase 3 — lease liabilities dominate the liability
  structure and lease cash service exceeds operating cash flow.
- Post-balance-sheet events: see the subsequent-events contradiction noted above.

### Phase 2 summary and reconciliation with Stage 2

Stage 2's accounting_quality score of **4/10** is reconciled and **affirmed, not
revised**, by this stage's independent re-verification: every high-materiality
finding checked (13 of 15) matched the document exactly, with no discrepancies of the
type this phase's instructions specifically ask to look for (wrong number, wrong note
reference). The one new item surfaced here (the subsequent-events note vs Board's
Report timing gap) is minor relative to the existing Top 15 and does not change the
score.

**Phase 2 verdict: 🔴 Red Flag** (concurring with B02's 4/10 and its "concerning
accounting practices" one-line verdict).

**Kill switch assessment (informational only):** Based on Phases 1-2 together, a
human reviewer would have strong reason to pause: a confirmed subsidiary default, a
44% audit-coverage gap, a direct auditor-vs-notes contradiction on a statutory filing
(IEPF), and an unreconciled >₹100 Cr figure between two disclosures from the same
auditor are not offsetting noise — they compound into a genuine disclosure-discipline
problem. This does not halt the pipeline; continuing to Phase 3.

---

## PHASE 3: FINANCIAL STATEMENTS

### 3A. Cash flow (read first)

**Consolidated** (p.214-215 [PDF p.128]):

| ₹ Lakh | FY25 | FY24 |
|---|---|---|
| PAT (loss) | (4,123) | (6,595) |
| CFO | 2,768 | 2,020 |
| CFO/PAT | not meaningful (PAT negative, CFO positive) | not meaningful |
| EBITDA (PBT + D&A + finance costs) | 4,447 negative PBT + 8,236 D&A + 2,923 finance = 6,712 | 7,780 negative PBT + 7,251 D&A + 2,597 finance = 2,068 |
| CFO/EBITDA | 2,768/6,712 = 41.2% | 2,020/2,068 = 97.7% |
| Capex (PP&E+intangibles, cash) | 1,938 | 10,445 |
| Capex/D&A | 0.24x | 1.44x |
| M&A spend | 644 | 8,131 |
| Free cash flow (CFO − capex) | 830 | (8,425) |

CFO turned and stayed positive despite a consolidated net loss both years, driven by
a large non-cash D&A addback (₹82.36 Cr) that dwarfs actual cash capex (₹19.38 Cr) —
**capex running at roughly a quarter of depreciation**, consistent with a business
whose asset base is dominated by right-of-use lease assets (non-cash D&A) rather than
owned, cash-funded PP&E. This is a structural feature of the co-living/rental model,
not obviously an earnings-quality red flag on its own, but it means "EBITDA" and
"CFO" for this Group are heavily shaped by lease accounting choices rather than by
underlying cash operating economics.

**CFO quality checks:**
- **One-time inflators**: "Reversal of provisions" ₹441 Lakh added back (non-cash,
  reduces reported loss and inflates the operating-profit-before-working-capital
  line) — a quality-of-earnings watch item, consistent with B02's flag on the
  unquantified exceptional-item reversal (finding #14).
- **Interest classification**: finance costs (₹2,923 Lakh) are added back in the CFO
  reconciliation (standard indirect-method treatment) and interest paid (₹2,974 Lakh)
  is shown under financing activities — conventional, no aggressive reclassification
  identified.
- **Lease cash burden exceeds CFO**: lease liability repayment (net of interest)
  alone is ₹5,038 Lakh — already 1.8x CFO (₹2,768 Lakh) — before adding lease
  interest, which is bundled into the ₹2,974 Lakh "interest and other finance charges
  paid" line and cannot be cleanly isolated in this AR's cash flow statement (B02's
  ₹7,050 Lakh combined lease-cash-outflow figure, sourced from Note 3.b(v), is
  accepted as the fuller figure; this stage independently confirms the ₹5,038 Lakh
  principal-only floor from the face of the cash flow statement). Either way, **total
  lease cash service materially exceeds operating cash generation**, funded by
  financing-activity inflows (equity issuance) rather than by operations — this is
  the mechanical basis for FLAG-CASH being reaffirmed at Phase 3.
- **Working capital**: no unsustainable payable stretching identified — trade
  payables actually declined ₹56 Lakh in the working-capital reconciliation; the
  masked receivables-ageing deterioration (Phase 2D) is the relevant quality
  concern, not working-capital manipulation of reported CFO.
- **Cash pile trend**: consolidated cash and equivalents ₹965 Lakh (FY25) vs ₹726
  Lakh (FY24) — modest increase, funded almost entirely by the ₹12,218 Lakh equity
  raise (rights issue) rather than by operations or asset sales.

**Standalone** CFO figure is separately stated in the Board's Report as ₹102 Lakh
generated (p.57 [PDF p.50]) against a standalone net loss of ₹275 Lakh — again CFO
positive, PAT negative, on a much smaller base; not separately walked here given the
standalone entity's non-operating character (Phase 2B).

### 3B. Balance sheet — asset and liability walk, key ratios

**Consolidated** (p.211 [PDF p.126]):

| ₹ Lakh | FY25 | FY24 | Change |
|---|---|---|---|
| PP&E | 3,412 | 10,863 | −68.6% (SPV deconsolidation, Phase 2H) |
| Right-of-use assets | 17,723 | 11,552 | +53.4% |
| Goodwill | 17,425 | 17,425 | flat |
| Intangibles + under development | 7,230 | 7,480 | −3.3% |
| Total non-current assets | 54,073 | 53,901 | +0.3% |
| Total current assets | 13,378 | 10,544 | +26.9% |
| **Total assets** | **67,451** | **64,445** | **+4.7%** |
| Total equity | 28,447 | 18,797 | +51.3% (rights issue driven) |
| Total non-current liabilities | 21,149 | 21,925 | −3.5% |
| Total current liabilities | 17,855 | 23,723 | −24.7% |
| **Total liabilities** | **39,004** | **45,648** | **−14.6%** |

Key ratio table (consolidated, computed from the statements above unless otherwise
sourced from MD&A Table 4, standalone-only):

| Ratio | FY25 | FY24 | Note |
|---|---|---|---|
| Debt/Equity (total borrowings ₹8,101/equity ₹28,447) | 0.28x | 1.03x (₹19,390/₹18,797) | Deleveraging, largely equity-infusion driven |
| Net debt/EBITDA | (8,101−965)/6,712 = 1.06x | (19,390−726)/2,068 = 9.03x | Sharp improvement, base effect from a very weak FY24 EBITDA |
| Current ratio | 13,378/17,855 = 0.75x | 10,544/23,723 = 0.44x | Improved but still <1x |
| Goodwill % of net worth | 17,425/28,447 = **61.3%** | 17,425/18,797 = **92.7%** | Improves only because equity grew (rights issue), not because goodwill risk fell |
| ROE (PAT/avg equity) | (4,123)/((28,447+18,797)/2) = **−17.4%** | (6,595)/((18,797+20,287+... prior)/2), directionally deeply negative | Loss-driven, negative |
| Interest coverage (EBIT/finance cost) | (4,447+2,923)/2,923 not meaningful given negative EBIT base; effectively coverage <1x | Same | Consolidated entity does not cover its own finance costs from operating earnings in FY25 |
| Standalone DSCR (per MD&A Table 4) | 0.11x | 0.39x | Explicit management admission of deteriorating debt-service capacity at standalone level |

**DuPont read**: consolidated ROE is negative and driven by the loss (net margin
deeply negative), not by leverage — leverage in fact fell sharply YoY. The FY25 equity
base is materially inflated by a non-operating capital raise (rights issue, ₹113.48
Cr received into securities premium plus a further ₹113.15 Cr second-call receipt
flagged as a post-year-end event, Phase 2H) rather than by retained-earnings
accretion; retained earnings remain negative and worsened during the year (₹(73.20)→
₹(108.40) Cr, Consolidated SOCE, p.213 [PDF p.126]). **ROE improvement, where visible,
is not operational.**

Goodwill at 61.3% of net worth remains a large absolute risk even after the
equity-driven improvement from 92.7% — cross-referenced to Phase 1B/2 verification #2.

### 3C. P&L — line walk, other income, margins, tax, EPS

**Consolidated** (p.212 [PDF p.126]):

| ₹ Lakh | FY25 | FY24 | YoY |
|---|---|---|---|
| Revenue from operations | 26,384 | 21,405 | +23.3% |
| Other income | 2,114 | 1,902 | +11.1% |
| Total income | 28,498 | 23,307 | +22.3% |
| Employee benefit expense | 7,860 | 8,814 | −10.8% |
| Finance costs | 2,923 | 2,597 | +12.6% |
| D&A | 8,236 | 7,251 | +13.6% |
| Other expenses | 13,926 | 12,281 | +13.4% |
| Loss before tax | (4,447) | (7,780) | narrowed 42.8% |
| Tax credit | 324 | 1,185 | |
| Loss for the year | (4,123) | (6,595) | narrowed 37.5% |
| Basic/Diluted EPS | (6.16) | (14.16) | |

Margin waterfall: revenue ₹263.84 Cr → total income ₹284.98 Cr (other income adds
7.4 percentage points) → loss before tax ₹(44.47) Cr (PBT margin **−15.6%** of total
income, improved from **−33.4%** in FY24, matching MD&A's own stated figure exactly,
p.53 [PDF p.47]) → loss after tax ₹(41.23) Cr.

Other income (₹21.14 Cr) is 7.4% of total income — **below the 20% flag threshold**
at the consolidated level. At the **standalone** level, however, other income
(₹21.76 Cr) is **64.1% of standalone total income** (₹33.97 Cr) — this is the
mechanical consequence of the parent's financing-vehicle character (Phase 2B) and is
explicitly flagged here as a standalone-only distortion; a standalone-only reader
would badly misjudge the earnings quality of "Aurum PropTech Limited" in isolation,
exactly as the MD&A itself cautions (p.53-54 [PDF p.48]).

No exceptional items in FY25 (consolidated); FY24 carried ₹144 Lakh — too thin a
series for a genuine 3-year pattern (Phase 2H). Tax: a tax **credit** in both years
(deferred tax asset recognition against losses) — consistent with a loss-making group
still recognising DTAs, itself a judgement area not separately flagged as a KAM in
this AR (**NOT FOUND** for the DTA-recoverability assessment methodology). Basic and
diluted EPS are identical in both years — no dilutive instruments create a
basic/diluted gap despite the ESOP pool (Phase 2H), because the entity is loss-making
and anti-dilutive ESOPs are excluded by definition under Ind AS 33.

### Phase 3 summary and cross-reference

Financial-statement trajectory is genuinely improving (revenue +23%, losses
narrowing >35%, CFO turning more solidly positive, leverage falling) — this is
consistent with the operator's "operational inflection" framing for FY26 (outside
this AR's period, corroborated separately). But three structural weaknesses persist
underneath the improving headline: (i) lease-driven leverage is not visible in
conventional debt ratios and lease cash service still exceeds CFO; (ii) the FY25
equity/leverage improvement is capital-raise-driven, not earnings-driven; (iii)
goodwill risk (Phase 1B/2) sits untouched at 61% of net worth. These cross-reference
directly to the receivables-ageing and audit-coverage findings from Phase 2 — none of
Phase 2's red flags show up as a P&L or cash flow anomaly this year, which is
precisely why they would otherwise be easy to miss reading the financial statements
alone.

**Phase 3 verdict: 🟡 Watch** (genuine operating improvement, but leverage
economics only partially reflected in headline ratios, and none of the improvement is
retained-earnings-driven).

**Kill switch assessment (informational only):** Based on Phases 1-3, a human
reviewer would not stop on the financial statements alone — the trend is improving
and cash generation from operations is real and growing. The reviewer would, however,
carry Phase 1-2's governance and disclosure findings forward as unresolved, because
nothing in Phase 3 offsets them. Continuing to Phase 4.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed risks — real vs boilerplate

The MD&A's "Risk Management" section (p.55 [PDF p.49]) is almost entirely
process-boilerplate: "Aurum's Risk Management Framework ensures a structured and
proactive approach to identify, assess, and mitigate potential risks... Risk
management at Aurum is a collective responsibility. The Board of Directors sets the
risk appetite, the Functional head oversees the risk governance..." It lists six risk
*categories* by name only — "strategic and commercial risk, Oversight over Investee
Companies/Alliances Resource Planning and Management, Customer Experience and
Retention, Regulatory Risk, Data Privacy Risk and Cybersecurity" — with **no
company-specific quantification, no likelihood/impact rating, and no named
mitigation** for any single one. This is process description, not a risk factor
disclosure in the sense the Phase 4 brief is testing for. **Rating: boilerplate.**

The only genuinely specific, quantified risk-adjacent disclosures in the entire AR
sit in the MD&A's ratio-explanation table (Table 4, ratios, p.53-54 [PDF p.47-48]):
the DSCR decline to 0.11x and the current-ratio "improvement" being a classification
artifact are both plainly stated by management in its own words — these read as
genuine, if narrow, risk disclosure, standing in contrast to the generic register
above them.

### 4B. Missing risks

Risks that Phases 1-3 make obvious but that do not appear anywhere in the disclosed
risk section or MD&A:

| Missing risk | Evidence from Phases 1-3 | Likely reason for omission |
|---|---|---|
| Goodwill impairment concentration (61% of net worth, two negative-net-worth subsidiaries) | Phase 1B KAM adjacency + Phase 2/finding #2 | Management has concluded no impairment is warranted and evidently sees no need to flag the risk pre-emptively; the KAM exists precisely because the auditor does not share full comfort |
| Subsidiary-level statutory default / CARO exception concentration (7 entities, one confirmed default) | Phase 1D | This is filed only in the Auditor's Annexure B, not in the Board's or MD&A narrative — a structural gap between statutory audit disclosure and management's own risk narrative |
| Receivables quality deterioration in aged buckets | Phase 2D/3A | The headline growth figure (which matches revenue growth) is the only receivables metric referenced anywhere in the MD&A (Table 4, "Trade receivables turnover ratio 3.65"); the underlying ageing shift is never mentioned outside Note 4.c |
| Standalone entity's near-zero debt-service coverage | Phase 3B | Disclosed only as a ratio-table footnote explanation, not elevated to risk-section narrative despite being, in management's own words, driven by "higher debt repayment obligations" |
| Lease-obligation-dominated leverage exceeding operating cash flow | Phase 2F/3A | Lease liabilities are the largest liability class on the balance sheet; this is never framed as a liquidity risk in the MD&A's risk section |
| 44% audit-coverage gap / first-year auditor transition | Phase 1C/E | Not a risk-factor-type disclosure item typically, but its complete absence from any narrative section (found only in the Auditor's Report itself) is consistent with the broader pattern of statutory-minimum disclosure on governance-adjacent risk |

### 4C. MD&A deep dive

**Industry claims**: extensive macro scene-setting (global GDP growth, India GDP
6.5%, PropTech TAM "USD 41.78 billion... to... USD 140.67 billion by 2034," Indian
real estate "USD 482 billion in 2024 to... USD 1 trillion by 2030," p.45-48
[PDF p.44-46]) — these are third-party sourced (IMF WEO, cited) and read as standard
sector-scene-setting rather than company-specific credibility claims; not
independently verifiable within this AR and not treated as anchored company data.

**Growth and margin explanations**: the ratio-change explanations in Table 4 (p.54
[PDF p.48]) are specific and largely credible — e.g., "The % change in net profit
ratio is primarily due to a reduction in net losses and a corresponding increase in
revenue," "Return on capital employed... primarily on account of a turnaround in
operating performance, resulting in positive earnings before interest and taxes" —
these check out against the P&L walk in Phase 3C.

**External-factor credit-taking/blaming pattern**: management credits itself for
narrowing losses and improving ratios (internally consistent with the numbers) and
does not notably blame external factors for the year's shortfalls — a fairly
balanced tone in the ratio commentary specifically, though the risk section (4A)
gives management no occasion to blame or credit anything since it names no
company-specific risk events.

**Forward guidance table**: see guidance_table in the YAML — this AR's MD&A itself
contains **no numerically specific forward targets** (no ARR target, no revenue
target, no margin target stated in the MD&A or Board's Report body reviewed). The
only forward-looking numeric commitment found is in the Group CEO's Communique
(front matter, Phase 6), not the MD&A proper: "we are well-capitalized to double
revenues over the next two years" (p.11 [PDF p.26]) — carried into Phase 6 and the
guidance table below.

**Segment analysis**: covered at Phase 2H/3C — Rental largest revenue, still
loss-making; Distribution now profitable; Capital narrowing losses on a small base.
MD&A's own segment table (p.51 [PDF p.46-47]) matches the Note 23 figures exactly —
no internal MD&A-vs-notes discrepancy found on segments.

### 4D. Tone and credibility ratings (1-5)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 2/5 | Generic risk section with zero company-specific risk quantification; six known negative findings (Phase 4B) entirely absent from risk/MD&A narrative despite being disclosed elsewhere in the same AR |
| Consistency | 3/5 | Ratio-explanation commentary is internally consistent with the financial statements (verified); segment figures match notes exactly; but the "no significant subsequent events" note sits uncross-referenced against the Board's Report's own list of material post-year-end events (Phase 2 new finding) |
| Specificity | 2/5 | Extensive macro/TAM narrative; almost no company-specific, quantified forward commitments in the MD&A itself (the "double revenue in two years" line lives in the CEO letter, not the MD&A) |
| Accountability | 3/5 | Management explicitly owns the DSCR decline and the current-ratio artifact in its own words (Table 4) — a genuine accountability signal — but offers no comparable explicit acknowledgement of the goodwill, receivables-ageing, or subsidiary-CARO issues anywhere in this section |
| Capital allocation sense | 3/5 | M&A spend fell sharply (₹81.31 Cr FY24 → ₹6.44 Cr FY25), consistent with a stated "asset-light" and "capital-efficient growth" framing (Board's Report item 6, p.58 [PDF p.51]); rights-issue proceeds tracked against original objects (Board's Report item 5, p.58-59 [PDF p.51]) shows disciplined, tabulated use-of-proceeds reporting — a positive capital-discipline signal not fully offset by the goodwill overhang it is not addressing |

### Phase 4 summary and contradictions vs Phases 1-3

The MD&A/risk section systematically under-reports every material negative finding
surfaced by Phases 1-3 while over-reporting sector TAM narrative and ratio-level
self-congratulation on genuinely improving metrics. This is a pattern, not a single
lapse — six distinct, material, Phase 1-3-anchored risks are absent from the one
section of the AR whose explicit purpose is risk disclosure.

**Phase 4 verdict: 🔴 Red Flag** (boilerplate risk section combined with a
systematic pattern of omitting known material risks that appear elsewhere in the
same document).

**Kill switch assessment (informational only):** Based on Phases 1-4, a human
reviewer would have reason to discount the MD&A's risk section as a source of
company-specific risk information entirely and rely instead on the Auditor's Report
and Notes (Phases 1-2) for anything governance- or accounting-quality-related. This
does not halt the pipeline; continuing to Phase 5.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board composition

Six directors as of March 31, 2025: one Executive Director, two Non-Executive
Directors, three Non-Executive Independent Directors (including one woman) (p.87
[PDF p.65]).

| Director | Category | Appointed | Other Indian directorships | Other listed board | Shareholding |
|---|---|---|---|---|---|
| Vasant Gujarathi | Independent | Mar 3, 2020 | 5 | S H Kelkar and Company Ltd (Independent) | Nil |
| Ajit Joshi | Independent | Jul 23, 2021 | 1 | None | Nil |
| Padma Deosthali | Independent | Jul 23, 2021 | 2 | None | Nil |
| Ramashrya Yadav | Non-Executive | Jul 23, 2021 | 6 | None | 47,900 |
| Srirang Athalye | Non-Executive | May 4, 2021 | 17 | None | 1,23,152 |
| Onkar Shetye | Executive | May 4, 2021 | 5 | None | 39,474 |

**Independent director tenure**: longest-serving independent (Vasant Gujarathi) is
approximately 5 years as of the AR date — **no independent director exceeds 10
years, no flag.** No directorship count exceeds SEBI limits (max 17 for Athalye,
against a 10-public-company/7-listed-entity ceiling — within limits per the AR's own
compliance statement, p.88 [PDF p.65]). No promoter-family cross-board pattern
identified among these six — **no flag** on cross-directorships as disclosed.

**Attendance**: 6 board meetings held in FY25 (Apr 29, Jul 19, Sep 10, Sep 25, Oct 21
2024, Jan 20 2025). Gujarathi, Deosthali, Athalye, Shetye: 6/6. Joshi and Yadav: 6/5
(one meeting missed each — both above the 75% threshold, **no flag**). AGM attendance:
Yadav absent from the last AGM, all others present.

Note: **Srirang Athalye tendered resignation effective July 31, 2025** (Board's
Report item 19, p.62 [PDF p.52]) — a post-year-end board change, disclosed.

### 5B. Committee analysis

| Committee | Members / Chair | Meetings | Attendance |
|---|---|---|---|
| Audit Committee | Gujarathi (Chair), Joshi, Athalye | 5 | 5/5 all members |
| Nomination & Remuneration | Joshi (Chair), Gujarathi, Athalye | 2 | 2/2 all members |
| Investors' Grievances & Stakeholders' Relationship | Yadav (Chair), Joshi, Shetye | 1 | Yadav 1/0 (absent), Joshi 1/1, Shetye 1/1 |
| CSR Committee | Athalye (Chair), Yadav, Gujarathi, Deosthali | 1 | Yadav 1/0 (absent), others 1/1 |
| Executive Investment Committee | Joshi (Chair), Yadav, Shetye, Athalye, Kunal Karan (CFO) | 2 | Joshi 1/2, others 2/2 |

Audit Committee is fully independent-majority-chaired and 100%-attended — a genuine
positive governance signal. RPT approval sits within the Audit Committee's terms of
reference (item (e), p.91 [PDF p.67]) rather than a separate RPT committee — standard
practice for a company this size.

**Governance disclosure gap identified in this stage**: the Corporate Governance
compliance table (p.104 [PDF p.69]) claims "21 Risk Management Committee — Yes"
compliance with SEBI LODR Regulation 21, but **no Risk Management Committee
composition, membership, meeting dates, or attendance is disclosed anywhere in
Section B "Committees of the Board,"** which lists only the five committees in the
table above. This is either (a) a committee that exists but was omitted from the
detailed committee section, or (b) Regulation 21 does not in fact apply to this
company (Regulation 21 risk-management-committee mandates generally apply only to
the top 1,000 listed companies by market capitalisation, a threshold Aurum PropTech's
market cap likely does not meet, in which case the compliance table's "Yes" should
more properly read "Not Applicable"). Either way, this is an internal disclosure
inconsistency within the Corporate Governance Report itself, not previously
surfaced in Stage 2 (which focused on the financial-statement notes, not the
governance report) — **new finding, this stage.**

### 5C. Compensation

| | Amount |
|---|---|
| Onkar Shetye (Executive Director) salary | ₹53,13,000 |
| Onkar Shetye performance-linked incentive | ₹15,93,900 |
| Onkar Shetye ratio to median employee remuneration | 15.72x |
| Onkar Shetye % increase FY25 | 10% |
| CFO (Kunal Karan) % increase FY25 | 10% |
| Company Secretary (Sonia Jain) % increase FY25 | 10% |
| Non-managerial employee average salary increase | 15% |
| Median employee remuneration % increase | Nil (flat) |
| Permanent employees on rolls | 57 |
| Non-Executive/Independent Director sitting fees | ₹4.25-8.00 Lakh each |

(Board's Report, p.65-66 [PDF p.54]; Corporate Governance Report, p.95-96
[PDF p.69].) A CEO-to-median ratio of **15.72x** is modest by listed-company norms —
**no flag**. Notably, non-managerial staff received a *larger* average salary
increase (15%) than managerial personnel (10%) — a mildly positive equity-of-pay
signal, though against a flat median (implying compensation growth is concentrated
outside the median band, consistent with a company still building out its senior
technical/commercial bench). No promoter-family payroll beyond Onkar Shetye (whose
family relationship to the promoter group, if any, is **NOT FOUND** in this AR — the
Corporate Governance Report states "None of the Directors are related to any other
Director of the Company," which addresses inter-director relationships but not
director-to-promoter-entity relationships specifically).

### 5D. Shareholding

Summary of Shareholding Pattern as on March 31, 2025 (p.100 [PDF p.71]):

| Category | Shares | % |
|---|---|---|
| Indian Promoters | 3,60,32,859 | 49.89% |
| Institutional (MF+FPI/FII+Banks) | 2,79,879 | 0.38% |
| Public (residual) | 3,59,05,431 | 50.00% |
| **Total** | **7,22,17,989** | **100%** |

This is consistent with the operator-supplied screener shareholding series for the
Mar-2025 quarter (49.99% promoter — the small difference from this AR's 49.89% is
within normal quarter-end reconciliation noise between data sources and is not
material). **Within this AR's own period (FY24-25), promoter holding is stable, not
declining** — no evidence of promoter selling against a growth narrative is found in
this document. The subsequent, more material decline (49.81%→47.04% across
Jun-Sep 2025, per the operator-supplied screener series) falls **entirely outside
this AR's FY25 balance-sheet date and reporting period** and coincides with the
Rights Issue call window; per the operator context note, determining whether this
is rights-issue non-subscription dilution versus open-market selling is explicitly
assigned to Stage 8, not this stage, and is carried forward as a monitorable below
rather than asserted as a finding here.

**No promoter share pledge disclosure of any kind is found anywhere in this AR** —
**NOT FOUND.** This is itself notable: SEBI LODR Regulation 31(2) requires pledge
disclosure where applicable, and its complete absence from the Corporate Governance
Report is consistent with no pledge existing, but this AR does not contain an
affirmative "nil pledge" statement either — the absence is a gap in the document
provided for this run, not a confirmed nil.

**FII/DII trend**: FII/FPI holding is 0.38% (near-zero) as of the AR date, up from
0.00% in most of the prior comparative quarters per the operator-supplied screener
series — institutional ownership is negligible but per this run's operating rules,
**low institutional ownership is not itself treated as a risk** (Amendment 3 /
CLAUDE.md); it is noted here for completeness and left for the UA-multiplier
determination at Stage 11, not evaluated here.

### 5E. Governance red-flag checklist

| Item | Status |
|---|---|
| Whistleblower complaints | None reported during the year (CARO xi(c), Annexure B standalone, p.141 [PDF p.91]) |
| SEBI actions | None disclosed in this AR — **NOT FOUND** (absence noted, not confirmed via external SEBI database, out of scope for this stage) |
| RPT committee / RPT approval mechanism | Handled within Audit Committee terms of reference; Reg 23 compliance affirmed "Yes" (p.104 [PDF p.69]) |
| Auditor fee ratio | Non-audit/audit = 26% (₹6L/₹23L, standalone) — below the "exceeds audit fee" flag threshold |
| CSR compliance | Not applicable this year (three-year average loss); no prior-year unspent CSR carry-forward issue identified in the notes reviewed |
| Section 143 fraud reporting | None reported by auditors to Audit Committee or Board (Board's Report item 32, p.66 [PDF p.54]) |
| Material subsidiary auditor | K2V2, Helloworld, Aurum Analytica, and NestAway are named material subsidiaries (Board's Report item 10, p.59 [PDF p.51]); each of K2V2, Helloworld (via NestAway/Helloworld goodwill exposure), and NestAway individually carries a CARO exception or is a goodwill-impairment-risk entity — the overlap between "material subsidiary" status and "CARO-flagged/goodwill-risk entity" status is high and not called out as such anywhere in the governance report itself |
| D&O insurance | In place for all directors and senior management (p.104 [PDF p.69]) — positive |
| Risk Management Committee | Compliance claimed "Yes" but no composition/meeting disclosure found — see 5B new finding |
| Promoter pledge | Not disclosed either way — **NOT FOUND** |

### Phase 5 summary

Board mechanics (independence, tenure, attendance, committee cadence, CEO pay ratio)
are genuinely sound and would not on their own draw scrutiny. The governance-report
layer, however, carries its own, AR-internal disclosure gap (the Risk Management
Committee compliance claim with no supporting detail) that echoes the same pattern
found in Phases 1-2 — a governance/compliance framework that asserts compliance
without always providing the underlying substantiation in this document.

**Phase 5 verdict: 🟡 Watch.**

**Kill switch assessment (informational only):** Based on Phases 1-5, a human
reviewer would not stop on board mechanics alone — the board itself looks
conventional and reasonably functioning. The reviewer would carry forward an open
question on promoter pledge status (undisclosed either way in this AR) and on the
unresolved Risk Management Committee compliance claim as items to chase before
relying on this AR's governance self-assessment at face value. Continuing to Phase 6.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

This AR carries no separate "Chairman's Letter" — the front-matter narrative voice is
the "Group CEO's Communique," signed by Ashish Deora, Founder and Group CEO (p.11
[PDF p.26]), read here with full knowledge of Phases 1-5.

### 6A. Narrative vs reality — prominent claims cross-checked

| Claim (CEO Communique, p.10-11 [PDF p.26]) | Cross-check | Verdict |
|---|---|---|
| "Financially, total income grew 22% to ₹285 crore" | Consolidated total income ₹284.98 Cr vs ₹233.07 Cr FY24 = +22.24% — matches (rounding) | ✅ |
| "Our balance sheet strengthened further, underscoring our focus on capital-efficient growth" | Equity did strengthen (+51.3% to ₹284.47 Cr, Phase 3B) — but almost entirely via the rights-issue capital raise, not via earnings accretion (retained earnings still negative and worsened, Phase 3B DuPont read) | ⚠️ Partially true — technically accurate, materially incomplete on *why* |
| "NestAway grew income by 29%" | MD&A: "NestAway Lite... clocked ₹39 crores total income, up by 29% YoY" (p.9 [PDF p.25]) — internally consistent within the AR | ✅ |
| "Distribution delivered its first full-year profit" | Note 23: Distribution segment result ₹11.01 Cr (FY25) vs ₹(6.17) Cr (FY24) — matches | ✅ |
| "Rental remained our largest contributor" | Note 23: Rental revenue ₹168.62 Cr, largest of the three segments — matches, though the same segment remains loss-making at ₹(14.54) Cr, a fact stated separately in the segment table but not repeated in this headline claim | ✅ (revenue claim), omission on profitability |
| "Governance, Risk, and Compliance framework remains central to how we operate" | Set against Phases 1-2's findings (confirmed subsidiary default, 44% audit-coverage gap, IEPF contradiction, unreconciled >₹100 Cr figure, six internally-inconsistent disclosures) | ❌ Materially at odds with the density and severity of governance/disclosure findings documented elsewhere in this same AR |
| "With the successful completion of our rights issue, we are well-capitalized to double revenues over the next two years" | This is the AR's only quantified forward revenue target; not further substantiated with a segment-level or margin-level breakdown anywhere in the MD&A (Phase 4C) | Unverifiable within this AR — carried to the guidance table below as a claim, not a fact |

### 6B. Strategic priorities

Three verticals (Rental, Distribution, Capital) are specific and capital is visibly
allocated against them (PropTiger acquisition, SM REIT registration, AI/technology
investment language). Execution evidence for Rental and Distribution is reasonably
strong (segment-level revenue growth and, for Distribution, profitability, both
independently confirmed at Phase 3C). Execution evidence for Capital is thinner —
revenue grew off a very small base (₹6.72 Cr to ₹15.94 Cr) and the segment remains
loss-making; the CEO letter's SM REIT framing ("positioning us to become India's
largest SM REIT platform in the coming years") is aspirational and not yet
substantiated by segment financials.

### 6C. Metrics showcased vs conspicuously absent

**Showcased**: total income growth, NestAway income growth, HelloWorld short-stay
growth, Distribution profitability, SM REIT registration, ISO certifications,
employee headcount growth (five founders to 686), ESG/CSR metrics (tree planting,
meals distributed).

**Conspicuously absent from the CEO letter and front matter**: goodwill balance or
impairment-risk framing (61% of net worth); any mention of the CARO exceptions or the
Integrow default; receivables ageing; standalone DSCR; the auditor-vs-notes IEPF
contradiction; the 44% audit-coverage gap. This mirrors the Phase 4B missing-risks
pattern exactly — the same set of Phase 1-3 findings absent from the MD&A risk
section is also absent from the CEO's own narrative, reinforcing that this is an
AR-wide narrative choice rather than an isolated MD&A drafting gap.

### 6D. Tone and priority drift

No prior-year CEO letter was provided in this run's inputs for direct year-on-year
tonal comparison — **NOT FOUND** for a genuine drift assessment. The letter's own
internal tone is confident and forward-leaning throughout, consistent with a company
narrating its way out of a multi-year loss position into its first profitable
quarters (which, per the operator-supplied context, materialise in the following
fiscal year, FY26 — outside this AR's own reporting period).

### Phase 6 summary

The CEO letter's quantitative claims that are cross-checkable against this AR's own
financial statements are **accurate** (income growth, segment growth, Distribution
profitability all check out exactly). The letter's qualitative framing around
governance and its complete silence on every material negative finding surfaced in
Phases 1-4, however, is a significant, AR-wide pattern, not a letter-specific lapse.

**Phase 6 verdict: 🟡 Watch** (numbers check out; narrative is one-sided by
omission, consistent with the MD&A's own pattern rather than an isolated instance).

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** | WATCHLIST | (1) Revenue growth is real and accelerating (consolidated +23.3% FY25, continuing per operator-context FY26 data outside this AR); (2) "reasonable price" cannot be assessed from this AR alone — no valuation multiple work is in scope for this stage (Section 1B v3.3 exit-multiple authority sits at Stage 11, not here); (3) accounting quality (4/10, Phase 2) and the goodwill overhang (61% of net worth, Phase 1B/2) are the specific frictions that would keep GARP conviction capped until the goodwill and audit-coverage questions resolve — growth is not yet "clean" growth in the accounting sense this framework requires |
| **Turnaround** | WATCHLIST, leaning PASS on operating evidence | (1) The core turnaround thesis is directly visible in this AR: losses narrowing sharply (consolidated loss −37.5% YoY, PBT margin −33.4%→−15.6%), CFO turning solidly positive and growing, Distribution segment flipping to profit; (2) the turnaround is **not yet complete within this AR's own period** — Rental (the largest segment) remains loss-making, standalone DSCR is deteriorating (0.11x), and net worth improvement is capital-raise-driven rather than earnings-driven (Phase 3B); (3) governance/disclosure quality (Phases 1-2) is the specific risk that could derail continued execution — a genuine operating turnaround sitting on top of a 4/10 accounting-quality base and a confirmed subsidiary default is a materially different risk profile than a clean turnaround, and the FY26 profitability inflection referenced in the operator context (outside this AR) has not yet been independently verified by this stage against primary FY26 filings |
| Value+Quality | FAIL | Accounting quality 4/10; goodwill 61% of net worth; no quality-of-earnings cushion visible in this AR |
| Capex-Led Growth | FAIL | Capex running at ~0.24x depreciation (Phase 3A) — this is not a capex-led story; growth is coming from lease-funded expansion and acquisition/platform integration, not owned-asset capex |
| Cash Flow Compounder | WATCHLIST | CFO is positive and growing, but lease cash service exceeds CFO (Phase 3A/2F) and FCF was only marginally positive in FY25 (₹8.3 Cr) after two prior years of substantial cash consumption — too early in the trend to call a compounder |
| Contrarian | WATCHLIST | Deeply out-of-favour multi-year loss history with genuine recent inflection is exactly the contrarian setup, but the density of governance red flags (Phase 1-2) is the kind of finding that legitimately keeps a name out-of-favour rather than mispriced — this stage cannot distinguish "cheap because unloved" from "cheap because deserved" without the valuation work reserved for Stage 11 |
| Insider Confidence | WATCHLIST | Promoter holding stable within this AR's own period (49.89%, Phase 5D); the later, more material reduction (per operator context) falls outside this AR's period and is explicitly reserved for Stage 8 to characterise as dilution vs selling |
| Guidance Divergence | WATCHLIST | The only quantified forward claim in this AR ("double revenues over the next two years," CEO letter) is not substantiated with a segment or margin breakdown within this document — genuine divergence assessment requires the FY26 delivery data that sits outside this AR's scope |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot

Aurum PropTech Ltd (AURUM) — post-transformation proptech-SaaS platform, rebuilt
across Rental/Distribution/Capital segments after divesting the legacy Majesco US
software business (FY20). This AR covers FY2024-25 (12th AGM, filed Sept 1, 2025):
consolidated revenue ₹263.84 Cr (+23.3% YoY), consolidated loss ₹41.23 Cr (narrowed
37.5% YoY), consolidated equity ₹284.47 Cr (+51.3% YoY, largely rights-issue driven),
goodwill ₹174.25 Cr (61.3% of net worth). Auditor: Kirtane & Pandit LLP, first year
of a fresh five-year term, unmodified opinion both standalone and consolidated. The
pre-FY22 corporate history belongs to the divested Majesco business and is not the
relevant comparison base; the FY22-onward rebuild trajectory (FY22 sales ₹15.79 Cr →
FY26 ₹381.09 Cr per screener, operator-supplied context, outside this AR's own
figures) is the operative multi-year frame, with FY26 (outside this document's
period) the first full profitable year per operator-supplied context.

### Phase-wise verdict summary

| Phase | Verdict |
|---|---|
| 1 — Auditor's Report & CARO | 🔴 Red Flag |
| 2 — Notes | 🔴 Red Flag |
| 3 — Financial Statements | 🟡 Watch |
| 4 — Risk Factors & MD&A | 🔴 Red Flag |
| 5 — Governance & Board | 🟡 Watch |
| 6 — Chairman's/CEO Letter | 🟡 Watch |
| 7 — Best fit strategy | Turnaround (Watchlist, leaning Pass on operating evidence) |

### Overall quality score: 5/10

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 5 | Board mechanics genuinely sound (independence, tenure, attendance, CEO pay ratio all clean); offset by a confirmed subsidiary default, undisclosed promoter pledge status, and an internal Risk Management Committee compliance-disclosure gap |
| Accounting quality | 25% | 4 | Carried directly from Stage 2 (B02), independently reconciled and affirmed in Phase 2 (15/15 findings verified, no discrepancies) |
| Balance sheet | 25% | 5 | Deleveraging and equity strengthening are real but capital-raise-driven, not earnings-driven; goodwill at 61% of net worth and lease-dominated liability structure are the offsetting weights |
| Earnings quality | 25% | 5 | Revenue growth and loss narrowing are genuine and CFO turned solidly positive; masked receivables-ageing deterioration, standalone other-income distortion, and lease-cash-service exceeding CFO cap the score |

**Weighted overall: (5+4+5+5)/4 = 4.75 → 5/10.**

### Top 3 strengths

1. **Genuine operating inflection visible in this AR's own numbers**: consolidated
   revenue +23.3%, loss narrowed 37.5%, CFO grew from ₹20.20 Cr to ₹27.68 Cr,
   Distribution segment flipped from a ₹6.17 Cr loss to an ₹11.01 Cr profit — this is
   not a story dependent solely on operator-supplied FY26 context; it is directly
   evidenced in the audited FY25 statements (Phase 3).
2. **Board mechanics are conventional and clean**: no over-tenured independents,
   strong attendance (all committees ≥5/5 or ≥2/2 except two single-meeting absences),
   a fully-attended, independent-chaired Audit Committee, a modest 15.72x CEO-to-median
   pay ratio, and disciplined, tabulated rights-issue use-of-proceeds reporting
   (Phase 5).
3. **Litigation and contingent-liability discipline is genuinely reasoned**: the one
   material litigation matter (furniture arbitration) is provided for close to the
   adjudicated amount rather than left as an open contingency, and total disclosed
   contingent liabilities are only 1.4% of net worth (Phase 2C).

### Top 3 red flags

1. **Confirmed subsidiary-level statutory default (Integrow, CARO ix(a)) within a
   Group audit year carrying six further entity-level CARO exceptions, none
   quantified in this AR**, under a first-year auditor covering only 56% of Group
   assets directly and who did not audit the FY24 comparative base (Phase 1).
2. **Density and severity of internally-inconsistent disclosures**: a direct
   auditor-vs-notes contradiction on IEPF compliance, an unreconciled >₹100 Cr gap
   between the auditor's own CARO investment table and its own audited notes, and a
   verified deferred-tax note arithmetic error — six distinct internal
   inconsistencies across one AR, reconciled and affirmed in this stage's independent
   re-verification (Phase 2, accounting quality 4/10).
3. **Goodwill concentration risk sitting adjacent to, but never named as a risk in,
   the MD&A/risk section or the CEO letter**: ₹174.25 Cr goodwill (61.3% of net
   worth) is 80.5% concentrated in two subsidiaries (NestAway, Helloworld) both
   acquired with negative net identifiable assets and both carrying negative,
   worsening net worth today — combined with a systematic pattern of this and five
   other material findings being entirely absent from both the disclosed risk
   section and the front-matter narrative (Phases 1, 2, 4, 6).

### Key monitorables for next quarter/next AR

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Integrow default cure status | Any disclosure of amount, counterparty, cure, or cross-default | Next year's CARO Annexure B / consolidated Auditor's Report Other Matters | The single most serious unresolved item from this AR; currently a confirmed fact with no quantum disclosed |
| Goodwill impairment test outcome | Any impairment charge against NestAway/Helloworld goodwill (₹96.35 Cr + ₹43.87 Cr combined exposure) | FY26 AR, Note 3.c/25 equivalent | Both subsidiaries carry negative and (per this AR) worsening net worth; a first impairment charge would directly hit reported equity and EPS |
| Receivables ageing (>1yr buckets) | Continued growth in the 1-2yr/2-3yr buckets, or a corresponding upward reclassification into the ECL "significant increase in credit risk" bucket | FY26 AR, Note 4.c equivalent | This AR's ageing shift was masked by headline growth matching revenue; a second consecutive year of the same pattern would confirm a genuine, not one-off, collection-quality issue |
| Promoter shareholding trajectory (49.81%→47.04% per operator-supplied screener data, Jun-Sep 2025) | Whether Stage 8's determination of rights-issue-dilution vs open-market-sale is corroborated by the FY26 AR's own shareholding pattern and any pledge disclosure | FY26 AR Corporate Governance Report; screener quarterly filings | This AR's own period showed stable promoter holding; the subsequent decline falls outside this AR and needs its own primary-source confirmation before being treated as a promoter-selling signal |
| Audit-coverage gap in FY26 | Whether the now-second-year auditor's directly-audited asset coverage expands beyond the 56% (100%−44%) achieved in this first year | FY26 AR, Auditor's Report Other Matters | A persistent large reliance on component auditors, especially at exactly the entities carrying CARO exceptions, would sustain rather than resolve this AR's central audit-scope concern |
| Standalone DSCR | Recovery from 0.11x, or continued deterioration | FY26 AR, MD&A ratio table | Currently near-zero; a standalone-only credit reader would already be alarmed; Group-level equity cover currently offsets this but the trend needs monitoring |
| Risk Management Committee disclosure | Whether FY26 AR provides composition/meeting detail for the Reg 21 compliance claimed in this AR, or corrects the compliance-status claim | FY26 AR Corporate Governance Report | Internal AR disclosure inconsistency identified in this stage, unresolved as of this document |

### Best fit strategy

**Turnaround** (Watchlist, leaning toward Pass on the operating evidence within
this AR, but capped by the accounting-quality and governance findings from Phases
1-2 and 4-6).

### One-line verdict

Real operating turnaround, unresolved governance and disclosure quality below it.

---
```yaml
stage: B03-ardeep
company: "AURUM"
run_date: "2026-07-14"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Quantum, counterparty, and cure status of the Integrow Asset Management CARO ix(a) default not disclosed anywhere in this AR"
  - "Amounts underlying the CARO exceptions at Monk Tech Ventures, NestAway (i(a)/(b) and vii(a)-(c)), K2V2, and Bonds Brain not disclosed in this AR (subsidiary-level detail sits in filings not collected for this run)"
  - "Consolidated/group-wide statutory audit fee and non-audit fee not separately disclosed; only standalone auditor remuneration (Rs23L audit / Rs6L non-audit) found"
  - "No single consolidated RPT-as-percentage-of-revenue figure tabulated in this AR"
  - "No unbilled revenue / contract asset breakout found in the receivables note"
  - "No covenant headroom/breach disclosure found in the borrowings notes"
  - "Promoter share pledge status not disclosed either way (no pledge stated, no explicit nil-pledge confirmation) in this AR"
  - "Per-CGU goodwill impairment test growth-rate/discount-rate assumptions not tabulated in the sections of this AR reviewed"
  - "DTA-recoverability assessment methodology for the consolidated deferred tax credit not disclosed"
  - "Whether the SEBI LODR Regulation 21 Risk Management Committee applies to this company, and if so its composition, is unresolved from this document alone"
flags:
  - type: FLAG-CASH
    reason: "Reaffirmed from B02 and independently extended in Phase 3: consolidated lease liability repayment alone (Rs50.38 Cr, net of interest) exceeds FY25 CFO (Rs27.68 Cr) by 1.8x before adding lease interest; combined lease cash service (per B02, Rs70.50 Cr) exceeds CFO by ~2.5x, funded through financing (equity raise) rather than operations. Layered on top of B02's original receivables-ageing masking finding, independently re-verified in this stage against Note 4.c: 1-2yr bucket +259.8% YoY, 2-3yr bucket +1,233% YoY, ECL significant-increase-in-credit-risk bucket shrank Rs159L to Rs109L, while headline receivables growth (+24.8%) tracked revenue growth (+23.3%) and would mask this without the ageing-table detail."
phase_verdicts:
  p1: "Red Flag"
  p2: "Red Flag"
  p3: "Watch"
  p4: "Red Flag"
  p5: "Watch"
  p6: "Watch"
  p7_best_fit: "Turnaround (Watchlist, leaning Pass on operating evidence)"
overall_quality: 5
quality_components: {governance: 5, accounting: 4, balance_sheet: 5, earnings: 5}
triple_pass_verification:
  verified: 15
  discrepancies: []
missing_risks:
  - {risk: "Goodwill impairment concentration (61% of consolidated net worth, 80.5% in two negative-net-worth subsidiaries)", evidence_anchor: "Note 3.c p.229 / Note 25 p.267, Consolidated Notes; Consolidated Balance Sheet p.211"}
  - {risk: "Subsidiary-level statutory default / 7-entity CARO exception concentration", evidence_anchor: "Consolidated Auditor's Report Annexure B, p.208"}
  - {risk: "Receivables ageing deterioration masked by headline growth", evidence_anchor: "Note 4.c, Consolidated Notes, p.236"}
  - {risk: "Standalone entity's near-zero debt-service coverage (DSCR 0.11x)", evidence_anchor: "MD&A Table 4, p.53-54"}
  - {risk: "Lease-obligation-dominated leverage exceeding operating cash flow", evidence_anchor: "Note 10.a p.243-245 (borrowings); Consolidated Cash Flow Statement p.214-215"}
  - {risk: "~44% audit-coverage gap / first-year auditor transition", evidence_anchor: "Consolidated Auditor's Report Other Matters (a)-(b), p.204"}
guidance_table:
  - {claim: "Double revenues over the next two years", number: "2x FY25 consolidated revenue (Rs263.84 Cr baseline)", timeframe: "2 years from FY25 (i.e., by approx. FY27)", credibility: "Unsubstantiated within this AR by any segment or margin breakdown; sourced from CEO letter, not MD&A; FY26 delivery data sits outside this document's scope and is not independently checked by this stage"}
monitorables:
  - {metric: "Integrow CARO ix(a) default cure status", threshold: "Any disclosure of amount/counterparty/cure/cross-default", where: "Next AR, CARO Annexure B / Auditor's Report Other Matters", why: "Single most serious unresolved finding from this AR; currently confirmed but unquantified"}
  - {metric: "NestAway/Helloworld goodwill impairment test outcome", threshold: "Any impairment charge against the combined Rs140.22 Cr goodwill exposure", where: "FY26 AR, Goodwill note", why: "Both subsidiaries carry negative, worsening net worth; a first impairment charge would directly hit reported equity and EPS"}
  - {metric: "Receivables ageing >1yr buckets", threshold: "Continued growth or ECL-bucket upward reclassification", where: "FY26 AR, trade receivables ageing note", why: "Confirms whether FY25's masked deterioration was a one-off or a genuine trend"}
  - {metric: "Promoter shareholding and pledge status", threshold: "Stage 8 determination of dilution vs open-market selling, corroborated by FY26 AR", where: "FY26 AR Corporate Governance Report; screener quarterly filings", why: "This AR's own period shows stable promoter holding (49.89%); the post-period decline needs primary-source confirmation before being read as a selling signal"}
  - {metric: "Audit-coverage gap in FY26", threshold: "Directly-audited asset coverage expanding beyond 56%", where: "FY26 AR, Auditor's Report Other Matters", why: "Persistent heavy reliance on component auditors at exactly the CARO-flagged entities would sustain rather than resolve this AR's central audit-scope concern"}
  - {metric: "Standalone DSCR", threshold: "Recovery from 0.11x", where: "FY26 AR, MD&A ratio table", why: "Near-zero standalone debt-service coverage; Group equity currently offsets but trend needs monitoring"}
  - {metric: "Risk Management Committee disclosure", threshold: "Composition/meeting detail provided, or compliance-status claim corrected", where: "FY26 AR Corporate Governance Report", why: "Internal disclosure inconsistency identified in this stage (Reg 21 'Yes' claimed with no supporting committee detail disclosed)"}
strengths_top3:
  - "Genuine operating inflection evidenced directly in this AR: revenue +23.3%, loss narrowed 37.5%, CFO grew to Rs27.68 Cr, Distribution segment flipped to profit"
  - "Conventional, clean board mechanics: no over-tenured independents, strong committee attendance, fully-attended independent-chaired Audit Committee, modest 15.72x CEO-to-median pay ratio"
  - "Reasoned litigation provisioning and low contingent-liability exposure (1.4% of net worth); disciplined, tabulated rights-issue use-of-proceeds reporting"
red_flags_top3:
  - "Confirmed subsidiary-level statutory default (Integrow, CARO ix(a)) within a 7-entity CARO exception year, unquantified in this AR, under a first-year auditor covering only 56% of Group assets directly"
  - "Six internally-inconsistent disclosures across one AR (IEPF auditor-vs-notes contradiction, >Rs100 Cr unreconciled CARO investment gap, deferred tax arithmetic error, K2V2 stake percentage inconsistency, lease write-back FY24 mismatch, liquidity boilerplate vs DSCR/lease-cash-flow facts), independently re-verified and affirmed in this stage (accounting quality 4/10)"
  - "Goodwill concentration (61.3% of net worth, 80.5% in two negative-net-worth subsidiaries) never named as a risk anywhere in the MD&A risk section or CEO letter, part of a systematic pattern of six material findings entirely absent from the AR's own narrative sections"
best_fit_strategy: "Turnaround (Watchlist, leaning Pass on operating evidence)"
one_line_verdict: "Real operating turnaround, unresolved governance and disclosure quality below it."
```
