# A3 FORENSIC NOTES: CONCALL | Poonawalla Fincorp Limited (POONAWALLA) | Q2FY27

Doctype: concall (Q2FY27 earnings call held 09-Oct-2026; transcript filed 14-Oct-2026, L18, L39)
Model: claude-opus-5-5
Lender: NBFC. F4, F5 and F12 run with explicit lender handling (orchestrator rule 12).
Read posture: PRE-THESIS. No Notion checklist and no companies/ file were supplied. No spear on record. Prior-quarter fulltext: ND.

Inputs read (only these):
- A1 structured: runs/poonawalla-q2fy27/extracted/poonawalla-concall-q2fy27-structured.md (R001-R287)
- A1 fulltext: runs/poonawalla-q2fy27/extracted/poonawalla-concall-q2fy27-fulltext.md (L1-L1093, read in full)
- A2 ledger: runs/poonawalla-q2fy27/work/ledger_concall_poonawalla_q2fy27.md

## 0. LEDGER RECONCILIATION

| ledger section | rows | read at cited line | result |
|---|---|---|---|
| 1 Participants (R246, R248-R253, R264-R267) | 11 | 11 | all match (L60, L71-77, L91, L625, L733, L811, L990) |
| 4 Management numbers (R001-R176) | 176 | 176 | all match; A2 VALUE_CONFLICT flags R116 (L603), R140 (L742), R175 (L1062) confirmed verbatim |
| 5 Forward commitments (R197-R241) | 45 | 45 | all match |
| 7 Dates (R177-R196) | 20 | 20 | all match |
| 8 Entities (R242-R271, less participants) | 30 type rows | 30 | all match |
| 9 Qualifiers (R272-R287) | 16 | 16 | all match; R280 label ambiguity confirmed (L168 vs L596) |
| 10 MISSING_FROM_STRUCTURED (M01-M03) | 3 | 3 | read at L817, L827, L845; all verbatim present |
| 11 ZERO_STANDING | 0 | n/a | A1 and A2 agree: none |

Rows read / rows in ledger: 287 / 287 = 100%, plus M01-M03.
A1 label note: R019 context reads "NIM plus fees sustained", but the verbatim at L169 is "sustained net income of over 9%". This is the same label drift as R280. It is folded into F14-03.
No A1 verbatim mismatch found. No source document opened.

## 1. FINDINGS TABLE

