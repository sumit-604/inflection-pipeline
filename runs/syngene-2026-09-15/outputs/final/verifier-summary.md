=== FILE: verifier-summary.md ===

# Verifier summary, phase 1 (SYNGENE 2026-09-15)

Findings of record are the final verifier run (run 2), after one correction cycle. Verifier C scope is phase 1 only: Gate 0 and Emerging Moat. Valuation adherence, the expectation ledger and the business understanding narrative are PENDING PHASE 3.

## Confidence delta (phase 1)

| Component | Run 2 (of record) | Run 1 | Source |
|---|---|---|---|
| numerical_acceptance | 96.6 | 89 | B12a |
| redflag_coverage | 67 | 38 | B12b |
| framework_adherence (phase 1 portion) | 85 | 80 | B12c |
| peer_utilisation | 83 | 100 | B12d |
| overall (min of four) | 67 | 38 | confidence.yaml |

Band: 60 to 74, PROCEED verdicts downgrade one level. Rework gate: NOT TRIGGERED in run 2 (Verifier A CRITICAL count 0; no acceptance rate below 60).

## Acceptance rates and counts (run 2)

| Verifier | Model | Checked | CRITICAL | MAJOR | MINOR | Acceptance |
|---|---|---|---|---|---|---|
| A numerical | claude-haiku-4-5 | 62 numbers | 0 | 2 | 2 | 96.6 |
| B red flags | claude-opus-5 | 39 independent flags (26 caught, 10 partial) | 1 | 3 | 18 | 67 |
| C framework, phase 1 | claude-opus-5 | Gate 0 48 rules, Emerging Moat 32 rules | 0 | 1 | 10 | 85 |
| D peers | claude-sonnet-5 | 6 peer transcripts | 0 | 1 | 1 | 83 |

## Findings, sorted by severity

### CRITICAL

| # | Verifier | Location | Finding |
|---|---|---|---|
| C-1 | B | B05 repeated_evasions / red_flags / 1B margin bridge | MISSED repeated evasion: Bayview and Unit 3 cost drag unquantified across calls; capitalization deferral keeps Bayview cost off FY27 P&L. Anchors: Q2FY26 Shyam Srinivasan/Deepak Jain PAGE 8; Q4FY26 Kunal Dhamesha/Deepak Jain PAGE 7; Q1FY27 Neelam Punjabi/Siddharth Mittal PAGE 13; Q4FY26 Deepak Jain PAGE 5. Status: not corrected upstream; carried to the gate recommendation and Halt 1. |

### MAJOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| M-1 | A | 05-concall.md, Section 1B promise/delivery table, FY26 row | Claimed "free cash Rs 521cr"; source truth Rs 547.0cr (CFO 915.2cr less capex 368.2cr), filed consolidated cash flow p.8. Figure does not appear in the 01-gate0.md operative scorecard. source_fidelity: true. Disposition: FLAG CLEARED on source recheck (see disagreement table). |
| M-2 | A | 05-concall.md, Section 1B guidance table, FY26 row | Claimed "closing net cash Rs 1,800cr"; source truth Rs 773.1cr net cash or Rs 833.0cr gross cash (results FY26 p.6). Verify against the Q4 FY26 transcript for a gross cash or timing adjusted basis. source_fidelity: true. Disposition: FLAG CLEARED on source recheck (see disagreement table). |
| M-3 | B | B05 promise row 8 / timeline_slippages / trigger 1 | MISSED Librela duration slip (FY26, then a couple of quarters of FY27, then end FY27) and the Zoetis two year inventory admission; B05 row 8 says no contradiction yet. Anchors: Q2FY26 Deepak Jain PAGE 11; Q3FY26 Peter Bains PAGE 14; Q4FY26 Peter Bains PAGE 8, PAGE 11; Q1FY27 Siddharth Mittal PAGE 10. |
| M-4 | B | B05 2B / trigger 4 | Attrition cause stated as both voluntary opt out and involuntary price loss in one call; B05 scores it honest admission. Anchors: Q1FY27 Siddharth Mittal PAGE 4-5; Kiran Mazumdar-Shaw PAGE 2, PAGE 7, PAGE 9. |
| M-5 | B | B06 item 5 | Bayview slip benchmarked against peer greenfield build durations; against their own guidance peers slip 1 to 4 months, against Bayview's ~12 months on an acquired, validated site. Anchors: Syngene Q3FY26 PAGE 4, PAGE 10; SAILIFE PAGE 12; ANTHEM Nov-25 PAGE 6, Jul-26 PAGE 9; PPLPHARMA PAGE 12. |
| M-6 | C | 07-emoat.md 6E moat evolution map; Section 3 B2/C1; 4C | Gate 0 confirmed moats misstated as BMS/dedicated centres plus regulatory licence; B01 confirmed M4 and M10 only, M7 = 0. Rationale sources to B04, not an injected stage 7 input; 4C exclusion applied to BMS but not to the Unit 3 USFDA VAI row scored in A1. Recomputed: existing (Gate 0, 2 confirmed) M4 Customer Stickiness (3), M10 Switching Costs (5); no score change. |
| M-7 | D | B06 Part 1 item 5 / 06-peers.md line ~95 | "won't be in the profitable zone" and "15% utilization in FY26" both cited to ANTHEM-Nov-2025 p.4. Source truth: the quote is on marker PAGE 5; the 15% figure is not in ANTHEM-Nov-2025 and appears in ANTHEM-Jul-2026 p.4. Residual anchor drift the correction log claimed to remove; no verdict flip, since the same fact is correctly anchored via Jul-2026 p.4 in the same sentence. |

