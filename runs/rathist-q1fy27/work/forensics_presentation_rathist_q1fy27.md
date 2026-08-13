# A3 FORENSIC NOTES — Rathi Steel and Power Limited (RATHIST) — Q1 FY27 — DOCTYPE: PRESENTATION (Reg 30 press release)

Source extract: `runs/rathist-q1fy27/work/extract_presentation_rathist_q1fy27.txt` (179 lines, 4 pages)
Ledger: `runs/rathist-q1fy27/work/ledger_presentation_rathist_q1fy27.txt` (Tables A-K)
Ledger reconciliation: 100% — every A2 row (Tables A-K, all 63 line_items + summary counts) read verbatim at its cited line.
Prior thesis / Notion checklist / companies/RATHIST.md: NONE supplied. Fresh, no-prior-thesis review.
Prior-quarter document: NOT PROVIDED (A2 flag NO_PRIOR_LEDGER). All diff-dependent checks marked N.A. accordingly.

Doctype note: this is a company-issued STANDALONE press release (line 33: "Unaudited Standalone Financial Results").
It carries NO consolidated accounts, NO balance sheet, NO segment tables, NO auditor letter/EoM, NO board-outcome
resolutions, NO transcript. Per the prompt's doctype-applicability rule, those checks are N.A.; forensic value is in
F1, F6, F7, F10, F14 and F16.

---

## FINDINGS TABLE