| id | check | ledger row ref | line | short verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| F6-01 | F6 | R152, R192, R225, R232; R156 (analyst) | L853-854; L876-877; L908 | "if you look at our commitment on the ROAs of June 2028" / "your peak will come in probably 2.5, 3 years from now" | FORWARD-SIGNAL | A dated ROA commitment (June 2028) is cited, but its level is never stated on the call. The analyst asked "what should be the sustainable ROA that you are targeting" (L876-877) and got no number. The peak sits 2.5-3 years out (Apr-Oct 2029), beyond the June 2028 date. Role 5 cannot track delivery until the level is on record. |
| F6-02 | F6 | R220, R221, R222, R231, R235, R285 | L747-748; L904; L1044-1045 | "2.19%, which looks more structural and stable" / "I can assure you this is structural, it's not cyclical" / "core credit cost impairment trend remains stable at an absolute basis ... despite approximately over 10% quarter-on-quarter growth" | FORWARD-SIGNAL | The CCO's own words say absolute impairment is flat. So the credit cost ratio fell because the book grew 10.4% QoQ. The "structural" claim depends on growth continuing. If growth slows, or the young book seasons, the ratio reverts. Lean bear. |
| F6-03 | F6 | R148, R223, R224; M01, M02 | L841; L850-851; L598 | "we are well-placed where it doesn't impact our profitability" / "pass this 25 basis point, which we've already passed effective a week back" | FORWARD-SIGNAL | A testable promise: a hike cycle with no profit impact. Cost of borrowing already moved 7.72% to 7.76% (L598) before any repo move (L827, L835). Q3FY27 test: cost of borrowing vs portfolio yield vs NIM. |
| F6-04 | F6 | R012, R014, R015, R150, R151, R176, R284 | L160-165; L852 | "disbursement yield by itself as well has further expanded by approximately 20 basis points ... on top of approximately 50 basis points" / "almost a 200 basis point difference ... at the minimum" | FORWARD-SIGNAL | Disbursement yield expansion slowed from about 50bp to about 20bp QoQ, while portfolio yield rose about 45bp. The portfolio-to-disbursement gap is closing by about 25bp a quarter. The disbursement yield level is never disclosed. The margin tailwind from transmission is finite, and the hike cycle works against it. |
| F6-05 | F6 | R043-R046, R138, R139, R202, R216, R217 | L224-226; L687-688 | "We remain on track to add a total of approximately 200 new branches in this financial year" / "we are investing in 300-400 branches every year" | AMBIGUOUS | Two branch numbers in one call: about 200 for FY27 against 300-400 every year. 90 opened in Q2 (460 to 550). At a 13-month breakeven (L687), the Q2 cohort breaks even around Nov 2027. Opex drag persists through FY28. A4 question: which number is the gold plan, and what is the FY26-end branch base. |
| F6-06 | F6 | R057, R058, R162-R164, R170, R171, R213, R258 | L243; L664; L796-797; L1038-1039 | "consumer durable to probably double our customer franchise this year" / "one of the most relatively riskier ones is the consumer durable in that hierarchy chain" | FORWARD-SIGNAL | The fastest-growing line (CD disbursement Rs606cr vs Rs433cr, +40% QoQ, L243) is, in the CEO's own ranking, the riskiest product. It is also the planned cross-sell funnel (L797-798). Credit behaviour of the CD cohort drives both credit cost and the cross-sell thesis. Seasoning evidence is 18 months, about 10 cycles (L1034-1035). |
| F6-07 | F6 | R029, R030, R112 | L186-188 | "This quarter movement sits within the 10 to 25 basis point range we had guided for" | AMBIGUOUS | Management claims the guidance was met but does not give the direction or the Q1 base. Opex-to-AUM is 4.15%, and "frontloaded" pre-investments (L186-187) suggest the movement was upward. A4 question: Q1FY27 opex-to-AUM and the sign of the move. |
| F7-01 | F7 | R233, R218 | L910-912 | "in between the quarter, you should expect some fluctuations, and I don't think there's anything to worry about that" | FORWARD-SIGNAL | A pre-emptive hedge on opex. It is paired with "I'm not going to shy away from any sensible investments" (L912-913, also L697-698). Read as advance cover for an opex-to-AUM uptick in coming quarters. |
| F7-02 | F7 | R238, R239, R271, R280, R017, R107, R175 | L1060-1066; L168; L596 | "if that framework comes alive" / "if at all, even if it plays out" | FORWARD-SIGNAL | A conditional hedge on the proposed insurance commission rules. No fee income share and no impact range were given, though the question was asked three times (L1003-1005, L1018-1019, L1057). The headline 9.26% is called "NIM plus fees" (L168) and also "net interest margin" (L596), so fee exposure cannot be separated. The answer cites portfolio yield as "14.8%" (L1062) vs 14.08% elsewhere (L161, L852). |
| F7-03 | F7 | R223; M02 | L839-840 | "we should be able to pass on the hike, depending on the product and the market dynamics" | AMBIGUOUS | Pass-through is conditional by product. Together with the unanswered floating share (F12-04), the margin effect of a 50bp hike cannot be bounded. |
| F12-01 | F12 (lender variant: asset-book decomposition) | R062-R066, R074-R083, R101, R118-R122 | L388-390; L582; L1051-1053 | "Stage 2 composition in Q2FY27 is at 0.94% versus 1.03% in Q1FY27" / "I have never seen Stage 2 getting compressed. You need to get the volumes down" | AMBIGUOUS (lean bear) | With AUM +10.4% QoQ, a flat absolute Stage 2 gives 1.03%/1.104 = 0.93%, below the reported 0.94%. The whole Stage 2 ratio fall is denominator, so absolute Stage 2 is flat to slightly up. GNPA: 1.37%/1.104 = 1.24%, so about 13bp of the 17bp fall is denominator and about 4bp is absolute reduction. The CEO credits calibration for Stage 2 compression; the arithmetic does not support that. Proxy caveat in Section 5. A4 question: absolute Rs Stage 2 and Stage 3, QoQ. |
| F12-02 | F12 (lender variant: equity-funded build) | R101, R127-R129, R154 | L582; L611-614 | "Our debt equity ratio stood at 4.3x" / "Tier 1 capital is 17.15%. This gives us enough headroom for our growth" | FORWARD-SIGNAL | The book grew 10.4% in one quarter (the analyst says 55% YoY, L873). A 2.18% ROA at 4.3x leverage does not self-fund that pace. No prior-quarter CRAR or Tier 1 was given, so the burn rate cannot be trended. Future external capital need, with timing unstated. A4 question: Tier 1 trajectory and capital-raise trigger. |
| F12-03 | F12 (lender variant: product segments) | R037-R058, R254-R258, R268 | L219; L222; L230; L236; L243; L775 | "average monthly disbursement of ₹127 crore" / "total quarterly disbursement of ₹606 crore" / "prudent mix of secured and unsecured" | AMBIGUOUS | Product data is disbursement only, on mixed bases: monthly average for Prime PL, CV and education; quarterly for gold and CD. CV and education have no prior-quarter comparatives. No product AUM, no total disbursement, and no secured/unsecured split. Segment asset trends cannot be built from this call. |
| F12-04 | F12 (lender variant: liability side) | R102, R103, R110, R111, R147, R269; M01, M03 | L585-586; L598; L816-818; L844-846 | "what is the mix of our floating and fixed-rate liabilities" / "our NCDs are 30% ... that's a fixed-rate" | AMBIGUOUS | Long-term borrowing share rose from 88.52% to 88.92%. Cost of borrowing rose 4bp. The floating/fixed mix was asked; only the NCD 30% fixed slice was answered. The rest (70%) has no rate-reset disclosure, and the 50bp sensitivity was not given. |
| F14-01 | F14 | R025-R028, R142-R144 | L179-181; L757 | "approximately 32 basis points lower than the 0.67%" vs "from a 0.67% is a substantial reduction there, almost 41 basis point" | AMBIGUOUS | In Q&A the CEO quotes the latest 6MOB 30+ fall as about 41bp. The prepared remarks put it at 32bp; 41bp was the prior quarter's fall. The overstatement flatters the lead indicator. A4 question: 6MOB 30+ cohort series for 4 quarters, ex-gold and incl gold. |
| F14-02 | F14 | R145, R168, R190, R191, R282 | L780-782 | "12 MoB 90-plus for origination post September 2024 has also seen an improvement of over 53% compared to the portfolio originated 12 months prior to September 2026" | AMBIGUOUS | The comparison window is incoherent: post-Sep-2024 originations overlap the 12 months before Sep-2026. The base cohort cannot be identified, so the 53% cannot be verified. Also "over 53%" (L781) vs "almost 53%" (L1027). |
| F14-03 | F14 | R021/R085 vs R116; R013/R151 vs R175; R017 vs R107 (R280); R019; R160/R161; R150/R284 | L174, L391 vs L603; L161, L852 vs L1062; L168 vs L596; L169; L959; L852 | "2.40% for Q1FY27" vs "2.41% in Q1 of FY27"; "14.08%" vs "14.8%"; "NIM plus fees" vs "net interest margin"; "almost a 200 basis point ... at the minimum" | NEUTRAL-FACT | Each item is immaterial on its own. Together they make the spoken numbers imprecise: five value or label drifts plus one self-contradicting qualifier ("almost" and "at the minimum" on one figure). Use the filed presentation and results numbers, not the spoken ones. |
| F14-04 | F14 | R251, R253, R277 | L89-92; L105 | "Mr. Harsh Kumar - Head, Artificial Intelligence and CHRO, and other senior management officials" / "this presentation may contain forward-looking statements" | NEUTRAL-FACT | The CFO (on the roster, L76) is left out of the moderator intro. He speaks once (L824-841), and the ED delivers the financials (L578-618). The safe harbor calls the call a "presentation". Governance-hygiene data points only. |
| F17-01 | F17 | R166, R167 (analyst), R237, R285 | L997-1000; L1042-1048 | "nearly 60% to 65% of your entire book is less than 12 months seasoned" / "My GNPA and write-offs are coming down significantly" | AMBIGUOUS (lean bear) | Write-offs were asked about directly and answered with no number. The analyst's claim that 60-65% of the book is under 12 months seasoned was not rebutted. On a young book, a 2.19% credit cost with only 1.2% GNPA implies write-offs carry the cost (analyst framing, L998-999). This is the key unknown for the credit cost path. |
| F17-02 | F17 | R219 | L709-710; L713-724 | "What is the product per customer right now versus say a year back" / "our product-per level will be more relevant to figure a year down the line" | AMBIGUOUS | The cross-sell metric was declined twice and deferred about 4 quarters, though cross-sell is called the "fundamental booster" of operating leverage (L668-669). Operating leverage is claimed, and its KPI is withheld. |
| F17-03 | F17 | R153, R154, R228 (analyst) | L869-870; L873 | "we have been saying that we target a 35% to 40% AUM CAGR" / "we are already growing at 55%" | AMBIGUOUS | The analyst attributed the AUM CAGR guidance to management. Management did not reaffirm it, revise it, or reply to the 55% YoY figure. No total disbursement or YoY AUM figure came from management. Growth guidance status: unconfirmed. |