### MINOR

| # | Verifier | Location | Finding |
|---|---|---|---|
| m-1 | A | 05-concall.md, LBF1 verification section | Claimed "PAT before exceptional Rs 1cr"; source truth PBT before exceptional -5.7cr consolidated or +3.5cr standalone (results Q1FY27 p.2-3). Directionally consistent, not reproducible as an exact filed figure; PARTIAL CONFIRMATION appropriate. source_fidelity: true. Disposition: GATE HELD (management stated only). |
| m-2 | A | 05-concall.md, Section 1B guidance table, Q1FY27 row | Claimed "Q1FY27 net cash Rs 1,541cr"; UNANCHORED, the Q1FY27 balance sheet is not in the extracted results file. Does not affect operative scorecards. source_fidelity: true. Disposition: FLAG CLEARED on source recheck (Concall_Jul_2026_Transcript.pdf p.5). |
| m-3 | B | B05 3C / promise row 7 | Retroactive FY26 base restatement ("declining since last year" against "momentum intact") not logged; Bino answer mis-scored as most transparent. Anchors: Q4FY26 PAGE 2, PAGE 6; Q1FY27 PAGE 2, PAGE 9. |
| m-4 | B | B05 red flags | FY26 margin beat explained as cost frugality to one analyst and as mix plus exceptional reclass to another. Anchors: Q4FY26 PAGE 7; PAGE 10-11. |
| m-5 | B | B05 2E | Q3FY26 "did it surprise you" and "slower vs peers" dodges not logged. Anchors: Q3FY26 PAGE 14, PAGE 15. |
| m-6 | B | B05 2D / B06 item 2 | Magnitude called unverifiable though the mix bounds research services at about -6% QoQ [INFERENCE]; CDMO share 41% to 22% not analysed. Anchors: Q4FY26 PAGE 8; Q1FY27 PAGE 5. |
| m-7 | B | B05 1B | Rs 50cr hedge loss (55% of Q1FY27 EBITDA [INFERENCE]) and undisclosed hedge book not carried into the H2 margin requirement. Anchors: Q1FY27 PAGE 5, PAGE 9. |
| m-8 | B | B05 2E | Clinical trial revenue refused in three calls, not in the repeated evasion tracker. Anchors: Q2FY26 PAGE 14; Q4FY26 PAGE 7; Q1FY27 PAGE 9. |
| m-9 | B | B05 2E rows 1-2 | Quarter counts understated; segment growth and medium term outlook evasions each span four calls. Anchors: Q2FY26 PAGE 12-13; Q4FY26 PAGE 12; Q1FY27 PAGE 6-7. |
| m-10 | B | B05 1C / dropped_triggers / peer question 4 | Funding "named headwind" rests on analyst wording only; management said broadly favorable. Anchors: Q4FY26 Harith Ahamed PAGE 12; Q3FY26 Peter Bains PAGE 14. |
| m-11 | B | B05 2E row 4 | Lenivia update promised for full year and delivered; stronger evidence is Q3 "working with our collaborating partner on that". Anchors: Q3FY26 PAGE 16; Q4FY26 PAGE 12. |
| m-12 | B | B05 1C / red flag LOW | India regulatory statements are tension, not a flat reversal. Anchors: Q2FY26 PAGE 10; Q1FY27 PAGE 12. |
| m-13 | B | B05/B06 Bayview date | "by end of this year" anchor on PAGE 6 attaches to discussions; clean anchor is PAGE 12. Anchors: Q1FY27 PAGE 6, PAGE 12. |
| m-14 | B | B05 promise row 4 | BMS extension is a disclosed fact, not a promise pair; inflates the delivered count. Anchor: Q3FY26 PAGE 3. |
| m-15 | B | B05 corrections item 19 / promise row 5 | Revenue decline and attrition disclosure attributed to Kiran Mazumdar-Shaw; speaker was Siddharth Mittal. Anchor: Q1FY27 PAGE 4-5. |
| m-16 | B | B06 item 4 | Discovery revenue conversion evidenced by SAILIFE only; ANTHEM growth is manufacturing led (refer Verifier D). Anchors: ANTHEM May-26 PAGE 15; SAILIFE PAGE 6. |
| m-17 | B | B06 risks_peers_raise | Rs 146cr is an analyst asserted accumulated loss, not a management confirmed unrecognized tax loss. Anchor: PPLPHARMA PAGE 18-19. |
| m-18 | B | B06 Part 2 | MISSED PPLPHARMA single customer destock context (no sales expected this fiscal), peer context for Librela duration. Anchor: PPLPHARMA-Concall_Jul_2026 Alankar Garude/Peter DeYoung PAGE 14-15. |
| m-19 | B | B06 2E(ii) | Peer multi year repositioning and AI hype evidence runs against Syngene's within FY27 turnaround claim; B06 calls it a parallel. Anchors: SAILIFE PAGE 6; ANTHEM Jul-26 PAGE 15; Syngene Q1FY27 PAGE 7. |
| m-20 | B | B06 item 5 / B05 2E row 5 | ANTHEM unit utilization disclosure not used as contrast to the Mangalore evasion. Anchors: ANTHEM Jul-26 PAGE 4; Syngene Q2FY26 PAGE 8. |
| m-21 | C | 07-emoat.md Section 5 row E1; Section 3 E1 | E1 scored INFER 0.5 against DOC tier; residual evidence (Bayview site exists) duplicates A1. Recomputed: E1 1.0 (total 19.6) or 0 (total 18.6); MODEST unchanged. Rule fails E-F3 and E-F3b, single finding. |
| m-22 | C | 07-emoat.md Section 5 rows B2, C1 | Weak rows scored raw 2, same as Moderate rows; conflicts with log item 6 logic. Recomputed: raw 1 each; total 17.1 (or 16.6 with E1 at 0); MODEST unchanged. |
| m-23 | C | B07-emoat.yaml evidence_mix, completionist_recount | 3 CLAIM / 2 INFER does not reconcile to Section 3 rows. Recomputed: at least 4 CLAIM (B2 Amgen, D1, E2 x2), 1 INFER (A3) on Section 3 as written; E1 listed as DOC but scored INFER; 23 row total counts R1 from Section 4. |
| m-24 | C | 07-emoat.md 1A, 1C, 2A, 2D, C2, G2, H3 | Rule 3 anchors: approximate pages (p.~9, p.~50, p.~52, p.~85, p.~217); line number residue "p.242/15706" in 2A; pipeline block anchors used in place of document pages. |
| m-25 | C | 07-emoat.md 1B, 1C, 2A; B07 input_gaps | NOT FOUND discipline: estimate (B04 single segment 61%/39%) in the 1C number cell; out of corpus $36.5mn retained; seller name retained while marked removed; conflicts with the B01 note 8 citation (fidelity to Verifier A). |
| m-26 | C | 01-gate0.md Deal-breakers; B01 deal_breakers | No years named for deal-breaker 1. Recomputed driver: FY26 ROCE 8.35% (A2, A4); window FY24 to FY26. |
| m-27 | C | B01 analyst_note | M1 described as peer relative. Recomputed: M1 is an own history margin trend (FY18 33.29% to FY26 24.64%), -8.65pp. |
| m-28 | C | B01-gate0.yaml | Non schema key "run: 2"; the block and the embedded YAML in 01-gate0.md differ. |
| m-29 | C | 01-gate0.md Block A table, FY24 row | Rule 4 anchors: AR2025 page missing for FY24 total current liabilities ("AR2025 p. consol BS"); fidelity owned by Verifier A. |
| m-30 | C | 01-gate0.md output | Dashboard format: moat profile bars required by the output spec are absent (table only). |
| m-31 | D | B06 Part 2E / risks_peers_raise | Only the negative Piramal overseas subsidiary tax loss comparator is used against Bayview. SAILIFE-Aug-2026 p.15 discloses a positive comparator (Boston, "a bit accretive", ~30-35% discovery revenue CAGR since ~2020) not incorporated. Industry context miss under Rule 3; would sharpen, not change, the analysis. |

