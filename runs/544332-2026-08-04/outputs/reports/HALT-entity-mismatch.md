# PIPELINE HALT — WRONG-ENTITY DOCUMENT CONTAMINATION

**Run:** 544332-2026-08-04 | **Target per manifest:** Fabtech Technologies Cleanrooms Ltd (BSE 544332 / FABCLEAN)
**Discovered:** Stage 1 (Gate 0), confirmed by orchestrator direct read + Stage 2 Pass 1.
**Nature:** Mechanical input-collection failure. `collect_to_repo.py v3` placed a DIFFERENT listed company's
filings (Fabtech Technologies Limited, BSE 544558 / NSE FABTECH — the related parent/sibling in the Fabtech
group) into the annual-report/, results/, rating/, and most presentation/ slots. Screener export and concalls
are correctly the target's.

## Entity verification (from the documents themselves)

| Document set | Entity string found | Ticker/scrip | FY26 scale | Target 544332? |
|---|---|---|---|---|
| screening/screener-*.csv | FABTECH TECHNOLOGIES CLEANROOMS LTD (Data_Sheet header; CMP 391.5, mcap 482.3) | 544332 | Sales 219.32cr | YES |
| concalls/ (all 3) | Fabtech Technologies Cleanrooms Limited | Scrip 544332 / Symbol FABCLEAN | TI ~221cr FY26, ~143cr FY25 | YES |
| presentation/Investor_Presentation_1.pdf | Fabtech Technologies Cleanrooms Limited | Symbol FABCLEAN | — | YES |
| annual-report/ (the 224pp AR) | Fabtech Technologies Limited (AGM notice) | Symbol FABTECH / Scrip 544558 | — | NO |
| results/ (both filings) | Fabtech Technologies Limited | Symbol FABTECH / Scrip 544558 | — | NO |
| rating/ratings.pdf (CRISIL) | Fabtech Technologies Limited (FTL, part of Fabtech group) | 544558 / group | FY25 224cr | NO |
| presentation/*IPO note* (3 files) | Fabtech Technologies Limited | 544558 (also sell-side, non-anchored) | — | NO |
| peer-concalls/, peer screeners | ANUP / GMMPFAUDLR / HLEGLAS / PRAJIND | external | — | peers, fine |

**Cross-proof the AR is FTL not Cleanrooms:** FTL's own AR Notes list "Fabtech Technologies Cleanrooms Limited"
as a RELATED PARTY (standalone purchases from Cleanrooms Rs 1,812.56 lakh FY26; corporate guarantee of
Rs 1,000 lakh given TO Cleanrooms as an external, non-consolidated counterparty). Cleanrooms is therefore a
separate entity from the AR's filer. Financial magnitudes also irreconcilable (target FY25 standalone sales:
screener 150.03cr vs FTL AR 236.42cr).

Note: two separate group IPOs occurred around Oct 2025 (FTL raised ~Rs 230cr per CRISIL; the target Cleanrooms
listed separately as FABCLEAN). The operator's mid-run announcements summary (FY26 total income 431cr) is
FTL/group scale, not the target's ~221cr — it is FTL-flavoured and stays non-anchored.

## Stage outputs status at halt
- B00 (inputs): valid; updated to reflect contamination.
- B01 (Gate 0): VALID for the target — Stage 1 correctly used screener CSVs only and excluded the wrong PDFs.
  (Core 38/100, Moat 15/60, Grand 53/160, classification AVOID on the Core<40 floor; Block E unscored for lack
  of SHP data — operator screener screenshot can inform a rescore.)
- B02 Pass 1 (Notes): INVALID — read the wrong entity's (FTL 544558) annual report. Must be discarded and
  redone against the correct-entity AR once supplied. Preserved as B02-pass1.md but marked wrong-entity.

## Required decision (operator)
Correct-entity primary sources currently available for the target are ONLY: screener CSVs + 3 concalls +
Investor_Presentation_1.pdf. No correct-entity AR, results filing, rating, prospectus, or SHP filing is present.
Options presented to operator via the pipeline's escalation. Pipeline paused pending direction.
