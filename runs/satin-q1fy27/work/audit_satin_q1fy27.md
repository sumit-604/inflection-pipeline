# A5 ADVERSARY / COMPLETENESS AUDIT — SATIN CREDITCARE (NSE: SATIN) — Q1 FY27

Target: `review_satin_q1fy27.md` (A4). Fresh context: audited only against A1
extracts and A2 ledgers; A3 reasoning not consulted; all cites re-derived, not
deferred to. Conversion Lakhs x0.01 = Rs Cr applied independently.

---

## 1. COVERAGE AUDIT

Fresh grep + line-by-line re-enumeration of each extract, diffed against the A2
ledgers and against A4's citations.

| Category | A2 count | My fresh count | Orphan rows (in ledger, absent from A4) | Status |
|---|---|---|---|---|
| Results — agenda items | 1 | 1 (extract ln 37-39) | none | PASS |
| Results — statement blocks (std+consol P&L) | 2 | 2 | none | PASS |
| Results — auditor LRRs / substantive paras | 2 / 13 | 2 / 13 (std 5 @ln90-145; consol 8 @ln467-552) | none (0D covers opinion, Other-Matters, balancing, Reg-53 title) | PASS |
| Results — entities | 6 | 6 (ln 513-520) | none | PASS |
| Results — notes | 32 | 32 (std 16 @240-428; consol 16 @653-802) | Note 3 (NCD security), Note 11 (project-finance NIL), Note 12-std (recovery ratings Rs 83.87 Cr) not in 0D table | PASS (0D is expressly "comparability-relevant"; these are nil/administrative "reviewed-no-finding" class; see Note A) |
| Results — line items | 144 | 144 (std 70 + consol 74) reconciled to extract | none material | PASS |
| Results — zero-standing rows | 29 | 29 | none | PASS |
| Press release — disclosure units | 112 | 112 (44+19+2+10+6+20+11); 6 pages grep-confirmed | none | PASS |
| Presentation — slides | 42 | 42 (`[page` grep = 42) | none | PASS |
| Presentation — OCR dividers | 6 | 6 (pp 2,4,13,28,34,42) | none | PASS |
| Presentation — KPI line items / footnotes | 240 / 55 | reconciled by sampling | none | PASS |

**Reg 52(4) consolidated sector-ratio absence — handled honestly? YES.** A4
treats consol GNPA/NNPA/PCR/CRAR/LCR as `ND` (preamble item 2; table 5.b; flags;
verdict) and NEVER substitutes the standalone analogue. Independently confirmed
against the extract: the OCR-repaired consol Reg 52(4) table (ln 759-783)
"genuinely terminates at row 18 (Net profit margin) ... No GNPA/NNPA/PCR/CRAR/LCR
rows exist below row 18" (ln 782). The lone SFL GNPA 3.5% used is correctly
flagged DECK-ONLY (s31/L991), not filing. Clean pass on the core discipline test.

**Note A — A2 ledger staleness on consol Reg 52(4) (A2 housekeeping, not verdict-driving).**
The A2 results ledger (rows 7.14.7-7.14.18) flags consol Net worth as garbled
("2 1.98"), and NPAT / EPS / Operating-margin / Total-debts-to-assets as
`OCR_DROPPED_LINE` / not-visible. The CURRENT A1 extract carries an OCR-REPAIRED
consol table (ln 759-783, re-OCR at 400 DPI) with those cells CLEAN: Net worth
Rs 2,94,361.98 L = 2,943.62 Cr (ln 769), NPAT 12,264.56 L = 122.65 Cr (ln 770),
EPS 11.15/11.15 (ln 771-772), Net-profit-margin 16.04% (ln 781), Total-debts-to-
assets 0.78 (ln 777). A4's PREAMBLE follows the stale ledger ("Net worth (ln
771), NPAT and EPS ... garbled or dropped") yet the BODY correctly USES the
repaired values (consol NW 2,943.62 in the net-worth-gap table and Q7; NPM 16.04%
in 5.b). No row is dropped and every number A4 relies on ties to the extract, so
this is not an orphan/missing-row FAIL — but A2 should refresh those six rows
against the repaired extract, and A4's preamble line 46-48 mis-describes now-legible
cells (cosmetic, self-corrected in-body).

