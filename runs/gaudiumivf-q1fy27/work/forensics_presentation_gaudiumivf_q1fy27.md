# A3 FORENSIC NOTES — GAUDIUMIVF — Q1 FY27 — DOCTYPE: PRESENTATION (Investor Presentation, 36 slides)

Source extract: `extract_presentation_gaudiumivf_q1fy27.txt`
Reconciliation contract: `ledger_presentation_gaudiumivf_q1fy27.md`
Ledger rows read verbatim at cited lines: 144/144 KPI units + 10 P&L rows + 2 Adj-EBITDA call-outs = 100%
Prior-quarter deck ledger: NOT PROVIDED (`NO_PRIOR_LEDGER`) — dropped-metric diff (part of F16) not possible this cycle.

Doctype note: this is a slide deck, not a full P&L/audit filing. The audit/balance-sheet
checks (F1, F3, F4, F5, F8, F9, F11, F12, F15) have no substrate in a deck and are
marked N.A. with a one-line reason. Weight is placed on the presentation-specific
forensics: adjusted/non-GAAP metrics (F16), management framing, selective disclosure,
forward-commitment mining (F6), the standalone-vs-consolidated decomposition the deck
itself carries (F2), and — most important — reconciling every deck number against the
filed reviewed results.

---

## DECK-vs-FILING RECONCILIATION (the core exercise)

Filed standalone figures (from cross-document context): revenue 13.68 Cr, reported PAT
1.66 Cr, operating EBITDA margin 15.90%, ~1,796 bps YoY margin collapse, S&M +140%
(~Rs 2.23 Cr / ~223 L standalone), Rs 1.02 Cr (~102 L) FD interest flattering PBT.

| Deck line (standalone, slide 26, lines 692-700) | Deck value | Filing | Ties? |
|---|---|---|---|
| Revenue from Operations | 1,367.73 L = 13.68 Cr | 13.68 Cr | YES |
| PAT | 166.35 L = 1.66 Cr | 1.66 Cr | YES |
| EBITDA (Ex. Other Income) margin | 15.89% | 15.90% | YES (rounding) |
| EBITDA YoY | -1797 bps | ~-1796 bps | YES |

Verdict: the deck's **reported / audit-traceable** standalone numbers tie to the filing
line by line. Nothing in the reported columns is fabricated or off.

What does NOT trace to the filing:
1. **"Adjusted EBITDA" 507.75 L / 37.12% (standalone, line 710) and 532.75 L / 27.49%
   (consolidated, line 737).** This is a deck-only non-GAAP construct. No reconciliation,
   no itemisation of the add-back, absent from the filed results. See F16 / read below.
2. **Consolidated column (slide 27)** cannot be independently reconciled — the
   cross-document context supplied only *standalone* filing figures. Flagged: consolidated
   basis is unverified against the filing here (`CONSOLIDATED_UNRECONCILED_VS_FILING`).
3. **Reported PAT is flattered by FD interest not called out.** Deck shows "EBITDA
   (Ex. Other Income)" (excludes other income on that line — conservative there), but the
   166.35 L PAT sits *below* the line and includes the ~102 L FD interest. The deck never
   discloses that roughly Rs 1.02 Cr of a Rs 1.66 Cr PAT is non-operating FD interest.
   Selective disclosure (F16 / FND-06).
4. **All operating KPIs** (8 hubs + 28 spokes, 367 OPU cycles, ARPU Rs 3.5 L, success
   62%/85%, FY27 2-of-10 hub guidance) are NOT in the filing — unaudited management
   claims. Treat as FORWARD-SIGNAL / unverified (F6, F16).

---

## THE Rs 290.35 L ADJUSTED-EBITDA ADD-BACK (single most important item)

- Standalone: reported EBITDA ex OI 217.40 + **290.35** = 507.75 (line 695 → line 710).
- Consolidated: reported EBITDA ex OI 242.40 + **290.35** = 532.75 (line 722 → line 737).
- The add-back is an **identical Rs 290.35 L in absolute terms at both the standalone and
  the consolidated level**, undisclosed and unreconciled in the deck (`ADJUSTED_EBITDA_GAP`,
  `CONSISTENT_ADJUSTMENT_AMOUNT`).

Read: this add-back does not hold together as a "normalisation for front-loaded expansion."
Two problems:
1. **It exceeds the stated driver.** The filing attributes the collapse mainly to S&M
   +140% (~223 L standalone). An add-back of 290.35 L is ~67 L (~30%) *larger* than the
   entire standalone S&M increase. So even if you accept adding back the S&M step-up, the
   number is over-scoped.
2. **An identical absolute add-back cannot be correct at two different consolidation
   levels.** The incremental expansion spend inside the consolidated group (extra
   subsidiary hubs, wider clinical hiring) would necessarily differ from the standalone
   figure. A single fixed Rs 290.35 L applied to both bases indicates a plugged/uniform
   number, not a genuinely re-computed group adjustment. It mechanically converts a 15.89%
   reported margin into 37.12%, and a 12.51% consolidated margin into 27.49%.

