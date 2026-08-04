# A3 FORENSIC NOTES — RSYSTEMS Q2 CY2026 (doctype: presentation / earnings press release)

Source extract: `runs/rsystems-q2cy26/work/extract_presentation_rsystems_q2cy26.txt` (579 lines, 11 pages)
Ledger: `runs/rsystems-q2cy26/work/ledger_presentation_rsystems_q2cy26.md` (189 gated rows, 18 categories)
Ledger reconciliation: 100% — every A2 row read verbatim at its cited line before judging.
Unit: Rs. in mn (x0.1 -> Rs Cr); parallel US$ mn columns present. Statutory tax reference: 25.17%.

Doctype note: this is management-authored commentary with embedded consolidated financial
tables. F16 is the primary presentation check; F6/F8/F10/F11/F14 run on the numbers/prose the
deck carries. Reg-33-only checks (F2-F5, F9, F12, F13, F15) that require a standalone column,
an auditor report, an OCI/segment note, a board-outcome agenda, or a consolidation entity list
are marked N.A. with a one-line reason — none of those artifacts exist in a press release. F17
is adapted per the injected task into a silence audit against the Notion monitoring checklist
(no transcript exists yet; concall ~12 Aug 2026).

---

## FINDINGS TABLE

| id | check | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|-------|----------------|------------|----------------|----------------|---------------------|
| A1 | F1 | §9 row 19 | 385 | "Assets held for sale ... - / -" | NEUTRAL-FACT | Template anticipates a disposal class; nil both periods means the FY25 NOIDA property monetisation (Rs 435.95 mn gain) is fully realised and no further asset is queued for sale. Low signal. |
| A2 | F6 | §3 rows 1-4 | 130-131, 135, 145 | "This strategic engagement will drive smarter decision-making, optimize operations, and accelerate growth"; "The GCC will drive AI-powered lending innovation"; "R Systems will modernize customer acquisition" | FORWARD-SIGNAL | Four deal wins framed as future value creation with no revenue, TCV, or ramp date. These are dateable commitments to test at the concall and in the Role 5 promise-vs-delivery tracker. |
| A3 | F6 | §2 row 4 | 121-122 | "sustaining our commitment to consistent shareholder returns" | FORWARD-SIGNAL | CFO reaffirms a shareholder-return commitment (dividend/buyback) with no quantum or date — a dateable capital-allocation commitment; ask for the payout mechanism and quantum. |
| A4 | F8 | §5 rows 9,12 | 186, 190 | "Profit before tax 805.07 ... Total tax expense 249.37" | FORWARD-SIGNAL | Q2 2026 ETR = 249.37/805.07 = 30.98%, ~5.8pp above the 25.17% statutory rate and up ~7.5pp YoY (Q2 2025 = 23.52%). A structurally higher tax take is a drag on reported PAT conversion; deferred-tax credit of only (3.94) offers little shield. |
| A5 | F10 | §9 rows 21-22; §5 rows 14-15 | 390-391, 194-195 | "Equity share capital 118.49 / 118.40"; "Instrument entirely equity in nature 5.16 / -" | FORWARD-SIGNAL | Paid-up capital rose 0.09 mn (Re 1 par -> ~90k new shares, RSU allotment). A new "instrument entirely equity in nature" of Rs 5.16 mn appears where prior period was nil — a corporate action needing a source note. Basic/diluted EPS spread ~4.3% (4.69 vs 4.49) confirms live dilutive RSUs. |
| A6 | F14 | §5 row 9; §6 row 9 | 186, 235 | "Profit before tax (1-2)" (quarter) vs "Profit before tax (1+2)" (six months) | NEUTRAL-FACT | Same subtotal labelled with two different derivation signs across adjacent tables. Immaterial arithmetically but a drafting-control data point. |
| A7 | F16 | §1 rows 1,4; page 2 banner | 62, 72, 82 | "Revenue Growth 30%"; "YoY Growth of 30.2% in INR terms and 17.7% in US$ terms" | AMBIGUOUS | Headline leads with the 30.2% INR figure; the US$ figure is 17.7%. The 12.5pp gap is currency plus Novigo inorganic. Organic constant-currency growth is disclosed nowhere — reported growth is not organic. Must be decomposed at the concall. |
| A8 | F16 | §1 row 3; §5 row 13; §7 row 20 | 78, 191, 292, 296 | "Adj. Net profit after taxes^ Rs. 629 mn ... YoY growth of 35.4%" | CONFIRMATORY-NEGATIVE | Reported Net profit fell to 555.70 from 758.54 YoY (-26.7%). The +35.4% headline exists only because the adjusted base strips FY25's Rs 409.36 mn non-recurring gain (NOIDA sale). Adjustments flatter the trend; the reported-PAT decline is absent from Highlights. |
| A9 | F16 | §16 row 2-3 footnote | 520 | "DSO is based on TTM and excluding the new acquisition of Novigo" | AMBIGUOUS | Novigo drives the INR-vs-US$ growth gap yet its revenue is never quantified, and the DSO metric is explicitly reframed to exclude it. Selective de-scoping of the acquisition; ask for Novigo quarterly revenue and margin uplift. |
| A10 | F16 | §3 rows 1-5 | 128-152 | "A leading global telecommunications and media company has engaged R Systems..." | AMBIGUOUS | Five key deal wins narrated with zero revenue, TCV, or duration. Impossible to size against the ACV-bookings monitor; convert to a booking-quantification question. |
| A11 | F17 | Notion checklist items 1,2,3,6,9 | 62-88, 431-521 | (silence — metric absent from doc) | FORWARD-SIGNAL | Press release is silent on organic constant-currency growth, TTM ACV bookings, Novigo quarterly revenue, fixed-price mix, and annualised ROCE. Each is a monitoring trigger; sustained silence on the organic/bookings line is a confirmatory negative if repeated. |
| A12 | F16 | §5 row 5; §7 row 16 | 182, 288, 332 | "Finance costs 94.77 ... 21.41" | FORWARD-SIGNAL | Finance cost quadrupled YoY (21.41 -> 94.77; H1 36.31 -> 190.68), reflecting Novigo acquisition debt (non-current borrowings 2,697.75 mn). Not mentioned in Highlights. Interest coverage still ~9.6x (EBIT 908.57/94.77) but the trajectory compresses the buffer toward the >6x trigger. |

