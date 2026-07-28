# STAGE 3: ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: Dynacons Systems & Solutions Ltd (DSSL) | Run date: 2026-07-27
Source: FY2024-25 Annual Report, 30th AGM (PRIMARY, Rs Lakhs in source, converted to Rs Crore /100
below), file runs/dssl-2026-07-27/inputs/_textcache/annual-report__4202212d-3c8c-4bf5-91b7-62e9a68fbaa1.txt.
Page anchors use the AR's own printed page numbers (= PDF page number in the text cache minus 1,
verified against the printed folio visible on each page). Supplementary: FY2019-20 AR (file
annual-report__Annual_Report.txt) used only for backward context, anchored "(FY20 AR, p.N)".
Consolidated notes analysis from Stage 2 (B02-notes.md, accounting_quality 4/10) is treated as
verified input for Phase 2 per the pipeline's special instruction, not re-derived from scratch.

Kill switch statements below are INFORMATIONAL ONLY per pipeline operating rules. The pipeline does
not halt on company quality; flags propagate to the verdict.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core opinion

Standalone: unmodified/unqualified opinion, standard "true and fair view" language, no material
uncertainty / going-concern paragraph anywhere in the report (Independent Auditor's Report, p.86-89).
Consolidated: unmodified/unqualified opinion in identical structure (p.144-148). No emphasis of
matter in either report. Signing partner M.S. Parikh, M S P & CO., Chartered Accountants, FRN
107565W, both reports dated May 24, 2025 (standalone UDIN 25008684BMIWQF4319; consolidated UDIN
25008684BMIWQG7499).

### 1B. Key Audit Matters

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Revenue recognition (cut-off), sole KAM, both statement sets | "Large volume of revenue transactions near period end" creates a presumed SA 240 fraud-risk of premature recognition (Auditor's Report KAM, standalone p.86-87, consolidated p.144-145) | Control-design testing, sample verification of customer acknowledgements before/after year-end | 🟡 Corroborated independently by the receivables-ageing deterioration found in Phase 2 (1-2yr bucket +238.6% YoY) and by Note 9.6's statement that "there are no unbilled dues receivable from any customers" (p.117), meaning the entire cut-off risk sits inside the trade receivables book with a frozen ECL |

No impairment, provisioning, or fair-value KAM was raised by the auditor despite the frozen ECL
against a deteriorating ageing tail (Phase 2) and the new, undisclosed lease-financing structure
(Phase 1D/2A) both being live, judgement-heavy areas this year. Their absence as a KAM is itself
worth noting: a rules-based cut-off KAM was selected over what a reader would consider the two most
judgement-intensive new items in the balance sheet.

### 1C. Emphasis of Matter and Other Matters

No Emphasis of Matter paragraph in either report. The Consolidated Auditor's Report carries an
"Other Matters" paragraph (p.147-148): "The Consolidated financial statements includes the unaudited
financial statements of 2 subsidiaries whose financial statements reflect total assets of Rs311.38
Lakhs... total revenues... of Rs39.19 Lakhs and total net profit after tax of Rs7.62 Lakhs for the
period from April 1, 2024 to March 31, 2025... whose financial statements are not audited by us."
This paragraph refers to Dynacons Systems & Solutions Pte Ltd (Singapore) and Cybercons Infosec
Private Limited jointly as "2 subsidiaries." Two pages later, in clause (g)(i) of the same report
(Report on Other Legal and Regulatory Requirements, p.148), the same auditor writes: "The
consolidated financial statements disclose the impact of pending litigations on the consolidated
financial position of the Group, its associate - Refer Note No.31.6." The word "associate" here can
only refer to Cybercons (the only 50%-held entity in the Group). The same signing partner, same
report, same date, calls Cybercons a subsidiary on p.147-148 and an associate on p.148. This is a
verifiable, page-level self-contradiction inside a single audited document, not an inference.

### 1D. CARO 2020 clause-by-clause (standalone Annexure A, p.90-93; consolidated relies on the
standalone CARO, no separate group CARO issued)

| Clause | Finding | Amount | Risk |
|---|---|---|---|
| ii (inventory) | Physical verification procedures reasonable, no discrepancies | - | 🟢 |
| iii (loans to related parties) | "Has not made any investments in or provided guarantee or granted any loans or advances... to companies, firms, LLPs or any other parties during the year other than loan to staff" (p.90) | - | 🟡 See note below: this statement appears to exclude the Rs165.97 lakh Cybercons "Advances to Related Parties" balance (Note 12, up from Rs15.00 lakh, +1006% YoY) from CARO's related-party loan disclosure. Reconcilable only if that balance is a trade/commercial advance (it coincides with a new Rs254.74 lakh purchase transaction from Cybercons this year, Note 32.4) rather than a loan; the Notes do not make the distinction explicit anywhere |
| vii (disputed statutory dues) | One dispute: GST FY2018-19, Rs9.64 lakh, Appeal to Appellate Authority (p.91); no undisputed dues in arrears >6 months | Rs9.64 lakh = 0.04% of net worth, 0.13% of PAT | 🟢 immaterial |
| ix (borrowing defaults) | No default in repayment of loans/interest; not a wilful defaulter; term loans applied for stated purpose; no short-term funds used for long-term purposes | - | 🟢 |
| xi (fraud) | "No fraud by the Company and no material fraud on the Company has been noticed or reported during the year"; no ADT-4 filed; "the Company has not received any whistle blower complaints during the year" (p.92) | - | 🟢 |
| xvii (cash losses) | "The Company has not incurred cash losses during the financial year covered by our audit and the immediately preceding financial year" (p.93) | - | 🟢 |
| xx (unspent CSR) | No unspent amounts; CSR Rs92.67 lakh spent against Rs92.63 lakh prescribed (Note 31.3) | - | 🟢 |
| xxi (group audit / CARO of subsidiary) | "The CARO report of the Company's Indian Subsidiary Company, Cybercons Infosec Private Limited, had not been issued by the subsidiary's auditor till the date of signing of this audit report" (p.93) | - | 🔴 Cybercons is called the Company's "Indian Subsidiary Company" here, by the same auditor who elsewhere (Consolidated Auditor's Report clause (g)(i), Board's Report Sec.9, and AOC-1 Part B) calls it an "Associate." Also, as of the May 24, 2025 audit sign-off, Cybercons' own statutory CARO had still not been issued, meaning the group's second-largest classification question was resolved at the parent level without a completed local audit opinion to rely on |

Clauses i, iv, v, vi, viii, x, xii, xiii, xiv, xv, xvi, xviii, xix: all reported as not applicable or
clean, no adverse remarks; xix (liquidity/going-concern-adjacent ratio review): standard "nothing
has come to our attention" formulation, not a going-concern paragraph.

### 1E. Auditor continuity

M S P & CO. (FRN 107565W) re-appointed at the 27th AGM (September 30, 2022) to hold office through
the 32nd AGM (2027); original first-appointment date is NOT FOUND IN DOCUMENT (only the
re-appointment cycle is disclosed, Board's Report item 12, p.35). Fees for FY25: Statutory Audit Fees
Rs9,00,000; Tax Audit Fees Nil; Others Nil; Total Rs9,00,000 (Corporate Governance Report 14(s),
p.80). Non-audit/audit fee ratio = 0%, clean, well below any flag threshold.

### 1F. Standalone vs consolidated differences

The single most important cross-document finding in this Annual Report is that Cybercons Infosec
Private Limited is classified inconsistently across at least five separate places within the same
audited package, by the same signing partner and the same Board, in the same reporting cycle:

| Document | Classification used | Anchor |
|---|---|---|
| Board's Report, Sec. 9 (Holding/Subsidiary/Associate) | "Associate Company" | p.34 |
| Form AOC-1, Part B | "Associate Company," 50% holding, "significant influence" | p.45-46 |
| Standalone Notes 32.4 (RPT) | "Associate Company," "exercises significant influence through board representation" | p.133 |
| Consolidated Note 1.2.1(iii) "Basis of Consolidation" table | Listed under the heading "Name of the subsidiary," 50% holding, footnoted with the Ind AS 28 "significant influence" test rather than the Ind AS 110 "control" test | p.156-157 |
| Consolidated Note 1.2.1(iv) "Principles of Consolidation" + Consolidated Balance Sheet | Full Ind AS 110 line-by-line consolidation applied, with a distinct "Non-controlling Interests" line (Rs13.24 lakh FY25 vs Rs3.67 lakh FY24) that only exists under full consolidation, never under equity accounting | p.157, p.151 |
| CARO Annexure A, clause xxi | "the Company's Indian Subsidiary Company" | p.93 |
| Consolidated Auditor's Report, Other Matters | "2 subsidiaries" (Singapore + Cybercons combined) | p.147-148 |
| Consolidated Auditor's Report, clause (g)(i) | "its associate" | p.148 |

Four of the eight anchors call Cybercons an associate; four call it a subsidiary or consolidate it as
one. This is not a single slip; it recurs across the Board's own report, the statutory annexure, and
the independent auditor's own consolidated report. Reliance on other auditors' work: the Consolidated
Auditor's Report states the financial statements of both group entities (Singapore, unaudited by a
local auditor, Group-converted and audited by M S P & CO. for conversion adjustments only; Cybercons,
"located in India," furnished by management, "not audited by us") were not independently locally
audited as of the sign-off date. Neither of the "2 subsidiaries" had a completed, independent local
statutory audit relied upon at consolidation.

### Phase 1 summary

| Item | Verdict |
|---|---|
| Opinion | Unqualified, standard |
| KAM | Single, narrow (cut-off); silent on lease structure and ECL adequacy |
| CARO | Clean except xxi (Cybercons classification/audit-status) and the iii/Note-12 advance ambiguity |
| Auditor independence/fees | Clean, 0% non-audit ratio |
| Cross-document consistency | 🔴 Fails: 4 of 8 primary-document anchors contradict the other 4 on Cybercons' legal/accounting status |

**Phase 1 verdict: 🔴 RED.** Not because the opinion is qualified (it is not) but because the audit
package's own internal documents cannot agree on the classification of a related entity with real,
growing transaction volume this year (Rs254.74 lakh purchases, Rs165.97 lakh advances), and the
subsidiary in question had not even completed its own statutory audit by the parent's sign-off date.

**Kill switch assessment (informational):** Based on Phase 1 alone, a human reviewer would have
reason to pause, because the CARO annexure and the Consolidated Auditor's Report disagree with each
other, and with the Board's own report, on whether Cybercons is a subsidiary or an associate. This is
a disclosure-integrity failure inside the audit itself, not a company-quality judgment call. Per
pipeline rules this does not halt the run; it is flagged and the analysis continues.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Triple-pass verification (Stage 2 Top 15, checked against this read of the primary document)

All 15 numbers and note references from B02-notes.md were traced back into the Annual Report text and
independently recomputed where the finding involves arithmetic. Result: **15 of 15 verified**, with
one labeling nuance and one citation correction, both noted below rather than counted as
discrepancies in substance.

| Rank | B02 finding (summary) | Verification result |
|---|---|---|
| 1 | New ~Rs95.50cr lease liability, ~Rs82.85cr lease receivable, no counterparty/rate/credit disclosure | ✓ Verified with clarification: Note 32.11/31.9 "Lease Commitments" (p.140-141/196) shows "Leased liability recognised during the year: Rs9,549.85 lakh" (= Rs95.50cr, the gross new addition) reconciling to a closing balance of Rs8,694.81 lakh (Rs86.95cr) after Rs560.01 lakh finance-cost accrual and Rs1,672.46 lakh of payments. Both Rs95.50cr (addition) and Rs86.95cr (closing balance) are correct, they measure different things and B02's own parenthetical ("Rs2.57cr to Rs86.95cr") already shows this; worth stating explicitly for a reader. Lease Receivable: Rs5,855.67 lakh non-current (Note 5, p.116) + Rs2,429.51 lakh current (Note 13, p.119) = Rs8,285.18 lakh = Rs82.85cr, exact match. No counterparty, discount rate, or credit-quality disclosure found anywhere in Notes 5, 13, 18, 22, or 32.11 |
| 2 | Cybercons "subsidiary" vs "associate" contradiction | ✓ Verified and strengthened (see Phase 1F): found a fifth and sixth anchor beyond B02's original two (the Basis-of-Consolidation table at Note C-1.2.1(iii), and the Non-Controlling Interest line on the consolidated balance sheet) |
| 3 | Schedule III net-asset roll-forward fails to reconcile, ~Rs46.55 lakh Singapore shortfall, ~Rs46.70 lakh Cybercons surplus | ✓ Verified by direct recomputation: Singapore FY24 closing net assets Rs3.51 lakh + FY25 profit share Rs29.64 lakh = expected Rs33.15 lakh; actual FY25 closing shown is Rs(13.40) lakh; gap = Rs46.55 lakh. Cybercons FY24 closing Rs7.34 lakh + FY25 loss share Rs(22.02) lakh = expected Rs(14.68) lakh; actual FY25 closing shown is Rs32.02 lakh; gap = Rs46.70 lakh. Both gaps land within Rs0.15 lakh of each other, consistent with a value having been swapped or mis-attributed between the two entities' rows (Note C-31.10/31.10, p.196-197) |
| 4 | AOC-1 vs Schedule III opposite-sign profit for both entities | ✓ Verified: AOC-1 Part A shows Singapore "Profit after taxation (12,992)" USD, a loss; Schedule III shows Singapore's FY25 profit share as +Rs29.64 lakh, a profit. AOC-1 Part B shows Cybercons "Profit/Loss for the year... considered in Consolidation: Rs19,14,367," a profit; Schedule III shows Cybercons' FY25 profit share as Rs(22.02) lakh, a loss. Both entities flip sign between the two statutory tables. The auditor's own "2 subsidiaries... total net profit after tax of Rs7.62 Lakhs" (Other Matters, p.147) reconciles exactly to Schedule III's sum (29.64 + (22.02) = 7.62), proving Schedule III, not AOC-1, is what the audited consolidation actually used |
| 5 | Receivables ageing tail: 1-2yr bucket +238.6%, >6mo book +84%, ECL frozen | ✓ Verified by direct recomputation from Note 9.2 (p.118): 1-2yr bucket Rs323.85 lakh (FY24) to Rs1,096.20 lakh (FY25) = +238.6% exactly. >6mo book (6mo-1yr + 1-2yr + 2-3yr + >3yr): Rs1,662.75 lakh (FY24) to Rs3,062.52 lakh (FY25) = +84.2%. ECL allowance Rs13.68 lakh unchanged both years (Note 9.1) |
| 6 | Full-consolidation mechanics applied to a nominal 50% associate | ✓ Verified: Non-Controlling Interest line exists on the consolidated balance sheet (Rs13.24 lakh FY25, Rs3.67 lakh FY24, p.151), which cannot exist under Ind AS 28 equity accounting; only under Ind AS 110 full/line-by-line consolidation, which Note C-1.2.1(iv) explicitly describes as the method used |
| 7 | New Rs38.20cr deferred contract cost, no amortisation schedule | ✓ Verified: Note 7 (standalone, p.117) / Note 6 (consolidated, p.173): "Deferred contract cost 3,819.71" (=Rs38.20cr), zero in FY24. No amortisation period, contract identity, or schedule anywhere in the note |
| 8 | Floating-rate borrowings narrative contradiction | ✓ Verified verbatim: "The Company's exposure to the risk of changes in market interest rates are managed by borrowing at fixed interest rates. During the year Company did not have any floating rate borrowings" (Note 32.9(c), p.140), followed two lines later by "Variable Rate Borrowings 4,963.88" vs "Fixed Rate Borrowings 224.83" (Rs49.64cr vs Rs2.25cr = 95.7% floating) |
| 9 | Sole KAM is revenue cut-off | ✓ Verified (see 1B) |
| 10 | Bank guarantees +71.8% to 63.4% of net worth | ✓ Verified: Rs14,645.70 lakh (FY25) vs Rs8,522.72 lakh (FY24), Note 32.7(b)/31.6(b), p.135/191 = +71.86%; net worth (equity) Rs23,091.97 lakh = Rs146.46cr / Rs230.92cr = 63.4% |
| 11 | DSCR fell 64.8% standalone, 52.1% consolidated | ✓ Verified: Note 32.12/31.11 Key Financial Ratios (p.140-141/197): standalone DSCR 3.05x (from 8.68x, -64.84%); consolidated 4.15x (from 8.66x, -52.11%); management's own remarks column attributes both to "interest cost increase in lease interest unwinding" |
| 12 | Derivatives/hedging narrative contradiction | ✓ Verified verbatim: "The Company also enters into derivative transactions to hedge... All derivative activities for risk management purposes are carried out by Group Treasury Team" (Note 32.9 intro, p.136) vs "The company has not entered in any forward contract for hedging or otherwise in respect of foreign currencies during [the year]" (same note, p.139) |
| 13 | MSME trade payables up 31x YoY | ✓ Verified: Rs197.20 lakh (FY25) vs Rs6.32 lakh (FY24) = Rs1.97cr vs Rs0.063cr, 31.2x, both from the standalone Balance Sheet trade-payables split |
| 14 | No capital-commitment note despite new CWIP; Singapore negative-net-worth subsidiary at cost | ✓ Verified: CWIP Rs2,195.48 lakh standalone / Rs2,407.18 lakh consolidated (=Rs21.95cr/Rs24.07cr) from zero (standalone) or Rs25.59 lakh (consolidated) FY24. Singapore: AOC-1 Part A shows total assets USD16,137 vs total liabilities USD19,161, a negative net worth of USD(3,024); investment carried at Rs5,05,143 (Note 32.10(b)) with no impairment charge found anywhere |
| 15 | Consolidated EPS computed pre-NCI rather than on profit attributable to parent | ✓ Verified by recomputation: disclosed consolidated Basic EPS Rs57.01 = Rs7,249.06 lakh (pre-NCI Group profit) / 1,27,16,071 weighted average shares. Profit attributable to shareholders of the Company is separately disclosed as Rs7,239.49 lakh (P&L, "Profit for the year attributable to... Shareholders of the Company," p.152), which would give Rs56.94/share if used, per Ind AS 33 |

**Citation correction (not a substance discrepancy):** B02 cites Finding 2 as "CARO Annexure B
cl.xxi, p.94." The Cybercons CARO clause is in **Annexure A** (the CARO annexure itself), not
Annexure B (which is the Internal Financial Controls report, a different annexure entirely), and sits
on printed **p.93**, not p.94. The substance of the finding is fully correct; only the annexure
letter and page require correction.

**New finding from this stage's extension (not in B02's Top 15):** Note 12 (Short-term Loans and
Advances, p.118) discloses "Advances to Related Parties (refer note 32.4) 165.97 15.00" under the
heading "Short Term Loans and Advances," a +1,006% YoY jump coinciding with a new Rs254.74 lakh
purchase transaction from Cybercons this year (Note 32.4, p.133). CARO clause iii states the Company
granted no loans/advances "other than loans to staff" during the year, which only reconciles if this
balance is a trade/commercial advance rather than a loan; the Notes never make that distinction
explicit, and bucketing a related-party trade advance under a note titled "Loans and Advances" (echoed
in the Board's Report item 44's cross-reference to "Note no. 32.10(b)" for Section 186 loans/
guarantees/investments, which does not separately surface this balance) is a further small piece of
the same disclosure-clarity pattern found throughout the Cybercons relationship this year. 🟡

