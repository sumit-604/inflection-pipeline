# VOEPL - Virtuoso Optoelectronics Ltd
## Sources read
- companies/VOEPL.md (origin/claude/baluforge-2026-09-06-runs-ah784w, on_main no)
- runs/voepl-2026-07-18/manifest.yaml (302 branches, on_main yes)
- runs/voepl-2026-07-18/outputs/blocks/B11-valuation.yaml, B13-synthesis.yaml, B14-thesis.yaml, B15-devil.yaml; B01, B05, B08, B10 by grep (on_main yes)
- runs/voepl-2026-07-18/outputs/reports/B11-valuation.md (lines 160-195 plus grep) (on_main yes)
- runs/voepl-2026-07-18/outputs/final/fttcp-recommendation.md (on_main yes)
- runs/voepl-2026-09-06/manifest.yaml; work/text/concalls__Concall_Aug_2026_Transcript.txt (grep) (153 branches, on_main yes)
- retro/2026-11/excerpts/sessions/VOEPL.md (five excerpts, 2026-09-06 to 2026-10-09)
- retro/2026-11/excerpts/local/VOEPL.md (local-folder excerpts; retro/2026-11/excerpts/local/VOEPL.md does not exist)

## Company-level facts
- board (main): "Mainboard migration (BSE SME to BSE Mainboard, effective 1-Jul-2026, 99.81% postal-ballot approval Nov-2025) forces full SEBI LODR governance scope" - runs/voepl-2026-07-18/outputs/blocks/B08-promoter.yaml:24; "mainboard migration effective 1-Jul-2026 forcing full LODR (B08)" - outputs/final/fttcp-recommendation.md:53; "prospectus (SME-DRHP ~2022) absent" - outputs/blocks/B13-synthesis.yaml:28
- reporting (quarterly): `quarters_analysed: ["Q2 FY26", "Q3 FY26", "Q4 FY26"]` - outputs/blocks/B05-concall.yaml:11; "# Virtuoso Optoelectronics — Q1 FY27 Post-Earnings Call Transcript" - C:/ConcallPipeline/Daily Concall Intelligence\analysis\.workspace\feed_2026-08-21_1322\Virtuoso_Optoelectronics_results.md (retro/2026-11/excerpts/local/VOEPL.md:179)
- archetype: `sector_cap_row: "Agri processing"` - runs/voepl-2026-07-18/manifest.yaml:8; "sector_cap_row: manifest 'Agri processing' is a collector defect" - outputs/blocks/B13-synthesis.yaml:27; `sector_cap_row: "Cables / Industrial products"` - runs/voepl-2026-09-06/manifest.yaml:8; `flag_gate0: "AVOID 55/160 (core 45, moat 10); ..."` - B13-synthesis.yaml:13; `headline: "AC contract maker bets on compressors"` - B13-synthesis.yaml:18
- first analysis: `run_date: 2026-07-18` - runs/voepl-2026-07-18/manifest.yaml:5
- verdict: `verdict: "PROCEED WITH FLAGS"` - outputs/blocks/B13-synthesis.yaml:7; "AVOID (on valuation)." - outputs/final/fttcp-recommendation.md:9; `verdict: "AVOID"` - outputs/blocks/B14-thesis.yaml:6
- later status in memory file: "NOT YET WRITTEN. No run has reached /finalize for this ticker." - companies/VOEPL.md:4; "Spear: OVERRIDE 2026-09-06 (operator)" - companies/VOEPL.md:11

