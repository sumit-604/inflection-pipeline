# STAGE 3: AR BACKWARD DEEP DIVE — Fabtech Technologies Ltd (FABTECH)
Run: fabtech-2026-09-26. Basis: consolidated (standalone noted where materially
different). AR is OCR text (INR lakh); load-bearing digits cross-checked
against the audited results filing (text layer) and the RHP/other filings
per README-AR-TEXT.md. Corrected balance-sheet anchor per Stage 2: trade
receivables Rs 20,433.51 lakh, total assets Rs 65,370.29 lakh (Note 13,
MD&A, financial-instruments note, and the exchange-filed audited FY26
results all agree; confirmed again in this stage at Results p.316/325:
"2043351" / "6537029"). The AR consolidated balance-sheet FACE figures
(Rs 24,151.90 lakh / Rs 69,088.68 lakh) are the confirmed drafting error.

---

## PHASE 1: AUDITOR'S REPORT & CARO

**1A Core opinion.** Standalone and consolidated: both unmodified/unqualified
(Ajmera & Ajmera, FRN 018796C; standalone AR p.86 (txt), consolidated AR
p.140 (txt)). No going-concern language anywhere (confirmed, both opinions,
consistent with B02 Pass 3). Internal financial controls: unmodified opinion
on both bases (Annexure B, standalone AR p.95-96 (txt); consolidated AR
p.148 (txt)).

**1B Key Audit Matters.**
| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Recoverability/valuation of ECL allowance on overdue trade receivables (both standalone and consolidated reports, identical KAM) | Rs 5,887.55 lakh overdue >365 days (consol., before ECL); subjective ECL judgement | Auditor tested ECL methodology, inputs, controls (AR p.85-86, p.139-140 txt) | 🔴 |

No separate KAMs on impairment, provisioning generally, or fair value beyond
the one named. No revenue-recognition KAM despite milestone/shipment basis —
worth noting as an absence given the archetype's revenue-timing complexity
(cross-ref Phase 4B).

**1C Emphasis of Matter / Other Matters.** No Emphasis of Matter. Other
Matters (consolidated report only): reliance on another auditor for "01
foreign subsidiary" — total assets (pre-consolidation) Rs 15,589.55 lakh
(22.5% of corrected consol. total assets), revenue Rs 17,378.57 lakh, PAT Rs
1,274.06 lakh (33.2% of consol. PAT Rs 3,835.80 lakh) — and for "01
associate" (Group share of PAT Rs 33.52 lakh) (AR p.142-143 txt). Annexure
A names only the first-tier entities (Fabtech Technologies LLC, UAE;
FT Institutions Pvt Ltd; Mark Maker Engineering Pvt Ltd; FABL International
Technologies LLP) — the two step-down subsidiaries (FTS Cleanrooms Systems
LLC, Fabtech Lifecare Company) are nested inside the UAE entity's own
audited consolidation, not separately named in Annexure A (AR p.146 txt).
This is a listing-convention gap, not evidence of misconsolidation, but it
means **a third of consolidated profit is certified only by an auditor
this pipeline cannot independently verify** — a genuine Phase 1F item.

**1D CARO 2020, clause by clause (standalone; consolidated report cross-refs
the same clauses for group entities).**
- Clause (ii) inventory: physically verified, no material discrepancies (AR
  p.90 txt). 🟢
- Clause (iii) loans to related parties: standalone loans/ICDs to
  subsidiaries (domestic+foreign) and associates total Rs 3,596.41 lakh,
  **99.40% of all standalone loans/advances-in-nature-of-loans** (Rs
  3,618.30 lakh), all "repayable on demand," none overdue >90 days (AR
  p.91-92 txt). This is a large, group-concentrated ICD book funded from
  the listed entity's own balance sheet — real exposure, not itself an
  irregularity (auditor found terms "not prejudicial"), but a scale worth
  naming: repayable-on-demand loans to a domestic subsidiary, a foreign
  subsidiary, and two associates make up essentially all of the Company's
  outstanding loan book. 🟡
- Clause (vii)(a) statutory dues: single Rs 22,371 TDS (Section 194C) delay
  at the Holding Company, paid within three weeks (23-Apr-2026) of the
  30-Apr-2026 due date (AR p.93 txt) — confirms B02 Pass-2 downgrade to 🟡.
  Separately qualified (consolidated report, Other Legal & Regulatory
  Requirements table, AR p.143 txt): FT Institutions Private Limited
  (subsidiary) and Mark Maker Engineering Private Limited (associate), own
  amounts **NOT FOUND IN DOCUMENT** (not reproduced in this AR; carried
  from B02 input_gaps).
- Clause (ix) borrowing defaults: none; no willful-defaulter declaration;
  term loans applied for stated purpose; no short-term-for-long-term
  diversion; no funds raised to meet subsidiary/associate obligations; no
  pledge of group-entity securities. 🟢
- Clause (x)(a) IPO fund utilisation — **auditor-reported delay**: "an
  amount of Rs 6,600 lakhs was proposed to be utilized towards Working
  Capital Requirements during Fiscal Year 2026, against which the Company
  has utilized Rs 2,747.24 lakhs up to March 31, 2026, resulting in a delay
  in the implementation of the said object" (AR p.93-94 txt). Management's
  explanation (per the auditor): met working capital needs through
  borrowings/internal accruals instead. This is the auditor independently
  confirming the LBF4 IPO-deployment gap, not just a monitoring-agency
  observation. 🔴 for the specific WC-object timeline the offer document
  itself set; not a going-concern matter.
- Clause (xi) fraud: none by or on the Company; no whistleblower complaints;
  no Section 143(12)/ADT-4 report required. 🟢
- Clause (xvii) cash losses: none in current or preceding year (not
  applicable). 🟢
- Clause (xx) CSR: fully compliant, no unspent amount. 🟢
- No Nidhi, no Section 185 loans to directors, no non-cash director
  transactions, no benami proceedings, no RBI registration issue.

