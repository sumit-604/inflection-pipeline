# Verifier D — Peer Coverage Audit of B06
IEX | Run date 2026-09-08 | Model: claude-sonnet-5 | Fresh context, artifact paths only

Inputs: 12 peer transcripts (runs/iex-2026-09-08/work/peer-concalls__*.txt), B06 report
(outputs/reports/06-peers.md), B06 block (outputs/blocks/B06-peers.yaml), B05 peer_questions
(outputs/blocks/B05-concall.yaml lines 74-78).

Method: verified the four B05 peer_questions all received a verdict in B06; spot-checked every
quote B06 cites as SUBSTANTIVE evidence against the actual transcript text and page; read the
three transcripts B06 marked CITED-ONLY in full for material the claim list should have used;
checked B06's own coverage-map table against its own summary counts.

---

## 1. Claims-addressed check

All four B05 `peer_questions[]` (fee-compression precedent, non-operating income share, IGX
OFS disclosure practice, customer-stickiness defence) received an explicit verdict in B06:
VERIFIED, PARTIALLY VERIFIED, UNVERIFIABLE, CONTRADICTED respectively. No skipped claim.
Rule 5: PASS.

## 2. Citation-fidelity spot checks (SUBSTANTIVE peers)

Checked 14 of B06's cited quotes/figures against the named transcript and page. Every one
matched exactly, including speaker attribution and page location:

| # | Claim | Cited anchor | Verified against transcript |
|---|---|---|---|
| 1 | 1 | BSE May 2026 p.18-19, Devesh Agarwal, "eight months" since Thursday expiry | MATCH (line 578: "it has been eight months that we have to Thursday") |
| 2 | 1 | BSE Nov 2025 p.9, Mohit Mangal, "seen the market share increase in the option derivative segment" | MATCH exactly |
| 3 | 1 | BSE May 2026 p.5-6, Rs.19,523cr vs Rs.8,978cr, +118% YoY, Thursday-transition liquidity broadening | MATCH exactly (verbatim) |
| 4 | 1 | MCX May 2026 p.18, Rishi Nathany, "sticky liquidity" / "does not just go away" | MATCH, correct page (falls between page markers 18-19) |
| 5 | 4 | MCX May 2026 p.13, Bharat Shah, IEX named, "derailed the situation" / BSE options "next to nothing" to "37%, 38%" | MATCH exactly, correct page |
| 6 | 2D | MCX Feb 2026 p.18, Parikshit Gupta, "We all know what is happening with IEX" | MATCH exactly |
| 7 | 4 | CDSL May 2026 p.7/p.9-10, Nehal Vora, "loyalty," "commitment," intangible-moat language | MATCH exactly, both citations |
| 8 | 4 | CDSL Aug 2026 p.6, Hiral Parekh, 420bps incremental-share loss to 81.4% since March | MATCH exactly |
| 9 | 4 | CDSL Aug 2026 p.6, Nehal Vora's non-response, "infrastructure company... not a quarter-on-quarter growth" | MATCH exactly, same page |
| 10 | 4 | CDSL Feb 2026 p.10, Nehal Vora, "no significant drop as I would see it as of now," answering Sanketh Godha | MATCH exactly, correct page |
| 11 | 2 | BSE Nov 2025 p.6, treasury income -32% to Rs.42cr from Rs.63cr | MATCH exactly |
| 12 | 2 | BSE Aug 2026 p.17, Madhukar (JP Morgan), "other income has also picked up quite significantly" | MATCH exactly, correct page |
| 13 | 2 | MCX Aug 2026 p.16, Bunty Chawla, "drastic growth" in other income, magnitude/driver framing only | MATCH exactly |
| 14 | 2D | BSE May 2026 p.19, Rushabh Doshi, payout ratio vs "IEX or NSE" | MATCH exactly |

Zero mismatches, zero anchor-not-found, zero fabricated or paraphrase-drifted quotes across the
sample. Every SUBSTANTIVE citation checked is a real, findable statement in the named peer's
transcript at (or immediately adjacent to) the cited page. Rule 2: PASS on every peer sampled.

## 3. Unused-but-relevant check (CITED-ONLY peers)

B06 marks three transcripts CITED-ONLY: MCX Nov 2025, BSE Feb 2026, CDSL Nov 2025. Read each
in full.

**MCX Nov 2025** — grepped for IEX, market coupling, interoperability, loyalty, other income,
treasury, market share: the only hit is a single analyst request for "transaction charges,
membership fees and float income" bookkeeping figures (line 525-526), no follow-through
discussion. B06's "no decisive contribution" label is accurate. Correctly handled.