## Q4 FY26
- base case: NOT FOUND (first analysis 2026-07-18 is after the FY26 result; "audited Q4 FY26 results board approval 29-May-2026" - outputs/blocks/B10-valinputs.yaml:40)
- guidance: `{item: "FY26 revenue", number: "900-1100cr (baseline) -> revised 800-900cr -> delivered 823cr", timeframe: "FY26", stated_in: "FY25 call -> Q2 FY26 call -> Q4 FY26 call"}` - outputs/blocks/B05-concall.yaml:22; "FY26 EBITDA margin ... 8.5-9% guided -> 10.4% delivered" - B05-concall.yaml:23; "FY26 PAT margin ... 2.5-3% guided -> 1.8% delivered" - B05-concall.yaml:24
- catalysts: `promise: "Chennai AC plant commercial production by end of Q4 FY26", outcome: "missed", explanation: "pushed to Q1 FY27, reframed rather than owned as a slip"` - B05-concall.yaml:48; `promise: "Mainboard listing filed by end of Nov-2025, listed in 2-4 months", outcome: "missed"` - B05-concall.yaml:52
- actuals: "| Revenue (Rs Cr) | 823.6 | 1,226 | 1,824 |", "| PAT (Rs Cr) | 15.03 | ~34 | 51.1 |" (FY26 column) - outputs/reports/B11-valuation.md:190-191; `ebitda_margin_pct: 10.4` - outputs/blocks/B10-valinputs.yaml:43. Q4 quarter alone: NOT FOUND (Q1 call: "it's a 19%, 18.7% to be precise kind of a jump on the revenue number" vs Q4 FY26 - retro/2026-11/excerpts/local/VOEPL.md:186)
- result vs base: NO BASELINE
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND (no analysis predates the result)

## Q1 FY27
- base case: FY27E figure NOT FOUND. "| Revenue CAGR (FY26-FY30) | 14% | 22% | 26% |" - outputs/reports/B11-valuation.md:169; "| Revenue (Rs Cr) | 823.6 | 1,226 | 1,824 |" (FY26 / FY28 / FY30) - B11-valuation.md:190; "| PAT (Rs Cr) | 15.03 | ~34 | 51.1 |" - B11-valuation.md:191; base logic "Compressor + AC ramp deliver, mgmt guidance discounted for grade B" - B11-valuation.md:168
- guidance: `{item: "FY27 revenue growth", number: "35-40% CAGR on 825cr base (~1100-1155cr), diluted from informal 2000cr target", timeframe: "FY27", stated_in: "Q2 FY26 call reference -> Q4 FY26 call"}` - outputs/blocks/B05-concall.yaml:31
- catalysts: "Compressor commissioning around March 2027 and utilisation crossing 60% to 80%, FY27 compressor revenue near Rs200 Cr at about 50% utilisation" - outputs/final/fttcp-recommendation.md:77; [holding detail removed]; EMS "phase 1 completion within 3 months of Q4 FY26 call (~Sep-2026) as promised" - B05-concall.yaml:17
- actuals: "the company has been able to achieve INR 376.6 crores worth of" - runs/voepl-2026-09-06/work/text/concalls__Concall_Aug_2026_Transcript.txt:97; "it with the Q4 of FY26, 9.3%-odd." - same file:103; "rather, Q1 FY26 number, we have moved to a INR9 crore number this" - same file:109
- result vs base: BASELINE NOT COMPARABLE (no same-period base figure; no file states a comparison). "Q1 FY27 results not logged in Notion, so H2 revenue needed for the Rs1,100-1,155 Cr guide cannot be computed" - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-10-30_0500_to_2026-10-31_0807\deep\out\T20.md (retro/2026-11/excerpts/local/VOEPL.md:238)
- management's stated reason: NOT FOUND
- risk flagged before / by whom / overruled: NOT FOUND
- note on the PAT quote: "the two figures imply ~+40%, transcript is internally inconsistent — verify against the filed results." - feed_2026-08-21_1322\Virtuoso_Optoelectronics_results.md (retro/2026-11/excerpts/local/VOEPL.md:188)

