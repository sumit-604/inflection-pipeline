# Verifier D: Peer Coverage Audit, CREDENT (2026-11-12)

Scope: B06 (06-peers.md, B06-peers.yaml) against the 12 peer .txt transcripts and the 9 peer_questions in B05. Method: located the key quoted citation of each SUBSTANTIVE row in the transcript text and confirmed wording and page marker; spot-read CITED-ONLY rows with grep for claim-relevant terms (asset-light, vendor, outsourc, receivable, debtor, minimum, capex, credit). Not every figure in B06 was re-read; coverage is a sample of load-bearing quotes.

## Coverage audit per peer

| Peer / call | B06 usage | Citation check | Result |
|---|---|---|---|
| THYROCARE Q3 FY26 (Feb) | SUBSTANTIVE | "dedicated phlebotomy fleet" (line 302); "market grows at 10%, right, 10%, 11%" (line 621); credit period 60 to 90 days (line 673) all found | Confirmed |
| THYROCARE Q4 FY26 (May) | CITED-ONLY | Cited facts not re-tested. Unused: asset-light, maintenance capex about INR 40 Cr (lines 629-634) | MINOR miss |
| THYROCARE Q1 FY27 (Jul) | CITED-ONLY | Only "credentials" hit for Credent search (line 201), matches B06 2D. No receivable or vendor terms found | Handled |
| THYROCARE Q2 FY27 (Nov) | SUBSTANTIVE | PharmEasy "around 11%" (line 435, after page 11 marker at 416 wait: p.11 per B06; text sits in page 11 block); "two or three quarters away" (line 455) found. Unused: outsourced kit vendors (lines 406-408) | Confirmed, MINOR miss |
| TCIEXP Q3 FY26 (Feb) | SUBSTANTIVE | "top 25 customers not giving more than 15%" (line 327) found | Confirmed |
| TCIEXP Q4 FY26 (Jun) | SUBSTANTIVE | "asset light business model" (line 250); 15% 16% margin (line 363) found | Confirmed |
| TCIEXP Q1 FY27 (Aug) | SUBSTANTIVE | D2C 16% to 18% (line 308); capex 125 to 140 Cr (line 440) found | Confirmed |
| TCIEXP Q2 FY27 (Nov) | SUBSTANTIVE | 12.7%, best in five quarters (lines 117, 155); receivable 59, payable 32 (line 182); INR 100 Cr plus capex (line 371); "two, three year ... 15%, 16%" (line 544) found | Confirmed |
| KRYSTAL Q4 FY25 (May 2025) | SUBSTANTIVE | "management fee based percentage of the CTC", two to three year contracts (lines 699-700, p.17 marker at 675); working capital from new businesses explains negative operating cash flow (lines 747-749; the negative CFO is stated by the analyst and not disputed) found | Confirmed |
| KRYSTAL Q2 FY26 (Nov 2025) | SUBSTANTIVE | debtor days "above 110" (lines 669-670, page 16) found; mgmt reply "cyclical" found, but reply also says days fell the next month (lines 673-675) | Confirmed, MINOR one-sided |
| KRYSTAL Q4 FY26 (May 2026) | CITED-ONLY | Receivables rise (line 324) found; no other claim-relevant gap found in grep | Handled |
| KRYSTAL Q2 FY27 (Nov 2026) | SUBSTANTIVE | "about 118 days, in line with March '26, despite increase in business" (lines 276-277); start-up dip quote (lines 288-292) found | Confirmed |

9 of 9 SUBSTANTIVE rows have real, findable citations. No SUBSTANTIVE row lacks one.

## Verdict-discipline audit (9 peer_questions)

| Q | B06 verdict | Anchors | Discipline |
|---|---|---|---|
| Q1 | UNVERIFIABLE | none claimed | OK; Thyrocare silence not upgraded |
| Q2 | PARTIALLY VERIFIED | Thyrocare only for 11%; deck path noted unsupported | OK |
| Q3 | UNVERIFIABLE | receivable-side terms flagged as not testing payables | OK |
| Q4 | PARTIALLY VERIFIED (one peer) | TCIEXP | OK |
| Q5 | CONTRADICTED | Krystal 118 days, TCIEXP 59 | OK; Q2 FY26 quote one-sided (MINOR) |
| Q6 | PARTIALLY VERIFIED | Krystal, TCIEXP | OK |
| Q7 | PARTIALLY VERIFIED (benchmark only) | TCIEXP, Thyrocare | OK, limitation stated |
| Q8 | PARTIALLY VERIFIED | TCIEXP, Krystal | OK |
| Q9 | CONTRADICTED on "no launch losses" | Krystal, TCIEXP | OK, minimum-guarantee part marked unverifiable |

Zero VERIFIED verdicts, so no single-peer VERIFIED and no upgrade from silence. All 9 questions received a verdict.

## Result
0 CRITICAL, 0 MAJOR, 3 MINOR. Acceptance 12 of 12 peers handled correctly (100%). The MINOR items do not change any verdict.
