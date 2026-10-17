# A4 MERGED REVIEW: Fedbank Financial Services Ltd (FEDFINA), Q2 FY27 (quarter ended 30 Sep 2026)

Agent: A4 analyst | model: claude-opus-5-5 | run date: 2026-10-17 | revision: correction loop 1 (A5 audit work/audit_fedfina_q2fy27.md, verdict INCOMPLETE)
Run type: FULL QUARTER, Role 4 (Quarterly Results Review Protocol v1.4) only. No concall in this run, so Role 5 was not loaded.
Lender variant: Steps 1L and 5L replace Steps 1 and 5. Step 7 uses the lender rows. Role 4 Steps 6.5 and 7 are deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts are flagged in Section 7.
Docs merged: results filing (Reg 33/52, 15 pages), investor presentation (42 slides), press release (3 pages).
Inputs read: A1 structured files (all rows), A1 fulltexts at cited lines only, A2 ledgers (all three), A3 forensics (all three), orchestrator extraction check (work/orch-check/extraction-check.md), Notion live copy (work/notion-thesis.md), A5 audit (loop 1). The source PDFs and inputs/ were not opened.

Anchor convention: "Res R###" = results structured row (line Lnnn in results fulltext); "Deck R###" = presentation row; "PR R###" = press-release row; "XC" = orchestrator extraction check. "derived" = A4 arithmetic on filed numbers; it is never an estimate.

---

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 38 notes / 0 turns / 45 slides. All 38 notes / 0 turns / 45 slides reviewed.
- Results ledger: 748 of 748 IDs, plus 4 rows A2 adds in loop 1 (752 rows). 36 notes and footnotes, 339 line-item groups plus 2 NOT DISCLOSED blank rows, 38 ZERO_STANDING rows, 6 agenda items, 19 auditor paragraphs, 38 entities, 7 signature blocks (was 5). MFS-1/2/3 noted (agenda enclosure prose, garbled UDINs). gate_a2 pass.
  - Loop 1 additions, each read at its fulltext line: Res L525 "Aggregate principal outstanding of loans transferred" (blank cell, NOT DISCLOSED); Res L526 "Weighted average residual tenor of the loans transferred" (blank cell, NOT DISCLOSED); Res L812 Annexure I company signature block; Res L932 (mark L934) Annexure II company signature block. Content already covered at Note 10(I) and Q13. No new finding.
- Presentation ledger: 1,102 of 1,102 IDs, 42 slides (5 text-only dividers), 37 footnotes, 1 ZERO_STANDING row (R1024). gate_a2 pass.
- Press-release ledger: 247 of 247 IDs, 3 pages, 2 notes/qualifier footnotes, 0 ZERO_STANDING. gate_a2 pass.
- Unreviewed rows: none.

Findings incorporated:
- Results (17): A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17.
- Presentation (25): FN01 to FN25.
- Press release (13): FND-01 to FND-13.

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
Results filing: INR Lakhs (Res R693, L208), except Annexure I security cover in INR crore (Res R739, L818). Converted to Rs Crore at x0.01. Presentation and press release: Rs Cr as printed (Deck R097; PR fulltext L79).

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
| Collection Efficiency % | As disclosed | ND | ND | ND (not disclosed in any of the three documents) |
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

### 1L-b. Prior-quarter Questions for Management: answer status (no concall in this run; graded against the three filings)

| # | Q1 FY27 question (Notion) | Status | Evidence this quarter |
|---|---|---|---|
| 1 | Branches opened in Q2; H1 count vs 200 target | PARTIALLY ANSWERED | 74 new branches, 831 total (Deck R033-R034). H1 = 74 vs 200. Target not restated. |
| 2 | Absolute gold tonnage Q1 and Q4 FY26; split of 25-30% guide | PARTIALLY ANSWERED | Tonnage 12.6 t Q4 FY26, 12.7 t Q1, 12.9 t Q2 (Deck R489-R491). No tonnage/LTV/price split. |
| 3 | Does the full FY27 stack hold; weakest leg | NOT ADDRESSED | No guidance in deck or release (FN02, FND-13). Concall transcript not in run. |
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

Pattern: 0 of 13 fully answered, 8 partial (rows 1, 2, 5, 6, 7, 8, 10, AR-1), 5 not addressed (rows 3, 4, 9, AR-2, AR-3). The concall transcript may change this. This counts toward DISCLOSURE-SILENCE, not yet a governance finding.

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

Sell-down reconciliation (C1): the deck shows a Rs 1,085 Cr Q2 sell-down (Deck R680). The filing shows Rs 876.89 Cr of loans transferred by assignment (Res R472). The Rs 208.11 Cr difference is UNRECONCILED. No document states its route. The deck funding legend lists both "Direct Assignments" and "CLM" (co-lending) as sources (Deck R587-R593; slice sizes unresolved). Co-lending is therefore one candidate route, NOT DISCLOSED in size. Question Q4 and row 31 carry this.

Cash quality (lender reading): H1 FY27 operating cash flow was -Rs 718.88 Cr (Res R306), driven by a loan-book build of Rs 1,843.15 Cr (Res R290). Operating cash flow before the loan build was +Rs 1,124.27 Cr (derived: -718.88 + 1,843.15). Cash fell 42% from Rs 1,339.73 Cr to Rs 773.68 Cr (Res R190, R189). CFO/PAT is not a meaningful lender metric. The lender cash-quality test (collection efficiency, write-offs) is NOT DISCLOSED. Classification: **INDETERMINATE-WITH-DIRECTION** (direction: growth-induced). This caps the verdict at PROCEED WITH CAVEATS or below. Missing evidence: collection efficiency and H1 write-offs.

