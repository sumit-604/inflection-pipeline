# A3 FORENSIC NOTES: Poonawalla Fincorp (POONAWALLA) Q2FY27, doctype presentation (press release, 3 pages)

Stage: A3-forensics | Model: claude-opus-5-5 | Run date: 2026-10-17
Inputs read: extracted/poonawalla-pressrelease-q2fy27-structured.md (R001-R096), extracted/poonawalla-pressrelease-q2fy27-fulltext.md (lines 1-137), work/ledger_pressrelease_poonawalla_q2fy27.md.
Not available: prior-quarter fulltext (ND), Notion monitoring checklist (NONE: no Notion page, no companies/POONAWALLA.md, no spear on record). This is a PRE-THESIS READ.
Source PDF and inputs/ were not opened.

Lender context: the company calls itself an ND-SI-NBFC (fulltext lines 123-124). The document is a Reg 30 cover letter (p1) plus a media release (p2-p3). It carries no financial statements, no auditor report, no notes, no segment table, and no tax, EPS, share count or net worth line. Every balance-sheet check therefore falls to N.A. on this doctype. The forensic weight sits in derived ratio cross-checks (F16) and the lender silence audit (F17).

## 0. LEDGER RECONCILIATION
- Ledger IDs: 96. Structured IDs: 96. Rows read verbatim at their cited fulltext line: 96 of 96 (100%).
- Coverage check of ledger section 2 groups: all 51 NUMBER rows (R001-R051) sit in a named group. ENTITY R052-R064, FORWARD R065-R072, DATE R073-R085, QUALIFIER R086-R096 all accounted for.
- Line-cite drift in A1 (quote verified on the adjacent line; non-blocking, no claim changes):
  - R057 cited line 64; "The Board of Directors of Poonawalla Fincorp Limited" is on line 63.
  - R060 cited line 124; "Reserve Bank of India (RBI)" is on line 125.
  - R079 cited line 80; "Q4FY26" is on line 81 (the "1.81% in" figure is on line 80).
  - R096 cited line 123; "(ND-SI-NBFC)" is on line 124 (the phrase spans 123-124).
- Arithmetic re-checks of stated deltas: PAT 375 vs 308 = +21.75%, stated 21.8% (line 61) OK. NIM 9.26 minus 9.10 = 16 bps (lines 77-78) OK. Credit cost 2.40 minus 2.19 = 21 bps (lines 67-68, 83) OK.

## 1. DERIVED CROSS-CHECKS (all [INFERENCE]; inputs anchored, method stated)
Three ratios in the release each imply an average lending base. They agree, which makes the derived numbers usable as question material.
| Check | Q2FY27 | Q1FY27 | Method |
| Avg base implied by RoA | Rs 68,807 cr | Rs 62,222 cr | PAT x4 / RoA (lines 75, 80) |
| Avg base implied by NIM | Rs 68,639 cr | Rs 62,198 cr | NII x4 / NIM; Q1 NII = 1,589/1.123 = 1,415 (lines 77, 90) |
| Avg base growth QoQ | about +10.6% | | about 50% annualised |
| Credit cost, Rs (ratio path) | about Rs 377 cr | about Rs 373 cr | ratio x avg base / 4 (lines 80, 83) |
| Credit cost, Rs (P&L path) | about Rs 376 cr | about Rs 373 cr | PPoP minus PAT/(1-25.17%); Q1 PPoP = 877/1.118 = 784 (lines 75, 92). ETR not disclosed; statutory rate assumed |
| Implied opex | about Rs 712 cr | about Rs 631 cr | NII minus PPoP; growth about +12.9% QoQ vs NII +12.3% |
| Implied cost/income | about 44.8% | about 44.6% | opex / NII |
| Stage 2+3 on-book | 2.1% | 2.4% | 100% minus Stage 1 (line 96) |
| Implied Stage 2 (if Stage 3 = GNPA) | about 0.9% | about 1.0% | Stage 2+3 minus GNPA (line 86) |
| Approx coverage | about 49% | about 49% | 1 minus NNPA/GNPA (lines 86, 88); approximate, NNPA denominator is net advances |
| GNPA stock upper bound | <= Rs 888 cr | | 1.20% x AUM 74,008; on-book is smaller, AUM not on-book |

