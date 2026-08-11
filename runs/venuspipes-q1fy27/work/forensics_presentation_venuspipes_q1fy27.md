# A3 FORENSIC NOTES — Venus Pipes & Tubes (VENUSPIPES) — Q1 FY27 — Doctype: PRESENTATION

Model: claude-opus-4-8. Inputs: extract_presentation_venuspipes_q1fy27.txt (37 pages,
1203 lines), ledger_presentation_venuspipes_q1fy27.md (629 numbers, 17 footnotes,
8 ZERO_STANDING, 9 admin identifiers). Prior-quarter deck: **none available**
(DROPPED_SLIDE / chart-baseline diffs not computable — stated under F16).
Ledger reconciled: **100%** — every one of the 200 NUMBERS line-groups, all 17
footnotes, all 8 ZERO_STANDING rows and the SLIDES/ADMIN tables were read verbatim at
their cited extract line before judging.

Doctype scope: this is an investor deck. F16 applies in full; F6/F7/F10/F11 apply to the
numbers/commitments the deck carries; F1/F8/F14 apply to the standing lines, tax and
drafting; F2/F3/F4/F5/F15 are N.A. (Venus is a standalone-only company — no subsidiary,
JV, associate, auditor Other-Matters or consolidation list appears anywhere in the deck);
F9/F12/F13 N.A. (no OCI, no segment balance-sheet, no board-resolution/AGM/term-date
content); F17 N.A. (not a concall — but the Notion monitoring-checklist silence
cross-reference was performed and is carried under F16 so the silence layer is not a gap).

NOTE ON BASELINES: only the presentation was supplied this run. The results-filing and
concall baselines the task asks to cross-check against are not in this run's inputs, so
all headline cross-checks below are internal-to-deck reconciliations. All deck arithmetic
ties (see F-notes). A4/A5 should still reconcile 320.5 / 51.5 / 26.4 / order-book / capex
/ debt against the filed results and the concall.

---

## 1. FINDINGS TABLE