Mandatory lender questions:
- Asset-Quality Multiplier band: level evidence (GNPA 1.82%, NNPA 1.18%, credit cost 0.6%) fits Sound 1.00x. Direction evidence points toward Stressed 0.80x: Stage 2 +34.6% with coverage -392 bps; stressed coverage 24.5% to 20.2%; PCR -299 bps; GNPA +27 bps. The Pillar 2L self-withdrawal clause condition "PCR thins further" reads as MET on a QoQ baseline (38.36% to 35.37%). It is NOT MET against the FY26 baseline (32.29%). The clause names no baseline. Recompute deferred (OR-30); operator ruling needed. Flag PILLAR2L-SELFWITHDRAW-CONDITION.
- Credit cost within guided band: yes (0.6% Q2, 0.69% H1 vs below 1%). Logged ON TRACK in the promise tracker.
- Concentration: the QoQ Stage 3 rise is product-concentrated (gold), not state-concentrated on the evidence. Gold GS3 moved from about Rs 9 Cr (0.1% of 9,473, rounded) to Rs 47.6 Cr; total GS3 rose Rs 44 Cr (252 to 296, Deck R780-R781). YoY, gold GS3 is up only 10 bps (0.4% to 0.5%, Deck R737, R739). Mortgage GS3 % was flat. Top-5 state share fell to 74.5% (Deck R385). North mortgage share rose to 32% (Deck R548) on an unseasoned book (FN12). The deck attributes the move to "gold loan industry changes" (Deck R722) without naming them. A product-specific cause has a normalisation path; it is not yet evidenced.
- AUM growth vs collection infrastructure: disbursals fell 1.2% QoQ while branches rose 9.8% and staff 10.1% (Deck R053, R075, R078). AUM growth in Q2 came mainly off-book. Collection efficiency is ND, so the classic pre-stress test cannot be run. Gold portfolio LTV rose from 59.3% (Q3 FY26) to 68.0% (Deck R498, R501): the collateral cushion is thinner.

Capital (A3-04, FN16, FND-07): D/E 4.61x against the 6x cap on the newest secured NCD (Res R543-R544): headroom 1.39x of net worth, about Rs 4,399 Cr of further debt at constant net worth (A3 derived). D/E was also 4.61x at Mar-26 (Res R390), so H1 net de-leverage is nil; the Q2 fall reversed Q1's rise to 4.89x. Average leverage rose from 5.9x to 6.0x in Q2 (Deck R1063, R1064). CRAR 20.96% vs 15% floor. About half the RoE rise from 12.0% to 17.0% came from leverage (avg TA / avg SF 5.0x to 6.0x, Deck R1062, R1064). Net worth grew 16.8% YoY vs borrowings 42.7% (Deck R058, R068). Growth at the H1 pace needs more assignment, co-lending or equity.

Standalone vs consolidated (A3 F2): standalone only; no subsidiary, associate or JV (Note 6, Res R702, L432). S-vs-C PAT gap 0.0% in Q2 FY26, Q1 FY27, Q2 FY27, H1 FY26, H1 FY27 and FY26. The consolidated column is ND because no consolidated statement exists.

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
| 1 | Credit cost <= 1.1% of avg assets, FY27 guidance issued | <= 1.1%; guidance issued | > 1.1% | 0.6% Q2 (Deck R1048); 0.69% H1 derived; guidance not in deck or release (FN02) | AMBER (level GREEN; guidance UNKNOWN; coverage caveat FN09) |
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

Checkpoint: 6A-6D presented.

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
- Output: entry zone unchanged pending Role 1 (flag ENTRY-ZONE-BELOW-BOOK). Gate: Q3 FY27 results (expected mid-January 2027 [INFERENCE from the 15-Jul and 15-Oct board cadence, Res R662, R657]). Proposed Decision Status: **no change** (WATCHLIST / AVOID, DEEP WATCH). The operator sets status.
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

Channel: an earnings call was held for Q2 FY27. The deck cover letter says the presentation "is referred during the Earnings call" (Deck fulltext L30-35, R006). The transcript is not in this run. Action: check the transcript when filed. Send every row it does not answer by IR email.

### Ranked questions (Q1 most material)

| # | Question | Why it matters | Bull answer | Bear answer | Cat. | Finding IDs |
|---|---|---|---|---|---|---|
| 1 | Stage 2 assets rose 34.6% QoQ to Rs 587 Cr while Stage 2 coverage fell from 16.53% to 12.61%. What share of Q2 Stage 2 is gold loans? | Separates mix shift from provision release. New stressed assets of Rs 195 Cr got Rs 10.0 Cr (5.1%); stressed coverage fell 24.5% to 20.2%; Stage 1 took Rs 12.0 Cr of the Rs 21.8 Cr build. | 75% or more gold, LTV at or below 75% | Mortgage Stage 2 rose, or mortgage coverage was cut | D | A3-11, FN09, FN10, FND-05 |
| 2 | What were gold auction losses in Q2 FY27, in Rs Cr? | Tests the low-LGD reading of gold Stage 3 (Rs 47.6 Cr, PCR 10.5%) | Below Rs 1 Cr | Above Rs 5 Cr, or not tracked | D | FN11 |
| 3 | Which "gold loan industry change" on slide 29 lifted gold Stage 3 from 0.1% to 0.5%? | A named, technical cause has a normalisation path; an unnamed one does not | A named rule change with a dated end to its effect | No specific cause given | D | FN03 |
| 4 | Of the Rs 1,085 Cr Q2 sell-down (Rs 876.89 Cr filed as direct assignment; Rs 208 Cr unreconciled), what share went to Federal Bank? | Growth now rides loan buyers; a promoter buyer is a related-party dependency | Below 25%, several unrelated banks | Above 50% to Federal Bank | E | FN07, A3-12 |
| 5 | What was the gross gain on pools assigned in Q2 FY27, before the reversal on older pools? | Net DA was -Rs 12.9 Cr and -Rs 1.2 Cr while sell-down doubled; tests whether off-book growth is bought at a loss | Positive gross gain; loss is EIS unwind timing | Gross gain near zero or negative | C | FN08, FND-06, A3-09 |
| 6 | At what CRAR level will the board raise equity? | D/E 4.61x vs 6x cap, unchanged from Mar-26; CRAR 22.40% to 20.96% in H1; half the RoE gain is leverage | Not before CRAR 18%; accruals plus assignment fund FY27-FY28 | Raise within 12 months | F | A3-04, FN16, FND-07 |
| 7 | Which of the five FY27 guidance items from the Q1 call do you now revise: entity AUM +20-22%, gold AUM +25-30%, tonnage +10-12%, 200 branches, credit cost below 1%? | No guidance in deck or release; 3 of 5 run behind (entity AUM, tonnage, branches) and gold AUM is at risk on a price-flat basis | None revised | Tonnage or branch target cut | B | FN02, FND-13 |
| 8 | Will the company refile Q2 FY27 basic EPS? Printed 3.56; H1 6.54 less Q1 3.05 gives 3.49. | Filed EPS error appears twice; tests reporting control | Yes, corrected filing with date | No, or no answer | G | A3-10 |

