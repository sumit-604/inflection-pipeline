# Stage 0 — Input Validation (B00)

Company: Divgi Torqtransfer Systems Ltd (DIVGIITTS)
Run date: 2026-08-29 | run_type: full | CMP Rs 1,175 | m-cap Rs 3,594 Cr
manifest.yaml: present and parses.

## SPEAR GATE
PASS. companies/DIVGIITTS.md carries: Spear HIT (Claude web, 29-Aug-2026),
entry zone ~Rs 630-715 vs CMP ~Rs 1,190. Load-bearing facts (first
verification priority, carried to every stage):
1. Q1 FY27 run rate vs Indonesia launch batch.
2. ~Rs 275 Cr net cash decline in FY26.
3. June 2026 FY25 results resubmission.
4. Sigma EV SOP in Q2 FY27 after April 2026 slip.

## FOLDER INVENTORY (by subfolder, not filename)
| Folder | Count | Notes |
|---|---|---|
| prospectus | 0 | GAP. Listed March 2023 (~3.4y). Borderline recently-listed. DRHP holds promoter/group history + restated pre-IPO financials. |
| annual-report | 1 | FY2025-26 AR (Annual Report 2025-26, 252 pp). |
| results | 2 | FY26/Q4 audited annual (ended 31-Mar-2026, filed 25-May-2026); Q1 FY27 (ended 30-Jun-2026, filed 11-Aug-2026). |
| rating | 0 | GAP. No credit rating rationale. |
| concalls | 4 | Nov 2025 (Q2 FY26), Feb 2026 (Q3 FY26), Jun 2026 (Q4/FY26), Aug 2026 (Q1 FY27). Use 3 most recent for stage 5. |
| peer-concalls | 16 | ENDURANCE, HAPPYFORGE, SANSERA (Nov/Feb/May/Aug), SONACOMS (Oct/Jan/May/Jul). 4 peers x 4 quarters. |
| announcements | 0 | GAP. No Reg 30 filings. Documented-ACTION record absent. |
| shareholding | 0 | GAP. No filed quarterly pattern. UA institutional qualifier withheld; pledge trend unavailable. |
| research | 0 | GAP (non-anchored anyway). |
| screening | 30 | screener + 4 peers x 6 CSVs each. |
| presentation | 1 | Investor_Presentation_1.pdf |
| other | 0 | - |

## DEGRADATION APPLIED (operator elected PROCEED WITH GAPS, 2026-08-29)
- No prospectus: stages 2/3 build backward history from AR alone (post-listing
  years, fewer years); FTTCP backward baseline runs post-listing only; stage 8
  sources promoter/group from web + AR governance, group map flagged web-derived.
- No announcements: stages 5/7/8 lose the documented-ACTION record; intent-and-
  action cross-check runs on concall/AR evidence only; stage 8 relies on web.
- No shareholding: stage 10 marks FII+DII unresolved; stage 11 withholds UA;
  promoter holding/pledge falls back to AR/last-known with staleness noted.
- No rating: stage 10 marks rating_wc_quote unresolved; Pillar 2 defaults
  conservative per framework; FLAG-CASH INDETERMINATE handling applies.
- No research: no effect on anchored evidence.

## NON-ANCHORED LEADS (operator-supplied, held as leads only, NOT evidence)
- Screener AI operational-update summary (late-Feb to 29-Aug-2026): AI-written
  digest, research-tier lead. Names Indonesia 4x4 ramp, AWD NexTrac order
  (19-Jun-2026, ~6,000 u/yr, 5-yr, SOP Q1 FY28), US subsidiary (Divgi
  Transmission Technologies and Systems Inc., South Carolina, Project
  Mayflower, ~USD 5m phase-1), CIO resignation (Mar 2026), Sigma EV SOP Q2 FY27.
  Stages may follow these as leads; every number must still be anchored to a
  filed input PDF.
- screener.in shareholding screenshot (Jun-2026 quarter usable): Promoters
  60.56% (flat Dec-25/Mar-26/Jun-26), FIIs 1.86%, DIIs 26.16%, Public 11.42%,
  17,929 holders. Secondary source, not the filed pattern. Sep-2025 column
  garbled (FII 81%, DII 93%), discarded. Does not close the UA qualifier at
  anchored tier.

