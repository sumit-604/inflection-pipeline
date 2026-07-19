# Verifier Disagreement Log — SHYAMMETL 2026-07-19

Every point where a downstream/other-family read conflicted with a Verifier A
(Haiku, out-of-family) source-fidelity finding, and how it resolved. Haiku is
the sole authority on whether a number exists in the source; clearances below
were established by Verifier A re-reading the source PDF at the correct anchor.

## Phase 1

| Date | Run | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-07-19 | shyammetl-2026-07-19 | Consol PAT decline 1,034.79->908.10cr, EPS -17.3% | Pass 1: ANCHOR NOT FOUND ("AR not in inputs"). Recheck: MATCH at AR consol P&L | B02 (sonnet) asserted the figure | FLAG CLEARED — source re-check found it at correct anchor (Verifier A recheck) | Pass-1 flag was a false absence: verifier had not opened the AR (present at inputs/annual-report/) |
| 2026-07-19 | shyammetl-2026-07-19 | Unrecognised DTA 686.32->955.21cr, tax effect 240.43cr, FY24 (338.57)cr | Pass 1: ANCHOR NOT FOUND. Recheck: MATCH at Note 24(c) p.304 / Note 37(c) p.309 | B02 asserted the figures | FLAG CLEARED — source re-check found them at correct anchor | False absence on pass 1 |
| 2026-07-19 | shyammetl-2026-07-19 | Cross-holding standalone equity investment 253.05cr | Pass 1: UNANCHORED. Recheck2: MATCH at Note 43 standalone | B02/B03 asserted it | FLAG CLEARED — source re-check found it | — |
| 2026-07-19 | shyammetl-2026-07-19 | Combined promoter-entity stake in SMEL: B02 said ~35.18%, B03 said ~65% | Recheck2: 35.18% CONFIRMED (Narantak 15.48% + Subham Capital 14.61% + Dorite 5.09%), AR Note 18(e) p.296-297 | B02 (35.18%) vs B03 (~65%) conflicted | GATE HELD — figure corrected at source: 35.18% is correct; B03's 65% removed/corrected | Verifier A adjudicated an intra-pipeline conflict; B02 was right |
| 2026-07-19 | shyammetl-2026-07-19 | CARO clause 3(xvii) cash-loss entity count | B02: 11 of 13. Offset-corrupted recheck: 9 of 13. Final clean recheck2 (exact PDF p.233, per-entity list): 10 of 13 — MISMATCH, severity CRITICAL | B02 (sonnet) asserted 11 of 13 | GATE HELD — figure corrected at source to 10 of 13 (auditable per-entity list). Non-verdict-card red-flag count; correct-at-source resolves it, no REWORK escalation. Qualitative conclusion (systemic cash losses, 77% of entities) unchanged | The one surviving CRITICAL. Off-by-one; corrected. First recheck's "9" was an artifact of a bad page offset supplied by the orchestrator (self-corrected in recheck2) |
| 2026-07-19 | shyammetl-2026-07-19 | Standalone related-party trade receivables 729.52cr / 78.1% | Recheck2: 726.53cr / 77.77% — MISMATCH (2.99cr, 0.33pp), AR Note 42 | B02 asserted 729.52cr / 78.1% | GATE HELD — figure corrected at source to 726.53cr / 77.77% | Immaterial to conclusion |
| 2026-07-19 | shyammetl-2026-07-19 | B04 FY26 raw-material ratio ~72% (Inv. Pres. p.57, 13,352.6cr) | Recheck2: 73.68% (13,680.15cr, audited P&L) — MISMATCH, source-basis (deck bundling vs audited) | B04 (sonnet) used the deck figure | GATE HELD — figure corrected at source to audited 73.68% | Audited P&L authoritative over the IR deck |
| 2026-07-19 | shyammetl-2026-07-19 | SSPL entity share-in-consol-profit 722.34->417.15cr (Note 47) | Recheck2: ANCHOR NOT FOUND — Note 47 table located (AR PDF p.298-302) but SSPL row not legible in extraction | B02 (two sonnet passes) + B03 independently sourced these figures | UNRESOLVED — rendering/legibility limit named per run-log rule; carry as source-supported-but-verifier-unconfirmed; re-read at phase 3 | Not a fabrication; three sonnet reads agree |
| 2026-07-19 | shyammetl-2026-07-19 | B08 ED PMLA attachment 159.51cr; CPCB Rengali closure | UNANCHORED (no filing PDF in inputs) | B08 sourced via web (MEDIA-REPORTED) + operator context | GATE HELD as-designed — remain caveated MEDIA-REPORTED flags, not anchored figures; corroborated by Q4 FY26 concall ED-coal-notice deflection (B05) | announcements/ folder empty this run; expected UNANCHORED |

**Phase 1 summary:** 4 flags CLEARED by source re-check (false absences from the verifier not opening the AR on pass 1); 4 figures CORRECTED at source (CARO 11->10, RP receivables 78.1->77.77%, raw-material 72->73.68%, cross-holding % 65->35.18); 1 UNRESOLVED rendering-limit (SSPL Note 47 profit, source-supported); expected UNANCHORED web items retained as caveated. Zero fabrications. No verdict-card / Section 1B pillar input affected. Source-fidelity gate HELD.

## Phase 3

phase 3: none. Phase 3 produced no new Verifier A source-fidelity findings. The phase-3 verifier work was Verifier C valuation-adherence (B12c-valuation) on B11 Role 1 and B14 Role 2; a valuation-adherence finding is not a source-fidelity finding and does not belong in this log. The one carry-forward item from phase 1, the SSPL Note 47 entity profit (722.34->417.15cr), was scheduled for phase-3 re-read but remained rendering-limited (source-supported, three sonnet reads agree); no Verifier A re-adjudication occurred that would create a new disagreement row. No downstream phase-3 step leaned on or attempted to keep a figure Verifier A had flagged.
