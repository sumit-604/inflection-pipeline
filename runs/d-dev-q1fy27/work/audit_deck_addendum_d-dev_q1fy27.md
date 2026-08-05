# A5 ADVERSARY / COMPLETENESS AUDIT — Deck Presentation Addendum
**Company:** DEE Development Engineers Ltd (D-DEV / DEEDEV / BSE 544198) | **Quarter:** Q1 FY27
**Under audit:** `review_deck_addendum_d-dev_q1fy27.md` (A4 presentation addendum, layering DOC5 36-slide investor deck onto the merged results review)
**Model:** claude-opus-4-8 | **Fresh context:** re-derived from A1 deck extract, A1 results extract, and A2 deck ledger only. A3 reasoning NOT read; all A4/A3 cites re-checked, not deferred to.
Anchor convention: `deck L###` = deck extract line; `res L###` = results extract line; `led …` = A2 deck ledger row.

---

## AUDIT 0 — DELIVERABLE / BRIEF-DELTA COMPLETENESS (hard gate)

This is an ADDENDUM: the standing four-part plain-language brief (narrative / sector / business-model / competition) lives in the merged review it extends (`review_d-dev_q1fy27.md`, referenced deck-addendum L6). The addendum's own deliverable is the **PLAIN-LANGUAGE BRIEF DELTA** (task item e). Assessed on that basis:

| Part | Present? | Basis |
|---|---|---|
| Brief-delta narrative (Section 7) | **PRESENT / non-empty** — 5 paragraphs, plain-language, numbers-first | addendum L188-198 |
| Sector intelligence (delta) | Present inside delta — TAM/industry drivers (thermal, refining, nuclear, data-center, semis) and the Vision-2030 growth frame | addendum L53, L192 |
| Business-model intelligence (delta) | Present inside delta — order intake vs execution, InVIT pellet optionality, plant-level capacity | addendum L192 |
| Competition intelligence (delta) | Present inside delta — "India's largest process piping capacity," marquee wins/BPCL, global-OEM LOI | addendum L49, L192 |

House-style check on Section 7: numbers-first, symmetric, no em/en-dashes used as punctuation, no landing line. One minor nit only: "the above-19 goal" (addendum L196) is a hyphenated compound modifier (STYLE discourages hyphenated compound modifiers). Non-blocking, does not fail the gate. **BRIEF-DELTA GATE: PASS.**

---

## AUDIT 1 — COVERAGE (fresh grep re-enumeration vs A2 ledger, and material-unit accounting in A4)

### 1a. Fresh count vs ledger (independent grep of `ledger_deck_…md`)

| Category | A2 count | My fresh grep | Orphan rows | Missing-from-ledger | Status |
|---|---|---|---|---|---|
| Slides (SLD-) | 36 | 36 | none | none | MATCH |
| Financial metrics (FM-) | 132 | 132 | none | none | MATCH |
| Forward-looking (FL-) | 34 | 34 | none | none | MATCH |
| Order-book (OB-) | 26 | 26 | none | none | MATCH |
| Capacity rows (CAP-) | 34 | 34 | none | none | MATCH |
| Chart data points (CH-) | 80 | 80 | none | none | MATCH |

Every A2 count reproduces on my own grep pass. No orphan row, no missing row. GATE A2 independently re-confirmed.

### 1b. Material-unit accounting in the A4 addendum

| Material unit (task-named) | Covered in addendum? | Cite |
|---|---|---|
| 36 slides | Material slides all addressed; qualitative-only slides (p12/p15/p21/p22/p25/p26 process/portfolio, no figures) carry no finding and are non-material to thesis | addendum §2-§5 |
| 34 forward-looking statements | Covered — Vision-2030 waypoints, margin/PAT/asset-turn guidance, InVIT (FL-015), pellet Rs.80cr, TAM drivers, Safe-Harbor disclaimer noted | addendum L45-53 |
| 26 order-book data points | Covered — intake 780.87, executed 294.37, closing 2,428.20, composition 93/7 & 89/9/2, marquee wins, book-to-bill | addendum L38-49 |
| Vision-2030 slide (SLD-29) | Covered in depth (DF-11 margin, DF-13 CAGR/run-rate) | addendum §4.1, §4.4 |
| Capacity rows (CAP) | Covered — segment + facility-level breakdown, Chennai ZERO_STANDING noted | addendum L43-44 |
| Shareholding / market slide (SLD-35) | Covered — CMP 658, mktcap 4,952, 7.52 cr shares, 65/19/16, marquee investors | addendum L50, L54, L163 |

