# STAGE 2: NOTES TO FINANCIAL STATEMENTS, TRIPLE PASS, CONSOLIDATED
Company: Fabtech Technologies Ltd (FABTECH). Run: fabtech-2026-09-26.
Basis: CONSOLIDATED (primary), standalone noted where materially different.
Units: as stated on the face of each source. AR is INR lakh (OCR text, cite
as "AR p.N (txt)"); FY26 audited results filing is INR lakh (text layer,
cite as "Results p.N"). All figures below carry their source unit; convert
to Rs Cr only downstream at stage 10 per B00 reporting_units.

Sources: runs/fabtech-2026-09-26/inputs/annual-report/Annual_Report_2026.txt
(standalone notes 1-56, txt p.101-138; consolidated notes 1-62, txt
p.155-200); runs/fabtech-2026-09-26/inputs/results/20260427-Results_FY26_audited.txt.

---

## PASS 1 (full extraction) and PASS 2 (what was missed): SUMMARY

Full Pass 1 and Pass 2 reports are held at
runs/fabtech-2026-09-26/outputs/reports/02-notes-pass1.md and
02-notes-pass2.md and are incorporated below in full. Pass 1 read every
note number, standalone and consolidated, note by note, with sub-notes and
footnotes. Pass 2 re-read end to end and resolved three Pass 1 open items
with new primary-source text, plus one genuinely new finding (the FABL
buyer is unnamed).

Pass 1 top-line: the FY26 AR consolidated balance sheet FACE misstates
trade receivables and total assets (Rs 3,718.39 lakh overstatement); every
other source in the same filing set (Note 13, MD&A, financial-instruments
note, exchange-filed audited results) agrees on the correct figures (Rs
20,433.51 lakh trade receivables, Rs 65,370.29 lakh total assets). Trade
receivable ageing is deteriorating and the auditor named it a Key Audit
Matter. Other income is 58% net FX gain against a materially under-hedged
FX book. Customer concentration shows severe year-on-year rotation, not
stickiness. Two consecutive years carry "exceptional" gains from disposing
of stakes in group/associate entities. MSME payment delays are worsening.
IPO inorganic-growth proceeds are 0% utilised at FY26 year-end.

Pass 2 resolved: (1) the CARO Clause (vii)(a) qualification is a single Rs
22,371 TDS delay paid within three weeks of year-end, not an unresolved
arrears problem — downgraded from the Pass 1 🔴 to 🟡; (2) the Rs 2,350.83
lakh "Loan from related party (Loan from Others)" cannot be the 100%-owned
UAE subsidiary (that balance eliminates on consolidation), which narrows
but does not close the disclosure gap — still 🔴; (3) the Saudi entity
naming question is fully resolved: "Fabtech Lifecare Company, KSA" (100%,
incorporated Aug-2025, in the FY26 AR) and "Specialized Contracting
Activities LLC" (51%, announced Jun-2026, a separate non-pharma entity)
are two different, correctly-named entities, not a mismatch — this closes
the earlier LBF3 naming flag; (4) new finding: the buyer of the 51% FABL
stake is not named anywhere in the notes (NOT FOUND IN DOCUMENT).

---

## PASS 3: PATTERN PASS

Read against the six pattern prompts (contradictions, note-vs-statement
mismatches, deliberately thin disclosure, restatements/reclassification,
post-balance-sheet events, going concern language).

**Contradictions / mismatches found (all already surfaced in Pass 1/2,
grouped here as a pattern):**
- The consolidated balance sheet FACE disagrees with Note 13, the MD&A,
  the financial-instruments note, and the exchange-filed audited results
  on trade receivables and total assets (Section 0 of Pass 1). This is
  the single clearest note-vs-statement mismatch in the filing.
- Payables-turnover divergence: standalone payables turnover ROSE 11%
  (1.97x to 2.19x) while consolidated payables turnover FELL 18% (2.59x
  to 2.12x) in the same year, with the consolidated fall left unexplained
  because it sits just under the 25%-variance disclosure trigger (Note
  48/50). The direction of travel differs by entity within the same
  group in the same year — worth a question, not evidenced as
  manipulation.
