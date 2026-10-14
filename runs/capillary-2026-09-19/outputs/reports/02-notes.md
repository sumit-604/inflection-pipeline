# CAPILLARY — Stage 2, Notes to Financial Statements — PASS 3 (Pattern Pass + Consolidation)

Run date: 2026-09-19 | Source: Annual_Report_2026.pdf (FY26, page-marked text, 271pp)
Units: source reports in INR millions (₹mn); figures below carry the source unit as stated. Two
note sets: STANDALONE (Notes 1-40, pp.125-177) and CONSOLIDATED (Notes 1-44, pp.189-259).

Rating key: 🟢 Clean | 🟡 Watch | 🔴 Red Flag

---

## PASS 3 — PATTERN RE-READ

Six pattern checks were run against the full note set, independent of the sequential Pass 1/2
reads.

1. **Contradictions between notes**: two found, both already surfaced individually but not
   framed as contradictions until this pass.
   - The standalone Ratio Analysis note (Note 36, p.174-176) attaches footnote (b) — "Due to
     decrease in losses during the year/period" — to the ROE and Net Profit ratio rows, but both
     ratios *fell* YoY (ROE 0.74% → 0.44%; NPR 2.01% → 1.36%). The footnote text describes an
     improvement while the row it explains shows deterioration. This is an internal drafting
     contradiction inside a single note, not just an ambiguous explanation (Note 36, p.174-176).
   - The Contingent Liabilities note (standalone Note 31, p.166; consolidated Note 34, p.244)
     promises "a description of claims and assertions... below" and then supplies no table, bullet,
     or line before the next note heading. Confirmed at the line level in Pass 2 (A1) as a genuine
     drafting gap, not an extraction artifact — the note contradicts its own stated structure.
2. **Numbers not matching the main financial statements**: none found. Consolidated PBT before
   exceptional items (₹261.50mn) plus the Churn Indemnity exceptional income (₹249.60mn)
   reconciles exactly to reported consolidated PBT (₹511.10mn) (Note 28, p.235). No other
   note-to-statement mismatch surfaced across either pass.
3. **Deliberately vague vs. detailed disclosure**: the RPT note (standalone Note 32) and the
   segment/geography notes are granular; by contrast, contingent liabilities (above), the major
   customer >10% sentence (Note 36(iii), consolidated, p.246-247 — confirmed in Pass 2 A2 as a
   sentence with no predicate), capital commitments (absent entirely, Pass 2 A5), and the
   forward-contract fair-value line (policy stated, Note 34(2) p.172-173, but zero notional/MTM
   disclosed anywhere) form a consistent pattern: every disclosure that would otherwise show a
   RISK NUMBER (litigation exposure, customer concentration, uncommitted capex, hedge notional)
   is the one left incomplete or unquantified. No single instance is individually alarming, but the
   pattern across four separate notes is worth naming as a house-style gap in this maiden
   post-listing AR, not four unrelated coincidences.
4. **Prior year restated/reclassified**: one cosmetic instance found (Pass 2, B6) — Consolidated
   Note 2.1 (p.195) refers to the "restated Consolidated Statement of Profit and Loss," language
   most likely carried over from the IPO/UDRHP drafting template. No actual prior-year figure was
   found restated anywhere in the note set; standalone Note 40 (p.177) carries only standard
   "regrouped/reclassified wherever necessary" boilerplate. Logged under `restatements_found` as
   a labelling artifact, not a substantive restatement.
5. **Events after balance sheet date**: SessionM Inc. + SessionM Czech Republic s.r.o. acquisition
   from Mastercard International, USD 20.00mn, signed 24-Feb-2026, completed 1-May-2026 —
   five days after the AR was signed (6-May-2026) (Consolidated Note 44, p.259). This is the only
   subsequent event disclosed and is not reflected in any FY26 number. Direct full-text search for
   "going concern" and "material uncertainty" found only standard basis-of-preparation language
   (Standalone Note 2.1, p.[125-126]/main text line "the Company has prepared the Standalone
   Financial Statements on the basis that it will continue to operate as a going concern"; identical
   language, Consolidated Note 2.1, p.195) and standard auditor-responsibility boilerplate — no
   material uncertainty paragraph, no emphasis-of-matter, in either auditor's report.
