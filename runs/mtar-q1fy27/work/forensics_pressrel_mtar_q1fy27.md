# A3 FORENSIC NOTES — MTAR Technologies (MTAR) — Q1 FY27 — DOCTYPE: presentation (SEBI Reg 30(6) Investors Press Release, 4 pages)

Source doc (this): `/home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_pressrel_mtar_q1fy27.txt`
Ledger: `/home/user/inflection-pipeline/runs/mtar-q1fy27/work/ledger_pressrel_mtar_q1fy27.md`
Cross-doc results filing: `/home/user/inflection-pipeline/runs/mtar-q1fy27/work/extract_results_mtar_q1fy27.txt`
Prior-quarter press release: NONE (first run).

Ledger reconciliation: 54/54 rows read verbatim at their cited extract line (26 financial numbers + 5 segment claims + 1 operational metric + 3 MD commentary + 5 footnotes/disclaimer + 14 administrative). 100% reconciled. Ledger records 0 ZERO_STANDING rows (narrative doctype, no results table) — consistent with the source.

Doctype application per task brief: APPLY F6, F7, F16 (F16 diff portion N.A. — no prior PR — current-framing portion assessed), F14 extended to cross-document number reconciliation, F10/F11 only if numbers appear (none appear). N.A. for results-filing-only checks: F1, F2, F3, F4, F5, F8, F9, F12, F13, F15, F17.

---

## CRITICAL CROSS-DOCUMENT RECONCILIATION (run under F14)

Press release states figures in Rs Cr in-text and declares them CONSOLIDATED (line 83: "unaudited consolidated financial results"). Results filing is in INR millions (x0.1 = Cr). Standalone = page 5; Consolidated = page 6. Every PR number tested against BOTH bases; the basis each matches is stated.

| PR item (ledger) | PR line | PR value | Standalone (p5, Cr) | Consolidated (p6, Cr) | Ties to | Match |
|---|---|---|---|---|---|---|
| Revenue Q1FY27 (FN3) | 90 | 360.7 | 360.72 | 360.72 | both (identical) | YES |
| Revenue Q1FY26 (FN4) | 90-91 | 156.6 | 156.58 | 156.58 | both (identical) | YES |
| Revenue Q4FY26 (FN16) | 102-103 | 306.1 | 306.03 -> 306.0 | 306.07 -> 306.1 | CONSOLIDATED | YES |
| Revenue YoY (FN5) | 91 | 130.4% | — | 360.72/156.58-1 = 130.4% | consol | YES |
| Revenue QoQ (FN17) | 103 | 17.9% | — | 360.72/306.07-1 = 17.9% | consol | YES |
| EBITDA Q1FY27 (FN6) | 92 | 85.1 | 84.93 -> 84.9 | 85.05 -> 85.1 | CONSOLIDATED | YES |
| EBITDA Q1FY26 (FN7) | 92 | 28.4 | 28.5 | 28.38 -> 28.4 | consol | YES |
| EBITDA Q4FY26 (FN19) | 104 | 61.8 | 61.9 | 61.81 -> 61.8 | consol | YES |
| EBITDA YoY (FN8) | 93 | 199.7% | — | 85.05/28.38-1 = 199.7% | consol | YES |
| EBITDA QoQ (FN20) | 105 | 37.6% | — | 85.05/61.81-1 = 37.6% | consol | YES |
| PBT Q1FY27 (FN9) | 94 | 67.4 | 67.64 -> 67.6 | 67.40 | CONSOLIDATED | YES |
| PBT Q1FY26 (FN10) | 94-95 | 14.8 | 15.20 | 14.81 -> 14.8 | CONSOLIDATED | YES |
| PBT Q4FY26 (FN22) | 106-107 | 59.5 | 59.61 -> 59.6 | 59.54 -> 59.5 | CONSOLIDATED | YES |
| PBT YoY (FN11) | 95 | 355.0% | — | 67.40/14.81-1 = 355.0% | consol | YES |
| PBT QoQ (FN23) | 107 | 13.2% | — | 67.40/59.54-1 = 13.2% | consol | YES |
| PAT Q1FY27 (FN12) | 96 | 50.2 | 50.50 | 50.23 -> 50.2 | CONSOLIDATED | YES |
| PAT Q1FY26 (FN13) | 96-97 | 10.8 | 11.23 | 10.81 -> 10.8 | CONSOLIDATED | YES |
| PAT Q4FY26 (FN25) | 108 | 44.3 | 44.34 -> 44.3 | 44.28 -> 44.3 | both round to 44.3 | YES |
| PAT YoY (FN14) | 97 | 364.5% | — | 50.23/10.81-1 = 364.6% ~ 364.5% | consol | YES |
| PAT QoQ (FN26) | 108-109 | 13.4% | — | 50.23/44.28-1 = 13.4% | consol | YES |

