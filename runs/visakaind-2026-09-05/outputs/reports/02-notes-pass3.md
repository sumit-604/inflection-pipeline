# VISAKAIND — Stage 2, Notes to Financial Statements — PASS 3 (Pattern Pass + Consolidation)

Run date: 2026-09-05. Third and final pass. Approach: instead of a sequential note-by-note read,
this pass hunts for patterns across notes already read in Pass 1 and Pass 2 — contradictions,
numbers that do not tie out, deliberately thin disclosure next to detailed disclosure elsewhere,
restatements, subsequent events, and going-concern language — then produces the consolidated
Top 15. Every figure below was re-verified directly against Annual_Report_2026.txt (grep +
line-range reads), not merely copied from Pass 1/2. Where a Pass 1 or Pass 2 number did not
reconcile on re-check, the correction is shown explicitly in Section A below, and the corrected
figure is what carries into the Top 15 and the YAML.

---

## SECTION A — PATTERN-SCAN FINDINGS (new or corrected on this pass)

### A1. NEW — a mid-year loan-term change removed money from a mandatory RPT disclosure line while the real exposure grew (headline new finding of Pass 3)
Note 12 standalone (AR FY26 p.179) carries a footnote on the Atum Life ICD: "During the year the
due date of payment for loan given to Atum Life Private Limited is modified from repayable on
demand to fixed term wherein principal and interest are repayable by March 31, 2028." Pass 2
(Finding #2) had already flagged this as a credit-risk inconsistency (loosening terms to a
collapsing borrower). Cross-referencing it against Note 47 standalone (AR FY26 p.206, table at
p.209) reveals a second, sharper effect: Note 47 is scoped ONLY to loans "repayable on demand or
without specifying any terms or period of repayment." Because Atum Life's loan was reclassified
out of that category mid-year, Note 47's "Related Parties" line for FY26 shows only the Visaka
Green balance (₹650.00 lakhs = ₹6.50 Cr), NOT the Atum Life balance (₹280.00 lakhs = ₹2.80 Cr,
now non-current and fixed-term). The result:
| | FY25 | FY26 |
|---|---|---|
| Note 47 "Related Parties" disclosed amount | ₹779.00 lakhs (₹7.79 Cr) | ₹650.00 lakhs (₹6.50 Cr) |
| Note 47 disclosed % of total loans-in-nature-of-loans | 52.67% | 39.88% |
| ACTUAL total related-party ICD outstanding (Note 12: Visaka Green + Atum Life) | ₹779.00 lakhs (₹6.50+₹2.80... FY25 = ₹5.27+₹2.52 Cr) | ₹930.00 lakhs (₹6.50+₹2.80 Cr) |
| Real YoY change in total related-party ICD | — | **+19.4%** |