**1E Auditor continuity.** Ajmera & Ajmera (FRN 018796C) reappointed at the
7th AGM (held for FY24-25) for five years to the 12th AGM (FY29-30) — no
rotation-year risk in this cycle. Fee mix (consolidated, Note 39, AR
p.181-182 txt): Statutory audit Rs 10.23 lakh + Tax audit Rs 1.30 lakh + GST
audit Rs 1.00 lakh = **Rs 12.53 lakh audit-related**; Certification and tax
consultancy Rs 12.67 lakh (non-audit). **Non-audit fees (Rs 12.67 lakh)
narrowly exceed audit-related fees (Rs 12.53 lakh)** — triggers the house
flag threshold, though the absolute gap (Rs 0.14 lakh) is immaterial. 🟡
Separately, the Corporate Governance Report states "Total fees for all
services paid by the Company and its subsidiaries, on a consolidated basis…
Rs. 10.33 Lakhs" (AR p.75 txt, CG report) — **this figure does not
reconcile with Note 39's consolidated total of Rs 25.20 lakh** for the same
year and the same "all services" scope. New finding, not in B02: a third
internal numeric mismatch in this AR (after the balance-sheet face error
and the duplicate note "60"). 🔴 (disclosure-quality pattern, not
misappropriation).

**1F Standalone vs consolidated differences.** Same KAM, same audit firm,
unmodified both bases. Consolidated report adds the CARO qualification
table naming FT Institutions and Mark Maker alongside the Holding Company
(1D above) and the other-auditor reliance for the UAE entity (1C above).
No standalone-only qualification beyond what flows through consolidation.

**Phase 1 summary + verdict.** Both audit opinions clean and the KAM is
narrowly but correctly targeted at the single worst-evidenced number in the
filing (receivables). But the auditor's own CARO clause (x)(a) independently
confirms the IPO-deployment shortfall, and the fee-note vs CG-report mismatch
is a new, auditor-adjacent disclosure-quality flag. **Verdict: 🟡 Watch.**
Kill-switch (informational): a human reviewer would not stop on the audit
opinion itself (clean, well-evidenced KAM), but would flag the CARO(x)(a)
deployment delay and the auditor-reliance concentration (33% of PAT from an
entity this pipeline cannot verify) for the dossier. Continuing.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the Phase 2 special instruction: the Top 15 from B02 are verified below
against the primary document, then extended with items the triple-pass
did not reach in the sections this stage read directly (CG report, MD&A,
segment note, RPT note, auditor's report, Board's Report, AGM notice).

**2-special: Triple-pass Top 15 verification.**
All 15 findings independently confirmed against the source pages read in
this stage (auditor's report, consolidated financial statements, Note
27/39/40/43/44/49/50/52/53/60). No discrepancies found between the
triple-pass values and the primary document. `triple_pass_verification:
verified 15/15, discrepancies: []`. Specific confirmations of note:
- Finding 1 (receivables KAM, Rs 5,887.55 lakh): confirmed verbatim in the
  auditor's KAM text (AR p.141 txt).
- Finding 2 (BS-face error): confirmed again in this stage from the raw
  balance-sheet face (Rs 24,151.90 lakh / Rs 69,088.68 lakh, AR p.150 txt)
  against the exchange-filed audited results (Rs 20,433.51 lakh / Rs
  65,370.29 lakh, Results p.316/325).
- Finding 4 (customer rotation): confirmed with exact percentages from
  Note 44 (AR p.184-185 txt) — Al-Afiya 1.58%→12.55%, Himalaya
  13.98%→8.09%, Qomel Company Arabia 13.51%→3.46%, Massoun Darou
  11.27%→3.38%.
- Finding 7 (exceptional items): confirmed, Note 40 (AR p.182 txt) —
  "Profit on stake sale of FABL International Technologies LLP" Rs 177.49
  lakh (FY26); "Profit on sales of Unlisted shares" Rs 1,784.86 lakh (FY25,
  the TSA-to-Thermax disposal per Note 59).
- Finding 12 (cross-collateralised guarantees): confirmed, Note 43
  contingent liability table (AR p.183 txt) — corporate guarantees to
  Fabtech Technologies Cleanrooms Limited Rs 1,000.00 lakh and Fabsafe
  Technologies Private Limited Rs 600.00 lakh, unchanged both years.
- Finding 14 (deconsolidation distortion): confirmed and **self-disclosed
  by the company** in Note 50's own variance column — inventory turnover
  +46.48% is explained: "As a result of the sale of the stake in one of
  the subsidiaries average inventory has been reduced" (AR p.196 txt).

**2A Accounting policy aggressiveness.** No new findings beyond B02;
confirmed no revaluation of PP&E/ROU/intangibles this year (CARO
1(i)(d)); Ind AS 116 lease additions modest (Rs 40.28 lakh, Note 51).

**2B RPT map, extended.** Purchases from Fabtech Technologies Cleanrooms
Limited (promoter-group, separately BSE SME-listed): Rs 2,358.58 lakh FY26
(5.7% of consol. revenue) vs Rs 2,985.00 lakh FY25 (9.1% of revenue) — a
material, though shrinking, RPT purchase line with the same entity that
receives/gives the Rs 1,000 lakh corporate guarantee (Note 49, AR p.192-193
txt). **New finding, not in B02:** the related-party list (Note 49, section
d, "Companies/Firms in which directors/KMP have significant influence")
names **"Fabtech Technologies KSA"** as a related party, with FY26 sales
of Rs 43.73 lakh and a trade-receivable balance of Rs 130.20 lakh (up from
Rs 15.76 lakh FY25) (AR p.193-194 txt). This is a **third, distinctly
named Saudi entity** in the group ecosystem, separate from both the
consolidated 100%-owned step-down subsidiary "Fabtech Lifecare Company,
Saudi Arabia" (Note 52-53) and the pending-acquisition target "Specialized
Contracting Activities LLC" (announced Jun-2026, per B00). Three
separately named Saudi-labelled entities across three different structural
roles (consolidated subsidiary, non-consolidated related party, pending
acquisition target) is a genuine group-structure-clarity concern for LBF3,
beyond what B02 flagged. Also new: **"Alanar One Health Equity Fund"**
appears for the first time with an FY26-only Rs 660.00 lakh investment
transaction and closing balance (no FY25 comparative), and **"G7 Universal
LLC"** appears with a new Rs 359.84 lakh "Sales commission" line item and
a Rs 215.31 lakh trade-payable balance (both NOT FOUND with amounts in the
FY25 column) — three new RPT counterparties this stage did not see named
in B02, fed to `ar_new_downstream_entities` below.

