# A4 MERGED REVIEW: Fedbank Financial Services Ltd (FEDFINA), Q2 FY27 (quarter ended 30 Sep 2026)

Agent: A4 analyst | model: claude-opus-5-5 | run date: 2026-10-17 | revision: Role 5 merge 2026-10-19, onto the audited Role 4 (correction loops 1 and 2, A5 audit work/audit_fedfina_q2fy27.md); Role 5 correction loop 1 2026-10-19 (A5 audit work/audit_concall_fedfina_q2fy27.md); Role 5 correction loop 2 2026-10-19 (A5 C7, work/blocks/a5-concall.yaml)
Run type: FULL QUARTER, Role 4 (Quarterly Results Review Protocol v1.4) + Role 5 (Quarterly Concall Analysis Protocol v1.1). Role 4 stands as audited. Role 5 runs on the concall in the section after Step 9.
Lender variant: Steps 1L and 5L replace Steps 1 and 5. Step 7 uses the lender rows. Role 5 uses Step 2L. Role 4 Steps 6.5 and 7 and Role 5 Step 8D are deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts are flagged in Role 4 Section 7 and Role 5 Step 8D.
Docs merged: results filing (Reg 33/52, 15 pages), investor presentation (42 slides), press release (3 pages), Q2 FY27 earnings-call transcript (machine transcript of company audio, 68m32s, 74 turns).
Inputs read: A1 structured files (all rows, four documents), A1 fulltexts at cited lines (concall fulltext read in full), A2 ledgers (all four; concall ledger as updated in A2 loop 1), A3 forensics (all four), orchestrator extraction check (work/orch-check/extraction-check.md), Notion live copy (work/notion-thesis.md, including the Q1 FY27 promise log and Questions table), A5 audits (Role 4 loops 1 and 2; Role 5 concall audit). The source PDFs, the source audio and inputs/ were not opened.
Concall source caveat: the transcript is ASR output with no speaker labels. A1 inferred the speaker in 52 of 74 turns. Garbled passages sit at Call L133-135, L152-153, L420 (auction-loss negation), L736 (ROE target number) and L826. Every conclusion that rests on them carries [ASR].

Anchor convention: "Res R###" = results structured row (line Lnnn in results fulltext); "Deck R###" = presentation row; "PR R###" = press-release row; "XC" = orchestrator extraction check; "Call L###" = concall fulltext line; "Call R###" = concall structured row; "MFS-C##" = concall ledger row added by A2 loop 1 with no A1 ID; "T##" = A2 concall ledger turn. Concall A3 findings use the hyphenated form FN-01 to FN-21; presentation A3 findings use the unhyphenated form FN01 to FN25. Concall commitment register rows are C01 to C26. "derived" = A4 arithmetic on filed numbers; it is never an estimate.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 38 notes / 74 turns / 45 slides. All 38 notes / 74 turns / 45 slides reviewed.
- Results ledger: 748 of 748 IDs, plus 4 rows A2 adds in loop 1 (752 rows). 36 notes and footnotes, 339 line-item groups plus 2 NOT DISCLOSED blank rows, 38 ZERO_STANDING rows, 6 agenda items, 19 auditor paragraphs, 38 entities, 7 signature blocks (was 5). MFS-1/2/3 noted (agenda enclosure prose, garbled UDINs). gate_a2 pass.
  - Loop 1 additions, each read at its fulltext line: Res L525 "Aggregate principal outstanding of loans transferred" (blank cell, NOT DISCLOSED); Res L526 "Weighted average residual tenor of the loans transferred" (blank cell, NOT DISCLOSED); Res L812 Annexure I company signature block; Res L932 (mark L934) Annexure II company signature block. Content already covered at Note 10(I) and Q13. No new finding.
- Presentation ledger: 1,102 of 1,102 IDs, 42 slides (5 text-only dividers), 37 footnotes, 1 ZERO_STANDING row (R1024). gate_a2 pass.
- Press-release ledger: 247 of 247 IDs, 3 pages, 2 notes/qualifier footnotes, 0 ZERO_STANDING. gate_a2 pass.
- Concall ledger (as updated in A2 loop 1): 267 of 267 IDs (R001-R267), 0 orphans, plus 21 MFS rows with no A1 ID (MFS-C1 to C21: 4 management numbers, 9 forward phrases, 1 date and 1 qualifier counted; 4 repeats and 2 time references listed, not counted). 17 participants (7 management including 3 named non-speakers R157-R159, 1 host, 9 analysts), 74 turns (52 SPEAKER_INFERRED; 9 MIXED_TURN: T22, T26, T33, T47, T50, T51, T54, T62, T71), 26 questions (9 primary, 14 follow-up, 3 embedded in mixed turns T47, T50, T51), 141 management numbers on A1 rows (149 NUMBER rows less 8 analyst or moderator rows; R121-R123 re-attributed to management, R130-R131 to analyst) and 145 with the four MFS numbers, 58 forward phrases (49 A1 + 9 MFS), 22 qualifiers, 35 entities, 14 dates, 1 ZERO_STANDING (R100). A1 header said 73 turns; the index holds 74 (header discrepancy, not a missing unit). gate_a2 pass. Every row, A1 and MFS, was read at its fulltext line. No A3 re-run is needed: the new units at Call L113, L482-L483 and L715-L716 support FN-05, FN-09 and the branch-breakeven qualifier and raise no new finding.
- Unreviewed rows: none.

Findings incorporated:
- Results (17): A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17.
- Presentation (25): FN01 to FN25.
- Press release (13): FND-01 to FND-13.
- Concall (21): FN-01 to FN-21 (FORWARD-SIGNAL: FN-02, FN-03, FN-05, FN-06, FN-08, FN-09, FN-10, FN-11, FN-12, FN-13; AMBIGUOUS: FN-01, FN-04, FN-07, FN-14, FN-17, FN-18, FN-20, FN-21; CONFIRMATORY-NEGATIVE: FN-16, FN-19; NEUTRAL-FACT: FN-15). Concall commitment register C01 to C26 and silence audit S01 to S10 incorporated.

Extraction corrections adopted (A1 rows differ; values used are the confirmed ones, both cited). A5 tested each by internal ties; all hold.
| Item | A1 row value | Value used | Basis |
|---|---|---|---|
| FVOCI Loans OCI Q1 FY27 | Res R134 15,851 | (5,851) lakh = Rs (58.51) Cr | XC p5; A3 Section 0 tie-out |
| FVOCI Loans OCI Q2 FY26 | Res R135 12,005 | (2,005) lakh | XC p5 |
| FVOCI Loans OCI H1 FY27 / H1 FY26 | Res R136 16,470 / R137 1,783 | (6,470) / (783) lakh | XC p5 |
| OCI reclassified total Q1 FY27 / Q2 FY26 / H1 FY27 / H1 FY26 | Res R158-R161 | (4,397) / (1,237) / (1,883) / (457) lakh | XC p5 |
| Cash-flow hedge Q1 FY27 | Res R146 (271) | (271) lakh (text layer "1271)") | XC p5 |
| Deferred tax H1 FY26 | Res R101 (170) | (70) lakh | XC p5 |
| Slide 22 MT LAP disbursals FY22-FY26 | Deck R460-R464 518/1,091/1,359/2,180/2,303 | 518 / 1,091 / 1,359 / 2,303 / 2,180 | XC s-22; FN13 |
| Slide 22 ST LAP & HL disbursals FY22-FY26 | Deck R455-R459 765/904/1,004/1,102/1,475 | 765 / 1,102 / 1,475 / 1,004 / 904 | XC s-22; FN13 |
| Slide 25 yields Q1 FY27 / Q2 FY27 | Deck R560 16.7 / R561 16.4 | 16.4% / 16.7% | XC s-25; FN23 |
| Slide 25 CoB vs Spread series (all 10 periods) | Deck R562-R581 (A1 and A3 FN25 read CoB Q2 FY27 = 8.8%) | CoB Q2 FY27 7.9%, Spread Q2 FY27 8.8% (full series below) | XC s-25 label positions. A1 swapped the spread and CoB series. Yield = CoB + spread is symmetric, so A3's identity test could not separate them. |

Consequence of the slide 25 correction: A3 FN25 ("slide 25 CoB 8.8% does not reconcile to P&L 7.87%") dissolves. Slide 25 CoB is 7.9% (XC), which agrees with the P&L-implied 7.87% (FN25 derived) and the I-GAAP daily 7.79% (Deck R610). FN25 keeps one question row on series basis.

Second consequence (Role 5 merge): the concall A3 file cites the uncorrected slide 25 rows. FN-06 says the deck spread "already narrowed about 50 bps QoQ" (yield 16.7% to 16.4%, CoB 8.6% to 8.8%). FN-07 says the CFO's yield claim has the "opposite sign" to the deck. On the XC values, yield rose 16.4% to 16.7%, CoB rose 7.7% to 7.9%, and spread widened 8.6% to 8.8%. Both direction legs dissolve. FN-06 keeps its forward signal on management's own words. FN-07 keeps two legs: CoB basis selection, and a level leg (the spoken 16.40 core yield ties only to the Q1 reported yield; ex-DA core derives to about 16.7% in both quarters, Role 5 Step 7A). FN-15's drift count stays at four: the yield-direction drift dissolves and the core-yield level drift replaces it.

---

## STEP 0 PRE-FLIGHT

### 0A. Notion baseline (live copy 2026-10-17, page 39fbb2b9-d3ab-81d9-b09d-dd45266d56c2, last edited 2026-09-30)
- Decision Status: **WATCHLIST / AVOID (DEEP WATCH)**. Verified before framing. Not held. Position branch: **8A-W**.
- Entry zone Rs 68-77; MoS Rs 61. CMP property 164 is stale (about Rs 157 on 23-Aug-2026). Position size: Small (ceiling only, not active).
- Destination PE Track 1 14.3x mid (13.0-15.5), Track 2 15.3x; sector cap 18x; Hurdle STOP (1.21 vs 1.953). FV 3yr bear 117 / base 150 / bull 186.
- Pillar 2L: operator override 1.00x (from 0.80x). Self-withdraws to 0.80x if credit cost > 1.1% or PCR thins further.
- Tripwires: (1) credit cost > 1.1% of average assets; (2) ROE fails to cross 14% by FY28; (3) PCR below 32%.
- Monitoring checklist: 8 items (Step 6B).
- Bear/Base/Bull P&L projections: ND (not on the page). Other pillar point values: ND (not passed).
- Prior Questions-for-Management: 10 rows (Q1 FY27) plus AR top 3. Status table in Step 1L-b below.

### 0B. Units
Results filing: INR Lakhs (Res R693, L208), except Annexure I security cover in INR crore (Res R739, L818). Converted to Rs Crore at x0.01. Presentation and press release: Rs Cr as printed (Deck R097; PR fulltext L79). Concall: crores as spoken (Call header L12).

### 0C. Share count changes
- Note 5: 2,35,701 shares allotted on ESOS exercise in Q2 FY27 (Res R369, L429). Note 4: no grants in Q2 (Res R371).
- Paid-up capital Rs 374.21 Cr (Mar-26, Res R174) to Rs 374.91 Cr (Jun-26, Res R170) to Rs 375.14 Cr (Sep-26, Res R169). About 37.51 Cr shares (37,51,41,782 per Notion AGM record).
- No split, bonus, rights, QIP or buyback. Share-adjusted EPS = reported EPS, except the Q2 FY27 basic EPS misprint (A3-10; see 1L).
- ESOP 2024 amendment passed at the 29-Sep-2026 AGM with 25.54% of institutional votes against (Notion). Dilution watch only.

### 0D. Notes extraction (mandatory)

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| 1 | Basis of preparation | Ind AS, Reg 33, Reg 52(4) r/w 63, SEBI circular (Res R697, L414). | Nil | All | None |
| 2 | Approval and review | Board approved 15-Oct-2026 after Audit Committee; limited review by joint auditors (Res R698, L421). | Nil | Q2 FY27 | First joint review. Comparatives reviewed by KKC alone (Other Matter, Res R727, L168-175; A3-03). |
| 3 | Secured NCDs | Rs 278.75 Cr secured NCDs, first pari passu charge, minimum cover 1.10x (Res R367-R368, L423). | Rs 278.75 Cr outstanding | Sep-26 | None. Actual cover 1.24x (Res R519, L803). |
| 4 | ESOS grants | No options granted under ESOS 2024 or 2018 in the quarter (Res R371, L426). | Nil | Q2 FY27 | None |
| 5 | ESOS allotment | 2,35,701 shares of Rs 10 allotted (Res R369, L429). | Rs 0.24 Cr capital | Q2 FY27 | EPS denominator +0.06% |
| 6 | Subsidiaries | No subsidiary, associate or JV at 30-Sep-2026 (Res R372, R702, L432). | Nil | All | Standalone only. S-vs-C gap 0%. |
| 7 | Segment | One segment, lending (Res R703, L434). | Nil | All | Product split only from the deck. |
| 8 (i) | Resolution framework 2020-21/16 | Personal-loan resolution exposure 4,697 lakh to 4,221 lakh; 91 lakh slipped to NPA; 385 lakh repaid; nil written off (Res R373-R385, L439-465). | Rs 46.97 Cr to Rs 42.21 Cr; Rs 0.91 Cr slipped | H1 FY27 | Small. 0.26% of AUF 16,264 (derived). |
| 8 (ii) | Restructured 2020-21/17 | 1 account, 4 lakh outstanding (Res R386-R387, L468-475). | Rs 0.04 Cr | Sep-26 | None |
| 9 | Reg 52(4) ratios | D/E 4.61x, CRAR 20.96%, GNPA 1.82%, NNPA 1.18%, LCR 156.85%, PCR 35.37%, NW 3,16,496 lakh (Res R388-R467, L478-506). | NW Rs 3,164.96 Cr | Sep-26 vs Jun-26, Mar-26, Sep-25 | Primary asset-quality source |
| 10 (I) | NPA sold to ARCs | 48 accounts (incl. written-off) sold for 3 lakh; NBV nil; principal-outstanding (L525) and residual-tenor (L526) cells blank, NOT DISCLOSED; asterisk footnote missing (Res R468-R471, R718, L519-529). | Rs 0.03 Cr consideration | Q2 FY27 | Write-off pool size NOT FOUND (A3-02) |
| 10 (II) | Direct assignment | 87,689 lakh of loans not in default assigned; residual 23 months; holding 8 months; 10% retained; 100% secured (Res R472-R476, L530-537). | Rs 876.89 Cr | Q2 FY27 | Off-book growth lever (A3-12, FN07). The deck shows a Rs 1,085 Cr Q2 sell-down (Deck R680). The Rs 208.11 Cr gap is not reconciled in any document; its route is NOT DISCLOSED (C1). |
| 10 (iii)/(iv) | Acquisitions | No loans acquired by assignment; no stressed loans acquired (Res R478-R479). | Nil | Q2 FY27 | None |
| 11 | Regrouping | Prior figures regrouped where needed (Res R722, L542). | ND | Prior periods | Not quantified |
| Ann. I | Security cover | Cover on book value 1.24x vs 1.10x contractual (Res R519-R520). Totals tie to the balance sheet (A3 Section 0). | n/a | Sep-26 | None |
| Ann. II | Covenants | All listed covenants complied (Res R746): CRAR 20.96% vs 15-16% floor; GNPA 1.82% vs 4-5% cap; NNPA 1.18% vs 3-4% cap; TOL/ATNW 4.61x vs 7.0, "calculated based on audited figures i.e. for 31st March 2026" (Res R743-R744, L843-844, L868-869); D/E 4.61x vs 6x on 30-Sep-2026 figures (Res R543-R544, R745, L893). | n/a | TOL/ATNW: Mar-26 audited; other ratios Sep-26 | TOL/ATNW label vs number (A3-15) |
| RPT Ann. | Federal Bank | Balances with Federal Bank closing 48,766.21 lakh; term loan 1,06,597 to 90,542 lakh (OCR-garbled); brand fee 184.97 lakh; derivative margin deposit closing 1,615.50 lakh with nil opening and nil flow (Res R545-R573, L956-966). | Rs 487.66 Cr balances; Rs 1.85 Cr brand fee | H1 FY27 | Promoter funding falling; margin deposit does not reconcile (A3-13, A3-16) |
| OCI (P&L page) | OCI items | Q2 OCI +2,662 lakh, Q1 (4,666) lakh. Q2 cash-flow hedge gain 4,348 lakh exceeds FY26 full year 3,182 (Res R109-R110, R145, L237-247; XC). | +Rs 26.62 Cr Q2; -Rs 46.66 Cr Q1 | Q1-Q2 FY27 | Explains the non-PAT net-worth moves (FND-04, FN05). Not in PAT. |
| Tax line | Earlier-year tax | Excess provision (18) lakh in FY26 only; nil in FY27 (Res R091-R096). | Rs (0.18) Cr | FY26 | Immaterial (A3-06) |

Answers to the four note questions:
- Change YoY/QoQ reading? Yes, three notes do. Note 10(II) shows Rs 876.89 Cr of assignment in one quarter, so AUM growth and on-book growth diverge (Step 5L). Note 2 and the Other Matter paragraph change the review regime. The OCI block shows Rs 26.62 Cr of Q2 equity growth outside PAT.
- Normalise any period? No exceptional item is disclosed. The net DA line (inside interest income) and the provision release are quantified in Step 4, not normalised away.
- Recurring vs one-off? The net DA loss (-Rs 1.2 Cr Q2, -Rs 12.9 Cr Q1; PR R026-R027) is recurring in kind and variable in size. The Q2 cash-flow hedge OCI gain is a reserve item.
- Thesis assumption change? Note 9 PCR 35.37% (Q1 38.36%) moves the Pillar 2L clause (Section 6C, 7).

Auditor opinion: **Unmodified** limited review (SRE 2410), "nothing has come to our attention" (Res R724-R726, L144-152). No EoM. No Going Concern. One **Other Matter** paragraph: comparatives were reviewed by KKC alone; conclusion not modified (Res R727). Cover letter names "V. Sankar Aiyar & Associates"; review report and certificate say "V. Sankar Aiyar & Co." (A3-14). Classification: clean, with a new-regime Other Matter. No AMBER flag from the opinion itself.

### 0E. Business type
**LENDING BUSINESS (NBFC)**: gold loans 54.1% of AUM, medium-ticket LAP 27.5%, small-ticket LAP and HL 17.8% (Deck R315-R317); 99.4% secured (Deck R064). Steps 1L and 5L apply.

Checkpoint: Notion fetched (Decision Status verified), units identified, share-count changes noted, all notes tabled, auditor opinion verified, business type stated.

---

## STEP 1L DATA EXTRACTION (LENDER), Rs Cr

Filing basis: Interest Income on the face of the P&L includes the net gain or loss on direct assignment. The press release shows interest income ex-DA; the two reconcile within Rs 0.1 Cr (Q2 692.01 + 1.2 = 693.2; Q1 644.57 + 12.9 = 657.47 vs 657.4 printed; Q2 FY26 507.70 - 6.6 = 501.1). Non-interest income = fee and commission + net gain on fair value changes + other income.

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | FY26 | FY27 | H1 FY26 | H1 FY27 |
|---|---|---|---|---|---|---|---|
| Interest Income (filing, incl. net DA) | 507.70 (Res R003, L218) | 644.57 (Res R002) | 692.01 (Res R001) | 2,109.07 (Res R006) | ND (year open) | 993.83 (Res R005) | 1,336.58 (Res R004) |
| Interest Expense (finance cost) | 213.84 (Res R039, L225) | 272.69 (Res R038) | 288.34 (Res R037) | 879.32 (Res R042) | ND | 431.81 (Res R041) | 561.03 (Res R040) |
| NII (filing) | 293.86 (derived; PR R033 293.9) | 371.88 (derived; PR R034) | 403.67 (derived; PR R035 403.7) | 1,229.75 (derived; Deck R969) | ND | 562.02 (derived; PR R038) | 775.55 (derived; PR R039) |
| of which Core NII ex-DA (mgmt) | 287.2 (PR R017) | 384.8 (PR R018) | 404.8 (PR R019) | 1,222.3 (Deck R959) | ND | 560.9 (PR R022) | 789.6 (PR R023) |
| of which net DA gain/(loss) (mgmt) | 6.6 (PR R025) | (12.9) (PR R026) | (1.2) (PR R027) | 7.4 (Deck R963) | ND | 1.2 (PR R030) | (14.0) (PR R031) |
| Other/Fee Income (fee + FV gain + other income) | 28.29 (Res R009+R015+R027) | 25.68 (Res R008+R014+R026) | 27.78 (Res R007+R013+R025) | 117.54 (Res R012+R018+R030) | ND | 59.41 (Res R011+R017+R029) | 53.46 (Res R010+R016+R028) |
| Operating Expenses (employee + D&A + other) | 183.16 (Res R051+R057+R063) | 210.02 (Res R050+R056+R062) | 226.37 (Res R049+R055+R061) | 771.01 (Res R054+R060+R066) | ND | 357.37 (Res R053+R059+R065) | 436.39 (Res R052+R058+R064) |
| PPOP | 138.99 (derived; PR R065 139.0) | 187.54 (derived; PR R066) | 205.08 (derived; PR R067 205.1) | 576.28 (derived; Deck R991) | ND | 264.06 (derived; PR R070) | 392.62 (derived; PR R071) |
| Provisions & Write-offs (impairment) | 31.52 (Res R045, L226) | 34.06 (Res R044) | 27.08 (Res R043) | 115.27 (Res R048) | ND | 56.24 (Res R047) | 61.14 (Res R046) |
| PBT | 107.47 (Res R075, L231) | 153.48 (Res R074) | 178.00 (Res R073) | 461.01 (Res R078) | ND | 207.82 (Res R077) | 331.48 (Res R076) |
| Tax | 27.32 (Res R081, L232) | 39.10 (Res R080) | 47.25 (Res R079) | 117.41 (Res R084) | ND | 52.66 (Res R083) | 86.35 (Res R082) |
| PAT | 80.15 (Res R105, L236) | 114.38 (Res R104) | 130.75 (Res R103) | 343.60 (Res R108) | ND | 155.16 (Res R107) | 245.13 (Res R106) |
| EPS basic, reported (Rs) | 2.15 (Res R177, L254) | 3.05 (Res R176) | 3.56 (Res R175) | 9.20 (Res R180) | ND | 4.16 (Res R179) | 6.54 (Res R178) |
| EPS diluted, reported (Rs) | 2.13 (Res R183, L255) | 3.03 (Res R182) | 3.53 (Res R181) | 9.12 (Res R186) | ND | 4.12 (Res R185) | 6.48 (Res R184) |
| EPS share-adjusted, basic (Rs) | 2.15 | 3.05 | 3.49 (derived: H1 6.54 - Q1 3.05; printed 3.56 does not reconcile, A3-10, XC) | 9.20 | ND | 4.16 | 6.54 |

Tie-checks: PPOP - provisions = PBT in every column (205.08 - 27.08 = 178.00; 187.54 - 34.06 = 153.48; 138.99 - 31.52 = 107.47; 576.28 - 115.27 = 461.01). Total expenses Q2 FY27: 288.34 + 27.08 + 126.54 + 15.41 + 84.42 = 541.79 = Res R067 54,179 lakh.

EPS misprint test (A3-10, printed values confirmed by XC): PAT 13,075 lakh / 3.56 = 3,673 lakh weighted shares, but paid-up capital gives 3,751 lakh shares. Q1 3.05 + Q2 3.56 = 6.61, but H1 is 6.54. H1 6.54 back-solves to 3,748 lakh shares, which matches capital. The printed Q2 basic EPS overstates by about 2% (3.56 vs 3.49). Diluted 3.53 implies fewer shares than basic, which is impossible. The same values appear twice (Res R456, R462, L505-506). Flag EPS-MISPRINT.

### Derived lender metrics

| Derived metric | Formula / source | Q2 FY26 | Q1 FY27 | Q2 FY27 |
|---|---|---|---|---|
| NIM (proxy) | NII / avg total assets, RoA tree | 8.8% (Deck R1026) | 8.5% (Deck R1027) | 8.8% (Deck R1028) |
| Core NII ex-DA / avg total assets | RoA tree | 8.6% (Deck R1018) | 8.8% (Deck R1019) | 8.8% (Deck R1020) |
| Spread (yield - CoB) | Slide 25, XC values | 8.7% (XC) | 8.6% (XC) | 8.8% (XC) |
| Cost-to-Income | Opex / (NII + other income) | 56.86% (derived; Deck R855 56.9%) | 52.83% (derived; Deck R856) | 52.47% (derived; Deck R857 52.5%) |
| Credit cost, annualised, company basis | Impairment / avg total assets (Deck R096 footnote) | 0.9% (Deck R1046) | 0.8% (Deck R1047); 0.78% derived (136.24 / 17,561) | 0.6% (Deck R1048); 0.59% derived (108.32 / 18,393.5) |
| Credit cost, annualised, protocol basis | Impairment / avg AUM | ND (Q1 FY26 AUM not in docs) | 0.66% derived (136.24 / 20,644.5) | 0.50% derived (108.32 / 21,585.5) |
| GNPA % / NNPA % | Reg 52(4) | 1.90% / 1.30% (Res R431, R435) | 1.55% / 0.96% (Res R429, R433) | 1.82% / 1.18% (Res R428, R432) |
| PCR % (Stage 3) | Reg 52(4) | 31.99% (Res R443) | 38.36% (Res R441) | 35.37% (Res R440) |
| Collection Efficiency % | As disclosed | ND | ND | ND (not disclosed in any of the three documents; not quantified on the call) |
| AUM (Rs Cr) | Deck slide 21/27 | 16,136 (Deck R424) | 21,136 (Deck R427) | 22,035 (Deck R428) |
| AUF on-book (Rs Cr) | Deck slide 27 | 11,743 (Deck R656) | 16,237 (Deck R657) | 16,264 (Deck R658) |
| Disbursements (Rs Cr) | Deck slide 21 | 5,205 (Deck R387) | 6,760 (Deck R390) | 6,676 (Deck R391) |
| RoA (annualised) | PAT / avg total assets | 2.4% (Deck R861) | 2.6% (Deck R862); 2.61% derived | 2.8% (Deck R863); 2.84% derived (523.0 / 18,393.5) |
| RoE (annualised) | PAT / avg net worth | 12.0% (Deck R867) | 15.4% (Deck R868); 15.43% derived | 17.0% (Deck R869); 16.96% derived (523.0 / 3,083.86) |
| CRAR % | Reg 52(4) | 21.64% (Res R427) | 20.71% (Res R425) | 20.96% (Res R424) |
| Leverage (avg TA / avg SF) | RoA tree | 5.0x (Deck R1062) | 5.9x (Deck R1063) | 6.0x (Deck R1064) |
| D/E (Reg 52(4)) | Borrowings / NW | 3.78x (Res R391) | 4.89x (Res R389) | 4.61x (Res R388); Mar-26 also 4.61x (Res R390) |

Averages used: total assets Mar-26 16,875 / Jun-26 18,247 / Sep-26 18,540 (Deck R917, R913, R914); net worth Mar-26 2,926.10 / Jun-26 3,002.76 / Sep-26 3,164.96 (Res R422, R421, R420).

Credit-cost basis flag (CREDITCOST-BASIS): the tripwire reads "of average assets". Notion records FY26 at "~0.64%". That figure matches average AUM (115.27 / avg(15,812, 20,153) = 0.641%, derived), not average assets. The company's FY26 figure on average total assets is 0.8% (Deck R1049, quarterly-average basis R1078). Q1 FY27 "0.8%" in Notion is on the company basis. The tripwire is not near on either basis this quarter. The operator should fix one basis in the Notion text.

### Yields, CoB and spreads (slide 25, XC values; quarterly two-point average, annualised; annual restated to quarterly average)

| Period | Yield | CoB | Spread | Source |
|---|---|---|---|---|
| FY22 | 16.0% | 7.8% | 8.2% | XC s-25 |
| FY23 | 16.1% | 7.8% | 8.3% | XC |
| FY24 | 16.7% | 8.6% | 8.1% | XC |
| FY25 | 17.1% | 9.0% | 8.2% | XC |
| FY26 | 16.7% | 8.1% | 8.6% | XC |
| Q2 FY26 | 17.0% | 8.4% | 8.7% | XC |
| Q3 FY26 | 16.8% | 7.8% | 9.0% | XC |
| Q4 FY26 | 16.8% | 7.8% | 9.0% | XC |
| Q1 FY27 | 16.4% | 7.7% | 8.6% | XC |
| Q2 FY27 | 16.7% | 7.9% | 8.8% | XC |
Cross-checks: daily average CoB (I-GAAP) 8.19% / 7.87% / 7.83% / 7.80% / 7.79% for Q2 FY26 to Q2 FY27 (Deck R606-R610). P&L-implied CoB Q2 FY27 7.87%, Q1 7.74% (FN25 derived). Both agree with the XC CoB series. QoQ, CoB rose 13-20 bps on two of three measures; only the daily I-GAAP series is flat.

### 1L-b. Prior-quarter Questions for Management: answer status (graded against the three filings; the call re-grade is in Role 5 Step 3E)

