# Verifier D: Peer Coverage Audit. SUPREMEPWR. Run date 2026-10-06

Inputs read: 06-peers.md (B06), B05 peer_questions (11 questions), peer transcripts (txt beside PDFs). Spot-checks were by text search of the transcripts. Scope note: the instruction file says 12 transcripts; the corpus holds six (Shilchar 4, Danish 2) plus INDOTECH with none.

## Coverage audit table per peer

| Peer / call | B06 usage | Citations located in transcript | Result |
|---|---|---|---|
| Shilchar Q4 FY25 (Apr-2025) | SUBSTANTIVE | Confirmed: "backward integration is not required at all ... never face any shortage" (file p.9-10); "lead time still remains the same" with analyst "1.5, 2 years" (p.15-16); premium "1%, 2%, 3% maximum" | Confirmed |
| Shilchar Q2 FY26 (Oct-2025) | SUBSTANTIVE | Confirmed: "no bottleneck in terms of sourcing any materials" (p.5); "5, 10 years" (p.9); "at least five to 6 years" (p.11); "about 22 weeks" (file p.16) | Confirmed |
| Shilchar Q4 FY26 (May-2026) | SUBSTANTIVE | Confirmed: "12 to 16 weeks" (p.7); "some orders ... based on the PV clause" (file p.16, B06 says 15); "Now it has come down to 10%" (p.16); Yash Highvoltage bushing supplier | Confirmed |
| Shilchar Q1 FY27 (Aug-2026) | SUBSTANTIVE | Confirmed: "50-60% of the price rise" (p.5); "10 to 12 weeks or even 16 weeks" (p.8) | Confirmed |
| Danish H1 FY26 (Nov-2025) | SUBSTANTIVE | Confirmed: "at least 3-5 years" (line 340); "6-8 weeks as a minimum" (line 568); analyst "Shilchar ... around 30%" margin context | Confirmed |
| Danish H2 FY26 (May-2026) | SUBSTANTIVE | Confirmed: "around 30% of the orders should be on price variation" (file p.9, B06 says p.8); "product type ... does not determine the margin ... myth has to go away" (file p.13, B06 says p.12); "five to seven years" (p.3); "INR20+crores" (p.3) | Confirmed |
| INDOTECH | UNUSED | No transcripts in corpus. B06 correctly states the input gap and does not cite it | Correctly handled |

Peers audited: 3 (Shilchar, Danish, INDOTECH). Substantive peers confirmed: 2 (6 of 6 peer-calls). SPEL name search: B06 reports zero hits; not re-run beyond the searches above, none found.

## Verdict-discipline audit per claim

| Claim | B06 verdict | Independent peer anchors | Audit |
|---|---|---|---|
| Q1a demand 5-10 yr | VERIFIED | Shilchar and Danish, 4+ anchors | Two peers anchor, so the rule passes. Calibration: peers state 3-7 years; the 10-year end rests on one passing Shilchar line about product focus (p.9). B06 says so in its own net read, so PARTIALLY VERIFIED fits better. MINOR |
| Q1b lead time 12-24 mo | CONTRADICTED | Shilchar, Danish | The peer lead times (10-22 weeks) are IDT makers' own niche, and Shilchar Apr-2025 supports the 1.5-2 year industry norm. CONTRADICTED is stronger than the evidence; "not comparable / PARTIALLY" fits. B06 does disclose both readings. MINOR (not an upgrade from silence) |
| Q2 ramp | PARTIALLY | both | Sound |
| Q3a PVC | CONTRADICTED as common | Danish 30% (verified), Shilchar "some" (verified) | Sound |
| Q3b margin dip | PARTIALLY | both | Sound |
| Q4 CRGO/bushing | VERIFIED | CRGO: Shilchar plus Danish; bushing: Shilchar only | Two anchors on CRGO. Peer CRGO evidence dates Oct-Nov 2025, before SPEL's Feb-2026 statement; B06 notes the 2026 risk moved to oil/copper. Acceptable |
| Q5 220 kV | PARTIALLY | both | Sound; NOT FOUND stated for CPRI and cost |
| Q6 MVA mix | CONTRADICTED gross gain | Danish plus Shilchar Q1 FY27; counter Shilchar Q2 FY26 disclosed | Sound |
| Q7 data centre | PARTIALLY | both | Sound |
| Q8 labour | PARTIALLY | Danish only | Single peer, correctly not VERIFIED |
| Q9 tank factory | PARTIALLY | Danish plus Shilchar contrary | Sound |
| Q10 receivables | PARTIALLY | both | Sound, but see unused item |
| Q11 US duty | PARTIALLY | both | Sound |

