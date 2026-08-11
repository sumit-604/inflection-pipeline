# QUARTERLY PIPELINE A5 — ADVERSARY / COMPLETENESS AUDIT
# Embassy Developments Limited (EMVDL) — Q1 FY27 (quarter ended 30-Jun-2026)
# Auditor: A5 (Opus 4.8) | Independent re-derivation from A1 extracts + A2 ledgers
# Verdict authority: COMPLETE only proceeds to Notion save.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The MANDATORY PLAIN-LANGUAGE BRIEF is present (review lines 462-474) with all four
labelled parts populated and provenance-tagged ([this quarter filing] / [Notion memory]):

| Brief part | Heading present | Content | Provenance-labelled | Status |
|---|---|---|---|---|
| 1. Summary narrative | line 464 | 18-line narrative (loss, presales, debt, warrants, CIRP, cash) | Yes | present |
| 2. Sector intelligence | line 467 | residential/commercial developer, Bengaluru+MMR, cost-of-debt headwind, legal overhang | Yes | present |
| 3. Business-model intelligence | line 470 | owned dev + DM fees + land bank; cash rhythm; DM-fee opacity; warrant equity swap; DTA | Yes | present |
| 4. Competition intelligence | line 473 | Prestige/Sobha/Brigade (BLR), Lodha/Godrej/DLF (MMR); win/lose axes; undisclosed benchmarks | Yes | present |

**Gate 0 result: PASS.** All four parts present, non-empty, non-placeholder.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledgers)

Fresh grep/sweep re-run of both A1 extracts, diffed against the A2 count tests.

### Results filing
| Category | A2 count | My fresh count | Derivation | Orphan rows | Status |
|---|---|---|---|---|---|
| Notes | 25 | 25 | standalone N1-11 (11) + consolidated N1-14 (14) | none | PASS |
| Line items | 57 | 57 | standalone 23 (§4) + consolidated 30 (§7) + Note-10 sub-table 4 (§8a) | none | PASS |
| Zero-standing cells | 7 | 7 | A-4(iv); S-exceptional; S-OCI-remeas; S-other equity; C-exceptional; C-OCI-remeas; C-other equity | none | PASS |
| Agenda items | 4 | 4 | A (results), B (warrants), C (Neel Virwani SMP), D (JV re-appointment) | none | PASS |
| Auditor paras | 14 | 14 | standalone 4 + consolidated 10 (1-4, 5-intro, 5a, 5b, 5c, 5-mgmt, 5-foreign) | none | PASS |
| Entities | 184 | 184 | Annexure 1 S.No 1-183 + 1 JV; ties to Note 1 "184" | none | PASS |

### Presentation
| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Slides | 33 | 33 | none | PASS |
| Table line items | 74 | 74 (11+13+13+13+7+6+11) | none | PASS |
| KPI callouts | 92 | 92 (14+12+6+18+4+4+3+9+14+8) | none | PASS |
| Chart data points | 30 | 30 | none | PASS |
| Cap-table points | 10 | 10 | none | PASS |
| Non-financial identifiers | 3 | 3 | none | PASS |
| Footnote definitions | 18 | 18 | none | PASS |
| Notes bullets (pg31) | 6 | 6 | none | PASS |
| Glossary terms (pg31) | 56 | 56 | none | PASS |
| Forward-looking rows | 12 | 12 | none | PASS |

**Every A2 count reproduces exactly on fresh enumeration. No orphan rows (all flagged
findings — STPL/CIRP, EEBPL/KIADB, NCD, SPA sale, warrants, SMP, strike-offs,
other-auditor reliance, OCR-garbled OCI, DTA — are cited in A4). No fresh row absent from
the ledger.** Coverage audit finds NO A2 or A3 defect.

**Note (not a coverage FAIL, routed to arithmetic audit):** A4's ledger-reconciliation
preamble (review line 10) restates the results line-item count as "87 financial line items
(57 standalone-side rows / 30 consolidated rows per A2 count)." The A2 ledger count test
(ledger_results line 12) records line_items = **57 total**, which is 23 standalone + 30
consolidated + 4 Note-10 sub-table rows. A2 is correct and matches my fresh sweep; A4's
"87" (and its attribution of "57 standalone" to A2) is an A4 mis-reconciliation of the
ledger, logged under Audit 2.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extracted numbers, ₹ Cr; results ₹m ×0.1)

Spot-recomputed every derived cell in A4 Steps 1C, 2, 3, 4, 6A and the deck cross-checks.