## FRESHNESS PAIR CHECK
| # | Pair | Trigger | Mate expected | Status |
|---|---|---|---|---|
| 1 | Results -> Concall | Q1 FY27 results (ended 30-Jun-2026) | Same-quarter concall | PASS (Concall_Aug_2026 present) |
| 2 | Rating bulletin -> Rationale | none (rating/ empty) | - | NA (not triggered) |
| 3 | SEBI order -> Order text | none referenced | - | NA |
| 4 | AR -> Latest audited annual | AR FY2025-26 | Not older than latest audited annual | PASS (latest audited annual is FY26; AR is FY26) |

freshness_verdict: FRESHNESS PAIRS OK.

## HALT CHECK
manifest present and parses; inputs/ tree not empty. NO HALT. Run proceeds.

## DATA NOTE (non-halting, for phase 3)
manifest sector_cap_row = "Agri processing" is wrong for an auto driveline /
transmission components maker. Does not affect phase 1. Correct before /finalize
so the Section 1B sector cap is right.

```yaml
stage: B00-inputs
company: DIVGIITTS
run_date: 2026-08-29
model: orchestrator
status: complete
run_type: full
spear_gate: PASS
spear_hit: "HIT 2026-08-29 - entry <= Rs 715 - load-bearing facts: [Q1FY27 run rate vs Indonesia launch batch, ~Rs 275 Cr net cash decline FY26, June 2026 FY25 results resubmission, Sigma EV SOP Q2 FY27 after April 2026 slip]"
input_gaps:
  - type: prospectus
    severity: HIGH_BORDERLINE
    note: "Listed March 2023 (~3.4y). DRHP holds promoter/group history and restated pre-IPO financials."
  - type: rating
    severity: MEDIUM
    note: "No credit rating rationale; Pillar 2 cash determination defaults conservative."
  - type: announcements
    severity: MEDIUM
    note: "No Reg 30 filings; documented-ACTION record absent; intent-action cross-check on concall/AR only."
  - type: shareholding
    severity: MEDIUM
    note: "No filed pattern; UA institutional qualifier withheld; pledge trend unavailable."
  - type: research
    severity: LOW
    note: "Non-anchored anyway."
non_anchored_leads:
  - "Screener AI operational-update summary (research-tier lead only)."
  - "screener.in shareholding screenshot Jun-2026: promoter 60.56% flat, FII 1.86%, DII 26.16%, public 11.42%, 17929 holders (secondary source)."
concalls_available: true
concall_map:
  - {file: Concall_Nov_2025_Transcript.pdf, quarter: Q2FY26}
  - {file: Concall_Feb_2026_Transcript.pdf, quarter: Q3FY26}
  - {file: Concall_Jun_2026_Transcript.pdf, quarter: Q4FY26_annual}
  - {file: Concall_Aug_2026_Transcript.pdf, quarter: Q1FY27}
concalls_for_stage5: [Concall_Feb_2026_Transcript.pdf, Concall_Jun_2026_Transcript.pdf, Concall_Aug_2026_Transcript.pdf]
results_map:
  - {file: 0231a580-f6c3-4589-8c23-42498b63eba0.pdf, period: FY26_Q4_annual_audited, ended: "2026-03-31", filed: "2026-05-25"}
  - {file: ece436bc-7c30-4aa4-a843-c161d1d3c65b.pdf, period: Q1FY27, ended: "2026-06-30", filed: "2026-08-11"}
peers: [ENDURANCE, HAPPYFORGE, SANSERA, SONACOMS]
freshness_pairs:
  - {pair: results_to_concall, trigger_doc: "Q1FY27 results", mate_expected: "Q1FY27 concall", status: PASS, missing_doc: none}
  - {pair: rating_bulletin_to_rationale, trigger_doc: none, mate_expected: rationale, status: NA, missing_doc: none}
  - {pair: sebi_order_to_text, trigger_doc: none, mate_expected: order_text, status: NA, missing_doc: none}
  - {pair: ar_to_latest_audited_annual, trigger_doc: "AR FY2025-26", mate_expected: "matching-year audited annual", status: PASS, missing_doc: none}
freshness_verdict: FRESHNESS PAIRS OK
sector_cap_row_manifest: "Agri processing (WRONG - auto driveline maker; fix before /finalize)"
flags: []
analyst_note: "Operator elected PROCEED WITH GAPS after two push attempts did not reach the repo. Prospectus, rating, announcements, shareholding absent; degradation map applied. Spear HIT load-bearing facts are first verification priority."
```