**2C Contingent liabilities, extended.** Total consolidated contingent
liability Rs 4,515.10 lakh (FY26) vs Rs 3,256.20 lakh (FY25) (Note 43, AR
p.183 txt). As % of net worth (Rs 41,976.93 lakh): **10.75%** — under the
25% flag threshold. As % of PAT (Rs 3,835.80 lakh): **117.7%** — **crosses
the >100% flag threshold** (FY25: Rs 3,256.20/Rs 4,645.29 = 70.1%, under
threshold). New finding: the >100%-of-PAT contingent-liability flag fires
for the first time this year, driven by the performance-guarantee line for
turnkey project execution nearly doubling (Rs 1,570.67 lakh → Rs 2,829.57
lakh), which is itself a symptom of the larger, faster-growing order book
rather than a going-concern signal.

**2D Receivables.** As per B02 (deteriorating, >6mo 43.6% vs 35.3%, KAM);
confirmed geography split (Note 44b): Saudi Arabia trade receivables more
than doubled (Rs 2,587.75 lakh → Rs 6,336.63 lakh) even as Saudi Arabia
*revenue* fell (Rs 9,471.57 lakh → Rs 8,272.36 lakh) — receivables growing
against a shrinking revenue base in the single largest export market is a
sharper, geography-specific version of the ageing concern than the
group-level figure alone shows.

**2E Inventory.** Confirmed mechanical FABL-deconsolidation effect (2A
above); no like-for-like write-down evidence found; no new finding.

**2F Borrowings.** No new finding beyond B02 (cross-collateralised
security, corporate guarantees). Facility II (cash credit/packing credit,
sanctioned Rs 1,000 lakh) secured by personal guarantees of Mr. Aasif Khan,
Mr. Hemant Anavkar and Mr. Aarif Khan and a lien on 50% of a Rs 10 Cr fixed
deposit (AR p.178 txt) — personal promoter guarantees backing a listed
company's working-capital facility, disclosed but worth naming as an
unusual-for-a-newly-listed-entity security structure.

**2G Deferred tax.** Deferred tax asset increased Rs 242.63 lakh (FY25) to
Rs 387.13 lakh (FY26); no reconciliation red flags found in the sections
read (detailed DTA/DTL breakup not separately re-extracted this stage;
relies on B02).

**2H Exceptional items / goodwill / ESOP / leases / post-BS events.**
Goodwill Rs 3,699.81 lakh (FY25) → Rs 2,296.83/2,294.83 lakh (FY26, two
slightly different figures appear across the balance sheet face and Note
53's goodwill roll-forward — Rs 2,296.83 lakh on the face, Rs 2,294.83
lakh in the Note 53 roll-forward table, a Rs 2.00 lakh gap that traces to
the "FT Institute" Rs 2.00 lakh goodwill line being shown separately) — not
material, but a fourth small internal reconciliation gap in the same AR.
No ESOP scheme in force (NRC policy references one, but Board's Report
confirms no ESOP shares issued this year). Leases: ROU assets Rs 2,597.70
lakh, lease liability Rs 2,690.19/2,690.20 lakh (Note 51); no new finding.
Post-balance-sheet events: only the Rs 0.60/share dividend disclosed in the
notes (Note 60, "Events after the Reporting period," AR p.200 txt) — the
Jun-2026 acquisition filings remain unaddressed in the notes, as B02 found.

**New finding — duplicate/conflicting IPO-utilisation tables.** The
Board's Report (AR p.24 txt) states: Total IPO proceeds Rs 23,029.65 lakh,
**total utilised Rs 5,707.70 lakh**, unutilised Rs 17,321.95 lakh (implied).
Consolidated Note 60 (AR p.200 txt) states the same total proceeds but
**total utilised Rs 5,107.70 lakh**, unutilised Rs 17,921.95 lakh. The two
tables in the *same annual report* disagree by **exactly Rs 600.00 lakh**
on IPO utilisation as of the same balance sheet date. Both tables agree on
the Working Capital line (Rs 2,747.24 lakh utilised) and the General
Corporate Purposes line (Rs 125.00 lakh utilised); the gap traces to the
Issue Expenses line (Board's Report: Rs 2,235.46 lakh utilised; Note 60's
OCR is degraded here and does not cleanly state a figure, but the
arithmetic implies Rs 1,635.46 lakh if the Rs 600 lakh delta sits entirely
there) or possibly a reclassification between Issue Expenses and General
Corporate Purposes. **This could not be fully resolved from the OCR text
and needs page-image confirmation**; flagged as an input_gap rather than
asserted as a hard number. This is the AR's **third** internal numeric
inconsistency (after the balance-sheet face and the CG-report/Note-39
auditor-fee mismatch), and a **fourth** appears below (2G/ROE).

**New finding — two ROE/RONW disclosures that do not reconcile.** MD&A
(AR p.47 txt) states RONW FY26 = 9.14%, FY25 = 26.83%. Note 50 "Analytical
ratios" (AR p.196 txt) states Return on equity FY26 = 12.94%, FY25 =
30.46%. Both are labelled as the same metric (profit after tax over
shareholders' equity) for the same two years, in the same annual report,
and do not match on either year. Likely explained by average-vs-closing
equity denominators, but **the AR does not disclose which convention each
table uses**, so a reader cannot reconcile them without external
recomputation. Flagged, not resolved.

**Phase 2 summary.** B02's 5/10 accounting-quality score is reaffirmed and,
if anything, modestly *reinforced downward* by this stage's four
additional internal-inconsistency findings (auditor-fee note vs CG report;
two IPO-utilisation tables; two ROE tables; a Rs 2.00 lakh goodwill
roll-forward gap) on top of the balance-sheet face error and the duplicate
note "60" B02 already found. This is now **six** independent instances of
internally-inconsistent disclosure in one annual report — a pattern, not a
one-off typo. **Verdict: 🔴 Red Flag** (disclosure-quality dimension);
consistent with, and reinforcing, B02's finding.
Kill-switch (informational): a reviewer would not stop here (no evidence of
fraud or misappropriation — every gap found is a reconciliation/drafting
issue, not a hidden liability), but the volume of internal mismatches at
this specific company, in its first full-year post-listing AR, is itself
the finding to carry forward. Continuing.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow first, then balance sheet, then P&L)