### Extended rows (every remaining FORWARD-SIGNAL or AMBIGUOUS finding)

| # | Question | Why it matters | Bull answer | Bear answer | Cat. | Finding IDs |
|---|---|---|---|---|---|---|
| 9 | How many of the 126 remaining FY27 branches will open by 31-Mar-2027? | 74 of 200 opened in H1; opex +7.8% QoQ | 120 or more | Below 80 | B | FN15, FND-08 |
| 10 | What 12-month AUM per branch do you target for the 74 Q2 branches, in Rs Cr? | Gold AUM per branch fell 17.7 to 16.9; C/I fell only 36 bps | Rs 10 Cr or more | No target | A | FN15, FND-08 |
| 11 | What drove the Q2 ETR of 26.54% vs 25.17% statutory? | About Rs 2 Cr of PAT; current tax 29.53% of PBT | A named one-off | Recurring disallowance | D | A3-05, FN04, FND-01 |
| 12 | What is the outstanding FCY/ECB borrowing at 30-Sep-2026, in Rs Cr? | Q2 hedge OCI gain Rs 43.48 Cr exceeds FY26 full year Rs 31.82 Cr; explains Rs 26.62 Cr of non-PAT equity growth | Small, fully hedged to maturity | Large, partial hedge | F | A3-08, FN05, FND-04 |
| 13 | What principal outstanding did the 48 accounts sold to ARCs carry, in Rs Cr? | NBV nil, consideration Rs 0.03 Cr, principal row (L525) blank | Small, fully written off earlier | Large write-off pool | D | A3-02 |
| 14 | What were total H1 FY27 write-offs, in Rs Cr? | Credit cost read is incomplete without write-offs | Below Rs 10 Cr | Above Rs 25 Cr | D | A3-02, FN09 |
| 15 | What makes up other financial liabilities of Rs 468.19 Cr at Sep-26 (Rs 216.38 Cr at Mar-26)? | +116% in H1; collections payable to assignees vs other build-up | Assignee collections payable | Margin money or unexplained payables | D | A3-12 |
| 16 | Who appointed V. Sankar Aiyar & Co. as joint statutory auditor, on what date, and under which rule? | First joint review this quarter; no board agenda item | AGM 29-Sep-2026 resolution under the RBI joint-audit rule | Mid-year appointment with no stated trigger | G | A3-03 |
| 17 | Does the trust deed define "total outstanding liability" as borrowings only? | Filed TOL/ATNW 4.61x is on 31-Mar-2026 audited figures (Res R743-R744) and equals Mar-26 D/E 4.61x; computed TOL/ATNW on the same Mar-26 figures is 4.79x | Yes, borrowings only | No; filed figure understated | G | A3-15 |
| 18 | How did the Federal Bank derivative margin deposit reach a Rs 16.16 Cr closing balance with nil opening and nil flow? | RPT table does not reconcile (OCR-garbled page) | Table error, corrected flow given | No answer | G | A3-16 |
| 19 | What is the Rs 1.85 Cr H1 brand-usage fee to Federal Bank based on, and from what date? | New related-party charge to promoter | Fixed fee at or below market, board-approved | Revenue-linked fee rising with AUM | G | A3-16 |
| 20 | What is Gross Stage 3 % for North-originated mortgages of FY25-FY26 vintage? | North mortgage share 6% (FY21) to 32%; unseasoned | Below the 3.4% book average | Above 4% | D | FN12 |
| 21 | What undrawn sanctioned lines did the company hold at 30-Sep-2026, in Rs Cr? | ALM below-3-month cumulative surplus only Rs 186 Cr on Rs 3,291 Cr outflows | Above Rs 1,500 Cr | Below Rs 500 Cr | F | FN17 |
| 22 | Is the Q2 FY26 column on the ECL slide on the same basis as Q1 and Q2 FY27? | Only that column carries the * and ^ markers; YoY PCR move may not be like-for-like | Yes, same basis | No; YoY coverage restated | D | FN20 |
| 23 | How many NAPS apprentices were on the rolls at 30-Sep-2026? | Headcount 5,920 excludes apprentices; productivity overstated | Fewer than 200 | More than 1,000 | G | FN21 |
| 24 | What were FY26 yield, CoB and spread on the old two-point basis? | Annual series restated this quarter; old decks not comparable | Change below 10 bps | Change above 25 bps, favourable to the new series | C | FN24 |
| 25 | Which CoB series does management steer on: slide 25 Ind-AS 7.9% or the daily I-GAAP 7.79%? | Two series on mixed bases; earlier read showed a gap (FN25 now dissolved by the XC correction) | One named series, reconciled | No answer | C | FN25, FN22 |
| 26 | Is the H1 FY27 Shareholder's Fund cell of Rs 2,926.1 Cr in the press release the 31-Mar-2026 opening balance? | Two net-worth values for one date (7.5% gap); 2,926.1 equals FY26 SF (Deck R169) | Yes, opening balance; label fixed | Unexplained | G | FND-03 |
| 27 | Why did other income fall 1.9% YoY to Rs 27.78 Cr while AUM grew 36.6%? | Fee and cross-sell yield on the book is shrinking | Treasury-only decline; fees up | Fee income lost | C | FND-09 |
| 28 | Is the 0.6% credit cost computed on two-point or daily average total assets? | Tripwire basis; Notion mixes AUM and asset bases | Two-point average, same as tripwire | Undefined | D | FND-12 |
| 29 | Publish gold 30+ and 60+ DPD for Q2 FY27 (carried from Q1 Q4, not addressed). | Early-warning for gold Stage 2/3 | Disclosed, stable | Refused again | D | carried; A3-11 |
| 30 | Give the bridge for the Stage 3 ECL move from Rs 96.8 Cr to Rs 104.7 Cr (carried from Q1 Q9). | Second quarter without a provision bridge | Bridge given | Not addressed again (governance signal) | D | carried; FN09 |
| 31 | Through which route did the Rs 208 Cr of the Q2 sell-down not filed as direct assignment leave the book: co-lending, securitisation, or other? | Deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr; CLM is a listed funding source of unresolved size | Co-lending with a named bank partner, disclosed | No reconciliation given | E | FN07, A3-12, FND-07 |

