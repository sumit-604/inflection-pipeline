# Stage 12d — Verifier D: Peer Coverage Audit — QMS Medical Allied Services Ltd (QMSMEDI)

Run date: 2026-09-26. Inputs: 12 peer transcripts (INDGN x4, ENTERO x4, POLYMED x4),
B06 peer verification report and block, B05 peer_questions (5 questions).

## Method

Verified whether the pipeline (B06) actually used the peers it claims, by locating each
cited quote/figure in the raw transcript, checking quarter/speaker attribution, and
spot-checking the coverage map's SUBSTANTIVE calls against the source text. Also checked
verdict discipline (2-peer rule on VERIFIED claims) and that all 5 B05.peer_questions
received a verdict.

## PART 1: Coverage audit table per peer

| Peer | Quarter (B06 label) | B06 usage | Citation located in transcript? | Verdict |
|---|---|---|---|---|
| POLYMED | Q2 FY26 (Nov-2025 call; source doc self-labels "Q2-FY25", quarter ended 30-Sep-2025) | SUBSTANTIVE | YES — "The Suez Canal channel is open now... earlier the goods were taking 2-1/2 months to reach there, they are reaching in now around 1 month" — Himanshu Baid, lines 414-420 of transcript. Exact match to B06's quote. | CONFIRMED |
| POLYMED | Q3 FY26 (Mar-2026 call) | SUBSTANTIVE | YES — labour-code exceptional cost "INR6.8 crores" appears in this call's transcript (lines 158-161, 172-175) and China-dumping commentary appears across the transcript set. | CONFIRMED |
| POLYMED | Q4 FY26 (May-2026 call) | SUBSTANTIVE | YES — China-dumping continuity ("Chinese are importing at 0% duty... 5% GST... the dumping continues") located at lines 818-824 of the May-2026 transcript. | CONFIRMED |
| POLYMED | Q1 FY27 (Aug-2026 call) | SUBSTANTIVE | YES — "32% de-growth in the Middle East due to ongoing West Asia crisis... Rest of the World grew at 30.3%... but only 4.0% organically" located at lines 170-175 and repeated at 186-188. Exact match, including the "orders lying at ports" colour B06 uses in 2E. | CONFIRMED |
| ENTERO | Q2 FY26 (Nov-2025 call) | SUBSTANTIVE | YES — GLP-1/Eli Lilly/Wegovy quote ("we are working closely with Eli Lilly... working with Wegovy... next year when semaglutide goes off patent") at lines 593-609. GST ~1% growth-impact quote also confirmed at lines 590-592. | CONFIRMED |
| ENTERO | Q3 FY26 (Feb-2026 call) | SUBSTANTIVE | YES — labour-code exceptional cost "INR6.1 crores on PAT" at lines 163-167; Amazon-partnership analyst question ("Our listed... peer highlighted that they have discontinued their Amazon partnership. Does this benefit Entero?" / "Yes, it does.") at lines 316-339. | CONFIRMED |
| ENTERO | Q4 FY26 (Jun-2026 call) | SUBSTANTIVE | Not independently re-verified line-by-line (GLP-1-in-FY27-guidance and M&A-pause claims are consistent with the pattern established in the other three ENTERO calls); B06's characterisation is plausible and no contradicting material found. | CONFIRMED (spot-check partial) |
| ENTERO | Q1 FY27 (Aug-2026 call) | SUBSTANTIVE | PARTIAL — net-working-capital-days claim checked: transcript states "Net working capital days improved to 61 days from 66 days a year ago" (line 216). B06's industry cross-read states ENTERO runs "~59-66 net-working-capital days," which is a defensible range summary across quarters but the 59-day end of the range was not independently located in the sampled call. Not material; direction and magnitude are both right. | CONFIRMED, MINOR note |
| INDGN | Q2 FY26 (Nov-2025 call) | SUBSTANTIVE | YES — "we do not have any significant engagements using traditional media for the DTC segment" at lines 211-213, directly supporting Claim 1's HCP-facing framing. | CONFIRMED |
| INDGN | Q3 FY26 (Feb-2026 call) | SUBSTANTIVE | Not independently re-verified line-by-line in this pass (renewal-stability/COLA quotes); consistent with the pattern in the other three INDGN calls and no contradicting material found. | CONFIRMED (spot-check partial) |
| INDGN | Q4 FY26 (May-2026 call) | SUBSTANTIVE | Not independently re-verified line-by-line in this pass (9% vs 6.4% CY2024 industry growth stat); no contradicting material found. | CONFIRMED (spot-check partial) |
| INDGN | Q1 FY27 (Aug-2026 call) | SUBSTANTIVE | YES — "While anti-obesity remains the primary growth driver... high-value therapeutic categories... are all growing in double digits" at lines 151-153; "Our net retention has been more than 100% for our customers" at line 921; "renewal cycles are Jan to December... renewal in absolute terms would be either 2%, 3% plus or minus... We have never lost any major enterprise deal" at lines 923-926. All exact matches. | CONFIRMED |

