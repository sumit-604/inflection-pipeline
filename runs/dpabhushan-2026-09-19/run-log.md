# RUN LOG — DPABHUSHAN 2026-09-19

- stage 0: run inline by the orchestrator (step1). Peer set changed at intake: THANGAMAYL -> MOTISONS (no transcripts).
- stage 1 + stage 2 pass 1: ran on -layout text that interleaved FY26 AR spread tables. All inputs re-extracted with pdftotext -table and spread pages split into halves. Stage 1 re-invoked (SendMessage) on corrected text; pass 2 told to re-read pass 1's garbled items.
- stage 2 pass 3: reply omitted the YAML block; B02-notes.yaml exists and parses. File governs.
- stage 5: reply omitted the YAML block; B05-concall.yaml exists and parses. File governs.
- stage 6 run 1: found the four MOTISONS-* peer transcripts were RBZ Jewellers (orchestrator used wrong BSE scrip 544060; Motisons is 544053 and has held no call since Jun-2024). Peer replaced by KALYANKJIL (4 BSE transcripts Q2 FY26-Q1 FY27). RBZ files moved to inputs/other/rbz-mislabeled/. Run-1 outputs kept as outputs/reports/06-peers-run1-superseded.md and B06-peers-run1-superseded.yaml (not a block; never consumed). Stage 6 re-run.
- stage 7: reply omitted the YAML block; B07-emoat.yaml exists and parses. File governs.
- stage 7: block file had two flag flow-mappings missing the closing brace; orchestrator added the braces (content unchanged), now parses.