---

## CHECKLIST SCORECARD (all 17; GATE A3 = every check has a status)

| Check | Status | Basis (one line) |
|-------|--------|------------------|
| F1 ZERO-VALUE STANDING | FINDING | One ZERO_STANDING row — "Assets held for sale" nil both periods (line 385); anticipates disposal class, low signal (A1). |
| F2 STANDALONE vs CONSOLIDATED | N.A. | Press release presents consolidated figures only; no standalone column to decompose. |
| F3 SHELL-ENTITY DETECTION | N.A. | Requires standalone-vs-consolidated cost lines; not present in a press release. |
| F4 UNAUDITED CONTRIBUTION RATIO | N.A. | No auditor "Other Matters" paragraph in a press release; tables marked "Un-audited" wholesale. |
| F5 GOING CONCERN / EoM | N.A. | No auditor EoM/going-concern paragraph; no prior-quarter extract supplied for a verbatim diff. |
| F6 FORWARD-COMMITMENT MINING | FINDING | "will drive"/"will modernize" deal commitments (A2) and "commitment to consistent shareholder returns" (A3). |
| F7 HEDGE PHRASE MINING | PASS | Only standard Safe Harbor boilerplate ("could differ", line 561) and CFO "approximately 20.1%" softening; no new hedge on revenue lumpiness or customer concentration. |
| F8 TAX FORENSICS | FINDING | Q2 2026 ETR 30.98% vs 25.17% statutory, +7.5pp YoY (A4); no "earlier years" tax-adjustment line disclosed. |
| F9 OCI FORENSICS | N.A. | No OCI statement / actuarial disclosure in the press release. New Hedge Reserve (Ind AS 109, line 197) noted but no actuarial trend to test. |
| F10 SHARE COUNT & DILUTION | FINDING | Paid-up capital +0.09 mn (RSU allotment) and new Rs 5.16 mn equity instrument (A5); EPS spread ~4.3% confirms live RSUs. |
| F11 RESERVES / NET WORTH TIE-OUT | PASS | 118.49 + 5.16 + 10,859.03 = 10,982.68 = total equity attributable (line 393) = headlined Rs 10,983 mn (lines 158, 519). Ties within rounding. |
| F12 SEGMENT FORENSICS | N.A. | Only revenue % by vertical/geography given; no segment assets/liabilities disclosed. |
| F13 BOARD OUTCOME | N.A. | No board's report, AGM notice, director-term or capital-raise resolution in a press release. |
| F14 NOTE DRAFTING INCONSISTENCIES | FINDING | PBT subtotal labelled "(1-2)" (line 186) vs "(1+2)" (line 235) across adjacent tables (A6). |
| F15 ENTITY LIST DIFFS | N.A. | No consolidation entity list to diff; Novigo referenced (line 520) but no full list — captured under F16 (A9). |
| F16 PRESENTATION-SPECIFIC | FINDING | INR-vs-US$ headline framing (A7), adjusted-flatters-reported PAT (A8), Novigo unquantified/DSO reframed (A9), unquantified deal wins (A10), finance-cost surge not highlighted (A12). |
| F17 CONCALL SILENCE AUDIT | FINDING | Adapted per injected task: silence audit vs Notion monitoring checklist — 5 triggers undisclosed (A11). No transcript yet; concall ~12 Aug. |

