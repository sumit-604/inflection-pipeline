# Verifier D — Peer Coverage Audit (B06 run 2)
IEX | Run date 2026-09-08 | Model: claude-sonnet-5 | Fresh context, artifacts only

Inputs read: 12 peer transcripts (MCX/BSE/CDSL x 4 quarters, work/ folder,
page-marker `=== PAGE n ===`), B05-concall.yaml (peer_questions[]),
B06-peers.yaml, outputs/reports/06-peers.md.

---

## 0. Process note: did run 2 close the three prior findings?

The prior verifier-D pass on B06 run 1 found one MAJOR (CDSL Nov-2025
marked CITED-ONLY despite carrying Claim-4-relevant evidence) and two
MINOR (BSE Feb-2026 likewise; a miscounted coverage summary line).

- **MAJOR (CDSL Nov-2025) — CLOSED.** Run 2's rework_note and Part 3 move
  this transcript to SUBSTANTIVE, citing the 93%-to-82% incremental
  demat-share figure. Verified against the transcript directly: the 93%
  figure sits on marker page 9, the 82% figure on marker page 10
  (`peer-concalls__CDSL-Concall_Nov_2025_Transcript.txt`, lines 367-373),
  matching B06's "p.9-10" citation exactly.
- **MINOR (BSE Feb-2026) — CLOSED.** Run 2 moves this transcript to
  SUBSTANTIVE, citing the algo/SOR-approval-bottleneck explanation.
  Verified: the SOR/"exchange agnostic" passage sits on marker page 13
  (`peer-concalls__BSE-Concall_Feb_2026_Transcript.txt`, lines 417-427),
  matching B06's "p.13" citation exactly.
- **MINOR (miscounted summary line) — CLOSED.** Run 2 states "12
  SUBSTANTIVE, 0 CITED-ONLY, 0 UNUSED" and the Part 3 table lists 12 rows,
  all SUBSTANTIVE. Arithmetic is now internally consistent.

All three prior findings are closed with real evidence, not just asserted.

---

## 1. Coverage audit: did B06 use the peers it claims to have used?

All 12 peer transcripts are marked SUBSTANTIVE in the Part 3 coverage map.
Rule 2 requires locating the cited material in Parts 1-2 and confirming it
exists in the transcript. Spot-checked citations across all three peers
and all four quarters (page-marker verified against the source file in
each case):

| Citation checked | B06 anchor | Transcript location (marker page) | Result |
|---|---|---|---|
| CDSL "We don't give any client-specific information" | Nov-2025 p.10 | p.10 (line 391, after PAGE 10 marker at 368) | MATCH |
| CDSL "We do not discuss this in our investor calls" | Aug-2026 p.8 | p.8 (line 322, before PAGE 9 marker at 337) | MATCH |
| MCX "I cannot name any specific member... More or less, it would be similar" | Nov-2025 p.16-17 | p.16 (line 608) / p.17 (line 620) | MATCH |
| MCX coal exchange, no size figure, all 4 transcripts | Nov-2025/Feb-2026 silent; May-2026 p.17; Aug-2026 p.6 | grep confirms zero "coal" hits in Nov-2025 and Feb-2026; May-2026 and Aug-2026 discuss coal qualitatively with no tonnage/rupee figure anywhere | MATCH |
| BSE "7% to 8%... far away from what we wanted... SOR... pending for more than six months" | May-2026 p.16 | p.16 (lines 511-522, before PAGE 17 marker at 523) | MATCH |
| BSE "creeping up... double-digit market share... calendar year 2027" | Aug-2026 p.14 | p.14 (lines 438-445, before PAGE 15 marker at 446) | MATCH |
| CDSL loyalty/commitment claim | May-2026 p.7, p.9-10 | p.7 (lines 313-317, before PAGE 8 marker at 318) confirmed; p.9-10 not separately re-verified | MATCH (partial spot-check) |
| CDSL 420bps incremental-share loss | Aug-2026 p.6 | line 234-235, consistent with p.6 region | MATCH |
| MCX Bharat Shah "derailed the situation" / BSE options "37%, 38%" | May-2026 p.13 | lines 494-502 | MATCH |
| MCX "68% yield compression" decomposition | Aug-2026 p.11-12 | lines 391-397 | MATCH |
| CDSL SEBI fetch/creation charge cuts (Rs35→28, Rs20→5) | Aug-2026 p.7-8 | lines 284-287 | MATCH |
| BSE/CDSL: no associate-entity IPO/OFS/stake-sale disclosure (Carried-forward C) | — | grepped "IPO/OFS/stake sale/divest" across all 8 BSE+CDSL transcripts: every hit is about third-party issuer IPO activity or CDSL's own IPO-linked corporate-action fee revenue, none about a BSE/CDSL associate entity's own stake sale or listing | CONFIRMED absence, correctly classified UNVERIFIABLE |