- A duplicate note number ("60" appears twice in the consolidated notes,
  once for the IPO note and once for events after the reporting period,
  AR p.199-200 txt) and the balance-sheet-face error are both drafting
  defects in the same filing. Pattern, not coincidence: this is the
  company's first full-year AR after listing, and the close process
  shows strain at exactly the scale-up point the strategy is testing for.

**Restatements/reclassifications:** the FABL International Technologies
LLP subsidiary-to-associate reclassification (1-Apr-2025, day 1 of FY26)
is a genuine scope change, not a restatement of prior-year figures — FY25
comparatives are not restated, only FY26 disclosure basis differs from
FY25. Keyword sweep for "restated," "reclassified," "revised" (Pass 2)
found no prior-year figure restatements.

**Events after balance sheet date:** only the Rs 0.60/share final dividend
(Rs 266.70 lakh) is disclosed in the notes. The Jun-2026 acquisition
filings (Specialized Contracting Activities LLC, announced 02-Jun-2026,
before the AR's 31-Jul-2026 filing date but after the 27-Apr-2026 audited
results and the AR's 31-Mar-2026 balance sheet date) are NOT mentioned in
the "events after reporting period" note. Whether this omission is
material turns on whether the transaction was sufficiently advanced and
known before the AR was finalised — flagged for stage 3/8, not resolved
here.

**Going concern language:** NONE found anywhere in the standalone or
consolidated notes or audit opinions. Both audit opinions are unmodified.

PASS 3 yields no findings beyond what Pass 1/2 already surfaced, read here
as a connected pattern rather than isolated items. Proceeding to
consolidation as required regardless.

---

═══════════════════════════════════════════════════════════
CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED
═══════════════════════════════════════════════════════════

## A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Trade receivable ageing deteriorating: >6mo gross receivables 43.6% (FY26) vs 35.3% (FY25); ECL rates in 1-3yr buckets roughly tripled (3.4-3.8% to 10.1%); auditor named Rs 5,887.55 lakh of >365-day receivables a Key Audit Matter | Note 13, consol.; Auditor's Report p.139-140 (txt) | 🔴 | External, independent confirmation that LBF2 cash-conversion strain is structural, not purely growth-induced |
| 2 | Consolidated AR balance-sheet FACE overstates trade receivables and total assets by Rs 3,718.39 lakh (24,151.90 vs correct 20,433.51 lakh; 69,088.68 vs correct 65,370.29 lakh); confirmed a genuine drafting error via triangulation across Note 13, MD&A, fin-instruments note, and the exchange-filed audited results | Note 13 / BS face, AR p.150 & 173 (txt) | 🔴 | Sets the correct anchor for all downstream cash/WC work; also a disclosure-quality signal on its own |
| 3 | 58% of FY26 other income (Rs 1,188.73 lakh of Rs 2,055.77 lakh) is a net FX gain, against a materially under-hedged FX book (one USD 20 lakh forward vs ~Rs 22,130 lakh monetary FX assets); FX PBT sensitivity nearly tripled YoY | Note 32 consol.; Note 48 sensitivity | 🔴 | Largest single earnings-quality item found; inflates PBT with a volatile, reversible item, directly informs LBF4 |
| 4 | Customer concentration shows rotation, not durability: 3 of FY25's top-4 named customers each fell from >10% to single digits of revenue in FY26; a new customer appeared from near-zero to 12.55%; no segment profitability disclosed to test margin impact | Note 44, consol. | 🔴 | Central to the order-book archetype's stickiness test and the R2/R3 pricing-power question |
| 5 | Rs 2,350.83 lakh unsecured current borrowing labelled "Loan from related party (Loan from Others)" cannot be traced to a named counterparty; Pass 2 ruled out the closest numeric candidate (the 100%-owned UAE subsidiary, whose balance would eliminate on consolidation) | Note 26, consol.; Note 47/49 cross-check | 🔴 | Genuine disclosure gap surviving two re-reads; direct question for management |
| 6 | Under-hedged FX exposure: only one USD 20 lakh forward contract against ~Rs 22,130 lakh of monetary FX assets; a 10% currency move swings consolidated PBT by ~Rs 2,350.64 lakh (FY26) vs Rs 811.49 lakh (FY25), nearly tripling YoY | Note 48, consol. sensitivity | 🔴 | FX risk to earnings has grown faster than the hedge programme; ties directly to Finding 3 |
| 7 | Two consecutive years of "exceptional" gains from disposing of stakes in group/associate entities: FY25 Rs 1,784.86 lakh (29.5% of consol. PBT, TSA/Thermax); FY26 Rs 177.49 lakh (3.7% of PBT, FABL) | Note 40, consol. | 🟡 | A recurring item under an "exceptional" label is an earnings-quality flag (LBF4), though the FY26 scale is now small |
| 8 | MSME payment delays worsening: interest accrued and unpaid to MSME suppliers up 149% YoY (Rs 21.52 to Rs 53.59 lakh); same interest expected to remain unpaid into next year; unpaid MSME principal also up YoY (consol. Rs 1,870.84 lakh) | Note 26/27 | 🟡 | Working-capital stress signal alongside the receivables deterioration |
| 9 | Zero (0%) utilisation of the Rs 3,000 lakh IPO proceeds earmarked for inorganic growth by FY26 year-end; only 22% of total IPO proceeds deployed overall | Note 53/60 | 🟡 | Directly tests LBF4 (IPO deployment vs RHP objects); the Jun-2026 acquisition activity began only after FY26 closed |
| 10 | CARO Clause (vii)(a) statutory-dues qualification across the Holding Company, a subsidiary (FT Institutions) and an associate (Mark Maker); the Holding Company's own instance resolved by Pass 2 to a single Rs 22,371 TDS delay paid within 3 weeks of year-end | Auditor's Report, CARO para 3(vii)(a), AR p.92-93 (txt) | 🟡 (revised down from 🔴 in Pass 1) | Compliance-process observation, not a material arrears problem for the parent; the two co-qualified entities' own amounts remain undisclosed in this AR |
| 11 | The buyer of the 51% FABL International Technologies LLP stake is not named in any of the three notes that discuss the transaction (exceptional items, subsidiary-movement, related-party) | Note 40/52/49, consol. | 🟡 | If the buyer is itself connected, the "exceptional gain" quality concern (Finding 7) is materially worse; unresolved after two passes |
| 12 | Cross-collateralised group security structure: the listed entity's working-capital facility is secured partly by non-consolidated promoter-group entities' assets/guarantees (Cleanrooms Ltd, Fabsafe, FTIPL, Fabtech Turnkey Projects LLP), and the listed entity gives corporate guarantees back to two of them (Rs 1,000 lakh and Rs 600 lakh, unchanged YoY) | Note 22/25 standalone; Note 23/26 consol. | 🟡 | Disclosed, but financially entangles the listed entity's balance sheet with non-consolidated related parties |
| 13 | Note-numbering and drafting-quality pattern: duplicate note "60" in the consolidated notes, plus the balance-sheet-face error (Finding 2), both in the same first full-year post-listing AR | AR p.199-200 (txt) | 🟡 | Pattern (not isolated) evidence of financial-close strain at listing-year scale-up |
| 14 | Deconsolidation of FABL (subsidiary to 49% associate, day 1 of FY26) distorts two consolidated ratios that read as operating improvement but are not: inventory turnover +46.5% and the consolidated payables-turnover fall of 18% both trace mechanically to the changed consolidation perimeter | Note 50, consol.; Note 52 | 🟡 | Screener-style ratio reads on these two lines should not be taken at face value without adjusting for the deconsolidation |
| 15 | Payables grew far slower (+6.7%) than revenue (+26%) or receivables (+38.5%) in FY26 — a working-capital mismatch where the company is both collecting slower and not stretching suppliers to compensate | Note 27, consol. | 🟡 | Compounds Finding 1; the WC drag is not offset anywhere else in the cycle |

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 6/10 | Shipment/milestone basis on turnkey contracts is disclosed and consistent, but creates lumpiness; no segment profitability to test it against delivery |
| Expense capitalisation honesty | 8/10 | Standard Schedule II lives (one immaterial 9-vs-10-year leasehold variance, disclosed); no aggressive capitalisation found |
| Provisioning adequacy | 5/10 | ECL rates roughly tripled in ageing 1-3yr buckets, and the auditor independently flagged overdue receivables as a Key Audit Matter — provisioning is rising but the underlying deterioration is faster |
| RPT fairness | 6/10 | Extensive, well-itemised RPT universe and a forward RPT ceiling disclosed for FY27, but one Rs 2,350.83 lakh related-party-labelled borrowing is untraceable and the FABL buyer is unnamed |
| Disclosure transparency | 4/10 | Balance-sheet-face error, duplicate note number, no segment reporting, untraceable RPT borrowing, unnamed FABL buyer — several independent gaps in the same filing |
| Consistency with prior years | 6/10 | Two ratios (inventory turnover, payables turnover) are distorted by a mid-year deconsolidation without adjustment; two consecutive years of "exceptional" stake-sale gains |
| **OVERALL** | **5/10** | A first full-year post-listing AR with real, evidenced deterioration in receivables quality (confirmed by the auditor), a materially FX-inflated PBT, and a cluster of drafting/disclosure defects; no evidence of outright manipulation, but transparency and provisioning both lag the pace of the underlying business change |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Receivables ageing and ECL deterioration | HIGH | >6mo % of gross receivables; 1-3yr ECL rate; the auditor's KAM figure in the next AR | Already live; next confirmation at FY27 AR/Q-results ageing tables |
| FX-gain-inflated PBT reversing | HIGH | Other-income composition each quarter; hedge ratio vs monetary FX exposure | Any INR strengthening quarter, or FY27 AR sensitivity note |
| Untraceable related-party borrowing (Rs 2,350.83 lakh) | MEDIUM | Whether stage 3/8 or a management Q&A names the counterparty | Next AR or a direct management response |
| Customer concentration rotation | MEDIUM | Whether FY27 top-4 customers repeat from FY26 or rotate again | FY27 AR customer-concentration note |
| MSME payment delay trend | MEDIUM | MSME interest-accrued-and-unpaid line YoY | FY27 AR Note 26/27 |
| Cross-collateralised group structure | MEDIUM | Any covenant or guarantee change at Cleanrooms Ltd/Fabsafe/FTIPL | Any of those entities' own filings, or a Fabtech guarantee-note update |
| Disclosure/drafting quality cluster | LOW-MEDIUM | Whether FY27 AR repeats a face-vs-note mismatch or numbering error | FY27 AR |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. Which related party or lender sits behind the Rs 2,350.83 lakh current borrowing labelled "Loan from related party (Loan from Others)" in consolidated Note 26, and why does it not appear in the Note 49 related-party balances table?
2. Who bought the 51% stake in FABL International Technologies LLP on 1-Apr-2025, and was the buyer connected to the promoter group at the time of sale?
3. What drove the FTS Cleanrooms Systems LLC (UAE) profit fall from Rs 1,161.83 lakh (FY25) to Rs 700.15 lakh (FY26) on higher revenue (Rs 13,888.46 to Rs 16,048.75 lakh), and how does that reconcile with the FY27 related-party sales ceiling of Rs 6,000 lakh sought at the AGM?
4. Why did >6-month trade receivables rise from 35.3% to 43.6% of the gross book, and what collection actions are underway on the Rs 5,887.55 lakh the auditor flagged as overdue beyond 365 days?
5. What is the status of the Rs 3,000 lakh IPO proceeds earmarked for inorganic growth, given 0% utilisation at FY26 year-end and the Jun-2026 acquisition announcements that followed shortly after?

## E. NOTES-BASED RED FLAGS

- Earnings management signal (moderate): other income is 58% net FX gain, a volatile non-operating item inflating PBT, against a thin hedge programme.
- Aggressive accounting: not evidenced. Capitalisation, revenue recognition basis, and DTA composition all read as standard for the archetype.
- Undisclosed risk indicators: the untraceable Rs 2,350.83 lakh related-party-labelled borrowing; the unnamed FABL stake buyer; no segment profitability despite a multi-geography, multi-entity group.
- Balance-sheet-face error and duplicate note numbering are disclosure-quality defects, not earnings-management devices, but they lower confidence in the filing's internal controls at the exact point the strategy is testing scale-up execution.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: receivables
ageing is deteriorating, confirmed by the auditor as a Key Audit Matter,
and PBT leans on a large, under-hedged FX gain. Key strength: no
restatements, no going-concern language, and a fully compliant CSR and
dividend record. Overall accounting quality: 5/10.

```yaml
stage: B02-notes
company: "FABTECH"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
input_gaps:
  - "CARO annexure full statutory-dues detail for FT Institutions Pvt Ltd and Mark Maker Engineering Pvt Ltd (co-qualified entities under Clause vii(a)) is not reproduced in this AR; own arrears amounts NOT FOUND IN DOCUMENT."
  - "Jun-2026 acquisition filings (Specialized Contracting Activities LLC, 02-Jun-2026 and 25-Jun-2026) postdate the FY26 balance sheet date and are not addressable from these notes; carry to stage 3/8 for announcements-based verification."
  - "Buyer of the 51% FABL International Technologies LLP stake not named anywhere in the notes; NOT FOUND IN DOCUMENT, pull from RHP/exchange filings/MCA if needed."
  - "Counterparty behind the Rs 2,350.83 lakh 'Loan from related party (Loan from Others)' current borrowing (consolidated Note 26) untraceable in Note 49; NOT FOUND IN DOCUMENT."
flags:
  - {type: FLAG-CASH, reason: "Trade receivable ageing worsening (>6mo gross receivables 43.6% FY26 vs 35.3% FY25); ECL rates in 1-3yr buckets roughly tripled; auditor named Rs 5,887.55 lakh of >365-day receivables a Key Audit Matter. Evidences LBF2 cash-conversion strain as GROWTH-INDUCED-AND-STRUCTURAL, not purely growth-induced."}
  - {type: FLAG-EARNINGS-QUALITY, reason: "58% of FY26 other income (Rs 1,188.73 lakh of Rs 2,055.77 lakh) is a net FX gain against a materially under-hedged FX book (one USD 20 lakh forward vs ~Rs 22,130 lakh monetary FX assets); FX PBT sensitivity nearly tripled YoY. Ties to LBF4."}
  - {type: FLAG-DISCLOSURE-QUALITY, reason: "Consolidated AR balance-sheet face overstates trade receivables and total assets by Rs 3,718.39 lakh vs Note 13/MD&A/audited results; duplicate note number 60 in consolidated notes; both in the first full-year post-listing AR."}
  - {type: FLAG-RPT-UNTRACEABLE, reason: "Rs 2,350.83 lakh current borrowing labelled related-party in Note 26 cannot be traced to a named counterparty in Note 49 after two re-reads; FABL 51%-stake buyer also unnamed."}
accounting_quality: 5        # /10
pass_2_empty: false
pass_3_empty: true
top_findings:                # max 15
  - {rank: 1, finding: "Trade receivable ageing deteriorating; >6mo gross receivables 43.6% FY26 vs 35.3% FY25; ECL 1-3yr rates roughly tripled; auditor Key Audit Matter on Rs 5,887.55 lakh overdue >365 days", note_ref: "Note 13 consol.; Auditor's Report p.139-140 (txt)", rating: "red", why: "External, independent confirmation LBF2 cash strain is structural"}
  - {rank: 2, finding: "Consolidated AR balance sheet face overstates trade receivables and total assets by Rs 3,718.39 lakh; correct figures are Note 13's Rs 20,433.51 lakh / Rs 65,370.29 lakh, confirmed by MD&A, fin-instruments note and exchange-filed audited results", note_ref: "Note 13 / BS face, AR p.150 & 173 (txt)", rating: "red", why: "Sets the correct anchor for all downstream WC/cash work; a disclosure-quality signal itself"}
  - {rank: 3, finding: "58% of FY26 other income (Rs 1,188.73 lakh of Rs 2,055.77 lakh) is a net FX gain, against a materially under-hedged FX book; FX PBT sensitivity nearly tripled YoY", note_ref: "Note 32 consol.; Note 48 sensitivity", rating: "red", why: "Largest single earnings-quality item found; inflates PBT with a volatile item"}
  - {rank: 4, finding: "Customer concentration rotates rather than repeats: 3 of FY25's top-4 named customers fell from >10% to single digits in FY26; a new customer appeared from near-zero to 12.55%", note_ref: "Note 44, consol.", rating: "red", why: "Tests the order-book archetype's stickiness and R2/R3 pricing-power question"}
  - {rank: 5, finding: "Rs 2,350.83 lakh unsecured current borrowing labelled 'Loan from related party (Loan from Others)' cannot be traced to a named counterparty; the closest numeric candidate (UAE subsidiary) is ruled out because it would eliminate on consolidation", note_ref: "Note 26 consol.; Note 47/49 cross-check", rating: "red", why: "Genuine disclosure gap surviving two re-reads"}
  - {rank: 6, finding: "Under-hedged FX exposure: one USD 20 lakh forward vs ~Rs 22,130 lakh monetary FX assets; 10% currency move swings PBT ~Rs 2,350.64 lakh FY26 vs Rs 811.49 lakh FY25", note_ref: "Note 48, consol. sensitivity", rating: "red", why: "FX risk to earnings has grown faster than the hedge programme"}
  - {rank: 7, finding: "Two consecutive years of 'exceptional' gains from group/associate stake disposals: FY25 Rs 1,784.86 lakh (29.5% of PBT); FY26 Rs 177.49 lakh (3.7% of PBT)", note_ref: "Note 40, consol.", rating: "yellow", why: "Recurring item under an exceptional label is an earnings-quality flag (LBF4)"}
  - {rank: 8, finding: "MSME payment delays worsening: interest accrued and unpaid up 149% YoY (Rs 21.52 to Rs 53.59 lakh); unpaid principal also up YoY", note_ref: "Note 26/27", rating: "yellow", why: "Working-capital stress signal alongside the receivables deterioration"}
  - {rank: 9, finding: "Zero utilisation of the Rs 3,000 lakh IPO proceeds earmarked for inorganic growth by FY26 year-end; only 22% of total proceeds deployed", note_ref: "Note 53/60", rating: "yellow", why: "Directly tests LBF4 IPO deployment vs RHP objects"}
  - {rank: 10, finding: "CARO Clause (vii)(a) qualification across Holding Company, a subsidiary and an associate; parent's own instance resolved to a single Rs 22,371 TDS delay paid within 3 weeks of year-end (revised down from red in Pass 1)", note_ref: "Auditor's Report CARO 3(vii)(a), AR p.92-93 (txt)", rating: "yellow", why: "Compliance-process observation, not material arrears; co-qualified entities' own amounts undisclosed"}
  - {rank: 11, finding: "Buyer of the 51% FABL International Technologies LLP stake not named in any of the three notes discussing the transaction", note_ref: "Note 40/52/49, consol.", rating: "yellow", why: "If connected, worsens the exceptional-gain quality concern; unresolved after two passes"}
  - {rank: 12, finding: "Cross-collateralised group security: listed entity's WC facility secured partly by non-consolidated promoter-group entities, and vice versa via corporate guarantees (Rs 1,000 lakh + Rs 600 lakh, unchanged YoY)", note_ref: "Note 22/25 standalone; Note 23/26 consol.", rating: "yellow", why: "Disclosed, but entangles the listed entity's balance sheet with non-consolidated related parties"}
  - {rank: 13, finding: "Drafting-quality pattern: duplicate note '60' in consolidated notes, alongside the balance-sheet-face error, both in the first full-year post-listing AR", note_ref: "AR p.199-200 (txt)", rating: "yellow", why: "Pattern evidence of financial-close strain at listing-year scale-up"}
  - {rank: 14, finding: "Deconsolidation of FABL (day 1 of FY26) mechanically distorts inventory turnover (+46.5%) and consolidated payables turnover (-18%); neither is an operating improvement", note_ref: "Note 50, consol.; Note 52", rating: "yellow", why: "Screener-style ratio reads on these lines should not be taken at face value"}
  - {rank: 15, finding: "Payables grew +6.7% vs revenue +26% and receivables +38.5% in FY26, a working-capital mismatch not offset elsewhere in the cycle", note_ref: "Note 27, consol.", rating: "yellow", why: "Compounds the receivables-ageing finding; no relief from the payables side"}
red_flags:
  - "58% of other income is net FX gain against a thin hedge programme (earnings-quality)"
  - "Rs 2,350.83 lakh related-party-labelled borrowing untraceable to a named counterparty after two re-reads"
  - "Consolidated AR balance-sheet face materially wrong on trade receivables and total assets, undetected until this pass"
  - "Auditor's own Key Audit Matter on >365-day overdue receivables independently confirms the ageing deterioration"
questions_for_mgmt:
  - "Which related party or lender sits behind the Rs 2,350.83 lakh 'Loan from related party (Loan from Others)' current borrowing, and why does it not appear in the Note 49 related-party balances table?"
  - "Who bought the 51% FABL International Technologies LLP stake on 1-Apr-2025, and was the buyer connected to the promoter group?"
  - "What drove the FTS Cleanrooms Systems LLC profit fall (Rs 1,161.83 to Rs 700.15 lakh) on higher revenue, and how does it reconcile with the FY27 related-party sales ceiling of Rs 6,000 lakh sought at the AGM?"
  - "Why did >6-month trade receivables rise from 35.3% to 43.6% of the gross book, and what is the collection status of the Rs 5,887.55 lakh flagged by the auditor as overdue beyond 365 days?"
  - "What is the status of the Rs 3,000 lakh IPO proceeds earmarked for inorganic growth, given 0% utilisation at FY26 year-end and the Jun-2026 acquisition announcements that followed?"
receivables_trend: "deteriorating: consolidated gross trade receivables >6 months rose from 35.3% (FY25) to 43.6% (FY26) of the total; ECL loss rates in the 1-3yr ageing buckets rose from 3.4-3.8% (FY25) to 10.1% (FY26); auditor's Key Audit Matter names Rs 5,887.55 lakh overdue >365 days (Note 13, consol.; Auditor's Report p.139-140 txt). Feeds FLAG-CASH."
restatements_found: []
going_concern_language: "NONE. Both standalone and consolidated audit opinions are unmodified/unqualified on going concern; no material uncertainty disclosed in the notes."
analyst_note: "The single most load-bearing correction from this stage: anchor all downstream cash/WC/balance-sheet work to consolidated trade receivables Rs 20,433.51 lakh and total assets Rs 65,370.29 lakh (Note 13, MD&A, financial-instruments note, and the exchange-filed audited results all agree), not the AR balance-sheet face's Rs 24,151.90 lakh / Rs 69,088.68 lakh, which is a confirmed drafting error. Separately, the Saudi entity naming question that Pass 1 flagged as a mismatch against company memory is fully resolved by Pass 2 as two distinct, correctly-named entities (Fabtech Lifecare Company KSA, 100%, in-AR; Specialized Contracting Activities LLC, 51%, announced Jun-2026, not yet in any AR) -- stage 3/8 should track both going forward and not re-open this as an open question."
```
