INPUT FOLDER CONTRACT
=====================

Inputs are identified BY FOLDER, not by filename. Drop files into the
matching subfolder using any filenames you like; the pipeline reads
whatever it finds in each folder.

Required (run halts if the folder is empty or the count is wrong):
  annual-report/    1 PDF
  results/          2 or 3 PDFs
  rating/           1 PDF        (any agency)
  concalls/         3 PDFs       -- required ONLY when the manifest sets
                                    concalls_available: true

Optional (recorded as input_gaps if absent):
  peer-concalls/    0-12 PDFs
  screening/        csv / txt / pdf / xlsx
  presentation/     1 PDF

THE concalls_available FLAG
---------------------------
manifest.yaml carries `concalls_available`. Set it false for companies
that hold no earnings calls. When it is false, the concalls/ folder is
not required and the pipeline runs in NO-CONCALL MODE: stage 5 reads the
annual report's MD&A, chairman's letter, and results commentary instead
of transcripts, and the credibility grade caps at B. Leave it true for
companies that do hold calls; then concalls/ must contain exactly 3 PDFs.

FILE SIZE / SPLIT-AR NOTE
-------------------------
GitHub web upload limit is 25MB per file. If an annual report exceeds it,
split it (any online PDF splitter) into two parts and place both PDFs in
annual-report/ (any filenames, e.g. -part1 / -part2).