| # | Q1 FY27 question (Notion) | Status | Evidence this quarter |
|---|---|---|---|
| 1 | Branches opened in Q2; H1 count vs 200 target | PARTIALLY ANSWERED | 74 new branches, 831 total (Deck R033-R034). H1 = 74 vs 200. Target not restated. |
| 2 | Absolute gold tonnage Q1 and Q4 FY26; split of 25-30% guide | PARTIALLY ANSWERED | Tonnage 12.6 t Q4 FY26, 12.7 t Q1, 12.9 t Q2 (Deck R489-R491). No tonnage/LTV/price split. |
| 3 | Does the full FY27 stack hold; weakest leg | NOT ADDRESSED | No guidance in deck or release (FN02, FND-13). Call re-grade in Role 5 Step 3E. |
| 4 | Gold 1+/30+/60+ DPD under bullet vs periodic | NOT ADDRESSED | Not in any filing. |
| 5 | PCR floor as gold mix rises; gold-only vs mortgage-only PCR | PARTIALLY ANSWERED | Product PCR given: gold 10.5%, mortgage 37.5%, BL 95.9% (Deck R726, R736, R746). Floor not stated. |
| 6 | CLM/DA timeline, de-leverage from 4.89x, CRAR floor | PARTIALLY ANSWERED | D/E 4.61x (Res R388), equal to Mar-26 4.61x (Res R390); Q2 sell-down Rs 1,085 Cr (Deck R680) of which Rs 876.89 Cr filed as assignment (Res R472); off-book 26.2% (Deck R661). CLM is a listed funding source (Deck R587-R593) of unresolved size. No timeline, no CRAR floor. |
| 7 | DA-unwind drag on NII next 4 quarters | PARTIALLY ANSWERED | Q2 DA -Rs 1.2 Cr vs Q1 -Rs 12.9 Cr (PR R026-R027). No forward number. |
| 8 | AR detail on "~585cr" FVOCI loss and ECL re-recognition | PARTIALLY ANSWERED, UNIT FLAG | Q1 FY27 FVOCI-loans OCI is (5,851) lakh = Rs 58.51 Cr (XC). If the Notion "~585cr" refers to this line, it carries a 10x unit error. Operator to verify. The ECL re-recognition bridge is not given. |
| 9 | Bridge for the ~40cr GS3 provision reduction | NOT ADDRESSED | Stage 3 ECL 96.8 to 104.7 Cr (Deck R786-R787). No bridge. |
| 10 | ST LAP standalone disbursal; in-housing complete | PARTIALLY ANSWERED | ST LAP & HL Q2 Rs 210 Cr (Deck R479, XC s-22). In-housing not mentioned. |
| AR-1 | PCR floor past 46% gold mix | PARTIALLY ANSWERED | As row 5. Gold mix is now 54.1% (Deck R315). |
| AR-2 | Tier I 17.52%, CRAR 20.71%: equity-raise floor | NOT ADDRESSED | CRAR 20.96% (Res R424). Tier I not disclosed this quarter. |
| AR-3 | Gold AUM +76% on +12% tonnage; FY27 split; 15% gold-price shock | NOT ADDRESSED | Tonnage +16% YoY (Deck R481); portfolio LTV 68.0% (Deck R501). No sensitivity. |

Pattern (filings only): 0 of 13 fully answered, 8 partial (rows 1, 2, 5, 6, 7, 8, 10, AR-1), 5 not addressed (rows 3, 4, 9, AR-2, AR-3). Role 5 Step 3E re-grades the same 13 rows against the call: 1 answered, 8 partial, 4 not addressed. This counts toward DISCLOSURE-SILENCE. The repeat silences are logged as REPEATED-EVASION-2Q.

### 1L-c. Prior concall promise log vs delivery

| Promise (Q1 FY27 call) | H1 FY27 delivery | Status |
|---|---|---|
| Credit cost below 1% FY27 | 0.69% H1 annualised (derived: 122.28 / 17,707.5); Q2 0.6% (Deck R1048) | ON TRACK |
| ROA +20-30 bps over FY26 2.4% | H1 2.7% (PR R151); Q2 2.8% | ON TRACK |
| 200 branches in FY27 | 74 in H1 (0 in Q1, 74 in Q2) (Deck R033); 126 left for H2 | BEHIND |
| Gold AUM +25-30% (base Mar-26 Rs 10,352 Cr, price flat) | Rs 11,917 Cr, +15.1% in H1 (derived; Deck R441, R443). H1 growth was LTV-led: LTV 60.9% to 68.0% (+11.7%), tonnage +2.4%, implied price +0.7%. Q2 growth (+6.49%) was about 70% price (see 6D). Price-flat FY27 pace about +19% to +26% (derived). | AT RISK: reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t), against +2.4% in H1 |
| Gold tonnage +10-12% (base 12.6 t) | 12.9 t, +2.4% in H1 (derived; Deck R489, R491) | BEHIND (management said H2-weighted) |
| Entity AUM +20-22% (base Rs 20,153 Cr) | Rs 22,035 Cr, +9.3% in H1 (derived); Q2 pace (+4.25% QoQ) compounds to about +18.8% (derived), below the 20% floor | DELAYED |
| De-leverage ("we hope") | D/E 4.89x (Jun-26) to 4.61x (Sep-26) (Res R389, R388), but Mar-26 was also 4.61x (Res R390): H1 net de-leverage nil. Average leverage rose 5.9x to 6.0x in Q2 (Deck R1063, R1064). | NOT DELIVERED in H1; Q2 only reversed Q1's rise |
| PCR "optically reducing" | 38.36% to 35.37% (Res R441, R440) | DELIVERED as warned |
| DA income negative going forward | -Rs 1.2 Cr Q2 (PR R027) | DELIVERED, loss narrower |

The Role 5 scoring of this log under the v1.1 points rule is in Role 5 Step 3A.

Checkpoint: extraction table complete; every cell a number with anchor or ND.

---

## STEP 2 Q2 YoY COMPARISON (Q2 FY27 vs Q2 FY26), lender substitution

| Metric | Q2 FY26 | Q2 FY27 | YoY % change | Verdict |
|---|---|---|---|---|
| NII (filing) | 293.86 | 403.67 | +37.4% | Strong; AUM +36.6% YoY (Deck R049) |
| Core NII ex-DA (mgmt) | 287.2 (PR R017) | 404.8 (PR R019) | +40.9% | Strong |
| PPOP | 138.99 | 205.08 | +47.6% | Strong; operating leverage |
| PPOP / NTI (pp change) | 43.14% | 47.53% | +439 bps | Cost discipline; C/I 56.86% to 52.47% |
| Depreciation | 13.06 (Res R057) | 15.41 (Res R055) | +18.0% | Below NII growth |
| Finance costs | 213.84 | 288.34 | +34.8% | Below interest-income growth (+36.3%, derived 692.01 / 507.70) |
| PPOP after D&A (EBIT-equivalent) | n/a (D&A already in opex) | n/a | n/a | Lender: D&A sits inside opex |
| Other income (non-interest total) | 28.29 | 27.78 | -1.8% | Weak vs AUM growth (FND-09) |
| of which treasury (FV gain + other income line) | 5.70 (Res R015+R027) | 4.66 (Res R013+R025) | -18.2% | Shrinking, small |
| Provisions | 31.52 | 27.08 | -14.1% | Falling while AUM +36.6% and Stage 2 assets +51.7% YoY (387 to 587, Deck R767, R769) |
| Credit cost (company basis) | 0.9% (Deck R1046) | 0.6% (Deck R1048) | -36 bps (Deck R086) | Within guide; coverage question (FN09) |
| GNPA | 1.90% | 1.82% | -8 bps | Level fine; QoQ +27 bps |
| **Core operating PBT (PBT - treasury)** | 101.77 | 173.34 | **+70.3%** | Real; ex-DA it is +83.4% (95.17 to 174.54, derived) |
| Reported PBT | 107.47 | 178.00 | +65.6% | |
| PAT | 80.15 | 130.75 | +63.1% | |
| EPS share-adjusted (basic) | 2.15 | 3.49 (derived) / 3.56 printed | +62.3% / +65.6% | Printed EPS overstates growth by about 3 pp |

Diagnostic answers:
1. NII grew 37.4% YoY (293.86 to 403.67). Against the FY27 entity AUM guide of +20-22%, the YoY pace is ahead because the comparison base (Sep-25 AUM 16,136) precedes the H2 FY26 gold surge. No Notion base projection exists (ND), so no base-case comparison is possible.
2. PPOP margin on NTI expanded from 43.14% (Q2 FY26) to 47.53% (Q2 FY27), a change of +439 bps. Sequentially it moved from 47.17% (Q1 FY27, derived 187.54 / 397.56) to 47.53%, +36 bps.
3. Core operating PBT grew 70.3% YoY (101.77 to 173.34). Reported PBT grew 65.6%. Core growth exceeds headline, so headline growth is real at the operating level. The caveat is provisioning: provisions fell 14.1% YoY while the book grew 36.6%.
4. Gap between core PBT growth (+70.3%) and PAT growth (+63.1%), 7.2 pp, Rs 5.76 Cr (130.75 vs 80.15 x 1.7033). Treasury is the main wedge: treasury fell from 5.70 to 4.66 instead of growing with core (5.70 x 1.7033 = 9.71), a shortfall of Rs 5.05 Cr pre-tax, Rs 3.71 Cr post-tax, 4.7 pp, 64% of the gap. ETR is the second wedge: 25.42% to 26.54% costs Rs 2.05 Cr, 2.5 pp, 36%. The DA swing (+6.6 to -1.2) sits inside NII and inside core PBT. No exceptional items.
5. D&A (+18.0%) and finance costs (+34.8%) grew slower than interest income (+36.3%). No absorption gap. Opex grew 23.6% vs NTI +33.9%.
6. Treasury and other-income concentration is falling: treasury is 2.6% of PBT in Q2 FY27 (4.66 / 178.00) vs 5.3% in Q2 FY26 (5.70 / 107.47). Not masking trajectory. The quarter-specific item is the provision line, not treasury.

---

## STEP 3 SEQUENTIAL TRAJECTORY

| Quarter | NII (Rs Cr) | C/I | PPOP | Provisions | Core PBT (PBT - treasury) | PAT | AUM | One-offs flagged | QoQ run-rate |
|---|---|---|---|---|---|---|---|---|---|
| Q1 FY26 (derived H1 FY26 - Q2 FY26) | 268.16 | 58.21% | 125.07 | 24.72 | 94.39 (derived: 100.35 - (5.31 + 0.65)) | 75.01 | ND | Rs 770 Cr BL 100% assignment (Deck R681) | base |
| Q2 FY26 | 293.86 | 56.86% | 138.99 | 31.52 | 101.77 | 80.15 | 16,136 | Rs 116 Cr BL assignment (Deck R681); DA +6.6 | stepping up |
| Q3+Q4 FY26 avg per quarter (derived FY26 - H1 FY26, /2; single quarters ND) | 333.87 | 56.99% | 156.11 | 29.52 | ND | 94.22 | Q3 17,500 / Q4 20,153 (Deck R425-R426) | Gold disbursal surge 7,853 / 10,744 (Deck R413-R414, XC) | stepping up |
| Q1 FY27 | 371.88 | 52.83% | 187.54 | 34.06 | 151.91 (153.48 - 1.57, Res R014+R026) | 114.38 | 21,136 | DA -12.9; FVOCI OCI loss Rs 58.51 Cr (XC) | stepping up |
| Q2 FY27 | 403.67 | 52.47% | 205.08 | 27.08 | 173.34 | 130.75 | 22,035 | DA -1.2; provision coverage fall (FN09) | stepping up, slower core |

Diagnostics:
- Trajectory: Stepping up. PAT rose in each period: 75.01, 80.15, 94.22 (H2 FY26 average), 114.38, 130.75.
- Distortion: Q2 FY27 PBT +24.52 Cr QoQ. Of that, DA loss narrowing gave +11.7 Cr (48%) and lower provisions gave +6.98 Cr (28%). Core NII + other income - opex gave +5.75 Cr (23%, with rounding). The core engine added little in Q2. Most of the QoQ gain came from two variable lines.
- H1 run-rate test: Q2 PAT 130.75 vs H1 average 122.57 (245.13 / 2): +6.7% above. Q2 PPOP 205.08 vs H1 average 196.31: +4.5%. Q2 exceeds the H1 average.
- Implied Q3 FY27 base to hold trajectory: PPOP at or above 205.08 Cr. If provisions return to the Q1 level (34.06 Cr), PBT would be 171.02 Cr (derived), below Q2's 178.00. A flat PAT print in Q3 needs either PPOP growth of 3.4% ((178.00 + 34.06) / 205.08, derived) or a second low-provision quarter.

---

## STEP 4 OPERATIONAL DECOMPOSITION (lender bridge)

### YoY: Q2 FY26 PAT 80.15 to Q2 FY27 PAT 130.75 (+50.60 Cr)

| Component | YoY change (Rs Cr) | Share of PBT change | Recurring? |
|---|---|---|---|
| Core NII ex-DA | +117.60 (287.2 to 404.8, PR R017/R019) | +166.7% | Recurring |
| Net DA gain/(loss) inside NII | -7.80 (+6.6 to -1.2, PR R025/R027) | -11.1% | Variable (pool-dependent) |
| Other income (fee +0.53, FV gain -0.81, other -0.23) | -0.51 | -0.7% | Fee recurring; treasury not |
| Opex (employee -21.31, D&A -2.35, other -19.55) | -43.21 | -61.3% | Recurring (branch build) |
| Provisions | +4.44 (31.52 to 27.08) | +6.3% | Regular credit cost vs release: split NOT DISCLOSED |
| = PBT change | +70.53 | 100% | |
| Tax: volume effect at Q2 FY26 ETR 25.42% | -17.93 | | Mixed |
| Tax: ETR rise to 26.54% | -2.00 | | Unexplained (A3-05) |
| Exceptional items | 0 | | None disclosed |
| **Reported PAT change** | **+50.60** | | |

### QoQ: Q1 FY27 PAT 114.38 to Q2 FY27 PAT 130.75 (+16.37 Cr)

| Component | QoQ change (Rs Cr) | Recurring? |
|---|---|---|
| Core NII ex-DA | +20.0 (384.8 to 404.8) | Recurring |
| Net DA gain/(loss) | +11.7 (-12.9 to -1.2) | Variable |
| Other income | +2.10 | Mixed |
| Opex | -16.35 | Recurring (74 branches) |
| Provisions | +6.98 (34.06 to 27.08) | Release vs regular: NOT DISCLOSED |
| = PBT change | +24.52 (rounding 0.09 on core NII) | |
| Tax | -8.15 (39.10 to 47.25) | ETR 25.48% to 26.54% |
| **PAT change** | **+16.37** | |

### Memo: the coverage fork (FN09, weighed with the A5 stage-wise build)

Sensitivity ([INFERENCE] on filed stage data, Deck R755-R796): at Q1 FY27 stage-wise coverage (Stage 1 0.34%, Stage 2 16.53%, Stage 3 38.36%), the Q2 ECL stock would be about Rs 262.8 Cr vs Rs 243.5 Cr actual, a gap of about Rs 19.3 Cr. Credit cost would be about Rs 46.4 Cr, about 1.0% of average total assets, against 0.6% reported and the 1.1% tripwire. Post-tax that is about Rs 14.5 Cr, about 88% of the QoQ PAT gain.

Whole-book counter-observation (derived): total ECL / AUF rose from 1.37% (221.7 / 16,237) to 1.50% (243.5 / 16,264) QoQ. Total ECL stock rose Rs 21.8 Cr against a Rs 27.1 Cr charge.

Stage-wise ECL build, Q1 to Q2 FY27 (derived, Deck R756-R787):
| Stage | Assets Q1 to Q2 (Rs Cr) | Asset change | ECL Q1 to Q2 (Rs Cr) | ECL change | Marginal coverage |
|---|---|---|---|---|---|
| Stage 1 | 15,549 to 15,381 | -168 | 52.8 to 64.8 | +12.0 | n/a (book shrank) |
| Stage 2 | 436 to 587 | +151 | 72.0 to 74.1 | +2.1 | 1.4% |
| Stage 3 | 252 to 296 | +44 | 96.8 to 104.7 | +7.9 | 18.0% |
| Stage 2 + 3 (stressed) | 688 to 883 | +195 | 168.8 to 178.8 | +10.0 | 5.1% |
| Total | 16,237 to 16,264 | +27 | 221.7 to 243.5 | +21.8 | |
Stressed-book coverage fell from 24.5% (168.8 / 688) to 20.2% (178.8 / 883). Stage 1 took Rs 12.0 Cr, 55% of the Rs 21.8 Cr build, on a book that shrank by Rs 168 Cr.

Weighing the fork:
- Reading A (mix shift into low-LGD gold Stage 2/3; gold Stage 3 PCR 10.5%, Deck R736; portfolio LTV 68%, Deck R501). Support: the gold share of the Stage 3 rise (Step 5L). Weakened: the whole-book coverage rise does not show stressed loans are better covered. It shows more provision went to performing Stage 1 loans.
- Reading B (provision release flattering PAT). Live. New stressed assets of Rs 195 Cr received Rs 10.0 Cr, 5.1% marginal cover. Stressed coverage fell 430 bps in one quarter.
- Net weight (conservative bias, Steps 0-6): B is not ruled out and carries at least equal weight with A. The Stage 1 build is the only offset, and a Stage 1 provision does not cover a loss that has already moved to Stage 2/3.
- Separating observation: the product-wise Stage 2 split and coverage, with gold auction losses (Q1, Q2 in Step 8.5).
- Role 5 note: the call adds management attribution in favour of Reading A (Stage 2/3 rise "entirely" gold, Call L160-161; nil auction loss in six years [ASR], Call L420-424) but no number. The separating observation is still missing. The weighting above stands (Role 5 Step 7A).

Mandatory questions:
- Recurring vs non-recurring share of YoY PAT change: core NII less opex (+74.39 Cr pre-tax) exceeds the full PBT change (+70.53 Cr). The YoY gain is recurring in source at the current gold price and LTV (gold supplied 88% of YoY AUM growth; Step 6D). QoQ, about 76% of the PBT gain came from the DA line and provisions.
- If treasury reverts to Q2 FY26 level (5.70): PBT +1.04 Cr. Immaterial.
- Steady state: opex is still ramping (74 branches in Q2, 126 to come per guide). The DA line has been negative for two quarters; its steady state is NOT DISCLOSED. Cost of borrowing rose 13-20 bps QoQ on two of three measures (slide 25 7.7% to 7.9%, XC; P&L-implied 7.74% to 7.87%, FN25); the daily I-GAAP series is flat (7.80% to 7.79%, Deck R609-R610); spread still widened from 8.6% to 8.8% (XC).
- Tax: deferred-tax credits of Rs 5.31 Cr in Q2 and Rs 4.80 Cr in Q1 (Res R097-R098) cut ETR by about 298 bps and 313 bps (A3-05). Current tax is 29.53% of Q2 PBT. DTA rose Rs 16.75 Cr in H1 and ties exactly to P&L plus OCI deferred tax. Deferred credits on rising ECL reverse at write-off. The reported ETR still rose.

Checkpoint: bridges presented.

---

## STEP 5L ASSET QUALITY AND CAPITAL

| Metric | Prior period (Q1 FY27) | Current period (Q2 FY27) | Change | Verdict |
|---|---|---|---|---|
| Credit cost (annualised) vs guided band (below 1% FY27) | 0.8% (Deck R1047) | 0.6% (Deck R1048); H1 0.69% derived | -19 bps (Deck R087) | Within guide. Quality of the fall in question (FN09; stressed marginal cover 5.1%). |
| GNPA % | 1.55% (Res R429) | 1.82% (Res R428) | +27 bps | AMBER direction; level within 1.9-2.1% checklist band |
| NNPA % | 0.96% (Res R433) | 1.18% (Res R432) | +22 bps | AMBER; 81% of the GNPA rise unprovided at the margin (22/27) |
| PCR % | 38.36% (Res R441) | 35.37% (Res R440) | -299 bps | AMBER; above 32% red line; checklist item 2 missed |
| Stage 2 assets (Rs Cr) / coverage | 436 / 16.53% (Deck R768, R777) | 587 / 12.61% (Deck R769, R778) | +34.6% / -392 bps | RED direction (FN09) |
| Stressed (Stage 2 + 3) coverage | 24.5% (derived) | 20.2% (derived) | -430 bps | RED direction (Step 4 memo) |
| Gold Stage 3 % / Rs Cr | 0.1% (Deck R738); Q2 FY26 0.4% (Deck R737) | 0.5%, Rs 47.6 Cr, PCR 10.5% (Deck R734, R736, R739) | +40 bps QoQ; +10 bps YoY | Gold drives the QoQ Stage 3 rise (FN11); YoY move small |
| Mortgage Stage 3 % / PCR | 3.4% / ND (Deck R728) | 3.4%, Rs 234.4 Cr, PCR 37.5% (Deck R724, R726, R729) | flat | Stable |
| Collection efficiency % | ND | ND | ND | NOT DISCLOSED |
| Restructured / stressed book | Resolution exposure Rs 46.97 Cr at Mar-26 (Res R381) | Rs 42.21 Cr (Res R385); restructured 1 account Rs 0.04 Cr (Res R386-R387) | -Rs 4.76 Cr | Small, run-off |
| Write-offs in period | ND | ND (resolution pool write-off nil, Res R383; ARC sale 48 accounts for Rs 0.03 Cr, NBV nil, principal and tenor NOT DISCLOSED, Res R468-R470, L525-L526) | ND | Write-off pool NOT FOUND (A3-02) |
| AUM growth YoY | +35% (Notion Q1 FY27 record) | +36.6% (Deck R049) | +1.6 pp | Strong; off-book-led in Q2 (FN07) |
| Disbursement growth YoY | ND (Q1 FY26 disbursals not in docs) | +28.3% (Deck R052) | ND | QoQ -1.2% (Deck R053) |
| Cost of funds | 7.7% slide 25 (XC); 7.80% daily I-GAAP (Deck R609); 7.74% P&L-implied | 7.9% (XC); 7.79% (Deck R610); 7.87% P&L-implied | +20 bps / -1 bp / +13 bps | Up on two of three measures; spread still +20 bps |
| CRAR % | 20.71% (Res R425) | 20.96% (Res R424) | +25 bps | Above 15-16% covenant; -144 bps vs Mar-26 22.40% |
| Promoter pledge | Nil (Notion) | ND in this quarter's filings; Federal Bank 60.6% (Deck R226) | ND | No signal |

Off-book and funding (FN07, A3-12, A3-13):
| Item | Q1 FY27 | Q2 FY27 | Change |
|---|---|---|---|
| Total AUM | 21,136 | 22,035 | +899 |
| Total AUF (on-book) | 16,237 | 16,264 | +27 |
| Gold AUM / AUF | 11,191 / 9,473 | 11,917 / 9,421 | +726 / -52 |
| Gold off-book share | 15.3% | 20.9% | +560 bps (Deck R642-R643) |
| Total off-book share | 23.2% | 26.2% | +300 bps (Deck R660-R661) |
| Incremental sell-down (deck) | 530 | 1,085 | x2.05 (Deck R679-R680) |
| of which filed as direct assignment (Note 10(II)) | ND (Q1 results not in run) | 876.89 (Res R472) | Gap Rs 208.11 Cr, route NOT DISCLOSED |
| Borrowings | 14,696 | 14,602 | -0.6% (Deck R933-R934) |
| Cash and bank | 919 | 827 | -92 (Deck R893-R894) |
| Other financial liabilities (results BS) | 216.38 (Mar-26, Res R242) | 468.19 (Sep-26, Res R241) | +116% vs Mar (A3-12) |

Sell-down reconciliation (C1): the deck shows a Rs 1,085 Cr Q2 sell-down (Deck R680). The filing shows Rs 876.89 Cr of loans transferred by assignment (Res R472). The Rs 208.11 Cr difference is UNRECONCILED. No document states its route. The deck funding legend lists both "Direct Assignments" and "CLM" (co-lending) as sources (Deck R587-R593; slice sizes unresolved). Co-lending is therefore one candidate route, NOT DISCLOSED in size. Question Q4 and row 31 carry this. Role 5 note: the CFO names co-lending in the gold portfolio as a second de-leveraging route ("higher coal ending" [ASR for co-lending], Call L148-150; "direct assignment and co-lending business normalized", Call L92-94). Size still NOT DISCLOSED.

Cash quality (lender reading): H1 FY27 operating cash flow was -Rs 718.88 Cr (Res R306), driven by a loan-book build of Rs 1,843.15 Cr (Res R290). Operating cash flow before the loan build was +Rs 1,124.27 Cr (derived: -718.88 + 1,843.15). Cash fell 42% from Rs 1,339.73 Cr to Rs 773.68 Cr (Res R190, R189). CFO/PAT is not a meaningful lender metric. The lender cash-quality test (collection efficiency, write-offs) is NOT DISCLOSED. Classification: **INDETERMINATE-WITH-DIRECTION** (direction: growth-induced). This caps the verdict at PROCEED WITH CAVEATS or below. Missing evidence: collection efficiency and H1 write-offs. The call mentions "improving collection efficiencies on the mortgage book" (Call L136) with no number, so the classification stands.

Mandatory lender questions:
- Asset-Quality Multiplier band: level evidence (GNPA 1.82%, NNPA 1.18%, credit cost 0.6%) fits Sound 1.00x. Direction evidence points toward Stressed 0.80x: Stage 2 +34.6% with coverage -392 bps; stressed coverage 24.5% to 20.2%; PCR -299 bps; GNPA +27 bps. The Pillar 2L self-withdrawal clause condition "PCR thins further" reads as MET on a QoQ baseline (38.36% to 35.37%). It is NOT MET against the FY26 baseline (32.29%). The clause names no baseline. Recompute deferred (OR-30); operator ruling needed. Flag PILLAR2L-SELFWITHDRAW-CONDITION.
- Credit cost within guided band: yes (0.6% Q2, 0.69% H1 vs below 1%). Logged ON TRACK in the promise tracker.
- Concentration: the QoQ Stage 3 rise is product-concentrated (gold), not state-concentrated on the evidence. Gold GS3 moved from about Rs 9 Cr (0.1% of 9,473, rounded) to Rs 47.6 Cr; total GS3 rose Rs 44 Cr (252 to 296, Deck R780-R781). YoY, gold GS3 is up only 10 bps (0.4% to 0.5%, Deck R737, R739). Mortgage GS3 % was flat. Top-5 state share fell to 74.5% (Deck R385). North mortgage share rose to 32% (Deck R548) on an unseasoned book (FN12). The deck attributes the move to "gold loan industry changes" (Deck R722) without naming them. A product-specific cause has a normalisation path; it is not yet evidenced. Role 5 note: the call names the cause as an April 2026 change that moved gold loans from bullet to periodic interest (Call L154-159, L341-342).
- AUM growth vs collection infrastructure: disbursals fell 1.2% QoQ while branches rose 9.8% and staff 10.1% (Deck R053, R075, R078). AUM growth in Q2 came mainly off-book. Collection efficiency is ND, so the classic pre-stress test cannot be run. Gold portfolio LTV rose from 59.3% (Q3 FY26) to 68.0% (Deck R498, R501): the collateral cushion is thinner.

Capital (A3-04, FN16, FND-07): D/E 4.61x against the 6x cap on the newest secured NCD (Res R543-R544): headroom 1.39x of net worth, about Rs 4,399 Cr of further debt at constant net worth (A3 derived). D/E was also 4.61x at Mar-26 (Res R390), so H1 net de-leverage is nil; the Q2 fall reversed Q1's rise to 4.89x. Average leverage rose from 5.9x to 6.0x in Q2 (Deck R1063, R1064). CRAR 20.96% vs 15% floor. About half the RoE rise from 12.0% to 17.0% came from leverage (avg TA / avg SF 5.0x to 6.0x, Deck R1062, R1064). Net worth grew 16.8% YoY vs borrowings 42.7% (Deck R058, R068). Growth at the H1 pace needs more assignment, co-lending or equity.

Standalone vs consolidated (A3 F2): standalone only; no subsidiary, associate or JV (Note 6, Res R702, L432). S-vs-C PAT gap 0.0% in Q2 FY26, Q1 FY27, Q2 FY27, H1 FY26, H1 FY27 and FY26. The consolidated column is ND because no consolidated statement exists. The call raised no entity-level item (concall A3 F2 N.A.).

Checkpoint: asset-quality table and answers presented.

---

## STEP 5.5 DOWNSTREAM SIGNAL RECONCILIATION

5.5A. Tracker rows: NOT SUPPLIED to this run (SIGNAL CONTEXT: tracker rows not supplied). Signal count 0, below the floor of 3. Flag TRACKER-ROWS-ND. Role 5.5 should be reopened for this company in claude.ai.

| Signal Name | Type | Cadence | Latest Observation | Direction | Thesis element | Health |
|---|---|---|---|---|---|---|
| ND | ND | ND | ND | ND | ND | ND |

5.5B. Reconciliation: not possible without tracker rows. Target reported: strong headline, mixed asset-quality direction. Signal reading: ND.

5.5C. New dependencies surfaced this quarter (payload candidates only; written only through the operator-approval write gate):
- Candidate 1, Case B: Assignment / co-lending buyer appetite. Off-book share rose to 26.2%; Q2 deck sell-down Rs 1,085 Cr, of which Rs 876.89 Cr filed as assignment (Deck R661, R680; Res R472). Buyer identity NOT DISCLOSED. Feeds AUM growth and CRAR.
- Candidate 2, Case B: Domestic gold price vs portfolio LTV. Gold AUM per tonne about Rs 924 Cr vs about Rs 606 Cr a year earlier (FN11 derived); portfolio LTV 68.0% (Deck R501). Q2 gold growth was about 70% price (Step 6D). Feeds gold Stage 3, auction loss and growth.
- Candidate 3, Case B: FCY/ECB borrowing cost and hedge. Q2 cash-flow hedge OCI gain Rs 43.48 Cr (Res R145); derivative assets Rs 278.46 Cr (Res R193); ECB appears in the funding legend (Deck R587-R593, unresolved). Feeds CoB and OCI.
Statement: "New signals proposed for tracker: three, Case B, pending operator approval. No tracker write performed in this stage."

5.5D. Forward-view weighting: no signal trajectory exists, so Step 6 rests on the single-quarter print. Conservative interpretation applies.

---

## STEP 6 RECONCILIATION VS THESIS

### 6A. Variance vs Notion projections

| Metric | Bear Proj | Base Proj | Bull Proj | Actual (Q2 FY27 / H1 FY27) | Lands In |
|---|---|---|---|---|---|
| Revenue (NII) | ND | ND | ND | 403.67 / 775.55 | ND (no P&L projections on the Notion page) |
| PPOP margin (C/I) | ND | ND | ND | 52.47% / 52.64% | ND |
| PAT | ND | ND | ND | 130.75 / 245.13 | ND |
| EPS | ND | ND | ND | 3.49 derived (3.56 printed) / 6.54 | ND |
| Net debt (borrowings) | ND | ND | ND | 14,602 (Deck R934) | ND |
| ROE | ND | ND | ND | 17.0% / 16.2% | ND |

Only 3-year fair values exist (bear 117 / base 150 / bull 186), which cannot be compared with a quarter. Probability re-weighting rule: NOT ASSESSABLE (no bands). Flag PROJECTIONS-ND for Role 1.

### 6B. Watchlist item status (Notion checklist, verbatim order)