**CDSL Nov 2025 (Q2 FY26)** — MAJOR MISS. This transcript already contains the opening move of
the Claim 4 arc, one full quarter earlier than B06's account. Devish Agarwal notes CDSL's
incremental demat-account market share fell from a 93% peak (3Q FY25) to 82% in this quarter
(CDSL Concall Nov 2025 Transcript, p.9-10). Nehal Vora's response pre-figures, almost verbatim,
the deflections B06 later cites from Feb-2026 and Aug-2026: "We've not been losing market...
percentage is basically a relative number... this company is finally a market infrastructure
company, like a road, you have to look at a little more medium-term and long-term perspective"
(same page). B06's Part 3/4 narrative calls the Feb-2026 CDSL call "the first leg of the Claim 4
arc" and treats the May-2026 loyalty claim as an apparently clean, unqualified statement later
contradicted by the Aug-2026 420bps admission. In fact CDSL was already fielding and downplaying
the identical erosion question TWO quarters before making that loyalty claim, not one. This
strengthens, rather than weakens, B06's own CONTRADICTED verdict on Claim 4 — but B06 did not
find it, filed the transcript as bookkeeping-only, and so understated both how early the warning
signs were and how much CDSL management had already been asked (and had already deflected) before
repeating the loyalty framing. Directly claim-relevant, left unused: MAJOR (Rule 3).

**BSE Feb 2026 (Q3 FY26)** — MINOR MISS. Amit Chandra's question and S. Ramamurthy's answer
(BSE Concall Feb 2026 Transcript, p.12-13) already describe the same mechanism B06 cites only
from the May-2026 call for Claim 4: cash-segment share stuck because algo/SOR approvals for
best-price execution face "quite a few bottlenecks," not because of customer loyalty to the
incumbent. This is a real, directly claim-relevant statement left unused, but it is duplicative
of material B06 already uses from a later quarter and does not change the verdict — it only
shows the "structural friction, not loyalty" explanation is older than B06's account suggests.
Graded MINOR: it corroborates rather than adds new information to an already-correct verdict.

## 4. Verdict-discipline audit

- Claim 2 (VERIFIED) rests on 3 independent peers (MCX, BSE, CDSL), anchor_count 6 — clears the
  ≥2-independent-peer-anchor bar for a VERIFIED verdict. PASS.
- Claim 4 (CONTRADICTED) rests on CDSL (own words, two quarters), BSE (own history), and an MCX
  investor (independent third party) — well above the bar, and arguably under-credited given the
  missed CDSL Nov-2025 anchor (section 3 above), which would have made the contradiction stronger
  still, not weaker. No fail.
- Claim 1 (PARTIALLY VERIFIED) and Claim 3 (UNVERIFIABLE) are not VERIFIED verdicts, so the
  ≥2-anchor rule for VERIFIED does not bind; both verdicts are conservative given the corpus (no
  peer precedent exists for Claim 3; only one directly comparable event exists for Claim 1), and
  neither reads as an upgrade from silence.
- No verdict in B06 is upgraded from silence (a "VERIFIED" resting on peer silence). No fail.

verdict_discipline_fails: none found.

## 5. Internal-consistency check on B06's own coverage map

B06's Part 3 table lists 9 rows as SUBSTANTIVE (MCX Feb, MCX May, MCX Aug, BSE Nov, BSE May, BSE
Aug, CDSL Feb, CDSL May, CDSL Aug) and 3 rows as CITED-ONLY (MCX Nov, BSE Feb, CDSL Nov). The
summary line immediately below the table, and echoed in B06-peers.yaml's implicit count, states
"8 SUBSTANTIVE, 4 CITED-ONLY, 0 UNUSED" — this does not match the table it summarises (9 and 3,
not 8 and 4). Total is right (12), the split is wrong. Cosmetic, does not change any verdict, but
it is a factual inconsistency inside the stage's own deliverable. MINOR.

## 6. Peer utilisation and acceptance

- Peers provided: 12 (peer-quarter transcripts).
- Peers actually used substantively, per this audit's read of the table (not the miscounted
  summary line): 9 of 12 = 75%.
- Peers "correctly handled" (accurate classification with a supportable citation, or accurately
  and completely assessed as having nothing decisive): MCX Nov (correct), MCX Feb/May/Aug
  (correct), BSE Nov/May/Aug (correct), CDSL Feb/May/Aug (correct) = 10 of 12. BSE Feb and CDSL
  Nov are classified CITED-ONLY but each holds a directly claim-relevant statement that should
  have been surfaced — not correctly handled, one MAJOR (CDSL Nov) and one MINOR (BSE Feb).
  10/12 = 83%.