**3A Cash flow.**
| Metric | FY26 | FY25 |
|---|---|---|
| PAT | Rs 3,835.80 lakh | Rs 4,645.29 lakh |
| CFO | Rs 47.74 lakh | Rs (3,614.49) lakh |
| **CFO/PAT** | **1.2%** | **-77.8%** |
| EBITDA (PBT+Dep+Fin cost) | Rs 5,773.46 lakh | Rs 6,513.73 lakh |
| **CFO/EBITDA** | **0.8%** | **-55.5%** |
| Capex | Rs 470.81 lakh | Rs 2,478.20 lakh |
| Capex/Depreciation | 0.89x (below 1x) | 9.51x |
| FCF (CFO − capex) | Rs (423.07) lakh | Rs (6,092.69) lakh |

**Two consecutive years of CFO/PAT far below the 0.7x flag threshold** —
confirms FLAG-CASH (B02) with hard cash-flow-statement numbers, not just a
balance-sheet inference. **CFO quality checks:**
- One-time inflators: an unrealised FX gain of Rs 1,034.62 lakh is
  correctly *subtracted* as a non-cash adjustment in the CFO
  reconciliation (not inflating CFO) — clean treatment.
- Interest classification: interest income (Rs 790.46 lakh) is added back
  in operating adjustments and the cash actually received (Rs 677.05 lakh)
  is shown under investing activities — standard Ind AS 7 classification,
  not aggressive.
- **Inventory rundown propping up CFO**: the Rs 3,807.43 lakh decrease in
  inventories that helped FY26's operating cash generation is, by the
  company's own admission (Note 50), a **mechanical artefact of the FABL
  deconsolidation**, not a genuine like-for-like reduction in working
  capital. Strip this out and FY26's already-weak CFO would read
  materially worse on a like-for-like consolidation basis — the true
  organic cash drag from the growing, ageing receivables book is
  understated at the headline CFO line.
- Payable stretch: trade payables rose Rs 4,450.79 lakh (AR consolidated
  cash-flow note) — but see the discrepancy below; either way, payables
  grew far slower than revenue or receivables (B02 finding 15), so this is
  a modest, not manufactured, offset.
- **New finding — cash-flow-statement working-capital lines do not match
  between the AR and the exchange-filed audited results**, though the
  subtotal they both roll up to is identical. The AR's consolidated cash
  flow note (AR p.152 txt) shows "Decrease/(Increase) in trade receivables
  (8,655.02)" and "(Decrease)/Increase in trade payables 4,450.79"; the
  exchange-filed FY26 audited results (Results p.388/392) show the same
  two lines as **(4,936.63)** and **732.40** respectively. Both filings
  agree exactly on "Cash generated from operations" (Rs 1,255.97 lakh) and
  on every other cash-flow subtotal (CFO Rs 47.74 lakh, CFI Rs (11,231.11)
  lakh, CFF Rs 18,965.97 lakh, closing cash Rs 8,688.16 lakh) — so the
  bottom line is not in dispute, but the *receivables-specific* cash drag
  cannot be pinned to a single number across the two documents that should
  be identical. This directly affects any attempt to isolate "how much
  cash the receivables deterioration actually cost this year," which is
  the single most decision-relevant number in the whole filing. Flagged,
  not resolved; needs page-image confirmation of the AR figure or a
  restated exchange filing.
- Cash pile: cash + other bank balances rose from Rs 3,500.98 lakh (FY25)
  to Rs 20,857.14 lakh (FY26) — entirely IPO-financed (financing activities
  brought in Rs 18,965.97 lakh net, dominated by Rs 20,752.03 lakh gross
  IPO proceeds), **not operations-financed** (CFO contributed only Rs
  47.74 lakh of the increase). Rs 11,744.92 lakh of IPO cash was placed
  into >3-month fixed deposits during the year — consistent with the 78%
  IPO-proceeds non-deployment already flagged in Phase 1/2.

**3B Balance sheet** (corrected anchor: total assets Rs 65,370.29 lakh
FY26 vs Rs 42,655.80 lakh FY25).
| Ratio | FY26 | FY25 | Source |
|---|---|---|---|
| Debt/Equity | 0.10x | 0.32-0.34x | Note 50 (0.10/0.32) vs MD&A (0.10/0.34) — small internal gap, immaterial |
| Current ratio | 2.21-2.50x | 1.37-1.45x | MD&A vs Note 50, small gap |
| Interest coverage | 36.84x | 31.09x | MD&A |
| ROCE | 11.05% | 19.83% | Note 50 |
| Return on Investment (asset basis) | 8.56% | 11.09% | Note 50 |
| ROE / RONW | 12.94% (Note 50) / 9.14% (MD&A) | 30.46% (Note 50) / 26.83% (MD&A) | see Phase 2 finding — does not reconcile |
| Goodwill / Net worth | 5.5% | 21.4% | Rs 2,296.83 lakh / Rs 41,976.93 lakh (FY26); Rs 3,699.81 / Rs 17,311.36 (FY25) |

**DuPont read**: Net margin 9.34% × Asset turnover 0.63x × Equity multiplier
1.56x ≈ ROE in the high single digits — consistent with the MD&A's own
narrative that the ROE/RONW decline is **overwhelmingly an enlarged-equity-
base (IPO) effect, not an operating deterioration** ("the increase in net
worth outpaced growth in profit after tax," MD&A, AR p.48 txt) — this
specific management explanation is credible and matches the DuPont math.
ROCE and Return-on-Investment fell on a like-for-like capital-employed
basis too, though, so **some of the profitability decline is real
operating margin compression, not only equity dilution** — see 3C.

**3C P&L.**
- Revenue Rs 41,077.18 lakh (+25.75% consol.), broad-based across nine
  geographies (Note 44a).
- **Other income Rs 2,055.77 lakh = 42.6% of PBT (Rs 4,827.41 lakh)** —
  well above the 20% flag threshold. Within it, net FX gain Rs 1,188.73
  lakh = 57.8% of other income and 24.6% of PBT alone (B02 finding 3,
  reconfirmed with the PBT-percentage framing this stage adds).
- Implied EBITDA margin: FY26 Rs 5,773.46 lakh / Rs 41,077.18 lakh =
  **14.05%**; FY25 Rs 6,513.73 lakh / Rs 32,666.85 lakh = **19.94%** — a
  real ~590bp compression, directionally consistent with the LBF4 "OPM 15%
  → 9%" screener read (definitions differ; both readings point the same
  direction — margin compression is real, not a definitional artefact).