| id | check | ledger row | line/slide | verbatim quote | classification | forward implication |
|----|-------|-----------|-----------|----------------|----------------|---------------------|
| F1-EXC | F1 | Table B r3 (ZERO_STANDING); Table C n1/n2 | L90, L95-96 | "EBITDA Margin (%) 4.01% 4.01% -"; "excludes extraordinary and exceptional items" | NEUTRAL-FACT | The footnote carve-out names an exceptional/extraordinary-items line that is nil this quarter; it exists in the template and can be switched on. Watch for a one-off appearing below EBITDA in a future quarter. The "-" YoY cell = margin genuinely FLAT, not a dropped datum. |
| F6-FWD | F6 | Table F F7,F8; Slide 9 | L124, L143-146 | "our focus remains firmly on scaling volumes, deepening market penetration, optimising our product mix and maintaining cost discipline"; "pursuing sustainable and profitable growth" | FORWARD-SIGNAL | Undated, unquantified FY27 commitments. No capacity, capex, timeline or target attached. Feeds A4 as management questions (quantify "scaling volumes" target; define "cost discipline" in bps). |
| F7-RM | F7 | Table F F5 | L140-141 | "Recent moderation in certain raw-material prices provides a relatively more constructive cost backdrop" | FORWARD-SIGNAL | Pre-emptive framing of a cost tailwind INTO next quarter. If input costs eased, flat 4.01% margin despite that tailwind implies realisation pressure is offsetting it (see F16-MIX). A4: did Q1 already capture the moderation, or is it a Q2 tailwind? |
| F7-HDG | F7 | Table F F3,F6 | L137-139, L141 | "softer steel realisations and continued volatility in energy and input costs"; "geopolitical and energy-market volatility remain key variables" | AMBIGUOUS | Management itself concedes "softer steel realisations" — corroborates the derived realisation decline. Legal hedge on volatility is pre-emptive cover. Direction uncertain; lean bear → A4 question on realisation trajectory and energy-cost pass-through. |
| F10-DIL | F10 | Table B r5,r6 | L91, L93 | "PAT 3.48 ... 84.56%"; "Diluted EPS (₹) 0.40 0.22 81.82%" | AMBIGUOUS | Diluted EPS grew 81.82% while PAT grew 84.56%. The per-share lag implies diluted share count rose ~1.5% YoY (implied ~8.59→8.70 Cr shares). No basic EPS, no share count, no paid-up capital disclosed to confirm. Possible dilutive instrument / issuance. A4: reconcile against paid-up capital in the statutory filing; identify any ESOP/warrant/conversion. (EPS coarsely rounded to ₹0.01, so treat as a flag, not proof.) |
| F14-TYPO | F14 | Table C n1; Slide 3 headline | L95, L77 vs L88, L89 | footnote "* EBIDTA includes other income" vs table "EBITDA"; headline "Revenue Grows 25% YoY" vs table "24.63%" | NEUTRAL-FACT | Drafting inconsistencies: "EBIDTA" typo, and headline rounds 24.63% up to "25%" / 84.56% up to "85%". Individually immaterial; cumulatively a low-rigour-disclosure data point on a promotional release. No restatement — rounding is directionally consistent. |
| F16-MARGIN | F16 | Table B r3; Slide 3 headline | L76, L90 | "Reports Strong Q1 FY27 Performance"; "EBITDA Margin (%) 4.01% 4.01% -" | FORWARD-SIGNAL | The honest tell buried under the "Strong Performance / +85% PAT" headline: EBITDA margin is FLAT YoY (4.01% both years). There was NO margin expansion. The growth story is entirely volume/operating-leverage, not profitability improvement. A4: probe why scale did not lift EBITDA margin. |
| F16-MIX | F16 | Table D h3; Table E E1-E7; Slide 6 | L102, L103, L107, L108 | "Higher TMT volumes strengthened the overall product mix"; volume "~30% YoY to 28,372 MT" vs revenue "over 24% YoY"; "TMT rebar ... more than doubled to 18,677 MT ... from 8,295 MT" | FORWARD-SIGNAL | CORE FINDING. Volume +29.76% but Total Income +24.63% ⇒ blended realisation FELL ~4% (₹71,076→₹68,260/MT). TMT rebar (lower-value MS) +125% and rose from 37.9% to 65.8% of volume; higher-value non-TMT/stainless volume FELL from 13,569→9,695 MT (-28.5% absolute). The deck calls this "strengthened the overall product mix" — it is a mix-DOWN. This asymmetry explains falling realisation and flat margin, and is the single most important forward-signal. A4: is the stainless volume decline structural (capacity re-allocated to TMT) and does it compress future margin mix? |
| F16-ASYM | F16 (cross-doc) | Table B r2,r4; Table C n1 | L89, L91, L95 | "EBITDA 7.77 6.23 24.83%"; "PAT 3.48 1.89 84.56%"; "EBIDTA includes other income" | FORWARD-SIGNAL | Cross-document arithmetic (statutory filing figures supplied to A3): filing PBT 347.99 + Finance cost 208.70 + Depreciation 220.70 = 777.39 Lakhs = ₹7.77 Cr = press-release EBITDA — the bridge RECONCILES, and confirms EBITDA INCLUDES other income (per footnote). PAT rose 84.56% vs EBITDA only 24.83% because the fixed charges BELOW EBITDA (depreciation down YoY, interest, and near-nil tax: filing PBT 347.99 ≈ PAT 347.99) shrank as a share. PAT growth is NOT operating-quality driven. FORWARD-SIGNAL: minimal current tax → future ETR step-up toward 25.17% and any depreciation normalisation are earnings headwinds. A4/A5: verify tax line and depreciation trend in the filing. |
| F16-PROMO | F16 | Table A slide 3/11; Table G G1,G3,G8 | L80, L154, L160-162 | "one of the leading players"; "renowned Rathi legacy"; "India's only stainless-steel wire rod manufacturer using direct billet charging technology" | NEUTRAL-FACT | Promotional superlatives not independently verifiable from this document. "India's only ... direct billet charging" is an exclusivity claim with no source cited. Flag as promotional/unverifiable-from-this-doc; do not carry into the thesis as fact. |

---

## CHECKLIST SCORECARD (all 17 — exactly one status each)