| # | Watchlist item | Green threshold | Red threshold | This quarter reading | Status |
|---|---|---|---|---|---|
| 1 | Credit cost <= 1.1% of avg assets, FY27 guidance issued | <= 1.1%; guidance issued | > 1.1% | 0.6% Q2 (Deck R1048); 0.69% H1 derived; guidance not in deck or release (FN02) | AMBER (level GREEN; guidance UNKNOWN; coverage caveat FN09). Role 5 8B: guidance issued on the call. |
| 2 | PCR >= 38% and rising toward 50%+ | >= 38%, rising | < 32% | 35.37% (Res R440), down 299 bps | AMBER |
| 3 | Gold branch count 140-150, AUM per branch > Rs 13.3 Cr | per definition | ND | Gold branches 706 (Deck R496); gold AUM per branch Rs 16.9 Cr (Deck R486), down from 17.7 on 74 new branches (Deck R503) | GREEN on per-branch; count band matches no disclosed series (definition flag) |
| 4 | Cost-to-income materially below ~57% and falling into FY27 | < 57%, falling | ND | 52.47% (Q1 52.83%; FY26 57.23%) | GREEN (QoQ fall only 36 bps, FN15) |
| 5 | ROE toward 14-15%, ROA >= 2.5% | ROE >= 14%, ROA >= 2.5% | ND | ROE 17.0%, ROA 2.8% (Deck R869, R863) | GREEN (about half of RoE gain is leverage, FN16) |
| 6 | GNPA / Gross Stage 3 at or below ~1.9-2.1% | <= 1.9-2.1% | ND | 1.82% (Res R428), +27 bps QoQ | GREEN (rising) |
| 7 | ST LAP collections in-housing complete, disbursals > Rs 208 Cr | both | ND | Q2 Rs 210 Cr (Deck R479, XC); in-housing NOT FOUND; FY26 Rs 904 Cr vs FY24 Rs 1,475 Cr (XC s-22) | AMBER (disbursal met by Rs 2 Cr; in-housing UNKNOWN) |
| 8 | Gold tonnage growth disclosed and rising, not just rupee AUM | disclosed, rising | ND | 12.9 t, +16% YoY (Deck R481, R491), +1.6% QoQ vs gold AUM +6.5% | GREEN on disclosure; growth is price and LTV-led (FN11, 6D) |

### 6C. Thesis-broken trigger check

| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| Credit cost > 1.1% of average assets | 1.1% | 0.6% Q2 (Deck R1048); 0.69% H1 derived; about 1.0% at Q1 coverage [INFERENCE, FN09] | NO |
| ROE fails to cross 14% by FY28 | 14% by FY28 | 17.0% Q2; 16.2% H1 (PR R159) | NO |
| PCR thins below 32% | 32% | 35.37% (Res R440) | NO |
| (Pillar 2L clause, not a tripwire) override self-withdraws if credit cost > 1.1% or PCR thins further | QoQ or vs FY26 baseline undefined | PCR 38.36% to 35.37% QoQ; vs FY26 32.29% higher | CONDITION MET QoQ; NOT MET vs FY26. FLAG; operator decides. |

No thesis-broken condition has FIRED. No AVOID reclassification is triggered by a tripwire.

### 6D. Growth trigger status

Gold AUM decomposition against the trigger's own "price flat" condition (derived; Deck R327, R441-R443, R489-R491, R497-R501):
| Period | Gold AUM growth | Tonnage | Portfolio LTV | Implied gold value per gram | Price share of growth |
|---|---|---|---|---|---|
| YoY (Q2 FY26 to Q2 FY27) | +77.0% | +16.2% (11.1 to 12.9 t) | +10.2% (61.7% to 68.0%) | about +38% | about 57% (log basis) |
| H1 FY27 (Mar-26 to Sep-26) | +15.1% | +2.4% (12.6 to 12.9 t) | +11.7% (60.9% to 68.0%) | about +0.7% | small; H1 was LTV-led |
| Q2 FY27 (QoQ) | +6.49% | about +1.6% (12.7 to 12.9 t) | flat (67.9% to 68.0%) | about +4.7% (range 3.8-5.5% on 0.1 t rounding) | about 70% |
LTV headroom: portfolio LTV 68.0% is 4.1 pp below the average origination LTV of 72.1% (Deck R327). The LTV lever is nearly used.
Price-flat, LTV-flat FY27 paths: tonnage at the Q2 rate (1.6% per quarter) gives about +18.8% (1.1512 x 1.016^2); tonnage guide met (13.86-14.11 t) gives about +23.7% to +25.9%. The Q2-pace +30.5% needs about 20% a year gold-price inflation, which the trigger excludes.

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| Gold AUM +25-30% FY27 (base Mar-26, price flat) | ND | +15.1% in H1 (10,352 to 11,917); Q2 pace compounds to about +30.5% (derived) | Price-flat pace about +19% to +26%; Q2 growth about 70% price; H1 LTV-led; LTV 4.1 pp below origination; Q2 gold on-book AUF fell Rs 52 Cr | AT RISK: reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t), against +2.4% in H1 |
| Gold tonnage +10-12% FY27 (H2-weighted) | ND | 12.9 t, +16% YoY | +2.4% in H1; Q2 pace gives about +5.7% (derived) | DELAYED |
| Entity AUM +20-22% | ND | +9.3% in H1 | Q2 pace (+4.25% QoQ) gives about +18.8% (derived), below the 20% floor | DELAYED |
| Mortgage 15-20% | ND | Mortgage AUM +13.5% YoY (Deck R031) | Non-gold AUM +3.2% in H1 (9,801 to 10,118); MSME hubs 129 to 125 (FN14) | WEAKENED |
| LAP 15-20% | ND | MT LAP H1 disbursals 1,174 vs FY26 2,180 (XC) | ST LAP disbursals down 39% FY24-FY26 (XC) | ND (segment AUM YoY not disclosed) |
| ROA +20-30 bps over FY26 ~2.4% | ND | H1 2.7%, Q2 2.8% | Partly provision- and leverage-driven | ON TRACK |
| 200 new branches FY27 | ND | 74 in Q2 | 0 in Q1; 126 needed in H2 | DELAYED |
| Parent-funded co-lending scale-up | ND | CLM listed as a funding source (Deck R587-R593), size unresolved | Federal Bank term loan Rs 1,065.97 to 905.42 Cr (Res R550-R551, OCR-garbled); co-lending volume NOT DISCLOSED | WEAKENED (no size evidence; promoter funding falling) |
| De-leverage as CLM normalises (from 4.89x) | ND | D/E 4.89x (Jun-26) to 4.61x (Sep-26) (Res R389, R388) | Mar-26 D/E also 4.61x (Res R390): H1 net nil; average leverage 5.9x to 6.0x (Deck R1063, R1064). Q2 deck sell-down Rs 1,085 Cr of which Rs 876.89 Cr filed DA; balance route NOT DISCLOSED. | DELAYED (no net H1 de-leverage) |
| Credit-cost normalisation (shared FTTCP catalyst) | ND | 0.6% Q2 | Stage 2 +34.6%; stressed coverage 24.5% to 20.2% | ON TRACK on number, quality unresolved |

Checkpoint: 6A-6D presented. Post-call trigger status is in Role 5 Step 8A.

---

## STEP 6.5 EXPECTATION LEDGER AND A21 BASE REFRESH: DEFERRED TO /fttcp AND ROLE 1 (OR-30)

Pillar-relevant facts for the A21 base (flagged, not computed):
- Latest-quarter PAT Rs 130.75 Cr; H1 FY27 Rs 245.13 Cr; trailing-four-quarter PAT Rs 433.57 Cr (derived: 343.60 - 155.16 + 245.13); TTM basic EPS Rs 11.58 (derived: 9.20 - 4.16 + 6.54).
- One-offs to state at refresh: none exceptional. Variable items: net DA loss (-Rs 1.2 Cr Q2), coverage-driven provision gap (about Rs 19.3 Cr pre-tax at Q1 coverage, INFERENCE; stressed marginal cover 5.1%), ETR 26.54%.
- Gold growth basis: Q2 growth was about 70% price; any base that annualises Q2 gold growth embeds gold-price inflation.
- Expectation Ledger rows: not passed; ageing not performed.

## STEP 7 FOUR-PILLAR RE-VALIDATION (LENDER ROWS): DEFERRED TO /fttcp AND ROLE 1 (OR-30)

