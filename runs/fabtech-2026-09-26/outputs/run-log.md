# RUN LOG — FABTECH 2026-09-26

- Stage 1: B01 block file arrived wrapped in a markdown fence; orchestrator stripped the fence (content unchanged) so the block parses.
- Stage 1 called the AR receivables figure an OCR misread; stage 2 pass 1 settled it as a genuine drafting error on the AR consolidated balance-sheet face (Rs 24,151.90 lakh face vs Rs 20,433.51 lakh Note 13 / MD&A / audited results). Downstream anchors use Rs 20,433.51 lakh.
- Verifier A run 1: VERIFIER A IDENTITY CHECK. Two CRITICAL rows struck as clerical errors in the finding:
  (1) B01 D2 depreciation: claimed Rs 5.30 Cr; B12a source_truth "Rs 53.02 Cr (530.15 lakh)". 530.15 lakh = Rs 5.30 Cr (results filing FY26 consolidated, inputs/results/20260427-Results_FY26_audited.txt line ~243). Same value; struck.
  (2) B01 D2 finance costs: claimed Rs 4.16 Cr; B12a source_truth "Rs 41.59 Cr (4158.6 lakh)". The filing text reads "41590" = 415.90 lakh = Rs 4.16 Cr (same file, line ~242). Same value; struck.
  Cause: a 10x lakh-to-crore conversion in the verifier. Per LESSONS recurring pattern, Verifier A re-invoked once with the severity-semantics plus coverage addendum. Run-1 files kept as *-run1-superseded.
- Verifier B returned two acceptance readings (67% counting partial catches, 33% full catches only). The orchestrator section 5 rule counts material_caught as reported by B12b (CAUGHT plus PARTIALLY CAUGHT = 14 of 21) = 67%; recorded in confidence.yaml with the 33% alternative stated so the synthesis and operator see both.
