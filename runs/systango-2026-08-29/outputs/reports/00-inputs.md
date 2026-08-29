# B00 — INPUT VALIDATION & CORPUS AUDIT

Company: Systango Technologies Ltd (SYSTANGO)
Run date: 2026-08-29 | Run type: full | CMP Rs 234 | m-cap Rs 343 cr
Sector cap row: Platform / SaaS / IT services (45x) [corrected from auto-picked "Pharma / CDMO" 38x, operator 2026-08-29]
manifest.yaml: present, parses.

## SPEAR GATE
Spear: HIT 2026-08-29 (entry <= Rs 210). Gate cleared. Load-bearing facts carried as first verification priority for every stage:
- [1] Guidance-vs-delivery POOR on revenue: guided 30% FY24 growth (H1FY24 concall 17-Nov-2023) and Rs 250 cr / $25M by FY26 (FY23 concall 7-Jul-2023); delivered 8% and Rs 90.4 cr. Only EBITDA >25% kept.
- [2] Rs 5.3 cr loans to unnamed "Others", unsecured, repayable on demand, 100% no repayment schedule per CARO (AR FY25); new Rs 2.4 cr long-term loans & advances FY26 BS. Recipients unidentified.
- [3] Gratuity and leave encashment NOT provided, payment-basis only (AR FY23 policy, carried forward); profits overstated vs accrual, quantum unknown.
- [4] Top-3 client concentration ~46-48% in H1FY26 (Nov-2025 deck) as margins spiked to 42%; H2FY26 EBITDA margin fell to 33.1%. FY26 AR must confirm concentration, consolidated CFO, other-income breakup, DBX Holdings identity.

## FOLDER INVENTORY
| Folder | Count | Files / note |
|---|---|---|
| prospectus/ | 0 | ABSENT — HIGH gap (listed ~Jul-2023, within ~3y) |
| annual-report/ | 1 | Annual_Report_2023.pdf is MISLABELED — actually the FY2024-25 AR (21st AR, year ended 31-Mar-2025, auditor 26-May-2025), 121pp. Carries CARO, related-party, contingent-liab, promoter shareholding (31-Mar-2025). FY26 AR absent. [corrected from stage 1 read] |
| results/ | 2 | Nov-2025 (H1FY26 board outcome, 13pp); May-2026 (FY26 audited full-year + H2, Rs 7 interim div) |
| rating/ | 0 | ABSENT |
| concalls/ | 3 | 2 unique calls (see chronology); newest Nov-2023 |
| peer-concalls/ | 12 | INFOBEAN x4, KSOLVES x4, ONWARDTEC x4 |
| announcements/ | 0 | ABSENT (dedicated folder); some Reg-30 intimations sit in results/ and presentation/ |
| shareholding/ | 0 | ABSENT; operator-supplied screener figures logged as NON-ANCHORED lead |
| research/ | 0 | ABSENT (.gitkeep planted) |
| screening/ | 6+18 | screener-*.csv (SYSTANGO) + peer CSVs (INFOBEAN, KSOLVES, ONWARDTEC, YUDIZ) |
| presentation/ | 2 | June-2026 Annual Update deck (32pp, FY26 headline data) x2 copies |
| other/ | 0 | none |

## CONCALL QUARTER MAP (chronology confirmed, oldest first)
1. Concall_Jul_2023_Transcript.pdf — FY23 annual earnings call, held 7-Jul-2023, year ended 31-Mar-2023. Cover page 1, transcript pp 2-19.
2. Concall_Nov_2023_Transcript_2.pdf — H1FY24 earnings call, held 17-Nov-2023, half ended 30-Sep-2023. Full transcript (17pp).
   - Concall_Nov_2023_Transcript.pdf (18pp) is the intimation+transcript of the SAME H1FY24 call. DUPLICATE of #2; do not double-count.

## FRESHNESS PAIR CHECK
| # | Pair | Trigger doc | Mate expected | Status | Missing |
|---|---|---|---|---|---|
| 1 | Results -> Concall | FY26 audited results (14-May-2026) | Q4FY26/FY26 concall | FAIL | FY26 concall transcript |
| 2 | Rating bulletin -> Rationale | none present | n/a | PASS (no trigger) | - |
| 3 | SEBI order -> Order text | none referenced | n/a | PASS (no trigger) | - |
| 4 | AR -> Latest audited annual | FY26 audited annual results | matching-year AR | FAIL | FY26 Annual Report (held AR is FY25, one year behind the FY26 audited results) |