| id | check | ledger row / ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|------------------|-----------|----------------|----------------|---------------------|
| A3-F1-01 | F1 | p14 L468 / p31 L984 / p32 L1005,1017 | slide 14 L468; slide 31 L984; slide 32 L1005/1017 | "Exceptional Items 0.0 0.0 -0.2" (L468); "Exceptional item 0.5 0.0 0.0 0.0 0.0" (L984); "Right-of-Use Assets 1.7 0.0 0.0 0.0 0.0" (L1005) | AMBIGUOUS | Exceptional-item template line turned non-zero (FY26 +0.5, Q4FY26 -0.2) with no explanation; first-ever ROU asset (1.7) + lease liabilities (1.5 NC, 0.1 curr) appear Mar-26 — new leasing/Ind AS 116 activity. Ask what the exceptional item was and what was leased. |
| A3-F6-01 | F6 | Key Highlights bullet | slide 8 L232 | "Forward integration into Pipe spooling remains on track for commencement by end of year" | FORWARD-SIGNAL | Dated management commitment: spooling commences by end of year (CY2026 / FY27). Feeds promise-vs-delivery tracker. "remains on track" implies a prior on-track statement — verify status transition once a prior deck exists. |
| A3-F6-02 | F6 | Capex/LOI, MD's Desk | slide 5 L118/L135; slide 15 L499 | "LOI received for INR 185 Cr Order" / "~INR 70 Crores Capex" / "capex execution on track" | FORWARD-SIGNAL | 185 Cr anchor LOI (Data Centre SS spool) + ~70 Cr spooling capex are dated funding/execution commitments; LOI is not a firm order (see F16-05). Track conversion of LOI to PO and the 70 Cr outflow against cash flow. |
| A3-F6-03 | F6 | Sustainability | slide 36 L1176 | "Installation in progress for additional 6.1 MW in-house solar power unit ... Currently 1.3 MW already installed" | NEUTRAL-FACT | ESG capex commitment underway; +6.1 MW on top of 1.3 MW. Minor cash/energy-cost lever. |
| A3-F7-01 | F7 | MD's Desk | slide 15 L504-506 | "the geopolitical situation remains an area of watch ... freight rates continue to remain a factor that we are monitoring closely. While these external factors may create near-term uncertainty" | FORWARD-SIGNAL | Newly stated export hedge sits directly above a -9% YoY export decline (F16-03). Pre-emptive management framing telegraphs continued export softness into Q2 FY27. |
| A3-F10-01 | F10 | Share Capital row | slide 32 L1002; slide 34 L1108 | "Share Capital 20.7 20.4 20.3 20.3 15.2" (L1002); "Rs. 35.06 crores raised via Share Warrant for FY 2024-25" (L1108) | AMBIGUOUS | Paid-up capital crept 20.4 (Mar-25) -> 20.7 (Mar-26), tracing to warrant conversion; the 35.06 Cr warrant programme implies a possible residual un-converted tranche = future dilution. Deck gives no share count or basic/diluted EPS. Ask if warrants are fully converted. |
| A3-F11-01 | F11 | Return ratios + footnotes | slide 34 L1092-1096; FN#15 L1108; FN#17 L1110 | "ROCE^ 34.7% 31.0% 32.0% 30.7% 27.0%" with "^Excluding CWIP from Total Capital Employed from FY23 to FY26"; "RoE* ... *Excluding Rs.107.9 crores ... IPO ... and Rs.35.06 crores ... Share Warrant" | FORWARD-SIGNAL | Net worth ties exactly (Share Capital + Reserves = Total Equity, all 5 years). BUT headline return ratios are non-GAAP adjusted: ROCE excludes a large, growing CWIP (123.7 Cr Mar-26). CWIP-inclusive ROCE FY26 ≈ 178.6 / (667.4 TNW + 112.1 NCL) = **~22.9%**, vs 27% reported — a ~4pp haircut that sits right on the thesis ">22% Green" line and below the "ROCE 25%" thesis anchor. As CWIP converts to PPE this reverses, but on as-reported basis the monitoring green light is marginal. |
| A3-F14-01 | F14 | Awards; CF header | slide 25 L763 vs L770; slide 33 L1044 | "AD 2000 - Merkblatt W0" (L763) vs "TUV – AD 200 Merkblatt W0" (L770); CF columns "Mar-26 Mar-25 Mar-24 FY23 FY22" (L1044) | NEUTRAL-FACT | Individually immaterial drafting slips (AD 2000 vs AD 200; period labels mix Mar-YY and FY within one table) — cumulatively a low-grade disclosure-quality data point. |
| A3-F16-01 | F16 | DROPPED_SLIDE section | ledger §2 L113-120 | "DROPPED_SLIDE cannot be computed this quarter" | NEUTRAL-FACT | No prior deck supplied -> slide-drop, axis-baseline and guidance-softening diffs are unavailable this run. Silence-detection layer must come from companies/VENUSPIPES.md or a later run. Genuine gap, flagged not skipped. |
| A3-F16-02 | F16 | absent operating KPIs | deck-wide (cf. slide 20 L620 capacity; no volume/util) | capacity "48,000" MT stated (L620); **no** sales-volume MT, **no** utilisation %, **no** EBITDA/kg anywhere in 629 numbers | AMBIGUOUS | For a pipes manufacturer the deck omits sales volume (MT), capacity utilisation (overall AND fittings-plant — monitoring item 2) and EBITDA/kg realization. Utilisation cannot be derived (capacity given, volume withheld). Their absence in a 37-slide deck is a disclosure choice worth an A4 question. |
| A3-F16-03 | F16 | Highlights vs Geography split | slide 8 L230 vs slide 12 L371/L389-390 | "exports continued to remain around 30% ... standing at INR 94 Cr" (L230) vs "Exports -9%" (L371) and contribution "37%" -> "29%" (L390/L389) | FORWARD-SIGNAL | Export share fell 37% -> 29% YoY (-8pp) and export revenue fell -9% (103.1 -> 93.7), but slide 8 frames it as "continued to remain around 30%" and rounds 93.7 up to "94 Cr". Declining export franchise softened into stability language — monitoring item 3 is trending down, not stable. |
| A3-F16-04 | F16 | monitoring-checklist silence | deck-wide; slide 25 approvals L750-788 | deck lists ISO/TÜV/IBR/BIS/NABL approvals; **no** mention of DRI investigation, **no** BHEL/NTPC approval, **no** risk-factor slide | AMBIGUOUS | Silence audit vs Notion watch items: (1) DRI investigation — not mentioned, no risk-factor slide; (4) BHEL/NTPC approval — not mentioned despite an approvals slide. Sustained silence on a previously-flagged watch item; A4 to convert to management questions. |
| A3-F16-05 | F16 | Order book / LOI | slide 9 L268; slide 5 L118 | "Order Book Increased ~2.5 times to INR 450 Crores" (L268, under FY23->FY26 "During the Same Period"); "LOI received for INR 185 Cr Order" (L118) | AMBIGUOUS | Order-book figure (450) carries no definition (gross/net of GST, executed/pending) and no as-of date — it sits in an FY23->FY26 historical block, not clearly a Q1FY27 current book. The 185 Cr is an LOI, not a firm PO. Order-book quality/date needs clarification. |
| A3-F16-06 | F16 | margin trend vs growth framing | slide 30 L940-943; slide 13 L427-428; slide 14 L458/L476 | EBITDA Margin "18.2% 17.5% ... 16.3%" (L940-941); PAT Margin "10.7% ... 9.7% ... 8.7%" (L940-942); Q1 "16.1%" / "8.2%" (L458/L476) | FORWARD-SIGNAL | Deck leads with "+40%" EBITDA CAGR (L916) while EBITDA margin compressed 18.2% (FY24) -> 16.3% (FY26) -> 16.1% (Q1FY27) and PAT margin 10.7% -> 8.7% -> 8.2%. Q1FY27 PAT grew only +6.5% vs revenue +16% (depreciation +38%, finance cost +15%, other income -31%) — the capex cycle's below-EBITDA drag is now hitting PAT. Watch thresholds MISSED: PAT 26.4 (<28-30 target); EBITDA margin 16.1% (< 16.5% rising target). |