**Silent-drop test (does any deck slide partially answer / contradict an open question yet go unaddressed?):** No. The addendum runs all 19 open questions against the deck (§3) with ANSWERED / PARTIAL / DID-NOT-ADDRESS dispositions and cites. Note p19 core-business Op.EBITDA margin **17.8%, +40bps YoY** (FM-057, deck L572-575) is a genuine bull data point the addendum does not spotlight; but it does not *contradict* the walk-back finding (consolidated 16.9% is the guidance basis, and core 17.8% is still below the >19% bar), so this is a de-emphasis, not a dropped contradiction. **No coverage FAIL.**

---

## AUDIT 2 — ARITHMETIC / RECONCILIATION RE-RUN (recomputed from raw extracts)

### 2a. Deck P&L → audited consolidated filing (four key lines)

| Line | Deck | Filing (raw lacs, res) | Filing → Cr | My recompute / tie | Status |
|---|---|---|---|---|---|
| Revenue from operations | 294.5 | 29,446.22 (res L541) | 294.46 | ties within rounding | PASS |
| Operating EBITDA | 49.7 | 29,446.22 − (27,688.68 − 1,500.77 D&A − 1,716.30 finance) = 4,974.61 (res L541/549/550/553) | 49.75 | I independently derive 49.75; excludes other income, same as deck's "Op." definition | PASS |
| PAT | 16.1 | 1,608.30 (res L562); parent-attributable 1,614.87 (res L573) | 16.08 / 16.15 | ties within rounding | PASS |
| EPS (diluted) | 2.32 | 2.32 (res L588) | 2.32 | ties exactly | PASS |

Reconciliation verdict CONFIRMED — independently reproduced. The forensic weight is in omission/framing, not numeric divergence. A4's reconciliation call stands.

### 2b. Book-to-bill

Intake 780.87 (deck L494, led OB-013) / Executed 294.37 (deck L215, led OB-012) = **2.6527 → 2.65x**. A4 claim 2.65x **PASS**. (Definitional caveat valid: two different "YTD" metrics — execution vs new intake — correctly routed to Q29.)

### 2c. Q1 annualised run-rate vs deck forward figures

- Annualised = 294.5 × 4 = **1,178.0 Cr** (A4: 1,178 — PASS)
- vs FY27E 1,500 (deck L869): 1,178/1,500 − 1 = **−21.5%** (A4: "~21% below" — PASS)
- QoQ = 294.5/361.6 − 1 = **−18.6%** (deck L958 — PASS)
- Bridge to hit FY27E: (1,500 − 294.5)/3 = **401.8/qtr ≈ 402** (A4: ~402 — PASS); step-up 402/294.5 = **+36.5%**, above Q4 FY26 peak 361.6 — PASS

### 2d. Vision-2030 CAGR checks

| Metric | My recompute | Deck / A4 | Status |
|---|---|---|---|
| **CAGR from FY25A 827 base → FY30E 2,500 (5yr)** | (2500/827)^(1/5) − 1 = **24.8%** | — (task-requested; deck does not print this window) | computed |
| Deck's stated FY26A 1,142 → FY30E 2,500 (4yr) | (2500/1142)^(1/4) − 1 = **21.6%** | deck "~22%" (L880); A4 21.6% | PASS |
| Op.EBITDA CAGR: FY30 EBITDA 2,500×19.5% = 488; (488/189.3)^(1/4) − 1 = **26.7%** | deck "~26%" (L874); A4 26.7% | PASS |
| Required CAGR from run-rate: (2500/1178)^(1/3) − 1 = **28.5%** | A4 ~28.5% | PASS |

**On-or-off-path verdict (independent):** On the FY25A 24.8% path, implied FY27 ≈ 827×1.248² = **1,288 Cr**; on the deck's own trajectory the FY27E waypoint is **1,500 Cr**. Q1 annualises to **1,178 Cr**, below both. **This quarter is OFF the Vision-2030 path** — confirmed. To recover, Q2-Q4 must average ~402 Cr (+36% on Q1). A4's DF-13 read reproduces exactly.