| Pillar / input | Original assumption (Notion) | Current reading (this quarter) | Action |
|---|---|---|---|
| Pillar 1 ROE base (lender) | ND (not passed) | ROE 17.0% Q2, 16.2% H1; leverage 6.0x; RoA 2.8% | Deferred to /fttcp ROE forward verdict. Flag LEVERAGE-LED-ROE. |
| Pillar 2L Asset-Quality Multiplier | 1.00x operator override (from 0.80x) | GNPA 1.82%, NNPA 1.18%, PCR 35.37%, credit cost 0.6%, Stage 2 +34.6% with coverage 12.61%, stressed coverage 20.2% | Deferred. Self-withdrawal condition met QoQ. Operator ruling on baseline required. |
| Growth Visibility Premium | ND | AUM +36.6% YoY, off-book-led; gold trigger AT RISK on price-flat basis; 6 of 10 (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK (6D) | Deferred |
| Strategic Premium | ND | EM MOAT STRENGTHENING 25.3/100 (Notion); no moat data this quarter | Deferred |
| UA Multiplier | ND | Institutions: FII 9.7%, MF 5.2%, insurance 3.0%, AIF 3.7% (Deck R225-R229) | Deferred |
| Sector cap | 18x (Banks/NBFCs/MFIs) | No reclassification | Hold |
| Hurdle Ratio | STOP (1.21 vs 1.953) | TTM basic EPS Rs 11.58 (derived); BVPS Rs 84.4 (Deck R060). CMP stale (164 property, about 157 on 23-Aug-2026). On the stale ~157: TTM P/E 13.6x, P/B 1.86x (derived, stale input). | Deferred to Role 1 with a fresh CMP |

Role 1 flag ENTRY-ZONE-BELOW-BOOK: the entry zone maximum Rs 77 is now 0.91x Q2 BVPS Rs 84.4 (derived). The zone was set 2026-07-15. Role 1 should test whether it is still the right construct.

---

## STEP 8 POSITION DECISION

Decision Status verified: WATCHLIST / AVOID (DEEP WATCH). Not held. Branch **8A-W**.

8A-W logic:
- Thesis-broken FIRED? No (6C).
- Landing vs bear/base/bull: NOT ASSESSABLE. Projections are ND on the Notion page.
- Pre-committed BUY gate: not met. Entry zone Rs 68-77 against a stale CMP of about Rs 157 (2x the zone maximum).
- Output: entry zone unchanged pending Role 1 (flag ENTRY-ZONE-BELOW-BOOK). Gate: Q3 FY27 results (expected mid-January 2027 [INFERENCE from the 15-Jul and 15-Oct board cadence, Res R662, R657]). Proposed Decision Status: **no change** (WATCHLIST / AVOID, DEEP WATCH). The operator sets status. Role 5 Step 8E confirms no change after the call.
- Separate operator item: rule on the Pillar 2L self-withdrawal baseline (QoQ vs FY26). If QoQ governs, Pillar 2L returns to 0.80x at the next valuation refresh.

### 8B. Add-back / trim trigger refinement
- Original add-back trigger: ND (not passed).
- Proposed refinement for the operator: write the Pillar 2L clause with a named baseline ("PCR below the prior quarter-end by more than 200 bps, or below the FY26 audited 32.29%") and add a product leg ("mortgage Stage 3 PCR below 35%"). Rationale: gold mix now moves aggregate PCR mechanically (gold PCR 10.5%, mortgage 37.5%).
- Fix the credit-cost tripwire basis to impairment / average total assets (company definition, Deck R096), since Notion records mix AUM and asset bases (CREDITCOST-BASIS).
- Original trim ladder: not applicable (not held).

### 8C. Single cleanest metric for Q3 FY27
**Q3 FY27 credit cost, impairment / average total assets (company basis, Deck R096).**
- Bull threshold: at or below 0.8% with GNPA at or below 1.82%. The Q2 fall was mix, not release.
- Bear threshold: at or above 1.0%. The coverage gap (about Rs 19 Cr) is being caught up; within 10 bps of the 1.1% tripwire.

Checkpoint: position decision, refinements, single metric presented.

---

## STEP 8.5 QUESTIONS FOR MANAGEMENT

Channel: the Q2 FY27 call transcript is now in the run (ASR of company audio). Each row 1-31 below carries its call status: ANSWERED, PARTLY or NOT ADDRESSED, with line cites. Rows 32-47 are new. They make sure every concall A3 FORWARD-SIGNAL and AMBIGUOUS finding has at least one question. Call grading of rows 1-31: 3 ANSWERED (rows 3, 7, 9), 8 PARTLY (rows 1, 2, 6, 10, 25, 28, 30, 31), 20 NOT ADDRESSED (rows 4, 5, 8, 11-24, 26, 27, 29). ANSWERED rows close; every other row carries forward.

### Ranked questions (Q1 most material)

| # | Question | Why it matters | Bull answer | Bear answer | Cat. | Finding IDs | Call status (Role 5) |
|---|---|---|---|---|---|---|---|
| 1 | Stage 2 assets rose 34.6% QoQ to Rs 587 Cr while Stage 2 coverage fell from 16.53% to 12.61%. What share of Q2 Stage 2 is gold loans? | Separates mix shift from provision release. New stressed assets of Rs 195 Cr got Rs 10.0 Cr (5.1%); stressed coverage fell 24.5% to 20.2%; Stage 1 took Rs 12.0 Cr of the Rs 21.8 Cr build. | 75% or more gold, LTV at or below 75% | Mortgage Stage 2 rose, or mortgage coverage was cut | D | A3-11, FN09, FN10, FND-05, FN-02 | PARTLY. CFO: the Stage 2 and Stage 3 rise is "entirely on account of this change constructed in goal loans" (Call L160-161, T05 explicit). No product number. CEO: mortgage stages "steady or in fact declining" (Call L348-349, inferred). |
| 2 | What were gold auction losses in Q2 FY27, in Rs Cr? | Tests the low-LGD reading of gold Stage 3 (Rs 47.6 Cr, PCR 10.5%) | Below Rs 1 Cr | Above Rs 5 Cr, or not tracked | D | FN11, FN-01 | PARTLY [ASR]. CFO: no auction loss on principal or interest in six years; "we will not have any loss" (Call L420-424, inferred; negation garbled at L420). No Q2 auction count, value or shortfall. |
| 3 | Which "gold loan industry change" on slide 29 lifted gold Stage 3 from 0.1% to 0.5%? | A named, technical cause has a normalisation path; an unnamed one does not | A named rule change with a dated end to its effect | No specific cause given | D | FN03 | ANSWERED. An April 2026 change: "the revised gold lending LTV framework" and the shift from bullet to periodic interest (Call L71-72, L154-159, L341-342). End date hedged: "it may take one or two more quarters" (Call L414-415). The regulator's text is not in the run. |
| 4 | Of the Rs 1,085 Cr Q2 sell-down (Rs 876.89 Cr filed as direct assignment; Rs 208 Cr unreconciled), what share went to Federal Bank? | Growth now rides loan buyers; a promoter buyer is a related-party dependency | Below 25%, several unrelated banks | Above 50% to Federal Bank | E | FN07, A3-12 | NOT ADDRESSED. No buyer or partner named. |
| 5 | What was the gross gain on pools assigned in Q2 FY27, before the reversal on older pools? | Net DA was -Rs 12.9 Cr and -Rs 1.2 Cr while sell-down doubled; tests whether off-book growth is bought at a loss | Positive gross gain; loss is EIS unwind timing | Gross gain near zero or negative | C | FN08, FND-06, A3-09 | NOT ADDRESSED. Only "the last quarter had a higher DA unwinding impact" (Call L140-141). |
| 6 | At what CRAR level will the board raise equity? | D/E 4.61x vs 6x cap, unchanged from Mar-26; CRAR 22.40% to 20.96% in H1; half the RoE gain is leverage | Not before CRAR 18%; accruals plus assignment fund FY27-FY28 | Raise within 12 months | F | A3-04, FN16, FND-07, FN-20 | PARTLY. No floor. CFO: growing ROE funds growth "through internal approvals" [ASR, read as accruals] (Call L129-130). |
| 7 | Which of the five FY27 guidance items from the Q1 call do you now revise: entity AUM +20-22%, gold AUM +25-30%, tonnage +10-12%, 200 branches, credit cost below 1%? | No guidance in deck or release; 3 of 5 run behind (entity AUM, tonnage, branches) and gold AUM is at risk on a price-flat basis | None revised | Tonnage or branch target cut | B | FN02, FND-13, FN-04 | ANSWERED, with a record mismatch. CEO: "I have not revised the AUM guidance or the ROA ... guidance" (Call L727). Restated: AUM about 20-25%, ROA +30-40 bps (Call L728-733), tonnage 10-12% (Call L885-886), at least 150 H2 branches (Call L188-189), credit cost "way below 1%" (Call L370). Gold AUM +25-30% not restated in number; the gold-growth answer reaffirms only "our guidance" (Call L248-249). |
| 8 | Will the company refile Q2 FY27 basic EPS? Printed 3.56; H1 6.54 less Q1 3.05 gives 3.49. | Filed EPS error appears twice; tests reporting control | Yes, corrected filing with date | No, or no answer | G | A3-10 | NOT ADDRESSED. |

### Extended rows (every remaining FORWARD-SIGNAL or AMBIGUOUS finding)

| # | Question | Why it matters | Bull answer | Bear answer | Cat. | Finding IDs | Call status (Role 5) |
|---|---|---|---|---|---|---|---|
| 9 | How many of the 126 remaining FY27 branches will open by 31-Mar-2027? | 74 of 200 opened in H1; opex +7.8% QoQ | 120 or more | Below 80 | B | FN15, FND-08 | ANSWERED. "At least another 150 branches in the second half" (Call L187-189, T05 explicit). The split has two parses [ASR] (Call L539-541): (a) about 75 in Q3 and 100 in Q4; (b) about 75 done in Q2 (filed 74, Deck R033), about 100 in Q3, more in Q4. Separating observation: Q3 FY27 additions, about 75 vs about 100. |
| 10 | What 12-month AUM per branch do you target for the 74 Q2 branches, in Rs Cr? | Gold AUM per branch fell 17.7 to 16.9; C/I fell only 36 bps | Rs 10 Cr or more | No target | A | FN15, FND-08 | PARTLY. Breakeven at Rs 6-7 Cr AUM, reached in 12-13 months (Call L714-722). The CEO ties the 12-13 months to a rising or current gold price (Call L715-L716, MFS-C21). The FY26 cohort he cites grew while gold value per gram rose about 38% YoY (Step 6D). The timeline is untested at a flat price, which is the guidance's own assumption. Below the bull bar. No target for the Q2 cohort. |
| 11 | What drove the Q2 ETR of 26.54% vs 25.17% statutory? | About Rs 2 Cr of PAT; current tax 29.53% of PBT | A named one-off | Recurring disallowance | D | A3-05, FN04, FND-01 | NOT ADDRESSED. |
| 12 | What is the outstanding FCY/ECB borrowing at 30-Sep-2026, in Rs Cr? | Q2 hedge OCI gain Rs 43.48 Cr exceeds FY26 full year Rs 31.82 Cr; explains Rs 26.62 Cr of non-PAT equity growth | Small, fully hedged to maturity | Large, partial hedge | F | A3-08, FN05, FND-04 | NOT ADDRESSED. Mix given only as 33% fixed, 24% MCLR, residual EBLR (Call L630-633). |
| 13 | What principal outstanding did the 48 accounts sold to ARCs carry, in Rs Cr? | NBV nil, consideration Rs 0.03 Cr, principal row (L525) blank | Small, fully written off earlier | Large write-off pool | D | A3-02 | NOT ADDRESSED. |
| 14 | What were total H1 FY27 write-offs, in Rs Cr? | Credit cost read is incomplete without write-offs | Below Rs 10 Cr | Above Rs 25 Cr | D | A3-02, FN09 | NOT ADDRESSED. |
| 15 | What makes up other financial liabilities of Rs 468.19 Cr at Sep-26 (Rs 216.38 Cr at Mar-26)? | +116% in H1; collections payable to assignees vs other build-up | Assignee collections payable | Margin money or unexplained payables | D | A3-12 | NOT ADDRESSED. |
| 16 | Who appointed V. Sankar Aiyar & Co. as joint statutory auditor, on what date, and under which rule? | First joint review this quarter; no board agenda item | AGM 29-Sep-2026 resolution under the RBI joint-audit rule | Mid-year appointment with no stated trigger | G | A3-03 | NOT ADDRESSED. |
| 17 | Does the trust deed define "total outstanding liability" as borrowings only? | Filed TOL/ATNW 4.61x is on 31-Mar-2026 audited figures (Res R743-R744) and equals Mar-26 D/E 4.61x; computed TOL/ATNW on the same Mar-26 figures is 4.79x | Yes, borrowings only | No; filed figure understated | G | A3-15 | NOT ADDRESSED. |
| 18 | How did the Federal Bank derivative margin deposit reach a Rs 16.16 Cr closing balance with nil opening and nil flow? | RPT table does not reconcile (OCR-garbled page) | Table error, corrected flow given | No answer | G | A3-16 | NOT ADDRESSED. |
| 19 | What is the Rs 1.85 Cr H1 brand-usage fee to Federal Bank based on, and from what date? | New related-party charge to promoter | Fixed fee at or below market, board-approved | Revenue-linked fee rising with AUM | G | A3-16 | NOT ADDRESSED. |
| 20 | What is Gross Stage 3 % for North-originated mortgages of FY25-FY26 vintage? | North mortgage share 6% (FY21) to 32%; unseasoned | Below the 3.4% book average | Above 4% | D | FN12 | NOT ADDRESSED. Only the generic mortgage-stage claim (Call L348-349). |
| 21 | What undrawn sanctioned lines did the company hold at 30-Sep-2026, in Rs Cr? | ALM below-3-month cumulative surplus only Rs 186 Cr on Rs 3,291 Cr outflows | Above Rs 1,500 Cr | Below Rs 500 Cr | F | FN17 | NOT ADDRESSED. |
| 22 | Is the Q2 FY26 column on the ECL slide on the same basis as Q1 and Q2 FY27? | Only that column carries the * and ^ markers; YoY PCR move may not be like-for-like | Yes, same basis | No; YoY coverage restated | D | FN20 | NOT ADDRESSED. |
| 23 | How many NAPS apprentices were on the rolls at 30-Sep-2026? | Headcount 5,920 excludes apprentices; productivity overstated | Fewer than 200 | More than 1,000 | G | FN21 | NOT ADDRESSED. |
| 24 | What were FY26 yield, CoB and spread on the old two-point basis? | Annual series restated this quarter; old decks not comparable | Change below 10 bps | Change above 25 bps, favourable to the new series | C | FN24 | NOT ADDRESSED. |
| 25 | Which CoB series does management steer on: slide 25 Ind-AS 7.9% or the daily I-GAAP 7.79%? | Two series on mixed bases; earlier read showed a gap (FN25 now dissolved by the XC correction) | One named series, reconciled | No answer | C | FN25, FN22, FN-07 | PARTLY. CFO cites "weighted average cost of borrowing ... flat ... at 7.80", "represented in the funding profile slide" (Call L141-144), i.e. the daily I-GAAP series. Not reconciled to slide 25. |
| 26 | Is the H1 FY27 Shareholder's Fund cell of Rs 2,926.1 Cr in the press release the 31-Mar-2026 opening balance? | Two net-worth values for one date (7.5% gap); 2,926.1 equals FY26 SF (Deck R169) | Yes, opening balance; label fixed | Unexplained | G | FND-03 | NOT ADDRESSED. |
| 27 | Why did other income fall 1.9% YoY to Rs 27.78 Cr while AUM grew 36.6%? | Fee and cross-sell yield on the book is shrinking | Treasury-only decline; fees up | Fee income lost | C | FND-09 | NOT ADDRESSED. Adjacent fact: insurance income about 0.1% of the ROA tree in FY26 (Call L904-905). Other income / ATA 0.9% to 0.6% YoY (Deck R1030, R1032). |
| 28 | Is the 0.6% credit cost computed on two-point or daily average total assets? | Tripwire basis; Notion mixes AUM and asset bases | Two-point average, same as tripwire | Undefined | D | FND-12 | PARTLY. "approximately 0.6% of the average total assets as an annualized basis" (Call L87-88). Averaging method not stated. |
| 29 | Publish gold 30+ and 60+ DPD for Q2 FY27 (carried from Q1 Q4, not addressed). | Early-warning for gold Stage 2/3 | Disclosed, stable | Refused again | D | carried; A3-11; FN-19 | NOT ADDRESSED, second consecutive quarter. |
| 30 | Give the bridge for the Stage 3 ECL move from Rs 96.8 Cr to Rs 104.7 Cr (carried from Q1 Q9). | Second quarter without a provision bridge | Bridge given | Not addressed again (governance signal) | D | carried; FN09; FN-19 | PARTLY. Mechanism only: PCR fell "due to a higher proportion of gold loans in stage three"; "mortgage PCR continues at similar levels" (Call L167-171, T05 explicit). No bridge. |
| 31 | Through which route did the Rs 208 Cr of the Q2 sell-down not filed as direct assignment leave the book: co-lending, securitisation, or other? | Deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr; CLM is a listed funding source of unresolved size | Co-lending with a named bank partner, disclosed | No reconciliation given | E | FN07, A3-12, FND-07 | PARTLY. Co-lending in gold named as a second route: "aided by higher coal ending [ASR: co-lending] in the gold portfolio" (Call L148-150); "direct assignment and co-lending business normalized" (Call L92-94). No size, no partner. |

### New rows from the concall (every A3 concall FORWARD-SIGNAL and AMBIGUOUS finding)

| # | Question | Why it matters | Bull answer | Bear answer | Cat. | Finding IDs | Call status (Role 5) |
|---|---|---|---|---|---|---|---|
| 32 | How many gold auctions ran in Q2 FY27, at what value in Rs Cr, and was any shortfall written off against principal or interest? Confirm the wording of the six-year record. | The one nil claim on the call rests on a garbled negation (Call L420); management is "fully geared" for auctions (Call L400-401) while Stage 2 rises | Auction value small; nil shortfall confirmed in writing | Rising auction volume or any shortfall | D | FN-01 | NEW (call) |
| 33 | What share of gold Stage 2 at 30-Jun-2026 rolled to Stage 3 by 30-Sep-2026, and at what gold Stage 2 % do you expect the peak? | The CEO declined a peak call and a Stage 2 number (Call L387-394); Stage 2 2.7% to 3.6% (Deck R705-R706) | Roll rate below 10%; peak named at or below 4% | No roll data; Stage 2 keeps rising in Q3 | D | FN-02, FN-14 | NEW (call) |
| 34 | What PCR floor will the board accept as gold reaches 55-60% of AUM? Give Stage 3 PCR by product (gold, mortgage, business loans) for Q1 and Q2 FY27. | PCR fell 299 bps; each gold Stage 3 step pulls the blend toward the 32% tripwire; floor silent two quarters | Floor at or above 33% with mortgage PCR held | No floor; mortgage PCR below 35% | D | FN-03, FN-16 | NEW (call) |
| 35 | Publish FY27 guidance in writing, split entity AUM and gold AUM. Is gold AUM still +25-30%? Was the Q1 ROA guide +20-30 or +30-40 bps? | The CEO says guidance is unchanged; the restated bands differ from the Q1 log; gold AUM was reaffirmed only as "our guidance", with no number (Call L248-249) | Written table matches the call; gold +25-30% kept | Gold guide cut, or no written table | B | FN-04 | NEW (call) |
| 36 | In which quarter do you expect ROA of 3%, and what ROE target goes with it? | ROA 3% pulled forward "sooner" (Call L947-948); the ROE number is inaudible [ASR] (Call L736); the CFO calls 15% an "interim" ROE milestone (Call L113, MFS-C2), so a higher ROE target exists; Q2 ROA 2.8% already at the top of the restated band | A dated quarter in FY28 with a named ROE | No date | B | FN-05 | NEW (call) |
| 37 | What gold yield change do you plan for in Q3 FY27, and what share of borrowings reprices within three months of a 50 bp rate rise? | Yield guide declined; Q3 "intense"; residual about 43% EBLR-linked (Call L630-633); NIM compression to be offset by "some other operating labor" [ASR: lever] (Call L661-662), named only as opex and credit cost (Call L567, L689-L695) | Yield held within 20 bps; repricing share below 40% | Yield cut above 50 bps with fast CoF transmission | C | FN-06, FN-14 | NEW (call) |
| 38 | Give core yield ex-DA and cost of borrowing on one stated basis for Q1 and Q2 FY27, and the DA-unwinding effect in bps each quarter. | CFO: core yield "constant ... at 16.40"; the 29 bp rise is DA unwinding (Call L138-141). The 16.40 ties only to the Q1 reported yield; ex-DA core derives to about 16.7% in both quarters (Step 7A). CoB quoted on the daily I-GAAP basis | One basis, reconciled to slide 25 | Mixed bases again | C | FN-07 | NEW (call) |
| 39 | How much DA excess-spread unwinding, in Rs Cr, will hit NII in each of the next four quarters, and when does net DA income turn neutral? | Record Q2 assignment; schedule silent two quarters (partial) | Schedule given; neutral by Q4 FY27 | No schedule | C | FN-21, FN-08 | NEW (call) |
| 40 | Give the product split of the Rs 876.89 Cr Note 10(II) assignment, against the spoken "approximately 700 crores of the gold loan book". Why is the weighted residual maturity 23 months? How does a record sell-down fit "reduce reliance on direct assignment"? | Spoken vs filed gap Rs 177 Cr; 23-month residual (Res R473) is long for a gold pool with a 2.5-3 month behavioural tenor (Call L355-357); stated priority (Call L56, MFS-C11) vs record Rs 1,085 Cr (Deck R680) | Rs 700 Cr gold plus Rs 177 Cr mortgage pools, named; Q3 sell-down lower | No split; Q3 sell-down higher | E | FN-08 | NEW (call) |
| 41 | Give disbursal-weighted gold LTV for Q1 and Q2 FY27, the share of the gold book above 75% LTV, and the share that crosses the LTV limit at a 10% and a 15% gold-price fall. | Book LTV 68% (Call L66) vs working mix 72-74% (Call L500-501); Jagdish: 90-95% of customers want the maximum their exposure slab allows, 75% or 80% (Call L480-L483, MFS-C3, MFS-C4). CEO: the company plays the LTV minus or two percent, and the working mix is 72-74%, not everybody at that highest one (Call L497-L506). Filed average origination LTV is 72.1% (Deck R327), below both caps. The share of new loans at the cap is ND; this row asks for it. IGL up to 85% on 20% of disbursal (Call L321, L484); no price-down case on the call | Above-75% share below 15%; small breach share at -15% | Above-75% share over 30%, or no answer | D | FN-09, FN-18 | NEW (call) |
| 42 | Confirm the ST LAP disbursal series for the last nine quarters and the Q3 FY27 bar it must beat. Give 1+ DPD on loans approved at the early/mid-40s approval rate. | Dated Q3 promise: "best quarter compared to the last eight or nine quarters" (Call L588-591); approval rate 30% to early/mid-40s (Call L799-800) in an "aggressive" market (Call L773-774). Rs 289 Cr (Q4 FY26) is the highest of the six known quarters (Deck R475-R479; Q1 FY26 derived Rs 201 Cr); FY25 quarters are not in the run, so the true bar may be higher | Q3 above the confirmed bar (at least Rs 289 Cr) with 1+ DPD below 2% | Q3 below Rs 289 Cr, or DPD rising | A | FN-10, FN-14 | NEW (call) |
| 43 | What gold tonnage do you target at 31-Dec-2026, in tonnes? | FY27 guide needs 13.86-14.11 t from 12.9 t; H2 "different trajectory" (Call L670) | 13.4 t or more | Below 13.2 t | B | FN-11 | NEW (call) |
| 44 | What H2 FY27 cost-to-income ceiling do you commit to with at least 150 new branches? | CFO only "hopeful of containing" C/I at about 52.5% (Call L190-192); opex / ATA 4.8% to 4.9% (Deck R1039-R1040) | Ceiling at or below 53% | No ceiling; C/I rises above 54% | A | FN-12 | NEW (call) |
| 45 | Which insurance-distribution change do you expect, by when, and which income line substitutes about 10 bps of ROA? | Raised unprompted in prepared remarks (Call L197-199); framed "whenever" (Call L906); about 0.1% of ROA (Call L904-905) | Named, small, substitute line named | Named, dated, no substitute | C | FN-13 | NEW (call) |
| 46 | Confirm the date ST LAP collections in-housing was completed. | Checklist item 7; silent two quarters; management says ST LAP credit cost has normalised (Call L455-458) | Completed, dated | Not complete | D | FN-17 | NEW (call) |
| 47 | How many co-lending partners do you have, is Federal Bank one, and what co-lending volume ran in Q2 FY27, in Rs Cr? | Co-lending named as a de-leveraging route (Call L149) with no size; parent-funded co-lending is a Notion growth trigger | Several partners, volume disclosed | No disclosure | E | FN-20 | NEW (call) |

Top 3 by likelihood of thesis-changing information:
- Bull probability: Q1 (Stage 2 gold share). A high gold share supports the mix reading and the 1.00x Pillar 2L. The call asserted "entirely" gold without a number.
- Bear confirmation: Q5 (gross DA gain). A near-zero gross gain means off-book growth is bought, and Q2 profit quality is weaker.
- Transparency test: Q35 (written FY27 guidance, entity vs gold) and Q8 (EPS refiling).

Channel recommendation: transcript read (ASR). Send an IR email with the 28 rows the call did not close (20 NOT ADDRESSED, 8 PARTLY) and rows 32-47 verbatim. Priority: rows 1, 2, 4, 5, 33, 34, 35, 40.

---

## STEP 9 NOTION UPDATE (payload only; this stage writes nothing)

- Decision Status: not written. Proposed: no change.
- Key Notes prepend (proposed): "2026-10-19 | Q2 FY27 results + call: PAT Rs 130.75 Cr (+63.1% YoY), ROE 17.0%; PCR 38.36% to 35.37%, stressed coverage 24.5% to 20.2%; call (ASR) keeps credit cost 'way below 1%', GNPA below 2%, AUM 20-25% on flat gold, ROA 3% 'sooner'; Stage 2 peak, gold yield and ST LAP numbers declined; record Rs 1,085 Cr sell-down against 'reduce reliance on DA'; credibility ratio ND; no tripwire fired; Pillar 2L self-withdraw condition met QoQ, operator to rule."
- Properties to refresh at the write gate: CMP (stale 164); gold mix (page says ~46.5%; Q2 54.1%, Deck R315); secured share (page 98.9%; Q2 99.4%, Deck R064). Promoter Verdict: no change (CAUTION). Management Grade: ND (Role 5 Step 3D).
- Sections to append: all tables above in full, then the Role 5 section below in full under "Q2 FY27 Concall Analysis".
- Promise log to save for the Q3 FY27 review: concall commitments C01-C26 (Role 5 Step 3B) and the 47-row Questions table.

---

## ROLE 5 CONCALL ANALYSIS (Quarterly Concall Analysis Protocol v1.1)

Source: Q2 FY27 post-results earnings call of Fedbank Financial Services. Machine transcript (faster-whisper ASR) of the company's audio file, 68m32s, 952 fulltext lines (Call L1-L21). No speaker labels: A1 inferred the speaker in 52 of 74 turns. Explicit turns include the IR safe-harbour (T03) and the CFO's prepared remarks (T05). Garbled passages: Call L133-135 (label of "205.1 crore" lost; YoY "40. 7.5%"), L152-153 (comparative word lost), L420 (auction-loss negation), L736 (ROE target number), L826. Conclusions that rest on them carry [ASR]. Reading rule: adversarial, bear interpretation when ambiguous (Role 5 style rules; Role 4 OR-26 conservative bias on filed evidence). The filing wins every conflict.

### R5 STEP 0 PRE-FLIGHT

0A. Notion (live copy, Role 4 Step 0A). Decision Status WATCHLIST / AVOID (DEEP WATCH), verified before framing. Not held. One-line thesis: ND on the page copy. Growth triggers: Role 4 Step 6D (10 rows). Thesis-broken conditions: three tripwires (Role 4 Step 6C). Checklist: 8 items (Role 4 Step 6B). Promoter Verdict CAUTION; Management Grade ND (not on the page). Devil's Advocate findings: ND (not passed). Previous concall log: Q1 FY27 promise log (9 items) and Q1 FY27 Questions (10 rows) plus AR top 3, all passed. This is the second call under Role 5 (the Q1 FY27 review of 2026-07-22 was concall-sourced). Trailing history passed: Q1 FY27 only.

0B. Call participants

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Sreepal Toshi, Aquarius Securities (Call R151-R152, L30-36) | Independence ND. The host asked no question. |
| CMD / Chairman | none on the call | Promoter Federal Bank (60.6%, Deck R226) not represented (ledger MGMT_ABSENCE). Protocol yellow flag. For a bank-promoted NBFC run by professional managers this is the normal structure [INFERENCE]. |
| Managing Director & CEO | Parvez Mulla (Call R153; ASR "Pervase Bula") | Took most of the Q&A, including asset quality, guidance and competition (T08-T73, inferred). |
| CEO | same as MD | n/a |
| CFO | C.V. Ganesh (Call R154; ASR "Sivi Ganesh") | Prepared remarks T05 (explicit). Answered borrowing mix (T40), spread (T42), rate shock (T47), insurance (T68): all financial. Add-on on auctions (T19, inferred). No CFO-on-operations yellow flag. |
| COO / Other senior | Jagdish Rao, head of gold and ST LAP (Call R156) | Answered IGL structure and LTV (T12, T25, inferred). Sharadur Kadam, Suresh Pumar (MT LAP), Vikram Rati named, no identified turn (Call R157-R159; NO_TURN_IDENTIFIED). |
| IR Advisor | Lokesh Parik, in-house IR head (Call R155) | Safe-harbour and hand-over only (T03). |

Yellow flags: promoter absent (noted). No new senior manager without introduction. IR did not dominate. No leadership change visible on the list.

0C. Call structure
- Date: ND in the transcript. The deck cover letter of 15-Oct-2026 says the presentation "is referred during the Earnings call" (Deck fulltext L18, L30-35). Call held on or after 15-Oct-2026 [INFERENCE]. Board approval 15-Oct-2026 (Res R698). Filing-to-call lag: ND.
- Quarter: Q2 FY27 (Call R234).
- Duration: 68m32s (Call L6). Above 60 minutes.
- Prepared remarks 00:01:13 to 00:14:46 (Call L37-L202), about 13.5 minutes. Q&A 00:14:54 to the last answer at 01:07:02 (Call L205-L924), about 52.1 minutes, 76% of the call (derived). The closing remarks run on to 01:08:19 (Call L928-L949).
- Analysts who asked: 9. Questions: 26 (9 primary, 14 follow-up, 3 embedded in mixed turns T47, T50, T51) (ledger Section 3).

0D. Safe harbour: two sentences (Call L39-42), covering financial performance, business strategy and growth plans. Narrow. The prior call's caveat text is ND, so no caveat diff is possible. New risk language sits in the CFO's prepared remarks, not in the caveat: "shock buffers to potential headwinds on the interest rates or any insurance distribution related changes" (Call L197-199) (FN-13).

0E. Business type: **LENDING BUSINESS (NBFC)**. Step 2L applies.

Checkpoint: Notion fetched, participants listed, structure noted, caveats logged, business type stated.

### R5 STEP 1 OPENING REMARKS: CLAIMS INVENTORY (T04 CEO, T05 CFO)

| # | Claim | Type | Quantified? | Source Line |
|---|---|---|---|---|
| 1 | Same set of priorities for the last six quarters, unchanged | Strategic | NO | Call L52-53 |
| 2 | Grow core income while "consciously reduce our reliance on direct assignment" | Strategic | NO | Call L56 (MFS-C11) |
| 3 | Hold credit costs below 1% | Forward Guidance | YES | Call L57 (MFS-C1, MFS-C12) |
| 4 | Total disbursements +28% YoY to Rs 6,676 Cr | Backward | YES | Call L60-61 |
| 5 | AUM +37% YoY to Rs 22,035 Cr | Backward | YES | Call L61 |
| 6 | Gold disbursements Rs 5,822 (unit not spoken), +31% YoY | Backward | YES | Call L62-63 |
| 7 | Gold AUM +77% YoY to Rs 11,917 Cr | Backward | YES | Call L63 |
| 8 | Doorstep gold AUM Rs 1,851 Cr | Backward | YES | Call L63-64 |
| 9 | AUM per branch after branch opening Rs 16.9 Cr | Operational | YES | Call L65 |
| 10 | Gold tonnage +16% YoY | Operational | YES | Call L65-66 |
| 11 | 68% LTV, well within regulatory limits | Operational | YES | Call L66-67 |
| 12 | 74 branches opened; "total gold branch count to 831. Total branch count to 831." | Operational | YES (misspoken: gold 706, Deck R496) | Call L67-68 |
| 13 | Expect to continue or expand the branch network in H2 | Forward Soft | NO | Call L68-69 |
| 14 | Entry into eastern India this quarter | Strategic | YES (binary, done) | Call L69-70 |
| 15 | Revised gold lending LTV framework still working through the system | Macro/Tailwind | NO | Call L71-72 |
| 16 | Gold GNPA 0.5% reflects the transition, "not a structural credit concern" | Backward | YES | Call L73-74 |
| 17 | Mortgage disbursements +12% YoY to Rs 855 Cr; mortgage AUM +13.5% to Rs 9,982 Cr | Backward | YES | Call L75-78 |
| 18 | MT LAP disbursed Rs 645 Cr, +16% YoY, yields stable | Backward | YES | Call L80-82 |
| 19 | ST LAP and housing disbursed Rs 210 Cr; BRE underwriting lowers credit cost | Backward | YES | Call L82-84 |
| 20 | Unsecured loans under 1% of on-book assets | Backward | YES | Call L85-86 |
| 21 | Credit cost Rs 27 Cr, about 0.6% of average total assets annualised, within "around below 1%" | Backward | YES | Call L87-89 |
| 22 | PAT Rs 130.8 Cr, +63% YoY; ROA 2.8% (spoken "ROE"); ROE 17% | Backward | YES | Call L89-90 |
| 23 | GNPA 1.8% from 1.6%, from the gold transition and flattish AUF after DA and co-lending | Backward | YES | Call L91-94 |
| 24 | NNPA 1.2%; PCR 35.4% | Backward | YES | Call L94 |
| 25 | GNPA and NNPA improved YoY | Backward | NO | Call L94-95 |
| 26 | CRAR 21%; book value per share 84.4 (spoken "%") | Backward | YES | Call L95-96 |
| 27 | Business "growing well with improving asset quality", highest ever ROE 17% | Strategic | NO | Call L96-98 |
| 28 | The foundation "positions us well for the quarters ahead" | Forward Soft | NO | Call L98-100 (MFS-C13) |
| 29 | Q2 FY27 strongest quarter to date in profitability and operating metrics | Backward | NO | Call L108-109 |
| 30 | ROA +24 bps QoQ to 2.8%; 2.1% to 2.8% over nine quarters | Backward | YES | Call L116-118 |
| 31 | ROE +153 bps QoQ to 17%; 10.9% to 17% over nine quarters | Backward | YES | Call L119-122 |
| 32 | "We remain optimistic on continuing on this trajectory" | Forward Soft | NO | Call L123 |
| 33 | AUM from a little over Rs 20,000 Cr to Rs 22,000 Cr in September, +9% in H1 | Backward | YES | Call L124-126 |
| 34 | Credit cost -18 bps, 0.78% to 0.6%, as mortgage flows improved | Backward | YES | Call L127-128 |
| 35 | Growing ROE funds book growth "through internal approvals" [ASR: accruals] | Strategic | NO | Call L129-130 |
| 36 | Core NII +5.2% QoQ to Rs 404.8 Cr, +40.9% YoY | Backward | YES | Call L132-133 |
| 37 | [label lost, PPOP] Rs 205.1 Cr, +9.4% QoQ, YoY "40. 7.5%" [ASR] | Backward | YES | Call L133-135 |
| 38 | Credit cost Rs 27.1 Cr, -20.5% QoQ from Rs 34.1 Cr, from mortgage collection efficiency | Backward | YES | Call L135-136 |
| 39 | PAT Rs 130.8 Cr, +14.3% QoQ, about +63.1% YoY | Backward | YES | Call L137-138 |
| 40 | Core yield constant at 16.40; the 29 bp "optical increase" is Q1 DA unwinding | Backward | YES | Call L138-141 |
| 41 | Weighted average CoB flat at 7.80, same as the previous three quarters | Backward | YES | Call L141-144 |
| 42 | 33% fixed-rate and 24% MCLR-linked borrowings insulate against rising rates | Operational | YES | Call L144-147 |
| 43 | DA of about Rs 700 Cr of the gold book plus co-lending [ASR "coal ending"] cut D/E 4.9 to 4.6; CRAR 21% from 20.7% | Backward | YES | Call L148-151 |
| 44 | Mortgage delinquency across stages [comparative lost] than the previous quarter [ASR] | Backward | NO | Call L152-153 |
| 45 | The shift from bullet to periodic interest, guided in Q1, raises technical delinquencies | Macro/Tailwind | NO | Call L154-159 |
| 46 | Stage 2 2.7% to 3.6%, Stage 3 1.6% to 1.8%, "entirely" from the gold change | Backward | YES | Call L160-161 |
| 47 | "Sufficiently collateralized"; no enhanced risk | Strategic | NO | Call L162-163 |
| 48 | Record low net slippages in the mortgage book; best quarter to date | Backward | NO | Call L164-166 |
| 49 | PCR 38.4% to 35.5% from more gold in Stage 3; mortgage PCR similar | Backward | YES | Call L167-171 |
| 50 | Opex / ATA 4.9% vs 4.8% in Q1, from 5.5% in FY26 | Backward | YES | Call L173-178 |
| 51 | Structural reduction in cost intensity "remains intact" | Forward Soft | NO | Call L179-180 |
| 52 | C/I 52.5% vs 52.8% in Q1; FY26 57.2% | Backward | YES | Call L181-184 |
| 53 | "At least another 150 branches in the second half of the year" | Forward Guidance | YES | Call L187-189 |
| 54 | "Hopeful of containing any material increases in cost to income over current levels" | Forward Soft | NO | Call L190-193 |
| 55 | Shock buffers to rate and insurance-distribution headwinds | Macro/Tailwind | NO | Call L194-199 |
| 56 | "Turbulent headwinds" and "lack of momentum and gold prices"; the resilience theme continues | Macro/Tailwind | NO | Call L106-107 |
| 57 | A model built for a "consistent non-cyclical" upward ROA and ROE path over eight to nine quarters | Strategic | NO | Call L110-112 |
| 58 | Crossed the "interim ROE milestone of 15 percent" last quarter (Q1 ROE 15.4%, Deck R868) | Backward | YES | Call L113 (MFS-C2) |

Diagnostics:
- Quantified share: 39 of 58 claims (67%). Forward-typed claims (Forward Guidance or Forward Soft) are rows 3, 13, 28, 32, 51, 53 and 54: 2 of 7 quantified (29%). Macro/Tailwind rows 15, 45, 55 and 56 are not counted as forward. Rows 56-58 were added in Role 5 loop 1 (A5 M15), out of line order, so the other row numbers stay stable. The opening is backward-heavy and specific. Its forward content is soft.
- New vs reaffirmation: new are eastern India entry (14), at least 150 H2 branches (53, above the 200 FY27 log), DA plus co-lending as the de-leveraging route (43) and the insurance-distribution headwind (55). Reaffirmed are credit cost below 1% (3), the periodic-interest technical delinquency guided in Q1 (45) and the 15% interim ROE milestone shared last quarter (58). "Interim" implies a higher ROE target, which the call leaves inaudible (Call L736; Step 8.5 row 36).
- Quietly dropped from the opening: gold AUM +25-30%, tonnage +10-12% and entity AUM +20-22% (the last two reappear in Q&A as 10-12% and 20-25%; gold AUM never reappears as a number, and the gold-growth answer reaffirms only "our guidance", Call L248-L249, L292-L293). Also dropped: DA income outlook and the PCR floor.
- Internal contradictions: (a) "improving asset quality" (row 27) vs GNPA 1.6% to 1.8% and Stage 2 2.7% to 3.6% stated minutes later (rows 23, 46); (b) "reduce our reliance on direct assignment" (row 2) vs "direct assignments of approximately 700 crores ... to de-leverage" (row 43); (c) "total gold branch count to 831" and "total branch count to 831" in the same sentence (row 12).

Checkpoint: inventory and four diagnostics shown.

### R5 STEP 2L LENDER GUIDANCE SET

| Metric | This Quarter's Guidance | Last Quarter's (Q1 FY27 log) | Two Quarters Ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| AUM / loan book growth (FY27) | "about 20 to 25%" on a flat gold price; better if gold rises (Call L733, L757-759, L888; Call R216, R219) = Rs 24,184-25,191 Cr (derived on Rs 20,153 Cr) | Entity AUM +20-22% = Rs 24,184-24,587 Cr (Notion) | CEO: "20 to 25 percent ... in the month of March" (Call L729-730); Notion record ND | Widened upward at the top end vs the log; management says Maintained | MEDIUM (band, "about", conditional on flat gold) |
| Disbursement target | No FY number. ST LAP Q3 "the best quarter compared to the last eight or nine quarters"; Q3 disbursals above Q2 (Call L588-591, L611-613) | ND | ND | New | MEDIUM (binary and dated, no number) |
| NIM / spread band | Declined: "It will be wrong of me to give you a guidance that we will play with a flattish yield" (Call L307-309). "If there is a nim compression, we will handle it" via other levers (Call L661-662), named only as opex and credit cost (Call L567, L689-L695). Limited pass-through (Call L681-683). | ND | ND | New (negative direction) | LOW |
| **Credit cost guided band (THE CRITICAL ONE)** | "way below 1%" (Call L370); "below 1%" (Call L57, L89); "committed to the guidances ... on our credit cost" (Call L943-944) | Below 1% FY27 | Below 1% (Notion: sub-1% FY27 guide) | Maintained (tone tightened) | HIGH |
| GNPA trajectory commitment | "below 2%", said "last year as well as the start of the year" (Call L372-373) | ND in the log | Per CEO, given last year (Call L372) | Maintained per management; new to the Notion log | MEDIUM-HIGH |
| Collection efficiency target | ND. Only "improving collection efficiencies on the mortgage book" (Call L136) | ND | ND | none | n/a |
| Cost-to-income target | "hopeful of containing any material increases ... over current levels" (about 52.5%, Call L181, L190-192); keep reducing non-branch opex (Call L553, L567-569) | ND (checklist: falling into FY27) | ND | New, softened | LOW |
| RoA / RoE target | ROA +30-40 bps over FY26 about 2.4% = 2.7-2.8% (Call L728-729); ROA 3% "sooner than we had promised" (Call L947-948); ROE target number inaudible [ASR] (Call L736); 15% called an "interim" ROE milestone (Call L113, MFS-C2) | ROA +20-30 bps = 2.6-2.7% | ND | Raised (management says not revised) | MEDIUM |
| Capital raise / CRAR plan | No raise implied: growth funded "through internal approvals" [ASR: accruals] (Call L129); CRAR 21% (Call L150) | De-leverage "we hope" | ND | Maintained (implicit) | LOW |
| Branch / geography expansion | "At least another 150 branches" in H2 (Call L187-189). Split, two parses [ASR] (Call L539-541): (a) about 75 in Q3 and 100 in Q4; (b) about 75 done in Q2 (filed 74, Deck R033), about 100 in Q3, more in Q4. Separating observation: Q3 FY27 additions. Eastern India entered (Call L69) | 200 branches FY27 | ND | Raised (74 + 150 = 224) | MEDIUM-HIGH |
| Gold tonnage (added lender row) | "10-12% every year. We will continue that" (Call L885-886); "different trajectory in H2" (Call L670) | +10-12% FY27, H2-weighted | ND | Maintained | MEDIUM |
| Gold AUM (added lender row) | Not restated in number; reaffirmed only as "our guidance" (Call L248-L249, L292-L293) | +25-30% FY27, price flat | ND | Not restated in number (DROPPED candidate stays open) | n/a |

Diagnostics:
- Widen or tighten: AUM top end +3 pts, ROA band +10 bps and branches +24 vs the log, all claimed as unchanged. Credit cost tone tightened. Gold AUM was not restated in number. NIM guidance declined.
- Dropped without acknowledgment: gold AUM +25-30% (candidate). The CEO's "20-25% growth on the AVM" at Call L888 sits in a gold-ROE answer. Three readings: (a) the entity guide rose to 20-25% and the gold guide was left out; (b) the gold guide was cut from 25-30% to 20-25%; (c) the gold guide was reaffirmed without a number in the gold-growth answer ("we will continue with our guidance in Q3 and Q4 as well", Call L248-L249; "perform to our guidance ... on AUM", Call L292-L293). The separating observation is a written guidance table split by entity and gold (row 35). A further possibility: ASR misheard numbers, or the Q1 Notion log carries an error. The Q1 transcript would settle it.
- Internal consistency (derived): the 20% entity floor needs Rs 24,184 Cr, i.e. +9.8% in H2 from Rs 22,035 Cr. At a flat gold price and flat LTV, gold grows at the tonnage pace: +7.4% to +9.4% in H2 (12.9 t to 13.86-14.11 t), so gold reaches Rs 12,799-13,037 Cr. Non-gold AUM must then reach Rs 11,147-11,385 Cr, +10.2% to +12.5% in H2, against +3.2% in H1 (Rs 9,801 to 10,118 Cr, Role 4 Step 6D). The guidance reconciles only if non-gold growth triples, LTV rises toward the 72.1% origination level (Deck R327), or the gold price rises. Management's own framing excludes the last.
- Vs Four-Pillar projections: ND (no projections on the Notion page).
- Refused under analyst pressure: gold yield and spread path (Shubranshu T10, Meghna T41, Devansh T46); Stage 2 number and peak (Ranish T17); ST LAP H2 numbers (Pawan T35); a guidance upgrade (Yash, T51, Call L743-L746).

Checkpoint: guidance table and diagnostics shown.

### R5 STEP 3 PROMISE vs DELIVERY AUDIT

3A. Q1 FY27 commitments: delivery status (v1.1 points)

| Commitment From Q1 FY27 Concall | This Quarter's Actual | Status | Points |
|---|---|---|---|
| Credit cost below 1% FY27 | H1 0.69% annualised (derived); Q2 0.6% (Deck R1048) | UNCLEAR (FY27 not closed; on track) | excluded |
| ROA +20-30 bps over FY26 2.4% | H1 2.7% (PR R151); Q2 2.8% (Deck R863) | UNCLEAR (FY27 not closed; at the top of the band) | excluded |
| 200 branches in FY27 | 74 in H1 (Deck R033); at least 150 planned for H2 (Call L188) | UNCLEAR (FY27 not closed; behind the linear pace of 100) | excluded |
| Gold AUM +25-30% (price flat) | +15.1% in H1 (derived, Role 4 Step 1L-c); not restated in number on the call, reaffirmed only as "our guidance" (Call L248-L249) | UNCLEAR, DROPPED candidate (FN-04) | excluded. Scores 0 with a governance flag if the written guidance omits it. |
| Gold tonnage +10-12% | +2.4% in H1 (Deck R489, R491); reaffirmed (Call L885-886) | UNCLEAR (FY27 not closed; H2-weighted) | excluded |
| Entity AUM +20-22% | +9.3% in H1 (derived); restated as 20-25% (Call L733) | UNCLEAR (FY27 not closed; Q2 pace about +18.8%) | excluded |
| De-leverage "we hope" | D/E 4.89x to 4.61x, equal to Mar-26 (Res R388-R390) | Not scored: hedge language, not a commitment (Role 5 failure mode 2). Q2 reversed Q1's rise; H1 net nil. | n/a |
| PCR "optically reducing going forward" | 38.36% to 35.37% (Res R441, R440) | Not scored: directional, unquantified. Came true. | n/a |
| DA income negative going forward | -Rs 1.2 Cr Q2 (PR R027) | Not scored: directional, unquantified. Came true. | n/a |

3B. Cumulative track record (trailing four concalls)

| Concall Date | Total Commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| Q2 FY26 call | ND (log not passed) | ND | ND | ND | ND | ND | ND | ND |
| Q3 FY26 call | ND (log not passed) | ND | ND | ND | ND | ND | ND | ND |
| Q4 FY26 call | ND (log not passed) | ND | ND | ND | ND | ND | ND | ND |
| Q1 FY27 call (review 2026-07-22) | 6 quantified | 0 | 0 | 0 | 0 | 0 (1 candidate) | 6 | 0 |
| Total | 6 | 0 | 0 | 0 | 0 | 0 | 6 | 0 |

Credibility Ratio = 0 / (6 - 6) = **ND**. No scorable commitment exists: all six quantified Q1 commitments are FY27 full-year targets, measurable at the Q4 FY27 review. Grade: **ND**. Role 1 Track Record input: **ND**. No session judgment substitutes for the ratio (Role 5 3B). DROPPED governance rule: 0 confirmed of the 2 needed; not fired.
Q2 FY27 call register for the next reviews: 26 commitments (C01-C26, concall A3 F6). Four are self-reported complete (C16 ST LAP credit-cost stabilisation, C17 IGL live since April, C18 DA de-leveraging, C26 eastern India). C18's spoken Rs 700 Cr differs from the filed Rs 876.89 Cr; it is scored at the Q3 review.

3C. Patterns
- Ratios deliver; volumes lag. Credit cost and ROA run on or ahead of guide. Tonnage (+2.4% in H1), branches (74 of 200) and entity AUM (+9.3% in H1) run behind. Management moves the volume load to H2 (Call L264-267, L669-670, L187-189).
- Restatement without acknowledgment. The CEO says the guidance has not changed since March and July (Call L727-731). The restated ROA and AUM bands differ from the Q1 log, and the gold AUM guide is absent as a number (FN-04). [ASR or Notion log error possible.]
- Quiet drops: one candidate (gold AUM). No confirmed DROPPED.
- Ratio trend: ND. No scorable history.

3D. Promoter Verdict / Management Grade: Promoter Verdict CAUTION, no change proposed. Management Grade ND (not on the page; no ratio). Downgrade rules: none fired. There are no confirmed DROPPEDs and no three consecutive misses on one metric. Repeated silence stands at two quarters (3E).

3E. Q1 FY27 Questions for Management: answered on this call?

| Q1 FY27 Question | Answer Status | If Answered, What Was Said | Verdict |
|---|---|---|---|
| 1. Branches opened in Q2; H1 count vs 200 | ANSWERED SPECIFICALLY | 74 in Q2 (Call L67, L187); at least 150 more in H2 (Call L188-189) | Closed |
| 2. Absolute gold tonnage; split of the 25-30% guide into tonnage / LTV / price | PARTIALLY ANSWERED | +16% YoY tonnage (Call L65-66); H2 tonnage trajectory (Call L669-670); no absolute tonnes and no split | Carry (row 43) |
| 3. Does the full FY27 stack hold; which leg is weakest | PARTIALLY ANSWERED | "committed to the guidances ... credit cost as well as AUM growth" (Call L943-945); weakest leg not named; gold AUM not restated in number | Carry (row 35) |
| 4. Gold 1+/30+/60+ DPD, bullet vs periodic | NOT ADDRESSED | n/a | Second consecutive quarter (row 29) |
| 5. PCR floor; gold-only vs mortgage-only PCR | PARTIALLY ANSWERED | Mix mechanism; "mortgage PCR continues at similar levels" (Call L167-171); no floor | Second quarter without a floor (row 34) |
| 6. CLM/DA timeline, partner count, de-leverage, CRAR floor | PARTIALLY ANSWERED | D/E 4.9 to 4.6 via DA of about Rs 700 Cr and gold co-lending (Call L148-150); no partner count, no CRAR floor | Carry (rows 6, 47) |
| 7. DA-unwinding drag next four quarters; DA-neutral date | PARTIALLY ANSWERED | Q1 drag about 29 bps of yield (Call L140-141); no forward schedule | Carry (row 39) |
| 8. FVOCI loss ("~585cr") and ECL re-recognition | NOT ADDRESSED | n/a | Second consecutive quarter |
| 9. Bridge for the ~Rs 40 Cr GS3 provision reduction | NOT ADDRESSED | n/a | Second consecutive quarter; deflected on the Q1 call (Notion) (row 30) |
| 10. ST LAP standalone disbursal; in-housing complete | PARTIALLY ANSWERED | Rs 210 Cr (Call L82-83, L807); in-housing not confirmed | Carry (row 46) |
| AR-1. PCR floor past 46% gold mix | PARTIALLY ANSWERED | As row 5 | Carry (row 34) |
| AR-2. Tier I / CRAR floor that triggers an equity raise | NOT ADDRESSED | Internal accruals stance only (Call L129) | Second consecutive call |
| AR-3. FY27 split and impact of a 15% gold-price fall | PARTIALLY ANSWERED | Guidance framed on flat or rising gold only (Call L756-759, L882-888); no downside case | First call since the AR (row 41) |

Count: 1 answered specifically, 8 partially answered, 4 not addressed, 0 evaded. Repeated across two concalls: rows 4, 8, 9 and AR-2. This is a governance signal (logged). Role 5 names three consecutive evasions of the same question as the downgrade trigger. These four rows sit at two.

Checkpoint: 3A-3E shown.

### R5 STEP 4 Q&A DECOMPOSITION

4A. Q&A inventory (26 analyst questions; ledger Q01-Q26; speaker attribution inferred unless noted). The table keeps 23 rows. The three questions embedded in mixed turns are folded into the row they extend: ledger Q24 (T47, Call L687-L690) into Q14; ledger Q25 (T50, Call L723-L726) and Q26 (T51, Call L743-L746) into Q15.

| # | Analyst Name & Firm | Question (1-line) | Question Category | Management Response Quality | Substance |
|---|---|---|---|---|---|
| Q01 (T07) | Shubranshu Mishra, Philip Capital | Gold growth against rising competition from NBFCs and banks; is an income-generating loan (IGL) product ready? | Strategic | B | Competition "heightened" in Q2; guidance held for Q3-Q4; gold yield down only 10 bps; LTV 68%; IGL live since April (Call L230-293) |
| Q02 (T10) | Shubranshu Mishra, Philip Capital | No spread compression despite competition and rate hikes? IGL LTV and ticket size? | Financial | C | Yield guide declined, "it is the ROA number that we are guiding on"; IGL capped at 85%, structured 75/78/80/85; ticket size not given (Call L299-325) |
| Q03 (T15) | Ranish, ICICI Securities | Are current gold Stage 2 / Stage 3 levels the new normal? | Customer/Order (asset quality) | B | April change; mortgage stages steady or declining; Stage 2 "technical"; credit cost way below 1%; GNPA below 2% (Call L339-381) |
| Q04 (T17) | Ranish, ICICI Securities | Has Stage 2 / GNPA peaked, with no further rise in Q3-Q4? | Forward Guidance | C | "I don't think like that"; "some numbers ... on the stage two side"; no number; one or two more quarters; CFO add-on on auction record [ASR] (Call L387-425) |
| Q05 (T20) | Ranish, ICICI Securities | ST LAP yield fall: ticket-size shift or rate cycle? | Financial | B | Ticket floor moved from Rs 5 lakh to Rs 8 lakh; yield dip from Q2 state mix; ST LAP credit cost stabilised; pickup in Q3 (Call L442-465) |
| Q06 (T24) | Digant Haria, Green Edge Wealth | What share of new gold loans is at full LTV, and what share is bullet with a discount? | Customer/Order | B | No new vs existing LTV difference; 90-95% take the maximum; LTV set by exposure slab caps of 75% and 80% (Call L482-L483, MFS-C3, MFS-C4); IGL is 20% of disbursal; bullet share not given (Call L477-487) |
| Q07 (T26) | Digant Haria, Green Edge Wealth | So Stage 2 rises industry-wide and is only technical? | Clarification | B | LTV played at plus or minus 2%; portfolio mix 72-74%; 71% where competition is low (Call L490-506) |
| Q08 (T28) | Digant Haria, Green Edge Wealth | Is competition unfair (valuation or LTV above the limit)? | Strategic | C | Old players play fair; "I can't talk about the others" (Call L523-532) |
| Q09 (T30) | Digant Haria, Green Edge Wealth | More operating leverage left, or more branches? | Operational | B | Branch split, two parses [ASR] (Call L539-541): about 75 in Q3 and 100 in Q4, or about 75 done in Q2, about 100 in Q3 and more in Q4; branches "not constrained by the cost to OPEX ratio"; ROA 3% target; cut non-branch opex (Call L538-569) |
| Q10 (T35) | Pawan Kumar, Edelweiss Public Alternatives | ST LAP yield 16.1% to 14.9%: rates or competition? H2 ST LAP disbursal numbers? | Forward Guidance | B | "I can't give you a definite guidance"; Q3 best of last 8-9 quarters; Q3 yield above Q2; disbursals higher (Call L588-616) |
| Q11 (T39) | Meghna Lutra, InCred Equities | Borrowing mix: fixed vs floating; repo vs MCLR? | Financial | A | 33% fixed; 24% MCLR of the 67% floating; residual EBLR; 58% of the book is short-tenor gold that reprices (Call L629-647) |
| Q12 (T41) | Meghna Lutra, InCred Equities | Will a CoF rise be passed on with no NIM compression? | Financial | B | "No."; no commitment to any line item; NIM compression offset by other levers (Call L652-662) |
| Q13 (T43) | Meghna Lutra, InCred Equities | How does tonnage play out in H2? | Forward Guidance | C | H1 tonnage "slightly ... positive"; Q3-Q4 are tonnage quarters; no number (Call L665-671) |
| Q14 (T46) | Devansh Dhruv, Equinities [ASR firm name] | Spread path on a 50 bp rate hike? Follow-up (ledger Q24, Call L687-L690, "a family object for our credit card" [ASR: read as opex or credit cost; the lever naming also rests on Call L567]): is the offset opex or credit cost? | Financial | C | "there will be a limitation to how much we can pass it on"; absorb the shock; superior ROA and ROE; offset "All of it ... a combination of all" (Call L691-L695), no size (Call L681-695) |
| Q15 (T50) | Yash, Dantee Equity | Branch scale-up time; ROE path; H2 AUM and ROA guide (ledger Q25, Call L723-L726); upgrade? (ledger Q26, Call L743-L746) | Forward Guidance | B | Breakeven Rs 6-7 Cr AUM in 12-13 months, tied to a rising or current gold price (Call L715-L716); guidance "not revised"; ROA +30-40 bps; AUM 20-25%; ROA 3%; ROE number inaudible [ASR]; no upgrade (Call L714-759) |
| Q16 (T54) | Rahul Kumar, Vakaria Fund | ST LAP competitive intensity vs last year in the six major states? | Strategic | B | Same players with aggressive appetite; yield pressure; SFBs and HFCs present; 16-17% vs 20-22% yield segments (Call L772-795) |
| Q17 (T56) | Rahul Kumar, Vakaria Fund | ST LAP approval-rate trend? | Operational | A | About 30% to the early or mid-40s (Call L799-800) |
| Q18 (T58) | Rahul Kumar, Vakaria Fund | Despite the competition? | Clarification | B | Tightened BRE engine; Rs 210 Cr disbursed; approval rate to hold as volume rises (Call L802-810) |
| Q19 (T60) | Rahul Kumar, Vakaria Fund | Outlook for medium-ticket LAP? | Customer/Order | B | Profitable; yield 11.5-12.5%; 15-16 geographies; partner-driven; steady delinquency; trajectory [ASR garbled at L826] (Call L815-826) |
| Q20 (T63) | Aditya, Securities Investment Management | Entity ROA when the mortgage share rises? | Strategic | C | "Cycle A / cycle B" narrative; ST LAP ROA to approach gold ROA; entity ROA "in a similar range"; no numbers (Call L844-869) |
| Q21 (T65) | Aditya, Securities Investment Management | Can gold ROA hold as competition rises? | Strategic | B | Tonnage 10-12% a year; 20-25% AUM on flat gold; AUM per gold branch Rs 8 Cr to Rs 16 Cr; gold ROA held, not expanded (Call L881-900) |
| Q22 (T67) | Aditya, Securities Investment Management | FY26 insurance income contribution? | Financial | B | About 0.1% of the ROA tree, "a little over 0.1" on income; substitute "whenever" the change comes (Call L901-907) |
| Q23 (T69) | Aditya, Securities Investment Management | Do new gold branches also sell ST LAP? | Operational | B | Market by market, not compulsory; gold branch footprint extends ST LAP (Call L910-920) |

Grade count: A 2 (Q11, Q17), B 15, C 6 (Q02, Q04, Q08, Q13, Q14, Q20), D 0, E 0. The refusals sit inside C-graded answers (gold yield, Q02; Stage 2, Q04) and the B-graded Q10 (ST LAP numbers declined, but a dated Q3 bar given).

4B. Question pattern analysis
- Most repeated: spread / rate pass-through (Shubranshu Q02, Meghna Q12, Devansh Q14: three analysts). Branch economics (Digant Q09, Yash Q15, Aditya Q23: three). Gold Stage 2 / Stage 3 (Ranish Q03-Q04, Digant Q06-Q07: two). The market did not accept the first spread answer.
- Topics graded C: spread and yield (Q02, Q14), Stage 2 path (Q04), tonnage (Q13), competition fairness (Q08) and entity ROA under a higher mortgage mix (Q20). For a lender the evasion rule binds on asset quality. On the Q1 call the GS3 bridge was deflected (Notion). On this call the Stage 2 number was declined and DPD buckets and the bridge stayed absent. That is absence or evasion on asset quality across two concalls: a **negative diagnostic for FTTCP lender Transition 3** (flag FTTCP-T3-NEGATIVE-DIAGNOSTIC, for /fttcp).
- Buy-side vs sell-side: five buy-side-type firms (Green Edge Wealth, Edelweiss Public Alternatives, Dantee Equity, Vakaria Fund, Securities Investment Management) and four sell-side (Philip Capital, ICICI Securities, InCred Equities, Equinities) [INFERENCE from ASR firm names]. Buy-side present. One buy-side questioner spoke as a holder ("players like us", "our stock", Call L517-L518, L571-L572), and management thanked him "for your support" (Call L573). Six of nine questioners opened with congratulations. This does not show pre-screening. It weakens the buy-side-independence reading.
- Hosting broker: Aquarius Securities asked nothing. The first question (Philip Capital) was substantive. No direct evidence of an orchestrated call; the holder-analyst qualifier above stands.
- Pushback: Ranish pressed for a peak (Q04); the CEO refused. Yash pressed for an upgrade (Q15, Call L743-746); the CEO declined. Meghna asked whether a CoF rise would be passed on easily; the CFO said "No." (Call L652). Contested topics: Stage 2 path, guidance level, spread.
- Obvious questions not asked: the Stage 1 ECL build and the Stage 2 coverage fall (16.53% to 12.61%), the Rs 208 Cr sell-down route, the EPS misprint, Federal Bank co-lending, write-offs, the PCR floor, the joint auditor. The filing's main asset-quality flag drew no question. Pre-screening is not evidenced, but the gap is noted.

4C. The three most important exchanges

Exchange 1 (Q04, T17-T19): has Stage 2 peaked?
- Question (Call L382-386): "since this new regulation being implemented from April and now you know we are in September. So, it is fair to assume that you know the Q2 numbers you know fairly captures the change of customer behavior and if that is the case then you know the stage 2 and Gauss NPA ideally you know has picked out at current level and maybe in Q3 Q4 there will not be further deterioration."
- Response (Call L387-396, L414-415, L420-424): "I don't think like that Renish, it won't be a debtor reation ... So there will be some numbers which will happen on the stage two side. ... I don't want to hold a number on the stage two side because it will constrain the business, but it is not a number which one should worry about. ... it may take one or two more quarters before customer behavior has changed." CFO add-on [ASR]: "We have had an auction loss on either principal or interest in the last six years ... we will not have any loss in terms of principle or interest."
- Said specifically: Stage 2 will rise further; the transition runs one or two more quarters; the six-year auction record stands [ASR].
- Not said: a Stage 2 number or peak; gold vs mortgage Stage 2; roll rates; auction volume; why Stage 2 coverage fell from 16.53% to 12.61%.
- Thesis implication: the PCR tripwire and the Pillar 2L clause face at least one more quarter of gold Stage 2/3 build at gold PCR 10.5% (Deck R736). The reading A vs B fork stays open.
- Follow-up we would ask: rows 32 and 33.

Exchange 2 (Q15, T50-T51): guidance level
- Question (Call L723-726): "since your ROE is already at 17%, what is the kind of trajectory that we'd be seeing and also on the AUM growth, I think you've guided for around 25% if I'm not mistaken, could you also give the guidance for H2".
- Response (Call L727-736): "I have not revised the AUM guidance or the ROA, ROA guidance ... last year we had an ROA of about 2.4, we said we will improve that ROA by 30 to 40 basis points and that time itself I had said that our AUM growth will be about 20 to 25 percent. ... So we will give a UAM growth of about 20 to 25% for the year. ... there might be an upside to the guidance ... Our target ROA we are trying to reach is three and correspondingly try and touch an AT in ROE."
- Said specifically: AUM 20-25% on flat gold; ROA +30-40 bps; ROA 3% target; possible upside.
- Not said: the gold AUM +25-30% guide; any H2 split; the ROE number [ASR]; any downside case.
- Thesis implication: the bands differ from the Q1 log while being called unchanged (GUIDANCE-RECORD-MISMATCH). The 20% floor at a flat gold price needs non-gold AUM to grow +10.2% to +12.5% in H2 against +3.2% in H1 (Step 2L, derived).
- Follow-up we would ask: rows 35 and 36.

Exchange 3 (Q12 and Q14, T41-T42, T46-T47): spread under rising rates
- Question (Call L648-651): "is it fair to assume that any sort of compression in, say, on the cost of funds will be easily passed off? And we should not see any invested compression in coming forward?"
- Response (Call L652-662; L681-686): "No. ... we would not want to be bound down by any particular line item in the ROA tree. If there is a nim compression, we will handle it by, you know, enhancing some other operating labor." And: "obviously there will be a limitation to how much we can pass it on ... we will absorb that shock, but still deliver a superior ROA and ROE to you."
- Said specifically: pass-through is limited; NIM may compress; 33% of borrowings fixed and 24% MCLR-linked (Call L630-632).
- Not said: the size of compression; the gold yield plan for Q3; the repricing gap; the size of either lever. Levers named only in general: opex and credit cost (Call L567, L689-L695), with no size. Both are partly used: at least 150 H2 branches add opex (Call L187-L189), and credit cost is already 0.6%.
- Thesis implication: the FTTCP NIM/spread leg (STAGNANT) is at risk of turning negative in H2. The +20 bp reported spread rise is the DA-drag reversal: the CFO calls the yield rise optical (Call L138-L141), and net DA / ATA moved from -0.3% to 0.0% (Deck R1023-R1024). Ex-DA, yield was flat while CoB rose 13-20 bps on two of three measures, so the ex-DA spread narrowed about 13-20 bps. Core NII / ATA held at 8.8% (Deck R1019-R1020). On the yield-less-CoB measure the pressure is already in Q2; core NII / ATA does not show it yet.
- Follow-up we would ask: row 37.

Checkpoint: 4A, 4B, 4C shown.

### R5 STEP 5 NEW INFORMATION AUDIT

5A. New disclosures

| Disclosure | Type | Material? | Thesis Impact |
|---|---|---|---|
| IGL product live since April 2026; 20% of gold disbursal; LTV structured at 75/78/80/85%, cap 85%, cash-flow assessed (Call L268-271, L316-325, L484-487) | New product / launch | YES | Incremental LTV runs above the book's 68%; thinner collateral cushion (FN-09) |
| Entry into eastern India in Q2 (Call L69-70) | New geography | NO | Size not given |
| Borrowings 33% fixed, 24% MCLR-linked, residual EBLR-linked (about 43%, derived) (Call L630-633) | New disclosure (funding) | YES | The EBLR share transmits a repo rise fast (FN-06) |
| About 58% of the loan book is short-tenor gold that reprices at maturity (Call L636-639) | New disclosure (funding) | YES | Offsets part of the CoF risk, if pricing holds against competition |
| Insurance income about 0.1% of the ROA tree in FY26; an insurance-distribution change expected (Call L197-199, L901-907) | Negative surprise | YES | About 10 bps of ROA at risk; substitute line unnamed (FN-13) |
| DA of about Rs 700 Cr of the gold book plus co-lending in gold cut D/E 4.9 to 4.6 (Call L148-150) | New detail | YES | De-leveraging came from asset sales, not capital (FN-08) |
| No auction loss on principal or interest in six years [ASR] (Call L420-424) | Standing claim | YES, if confirmed | Supports the low-LGD reading A; unverified |
| ST LAP: Rs 8 lakh minimum ticket (from Rs 5 lakh); approval rate 30% to early/mid-40s; Q3 best quarter of the last 8-9 (Call L443-446, L799-800, L588-591) | Forward catalyst pre-announced | YES | Testable at Q3; FY28 vintage risk in an aggressive market (FN-10) |
| Branch breakeven at Rs 6-7 Cr AUM in 12-13 months; about 150 FY26 branches on that path (Call L714-722) | Operational | YES | Supports the H2 branch economics only at a rising or current gold price. The CEO ties the 12-13 months to it (Call L715-L716, MFS-C21). The FY26 cohort he cites grew while gold value per gram rose about 38% YoY (Step 6D). The timeline is untested at a flat price, which is the guidance's own assumption. Below the Rs 10 Cr bull bar of row 10. |
| AUM per gold branch Rs 8 Cr to Rs 16 Cr (base date ND) (Call L894-896) | Operational | NO | Directional; Q2 Rs 16.9 Cr (Deck R486) |
| MT LAP yield 11.5-12.5%, 15-16 geographies, partner-driven (Call L815-819) | New detail | NO | Context |
| Gold yield fell only 10 bps Q1 to Q2 (Call L256-257) | New detail | YES | Gold yield defended, if true; not in the filing |
| Credit-cost fall from mortgage collection efficiency; record low mortgage net slippages (Call L127-128, L135-136, L164-166) | New attribution | YES | Supports reading A; unquantified |
| ROA 3% "sooner than we had promised" (Call L564, L735-736, L947-948) | Forward catalyst pre-announced | YES | Bar raised into a NIM-pressure half (FN-05) |
| At least 150 branches in H2 FY27 (Call L187-189) | New capacity plan | YES | Opex load in H2; C/I only "hopeful" (FN-12) |
| The gold change is dated April 2026: periodic interest replaces bullet (Call L154-159, L341-342) | New regulatory detail | YES | Names the Stage 2/3 cause; the end date is hedged |

5B. What was NOT discussed

| Expected Topic | Why It Should Have Been Discussed | Significance of Silence |
|---|---|---|
| PCR floor; gold vs mortgage PCR (S01) | Most-at-risk tripwire fell 299 bps; prior Q5 and AR-1 | RED: second quarter, deteriorating metric (FN-16, CONFIRMATORY-NEGATIVE) |
| Gold 1+/30+/60+ DPD (S04) | Prior Q4; Stage 2 rising | RED: second quarter (FN-19, CONFIRMATORY-NEGATIVE) |
| GS3 provision bridge; write-offs (S05) | Prior Q9; A3-02 | RED: second quarter (FN-19) |
| Stage 1 ECL build; Stage 2 coverage 16.53% to 12.61%; stressed coverage 24.5% to 20.2% | Role 4 Step 4 memo, the coverage fork | RED: the filing's main asset-quality flag, neither asked nor addressed |
| Gold-price fall scenario (S09) | AR-3; LTV 68% book, 72-74% working mix | AMBER to RED (FN-18) |
| Gold AUM +25-30% guide (S10) | Q1 promise log | AMBER: DROPPED candidate |
| CRAR / Tier I equity floor; co-lending partner count (S06) | Prior Q6 and AR-2 | AMBER: second quarter (FN-20) |
| DA-unwinding schedule; DA-neutral date (S07) | Prior Q7 | AMBER: second quarter, partial (FN-21) |
| FVOCI loss and ECL re-recognition (S08) | Prior Q8 | AMBER: second quarter |
| Absolute tonnage; tonnage / LTV / price split (S03) | Checklist 8; prior Q2 | AMBER: the deck has 12.9 t; the call spoke only % |
| ST LAP collections in-housing (S02) | Checklist 7; prior Q10 | AMBER: second quarter (FN-17) |
| Rs 208 Cr of sell-down not filed as DA; Federal Bank share | SELLDOWN-DA-GAP | AMBER: co-lending named, unsized |
| Parent-funded co-lending scale-up | Notion growth trigger | AMBER: thesis catalyst silent; Federal Bank not mentioned once |
| Federal Bank RPTs: brand fee, term loan Rs 1,066 Cr to Rs 905 Cr, margin deposit | A3-13, A3-16 | AMBER |
| EPS misprint 3.56 vs 3.49 | A3-10 | AMBER: reporting control |
| FCY/ECB and the Rs 43.48 Cr hedge OCI gain | A3-08 | AMBER: rates were discussed, FX was not |
| Other financial liabilities +116% in H1 | A3-12 | AMBER |
| Joint statutory auditor, first joint review | A3-03 | Routine |
| ETR 26.54% | A3-05 | Routine |
| ESOP amendment with 25.54% institutional votes against | Notion AGM record | Routine |
| Named peer numbers | Management invoked peers three times (Call L255-L258, L378-380, L416-418) and named none | AMBER: claim untestable on the call |

Checkpoint: 5A and 5B shown.

### R5 STEP 6 TONE AND SPECIFICITY

6A. Tone comparison (prior phrase from the Notion Q1 FY27 log; Q1 transcript not in the run)

| Topic | Prior Concall Adjective / Phrase | This Concall Adjective / Phrase | Direction |
|---|---|---|---|
| PCR | "optically reducing going forward" | "decrease in PCR ... is due to a higher proportion of gold loans in stage three" (Call L167-168) | MAINTAINED |
| De-leverage | "we hope" | "direct assignments of approximately 700 crores ... to de-leverage"; D/E 4.9 to 4.6 (Call L148-150) | UPGRADED (delivered via asset sales) |
| DA income | "DA income negative going forward" | No DA income outlook; "consciously reduce our reliance on direct assignment" (Call L56) | DROPPED (outlook); contradicted by the record sell-down |
| ROA | "+20-30 bps" | "30 to 40 basis points"; "a ROA of three ... sooner than we had promised" (Call L729, L947-948) | UPGRADED |
| Entity AUM | "+20-22%" | "about 20 to 25%" (Call L733) | UPGRADED at the top end; management says unchanged |
| Gold AUM | "+25-30%" | not restated in number; "we will continue with our guidance in Q3 and Q4 as well" in the gold-growth answer (Call L248-L249) | DROPPED in number (candidate); reaffirmed only generically |
| Gold tonnage | "+10-12%", H2-weighted | "10-12% every year. We will continue that" (Call L885-886) | MAINTAINED |
| Branches | "200 in FY27" | "at least another 150 branches in the second half" (Call L188-189) | UPGRADED |
| Credit cost | "sub-1%" | "way below 1%" (Call L370) | UPGRADED (tone) |
| Gold Stage 2 / transition | Stage 1/2 "will be different for the year" (recalled, Call L343-347) | "it may take one or two more quarters" (Call L414-415) | MAINTAINED (Q1 window ND) |
| Gold competition | ND | "Q2, the intensity was a heightened one"; "Q3 will be an intense market" (Call L238, L307-308) | ND (no prior phrase; new negative language) |
| Gold yield / spread | ND | "It will be wrong of me to give you a guidance that we will play with a flattish yield" (Call L308-309) | ND (no prior phrase; new negative language) |
| Cost-to-income | ND (Q1 trend: falling, 52.8%) | "hopeful of containing any material increases" (Call L191-192) | DOWNGRADED vs the Q1 falling trend (prior phrase ND) |

6B. Specificity score (concall FORWARD rows: A1 rows Call R185-R233 plus ledger MFS-C11 to C19)
- Quantified forward statements (number, date or binary milestone): 17 or 18. The 16 A1 rows R186, R189, R200, R201, R202, R203, R207, R209, R211, R212, R213, R216, R218, R219, R224, R231, plus MFS-C12 (Call L57, "below 1%"). MFS-C15 (Call L567) counts only by its reference to the 3% ROA target.
- Unquantified forward statements: 40 or 41 (33 A1 rows plus MFS-C11, C13, C14, C16, C17, C18, C19, and C15 if it is not counted). MFS-C16 (Call L615) names Q3 but no measure.
- Specificity ratio: 17-18 / 58 = **0.29-0.31**. On the 0.3 line between hedge-heavy and moderate. Several quantified rows repeat one item (credit cost three times, ROA 3% three times, AUM 20-25% twice).

6C. Defensive language count
- Lexicon instances (7): "I don't want to specifically give you a guidance" / "It will be wrong of me to give you a guidance" (Call L306-309); "I don't want to hold a number on the stage two side" (Call L394); "I can't talk about the others" (Call L528-529); "I can't give you a definite guidance" (Call L589); "We will evaluate them" (Call L646-647); "allow us to play with our levers without holding on to any ... would not want to be bound down by any particular line item" (Call L656-660); "we are hopeful of containing" (Call L191).
- "we believe": 8 (Call L100, L244, L251, L261, L543, L634, L855, L892). "we expect": 1 (Call L68). Conditional framing "whenever that happens" (Call L906) noted, not counted.
- Total 16 markers, above 5: a **hedge-heavy call** on the protocol benchmark. Prior count ND (Q1 transcript not in the run).

6D. Confidence indicators
- Specific dates: Q3 FY27 ST LAP best quarter of the last 8-9 and yield above Q2 (Call L588-613); H2 at least 150 branches (Call L188).
- Numerical commitments: ROA +30-40 bps; AUM 20-25%; credit cost way below 1%; GNPA below 2%; tonnage 10-12%.
- Acknowledged misses with recovery timelines: partial. "Q1, Q2 is usually a tough quarter for us in tonnage" (Call L669) with H2 recovery; ST LAP "the pickup has not been that great but it will definitely pick up in Q3" (Call L460). No acknowledgment of the branch or entity-AUM lag.
- Named customer wins: not applicable to this lender.
- Promoter on the call: no. The MD & CEO answered operational questions directly.

6E. Management archetype (specificity x credibility)
- Specificity 0.29-0.31 (at or below 0.5): bottom row.
- Credibility ratio: ND (Step 3B).
- Archetype: **ND**. The bottom row resolves to MEASURED & CREDIBLE if the Q4 FY27 scoring is 60% or above, and EVASIVE if below. No provisional label: the protocol bars a session judgment in place of the ratio. Track the archetype from the Q4 FY27 review.

Checkpoint: 6A-6E shown.

### R5 STEP 7 CROSS-REFERENCE vs FILING AND PEER CONCALLS

7A. Concall narrative vs filing numbers (Role 4 rows cited)

| Concall Claim | Filing Evidence | Reconciliation |
|---|---|---|
| PAT Rs 130.8 Cr, +63% YoY, +14.3% QoQ (Call L89-90, L137-138) | Rs 130.75 Cr (Res R103); +63.1% YoY, +14.31% QoQ (Role 4 Step 2, Step 4) | CONFIRMED |
| ROA 2.8%, +24 bps QoQ; ROE 17%, +153 bps (Call L116-120) | 2.84% and 16.96% derived; Q1 2.61% and 15.43% (Role 4 Step 1L; Deck R862-R863, R868-R869) | CONFIRMED |
| AUM Rs 22,035 Cr, +37% YoY; +9% in H1 (Call L61, L124-126) | Rs 22,035 Cr (Deck R428); +36.6% (Deck R049); +9.3% H1 (Role 4 Step 1L-c) | CONFIRMED |
| Disbursements Rs 6,676 Cr, +28%; gold Rs 5,822, +31%; MT LAP Rs 645 Cr, +16%; ST LAP Rs 210 Cr; mortgage Rs 855 Cr, +12% (Call L60-83) | Deck R391, R052 (+28.3%); slide 22 quarterly gold 5,822 vs 4,445 (+31.0%), MT LAP 645 vs 554 (+16.4%), ST LAP 210 vs 206, mortgage 855 vs 760 (+12.5%) (XC s-22, derived) | CONFIRMED |
| Gold AUM Rs 11,917 Cr, +77%; tonnage +16% YoY (Call L63-66) | Deck R443; +77.0% and tonnage +16.2% (Role 4 Step 6D; Deck R481) | CONFIRMED |
| 68% LTV (Call L66, L259) | Portfolio LTV 68.0% (Deck R501) | CONFIRMED. The working mix of 72-74% (Call L500-501) agrees with origination LTV 72.1% (Deck R327). |
| "total gold branch count to 831" (Call L67-68) | Gold branches 706 (Deck R496); total 831 (Deck R034) | CONTRADICTED (misspoken; trust the filing) |
| AUM per branch Rs 16.9 Cr (Call L65) | Rs 16.9 Cr (Deck R486) | CONFIRMED |
| Credit cost Rs 27.1 Cr, 0.6%, -18 bps from 0.78%, -20.5% QoQ (Call L87-88, L127, L135) | Rs 27.08 Cr (Res R043); Rs 34.06 Cr Q1 (Res R044); 0.59% vs 0.78% derived; -19 bps (Deck R087) | CONFIRMED (the number) |
| Credit-cost fall from mortgage collection efficiency and improved mortgage flows (Call L127-128, L136) | Collection efficiency ND in all filings; mortgage GS3 flat at 3.4% (Deck R711-R712); stressed coverage 24.5% to 20.2%, Stage 1 took 55% of the ECL build (Role 4 Step 4 memo) | UNVERIFIABLE (cause). The filing's coverage thinning is not addressed. |
| GNPA 1.8% from 1.6%; NNPA 1.2% (Call L91-94) | 1.82% / 1.55% / 1.18% (Res R428, R429, R432) | CONFIRMED |
| GNPA and NNPA improved YoY (Call L94-95) | 1.90% to 1.82%; 1.30% to 1.18% (Res R431, R435) | CONFIRMED |
| "improving asset quality" (Call L97) | QoQ: GNPA +27 bps, NNPA +22 bps, Stage 2 +34.6%, PCR -299 bps (Role 4 Step 5L) | CONTRADICTED on QoQ; true only YoY |
| PCR 35.4% (Call L94) and 38.4% to 35.5% (Call L167) | 35.37% and 38.36% (Res R440, R441) | CONFIRMED at 35.4%; 35.5% misspoken by 13 bps |
| PCR fall from more gold in Stage 3 (Call L167-170) | Gold GS3 0.1% to 0.5%, PCR 10.5% (Deck R736, R738-R739); Stage 3 marginal cover 18.0% on +Rs 44 Cr (Role 4 Step 4 memo). Segment check (derived): mortgage Rs 234.4 Cr x 37.5% = Rs 87.9 Cr, gold Rs 47.6 Cr x 10.5% = Rs 5.0 Cr; residual GS3 Rs 14.0 Cr carries Rs 11.8 Cr of ECL, 84% cover, near the business-loan PCR of 95.9% (Deck R746). | CONFIRMED (mechanism). The residual segment largely explains A3 FN-03's 33.0% vs 35.4% blend gap [INFERENCE: residual assumed to be business loans]. |
| "Our mortgage PCR continues at similar levels" (Call L171) | Q2 mortgage PCR 37.5% (Deck R726); Q1 mortgage PCR ND (Role 4 Step 5L) | UNVERIFIABLE (no Q1 base) |
| Stage 2 2.7% to 3.6%, Stage 3 1.6% to 1.8%, "entirely" gold (Call L160-161) | Levels: Deck R705-R706, R708-R709; Stage 2 Rs 436 Cr to Rs 587 Cr (Deck R768-R769). Gold supplies about Rs 38.6 Cr of the Rs 44 Cr GS3 rise (Role 4 Step 5L). Gold Stage 2 not disclosed. | CONFIRMED (levels); PARTIALLY CONFIRMED for Stage 3 (about 88% gold); UNVERIFIABLE for Stage 2 |
| Mortgage stages "steady or in fact declining" (Call L348-349) | Mortgage GS3 3.2% / 3.4% / 3.4% for Q2 FY26 / Q1 / Q2 FY27 (Deck R710-R712); mortgage Stage 2 ND | PARTIALLY CONFIRMED (GS3 flat, not declining) |
| Core NII Rs 404.8 Cr, +5.2% QoQ, +40.9% YoY (Call L132-133) | PR R019, R018; +40.9% (Role 4 Step 2) | CONFIRMED |
| "profit" Rs 205.1 Cr, +9.4% QoQ, YoY "40. 7.5%" [ASR] (Call L133-135) | PPOP Rs 205.08 Cr (PR R067); +9.35% QoQ vs Rs 187.54 Cr; +47.6% YoY (Role 4 Step 2) | CONFIRMED (label inferred as PPOP; the YoY reads as 47.5% [ASR]) |
| Core yield constant at 16.40; 29 bp "optical increase" from Q1 DA unwinding (Call L138-141) | Slide 25 yield 16.4% to 16.7% (XC; only the XC order passes yield = CoB + spread: Q1 7.7 + 8.6 = 16.3, Q2 7.9 + 8.8 = 16.7); net DA / ATA -0.3% to 0.0% (Deck R1023-R1024); net DA -Rs 12.9 Cr to -Rs 1.2 Cr (PR R026-R027) | PARTIALLY CONFIRMED: the +29 bp optical rise and its DA cause tie under XC; the 16.40 level does not. Core ex-DA derives to about 16.7% in both quarters; 16.4% is the Q1 reported yield [ASR or definition]. A3 FN-07's "opposite sign" used A1's swapped slide 25 labels and dissolves. |
| Weighted average CoB flat at 7.80 for four quarters (Call L141-144) | Daily I-GAAP 7.87% / 7.83% / 7.80% / 7.79% (Deck R607-R610); slide 25 CoB 7.7% to 7.9% (XC); P&L-implied 7.74% to 7.87% (FN25) | PARTIALLY CONFIRMED (true on the basis cited; the other two bases rose 13-20 bps) |
| 33% fixed, 24% MCLR (Call L144-146, L630-632) | Not in the filings | UNVERIFIABLE |
| DA of about Rs 700 Cr of the gold book to de-leverage (Call L148) | Filed assignment Rs 876.89 Cr, weighted residual 23 months (Res R472-R473); deck sell-down Rs 1,085 Cr (Deck R680); gold off-book stock Rs 1,718 Cr to Rs 2,496 Cr (+Rs 778 Cr) of a total +Rs 872 Cr (derived, Role 4 Step 5L off-book table) | PARTIALLY CONFIRMED (understated by Rs 177 Cr vs filed DA). Two readings: Rs 700 Cr is the gold part of a mixed Rs 876.89 Cr pool (fits the 23-month residual), or a misstatement. Separating observation: the product split of Note 10(II) (row 40). |
| D/E 4.9 to 4.6; CRAR 21% from 20.7% (Call L149-151) | 4.89x to 4.61x (Res R389, R388); 20.71% to 20.96% (Res R425, R424); Mar-26 D/E also 4.61x (Res R390) | CONFIRMED. The call omits that H1 net de-leverage is nil. |
| "consciously reduce our reliance on direct assignment" (Call L56; ledger MFS-C11) | Sell-down Rs 530 Cr to Rs 1,085 Cr, highest in the series (Deck R679-R680); off-book 23.2% to 26.2% (Deck R660-R661) | CONTRADICTED |
| Growth funded "through internal approvals" [ASR: accruals] (Call L129) | Net worth +16.8% YoY vs borrowings +42.7% (Deck R058, R068); leverage 5.9x to 6.0x (Deck R1063-R1064); de-leveraging came from sell-downs | PARTIALLY CONTRADICTED |
| Opex / ATA 4.9% vs 4.8%; FY26 5.5% (Call L173-178) | Deck R1039, R1040, R1041 | CONFIRMED |
| C/I 52.5% vs 52.8%; FY26 57.2% (Call L181-184) | 52.47% / 52.83% / 57.23% derived (Role 4 Step 1L, Step 6B) | CONFIRMED |
| 74 branches added (Call L67, L187) | Deck R033 | CONFIRMED |
| Mortgage AUM Rs 9,982 Cr, +13.5% (Call L77-78) | +13.5% YoY (Deck R031) | CONFIRMED |
| Unsecured below 1% of on-book (Call L85-86) | Secured 99.4% (Deck R064) | CONFIRMED |
| BVPS 84.4 (Call L96) | Rs 84.4 (Deck R060); Rs 3,164.96 Cr / 37.514 Cr shares = Rs 84.37 (Res R420, R169) | CONFIRMED |
| "lack of momentum and gold prices"; guidance "in spite of the gold prices being almost flat" (Call L106, L732-733) | Q2 gold AUM per tonne about +4.7% QoQ (range 3.8-5.5%) with LTV flat at 67.9% to 68.0% (Role 4 Step 6D, derived) | PARTIALLY CONTRADICTED [INFERENCE]: the filed collateral value per gram rose about 4.7% in the quarter. A3 FN-09's loan-to-gram reading does not fit the flat Q2 book LTV. |
| ST LAP credit cost normalised; "bucket negatives" (Call L455-458) | Segment credit cost not in the filings | UNVERIFIABLE |
| Record low mortgage net slippages (Call L164-166) | Slippages not disclosed | UNVERIFIABLE |
| Gold yield down only 10 bps QoQ (Call L256-257) | Product yields not in the filings | UNVERIFIABLE |
| ROA 2.1% to 2.8% and ROE 10.9% to 17% over nine quarters (Call L117-122) | Nine-quarter series not in the run | UNVERIFIABLE |

Reconciliation count: 22 CONFIRMED, 4 PARTIALLY CONFIRMED, 2 PARTIALLY CONTRADICTED, 3 CONTRADICTED, 7 UNVERIFIABLE (38 claims; a row with two verdicts is counted by its first). The filing wins every conflict. The three contradictions (gold branch count, "improving asset quality", DA reliance) are logged as credibility data points, not as numbers to use.

7B. Peer concall cross-check

| Topic | This Company Said | Peer 1 Said | Peer 2 Said | Most Credible Narrative |
|---|---|---|---|---|
| Gold competitive intensity | Q2 "heightened"; Q3 "intense" (Call L238, L307-308) | UNVERIFIABLE this run (no peer concall passed) | UNVERIFIABLE this run | UNVERIFIABLE |
| Gold Stage 2 rise after the April change is industry-wide | "as you see more gold companies coming up, you will see similar kind of numbers" (Call L378-380) | UNVERIFIABLE this run | UNVERIFIABLE this run | UNVERIFIABLE; testable against the listed gold lenders' Q2 FY27 calls |
| Rate pass-through on gold | Limited (Call L681-683) | UNVERIFIABLE this run | UNVERIFIABLE this run | UNVERIFIABLE |
| ST LAP competition | Same players, aggressive appetite; SFBs and HFCs present (Call L772-786) | UNVERIFIABLE this run | UNVERIFIABLE this run | UNVERIFIABLE |
Flag PEER-CROSSCHECK-UNVERIFIABLE (the Notion flag PEER-CROSSCHECK-MISSING stands).

7C. Concall vs external channel checks

| Concall Claim | External Source | External Says | Alignment |
|---|---|---|---|
| An April 2026 gold-lending change moved loans from bullet to periodic interest (Call L154-159, L341-342) | Regulator text not in the run | PENDING LIVE VERIFICATION | UNVERIFIABLE this run |
| Funding insulated by the rating and mix (Call L144-147) | Rating AA+/Stable, four agencies, as reported in the deck (Deck R620-R622) | Deck-reported only | UNVERIFIABLE externally this run |

Checkpoint: 7A, 7B, 7C shown.

### R5 STEP 8 UPDATE THESIS AND POSITION DECISION

8A. Growth trigger status (Role 4 Step 6D status = pre-concall)

| Trigger | Status Pre-Concall | Concall Evidence | Status Post-Concall |
|---|---|---|---|
| Gold AUM +25-30% FY27 (price flat) | AT RISK | Not restated in number; generic "our guidance" (Call L248-L249); "20-25% growth on the AVM" in a gold context (Call L888) | WEAKENED |
| Gold tonnage +10-12% FY27 (H2-weighted) | DELAYED | Reaffirmed; "different trajectory in H2" (Call L670, L885-886); last year's H2 +13.5% (11.1 t to 12.6 t, Deck R487, R489) | DELAYED (Q3 test: 13.4 t) |
| Entity AUM +20-22% | DELAYED | Restated as 20-25% on flat gold (Call L733); needs +9.8% to +14.3% in H2; non-gold must triple its H1 pace (Step 2L) | DELAYED |
| Mortgage 15-20% | WEAKENED | Mortgage AUM +13.5% (Call L77); MT LAP "steady" (Call L815-826); ST LAP push in Q3-Q4 (Call L464-465) | WEAKENED |
| LAP 15-20% | ND | ST LAP "pedal pressed" in Q3-Q4; no segment AUM | ND |
| ROA +20-30 bps over FY26 2.4% | ON TRACK | Restated +30-40 bps; ROA 3% "sooner" (Call L729, L947-948) | ON TRACK |
| 200 new branches FY27 | DELAYED | At least 150 in H2 planned (Call L187-189) | DELAYED (plan restated to 224; delivery test 2027-03-31) |
| Parent-funded co-lending scale-up | WEAKENED | Co-lending in gold named (Call L93, L149 [ASR]); no partner, no size; Federal Bank never mentioned | WEAKENED |
| De-leverage as CLM normalises | DELAYED | D/E 4.9 to 4.6 via DA and co-lending (Call L148-150), back to the Mar-26 level | DELAYED |
| Credit-cost normalisation (shared FTTCP catalyst) | ON TRACK | "way below 1%" (Call L370); cause attributed to mortgage flows; coverage fork not addressed | ON TRACK on number, quality unresolved |
| ROA 3% target | n/a | "we are targeting a ROA of three and we should see it sooner than we had promised" (Call L946-948) | NEW (undated) |
| ST LAP Q3 FY27 pickup | n/a | Best quarter of the last 8-9; yield above Q2 (Call L588-613) | NEW (dated Q3 FY27) |

8B. Watchlist items: concall readings

| # | Watchlist Item | This Concall Reading | Status |
|---|---|---|---|
| 1 | Credit cost <= 1.1% of avg assets, FY27 guidance issued | 0.6% (Call L87-88); guidance "way below 1%" issued (Call L370) | GREEN on the item definition; coverage caveat (FN09) carried in flags |
| 2 | PCR >= 38% and rising toward 50%+ | 35.4% and falling; mechanism given; no floor (Call L94, L167-171) | AMBER (fails green, above red) |
| 3 | Gold branch count 140-150, AUM per branch > Rs 13.3 Cr | AUM per branch Rs 16.9 Cr (Call L65); gold branch count misspoken as 831 (Call L67-68; filed 706, Deck R496) | GREEN on per-branch; count definition flag |
| 4 | Cost-to-income below ~57% and falling into FY27 | 52.5% (Call L181); H2 only "hopeful of containing" (Call L191) | GREEN on level; AMBER on trend (FN-12) |
| 5 | ROE toward 14-15%, ROA >= 2.5% | 17% / 2.8% (Call L90, L116-120) | GREEN |
| 6 | GNPA at or below ~1.9-2.1% | 1.8%; guide below 2% (Call L91, L373) | GREEN (rising; 20 bps to the guide) |
| 7 | ST LAP in-housing complete; disbursals > Rs 208 Cr | Rs 210 Cr (Call L82-83, L807); in-housing silent (FN-17) | AMBER |
| 8 | Gold tonnage disclosed and rising | +16% YoY spoken (Call L66); absolute tonnes not spoken (deck 12.9 t, Deck R491) | GREEN on disclosure (deck) |

8C. Thesis-broken trigger check (concall)

| Thesis-Broken Condition | Threshold | Concall-Relevant Evidence | FIRED? |
|---|---|---|---|
| Credit cost > 1.1% of average assets | 1.1% | 0.6% Q2; guide "way below 1%" (Call L370). Not moved closer on the call; the coverage fork (about 1.0% at Q1 coverage [INFERENCE]) is unaddressed. | NO |
| ROE fails to cross 14% by FY28 | 14% | 17%; ROA 3% target (Call L947-948); NIM compression signalled (Call L661) | NO |
| PCR thins below 32% | 32% | 35.4% (Call L94); Stage 2 to rise further for one or two quarters (Call L392, L414); gold PCR 10.5% keeps pulling the blend down; no floor given | NO; moved closer in mechanism |
| (Pillar 2L clause) override self-withdraws if credit cost > 1.1% or PCR thins further | baseline undefined | CFO confirms the fall is gold mix (Call L167-170), not a policy cut | CONDITION MET QoQ (unchanged); operator rules |

8D. Four-Pillar inputs: concall adjustments: **DEFERRED TO /fttcp AND ROLE 1 (OR-30)**. Pillar-relevant facts are flagged below. Nothing is recomputed here.

| Pillar | Pre-Concall | Concall Evidence | Post-Concall Adjustment |
|---|---|---|---|
| Pillar 1 ROE (lender), via the FTTCP ROE forward verdict | ROE 17.0%, leverage 6.0x (Role 4 Step 7) | ROA 3% target "sooner", undated (Call L947-948); ROE target inaudible [ASR] (Call L736); 15% called an "interim" ROE milestone (Call L113); NIM compression to be offset by opex and credit cost (Call L567, L661-662, L689-L695); insurance about 0.1% of ROA at risk (Call L904-907) | Deferred. Flag for /fttcp: the ROA path now leans on opex and credit cost while NIM pressure is signalled. |
| Pillar 2L Asset-Quality Multiplier | 1.00x override; self-withdrawal condition met QoQ | CFO: PCR fall is gold mix; mortgage PCR "similar" (Call L167-171). Stage 2 not called peaked (Call L387-394). Nil auction loss claimed [ASR] (Call L420-424). Working LTV 72-74%, IGL to 85% (Call L321, L500-501). No price-down case. | Deferred. Operator ruling on the baseline still needed. Flag FTTCP-T3-NEGATIVE-DIAGNOSTIC (asset-quality bucket data absent across two concalls). |
| Growth Visibility Premium | 6 of 10 triggers lagging; gold AUM AT RISK | AUM 20-25% on flat gold; tonnage 10-12%; at least 150 H2 branches; ST LAP Q3 push; gold AUM guide not restated in number on the call; the guidance needs non-gold to triple its H1 pace (Step 2L) | Deferred. Flag GUIDANCE-CONSISTENCY. |
| Strategic Premium | ND | IGL live (20% of gold disbursal); eastern India entry; AUM per gold branch Rs 8 Cr to Rs 16 Cr (Call L268-271, L484, L69, L894-896) | Deferred. Single-credit rule: any ROA/ROE recovery credit sits in Pillar 1 OR Strategic Premium, never both. |
| FTTCP lender legs | NIM/spread STAGNANT; asset quality STARTING | NIM: yield guide declined, Q3 "intense", about 43% EBLR-linked borrowings (Call L307-309, L630-633); the +20 bp Q2 spread rise is the DA reversal; ex-DA the spread narrowed about 13-20 bps, while core NII / ATA held at 8.8% (Deck R1019-R1020, R1023-R1024). Asset quality: evasion on bucket data across two calls. | Deferred. The NIM leg is at risk of turning negative; Transition 3 carries the negative diagnostic. |

8E. Position decision
- Decision Status verified: WATCHLIST / AVOID (DEEP WATCH). Not held. Branch 8A-W.
- Credibility ratio below 60%? Not testable (ND). The 30-50% discount rule is not triggered by a ratio. The filing-first rule applies anyway: the call contradicts the filing in three places.
- Two or more DROPPED in trailing four? No (0 confirmed, 1 candidate).
- Undisclosed material risk? The insurance-distribution change (FN-13) is new risk language, about 10 bps of ROA. The 25% trim rule applies to held names only. Not held: logged.
- Undisclosed material positive? None that changes a thesis input. The IGL product and branch breakeven economics are operational context.
- Evasion pattern across three or more quarters? Not yet: four rows sit at two quarters (Step 3E).
- Narrative contradicts the filing materially? Yes on DA reliance and "improving asset quality". Trust the filing; note the credibility issue; tighten the watchlist (rows 33, 34, 40).
- Output: no change. WATCHLIST / AVOID (DEEP WATCH). Entry zone Rs 68-77 unchanged pending Role 1 (ENTRY-ZONE-BELOW-BOOK). Gate: Q3 FY27 results and call, mid-January 2027 [INFERENCE]. The operator sets status.

8F. Updated questions for the next review (feeds Role 4 Step 8.5 in Q3 FY27). All 47 Step 8.5 rows carry forward except the three ANSWERED rows (3, 7, 9). The twelve to press first on the Q3 FY27 call:

| # | Question | Why It Matters | What to Watch in Next Concall |
|---|---|---|---|
| 1 | Row 33: gold Stage 2 roll rate and expected peak | Stage 2 path drives PCR and Pillar 2L | A number, or a third refusal |
| 2 | Row 1: gold share of Stage 2 | Separates reading A from reading B | Product split given |
| 3 | Row 34: PCR floor; Stage 3 PCR by product | Most-at-risk tripwire; silent two quarters | A third silence triggers the downgrade rule |
| 4 | Row 29: gold 30+ and 60+ DPD | Silent two quarters | Disclosed, or a third silence |
| 5 | Row 30: Stage 3 ECL bridge | Mechanism given, no numbers | Bridge given |
| 6 | Row 32: Q2 and Q3 auction count, value and shortfall | Tests the six-year nil-loss claim [ASR] | Auction volume trend; any shortfall |
| 7 | Row 35: written FY27 guidance, entity vs gold | Resolves the record mismatch and the gold drop | Gold +25-30% kept or cut |
| 8 | Row 40: product split of the Rs 876.89 Cr assignment | Spoken Rs 700 Cr vs filed; DA-reliance contradiction | Q3 sell-down vs Q2 Rs 1,085 Cr |
| 9 | Row 5: gross gain on assigned pools | Tests whether off-book growth is bought | Gross gain disclosed |
| 10 | Row 37: Q3 gold yield and repricing share | NIM leg | Yield move vs CoF move |
| 11 | Row 41: LTV distribution and price-down breach share | Collateral cushion | Above-75% share |
| 12 | Row 42: ST LAP Q3 disbursal vs the 8-9 quarter bar | Dated promise | Above Rs 289 Cr (the highest of six known quarters; FY25 quarters are not in the run, so the true bar may be higher), or a miss |

Checkpoint: 8A-8F shown.

### R5 STEP 9 NOTION SAVE (payload only; this stage writes nothing)

- Row properties: none changed (Decision Status, Position Size, Promoter Verdict CAUTION, Management Grade ND). Key Notes prepend: Role 4 Step 9.
- Section to append under the Q2 FY27 Results Review: "Q2 FY27 Concall Analysis, call date ND (on or after 2026-10-15)", carrying R5 Steps 1-8F in full.
- Header for the save: participants MD & CEO Parvez Mulla, CFO C.V. Ganesh, Jagdish Rao, IR Lokesh Parik (Kadam, Pumar, Rati named, silent); hosting broker Aquarius Securities; duration 68m32s, Q&A about 52.1 minutes (76%, closing remarks excluded); analyst questions 26 from 9 analysts (23 inventory rows, three embedded follow-ups folded); business type Lender.
- Source line: "Concall reviewed 2026-10-19 | Source: ASR transcript of company audio, audio_recordings_of_q2_fy_27_post_results_conference_call.mp3 (Call L3)".

Concall Verdict:
- Management Credibility (this quarter): Grade ND (no scorable commitment)
- Trailing 4-Quarter Credibility Ratio: ND (0 points / (6 commitments - 6 unclear))
- Management Archetype (6E): ND (specificity 0.29-0.31, bottom row: MEASURED & CREDIBLE or EVASIVE, resolved at the Q4 FY27 review)
- Role 1 Track Record Input: ND
- Net concall impact on thesis: Maintained (lagging numbers confirmed; leading variables declined; three filing contradictions; coverage and funding questions open)
- Position decision: no change, WATCHLIST / AVOID (DEEP WATCH); entry zone unchanged pending Role 1

### SECTION C: COMBINED VERDICT (Role 4 + Role 5)

| Element | Reading |
|---|---|
| Filing-derived signals | PAT +63.1% YoY on real core growth; PCR -299 bps; Stage 2 +34.6% with coverage down; stressed coverage 24.5% to 20.2%; growth off-book; H1 net de-leverage nil; EPS misprint |
| Concall-derived signals | Credit cost, GNPA, AUM and ROA guides kept or raised; Stage 2 peak, gold yield and ST LAP numbers declined; NIM pressure and an insurance-income headwind signalled; record DA against a stated wish to cut DA; gold AUM guide not restated in number |
| Reconciliation | Of 38 spoken claims checked, the filing confirms 22 and contradicts 3. The call attributes the asset-quality move to gold without product data. It never addresses the stage-wise coverage fall. |
| Net thesis impact | Maintained. No tripwire fired. The PCR tripwire moved closer in mechanism. Credibility ND. |
| Position decision | No change: WATCHLIST / AVOID (DEEP WATCH). Operator rulings open: Pillar 2L baseline; credit-cost tripwire basis. |
| Watchpoints for next quarter | Q3 credit cost (single cleanest metric); Stage 2 and PCR; ST LAP Q3 bar; tonnage at or above 13.4 t; Q3 sell-down vs Rs 1,085 Cr; written FY27 guidance; third-quarter silence on DPD, bridge, FVOCI or CRAR floor |

---

## MONITORABLES / CATALYST LIST (seeded by A3 F6 registers and F13, including the concall commitment register C01-C26)

| # | Item | Implied date | Source |
|---|---|---|---|
| 1 | DONE: Q2 FY27 call transcript (ASR of company audio) read; prior and new questions graded (Step 8.5, Role 5 Step 3E) | done 2026-10-19; call date ND, on or after 2026-10-15 | Call L1-L21; Deck fulltext L18, L30-35 |
| 2 | Results published in Business Standard and Pratahkal | about 2026-10-17 | Res R649, L61 |
| 3 | Q3 FY27 results: credit cost, PCR, Stage 2 (management: no peak), stressed coverage, gold Stage 3, DA line | mid-January 2027 [INFERENCE from 15-Jul and 15-Oct cadence] | Res R662, R657; Call L387-394 |
| 4 | Q3 FY27 ST LAP disbursal best of the last 8-9 quarters (above Rs 289 Cr, Q4 FY26, the highest of the six known quarters; FY25 quarterly values are not in the run, so the true bar may be higher; row 42 asks for the series) and yield above Q2 (concall C13) | Q3 FY27 results, mid-January 2027 | Call L588-591, L611-613; Deck R475-R479 |
| 5 | Q3 FY27 gold tonnage at or above 13.4 t to keep the FY27 path (concall C09) | mid-January 2027 | Call L670, L885-886; Deck R491 |
| 6 | Q3 FY27 call transcript: re-grade carried questions; a third consecutive silence on DPD, FVOCI, GS3 bridge or CRAR floor triggers the Role 5 downgrade rule | mid/late January 2027 [INFERENCE] | Role 5 Step 3E |
| 7 | At least 150 branches in H2 FY27 (concall C06). Split, two parses [ASR]: (a) about 75 in Q3, 100 in Q4; (b) about 75 done in Q2 (filed 74), about 100 in Q3, more in Q4. Separating observation: Q3 FY27 additions, about 75 vs about 100 | Q3 FY27 results; by 2027-03-31 | Call L187-189, L539-541; Deck R033 |
| 8 | Remaining 126 of 200 FY27 branches | by 2027-03-31 | Deck R033; Notion promise log |
| 9 | Gold tonnage +10-12% FY27 (13.86-14.11 t derived) | by 2027-03-31 | Deck R491; Notion; Call L885-886 |
| 10 | Gold AUM +25-30% FY27 on a price-flat basis (not restated in number on the call; reaffirmed only as "our guidance", Call L248-L249, L292-L293; DROPPED candidate) | by 2027-03-31 | Deck R441-R443; Notion |
| 11 | Entity AUM +20-25% FY27 on flat gold (Rs 24,184-25,191 Cr derived); Q1 log +20-22% (Rs 24,184-24,587 Cr derived) (concall C03) | by 2027-03-31 | Call L727-733, L757-758; Deck R423; Notion |
| 12 | Credit cost "way below 1%" FY27 (concall C01) | by 2027-03-31 | Call L57, L89, L370; Notion promise log |
| 13 | GNPA below 2% (concall C02) | each quarter; 2027-03-31 | Call L372-373 |
| 14 | ROA +30-40 bps over FY26 2.4% (2.7-2.8%; Q1 log +20-30 bps) (concall C04) | by 2027-03-31 | Call L728-729 |
| 15 | ROA 3% "sooner than we had promised" (concall C05) | undated | Call L735-736, L947-948 |
| 16 | H2 FY27 cost-to-income contained at about 52.5% ("hopeful") (concall C07) | Q3 and Q4 FY27 results | Call L181, L190-192 |
| 17 | Gold customer-behaviour transition settles in one or two more quarters (concall C11) | by Q4 FY27 (2027-03-31) | Call L414-415 |
| 18 | No auction loss on principal or interest (concall C12) [ASR] | standing; each quarter | Call L420-424 |
| 19 | "Reduce reliance on direct assignment" (concall C19): Q3 sell-down vs Q2 Rs 1,085 Cr | Q3 FY27 results | Call L56 (ledger MFS-C11); Deck R680 |
| 20 | Fund growth through internal accruals, no equity (concall C20) | standing | Call L129 |
| 21 | Insurance-distribution change; substitute about 0.1% of ROA (concall C21) | conditional, undated | Call L197-199, L904-907 |
| 22 | CRAR at or above 16% (07041, 07058) and 15% (07066) | at all times; next audited test 2027-03-31 | Res R654-R655, Annexure II |
| 23 | D/E within 6x (07066, tested on 30-Sep-2026 figures, Res R745); TOL/ATNW at or below 7.0 (07041, 07058; filed 4.61x is on 31-Mar-2026 audited figures, Res R743-R744) | tenor; next TOL/ATNW test on 31-Mar-2027 audited figures | Res R653, R543-R544, R743-R745 |
| 24 | GNPA at or below 4-5%, NNPA at or below 3-4% | tenor; half-yearly | Res R523-R542 |
| 25 | Security cover at or above 1.10x on Rs 278.75 Cr secured NCDs | ongoing; next certificate with Q4 FY27 | Res R367-R368, R519-R520 |
| 26 | Management certification of other NCD covenants | each half-year; next 2027-03-31 | Res R652 |
| 27 | FY27 audited results and annual credit cost | late April 2027 [INFERENCE from FY26 audit report 2026-04-28] | Res R664 |
| 28 | Q1 FY28 results | mid-July 2027 [INFERENCE] | Res R662 |
| 29 | FY27 Annual Report and AGM (actuarial assumption, FVOCI detail, joint-auditor tenure) | about late September 2027 [INFERENCE from 2026 AGM 29-Sep] | Notion AGM record; A3-03, A3-07 |
| 30 | ESG KPI evaluation metrics ("being developed") | undated | Deck R1091 |
| 31 | Nation Skill Building CSR apprentice programme | undated; first in this deck | Deck R1099 |
| 32 | Digital ecosystem build | undated aspiration | Deck R1081 |
| 33 | Stree Sakthi gold scheme crossed Rs 100 Cr | completed (launched 2026-01-07) | Deck R1095-R1096 |
| 34 | Board outcome forward items (F13) | none beyond results approval and publication | Res R728, R649 |
| 35 | Operator rulings: the Pillar 2L self-withdrawal baseline (QoQ vs FY26) and the credit-cost tripwire basis (average total assets vs average AUM) | before the next /fttcp or Role 1 refresh | Res R440-R442; Deck R096; Notion Pillar 2L |

---

## VERDICT AND FLAGS

Protocol verdict: **PROCEED WITH FLAGS**. Cash conversion INDETERMINATE-WITH-DIRECTION (growth-induced) caps at PROCEED WITH CAVEATS or below. Flags below propagate. No mechanical failure. Extraction defects were resolved by the orchestrator check. The concall adds flags, fires no tripwire and changes no Decision Status. Role 5 loop 1 changes no verdict, tripwire or Decision Status: every fix is a qualifier, a count or a cite. Role 5 loop 2 (A5 C7) corrects the Q41 and flag 5 wording only; it changes no number, flag, verdict, tripwire or Decision Status.

Flags:
1. PILLAR2L-SELFWITHDRAW-CONDITION: PCR thinned QoQ 38.36% to 35.37%; clause condition met on QoQ baseline, not on FY26 baseline. The CFO attributes the fall to gold mix (Call L167-171). Operator ruling.
2. PCR-EROSION: checklist item 2 AMBER; red line 32% holds. PCR floor silent on the call for a second quarter (FN-16).
3. COVERAGE-RELEASE-PAT [INFERENCE]: at Q1 stage coverage, about Rs 19.3 Cr more ECL; about 88% of the QoQ PAT gain; credit cost about 1.0%. Stage 1 took Rs 12.0 Cr (55%) of the Rs 21.8 Cr ECL build; new stressed assets of Rs 195 Cr got Rs 10.0 Cr (5.1%); stressed coverage 24.5% to 20.2%. Reading B (release) stays live. The call did not address it.
4. STAGE2-SURGE and STAGE2-NO-PEAK: Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%. The CEO declined a peak call and a number; one or two more quarters (FN-02, Call L387-415).
5. GOLD-GROWTH-QUALITY and LTV-CREEP: tonnage +1.6% QoQ vs gold AUM +6.5%; portfolio LTV 68.0%; working mix 72-74% and IGL up to 85% (Call L321, L484, L500-501); 90-95% of customers want the slab maximum, 75% or 80% (Jagdish, Call L480-L483); the CEO puts the working mix at 72-74%, not everybody at that highest one (Call L500-L502); filed origination LTV 72.1% (Deck R327); no gold-price-down case (FN-09, FN-18); gold Stage 3 0.1% to 0.5% QoQ (0.4% a year ago, +10 bps YoY).
6. GOLD-TRIGGER-AT-RISK and GOLD-AUM-GUIDE-NOT-RESTATED: gold AUM +25-30% (price flat) is reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t), against +2.4% in H1; price-flat pace about +19% to +26%; Q2 growth about 70% price. The guide was not restated in number on the call; the gold-growth answer reaffirmed "our guidance" without one (Call L248-L249, L292-L293) (DROPPED candidate, FN-04).
7. GUIDANCE-RECORD-MISMATCH: the CEO says guidance is not revised (Call L727) but restates AUM 20-25% and ROA +30-40 bps against a Q1 log of 20-22% and +20-30 bps. ASR or log error possible.
8. GUIDANCE-CONSISTENCY [derived]: a 20% entity AUM floor at a flat gold price needs non-gold AUM +10.2% to +12.5% in H2 against +3.2% in H1.
9. OFFBOOK-DEPENDENCE and DA-RELIANCE-CONTRADICTION: AUF +Rs 27 Cr vs AUM +Rs 899 Cr; gold AUF -Rs 52 Cr; buyer identity ND. Management says it will "reduce our reliance on direct assignment" (Call L56, ledger MFS-C11) in the quarter of a record Rs 1,085 Cr sell-down (Deck R680).
10. SELLDOWN-DA-GAP: deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr vs spoken "approximately 700 crores" of gold (Call L148); Rs 208 Cr unreconciled. Co-lending named as a route (Call L93, L149 [ASR]), size NOT DISCLOSED.
11. DA-DRAG: net DA loss two quarters running; forward schedule not given for a second quarter (FN-21).
12. NIM-PRESSURE-SIGNALLED: yield guide declined, Q3 "intense", NIM compression to be offset by opex and credit cost, unsized (Call L307-309, L567, L652-662, L681-695). The Q2 reported spread rise of +20 bps (XC) is the DA-drag reversal; ex-DA the spread narrowed about 13-20 bps; core NII / ATA held at 8.8% (Deck R1019-R1020, R1023-R1024).
13. INSURANCE-INCOME-RISK: an insurance-distribution change raised by the CFO, about 0.1% of ROA, substitute unnamed (Call L197-199, L904-907).
14. DECLINED-GUIDANCE: gold yield, Stage 2 and ST LAP numbers declined (FN-14).
15. SPOKEN-VS-FILED-DRIFT: gold branches 831 vs 706; DA about 700 vs 876.89; PCR 35.5% vs 35.37%; core yield 16.40 spoken vs about 16.7% ex-DA (FN-15, FN-07). A3's yield-direction drift dissolves under XC.
16. REPEATED-EVASION-2Q: gold DPD, FVOCI detail, GS3 provision bridge and CRAR equity floor silent on two consecutive calls. A third triggers the Role 5 downgrade rule.
17. FTTCP-T3-NEGATIVE-DIAGNOSTIC: asset-quality bucket data absent across two concalls (Role 5 Step 4B rule). For /fttcp.
18. CREDIBILITY-ND: credibility ratio ND. All six quantified Q1 commitments are FY27 targets (UNCLEAR at H1). Role 1 track-record input ND. Archetype ND (specificity 0.29-0.31).
19. LEVERAGE-LED-ROE and CAPITAL-COMPRESSION: leverage 5.0x to 6.0x; CRAR -144 bps in H1; D/E 4.61x vs 6x cap; H1 net de-leverage nil (Mar-26 and Sep-26 both 4.61x).
20. EPS-MISPRINT: Q2 basic EPS 3.56 printed vs 3.49 derived. Not mentioned on the call.
21. CREDITCOST-BASIS: Notion records mix AUM and average-asset bases. Operator ruling open.
22. NOTION-STALE: CMP, gold mix, secured share; PRIOR-FVOCI-UNIT ("~585cr" vs Rs 58.51 Cr filed).
23. CASHCONV-INDETERMINATE-WITH-DIRECTION: collection efficiency and write-offs ND in all four documents.
24. DISCLOSURE-SILENCE: on the call, Role 4 rows 1-31 graded 3 answered, 8 partly, 20 not addressed. The 13 prior questions graded 1 answered, 8 partial, 4 not addressed (0 of 13 fully answered on the filings alone).
25. GROWTH-TRIGGERS-LAGGING: entity AUM, branches, tonnage, de-leverage DELAYED; mortgage, co-lending and gold AUM WEAKENED (post-call).
26. TRACKER-ROWS-ND: 0 signals supplied; reopen Role 5.5.
27. PEER-CROSSCHECK-UNVERIFIABLE: no peer concalls passed. Management claims peers will show similar Stage 2 numbers (Call L378-380).
28. ENTRY-ZONE-BELOW-BOOK: zone max Rs 77 < BVPS Rs 84.4 (Role 1).
29. PROJECTIONS-ND: no bear/base/bull P&L on Notion; 6A and 8A-W landing not assessable.
30. CONCALL-ASR-SOURCE: machine transcript of company audio; 52 of 74 turns speaker-inferred; 9 mixed turns; garbled at Call L133-135, L152-153, L420, L736, L826. Conclusions resting on them are labelled [ASR].
31. PIPELINE A1-EXTRACTION-DEFECTS: OCI sign misreads (R101, R134-R137, R158-R160), slide 22 and slide 25 attribution; resolved via XC. A2 adds four results rows (L525, L526, L812, L932) in loop 1. A3 concall FN-06 and FN-07 used the uncorrected slide 25 labels; their spread and yield-direction legs dissolve. A1 and A2 missed concall units; A2 Role 5 loop 1 adds them as MFS-C1 to C21 and re-attributes R121-R123 and R130-R131.
32. DEFERRED-OR30: Role 4 Steps 6.5 and 7 and Role 5 Step 8D deferred to /fttcp and Role 1.