Direction (conservative bias): AMBIGUOUS leaning CONFIRMATORY-NEGATIVE. The add-back is
undisclosed, unreconciled, over-scoped vs its own stated cause, and arithmetically
incoherent across the two bases. It should not be relied on; it is a management-framing
device, not a reconcilable metric. Converts directly into an A4 management question:
*"Itemise the Rs 290.35 L Adjusted-EBITDA add-back; why is it identical in absolute terms
at standalone and consolidated; which line items and which entities does it comprise; and
how does it reconcile to the S&M increase in the filed results?"*

---

## FINDINGS TABLE

| id | check | ledger row ref | line / slide | verbatim quote | classification | forward implication |
|---|---|---|---|---|---|---|
| FND-01 | F2 | items 88/96 (S vs C PAT) | slides 26 & 27, lines 699 & 726 | "PAT 166.35" (std) vs "PAT (Continuing Operations) 177.59" (consol) | AMBIGUOUS | Subsidiary PAT contribution collapsed from ~72.5 L (30.9% of standalone PAT, Q1FY26) to ~11.2 L (6.8%, Q1FY27); consolidated entity is margin-dilutive (12.51% vs 15.89% EBITDA). Future consolidated drag / subsidiary stress. |
| FND-02 | F6 | items 65-69, 28, 92 | slide 22 lines 584/598/601; slide 7 line 174 | "2 out of 10 ... Hubs Launching Soon"; "expected to drive higher revenues" | FORWARD-SIGNAL | Dated expansion commitments (FY27 Delhi/NCR + Nagpur; FY28 8 centers; FY29 1) for the Role 5 promise-vs-delivery tracker and FTTCP catalyst timeline. |
| FND-03 | F13 | items 70-75 | slide 23 lines 622-642 | "Independent Director" (x3, no DIN, no term dates) | AMBIGUOUS | Cannot map independent-director term expiry against the FY27-FY29 commissioning window; governance data gap. |
| FND-04 | F14 | item 112 | slide 29 line 749 | "Additional Slide Proposed" | NEUTRAL-FACT | Leftover draft/template annotation in an investor-facing deck, plus multiple award-slide typos ("Pracice", "inferility", "Praibha Pail", "Fdamily"): document QC lapse, cumulative governance data point. |
| FND-05 | F16 | items 90/91, 98/99, 101 | slide 26 line 710; slide 27 line 737 | "Adjusted EBITDA is 507.75 being 37.12 % margin" | AMBIGUOUS (→CONFIRMATORY-NEGATIVE) | Undisclosed, unreconciled, identical Rs 290.35 L add-back at both bases; over-scopes the ~223 L S&M increase; recasts 15.89% reported margin as 37.12%. Not traceable to the filing. |
| FND-06 | F16 | items 76-84, 88 | slide 25 lines 653-685; slide 26 line 699 | "*Note: Margin Ratios are based on PAT from Continuing Operations."; snapshot revenue "1,937.66" | AMBIGUOUS | Headline "Financial Snapshot" silently uses **consolidated** figures (unlabeled, `CONSOLIDATED_BASIS_UNLABELED`); "Continuing Operations" label with no discontinued-ops disclosure; ~102 L FD interest inside PAT never called out. Selective framing. |

---

## CHECKLIST SCORECARD (all 17, exactly one status each)

| # | Status | Basis (one line) |
|---|---|---|
| F1 ZERO-VALUE STANDING ITEMS | N.A. | Deck P&L snapshot carries only 5 populated line items per table (slides 26/27); zero `ZERO_STANDING` rows (A2 confirms 0); full line-item set where zero rows appear is not present in a deck. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | Deck carries both statements; S-vs-C PAT gap moved ~24 pp of standalone PAT YoY (30.9%→6.8%), > 5 pp threshold. FND-01. |
| F3 SHELL-ENTITY DETECTION | N.A. | Deck P&L shows no cost lines (no Cost of Materials / Employee Benefits / Depreciation) to compare standalone vs consolidated. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor report / Other Matters paragraph in a deck. |
| F5 GOING CONCERN / EoM SCOPE | N.A. | No auditor EoM in a deck; no prior-quarter ledger for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | Multiple dated commitments: "under construction" (Gurgaon/Nagpur, l.174), "Launching Soon" (l.584), "expected to drive higher revenues" (l.598), "planned rollout for FY27" (l.708). FND-02; see Commitment Register. |
| F7 HEDGE PHRASE MINING | PASS | Only generic Safe Harbour boilerplate (slide 3, "cannot assure investors ... will prove to be correct"); no substantive newly-added hedge on revenue lumpiness / customer concentration. |
| F8 TAX FORENSICS | N.A. | Deck discloses no PBT and no current/deferred tax line; ETR not computable. |
| F9 OCI FORENSICS | N.A. | No OCI / actuarial disclosure in a deck. |
| F10 SHARE COUNT & DILUTION | PASS | Single share count 7,27,86,884 (l.759) reconciles to market cap (112.95 × shares = Rs 822.13 Cr, l.761/764); no EPS or dilutive-instrument disclosure, no period change, nothing anomalous. |
| F11 RESERVES / NET WORTH TIE-OUT | N.A. | No balance sheet / other equity in a deck (market-cap arithmetic ties internally, noted under F10). |
| F12 SEGMENT FORENSICS | N.A. | Only a revenue-mix pie (IVF 66.24% / Hospital 29.41% / Pharmacy 4.35%, slide 6); no segment assets/liabilities. |
| F13 BOARD OUTCOME / TERM DATES | FINDING | 6 directors incl. 3 independent, all missing DIN and term dates (l.622-642); term expiry cannot be mapped to catalyst window. FND-03. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | "Additional Slide Proposed" leftover template text (l.749) + multiple typos; cumulative QC/governance data point. FND-04. |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list disclosed anywhere in the deck and no prior ledger; note: consolidated statement is presented but no subsidiary/associate is ever named (flag for A4). |
| F16 DROPPED / REFRAMED DISCLOSURES | FINDING | Non-GAAP "Adjusted EBITDA" add-back (FND-05) + unlabeled consolidated snapshot + uncalled FD-interest flattering (FND-06). Dropped-metric diff not possible (`NO_PRIOR_LEDGER`). |
| F17 CONCALL SILENCE AUDIT | N.A. | Not a concall; no Notion monitoring checklist injected this run. |