## Verifier notes recorded alongside the findings

| Verifier | Item | Recorded note |
|---|---|---|
| A | Coverage | 87% of material numbers in nine stage reports verified. Verdict card figures 100% audited. Scorecard inputs (Blocks A to E) 100% audited. Table cells 85% audited. All unit conversions checked. |
| B | Promise delivery spot checks | 5 checked, 5 confirmed, 0 wrong. |
| B | Credibility grade | Concur with D: two post miss guidance cuts, an unacknowledged ~12 month Bayview slip and multi quarter evasions; BMS, the met FY26 margin guide and Q1FY27 candor keep the record from being uniformly negative. |
| B | Pipeline flags not supported | None. |
| C | Observation G-O4 (not counted) | Gate 0 data confidence tier keys to the 9 year "data available" per the prompt text; a shortest window reading (3 year ROCE, B2 to B4) would give LIMITED and move AVERAGE to AVOID; the prompt does not support it; operator ruling candidate. |
| C | Observation G-O1 (not counted) | M3 on median ROCE would score 1 (moat 11, grand total 67); no class change. |
| C | Observation E-O1 (not counted) | Section 5A Undiscovered Alpha qualifier wording deferred to phase 3. |
| D | Citation spot check | 33 of 34 citations land on the cited page marker. |
| D | Claims and verdict discipline | All claims addressed; no verdict discipline fails; no substantive usage unsupported. |

