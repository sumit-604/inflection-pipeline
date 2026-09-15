# VERIFIER DISAGREEMENT LOG — ORCHPHARMA 2026-09-06 (phase 1)

Every point where a downstream step's conclusion conflicts with a Verifier A
source-fidelity finding. Not a REWORK trigger. Standing evidence on whether the
out-of-family numerical check catches what the others miss, or produces noise.

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-06 | orchpharma-2026-09-06 | Q4 FY26 EBITDA, Rs 42.3 cr, claimed in 05-concall.md | MISMATCH, source_fidelity true. Verifier A read the source as "approximately INR23 crores" at Concall_Jun_2026_Transcript.pdf p.2-3 and called the report figure a 2x error requiring correction before stage 11 | Orchestrator re-read the source. The transcript reads "Our EBITDA for Q4 stood at approximately INR42.3 crores compared to approximately INR40 crores in Q4 of '25" at Concall_Jun_2026_Transcript.pdf p.3, confirmed in the clean embedded text layer and by an independent extraction. Stage 5's figure is correct and correctly anchored | FLAG CLEARED — source re-check found the number at a correct anchor (re-checked by the orchestrator session, 2026-09-06) | Verifier A misquoted the source. The surrounding sentence also carries Q4 FY25 EBITDA about Rs 40 cr, FY26 revenue Rs 811 cr against Rs 922 cr, and FY26 EBITDA Rs 101 cr against Rs 155 cr, all consistent with stage 5. This is the LESSONS-catalogued Verifier A failure mode: a false finding on a figure that matches its source |

## TWO FURTHER VERIFIER A SEVERITY MISLABELS THIS RUN, not disagreements

Neither is a disagreement, because neither is a source-fidelity finding. Both are
recorded because they inflate the MAJOR count and would distort the confidence
delta if read at face value.

1. 09-tam.md Method 3, Covalent revenue and the unorganised-sector multiplier.
   Verifier A labelled it MAJOR and then wrote in its own note that it "is not a
   MISMATCH, it is a confidence limitation transparently disclosed by the report".
   A stage that flags its own low confidence, names the blocked source and states
   the limit of its method has followed the rules. Not a finding.

2. 06-peers.md peer financial screening. Verifier A labelled it MAJOR and then
   wrote in its own note "CORPUS LIMITATION, NOT REPORT ERROR" and called the
   stage's workaround appropriate. The peer screener exports are empty templates,
   which stage 0 recorded and every stage was told. Not a finding.

CORRECTED VERIFIER A COUNTS FOR THIS RUN: 0 CRITICAL, 0 MAJOR surviving scrutiny,
6 MINOR. The stated acceptance rate of 95.2% is therefore a floor, not a ceiling.
The confidence delta uses the stated figure and this note records why the true
numerical fidelity is higher.

## WHAT VERIFIER A DID WELL THIS RUN

Run 2 verified clean, against source, every figure in the run's most load-bearing
findings: the Rs 447.22 cr corporate guarantee, the Rs 230.72 cr GCLE purchase from
Otsuka, the Rs 108.24 cr loan to Orchid Bio-Pharma, the working capital movements
(receivables +27.7%, inventory +41.0%, revenue +12.5%), and the consolidation-scope
correction itself, confirmed across three transcripts. It also reported its own
coverage honestly at 10.1% after run 1 overstated it at 80%, and gave per-report
acceptance rather than one average that would hide a weak report.
