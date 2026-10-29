# SONACOMS Q2 FY27: MERGED QUARTERLY REVIEW (A4 ANALYST)

Sona BLW Precision Forgings Ltd ("Sona Comstar"), quarter and half year ended 30-Sep-2026. Results, deck and press release dated 26-Oct-2026. Earnings call 26-Oct-2026 17:00 IST.

Agent: A4 analyst | model claude-opus-5-5 | run date 2026-10-28 | revision: correction loop 1 (A5 audit work/audit_sonacoms_q2fy27.md)
Protocols loaded: Role 4 Quarterly Results Review Protocol v1.4; Role 5 Quarterly Concall Analysis Protocol v1.1. Not loaded: Master, FTTCP, Section 1B, RDE manual, Document Review Protocol.
Role 4 Steps 6.5 and 7 and Role 5 Step 8D: deferred to /fttcp and Role 1 (operator ruling OR-30). Pillar-relevant facts are flagged where they arise.

## LOOP 1 CHANGE LOG (A5 findings M1, M2, F1, F2, C1 and style notes)

| ID | Fix | Where |
|---|---|---|
| M1 | Deck ledger rows M01-M15 (A2 revision 2) added to the preamble counts and cited at each use. Deck L516 44,752 (M09) checked against the filing: it equals FY26 rev ops 44,494.60 mn + forex 256.88 mn (res L470-471), so it is FY26 on the deck's forex-inclusive basis; the year label is positional only. The FY21 start point (15,663, R239, LABEL_UNMAPPED) is positional only, so FY28E-B now uses the labelled deck "5-year Revenue CAGR 23%" (R242, deck L583-587) | Preamble; Step 2c; Forward Estimate table (FY28E-B restated) |
| M2 | DENSO 49% stake-sale economics added: EV Rs 1,750 Cr, 49% = Rs 857.5 Cr pre-tax, taxable [ASR]; carve-out EBITDA/PAT NOT FOUND; proxy EV/sales about 2.2x (1.8x on ASR run-rate) vs Sona about 10.1x; two readings; separating observation; bull-fork cash capped | New subsection after Step 6.5/7; Step 6.5/7 table; Q2 in Step 8.5; Role 5 5A; Section C; Brief parts 3 and 5 |
| F1 | BEV +129% cause re-tagged [ASR, call L135-140]; concentration counter added | Brief part 2 |
| F2 | Starter-motor share history corrected (also fell CY21 4.6% to CY22 4.1%, deck L703) | Brief part 4 |
| C1 | Railway aligned to AMBER / UNVERIFIED everywhere (growth trigger #1, tripwire 8, concall 8A and 8B) with one evidence set | Step 6B, 6D; Role 5 8A, 8B; Section C |
| S1-S9, S11, S12 | Applied (raw-million growth rates; 3.6x subsidiary layer; tags; 0.77 yr; Q1 FY26 derived from filing; forex period alignment; Q15 asker; A2-flag dispositions; NCI caveat; net-capex tie) | Inline |
| S10 | Skipped: an A2 ledger housekeeping item (closing YAML on the PR ledger; PR footer L101 row). Not an A4 file. The deck ledger now carries its closing block (revision 2) | n/a |

Verdict unchanged: PROCEED WITH FLAGS. No fix moves it.

## SOURCE-CLASS HEADER (read first)

| Document | Source class | Anchor key |
|---|---|---|
| Results (Reg 33, 16 pages) | FILED. Statement pages 4-8 and 12-16 are image-only; A1 transcribed them visually | "res L###" = A1 results fulltext line |
| Investor deck (36 slides) | MGMT-FILED (exchange filing, company-authored) | "deck L###" = A1 presentation fulltext line |
| Press release (4 pages) | MGMT-FILED | "PR L###" = A1 press release fulltext line |
| Concall | MACHINE ASR transcript (faster-whisper small.en). NOT company-filed. Management-tier, unverified, speakers inferred, numbers may be misheard | "call L###" = source line in the A1 concall fulltext; every concall-only number carries [ASR] |
| Notion page (fetched 28-Oct-2026) | Operator memory, not a corpus document | [NOTION MEMORY] |

Rule applied throughout: filed documents win on every conflict with the transcript.
Units: filing in Rs million, converted x0.1 to Rs Crore. Deck Rs mn x0.1; deck Rs bn x100. All figures below are Rs Cr unless stated.
Company memory: no companies/SONACOMS.md exists in the repo. None was read.
Derived figures (margins, growth, days, ratios) are my arithmetic on the anchored lines cited in the same row or table header. Growth rates are computed on raw Rs million values (A5 S1).

## LEDGER RECONCILIATION PREAMBLE

Ledger contains 13 notes (15 counting Notes 4a and 4b; standalone 7, consolidated 6) / 53 turns (inferred) and 18 questions / 36 slides (plus 4 press-release pages). All reviewed.

| Ledger | IDs | Count test | Orphans | Reviewed |
|---|---|---|---|---|
| Results | R001-R1098 (1,098); notes 15, line items 249, cells 771, zero-standing 47 cells on 19 lines, agenda 1, auditor paras 9, entities 17, signature blocks 5 | gate_a2 pass | none | 1,098 / 1,098 |
| Presentation | R001-R317 (317) + M01-M15 (15 MISSING_FROM_STRUCTURED, A2 revision 2) = 332; 36 slides, 201 + 12 = 213 numbers (M01, M04-M14), 42 footnotes, 12 forward, 22 dates, 40 + 3 = 43 entities (M02, M03, M15) | gate_a2 pass (revision 2) | none | 332 / 332 |
| Press release | R001-R127 (127); 4 pages, 52 numbers | gate_a2 pass | none | 127 / 127 |
| Concall | R001-R336 (336) + M01-M09 (9 MISSING_FROM_STRUCTURED); 53 turns, 18 questions, 110 management numbers | gate_a2 pass | none | 345 / 345 |

Deck MISSING_FROM_STRUCTURED rows (A2 revision 2), cited by ID wherever used: M01 deck L291 "22%"; M02 deck L504 "Became publicly listed"; M03 deck L505 "Acquisition of NOVELIC and Railway Business"; M04 deck L506 "12 plants"; M05 deck L507 "34 products"; M06 deck L510 "57,136 H1FY27 (Ann.)"; M07 deck L512-513 "Avg. EBITDA margin 25.1%"; M08 deck L515 "Revenue CAGR 24.1%"; M09-M13 deck L516, L518, L519, L520, L522 revenue bars 44,752 / 35,545 / 31,866 / 26,756 / 21,306 (LABEL_UNMAPPED, year positional); M14 deck L523 "28,568 H1FY27"; M15 deck L156, L378 photo captions. M09 tie-out: 44,752 = FY26 rev ops 44,494.60 + forex 256.88 = 44,751.48 mn (res L470-471), so the bar series is forex-inclusive revenue and M09 is FY26. M14 ties to H1 FY27 rev ops 28,370.41 + forex 197.48 = 28,567.89 mn.

A2-flagged rows with no separate finding, dispositioned (A5 S9): R882 NAME_VARIANT "Precisions" (res L437): reviewed, no finding beyond RES:F14-02. R537 LOW_LEGIBILITY C OCI remeasurement H1 FY27 7.05 (res L489): reviewed, ties within rounding (Q1 (0.04) + Q2 7.08 = 7.04), no finding. Deck R044, R058, R317 FOOTNOTE_UNRESOLVED: reviewed, no finding beyond P-A3-F14-04.

Findings incorporated (98 A3 findings; results IDs carry the prefix RES: because they share bare IDs with other files):
- Results (28): RES:F1-01, RES:F1-02, RES:F1-03, RES:F2-01, RES:F2-02, RES:F2-03, RES:F2-04, RES:F2-05, RES:F2-06, RES:F3-01, RES:F3-02, RES:F6-01, RES:F6-02, RES:F7-01, RES:F8-01, RES:F8-02, RES:F8-03, RES:F10-01, RES:F10-02, RES:F12-01, RES:F12-02, RES:F12-03, RES:F14-01, RES:F14-02, RES:F14-03, RES:F14-04, RES:F15-01, RES:F15-02.
- Presentation (25): P-A3-F6-01 to P-A3-F6-05, P-A3-F7-01, P-A3-F10-01, P-A3-F14-01 to P-A3-F14-04, P-A3-F16-01 to P-A3-F16-09, P-A3-F17-01 to P-A3-F17-05.
- Press release (17): A3-PR-F6-01 to A3-PR-F6-03, A3-PR-F14-01 to A3-PR-F14-06, A3-PR-F16-01 to A3-PR-F16-04, A3-PR-F17-01 to A3-PR-F17-04.
- Concall (28): A3-F6-01 to A3-F6-06, A3-F7-01 to A3-F7-05, A3-F8-01, A3-F10-01, A3-F14-01 to A3-F14-04, A3-F17-01 to A3-F17-11.
- A5 loop 1 findings addressed: M1, M2, F1, F2, C1.

---

# SECTION A: RESULTS REVIEW (ROLE 4)

## STEP 0: PRE-FLIGHT

### 0A. Notion baseline (fetched 28-Oct-2026 10:02 IST)

| Field | Value on page | Status |
|---|---|---|
| Decision Status | WATCHLIST (property). Body: "WATCHLIST, Avoid at CMP" | VERIFIED before any framing. Operator-only field |
| Position size / cost basis | Position Size "None"; Avg Cost blank | Not held. Branch 8A-W applies |
| One-line thesis | "NOT buying Sona at Rs 609 ... The problem is the multiple, not the business" | [NOTION MEMORY] |
| Gate 0 | AVERAGE, 85/160 (core 69/100, moat 16/60) | [NOTION MEMORY] |
| EM | MOAT EXPANSION UNDERWAY, 52/100 | [NOTION MEMORY] |
| Destination PE | about 22.5x (revised from 24x after FY26 AR) | [NOTION MEMORY] |
| Pillar values | ROCE base 16x (15-20% band); Cash Multiplier 0.85x; Growth Premium +4.0x; Strategic Premium +4.0x; RRM 1.00x; Manufacturing cap 25x, no quality uplift | [NOTION MEMORY] |
| Bear/Base/Bull | FY29 (Y3) EPS Rs 12.2 / 16.0 / 20.6; FV about Rs 293 / 384 / 494 | [NOTION MEMORY] |
| FY27 and FY28 revenue, margin, PAT, EPS projections | ND, not on page | Gap |
| Entry levels | 25% CAGR entry about Rs 197; MoS about Rs 157; quality-hold about Rs 385; buyable trigger CMP <= Rs 185 + ROCE > 18% + Novelic resolved | [NOTION MEMORY] |
| Thesis-broken conditions | ROCE < 14% for 2 consecutive years; forced block sale or control dispute. Monitored: Novelic KAM impairment > Rs 350 Cr; CFO/PAT < 1.0x sustained; corporate guarantee expansion | [NOTION MEMORY] |
| Monitoring checklist | Tripwires 1-10 (Q1 FY27 Step 6B table) | [NOTION MEMORY] |
| Growth triggers | #1 Railway diversification (FIRED); #2 BEV anchor (AMBER); #3 Sensors and Software / Robotics (live). The AR note also labels "India 51%" as Trigger #3 FIRED: two labels for #3 on the page | [NOTION MEMORY]; numbering conflict flagged |
| Devil's Advocate split | ND, not on page (child page not passed) | Gap |
| Prior Questions for Management | Role 4 Q1-Q12 and Role 5 N1-N14 | Scored below |
| Prior concall promise log | C1-C9 baseline (Q1 call 23-Jul-2026) | Scored in Step 3 (Role 5) |
| Promoter Verdict / Mgmt grade | TRUSTWORTHY; "Mgmt grade A" (AR entry) | [NOTION MEMORY] |
| Pending operator rulings | (1) Does the margin gate include net forex? (2) Is the cash leg tested ex-payables? (3) Score C1 now or after the call? | Still open |
| CMP context | Rs 879, market cap Rs 55,012 Cr (screener.in, 28-Oct-2026 08:48 IST). Rs 782 on page (26-Oct close, pre-results) | +12.4% since results |

Frame: this is a THESIS CHECK against a WATCHLIST name with an AVOID-at-CMP posture in the body.

### 0B. Units
All filing figures in Rs million (res L144, L468: "Figures in Million Rs"). Conversion x0.1 to Rs Crore. EPS in Rs.

### 0C. Share-count changes
| Item | Value | Anchor |
|---|---|---|
| Paid-up capital (Rs mn, face value Rs 10) | 6,218.47 (31-Mar-26) to 6,220.35 (30-Jun-26) to 6,241.28 (30-Sep-26) | res L171, L502, L536 |
| Implied shares at 30-Sep-26 | 624.128 mn = 62.41 Cr shares | my arithmetic, res L502 |
| H1 increase | 2.281 mn shares (+0.37%); Q2 alone 2.093 mn (+0.34%) | my arithmetic |
| ESOP cash, H1 | Rs 107.60 Cr | res L614 |
| ESOP grant | 1,00,000 options at Rs 596.35, 16-Jun-2026 | res L313 / L646 |
| MD Performance Share Plan | 1,70,747 shares at face value on FY26 metrics, NRC 05-May-2026 | res L314 / L647. Not in the Notion share log [NOTION MEMORY] |
| Basic vs diluted EPS | First spread: SA Q2 3.17 / 3.16; C H1 6.49 / 6.48 | res L173-174, L504-505 |
| Split, bonus, rights, QIP, buyback | None in the period | res notes |
No restatement needed. Share-adjusted EPS = reported EPS.

### 0D. Notes extraction

| Note # | Subject | What it says (1 sentence) | Rs Cr impact | Period affected | Comparability impact |
|---|---|---|---|---|---|
| SA 1 / C 1 | Basis, approvals | Audit Committee reviewed 25-Oct-2026, Board approved 26-Oct-2026, auditor issued unmodified review report (res L303-304, L636-637) | ND (no amount) | Q2/H1 FY27 | None; context for the signing-time finding RES:F14-01 |
| SA 2 / C 2 | Railway acquisition | Railway Business of Escorts Kubota acquired 01-Jun-2025 by slump sale for Rs 1,642.63 Cr (res L305, L638) | 1,642.63 (consideration) | From 01-Jun-2025 | Q1 FY26 had about 1 month of railway; Q2 FY26 and Q2 FY27 both carry a full quarter, so the Q2 YoY is like-for-like on railway |
| SA 3 / C 3 | Exceptional items | Nil in Q1, Q2, H1 FY27; Q2 FY26 1.67 (acquisition costs); FY26 SA 50.79 / C 50.98 incl. New Labour Codes SA 39.95 / C 40.14 (res L309-311, L642-644) | Q2 FY26 1.67; H1 FY26 10.84 | Prior periods | Q2 FY26 PBT depressed by 1.67; YoY PBT and PAT flattered by that amount. SA H1 FY26 total cell blank (RES:F14-03) |
| SA 4a / C 4a | ESOP grant | 1,00,000 options at Rs 596.35 on 16-Jun-2026 (res L313) | ND | FY27 onward | Share-based cost; first diluted spread |
| SA 4b / C 4b | MD performance shares | 1,70,747 shares to the MD at face value on FY26 metrics (res L314) | about 0.17 Cr face value; market value ND in filing | FY27 | Dilution about 0.03% |
| SA 5 / C 5 | DENSO JVs | Definitive agreements 22-Jul-2026 for two JVs; EV motors and controllers business to be slump-sold into a 100% subsidiary; DENSO buys 49% at EV Rs 1,750 Cr; royalties to each partner (res L315-319, L648-652) | EV 1,750.00; gain ND | Close pending ("subject to fulfilment of customary conditions") | H1 is like-for-like (eDrive still WOS, res L448). From close, like-for-like breaks. Accounting route ambiguous (RES:F1-02). Pricing economics: see "DENSO 49% stake-sale economics" after Step 6.5/7 |
| SA 6 | Dividend from WOS | Rs 59.46 Cr dividend from an unnamed WOS on 19-Jun-2026 (res L320) | 59.46 in SA Q1 other income | SA Q1 FY27 | Inflated SA Q1 PAT and SA H1 other income; eliminated in C |
| SA 7 / C 6 | Segment | Single segment "Mobility components, systems and sub-systems" (res L321, L653) | n/a | All | No segment split possible |
| Unnumbered | Cash flow method, Ind AS 7 (res L292, L625); Novelic India incorporated 28-Nov-2025 (res L460) | n/a | n/a | Perimeter: Novelic India new vs Q2 FY26 |

Auditor opinion: UNMODIFIED on both standalone (res L113-119) and consolidated (res L379-386, "Our conclusion is not modified", res L408). No emphasis of matter. No going concern. Consolidated para 5 relies on another auditor for five unnamed foreign subsidiaries: total assets Rs 200.74 Cr, H1 revenue Rs 38.96 Cr, H1 loss Rs 2.42 Cr (res L388-394). No AMBER from opinion.

Governance item (not opinion): both review reports were signed 13:26:32 (SA, res L128) and 13:27:12 (C, res L418), before the board started at 14:00 (res L49). Second quarter running (Q1: 14:11 vs 14:15 start [NOTION MEMORY]). RES:F14-01.

### 0E. Business type
Standard operating business (build-to-spec component maker). Steps 1 and 5 apply; lender variants not used.

Checkpoint: Notion fetched with Decision Status, units stated, share changes noted, notes extracted, auditor opinion verified, business type stated.

## STEP 1: DATA EXTRACTION (both statements, Rs Cr)

### 1a. Consolidated

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 | Source |
|---|---|---|---|---|---|---|---|---|
| Revenue from operations | 1,138.29 | 1,301.20 | 1,535.84 | 1,992.20 | 2,837.04 | 4,449.46 | ND (year in progress) | res L470 |
| Foreign exchange gain (net) | 5.23 | 9.17 | 10.58 | 2.22 | 19.75 | 25.69 | ND | res L471 |
| Other income | 16.95 | 25.70 | 30.95 | 61.14 | 56.65 | 96.97 | ND | res L472 |
| Total income | 1,160.47 | 1,336.07 | 1,577.37 | 2,055.56 | 2,913.44 | 4,572.11 | ND | res L473 |
| Cost of materials consumed | 558.41 | 679.86 | 818.48 | 974.78 | 1,498.34 | 2,141.96 | ND | res L474 |
| Change in inventories | (11.88) | (29.85) | (35.62) | (49.08) | (65.47) | (45.12) | ND | res L475 |
| Employee benefits expense | 103.04 | 128.84 | 130.60 | 190.84 | 259.45 | 434.18 | ND | res L476 |
| Finance costs | 5.16 | 10.48 | 12.32 | 10.49 | 22.79 | 23.48 | ND | res L477 |
| Depreciation and amortisation | 71.62 | 76.88 | 78.91 | 138.61 | 155.79 | 287.74 | ND | res L478 |
| Other expenses | 204.89 | 228.91 | 276.71 | 386.27 | 505.63 | 837.28 | ND | res L479 |
| Total expenses | 931.24 | 1,095.12 | 1,281.41 | 1,651.92 | 2,376.53 | 3,679.51 | ND | res L480 |
| Profit before exceptional items and tax | 229.23 | 240.94 | 295.96 | 403.64 | 536.91 | 892.60 | ND | res L481 |
| Exceptional items | 1.67 | nil | nil | 10.84 | nil | 50.98 | ND | res L482 |
| Profit before tax | 227.56 | 240.94 | 295.96 | 392.80 | 536.91 | 841.62 | ND | res L483 |
| Tax expense | 57.09 | 62.43 | 72.98 | 100.62 | 135.41 | 212.43 | ND | res L487 |
| PAT (total) | 170.47 | 178.51 | 222.99 | 292.17 | 401.50 | 629.19 | ND | res L488 |
| PAT, owners of the parent | 172.77 | 180.47 | 223.40 | 297.48 | 403.87 | 640.17 | ND | res L496 |
| PAT, non-controlling interests | (2.31) | (1.96) | (0.42) | (5.31) | (2.37) | (10.98) | ND | res L497 |
| EPS basic (Rs) | 2.78 | 2.90 | 3.58 | 4.78 | 6.49 | 10.30 | ND | res L504 |
| EPS diluted (Rs) | 2.78 | 2.90 | 3.58 | 4.78 | 6.48 | 10.30 | ND | res L505 |
| EPS share-adjusted (Rs, diluted) | 2.78 | 2.90 | 3.58 | 4.78 | 6.48 | 10.30 | ND | no split/bonus; = res L505 |

Derived (consolidated). Operating EBITDA uses profit before exceptional items, so the one-off in prior periods does not distort it. Forex stays inside operating EBITDA under the protocol formula; the ex-forex row is shown because the gate basis is pending.

| Derived metric | Formula | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|---|
| Operating EBITDA | PBET + D&A + Finance - OI | 289.06 | 302.60 | 356.24 | 491.60 | 658.84 | 1,106.85 | ND |
| Op EBITDA margin (on rev ops) | Op EBITDA / Rev ops | 25.39% | 23.26% | 23.20% | 24.68% | 23.22% | 24.88% | ND |
| Op EBITDA ex-forex | Op EBITDA - forex | 283.83 | 293.43 | 345.66 | 489.39 | 639.10 | 1,081.17 | ND |
| Op EBITDA margin ex-forex | / Rev ops | 24.93% | 22.55% | 22.51% | 24.57% | 22.53% | 24.30% | ND |
| Op EBITDA margin, deck basis | Op EBITDA / (Rev ops + forex) | 25.28% | 23.09% | 23.04% | 24.65% | 23.06% | 24.73% | ND |
| Reported EBITDA | PBT + D&A + Finance | 304.34 | 328.30 | 387.19 | 541.90 | 715.49 | 1,152.84 | ND |
| Core PBT (ex-OI), before exceptional | PBET - OI | 212.28 | 215.24 | 265.01 | 342.50 | 480.26 | 795.63 | ND |
| Core PBT (ex-OI), reported | PBT - OI | 210.61 | 215.24 | 265.01 | 331.66 | 480.26 | 744.65 | ND |
| Other income / PBT | OI / PBT | 7.45% | 10.67% | 10.46% | 15.57% | 10.55% | 11.52% | ND |
| Effective tax rate | Tax / PBT | 25.09% | 25.91% | 24.66% | 25.62% | 25.22% | 25.24% | ND |
| PAT margin (total PAT / rev ops) | | 14.98% | 13.72% | 14.52% | 14.67% | 14.15% | 14.14% | ND |
| Materials (incl. inventory change) / rev ops | | 48.01% | 49.95% | 50.97% | 46.47% | 50.51% | 47.13% | ND |
| Employee cost / rev ops | | 9.05% | 9.90% | 8.50% | 9.58% | 9.14% | 9.76% | ND |
| Other expenses / rev ops | | 18.00% | 17.59% | 18.02% | 19.39% | 17.82% | 18.82% | ND |

Cross-checks: Q2 FY27 op EBITDA 356.24 ties to the deck "3,562 mn" (deck L119). Deck revenue 15,464 mn (deck L119) = rev ops 15,358.40 + forex 105.79 (res L470-471): the deck and press release revenue includes net forex (deck L404 footnote; PR L69 Rs 1,547 Cr). Deck PAT 2,234 mn = owners PAT 2,234.04 (res L496).

### 1b. Standalone

| Line item | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 | Source |
|---|---|---|---|---|---|---|---|---|
| Revenue from operations | 1,056.99 | 1,157.24 | 1,377.04 | 1,824.30 | 2,534.28 | 4,123.67 | ND | res L146 |
| Foreign exchange gain (net) | 6.24 | 8.30 | 7.80 | 6.53 | 16.10 | 31.40 | ND | res L147 |
| Other income | 15.92 | 81.78 | 28.70 | 58.70 | 110.49 | 114.68 | ND | res L148 |
| Total income | 1,079.15 | 1,247.33 | 1,413.54 | 1,889.52 | 2,660.86 | 4,269.75 | ND | res L149 |
| Cost of materials consumed | 516.43 | 610.14 | 735.01 | 886.45 | 1,345.15 | 1,977.99 | ND | res L150 |
| Change in inventories | (7.61) | (32.14) | (31.40) | (38.26) | (63.54) | (31.22) | ND | res L151 |
| Employee benefits expense | 81.20 | 103.91 | 105.51 | 148.97 | 209.42 | 346.92 | ND | res L152 |
| Finance costs | 4.18 | 7.11 | 9.04 | 8.69 | 16.16 | 18.74 | ND | res L153 |
| Depreciation and amortisation | 64.86 | 69.33 | 70.85 | 124.94 | 140.18 | 259.94 | ND | res L154 |
| Other expenses | 195.69 | 213.36 | 261.32 | 363.71 | 474.67 | 789.34 | ND | res L155 |
| Total expenses | 854.75 | 971.70 | 1,150.33 | 1,494.50 | 2,122.03 | 3,361.71 | ND | res L156 |
| Profit before exceptional items and tax | 224.40 | 275.62 | 263.21 | 395.03 | 538.83 | 908.04 | ND | res L157 |
| Exceptional items | 1.67 | nil | nil | 10.84 | nil | 50.79 | ND | res L158 |
| Profit before tax | 222.73 | 275.62 | 263.21 | 384.19 | 538.83 | 857.25 | ND | res L159 |
| Tax expense | 56.48 | 55.52 | 65.83 | 97.81 | 121.34 | 210.84 | ND | res L163 |
| PAT | 166.25 | 220.11 | 197.38 | 286.38 | 417.48 | 646.42 | ND | res L164 |
| EPS basic (Rs) | 2.67 | 3.54 | 3.17 | 4.61 | 6.70 | 10.40 | ND | res L173 |
| EPS diluted (Rs) | 2.67 | 3.54 | 3.16 | 4.61 | 6.70 | 10.40 | ND | res L174 |
| EPS share-adjusted (Rs) | 2.67 | 3.54 | 3.16 | 4.61 | 6.70 | 10.40 | ND | = res L174 |

| Derived (standalone) | Q2 FY26 | Q1 FY27 | Q2 FY27 | H1 FY26 | H1 FY27 | FY26 | FY27 |
|---|---|---|---|---|---|---|---|
| Operating EBITDA (PBET + D&A + Fin - OI) | 277.52 | 270.28 | 314.40 | 469.96 | 584.68 | 1,072.04 | ND |
| Op EBITDA margin | 26.26% | 23.36% | 22.83% | 25.76% | 23.07% | 26.00% | ND |
| Op EBITDA margin ex-forex | 25.66% | 22.64% | 22.27% | 25.40% | 22.44% | 25.24% | ND |
| Reported EBITDA (PBT + D&A + Fin) | 291.77 | 352.06 | 343.10 | 517.82 | 695.17 | 1,135.93 | ND |
| Core PBT before exceptional (PBET - OI) | 208.48 | 193.84 | 234.51 | 336.33 | 428.34 | 793.36 | ND |
| Other income / PBT | 7.15% | 29.67% | 10.90% | 15.28% | 20.51% | 13.38% | ND |
| Effective tax rate | 25.36% | 20.14% | 25.01% | 25.46% | 22.52% | 24.59% | ND |
| PAT margin | 15.73% | 19.02% | 14.33% | 15.70% | 16.47% | 15.68% | ND |

### 1c. Standalone vs consolidated gap (first-class metric; RES:F2-01, RES:F2-02)

| Period | SA PAT | C PAT (total) | SA - C | Gap % of SA PAT | Subsidiary layer op EBITDA incl. forex (C - SA, incl. eliminations) | Subsidiary share of C op EBITDA |
|---|---|---|---|---|---|---|
| Q2 FY26 | 166.25 | 170.47 | (4.22) | -2.54% | 11.54 | 4.0% |
| Q1 FY27 | 220.11 | 178.51 | 41.60 | +18.90% (ex-dividend about -11.1%) | 32.32 | 10.7% |
| Q2 FY27 | 197.38 | 222.99 | (25.61) | -12.97% | 41.84 | 11.7% |
| H1 FY26 | 286.38 | 292.17 | (5.79) | -2.02% | 21.64 | 4.4% |
| H1 FY27 | 417.48 | 401.50 | 15.98 | +3.83% (ex-dividend about -12.1%) | 74.16 | 11.3% |
| FY26 | 646.42 | 629.19 | 17.23 | +2.66% | 34.81 | 3.1% |

Sources: res L164, L488; op EBITDA from Step 1 tables. Gap moved -31.9 pp QoQ (the Q1 Rs 59.46 Cr WOS dividend unwound, res L320) and -10.4 pp YoY (subsidiary layer growth: op EBITDA 11.54 to 41.84, 3.6x, incl. eliminations). Consolidated is the honest basis. The parent (standalone) margin fell 343 bps YoY in Q2 (26.26% to 22.83%); the group margin fell 219 bps because the subsidiary layer cushioned it. Which subsidiary drives it is not disclosed. If that layer sits in the DENSO perimeter, 49% of it leaks to NCI or leaves the consolidation after JV1 close (RES:F2-02, RES:F15-02).

Checkpoint: every cell filled or ND.

## STEP 2: Q2 YoY COMPARISON (Q2 FY26 vs Q2 FY27)

### 2a. Consolidated

| Metric | Q2 FY26 | Q2 FY27 | YoY change | Verdict |
|---|---|---|---|---|
| Revenue from operations | 1,138.29 | 1,535.84 | +34.92% | Strong; like-for-like on railway (full quarter in both) |
| Operating EBITDA (incl. forex) | 289.06 | 356.24 | +23.24% | Grew 11.7 pp slower than revenue |
| Operating EBITDA ex-forex | 283.83 | 345.66 | +21.78% | Slower still |
| Op EBITDA margin, rev-ops basis (pp) | 25.39% | 23.20% | -219 bps | Contracted |
| Op EBITDA margin ex-forex (pp) | 24.93% | 22.51% | -243 bps | Contracted |
| Depreciation | 71.62 | 78.91 | +10.18% | Scaling well below revenue |
| Finance costs | 5.16 | 12.32 | +138.56% | Small base; rising with ST borrowings |
| EBIT (operating) = Op EBITDA - D&A | 217.44 | 277.33 | +27.54% | Helped by D&A leverage |
| Other income | 16.95 | 30.95 | +82.58% | Non-operating lift of 14.00 |
| Core operating PBT (PBET - OI) | 212.28 | 265.01 | +24.84% | Real, but below reported PBT growth |
| Core PBT ex-forex | 207.05 | 254.43 | +22.88% | Cleanest operating read |
| Reported PBT | 227.56 | 295.96 | +30.06% | Flattered by OI and the absent 1.67 exceptional |
| PAT (total) | 170.47 | 222.99 | +30.81% | |
| PAT (owners) | 172.77 | 223.40 | +29.30% | Matches deck "29%" (deck L119) |
| EPS diluted (share-adjusted) | 2.78 | 3.58 | +28.78% | +0.34% Q2 share issuance dilutes slightly |

### 2b. Standalone (parent)

| Metric | Q2 FY26 | Q2 FY27 | YoY change |
|---|---|---|---|
| Revenue from operations | 1,056.99 | 1,377.04 | +30.28% |
| Operating EBITDA | 277.52 | 314.40 | +13.29% |
| Op EBITDA margin | 26.26% | 22.83% | -343 bps |
| Depreciation | 64.86 | 70.85 | +9.24% |
| Finance costs | 4.18 | 9.04 | +116.36% |
| EBIT (operating) | 212.66 | 243.55 | +14.53% |
| Other income | 15.92 | 28.70 | +80.25% |
| Core PBT (PBET - OI) | 208.48 | 234.51 | +12.49% |
| Reported PBT | 222.73 | 263.21 | +18.17% |
| PAT | 166.25 | 197.38 | +18.72% |
| EPS diluted | 2.67 | 3.16 | +18.35% |

### 2c. Six diagnostics

1. Revenue grew +34.92% YoY (Q2 FY26 vs Q2 FY27, consolidated). The company gives no annual revenue guidance; management's medium-term aspiration is a 25% CAGR [ASR, call L830-838]. Notion FY27 projections: ND, not on page. Q2 runs above the aspiration and above the deck's FY22-H1 FY27 annualised CAGR of 24.1% (deck L515, row M08).
2. Op EBITDA margin contracted. Q2 FY27 23.20% vs Q2 FY26 25.39% = -219 bps (rev-ops basis). Ex-forex 22.51% vs 24.93% = -243 bps. Deck basis 23.04% vs 25.28% = -224 bps. The cost decomposition: materials rose from 48.01% to 50.97% of revenue (+296 bps); employee cost fell from 9.05% to 8.50% (-55 bps); other expenses flat (18.00% to 18.02%). The whole compression is material cost and mix.
3. Core operating PBT (PBET - OI) grew +24.84% (212.28 to 265.01). Reported PBT grew +30.06%. Core grew, so the headline is real, but 5.2 pp of the reported PBT growth is non-operating.
4. Gap between core PBT growth and reported PAT growth (+30.81%): other income +14.00; prior-year exceptional charge absent +1.67; ETR down 43 bps (25.09% to 24.66%) adds about +1.27 to PAT; finance cost -7.16 sits inside core PBT already. See Step 4.
5. D&A +10.18% and finance +138.56% vs revenue +34.92%. D&A scales well below revenue: no absorption deficit; capex halved in H1 (Step 5). Finance cost is rising fast from a small base because short-term borrowings doubled (Step 5).
6. Other income concentration: Q2 OI 30.95 vs H1 56.65; not a spike relative to Q1 (25.70). OI/PBT 10.46% (C). The standalone Q1 OI spike (81.78, of which 59.46 dividend) is an SA artefact only. Stripping OI entirely, core PBT ex-forex grows +22.88%.

Checkpoint: YoY table and diagnostics shown.

## STEP 3: SEQUENTIAL QoQ TRAJECTORY (consolidated)

| Quarter | Revenue (Rs Cr) | Op EBITDA margin (rev ops) | Core PBT before exceptional (ex-OI) | One-offs flagged | QoQ revenue run-rate |
|---|---|---|---|---|---|
| Q1 FY26 | 853.91 [FILED, derived: H1 FY26 - Q2 FY26, res L470] | 23.72% [FILED, derived] | 130.22 [FILED, derived, res L481, L472] | Exceptional 9.17 (H1 FY26 10.84 - Q2 FY26 1.67); railway about 1 month only | ND (Q4 FY25 not on file) |
| Q2 FY26 | 1,138.29 (res L470) | 25.39% | 212.28 | Exceptional 1.67 (res L482) | +33.30% (railway full quarter) |
| Q3 FY26 | 1,199.76 (derived: FY26 - H1 FY26 - Q4 FY26 [NOTION MEMORY]) | 25.39% (derived) | 224.27 (derived) | New Labour Codes 40.14 (FY26 H2 exceptional; Q4 recorded nil on page, so Q3 [INFERENCE]) | +5.40% |
| Q4 FY26 | 1,257.50 [NOTION MEMORY] | 24.70% [NOTION MEMORY] | 228.86 [NOTION MEMORY] | Balancing-figure quarter | +4.81% |
| Q1 FY27 | 1,301.20 (res L470) | 23.26% | 215.24 | SA dividend 59.46 (SA only) | +3.48% |
| Q2 FY27 | 1,535.84 (res L470) | 23.20% | 265.01 | None | +18.03% |

Q3 and Q4 FY26 inputs come from Notion memory and were not audited against an extract (A5 S6).

Diagnostics:
- Run-rate: STEPPING UP on revenue (+18.03% QoQ, a new high), PLATEAU-LOW on margin (23.26% to 23.20%, -6 bps; two quarters near 23% after four quarters at 23.7% to 25.4%).
- One-off distortion: none in Q2 FY27. Q1 FY27 SA dividend does not touch consolidated.
- Q2 revenue 1,535.84 exceeds the H1 average run-rate of 1,418.52 by 8.27%. Core PBT 265.01 exceeds the H1 average 240.13 by 10.4%. Capex commissioning test: CWIP rose (Step 5); no large commissioning in H1, so the H1-vs-Q4 test is not binding this half.
- Implied Q3 FY27 base to hold trajectory: revenue >= 1,535.84 and op EBITDA margin >= 23.20% (rev ops) / 22.51% ex-forex. Seasonal reference: FY26 Q3 grew +5.40% QoQ (derived from memory figures).

Checkpoint: QoQ table and diagnostics shown.

## STEP 4: OPERATIONAL DECOMPOSITION (PAT bridge, consolidated, Q2 FY26 to Q2 FY27)

| Component | YoY change (Rs Cr) | Share of PBT change | Recurring? |
|---|---|---|---|
| Revenue contribution at prior ex-forex margin (397.55 x 24.93%) | +99.13 | 144.9% | Recurring |
| Margin change contribution (1,535.84 x -2.43 pp) | -37.29 | -54.5% | Recurring (mix and input cost) |
| Net forex gain change (5.23 to 10.58) | +5.35 | 7.8% | Mixed (currency, not volume) |
| D&A change | -7.29 | -10.7% | Recurring (post-capex) |
| Finance cost change | -7.16 | -10.5% | Recurring while ST borrowings stay up |
| Other income change | +14.00 | 20.5% | NON-RECURRING typically |
| Exceptional items (1.67 charge in prior year, nil now) | +1.67 | 2.4% | NON-RECURRING |
| PBT change (sum) | +68.40 | 100% | Ties: 295.96 - 227.56 |
| Tax at prior ETR on PBT change (68.40 x 25.09%) | -17.16 | | Mixed |
| ETR change effect ((24.66% - 25.09%) x 295.96) | +1.27 | | Mixed |
| Reported PAT YoY change | +52.52 (+30.81%) | | Ties: 222.99 - 170.47 |

Answers:
- Recurring core (revenue + margin + D&A + finance) = +47.39 of the +68.40 PBT change (69.3%). Forex +5.35 (7.8%), other income +14.00 (20.5%), exceptional base effect +1.67 (2.4%). About 31% of the PBT increase is non-operating or currency.
- If other income reverts to the Q2 FY26 level (16.95), PBT falls 14.00 and PAT by about 10.55 (at 24.66% ETR): run-rate PAT about 212.44, +24.6% YoY instead of +30.8%.
- D&A is near steady state: +2.64% QoQ (76.88 to 78.91), capex halved in H1. Finance cost is still ramping with short-term borrowings (Rs 234.25 Cr to Rs 461.97 Cr, res L546). Steady state depends on whether that debt is rolled or repaid.
- Tax: deferred tax is a charge in every period (C Q2 10.61, res L486); no DTA shield, no deferred credit inflating PAT (RES:F8-02). ETR is near statutory 25.17%. DENSO proceeds are taxable [ASR, call L660-661], so the close quarter will carry a non-comparable tax line (A3-F8-01).

Checkpoint: bridge presented.

## STEP 5: CASH QUALITY AND BALANCE SHEET (consolidated; H1 figures are the Reg 33 half-yearly statements)

| Metric | Prior period | Current period | Change | Verdict |
|---|---|---|---|---|
| CFO (H1) | 339.75 (H1 FY26, res L591) | 593.53 (H1 FY27, res L591) | +74.70% | Strong as printed |
| CFO / PAT (total) | 1.16x (339.75 / 292.17) | 1.48x (593.53 / 401.50) | +0.32x | Passes the >= 1.0x leg as printed |
| CFO / PAT ex trade-payables movement | 1.00x ((339.75 - 46.45) / 292.17) | 0.78x ((593.53 - 278.79) / 401.50) | -0.22x | FAILS ex-payables; quality worse than last year |
| Capex (payments for PPE, intangibles, CWIP) | 307.59 (res L592) | 148.50 (res L592) | -51.72% | Halved |
| FCF (CFO - capex) | 32.16 | 445.03 | +412.87 | Ties deck FCFO 4,456 mn (deck L442) on a net-capex basis: 1,485.04 - 6.27 sale proceeds = 1,478.77 mn (res L592-593; deck L448 shows 1,479) |
| Working capital change (net movements) | (94.09) | (11.08) | +83.01 | Payables +278.79 offset inventory (176.23), receivables (58.53), other assets (47.57) (res L581-588) |
| Receivable days | 94.4 (Mar-26: 1,150.71 / 4,449.46 x 365) | 76.2 (Sep-26: 1,185.29 / H1 rev annualised 5,674.08 x 365) | -18.2 days | Improved (annualised H1 basis; seasonality caveat) |
| Inventory days (on materials + inventory change) | 107.2 (615.59 / 2,096.84 x 365) | 100.1 (785.65 / 2,865.74 annualised x 365) | -7.1 days | Improved slightly; inventory +27.6% in rupees |
| Payable days (on same cost base) | 80.5 (462.23 / 2,096.84 x 365) | 93.3 (732.56 / 2,865.74 x 365) | +12.8 days | Stretch on suppliers |
| Cash conversion cycle | 121.1 days | 83.0 days | -38.1 days | Improved; one-third of the gain is payables |
| PPE | 1,574.35 (res L516) | 1,553.85 | -20.50 | Depreciation exceeds additions |
| CWIP | 135.57 (res L518) | 208.28 | +72.71 | Build ongoing; subsidiary CWIP 77.63 (C - SA) |
| Intangible assets under development | 291.18 (res L521) | 305.81 | +14.63 | Subsidiaries hold 299.66 (RES:F12-01) |
| Gross borrowings (current + non-current) | 242.68 (res L540, L546) | 469.40 | +93.42% | ST borrowings doubled |
| Cash, bank, current investments (narrow, filed BS) | 848.26 (res L528, L530, L531) | 1,323.92 | +475.66 | |
| Net debt / (net cash), narrow filed basis | (605.58) | (854.52) | more net cash | Excludes other current financial assets and leases |
| Net debt / (net cash), deck basis (cash, FDs, MF) | (1,026.3) (12,690 mn opening, deck L448, less 242.68) | (1,496.1) (19,655 mn closing, deck L446, less 469.40) | | Deck net debt / LTM EBITDA (0.93)x to (1.17)x (deck L479) ties: 1,496.1 / LTM EBITDA 1,274.09 = 1.17x |
| Promoter pledge | ND in this corpus ("no pledge" [NOTION MEMORY]) | ND in this corpus | ND | Not in filing |

Standalone cash (both, always): CFO 548.18 (res L259) / PAT 417.48 = 1.31x; ex-payables (548.18 - 245.66) / 417.48 = 0.72x (A3 printed 0.73x; my arithmetic and A5 both give 0.72x). Ex-dividend PAT basis (417.48 - 59.46 = 358.02): 1.53x. SA capex 116.87 (res L260); SA FCF 431.31. SA ST borrowings 219.00 to 384.85 (res L213).

Mandatory questions:
- Pillar 2 band: as printed CFO/PAT 1.48x sits at the top band; ex-payables 0.78x sits near the 0.80x band. FY26 was 1.05x and the page set Cash Multiplier 0.85x [NOTION MEMORY]. PILLAR FLAG: two readings, 1.48x vs 0.78x, separated by whether the payables build holds at FY27 year end. Recompute deferred (OR-30). Operator ruling on the cash-leg basis is still pending.
- WC drag structural or growth-induced: receivable days fell 18 days and inventory days fell 7 days while revenue grew 42%. The inventory rupee build (+176.23) is growth-induced. The CFO strength leans on payables (+12.8 days, MSME payables +52.3%, res L548). If growth stopped, receivable and inventory days would likely stay near current levels and payables would likely normalise down, so CFO/PAT would fall toward the ex-payables reading [INFERENCE]. Rating-agency commentary on structural WC: India Ratings AA+/Stable affirmed 25-Jun-2026, cites customer concentration and forex; silent on WC days [NOTION MEMORY].
- CWIP capitalisation: no major commissioning in H1; CWIP rose 72.71 while PPE fell 20.50. Nothing was projected to commission in H1 on the page. Not a red flag this half.
- Net debt: net cash rose on the deck basis (1,026.3 to 1,496.1) even as gross borrowings rose 226.72. The group borrowed short-term while building treasury (RES:F12-02, P-A3-F17-02). Notion projection for net debt: ND, not on page. Finance cost will keep running near 12 Cr a quarter while the debt stays.

Cash-conversion classification: INDETERMINATE-WITH-DIRECTION. Direction is positive as printed (1.48x, receivable and inventory days down), but the quality rests on a 278.79 payables build and one half-year reading. Missing evidence that would resolve it: FY27 full-year CFO and payables days at 31-Mar-2027 (Q4 FY27 results, about May 2027). Per house rule this caps the verdict at no better than PROCEED WITH CAVEATS.

Checkpoint: cash table and answers shown.

## STEP 5.5: DOWNSTREAM SIGNAL RECONCILIATION

### 5.5A Tracker pull
Tracker rows not supplied. The Notion page has no Downstream Signals property linked ("No Downstream Signals property, so no tracker rows linked" [NOTION MEMORY]).

| Signal name | Type | Cadence | Latest observation | Direction | Thesis element | Health |
|---|---|---|---|---|---|---|
| ND (tracker rows not supplied) | ND | ND | ND | ND | ND | ND |

FLAG: fewer than three signals for this company. The quarterly review is the checkpoint to reopen Role 5.5 for SONACOMS.

### 5.5B Reconciliation
Not computable: no signal readings. Target reported: STRONG on revenue (+34.92% YoY), WEAK on margin (-219 bps YoY). Signals said: ND.

### 5.5C New signal candidates (payload rows only; written only through the operator-approval gate; Decision Status never written)
No tracker write this run. Candidates surfaced by this quarter, proposed as Case B (create new) for operator approval:
1. India E2W/E3W traction-motor end demand (Vahan registrations, monthly). Reason: 2W/3W traction motors drove the quarter ("almost 50% quarter on quarter" [ASR, call L060]); E2W/E3W share of revenue 10% in FY26 to 14% in H1 FY27 (deck L297); Rs 16.3 bn of Q2 order additions are 2W motors and controllers (deck L201-203).
2. Consolidated op EBITDA margin incl. and ex-forex (quarterly). Reason: the gate variable needs a defined basis (pending ruling). Already proposed on 26-Oct [NOTION MEMORY].
3. Trade payables and short-term borrowings vs CFO (half-yearly). Reason: cash leg passed on payables. Already proposed on 26-Oct [NOTION MEMORY].
4. DENSO JV1 close event (event-driven). Reason: guided end-Dec 2026, may slip to Jan 2027 [ASR, call L439-440]; breaks like-for-like.
5. Steel, copper and freight cost indices (monthly). Reason: management names West Asia war, steel, copper, oil derivatives and freight "nearly doubled" [ASR, call L064-067].

### 5.5D Forward-view weighting
No signal trajectory exists, so Step 6 weighs the filing alone. The single-quarter print carries more weight than it should; this is a stated limitation.

## STEP 6: RECONCILIATION VS THESIS

### Prior quarter Questions for Management: answer status (Role 4 Q1-Q12 from the Q1 review)

| Q1 FY27 question | Answer status | What was said / shown | Verdict |
|---|---|---|---|
| Q1 DENSO close date, valuation, gain P&L geography, core divestment | PARTIALLY ANSWERED | JV1 end-Dec 2026 or Jan 2027; JV2 H1 CY27; proceeds taxable [ASR, call L439-445, L660-661]. Valuation, gain line and post-close share: silent | Second call without terms |
| Q2 SA PAT premium from the dividend: recurring? | ANSWERED by the filing, not the call | No Q2 dividend; SA-C gap -12.97% (res L164, L488) | Closed |
| Q3 Margin bridge and forex quantum | PARTIALLY ANSWERED | Cause named: mix and input prices (deck L398; call L316-317 [ASR]); no bps bridge; forex amount not stated (filing shows 10.58, res L471) | Forex basis silent two calls |
| Q4 Capex envelope, CFO and CFO/PAT | PARTIALLY ANSWERED | H1 CFO 594 Cr, capex 148 Cr [ASR, call L350-354], tie to filing res L591-592. FY27-28 envelope not given | Cash disclosed; envelope silent |
| Q5 Un-normalised ROCE and path to > 18% | NOT ADDRESSED | Deck 16.4% normalised (deck L469); "return ratios continue to show improvement" [ASR, call L367] | Second call silent |
| Q6 Gross order book, discount rate, bridge | NOT ADDRESSED | Footnote method only (deck L263-266) | Second call silent |
| Q7 Single-customer concentration | NOT ADDRESSED | Suspension motors on one customer [ASR, call L417] | Silent on % |
| Q8 Quarterly BEV share and forward EV share of book | PARTIALLY ANSWERED | Quarterly BEV 51% of auto product revenue (deck L125). EV share of book 61% in deck (deck L257-258), not spoken | Deck answers; call silent |
| Q9 Novelic carrying value and impairment | NOT ADDRESSED | Name only (call L653, L757 [ASR]) | Second call silent |
| Q10 Governance: auditor signing, note-only DENSO, PR QC | PARTIALLY ANSWERED | PR dateline and disclaimer fixed (PR L62). Auditor signed before board again (res L128, L418 vs L49). Not addressed on call | Repeat inversion |
| Q11 10x bridge; firm vs indicative SOPs | PARTIALLY ANSWERED | "implies a 25% CAGR" [ASR, call L831]. SOPs still "expected" (PR L126-151) | No bridge |
| Q12 AMR timeline; India revenue share | EVADED (timeline); NOT ADDRESSED (India %) | "I don't know is the real answer" [ASR, call L772]; eastern markets "almost two thirds" [ASR, call L233] | Repeat |

Governance signal: forex basis, ROCE, gross order book, Novelic and railway P&L are now unanswered on two consecutive calls. Three consecutive evasions would trigger a Promoter Verdict review under Role 5; that point is one quarter away.

### 6A. Variance vs Notion projections

| Metric | Bear proj | Base proj | Bull proj | Actual | Lands in |
|---|---|---|---|---|---|
| Revenue (FY27 / Q2) | ND, not on page | ND, not on page | ND, not on page | Q2 1,535.84; H1 2,837.04 (res L470) | Not testable |
| EBITDA margin (gate) | < 23.0% (bear line) | ND, not on page | >= 24.5% (bull line) | 23.20% rev ops; 23.04% deck basis; 22.51% ex-forex | Between bear and bull incl. forex; BELOW BEAR ex-forex. Depends on pending ruling |
| PAT | ND, not on page | ND, not on page | ND, not on page | Owners Q2 223.40; H1 403.87 (res L496) | Not testable |
| EPS (FY29 Y3) | 12.2 | 16.0 | 20.6 | H1 FY27 diluted 6.48 (res L505); TTM owners EPS about 11.96 | Not comparable (different year) |
| Net debt | ND, not on page | ND, not on page | ND, not on page | Net cash 1,496.1 deck basis | Not testable |
| ROCE | < 14% x 2 yrs (broken) | ND | > 18% (buyable leg) | 16.4% normalised LTM (deck L469) | Between |

Probability re-weighting rule: not triggered. Only one projectable metric (margin) and it lands below bear only on the ex-forex basis (Q1 22.55%, Q2 22.51%, two quarters). If the operator rules ex-forex, the margin is below bear for two consecutive quarters on ONE metric; the rule needs two or more metrics. Flag for Role 1.

### 6B. Watchlist item status (Notion tripwires 1-10)

| # | Item | Green threshold | Red threshold | This quarter reading | Status |
|---|---|---|---|---|---|
| 1 | ROCE trajectory | > 18% | < 14% for 2 yrs | 16.4% Sep-26 normalised LTM (deck L469); 15.4% Mar-26; 18.4% Mar-25. Definition differs between deck L150 and L485 (P-A3-F14-01). Un-normalised: ND | AMBER |
| 2 | Forced block sale / control dispute | none | any | DENSO voluntary. Promoter group cast no votes on the eDrive RPT [NOTION MEMORY] | GREEN |
| 3 | Novelic KAM impairment | no impairment | > Rs 350 Cr | No impairment line. NCI-implied Novelic-group loss narrowed to about -0.91 Cr in Q2 (res L497 / 0.46, RES:F2-04). Subsidiaries hold 299.66 Cr capitalised development (res L521 vs L190) | AMBER / UNKNOWN |
| 4 | CFO/PAT sustained | >= 1.0x | < 1.0x sustained | 1.48x as printed; 0.78x ex-payables | AMBER (passes on the letter) |
| 5 | Corporate guarantee expansion | none | expansion | ND in filing | UNKNOWN |
| 6 | EBITDA margin (FY26 24.7% [NOTION MEMORY]) | recovery toward 24.7% | continued compression | 23.20% rev ops; -219 bps YoY (Q1 was -46 bps); flat QoQ | RED (compression widened YoY) |
| 7 | Working-capital stretch | days falling | days rising | Receivable days about 76 vs 94; inventory 100 vs 107; payable days up 13 | AMBER (improvement is partly payables) |
| 8 | Railway diversification | railway revenue growing | stall | Railway evidence set R (see below) | AMBER / UNVERIFIED |
| 9 | BEV anchor (order book EV share) | stable or rising | easing | EV share of book 61% (deck L257-258) from 64% Q1 and about 70% FY26 [NOTION MEMORY]: third easing. BEV revenue 51% of auto product revenue (deck L125) | AMBER |
| 10 | India revenue mix (FY26 51%) | ND | ND | Geography pie labels not recoverable (deck L280-298; M01 deck L291); "eastern markets almost two thirds" [ASR, call L233] | UNKNOWN |

Railway evidence set R (one status, used for tripwire 8, growth trigger #1 and Role 5 8A/8B; resolves A5 C1). For continued delivery: railway book Rs 9 bn (4%), executes within 12 months (deck L257, L267); air springs commercialised (PR L117), HVAC first batch and electric panels ramping [ASR, call L815-818]. Against: non-auto share of revenue fell 31% (FY26) to 29% (H1 FY27) (deck L305); the book covers about 0.77 years of FY26 annualised railway revenue [NOTION MEMORY Rs 973 Cr in 10 months; my arithmetic]; no railway order is itemised among Q2 wins (deck L190-238; PR L120-151), although the CEO lists railway products among wins without a value (call L097 [ASR]); railway revenue and PAT undisclosed on two calls (call L809-810 [ASR]); growth "dependent on whether we are successful to launch these products on time" (call L824-825 [ASR]); suspension motors already equal railway brake systems for H1 (call L242-243 [ASR], concall M05). Status: AMBER / UNVERIFIED. The trigger FIRED on the FY26 AR [NOTION MEMORY]; this quarter's evidence neither confirms continued delivery nor shows a stall.

### 6C. Thesis-broken trigger check

| Thesis-broken condition | Threshold | Current reading | FIRED? |
|---|---|---|---|
| ROCE < 14% for two consecutive years | < 14% x 2 yrs | 16.4% normalised (deck L469); FY26 15.4% | NOT FIRED |
| Forced block sale / management change from control dispute | any | None; DENSO transaction is voluntary (res L315-319) | NOT FIRED |
| Novelic KAM impairment materially exceeds Rs 350 Cr (monitored) | > 350 Cr | No impairment disclosed | NOT FIRED |
| CFO/PAT below 1.0x sustained (monitored) | < 1.0x sustained | 1.48x printed; 0.78x ex-payables (one half-year reading) | NOT FIRED (watch) |
| Corporate guarantee expansion (monitored) | expansion | ND | NOT FIRED (unverifiable) |

No thesis-broken condition has fired. No exit or AVOID reclassification is triggered by the pre-committed rules.

### 6D. Growth trigger status

| Trigger | Original confidence | Confirming evidence | Killing evidence | Updated status |
|---|---|---|---|---|
| #1 Railway diversification | ND, not on page (status FIRED in AR entry) | Railway evidence set R, "for" items (Step 6B) | Railway evidence set R, "against" items (Step 6B) | AMBER / UNVERIFIED (FIRED on FY26 AR; Q2 does not confirm continued delivery) |
| #2 BEV anchor | ND, not on page (AMBER on page) | BEV revenue 606.1 Cr, +129% YoY (deck L125, L392); 51% of auto product revenue; H1 1,041.6 Cr (deck L167) | EV share of order book 61%, third easing (deck L257-258); EV motors business moving into a 51:49 vehicle with DENSO (res L318-319), priced at about 2.2x proxy sales (DENSO economics below) | ON TRACK on revenue; WEAKENED on forward book share and ownership |
| #3 Sensors and Software / Robotics and Physical AI | ND, not on page | Robotics book Rs 13 bn, 5% (deck L257-258); 2W rear radar order Rs 1.0 bn, SOP H2 FY28 (deck L201-205) | Robotics revenue 1% of revenue (deck L311); C2 SOP not evidenced; timing withdrawn ("I don't know" [ASR, call L772]) | DELAYED |
| India 51% (labelled Trigger #3 FIRED in AR entry) | ND | Eastern markets about two thirds [ASR, call L233] | India % not recoverable this quarter (M01, deck L291) | UNKNOWN (numbering conflict on page) |

Checkpoint: 6A-6D shown.

## STEP 6.5 and STEP 7: DEFERRED TO /fttcp AND ROLE 1 (OR-30)

Step 6.5 (A21 base refresh, Expectation Ledger ageing) and Step 7 (four-pillar re-validation, Hurdle recheck) are not run here. Pillar-relevant facts flagged for /fttcp and Role 1:

| Pillar / input | Fact this quarter | Anchor | Direction of pressure |
|---|---|---|---|
| Pillar 1 ROCE (FTTCP verdict is sole authority) | 16.4% normalised LTM, up from 15.4% Mar-26; denominator definition differs on p7 and p23; railway EBIT annualised; un-normalised ND | deck L144, L150, L469, L485, L492 | Up, but sub-18% and definitionally unstable |
| Pillar 2 Cash Multiplier (page 0.85x) | CFO/PAT 1.48x printed vs 0.78x ex-payables (1.00x ex-payables a year ago) | res L585, L591, L488 | Two readings; ruling pending |
| Growth Visibility Premium | Net book Rs 251 bn = 5.6x FY26 revenue; 36 bn added, 25 bn consumed (1.6x Q2 revenue); 60% of itemised Q2 adds start FY28-FY29; EV share 61% | deck L244-258, L201-238 | Mixed: volume up, conversion lag and quality questions |
| Strategic Premium (single-credit rule) | DENSO JVs: 49% of the EV-motor carve-out sold at EV Rs 1,750 Cr, about 2.2x proxy sales vs about 10.1x for Sona (see DENSO economics below); Deming Prize (PR L110); global diff-gear share 8.8% to 8.7%, starter motors 4.4% to 4.2% in CY25 | res L315-319; deck L297, L700, L703 | Mixed; carve-out price is a value-transfer risk until carve-out earnings are known |
| A21 run-rate base | Q2 annualised owners PAT 893.60 (223.40 x 4); H1 annualised 807.74 | res L496 | Q2 run-rate is 1.40x FY26 owners PAT |
| Expectation Ledger | C1 missed, C2 not evidenced, C3 delayed (Role 5 Step 3) | call L053-057 [ASR] | Decay candidates |
| Sector cap | Manufacturing 25x; no reclassification evidence | [NOTION MEMORY] | Hold |
| UA multiplier | Not applicable per page | [NOTION MEMORY] | n/a |

### DENSO 49% stake-sale economics (A5 M2; acquisition-economics probe)

| Item | Value | Anchor / tier |
|---|---|---|
| Consideration basis | DENSO buys 49% of the 100% subsidiary that receives the EV motors and controllers business, at an Enterprise Value of Rs 17,500 mn = Rs 1,750 Cr | res L318-319 [FILED] |
| 49% at EV | Rs 1,750 Cr x 49% = Rs 857.5 Cr, before tax | my arithmetic |
| Tax | "what we get from Denso will pay tax on" | call L660-661 [ASR] |
| Equity bridge (carve-out debt or cash) | ND | not disclosed |
| Cash route | Note 5 says DENSO "will buy" 49%; whether it buys from Sona (cash to Sona) or subscribes new shares (cash stays in the vehicle) is not stated. The taxability remark implies a sale by Sona [ASR, INFERENCE] | res L319 |
| Carve-out revenue, EBITDA, PAT | NOT FOUND (Note 5 and both calls silent) | res L315-319; call L435-453 |
| EV / earnings multiple | NOT FOUND (no target EBITDA or PAT) | n/a |
| Nearest filed proxy for carve-out sales | E2W/E3W market segment 14% of H1 FY27 revenue (deck L297) x Rs 28,568 mn (deck L138) = Rs 399.95 Cr in H1, Rs 799.9 Cr annualised. This is a market segment, not the carve-out perimeter | [MGMT-FILED], my arithmetic |
| EV / proxy annualised sales | 1,750 / 799.9 = 2.19x | my arithmetic |
| Run-rate cross-check | Traction plus suspension motors Rs 1,400 Cr annualised (call L260) less suspension at about 7% of Q2 revenue (call L241; 7% x 1,546.42 x 4 = 433.0) = about Rs 967 Cr; EV / run-rate sales = 1.81x | [ASR], my arithmetic |
| Comparator: Sona at Rs 879 | (Rs 55,012 Cr market cap - Rs 1,496.1 Cr deck net cash) / TTM rev ops Rs 5,294.30 Cr = 10.1x EV / sales | [SECONDARY] market cap; res L470; deck L446 |
| Price date | EV fixed at signing on 22-Jul-2026 (res L315), three weeks into the quarter in which traction motors grew almost 50% QoQ (call L060 [ASR]), beyond management's own expectations (call L058-059 [ASR]), and before Rs 16.3 bn of 2W motor and controller order additions (deck L201-203) | [FILED] / [ASR] |
| Valuation process | Slump sale into the subsidiary at fair market value per an independent valuer's report | res L318 [FILED] |

Two readings:
- Reading A (fair price): the EV-motor unit earns thin margins ("one particular product line makes lesser margin", CFO, call L622-623 [ASR]). At 1.8-2.2x sales the price is fair; Sona's retained margin rises after close and the NCI leakage is small.
- Reading B (value transfer): Sona sells 49% of its fastest-growing engine (about +50% QoQ, call L060; Rs 16.3 bn of Q2 additions, deck L201-203) at about one-fifth of its own EV/sales multiple, on a price set before the Q2 surge.

The one observation that separates them: the carve-out's EBITDA and PAT (the independent valuer's FMV report, or the first post-close NCI or equity-income line). Until then the price cannot be called fair or cheap.

Cash cap: any bull case for DENSO cash caps at Rs 857.5 Cr before tax, and only if DENSO buys from Sona. The analyst's Rs 900 Cr (call L649 [ASR]) exceeds the EV-implied gross unless the carve-out holds net cash (ND). Management neither confirmed nor corrected it.

Railway acquisition (Note 2) for comparison: consideration Rs 1,642.63 Cr (res L305); target PAT NOT FOUND in this corpus; sales proxy about 1.4x annualised [NOTION MEMORY Rs 973 Cr in 10 months]. No further graft.

## STEP 8: POSITION DECISION

Decision Status verified: WATCHLIST (Notion property, fetched 28-Oct-2026). Not held. Branch 8A-W.

8A-W logic:
- Thesis-broken FIRED? No.
- Below bear on 2+ key metrics? No. One projectable metric (margin) lands below bear only on the ex-forex basis.
- Between bear and base? Margin lands between bear and bull on the forex-inclusive basis; base margin projection ND, not on page.
- Output: revise projections down on margin (the page already planned a downward tilt). Entry zone recompute is deferred to Role 1 (OR-30). Gate: the Q2 master gate did not clear for re-rating and did not fire the bear line unless forex is excluded. Proposed next gate: Q3 FY27 results (about late January 2027), with the margin basis ruled first.
- Proposed Decision Status change: none. No pre-committed trigger fired. The operator sets status.
- Price context: CMP Rs 879 is 2.29x the page's base FV Rs 384 and 4.75x the Rs 185 buyable line (my arithmetic on page values). The quarter cannot make the stock buyable at this price; it can only move fair value.

### 8B. Trigger refinement (proposals; operator decides)
- Original add-back / buyable trigger: CMP <= Rs 185 AND ROCE > 18% AND Novelic resolved [NOTION MEMORY].
- Revised trigger proposal: add (a) margin measured on revenue from operations ex-forex, (b) CFO/PAT ex-payables >= 1.0x on a full year, (c) DENSO post-close accounting known (subsidiary with NCI vs equity-accounted JV), (d) carve-out EBITDA and PAT disclosed so the DENSO price can be judged.
- Trim ladder: not applicable (not held).

### 8C. Single cleanest metric for Q3 FY27
Consolidated operating EBITDA margin on revenue from operations, reported both incl. and ex-forex, Q3 FY27 (results about late January 2027).
- Bull threshold: >= 24.0% incl. forex with trade payables flat or down at 31-Dec (pass-through real).
- Bear threshold: < 23.0% incl. forex, or < 22.5% ex-forex, or a payables unwind that takes 9M CFO/PAT below 1.0x.
Caveat: if DENSO JV1 closes inside Q3 under joint control, Q3 is not like-for-like; then use the margin ex the EV-motors perimeter, which only management can supply.

## STEP 8.5: QUESTIONS FOR MANAGEMENT

The Q2 call has happened (26-Oct). Channel: IR email now with all questions; the top three to the Q3 live call. Every A3 FORWARD-SIGNAL and AMBIGUOUS finding maps to at least one row below.

| # | Question | Cat | Why it matters | Bull answer | Bear answer | From finding IDs |
|---|---|---|---|---|---|---|
| 1 | Note 5 calls the DENSO vehicle both "Joint Ventures" (res L315) and "this subsidiary" (res L319). After JV1 closes (guided end-Dec 2026 / Jan 2027 [ASR]), will Sona consolidate the EV-motors entity at 51% with 49% NCI, or equity-account it? Name the entity (Sona Comstar eDrive Pvt Ltd or Sona BLW eDrive Mexicana). | E | Decides whether revenue and EBITDA stay in the consolidated base and whether a remeasurement gain hits consolidated P&L | Subsidiary at 51%, consolidated, NCI only; entity named | Joint control, deconsolidated, equity-accounted; revenue base drops | RES:F1-02, RES:F15-02, RES:F6-01, A3-F6-03, A3-F17-08, P-A3-F17-03, A3-PR-F16-04 |
| 2 | State the carve-out's FY26 and H1 FY27 revenue, EBITDA and PAT used by the independent valuer for the EV Rs 1,750 Cr (res L318-319). Does DENSO buy its 49% from Sona or subscribe new shares? What gain do you expect, on which line (standalone exceptional, consolidated P&L or equity), what tax on the proceeds, and what net cash? Analyst cited Rs 900 Cr by year end [ASR, call L649], above the EV-implied Rs 857.5 Cr before tax; confirm or correct. Where are the Q2 deal costs (no exceptional booked, res L482)? | F | Price fairness (about 2.2x proxy sales vs about 10.1x for Sona), one-off size and line, year-end cash | Thin-margin unit at a fair multiple; secondary sale; gain in SA exceptional only; tax quantified | High-margin unit sold at a low multiple; primary subscription (cash stays in the vehicle); deal costs buried in other expenses | RES:F1-01, RES:F7-01, A3-F8-01, A5 M2 |
| 3 | State the royalty rate, base and term each partner receives from its majority-owned JV. | C | Net margin effect on Sona and on equity income | Royalty net positive to Sona | Net royalty outflow from Sona's 49% JV exceeds inflow | RES:F6-02 |
| 4 | What share of Q2 revenue from operations (Rs 1,535.84 Cr) and of the Rs 16.3 bn 2W traction-motor and controller order additions sits in the business DENSO will own 49% of? Which subsidiary generated the Rs 39.06 Cr ex-forex op EBITDA of the subsidiary layer in Q2? | E | 45% of Q2 order additions may sit in the carve-out; NCI leakage size | Small share; subsidiary layer is outside the carve-out | Large share; the growth engine moves into a 51:49 vehicle | RES:F2-02, RES:F3-01, P-A3-F16-04, P-A3-F6-01, A3-PR-F6-01 |
| 5 | Q2 deck and press-release revenue (Rs 1,546 Cr; PR L69) includes net forex of Rs 10.58 Cr (res L471). State Q2 EBITDA and margin ex-forex. For H1, the cash flow adds back an unrealised forex loss of Rs 11.67 Cr (res L579) while the H1 P&L shows a net forex gain of Rs 19.75 Cr (res L471): what is realised forex in H1, and in Q2? | C | The margin gate basis is pending an operator ruling | Ex-forex margin >= 23.0% | Ex-forex 22.5% confirmed; realised forex larger than the P&L line | RES:F2-05, P-A3-F16-01, A3-PR-F14-01, A3-F17-07 |
| 6 | The CFO gave "around 23%" with a 10-20 bps tolerance [ASR, call L632-634]. What does the five-year margin exercise (call L616) show for FY28? At what steel/copper path does the margin return to 24%+, given full pass-through lowers the % margin (call L865-868 [ASR])? How many bps of Q2 margin did robotics R&D cost (call L751 [ASR])? Why does the deck understate the H1 margin decline (~1.5% stated vs 1.6 pp)? | C | Whether 23% is a floor or a ceiling | FY28 >= 24% with a dated input-cost path | 23% is the ceiling; mix keeps it there | A3-F6-02, A3-F7-01, A3-F7-02, A3-F6-06, P-A3-F14-03 |
| 7 | Freight "nearly doubled" QoQ [ASR, call L066-067]. Is freight passed through, and how much of the +20.9% QoQ other-expense rise (228.91 to 276.71, res L479) is freight? | C | A separate unrecovered % headwind | Passed through with a lag | Not passed through | A3-F7-05 |
| 8 | Consolidated warranty provision rose to Rs 12.49 Cr (H1 FY26 Rs 2.18 Cr; res L576), of which subsidiaries Rs 4.86 Cr; slow-moving inventory provision Rs 8.02 Cr (Rs 1.20 Cr; res L573). Which products and entities, and are they recurring? | D | About 70 bps of H1 margin [NOTION MEMORY]; product-quality signal in a Deming-award quarter | One-off, specific program, closed | Recurring; quality issue in a growing product line | RES:F12-03, A3-PR-F17-04, A3-F17-10 |
| 9 | Trade payables rose Rs 278.79 Cr in H1 (res L585) and short-term borrowings rose from Rs 234.25 Cr to Rs 461.97 Cr (res L546) while treasury rose. Why borrow while holding about Rs 1,966 Cr gross cash [ASR, call L361]? Tenor, rate, purpose? What is 9M CFO/PAT ex-payables? Are MSME dues (Rs 145.15 Cr, +52%) within 45 days? What is FCFO in rupees for FY26, to test the "1.5x" claim (PR L97-98)? | D | Cash leg passed on payables (0.78x ex-payables) | Export packing credit arbitrage; payables days hold | WC funded by suppliers and banks; payables unwind | RES:F12-02, P-A3-F17-02, A3-F17-04, A3-PR-F16-03 |
| 10 | Name the WOS that paid the Rs 59.46 Cr dividend (res L320), the subsidiary that received the Rs 33.05 Cr injection (res L265), and the subsidiary whose short-term borrowings rose from Rs 15.25 Cr to Rs 77.13 Cr. Is there an intra-group loan from a subsidiary to the parent (consolidated interest paid Rs 8.41 Cr is below standalone Rs 9.15 Cr, res L615 vs L284)? | D | Group-level circularity: debt-funded dividend | Unrelated entities; no intra-group loan | Same entity borrowed, paid the dividend and got capital back | RES:F2-03, RES:F2-06 |
| 11 | Name the five foreign subsidiaries reviewed by the other auditor (assets Rs 200.74 Cr, H1 loss Rs 2.42 Cr; res L388-394). What is the Novelic carrying value and the impairment test result? Which entity holds the Rs 299.66 Cr of capitalised development in subsidiaries (res L521 vs L190) and the Rs 77.63 Cr subsidiary CWIP? | G | Tripwire 3; asset first in line for impairment | Novelic losses narrowing (NCI-implied -0.91 Cr Q2); headroom on test | Capitalised development in a loss-making layer; impairment risk | RES:F3-02, RES:F12-01, RES:F2-04, A3-F17-06 |
| 12 | Give un-normalised ROCE and ROE at 30-Sep-2026. Which footnote is correct: p7 "capital deployed for acquiring NOVELIC" (deck L150) or p23 "NOVELIC and Railway Business" (deck L485)? Dated path to > 18%? | F | Pillar 1 input and buyable leg | Un-normalised >= 16%; path dated | Un-normalised materially below 16.4% | P-A3-F14-01, A3-F17-05 |
| 13 | What is the gross order book before the delay discount and EOL haircut (deck L263-266)? Define "consumed": Rs 25 bn consumed against Rs 15.5 bn revenue (1.6x) in Q2 (deck L248). Itemise the Rs 4.8 bn of unitemised additions (Rs 6.8 bn on press-release items). Why does the robotics book rise to Rs 13 bn with no itemised robotics win? Reconcile the p13 heading Rs 6.6 bn with tiles summing to Rs 6.9 bn. What does the asterisk on "net order book*" (PR L83) refer to? | E | Order-book quality; growth visibility pillar | Consumption equals revenue plus scheduled EOL; adds itemised | Consumption includes write-downs; unitemised adds are re-estimates | P-A3-F7-01, P-A3-F16-03, A3-PR-F14-03, A3-PR-F14-04, A3-F14-03 |
| 14 | The release reports "EV and Robotics and Physical AI" at 65% of the book (PR L83); the deck shows EV-only 61% (deck L257-258). Why change the metric, and what is the EV-only share trend? | E | Tripwire 9 numerator change | EV-only stable from here | EV-only keeps easing | A3-PR-F16-01, A3-F17-03 |
| 15 | Are the seven SOP dates (H2 FY27 to H1 FY29; deck L205, L238) firm or indicative? What is the FY27-FY28 capex envelope given H1 capex of Rs 148.50 Cr (res L592), about 5.2% of annualised revenue? How much capital is blocked for JV2 [ASR, call L662]? | F | 60% of Q2 itemised wins start FY28-FY29; capacity funding | Firm dates; capex inside a stated envelope | Capex step-up later, or capacity sits off Sona's books | P-A3-F6-02, A3-PR-F6-02, P-A3-F16-08 |
| 16 | Which four programs entered production in Q2 (not-yet-in-production stayed at 31; deck L174)? Did any robotics SOP occur in Q2 (Q1 promise C2: one this quarter, one next, one within 15 months)? If not, the new date. | B | C2 scoring; robotics timing withdrawn | Robotics SOP occurred; dated next steps | No SOP; no date | P-A3-F16-09, P-A3-F17-05, A3-PR-F17-02, A3-F17-02, A3-F7-04 |
| 17 | Define "commercialised" for the helical LSD, air springs and rear radar (PR L116-118). For each: customer, Q2 revenue booked, SOP date. Is the 2W rear radar the "ADAS short-range radar" promised for Q1 (C3)? | B | C3 scoring; LSD SOP is H1 FY29 and radar SOP H2 FY28 (deck L205) | Revenue booked in Q2 with an earlier customer | Order won only; production years away | P-A3-F6-03, A3-PR-F14-05 |
| 18 | State H1 BEV revenue in Rs Cr and its share of total revenue. The deck shows Rs 1,041.6 Cr (deck L167); the call said "2,042 crores" [ASR, call L328]. The CEO cited 51% as share of automotive revenue, of automotive product sales and of revenue (call L131, L311, L775 [ASR]). | A | EV dependence of the whole company (BEV is about 39% of total Q2 revenue on deck figures) | 51% of automotive only; total share stated | Basis drift persists | A3-F14-01, A3-F14-02 |
| 19 | Railway revenue and PAT for H1 FY27? The Rs 9 bn railway book executes within 12 months (deck L267): what fresh PO intake is needed to grow FY28? | A | Tripwire 8 and growth trigger #1 (AMBER / UNVERIFIED); Head of Railway declined guidance [ASR, call L809] | Railway revenue and PAT disclosed and growing | Book covers under a year; growth depends on launches | P-A3-F6-04, A3-F17-09 |
| 20 | Suspension motors are about 7% of revenue [ASR, call L241] on one customer and one model [ASR, call L417]. Share of Q2 revenue from that customer? When will a second customer start? | E | Single-point concentration | Second customer dated | Model cycle risk on 7% of revenue | A3-F7-03 |
| 21 | Is the 1.5x cash/EBITDA threshold [ASR, call L698-700] on gross or net cash, trailing or forward EBITDA? Gross cash is already about 1.5x annualised H1 EBITDA. What happens when it is crossed with DENSO proceeds? | F | Capital-allocation decision inside 12 months | Return of capital or accretive M&A on the four filters | Large M&A outside the core | A3-F6-04 |
| 22 | Which motor product launches in Q3 FY27 [ASR, call L561-562], and what is the 3W share of traction-motor revenue ("pretty small so far", call L558)? | B | Scorable Q3 commitment | Named product, shipped in Q3 | Slips | A3-F6-05 |
| 23 | The "10X ambition" (PR L99): 10x of what metric, from which base year, by when (FY35 in the Q1 release [NOTION MEMORY]; "10x over 10 years", call L046 [ASR])? | B | Undated aspiration used to frame growth | Metric and base stated | Stays undated | A3-PR-F6-03 |
| 24 | Both review reports were signed at 13:26:32 and 13:27:12 (res L128, L418) and state the Statement was "approved by" the Board, which met at 14:00 (res L49). This is the second quarter running. What did the auditor sign against, and will the sequence change? | G | Governance pattern | Process explanation; sequence fixed from Q3 | No answer; repeats | RES:F14-01 |

Top 3 by likelihood of thesis-changing information:
- Q1 (DENSO accounting and entity): the answer changes the consolidated revenue and EBITDA base used for every forward number, and so the bull case.
- Q9 (payables and borrowings): the answer confirms or kills the cash leg (1.48x vs 0.78x), the bear case's main evidence.
- Q24 (auditor signing sequence): a test of management transparency against the TRUSTWORTHY promoter verdict.

Channel: the Q2 concall has already occurred without these answers. Send an IR email with all 24 questions verbatim now; carry Q1, Q6 and Q9 to the Q3 live call.

## STEP 9: NOTION UPDATE (payload only; not written by A4)

Under /run-quarterly, Notion is written only after the operator approves the printed payload in this run. Decision Status is never written.
- Proposed Key Notes prepend: "28-Oct-2026 | Q2 FY27 full review (filing + deck + PR + ASR call): consol rev ops Rs 1,535.84 Cr +34.9% YoY; owners PAT Rs 223.40 Cr +29.3%; op EBITDA margin 23.20% rev ops / 22.51% ex-forex (-219 / -243 bps YoY); parent margin -343 bps. CFO/PAT H1 1.48x printed, 0.78x ex-payables (1.00x a year ago). C1 MISSED (conceded on call), C2 not evidenced (scored DROPPED), C3 DELAYED: provisional credibility 8.3% on 3 scored commitments, grade D, archetype EVASIVE (one quarter only). DENSO JV1 close guided end-Dec/Jan [ASR]; accounting route unstated; 49% priced at EV Rs 1,750 Cr (about 2.2x proxy sales vs about 10.1x for Sona), carve-out earnings NOT FOUND. Railway AMBER / UNVERIFIED. No thesis-broken trigger fired. Decision Status unchanged (operator-only)."
- Row properties proposed: none changed by A4. Management Grade change is flagged, not proposed as decided.

---

# SECTION B: CONCALL ANALYSIS (ROLE 5)

Source class reminder: MACHINE ASR transcript. Every concall-only number below carries [ASR]. Filed documents win on conflict.

## STEP 0: PRE-FLIGHT

### 0A. Notion
Growth triggers, thesis-broken conditions, checklist, Promoter Verdict TRUSTWORTHY, Mgmt grade A (AR entry), prior concall log C1-C9 and N1-N14: all loaded from the page [NOTION MEMORY]. Devil's Advocate expected-evasion list: ND, not on page. This is the second tracked concall; the Q1 call set the baseline.

### 0B. Participants (call L015-025)

| Role | Name | Notes |
|---|---|---|
| Hosting broker / IR | Kapil Singh, Nomura (Deputy Head of Research India, Lead Auto Analyst) | Hosted; asked no question this time (Q1: led with a substantive one [NOTION MEMORY]). House-broker status: ND |
| CMD / Chairman | ND (not on call) | Promoter group (Aureus 28.02% [NOTION MEMORY]) has no named representative on the call. The page previously treated the MD as present leadership with no absence flag; operator to confirm whether this is a yellow flag |
| Managing Director and Group CEO | Vivek Vikram Singh | Present and dominant (ASR self-name "Gopal", call L029) |
| CEO, Driveline | Vikram Verma (Whole-Time Director) | Introduced; no clearly attributed turn |
| CEO, Motor Business | Satmohan Gupta | JV2 date, traction motors |
| CFO | Rohit Nanda | Financials, margin range, pass-through. No CFO-on-operations flag: he answered financial questions |
| CTO | Praveen Rao | Prepared remarks on new products |
| Head, Railway | Amit Mishra | Spoke this time (Q1: 0 turns), declined guidance |
| IR | Ankit Agarwal | No turn |
| Head Strategy and M&A | Prateek Sachan | No turn |

Yellow flags: none for an undisclosed new face. No IR-firm dominance.

### 0C. Structure
- Call 26-Oct-2026 17:00 IST; board concluded 16:05 (res L50): same day, so canned.
- Duration 63.6 min (3,818 s, call L001). Q&A [00:26:23] to [01:02:26] = 36.1 min = 57% of time (59% of lines, ledger).
- Analysts: 5 named (firms NOT FOUND) plus 3 chat questions; 18 asks in total.

### 0D. Safe harbour and caveats
Forward-looking caveat refers to the deck disclaimer (call L007-010). Customer-confidentiality rule: no customer names (call L011-014). Prior-call caveat text verbatim: ND (no prior extract), so new caveats cannot be diffed. The customer rule was later broken by the CEO (call L402-403, A3-F14-04).

### 0E. Business type
Standard operating business.

## STEP 1: OPENING REMARKS, CLAIMS INVENTORY (T03-T05)

| # | Claim | Type | Quantified? | Source line |
|---|---|---|---|---|
| 1 | "Q2 was almost a perfect quarter for us across all metrics" | Strategic | NO | call L032 |
| 2 | Highest ever revenue; BEV more than half of automotive revenue | Backward | YES | call L035-039 |
| 3 | Three new products commercialised, most ever in a quarter | Operational | YES | call L040-041, L098-105 |
| 4 | Third highest order additions | Customer/Order | YES (rank) | call L042-043 |
| 5 | 10x over 10 years ambition; Q2 raises confidence | Forward Soft | YES (10x) | call L045-049 |
| 6 | Margin pressure continued, "mainly driven by change in product mix"; Q1 pass-through promise acknowledged | Backward | NO | call L053-057 |
| 7 | Traction motor business grew almost 50% QoQ | Backward | YES [ASR] | call L060 |
| 8 | Steel, copper, oil-derivative inflation; freight nearly doubled QoQ | Macro | YES (freight) [ASR] | call L063-067 |
| 9 | Near-term margin predictability "a little difficult"; absolute margins improve | Forward Soft | NO | call L069-072 |
| 10 | EV business +129% YoY; India E2W/E3W the biggest reason | Backward | YES | call L076-078 |
| 11 | Suspension motor, fastest growing, driven by success in China | Backward | NO | call L083-084 |
| 12 | Highest ever FCFO; H1 more than 1.5x FY26 FCFO | Backward | YES | call L109-112 |
| 13 | Deming Prize to Driveline division | Operational | YES (binary) | call L114-115 |
| 14 | Revenue +35%, EBITDA +23%, PAT +29% | Backward | YES | call L122-124 |
| 15 | BEV revenue +40% sequentially; US EV deliveries unchanged | Backward | YES [ASR] | call L134-136 |
| 16 | Q2 EBITDA Rs 356 Cr | Backward | YES | call L142 |
| 17 | Return ratios improved and expected to keep improving | Forward Soft | NO | call L152-153 |
| 18 | First priority broadened to "EPIC mobility" | Strategic | NO | call L155-157 |
| 19 | 75 EPIC programs across 37 customers; 44 in production, 31 not yet | Customer/Order | YES | call L169-172 |
| 20 | Q2 wins: helical LSD, rear radar (new customer), IMC, traction motor volumes, ICE diff assembly, starter motor, diff gears | Customer/Order | NO (no values spoken) | call L175-212 |
| 21 | Rs 36 bn new business; net order book Rs 251 bn; robotics 4% | Customer/Order | YES [ASR units] | call L215-222 |
| 22 | Eastern markets almost two thirds of revenue | Strategic | YES (approx.) | call L230-233 |
| 23 | Suspension motors about 7% of revenue | Backward | YES [ASR] | call L239-241 |
| 24 | DA plus DG +37% YoY | Backward | YES [ASR] | call L248-250 |
| 25 | Traction plus suspension motors annualised run-rate Rs 1,400 Cr | Backward | YES [ASR] | call L256-260 |
| 26 | E2W/E3W 14% of revenue; auto/non-auto 70:30 | Backward | YES | call L274-276 |
| 27 | CFO: revenue Rs 1,546 Cr +35%; EBITDA Rs 356 Cr; margin 23%, lower by 2.3%; PAT "23 crores", margin 14.4% | Backward | YES [ASR; PAT digit dropped] | call L305-321 |
| 28 | CFO: H1 revenue Rs 2,857 Cr +43%; BEV "2,042 crores", 48%; EBITDA Rs 659 Cr, 23.1%; PAT Rs 404 Cr | Backward | YES [ASR; BEV figure conflicts with deck] | call L327-340 |
| 29 | CFO: CFO Rs 594 Cr = 90% of EBITDA; WC release Rs 44 Cr; capex about Rs 148 Cr; FCF Rs 446 Cr | Backward | YES [ASR] | call L350-354 |
| 30 | CFO: dividend Rs 112 Cr; borrowings Rs 224 Cr; ESOP Rs 108 Cr; finance income Rs 32 Cr; cash and investments Rs 1,966 Cr | Backward | YES [ASR] | call L356-361 |
| 31 | CFO: return ratios improve "every quarter"; net debt/EBITDA negative | Forward Soft | NO | call L367-369 |

Diagnostics:
- Quantified: 23 of 31 (74%). Unquantified: 8. Most quantified items are backward-looking; forward items in the opening are almost all unquantified (claims 5, 9, 17, 31).
- New vs reaffirmed: new are the mix explanation, freight, EPIC broadening, suspension 7%, motors Rs 1,400 Cr run-rate. Reaffirmed: 10x ambition, return-ratio improvement.
- Quietly dropped: C2 robotics SOP dates (not mentioned in the opening or anywhere); DENSO not mentioned in the opening at all.
- Internal contradiction: "almost a perfect quarter" (call L032) vs "continued margin pressure" (call L055) and a self-declared miss on the Q1 margin promise (call L053-057).

## STEP 2: FORWARD GUIDANCE

| Metric | This quarter's guidance | Last quarter's (Q1 call [NOTION MEMORY]) | Two quarters ago | Trajectory | Confidence |
|---|---|---|---|---|---|
| Revenue growth (FY27) | No FY27 number; "25% CAGR" medium-term implied by the aspiration [ASR, call L830-838] | No explicit number; TAM aspirations | ND (no tracked call) | New (medium-term only) | LOW |
| Revenue growth (FY28) | Same 25% CAGR medium-term | none | ND | New | LOW |
| EBITDA margin band | 23-25% range held; "around 23%", 10-20 bps tolerance; holds "unless oil goes to 150" [ASR, call L610-638] | No band; recovery "from Q2" but pressure "may continue" | ND | Widened downward in practice (range kept, working point at the floor) | MEDIUM |
| Order book / pipeline | Net Rs 251 bn; robotics 4% [ASR]; deck 5% | Net Rs 240 bn [deck L248]; EV 64%; robotics 3% | ND | Maintained (level up, EV share down) | MEDIUM |
| Capex envelope | Robotics Rs 62 Cr "should cover it" [ASR, call L762-763]; JV2 capital to be blocked; no total | Intensity ratios only | ND | Maintained (no envelope) | LOW |
| Utilisation target / timeline | ND | ND | ND | n/a | ND |
| Strategic order execution timeline | JV1 close end-Dec 2026, may slip to Jan 2027; JV2 close H1 CY2027 [ASR, call L439-445] | JV2 SOP refused (confidentiality) | ND | New (dated) | MEDIUM |
| Working capital / CCC band | none; "release of 44 crores" backward [ASR] | debtor days "significant reduction" claimed | ND | Maintained (none) | LOW |
| Net debt trajectory | "substantial cash balance at the end of the year"; cash/EBITDA 1.5x threshold [ASR, call L663-700] | "continues to be negative" | ND | New threshold | MEDIUM |
| Export / segment guidance | Railway: no guidance by policy [ASR, call L809-810]; Europe more business [ASR, call L498-501] | none | ND | Maintained (none) | LOW |
| New product / contract milestones | Motor product launch in Q3 FY27 [ASR, call L561-562]; Bharat Expo robotics demo Feb 2027 [ASR, call L766]; deck SOPs H2 FY27 to H1 FY29 | Robotics SOPs 1 this quarter / 1 next / 1 within 15 months | ND | Robotics dates WITHDRAWN; motor launch new | MEDIUM (motor) / LOW (robotics) |
| Dividend / payout policy | ND | ND | ND | n/a | ND |

Diagnostics:
- Widened or tightened: the range was kept but the CFO placed the working number at its floor with tolerance below it. That is a de facto widening downward.
- Dropped without acknowledgment: the robotics SOP dates (C2). Five robotics questions, no SOP status (Q05, Q12-Q14, Q18).
- Internal consistency: 25% revenue CAGR plus a 23% margin plus a Rs 251 bn book (5.6x FY26 revenue over 10 years, deck L244) is arithmetically compatible at the revenue level; the margin path depends on mix, which management says pulls down (call L621-623 [ASR]).
- Versus Four-Pillar projections: base margin projection ND on page; the gate bear line is 23.0%, and the CFO's ballpark sits on it.
- Refused: robotics inflection year (call L772); railway growth (call L809); 3W size (call L558-561); suspension pipeline (call L427-428); DENSO price basis (carve-out earnings) never offered.

## STEP 3: PROMISE VS DELIVERY AUDIT

### 3A. Q1 commitments scored (quantified or dated items only; C4-C9 were unquantified or undated)

| Commitment from Q1 FY27 call (23-Jul) | This quarter's actual | Status | Points |
|---|---|---|---|
| C1 Cost pass-through recovery "progressively more visible from Q2" | Margin 23.20% vs Q1 23.26% (rev ops); management conceded "continued margin pressure" (call L053-057 [ASR]); deck names input prices (deck L398) | MISSED | 0 |
| C2 Robotics SOPs: one this quarter (Q2), one next, one within 15 months | No robotics product among Q2 commercialisations (PR L116-118); robotics revenue 1% (deck L311); never addressed in five robotics questions; timing withdrawn ("I don't know", call L772) | DROPPED (quiet, no acknowledgment) | 0 + governance flag |
| C3 ADAS short-range radar "under commercialisation this quarter" (Q1) | 2W rear radar commercialised in Q2 (PR L117-118; deck L367), one quarter late; whether it is the same product is not stated (the deck lists short-range radar separately, deck L363-364) | DELAYED (first delay) | 0.25 |
| C7 2W/3W India traction share 25% to > 50% | Wallet share up (call L549 [ASR]); no % | UNCLEAR | excluded |
| C8 10x over the decade | Reaffirmed; not measurable | UNCLEAR | excluded |

Alternative scoring (stated, not adopted): C2 as UNCLEAR and C3 as PARTIALLY DELIVERED gives 0.5 / 2 = 25%. Both scorings give grade D.

### 3B. Cumulative track record

| Concall date | Total commitments | Delivered | Partially | Missed | Delayed | Dropped | Unclear | Points |
|---|---|---|---|---|---|---|---|---|
| 23-Jul-2026 (Q1, baseline) | 9 registered | not scored | not scored | not scored | not scored | not scored | not scored | baseline |
| 26-Oct-2026 (scoring Q1 items) | 5 | 0 | 0 | 1 | 1 | 1 | 2 | 0.25 |

Credibility ratio = 0.25 / (5 - 2) = 8.3% on one scored quarter (trailing window holds 1 of 4 quarters). Grade D (provisional). Role 1 mapping: Poor, if adopted. FLAG: a one-quarter, three-item sample; the protocol says never grade on one quarter alone, so the operator decides whether Role 1 takes this input now or after Q3. DROPPED count = 1 (the automatic downgrade needs 2).

### 3C. Patterns
- Revenue over-delivered (Q2 +18% QoQ), margin under-delivered: management misses margin and meets revenue.
- Robotics: dated in Q1, withdrawn in Q2.
- Silence on items with bad numbers: forex basis, ROCE number, Novelic, railway P&L, gross order book, DENSO terms (two calls each).
- Trend of the ratio: first reading, no trend.

### 3D. Promoter Verdict / Management Grade
Page: Promoter Verdict TRUSTWORTHY; Mgmt grade A. The provisional ratio maps to D. Flag only: the operator decides. One C2 DROPPED is logged; a second DROPPED in the trailing four calls triggers the automatic one-grade downgrade.

### 3E. Last quarter's concall questions (N1-N14)

| Q1 question | Answer status | What was said | Verdict |
|---|---|---|---|
| N1 Is 23.1% the trough? | ANSWERED SPECIFICALLY | "around 23%", 10-20 bps tolerance [ASR, call L632-634] | Answered: about 23% is the working level |
| N2 Earliest JV2 revenue quarter | PARTIALLY ANSWERED | JV2 close H1 CY2027; revenue quarter not given [ASR, call L443-445] | Third ask without a revenue date |
| N3 DENSO terms, EV, economic interest, close, P&L | PARTIALLY ANSWERED | Dates and taxability only | Two calls without terms |
| N4 Deliver three robotics SOPs | NOT ADDRESSED | none | Dropped |
| N6 EV inflection | PARTIALLY ANSWERED | "Demand for EVs continues to accelerate" (call L075); BEV +129% | Directional |
| N7 Robotics revenue conversion | EVADED | "I don't know is the real answer" (call L772) | Second evasion |
| N8 Forex in revenue | NOT ADDRESSED | none | Two calls |
| N9 Un-normalised ROCE, path | NOT ADDRESSED | "return ratios continue to show improvement" (call L367) | Two calls |
| N10 Capex, CFO, CFO/PAT | ANSWERED SPECIFICALLY (H1) | CFO 594, capex 148, FCF 446 [ASR]; tie to res L591-592 | Answered; envelope still missing |
| N11 Gross order book, haircut | NOT ADDRESSED | none | Two calls |
| N12 Railway revenue and PAT | EVADED | "We don't share business-wise growth outlook" (call L809) | Two calls |
| N13 Top-customer share | NOT ADDRESSED | Suspension motors one customer (call L417) | Two calls |
| N14 Novelic carrying value | NOT ADDRESSED | name only | Two calls |

Repeated evasion across two calls on N7, N12; non-address on N8, N9, N11, N13, N14. Logged as a governance signal for the Promoter Verdict update; the three-call threshold is reached if Q3 repeats.

## STEP 4: Q&A DECOMPOSITION

### 4A. Q&A inventory

| # | Analyst (firm) | Question (1 line) | Category | Response grade | Substance |
|---|---|---|---|---|---|
| Q01 | Arvind Sharma (NOT FOUND) | Driver of suspension-motor growth (call L393-395) | Customer/Order | B | One end customer; new model sold well (call L400-412) |
| Q02 | Arvind Sharma | Suspension-motor order pipeline (call L396) | Customer/Order | C | "can't give you anything definite" (call L427) |
| Q03 | Arvind Sharma | DENSO tie-up update (call L433-434) | Strategic | B | JV1 end-Dec, may slip to Jan; JV2 H1 CY27 (call L439-445) |
| Q04 | Chandra Moli Mutia (NOT FOUND) | Europe competition, legacy growth runway (call L459-469) | Strategic | B | 9% of world in diff gears, about 3% in diff assemblies (call L507-509) |
| Q05 | Chandra Moli Mutia | Robotics actuator milestones (call L470-477) | Forward Guidance | D | No milestones; "leave to God" (call L495) |
| Q06 | Gunjan Prithyani (NOT FOUND) | Traction-motor scale-up, wallet share, 3W, new program (call L514-530) | Operational | B | Wallet share plus market growth; Q3 launch (call L548-556) |
| Q07 | Gunjan Prithyani | Differential assembly pickup (call L531-539) | Operational | B | All three large EV customers picked up (call L577) |
| Q08 | Gunjan Prithyani | Size of 3W in traction motors (call L557) | Clarification | D | "pretty small so far", no number (call L558-561) |
| Q09 | Basudev Banerjee (NOT FOUND) | 23-25% margin range under the mix shift (call L599-609) | Financial | B | Range held; "around 23%" (call L610-638) |
| Q10 | Basudev Banerjee | Cash Rs 1,900 Cr: gross or net (call L640-643) | Financial | A | "That's gross" (call L644) |
| Q11 | Basudev Banerjee | Deployment of Rs 2,800-3,000 Cr net cash; M&A (call L645-659) | Financial | B | Four M&A filters; 1.5x cash/EBITDA threshold; DENSO taxable (call L660-704) |
| Q12 | Ramod Kumar (NOT FOUND) | Humanoid validation spend, timeline, capital (call L711-722) | Forward Guidance | C | Rs 62 Cr capex; Feb expo; no spend or timeline (call L762-767) |
| Q13 | Ramod Kumar | Positioning EV infrastructure for robotics projects (call L723-726) | Customer/Order | E | Customer rule invoked (call L727-728) |
| Q14 | Ramod Kumar | Robotics inflection year (call L768-771) | Forward Guidance | E | "I don't know is the real answer" (call L772) |
| Q15 | Ramod Kumar (answer opens "Hi, Brahmoor", call L808) | Railway growth outlook (call L801-805) | Forward Guidance | D | No guidance by policy; product levers (call L809-825) |
| Q16 | Chat | Heavy rare earth switch-back (call L841-844) | Macro | A | Not available; China export restrictions continue (call L845-854) |
| Q17 | Chat | Pass-through arrangements (call L856-857) | Financial | B | Lead-lag; full pass-through dilutes % margin (call L858-882) |
| Q18 | Chat | Humanoids on own lines (call L883-885) | Operational | C | "We are evaluating" (call L886-898) |

### 4B. Pattern analysis
- Most repeated topic: robotics (Q05, Q12, Q13, Q14, Q18; five asks). Margin asked twice (Q09, Q17). The market does not trust the robotics answers.
- C/D/E grades cluster on robotics (Q05, Q12-Q14, Q18), railway quantum (Q15), 3W size (Q08) and suspension pipeline (Q02). Management avoids dating robotics and quantifying segment economics.
- Buy-side vs sell-side split: ND (no firms named). Host Nomura asked no question.
- Hosting broker: did not lead with any question; no softball opening by the host.
- Pushback: Basudev pushed on net cash deployment (call L645-659); Ramod pushed for an inflection year (call L768-771). Both topics are contested. Ramod Kumar took four asks (Q12-Q15), above the two-question rule (call L382).
- Absence of asks (ledger): no analyst asked on working capital, receivables, tax rate, customer concentration %, Novelic, or the DENSO price basis.

### 4C. Three most important exchanges

Exchange 1 (Q09, margin; call L599-638)
- Question: with two quarters at about 23% and a rising mix of motor controllers, 3W, robotics and railways, how should we read the 23-25% range given motor controllers are lower margin?
- Response: CEO: no reason to change the range, "23 to 25 is fair", exceptional inflation (call L610-615). CFO: "if the world is operating in a normal fashion, I think we should probably, around 23%. I don't hold us to like every 10 or 20 bips ... unless oil goes to 150" (call L630-638).
- Said: range held; working number about 23%; pass-through with a lag.
- Not said: FY28 margin from the five-year exercise (call L616); a bps bridge; the ex-forex margin.
- Implication: the bull gate (>= 24.5%) has no management path. The tolerance band sits on the bear line.
- Follow-up: "What margin does the five-year exercise show for FY28, ex-forex?"

Exchange 2 (Q03 and Q11, DENSO; call L433-453, L660-664)
- Question: anything more on the DENSO tie-up? Later: net cash would reach Rs 2,800-3,000 Cr with Rs 900 Cr from DENSO by year end.
- Response: "carving out of the business by end of December ... may spill over to January"; JV2 "not yet formed up ... first half of calendar year, 27"; "what we get from Denso will pay tax on".
- Said: dates; taxability; JV2 capex will block capital.
- Not said: whether Sona consolidates the JV1 vehicle; gain size and line; the entity; royalty terms; the carve-out's earnings behind the EV Rs 1,750 Cr; the Rs 900 Cr was neither confirmed nor corrected, although it exceeds the EV-implied Rs 857.5 Cr before tax.
- Implication: Q3 or Q4 FY27 will be non-comparable, and the consolidated base may shrink if control is joint. The price cannot be judged fair or cheap (DENSO economics, Section A).
- Follow-up: Questions 1 and 2 in Step 8.5.

Exchange 3 (Q14, robotics inflection; call L768-800)
- Question: in the next three to four years, which year is the robotics inflection?
- Response: "I don't know is the real answer ... this is a recorded call and you know you can always hold me to it ... which is why we don't want to stick our neck out on this one" (call L772-778).
- Said: no timing; AMRs deployed on own floors (call L792-797); Feb expo demo.
- Not said: status of the three dated Q1 robotics SOPs.
- Implication: C2 is dropped by silence; the robotics trigger is DELAYED; the refusal reason (accountability) is itself a credibility signal.
- Follow-up: "Did the Q2 robotics SOP happen, yes or no?"

## STEP 5: NEW INFORMATION AUDIT

### 5A. New disclosures

| Disclosure | Type | Material? | Thesis impact |
|---|---|---|---|
| JV1 close end-Dec 2026 (may slip to Jan 2027); JV2 close H1 CY2027 [ASR, call L439-445] | Forward catalyst pre-announced | YES | Dates the like-for-like break. Price: EV Rs 1,750 Cr for 49% = Rs 857.5 Cr before tax, about 2.2x proxy sales (1.8x ASR run-rate) vs about 10.1x for Sona; carve-out earnings NOT FOUND (Section A, DENSO economics) |
| DENSO proceeds taxable; JV2 capex will block capital [ASR, call L660-663] | Forward catalyst | YES | One-off tax in the close quarter; net cash lower than analyst estimate; cash to Sona only if DENSO buys from Sona |
| Cash/EBITDA 1.5x deployment threshold [ASR, call L698-700] | New policy | YES | Capital-allocation decision likely within 12 months |
| Suspension motors about 7% of revenue, one customer, one model, China [ASR, call L241, L417, L084] | Negative surprise (concentration) | YES | Single-point dependency |
| Traction plus suspension motors run-rate Rs 1,400 Cr annualised [ASR, call L260] | Operational | YES | Scale of the organic motor engine; run-rate base for the DENSO price check |
| Freight nearly doubled QoQ [ASR, call L066-067] | Negative surprise | YES | Added cost headwind |
| New motor product launch in Q3 FY27 [ASR, call L561-562] | New product | NO (unnamed) | Scorable Q3 |
| Bharat Expo robotics demo, Feb 2027 [ASR, call L766] | Forward catalyst | NO | Demo, not revenue |
| AMRs deployed on own factory floors [ASR, call L792-797] | Operational | NO | Development step |
| Five-year margin exercise exists, undisclosed [ASR, call L616] | Information withheld | YES | Ask for it |
| Head of Railway: air springs started, HVAC first batch, panels ramping [ASR, call L815-818] | Operational | NO | Railway levers, no numbers (railway AMBER / UNVERIFIED) |
| Heavy rare-earth restrictions continue; light rare-earth design used [ASR, call L569, L847-854] | Regulatory/macro | YES | Supply-chain edge vs peers who cannot switch |
| All three large EV differential-assembly customers picked up [ASR, call L577] | Customer | NO | Supports driveline recovery |

### 5B. What was NOT discussed

| Expected topic | Why it should have been discussed | Significance of silence |
|---|---|---|
| Margin basis incl./ex forex | Gate outcome turns on it; Q1 question N8 | RED (two calls) |
| Payables build behind CFO (+278.79, res L585) | Cash leg quality | AMBER (one call) |
| Robotics SOP C2 | Dated Q1 promise | RED (dropped) |
| DENSO financial terms, carve-out earnings, accounting, gain line | Largest strategic event; two calls | RED |
| eDrive named; NCI vs equity accounting | Defines the post-close base | AMBER |
| EV share of order book (61%, third easing) | Tripwire 9 | AMBER (one call) |
| Order-book gross-to-net, consumption 1.6x | Book quality | RED (two calls) |
| Novelic carrying value / impairment | Tripwire 3; FY26 KAM | RED (two calls) |
| ROCE number and path to > 18% | Tripwire 1, buyable leg | AMBER to RED (two calls) |
| Railway revenue and PAT | Tripwire 8 | RED (two calls) |
| Customer concentration % | Rating agency weakness | AMBER (two calls) |
| Warranty and slow-moving inventory provisions | 70 bps of H1 margin [NOTION MEMORY] in a Deming-award quarter | AMBER |
| Corporate guarantees | Tripwire 5 | AMBER (two calls) |
| Auditor signing before board start | Repeat governance item | AMBER (routine call silence; carry to AR) |
| Capex envelope FY27-FY28 | Seven SOPs to H1 FY29 | AMBER (two calls) |
| Short-term borrowings doubling | Treasury plus debt | AMBER |
| Peer developments | No peer commentary | Neutral (peer concalls not passed) |

## STEP 6: TONE AND SPECIFICITY

### 6A. Tone comparison

| Topic | Prior concall (Q1 [NOTION MEMORY]) | This concall | Direction |
|---|---|---|---|
| Margin | Recovery "progressively more visible from Q2"; pressure "may continue" | "continued margin pressure ... mainly driven by change in product mix"; "around 23%" (call L055-057, L632) | DOWNGRADED |
| Margin cause | Input costs (pass-through lag) | Mix first, inflation second (call L057, L063) | DOWNGRADED (structural cause) |
| Robotics timing | Three dated SOPs; ramp "faster, much faster" | "I don't know is the real answer" (call L772) | DROPPED |
| EV demand | Refused inflection call | "Demand for EVs continues to accelerate" (call L075) | UPGRADED |
| DENSO | Scope only; JV2 date refused | Close dates given (call L439-445) | UPGRADED (specificity) |
| Cash | "best cash-flow quarter", no number | CFO Rs 594 Cr, FCF Rs 446 Cr (call L350-354) | UPGRADED |
| Return ratios | "gradual improvement" | "continue to show improvement" (call L367) | MAINTAINED (no number) |
| Railway | Head of Railway silent | Spoke, no numbers (call L809-825) | MAINTAINED |
| Quarter framing | ND | "almost a perfect quarter" (call L032) | UPGRADED (rhetoric) |

### 6B. Specificity score
Forward statements in the Q2 commitment register (A3 K01-K19): quantified (number, date or binary) 8: JV1 date, JV2 date, 1.5x threshold, 23-25% / about 23%, Q3 launch, Feb 2027 expo, Rs 62 Cr capex, 10x / 25% CAGR. Unquantified 11. Specificity ratio 8 / 19 = 0.42 (moderate). Q1 was about 0.40 [NOTION MEMORY].

### 6C. Defensive language
About 19 instances (A3 hedge inventory), including "I don't know is the real answer" (call L772, L798), "can't give you anything definite" (call L427), "don't want to stick our neck out" (call L778), "We don't share business-wise growth outlook" (call L809), "may spill over" (call L440), "I don't hold us to" (call L633), "we are evaluating" four times (call L886-892), customer-confidentiality invocations (call L011, L727). Count > 5: hedge-heavy call. Q1 about 9 [NOTION MEMORY]; counting methods differ, so the trend is indicative only.

### 6D. Confidence indicators
- Specific dates: JV1 Dec/Jan, JV2 H1 CY27, Q3 motor launch, Feb 2027 expo.
- Acknowledged miss: the CEO opened with the margin miss (call L050-057), though without a recovery date.
- MD present and answering operational questions directly.
- No named customer wins with deal size spoken (deck itemises them).

### 6E. Management archetype
Specificity 0.42 (<= 0.5) x credibility 8.3% provisional (< 60%) = EVASIVE (provisional). Q1 was provisionally MEASURED & CREDIBLE with an EVASIVE-on-financials watch [NOTION MEMORY]. Archetype shift flagged; it rests on one scored quarter and three commitments.

## STEP 7: CROSS-REFERENCE

### 7A. Concall narrative vs filing

| Concall claim | Filing evidence | Reconciliation |
|---|---|---|
| Revenue Rs 1,546 Cr, +35% [ASR, call L306] | Rev ops 1,535.84 + forex 10.58 = 1,546.42 (res L470-471) | CONFIRMED on a forex-inclusive basis that the call never states |
| EBITDA Rs 356 Cr, margin 23% (call L313-314) | 356.24 incl. forex; 23.04% on revenue incl. forex | CONFIRMED (basis unstated) |
| PAT "23 crores" +29% (call L320) | Owners PAT 223.40 (res L496) | CONFIRMED after ASR digit drop |
| Margin lower by 2.3% YoY (call L314) | -224 bps deck basis; -219 bps rev ops | CONFIRMED |
| H1 BEV "2,042 crores", 48% (call L328-329) | Deck H1 BEV 10,416 mn = 1,041.6 Cr (deck L167) | CONTRADICTED (likely ASR; filed deck governs) |
| BEV 51% "of our revenue" (call L775) | 51% is of automotive product revenue (deck L125); BEV is about 39.2% of total Q2 revenue (606.1 / 1,546.4) | CONTRADICTED (basis drift) |
| EV business "more diversified and less dependent on any single customer or single geography" (call L137-140) | Rs 16.3 bn (45%) of Q2 additions from existing Indian 2W OEM customer(s) (deck L196-203; PR L128-135); suspension motors on one customer (call L417) | PARTIALLY CONFIRMED (geography broader; customer concentration in the growth engine) |
| CFO Rs 594 Cr, 90% of EBITDA (call L350-351) | CFO 593.53 (res L591); 593.53 / 658.84 = 90.1% | CONFIRMED |
| "release of 44 crores from working capital" (call L352) | Filed cash flow: net WC movement (11.08), with payables +278.79 (res L581-588). Deck shows WC +440 mn in its own bridge (deck L456) | PARTIALLY CONFIRMED (deck basis); filed statement shows net absorption and a payables-carried CFO |
| Capex about Rs 148 Cr; FCF Rs 446 Cr (call L354) | 148.50 and 445.03 (res L591-592) | CONFIRMED |
| Borrowings Rs 224 Cr (call L357) | Net ST borrowing proceeds 223.62 (res L609) | CONFIRMED (reason not given) |
| ESOP Rs 108 Cr; dividend Rs 112 Cr (call L356-358) | 107.60 and 111.97 (res L614, L613) | CONFIRMED |
| Cash and investments Rs 1,966 Cr gross (call L361, L644) | Deck closing 19,655 mn (deck L446) | CONFIRMED (deck) |
| "Return ratios have improved" (call L152) | ROCE 15.4% to 16.4% normalised (deck L469) | PARTIALLY CONFIRMED (normalised only) |
| "almost a perfect quarter" (call L032) | Margin -219 bps YoY; C1 missed; payables-carried CFO | CONTRADICTED on margin and cash quality |
| "absolute margins continue to improve" (call L071-072) | Op EBITDA 289.06 to 356.24 YoY; 302.60 to 356.24 QoQ | CONFIRMED |
| "EV demand continues to accelerate" (call L075) | BEV +129% (deck L125); EV share of book 61% easing (deck L257-258) | PARTIALLY CONFIRMED |
| VA/employee cost decline due to assembly mix (call L365-366) | 5.8 to 4.9 to 4.7 (deck L467) | CONFIRMED (the decline itself) |

Concall narrative contradicts filing numbers on the H1 BEV figure and the BEV basis. The filing wins; noted as a credibility item (basis drift), not as a numbers dispute.

### 7B. Peer concall cross-check
UNVERIFIABLE this run: peer concalls not passed.

| Topic | This company said | Peer 1 | Peer 2 | Most credible |
|---|---|---|---|---|
| Demand (E2W/E3W India) | Accelerating (call L075-078) | ND | ND | UNVERIFIABLE |
| Input costs | Steel, copper, oil derivatives up; freight doubled (call L064-067) | ND | ND | UNVERIFIABLE |
| Rare earths | Heavy rare earths unavailable (call L847-854) | ND | ND | UNVERIFIABLE |
| US EV | Deliveries broadly unchanged (call L135-136) | ND | ND | UNVERIFIABLE |

### 7C. Channel checks

| Concall claim | External source | External says | Alignment |
|---|---|---|---|
| Strong liquidity, net cash | India Ratings 25-Jun-2026 [NOTION MEMORY] | AA+/Stable; robust liquidity; weaknesses customer concentration and forex | ALIGNED on liquidity; concentration silence persists |
| E2W demand strong | Vahan registrations | not passed | UNVERIFIABLE |
| Global share gains | Ricardo/CRISIL in deck (deck L716-718) | CY25 diff-gear share 8.7% (from 8.8%), starter 4.2% (from 4.4%) (deck L700, L703) | NOT ALIGNED with a share-gain narrative in CY25 |

## STEP 8: THESIS AND POSITION UPDATES

### 8A. Growth trigger status (post-concall)

| Trigger | Status pre-concall (filing) | Concall evidence | Status post-concall |
|---|---|---|---|
| #1 Railway diversification | AMBER / UNVERIFIED (railway evidence set R, Step 6B) | Product levers, no numbers; "dependent on whether we are successful to launch these products on time" (call L824-825) | AMBER / UNVERIFIED |
| #2 BEV anchor | ON TRACK revenue / WEAKENED book | EV demand "accelerating"; traction +50% QoQ [ASR]; DENSO JV1 close dated; 49% of the EV-motor carve-out priced at about 2.2x proxy sales | ON TRACK on revenue; WEAKENED on ownership and book share |
| #3 Robotics and Physical AI | DELAYED | "I don't know"; Feb 2027 demo only | DELAYED |
| NEW: Suspension motors | n/a | About 7% of revenue, fastest growing, one customer [ASR] | NEW (single-customer) |

### 8B. Concall-specific watchlist updates

| # | Watchlist item | This concall reading | Status |
|---|---|---|---|
| 1 | ROCE | Number not spoken; "improving" | AMBER |
| 3 | Novelic | Name only | UNKNOWN (two calls silent) |
| 4 | CFO/PAT | CFO 594 Cr spoken; payables silent | AMBER |
| 6 | Margin | "around 23%"; mix cause | RED |
| 8 | Railway | Head of Railway declined guidance; railway evidence set R | AMBER / UNVERIFIED |
| 9 | BEV anchor / EV share of book | EV share not spoken; BEV 51% of auto | AMBER |
| 10 | India mix | "eastern markets almost two thirds" | UNKNOWN |

### 8C. Thesis-broken trigger check (concall)

| Condition | Threshold | Concall-relevant evidence | FIRED? |
|---|---|---|---|
| ROCE < 14% x 2 yrs | < 14% | "return ratios continue to show improvement" (call L367) | NOT FIRED |
| Forced block sale / control dispute | any | DENSO presented as partnership with dated closes; no control change at Sona | NOT FIRED |
| Novelic impairment > Rs 350 Cr | > 350 | silent | NOT FIRED (unverifiable) |
| CFO/PAT < 1.0x sustained | < 1.0x | CFO 90% of EBITDA (call L351) | NOT FIRED |
| Corporate guarantee expansion | expansion | silent | NOT FIRED (unverifiable) |

### 8D. Four-pillar concall adjustments
Deferred to /fttcp and Role 1 (OR-30). Pillar-relevant concall facts:
- Pillar 1 (via FTTCP ROCE forward verdict): "return ratios ... incremental returns ... supporting this improvement every quarter" [ASR, call L367-368]; no number.
- Pillar 2: CFO 90% of EBITDA [ASR]; WC framed as a Rs 44 Cr release while the filed statement shows payables-carried CFO.
- Pillar 3 / Growth visibility: Q3 motor launch; robotics timing withdrawn; suspension motors single-customer; 25% CAGR aspiration.
- Strategic premium: DENSO JV dates; DENSO price about 2.2x proxy sales vs about 10.1x group, carve-out earnings NOT FOUND; heavy rare-earth workaround (light rare earth) as a capability (call L569-573 [ASR]). Single-credit rule: no ROCE recovery is credited anywhere in this review.

### 8E. Position decision (concall overrides)
- Credibility ratio < 60% (provisional 8.3%): discount management commentary by 30-50%; tighten add-back triggers; consider Promoter Verdict review. Operator decides; one-quarter sample.
- Two or more DROPPED in trailing four: NO (one).
- Undisclosed material risk revealed: suspension-motor single-customer dependency (about 7% of revenue). Trim rule applies to held names only; not held.
- Undisclosed material positive: DENSO close dates. Hold pending verification; the price basis (carve-out earnings) is unknown, so the dates are positive for visibility only, not for value.
- Evasion pattern across 3+ quarters: not yet (two calls).
- Narrative contradicts filing: H1 BEV figure and BEV basis. Trust the filing; tighten next-quarter watchlist.
- Net: Decision Status WATCHLIST verified; branch 8A-W; no status change proposed.

### 8F. Updated questions for the next quarter (feeds Q3 Role 4 Step 8.5)

| # | Question | Why it matters | What to watch in the next concall |
|---|---|---|---|
| F1 | JV1 closed? Consolidated at 51% with NCI or equity-accounted? Gain, tax and line? Carve-out EBITDA and PAT? | Defines the post-close base and the price fairness | eDrive leaves the WOS list; NCI or equity income line appears |
| F2 | Q3 margin incl. and ex forex; payables days at 31-Dec | The single cleanest metric | Ex-forex >= 22.5%; payables flat |
| F3 | Q2 robotics SOP: yes or no; new dates | C2 | A dated SOP or a third non-answer |
| F4 | Un-normalised ROCE and one footnote definition | Pillar 1 | A number, or a third silence |
| F5 | Gross order book and consumption definition | Book quality | A bridge, or a third silence |
| F6 | Novelic carrying value | Tripwire 3 | Impairment test result |
| F7 | Railway revenue and PAT | Tripwire 8 / growth trigger #1 | Numbers, or a third evasion |
| F8 | Q3 motor product launched? 3W share? | K07 | Product named and shipped |
| F9 | Freight pass-through | Margin | Yes/no |
| F10 | Use of cash above 1.5x cash/EBITDA | Capital allocation | Policy action |

---

# SECTION C: COMBINED VERDICT

- Filing-derived signals: revenue +34.92% YoY to a record 1,535.84; owners PAT +29.30%; op EBITDA margin 23.20% (rev ops), 22.51% ex-forex, -219 / -243 bps YoY; parent margin -343 bps; core PBT +24.84%; CFO/PAT 1.48x printed, 0.78x ex-payables; short-term borrowings doubled; warranty and obsolescence provisions up; auditor signed before the board again; DENSO not closed, accounting route ambiguous, and 49% priced at EV Rs 1,750 Cr with carve-out earnings NOT FOUND.
- Concall-derived signals: C1 conceded missed; margin working level about 23%; DENSO close dates given; robotics timing withdrawn; suspension motors single-customer; 1.5x cash/EBITDA threshold; silence on forex basis, ROCE number, Novelic, railway P&L, DENSO terms, order-book bridge for a second call.
- Reconciliation: headline numbers reconcile to the filing on a forex-inclusive basis. Two narrative items contradict the filed deck (H1 BEV figure, BEV basis). The call's "release of 44 crores from working capital" does not match the filed statement's payables-carried CFO.
- Net thesis impact: MAINTAINED. Catalyst status: DENSO ON TRACK on timing (dated, ASR); price fairness unevaluable (carve-out earnings NOT FOUND). Railway growth trigger AMBER / UNVERIFIED. Thesis status: INTACT (no broken condition), with growth strong and margin and cash quality adverse.
- Position decision: branch 8A-W, Decision Status WATCHLIST unchanged (operator-only). No pre-committed trigger fired. Entry-zone recompute deferred to Role 1.
- Watchpoints for Q3 FY27: (1) consolidated op margin incl./ex forex; (2) payables days and 9M CFO/PAT; (3) DENSO JV1 close, accounting and carve-out earnings; (4) robotics SOP yes/no; (5) EV share of order book; (6) warranty provision run-rate; (7) auditor signing time vs board start.

Protocol verdict: PROCEED WITH FLAGS. Cash conversion INDETERMINATE-WITH-DIRECTION caps the verdict at no better than PROCEED WITH CAVEATS; the flags below make it PROCEED WITH FLAGS. Missing cash evidence: FY27 full-year CFO and payables days at 31-Mar-2027. Loop 1 fixes do not move the verdict.

Concall Verdict:
- Management credibility (this quarter): Grade D (provisional, one scored quarter, three commitments)
- Trailing 4-quarter credibility ratio: 8.3% (0.25 / (5 - 2))
- Management archetype (6E): EVASIVE (provisional; shift from provisional MEASURED & CREDIBLE)
- Role 1 track-record input: Poor if adopted; operator to decide whether to adopt on one quarter
- Net concall impact on thesis: Weakened (margin floor confirmed, robotics dates withdrawn), offset in part by DENSO dates and quantified cash
- Position decision: entry-zone update deferred to Role 1; WATCHLIST unchanged

Flags for the operator:
1. Margin gate basis ruling pending (23.20% incl. forex vs 22.51% ex-forex). Ex-forex is below the bear line for the second quarter.
2. Cash leg ruling pending: 1.48x printed vs 0.78x ex-payables (1.00x a year ago).
3. C1 MISSED (conceded); C2 DROPPED on silence; C3 DELAYED. Provisional grade D, archetype EVASIVE. Page shows Mgmt grade A.
4. Auditor reports signed before the board met, second quarter running, lead about 33 minutes.
5. DENSO JV1 close guided end-Dec / Jan [ASR]; Note 5 wording leaves the consolidation route open; the eDrive economics are undisclosed.
6. DENSO 49% priced at EV Rs 1,750 Cr = Rs 857.5 Cr before tax: about 2.2x proxy sales (1.8x ASR run-rate) vs about 10.1x for Sona; set at 22-Jul signing before the Q2 surge; carve-out EBITDA and PAT NOT FOUND, so fair price and value transfer cannot be separated.
7. Parent (standalone) margin -343 bps YoY; group margin held only through the subsidiary layer.
8. Short-term borrowings doubled (234.25 to 461.97) while treasury grew.
9. EV share of order book 61%, third easing (tripwire 9); release reframed it as 65% "EV and Robotics".
10. Order-book consumption 1.6x revenue; Rs 4.8 bn of additions unitemised.
11. Warranty provision 5.7x and slow-moving inventory provision 6.7x YoY.
12. ROCE 16.4% normalised under two definitions; un-normalised ND.
13. Two-call silences: forex basis, ROCE number, Novelic, railway P&L, DENSO terms, order-book bridge.
14. Railway growth trigger #1 and tripwire 8 both AMBER / UNVERIFIED (FIRED on FY26 AR; Q2 does not confirm continued delivery).
15. Tracker rows not supplied; fewer than three signals; reopen Role 5.5.
16. Notion holds no FY27 or FY28 projections; growth-trigger #3 label conflict on the page.
17. Concall is ASR: all concall-only numbers unverified.
18. Promoter-group representative not on the call; operator to confirm whether this is a yellow flag.
19. CMP Rs 879 is 2.29x the page's base FV Rs 384 (context only; no FV recompute here).

---

## FORWARD ESTIMATE INPUTS (indicative, not Role 1)

Consolidated, Rs Cr. No Section 1B exit multiple, no fair value. Evidence tiers: [FILED] results filing; [MGMT-FILED] deck or press release; [ASR] call transcript; [NOTION MEMORY] page. Base = most evidenced path (A26.3), no shading; conservatism belongs in position size. DENSO gain, tax on proceeds and other income on proceeds are excluded from both readings (one-off; terms undisclosed). NCI leakage from a 51% DENSO vehicle is not netted in either reading because the vehicle's revenue and PAT are not disclosed (ND); it is a downside to both from the close quarter.

Diluted share count: the filing does not print a share count. Paid-up equity capital Rs 6,241.28 mn at Rs 10 face value at 30-Sep-2026 [FILED, res L502, L536] = 624.128 mn = 62.41 Cr shares (my arithmetic). Cross-check: H1 owners PAT 4,038.73 mn / diluted EPS Rs 6.48 [FILED, res L496, L505] = 623.26 mn weighted. Screener market cap Rs 55,012 Cr / Rs 879 implies 62.58 Cr [SECONDARY], 0.27% above the filing; the filing figure is used.

Deck revenue series check (A5 M1): deck L516 44,752 (row M09) has no year label on the slide; its year is positional. It ties to filed FY26 consolidated revenue from operations plus net forex: 44,494.60 + 256.88 = 44,751.48 mn (res L470-471). It is therefore FY26 revenue on the deck's forex-inclusive basis, not revenue from operations. The FY21 start point used in loop 0 (15,663, R239, LABEL_UNMAPPED) cannot be tied to any filed figure in this corpus and is positional only. FY28E-B is therefore re-derived on the deck's labelled "5-year Revenue CAGR 23%" (R242, deck L583-587, "Growth"), applied to the rev-ops base. The forex share of revenue is about 0.6-0.7% (res L470-471), so the basis difference does not move the rate. Cross-check: the positional FY21-FY26 CAGR is 23.36%; the labelled FY22-H1 FY27 annualised CAGR is 24.1% (M08, deck L515).

| Year | Reading | Revenue (rev ops) | Arithmetic | Owners PAT | Arithmetic | EPS (Rs) | PE at Rs 879 | Basis and tier |
|---|---|---|---|---|---|---|---|---|
| FY26 | Actual | 4,449.46 | res L470 | 640.17 | res L496 | 10.30 diluted (res L505) | 85.3x | [FILED] |
| TTM to Sep-26 | Actual | 5,294.30 | 4,449.46 - 1,992.20 + 2,837.04 | 746.56 | 640.17 - 297.48 + 403.87 | 11.96 | 73.5x | [FILED], my arithmetic |
| FY27E | A (base) | 5,908.72 | H1 2,837.04 + H2 (Q2 1,535.84 x 2 = 3,071.68) | 850.67 | H1 403.87 + H2 (Q2 223.40 x 2 = 446.80) | 13.63 | 64.5x | Q2 run-rate held through H2. Evidence: Q2 is the latest quarter [FILED res L470, L496]; traction-motor extra volumes SOP H2 FY27 [MGMT-FILED deck L201-209, PR L132-135]; Q3 motor launch [ASR call L561-562]. Growth +32.80%; H2 is +25.0% on H2 FY26 (2,457.26) |
| FY27E | B | 5,674.08 | H1 2,837.04 + H2 equal to H1 (2,837.04) | 807.74 | H1 403.87 x 2 | 12.94 | 67.9x | Q2 was a step that does not hold (traction motors +50% QoQ [ASR call L060] partly a one-quarter surge); H2 at the H1 average [FILED]. Growth +27.52% |
| FY28E | A (base) | 7,385.90 | FY27E-A 5,908.72 x 1.25 | 1,074.34 | 7,385.90 x Q2 owners PAT margin 14.546% (223.40 / 1,535.84) | 17.21 | 51.1x | 25% CAGR medium-term aspiration [ASR call L830-838]; net order book Rs 251 bn = 5.6x FY26 revenue [MGMT-FILED deck L244]; H1 FY28 SOPs Rs 5.8 bn lifetime (deck L201-238) |
| FY28E | B (restated loop 1) | 6,979.12 | FY27E-B 5,674.08 x 1.23 | 993.52 | 6,979.12 x H1 FY27 owners PAT margin 14.236% (403.87 / 2,837.04) | 15.92 | 55.2x | Labelled deck 5-year revenue CAGR 23% [MGMT-FILED, R242, deck L583-587]; H1 margin level [FILED]. Loop 0 value (7,001.81 / 996.75 / 15.97 / 55.0x) rested on the positional FY21 bar and is withdrawn |

Separating observations:
- FY27: Q3 FY27 revenue from operations vs Rs 1,535.84 Cr (results about late January 2027). At or above it, Reading A holds; at or near the H1 quarterly average of Rs 1,418.52 Cr, Reading B holds.
- FY28: the DENSO JV1 closing note (subsidiary at 51% with NCI vs joint venture equity-accounted) together with the Q4 FY27 revenue run-rate. Joint control removes the EV-motors revenue from the consolidated base and pushes FY28 below both readings; consolidation at 51% keeps revenue but leaks 49% of that entity's PAT.

Sensitivities (not readings): (1) Role 5 Step 8E discounts management commentary by 30-50% while provisional credibility is below 60%; applied to the 25% aspiration this gives 12.5-17.5% FY28 growth, i.e. FY28 revenue 6,647-6,943 on the FY27E-A base. (2) Notion FY29 base EPS Rs 16.0 [NOTION MEMORY] is below FY28E-A EPS Rs 17.21 and close to FY28E-B Rs 15.92. Both forward EPS figures are gross of the DENSO NCI leakage and include other income at about 10.5% of PBT; the comparison overstates the gap until the post-close NCI line is known. The base FV refresh is for Role 1.

---

## PLAIN-LANGUAGE BRIEF

### 1. SUMMARY NARRATIVE
Sona sold Rs 1,536 Cr of goods in the September quarter, 35% more than a year ago [FILED]. Owners' profit rose 29% to Rs 223 Cr [FILED]. Both are records [MGMT-FILED, PR L68].
Profit grew slower than sales. The operating margin fell to 23.2% from 25.4% a year ago [FILED, my arithmetic]. Without the forex gain it is 22.5% [FILED, my arithmetic].
Materials now take 51% of every rupee of sales, up from 48% [FILED]. Faster growth in lower-margin motors and higher steel and copper prices did this [MGMT].
The parent company's own margin fell 3.4 points [FILED]. The group held up only because the subsidiary layer's operating profit rose 3.6 times (consolidated minus standalone, including eliminations) [FILED, my arithmetic].
Cash looks strong on paper: Rs 594 Cr from operations, 1.48 times profit [FILED]. But Rs 279 Cr of that came from paying suppliers later [FILED]. Without it, cash is 0.78 times profit, worse than last year's 1.00 [FILED, my arithmetic].
Short-term debt doubled to Rs 462 Cr while cash also rose [FILED].
Management admitted the promised margin recovery did not come [ASR]. The robotics start promised for this quarter was never mentioned [ASR]. The radar launch came one quarter late [MGMT].
The DENSO deal now has dates: first part by end-December, maybe January [ASR]. DENSO pays about 2.2 times sales for its 49% stake, while Sona itself trades near 10 times sales [FILED, MGMT-FILED, my arithmetic]. The unit's profit is not disclosed, so we cannot tell if that price is fair.
The auditors again signed before the board met [FILED].
No rule that would break the thesis fired. The status stays WATCHLIST. At Rs 879 the stock trades at about 74 times trailing earnings [my arithmetic]. That is far above the page's 22.5x destination [NOTION MEMORY]. This quarter does not change that gap.

### 2. SECTOR INTELLIGENCE
- Demand: Indian electric two- and three-wheelers drove the quarter. Traction-motor sales rose almost 50% in one quarter [ASR, this quarter]. E2W/E3W rose from 10% of revenue in FY26 to 14% in H1 FY27 [MGMT-FILED, deck L297].
- BEV revenue grew 129% YoY [MGMT-FILED, deck L125]. Management attributes it to a broader customer base [ASR, call L135-140], but it named India E2W/E3W demand as the biggest reason [ASR, call L077-080]. The two 2W motor and controller additions (Rs 16.3 bn, 45% of Q2 additions) come from existing Indian 2W OEM customer(s) [MGMT-FILED, deck L196-203; PR L128-135]. Suspension motors (about 7% of revenue) sit on one customer and one model [ASR, call L241, L417]. US EV deliveries stayed flat [ASR, call L135-136].
- Input costs: management names the West Asia war, steel, copper, oil derivatives and a near doubling of freight [ASR, this quarter]. Pass-through comes with a lag and lowers the percentage margin even when complete [ASR].
- Supply chain: China still restricts heavy rare-earth exports [ASR]. Sona moved to light rare-earth designs and gained share when rivals could not ramp [ASR, INFERENCE on the share effect].
- Europe: OEMs want a non-China supply chain [ASR]. Not yet visible in filed numbers.
- Railway: LHB coach air springs and HVAC are starting [ASR]. The railway order book is Rs 900 Cr, about 0.77 years of work at the FY26 run-rate [MGMT-FILED; NOTION MEMORY for the revenue base]. Status AMBER / UNVERIFIED.
- Credit: India Ratings AA+/Stable, June 2026 [NOTION MEMORY, prior work].
- Not disclosed this quarter: India revenue share, customer concentration %, railway revenue and profit, DENSO carve-out earnings.

### 3. BUSINESS-MODEL INTELLIGENCE
- Sona is a build-to-spec component maker: gears, differential assemblies, starter, traction and suspension motors, controllers, railway parts and sensors [MGMT-FILED].
- Unit economics this quarter: materials 51% of sales, employees 8.5%, other costs 18%, operating margin about 23% [FILED, my arithmetic].
- Model drift 1, mix: motors and assemblies grow faster than gears. Value added per rupee of labour cost fell from 5.8 to 4.7 [MGMT-FILED, prior and this quarter]. The margin floor is moving down, not recovering.
- Model drift 2, ownership: the EV-motor business moves into a vehicle where DENSO owns 49%, valued at Rs 1,750 Cr [FILED]. 49% is Rs 857.5 Cr before tax, and the proceeds are taxable [ASR]. That is about 2.2 times the E2W/E3W segment's annualised sales (1.8 times on the spoken run-rate), against about 10 times for Sona as a whole [MGMT-FILED, ASR, my arithmetic]. 45% of this quarter's order additions are two-wheeler motors and controllers [MGMT-FILED, my arithmetic]. Reading A: a thin-margin unit at a fair price. Reading B: 49% of the fastest-growing engine sold cheaply, priced on 22-Jul before the Q2 surge. The unit's EBITDA and PAT decide it; both are NOT FOUND.
- Model drift 3, capital: capex halved to Rs 149 Cr in H1 [FILED] while seven product starts run to H1 FY29 [MGMT-FILED]. Either capex rises later or new capacity sits in partner vehicles [INFERENCE].
- Orders: net order book Rs 25,100 Cr, 5.6 times FY26 sales [MGMT-FILED]. The quarter used Rs 2,500 Cr of book against Rs 1,546 Cr of sales [MGMT-FILED, my arithmetic]. The difference is not explained.
- Scale: 12 plants and 34 products (deck L506-507, rows M04, M05) [MGMT-FILED].

### 4. COMPETITION INTELLIGENCE
- Where Sona wins: global share in differential gears rose from 4.5% (CY19) to 8.7% (CY25); starter motors from 2.5% to 4.2% [MGMT-FILED, Ricardo/CRISIL data]. It claims about 9-10% of the world traction-motor market outside China [ASR]. It serves 7 of the top 10 PV OEMs and 3 of the top 10 EV OEMs [MGMT-FILED].
- Where it is weaker: CY25 is the first year both share series fell together (gears 8.8% to 8.7%; starters 4.4% to 4.2%) [MGMT-FILED, deck L700, L703]. Starter-motor share also fell once before, from 4.6% in CY21 to 4.1% in CY22 (deck L703). The India dominance claim (55-90% by segment) rests on a February 2021 CRISIL report [MGMT-FILED].
- Differential assemblies: only about 3% of the world market [ASR], so room to grow but no scale edge yet.
- DENSO is both partner and potential competitor in high-voltage motors; the JV makes DENSO the majority owner of the 4W HV vehicle [FILED].
- Named listed Indian peers and their numbers: ND in this corpus and on the Notion page read. Chinese motor suppliers are the implied rival in management's Europe comments [ASR, INFERENCE].
- Risk to watch: if CY26 share data show another joint dip, the gear franchise is maturing while the motor business moves into shared ownership.

### 5. FORWARD MAP (next 10-11 months, Nov-2026 to Sep-2027)
Make-or-break reading: Q3 FY27 consolidated operating margin, incl. and ex forex, at results in about late January 2027. Bull at or above 24.0% with supplier payables flat; bear below 23.0% (or below 22.5% ex-forex) or a payables unwind that takes 9M CFO/PAT below 1.0x.

| Date (implied) | Catalyst | Bull fork | Bear fork |
|---|---|---|---|
| Oct-Dec 2026 | New motor product launch (Q3) [ASR] | Named and shipping; 3W share rises | Slips; another unnamed launch |
| Oct 2026-Mar 2027 | Extra traction-motor volumes start (Rs 12.5 bn order) [MGMT-FILED] | Revenue holds above Rs 1,536 Cr a quarter | Volumes book inside the DENSO vehicle, not Sona's share |
| End-Dec 2026 / Jan 2027 | DENSO JV1 close [ASR] | Consolidated at 51%; gain booked in standalone; cash to Sona up to Rs 857.5 Cr before tax (EV-implied cap), less tax | Joint control; EV-motor revenue leaves the consolidated base; a primary subscription keeps the cash in the vehicle; carve-out earnings show value transfer |
| Late Jan 2027 | Q3 FY27 results | Margin at or above 24.0%; payables flat | Margin below 23.0%; payables unwind |
| Feb 2027 | Bharat Expo robotics demonstration [ASR] | Demo plus a dated robotics production start | Demo only; robotics dates stay withdrawn |
| Jan-Jun 2027 | DENSO JV2 close [ASR] | Closes on time with capex stated | Slips again; capital blocked without a revenue date |
| By 31-Mar 2027 | Cash/EBITDA crosses 1.5x [ASR] | Return of capital or accretive buy on the four filters | Large purchase outside the core |
| About May 2027 | Q4 FY27 results; full-year CFO | CFO/PAT at or above 1.0x without the payables build | Cash leg fails ex-payables for the full year |
| Apr-Sep 2027 | H1 FY28 product starts (controllers Rs 3.8 bn, gears Rs 2.0 bn) [MGMT-FILED] | Starts on time | Dates slip |
| Jun-Jul 2027 | FY27 annual report | Novelic carrying value cleared; guarantees disclosed | Novelic impairment; capitalised development written down |
| Through Sep 2027 | Railway book of Rs 9 bn runs off [MGMT-FILED] | New orders refill the book | Book not replaced; non-auto share keeps falling |
| Late Jul 2027 | Q1 FY28 results | Margin stable with DENSO effects explained | Third concall silent on forex basis, ROCE and Novelic: governance review threshold |

```yaml
stage: A4-analyst
company: "SONACOMS"
quarter: "q2fy27"
model: "claude-opus-5-5"
status: complete
docs_merged: [results, concall, presentation, pressrelease]
ledger_reconciliation:
  notes: 13
  turns: 53
  slides: 36
  all_reviewed: true
  a3_findings_incorporated: ["RES:F1-01", "RES:F1-02", "RES:F1-03", "RES:F2-01", "RES:F2-02", "RES:F2-03", "RES:F2-04", "RES:F2-05", "RES:F2-06", "RES:F3-01", "RES:F3-02", "RES:F6-01", "RES:F6-02", "RES:F7-01", "RES:F8-01", "RES:F8-02", "RES:F8-03", "RES:F10-01", "RES:F10-02", "RES:F12-01", "RES:F12-02", "RES:F12-03", "RES:F14-01", "RES:F14-02", "RES:F14-03", "RES:F14-04", "RES:F15-01", "RES:F15-02", "P-A3-F6-01", "P-A3-F6-02", "P-A3-F6-03", "P-A3-F6-04", "P-A3-F6-05", "P-A3-F7-01", "P-A3-F10-01", "P-A3-F14-01", "P-A3-F14-02", "P-A3-F14-03", "P-A3-F14-04", "P-A3-F16-01", "P-A3-F16-02", "P-A3-F16-03", "P-A3-F16-04", "P-A3-F16-05", "P-A3-F16-06", "P-A3-F16-07", "P-A3-F16-08", "P-A3-F16-09", "P-A3-F17-01", "P-A3-F17-02", "P-A3-F17-03", "P-A3-F17-04", "P-A3-F17-05", "A3-PR-F6-01", "A3-PR-F6-02", "A3-PR-F6-03", "A3-PR-F14-01", "A3-PR-F14-02", "A3-PR-F14-03", "A3-PR-F14-04", "A3-PR-F14-05", "A3-PR-F14-06", "A3-PR-F16-01", "A3-PR-F16-02", "A3-PR-F16-03", "A3-PR-F16-04", "A3-PR-F17-01", "A3-PR-F17-02", "A3-PR-F17-03", "A3-PR-F17-04", "A3-F6-01", "A3-F6-02", "A3-F6-03", "A3-F6-04", "A3-F6-05", "A3-F6-06", "A3-F7-01", "A3-F7-02", "A3-F7-03", "A3-F7-04", "A3-F7-05", "A3-F8-01", "A3-F10-01", "A3-F14-01", "A3-F14-02", "A3-F14-03", "A3-F14-04", "A3-F17-01", "A3-F17-02", "A3-F17-03", "A3-F17-04", "A3-F17-05", "A3-F17-06", "A3-F17-07", "A3-F17-08", "A3-F17-09", "A3-F17-10", "A3-F17-11"]
  deck_missing_from_structured_cited: ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13", "M14", "M15"]
  deck_rows_reviewed: 332
protocol_verdict: "PROCEED WITH FLAGS"
cash_conversion: "INDETERMINATE-WITH-DIRECTION"
decision_status_verified: "WATCHLIST"
position_branch: "8A-W"
sc_gap_pat_pct:
  - {period: "Q2 FY26", sa_pat_cr: 166.25, c_pat_cr: 170.47, gap_pct: -2.54}
  - {period: "Q1 FY27", sa_pat_cr: 220.11, c_pat_cr: 178.51, gap_pct: 18.90, note: "ex-dividend about -11.1"}
  - {period: "Q2 FY27", sa_pat_cr: 197.38, c_pat_cr: 222.99, gap_pct: -12.97}
  - {period: "H1 FY26", sa_pat_cr: 286.38, c_pat_cr: 292.17, gap_pct: -2.02}
  - {period: "H1 FY27", sa_pat_cr: 417.48, c_pat_cr: 401.50, gap_pct: 3.83, note: "ex-dividend about -12.1"}
  - {period: "FY26", sa_pat_cr: 646.42, c_pat_cr: 629.19, gap_pct: 2.66}
questions_for_management:
  - {q: "After JV1 closes, is the EV-motors vehicle consolidated at 51% with 49% NCI or equity-accounted; name the entity (Note 5 says both 'Joint Ventures' and 'this subsidiary')", from_finding_id: "RES:F1-02, RES:F15-02, RES:F6-01, A3-F6-03, A3-F17-08, P-A3-F17-03, A3-PR-F16-04"}
  - {q: "State the carve-out's FY26 and H1 FY27 revenue, EBITDA and PAT behind the EV Rs 1,750 Cr; does DENSO buy from Sona or subscribe new shares; expected gain, its line, tax on proceeds and net cash; confirm or correct Rs 900 Cr (above the EV-implied Rs 857.5 Cr before tax); where are Q2 deal costs booked", from_finding_id: "RES:F1-01, RES:F7-01, A3-F8-01, A5 M2"}
  - {q: "Royalty rate, base and term each partner receives from its majority JV", from_finding_id: "RES:F6-02"}
  - {q: "Share of Q2 rev ops and of the Rs 16.3 bn 2W motor/controller additions inside the DENSO perimeter; which subsidiary made the Rs 39.06 Cr ex-forex op EBITDA of the subsidiary layer", from_finding_id: "RES:F2-02, RES:F3-01, P-A3-F16-04, P-A3-F6-01, A3-PR-F6-01"}
  - {q: "State Q2 EBITDA and margin ex-forex (forex Rs 10.58 Cr in revenue); realised forex in H1 and Q2 given the H1 Rs 11.67 Cr unrealised loss add-back against a Rs 19.75 Cr H1 P&L gain", from_finding_id: "RES:F2-05, P-A3-F16-01, A3-PR-F14-01, A3-F17-07"}
  - {q: "What does the five-year margin exercise show for FY28; what commodity path returns 24%+; robotics R&D bps cost; why deck understates margin declines", from_finding_id: "A3-F6-02, A3-F7-01, A3-F7-02, A3-F6-06, P-A3-F14-03"}
  - {q: "Is freight (nearly doubled QoQ) passed through; how much of the +20.9% QoQ other-expense rise is freight", from_finding_id: "A3-F7-05"}
  - {q: "Warranty provision Rs 12.49 Cr vs 2.18 and slow-moving inventory Rs 8.02 Cr vs 1.20: which products and entities; recurring", from_finding_id: "RES:F12-03, A3-PR-F17-04, A3-F17-10"}
  - {q: "Why did ST borrowings double to Rs 461.97 Cr while treasury rose; tenor and rate; 9M CFO/PAT ex-payables; MSME dues within 45 days; FY26 FCFO in rupees", from_finding_id: "RES:F12-02, P-A3-F17-02, A3-F17-04, A3-PR-F16-03"}
  - {q: "Name the dividend-paying WOS, the Rs 33.05 Cr investee and the borrowing subsidiary; is there an intra-group loan to the parent", from_finding_id: "RES:F2-03, RES:F2-06"}
  - {q: "Name the five foreign subsidiaries; Novelic carrying value and impairment test; which entity holds Rs 299.66 Cr capitalised development", from_finding_id: "RES:F3-02, RES:F12-01, RES:F2-04, A3-F17-06"}
  - {q: "Un-normalised ROCE and ROE; which ROCE footnote is correct; dated path to >18%", from_finding_id: "P-A3-F14-01, A3-F17-05"}
  - {q: "Gross order book; define consumption (Rs 25 bn vs Rs 15.5 bn revenue); itemise unitemised adds; robotics book rise; 6.6 vs 6.9 bn; asterisk footnote", from_finding_id: "P-A3-F7-01, P-A3-F16-03, A3-PR-F14-03, A3-PR-F14-04, A3-F14-03"}
  - {q: "Why report 'EV and Robotics' 65% instead of EV-only 61%; EV-only trend", from_finding_id: "A3-PR-F16-01, A3-F17-03"}
  - {q: "Are the seven SOP dates firm; FY27-FY28 capex envelope; capital blocked for JV2", from_finding_id: "P-A3-F6-02, A3-PR-F6-02, P-A3-F16-08"}
  - {q: "Which four programs entered production in Q2; did any robotics SOP occur (C2); new dates", from_finding_id: "P-A3-F16-09, P-A3-F17-05, A3-PR-F17-02, A3-F17-02, A3-F7-04"}
  - {q: "Define 'commercialised' for LSD, air springs, rear radar: customer, Q2 revenue, SOP; is the 2W rear radar the promised ADAS short-range radar (C3)", from_finding_id: "P-A3-F6-03, A3-PR-F14-05"}
  - {q: "H1 BEV revenue in Rs Cr and share of total revenue; reconcile spoken 2,042 Cr and 51% on three bases", from_finding_id: "A3-F14-01, A3-F14-02"}
  - {q: "Railway H1 revenue and PAT; fresh PO intake needed beyond the 12-month Rs 9 bn book", from_finding_id: "P-A3-F6-04, A3-F17-09"}
  - {q: "Suspension motors (about 7% of revenue): share from one customer and model; date of a second customer", from_finding_id: "A3-F7-03"}
  - {q: "Is the 1.5x cash/EBITDA threshold gross or net, trailing or forward; action when crossed", from_finding_id: "A3-F6-04"}
  - {q: "Which motor product launches in Q3 FY27; 3W share of traction-motor revenue", from_finding_id: "A3-F6-05"}
  - {q: "10X ambition: metric, base year, end year", from_finding_id: "A3-PR-F6-03"}
  - {q: "Review reports signed 13:26/13:27 before the 14:00 board, second quarter running: what did the auditor sign against", from_finding_id: "RES:F14-01"}
monitorables:
  - {item: "Q3 motor product launch", implied_date: "Oct-Dec 2026 (Q3 FY27)", source_ref: "call L561-562 [ASR]; A3 K07"}
  - {item: "Traction-motor extra volumes SOP, Rs 12,500 mn", implied_date: "H2 FY27 (Oct-2026 to Mar-2027)", source_ref: "deck L201-209; PR L132-135"}
  - {item: "DENSO JV1 close (carve-out); eDrive leaves WOS list; NCI or equity line; carve-out EBITDA/PAT; cash to Sona capped at Rs 857.5 Cr pre-tax", implied_date: "end-Dec 2026, may slip to Jan 2027", source_ref: "call L439-440 [ASR]; res L318-319, L448"}
  - {item: "Q3 FY27 results: consolidated op margin incl/ex forex; payables days", implied_date: "about late Jan 2027", source_ref: "Step 8C; Notion 26-Oct separating observation"}
  - {item: "Bharat Expo robotics demonstration", implied_date: "Feb 2027", source_ref: "call L764-767 [ASR]"}
  - {item: "DENSO JV2 formed and closed", implied_date: "H1 CY2027 (Jan-Jun 2027)", source_ref: "call L443-445 [ASR]"}
  - {item: "Cash/EBITDA crosses 1.5x; capital allocation decision", implied_date: "by FY27 year end (Mar 2027)", source_ref: "call L698-700 [ASR]"}
  - {item: "Q4 FY27 results; full-year CFO/PAT ex-payables", implied_date: "about May 2027", source_ref: "Step 5"}
  - {item: "IMC E2W SOP Rs 3,800 mn; differential gears Rs 2,000 mn SOP", implied_date: "H1 FY28 (Apr-Sep 2027)", source_ref: "deck L201-207, L234-240"}
  - {item: "FY27 annual report: Novelic KAM, corporate guarantees, entity list", implied_date: "about Jun-Jul 2027", source_ref: "RES:F3-02; tripwires 3 and 5"}
  - {item: "Railway order book Rs 9 bn executed; refill (growth trigger #1 AMBER / UNVERIFIED)", implied_date: "within 12 months (about Sep 2027)", source_ref: "deck L257, L267"}
  - {item: "Q1 FY28 results; third-call silence test (forex basis, ROCE, Novelic, railway P&L)", implied_date: "about late Jul 2027", source_ref: "Role 5 Step 3E"}
  - {item: "Rear radar 2W SOP Rs 1,000 mn; ICE diff assembly Rs 1,600 mn", implied_date: "H2 FY28 (Oct-2027 to Mar-2028)", source_ref: "deck L205, L238; PR L141, L151"}
  - {item: "Helical LSD Rs 7,000 mn; starter motors Rs 3,300 mn SOP", implied_date: "H1 FY29 (Apr-Sep 2028)", source_ref: "deck L205, L238; PR L126, L145"}
  - {item: "Auditor signing time vs board start at each results day", implied_date: "each results day", source_ref: "res L128, L418, L49"}
flags:
  - "Margin gate basis ruling pending: 23.20% incl forex vs 22.51% ex-forex; ex-forex below bear line second quarter"
  - "Cash leg ruling pending: CFO/PAT 1.48x printed vs 0.78x ex-payables (1.00x a year ago); cash INDETERMINATE-WITH-DIRECTION"
  - "C1 MISSED (conceded), C2 DROPPED on silence, C3 DELAYED; provisional credibility 8.3% grade D, archetype EVASIVE on one scored quarter; page shows Mgmt grade A"
  - "Auditor review reports signed about 33 min before the board met, second quarter running"
  - "DENSO JV1 close end-Dec/Jan [ASR]; Note 5 leaves consolidation route open; eDrive economics undisclosed"
  - "DENSO 49% at EV Rs 1,750 Cr = Rs 857.5 Cr pre-tax, about 2.2x proxy sales (1.8x ASR run-rate) vs about 10.1x for Sona; carve-out EBITDA/PAT NOT FOUND; fair price vs value transfer unseparated"
  - "Parent standalone op margin -343 bps YoY; group margin held via subsidiary layer (op EBITDA 3.6x incl eliminations)"
  - "Short-term borrowings doubled 234.25 to 461.97 Cr while treasury rose"
  - "EV share of order book 61%, third easing (tripwire 9); release reframed as 65% EV plus Robotics"
  - "Order-book consumption 1.6x revenue; Rs 4.8 bn adds unitemised"
  - "Warranty provision 5.7x and slow-moving inventory provision 6.7x YoY"
  - "ROCE 16.4% normalised under two definitions; un-normalised ND"
  - "Two-call silences: forex basis, ROCE number, Novelic, railway P&L, DENSO terms, order-book bridge"
  - "Railway growth trigger #1 and tripwire 8 both AMBER / UNVERIFIED"
  - "Tracker rows not supplied; fewer than three signals; reopen Role 5.5"
  - "Notion holds no FY27/FY28 projections; growth-trigger #3 label conflict on page"
  - "Concall is machine ASR: concall-only numbers unverified; filed documents govern"
  - "Promoter-group representative not on call; operator to confirm yellow flag"
  - "No thesis-broken trigger fired; Decision Status WATCHLIST unchanged (operator-only)"
  - "Role 4 Steps 6.5/7 and Role 5 Step 8D deferred to /fttcp and Role 1 (OR-30)"
plain_language_brief_included: true
analyst_note: "Consolidated is the basis. Q2 revenue +34.9% YoY is real, but the parent's own op EBITDA rose only 13.3% on +30.3% revenue (margin 26.26% to 22.83%); the group margin held at 23.20% because the subsidiary layer's op EBITDA rose 3.6x (incl. eliminations). The cash leg passes as printed (1.48x) but is 0.78x ex-payables against 1.00x a year ago. The margin gate turns on the pending forex ruling. Promise scoring rests on one quarter and three items, so grade D and EVASIVE are provisional. DENSO pays EV Rs 1,750 Cr for 49% (Rs 857.5 Cr pre-tax): about 2.2x proxy sales against about 10x for Sona, priced before the Q2 surge; carve-out earnings are NOT FOUND, so fair price and value transfer cannot be separated. Loop 1: FY28E-B now uses the labelled deck 23% CAGR because the FY21 bar is positional only; the FY26 bar ties to filed revenue incl. forex. Railway is AMBER / UNVERIFIED throughout. Concall numbers are ASR and lose to filings."
review_path: "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/qr-sonacoms-q2fy27-c7173c/runs/sonacoms-q2fy27/work/review_sonacoms_q2fy27.md"
loop1_changes:
  - "M1: preamble deck ledger 317 + M01-M15 = 332 rows reviewed; M-IDs cited at use (M01, M04, M05, M08, M09); deck L516 44,752 tied to filed FY26 rev ops + forex (44,751.48 mn, res L470-471); FY28E-B re-derived on labelled 23% 5-year CAGR (R242, deck L583-587): 6,979.12 / 993.52 / EPS 15.92 / 55.2x (was 7,001.81 / 996.75 / 15.97 / 55.0x)"
  - "M2: DENSO 49% stake-sale economics subsection added after Step 6.5/7; EV Rs 1,750 Cr, 49% = Rs 857.5 Cr pre-tax, taxable [ASR]; carve-out EBITDA/PAT NOT FOUND; EV/proxy sales 2.19x (1.81x ASR run-rate) vs Sona 10.1x; two readings and separating observation; bull-fork cash capped at Rs 857.5 Cr pre-tax; primary vs secondary route flagged; grafted into 0D, 6D, 6.5/7 table, 8B, Q2, 5A, 4C, 8D, 8E, Section C, flags, brief parts 1, 3, 5"
  - "F1: brief part 2 BEV +129% cause re-tagged [ASR, call L135-140]; concentration counter added (call L077-080; deck L196-203; PR L128-135; call L241, L417); 7A row added"
  - "F2: brief part 4 corrected: CY25 first joint dip; starter share also fell CY21 4.6% to CY22 4.1% (deck L703)"
  - "C1: railway aligned to AMBER / UNVERIFIED in 6B tripwire 8, 6D trigger #1, Role 5 8A and 8B, Section C, brief; single railway evidence set R in Step 6B"
  - "Style S1-S9, S11, S12 applied; S10 skipped (A2 ledger housekeeping, not an A4 file)"
  - "Verdict unchanged: PROCEED WITH FLAGS"
```