A reader of Note 47 alone sees the related-party loan share nearly halve (52.67% → 39.88%) and
would reasonably read that as de-risking. The true picture, reading Note 12 (AR FY26 p.179
standalone / p.247 consolidated) alongside Note 47, is that total related-party ICD exposure grew
19.4% (₹7.79 Cr → ₹9.30 Cr FY26) — the fall in Note 47's percentage is a disclosure-scope artifact
of the term modification, not a reduction in the underlying exposure. This directly resolves the
open question Pass 2 posed for Pass 3 (Finding #12: "is Note 47's divergence worth its own line").
It is: elevated to a standalone red flag in the Top 15 below (#4), and it sharpens Pass 2's
Atum Life finding from a credit-discipline observation into a disclosure-optics one as well.

### A2. NEW — capital commitments more than doubled; not previously extracted by Pass 1 or Pass 2
Note 39 standalone (AR FY26 p.203) / Note 38 consolidated (AR FY26 p.271), "Capital commitments —
Capital expenditure contracted for at the end of the reporting period but not recognised as
liabilities": standalone ₹1,686.51 lakhs (₹16.87 Cr) FY26 vs ₹758.31 lakhs (₹7.58 Cr) FY25, +122%;
consolidated ₹1,686.51 lakhs (₹16.87 Cr) FY26 vs ₹775.90 lakhs (₹7.76 Cr) FY25, +117%. Neither Pass
1 nor Pass 2 extracted this note despite both listing "capital commitments" as an extraction target.
This corroborates the already-noted capex increase (₹37.07 Cr FY26 vs ₹30.20 Cr FY25, Pass 1
Finding #5) with a forward-looking signal: the company has contracted for meaningfully more capex
than it has already spent, consistent with continued (not slowing) capital intensity into FY27. 🟢
Genuine new data point, not a red flag on its own, but material to any FY27 free-cash-flow estimate.

### A3. CORRECTION — the receivables ">1-year tail more than doubled" claim (Pass 1 Finding #6) is
overstated; the real, still-genuine deterioration is smaller
Pass 1 stated the consolidated >1-year ageing tail moved "4.1% → 9.6% of gross receivables." Direct
re-addition of the ageing schedule (Note 8(a)/(b) consolidated, AR FY26 p.242-243) shows Pass 1
summed the FY26 side correctly (1Yr-2Yr ₹545.97 + 2Yr-3Yr ₹359.79 + >3Yr ₹773.54 lakhs = ₹1,679.30
lakhs = ₹16.80 Cr / ₹174.88 Cr gross = 9.6%, confirmed correct) but used an inconsistent basis for
FY25, apparently omitting the 1Yr-2Yr bucket (₹395.47 lakhs). The correct FY25 sum is 1Yr-2Yr
₹395.47 + 2Yr-3Yr ₹244.53 + >3Yr ₹575.26 lakhs = ₹1,215.26 lakhs = ₹12.15 Cr / ₹199.12 Cr gross =
**6.1%**, not 4.1%. Corrected trend: **6.1% (FY25) → 9.6% (FY26)**, a genuine deterioration (+3.5
percentage points, the absolute >1-year balance rose 38% even as total receivables fell 12%) but not
the "more than doubled" framing Pass 1 used. The standalone equivalent (Note 9(a)/(b), AR FY26
p.174-175) confirms the same direction on a smaller scale: 5.7% (FY25) → 6.8% (FY26). This
correction is what carries into the YAML `receivables_trend` field and FLAG-CASH below — the
direction (deteriorating) and the FLAG-CASH trigger are UNCHANGED; only the magnitude is corrected.

### A4. CORRECTION — the ₹7.00 Cr ICD write-off's per-counterparty split (Pass 1 Finding #3)
Pass 1 attributed the FY26 write-off as "Bhagyanagar Hotels ₹2.50 Cr + Galvanizz Projects Pvt Ltd
₹5.50 Cr." The Note 12 party-level table (AR FY26 p.179 standalone / p.247 consolidated) shows
"Amount granted during the year" (cumulative, as of the FY25 column) for Bhagyanagar was indeed
₹250.00 lakhs (₹2.50 Cr), but "Amount outstanding net of loss allowance" as of 31-Mar-2025 was
already only ₹150.00 lakhs (₹1.50 Cr) — ₹1.00 Cr of the original Bhagyanagar loan was already off
the books before FY26 for a reason not disclosed anywhere in the Notes read (partial recovery is the
likeliest explanation; a prior undisclosed write-down cannot be ruled out). The amount actually
carried into and written off during FY26 was Bhagyanagar ₹1.50 Cr + Galvanizz ₹5.50 Cr = ₹7.00 Cr
total — the aggregate ₹7.00 Cr figure Pass 1 used for the P&L provision (Note 32 standalone p.189-
190) is correct; only the per-counterparty attribution needed correcting. CARO (Auditor's Report,
AR FY26 p.144-145, para (iii)(d)) independently corroborates the corrected split: "the total amount
overdue for more than ninety days... is ₹794.83 lakhs" against exactly 2 cases (₹700.00 lakhs
principal, matching Bhagyanagar ₹150 + Galvanizz ₹550, plus ₹94.83 lakhs accrued interest).

### A5. CORRECTION — Pass 2's Finding #6 mis-stated the consolidated critical-judgements list
Pass 2 claimed Note 2 "lists BOTH 'Recoverability of investments in subsidiaries'... AND
'Impairment of loans-inter corporate deposits' as critical judgement areas in the SAME list" at
both standalone (AR FY26 p.161) AND consolidated (p.226) level. Direct read of the consolidated
Note 2 (verified at AR FY26 p.229, a 9-item list) confirms "Impairment of loans-inter corporate
deposits" IS item 5, but "Recoverability of investments in subsidiaries" is **absent** from the
consolidated list — correctly so, because subsidiaries are consolidated line-by-line in the CFS;
there is no "investment in subsidiary" balance sheet asset at the consolidated level to be impaired
(that asset exists only in the STANDALONE books, Note 5, AR FY26 p.173). The substance of Pass 1's
Red Flag #2 is unaffected (the standalone investment truly is unimpaired against a subsidiary at
4% of cost), but the "tension between two judgements" framing (Pass 1 Finding #9) is precise only
when stated as: standalone non-impairment of the subsidiary investment, set against CONSOLIDATED
non-recognition of DTA on the same subsidiaries' tax losses — two different registers (standalone
vs consolidated), not one shared list at both levels.

### A6. CORRECTION — Finding #1's framing (Pass 1) overstates a company disclosure failing; the bundling is external, not internal
Direct check of both P&L faces confirms the Company's OWN presentation is clean: standalone
"Other income" (Note 26, ₹710.49 lakhs) and "Exceptional items" (Note 59, ₹5,970.33 lakhs) are two
SEPARATE line items on the face of the standalone Statement of Profit and Loss (AR FY26 p.156,
lines II and VI respectively), never bundled; the same separation holds at consolidated level
(Note 25 / Note 58, AR FY26 p.224). The tax reconciliation (Note 33 standalone p.192 / Note 32
consolidated p.259) explicitly walks the concessional 14.3% LTCG rate applied only to the
exceptional-items slice. The Company's own Note 44 ratio-variance disclosure (AR FY26 p.209
standalone) states in its own words that ROE +55,250%, Net Profit Ratio +52,800%, RoCE +243% and
DSCR +85% are "primarily on account of... exceptional items." **Correction: this is not a company
mislabeling or aggressive-accounting issue** (no red flag on the Company's own disclosure quality
here) — it is a THIRD-PARTY DATA-VENDOR/SCREENER aggregation issue (the screener figure bundling
"other income" apparently sums the two separately-disclosed AR line items into one feed field).
Downstream stages that inherited the company-memory-flagged "₹66.81 Cr other income surge" should
treat the underlying AR disclosure as clean and well-signposted; the normalisation work is real and
necessary for an investor, but it is an analyst task, not evidence of an accounting-quality failure
by the Company. This finding is DOWNGRADED from 🔴 red flag to 🟡 analyst-normalisation note in the
Top 15 below, with the cash-flow corroboration (Finding A7 below / Pass 2 Finding #7) promoted in
its place as the lead item on genuine-recovery evidence.

### A7. Going concern and restatements — confirmed clean on full-text grep, both years
Grepped the full document for "going concern," "material uncertainty," "restated," "prior period
error," and "Ind AS 8" retrospective-correction language. Every "going concern" and "material
uncertainty" hit is boilerplate from the standard "Auditor's Responsibilities" and "Responsibilities
of Management" sections of the audit report template (AR FY26 p.144-155 standalone, p.212-223
consolidated) — present in every Indian audit report regardless of the auditee's health, not an
actual conclusion of doubt. No "prior period error" or Ind AS 8 retrospective RESTATEMENT of
comparative figures was found; the only Ind AS 8 references are to the routine, prospective
application of the FY26 standard amendments (Note 1(iii)/(iv)), which is not a restatement. Both
auditor's reports are unmodified/unqualified opinions. **Confirmed: going_concern_language = NONE;
restatements_found = none.**