- Exceptional items: two consecutive years of gains from group/associate
  stake disposals (Rs 1,784.86 lakh FY25 TSA-to-Thermax; Rs 177.49 lakh
  FY26 FABL) — recurring "exceptional" label is itself an earnings-quality
  flag (B02 finding 7, reaffirmed).
- Tax rate: effective ~20.5% (FY26) vs ~23.1% (FY25) — no aggressive swing.
- EPS: basic = diluted both years (Rs 10.00 FY26, Rs 14.34 FY25) — no
  dilution gap; clean.

**Phase 3 summary + cross-reference.** Phase 3 independently confirms, with
hard cash-flow-statement arithmetic, everything B02 inferred from the
balance sheet: two years of near-zero-to-negative cash conversion, propped
up in FY26 by a mechanical deconsolidation effect the company itself
discloses; other income (FX-heavy) inflating PBT past the 20% threshold;
real (not just optical) margin compression; and a cash pile that is
entirely IPO-financed rather than operations-financed. **Verdict: 🔴 Red
Flag.** Kill-switch (informational): a reviewer would flag this hard for
the dossier — cash conversion is the single most important unresolved fact
in the filing — but would not halt, since the company discloses (rather
than hides) the receivables deterioration and the deconsolidation effect.
Continuing.

---

## PHASE 4: RISK FACTORS & MD&A

**4A Disclosed risks — real vs boilerplate.** The MD&A risk section (AR
p.44 txt) is more specific than typical boilerplate: it explicitly names
"Rising trade receivables and collection risk" and "Working capital
intensive business operations" as risks in the same year the receivables
book is deteriorating — a candid, non-evasive disclosure. FX volatility,
milestone-billing dependence, geopolitical risk in overseas territories,
and input-cost inflation are all named and map to real, evidenced exposures
found in Phases 1-3.

**4B Missing risks** (obvious from Phases 1-3 but absent from the risk
section):
1. **Related-party/group-structure concentration risk** — Rs 3,596.41 lakh
   of standalone loans (99.4% of the loan book) to subsidiaries/associates,
   cross-collateralised guarantees with non-consolidated promoter-group
   entities (Cleanrooms Ltd, Fabsafe), and material RPT purchase volume
   (5.7-9.1% of revenue) are not named as a risk factor despite their scale.
2. **Auditor-reliance concentration** — a third of consolidated PAT is
   certified by another auditor this pipeline cannot verify; not disclosed
   as a risk.
3. **Governance-continuity risk** — both FY26 independent directors
   departed within a quarter of the AR's signing, and the Company Secretary
   resigned shortly after (24-Sep-2026, per B00 LBF3); not named as a risk
   anywhere in the AR, though each departure is individually disclosed as
   a factual event.
4. **IPO-non-deployment / opportunity-cost risk** — 78% of net IPO
   proceeds sit undeployed at year-end, with the auditor's own CARO(x)(a)
   flag on the working-capital-object timeline; not named as a risk in
   MD&A despite being the subject of a formal auditor qualification.
Likely reason for omission: MD&A risk sections in India routinely track a
standard template (FX, execution, competition, regulation) rather than a
company-specific bottom-up risk register; the omissions above are the kind
that a standard template misses by construction, not necessarily a
deliberate management choice to conceal.