No fabricated citations found. No SUBSTANTIVE claim resting on an unsupported anchor. No
CRITICAL finding.

---

## Findings

1. MAJOR — CDSL Q2 FY26 (Nov-2025) transcript marked CITED-ONLY in B06's coverage map, but
   contains a directly Claim-4-relevant peer statement left unused: CDSL's incremental
   demat-account market share already down from 93% (3Q FY25) to 82% this quarter, with
   management's deflection ("look at absolute numbers... market infrastructure company, like a
   road...") pre-figuring the identical language used again in Feb-2026 and Aug-2026. This
   antedates B06's own "first leg of the Claim 4 arc" (which it places at Feb-2026) by one
   quarter and shows CDSL's May-2026 loyalty claim followed two, not one, prior quarters of
   downplayed erosion questions. Strengthens B06's CONTRADICTED verdict but was not found.
   Location: outputs/reports/06-peers.md Part 3 (CDSL Q2 FY26 row) / outputs/blocks/B06-peers.yaml
   peer_coverage_map. Source: peer-concalls__CDSL-Concall_Nov_2025_Transcript.txt, p.9-10.

2. MINOR — BSE Q3 FY26 (Feb-2026) transcript marked CITED-ONLY, but contains an earlier instance
   of the same "SOR/algo-approval bottleneck, not customer loyalty" explanation for BSE's stuck
   cash-segment share that B06 cites only from the May-2026 call for Claim 4. Duplicative of
   already-used material; does not change the verdict. Location: outputs/reports/06-peers.md
   Part 3 (BSE Q3 FY26 row). Source: peer-concalls__BSE-Concall_Feb_2026_Transcript.txt, p.12-13.

3. MINOR — Internal arithmetic inconsistency: B06's Part 3 summary line reads "8 SUBSTANTIVE, 4
   CITED-ONLY, 0 UNUSED," but the coverage-map table immediately above it lists 9 SUBSTANTIVE
   rows and 3 CITED-ONLY rows. The total (12) is right; the split is miscounted. Cosmetic, no
   verdict impact. Location: outputs/reports/06-peers.md line 368.

No CRITICAL findings. No substantive citation was unsupported; every SUBSTANTIVE-marked claim
sampled (14 of the report's cited anchors) was independently confirmed against the source
transcript at the stated page.

---

```yaml
stage: B12d
company: "IEX"
run_date: "2026-09-08"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant:
  - {peer: "CDSL Q2 FY26 (Nov 2025)", missed_item: "Incremental demat-account market share already down from 93% (3Q FY25) to 82% this quarter; management deflection pre-figures the identical language repeated in Feb-2026 and Aug-2026, one quarter earlier than B06's stated 'first leg' of the Claim 4 arc", anchor: "CDSL-Concall_Nov_2025_Transcript.txt p.9-10"}
  - {peer: "BSE Q3 FY26 (Feb 2026)", missed_item: "Same SOR/algo-approval-bottleneck, not-loyalty explanation for BSE's stuck cash-segment share that B06 cites only from the May-2026 call for Claim 4, present one quarter earlier", anchor: "BSE-Concall_Feb_2026_Transcript.txt p.12-13"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "outputs/reports/06-peers.md Part 3 (CDSL Q2 FY26 row); B06-peers.yaml peer_coverage_map", description: "CDSL Nov-2025 transcript marked CITED-ONLY but contains a directly Claim-4-relevant statement left unused: incremental demat market share already down 93%->82% this quarter, with a deflection pre-figuring later quarters' language. Antedates B06's stated 'first leg' of the Claim 4 arc by one quarter; strengthens the CONTRADICTED verdict but was not surfaced. Source: CDSL-Concall_Nov_2025_Transcript.txt p.9-10."}
  - {severity: "MINOR", location: "outputs/reports/06-peers.md Part 3 (BSE Q3 FY26 row)", description: "BSE Feb-2026 transcript marked CITED-ONLY but contains an earlier instance of the same SOR-bottleneck-not-loyalty explanation B06 cites only from May-2026 for Claim 4. Duplicative, no verdict change. Source: BSE-Concall_Feb_2026_Transcript.txt p.12-13."}
  - {severity: "MINOR", location: "outputs/reports/06-peers.md line 368 (Part 3 summary line)", description: "Summary line states '8 SUBSTANTIVE, 4 CITED-ONLY, 0 UNUSED' but the coverage-map table it summarises lists 9 SUBSTANTIVE and 3 CITED-ONLY rows. Total of 12 is correct; the split is miscounted. No verdict impact."}
critical_count: 0
major_count: 1
minor_count: 2
acceptance_rate: 83
peer_utilisation: 75