---

## PLAIN-LANGUAGE BRIEF

Provenance labels: FILED = results filing; MGMT-DECK = investor presentation or press release; MGMT-CALL = the Q2 FY27 call (machine transcript, most speakers inferred); INFERENCE = A4 reasoning or arithmetic on the above. Every figure is from this quarter's documents unless marked "prior Notion".

### 1. Summary narrative
Fedfina earned Rs 130.75 Cr after tax in Q2 FY27. That is 63.1% more than a year ago (FILED).
Return on equity reached 17.0% and return on assets 2.8% (MGMT-DECK). Management repeated both on the call (MGMT-CALL).
Loans under management grew 36.6% to Rs 22,035 Cr (MGMT-DECK). Cost-to-income fell from 56.9% to 52.5% (FILED, derived).
None of the three tripwires fired. Credit cost was 0.6%, ROE is above 14%, and PCR is 35.37%, above 32% (FILED; MGMT-DECK).
Bad loans rose while the provision charge fell. Gross Stage 3 went from 1.55% to 1.82%, and PCR fell from 38.36% to 35.37% (FILED).
The CFO blamed the whole rise on gold loans (MGMT-CALL). The CEO said an April change moved gold borrowers from one payment at the end to regular interest (MGMT-CALL). Neither gave a product split to prove it.
Rs 195 Cr of new stressed loans got only Rs 10 Cr of new provision (MGMT-DECK, derived). At last quarter's coverage, provisions would be about Rs 19 Cr higher (INFERENCE). Nobody on the call raised this.
Growth went off the balance sheet. Loans on the books rose Rs 27 Cr while loans under management rose Rs 899 Cr (MGMT-DECK).
Management said it wants to rely less on loan sales. It sold a record Rs 1,085 Cr of loans in the quarter (MGMT-CALL; MGMT-DECK).
The CFO put the gold loan sale at about Rs 700 Cr. The filing shows Rs 876.89 Cr assigned (MGMT-CALL; FILED).
Management kept credit cost "way below 1%", bad loans below 2% and AUM growth of 20-25% at a flat gold price (MGMT-CALL). It aims for a 3% return on assets "sooner", with no date.
It refused numbers for gold yield, Stage 2 loans and small-ticket property loans. It said Q3 will be intense and that rate rises may squeeze margins (MGMT-CALL).
The printed Q2 basic EPS of Rs 3.56 is wrong. The half-year figure gives Rs 3.49 (FILED, derived). The call did not mention it.
The decision does not change: WATCHLIST / AVOID, deep watch. The stock sits about 2x above the Rs 68-77 entry zone on a stale price (prior Notion).
The operator must rule on two items: whether the PCR fall triggers the Pillar 2L step-down from 1.00x to 0.80x, and which basis the credit-cost tripwire uses (average total assets or average AUM).

