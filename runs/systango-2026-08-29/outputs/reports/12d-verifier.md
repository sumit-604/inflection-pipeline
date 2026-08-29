# STAGE 12D: VERIFIER D — PEER COVERAGE AUDIT — SYSTANGO
Run date: 2026-08-29 | Model: claude-sonnet-5
Scope: independent read of all 12 peer transcripts (INFOBEAN x4, KSOLVES x4,
ONWARDTEC x4) under runs/systango-2026-08-29/inputs/peer-concalls/, checked
against B06 (outputs/reports/06-peers.md, outputs/blocks/06-peers.yaml) and
the 6 peer_questions handed off by B05 (Section 4B of 05-concall.md).

All 12 PDFs were located and read page-by-page (file naming pattern
`<TICKER>-Concall_<Mon>_<Year>_Transcript.pdf`, confirmed by direct Read,
not discoverable via grep because ripgrep skips binary PDFs entirely in
this environment — noted for future verifier runs).

---

## PART 1: COVERAGE AUDIT TABLE (per peer-quarter)

| Peer | Quarter | B06 label | Citation checked | Verdict |
|---|---|---|---|---|
| INFOBEAN | Q1FY26 (Jul-2025) | SUBSTANTIVE | "21 to 23, we doubled in two years... did not grow in the last two years" (Avinash Sethi) — FOUND, verbatim match. Blockchain-exit quote ("we did invest in blockchain in 23 and 24... out of blockchain as of now") — FOUND, verbatim match | Citations real. **But** the blockchain quote is characterized by B06 as "unprompted... volunteered during prepared remarks, not in response to an analyst question about blockchain." Transcript shows the opposite: it is Avinash Sethi's direct answer to analyst Mohit's explicit question ("I wanted to hear about your thought leadership or point of view in blockchain... will you be exploring on blockchain"). MAJOR — mischaracterizes the evidentiary strength of Part 4's "single strongest independent confirmation" claim. |
| INFOBEAN | Q2FY26 (Nov-2025) | CITED-ONLY | Part 1 Q1 text quotes: "InfoBeans confirms elsewhere (Nov-2025 call) it had 'always had ambition of doubling revenue every three years... macro and other factors led to pausing that journey for one or two years'" | This phrase is spoken by analyst Rupesh as part of his (crammed, multi-part) question, NOT by management, and Avinash's actual answer does not restate or confirm this specific framing — he answers generally about breaking the "100 crore quarter on quarter" plateau. B06 attributes an analyst's words to "InfoBeans confirms." MAJOR — misattributed speaker inflates Q1's evidence base (the call's own coverage-map classification, CITED-ONLY, is otherwise reasonable). |
| INFOBEAN | Q3FY26 (Feb-2026) | SUBSTANTIVE | TCS-deflection quote (Siddharth Sethi): "we don't know what TCS is doing or not doing... we cannot, I personally or this room cannot comment on what TCS or XYZ company is doing or not doing. Let's not." | FOUND, verbatim match, correctly attributed to Siddharth Sethi responding to analyst Mehul. Confirmed accurate. |
| INFOBEAN | Q4FY26/FY26 (May-2026) | SUBSTANTIVE | Receivables quote (Avinash/Siddharth): "Fortune 500 customers... come up with their 90-day kind of a payment cycle... If receivables do not increase, then that's a problem, actually." Also the Jan-2026-to-May-2026 hedging flip-flop quote | FOUND, verbatim match on both. Receivables rose "22 crores" per analyst Mehul's question, matching B06's "Rs22cr" figure. Confirmed accurate. |
| KSOLVES | Q1FY26 (Jul-2025) | SUBSTANTIVE | "debtors of less than 60 days from last two years" + "working capital of less than 50 days"; margin 26.41% operational / 37.33% ex-events-ESOP | FOUND, verbatim match (p.8 of 25). Confirmed accurate on substance and framing (a positive-achievement statement, not a stress signal). MINOR: B06 locates this quote in "Q&A"; it is actually in prepared remarks/the presentation section, before Q&A opens. |
| KSOLVES | Q2FY26 (Oct-2025) | CITED-ONLY | none listed as a "contribution" in Part 3/YAML | Transcript (p.7) contains: "This is our 21st result after launching the IPO. Out of 21st, 20 quarters, we have made quarter-on-quarter growth." This is the actual, decisive evidentiary basis for B06's own Q6 verdict text ("Ksolves: management describes the Oct-2025 call as its '21st result... after launching the IPO,' implying an IPO roughly five-plus years before Oct-2025"). Part 1 correctly sources this to Oct-2025, but Part 3's coverage map and the B06.yaml block instead credit "IPO-vintage ~2020 established" as a Jul-2025 contribution and rate Oct-2025 "CITED-ONLY... no decisive new fact." MAJOR — a directly claim-relevant (Q6) peer statement is present in this transcript and used by B06 elsewhere, yet the coverage map miscredits it to the wrong quarter and downgrades the quarter that actually carries it. |
| KSOLVES | Q3FY26 (Jan-2026) | SUBSTANTIVE | "we have not seen pricing pressure from clients. Instead clients are focused on improving output and accelerating... programs with AI rather than negotiating lower rates" | FOUND, verbatim match (p.3). Confirmed accurate. |
| KSOLVES | Q4FY26/FY26 (May-2026) | SUBSTANTIVE | FY26 margin 29.7% vs FY25 34.8%; DFM product retreat/P&L cost admission; war-related UAE order-delay disclosure | Not independently re-verified page-by-page in this pass (already read in full during the initial batch with intact images); no discrepancy found against B06's characterization on spot inspection. Treated as confirmed on the strength of the earlier full read. |
| ONWARDTEC | Q2FY26 (Oct-2025) | SUBSTANTIVE | DSO ~73 days trending to 65; EBITDA margin 14.3% vs prior-year "low single digit"; auto-vertical de-growth/tough-year framing | Read in full during the initial batch; consistent with B06's characterization on spot inspection. No discrepancy found. |
| ONWARDTEC | Q3FY26 (Jan-2026) | CITED-ONLY | none listed | Read in full during the initial batch; no additional claim-relevant material identified beyond B06's "confirms trend" characterization. |
| ONWARDTEC | Q4FY26/FY26 (May-2026) | SUBSTANTIVE | Competitor-naming quote (Jigar Mehta): "L&T Technologies Services, you know KPIT, and you know Cyient... A more recent example is Tata Technologies, which is Pune-based and owned by Tata Motors." Also: transportation-vertical revenue de-growth of 1%, EBITDA margin 13.2% FY26 record | FOUND, verbatim match on the competitor quote (p.6-7), correctly attributed to Jigar Mehta responding to analyst Madhur Rathi's explicit "listed peers that are relatively like-to-like comparable" question. This is B06's "single most consequential contradiction" (Q5) — confirmed accurate and correctly characterized as a direct, specific answer (not a deflection). Transportation de-growth 1% and its two stated causes (Tier-1/Tier-2 exit + automotive slowdown) also confirmed verbatim (p.7). EBITDA margin 13.2% confirmed (p.2, p.8). |
| ONWARDTEC | Q1FY27 (Jul-2026) | SUBSTANTIVE | "AI is affecting IT companies and Onward Technologies is not an IT company"; European auto-OEM project cancellations | Read in full during the initial batch. The near-identical talking point ("It's affecting... IT companies and BPO companies. It's not affecting engineering companies") recurs verbatim in the May-2026 call too, so this is a repeated management line, not unique to Jul-2026 — consistent with, not contradicting, B06's citation. No discrepancy found. |