## 2. CHECKLIST SCORECARD

| check | status | basis |
|---|---|---|
| F1 Zero-value standing items | N.A. | Concall, no financial tables; ZERO_STANDING count 0 (A1 and A2 agree). |
| F2 Standalone vs consolidated | N.A. | No S-vs-C figures spoken on the call. |
| F3 Shell-entity detection | N.A. | No entity cost lines on a concall. |
| F4 Unaudited contribution ratio | N.A. | Lender handled: no auditor report or Other Matters in a transcript. The results are "Unaudited" (L29). Component or subsidiary share cannot be seen here. A4 must run F4 on the Q2FY27 results filing. |
| F5 Going concern / EoM tracking | N.A. | Lender handled: no EoM paragraph in a transcript, and the prior-quarter fulltext is ND. ECL management overlay (a typical lender EoM topic) is not mentioned on the call; carried to F17. |
| F6 Forward-commitment mining | FINDING | 45 FORWARD rows read; register below; 7 findings (F6-01 to F6-07). |
| F7 Hedge mining | FINDING | Lexicon hit "subject to" only in the safe harbor (L108, boilerplate). Concall hedge forms ("you should expect some fluctuations", "if that framework comes alive", "depending on the product") give 3 findings. A2's 80 soft hedges were reviewed; "probably" attaches to the gold breakeven (L687), CD doubling (L664) and ROA peak (L908). |
| F8 Tax forensics | N.A. | No tax line spoken. |
| F9 OCI forensics | N.A. | No OCI spoken. |
| F10 Share count / dilution | N.A. | No paid-up capital or EPS spoken. |
| F11 Net worth tie-out | N.A. | No net worth spoken; only D/E 4.3x (L611) and CRAR (L613). Nothing to tie. |
| F12 Segment forensics | FINDING | Lender variant run: no segment table, so the product lines, the asset book (stage decomposition), capital, and liability mix were tested. 4 findings. |
| F13 Board outcomes | N.A. | Cover letter cites only earlier letters dated 30-Sep and 09-Oct-2026 (L36); no board outcomes in the transcript. |
| F14 Drafting inconsistencies | FINDING | 4 findings: 6MOB delta overstated, incoherent 12MoB window, number and label drift, intro and safe-harbor hygiene. |
| F15 Entity list diffs | N.A. | No consolidation list; no prior ledger. |
| F16 Dropped / reframed disclosures | N.A. | Presentation-specific check, and no prior deck or transcript was supplied. In-call reframing is under F14. |
| F17 Silence audit | FINDING | Notion checklist NOT SUPPLIED (pre-thesis). Audit run against standard lender monitorables plus F6 commitments; 17 silent rows below; 3 findings. |

