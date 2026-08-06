# A3 FORENSIC NOTES — IKS (Inventurus Knowledge Solutions Ltd) — Q1 FY27 — DOCTYPE: PRESENTATION

Source deck: `extract_presentation_iks_q1fy27.txt` (18 PDF pages; footer slides 1-17)
Ledger: `ledger_presentation_iks_q1fy27.md` — 100% of rows read at cited lines and reconciled.
Cross-check filing: `extract_results_iks_q1fy27.txt` (Board Outcome + Limited Review Report, PWC, unaudited).
Prior-quarter deck ledger: NOT PROVIDED (`PRIOR_LEDGER_UNAVAILABLE`) — dropped-slide diff could not run.
Notion checklist: NONE (fresh coverage).

## RECONCILIATION SUMMARY (deck vs filing — headline P&L)
All deck headline figures tie to the consolidated limited-reviewed filing within rounding:
- Revenue 8,936 = filing 8,936.29 (deck L450 / filing L319). Q1FY26 7,401 = 7,400.95; Q4FY26 8,577 = 8,576.52.
- EBITDA 2,949 = filing-derived 2,949.40 (PBT-before-assoc 2,562.51 + D&A 342.89 + Fin cost 101.10 − Other income 57.10). Deck L457 / filing L319-331.
- PAT 1,937 = filing 1,937.41 (L468 / L345). Tax 572 = filing total tax 572.03 (L464 / L343).
- Employee benefit excl ESOP 4,332 + ESOP 218 = filing Employee benefit 4,550.10 (L452/456 / L325). Clean.
- EPS deck 11.6/12.3/9.1 = filing BASIC EPS 11.56/12.31/9.07 (L422-425 / L391).
No hard deck-vs-filing numeric contradiction on revenue/EBITDA/PAT/margins/tax/EPS. All findings below are (a) selective framing / non-GAAP normalisation inside the deck, (b) material items disclosed in the filing but ABSENT from the deck, or (c) internal deck inconsistencies.

---

## FINDINGS TABLE

