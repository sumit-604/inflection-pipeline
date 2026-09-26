# Stage 2 — Notes to Financial Statements, Triple Pass, Consolidated
Company: Trident Lifeline Ltd (TLL) | Run: tll-2026-09-26 | Source: Annual_Report_2026.txt (FY2025-26, primary), Annual_Report_2025.txt (backward-check), H1 FY25/FY26 original vs refiled results.
Unit: source is ₹ Lakhs throughout (AR face: "Amount in Lakhs"); ₹ Cr shown in parentheses on first use. Basis: Indian GAAP (AS-18, AS-3), not Ind AS.

This report combines Pass 1 (full extraction, Note 1 to last), Pass 2 (what Pass 1 missed, five orchestrator-named open items plus a second sweep), and Pass 3 (pattern re-read: contradictions, cross-note number mismatches, vague-vs-detailed disclosure asymmetry, restatements, subsequent events, going-concern language).

## PASS 3 — PATTERN RE-READ

Targeted the three cross-note number-matching items the orchestrator carried forward from Pass 2, plus a fresh sweep for restatements and subsequent events.

1. **"Shareholders Funds" ratio-note denominator vs Balance Sheet net worth — CONFIRMED MISMATCH, FY26 only.** Note 29-equivalent Ratio Analysis (consolidated, p.116-117) uses Shareholders Funds ₹10,416.58L (FY26) as the denominator for Debt-Equity and Return on Equity/Investment ratios. Pass 1's Balance-Sheet-derived net worth (Reserves ₹8,474.26L + Share Capital ₹1,193.30L = ₹9,667.56L, p.107) is ₹749.02L lower. FY25 figures match exactly (₹6,964.96L both places). No note bridges the FY26-only gap; Share Application Money Pending Allotment (₹372.67L) and/or Minority Interest are the plausible but unconfirmed candidates. (Note 29-equiv Ratio Analysis p.116-117; Balance Sheet p.107) 🟡 unresolved definitional mismatch, confined to the current year.

2. **Segment-note receivables (Note 31) vs Balance Sheet consolidated trade receivables (Note 17) — CONFIRMED MISMATCH, refined to a near-standalone match.** Segment note total ₹4,947.50L (FY26) sits ₹2,417.89L below the consolidated Note 17 total of ₹7,365.39L, but only ₹13.39L above the STANDALONE Note 17 total (₹4,934.11L) — same pattern in FY25 (segment ₹2,049.38L vs standalone ₹2,040.16L, gap ₹9.22L). The consolidated segment note is built substantially off the parent-only receivables book while sitting inside the consolidated financial statements, with a small unexplained residual even against standalone. (Note 31 p.123; Note 17 standalone p.67, consolidated p.108-109) 🔴 RED FLAG, internal inconsistency within the same consolidated statements.

3. **Undisclosed "Changes in Working Capital Facilities" cash-flow line — CONFIRMED, mechanism fully traced.** This line (₹945.65L FY26 addback / ₹625.67L FY25 addback) exists ONLY in the FY26 AR's cash flow statement; it is absent from the FY25 AR's own FY25 figures and absent from the H1 FY26 refiled results (14-Nov-2025), which use the conventional 7-line working-capital block. The reclassification was introduced between the H1 FY26 filing and the FY26 annual audit sign-off (07-May-2026), applied retroactively to the FY25 comparative, with no restatement/regrouping note anywhere (searched "restat", "regroup", "reclassif" — only hits are unrelated fixed-asset-schedule "Previous Year's Figures" headers, p.6638/11798, confirmed on this pass, no accompanying explanatory text). Net effect: flatters both years' reported operating cash generation; the auditor issued an unmodified opinion both years with no qualification on this point. (FY26 AR cash flow p.96 vs FY25 AR cash flow p.84; H1 FY26 refiled cash flow p.13) 🔴 RED FLAG.

4. **Restatements sweep — no material findings.** No standalone or consolidated note discloses a prior-period restatement of P&L, balance sheet, or cash flow figures (beyond the undisclosed cash-flow reclassification in item 3 above, which is a presentation change, not a labelled restatement). "Previous Year's Figures" occurrences (p.6638, 11798) are fixed-asset-schedule column headers, not restatement notes.

