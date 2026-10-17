cd "C:/Users/SUMIT SHARMA/repos/inflection-pipeline/.claude/worktrees/q2fy27/runs/indorama-q2fy27"
W=work/a1-results
S=extracted/indorama-results-q2fy27-structured.md
cat $W/numA.txt $W/numB.txt | awk 'NF' > $W/numall.txt
N=$(wc -l < $W/numall.txt); E=$(wc -l < $W/ent.txt); F=$(wc -l < $W/fwd.txt); D=$(wc -l < $W/date.txt); Q=$(wc -l < $W/qual.txt)
T=$((N+E+F+D+Q))
{
echo "# A1 STRUCTURED EXTRACTION: Indo Rama Synthetics (India) Ltd (INDORAMA), Q2 FY27, results filing"
echo "source fulltext: runs/indorama-q2fy27/extracted/indorama-results-q2fy27-fulltext.md (line numbers refer to that file, header included)"
printf "ID range: R001-R%03d\n" $T
echo "counts: NUMBER $N | ENTITY $E | FORWARD $F | DATE $D | QUALIFIER $Q"
echo "unit: Rs crores (x1); EPS in Rs; parentheses = negatives. Text layer is OCR; pages 3 and 9 P&L tables are garbled, so period attribution for some values is positional and marked in context. Board Outcome letter has agenda items a and b only, both captured individually."
echo "row format: R### | page | line | TYPE | verbatim value | context"
for f in numall ent fwd date qual; do echo; echo "## $f"; cat $W/$f.txt; done
} | awk -F'|' 'BEGIN{OFS=" | "} /^[0-9]+\|/{i++; printf "R%03d | page %s | line %s | %s | %s | %s\n", i,$1,$2,$3,$4,$5; next} {print}' > $S
grep -c '^R[0-9]' $S; sed -n 3,4p $S
echo $N $E $F $D $Q $T