No orphan rows and no rows my fresh pass found that the ledger lacks.
**COVERAGE: PASS.**

---

## 2. ARITHMETIC AUDIT

Every derived figure recomputed from raw Lakhs in the extract. All headline lines
tie. Representative recomputations:

| Metric | A4 value | Recomputed (source) | Status |
|---|---|---|---|
| Std NII Q1FY27 | 363.14 | 632.03 (ln175) - 268.89 (ln187) = 363.14 | TIE |
| Std PPOP Q1FY27 | 258.11 | 157.96 (ln195) + 100.15 (ln189) = 258.11 | TIE |
| Std PAT Q1FY27 | 120.29 | 12,028.68 L (ln203) x0.01 | TIE |
| Consol PPOP Q1FY27 | 267.32 | 161.20 (ln603) + 106.12 (ln598) = 267.32 | TIE |
| Consol PAT Q1FY27 | 122.65 | 12,264.56 L (ln609) x0.01 | TIE |
| Consol PAT owners / NCI | 122.67 / (0.02) | 12,267.04 (ln622) / (2.48) (ln623) | TIE |
| Consol PBT YoY | +177.6% | 58.08 -> 161.20 = +177.5% | TIE |
| Consol PAT YoY | +171.9% | 45.10 -> 122.65 = +171.95% | TIE |
| Std PAT YoY | +182.4% | 42.60 -> 120.29 = +182.37% | TIE |
| Consol total income YoY | +8.0% | 707.84 -> 764.75 = +8.04% | TIE |
| Consol impairment YoY | -25.7% | 142.88 -> 106.12 = -25.73% | TIE |
| SC gap Q1FY27 (Rs / %) | +2.36 / +1.96% | 122.65-120.29=2.36; /120.29=1.96% | TIE |
| SC gap Q4FY26 | +25.10 / +18.33% | 162.05-136.95=25.10; /136.95=18.33% | TIE |
| SC gap Q1FY26 | +2.50 / +5.86% | 45.10-42.60=2.50; /42.60=5.865% | TIE (rounding; 5.865% -> 5.86/5.87 boundary) |
| SC gap FY26 | +30.13 / +9.97% | 332.21-302.08=30.13; /302.08=9.97% | TIE |
| Std ETR Q1FY27 | ~24% | 37.67/157.96 = 23.85% | TIE |
| Consol ETR Q1FY27 | ~24% | 38.55/161.20 = 23.92% | TIE |
| Deferred-tax credit std / consol | 4.72 / 7.45 | 472.20 L (ln200) / 744.80 L (ln607) | TIE |
| Overlay QoQ delta | +15 (21->36) | s17-note2/L495: 36 (Q1) - 21 (Q4) = 15 | TIE |
| Overlay Rs 36 Cr effect on PAT | Rs 15 Cr fresh drag | 36 - 21 = 15 incremental charge | TIE |
| Consol ROA/ROE/NIM QoQ step | -141 / -656 / -199 bps | 4.71->3.30 / 23.31->16.75 / 15.20->13.21 (s17 L486-489,482) | TIE |
| Net-worth gap std vs consol | 275.31 / 8.55% | 3,218.93 (ln389) - 2,943.62 (ln769) = 275.31; /3,218.93 = 8.55% | TIE |
| Escalation ROE annualised | 16.7% | 122.65 x4 / 2,943.62 = 16.67% | TIE |
| Off-book implied | ~3,270 (~25%) | 13,312 - 10,035 (on-book, s35/L1102) = 3,277 (24.6%) | TIE |
| Auditor unreviewed PAT share | 4.95% | 6.07 (606.58 L, ln535) / 122.65 = 4.95% | TIE |
| Warrant value | Rs 100.1 Cr | 38,50,000 x 260 = 100.10 Cr (ln279) | TIE |
| ESOP share add | +70,000 (+Rs 7.00 L) | 11,011.32 - 11,004.32 = 7.00 L /10 = 70,000 | TIE |
| Consol PAT bridge YoY | +78 (45->123) | +103 NII -37 opex +37 credit -26 tax = +77 (~78) | TIE |
| Consol PAT bridge QoQ | -39 (162->123, -24.3%) | 122.65-162.05 = -39.40; /162.05 = -24.3% | TIE |

