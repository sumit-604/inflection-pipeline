# A5 ADVERSARY / COMPLETENESS AUDIT — SAMMAANCAP Q1FY27

Auditor: A5 (adversary). Model: claude-opus-4-8. Fresh context: only the A4 review, the A1
extracts, and the A2 ledgers were read. A3's reasoning was NOT consulted; every cite below was
re-derived from the raw extracts and ledgers. Verdict at foot: **COMPLETE**.

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate, run first)

The PLAIN-LANGUAGE BRIEF is present (review L602-626) with all four labelled parts non-empty:

| Part | Heading | Location | Present / Empty | Content check |
|---|---|---|---|---|
| 1 | SUMMARY NARRATIVE | L604-606 | **present** | Substantive; ~15+ sentences covering PAT non-core nature, negative NII, HTS pool, covenant breach, capital, warrants, tax shield, signature anomaly, guidance, flag-not-decide. Real content, not placeholder. |
| 2 | SECTOR INTELLIGENCE | L608-613 | **present** | Sub-sector, demand read, regulation, funding mix, name-specific headwind; provenance labelled this-quarter/un-benchmarked. |
| 3 | BUSINESS-MODEL INTELLIGENCE | L615-620 | **present** | Revenue mechanics, spread-engine failure, unit-economics drift, capital/leverage, undisclosed-metric gap. |
| 4 | COMPETITION INTELLIGENCE | L622-626 | **present** | Structural wins (IHC parent, rating uplift), structural weaknesses (negative spread, HTS pool, covenant breach), competitive risk, candidate peer set. |

Note (non-failing): Part 1 is rendered as a single prose block rather than 10-20 discrete lines,
but the content is clearly present and exceeds the substance bar. Gate = **PASS**.

---

## AUDIT 1 — COVERAGE (fresh independent enumeration vs A2 ledger)

Fresh grep passes were run over both extracts and diffed against the ledgers.

| Category | A2 count | My fresh count | Method | Orphan rows | Status |
|---|---|---|---|---|---|
| Presentation: pages | 4 | 4 | `grep -c "\[page N\]"` = 4 (L1,39,87,131) | none | PASS |
| Presentation: highlight bullets | 16 | 16 | `grep -c "•"` = 16 (11 pg2 + 5 pg3) | none | PASS |
| Presentation: A3-01..A3-14 findings | 14 | 14 | all 14 ids mapped to Qs 13-26 (review L374-389) | none | PASS |
| Results: auditor signatures (UDIN) | 5 auditor of 10 blocks | 5 | UDIN grep L319 (x2 consol), L623 (x2 SA), L1478 (x1 SCC) | none | PASS |
| Results: signature blocks | 10 | 10 | 5 auditor + Banga + Jain x3 + Chaudhary | none | PASS |
| Results: agenda items | 4 | 4 | results/Khorshid/Mundra-Mohapatra/LIC-Negi | none | PASS |
| Results: consolidation entities | 10 | 10 | matches Other Matters (9 subs + 1 trust) | none | PASS |
| Results: notes | 42 | 42 | consol 1-19 (19) + standalone 1-23 (23) | none | PASS |
| Results: line items / footnotes / annexures / auditor paras | 194 / 11 / 3 / 26 | consistent | structural cross-check; key raw values verified below | none | PASS |

**Every ledger flag traced to A4 treatment (no orphan rows):**
- COVENANT_BREACH (SCC para 13, L1409/1411) -> F5-a, Step 5L covenant subsection, Q1, flag list. Cited.
- SIGNATURE_BEFORE_BOARD_CONCLUSION (6 sigs) -> F14-a, Step 0 procedural flag, Q11, flag list. Cited.
- OCR_UNCERTAIN (pp.39-42) -> Step 5L OCR caveat (L288), derived-metrics table marks Loans 37,021.94 uncertain. Cited.
- ANNEXURE_REFERENCED_NOT_FOUND (Annexure I) -> Q12 (F14-b), flag list. Cited.
- CROSS_CHECK_NEEDED (a) default-format vs breach -> Step 5L (breach != default, L286). Cited.
- CROSS_CHECK_NEEDED (b) SCC Note-4 scope vs para 13 -> review L285 (debenture-scoped). Cited.
- CROSS_CHECK_NEEDED (c) SA N15 NCD no consol mirror -> note table (N15, CROSS_CHECK flag), monitorable 6. Cited.
- TEMPLATE_ARTIFACT (Form-1 Yes/No) -> Q12 (F14-b). Cited.
- ENTITY_CHANGE (not assignable) -> entity #5 rebrand asked in Q12. Cited.
- Methodology delta 1,154.93 vs 996.25 -> note table ("scope difference; not a drafting error"). Cited.
- REPEAT_METRIC disbursements Rs.3,875cr -> A3-14, Q26. Cited.
- ZERO_STANDING project-finance template silence -> SA N21 folded into Step 5L asset-quality block. Reviewed.