---

## 2. CHECKLIST SCORECARD (all 17 — no blanks)

| Check | Status | One-line basis |
|-------|--------|----------------|
| F1 ZERO-VALUE STANDING LINES | **FINDING** | Exceptional-item line non-zero (FY26 +0.5, Q4FY26 -0.2), unexplained; first-ever ROU/lease lines Mar-26 (A3-F1-01). Other 6 ZERO_STANDING rows are immaterial historical nils/dashes. |
| F2 STANDALONE vs CONSOLIDATED | **N.A.** | Standalone-only issuer; deck carries no consolidated column, no subsidiary/JV/associate. No S-vs-C gap to decompose. |
| F3 SHELL-ENTITY DETECTION | **N.A.** | No subsidiaries disclosed; no consolidated cost lines to compare. |
| F4 UNAUDITED CONTRIBUTION RATIO | **N.A.** | A presentation carries no auditor Other-Matters / component-auditor disclosure. |
| F5 GOING CONCERN / EoM SCOPE | **N.A.** | No auditor report / EoM paragraph in a deck; no prior deck for verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | **FINDING** | Spooling "commencement by end of year" (L232), 185 Cr LOI + ~70 Cr capex "on track" (L118/135/499), +6.1 MW solar "in progress" (L1176), fittings/VAP mix-up "over medium term" (L496). See register. |
| F7 HEDGE PHRASE MINING | **FINDING** | MD adds export hedge: "area of watch", "monitoring closely", "may create near-term uncertainty" (L504-506) atop a -9% export quarter (A3-F7-01). |
| F8 TAX FORENSICS | **PASS** | ETR consistent ~26% (Q1FY27 9.3/35.7=26.0%; FY22-26 all 25.7-26.1%), modestly above 25.17% statutory, no anomaly. Deferred tax is a persistent LIABILITY (0.7->18.2, capex depreciation timing), not a DTA credit; no "earlier years" adjustment disclosed. |
| F9 OCI FORENSICS | **N.A.** | No OCI / actuarial disclosure anywhere in the deck. |
| F10 SHARE COUNT AND DILUTION | **FINDING** | Paid-up capital 20.4 (Mar-25) -> 20.7 (Mar-26) via warrant conversion; 35.06 Cr warrant programme implies possible residual dilution; no EPS spread given (A3-F10-01). |
| F11 RESERVES / NET WORTH TIE-OUT | **FINDING** | Net worth ties exactly all 5 years, BUT MATERIAL_FOOTNOTE: RoE excludes IPO/warrant proceeds and ROCE excludes CWIP — CWIP-inclusive ROCE FY26 ≈ 22.9% vs 27% reported, on the ">22% Green" line and below the 25% thesis anchor (A3-F11-01). |
| F12 SEGMENT FORENSICS | **N.A.** | Deck gives segment REVENUE only (Seamless/Welded/Others); no segment assets/liabilities to trend. |
| F13 BOARD OUTCOME BEYOND RESULTS | **N.A.** | No board resolution / AGM notice / record date / director term-date content in the deck (bios only, no re-appointment dates). |
| F14 NOTE DRAFTING INCONSISTENCIES | **FINDING** | "AD 2000" vs "AD 200" (L763/L770); CF table mixes Mar-YY and FY period labels (L1044) — cumulative low-grade data point (A3-F14-01). |
| F15 ENTITY LIST DIFFS | **N.A.** | No consolidation list; standalone issuer; no prior deck to diff. |
| F16 DROPPED / REFRAMED DISCLOSURES | **FINDING** | DROPPED_SLIDE not computable (no prior deck, A3-F16-01); volume/util/EBITDA-kg absent (02); export share reframed "around 30%" vs 29% falling (03); DRI + BHEL/NTPC silence (04); order-book undefined (05); margin compression masked by growth framing (06). |
| F17 CONCALL SILENCE AUDIT | **N.A.** | Not a concall transcript. Notion-checklist silence cross-reference performed anyway and carried under F16-04 (DRI, BHEL/NTPC) and F16-02 (utilisation) so the silence layer is not a gap. |

