# Venus Remedies (VENUSREM) — Verifier Summary (Phase 1)

_Phase 1 verifiers only: A (numerical), B (red-flag coverage), D (peer utilisation), and the Gate 0 + Emerging Moat portion of C (framework). Verifier C's valuation-adherence half (B10/B11) is deferred to Phase 3. Findings sorted CRITICAL, then MAJOR, then MINOR._

## Phase 1 confidence delta

| Component | Score | Acceptance basis |
|---|---|---|
| Numerical acceptance (Verifier A / B12a) | 96 | 24 numbers, 0 CRITICAL/MAJOR, 1 MINOR; source-fidelity gate CLEAR |
| Red-flag coverage (Verifier B / B12b) | 89 | pipeline-reconciled; raw B05-scoped acceptance 44% |
| Framework adherence (Verifier C / B12c) | 99 | Gate 0 (45 rules, 0 fails) + Emerging Moat (30 rules, 1 fail) |
| Peer utilisation (Verifier D / B12d) | 78 | 18/23 substantive as classified; audit warrants 83% |
| **Overall** | **78** | Normal band (75-89). REWORK gate NOT triggered. |

**Verifier B reconciliation.** Verifier B's raw 44% acceptance is B05-scoped. Verifier independence gave B12b only the B05 (NO-CONCALL concall/guidance) stage and B06 (peers) to audit. B05 does not own note-level RPT, contingent-liability, or governance forensics. All four B05-missed flags are caught upstream: related-party IP sourcing by B02/B03/B08; the GST contingent liability by B02/B03; MD-equals-CFO and family board by B03/B08; the 36-object MOA expansion and about 8% AGM dissent by B03/B08. Pipeline-wide red-flag coverage is about 89%, the figure used in the confidence delta. The one genuinely incremental Verifier B item (Q4 earnings-quality point) is carried to monitorables. REWORK not warranted: the flags are present in committed blocks; the 44% reflects the NO-CONCALL scope of B05, not a pipeline failure.

---

## Findings (sorted by severity)

### CRITICAL
None across all four verifiers.

### MAJOR

| Verifier | Location anchor | Finding |
|---|---|---|
| B (B12b) | AR Note 36/RPT, p.112 lines 17906-17928 | Related-party sourcing of the IP/technology pipeline (Rs 30 Cr Patent IPR + Rs 21.55 Cr in-licensing advance from KMP-influence entities, plus FY26 IT Rs 4.36 Cr and brand Rs 1.26 Cr) not surfaced in B05; the growth thesis rests on this IP. MISSED by B05, CAUGHT upstream by B02/B03/B08. |
| B (B12b) | AR Note 44, p.114 lines 18512-18514 | Rising GST disputed contingent liability, Rs 8.28 Cr to Rs 19.26 Cr, pending in appeal; no contingent liability mentioned in B05. MISSED by B05, CAUGHT upstream by B02/B03. |
| B (B12b) | AR p.114 line 18537; lines 2926-2987 | Managing Director is also CFO (Pawan Chaudhary signs as MD & CFO); family-dominated executive board. MISSED by B05, CAUGHT upstream by B03/B08. |
| D (B12d) | B06 Part 3 coverage map | Shilpa Medicare May-2026 call mislabelled CITED-ONLY; should be SUBSTANTIVE. Two claim-relevant statements left unused (RM/input-cost corroboration for the platinum/API cost claim; a Jadcherla USFDA audit-continuity update). Coverage-completeness finding, not source-fidelity. Acceptance 96% > 60%, no REWORK. |

### MINOR

| Verifier | Location anchor | Finding | Disposition |
|---|---|---|---|
| A (B12a) | 01-gate0.md line 24 (Spear fact) | EPS Rs 76.90 claimed vs Rs 76.89 audited (consolidated FY26); 0.013% rounding variance. source_fidelity: true. | GATE HELD — figure corrected at source; Rs 76.89 carried forward. |
| B (B12b) | Q1 p.12-15; AGM37 voting results lines 1673-1678 | Broad 36-object MOA/AOA expansion plus about 8% public dissent at AGM on AOA adoption; B05 notes MOA only procedurally. | MISSED scope-creep by B05; caught upstream by B03/B08. |
| B (B12b) | B05 4A trigger #1 / 3C | Margin step-up flagged only as an open question; sharper point is Q4 = 34% of FY revenue at ~22% PBT margin, a possible balancing figure. | PARTIALLY CAUGHT; carried to monitorables (item 4). |
| B (B12b) | B05 3D | Receivables described as falling (earnings-quality positive); consolidated fell but standalone rose Rs 99.26 to 116.39 Cr, partly an elimination artefact. | One-sided in B05; B02 covered both sides. |
| B (B12b) | B05 RF#3 | B05 states only CWIP actuals, no capex number; a Rs 26.76 Cr capital commitment is disclosed in Note 44. | Mildly overstated in B05; B03/B09 have it. |
| C (B12c) | 07-emoat.md L291-301 / B07 L30 | Completionist recount total states 26 but per-category breakdown sums to 27; presentational, guard decision (10 < 12, no inflation) unchanged. | EM 1 fail of 30 rules; framework score 99. |
| C (B12c) | 01-gate0.md L89-96, 109-128 | B2/B3 (and A1/A2/A4) rest on a 2-year window from the Data_Sheet gap; permitted by rule 6 and disclosed. | Confidence caveat only. |
| C (B12c) | 01-gate0.md L72-87 | Basis mix: A1/A2/A4 standalone ROCE vs A3 consolidated ROE; both anchored and explained; formula defs do not mandate one basis. | No framework breach. |
| C (B12c) | 01-gate0.md L208 vs 07-emoat.md L84-87 | M3 FAT uses screener Net Block 231.60 while B07 uses AR net PP&E 110.23; number-reconciliation for Verifier A; M3 score (3) unaffected. | No score impact. |
| D (B12d) | B06 Part 1 Claim 6 | Gland Aug-2026 page-citation drift: Claim 6 cites p.5-6, true anchor p.4. | Citation hygiene. |
| D (B12d) | B06 Part 2A / Part 3 | Caplin Point Aug-2026 "5 to 17 sterile lines" quote cited within p.10-11, true anchor p.9. | Citation hygiene. |

---

## Verifier disagreement log (source-fidelity)

One Verifier A source-fidelity finding this run. Fixed shape below.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-02 | venusrem-2026-09-02 | Consolidated FY26 EPS Rs 76.90 | MINOR MISMATCH; true Rs 76.89 (audited results line 1141/1147); 01-gate0.md line 24 | Spear fact carried Rs 76.90 | GATE HELD — corrected at source; Rs 76.89 carried forward into all downstream use | 0.013% rounding, immaterial; no re-invoke needed |

No other downstream step leaned on a flagged number, and no flag was cleared by re-check this run.