## 3. COMMITMENT REGISTER (F6)

| # | commitment | implied date | turn / line ref | status word |
|---|---|---|---|---|
| C01 | Add about 200 new gold loan branches in FY27 | 31-Mar-2027 | T03 L225-226 (R202) | underway (90 added in Q2, 460 to 550) |
| C02 | Invest in 300-400 branches every year | annual, ongoing | T09 L688 (R217) | underway (conflicts with C01, see F6-05) |
| C03 | Gold branches break even in about 13 months | Q2 cohort about Nov-2027 | T09 L687 (R216) | initiated |
| C04 | CD customer franchise to about double this year | FY27 end, 31-Mar-2027 | T09 L664; T18 L796-797 (R213) | underway |
| C05 | Cross-sell expands QoQ; product-per-customer metric relevant a year out | about Q2FY28 | T03 L301-302; T09 L667-668; T11 L723-724 (R203, R214, R219) | initiated ("has commenced", L302) |
| C06 | Operating leverage plays out; opex-to-AUM becomes a key ROA contributor over two years | about Oct-2028 | T09 L653-654, L672-673; T27 L913-915 (R211, R215, R234) | underway |
| C07 | Opex-to-AUM movement within the guided 10-25bp range | per quarter | T03 L188 (R030) | completed for Q2 per management (direction not stated) |
| C08 | Credit cost stabilises; moves "strength-to-strength" over 1-2 years | Oct-2027 to Oct-2028 | T16 L748; T17 L772-773, L783; T27 L900-901; T29 L961-962 (R220-R222, R231, R235) | underway |
| C09 | GNPA and write-offs will come down | undated | T39 L1047-1048 (R237) | underway |
| C10 | ROA commitment for June 2028 (level not stated) | Jun-2028 | T25 L853-854 (R152, R192, R225) | underway |
| C11 | ROA peak in 2.5-3 years | Apr-2029 to Oct-2029 | T27 L908 (R232) | initiated |
| C12 | Rate hikes passed through; no profitability impact | Q3FY27 onward | T24 L839-841; T25 L850-851 (R223, R224, R148) | underway (25bp passed about 02-Oct-2026, "a week back") |
| C13 | Insurance commission fee compression absorbed by spread and operating leverage | conditional on the regulation | T42 L1060-1066 (R238, R239) | initiated (conditional) |
| C14 | 35-40% AUM CAGR over the next couple of years | about FY29 | T26 L869-870 (R228, analyst-attributed) | initiated (not reaffirmed by management) |
| C15 | AI "depth" phase; report progress next quarter | Q3FY27 call | T05 L565-572 (R209, R210) | underway (59 projects underway, L479) |
| C16 | Scale the two-pronged collections investment | undated | T04 L412 (R207, R208) | underway |
| C17 | Continue AI and "sensible" investment | ongoing | T09 L697-698; T27 L912-913 (R218) | underway |
| C18 | Margin positive on all three vectors over the next 1-2 years | Oct-2027 to Oct-2028 | T25 L855-858 (R226, R229) | underway |

