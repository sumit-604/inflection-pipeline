# STAGE 12 VERIFIER D: PEER COVERAGE AUDIT — Pitti Engineering Ltd (PITTIENG)
Run: pittieng-2026-09-05 | Audits: B06 (Stage 6 Peer Concall Verification) against the 12 raw peer
transcripts (RKFORGE x4, SANSERA x4, VILAS x4) and the injected B05 peer_questions claim list.
Model: claude-sonnet-5

Method: every peer transcript was read in full from its page-marked text sidecar. Every inline
quote cited in B06 Parts 1-2 tied to one of the six claims was located in its source transcript and
checked against (a) whether the quoted words exist, (b) whether the cited PDF page number is
correct, (c) whether the cited speaker actually said it, and (d) whether the cited call/quarter is the
one that actually contains it. Page numbers below use the sidecar's "===== PAGE N =====" markers
as the PDF page index, per this run's anchor convention.

---

## PART 1: COVERAGE AUDIT TABLE PER PEER

| # | Peer | Call | B06 usage tag | Verdict |
|---|---|---|---|---|
| 1 | RKFORGE | Q2/H1 FY26 (Nov-2025) | SUBSTANTIVE | CONFIRMED — real content used (railway traction quote, p.4; Rs 200 Cr castings order, quoted content real but page mis-cited, see Finding F3; net-debt run-up figure misattributed to wrong speaker, see Finding F1) |
| 2 | RKFORGE | Q3 FY26 (Feb-2026) | SUBSTANTIVE | CONFIRMED — Rs 2,000 Cr railway demand quote (p.5) and Rs 350 Cr debt-reduction quote (p.6) both verified verbatim and correctly attributed to Milesh Gandhi / Lalit Khetan respectively |
| 3 | RKFORGE | Q4 FY26 (May-2026) | SUBSTANTIVE | CONFIRMED — railway share 4.6%→7.5% (p.4) and capex-discipline "Rs.300 to Rs.400 crores maximum" (p.13) both verified verbatim |
| 4 | RKFORGE | Q1 FY27 (Jul-2026) | SUBSTANTIVE | CONFIRMED — net debt Rs 1,900 Cr (p.17), asset-turn/Rs 9,000 Cr sales (p.19), and working-capital-day targets (p.21) all verified verbatim; one adjacent figure in the same exchange (op cash flow "Rs 840 crores... highest in history") is the analyst's own assertion, not a management-confirmed number — see Finding F4 |
| 5 | SANSERA | Q2/H1 FY26 (Nov-2025) | SUBSTANTIVE | CONFIRMED — 10-20% base-tariff discussion (p.7) and skilled-manpower-shortage quote (p.11) both verified verbatim; NOTE the "we will run out of space" quote B06 attributes to this call is NOT in this transcript — it belongs to the Q4 FY26 call, see Finding F2 |
| 6 | SANSERA | Q3 FY26 (Feb-2026) | SUBSTANTIVE | CONFIRMED — 18% tariff quote verified verbatim (p.7); "trade deal and EU FTA" quote real but page mis-cited (p.2 cited vs actual p.3), see Finding F3 |
| 7 | SANSERA | Q4 FY26 (May-2026) | SUBSTANTIVE | CONFIRMED — 12%→11% op-cash-flow-pressure quote verified verbatim (p.16); AI/semicon quote verified verbatim (p.4); forging-shortage "40% increase" quote real but page mis-cited (p.9 cited vs actual p.10), see Finding F3; "we will run out of space" IS here (p.8), but B06 mislabels it as a Q2 FY26 quote — see Finding F2 |
| 8 | SANSERA | Q1 FY27 (Aug-2026) | SUBSTANTIVE | CONFIRMED — "stop-gap arrangement" India-sourcing quote (p.7) and FY29/FY30 AI-demand-visibility quote (p.18-19) both verified verbatim and correctly attributed to Hari Krishnan |
| 9 | VILAS | H1 FY25 (Nov-2024) | SUBSTANTIVE | CONFIRMED — BIS/Korea-mill quote verified verbatim and correctly attributed to Nilesh Patel (p.10) |
| 10 | VILAS | FY25 (May-2025) | SUBSTANTIVE | CONFIRMED — 60% local / 40% import split and Germany/Japan/Korea/Russia sourcing basket verified verbatim (p.22); no explicit inline page anchor given in B06 Part 1 prose for this call, but the coverage-map description is accurate and the content is genuinely present |
| 11 | VILAS | H1 FY26 (Nov-2025) | SUBSTANTIVE | CONFIRMED — Chinese-mill BIS reopening / 15-20% CRGO price decline quote verified verbatim (p.5) |
| 12 | VILAS | FY26 (May-2026) | SUBSTANTIVE | CONFIRMED — two-mill BIS renewal uncertainty quote verified verbatim and correctly attributed (p.7); anti-dumping-duty quotes verified verbatim at BOTH cited locations (p.14 and p.16); working-capital 95-100 day cycle quote verified verbatim (p.7) |