### A8. Minor — a systematic page-anchor drift in Pass 1/Pass 2 citations
Several Pass 1/Pass 2 page anchors are off by 1-4 pages against the document's own
"===== PAGE N =====" tags when independently re-checked (e.g., standalone Note 12 cited at p.176,
verified at p.179; standalone Note 38 cited at p.204, verified at p.203; consolidated Note 37 cited
at p.267, verified at p.271; consolidated Note 2 cited at p.226, verified at p.229; standalone Note
44 ROI line cited at p.206, verified at p.209). None of these anchor slips changed a substantive
figure in this pass — the underlying numbers Pass 1/2 read were correct in every case checked
except A3 and A4 above. Flagged here as a light QA note for downstream stages: verify against the
"===== PAGE N =====" tag itself, not against a note's stated anchor, when precision matters (e.g.
for a Notion citation or a verifier cross-check).

**PASS 3 verdict on the "no material new findings" test: NOT EMPTY.** The pattern scan produced one
materially important new red flag (A1, the Note 47 disclosure-optics mechanism), one new positive
data point (A2, capital commitments), and three corrections that change the stated magnitude (not
the direction) of two Pass 1 findings and one Pass 2 finding (A3, A4, A5), plus a reclassification
of Finding #1's severity (A6) that meaningfully changes the accounting-quality read for the better.
`pass_3_empty: false`.

---

