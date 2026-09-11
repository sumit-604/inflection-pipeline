# Re-extraction, 11-Sep-2026 — six shallow cards

Raised by Claude web after three cards failed live verification. Extraction
only. No card was re-graded or edited in this pass.

Note on the run folder: the prompt named `runs/company-shallow-analysis-y3r9le`.
No such folder exists. The corpus is `screens/corpus/<TICKER>/`, and it holds
only markdown extracts, no PDFs. This pass re-read the SOURCE documents through
Bull AI's chunk reader rather than re-quoting the earlier extract files.

## Material differences found against the original cards

| Company | Item | Original card | Re-extracted | Source |
|---|---|---|---|---|
| WENDT | Latest result held | "no result filed since April 2026" | Q1 FY27, quarter ended 30-Jun-2026, filed 24-Jul-2026 | docs.bull-ai.in/d/xBuREI p3-p6 |
| WENDT | Most recent quarter profit | "profit fell 63%" | Consolidated profit ROSE, 618 vs 378 lakhs, +63.5% | xBuREI p5 |
| WENDT | Machines & Accessories | loss-making | Still loss-making but narrowing: (149) vs (330) | xBuREI p6 |
| PANORAMA | Bonus ratio | "2:5" | FY26 filing note 4 says "2.5"; Q1 FY27 filing note 5 says "2:5". The two filings conflict | Vw2djB p2 note 4; 3d4U8O p2 note 5 |
| PANORAMA | Bonus share of capital rise | "about Rs 5.7 cr of a Rs 37.9 cr increase" | Under the "2.5" reading the bonus accounts for Rs 35.47 cr of Rs 37.92 cr | CALCULATED from Vw2djB p2 |
| PANORAMA | Operating cash flow | INDETERMINATE, none held | FY26 (605.14) lakhs; FY25 (1,636.66) lakhs, both negative | Vw2djB p4 |
| PANORAMA | FY26 direction | implied growth | FY26 standalone revenue FELL 14.3% and PAT FELL 45.7% vs FY25 | Vw2djB p2 |
| PANORAMA | Dividend | "no dividend in any period shown" | FY25 final dividend Rs 0.20 per share was paid | Vw2djB p2 |
| KROSS | Corpus cut-off | card closed at 25-Jul-2026 deck | Five later filings indexed, incl. Issue of Securities 31-Aug-2026; all return zero text | availability map |
| KROSS | Operating cash flow | INDETERMINATE, none held | FY25 (320.59) Mn NEGATIVE; FY24 82.51 Mn positive | z1K1jZ p58 |
| KROSS | Anita Rai | "sits on a board committee" | Whole Time Director, DIN 00513329 | z1K1jZ p57 |
| EMIL | FY26 context | not shown | FY26 standalone PAT 1,071.80 Mn vs FY25 1,605.21 Mn, a 33% FALL | STo5eH p5 |
| EMIL | Q1 FY26 base | "8.2 exceptional charge" unexplained | Godown fire 29-May-2025, inventory written off Rs 81.72 Mn | SrXLQc p5 note 5 |
| EMIL | June-2026 quarter transcript | implied available | No transcript exists for that quarter; latest call is Q4 FY26 | availability map |

## Extractor defects recorded this pass

- KROSS Q1 FY27 deck page 4: fabricated dollar-denominated metrics table with
  North America / Europe / Asia-Pacific splits. Rejected in the original run.
- WENDT Q1 FY27 results page 4 and 6: Company Secretary shown as "S Jagadeesh",
  which is also the digital-signature name of the Price Waterhouse audit
  partner Jagadeesh Sridharan on page 7. Probable signature mis-attribution.
- EMIL Q1 FY27 consolidated page 8: email printed "communications@baaniel.com"
  against "communications@bajajelectronics.in" everywhere else.
- EMIL Q1 FY27 standalone page 4: fourth column headed "31.03.2025 (Audited)"
  carries 71,832.62, which is the FY26 figure. The consolidated table heads the
  same column "31.03.2026". Header is wrong on the standalone table.
- KROSS Q1 FY27 transcript page 5: steel settlement quoted as "INR4,700 per
  kilo". Implausible for steel; per tonne is the plausible unit. Not used.
- Nine documents are indexed but return zero text: KROSS Issue of Securities
  (p24Y1p), KROSS Outcome of Board Meeting (EKuHbE), KROSS Shareholders meeting
  (iAjTEn), KROSS Updates (NuRBmT), KROSS FY26 Annual Report (HPJbCy), WENDT
  Outcome of Board Meeting (Pzj42B), PANORAMA EGM (65kfAB), PANORAMA Reg. 31
  SAST (oqPdWB), PANORAMA Outcome of Board Meeting (7P0DOl).
- `search_company_documents` was unavailable for this entire session, a second
  consecutive day.
