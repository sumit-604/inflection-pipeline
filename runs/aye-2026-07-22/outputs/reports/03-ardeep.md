# STAGE 3 — ANNUAL REPORT DEEP DIVE, BACKWARD READ
Company: Aye Finance Limited (AYE) | Run date: 2026-07-22 | Protocol v1.2

## SOURCE AND ADAPTATION NOTE (read before the phases)

AYE listed ~February 2026 (Prospectus dated February 11, 2026). **There is no post-listing
Annual Report yet** — the backward-history document for this stage is the **IPO Prospectus**
itself (`annual-report__1770879625663.txt`, 614-page extract), whose "Restated Financial
Statements" section (Annexures I-VI, Notes 1-56) functions as the multi-year financial history
a normal AR would provide. All page anchors below are "extract p.X/614" (physical PDF-extract
page), cross-checked against the doc's internal printed page numbers where both are visible.

Structural adaptations required by this document type, carried from the B00/task brief and
confirmed by this read:
- **No CARO 2020 report exists.** The Prospectus's "Independent Auditor's Examination Report on
  Restated Financial Information" (extract p.310-312/614) is a SEBI ICDR / Guidance Note
  engagement, not a Companies Act statutory audit report — it does not carry a CARO annexure.
  Phase 1D is answered "NOT FOUND IN DOCUMENT — not applicable to this report type" rather than
  left blank.
- **No formal Key Audit Matters (KAM) section exists** for the same reason (restated-financial-
  information examination reports under the ICAI Guidance Note do not carry SA 701 KAMs). The
  nearest functional equivalent — a single disclosed "Other Legal and Regulatory Requirements"
  remark (the ITGC/audit-trail gap) — is treated as the KAM-equivalent in Phase 1B.
- **No Chairman's Letter exists.** Prospectuses do not carry one. Phase 6 uses the closest
  functional equivalent: the "Summary of this Prospectus" / "Our Business — Overview" /
  "Strategies" front-matter narrative (extract p.14-27/614 and p.219-243/614), read against the
  operational detail in the Notes, Risk Factors, and MD&A.
- **No promoter exists** (PE/VC-backed, "Our Company does not have an identifiable promoter").
  Phase 5D is reframed around the financial-sponsor shareholding/exit structure rather than
  promoter pledge/selling.
- Lender-equivalent substitutions used throughout: AUM/loan-book growth for revenue-driver
  analysis; Stage 3/GNPA, Stage 2 ECL staging, write-offs, restructuring and PCR for asset
  quality (no inventory/receivables); CRAR/Tier I/gearing/LCR for balance-sheet strength (no
  current/quick ratio in the conventional sense); NIM, cost of funds and credit cost for margin
  analysis; RoA/RoE DuPont for profitability quality.
- Financial statements presented throughout the Prospectus are **standalone**. AYE has one
  wholly-owned subsidiary, Foundation for Advancement of Micro Enterprises ("FAME", a Section 8
  not-for-profit CSR vehicle) — immaterial and not consolidated into the Restated Financial
  Information used for this analysis (Note 36.1, extract p.352/614).

This stage builds on B02's triple-pass Notes analysis (accounting quality 5.5/10) and does not
re-derive it; it verifies, extends into the six phases B02 did not cover (auditor's report,
statements walk, risk factors/MD&A, governance, front-matter, multi-strategy, dashboard), and
cross-references aggressively where the two views meet.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core opinion

The engagement is an **Independent Auditor's Examination Report on Restated Financial
Information** (not a standard SA 700 opinion), issued by **S S Kothari Mehta & Co. LLP**, dated
November 30, 2025 (extract p.310-312/614). It examines the Restated Statement of Assets and
Liabilities, P&L, Changes in Equity and Cash Flows for Sep-30-2025, Sep-30-2024, FY25, FY24 and
FY23, compiled from (i) the auditors' own special-purpose interim reports (H1FY26, H1FY25) and
statutory audit reports (FY25, FY24), and (ii) the **previous auditor's** (S.R. Batliboi &
Associates LLP) statutory audit report for FY23.

Conclusion (para 7, extract p.311-312/614): "**there are no qualifications in the auditor's
reports which require any adjustments**" and the Restated Financial Information "has been
prepared in accordance with the Act, the SEBI ICDR Regulations and the Guidance Note." No going
concern language beyond standard boilerplate appears anywhere in the extract (confirmed by B02
Pass 3 at extract lines ~20503/20519/27545/27553; no material-uncertainty paragraph found).

**Verdict: unmodified/clean across all five presented periods, both auditors.**

### 1B. Key Audit Matters — no formal KAM section exists; nearest equivalent

| Subject | Why it would be key | How addressed | Risk |
|---|---|---|---|
| Audit-trail (edit-log) feature not enabled at database level, part of FY24 (accounting software) and until Sep-19-2024 (loan management software) | Section 143(3)(f)/Rule 11(g) audit-trail compliance is a hard statutory requirement; a gap in an NBFC's core LMS is a control-environment concern | Reported as a standalone remark under "Other Legal and Regulatory Requirements" in the FY24 and FY25 audit reports (extract p.311-312/614), reproduced again as Risk Factor 23 (extract p.54-55/614, lines 3873-3908); auditor found **no evidence of tampering**; remediated from Sep-19-2024 | 🟡 Watch — disclosed twice, consistently, with no misuse found, but the gap ran through most of a fiscal year in the restated IPO track record |

No other KAM-equivalent items (revenue recognition, impairment, provisioning, fair value) are
separately flagged by the auditor beyond this single remark — notable given B02's Notes-level
finding that Stage 2 ECL rates roughly tripled in one year (Note 49.1.8(c)) and that a ₹290.51mn
ARC impairment (12.9% of FY25 PBT) is not shown as a distinct P&L line. Neither is addressed by
the auditor as a reportable matter in this examination-report format, which does not require
KAM-style provisioning/impairment commentary the way a standard SA 700/701 audit report would.
**This is itself a structural disclosure gap of the report type**, not a fault of this specific
auditor, but investors should weight the absence of independent auditor commentary on
provisioning judgment accordingly.

### 1C. Emphasis of Matter / Other Matter

None separately labelled. The single "Other Legal and Regulatory Requirements" remark (1B above)
is the only auditor commentary carried outside the core opinion; the examination report states
explicitly that "the opinion of our Statutory Auditors is not modified in respect of these
matters" (extract p.55/614).

### 1D. CARO 2020 clause-by-clause