## Run 1 and the correction cycle

Run 1 acceptance: A 89, B 38, C 80 (phase 1 scope), D 100. Overall 38. Verifier B below 60 forced REWORK unless corrected, so one correction cycle ran.

- Verifier A run 1: one CRITICAL, FCF FY26 Rs 547.0 Cr and FY25 Rs 397.5 Cr called "10x overstated". Cleared on arithmetic of the verifier's own source truth: 5,470mn equals Rs 547.0 Cr. One MAJOR: FY26 employee cost, AR Rs 12,297mn against consolidated P&L Rs 11,049mn. It stays open for Halt 1, because stage 4 was not re-run. Four MINORs.
- Verifier B run 1: one CRITICAL (the Zoetis follow on molecule Lenivia evasion), 11 MAJOR, 13 MINOR.
- Verifier C run 1: four MAJORs (A1 misband; a 2 year window on B2, B3, B4 and M12; company memory anchors in B07; BMS credited three times), 12 MINOR.
- Verifier D run 1: three MAJORs (misattributed SAILIFE 4 to 5% figure; spurious ANTHEM Nov-2025 anchor; systemic anchor drift on about 13 of 24 citations).

What the cycle changed. Stages 1, 5, 6 and 7 re-ran, then all four verifiers re-ran.
- Stage 1: Block A fell from 7 to 5. Block B rose from 18 to 20 on a corrected 3 year window, FY24 to FY26. Grand total moved from 67 to 66, and the classification stayed AVERAGE. FCF was reconfirmed against the FY26 audited cash flow statement p.8.
- Stage 5: credibility moved from C to D. The Lenivia evasion was added. The Bayview "no firm date" claim was corrected to a stated end FY27 target. The FY26 margin beat was reframed as partly a reclassification into exceptional items.
- Stage 6: anchors were re-marked to PDF page markers. The research commoditisation contradiction was scoped to direction only, because the Q1 FY27 16% fall is total company revenue. The Labour Code gap was removed, and the tariff and BIOSECURE test was reframed as secondary.
- Stage 7: the triple BMS credit was collapsed to one mechanism. The emerging moat score fell from 23 to 19, still MODEST, now 0 Strong and 4 Moderate. Page citations were corrected.
- Overall confidence moved from 38 to 67. Run 2 left one Verifier B CRITICAL open (C-1 above).

