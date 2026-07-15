# FEDFINA — Stage 2: Notes to Financial Statements, PASS 3 OF 3 (Pattern Pass + Consolidation)
Company: Fedbank Financial Services Ltd (FEDFINA) | Run date: 2026-07-15
Source: runs/fedfina-2026-07-15/derived/annual-report.txt (FY2024-25 Annual Report, standalone
financial statements, Notes 1-59, printed pages 174-258 / PDF pages 90-132). RHP backup at
runs/fedfina-2026-07-15/derived/RHP-prospectus.txt not required for this pass (all figures sourced
from the current-year audited Notes). Figures quoted in ₹ Lakhs from source, with ₹ Crore
equivalent in parentheses. Input gaps carried forward: announcements feed absent; screening-fedfina
not available to this stage; RHP used as prospectus backup in place of a dedicated prospectus
folder; FY26 AR notes not yet published (no forward look possible).

---

## PASS 3: PATTERN RE-READ (contradictions, mismatches, vague disclosure, restatements, subsequent events, going concern)

- **Stage 3 figure does not tie across three notes.** Note 48.09/48.30(A) states aggregate Ind AS
  Stage 3 (credit-impaired) gross loans of ₹23,888 Lakh. Separately, Note 8.3(a) (amortised cost,
  ₹19,475 Lakh) + Note 8(d) (FVOCI, ₹7,127 Lakh) sum to ₹26,602 Lakh — a ₹2,714 Lakh gap already
  surfaced in Pass 1 (Section 12) as a reconciliation item. Pass 2's NPA-vintage sub-buckets from
  the **same** Note 48.30(A) table (Sub-Standard ₹15,124L + Doubtful 1-3yr ₹3,467L + Doubtful >3yr
  ₹45L + Loss ₹406L) sum to only ₹19,042 Lakh — a **third, different total**, ₹4,846 Lakh short of
  the ₹23,888 Lakh headline in the very same note. None of the three totals (₹19,042L / ₹23,888L /
  ₹26,602L) are bridged explicitly anywhere in the Notes; the gold-loan "Stage 2*" rebuttal
  footnote in Note 48.30(A) is the only clue offered and does not fully explain a gap of this size.
  This is a genuine disclosure-quality pattern finding: the RBI IRACP asset-classification bucket
  (Sub-Standard/Doubtful/Loss) and the Ind AS 109 Stage 3 population are evidently drawn from
  different scopes, and the document does not walk an investor through the bridge. 🟡 New pattern
  finding (Notes 48.09, 48.30(A), 8.3(a), 8(d), p.191-192, 238, 248-250).
- **Vague restatement disclosure confirmed on re-read.** Note 59 (p.258): "prior year figures have
  been regrouped/reclassified, wherever considered necessary," with no line items or amounts
  named. Cross-checked against the primary statements and Notes 4-31 line-by-line; no specific
  regrouped balance could be independently traced from the disclosure as given. This is boilerplate
  without quantification, not evidence of a specific irregularity, but it fails the "specifics of
  what was regrouped" test on a second read. 🟡 (confirms Pass 1 Section 1 finding, no new content)
- **Auditor transition (Note 34.1) re-checked against the rest of the document:** no other note
  cross-references the change (no separate "change of auditor" note, no reason disclosed within the
  Notes). This is consistent with the item already raised in Pass 2; nothing further found on the
  pattern pass.
- **No going-concern qualifying language anywhere** in the Notes on this final re-read (searched for
  "going concern," "material uncertainty," "ability to continue" — none found beyond the routine,
  unqualified reference in Note 40, Capital Management, that the company has complied in full with
  externally imposed capital requirements). NONE.
- **No subsequent/events-after-balance-sheet-date note number exists** within the Notes to Financial
  Statements (confirmed again on this pass — Note 59 is the last note and deals only with rounding/
  regrouping). Any post-year-end items (e.g., governance changes) sit outside the Notes and outside
  this stage's scope, as already noted in Pass 1.
- **No further contradictions found** between the credit-cost narrative (Note 32, provisioning
  surge) and the write-off data (Note 50, write-offs down 14.0% YoY) beyond what Pass 2 already
  captured as a genuine offsetting data point — re-reading both notes side by side confirms the
  provisioning increase is being driven by Stage 1/2 overlay and Stage 3 ECL coverage increases
  (Note 44.1.2), not by a wave of realised write-offs, which is internally consistent rather than
  contradictory.