| # | Check | Status | Basis |
|---|-------|--------|-------|
| F1 | Zero-value standing line items | FINDING | ZERO_STANDING row = EBITDA Margin "-" (L90, flat not dropped); footnote L95-96 names an exceptional/extraordinary carve-out that is nil this quarter (F1-EXC). |
| F2 | Standalone vs consolidated decomposition | N.A. | Standalone-only press release (L33). No consolidated figures to decompose. |
| F3 | Shell-entity detection | N.A. | No entity-level cost lines; standalone only. No consolidation to compare. |
| F4 | Unaudited contribution ratio | N.A. | No auditor "Other Matters" / component-auditor disclosure in a press release. |
| F5 | Going concern / EoM scope | N.A. | No auditor report or EoM in doc; no prior-quarter doc to verbatim-diff. |
| F6 | Forward-commitment phrase mining | FINDING | Multiple undated FY27 commitments in the Rathi comment and Slide 9 (F6-FWD). See Commitment Register. |
| F7 | Hedge phrase mining | FINDING | Raw-material-moderation cost-backdrop hedge (F7-RM) + "softer realisations" / "key variables" legal hedges (F7-HDG). |
| F8 | Tax forensics | N.A. | No tax line/ETR disclosed in the press release. (Near-nil tax observed in the statutory filing is carried under F16-ASYM as a cross-doc signal for A4/A5.) |
| F9 | OCI forensics | N.A. | No OCI / actuarial disclosure in a press release. |
| F10 | Share count and dilution | FINDING | Diluted EPS +81.82% lags PAT +84.56% ⇒ implied ~1.5% share-count rise; no basic EPS / share count disclosed (F10-DIL). |
| F11 | Reserves and net worth tie-out | N.A. | No balance sheet / equity figures in doc. |
| F12 | Segment forensics | N.A. | No segment asset/liability tables. (Product-line volume mix handled under F16-MIX.) |
| F13 | Board outcome beyond results | N.A. | Reg 30 media-release covering letter only; no board resolutions, AR/AGM notice, dividend, or director-term disclosure. |
| F14 | Note drafting inconsistencies | FINDING | "EBIDTA" typo (L95) and headline rounding 24.63%→"25%" / 84.56%→"85%" (L77 vs L88/L91) (F14-TYPO). |
| F15 | Entity list diffs | N.A. | No consolidation list; no prior-quarter doc. |
| F16 | Presentation-specific reframing | FINDING | Flat EBITDA margin under "Strong" headline (F16-MARGIN); mix-DOWN sold as "strengthened mix" (F16-MIX); PAT/EBITDA asymmetry + EBITDA bridge (F16-ASYM); unverified superlatives (F16-PROMO). Dropped-disclosure sub-test N.A. (no prior deck). |
| F17 | Concall silence audit | N.A. | Not a concall; no transcript and no Notion monitoring checklist supplied. |

Blank checks: NONE. GATE A3: PASS.

---

## COMMITMENT REGISTER (from F6 / forward language)

| commitment | implied date | ref | status word |
|------------|-------------|-----|-------------|
| "scaling volumes, deepening market penetration, optimising our product mix and maintaining cost discipline" | FY27 (undated within year) | L143-144 (Table F F7) | ongoing/underway |
| "remains focused on leveraging its diversified capabilities to capture emerging market opportunities" | undated | L124 (Slide 9) | ongoing |
| "pursuing sustainable and profitable growth" | undated | L145-146 (Table F F8) | ongoing |
| "Recent moderation in certain raw-material prices provides a relatively more constructive cost backdrop" (outlook, not a committed action) | forward (into Q2 FY27) | L140-141 (Table F F5) | outlook/hedge |

All commitments are soft, undated and unquantified — none is a milestone-dated deliverable. Each is a candidate A4 management question (quantify the target, attach a date/metric). No prior-quarter deck exists, so no initiated→underway→completed status-transition can be tracked this run.

---

## CLASSIFICATION SUMMARY (for A4 hand-off)
- FORWARD-SIGNAL (probe): F6-FWD, F7-RM, F16-MARGIN, F16-MIX (core), F16-ASYM.
- AMBIGUOUS (convert to management question): F7-HDG, F10-DIL.
- NEUTRAL-FACT: F1-EXC, F14-TYPO, F16-PROMO.
- CONFIRMATORY-NEGATIVE: none standalone (F7-HDG carries the confirmatory element that management concedes "softer steel realisations").