Blank checks: none. **GATE A3: pass.**

---

## 3. COMMITMENT REGISTER (from F6)

| # | Commitment | Implied date | Ref | Status word |
|---|-----------|--------------|-----|-------------|
| 1 | Forward integration into pipe spooling commences | "by end of year" (CY2026 / FY27) | slide 8 L232 | underway ("remains on track") |
| 2 | ~INR 70 Cr spooling capex build-out (Spooling Plant + Fabrication Plant + Fitting machines) | tied to #1, by end FY27 | slide 5 L135; slide 15 L499 | underway ("capex execution on track") |
| 3 | INR 185 Cr Data-Centre SS-spool supply order | on LOI conversion | slide 5 L118 | initiated (LOI received, not firm PO) |
| 4 | Steadily increase fittings / value-added product contribution to revenue mix | "over the medium term" | slide 15 L496 | initiated ("intend to") |
| 5 | Additional 6.1 MW in-house solar unit (1.3 MW already installed) | "installation in progress" | slide 36 L1176 | underway |
| 6 | Fittings & Pipe Spooling capability (integrated piping platform) | "(upcoming)" | slide 17 L536; slide 19 L600 | initiated / upcoming |

---

## 4. NOTES FOR A4/A5 (question seeds)

- FORWARD-SIGNAL findings (highest-priority monitoring): A3-F6-01, A3-F6-02, A3-F7-01,
  A3-F11-01, A3-F16-03, A3-F16-06.
- AMBIGUOUS findings (A4 to convert to management questions): A3-F1-01, A3-F10-01,
  A3-F16-02, A3-F16-04, A3-F16-05.
- Monitoring-checklist scorecard (deck read):
  1. DRI investigation — SILENT (no risk slide) [F16-04]
  2. Fittings-plant utilisation — SILENT (no util % anywhere) [F16-02]
  3. Export revenue % — DECLINING 37% -> 29% YoY, framed as "around 30%" [F16-03]
  4. BHEL/NTPC approval — SILENT (approvals slide lists ISO/TÜV/IBR/BIS/NABL only) [F16-04]
  5. Revenue growth YoY — +16% (in the 15% band, below 25% band), framed "healthy growth" [L486]
  6. ROCE vs >22% Green / <18% Red — reported 27% is CWIP-EXCLUDED adjusted basis;
     CWIP-inclusive ≈ 22.9%, marginal-Green [F11-01]
  7. PAT margin trend — DECLINING 10.7% (FY24) -> 8.7% (FY26) -> 8.2% (Q1FY27) [F16-06]
  Watch levels: PAT 26.4 (< 28-30 target, MISS); EBITDA margin 16.1% (< 16.5% rising, MISS).
- Deck arithmetic verified internally consistent (Q1FY27 P&L cascade ties to PAT 26.4;
  segment 176.1+125.3+19.1=320.5; geography 226.8+93.7=320.5; net worth ties all years;
  CAGR differences on slides 9 vs 30/31 are base-year artifacts, FY23->FY26 28% vs
  FY22->FY26 31.8%, both correct — not a finding).

---

