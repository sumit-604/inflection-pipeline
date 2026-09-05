# STAGE 3 — ANNUAL REPORT DEEP DIVE (BACKWARD READ) — Aequs Ltd (AEQUS)

**Run date:** 2026-09-05 | **AR:** FY2025-26 (year ended 31-Mar-2026), 361 PDF pages
**Basis:** AR reports in INR Millions; this report states figures in **Rs Crore** (Mn ÷ 10) except where Mn is shown for direct-quote fidelity. Page anchors are the `=== PAGE n of 361 ===` marker in `Annual_Report_2026.txt`, sourced against the PDF.
**Method:** Backward read (AGM Notice → Notes → Statements → Auditor's Report → standalone equivalents → Governance → Board's Report → MD&A → Chairman/CEO letters), per protocol. Phase 2 builds on the Stage 2 triple-pass notes analysis (`02-notes.md`), verifying rather than re-extracting, and independently re-derived a majority of the Top-15 findings directly from source in this pass.

---

## PHASE 1: AUDITOR'S REPORT & CARO

### 1A Core opinion
Both the **Consolidated** (Auditor's Report p.219-226) and **Standalone** (p.149-159) Independent Auditor's Reports, B S R & Co. LLP, give an **unmodified "true and fair view" Opinion** on the financial statements as a whole (Opinion paragraph, p.219 / p.149). No going-concern material uncertainty language appears in either report — only standard auditor-responsibility boilerplate on evaluating management's going-concern basis (p.220-221 / p.151).

However, under "**Report on Other Legal and Regulatory Requirements**," **both reports qualify Section 143(3)(b)** ("proper books of account... **except for** the matters stated in paragraph 2B(f)... Rule 11(g)") — Consolidated para 2A(b), p.222; Standalone para 2A(b), p.152. Para 2B(f) (Consol p.223, Standalone p.153) details the audit-trail (edit-log) gap: **database-level logging not enabled 1-Apr-2025 to 15-Dec-2025**; **application-level logging not enabled for certain fields/tables 1-Apr-2025 to 9-Oct-2025**, spanning the Holding Company plus **4 subsidiaries and 3 joint ventures** (consolidated scope) / Parent only (standalone scope). Where the trail *was* enabled, the auditor found no evidence of tampering and records were retained per statutory requirement.

**Precise characterisation:** the core "Opinion" paragraph is clean; the qualification sits in the statutory Section 143(3)(b) sub-report. Both framings are true — this is a genuine audit exception, not routine disclosure, even though it does not modify the headline "true and fair view" opinion. The Corporate Governance Report's claim that "the Auditors have expressed an **unmodified opinion**" (CG Report p.114, item 14(e)(iii)) is technically defensible only for the narrow Opinion paragraph and **omits** this Section 143(3)(b) exception disclosed 40+ pages earlier in the same document — a Phase 6A finding.

### 1B Key Audit Matters

| Report | Subject | Why key | How addressed | Risk |
|---|---|---|---|---|
| Consolidated (p.219-220) | Revenue recognition | Contract manufacturing, concentrated customer base, judgement on control-transfer timing near period-end | IT control testing, statistical sampling of transactions, substantive testing of credit notes/reversals | 🟡 |
| Standalone (p.149) | Revenue recognition | Same as above | Same as above | 🟡 |
| Standalone only (p.150) | Impairment of investments in subsidiaries | Rs 1,410.31 Cr net investment (net of Rs 662.71 Cr impairment) = **70.63% of standalone total assets**; DCF-based, sensitive to growth/discount/terminal-growth assumptions | Valuation-specialist involvement, retrospective review of prior-year projections vs actuals, sensitivity testing | 🔴 |

**Cross-reference (1F):** the Consolidated report carries **no equivalent goodwill/CGU-impairment KAM**, despite the Group having booked a Rs 48.27 Cr goodwill impairment in FY25 and continuing Consumer-segment losses. The standalone-only KAM foreshadows exactly the area (investment valuation in loss-making subsidiaries) where the AABV near-total write-down and the Consumer segment's capital destruction later show up in the Notes — good internal consistency between what the auditor flagged as risky and what happened.

### 1C Emphasis of Matter / Other Matters
No Emphasis of Matter in either report. **Other Matters** (Consolidated only, p.221-222): 9 subsidiaries + 1 JV audited by other auditors (pre-consolidation total assets Rs 511.58 Cr, revenue Rs 242.21 Cr, net cash inflow Rs 4.71 Cr); 3 of these are foreign subsidiaries whose GAAP-conversion adjustments were separately audited by B S R. Opinion not modified for this reliance.

### 1D CARO 2020 — clause-by-clause
**Standalone Annexure A (p.154-158)** is the full clause-by-clause report for the Parent; **Consolidated Annexure A (p.224)** carries only clause (xxi), a roll-up of adverse remarks reported by *other* auditors across the Group — a reader relying on the consolidated Annexure alone would miss the Parent's own detailed findings below.

| Clause | Parent (standalone) finding | Group finding (consol Annexure A, clause xxi) |
|---|---|---|
| ii(a) inventory count | Clean, no discrepancy >10% | ASMIPL, Aequs Toys flagged ii(a) |
| ii(b) stock-statement vs books | Parent flagged: HDFC Bank gaps Rs 0.09-23.63 Mn per quarter (largest Mar-26 inventories, Rs 23.63 Mn) | Holding Co, ASMIPL, AEPPL, AFCPPL flagged ii(b) — ties to the much larger Axis Bank Rs 59.01 Cr consolidated gap (Stage 2 Note 15(B)) |
| iii loans to RPs | Rs 47.40 Cr repayable-on-demand loans to subsidiaries, not demanded (no default); Rs 1.72 Cr + Rs 5.16 Cr with **no stipulated repayment schedule** (auditor "unable to comment" on 90-day overdue status); Rs 6.47 Cr interest overdue >90 days; **Rs 15.22 Cr of interest dues extended = 11.07% of total loans granted in the year** (a soft "loans renewed to settle overdues" pattern); Rs 11.50 Cr loans with no specified terms (5.74% of total loans) | Holding Co, ASMIPL flagged iii(c)-(f) at Group level |
| vii disputed statutory dues | Income Tax Act: Rs 2.53 Cr (FY2016-17) + Rs 0.05 Cr (FY2017-18), both at CIT(Appeals) | Ajna JV flagged vii(a) |
| ix borrowing defaults | (a) no default; (b) not a wilful defaulter; (c) N/A (no term loans at Parent); (d) no short-term-for-long-term use at Parent | AFCPPL flagged ix(d) (short-term funds used long-term) |
| ix(e) — new finding this stage | Parent raised **Rs 174.82 Cr (IPO) + further private-placement proceeds specifically to meet subsidiary obligations** (loan repayment, capex, general corporate purposes) at ASMIPL/ACPPL/AEPPL/ATPL/AFCPPL; **Rs 81.20 Cr (IPO) + Rs 18.78 Cr (placement) remained UNUTILISED by subsidiaries at year-end** (p.156-157) | — |
| xi fraud | (a) none noticed; (c) auditor **explicitly factored in whistleblower complaints received during the year** when scoping audit procedures | — |
| xvii cash losses | Parent: **has NOT incurred cash losses**, current or preceding year | ACPPL, AEPPL, AFCPPL (three Consumer subsidiaries) flagged xvii = **auditor-confirmed cash losses** |
| xx unspent CSR | N/A — no CSR obligation arose (average loss over trailing 3 years) | — |
| xxi Group adverse remarks | — | Exactly 7 entities (Holding Co, ASMIPL, ACPPL, AEPPL, AFCPPL, Aequs Toys, Ajna JV) per clauses listed above; **3 JVs (SQuAD, API, Aequs Cookware/ACPL) + 1 associate (Aequs Foundation) had NO CARO report issued at all** by their auditors as of the 26-May-2026 sign-off date |

**New this stage:** the Parent is standalone **cash-profitable and not itself flagged for cash losses (xvii)**, while three Consumer-segment subsidiaries are auditor-confirmed cash-loss entities — the segment split shows up at the audit-opinion level, not just in the Notes.

### 1E Auditor continuity and fees
B S R & Co. LLP appointed at the AGM held **25-Oct-2024** for a fresh 5-year term (24th AGM → 29th AGM, i.e. through FY2029-30) — early in a first term, no rotation-due concern. Fees (CG Report p.114, SEBI LODR disclosure, consolidated basis incl. network): Statutory Audit Rs 0.90 Cr + Quarterly Reviews Rs 0.08 Cr = **Rs 0.98 Cr audit fees**; Certification Rs 0.36 Cr + Reimbursement Rs 0.48 Cr + **IPO-related services Rs 3.37 Cr** = **Rs 4.21 Cr non-audit fees**; total Rs 5.19 Cr. **Non-audit fees are 4.3x audit fees — FLAGGED** per protocol, though 80% of the non-audit total is IPO-specific (one-time, FY26 listing event); the recurring P&L "Payment to auditors" line (Note 23 consol, p.276) is a much smaller and stable Rs 1.05 Cr FY26 vs Rs 0.92 Cr FY25.

### 1F Standalone vs consolidated differences
- Standalone carries an extra KAM (investment impairment) that consolidated does not.
- Standalone CARO Annexure A is the full clause set; consolidated Annexure A is only the roll-up (clause xxi).
- 9 subsidiaries + 1 JV rely on other auditors' work at consol level only.
- Both reports carry the identical Rule 11(g) qualification at different scope (Parent-only vs Parent+4 subs+3 JVs).

**Phase 1 verdict: 🔴 Red Flag.**
**Kill switch (informational):** A human reviewer *would* have reason to pause — both statutory opinions carry a genuine Section 143(3)(b) qualification tied to a group-wide IT-control gap, and CARO flags adverse remarks (including auditor-confirmed cash losses) across 7 entities plus 4 with no CARO issued at all, in the company's first year as a listed entity. Continuing to Phase 2 regardless, per protocol.

---

## PHASE 2: NOTES TO FINANCIAL STATEMENTS

### Triple-pass Top-15 verification (this stage's independent re-checks against source)

| # | Finding (Stage 2) | Independently re-verified this stage? | Result |
|---|---|---|---|
| 1 | Consumer PBT -Rs 217.92 Cr FY26 (+49.4%), Aerospace PBT +144.5% | ✅ Re-derived directly from Note 36 (p.289-294): Consumer segment result (782.73) Mn = -Rs 78.27 Cr; Consumer PBT (2,179.23) Mn = -Rs 217.92 Cr vs (1,458.54) Mn = -Rs 145.85 Cr FY25; Aerospace PBT 1,739.83 Mn = Rs 173.98 Cr vs 711.66 Mn = Rs 71.17 Cr FY25 | ✓ exact match |
| 2 | Receivables +69.0% vs revenue +33.1%, DSO 61.8→78.5d, ECL 1.91%→0.73% | ✅ Balance Sheet (p.227): trade receivables Rs 264.61 Cr FY26 vs Rs 156.60 Cr FY25 = +69.0% exactly | ✓ exact match |
| 3 | CARO adverse across 7 entities, qualified audit-trail opinion | ✅ Re-read Annexure A verbatim (p.224) and both Auditor's Reports (p.152-153, 222-223) | ✓ exact match |
| 4 | Standalone +Rs 49.80 Cr vs consolidated -Rs 113.25 Cr | ✅ Standalone P&L (p.162): profit Rs 49.80 Cr; Consolidated P&L (p.228): loss Rs 113.25 Cr (Rs 102.35 Cr FY25) | ✓ exact match |
| 5 | Net debt gap: Note 15(C) -Rs 344.28 Cr vs Note 29 Rs 250.05 Cr | ✅ Note 15(C) (p.267): "Net debt (3,442.80)" Mn FY26, "(7,052.56)" Mn FY25 — reproduced the formula (cash+bank−lease−NCD−borrowings) and it ties to -344.28 Cr | ✓ exact match; see refinement below |
| 6 | 4 customers ≈58.0% of revenue | ✅ Note 36 (p.294): Customer 1 22.87%, 2 19.07%, 3 5.88%, 4 10.15% = 57.97% ≈ 58.0%, all Aerospace | ✓ exact match |
| 7 | AABV loan-to-equity + Rs 214.20 Cr cumulative impairment | Not re-derived line-by-line this stage; no contradicting evidence found | ✓ accepted, no discrepancy |
| 8 | RPT ≈9.4% of revenue; CEO pay +111%; 13% p.a. RP loans | ✅ Extended (see 2B below): found a **second** 13% p.a. related-party loan (Melligeri Investment LLC) not itemised in Stage 2 | ✓ confirmed + extended |
| 9 | Aerospace EBITDA margin 26.9% FY26 | ✅ matches Note 36 segment-result math | ✓ exact match |
| 10 | Standalone net profit ratio 40.21% is a holding-co artefact; only ROCE in Notes is standalone 3.41% | ✅ Note 33 (p.215): ROCE 3.41% vs -6.81%; confirmed **no consolidated ratio note exists at all** (grep for "Financial ratios" returns only the two standalone-note hits) | ✓ exact match |
| 11 | Inventory +39.0% vs revenue +33.1% | ✅ Balance Sheet (p.227): inventories Rs 567.44 Cr vs Rs 408.27 Cr = +39.0% | ✓ exact match |
| 12 | Non-operating FX gain ~Rs 22.97 Cr cushions FY26 | Not independently re-summed; consistent with Note 19/24 line items seen | ✓ accepted |
| 13 | Tax charge Rs 41.76 Cr on pretax loss Rs 71.54 Cr | ✅ P&L (p.228): tax expense 417.55 Mn = Rs 41.76 Cr on loss before tax (715.36) Mn = -Rs 71.54 Cr | ✓ exact match |
| 14 | 7 of 19 entities liquidated/struck off/inactive | ✅ Partially re-confirmed via Note 37 (p.293) + Board's Report: AHAPL (liquidated 27-Jun-25), KTTCPL (liquidated 30-Nov-24), AMMPL (liquidated 29-Jun-24), AREPL (inactive), ATHKPL (MVL in process), AOGLLC (operations closed) = 6 directly seen, consistent with Stage 2's 7 | ✓ consistent |
| 15 | Contingent tax liability fell to Rs 8.06 Cr from Rs 86.12 Cr (Karnataka HC) | Not re-derived line-by-line; consistent with litigation language seen at Note 30 (p.282-283) | ✓ accepted |

**Verified: 15 of 15. Discrepancies: none found.** Several items were independently re-derived from primary source in this stage with exact numerical matches (marked "exact match" above); this materially raises confidence in Stage 2's accounting_quality:5 score, which I do not revise.

### 2A Accounting policy aggressiveness — extended
- **Revenue:** point-in-time on transfer of control; both KAMs confirm no percentage-of-completion for long-lead aerospace programmes; no aggressive recognition found by the auditor's substantive testing.
- **Capitalisation (new detail this stage):** Note 4A CWIP (p.245) discloses the exact capitalisation mix for FY26: Other expenses Rs 19.68 Cr, Employee costs Rs 16.36 Cr, **Finance cost Rs 15.92 Cr**, Materials Rs 35.86 Cr, ROU depreciation Rs 2.03 Cr = **Rs 89.85 Cr total capitalised** (vs Rs 105.88 Cr FY25) — standard Ind AS 16/23 practice, transparently tabulated, not aggressive.
- **ECL matrix:** the single most policy-relevant flag in the whole note set — coverage nearly halved (1.91%→0.73%) with **zero fresh charge** even as the book grew 69% (Note 9(i) p.250, Note 28(A)(ii) p.279).
- **Lease IBR:** 6%-13.5% p.a. range disclosed (Note 5, p.245) — wide, reflecting the India-SEZ vs foreign-lease mix; disclosed, not itself aggressive.
- No policy changes quantified this year; no restatements found (confirmed independently by full-document search for "restat").

### 2B RPT map — extended (debt-cost angle, thin in Stage 2)
Beyond Stage 2's Rs 115 Cr / ~9.4%-of-revenue purchase/services total, this stage adds: **Melligeri Investment LLC (MILLC)** loan of **Rs 1.81 Cr at 13% p.a., repayable on demand** (Note 15, p.266) — a *second* promoter-linked facility at the identical 13% rate as the AMIPL loan (Rs 28.43 Cr), not previously itemised. Non-related-party debt priced in the same window: **Twin and Bull Opportunities Fund-1 NCD, Rs 37.16 Cr at 13% p.a.** (24-month tenor, unsecured) and **Vivriti Capital term loan, Rs 1.92 Cr at 11.80% p.a.** (p.264-266). The company's marginal cost of *new* non-bank debt in FY26 clusters at **11.8%-13% p.a.**, well above its bank facility rates (T-bill/Repo + 2.75%-8.95%) — a genuinely new data point on financing cost.

### 2C Contingent liabilities
FY26 total Rs 14.96 Cr (Labour Rs 6.90 Cr + Tax Rs 8.06 Cr) ≈ **1.01% of net worth** (Rs 1,485.55 Cr) — well under the 25%/100% flags. FY25's equivalent was ~12.98% of the smaller FY25 net worth, reduced only by a favourable Karnataka HC order reversing a Rs 7.80 Cr tax demand — the FY26 "immaterial" read is a product of a one-off court outcome, not a structurally low base (Note 30, p.282-283).

### 2D Receivables — see 2A/Phase 3; **FLAG-CASH** confirmed independently this stage.

### 2E Inventory
FY26 Rs 567.44 Cr vs FY25 Rs 408.27 Cr (+39.0%, independently verified from the Balance Sheet) against revenue +33.1% — inventory growing faster than revenue, consistent direction with the receivables finding.

### 2F Borrowings / debt maturity wall — EXTENDED (flagged thin in the task brief)
Facility-by-facility detail from Note 15(A) (p.264-266), not previously enumerated at this granularity:

| Facility | Amount (Rs Cr) | Rate | Tenor/security |
|---|---|---|---|
| HDFC Bank Loan 3 (ASMIPL) | 74.25 | 1M Repo+3% | 20 quarterly instalments; exclusive P&M charge, 2nd pari-passu current assets, 1st pari-passu on "Quest Towers" (MFRE Private Trust), Aequs corporate guarantee, DSRA |
| HDFC Bank Working Capital | 26.17 | CC 3M Repo+2.75%, PCFC SOFR+200bps | 1st pari-passu current assets + SEZ land + Aequs corporate guarantee + **Melligeri personal guarantee** |
| Twin and Bull Opportunities Fund-1 NCD | 37.16 | 13% p.a. half-yearly | 24-month tenor, unsecured |
| Aequs Aero Machine Inc (US, equipment finance) | 0.79 | 4.73-6.18% p.a. | 60-84 monthly instalments, machinery-only security |
| Aequs Aerospace France SAS (BPI/HSBC/Credit Coop/Codefi) | 5.28 | 2.03-2.25% p.a. | 80% National-Guarantee-Fund backed, 5-7yr tenor — materially cheaper than India rupee facilities |
| Melligeri Investment LLC | 1.81 | 13% p.a. | Repayable on demand, unsecured (RP) |
| AMIPL | 28.43 | 13% p.a. | Repayable on demand, unsecured (RP) |
| Vivriti Capital (ASMIPL/AFCPPL) | 1.92 | 11.80% p.a. | 45 monthly instalments, 2nd pari-passu current assets + 1st exclusive P&M charge + 20% cash collateral |

**Net debt reconciliation — refinement of Stage 2's finding.** Note 15(C)'s own formula (cash + other bank balances − lease liabilities − NCDs − non-current borrowings − current borrowings) produces a **NEGATIVE net debt (i.e. NET CASH) of Rs 344.28 Cr FY26 and Rs 705.26 Cr FY25** — the company is net-cash on this basis in *both* years. If Note 29 reports a *positive* "net debt Rs 250.05 Cr" and divides it into equity to get a *positive* 0.17 ratio, either (a) Note 29 uses a materially narrower cash-offset than Note 15(C), or (b) the two notes are not measuring the same concept, not merely failing to tie out arithmetically. **Stage 11 should not use Note 29's 0.17 at all**; it should use Note 15(C)'s reconciliation (which ties exactly to the cash-flow rollforward) and recognise the company is in a **net-cash**, not net-debt, position — a materially different characterisation than "leverage" language suggests, even though the "0.23" figure (front-matter chart AR p.14; MD&A "Total Debt/Equity" AR p.46) is itself a **third, differently-defined** (gross, not net) ratio that this AR does not itemise enough to fully bridge to Notes 15/28/29. Three leverage figures (0.17 net/Note29, ~0.23 net-recompute/Note15(C) sign-issue aside, 0.23 gross/MD&A) appear in one AR; only two are independently reconcilable from disclosed formulas.

### 2G Deferred tax
DTA recognised Rs 31.74 Cr FY26 / Rs 33.17 Cr FY25 (Balance Sheet, p.227) alongside large **unrecognised** losses (Stage 2: Rs 542.65 Cr never-expiring, Rs 701.22 Cr total) — consistent with the tax-charge-on-a-loss finding (2 above) independently confirmed from the P&L.

### 2H Exceptional items / ESOP / leases / subsequent events
Exceptional loss Rs 7.70 Cr FY26 (Rs 70.05 Mn Aerospace + Rs 6.90 Mn Consumer, Note 36 p.292) vs Rs 48.27 Cr FY25 (a disclosed one-off goodwill impairment, confirmed via the cash-flow adjustment line "Impairment of goodwill 482.65," p.231) — FY26's smaller exceptional charge makes the YoY "improvement" partly an easy comp against last year's one-off. ESOP: 19,92,313 options exercised (Rs 4.42 Cr realised), 1,04,46,893 outstanding at 31-Mar-26; a further 15,00,000-share RSU Plan 2026 is up for AGM approval (Notice p.307-309) — modest incremental dilution, capped and disclosed. Leases: total minimum payments Rs 382.66 Cr, PV Rs 297.35 Cr, 6-10yr terms (Note 5, p.245-246). **Subsequent event (Note 41, p.302):** Scheme of Amalgamation (board-approved 23-Apr-2026) folding ASMIPL, AEPPL and AFCPPL into the Parent — "will not have an impact on the consolidated financial statements" but will end the standalone/consolidated profitability divergence (Finding 4 above) going forward, since two of the three merging entities are the Consumer-segment cash-loss subsidiaries (per Phase 1's CARO xvii finding).

**Phase 2 verdict: 🟡 Watch.** Reconciles with Stage 2's accounting_quality:5 — I concur and do not revise it; independent re-derivation found zero discrepancies and one useful refinement (net-cash vs net-debt framing).
**Kill switch:** would not halt (no fraud, no going-concern doubt) but would require the five Stage-2 management questions answered before Halt 1. Continuing regardless.

---

## PHASE 3: FINANCIAL STATEMENTS (cash flow → balance sheet → P&L)

### 3A Cash flow (consolidated, Rs Cr)
| | FY26 | FY25 |
|---|---|---|
| PAT | (113.25) | (102.35) |
| CFO | **(98.75)** | +26.14 |
| CFO/EBITDA | **-0.64x** | +0.24x |
| Capex (PP&E acquisition) | 342.55 | 265.16 |
| FCF (CFO−capex) | **(441.30)** | (239.02) |
| Capex/D&A | 2.49x | 2.56x |
| Financing net inflow | 703.97 | 25.40 |
| Cash & equivalents, YE | 301.49 | 60.94 |

CFO turned **negative** for the first time in the two years shown, even as EBITDA rose 43% to Rs 154.45 Cr — the entire EBITDA (and more) was consumed by working-capital build: trade receivables +Rs 88.70 Cr, inventory +Rs 148.99 Cr (cash-flow statement adjustment lines, p.231), plus Rs 24.96 Cr income tax paid. FCF negative in both years and worsening. **The FY26 cash build (+Rs 234.53 Cr net) is entirely IPO-proceeds-funded** (Rs 943.81 Cr gross issue less Rs 43.73 Cr issue expenses), not operations-funded; absent the IPO, the company would have burned cash further.

**CFO quality checks:** (i) no one-time CFO inflators found — the Rs 22.97 Cr net FX gain is substantially *unrealised* and correctly excluded from CFO (Rs (46.86) Cr "unrealised exchange (gain)/loss" adjustment, p.231), so it inflates the *P&L* narrative, not the *cash* number; (ii) finance costs paid sit in financing activities (standard classification, not managed to flatter CFO); (iii) trade payables *increased* Rs 78.58 Cr (a mild cash-positive contributor — worth watching for stretching, though ageing shows only a small overdue tail); (iv) inventory *built*, it did not run down — a genuine cash drag, not an inflator.

Standalone CFO: Rs (4.79) Cr FY26 vs Rs +0.27 Cr FY25 — small in absolute terms; most Parent cash movement is investing (Rs 627.73 Cr into subsidiaries) and financing (IPO).

### 3B Balance sheet & key ratios
Consolidated total assets Rs 2,690.47 Cr FY26 vs Rs 1,859.84 Cr FY25 (+44.7%). Total Equity Rs 1,485.55 Cr vs Rs 715.98 Cr (IPO-driven).

| Ratio | FY26 | FY25 | Source |
|---|---|---|---|
| Current ratio (consol) | 1.58 | 1.10 | MD&A p.46 |
| Debt-Equity, Total Debt/Equity (consol) | 0.23 | 0.99 | MD&A p.46 |
| Net debt/Equity (Note 29, unreliable per 2F) | 0.17 | n/a (ties to Note15C) | Note 29 p.282-283 |
| DSCR (consol) | **0.34** | **0.07** | MD&A p.46 |
| DSCR (standalone) | 2.06 | 0.76 | Note 33 p.215 |
| ROCE (consol, EBIT/(Equity+debt+lease−cash)) | **1.56%** | 0.92% | MD&A p.46 |
| ROCE (standalone) | 3.41% | -6.81% | Note 33 p.215 |
| ROCE (consol, front-matter chart, FY24 for context) | — | — | **3.4% FY24** (AR p.14 image) |
| Return on Investment (consol, EBIT/Avg Assets) | 1.25% | 0.71% | MD&A p.46 |
| Return on net worth (consol) | -7.60% | -14.30% | MD&A p.46 |
| Fixed asset turnover (front-matter chart) | 1.18 | 1.84 | AR p.14 (FY24: 1.65) |
| Goodwill % of net worth | 1.16% | — | Balance Sheet p.227 |
| Quick ratio (computed) | ~0.89 | — | computed from BS |

**Both consolidated DSCR figures sit below 1.0x even after the FY26 "improvement"** — and the DSCR numerator is an EBITDA-like proxy (PBT+finance cost+ESOP+non-cash items), *not* actual CFO, which is negative. **Consolidated ROCE of 1.56% FY26 has not yet recovered to the FY24 level of 3.4%** despite two years of "growth" — the single most important credibility data point against any near-term "~20% manufacturing ROCE" claim (see Phase 4C). **Fixed asset turnover fell sharply** (1.84→1.18) as PP&E roughly quadrupled (Rs 166.88 Cr→Rs 773.21 Cr, driven by the Rs 412.19 Cr CWIP-to-PP&E transfer, Note 4A) while revenue grew only 33% — classic capex-ahead-of-utilisation.

**DuPont / ROE:** MD&A discloses Return on net worth -7.60% FY26 (from -14.30% FY25) — an improvement, and since Debt-Equity *fell* over the same period (0.99→0.23), **the improvement is not leverage-driven**; it is a genuine (if still-negative) operating improvement concentrated entirely in the Aerospace segment's more-than-doubled PBT, offset by the Consumer segment's widening loss.

### 3C P&L walk (consolidated, Rs Cr, verified directly from p.228)
Revenue 1,230.44 (+33.1%) → Other income 65.38 (+88.9%, cushions what would otherwise be a Rs 136.92 Cr pretax loss down to Rs 71.54 Cr) → EBITDA 154.45 (margin 12.55%, +43.0%) → Finance costs 92.35 (+56.8%, outrunning revenue growth) → D&A 137.69 (+33.1%) → Loss before JV/exceptional -75.60 (widened from -54.34) → JV share +11.75 → Exceptional -7.70 (vs -48.27 FY25, an easier comp) → **PBT -71.54 (vs -94.08 FY25 — the pretax loss actually NARROWED)** → Tax charge **+41.76 (vs +8.34 FY25, a 5x increase — a tax CHARGE on a pretax LOSS)** → **PAT -113.25 (vs -102.35 FY25 — the post-tax loss WIDENED)**.

**Earnings-quality finding (new this stage):** the market-visible "loss widened" headline is **substantially a tax story, not an operating-deterioration story** — the pretax loss *narrowed* by Rs 22.54 Cr YoY, but a Rs 33.42 Cr larger tax charge (non-recognition of DTA on growing losses + differential subsidiary tax rates, Note 35) more than offset that improvement and drove the post-tax loss wider. This nuance appears nowhere in the CEO/MD letters (see Phase 6A).

Basic/diluted EPS -1.87 vs -1.80 (continuing ops) — worsened slightly despite the smaller pretax loss, an artefact of the tax charge plus a ~6.8% higher weighted-average share count from the IPO; no basic/diluted gap of concern (anti-dilutive treatment properly applied both years, p.228/280).

Margin waterfall: Revenue 100% → EBITDA 12.55% → EBIT ~1.36% → PBT -5.82% → **PAT -9.21%** (exact match to MD&A's disclosed "Net profit margin (9%)," p.46) — finance costs and tax, not operating costs, turn a barely-positive EBIT into a wide net loss.

**Phase 3 verdict: 🟡 Watch, leaning Red on cash generation.**
**Kill switch:** a reviewer would flag that Rs 154 Cr of EBITDA converted to **zero** operating cash, and that DSCR sits below 1.0x on both bases even after the IPO — the balance sheet looks de-risked (low leverage, net cash) but the operating engine is not yet self-funding. Continuing regardless.

---

## PHASE 4: RISK FACTORS & MD&A

### 4A Disclosed risks (real vs boilerplate)
| Risk | Assessment |
|---|---|
| Foreign Exchange | Boilerplate ("natural hedging"); real Rs 22.97 Cr FY26 swing exists but no magnitude/sensitivity given in the risk text |
| Industry Demand (Aerospace) | Boilerplate diversification narrative; no cyclicality data despite order book being central to the thesis |
| Customer Concentration | Names "ten largest customer groups" generically — the actual, much sharper 58.0%-in-4-customers figure (Note 36) is **not referenced or sized here at all** |
| Capital Investment | Boilerplate ("prudent capital structure... lender covenants"); no covenant terms or capex-return sensitivity |
| Geographic Concentration | 🟢 Genuinely specific — names Karnataka concentration and the Hosur (TN) plan as concrete mitigation |
| Regulatory/Compliance | Boilerplate |
| Supply Chain | Moderately specific (single-source dependency named), generic mitigation |

### 4B MISSING RISKS (evidenced by Phases 1-3, absent from the Risk Management table, p.50-51)
1. **Cash conversion deterioration** — DSO 61.8→78.5d, ECL coverage halved, Axis Bank gap widening to Rs 59.01 Cr — a live, quantified, worsening trend with two independent corroborating disclosures elsewhere in this same AR, entirely absent from the risk table. Likely reason: generic pre-IPO risk-factor template not reconciled against FY26's own Note-level evidence.
2. **Governance/audit-trail/CARO risk** — a qualified Section 143(3)(b) opinion and CARO adverse remarks across 7 entities are not named anywhere in the risk table, despite being disclosed ~170 pages later in the same document. Likely reason: risk factors typically drafted before final audit sign-off items lock.
3. **Related-party financial dependency** — continuing 13% p.a. promoter/former-holding-company loans, promoter personal guarantees on Parent *and* subsidiary facilities, ~9.4% of revenue in RP flows — not flagged as a risk anywhere.
4. **Leverage-measurement reliability** — three non-reconciling leverage figures in one AR (2F above); no risk factor addresses financial-reporting/measurement risk.
5. **CFO transition** — Dinesh Iyer's departure effective 30-Jun-2026 (KMP footnote, p.60) is not flagged as a key-person/finance-leadership risk, despite occurring in the company's first year listed.
6. **Consumer-segment capital-allocation tension** — the risk table's generic diversification narrative never names the scale of the Consumer PBT loss (Rs 217.92 Cr, exceeding the Group's entire consolidated net loss once ACPPL is isolated) or its finance-cost burden nearly equalling Aerospace's.

### 4C MD&A deep dive
**Industry claims:** extensive macro/industry narrative (global aerospace TAM $340bn→$445.64bn by 2030, India aerospace $257.09bn by 2030, EMS/toy/cookware TAMs) — all third-party-sourced with footnoted URLs, appropriately caveated, outside this stage's remit to verify (a POND-type exercise for the spear pass).
**Growth/margin explanations:** Aerospace +27% "supported by strong programme execution" (vague); Consumer +84% "progressed from pilot to commercial scale" (verifiable against, and consistent with, the segment note).
**Credit-taking/blaming:** management credits its own execution for Aerospace growth and does **not** blame external factors for Consumer losses — attributes them candidly to capex-timing ("the arithmetic of an investment cycle... now behind us in spending terms," MD letter p.11) — relatively accountable tone.

**Guidance table:**

| Claim | Number | Timeframe | Source | Credibility check |
|---|---|---|---|---|
| Consumer segment EBITDA breakeven | 0% margin | Q4 FY2026-27 | CEO letter p.9 | Consumer FY26 margin -42.5% (Note 36); a >40pp swing in ~4 quarters is aggressive; no interim bridge given |
| Consolidated PAT breakeven | 0 | H1 FY2027-28 | CEO letter p.9 | Consolidated PBT still -Rs 71.54 Cr FY26; plausible only if Aerospace's 144.5% PBT growth pace continues — unverified from this AR |
| Consumer net-level profitability | Profitable | FY2029-30 | CEO letter p.9 | 3+ year-out, not independently testable here |
| Vision 2031 revenue | 4-6x FY26 base | FY2030-31 | CEO letter p.10 | Implies ~19-33% CAGR sustained 5 years; Aerospace alone grew 27% FY26, so plausible if sustained AND Consumer scales |
| Vision 2031 EBITDA margin | 18-22% | FY2030-31 | CEO letter p.10 | Aerospace segment ALREADY at 26.9% FY26 exceeds the top end of this *group* target; Consumer (-42.5%) is the sole drag |
| Vision 2031 ROCE | ~20% steady state | FY2030-31 | CEO letter p.10 | Consolidated ROCE only 1.56% FY26 (up from 0.92%, but below FY24's 3.4%) — closing an ~18.5pp gap in 5 years is a very large climb, unbridged by any interim milestone in this AR |
| FY27 aerospace revenue +25-30%, segment EBITDA margin >20%, ~20% "manufacturing ROCE" (company memory) | n/a | FY2026-27 | **NOT FOUND IN THIS AR** | This specific near-term FY27 guidance line does not appear anywhere in the FY26 Annual Report text; only the longer-dated Vision 2031 targets and the three CEO milestone dates appear here. Stage 11 must source the FY27 number outside this document. |

### 4D Tone and credibility (1-5)
| Dimension | Score | Evidence |
|---|---|---|
| Transparency | 3/5 | Loss directly named/explained (positive); but CG Report's "unmodified opinion" line omits the Section 143(3)(b) exception; risk section omits several live, evidenced risks |
| Consistency | 4/5 | Every cross-check performed (Aerospace/Consumer revenue, EBITDA, PAT, ROCE, D/E) matched exactly across front matter, letters, MD&A and audited Notes |
| Specificity | 3/5 | Three named milestone dates are unusually specific; risk/strategy sections are almost entirely generic template language |
| Accountability | 4/5 | Management owns the loss narrative, does not blame external factors; but the CGR's "unmodified opinion" framing specifically understates a real exception |
| Capital allocation sense | 3/5 | Rs 2,856 Cr Karnataka plan and Rs 1,900 Cr Hosur MoU named with a funding-mix statement, but Note 31's own capital-commitments figure (Rs 21.01 Cr contracted PP&E at 31-Mar-26) is nowhere near this scale — almost none of the announced capex is yet a contractual Ind AS commitment |

**Phase 4 verdict: 🟡 Watch.**
**Kill switch:** would not halt (no fabricated numbers; every cross-check matched) but would insist the six missing risks be added to the operator's own register before relying on the MD&A risk section as complete. Continuing regardless.

---

## PHASE 5: CORPORATE GOVERNANCE & BOARD

### 5A Board composition
6 directors: 3 Independent (incl. 1 woman) + 3 Non-Independent. Executive Chairman & CEO Aravind Melligeri; Co-founder & MD Rajeev Kaul; NED Dr. Ajay Aravind Prabhu; Independent Directors Dr. Eberhard Klaus Richter, Ms. Vidya Sarathy, Dr. Anup Wadhawan — **all three Independents appointed 25-Apr-2025** (EGM), i.e. **<18 months tenure** as of this AR — a newly-constituted, pre-IPO board with no long-tenure concern but also no established track record (WATCH, not red flag; typical of a recent listing). **18 board meetings** held in FY26 (unusually high, IPO-year activity); attendance range **83.3%-100%** — no director breaches the 75% threshold. **AGM attendance was weak**: 4 of 6 directors, including the CEO, did **not** attend the 30-Sep-2025 AGM (p.97). Dr. Anup Wadhawan holds 3 other listed directorships (Yatra Online, GSK Pharmaceuticals, Turtlemint Fintech) — within the Reg.17A limit of 7. No director exceeds 8 board seats or the 10/5 committee limits (self-certified, p.97).

### 5B Committees
8 committees (Audit, NRC, CSR, Stakeholders' Relationship, Risk Management, Independent Director, IPO, Administrative). CSR Committee exists despite no CSR obligation arising in FY26. 2 Independent Director meetings held (p.114).

### 5C Compensation
**CEO fixed-pay-to-median multiple: 129.31x** (Annexure 4, p.83) — very high even by listed-company norms, and this *excludes* variable pay (not yet paid) from both the ratio and the YoY-increase base. MD Rajeev Kaul: 36.60x. **Internal contradiction flagged:** Annexure 4 states the CEO's *fixed* pay rose only **+0.63%** YoY, yet Note 34's RPT total-remuneration figure shows the CEO's *total* comp rose **+111% to Rs 9.27 Cr** (Stage 2) — the entire increase came from a non-fixed-pay component (variable/bonus/ESOP or another element) that neither note reconciles against the other. **Median employee remuneration fell -16.82% YoY** (Annexure 4, p.83) in the same year the CEO's total package rose 111% — a stark divergence in a widening-loss year, regardless of which specific component drove it. ESOP: 19,92,313 options exercised (Rs 4.42 Cr realised); 1,04,46,893 outstanding at 31-Mar-26; a further 15,00,000-share RSU Plan 2026 up for AGM approval — modest, capped, disclosed dilution.

### 5D Shareholding
Promoters and Promoter Group hold **59.08%** (CG Report p.111). **No share pledge disclosed anywhere** (full-document search for "pledge" returns only lender-side asset pledges, never a promoter share pledge) — clean on this specific test. FPI(Corp) 3.90%, Mutual Funds 5.63%, AIFs 5.52%, **Foreign Companies 14.47%** (unusually large; holder identity not disclosed below the promoter line). **No YoY shareholding-pattern comparison exists** — this is the company's first year listed, so a "promoter selling against growth narrative" test is **NOT YET POSSIBLE** from this document (flag as NOT FOUND, not as a clean pass; re-test at the next AR).

### 5E Governance red-flag checklist
| Item | Finding |
|---|---|
| Whistleblower | 1 complaint received FY26, concluded per policy (p.62); auditor factored it into scoping (CARO xi(c)) |
| SEBI/exchange actions | None in last 3 years (p.113) — clean |
| RPT committee | Audit Committee reviews RPTs quarterly; FY27 material-RPT shareholder approval obtained 27-Mar-2026 for Aequs SEZ Private Limited (p.63) |
| Auditor fee ratio | Non-audit (Rs 4.21 Cr) > audit (Rs 0.98 Cr), 4.3x — flagged, IPO-year context noted |
| CSR compliance | No obligation arose; no violation |
| Section 143 fraud | None reported by either auditor |
| Material subsidiary auditor | ASMIPL audited by same firm (B S R) as Parent; **Aequs Aerospace France SAS's auditor (PKF Arsilon) was appointed 26-Jun-2026 — AFTER the FY26 audit sign-off (26-May-2026)** — a post-year-end auditor change at a material foreign subsidiary, not explained in this AR |
| CFO turnover | Dinesh Iyer ceased to be CFO effective **30-Jun-2026** — disclosed only as a KMP-table footnote (p.60, p.83), occurring after the FY26 audit sign-off but before the Board's Report finalisation (07-Aug-2026); a first-year-listed finance-leadership departure warranting a direct question |

**FLAG-PROMOTER-PRELIM: NOT raised** — no pledge found and no YoY trend data exists yet (year 1 as listed) to test a selling pattern.

**Phase 5 verdict: 🟡 Watch.**
**Kill switch:** would not halt (no pledge, no SEBI action, no fraud) but would want the CEO-to-median multiple, the CFO departure, and the France-subsidiary auditor change explained before Halt 1. Continuing regardless.

---

## PHASE 6: CHAIRMAN'S LETTER & FRONT MATTER

### 6A Narrative vs reality

| # | Claim (source) | ✅/❌ |
|---|---|---|
| 1 | "Revenue grew 33% to Rs 12,304 Mn, EBITDA grew 43% to Rs 1,545 Mn, margin 13% from 12%" (CEO letter p.9) | ✅ exact match to audited P&L |
| 2 | "Aerospace order book USD 889 million as at 31-Mar-2026" (CEO p.9; MD&A p.44) | ✅ internally consistent (3 mentions); **also consistent with company memory's Q1FY27 figure of USD 1,004mn (+13% QoQ): 889×1.13=1,004.6** — a genuine cross-document corroboration |
| 3 | "Consumer contribution rose from 11% FY25 to 15% FY26" (MD letter p.11-12) | ✅ verified: 99.97/924.61=10.81%≈11%; 184.06/1,230.44=14.96%≈15% |
| 4 | "The loss reflects depreciation and financing costs of recently commissioned capacity, and Consumer's cost base largely in place" (CEO p.9) | ⚠️ Directionally true (finance costs +56.8%, D&A +33.1%) but **incomplete**: does not mention that the *post-tax* loss widened substantially because of a larger tax charge, while the *pretax* loss actually narrowed (Phase 3C) |
| 5 | "As a listed company, we remain committed to... transparency" (CEO p.8) | ❌ in tension with the CG Report's "unmodified opinion" claim (p.114), which omits the Section 143(3)(b)/Rule 11(g) qualification disclosed in the same AR's Auditor's Reports |
| 6 | "Rs 2,856 Cr investment over five years... funded through accruals, calibrated debt, and equity" (CEO p.6) | ⚠️ Untestable against this AR's own Note 31 capital-commitments figure of only Rs 21.01 Cr contracted at 31-Mar-26 — not false, but minimally backed by Ind AS "commitment" |
| 7 | "Balance sheet strengthened materially... headroom to invest" (MD p.11) | ✅ on stated ratios (D/E, current ratio); ⚠️ but the same balance sheet produced **zero** operating cash in FY26 — the strength is IPO-funded, not operations-funded, a distinction the letter does not draw |

### 6B Strategic priorities
Four named priorities (Strengthen Partnerships, Scale Growth Platforms, Extend Core Capabilities, Drive Technology/Operational Excellence, MD&A p.50) are broad and generic; the more specific, capital-backed items (Hosur MoU, Rs 2,856 Cr Karnataka plan) carry minimal current contractual commitment (per 6A#6).

### 6C Metrics showcased vs conspicuously absent
Showcased: revenue, EBITDA, PAT, D/E, ROCE, fixed-asset turnover (front-matter chart p.14); order book; segment growth. **Conspicuously absent from the letters:** operating cash flow (never mentioned, despite being negative); DSO/receivables trend; the audit qualification; CEO-to-median pay ratio; the precise 58%-in-4-customers concentration figure.

### 6D Tone/priority drift vs prior year
**NOT INFERABLE** — this is the company's first Annual Report as a listed entity; no prior-year Chairman's letter exists in this corpus for comparison.

### 6E Quiet Abandonment Check (mandatory)
Three findings from reading the opening letters against the operational sections:

1. **Aerospace product-mix/customer-broadening claim** — MD's letter (p.11-12) names "deepening participation in landing-gear and engine components" and "broadening the customer base" as FY27 priorities. The segment note (Note 36) discloses no product-mix-within-Aerospace or customer-count trend data at all — this is a *forward-looking* FY27 claim being made at a FY26 year-end, so it cannot yet be judged abandoned; classified as **materiality-limited / untestable from this AR**, not a true abandonment.
2. **Vision 2031 ROCE aspiration vs the same AR's own ROCE disclosure** — the CEO letter (p.10) states a ~20% steady-state ROCE target for FY30-31; the *same annual report's* own MD&A (p.46) discloses consolidated ROCE of just 1.56% FY26 (up from 0.92%, but below FY24's 3.4%), with **no bridge or interim milestone anywhere in the operational sections** for how the company closes an ~18.5pp gap. Classified as **(c) hedged retreat in spirit** — an ambitious number stated up front, with the operational sections silent on the scale of the climb required. **Materiality: HIGH** — directly bears on company memory's central "guidance vs delivery" load-bearing fact.
3. **Consumer "commercial scale" narrative vs the segment margin** — the MD's letter (p.11-12) frames FY26 as the year Consumer "progressed from pilot production to commercial scale," presented as an unambiguous positive milestone. The segment note shows Consumer's EBITDA-equivalent margin **worsened** from -28.7% to -42.5% YoY in this exact year, with no acknowledgement in the letter that scaling up made the segment's percentage loss *bigger*, not smaller. Classified as **(a) implicit retraction**. **Materiality: HIGH** — central to the Consumer capital-allocation load-bearing fact.

**Conclusion: quiet abandonments identified (items 2 and 3 above); item 1 is noted as untestable rather than abandoned.** This is distinct from Phase 4B's omission analysis: these are claims *present* in the opening narrative that the operational sections *contradict or leave unaddressed at scale*, not simply topics never covered.

**Phase 6 verdict: 🟡 Watch.**

---

## PHASE 7: MULTI-STRATEGY SIGNAL EXTRACTION

| Strategy | Verdict | Top reasons |
|---|---|---|
| Value + Quality | FAIL | No value support (loss-making, ROCE 1.56%, negative CFO); quality mixed (qualified audit, CARO adverse across 7 entities) — fails both legs |
| **GARP** | **WATCHLIST** | (1) Growth is real and verified — Aerospace +27%, Consumer +84%, order book internally and cross-document consistent (889→1,004 USD mn). (2) "Reasonable price/quality" legs unresolved from this AR alone: consolidated ROCE (1.56%) and negative CFO fail a strict quality screen *today*; the case rests on the multi-year Vision 2031 climb, which this AR cannot yet corroborate beyond the Aerospace segment's own margin (26.9%, already ahead of the group target). (3) The destination-PE/Section 1B work sits with Stage 11, but the raw material — a real, verified, high-growth Aerospace segment inside a consolidated entity whose whole-company numbers still look weak — is exactly the profile Amendment 19's FV-CAGR test needs to price carefully |
| **Turnaround** | **WATCHLIST, bordering PASS** | For: Aerospace PBT +144.5%, segment margin already ahead of guidance; pretax loss *narrowed* once the tax-charge effect is stripped (Phase 3C); balance sheet delevered post-IPO. Against: post-tax loss widened; CFO turned negative; Consumer segment margin *worsened* in the exact year management calls its "commercial scale" milestone (Phase 6E); qualified audit opinion and 7-entity CARO adverse remarks raise doubt about the control environment underpinning the turnaround's own numbers. Net: WATCHLIST, biased toward PASS if FY27 data (outside this document) confirms the Aerospace pace continuing and the audit-trail/CARO items clear |
| Capex-Led Growth | WATCHLIST, leaning PASS | Textbook profile: Rs 412.19 Cr CWIP-to-PP&E transfer in-year, Rs 342.55 Cr FY26 capex (2.49x depreciation), fixed-asset turnover falling sharply (1.84→1.18) as new capacity awaits utilisation, Rs 2,856 Cr multi-year Karnataka plan plus Rs 1,900 Cr Hosur MoU — but only Rs 21.01 Cr is contractually committed at year-end, a genuine "trust the plan" gap |
| Cash Flow Compounder | FAIL | CFO negative FY26; FCF negative both years and worsening; cash build is entirely IPO-funded |
| Contrarian | WATCHLIST | Market cap ~Rs 16,242 Cr sits above the strategy's normal small/micro-cap remit (already an operator-flagged environment note); whether the market price already reflects Vision 2031 optimism or still discounts the Consumer drag and governance flags cannot be assessed from this document |
| Insider Confidence | WATCHLIST / NOT FOUND | No promoter pledge (clean); but no post-IPO buying/selling trend exists yet — genuinely not found, not a clean pass by default |
| Guidance Divergence | WATCHLIST, material | The clearest, most quantifiable divergence in this AR: consolidated ROCE of 1.56% (company's own disclosed formula) against a ~20% steady-state Vision 2031 target, with the FY27-specific "~20% manufacturing ROCE" guidance line itself NOT FOUND anywhere in this AR |

---

## PHASE 8: FINAL VERDICT DASHBOARD

**Company snapshot:** Aequs Ltd, listed 10-Dec-2025 (BSE 544634 / NSE AEQUS); FY26 consolidated revenue Rs 1,230.44 Cr (+33.1%), EBITDA Rs 154.45 Cr (margin 12.55%), net loss Rs 113.25 Cr (widened from Rs 102.35 Cr); two segments, Aerospace (85.0% of revenue, PBT +144.5% to Rs 173.98 Cr) and Consumer (15.0% of revenue, PBT -Rs 217.92 Cr, margin -42.5%); promoters Aravind Melligeri (Exec. Chairman & CEO) and Rajeev Kaul (Co-founder & MD) hold 59.08% via Promoter Group.

### Phase-wise verdict summary
| Phase | Verdict |
|---|---|
| 1 — Auditor's Report & CARO | 🔴 Red Flag |
| 2 — Notes | 🟡 Watch |
| 3 — Financial Statements | 🟡 Watch (leaning Red on cash) |
| 4 — Risk Factors & MD&A | 🟡 Watch |
| 5 — Corporate Governance | 🟡 Watch |
| 6 — Chairman's Letter & Front Matter | 🟡 Watch |
| 7 — best-fit strategy | Capex-Led Growth (Turnaround/GARP close behind) |

### Overall quality score: 4.5/10
| Component (25% each) | Score | Basis |
|---|---|---|
| Governance | 4/10 | Qualified audit-trail opinion, CARO adverse across 7 entities, 129.31x CEO-to-median multiple, non-audit fees 4.3x audit fees, CFO and material-subsidiary-auditor turnover post year-end; offset by clean pledge/SEBI/fraud record and solid board attendance |
| Accounting quality | 5/10 | Concurs with Stage 2; independently re-verified with zero discrepancies. Genuine positives (Aerospace margin, tax de-risking) offset by ECL-coverage decline, unreconciled net-debt figures, qualified opinion |
| Balance sheet | 6/10 | Net cash position both years, D/E and current ratio materially improved post-IPO, no borrowing defaults; offset by DSCR below 1.0x on both bases and fixed-asset turnover collapse |
| Earnings quality | 3/10 | Consolidated ROCE only 1.56%, post-tax loss widened on a tax-charge effect (pretax loss actually narrowed), CFO negative, Consumer segment margin worsened during its "scale-up" year |

### Top 3 strengths
1. Aerospace segment PBT more than doubled to Rs 173.98 Cr (+144.5%), segment EBITDA margin 26.9% FY26 already exceeding the ">20%" guidance neighbourhood referenced in company memory a year early (Note 36, verified).
2. Post-IPO balance sheet materially delevered: consolidated D/E 0.99→0.23 (or ~0.23 net-cash-adjusted), current ratio 1.10→1.58, genuine net-cash position of Rs 344-705 Cr in both years shown, zero borrowing defaults (CARO ix(a)).
3. Direct, specific management acknowledgment of the loss with three named, checkable milestones (Consumer EBITDA breakeven Q4 FY26-27, consolidated PAT breakeven H1 FY27-28) — an unusually candid disclosure for a first-year-listed company's Annual Report.

### Top 3 red flags
1. Both statutory audit opinions carry a Section 143(3)(b)/Rule 11(g) audit-trail qualification, and CARO Annexure A names adverse remarks (including auditor-confirmed cash losses) across 7 Group entities, with 4 further entities having no CARO report issued at all.
2. Cash conversion deteriorating on two independent, corroborating disclosures: receivables +69% vs revenue +33%, ECL coverage halved with zero fresh charge, Axis Bank stock-statement gap widening every quarter to Rs 59.01 Cr — CFO turned negative (Rs -98.75 Cr) for the first time in the two years shown, converting zero of Rs 154.45 Cr EBITDA to cash. **FLAG-CASH.**
3. Consolidated ROCE of just 1.56% FY26 (company's own disclosed formula, MD&A p.46) sits far below a Vision 2031 target of ~20% steady-state ROCE by FY30-31, with no interim bridge anywhere in this AR, and the FY27-specific "~20% manufacturing ROCE" guidance referenced in company memory does not appear in this document at all.

### Key monitorables for next quarter/AR
See `monitorables` in the YAML block below.

### One-line verdict
Aerospace beats its own guidance. Cash, tax and governance flags need answers first.

**Best-fit strategy: Capex-Led Growth** (Turnaround and GARP close behind, both WATCHLIST; see Phase 7 for full reasoning).

---

```yaml
stage: B03-ardeep
company: "AEQUS"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "prospectus: ABSENT (HIGH gap; company listed 10-Dec-2025)"
  - "results: ABSENT"
  - "rating: ABSENT as a separate document; a CARE BBB-;Stable rating on Rs 25 Cr long-term bank facilities is disclosed inside the AR's Corporate Governance Report (p.113)"
  - "announcements: ABSENT"
  - "shareholding: ABSENT as a separate document; the AR's own CG Report shareholding pattern (p.111) is the only source, and carries no YoY comparison (first year listed)"
  - "research: ABSENT"
  - "other: ABSENT"
  - "screening: companion CSVs header-only; Data_Sheet populated"
  - "peer-concalls: DYNAMATECH single transcript Feb-2024 (stale)"
  - "manifest: no listed_date; sector_cap_row set by Step 1 brief"
  - "prior-year ARs: FY24 and FY25 ARs absent; Phase 6D (tone/priority drift vs prior year) and part of Phase 5D (promoter selling pattern) are NOT FOUND IN DOCUMENT for this reason"
flags:
  - type: FLAG-CASH
    reason: "Independently re-verified: consolidated CFO turned negative (Rs -98.75 Cr FY26 vs +Rs 26.14 Cr FY25) for the first time in the two years shown, converting zero of Rs 154.45 Cr FY26 EBITDA to operating cash (CFO/EBITDA -0.64x); FCF negative and worsening both years; the entire FY26 cash build is IPO-proceeds-funded, not operations-funded. Corroborates Stage 2's receivables/ECL/stock-statement FLAG-CASH with an independent cash-flow-statement angle (Consolidated Cash Flow Statement, AR p.231-232)."
  - type: FLAG-GOVERNANCE
    reason: "Both statutory audit opinions (standalone AR p.152-153, consolidated AR p.222-223) carry a Section 143(3)(b)/Rule 11(g) audit-trail qualification; CARO Annexure A (AR p.224) names adverse remarks across 7 Group entities including auditor-confirmed cash losses at 3; CEO-to-median pay multiple is 129.31x (Annexure 4, AR p.83) with an unreconciled +0.63% fixed-pay-increase vs +111% total-remuneration-increase internal contradiction; CFO and a material foreign subsidiary's auditor both turned over after the FY26 audit sign-off date, undisclosed beyond footnotes."
phase_verdicts: {p1: "Red Flag", p2: "Watch", p3: "Watch (leaning Red on cash)", p4: "Watch", p5: "Watch", p6: "Watch", p7_best_fit: "Capex-Led Growth"}
overall_quality: 4.5
quality_components: {governance: 4, accounting: 5, balance_sheet: 6, earnings: 3}
kill_switch_notes:
  - "Phase 1: a reviewer would pause on the group-wide audit-trail qualification and 7-entity CARO adverse remarks in a first listed year; continued per protocol."
  - "Phase 2: would not halt but would require the five Stage 2 management questions answered before Halt 1; continued per protocol."
  - "Phase 3: would flag that Rs 154 Cr EBITDA converted to zero operating cash and that DSCR sits below 1.0x on both bases; continued per protocol."
  - "Phase 5: would want the CEO-to-median multiple, the CFO departure, and the France-subsidiary auditor change explained before Halt 1; continued per protocol."
triple_pass_verification:
  verified: 15
  discrepancies: []
missing_risks:
  - {risk: "Cash conversion deterioration (DSO, ECL coverage, Axis Bank stock-statement gap)", evidence: "Note 9(i) AR p.250; Note 28(A)(ii) AR p.279; Note 15(B) AR p.267 — absent from MD&A Risk Management table AR p.50-51"}
  - {risk: "Governance/audit-trail/CARO risk", evidence: "Auditor's Reports AR p.152-153, p.222-224 — absent from MD&A Risk Management table AR p.50-51"}
  - {risk: "Related-party financial dependency (13% p.a. RP loans, promoter personal guarantees, ~9.4% of revenue in RPT flows)", evidence: "Note 34 AR p.284-289; Note 15 AR p.264-266 — absent from MD&A Risk Management table"}
  - {risk: "Leverage-measurement reliability (three non-reconciling FY26 leverage ratios in one AR)", evidence: "Note 15(C) AR p.267; Note 29 AR p.282-283; MD&A AR p.46 — absent from MD&A Risk Management table"}
  - {risk: "CFO (finance-leadership) transition", evidence: "KMP table footnote AR p.60, p.83 — absent from MD&A Risk Management table"}
  - {risk: "Consumer-segment capital-allocation tension (PBT loss scale vs Aerospace)", evidence: "Note 36 AR p.292-294 — absent from MD&A Risk Management table"}
guidance_table:
  - {claim: "Consumer segment EBITDA breakeven", number: "0% margin", timeframe: "Q4 FY2026-27", credibility: "Aggressive: FY26 Consumer margin -42.5% (Note 36); >40pp swing in ~4 quarters, no interim bridge given (CEO letter AR p.9)"}
  - {claim: "Consolidated PAT breakeven", number: "breakeven", timeframe: "H1 FY2027-28", credibility: "Requires Aerospace PBT growth to keep outrunning Consumer losses and finance costs; consolidated PBT still -Rs 71.54 Cr FY26 (CEO letter AR p.9)"}
  - {claim: "Consumer net-level profitability", number: "profitable", timeframe: "FY2029-30", credibility: "3+ year-out, not independently testable from this AR (CEO letter AR p.9)"}
  - {claim: "Vision 2031 revenue growth", number: "4-6x FY26 base", timeframe: "FY2030-31", credibility: "Implies ~19-33% CAGR for 5 years; Aerospace alone grew 27% FY26, plausible if sustained and Consumer scales (CEO letter AR p.10)"}
  - {claim: "Vision 2031 EBITDA margin", number: "18-22%", timeframe: "FY2030-31", credibility: "Aerospace already at 26.9% FY26 exceeds the top end of this group target; Consumer at -42.5% is the sole drag (CEO letter AR p.10; Note 36)"}
  - {claim: "Vision 2031 ROCE", number: "~20% steady state", timeframe: "FY2030-31", credibility: "Consolidated ROCE only 1.56% FY26 (MD&A AR p.46), below the FY24 level of 3.4% (front-matter chart AR p.14); no interim bridge given anywhere in this AR"}
  - {claim: "FY27 aerospace revenue +25-30%, segment EBITDA margin above 20%, ~20% manufacturing ROCE (company memory)", number: "n/a", timeframe: "FY2026-27", credibility: "NOT FOUND IN THIS AR; only Vision 2031 (FY30-31) and the three CEO milestone dates appear in this document"}
monitorables:
  - {metric: "DSO (days sales outstanding)", threshold: "further rise above 78.5 days", where: "Quarterly results / next AR Note 9(i)", why: "DSO rose 61.8->78.5 days FY26 alongside ECL coverage halving; FLAG-CASH driver"}
  - {metric: "Axis Bank quarterly stock-statement gap (trade receivables)", threshold: "gap continuing to widen past Rs 59.01 Cr", where: "Next AR Note 15(B) / quarterly bank filings", why: "Independently corroborates the receivables/ECL trend from a lender-facing disclosure"}
  - {metric: "Consolidated ROCE (company's own MD&A formula)", threshold: "material improvement above the FY26 1.56% base, tracking toward Vision 2031's ~20%", where: "Next AR MD&A Key Financial Ratios table", why: "Single largest guidance-vs-delivery gap found in this AR"}
  - {metric: "Net debt reconciliation across Notes 15(C)/28(C)(ii)/29", threshold: "whether the FY26 discrepancy is corrected or explained", where: "FY27 AR Notes 15/28/29", why: "Feeds the leverage ratio presented as evidence of post-IPO balance-sheet repair"}
  - {metric: "Consumer segment PBT and finance-cost share of combined segment finance costs", threshold: "narrowing toward the CEO's Q4 FY26-27 EBITDA-breakeven milestone", where: "Quarterly segment disclosures / FY27 AR Note 36", why: "Tests the single most specific, checkable guidance claim in this AR"}
  - {metric: "Rule 11(g) audit-trail qualification and CARO adverse-remark count (7 entities)", threshold: "whether the FY27 opinion clears the qualification and adverse-remark count falls", where: "FY27 Auditor's Report and CARO Annexure A", why: "Tests whether this was a one-off IPO-year transition issue or a persistent group-wide gap"}
  - {metric: "Consolidated CFO / CFO-EBITDA conversion", threshold: "return to positive CFO, conversion above ~0.5x", where: "Quarterly cash-flow disclosures / FY27 AR cash flow statement", why: "FY26 EBITDA of Rs 154 Cr converted to zero operating cash"}
  - {metric: "CFO (person) successor and stated reason for departure", threshold: "named permanent successor disclosed", where: "Exchange filings / next AR KMP section", why: "First-year-listed finance-leadership turnover coincided with the audit-trail qualification and negative CFO"}
ar_new_downstream_entities:
  - name: "Ajna Aerospace & Defence Private Limited"
    where_in_ar: "Board's Report p.56-57 (Performance of JVs); Note 37 p.293; CARO Annexure A clause vii(a)/xiv p.224"
    entity_type: "New joint venture (UAV/defence manufacturing), incorporated 22-Oct-2025"
  - name: "Accel India VIII (Mauritius) Limited"
    where_in_ar: "Board's Report p.56-57 (Ajna JV partner)"
    entity_type: "New JV partner (PE/VC investor in Ajna Aerospace & Defence)"
  - name: "Vagus Defence Tech & Aerospace Fund I"
    where_in_ar: "Board's Report p.56-57 (Ajna JV partner)"
    entity_type: "New JV partner (defence-tech fund, Ajna Aerospace & Defence)"
  - name: "Twin and Bull Opportunities Fund-1"
    where_in_ar: "Note 15(A) borrowings, AR p.265"
    entity_type: "New financing counterparty; Rs 37.16 Cr NCD at 13% p.a., unsecured, 24-month tenor"
  - name: "Vivriti Capital Limited"
    where_in_ar: "Note 15(A) borrowings, AR p.264-266"
    entity_type: "New lender; Rs 1.92 Cr term loan at 11.80% p.a. to ASMIPL/AFCPPL, secured"
  - name: "Hasbro / Mattel / Spin Master"
    where_in_ar: "BRSR Section A, AR p.121 (types of customers)"
    entity_type: "Named Consumer-segment (toy brand) customers, first explicit naming in this AR; not tied to a disclosed revenue percentage"
  - name: "Safran (named alongside Airbus, Boeing, Collins Aerospace, Honeywell, SAAB, GKN Aerospace, Eaton, DTL, Bombardier)"
    where_in_ar: "BRSR Section A AR p.121; Global Operations AR p.15"
    entity_type: "Named Aerospace-segment customer, first explicit naming in this AR; corroborates but does not size or confirm the company-memory Safran LTA claim, and is not tied to Note 36's anonymised Customer 1-4"
strengths_top3:
  - "Aerospace segment PBT more than doubled to Rs 173.98 Cr (+144.5%), segment EBITDA margin 26.9% FY26 already exceeding the >20% guidance neighbourhood a year early (Note 36, independently verified)"
  - "Post-IPO balance sheet materially delevered: D/E 0.99 to 0.23, current ratio 1.10 to 1.58, genuine net-cash position both years, zero borrowing defaults (CARO ix(a))"
  - "Management directly names and explains the loss with three specific, checkable milestones (Consumer EBITDA breakeven Q4 FY26-27, consolidated PAT breakeven H1 FY27-28), unusually candid for a first-year-listed AR"
red_flags_top3:
  - "Both statutory audit opinions carry a Section 143(3)(b)/Rule 11(g) audit-trail qualification; CARO names adverse remarks (including auditor-confirmed cash losses) across 7 Group entities, with 4 more entities having no CARO issued at all"
  - "Cash conversion deteriorating on two corroborating notes plus an independently verified cash-flow-statement angle: CFO turned negative (Rs -98.75 Cr), converting zero of Rs 154.45 Cr EBITDA to cash (FLAG-CASH)"
  - "Consolidated ROCE of just 1.56% FY26 (company's own disclosed formula) sits far below the Vision 2031 ~20% steady-state target with no interim bridge in this AR, and the FY27-specific near-term ROCE guidance referenced in company memory does not appear in this document at all"
best_fit_strategy: "Capex-Led Growth"
one_line_verdict: "Aerospace beats its own guidance. Cash, tax and governance flags need answers first."
analyst_note: "Two refinements beyond Stage 2, both load-bearing for Stage 11. First, Note 15(C)'s own formula produces a NEGATIVE net debt (net CASH) of Rs 344.28 Cr FY26 in both years shown; Note 29's positive Rs 250.05 Cr figure and the front-matter/MD&A 0.23 ratio use different, narrower formulas that this AR does not fully itemise — three leverage figures exist, only two are independently reconcilable, and the underlying economic position is net cash, not net debt, on the most defensible basis. Second, the post-tax loss widening (-102.35 to -113.25 Cr) is substantially a TAX-CHARGE story: pretax loss actually NARROWED (-94.08 to -71.54 Cr) but a 5x larger tax charge on a pretax loss reversed that improvement. Neither nuance appears in the CEO/MD letters. Phase 6E found two genuine quiet abandonments (Vision 2031 ROCE vs the 1.56% actual; Consumer 'commercial scale' framing vs its worsening margin) that bear directly on the transition thesis's credibility."
```