Top 3 by likelihood of thesis-changing information:
- Bull probability: Q1 (Stage 2 gold share). A high gold share supports the mix reading and the 1.00x Pillar 2L.
- Bear confirmation: Q5 (gross DA gain). A near-zero gross gain means off-book growth is bought, and Q2 profit quality is weaker.
- Transparency test: Q8 (EPS refiling). A clear yes or no on a filed error.

Channel recommendation: Concall already held; transcript not in run. Read the transcript first. Then send an IR email with every unanswered row verbatim. Rows 1-6 are the priority.

---

## STEP 9 NOTION UPDATE (payload only; this stage writes nothing)

- Decision Status: not written. Proposed: no change.
- Key Notes prepend (proposed): "2026-10-17 | Q2 FY27: PAT Rs 130.75 Cr (+63.1% YoY), ROE 17.0%; PCR 38.36% to 35.37%, stressed coverage 24.5% to 20.2%; no tripwire fired; Pillar 2L self-withdraw condition met QoQ, operator to rule; growth off-book-led and gold-price-led."
- Properties to refresh at the write gate: CMP (stale 164); gold mix (page says ~46.5%; Q2 54.1%, Deck R315); secured share (page 98.9%; Q2 99.4%, Deck R064).
- Sections to append: all tables above in full.

---

## MONITORABLES / CATALYST LIST (seeded by A3 F6 registers and F13)

| # | Item | Implied date | Source |
|---|---|---|---|
| 1 | Q2 FY27 earnings-call transcript filed; grade prior and new questions | about 2026-10-22 [INFERENCE: Reg 46 window after the mid-October call] | Deck R006, fulltext L30-35 |
| 2 | Results published in Business Standard and Pratahkal | about 2026-10-17 | Res R649, L61 |
| 3 | Q3 FY27 results: credit cost, PCR, Stage 2, stressed coverage, gold Stage 3, DA line | mid-January 2027 [INFERENCE from 15-Jul and 15-Oct cadence] | Res R662, R657 |
| 4 | Remaining 126 of 200 FY27 branches | by 2027-03-31 | Deck R033; Notion promise log |
| 5 | Gold tonnage +10-12% FY27 (13.86-14.11 t derived) | by 2027-03-31 | Deck R491; Notion |
| 6 | Entity AUM +20-22% FY27 (Rs 24,184-24,587 Cr derived) | by 2027-03-31 | Deck R423; Notion |
| 7 | Credit cost below 1% FY27 | by 2027-03-31 | Notion promise log |
| 8 | CRAR at or above 16% (07041, 07058) and 15% (07066) | at all times; next audited test 2027-03-31 | Res R654-R655, Annexure II |
| 9 | D/E within 6x (07066, tested on 30-Sep-2026 figures, Res R745); TOL/ATNW at or below 7.0 (07041, 07058; filed 4.61x is on 31-Mar-2026 audited figures, Res R743-R744) | tenor; next TOL/ATNW test on 31-Mar-2027 audited figures | Res R653, R543-R544, R743-R745 |
| 10 | GNPA at or below 4-5%, NNPA at or below 3-4% | tenor; half-yearly | Res R523-R542 |
| 11 | Security cover at or above 1.10x on Rs 278.75 Cr secured NCDs | ongoing; next certificate with Q4 FY27 | Res R367-R368, R519-R520 |
| 12 | Management certification of other NCD covenants | each half-year; next 2027-03-31 | Res R652 |
| 13 | FY27 audited results and annual credit cost | late April 2027 [INFERENCE from FY26 audit report 2026-04-28] | Res R664 |
| 14 | Q1 FY28 results | mid-July 2027 [INFERENCE] | Res R662 |
| 15 | FY27 Annual Report and AGM (actuarial assumption, FVOCI detail, joint-auditor tenure) | about late September 2027 [INFERENCE from 2026 AGM 29-Sep] | Notion AGM record; A3-03, A3-07 |
| 16 | ESG KPI evaluation metrics ("being developed") | undated | Deck R1091 |
| 17 | Nation Skill Building CSR apprentice programme | undated; first in this deck | Deck R1099 |
| 18 | Digital ecosystem build | undated aspiration | Deck R1081 |
| 19 | Stree Sakthi gold scheme crossed Rs 100 Cr | completed (launched 2026-01-07) | Deck R1095-R1096 |
| 20 | Board outcome forward items (F13) | none beyond results approval and publication | Res R728, R649 |

---

## VERDICT AND FLAGS

Protocol verdict: **PROCEED WITH FLAGS**. Cash conversion INDETERMINATE-WITH-DIRECTION (growth-induced) caps at PROCEED WITH CAVEATS or below. Flags below propagate. No mechanical failure. Extraction defects were resolved by the orchestrator check.

