# STAGE 5: CONCALL ANALYSIS — KABRAEXTRU — NO-CONCALL MODE — REWORK RERUN

**Company:** Kabra Extrusiontechnik Ltd (KABRAEXTRU) | **Run date of record:** 2026-09-05 | **Rerun ordered:** 2026-09-09 | **Rerun #2**

**WHY THIS RERUN.** Run 1 (preserved at `outputs/reports/05-concall-run1.md`) was audited by an independent fresh
read of both annual reports (`outputs/final/run1/gate-recommendation.md`). The audit found 1 CRITICAL, 10 MAJOR
and 11 MINOR items against Stage 5, driving red-flag coverage to 23.0%, below the 60% floor, and forcing a
pipeline-wide REWORK verdict. This rerun re-derives every figure below directly from the two annual reports, with a
verbatim quote or table extract and a filename + PDF page anchor for each. Quote-then-comment. NOT DISCLOSED where
the corpus is silent. Nothing here is estimated.

**MODE NOTICE (unchanged from run 1):** No earnings-call transcripts exist for this company
(`concalls_available: false`). This report follows the NO-CONCALL DEGRADED PROCEDURE in
`prompts/05-concall-pipeline.md`. Sections that require live analyst Q&A (2E, 3C) have no source and say so.
The promise-vs-delivery tracker (2A) runs AR-FY25-guidance vs AR-FY26-delivery. PDF page numbers below are the
"PAGE n" markers in the page-marked text twins; printed report page numbers are given in parentheses where useful.

