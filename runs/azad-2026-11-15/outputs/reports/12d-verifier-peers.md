# Verifier D: Peer Coverage Audit, AZAD, run 2026-11-15

Scope: 9 peer transcripts held (3 PTCIL transcripts missing, already disclosed in B06). B06 report with CAVEATS read. B05 peer_questions: 14 items.

## Coverage audit per peer

| Peer / file | B06 usage | Citations found in transcript | Unused relevant material | Result |
|---|---|---|---|---|
| MTAR Q3 (2026-02-05) | SUBSTANTIVE | 260 days [page 6] found | none found | confirmed |
| MTAR Q4 (2026-05-20) | SUBSTANTIVE | advances quote [page 13] found | none found | confirmed |
| MTAR Q1 (2026-08-06) | SUBSTANTIVE | 59 days [page 7] found | none found | confirmed |
| MTAR Q2 (2026-11-06) | SUBSTANTIVE | USD 1 Mn discounted [page 13] found; WC 50 [page 7], advances [page 11] present | MAJOR: 100-day year-end and 150-day long-term WC guidance, GST refund Rs 70-80 Cr per year ([page 10], [page 11]) | confirmed, with MAJOR miss |
| UNIMECH ACQ (2026-05-04) | SUBSTANTIVE | 93% [page 10]; wallet share [page 16] found | none found | confirmed |
| UNIMECH Q4 (2026-06-03) | SUBSTANTIVE | 120-125 days [page 7] found | none found | confirmed |
| UNIMECH Q1 (2026-08-08) | SUBSTANTIVE | 130 days [page 7]; 120-125 to 150-160 text found | none found | confirmed |
| UNIMECH Q2 (2026-10-31) | SUBSTANTIVE | equity raise [page 9]; fungible [page 13]; qualification year [page 17] found | none found | confirmed |
| PTCIL 2023 | CITED-ONLY | [page 22], [page 24], [page 28], [page 30], [page 31] used in Q2, Q7, Q8 | MAJOR: gas turbine mentions ([page 10], [page 31]); MINOR: EBITDA 26% to 29% [page 19], WC and ROE remark [page 20] | handling flawed |

No SUBSTANTIVE peer lacks a findable citation. substantive_unsupported is empty.

## Unused material detail
1. MTAR Q2, [page 10] and [page 11]. The CFO says the year ends near 100 days and the long-term goal is 150 days, because growth needs working capital. He says "if everything goes as per the same manner, we will be at 50, 60". B06 Q1 and the Part 5 hypothesis use 260 to 50 as the improvement path and never state this. A 150-day long-term peer anchor sits close to Azad's 160-180 H2 target. It matters to load-bearing fact 1. The GST refund of Rs 70-80 Cr a year is also a stated MTAR lever and parallels Azad's Rs 100 Cr GST credit.
2. PTCIL, [page 10]: "industrial gas turbines, that's another very big area that's evolving". [page 31]: for industrial gas turbines "the certification process is much, much shorter". B06 says no peer discusses gas turbine and sets FLAG-NO-GAS-TURBINE-PEER. The claim of no growth rate holds. The claim of silence does not. The shorter approval time is also relevant to Q2 (delta qualification).
3. PTCIL, [page 19]: EBITDA margin 26% to 29% (FY22 to FY23) on titanium and superalloy castings. [page 20]: analyst says working capital need is very high and ROE sub-10%. Q6 and Q1 omit these. The source is stale, so MINOR.

## Verdict-discipline audit per claim