**No arithmetic mismatch above rounding anywhere.**

---

## AUDIT 3 — ADVERSARIAL READ (task-scoped a–e)

### (a) Margin walk-back — is "WALKED BACK from FY27 to FY30" supported, or over-read?
Deck verbatim, re-read from extract: L862 "Unlocking ₹2,500 Cr Revenue with 20% Margins **by FY30**"; L873/L888 "Op.EBITDA Guidance: 19-20% margin **by FY30**." No FY27 (or FY28) margin figure exists anywhere in the deck — the p29 panel gives FY27E/FY28E/FY30E **revenue** waypoints (1,500/1,800/2,500) but a **margin** number only "by FY30." Q1 FY27 actual is 16.9% (deck L960). Notion recorded FY27 consolidated EBITDA guidance ">19%."
**My independent call: WALK-BACK / deferral is SUPPORTED, and A4 did NOT over-read in either direction.** The 19-20% band is anchored solely to FY30 with no coexisting nearer FY27 milestone, which cannot be read as reaffirming a >19% FY27 bar. Critically, A4 does **not** overclaim a formal withdrawal — it states the FY27 figure is "neither shown nor reaffirmed" and routes the definitive question to **mandatory Q26**. That is the correctly calibrated read: a wrong walk-back in either direction is avoided. **No surviving counter.**

### (b) The two RED-FLAG omission findings — faithful or overstated?
- **DF-09 (no qualification/impairment/EoM language in 36 slides):** I grep-tested the deck extract for `impairment|qualified|qualification|emphasis of matter|limited review`. Zero substantive hits — the only "qualification" hit is "qualification barriers" (deck L211, technical-bidding context). The Malwa matter that carries the **QUALIFIED consolidated conclusion** (Rs.5,082.67 lacs, res L462-468) and the **PSPCL Emphasis of Matter** (res L486-494) is presented only as a tariff win (deck L390-391, L818-821). **FAITHFUL, not overstated.**
- **DF-10 (no balance sheet / net-debt / WC; leverage charts stop at FY26):** Grep for `net debt|net worth|working capital|balance sheet` returns only (i) three *rhetorical/promotional* "balance sheet" uses (deck L387/398/460 — "strengthened our balance sheet"), not a balance-sheet statement, and (ii) the p34 chart labels "Debt to Equity" and "Net Debt to EBITDA" (deck L1123/1137), which are FY22-FY26 ratio trends with **no Q1 FY27 bar**. No standing net-worth/net-debt/WC figure exists. A4 correctly honours the A2 `CHART_YEAR_MAPPING_AMBIGUOUS` flag and does not cite a year-specific p34 ND/EBITDA. **FAITHFUL, not overstated.** Both are correctly characterised as *presentation/selective-disclosure* signals, not data-integrity failures (every printed number ties — Audit 2). Watch items 4/5 support confirmed: grep for `HRSG|Nooter|BHEL` = zero hits, so "absent from 36 slides" is exact.

### (c) Did every A3 deck finding generate a question, or were any silently dropped?
Tracing all 14 DF finding-ids to their disposition: DF-01→Q20, DF-02→Q21, DF-03→Q3/Q11(existing), DF-04→Q10(existing), DF-05→Q5(existing)+Q24, DF-06→Q22, DF-07→Q2(existing), DF-08→Q23, DF-09→Q24, DF-10→Q25(+Q22), DF-11→Q26, DF-12→Q27, DF-13→Q28, DF-14→Q4(existing)+Q29. **Every finding routes to a new or existing question — none silently dropped.** New questions Q20-Q29 = **10**, running total 29. Confirmed.
*Non-blocking observation:* the preamble labels the A3 tally "10 FINDING / 7 N.A." (17 checks) yet lists **14** DF-## findings incorporated (addendum L16-17). These are two different taxonomies (checklist-check status vs granular finding-ids). I do not hold the A3 artifact (out of my input scope) so cannot fully reconcile the labels; but the material completeness test — every DF finding → a question — is satisfied on the face of the addendum, so this is a descriptive-labeling inconsistency, not a coverage gap. Flagged for A4 tidy-up, not a gate failure.

