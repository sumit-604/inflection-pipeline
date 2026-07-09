Inputs are identified by SUBFOLDER, not by filename. Files inside each
folder may have any filename; the pipeline reads them by folder.

Required (run halts if a folder is missing or holds the wrong count):
  annual-report/   exactly 1 PDF
  results/         2 or 3 PDFs (both counts pass)
  rating/          exactly 1 PDF (any agency)
  concalls/        exactly 3 PDFs, main company
                   Required ONLY when manifest.yaml has
                   concalls_available: true. Set that flag to false for
                   companies that hold no earnings calls; then concalls/
                   may be empty and the run proceeds in no-concall mode
                   (stage 5 reads the AR MD&A, chairman's letter, and
                   results commentary instead of transcripts).

Optional (recorded as input_gaps if the folder is empty or absent):
  peer-concalls/   0-12 PDFs
  screening/       any csv / txt / pdf / xlsx
  presentation/    1 PDF

GitHub web upload limit is 25MB per file. If an AR exceeds it, split it
(any online PDF splitter) into two parts and drop both into
annual-report/.