## 4. WHAT WAS NOT DISCUSSED (F17 silence audit)

The Notion monitoring checklist was not supplied. This audit uses standard lender monitorables plus F6 commitments. Consecutive-quarter counts are a floor of 1 because the prior transcript is ND.

| # | monitorable | status on call | evidence | consecutive quarters silent |
|---|---|---|---|---|
| S01 | Total quarterly disbursement | not stated | only product fragments, L216-243 | 1 (floor) |
| S02 | AUM YoY growth (management-stated) | not stated by management | analyst 55%, L873, unanswered | 1 (floor) |
| S03 | Product-level AUM; secured/unsecured mix | not stated | "prudent mix of secured and unsecured", L775 | 1 (floor) |
| S04 | Write-offs (Rs, % of book) | asked, not quantified | L998-1000 vs L1042-1048 | 1 (floor) |
| S05 | Collection efficiency (%) | not stated | collections described in words only, L270-278, L407-433 | 1 (floor) |
| S06 | Absolute Stage 2 / Stage 3 (Rs cr) | not stated | ratios only, L388-390 | 1 (floor) |
| S07 | ECL management overlay; PCR trend | PCR level only, no prior | "49.14%", L608 | 1 (floor) |
| S08 | Fee income share; insurance commission impact | asked 3 times, not quantified | L1003-1005, L1057, L1060-1066 | 1 (floor) |
| S09 | Floating vs fixed borrowing mix; 50bp sensitivity | asked, partly answered (NCD 30% fixed) | L816-818, L844-846 | 1 (floor) |
| S10 | Disbursement yield level | deltas only | L162-165, L852 | 1 (floor) |
| S11 | Opex-to-AUM prior quarter and direction | not stated | L186-188 | 1 (floor) |
| S12 | ROA target level (June 2028; sustainable) | asked, not stated | L853-854, L876-877 | 1 (floor) |
| S13 | Products per customer | asked twice, deferred a year | L709-710, L723-724 | 1 (floor) |
| S14 | Numeric credit cost guidance | "stabilize" only | L772-773, L783 | 1 (floor) |
| S15 | Prior-quarter CRAR / Tier 1; capital-raise plan | not stated | L612-614 | 1 (floor) |
| S16 | AUM CAGR guidance reaffirmation | not reaffirmed | L869-870 | 1 (floor) |
| S17 | SMA / 1-90 DPD buckets; restructured book | not stated | n/a | 1 (floor) |

