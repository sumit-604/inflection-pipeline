# A3 FORENSIC NOTES — India Glycols / IGL Spirits (Entity B) — 2026-09 — doctype: presentation

Source inputs (A1 + A2 only; source PDF never opened):
- structured: indiaglyco-presentation-spirits-2026-09-structured.md (R001-R355)
- fulltext:   indiaglyco-presentation-spirits-2026-09-fulltext.md (1008 lines)
- ledger:     ledger_presentation-spirits_indiaglyco_2026-09.md (355/355 rows, gate_a2 pass)

Reconciliation: 355 structured IDs, all grouped in A2 Table 1 (orphan_ids empty). Every
ledger row read at its cited fulltext line before judging. ledger_reconciled_pct = 100.

Doctype rule applied: F1-F15 where content exists; F16 applies (no prior deck supplied, so
the cross-quarter dropped-disclosure diff is NOT runnable — recorded, plus within-deck
reframing findings); F17 N.A. (concall-specific).

---

## FINDINGS TABLE

id | check | ledger row ref | slide/line | verbatim quote | classification | forward implication
---|-------|----------------|-----------|----------------|----------------|--------------------
FND-01 | F6 | R280,R281,R284,R285 (+R248,R254,R262,R263,R245) | slide 30 / L981-993 | "Aspire to Deliver in EBITDA over INR 550Cr by FY27" … "2x IMFL Volumes through new brand launches by FY27" … "Achieve a Debt Free Balance Sheet by FY28 & INR 1,000Cr EBITDA in next 3-4 years" | FORWARD-SIGNAL | Dated management commitments. Feed Role 5 promise-vs-delivery tracker; test EBITDA>550 and 2x IMFL volume at the FY27 print, debt-free at FY28.
FND-02 | F12 | R126-R131 (+R100,R101,R278) | slide 27 / L883-895 | "Bio-fuels … 1,470" vs "Portable Spirits … 1,331" (FY26) | FORWARD-SIGNAL | Bio-fuels (regulated OMC quota) overtook spirits in FY25 and is the larger, faster segment in FY26 (1,470 vs 1,331 Cr). Entity growth is increasingly policy/quota driven, not premiumisation. Segment assets/liabilities NOT disclosed. Only ESY 2025-26 allocation shown (220 mn L / Rs1,450 Cr, R100/R101); current ESY 2026-27 allocation absent despite the EBITDA guide leaning on "Structural Bio-fuel Demand Tailwinds" (R278).
FND-03 | F11 | R145-R147, R355 | slide 28 / L917-936 | "Net Debt is defined as Term loan plus Fund Based Working Capital minus Cash & Cash Equivalents" ; "767" (FY26) | AMBIGUOUS | Standalone net debt disclosed at Rs 767 Cr FY26 — below the ~Rs 1,050 Cr thesis trigger. But the definition excludes non-fund-based facilities (LC/BG), a possible understatement, and net worth itself is not disclosed, so the 20.5% RoCE denominator (Net Worth + Term Loan, R355) cannot be tied out. A4 question.
FND-04 | F14 | R126-R128 | slide 27 / L901 (+L289) | "Portable Spirits" (mislabel of Potable) ; "Non-IFML" (L289) ; "MaQintosh"/"Maqintosh" (R193/R224) | NEUTRAL-FACT | Cumulative drafting inconsistencies in an investor deck; individually immaterial, together a low-grade governance data point.
FND-05 | F16 | R354 | slide 27 / L905 | "PAT post Group's bifurcation into resulting companies" | AMBIGUOUS | FY24-26 PAT (88/151/244) is a post-bifurcation carve-out basis; period comparability limited. No prior deck supplied, so cross-quarter diff not runnable.
FND-06 | F16 | R352 | slide 21 / L722 | "Note: (1) As of FY26. (2) FY27E Projection." | AMBIGUOUS | Capacity slide mixes an FY26-actual figure with an FY27E-projected figure under one headline (~30mn cases potable / 136 Mn L). A projected number is presented beside actuals — confirm which capacity is live today.
FND-07 | F16 | R119,R109,R110-R115 | slide 26 / L834 | "Stable volumes coupled with premium portfolio expansion translate into strong value creation and margin enhancement" | AMBIGUOUS | Deck attributes the gross-margin rise (36.0%→41.9%→45.9%, R117-R119) to premiumisation. But cases were FLAT FY25→FY26 (30.1→30.0, R111/R112); all value growth came from realisation per case (947/25.0=~Rs3,788 → 1176/30.1=~Rs3,907 → 1331/30.0=~Rs4,437). That is consistent with premiumisation OR regulated UP/Uttarakhand country-liquor price hikes. Deck cites "Regulated demand" (L781) but never regulated pricing. Current-quarter Q1 FY27 volume/realisation NOT disclosed; deck shows favourable annual actuals instead. A4 question: mix or government-set price?
FND-08 | F16 | R155 vs R285 | slide 29 L947/970 vs slide 30 L993 | "~INR 1,000 Cr … FY31E" vs "INR 1,000Cr EBITDA in next 3-4 years" | AMBIGUOUS | Same Rs1,000 Cr EBITDA target carries two horizons — FY31E on the pathway chart, "next 3-4 years" (~FY29-30) in the outlook. ~1-2yr guidance inconsistency on a headline number. Ask which is live.

