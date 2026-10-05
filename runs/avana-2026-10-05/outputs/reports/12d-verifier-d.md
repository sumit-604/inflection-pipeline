# VERIFIER D: PEER COVERAGE AUDIT (B12d), AVANA, run 2026-10-05

Model: claude-sonnet-5-5. Artifacts audited: outputs/reports/06-peers.md, outputs/blocks/B06-peers.yaml, peer_questions in B05-concall.yaml (9 questions, lines 52-61). Page numbers are the [page N] markers in the .txt files.

## Counts
- peers_provided: 3 peers (DANISH, SPCL, MARINE); 4 documents (DANISH Nov-25 and May-26 calls, SPCL deck, MARINE deck); 3 screener sheets. B06 yaml says 4, counting documents.
- Used substantively: 3 of 3 (DANISH, SPCL by document; MARINE by sheet).
- peer_utilisation: 100% by peer; 67% if MARINE is counted CITED-ONLY on document text.

## Coverage audit per peer

| Peer | B06 label | Citations checked | Result |
|---|---|---|---|
| DANISH Nov-25 | SUBSTANTIVE | p2 order book 405 (line 90); p3 analyst "1-1.5% drop in gross margins" (l144); p4 "do not see any significant challenge" (l170) and monsoon (l176); p11 "end of December positively" (l541); p13 utilisation 92 or 93% (l638); p15 phase 1 "four months before" (l732); p21 monsoon (l1026); p29 "90% is the private sector", discom payment delays (l1394-1416) | All found in the stated pages. CONFIRMED |
| DANISH May-26 | SUBSTANTIVE | p3 sheet-metal "three to four months" (l124); p4 order book "about INR450 crores" (l163); p5 90% private (l183), EBITDA ~19% (l194); p6 "second phase came in live only after January" (l237); p9 ~30% price variation (l343); p10 19-21% margin exchange (l386-395); p16 Waaree (l630-646) | All found. CONFIRMED |
| SPCL deck (+sheet) | SUBSTANTIVE | p17 warranty split (l331, l338); p21 10,000 verticals, ~75% on 1 shift and ~25% on 3 shifts (l427-429); p25 top 5 66.1%, top 10 81.6% (l529-530); p30 40-45% CAGR (l644); p32 India CAGR 7.1% (l676-677); p37 EBITDA 17.5% vs 21.0% (l816); p39 inventory 316.8 to 568.7 (l879). Sheet: sales 132.36/155.4, RM 110.74/127.42, receivables 28.53/57.98, inventory 57.01/80.03, CFO -8.55/-22.81, borrowings 5.25/37.88 | All found and match. CONFIRMED |
| MARINE deck (+sheet) | SUBSTANTIVE (sheet-carried; B06 self-flags) | Deck p16-17 customers (shipyards, Navy, Coast Guard) and p32 "looking to have new facilities" found. Sheet: sales 767.10/876.94, RM 543.65/618.36, receivables 330.84/427.73, inventory 78.88/85.17, CFO -16.06, Q1 FY27 sales 259.16 vs 166.98, all match | Citations real; document weight light. MINOR: CITED-ONLY on document text, sheet is the carrier. |

## Unused or missed material (Rule 3)
- MARINE p31 (l693-696): approved-vendor list with Indian Navy/Coast Guard; "vendor qualification requires prior experience of similar work, references". Relates to Q9 vendor registration. It gives a barrier, not a registration-to-order lag, so the UNVERIFIABLE verdict stands. MINOR (context miss).
- DANISH and SPCL: grep for warranty, receivable ageing, provisioning, book-to-bill, concentration, registration found nothing beyond what B06 cites. No claim-relevant statement left unused.

## Verdict discipline (Rules 4 and 5)

| Claim | B06 verdict | Independent anchors | Discipline |
|---|---|---|---|
| Q1 margin fall | PARTIALLY VERIFIED | DANISH (2 calls) plus MARINE and SPCL sheets | OK, correctly held below VERIFIED since magnitude not matched |
| Q2 warranty rate | UNVERIFIABLE | none on rate | OK, no upgrade from silence |
| Q3 build slip | PARTIALLY VERIFIED | DANISH only | OK, one peer capped |
| Q4 sector growth | PARTIALLY VERIFIED | DANISH, MARINE, SPCL | OK |
| Q5 receivables | PARTIALLY VERIFIED | three sheets, DANISH call | OK |
| Q6 inventory and WC | PARTIALLY VERIFIED | three sheets, DANISH calls, SPCL deck | OK |
| Q7 order book, concentration | PARTIALLY VERIFIED | DANISH, SPCL | OK |
| Q8 capacity | PARTIALLY VERIFIED | DANISH, SPCL | OK |
| Q9 utility lag | UNVERIFIABLE | none | OK, analogy labelled as analogy |

Zero VERIFIED, so no single-peer VERIFIED and no upgrade from silence. All 9 of 9 peer_questions received a verdict.

## Other notes
- B06 Part 3 and yaml disclose the MARINE basis honestly; no concealment.
- Derived ratios (days, growth) are B06 arithmetic on sheet rows; spot-checked rows match the sheets. Not every derived ratio was recomputed.
- Not checked line by line: DANISH May-26 pages 7, 12, 14-15, 18 and Nov-25 pages 6, 16-17, 20-23, 27-28, 33-36 (cited for risks and context).

## Result
critical 0, major 0, minor 3. acceptance_rate 100.

```yaml
stage: B12d
company: "AVANA"
run_date: "2026-10-05"
model: claude-sonnet-5-5
status: complete
peers_provided: 3
peers_used_substantively: 3
peer_utilisation: "100% by peer (3 of 3); 67% if MARINE is counted CITED-ONLY (2 of 3 carried by document text)"
peers_audited: 3
substantive_confirmed: 3
substantive_unsupported: []
unused_but_relevant:
  - {peer: "MARINE", missed_item: "Vendor qualification barrier (Navy/Coast Guard approved vendor list), Q9 context, no lag", anchor: "MARINE deck page 31, lines 693-696"}
claims_all_addressed: true
verdict_discipline_fails: []
findings:
  - {severity: MINOR, item: "MARINE SUBSTANTIVE is sheet-carried; deck citations p16-17, p32 real but light"}
  - {severity: MINOR, item: "Q9 omits MARINE p31 vendor barrier; verdict stands"}
  - {severity: MINOR, item: "B06 peers_provided 4 counts documents, not peers"}
critical_count: 0
major_count: 0
minor_count: 3
acceptance_rate: 100
```