---

## COMMITMENT REGISTER (from F6)

| commitment | implied date | note/line ref | status word |
|------------|--------------|---------------|-------------|
| Telecom/media analytics engagement "will drive smarter decision-making, optimize operations, and accelerate growth" | none stated | line 130-131 | underway (engaged) |
| U.S. small-business-lender GCC "will drive AI-powered lending innovation, modernize core platforms" | none stated | line 133-135 | established/commenced |
| HNW Reimagine QE partnership "enabling faster innovation, greater reliability" | none stated | line 138-141 | underway (partnered) |
| Financial-services Microsoft Dynamics 365 Retail "R Systems will modernize customer acquisition, engagement, onboarding" | none stated | line 143-145 | initiated (selected) |
| AdTech core platform modernisation "supports future growth ... innovate more quickly" | none stated | line 148-152 | completed (upgraded) |
| "sustaining our commitment to consistent shareholder returns" | none stated | line 121-122 | ongoing |

---

## "WHAT WAS NOT DISCLOSED" — Notion monitoring checklist silence audit (F17)

| # | Monitor trigger | Disclosed? | Verdict / classification |
|---|-----------------|-----------|--------------------------|
| 1 | Organic constant-currency revenue growth >5% | No | AMBIGUOUS — only reported INR 30.2% / US$ 17.7% (Novigo+FX); organic CC not given. Concall Q. |
| 2 | TTM ACV bookings >$88m | No | FORWARD-SIGNAL — no bookings/ACV metric anywhere. Concall Q. |
| 3 | Novigo revenue disclosed >Rs 55 Cr/qtr | No | AMBIGUOUS — Novigo revenue never quantified; DSO reframed to exclude it (line 520). Concall Q. |
| 4 | Adjusted EBITDA margin >=18.5% | Yes | MET — 20.1% (line 75). |
| 5 | USD/INR >89 | Implied | MET (derived) — 6,017.01/63.56 = ~94.7 avg rate; not stated explicitly. |
| 6 | Fixed-price mix >18% | No | FORWARD-SIGNAL — no contract-type/pricing mix disclosed. Concall Q. |
| 7 | Debtor turnover >=1.45x | Partial | MET (derived) — quarterly rev/receivables 6,017.01/3,760.81 = 1.60x; billed DSO 55d (line 516). |
| 8 | Interest coverage >6x | Partial | MET (derived) — EBIT 908.57/finance cost 94.77 = ~9.6x, but coverage compressing (see A12). |
| 9 | Annualised ROCE >20% | No | AMBIGUOUS — not disclosed and not cleanly derivable from the deck. Concall Q. |

THESIS-BROKEN triggers scan: no KMP fraud, no audit qualification (doc is un-audited by design,
not qualified); no Blackstone/NCI exit signal in the text (NCI held flat at 1,923.88, line 394);
organic revenue sign undeterminable from this doc (feeds trigger-1 monitoring). Nothing tripped
from the press release alone.

---

## ADJUSTED-TO-REPORTED BRIDGE (supporting A8, the core presentation finding)

| metric | Q2 2026 reported | Q2 2026 adjusted (headline) | Q2 2025 reported | Q2 2025 adjusted | headline YoY | reported YoY |
|--------|------------------|-----------------------------|-------------------|-------------------|--------------|--------------|
| Net profit (mn) | 555.70 (L191) | 628.74 (L296) | 758.54 (L191) | 464.38 (L296) | +35.4% | -26.7% |
| Basic EPS (Rs) | 4.69 (L194) | 5.31 (L205) | 6.41 (L194) | 3.92 (L205) | +35.5% | -26.8% |
| EBITDA (mn) | 1,145.13 (L282) | 1,207.50 Adj (L279) | 748.71 (L282) | 797.43 Adj (L279) | +51.4% | +52.9% |

The PAT adjustment reverses direction of the YoY trend (from -26.7% reported to +35.4% adjusted)
because FY25's Rs 409.36 mn NOIDA-sale gain (L286) sits in the reported base and is stripped from
the adjusted base. This is the single most consequential presentation choice in the deck.

---

