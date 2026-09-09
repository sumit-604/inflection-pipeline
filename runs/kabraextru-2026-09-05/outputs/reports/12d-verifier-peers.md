# VERIFIER D — PEER COVERAGE AUDIT (RERUN)
**Company:** KABRAEXTRU | **Run date of record:** 2026-09-05 | **B06 version audited:** Rerun 3 (dated 2026-09-09)
**Verifier D pass:** 2nd (this is the re-audit of the rerun; prior Verifier D pass audited run 2 of B06)
**Model:** claude-sonnet-5 | **Scope:** B06 report + block, cross-checked against the 5 raw peer transcripts and the WINDMACHIN screener CSV, and against the 10 injected peer_questions (9 from B05 run1 + 1 added this rerun).

I did not read any other pipeline stage report or any other verifier's output, per the structural rule.

---

## METHOD

For every peer marked SUBSTANTIVE in B06 Part 3, I opened the actual source file, located every PDF-page-marker anchor cited in B06 Parts 1-2, and confirmed the cited text exists at that marker (not one page off, not paraphrased into something the source doesn't say). I read all five transcripts in full (not by anchor-hopping) so I could also spot-read for unused, claim-relevant material. I opened the WINDMACHIN CSV and checked every cell B06 cites against the raw row. I then checked verdict discipline against Rule 4 (peer-count adequacy for VERIFIED) and confirmed all ten claims in the injected peer_questions list received a verdict (Rule 5).

---

## PART 1: COVERAGE AUDIT TABLE (per peer)

| Peer / call | B06 usage | Anchors checked | Result |
|---|---|---|---|
| RAJOOENG Q4 FY23 (16-May-2023, `..._May_2023_...txt`) | SUBSTANTIVE | FY23 revenue Rs159.79 Cr (p.3) ✓; capex plan Rs20-25 Cr at Rs200 Cr ceiling (p.5) ✓; Pakistan/Russia-Ukraine geopolitical export friction (p.9-10) ✓; late-dispatch/space-occupation 2-3% margin cost (p.8-9) ✓; domestic 4-5% vs export "nearly 30% to 35% more" margin (p.20) ✓; Rajoo Bausano 49%-owned JV, ~Rs30 Cr FY23 turnover (p.16, corrected from run 2's p.17) ✓ | CONFIRMED — every citation checked is genuine and correctly anchored |
| RAJOOENG Q2 FY24 (6-Nov-2023, `..._Nov_2023_...txt`) | SUBSTANTIVE | Global CAGR 4.6%/4.2% quote (p.3) ✓; RM "prices have gone up...only volume can help" (p.7) ✓; back-to-back procurement (p.10, corrected from run 2's p.9) ✓; three Claim-10 working-capital quotes — 35-40% advance (p.10) ✓, 95% payment before dispatch (p.12) ✓, 71→22-day receivable days + "terms has not changed" (p.11) ✓; capacity expansion to Rs300-325 Cr via 3 Rajkot plots (p.5) ✓ | CONFIRMED — all three Claim-10 anchors verified exactly at p.10/p.11/p.12 as re-stated in the rerun |
| RAJOOENG Q4 FY24 (18-Apr-2024, `..._Apr_2024_...txt`) | SUBSTANTIVE | Global market size USD 8.33bn→11.6bn (p.2) ✓; 80%/60% category shares (p.7) ✓; Rs9.33 Cr capex (p.6, corrected from run 2's p.5) ✓; Rs15 Cr tooling capex (p.9) ✓; order book Rs140 Cr (p.8) ✓; "Windsor machines and carbon extrusion" (p.9, corrected from run 2's p.8) ✓; Rs1,500 Cr domestic market sizing (p.11) ✓; 45% FY24 export share (p.12, corrected from run 2's p.11) ✓; RM stability quote (p.14, corrected from run 2's p.12) ✓; replacement-cycle 20yr→10yr (p.8) ✓ | CONFIRMED, with 2 MINOR anchor-range imprecisions (see Findings 2-3) |
| RAJOOENG Q2 FY25 (22-Oct-2024, filename mislabeled `..._Nov_2025_...txt`) | SUBSTANTIVE | H1 FY25 revenue Rs107.68 Cr, +27.07% (p.4) ✓; order book Rs200+ Cr (p.13 **and** p.15, both checked) ✓; Rs1,000 Cr pipeline (p.15) ✓; Rs2,000 Cr total market size + scope caveat (p.6) ✓; 33% PVC installed-capacity share (p.11) ✓; 55-60% blown-film share (p.12) ✓; 73% export + "domestic is not really encouraging margin" (p.12) ✓; "probably FY '26 we would be able to fill up all the capacity" (p.15) ✓; RM stability / "apple-plus-plus" (p.13) ✓ | CONFIRMED, with 1 MINOR imprecision on the composite "73-74%" figure (Finding 2) |
| HBLENGINE FY25 AGM (25-Sep-2025) | SUBSTANTIVE | "no one outside China can make a profit...We chose a niche for defense" (p.3-4) ✓; "~200 crores or less...profit from year one" (p.4) ✓; failed bets (Reliance, Exide, Amara Raja, Northvolt) (p.4) ✓; conglomerate discount / portfolio premium (p.5) ✓; 35-55 tonne truck pivot, smaller-truck prototypes dropped (p.15-16) ✓; p.17 "everybody can import **sales**" verbatim, correcting run 2's "cells" (p.17) ✓; Kavach Rs3,000 Cr budget (p.2) ✓; Rs4,500 Cr by FY30 (p.3) ✓ | CONFIRMED — the run's own headline correction (p.17 "sales" not "cells") verified accurate against the transcript |
| WINDMACHIN (screener only, no transcript) | CITED-ONLY | Sales row 11 (FY25 327.6→FY26 566.52, +72.9%) ✓; Net profit row 24 (FY25 -25.27→FY26 -4.43) ✓; Equity Share Capital row 39, Reserves row 40 ✓; Investments row 46 (9.19→343.11→42.0) ✓; Net Block row 44 (321.76→331.79→212.71) ✓; CWIP row 45 (20.91/16.05) ✓; Cash from Investing row 58, Financing row 59 ✓; June-2026 quarter Sales row 28 (146.21) and Net profit row 35 (-1.08) ✓ | CONFIRMED — every cited figure matches the CSV exactly; row references in the "Sources Re-Read" list are accurate; no CSV defect found (consistent with B06's own note) |

**Result: 6 of 6 peer-coverage-map entries confirmed. Zero fabricated or unfindable citations across every anchor checked (approximately 45 discrete citations verified against source).** This is a materially cleaner rerun than the prior draft (which drew a REWORK verdict from prior verifiers on page-offset grounds); the page-offset fix list appears to have been executed with genuine care, not just relabeled.

---

## PART 2: VERDICT-DISCIPLINE AUDIT (per claim)

| # | Verdict | Peers relied on | Anchor count | Rule 4 check | Result |
|---|---|---|---|---|---|
| 1 | CONTRADICTED (framing) | RAJOOENG (+ weak WINDMACHIN corroboration) | Multiple, single peer | N/A (rule targets VERIFIED only) | Caveat ("framing plausibility, not FY26 figures") is stated inline and is accurate — the peer set genuinely cannot reach FY26. PASS |
| 2 | PARTIALLY VERIFIED | RAJOOENG | 2 (two calls, same peer) | N/A | Single-peer, but classification is already the downgraded tier (PARTIALLY, not VERIFIED); consistent with the spirit of Rule 4. PASS |
| 3 | PARTIALLY CONTRADICTED | RAJOOENG | 2 (Rs1,500 Cr + Rs2,000 Cr quotes) | N/A | Arithmetic re-checked (314.89/2000=15.7%, 314.89/1500=21.0%) against real, correctly-anchored quotes. PASS |
| 4 | UNVERIFIABLE | RAJOOENG | — | N/A | Peer data genuinely does not reach the FY25-26 window. PASS |
| 5 | CONTRADICTED (framing) | RAJOOENG | Multiple, single peer | N/A | Same caveat structure as Claim 1; see Finding 2 for a citation-precision note on the underlying "73-74%" figure. PASS with a minor citation-precision caveat |
| 6 | CONTRADICTED (direction) | RAJOOENG + WINDMACHIN | Multiple | N/A | Correctly labeled as two peers of "different and not fully explained mechanisms," not claimed as a clean two-peer confirmation. PASS |
| 7 | UNVERIFIABLE | HBLENGINE | — | N/A | Genuine segment mismatch, correctly held to UNVERIFIABLE despite the added capital-scale contrast. PASS |
| 8 | UNVERIFIABLE | HBLENGINE | — | N/A | Same as above; p.17 quote corrected and verified. PASS |
| 9 | UNVERIFIABLE | HBLENGINE | — | N/A | Confirmed absent from the transcript — no EV battery-pack market-size figure anywhere in the AGM. PASS |
| 10 | **VERIFIED** | **RAJOOENG only** | **3 (all three from the same single peer)** | **FAILS** | **MAJOR — see Finding 1** |

**Rule 4 finding.** Claim 10 is logged in the B06 YAML under `verified:` with `peers: ["RAJOOENG"]` — one peer. B06's own prose hedges this ("the comparison itself is not a claim-verification in the usual sense... logged as a verified peer finding"), which is an honest flag that something is atypical about the classification, but it does not change the verdict label actually recorded, which is VERIFIED, and the schema field is `verified`, not `partially_verified`. Rule 4 states plainly: "any VERIFIED resting on one peer is MAJOR (should be PARTIALLY VERIFIED)." Three anchors from a single peer is still one peer. Whatever the underlying evidence quality (and it is strong — three separately located, verbatim, on-topic quotes, all independently re-verified above), the rule does not carve out an exception for high-quality single-peer evidence, and Claim 10 is exactly the pattern the rule targets. This should have been labeled PARTIALLY VERIFIED, with the "peer disclosure vs. claim-test" nuance kept as a note inside that entry, not used as a basis to keep the stronger VERIFIED label.

**Rule 5 check — all ten claims addressed.** The nine B05 peer_questions plus the one rerun-added working-capital question (check_peers: RAJOOENG) all appear as Claims 1-10 in B06 Part 1, each with a verdict, peer evidence field, and net read. No skipped claim. `claims_all_addressed: true`.

**On testing a FY26-window claim with pre-FY26 peer evidence.** B06 is unusually disciplined here relative to a typical single-pass report: every CONTRADICTED/PARTIALLY CONTRADICTED verdict that touches the FY26 window carries an explicit "framing plausibility only, not a test of FY26 figures" caveat inline in the Verdict field itself (not only in a top-of-report notice), and Part 4's own triangulation summary restates this limit rather than overclaiming. The peer set (4 RAJOOENG calls through Oct-2024, one HBL AGM from Sep-2025 that is a segment mismatch, one screener-only competitor) genuinely cannot directly confirm or deny KABRAEXTRU's FY26 figures; B06 does not claim otherwise. This is correct methodology, not a violation of Rule 4 (which is about peer-count, not staleness), and I did not fabricate a Rule-4-style finding here since the rule as written targets the VERIFIED tier specifically.

---

## PART 3: FINDINGS

| # | Severity | Location | Finding |
|---|---|---|---|
| 1 | **MAJOR** | Claim 10 verdict field (B06 report Part 1 + B06 YAML `verified:`) | VERIFIED verdict rests on a single peer (RAJOOENG), despite three anchors, contrary to Verifier D Rule 4 ("any VERIFIED resting on one peer is MAJOR (should be PARTIALLY VERIFIED)"). This is a verdict-discipline fail. |
| 2 | MINOR | Claim 5, "73-74% of H1 FY25 revenue" (report Part 1, Claim 5; also Part 4, Part 5) | The "domestic is not really encouraging margin...73%...export" quote is correctly anchored at Q2 FY25 PDF p.12. But the companion "74%" figure is stated separately, on PDF p.10 ("the current quarter and in the last quarter we did around 74% revenue coming from the export market"), a different Q&A exchange about quarterly, not half-yearly, export share. The composite "73-74%" is cited to p.12 alone; p.10 is the actual source of "74%". Content is genuine either way — no fabrication — but the anchor for one half of the composite figure is imprecise. |
| 3 | MINOR | Claim 6, "new facility inaugurated Apr-2024 (PDF p.2-3)" | The inauguration sentence ("Moreover, on April 16th 2024 we celebrated the inauguration of our new facility...") is located entirely within PDF p.3 of the Q4 FY24 call; PDF p.2 (the preceding page, covering the global market-size figures) does not contain this text. The p.2-3 range overstates by one page. |
| 4 | MINOR | Claim 4 / Part 2E(i), "Red Sea shipping crisis...(PDF p.6-7)" | The full Red Sea/inventory-days/payable-days answer from Prakash Daga is located entirely on PDF p.7 of the Q4 FY24 call (the question that prompts it begins at the very end of p.6/start of p.7, but the substantive quoted material is on p.7). The p.6-7 range is a minor overreach, not a wrong page. |
| 5 | MINOR (cosmetic) | B06 "Sources Re-Read" file-list | B06 states "(11pp)" for the Nov-2023 (Q2 FY24) transcript and "(15pp)" for the Apr-2024 (Q4 FY24) transcript; the actual PDF-page-marker count in both files runs one page higher (12 and 16 respectively, matching the page counts given in the audit brief), because B06 appears to be counting the transcript's own internal "Page X of N" footer (which excludes the BSE covering letter) rather than total PDF pages. Does not affect any individual anchor, since every citation I checked matched its stated "===== PAGE n =====" marker correctly. |
| 6 | MINOR (unused, relevant) | WINDMACHIN CSV, Cash from Operating Activity (row 57) | Not cited: FY25 OCF -Rs2.4 Cr, FY26 OCF -Rs59.09 Cr, sharply negative and worsening despite the +72.9% FY26 sales growth used as a corroborating "second growth signal" in Claims 1 and 6. This datum would have reinforced, not contradicted, B06's own existing "possibly inorganic, treat as caveated context only" framing, so it does not change any verdict, but it was available in the same CSV and directly bears on how much weight the WINDMACHIN growth signal deserves. |
| 7 | MINOR (unused, relevant) | WINDMACHIN CSV, Borrowings (row 41) | Not cited: Borrowings rose from Rs34.86 Cr (FY25) to Rs86.04 Cr (FY26), +147%, alongside the already-discussed equity raise and Investments spike. An additional financing-mix data point for the same "possibly inorganic vs. organic capex" question Claim 6 raises; omission is minor since it would not change the conclusion already reached. |
| 8 | MINOR (unused, relevant) | RAJOOENG Q2 FY25, PDF p.8-9 (Aditya Shah exchange) | "These are the advance against order booking" (re: Rs127 Cr reserve/surplus) is a second, later (Oct-2024) corroboration of the order-linked-advance working-capital model used for Claim 10, sourced from the Q2 FY25 call rather than the already-cited Q2 FY24 call. Not cited. Duplicative of already-strong Claim 10 evidence, so immaterial to the verdict; noted for completeness only. |

**Critical count: 0. Major count: 1. Minor count: 7.**

No fabricated citation was found anywhere in this rerun. No peer was mismarked SUBSTANTIVE without real supporting text. No claim in the injected peer_questions list (all ten, nine original plus the rerun addition) was skipped. The single MAJOR finding is a verdict-taxonomy discipline issue (Claim 10 should read PARTIALLY VERIFIED, not VERIFIED), not a fabrication or an unfindable anchor.

---

## PART 4: ACCEPTANCE-RATE BASIS

Peers audited (peer-coverage-map rows): 6 (RAJOOENG x4 quarterly calls, HBLENGINE x1, WINDMACHIN x1 screener-only).
Peers correctly handled: 6 of 6 — every SUBSTANTIVE citation checked was genuine and locatable at (or immediately adjacent to, within the tolerances noted above) its stated anchor; the CITED-ONLY WINDMACHIN entry was used with the caveats a non-filing, unaudited screener source requires (explicitly flagged as unanchored to any filing, explicitly excluded from claims it cannot test (Claim 5), and explicitly labeled a "possibly inorganic" signal rather than treated as confirmed fact).
Acceptance rate: 100% (6/6 peers correctly handled at the coverage/citation-fidelity level). The one MAJOR finding (Claim 10 verdict discipline) is a claim-level taxonomy fail under Rule 4, tracked separately in `verdict_discipline_fails`, and does not itself represent a mishandled peer source.

---

```yaml
stage: B12d
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
rerun: 2
status: complete
peers_audited: 6
substantive_confirmed: 5
substantive_unsupported: []
unused_but_relevant:
  - {peer: "WINDMACHIN", missed_item: "Cash from Operating Activity sharply negative and worsening (FY25 -Rs2.4 Cr, FY26 -Rs59.09 Cr) despite the +72.9% FY26 sales growth cited as a corroborating signal in Claims 1 and 6", anchor: "WINDMACHIN-Data_Sheet.csv, row 57, columns 2025-03-31/2026-03-31"}
  - {peer: "WINDMACHIN", missed_item: "Borrowings rose Rs34.86 Cr (FY25) to Rs86.04 Cr (FY26), +147%, an additional financing-mix data point for the Claim 6 organic-vs-inorganic capex question", anchor: "WINDMACHIN-Data_Sheet.csv, row 41, columns 2025-03-31/2026-03-31"}
  - {peer: "RAJOOENG", missed_item: "Second, later corroboration of order-linked advance working-capital model ('these are the advance against order booking', re: Rs127 Cr reserve/surplus), duplicative of Claim 10's existing Q2 FY24 anchors so immaterial to the verdict", anchor: "RAJOOENG Q2 FY25, 22-Oct-2024, PDF p.8-9"}
claims_all_addressed: true
verdict_discipline_fails:
  - {claim: "Claim 10 (Rajoo working-capital terms vs KABRAEXTRU receivable ageing)", issue: "Verdict recorded as VERIFIED resting on a single peer (RAJOOENG), three anchors all from that one peer; per Verifier D Rule 4 a VERIFIED resting on one peer is MAJOR and should be PARTIALLY VERIFIED. B06's own text notes the classification is atypical but does not relabel the verdict field.", severity: "MAJOR"}
findings:
  - {severity: "MAJOR", location: "Claim 10 verdict (B06 report + B06 YAML verified: block)", claimed: "VERIFIED", note: "Single-peer VERIFIED violates Rule 4; should be PARTIALLY VERIFIED", source_fidelity: false}
  - {severity: "MINOR", location: "Claim 5, '73-74% of H1 FY25 revenue' composite figure", claimed: "PDF p.12 for both 73% and 74%", note: "74% is actually stated on PDF p.10 (a different, quarterly-only Q&A exchange); 73% and the accompanying quote are correctly on p.12", source_fidelity: false}
  - {severity: "MINOR", location: "Claim 6, facility-inauguration anchor", claimed: "PDF p.2-3", note: "Quote is located entirely on PDF p.3; p.2 does not contain it", source_fidelity: false}
  - {severity: "MINOR", location: "Claim 4 / Part 2E(i), Red Sea shipping crisis anchor", claimed: "PDF p.6-7", note: "Quoted material is located entirely on PDF p.7", source_fidelity: false}
  - {severity: "MINOR", location: "B06 'Sources Re-Read' page-count metadata for Nov-2023 and Apr-2024 transcripts", claimed: "11pp and 15pp respectively", note: "Actual PDF-page-marker counts run one higher (12pp, 16pp); appears to be an internal-footer vs total-PDF-page counting convention difference; no anchor affected", source_fidelity: false}
critical_count: 0
major_count: 1
minor_count: 7
acceptance_rate: 100
```