freshness_verdict: CORPUS GAPPED-FRESHNESS (pairs 1 and 4 FAIL).
AR-YEAR CORRECTION (stage 1): the sole AR is the FY2024-25 report, not FY2023. Backward baseline is 4 audited years with full notes, not post-listing-only. FY26 financial DEPTH (CARO loans movement, related-party, consolidated CFO, DBX Holdings, client concentration) is still unresolvable until the FY26 AR is pushed; FY26 HEADLINE numbers are anchored in the May-2026 audited results + June-2026 deck.
Effect: gate recommendation capped at PROCEED WITH CAVEATS; missing mates (FY26 concall, FY26 AR) named as first line of gate-recommendation.md and first upload priority at Halt 1.

## OPERATOR-SUPPLIED LEADS (NON-ANCHORED, weigh never anchor)
- Shareholding (screener, Mar-2026): Promoter 72.17%, FII 0.47%, DII 1.69%, Public 25.67%, 2,637 holders. FII+DII 2.16% (<3%, UA qualifier would pass at stage 11). Not a filed source; stage 10 marks FII+DII unresolved until filed pattern pushed.
- ValuePickr thread (https://forum.valuepickr.com/t/systango-technologies-ltd/150052): routed to stage 8 as a lead to chase DBX Holdings, loans-to-Others recipients, promoter record; flagged for Halt-1 live verification. Never anchored.

## DEGRADATION (per DEGRADATION MAP)
- No FY26 AR: stages 2/3 build notes and backward history from the FY25 AR (4 audited years, full notes incl. CARO/related-party); FTTCP backward baseline runs FY23-FY26 post-listing and says so. FY26 notes-level depth comes from May-2026 audited results + June-2026 deck until the FY26 AR is pushed.
- No prospectus (recently listed): stage 8 sources promoter/group background from web + AR governance, flags group-map as web-derived not filing-anchored.
- No rating: stage 10 marks rating_wc_quote unresolved; Pillar 2 defaults conservative.
- No announcements folder: intent-and-action cross-check runs on concall/AR/deck evidence; stage 8 relies on web for material events.
- No shareholding filing: stage 10 marks FII+DII unresolved; UA withheld unless a filed source appears; promoter/pledge from screener lead noted stale.

```yaml
stage: B00-inputs
company: SYSTANGO
run_date: 2026-08-29
model: orchestrator-inline
status: complete
sector_cap_row: "Platform / SaaS / IT services"
sector_cap_x: 45
spear: "HIT 2026-08-29 entry<=210"
spear_facts_priority: 4
input_gaps:
  - prospectus (HIGH; listed ~Jul-2023)
  - annual-report-FY24
  - annual-report-FY25
  - annual-report-FY26 (HIGH; freshness pair 4)
  - concall-FY26 (HIGH; freshness pair 1)
  - rating
  - announcements-folder
  - shareholding-filing
  - research
freshness_pairs:
  - {pair: results-to-concall, trigger_doc: "FY26 audited results 2026-05-14", mate_expected: "FY26/Q4 concall", status: FAIL, missing_doc: "FY26 concall transcript"}
  - {pair: rating-bulletin-to-rationale, trigger_doc: none, mate_expected: n/a, status: PASS, missing_doc: null}
  - {pair: sebi-order-to-text, trigger_doc: none, mate_expected: n/a, status: PASS, missing_doc: null}
  - {pair: ar-to-latest-audited-annual, trigger_doc: "FY26 audited annual results", mate_expected: "FY26 AR", status: FAIL, missing_doc: "FY26 Annual Report"}
freshness_verdict: CORPUS GAPPED-FRESHNESS
concall_map:
  - {order: 1, file: Concall_Jul_2023_Transcript.pdf, period: FY23-annual, held: 2023-07-07}
  - {order: 2, file: Concall_Nov_2023_Transcript_2.pdf, period: H1FY24, held: 2023-11-17}
  - {duplicate: Concall_Nov_2023_Transcript.pdf, of: Concall_Nov_2023_Transcript_2.pdf}
concalls_available: true
non_anchored_leads:
  - {type: shareholding-screener, source: operator-paste, mar2026: "Promoter 72.17 / FII 0.47 / DII 1.69 / Public 25.67", holders: 2637}
  - {type: valuepickr-thread, url: "forum.valuepickr.com/t/systango-technologies-ltd/150052", routed_to: stage-08, halt1_verify: true}
flags: []
analyst_note: "Corpus jumps from Nov-2023 to FY26 results; the 2.5-year concall gap and absent FY26 AR are the binding limits. FY26 headline financials are anchored in the June-2026 deck and May-2026 audited results, so Gate 0 and the evidence stages run for real; only the notes-level FY26 depth (CARO loans, related-party, consolidated CFO, DBX Holdings) is unresolvable until the FY26 AR is pushed."
```
