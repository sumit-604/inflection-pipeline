# Verifier D: Peer Coverage Audit, PREMEXPLN, run 2026-11-15

## Coverage audit per peer (spot-read against transcripts)

| Peer | B06 label | Citations tested | Result |
|---|---|---|---|
| SOLARINDS (4 calls) | SUBSTANTIVE | Q4 FY26 rise-and-fall clause (line 320, p7), "60% of the total increase" (line 353, p8), EBITDA down "2% to 3%" (line 460); Q2 FY27 banned-country rule (line 388) and Rs 20,178 Cr order book (line 392); Q3 FY26 defence Rs 702 Cr (line 168) and Pinaka "no more delay" (line 380); Kalyani entry (Q4 FY26 line 291) | All found, wording matches. Page labels follow the transcript's own "Page N of 12" footer. |
| ASTRAMICRO (4 calls) | SUBSTANTIVE | Q3 FY26 inspection "hindrances" (line 411); Q1 FY27 "inspection issues" (line 702); Q4 FY26 "top end" (line 501), OCF Rs 370 Cr vs -Rs 99 Cr (line 143), Rs 38,000 Cr and 75% (lines 116-123), FOPM (684-686), electronic mines (764); Q2 FY26 L2 counter-drone (624); Q3 FY26 Rs 1,477 Cr (122), PSU working capital (257) | All found. Rs 38,000 Cr is stated as "India's defence exports"; B06 reports it as a level only, as the transcript says. |
| BDL | UNUSED | No transcripts in the corpus (0 of 4) | Correct: corpus gap, nothing to use. |

Zero-hit searches confirmed: "inspection" appears only twice (both Astra), as B06 states; no peer mentions Premier, chaff, flares, liquidated damages or Munitions India.

## Unused-but-relevant scan
Astra Q4 FY26 lines 532-534 and 665 (programmes and DRDO orders delayed) support Q1 and are additional to two Astra anchors already cited. MINOR, no verdict effect. Solar "licence" hits are only the banned-country rule, already used in Q2. No directly claim-relevant statement left unused.

## Verdict-discipline audit

| Claim | B06 verdict | Independent peer anchors | Assessment |
|---|---|---|---|
| Q1 inspection/LD | PARTIALLY | Astra x2 clear, Solar weak | Correct; LD half UNVERIFIABLE, no silence upgrade |
| Q2 licences | UNVERIFIABLE | Solar regime only | Correct |
| Q3 input prices/MIL | PARTIALLY | Solar; Astra no price talk | Correct |
| Q4 margins | VERIFIED | Solar + Astra (6 anchors) | Meets 2-peer bar; mix caveat stated |
| Q5 growth | PARTIALLY | Astra budget; exports level only | Correct |
| Q6 capex | PARTIALLY | Solar only | Correct |
| Q7 moat | UNVERIFIABLE | Silence not upgraded | Correct |
| Q8 QRSAM | PARTIALLY | Astra only | Correct |
| Q9 cash conversion | VERIFIED | Astra + Solar | Meets bar |
| Q10 Apollo | UNVERIFIABLE | none | Correct |
| Q11 disclosure | PARTIALLY | Solar + Astra on splits; licence cover UNVERIFIABLE | Correct |

No VERIFIED rests on one peer. No verdict upgraded from silence. Tally 2 / 6 / 3 = 11 matches.

## Peer-question coverage
B05 lists 11 numbered peer_questions? Count in B05 block: 11 entries (the list holds Q1-Q11 including the Apollo question). B06 Q1-Q11 maps one to one. claims_all_addressed: true. Skipped: none.

## Findings
3 MINOR, 0 MAJOR, 0 CRITICAL. Acceptance rate 100% of the two peers with transcripts (67% if BDL is counted; BDL is a corpus gap, not a handling failure).

```yaml
stage: B12d
company: "PREMEXPLN"
run_date: "2026-11-15"
model: claude-sonnet-5-5
status: complete
peers_audited: 3
substantive_confirmed: 2
substantive_unsupported: []
unused_but_relevant:
  - {peer: "ASTRAMICRO", missed_item: "Q4 FY26 programme/DRDO delay remarks supporting Q1; additive only", anchor: "ASTRAMICRO-202606-Q4FY26 lines 532-534, 665"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, finding: "Q1 omits Astra Q4 FY26 delay remarks; no verdict change", anchor: "ASTRAMICRO-202606-Q4FY26 lines 532-534"}
  - {severity: MINOR, finding: "BDL 0 transcripts, honestly recorded UNUSED; corpus gap", anchor: "B06 Part 3"}
  - {severity: MINOR, finding: "Q4 VERIFIED with neither peer selling countermeasures; caveat stated in B06", anchor: "B06 Q4 net read"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