No arithmetic mismatch above rounding. The single boundary item (Q1FY26 SC gap
5.865% shown as 5.86%) is within rounding tolerance, not a FAIL.
**ARITHMETIC: PASS.**

---

## 3. ADVERSARIAL READ — three most-positive claims, strongest bear counter each

### Claim A (most positive): "All three escalation conditions MET on reported numbers -> escalation gate MET, recommend escalate toward BUY" (Step 6C / Step 8).
**Strongest bear (same text):** the gate hangs on a consol ROE of 16.75% that
clears its 16% floor by only 75 bps, is a simple x4 annualisation of a single Q1,
and rests on a PAT flattered by a Rs 62.43 Cr FX finance-cost CREDIT (ln 597) that
was a CHARGE in Q4 (Rs 92.63 Cr) and in Q1FY26 (Rs 28.18 Cr); and the GNPA leg is
mechanism-unverified.
**Survives? NO — already fully incorporated.** A4 states the "thin"/"fragile"
75-bps clearance (6C caveat i), the FX reversal risk (diagnostic 6, Q8, Bear,
flag 7), and the unverified GNPA mechanism (INDETERMINATE cap, Q1, flag 2). No
graft required.

### Claim B: "PPOP grew +33% consol / +36% standalone on genuine operating leverage, NOT treasury timing" (Step 2 diagnostics 3 & 5; Bull).
**Strongest bear (same text):** PPOP is struck after the finance-cost FX line, so
the Rs 62.43 Cr Q1FY27 FX credit vs the Rs 28.18 Cr Q1FY26 FX charge is a ~Rs 90 Cr
favourable swing that mechanically inflates PPOP growth.
**Survives? NO — counter fails on the extract.** The FX credit is one leg of a
100%-hedged pair; the offsetting MTM fair-value LOSS sits in revenue, also above
PPOP. Net treasury effect on PPOP = consol -56.73 (ln588) + 62.43 (ln597) = +5.70
Cr (Q1FY27) vs +32.68 (ln588 py) - 28.18 (ln597 py) = +4.50 Cr (Q1FY26): a ~Rs 1.2
Cr YoY delta against +66 Cr of PPOP growth. A4's "not treasury timing" claim is
CORRECT. No graft required.

### Claim C: "AUM +27.5% consol / +21.5% standalone Strong; T1 branches ON TRACK; growth-visibility premium HOLD; FY2030 AUM target raised to Rs 32,000 Cr" (Step 2, 6B, 6D-T1, 7).
**Strongest bear (same text):** the company's OWN snapshots show AUM +22-27% YoY
but ACTIVE CLIENTS only +3% YoY — consol 34 vs 33 lakh (+3%, s14/ln399-401) and
standalone 33 vs 32 lakh (+3%, s15/ln419-421) — while NEW CLIENTS ADDED are
DECLINING every quarter (1.9 -> 2.5 -> 2.2 -> 1.6 -> 1.5 lakh; deck 4d). With SCNL
JLG avg ticket at Rs 61,000 (s36/L1147), ~19 pp of the standalone AUM growth is
deeper per-borrower exposure on a near-static client base, not client acquisition —
a recognised MFI over-indebtedness / growth-quality early-warning, in the same
cycle whose stress A4 elsewhere treats as normalising.
**Survives? YES.** Extract-supported and NOT surfaced anywhere in A4 (no
diagnostic, monitorable, Bear line, or QfM addresses client-count vs AUM
divergence or the declining new-client run-rate). This must be grafted into A4
before save — minimally into the Bear column and as a Q2 monitorable, ideally as a
Questions-for-Management row (ticket-size vs client-acquisition mix; per-borrower
indebtedness trend). **-> loop back to A4.**