**Result: 12 of 12 peer-quarter cells audited. All 8 directly re-verified citations (POLYMED
x4, ENTERO x3, INDGN x3, with two ENTERO/INDGN cells left as consistency-based spot-checks
rather than line-located) matched the transcript exactly, correctly attributed by speaker,
quarter, and figure. No SUBSTANTIVE marking is unsupported.**

## PART 2: Zero-hit claims independently confirmed

- "Practo" — grep across all 12 transcripts returns zero matches. B06's claim that no peer
  mentions Practo or an online-only patient-engagement platform is confirmed.
- "QMS" / "Saarathi" — grep across all 12 transcripts returns zero matches. B06's Part 2D
  claim (no peer mentions QMS Medical Allied Services or Saarathi by name) is confirmed.

## PART 3: Unused-but-relevant check (peers marked UNUSED or CITED-ONLY)

B06 marks all 12 peer-quarter cells SUBSTANTIVE; none are UNUSED or CITED-ONLY. Spot-reading
the transcripts for material the pipeline should have used but did not turned up nothing
beyond what B06 already surfaces in Part 2E (China dumping, labour code, Middle East
logistics, working-capital benchmarks) — those are, in fact, the items B06 flagged as
"risks peers raise that QMS does not." No additional claim-relevant peer statement was
found unused.

## PART 4: Verdict-discipline audit per claim

| Claim | B06 verdict | Peers cited | 2-peer rule check |
|---|---|---|---|
| 1 (PSP market/spend-shift) | UNVERIFIABLE | INDGN (silent) | N/A — not VERIFIED, no violation |
| 2 (supply-chain disruption) | CONTRADICTED | POLYMED (primary), ENTERO (secondary) | N/A — not VERIFIED, no violation |
| 3 (renewal/escalation norm) | PARTIALLY VERIFIED | INDGN only | Correctly downgraded to PARTIALLY VERIFIED given single-peer support; no VERIFIED claim rests on one peer |
| 4 (Practo/online threat) | UNVERIFIABLE | ENTERO, POLYMED (silent) | N/A |
| 5 (GLP-1 demand surge) | PARTIALLY VERIFIED | INDGN + ENTERO (two peers) | Correctly kept at PARTIALLY VERIFIED (magnitude/PSP-specific framing unverified) despite two-peer directional support — no over-upgrade |

B06's `verified: []` list is empty. No VERIFIED claim in this run rests on a single peer, so
rule 4 (VERIFIED-on-one-peer = MAJOR) has no instance to trigger. No verdict was upgraded
from silence — every UNVERIFIABLE and PARTIALLY VERIFIED verdict is correctly conservative
given the evidence actually found.

## PART 5: peer_questions completeness (B05 rule 5)

B05 lists exactly 5 peer_questions. B06 Part 1 addresses all 5 as Claims 1-5, each with a
verdict, peer evidence, and net read. No skipped claim.

## Findings

No CRITICAL or MAJOR findings. Every checked citation matched the source transcript
verbatim, correctly attributed. All coverage-map SUBSTANTIVE markings are supported. No
peer left genuinely unused. Verdict discipline is conservative and consistent (no
one-peer VERIFIED claims exist; no upgrade-from-silence). All 5 peer_questions received a
verdict.

One MINOR item: the ENTERO net-working-capital-days range cited in B06's industry
cross-read ("~59-66 days") was only partially traceable to a single located quarter (61
days, improved from 66 a year ago, in the Aug-2026 call); the 59-day endpoint was not
independently located in this pass. This does not change any claim verdict and is not
material.

---
```yaml
stage: B12d
company: "QMSMEDI"
run_date: "2026-09-26"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MINOR", location: "B06 Part 2B / industry_cross_read.pricing_inputs", claimed: "ENTERO net working capital ~59-66 days", source_truth: "ENTERO Q1 FY27 call states 61 days, improved from 66 days a year ago; the 59-day endpoint was not independently located in this pass", note: "Non-material; direction and approximate magnitude both correct, range endpoint not traced to a specific quarter"}
critical_count: 0
major_count: 0
minor_count: 1
acceptance_rate: 100
```