Discriminators (Q4FY26 revenue, all EBITDA, all PBT, Q1FY27/Q1FY26 PAT) each resolve to the CONSOLIDATED column, never standalone. Consistent with the PR's own basis statement (line 83). No PR number fails to tie. NO reconciliation FINDING on the discrepancy axis.

EBITDA DEFINITION (load-bearing for the promise tracker): PR "EBITDA" of Rs 85.1 Cr reconciles to consolidated ONLY when Other Income (Rs 7.9 Cr; p6 line 397, 78.87 mn) is EXCLUDED. i.e. MTAR EBITDA = Total Revenue from Operations 3,607.21 minus [Cost of materials 2,043.19 + Change in WIP inventory (78.16) + Employee 465.20 + Other expenses 326.44] = 850.54 mn = Rs 85.05 Cr. Had Other Income been included, "EBITDA" would read ~Rs 92.9 Cr. Recorded as F14-01 (NEUTRAL-FACT) so future quarters compare like-for-like.

CONFIRMATORY POSITIVE (Notion checklist item 4): implied consolidated EBITDA margin = 85.05/360.72 = 23.6%, ABOVE Q3 FY26 record ~23%. The PR does NOT print this % (see F16); it must be computed. Margin-sustain monitorable is met on this quarter's math.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-F6-01 | F6 | MD1 | p3 L112-113 | "in line with the growth guidance provided for the current fiscal year" | FORWARD-SIGNAL | FY27 growth guidance reaffirmed. But Q1 YoY +130.4% vastly outpaces the ~50% FY27 revenue-growth guidance (Notion L34); largely a soft Q1 FY26 base (156.6 Cr). A4: will full-year guidance be revised, or does H2 decelerate? Datable to FY27 close. |
| A3-F6-02 | F6 | MD3 | p3 L114-116 | "each of our key business verticals positioned for the next phase of growth" | FORWARD-SIGNAL | Vertical-level growth signaled but unquantified and unnamed. A4: which verticals — Clean Energy/Bloom hot-box (12k->20k Dec-26), Civil Nuclear (Kaiga 5&6 PO), O&G/Weatherford commissioning (Jun-Sep 26)? Convert to per-vertical monitorable questions. |
| A3-F7-01 | F7 | MD3 / FD4 | p3 L115 / p4 L140 | "We believe we are at an inflection point" ; "Actual results might differ substantially" | AMBIGUOUS | Optimistic unquantified framing paired with boilerplate legal hedge. Notably NO operational hedge on US tariff (Notion: 79% revenue export) or Bloom customer concentration, both live named risks. A4: ask management to address tariff/concentration exposure explicitly. |
| A3-F14-01 | F14 | FN3-FN26 (all 26) | p2 L90-109 vs results p6 | "Rs. 85.1 Cr." (EBITDA) | NEUTRAL-FACT | All 26 PR numbers tie to CONSOLIDATED filing. "EBITDA" reconciles only when Other Income (Rs 7.9 Cr) is EXCLUDED; MTAR EBITDA = Revenue from operations minus operating expenses. Record the definition for cross-quarter promise-vs-delivery consistency. |
| A3-F16-01 | F16 | SG1/SG4/OM1 + absence set | p2 L77, L87-109; p4 L118-122 | "highest ever revenue in Q1 FY 27" | AMBIGUOUS | PR leads with superlative + growth-% framing and OMITS every quantitative monitorable: order book/inflow (Kaiga ~Rs 500 Cr, Bloom PO Rs 2,279 Cr), segment-wise revenue, EBITDA margin %, PAT margin, EPS, WC days (<200 target), capex, headcount. Omission of order book despite it being the highest-value catalyst is the notable framing choice. A4: source all of these from the results filing / concall; do not let the press-release framing set the narrative. |

No FINDING requires escalation as a mechanical failure; per CLAUDE.md there is no STOP verdict. Flags propagate.

