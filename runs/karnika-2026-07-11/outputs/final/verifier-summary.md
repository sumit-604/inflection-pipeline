# Verifier summary (phase 1)

## Confidence delta and acceptance rates

| Component | Score | Verifier acceptance | Source |
| --- | --- | --- | --- |
| Numerical acceptance | 89.5 | 89.5% | B12a |
| Redflag coverage | 65 | 65% | B12b |
| Framework adherence | 99 | 99% | B12c |
| Peer utilisation | 75 | 83% | B12d |
| Overall | 65 | 60 to 74 band | confidence.yaml |

Notes on scope:
- Verifier A (numerical) is the source grounded re run. The first pass ran degraded (could not access source PDFs, produced 5 false CRITICALs and one arithmetic error) and is superseded; the source grounded re run governs, with 0 CRITICAL and 89.5% acceptance.
- Verifier C's valuation half is deferred to phase 3. Only the Gate 0 and Emerging Moat portions ran here (94 rules checked, one soft fail).
- REWORK not triggered: no CRITICAL, no verifier acceptance below 60.

## Findings sorted by severity

### MAJOR

| Verifier | Location anchor | Finding |
| --- | --- | --- |
| A (numerical) | 01-gate0.md, ROE FY25 | ROE stated 25.47% (AR Note 37xvii); recomputation from raw data (PAT 1,803.04L / avg equity 6,469.89L) yields 27.84%. Likely a legitimate equity basis difference (opening vs closing vs average), but the basis is not independently anchored. Clarification needed. |
| A (numerical) | 04-bizmodel.md, Revenue FY26 | FY26 consolidated revenue Rs 248 Cr not located in the Mar 2026 results pages read; standalone Rs 224.28Cr confirmed. The consolidated figure is concall / management guidance sourced (standalone Rs 224.28Cr + Kidcity ~Rs 24-25Cr). Verify against full consolidated P&L or accept as concall sourced. |
| B (redflags) | B05 concall, all sections | Fully missed MAJOR: FY26 PAT +57% and Q4 +48.6% credited as genuine delivery, but inflated by a management confirmed one time other income securities gain of about Rs 9 Cr (IT investment bought January, sold March). Caught for FY25 upstream but absent from the concall analysis that should own the FY26 disclosure. Anchor: May 2026 call p.4, p.7, p.12. |
| D (peers) | 06-peers.md Claim 7, CANTABIL Q4/FY26 | Cited Cantabil Q4 FY26 revenue +36% YoY at its own call p.3; the transcript shows +15% YoY (INR 253.5cr vs 219.8cr). The 36% belongs to MONTECARLO. Peer data mix up; the CONTRADICTED verdict survives on Cantabil's other genuine anchors, but the figure should be struck. |
| D (peers) | 06-peers.md Claim 5, MONTECARLO Q4/FY26 | Zara/Shein competitor quote cited at p.18-19; transcript is 16 pages, quote is on p.14. Content accurate, anchor as written unfindable. |

### MINOR

| Verifier | Location anchor | Finding |
| --- | --- | --- |
| B (redflags) | B05 2C/consistency | Nov CFO projection garble (contradictory Kidcity figures; FY26 repeated for FY28) not surfaced. Anchor: Nov 2025 call p.3, p.11. |
| B (redflags) | B05, not surfaced | Gross margin internally inconsistent within one May exchange: "over 150% on unit economics" vs Kidcity "28-32%". Anchor: May 2026 call p.5-6. |
| B (redflags) | B05 trigger #6 | Property integration carried as a trigger but not framed as a same call contradiction of the asset light claim. Anchor: May 2026 call p.3, p.7. |
| B (redflags) | B05/B06, not surfaced | Concall fundraise and warrant promoter dilution evasiveness not noted (owned by B08). Anchor: May 2026 call p.4, p.8. |
| B (redflags) | B05, not surfaced | Nov capacity utilisation inconsistency: CFO 80-85% vs MD 90%. Anchor: Nov 2025 call p.6, p.13. |
| C (Gate 0/EM) | 07-emoat.md C2 | C2 assigned documented (1.0) to un contracted concall stated new orders; taxonomy places at concall (0.7). em_score 18.3 to 17.7, classification MODEST unchanged. Sole soft fail of the 94 rules checked. |
| C (Gate 0/EM) | 01-gate0.md M9/M2 | Peer median drawn from a single peer (M9); Other Income basis unreconciled vs peers (M2). No score change. |
| C (Gate 0/EM) | 01-gate0.md M5/M11 | Conservative zeros where a literal top 5 (M5) or trend read (M11) was arguable. Moats present count and STRONG class unaffected. |
| C (Gate 0/EM) | 07-emoat.md F2 | F2 built from transcripts because the B05 promise delivery record was not injected at that stage. Disclosed, reasonable substitution, no score impact. |
| C (Gate 0/EM) | 07-emoat.md 6D | Combined classification reasoned without the injected Master v3.3 matrix. Disclosed; AVERAGE stands. |
| D (peers) | 06-peers.md Claim 2, CANTABIL Q4/FY26 | CFO quote "some input material has seen some hike" cited at p.10; actual p.5. Verbatim accurate, page wrong. |
| D (peers) | 06-peers.md Claim 6, CANTABIL Q4/FY26 | Gross margin 60.4% FY26 vs 56.2% FY24 bundled under p.3; actual p.9. EBITDA margin at p.3 correctly anchored. |
| D (peers) | 06-peers.md Part 2A, CANTABIL Q3 FY26 | GST momentum quote cited at p.10; actual p.6. Verbatim accurate, page wrong. |
| D (peers) | 06-peers.md Claim 3, MONTECARLO Q2 FY26 | "We dropped that idea" quote cited at p.10; actual p.9. Verbatim accurate, page wrong. |

### CRITICAL

None across all four verifiers.

## Counts

- Verifier A: 0 CRITICAL, 2 MAJOR, 0 MINOR (38 numbers checked; source grounded re run).
- Verifier B: 0 CRITICAL, 1 MAJOR, 5 MINOR (20 independent flags found, 13 fully caught, 4 partial).
- Verifier C: 0 CRITICAL, 0 MAJOR, 5 MINOR (Gate 0 + Emerging Moat; valuation deferred to phase 3).
- Verifier D: 0 CRITICAL, 2 MAJOR, 4 MINOR (12 peers audited, 9 substantive confirmed).