Flags:
1. PILLAR2L-SELFWITHDRAW-CONDITION: PCR thinned QoQ 38.36% to 35.37%; clause condition met on QoQ baseline, not on FY26 baseline. Operator ruling.
2. PCR-EROSION: checklist item 2 AMBER; red line 32% holds.
3. COVERAGE-RELEASE-PAT [INFERENCE]: at Q1 stage coverage, about Rs 19.3 Cr more ECL; about 88% of the QoQ PAT gain; credit cost about 1.0%. Stage 1 took Rs 12.0 Cr of the Rs 21.8 Cr ECL build; new stressed assets of Rs 195 Cr got Rs 10.0 Cr (5.1%); stressed coverage 24.5% to 20.2%. Reading B (release) stays live.
4. STAGE2-SURGE: Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%.
5. GOLD-GROWTH-QUALITY: tonnage +1.6% QoQ vs gold AUM +6.5%; portfolio LTV 68.0%; gold Stage 3 0.1% to 0.5% QoQ (0.4% a year ago, +10 bps YoY).
6. GOLD-TRIGGER-AT-RISK: gold AUM +25-30% (price flat) is reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t), against +2.4% in H1; price-flat pace about +19% to +26%; Q2 growth about 70% price.
7. OFFBOOK-DEPENDENCE: AUF +Rs 27 Cr vs AUM +Rs 899 Cr; gold AUF -Rs 52 Cr; buyer identity ND.
8. SELLDOWN-DA-GAP: deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr; Rs 208 Cr unreconciled; route NOT DISCLOSED.
9. DA-DRAG: net DA loss two quarters running.
10. LEVERAGE-LED-ROE and CAPITAL-COMPRESSION: leverage 5.0x to 6.0x; CRAR -144 bps in H1; D/E 4.61x vs 6x cap; H1 net de-leverage nil (Mar-26 and Sep-26 both 4.61x).
11. EPS-MISPRINT: Q2 basic EPS 3.56 printed vs 3.49 derived.
12. CREDITCOST-BASIS: Notion records mix AUM and average-asset bases.
13. NOTION-STALE: CMP, gold mix, secured share; PRIOR-FVOCI-UNIT ("~585cr" vs Rs 58.51 Cr filed).
14. CASHCONV-INDETERMINATE-WITH-DIRECTION: collection efficiency and write-offs ND.
15. DISCLOSURE-SILENCE: guidance, collection efficiency, write-offs, Tier I, DPD buckets; 0 of 13 prior questions fully answered (8 partial, 5 not addressed).
16. GROWTH-TRIGGERS-LAGGING: entity AUM, branches, tonnage, de-leverage DELAYED; mortgage and co-lending WEAKENED; gold AUM AT RISK.
17. TRACKER-ROWS-ND: 0 signals supplied; reopen Role 5.5.
18. ENTRY-ZONE-BELOW-BOOK: zone max Rs 77 < BVPS Rs 84.4 (Role 1).
19. PROJECTIONS-ND: no bear/base/bull P&L on Notion; 6A and 8A-W landing not assessable.
20. CONCALL-NOT-IN-RUN: call held; transcript absent.
21. PIPELINE A1-EXTRACTION-DEFECTS: OCI sign misreads (R101, R134-R137, R158-R160), slide 22 and slide 25 attribution; resolved via XC. A2 adds four results rows (L525, L526, L812, L932) in loop 1.

---

## PLAIN-LANGUAGE BRIEF

### 1. Summary narrative
Fedfina earned Rs 130.75 Cr after tax in Q2 FY27. That is 63.1% more than a year ago (FILED, this quarter).
Return on equity reached 17.0% and return on assets 2.8% (MGMT, deck).
The loan book under management grew 36.6% to Rs 22,035 Cr (MGMT).
Costs grew slower than income. Cost-to-income fell from 56.9% to 52.5% (FILED, derived).
None of the three thesis-broken tripwires fired. Credit cost was 0.6%, ROE is above 14%, and PCR is above 32%.
Two parts of the quarter need care.
First, bad loans rose while provisions fell. Gross Stage 3 went from 1.55% to 1.82%. PCR fell from 38.36% to 35.37% (FILED).
Stage 2 loans grew 34.6% in one quarter. Rs 195 Cr of new stressed loans got only Rs 10 Cr of new provision, so cover on stressed loans fell from 24.5% to 20.2% (MGMT, derived).
At last quarter's coverage, provisions would be about Rs 19 Cr higher (INFERENCE). That is most of the quarter's profit gain.
Second, the growth went off the balance sheet. Loans under management rose Rs 899 Cr, but loans on the books rose only Rs 27 Cr (MGMT).
The deck shows Rs 1,085 Cr of loans sold in the quarter. The filing shows Rs 876.89 Cr of that as assignment. The route for the other Rs 208 Cr is not disclosed (FILED, MGMT).
About half of the ROE rise comes from more debt per rupee of equity (MGMT). Debt to equity is 4.61x, the same as in March (FILED).
The printed Q2 basic EPS of Rs 3.56 is wrong. The half-year figure gives Rs 3.49 (FILED, derived).
The decision does not change: WATCHLIST / AVOID, deep watch. The stock sits about 2x above the Rs 68-77 entry zone on a stale price.
The operator must rule on one item: whether the PCR fall triggers the Pillar 2L step-down from 1.00x to 0.80x.