### (d) Did the addendum correctly refrain from curing flags / changing Decision Status / re-running valuation?
Yes. Decision Status stays HELD; verdict PROCEED WITH FLAGS unchanged; triggers 1 and 4 remain PROGRESSING-TOWARD (reinforced, not fired); no trigger fired; **valuation_rerun: false** with the stated basis "no pillar input moved" — correct, since the deck adds no balance-sheet input and the margin reframing is flagged, not booked into the base case (addendum L163, L204-210). The deck is treated as ADD-only ("can only ADD flags, never cure an audited one," L7). Compliant with CLAUDE.md (no exit-PE misuse; flags propagate; no valuation churn on company-authored unaudited data). **Correct.**

### (e) Brief-delta present and house-style compliant?
Present (Section 7), substantive, house-style compliant but for the single minor "above-19" compound-modifier nit noted in Audit 0. **PASS.**

---

## VERDICT

**COMPLETE.** The addendum's four reconciliation lines, the 2.65x book-to-bill, the 1,178 Cr run-rate, the OFF-path Vision-2030 read, and every internal CAGR all reproduce independently from the raw extracts within rounding. All six gated ledger categories (36/132/34/26/34/80) reproduce on a fresh grep with zero orphan and zero missing rows. The margin walk-back determination is supported by verbatim deck text and appropriately hedged to Q26 (not over-read either way). Both RED-FLAG omission findings are grep-confirmed faithful, not overstated. All 14 A3 findings route to questions (10 new, Q20-Q29). Decision Status, verdict and no-valuation-rerun discipline are correctly held. No FAIL. Proceeds to Notion save.

Non-blocking note for A4 (not a gate failure): reconcile the "10 FINDING" tally label against the 14 DF-## finding-ids listed (addendum L16-17), and drop the "above-19" hyphen for full STYLE compliance.

```yaml
stage: A5-adversary
company: "D-DEV"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:            # addendum brief-DELTA (four-part standing brief lives in the merged review this extends)
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
  ledger_recount: {slides: 36, financial_metrics: 132, forward_looking: 34, order_book: 26, capacity_rows: 34, chart_data_points: 80}
arithmetic_mismatches: []
independent_recompute:
  revenue_tie: "deck 294.5 vs filing 29,446.22 lacs = 294.46 — ties"
  ebitda_tie: "deck 49.7 vs derived 4,974.61 lacs = 49.75 (rev 29,446.22 less opex ex-D&A/finance) — ties"
  pat_tie: "deck 16.1 vs filing 1,608.30 lacs = 16.08 (parent 1,614.87 = 16.15) — ties"
  eps_tie: "deck 2.32 vs filing 2.32 — exact"
  book_to_bill: "780.87 / 294.37 = 2.65x — confirmed"
  q1_annualised: "294.5 x 4 = 1,178 Cr; vs FY27E 1,500 = -21.5% (OFF FY27E path)"
  vision_cagr_from_fy25a: "(2500/827)^(1/5)-1 = 24.8%; implied FY27 ~1,288 Cr > 1,178 annualised => OFF path"
  vision_cagr_fy26_30_stated: "(2500/1142)^(1/4)-1 = 21.6% vs deck ~22% — internally consistent"
  path_call: "OFF the Vision-2030 path this quarter"
margin_walkback_call: "WALK-BACK / deferral SUPPORTED by verbatim deck text (L862/L873/L888, no FY27 margin figure); A4 did not over-read; correctly hedged to mandatory Q26"
red_flag_findings_faithful: true    # DF-09 and DF-10 grep-confirmed (impairment/qualified/EoM/limited-review/net-debt/net-worth/WC/HRSG/Nooter/BHEL all absent from 36 slides)
findings_to_questions_complete: true # all 14 DF findings route to new/existing questions; 10 new (Q20-Q29)
valuation_rerun_correctly_avoided: true
decision_status_unchanged: "HELD"
surviving_bear_counters: []
non_blocking_notes:
  - "Addendum labels A3 tally '10 FINDING' but lists 14 DF-## findings incorporated (L16-17); different taxonomies, material findings->questions test still passes; A3 artifact out of A5 input scope so label not fully reconcilable here"
  - "STYLE: 'above-19' hyphenated compound modifier in Section 7 (L196)"
loop_back_to: ""
gap: ""
```