---

## CHECKLIST SCORECARD (all 17; one status each)

| Check | Status | One-line basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Narrative press release; no results table; ledger records 0 ZERO_STANDING rows. |
| F2 Standalone vs consolidated decomposition | N.A. | PR reports consolidated only; no standalone figures in PR to decompose. Basis confirmed CONSOLIDATED via F14 cross-doc. |
| F3 Shell-entity detection | N.A. | Cost-line S-vs-C comparison is a results-filing check; not present in PR. |
| F4 Unaudited contribution ratio | N.A. | Auditor Other-Matters not in PR (lives in results filing p8). |
| F5 Going concern / EoM scope | N.A. | No EoM/going-concern paragraph in PR; no prior quarter to diff. |
| F6 Forward-commitment phrase mining | FINDING | MD reaffirms FY27 growth guidance (MD1) and signals per-vertical "next phase of growth" (MD3); no hard-lexicon dated milestones present — commitments are guidance-level. See A3-F6-01/02. |
| F7 Hedge phrase mining | FINDING | Optimistic "inflection point" framing + boilerplate FLS disclaimer ("subject to", "might differ substantially"); no operational hedge on tariff/concentration despite live risks. See A3-F7-01. |
| F8 Tax forensics | N.A. | Tax lines not in PR (implied ETR ~25.5% only derivable; check belongs to results filing). |
| F9 OCI forensics | N.A. | No OCI disclosed in PR. |
| F10 Share count / dilution | N.A. | No paid-up capital, no EPS (basic/diluted) in PR. |
| F11 Reserves / net worth tie-out | N.A. | No reserves/net-worth number in PR. |
| F12 Segment forensics | N.A. | No segment assets/liabilities/revenue split in PR; results filing declares single Ind AS 108 segment. |
| F13 Board outcome beyond results | N.A. | Board agenda/AGM/director items live in the results filing cover letter, not this PR. |
| F14 Note-drafting / cross-doc reconciliation | FINDING | All 26 numbers tie to CONSOLIDATED filing; EBITDA reconciles only excluding Other Income — definition recorded. See A3-F14-01. |
| F15 Entity list diffs | N.A. | No consolidation list in PR; no prior quarter. |
| F16 Presentation dropped/reframed disclosures | FINDING | No prior PR (diff N.A.); current framing omits order book, margins, EPS, WC, segment split — every quantitative monitorable — while leading with "highest ever revenue" superlative. See A3-F16-01. |
| F17 Concall silence audit | N.A. | No concall transcript in scope. |

Blank checks: none. GATE A3: pass.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Quarterly performance "in line with the growth guidance provided for the current fiscal year" (FY27 guidance = ~50% revenue growth per Notion) | FY27 full year (by 31-Mar-2027) | MD1, p3 L112-113 | reaffirmed / in-progress |
| "each of our key business verticals positioned for the next phase of growth" | undated ("next phase") | MD3, p3 L114-116 | initiated / positioned |

Note for A4/Role 5 promise tracker: neither commitment is quantified in this document. The FY27 50% guidance and the per-vertical catalysts (Bloom 12k->20k, Kaiga 5&6 PO ~Rs 500 Cr, Weatherford O&G Jun-Sep 26) are the datable anchors from Notion against which these two soft commitments should be tracked at the results filing and concall.

## MONITORING-CHECKLIST COVERAGE IN THIS PR (context for A4; F17 formally N.A. — no transcript)

| Notion monitorable | Addressed in PR? |
|---|---|
| Bloom hot-box 12k Mar-26 -> 20k Dec-26 | NO — no segment/product volume disclosed. |
| Kaiga 5&6 PO ~Rs 500 Cr + refurbishment | NO — no order book / inflow figure. |
| Weatherford O&G commissioning Jun-Sep 26 + FY27 contribution | NO — not mentioned. |
| EBITDA margin sustains Q3 FY26 ~23% | NOT stated, but DERIVABLE = 23.6% (meets target this quarter). |
| WC days < 200 | NO — no balance-sheet/WC data. |
| Tripwire: promoter stake < 25% | NO — no shareholding data. |
| Tripwire: Bloom concentration | NO — no customer data. |

All named catalysts are silent in the press release; this is expected for a 4-page Reg 30(6) release but confirms the PR cannot be the monitoring source. Escalate to the results filing (already extracted) and the concall.