### 2A. Accounting policy aggressiveness

Revenue recognition: point-in-time on delivery/customer acknowledgement (Note 1.2.2), adopted under
Ind AS 115 "from the current year" per the Auditor's KAM wording (p.86), consistent with the single
KAM. Depreciation: standard useful lives per Schedule II, no policy change disclosed. Inventory:
lower of cost and NRV, no method change. Capitalisation: the Rs38.20cr deferred contract cost and the
new CWIP program are this year's two new capitalisation judgments; neither is referenced in the
"Use of estimates and judgements" note (Note 1.2(e), standalone p.102-103; Note 1.2.1(vii),
consolidated), which lists only Lease classification, deferred tax, useful life, defined benefit
obligations, and impairment of trade receivables as areas of significant judgement. Confirms B02's
Pass-3 meta-pattern: the two largest new balance-sheet items this year (lease structure, deferred
contract cost) are absent from the note that is supposed to flag exactly this kind of new judgement.
ECL matrix: frozen allowance, no matrix disclosed, no methodology note beyond the movement table.
Ind AS 116 (leases): discount rate not disclosed anywhere for the new lease structure.

### 2B. RPT map

Total related-party payment/transaction value for the year (rent, reimbursements, KMP remuneration,
CSR-linked payment, Cybercons purchases/advances/investment, advertisement): approximately Rs8.50cr
against standalone revenue of Rs1,266.83cr = **0.67% of revenue**, immaterial by any standard
threshold (Note 32.4, p.133). Value-extraction signal: none material in aggregate, but the step-up
in Cybercons-specific dealings (new Rs254.74 lakh purchase, advances up 11x to Rs165.97 lakh) lands
in the same year as the unresolved classification question, worth watching rather than dismissing.

