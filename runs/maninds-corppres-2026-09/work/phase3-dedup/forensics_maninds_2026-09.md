# MANINDS Corporate Presentation (01 Sep 2026) — A3 FORENSIC NOTES (doctype: presentation)

Inputs read: A1 structured (`extracted/maninds-presentation-2026-09-structured.md`, R001-R335),
A1 fulltext (`extracted/maninds-presentation-2026-09-fulltext.md`), A2 ledger
(`work/phase3-dedup/ledger_presentation_maninds_2026-09.md`). No source PDF, no inputs/ opened.
Ledger reconciliation: 335 / 335 structured rows accounted (100%). No prior-quarter deck supplied
(prior_ledger_path: none) — F16 dropped-disclosure diff and F15 prior-list diff not runnable; noted per check.

Notion tripwires carried in: consol vs standalone PAT divergence; EBITDA margin ex-other-income vs 13%
floor; ROCE clean basis; net-debt vs net-cash; NPC acquisition economics/integration; Jammu/Dammam
commissioning Mar 2027; India order-book split; working-capital direction.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| A3-01 | F16 | R153, R165 (A2 FOOTNOTE_UNRESOLVED, now resolved) | line 775 / 812, slide 28-29 | "EBITDA is inclusive of Other Income, since it's operational in nature" | AMBIGUOUS | The 13.0% consolidated EBITDA margin headline (R166) includes Rs286 Mn other income. Ex-OI EBITDA = 4,393 Mn -> 12.3% on revenue 35,639, BELOW the 13% floor tripwire. Standalone ex-OI = 12.7% (vs 14.0% headline). The margin milestone is reached only by folding other income into EBITDA. A4 question: normalise both margins ex-OI and test against the 13% floor. |
| A3-02 | F16 | R210, R211 | line 866-870, slide 31 | "Gross Profit ... FY25 7,905 ... FY26 13,639 ... 22.4% ... 38.0%" | AMBIGUOUS | Consolidated gross-profit margin jumps 1,560 bps (22.4% -> 38.0%) in one year on ~flat revenue (+1.7%), while EBITDA margin rises only 290 bps. A gross-profit redefinition or cost reclassification between COGS and operating expenses is the likely cause. Reframes the historical gross-margin baseline. A4 question: what changed in the gross-profit build FY25 vs FY26? |
| A3-03 | F2 | R159 (standalone PAT), R171 (consol PAT), R149/R161 (revenue) | line 769 / 806, slide 28-29 | "PAT ... 1,958" (standalone FY26) vs "PAT ... 1,705" (consolidated FY26) | FORWARD-SIGNAL | Consol PAT sits BELOW standalone in FY26 (1,705 < 1,958; subsidiaries drag -253 Mn), reversed from FY25 (consol 1,532 > standalone 1,370; +162 Mn accretive). Swing = 415 Mn = 21% of standalone PAT, far above the 5-pt threshold. Consol revenue grew 1.7% vs standalone 10.8%: subsidiary/elimination revenue fell from 3,872 to 1,087 Mn. Directly the Notion S-vs-C PAT tripwire. A4: name which subsidiaries turned dilutive (pre-NPC MISIC/Merino/Jammu build carry). |
| A3-04 | F10 | R173 | line 823, slide 30 | "Equity Share Capital ... 324 ... 324 ... 375" | AMBIGUOUS | Paid-up capital rose 15.7% FY25->FY26 (324 -> 375 Mn); Other Equity rose 4,741 Mn (15,749 -> 20,490). Traces to an equity raise (NPC funding carried USD 32 Mn equity component). Deck discloses no share count, instrument, or EPS despite "except EPS" table headers. A4/Notion: verify warrant/preferential terms and dilution vs thesis share count. |
| A3-05 | F14 | R088/R103/R324/R325 vs R110/R264/R323 (A2 DATA_INCONSISTENCY) | line 468/531/639/685 vs 569/579, slide 19-25 vs 22 | "Since more than two decades" / "since 2005" vs "40+ Years" | AMBIGUOUS | Same NPC-Aramco relationship dated ~20-21 years (pages 19/21/24/25) and "40+ Years" (page 22, twice) inside one acquisition section. Both cannot be the same start date. The stronger "40+ Years" framing underwrites the durability claim. A4: do not anchor a durability claim to either figure; reconcile against the NPC transaction documents. |
| A3-06 | F15 | R261/R263 (NPC), R260 (MISIC), R333 | line 481/507, 476, slide 19/20/32; date line 938 | "completion of 100% acquisition on 21st May 2026" | FORWARD-SIGNAL | NPC enters the consolidation perimeter 21 May 2026 via new WOS vehicle MISIC; Q1FY27 carries only 40 days (R220), full earnings from Q2FY27 (R286/R334). FY27 consolidated statements will restructure materially. No prior-quarter consolidation list supplied, so a full add/drop diff is not runnable; the disclosed relationship change is surfaced. |

---

## CHECKLIST SCORECARD