### 2. Sector intelligence
Gold loans are the fastest part of the book. Fedfina's gold book grew 77% in a year (MGMT-DECK).
Most of that came from a higher gold price and higher loan-to-value, not from more gold. Tonnage rose 16% a year, and only 1.6% in the quarter (MGMT-DECK).
In Q2, about 70% of gold-book growth came from the gold price (INFERENCE on MGMT-DECK data). Management still called gold prices "almost flat" (MGMT-CALL).
At a flat gold price, the FY27 gold guide of +25-30% needs FY27 tonnage of about 14.0 t. That is +11.2% on 12.6 t, against +2.4% in H1 (INFERENCE). Management did not repeat the gold guide as a number on the call. It said only that it would continue with "our guidance" (MGMT-CALL).
Management says gold competition was "heightened" in Q2 and Q3 "will be an intense market" (MGMT-CALL). It says banks compete in a different segment; the fight is with other NBFCs.
The CEO says an April 2026 change caused the rise in gold Stage 2 and Stage 3 loans (MGMT-CALL). Gold loans moved from one bullet payment to periodic interest. The rule's text is not in this run.
He expects one or two more quarters before borrower behaviour settles (MGMT-CALL).
Portfolio LTV is 68.0% (MGMT-DECK). New loans run at 72-74%, and income-generating gold loans go up to 85% (MGMT-CALL). A fall in the gold price now hits a thinner cushion (INFERENCE). The call offered no price-fall case.
Management expects interest rates to rise (MGMT-CALL). About 43% of borrowings are linked to the bank external benchmark rate and reprice fast (MGMT-CALL, derived). About 58% of loans are short gold loans that reprice at maturity (MGMT-CALL).
Funding cost rose a little: 7.7% to 7.9% on slide 25 and 7.74% to 7.87% on the P&L basis. The daily measure the CFO quoted stayed at about 7.8% (MGMT-DECK; FILED, derived; MGMT-CALL). The reported spread widened from 8.6% to 8.8% (MGMT-DECK). That rise is the end of last quarter's loan-sale drag. Without it, the spread narrowed about 13-20 basis points (INFERENCE).
The credit rating is AA+/Stable from four agencies, as reported in the deck (MGMT-DECK).

