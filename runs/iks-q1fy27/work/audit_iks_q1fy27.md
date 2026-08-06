# A5 ADVERSARY — COMPLETENESS AUDIT (RE-AUDIT, loop 2) — IKS Q1 FY27

Fresh-context adversarial audit of A4's corrected review. Inputs: corrected A4 review,
A1 extracts (results, press release, directors, presentation), A2 ledgers (results,
presentation). Independence: every figure below re-derived from the raw INR-Million
extract (÷10 to Rs Cr), not taken from A4's or A3's cites.

Two prior-loop gaps under specific re-verification:
- GAP-1: missed YoY ROE-decline cluster (deck slide 12 title "maintaining high ROE" vs
  32.3%→26.4% chart; Abridge FVOCI revaluation driver; filing L377).
- GAP-2: Step 4A arithmetic error (operating-cost-growth intermediate +82.85
  contradicting −96.51 impact).

---

## AUDIT 0 — DELIVERABLE-COMPLETENESS (hard gate)

Plain-Language Brief, Section E (review L409–439). All four labelled parts present and
carry real, non-placeholder content:

| Part | Location | Present | Content check |
|---|---|---|---|
| (1) Summary narrative | L411–417 | present | Two substantive paragraphs; numbers anchored; now carries the ROE sentences (L415) |
| (2) SECTOR intelligence | L419–423 | present | TAM, USD/INR exposure, agentic-AI thesis, provenance-labelled |
| (3) BUSINESS-MODEL intelligence | L425–431 | present | Segment, margin structure, model-drift (acquisition-led, concentration, ROE tie-in) |
| (4) COMPETITION intelligence | L433–439 | present | Named peers (GENERAL KNOWLEDGE-labelled), concentration/AI-threat bear points |

Gate: PASS.

---

## GAP-1 RE-VERIFICATION — ROE / Abridge cluster (was: return to A3, then graft by A4)

A3 produced forensic F-13; A4 grafted it. I independently confirm the primary text and
that every required surface now carries it:

- Deck slide 12 title verbatim: "Q1 FY 27 - Improving EPS and maintaining high ROE"
  (extract_presentation L415). Confirmed.
- ROE chart values: 32.3% (L420), 31.3% (L421), 26.4% (L423). Decline = 590bps YoY /
  490bps QoQ. Matches A4's "~590bps YoY / ~490bps QoQ" (review L345, L373, L415). Confirmed.
- Footnote driver verbatim: "*ROE declined due to increased equity base from revaluation
  of Abridge, alongside lower earnings from reduced currency gains and one-time acquisition
  costs." (L443). Confirmed.
- Abridge FVOCI quantum: filing L377 consolidated Q1 FY27 = 226.42 Mn gross; L378 tax
  (56.86); L379 net = 178.47 Mn. A4 states "Rs 226.42 Mn gross / 178.47 Mn net,
  L377–379". Confirmed exact.

Graft completeness across the review:
- Question Q16 (Step 8.5, review L345) — present, with denominator-vs-numerator split and
  bull/bear.
- Caution flag in Combined Verdict (Section C, L373) — present.
- Monitorable #13 (Section D, L405) — present.
- Brief sentences (Section E narrative, L415) — present.
- YAML: flag (L506), monitorable (L497), question row (L483), F-13 in
  a3_findings_incorporated (L457) — all present.

The "~80bps from the Abridge mark, ~500bps earnings-driven" claim is an estimate framed as
a management question (Q16) and directionally internally consistent (590 − 80 ≈ 510 ≈
~500). It is not a hard arithmetic assertion and does not fail. GAP-1: CLOSED.

---

## GAP-2 RE-VERIFICATION — Step 4A PAT bridge arithmetic (was: return to A4)

Erroneous prior figures (+82.85 / −96.51) fully purged (grep of review returns zero hits;
only +96.35 remains, review L215 and L225). Re-derived from raw extract (Rs Cr, ÷10):

- Operating-cost growth components: employee 455.01 − 395.96 = +59.05; other-exp
  143.84 − 106.38 = +37.46; inventory-change (−0.16) − 0 = −0.16.
  Sum = 59.05 + 37.46 − 0.16 = **+96.35** (expense increase). Matches A4.
- Cross-check via totals: Total expenses 643.09 − 548.33 = +94.76; remove D&A (+6.39) and
  finance (−7.97): 94.76 − 6.39 + 7.97 = 96.34 ≈ +96.35 (rounding). Consistent.