5. **Subsequent events sweep — no material findings.** No "Events after the Balance Sheet Date" note beyond generic going-concern/impairment boilerplate ("Balance Sheet date" used only in accounting-policy and CARO going-concern language, pp.4659-4982, 8717-8844, 14222-14327). No disclosed subsequent event that changes the picture (e.g., the Section 197 AGM ratification vote and the main-board migration are both prospective items already carried as open items, not undisclosed subsequent events).

6. **Going concern — CONFIRMED NONE.** Both audit reports (standalone and consolidated) explicitly conclude no material uncertainty exists on going concern (Standalone CARO xix, p.51; auditor's responsibilities section, both reports). No going-concern language found anywhere in the notes on this final pass either.

PASS 3 yields three confirmed/refined findings (all carried from Pass 2, now cross-checked one further time against the source) and no new items. Proceeding to consolidation.

---

## CONSOLIDATED NOTES ANALYSIS, ALL THREE PASSES COMBINED

### A. TOP 15 MOST SIGNIFICANT FINDINGS

| Rank | Finding | Note # | Rating | Why it matters |
|---|---|---|---|---|
| 1 | Undisclosed "Changes in Working Capital Facilities" cash-flow reclassification, introduced only in the FY26 AR, applied retroactively to FY25, absent from the FY25 AR and the H1 FY26 filing; flatters CFO both years, no note, no audit qualification | Cash Flow Statement, p.96 vs FY25 AR p.84 | 🔴 | Directly inflates the operating cash-generation number the market uses to judge cash conversion (LBF1); an undisclosed methodology change mid-audit-cycle is an accounting-quality red flag independent of the underlying WC stretch |
| 2 | Corporate guarantees given for non-subsidiary, director-interest LLPs (Talon Healthcare LLP, Tench Life Sciences LLP): ₹500L consolidated / ₹2,855L standalone | Note 32, pp.80/124 | 🔴 | Balance sheet risk extended to entities the company neither owns nor controls; only disclosed link is "Director's Interest" |
| 3 | Segment note (Note 31) consolidated trade-receivable total does not reconcile to Balance Sheet/Note 17 consolidated trade receivables (₹4,947.50L vs ₹7,365.39L, gap ₹2,417.89L); refined to a near-exact match with STANDALONE receivables instead, with a small unexplained residual (₹13.39L) | Notes 17 & 31, pp.108/123 | 🔴 | Internal inconsistency inside the same consolidated financial statements; the "consolidated" segment note appears built off the parent-only book |
| 4 | Goodwill jumped 10.6x (₹52.37L → ₹555.15L) with zero explanatory or computation note; dated to Trident Mediquip share tranches (30.12.2025, 31.12.2025, 16.03.2026) and bonus issue (01.02.2026), but no purchase-consideration or fair-value-of-net-assets disclosure exists | Balance Sheet p.107; corporate-history note p.125 | 🔴 | Material, fast-growing intangible with zero accounting support for its measurement |
| 5 | AOC-1 confirms the deck-vs-delivery gap directly from audited data: TNS Pharma loss-making, negative net worth, ₹5.77 Cr turnover (deck peak ₹40 Cr); TLL Parenterals "yet to commence operations" (deck peak ₹200 Cr); Trident Mediquip ₹27.32 Cr (deck peak ₹70 Cr) | AOC-1, p.41 | 🔴 | Independently evidences LBF3 from the audited annexure itself, not from inference |
| 6 | TNS Pharma investment carried at INCREASED cost (₹153L→₹255L, a further 16-Apr-2025 share purchase) despite negative net worth and a widening loss, no impairment disclosed | Note 11 vs AOC-1, pp.65/41 | 🔴 | Capital added to a deteriorating subsidiary in the same year its losses widened, with no impairment test disclosed against generic CGU policy language |
| 7 | Section 197 excess director remuneration: Ashish Bafna's excess (₹6.37L) taken WITHOUT prior member approval, ratified by the Board 26-Aug-2026 subject to a pending shareholder vote at the FY26 AGM; separately qualified by the statutory auditor | Consolidated Auditor's Report pp.89/91; Directors' Report p.25 | 🔴 | Auditor-flagged Companies Act breach with a live, checkable outcome |
| 8 | IT audit trail (edit log) not maintained at one (unnamed) subsidiary, database AND application level, for the full year | Consolidated Auditor's Report Rule 11(g), p.90 | 🔴 | Named, unremediated internal-control gap under the mandatory audit-trail rule |
| 9 | Preferential warrant proceeds utilisation: only 57.5% (₹1,526.57L of ₹2,657.34L) utilised by year-end, disclosed in one vague line with no category breakdown, unlike the itemised IPO utilisation table | Directors' Report item 5, p.24 | 🔴 | Investors cannot see where the ₹1,130.77L shortfall sits (working capital vs subsidiary investment vs capex vs debt repayment) |
| 10 | "Shareholders Funds" in the consolidated Ratio Analysis Note (₹10,416.58L FY26) does not match Balance-Sheet-derived net worth (₹9,667.56L FY26); FY25 figures match exactly | Ratio Analysis Note p.116-117; Balance Sheet p.107 | 🟡 | Definitional mismatch confined to the current year, same pattern-family as finding 3 |
| 11 | Consolidated trade receivables grew 3.4x faster than revenue (166% vs 48.4%); CFO only ₹469.07L against PAT ₹1,931.88L; BUT the company's own ratio-analysis note shows receivable AND payable turnover both slowed ~40%, a symmetric growth-induced signature, not receivables-only | Cash Flow Statement p.97-98; Note 17 p.108-109; Ratio Analysis p.116-117 | 🟡/🔴 | Cash-conversion stretch confirmed quantitatively (LBF1), but the company's own data leans the classification toward GROWTH-INDUCED rather than STRUCTURAL; still needs customer-terms evidence to close |
| 12 | Zero doubtful-debt provisioning against a fast-tripling, largely export receivables book (Ghana, Kenya, Peru, Venezuela); no ECL matrix (AS framework does not require one) | Note 17.1/17.2, pp.67, 108-109 | 🟡 | Removes a normal early-warning signal on receivable quality at exactly the point receivables are growing fastest |
| 13 | Unsecured loan FROM Chairman Hardik Desai accelerating (₹1,353.37L FY26 vs ₹491.00L FY25 drawn during the year), repayable on demand, outside normal maturity/covenant discipline | Note 30B/C, pp.120-121; Note 3.2 | 🟡 | Material liquidity item funded by the promoter at an accelerating pace, on demand terms |
| 14 | "Claim Income" ₹541.05L (58% of consolidated Other Income) is RECURRING (₹522.17L FY25, +3.6% YoY) but its nature and counterparty are never disclosed anywhere in the AR | Note 22, p.110-111 | 🟡 | Recurring ~₹5+ Cr/year income line with zero qualitative disclosure is a genuine, persistent disclosure gap even though not one-off |
| 15 | Debt-funding of a pre-revenue subsidiary: TLL Parenterals ("not commenced operations") carries a Yes Bank term loan of ₹1,067.47L non-current + ₹186.44L current | Note 3, consolidated p.100 | 🟡 | Funding-structure point tied to LBF3's funding-plan question; leverage sits ahead of any revenue at that subsidiary |

### B. ACCOUNTING QUALITY SCORE

| Dimension | Score /10 | Basis |
|---|---|---|
| Revenue recognition conservatism | 7 | Dispatch-based recognition, KAM on discount/rebate estimation but no restatement or reversal found; no customer concentration disclosure limits independent verification |
| Expense capitalisation honesty | 7 | No capitalisation-threshold disclosed but no evidence of aggressive capitalisation found; depreciation policy conservative on vehicles, matches Schedule II elsewhere |
| Provisioning adequacy | 4 | Zero doubtful-debt provisioning on a tripling receivables book; static ₹7.02L gratuity provision two years running with no actuarial assumptions disclosed; no impairment against a negative-net-worth subsidiary investment |
| RPT fairness | 5 | Rates on related-party loans broadly arm's-length, but corporate guarantees extended to non-subsidiary director-interest LLPs, and RPT sales (Tench+Talon) are 13.9% of consolidated revenue |
| Disclosure transparency | 3 | Goodwill 10.6x jump with zero note; segment-note receivables mismatch; "Shareholders Funds" denominator mismatch; undisclosed cash-flow reclassification; unexplained recurring "Claim Income"; vague warrant-utilisation disclosure vs the itemised IPO table |
| Consistency with prior years | 4 | The cash-flow methodology change applied retroactively to FY25 without disclosure is a direct consistency breach; segment/receivables and Shareholders Funds mismatches are internal, not year-over-year, but compound the pattern |
| **OVERALL** | **4** | Multiple genuine, evidenced disclosure gaps and one undisclosed presentation change that flatters a headline cash metric, set against no restatements, no going-concern issue, and clean MSME/CSR/warrant-reconciliation mechanics elsewhere |

### C. KEY RISKS FROM NOTES

| Risk | Severity | What to monitor | When it could hit |
|---|---|---|---|
| Cash-flow presentation change overstates CFO | High | Whether FY27 AR restores the conventional 7-line WC block or keeps the addback; ask management directly for the accounting rationale | Next annual audit sign-off (FY27, expected ~May 2027) |
| Corporate guarantees to non-group LLPs | High | Any drawdown/default event at Talon or Tench; renewal or expansion of the guarantee | Any credit event at either LLP |
| Goodwill impairment | Medium-High | Whether a goodwill note appears in FY27 AR; Trident Mediquip's subsequent performance vs the price paid | Next impairment test cycle, or earlier if Mediquip underperforms |
| Negative-net-worth subsidiary carried at cost | Medium-High | Whether TNS Pharma's losses widen further; any impairment charge in FY27 | Next annual result if losses continue |
| Section 197 remuneration ratification | Medium | Outcome of the FY26 AGM special resolution on Ashish Bafna's excess remuneration | FY26 AGM (per the notice already issued) |
| IT audit-trail gap at unnamed subsidiary | Medium | Whether the FY27 auditor's report repeats the Rule 11(g) qualification | FY27 audit report |
| Receivables/cash-conversion stretch | Medium | Customer-level ageing and terms once obtainable; whether the >6-months bucket reverses its current improving trend | Ongoing, next 1-2 quarters |
| Warrant-proceeds utilisation shortfall | Low-Medium | Whether the deviation statement narrows and gains category-level disclosure | Next deviation statement filing |

### D. FIVE QUESTIONS FOR MANAGEMENT

1. What is the accounting basis for the "Changes in Working Capital Facilities" line introduced in the FY26 cash flow statement and applied retroactively to the FY25 comparative, and why does it not appear in the H1 FY26 refiled results or the FY25 Annual Report?
2. What purchase consideration and fair-value-of-net-assets computation underlie the ₹502.78L consolidation goodwill increase from the Trident Mediquip stake changes, and why is there no goodwill note in the AR?
3. What is the commercial nature, counterparty, and legal basis of the "Claim Income" line (₹541.05L FY26, ₹522.17L FY25) inside Other Income?
4. Why does the Note 31 segment-assets-by-geography receivables total reconcile to the standalone book rather than the consolidated Group receivables, and why does "Shareholders Funds" in the Ratio Analysis Note not match the Balance-Sheet-derived net worth in FY26?
5. What is the business rationale and exit plan for the corporate guarantees extended to Talon Healthcare LLP and Tench Life Sciences LLP, entities the company does not consolidate or control?

### E. NOTES-BASED RED FLAGS

- **Earnings management signal**: undisclosed, retroactive cash-flow reclassification ("Changes in Working Capital Facilities") that flatters operating cash generation in both the current and comparative year, introduced only at the annual-audit stage and absent from the interim filing.
- **Aggressive accounting**: no impairment recognised against a negative-net-worth, loss-making subsidiary (TNS Pharma) into which the company added further capital during the year the losses widened.
- **Undisclosed risk indicator**: corporate guarantees for two non-consolidated, director-interest LLPs, disclosed only as a contingent-liability quantum with no qualitative business rationale.
- **Disclosure gap pattern**: three separate cross-note number mismatches in the same AR (segment receivables vs balance sheet, Shareholders Funds ratio denominator vs balance sheet, and the undisclosed cash-flow line) point to a consolidation/reporting-systems weakness, consistent with the auditor's own KAM #2 naming a "DOS based accounting system" needing strengthening.

### F. ONE-LINE NOTES VERDICT

The notes reveal concerning accounting practices. Key concern: an undisclosed, retroactive cash-flow reclassification inflates reported operating cash generation alongside three unreconciled cross-note figures and a fully unexplained goodwill jump. Key strength: no restatements, no going-concern issue, clean MSME/CSR/warrant mechanics, and the company's own ratio-analysis data support a growth-induced (not purely structural) reading of the working-capital stretch. Overall accounting quality: 4/10.

---
Pipeline note: this file is Pass 3 (pattern pass + consolidated analysis), combining Pass 1 (outputs/reports/02-notes-pass1.md) and Pass 2 (outputs/reports/02-notes-pass2.md) per the 02-notes-triple-pass-pipeline.md instruction. The final B02-notes YAML block is written separately at outputs/blocks/B02-notes.yaml.