## Verifier disagreement table (phase 1)

| Date | Run (ticker-date) | Number/claim | Verifier A verdict + anchor | Downstream step + its position | Disposition | Note |
|---|---|---|---|---|---|---|
| 2026-09-15 | SYNGENE-2026-09-15 | FCF FY26 Rs 547.0 cr, FY25 Rs 397.5 cr (01-gate0 Block B) | Run 1 CRITICAL, "10x overstated"; source_truth CFO 9,152mn less capex 3,682mn = 5,470mn (FY26 audited CF p.8) | Stage 1 held the figure; stage 1 run 2 re-confirmed at FY26 audited consolidated CF p.8 | FLAG CLEARED: source recheck found the number at a correct anchor (rechecked by orchestrator arithmetic and stage 1 run 2) | 1 crore = 10 million, so 5,470mn = Rs 547.0 cr. The verifier mis-converted units. Run 2 raised no finding. |
| 2026-09-15 | SYNGENE-2026-09-15 | "free cash Rs 521 cr" FY26 (05-concall guidance table) | Run 2 MAJOR, source_truth Rs 547.0 cr CFO less capex | Stage 5 quoted management | FLAG CLEARED: source recheck found the number at a correct anchor (rechecked by orchestrator: Concall_Apr_2026_Transcript.pdf p.3 "generated a healthy INR521 crores in free cash"; 2026-04-29 press release p.1 "Net cash generated during the year was Rs. 521 Cr") | Two bases: management's net cash generated Rs 521 cr against CFO less capex Rs 547.0 cr. Label both; neither is wrong. |
| 2026-09-15 | SYNGENE-2026-09-15 | "closing net cash Rs 1,800 cr" at 31-Mar-2026 (05-concall) | Run 2 MAJOR, source_truth Rs 773.1 cr net cash or Rs 833.0 cr gross cash (FY26 results p.6) | Stage 5 quoted management; B03 cites Rs 18,003mn consolidated net cash | FLAG CLEARED: source recheck found the number at a correct anchor (rechecked by orchestrator: Concall_Apr_2026_Transcript.pdf p.3 and p.6) | Management's net cash includes treasury investments; balance sheet cash and bank is a narrower measure. Label the basis wherever used. |
| 2026-09-15 | SYNGENE-2026-09-15 | Q1FY27 net cash Rs 1,541 cr (05-concall) | Run 2 MINOR, UNANCHORED | Stage 5 quoted management | FLAG CLEARED: source recheck found the number at a correct anchor (rechecked by orchestrator: Concall_Jul_2026_Transcript.pdf p.5) | Management stated; no Q1 balance sheet in the results filing. |
| 2026-09-15 | SYNGENE-2026-09-15 | Q1FY27 PAT before exceptional Rs 1 cr | Run 1 and run 2 MINOR, not reproducible from filed subtotals | Stages 1 and 5 marked it partial confirmation | GATE HELD: figure kept only as management stated with its anchor (Concall_Jul_2026_Transcript.pdf p.5) and flagged not reproducible from the filed P&L | Filed PBT before exceptional: -Rs 5.7 cr consolidated, +Rs 3.5 cr standalone (Q1FY27 results p.2-3). |
| 2026-09-15 | SYNGENE-2026-09-15 | FY26 employee cost 32.9% of revenue (04-bizmodel) | Run 1 MAJOR: AR states Rs 12,297mn; consolidated P&L shows Rs 11,049mn | Stage 4 not re-run; run 2 did not re-raise | OPEN: carried to Halt 1 as an unreconciled basis gap | Not used in any score. Resolve before any margin bridge uses employee cost. |