## GATE A3
Every F1-F17 carries exactly one status; every FINDING cites a line number and a verbatim quote.
17/17 statuses assigned, 0 blanks. GATE A3 = PASS.

```yaml
stage: A3-forensics
company: "rsystems"
quarter: "q2cy26"
doctype: "presentation"
model: claude-opus-4-8
status: complete
forensics_path: "runs/rsystems-q2cy26/work/forensics_presentation_rsystems_q2cy26.md"
ledger_reconciled_pct: 100
checklist:
  F1: FINDING
  F2: N.A.
  F3: N.A.
  F4: N.A.
  F5: N.A.
  F6: FINDING
  F7: PASS
  F8: FINDING
  F9: N.A.
  F10: FINDING
  F11: PASS
  F12: N.A.
  F13: N.A.
  F14: FINDING
  F15: N.A.
  F16: FINDING
  F17: FINDING
findings:
  - {id: "A1", check: "F1", line: "385", classification: "NEUTRAL-FACT", implication: "Assets-held-for-sale nil both periods; FY25 NOIDA disposal fully realised, none queued"}
  - {id: "A2", check: "F6", line: "130-131,135,145", classification: "FORWARD-SIGNAL", implication: "Four deal wins framed as future value with no revenue/date; promise-vs-delivery tracker rows"}
  - {id: "A3", check: "F6", line: "121-122", classification: "FORWARD-SIGNAL", implication: "Shareholder-return commitment with no quantum/date; ask payout mechanism"}
  - {id: "A4", check: "F8", line: "186,190", classification: "FORWARD-SIGNAL", implication: "Q2 ETR 30.98% vs 25.17% statutory, +7.5pp YoY; structural PAT-conversion drag"}
  - {id: "A5", check: "F10", line: "390-391,194-195", classification: "FORWARD-SIGNAL", implication: "Paid-up +0.09mn RSU allotment; new Rs5.16mn equity instrument; live dilution"}
  - {id: "A6", check: "F14", line: "186,235", classification: "NEUTRAL-FACT", implication: "PBT subtotal labelled (1-2) vs (1+2) across tables; drafting-control data point"}
  - {id: "A7", check: "F16", line: "62,72,82", classification: "AMBIGUOUS", implication: "Headline INR 30.2% vs US$ 17.7%; gap is FX+Novigo, organic CC undisclosed"}
  - {id: "A8", check: "F16", line: "78,191,292,296", classification: "CONFIRMATORY-NEGATIVE", implication: "Reported PAT -26.7% YoY masked by +35.4% adjusted; FY25 NOIDA gain stripped from base"}
  - {id: "A9", check: "F16", line: "520", classification: "AMBIGUOUS", implication: "Novigo revenue unquantified; DSO reframed to exclude acquisition"}
  - {id: "A10", check: "F16", line: "128-152", classification: "AMBIGUOUS", implication: "Five deal wins with zero revenue/TCV; cannot size against ACV monitor"}
  - {id: "A11", check: "F17", line: "62-88,431-521", classification: "FORWARD-SIGNAL", implication: "Silent on organic CC growth, ACV bookings, Novigo revenue, fixed-price mix, ROCE"}
  - {id: "A12", check: "F16", line: "182,288,332", classification: "FORWARD-SIGNAL", implication: "Finance cost 4x YoY (Novigo debt); interest coverage compressing toward >6x trigger, not highlighted"}
forward_signals: ["A2", "A3", "A4", "A5", "A11", "A12"]
ambiguous: ["A7", "A9", "A10"]
commitments:
  - {commitment: "Telecom/media analytics engagement 'will drive smarter decision-making, optimize operations, accelerate growth'", implied_date: "none stated", ref: "L130-131", status_word: "underway"}
  - {commitment: "U.S. small-business-lender GCC 'will drive AI-powered lending innovation, modernize core platforms'", implied_date: "none stated", ref: "L133-135", status_word: "commenced"}
  - {commitment: "HNW Reimagine QE partnership 'enabling faster innovation, greater reliability'", implied_date: "none stated", ref: "L138-141", status_word: "underway"}
  - {commitment: "Microsoft Dynamics 365 Retail 'R Systems will modernize customer acquisition, engagement, onboarding'", implied_date: "none stated", ref: "L143-145", status_word: "initiated"}
  - {commitment: "AdTech core-platform modernisation 'supports future growth ... innovate more quickly'", implied_date: "none stated", ref: "L148-152", status_word: "completed"}
  - {commitment: "'sustaining our commitment to consistent shareholder returns'", implied_date: "none stated", ref: "L121-122", status_word: "ongoing"}
gate_a3: pass
blank_checks: []
```
