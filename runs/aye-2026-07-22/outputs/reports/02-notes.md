# STAGE 2 — NOTES TO FINANCIAL STATEMENTS — PASS 3 (PATTERN PASS + CONSOLIDATION)
Company: AYE (Aye Finance Limited, formerly Aye Finance Private Limited)
Source: IPO Prospectus, 614-page extract `annual-report__1770879625663.txt`. Notes = Annexure V
("Material accounting policies and explanatory notes to Restated financial statements"), Notes 1-56,
extract pages ~309-405/614, plus the Auditor's Examination Report and Annexure VI (Statement of
Restatement Adjustments). Figures in ₹ millions as presented in the source unless stated otherwise
(₹1 Cr = ₹10 million).

**NBFC caveat, carried from Passes 1-2**: this is a lending NBFC with no inventory, no conventional
trade receivables, and minimal trade payables. Those checklist items are NOT APPLICABLE; the loan-book
equivalents (loan portfolio, ECL/Stage migration, GNPA) are the signal that matters and are what this
consolidation weighs most heavily, per the B00 context.

---

## PASS 3 — PATTERN RE-READ

Method: rather than a third sequential note-by-note read, this pass hunted for contradictions between
notes, note-vs-main-statement mismatches, deliberately thin disclosure next to richly detailed
disclosure elsewhere, restated/reclassified prior-year figures, subsequent events, and going-concern
language — then spot-verified the highest-stakes Pass 1/Pass 2 numbers directly against the source
extract before consolidating.

**Verification performed this pass** (all confirmed against the source text, not re-derived):
- Annexure VI reconciliation (p.404/614): audited-to-restated PAT and equity bridge figures match
  Pass 2's transcription exactly, including the FY23 -₹139.23mn PAT / -₹140.11mn equity tax-expense
  adjustment and the sign-reversing adjustments in FY24 (+₹105.52mn) and FY25 (+₹39.80mn).
- Covenant-breach note (p.401-402/614, Note 53.36): confirmed 23 instances / ₹12,344.12mn at Sep-25
  with waivers secured in only 9; 20 instances / ₹9,659.70mn at FY25 with waivers secured in only 5.
  Matches Pass 1 exactly.
- ARC-transfer footnote (p.393-394/614): confirmed verbatim — "Including written off loans amounting
  to Rs. 2593.7 millions in March, 2025 and Rs. 516.5 millions in March, 2023" — i.e. the entire FY25
  ARC transfer and 61.7% of the FY23 transfer were already written off before the transfer. Matches
  Pass 2's reconciliation of Pass 1's Finding #5 exactly.
- CRAR / Tier I capital table (Note 48, p.365/614, cross-checked against five other locations in the
  prospectus that repeat the same CRAR series): confirmed 37.61% (Sep-24) → 32.27% (Sep-25); Tier I
  capital ₹14,295.19mn (FY25) → ₹14,262.45mn (Sep-25). One new corroborating data point found in this
  pass: the prospectus separately discloses a **pro forma Post-Offer CRAR of 47.48%** (p.9125 of the
  extract line index, IPO-proceeds-adjusted) — confirming Pass 2's read that the CRAR fall is a
  capital-consumption trend that the IPO itself resolves, not an unaddressed capital shortfall.
- Going-concern language (extract lines ~20503/20519/27545/27553): confirmed standard boilerplate only
  ("The financial statements have been prepared on a going concern basis") in every location it
  appears; no material-uncertainty paragraph anywhere in the document. Matches Pass 2.

**One genuine pattern-level observation not previously named as such**: three of the highest-stakes
findings across Passes 1-2 (the Annexure VI tax restatement, the ₹290.51mn ARC security-receipt
impairment, and the ARC-transfer write-off status) each required cross-referencing between two or
three notes/annexures that do not reference one another (Note 40(b) tax reconciliation vs. Annexure VI;
Note 6 Investments vs. Annexure III Cash Flow vs. Note 28/30 P&L expense notes; the ARC principal table
vs. its own footnote). This is a **recurring disclosure-fragmentation pattern**, not three unrelated
coincidences — material adjustments are technically disclosed (nothing is hidden outright) but are
scattered such that no single note tells the full story. This pattern itself is weighed in the
disclosure-transparency score below, distinct from and in addition to the three underlying findings.