- Net Operating EBITDA change: revenue +153.53 − 96.35 = +57.18 ≈ **+57.19**.
  Independent direct check: OpEBITDA Q1FY27 = 256.25+34.29+10.11−5.71 = 294.94;
  Q1FY26 = 194.88+27.90+18.08−3.11 = 237.75; Δ = +57.19. Matches.
- Full bridge to PAT: +57.19 − 6.39 (D&A) + 7.97 (finance) + 2.60 (OI) − 5.31 (assoc)
  − 13.86 (tax) = +42.20 = reported PAT change (193.74 − 151.54). Reconciles exactly.

GAP-2: CLOSED. The intermediate no longer contradicts the impact; both are +96.35 and the
bridge closes to the reported PAT delta.

---

## AUDIT 1 — COVERAGE (fresh enumeration vs A2 ledgers)

Fresh pass over the extracts; counts diffed against both ledgers; every ledger row checked
for citation-or-"reviewed,no-finding" in A4.

| Category | A2 count | My fresh count | Orphan rows | Status |
|---|---|---|---|---|
| Results: notes | 10 | 10 (L406,410,413,415,418,422,424,427,438,446) | 0 | PASS |
| Results: line items | 37 | 37 (statement L318–393, incl. OCI block) | 0 | PASS |
| Results: zero-standing | 4 | 4 (#6 inventory, #13 assoc, #23 FX-translation, #28 FVOCI) | 0 | PASS |
| Results: agenda items | 3 | 3 (results approval; Desai retire; King succeed) | 0 | PASS |
| Results: auditor paras | 11 | 11 (4 s/a + 7 consol) | 0 | PASS |
| Results: entities | 11 | 11 (10 subs + WWMG associate) | 0 | PASS |
| Results: annexures / rows | 4 / 10 | 4 / 10 | 0 | PASS |
| Results: signature blocks | 5 | 5 | 0 | PASS |
| Pres: slides | 18 | 18 | 0 | PASS |
| Pres: financials-summary rows | 24 | 24 (deck L449–472) | 0 | PASS |
| Pres: other-KPI rows | 8 | 8 (deck slide 14) | 0 | PASS |
| Pres: footnotes | 11 | 11 | 0 | PASS |
| Pres: per-slide units | 161 | reconciled (no residual) | 0 | PASS |

Material-row citation trace: FVOCI/Abridge → F-13/Q16 (the previously-orphaned row, now
cited); associate reclass → F-05/F-07/Q11; inventory → bridge; TruBridge license → F-02/Q2;
Adjusted-PAT footnote → Q13; OCF/FCF add-back footnote → F16c/Q1; ROE/EPS footnotes →
F-13/F10/Q16/Q14; acquisition-expense footnote → F16f/Q3; Top-10/Top-5 inconsistency →
F14/Q10; CAGR framing → F16d/Q15; concentration → F16a/F16b/Q9. Non-material rows (awards
slides, thank-you, cover letter, OCI cash-flow-hedge/remeasurement lines that do not touch
PAT, administrative signature blocks) are covered by the blanket "All reviewed" preamble
(review L15–21) — acceptable as "reviewed, no finding".

No orphan rows. No row found by my fresh pass that the ledger lacks.

---

## AUDIT 2 — ARITHMETIC (recomputed from raw INR Mn, ÷10)

| Metric | A4 value | Recomputed | Source line | Status |
|---|---|---|---|---|
| Consol revenue YoY | +20.7% | 8936.29/7400.95−1 = 20.7% | L319 | PASS |
| Consol OpEBITDA Q1FY27 | 294.94 | 256.25+34.29+10.11−5.71 = 294.94 | L331/327/326/320 | PASS |
| Consol OpEBITDA margin Q1FY27 | 33.0% | 294.94/893.63 = 33.0% | derived | PASS |
| Consol OpEBITDA margin Q1FY26 | 32.1% | 237.75/740.10 = 32.1% | derived | PASS |
| Consol core PBT ex-OI YoY | +27.9% | 245.23/191.77−1 = 27.9% | derived | PASS |
| Consol PAT | 193.74 | 1937.41/10 | L345 | PASS |
| Consol PAT YoY | +27.8% | 193.74/151.54−1 = 27.8% | L345 | PASS |
| ETR Q1FY27 | 22.8% | 57.20/250.94 = 22.8% | L343/338 | PASS |
| ETR Q4FY26 | 18.6% | 46.99/252.96 = 18.6% | L343/338 | PASS |
| QoQ PAT | −5.9% | 193.74/205.97−1 = −5.9% | L345 | PASS |
| QoQ OpEBITDA margin | −2.0pp | 35.0%→33.0% | derived | PASS |
| Step 4A operating-cost growth | +96.35 | 59.05+37.46−0.16 = 96.35 | L325/328/324 | PASS |
| Step 4A net OpEBITDA change | +57.19 | 153.53−96.35 = 57.18 ≈ 57.19 | derived | PASS |
| Full PAT bridge | +42.20 | 57.19−6.39+7.97+2.60−5.31−13.86 = 42.20 | derived | PASS |
| Standalone revenue YoY | +48.8% | 475.27/319.47−1 = 48.8% | L319 | PASS |
| Standalone other-exp QoQ | +117.0% | 57.36/26.43−1 = 117.0% | L328 | PASS |
| Standalone PAT YoY | +44.0% | 162.55/112.88−1 = 44.0% | L345 | PASS |
| Consol premium over s/a Q1FY26 | 34.3% | 38.66/112.88 = 34.3% | L345 | PASS |
| Consol premium over s/a Q1FY27 | 19.2% | 31.19/162.55 = 19.2% | L345 | PASS |
| Deck EBITDA tie | 294.94 = deck 2,949 | L457 | PASS |
| ROE decline YoY | ~590bps | 32.3%−26.4% = 5.9pp | deck L420/423 | PASS |
| Abridge FVOCI net | 178.47 Mn | L379 net of L377 gross 226.42 / L378 tax | L377–379 | PASS |

No mismatch above rounding. Corrected Step 4A bridge reconciles cleanly.

---

## AUDIT 3 — ADVERSARIAL READ (three most-positive claims, strongest bear from same text)

1. Claim: "Growth is core-operating, not treasury" (core PBT ex-OI +27.9%; OI only 2.3% of
   PBT; review L169). Strongest bear from the extract: consolidated +20.7% INR is only +12%
   USD (deck L449) — ~8–9pp is rupee depreciation, not organic; and standalone +48.8% is
   inflated by the non-repeatable TruBridge license sale that eliminates from Q2 (Note 9,
   L442). Survives? Yes — but ALREADY grafted: review Step 2A (L159, L167), F-02, Q2 and the
   Combined-Verdict caution block already carry both points. No new graft required.

2. Claim: "De-levering — net debt −40.8% YoY to Rs 265.4 Cr, finance costs −44%" (review
   L148, L270). Strongest bear: figure is pre-TruBridge; the US$557 Mn EV (Note 9, L438)
   closed 9-Jul-2026 with undisclosed funding (F-10) and will step up net debt / finance
   cost from Q2. Survives? Yes — ALREADY grafted: Step 2 diagnostic 5 (L171), Step 5 (L278),
   Q7, Monitorable 9. No new graft required.

3. Claim: "Clean audit, high margins" (UNMODIFIED, no GC/EoM; 33% consol / ~46% s/a).
   Strongest bear: 5 subsidiaries + 1 associate are UNREVIEWED (~5.8% of PAT, L275–286), and
   headline "Adjusted PAT 2,153" is a non-GAAP figure not reconciled on the filing face
   (deck L471). Survives? Yes — ALREADY grafted: F-04 (Step 0D), Q13, and the Combined-Verdict
   caution block. No new graft required.

All three strongest bear counters are already present in the corrected review. No surviving
counter is absent and requiring a return to A4.

---

## NEW-INCONSISTENCY CHECK (edits introduced this loop)

The F-13 graft is internally consistent across every surface (narrative L415, verdict L373,
monitorable L405, Q16 L345, YAML L483/L497/L506). No figure introduced by the edit
contradicts another (590bps decline, ~80bps Abridge, ~500bps earnings — all reconcile).
The Step 4A correction is consistent in both the bridge table and the reconciliation prose
(+96.35 in both; closes to +42.20 reported PAT delta). No new inconsistency introduced.

---

## VERDICT

COMPLETE. Both prior-loop gaps are genuinely closed (GAP-1 ROE/Abridge cluster fully
grafted and correctly sourced; GAP-2 Step 4A bridge corrected to +96.35 and reconciling).
Coverage: no orphan rows, no rows missing from ledger. Arithmetic: every recomputed metric
matches within rounding. Adversarial: the three strongest bear counters are already
incorporated; none survives absent. Deliverable gate: all four brief parts present.
Proceeds to Notion save.

```yaml
stage: A5-adversary
company: "IKS"
quarter: "q1fy27"
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