**Rows my fresh pass found that the ledger lacks:** none. My raw-figure grep (interest income,
finance costs, fair value, PBT, PAT — consol and standalone) returned exactly the values the ledger
transcribed (L367/369/377/385/387/406 and L640/642/650/658/660/678). No enumerated unit missing.

Coverage = **PASS**. No loop-back to A2 or A3.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw extract numbers, not A4's cites)

| Metric | A4 value | My recompute | Source lines | Status |
|---|---|---|---|---|
| NII consol Q1FY27 | (257.09) | 1,078.17 − 1,335.26 = (257.09) | L367,L377 | PASS |
| NII consol Q1FY26 | +367.52 | 1,563.64 − 1,196.12 = 367.52 | L367,L377 | PASS |
| NII standalone Q1FY27 | (197.82) | 1,039.36 − 1,237.18 = (197.82) | L640,L650 | PASS |
| NII standalone Q1FY26 | +363.81 | 1,495.90 − 1,132.09 = 363.81 | L640,L650 | PASS |
| PPOP consol Q1FY27 | 85.54 | 1,682.81 − 1,335.26 − 262.01 = 85.54 (opex 176.61+20.11+65.29) | L375,L377,L381-383 | PASS |
| PPOP consol Q1FY26 | 934.09 | 2,409.43 − 1,196.12 − 279.22 = 934.09 | L375,L377,L381-383 | PASS |
| PPOP standalone Q1FY27 | 63.18 | 1,519.12 − 1,237.18 − 218.76 = 63.18 | L648,L650,L654-656 | PASS |
| PPOP standalone Q1FY26 | 826.90 | 2,200.20 − 1,132.09 − 241.21 = 826.90 | L648,L650,L654-656 | PASS |
| Interest income YoY consol | −31.05% | −485.47/1,563.64 = −31.05% | L367 | PASS |
| Total rev YoY consol | −31.18% | −748.40/2,400.33 = −31.18% | L373 | PASS |
| Finance cost YoY consol | +11.63% | 139.14/1,196.12 = +11.63% | L377 | PASS |
| PPOP YoY consol | −90.84% | −848.55/934.09 = −90.84% | derived | PASS |
| PBT YoY consol | −30.36% | −142.10/468.11 = −30.36% | L387 | PASS |
| PAT YoY consol | −27.22% | −91.00/334.30 = −27.22% | L406 | PASS |
| EPS basic YoY consol | −48.05% | −1.97/4.10 = −48.05% | L436 | PASS |
| Fair-value YoY consol | +1,067.4% | 448.93/42.05 = +1,067.6% | L369 | PASS (0.2pp, rounding-level on a 1,068% figure; immaterial) |
| Fair-value YoY standalone | +2,765.5% | 383.30/13.86 = +2,765.5% | L642 | PASS |
| PPOP ex-FV consol Q1FY27 | (405.44) | 85.54 − 490.98 = (405.44) | L369 | PASS |
| Cost-to-income consol Q1FY27 | 75.4% | 262.01/347.55 = 75.39% | derived | PASS |
| Cost-to-income standalone Q1FY27 | 77.6% | 218.76/281.94 = 77.59% | derived | PASS |
| Credit cost annualised consol | (1.71)% | (240.47×4)/56,239 = −1.71% | L378, PR L51 | PASS |
| Consol ETR Q1FY27 | 25.37% | 82.71/326.01 = 25.37% | L404,L387 | PASS |
| Standalone ETR Q1FY27 | 23.59% | 69.63/295.23 = 23.58-23.59% | L677,L660 | PASS |
| PAT bridge: NII leg | −624.61 | (257.09) − 367.52 = −624.61 | derived | PASS |
| PAT bridge: derecognition leg | −708.39 | 24.01 − 732.40 = −708.39 | L370 | PASS |
| PAT bridge: provision swing | +706.45 | 465.98 − (−240.47) = +706.45 | L378 | PASS |
| PAT bridge: PPOP change | −848.55 | 85.54 − 934.09 = −848.55 | derived | PASS |
| PAT bridge closes to PBT | −142.10 | −848.55 + 706.45 = −142.10 | derived | PASS |
| S-vs-C PAT gap Q1FY27 (=sub+trust PAT) | 17.70 (7.85% of SA) | 243.30 − 225.60 = 17.70; 17.70/225.60 = 7.85% | L406,L678 | PASS (ties to Other Matters PAT 17.70) |
| S-vs-C PAT gap Q1FY26 | 36.86 (12.39%) | 334.30 − 297.44 = 36.86; /297.44 = 12.39% | L406,L678 | PASS |
| S-vs-C paid-up gap | 3.17 | 232.51 − 229.34 = 3.17 | L418-420,L704-706 | PASS |