No further material new findings emerged from the pattern re-read beyond what Passes 1-2 already
surfaced and what is verified above.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS, RANKED BY INVESTOR IMPORTANCE

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Covenant breaches on loans/debt securities: 23 instances, ₹12,344.12mn (~23.6% of total borrowings of ₹52,184.98mn) at Sep-25, waivers secured in only 9 of 23 (14 unwaived); 20 instances/₹9,659.70mn at FY25 with only 5 of 20 waived. No detail given on covenant type (financial vs. reporting/technical) or lender identity. | Note 53.36, p.401-402/614 | 🔴 Red Flag | Cross-default/acceleration risk on nearly a quarter of the funding base; majority of instances remain unresolved at each period-end. |
| 2 | Recurring tax-expense restatement: FY23 audited PAT (₹537.96mn) cut 25.9% to ₹398.73mn (-₹139.23mn) in the restated financials used for this IPO; further tax-expense restatements in FY24 (+₹105.52mn, favourable) and FY25 (+₹39.80mn, favourable) — 4 of 5 presented periods carry a material prior-period tax correction, in both directions. Directly explains Pass 1's previously-unexplained FY23 "Others" tax-reconciliation item of ₹174.05mn (Note 40(b)). | Annexure VI, p.404/614; cross-ref Note 40(b), p.358/614 | 🔴 Red Flag | None of the three full restated years is free of a material prior-period tax correction; the FY23 base year of the IPO's growth track record is 26% lower than what was originally reported to the board/auditors at the time. |
| 3 | Stage 3 (GNPA) ratio, MSME sector, rising for 4 consecutive periods: 2.49% (FY23) → 3.19% (FY24) → 4.21% (FY25) → 4.85% (Sep-25). | Note 53.13.4, p.385/614 | 🔴 Red Flag | Sustained, multi-period credit-quality deterioration, not a one-off. |
| 4 | ECL rate on Stage 2 loans, Hypothecated/Switch book (~93% of the loan book), roughly tripled in one year: 13.90% (FY23) → 40.73% (FY24) → 43.31% (FY25) → 40.96% (Sep-25). No explanation given for whether this is genuine deterioration or a PD/LGD methodology recalibration. | Note 49.1.8(c), p.369/614 | 🔴 Red Flag | A step-change of this size, unexplained, is a fair-value/provisioning-methodology question mark that compounds finding #3. |
| 5 | Write-offs (net of recovery) nearly quadrupled: ₹500.00mn (FY23) → ₹529.20mn (FY24) → ₹2,034.89mn (FY25) → ₹1,462.03mn (H1FY26 alone, annualising to ~₹2,900mn). | Note 28, p.347/614 | 🔴 Red Flag | Confirms the Stage 3 migration is translating into realised credit losses, not just provisioning-model movement. |
| 6 | Restructured book: FY23→FY25 grew 262→401 borrowers (+53%)/₹24.30mn→₹40.93mn (+68%); then accelerated sharply WITHIN H1FY26 alone to 665 borrowers/₹67.50mn (+66% and +65% respectively in one half-year), on 317 fresh restructurings comparable in volume to the entire prior track record. Still small in absolute AUM terms (0.12% of gross loans). | Note 46 / 46.1, p.361-364/614 | 🔴 Red Flag | Rate of acceleration is the sharpest, most recent data point in the credit-stress pattern (#3-#5); the trend is worsening, not stabilising, into the most recent reported half-year. |
| 7 | CRAR fell from 37.61% (Sep-24, immediately post the ~₹1,858mn Sep-2024 equity raise) to 32.27% (Sep-25), a 5+ point drop in twelve months on a zero-Tier-II capital structure; Tier I capital was effectively flat/-0.23% within H1FY26 itself despite ₹645.97mn of profit earned in the same half. Comfortably above the RBI 15% minimum throughout; pro forma Post-Offer CRAR is 47.48% once IPO proceeds are applied. | Note 48, p.365/614 | 🟡 Watch | Genuine capital-consumption trend coinciding with the sharpest point of credit-quality deterioration (#3-#6); not a compliance risk given the IPO capital infusion, but a trajectory worth tracking post-listing. |
| 8 | ₹290.51mn ARC security-receipt impairment charge in FY25 (12.9% of FY25 PBT of ₹2,250.12mn) is not shown as a distinct line in any P&L expense note (Note 28's four sub-lines sum to the full ₹2,888.26mn impairment charge without it; Note 30 shows "Provision on investments" at ₹0 for FY25); visible only by differencing the Investments note's balance-sheet movement (Note 6) against the Cash Flow Statement's non-cash add-back (Annexure III) — two notes that do not cross-reference each other. | Note 6, p.329/614; Annexure III, p.315/614; Note 28, p.347/614; Note 30, p.348/614 | 🔴 Red Flag | A material (12.9% of PBT) charge is technically traceable but not transparently disclosed as a distinct P&L line; a disclosure-transparency gap on an amount this size ahead of listing. |
| 9 | NPA sales to ARCs — reconciled view: the FY25 transfer (₹2,593.70mn) was 100% already-written-off paper before the sale (a post-write-off recovery/monetisation event, economically similar to a recovery, not a mechanism that understates GNPA, since written-off loans are already excluded from the Stage 3 denominator). Only the smaller FY23 transfer's unwritten-off portion (₹321.10mn of ₹837.60mn) fits the original "moved off-book before recognition" concern. | Note 53.27.1(d)(i) + footnote, p.393-394/614 | 🟡 Watch (downgraded from Pass 1's 🔴 on the strength of the footnote) | Materially tempers the standalone GNPA-understatement reading of the FY25 ARC transaction; the residual concern is real but ~8x smaller (₹32.1 Cr, FY23 only) than the raw transfer amount suggested. |
| 10 | Ind AS 109 ECL provisioning exceeds the RBI IRACP regulatory minimum by ₹1,678.02mn (Sep-25) — running at 3.4x the regulatory floor — and this excess-over-floor cushion has grown ~5x since FY23 (₹346.50mn). | Note 52, p.382-384/614 | 🟢 Clean (mitigating strength) | A genuine, quantified offsetting strength against findings #3-#6: provisioning is materially conservative relative to the regulatory floor even as GNPA/write-offs/restructuring rise. |
| 11 | Credit-rating trajectory improving through the same window as the credit-quality flags: India Ratings upgrade to [IND] A/Stable from [IND] A-/Positive (Jul-2024); ICRA reaffirmed A/Stable with expanded bank-facility limits (Nov-2025); new international CareEdge Global rating (B+/Positive) for an ECB. | Note 53.11.4, p.390/614 | 🟢 Clean (mitigating strength) | An independent, external counter-signal to findings #3-#6 — rating agencies with visibility into the same credit book have not downgraded. |
| 12 | Customer complaints grew 405 (FY23) → 864 (FY24, +113%) → 1,612 (FY25, +87%) → 1,106 in H1FY26 alone (+60% YoY vs. H1FY25); pending complaints at period-end rose 4→12→49→69 over the same window. Ombudsman-tier (harder-escalation) complaints show the same pattern: 14 (FY23) → 31 (FY24) → 40 (FY25). | Note 53.16 / 53.16.1, p.386-390/614 | 🟡 Watch | Complaint growth outpacing loan-book growth in places (FY24 +113% vs. ~58% AUM growth), and rising at the harder Ombudsman escalation tier too, is consistent with (not proof of) collections-related friction alongside the credit-quality trend. |
| 13 | Auditor-identified ITGC gap: audit-trail (edit-log) features not enabled at the database level for part of FY24 for the loan-management software; remediated only from Sep-19-2024. No evidence of tampering found by the auditor. | Auditor's Examination Report, extract p.311-312/614 | 🟡 Watch | A control-environment observation independent of, and predating, the credit-quality/restatement findings; auditor found no misuse but the gap existed for a substantial part of a year now in the restated IPO track record. |
| 14 | Unsecured loan mix rose from 31.3% of gross loans (FY23) to 41.0% (Sep-25). | Note 5, p.328/614 | 🟡 Watch | A meaningful mix shift toward higher-risk unsecured lending, consistent with the MSME hypothecation/working-capital product growth, running in parallel with the credit-quality deterioration above. |
| 15 | Gain-on-derecognition (assignment/securitisation) income grew from ₹125.10mn (FY23) to ₹375.93mn (FY25), and ₹293.24mn in H1FY26 alone (already 78% of the full FY25 figure) — a legitimate but front-loaded, origination/sale-volume-linked income stream rather than the core NIM engine, becoming a larger share of reported profit as the assignment book scales. | Note 25 / 53.27, p.346, 393-394/614 | 🟡 Watch | Quality-of-earnings item: a growing share of profit is coming from day-one gain-on-sale accounting rather than recurring net interest margin. |

---

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | EIR-method interest recognition is standard and not aggressive (Note 2.4); however gain-on-derecognition income is a growing, front-loaded share of profit (#15) — legitimate treatment, but a quality-of-earnings watch item. |
| Expense capitalisation honesty | 8 | No capitalisation abuse found; ROU/lease accounting routine and growth-consistent (Note 2.5/50); ESOP fair-valuation standard and disclosed (Note 39). |
| Provisioning adequacy | 5 | Mixed: ECL cushion over the IRACP regulatory floor is strong and growing (#10, genuine strength), but the unexplained Stage 2 ECL methodology step-change (#4), rising GNPA (#3), quadrupled write-offs (#5), and accelerating restructuring (#6) together raise real questions about whether provisioning is keeping pace with underlying deterioration rather than just complying with the regulatory floor. |
| RPT fairness | 9 | No promoter; RPT compensation + CSR-via-subsidiary under 0.5% of revenue; MD remuneration 2.4% of PAT; all RPTs disclosed as arm's-length and Audit-Committee-reviewed; small KMP loan (₹3.32mn) is the only minor watch item. |
| Disclosure transparency | 4 | Materially hurt by the recurring disclosure-fragmentation pattern identified in Pass 3: the ₹290.51mn ARC-investment impairment (#8) is not shown as a distinct P&L line anywhere; the covenant-breach note (#1) gives no covenant-type or lender detail; the tax-restatement rationale (#2) is a boilerplate one-line explanation for adjustments touching 4 of 5 periods and up to 26% of a year's PAT. |
| Consistency with prior years | 4 | Tax-expense restatements in 4 of 5 presented periods (#2), an unexplained single-period Stage 2 ECL rate discontinuity (#4), and a discrete, unexplained jump in gratuity attrition assumptions in a single half-year (up-to-30yr band 33.10%→40.00%, above-44 band 6.20%→15.00% at Sep-25, Note 35.4) together represent more inconsistency across the restated track record than is typical for an IPO-stage filing. |
| **OVERALL** | **5.5** | Weighted toward the red-flag dimensions (provisioning adequacy, disclosure transparency, consistency) given the B00 context that credit-quality and provisioning mechanics are the primary signal for a lender. No evidence of fraud, tampering, or promoter-related leakage; audit opinions unmodified for every period; no going-concern language. But the covenant-breach severity, the recurring tax-restatement pattern spanning nearly the entire disclosed operating history, and the disclosure-fragmentation pattern on a material impairment charge are real, quantified dents that keep this out of "moderate" territory. |

---

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Covenant-breach acceleration/cross-default | High | Waiver status on the 14 instances unwaived at Sep-25 (₹12,344.12mn total breach amount); whether breach count/amount grows or shrinks at the next filing | Could crystallise at any time if a lender chooses to enforce; next data point is the first post-listing quarterly/annual filing |
| Credit-quality deterioration (GNPA, Stage 2 ECL, write-offs, restructuring) | High | Stage 3 %, Stage 2 ECL rate on the Hypothecated/Switch book, write-off run-rate, restructured-book growth rate | Ongoing; the trend has worsened in every one of the last 4-5 reported periods including the most recent half-year |
| Capital consumption (CRAR decline, Tier I stalling in H1FY26) | Medium | CRAR trend post-IPO-proceeds infusion; whether Tier I capital growth resumes tracking retained profit | Next 1-2 years; substantially mitigated by the ₹7,100mn+ IPO fresh-issue proceeds and the disclosed 47.48% pro forma Post-Offer CRAR |
| Recurring tax-provisioning restatements | Medium | Whether the FY26 (post-restated-track-record) tax line requires further prior-period correction; any disclosed process change in tax-provisioning controls | At the first post-listing annual filing |
| Disclosure fragmentation on material items | Medium | Whether post-listing annual reports disclose items like the ARC-investment impairment as a distinct P&L line, and give covenant-type/lender detail on breach disclosures | Ongoing; first test is the first post-listing annual report |

---

### D. FIVE QUESTIONS FOR MANAGEMENT

1. Of the 23 covenant-breach instances (₹12,344.12mn) outstanding at Sep-30-2025, which are financial covenants versus reporting/technical breaches, which lenders are involved, and what is the expected timeline to secure waivers on the 14 instances still unwaived? (Note 53.36, p.401-402/614)
2. What specifically drove the FY23 tax-expense restatement (-₹139.23mn, a 25.9% cut to that year's PAT), and what process or control changes have been made since to prevent the recurring prior-period tax corrections that appear in 4 of the 5 periods presented (Annexure VI)? (Annexure VI, p.404/614)
3. What caused the roughly 3x jump in the Stage 2 ECL rate on the Hypothecated/Switch book, from 13.90% (FY23) to 40.73% (FY24) and sustained since — a genuine deterioration in early-stage credit quality, or a PD/LGD model recalibration, and if the latter, what changed in the methodology? (Note 49.1.8(c), p.369/614)
4. Why is the ₹290.51mn ARC security-receipt impairment charge in FY25 (12.9% of FY25 PBT) not disclosed as a distinct line item in any of the P&L expense notes (Notes 21-30), and will this be broken out separately in future filings? (Note 6, p.329/614; Annexure III, p.315/614; Note 28, p.347/614)
5. What is driving the sharp acceleration in the restructured loan book within H1FY26 alone (401→665 borrowers, +66% in a single half-year, on fresh restructuring volume comparable to the entire FY23-FY25 track record) — is it concentrated in specific loan products, vintages, or geographies? (Note 46.1, p.361/614)

---

### E. NOTES-BASED RED FLAGS

- Covenant breaches on ~23.6% of total borrowings (₹12,344.12mn of ₹52,184.98mn) at Sep-25, with a majority of instances (14 of 23) unwaived; ₹9,659.70mn/20 instances at FY25 with 15 unwaived. No covenant-type or lender detail disclosed. (Note 53.36)
- Recurring tax-expense restatement pattern across 4 of 5 presented periods, including a 25.9% cut to FY23 PAT (₹537.96mn → ₹398.73mn) — the entire restated three-year track record used for the IPO carries at least one material prior-period tax correction. (Annexure VI)
- Stage 3 GNPA ratio rising for 4 consecutive periods: 2.49% → 3.19% → 4.21% → 4.85% (FY23 → Sep-25). (Note 53.13.4)
- Stage 2 ECL rate on the core Hypothecated/Switch book roughly tripled in one year (13.90% FY23 → 40.73% FY24) with no explanation given for the step-change. (Note 49.1.8(c))
- Write-offs (net of recovery) nearly quadrupled from ₹500.00mn (FY23) to ₹2,034.89mn (FY25), continuing at an elevated annualised pace into FY26. (Note 28)
- Restructured book accelerated sharply within H1FY26 alone: +66% in borrower count, +65% in amount, in a single half-year. (Note 46.1)
- ₹290.51mn ARC security-receipt impairment charge (12.9% of FY25 PBT) is not disclosed as a distinct line item in any P&L expense note; traceable only by cross-referencing the Investments note, the Cash Flow Statement, and the (silent) P&L expense notes. (Note 6; Annexure III; Note 28; Note 30)

**Not upgraded to a red flag, but material context**: the FY25 ARC transfer of ₹2,593.70mn was 100% already-written-off paper before the sale (Note 53.27.1(d)(i) footnote) — this is a recovery/monetisation event, not a GNPA-avoidance mechanism, and should not be read as compounding the GNPA-understatement concern. Only the FY23 transfer's ₹321.10mn unwritten-off portion carries that original concern, and it is small in absolute terms.

**No evidence found of**: earnings management via revenue recognition, undisclosed related-party leakage, promoter-related siphoning (no promoter exists), goodwill impairment gaming, undisclosed off-balance-sheet vehicles, hedge-accounting abuse, or going-concern doubt. Audit opinions are unmodified for every period presented; the one ITGC (audit-trail) gap found by the auditor was itself disclosed by the auditor with no evidence of tampering.

---

### F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices, fully disclosed but materially inconsistent across
the restated track record. Key concern: covenant breaches on ~24% of total borrowings with the
majority unwaived, layered on a tax-restatement pattern touching 4 of 5 presented periods and a
disclosure-fragmentation pattern that buries a 12.9%-of-PBT impairment charge outside any single P&L
note. Key strength: ECL provisioning running at 3.4x the RBI regulatory floor and growing, an improving
external credit-rating trajectory, and clean, immaterial, arm's-length related-party dealings with no
promoter to conflict against. Overall accounting quality: 5.5/10.

---

```yaml
stage: B02-notes
company: "AYE"
run_date: "2026-07-22"
model: claude-sonnet-5
status: complete
input_gaps:
  - "post-listing annual report absent (company listed Feb-2026, first AR not yet due); this Notes analysis is sourced entirely from the IPO Prospectus' Restated Financial Statements (Annexure V/VI), carried from B00"
  - "aye_screening_csv absent; no independent screener financial dataset to cross-check note-level figures against, carried from B00"
  - "operator 6-month digest (announcements) is NON-ANCHORED, lead/cross-check only; not used to source any figure in this Notes analysis, carried from B00"
flags:
  - type: FLAG-ASSET-QUALITY
    reason: "B02 reinforces and extends B01's FLAG-ASSET-QUALITY with note-level detail: Stage 3/GNPA (MSME sector) rose for 4 consecutive periods to 4.85% at Sep-25 (Note 53.13.4); Stage 2 ECL rate on the core book roughly tripled FY23->FY24 with no explanation (Note 49.1.8(c)); write-offs nearly quadrupled FY23->FY25 (Note 28); restructured book accelerated +66% WITHIN H1FY26 alone (Note 46.1). New and adjacent to this flag: covenant breaches on ~23.6% of total borrowings, majority unwaived (Note 53.36) — a funding/liquidity risk correlated with, though distinct from, the credit-quality deterioration."
  - type: FLAG-DATA
    reason: "B02 corroborates and quantifies B01's FLAG-DATA restatement-uplift observation with the exact source mechanism: Annexure VI shows FY24 PAT restated UP +Rs105.52mn (+6.5%) and FY25 PAT restated UP +Rs39.80mn (+2.3%) via prior-period tax-expense adjustments -- consistent with B01's independently-derived ~6.6%/~2.3% deltas vs ICRA's originally-audited PAT. New finding not in B01: FY23 PAT was restated DOWN -Rs139.23mn (-25.9%, Rs537.96mn->Rs398.73mn) via the same tax-expense mechanism, and a further small adjustment appears in H1FY26 (-Rs5.21mn). The restatement pattern touches 4 of 5 presented periods."
  - type: FLAG-CASH
    reason: "No trade receivables/working-capital concept exists for this lending NBFC (NOT APPLICABLE per B00 context); B02 does not add new evidence to B01's CFO-structural-negative determination. The credit-quality-equivalent trend (Stage 3/GNPA, write-offs, restructuring -- see FLAG-ASSET-QUALITY above) is deteriorating across the same window, which is a different signal from cash conversion but should be read alongside it; B01's INDETERMINATE cash-conversion read is not resolved by anything found in the notes and should not be silently upgraded to PROCEED."
accounting_quality: 5.5
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Covenant breaches on ~23.6% of total borrowings (Rs12,344.12mn of Rs52,184.98mn) at Sep-25, majority unwaived (9 of 23 waived)", note_ref: "Note 53.36, p.401-402/614", rating: "🔴", why: "Cross-default/acceleration risk on nearly a quarter of the funding base; unresolved at each period-end"}
  - {rank: 2, finding: "Recurring tax-expense restatement: FY23 PAT cut 25.9% (Rs537.96mn->Rs398.73mn); adjustments in 4 of 5 periods presented, both directions", note_ref: "Annexure VI, p.404/614; cross-ref Note 40(b), p.358/614", rating: "🔴", why: "No presented full year of the IPO growth track record is free of a material prior-period tax correction"}
  - {rank: 3, finding: "Stage 3/GNPA ratio rising 4 consecutive periods: 2.49%->3.19%->4.21%->4.85% (FY23->Sep-25)", note_ref: "Note 53.13.4, p.385/614", rating: "🔴", why: "Sustained multi-period credit-quality deterioration"}
  - {rank: 4, finding: "Stage 2 ECL rate on core Hypothecated/Switch book roughly tripled FY23->FY24 (13.90%->40.73%), stayed elevated, unexplained", note_ref: "Note 49.1.8(c), p.369/614", rating: "🔴", why: "Unexplained step-change is a provisioning-methodology question mark compounding the GNPA trend"}
  - {rank: 5, finding: "Write-offs nearly quadrupled: Rs500.00mn (FY23) -> Rs2,034.89mn (FY25), elevated pace continuing into FY26", note_ref: "Note 28, p.347/614", rating: "🔴", why: "Confirms Stage 3 migration is translating into realised credit losses"}
  - {rank: 6, finding: "Restructured book accelerated +66% in borrowers/+65% in amount WITHIN H1FY26 alone (401->665 borrowers)", note_ref: "Note 46/46.1, p.361-364/614", rating: "🔴", why: "Sharpest, most recent data point in the credit-stress pattern; still small vs AUM (0.12%) but accelerating"}
  - {rank: 7, finding: "CRAR fell 37.61% (Sep-24) -> 32.27% (Sep-25); Tier I capital flat/-0.23% within H1FY26 despite profit earned", note_ref: "Note 48, p.365/614", rating: "🟡", why: "Capital-consumption trend coinciding with sharpest credit deterioration; mitigated by IPO proceeds (pro forma Post-Offer CRAR 47.48%)"}
  - {rank: 8, finding: "Rs290.51mn ARC security-receipt impairment (12.9% of FY25 PBT) not shown as a distinct line in any P&L note", note_ref: "Note 6 p.329/614; Annexure III p.315/614; Note 28 p.347/614; Note 30 p.348/614", rating: "🔴", why: "Material charge traceable only by cross-referencing three notes that do not reference each other"}
  - {rank: 9, finding: "NPA-to-ARC sales reconciled: FY25 Rs2,593.70mn transfer was 100% already-written-off (recovery event); only FY23 Rs321.10mn unwritten-off portion fits the original GNPA-understatement concern", note_ref: "Note 53.27.1(d)(i) + footnote, p.393-394/614", rating: "🟡", why: "Materially tempers the raw transfer amount's implied severity; residual concern real but ~8x smaller and FY23-only"}
  - {rank: 10, finding: "Ind AS 109 ECL provisioning exceeds RBI IRACP floor by Rs1,678.02mn (Sep-25), 3.4x the floor, cushion grown ~5x since FY23", note_ref: "Note 52, p.382-384/614", rating: "🟢", why: "Genuine offsetting strength against the credit-quality flags"}
  - {rank: 11, finding: "Credit-rating trajectory improving through the same window: IndRa upgrade to A/Stable (Jul-2024), ICRA reaffirmed A/Stable with expanded limits (Nov-2025)", note_ref: "Note 53.11.4, p.390/614", rating: "🟢", why: "Independent external counter-signal to the credit-quality flags"}
  - {rank: 12, finding: "Customer complaints and Ombudsman-tier complaints both rising faster than the book in places (FY24 complaints +113% vs ~58% AUM growth)", note_ref: "Note 53.16 / 53.16.1, p.386-390/614", rating: "🟡", why: "Consistent with, not proof of, collections-related friction alongside the credit-quality trend"}
  - {rank: 13, finding: "Auditor-identified ITGC gap: audit-trail not enabled at database level for part of FY24, remediated from Sep-19-2024, no tampering found", note_ref: "Auditor's Examination Report, extract p.311-312/614", rating: "🟡", why: "Control-environment observation in the restated IPO track record"}
  - {rank: 14, finding: "Unsecured loan mix rose from 31.3% (FY23) to 41.0% (Sep-25) of gross loans", note_ref: "Note 5, p.328/614", rating: "🟡", why: "Mix shift toward higher-risk unsecured lending running parallel to the credit-quality deterioration"}
  - {rank: 15, finding: "Gain-on-derecognition income grew Rs125.10mn (FY23) to Rs375.93mn (FY25), front-loaded and growing as a share of profit", note_ref: "Note 25/53.27, p.346, 393-394/614", rating: "🟡", why: "Quality-of-earnings item: growing share of profit from day-one gain-on-sale rather than recurring NIM"}
red_flags:
  - "Covenant breaches on ~23.6% of total borrowings (Rs12,344.12mn of Rs52,184.98mn) at Sep-25, majority unwaived (Note 53.36)"
  - "Recurring tax-expense restatement across 4 of 5 presented periods, including a 25.9% cut to FY23 PAT (Annexure VI)"
  - "Stage 3/GNPA ratio rising 4 consecutive periods, 2.49%->4.85% FY23->Sep-25 (Note 53.13.4)"
  - "Stage 2 ECL rate on the core book roughly tripled in one year with no explanation given (Note 49.1.8(c))"
  - "Write-offs nearly quadrupled FY23->FY25, elevated pace continuing into FY26 (Note 28)"
  - "Restructured book accelerated +66% within H1FY26 alone (Note 46.1)"
  - "Rs290.51mn ARC security-receipt impairment (12.9% of FY25 PBT) not disclosed as a distinct P&L line item (Note 6; Annexure III; Note 28; Note 30)"
questions_for_mgmt:
  - "Of the 23 covenant-breach instances (Rs12,344.12mn) at Sep-30-2025, which are financial vs reporting/technical breaches, which lenders are involved, and what is the timeline to waiver on the 14 unwaived instances? (Note 53.36)"
  - "What specifically drove the FY23 tax-expense restatement (-Rs139.23mn, -25.9% of PAT), and what process changes prevent the recurring prior-period tax corrections appearing in 4 of 5 periods presented? (Annexure VI)"
  - "What caused the ~3x jump in the Stage 2 ECL rate on the Hypothecated/Switch book (13.90% FY23 -> 40.73% FY24, sustained since) -- genuine deterioration or a PD/LGD methodology recalibration? (Note 49.1.8(c))"
  - "Why is the Rs290.51mn ARC security-receipt impairment charge in FY25 (12.9% of FY25 PBT) not disclosed as a distinct P&L line item, and will it be broken out separately in future filings? (Note 6; Annexure III; Note 28)"
  - "What is driving the sharp acceleration in restructured accounts within H1FY26 alone (401->665 borrowers, +66% in one half-year) -- specific products, vintages, or geographies? (Note 46.1)"
receivables_trend: "NOT APPLICABLE -- lending NBFC, no trade receivables. Credit-quality equivalent (Stage 3/GNPA, MSME sector) is deteriorating: 2.49% (FY23) -> 3.19% (FY24) -> 4.21% (FY25) -> 4.85% (Sep-25), rising for 4 consecutive periods (Note 53.13.4, p.385/614); net NPA/net advances also rose the last two periods, 0.91% (FY24) -> 1.40% (FY25) -> 1.78% (Sep-25) (Note 53.13.5(a), p.385/614)"
restatements_found:
  - "FY23 PAT restated DOWN 25.9%: Rs537.96mn (audited) -> Rs398.73mn (restated), -Rs139.23mn, entirely a tax-expense prior-period adjustment (Annexure VI, p.404/614)"
  - "FY24 PAT restated UP 6.5%: Rs1,611.27mn (audited) -> Rs1,716.79mn (restated), +Rs105.52mn, tax-expense adjustment (Annexure VI, p.404/614)"
  - "FY25 PAT restated UP 2.3%: Rs1,712.72mn (audited) -> Rs1,752.52mn (restated), +Rs39.80mn, tax-expense adjustment (Annexure VI, p.404/614)"
  - "H1FY26 PAT restated DOWN 0.8%: Rs651.18mn (audited) -> Rs645.97mn (restated), -Rs5.21mn, tax-expense adjustment (Annexure VI, p.404/614)"
  - "Equity restated DOWN at FY23 (-Rs140.11mn, Rs7,685.04mn -> Rs7,544.93mn) and at April-01-2022 opening (-Rs0.88mn); mixed direction at FY24 (-Rs34.59mn) and Sep-24 (-Rs34.59mn), consistent with the PAT-level tax adjustments carried into opening reserves (Annexure VI, p.404/614)"
going_concern_language: "NONE -- standard boilerplate only ('The financial statements have been prepared on a going concern basis'), confirmed at every location it appears in the extract (lines ~20503, 20519, 27545, 27553); no material-uncertainty paragraph anywhere in the document"
```