### 2. Sector intelligence
Gold loans are the fastest part of the book. Fedfina's gold book grew 77% in a year (MGMT, this quarter).
Most of that came from a higher gold price and higher loan-to-value, not from more gold. Tonnage rose 16% a year, and only 1.6% in the quarter (MGMT).
In Q2, about 70% of gold-book growth came from the gold price (INFERENCE on MGMT data). At a flat gold price, the FY27 gold guide of +25-30% is reachable only if FY27 tonnage reaches about 14.0 t. That is +11.2% on 12.6 t, against +2.4% in H1 (INFERENCE). The flat-price path gives about +19% at the Q2 tonnage pace and up to about +26% if the tonnage guide is fully met (INFERENCE).
Portfolio LTV rose from 59.3% to 68.0% in three quarters (MGMT). New loans start at 72.1% LTV, so little room is left to grow by lending more per gram (MGMT). A fall in the gold price now hits a thinner cushion (INFERENCE).
The deck blames the rise in gold bad loans on "gold loan industry changes" but does not name them (MGMT). The rule or practice behind it is NOT DISCLOSED.
Funding costs rose a little. Cost of borrowing went from 7.7% to 7.9% on slide 25 and from 7.74% to 7.87% on the P&L basis. The daily measure stayed at about 7.8% (MGMT; FILED, derived; orchestrator image check). The spread still widened from 8.6% to 8.8%.
The credit rating is AA+/Stable from four agencies (AGENCY, as reported in the deck).
Industry demand figures in the deck come from RBI, BIS and Crisil (SECONDARY). They were not used for any thesis number.

### 3. Business-model intelligence
Fedfina lends against gold and against property. Gold is 54.1% of the book, medium-ticket LAP 27.5%, small-ticket LAP and home loans 17.8% (MGMT, this quarter). The Notion page still says about 46.5% gold (prior Notion, stale).
It earns a spread of about 8.8% between loan yield (16.7%) and borrowing cost (7.9%) (MGMT, image check). The spread was 8.7% a year ago, so it is flat.
The model is drifting in three ways this quarter.
One: it now grows by originating loans and selling a part to banks. The off-book share rose from 23.2% to 26.2% (MGMT). Assignment is filed at Rs 876.89 Cr; co-lending is a listed source of unknown size (FILED, MGMT).
Two: mortgage growth is slow. Mortgage AUM grew 13.5% a year, below the 15-20% guide. Small-ticket LAP disbursals fell from Rs 1,475 Cr in FY24 to Rs 904 Cr in FY26 (MGMT, corrected by image check).
Three: all new branches since FY26 are gold branches. Mortgage hubs fell from 129 to 125 (MGMT, A3 resolved).
The parent, Federal Bank, owns 60.6% (MGMT). Its term-loan funding to Fedfina fell from about Rs 1,066 Cr to Rs 905 Cr in the half year (FILED, OCR-garbled page).
Collection efficiency and write-offs are NOT DISCLOSED. The real cash test for a lender cannot be run.

### 4. Competition intelligence
No peer figures were passed to this run. The prior flag PEER-CROSSCHECK-MISSING stands.
The named peers below are context only. Their numbers are NOT FOUND in this run.
In gold loans, the large listed gold lenders (Muthoot Finance, Manappuram Finance) have much larger branch networks (INFERENCE, no figures). Fedfina wins on its parent-bank brand and a AA+ rating, which keep its borrowing cost low (INFERENCE).
In property loans, small-ticket LAP lenders compete on reach and underwriting (INFERENCE). Fedfina's falling small-ticket disbursals suggest it is losing ground in that segment, or chose to pull back (INFERENCE). The filings do not say which.
The competitive risk to watch: if gold prices stall, growth that came from price and LTV stops. The rival with more branches and more grams per branch then holds up better (INFERENCE).

