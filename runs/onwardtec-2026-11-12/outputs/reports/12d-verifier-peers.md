# Verifier D: peer coverage audit, ONWARDTEC, 2026-11-12

Method: read B06 report and block, B05 peer_questions (11), then grepped the page-marked .txt files and matched each SUBSTANTIVE citation to its quote and page marker. Not every B06 figure was re-read; a sample of load-bearing ones was.

## Coverage audit per peer (B06 Part 3)

| Peer / call | B06 usage | Check | Result |
|---|---|---|---|
| LTTS Q3 FY26 (Jan) | SUBSTANTIVE | DSO 112 (.txt l.334), offshore 54.6% and T&M 61.4% (l.370-371), data-centre and energy build-up (l.413) all found | Confirmed |
| LTTS Q1 FY27 (Jul) | SUBSTANTIVE | DSO 77 vs 83, guide 80-85 (l.338-340); "pass on some productivity improvement" (l.586); "Nobody has ever come back and say reduce your rates" (l.555); data centres upside (l.449) | Confirmed |
| LTTS Q2 FY27 (Oct) | SUBSTANTIVE | Data Center Engineering line (l.225, page 6); EBIT 16.3%, revenue Rs 3,040 Cr, offshore 55.9%, headcount 24,035, attrition 14.7%, DSO 78 (60/18); "Auto Europe has been in a problem" (l.426, page 11) | Confirmed |
| TATATECH Q3 FY26 (Jan) | CITED-ONLY | DSO 111 vs 109 (l.459-461); wage-hit margin 14.1% (l.188); attrition up (l.490) | Handling correct; see minor 2 |
| TATATECH Q4 FY26 (May) | CITED-ONLY | DSO 95 vs 111, billed 59, unbilled 36 (l.477-481) | Confirmed |
| TATATECH Q1 FY27 (Jul) | SUBSTANTIVE | DSO 97, billed 65, unbilled 32 (l.447-450); "force multiplier" (l.641); "singing quite a different tune" (l.576); aerospace CAGR about 40% (l.749) | Confirmed |
| TATATECH Q2 FY27 (Oct) | SUBSTANTIVE | EBITDA 16.1% after 100 bps headwind (l.128-129); attrition 15.6% (l.135-136); 316 net adds, 12,895 (l.444-446); DSO 102, 63/39 (l.425-428, page 12); VW cut (l.719, page 20) | Confirmed |
| CYIENT Q4 FY26 (Apr) | SUBSTANTIVE | EBIT 12.4% (l.208, l.294); FY26 12.2%, 67 bps down, merit increases (l.325-326); price increases (l.200) | Confirmed. Note: "12.4%" at l.238 is the strategic-unit decline, not margin; B06 did not confuse them |
| CYIENT Q1 FY27 (Aug) | SUBSTANTIVE | DET -0.5% QoQ, -0.9% YoY cc, Rs 1,540 Cr (l.304-306); EBIT 13.2% (l.225); 15% goal "H1 next year" (l.473); FCF Rs 114 Cr, 80.5% (l.330); wage hike decision (l.475) | Confirmed |
| CYIENT TAO event (Jun) | CITED-ONLY | Rev/employee $33-34k (l.375, page 9); outcome-based models (l.165, page 5); top 10 about 60% (l.577, page 14); AI data centre energy OEMs (l.517, page 12) | Confirmed. Underuse not material |
| CYIENT semiconductor event (26 May) | UNUSED | Read pages 1-6. No margin, working-capital or T&M content. Contains data-centre power demand (p.3-4) | UNUSED holds for claim list; industry-context miss, MINOR |

SUBSTANTIVE count: 7 of 7 have real, findable citations in B06 Parts 1-2. substantive_unsupported: none.

## Verdict-discipline audit per claim

| Q | B06 verdict | Independent anchors | Discipline |
|---|---|---|---|
| Q1 data-centre pull | PARTIALLY | LTTS across 3 calls plus Cyient mention | Correct. Cyient's mention is only theme-level, so not VERIFIED |
| Q2 budgets / Europe | PARTIALLY (Europe cuts VERIFIED) | Tata and LTTS on Europe | Correct, 2 peers for sub-claim |
| Q3 work permit | UNVERIFIABLE | none | Correct. My keyword search of all 11 .txt for H-1B, visa, work permit found nothing relevant |
| Q4 AI / T&M pressure | PARTIALLY | LTTS admits; Tata and Cyient do not | Correct |
| Q5 margin | PARTIALLY | 3 peers, bases differ | Correct |
| Q6 rev per employee | PARTIALLY, derived | derived only | Correct and labelled own arithmetic |
| Q7 DSO | VERIFIED | Tata, LTTS (Cyient silent) | 2 independent peers; passes. Range stated 78-102 omits 111-112 (minor 2) |
| Q8 top-5/10 | UNVERIFIABLE | none | Correct; keyword check agrees |
| Q9 R&D credit | UNVERIFIABLE | none | Correct; keyword check found no credit mention |
| Q10 wage / attrition | VERIFIED (lateral hiring NOT FOUND) | Tata, LTTS, Cyient | 3 peers; passes |
| Q11 fastest growth | CONTRADICTED (weak) | Tata +22.2% vs Onward 17.5% | Properly hedged; no upgrade from silence |

No VERIFIED rests on one peer. No verdict is upgraded from silence. All 11 peer_questions received a verdict (claims_all_addressed: true).

## Findings
- MINOR: semiconductor event call called content-free; it has data-centre power statements (CYIENT Jun_2, p.3-4). Industry context only.
- MINOR: Q7 peer DSO range 78-102 understated against B06's own 111-112 readings.
- MINOR: Tata Tech Q3/Q4 FY26 anchors lack page numbers (disclosed in B06 stage notes).

Acceptance: 11 of 11 peers correctly handled (100%).

```yaml
stage: B12d
company: "ONWARDTEC"
run_date: "2026-11-12"
model: claude-sonnet-5-5
status: complete
peers_audited: 11
substantive_confirmed: 7
substantive_unsupported: []
unused_but_relevant:
  - {peer: "CYIENT", missed_item: "Semiconductor event call (26 May 2026): data-centre power as the biggest bottleneck, share of data-centre power 2% to 8% by 2030, HVDC patents for AI data centres. B06 says no ER&D demand content. Industry-context only, semiconductor products not engineering services.", anchor: "CYIENT-Concall_Jun_2026_Transcript_2, PDF p.3-4"}
  - {peer: "TATATECH", missed_item: "Q3 FY26 call (Jan 2026): DSO 111 vs 109 in Q2 and Q4 FY26 recovery from 111 to 95. B06 net read quotes a 78-102 day peer DSO range, which omits these 111-112 day readings.", anchor: "TATATECH-Concall_Jan_2026_Transcript, .txt lines 459-464 (page not cited by B06)"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "Cyient 26 May semiconductor call marked UNUSED with 'no ER&D demand content found'; it carries data-centre power demand statements at PDF p.3-4 (industry context for Q1)"}
  - {severity: MINOR, item: "Q7 net read states peer DSO range 78-102 days, but B06 evidence itself lists LTTS 112 (Q3 FY26) and Tata Tech 111 (Dec 2025); range understated, verdict VERIFIED unaffected"}
  - {severity: MINOR, item: "Tata Tech Q3 FY26 and Q4 FY26 anchors cited by call, not PDF page (B06 stage notes admit this); not findable by page"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