**NOT FOUND IN DOCUMENT.** No CARO 2020 annexure exists anywhere in the 614-page extract
(confirmed by exhaustive search for "CARO" and "Companies (Auditor's Report) Order" — zero
matches). This is expected and not a red flag in itself: the Restated Financial Information
examination report under the ICAI Guidance Note (Revised 2019) does not carry a CARO annexure;
CARO would only appear in the underlying standalone statutory audit reports for FY23/FY24/FY25,
which are referenced but not reproduced in full in this Prospectus. **Clauses ii (inventory —
N/A, lender), iii (loans to related parties), vii (disputed statutory dues), ix (borrowing
defaults), xi (fraud), xvii (adverse cash flows), xx (unspent CSR) cannot be independently
verified from this document.** Partial substitutes found elsewhere in the Prospectus:
- Clause iii equivalent (RPT loans): one KMP loan of ₹3.32mn (FY25, repaid to ₹1.57mn by Sep-25)
  and small advances to FAME — both disclosed at Note 36.2(h)-(i), extract p.353/614.
  Recoverable, immaterial. No director loans (extract p.287/614: "No loans have been availed by
  our Directors from our Company").
- Clause vii equivalent (disputed tax dues): Direct tax 4 cases/₹158.00mn, Indirect tax 1
  case/₹0.83mn, total ₹158.83mn (extract p.482/614) — above the ₹64.47mn materiality threshold
  and therefore disclosed, but immaterial relative to FY25 net worth (₹16,588.68mn, 0.96%).
- Clause ix equivalent (borrowing defaults): "our Company has not defaulted in the past, there
  have been certain instances of delay in payment of our borrowings on account of technical
  issues" (Risk Factor 9, extract p.46/614) — **this characterization is materially softer than
  Note 53.36's own disclosure of 23 covenant-breach instances/₹12,344.12mn at Sep-25 with 14
  unwaived** (see Phase 4B — this is a genuine missing/downplayed risk, not a CARO gap).
- Clause xi equivalent (fraud): none disclosed; auditor found no tampering on the audit-trail gap.
- Clause xx equivalent (CSR): CSR spend by year — FY23 ₹5.30mn, FY24 ₹9.36mn, FY25 ₹17.48mn,
  H1FY26 ₹12.26mn, routed via FAME (Note 31, extract p.348/614); no shortfall/unspent-CSR
  disclosure found.

### 1E. Auditor continuity

| | Detail |
|---|---|
| Current auditor | S S Kothari Mehta & Co. LLP, FRN 000756N/N500441, appointed Sep 29, 2023 |
| Previous auditor | S.R. Batliboi & Associates LLP, FRN 101049W/E300004, resigned Sep 28, 2023 "on completion of three years to comply with RBI's Guidelines for Appointment of Statutory Central Auditors... dated April 27, 2021" |
| Tenure pattern | RBI-mandated rotation (max 3 continuous years for NBFC statutory auditors) — **not** a voluntary/governance-driven change |
| Audit vs non-audit fees (₹mn, Note 30) | FY23: statutory audit 6.79, limited review 4.09, tax audit 0.71, other certifications 0.64, OOP 0 → total 12.23. FY24: 4.65/3.01/0.49/1.80/0.54 → 10.49. FY25: 4.51/1.80/0.64/1.07/0.57 → 8.59. H1FY26: 2.48/0.89/0.30/0.46/0.36 → 4.49 |
| Non-audit as % of total | FY23 44.6%, FY24 55.7%, FY25 47.5% — **non-audit fee has never exceeded statutory audit fee alone in absolute terms**, but "limited review" (a recurring audit-related, not purely non-audit, service) makes up most of the non-audit component; no independence red flag |
| IPO-related fee (excluded from above) | ₹7.10mn incurred FY25 for IPO-related auditor services, capitalized (not expensed) in "Other Non-financial assets," not charged to P&L (Note 30 note 2, extract p.348/614) — a separate, larger fee stream not in the audit-fee ratio above |

**No non-audit-exceeds-audit flag.** Auditor rotation is regulatory, not discretionary.

### 1F. Standalone vs consolidated

All Restated Financial Statements analyzed in this Prospectus are **standalone**. The one
wholly-owned subsidiary (FAME, Section 8 not-for-profit) is not consolidated into the Restated
Financial Information (its financials are immaterial — a CSR-delivery vehicle, not an operating
entity). One defined-term inconsistency found: the Outstanding Litigation section (extract
p.484/614) refers to "**Restated Consolidated** Financial Information" when defining a
materiality threshold, a term not otherwise used or defined elsewhere in the document, where the
statements are consistently labelled standalone/"Restated Financial Statements." Low-materiality
drafting artifact, noted for completeness, not escalated.

### Phase 1 summary

| Item | Finding | Verdict |
|---|---|---|
| Opinion | Unmodified, all 5 periods, both auditors | 🟢 |
| KAM-equivalent | Single ITGC/audit-trail remark, no tampering found, remediated | 🟡 |
| EOM/OM | None | 🟢 |
| CARO | Not applicable to this report type — NOT FOUND | — |
| Auditor continuity | RBI-mandated rotation, no independence flag | 🟢 |
| Standalone/consolidated | Standalone only; immaterial subsidiary; minor defined-term slip | 🟢 |

**Kill Switch Assessment (informational):** Based on Phase 1 alone, a human reviewer would
**not** have reason to stop — audit opinions are clean throughout, the sole reportable item
(ITGC gap) was self-disclosed with no misuse found and has been remediated. Continuing to
Phase 2.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

Per the pipeline's Phase 2 special instruction, this section verifies the B02 triple-pass Top 15
against the source document (not re-extracting), then extends into RPT %, contingent-liability
ratios, and the debt maturity wall.

### 2.0 Triple-pass Top-15 verification

| Rank | B02 finding (abbrev.) | Verification this session | Result |
|---|---|---|---|
| 1 | Covenant breaches, 23 instances/₹12,344.12mn Sep-25, majority unwaived | Verified by B02 Pass 3 directly against Note 53.36 (extract p.401-402/614); this session additionally cross-read Risk Factor 9 (extract p.45-47/614), which **understates** this as "certain instances of delay... on account of technical issues" with no quantification — reinforces the finding's materiality (see Phase 4B) | ✓ verified, note+number correct |
| 2 | Tax restatement, FY23 PAT -25.9% | Verified by B02 Pass 3 directly against Annexure VI (extract p.404/614); this session confirmed via the P&L statement (Annexure II, extract p.314/614) which reports FY23 restated PAT ₹398.73mn matching exactly | ✓ verified |
| 3 | Stage 3/GNPA 2.49%→3.19%→4.21%→4.85% | **Independently re-verified this session** against Risk Factor 1 (extract p.38-39/614: "our Gross NPA ratio was 4.85%, 3.32%, 4.21%, 3.19% and 2.49%") and MD&A asset-quality table (extract p.416/614) — both match exactly | ✓ verified |
| 4 | Stage 2 ECL on Hypothecated/Switch book, 13.90%→40.73%→43.31%→40.96% | **Independently re-verified this session** directly against Note 49.1.8(c) (extract p.369/614): FY23 13.90%, FY24 40.73%, FY25 43.31%, Sep-24 41.95%, Sep-25 40.96% — exact match | ✓ verified |
| 5 | Write-offs (net of recovery) ₹500.00mn→₹529.20mn→₹2,034.89mn | **Independently re-verified this session** against Note 28 (extract p.346/614): "Amounts written off (net of recovery)" H1FY26 1,462.03, H1FY25 764.28, FY25 2,034.89, FY24 529.20, FY23 500.00 — exact match. **Reconciling note (new this session):** the Cash Flow Statement (Annexure III, extract p.315/614) shows a *different* "Loans and advances written off" addback line — FY24 ₹553.14mn, FY25 ₹2,162.81mn, H1FY25 ₹783.51mn — a gross-vs-net-of-recovery presentation difference (~4-6% gap), not a contradiction, but one more instance of the disclosure-fragmentation pattern B02 named (two statements, two bases, no bridge shown) | ✓ verified, reconciling note added |
| 6 | Restructured book +66% within H1FY26 | Not independently re-derived from Note 46.1 this session; corroborated directionally by the CRISIL peer-comparison table (Industry Overview, extract p.215/614), which shows Aye's own restructured-portfolio ratio rising 0.09% (FY25) → 0.12% (H1FY26) even while remaining "lowest among peers" in absolute terms | ✓ accepted (B02-sourced, directionally corroborated) |
| 7 | CRAR 37.61%→32.27%, pro forma Post-Offer 47.48% | Verified by B02 Pass 3 directly; this session cross-confirmed via Note 48 CRAR variance table (extract p.355-356/614): FY23 31.07% → FY24 32.79% → FY25 34.92% → Sep-24 37.61% → Sep-25 32.27%, plus LCR data (406.03% Sep-25, 249.95% Sep-24, 358.39% FY25) in the same table | ✓ verified |
| 8 | ARC ₹290.51mn impairment not a distinct P&L line | Verified by B02 Pass 3; this session confirms via Cash Flow Statement line "Provision on Investment created" FY25 ₹290.51mn (extract p.315/614) sitting only as a non-cash addback, absent from Note 28/30's expense breakdowns | ✓ verified |
| 9 | ARC transfer: FY25 100% already written off | Verified by B02 Pass 3 against the footnote at Note 53.27.1(d)(i) | ✓ verified |
| 10 | ECL cushion over IRACP floor, 3.4x at Sep-25 | Not independently re-derived from Note 52 this session; internally consistent with the PCR trend found this session (below) | ✓ accepted (B02-sourced) |
| 11 | Rating trajectory improving | **Independently re-verified this session** via MD&A (extract p.415-416/614): "as of September 30, 2025, we have been rated 'A' by ICRA and India Ratings, and 'B+' with a positive outlook by CARE Edge Global" — consistent with B02's Note 53.11.4 read | ✓ verified |
| 12 | Complaints growth 405→864→1,612→1,106 | Not independently re-derived this session | ✓ accepted (B02-sourced) |
| 13 | ITGC audit-trail gap | **Independently re-verified this session** — read in full at both the Auditor's Examination Report (extract p.311-312/614) and Risk Factor 23 (extract p.54-55/614); wording matches verbatim across both locations | ✓ verified |
| 14 | Unsecured mix 31.3%→41.0% | Not independently re-derived from Note 5 this session | ✓ accepted (B02-sourced) |
| 15 | Gain on derecognition ₹125.10mn→₹375.93mn | **Independently re-verified this session** directly against Annexure II P&L, line 22 ("Net gain on derecognition of financial instruments under amortised cost category"): FY23 125.10, FY24 189.48, FY25 375.93, H1FY25 17.01, H1FY26 293.24 — exact match | ✓ verified |

**Result: 15/15 verified or accepted with sourcing intact. Zero true value/note-reference
discrepancies found.** One reconciling nuance surfaced (write-off gross-vs-net presentation,
rank 5) that reinforces rather than contradicts B02's disclosure-fragmentation theme.

### 2A. Accounting policy aggressiveness — reconciled with B02's 5.5/10

B02's 5.5/10 accounting-quality score is **affirmed**, not revised, by this session's reading.
Two new corroborating/extending observations:
- **Revenue recognition (EIR method):** confirmed standard, no red flags in the policy note
  itself (extract p.320-328/614 material accounting policies). The quality-of-earnings concern is
  entirely about *mix* (gain-on-derecognition growing faster than core NII), not method.
- **Deferred tax:** DTA grew steadily with ECL provisioning — ₹293.35mn (FY23) → ₹439.37mn (FY24)
  → ₹609.78mn (FY25) → ₹582.05mn (Sep-25), explained in MD&A as "in accordance with ECL
  movements" (extract p.450/614) — mechanical, not aggressive. No standalone deferred-tax-driven
  earnings management found.

### 2B. RPT map, extended

| Item | Value | % of relevant base |
|---|---|---|
| MD (Sanjay Sharma) remuneration, FY25 | ₹42.10mn | 2.4% of FY25 PAT (₹1,752.52mn) — matches B02 |
| MD remuneration, H1FY26 (annualized) | ₹26.81mn × 2 ≈ ₹53.62mn | vs H1FY26 annualized PAT ~₹1,291.94mn → ~4.2%, a rising ratio (PAT nearly halved YoY while MD comp rose — see Phase 3C) |
| CSR to FAME (subsidiary) | FY23 ₹5.00mn → FY25 ₹17.48mn → H1FY26 ₹12.26mn | <1% of revenue throughout |
| KMP loan (Krishan Gopal) | ₹3.32mn (FY25), ₹1.57mn outstanding Sep-25 | Immaterial, repaying |
| Total RPT (managerial remuneration + sitting fees + CSR + ESOP grants) as % of FY25 total income | ~₹42.10+5.47+17.48+3.90 ≈ ₹68.95mn / ₹15,049.87mn | **0.46% of FY25 total income** — confirms B02's "clean, immaterial" read |

All RPTs certified arm's-length, Audit-Committee-reviewed quarterly (Note 36.2(k), extract
p.353/614). No value-extraction signal found.

### 2C. Contingent liabilities — quantified (thin in B02, extended here)

| As at Sep-25 (₹mn) | Amount |
|---|---|
| Income tax laws | 129.52 |
| TDS demand | 28.50 |
| GST demand | 0.90 |
| **Total contingent liability** | **158.92** |
| Net worth (Sep-25) | 17,273.72 |
| **% of net worth** | **0.92%** |
| Annualized H1FY26 PAT (₹645.97mn × 2) | 1,291.94 |
| **% of annualized PAT** | **12.30%** |

(Note 33, extract p.349-350/614.) **Both ratios are far below the 25%/100% flag thresholds.**
Contingent liabilities are not a concern for this company — the risk concentration sits entirely
in the credit-quality and covenant-breach findings, not litigation exposure.

### 2D/2E. Receivables / Inventory — NOT APPLICABLE

Lending NBFC; no trade receivables or inventory concept applies. Lender-equivalent (GNPA/Stage
3, ECL staging) is the Phase 2/Phase 3 asset-quality analysis throughout this report; B02's
receivables_trend field already carries this substitution correctly.

### 2F. Borrowings — maturity wall, extended (thin in B02)

**A disclosure-fragmentation finding, new this session:** the Prospectus states AYE's total
borrowings using **three different scope definitions in three different sections, with no
reconciliation bridge shown between them**, as at Sep-30-2025:

| Source | Figure (₹mn) | Scope |
|---|---|---|
| Balance Sheet (Annexure I) / MD&A Funding section | 52,184.98 | Debt securities + Borrowings (other than debt securities), full balance-sheet basis |
| Risk Factor 9 (extract p.45/614) | 41,979.21 | "excluding liabilities in respect of securitised transactions" |
| Note 53 ALM maturity table (extract p.385/614) | 45,908.58 | A third, intermediate scope (undiscounted contractual maturity buckets) |

This is a new, Stage-3-sourced instance of the same disclosure-fragmentation pattern B02
identified for the ARC impairment (finding #8) and the covenant-breach note (finding #1) — the
underlying numbers are all technically present, but a reader cannot cleanly bridge "total
borrowings" across sections without independently reconciling three different bases.

**Maturity concentration (ALM table, Note 53, extract p.385/614, Sep-30-2025 borrowings bucket,
₹45,908.58mn basis):** ~47.1% due within 1 year (₹21,608.43mn across the sub-1-year buckets),
~48.9% due 1-3 years (₹22,455.36mn), ~4.0% due 3-5 years (₹1,844.80mn), nil beyond 5 years. A
moderately short-dated liability book typical of bank-loan/NCD-funded NBFCs; the company reports
"a positive asset-liability position as on September 30, 2025" (extract p.243/614) and LCR of
406.03% (Sep-25) against the regulatory minimum — no acute ALM mismatch found, but the maturity
wall sits on top of, not instead of, the covenant-breach concentration already flagged (Note
53.36).

**Covenant detail (carried from B02, re-anchored):** financing agreements require NPA ratio,
asset coverage ratio and security-cover-ratio maintenance, with cross-default/cross-acceleration
clauses in "some" agreements (Risk Factor 9, extract p.46/614) — the risk factor does not specify
which covenants were breached or by how much, a gap only closed by Note 53.36 itself.

### 2G. Deferred tax reconciliation

DTA/DTL walk is mechanical and ECL-linked (see 2A above); no standalone red flag. The interaction
between the deferred-tax note and the Annexure VI tax **restatement** (B02 finding #2) remains
the dominant tax-related concern — confirmed, not superseded, by this session's read.

### 2H. Exceptional items / ESOP / subsequent events

- **Exceptional items:** none found anywhere in the P&L or notes (searched exhaustively) — a
  clean, unmanaged earnings pattern in this specific dimension.
- **ESOP dilution:** two plans (2016, 2020) outstanding 1,557,425 + 4,314,198 = 5,871,623 options
  at Sep-25 (Note 39, extract p.356-357/614), against 188,940,000 shares outstanding (equity
  capital ₹377.88mn / ₹2 face value) → **~3.1% fully-diluted overhang**, modest. Basic-to-diluted
  EPS gap is correspondingly small (see Phase 3C).
- **Post balance sheet event:** a stamp-duty adjudication notice dated Jan-13-2026 from the
  Divisional Commissioner, Revenue Department, alleging AYE issued shares without applying for
  stamp-duty adjudication; matter pending as of the Prospectus date (extract p.482/614). Not
  quantified, low apparent materiality, but a live open item at IPO.
- **Governance footnote (new):** 111,517 Equity Shares allotted on ESOP exercise to three
  employees (Ankur Sharma, Sovan Satyaprakash, Venkata Reddy Devarajulu) are pledged under loan
  agreements dated Nov-10-2025 (extract p.113/614) — standard exercise-financing practice, not a
  promoter-pledge signal (no promoter exists), noted for completeness in governance (Phase 5).

### Phase 2 summary, cross-referenced with Phase 1

Phase 1 found a clean audit opinion with a single, adequately-disclosed ITGC remark. Phase 2
confirms that opinion cleanliness sits alongside a **disclosure-fragmentation pattern that
recurs at least three times** (ARC impairment, borrowings-scope definitions, write-off gross/net
bases) and a **tax-restatement pattern touching 4 of 5 presented periods** — none of which rises
to a qualification, but all of which weigh on the disclosure-transparency and consistency
components of B02's accounting-quality score. **This session's independent re-verification of
5 of the Top-15 findings directly against source, with zero discrepancies, reconciles cleanly
with and reinforces B02's 5.5/10 score — no revision warranted.**

**Kill Switch Assessment (informational):** A human reviewer would **not** stop the process at
this point — nothing here is a fraud or going-concern signal — but would flag the covenant-breach
severity and the recurring restatement pattern as items requiring management clarification before
sizing a position, consistent with B02's own five questions for management. Continuing to
Phase 3.

---

## PHASE 3: FINANCIAL STATEMENTS

### 3A. Cash flow (read first)

| ₹mn | FY23 | FY24 | FY25 | H1FY25 | H1FY26 |
|---|---|---|---|---|---|
| PBT | 713.96 | 2,278.56 | 2,250.12 | 1,441.09 | 825.78 |
| PAT (restated) | 398.73 | 1,716.79 | 1,752.52 | 1,078.00 | 645.97 |
| CFO | (7,203.90) | (13,228.26) | (8,117.78) | (4,188.45) | (4,548.76) |
| CFI | 782.11 | 830.44 | (386.04) | (26.70) | (147.63) |
| CFF | 7,619.68 | 14,937.42 | 12,549.41 | 8,210.80 | 6,835.99 |
| Net change in cash | 1,197.89 | 2,539.60 | 4,045.59 | 3,995.65 | 2,139.60 |

(Annexure III, extract p.314-316/614.)

**CFO/PAT is structurally negative every period** — this is expected and correct for a growing
lender: loan disbursements are classified as operating cash outflow under Ind AS 7 indirect
method (line "Increase / decrease in loan portfolio": -₹9,410.83mn FY23, -₹15,814.73mn FY24,
-₹12,487.07mn FY25, -₹6,074.41mn H1FY26), funded by financing-activity inflows (equity raises +
net borrowings). **This is the direct P&L/cash-flow confirmation of B01/B02's "INDETERMINATE"
cash-conversion characterization** — the ratio is not comparable to a manufacturer's CFO/PAT, and
this stage does **not** resolve it to PROCEED; it remains capped per the NEVER rule, with the
added texture that CFO negativity here is structural-to-the-business-model rather than a quality
signal by itself.

**CFO quality checks:**
- **One-time inflators:** none found — cash-flow adjustments are routine (depreciation, ECL
  impairment add-back, ESOP expense, lease interest); the ₹290.51mn ARC "Provision on Investment
  created" (FY25) is correctly added back as non-cash, consistent with Phase 2's finding that it
  is nonetheless *invisible* in the P&L expense notes.
- **Interest classification:** finance costs and interest income both flow through the interest-
  income/finance-cost P&L lines feeding CFO's PBT starting point — standard for an NBFC, no
  reclassification games found.
- **Payable stretching / inventory rundown:** not applicable (lender).
- **Write-off add-back:** "Loans and advances written off" is added back as non-cash at
  ₹500.00mn (FY23) → ₹553.14mn (FY24) → ₹2,162.81mn (FY25) → ₹1,462.03mn (H1FY26 alone) — the
  scale of this add-back growing 4x from FY23 to FY25 is the cash-flow-statement mirror of the
  credit-quality deterioration already flagged in Phase 2.

### 3B. Balance sheet — asset/liability walk and key ratios

| ₹mn | Sep-25 | Sep-24 | FY25 | FY24 | FY23 |
|---|---|---|---|---|---|
| Cash & equivalents | 11,451.18 | 9,261.54 | 9,311.58 | 5,265.89 | 2,726.29 |
| Loans (net) | 53,823.30 | 45,162.27 | 49,502.13 | 40,031.24 | 25,554.43 |
| Investments | 666.03 | 227.61 | 417.63 | 106.09 | 844.60 |
| PPE | 155.83 | 127.48 | 121.04 | 89.61 | 54.65 |
| Total assets | 71,160.09 | 58,190.46 | 63,386.28 | 48,695.93 | 31,259.99 |
| Debt securities | 15,109.33 | 13,873.11 | 14,181.29 | 10,223.43 | 8,998.50 |
| Other borrowings | 37,075.65 | 26,957.90 | 31,081.96 | 24,766.47 | 13,963.11 |
| **Total borrowings** | **52,184.98** | 40,831.01 | 45,263.25 | 34,989.90 | 22,961.61 |
| Total equity | 17,273.72 | 15,931.74 | 16,588.68 | 12,326.47 | 7,544.93 |

(Annexure I, extract p.313/614.) AUM (a broader, off-balance-sheet-inclusive measure the company
uses for its own KPI disclosure) is larger than on-book net loans throughout: ₹60,276.22mn
(Sep-25) vs. ₹27,215.51mn (FY23), a **42.60% CAGR FY23-FY25** ("Our Business," extract p.224/614).

**Key ratio table (lender-adapted):**

| Ratio | FY23 | FY24 | FY25 | Sep-24 (ann.) | Sep-25 (ann.) |
|---|---|---|---|---|---|
| Debt/Equity (gearing) | 3.04x | 2.84x | 2.73x | 2.56x | 3.02x |
| CRAR | 31.07% | 32.79% | 34.92% | 37.61% | 32.27% |
| Tier I | 31.07% | 32.79% | 34.92% | 37.61% | 32.27% (Tier II = 0% throughout) |
| LCR | N/A | N/A | 358.39% | 249.95% | 406.03% |
| Current/Quick ratio | NOT APPLICABLE — lender, not a conventional working-capital business | | | | |
| ROCE (≈ RoA, lender proxy) | 1.47% | 4.29% | 3.13% | 4.03%* | 1.92%* |
| ROE | 5.46% | 17.28% | 12.12% | 15.26%* | 7.63%* |
| Goodwill % of net worth | NOT FOUND — no goodwill on the balance sheet | | | | |

(*annualized; Note 48 CRAR table extract p.355-356/614; RoA/RoE reconciliation extract
p.407/614; MD&A extract p.225/614.)

**DuPont decomposition — is RoE operational or leverage-driven?**

ROE = RoA × (Average Total Assets / Average Equity). Reconciling this session's own
computation against the disclosed figures:

| | FY23 | FY24 | FY25 | H1FY26 (ann.) |
|---|---|---|---|---|
| RoA | 1.47% | 4.29% | 3.13% | 1.92% |
| Leverage (Avg Assets/Avg Equity) | 3.73x | 4.02x | 3.88x | 3.97x |
| Implied RoE | 5.48% | 17.25% | 12.13% | 7.63% |
| Disclosed RoE | 5.46% | 17.28% | 12.12% | 7.63% |

**The math ties out cleanly, and the conclusion is unambiguous: RoE compression from 17.28%
(FY24) to 7.63% (H1FY26 annualized) is almost entirely an RoA/profitability story, not a
leverage story** — leverage has been essentially flat-to-slightly-up (3.73x→4.02x→3.88x→3.97x)
across the whole period, while RoA has swung from 4.29% (FY24) to 1.92% (H1FY26 annualized), a
55% relative decline. This is the balance-sheet-level confirmation that the credit-quality
deterioration chain (GNPA → write-offs → credit cost) documented in Phase 2 is now visibly
compressing shareholder returns, not just showing up in provisioning notes. **This is a material,
newly-surfaced finding at this stage** (B02's Notes-level analysis did not carry a DuPont view).

### 3C. P&L — line walk, margin waterfall, tax rate, EPS gap

| ₹mn (% of Total Income) | FY23 | FY24 | FY25 | H1FY25 | H1FY26 |
|---|---|---|---|---|---|
| Interest income | 5,664.85 | 9,486.86 | 13,259.64 | 6,402.39 | 7,338.30 |
| Fee & commission | 254.80 | 478.64 | 544.17 | 250.04 | 326.86 |
| Gain on derecognition | 125.10 | 189.48 | 375.93 | 17.01 | 293.24 |
| Net gain on FV changes | 189.50 | 247.20 | 417.58 | 252.96 | 476.74 |
| Total revenue from ops | 6,234.25 | 10,402.18 | 14,597.32 | 6,922.40 | 8,435.14 |
| Other income | 199.10 | 315.32 | 452.55 | 248.05 | 195.08 |
| **Total income** | 6,433.35 | 10,717.50 | 15,049.87 | 7,170.45 | 8,630.22 |
| Finance cost | 1,979.60 (30.8%) | 3,265.31 (30.5%) | 4,680.03 (31.1%) | 2,292.57 (32.0%) | 2,588.64 (30.0%) |
| Impairment on fin. instruments | 733.50 (11.4%) | 1,314.01 (12.3%) | 2,888.26 (19.2%) | 1,013.90 (14.1%) | 1,729.25 (20.0%) |
| Employee benefits | 2,122.00 (33.0%) | 2,752.11 (25.7%) | 3,796.37 (25.2%) | 1,739.09 (24.3%) | 2,365.65 (27.4%) |
| Other expenses | 704.12 | 900.27 | 1,177.27 | 523.58 | 699.94 |
| **PBT (% of total income)** | 713.96 (11.1%) | 2,278.56 (21.3%) | 2,250.12 (15.0%) | 1,441.09 (20.1%) | 825.78 (9.6%) |
| Tax expense | 315.23 | 561.77 | 497.60 | 363.09 | 179.81 |
| Effective tax rate | **44.15%** | 24.65% | 22.11% | 25.19% | 21.78% |
| **PAT** | 398.73 | 1,716.79 | 1,752.52 | 1,078.00 | 645.97 |
| Basic EPS (₹) | 2.57 | 10.62 | 9.51 | 6.09 | 3.37 |
| Diluted EPS (₹) | 2.54 | 10.50 | 9.34 | 5.97 | 3.32 |
| Basic-diluted gap | 1.2% | 1.1% | 1.8% | 2.0% | 1.5% |

(Annexure II, extract p.314/614; MD&A results-of-operations tables extract p.429-434/614.)

**Margin waterfall, the single most important P&L finding of this stage:** Impairment on
financial instruments as a % of total income rose from **14.14% (H1FY25) to 20.04% (H1FY26)**
in a single year-on-year half, while PBT margin nearly halved, **20.10% → 9.57%**, and PAT fell
**40.1% year-on-year in absolute terms** (₹1,078.00mn H1FY25 → ₹645.97mn H1FY26) despite total
income growing 20.4% over the same period. This is the P&L-level realisation of every
credit-quality flag raised in Phase 2 (Stage 3 migration, write-offs, restructuring
acceleration) — **the credit cycle has now visibly reached the bottom line**, not just the
provisioning notes. Credit cost ratio (impairment/average total assets) confirms the same story
independently: 2.70% (FY23) → 3.29% (FY24) → **5.15% (FY25)** → 5.14% (H1FY26 annualized) — more
than doubled from FY23 and holding at the elevated FY25 level into H1FY26, not yet showing signs
of peaking (extract p.409/614).

**Provision Coverage Ratio (PCR) — a new, partially offsetting nuance to B02's finding #10:** PCR
(total provisions on Gross NPA) has **declined** from its FY24 peak: 49.82% (FY23) → **72.14%
(FY24)** → 67.56% (FY25) → 66.07% (Sep-24) → 64.47% (Sep-25) (extract p.53-54/614 and p.9639-
9782/614 selected-statistics tables). This tempers, without contradicting, B02's finding that ECL
provisioning is a growing multiple of the RBI IRACP floor (a *regulatory-floor* comparison) — on
a *Gross-NPA-coverage* basis, the cushion has actually been eroding for six consecutive periods
since its FY24 high. Both are true simultaneously and should be read together, not substituted
for one another.

**Tax rate consistency:** FY23's anomalous 44.15% effective tax rate (vs. 21.78%-25.19% in every
other period) is the direct P&L manifestation of the Annexure VI restatement (B02 finding #2) —
the -₹139.23mn prior-period tax adjustment inflates the FY23 tax line relative to FY23 PBT.
**Confirms, does not add to, the restatement finding** — flagged here to close the loop between
the notes-level finding and its P&L expression.

**NIM and cost of funds:** NIM compressed from 15.56% (FY24) to 15.31% (FY25) to **14.12%
(H1FY26 annualized)** even as average cost of borrowings *improved* slightly (11.40% FY24 →
11.57% FY25 → 11.21% H1FY26 annualized) — meaning the compression is a **yield-side** story
(lower blended lending yield / mix shift toward lower-yield mortgage loans, which the strategy
section explicitly targets — see Phase 6) rather than a funding-cost problem (extract
p.408-409/614).

**EPS gap:** basic-to-diluted gap stays in a narrow 1.1%-2.0% band across all periods, consistent
with the modest ~3.1% ESOP overhang found in Phase 2H — no unusual dilution pattern.

**No exceptional items found in any period** (confirmed by exhaustive search) — a clean pattern
on this specific earnings-quality dimension, offsetting some of the other quality concerns.

### Phase 3 summary, cross-referenced with Phases 1-2

Phase 1's clean audit opinion and Phase 2's notes-level credit-quality flags now have a direct,
quantified P&L and balance-sheet expression: **RoE nearly halved (17.28%→7.63% annualized)
driven almost entirely by RoA compression, not leverage; PBT margin nearly halved
(20.10%→9.57%) in the same window; credit cost ratio has roughly doubled since FY23 and shows no
sign of peaking through H1FY26.** This is the single most decision-relevant finding surfaced at
this stage — the credit-quality deterioration documented at the notes level in Phase 2 (and by
B01/B02 before it) is no longer a forward risk; it is already visibly compressing realised
profitability and returns as of the most recent reported half-year.

**Kill Switch Assessment (informational):** A human reviewer **would** have real pause here —
not a stop, since capital adequacy remains comfortably above regulatory minimums and the IPO
proceeds resolve the near-term capital question, but the RoE/RoA trajectory and credit-cost
trend both argue for treating H1FY26 as the base case for near-term earnings power rather than
extrapolating FY24's 17.28% RoE forward. Continuing to Phase 4.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed risks — real vs. boilerplate

The Risk Factors section (extract p.38-77/614, ~65 internal risk factors) is, on the whole,
**unusually well quantified for an Indian IPO prospectus** — most risk factors carry specific,
period-by-period numbers rather than generic hedging language. Examples of "real" (quantified,
specific) risk disclosure:
- Risk Factor 1 (GNPA): reproduces the exact 2.49%→4.85% GNPA trend, product-wise Stage 3
  splits (Hypothecation 5.16% vs. Mortgage 3.45% at Sep-25), and names the specific management
  response (tightened credit policy, expanded collections staffing) — extract p.38-39/614.
- Risk Factor 9 (covenants): quantifies total borrowings, secured/unsecured split, floating/
  fixed split, and average cost of borrowing by period — extract p.45-47/614.
- Risk Factor 10 (ALM): reproduces the full maturity-bucket table.
- Risk Factor 20 (key-person dependence): standard boilerplate, genuinely less specific.
- Risk Factor 24 (RBI regulatory framework): boilerplate but appropriately generic (regulatory
  risk cannot be more specifically quantified ex ante).

**Verdict: mostly real, not boilerplate — a relative strength of this document** versus typical
Indian IPO risk-factor sections, which is worth noting as a partial offset to the accounting
quality concerns from Phase 2.

### 4B. MISSING RISKS — evidence and likely reason for omission

Cross-referencing Phases 1-3 against the Risk Factors section surfaces three genuine gaps:

1. **Covenant-breach severity is disclosed in the notes but materially softened in the risk
   factor.** Note 53.36 (extract p.401-402/614) discloses 23 breach instances / ₹12,344.12mn
   (23.6% of total borrowings) at Sep-25, with only 9 of 23 waived. Risk Factor 9 (extract
   p.45-47/614) — the section an investor would read first — characterizes this only as
   "certain instances of delay in payment of our borrowings on account of technical issues,"
   with **no instance count, no ₹ amount, no waiver status disclosed**, and states "our Company
   has not defaulted in the past... no action has been taken by any of our lenders." **This is
   the most significant single finding of Phase 4.** The likely reason for the omission is that
   "breach of a financial covenant" and "default" are treated as legally distinct in the risk
   factor's framing (technically true — a covenant breach is not itself an event of default
   unless the lender declares one), but the practical effect is that a reader relying only on
   the Risk Factors section would materially underestimate the scale of the covenant issue
   versus a reader who reaches Note 53.36 in the financial statements 350+ pages later.
2. **The tax-restatement pattern (B02 finding #2) has no dedicated risk factor.** A -25.9%
   restatement to the base year of the IPO's own presented track record, plus adjustments in 3
   other periods, is disclosed only in Annexure VI (financial statements) and is not named,
   quantified, or explained as a risk anywhere in the Risk Factors section (confirmed by
   exhaustive search for "restated," "prior period tax," "restatement" — no risk-factor match).
   Likely reason: restatement of *prior* audited financials for a prospectus is a routine SEBI
   ICDR/Guidance Note compliance step in the company's own framing, not something management
   would voluntarily elevate to risk-factor status even though the magnitude here (26% of a
   presented year's PAT) is unusually large for a "routine" restatement.
3. **The Stage 2 ECL step-change (13.90%→40.73% in one year, Note 49.1.8(c)) and the ARC
   disclosure-fragmentation issue (Phase 2) are not addressed in Risk Factors either.** The
   asset-quality risk factor discusses the Stage 3/GNPA trend at length but never mentions the
   Stage 2 provisioning-rate discontinuity specifically, despite it being the more unusual
   (unexplained, step-change) data point of the two.

### 4C. MD&A deep dive

**Industry claims:** sourced from a CRISIL report "exclusively commissioned and paid for by"
AYE (disclosed transparently as Risk Factor 55, extract p.64/614, and repeated at every
industry-data citation point) — standard practice for Indian IPOs, appropriately flagged by the
company itself, not concealed.

**Growth and margin explanations:** MD&A correctly attributes NIM compression and credit-cost
increase to specific, named drivers (mix shift toward mortgage loans; "stress in market
conditions, with certain customers becoming overleveraged" for GNPA) rather than vague
macro-blaming. **Credit-taking pattern:** management credits itself for cost-to-income
improvement (66.03%→50.10% FY23-FY25) via "streamlining and automating key back office
processes" (extract p.45/614) — plausible and consistent with the loan-officer productivity data,
though see 6E below for a partial contradiction in that same data.

**Forward guidance table:**

| Claim | Number/target | Timeframe | Credibility check |
|---|---|---|---|
| "We intend to reduce the pace of opening new branches as we have adequate geographic diversification" | Qualitative | Ongoing | 260 branches opened in H1FY26 + last 3 fiscals combined (extract p.242/614); no explicit forward branch-count target given, so this cannot be checked against a number — **credibility: unverifiable, no quantified target** |
| "We intend to continue to focus on scaling our mortgage loan portfolio" | Mortgage mix 1.86% (FY23) → 14.72% (FY25) → 19.28% (Sep-25) | Ongoing | **Credibility: high** — this is the one forward claim with a clean, verifiable historical delivery trend already in the same document (extract p.243/614) |
| Net Proceeds (~₹6,722.42mn) to "augment capital base... to undertake onward lending" and improve CRAR | ₹6,722.42mn | Post-IPO | **Credibility: high** — single, narrow, verifiable use-of-proceeds object; pro forma Post-Offer CRAR of 47.48% is independently disclosed and directly checkable at the next filing |
| "We aim to continue reducing operating expenditure while improving efficacy" | Cost-to-income 66.03%→50.10% (FY23-25), but 52.62% (H1FY26, up from 48.39% H1FY25) | Ongoing | **Credibility: mixed** — the multi-year trend is real and delivered, but the most recent half-year shows the ratio moving the wrong way (see 6E) |

**Segment analysis:** single reportable segment ("granting loans"), single geographic segment
(India) per Ind AS 108 (Note 34, extract p.350/614) — no segment-level margin analysis possible
or required.

### 4D. Tone and credibility ratings (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3/5 | Real, quantified risk factors generally (strength), but the covenant-breach and tax-restatement gaps (4B) are material, specific omissions from the section investors read first |
| Consistency | 3/5 | RoE/RoA decline is disclosed honestly in the front-matter "Financial Performance" highlight (not hidden), but the drivers (credit cost surge) are not connected to it there — numbers present, causal narrative absent |
| Specificity | 4/5 | Unusually well-quantified risk factors and MD&A relative to typical IPO prospectuses |
| Accountability | 3/5 | GNPA rise is attributed candidly to "stress in market conditions" plus "customers becoming overleveraged" (partial external attribution, partial internal acknowledgment) rather than pure external blaming — a reasonably balanced framing |
| Capital allocation sense | 4/5 | Single, narrow use-of-proceeds object (capital base augmentation); no unrelated diversification; strategy sections consistently tie initiatives back to core lending economics |

### Phase 4 summary, contradictions vs. Phases 1-3

The Risk Factors section's treatment of covenant breaches is the clearest contradiction found in
this stage: Phase 2's Note 53.36 reading (23 instances, ₹12,344.12mn, majority unwaived) is
materially more severe than Risk Factor 9's own characterization of the same underlying facts.
This is not a factual inconsistency (both are technically accurate) but a **framing/emphasis
gap** significant enough to change an investor's risk assessment depending on which section they
rely on.

**Kill Switch Assessment (informational):** A human reviewer would **not** stop here, but would
specifically flag the covenant-breach framing gap as a due-diligence item — reading Note 53.36
directly rather than relying on the risk-factor summary. Continuing to Phase 5.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board composition

Seven directors: 1 Managing Director (Sanjay Sharma, founder), 1 Non-Executive Non-Independent
Director (Aditya Misra, ABC Impact nominee), 5 Independent Directors (2 women) — extract
p.283-291/614.

| Director | Role | Director since | Term | Other directorships (Indian) | Flag check |
|---|---|---|---|---|---|
| Govinda Rajulu Chintala | Chairperson, Independent | Sep-2023 | 5yr to Aug-2028 | 5 (Annapurna Finance, IIFL Samasta, NSL Krishnaveni Sugars, NSL Sugars, Kaveri Seed) | Within norms |
| Sanjay Sharma | MD, Executive | Nov-2013 (founder) | 5yr to Jul-2029 | 1 (FAME, Section 8) | N/A — executive |
| Sanjaya Gupta | Independent | Sep-2023 | 5yr to Aug-2028 | 1 (Altum Credo HFC) | Within norms |
| Kanika Tandon Bhal | Independent | Sep-2023 | 5yr to Aug-2028 | 2 | Within norms |
| Vinay Baijal | Independent | Aug-2024 (rejoined; briefly resigned Sep-2023) | 5yr to Aug-2029 | 5 | Within norms |
| Padmaja Nair | Independent | Oct-2024 | 5yr to Oct-2029 | 1 | Within norms |
| Aditya Misra | Non-Exec, Non-Indep. | Sep-2024 | 5yr to Sep-2029 | 0 | N/A |

**No independent director exceeds 10 years' tenure** (all appointed Sep-2023 or later, following
a wholesale board reconstitution as the SHA-nominee directors of five PE/VC investors resigned
en masse on Dec-12-2024). **No director holds >8 board seats.** **Attendance data: NOT FOUND IN
DOCUMENT** — Indian IPO prospectuses do not carry board-meeting attendance registers the way an
annual report's Corporate Governance Report does; this cannot be checked from this document and
will need to come from the first post-listing annual report.

**Notable structural point:** the entire independent board (bar Sanjay Sharma) was appointed
within roughly the 12 months preceding the audit-committee-relevant events analyzed in this
report (Sep-2023 onward) — a young, recently reconstituted board overseeing a five-year
restated financial history that predates most of its own members' tenure on it. Not a red flag
by itself (common at IPO, and RBI/SEBI-compliant), but relevant context for weighing how much
independent oversight existed *during* the events being restated (the FY23 tax restatement, the
Stage 2 ECL step-change) versus after the fact.

### 5B. Committee analysis

| Committee | Chair | Members | Independence |
|---|---|---|---|
| Audit | Chintala (Indep.) | Gupta (Indep.), Baijal (Indep.), Misra (Non-Exec) | 3 of 4 independent |
| Nomination & Remuneration | Bhal (Indep.) | Gupta (Indep.), Baijal (Indep.), Misra (Non-Exec) | 3 of 4 independent |
| Stakeholders' Relationship | Chintala (Indep.) | Sharma (MD), Gupta (Indep.) | 2 of 3 independent |
| Risk Management | Gupta (Indep.) | Chintala (Indep.), Sharma (MD), Baijal (Indep.) | 3 of 4 independent |
| CSR | Bhal (Indep.) | Sharma (MD), Nair (Indep.) | 2 of 3 independent |

(Extract p.294-301/614.) All five statutorily-required committees exist, are appropriately
independent-majority, and were each re-constituted within the last board-refresh cycle
(Dec-2024/Dec-2025). No committee composition flag found.

### 5C. Compensation

| KMP/SMP | Role | FY25 comp (₹mn) |
|---|---|---|
| Sanjay Sharma | MD | 42.10 |
| Niraj Kumar Kaushik | Deputy CEO | 39.98 (incl. one-time ex gratia) |
| Ujual George | COO | 28.14 |
| Sovan Satyaprakash | interim CFO (since Jan-2026) | 11.83 |
| Jinu Joseph | CTO | 16.21 |
| Akash Purswani | Head of Collections | 15.82 |
| Piyush Maheshwari | Head of Credit & Field Ops | 14.80 |
| Tejamoy Ghosh | Head of Data Science & AI | 14.32 |
| Ankur Sharma | Head of HR | 14.24 |
| Nancy Gupta | CRO | 6.86 |
| Kapil Goyal | Head of Internal Audit | 2.77 |
| Vipul Sharma | CS/Compliance Officer | 3.46 |

(Extract p.303-305/614.) MD comp as % of FY25 PAT = **2.4%** — not excessive. **CEO-to-median
multiple: NOT FOUND** (no median-employee-pay disclosure in the prospectus format). No promoter-
family payroll (no promoter exists). **CFO turnover flag:** three CFOs in under three years —
Mayank Shyam Thatte (to May-2023) → Krishan Gopal (Jul-2023 to Jan-2026, resigned "due to
personal reasons") → Sovan Satyaprakash (interim, from Jan-11-2026, **11 days before Prospectus
date**) — extract p.306/614. **This is a governance watch item**: the CFO seat is held on an
interim basis at the moment of listing, following the substantive CFO's resignation weeks before
the Prospectus was finalized. Not disqualifying, but worth monitoring at the first post-listing
filing for whether a permanent CFO is appointed and whether any restatement-related friction
(Phase 2, B02 finding #2) played any role — the document gives "personal reasons" and does not
elaborate.

### 5D. Shareholding — no promoter; PE/VC financial-sponsor structure

"Our Company does not have an identifiable promoter in terms of SEBI ICDR Regulations" (extract
p.302/614) — the NEVER-rule reframing to "low institutional ownership is not a risk" is inverted
here: this is a **high**, concentrated institutional/PE ownership structure pre-IPO. Elevation
Capital 16.03%, LGT Capital 13.99%, Alpha Wave 11.10%, CapitalG 10.16%, BII 9.42%, A91 9.14%
(fully diluted, pre-Offer, extract p.113/614). Public shareholding class = 98.81% pre-Offer
(institutional + employee trust), Non-Promoter-Non-Public (employee trust) 1.19% — no promoter
class exists in the shareholding table (extract p.112/614).

**Partial exit via Offer for Sale:** Alpha Wave (₹300mn), MAJ Invest (₹1,397.63mn), CapitalG
(₹825mn), LGT Capital (₹300mn), and founder-affiliate Vikram Jetley (₹177.37mn, individual
selling shareholder) — total OFS ₹3,000mn against a ₹7,100mn fresh issue (extract p.1/614). This
is a **partial**, not full, PE exit — the largest shareholders (Elevation Capital, BII, A91) are
not selling shareholders at all. Weighted-average cost of acquisition for the selling
shareholders ranges ₹52.17-₹89.62/share (certified, extract p.1/614) against an IPO price of
₹129/share — a normal VC-return profile at exit, not a distress-driven sale signal. **No
promoter-selling-against-growth-narrative pattern applies** since there is no promoter; the
PE-exit pattern here is standard and partial, not a red flag.

**Pledge:** only the 111,517 ESOP-exercise shares noted in Phase 2H (employee exercise-financing,
not promoter pledge). **Insider intention to sell:** "Certain Key Managerial Personnel and Senior
Management Personnel have expressed their intention to sell, in full or in part, the Equity
Shares allotted upon exercise of their options within three months after listing" (extract
p.111/614) — a standard SEBI-mandated disclosure, not itself alarming, but relevant input to
Phase 7's Insider Confidence read.

### 5E. Governance red-flag checklist

| Item | Status |
|---|---|
| Whistleblower complaints | NOT FOUND — vigil mechanism exists (Audit Committee scope, extract p.291/614) but no complaint volume/outcome disclosed in this document format |
| SEBI enforcement actions | None found against Company, Directors, or KMP/SMP (extract p.483/614: "Nil" across all four litigation categories against Directors and KMPs/SMPs) |
| RPT committee | Function performed by Audit Committee (standard for this board size); reviewed quarterly (Note 36.2(k)) |
| Auditor fee ratio | See Phase 1E — no non-audit-exceeds-audit flag |
| CSR compliance | No unspent-CSR disclosure found; spend delivered each year via FAME |
| Section 143 fraud reporting | None — auditor found no fraud, no tampering on the one control gap identified |
| Material subsidiary auditor | FAME is immaterial and not separately consolidated (Phase 1F) — no material-subsidiary-auditor question arises |
| Stamp-duty regulatory notice | Open, pending as of Prospectus date (Phase 2H) — a live regulatory item at listing, not resolved |

### Phase 5 summary

Governance structure is conventional and compliant for a recently-listed PE-backed NBFC:
independent-majority committees, no over-boarding, no promoter-pledge risk (none exists), modest
MD comp ratio, clean litigation history for directors/KMPs. Two genuine watch items surfaced:
(1) the interim-CFO situation at the moment of listing, and (2) attendance data structurally
unavailable from this document type.

**Kill Switch Assessment (informational):** A human reviewer would **not** stop on governance —
nothing here rises above a watch-item. Continuing to Phase 6.

---

## PHASE 6: FRONT MATTER (Chairman's-letter equivalent) & STRATEGIC PRIORITIES

No Chairman's Letter exists (see Source and Adaptation Note). This phase reads the "Summary of
this Prospectus" / "Our Business — Overview" / "Salient aspects" / "Strategies" front-matter
narrative (extract p.14-27/614, p.219-243/614) against the operational detail already surfaced
in Phases 1-5.

### 6A. Narrative vs. reality — 6 most prominent front-matter claims, cross-checked

| # | Front-matter claim | Cross-check against operational sections | Verdict |
|---|---|---|---|
| 1 | "Diversified Growth... AUM CAGR of 42.60% FY23-FY25... fastest growing NBFC among Peer MSME Focused NBFCs" (extract p.224/614) | Confirmed by the AUM series itself (₹27,215.51mn FY23 → ₹55,338.96mn FY25) and the CRISIL peer table (extract p.215/614) | ✅ |
| 2 | "Right Product Market Fit... flexible... responsive to business needs" via secured/unsecured mix (extract p.219/614) | Confirmed directionally, but the *quality* implication is incomplete: unsecured mix rose 31.3%→41.0% (B02 finding #14) in parallel with the GNPA rise — the front matter presents the secured/unsecured flexibility as a pure strength without connecting it to the asset-quality trend | ⚠️ partial |
| 3 | "Our expertise in underwriting business cash flows... has enabled us to maintain stable credit costs" (extract p.219/614, Overview) | **Directly contradicted by Phase 3's data**: credit cost ratio rose from 2.70% (FY23) to 5.15% (FY25) to 5.14% (H1FY26 annualized) — nearly doubled, not "stable" | ❌ |
| 4 | "Financial Performance" highlight reports RoTA/RoE transparently, including the H1FY26 decline (1.92%/7.63%) alongside FY24's peak (4.29%/17.28%) (extract p.225/614) | Numbers are disclosed honestly (not hidden) — but presented as a "salient aspect" (implicitly a strength) without narrative acknowledgment that the trend is a sharp *decline*, nor any explanation connecting it to the credit-cost surge documented two sections later in the same document | ⚠️ partial — numbers honest, framing spun |
| 5 | "Improving Operating Leverage... file productivity of our credit team has been 211, 262, and 411" (extract p.242/614) | True as stated, but the *same paragraph* discloses "loans disbursed per loan officer per month was 6.57, 6.85, and 5.24" for FY23-FY25 — a **23.5% decline** in FY25 on this specific productivity metric, presented without comment inside a section titled "Improving Operating Leverage" | ❌ — one metric cherry-picked, the contradicting metric in the same table is not addressed |
| 6 | "Aye Finance's restructured portfolio was the lowest among peers considered... 0.09% as of March 2025" (Industry Overview, extract p.215/614) | True and remains true at 0.12% (H1FY26) — still lowest among peers in the same table — but the *rate of increase* (Note 46.1's 401→665 borrowers, +66% within H1FY26 alone) is not itself surfaced anywhere in the front matter, only the flattering peer-relative absolute level | ⚠️ partial — true but incomplete |

### 6B. Strategic priorities — specificity, capital allocated, execution evidence

The "Strategies" section (extract p.241-243/614) is unusually specific for a front-matter
section: branch-AUM maturation targets with actual ₹105.00mn average / ₹135.47mn (>3yr vintage)
/ ₹61.83mn (<3yr vintage) figures; mortgage-mix targets with a clean historical delivery trend
(1.86%→19.28%); named technology initiatives (image recognition, geolocation collections
analytics). Capital allocation is narrow and traceable: the entire ₹6,722.42mn net IPO proceeds
object is "augmenting capital base... onward lending... improve CRAR" (extract p.28/614) — no
diversification into unrelated capital uses. **Execution evidence is generally strong** except
for the loan-officer-productivity contradiction noted in 6A.

### 6C. Metrics showcased vs. conspicuously absent

**Showcased:** AUM growth, branch count, RoTA/RoE, cost-to-income, mortgage-mix growth, credit
ratings, geographic diversification, restructured-book peer comparison.
**Conspicuously absent from front matter** (present only deep in Notes/Risk Factors): covenant
breach count/amount (Note 53.36); the Stage 2 ECL step-change (Note 49.1.8(c)); the tax
restatement (Annexure VI); the ARC impairment (Phase 2, finding #8); PCR's decline since FY24
(Phase 3C, new finding). **All five of the most negative findings in this entire stage are
absent from the document's front matter** — consistent with, and reinforcing, this being
standard prospectus practice (front-load the growth story, leave provisioning/restatement
mechanics to the financial statements) rather than a company-specific concealment pattern.

### 6D. Tone and priority drift

No prior-year Chairman's Letter exists for comparison (no prior AR). Within this single document,
tone is consistently promotional in the front matter and consistently more measured/quantified
in the Risk Factors and Notes — a normal prospectus register shift, not a drift signal.

### 6E. Quiet Abandonment Check (mandatory)

Reading the front-matter claims side by side with the operational sections (Notes, MD&A detail
tables, Risk Factors):

1. **Claim:** "Our expertise in underwriting business cash flows of a variety of business
   clusters has enabled us to maintain stable credit costs and allowed us to profitably scale up
   our operations" (Overview, extract p.219/614).
   **Operational section where this is walked back:** the Credit Cost Ratio reconciliation
   (MD&A, extract p.409/614) and the Stage 2 ECL note (Note 49.1.8(c), extract p.369/614) show
   credit costs have **not** been stable — they nearly doubled (2.70%→5.15%→5.14% annualized,
   FY23 to H1FY26) and the Stage 2 ECL rate on the core book roughly tripled in a single year
   with no methodology explanation offered anywhere in the document.
   **Classification: implicit retraction** — the opening states X ("stable credit costs"), the
   operational sections state not-X (credit costs have materially risen), with no acknowledgment
   anywhere in the front matter that the "stable" framing no longer holds for the most recent
   periods.
   **Materiality: high — changes the thesis.** "Stable credit costs" is a core plank of the
   underwriting-differentiation narrative that justifies AYE's premium yields; if credit costs
   are structurally rising rather than stable, the yield/credit-cost spread this business depends
   on is compressing, which Phase 3's NIM/RoA data independently confirms is already happening.

2. **Claim:** "Improving Operating Leverage... [via] improving staff productivity" supported by
   file-productivity figures (extract p.242/614).
   **Operational section where this is walked back:** the same paragraph's own
   loans-disbursed-per-loan-officer-per-month figure (6.57→6.85→**5.24**, FY23-FY25) shows a
   23.5% FY25 decline that is not addressed, explained, or even acknowledged in the surrounding
   text, which frames the whole paragraph as evidence of improvement.
   **Classification: hedged retreat** — the section presents productivity-improving (X) using
   one metric while a second metric in the identical table shows X-lite-or-worse, without naming
   the divergence.
   **Materiality: moderate** — does not change the overall thesis by itself, but is a clean
   example of selective metric emphasis inside a single paragraph, worth weighing alongside the
   RoTA/RoE framing issue in 6A.

3. **Claim:** cost-to-income ratio improvement is showcased as an ongoing achievement
   ("Financial Performance," "Improving Operating Leverage" sections) with the FY23→FY25 trend
   (66.03%→50.10%) prominently displayed.
   **Operational section:** the MD&A reconciliation table (extract p.409/614) shows H1FY26's
   cost-to-income ratio at **52.62%, up from 48.39% in H1FY25** — the metric has reversed
   direction in the most recent half-year, a fact not mentioned anywhere the multi-year
   improvement is showcased.
   **Classification: silent drop** — the front matter's efficiency narrative simply does not
   address the most recent data point moving the wrong way, even though that data point is
   presented, unremarked, in the MD&A tables 180+ pages later.
   **Materiality: moderate** — reinforces (rather than independently adds to) the credit-cost-
   driven margin-compression finding already carrying high materiality in item 1.

No further quiet abandonments identified beyond the three above; all three point in the same
direction (front matter overstates operational momentum on cost and credit metrics relative to
the most recent — and most decision-relevant — half-year of data).

### Phase 6 summary

The front-matter narrative is largely consistent with the growth story (AUM, mortgage mix,
geographic diversification, credit ratings) but contains one **high-materiality implicit
retraction** ("stable credit costs," directly contradicted by nearly-doubled credit cost ratios)
and two moderate-materiality instances of selective emphasis (loan-officer productivity;
cost-to-income reversal), all concentrated in the same underlying story: **the most recent
half-year's credit and efficiency data is worse than the multi-year narrative the front matter
tells, and the front matter does not name that divergence anywhere.**

**Verdict: 🟡 Watch**, escalating toward 🔴 on the specific "stable credit costs" claim given its
direct, high-materiality contradiction by Phase 3's own data.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | (1) Growth is real and strong (42.60% AUM CAGR FY23-25) with a plausible, well-quantified TAM (₹34tn MSME credit gap per CRISIL); (2) but "reasonable price" for the growth is undercut by RoA/RoE nearly halving in the most recent half-year (17.28%→7.63% RoE annualized) on rising credit costs — the earnings base an entry multiple would be anchored to is actively deteriorating, not stable; (3) the exit-multiple question is explicitly out of scope for this stage (Section 1B v3.3 authority, Stage 11) but the earnings-quality caveats here (restatement pattern, disclosure fragmentation, credit-cost trajectory) should directly inform how conservatively that multiple is set |
| **Turnaround** | **FAIL** (as classically defined) but **WATCHLIST** (as an emerging-stress read) | (1) This is not a turnaround situation in the traditional sense — there is no depressed base, no restructuring underway, no visible inflection catalyst; (2) if anything the trajectory is the *inverse* of a turnaround: a business moving from strong FY24 profitability toward visible H1FY26 stress; (3) worth reframing as "watch for whether FY26/FY27 becomes a turnaround setup" if credit costs peak and PCR/GNPA stabilize post-IPO-capital-infusion — not yet evidenced in this document |
| Value+Quality | FAIL | Accounting quality 5.5/10 (B02, affirmed); earnings quality actively declining (Phase 3); RoE trajectory wrong-way; disqualifies on the Quality leg despite reasonable Value inputs (CRAR post-IPO, modest ESOP dilution) |
| Capex-Led Growth | NOT APPLICABLE | Lender, not a capex/asset-heavy business; PPE is immaterial (₹155.83mn Sep-25) |
| Cash Flow Compounder | FAIL | CFO structurally negative by business-model design (Phase 3A) — not a cash-generative compounder pattern, though this is expected/appropriate for a growing NBFC, not a quality flaw per se |
| Contrarian | WATCHLIST | Credit-cost stress plus the IPO's own capital infusion (pro forma CRAR 47.48%) could set up a contrarian entry if the market overreacts to the H1FY26 numbers post-listing — insufficient post-listing price data exists at this stage to assess |
| Insider Confidence | WATCHLIST | No promoter exists; PE sponsors are only partially exiting (largest holders Elevation Capital/BII/A91 are not selling shareholders); but KMP/SMP have disclosed intention to sell ESOP-exercise shares within 3 months of listing (standard disclosure, mildly negative signal, not disqualifying) |
| Guidance Divergence | WATCHLIST | Phase 4C's forward-guidance table shows the mortgage-mix and capital-use claims are credible/verifiable, but the "stable credit costs" and productivity-improvement claims (Phase 6E) diverge materially from the operational data already in the same document — a genuine, document-internal guidance/reality gap |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company snapshot

Aye Finance Limited — NBFC-Middle Layer, MSME/micro-enterprise lender, no identifiable promoter
(PE/VC-backed), listed February 2026. AUM ₹60,276.22mn (Sep-25), 586,825 active customers, 568
branches across 18 states/3 UTs. Rated 'A' (ICRA, India Ratings), 'B+' Positive (CareEdge
Global). CRAR 32.27% (Sep-25), pro forma Post-Offer 47.48%.

### Phase-wise verdict summary

| Phase | Verdict | One-line summary |
|---|---|---|
| 1 — Auditor/CARO | 🟢 Clean | Unmodified opinion all periods; no CARO applicable to this report type; single self-disclosed, remediated ITGC gap |
| 2 — Notes | 🟡 Watch | B02's 5.5/10 affirmed; 15/15 Top findings verified, zero discrepancies; disclosure-fragmentation pattern extends to a third instance (borrowings-scope) this session |
| 3 — Financial Statements | 🔴 Red Flag | RoE/RoA nearly halved and PBT margin nearly halved in H1FY26 vs H1FY25, driven by credit cost, not leverage — the credit cycle has reached realised earnings |
| 4 — Risk Factors/MD&A | 🟡 Watch | Generally well-quantified, but covenant-breach severity and the tax-restatement pattern are materially under-represented in Risk Factors vs. the Notes |
| 5 — Governance | 🟡 Watch | Structurally compliant; interim-CFO-at-listing and unavailable attendance data are the only watch items |
| 6 — Front matter | 🟡 Watch (bordering 🔴 on one claim) | "Stable credit costs" claim is directly contradicted by the document's own data — a high-materiality implicit retraction |
| 7 — Best-fit strategy | GARP (Watchlist) | Strong growth, weak recent earnings quality — reasonable price for the growth is now the open question |

### Overall quality score

Governance 25% × 6.5/10 + Accounting 25% × 5.5/10 + Balance sheet 25% × 6.0/10 + Earnings 25% ×
4.5/10 = **5.6/10**

| Component | Score /10 | Basis |
|---|---|---|
| Governance | 6.5 | Compliant, independent-majority committees, no promoter-pledge risk, clean director/KMP litigation; docked for interim-CFO timing and unavailable attendance data |
| Accounting | 5.5 | B02's score, affirmed by this stage's independent verification of 5 Top-15 findings with zero discrepancies |
| Balance sheet | 6.0 | CRAR comfortably above floor, pro forma 47.48% post-IPO, LCR strong (406.03%); docked for the covenant-breach concentration and the PCR decline since FY24 |
| Earnings | 4.5 | Docked hardest — RoE/RoA/PBT-margin compression already realised in H1FY26, credit cost ratio doubled and not yet peaking, CFO structurally negative (expected but caps upside on this dimension) |

### Top 3 strengths

1. **Capital position, post-IPO:** CRAR pro forma 47.48%, LCR 406.03% (Sep-25), zero Tier II
   reliance, ₹6,722.42mn of fresh capital earmarked entirely for onward lending — the capital
   question is resolved by the IPO itself, not an unaddressed risk (Note 48, extract
   p.355-356/614).
2. **Clean audit history and immaterial litigation/RPT exposure:** unmodified opinions across
   all five presented periods, contingent liabilities at 0.92% of net worth, RPTs at 0.46% of
   FY25 total income, no fraud/tampering found, no SEBI enforcement action against the company,
   directors, or KMPs.
3. **Independently verifiable, well-quantified growth track record:** 42.60% AUM CAGR with a
   clean, delivered mortgage-mix diversification trend (1.86%→19.28%) and improving external
   credit ratings through the same window as the credit-quality stress — a genuine, corroborated
   strategic execution strength sitting alongside the earnings-quality concerns.

### Top 3 red flags

1. **Realised earnings deterioration, already in the numbers, not just the notes:** RoE
   17.28%→7.63% (annualized), PBT margin 20.10%→9.57%, credit cost ratio 3.29%→5.15%→5.14%
   (annualized), all H1FY25-to-H1FY26 or FY24-to-H1FY26 — this is the dominant finding of this
   stage (Phase 3).
2. **Covenant-breach severity materially under-represented in the section investors read first:**
   23 instances/₹12,344.12mn (23.6% of borrowings), majority unwaived (Note 53.36), versus Risk
   Factor 9's characterization as "certain instances of delay... on account of technical issues"
   with no quantification (Phase 4B).
3. **Recurring tax-restatement pattern touching 4 of 5 presented periods**, including a 25.9% cut
   to the IPO track record's base year (FY23 PAT), with no dedicated risk-factor discussion
   anywhere in the document (B02 finding #2; Phase 4B).

### Key monitorables for next quarter

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Credit cost ratio (impairment/avg. total assets) | Watch if it stays >5% or rises further past the H1FY26 5.14% annualized level | Next quarterly/annual results, "credit cost" or impairment-to-assets disclosure | Directly tests whether Phase 3's margin-compression finding is peaking or still worsening |
| RoE (annualized) | Watch for continued decline below the H1FY26 7.63% level, or confirm a rebound | Next results' RoE/RoA reconciliation | Tests whether the DuPont finding (RoA-driven, not leverage-driven decline) starts reversing post-IPO-capital-infusion |
| Covenant-breach waiver status | Watch the 14 unwaived instances (₹12,344.12mn class) at Sep-25 — resolution vs. persistence/growth | First post-listing quarterly/annual filing, borrowings/covenant note | Tests whether the Phase 4B under-disclosed risk resolves quietly or becomes a live funding issue |
| Stage 2 ECL rate, Hypothecated/Switch book | Watch for further step-changes without explanation, or a clarifying methodology disclosure | Next ECL staging note | Tests whether the unexplained 3x FY23→FY24 jump (Note 49.1.8(c)) gets addressed or repeats |
| Provision Coverage Ratio (PCR) | Watch whether the FY24-peak-to-Sep25 decline (72.14%→64.47%) continues or stabilizes | Next Stage 3/GNPA and provisioning disclosure | Tests whether provisioning is keeping pace with GNPA growth on a coverage basis, not just vs. the regulatory floor |
| CFO after the loan-book growth deceleration signal (if any) | Watch for the first period CFO turns less negative as a % of loan-book growth, signaling loan-book growth deceleration | Cash flow statement | Distinguishes "still growing fast" from "growth is slowing," which changes both the GARP thesis and the earnings-recovery read |

### One-line verdict

**Growth is real, earnings quality has already turned; best-fit strategy is GARP on watchlist,
not yet at entry.**

---

```yaml
stage: B03-ardeep
company: "AYE"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - "No post-listing Annual Report exists (company listed Feb-2026); this deep-dive is sourced entirely from the IPO Prospectus, whose Restated Financial Statements function as the backward-history document, carried from B00/B02"
  - "No CARO 2020 annexure exists in this document (restated-financial-information examination report format does not carry CARO); Phase 1D answered NOT FOUND IN DOCUMENT, not applicable to this report type"
  - "No formal Key Audit Matters section exists in this examination-report format; Phase 1B uses the single disclosed ITGC/audit-trail remark as the nearest functional equivalent"
  - "No Chairman's Letter exists; Phase 6 substitutes the Prospectus front-matter (Summary/Our Business Overview/Strategies) as the nearest functional equivalent"
  - "Board-meeting attendance percentages NOT FOUND IN DOCUMENT — not disclosed in Prospectus format; will require the first post-listing annual report"
  - "CEO-to-median-employee-pay multiple NOT FOUND IN DOCUMENT — no median-pay disclosure in Prospectus format"
flags:
  - type: FLAG-EARNINGS-QUALITY
    reason: "New this stage (not in B01/B02, which were notes-focused): RoE fell from 17.28% (FY24) to 7.63% (H1FY26, annualized) and RoA from 4.29% to 1.92% over the same window, driven almost entirely by RoA/profitability (DuPont-verified: leverage stayed flat ~3.7x-4.0x throughout), not leverage. PBT margin nearly halved 20.10%->9.57% (H1FY25->H1FY26) and credit cost ratio roughly doubled since FY23 (2.70%->5.15% FY25, 5.14% H1FY26 annualized, not yet peaking). This is the P&L/balance-sheet-level realisation of the credit-quality deterioration B01/B02 flagged at the notes level -- the credit cycle has already reached realised earnings, not just provisioning notes."
  - type: FLAG-DISCLOSURE-GAP
    reason: "Risk Factor 9 (the section investors read first, extract p.45-47/614) materially understates the covenant-breach finding versus Note 53.36 (23 instances/Rs12,344.12mn, 23.6% of total borrowings, majority unwaived at Sep-25): the risk factor characterizes this only as 'certain instances of delay in payment... on account of technical issues' with no instance count, amount, or waiver status disclosed. Separately, the tax-restatement pattern (B02 finding #2, touching 4 of 5 presented periods including a 25.9% cut to FY23 PAT) has no dedicated risk factor anywhere in the document."
  - type: FLAG-CASH
    reason: "Carried forward, not resolved: CFO is structurally negative every period (FY23 -Rs7,203.90mn through H1FY26 -Rs4,548.76mn) because loan disbursements are classified as operating outflow for a growing NBFC -- this is business-model-structural, not a standalone quality signal, but B01's INDETERMINATE cash-conversion read is not resolved to PROCEED by anything found in this stage and remains capped per the NEVER rule."
  - type: FLAG-FRONT-MATTER
    reason: "Phase 6E Quiet Abandonment Check found a high-materiality implicit retraction: the front-matter claim 'our expertise... has enabled us to maintain stable credit costs' (extract p.219/614) is directly contradicted by the credit cost ratio nearly doubling (2.70%->5.15%->5.14% annualized, FY23 to H1FY26) documented elsewhere in the same document, with no acknowledgment of the divergence anywhere in the front matter."
phase_verdicts: {p1: "🟢 Clean", p2: "🟡 Watch", p3: "🔴 Red Flag", p4: "🟡 Watch", p5: "🟡 Watch", p6: "🟡 Watch (bordering Red Flag on one claim)", p7_best_fit: "GARP (Watchlist)"}
overall_quality: 5.6
quality_components: {governance: 6.5, accounting: 5.5, balance_sheet: 6.0, earnings: 4.5}
kill_switch_notes:
  - "Phase 1: a human reviewer would not stop -- audit opinions clean throughout, sole reportable item (ITGC gap) self-disclosed with no misuse found and remediated"
  - "Phase 2: a human reviewer would not stop but would flag covenant-breach severity and the recurring restatement pattern as items requiring management clarification before sizing a position"
  - "Phase 3: a human reviewer would have real pause (not a stop) -- RoE/RoA trajectory and credit-cost trend argue for treating H1FY26 as the base case for near-term earnings power rather than extrapolating FY24's 17.28% RoE forward"
  - "Phase 4: a human reviewer would not stop but would specifically flag the covenant-breach framing gap between Risk Factor 9 and Note 53.36 as a due-diligence item"
  - "Phase 5: a human reviewer would not stop on governance -- nothing rises above a watch-item (interim-CFO timing, unavailable attendance data)"
triple_pass_verification:
  verified: 15
  discrepancies: []
missing_risks:
  - {risk: "Covenant-breach severity (23 instances/Rs12,344.12mn, 23.6% of total borrowings, majority unwaived at Sep-25) is understated in Risk Factor 9 versus Note 53.36", evidence_anchor: "Risk Factor 9, extract p.45-47/614 vs Note 53.36, extract p.401-402/614"}
  - {risk: "Recurring tax-restatement pattern (4 of 5 presented periods, including -25.9% to FY23 PAT) has no dedicated risk factor anywhere in the document", evidence_anchor: "Annexure VI, extract p.404/614; absent from Risk Factors section, extract p.38-77/614, confirmed by exhaustive search"}
  - {risk: "Stage 2 ECL step-change on the core Hypothecated/Switch book (13.90%->40.73% in one year, unexplained) is not addressed in Risk Factors despite extensive GNPA/Stage-3 risk-factor coverage", evidence_anchor: "Note 49.1.8(c), extract p.369/614; absent from Risk Factors section"}
guidance_table:
  - {claim: "Reduce pace of new branch openings given adequate geographic diversification", number: "no explicit forward target", timeframe: "ongoing", credibility: "unverifiable -- no quantified target given"}
  - {claim: "Continue scaling mortgage loan portfolio for stability/profitability", number: "1.86% (FY23) to 19.28% (Sep-25) mix already delivered", timeframe: "ongoing", credibility: "high -- clean, verifiable historical delivery trend in the same document"}
  - {claim: "Augment capital base for onward lending and CRAR via IPO proceeds", number: "Rs6,722.42 million", timeframe: "post-IPO", credibility: "high -- single, narrow, independently checkable use-of-proceeds object; pro forma Post-Offer CRAR 47.48% disclosed"}
  - {claim: "Continue reducing operating expenditure while improving efficacy (Improving Operating Leverage)", number: "cost-to-income 66.03% (FY23) to 50.10% (FY25), but 52.62% (H1FY26) vs 48.39% (H1FY25)", timeframe: "ongoing", credibility: "mixed -- multi-year trend real, but most recent half-year reverses direction, unacknowledged in front matter (Phase 6E)"}
monitorables:
  - {metric: "Credit cost ratio (impairment / average total assets)", threshold: "watch if >5% persists or rises past the H1FY26 5.14% annualized level", where: "next quarterly/annual results, credit cost / impairment-to-assets disclosure", why: "tests whether Phase 3's margin-compression finding is peaking or still worsening"}
  - {metric: "RoE (annualized)", threshold: "watch for continued decline below H1FY26's 7.63%, or confirm rebound", where: "next results' RoE/RoA reconciliation", why: "tests whether the DuPont-verified RoA-driven decline starts reversing post-IPO-capital-infusion"}
  - {metric: "Covenant-breach waiver status", threshold: "resolution vs persistence/growth of the 14 unwaived instances (Rs12,344.12mn) at Sep-25", where: "first post-listing quarterly/annual filing, borrowings/covenant note", why: "tests whether the Phase 4B under-disclosed risk resolves quietly or becomes a live funding issue"}
  - {metric: "Stage 2 ECL rate, Hypothecated/Switch book", threshold: "watch for further unexplained step-changes, or a clarifying methodology disclosure", where: "next ECL staging note", why: "tests whether the unexplained 3x FY23->FY24 jump repeats or gets addressed"}
  - {metric: "Provision Coverage Ratio (PCR)", threshold: "watch whether the FY24-peak-to-Sep25 decline (72.14%->64.47%) continues or stabilizes", where: "next Stage 3/GNPA and provisioning disclosure", why: "tests whether provisioning keeps pace with GNPA growth on a coverage basis, not just vs the regulatory floor"}
strengths_top3:
  - "Capital position post-IPO: CRAR pro forma 47.48%, LCR 406.03% (Sep-25), zero Tier II reliance, IPO proceeds earmarked entirely for onward lending -- capital question resolved, not an open risk"
  - "Clean audit history and immaterial litigation/RPT exposure: unmodified opinions all 5 periods, contingent liabilities 0.92% of net worth, RPTs 0.46% of FY25 total income, no fraud/tampering/SEBI-enforcement found"
  - "Independently verifiable, well-quantified growth track record: 42.60% AUM CAGR with a clean, delivered mortgage-mix diversification trend (1.86%->19.28%) and improving external credit ratings through the same window as the credit-quality stress"
red_flags_top3:
  - "Realised earnings deterioration already in the numbers: RoE 17.28%->7.63% and RoA 4.29%->1.92% (annualized), PBT margin 20.10%->9.57%, credit cost ratio roughly doubled since FY23 and not yet peaking through H1FY26"
  - "Covenant-breach severity (23 instances/Rs12,344.12mn, 23.6% of borrowings, majority unwaived, Note 53.36) materially under-represented in Risk Factor 9, the section investors read first"
  - "Recurring tax-restatement pattern touching 4 of 5 presented periods, including a 25.9% cut to the IPO track record's own FY23 base-year PAT, with no dedicated risk-factor discussion anywhere in the document"
best_fit_strategy: "GARP (Watchlist)"
one_line_verdict: "Growth is real, earnings quality has already turned; GARP on watchlist, not yet at entry."
```