### 5. Forward map (next about 10-11 months)
Make-or-break reading: Q3 FY27 credit cost on average total assets, at the Q3 results in mid-January 2027. Bull at or below 0.8%. Bear at or above 1.0%.
- About 22-Oct-2026, Q2 call transcript. Bull: management names the gold Stage 2 share, the industry change and the route of the Rs 208 Cr. Bear: Stage 2 and the sell-down economics go unanswered again.
- Mid-January 2027, Q3 FY27 results. Bull: credit cost at or below 0.8%, PCR at or above 35.37%, stressed cover stops falling. Bear: credit cost at or above 1.0% as coverage catches up.
- By 31-Mar-2027, 200-branch target. Bull: 126 more branches open with productivity holding. Bear: the target is cut and opex stays ahead of AUM.
- By 31-Mar-2027, gold tonnage +10-12% (13.86-14.11 t). Bull: grams catch up with rupees. Bear: tonnage stays near 12.9-13.3 t and growth stays price-led.
- By 31-Mar-2027, gold AUM +25-30%. Bull: tonnage growth carries it with the price flat. Bear: it is met only if the gold price keeps rising.
- 31-Mar-2027, covenant and CRAR test. Bull: CRAR stays near 21% without new equity and D/E falls below 4.61x. Bear: an equity raise is announced, or CRAR falls toward 18%.
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
docs_merged: [results, presentation, pressrelease]
ledger_reconciliation:
  notes: 38
  turns: 0
  slides: 45
  all_reviewed: true
  a3_findings_incorporated: [A3-01, A3-02, A3-03, A3-04, A3-05, A3-06, A3-07, A3-08, A3-09, A3-10, A3-11, A3-12, A3-13, A3-14, A3-15, A3-16, A3-17, FN01, FN02, FN03, FN04, FN05, FN06, FN07, FN08, FN09, FN10, FN11, FN12, FN13, FN14, FN15, FN16, FN17, FN18, FN19, FN20, FN21, FN22, FN23, FN24, FN25, FND-01, FND-02, FND-03, FND-04, FND-05, FND-06, FND-07, FND-08, FND-09, FND-10, FND-11, FND-12, FND-13]
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
  - {q: "What share of the Rs 587 Cr Q2 Stage 2 book is gold loans (Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%; stressed coverage 24.5% to 20.2%)?", from_finding_id: "A3-11, FN09, FN10, FND-05"}
  - {q: "What were gold auction losses in Q2 FY27, in Rs Cr?", from_finding_id: "FN11"}
  - {q: "Which gold loan industry change on slide 29 lifted gold Stage 3 from 0.1% to 0.5%?", from_finding_id: "FN03"}
  - {q: "Of the Rs 1,085 Cr Q2 sell-down (Rs 876.89 Cr filed as DA; Rs 208 Cr unreconciled), what share went to Federal Bank?", from_finding_id: "FN07, A3-12"}
  - {q: "What was the gross gain on pools assigned in Q2 FY27, before reversal on older pools?", from_finding_id: "FN08, FND-06, A3-09"}
  - {q: "At what CRAR level will the board raise equity (D/E 4.61x vs 6x cap, unchanged from Mar-26; CRAR 22.40% to 20.96% in H1)?", from_finding_id: "A3-04, FN16, FND-07"}
  - {q: "Which of the five FY27 guidance items from the Q1 call do you now revise?", from_finding_id: "FN02, FND-13"}
  - {q: "Will the company refile Q2 FY27 basic EPS (printed 3.56 vs 3.49 implied by H1 6.54 less Q1 3.05)?", from_finding_id: "A3-10"}
  - {q: "How many of the 126 remaining FY27 branches will open by 31-Mar-2027?", from_finding_id: "FN15, FND-08"}
  - {q: "What 12-month AUM per branch do you target for the 74 Q2 branches?", from_finding_id: "FN15, FND-08"}
  - {q: "What drove the Q2 ETR of 26.54% vs 25.17% statutory?", from_finding_id: "A3-05, FN04, FND-01"}
  - {q: "What is the outstanding FCY/ECB borrowing at 30-Sep-2026 (Q2 hedge OCI gain Rs 43.48 Cr)?", from_finding_id: "A3-08, FN05, FND-04"}
  - {q: "What principal outstanding did the 48 accounts sold to ARCs carry (L525 blank)?", from_finding_id: "A3-02"}
  - {q: "What were total H1 FY27 write-offs, in Rs Cr?", from_finding_id: "A3-02, FN09"}
  - {q: "What makes up other financial liabilities of Rs 468.19 Cr at Sep-26 (Rs 216.38 Cr at Mar-26)?", from_finding_id: "A3-12"}
  - {q: "Who appointed V. Sankar Aiyar & Co. as joint statutory auditor, on what date, under which rule?", from_finding_id: "A3-03"}
  - {q: "Does the trust deed define total outstanding liability as borrowings only (filed TOL/ATNW 4.61x on 31-Mar-2026 audited figures vs 4.79x computed on the same figures)?", from_finding_id: "A3-15"}
  - {q: "How did the Federal Bank derivative margin deposit reach Rs 16.16 Cr with nil opening and nil flow?", from_finding_id: "A3-16"}
  - {q: "What is the Rs 1.85 Cr H1 brand-usage fee to Federal Bank based on, and from what date?", from_finding_id: "A3-16"}
  - {q: "What is Gross Stage 3 % for North-originated mortgages of FY25-FY26 vintage?", from_finding_id: "FN12"}
  - {q: "What undrawn sanctioned lines did the company hold at 30-Sep-2026 (ALM <3m surplus Rs 186 Cr)?", from_finding_id: "FN17"}
  - {q: "Is the Q2 FY26 ECL column on the same basis as Q1 and Q2 FY27?", from_finding_id: "FN20"}
  - {q: "How many NAPS apprentices were on the rolls at 30-Sep-2026?", from_finding_id: "FN21"}
  - {q: "What were FY26 yield, CoB and spread on the old two-point basis?", from_finding_id: "FN24"}
  - {q: "Which CoB series does management steer on: slide 25 7.9% or daily I-GAAP 7.79%?", from_finding_id: "FN25, FN22"}
  - {q: "Is the press-release H1 FY27 Shareholder's Fund of Rs 2,926.1 Cr the 31-Mar-2026 opening balance?", from_finding_id: "FND-03"}
  - {q: "Why did other income fall 1.9% YoY to Rs 27.78 Cr while AUM grew 36.6%?", from_finding_id: "FND-09"}
  - {q: "Is the 0.6% credit cost on two-point or daily average total assets?", from_finding_id: "FND-12"}
  - {q: "Publish gold 30+ and 60+ DPD for Q2 FY27 (carried from Q1, not addressed).", from_finding_id: "carried Q1 Q4; A3-11"}
  - {q: "Give the bridge for Stage 3 ECL from Rs 96.8 Cr to Rs 104.7 Cr (carried from Q1, not addressed).", from_finding_id: "carried Q1 Q9; FN09"}
  - {q: "Through which route did the Rs 208 Cr of the Q2 sell-down not filed as direct assignment leave the book: co-lending, securitisation, or other?", from_finding_id: "FN07, A3-12, FND-07"}
monitorables:
  - {item: "Q2 FY27 earnings-call transcript filed; grade questions", implied_date: "about 2026-10-22 [INFERENCE]", source_ref: "Deck R006, fulltext L30-35"}
  - {item: "Results newspaper publication", implied_date: "about 2026-10-17", source_ref: "Res R649 L61"}
  - {item: "Q3 FY27 results: credit cost (single cleanest metric; bull <=0.8%, bear >=1.0%), PCR, Stage 2, stressed coverage, gold Stage 3, DA line", implied_date: "mid-January 2027 [INFERENCE]", source_ref: "Res R657, R662"}
  - {item: "Remaining 126 of 200 FY27 branches", implied_date: "2027-03-31", source_ref: "Deck R033; Notion promise log"}
  - {item: "Gold tonnage +10-12% FY27 (13.86-14.11 t)", implied_date: "2027-03-31", source_ref: "Deck R491; Notion"}
  - {item: "Gold AUM +25-30% FY27 on a price-flat basis (price-flat pace about +19% to +26%)", implied_date: "2027-03-31", source_ref: "Deck R441-R443, R489-R491, R499-R501"}
  - {item: "Entity AUM +20-22% FY27 (Rs 24,184-24,587 Cr)", implied_date: "2027-03-31", source_ref: "Deck R423; Notion"}
  - {item: "Credit cost below 1% FY27", implied_date: "2027-03-31", source_ref: "Notion promise log"}
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
  - {item: "Operator ruling on Pillar 2L self-withdrawal baseline (QoQ vs FY26)", implied_date: "before next /fttcp or Role 1 refresh", source_ref: "Res R440-R442; Notion Pillar 2L"}