| Check | Status | Basis |
|---|---|---|
| F1 ZERO-STANDING | PASS | Both zero-standing rows benign: R194 Intangibles (FY24 nil, FY25 5, FY26 3) and R206 Current Tax Assets (nil all years). No exceptional / profit-on-sale / discontinued-ops line held at zero. |
| F2 S-vs-C DECOMPOSITION | FINDING | A3-03. Consol PAT falls below standalone in FY26 (drag -253 Mn) vs +162 Mn accretive FY25; 415 Mn swing = 21% of standalone PAT. Consol revenue +1.7% vs standalone +10.8%. |
| F3 SHELL-ENTITY | N.A. | Deck gives no standalone-vs-consolidated cost-line split (Materials/Employee/Depreciation); shell test not runnable on a presentation. |
| F4 UNAUDITED RATIO | N.A. | No auditor Other Matters paragraph in a presentation. |
| F5 GOING CONCERN / EoM | N.A. | No auditor EoM in a presentation; no prior deck for verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Eleven dated/dateable commitments (Dammam Mar'27, Jammu Mar'27, Merino launch Mid-Sep'26, NPC full earnings Q2FY27, 5-yr 20-25% CAGR, 15% EBITDA). See Commitment Register. Feeds Role 5 tracker. |
| F7 HEDGE MINING | PASS | Only deck-wide safe-harbor boilerplate (R269, lines 1013-1037). No note-specific hedge newly added on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | PASS | Standalone ETR 25.6% FY26 / 26.1% FY25; consol ETR 28.1% / 26.5% — near statutory 25.17%. DTL stable (R178: 258/276/258). No "earlier-years" tax-adjustment line. NPC Saudi/Zakat rate 11.4% (R133) is a future consolidated ETR tailwind, not a flag. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in the deck. |
| F10 SHARE COUNT / DILUTION | FINDING | A3-04. Paid-up capital +15.7% FY25->FY26 (R173); no share count / instrument / EPS disclosed. |
| F11 NET WORTH TIE-OUT | PASS | Other Equity 20,490 + Paid-up 375 = Shareholders Fund 20,865 (R175); ties to slide-4 Networth Rs2,087 Cr within rounding. No unexplained gap. |
| F12 SEGMENT FORENSICS | N.A. | No IND-AS segment asset/liability tables in the deck. |
| F13 BOARD OUTCOME | N.A. | Reg-30 investor-meeting intimation, not a board-outcome filing; no AGM notice, no director term dates. |
| F14 NOTE DRAFTING INCONSISTENCY | FINDING | A3-05. Aramco relationship dated "2+ decades"/"since 2005" (pp19/21/24/25) vs "40+ Years" (p22) inside one NPC section. Minor typos noted (line 208 "non only", 210 missing "since", 1017 "may forward-looking"). |
| F15 ENTITY LIST DIFFS | FINDING | A3-06. NPC newly consolidated 21 May 2026 via new WOS MISIC. No prior-quarter list supplied, so full add/drop diff not runnable; disclosed change surfaced. |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | A3-01 (EBITDA inclusive of other income) and A3-02 (gross-profit margin 22.4%->38.0% reclassification). Prior-deck drop diff not runnable (no prior deck). |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall / transcript. |

Counts: FINDING 6 (F2, F6, F10, F14, F15, F16) | PASS 4 (F1, F7, F8, F11) | N.A. 7 (F3, F4, F5, F9, F12, F13, F17) = 17.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Dammam Coating Plant (KSA) production | Mar 2027 | R273/R300, slide 5 | targeted |
| Jammu SS Plant production (Rs350cr of Rs600cr capex incurred) | Mar 2027 | R274/R277/R318, slide 5/16 | underway |
| Merino Shelters project launch | Mid-September 2026 | R280/R321, slide 17 | on track |
| Merino cashflow Rs35-50 Cr | FY27 | R281, slide 17 | expected |
| Merino annual cashflow starts | FY28 | R278/R320, slide 17 | expected |
| Merino revenue Rs700-800 Cr | next 5-6 years | R279, slide 17 | expected |
| NPC full earnings contribution | Q2 FY27 | R286/R334, slide 32 | expected |
| NPC 100% stake acquisition | 21 May 2026 | R333, slide 32 | completed |
| NPC HSAW OD upgrade to 120" | no date given | R107, slide 21 | will be upgraded |
| Revenue CAGR 20-25% | next 5 years | R291, slide 34 | goal |
| EBITDA margin to 15% long-term | 5-year horizon | R292, slide 34 | goal |

---

## ANALYST NOTE

The load-bearing forensic item is margin quality. A2 left the EBITDA asterisk UNRESOLVED; the
fine print sits at lines 775/812: EBITDA "inclusive of Other Income." Strip it and consolidated
FY26 EBITDA margin is 12.3%, under the deck's own 13.0% headline and the Notion 13% floor. The
gross-profit line compounds this: 22.4% -> 38.0% in one year on flat revenue reads as a COGS/opex
reclassification, not real gross-margin gain. Both reframings inflate the transition optics A4 will
weigh. Separately, consolidated PAT dropping below standalone (subsidiaries turned dilutive -253 Mn)
runs opposite to the growth story and must be decomposed before NPC (Q2FY27) muddies the base. The
15.7% paid-up-capital rise is undisclosed dilution to size. Findings A3-01/02/03/04/05 are all
management questions for A4; A3-06 is a structural heads-up for FY27 consolidation.