### Cells that RECONCILE (representative, all PASS)
| Metric | A4 value | Recomputed | Source |
|---|---|---|---|
| Consol Op EBITDA Q1FY27 (PBT+D+Fin−OI) | (130.657) | −237.680+12.982+118.568−24.527 = −130.657 | ledger_results 881-897 |
| Consol Reported EBITDA Q1FY27 (PBT+D+Fin) | (106.130) | −237.680+12.982+118.568 = −106.130 (=deck "EBIDTA (106)" L702) | ledger 881-897 / presn 702 |
| Standalone Op EBITDA Q1FY27 | (73.466) | −89.571+7.849+22.427−14.171 = −73.466 | ledger 419-433 |
| Consol Op EBITDA margin Q1FY27 | (60.3%) | −130.657/216.754 = −60.28% | — |
| Consol Core PBT ex-OI Q1FY27 | (262.207) | −237.680−24.527 = −262.207 | — |
| Revenue YoY | −68.2% | (216.754−680.919)/680.919 = −68.16% | ledger 881 |
| Finance cost YoY | −26.1% | (118.568−160.421)/160.421 = −26.09% | ledger 887 |
| Reported PBT YoY (loss widened) | +44.3% | (237.680−164.758)/164.758 = 44.26% | ledger 891/893 |
| PAT-after-JV YoY (loss widened) | +41.5% | (234.402−165.644)/165.644 = 41.51% | ledger 902 |
| Consol loss narrowed QoQ | 27.5% | (323.432−234.402)/323.432 = 27.53% | ledger 902 |
| Presales floor gap | ₹5,132 Cr / ₹1,711 q avg | 6,000−868 = 5,132; /3 = 1,710.7 | presn 247/437 |
| Presales delivered vs floor | ~14.5% | 868/6,000 = 14.47% | presn 247/437 |
| Presales QoQ / area QoQ | −67% / −73% | 868/2,632−1 = −67.0%; 484/1,783−1 = −72.9% | presn Table 4 |
| Presales YoY | +338% | 868/198−1 = +338.4% | presn Table 4 |
| S-vs-C loss ratio | ~2.6x | 234.402/90.288 = 2.60x | ledger 442/902 |
| Other-auditor revenue share | 75.9% | 1,645.39/2,167.54 = 75.9% | ledger para 5a / 881 |
| Other-auditor loss share | 26.8% | 627.36/2,344.02 = 26.8% | ledger para 5a / 902 |
| Net debt QoQ | −₹719 Cr | 4,082−3,363 = 719 | presn 266 / [memory] |
| Warrant value | ₹362.62 Cr | 3,25,18,900 × 111.51 = ₹362,61,82,539 | ledger A-3 |
| Spends-to-collections | ~56% | 276/496 = 55.6% | presn 234/254 |

### Cells that FAIL (mismatch above rounding)

**FAIL 2.1 — PAT bridge, Tax-change component (review Step 4, line 184). → loop A4.**
- A4 value: **−2.047**, annotated "from **0.842 credit** to 0.289 charge."
- Source raw: consolidated Q1FY26 tax = current 56.52m + deferred (48.10m) = **8.42m net = ₹0.842 Cr CHARGE** (extract lines 895-897; loss deepens PBT −1,647.58 → LAT −1,656.00). Q1FY27 tax = 2.89m = ₹0.289 Cr charge.
- Recomputed tax delta: charge fell 0.842 → 0.289, i.e. **+₹0.553 Cr favourable to PAT**. Q1FY26 tax is a **charge, not a credit** — the sign label is also wrong.
- Consequence: A4's bridge does not reconcile. Non-tax components sum to −69.311 (−77.098 gross −42.797 opex −6.275 D&A +41.853 finance +11.395 OI +3.611 JV). To reach the stated reported-PAT change of **−68.758** the tax term MUST be **+0.553**. With A4's −2.047 the bridge sums to −71.358, off by ₹2.6 Cr. The error is internally self-evident and above rounding.

**FAIL 2.2 — Ledger-reconciliation preamble, results line-item count (review line 10). → loop A4.**
- A4 value: "**87** financial line items (57 standalone-side rows / 30 consolidated rows per A2 count)."
- Recomputed: **57 total** (standalone 23 + consolidated 30 + Note-10 sub-table 4), which is exactly the A2 count test figure (ledger_results line 12) and my fresh sweep. A4's "87," and its claim that A2 counted "57 standalone," misstate the ledger. Contractual preamble figure is wrong.