**4C MD&A deep dive.** Credit-taking: revenue growth credited to "strong
overseas execution and expansion of international business operations"
(AR p.43 txt) — plausible, matches the geography data. Blame pattern:
receivables decline explained by "growth in international business
operations and longer project realization cycles" (AR p.46-47 txt) — an
external/structural framing that is consistent with, not evasive of, the
facts (the auditor independently confirms the same mechanism via the KAM).
Segment analysis: unusually granular geography-level revenue and
receivables breakdowns are given (a positive transparency signal relative
to peers), but **no segment profitability** is disclosed ("interwoven /
intermix nature of business," Note 44) — this blocks any test of whether
margin, not just revenue, is holding up market by market.
**Forward guidance table**: this AR itself carries **no quantified FY27
guidance** (no numeric revenue/margin targets in the Board's Report, MD&A,
or CEO/Chairperson letters) — the "20-25% organic growth, PAT margin
9-11%" guidance named in B00 LBF1 comes from the Q4 FY26/FY27 concalls, not
this document. **NOT FOUND IN DOCUMENT** inside the AR; credibility check
against delivery is deferred to the concall-reading stages.

**4D Tone and credibility (1-5 each, evidenced):**
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3/5 | Candid prose on receivables/CFO impact in MD&A, but six internal numeric mismatches across the filing (Phase 2) undercut it |
| Consistency | 2/5 | BS face vs Note 13; two IPO-utilisation tables; two ROE tables; CG-report vs Note-39 auditor fee; duplicate note "60"; Rs 2 lakh goodwill gap |
| Specificity | 4/5 | Real geography-level revenue/receivables tables, real ratio values, explicit variance explanations in Note 50 |
| Accountability | 4/5 | CEO letter explicitly isolates the FY25 exceptional item and states FY26 profit is core-driven, rather than hiding the YoY PAT decline |
| Capital allocation sense | 2/5 | 78% of IPO proceeds undeployed ~10 months after listing; inorganic-growth bucket at 0%; auditor-flagged WC-object delay |

**Phase 4 summary.** MD&A is more candid than average on the year's central
negative fact (receivables/cash), which is a genuine strength; but the
missing-risk list and the capital-deployment gap between stated intent and
actual utilisation are real. **Verdict: 🟡 Watch.** No contradiction with
Phases 1-3 beyond what is already integrated above. Continuing.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

**5A Board composition.** Six members at FY26-end: Mr. Naushad Panjwani
(Chairperson, Independent), Mr. Hemant Anavkar (Executive, promoter), Mr.
Amjad Arbani (Non-Executive), Mr. Chirag Doshi (Non-Executive), Mr. Shyam
Khante (Independent), Ms. Aparna Sharma (Independent). Attendance strong:
90.91-100% across all six directors, 11 board meetings held (AR p.50-51
txt). No director exceeds the permissible board-seat count; no ID has
tenure >10 years (all appointed 2024, well inside limits).

**Real governance flag — cross-board membership with the largest RPT
counterparty.** Per the "Other Directorships" table (AR p.52 txt):
- Mr. Amjad Arbani — Executive Director, Fabtech Technologies Cleanrooms
  Limited.
- Mr. Chirag Doshi — Non-Executive Director, Fabtech Technologies
  Cleanrooms Limited.
- Mr. Shyam Khante — Non-Executive Independent Director, Fabtech
  Technologies Cleanrooms Limited.

**Three of the six FY26 board members — half the board, including one of
three Independent Directors — sit simultaneously on the board of Fabtech
Technologies Cleanrooms Limited**, the promoter-group's separately BSE
SME-listed entity that is also FABTECH's single largest disclosed
related-party purchase counterparty (Rs 2,358.58 lakh, 5.7% of FY26
revenue) and a Rs 1,000 lakh corporate-guarantee counterparty. An
"independent" director sitting on the board of the company's own largest
RPT counterparty is a real independence-quality concern the CLAUDE.md Phase
5A instruction is written to catch. 🔴

**Board-level KMP/ID churn.** Both FY26 independent directors — Ms. Aparna
Sharma and Mr. Shyam Khante — completed exactly two-year terms and ceased
office within a quarter of each other (02-Apr-2026 and 25-Jun-2026), both
scheduled/disclosed events (tenure completion, not resignation-for-cause),
replaced by two new independent directors (Ms. Rupal Haria, Ms. Bharti
Khanna) via postal ballot in mid-2026. Combined with the Risk Management
Committee's dissolution (Feb-2026, cited as non-mandatory for the
Company's size) and the Company Secretary's own resignation shortly after
(per B00 LBF3, 24-Sep-2026), FY26/early-FY27 shows a real cluster of board
and KMP turnover in the company's first year as a listed entity — every
individual event is disclosed and appears procedurally clean, but the
clustering itself is worth tracking. 🟡

**5B Committees.** Audit (4 members incl. Chairperson Panjwani, 7 meetings,
full attendance), NRC (4 members, 3 meetings, full attendance),
Stakeholders' Relationship (4 members, 1 meeting), CSR (4 members, 2
meetings), Risk Management (dissolved Feb-2026). No standalone RPT
committee — folded into Audit Committee per standard (not SEBI-mandated
separately), consistent with governance norms.

**5C Compensation.** Board's Report remuneration table shows only NED
sitting fees (Rs 1.10-5.39 lakh each) plus ED Anavkar's Rs 55.62 lakh —
CFO/CS pay legally excluded from this table (Section 136 proviso). Note 49
RPT table separately shows: CEO Ashwani Singh's remuneration **fell**
slightly (Rs 129.13 lakh FY25 → Rs 126.63 lakh FY26) despite 25.8% revenue
growth — mildly positive comp-discipline signal, not excess pay. Promoter
family payroll: Hemant Anavkar Rs 55.62 lakh + Manisha Anavkar Rs 54.22
lakh + Aamer Aasif Khan Rs 4.50 lakh = Rs 114.34 lakh, 3.0% of consol. PAT
— present but not excessive. Auditor fee mix flag carried from Phase 1E.

**5D Shareholding.** Promoter and promoter group **68.94%** at both
31-Mar-2026 and 30-Jun-2026 (unchanged; NSE XBRL per B00) — no promoter
selling against the growth narrative; no pledge disclosure found in this
AR (pledge status NOT FOUND in the AR itself; relies on the shareholding
XML). FII holding tiny (Cat I 0.07%, Cat II 0.01%) — per house rule, low
institutional ownership is **not** treated as a risk here, only as a
UA-multiplier input for a later stage.

**5E Red-flag checklist.** Whistleblower complaints: Nil. SEBI/MCA actions
last 3 years: none disclosed. RPT committee: folded into Audit Committee
(standard). Auditor fee ratio: flagged (1E). CSR compliance: full, prior
shortfall (Rs 0.68 lakh) cleared. Section 143 fraud: none reported.
Material subsidiary/auditor: Board's Report states "no material
subsidiaries" under the Company's own materiality policy, yet the UAE
entity nested group (Fabtech Technologies LLC + its two step-downs)
contributes 33% of consol. PAT and is audited by another auditor — a
policy-definition-vs-economic-substance tension worth naming, not a
compliance breach (the materiality policy's percentage threshold is a
Board-set policy choice, not misapplied here).

**Phase 5 summary + verdict.** Attendance, CSR, and whistleblower record
are clean. But cross-board membership with the top RPT counterparty
spanning half the board (including an Independent Director), full
independent-director turnover clustered right after the listing year, and
the material-subsidiary/auditor-reliance framing gap are real,
evidenced governance-quality concerns. **Verdict: 🟡 Watch** (would be 🔴
if the cross-board pattern were paired with evidence of value extraction
through the RPT relationship rather than disclosed arm's-length pricing;
no such evidence found in this stage). Kill-switch (informational): a
reviewer would not stop, but would carry the cross-board finding into the
promoter-verdict stage (B08) as a named input.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER (read last, with full knowledge
of Phases 1-5)

**6A Narrative vs reality — top claims tested:**
1. Chairperson: "quiet compounding… maintaining earnings quality" — ❌.
   Other income is 42.6% of PBT (FX-heavy); two straight years of
   "exceptional" group-disposal gains; CFO/PAT ~1%. Earnings quality is a
   live flag, not something maintained.
2. Chairperson: "strengthening our balance sheet" — ✅/❌ mixed. Gross
   balance sheet is stronger (equity +142%, cash pile +496%), but entirely
   IPO-financed; CFO contributed almost nothing to the improvement.