## SECTION B — CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### B1. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Consolidated operating cash flow rose to ₹183.14 Cr FY26 (+60.6% YoY) and is explicitly, mechanically stripped of the ₹59.70 Cr exceptional land-sale gain in the PBT-to-OCF reconciliation ("Net profit on sale of assets - exceptional items" is subtracted out; sale proceeds sit in investing activities instead). The single cleanest, least-manipulable evidence that FY26's operating recovery is real. | Cash Flow Statement, AR FY26 p.226 consolidated | 🟢 | Cash cannot be timed the way an asset-sale-driven P&L line nominally could; this corroborates the recovery from a different accounting base than profit. |
| 2 | Standalone PAT of ₹87.83 Cr is not comparable to prior years on a like-for-like basis: it includes a ₹59.70 Cr pre-tax (≈₹51.16 Cr post-tax) exceptional gain from selling Ahmedabad land (₹36.74 Cr) and Kanchipuram land+building (₹22.96 Cr). Ex-exceptional standalone PAT is ≈₹36.7 Cr FY26 vs ₹0.14 Cr FY25 — still a real improvement, driven by segment operating profit rising to ₹142.36 Cr from ₹95.09 Cr, but far smaller than the headline. The Company's OWN disclosure (separate P&L line, separate note, explicit tax-rate walk, explicit ratio-variance admission) is clean; this is a normalisation task for the analyst, not a Company accounting-quality failure. | Note 26/59 standalone, AR FY26 p.187 & p.203; Note 25/58 consolidated p.224 & p.279 | 🟡 (analyst normalisation, not a red flag on the Company) | The single most important adjustment for any earnings-quality read of FY26; misapplied by any external data feed that bundles the two lines. |
| 3 | Unimpaired subsidiary investments despite severe, accelerating erosion: Atum Life's own net worth fell 71% in FY26 ALONE (₹1.12 Cr → ₹0.32 Cr) against a ₹7.795 Cr cost (96% cumulative erosion); Visaka Green fell 24% (₹6.88 Cr → ₹5.20 Cr) against a ₹6.51 Cr cost, loss widening YoY. "Recoverability of investments in subsidiaries" is management's own named critical judgement (standalone only — correctly absent from the consolidated list, see A5) yet no impairment is booked. The standalone-level ROI ratio (-16.03% FY26 vs -18.74% FY25) independently corroborates persistent value destruction. | Note 5/2 standalone, AR FY26 p.173/161; Note 44 consolidated p.276-277; AOC-1 p.82; Note 44 ROI standalone p.209 | 🔴 | Names its own risk, then does not act on it; the gap between cost and net worth is now material and widening. |
| 4 | NEW (Pass 3): a mid-year change to Atum Life's ICD terms (on-demand → fixed term to Mar-2028) removed ₹2.80 Cr from Note 47's mandatory "related-party loans repayable on demand" disclosure line. The result LOOKS like de-risking (Note 47's disclosed related-party share fell 52.67% → 39.88%) but the true total related-party ICD exposure actually GREW 19.4% (₹7.79 Cr → ₹9.30 Cr). A disclosure-optics artifact, not a real reduction in exposure, layered on top of lending more time to a deteriorating borrower. | Note 12 standalone, AR FY26 p.179; Note 47 standalone p.206/209 | 🔴 | A reader relying on Note 47's headline percentage alone would draw the opposite conclusion from the truth. |
| 5 | ₹7.00 Cr of ICDs to unrelated, non-operating counterparties (Bhagyanagar Hotels ₹1.50 Cr, Galvanizz Projects ₹5.50 Cr — corrected split, see A4) fully impaired in FY26, and a THIRD such counterparty this year (Sreenidi-Deccan Football Club, ₹6.00 Cr at 18% p.a.) received and repaid money within the year. "Impairment of loans-ICD" was itself a named critical judgement (Note 2) before the write-off happened. | Note 12 standalone AR FY26 p.179 / consolidated p.247; Note 32 standalone p.189-190; Note 2 p.161 | 🔴 | Treasury/capital-allocation quality issue distinct from the core manufacturing business; a pattern (three counterparties), not a one-off. |
| 6 | Three same-year round-trip financing arrangements with promoter/non-operating counterparties: Chairman Dr. G. Vivek Venkatswamy (₹13.03 Cr lent and repaid, ₹0.16 Cr interest paid); Vigilance Security Services Pvt Ltd, promoter-controlled (₹21.00 Cr ICD received / ₹15.75 Cr repaid, ₹5.25 Cr o/s, 8% p.a., ₹0.54 Cr interest expense); Sreenidi-Deccan Football Club (₹6.00 Cr ICD given and repaid, 18% p.a.). Gross ₹40.03 Cr in / ₹34.78 Cr repaid across the three; business purpose undisclosed for the Chairman loan. | Note 40 standalone, AR FY26 p.201-202; Note 12 p.179 | 🟡 | Round-tripping this size, three times in one year, with promoter-adjacent and non-operating counterparties, is a treasury-discipline question the notes do not answer. |
| 7 | Genuine, material deleveraging: consolidated debt fell ₹534.10 Cr (FY24) → ₹478.44 Cr (FY25) → ₹302.49 Cr (FY26); gearing 71% → 64% → 37%; no covenant breaches; undrawn facilities nearly doubled to ₹264.88 Cr (from ₹139.28 Cr); management guides FY27 finance cost down to ₹27.00 Cr from FY26's actual ₹32.96 Cr. | Note 35 consolidated, AR FY26 p.265; Note 35(C)(i) standalone p.196 | 🟢 | A structural balance-sheet improvement, not a one-year optical effect; corroborated from three independent angles (debt level, gearing ratio, headroom). |
| 8 | Positive FY26 investing cash flow (+₹35.25 Cr) is fully explained by the land/building disposals, not a capex pullback — capex rose to ₹37.07 Cr (from ₹30.20 Cr) and contracted capital commitments more than doubled to ₹16.87 Cr (from ₹7.58 Cr standalone, +122%, NEW in Pass 3). | Cash Flow Statement AR FY26 p.223 consolidated; Note 39 standalone p.203 / Note 38 consolidated p.271 | 🟢 | Forward-looking: the Company is accelerating capex commitments, not retrenching, even while divesting non-core land. |
| 9 | Trade receivables >1-year ageing tail deteriorated genuinely, though LESS dramatically than Pass 1 first stated (corrected in A3): consolidated gross >1-year share rose from 6.1% (FY25, ₹12.15 Cr) to 9.6% (FY26, ₹16.80 Cr) even as absolute receivables fell 12.2% and the DSO ratio nominally improved (9.58x vs 9.41x turnover); standalone loss allowance held flat at ₹8.43 Cr across both years despite the ageing-tail growth. | Note 9(a)/(b) standalone, AR FY26 p.174-175; Note 8(a)/(b) consolidated p.242-243 | 🟡 | Two receivables-quality signals point opposite ways; the ECL matrix calibration question stands, at the corrected magnitude. |
| 10 | Blended effective tax rate is depressed by the 14.3% concessional LTCG rate on the exceptional gain (vs 25.168% standard); the Company's own Schedule III-mandated ratio-variance table concedes ROE +55,250%, Net Profit Ratio +52,800%, RoCE +243% and DSCR +85% are substantially exceptional-item-driven — a direct, citable management admission. | Note 33 standalone AR FY26 p.192; Note 32 consolidated p.259-260; Note 44 standalone p.209 | 🟡 | Reinforces Finding #2's normalisation point with the Company's own words, not just analyst inference. |
| 11 | Governance/RPT footprint widened while unrelated executives churned: two CXO exits within the year (COO to 25-May-2025; CEO in post only 14-Apr to 22-Aug-2025, ~4 months) alongside a NEW paid role for the MD's daughter, Mrs. G. Vritika, "Chief Business Strategist and Advisor to the Chairman" (₹25.88 lakh remuneration FY26, nil FY25). | Note 40 standalone, AR FY26 p.201; Note 39 consolidated p.269 | 🟡 | Family-related-party footprint growing at the same time non-family leadership roles show high turnover. |
| 12 | Segment decomposition (not previously separated by Pass 1): Synthetic Yarn delivered a disproportionate share of the profit recovery — segment profit ₹14.08 Cr FY26 vs ₹1.36 Cr FY25 (+934%), contributing 27% of the total ₹47.27 Cr segment-profit improvement on only 15.6% of revenue. Building Products, the core segment, grew profit a more modest +37% (₹93.73 Cr → ₹128.28 Cr). | Note 37 standalone, AR FY26 p.199-200 | 🟡 | The smaller, historically weaker segment is inflecting fastest; repeatability (cost, pricing, or mix driven) is unconfirmed in the notes. |
| 13 | No Key Audit Matter raised on subsidiary-investment recoverability or ICD impairment despite both being named critical judgements with clear FY26 quantitative stress triggers (a subsidiary at 4% of cost, a 100% ICD write-off); the two subsidiaries are audited by a different, smaller component auditor (combined FY26 total assets ₹19.35 Cr, net cash outflow ₹0.56 Cr). | Auditor's Reports, AR FY26 p.144-145 standalone (KAM), p.212-215 consolidated (Other Matter) | 🟡 | Disclosure-quality/audit-scope observation: the two areas with the clearest quantitative stress got no elevated audit scrutiny disclosed. |
| 14 | Export revenue is shrinking in absolute terms (₹115.23 Cr FY25 → ₹108.56 Cr FY26, -5.8%) even as total revenue grows +8.7% — a geographic-mix shift toward India-only growth. | Note 36 consolidated, AR FY26 p.267 (segment note) | 🟡 | Worth watching whether this is deliberate mix shift or lost export competitiveness. |
| 15 | Final dividend raised 140% per share (₹0.50 → ₹1.20, 25% → 60% of face value) in the same year as the ₹59.70 Cr one-time gain; the raised payout is being set in a year whose ex-exceptional earnings base is only ≈₹37 Cr standalone. | Note 36(B) standalone, AR FY26 p.198; Note 35(B) consolidated p.265-266 | 🟡 | Sustainability of the higher payout should be checked against recurring, not headline, earnings. |

### B2. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 8 | Point-in-time on transfer of control, no significant financing component, standard for the industry; the one non-recurring item embedded in revenue (₹9.62 Cr TUFS subsidy) is disclosed, not hidden. |
| Expense capitalisation honesty | 7 | No capitalisation threshold disclosed (minor gap); no evidence of aggressive capitalisation; PPE write-offs and bad-debt write-offs both small and disclosed; capital commitments properly tabulated. |
| Provisioning adequacy | 4 | The weakest dimension: no impairment on a subsidiary investment at 4% of cost (Finding #3); flat standalone ECL allowance against a rising ageing tail (Finding #9); a static, unexplained "provision for contingencies" line for at least two years. |
| RPT fairness | 5 | Rates on disclosed related-party ICDs are broadly arm's length (8-10%), but three same-year round-trip arrangements with promoter/non-operating counterparties and undisclosed business purpose, plus a new promoter-family paid role, weigh this down. |
| Disclosure transparency | 6 | Genuinely strong on the exceptional item (clean separate-line presentation, explicit tax walk, candid ratio-variance admissions — Finding #10) and on cash-flow reconciliation (Finding #1); genuinely weak on the Note 47 disclosure-optics effect (Finding #4) and the absence of a KAM on the two most quantitatively stressed judgement areas (Finding #13). |
| Consistency with prior years | 8 | No restatements found; ECL rates, useful lives, and accounting policies unchanged YoY; routine standard amendments only, all assessed as no material impact. |
| **OVERALL** | **6/10** | Mechanically clean, compliant, well-signposted financial reporting on the headline numbers (exceptional item, cash flow, deleveraging), undercut by real judgement-application weaknesses on subsidiary impairment and inter-corporate-deposit/related-party treasury discipline that the balance sheet numbers do not yet reflect. |

### B3. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Subsidiary investment (Atum Life, Visaka Green) eventually forces an impairment charge the notes already signal but have not booked | Medium | Note 5/44 net-worth-vs-cost gap each AR/quarterly cycle; any KAM added in a future audit report | Next AR (FY27) if net worth keeps falling at the FY26 pace |
| Further ICD losses to non-operating counterparties (pattern of 3 in FY26: hotel, projects company, football club) | Medium | Note 12 party-level table each period; any NEW unrelated counterparty appearing | Any period a new ICD is granted outside the core business |
| Trade receivables ageing-tail continues to widen while loss allowance stays flat | Low-Medium | Note 9/8 ageing schedule and loss-allowance movement each period | Ongoing; watch the >1-year share trend, not just DSO |
| Related-party loan exposure understated by Note 47's disclosure scope (on-demand vs fixed-term reclassification) | Low (disclosure-quality, not solvency) | Note 12 total related-party ICD (not just Note 47's on-demand subset) each period | If further terms are extended/reclassified |
| Dividend payout raised off a one-time-gain-inflated earnings base | Low-Medium | FY27 dividend decision against ex-exceptional recurring earnings (~₹37 Cr base) | FY27 AGM dividend proposal |
| Management-stability/related-party overlap (CXO churn + new family advisory role) | Low | Note 40 KMP list and remuneration lines each period | Any further CXO exit within 12 months |

### B4. FIVE (PLUS ONE) QUESTIONS FOR MANAGEMENT

1. What is the business rationale for the Chairman's same-year round-trip ₹13.03 Cr loan, the ₹21.00
   Cr ICD facility from promoter-controlled Vigilance Security Services, and the ₹6.00 Cr ICD to
   Sreenidi-Deccan Football Club — why place cash with three non-operating counterparties in one
   year rather than repay debt or return capital to shareholders?
2. Given Atum Life's net worth fell 71% in FY26 alone to ₹0.32 Cr against a ₹7.795 Cr cost, why was
   the ICD due date extended (on-demand to March 2028) rather than the investment impaired, and
   what is management's basis for continuing to treat it as fully recoverable?
3. The Atum Life term modification also removed ₹2.80 Cr from Note 47's related-party "on-demand
   loan" disclosure even as total related-party ICD exposure grew 19.4% — was this disclosure effect
   considered when the term change was approved?
4. What specifically drove Synthetic Yarn's segment profit +934% (cost, pricing, or product mix), and
   is the improvement repeatable, given it delivered 27% of the total segment-profit recovery on only
   15.6% of revenue?
5. With the FY26 dividend per share raised 140% in the same year as a ₹59.70 Cr one-time land-sale
   gain, is the new payout level calibrated to the recurring (ex-exceptional) earnings base of
   roughly ₹37 Cr, or to headline PAT?
6. Of the two critical judgements named in Note 2 (recoverability of subsidiary investments;
   impairment of loans-ICD), one was written off in full this year and the other has not moved at
   all — what differentiates management's assessment of the two?

### B5. NOTES-BASED RED FLAGS

- Unimpaired subsidiary investments (Atum Life, Visaka Green) against accelerating net-worth
  erosion, with "recoverability" self-named as a critical judgement (standalone Note 2) but not
  acted on (Note 5 p.173; Note 44 consolidated p.276-277; AOC-1 p.82).
- A mid-year loan-term change (Atum Life ICD, on-demand → fixed term to Mar-2028) that mechanically
  shrank the mandatory Note 47 related-party disclosure line while the true related-party ICD
  exposure grew 19.4% (Note 12 p.179; Note 47 p.206/209).
- ₹7.00 Cr of ICDs to unrelated non-operating counterparties (hotel, projects company) fully
  impaired in FY26, plus a third round-trip ICD to a football club at 18% p.a. — a pattern, not a
  one-off (Note 12 p.179/247; Note 32 p.189-190; Note 2 p.161).
- Three same-year round-trip financing arrangements with promoter/non-operating counterparties,
  gross ₹40.03 Cr in / ₹34.78 Cr repaid, business purpose undisclosed (Note 40 p.201-202).
- Standalone trade-receivables loss allowance held flat at ₹8.43 Cr across FY25→FY26 despite the
  >1-year ageing tail rising from 6.1% to 9.6% of gross receivables (Note 9(a)/(b) p.174-175).
- No Key Audit Matter on either of the two areas with the clearest FY26 quantitative stress
  (subsidiary recoverability, ICD impairment); those two subsidiaries are audited by a smaller,
  different component auditor (AR FY26 p.144-145, p.212-215).

### B6. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices. Key concern: unimpaired subsidiary investments
paired with a loan-term change that shrank a mandatory related-party disclosure line while the
real exposure grew. Key strength: a cleanly disclosed, fully cash-corroborated exceptional item and
genuine, well-evidenced deleveraging. Overall accounting quality: 6/10.

---

## SECTION C — RECONCILIATION OF PASSES 1, 2 AND 3 (summary)

- Pass 1 (sequential, Note 1 to last note, both standalone and consolidated): 10 ranked findings,
  anchored, no notes skipped. Strongest original contributions: the exceptional-item/other-income
  separation (#1), the unimpaired-subsidiary-investment red flag (#2), the ICD write-off (#3), and
  the deleveraging evidence (#4).
- Pass 2 (re-read for what was missed): 12 new findings, none overturning Pass 1's Top 10, several
  sharpening them materially — the third round-trip ICD counterparty (football club), the Atum Life
  term-loosening footnote, the single-year (not merely cumulative) net-worth-collapse data, the
  independently-disclosed negative ROI ratio, the cash-flow-based confirmation of genuine operating
  recovery (its own top-rated new finding), and the segment-level decomposition of the profit
  recovery.
- Pass 3 (pattern scan, this pass): connected two of Pass 2's separate findings (Atum Life term
  change + Note 47 divergence) into one new, higher-severity red flag (A1) that neither earlier pass
  had assembled; added one wholly new data point Pass 1/2 both missed despite listing it as an
  extraction target (capital commitments, A2); corrected the magnitude of two Pass 1/2 findings
  after full re-addition of the underlying tables (receivables ageing %, A3; ICD write-off
  per-counterparty split, A4); corrected a factual slip in Pass 2's own critical-judgements
  cross-reference (A5); and reclassified Pass 1's top-ranked finding from a Company accounting-
  quality red flag to an analyst-normalisation note once the face-of-P&L presentation was directly
  verified as clean (A6). Confirmed clean on going concern and restatements (A7). No note was found
  to materially contradict another beyond the corrections listed above; standalone and consolidated
  figures tie out everywhere checked except the Note 47 scope effect, which is explained, not an
  error.
- Net effect on the Top 15 and the accounting-quality score: the direction of every original red
  flag survives Pass 3; the CFO-based recovery evidence is promoted to the top of the list; the
  exceptional-item finding is downgraded from red to a normalisation note; the subsidiary/ICD
  cluster gains one new, sharper red flag (Note 47 disclosure-optics mechanism) and loses none.

---

```yaml
stage: B02-notes
company: "VISAKAIND"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
input_gaps:
  - "Results filings absent from corpus; no quarterly/annual results PDF beyond the two Annual Reports (carried from B00)."
  - "Credit rating bulletin/rationale absent from corpus (carried from B00)."
  - "Reg 30 announcements (last ~12m) absent from corpus (carried from B00)."
  - "Shareholding pattern (SEBI quarterly filing) absent from corpus; promoter holding/pledge known only from AR FY26 annual snapshot (carried from B00)."
  - "Broker/analyst research absent from corpus (carried from B00)."
  - "Main concalls stale: newest available is Q1 FY24 (Aug-2023); no FY25/FY26 concall transcript in corpus (carried from B00)."
  - "Investor presentation stale: newest available is the Q1 FY24 deck (carried from B00)."
  - "Screening split CSVs empty; only the screener Data_Sheet is populated (carried from B00)."
  - "Only 1 of 3 named peers has transcripts available (carried from B00)."
flags:
  - {type: FLAG-CASH, reason: "Consolidated trade receivables >1-year ageing tail rose from 6.1% of gross (FY25, Rs 12.15 Cr of Rs 199.12 Cr) to 9.6% (FY26, Rs 16.80 Cr of Rs 174.88 Cr) even as absolute gross receivables fell 12.2% and the DSO ratio nominally improved (9.58x vs 9.41x turnover); standalone loss allowance held flat at Rs 8.43 Cr through both years despite the ageing-tail growth (Note 9(a)/(b) standalone AR FY26 p.174-175; Note 8(a)/(b) consolidated p.242-243). Corrects Pass 1's overstated 4.1%->9.6% framing (see report Section A3); direction and FLAG-CASH trigger unchanged, magnitude corrected."}
accounting_quality: 6
pass_2_empty: false
pass_3_empty: false
top_findings:
  - {rank: 1, finding: "Consolidated operating cash flow Rs 183.14 Cr FY26 (+60.6% YoY), explicitly stripped of the Rs 59.70 Cr exceptional land-sale gain in the PBT-to-OCF reconciliation; the cleanest evidence FY26's operating recovery is real.", note_ref: "Cash Flow Statement, AR FY26 p.226 consolidated", rating: "green", why: "Cash-based, not accrual-timeable, corroboration of genuine recovery independent of the asset-sale gain."}
  - {rank: 2, finding: "Standalone PAT Rs 87.83 Cr FY26 includes a Rs 59.70 Cr pre-tax (~Rs 51.16 Cr post-tax) one-time land-sale gain (Ahmedabad Rs 36.74 Cr + Kanchipuram Rs 22.96 Cr); ex-exceptional PAT is ~Rs 36.7 Cr. Company's own presentation is clean (separate P&L line, separate note); bundling into a single 'other income' figure is a third-party data-vendor artifact, not a Company disclosure failing.", note_ref: "Note 26/59 standalone AR FY26 p.187/203; Note 25/58 consolidated p.224/279", rating: "yellow", why: "The single most important normalisation adjustment for FY26 earnings quality; downgraded from red flag after verifying the AR's own presentation is clean."}
  - {rank: 3, finding: "Unimpaired subsidiary investments despite severe erosion: Atum Life net worth fell 71% in FY26 alone (Rs 1.12 Cr -> Rs 0.32 Cr) against Rs 7.795 Cr cost (96% cumulative erosion); Visaka Green fell 24% (Rs 6.88 Cr -> Rs 5.20 Cr) against Rs 6.51 Cr cost. 'Recoverability of investments in subsidiaries' is a named critical judgement (standalone only) but not acted on; ROI ratio -16.03%/-18.74% corroborates.", note_ref: "Note 5/2 standalone AR FY26 p.173/161; Note 44 consolidated p.276-277; AOC-1 p.82", rating: "red", why: "Names its own risk, then does not reflect it in the balance sheet; gap is material and widening."}
  - {rank: 4, finding: "A mid-year Atum Life ICD term change (on-demand -> fixed term to Mar-2028) removed Rs 2.80 Cr from Note 47's mandatory related-party 'on-demand loan' disclosure, making the disclosed related-party-loan share look like it fell (52.67% -> 39.88%) even though true total related-party ICD exposure grew 19.4% (Rs 7.79 Cr -> Rs 9.30 Cr).", note_ref: "Note 12 standalone AR FY26 p.179; Note 47 standalone p.206/209", rating: "red", why: "A reader relying on Note 47's headline percentage alone would conclude the opposite of the truth; new pattern-pass catch, not previously assembled by Pass 1/2."}
  - {rank: 5, finding: "Rs 7.00 Cr of ICDs to unrelated non-operating counterparties fully impaired in FY26 (Bhagyanagar Hotels Rs 1.50 Cr + Galvanizz Projects Rs 5.50 Cr, corrected split); a third counterparty this year, Sreenidi-Deccan Football Club, received and repaid Rs 6.00 Cr at 18% p.a. 'Impairment of loans-ICD' was itself a named critical judgement before the write-off.", note_ref: "Note 12 standalone AR FY26 p.179 / consolidated p.247; Note 32 standalone p.189-190", rating: "red", why: "Capital-allocation/treasury quality issue distinct from the core business; a pattern of three counterparties, not one-off."}
  - {rank: 6, finding: "Three same-year round-trip financing arrangements with promoter/non-operating counterparties: Chairman (Rs 13.03 Cr), Vigilance Security Services (Rs 21.00 Cr ICD, 8% p.a., Rs 5.25 Cr o/s), football club (Rs 6.00 Cr, 18% p.a.). Gross Rs 40.03 Cr in / Rs 34.78 Cr repaid; business purpose undisclosed for the Chairman loan.", note_ref: "Note 40 standalone AR FY26 p.201-202; Note 12 p.179", rating: "yellow", why: "Round-tripping this size, three times in one year, is a treasury-discipline question the notes do not answer."}
  - {rank: 7, finding: "Genuine, material deleveraging: consolidated debt Rs 534.10 Cr (FY24) -> Rs 478.44 Cr (FY25) -> Rs 302.49 Cr (FY26); gearing 71% -> 64% -> 37%; no covenant breaches; undrawn facilities nearly doubled to Rs 264.88 Cr; FY27 finance cost guided down to Rs 27.00 Cr.", note_ref: "Note 35 consolidated AR FY26 p.265; Note 35(C)(i) standalone p.196", rating: "green", why: "Structural balance-sheet improvement corroborated from three independent angles."}
  - {rank: 8, finding: "Positive FY26 investing cash flow (+Rs 35.25 Cr) is fully explained by land/building disposals, not a capex pullback: capex rose to Rs 37.07 Cr (from Rs 30.20 Cr) and contracted capital commitments more than doubled to Rs 16.87 Cr (from Rs 7.58 Cr, +122%).", note_ref: "Cash Flow Statement AR FY26 p.223 consolidated; Note 39 standalone p.203 / Note 38 consolidated p.271", rating: "green", why: "Forward capex signal not previously extracted by Pass 1 or Pass 2 despite being a named extraction target."}
  - {rank: 9, finding: "Trade receivables >1-year ageing tail rose from 6.1% of gross (FY25) to 9.6% (FY26) even as absolute receivables fell 12.2% and DSO nominally improved; standalone loss allowance held flat at Rs 8.43 Cr through both years.", note_ref: "Note 9(a)/(b) standalone AR FY26 p.174-175; Note 8(a)/(b) consolidated p.242-243", rating: "yellow", why: "Corrected magnitude of Pass 1's finding (was mis-stated as 4.1%->9.6%); ECL calibration question stands at the corrected level."}
  - {rank: 10, finding: "Blended effective tax rate depressed by the 14.3% concessional LTCG rate on the exceptional gain (vs 25.168% standard); Company's own ratio-variance table concedes ROE +55,250%, Net Profit Ratio +52,800%, RoCE +243%, DSCR +85% are substantially exceptional-item-driven.", note_ref: "Note 33 standalone AR FY26 p.192; Note 32 consolidated p.259-260; Note 44 standalone p.209", rating: "yellow", why: "A direct, citable management admission reinforcing the normalisation point in Finding #2."}
  - {rank: 11, finding: "Two CXO exits within the year (COO to 25-May-2025; CEO in post 14-Apr to 22-Aug-2025, ~4 months) alongside a new paid role for the MD's daughter, 'Chief Business Strategist and Advisor to the Chairman' (Rs 25.88 lakh FY26, nil FY25).", note_ref: "Note 40 standalone AR FY26 p.201; Note 39 consolidated p.269", rating: "yellow", why: "Family-related-party footprint widening while unrelated leadership shows high turnover."}
  - {rank: 12, finding: "Synthetic Yarn segment profit rose 934% (Rs 1.36 Cr -> Rs 14.08 Cr FY26), contributing 27% of the total segment-profit recovery on only 15.6% of revenue; Building Products (core segment) grew profit a more modest 37%.", note_ref: "Note 37 standalone AR FY26 p.199-200", rating: "yellow", why: "The smaller, historically weaker segment is inflecting fastest; repeatability is unconfirmed in the notes."}
  - {rank: 13, finding: "No Key Audit Matter raised on subsidiary-investment recoverability or ICD impairment despite both being named critical judgements with clear FY26 quantitative stress triggers; the two subsidiaries are audited by a different, smaller component auditor.", note_ref: "Auditor's Reports, AR FY26 p.144-145 standalone (KAM); p.212-215 consolidated (Other Matter)", rating: "yellow", why: "The two areas with the clearest quantitative stress received no disclosed elevated audit scrutiny."}
  - {rank: 14, finding: "Export revenue shrank in absolute terms (Rs 115.23 Cr FY25 -> Rs 108.56 Cr FY26, -5.8%) even as total revenue grew +8.7%, a geographic-mix shift toward India-only growth.", note_ref: "Note 36 consolidated AR FY26 p.267 (segment note)", rating: "yellow", why: "Worth confirming whether this is deliberate mix shift or lost export competitiveness."}
  - {rank: 15, finding: "Final dividend raised 140% per share (Rs 0.50 -> Rs 1.20) in the same year as the Rs 59.70 Cr one-time gain; the higher payout is set against an ex-exceptional standalone earnings base of only ~Rs 37 Cr.", note_ref: "Note 36(B) standalone AR FY26 p.198; Note 35(B) consolidated p.265-266", rating: "yellow", why: "Sustainability of the raised payout should be checked against recurring, not headline, earnings."}
red_flags:
  - "Unimpaired subsidiary investments: Atum Life net worth fell 71% in FY26 alone to Rs 0.32 Cr against Rs 7.795 Cr cost (96% cumulative erosion); Visaka Green Rs 6.88 Cr -> Rs 5.20 Cr; no impairment booked despite 'recoverability of investments in subsidiaries' being a named critical judgement (Note 2 p.161; Note 5 p.173; Note 44 consolidated p.276-277; AOC-1 p.82)."
  - "Loan-term loosening that shrank a mandatory disclosure line: Atum Life's ICD moved from repayable-on-demand to a fixed term (due Mar-2028) during FY26 while its net worth collapsed; this removed Rs 2.80 Cr from Note 47's related-party 'on-demand loan' table, making the disclosed related-party-loan percentage fall (52.67% -> 39.88%) even though total related-party ICD exposure actually grew 19.4% (Rs 7.79 Cr -> Rs 9.30 Cr) (Note 12 p.179 standalone; Note 47 p.206/209 standalone)."
  - "Rs 7.00 Cr of ICDs to unrelated non-operating counterparties (Bhagyanagar Hotels Rs 1.50 Cr, Galvanizz Projects Rs 5.50 Cr) fully impaired in FY26, and a THIRD such counterparty (Sreenidi-Deccan Football Club, Rs 6.00 Cr at 18% p.a.) received and repaid money the same year; 'impairment of loans-ICD' was itself a named critical judgement before the write-off (Note 2 p.161; Note 12 p.179/247; Note 32 p.189-190)."
  - "Three same-year round-trip financing arrangements with promoter/non-operating counterparties (Chairman Rs 13.03 Cr; Vigilance Security Services Rs 21.00 Cr ICD; football club Rs 6.00 Cr ICD), gross Rs 40.03 Cr in / Rs 34.78 Cr repaid, business purpose undisclosed (Note 40 p.201-202 standalone)."
  - "Standalone loss allowance on trade receivables held flat at Rs 8.43 Cr across FY25->FY26 despite the >1-year ageing tail rising from 6.1% to 9.6% of gross receivables (Note 9(a)/(b) p.174-175 standalone)."
  - "No Key Audit Matter raised on subsidiary-investment recoverability or ICD impairment despite both being named critical judgements with clear FY26 quantitative stress triggers; the two subsidiaries are audited by a different, smaller component auditor (AR FY26 p.144-145, p.212-215)."
questions_for_mgmt:
  - "What is the business rationale for the Chairman's same-year round-trip Rs 13.03 Cr loan, the Rs 21.00 Cr ICD facility from Vigilance Security Services, and the Rs 6.00 Cr ICD to Sreenidi-Deccan Football Club, and why place cash with three non-operating counterparties in the same year rather than repay debt or return it to shareholders?"
  - "Given Atum Life's net worth fell 71% in FY26 alone to Rs 0.32 Cr against a Rs 7.795 Cr cost, why was the ICD due date extended (on-demand to March 2028) instead of impairing the investment, and what is management's basis for treating recoverability as unimpaired?"
  - "The loan-term modification also removed Rs 2.80 Cr from Note 47's related-party on-demand-loan disclosure even as total related-party ICD exposure grew 19.4%; was this disclosure effect considered when the term change was approved?"
  - "What specifically drove Synthetic Yarn segment profit's 934% jump (cost, pricing, or mix), and is it repeatable, given it delivered 27% of the total segment-profit recovery on only 15.6% of revenue?"
  - "With FY26 dividend per share raised 140% in the same year as a Rs 59.70 Cr one-time land-sale gain, is the payout calibrated to the recurring earnings base (~Rs 37 Cr ex-exceptional) or to headline PAT?"
  - "Of the two critical judgements named in Note 2 (recoverability of subsidiary investments; ICD impairment), one was written off in full this year and one has not moved at all -- what differentiates management's assessment of the two?"
receivables_trend: "deteriorating - consolidated gross trade receivables >1-year ageing tail rose from 6.1% (FY25, Rs 12.15 Cr of Rs 199.12 Cr gross) to 9.6% (FY26, Rs 16.80 Cr of Rs 174.88 Cr gross), a genuine but smaller move than Pass 1's originally stated 4.1%->9.6% (corrected on Pass 3 re-addition, see report Section A3); absolute receivables fell 12.2% and DSO nominally improved (9.58x vs 9.41x turnover) over the same period; standalone loss allowance held flat at Rs 8.43 Cr both years (Note 9(a)/(b) standalone AR FY26 p.174-175; Note 8(a)/(b) consolidated p.242-243)."
restatements_found: []
going_concern_language: "NONE - no going-concern qualification or material-uncertainty conclusion anywhere in the Notes or in either auditor's report; the only 'going concern' text found is the standard boilerplate Auditor/Management Responsibilities paragraph common to every Indian audit report (AR FY26 p.144-155 standalone, p.212-223 consolidated). Both audit opinions are unmodified/unqualified."
analyst_note: "Two corrections matter for downstream stages. First, Pass 1's top-ranked 'Other Income surge' finding should not be read as a Company disclosure failing: the AR itself separates other income and the exceptional land-sale gain cleanly on the face of the P&L, in the notes, and in the tax reconciliation; only an external data feed bundles them. Second, Pass 1's receivables ageing-tail deterioration was overstated (4.1%->9.6%) due to an inconsistent bucket basis between years; the corrected, still-genuine move is 6.1%->9.6%. The one finding this pass adds that neither Pass 1 nor Pass 2 assembled is the Note 47/Note 12 interaction: a mid-year loan-term change to a collapsing subsidiary mechanically shrank a mandatory related-party disclosure line while the real exposure grew 19.4%. This is the sharpest evidence in the notes that headline ratios here can move opposite to substance, and it should be the first thing verified live in claude.ai against any subsequent filing."
```
