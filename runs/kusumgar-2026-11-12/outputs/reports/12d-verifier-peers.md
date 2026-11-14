# Verifier D: Peer Coverage Audit, KUSUMGAR, 2026-11-12

Scope: 6 transcripts provided (ARVIND 2, MAYURUNIQ 4), GARFIBRES none. Method: spot-read the .txt twins for the load-bearing B06 quotes and for claim-relevant material B06 might have missed.

## Coverage audit per peer

| Peer | Marked | Citations located | Result |
|---|---|---|---|
| ARVIND Jan 2026 | SUBSTANTIVE | AMD margin 15.5% (line 117), 14-15% thumb rule (line 200), defence orders lumpy (lines 193-194), discount "settled at this level" and INR25 crore run rate (lines 304, 317), working capital turns 6x (line 439) | Confirmed |
| ARVIND May 2026 | SUBSTANTIVE | 85% sole sourced (line 273), 88% model-specific (line 680), 60-day working capital (line 154) | Confirmed |
| MAYURUNIQ Feb 2026 | SUBSTANTIVE | "not impacted right now" tariff (line 176) | Confirmed |
| MAYURUNIQ May 2026 | SUBSTANTIVE | "we don't get fixed orders ... projections" (line 357) | Confirmed |
| MAYURUNIQ Aug 2026 | SUBSTANTIVE | "25 plus 1% or 2%" and "abnormally high" FX (lines 215-216); "10% ... natural hedge" (line 335) | Confirmed |
| MAYURUNIQ Nov 2026 | SUBSTANTIVE | "2, 3 years" sampling to order (line 331) | Confirmed |
| GARFIBRES | NOT PROVIDED | No file; not an unused peer | Correct handling |

Unused-material search (government, defence, receivable, debtor, working capital, cash flow, operating cash): all hits are already used in B06 or are non-claim context (state government CSR, FTA commentary, Mexico tariff). No directly claim-relevant statement left unused. No MAJOR or MINOR unused-material finding.

## Verdict-discipline audit

B06 issues 0 VERIFIED, 7 PARTIALLY VERIFIED, 1 UNVERIFIABLE, 0 contradicted. No VERIFIED rests on one peer. No upgrade from silence: Q1 defence share, Q3 and Q7 market growth are stated as unverifiable or peers silent. Q8 is single-peer (Mayur) and correctly capped at PARTIALLY VERIFIED. Weighting note on defence unreachable VERIFIED is correct.

## peer_questions coverage

peer_questions in B05 holds 8 items (lines 61-68; the Q7 line is truncated in display but present, and it is the market-growth/pass-through item). B06 Q1 to Q8 maps one to one. All answered.

## Findings
- MINOR: input gap, 6 of 12 transcripts, disclosed.
- MINOR: Q8 single-peer anchor.
- MINOR: Q5 "supplier paid" line is Arvind-only; Mayur reports no tariff impact.

Counts: critical 0, major 0, minor 3. Acceptance rate 100% (2 of 2 peers handled correctly).

```yaml
stage: B12d
company: "KUSUMGAR"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 2
substantive_confirmed: 2
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Transcripts provided: 6 of 12 (GARFIBRES zero); input gap disclosed in B06, not a pipeline fault"}
  - {severity: MINOR, item: "B06 Q8 PARTIALLY VERIFIED rests on one peer (Mayur); permitted since no VERIFIED claimed, but flagged as single-anchor"}
  - {severity: MINOR, item: "B06 Q5 sentence 'where tariffs bit, supplier paid' rests on Arvind Jan p.8 only; Mayur reports no tariff impact"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