Priority for A4 management questions:
1. F16-MIX — stainless/high-value volume down ~28.5% absolute while TMT doubled; is the mix-down structural, and what is the margin path?
2. F16-ASYM — PAT surge is below-EBITDA (depreciation + near-nil tax); what normalised, tax-adjusted PAT growth remains?
3. F16-MARGIN — why did ~30% volume growth deliver zero EBITDA-margin expansion?
4. F10-DIL — reconcile implied ~1.5% share-count increase.
5. F7-HDG / F7-RM — realisation trajectory and raw-material pass-through into Q2.

```yaml
stage: A3-forensics
company: "RATHIST"
quarter: "Q1FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/rathist-q1fy27/work/forensics_presentation_rathist_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: N.A.
  F9: N.A.
  F10: FINDING
  F11: N.A.
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "F1-EXC", check: "F1", line: "L90,L95-96", classification: "NEUTRAL-FACT", implication: "Exceptional/extraordinary-items carve-out is nil now but template-live; EBITDA margin flat not dropped"}
  - {id: "F6-FWD", check: "F6", line: "L124,L143-146", classification: "FORWARD-SIGNAL", implication: "Undated unquantified FY27 volume/cost commitments; A4 to quantify"}
  - {id: "F7-RM", check: "F7", line: "L140-141", classification: "FORWARD-SIGNAL", implication: "Raw-material moderation framed as Q2 cost tailwind; flat margin despite it implies realisation offset"}
  - {id: "F7-HDG", check: "F7", line: "L137-139,L141", classification: "AMBIGUOUS", implication: "Management concedes softer realisations; volatility legal hedge; A4 question on realisation path"}
  - {id: "F10-DIL", check: "F10", line: "L91,L93", classification: "AMBIGUOUS", implication: "Diluted EPS +81.82% lags PAT +84.56%; implied ~1.5% share-count rise; no basic EPS/share count disclosed"}
  - {id: "F14-TYPO", check: "F14", line: "L95,L77", classification: "NEUTRAL-FACT", implication: "EBIDTA typo + headline rounding 24.63%/84.56% up to 25%/85%; low-rigour disclosure, no restatement"}
  - {id: "F16-MARGIN", check: "F16", line: "L76,L90", classification: "FORWARD-SIGNAL", implication: "EBITDA margin FLAT 4.01% under 'Strong Performance/+85% PAT' headline; no margin expansion"}
  - {id: "F16-MIX", check: "F16", line: "L102,L103,L107,L108", classification: "FORWARD-SIGNAL", implication: "CORE: volume +30% vs revenue +24.6% => realisation -4%; TMT doubled to 65.8% of mix, stainless volume -28.5%; 'strengthened mix' is a mix-DOWN"}
  - {id: "F16-ASYM", check: "F16", line: "L89,L91,L95", classification: "FORWARD-SIGNAL", implication: "EBITDA bridge to filing reconciles (PBT347.99+Fin208.70+Dep220.70=777.39=7.77Cr, incl other income); PAT+84.56%>>EBITDA+24.83% driven by lower depreciation + near-nil tax => future ETR step-up risk"}
  - {id: "F16-PROMO", check: "F16", line: "L80,L154,L160-162", classification: "NEUTRAL-FACT", implication: "Unverifiable superlatives ('leading player','only ... direct billet charging'); do not carry as fact"}
forward_signals: ["F6-FWD", "F7-RM", "F16-MARGIN", "F16-MIX", "F16-ASYM"]
ambiguous: ["F7-HDG", "F10-DIL"]
commitments:
  - {commitment: "scaling volumes, deepening market penetration, optimising product mix, maintaining cost discipline", implied_date: "FY27", ref: "L143-144", status_word: "underway"}
  - {commitment: "leveraging diversified capabilities to capture emerging market opportunities", implied_date: "undated", ref: "L124", status_word: "ongoing"}
  - {commitment: "pursuing sustainable and profitable growth", implied_date: "undated", ref: "L145-146", status_word: "ongoing"}
  - {commitment: "raw-material price moderation provides a more constructive cost backdrop", implied_date: "Q2FY27-outlook", ref: "L140-141", status_word: "outlook"}
gate_a3: pass
blank_checks: []
```