### 3. Business-model intelligence
Fedfina lends against gold and against property. Gold is 54.1% of the book, medium-ticket LAP 27.5%, small-ticket LAP and home loans 17.8% (MGMT-DECK). The Notion page still says about 46.5% gold (prior Notion, stale).
It earns a spread of about 8.8% between loan yield (16.7%) and borrowing cost (7.9%) (MGMT-DECK, image check). The spread was 8.7% a year ago, so it is flat.
Management now steers the business on return on assets, not on yield (MGMT-CALL). If margins fall, it plans to pull on costs and credit cost instead.
That lever is partly used. Opex rose from 4.8% to 4.9% of assets, and at least 150 more branches open in H2 (MGMT-DECK; MGMT-CALL). The CFO is only "hopeful" of holding cost-to-income near 52.5% (MGMT-CALL).
A new gold branch breaks even at Rs 6-7 Cr of loans in 12-13 months (MGMT-CALL). The CEO tied that timeline to a rising or current gold price. Last year's branches grew while gold value per gram rose about 38% (INFERENCE). The timeline is untested at the flat price the guidance assumes.
The model is drifting in three ways.
One: it grows by originating loans and selling part of them to banks. The off-book share rose from 23.2% to 26.2% (MGMT-DECK). Assignment is filed at Rs 876.89 Cr (FILED). The CFO named co-lending in gold as a second route, with no size (MGMT-CALL).
Two: mortgage growth is slow. Mortgage AUM grew 13.5% a year, below the 15-20% guide (MGMT-DECK). Management promises the best small-ticket LAP quarter in two years in Q3. It now approves 40-45% of applicants, up from about 30% (MGMT-CALL).
Three: new branches are gold branches. Mortgage hubs fell from 129 to 125 (MGMT-DECK).
Insurance income is about 0.1% of assets, and the CFO expects a rule change there (MGMT-CALL).
The parent, Federal Bank, owns 60.6% (MGMT-DECK). Its term loan to Fedfina fell from about Rs 1,066 Cr to Rs 905 Cr in the half year (FILED, OCR-garbled page). No Federal Bank person spoke on the call (MGMT-CALL).
Collection efficiency and write-offs are NOT DISCLOSED in any document. The real cash test for a lender cannot be run.

### 4. Competition intelligence
No peer figures or peer calls were passed to this run. Peer numbers are NOT FOUND.
In gold loans, management says the fight is with other NBFCs, and banks play in a different yield band (MGMT-CALL). The large listed gold lenders, Muthoot Finance and Manappuram Finance, have far larger networks (INFERENCE, no figures).
Management claims its gold yield fell only 10 bps in Q2 while peers cut harder (MGMT-CALL). The filings do not show product yields, so this cannot be checked.
Management says peers will report similar Stage 2 rises (MGMT-CALL). Their Q2 FY27 numbers will test this. If peers show no such rise, the "industry change" story weakens (INFERENCE).
In small-ticket LAP, the same players chase loans hard, and small finance banks and housing finance companies compete too (MGMT-CALL). Fedfina works the 16-17% yield band, not the 20-22% band (MGMT-CALL).
Fedfina wins on its parent-bank name and AA+ rating, which keep its borrowing cost near 7.8% (MGMT-DECK; INFERENCE).
The competitive risk to watch: a rate rise squeezes margins just as gold competition peaks (MGMT-CALL). The lender with more branches and more grams per branch then holds up better (INFERENCE).

### 5. Forward map (next about 10-11 months)
Make-or-break reading: Q3 FY27 credit cost on average total assets, at the Q3 results in mid-January 2027. Bull at or below 0.8%. Bear at or above 1.0%.
- Mid-January 2027, Q3 FY27 results. Bull: credit cost at or below 0.8%, PCR at or above 35.37%, Stage 2 stops rising. Bear: credit cost at or above 1.0% as coverage catches up, and Stage 2 keeps rising as the CEO warned.
- Mid-January 2027, Q3 small-ticket LAP. Bull: disbursals above Rs 289 Cr (the highest known quarter; the true bar may be higher) at a higher yield. Bear: the promised best quarter in two years does not come.
- Mid-January 2027, Q3 gold tonnage. Bull: 13.4 t or more. Bear: tonnage stays near 12.9-13.3 t and growth stays price-led.
- Mid-January 2027, Q3 sell-down. Bull: loan sales fall below Rs 1,085 Cr, as management promised. Bear: sales rise again and the off-book share keeps climbing.
- Mid/late January 2027, Q3 call. Bull: management gives the Stage 2 split, the PCR floor and written guidance. Bear: a third silent quarter on gold DPD, the provision bridge or the equity floor.
- By 31-Mar-2027, at least 150 H2 branches. Bull: they open and cost-to-income holds near 52.5%. Bear: cost-to-income rises as branches arrive.
- By 31-Mar-2027, AUM +20-25% (Rs 24,184-25,191 Cr). Bull: tonnage and property loans carry it at a flat gold price. Bear: it is met only if the gold price keeps rising.
- By 31-Mar-2027, covenant and CRAR test. Bull: CRAR stays near 21% without new equity and D/E falls below 4.61x. Bear: an equity raise is announced, or CRAR falls toward 18%.
- Late April 2027, FY27 audited results. Bull: full-year credit cost below 1% with write-offs disclosed. Bear: write-offs reveal a larger loss pool behind the ARC sale.
- Mid-July 2027, Q1 FY28 results. Bull: on-book growth resumes as sell-down slows. Bear: growth still depends on loan sales to buyers.
- About late September 2027, FY27 Annual Report and AGM. Bull: FVOCI, hedge and joint-auditor details close the open questions. Bear: the disclosure silence continues into a third period.

---

## LOOP 1 CHANGES (A5 audit work/audit_fedfina_q2fy27.md; change log, not narrative)

1. F1: Step 3 diagnostic. PPOP growth needed for a flat Q3 PAT is 3.4% ((178.00 + 34.06) / 205.08), not "about 4%".
2. F2: Step 1L-b pattern line. 8 partial (rows 1, 2, 5, 6, 7, 8, 10, AR-1), 5 not addressed (rows 3, 4, 9, AR-2, AR-3). Flag 15 aligned.
3. F3: Step 2 diagnostic 4. Treasury is the main core-PBT-to-PAT wedge (Rs 3.71 Cr post-tax, 4.7 pp, 64%); ETR is second (Rs 2.05 Cr, 2.5 pp, 36%).
4. M3: stage-wise ECL build table added in the Step 4 memo (Stage 1 +12.0 of +21.8 Cr; stressed +195 Cr got +10.0 Cr, 5.1%; stressed coverage 24.5% to 20.2%). The fork is re-weighed: reading B stays live with at least equal weight. Grafted in flag 3, Q1 rationale, Step 5L table and brief.
5. M4: gold AUM price-flat decomposition table added in 6D. The gold AUM trigger is re-graded to AT RISK in 1L-c and 6D. New flag 6; Step 6.5 note; brief sector part and forward map updated.
6. M5: Mar-26 D/E 4.61x (Res R390) and average leverage 5.9x to 6.0x (Deck R1064) added. De-leverage re-graded: 1L-c NOT DELIVERED in H1; 6D DELAYED. Step 5L capital paragraph and flag 10 updated.
7. M6: TOL/ATNW 4.61x stated as 31-Mar-2026 audited basis (Res R743-R744) in the Annexure II note row, monitorable 9 and Q17. Q17 now compares it with the 4.79x computed on the same Mar-26 figures.
8. C1: deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr. The gap of Rs 208.11 Cr is stated as UNRECONCILED, route NOT DISCLOSED. CLM is listed as a funding source of unresolved size. "Via DA, not CLM" is removed. Changes in Note 10(II), 1L-b row 6, off-book table, 5.5C, 6D, Q4, new Q31, flag 8 and brief.
9. C2: entity AUM +20-22% is DELAYED in 1L-c, 6D and Q7.
10. Ledger preamble: results ledger is now 752 rows, with 4 A2 additions (L525, L526 NOT DISCLOSED; signature blocks L812, L932). Signatures are 7, not 5. All four were read and reviewed; no new finding.
11. Style S1: Q1 FY26 core PBT cell now 94.39 (derived). S2: "reconcile within Rs 0.1 Cr". S3: CoB described as up 13-20 bps on two of three measures (Step 4, Step 5L, CoB note, brief). S4: ROA trigger labelled ON TRACK in both places. S5: "at the current gold price and LTV" added in Step 4. S6: gold Stage 3 YoY context (0.4% a year ago, +10 bps) added in Step 5L and flag 5.

## LOOP 2 CHANGES (A5 re-audit loop 1; change log, not narrative)

1. F4: Step 7 Growth Visibility row. Growth triggers now read 6 of 10 (4 DELAYED, 2 WEAKENED), plus gold AUM AT RISK, not 5 of 10.
2. C3: brief sector part. The +25-30% FY27 gold guide is reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t), against +2.4% in H1. The +19% to +26% range is kept and tied to the Q2 tonnage pace and the full tonnage guide. The AT RISK clause in 1L-c, 6D, flag 6 and the YAML flag now carries the same 14.0 t condition; "on track only with a rising gold price or LTV" is removed.
3. S11: Annexure II note row. D/E anchor changed from Res R543-R545 to Res R543-R544, R745.