| id | F# | ledger row ref | line/slide | verbatim quote | classification | forward implication |
|----|----|----------------|-----------|----------------|----------------|---------------------|
| F1 | F1 | Tbl2 r19 ZERO_STANDING | deck L467; filing L335, L427-428 | "Share of Profit/(Loss) from Associates (net of tax) (53) [Q1FY26 blank]" | FORWARD-SIGNAL | Q1FY26 blank is genuine (associate acquired after Q1FY26). Per filing note 8 the associate (IKS WWMG MSO LLC) became a step-down SUBSIDIARY w.e.f. June 30, 2026 — this equity-method loss line disappears and full consolidation begins Q2FY27; deck is silent on the transition. |
| F6 | F6 | Tbl5 slide16 r14; slide4 | deck L582, L546/574/578, L158 | "Sustained EBITDA expansion without significant dilution of Equity"; FY30 EBITDA ~30,000 / Net Debt 3,000; "Execute Operating model Transformation in TruBridge RCM & Coding Businesses" | FORWARD-SIGNAL | Dated FY30 guidance + TruBridge integration commitment. TruBridge (EV up to US$557mn) closed July 9 2026 per filing note 9 — NOT in Q1 numbers yet the deck's strategy/targets assume it. See commitment register. |
| F7 | F7 | Tbl4 r6/7/10; slide2 disc. | deck L314-325, L443, L349, L370 | "1.8% QoQ (due to one-time acquisition costs and reduction in currency gains)"; "*ROE declined due to increased equity base from revaluation of Abridge, alongside lower earnings from reduced currency gains and one-time acquisition costs" | FORWARD-SIGNAL / AMBIGUOUS | Deck pre-emptively hedges QoQ EBITDA fall (35.0%→33.0%) and ROE fall (31.3%→26.4%) as "one-time." Forex tailwind collapsed (Q4 forex gain 352 → Q1 12, L451). Signals margin/ROE pressure persisting; test whether "one-time" costs recur with TruBridge integration. |
| F8 | F8 | Tbl2 r14/16 | deck L462/464; filing L338/341-343 | deck: "Tax expense 572"; filing: "Current tax 682.98 / Deferred tax (110.95) / Total 572.03" | FORWARD-SIGNAL | Consol ETR ≈22.3% (572/2,563) vs statutory 25.17%. Deck's single tax line masks a Rs 110.95mn deferred-tax CREDIT (~440 bps shield); credits persistent (Q1FY26 −138.77, standalone Q1FY27 −64.00). Q4FY26 ETR only ~18.6%. ETR normalisation is a future earnings headwind. |
| F10 | F10 | Tbl5 slide12 r1-5 | deck L422-429; filing L391-393 | "12.3 ... 11.6 ... 9.1 ... 6.1% QoQ" | AMBIGUOUS | Deck shows BASIC EPS only; "6.1% QoQ" is presented unsigned though EPS FELL 12.3(Q4)→11.6(Q1FY27). Diluted EPS omitted (filing: diluted 11.32 vs basic 11.56). ESOP issuance ongoing (filing note 5: 140,085 allotted, 143,814 granted). |
| F13 | F13 | (filing-only; deck silent) | filing L45-54, L77-84, L488-489, L418-420 | "Mr. Berjis Desai ... expressed his unwillingness to seek re-appointment"; "designated Mr. Clarence Carleton King II, Independent Director, as ... Non-Executive Chairman ... w.e.f. conclusion of ensuing 20th AGM" | FORWARD-SIGNAL | Board transition: Non-Executive/Non-Independent Chairman retiring; an INDEPENDENT director becomes Non-Exec Chairman (net governance improvement). 20th AGM record/effective date Sept 21 2026 → Annual Report imminent → schedule Role 6 AR Deep Dive. Deck omits all board-outcome content. |
| F14 | F14 | INTERNAL_INCONSISTENCY x1 | deck L295-296 vs L486/490 | "INR mn 3,759 / Revenue from Top 10 customers" | AMBIGUOUS | Slide 8 headline labels a Top-5 figure (3,759, = slide-14 Top-5) as "Top 10" (actual Top 10 = 4,808). Also deck L462 "Profit before exceptional items and tax" mislabels the before-associates subtotal (no exceptional items exist). Drafting-consistency data point; confirm which concentration figure is authoritative. |
| F15 | F15 | (filing entity list) | filing L238, L427-428, L446-448, L438-440 | "IKS WWMG MSO, LLC [Step down Subsidiary w.e.f. June 30, 2026]"; "acquired ... ARAI ... has become a subsidiary" | FORWARD-SIGNAL | Three in-period/post-period structure changes: (1) WWMG associate→step-down subsidiary (June 30 2026); (2) ARAI new wholly-owned subsidiary (May 14 2026, Rs 110mn); (3) TruBridge acquisition completed July 9 2026 (EV up to US$557mn, subsequent event). Deck discloses none. Q2FY27 consolidation scope changes materially. |
| F16a | F16 | Tbl5 slide3 r6/7 | deck L118, L129 | "600+/650+ ... Healthcare Organizations ... Q1 27/Q1 26" | FORWARD-SIGNAL | Client-organisation count DECLINED YoY (650+ → 600+) while revenue rose 20.7% — fewer, larger clients. Presented under "Established Client Relationships" without noting the decline. |
| F16b | F16 | Tbl3 r3/5 | deck L488, L492 | "Contribution from Top 10 customers 53.8% [Q1FY26 43.4%]"; "Top 5 42.1% [31.7%]" | FORWARD-SIGNAL | Customer concentration rising sharply YoY (Top10 +10.4pp, Top5 +10.4pp). Corroborates the org-count decline. Concentration risk building. |
| F16c | F16 | Tbl4 r7; slide10 | deck L370, L375, L499 | "OCF and FCF are adjusted for upfront guarantee payment of economic value add made to a customer, for Rs 1,430 mn in Q1 FY27" | AMBIGUOUS | Deck FCF 1,742 is AFTER adding back a Rs 1,430mn cash payment to a customer; unadjusted FCF ≈ 312mn (~5.6x lower). "FCF Yield 89.9%" (L499) rests on the adjusted figure. Nature of the payment (contra-revenue? recurring? guarantee call?) is undisclosed. |
| F16d | F16 | Tbl5 slide16 r11 | deck L574-575 | "LTM Sep 24 Pre-IPO Baseline" | AMBIGUOUS | FY30 outlook anchors CAGR to a hand-picked "Pre-IPO Baseline" (LTM Sep'24), flattering the growth optic; slide 15 similarly frames a 28.7%/46.4% CAGR from FY2017. Selective period framing. |
| F16e | F16 | Tbl3 r7 | deck L494-496 | "Ageing of Top 5 clients (number of years) 7.41 [Q1FY26 5.52]" | AMBIGUOUS | Top-5 average vintage jumped +1.89 yrs in 12 months (mathematically impossible for a stable set) while Top-10 rose only +0.22 — the Top-5 client COMPOSITION shifted. Possible churn/replacement in the top cohort. |
| F16f | F16 | Tbl5 slide9 r9 | deck L314-316 | "24.0% YoY (even higher if not for one-time acquisition costs)" | AMBIGUOUS | Unquantified "even higher" adjustment on EBITDA growth; magnitude of the acquisition-cost drag not disclosed on-slide (only footnoted as inside Other Expenses, L475). |

Not carried as findings (checked, no issue): headline P&L reconciliation is clean (see summary). Adjusted PAT and EBITDA-excl-ESOP are non-GAAP but ARE reconciled inside the slide-13 table (Amort of intangibles 216 → Adj PAT 2,153; ESOP 218 bridges the two EBITDA lines).

---

## CHECKLIST SCORECARD (all 17)

| F# | Check | Status | Basis (one line) |
|----|-------|--------|------------------|
| F1 | Zero-value standing items | FINDING | Associate line blank in Q1FY26 (deck L467); entity became subsidiary June 30 2026 per filing note 8 — deck silent. |
| F2 | Standalone vs consolidated | N.A. | Deck presents CONSOLIDATED figures only; no standalone data to decompose (filing standalone PAT 1,625.46 vs consol 1,937.41, not in deck). |
| F3 | Shell-entity detection | N.A. | Deck carries no entity-level cost breakdown; needs filing cost lines by entity (not present). |
| F4 | Unaudited contribution ratio | N.A. | No auditor Other Matters in a deck. Cross-check: filing notes 6-7 unaudited portion is a net LOSS (5 subs −5.67mn + associate −53.07mn) ≈ 3% of PAT, below 10% threshold — no finding. |
| F5 | Going concern / EoM | N.A. | PWC review report is UNMODIFIED (filing L155-160, L255-261); no going-concern or emphasis-of-matter paragraph; deck carries none. |
| F6 | Forward-commitment mining | FINDING | FY30 targets + "without significant dilution of Equity" (deck L582) + TruBridge integration commitment; see register. |
| F7 | Hedge-phrase mining | FINDING | Deck pre-emptively hedges QoQ EBITDA & ROE declines as "one-time"/forex (deck L321-325, L443). |
| F8 | Tax forensics | FINDING | ETR ≈22.3% < 25.17% statutory; deck's single tax line masks Rs 110.95mn deferred-tax credit (~440bps shield), persistent (filing L341-343). |
| F9 | OCI forensics | N.A. | Deck carries no OCI statement. Cross-check: no actuarial swing > prior year; Abridge FVOCI revaluation (+226.42mn, filing L377) is referenced only via ROE footnote. |
| F10 | Share count & dilution | FINDING | Basic EPS only; QoQ "6.1%" is an unsigned DECLINE (12.3→11.6); diluted (11.32) omitted; ESOP issuance ongoing (filing note 5). |
| F11 | Reserves & net-worth tie-out | N.A. | Deck carries no net worth / reserves figure (filing: paid-up 170.71 + reserves 27,831.66); nothing on-deck to tie out. |
| F12 | Segment forensics | N.A. | Single reportable segment per filing note 4 (L415-416); no segment assets/liabilities disclosed. |
| F13 | Board outcome beyond results | FINDING | Chairman Berjis Desai retiring; Independent Director King designated Non-Exec Chairman; 20th AGM Sept 21 2026 → AR deep-dive catalyst (filing L45-54, L77-84). |
| F14 | Note-drafting inconsistencies | FINDING | Slide-8 mislabels Top-5 (3,759) as "Top 10" vs slide-14 Top10=4,808; "before exceptional items" mislabel; minor entity-name comma variances. |
| F15 | Entity-list diffs | FINDING | WWMG associate→subsidiary; ARAI new sub; TruBridge completed July 9 — three scope changes, deck silent (filing L238, L446-448, L438-440). Prior-deck diff N/A (`PRIOR_LEDGER_UNAVAILABLE`). |
| F16 | Presentation: dropped/reframed | FINDING | Org count 650+→600+ decline; rising concentration; unsigned EPS/ROE QoQ declines; Rs1,430mn FCF add-back; pre-IPO baseline framing; Top-5 vintage jump; unquantified "even higher." |
| F17 | Concall silence audit | N.A. | Doctype is presentation; no transcript/concall to audit; no Notion checklist (fresh coverage). |

Marks: 9 FINDING, 8 N.A., 0 PASS, 0 blank. GATE A3 = pass.

---

## COMMITMENT REGISTER (F6)

| commitment | implied date | note/slide ref | status word |
|-----------|--------------|----------------|-------------|
| FY30 EBITDA target ≈ INR 30,000 mn (from LTM Jun'26 11,485) | FY2030 | deck slide 16, L546/570/574 | stated target |
| FY30 Revenue target (bar labelled ~30,000; label-to-series binding AMBIGUOUS per ledger) | FY2030 | deck slide 16, L553-574 | stated target (verify) |
| FY30 Net Debt target INR 3,000 mn (from 2,654) | FY2030 | deck slide 16, L578 | stated target |
| "Sustained EBITDA expansion without significant dilution of Equity" | medium-term | deck slide 16, L582 | outlook |
| "Execute Operating model Transformation in TruBridge RCM & Coding Businesses" | ongoing | deck slide 4, L158 | underway |
| "Realize Operating and SG&A Synergies" | ongoing | deck slide 4, L160-161 | initiated |
| "Get back to optimized margins through operating model transformation" | ongoing | deck slide 4, L149-150 | initiated |
| TruBridge acquisition completed (EV up to US$557mn) | July 9, 2026 (done) | filing note 9, L438-440 | completed |
| TruBridge / WWMG PPA finalisation (Ind AS 103 measurement period) | ≤12 months from acq. (by ~June/July 2027) | filing notes 8 & 10, L432-436, L455-457 | in process |
| ARAI acquisition (Rs 110mn, 100%) | completed May 14, 2026 | filing note 10, L446-448 | completed |

---

## FLAGGED FOR A4 (convert to management questions)
FORWARD-SIGNAL: F1, F6, F7, F8, F13, F15, F16a, F16b.
AMBIGUOUS: F7, F10, F14, F16c, F16d, F16e, F16f.
Priority A4 questions: (1) F16c — what is the Rs 1,430mn "upfront guarantee payment of economic value add to a customer," is it recurring/contra-revenue, and what is UNadjusted FCF? (2) F8 — expected normalised ETR once deferred-tax credits exhaust? (3) F6/F15 — TruBridge (US$557mn) revenue/margin/net-debt contribution and whether FY30 targets are pre- or post-TruBridge. (4) F16b/F16a — client-count decline vs rising Top-10 concentration. (5) F14 — is the deck's Top-10 concentration figure 3,759 or 4,808?
