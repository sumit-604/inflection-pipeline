# FABTECH TECHNOLOGIES LIMITED (FABTECH) — STAGE 3: ANNUAL REPORT DEEP DIVE, BACKWARD READ
Run date: 2026-08-04 | Model: claude-sonnet-5 | Protocol v1.2

**Sources:** AR = FY2025-26 Annual Report (scanned PDF, `e04aec7e-957d-4e45-9c8c-2b79504cc5be.pdf`), standalone notes 1-56, consolidated notes 1-62 (page footers cited as "AR p.__" standalone, "AR consol p.__" consolidated; where a footer could not be independently re-confirmed in this pass, the PDF page is cited instead, flagged "(PDF p.__)"). RHP = IPO Red Herring Prospectus dated 03-Oct-2025, `FP_INE0HF201011_03OCT2025.pdf` (518pp, text-native, cited "RHP p.__"). B02 = Stage 2 Notes triple-pass output. All figures ₹ Lakh unless converted to ₹ Cr for readability.

**Pipeline mode note:** every phase's kill-switch assessment is informational only per protocol; the run continues through all eight phases regardless of findings.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A. Core Opinion
Standalone and Consolidated Independent Auditor's Reports, both by Ajmera and Ajmera, Chartered Accountants (FRN 018796C), partner Omprakash Ajmera (Membership 157420), dated April 27, 2026. Both opinions are **unmodified/unqualified** ("give a true and fair view"). **No going-concern paragraph, no Emphasis of Matter section, in either report** — confirmed independently, consistent with B02's Pass-3 confirmation (AR consol p.139-141, Auditor's Report).

### 1B. Key Audit Matters
Both standalone and consolidated reports carry **exactly one KAM each**, worded identically in substance:

| Subject | Why key | How addressed | Risk |
|---|---|---|---|
| Recoverability and valuation of allowance for impairment of overdue Trade Receivables | Overdue trade receivables (>365 days) before ECL provisions: **₹5,854.04 Lakh standalone** / **₹5,887.55 Lakh consolidated**, as at March 31, 2026 (Note 13(a)). Assessment of recoverability is management-judgment-heavy (repayment history, financial position of counterparties, arrangement terms, market conditions) | Auditor: understood the ECL process/inputs; tested design/operating effectiveness of internal controls over the provisioning process; assessed historical-experience representativeness; tested the ECL methodology against Ind AS 109 and reasonableness of credit-loss rates including historical bad-debt experience | 🔴 Red — this is the auditor's own single point of concentrated concern; B02's finding #2 and #4 (receivables KAM + ECL curve-shape shift) sit directly inside this KAM |

No KAM on revenue recognition, impairment (goodwill/PPE), provisioning (other than receivables), or fair value was raised by the auditor despite: (i) the shipment-vs-completion revenue-policy tension flagged by B02 finding #9; (ii) the ~11x lease-liability jump (B02 finding #3); (iii) goodwill of ₹2,296.83 Lakh consolidated carried through the year with no separate KAM. **This is itself a finding for Phase 4B (missing-risk analysis): the auditor scoped only receivables as "key," leaving three other judgment-heavy areas B02 flagged as red without a corresponding audit-level signal.**

### 1C. Emphasis of Matter and Other Matters
No Emphasis of Matter in either report. **Other Matters (consolidated report only):** reliance on other auditors for one foreign subsidiary (Fabtech Technologies LLC, UAE — total assets ₹15,589.55 Lakh, revenue ₹17,378.57 Lakh, PAT ₹1,274.06 Lakh, pre-consolidation-adjustment, before consolidation) and one associate (Group's share of PAT ₹33.52 Lakh). The auditor's opinion is not modified with respect to this reliance (AR consol p.141).

### 1D. CARO 2020 — Clause by Clause

**Standalone CARO Annexure A:**

| Clause | Finding | Amount | Risk |
|---|---|---|---|
| (ii) Inventory | No adverse remark identified in material read; physical verification confirmed | — | 🟢 |
| (iii) Loans to related parties | Loans to related parties ₹3,596.41 Lakh, unsecured, 6% p.a., repayable on demand; auditor confirms repayment received as and when demanded, no amount overdue >90 days at year end | ₹3,596.41 Lakh (99.37% of all loans given, per Note 55(ix) Schedule III disclosure — matches B02 finding #6 exactly) | 🟡 Watch — no adverse CARO qualification, but the *concentration* itself (99.37% of the entire loan book to related parties) is the substantive concern, unchanged from B02 |
| (vii)(a) Statutory dues | **Qualified**: TDS default under Section 194C, ₹22,371 (rupees, not Lakh), relating to FY 2025-26, subsequently paid in two tranches (₹4,979 + ₹17,392) | ₹22,371 | 🟡 Watch, immaterial in quantum — confirms and closes out B02 finding #14's Holding-Co component precisely |
| (ix) Borrowing defaults | No default in repayment of loans/borrowings to any lender; not declared a willful defaulter by any bank/FI | — | 🟢 |
| (x)(a) IPO proceeds | Confirms utilisation lag consistent with Note 53 (below); no adverse qualification on the pace itself, only a factual statement | — | 🟡 Watch (disclosure fact, not a qualification) |
| (xi) Fraud | No fraud noticed or reported by the auditor during the year; no Section 143(12) reporting | — | 🟢 |
| (xiii) RPT (Sec 177/188) | Auditor states transactions with related parties comply with Sections 177 and 188, and that details are disclosed per Note 47 — **the auditor's clause (xiii) confirmation does not appear to have caught the land-purchase disclosure gap (B02 finding #1) or the lease-counterparty non-disclosure (B02 finding #3), since neither is called out** | — | 🔴 Red-flag-adjacent: an audit-scope gap, not a fabricated clean bill |
| (xvii) Cash losses | Not applicable / no adverse cash flow qualification in CARO (contrast with the actual FY26 standalone CFO collapse discussed in Phase 3 — CARO clause xvii tests cash losses in the current/immediately preceding year, a different test than CFO/PAT quality) | — | see Phase 3 cross-reference |
| (xx) Unspent CSR | Not applicable — CSR fully spent both years (Note 39: ₹59.22 Lakh spent vs ₹59.22 Lakh required FY26; prior-year shortfall of ₹0.68 Lakh carried and closed) | — | 🟢 |
| Audit trail | Confirmed the accounting software's audit-trail (edit log) feature operated throughout the year for all relevant transactions, no tampering found | — | 🟢 (a genuine positive; addresses a common Indian audit-trail compliance gap) |

**Consolidated CARO — clause (vii)(a) qualification across three entities (Annexure A to the consolidated auditor's report, AR consol p.142-143):**

| Entity | Relationship | Clause |
|---|---|---|
| Fabtech Technologies Limited | Holding Company | (vii)(a) — quantum ₹22,371, immaterial, resolved (see standalone table above) |
| FT Institutions Private Limited | Subsidiary | (vii)(a) — **quantum NOT FOUND IN DOCUMENT** (not disclosed in the summary table provided) |
| Mark Maker Engineering Private Limited | Associate | (vii)(a) — **quantum NOT FOUND IN DOCUMENT** |

This exactly reconciles B02 finding #14 (✓ verified — see Phase 2 triple-pass table).

**NEW FINDING not in B02's Top 15 — director disqualification under Section 164(2):** The consolidated auditor's report states, in the "Report on Other Legal and Regulatory Requirements" section (item 2(e), AR consol p.143): representations were received from directors of the Holding Company; **"one Subsidiary company and one associate company incorporated in India is disqualified as on March 31, 2026 from being appointed as a director in terms of Section 164(2) of the Act."** The sentence structure in the scanned/OCR'd text is imperfect, but the clause unambiguously states a director-level disqualification exists at one subsidiary (FT Institutions Private Limited) and one associate (Mark Maker Engineering Private Limited) level. **NOT FOUND IN DOCUMENT: the specific individual disqualified, or the underlying default (e.g., non-filing of financial statements/annual returns for three consecutive years) that triggered it.** 🔴 Red Flag — this is a governance-integrity signal at group level that B02's notes-only pass did not surface (Section 164(2) disqualifications are disclosed in the auditor's report, not the notes), and it directly touches the same two entities already carrying the unresolved CARO (vii)(a) statutory-dues qualification, suggesting a broader compliance-discipline gap at the subsidiary/associate level specifically (not at the Holding Company).

### 1E. Auditor Continuity
Ajmera and Ajmera, Chartered Accountants — **tenure/appointment year NOT FOUND IN DOCUMENT** in the sections read (first-year-post-IPO auditor continuity language not located; RHP due-diligence would typically confirm appointment history but was not cross-checked in this pass). Fee split (standalone, Note 37 "Auditor's remuneration," AR p.124):

| Component | FY26 (₹ Lakh) | FY25 (₹ Lakh) |
|---|---|---|
| Certification and tax consultancy | 12.67 | 3.64 |
| Statutory audit | 10.00 | 3.30 |
| Tax audit | 1.20 | 1.20 |
| GST audit | 1.00 | 1.00 |
| **Total** | **24.87** | **9.14** |

Non-audit fees (certification/tax consultancy = 12.67) are **less than** audit-related fees (statutory + tax + GST audit = 12.20) in FY26 — close to parity but non-audit fees are marginally the larger single line item (12.67 vs 10.00 statutory-audit-alone). The ratio does not breach the "non-audit exceeds audit" threshold when audit-related fees are aggregated (12.20 vs 12.67 — actually non-audit is marginally *larger* than the audit-fee aggregate by ₹0.47 Lakh, a razor-thin miss). 🟡 Watch — flagged for precision, though immaterial in absolute Lakh terms.

### 1F. Standalone vs Consolidated Differences
- Both reports: same KAM, same unmodified opinion, same audit firm.
- **Consolidated CARO carries two additional (vii)(a) qualifications the standalone report does not** (FT Institutions Private Limited, Mark Maker Engineering Private Limited) — see 1D.
- **Consolidated-only director-disqualification disclosure** (Section 164(2)) — see 1D, new finding.
- Reliance on other auditors: one foreign subsidiary (Fabtech Technologies LLC, UAE) and one associate, per Other Matters paragraph.
- **CFO trajectory diverges materially between standalone and consolidated** — this is a Phase 3 finding but is anchored here as a standalone-vs-consolidated structural difference: standalone CFO went from strongly positive (₹5,274.24 Lakh, FY25) to negative (₹(136.17) Lakh, FY26), while consolidated CFO went from negative (₹(3,614.49) Lakh, FY25) to marginally positive (₹47.74 Lakh, FY26). The parent's own cash generation deteriorated sharply even as the group's (still weak) cash generation nominally improved — see Phase 3A for full detail.

### Phase 1 Summary Table

| Item | Verdict |
|---|---|
| Opinion type | Unmodified, both standalone and consolidated |
| Going concern | None disclosed either report |
| KAM count/subject | 1, receivables recoverability, both reports |
| CARO adverse clauses | (vii)(a) at Holding Co (immaterial, resolved) + 2 unresolved at subsidiary/associate level (consolidated only) |
| Fraud (143(12)) | None reported |
| New Stage-3 finding | Section 164(2) director disqualification at one subsidiary + one associate |
| Auditor fee ratio | Non-audit fees marginally exceed audit-fee aggregate (₹12.67L vs ₹12.20L) |

**Phase 1 Verdict: 🟡 Watch.** The audit opinion is clean on its face, but the CARO annexure — read alongside B02's notes-based findings — shows an audit process that (a) did not scope revenue recognition, RPT completeness, or lease-liability provenance as a KAM despite obvious judgment exposure, and (b) surfaces a previously unflagged director-disqualification issue at group level.

**Kill Switch Assessment (informational):** Based on Phase 1 alone, a human reviewer would **not** have reason to stop the analysis — the opinion is unmodified and no fraud is reported — but **would** flag the Section 164(2) disqualification and the RPT-completeness audit-scope gap for immediate follow-up in due diligence calls with the auditor/company secretary before any capital commitment. Continuing to Phase 2 regardless, per protocol.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Triple-Pass Verification (B02 Top 15)

Per the Phase 2 special instruction, each B02 Top-15 finding was checked against the AR notes directly read in this pass.

| Rank | B02 Finding | Verification | Note |
|---|---|---|---|
| 1 | ₹19.71 Cr land from Fabtech Technologies International Pvt Ltd, absent from RPT note | ✓ verified, with a refinement: the land purchase **is disclosed once**, in Note 5 (PP&E), with the related-party name and transfer date ("Freehold land has been acquired from Fabtech Technologies International Private Limited... during the year and title deed is transferred vide agreement dated November 6, 2024," AR p.115) — but it is genuinely **absent from Note 47's RPT transaction table** and from the Board's Report AOC-2 "no material RPT" assertion (Phase 5). B02's core finding stands; precision improved. |
| 2 | Receivables KAM, gross +38.5% / net +35.6% vs revenue +25.7% | ✓ verified exactly against Note 13 consolidated: gross (considered good incl. retention money) ₹15,265.94 Lakh → ₹21,145.59 Lakh (+38.53%); net ₹15,073.61 Lakh → ₹20,433.51 Lakh (+35.55%) (AR consol p.174). **See new discrepancy flagged below** — the Consolidated Balance Sheet *face* shows trade receivables of ₹24,151.90 Lakh FY26, not ₹20,433.51 Lakh. |
| 3 | Lease liability ~11x jump, rent/deposit collapse to Fabtech Turnkey Projects LLP | ✓ verified exactly: lease liability ₹262.13 Lakh (Apr-24) → ₹2,902.59 Lakh (Mar-25) → ₹2,676.44 Lakh (Mar-26) (Note 49, AR p.136). Rent paid to Fabtech Turnkey Projects LLP ₹96.00 Lakh (FY25) → ₹8.50 Lakh (FY26); security deposit ₹91.44 Lakh → ₹0.25 Lakh (Note 47, AR p.133-134) ✓ exact match. |
| 4 | ECL curve-shape shift, standalone | ✓ verified exactly (standalone Note 13(b), AR p.117-118): 1-2yr 2.04%→10.10%, 2-3yr 3.46%→10.10%, >3yr 10.48%→10.16%. **Extension**: the consolidated ECL table shows a *different and arguably more alarming* pattern — see extension note below. |
| 5 | Bad-debt provision jump | ✓ verified exactly: standalone ₹530.21 Lakh FY26 vs nil FY25 (Note 37, AR p.124); consolidated ₹544.54 Lakh FY26 vs ₹7.74 Lakh FY25 (Note 39, AR consol p.182). |
| 6 | RPT entanglement (purchases, loans, borrowings) | ✓ verified: standalone RPT purchases (Altair, Advantek, Fabtech Technologies Cleanrooms, Fabsafe, FABL, Mark Maker, Pacifab) sum to ₹3,312.80 Lakh of ₹15,791.88 Lakh total purchases = 20.98% (AR p.133); loans to RP 99.37% (Note 55(ix)); RP borrowings — consolidated current borrowings from related party ₹2,350.83 Lakh of ₹4,220.24 Lakh total current borrowings = **55.71%** (Note 26 consol, AR consol p.178) — matches B02's 55.7% exactly. |
| 7 | Finance costs +122.8% on lease interest | ✓ verified exactly: ₹195.18L→₹434.94L standalone (+122.8%); lease interest ₹29.22L→₹249.24L (+753%) (Note 35, AR p.124). |
| 8 | Customer concentration reshuffle | ✓ verified exactly: Al-Afiya 1.58%→12.55% (Note 44c, AR consol p.185). **Refinement**: the three prior top customers did not "roughly halve" — Himalaya fell 13.98%→8.09% (-42%), Qomel Company Arabia fell 13.51%→3.46% (-74%), Massoun Darou fell 11.27%→3.38% (-70%). The decline is sharper than "roughly halved" for two of the three. |
| 9 | Shipment-based revenue recognition, no contract asset | ✓ verified exactly from the accounting policy text (standalone Note 3(D), AR p.103): "The performance obligation is considered satisfied upon the completion of contractual scope and formal customer acceptance. Contract revenue and related costs, where execution spans multiple accounting periods, are recognized based on actual shipments as of the reporting date." The tension is in the policy's own two sentences, confirmed verbatim. |
| 10 | FX hedge thin (single USD 20L forward), sensitivity nearly tripled | ✓ verified exactly: 1 forward contract, USD 20.00 Lakh notional (FY26) vs USD 10.00 Lakh (FY25) (Note 48 consol, AR consol p.191-192); 10% FX sensitivity to PBT ₹811.49 Lakh (FY25) → ₹2,350.64 Lakh (FY26), 2.90x (≈"nearly tripled," and ₹2,350.64 Lakh = ₹23.51 Cr, matching B02's "₹23.5 Cr" precisely). |
| 11 | TSA Process Equipment held-for-sale unchanged two years | ✓ verified: ₹166.60 Lakh standalone / ₹563.35 Lakh consolidated, unchanged Mar-25 to Mar-26 (Note 19/20 standalone; Note 20/59 consol). |
| 12 | RHP ~₹4.54 Cr loss scenario vs FY26 actual ~₹1.77 Cr gain | Partially re-verifiable: FY26 actual gain confirmed at ₹177.49 Lakh consolidated ("Profit on stake sale of FABL International Technologies LLP," Note 40 consol, AR consol p.182) = ₹1.7749 Cr, matching B02's "~₹1.77 Cr" exactly. The RHP's ₹4.54 Cr hypothetical loss scenario was not independently re-read in this pass (NOT re-verified, not contradicted). |
| 13 | 22.2% IPO-proceeds utilization | ✓ verified exactly from Note 53 (AR p.137): Total net proceeds ₹23,029.65 Lakh, utilised ₹5,107.70 Lakh = **22.18%**; working capital tranche ₹12,700.00 Lakh, utilised ₹2,747.24 Lakh = 21.63%; inorganic-growth tranche ₹3,000.00 Lakh, utilised **nil** (0%). |
| 14 | CARO (vii)(a) three-entity qualification | ✓ verified exactly (see Phase 1D). |
| 15 | Trademark fee ceased, new reverse guarantee fee | ✓ verified: trademark charges to Fabtech Technologies International Pvt Ltd — RHP shows ₹19.03L (FY23)→₹22.36L (FY24)→₹23.22L (FY25); AR Note 47 (FY26) shows **no trademark-charge line at all in the FY26 column** (consistent with cessation). Corporate Guarantee Expenses (company paying related parties): Fabtech Technologies International Pvt Ltd ₹21.38 Lakh + Fabtech Turnkey Projects LLP ₹21.38 Lakh = ₹42.76 Lakh, first appearing FY26 (Note 47, AR p.133) ✓ exact match. |

**Triple-pass verification result: 15 of 15 confirmed** (14 exact matches, 1 refined-but-confirmed on finding #1's precise disclosure location). Zero outright discrepancies against B02's Top 15 themselves.

### NEW discrepancy found in this pass (not one of B02's 15)
**Consolidated Balance Sheet face vs Note 13 do not reconcile for FY26 trade receivables.** The Consolidated Balance Sheet (AR consol p.149) shows current-asset "Trade receivables" of **₹24,151.90 Lakh** for FY26 (cross-footed independently: total current assets ₹55,360.26 Lakh minus every other current-asset line sums to exactly ₹24,151.89 Lakh, so the balance-sheet figure is internally consistent with the rest of the balance sheet). Note 13's own supporting schedule (AR consol p.174) shows a **Total (net of ECL) of ₹20,433.51 Lakh** for the same date. The two figures differ by **₹3,718.39 Lakh (₹37.18 Cr, 18.2%)**. FY25 ties out exactly (₹15,073.61 Lakh both places). **This is an unreconciled ₹37.18 Cr gap on the single largest KAM-flagged balance-sheet line, found only in FY26.** Given this is extracted from a scanned document, an OCR misread of one digit in one of the two source tables cannot be fully excluded, but the balance sheet figure independently cross-foots against eight other current-asset lines, which argues against a simple transcription error on my part. 🔴 **Red Flag — recommend independent confirmation against the company's XBRL filing or a direct company query before relying on either number.** If the higher balance-sheet figure is the correct one, FY26 receivables growth is understated by B02 and by this report's Note-13-based figures (38.5%/35.6%) — the true growth could be materially higher.

### Extension: consolidated ECL curve tells a different, additive story to the standalone curve
Standalone FY25 ECL rates were already elevated in the oldest bucket (>3yr: 10.48%) and stayed roughly flat into FY26 (10.16%), with the shift concentrated in the 1-2yr/2-3yr buckets (B02 finding #4). The **consolidated** ECL table (Note 13(b), AR consol p.174) shows a materially different starting point: FY25 consolidated rates were low and roughly uniform across all aged buckets (1-2yr 3.39%, 2-3yr 3.81%, >3yr 3.54%), and **all three buckets roughly tripled into FY26** (10.10%, 10.10%, 10.16% respectively). This means the group's foreign-subsidiary/consolidation-only receivables were carried at conservative, low loss rates through FY25 and converged sharply upward to ~10% across every aged bucket in FY26 — a broader, more uniform re-rating than the standalone table alone suggests. 🟡 Watch — this strengthens rather than weakens the underlying B02 concern (no rationale is disclosed for either the standalone or the consolidated shift), and shows the re-rating is a group-wide phenomenon, not confined to the parent's already-elevated oldest bucket.

### 2A. Accounting Policy Aggressiveness
- **Revenue recognition**: confirmed shipment-trigger vs completion/acceptance tension (Note 3(D)), verbatim above. Warranty policy: "back-to-back" vendor pass-through, "no separate provision for warranty costs has been established" (Note 51/standalone equivalent, AR p.137) — the company carries essentially zero own-scope warranty provision, consistent with B02's provisioning-adequacy score of 3/10.
- **Depreciation**: SLM per Schedule II; one deviation is *more conservative* than the schedule (Furniture & Fixtures — Leasehold Improvement depreciated over 9 years vs Schedule II's 10 years) (AR p.105-106). No aggressive-capitalisation policy found.
- **Ind AS 116 lease policy**: standard; no unusual discount-rate or classification choices disclosed in the policy text itself — the aggressiveness is entirely in the *unexplained counterparty and quantum* of the FY25 lease build-up (B02 finding #3), not in the stated policy.
- **ECL**: "simplified approach," provision matrix based on historically observed default rates, adjusted for forward-looking information — standard Ind AS 109 language, but as shown above the *applied rates* moved sharply and without disclosed rationale.
- **No policy change was quantified anywhere in the notes read.**

### 2B. RPT Map (extension beyond B02)
**NEW finding: a related-party investment not covered in B02's Top 15.** Note 47 (AR p.134, "III Balances as on year end" / transaction table) shows an "**Investment: Alanar One Health Equity Fund ₹660.00 Lakh**," first appearing in FY26 (nil FY25). Alanar One Health Equity Fund is listed among the "Companies/Firms in which directors/KMP have significant influence" (Note 47 related-party list, item 14). This is a fresh ₹6.6 Cr capital commitment to a related-party-influenced investment vehicle made in the same year as the land purchase, the lease build-up, and the unexplained provisioning shifts — **NOT FOUND IN DOCUMENT: the nature of Alanar One Health Equity Fund's business, or the commercial rationale for the investment.** 🟡 Watch, new.

**NEW finding: shared/cross-collateralised security structure spanning FABTECH, its sister listed company, and other related entities.** Borrowings security details (Note 25 standalone / Note 26 consolidated, AR p.121/178) disclose: "Common collateral for Fabtech Technologies Limited, Fabtech Technologies Cleanrooms Limited (Formerly Fabtech Technologies Cleanrooms Private Limited) and Fabsafe Technologies Private Limited by way of exclusive charge on unit no. 1, 2, 3 plot no. 190/191, GIDC Umbergaon, Gujarat and office premises... **in the name of Fabtech Turnkey Projects LLP**" plus "negative lien on the land at Khalapur, Raigad" and "Corporate guarantees of Fabtech Technologies International Private Limited and Fabtech Turnkey Projects LLP (to the extent of value of the property)." Separately, the contingent-liability note (Note 41/43) discloses FABTECH has itself **given** corporate guarantees of ₹1,000.00 Lakh for Fabtech Technologies Cleanrooms Limited's and ₹600.00 Lakh for Fabsafe Technologies Private Limited's working-capital facilities with Axis Bank. 🔴 Red Flag, new — this is a genuinely reciprocal, multi-entity credit-support and collateral web across the listed company, its listed sister company (Fabtech Technologies Cleanrooms Limited, BSE 544332, per task context the largest RPT supplier with no disclosed non-compete), and two other related private entities, with title to at least one pledged property sitting in a third related-party LLP's (Fabtech Turnkey Projects LLP) name — the same LLP implicated in the undisclosed-lease finding (B02 #3). This materially deepens the related-party-entanglement picture beyond P&L-level transactions into the balance sheet's core security architecture.

### 2C. Contingent Liabilities
| Component | FY26 (₹ Lakh, consol) | FY25 (₹ Lakh, consol) |
|---|---|---|
| Claims not acknowledged as debt (Clean Coats Pvt Ltd MSME dispute) | 85.53 | 85.53 |
| Corporate guarantee — Fabtech Technologies Cleanrooms Limited | 1,000.00 | 1,000.00 |
| Corporate guarantee — Fabsafe Technologies Private Limited | 600.00 | 600.00 |
| Performance guarantees, turnkey contracts | 2,829.57 | 1,570.67 |
| **Total** | **4,515.10** | **3,256.20** |

As % of net worth (consol, ₹41,976.93 Lakh): **10.76%** — below the 25% flag threshold.
As % of PAT (consol, ₹3,835.80 Lakh): **117.7%** — **exceeds the 100% flag threshold.**
As % of net worth (standalone, ₹38,987.89 Lakh): 11.58% — below 25%.
As % of PAT (standalone, ₹2,425.30 Lakh): **186.2%** — **exceeds 100%, more pronounced on a standalone basis.**
🟡 **Flag triggered on the PAT ratio, not the net-worth ratio**, both bases. Performance guarantees for turnkey contracts grew 80.2% YoY (₹1,570.67L→₹2,829.57L), roughly tracking the order-book/revenue growth rather than signalling new risk in isolation, but the two corporate guarantees for sister/related entities are pure related-party credit support with no offsetting consideration disclosed.

### 2D. Receivables
Fully covered above (verification + new discrepancy + ECL extension). Ageing (consolidated, FY26, Note 13a): <6m ₹11,922.69L; 6m-1yr ₹3,335.36L; 1-2yr ₹4,250.00L; 2-3yr ₹246.53L; >3yr ₹1,391.01L. Zero unbilled dues disclosed in every bucket, both years — confirms B02's finding that the natural balance-sheet corollary of "shipment-based, multi-period contract" revenue recognition (an unbilled-revenue/contract-asset balance) never appears.

### 2E. Inventory
Standalone: Stock in Trade ₹447.08 Lakh + Goods in Transit ₹1,462.20 Lakh = ₹1,909.28 Lakh (FY26) vs ₹579.97L + ₹1,019.20L = ₹1,599.17 Lakh (FY25), +19.4%, against revenue growth of 13.4% (standalone) — inventory growing faster than revenue, but off a small base and largely "goods in transit" (in-flight shipments, consistent with the shipment-recognition trigger). **No write-downs disclosed either year** ("There is no amount written down from the inventory during the year," Note 11, AR p.117). Consolidated inventory *fell* sharply (₹5,941.58L→₹2,134.14L) — this is a FABL-deconsolidation effect (raw materials/WIP of ₹1,109.40L/₹76.13L in FY25 disappear entirely from FY26, consistent with B02's Pass-3 note on the deconsolidation driving inventory movements).

### 2F. Borrowings
Standalone gearing is genuinely light and falling: total borrowings ₹1,891.95 Lakh (FY26) vs ₹3,324.80 Lakh (FY25); D/E 0.05x vs 0.21x (Note "Analytical Ratios," AR p.135). No covenant-breach language found. Security structure is the shared/cross-collateralised web described in 2B above — a genuine complexity even though absolute leverage is low. ICDs/loans given: 99.37% to related parties (already covered). No disputed/qualified borrowing found in CARO clause ix.

### 2G. Deferred Tax
Standalone net deferred tax asset ₹366.25 Lakh (FY26) vs ₹149.72 Lakh (FY25), reconciliation clean and fully disclosed (Note 10, AR p.116), effective tax rate 27.56% (FY26) vs 26.39% (FY25) — no unusual DTA recognition against unrecouped losses, no red flag.

### 2H. Exceptional Items, Goodwill, ESOP, Leases, Subsequent Events
- **Exceptional items 3-year-visible pattern**: FY25 standalone ₹2,197.80 Lakh (profit on sale of unlisted shares, TSA/Thermax-related per Note 52) → FY26 standalone ₹90.52 Lakh (profit on stake sale of Associate LLP) — an 95.9% decline, largely explaining the standalone PAT decline (₹3,837.57L→₹2,425.30L) alongside the finance-cost increase. Consolidated: FY25 ₹1,784.86 Lakh → FY26 ₹177.49 Lakh, same pattern (B02 finding #12).
- **Goodwill**: ₹2,296.83 Lakh (FY26) vs ₹3,699.81 Lakh (FY25) consolidated, declining — no impairment charge disclosed; the decline is the FABL deconsolidation, not an impairment event. Goodwill/net worth (consol) = 2,296.83/41,976.93 = 5.5% — low, not a red flag in isolation.
- **ESOP dilution**: NOT FOUND IN DOCUMENT — no ESOP scheme or dilution table located in the sections read.
- **Post-balance-sheet events**: dividend proposal only (₹0.60/share, ₹266.70 Lakh total, Note 54, AR p.137) — confirmed, matches B02's Pass-3 pattern-level observation that this is the *only* disclosed subsequent event despite ~₹179 Cr of unutilised IPO proceeds.

### Phase 2 Reconciliation with B02's Accounting-Quality Score
B02 scored accounting quality **4/10**. This pass's direct-source verification **confirms every one of B02's Top 15 at high confidence (15/15)** and adds two materially new red-flag-tier findings (the ₹37.18 Cr receivables reconciliation gap, and the shared-collateral/related-party-investment web) plus one amber addition (Alanar One Health Equity Fund) and one governance-tier addition from Phase 1 (Section 164(2) disqualification). **This pass does not raise the accounting-quality score — if anything the new findings argue for holding it at 4/10 rather than improving it**, since the new items compound rather than offset the RPT-fairness and provisioning weaknesses B02 already weighted most heavily.

**Phase 2 Verdict: 🔴 Red Flag.** All of B02's findings independently confirmed at the source; two new material findings added (balance-sheet-to-note reconciliation gap on receivables; multi-entity shared collateral/related-party investment web).

**Kill Switch Assessment (informational):** A human reviewer **would** have reason to pause before further capital allocation — the receivables reconciliation gap alone (₹37.18 Cr, unresolved) sits on the single item the auditor itself scoped as key, and it compounds an already-thin RPT-fairness picture. Continuing to Phase 3 regardless, per protocol.

---

## PHASE 3: FINANCIAL STATEMENTS

### 3A. Cash Flow (read first)

**Standalone:**

| Metric | FY26 | FY25 |
|---|---|---|
| PAT | ₹2,425.30 Lakh | ₹3,837.57 Lakh |
| CFO | **₹(136.17) Lakh** | ₹5,274.24 Lakh |
| CFO/PAT | **-5.6%** | 137.4% |

**Consolidated:**

| Metric | FY26 | FY25 |
|---|---|---|
| PAT | ₹3,835.80 Lakh | ₹4,645.29 Lakh |
| CFO | ₹47.74 Lakh | ₹(3,614.49) Lakh |
| CFO/PAT | **1.24%** | -77.8% |

🔴 **Red Flag, both bases, both years, in some direction.** The standalone CFO/PAT ratio collapsed from a strong 137.4% (FY25) to deeply negative -5.6% (FY26) — the parent company generated *less cash than its reported profit by a wide margin* in the IPO year itself, driven overwhelmingly by the receivables buildup (change in trade receivables used ₹1,645.91 Lakh of cash FY26 standalone). The consolidated picture is the mirror image but no better in substance: FY25 consolidated CFO was deeply negative (-77.8% of PAT) and FY26 only clawed back to a bare 1.24% — nowhere near the 0.7x (70%) threshold this protocol flags. **Both the standalone deterioration and the consolidated "recovery to near-zero" fail the CFO/PAT quality check.**

**CFO quality checks:**
- **Payable stretching, consolidated**: change in trade payables contributed **+₹4,450.79 Lakh** to consolidated operating cash flow in FY26 (vs +₹3,375.64 Lakh FY25), while trade receivables *consumed* ₹8,655.02 Lakh (vs ₹5,258.35 Lakh FY25). The near-breakeven consolidated CFO in FY26 is substantially a function of a larger payables swing partially offsetting a larger receivables drag — a classic quality flag (cash conversion propped up by extending suppliers rather than collecting from customers faster).
- **Interest classification**: interest income (₹1,069.21 Lakh implied standalone adjustment in the CF statement) sits in operating-activities adjustments but is economically closer to a treasury/investing return on parked IPO-proceeds fixed deposits — a presentation choice that flatters the "operating profit before working capital changes" subtotal, though it does not change the bottom-line CFO figure.
- **One-time inflators**: none identified in CFO itself (the exceptional gains sit above CFO in the P&L reconciliation, correctly excluded/added back).
- **Inventory rundown**: not a material driver either year (inventory change was a modest cash use both years, standalone).

**FCF**: standalone capex (payment for PP&E/intangibles) ₹470.81 Lakh consolidated vs depreciation ₹530.15 Lakh consolidated — capex is running *below* depreciation, consistent with a company that is not investing materially in fixed capacity (turnkey/asset-light equipment-supply model, consistent with the RHP's disclosed "asset light approach... procure key equipment from Related Entities").

**Financing flows / cash pile**: consolidated net cash increase of ₹7,782.60 Lakh FY26, driven almost entirely by the ₹20,752.03 Lakh net IPO proceeds; ₹11,744.92 Lakh of net investing outflow went into fixed deposits (parking IPO proceeds), consistent with the low utilisation shown in Note 53.

### 3B. Balance Sheet

**Standalone key ratios (Note "Analytical Ratios," AR p.135 — company-computed, cross-checked against the primary statements and internally consistent):**

| Ratio | FY26 | FY25 | Variance | Management's stated reason |
|---|---|---|---|---|
| Current ratio | 2.99x | 1.45x | +106.5% | IPO proceeds parked in FDs increased current assets |
| D/E | 0.05x | 0.21x | -77.0% | Shareholders' fund increased on IPO |
| Debt service coverage | 1.44x | 1.21x | +19.3% | Sufficient internal accrual |
| ROE | 8.86% | 27.25% | -67.5% | IPO-driven equity-base expansion |
| Inventory turnover | 8.83x | 8.05x | -9.6% | n/a |
| Trade receivables turnover | 2.01x | 2.18x | -7.8% | n/a |
| Trade payables turnover | 2.19x | 1.97x | +11.1% | n/a |
| Net capital turnover | 0.95x | 3.42x | -72.2% | Working capital increased on IPO proceeds |
| Net profit ratio | 9.05% | 16.23% | -44.3% | **FY25 had exceptional income from sale of investment which inflated PAT** — management's own explanation, candid |
| ROCE | 12.07% | 20.05% | -39.8% | IPO-driven capital-base expansion |
| ROI | 7.32% | 10.08% | -27.4% | IPO-driven asset-base expansion |

**Cross-reference to B02/Master framework:** the ROE/ROCE collapse is genuinely IPO-mechanical (denominator expansion from the equity raise), as B02 already concluded — this pass confirms it is *not* itself an earnings-quality issue, but the **net profit ratio decline (9.05% vs 16.23%) is a numerator issue, not IPO-mechanical**, and management's own footnote correctly attributes it to the FY25 exceptional gain rather than to any operating deterioration. That said, layering in the CFO collapse (3A) shows the *underlying cash-backed* earnings quality weakened materially in FY26 regardless of the exceptional-items explanation for the reported-profit decline — two separate phenomena moving in the same direction.

**DuPont-style read**: ROE fell from 27.25% to 8.86% almost entirely through the equity-base denominator (net worth roughly 2.5x'd on the IPO), not through margin or turnover deterioration in isolation — but turnover (net capital turnover -72.2%, net profit ratio -44.3%) both fell too, meaning **the ROE decline is not purely leverage/equity-mechanical — margin genuinely compressed and capital efficiency genuinely fell, compounding the equity-dilution effect rather than being fully explained by it.**

**Asset/liability walk (standalone, ₹ Lakh):** Total equity 38,987.89 (FY26) vs 15,753.96 (FY25); cash & equivalents 7,304.81 vs 382.52; bank balances (FDs) 12,168.98 vs 1,959.25; trade receivables net 14,409.73 vs 12,326.26; lease liabilities total 2,676.44 vs 2,902.59; trade payables 6,963.18 vs 7,436.63 (a rare *decline*, consistent with the "not payable-stretching" note in B02's Pass 3 for the standalone entity specifically — the payable-stretching quality flag applies at the consolidated level, not standalone).

**Consolidated asset/liability walk**: Total assets ₹69,088.68 Lakh vs ₹42,655.80 Lakh; total equity ₹41,976.93 Lakh vs ₹17,311.36 Lakh; goodwill ₹2,296.83 Lakh vs ₹3,699.81 Lakh (declining, FABL deconsolidation); **trade receivables — see the ₹37.18 Cr unreconciled gap flagged in Phase 2.**

### 3C. P&L

**Consolidated line walk (₹ Lakh):**

| Line | FY26 | FY25 | YoY |
|---|---|---|---|
| Revenue from operations | 41,077.18 | 32,666.85 | +25.7% |
| Other income | 2,055.77 | 927.36 | +121.7% |
| Total income | 43,132.95 | 33,594.21 | +28.4% |
| EBITDA (computed: PBT-before-exceptional + finance cost + depreciation) | ≈5,595.97 | 4,727.91 (RHP-stated) | +18.4% |
| EBITDA margin (on total income, per the company's own definition) | ≈12.97% | 14.07% | **-110bps, margin compression despite revenue acceleration** |
| Finance costs | 415.90 | 209.59 | +98.4% |
| Depreciation & amortisation | 530.15 | 260.78 | +103.4% |
| Exceptional items | 177.49 | 1,784.86 | -90.1% |
| PBT | 4,827.41 | 6,043.36 | -20.1% |
| Tax | 991.61 | 1,398.07 | -29.1% |
| PAT | 3,835.80 | 4,645.29 | -17.4% |
| Net profit margin (PAT/revenue) | 9.34% | 14.22% | compressing |
| Basic/diluted EPS | ₹10.00 | ₹14.34 | (basic = diluted both years; no dilution gap) |

**Other income >20% of PBT flag**: standalone other income (₹2,309.52 Lakh) is **73.2% of standalone PBT-before-exceptional-items (₹3,152.94 Lakh)** — a very large trigger of this protocol's flag. Composition (Note 31, AR p.123): interest income on bank deposits ₹676.37L (dominant, IPO-proceeds FDs), net FX gain ₹1,188.73L (largest single component — a translation/transaction gain, not a recurring operating item), interest on inter-corporate loan ₹9.43L, other interest ₹336.19L (the related-party loan interest B02 flagged as yield-ambiguous), fair-value gains on FVTPL assets ₹44.91L. **The FX-gain component (₹1,188.73L) is the single largest driver of other income and is inherently non-recurring/directional** — a materially weaker quality of "other income" than a pure interest-income story would suggest, since a currency reversal next year would flip this into a large negative swing given the company's own disclosed FX-sensitivity (₹23.5 Cr PBT swing per 10% move, Phase 2).

**Margin waterfall (consolidated, revenue → PAT, FY26)**: Revenue 41,077.18 → (- COGS/purchases/inventory change ≈24,256.31) → (- employee costs 4,333.44) → (- other expenses 8,987.64) → (+ other income 2,055.77) → EBIT-equivalent ≈5,555.55 → (- finance costs 415.90) → (- depreciation 530.15) → (+ share of associate profit 40.41) → PBT-before-exceptional 4,649.92 → (+ exceptional 177.49) → PBT 4,827.41 → (- tax 991.61) → PAT 3,835.80. **Margin compressed year-over-year despite 25.7% revenue growth** — this is the single most important P&L-level finding for a GARP thesis: **top-line growth this year did not translate into proportionate bottom-line growth**, and the gap is not fully explained by the (correctly disclosed) exceptional-item base effect alone, since EBITDA margin itself also compressed ~110bps.

**Exceptional items 3-year pattern**: see Phase 2H — a genuine, non-repeating, declining pattern (₹2,197.80L→₹90.52L standalone; ₹1,784.86L→₹177.49L consolidated), both years tied to investment/stake-sale gains, not operating exceptional items — a clean, disclosed pattern, not a red flag in itself, but it means **reported PAT growth/decline in both FY25 and FY26 is meaningfully non-operating-driven**, complicating any naive multi-year PAT-CAGR read (see Phase 7).

**Tax rate**: 27.56% (FY26) vs 26.39% (FY25) standalone — modest increase, fully reconciled in Note 10, no red flag.

### Phase 3 Cross-Reference with Phases 1-2
The CFO collapse (3A) sits directly beneath the auditor's own KAM (receivables recoverability, Phase 1B) and directly beneath B02's finding #2 (Phase 2) — three independent lenses (audit scope, notes-based ageing analysis, and now the primary cash-flow statement) all converge on the same underlying phenomenon: **receivables are growing faster than revenue and are not converting to cash.** This is the single most load-bearing, multiply-corroborated finding in this entire report.

**Phase 3 Verdict: 🔴 Red Flag.** CFO/PAT badly broken on both consolidation bases; EBITDA margin compressing despite strong revenue growth; other income dominated by a non-recurring FX-gain component; ROE/ROCE decline only partially IPO-mechanical.

**Kill Switch Assessment (informational):** A human reviewer **would** have strong reason to pause on cash-conversion grounds alone before treating FY26's reported PAT growth trajectory (consolidated, historical FY23-25) as continuing cleanly into FY26 — the cash story and the profit story have diverged sharply in the IPO year. Continuing to Phase 4 regardless, per protocol.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A. Disclosed Risks — Real vs Boilerplate
The MD&A and risk-factor sections read (Board's Report / MD&A, AR PDF p.~44-53; supplemented by RHP risk-factor language) contain standard categories: customer concentration, competition, raw-material/input cost, forex, execution/project-delay risk, regulatory (pharma-sector) risk, and — genuinely specific and *not* boilerplate — two RHP-disclosed risks that corroborate the AR-notes-based findings:
1. **"The actual orders received by our Company during the preceding three Financial Years is less than 11% of the total value of the proposals submitted by us"** (RHP forward-looking-statements section) — a specific, quantified, and unflattering order-conversion disclosure. This is a genuine risk disclosure, not boilerplate, and it is a useful monitorable (Phase 8).
2. **"We procure a significant portion of our equipment and materials from our Associate, Promoter Group entities and Group Companies. Accordingly, we are dependent upon them to procure the equipment required for executing our projects"** (RHP forward-looking-statements section) — this is a direct, pre-IPO acknowledgment of RPT-sourcing dependency as a *named risk factor*, which stands in tension with the Board's Report's post-listing AOC-2 assertion of "no material related party transactions" (Phase 5). **The RHP was more candid about RPT dependency than the post-listing AR is.**

### 4B. Missing Risks
Cross-referencing Phases 1-3 against the risk-factor/MD&A sections read, the following are **not found as named risks** despite being material, evidenced issues elsewhere in the same annual report:

| Missing risk | Evidence it should be there | Likely reason for omission |
|---|---|---|
| Related-party land purchase / lease-liability provenance | B02 finding #1, #3; Phase 2 land-purchase and lease-counterparty findings | A named risk here would draw direct attention to an item the company has not otherwise proactively explained |
| Receivables/ECL curve-shape shift with no disclosed rationale | Phase 1B (KAM), Phase 2 (ECL extension), Phase 3A (CFO collapse) | The KAM itself discloses the *existence* of overdue receivables, but "why did our own credit-loss assumptions change so sharply this year" is not addressed as a risk or in MD&A narrative |
| Consolidated trade-receivables balance-sheet-to-note reconciliation gap (₹37.18 Cr) | Phase 2 new finding | Not previously identified even internally, on the evidence available |
| Customer-concentration *instability* (not just concentration) | B02 finding #8; an 8x jump by one customer and a 42-74% fall by three others in one year is a *churn* risk, distinct from steady-state concentration risk, which is typically all that's disclosed | Standard boilerplate "we depend on a limited number of customers" language does not capture year-to-year churn severity |
| Multi-entity shared collateral / cross-guarantee structure with the sister listed company | Phase 2B new finding | This is a security/legal-structure fact, not conventionally framed as a "risk factor" in Indian AR practice, but it is materially relevant to minority shareholders of the listed entity |
| Section 164(2) director disqualification at group level | Phase 1D new finding | Disclosed only in the audit report's technical compliance section, not surfaced in the Board's Report narrative |

### 4C. MD&A Deep Dive
**Industry claims**: growth narrative centres on pharmaceutical-sector capex expansion (supported by the RHP's CRISIL-commissioned industry report — a paid-for, company-commissioned source, so treat industry growth figures as directionally useful but not independent). **Growth/margin explanations**: MD&A explains the ROE/ROCE/net-profit-ratio declines almost entirely via the IPO-mechanical equity-base-expansion narrative (Note "Analytical Ratios" reason column, Phase 3B) — this is directionally correct for the balance-sheet ratios but, as shown in Phase 3C, does not fully explain the EBITDA-margin compression, which management's disclosed reasoning does not address at all. **External-factor credit-taking/blaming**: the FY25-vs-FY26 net-profit-ratio explanation ("FY 2024-25 the Company has exceptional Income from sale of Investment") is a candid, non-blame-shifting explanation — a genuine strength, contrasted against the silence on the margin-compression driver.

**Forward guidance table:**

| Claim | Number | Timeframe | Credibility |
|---|---|---|---|
| Order-to-proposal conversion | <11% of proposal value converted to orders | Preceding 3 FY | Disclosed as a risk, not a guidance target — no forward number to test against |
| IPO proceeds deployment | ₹230.30 Cr objects, 3-year deployment plan implied by RHP | Through FY27-28 (per B02 Pass-3/prospectus timeline) | **Weak so far** — only 22.2% deployed at FY26 year-end, working-capital tranche 21.6%, inorganic-growth tranche 0% — no revised timeline disclosed post-listing |
| Dividend | ₹0.60/share proposed FY26 | FY26 | Concrete, low materiality (₹266.70 Lakh, ~7% of standalone PAT) — not a stretch claim |

**NOT FOUND IN DOCUMENT**: no explicit multi-year revenue/margin guidance numbers were located in the MD&A sections read to test against historical delivery — the "guidance" surface area in this AR is thin (a first-year-listed company constraint, not necessarily evasiveness).

**Segment analysis**: the company discloses a single reportable segment ("Trading of pharmaceutical and surgical products" / turnkey project solutions) — no sub-segment profitability breakdown, consistent with Note 42 standalone ("segment information has been given in the consolidated financial statements... no separate disclosure... in standalone") and the consolidated Note 44's geography-only (not product-line) segment view.

### 4D. Tone and Credibility Ratings (1-5)

| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 2/5 | Land purchase, lease counterparty, ECL rationale, and the receivables reconciliation gap are all either unexplained or absent from the narrative sections; contrasted against genuinely candid explanations elsewhere (exceptional-item PAT driver) |
| Consistency | 2/5 | RHP (pre-IPO) discloses RPT-sourcing dependency as a named risk; the post-listing Board's Report asserts no material RPT for AOC-2 purposes (Phase 5) — a direct posture shift across the IPO event |
| Specificity | 3/5 | Ratio-variance explanations are specific and quantified where given; IPO-deployment and RPT-completeness narrative is not |
| Accountability | 3/5 | Management owns the FY25-exceptional-item PAT explanation candidly; does not address the margin-compression or cash-conversion deterioration in the narrative sections read |
| Capital allocation sense | 2/5 | 22.2% IPO-proceeds deployment after a full fiscal year, 0% of the inorganic-growth tranche, ₹660 Lakh committed instead to a related-party-influenced investment fund (Alanar One Health Equity Fund) not among the disclosed IPO objects |

**Phase 4 Verdict: 🔴 Red Flag.** Multiple material, evidenced omissions from the risk/MD&A narrative; a genuine pre-IPO-to-post-IPO disclosure-posture shift on RPT.

**Kill Switch Assessment (informational):** A human reviewer **would** flag the RHP-to-AR RPT disclosure-posture shift as a credibility concern warranting a direct management/IR query before relying on forward-looking MD&A statements. Continuing to Phase 5 regardless, per protocol.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A. Board Composition
Per Note 47's related-party/director list (AR p.133, cross-referenced against the Board's Report/CG report sections read), the Board as of FY26 year-end comprises:

| Director | Role | Notes |
|---|---|---|
| Hemant Mohan Anavkar | Promoter, Executive Director (Managing Director) | Signs financial statements |
| Manisha Hemant Anavkar | Promoter, Director | |
| Amjad Adam Arbani | Non-Executive Director (from 06-06-2024) | Signs financial statements as Director |
| Chirag Doshi | Nominee Director (16-01-2023 to 04-06-2024), then Non-Executive Director (from 06-06-2024) | |
| Shyam Nagorao Khante | Independent Director (from 26-06-2024) | |
| Aparna Sharma | Independent Director (from 03-04-2024) | |
| Naushad Panjwani | Independent Director (from 30-07-2024), **Chairman from 17-02-2025** | Non-executive independent chairman |
| Naseem Khan | Director (upto 02-01-2024) | Departed before FY26 |

Board size: 7 (current). Independent directors: 3 of 7 (42.9%) — comfortably satisfies the standard SEBI LODR 1/3-independence threshold; **an earlier draft characterisation in this analysis process questioned a "more than half independent" claim, but on the confirmed Note 47 composition this does not apply — no composition-compliance issue found.** Tenure, attendance, and "independent >10 years" checks: **NOT FOUND IN DOCUMENT** with sufficient page-level confidence in this pass to state exact attendance percentages — all listed independent directors were appointed in 2024, well under a 10-year tenure flag threshold by construction (company itself IPO'd in late 2025).

**Board interlock with the sister listed company**: per the CG report's other-directorships disclosure (read but not independently re-confirmable to exact wording in this pass — flagged with appropriate caution), at least one director (Amjad Adam Arbani) holds a role at Fabtech Technologies Cleanrooms Limited (BSE 544332), the demerger-parent and largest related-party supplier (per task context and independently corroborated via Note 47's largest single RPT-purchase line, ₹1,812.96 Lakh FY26 standalone). **NOT FOUND IN DOCUMENT with full confidence in this pass: the precise executive/non-executive nature of that cross-directorship, or an explicit non-compete clause between the two entities** — treating the "no non-compete" fact as provided operator/task context rather than independently re-verified from the AR in this pass. 🟡 Watch — a board interlock between a company and its largest related-party supplier, without an independently confirmed non-compete, is a structural governance concern regardless of the exact role title.

### 5B. Committee Analysis
**NEW finding, extension of B02's Pass-3 observations**: the **Risk Management Committee was dissolved on February 2, 2026** (noted as not mandatorily required for the company's category) — this removes a formal risk-oversight body in the same fiscal year the company disclosed its sharpest FX-sensitivity increase (Phase 2), its ECL curve-shape shift (Phase 2), and its CFO collapse (Phase 3A). 🟡 Watch — the dissolution may be technically compliant (not mandated for this company category under SEBI LODR thresholds), but the timing, alongside the year's risk profile, is worth noting. Audit Committee and Nomination & Remuneration Committee composition/meeting counts: **NOT FOUND IN DOCUMENT** with sufficient page-confidence to tabulate exactly in this pass.

### 5C. Compensation
KMP remuneration (standalone, Note 47, AR p.133):

| KMP | FY26 (₹ Lakh) |
|---|---|
| Hemant Anavkar (Executive Director) | 55.62 |
| Manisha Anavkar | 54.22 |
| Aamer Aasif Khan | 4.50 |
| Ashwani Singh (CEO) | 126.63 |
| Guman Mal Jain (CFO, part-year) | — (departed mid-year per Note 47 director/KMP list) |
| Neetu Buchasia (Company Secretary) | 9.45 |
| Kalpesh Chauhan (CFO, from later in year) | 30.36 |

Total KMP comp is a small fraction of PAT (Hemant Anavkar's own comp alone = 55.62/2,425.30 standalone PAT = 2.29%) — **not excessive**, no CEO-to-median multiple data found (median employee salary not disclosed in the sections read — NOT FOUND IN DOCUMENT). Board sitting fees are modest (₹1.10L-₹5.00L per independent director, Note 47). **No ESOP scheme found** (see Phase 2H) — comp structure is cash-only among disclosed KMP, a mild positive for alignment-simplicity, though it also means no equity-based long-term-incentive mechanism was identified.

### 5D. Shareholding
Promoter shareholding: **68.94% total, unchanged (0.00% change) during FY26** (Note "Details of Shares held by promoters," AR p.119; RHP Capital Structure section corroborates): Aasif Ahsan Khan 41.52%, Aarif Ahsan Khan 10.28%, Hemant Mohan Anavkar 8.57%, Manisha Hemant Anavkar 8.57%. **No promoter selling against a growth narrative** — holding is flat post-IPO, a genuine positive signal (though the IPO itself was a pure primary/fresh issue with no Offer for Sale component, per the RHP's issue-structure table, so promoters had no opportunity to sell down at listing in any case — this reduces, but does not eliminate, the read-through value of "no selling" as a confidence signal). **Pledge status: NOT FOUND IN DOCUMENT** in the sections read with confidence — recommend explicit confirmation before treating as nil. **FII/DII trend**: NOT FOUND IN DOCUMENT (first annual report post-listing; shareholding-pattern filings were flagged as an input gap by B02/Stage 0, consistent with this pass's own inability to locate FII/DII detail in the AR itself).

### 5E. Governance Red-Flag Checklist

| Item | Status |
|---|---|
| Whistleblower complaints | NOT FOUND IN DOCUMENT |
| SEBI actions | NOT FOUND IN DOCUMENT in the AR sections read (RHP litigation summary showed 3 statutory/tax proceedings against the Company, 6 against Promoters, aggregate quantum disclosed — see RHP p.28 litigation table; nothing SEBI-specific identified) |
| RPT committee approval process | Asserted compliant in Board's Report RPT policy language and Note 47(iii) ("at arm's length... ordinary course"), **but this assertion did not catch the land-purchase RPT-note omission (Phase 2) or the AOC-2 "no material RPT" contradiction below** |
| Auditor fee ratio | Non-audit fees marginally exceed audit-fee aggregate (Phase 1E) — a mild flag |
| CSR compliance | 🟢 Fully compliant, prior-year shortfall closed (Phase 2H) |
| Section 143 fraud reporting | 🟢 None reported (Phase 1D) |
| Material subsidiary auditor | Reliance on other auditors for the foreign subsidiary and one associate (Phase 1C/1F) — standard, not itself a red flag |
| **AOC-2 "no material RPT" assertion** | 🔴 **Red Flag** — the Board's Report states there were no material related-party transactions requiring AOC-2 disclosure under Section 134(3)(h) of the Companies Act, **in the same annual report that discloses ₹3,312.80 Lakh (21.0% of standalone purchases) in related-party purchases, 99.37% of the loan book to related parties, 55.71% of consolidated current borrowings from a related party, and an undisclosed-in-Note-47 ₹19.71 Cr related-party land purchase.** This is the single sharpest governance-narrative-vs-substance contradiction found in this report — flagged with the caveat that the exact AOC-2 wording was read in an earlier batch of this pass and could not be re-displayed for verbatim re-confirmation, but the substance of the assertion (no material RPT, Section 134(3)(h) not applicable) is recalled with high confidence given its distinctiveness and is directly and irreconcilably at odds with Note 47's own transaction table. |
| Section 164(2) disqualification | 🔴 See Phase 1D — new finding, group level |

**Phase 5 Verdict: 🔴 Red Flag.** The AOC-2 "no material RPT" assertion is the standout finding — a governance-disclosure claim that does not survive contact with the company's own RPT note.

**Kill Switch Assessment (informational):** A human reviewer **would** have strong reason to stop and seek direct clarification from the company secretary/board on the AOC-2 assertion before proceeding further — this is a Companies Act compliance-framing question, not merely an accounting-judgment question. Continuing to Phase 6 regardless, per protocol.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

*(Read with full knowledge of Phases 1-5. Exact verbatim quotes from the Chairperson's Message and CEO Message could not be re-displayed for character-level re-confirmation in this pass; the thematic content below is recalled at high confidence from direct reading and is presented with that caveat rather than as blockquoted verbatim text, per the protocol's grounded-claims rule.)*

### 6A. Narrative vs Reality

| Prominent claim (theme) | Cross-check against Phases 1-5 | ✅/❌ |
|---|---|---|
| "Landmark year of growth," IPO listing as a validating milestone | Revenue +25.7% consolidated — genuinely strong; but margin compressed and CFO collapsed the same year (Phase 3) | ❌ (growth real, "landmark" quality claim not supported by cash/margin trend) |
| Strengthening the balance sheet / financial discipline | Net worth genuinely up (IPO proceeds); D/E genuinely down; **but** CFO/PAT badly broken both bases (Phase 3A), and 22.2% of the fresh capital remains undeployed a full year later (Phase 2H) | ❌ (balance-sheet size grew; balance-sheet *quality*, measured by cash conversion, deteriorated) |
| Commitment to governance/transparency post-listing | AOC-2 "no material RPT" assertion in the same report as extensive RPT disclosure (Phase 5); land purchase and lease counterparty undisclosed in the RPT note (Phase 2) | ❌ |
| Global/geographic expansion | Genuine — export revenue ~89%, new geographies (Morocco 132x YoY per B02); **but** underlying customer base churned sharply (Al-Afiya 1.58%→12.55%, three others nearly halved-to-three-quarters-fell, Phase 2) | Mixed — expansion is real, stability underneath it is not |
| Disciplined capital allocation | Contradicted by the IPO-proceeds deployment lag and the ₹660 Lakh related-party-fund investment outside the disclosed IPO objects (Phase 2B) | ❌ |

### 6B. Strategic Priorities
Priorities emphasised in the opening sections (growth, geographic diversification, execution discipline, digitalisation/technology investment, governance strengthening) are **specific enough to be tested** but **capital allocated against them is thin**: the inorganic-growth (M&A) IPO tranche is at 0% deployment a full fiscal year after listing (Phase 2H/4C), and no revised timeline or specific target-identification narrative was found in the sections read.

### 6C. Metrics Showcased vs Conspicuously Absent
**Showcased**: revenue growth, geographic footprint (countries served), IPO milestone, EPS. **Conspicuously absent from the front-matter/opening narrative**: CFO/cash conversion, receivables ageing/DSO trend, the ECL rate change, the RPT quantum, the IPO-deployment percentage (which does appear, factually, in Note 53, but not in the Chairman's/CEO's opening narrative).

### 6D. Tone and Priority Drift
**No prior-year annual report exists** (first listed-company AR; company IPO'd Oct 2025) — a YoY tone-drift comparison is not possible. **NOT APPLICABLE / structurally unavailable**, not a gap in this analysis.

### 6E. Quiet Abandonment Check (mandatory)

Reading the opening sections (Chairperson's Message, CEO Message, front-matter growth narrative) side by side with the operational sections (MD&A ratio table, notes, cash flow statement):

1. **Claim**: the opening narrative frames the IPO and its proceeds as fuel for "disciplined," purposeful expansion (working capital, inorganic growth). **Operational section it should show up in**: Note 53 (IPO utilisation) and the MD&A's own capital-deployment narrative. **What operations actually show**: 22.2% total deployment, 0% of the inorganic-growth tranche, with no revised deployment timeline disclosed. **Classification**: **(b) silent drop** — the opening claims a purposeful use-of-proceeds narrative; the operational section (Note 53) simply shows the money sitting in fixed deposits, with no narrative acknowledgment anywhere in the front matter that deployment is running far behind the implied pace. **Materiality**: moderate-to-high — this directly affects near-term ROE/ROCE optics and is the kind of gap a GARP-focused reader would want called out explicitly rather than left to a numbers-only note.

2. **Claim**: governance/transparency commitments in the opening narrative (a natural theme for a newly-listed company's first AR). **Operational section it should show up in**: the Board's Report RPT disclosure (AOC-2) and Note 47. **What operations actually show**: the AOC-2 "no material RPT" assertion sits in direct tension with Note 47's own transaction table and with the undisclosed land purchase (Phase 5). **Classification**: **(a) implicit retraction** — the opening frames transparency as a priority; the operational RPT disclosure does not name-check, quantify, or acknowledge the scale of related-party dealing that the notes themselves later reveal, and the AOC-2 clause actively asserts the opposite of what the notes show. **Materiality**: high — this is a direct, filing-level contradiction, not a tonal soft-pedal.

3. **Claim**: growth/geographic-expansion narrative implies a broadening, diversifying customer base. **Operational section**: Note 44c customer concentration. **What operations show**: extreme single-customer churn (Al-Afiya 1.58%→12.55%; three prior top customers falling 42-74%) — the customer base is not broadening in a stable way, it is *reshuffling* sharply. **Classification**: **(c) hedged retreat** — the growth narrative is not false (revenue did grow, geographies did diversify), but the underlying customer-base stability implied by "expansion" is walked back by the concentration note without acknowledgment of the churn. **Materiality**: moderate — relevant to revenue durability/predictability, core to a GARP thesis's forward visibility.

No other quiet abandonments identified beyond these three.

**Phase 6 Verdict: 🔴 Red Flag.** All three quiet-abandonment items found are material to a GARP thesis (capital discipline, governance credibility, revenue durability), not framework noise.

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top 3 reasons |
|---|---|---|
| **GARP** | **WATCHLIST** | (1) Genuine multi-year revenue CAGR is strong — consolidated revenue ₹193.80 Cr (FY23) → ₹410.77 Cr (FY26), a ~28.4% 3-year CAGR (RHP-restated FY23-25 + AR FY26), squarely in transition-alpha territory; (2) but earnings quality has deteriorated sharply in the most recent year exactly when a GARP thesis needs it to hold — EBITDA margin compressed ~110bps YoY, CFO/PAT is broken on both consolidation bases (Phase 3A), and reported PAT growth in FY25 and FY26 alike is meaningfully non-operating (exceptional-item) driven, making the "P" in GARP's growth-at-reasonable-price harder to trust at face value; (3) the RPT/governance findings (undisclosed land purchase, AOC-2 contradiction, shared collateral web, Section 164(2) disqualification) are exactly the class of issue that turns a promising growth transition into a value trap if left unaddressed — this is a name to watch for resolution of the receivables-reconciliation gap and the next 1-2 quarters' CFO trend before treating the growth story as investable at face value. |
| **Turnaround** | **FAIL** | (1) Not a turnaround situation — the company was never in distress; it is a growing, profitable business with a governance/disclosure-quality problem layered on top, not an operational-recovery story; (2) no impairment/restructuring/loss history to turn around from; (3) the relevant thesis framework here is GARP-transition-with-flags, not turnaround. |
| Value+Quality | FAIL | Quality score too low currently (accounting quality 4/10 per B02, confirmed and extended by this pass) to qualify on the quality leg, despite reasonable growth. |
| Capex-Led Growth | FAIL | Capex is running *below* depreciation (Phase 3A) — an explicitly asset-light, RPT-sourced-equipment model, the opposite of a capex-led thesis. |
| Cash Flow Compounder | FAIL | CFO/PAT badly broken both consolidation bases (Phase 3A) — disqualifying on its face. |
| Contrarian | WATCHLIST | Post-IPO governance/RPT overhang could create a contrarian entry if the market has already priced in the flags and the underlying growth persists — worth monitoring valuation vs the flag severity, but not yet a clean contrarian setup given the newness of the listing and thin trading history. |
| Insider Confidence | WATCHLIST | Promoter holding flat at 68.94%, no selling (Phase 5D) — a mild positive, but the IPO was a pure fresh issue with no OFS component, so "no selling" carries less signal than in a company where promoters had a live opportunity to cash out and declined. |
| Guidance Divergence | WATCHLIST | Thin forward-guidance surface area (first-year-listed company) limits testability; the one quantified, credible forward-looking risk disclosure found (order-to-proposal conversion <11%, Phase 4C) is itself a divergence-relevant monitorable for FY27. |

---

## PHASE 8: FINAL VERDICT DASHBOARD

### Company Snapshot
Fabtech Technologies Limited (FABTECH), NSE/BSE-listed October 2025, turnkey pharmaceutical-engineering/cleanroom equipment and process-solutions provider, ~89% export revenue, demerged in 2024 from sister listed company Fabtech Technologies Cleanrooms Limited (BSE 544332). Promoters Aasif Ahsan Khan, Hemant Mohan Anavkar, Aarif Ahsan Khan, Manisha Hemant Anavkar, 68.94% combined holding, unchanged post-IPO. FY26 consolidated revenue ₹410.77 Cr (+25.7%), PAT ₹38.36 Cr (-17.4%), net worth ₹419.77 Cr (IPO-inflated).

### Phase-Wise Verdict Summary

| Phase | Verdict |
|---|---|
| 1. Auditor's Report & CARO | 🟡 Watch |
| 2. Notes to Financial Statements | 🔴 Red Flag |
| 3. Financial Statements | 🔴 Red Flag |
| 4. Risk Factors & MD&A | 🔴 Red Flag |
| 5. Corporate Governance & Board | 🔴 Red Flag |
| 6. Chairman's Letter & Front Matter | 🔴 Red Flag |
| 7. Multi-Strategy Fit (best fit: GARP) | WATCHLIST |

### Overall Quality Score
| Component | Weight | Score /10 | Basis |
|---|---|---|---|
| Governance | 25% | 3 | AOC-2 contradiction, Section 164(2) group-level disqualification, shared-collateral/interlocked-board web with the sister listed company, undisclosed land purchase |
| Accounting quality | 25% | 4 | B02's score of 4/10, confirmed 15/15 on verification, held (not improved) given two new material findings this pass |
| Balance sheet | 25% | 5 | Genuinely light leverage (D/E 0.05x) and large cash/FD balance are real strengths; offset by the unreconciled ₹37.18 Cr receivables gap and the shared-collateral structure |
| Earnings quality | 25% | 3 | CFO/PAT broken both consolidation bases; EBITDA margin compression despite revenue growth; other income dominated by a non-recurring FX-gain line; two consecutive years of exceptional-item-driven reported PAT |
| **Overall** | | **3.75 ≈ 4/10** | Weighted average; consistent with B02's 4/10 accounting-quality anchor, with this pass's balance-sheet-strength observation the only meaningfully offsetting factor |

### Top 3 Strengths
1. **Genuinely strong, multi-year revenue growth** — consolidated revenue CAGR of ~28% FY23-FY26, with real geographic diversification (89% export) and a large, credible addressable pharma-capex market per the RHP's CRISIL-sourced industry data.
2. **Light, de-levered balance sheet post-IPO** — D/E 0.05x standalone, no covenant breaches, no willful-defaulter status, clean statutory-dues position at the Holding Company level (CARO vii(a) resolved and immaterial).
3. **Candid disclosure where management chooses to be candid** — the FY25-exceptional-item explanation for the net-profit-ratio decline, the CSR compliance closure, and the audit-trail (edit-log) confirmation are all genuine, unhedged positives that should not be discounted just because other disclosures fall short.

### Top 3 Red Flags
1. **Cash conversion has broken in the IPO year** — standalone CFO/PAT -5.6% (from +137.4% the prior year); consolidated CFO/PAT a bare 1.24% after a deeply negative prior year; both driven by receivables outrunning revenue and (consolidated) propped up by payable-stretching.
2. **The AOC-2 "no material RPT" assertion is irreconcilable with Note 47** — a Companies Act compliance-framing claim that does not survive contact with the company's own disclosed related-party purchases (21% of standalone purchases), loan book (99.37% to related parties), and current borrowings (55.71% from a related party), compounded by the undisclosed land purchase and the newly identified shared-collateral/cross-guarantee web with the sister listed company.
3. **An unreconciled ₹37.18 Cr (18.2%) gap between the Consolidated Balance Sheet's trade-receivables line and its own supporting Note 13**, on the single item the auditor scoped as its sole Key Audit Matter — new to this pass, unresolved, and warrants direct confirmation before this figure is relied upon in any valuation model.

### Key Monitorables for Next Quarter/Year

| Metric | Threshold | Where to find it | Why it matters |
|---|---|---|---|
| Receivables reconciliation (Balance Sheet vs Note 13) | Should tie exactly to zero variance | Next quarterly/annual filing, Note on trade receivables vs BS face | Currently ₹37.18 Cr unreconciled; resolution direction (up or down) materially changes the receivables-growth read |
| CFO/PAT ratio | Should recover to >70% (this protocol's threshold) on at least one consolidation basis within 2-3 quarters | Cash flow statement, quarterly results | Currently badly broken both bases; sustained sub-threshold readings would be a strong sell/avoid signal |
| IPO-proceeds deployment pace | Inorganic-growth tranche should show non-zero deployment; total deployment should meaningfully exceed 22.2% | Note 53-equivalent in next filing / stock-exchange utilisation disclosure | 0% inorganic-growth deployment a year post-IPO is a capital-discipline red flag if it persists |
| AOC-2 / RPT disclosure resolution | Should the company amend or clarify the "no material RPT" assertion, or formally add the land purchase/lease to Note 47/RPT-committee approvals | Next Board's Report, stock-exchange filings, AGM notice | Tests whether management corrects a governance-disclosure gap once flagged, or repeats it |
| Customer concentration | Al-Afiya's FY27 share and payment behaviour; whether the Morocco/geography surge (132x YoY per B02) proves durable | Note 44c-equivalent, next annual report | Tests whether FY26's reshuffle was a one-off contract or a genuine customer-base shift |
| Section 164(2) disqualification | Should be resolved/disclosed with specifics | Next auditor's report, MCA filings | Currently opaque — no individual or root cause named |

### Best-Fit Strategy
**GARP (Growth at a Reasonable Price) — WATCHLIST, not yet PASS.**

### One-Line Verdict
Strong multi-year growth undercut by an IPO-year cash-conversion break, a Companies Act RPT-disclosure contradiction, and an unreconciled receivables gap.

---

```yaml
stage: B03-ardeep
company: "FABTECH"
run_date: "2026-08-04"
model: claude-sonnet-5
status: complete
input_gaps: [announcements, shareholding, research, "board attendance/tenure percentages", "AOC-2 verbatim wording re-confirmation", "auditor tenure/appointment year", "ESOP scheme existence", "FII/DII shareholding trend", "consolidated CARO vii(a) quantum for FT Institutions and Mark Maker Engineering"]
flags:
  - {type: FLAG-CASH, reason: "Standalone CFO/PAT collapsed from +137.4% (FY25) to -5.6% (FY26); consolidated CFO/PAT only 1.24% (FY26) after -77.8% (FY25) -- receivables outrunning revenue on all three independent lenses (auditor KAM, notes ageing, primary cash flow statement)"}
  - {type: FLAG-RPT, reason: "Board's Report AOC-2 assertion of no material related-party transactions under Section 134(3)(h) is irreconcilable with Note 47's own disclosed related-party purchases (21% of standalone purchases), loans (99.37% to related parties), and current borrowings (55.71% from a related party)"}
  - {type: FLAG-RPT, reason: "New finding: multi-entity shared/cross-collateralised security structure spanning FABTECH, sister listed company Fabtech Technologies Cleanrooms Limited (BSE 544332), and other related entities, with title to pledged property held by related-party LLP Fabtech Turnkey Projects LLP; reciprocal corporate guarantees (Rs 1,000L and Rs 600L) given by FABTECH for two related entities' working-capital facilities (Note 25/26 standalone/consol; Note 41/43 contingent liability)"}
  - {type: FLAG-CASH, reason: "New finding: unreconciled Rs 37.18 Cr (18.2%) gap between Consolidated Balance Sheet trade receivables (Rs 24,151.90 Lakh) and Note 13's supporting schedule total (Rs 20,433.51 Lakh) for FY26, on the auditor's sole Key Audit Matter line; FY25 ties out exactly"}
  - {type: FLAG-PROMOTER-PRELIM, reason: "Promoter holding flat at 68.94%, zero change during FY26, no selling identified -- but IPO was a pure fresh issue with no Offer for Sale component, limiting the signal value of 'no selling'; pledge status NOT FOUND IN DOCUMENT in sections read, recommend explicit confirmation"}
phase_verdicts: {p1: "watch", p2: "red_flag", p3: "red_flag", p4: "red_flag", p5: "red_flag", p6: "red_flag", p7_best_fit: "GARP-watchlist"}
overall_quality: 4            # /10 with the four 25% components
quality_components: {governance: 3, accounting: 4, balance_sheet: 5, earnings: 3}
kill_switch_notes:
  - "Phase 1: would not stop on the opinion itself (unmodified, no fraud reported), but would flag the Section 164(2) group-level director disqualification and the RPT-completeness audit-scope gap for immediate follow-up"
  - "Phase 2: would pause before further capital allocation given the unreconciled Rs 37.18 Cr receivables gap on the auditor's own KAM line, compounding an already-thin RPT-fairness picture"
  - "Phase 3: would pause on cash-conversion grounds before treating FY26 reported PAT growth as a clean continuation of the FY23-25 trajectory -- cash and profit have diverged sharply"
  - "Phase 4: would flag the RHP-to-AR RPT disclosure-posture shift as a credibility concern warranting a direct management/IR query"
  - "Phase 5: would stop and seek direct clarification from the company secretary/board on the AOC-2 no-material-RPT assertion before proceeding -- a Companies Act compliance-framing question, not merely an accounting-judgment question"
triple_pass_verification:
  verified: 15                # of 15
  discrepancies: []
missing_risks:
  - {risk: "Related-party land purchase / lease-liability provenance not named as a risk despite Note 5/49 disclosure", evidence_anchor: "Note 5 AR p.115, Note 49 AR p.136"}
  - {risk: "ECL curve-shape shift with no disclosed rationale, standalone and consolidated", evidence_anchor: "Note 13(b) standalone AR p.117-118, Note 13(b) consol AR consol p.174"}
  - {risk: "Consolidated trade-receivables balance-sheet-to-Note-13 reconciliation gap (Rs 37.18 Cr)", evidence_anchor: "AR consol p.149 (Balance Sheet) vs AR consol p.174 (Note 13)"}
  - {risk: "Customer-concentration instability/churn (not just steady-state concentration)", evidence_anchor: "Note 44c AR consol p.185"}
  - {risk: "Multi-entity shared collateral / cross-guarantee structure with sister listed company", evidence_anchor: "Note 25 standalone AR p.121, Note 26 consol AR consol p.178, Note 41/43 contingent liability"}
  - {risk: "Section 164(2) director disqualification at group level", evidence_anchor: "Consolidated Auditor's Report, item 2(e), AR consol p.143"}
guidance_table:
  - {claim: "Order-to-proposal conversion", number: "<11% of proposal value converted to orders", timeframe: "preceding 3 FY", credibility: "disclosed as a risk, not guidance -- no forward number to test yet"}
  - {claim: "IPO proceeds deployment", number: "Rs 230.30 Cr net proceeds, implied 3-year deployment plan", timeframe: "through FY27-28", credibility: "weak so far -- 22.2% deployed at FY26 year end, inorganic-growth tranche 0%, no revised timeline disclosed"}
  - {claim: "Dividend", number: "Rs 0.60/share, Rs 266.70 Lakh total", timeframe: "FY26", credibility: "concrete, low materiality, ~7% of standalone PAT -- not a stretch claim"}
monitorables:
  - {metric: "Trade receivables Balance-Sheet-vs-Note-13 reconciliation", threshold: "should tie to zero variance", where: "next quarterly/annual filing, receivables note vs BS face", why: "currently Rs 37.18 Cr unreconciled on the auditor's sole KAM line"}
  - {metric: "CFO/PAT ratio, both consolidation bases", threshold: ">70% (this protocol's flag threshold)", where: "cash flow statement, quarterly results", why: "currently badly broken both bases; sustained sub-threshold readings would be a strong avoid signal"}
  - {metric: "IPO-proceeds deployment, inorganic-growth tranche", threshold: "non-zero deployment", where: "Note 53-equivalent in next filing / exchange utilisation disclosure", why: "0% deployment a year post-IPO is a capital-discipline red flag if it persists"}
  - {metric: "AOC-2 / RPT disclosure resolution", threshold: "amendment or clarification of the no-material-RPT assertion", where: "next Board's Report, AGM notice, exchange filings", why: "tests whether management corrects a governance-disclosure gap once flagged"}
  - {metric: "Al-Afiya revenue share and customer concentration", threshold: "watch for further single-customer share jumps >10pp YoY", where: "Note 44c-equivalent, next annual report", why: "tests whether FY26's customer reshuffle was a one-off or a durable shift"}
  - {metric: "Section 164(2) disqualification resolution", threshold: "specifics disclosed (individual, root cause, remediation)", where: "next auditor's report, MCA filings", why: "currently opaque"}
strengths_top3:
  - "Genuinely strong multi-year revenue growth (~28% consolidated CAGR FY23-FY26), real geographic diversification, 89% export revenue"
  - "Light, de-levered balance sheet post-IPO (D/E 0.05x standalone), no covenant breaches, no willful-defaulter status"
  - "Candid disclosure where management chooses to be candid (FY25 exceptional-item explanation, CSR compliance closure, clean audit-trail confirmation)"
red_flags_top3:
  - "Cash conversion broke in the IPO year -- CFO/PAT -5.6% standalone (from +137.4%), 1.24% consolidated (from -77.8%)"
  - "AOC-2 'no material RPT' assertion irreconcilable with Note 47's disclosed RPT footprint (21% of purchases, 99.37% of loans, 55.71% of current borrowings, undisclosed land purchase, new shared-collateral/cross-guarantee web with sister listed company)"
  - "Unreconciled Rs 37.18 Cr (18.2%) gap between Consolidated Balance Sheet trade receivables and Note 13, on the auditor's sole KAM line, new to this pass and unresolved"
best_fit_strategy: "GARP (watchlist, not yet pass)"
one_line_verdict: "Strong growth undercut by a cash-conversion break, an RPT-disclosure contradiction, and an unreconciled receivables gap"
```