(Minor, not scored as a FAIL: A4's parenthetical presentation-unit breakdown at line 12 lists eight sub-categories summing to 298 while quoting the ledger total 334; the ledger 334 legitimately also counts 33 slides + 3 identifiers, so the total is right and no data unit is dropped — imprecise wording only.)

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear from same text)

**Positive claim 1 — "Net institutional debt DOWN ₹719 Cr QoQ to ₹3,363 Cr — the clearest
positive" (review 209, 221, 435).**
Bear counter from the same extract: "net institutional debt" **excludes ₹1,100 Cr of
shareholder debt** (deck footnote, presn Table 7 #5 / line 272) and gross institutional
debt is still ~₹4,500 Cr (presn L263); operating cash flow was **negative ₹285 Cr** (presn
L643), so the QoQ decline is financing/warrant-funded, not cash-generated; the post-quarter
₹1,020 Cr NCD re-levers (Note S7/C6). **Counter SURVIVES but is ALREADY incorporated** — A4
carries shareholder debt ₹1,100 Cr (line 210), negative CFO ₹285 Cr (line 202), gross debt
~₹4,500 Cr (line 208) and the NCD refi. No graft required.

**Positive claim 2 — "Presales ₹868 Cr, +338% YoY" (review 146, 356, Step 1 deck claim 1).**
Bear counter from the same extract: the Q1FY26 base of ₹198 Cr is (a) a quarter management
itself declares "**not comparable**" (presn note 6 / L964) and (b) a seasonal low; sequentially
presales fell **−67%** off Q4's ₹2,632 Cr and the absolute ₹868 Cr sits **below the ₹1,200 Cr
Q1 Red monitor**. **Counter SURVIVES but is ALREADY incorporated** — A4 Step 3, monitor #1,
F16-a/-b and the combined verdict all foreground exactly this. No graft required.

**Positive claim 3 — "NCLAT allowed appeal, Company no longer under CIRP — GREEN" (review
43, 250, 263).**
Bear counter attempt from the same extract: residual corporate-guarantee exposure to STPL
and a possible higher-court appeal. **Counter does NOT survive** — the extract (Note S6/C8)
states the Section 7 petition was dismissed and the company is no longer under CIRP, with no
pending appeal disclosed; the STPL guarantee is noted but not quantified as live. Nothing in
the extract supports re-opening. No graft required.

**Adversarial result:** the strongest surviving bear counters are already symmetrically
present in A4. **No new surviving bear counter must be grafted.** Audit 3 adds no FAIL.

---

## VERDICT

**INCOMPLETE.** Coverage audit (A2 enumeration) and the deliverable-completeness gate both
PASS; the adversarial read surfaces no un-incorporated bear counter. However the ARITHMETIC
audit finds two A4 computation errors above rounding:

1. **FAIL 2.1** — PAT-bridge tax-change cell shows −2.047 ("0.842 credit"); correct value is
   +0.553 favourable and Q1FY26 tax is a ₹0.842 Cr **charge**, not a credit. A4's own bridge
   fails to reconcile to its stated −68.758 PAT change (sums to −71.358).
2. **FAIL 2.2** — Ledger-reconciliation preamble states 87 results line items (57 standalone
   + 30 consolidated "per A2 count"); the A2 count and my fresh sweep are **57 total**.

Both are A4 errors (A2's and A3's counts are correct). **loop_back_to = A4.** Fix the two
figures, re-emit; on correction this review is otherwise save-ready.

```yaml
stage: A5-adversary
company: "EMVDL"
quarter: "Q1 FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches:
  - metric: "PAT bridge — Tax-change component (consolidated, Q1FY27 vs Q1FY26), Step 4"
    a4_value: "-2.047 (labelled 'from 0.842 credit to 0.289 charge')"
    recomputed: "+0.553 favourable; Q1FY26 tax is a CHARGE of 0.842 Cr, not a credit; with -2.047 the bridge sums to -71.358 not the stated -68.758"
    source_line: "review line 184; extract_results lines 895-897; ledger_results line 171"
  - metric: "Results line-item count, ledger-reconciliation preamble"
    a4_value: "87 (57 standalone + 30 consolidated 'per A2 count')"
    recomputed: "57 total (23 standalone + 30 consolidated + 4 Note-10 sub-table), matching A2 count test = 57"
    source_line: "review line 10; ledger_results line 12"
surviving_bear_counters: []
loop_back_to: "A4"
gap: "Two A4 arithmetic errors: (1) Step-4 PAT-bridge tax-change cell = -2.047/'credit' should be +0.553 favourable/charge (bridge does not reconcile to -68.758); (2) preamble results line-item count = 87 should be 57 (A2 count). Correct both and re-emit."
```
