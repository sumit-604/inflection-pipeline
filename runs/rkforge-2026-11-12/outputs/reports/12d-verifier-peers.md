# VERIFIER D: Peer coverage audit, RKFORGE, run 2026-11-12

Method: read B06 (outputs/reports/06-peers.md) and the peer_questions list in B05-concall.yaml. Grepped the page-marked .txt transcripts for B06's quotes and page anchors. Page marker `[page N]` precedes the page's text, so a line below marker N and above marker N+1 sits on page N.

## Coverage audit per peer (Rule 2)

All 12 peer-calls are marked SUBSTANTIVE in B06 Part 3. None is UNUSED or CITED-ONLY, so Rule 3 has no object. Citations spot-checked (quote found and page matches):

| Peer call | B06 anchors checked | Result |
|---|---|---|
| BHARATFORG Nov 2026 | "18 to 20 months" blocking and order-inflow "varied quite substantially" p7 (lines 265-270, page 7 spans 251-289); analyst "weakness in the orders" p7; aerospace plant "60% sold out" p5 (line 211) | Confirmed |
| BHARATFORG Aug 2026 | 160 bps (line 102); capex "1,800-odd crores" (229); asset turn "above 1.5" (277) | Confirmed |
| BHARATFORG May 2026 | Capex Rs 800-850 Cr over 15-18 months p5 (211); ageing US fleet p8-9 (330); AMCA prototype 2032 p16 (614-615) | Confirmed |
| BHARATFORG Feb 2026 | EBITDA 27.3% p3 (109); utilisation 60-65% p4 (138) | Confirmed |
| MMFL Aug 2026 | "running pretty hot" p3 (96); Hormuz freight p13 (494); inventory "7 to 10 days" and "rapid action force" p16 (611-612) | Confirmed |
| MMFL Mar 2026 | Class 8 "shot through the roof" p5 (249); "second half of 2027" p9 (453); "our competition would be Bharat, Ram Krishna, and Happy Forge" p11 (563); "clawed back" p13 (632) | Confirmed |
| MMFL Feb 2026 | Gross margin 56.34% p16 (682); "brutal" domestic competition p16 (657); EU FTA "certainly will bring" p13 (532) | Confirmed |
| MMFL Nov 2025 | "at best 1.2" p11 (427); "ceded some market share" (767, late page, B06 cites p18) | Confirmed |
| HAPPYFORGE Aug 2026 | 59% / 78% utilisation p5 (197); price revisions 4.5-5% (263); USD 4,500 of 6,000 container recovery p8 (318); CV production "almost 10%" p8 (304); "inquiry flow is very strong... Europe 60% of exports" p10 (406-407); "Inventory days. 50 days" p9 (362) | Confirmed |
| HAPPYFORGE May 2026 | Steel lag "1 month... export lag of 1 quarter" p8 (337) | Confirmed |
| HAPPYFORGE Feb 2026 | "almost 85% of the business" p9 (364); Tata Motors alloy steel settlement p13 (529); "excess inventories" CV p15 (627) | Confirmed |
| HAPPYFORGE Nov 2025 | Raw material "settled after 6 months" p12 (481) | Confirmed |

Result: 12 of 12 SUBSTANTIVE confirmed. Substantive_unsupported: none. Unused_but_relevant: none. Not every B06 sentence was re-verified, only 1 to 6 anchors per call, chosen on the load-bearing verdicts (Q2, Q3, Q4, Q6, Q8, Q10, 2D).

## Verdict discipline per claim (Rules 4 and 5)

| Q | B06 verdict | Independent peer anchors | Discipline |
|---|---|---|---|
| Q1 CV/PV/IIP | PARTIALLY | Happy, MMFL, BF directional; no magnitude | OK. "Not corroborated" stated. |
| Q2 Class 8 | VERIFIED | MMFL (3 calls) and BF (3 calls), two independent peers | OK. Counter-signal (October inflow weakness) disclosed. |
| Q3 Steel lag | PARTIALLY | Happy (3 calls); BF ambiguous, excluded | OK. Not upgraded. |
| Q4 Energy/shipping | VERIFIED | BF, Happy, MMFL (three peers) | MINOR: see finding 1. |
| Q5 GM vs EBITDA | PARTIALLY | Happy, MMFL, BF gap benchmark; selectivity unsupported | OK. |
| Q6 Share | PARTIALLY | MMFL lost, Happy gained | OK. |
| Q7 Capex | PARTIALLY | All three raise; 75-80% gate not found | OK. |
| Q8 Asset turn | PARTIALLY | Computed from Data_Sheet plus MMFL, BF, Happy statements | OK. Computed ratios labelled. |
| Q9 Aerospace | UNVERIFIABLE | None | OK. Nothing filled from silence. |
| Q10 Working capital | PARTIALLY | Computed days; bill discounting NOT FOUND at peers | OK. |
| Q11 EU FTA | PARTIALLY | Happy inquiries, MMFL sentiment; no FTA link | OK. |

Any VERIFIED on one peer: none. Any verdict upgraded from silence: none (Q9 and the bill-discounting half of Q10 stay at UNVERIFIABLE / NOT FOUND). Peer_questions count is 11 in B05 and 11 in B06 Part 1; Q1 to Q11 match the B05 wording in order. All addressed.

## Findings

1. MINOR. Q4 is VERIFIED against a reworded claim. B05 says "without customer recovery". B06 verifies "cost borne, recovery lagged or partial". Happy (price revisions 4.5-5%) and BF (H2 recovery expected) show recovery under way. As written, the claim is only partly supported. B06 states this in its net read, so no one is misled, but the label would be PARTIALLY VERIFIED under the strict reading. Does not change the stage conclusion.
2. MINOR. Q9: BF Aug 2026 has defence approval discussion (ATAGS, FOPM, plant timeline of 2.5 years after approval, lines 280-282, 469-505). It is not an aerospace forging approval timeline. UNVERIFIABLE stands. Industry context only.

Counts: critical 0, major 0, minor 2. Acceptance rate 12 of 12 peers correctly handled = 100%.

```yaml
stage: B12d
company: "RKFORGE"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 12
substantive_confirmed: 12
substantive_unsupported: []
unused_but_relevant: []
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Q4 verdict VERIFIED rests on a reworded claim. B05 asks whether peers bear the cost 'without customer recovery'; B06 verifies 'cost borne, recovery lagged or partial, not nil'. Cost-borne has 3 peer anchors (BF Aug-26 p3, Happy Aug-26 p8, MMFL Aug-26 p13); no-recovery is contradicted by Happy and BF. PARTIALLY VERIFIED would fit the claim as written. Not an upgrade from silence; B06 states the distinction in its own text."}
  - {severity: MINOR, item: "Q9 aerospace: BF Aug-26 lines 280-282 and 469-505 discuss defence approvals (ATAGS, FOPM, 2-3 months to start / 2.5 years to run a plant). Not an aerospace forging approval timeline; UNVERIFIABLE stands. Industry-context only."}
critical_count: 0
major_count: 0
minor_count: 2
acceptance_rate: 100
```
