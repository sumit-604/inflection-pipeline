# Notion payload: FAIRCHEMOR Q2 FY27 (NOT WRITTEN)

Status: NOT WRITTEN. The session instruction says do not write to Notion; print the payload and stop for the operator's approval. A5 is COMPLETE (iteration 2), so the write gate would otherwise allow it on approval.
Decision Status: never written by /run-quarterly. No page exists, so no Decision Status exists.

## Target
- Database: COMPANIES MASTER (collection://345bb2b9-d3ab-8032-9b46-000ba16ab827)
- Page: NONE EXISTS. Notion search "Fairchem Organics" on 2026-10-23 returned no page. The operator creates the page, or claude.ai does on approval. Proposed title: "Fairchem Organics Ltd (FAIRCHEMOR)".

## Properties
- Key Notes (prepend; no prior entries exist):
  2026-10-24 | Q2 FY27 pre-thesis read (results + deck + ASR concall): rev 166.92 Cr +49.7% YoY price-led, volume -8.9% QoQ [ASR], op EBITDA margin 10.51% (FY24 peak 10.78%), H1 ex-release FCF -2.78 Cr, FY26 buyback debt-funded on filed totals, Rs 12.01 Cr land from CMD and relatives with no valuer (land already in use per call) | PROCEED WITH FLAGS | A5 COMPLETE (loop 2)
- Decision Status: DO NOT WRITE.

## Content (insert_content, position: end, split across sequential inserts)
1. Full A4 review, verbatim, all tables, ending with the PLAIN-LANGUAGE BRIEF:
   runs/fairchemor-q2fy27/work/review_fairchemor_q2fy27.md (escape | inside cells as \|)
2. A3 forensics tables, verbatim:
   runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_results.md (F1-F17, A3-01..A3-14)
   runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_presentation.md (F1-F17, A3P-01..A3P-21)
   runs/fairchemor-q2fy27/work/forensics_fairchemor_q2fy27_concall.md (F1-F17, A3C-01..A3C-19)
3. A5 audit verdict block:
   COMPLETE after loop iteration 2. Iteration 0: FACTUAL 1, MISSING 4, CONTRADICTION 2, all closed in loop 1. Iteration 1: C3 (buyback funding) and F2 (land attribution), closed in loop 2. Arithmetic mismatches: 0. Orphan rows: 0. STYLE S1-S10 logged.
   Source: runs/fairchemor-q2fy27/work/audit_fairchemor_q2fy27.md

## Flags for the Key Notes reader
- Land RPT Rs 12.01 Cr from the CMD and relatives; no valuer; split between sellers and prior-use terms NOT FOUND; CMD look-through stake 6.07%.
- Cash conversion INDETERMINATE-WITH-DIRECTION: CFO/PAT 1.19x rests on a 22.31 Cr inventory release.
- Buyback at Rs 800 funded by bank debt (H2 FY26 liabilities +33.60 Cr, equity -31.00 Cr).
- Concall is machine-transcribed; about 22% of audio in gaps; rerun A1-A3 if a transcript is filed.
- No spear on record: /step1 before any pipeline run.
