# Stage 13 synthesis, phase 1 lite: SUDARCOLOR, run 2026-11-12

Mode: PHASE 1 LITE. Three final files, no valuation-dependent content. Model claude-opus-5-5. All figures in ₹ Cr unless the source says otherwise.

## What was written

1. outputs/final/business-narrative.md. The BUSINESS UNDERSTANDING NARRATIVE (five questions, prose) comes first. Then the headline "The parent now decides this company's growth" and seven paragraphs: business, transition, Gate 0 and cash, earnings quality, credibility and governance, peers, market opportunity. The valuation paragraph is omitted. No block references.
2. outputs/final/gate-recommendation.md. Verdict line PROCEED WITH CAVEATS. It holds the verdict block with the rule derivation, three flag blocks (FLAG-CASH INDETERMINATE, FLAG-PROMOTER not active, FLAG-GATE0), the confidence delta table, contradicted claims, 8 monitorables, the falsification line, open items (a) to (g) and the publish check.
3. outputs/final/verifier-summary.md. It opens with the confidence delta and acceptance rates. Then 46 findings sorted by severity (0 CRITICAL, 18 MAJOR, 28 MINOR), Verifier B spot checks, the Verifier C recomputes, and the Verifier D coverage table. B12a findings carry no IDs in the block, so this file labels them A-1 to A-11 in block order.

## Verdict derivation

- Rule 1 (REWORK): not fired. No CONFIRMED B12a CRITICAL. A 95, B 69, C 77.8, D 100.
- Rule 2 (INSUFFICIENT EVIDENCE): not fired. Both ARs, three results filings and eleven peer transcripts are present, and Gate 0 ran on screening data and results. The named gaps are partial. The other reading, which treats the H1 FY27 Reg 23 split as decision-defining, is stated in the file.
- Rule 3: FLAG-CASH is active. No stage made a STRUCTURAL / GROWTH-INDUCED / INDETERMINATE call; the search found none in the run. Synthesis made the call from the blocks. The FY26 build came on revenue down 5.4%. The H1 FY27 build came on revenue up 25.0%. The group share of balances is NOT FOUND, and no rating exists. Result: INDETERMINATE, which caps the verdict at PROCEED WITH CAVEATS.
- Rule 4: confidence 69 (band 60-74) concurs. No second downgrade.

## Source fidelity gate

Every B12a source_fidelity finding is carried at its source_truth value: H1 FY27 PBT 59.67, peer EBITDA median 8.17%, peer gross margin median 39.00%, FY17 EBITDA margin 6.84%, OCF excluding government balances 13.71 (government balances 20.53; 24.76 described as a three-line sum), institutional holding 0.71%. Verifier B items B-09, B-12, B-14 and B-15 are not repeated as claims. No downstream conclusion conflicted with a Verifier A finding, so the disagreement set is empty. The disagreement log file was not written, because the phase 1 lite scope is exactly three final files.

## Not produced (scope)

fttcp-handoff.md, verifier-disagreement-log.md, notion-payload.md and the downstream tracker payload. No valuation, entry zone, destination PE or Hurdle verdict.

## Inputs read

manifest.yaml, confidence.yaml, B00 to B09, B12a to B12d, companies/SUDARCOLOR.md, step1-business-brief.md (memory, not evidence), 04-bizmodel.md (Section 1-2), 07-emoat.md (Sections 3-5), 12c-verifier-framework.md (operator questions, propagation), 12d-verifier-peers.md.

```yaml
stage: B13-synthesis-lite
company: "SUDARCOLOR"
run_date: "2026-11-12"
model: "claude-opus-5-5"
status: complete
verdict: "PROCEED WITH CAVEATS"
verdict_rule_applied: 3
flags_active: ["FLAG-CASH (INDETERMINATE)", "FLAG-GATE0 (AVERAGE, DB3; class convention-dependent)"]
confidence_delta: {numerical: 95, redflag: 69, framework: 77.8, peer: 81.8, overall: 69}
headline: "The parent now decides this company's growth"
block_path: "outputs/blocks/B13-synthesis-lite.yaml"
```