Sources re-read for this rerun: `inputs/annual-report/Annual_Report_2025.txt` (168pp, FY2024-25),
`inputs/annual-report/Annual_Report_2026.txt` (170pp, FY2025-26). The Dec-2023 investor deck and screener CSV are
carried forward from run 1 unchanged (not implicated in the audit's fix list for Stage 5).

---

## SECTION 1: GROWTH TRIGGERS & DRIVERS

### 1A. Every growth trigger / catalyst / driver named, by document

| Trigger | Type | Classification | Timeframe | Confidence | Specificity | Source |
|---|---|---|---|---|---|---|
| Extrusion: enhance film plants for greater output/width, high-demand applications | Both | VOLUME/COST | Medium | Planned | Low, no number/date | AR FY25 p.38, Business Outlook |
| Extrusion: benefit from JJM 2.0 / infra capex revival | Revenue | REGULATORY-POLICY/SECTORAL | Near-medium | Aspirational | Low | AR FY26 p.38, Business Outlook |
| Geon: E-3W and Battery Swapping entry | Revenue | VOLUME | Near | Committed (claimed done FY25) | Medium | AR FY25 p.5, p.38 |
| Geon: E-LCV, E-4W entry "in the upcoming fiscal year" (FY26) | Revenue | VOLUME | Near (FY26) | Planned | Low, no number | AR FY25 p.36/38 |
| Geon: BESS build-out | Revenue | SECTORAL | Medium-long | Aspirational | Low | AR FY25 p.38; AR FY26 p.36/38 |
| Geon: lithium-ion inverter battery / D2C entry | Revenue | VOLUME/SECTORAL | Near (entered FY26) | Committed (claimed delivered) | Medium | AR FY26 p.5 |
| Geon: ~Rs 150 Cr order "secured for execution in the upcoming year" (FY27) | Revenue | VOLUME | Near (FY27) | Committed | Low, no counterparty/terms/Reg-30 in corpus | AR FY26 p.37, Key Strength 8 |
| Geon: facility can generate Rs 1,500+ Cr revenue "at optimal levels" | Revenue | VOLUME | Long, undated | Aspirational | Low, no utilisation rate given | AR FY26 p.37 |
| Geon: "moving towards profitability as volumes scale up" | Margin | COST/VOLUME | Medium, undated | Aspirational | Very low | AR FY26 p.38 |
| Extrusion: "~40% market share" | positioning | — | — | Stated as fact, then dropped | Was specific; absent AR FY26 | AR FY25 p.37 |
| Global plastic pipes / CPVC market growth | Revenue | SECTORAL/REGULATORY | Long | Aspirational (macro) | Medium, but figures move 2.7x between reports (see 3B) | AR FY25 p.4-5, p.35; AR FY26 p.33 |
| Indian EV / EV battery-pack market growth | Revenue | SECTORAL | Long | Aspirational (macro) | Medium, internally inconsistent (see 3B) | AR FY25 p.4-5; AR FY26 p.34 |

Cross-test added this rerun: the ~7 GWh Chakan capacity claim (AR FY26 p.36, p.37), the ~Rs 150 Cr FY27 order (p.37)
and the Rs 1,500+ Cr "optimal level" ceiling (p.37) do not reconcile with each other or with delivered revenue.
Battery Division revenue was Rs 13,610.84 lakh (Rs 136.11 Cr) in FY26 (Note 38 standalone, AR FY26 p.105). Even if
the ~Rs 150 Cr order lands in full in FY27, segment revenue would reach roughly Rs 286 Cr, about 19% of the claimed
Rs 1,500+ Cr ceiling, with no utilisation-rate disclosure given to test the gap (illustrative arithmetic, not a
filed figure). Separately, AR FY26's own Mordor Intelligence citation puts the entire India EV battery-pack market
at USD 53.76 million for 2026 (AR FY26 p.34). Geon's FY26 segment revenue of Rs 136.11 Cr converts to roughly
USD 16-16.5 million at a representative FY26 average rate (illustrative, rate not in corpus), which would imply
Geon alone holds close to 30% of the entire market Mordor describes for the same year, a share the company never
claims anywhere in AR FY26. Either the Mordor market-size citation is too narrow, or the market-share implication is
not credible; the AR does not resolve which. **Flagged for peer verification.**

### 1B. Quantified guidance

| Item | Number | Timeframe | Stated in |
|---|---|---|---|
| Geon new-segment entry (E-LCV, E-4W) | not quantified | "upcoming fiscal year" (FY26) | AR FY25 p.36/38 |
| Geon secured order | ~Rs 150 Crore | execution "upcoming year" (FY27) | AR FY26 p.37 |
| Geon facility revenue ceiling | Rs 1,500+ Crore "at optimal levels" | Undated | AR FY26 p.37 |
| Geon installed capacity | ~7 GWh, ~USD 30mn (~Rs 250 Cr) invested to date | As of FY26 | AR FY26 p.36 |
| Capital commitment (contracted, not executed) | Rs 3,177.38 lakh, up from Rs 143.42 lakh FY25 (22.2x) | Next FY | AR FY26 Note 41(b), p.110 |
| FY25 dividend | Rs 2.50/share (50% of face value) | Declared FY25 | AR FY25 p.19 |
| FY26 dividend | Nil, "Board of Directors has not recommended any dividend" | FY26 | **AR FY26 p.17** (run 1 mis-cited p.18; corrected) |
| Extrusion market share (positioning) | ~40% "as on FY25" | AR FY25 | AR FY25 p.37 |
| R&D spend, Extrusion | Rs 1,116.62 lakh (FY25, per AR FY25) -> Rs 367 lakh (FY26) | Actuals | AR FY25 p.30; **AR FY26 p.28** (run 1 mis-cited p.29 for the "accelerated its R&D" sentence; corrected) |
| R&D spend, Geon | Rs 866.78 lakh (FY25) -> Rs 185.18 lakh (FY26) | Actuals | AR FY25 p.31; AR FY26 p.29 |

### 1C. Trigger evolution, Dec-2023 deck (T0) -> AR FY25 (T1) -> AR FY26 (T2)

Unchanged in substance from run 1 (~40% share dropped; ~18% Battrixx share dropped; ARAI/IATF claims dropped;
E-3W slipped ~1 year then delivered; E-4W/E-LCV timeline slipped and goalposts moved; R&D headcount claim repeated
even as rupee R&D spend collapsed; Geon "profitability" claim is new at T2 and unquantified; extrusion machinery
CAGR estimate moved from 3.9% to 6.7% between consecutive ARs; India EV battery-pack market citation swings sharply
between ARs). One entry corrected this rerun and one entry added:

- **CORRECTED:** run 1 stated the AR FY25 extrusion-machinery CAGR (3.9%) carried "no source house named." It does:
  AR FY25 names "Plastic Extrusion Machines Market Size & Share 2024-2032 (imarcgroup.com), Plastic Extrusion
  Machine Market Size, Demand, Trends - 2032 (futuremarketinsights.com)" (AR FY25 p.34). AR FY26's 6.7% figure is
  sourced instead to "Research and Markets - Plastic Extrusion Machinery Market - Global Forecast 2026-2032"
  (AR FY26 p.33), a third, different source house. The CAGR still nearly doubled between reports with the source
  house switched each year and no reconciliation offered; the finding stands, the "no source" framing was wrong.
- **NEW: heritage claim shrinks, then the chairman's letter contradicts the shrink.** AR FY25: "With over six
  decades of industry experience, a track record of more than 15,000 successful installations" (AR FY25 p.36). AR
  FY26 MD&A: "With a legacy of over four decades" (AR FY26 p.35), installation count dropped entirely. The same
  AR FY26's chairman's letter calls the same year "its 60-year journey" (AR FY26 p.5). Two claims about the same
  company's age, six decades and four decades, sit inside the same annual report.
- **NEW: revenue down three years running from the deck's own FY23 base.** Deck (Q3 FY24, 25-Jan-2024): FY23
  consolidated revenue Rs 6,700 million = Rs 670 Cr (deck p.7). AR FY25 p.37: FY24 revenue Rs 608 Cr, FY25 Rs 477
  Cr. AR FY26 p.37: FY25 Rs 477 Cr, FY26 Rs 451 Cr. Three consecutive years of decline (670 -> 608 -> 477 -> 451),
  against a "long-term growth trajectory" outlook repeated in both ARs' Business Outlook sections.
- **NEW: the Kabra Mecanor / Extron Mecanor technical-collaboration table is present in AR FY25 (p.37) listing two
  partners; Penta Auto Feeding India Ltd (the JV pillar, 49.94% holding per AOC-1, AR FY25 p.25) ceased as an
  associate 6-Feb-2025 on sale of the entire stake and is absent from the AR FY26 collaboration language with no
  narrative comment on its exit, despite the Dec-2023 deck describing it as a "50:50" JV (deck p.24) against the
  49.94% actually held per both years' AOC-1.**

---

## SECTION 2: MANAGEMENT CREDIBILITY CHECK

### 2A. Promise vs delivery tracker (AR FY25 guidance -> AR FY26 delivery)

| # | Promised in AR FY25 | Outcome per AR FY26 | Verdict | Explanation given |
|---|---|---|---|---|
| 1 | Geon to pursue E-LCV and E-4W "in the upcoming fiscal year" (p.36/38) | Not confirmed by name in AR FY26; RESS, inverter D2C and e-bus high-voltage packs substituted instead (p.28, p.34, p.36-37) | Partial | None; the FY26-dated targets are simply not mentioned again |
| 2 | "~40% market share" in extrusion machinery maintained (p.37) | Claim dropped entirely (no "40%" anywhere in AR FY26); extrusion segment revenue fell 13.2% (Rs 314.89 Cr vs Rs 362.85 Cr) and segment result fell 27.6% (Rs 50.75 Cr vs Rs 70.14 Cr, Note 38, p.105) | Missed | None |
| 3 | Implicit: "well-positioned to capitalize on anticipated growth" (p.37) | Revenue -5.45%, EBITDA -74.88%, PAT swung to a standalone net loss of Rs (2.44) Cr from Rs 34 Cr profit (MD&A table, p.37); the standalone **pre-tax** loss driving that figure was Rs (423.21) lakh (Directors' Report, p.17), and Rs 1,668.41 lakh of Other Income inside that pre-tax number is an unexplained catch-all line, up from Rs 22.91 lakh a year earlier (Note 23, p.95) | Missed | Extrusion weakness blamed on JJM disbursement delays, state infra spending delays and export geopolitical/currency weakness (p.36). No line anywhere explains what the Rs 1,668.41 lakh "Other" income item is, despite it being large enough to materially change the size of the reported loss |
| 4 | Geon "aims to be a key player in the BESS arena" (p.38) | RESS/BESS/D2C products launched (real product progress, p.28, p.36-37), but Battery Division segment loss widened to Rs (4,334.64) lakh from Rs (2,553.28) lakh (+69.8%) even as segment revenue grew 7.2% (Note 38, p.105) | Partial (narrative progress, financial delivery negative) | None; "moving towards profitability" (p.38) is not reconciled against this same document's own segment loss |
| 5 | Continued R&D investment, both divisions (p.30-31, p.36-37) | R&D spend cut 67.1% (Extrusion, Rs 1,116.62 lakh -> Rs 367 lakh) and 78.6% (Geon, Rs 866.78 lakh -> Rs 185.18 lakh), while the AR FY26 narrative states Geon "has accelerated its R&D" (**AR FY26 p.28**, corrected from run 1's p.29) | Missed / contradicted | None |

**Tally unchanged: delivered = 0, partial = 2, missed = 3.**

**New context this rerun on row 3, the base year itself.** The FY25 comparison base carries its own credibility
problem. AR FY25 reports three different FY25 PAT figures inside the same document: the Financial Performance
Snapshot table gives "PAT... 34" Cr at "PAT margin %... 7.2%" (AR FY25 p.38); the prose two lines below the same
table says "KET's PAT stood at ₹ 32 crores. PAT margin stood at 6.8% during FY25" (AR FY25 p.38); the chairman's
letter gives "PAT... stood at ₹33.9 crores, with a PAT margin of 7.2%" (AR FY25 p.4). None of the three is
reconciled to the others anywhere in the report. Separately, the FY25 Directors' Report financial table shows an
exceptional item of Rs 848.98 lakh, the Penta Auto Feeding divestment gain, feeding into FY25 profit before tax of
Rs 4,192.26 lakh standalone (AR FY25 p.19); Rs 848.98 lakh is about 20% of that pre-tax profit. The FY25 chairman's
letter reports PAT and margin without naming this exceptional item anywhere in the letter (AR FY25 p.4). The FY25
MD&A's own Key Financial Ratios table does at least flag it, crediting the 36.30% net-profit-margin variance to
"exceptional item" (AR FY25 p.38), so the fact was disclosed somewhere in the report; it was simply never carried
into the chairman's headline framing. Every subsequent year-on-year comparison in both ARs (including the FY26
snapshot table's "-107.21%" PAT change) is drawn against this base year without ever flagging that a fifth of FY25
profit was a one-off asset sale.

### 2B. Excuse pattern analysis

Only the extrusion revenue decline receives an explicit explanation, and it is entirely external-blame: JJM
fund-disbursement delays, state-government infra spending delays, export weakness from "geopolitical challenges and
currency volatility" (AR FY26 p.36). Every other miss or contradiction is met with silence:

- The Rs 1,668.41 lakh unexplained "Other" income line that determines the size of the reported loss (Note 23,
  p.95) — never named.
- The Battery Division's widening loss despite revenue growth (2A row 4) — never addressed.
- The R&D spend cut against an "accelerated R&D" claim (2A row 5) — never addressed.
- The dropped 40% market-share claim (2A row 2) — never addressed; the number stops appearing.
- Receivables ageing deterioration (48.9% of gross receivables over one year overdue, Note 9, p.88) against an MD&A
  that reports only a debtors-turnover *improvement* (+5.20%, p.37) — the improvement is a book-shrinkage artefact,
  not addressed as such.
- Varos Technology Pvt Ltd, a Key Strength in AR FY25 ("In FY22, KET fully acquired Varos Technology," p.37), with
  turnover down 95.2% (Rs 372.99 lakh FY25 -> Rs 17.84 lakh FY26) and a net worth that moved further negative
  (Share Capital + Reserves & Surplus: Rs (264.68) lakh FY25 -> Rs (556.17) lakh FY26, AOC-1, AR FY25 p.25 / AR FY26
  p.23) — Varos disappears from the AR FY26 Key Strengths list with no comment.
- The CRISIL two-step downgrade during FY26 (see 2D) — disclosed only in the mandatory Corporate Governance table
  with the generic reason "Basis performance reported for Quarter 3" (AR FY26 p.51).
- The HEVPL receivable note, still dated "As at March 31, 2025" inside the FY26 report (Note 9, p.87), with the
  underlying case status unrefreshed.
- The Interest Coverage Ratio and Return on Capital Employed lines in the MD&A Key Financial Ratios table, both
  past the mandatory 25% variance threshold, both with a blank "Reasons for Variation" cell (AR FY26 p.37) — see 2C.
- Item 12 of the Directors' Report ("no material changes... between the end of the year and date of this report,"
  AR FY26 p.20, signed 28-May-2026) sits nine business days after the 13-May-2026 CRISIL downgrade (AR FY26 p.51)
  with no cross-reference.

**Pattern check:** management never says "we made a mistake" in either report. The one acknowledged shortfall
(extrusion demand) is blamed entirely on externals. The one *volunteered* negative in the whole corpus is the
Secretarial Auditor's own exception, not management's: Form MR-3 records that "the Company has transferred the
shares pertaining to unpaid/unclaimed dividend for seven consecutive years for the financial year 2017-18 to the
[IEPF] Authority on October 31, 2025... beyond the timelines prescribed under Section 124" (AR FY26 p.24), echoed
in the Directors' Report itself (p.21). That single item is a compliance auditor's finding, not something management
raised on its own initiative in the chairman's letter or MD&A.

**Classification: external-blame-heavy, with a substantial and now larger silence component on company-specific
misses.**

### 2C. Tone ratings (1 = worst/highest concern, 5 = best/lowest concern for the first four rows; reversed for the
last two)

| Dimension | Rating | Evidence |
|---|---|---|
| Transparency | 1/5 (down from 2/5 in run 1) | CRISIL two-step downgrade never narrated (p.51). A Rs 1,668.41 lakh unexplained "Other" income line drives the reported loss size (p.95, p.17). Three different FY25 PAT figures inside one report (p.38 x2, p.4). Chairman's letter EBITDA Rs 10 Cr vs MD&A table Rs 13.05 Cr, same year, same document (p.4 vs p.37). Chairman's letter reports EBITDA but never PAT for FY26, and never uses the word "loss" anywhere in the letter (p.4-5), despite the standalone result being a loss |
| Specificity | 2/5 | "Moving towards profitability as volumes scale up" (p.38) carries no number or date. Rs 1,500+ Cr "at optimal levels" (p.37) carries no utilisation rate. No aggregate order-book figure is disclosed, only the single ~Rs 150 Cr order |
| Consistency | 1/5 (down from 2/5) | 40% market-share claim dropped without note. Extrusion CAGR estimate moved 3.9% -> 6.7% with the source house switched each year. India EV battery-pack market citation swings materially between years. India plastic-pipes market citation moves ~2.7x between years with the source switched to IMARC (see 3B, corrected this rerun). Heritage claim shrinks from "six decades" to "four decades" in the same year the chairman calls it a "60-year journey." Inventory-turnover "Reasons for Variation" text is copied verbatim from FY25 to FY26 even though the underlying direction of inventory reversed (see 4D) |
| Accountability | 1/5 (down from 2/5) | No instance of "we made a mistake" in either report. The Interest Coverage Ratio and ROCE lines in the MD&A ratio table are the two clearest candidates for a "Reasons for Variation" entry (both past the mandatory 25% threshold) and both are left blank (p.37), even though the company's own mandatory Note 43 ratio disclosure gives a reason for the equivalent ROCE move the same year ("Due to generate negative profit after tax," Note 43(j), p.112) |
| Defensiveness (no live Q&A; proxy only) | 3/5 | Cannot be scored directly without transcripts. Risk sections in both ARs frame competitive and import pressure only in generic, unfalsifiable terms; neither year's Risks and Challenges section names customer or customer-credit risk at all, despite an insolvent customer (HEVPL) and a receivables book that is 48.9% over one year overdue (AR FY26 p.38) |
| Over-promotion | 4/5 (high concern, unchanged) | Chairman's letter calls FY26 "a transitional year" in the same letter that omits PAT and the word "loss" entirely (p.4-5). Key Strengths language ("Strong Order Visibility," "well-positioned," "confident of creating long term sustainable value") is maintained at the same register as FY25 despite the results |

**One MD&A figure traced to a probable source-note mislabel, new this rerun.** The MD&A Key Financial Ratios table
reports "Interest Coverage Ratio... 39.20%" with no reason given (AR FY26 p.37). EBIT was Rs 7.16 Cr and finance
cost was Rs 1,139.25 lakh (Rs 11.3925 Cr) in FY26 (p.37, p.17); FY25 EBIT was Rs 45 Cr against finance cost Rs
1,117.31 lakh (Rs 11.1731 Cr, AR FY25 p.19). On these figures, interest coverage fell from roughly 4.03x (FY25) to
roughly 0.63x (FY26), a decline of about 84%, not a rise of 39.20%. The mandatory Note 43 ratio disclosure in the
same annual report shows a **Debt Service Coverage Ratio** of 14.36x (FY26) against 10.32x (FY25), a variance of
"39.2%," with the reason "Due to generate lower net operating income" (Note 43(c), AR FY26 p.112). The MD&A's
"Interest Coverage Ratio... 39.20%" figure matches the Note 43 Debt Service Coverage Ratio variance number, not any
interest-coverage calculation the same report's own EBIT and finance-cost lines support. This reads as a mislabelled
or miscopied cell, not merely an unreconciled one; it is presented here as an anchored observation, not a
certainty, because no corrigendum or restatement is in the corpus.

### 2D. What they are NOT saying

Everything from run 1 stands (CRISIL downgrade undiscussed in the chairman's letter/MD&A; R&D spend cut never
mentioned; battery segment negative operating leverage never reconciled; senior-management churn disclosed only in
mandatory tables; the stale HEVPL note; no order-book total). This rerun adds:

- **The Rs 1,668.41 lakh "Other" income line, and what it is.** Note 23 shows "Other... 1,668.41" for FY26 against
  "22.91" for FY25, out of total other income of Rs 2,367.55 lakh FY26 (AR FY26 p.95). No line-item breakdown, no
  sentence anywhere in the chairman's letter, Directors' Report or MD&A names or explains this item, even though it
  is large enough (about 4x the standalone pre-tax loss of Rs 423.21 lakh) to materially affect whether FY26 was a
  narrow loss or something larger. **NOT DISCLOSED what this line comprises.**
- **The receivables ageing profile, as distinct from the turnover ratio.** Of Rs 9,052.43 lakh gross trade
  receivables at FY26 close, Rs 4,428.68 lakh (48.9%) is more than one year overdue, and Rs 1,935.36 lakh is more
  than three years overdue, carrying only a 23.5% provision (Rs 455.13 lakh / Rs 1,935.36 lakh; Note 9, p.87-88).
  The MD&A instead reports a **debtors-turnover improvement** of +5.20% (p.37); a turnover ratio improves
  mechanically when the receivables base shrinks (it fell from Rs 9,893.76 lakh to Rs 9,052.43 lakh, largely on the
  HEVPL provision), so the improving ratio and the worsening ageing profile both come from the same underlying
  event, and only the favourable framing is carried into the MD&A.
- **Varos Technology Pvt Ltd's collapse and quiet removal from the Key Strengths narrative.** AR FY25 names Varos
  as a diversification strength: "In FY22, KET fully acquired Varos Technology, a Pune-based company specializing
  in... battery management systems... cloud-powered AI analytics" (AR FY25 p.37, Key Strength 5). Varos's own
  AOC-1 disclosure shows turnover falling from Rs 372.99 lakh (FY25) to Rs 17.84 lakh (FY26), a 95.2% decline, with
  net worth (Share Capital + Reserves & Surplus) at Rs (556.17) lakh FY26 versus Rs (264.68) lakh FY25 (AOC-1, AR
  FY25 p.25 / AR FY26 p.23). AR FY26's Key Strengths list no longer mentions Varos at all (AR FY26 p.36-37).
- **The "Technology-Agnostic and Asset-Light Approach in Energy Business" Key Strength, against the balance sheet.**
  AR FY26 Key Strength 5 states GEON "follows a technology-agnostic approach... reduces technology risk, and
  enhances the ability to adopt evolving battery chemistries without heavy capital investments in cell
  manufacturing" (AR FY26 p.36). The Battery Division's own segment assets were Rs 36,437.25 lakh at FY26 close,
  50.1% of total segment assets (Rs 72,775.30 lakh), on segment revenue of Rs 13,610.84 lakh, an asset turn of
  0.37x, and a segment loss of Rs 4,334.64 lakh (Note 38, AR FY26 p.105-106). A division holding half the company's
  segment assets while turning them over at 0.37x and losing money is not naturally described as "asset-light";
  the claim and the balance sheet are never reconciled in the same document.
- **Item 12 of the Directors' Report and the CRISIL downgrade.** The Directors' Report, signed 28-May-2026, states
  under item 12 "Material changes and commitments affecting financial position between the end of the financial
  year and date of the report": "There are no material changes and commitments affecting the financial position of
  your Company, which have occurred between the end of the year and date of this report" (AR FY26 p.20). CRISIL's
  downgrade to A-/Stable (long term) and A2+ (short term) took effect 13-May-2026, "Basis performance reported for
  Quarter 3" (AR FY26 p.51), fifteen days before that statement was signed. The two are never cross-referenced.
- **Neither year's Risks and Challenges section names customer or customer-credit risk.** AR FY25 lists
  "technology becoming outdated," Covid-19, "geopolitical matters, trade wars, market volatility, intensifying
  competition, import pressures, and challenges from the unorganized sector" (AR FY25 p.38). AR FY26 lists cyclical
  extrusion demand, JJM/state infra delays, export volatility, GEON execution risk, and battery-component supply
  risk (AR FY26 p.38). Neither mentions counterparty credit risk, receivable concentration, or customer insolvency,
  despite HEVPL's CIRP and the receivables ageing profile above.
- **The Bagra re-designation, disclosed but not narratively flagged as a governance question.** Mr Bajrang Lal Bagra
  completed his second consecutive term as Independent Director on 26-Aug-2025 and was appointed Non-Executive
  Non-Independent Director nine days later, effective 11-Sep-2025 by postal ballot (AR FY26 p.18). He appears twice
  in the same Corporate Governance board table: once as "Non-Executive Non-Independent" (row 5) and once as
  "Non-Executive Independent" (row 6), both with 3 of the year's board meetings attended (AR FY26 p.39-40). This is
  compliant disclosure (also confirmed clean by the Secretarial Auditor, MR-3, AR FY26 p.25) but the double listing
  is never explained in the narrative sections of the report.

### 2E. Repeated question tracker

**NO SOURCE AVAILABLE.** Unchanged from run 1: no earnings calls, no analyst Q&A record exists in the corpus.

---

## SECTION 3: COMPETITIVE INTELLIGENCE (from AR industry commentary, in place of concalls)

### 3A. What management says about competitors

Unchanged from run 1. Neither AR names a specific competitor. Both years use generic language: "intensifying
competition, import pressures, and challenges from the unorganized sector" (AR FY25 p.38); "increasing competition
across both the extrusion and energy segments" (AR FY26 p.38). Unfalsifiable as written; routed to peer
verification.

### 3B. Industry and market intelligence dropped in the reports — **CORRECTED THIS RERUN**

- **Extrusion machinery market:** AR FY25 cites USD 6.9bn (2024) -> USD 10bn (2030), 3.9% CAGR, sourced to
  imarcgroup.com and futuremarketinsights.com (AR FY25 p.34). AR FY26 cites USD 7.74bn (2025) -> USD 8.24bn (2026)
  -> USD 12.22bn (2032), 6.72% CAGR, sourced to "Research and Markets" (AR FY26 p.33). The CAGR nearly doubled and
  the source house changed with no reconciliation. (Run 1's claim that AR FY25 gave "no source house" is corrected
  above in 1C; the substantive finding, an unreconciled near-doubling of the growth estimate, stands.)
- **India plastic pipes / CPVC market — RUN 1 CALLED THIS "INTERNALLY CONSISTENT." IT WAS WRONG.** AR FY25: "Valued
  at approximately ₹450 billion in 2024, the sector is projected to exceed ₹500 billion by FY2025, growing at a
  CAGR of 10.8%" (AR FY25 p.4-5, repeated p.35), no source house named for the India-specific figure. AR FY26: "The
  India plastic pipes market, valued at USD 2.10 billion in 2025, is projected to reach USD 3.65 billion by 2034,
  growing at a CAGR of 6.30%," sourced to "IMARC Group's report" (AR FY26 p.33). USD 2.10 billion converts to
  roughly Rs 185 billion at a representative FX rate (illustrative, rate not in corpus), against the Rs 500 billion
  AR FY25 claims for essentially the same India market and adjacent year, a difference of about 2.7x, with the
  source switched to IMARC and no reconciliation offered anywhere in either report. **Corrected verdict: the two
  citations are CONTRADICTORY, not consistent.**
- **Indian EV market size:** AR FY25 cites Fortune Business Insights, USD 23.38bn (2024) -> USD 117.78bn (2032),
  22.4% CAGR (p.4-5). AR FY26 cites Grand View Horizon, USD 20.2bn (2025) -> USD 178.2bn (2033), 29.4% CAGR (p.34).
  Different source houses, different base years; directionally bullish both years but not comparable figure to
  figure.
- **India EV battery-pack market size:** AR FY25 cites USD 2.22bn (2024) -> USD 13.89bn (2033), source unnamed
  (p.5). AR FY26 cites Mordor Intelligence, USD 39.39mn (2025) -> USD 53.76mn (2026) -> USD 254.59mn (2031), 36.5%
  CAGR (p.34). An approximately 100x discrepancy between the company's own two annual reports for what is nominally
  the same market, unexplained. **New this rerun:** the AR FY26 figure (USD 53.76mn total India market for 2026) is
  also small enough that Geon's own FY26 battery segment revenue (Rs 136.11 Cr, roughly USD 16-16.5mn at a
  representative rate) would represent close to 30% of the entire market Mordor describes, an implied share the
  company never claims. **Flagged for peer verification.**