Blank checks: none. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | ref | status word |
|---|---|---|---|
| Delhi South Extension Hub pre-operationalisation | FY27 | slide 26, line 705 | underway |
| Gurgaon hub construction | FY27 | slide 7, line 174 / slide 22, line 584 | underway (under construction) |
| Nagpur hub construction | FY27 | slide 7, line 174 / slide 22, line 584 | underway (under construction) |
| 1 hub in Delhi/NCR "launching soon" | FY27 | slide 22, line 584 | initiated |
| 2 of 10 hubs to launch | FY27 | slide 22, line 584 | initiated |
| 8 new centers | FY28 | slide 22, line 590 | planned |
| 1 new center | FY29 | slide 22, line 593 | planned |

FORWARD-SIGNAL findings (flag to A4): FND-02, FND-05 (forward implication).
AMBIGUOUS findings (convert to management questions, A4): FND-01, FND-03, FND-05, FND-06.

---

```yaml
stage: A3-forensics
company: "GAUDIUMIVF"
quarter: "q1fy27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/gaudiumivf-q1fy27/work/forensics_presentation_gaudiumivf_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: N.A.
  F2: FINDING
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: N.A.
  F9: N.A.
  F10: PASS
  F11: N.A.
  F12: N.A.
  F13: FINDING
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "FND-01", check: "F2", line: "699,726", classification: "AMBIGUOUS", implication: "Subsidiary PAT contribution collapsed 30.9%->6.8% of standalone PAT YoY; consolidated is margin-dilutive; future consolidated drag"}
  - {id: "FND-02", check: "F6", line: "584,598,601,174", classification: "FORWARD-SIGNAL", implication: "Dated FY27-FY29 hub-expansion commitments for promise-vs-delivery tracker"}
  - {id: "FND-03", check: "F13", line: "622-642", classification: "AMBIGUOUS", implication: "Independent-director term dates absent; cannot map governance against commissioning window"}
  - {id: "FND-04", check: "F14", line: "749", classification: "NEUTRAL-FACT", implication: "'Additional Slide Proposed' leftover template text plus typos; document QC/governance lapse"}
  - {id: "FND-05", check: "F16", line: "710,737", classification: "AMBIGUOUS", implication: "Undisclosed identical Rs 290.35L add-back at both bases inflates 15.89% margin to 37.12%; over-scopes the ~223L S&M rise; not traceable to filing"}
  - {id: "FND-06", check: "F16", line: "653-685,699", classification: "AMBIGUOUS", implication: "Headline snapshot silently uses consolidated basis; 'Continuing Operations' label with no discontinued-ops disclosure; ~102L FD interest inside PAT not called out"}
forward_signals: ["FND-02", "FND-05"]
ambiguous: ["FND-01", "FND-03", "FND-05", "FND-06"]
commitments:
  - {commitment: "Delhi South Extension Hub pre-operationalisation", implied_date: "FY27", ref: "slide26/L705", status_word: "underway"}
  - {commitment: "Gurgaon hub construction", implied_date: "FY27", ref: "slide7/L174,slide22/L584", status_word: "underway"}
  - {commitment: "Nagpur hub construction", implied_date: "FY27", ref: "slide7/L174,slide22/L584", status_word: "underway"}
  - {commitment: "1 hub Delhi/NCR launching soon", implied_date: "FY27", ref: "slide22/L584", status_word: "initiated"}
  - {commitment: "2 of 10 hubs to launch", implied_date: "FY27", ref: "slide22/L584", status_word: "initiated"}
  - {commitment: "8 new centers", implied_date: "FY28", ref: "slide22/L590", status_word: "planned"}
  - {commitment: "1 new center", implied_date: "FY29", ref: "slide22/L593", status_word: "planned"}
gate_a3: pass
blank_checks: []
```