Addressed on the call: AUM (L582), NIM / NIM plus fees (L168, L596), cost of borrowing (L598), credit cost (L391, L603), GNPA/NNPA (L383-384, L605-607), Stage 1/2/3 (L388-390), CRAR and Tier 1 (L613), LCR (L615), ALM "positive cumulative mismatch across all buckets" (L617), surplus liquidity (L618), long-term borrowing share (L585-586), D/E (L611).

## 5. DERIVATION NOTES (arithmetic on disclosed numbers only)

- Q1FY27 AUM base: 74,008 / 1.104 = about Rs67,036cr (L582, R100, R101).
- Stage 2 at a flat absolute amount: 1.03% / 1.104 = 0.933%; reported 0.94% (L389). Implied absolute: 0.94% x 74,008 = about 696 vs 1.03% x 67,036 = about 690, so flat to +1%.
- GNPA at a flat absolute amount: 1.37% / 1.104 = 1.241%; reported 1.20% (L383). Implied absolute: about 888 vs about 918, so about -3%. Of the 17bp fall, about 13bp is denominator.
- NNPA: 0.70% / 1.104 = 0.634%; reported 0.61% (L384). Absolute about -4%.
- PCR check: 1 - 0.61/1.20 = 49.2%, in line with the stated 49.14% (L608). No finding.
- Caveat: stage ratios sit on the gross stage-asset base, not AUM. AUM is used as the proxy. If AUM includes off-book or co-lent assets that grew at a different pace, the split moves. The direction of F12-01 holds unless the stage-asset base grew well below 10.4%. Absolute Rs figures are NOT FOUND in this document.

## 6. FLAGGED FOR A4 (management questions)

FORWARD-SIGNAL: F6-01, F6-02, F6-03, F6-04, F6-06, F7-01, F7-02, F12-02.
AMBIGUOUS: F6-05, F6-07, F7-03, F12-01, F12-03, F12-04, F14-01, F14-02, F17-01, F17-02, F17-03.
Results-filing hand-offs: F4 (component or unaudited share) and F5 (EoM, ECL overlay) are N.A. on a transcript. Run them on the Q2FY27 results filing.