- **EV sales data (FADA, both years):** internally consistent and independently checkable. FY25 total 19,64,975
  units, +16.9% YoY (AR FY25 p.36); FY26 total 24,52,014 units, +24.6% YoY (AR FY26 p.35), E-4 Wheelers the fastest
  growing segment at +83.6% YoY (AR FY26 p.35).

### 3C. Toughest analyst questions

**NO SOURCE AVAILABLE.** Unchanged from run 1.

### 3D. Customer and order book signals

Unchanged from run 1, restated with the FY26 figures re-verified against Note 38 (AR FY26 p.106): one customer
accounted for 19.11% of FY26 revenue, down from two customers at 26.94% in FY25. Export revenue fell to Rs 5,751.82
lakh (FY26) from Rs 6,507.94 lakh (FY25), -11.6%. Domestic revenue fell to Rs 39,191.86 lakh from Rs 41,022.11
lakh. No order-book total is disclosed in either MD&A; only the single ~Rs 150 Cr order is named (AR FY26 p.37),
with no counterparty, terms, or Reg-30 corroboration in the corpus.

---

## SECTION 4: KEY TAKEAWAYS & TRIGGERS SUMMARY

### 4A. Investment-ready trigger list, ranked by earnings impact

| Priority | Trigger | Type | Timeframe | Conviction | Confirms it | Kills it |
|---|---|---|---|---|---|---|
| 1 | ~Rs 150 Cr Geon order executes into FY27 revenue | Revenue | Near (FY27) | M | FY27 filing shows a battery-segment revenue step-up correlated with this order; counterparty/Reg 30 surfaces | FY27 battery revenue flat/down, order deferred, descoped or never corroborated; customer advances already fell 18.9% (screener data) in the year the order is described as secured |
| 2 | Battery segment reaches profitability | Margin | Medium, undated | L | Segment loss narrows materially or turns positive in FY27/FY28 filing | Segment loss stays above ~Rs 40 Cr or widens further; receivables ageing and the unexplained Other-income line both suggest the FY26 loss print may itself understate underlying cash weakness |
| 3 | Geon facility scales toward the claimed Rs 1,500+ Cr "optimal level" | Volume/capacity | Long, undated | L | Company discloses a utilisation rate and a stepped growth path | No utilisation disclosure ever given; battery revenue (Rs 136.11 Cr FY26) stays a small fraction of the claimed ceiling for multiple years, and the company's own India-market citation (Mordor, p.34) cannot obviously support it (see 1A, 3B) |
| 4 | Extrusion recovery on JJM 2.0 / state infra capex revival | Revenue | Near-medium | M | Extrusion segment revenue growth resumes | JJM 2.0 disbursement delays persist, the same cause the company names for FY26 and, per the deck's FY23 base, for three consecutive years of decline |
| 5 | Geon diversification into BESS/telecom/solar/inverter D2C | Revenue | Medium-long | L | Future filing discloses quantified non-mobility Geon revenue growing | No quantified non-mobility revenue disclosed after two further filing cycles |
| 6 | Credit rating stabilises (CRISIL A-/Stable after the two-step FY26 downgrade) | Cost of funding | Near | L-M | No further downgrade at next review | A further downgrade or return to "Negative" outlook |