No arithmetic mismatch above rounding. The single sub-rounding item (fair-value YoY consol,
1,067.4% vs my 1,067.6%) is a 0.2-percentage-point rounding artefact on a four-digit percentage and
is immaterial to any conclusion. Arithmetic = **PASS**. No loop-back to A4.

**OCR-dependence discipline (per task mandate):** every A4 finding that rests on an unconfirmed OCR
matrix figure carries the caveat. Standalone Loans Rs.37,021.94cr is tagged OCR-UNCERTAIN in the
derived table (L140) and again at L530. Cover ratios 1.21/1.62/1.18 are cited only inside the
explicit "must be confirmed against the source PDF" caveat (L288), and the addendum (L1767-1770)
confirms those very figures (200dpi had rendered 41.21/4.62/4.18). The debt-securities columns
(44,031.17 / 14,031.1x) appear only within that caveat sentence. A4 computes no metric off an
uncaveated OCR figure. Rs.908cr ECB revaluation and Rs.355cr HQLA are drawn from cleanly-readable
verbatim notes (addendum notes 5, 7), not the fragile matrix. Discipline satisfied.

**Verdict-logic check:** protocol_verdict = "PROCEED WITH CAVEATS" with cash_conversion =
"INDETERMINATE" (YAML L643-644; narrative L570). The INDETERMINATE cash conversion does NOT
silently resolve to PROCEED — it is explicitly capped at PROCEED WITH CAVEATS with the missing
evidence named (Q2 cash-flow statement, PCR, collection efficiency). The lender asset-quality
analogue is handled the same way: Elite band declined, band = INDETERMINATE (Step 5L, Step 7).
House rule honoured.

---

## AUDIT 3 — ADVERSARIAL READ (three most positive claims; strongest bear counter each)

| # | A4's positive claim | Strongest bear counter from the SAME extract | Survives? |
|---|---|---|---|
| 1 | Capital strong — CRAR 20.06%, Rs.4,587cr IHC infusion, four-agency upgrade to AA+/BB- (review L560, L624) | Covenant already breached on non-debenture borrowings (L1411) shows leverage constraints already binding; warrants only 25% subscribed (Rs.301.95cr+Rs.763.80cr of the Rs.4,262cr value) so much of the "infusion" is a future dilution overhang; capital sits above a Rs.14,953cr HTS/FVTPL pool whose resolution haircut could erode net worth. | NO — already fully incorporated (F5-a covenant, F10-a warrant overhang, N8 HTS-pool capital risk, INDETERMINATE band). |
| 2 | AUM grew 5.79% QoQ to Rs.56,239cr; disbursals Rs.3,875cr (review L490, L610) | Growth is a single QoQ point off a cleanup trough; interest income fell ~31% YoY so the earning book shrank materially YoY; YoY AUM is ND (not computable); the AUM figure is press-release-only and unverifiable from the filing. | NO — already incorporated (Step 5L AUM-YoY ND; Step 7A "UNVERIFIABLE from filing"; "early-cycle" framing). |
| 3 | Reported consol PAT Rs.243.30cr, back in the black (review L560, L606) | Profit is non-core: NII negative Rs.257.09cr, PPOP ex-fair-value negative Rs.405.44cr; Rs.490.98cr fair-value mark + Rs.240.47cr provision write-back carry the entire result; strip both and the quarter is a loss. | NO — this IS A4's central thesis (Step 2 diag 6, Step 4 bridge, Combined Verdict). |

Supplementary probe — the rating-upgrade positive (A4 treats BB-/AA+ as a clean tailwind, L519/543):
the strongest bear angle (S&P BB- remains sub-investment-grade) relies on external knowledge of
rating scales, NOT on anything in the extracted text, so it does not qualify under the "from the
same extracted text" rule and is not grafted. Recorded for completeness only.

No bear counter survives that is absent from A4. The review is already adversarially self-aware
(it leads with the negative-NII / non-core-PAT finding). **Nothing to graft.** No loop-back to A4.

---

## VERDICT

**COMPLETE.** All four deliverable-brief parts present and substantive; fresh enumeration matches
the A2 ledgers with zero orphan rows and zero rows missing from the ledger; every derived metric
recomputes to A4's value within rounding; every OCR-dependent finding is caveated; the
INDETERMINATE cash-conversion and INDETERMINATE asset-quality band are correctly capped at PROCEED
WITH CAVEATS with missing evidence named; and no bear counter survives outside what A4 already
incorporated. This review proceeds to Notion save.

```yaml
stage: A5-adversary
company: "SAMMAANCAP"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: COMPLETE
plain_language_brief:
  narrative: present
  sector: present
  business_model: present
  competition: present
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters: []
loop_back_to: ""
gap: ""
```