**Every citation spot-checked is real, correctly page-anchored, and
accurately quoted.** No fabricated or misattributed material found across
11 independent spot-checks spanning all three peers and all four quarters.
substantive_unsupported = **none**.

One partial exception on depth, not accuracy: the MCX May-2026
"interoperability" exchange (lines 678-701, marker p.18-19) — management's
argument that interoperability requires "100% similar product" (same
ISIN) and therefore liquidity would not migrate between structurally
different products — is real, accurately findable, and directly on-topic
for the coupling/interoperability theme central to this run. It is
name-checked in B06's Part 3 coverage-map contribution line ("'sticky
liquidity' interoperability defence") but never actually discussed,
quoted, or weighed anywhere in Parts 1, 1B, or 2 of the report. It is a
citation without an analysis attached to it — a small piece of cited-only
material sitting inside an otherwise-substantive transcript. This is not
a rebuttal to any specific claim IEX itself has made (no IEX transcript in
this corpus uses "sticky liquidity" language re coupling, confirmed by
grep), so it is industry-context depth, not a missed direct claim
contradiction; the coupling-severity theme is otherwise well covered by
the Q6 verdict and the 2D independent-mention section. MINOR.

---

## 2. Testing the two counterintuitive findings

**Finding 1 — peers are LESS forthcoming than IEX on concentration
disclosure (Q5, CONTRADICTED).** Independently verified against all three
cited quotes (CDSL Nov-2025 p.10, CDSL Aug-2026 p.8, MCX Nov-2025
p.16-17) — all three are genuine flat refusals or non-answers when asked
comparably direct concentration questions, none softened or
mischaracterized in the report. BSE was independently checked (grep for
member/broker/client-concentration language across all four BSE
transcripts) and found silent, consistent with B06's claim. The
counterintuitive framing holds up: this is a real, well-evidenced finding,
not an artifact of selective quoting.