```yaml
stage: A3-forensics
company: "VENUSPIPES"
quarter: "Q1 FY27"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "/home/user/inflection-pipeline/runs/venuspipes-q1fy27/work/forensics_presentation_venuspipes_q1fy27.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: FINDING
  F8: PASS
  F9: N.A.
  F10: FINDING
  F11: FINDING
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: N.A.
findings:
  - {id: "A3-F1-01", check: "F1", line: "slide14 L468 / slide31 L984 / slide32 L1005", classification: "AMBIGUOUS", implication: "Exceptional-item line turned non-zero (FY26 +0.5, Q4FY26 -0.2) unexplained; first-ever ROU/lease lines Mar-26 = new leasing activity"}
  - {id: "A3-F6-01", check: "F6", line: "slide8 L232", classification: "FORWARD-SIGNAL", implication: "Spooling commences 'by end of year' (FY27) — dated promise-vs-delivery item"}
  - {id: "A3-F6-02", check: "F6", line: "slide5 L118/L135; slide15 L499", classification: "FORWARD-SIGNAL", implication: "185 Cr LOI + ~70 Cr spooling capex 'on track' — track LOI->PO and cash outflow"}
  - {id: "A3-F6-03", check: "F6", line: "slide36 L1176", classification: "NEUTRAL-FACT", implication: "+6.1 MW solar install in progress (1.3 MW done) — minor ESG capex"}
  - {id: "A3-F7-01", check: "F7", line: "slide15 L504-506", classification: "FORWARD-SIGNAL", implication: "New MD export hedge (geopolitics/freight) atop -9% export quarter telegraphs continued export softness"}
  - {id: "A3-F10-01", check: "F10", line: "slide32 L1002; slide34 L1108", classification: "AMBIGUOUS", implication: "Paid-up capital 20.4->20.7 via warrant conversion; 35.06 Cr warrant programme = possible residual dilution; no EPS spread disclosed"}
  - {id: "A3-F11-01", check: "F11", line: "slide34 L1092-1096; FN15 L1108; FN17 L1110", classification: "FORWARD-SIGNAL", implication: "Net worth ties, but adjusted-basis ROCE (excl CWIP) 27% vs CWIP-inclusive ~22.9% sits on the >22% Green line and below 25% thesis anchor"}
  - {id: "A3-F14-01", check: "F14", line: "slide25 L763/L770; slide33 L1044", classification: "NEUTRAL-FACT", implication: "AD 2000 vs AD 200 typo; mixed Mar-YY/FY period labels — low-grade disclosure-quality data point"}
  - {id: "A3-F16-01", check: "F16", line: "ledger sec2 L113-120", classification: "NEUTRAL-FACT", implication: "No prior deck -> DROPPED_SLIDE / axis-baseline / guidance-softening diffs not computable this run"}
  - {id: "A3-F16-02", check: "F16", line: "deck-wide; slide20 L620", classification: "AMBIGUOUS", implication: "Sales volume (MT), utilisation % (incl fittings plant) and EBITDA/kg absent — utilisation not derivable"}
  - {id: "A3-F16-03", check: "F16", line: "slide8 L230 vs slide12 L371/L389-390", classification: "FORWARD-SIGNAL", implication: "Export share 37%->29% and revenue -9% framed as 'continued to remain around 30%'; declining export franchise softened"}
  - {id: "A3-F16-04", check: "F16", line: "deck-wide; slide25 L750-788", classification: "AMBIGUOUS", implication: "DRI investigation and BHEL/NTPC approval both silent; no risk-factor slide — sustained silence on watch items"}
  - {id: "A3-F16-05", check: "F16", line: "slide9 L268; slide5 L118", classification: "AMBIGUOUS", implication: "Order book 450 Cr undefined (gross/net, executed/pending) and undated; 185 is an LOI not a firm PO"}
  - {id: "A3-F16-06", check: "F16", line: "slide30 L940-943; slide13 L427-428; slide14 L458/L476", classification: "FORWARD-SIGNAL", implication: "EBITDA margin 18.2%->16.1% and PAT margin 10.7%->8.2% compressing while deck leads with +40% CAGR; PAT +6.5% vs rev +16%; watch thresholds missed"}
forward_signals: ["A3-F6-01", "A3-F6-02", "A3-F7-01", "A3-F11-01", "A3-F16-03", "A3-F16-06"]
ambiguous: ["A3-F1-01", "A3-F10-01", "A3-F16-02", "A3-F16-04", "A3-F16-05"]
commitments:
  - {commitment: "Pipe spooling commencement", implied_date: "by end of year (FY27)", ref: "slide8 L232", status_word: "underway"}
  - {commitment: "~70 Cr spooling capex build-out", implied_date: "by end FY27", ref: "slide5 L135; slide15 L499", status_word: "underway"}
  - {commitment: "185 Cr Data-Centre SS-spool order", implied_date: "on LOI conversion", ref: "slide5 L118", status_word: "initiated"}
  - {commitment: "Raise fittings/value-added product revenue mix", implied_date: "over medium term", ref: "slide15 L496", status_word: "initiated"}
  - {commitment: "+6.1 MW in-house solar unit", implied_date: "installation in progress", ref: "slide36 L1176", status_word: "underway"}
  - {commitment: "Fittings & Pipe Spooling integrated platform", implied_date: "upcoming", ref: "slide17 L536; slide19 L600", status_word: "initiated"}
gate_a3: pass
blank_checks: []
```