Reading: absolute credit cost is flat at about Rs 373-377 cr in both quarters. The 21 bps ratio fall comes from the larger denominator, not from lower rupee losses. The absolute GNPA stock moved little; most of the 17 bps GNPA fall is also denominator.

## 2. FINDINGS TABLE
| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F6 | R046, R047, R048, R071 | 105-106, 117 | "bringing the total to 143 cutting-edge AI projects, of which 84 projects have been successfully implemented"; "Accelerated by our rapidly maturing proprietary AI layer" | AMBIGUOUS | 59 projects (143 minus 84) are open with no date. Prior total implied 101 (143 minus 42). The CEO credits AI for the gains, but the release gives counts only, no rupee effect. Implied opex grew about 12.9% QoQ against NII 12.3%, so cost/income did not improve (about 44.6% to 44.8%). Track the implemented count each quarter and ask for a measured opex or credit benefit. |
| A3-02 | F6 | R040, R041, R042, R066 | 98-99 | "well above the regulatory requirement of 15% providing enough headroom for growth" | FORWARD-SIGNAL | Headroom is 3.68 pp of CAR. Tier-1 is 17.15%. The average base grows about 10.6% QoQ (Section 1). If risk-weighted assets track the book, that pace uses about 1.6 pp of CAR per quarter, against about 0.5 pp of accrual at a 2.18% RoA. On that assumption, the buffer lasts about 3-4 quarters before a capital raise or slower growth. This is the main dated funding risk. Watch the enabling resolutions. |
| A3-03 | F14 | R016, R017, R091, R095; R014, R090 | 67-68 vs 83, 90 | "NII grew by 12.3% QoQ to ₹1,589 crore" (line 68) vs "Net Interest Income (inc. fees and other income)" (line 90); "Credit cost at 2.19%" (line 67) vs "Credit cost as a percentage to average AUM" (line 83) | NEUTRAL-FACT | The lead paragraph drops both definitional qualifiers. The headline NII includes fees and other income and is not core NII. A data point on drafting care. No forward effect alone. |
| A3-04 | F14 | R052, R057, R088 | 63-65, 71 | "today announced its unaudited financial results for the quarter ended September 30, 2026" | AMBIGUOUS | The release never says whether the numbers are standalone or consolidated. F2 to F4 cannot run until the results filing fixes the basis. Ask which basis the release uses and whether any subsidiary or JV is in scope. |
| A3-05 | F14 | R086 | 55 | "Classification \| INTERNAL" | NEUTRAL-FACT | A public exchange filing carries an INTERNAL marking. Template residue. Individually immaterial. |
| A3-06 | F16 | R009, R012, R018, R050; R068 | 60, 67, 73, 128; 113 | "AUM stood at ₹74,008 crore"; "We have delivered disciplined AUM expansion" | AMBIGUOUS | AUM appears four times as a level with no growth rate and no prior-period figure. PAT, NII and PPoP each get a growth rate. The derived average base grew about 10.6% QoQ, about 50% annualised. "Disciplined" is unquantified. Fast growth flatters every per-average-AUM ratio now, and loss seasoning lands in 12-18 months. Ask for QoQ and YoY AUM growth and disbursements. |
| A3-07 | F16 | R014, R015, R027, R028, R029-R032, R070 | 67-68, 83, 86, 116-117 | "Credit cost at 2.19%, a reduction of 21 bps"; "driven credit costs lower from an already formidable baseline, translating directly into a structural lift in our Return on Assets" | FORWARD-SIGNAL | Two independent derivations put rupee credit cost at about Rs 373 cr (Q1) and about Rs 376-377 cr (Q2), so flat. The "reduction" and the claimed "structural lift" in RoA are denominator effects of book growth. The GNPA fall from 1.37% to 1.20% also follows the denominator. If growth slows, the ratios will rise again with no change in rupee losses. Lean bear: treat the RoA lift as unproven until rupee credit cost falls. |
| A3-08 | F16 | R024, R025, R026, R079 | 80-81 | "RoA ... stood at 2.18% in Q2FY27 vs 1.98% in Q1FY27 and 1.81% in Q4FY26" | AMBIGUOUS | RoA is the only metric shown with a three-quarter series, and it is the best-trending one. Every other metric gets one QoQ comparator, and no metric has a YoY comparator. This is a selective-baseline pattern. Ask for YoY on PAT, AUM, credit cost and GNPA. |
| A3-09 | F16 | R037, R093, R069 | 94, 114-115 | "Secured to Unsecured on-book mix at 52:48"; "strong pricing power across core and newly incubated verticals" | AMBIGUOUS | The mix is given for Q2 only with no Q1 comparator. "On-book" implies an off-book book (co-lending or assignment) that is not sized. The release lists 13 products (lines 129-132) and new verticals, but gives no product AUM split. A rising unsecured share would explain both the NIM gain and a future credit cost lag. Ask for the mix trend, the off-book share and the AUM split by vertical. |
| A3-10 | F16 | R021, R022, R023, R089, R044, R045 | 77-78, 103 | "NIM (inc. fees and other income) at 9.26% in Q2FY27 vs 9.10%"; "Cost of Borrowing at 7.76% for this quarter, 4 bps higher than Q1FY27" | AMBIGUOUS | The NIM figure includes fees and other income, and core NIM is not disclosed. Funding cost rose 4 bps while the blended margin rose 16 bps. The gain may come from fees or from an unsecured mix shift, not from loan pricing. Ask for core NIM, the fee-income share and the borrowing mix behind the CoB rise. |
| A3-11 | F17 | R029-R032, R038, R039 | 86-88, 96 | "GNPA stood at 1.20% in Q2FY27"; "Stage 1 Assets stood at 97.9% of on-book assets" | AMBIGUOUS | Quarterly credit cost of about Rs 376 cr is at least 42% of the GNPA stock upper bound (Rs 888 cr). This points to heavy write-offs keeping GNPA low. Write-offs are not disclosed. Implied Stage 2 of about 0.9% is thin for a book that is 48% unsecured. Approximate coverage is about 49%. Ask for gross write-offs, recoveries, Stage 2 and 3 levels and ECL coverage by stage. |
| A3-12 | F17 | (absence; ledger section 8) | 71-106 | "Financial highlights for the quarter ended September 30, 2026:" (scope scanned) | AMBIGUOUS | 9 standard lender monitorables are silent (see table). This is the first observed quarter (prior ND), so silence count = 1. No confirmatory negative yet. Each row becomes an A4 question. |