flags:
  - "PILLAR2L-SELFWITHDRAW-CONDITION: PCR 38.36% to 35.37% QoQ meets 'PCR thins further' on QoQ baseline, not vs FY26 32.29%; operator ruling"
  - "PCR-EROSION: checklist item 2 AMBER; 32% red line holds"
  - "COVERAGE-RELEASE-PAT [INFERENCE]: ~Rs 19.3 Cr ECL gap at Q1 stage coverage; ~88% of QoQ PAT gain; Stage 1 took 12.0 of 21.8 Cr build; stressed +195 Cr got 10.0 Cr (5.1%); stressed coverage 24.5% to 20.2%"
  - "STAGE2-SURGE: Stage 2 +34.6% QoQ, coverage 16.53% to 12.61%"
  - "GOLD-GROWTH-QUALITY: tonnage +1.6% QoQ vs gold AUM +6.5%; LTV 68.0% vs origination 72.1%; gold GS3 0.1% to 0.5% QoQ (+10 bps YoY)"
  - "GOLD-TRIGGER-AT-RISK: gold AUM +25-30% reachable at a flat gold price only if FY27 tonnage reaches about 14.0 t (+11.2% on 12.6 t) vs +2.4% in H1; price-flat pace about +19% to +26%; Q2 growth about 70% price"
  - "OFFBOOK-DEPENDENCE: AUF +27 Cr vs AUM +899 Cr; gold AUF -52 Cr; buyer identity ND"
  - "SELLDOWN-DA-GAP: deck sell-down Rs 1,085 Cr vs filed DA Rs 876.89 Cr; Rs 208 Cr unreconciled, route NOT DISCLOSED; CLM size unresolved"
  - "DA-DRAG: net DA loss -12.9 / -1.2 Cr"
  - "LEVERAGE-LED-ROE / CAPITAL-COMPRESSION: leverage 5.0x to 6.0x; CRAR -144 bps H1; D/E 4.61x vs 6x; H1 net de-leverage nil"
  - "EPS-MISPRINT: Q2 basic 3.56 printed vs 3.49 derived"
  - "CREDITCOST-BASIS: Notion mixes avg AUM (FY26 0.64%) and avg assets (company FY26 0.8%)"
  - "NOTION-STALE: CMP 164; gold mix 46.5% vs 54.1%; secured 98.9% vs 99.4%"
  - "PRIOR-FVOCI-UNIT: Notion '~585cr' vs filed Q1 FVOCI-loans OCI Rs 58.51 Cr"
  - "CASHCONV-INDETERMINATE-WITH-DIRECTION: growth-induced; collection efficiency and write-offs ND"
  - "DISCLOSURE-SILENCE: 0 of 13 prior questions fully answered (8 partial, 5 not addressed); guidance, CE, write-offs, Tier I, DPD ND"
  - "GROWTH-TRIGGERS-LAGGING: entity AUM, branches, tonnage, de-leverage DELAYED; mortgage, co-lending WEAKENED; gold AUM AT RISK"
  - "TRACKER-ROWS-ND: 0 signals supplied; reopen Role 5.5; 3 Case B candidates"
  - "ENTRY-ZONE-BELOW-BOOK: zone max Rs 77 < BVPS Rs 84.4 (Role 1)"
  - "PROJECTIONS-ND: no bear/base/bull P&L; 6A landing not assessable"
  - "CONCALL-NOT-IN-RUN: call held per deck cover letter; transcript absent"
  - "PIPELINE: A1 OCI sign misreads and slide 22/25 attribution errors, resolved via orchestrator check; A2 adds results rows L525, L526, L812, L932 in loop 1"
  - "DEFERRED-OR30: Role 4 Steps 6.5 and 7 deferred to /fttcp and Role 1"
plain_language_brief_included: true
loop_2: "F4, C3, S11 applied"
analyst_note: "Loop 1 revision. YoY headline is real: core PBT ex-treasury +70.3%; treasury, not ETR, is the main wedge to PAT growth. QoQ, about 76% of the +24.5 Cr PBT gain came from the DA loss narrowing and lower provisions. The coverage fork now leans bear: total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build; Rs 195 Cr of new stressed assets got Rs 10 Cr, so stressed coverage fell 24.5% to 20.2%. Reading B (release) carries at least equal weight. Gold AUM growth fails its own price-flat condition: Q2 was about 70% price, H1 was LTV-led, and LTV sits 4 pp below origination; the trigger is AT RISK and needs about 14.0 t of FY27 tonnage at a flat price. H1 net de-leverage is nil (D/E 4.61x at Mar-26 and Sep-26). The deck sell-down (Rs 1,085 Cr) exceeds filed DA (Rs 876.89 Cr) by Rs 208 Cr with no stated route. The Pillar 2L baseline ruling stays with the operator. loop_2: F4, C3, S11 applied."
review_path: "C:\\Users\\SUMIT SHARMA\\repos\\inflection-pipeline\\.claude\\worktrees\\q2fy27\\runs\\fedfina-q2fy27\\work\\review_fedfina_q2fy27.md"
```

---

## OPEN ITEMS AT CLOSE (orchestrator record; text from the A5 loop-2 audit, no analysis added)

Loop cap reached (operator ruling 2026-10-17: one second loop, no third; close with open items flagged). A5 loop-2 verdict INCOMPLETE on one item; carried here for the operator:
- F5 (FACTUAL, A4 YAML analyst_note, about L814): "total ECL/AUF rose only because Stage 1 took 12.0 of the 21.8 Cr build" is not supported. A5 replacement text: "total ECL/AUF rose mainly because Stage 1 took 12.0 (55%) of the 21.8 Cr build". With no Stage 1 build the ratio still rises 1.365% to 1.423%. The body at L304 (55%) is correct. No figure, flag, protocol verdict or Decision Status changes.
- STYLE, logged only: S7-S10, S12-S14 (see work/audit_fedfina_q2fy27.md, Re-audit loop 2).