## Q2/H1 FY27
- base case: FY27E figure NOT FOUND (same lines as Q1) - outputs/reports/B11-valuation.md:169, 190-191
- guidance: "Hemant Sood: So, as of now, sir, we are sticking to our guidance of 35% to 40% in" - runs/voepl-2026-09-06/work/text/concalls__Concall_Aug_2026_Transcript.txt:431; "9% to 10% is the guidance that we gave, and we continue to be on that guidance" - retro/2026-11/excerpts/local/VOEPL.md:189
- catalysts: "EMS capacity live ~December 2026; compressors 2.8M→6M units by end FY27 (Q4); utilisation of existing compressors ~70–75%." - C:/ConcallPipeline/Daily Concall Intelligence\analysis\2026-11-09_evening.md (retro/2026-11/excerpts/local/VOEPL.md:217); "non-binding Memorandum of Understanding (\"MOU\") with Government of Maharashtra for proposed investment of Rs. 1050 Cr. ... tentatively planned over the next 5 years." - retro/2026-11/excerpts/local/VOEPL.md:40
- actuals: revenue, margin, PAT NOT FOUND. "Trigger 1 (H1 CFO -₹105.84 Cr) still not on the record." - C:/ConcallPipeline/Daily Concall Intelligence\announcements\2026-11-10_0500_to_2026-11-11_0500\deep\out\T08.md (retro/2026-11/excerpts/local/VOEPL.md:278)
- result vs base: MISS, file-stated. "Log the 6-Nov H1 results (CFO minus ₹105.84 Cr; 7-Nov review said trigger 1 fires as written) in Key Notes now, or wait for the carried WC-days-leg ruling?" - same T08.md (retro/2026-11/excerpts/local/VOEPL.md:281). Trigger wording: `thesis_broken_if: "H1 FY27 CFO/PAT below 0.5x with working capital days expanding, OR first FY27 ROCE fails to clear the FY25 trough of 17.19% ..."` - outputs/blocks/B14-thesis.yaml:10
- management's stated reason: NOT FOUND
- risk flagged before: YES. "Cash reality contradicts the STARTING override: FY26 CFO/PAT 0.22x, negative FCF, no documented WC program ... falsifier H1 FY27 CFO/PAT <0.5x flips the tag structural (0.65x)." - runs/voepl-2026-07-18/outputs/blocks/B15-devil.yaml:15; "The single most damaging next-quarter print: H1 FY27 CFO/PAT below 0.5x with working capital days expanding." - outputs/final/fttcp-recommendation.md:86
- by whom: Stage 15 devil's advocate (B15-devil); Stage 13 synthesis FLAG-CASH falsifier; Stage 14 thesis tripwire
- overruled: YES for the earlier cash score. "The +4 FTTCP composite and the whole investable-business leg rest on two one-sentence operator overrides ('I think ROC is recovering'; 'cash is also improving'); the autonomous draft scored both STAGNANT (+2 composite)." - outputs/blocks/B15-devil.yaml:14. The H1 falsifier itself was carried into the final recommendation (fttcp-recommendation.md:86)
- related later facts: "₹85 Cr raised at ₹503 from ICICI Pru + Clarus; 4.93% dilution" - announcements\2026-10-15_1056_to_2026-10-16_0643\deep\out\T05.md (retro/2026-11/excerpts/local/VOEPL.md:224); "The non-binding Maharashtra MOU is Rs 1,050 Cr, about 62% of market cap." - session 2026-10-05 bda01a5f-072d-4017-a4fe-08e0f47f1458.jsonl (retro/2026-11/excerpts/sessions/VOEPL.md:37)

## Not found
- FY27E base revenue, margin, PAT (base table gives FY26, FY28, FY30 only)
- Q4 FY26 quarter-only revenue and PAT
- Q2/H1 FY27 revenue, margin, PAT
- mgmt_reason (all periods)
- listed_date (blank in runs/voepl-2026-09-06/manifest.yaml:9)
- promoter pledge % ("NOT FOUND (BSE/screener 403)" - B13-synthesis.yaml:29)