6. **Going concern language**: NONE beyond the standard basis-of-preparation statement in both
   note sets (see above). No qualification, no material uncertainty disclosure.

No further pattern-level findings beyond what Pass 1 and Pass 2 already surfaced individually.
Proceeding to consolidation.

---

## LOAD-BEARING FACTS — WHAT THE NOTES SHOW (per companies/CAPILLARY.md Spear line)

**LBF1 (Guidance decomposition — organic vs. SessionM)**: The FY26 AR predates SessionM's
completion (1-May-2026, five days after AR sign-off) and cannot speak to SessionM's PPA,
goodwill, or the "profitable within two months" claim — those remain PENDING LIVE
VERIFICATION against the FY27 filings. What the notes DO establish is the template the SessionM
PPA will likely follow: the Kognitiv acquisition (1-May-2025, CAD 23.44mn/₹1,447.43mn) allocated
62% of consideration to goodwill (₹909.53mn, attributed to "assembled workforce and estimated
synergies") against only ₹390.37mn customer relationships and ₹172.43mn IP (Note 39, p.254).
The ₹249.60mn Churn Indemnity exceptional income (49% of consolidated PBT) is now confirmed
(via MD&A cross-reference, Pass 2 A3) as relating to Kognitiv, not a new/unnamed deal — a clean
one-off that must be stripped from any FY26 run-rate read feeding into the FY27 guidance bridge.

**LBF2 (Governance and earnings quality)**: The FY26 AR's audit sign-off (6-May-2026) predates
the Czech step-down subsidiary cyber fraud (Reg 30, 6-Jul-2026) and the CTIPL/Peak XV stake sale
(10-Aug-2026); neither appears in this AR (correctly — both are FY27 events) and both remain
PENDING LIVE VERIFICATION. What the notes DO show, directly relevant to the same governance
question: the auditor's IFC report carries two named exceptions — books-of-account backup not
held on India-located servers daily, and inability to confirm database-level audit-trail (edit-log)
integrity at a third-party accounting-software host (Auditor's Report, Annexure II, p.184-185,
188) — despite an overall unmodified IFC opinion. FY26 other income (₹39mn per company memory)
decomposes in the notes to FY25-only corporate-deposit interest income (₹25.18mn, wound down
before FY26) plus treasury income on IPO-proceeds fixed deposits building through the year (Note
21/23); a full FY26 other-income bridge could not be reconstructed to a single ₹39mn figure from
the extracted notes and remains a residual gap for the Q4 FY26 concentration point in LBF2(b).

**LBF3 (Concentration and retention)**: The notes do NOT deliver a usable FY26 top-10/customer
concentration number. The one line that should carry it, Note 36(iii) (consolidated, p.246-247,
"Revenue from one customer... that individually accounted for more than 10% of the total
revenue"), is grammatically incomplete in the filed AR — no name, amount, or "Nil" follows
(confirmed genuine drafting defect, Pass 2 A2, not an extraction loss). The only concentration data
the notes do supply is geographic: USA 55.6%, UK 15.4%, Others 29.0% of consolidated revenue
(Note 22, p.232-233). The standalone entity's "concentration" is structural rather than customer-based:
75.7% of standalone revenue is intercompany (Capillary Pte Ltd, Singapore hub). No NRR, churn, or
FY26 top-10 percentage is disclosed anywhere in the notes; this load-bearing fact is unresolved by
this AR and needs a source outside the notes (MD&A/investor deck/concall).

**LBF4 (Cash conversion)**: The notes resolve most of this LBF at the consolidated level. Trade
receivables grew 12.2% against 22.8% revenue growth (favourable decoupling); credit-impaired
receivables fell 65.3%; unbilled revenue fell slightly (Note 8, p.222-223) — consistent with the
memory's CFO recovery from -₹46 Cr (FY25) to ~₹150 Cr (FY26). The standalone-only picture is the
opposite (unbilled revenue +126.5%) but is confirmed intercompany and nets out on consolidation
(Note 8, p.146 vs p.222). Capitalised internally generated software (₹366.15mn, ~34% of
consolidated EBITDA, 3-year amortisation) is the fixed-assets-growth driver the memory flags
(₹301 Cr → ₹460 Cr); it is a named Key Audit Matter (auditor's report, p.178-179) and the single
largest judgement behind the cash-conversion-vs-reported-earnings gap. IPO-proceeds cash
(₹3,232.40mn in fixed deposits) sits outside the Capital Management note's "Total Fund"
definition (Pass 2, B2) — a disclosure-clarity point, not a conversion-quality one. Debtor days:
standalone trade receivable turnover fell from 3.97x to 3.49x (Note 36, p.175), consistent with
lengthening (not shortening) collection at the standalone level, though this is the intercompany-
dominated book.

---

## A. TOP 15 MOST SIGNIFICANT FINDINGS (all three passes combined)

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Standalone revenue 75.7% related-party (Singapore hub); RP receivables 80.6%, RP payables 81.1% of totals; FY26 transfer-pricing study still "in process" at report date. | Note 20/32 (standalone), p.155-156, 166-168 | 🟡 | Standalone entity's P&L is structurally an internal transfer-pricing construct, not third-party economics; arm's-length not yet independently certified for the year. |
| 2 | ₹249.60mn one-time Churn Indemnity income (Kognitiv-related, confirmed via MD&A) = 49% of consolidated PBT. | Note 28 (consolidated), p.235; MD&A p.82 | 🟡 | Must be stripped for any run-rate/FY27 bridge read (LBF1). |
| 3 | Group profit concentration: Capillary Technologies LLC (US) contributed 104.9% of consolidated profit, requiring a -45.6% elimination adjustment. | Note 40, p.274 | 🟡 | Single-entity dependency inside the consolidated number; India standalone entity is near-breakeven. |
| 4 | Goodwill ₹3,095.76mn (24% of consolidated assets) tested at 27.70% WACC, no disclosed sensitivity headroom; CGU structure changed 1→2 this year. Key Audit Matter. | Note 4, p.219-220; KAM p.180-181 | 🟡 | High discount rate leaves thin headroom; methodology change needs consistency tracking. |
| 5 | Standalone profitability ratios (ROE, NPR, RoCE, RoI) all fell sharply YoY post-IPO equity infusion, with an internally contradictory footnote ("decrease in losses") attached to worsening rows. | Note 36, p.174-176 | 🟡 | Pattern-pass contradiction; mechanical (equity base doubled) but the note's own drafting is wrong on its face. |
| 6 | Auditor's IFC report: books-of-account backup not held on India servers daily; unable to confirm database-level audit-trail integrity at third-party host. Overall IFC opinion unmodified. | Auditor's Report Annexure II, p.184-185, 188 | 🟡 | Named control gap in the exact area (audit trail/edit-log) under active SEBI/MCA scrutiny since FY24; feeds LBF2 governance question. |
| 7 | Contingent liabilities note (both entity levels) promises a description of claims and supplies none — confirmed genuine drafting gap, not extraction loss. | Note 31 (standalone) p.166; Note 34 (consolidated) p.244 | 🟡 | Either genuinely NIL contingent items or an omitted schedule; a management query item, not assumable as fact for valuation. |
| 8 | Major-customer >10% disclosure (Note 36(iii)) is a grammatically incomplete sentence — no name/amount/Nil. Confirms LBF3 cannot be resolved from the notes. | Note 36(iii), p.246-247 | 🟡 | Ind AS 108 disclosure requirement not actually discharged in the filed AR; concentration data must come from elsewhere. |
| 9 | Internally generated software capitalisation ₹366.15mn (~34% of consolidated EBITDA), 3-year amortisation, judgement-heavy. Named Key Audit Matter. | Note 4/2.3(f), p.131-132, 219; KAM p.178-179 | 🟡 | Largest driver of fixed-asset growth (LBF4); high capitalisation-to-earnings ratio. |
| 10 | Standalone unbilled revenue +126.5% (₹283.36mn→₹641.83mn) vs 21.7% revenue growth — intercompany, reverses at consolidated level (unbilled revenue fell). | Note 8, p.146 vs p.222 | 🟡 | Confirms standalone-only WC stress is a timing/intercompany artifact, not a group-level cash-conversion problem. |
| 11 | Fair value hierarchy shows zero forward-contract balance despite a stated hedging policy across a 12-currency exposure table. | Note 34(2), p.172-173 | 🟡 | Confirmed gap (not a read error): policy dormant or disclosure incomplete; do not assume active FX hedging in place. |
| 12 | Capital Management note's "Total Fund" (liquidity) definition excludes ₹3,232.40mn of fixed deposits held on the same balance sheet, understating true liquid position by ~₹3.2bn. | Note 35 (standalone) p.173-174; Note 38 (consolidated) p.253 | 🟡 | Disclosure-clarity issue only (understates strength); relevant to reading the group's true net-cash position post-IPO. |
| 13 | Kognitiv Solutions Inc. acquired for CAD 23.44mn; goodwill ₹909.53mn = 62% of consideration, allocated mainly to "assembled workforce and synergies." | Note 39, p.254 | 🟡 | Template/comp for how the SessionM PPA (LBF1) is likely to allocate; high goodwill-to-consideration ratio. |
| 14 | Capital commitments: no dedicated note found anywhere despite ₹979.85mn earmarked for "inorganic growth" from IPO proceeds and the SessionM deal signed 3 months post year-end. | Full-document search; no note anchor | 🟡 | Genuine disclosure gap for a company that just raised and is actively deploying IPO capital. |
| 15 | SessionM Inc. + Czech step-down subsidiary acquisition (USD 20.00mn), signed 24-Feb-2026, completed 1-May-2026 — confirms B00/LBF1 context; not in any FY26 figure. | Note 44 (consolidated), p.259 | 🟢/informational | Directly load-bearing for LBF1; PPA, financing source and integration plan remain PENDING LIVE VERIFICATION. |

## B. ACCOUNTING QUALITY SCORE (1-10)

| Dimension | Score | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Standard Ind AS 115 five-step model, ECL matrix unremarkable; the LRD/guaranteed-profitability standalone construct (Note 2.3(c)(iv)) and the unlabelled RPO-vs-full-backlog gap are the deductions. |
| Expense capitalisation honesty | 5 | Capitalisation itself follows Ind AS 38 criteria as recited, but the scale (₹366.15mn, ~34% of consolidated EBITDA) against a fast 3-year amortisation life and no bright-line technical-feasibility test is the single most judgement-heavy item in the filing, flagged by the auditors themselves as a KAM. |
| Provisioning adequacy | 7 | Gratuity assumptions standard with sensitivity disclosed; no warranty/decommissioning/onerous items (none applicable); the empty contingent-liability table (should this represent an omitted schedule rather than a genuine NIL) is the main deduction. |
| RPT fairness | 6 | Fully disclosed by name and amount with no non-arm's-length signal evidenced, but 75.7% of standalone revenue is intercompany and the transfer-pricing study for the year was still "in process" at sign-off — arm's-length is asserted, not yet independently certified. |
| Disclosure transparency | 5 | A consistent pattern (Pass 3 finding 3) of leaving exactly the risk-quantifying line incomplete across four separate notes: contingent liabilities, major-customer concentration, capital commitments, and forward-contract notional/MTM. None individually alarming; the pattern across a maiden post-listing AR is a real deduction. |
| Consistency with prior years | 7 | No genuine restatement found (the "restated" P&L label is a cosmetic IPO-template carryover, not a substantive restatement); CGU structure change (1→2) and the ratio-analysis footnote contradiction are the deductions. |
| **OVERALL** | **6** | A first-year-listed company with generally standard Ind AS mechanics and no evidence of earnings manipulation, held down by one high-judgement capitalisation policy (a named KAM) and a repeating pattern of incomplete risk-quantifying disclosures that a more mature filer would have closed out. |

## C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Capitalised software (₹366.15mn, KAM) overstates earnings if technical-feasibility judgement proves optimistic | Medium | Capitalisation-to-EBITDA ratio trend; any future write-off/impairment of capitalised software | Next AR (FY27) or an interim quarter if a product line is discontinued |
| Goodwill (₹3,095.76mn, 24% of consolidated assets) tested at 27.70% WACC with no disclosed sensitivity headroom | Medium | Any softening of the 4-10% growth / 4% terminal-growth assumptions; CGU-level performance of "Kognitiv" vs "US region" | FY27 impairment test, or sooner if Kognitiv/US organic growth disappoints |
| Transfer-pricing study for FY26 RPTs incomplete at sign-off, against a 75.7% RP-revenue standalone base | Medium | Completion and outcome of the TP study; any adjustment required | Whenever the FY26 TP study is finalised (timing not disclosed) |
| Auditor IFC exceptions on books-of-account backup location and audit-trail/edit-log verification | Low-Medium | Remediation status in the FY27 auditor's report; whether the exception recurs or is closed | FY27 AR sign-off |
| Contingent liabilities and major-customer concentration undisclosed/incomplete in the notes | Low (as filed) / unknown (if real gap) | Direct management query; cross-check against any BSE/NSE disclosures for either item | Ongoing; resolve before treating either as NIL in valuation |
| No forward-contract hedge book despite multi-currency exposure and a stated hedging policy | Low-Medium | USD/GBP/CAD movements against unhedged receivables/payables; any future hedge-book disclosure | Each quarter with meaningful FX-rate movement |

## D. FIVE QUESTIONS FOR MANAGEMENT

1. The contingent liabilities note (Note 31 standalone / Note 34 consolidated) promises a
   description of claims and lists none — is this a genuine NIL position, or was a schedule
   omitted from the filed AR, and if NIL, why does the note's own sentence structure promise a
   list?
2. Note 36(iii) states a >10% single-customer revenue disclosure requirement but the sentence has
   no name, amount, or "Nil" — what is the actual FY26 top-customer and top-10 concentration
   percentage, and does it differ meaningfully from the FY25 UDRHP figure of 58.71%?
3. The standalone policy note states the Company holds forward contracts to hedge FX exposure,
   but no forward notional, fair value, or hedge-effectiveness disclosure appears in either fair
   value hierarchy table — is the hedging programme currently active, and if so, why is it absent
   from the financial instruments note?
4. Was the FY26 transfer-pricing study (Note 37 standalone / Note 41 consolidated, "in process" at
   report date) completed by the time of this query, and did it result in any adjustment to the
   Capillary Pte Ltd service-income pricing?
5. The Kognitiv goodwill allocation (₹909.53mn, 62% of consideration, attributed to "assembled
   workforce and estimated synergies") sets a template — is the SessionM purchase price
   allocation expected to follow a similar goodwill-heavy split, and what is the expected
   intangible/goodwill mix once that PPA is finalised?

## E. NOTES-BASED RED FLAGS

No red flags (🔴) were identified across all three passes. The findings above are consistently
rated 🟡 Watch: a high-judgement capitalisation policy, a repeating pattern of incomplete
risk-quantifying disclosures, one internally contradictory footnote, and a structural
related-party revenue base at the standalone level. None shows a hallmark of deliberate earnings
management (no unusual revenue timing shifts inconsistent with cash, no undisclosed related-party
loans, no reserve-bypass entries beyond standard Ind AS treatments, no restated prior-year
figures). The concentration of items in "disclosure completeness" rather than "number
manipulation" is itself the pattern worth carrying forward.

## F. ONE-LINE NOTES VERDICT

The notes reveal moderate accounting practices, clean on RPT and reserve treatment but weak on
disclosure completeness. Key concern: a named-KAM software capitalisation charge (~34% of
consolidated EBITDA) sitting alongside a repeated pattern of unquantified risk disclosures
(contingent liabilities, customer concentration, capital commitments, FX hedge notional). Key
strength: consolidated receivables and ageing quality genuinely improved YoY, and the group
de-levered ₹1,000.94mn→₹447.21mn using IPO proceeds with no covenant issues. Overall accounting
quality: 6/10.

---
*End of consolidated Notes analysis (Stage 2, all three passes).*