```yaml
stage: A3-forensics
company: "POONAWALLA"
quarter: "q2fy27"
doctype: "concall"
model: "claude-opus-5-5"
status: complete
forensics_path: "runs/poonawalla-q2fy27/work/forensics_concall_poonawalla_q2fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: N.A.
  F11: N.A.
  F12: FINDING
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: N.A.
  F17: FINDING
findings:
  - {id: "F6-01", check: "F6", line: "L853-854; L876-877; L908", classification: "FORWARD-SIGNAL", implication: "June 2028 ROA commitment cited with no level; sustainable ROA asked, not given; peak 2.5-3y out"}
  - {id: "F6-02", check: "F6", line: "L747-748; L904; L1044-1045", classification: "FORWARD-SIGNAL", implication: "credit cost called structural, yet CCO says absolute impairment flat; ratio fall is growth denominator; reverts if growth slows"}
  - {id: "F6-03", check: "F6", line: "L841; L850-851; L598", classification: "FORWARD-SIGNAL", implication: "no profit impact from hike cycle promised; CoB already 7.72 to 7.76%; test in Q3FY27"}
  - {id: "F6-04", check: "F6", line: "L160-165; L852", classification: "FORWARD-SIGNAL", implication: "disbursement yield expansion slowed 50bp to 20bp; portfolio gap closing ~25bp/qtr; transmission tailwind finite"}
  - {id: "F6-05", check: "F6", line: "L224-226; L687-688", classification: "AMBIGUOUS", implication: "~200 gold branches FY27 vs 300-400 every year; 13-month breakeven pushes Q2 cohort to ~Nov-2027"}
  - {id: "F6-06", check: "F6", line: "L243; L664; L796-797; L1038-1039", classification: "FORWARD-SIGNAL", implication: "CD +40% QoQ and doubling franchise is self-ranked riskiest product and the cross-sell funnel"}
  - {id: "F6-07", check: "F6", line: "L186-188", classification: "AMBIGUOUS", implication: "opex guidance claimed met; direction and Q1 base undisclosed"}
  - {id: "F7-01", check: "F7", line: "L910-912", classification: "FORWARD-SIGNAL", implication: "pre-emptive hedge: expect quarterly opex fluctuations"}
  - {id: "F7-02", check: "F7", line: "L1060-1066; L168; L596", classification: "FORWARD-SIGNAL", implication: "insurance commission impact unquantified after 3 asks; fee share hidden in 9.26% NIM vs NIM-plus-fees label"}
  - {id: "F7-03", check: "F7", line: "L839-840", classification: "AMBIGUOUS", implication: "rate pass-through conditional by product and market"}
  - {id: "F12-01", check: "F12", line: "L388-390; L582; L1051-1053", classification: "AMBIGUOUS", implication: "Stage 2 fall fully denominator (1.03/1.104=0.93 vs 0.94 reported); ~13 of 17bp GNPA fall denominator; calibration claim unsupported"}
  - {id: "F12-02", check: "F12", line: "L582; L611-614", classification: "FORWARD-SIGNAL", implication: "10.4% QoQ growth at 4.3x D/E, Tier 1 17.15%, no prior CRAR; external capital need, timing unstated"}
  - {id: "F12-03", check: "F12", line: "L219; L222; L230; L236; L243; L775", classification: "AMBIGUOUS", implication: "product data disbursement-only on mixed bases; no product AUM, total disbursement or secured/unsecured split"}
  - {id: "F12-04", check: "F12", line: "L585-586; L598; L816-818; L844-846", classification: "AMBIGUOUS", implication: "only NCD 30% fixed disclosed; 70% reset profile and 50bp sensitivity unanswered"}
  - {id: "F14-01", check: "F14", line: "L179-181; L757", classification: "AMBIGUOUS", implication: "6MOB fall overstated in Q&A as ~41bp vs 32bp; lead indicator flattered"}
  - {id: "F14-02", check: "F14", line: "L780-782; L1027", classification: "AMBIGUOUS", implication: "12MoB 90+ comparison window incoherent; 53% unverifiable; over vs almost 53%"}
  - {id: "F14-03", check: "F14", line: "L174, L391, L603; L161, L852, L1062; L168, L596; L169; L959; L852", classification: "NEUTRAL-FACT", implication: "spoken number and label drift; use filed figures"}
  - {id: "F14-04", check: "F14", line: "L89-92; L105", classification: "NEUTRAL-FACT", implication: "CFO omitted from intro; safe harbor calls call a presentation"}
  - {id: "F17-01", check: "F17", line: "L997-1000; L1042-1048", classification: "AMBIGUOUS", implication: "write-offs unquantified; 60-65% book under 12m seasoned unrebutted; key unknown for credit cost path"}
  - {id: "F17-02", check: "F17", line: "L709-710; L713-724", classification: "AMBIGUOUS", implication: "products-per-customer withheld twice, deferred ~4 quarters while cross-sell is the claimed lever"}
  - {id: "F17-03", check: "F17", line: "L869-870; L873", classification: "AMBIGUOUS", implication: "35-40% AUM CAGR guidance not reaffirmed; 55% YoY unanswered"}
forward_signals: ["F6-01", "F6-02", "F6-03", "F6-04", "F6-06", "F7-01", "F7-02", "F12-02"]
ambiguous: ["F6-05", "F6-07", "F7-03", "F12-01", "F12-03", "F12-04", "F14-01", "F14-02", "F17-01", "F17-02", "F17-03"]
commitments:
  - {commitment: "~200 new gold branches in FY27", implied_date: "2027-03-31", ref: "T03 L225-226 R202", status_word: "underway"}
  - {commitment: "300-400 branches every year", implied_date: "annual", ref: "T09 L688 R217", status_word: "underway"}
  - {commitment: "gold branch breakeven ~13 months", implied_date: "2027-11 (Q2 cohort)", ref: "T09 L687 R216", status_word: "initiated"}
  - {commitment: "CD customer franchise ~doubles this year", implied_date: "2027-03-31", ref: "T09 L664; T18 L796-797 R213", status_word: "underway"}
  - {commitment: "cross-sell expands QoQ; product-per-customer metric a year out", implied_date: "~Q2FY28", ref: "T03 L301-302; T11 L723-724 R203 R219", status_word: "initiated"}
  - {commitment: "operating leverage; opex-to-AUM key ROA contributor over two years", implied_date: "~2028-10", ref: "T09 L653-654; T27 L913-915 R211 R234", status_word: "underway"}
  - {commitment: "opex-to-AUM movement within 10-25bp guided range", implied_date: "quarterly", ref: "T03 L188 R030", status_word: "completed"}
  - {commitment: "credit cost stabilises, improves over 1-2 years", implied_date: "2027-10 to 2028-10", ref: "T16 L748; T17 L772-783; T27 L900-901 R220-R222 R231 R235", status_word: "underway"}
  - {commitment: "GNPA and write-offs will come down", implied_date: "undated", ref: "T39 L1047-1048 R237", status_word: "underway"}
  - {commitment: "ROA commitment for June 2028 (level not stated)", implied_date: "2028-06", ref: "T25 L853-854 R152 R192 R225", status_word: "underway"}
  - {commitment: "ROA peak in 2.5-3 years", implied_date: "2029-04 to 2029-10", ref: "T27 L908 R232", status_word: "initiated"}
  - {commitment: "rate hikes passed through, no profitability impact", implied_date: "Q3FY27 onward", ref: "T24 L839-841; T25 L850-851 R223 R224", status_word: "underway"}
  - {commitment: "insurance fee compression absorbed via spread and operating leverage", implied_date: "conditional", ref: "T42 L1060-1066 R238 R239", status_word: "initiated"}
  - {commitment: "35-40% AUM CAGR next couple of years (analyst-attributed, not reaffirmed)", implied_date: "~FY29", ref: "T26 L869-870 R228", status_word: "initiated"}
  - {commitment: "AI depth phase; report progress next quarter", implied_date: "Q3FY27 call", ref: "T05 L565-572 R209 R210", status_word: "underway"}
  - {commitment: "scale two-pronged collections investment", implied_date: "undated", ref: "T04 L412 R207", status_word: "underway"}
  - {commitment: "continue AI and sensible investment", implied_date: "ongoing", ref: "T09 L697-698 R218", status_word: "underway"}
  - {commitment: "margin positive on all three vectors over 1-2 years", implied_date: "2027-10 to 2028-10", ref: "T25 L855-858 R226", status_word: "underway"}
gate_a3: pass
blank_checks: []
analyst_note: "Pre-thesis read with no prior transcript, so silence counts are floors and no EoM or entity diff was possible. The headline asset-quality gain is mostly a growth denominator. With AUM up 10.4% QoQ, a flat absolute Stage 2 gives 0.93% against 0.94% reported, and about 13 of the 17bp GNPA fall is arithmetic. The CCO says absolute impairment is stable (L1044). So the structural credit cost claim (L748, L904) rests on growth continuing, on a book the analyst says is 60-65% under 12 months seasoned (L997, unrebutted). Write-offs, the swing variable, were never quantified. Three margin supports are weakening together: yield transmission is narrowing, funding costs are turning in a hike cycle, and fee income exposed to the insurance commission proposal is buried in a 9.26% figure labelled both NIM and NIM plus fees. The fastest-growing line, consumer durable at +40% QoQ, is the riskiest by the CEO's own ranking and is also the cross-sell funnel. Growth at 4.3x leverage implies a capital raise; its timing is unstated. Stage derivations use AUM as a proxy. A4 should source absolute Stage 2/3, write-offs and the F4/F5 checks from the results filing."
```