### 4B. Questions for peer verification (formal handoff to Stage 6)

Questions 1-9 carried unchanged from run 1 (stage 6 is rerunning against them in parallel; not restated here to
avoid drift, see `05-concall-run1.md` Section 4B for full text). **Question 10 is new this rerun:**

10. **{question:** "What working-capital terms does Rajoo Engineers describe for extrusion machinery orders
    (advance on order finalisation, payment before dispatch, receivable days), and how does that compare with
    KABRAEXTRU's receivable profile (48.9% of gross receivables more than one year overdue, AR FY26 Note 9 p.88)?",
    **why:** "Tests whether KABRAEXTRU's receivables deterioration is a company-specific collection or credit
    problem, against a peer's stated order-economics discipline, and bears directly on how much of the reported
    FY26 loss and cash weakness is structural versus one-off (HEVPL).",
    **check_peers:** ["RAJOOENG"]**}**

### 4C. Management quality verdict table

| Criterion | Assessment |
|---|---|
| Delivery vs guidance (2A) | 0 delivered / 2 partial / 3 missed, on 5 testable promise-delivery pairs |
| Excuse pattern (2B) | External-blame-heavy on the one miss explained; total silence on every self-inflicted miss, now including the unexplained Other-income line, Varos, the asset-light/balance-sheet contradiction, and the item-12/CRISIL-date gap |
| Transparency (2C) | 1/5 (down from 2/5). Rating downgrade never narrated; three FY25 PAT figures inside one report; a Rs 1,668.41 lakh unexplained income line drives the reported loss size; chairman's letter drops PAT and the word "loss" entirely for FY26 |
| Consistency (2C, 1C) | 1/5 (down from 2/5). Market-share claim dropped; two industry-size citations swing materially (extrusion CAGR, EV battery-pack market); the India plastic-pipes citation swings ~2.7x (corrected this rerun); heritage claim shrinks from six decades to four in the same year the letter says "60-year journey"; the inventory-turnover explanation is copied verbatim across years despite the underlying direction reversing |
| Accountability (2C) | 1/5 (down from 2/5). No "we made a mistake" anywhere. Two ratio lines past the mandatory 25% variance threshold (Interest Coverage, ROCE) are left with blank Reasons for Variation in the MD&A table, while the company's own Note 43 gives a reason for the equivalent ROCE move the same year |
| Over-promotion (2C) | High concern (4/5, unchanged) |
| **Overall grade** | **D** |

**Grade BEFORE this rerun:** D (run 1; the independent audit concurred with D on the evidence run 1 did carry).

**Grade AFTER this rerun:** **D, unchanged, on a materially wider evidence base.** The no-concall degraded-mode
rule sets a default of C and allows a rise to B only on documented delivery evidence, never to A; it does not
address a floor below C. Run 1's analyst note read that silence as leaving room to grade below C on the evidence,
and this rerun concurs and goes further: this rerun adds five new HIGH/MEDIUM findings the pipeline caught
elsewhere but Stage 5 missed (the unexplained Rs 1,668.41 lakh Other-income line that determines the size of the
reported loss; the receivables-ageing profile behind a headline "improving" turnover ratio; Varos Technology's
collapse and quiet removal from the strengths narrative; the asset-light claim against a battery balance sheet that
is half the company's segment assets at 0.37x turn and a loss; and the corrected, now-contradictory plastic-pipes
market citation), plus four cross-stage management-communication defects re-derived independently here (three
different FY25 PAT figures; the FY25 exceptional gain never named in the chairman's letter; the MD&A Interest
Coverage Ratio figure that traces to a probable mislabelled Debt Service Coverage Ratio cell; the silent Rs 421.14
lakh FY25 comparative reclassification between employee benefits and other expenses, standalone Note 47, AR FY26
p.113, disclosed only as boilerplate regrouping language). None of this moves the grade toward B; all of it
reinforces D. D is the floor of the A-D scale used by this framework; there is no lower letter grade to assign.

### 4D. Red flags