```yaml
stage: A4-analyst
company: "FEDFINA"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, concall, presentation, pressrelease]
ledger_reconciliation:
  notes: 38
  turns: 74
  slides: 45
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20, FN21, FN22, FN23, FN24, FN25, FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10, FND-11, FND-12, FND-13, FN-01, FN-02, FN-03, FN-04, FN-05, FN-06, FN-07, FN-08, FN-09, FN-10, FN-11, FN-12, FN-13, FN-14, FN-15, FN-16, FN-17, FN-18, FN-19, FN-20, FN-21]
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST / AVOID (DEEP WATCH)"
position_branch: "8A-W"
sc_gap_pat_pct:
  - "Q2FY27: 0.0 (standalone only; no subsidiary/associate/JV, Note 6 Res R702 L432)"
  - "Q1FY27: 0.0 (standalone only)"
  - "Q2FY26: 0.0 (standalone only)"
  - "H1FY27: 0.0 (standalone only)"
  - "H1FY26: 0.0 (standalone only)"
  - "FY26: 0.0 (standalone only)"
questions_for_management:
  - {q: "What share of the Rs 587 Cr Q2 Stage 2 book is gold loans (Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%; stressed coverage 24.5% to 20.2%)? Call: PARTLY (CFO 'entirely' gold, no number, Call L160-161).", from_finding_id: "A3-11, FN09, FN10, FND-05, FN-02"}
  - {q: "What were gold auction losses in Q2 FY27, in Rs Cr? Call: PARTLY (nil six-year record claimed, negation ASR-garbled, Call L420-424).", from_finding_id: "FN11, FN-01"}
  - {q: "Which gold loan industry change on slide 29 lifted gold Stage 3 from 0.1% to 0.5%? Call: ANSWERED (April change, periodic interest replacing bullet, Call L71-72, L154-159, L341-342).", from_finding_id: "FN03"}
  - {q: "Of the Rs 1,085 Cr Q2 sell-down (Rs 876.89 Cr filed as DA; Rs 208 Cr unreconciled), what share went to Federal Bank? Call: NOT ADDRESSED.", from_finding_id: "FN07, A3-12"}
  - {q: "What was the gross gain on pools assigned in Q2 FY27, before reversal on older pools? Call: NOT ADDRESSED.", from_finding_id: "FN08, FND-06, A3-09"}
  - {q: "At what CRAR level will the board raise equity (D/E 4.61x vs 6x cap, unchanged from Mar-26; CRAR 22.40% to 20.96% in H1)? Call: PARTLY (internal accruals stance, ASR 'internal approvals', Call L129).", from_finding_id: "A3-04, FN16, FND-07, FN-20"}
  - {q: "Which of the five FY27 guidance items from the Q1 call do you now revise? Call: ANSWERED ('not revised', Call L727) but restated figures differ from the Q1 log; gold AUM reaffirmed only as 'our guidance', no number (Call L248-249).", from_finding_id: "FN02, FND-13, FN-04"}
  - {q: "Will the company refile Q2 FY27 basic EPS (printed 3.56 vs 3.49 implied by H1 6.54 less Q1 3.05)? Call: NOT ADDRESSED.", from_finding_id: "A3-10"}
  - {q: "How many of the 126 remaining FY27 branches will open by 31-Mar-2027? Call: ANSWERED (at least 150 in H2, Call L187-189); split has two ASR parses (Call L539-541): 75 in Q3 and 100 in Q4, or 75 done in Q2, about 100 in Q3 and more in Q4.", from_finding_id: "FN15, FND-08"}
  - {q: "What 12-month AUM per branch do you target for the 74 Q2 branches? Call: PARTLY (breakeven Rs 6-7 Cr in 12-13 months, Call L714-722, tied by the CEO to a rising or current gold price, Call L715-716; untested at a flat price).", from_finding_id: "FN15, FND-08"}
  - {q: "What drove the Q2 ETR of 26.54% vs 25.17% statutory? Call: NOT ADDRESSED.", from_finding_id: "A3-05, FN04, FND-01"}
  - {q: "What is the outstanding FCY/ECB borrowing at 30-Sep-2026 (Q2 hedge OCI gain Rs 43.48 Cr)? Call: NOT ADDRESSED.", from_finding_id: "A3-08, FN05, FND-04"}
  - {q: "What principal outstanding did the 48 accounts sold to ARCs carry (L525 blank)? Call: NOT ADDRESSED.", from_finding_id: "A3-02"}
  - {q: "What were total H1 FY27 write-offs, in Rs Cr? Call: NOT ADDRESSED.", from_finding_id: "A3-02, FN09"}
  - {q: "What makes up other financial liabilities of Rs 468.19 Cr at Sep-26 (Rs 216.38 Cr at Mar-26)? Call: NOT ADDRESSED.", from_finding_id: "A3-12"}
  - {q: "Who appointed V. Sankar Aiyar & Co. as joint statutory auditor, on what date, under which rule? Call: NOT ADDRESSED.", from_finding_id: "A3-03"}
  - {q: "Does the trust deed define total outstanding liability as borrowings only (filed TOL/ATNW 4.61x on 31-Mar-2026 audited figures vs 4.79x computed)? Call: NOT ADDRESSED.", from_finding_id: "A3-15"}
  - {q: "How did the Federal Bank derivative margin deposit reach Rs 16.16 Cr with nil opening and nil flow? Call: NOT ADDRESSED.", from_finding_id: "A3-16"}
  - {q: "What is the Rs 1.85 Cr H1 brand-usage fee to Federal Bank based on, and from what date? Call: NOT ADDRESSED.", from_finding_id: "A3-16"}
  - {q: "What is Gross Stage 3 % for North-originated mortgages of FY25-FY26 vintage? Call: NOT ADDRESSED.", from_finding_id: "FN12"}
  - {q: "What undrawn sanctioned lines did the company hold at 30-Sep-2026 (ALM <3m surplus Rs 186 Cr)? Call: NOT ADDRESSED.", from_finding_id: "FN17"}
  - {q: "Is the Q2 FY26 ECL column on the same basis as Q1 and Q2 FY27? Call: NOT ADDRESSED.", from_finding_id: "FN20"}
  - {q: "How many NAPS apprentices were on the rolls at 30-Sep-2026? Call: NOT ADDRESSED.", from_finding_id: "FN21"}
  - {q: "What were FY26 yield, CoB and spread on the old two-point basis? Call: NOT ADDRESSED.", from_finding_id: "FN24"}
  - {q: "Which CoB series does management steer on: slide 25 7.9% or daily I-GAAP 7.79%? Call: PARTLY (CFO cites 7.80 from the funding profile slide, no reconciliation, Call L141-144).", from_finding_id: "FN25, FN22, FN-07"}
  - {q: "Is the press-release H1 FY27 Shareholder's Fund of Rs 2,926.1 Cr the 31-Mar-2026 opening balance? Call: NOT ADDRESSED.", from_finding_id: "FND-03"}
  - {q: "Why did other income fall 1.9% YoY to Rs 27.78 Cr while AUM grew 36.6%? Call: NOT ADDRESSED (insurance about 0.1% of ROA tree, Call L904-905).", from_finding_id: "FND-09"}
  - {q: "Is the 0.6% credit cost on two-point or daily average total assets? Call: PARTLY ('average total assets, annualised', Call L87-88).", from_finding_id: "FND-12"}
  - {q: "Publish gold 30+ and 60+ DPD for Q2 FY27 (carried from Q1). Call: NOT ADDRESSED, second quarter.", from_finding_id: "carried Q1 Q4; A3-11; FN-19"}
  - {q: "Give the bridge for Stage 3 ECL from Rs 96.8 Cr to Rs 104.7 Cr (carried from Q1). Call: PARTLY (gold-mix mechanism, no bridge, Call L167-171).", from_finding_id: "carried Q1 Q9; FN09; FN-19"}
  - {q: "Through which route did the Rs 208 Cr of the Q2 sell-down not filed as direct assignment leave the book? Call: PARTLY (co-lending in gold named, ASR 'coal ending', Call L93, L149; no size).", from_finding_id: "FN07, A3-12, FND-07"}
  - {q: "How many gold auctions ran in Q2 FY27, at what value in Rs Cr, and was any shortfall written off against principal or interest? Confirm the six-year record wording.", from_finding_id: "FN-01"}
  - {q: "What share of gold Stage 2 at 30-Jun-2026 rolled to Stage 3 by 30-Sep-2026, and at what gold Stage 2 % do you expect the peak?", from_finding_id: "FN-02, FN-14"}
  - {q: "What PCR floor will the board accept as gold reaches 55-60% of AUM; give Stage 3 PCR by product (gold, mortgage, business loans) for Q1 and Q2 FY27.", from_finding_id: "FN-03, FN-16"}
  - {q: "Publish FY27 guidance in writing, split entity AUM and gold AUM: is gold AUM still +25-30% (reaffirmed only as 'our guidance', Call L248-249), and was the Q1 ROA guide +20-30 or +30-40 bps?", from_finding_id: "FN-04"}
  - {q: "In which quarter do you expect ROA of 3%, and what ROE target goes with it (inaudible at Call L736; the CFO calls 15% an 'interim' ROE milestone, Call L113)?", from_finding_id: "FN-05"}
  - {q: "What gold yield change do you plan for in Q3 FY27, and what share of borrowings reprices within three months of a 50 bp rate rise?", from_finding_id: "FN-06, FN-14"}
  - {q: "Give core yield ex-DA and cost of borrowing on one stated basis for Q1 and Q2 FY27, and the DA-unwinding effect in bps each quarter (spoken 16.40 ties only to the Q1 reported yield; ex-DA core derives to about 16.7% both quarters).", from_finding_id: "FN-07"}
  - {q: "How much DA excess-spread unwinding, in Rs Cr, will hit NII in each of the next four quarters, and when does net DA income turn neutral?", from_finding_id: "FN-21, FN-08"}
  - {q: "Give the product split of the Rs 876.89 Cr Note 10(II) assignment (spoken 'approximately 700 crores of the gold loan book'); why is weighted residual maturity 23 months; how does a record sell-down fit 'reduce reliance on DA' (Call L56, MFS-C11)?", from_finding_id: "FN-08"}
  - {q: "Give disbursal-weighted gold LTV for Q1 and Q2 FY27, the share of the gold book above 75% LTV, and the share that crosses the LTV limit at a 10% and a 15% gold-price fall (Jagdish: 90-95% of customers want the slab maximum, 75% or 80%, Call L480-483; the CEO puts the working mix at 72-74%, not everybody at that highest one, Call L500-502; filed origination LTV 72.1%, Deck R327; share of new loans at the cap ND).", from_finding_id: "FN-09, FN-18"}
  - {q: "Confirm the ST LAP disbursal series for the last nine quarters, the Q3 FY27 bar it must beat (Rs 289 Cr is only the highest of six known quarters), and 1+ DPD on loans approved at the early/mid-40s approval rate.", from_finding_id: "FN-10, FN-14"}
  - {q: "What gold tonnage do you target at 31-Dec-2026, in tonnes (FY27 guide needs 13.86-14.11 t)?", from_finding_id: "FN-11"}
  - {q: "What H2 FY27 cost-to-income ceiling do you commit to with at least 150 new branches?", from_finding_id: "FN-12"}
  - {q: "Which insurance-distribution change do you expect, by when, and which income line substitutes about 10 bps of ROA?", from_finding_id: "FN-13"}
  - {q: "Confirm the date ST LAP collections in-housing was completed.", from_finding_id: "FN-17"}
  - {q: "How many co-lending partners do you have, is Federal Bank one, and what co-lending volume ran in Q2 FY27, in Rs Cr?", from_finding_id: "FN-20"}
monitorables:
  - {item: "DONE: Q2 FY27 call transcript (ASR of company audio) read 2026-10-19; call date ND, on or after 15-Oct-2026", implied_date: "done 2026-10-19", source_ref: "Call L1-L21; Deck fulltext L18, L30-35"}
  - {item: "Results newspaper publication", implied_date: "about 2026-10-17", source_ref: "Res R649 L61"}
  - {item: "Q3 FY27 results: credit cost (single cleanest metric; bull <=0.8%, bear >=1.0%), PCR, Stage 2 (mgmt: no peak), stressed coverage, gold Stage 3, DA line", implied_date: "mid-January 2027 [INFERENCE]", source_ref: "Res R657, R662; Call L387-394"}
  - {item: "Q3 FY27 ST LAP disbursal best of last 8-9 quarters (above Rs 289 Cr, Q4 FY26, the highest of six known quarters; FY25 quarterly values not in the run, so the true bar may be higher; row 42 asks for the series) and yield above Q2 (concall C13)", implied_date: "Q3 FY27 results, mid-January 2027", source_ref: "Call L588-591, L611-613; Deck R475-R479"}
  - {item: "Q3 FY27 gold tonnage at or above 13.4 t keeps the FY27 path (concall C09)", implied_date: "mid-January 2027", source_ref: "Call L670, L885-886; Deck R491"}
  - {item: "Q3 FY27 call transcript: re-grade carried questions; third consecutive silence on DPD, FVOCI, GS3 bridge or CRAR floor triggers the Role 5 evasion rule", implied_date: "mid/late January 2027 [INFERENCE]", source_ref: "Role 5 Step 3E"}
  - {item: "At least 150 branches in H2 FY27 (concall C06). Split has two ASR parses: (a) about 75 in Q3, 100 in Q4; (b) about 75 done in Q2 (filed 74), about 100 in Q3, more in Q4. Separating observation: Q3 FY27 additions, about 75 vs about 100", implied_date: "Q3 FY27 results; 2027-03-31", source_ref: "Call L187-189, L539-541; Deck R033"}
  - {item: "Remaining 126 of 200 FY27 branches", implied_date: "2027-03-31", source_ref: "Deck R033; Notion promise log"}
  - {item: "Gold tonnage +10-12% FY27 (13.86-14.11 t)", implied_date: "2027-03-31", source_ref: "Deck R491; Notion; Call L885-886"}
  - {item: "Gold AUM +25-30% FY27 on a price-flat basis (not restated in number on the call; reaffirmed only as 'our guidance', Call L248-249, L292-293; DROPPED candidate)", implied_date: "2027-03-31", source_ref: "Deck R441-R443, R489-R491, R499-R501; Notion"}
  - {item: "Entity AUM +20-25% FY27 on flat gold (Rs 24,184-25,191 Cr); log said +20-22% (Rs 24,184-24,587 Cr) (concall C03)", implied_date: "2027-03-31", source_ref: "Call L727-733, L757-758; Deck R423; Notion"}
  - {item: "Credit cost 'way below 1%' FY27 (concall C01)", implied_date: "2027-03-31", source_ref: "Call L57, L89, L370; Notion promise log"}
  - {item: "GNPA below 2% (concall C02)", implied_date: "each quarter; 2027-03-31", source_ref: "Call L372-373"}
  - {item: "ROA +30-40 bps over FY26 2.4% (2.7-2.8% FY27; log +20-30) (concall C04)", implied_date: "2027-03-31", source_ref: "Call L728-729"}
  - {item: "ROA 3% 'sooner than promised' (concall C05)", implied_date: "undated", source_ref: "Call L735-736, L947-948"}
  - {item: "Contain H2 FY27 cost-to-income at about 52.5% ('hopeful') (concall C07)", implied_date: "Q3 and Q4 FY27 results", source_ref: "Call L181, L190-192"}
  - {item: "Gold customer-behaviour transition settles in one or two more quarters (concall C11)", implied_date: "by Q4 FY27 (2027-03-31)", source_ref: "Call L414-415"}
  - {item: "No auction loss on principal or interest (concall C12, ASR-garbled)", implied_date: "standing; each quarter", source_ref: "Call L420-424"}
  - {item: "Reduce reliance on direct assignment (concall C19): Q3 sell-down vs Q2 Rs 1,085 Cr", implied_date: "Q3 FY27 results", source_ref: "Call L56 (ledger MFS-C11); Deck R680"}
  - {item: "Fund growth through internal accruals, no equity (concall C20)", implied_date: "standing", source_ref: "Call L129"}
  - {item: "Insurance-distribution change; substitute about 0.1% ROA (concall C21)", implied_date: "conditional, undated", source_ref: "Call L197-199, L904-907"}
  - {item: "CRAR >= 16% (07041, 07058) and >= 15% (07066)", implied_date: "at all times; next audited test 2027-03-31", source_ref: "Res R654-R655"}
  - {item: "D/E within 6x (07066, 30-Sep-2026 basis); TOL/ATNW <= 7.0 (07041, 07058; filed 4.61x on 31-Mar-2026 audited figures)", implied_date: "tenor; next TOL/ATNW test on 31-Mar-2027 audited figures", source_ref: "Res R653, R543-R544, R743-R745"}
  - {item: "GNPA <= 4-5%, NNPA <= 3-4% covenants", implied_date: "tenor; half-yearly", source_ref: "Res R523-R542"}
  - {item: "Security cover >= 1.10x on Rs 278.75 Cr secured NCDs", implied_date: "ongoing; next certificate Q4 FY27", source_ref: "Res R367-R368, R519-R520"}
  - {item: "Management certification of other NCD covenants", implied_date: "2027-03-31", source_ref: "Res R652"}
  - {item: "FY27 audited results; write-offs and full-year credit cost", implied_date: "late April 2027 [INFERENCE]", source_ref: "Res R664"}
  - {item: "Q1 FY28 results", implied_date: "mid-July 2027 [INFERENCE]", source_ref: "Res R662"}
  - {item: "FY27 Annual Report and AGM: actuarial, FVOCI, joint-auditor tenure", implied_date: "about late September 2027 [INFERENCE]", source_ref: "Notion AGM record; A3-03, A3-07"}
  - {item: "ESG KPI evaluation metrics being developed", implied_date: "undated", source_ref: "Deck R1091"}
  - {item: "Nation Skill Building CSR apprentice programme", implied_date: "undated", source_ref: "Deck R1099"}
  - {item: "Digital ecosystem build", implied_date: "undated", source_ref: "Deck R1081"}
  - {item: "Operator rulings: Pillar 2L self-withdrawal baseline (QoQ vs FY26); credit-cost tripwire basis (average total assets vs average AUM)", implied_date: "before next /fttcp or Role 1 refresh", source_ref: "Res R440-R442; Deck R096; Notion Pillar 2L"}
flags:
  - "PILLAR2L-SELFWITHDRAW-CONDITION: PCR 38.36% to 35.37% QoQ meets 'PCR thins further' on QoQ baseline, not vs FY26 32.29%; CFO attributes the fall to gold mix (Call L167-171); operator ruling"
  - "PCR-EROSION: checklist item 2 AMBER; 32% red line holds; PCR floor silent on the call for a second quarter (FN-16)"
  - "COVERAGE-RELEASE-PAT [INFERENCE]: ~Rs 19.3 Cr ECL gap at Q1 stage coverage; ~88% of QoQ PAT gain; Stage 1 took 12.0 (55%) of 21.8 Cr build; stressed +195 Cr got 10.0 Cr (5.1%); stressed coverage 24.5% to 20.2%; the call did not address it"
  - "STAGE2-SURGE / STAGE2-NO-PEAK: Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%; CEO declined to call a peak or give a number; 1-2 more quarters (FN-02, Call L387-415)"
  - "GOLD-GROWTH-QUALITY / LTV-CREEP: tonnage +1.6% QoQ vs gold AUM +6.5%; book LTV 68.0% vs working mix 72-74% and IGL to 85% (Call L321, L484, L500-501); 90-95% of customers want the slab maximum, 75% or 80% (Jagdish, Call L480-L483); the CEO puts the working mix at 72-74%, not everybody at that highest one (Call L500-L502); filed origination LTV 72.1% (Deck R327); no gold-price-down case (FN-09, FN-18)"
  - "GOLD-TRIGGER-AT-RISK / GOLD-AUM-GUIDE-NOT-RESTATED: gold AUM +25-30% reachable at a flat price only if FY27 tonnage reaches about 14.0 t vs +2.4% in H1; the +25-30% was not restated in number on the call; the gold-growth answer reaffirmed 'our guidance' without one (Call L248-249, L292-293) (DROPPED candidate, FN-04)"
  - "GUIDANCE-RECORD-MISMATCH: CEO says guidance not revised (Call L727) but restates AUM 20-25% and ROA +30-40 bps vs Q1 log 20-22% and +20-30 bps; ASR or log error possible"
  - "GUIDANCE-CONSISTENCY [derived]: 20% entity AUM at a flat gold price needs non-gold AUM +10% to +13% in H2 vs +3.2% in H1"
  - "OFFBOOK-DEPENDENCE / DA-RELIANCE-CONTRADICTION: AUF +27 Cr vs AUM +899 Cr; 'reduce reliance on DA' (Call L56, ledger MFS-C11) vs record Rs 1,085 Cr sell-down (Deck R680)"
  - "SELLDOWN-DA-GAP: deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr vs spoken ~700 Cr; co-lending named as a route (Call L93, L149, ASR) with no size"
  - "DA-DRAG: net DA loss -12.9 / -1.2 Cr; forward schedule not given for a second quarter (FN-21)"
  - "NIM-PRESSURE-SIGNALLED: yield guide declined, Q3 'intense', NIM compression to be offset by opex and credit cost, unsized (Call L307-309, L567, L652-662, L681-695); the +20 bp Q2 reported spread rise (XC) is the DA-drag reversal; ex-DA the spread narrowed about 13-20 bps; core NII/ATA held at 8.8% (Deck R1019-R1020, R1023-R1024)"
  - "INSURANCE-INCOME-RISK: insurance-distribution change raised by the CFO, about 0.1% of ROA, substitute unnamed (Call L197-199, L904-907)"
  - "DECLINED-GUIDANCE: gold yield, Stage 2, ST LAP number declined (FN-14)"
  - "SPOKEN-VS-FILED-DRIFT: gold branches 831 vs 706; DA ~700 vs 876.89; PCR 35.5 vs 35.37; core yield 16.40 spoken vs about 16.7% ex-DA (FN-15, FN-07); A3 yield-direction drift dissolves under XC"
  - "REPEATED-EVASION-2Q: gold DPD, FVOCI detail, GS3 provision bridge, CRAR equity floor silent on two consecutive calls; a third triggers the Role 5 downgrade rule"
  - "FTTCP-T3-NEGATIVE-DIAGNOSTIC: asset-quality bucket data absent across 2 concalls (Role 5 Step 4B rule); for /fttcp"
  - "CREDIBILITY-ND: credibility ratio ND; all six quantified Q1 commitments are FY27 targets (UNCLEAR at H1); Role 1 track-record input ND"
  - "CONCALL-VERDICT: credibility grade ND; archetype ND (specificity 0.29-0.31 on 58 forward phrases, bottom row: MEASURED & CREDIBLE or EVASIVE); net thesis impact Maintained"
  - "LEVERAGE-LED-ROE / CAPITAL-COMPRESSION: leverage 5.0x to 6.0x; CRAR -144 bps H1; D/E 4.61x vs 6x; H1 net de-leverage nil"
  - "EPS-MISPRINT: Q2 basic 3.56 printed vs 3.49 derived; not mentioned on the call"
  - "CREDITCOST-BASIS: Notion mixes avg AUM (FY26 0.64%) and avg assets (company FY26 0.8%); operator ruling open"
  - "NOTION-STALE: CMP 164; gold mix 46.5% vs 54.1%; secured 98.9% vs 99.4%"
  - "PRIOR-FVOCI-UNIT: Notion '~585cr' vs filed Q1 FVOCI-loans OCI Rs 58.51 Cr"
  - "CASHCONV-INDETERMINATE-WITH-DIRECTION: growth-induced; collection efficiency and write-offs ND on all four documents"
  - "DISCLOSURE-SILENCE: 31 Role 4 questions on the call: 3 answered, 8 partly, 20 not addressed; 13 prior questions: 1 answered, 8 partly, 4 not addressed"
  - "GROWTH-TRIGGERS-LAGGING: entity AUM, branches, tonnage, de-leverage DELAYED; mortgage, co-lending WEAKENED; gold AUM WEAKENED"
  - "TRACKER-ROWS-ND: 0 signals supplied; reopen Role 5.5; 3 Case B candidates"
  - "PEER-CROSSCHECK-UNVERIFIABLE: no peer concalls passed; mgmt claims peers will show similar Stage 2 numbers (Call L378-380)"
  - "ENTRY-ZONE-BELOW-BOOK: zone max Rs 77 < BVPS Rs 84.4 (Role 1)"
  - "PROJECTIONS-ND: no bear/base/bull P&L; 6A landing not assessable"
  - "CONCALL-ASR-SOURCE: machine transcript of company audio; 52 of 74 turns speaker-inferred; 9 mixed turns; garbled at Call L133-135, L152-153, L420, L736, L826"
  - "PIPELINE: A1 OCI sign misreads and slide 22/25 attribution errors resolved via XC; A3 concall FN-06/FN-07 spread and yield-direction legs used the uncorrected slide 25 labels; A1/A2 concall units missed in loop 0 added as MFS-C1 to C21"
  - "DEFERRED-OR30: Role 4 Steps 6.5 and 7 and Role 5 Step 8D deferred to /fttcp and Role 1"
plain_language_brief_included: true
role5_loop_2: "C7 applied"
analyst_note: "Role 5 loops 1 and 2 apply A5's concall audits; no verdict, tripwire or Decision Status change. Loop 2 corrects Q41 and flag 5: 90-95% of customers want the slab maximum, but the CEO puts the working mix at 72-74% and filed origination LTV is 72.1%, so the share at the cap is ND. The call (ASR; 52 of 74 turns speaker-inferred) confirms the lagging filed numbers but declines the leading ones: gold yield, Stage 2, ST LAP disbursals. Coverage: total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build; stressed coverage fell 24.5% to 20.2%. The CFO attributes the Stage 2/3 rise and PCR fall entirely to gold, with no product split, so reading B stays live. Spread: the +20 bp reported rise is the DA-drag reversal; ex-DA the spread narrowed about 13-20 bps while core NII/ATA held at 8.8%. Funding: management says it will reduce DA reliance (Call L56), yet the Q2 sell-down was a record Rs 1,085 Cr. Guidance: the CEO says nothing was revised but restates AUM 20-25% and ROA +30-40 bps against a Q1 log of 20-22% and +20-30; gold AUM +25-30% is reaffirmed only as 'our guidance'."
review_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\fedfina-q2fy27\\work\\review_fedfina_q2fy27.md"
```

---

## OPEN ITEMS AT CLOSE (orchestrator record; text from the A5 loop-2 audit, no analysis added)

Loop cap reached (operator ruling 2026-10-17: one second loop, no third; close with open items flagged). A5 loop-2 verdict INCOMPLETE on one item; carried here for the operator:
- F5 (FACTUAL, A4 YAML analyst_note, about L814): "total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build" is not supported. A5 replacement text: "total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build". With no Stage 1 build the ratio still rises 1.365% to 1.423%. The body at L304 (55%) is correct. No figure, flag, protocol verdict or Decision Status changes.
  - Status (Role 5 merge, 2026-10-19): FIXED. The rewritten analyst_note in the YAML above and in work/blocks/a4.yaml reads "total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build". Flag 3 carries "(55%)" too.
- STYLE, logged only: S7-S10, S12-S14 (see work/audit_fedfina_q2fy27.md, Re-audit loop 2).

## ROLE 5 MERGE CHANGES (2026-10-19; change log, not narrative)

1. Header: run type is now FULL QUARTER, Role 4 + Role 5. Docs merged and inputs read add the concall. Concall source caveat added. Anchor convention adds Call L###, Call R###, T##, FN-xx (concall) vs FNxx (presentation), and C01-C26.
2. Ledger preamble: now 38 notes / 74 turns / 45 slides. Concall ledger line added (17 participants, 74 turns, 23 questions, 140 management numbers, 267 IDs, 0 orphans, all reviewed). Concall findings FN-01 to FN-21 listed as incorporated.
3. Extraction note: the slide 25 correction's second consequence is recorded. A3 concall FN-06 ("spread narrowed about 50 bps") and FN-07 ("yield opposite sign") used A1's swapped labels. On XC values both legs dissolve. FN-15 drifts fall from four to three.
4. New section "ROLE 5 CONCALL ANALYSIS" after Step 9 and before MONITORABLES. It runs Steps 0-9 in full: 55-claim inventory, Step 2L guidance table, 3A-3E promise audit against the Notion Q1 log (credibility ratio ND), 23-row Q&A inventory, three key exchanges, 5A/5B, tone and specificity (0.33; 16 hedge markers; archetype ND), a 38-claim filing reconciliation citing Role 4 rows (23 confirmed, 3 partly confirmed, 2 partly contradicted, 3 contradicted, 7 unverifiable), 7B/7C UNVERIFIABLE this run, 8A-8F, the Concall Verdict, and the Section C combined verdict. Step 8D is marked deferred to /fttcp and Role 1 (OR-30), with pillar-relevant facts flagged.
5. Step 8.5: rows 1-31 graded against the call (3 ANSWERED, 8 PARTLY, 20 NOT ADDRESSED) in a new "Call status" column with line cites. Concall finding IDs added to rows 1, 2, 6, 7, 25, 29, 30 (body and YAML). New rows 32-47 cover every concall FORWARD-SIGNAL (FN-02, FN-03, FN-05, FN-06, FN-08, FN-09, FN-10, FN-11, FN-12, FN-13) and AMBIGUOUS finding (FN-01, FN-04, FN-07, FN-14, FN-17, FN-18, FN-20, FN-21), plus FN-16. Channel line, top-3 and channel recommendation updated.
6. Step 9: Key Notes one-liner rewritten for results plus call. Promoter Verdict and Management Grade lines added. Promise-log save added.
7. MONITORABLES: item 1 marked DONE. Thirteen concall rows added (C02, C04, C05, C06, C07, C09, C11, C12, C13, C19, C20, C21 and the Q3 call re-grade). Rows for Q3 results, tonnage, entity AUM (now C03, 20-25%) and credit cost (now C01) updated with call cites. The gold AUM price-flat row, already in the YAML, added to the body. The body list is renumbered 1-35; the YAML carries 33 rows (the body's Stree Sakthi and F13 rows stay body-only, as before).
8. VERDICT AND FLAGS: verdict unchanged (PROCEED WITH FLAGS). CONCALL-NOT-IN-RUN replaced by CONCALL-ASR-SOURCE. Added flags: GUIDANCE-RECORD-MISMATCH, GUIDANCE-CONSISTENCY, GOLD-AUM-GUIDE-NOT-RESTATED, DA-RELIANCE-CONTRADICTION, NIM-PRESSURE-SIGNALLED, INSURANCE-INCOME-RISK, DECLINED-GUIDANCE, SPOKEN-VS-FILED-DRIFT, STAGE2-NO-PEAK, LTV-CREEP, REPEATED-EVASION-2Q, FTTCP-T3-NEGATIVE-DIAGNOSTIC, CREDIBILITY-ND, PEER-CROSSCHECK-UNVERIFIABLE. Existing flags aligned to the call: PILLAR2L-SELFWITHDRAW-CONDITION, PCR-EROSION, COVERAGE-RELEASE-PAT, STAGE2-SURGE, GOLD-GROWTH-QUALITY, GOLD-TRIGGER-AT-RISK, OFFBOOK-DEPENDENCE, SELLDOWN-DA-GAP, DA-DRAG, EPS-MISPRINT, DISCLOSURE-SILENCE, GROWTH-TRIGGERS-LAGGING, PIPELINE, DEFERRED-OR30. Flags renumbered 1-32.
9. PLAIN-LANGUAGE BRIEF: all five parts rewritten to include what management said. Provenance labels are now FILED / MGMT-CALL / MGMT-DECK / INFERENCE. The forward map drops the done transcript item and adds the Q3 ST LAP, tonnage, sell-down and Q3-call forks.
10. Dependency alignment: Role 4 Step 1L-b heading, row 3 and pattern line point to Role 5 Step 3E. A pointer to Role 5 Step 3A added under 1L-c. Role 5 notes added in the Step 4 memo, the Step 5L sell-down paragraph, cash quality, the concentration answer and the S-vs-C line. The collection-efficiency cell in the derived-metrics table notes the call gave no number. Step 6B row 1, Step 6D checkpoint and Step 8 8A-W point to Role 5. The Step 0B units line adds the concall. Role 4 figures, verdict and Decision Status are unchanged.
11. YAML: docs_merged adds concall; turns 74; concall findings added; 47 questions with call status; 33 monitorables; flags aligned; analyst_note rewritten (open item F5 fixed). The same block is written to work/blocks/a4.yaml.

## ROLE 5 LOOP 1 CHANGES (2026-10-19; A5 audit work/audit_concall_fedfina_q2fy27.md and A2 ledger loop 1; change log, not narrative)

1. Counts (F6, M7-M9): the concall ledger line in the preamble now reads 26 questions (9 primary, 14 follow-up, 3 embedded in T47, T50, T51), 9 MIXED_TURN (adds T47, T50, T51, T54), 141 management numbers on A1 rows and 145 with MFS-C1 to C4, 8 analyst numbers, 58 forward phrases, 22 qualifiers, 14 dates, and 21 MFS rows read. Aligned at 0C (26 questions), 4A heading (26; ledger Q24-Q26 folded into Q14 and Q15, 23 table rows kept), the Step 9 save header and flag 30 (9 mixed turns). The Role 5 merge change log keeps its original counts as a record.
2. MFS units used where the review relies on them: MFS-C11 (Call L56) at Step 1 row 2, 7A DA-reliance row, flag 9, Q40 and monitorable 19; MFS-C1/C12 (Call L57) at row 3 and 6B; MFS-C2 (Call L113, 15% interim ROE) at new Step 1 row 58, 2L RoA/RoE row, 8D Pillar 1 and Q36; MFS-C3/C4 (Call L482-L483 LTV slab caps) at Q06, Q41 and flag 5; MFS-C21 (Call L715-L716) at Q10 and 5A. A3 re-run judged unnecessary: the new units support FN-05, FN-09 and the breakeven qualifier and raise no new finding.
3. M15: Step 1 adds rows 56 (Call L106-L107), 57 (Call L110-L112) and 58 (Call L113, quantified). Quantified share is 39 of 58 (67%). S20: forward claims are now the Forward Guidance and Forward Soft rows only, 2 of 7 (29%); Macro/Tailwind rows are excluded.
4. 6B: forward base is 58 (49 A1 + 9 MFS). Quantified 17-18; ratio 0.29-0.31, on the 0.3 hedge-heavy line. 6E, the Concall Verdict, flag 18 and the YAML CONCALL-VERDICT flag carry 0.29-0.31. The archetype stays ND (bottom row unchanged).
5. F7: 7A core-yield row is PARTIALLY CONFIRMED (the +29 bp optical rise and its DA cause tie under XC; the 16.40 level does not; ex-DA core about 16.7% both quarters). Tally 22 CONFIRMED / 4 PARTIALLY CONFIRMED in 7A and Section C. FN-07 keeps a level leg (extraction note). Flag 15 and its YAML line add the fourth drift (core yield 16.40 vs about 16.7%). Q38 and its YAML question note the level gap.
6. F8: Exchange 3 "Not said" now names the levers (opex and credit cost, Call L567, L689-L695, unsized) and cites the 150 branches at Call L187-L189. The 2L NIM row, Q37, Q14, 8D Pillar 1 and flag 12 name the same levers.
7. C4: Step 2L diagnostic adds reading (c), the gold guide reaffirmed without a number (Call L248-L249, L292-L293). Qualified the same way: Step 1 dropped-claims line, 2L gold AUM row and widen/tighten line, 3A, 3C, 3E row 3, 6A, 8A, 8D growth row, Section C, Q7, Q35, monitorable 10, flag 6, the brief sector part, and the YAML (Q7, Q35, monitorable, flag, analyst_note). The DROPPED candidate stays open; row 35 still separates the readings.
8. C5: the 4A grade line now reads "C-graded answers (Q02, Q04) and the B-graded Q10". Grades unchanged (A 2, B 15, C 6).
9. C6: the brief summary names both open operator rulings (Pillar 2L baseline; credit-cost tripwire basis). Monitorable 35 and its YAML row name both; flag 21 says the ruling is open.
10. M10: both parses of the branch split (Call L539-L541) stated at Q9, 2L branch row, 4A Q09, monitorable 7 and the YAML (Q9, monitorable). Separating observation: Q3 FY27 additions, about 75 vs about 100.
11. M11: the Rs 289 Cr ST LAP bar is qualified as the highest of six known quarters, FY25 quarters not in the run, at Q42, 8F row 12, monitorable 4 (source now Deck R475-R479), the brief forward map and the YAML (Q42, monitorable).
12. M12: the spread counter (the +20 bp reported rise is the DA reversal; ex-DA spread narrowed about 13-20 bps; core NII / ATA held at 8.8%) is grafted at Exchange 3, 8D FTTCP row, flag 12 and its YAML line, the brief sector part and the analyst_note. Role 4 body lines that state the reported spread are unchanged.
13. M13: the breakeven qualifier (tied to a rising or current gold price; FY26 cohort grew with gold value per gram up about 38% YoY; untested at a flat price) is grafted at 5A, Q10 and its YAML question, 4A Q15 and the brief business-model part.
14. M14: the holder-analyst qualifier is grafted at 4B buy-side and hosting-broker lines.
15. Style: S15 (0D two sentences), S16 (Q&A about 52.1 minutes, 76%, closing remarks excluded; 0C and Step 9 header), S17 (4B C-graded topics add Q08 and Q20), S18 (brief: the CEO dated the change to April), S19 (brief: "the provision charge fell"), S20 (item 3), S21 (2L refusal list: Yash at T51, Call L743-L746), S22 (5B peers invoked three times, adds Call L255-L258). S13 and S23 not applied (not one-line A4 edits in scope).
16. Header and inputs line note the Role 5 loop 1 revision and the A5 concall audit. The verdict line states that loop 1 changes no verdict, tripwire or Decision Status. Protocol verdict (PROCEED WITH FLAGS), tripwires, Pillar 2L condition and Decision Status (WATCHLIST / AVOID, DEEP WATCH) are unchanged; my re-read found no reason to change them.
17. YAML: rewritten in the review and written first to work/blocks/a4.yaml (same content).

## ROLE 5 LOOP 2 CHANGES (2026-10-19; A5 concall re-audit work/blocks/a5-concall.yaml, finding C7; change log, not narrative)

1. C7, Step 8.5 Q41 (Why it matters cell): "90-95% of customers take the maximum, set by exposure slab caps of 75% and 80% (Call L480-L483, MFS-C3, MFS-C4), so most new loans sit at their slab cap" is replaced with A5's text verbatim: Jagdish wants-the-maximum line (Call L480-L483, MFS-C3, MFS-C4); CEO minus-two-percent, 72-74% working mix, "not everybody at that highest one" (Call L497-L506); filed average origination LTV 72.1% below both caps (Deck R327); share of new loans at the cap ND, which the row asks for. Verified before writing at Call L480-L483, Call L497-L506 and Deck R327 (presentation structured row, 72.1%). The cell now agrees with 7A ("working mix agrees with 72.1%") and 6D (LTV headroom).
2. Flag 5 body and its YAML flag line: "90-95% of customers take the maximum at the 75% or 80% exposure slab cap" is replaced with A5's text: slab maximum wanted (Jagdish, Call L480-L483); CEO working mix 72-74%, not everybody at that highest one (Call L500-L502); filed origination LTV 72.1% (Deck R327).
3. YAML Q41 parenthetical aligned the same way (Jagdish wants the slab maximum; CEO working mix 72-74%; filed origination LTV 72.1%; share at the cap ND).
4. Style: S24, Step 1 diagnostic, "(Call L736; row 36)" now reads "(Call L736; Step 8.5 row 36)". S26, Q37: "other levers" now quotes the transcript verbatim with the gloss, "some other operating labor" [ASR: lever] (Call L661-662). S27, 4A Q14: the ASR line "a family object for our credit card" (Call L689-L690) now carries an [ASR] tag, read as opex or credit cost, with the lever naming resting also on Call L567. Each was a one-line edit.
5. Alignment: header revision line and the verdict line note loop 2. YAML adds role5_loop_2: "C7 applied"; analyst_note opens with loops 1 and 2 and the Q41 correction. The same block was written first to work/blocks/a4.yaml.
6. Not applied: S25 (A2 ledger items, not A4). Carried open: S13, S23, S7-S10, S12. No number, flag, protocol verdict, tripwire or Decision Status changes; LTV-CREEP stands on the 72-74% working mix and 72.1% origination LTV against the 68.0% book.