3. Chairperson: "distributing our first dividend as a listed company" —
   ✅. Rs 0.60/share, Rs 266.70 lakh, small and affordable.
4. CEO: "we enter FY27 with the strongest balance sheet in our history,
   ready to capture large-scale industrial projects globally" — ❌ on
   execution-to-date. Rs 17,921.95 lakh (78%) of IPO proceeds remain
   undeployed at year-end, and the auditor's own CARO(x)(a) flags a
   deployment delay against the offer document's own schedule.
5. CEO: "FY26 results are driven by core operations" (contrasted with
   FY25's exceptional stake-sale gain) — ❌/mixed. FY26 PBT still carries
   a Rs 177.49 lakh exceptional gain and a Rs 1,188.73 lakh FX gain —
   together 28.3% of FY26 PBT from non-core or volatile sources, so "core
   operations" understates the continuing non-operating contribution.
6. Chairperson: "Growth without governance is dangerous… our commitment to
   institutional discipline only intensifies" — ❌. The same AR carries a
   balance-sheet-face error, a duplicate note number, two internally
   conflicting IPO-utilisation tables, two conflicting ROE/RONW tables, an
   auditor-fee mismatch between the CG report and Note 39, and full
   independent-director board turnover within a quarter of signing. The
   discipline claim is not evidenced by the filing's own execution quality.
7. MD&A: "Working capital intensive… rising trade receivables and
   collection risk" — ✅. Candid and matches the facts.

**6B Strategic priorities.** "Inorganic growth through acquisitions" is
named repeatedly (Achievements, Board's Report, MD&A outlook, CEO letter)
but the Rs 3,000 lakh earmarked bucket sits at **0% deployed** at FY26
year-end; the Jun-2026 Saudi acquisition activity (Specialized Contracting
Activities LLC) only began after FY26 closed. "KP Group green-
infrastructure collaboration" (Achievements p.11-12 txt) is announced with
no execution evidence (no revenue, capex, or contract terms disclosed
anywhere in this AR) — a pure announcement at this stage.

**6C Metrics showcased vs absent.** Showcased: revenue, PAT, order book
(>Rs 900 Cr, management claim), IPO metrics, nine-country geography split,
standard ratio table. Conspicuously absent from the CEO/Chairperson/
Achievements sections: **segment profitability** (explicitly declared "not
ascertainable" in the notes), and **the CFO/cash-conversion figure** —
not mentioned anywhere in the front-matter narrative despite being the
single most negative operating fact of the year, one the MD&A itself
(more honestly) acknowledges in prose.

**6D Tone/priority drift.** Within FY26 alone, the AR runs a two-register
tone: triumphant in the Achievements/CEO/Chairperson sections, candid in
the MD&A risk section. This split-register pattern (rather than a
consistent voice) is itself worth naming as a house-style/credibility
signal for future ARs to be checked against.

**6E Quiet Abandonment Check (mandatory).**
1. **Chairperson's "institutional discipline only intensifies" (opening)
   vs the filing's own six internal numeric inconsistencies (operational
   sections: notes, cash flow statement, CG report, Note 50)** —
   classification: **IMPLICIT RETRACTION** (opening asserts intensifying
   discipline; the operational sections show reduced disclosure discipline
   with no acknowledgement anywhere in the AR). Materiality: **MODERATE-
   HIGH** — it changes confidence in every other number in the filing,
   even though it does not on its own overturn the operating thesis.
2. **CEO's "ready to capture large-scale industrial projects globally"
   (opening) vs the IPO-deployment notes and the auditor's own CARO(x)(a)
   clause (operational sections)** — classification: **HEDGED RETREAT**
   (readiness is asserted in general terms; the specific capital that
   would fund that readiness — the inorganic-growth bucket, at 0% deployed
   — is quietly not mentioned in the letter at all). Materiality:
   **MODERATE** — bears directly on LBF4 and the IPO-deployment
   load-bearing fact.
3. **Chairperson's "we maintained earnings quality" (opening) vs the
   exceptional-items note and the other-income/FX composition
   (operational sections)** — classification: **IMPLICIT RETRACTION**.
   Materiality: **HIGH** — earnings quality is a core valuation input for
   the strategy's exit-PE work at Stage 11.
No further candidates found beyond these three; the remaining testable
claims (dividend, GCC/Africa geography thesis, listing itself) are either
directly evidenced or too general to test against operational sections.

**Phase 6 summary + verdict.** 🔴 Red Flag. Three separate quiet-
abandonment instances, two of them (earnings quality; discipline claim)
bearing materially on how the rest of this stage's findings should be
weighted. The front-matter narrative is more optimistic than the filing's
own numbers support; the MD&A, read on its own, is considerably more
trustworthy than the CEO/Chairperson letters.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| Value + Quality | FAIL | (1) CFO/PAT ~1% FY26, negative FY25; (2) ROCE/ROI declining; (3) six internal disclosure inconsistencies undercut quality read |
| **GARP** (fullest reasoning) | **WATCHLIST** | (1) Growth is real and broad-based — 25.8% consol. revenue growth across 9 geographies, order book >Rs 900 Cr per management (LBF1, unverified in this stage); (2) earnings quality is the load-bearing weakness — 42.6% of PBT from other income (58% FX-driven), two years of recurring "exceptional" disposal gains, and CFO/PAT near-zero/negative both independently confirmed by the auditor's KAM and by the cash-flow statement itself, not just inferred; (3) a second, independent reason for caution sits in governance/disclosure quality — the cross-board RPT-counterparty pattern, full ID board turnover, and the six internal numeric mismatches all cluster in the exact first-full-year-post-listing scale-up window the transition thesis is testing. On the Transition Decision Matrix: PROOF GATE reads NOT FIRED on this year's cash evidence alone (growth is real, but the cash-conversion proof the strategy needs has not yet shown up); RECOGNITION GAP and UGLINESS classification are Stage 8/11/13 calls, not this stage's |
| Turnaround | FAIL | Growing, not distressed — not a turnaround setup |
| Capex-Led Growth | FAIL | Capex (Rs 470.81 lakh) below depreciation (Rs 530.15 lakh) FY26; asset-light model by design, not a capex-led thesis |
| Cash Flow Compounder | FAIL | Definitional fail — CFO/PAT ~1% FY26, negative FY25 |
| Contrarian | WATCHLIST | Recently listed, thinly covered; order-book claim not yet reconciled against filed figures (LBF1 deferred to Stage 5/8) |
| Insider Confidence | WATCHLIST | Promoter holding flat at 68.94% (no selling — mildly positive), no fresh insider buying disclosed either — neutral |
| Guidance Divergence | WATCHLIST | This AR itself carries no quantified FY27 guidance (NOT FOUND); qualitative guidance lives in the concalls, deferred to Stage 5 verification against delivery |

---

## PHASE 8: FINAL VERDICT DASHBOARD

**Company snapshot.** Fabtech Technologies Ltd — turnkey pharma/biotech/
cleanroom EPC (design, engineering, procurement, installation,
validation), operating in 62+ countries. FY26 consolidated revenue Rs
41,077.18 lakh (+25.75% YoY), PAT Rs 3,835.80 lakh (-17.4% YoY, driven by a
smaller FY26 exceptional gain vs FY25). Listed Oct-2025. Promoter holding
68.94% (unchanged). Total assets (corrected) Rs 65,370.29 lakh.

**Phase-wise verdict summary.**
| Phase | Verdict |
|---|---|
| 1 Auditor's Report & CARO | 🟡 Watch |
| 2 Notes to Financial Statements | 🔴 Red Flag |
| 3 Financial Statements | 🔴 Red Flag |
| 4 Risk Factors & MD&A | 🟡 Watch |
| 5 Corporate Governance & Board | 🟡 Watch |
| 6 Chairman's Letter & Front Matter | 🔴 Red Flag |
| 7 Best-fit strategy | GARP (Watchlist) |

**Overall quality score: 5.0/10** — governance 5/10 (25%), accounting
quality 5/10 (25%), balance sheet 6/10 (25%), earnings quality 4/10 (25%).

**Top 3 strengths.**
1. Genuine, broad-based revenue growth across nine geographies with no
   single-country dominance (largest single geography, "Rest of the
   world," is itself a diversified bucket) — reduces single-market
   concentration risk relative to the customer-level rotation seen in
   Note 44.
2. Post-IPO balance sheet is low-leverage (D/E ~0.10x) with a large liquid
   cushion (Rs ~20,857 lakh cash + FDs) providing multi-year runway
   independent of operating cash generation.
3. MD&A (though not the CEO/Chairperson letters) is candid about the
   year's central negative fact — receivables ageing and its cash-flow
   impact — rather than concealing it, and the CEO letter transparently
   isolates the FY25 exceptional item in the YoY PAT comparison.

**Top 3 red flags.**
1. Cash conversion failure two years running (CFO/PAT ~1.2% FY26, -77.8%
   FY25), partly masked in FY26 by a deconsolidation-driven inventory
   swing the company itself discloses but does not adjust for in its
   headline ratios.
2. A cluster of at least six internal numeric inconsistencies within the
   same annual report (balance-sheet face vs Note 13; duplicate note "60";
   two IPO-utilisation tables Rs 600 lakh apart; two ROE/RONW tables; CG-
   report vs Note-39 auditor fee; a Rs 2 lakh goodwill roll-forward gap) —
   a disclosure-quality pattern, not a single typo, appearing in exactly
   the first full-year post-listing filing where scale-up execution is
   under test.
3. Governance-independence concentration: three of six FY26 board seats
   (half the board, including one Independent Director) sit simultaneously
   on the board of the promoter-group's separately-listed related-party
   trading counterparty (Fabtech Technologies Cleanrooms Limited), which
   is also a Rs 1,000 lakh corporate-guarantee counterparty.

**Monitorables for next quarter.**
| Metric | Threshold | Where | Why |
|---|---|---|---|
| CFO/PAT ratio | Return above ~0.5x would be the first real evidence of easing | Next quarterly/half-yearly cash flow disclosure | Single most important unresolved fact from FY26 |
| Trade receivables >6-month / >365-day share | Any further rise past 43.6% / Rs 5,887.55 lakh | FY27 AR Note 13-equivalent, or Q4 FY27 results | Auditor's own KAM; tests whether deterioration is structural |
| IPO inorganic-growth bucket utilisation | First rupee deployed against the Rs 3,000 lakh bucket | Announcements/monitoring-agency reports, deviation statements | Tests whether Jun-2026 Saudi acquisition draws on this bucket and whether "ready to capture" converts to deployment |
| FTS Cleanrooms Systems LLC profit trend | Any further decline against rising revenue | FY27 AR business-combination note equivalent | This single UAE entity is ~33% of consol. PAT; its FY26 profit fell while revenue rose |
| Board composition post new IDs | Whether Ms. Haria or Ms. Khanna also sit on Fabtech Technologies Cleanrooms Ltd's board | FY27 AR / postal ballot outcome | Tests whether the cross-board governance concern eases or persists |

**One-line verdict.** Real, broad-based growth funded by a clean IPO
balance sheet, undercut by two years of failed cash conversion and a
first-year post-listing disclosure-quality cluster the front-matter
narrative does not acknowledge; best-fit strategy is GARP, on a Watchlist
pending the proof gate the cash-flow statement has not yet fired.

---
### Notes on this stage's process
- All figures above are stated in the source unit (INR lakh, AR/results
  face; INR Cr only where the RHP/screener/CRISIL source itself uses Cr,
  none of which was needed in this stage). Conversion to Rs Cr for
  synthesis happens at Stage 10 per B00 `reporting_units`.
- Every load-bearing digit above was either (a) already anchored and
  verified in B02, and reconfirmed here against the primary document, or
  (b) newly read from the auditor's report, financial statements, MD&A,
  Board's Report, CG Report, or AGM Notice directly in this stage, with a
  page citation in every case.
- Two numeric discrepancies (the Rs 600 lakh IPO-utilisation gap; the two
  cash-flow-statement working-capital breakdowns) could not be fully
  resolved from OCR text alone and are carried forward as input_gaps
  needing page-image confirmation, per the AR-text protocol.