| Flag | Severity | Evidence |
|---|---|---|
| Unexplained "Other" income line of Rs 1,668.41 lakh determines the size of the reported FY26 loss | **HIGH, NEW** | Note 23, AR FY26 p.95 (vs Rs 22.91 lakh FY25); standalone pre-tax loss Rs (423.21) lakh, Directors' Report p.17 |
| Receivables ageing crisis behind a headline "improving" turnover ratio | **HIGH, NEW** | 48.9% of gross receivables (Rs 4,428.68 / Rs 9,052.43 lakh) over one year overdue; Rs 1,935.36 lakh over three years at 23.5% provision cover (Note 9, AR FY26 p.87-88); MD&A reports only a +5.20% debtors-turnover "improvement" (p.37) |
| Varos Technology Pvt Ltd: negative and worsening net worth, turnover down 95.2%, dropped from Key Strengths without comment | **HIGH, NEW** | AOC-1, AR FY25 p.25 / AR FY26 p.23; strength claimed AR FY25 p.37 |
| "Technology-Agnostic and Asset-Light" Key Strength against a battery balance sheet that is 50.1% of segment assets at 0.37x turn and loss-making | **HIGH, NEW** | AR FY26 p.36 vs Note 38, p.105-106 |
| Three different FY25 PAT figures inside the FY25 report (Rs 34 Cr / 7.2%, Rs 32 Cr / 6.8%, Rs 33.9 Cr / 7.2%) | **HIGH, NEW to Stage 5 (cross-stage item)** | AR FY25 p.38 (table and prose), p.4 (chairman's letter) |
| FY25 exceptional gain of Rs 848.98 lakh (Penta divestment), ~20% of FY25 pre-tax profit, never named in the chairman's letter that reports the resulting PAT and margin | **MEDIUM-HIGH, NEW to Stage 5** | AR FY25 p.19 (Directors' Report table) vs p.4 (letter); flagged with a reason only in the MD&A ratio note, p.38 |
| MD&A Interest Coverage Ratio "+39.20%" does not reconcile with the report's own EBIT/finance-cost figures and traces numerically to the Debt Service Coverage Ratio variance in Note 43; ROCE variance also left with no Reasons for Variation despite both past the mandatory 25% threshold | **HIGH, NEW to Stage 5** | AR FY26 p.37 vs p.17, p.112 |
| Silent Rs 421.14 lakh FY25 comparative reclassification between employee benefits expense and other expenses, standalone and consolidated, disclosed only as generic regrouping boilerplate | **MEDIUM, NEW to Stage 5** | AR FY25 p.19 vs AR FY26 p.17; standalone Note 47, AR FY26 p.113 |
| India plastic-pipes market citation moves ~2.7x between AR FY25 and AR FY26 for the same market, source switched to IMARC, no reconciliation | **MEDIUM, CORRECTED this rerun (run 1 wrongly called this "internally consistent")** | AR FY25 p.4-5, p.35 vs AR FY26 p.33 |
| CRISIL two-step downgrade undiscussed in chairman's letter/MD&A in **both** years, a repeated omission, not a one-off | **HIGH** | AR FY25 p.49 (A+/Negative -> A/Negative); AR FY26 p.51 (A/Negative -> A-/Stable, A1 -> A2+); neither narrated outside the mandatory table |
| 13-May-2026 CRISIL downgrade against the 28-May-2026 Directors' Report item 12 "no material changes" statement | **HIGH** | AR FY26 p.51, p.20 |
| R&D spend cut 67-79% across both divisions while AR FY26 narrative claims Geon "accelerated its R&D" | **HIGH** | AR FY26 p.28-29; AR FY25 p.30-31 |
| Inventory-turnover "Reasons for Variation" text copied verbatim from FY25 to FY26 despite inventory actually falling (Rs 29,014.77 -> Rs 28,538.08 lakh) in FY26 | **MEDIUM** | AR FY26 p.37; Note 7, p.87; AR FY25 p.38 |
| ~40% extrusion market share claim silently dropped alongside a 13.2% segment revenue decline | **MEDIUM-HIGH** | AR FY25 p.37; absent AR FY26 |
| Heritage claim shrinks from "six decades... 15,000 installations" to "four decades," while the same-year chairman's letter calls it a "60-year journey" | **MEDIUM, NEW** | AR FY25 p.36; AR FY26 p.35, p.5 |
| Penta JV pillar (49.94% held per AOC-1 both years, described "50:50" in the Dec-2023 deck) exits the collaboration narrative without comment after its Feb-2025 divestment | **MEDIUM, NEW** | AR FY25 p.25, p.37; deck p.24 |
| Chairman's letter drops PAT entirely for FY26 and never uses the word "loss," after giving PAT explicitly for FY25 | **MEDIUM, NEW** | AR FY26 p.4-5 vs AR FY25 p.4 |
| Mr Bajrang Lal Bagra re-designated Non-Executive Non-Independent 16 days after his second independent term ended, listed twice in the board composition table | **MEDIUM, NEW** | AR FY26 p.18, p.39-40 |
| Secretarial audit (MR-3) exception: unpaid dividend for FY2017-18 transferred to IEPF beyond the statutory timeline, the one clearly volunteered negative in the corpus, and it comes from the auditor, not management | **LOW-MEDIUM, NEW** | AR FY26 p.24 (also Directors' Report p.21) |
| Battery segment loss widened 69.8% despite 7.2% revenue growth, unreconciled against a same-document "moving towards profitability" claim | **HIGH** | Note 38, AR FY26 p.105-106; claim p.38 |
| Same-document EBITDA figure inconsistency (chairman's letter Rs 10 Cr vs MD&A table Rs 13.05 Cr) | **MEDIUM** | AR FY26 p.4 vs p.37 |
| Stale HEVPL/NCLT receivable disclosure still dated "as at March 31, 2025" inside the FY26 report; wording is not identical to FY25, the FY26 version adds a warranty-reversal sentence (**CORRECTED this rerun; run 1 called the two notes "identical, word-for-word"**) | **MEDIUM** | AR FY26 Note 9, p.87-88, vs AR FY25 Note 9, p.86 |
| Senior-management churn disclosed only in mandatory tables, never narratively | **MEDIUM** | AR FY26 p.3, p.107; AR FY25 p.3 |
| No order-book total disclosed; single ~Rs 150 Cr order lacks counterparty/terms/Reg-30 corroboration | **MEDIUM** | AR FY26 p.37 |
| Neither year's Risks and Challenges section names customer or customer-credit risk, despite HEVPL's insolvency and a 48.9%-overdue receivables book | **MEDIUM, NEW** | AR FY25 p.38; AR FY26 p.38 |
| Industry market-size citations swing materially year to year with no source reconciliation (extrusion CAGR, India EV battery-pack market ~100x) | **LOW-MEDIUM** | AR FY25 p.34-35; AR FY26 p.33-34 |

---

## RERUN DELTA (2026-09-09)

Each numbered item below is from `outputs/final/run1/gate-recommendation.md`, "What a rerun must fix." "Where it
now sits" names the section in this report; "BEFORE / AFTER" states what run 1 said versus what this rerun found.

**Class A (pipeline-wide misses; carried here as management-communication defects per this rerun's brief).**

1. **Rs 421.14 lakh silent FY25 reclassification (employee benefits <-> other expenses).** Where it sits: 4D red
   flags, 2B. BEFORE: not present in run 1 at all. AFTER: re-derived independently (AR FY25 p.19: Employee benefits
   Rs 5,907.53 lakh, Other expenses Rs 7,473.91 lakh; AR FY26 p.17 FY25 comparative: Employee benefits Rs 6,328.67
   lakh, Other expenses Rs 7,052.77 lakh; both moves are exactly Rs 421.14 lakh, offsetting), disclosed only as
   generic regrouping boilerplate at standalone Note 47 (AR FY26 p.113). New MEDIUM flag. Grade impact: reinforces D.
2. **Rs 848.98 lakh Penta exceptional gain, ~20% of FY25 pre-tax profit, absent from the chairman's letter.** Where
   it sits: 2A (new context on row 3), 4D. BEFORE: not present in run 1. AFTER: confirmed (AR FY25 p.19, p.4); noted
   that the MD&A ratio table does at least name it as the cause of a ratio variance (p.38), so it was disclosed
   somewhere, just not in the letter that gives the headline PAT number. New MEDIUM-HIGH flag.
3. **Three different FY25 PAT figures inside the FY25 report.** Where it sits: 2A, 2C, 4D, 4C. BEFORE: not present
   in run 1. AFTER: confirmed verbatim (table "PAT... 34"/"7.2%," prose "KET's PAT stood at ₹32 crores... 6.8%,"
   letter "PAT (PAT) stood at ₹33.9 crores... 7.2%," all AR FY25 p.38/p.4). New HIGH flag; drives Transparency and
   Consistency ratings down from 2/5 to 1/5.
4. **MD&A Interest Coverage Ratio "+39.20%" not reconcilable to EBIT/finance cost; ROCE and Interest Coverage both
   past 25% variance with blank Reasons for Variation.** Where it sits: 2C, 4D. BEFORE: not present in run 1. AFTER:
   confirmed the figures do not reconcile (implied actual interest coverage fell ~84%, not rose 39.20%), and traced
   the 39.20% number to a probable mislabelled Debt Service Coverage Ratio cell from Note 43 (p.112), an original
   finding of this rerun beyond what the fix list named. New HIGH flag; drives Accountability rating down.
5. **Rajoo working-capital contrast.** Stage 6's item, not Stage 5's. Carried here only as the new peer question 4B
   #10, worded exactly as instructed.

**Class B (caught elsewhere in the pipeline, missed by Stage 5 run 1; now joined to the credibility read).**

6. **Unexplained Rs 1,668.41 lakh "Other" income line.** Where it sits: 2A row 3, 2D, 4D. BEFORE: absent from run 1
   entirely. AFTER: confirmed (Note 23, AR FY26 p.95, vs Rs 22.91 lakh FY25); tied explicitly into the "well
   positioned" promise-delivery row and the loss-size discussion. New HIGH flag.
7. **Receivables ageing (48.9% over one year, Rs 1,935.36 lakh over three years at 23.5% cover).** Where it sits:
   2B, 2D, 4D. BEFORE: run 1 discussed the HEVPL receivable specifically but never the aggregate ageing profile or
   the turnover-ratio-improves-as-book-shrinks mechanism. AFTER: confirmed and computed independently from Note 9
   (AR FY26 p.87-88): (471.76 + 2,021.56 + 1,935.36) / 9,052.43 = 48.92%; 455.13 / 1,935.36 = 23.52%. New HIGH flag.
8. **Varos Technology negative net worth, turnover down 95%, dropped Key Strength.** Where it sits: 2B, 2D, 4D.
   BEFORE: run 1 quoted the Varos Key Strength language in the 1A table but never analysed the AOC-1 financials or
   flagged the disappearance. AFTER: confirmed and computed net worth from AOC-1 line items (Share Capital +
   Reserves & Surplus): Rs (264.68) lakh FY25 -> Rs (556.17) lakh FY26 (AR FY25 p.25 / AR FY26 p.23); turnover Rs
   372.99 lakh -> Rs 17.84 lakh, -95.2%. New HIGH flag.
9. **"Technology-Agnostic and Asset-Light" claim against battery segment assets (50.1% of segment assets, 0.37x
   turn).** Where it sits: 2D, 4D. BEFORE: absent from run 1. AFTER: confirmed and computed (Note 38, AR FY26
   p.105-106: Battery segment assets Rs 36,437.25 lakh / Total segment assets Rs 72,775.30 lakh = 50.07%; segment
   revenue Rs 13,610.84 lakh / segment assets = 0.373x). New HIGH flag.

**Class C (correction to a Stage 5 finding).**

10. **Plastic-pipes market citations, "internally consistent" -> corrected to CONTRADICTORY.** Where it sits: 3B,
    1A, 4D. BEFORE: run 1 stated "internally consistent, sourced to a named government scheme." AFTER: corrected.
    The AR FY25 figure (Rs 500 billion by FY2025) and the AR FY26 figure (USD 2.10 billion for 2025, roughly Rs 185
    billion at a representative rate) describe the same India market for adjacent years and differ by roughly
    2.7x, with the source switched to IMARC Group in AR FY26 and no reconciliation offered. Verdict changed from
    "internally consistent" to "contradicted, unreconciled," and the item is now flagged for peer verification.

**Other run-1 gaps the audit named (all carried into this rerun).** CRISIL downgrade undiscussed in **both** years
(a repeated pattern, not a one-off): confirmed at AR FY25 p.49 and AR FY26 p.51. The 13-May-2026 downgrade against
the 28-May-2026 "no material changes" statement: confirmed at AR FY26 p.51 and p.20. The inventory-turnover
"reason" text copied verbatim from FY25 to FY26 while the underlying direction reversed: confirmed, Note 7 shows
inventory falling Rs 29,014.77 -> Rs 28,538.08 lakh (AR FY26 p.37, Note 7 p.87; AR FY25 p.38). Heritage claim
shrinking from "over six decades... 15,000 installations" to "a legacy of over four decades" while the same
report's letter says "60-year journey": confirmed, AR FY25 p.36; AR FY26 p.35 and p.5. The Penta JV pillar removed
from the collaboration table without comment, deck "50:50" vs AOC-1 49.94%: confirmed, deck p.24; AR FY25 p.37,
p.21, p.25. The FY26 secretarial-audit exception on the late IEPF transfer, the one clear volunteered negative:
confirmed, AR FY26 MR-3 p.24; Directors' Report item 23, p.21. Mr Bajrang Lal Bagra re-badged Non-Executive
Non-Independent sixteen days after his second independent term ended, listed twice in the board table: confirmed,
AR FY26 p.18, p.39-40 (run 1's page-40 citation retained; p.25 in the task brief is the MR-3 confirmation, also
checked). The FY26 chairman's letter dropping PAT entirely and never using the word "loss": confirmed, AR FY26
p.4-5. Neither year's Risks and Challenges section naming customer or customer-credit risk: confirmed, AR FY25
p.38, AR FY26 p.38. The ~Rs 150 Cr order, the Rs 1,500+ Cr ceiling and the ~7 GWh capacity claims tested against
each other: done in 1A, with the arithmetic and the Mordor cross-test both flagged as illustrative, not filed,
figures. Revenue down three years running from the deck's FY23 base: confirmed and computed, deck p.7 (Rs 670 Cr)
-> AR FY25 p.37 (Rs 608 Cr, Rs 477 Cr) -> AR FY26 p.37 (Rs 477 Cr, Rs 451 Cr). The AR FY26 Mordor citation of a
USD 53.76 million 2026 India EV battery-pack market being implausibly small next to Geon's own segment revenue:
confirmed and computed in 1A/3B.

**Two wording corrections named in the brief.** The HEVPL note is corrected from "identical, word-for-word" to: the
FY26 version (Note 9, AR FY26 p.87-88) adds a fuller warranty-reversal sentence not present in the FY25 Note 9 (AR
FY25 p.86); a shorter warranty-reversal sentence does appear in FY25, but in a different note (the borrowings/other
dues footnote, AR FY25 p.90-91 equivalent). The core finding, that the receivable is still dated "as at March 31,
2025" inside the FY26 report with the balance and case status unrefreshed, stands unchanged. "Accelerated its R&D"
is corrected from AR FY26 p.29 to **AR FY26 p.28** (Geon Division technology-absorption section). The nil dividend
citation is corrected from AR FY26 p.18 to **AR FY26 p.17** (Directors' Report item 3).

---

## Sources re-read for this rerun, filenames and PDF pages

`inputs/annual-report/Annual_Report_2025.txt`: p.4-5 (chairman's letter, PAT/EBITDA/market citations), p.19-20
(Directors' Report financial table, exceptional item, dividend), p.25 (AOC-1, Varos), p.33-38 (MD&A: economy,
industry overview, company overview, Key Strengths, Financial Performance Snapshot, Key Financial Ratios, Business
Outlook, Risks and Challenges), p.49 (CRISIL rating table). Confirmed via targeted grep: HEVPL note locations
(pp.84-91 equivalent range), Varos references across AOC-1, Notes 39/related-party.

`inputs/annual-report/Annual_Report_2026.txt`: p.4-5 (chairman's letter), p.17-24 (Directors' Report: financial
table, dividend, director changes, item 12, item 23/auditors; Annexure-1 AOC-1; Annexure-2 MR-3 secretarial audit),
p.28-30 (Annexure-4 R&D/technology absorption, Annexure-5 remuneration), p.31-40 (MD&A: economy, industry overview
incl. IMARC/Mordor/Grand View Horizon/Research and Markets citations, company overview, Key Strengths, Financial
Performance Snapshot, Key Financial Ratios, Business Outlook, Risks and Challenges; Corporate Governance Report
board composition table), p.51 (CRISIL rating table), p.87-88 (Note 9, trade receivables and ageing), p.95 (Note
23, other income), p.103-113 (Note 38 standalone segment information, Note 41 contingent liabilities/commitments,
Note 42 income taxes, Note 43 ratios, Note 44 dividend, Note 47 regrouping), p.160-161 (Note 38 consolidated segment
information, cross-check only).

`inputs/presentation/Investor_Presentation_1.txt`: p.7 (FY23 consolidated revenue base, for the three-year decline
computation).

Not re-read this rerun (unchanged from run 1, not implicated in the audit's Stage 5 fix list): the Dec-2023 deck's
remaining pages (market-share, ARAI/IATF, Penta JV percentage claims) and `screener-Data_Sheet.csv`.

```yaml
stage: B05-concall
company: "KABRAEXTRU"
run_date: "2026-09-05"
model: claude-sonnet-5
status: complete
no_concall_mode: true
rerun: 2
input_gaps:
  - "results (HIGH): no results PDFs in corpus; FY26 audited AR used as delivery record"
  - "rating (HIGH): CRISIL rationale for both the FY25 and FY26 downgrades absent from corpus; only the generic Corporate Governance table reason available (AR FY26 p.51; AR FY25 p.49)"
  - "announcements: no Reg 30 record; ~Rs150 Cr order and web-reported 2026 preferential issue uncorroborated by filings"
  - "shareholding: not in corpus"
  - "research: not in corpus"
  - "prospectus: not expected"
  - "presentation-stale: only investor presentation in corpus is Dec-2023 deck, 2.5+ years stale"
  - "peer-concall-windsor: Windsor Machines has no transcript, excluded from peer verification"
  - "peer-concall-mislabel-stale: carried forward per orchestrator, not independently investigated"
  - "screener-csv-defect: carried forward per orchestrator; no defect independently observed in rows used here"
  - "sector_cap_row: carried forward per orchestrator, not applicable to this stage"
flags:
  - {type: "UNEXPLAINED_OTHER_INCOME", reason: "Rs 1,668.41 lakh unexplained Other income line (vs Rs 22.91 lakh FY25) determines the size of the reported FY26 standalone pre-tax loss of Rs (423.21) lakh; never named in narrative (Note 23, AR FY26 p.95; loss AR FY26 p.17)"}
  - {type: "RECEIVABLES_AGEING_VS_TURNOVER_FRAMING", reason: "48.9% of gross receivables (Rs 4,428.68/9,052.43 lakh) over one year overdue and Rs 1,935.36 lakh over three years at 23.5% provision cover, against an MD&A that reports only a +5.20% debtors-turnover improvement driven by book shrinkage (Note 9, AR FY26 p.87-88; ratio p.37)"}
  - {type: "VAROS_KEY_STRENGTH_COLLAPSE", reason: "Varos Technology Pvt Ltd, a named Key Strength in AR FY25, has turnover down 95.2% (Rs 372.99 to Rs 17.84 lakh) and net worth of Rs (556.17) lakh FY26 vs Rs (264.68) lakh FY25, dropped from AR FY26 Key Strengths without comment (AOC-1, AR FY25 p.25/AR FY26 p.23; strength claim AR FY25 p.37)"}
  - {type: "ASSET_LIGHT_CLAIM_CONTRADICTED", reason: "'Technology-Agnostic and Asset-Light Approach' Key Strength (AR FY26 p.36) against battery segment assets of Rs 36,437.25 lakh, 50.1% of segment assets, 0.37x asset turn, and a Rs 4,334.64 lakh segment loss (Note 38, AR FY26 p.105-106)"}
  - {type: "THREE_FY25_PAT_FIGURES", reason: "AR FY25 reports three different FY25 PAT figures in one document: table Rs 34 Cr/7.2%, prose Rs 32 Cr/6.8%, chairman's letter Rs 33.9 Cr/7.2% (AR FY25 p.38, p.4), none reconciled to the others"}
  - {type: "EXCEPTIONAL_GAIN_OMITTED_FROM_LETTER", reason: "FY25 exceptional gain of Rs 848.98 lakh (Penta divestment), about 20% of FY25 pre-tax profit, never named in the FY25 chairman's letter that reports the resulting PAT and margin (AR FY25 p.19 vs p.4)"}
  - {type: "INTEREST_COVERAGE_RATIO_MISLABEL", reason: "MD&A Interest Coverage Ratio '+39.20%' does not reconcile with the report's own EBIT (Rs 7.16 Cr) and finance cost (Rs 1,139.25 lakh); the figure numerically matches Note 43's Debt Service Coverage Ratio variance instead; ROCE also left with no Reasons for Variation despite both exceeding the mandatory 25% threshold (AR FY26 p.37 vs p.17, Note 43 p.112)"}
  - {type: "SILENT_EXPENSE_RECLASSIFICATION", reason: "Rs 421.14 lakh FY25 comparative reclassified between employee benefits expense and other expenses, standalone and consolidated, exactly offsetting, disclosed only as generic regrouping boilerplate (AR FY25 p.19; AR FY26 p.17; standalone Note 47, AR FY26 p.113)"}
  - {type: "MARKET_SIZE_CITATION_CONTRADICTION_CORRECTED", reason: "India plastic-pipes market citation moves ~2.7x between AR FY25 (Rs 500bn by FY2025) and AR FY26 (USD 2.10bn/~Rs185bn for 2025, sourced to IMARC), unreconciled; run 1 wrongly called these citations internally consistent (AR FY25 p.4-5, p.35; AR FY26 p.33)"}
  - {type: "RATING_DOWNGRADE_UNDISCUSSED_REPEATED", reason: "CRISIL downgrades in both FY25 (A+/Negative to A/Negative) and FY26 (A/Negative to A-/Stable, A1 to A2+) are disclosed only in the mandatory Corporate Governance table, never narrated in either year's chairman's letter or MD&A (AR FY25 p.49; AR FY26 p.51)"}
  - {type: "MATERIAL_CHANGES_STATEMENT_VS_DOWNGRADE_DATE", reason: "13-May-2026 CRISIL downgrade against the 28-May-2026 Directors' Report item 12 statement of no material changes affecting financial position (AR FY26 p.51, p.20)"}
  - {type: "RD_SPEND_CUT_VS_ACCELERATED_CLAIM", reason: "R&D spend cut 67.1% (Extrusion) and 78.6% (Geon) while AR FY26 narrative claims Geon 'has accelerated its R&D' (AR FY26 p.28-29; AR FY25 p.30-31)"}
  - {type: "MARKET_SHARE_CLAIM_DROPPED", reason: "~40% extrusion market share claim present AR FY25 p.37, silently absent from AR FY26, alongside a 13.2% segment revenue decline"}
  - {type: "HERITAGE_CLAIM_SHRUNK_AND_CONTRADICTED", reason: "Company age claim shrinks from 'over six decades, 15,000 installations' (AR FY25 p.36) to 'over four decades' (AR FY26 p.35) while the same AR FY26 chairman's letter calls it a '60-year journey' (p.5)"}
  - {type: "PENTA_JV_PILLAR_DROPPED_SILENTLY", reason: "Penta Auto Feeding India Ltd (49.94% held per AOC-1, described '50:50' in the Dec-2023 deck) ceased as associate Feb-2025 and exits the collaboration narrative without comment (deck p.24; AR FY25 p.25, p.37; AR FY26 silent)"}
  - {type: "CHAIRMAN_LETTER_DROPS_PAT_AND_LOSS_WORD", reason: "FY26 chairman's letter gives EBITDA but never PAT and never uses the word 'loss', despite giving PAT explicitly in the FY25 letter (AR FY26 p.4-5 vs AR FY25 p.4)"}
  - {type: "BAGRA_REDESIGNATION_DOUBLE_LISTED", reason: "Mr Bajrang Lal Bagra re-designated Non-Executive Non-Independent 16 days after his second independent term ended (26-Aug-2025 to 11-Sep-2025), listed twice in the AR FY26 board composition table (p.18, p.39-40)"}
  - {type: "SECRETARIAL_AUDIT_IEPF_EXCEPTION", reason: "MR-3 records a delayed IEPF transfer of unpaid FY2017-18 dividend beyond the statutory timeline, the one clearly volunteered negative in the corpus, raised by the auditor not management (AR FY26 p.24, p.21)"}
  - {type: "BATTERY_SEGMENT_LOSS_WIDENING_UNRECONCILED", reason: "Battery Division segment loss widened 69.8% (Rs 2,553.28 to Rs 4,334.64 lakh) despite 7.2% revenue growth, unreconciled against a same-document 'moving towards profitability' claim (Note 38, AR FY26 p.105-106; claim p.38)"}
  - {type: "EBITDA_FIGURE_INCONSISTENCY_SAME_DOCUMENT", reason: "Chairman's letter EBITDA Rs 10 Cr vs MD&A table EBITDA Rs 13.05 Cr, same year, same document (AR FY26 p.4 vs p.37)"}
  - {type: "HEVPL_NOTE_STALE_WORDING_CORRECTED", reason: "HEVPL/NCLT receivable note still dated 'as at March 31, 2025' inside the FY26 report; wording is not identical across years as run 1 stated, the FY26 version adds a fuller warranty-reversal sentence (AR FY26 Note 9 p.87-88 vs AR FY25 Note 9 p.86)"}
  - {type: "KMP_CHURN_UNDISCLOSED_NARRATIVELY", reason: "Senior-management churn (COO-Geon, CFO, Extrusion CEO) disclosed only in mandatory tables, never narratively (AR FY26 p.3, p.107; AR FY25 p.3)"}
  - {type: "NO_ORDER_BOOK_TOTAL_DISCLOSED", reason: "Single ~Rs150 Cr order lacks counterparty, terms, or Reg 30 corroboration; no aggregate order book disclosed (AR FY26 p.37)"}
  - {type: "CUSTOMER_CREDIT_RISK_ABSENT_FROM_RISKS_SECTION", reason: "Neither year's Risks and Challenges section names customer or customer-credit risk despite HEVPL's insolvency and a 48.9%-overdue receivables book (AR FY25 p.38; AR FY26 p.38)"}
  - {type: "INVENTORY_TURNOVER_REASON_COPIED_VERBATIM", reason: "FY26 inventory-turnover reason text copied verbatim from FY25 while inventory actually fell Rs 29,014.77 to Rs 28,538.08 lakh (AR FY26 p.37; Note 7 p.87; AR FY25 p.38)"}
  - {type: "MARKET_SIZE_CITATIONS_SWING_UNRECONCILED", reason: "Extrusion machinery CAGR nearly doubled (3.9% to 6.72%) and India EV battery-pack market swung ~100x between AR FY25 and AR FY26, source houses switched both times with no reconciliation (AR FY25 p.34-35; AR FY26 p.33-34)"}
quarters_analysed: ["AR FY25 (year ended 31-Mar-2025)", "AR FY26 (year ended 31-Mar-2026)"]
triggers:
  - {priority: 1, name: "Rs 150 Cr Geon order executes into FY27 revenue", type: "revenue", timeframe: "near (FY27)", conviction: "M", confirm_signal: "FY27 battery segment revenue step-up correlated with order; counterparty/Reg 30 corroboration surfaces", kill_signal: "FY27 battery revenue flat/down or order deferred/uncorroborated; customer advances already fell 18.9% the year the order was described as secured"}
  - {priority: 2, name: "Battery segment reaches profitability", type: "margin", timeframe: "medium, undated", conviction: "L", confirm_signal: "Segment loss narrows materially or turns positive in FY27/FY28 AR", kill_signal: "Segment loss stays above ~Rs40 Cr or widens further"}
  - {priority: 3, name: "Geon facility scales toward Rs1,500+ Cr revenue ceiling", type: "revenue", timeframe: "long, undated", conviction: "L", confirm_signal: "Company discloses utilisation rate and stepped revenue growth path", kill_signal: "No utilisation disclosure given; battery revenue stays near Rs136 Cr for multiple years against a claimed Rs1,500+ Cr ceiling and a India-market citation (Mordor) too small to obviously support it"}
  - {priority: 4, name: "Extrusion recovery on JJM 2.0 / state infra capex revival", type: "revenue", timeframe: "near-medium", conviction: "M", confirm_signal: "Extrusion segment revenue growth resumes in FY27 AR", kill_signal: "JJM 2.0 disbursement delays persist, as already named by the company for a third consecutive declining year"}
  - {priority: 5, name: "Geon diversification into BESS/telecom/solar/inverter D2C", type: "revenue", timeframe: "medium-long", conviction: "L", confirm_signal: "Future AR discloses quantified non-mobility Geon revenue share growing", kill_signal: "No quantified non-mobility revenue disclosed after two further AR cycles"}
  - {priority: 6, name: "Credit rating stabilises post two-step downgrade", type: "cost", timeframe: "near", conviction: "L", confirm_signal: "No further CRISIL downgrade at next review", kill_signal: "Further downgrade or return to Negative outlook"}
guidance:
  - {item: "Geon new-segment entry (E-LCV, E-4W)", number: "not quantified", timeframe: "upcoming fiscal year (FY26)", stated_in: "AR FY25 p.36/38"}
  - {item: "Geon secured order", number: "~Rs 150 Crore", timeframe: "execution in upcoming year (FY27)", stated_in: "AR FY26 p.37"}
  - {item: "Geon facility revenue ceiling at optimal utilisation", number: "Rs 1,500+ Crore", timeframe: "undated / long-term", stated_in: "AR FY26 p.37"}
  - {item: "Capital commitment (contracted capex not yet executed)", number: "Rs 3,177.38 lakh, up from Rs 143.42 lakh FY25", timeframe: "near-term (next FY)", stated_in: "AR FY26 Note 41(b), p.110"}
  - {item: "FY26 dividend", number: "Nil", timeframe: "FY26", stated_in: "AR FY26 Directors' Report p.17"}
promise_delivery:
  delivered: 0
  partial: 2
  missed: 3
  rows:
    - {promised_in: "AR FY25 p.36/38", promise: "Geon to enter E-Low Commercial Vehicles and E-4 Wheelers in FY26", outcome: "Not confirmed by name in AR FY26; RESS, inverter D2C and e-bus packs substituted instead", explanation: "None given"}
    - {promised_in: "AR FY25 p.37", promise: "~40% extrusion market share maintained", outcome: "Claim dropped entirely from AR FY26; extrusion segment revenue fell 13.2% and segment result fell 27.6%", explanation: "None given"}
    - {promised_in: "AR FY25 p.37 outlook", promise: "Well-positioned to capitalize on anticipated growth across both divisions", outcome: "Revenue -5.45%, EBITDA -74.88%, standalone PAT swung to a Rs(2.44) Cr loss on a Rs(423.21) lakh pre-tax loss driven partly by an unexplained Rs1,668.41 lakh Other-income line; dividend cut to Nil", explanation: "External causes cited for extrusion only; no explanation for the Other-income line or the battery segment"}
    - {promised_in: "AR FY25 p.38", promise: "Geon to become a key player in BESS", outcome: "RESS/BESS/inverter D2C products launched (real progress), but battery segment loss widened 69.8% despite 7.2% revenue growth", explanation: "None given for the loss widening"}
    - {promised_in: "AR FY25 p.30-31, p.36-37", promise: "Continued R&D investment across both divisions", outcome: "R&D spend cut 67.1% (Extrusion) and 78.6% (Geon), while AR FY26 narrative claims Geon 'accelerated its R&D'", explanation: "None given; contradiction not addressed"}
excuse_pattern: "external-blame-heavy"
repeated_evasions: []
credibility_grade: "D"
credibility_basis: "Grade unchanged from D (run 1) on a materially wider evidence base. 0/5 testable AR-guidance-vs-delivery promises fully delivered. New this rerun: an unexplained Rs1,668.41 lakh Other-income line sizing the reported loss; a receivables book 48.9% overdue past one year behind a headline turnover 'improvement'; a named Key Strength (Varos) with turnover down 95% and negative net worth, dropped without comment; an asset-light claim against a battery balance sheet that is half of segment assets at 0.37x turn and loss-making; three irreconcilable FY25 PAT figures; an unnamed exceptional gain behind the FY25 base year; an MD&A ratio figure that traces to a probable mislabelled cell; a silent Rs421.14 lakh expense reclassification; and a corrected market-size citation now shown to be contradictory rather than consistent. The no-concall floor is C by default and rises only to B on delivery evidence, never to A; it is silent on a floor below C, and this evidence supports D, the lowest grade the A-D scale provides."
peer_questions:
  - {question: "Does Rajoo Engineers' order book/demand commentary for FY25-26 support or contradict KABRAEXTRU's external-blame framing (JJM disbursement delays, state infra spending delays) for its 13.2% extrusion segment revenue decline?", why: "Tests whether the decline is industry-wide or KABRAEXTRU-specific share loss", check_peers: ["RAJOOENG"]}
  - {question: "What CAGR/market-size does Rajoo cite for the extrusion machinery industry across its FY24-25 calls?", why: "KABRAEXTRU's own cited CAGR nearly doubled between AR FY25 (3.9%) and AR FY26 (6.72%) with the source house switched and no reconciliation", check_peers: ["RAJOOENG"]}
  - {question: "Does Rajoo's market-positioning commentary corroborate or dispute KABRAEXTRU's claimed ~40% extrusion machinery market share, dropped without explanation from AR FY26?", why: "Tests whether the original leadership claim was ever accurate", check_peers: ["RAJOOENG"]}
  - {question: "What raw-material cost trend and pass-through experience does Rajoo report for FY25-26?", why: "KABRAEXTRU's AR MD&A never discusses raw-material trends despite gross margin falling 326 bps FY25-FY26", check_peers: ["RAJOOENG"]}
  - {question: "Does Rajoo report export-market weakness from geopolitical/currency factors in the same FY26 window KABRAEXTRU cites?", why: "Tests whether KABRAEXTRU's 11.6% export revenue decline is sector-wide or customer-specific", check_peers: ["RAJOOENG"]}
  - {question: "What capex-cycle and capacity-addition signal does Rajoo describe for FY25-26 new order intake?", why: "KABRAEXTRU's own capex nearly halved even as its AR reiterates a long-term extrusion growth trajectory", check_peers: ["RAJOOENG"]}
  - {question: "What EV-OEM customer credit quality does HBL Engineering report for its battery vertical, particularly exposure to distressed two/three-wheeler OEMs?", why: "KABRAEXTRU carries a stale, unrefreshed Rs30.39 Cr Hero Electric (HEVPL) receivable tied to an OEM now under NCLT insolvency", check_peers: ["HBLENGINE"]}
  - {question: "What capacity-utilisation and margin trend does HBL Engineering report in its own lithium-ion battery pack business?", why: "Tests whether KABRAEXTRU's negative operating leverage in Geon (loss +69.8% on +7.2% revenue) is structural/industry-wide or company-specific execution", check_peers: ["HBLENGINE"]}
  - {question: "What India EV battery pack market-size figure, if any, does HBL Engineering cite?", why: "KABRAEXTRU's own two ARs cite India EV battery pack market sizes roughly 100x apart, and the AR FY26 figure implies an improbable ~30% Geon market share", check_peers: ["HBLENGINE"]}
  - {question: "What working-capital terms does Rajoo Engineers describe for extrusion machinery orders (advance on order finalisation, payment before dispatch, receivable days), and how does that compare with KABRAEXTRU's receivable profile (48.9% of gross receivables more than one year overdue, AR FY26 Note 9 p.88)?", why: "Tests whether KABRAEXTRU's receivables deterioration is a company-specific collection/credit problem against a stated peer order-economics discipline", check_peers: ["RAJOOENG"]}
red_flags:
  - "HIGH, NEW: Rs1,668.41 lakh unexplained Other-income line (vs Rs22.91 lakh FY25) determines the size of the reported FY26 standalone pre-tax loss of Rs(423.21) lakh, never named in narrative (Note 23, AR FY26 p.95)"
  - "HIGH, NEW: receivables 48.9% overdue past one year, Rs1,935.36 lakh past three years at 23.5% provision cover, behind a headline debtors-turnover 'improvement' driven by book shrinkage (Note 9, AR FY26 p.87-88)"
  - "HIGH, NEW: Varos Technology Pvt Ltd, a named FY25 Key Strength, turnover down 95.2% and net worth Rs(556.17) lakh FY26 vs Rs(264.68) lakh FY25, dropped from AR FY26 Key Strengths without comment (AOC-1, AR FY25 p.25 / AR FY26 p.23)"
  - "HIGH, NEW: 'Technology-Agnostic and Asset-Light' Key Strength against battery segment assets 50.1% of total segment assets at 0.37x turn and a Rs4,334.64 lakh loss (AR FY26 p.36 vs Note 38 p.105-106)"
  - "HIGH, NEW: three irreconcilable FY25 PAT figures inside the FY25 report, Rs34 Cr/7.2%, Rs32 Cr/6.8%, Rs33.9 Cr/7.2% (AR FY25 p.38, p.4)"
  - "HIGH, NEW: MD&A Interest Coverage Ratio '+39.20%' does not reconcile with the report's own EBIT/finance-cost figures and matches Note 43's Debt Service Coverage Ratio variance instead; ROCE also left with no Reasons for Variation despite exceeding the mandatory 25% threshold (AR FY26 p.37 vs p.17, p.112)"
  - "HIGH: CRISIL downgrades undiscussed narratively in BOTH FY25 and FY26, a repeated omission (AR FY25 p.49; AR FY26 p.51)"
  - "HIGH: 13-May-2026 CRISIL downgrade against the 28-May-2026 Directors' Report item 12 'no material changes' statement (AR FY26 p.51, p.20)"
  - "HIGH: R&D spend cut 67-79% across both divisions while AR FY26 narrative claims Geon 'accelerated its R&D' (AR FY26 p.28-29; AR FY25 p.30-31)"
  - "HIGH: Battery segment loss widened 69.8% (Rs4,334.64 lakh FY26 vs Rs2,553.28 lakh FY25) despite 7.2% revenue growth, unreconciled against a same-document 'moving towards profitability' claim"
  - "MEDIUM-HIGH, NEW: FY25 exceptional gain of Rs848.98 lakh (Penta divestment), ~20% of FY25 pre-tax profit, never named in the FY25 chairman's letter (AR FY25 p.19 vs p.4)"
  - "MEDIUM-HIGH: ~40% extrusion market share claim silently dropped between AR FY25 and AR FY26, alongside a 13.2% segment revenue decline"
  - "MEDIUM, NEW: silent Rs421.14 lakh FY25 comparative reclassification between employee benefits and other expenses, disclosed only as generic regrouping boilerplate (AR FY25 p.19; AR FY26 p.17; standalone Note 47 p.113)"
  - "MEDIUM, CORRECTED: India plastic-pipes market citation moves ~2.7x between AR FY25 and AR FY26 for the same market, source switched to IMARC, unreconciled (run1 wrongly called this internally consistent)"
  - "MEDIUM, NEW: heritage claim shrinks from 'six decades, 15,000 installations' to 'four decades' while the same-year chairman's letter says '60-year journey' (AR FY25 p.36; AR FY26 p.35, p.5)"
  - "MEDIUM, NEW: Penta JV pillar (49.94% held, deck claimed '50:50') exits collaboration narrative without comment after Feb-2025 divestment (deck p.24; AR FY25 p.25, p.37)"
  - "MEDIUM, NEW: FY26 chairman's letter drops PAT entirely and never uses the word 'loss', after giving PAT explicitly in FY25 (AR FY26 p.4-5 vs AR FY25 p.4)"
  - "MEDIUM, NEW: Mr Bajrang Lal Bagra re-designated Non-Executive Non-Independent 16 days after his second independent term ended, listed twice in the board table (AR FY26 p.18, p.39-40)"
  - "MEDIUM: same-document EBITDA figure inconsistency (chairman's letter Rs10 Cr vs MD&A table Rs13.05 Cr, AR FY26 p.4 vs p.37)"
  - "MEDIUM, CORRECTED: HEVPL/NCLT receivable note still dated 'as at March 31, 2025' inside FY26 report; wording not identical across years as run1 stated, FY26 adds a fuller warranty-reversal sentence (Note 9, AR FY26 p.87-88 vs AR FY25 p.86)"
  - "MEDIUM: senior-management churn disclosed only in mandatory tables, never narratively (AR FY26 p.3, p.107; AR FY25 p.3)"
  - "MEDIUM: no order-book total disclosed; single ~Rs150 Cr order lacks counterparty, terms, or Reg 30 corroboration (AR FY26 p.37)"
  - "MEDIUM, NEW: neither year's Risks and Challenges section names customer or customer-credit risk despite HEVPL insolvency and a 48.9%-overdue receivables book (AR FY25 p.38; AR FY26 p.38)"
  - "LOW-MEDIUM, NEW: FY26 inventory-turnover reason text copied verbatim from FY25 while inventory actually fell Rs29,014.77 to Rs28,538.08 lakh (AR FY26 p.37; Note 7 p.87)"
  - "LOW-MEDIUM: industry market-size citations swing materially year to year with no source reconciliation (extrusion CAGR 3.9% to 6.72%; India EV battery-pack market ~100x)"
  - "LOW-MEDIUM, NEW: secretarial audit (MR-3) exception on the late IEPF transfer, the one clearly volunteered negative in the corpus, raised by the auditor not management (AR FY26 p.24, p.21)"
dropped_triggers:
  - "~40% extrusion market share claim (AR FY25 p.37) - absent from AR FY26 entirely, no explanation"
  - "ARAI AIS-156 certification and IATF-approved facility claims (Dec-2023 deck p.16, p.22) - never repeated in AR FY25 or AR FY26"
  - "~18% li-ion battery segment market share claim (Dec-2023 deck p.12, p.21) - never repeated or updated in AR FY25 or AR FY26"
  - "Varos Technology as a Key Strength (AR FY25 p.37) - absent from AR FY26 Key Strengths despite the subsidiary remaining active and its financials worsening"
  - "Penta Auto Feeding India Ltd as a JV/collaboration pillar (Dec-2023 deck p.24; AR FY25 collaboration table p.37) - divested Feb-2025, absent from AR FY26 narrative"
timeline_slippages:
  - "E-3 Wheeler entry promised 'Q4FY24' (Dec-2023 deck p.16); AR FY25 states entry only 'in FY25', roughly a year later than the deck's timeline"
  - "E-Low Commercial Vehicle and E-4 Wheeler entry promised 'in the upcoming fiscal year' (FY26) per AR FY25 p.36/38; AR FY26 does not confirm entry into either segment by name, replaced by undated 'medium to long term' framing"
  - "Geon path to profitability: framed as 'moving towards profitability as volumes scale up' in AR FY26 p.38 with no date; battery segment loss instead widened 69.8%"
analyst_note: "This rerun re-derived every figure independently from the two annual reports; no figure or page anchor above was copied from run 1 without re-checking against the source text. Two run-1 findings were corrected on re-derivation: the plastic-pipes market citations, called 'internally consistent' in run 1, are in fact ~2.7x apart and the source house changed; the HEVPL note, called 'identical, word-for-word' in run 1, in fact gains a fuller warranty-reversal sentence in the FY26 version (the core staleness finding still holds). Two page-citation errors were corrected: 'accelerated its R&D' is at AR FY26 p.28, not p.29; the nil-dividend statement is at AR FY26 p.17, not p.18. The degraded-mode rule's silence on a floor below C is treated the same way run 1's analyst note treated it: as leaving room to grade on the evidence, which here supports D, the lowest grade the A-D scale provides. This rerun did not re-verify the Dec-2023 deck's market-share, ARAI/IATF or Penta-percentage claims beyond what run 1 already cited, since the audit did not name deck-citation errors in its Stage 5 fix list; those citations are carried forward from run 1 unchanged."
```