### Adversarial discipline checks (all confirmed except where noted)
- AMBIGUOUS/FORWARD-SIGNAL -> question coverage: every FND-01..10, every
  presentation A3-01..12, and 8/9 press-release A3-F findings map to a QfM row
  (Q1-Q12 `from_finding_id`). **A3-F6-01 is the sole finding with no QfM row**; A4
  routes the F6 commitment register into the Monitorables/Catalyst timeline
  (and its principal item, the promoter warrant, also appears in Q6). Acceptable
  as a NEUTRAL/commitment destination, but flagged for A4 to confirm A3-F6-01 is
  not a FORWARD-SIGNAL owed a discrete question.
- No AMBIGUOUS finding silently upgraded to fact: SFL GNPA (deck-only), consol
  sector ratios (ND), Q2-Q4 mid-quarter chart values (CHART_LAYOUT_AMBIGUOUS) all
  carried with their hedges intact. PASS.
- Trigger stated as FLAG, not a Decision Status change: "A4 FLAGS; the human
  decides. Decision Status is NOT changed" (6C, Step 8, verdict). PASS.
- Verdict within PROCEED set and INDETERMINATE-capped: PROCEED WITH CAVEATS,
  explicitly capped by the INDETERMINATE asset-quality/cash-conversion read with
  the four missing-evidence items named. Consistent with the house rule. PASS.

---

## VERDICT

**INCOMPLETE.** One surviving bear counter (Claim C) is supported by the company's
own extracted disclosure and is absent from A4's review; per the adversarial-read
discipline it must be grafted before save.

- **Loop back to: A4.**
- **Exact gap:** A4 asserts AUM growth as unqualified "Strong" and holds the
  growth-visibility premium, but never surfaces that Active Clients grew only +3%
  YoY (consol 34 vs 33 lakh, ln 399-401; standalone 33 vs 32 lakh, ln 419-421)
  against AUM +22-27%, with new-client additions declining 1.9 -> 1.5 lakh/qtr
  (deck Table 4d). Add this ticket-size-led / static-client-base growth-quality
  bear point to the Bear column and monitorables (and ideally a QfM row on the
  ticket-size vs client-acquisition mix and per-borrower indebtedness trend).
- **Secondary (non-blocking, for the same loop):** (i) A4 preamble ln 46-48
  mis-describes consol Reg 52(4) Net worth/NPAT/EPS as garbled/dropped though the
  repaired extract (ln 759-783) and A4's own body use them cleanly — align the
  preamble; (ii) confirm A3-F6-01 is adequately discharged by the Monitorables
  register rather than a QfM row.
- **For A2 (housekeeping):** refresh consol Reg 52(4) rows 7.14.7/7.14.8/7.14.9/
  7.14.14/7.14.17/7.14.18 against the OCR-repaired extract (values now legible);
  no row is missing, so gate_a2 stands, but the flags are stale.

Coverage and arithmetic both PASS independently. The single blocking item is the
unincorporated surviving bear counter.

```yaml
stage: A5-adversary
company: "SATIN"
quarter: "Q1FY27"
model: claude-opus-4-8
status: complete
verdict: INCOMPLETE
coverage:
  orphan_rows: []
  missing_from_ledger: []
arithmetic_mismatches: []
surviving_bear_counters:
  - claim: "AUM +27.5% consol / +21.5% standalone Strong; growth-visibility premium HOLD; FY2030 AUM target raised"
    counter: "Active Clients grew only +3% YoY (consol 34 vs 33 lakh; standalone 33 vs 32 lakh) against AUM +22-27%, with new-client additions declining 1.9->1.5 lakh/qtr; growth is ticket-size/per-borrower-exposure led on a near-static client base, an MFI over-indebtedness early-warning A4 does not surface"
    source_line: "presentation s14 ln399-401 / s15 ln419-421 / deck Table 4d new-clients / s36 L1147 avg ticket Rs 61,000"
loop_back_to: "A4"
gap: "Graft the client-growth-vs-AUM divergence bear counter (Active Clients +3% YoY vs AUM +22-27%; new-client adds declining 1.9->1.5 lakh/qtr) into A4's Bear column, monitorables, and ideally a Questions-for-Management row on ticket-size vs client-acquisition mix and per-borrower indebtedness. Also align preamble ln46-48 (consol Reg 52(4) NW/NPAT/EPS are legible in the repaired extract, not dropped) and confirm A3-F6-01 discharge via the Monitorables register."
```
