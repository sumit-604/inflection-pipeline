# Verifier D: Peer coverage audit. JLHL, run 2026-11-12

Inputs read: B06 report (outputs/reports/06-peers.md), B05 peer_questions (10), and the page-marked .txt of the 12 peer transcripts. Page numbers below are PDF pages from the "[page N]" markers.

Method. Rule 2: every SUBSTANTIVE peer was tied to at least one B06 citation re-found in the transcript text. About 30 load-bearing citations were re-read in full context. The rest were not individually re-read. Coverage of the sample is stated, not claimed as total.

## Coverage audit per peer

| Peer / call | B06 mark | Citation re-found in transcript | Result |
|---|---|---|---|
| KIMS Q3 FY26 | SUBSTANTIVE | "NABH is not a prerequisite for empanelment" and "2 of top 5 done" (p.7); Nashik "13 months to break even" (Feb file l.554); insurers "lower the price" (p.7) | Confirmed |
| KIMS Q4 FY26 | SUBSTANTIVE | debt/EBITDA "1 is to 2" (p.18, garbled wording as B06 notes) | Confirmed |
| KIMS Q1 FY27 | SUBSTANTIVE | ARPOB "too aggressive. Four to five is a good number" (p.15); Thane July Rs 21 Cr, 10% margin (p.11) | Confirmed |
| KIMS Q2 FY27 | SUBSTANTIVE | net debt Rs 2,150 Cr, ratio about 1.9 (p.18); Kakinada Rs 80 Cr for 51% (p.4); 70% occupancy in four to six years (p.14); Rs 7.8 Cr provision (p.8); PAT Rs 76 Cr vs 72 Cr | Confirmed; one page slip (finding 2) |
| MEDANTA Q3 FY26 | SUBSTANTIVE | Noida loss Rs 320 million (p.4); four or five insurance contracts signed (p.7) | Confirmed |
| MEDANTA Q4 FY26 | SUBSTANTIVE | Rs 236 million vs Rs 320 million (p.5); breakeven at 40% to 45% occupancy (p.9); 2,700 greenfield beds (p.7) | Confirmed |
| MEDANTA Q1 FY27 | SUBSTANTIVE | "very negligible to no attrition" (Pankaj Sahni); Guwahati 650 beds, Rs 9,700 million; 3,350 beds | Confirmed |
| MEDANTA Q2 FY27 | SUBSTANTIVE | EBITDA +60%, PAT +38%; Noida operating EBITDA Rs 86 million on Rs 1,059 million; Ghaziabad Rs 166 Cr land, about Rs 1,000 Cr capex (p.6); over Rs 6,000 Cr, 3,450 beds (p.7); tariff "5% or less" | Confirmed |
| YATHARTH Q3 FY26 | SUBSTANTIVE | Rs 60 lakh per bed, Rs 80-90 lakh at newer sites; 30-35% of full beds breakeven | Confirmed |
| YATHARTH Q4 FY26 | SUBSTANTIVE | Rs 75 lakh per bed Noida brownfield, "no escalation" (p.16) | Confirmed |
| YATHARTH Q1 FY27 | SUBSTANTIVE | Faridabad breakeven at 9 months vs 12-14 planned; attrition "not even 3% to 4%" (p.15); "2x of trailing 12 months EBITDA" (p.18); Rs 30.7 to 61.4 lakh; "almost a Rs 1 crore capex bed" | Confirmed |
| YATHARTH Q2 FY27 | SUBSTANTIVE | cancer drug cap, EBITDA reduction "around 0.3%" (p.7) | Confirmed |

All 12 SUBSTANTIVE marks stand. No SUBSTANTIVE peer lacks a findable citation. No fabricated figure found in the sample. Derived figures re-computed: MEDANTA Rs 1.41 / 1.45 / 1.74 Cr per bed (4,500/3,200; 4,850/3,350; 6,000/3,450) are correct.

Rule 3: no peer is marked UNUSED or CITED-ONLY, so the rule has no object. I still searched all 12 for a Q2 medical-mix ARPOB mechanism (B06 Q8 says none). One loose hit, MEDANTA Aug l.749, "slightly lower ARPOBs" on a Noida-type ramp, is not seasonal. No directly claim-relevant statement was missed.

## Verdict-discipline audit per claim

| Q | B06 verdict | Peer anchors | Audit |
|---|---|---|---|
| Q1 | VERIFIED (reset sub-part PARTIAL) | MEDANTA, YATHARTH, KIMS | Passes. Sub-part honestly split. |
| Q2 | VERIFIED | 3 peers | Passes. |
| Q3 | PARTIALLY | 3 | Passes. |
| Q4 | VERIFIED on timing | 3 | Soft. JLHL says about one year. YATHARTH's 5 months is an expectation, KIMS shows 15 to 23 months. Defensible as VERIFIED only because B06 calls the range 5-23 months. PARTIALLY would be safer. Not an upgrade from silence. |
| Q5 | PARTIALLY | 3 | Passes. |
| Q6 | PARTIALLY | 3 | Passes. |
| Q7 | VERIFIED on range and escalation | MEDANTA, YATHARTH (KIMS derived only) | Soft. The claim asks "with and without land". The split is NOT FOUND at every peer, which B06 says. Escalation has 2 independent anchors. Passes Rule 4 on the scope B06 names. |
| Q8 | PARTIALLY | 3 | Passes. |
| Q9 | PARTIALLY | 3 | Passes. |
| Q10 | PARTIALLY | 2 | Passes. |

No verdict is upgraded from silence. No VERIFIED rests on one peer. No CRITICAL.

Claims addressed: all 10 peer_questions in B05 have a Part 1 section with a verdict. `claims_all_addressed: true`.

## Findings

1. MINOR. Void MEDANTA attribution still in body and block. B06 Section 2B and the yaml `industry_cross_read.pricing_inputs` say insurers push prices down in empanelment, citing KIMS and MEDANTA. MEDANTA Q3 FY26 p.7 only says Noida ARPOB is high now and will balance as panels are added. KIMS Q3 FY26 p.7 supports it alone ("they obviously want to lower the price"). An erratum is appended to B06, but the yaml line is uncorrected, so a downstream reader of the block gets the unsupported two-peer reading. Single-peer, so it should read as KIMS-only.
2. MINOR. Page slip. B06 Part 5 cites the KIMS Rs 13.2 Cr call-option gain to KIMS Q2 FY27 p.14. The text is at p.15 (line 592, inside the p.15 span). Number is right.
3. MINOR. Q4 and Q7 VERIFIED labels are lenient, see the table. Both disclose the gap in the same row, so the cost is label strength only.

## Counts
Peers audited 12. SUBSTANTIVE confirmed 12. CRITICAL 0, MAJOR 0, MINOR 3. Acceptance rate 100% (12 of 12 peers correctly handled).

```yaml
stage: B12d
company: "JLHL"
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
  - {severity: MINOR, where: "B06 2B and yaml industry_cross_read.pricing_inputs", issue: "insurers-push-price-down attributed to KIMS and MEDANTA; MEDANTA Q3 FY26 p.7 does not say it; KIMS Q3 FY26 p.7 alone supports it; erratum appended to report but yaml uncorrected"}
  - {severity: MINOR, where: "B06 Part 5", issue: "KIMS Q2 FY27 Rs 13.2 Cr call-option gain cited p.14; text is on p.15"}
  - {severity: MINOR, where: "B06 Q4 and Q7 verdicts", issue: "VERIFIED labels lenient: Q4 peer range 5-23 months with one expectation not outcome; Q7 land vs no-land split NOT FOUND at all peers; gaps disclosed in-row, no upgrade from silence"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