No further material items beyond the Stage 3 three-way reconciliation gap above emerged from the
pattern re-read. This item is added to Section A below; no other new findings from Pass 3.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS (ranked by investor importance)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Impairment on financial instruments (credit-cost P&L charge) surged 228.6% YoY, ₹65.85 Cr → ₹216.36 Cr — the primary driver of an 8.0% PAT decline despite 29.0% interest-income growth | Note 32, p.208 | 🔴 Red Flag | Direct earnings driver; asset-quality deterioration is now the dominant swing factor in the P&L |
| 2 | NPA vintage aging: Doubtful (1-3yr) bucket up 292.6% YoY (₹8.83 Cr → ₹34.67 Cr); Doubtful (>3yr) newly appeared at ₹0.45 Cr — the oldest Stage 3 tranche is not resolving, distinct from simply "more Stage 3" | Note 48.30(A), p.248-249 | 🔴 Red Flag | Slower workout/recovery signal, harder to reverse than fresh slippage |
| 3 | FVOCI-book Stage 3 loans exploded 2,027.5% YoY (₹3.35 Cr → ₹71.27 Cr), materially faster migration than the already-elevated amortised-cost Stage 3 book | Note 8(d)/(f), 44.1.2(b), p.192-193, 227 | 🔴 Red Flag | Extreme base-effect growth but concentrated in the assigned/off-book-adjacent portfolio; a distinct, previously unflagged stress pocket |
| 4 | Customer complaints surged 897.3% YoY (37 → 369), led by "Issuance of Foreclosure Letter" complaints up 1,508% (12 → 193) — an operations/process signal not yet reflected in ECL numbers | Note 48.17, p.242-243 | 🔴 Red Flag | Leading indicator of collections-process strain that could feed into future credit costs or regulatory scrutiny |
| 5 | Standard-asset (Stage 1&2) provisioning rose 792.7% YoY (₹8.26 Cr → ₹73.73 Cr); Ind AS-over-IRACP provisioning buffer rose 7.1x (₹13.84 Cr → ₹98.79 Cr) — the single largest swing in the provisioning note, a disclosed forward-looking overlay | Note 48.15 / 48.30(A), p.243, 249-250 | 🔴 Red Flag | Large, judgment-driven P&L item; conservative in intent but scale of swing itself is a material disclosure |
| 6 | Funding mix shifted sharply to short-tenor, on-demand borrowing (WCDL/CC/OD +331.6% YoY, ₹761.2 Cr → ₹3,285.2 Cr); CRAR declined 23.46% → 21.92%; asset-liability net position in the >1-year bucket swung to -₹529.27 Cr from +₹60.04 Cr | Note 17/42/48.29-31, p.199-201, 222, 244-251 | 🟡 Watch | Refinancing/rollover risk building even though LCR (150%) and CRAR (21.92%) remain within regulatory bounds today |
| 7 | Related-party dependency on parent Federal Bank intensified (term loans +39.9%, interest paid +71.8%); a new, unexplained "Brand Usage Charges" RPT line of ₹2.44 Cr appeared with no prior-year comparative or disclosed basis | Note 39.2/39.3, p.216-217 | 🟡 Watch | Federal Bank is now the single largest funding counterparty at 12.47% of total liabilities; concentration + an unexplained new fee are both worth tracking |
| 8 | Direct assignment income +66.9% YoY (₹91.24 Cr → ₹152.31 Cr) outpaced on-book loan growth; income recognised upfront per policy; retained beneficial interest narrowed to a 5%/10% range | Note 26/48.04, p.206, 235-236 | 🟡 Watch | Revenue-quality/timing item: more loans sold with less retained skin-in-the-game, gains booked upfront |
| 9 | Real estate exposure (residential mortgage + commercial RE) = ₹5,616.05 Cr, 47.4% of the gross loan book — previously unquantified in the Notes despite FEDFINA's "diversified lender" positioning | Note 48.08, p.238 | 🟡 Watch | Single largest asset-class concentration; absolute exposure still growing even as its book share declines |
| 10 | Restructured loan book resolved 89.9% via write-off (3 of 4 borrowers, ₹2.57 Cr of ₹2.86 Cr opening balance) rather than cure/upgrade to standard during the year | Note 49, p.252 | 🟡 Watch | Small in absolute size but a negative signal on restructuring recovery quality |
| 11 | Mid-year statutory auditor transition disclosed only via a remuneration footnote ("includes remuneration paid to previous Auditors"); no reason or fee-split given within the Notes | Note 34.1, p.209 | 🟡 Watch | Governance item at a recently listed (Nov-2023) NBFC warranting independent verification outside Notes scope |
| 12 | Net interest-rate sensitivity worsened 24.5% YoY: a +25bps parallel shock now cuts PAT by ₹11.19 Cr (FY24: ₹8.99 Cr), reflecting rising liability-side rate exposure | Note 44.3.2, p.229 | 🟡 Watch | Confirms the funding-mix shift (finding #6) is translating into real earnings sensitivity |
| 13 | Stage 3 gross-loan figure cannot be reconciled across three separate notes in the same document: ₹19,042L (NPA vintage sub-buckets) vs ₹23,888L (headline Ind AS Stage 3) vs ₹26,602L (sum of Note 8.3(a)+8(d)) — no bridge given | Notes 48.09, 48.30(A), 8.3(a), 8(d), p.191-192, 238, 248-250 | 🟡 Watch (Pass 3 pattern finding) | Disclosure-transparency gap on the single most important asset-quality metric in the document |
| 14 | Gold loan "90-day rebuttal" mechanism kept ₹77.56 Cr of 90+DPD accounts out of Stage 3 on collateral-sufficiency judgment (RBI-permitted carve-out); auction activity rose alongside (accounts +19.7%, value fetched +27.5%) | Note 48.28, 48.30(B), p.243-244, 250 | 🟡 Watch | Genuine judgment-dependent staging area; consistency of application over time needs tracking |
| 15 | Gross loan write-offs actually declined 14.0% YoY (₹46.03 Cr → ₹39.58 Cr) even as provisioning surged — supports a forward-looking-overlay reading of the credit-cost increase rather than a realised-loss reading | Note 50, p.252 | 🟢 Clean/Positive | Genuine offsetting data point; realised losses have not (yet) risen in tandem with the provisioning build |

### B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score /10 | Rationale |
|---|---|---|
| Revenue recognition conservatism | 6 | Standard EIR-based interest recognition (🟢), but DA income upfront-recognition growing faster than the book with narrowing retained interest is a genuine judgment-heavy area (Note 26, 48.04) |
| Expense capitalisation honesty | 8 | PPE/intangible useful lives match Schedule II exactly, no revaluation; ROU/lease policy standard; rising rent/collection-agency costs are expensed, not capitalised aggressively (Notes 3.3-3.4, 34, 47) |
| Provisioning adequacy | 7 | Large FY25 swing (Stage 1&2 +792.7%, IRACP buffer 7.1x) reads as conservative overlay-building corroborated by declining realised write-offs (Note 50), but the NPA-vintage aging and FVOCI Stage 3 explosion (findings #2, #3) raise the question of whether even this larger buffer is sufficient |
| RPT fairness | 6 | No loans to promoters/KMP, no covenant breaches, arm's-length framing generally maintained, but the new unexplained Brand Usage Charge and intensifying parent-funding dependency are watch items (Note 39) |
| Disclosure transparency | 7 | Very granular in most areas (ALM, EaR, LCR, CRAR, NPA vintage, ECL model description) but the un-bridged Stage 3 reconciliation across three notes (finding #13), vague regrouping boilerplate (Note 59), and the undisclosed auditor-transition reason (Note 34.1) pull the score down |
| Consistency with prior years | 8 | No accounting policy changes disclosed (Note 48.14); consistent staging methodology and actuarial approach year over year; the changes seen are in the underlying risk profile (funding mix, asset quality), not in accounting method |
| **OVERALL** | **7** | Disclosure is dense and largely grounded, provisioning looks genuinely conservative on balance, but real asset-quality and funding-tenor stress is emerging and one internal reconciliation on the single most important credit metric does not tie out |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Asset-quality deterioration (NPA vintage aging + FVOCI Stage 3 explosion) | High | Stage 3 ratios, NPA vintage buckets, FVOCI Stage 3 balance in FY26 Notes | Already visible in FY25; could compound in FY26 if the current overlay proves insufficient |
| Funding-tenor mismatch (short-tenor shift, negative >1yr ALM gap) | Medium-High | LCR, ALM maturity buckets, CP rollover, CRAR trend | Refinancing events over FY26-27, amplified in a tighter credit-market scenario |
| Related-party/parent funding concentration (Federal Bank, 12.47% of total liabilities) plus an unexplained new RPT fee | Medium | Note 39 RPT table, funding-cost trend from Federal Bank | If parent relationship terms or funding appetite change |
| Operational/process quality (complaint surge, especially foreclosure-letter related) | Medium | Complaint volumes and categories, Ombudsman cases | Could translate into regulatory action or additional provisioning if the root cause is not remediated |
| Real estate concentration (~47% of gross loan book) | Medium | Absolute Rupee growth of RE exposure vs total book | A property-market downturn scenario |
| Governance disclosure gaps (undisclosed auditor-transition reason; un-bridged Stage 3 figures) | Low-Medium | AGM disclosures, FY26 Notes for a clearer Stage 3 bridge | Ongoing; watch for repeat of the same disclosure gaps next year |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. What is the quantum basis and commercial rate for the new "Brand Usage Charges" of ₹2.44 Cr paid to Federal Bank this year, and why does this line item have no prior-year comparative or disclosed methodology (Note 39.2)?
2. What drove the mid-year statutory auditor transition referenced in Note 34.1 ("includes remuneration paid to previous Auditors"), and can management confirm there was no disagreement with the outgoing auditor over financial reporting matters?
3. Given the 792.7% YoY rise in standard-asset (Stage 1&2) provisioning and the 7.1x rise in the Ind AS-over-IRACP buffer, which specific portfolio segments or macro overlay assumptions drove this build, and what portion of it is expected to reverse versus convert into realised losses in FY26 (Note 48.15/48.30(A))?
4. What is the root cause of the 897.3% surge in customer complaints, particularly the 1,508% rise in foreclosure-letter complaints, and what operational remediation is underway (Note 48.17)?
5. Can management reconcile the three different Stage 3 gross-loan totals disclosed in the Notes — ₹19,042 Lakh (NPA vintage sub-buckets, Note 48.30(A)), ₹23,888 Lakh (headline Ind AS Stage 3, Note 48.09/48.30(A)), and ₹26,602 Lakh (sum of Note 8.3(a) + Note 8(d)) — and provide the bridge that ties these together?

### E. NOTES-BASED RED FLAGS

- **Earnings deterioration driven by credit cost, not operations:** the 228.6% YoY impairment surge (Note 32) is the dominant driver of an 8.0% PAT decline despite 29.0% revenue growth — a genuine asset-quality signal, not an accounting-policy artifact.
- **NPA vintage aging** (Doubtful 1-3yr +292.6%, first-ever >3yr Doubtful bucket) and the **2,027.5% FVOCI Stage 3 explosion** together indicate stress is broadening beyond what the aggregate Stage 3 growth rate alone would suggest (Notes 48.30(A), 8(d)/(f)).
- **Undisclosed risk indicator:** customer complaint surge (+897.3%), concentrated in foreclosure-letter issues, is an operational red flag not yet reflected in the ECL model (Note 48.17).
- **Judgment-heavy, large-magnitude provisioning swing** (Stage 1&2 +792.7%) — while corroborated by a declining realised write-off rate (a genuine offsetting positive), the sheer scale of a management-overlay-driven charge in a single year is a disclosure item investors should track for repeatability (Note 48.15).
- **Disclosure-quality flag, not earnings management:** the Stage 3 gross-loan figure does not reconcile across three notes in the same document (finding #13); this is a transparency gap on the single most important credit metric rather than evidence of manipulated numbers, but it should be resolved by management/auditors in FY26.
- No evidence of round-tripping, premature revenue recognition outside the disclosed DA-upfront policy, undisclosed contingent liabilities, or reserve bypass; RPTs are largely arm's length save for the two watch items above (Brand Usage Charges, funding concentration).

### F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices with genuine, broadening asset-quality stress.
Key concern: NPA vintage aging and a 2,027.5% FVOCI Stage 3 explosion sit alongside a 228.6% credit-cost surge and an unreconciled Stage 3 figure across three notes. Key strength: transparently disclosed, apparently conservative forward-looking provisioning corroborated by a 14.0% decline in realised write-offs, clean RPT-loan/covenant/RBI-divergence discipline, and no policy changes or going-concern language. Overall accounting quality: 7/10.

---

```yaml
stage: B02-notes
company: "FEDFINA"
run_date: "2026-07-15"
model: claude-sonnet-5
status: complete
input_gaps: ["announcements feed absent", "screening-fedfina not available", "RHP used as prospectus-folder backup", "FY26 AR notes not yet published"]
flags:
  - {type: FLAG-CASH, reason: "Trade receivables >6-month ageing bucket worsened to 23.5% of gross (Note 7, p.189-190) from ~16.0% in FY24 even as absolute net receivables shrank 44.1% YoY (Rs 34.52 Cr to Rs 19.31 Cr); immaterial in absolute size relative to balance sheet but flagged per receivables_trend rule. Core loan-book asset quality (Stage 3/NPA vintage) is a separate, more material concern captured in red_flags below, not this trade-receivables item."}
accounting_quality: 7        # /10
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Impairment on financial instruments (credit-cost charge) surged 228.6% YoY, Rs 65.85 Cr to Rs 216.36 Cr, the primary driver of an 8.0% PAT decline despite 29.0% interest-income growth", note_ref: "Note 32, p.208", rating: "Red Flag"}
  - {rank: 2, finding: "NPA vintage aging: Doubtful (1-3yr) bucket up 292.6% YoY (Rs 8.83 Cr to Rs 34.67 Cr); Doubtful (>3yr) newly appeared at Rs 0.45 Cr, indicating the oldest Stage 3 tranche is not resolving", note_ref: "Note 48.30(A), p.248-249", rating: "Red Flag"}
  - {rank: 3, finding: "FVOCI-book Stage 3 loans exploded 2,027.5% YoY (Rs 3.35 Cr to Rs 71.27 Cr), materially faster than the amortised-cost book's Stage 3 growth", note_ref: "Note 8(d)/(f), 44.1.2(b), p.192-193, 227", rating: "Red Flag"}
  - {rank: 4, finding: "Customer complaints surged 897.3% YoY (37 to 369), led by Issuance of Foreclosure Letter complaints up 1,508% (12 to 193), an operations signal not yet in the ECL numbers", note_ref: "Note 48.17, p.242-243", rating: "Red Flag"}
  - {rank: 5, finding: "Standard-asset (Stage 1&2) provisioning rose 792.7% YoY (Rs 8.26 Cr to Rs 73.73 Cr); Ind AS-over-IRACP buffer rose 7.1x (Rs 13.84 Cr to Rs 98.79 Cr), the single largest swing in the provisioning note", note_ref: "Note 48.15 / 48.30(A), p.243, 249-250", rating: "Red Flag"}
  - {rank: 6, finding: "Funding mix shifted sharply to short-tenor on-demand borrowing (+331.6% YoY); CRAR declined 23.46% to 21.92%; asset-liability net position beyond 1 year swung to -Rs 529.27 Cr from +Rs 60.04 Cr", note_ref: "Note 17/42/48.29-31, p.199-201, 222, 244-251", rating: "Watch"}
  - {rank: 7, finding: "Related-party dependency on parent Federal Bank intensified (term loans +39.9%, interest paid +71.8%); a new unexplained Brand Usage Charges RPT line of Rs 2.44 Cr appeared with no prior-year comparative or disclosed basis", note_ref: "Note 39.2/39.3, p.216-217", rating: "Watch"}
  - {rank: 8, finding: "Direct assignment income +66.9% YoY (Rs 91.24 Cr to Rs 152.31 Cr) outpaced on-book loan growth, recognised upfront, with retained beneficial interest narrowing to 5%/10%", note_ref: "Note 26/48.04, p.206, 235-236", rating: "Watch"}
  - {rank: 9, finding: "Real estate exposure = Rs 5,616.05 Cr, 47.4% of gross loan book, previously unquantified within the Notes", note_ref: "Note 48.08, p.238", rating: "Watch"}
  - {rank: 10, finding: "Restructured loan book resolved 89.9% via write-off rather than cure/upgrade to standard during the year", note_ref: "Note 49, p.252", rating: "Watch"}
  - {rank: 11, finding: "Mid-year statutory auditor transition disclosed only via a remuneration footnote, no reason or fee-split given within the Notes", note_ref: "Note 34.1, p.209", rating: "Watch"}
  - {rank: 12, finding: "Net interest-rate sensitivity worsened 24.5% YoY: a +25bps shock now cuts PAT by Rs 11.19 Cr versus Rs 8.99 Cr in FY24", note_ref: "Note 44.3.2, p.229", rating: "Watch"}
  - {rank: 13, finding: "Stage 3 gross-loan figure does not reconcile across three notes: Rs 19,042L (NPA vintage sub-buckets) vs Rs 23,888L (headline Ind AS Stage 3) vs Rs 26,602L (sum of Note 8.3(a)+8(d)), no bridge given", note_ref: "Notes 48.09, 48.30(A), 8.3(a), 8(d), p.191-192, 238, 248-250", rating: "Watch"}
  - {rank: 14, finding: "Gold loan 90-day rebuttal mechanism kept Rs 77.56 Cr of 90+DPD accounts out of Stage 3 on collateral-sufficiency judgment; auction activity rose alongside", note_ref: "Note 48.28, 48.30(B), p.243-244, 250", rating: "Watch"}
  - {rank: 15, finding: "Gross loan write-offs declined 14.0% YoY even as provisioning surged, supporting a forward-looking-overlay reading of the credit-cost increase", note_ref: "Note 50, p.252", rating: "Clean/Positive"}
red_flags:
  - "Impairment/credit-cost charge +228.6% YoY (Note 32) is the primary driver of the PAT decline, a genuine asset-quality signal"
  - "NPA vintage aging: Doubtful 1-3yr bucket +292.6%, first-ever Doubtful >3yr bucket appeared (Note 48.30(A))"
  - "FVOCI-book Stage 3 loans +2,027.5% YoY, a distinct and previously unflagged stress pocket (Note 8(d)/(f))"
  - "Customer complaints +897.3% YoY, concentrated in foreclosure-letter issues, an operational red flag not yet in the ECL model (Note 48.17)"
  - "Standard-asset provisioning swing of 792.7% YoY is judgment-heavy and large in magnitude even though corroborated by declining realised write-offs (Note 48.15, Note 50)"
  - "Stage 3 gross-loan figure does not reconcile across three notes in the same document, a disclosure-transparency gap on the single most important credit metric (Notes 48.09, 48.30(A), 8.3(a), 8(d))"
questions_for_mgmt:
  - "What is the quantum basis and commercial rate for the new Brand Usage Charges of Rs 2.44 Cr paid to Federal Bank, and why does this line have no prior-year comparative or disclosed methodology (Note 39.2)?"
  - "What drove the mid-year statutory auditor transition (Note 34.1), and can management confirm there was no disagreement with the outgoing auditor over financial reporting matters?"
  - "Which portfolio segments or macro overlay assumptions drove the 792.7% rise in Stage 1&2 provisioning, and what portion is expected to reverse versus convert into realised losses in FY26 (Note 48.15/48.30(A))?"
  - "What is the root cause of the 897.3% surge in customer complaints, particularly the 1,508% rise in foreclosure-letter complaints, and what operational remediation is underway (Note 48.17)?"
  - "Can management reconcile the three different Stage 3 gross-loan totals in the Notes (Rs 19,042L vs Rs 23,888L vs Rs 26,602L) and provide the bridge that ties them together (Notes 48.09, 48.30(A), 8.3(a), 8(d))?"
receivables_trend: "deteriorating on ageing mix, improving on absolute balance: net trade receivables fell 44.1% YoY (Rs 34.52 Cr to Rs 19.31 Cr, Note 7, p.189-190) but the >6-month past-due bucket rose to 23.5% of gross receivables (FY25) from ~16.0% (FY24); this is the minor trade-receivables book, not the core loan portfolio, whose asset quality is tracked separately in red_flags above (Note 45, p.231)"
restatements_found:
  - "Note 59 (p.258): prior year figures 'regrouped/reclassified, wherever considered necessary' with no specific line items or amounts disclosed - vague boilerplate, not quantified"
going_concern_language: "NONE - no explicit going-concern qualifying language found anywhere in the Notes; Note 40 (Capital Management) states the company has complied in full with externally imposed capital requirements, implicit going concern, no doubt disclosed"
```