No VERIFIED rests on one peer. No verdict upgraded from silence: silent items are marked NOT FOUND (CPRI, prototype cost, wage data, receivable days). Verdict-discipline fails: none at MAJOR or CRITICAL.

## Peer_questions coverage
All 11 B05 questions have a verdict (Q1 and Q3 split into two lines each, 13 lines). claims_all_addressed: true.

## Unused but relevant (rule 3)
1. Shilchar Q1 FY27 (Aug-2026, Alay Shah, file p.8 area, line 122): "we won't be doing any business with any state utility companies". This bears on Q10 (government receivables) and on SPEL's 30.10% government exposure. B06 Q10 says neither peer reports government receivable days and cites only Danish's 10% government share. A claim-adjacent peer statement, not a days figure. MINOR.
2. Stale export mix: B06 comparability note says Shilchar exports "about 50% of revenue" (Oct-2025 call p.8). Later calls say about 30% of FY26 revenue (May-2026, line 262) and order book 30% export/70% domestic (Aug-2026, line 110). Context only. MINOR.

## Anchor hygiene
B06 states the convention "file marker N". Danish May-2026 anchors p.8 and p.12 sit on file markers p.9 and p.13; Shilchar May-2026 PV and Oct-2025 22 weeks sit one page high on printed numbering (file p.16). All items are findable on the adjacent page. MINOR (one finding).

## Findings
- MINOR: Q1a VERIFIED overstated against the 10-year end of the claim.
- MINOR: Q1b CONTRADICTED rests on IDT niche lead times; comparability caveat is present but verdict is firm.
- MINOR: Shilchar state-utility avoidance not used in Q10.
- MINOR: Shilchar export share stated at 50% (Oct-2025) when later calls give about 30%.
- MINOR: page anchors off by one in several places.

Counts: critical 0, major 0, minor 5. Acceptance: 3 of 3 peers correctly handled (100%).

```yaml
stage: B12d
company: "SUPREMEPWR"
run_date: "2026-10-06"
model: claude-sonnet-5-5
status: complete
peers_audited: 3
substantive_confirmed: 2
substantive_unsupported: []
unused_but_relevant:
  - {peer: "SHILCHAR", missed_item: "Will not do business with any state utility companies (relevant to Q10 government receivables and SPEL's 30.10% government share)", anchor: "531201-Concall_Aug_2026_Transcript line 122, Alay Shah"}
  - {peer: "SHILCHAR", missed_item: "Export mix stated as about 50% in comparability note; later calls give about 30% of FY26 revenue and 30/70 order book (context only)", anchor: "531201-Concall_May_2026 line 262; Aug_2026 line 110"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, finding: "Q1a VERIFIED overstated: peers state 3-7 years, 10-year end rests on one passing line (Oct-2025 p.9)"}
  - {severity: MINOR, finding: "Q1b CONTRADICTED rests on IDT-niche lead times of 10-22 weeks; Shilchar Apr-2025 supports 1.5-2 year industry norm; comparability caveat present"}
  - {severity: MINOR, finding: "Shilchar state-utility avoidance (Aug-2026) not used in Q10"}
  - {severity: MINOR, finding: "Shilchar export share cited at 50% (Oct-2025) while later calls say about 30%"}
  - {severity: MINOR, finding: "Page anchors off by one in several B06 citations (Danish May-2026 p.8, p.12; Shilchar May-2026 PV p.15); all findable on adjacent page"}
critical_count: 0
major_count: 0
minor_count: 5
acceptance_rate: 100
```