**Finding 2 — MCX discloses no coal-exchange size figure across its four
transcripts.** Independently re-verified with a direct grep for "coal"
across all four MCX transcripts. Nov-2025 and Feb-2026: zero mentions.
May-2026 and Aug-2026: coal is discussed at length (subsidiary
incorporation, SEBI approval process, "transparent, efficient
technology-driven national coal trading ecosystem") but not one tonnage,
rupee, or percentage figure appears anywhere near any of the four "coal"
passages in either transcript. This finding is fully supported and stated
with appropriate caution in the report (treats silence as a different
failure mode from IEX's unreconciled revision, not a verdict either way).

Both counterintuitive findings survive independent re-verification.

---

## 3. Verdict discipline (Rule 4)

- The one VERIFIED claim (Carried-forward B, non-operating income
  blind spot) rests on three independent peers (MCX, BSE, CDSL,
  anchor_count 6) — clears the ≥2-anchor bar comfortably.
- No verdict is upgraded from silence. UNVERIFIABLE verdicts (Q2, Q3, Q4,
  Carried-forward C) are all explicitly built on documented absence and
  are labeled UNVERIFIABLE, not VERIFIED or CONTRADICTED — the report is
  careful to caveat these ("a finding by absence rather than a tested and
  failed precedent," Q3; "not a finding about IEX's disclosure practice,"
  Carried-forward C). No CRITICAL verdict-discipline failure found.
- CONTRADICTED verdicts (Q5, Q6) rest on multiple, quoted, page-anchored
  peer statements each, not on inference from silence.

verdict_discipline_fails: none found.

---

## 4. Claims-all-addressed check (Rule 5) — the central finding of this audit

B05-concall.yaml `peer_questions[]` (lines 195-201) contains **seven**
entries, not six:

1. Fee realization trailing volume (MCX/BSE/CDSL) — answered, Q1 PARTIALLY VERIFIED
2. MCX electricity derivatives vs. 18%/1% growth claim — answered, Q2 UNVERIFIABLE
3. Long-dated TAM claims, sector-standard or overreach — answered, Q3 UNVERIFIABLE
4. MCX coal-exchange sizing consistency — answered, Q4 UNVERIFIABLE
5. Customer/counterparty concentration disclosure — answered, Q5 CONTRADICTED
6. BSE market-share trajectory vs. NSE — answered, Q6 CONTRADICTED
7. **"Do any of the three peers disclose product-level or segment-level
   market share with degrading precision when a competitive or
   regulatory threat becomes more concrete, the way IEX's disclosure
   narrowed between Q2FY26 and Q1FY27?"** — **NOT ANSWERED.**

B06's rework_note, its report header, and Part 4's triangulation summary
all state the run answers "all six current B05 peer_questions" / "the six
current questions." This miscounts B05's actual list by one. Question 7
receives no verdict anywhere in B06-peers.yaml or 06-peers.md — it is
absent from `verified`, `partially_verified`, `contradicted`, and
`unverifiable`, and absent from the prose. This is a skipped claim per
Rule 5: **MAJOR**.

This is not a trivial omission. The raw material to answer Q7 substantially
overlaps evidence B06 already gathered for Q6: CDSL's disclosure precision
across the four quarters actually SHARPENS under pressure, not degrades
(93% → 82% round-number → "no significant drop" qualitative downplay →
explicit percentage figures → a named 420bps figure in Aug-2026, the most
precise disclosure of the whole arc, given at the point of maximum
pressure); BSE similarly moves from round "7-8%" language toward a named
double-digit target with a dated milestone as pressure persists. Both
data points point toward a third counterintuitive finding in the same
family as Q5 and Q6 — peers' disclosure precision does not degrade under
competitive threat the way IEX's does, and in CDSL's case arguably
improves — but this synthesis step was never taken because the question
was dropped from the run's working list entirely, not because the
evidence was unavailable.

claims_all_addressed = **false**.

---

## 5. Coverage and cross-read spot checks

- Re-grepped the full 12-transcript set for "interoperability", "market
  coupling", "REC"/"renewable energy certificate": confirms B06's implicit
  premise that no peer discusses a comparable coupling event that has
  actually been implemented (input_gap `regulatory_order_text`/
  `peer_precedent_gap` framing holds), with the one exception (MCX's
  interoperability mechanics passage) noted in Section 1 above.
- Re-grepped BSE and CDSL transcripts for IPO/OFS/stake-sale language to
  confirm Carried-forward C's "no comparable event" claim: holds, all
  hits are third-party issuer activity, not an associate-entity
  transaction.
- No additional directly claim-relevant peer statement bearing on IEX's
  claims was found unused in this pass, beyond the MCX interoperability
  item (Section 1, MINOR) and the Q7 gap (Section 4, MAJOR).

---

## Summary

Citation fidelity in this report is excellent: every spot-checked
quote, page anchor, and both flagship counterintuitive findings hold up
against the raw transcripts, and all three prior verifier-D findings from
run 1 are genuinely closed with verifiable fixes. The material defect is
coverage completeness, not accuracy: B06 miscounted B05's current
peer_questions list as six when it is seven, and question 7 (disclosure
precision under threat, peer-wide) was dropped without a verdict, despite
overlapping evidence already sitting in the report's own Q6 material.

peer_utilisation: 12/12 peer-quarters used substantively = 100%.
acceptance_rate: of 10 distinct claims this audit could check (7 current
B05 questions + 3 carried-forward findings), 9 were rendered and verified
clean on independent re-read of the transcripts; 1 (Q7) was never
rendered = 90%.

---

```yaml
stage: B12d
company: "IEX"
run_date: "2026-09-08"
model: claude-sonnet-5
status: complete
run_number: 2
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant:
  - {peer: "MCX (May-2026)", missed_item: "Interoperability mechanics defence: 'interoperability is only possible when there is a 100% similar product... in commodities may be different' -- cited in the Part 3 coverage-map contribution line as 'sticky liquidity interoperability defence' but never discussed, quoted, or weighed in Parts 1, 1B, or 2. No IEX transcript in this corpus uses comparable 'sticky liquidity' language, so this is industry-context depth left on the table, not a missed direct rebuttal to a stated IEX claim.", anchor: "MCX Concall May 2026 Transcript, p.18-19"}
claims_all_addressed: false
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06-peers.yaml / 06-peers.md, entire document (absent); B05-concall.yaml lines 195-201 (source list)", description: "B05-concall.yaml peer_questions[] contains seven questions, not six. B06's rework_note, report header, and Part 4 triangulation summary all state the run answers 'all six current B05 peer_questions.' Question 7 ('Do any of the three peers disclose product-level or segment-level market share with degrading precision when a competitive or regulatory threat becomes more concrete...') receives no verdict anywhere in B06 -- absent from verified/partially_verified/contradicted/unverifiable and from the prose. A skipped claim per Rule 5. Evidence B06 already gathered for Q6 (CDSL's disclosure precision sharpening, not degrading, across the pressure arc; BSE's move toward a named dated target) substantially overlaps what Q7 needed and points toward a third counterintuitive finding never synthesized."}
  - {severity: "MINOR", location: "B06-peers.yaml peer_coverage_map entry for MCX Q4 FY26 (May 2026); 06-peers.md Part 3 table, same row", description: "MCX's interoperability-mechanics passage ('100% similar product' argument for why liquidity would not migrate under interoperability) is name-checked as a SUBSTANTIVE contribution but never actually analyzed in Parts 1, 1B, or 2. Real, accurately quotable, and on-topic for the coupling theme, but functionally cited-only within an otherwise well-used transcript. Not a rebuttal to any stated IEX claim (no 'sticky liquidity' language found in IEX's own corpus), so treated as an industry-context miss rather than a direct-claim miss."}
critical_count: 0
major_count: 1
minor_count: 1
acceptance_rate: 90
peer_utilisation: 100
```