## 3. CHECKLIST SCORECARD
| Check | Status | Basis |
|---|---|---|
| F1 | N.A. | No financial statement template in a press release. Ledger section 7: zero ZERO_STANDING rows, no tables. |
| F2 | N.A. | No standalone or consolidated statements. The basis is not stated (see A3-04). |
| F3 | N.A. | No cost lines, standalone or consolidated. |
| F4 | N.A. | No auditor report or Other Matters paragraph in this doctype. The release says only "unaudited" (lines 33, 65). Run F4 on the results filing. |
| F5 | N.A. | No EoM or going-concern text, and no prior-quarter fulltext for a verbatim diff. Run on the results filing. |
| F6 | FINDING | Zero literal lexicon hits. Two forward items carry trackable status: the AI project pipeline (A3-01) and the CAR headroom claim (A3-02). Register below. |
| F7 | PASS | Zero hedge-lexicon hits in lines 1-137. Note: the CEO quote (lines 111-119) makes unhedged forward claims, and the document has no safe-harbour text. That is weighed under A3-07, not as a hedge. |
| F8 | N.A. | No tax, PBT or deferred-tax line. ETR not disclosed. The statutory rate is used only as an assumption in Section 1. |
| F9 | N.A. | No OCI line. |
| F10 | N.A. | No paid-up capital, share count or EPS in the release. |
| F11 | N.A. | No net worth or other equity figure to tie. CAR 18.68% and Tier-1 17.15% (line 98) are ratios only. |
| F12 | N.A. | No segment assets or liabilities table. The only split is the one-period secured:unsecured mix (line 94), weighed under A3-09. Run F12 on the results filing or the investor deck. |
| F13 | PASS | Lines 63-65 report only the results announcement. No dividend, fund-raise, AGM, AR approval or director change is in this document. The board outcome letter was not supplied. |
| F14 | FINDING | Qualifier omissions in the lead paragraph (A3-03), consolidation basis unstated (A3-04), INTERNAL marking on a public filing (A3-05). |
| F15 | N.A. | No consolidation entity list and no prior quarter to diff. Ledger section 3: ENTITY_CHANGE not testable. |
| F16 | FINDING | The prior deck is ND, so the dropped-metric diff was not run. The in-document reframing tests found AUM growth withheld (A3-06), a ratio-only credit cost "reduction" (A3-07), a selective RoA baseline (A3-08), a mix with no comparator (A3-09) and a non-standard NIM (A3-10). |
| F17 | FINDING | Run at the orchestrator's instruction against standard lender monitorables. The Notion checklist was not supplied (pre-thesis). 9 silent items (A3-11, A3-12). |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit; checklist not supplied, standard lender monitorables used)
| Monitorable | Status in release | Line ref | Consecutive quarters silent |
|---|---|---|---|
| AUM | Level only, no growth % | 60, 73 | 1 (growth %) |
| Disbursement | SILENT | scope 71-106 | 1 (first observed; prior ND) |
| NIM | Disclosed incl. fees; core NIM silent | 77 | 1 (core NIM) |
| Cost of funds | Disclosed 7.76%, +4 bps | 103 | 0 |
| Credit cost | Disclosed as a ratio; rupee amount silent | 83 | 1 (rupee amount) |
| GNPA / NNPA | Disclosed | 86, 88 | 0 |
| Stage 2 / Stage 3 | Stage 1 only; Stage 2 and 3 silent | 96 | 1 |
| ECL coverage / PCR | SILENT (about 49% derived) | scope 71-106 | 1 |
| Write-offs | SILENT | scope 71-106 | 1 |
| CRAR / Tier-1 | Disclosed | 98 | 0 |
| ALM | SILENT | scope 71-106 | 1 |
| Borrowing mix | SILENT | scope 71-106 | 1 |
| Liquidity | Disclosed Rs 6,526 cr | 101 | 0 |
| YoY comparators (any metric) | SILENT | scope 60-106 | 1 |
| RoE / net worth | SILENT | scope 60-106 | 1 |
| Off-book / co-lending share | SILENT ("on-book" implies off-book exists) | 94, 96 | 1 |

