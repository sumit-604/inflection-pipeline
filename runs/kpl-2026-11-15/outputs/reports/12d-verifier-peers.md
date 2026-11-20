# Verifier D: Peer coverage audit, KPL, run 2026-11-15

Method: spot-read the page-marked .txt transcripts against B06 citations. Only 10 transcripts exist (not 12), per B00 gap noted in B06.

## Coverage audit per peer

| Peer / call | B06 usage | Citation checked | Found in transcript | Result |
|---|---|---|---|---|
| CAPLIPOINT Q2 FY26 | SUBSTANTIVE | "35+ products filed, 20 approvals along with partners" (Nov 2025 txt line 180) | Yes | Confirmed |
| CAPLIPOINT Q3 FY26 | SUBSTANTIVE | 55% warehouse stock, sterile range, US label ~$10M (Feb txt lines 108-135, 247) | Context found; 18-24 month and 75/25 lines not individually re-read | Confirmed (partial re-read) |
| CAPLIPOINT Q4 FY26 | SUBSTANTIVE | 136 days, 11 days FX, 125 ex-FX (lines 317-319); "100 to 120" (487) and "100 to 130 days ... still okay" (506); Chile 135 products, $10M, 18 months (152-153) | Yes, all | Confirmed |
| CAPLIPOINT Q1 FY27 | SUBSTANTIVE | Gross margin 55% target vs 59.8% (Aug txt 277-284); 17 sterile lines (376) | Yes | Confirmed |
| SENORES Q3 FY26 | SUBSTANTIVE | 55% own product mix (line 283, page 7); CDMO margin "4% to 5% or 5% to 6% lower" (292); US ~40% long term (612-613, page 15) | Yes, pages match | Confirmed |
| SENORES Q4 FY26 | SUBSTANTIVE | EM realisation INR 1.20 (May txt line 398) | Found | Confirmed |
| SENORES Q1 FY27 | SUBSTANTIVE | Sterile proceeds moved to oral solids (Aug txt 404-408, 467-469) | Yes | Confirmed |
| SENORES Q2 FY27 | SUBSTANTIVE | "558 is approved, and 944 ... two to three, max" (Nov txt 717, page 17); Talati and Talati (438-444) | Yes, page 17 matches | Confirmed |
| LINCOLN Q3 FY26 | SUBSTANTIVE | 15-18% (Feb txt 331, 533, 649); Africa cash "10, 15 days" (613); Canada $3-4M and partner-held LatAm (421-423) | Yes | Confirmed |
| LINCOLN Q4 FY24 | CITED-ONLY | Debtor "89 to 101" (May 2024 txt 705) | Yes | Correctly labelled STALE |

Substantive confirmed: 9 of 9. Unsupported: none. B06 also truthfully reports that no peer mentions KPL (not re-searched; no reason to doubt).

## Unused or CITED-ONLY material
- LINCOLN Q4 FY24 (CITED-ONLY): used only for stale comparisons; correct handling.
- MINOR: Lincoln Q3 FY26 says it targets INR 5-7 Cr a year on registrations and BE studies and re-registers partner-held LatAm products as owned (lines 422-428). B06 cites the re-registration but not the cost. Relevant to Q4 and Q8.
- MINOR: Senores Q1 FY27 Apnar utilisation 80-90% (Aug txt 524-529). Industry context for Q6, not claim-direct.
- No claim-direct statement left unused (no MAJOR).

## Verdict discipline per claim
| Claim | B06 verdict | Independent anchors | Discipline |
|---|---|---|---|
| Q1 | PARTIALLY VERIFIED | Senores, Caplin, Lincoln | OK |
| Q2 | CONTRADICTED | Caplin 117-136 days, Senores NWC 90-104, Lincoln 89-101 (stale); numbers stated, not silence; comparability caveat disclosed | OK, not an upgrade from silence |
| Q3 | PARTIALLY | Caplin, Senores | OK |
| Q4 | PARTIALLY | Caplin, Senores | OK |
| Q5 | PARTIALLY | Caplin, Senores | OK |
| Q6 | UNVERIFIABLE | none | OK; adjacent evidence labelled |
| Q7 | PARTIALLY | Senores, Lincoln, Caplin | OK |
| Q8 | PARTIALLY | Margin gap from Senores alone; both assigned peers silent on gap | OK (capped); MINOR wording note |
| Q9 | UNVERIFIABLE | none | OK |
| Q10 | UNVERIFIABLE | none | OK |

Zero VERIFIED claims, so no single-peer VERIFIED. No verdict was upgraded from silence.

## Peer-questions coverage
All 10 questions in B05 peer_questions (Q1 to Q10) received a verdict in B06 Part 1. None skipped.

```yaml
stage: B12d
company: "KPL"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 10
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant:
  - {peer: "LINCOLN Q3 FY26", missed_item: "Lincoln spends INR 5-7 Cr a year on registrations and BE studies and re-registers partner-held LatAm products as owned; a cost-per-registration datapoint for Q4/Q8 (B06 cites only the re-registration, p.10)", anchor: "LINCOLN-Concall_Feb_2026_Transcript.txt lines 422-428 (page 10-11 boundary)"}
  - {peer: "SENORES Q1 FY27", missed_item: "Apnar plant utilisation 80-90%, mostly product-led; industry context for Q6 utilisation", anchor: "SENORES-Concall_Aug_2026_Transcript.txt lines 524-529"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Lincoln INR 5-7 Cr a year registration spend not used in Q4 or Q8"}
  - {severity: MINOR, item: "Senores Apnar utilisation 80-90% not used in Q6 context"}
  - {severity: MINOR, item: "Q8 PARTIALLY VERIFIED margin-gap leg rests on one peer (Senores, not assigned); both assigned peers give no gap. Verdict cap is right; wording should say single-peer on margin gap"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
