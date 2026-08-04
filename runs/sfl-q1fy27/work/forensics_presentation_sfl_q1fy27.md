# A3 FORENSIC NOTES — Sheela Foam Ltd (SFL) — Q1 FY27 — DOCTYPE: PRESENTATION

Source extract: `runs/sfl-q1fy27/work/extract_presentation_sfl_q1fy27.txt` (51 slides, 100% coverage, 27 OCR pages)
Ledger reconciled: 218 ledger rows / all read verbatim at cited lines = 100%.
Doctype scope applied: F16 active; F1/F2/F6/F8/F9/F10/F14/F15 active because the deck carries income statements (slides 49-50), the S-vs-C performance table (slide 11) and per-geography P&Ls (slides 17-19). Balance-sheet-only and auditor-only checks marked N.A. with a one-line reason each. F17 N.A. (no transcript).

Cross-check anchors used (from audited-structure results filing, supplied in task):
- Standalone core EBITDA ex-other-income ~8.99% (below 10% falsification line); consolidated ~10.55%.
- Standalone depreciation fell ~42% YoY with no explanatory note.
- Furlenco Global Pte Ltd deconsolidated 01.04.2026; a JV stake diluted 43.89%->34.53% via non-participation.
Notion monitoring checklist items tracked for touch/silence: core EBITDA ex-OI >12% (falsification <10%); Kurlon synergy Rs 40-60 Cr step-up Q1 FY27; net debt toward FY28 net cash; receivables growth <= revenue with CFO/PAT >1.0x; second consecutive dividend FY27.

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|-----------|----------------|----------------|---------------------|
| A3-01 | F1 | p49 Exceptional Item / p50 Exceptional Item | L1059 (consol) & L1079 (standalone), slides 49-50 | "Exceptional Item  -6 ... -16" | FORWARD-SIGNAL | Shown with a minus sign but arithmetically ADDS to PAT (standalone 52 PBT +6 −15 tax ≈ 44 PAT; consol 73 −20 +3 +6 = 62). It is an exceptional GAIN of ~Rs 6 Cr (Q1FY27) / ~Rs 16 Cr (Q4FY26), identical in standalone and consol, nature undisclosed. Reported PAT is flattered by an undisclosed one-off; ties to the filing's Furlenco deconsolidation (01.04.2026) / JV dilution 43.89%->34.53%. Ask management to name the item and its recurrence. |
| A3-02 | F2 | p49 PAT / p50 PAT | L1062 & L1081, slides 49-50 | "PAT  62 ... 7" / "PAT  44 ... 11" | FORWARD-SIGNAL | S-vs-C PAT gap swung from −4 (Q1FY26 consol 7 BELOW standalone 11 = −36% of standalone PAT) to +18 (Q1FY27 = +41%), a ~77 pp swing, far above the 5 pp threshold. Consolidated earnings have flipped to being materially levered to Joyce/Interplasp/JV; international is now the growth engine, not the domestic base. |
| A3-03 | F6 | p12 geographic footprint | L243, slide 12 | "COCO - 42 stores operational; ramp-up to 50 over next quarter" | FORWARD-SIGNAL | Dated commitment: COCO store count 42->50 by Q2 FY27. Milestone to track in Role 5 promise-vs-delivery. |
| A3-04 | F9 | p49 Other Comprehensive Income | L1064, slide 49 | "Other Comprehensive Income  -6  23  18" | AMBIGUOUS | Consol OCI swung +23 (Q1FY26) -> −6 (Q1FY27), a −29 Cr move, while standalone OCI is stable (−3 vs −1, L1083). Swing sits in the FX-translation reserve of the international subs, corroborated by the "*before Forex MTM" footnote. Generate a question on FX exposure/hedging on Joyce+Interplasp. |
| A3-05 | F14 | p49/p50 Exceptional Item; entity names | L1059/L1079; L189 vs L155/L320; L205/L218 | "Exceptional Item ... -6" ; "Joyce (Australia)" vs "Interplasp (Spain)" vs "interplasp" ; "Standalone (SFL + KEL)" | AMBIGUOUS | Sign convention on the exceptional item is misleading (negative sign, positive P&L effect). Entity-name casing is inconsistent across tables. "Standalone (SFL + KEL)" labels a combined entity as standalone — confirm the filing's standalone basis matches before trusting the 9.0% margin. Individually immaterial, cumulatively a governance data point. |
| A3-06 | F15 | p7 group brands; p49 JV share | L156-157; L1061, slides 7 & 49 | "FURLENCO" (group companies slide) ; "Share in profit/(loss) of Joint venture  3  2  14" | FORWARD-SIGNAL | Deck still lists Furlenco under "Furniture rental business" despite the filing's deconsolidation on 01.04.2026 (the first day of this very quarter); the JV share line is populated, reflecting the diluted 34.53% stake. A material group-structure change is not narrated anywhere in the deck. Verify continuing-obligation / re-consolidation risk. |
| A3-07 | F16 | p10 footnote | L211, slide 10 (footnote #1, ledger Table C) | "*before Forex MTM" | AMBIGUOUS | Headline EBITDA-growth figures (45% consol, 13% standalone) carry a bespoke "before Forex MTM" adjustment whose scope is ambiguous (standalone/consol/both per A2). Any adjusted-EBITDA basis flatters vs the filing's core figure; ask which line(s) it qualifies and the Rs quantum removed. |
| A3-08 | F16 | p11 Gross Margin | L224, slide 11 | "GROSS MARGIN  44.4%  37.6%  -688 bps ... 44.6%  40.6%  -405 bps" | FORWARD-SIGNAL | Standalone gross margin fell 688 bps YoY (44.4%->37.6%), consol 405 bps, disclosed only in the detail table; the milestone slides 8 and 10 omit it entirely and lead with EBITDA growth. Input-cost/mix margin pressure is the buried story. |
| A3-09 | F16 | p11 EBITDA %; p8 milestone | L227/L1074 vs L172-173, slides 11/50 & 8 | "EBITDA %  9.5%  9.0%" ; "1ST TIME EVER ... Rs 100 Cr + EBITDA" | FORWARD-SIGNAL | Deck headlines the consol "Rs 100 Cr+ / 10.6%" milestone while standalone core EBITDA is 9.0% (68/761=8.94%), below the 10% Notion falsification line and matching the filing's 8.99% core. The falsification-relevant standalone number is not surfaced in any headline. |
| A3-10 | F16 | p50 Depreciation | L1076, slide 50 | "Depreciation  17  30  17" | FORWARD-SIGNAL | Standalone depreciation fell ~43% YoY (30->17) with no explanatory note, matching the filing's ~42% flag. A depreciation collapse flatters PBT/PAT and the EBITDA-to-PBT bridge; ask for the driver (asset-life change? impairment? Kurlon PPA re-basing?). |
| A3-11 | F16 | checklist silence (no ledger row — absence) | slides 10/11/37 (Kurlon touched); no BS slide | (absence — Kurlon synergy Rs quantum, net debt, dividend, receivables/CFO all not stated) | CONFIRMATORY-NEGATIVE | The deck touches Kurlon (labels standalone "SFL+KEL", new-models slide 37) but never quantifies the Rs 40-60 Cr synergy step-up the monitoring checklist expects; it carries no net-debt slide, no dividend line, and no receivables/CFO/PAT disclosure. Four first-class monitored items are silent in a deck that had room for them. |
| A3-12 | F16 | A2 POSSIBLE_NEW_OR_REFRAMED (p8, p19, p38, p41) | L164/L330/L713/L847, slides 8/19/38/41 | "1ST TIME EVER" ; "STAQO : Q1 FY27" ; "Kurlon | Venti Launch" ; "AI led ads" | NEUTRAL-FACT | Four slides read as newly added or reframed (milestone framing, STAQO break-out, Venti product, AI-led ads). Cannot be confirmed as reframes/dropped-metric candidates without the prior-quarter deck (no PRIOR_LEDGER_PATH supplied); flagged for a downstream diff. |

---

## CHECKLIST SCORECARD (all 17, one status each)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING | FINDING | Exceptional Item line (L1059/L1079) carries an undisclosed one-off shown as "-6" that arithmetically adds to PAT = a hidden gain (A3-01). Other ZERO_STANDING rows (p13 blank Volume, p30 empty template, EPS YoY/QoQ dashes) are benign template artefacts. |
| F2 STANDALONE vs CONSOLIDATED | FINDING | S-vs-C PAT gap swung ~77 pp of standalone PAT (A3-02); international flipped from drag to driver. |
| F3 SHELL-ENTITY DETECTION | N.A. | Deck gives no entity-level cost lines (COGS/employee/depreciation per subsidiary); international subs (Joyce/Interplasp/Staqo) are visibly operating with growing revenue, not shells. |
| F4 UNAUDITED CONTRIBUTION | N.A. | Presentation carries no auditor letter / Other Matters paragraph. |
| F5 GOING CONCERN / EoM | N.A. | No auditor EoM in a deck; no prior-quarter deck for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "ramp-up to 50 over next quarter" (A3-03) plus "commenced" milestones (solar Jabalpur, STP Nandigram) — see commitment register. |
| F7 HEDGE PHRASE MINING | PASS | Only hedge language is the standard safe-harbour boilerplate (p3: "there can be no assurance", "No assurance can be given"); no newly added operational hedge on lumpiness/concentration. |
| F8 TAX FORENSICS | PASS | ETR 27-29% (consol 20/73=27.4%; standalone 15/52=28.8%) marginally above statutory 25.17%, explainable by non-deductible exceptional; deck gives no deferred-tax or earlier-year-adjustment line to test further. |
| F9 OCI FORENSICS | FINDING | Consol OCI swung +23 -> −6 YoY, FX-translation driven; standalone (actuarial) OCI stable (A3-04). |
| F10 SHARE COUNT / DILUTION | PASS | Single "Basic/Diluted EPS" line, no spread = no dilutive instruments; implied share count consistent (consol 62/5.6 ≈ 11.1 Cr; standalone 44/4.0 = 11.0 Cr). No corporate-action gap vs filing. |
| F11 RESERVES / NET WORTH | N.A. | Deck carries no balance sheet, reserves, or net-worth figure to tie out (income statement only). |
| F12 SEGMENT FORENSICS | N.A. | Deck discloses segment revenue/volume/value only (slide 13) and geography P&Ls; no segment assets or liabilities. |
| F13 BOARD OUTCOME | N.A. | Presentation carries no board-meeting outcome, AGM notice, record date, or director appointment. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | Exceptional-item sign convention misleading + entity-name casing + "Standalone (SFL+KEL)" combined-basis label (A3-05). |
| F15 ENTITY LIST DIFFS | FINDING | Furlenco still shown as a group company despite filing deconsolidation 01.04.2026; JV share line reflects diluted 34.53% stake (A3-06). |
| F16 PRESENTATION-SPECIFIC | FINDING | "before Forex MTM" basis, buried gross-margin collapse, sub-10% standalone core, −43% depreciation no-note, Kurlon-synergy/net-debt/dividend silence, four reframed slides (A3-07 to A3-12). |
| F17 CONCALL SILENCE AUDIT | N.A. | No concall transcript in scope; checklist-silence items folded into F16 (A3-11). |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/slide ref | status word |
|-----------|--------------|----------------|-------------|
| COCO stores 42 -> 50 | Q2 FY27 ("next quarter") | slide 12, L243 | ramp-up (underway) |
| 500 kWp solar capacity, Jabalpur, usage to rise from 35%+ | ongoing FY27 | slide 23, L406-408 | commenced |
| New STP (sewage treatment), Nandigram | Q1 FY27 | slide 23, L406-408 | commenced |
| Sustainability 2030 targets (Gender Diversity 10%, Disability employment 11, ISO 45001) | FY30 | slide 22, L381-391 | target (underway) |

---

## LEDGER RECONCILIATION
All 218 numbers-ledger rows and all 3 footnote rows were read at their cited lines in the A1 extract before judging. A2-raised flags addressed: ZERO_STANDING (F1 — exceptional item elevated to finding, rest benign), OCR_LOW_CONFIDENCE (marketing/infographic slides p6/p38/p43-47 carry no financial metric that bears on any finding; all excluded numbers are marketing creative, not reconcilable P&L data), OCR_NOISE_NO_DATA (p31-34/39-40 photo collages — no data, no forensic weight), POSSIBLE_NEW_OR_REFRAMED (F16/A3-12). ledger_reconciled_pct = 100.