Coverage conclusion: all 12 peer transcripts were genuinely read and substantively used, as B06
claims. No peer marked SUBSTANTIVE turns out to be padding or a fabricated citation. Two specific
inline citations, however, are factually wrong in ways that matter (Findings F1 and F2, both MAJOR):
one attributes an analyst's own figure to management, the other cites the wrong quarter's call
entirely for a load-bearing quote in Claim 4. A further pattern of three page-number-only slips
(Finding F3, MINOR each) reduces anchor precision without changing any verdict's substance.

No peer was marked UNUSED or CITED-ONLY, and a full read of all 12 transcripts did not surface
material directly relevant to the six B05 claims that B06 failed to use. The transcripts contain other
content B06 folds into "Part 2 unprompted cross-read" and "risks peers raise" (energy/gas cost,
Labour Code charge, skilled-labour attrition, customer concentration, anti-dumping risk, BIS
renewal risk) rather than into the six claim verdicts, which is the correct placement since none of
that content was asked for by a B05 claim.

---

## PART 2: VERDICT-DISCIPLINE AUDIT PER CLAIM

| Claim | B06 verdict | Peers used | Independent-peer count | Discipline check |
|---|---|---|---|---|
| 1. BIS Korea/Japan steel resolved | CONTRADICTED | VILAS only (4 calls) | 1 peer (VILAS is the only relevant peer per B05's own check_peers list) | PASS. Rule 4's ≥2-peer bar binds VERIFIED verdicts; this is CONTRADICTED, and B06 itself flags the single-peer, adjacent-market (CRGO vs CRNGO) limitation transparently in its flags block and net-read prose. No overreach. |
| 2. India-US tariff relief + customer-acquisition tailwind | VERIFIED | SANSERA + RKFORGE (2 peers, 5 anchors) | 2 independent peers | PASS. Meets the ≥2-independent-peer bar for a VERIFIED verdict. Anchors independently verified verbatim (SANSERA p.7 Feb-2026; RKFORGE p.5 and p.9 Nov-2025; SANSERA p.7 Aug-2026). Not upgraded from silence — both peers state the tailwind affirmatively. |
| 3. Railway capex moderating | CONTRADICTED | RKFORGE only (all 4 calls) | 1 peer (only RKFORGE serves this end market per B05's check_peers list) | PASS. Single-peer CONTRADICTED is not barred by Rule 4 (which binds VERIFIED); B06 names the segment-mapping caveat (RKFORGE's domestic wheels/bogies vs Pitti's export lamination customers) explicitly. Anchors verified verbatim. |
| 4. Casting/machining capacity tightness = biggest bottleneck | PARTIALLY VERIFIED | SANSERA (supports) + RKFORGE (contradicts) | 2 peers, genuine split | PASS on structure, but one supporting anchor is corrupted: the "we will run out of space" quote is misattributed to the wrong call (Finding F2). The underlying PARTIALLY VERIFIED conclusion survives on the other anchors (forging-shortage quote, machine-lead-time quote, RKFORGE's spare-capacity evidence), but this specific citation must be corrected. |
| 5. Data-centre genset demand surge | UNVERIFIABLE | None directly; SANSERA cited as adjacent-only | 0 peers on-point, correctly flagged | PASS. B06 does not upgrade on plausibility; it explicitly separates the SANSERA AI/semicon macro read (real, verified quote) from a genset-specific claim it cannot speak to. This is correct verdict discipline for a claim with no on-point peer. |
| 6. WC/net-debt build is industry-wide, not Pitti-specific | CONTRADICTED | VILAS + RKFORGE + SANSERA (all 3) | 3 peers | PASS on structure. One supporting RKFORGE anchor (Sunny Gosar's "Rs. 2,500 crores" figure) is misattributed to Lalit Khetan (Finding F1); the CONTRADICTED verdict itself is not put at risk because RKFORGE's own CFO independently confirms a comparable net-debt run-up and a faster, quantified unwind elsewhere in the same transcript set (Rs 2,250 Cr and Rs 350 Cr reduction, correctly attributed, Q3 FY26 p.6; Rs 1,900 Cr, Q1 FY27 p.17). |

claims_all_addressed: every claim in the injected B05 peer_questions list (6 of 6, identical wording
and identical check_peers lists to B06's own Claims 1-6) received an explicit verdict. No skipped
claim.

verdict_discipline_fails: none that change a verdict. Two citation-integrity defects (F1, F2) sit
inside claims 6 and 4 respectively without being load-bearing enough to flip either verdict, given
the other, correctly-anchored evidence carrying each claim.

---

## PART 3: FINDINGS

**F1 — MAJOR — misattributed speaker, Claim 6 (RKFORGE net-debt figure).**
B06 writes: "RKFORGE shows a genuine net-debt run-up... (debt 'shot up as on September '25 to, I
think, more than Rs. 2,500 crores' on capex plus a working-capital and creditor swing, RKFORGE, Q2
FY26 call, **Lalit Khetan**, PDF p.9)." The actual transcript (RKFORGE Nov-2025 call, p.9) shows this
exact sentence spoken by the analyst **Sunny Gosar** as a question ("My first question is on the debt
levels. So, debt levels have substantially shot up as on September '25 to, I think, more than Rs. 2,500
crores..."). Lalit Khetan's actual answer, on the same page, confirms a debt increase but gives a
different figure and mechanism ("that has almost gone up by Rs. 600 crores in the 6 months... Rs.
400 crores capex... Rs. 200 crores reduction on account of creditors"), and Naresh Jalan later
clarifies the figure as "close to Rs. 2,400 crores," not Rs. 2,500 crores. Presenting an analyst's
speculative figure as a management-confirmed statement overstates the evidentiary weight of this
anchor. Net effect on the claim: minor — the CONTRADICTED verdict for Claim 6 does not depend on
this figure; it is carried by RKFORGE's independently-confirmed, correctly-attributed debt-reduction
schedule elsewhere (Q3 FY26 p.6, Q1 FY27 p.17).

**F2 — MAJOR — wrong call cited, Claim 4 (SANSERA "run out of space").**
B06 writes: "SANSERA is racing to add ADS capacity every quarter... specifically because it cannot
make orders fast enough: 'we will run out of space' (**Q2 FY26 call**, PDF p.7)." This exact phrase
does not appear anywhere in the SANSERA Q2/H1 FY26 (Nov-2025) transcript (confirmed by full-text
search: no match). It is spoken by B.R. Preetham in the **Q4 FY26 (May-2026)** call, page 8: "The way
we see the momentum building up in ADS, I'm very, very -- pretty sure that we will run out of space."
Citing the wrong quarter for a quote used to support an "every quarter" pattern claim weakens the
multi-quarter framing (the quote is one data point from one call, not evidence spread across the
period as implied). The PARTIALLY VERIFIED verdict for Claim 4 survives on other, correctly-cited
anchors (the forging-shortage quote genuinely is Q4 FY26, just mis-paged — see F3 — and the
mother-machine lead-time quote is genuinely Q4 FY26 as B06's own parenthetical states).

**F3 — MINOR (three instances) — off-by-one page-anchor slips.**
Three quotes are real, correctly attributed to the right speaker and the right call, but cited to the
page before the one that actually contains them:
- RKFORGE Nov-2025: "we have bagged orders worth Rs. 200 crores" — cited p.4, actual p.5.
- SANSERA Feb-2026: "Following the interim U.S.-India trade deal and EU FTA..." — cited p.2, actual p.3.
- SANSERA May-2026: "forging could be a very, very -- there could be a shortage..." — cited p.9, actual p.10.
Each is trivially locatable one page from the cited anchor and does not affect any verdict. Flagged as
a pattern because three independent slips in the same direction suggest a systematic off-by-one in
part of the page-counting method used when drafting B06, worth a quick anchor QA pass before this
report is relied on downstream.

**F4 — MINOR — analyst assertion presented without provenance flag, Claim 6.**
B06's Claim 6 net-read cites, from the same RKFORGE Q1 FY27 exchange as the (correctly-attributed)
working-capital-day targets: "operating cash flow 'after working capital at about Rs. 840 crores last
year and probably is highest in the history of the company' (same call, PDF p.21)." This sentence in
the transcript is spoken by the analyst Bharat C. Shah as a framing remark inside his question, not
independently confirmed with that figure by Lalit Khetan in his reply (which addresses the
improvement plan, not the Rs 840 Cr number itself). Management does not contest the figure, but it
is not sourced to management either. Does not change the verdict; noted for citation hygiene.

---

## PART 4: CONCLUSION

The pipeline actually used the peers it claims to have used. All 12 transcripts were read and mined
substantively across all six claims and the unprompted cross-read sections; no SUBSTANTIVE tag
was padding. Verdict discipline holds structurally: the one VERIFIED claim clears the ≥2-independent-
peer bar with correctly-anchored evidence, no claim was skipped, and no verdict was upgraded from
silence. Two MAJOR citation-integrity defects were found (an analyst's question misattributed to
management in Claim 6, and a quote pulled from the wrong quarter's call in Claim 4), plus a small
cluster of MINOR page-anchor slips. None of these defects is load-bearing enough to flip a verdict,
because each affected claim carries independent, correctly-anchored evidence elsewhere — but both
MAJOR items should be corrected in B06 before the report is used to brief a valuation stage, since a
downstream reader relying on the "Lalit Khetan" or "Q2 FY26" attributions as-is would be citing
evidence that does not exist as described.

```yaml
stage: B12d
company: "PITTIENG"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 Claim 6 net-read", claimed: "RKFORGE, Q2 FY26 call, Lalit Khetan, PDF p.9 — 'debt levels have substantially shot up as on September '25 to, I think, more than Rs. 2,500 crores'", source_truth: "RKFORGE Nov-2025 transcript p.9: this sentence is spoken by analyst Sunny Gosar as a question, not by Lalit Khetan; Lalit Khetan's actual reply cites a Rs 600 Cr six-month increase and Naresh Jalan later states 'close to Rs. 2,400 crores'", note: "analyst's figure misattributed to management; does not flip Claim 6's CONTRADICTED verdict, which is independently carried by correctly-attributed RKFORGE debt-reduction figures elsewhere"}
  - {severity: "MAJOR", location: "B06 Part 1 Claim 4 net-read", claimed: "'we will run out of space' cited as SANSERA Q2 FY26 call, PDF p.7", source_truth: "phrase does not appear in the SANSERA Nov-2025 (Q2/H1 FY26) transcript at all; it appears in the SANSERA May-2026 (Q4 FY26) transcript, PDF p.8, spoken by B.R. Preetham", note: "wrong quarter cited for a quote used to support an 'every quarter' capacity-racing pattern; PARTIALLY VERIFIED verdict for Claim 4 survives on other correctly-cited anchors"}
  - {severity: "MINOR", location: "B06 Part 1 Claim 3/4 quotes", claimed: "RKFORGE Nov-2025 'bagged orders worth Rs. 200 crores' cited PDF p.4; SANSERA Feb-2026 'trade deal and EU FTA' cited PDF p.2; SANSERA May-2026 'forging could be a very, very shortage' cited PDF p.9", source_truth: "actual pages are p.5, p.3, and p.10 respectively (confirmed by page-marker search)", note: "three independent off-by-one page slips, all in the same direction; content and attribution otherwise correct; no verdict affected"}
  - {severity: "MINOR", location: "B06 Part 1 Claim 6 net-read", claimed: "RKFORGE Q1 FY27 call, PDF p.21 — operating cash flow 'about Rs. 840 crores last year and probably is highest in the history of the company'", source_truth: "this figure is spoken by analyst Bharat C. Shah inside his own question, not confirmed with that number by management in the same exchange", note: "sourcing-provenance gap, not a fabrication; management does not contest the figure but does not independently restate it either"}
critical_count: 0
major_count: 2
minor_count: 4
acceptance_rate: 100
```