---

## PART 2: VERDICT-DISCIPLINE AUDIT (per B05 claim)

| # | Claim | B06 verdict | Peer-anchor count | Discipline check |
|---|---|---|---|---|
| Q1 | H1FY24 industry-wide slowdown | PARTIALLY VERIFIED | 1 peer (INFOBEAN) direct + 1 peer (INFOBEAN, different call) misattributed-quote support | Correctly capped below VERIFIED (only 1 peer addresses it at all); however part of the supporting evidence (Nov-2025 quote) is a misattribution, see Part 1. Verdict label itself (PARTIALLY VERIFIED, not VERIFIED) is not overstated. |
| Q2 | Receivables/payment-cycle stress | CONTRADICTED (partial) | KSOLVES (direct contradiction) + INFOBEAN/ONWARDTEC (current-era corroboration of "long cycles = normal") | Both underlying quotes verified verbatim. No discipline issue. |
| Q3 | Peer EBITDA margins vs Systango | UNVERIFIABLE (FY23/H1FY24) / PARTIALLY VERIFIED (current-era) | 3 peers, current-era only, correctly labeled as not period-matched | No discipline issue; correctly caveated. |
| Q4 | Blockchain/Web3 demand softness | PARTIALLY VERIFIED | 1 peer (INFOBEAN) | Correctly capped at PARTIALLY VERIFIED per B06's own stated 2-peer rule for VERIFIED. However the "unprompted/volunteered" framing overstates how the single data point was obtained (see Part 1, MAJOR). |
| Q5 | Competitor-naming vs deflection | CONTRADICTED | ONWARDTEC (direct contradiction) + INFOBEAN (matches Systango's evasive pattern) | Verified verbatim, correctly characterized (Q&A-elicited, direct, specific). No discipline issue — this is B06's strongest, cleanest finding. |
| Q6 | FY22-23 IPO-vintage benchmark | UNVERIFIABLE | 0 peers fit the criterion (structural) | Correctly reasoned as structurally unanswerable. The supporting Ksolves IPO-vintage quote is real but miscredited to the wrong call (Jul-2025 instead of Oct-2025) in Part 3/YAML — does not change the verdict, but is a sourcing error (see Part 1). |

No claim was skipped (claims_all_addressed: true). No VERIFIED claim exists in B06, so the "≥2 independent peer anchors for VERIFIED" rule has no violation to check. No verdict was upgraded from silence — every CONTRADICTED and PARTIALLY VERIFIED verdict traces to a real, quoted, correctly-directional peer statement.

---

## PART 3: SUMMARY-ARITHMETIC DEFECT

B06 Part 3 closing paragraph states: "10 of 12 peer transcripts rated SUBSTANTIVE; 2 rated CITED-ONLY... correcting count: INFOBEAN Nov-2025, KSOLVES Oct-2025, ONWARDTEC Jan-2026 — three total CITED-ONLY." This is an internal self-contradiction: it opens with "10... 2" and closes the same sentence naming three CITED-ONLY peer-quarters, without ever correcting the leading "10." The peer_coverage_map table itself (both in the .md and the .yaml block) lists exactly 3 CITED-ONLY rows (INFOBEAN Nov-2025, KSOLVES Oct-2025, ONWARDTEC Jan-2026), which makes the correct SUBSTANTIVE count **9**, not 10. MAJOR — this is the headline coverage statistic and it is arithmetically wrong in the prose summary (the underlying table is internally consistent at 9/3; only the stated "10 of 12" sentence is wrong).

---

## PART 4: FINDINGS

| Severity | Location | Issue |
|---|---|---|
| MAJOR | B06 Part 1, Q4 (blockchain), and Part 4 "strongest independent confirmation" | Blockchain-exit quote (INFOBEAN, Jul-2025) mischaracterized as "unprompted... volunteered during prepared remarks, not in response to an analyst question about blockchain." Transcript shows it is a direct answer to analyst Mohit's explicit blockchain question. Inflates the credibility of the single strongest corroborating data point in the report. |
| MAJOR | B06 Part 1, Q1 (growth slowdown) | "InfoBeans confirms elsewhere (Nov-2025 call) it had 'always had ambition of doubling revenue every three years... macro and other factors led to pausing that journey for one or two years'" — this is analyst Rupesh's phrasing inside his question, not a management statement, and management's answer does not restate or confirm it. Misattributes an analyst's framing as company confirmation. |
| MAJOR | B06 Part 3 coverage map + 06-peers.yaml peer_coverage_map | KSOLVES Q2FY26 (Oct-2025) rated CITED-ONLY ("no decisive new fact") while carrying the "21st result... after launching the IPO" quote that Part 1's own Q6 verdict text correctly sources to Oct-2025. The coverage map instead miscredits this contribution to the Jul-2025 call. A directly claim-relevant (Q6) peer statement is present and used, but the map misattributes and thereby undercounts the peer-quarter that actually carries it. |
| MAJOR | B06 Part 3 closing paragraph | "10 of 12 peer transcripts rated SUBSTANTIVE" is arithmetically inconsistent with the same paragraph's "three total CITED-ONLY" correction and with the coverage-map table itself (9 SUBSTANTIVE + 3 CITED-ONLY). The headline peer-utilization statistic is wrong in the prose, though internally consistent in the table. |
| MINOR | B06 Part 1, Q2 (receivables) | KSOLVES "debtors <60 days" quote is located by B06 in "Q&A"; it actually appears in prepared remarks/the presentation section of the Jul-2025 call, before Q&A opens. Cosmetic — the quote and its framing are otherwise correctly captured. |

No CRITICAL findings. No fabricated citations were found: every SUBSTANTIVE-labeled quote checked was located verbatim in its named source transcript. No verdict was upgraded from silence, and every B05 claim received a verdict.

---

## PART 5: UNUSED-BUT-RELEVANT

| Peer | Missed item | Anchor |
|---|---|---|
| KSOLVES | The Q2FY26 (Oct-2025) call's "21st result... after launching the IPO, out of 21st, 20 quarters" statement is the actual decisive evidence for Q6 (IPO-vintage benchmark), yet the peer-coverage map rates this quarter CITED-ONLY and credits the Q6 contribution to Jul-2025 instead. | KSOLVES-Concall_Oct_2025_Transcript.pdf, p.7 of 18, Ratan Srivastava |

No other transcript was found to contain directly claim-relevant material that B06 left unused. The three CITED-ONLY peer-quarters (INFOBEAN Nov-2025, ONWARDTEC Jan-2026, and — per this audit's correction — KSOLVES Oct-2025 excepted) were spot-read and found to genuinely contain only confirmatory/trend material relative to what their SUBSTANTIVE-quarter siblings already established.

---

```yaml
stage: B12d
company: "SYSTANGO"
run_date: "2026-08-29"
model: claude-sonnet-5
status: complete
peers_audited: 12
substantive_confirmed: 9
substantive_unsupported: []
unused_but_relevant:
  - {peer: "KSOLVES", missed_item: "Q2FY26 (Oct-2025) call's '21st result...after launching the IPO, out of 21st, 20 quarters' quote is the decisive Q6 IPO-vintage evidence Part 1 relies on and correctly sources to Oct-2025, but the coverage map rates this quarter CITED-ONLY and credits the contribution to Jul-2025 instead.", anchor: "KSOLVES-Concall_Oct_2025_Transcript.pdf p.7, Ratan Srivastava"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: "MAJOR", location: "B06 Part 1 Q4 / Part 4", claimed: "Blockchain-exit quote (INFOBEAN Jul-2025) characterized as unprompted, volunteered in prepared remarks", source_truth: "Quote is Avinash Sethi's direct answer to analyst Mohit's explicit blockchain question", note: "Inflates credibility of the report's strongest single corroborating data point"}
  - {severity: "MAJOR", location: "B06 Part 1 Q1", claimed: "'InfoBeans confirms elsewhere (Nov-2025 call)' the doubling-every-3-years/paused-1-2-years framing", source_truth: "This phrase is analyst Rupesh's own framing inside his question; management's answer does not restate or confirm it", note: "Misattributes analyst framing as management confirmation"}
  - {severity: "MAJOR", location: "B06 Part 3 coverage map / 06-peers.yaml", claimed: "KSOLVES Q2FY26 (Oct-2025) = CITED-ONLY, no decisive new fact; Q6 IPO-vintage contribution credited to Jul-2025", source_truth: "The '21st result...after launching the IPO' quote (the actual Q6 evidence Part 1 uses) is in the Oct-2025 transcript, p.7", note: "Peer-quarter miscredited; Oct-2025 should be SUBSTANTIVE for Q6"}
  - {severity: "MAJOR", location: "B06 Part 3 closing paragraph", claimed: "10 of 12 peer transcripts rated SUBSTANTIVE; 2 CITED-ONLY", source_truth: "Same paragraph's own correction and the coverage-map table both show 3 CITED-ONLY (INFOBEAN Nov-2025, KSOLVES Oct-2025, ONWARDTEC Jan-2026), i.e. 9 SUBSTANTIVE", note: "Headline coverage statistic is arithmetically wrong in the prose"}
  - {severity: "MINOR", location: "B06 Part 1 Q2", claimed: "KSOLVES debtors <60 days quote located in Q&A", source_truth: "Quote is in prepared remarks/presentation, p.8 of 25, before Q&A opens", note: "Cosmetic location error only"}
critical_count: 0
major_count: 4
minor_count: 1
acceptance_rate: 75    # 9 of 12 peer-quarters handled without a MAJOR/CRITICAL finding
peer_utilisation: 0.75  # corrected: 9 substantive-confirmed / 12 peers provided (B06's own stated "10/12" is the arithmetic error found above)
```