## 5. COMMITMENT REGISTER (F6)
Literal lexicon hits: 0. The register lists the forward items that carry a trackable status.
| Commitment | Implied date | Ref | Status word |
|---|---|---|---|
| AI programme: 143 projects, 84 implemented, 59 open; 42 added in Q2 | none stated | lines 105-106 (R046-R048) | underway (59 open); completed (84) |
| CAR "providing enough headroom for growth" | none stated; about 3-4 quarters of runway on the derived pace [INFERENCE] | lines 98-99 (R066) | claim |
| Business focus "consumer and MSME finance" | standing | line 64 (R065) | standing |
| "Structural lift" in RoA from lower credit cost; "disciplined AUM expansion" | implied ongoing | lines 113, 116-117 (R068, R070) | claim (unproven per A3-07) |
| "Newly incubated verticals" | none stated | line 115 (R069) | initiated |

## 6. FLAGS FOR A4 (management questions)
- FORWARD-SIGNAL: A3-02, A3-07.
- AMBIGUOUS: A3-01, A3-04, A3-06, A3-08, A3-09, A3-10, A3-11, A3-12.
- A3 did not judge the thesis. No thesis exists for this name (pre-thesis read).

```yaml
stage: A3-forensics
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "presentation"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/poonawalla-q2fy27/work/forensics_pressrelease_poonawalla_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: N.A.
  F13: PASS
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A3-01", check: "F6", line: "105-106, 117", classification: "AMBIGUOUS", implication: "59 of 143 AI projects open, undated; AI credited for gains but implied opex +12.9% QoQ vs NII +12.3%, cost/income flat about 44.8%; no rupee benefit disclosed"}
  - {id: "A3-02", check: "F6", line: "98-99", classification: "FORWARD-SIGNAL", implication: "CAR 18.68% vs 15% floor; at about 10.6% QoQ avg-base growth the 3.68 pp buffer lasts about 3-4 quarters [INFERENCE, RWA tracks book]; capital raise or growth slowdown ahead"}
  - {id: "A3-03", check: "F14", line: "67-68 vs 83, 90", classification: "NEUTRAL-FACT", implication: "lead para drops NII incl-fees and credit-cost avg-AUM qualifiers; headline NII is not core NII"}
  - {id: "A3-04", check: "F14", line: "63-65, 71", classification: "AMBIGUOUS", implication: "standalone vs consolidated basis never stated; F2-F4 blocked until results filing fixes it"}
  - {id: "A3-05", check: "F14", line: "55", classification: "NEUTRAL-FACT", implication: "INTERNAL classification marking on a public exchange filing; template residue"}
  - {id: "A3-06", check: "F16", line: "60, 67, 73, 113, 128", classification: "AMBIGUOUS", implication: "AUM growth withheld while PAT/NII/PPoP growth shown; derived avg base +10.6% QoQ (about 50% annualised); per-avg-AUM ratios flattered, seasoning lag 12-18 months"}
  - {id: "A3-07", check: "F16", line: "67-68, 83, 86, 116-117", classification: "FORWARD-SIGNAL", implication: "rupee credit cost flat about Rs 373-377 cr both quarters (two derivations); 21 bps fall and RoA structural lift are denominator effects; ratios reverse if growth slows"}
  - {id: "A3-08", check: "F16", line: "80-81", classification: "AMBIGUOUS", implication: "only RoA gets a three-quarter series; no YoY comparator for any metric; selective baseline"}
  - {id: "A3-09", check: "F16", line: "94, 114-115", classification: "AMBIGUOUS", implication: "52:48 secured:unsecured mix has no Q1 comparator; off-book share unsized; newly incubated verticals with no AUM split"}
  - {id: "A3-10", check: "F16", line: "77-78, 103", classification: "AMBIGUOUS", implication: "NIM includes fees and other income; core NIM undisclosed; NIM +16 bps vs CoB +4 bps may be fee or unsecured-mix driven"}
  - {id: "A3-11", check: "F17", line: "86-88, 96", classification: "AMBIGUOUS", implication: "quarterly credit cost >=42% of GNPA stock upper bound implies heavy write-offs, undisclosed; implied Stage 2 about 0.9% thin for 48% unsecured book; coverage about 49%"}
  - {id: "A3-12", check: "F17", line: "71-106", classification: "AMBIGUOUS", implication: "9 lender monitorables silent (disbursement, write-offs, ECL coverage, Stage 2/3, ALM, borrowing mix, YoY, RoE/net worth, off-book share); silence count 1, first observed quarter"}
forward_signals: ["A3-02", "A3-07"]
ambiguous: ["A3-01", "A3-04", "A3-06", "A3-08", "A3-09", "A3-10", "A3-11", "A3-12"]
commitments:
  - {commitment: "AI programme 143 projects, 84 implemented, 59 open, 42 added Q2", implied_date: "none stated", ref: "lines 105-106 (R046-R048)", status_word: "underway"}
  - {commitment: "CAR provides enough headroom for growth", implied_date: "none stated; about 3-4 quarters runway [INFERENCE]", ref: "lines 98-99 (R066)", status_word: "claim"}
  - {commitment: "focus on consumer and MSME finance", implied_date: "standing", ref: "line 64 (R065)", status_word: "standing"}
  - {commitment: "structural RoA lift from lower credit cost; disciplined AUM expansion", implied_date: "implied ongoing", ref: "lines 113, 116-117 (R068, R070)", status_word: "claim"}
  - {commitment: "newly incubated verticals", implied_date: "none stated", ref: "line 115 (R069)", status_word: "initiated"}
gate_a3: pass
blank_checks: []
analyst_note: "Press release only: no statements, auditor text or segments, so F1-F5 and F8-F12 are N.A. Run them on the results filing. Three independent ratios (RoA, NIM, credit cost) imply the same average base: about Rs 68.7k cr in Q2 vs 62.2k cr in Q1, so about 10.6% QoQ growth. The release withholds that growth rate. On that base, rupee credit cost is flat at about Rs 375 cr. The headline 21 bps credit-cost fall, the GNPA fall and the CEO's 'structural lift in RoA' are mostly denominator effects of fast book growth on a 48% unsecured book. Quarterly credit cost is at least 42% of the GNPA stock, which points to write-offs doing the work behind a low GNPA. The bear reading: ratios reverse when growth slows and seasoning arrives. The bull reading: pricing and fee income lift PPoP while losses stay flat in rupees. The separating observation is rupee credit cost and gross write-offs over the next two quarters against disbursement growth. At this growth pace, capital headroom of 3.68 pp is about 3-4 quarters, so watch for a raise. A1 line-cite drift on R057, R060, R079 and R096 is non-blocking."
```