| Q | B06 verdict | Peer anchors | Audit |
|---|---|---|---|
| Q1 | PARTIALLY VERIFIED | MTAR, Unimech | ok; see MAJOR miss above |
| Q2 | PARTIALLY VERIFIED | MTAR, Unimech, PTCIL | ok |
| Q3 | PARTIALLY VERIFIED | MTAR only | ok, one peer, not VERIFIED |
| Q4 | PARTIALLY VERIFIED | MTAR only | ok |
| Q5 | UNVERIFIABLE | none | ok; grep for take-or-pay and minimum volume finds nothing |
| Q6 | PARTIALLY VERIFIED | Unimech, MTAR | ok; PTCIL EBITDA unused (MINOR) |
| Q7 | PARTIALLY VERIFIED | Unimech, MTAR, PTCIL | ok |
| Q8 | PARTIALLY VERIFIED | PTCIL only, stale | ok, labelled weak support |
| Q9 | PARTIALLY VERIFIED | MTAR, Unimech, PTCIL | ok; "gas turbine silent" overstated |
| Q10 | UNVERIFIABLE | none | ok; grep for Sunflag, Star Wire finds nothing, steel hits are PTCIL context only |
| Q11 | VERIFIED | MTAR (debt), Unimech (equity) | ok, two independent peers |
| Q12 | PARTIALLY VERIFIED | Unimech, MTAR | MINOR: no figure quoted, under-2% unchecked; UNVERIFIABLE fits better |
| Q13 | PARTIALLY VERIFIED | MTAR, Unimech | MINOR: lift untested per B06 own text |
| Q14 | PARTIALLY VERIFIED | MTAR, PTCIL, Unimech | ok |

Only one VERIFIED, and it has two independent anchors. No verdict is upgraded from silence. Zero CRITICAL.

Claims addressed: 14 of 14 peer_questions have a verdict. Azad name search: zero hits in the peer text, consistent with B06.

## Counts
CRITICAL 0, MAJOR 2, MINOR 2. Acceptance rate 7 of 9 peers handled correctly = 78% (MTAR Q2 and PTCIL flagged).

```yaml
stage: B12d
company: "AZAD"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 9
substantive_confirmed: 8
substantive_unsupported: []
unused_but_relevant:
  - {peer: "MTARTECH (Q2 FY27)", missed_item: "MTAR says 50 days is not sustainable: year-end target about 100 days, long-term goal 150 days over 2-3 years; GST refund Rs 70-80 Cr per year is part of the lever", anchor: "MTARTECH_Concall_Transcript_2026-11-06.pdf [page 10], [page 11]"}
  - {peer: "PTCIL (Jun 2023)", missed_item: "Industrial gas turbines named as 'very big area that's evolving' and gas turbine certification 'much, much shorter' than aerospace; B06 says no peer speaks to gas turbine", anchor: "PTCIL_Concall_Transcript_2023-06-09.pdf [page 10], [page 31]"}
  - {peer: "PTCIL (Jun 2023)", missed_item: "EBITDA margin 26% to 29% FY22 to FY23; analyst: working capital requirement very high, ROE sub-10% (Q6 and Q1 left PTCIL out)", anchor: "PTCIL_Concall_Transcript_2023-06-09.pdf [page 19], [page 20]"}
claims_all_addressed: true
verdict_discipline_fails:
  - "Q12 PARTIALLY VERIFIED although no peer quotes any wallet-share figure and the under-2% claim stays unchecked (MINOR, not silence: peers spoke on wallet share qualitatively)"
  - "Q13 PARTIALLY VERIFIED although B06 says the 5-6% revenue lift is not tested; peers only place FX elsewhere (MINOR)"
findings:
  - {severity: MAJOR, item: "Q1 and Part 5 omit MTAR's own statement that 50 days is not sustainable (100 by year end, 150 long term)", anchor: "MTARTECH_Concall_Transcript_2026-11-06.pdf [page 10], [page 11]"}
  - {severity: MAJOR, item: "FLAG-NO-GAS-TURBINE-PEER and 'Gas turbine: silent' overstate; PTCIL names industrial gas turbines and shorter approvals", anchor: "PTCIL_Concall_Transcript_2023-06-09.pdf [page 10], [page 31]"}
  - {severity: MINOR, item: "PTCIL EBITDA margin trend and WC/ROE remark not used in Q6 or Q1 (stale 2023 source)", anchor: "PTCIL_Concall_Transcript_2023-06-09.pdf [page 19], [page 20]"}
  - {severity: MINOR, item: "Q12 and Q13 verdict grade is generous", anchor: "B06 Part 1 Q12, Q13"}
critical_count: 0
major_count: 2
minor_count: 2
acceptance_rate: 78
```