### 2C. Contingent liabilities

Only disclosed contingent liability: GST dispute FY2018-19, Rs9.64 lakh, unchanged both years (Note
32.7(a), p.134-135). As % of net worth: 0.04%. As % of PAT: 0.13%. Both far below the 25%/>100% flag
thresholds. Bank guarantees (a separate line, not classified as a contingent liability under Ind AS
37 since these are performance/financial guarantees given by banks on the Company's behalf) at
Rs146.46cr = 63.4% of net worth is the more material off-balance-sheet exposure metric (see 1D/Rank
10 above); it does not meet the contingent-liability flag test but is material enough to monitor.

### 2D. Receivables

Fully covered in the triple-pass verification (Rank 5) above. Summary: closing-balance DSO improved
(per Board's Report ratio table, Debtors Turnover improved from 4.70 to 4.14 months, +11.9%) on the
back of 23.7% revenue growth, while the ageing tail (1-2yr, >6mo buckets) deteriorated sharply beneath
that headline, with ECL frozen. No unbilled revenue/contract assets exist (Note 9.6: "there are no
unbilled dues receivable from any customers"), meaning 100% of the cut-off KAM risk sits in trade
receivables. Customer concentration: NOT FOUND IN DOCUMENT (no top-customer or top-5-customer
receivables concentration disclosed anywhere in the Notes).

### 2E. Inventory

Stock-in-trade down from Rs73.39cr to Rs58.24cr even as revenue grew 23.7%; Inventory Turnover ratio
improved from 18.62x to 19.25x (Board's Report ratio table, p.33); no write-downs disclosed; no
discrepancies on physical verification (CARO cl.ii). Clean, efficiency-improving. 🟢

### 2F. Borrowings

Total debt Rs51.89cr (FY25) vs Rs33.19cr (FY24), still small relative to Rs230.92cr net worth (D/E
0.22x). Composition is almost entirely short-term working-capital loans (Rs49.02cr, hypothecated
against stock and book debts, Note 17.1/21.1) plus small vehicle term loans. No covenant-breach
language found; no ICDs given other than the Cybercons advance discussed above. Pledge of company
assets: bank deposits and cash balances pledged for banking facilities (Note 5, 10), standard working-
capital security, not a promoter-share pledge (see Phase 5D). Borrowing-limit authorisation sought at
this AGM (Item 5 of the Notice, p.24): shareholder approval to raise the Section 180(1)(c) borrowing
limit to **Rs1,500 crore**, described only as an "enabling provision" for "larger projects" requiring
"enhanced bank guarantees and mobilization of credit facilities," with no specific financing plan,
project list, or amount actually intended to be drawn. Against a current total debt base of Rs51.89cr
and net worth of Rs230.92cr, this is a roughly 6.5x-net-worth blank-authorisation request unsupported
by any disclosed financing plan; flagged in Phase 4 below.

### 2G. Deferred tax reconciliation

Clean. Effective tax rate 25.35% (FY25) vs 25.27% (FY24), tracking the domestic statutory rate of
25.17%/25.09% closely with only small (<1%) reconciling items (Note 6(c), p.116). Deferred tax asset
net Rs106.24 lakh (FY25) vs Rs61.16 lakh (FY24), driven by lease-rental timing differences (Rs543.09
lakh DTA) newly created this year alongside the lease structure, and PPE timing differences (Rs507.64
lakh DTL). No aggressive or unusual deferred-tax judgement found. 🟢

### 2H. Exceptional items, goodwill, ESOP, lease obligations, subsequent events

No exceptional items line anywhere in either P&L; NOT FOUND IN DOCUMENT (clean by absence, no pattern
to assess). No goodwill; the consolidation note describes a "Capital reserve" (not goodwill) arising
where the Parent's share of an acquiree's equity exceeds acquisition cost (Note C-1.2.1(iv), p.157);
this is the "capital reserve on consolidation" B02 referenced, confirmed. ESOP: 12,750 options granted
January 9, 2025; 12,200 shares allotted; total dilution since inception roughly 0.1-0.2% of paid-up
capital, immaterial. Lease obligations: fully covered under 32.11/31.9 above. Post-balance-sheet
events: NOT FOUND IN DOCUMENT beyond the board-approval date (May 24, 2025); no subsequent-events
note in either statement set, reconfirmed on this read (consistent with B02 Pass 3).

### Phase 2 summary and reconciliation with Stage 2's 4/10 score

This read agrees with B02's accounting_quality score of **4/10**. Every one of the 15 triple-pass
findings survived independent primary-source verification (several with exact-to-the-lakh arithmetic
recomputation), one new finding was added (the Note 12/CARO cl.iii advance-vs-loan ambiguity), and one
citation was corrected. Nothing found in this extension pass would move the score materially in
either direction: the genuinely clean areas (inventory, payables discipline, deferred tax, RPT
proportionality, CSR) are real and offset nothing against the weak areas (Cybercons classification
integrity now confirmed across six anchors, the Schedule III arithmetic failure independently
recomputed, and the frozen ECL against a tripling ageing tail).

**Phase 2 verdict: 🔴 RED**, consistent with B02.

**Kill switch assessment (informational):** Based on Phases 1-2, a human reviewer would have strong
reason to pause, because a primary statutory table (Schedule III) fails its own arithmetic for both
group entities in a pattern consistent with a swapped value, independent of and in addition to the
classification dispute. This is a data-integrity issue in the filing itself. Per pipeline rules,
flagged and continuing.

---

## PHASE 3: FINANCIAL STATEMENTS

### 3A. Cash flow (read first)

| Metric | FY25 | FY24 |
|---|---|---|
| PAT (standalone) | Rs72.41cr | Rs53.96cr |
| CFO | Rs64.11cr | Rs29.04cr |
| CFO/PAT | 0.885x | 0.538x |
| EBITDA (PBT+Fin.cost+D&A) | Rs111.87cr | Rs82.52cr |
| CFO/EBITDA | 57.3% | 35.2% |
| Capex (PPE + CWIP) | Rs27.31cr | Rs0.29cr |
| FCF (CFO - capex) | Rs36.80cr | Rs28.75cr |
| Capex/Depreciation | 16.6x | 0.19x |
| Financing outflow | Rs(6.27)cr | Rs(42.27)cr |

(Standalone Cash Flow Statement, p.98-99; consolidated is materially identical at group level.)

CFO/PAT improved sharply YoY and both years, taken at face value, sit at or above the pipeline's 0.7x
flag threshold in FY25 (though FY24 was below it at 0.54x). Read in isolation this looks like an
improving cash-conversion story. Three quality caveats sit underneath that headline:

1. **Frozen ECL against a tripling ageing tail (Phase 2, Rank 5)** means the CFO figure benefits from
   not having taken a bad-debt charge that the ageing data would support at least questioning; if any
   portion of the 1-2yr/>2yr buckets is eventually provided for, both PAT and CFO in a future period
   will absorb it retroactively.
2. **The Rs38.20cr deferred contract cost** (Note 7/6) is treated as a non-current asset addition
   inside "Other non current assets (3,819.71)" in the CFO working-capital adjustment, i.e. it already
   reduces CFO this year (a use of cash) rather than sitting in expenses; this is conservative for CFO
   *this* year but defers the question of whether it was a genuine investment or a disguised expense
   to future periods' amortisation, none of which is disclosed (Phase 2, Rank 7).
3. **An internal reconciliation gap in the "Other current financial assets" cash-flow line.** The
   Standalone Cash Flow Statement shows "Other current financial assets 2,994.23" as a *positive*
   (cash-generating) adjustment in FY25. The corresponding balance-sheet note (Note 13, "Other
   Financial Assets," current) shows the underlying balance *increased* from Rs696.70 lakh to
   Rs2,735.46 lakh, i.e. a Rs2,038.76 lakh (Rs20.39cr) build, primarily driven by the new Rs2,429.51
   lakh current Lease Receivable. A balance-sheet increase in a current asset is conventionally a use
   of cash in the indirect method, not a source. The direction and the magnitude (Rs29.94cr positive
   vs an Rs20.39cr actual increase in the same-titled note) do not reconcile on this reading. This may
   reflect netting against another line not separately disclosed in the cash flow statement (e.g. the
   Rs199.42 lakh increase in Note 12 short-term loans/advances is not separately visible either), or
   an extraction/labelling issue; either way it is not traceable line-by-line from the notes as
   presented, and is flagged here as a fresh Phase 3 finding for follow-up rather than asserted as a
   definitive error. 🟡

One-time inflators: none identified (no exceptional gains, no large one-off working-capital release
beyond the items above). Interest classification: Finance costs Rs13.21cr are correctly shown in both
the P&L and as a financing outflow in the cash flow statement (no reclassification games noted).
Payable stretching: trade payables grew a modest +2.4% (Rs391.86cr to Rs392.86cr combined dues,
standalone) against 23.7% revenue growth, i.e. payables did *not* stretch to fund growth; the opposite
of an unsustainable-payable-stretch pattern. Cash pile: cash & equivalents grew from Rs2.66cr to
Rs34.41cr, plus Rs69.85cr in bank margin-money/deposit balances (largely pledged for banking
facilities and bank-guarantee support, Note 11), so the "cash pile" is mostly encumbered, not free.

### 3B. Balance sheet

| Item | FY25 | FY24 |
|---|---|---|
| Total Assets | Rs774.07cr | Rs587.03cr |
| Equity (net worth) | Rs230.92cr | Rs157.57cr |
| Non-current liabilities | Rs71.50cr | Rs14.95cr |
| Current liabilities | Rs471.66cr | Rs414.51cr |
| Total Debt | Rs51.89cr | Rs33.19cr |

**Key ratio table** (standalone, Board's Report/Note 32.12, p.33/140-141):

| Ratio | FY25 | FY24 | Variance |
|---|---|---|---|
| Current ratio | 1.36x | 1.39x | -2.5% |
| Quick ratio | NOT FOUND IN DOCUMENT | NOT FOUND IN DOCUMENT | - |
| Debt/Equity | 0.22x | 0.21x | +6.7% |
| Net Debt/EBITDA | ~0.46x (Rs51.89cr debt less Rs34.41cr cash / Rs111.87cr EBITDA) | ~0.40x (implied) | modest increase |
| Interest coverage | 8.47x | 9.39x | -9.8% |
| DSCR | 3.05x | 8.68x | -64.8% |
| ROCE (per Board's Report) | 46.55% | 38.19% (FY24 std., prior year table) | improving |
| ROE (Note 32.12) | 37.28% | 41.17% | -9.45% |
| Goodwill % of net worth | 0% (no goodwill on balance sheet; consolidation carries a Capital Reserve, not goodwill) | 0% | - |

The current ratio at 1.36x is on the tighter side for a systems-integration business carrying large
trade-receivable and inventory balances, and it *fell* slightly this year even as the balance sheet
grew; this bears watching alongside the receivables-ageing deterioration (Phase 2D), since a tight
current ratio combined with a lengthening ageing tail is a combination worth more attention than
either fact alone. Interest coverage (a P&L-only measure) fell a modest 9.8%, while DSCR (which
includes principal repayment, and now carries the new lease-liability service burden) fell a much
sharper 64.8%, both real, both explained candidly by management as lease-interest-driven (Note 32.12
remarks column), and both directionally consistent with each other, not contradictory.

**DuPont decomposition (standalone, approximate from disclosed figures):** Net margin 5.72% (FY25,
+8.9% YoY) x Asset turnover (Revenue/Avg Assets ~Rs1,266.83cr/Rs680.55cr ~1.86x) x Equity multiplier
(Avg Assets/Avg Equity ~Rs680.55cr/Rs194.24cr ~3.50x) approximates the disclosed ROE of 37.28%. The
equity multiplier of ~3.5x is the largest single driver of ROE, meaning **ROE is materially
leverage/balance-sheet-structure-driven this year**, not purely margin-driven, even though the
Debt/Equity ratio itself (0.22x) looks low; the multiplier is inflated by the current-liability side
of the balance sheet (trade payables + short-term borrowings, not formal "debt") rather than by
interest-bearing leverage per se. This is a nuance the headline D/E ratio alone would miss.

### 3C. P&L

| Line | FY25 | FY24 | YoY |
|---|---|---|---|
| Revenue from Operations | Rs1,266.83cr | Rs1,024.43cr | +23.7% |
| Other Income | Rs6.71cr | Rs4.38cr | +53.2% |
| EBITDA | Rs111.87cr | Rs82.52cr | +35.6% |
| EBITDA margin | 8.78% | 8.02% | +0.76pp |
| Finance Costs | Rs13.21cr | Rs8.79cr | +50.4% |
| PBT | Rs97.01cr | Rs72.21cr | +34.3% |
| Tax | Rs24.60cr | Rs18.25cr | +34.8% |
| PAT | Rs72.41cr | Rs53.96cr | +34.2% |
| Basic EPS | Rs56.95 | Rs42.51 | +34.0% |
| Diluted EPS | Rs56.89 | Rs42.47 | +34.0% |

Other income as % of PBT: 6.9%, well below the 20% flag threshold, clean. Margin waterfall
(revenue to PAT): revenue growth (+23.7%) converted to faster EBITDA growth (+35.6%) and faster PAT
growth (+34.2%), i.e. genuine operating leverage, not a one-off. Exceptional items 3-year pattern:
NOT FOUND IN DOCUMENT (no exceptional-item line disclosed in any year shown), clean by absence. Tax
rate consistency: clean, see 2G. Basic vs diluted EPS gap: Rs56.95 vs Rs56.89 (standalone), a
negligible 0.1% gap from ESOP dilution, immaterial.

### Phase 3 summary and cross-reference

The headline P&L and cash-flow story is genuinely strong: real double-digit revenue growth converting
to faster profit growth, improving CFO/PAT, low formal leverage, and management candour on the one
metric (DSCR) that visibly worsened. Set against Phases 1-2, though, three of this year's largest new
balance-sheet items (the lease-financing structure, the deferred contract cost, and the frozen ECL)
sit directly upstream of this quarter's reported cash and profit numbers, and none of the three is
transparently disclosed enough for an outside reader to independently stress-test them.

**Phase 3 verdict: 🟡 YELLOW** (strong reported numbers, real but incompletely disclosed
cash-quality risk underneath them).

**Kill switch assessment (informational):** Based on Phases 1-3, a human reviewer would not stop
solely on the numbers reported (they are genuinely strong and improving), but would want the Note
13/cash-flow reconciliation gap and the ECL-vs-ageing gap explained before treating reported CFO and
PAT at full face value. Flagged, continuing.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed risks, real vs boilerplate

The Board's Report / MD&A "Threats" and "Risks and Concerns" sections (p.30-31) name: competitive
intensity/commoditisation, technology obsolescence, talent retention, and cybersecurity. Each is
paired with a stated mitigation (R&D/training investment, value-added service focus, SOC monitoring,
employee engagement programs). These are largely industry-standard, template-adjacent risk statements
common to Indian IT-services MD&As; none is company-specific in a way that would let a reader
distinguish DSSL's actual risk exposure from any peer's. Real, specific content does exist elsewhere
in the MD&A (named client wins: Canara Bank, NABARD CBAAS; named awards: Deloitte Fast 50, HPE/Lenovo
partner awards; the 5-year consolidated financial table), just not inside the "Risks and Concerns"
section itself.

### 4B. Missing risks

Risks that Phases 1-3 make clearly relevant but that are absent from the disclosed risk section:

1. **Credit/counterparty risk on the new ~Rs82.85cr lease receivable book.** DSSL has become, in
   effect, a lessor/financing intermediary for customer hardware this year (Phase 2, Rank 1). No risk
   factor anywhere discusses this new credit exposure, even though it is roughly 36% of net worth in
   size. Likely reason for omission: the structure itself is under-disclosed at the note level too
   (no counterparty named), so a risk-factor discussion would have required disclosing what the
   structure actually is.
2. **Receivables collection/ageing risk.** Given the 238.6% growth in the 1-2yr bucket, a reader would
   expect at least a line on collection risk; none exists. Likely reason: the turnover-ratio headline
   (improving DSO) is the only version of this story management chose to tell (Board's Report ratio
   table, p.33), and it is technically accurate on an average basis while masking the closing-book
   tail.
3. **Governance/disclosure-integrity risk around Cybercons.** Given that the classification question
   spans the Board's own report, AOC-1, CARO, and the Consolidated Auditor's Report, this would
   normally warrant at least a line in risk factors or Critical Judgements; it appears in neither.
4. **Concentration/execution risk on large single-client wins** (Canara Bank data-centre modernisation,
   NABARD CBAAS 5-year contract) is not discussed as a concentration risk, only celebrated as a growth
   driver in the "Company Performance"/"Managed Services" narrative sections (p.27-29).
5. **Funding-plan risk behind the Rs1,500cr borrowing-limit authorisation request** (Item 5 of the
   Notice, p.24): sought without any specific project list or amount intended to be drawn, against a
   current debt base of only Rs51.89cr; no risk-factor or capital-allocation discussion accompanies
   this outsized ask.

### 4C. MD&A deep dive

Industry claims: global IT systems-integration market "over USD 430 billion," Indian domestic market
"approximately USD 15 billion" (p.26); both are asserted without a cited source, standard practice
in this segment but not independently verifiable from the document itself. Growth/margin
explanations: growth attributed to "robust traction in Infrastructure Management Services, Data
Centre and Cloud Solutions, and large integration projects"; margin improvement (8.02% to 8.78%
EBITDA) attributed to "higher contribution from managed services, enhanced project execution
efficiencies, and investments in automation-led delivery models" (p.26); both plausible and broadly
consistent with the segment note (System Integration segment result margin 8.19% vs Technology
Workforce Augmentation Services 48.3%, though the latter is only 0.96% of revenue so cannot itself
explain the group-level margin move). External-factor credit-taking/blaming: management takes credit
for the growth and margin improvement without attributing it to sector tailwinds alone, and does not
blame external factors for anything (no adverse commentary at all this year); a mild positive for
accountability tone, though it also means the one metric genuinely explained by an external/mechanical
factor (DSCR, lease-interest unwinding) is the only place management volunteers a "things got worse
and here is exactly why" statement.

**Forward guidance table:**

| Claim | Number | Timeframe | Credibility check |
|---|---|---|---|
| "The outlook for the IT system integration industry remains highly positive" | No number | Unspecified | Not testable; standard boilerplate |
| "Strong order book, landmark projects such as NABARD's Core Banking as a Service deployment" | No revenue/order-book value disclosed | Unspecified | NOT FOUND IN DOCUMENT: no order-book size, backlog value, or specific FY26 revenue/margin target given anywhere in the AR |
| Borrowing limit raised to Rs1,500cr (Notice Item 5) | Rs1,500cr ceiling | Enabling, no timeframe | Not a guidance number in the ordinary sense; flagged above as unsupported by a stated financing plan |
| 5-year consolidated financial summary (FY21-FY25: Revenue Rs437cr to Rs1,274cr, PAT Rs8.54cr to Rs72.49cr, ROCE 21.8% to 38.9%) | Historical, not forward | Historical | Credible: this is the one place management shows its own multi-year delivery record, and it is internally consistent with the audited financials cross-checked in Phase 3 |

Overall: the AR gives essentially **no explicit forward numeric guidance** for FY26 (revenue growth
rate, margin target, or order-book value); the only quantified forward-looking figure in the entire
document is the Rs1,500cr borrowing-limit request, which is a ceiling, not a plan. Segment analysis:
covered in Phase 2H/6C; Technology Workforce Augmentation Services is named a "focus business segment"
in the Notes (31.5, p.189) but is entirely unaddressed in the MD&A's "Business Segments" narrative
section, which covers only Data Centre & Cloud, Network & Security, Workplace Solutions, and Managed
Services (p.27-29).

### 4D. Tone and credibility ratings (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | Genuinely material new items (lease structure counterparty/rate, Cybercons status, deferred contract cost rationale) are simply absent from both the qualitative MD&A and the quantitative notes; what is disclosed is compliant in form but silent on the year's two biggest judgement calls |
| Consistency | 2/5 | Two verbatim self-contradicting risk-narrative paragraphs (floating-rate debt, derivatives) plus the six-anchor Cybercons classification split materially undercut internal consistency |
| Specificity | 3/5 | Real specifics on named clients/awards/5-year financial table; near-total absence of forward numeric targets or order-book size |
| Accountability | 3/5 | Candid, specific explanation of the one metric that clearly worsened (DSCR); no acknowledgement anywhere of the ECL/ageing, Cybercons, or lease-disclosure gaps |
| Capital allocation sense | 3/5 | Low leverage, modest dividend (5% face value, <1% of PAT), reinvestment into a new CWIP program consistent with a growth phase; but the Rs1,500cr borrowing-limit ask and the launch of an undisclosed lease-financing business line both lack an articulated capital-allocation rationale in the MD&A |

### Phase 4 summary

**Phase 4 verdict: 🟡 YELLOW.** The core operating narrative (client wins, margin drivers, segment
mix) is broadly credible and cross-checks against the financials. The risk section, however, is
templated and omits precisely the items Phases 1-3 show matter most this year, and forward guidance
is essentially absent.

**Kill switch assessment (informational):** Based on Phases 1-4, a human reviewer would not stop on
the operating narrative itself, but would note that the risk-factor section systematically avoids the
year's most material new judgement calls, which is itself informative about management's disclosure
posture. Flagged, continuing.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board composition

| Director | Category | Appointed | Board meetings attended (of 13) | Attendance % | Other public directorships | Flags |
|---|---|---|---|---|---|---|
| Shirish M. Anjaria | Promoter, Chairman cum MD | 26/09/1995 | 13/13 | 100% | 0 | Age 80 (per Annexure II) |
| Parag J. Dalal | Promoter, Executive/WTD | 26/09/1995 | 13/13 | 100% | 0 | - |
| Dharmesh S. Anjaria | Promoter, Executive/WTD & CFO | 30/09/1998 | 13/13 | 100% | 0 | Father-son relation with Shirish Anjaria (disclosed) |
| Vijay M. Doshi | Independent | 05/09/2022 | 10/13 | 76.9% | 2 | - |
| Jitesh J. Jain | Independent (resigned 04/03/2025) | NOT FOUND IN DOCUMENT | 10/13 | 76.9% | 2 | Resigned mid-year, was Audit Committee Chairperson |
| Archana V. Phadke | Independent | 27/03/2015 | 7/13 | **53.8%** | 2 | 🔴 Attendance <75%; tenure ~10 years as of FY25 (borderline the 10-year "long-tenure independence" watch threshold; her continuation past age 75 was itself put to a special resolution at the 2022 AGM) |
| Ashok B. Rajagiri | Independent (appointed 05/03/2025) | 05/03/2025 | 1/1 (eligible from appointment) | N/A (new) | 2 | Appointed as new Audit Committee Chairperson in the final weeks of the fiscal year (see 5B) |

No independent director sits on more than 2 other public boards or holds more than the regulatory
committee-chair limits; no promoter-group cross-board-membership concentration found; none of the
three executive/promoter directors holds any other public directorship (a mild positive: no divided
attention).

### 5B. Committee analysis

Audit Committee met 12 times; chaired by Jitesh Jain for 10 of those 12 meetings until his resignation
"due to other ongoing engagements and personal commitments" effective March 4, 2025, with Ashok
Rajagiri appointed Chairperson the very next day (March 5, 2025) and attending only the single
remaining meeting (March 14, 2025) before the FY25 financial statements were signed off on May 24,
2025. 🟡 The Audit Committee that formally signed off on the FY25 audit process was chaired by a
director who had been on the Board for barely ten weeks and had attended one Audit Committee meeting,
in the same year the audit surfaced the Cybercons classification question, the Schedule III
reconciliation failure, and the frozen-ECL finding; this is a governance-continuity concern regardless
of Mr. Rajagiri's individual qualifications (he is a Chartered Accountant). Nomination & Remuneration
Committee (5 meetings), Stakeholders' Relationship Committee (4 meetings), CSR Committee (6 meetings):
all met with adequate quorum and no adverse findings. Risk Management Committee: constituted
voluntarily (not mandatorily applicable under Reg. 21(5)) but held **zero meetings** during FY25 (p.71
"the members of the Risk Management committee did not conduct any meeting during the FY 2024-2025"),
worth noting given this is the same year the company took on a new, undisclosed lease-financing risk
and a large capex program.

### 5C. Compensation

KMP (3 executive directors) total remuneration FY25: Rs3.90cr (Shirish Rs1.38cr, Parag Rs1.26cr,
Dharmesh Rs1.26cr) = **5.39% of standalone PAT** (Rs72.41cr), a modest ratio for a promoter-run
company of this scale. Ratio to median employee remuneration: 67.69x (Shirish), 61.80x each (Parag,
Dharmesh) (Annexure II, p.47-48), within a defensible range for an Indian small-cap, not flagged as
excessive. No performance bonus/variable component paid to any executive director. Promoter family
payroll: all three executive directors are promoters; Shirish and Dharmesh are father and son
(disclosed). ESOP dilution: immaterial (~0.1-0.2%, see 2H).

### 5D. Shareholding

Promoter/promoter-group holding as at March 31, 2025 (summing disclosed categories): Promoters/
Directors 35.39% + Corporate Bodies (Promoter Company) 16.40% + Relative of Director 9.16% =
**60.95% combined** (Corporate Governance Report 13.11, p.76). YoY change in this combined percentage:
NOT FOUND IN DOCUMENT (only the current-year distribution table is given; the one specific
shareholding movement disclosed, the transmission of the late Mrs. Hasumati Dalal's 1,44,816 shares to
Mr. Parag Dalal, is stated to leave "no change in pre and post Shareholding percentage held by
Promoter/Promoter Group," p.76). Pledge: no promoter-share pledge disclosure of any kind found in the
Annual Report text (the only "pledge" references in the document relate to bank deposits/inventory/
receivables hypothecated for working-capital facilities, an entirely different, routine matter); a
positive-by-absence read, though the AR itself does not carry an affirmative "nil pledge" shareholding
statement, so this should be cross-checked against SAST/BSE shareholding-pattern filings at Stage 8
rather than treated as fully confirmed here. No promoter selling against the growth narrative was
found; the only share-count changes are ESOP-driven dilutive issuances and the family-transmission
event above, not open-market promoter sales.

### 5E. Governance red-flag checklist

| Item | Status |
|---|---|
| Whistleblower complaints | None received (CARO xi(c), Board's Report) |
| SEBI/regulatory actions | None material; one minor Rs5,000+GST fine each from BSE/NSE for delayed Reg.33 board-outcome disclosure, explained and paid (Corporate Governance Report 14(d), p.78) |
| RPT committee | No separate RPT committee; handled by the Audit Committee, standard practice |
| Auditor fee ratio | 0% non-audit, clean (1E) |
| CSR compliance | Fully spent, Rs92.67 lakh vs Rs92.63 lakh prescribed, transparently itemised (Annexure IV) |
| Section 143 fraud reporting | None (CARO xi(a)/(b)) |
| Material subsidiary auditor | 🔴 Neither of the Group's "2 subsidiaries" (Singapore, Cybercons) had an independent local statutory audit completed and relied upon as of the parent's May 24, 2025 sign-off (Consolidated Auditor's Report, Other Matters, p.147; CARO cl.xxi, p.93) |

### Phase 5 summary

**Phase 5 verdict: 🟡 YELLOW.** The governance apparatus is largely compliant on paper (committee
structure, CSR, fees, whistleblower, no fraud), but three concrete items narrow the margin: one
independent director below the 75% attendance threshold, an Audit Committee chair transition in the
final ten days of the fiscal year with essentially no committee-meeting overlap before sign-off, and
a Risk Management Committee that held zero meetings in the exact year the Group took on a new,
materially undisclosed financing structure.

**Kill switch assessment (informational):** Based on Phases 1-5, a human reviewer would have reason to
ask why none of the five available governance checkpoints (Board, Audit Committee, Risk Management
Committee, statutory auditor, Board's Report) caught or reconciled the Cybercons classification
question or the Schedule III arithmetic failure before the Annual Report was finalised. Flagged,
continuing.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

### 6A. Narrative vs reality

The Chairman's letter (p.2, unusually short and purely thematic, no financial figures at all) makes
these prominent claims:

| Claim | Cross-check | Verdict |
|---|---|---|
| "For 30 years, we have been a trusted partner in India's digital evolution" | Incorporated 1995, 30th AGM this cycle | ✅ Factually accurate |
| "We have successfully powered the first wave of digitalization" | Consistent with the 10-year growth history (screener context: Sales Rs158cr FY17 to Rs1,424cr FY26) and the FY20 AR's own COVID-era "greater demand for our services" narrative (FY20 AR, p.37) | ✅ Broadly consistent with the historical growth trajectory |
| "Our focus has shifted from simply providing technology to a more powerful mission... embedding intelligence into every layer of our solutions" (AI positioning) | No R&D spend disclosed ("Such methods do not involve any specific cost burden to the Company - NIL," Board's Report 32(B)(iv), p.41); no AI-specific segment, revenue line, or capex breakout anywhere in the Notes | ❌ Not evidenced in the financial disclosures; see 6E below |
| Implicit claim of continued strong execution/growth momentum | Revenue +23.7%, PAT +34.2%, margin expansion, all independently verified in Phase 3 | ✅ Fully supported |
| "Powering the Next Intelligent Enterprise" (cover theme, repeated) | See AI point above | ❌ Marketing theme not reflected in segment/capex disclosure |

### 6B. Strategic priorities

Priorities named in the MD&A: (1) scaling digital capabilities, (2) upskilling workforce, (3)
expanding portfolio, (4) revitalising core IT infrastructure ("four-pronged approach," p.32). Capital
allocated: the new CWIP program (Rs21.95-24.07cr) and the new lease-financing intermediary structure
are the two concrete capital commitments visible in the financials this year, both consistent with
"revitalising core IT infrastructure" and "expanding portfolio" in a general sense, though neither is
explicitly tied back to the four-pronged framework by name anywhere in the document. Execution
evidence: named wins (Canara Bank, NABARD) and awards (Deloitte Fast 50, CMMI Level 5) are concrete and
verifiable-in-principle, a genuine positive.

### 6C. Metrics showcased vs conspicuously absent

Showcased: revenue, EBITDA, PAT, EPS, ROCE, RONW, net margin, D/E (5-year table, p.26); credit
ratings; award list; employee count (1,013). Conspicuously absent: any order-book/backlog size; any
customer-concentration metric; any receivables-ageing commentary (even though the Notes disclose it);
any discussion of the "Technology Workforce Augmentation Services" segment despite it being named a
"focus business segment" in Note 31.5; any R&D spend figure beyond "NIL."

### 6D. Tone and priority drift

Tone is confidently forward-looking and thematic throughout, consistent year-to-year in style with
the FY20 AR's own resilience-and-growth framing (FY20 AR, p.37), suggesting a consistent authorial
voice rather than a one-off marketing push. No explicit prior-year strategic priority is walked back
in words; the walk-backs found in this Annual Report (below) are silent, not verbal.

### 6E. Quiet Abandonment Check (mandatory)

Two quiet abandonments identified on this reading:

1. **AI ambition, silent drop.** The Chairman's letter and the MD&A's dedicated "Embracing the AI
   Opportunity" section (approximately 1.5 pages, p.29-30) describe AI as central to the Company's
   forward strategy ("Dynacons is investing in strengthening its AI infrastructure capabilities,
   forming strategic alliances with technology leaders, and expanding its portfolio of AI-driven
   solutions"). The operational and financial sections never take this up: R&D expenditure is
   explicitly disclosed as NIL with "no specific cost burden" (Board's Report 32(B)(iv), p.41); the
   segment note recognises only "System Integration" and "Technology Workforce Augmentation Services"
   as reportable segments (Note 31.5, p.189), with no AI-specific segment, product line, or revenue
   disclosure anywhere; and the new CWIP/capex program is not broken down in any way that would let a
   reader see an AI-infrastructure component within it. Classification: **(b) silent drop.**
   Materiality: moderate, does not change the core growth-and-margin thesis, but it does mean the
   AI narrative should be read as aspirational positioning rather than a funded, trackable strategic
   initiative, consistent with the broader disclosure-transparency concerns found in Phases 1-2.
2. **"Focus business segment" not carried into the operating narrative, silent drop.** Note 31.5
   states "The Company has identified Technology Workforce Augmentation Services as a focus business
   segment from the existing services provided by the Company," yet the MD&A's "Business Segments"
   narrative (p.27-29, covering Data Centre & Cloud, Network & Security, Workplace Solutions, Managed
   Services) never mentions this segment at all, what it does, why it was designated a focus area, or
   what progress was made, even though the segment note shows it grew from Rs5.21cr to Rs12.16cr in
   revenue this year (+133%, off a tiny base, 0.96% of total revenue). Classification: **(b) silent
   drop.** Materiality: low in Rupee terms given the segment's current size, but the gap between a
   note-level "focus" designation and zero qualitative discussion is a small, clean example of the
   same pattern found at larger scale with the lease structure and Cybercons (Phase 2): items get a
   bare mention in the Notes and no narrative context anywhere else in the report.

No implicit retraction or hedged-retreat cases were separately identified beyond the two silent drops
above; this is a narrower Quiet Abandonment finding than the volume of contradictions found in Phases
1-2, because those contradictions are inter-document (auditor vs Board's Report) rather than
opening-narrative-vs-operations in the specific sense this check targets.

### Phase 6 summary

**Phase 6 verdict: 🟡 YELLOW.** The core growth narrative is honestly told and matches the financials.
The AI and "focus segment" framing in the front matter and MD&A both go unaddressed in the operational
and financial sections, a pattern of narrative-ahead-of-substance that rhymes with, without being
identical to, the disclosure gaps found deeper in the Notes.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | (1) The "growth" leg is real and verified: standalone revenue +23.7%, PAT +34.2%, EBITDA margin +0.76pp, all independently confirmed in Phase 3, on top of an 8x standalone revenue expansion since FY17 per the operator's screener context. (2) The "reasonable" (valuation) leg is explicitly out of scope for this stage; no exit multiple is used or implied here, that determination belongs solely to Section 1B v3.3 at Stage 11. (3) The "quality" leg, which GARP requires alongside growth and reasonable valuation, is not currently met: B02's accounting-quality score of 4/10 is fully corroborated by this stage's independent primary-source verification, with the Cybercons classification integrity failure, the Schedule III arithmetic failure, and the frozen ECL against a tripling ageing tail all being genuine, unresolved, and material enough to withhold a clean PASS until at least one AGM cycle shows resolution or explanation |
| **Turnaround** | **FAIL (not applicable)** | Full reasoning per operator mandate: this is not a turnaround situation by any definition Phases 1-6 support. There is no distressed starting point (no cash losses in the current or preceding year, per CARO cl.xvii), no restructuring, no new-management narrative, and no depressed-asset-value thesis to underwrite; the Company has instead grown standalone revenue roughly 8x over the 2017-2025 window (screener context) with continuously improving margins and ROE. If anything, the risk here runs in the opposite direction from a turnaround thesis: this is a demonstrably successful multi-year growth story where the concern is deteriorating *disclosure and provisioning quality inside* an otherwise-working growth engine, not a business that needs to be turned around. A turnaround-strategy lens would misframe the actual risk in this name |
| Value+Quality | WATCHLIST | Low formal leverage (D/E 0.22x) and immaterial RPT-to-revenue (0.67%) support "quality" on the surface, but the 4/10 accounting-quality score and this stage's verification of it caps a clean Value+Quality pass regardless of entry valuation |
| Capex-Led Growth | WATCHLIST | Genuine new CWIP program (Rs21.95-24.07cr) and named large-project wins (Canara Bank, NABARD) support the thesis, but the undisclosed lease-financing business line and the unexplained Rs1,500cr borrowing-limit request both need a clearer capital-allocation rationale before this reads as clean capex-led growth rather than opportunistic balance-sheet expansion |
| Cash Flow Compounder | WATCHLIST | CFO/PAT improved to 0.885x and FCF is positive (~Rs36.8cr), but the frozen ECL, the unreconciled Note-13 cash-flow line, and the growing off-balance-sheet bank-guarantee exposure (63.4% of net worth) are cash-quality risks a pure compounder thesis should not have to carry |
| Contrarian | FAIL (not applicable) | No distress, no out-of-favour setup visible in this document; the Company is growing, winning awards, and had its credit rating assigned/reaffirmed positively this year, the opposite of a contrarian setup |
| Insider Confidence | WATCHLIST | Promoter group holds a stable ~61% combined with no pledge found in this document, a mild positive, but no evidence of recent open-market insider buying either (the only share-count changes are ESOP-driven or a family transmission); a full insider-confidence read requires the SAST/shareholding-pattern filings reviewed at Stage 8, not covered here |
| Guidance Divergence | WATCHLIST | The AR provides almost no explicit forward numeric guidance to test against actual delivery next cycle (see Phase 4C); the 5-year historical delivery table is credible, but this year's near-total absence of forward targets limits how testable the "guidance divergence" signal can be for FY26 |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot

Dynacons Systems & Solutions Ltd (DSSL), incorporated 1995, 30-year-old promoter-run (Anjaria family)
Indian IT systems-integration, infrastructure managed-services, and cloud/data-centre solutions
company, listed on BSE (532365) and NSE (DSSL). FY25 standalone revenue Rs1,266.83cr (+23.7% YoY),
PAT Rs72.41cr (+34.2% YoY), EBITDA margin 8.78%, ROE 37.28%, D/E 0.22x, net worth Rs230.92cr, promoter
group holding ~60.95% combined, ~1,013 employees, 250+ service locations claimed nationwide.

### Phase-wise verdict summary

| Phase | Verdict | One-line reason |
|---|---|---|
| 1 (Auditor/CARO) | 🔴 RED | Cybercons classified as subsidiary and associate across contradicting anchors in the same audit package, including within the Consolidated Auditor's Report itself |
| 2 (Notes) | 🔴 RED | All 15 triple-pass findings independently verified; Schedule III fails its own arithmetic; ECL frozen against a tripling ageing tail |
| 3 (Financials) | 🟡 YELLOW | Genuinely strong, improving reported numbers sit atop three incompletely disclosed new balance-sheet items |
| 4 (Risk/MD&A) | 🟡 YELLOW | Credible operating narrative; risk section and forward guidance both silent on this year's most material new items |
| 5 (Governance) | 🟡 YELLOW | Compliant on paper; one attendance flag, an eleventh-hour Audit Committee chair transition, and a Risk Committee that never met |
| 6 (Chairman/front matter) | 🟡 YELLOW | Core narrative matches delivery; AI ambition and the named "focus segment" both go unaddressed operationally |
| 7 (Best fit) | GARP, WATCHLIST | Growth verified; quality leg not yet met |

### Overall quality score

| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 6 | Compliant structure and clean fraud/whistleblower/CSR/fee record, offset by attendance, Audit Committee transition timing, and an inactive Risk Committee |
| Accounting quality | 25% | 4 | Matches B02, fully corroborated by independent primary-source verification in this stage |
| Balance sheet | 25% | 6 | Low formal leverage and growing net worth, offset by the opaque lease-financing book and 63.4%-of-net-worth bank guarantee growth |
| Earnings quality | 25% | 5 | Real, improving revenue/margin/CFO delivery, offset by frozen ECL, unreconciled cash-flow line, and a new undisclosed deferred contract cost |

**Overall quality: 5/10** (0.25x6 + 0.25x4 + 0.25x6 + 0.25x5 = 5.25, rounded to 5).

### Top 3 strengths

1. Genuine, multi-year, accelerating revenue and profit growth (standalone PAT +34.2% this year, on
   top of an 8x revenue expansion since FY17 per the operator's screener context) with real margin
   expansion and low formal leverage (D/E 0.22x, ROE 37.3%).
2. Clean core-business hygiene away from the items flagged above: no fraud, no whistleblower
   complaints, fully-spent and transparently itemised CSR, immaterial RPT-to-revenue ratio (0.67%),
   clean deferred-tax reconciliation, and disciplined inventory/payables management (payables did not
   stretch to fund growth).
3. Where management does explain a deteriorating metric, it does so candidly and specifically (the
   DSCR fall is attributed, correctly and verifiably, to lease-interest unwinding, right in the ratio
   table itself, not buried or omitted).

### Top 3 red flags

1. Cybercons Infosec's classification (subsidiary vs associate) is unresolved across at least six
   separate anchors within the same audited Annual Report, including a direct page-level
   self-contradiction inside the Consolidated Auditor's Report itself, and Cybercons' own statutory
   CARO had not been issued as of the parent's sign-off date.
2. Trade receivables ageing tail deteriorated sharply (1-2yr bucket +238.6% YoY, >6-month book +84%
   YoY) while the ECL allowance stayed frozen at Rs0.14cr for a second consecutive year, invisible to
   the average-based turnover ratio management reports.
3. A new ~Rs95.5cr lease-financing/hardware-finance structure was recognised this year with no
   counterparty, discount-rate, or credit-quality disclosure, alongside a statutory Schedule III table
   that independently fails its own year-over-year net-asset arithmetic for both group entities in a
   pattern consistent with a swapped value.

### Key monitorables for next quarter/cycle

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| 1-2yr and >6mo trade receivables ageing buckets | Further growth beyond FY25's 238.6%/84% YoY, or any ECL movement off Rs0.14cr | Note 9.1/9.2 standalone, 8.1/8.2 consolidated, next AR/quarterly ageing disclosure | Clearest under-provisioning signal; a bad-debt charge would hit FY26 P&L directly |
| Cybercons Infosec classification and CARO status | A restatement, or Cybercons' own CARO finally issued and the group's consolidation basis explicitly reconciled | FY26 Board's Report, AOC-1, CARO Annexure, Auditor's Report | Resolves whether FY25's consolidated financials used the correct consolidation method |
| Lease liability/receivable counterparty and credit disclosure | Any disclosure of counterparty name, discount rate, or receivable ageing/credit quality | Note 32.11/31.9 and successor notes, FY26 AR | Tests whether DSSL bears real, undisclosed credit risk on the Rs82.85cr lease receivable book |
| Deferred contract cost balance and amortisation | Any amortisation charge in FY26 P&L, or further unexplained growth in the Rs38.20cr balance | Note 7/6 Other Non-Current Assets, FY26 AR | Tests whether this is a genuine contract asset or a deferred expense |
| Standalone debt service coverage ratio | Further deterioration below 3.05x, or stabilisation as the lease structure matures | Note 32.12 Key Financial Ratios, FY26 AR | Tracks whether the lease-interest-driven DSCR fall is transitory or structural |
| Bank guarantees outstanding as % of net worth | Continued growth materially outpacing revenue growth (currently 63.4% of net worth vs +23.8% revenue growth) | Note 32.7(b)/31.6(b), FY26 AR | Leading indicator of order-book-linked contingent/off-balance-sheet risk |
| Audit Committee composition stability and meeting cadence | Whether the committee chaired for a full year without a late-cycle transition | FY26 Corporate Governance Report | Tests whether the FY25 eleventh-hour chair transition was a one-off or a recurring pattern |

### One-line verdict

Real growth story, unresolved disclosure integrity: GARP watchlist, not yet a clean PASS.

```yaml
stage: B03-ardeep
company: "DSSL"
run_date: "2026-07-27"
model: claude-sonnet-5
status: complete
input_gaps: []
flags:
  - {type: FLAG-CASH, reason: "Frozen ECL (Rs0.14cr, two straight years) against a receivables ageing tail that grew 238.6% (1-2yr bucket) and 84% (>6mo book), plus an unreconciled Rs29.94cr positive cash-flow adjustment for 'Other current financial assets' against a Rs20.39cr note-level increase in the same balance (standalone Cash Flow Statement p.99 vs Note 13 p.119); CFO/PAT itself improved YoY to 0.885x but the underlying provisioning and one cash-flow line do not independently confirm that improvement"}
phase_verdicts: {p1: "RED - Cybercons subsidiary/associate contradiction spans 6+ anchors incl. within the Consolidated Auditor's Report itself", p2: "RED - all 15 triple-pass findings verified; Schedule III fails own arithmetic; ECL frozen vs tripling ageing tail", p3: "YELLOW - strong improving reported numbers atop 3 incompletely disclosed new balance-sheet items", p4: "YELLOW - credible operating narrative; risk section and guidance silent on year's most material new items", p5: "YELLOW - compliant on paper; attendance flag, eleventh-hour Audit Committee chair transition, inactive Risk Committee", p6: "YELLOW - narrative matches delivery; AI ambition and named focus segment both unaddressed operationally", p7_best_fit: "GARP - WATCHLIST (growth verified, quality leg not yet met)"}
overall_quality: 5            # /10 with the four 25% components
quality_components: {governance: 6, accounting: 4, balance_sheet: 6, earnings: 5}
kill_switch_notes:
  - "Phase 1: a human reviewer would have reason to pause because the CARO annexure and the Consolidated Auditor's Report disagree with each other, and with the Board's own report, on whether Cybercons is a subsidiary or an associate"
  - "Phase 2: a human reviewer would have strong reason to pause because Schedule III fails its own arithmetic for both group entities in a pattern consistent with a swapped value, a data-integrity issue in the filing itself"
  - "Phase 3: a human reviewer would not stop on the numbers reported, but would want the Note 13/cash-flow reconciliation gap and the ECL-vs-ageing gap explained before treating reported CFO and PAT at full face value"
  - "Phase 4: a human reviewer would note that the risk-factor section systematically avoids the year's most material new judgement calls, itself informative about management's disclosure posture"
  - "Phase 5: a human reviewer would ask why none of the five available governance checkpoints (Board, Audit Committee, Risk Management Committee, statutory auditor, Board's Report) caught or reconciled the Cybercons question or the Schedule III failure before the Annual Report was finalised"
triple_pass_verification:
  verified: 15                # of 15
  discrepancies:
    - {finding_rank: 2, triple_pass_value: "CARO Annexure B cl.xxi, p.94", ar_value: "CARO Annexure A cl.xxi, p.93 (Annexure B is the separate Internal Financial Controls report); substance of the finding fully confirmed", note_ref: "Annexure A, cl.xxi"}
missing_risks:
  - {risk: "Credit/counterparty risk on the new ~Rs82.85cr lease receivable book", evidence: "No risk-factor or Notes disclosure of counterparty, discount rate, or credit quality anywhere; structure is ~36% of net worth (Note 32.11/31.9, Note 5/13)"}
  - {risk: "Receivables collection/ageing risk", evidence: "1-2yr bucket +238.6% YoY, >6mo book +84% YoY, ECL frozen (Note 9.1/9.2 p.118); absent from Risks and Concerns section (p.31)"}
  - {risk: "Governance/disclosure-integrity risk around Cybercons classification", evidence: "Spans Board's Report, AOC-1, CARO, and Consolidated Auditor's Report; absent from Critical Judgements note and risk factors alike"}
  - {risk: "Concentration/execution risk on large single-client wins (Canara Bank, NABARD)", evidence: "Celebrated as growth drivers (p.27-29) but never framed as concentration risk; no customer-concentration % disclosed anywhere"}
  - {risk: "Funding-plan risk behind the Rs1,500cr borrowing-limit authorisation request", evidence: "Notice Item 5, p.24, sought as an 'enabling provision' with no project list or draw plan, against a Rs51.89cr current debt base"}
guidance_table:
  - {claim: "IT system integration industry outlook remains highly positive", number: "NOT FOUND IN DOCUMENT", timeframe: "unspecified", credibility: "not testable, standard boilerplate"}
  - {claim: "Strong order book, NABARD Core Banking as a Service deployment", number: "NOT FOUND IN DOCUMENT (no order-book value disclosed)", timeframe: "unspecified", credibility: "not testable this cycle"}
  - {claim: "Borrowing limit increase sought", number: "Rs1,500 crore ceiling", timeframe: "enabling, no timeframe", credibility: "unsupported by any disclosed financing plan or project list"}
  - {claim: "5-year consolidated financial delivery record", number: "Revenue Rs437cr (FY21) to Rs1,274cr (FY25); PAT Rs8.54cr to Rs72.49cr; ROCE 21.8% to 38.9%", timeframe: "historical", credibility: "credible, cross-checked and consistent with Phase 3's independent verification"}
monitorables:
  - {metric: "1-2yr and >6mo trade receivables ageing buckets", threshold: "further growth beyond FY25's 238.6%/84% YoY, or any ECL movement off Rs0.14cr", where: "Note 9.1/9.2 standalone, 8.1/8.2 consolidated, FY26 AR/quarterly", why: "clearest under-provisioning signal; a bad-debt charge would hit FY26 P&L directly"}
  - {metric: "Cybercons Infosec classification and CARO status", threshold: "restatement, or Cybercons' own CARO issued and consolidation basis explicitly reconciled", where: "FY26 Board's Report, AOC-1, CARO Annexure, Auditor's Report", why: "resolves whether FY25 consolidated financials used the correct consolidation method"}
  - {metric: "Lease liability/receivable counterparty and credit disclosure", threshold: "any disclosure of counterparty name, discount rate, or receivable ageing/credit quality", where: "Note 32.11/31.9 and successor notes, FY26 AR", why: "tests whether DSSL bears real, undisclosed credit risk on the Rs82.85cr lease receivable book"}
  - {metric: "Deferred contract cost balance and amortisation", threshold: "any amortisation charge in FY26 P&L, or further unexplained growth in the Rs38.20cr balance", where: "Note 7/6 Other Non-Current Assets, FY26 AR", why: "tests whether this is a genuine contract asset or a deferred expense"}
  - {metric: "Standalone debt service coverage ratio", threshold: "further deterioration below 3.05x, or stabilisation", where: "Note 32.12 Key Financial Ratios, FY26 AR", why: "tracks whether the lease-interest-driven DSCR fall is transitory or structural"}
  - {metric: "Bank guarantees outstanding as % of net worth", threshold: "continued growth materially outpacing revenue growth (currently 63.4% vs +23.8%)", where: "Note 32.7(b)/31.6(b), FY26 AR", why: "leading indicator of order-book-linked contingent/off-balance-sheet risk"}
  - {metric: "Audit Committee composition stability and meeting cadence", threshold: "a full year without a late-cycle chair transition", where: "FY26 Corporate Governance Report", why: "tests whether the FY25 eleventh-hour transition was a one-off"}
strengths_top3:
  - "Genuine, multi-year, accelerating revenue and profit growth (standalone PAT +34.2%, 8x revenue expansion since FY17 per screener context) with real margin expansion and low formal leverage (D/E 0.22x, ROE 37.3%)"
  - "Clean core-business hygiene: no fraud, no whistleblower complaints, fully-spent transparently itemised CSR, immaterial RPT-to-revenue ratio (0.67%), clean deferred-tax reconciliation, disciplined payables/inventory management"
  - "Candid, specific management explanation where a metric did deteriorate (DSCR fall correctly and verifiably attributed to lease-interest unwinding, disclosed in the ratio table itself)"
red_flags_top3:
  - "Cybercons Infosec classified as both subsidiary and associate across 6+ anchors in the same audited Annual Report, including a direct page-level self-contradiction inside the Consolidated Auditor's Report; Cybercons' own statutory CARO was not issued as of the parent's sign-off"
  - "Trade receivables ageing tail deteriorated sharply (1-2yr bucket +238.6% YoY, >6mo book +84% YoY) while ECL stayed frozen at Rs0.14cr for a second consecutive year, invisible to the average-based turnover ratio management reports"
  - "New ~Rs95.5cr lease-financing structure recognised with no counterparty/rate/credit disclosure, alongside a statutory Schedule III table that independently fails its own year-over-year net-asset arithmetic for both group entities in a pattern consistent with a swapped value"
best_fit_strategy: "GARP (WATCHLIST)"
one_line_verdict: "Real growth story, unresolved disclosure integrity: GARP watchlist, not yet a clean PASS."
```