---

## CHECKLIST SCORECARD (all 17; PASS / FINDING / N.A.)

check | status | basis
------|--------|------
F1 ZERO-STANDING | N.A. | 0 ZERO_STANDING rows (A2 Table 4). Broker-meet deck, no standardised P&L/BS template that anticipates a zero-value transaction class.
F2 STANDALONE vs CONSOLIDATED | N.A. | No standalone-vs-consolidated split in the deck; IGL Spirits presented as a single post-demerger entity.
F3 SHELL-ENTITY | N.A. | No S-vs-C cost lines to compare.
F4 UNAUDITED CONTRIBUTION | N.A. | No auditor's Other Matters; presentation carries no audit opinion. (Comparability caveat captured at FND-05.)
F5 GOING CONCERN / EoM | N.A. | No going-concern / EoM paragraph in a presentation.
F6 FORWARD-COMMITMENT MINING | FINDING | FND-01. Dated commitments: "expected to be available … by FY-end" (R254), "under development" (R263), "slated for launch" (R262), "Expansion Underway" (R248), "expected to exceed 450mn by 2030" (R245), plus FY27/FY28/3-4yr targets.
F7 HEDGE MINING | PASS | Only boilerplate safe-harbor (R337, L86-103): "risks, uncertainties … could cause actual results to differ materially". No note newly adds a substantive hedge on lumpiness/concentration.
F8 TAX FORENSICS | N.A. | No tax line / ETR / deferred-tax data in the deck.
F9 OCI FORENSICS | N.A. | No OCI / actuarial data.
F10 SHARE COUNT / DILUTION | N.A. | No paid-up capital, share count or EPS; CIN only (R159).
F11 RESERVES / NET WORTH TIE-OUT | FINDING | FND-03. Net debt disclosed (728/900/767, R145-R147) under a narrow definition (R355); net worth not disclosed, RoCE denominator not verifiable.
F12 SEGMENT FORENSICS | FINDING | FND-02. Segment revenue given (spirits vs bio-fuels), assets/liabilities NOT disclosed; bio-fuels now the larger, regulated-quota segment; current-year ethanol allocation absent.
F13 BOARD OUTCOME | N.A. | No board's report / AGM notice / director term dates in the deck.
F14 DRAFTING INCONSISTENCIES | FINDING | FND-04. "Portable"/"Potable" (L901), "Non-IFML" (L289), "MaQintosh"/"Maqintosh".
F15 ENTITY LIST DIFFS | N.A. | No consolidation list and no prior-quarter list to diff. (Three-way bifurcation into IGL Spirits / India Glycols / Ennature Bio Pharma noted at R171/R172/R186/R354; carried in analyst_note.)
F16 DROPPED / REFRAMED | FINDING | FND-05,06,07,08. No prior deck so cross-quarter diff not runnable; within-deck reframing: post-bifurcation PAT basis, FY26/FY27E capacity mix, premiumisation-vs-regulated-pricing narration, split Rs1,000 Cr horizon.
F17 SILENCE AUDIT | N.A. | Concall-specific; this is a presentation.

Gate A3: PASS (every check marked; no blanks).

---

## COMMITMENT REGISTER (from F6)

commitment | implied date | ref | status word
-----------|--------------|-----|------------
EBITDA over INR 550 Cr | FY27 | slide 30 / R280 | aspire (guidance)
2x IMFL volumes via new brand launches | FY27 | slide 30 / R281 | planned
Debt-free balance sheet | FY28 | slide 30 / R284 | target
INR 1,000 Cr EBITDA | "next 3-4 years" (~FY29-30) AND FY31E on pathway chart — inconsistent | slide 30 R285 / slide 29 R155 | target (horizon conflict, see FND-08)
Amazing & Zumba available across 8 states | FY-end (FY27) | slide 13 / R254 | underway
Elite-tier portfolio expansion | undated | slide 12 / R248 | underway
Amazing Vodka & IGL Amazing Craft Whisky (CSD) | undated | slide 19 / R262 | slated for launch
Exclusive CSD-focused rum brand | undated | slide 19 / R263 | under development
CSD depot / brand-presence expansion | undated | slide 19 / R264 | to be expanded
Pipeline launches (Affluent ~2 whisky/~2 vodka; Premium +2; Deluxe +2) | undated | slide 12 / R249-R252 | in pipeline
White spirits 1Mn+ cases across 3 states | undated | slide 13 / R253 | targeting
India vehicle fleet >450mn (macro backdrop for ethanol) | 2030 | slide 10 / R245 | expected to exceed
