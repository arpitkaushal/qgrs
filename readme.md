<!-- we can do this  -->

[the tool](https://bioinformatics.ramapo.edu/QGRS/analyze.php)

1. get the sequence from ncbi
2. set parameters for the sequence at qgrs
3. run analysis and select data view
4. will get a table in result 
   1. with first row as headers
   2. all rows following it have info "position, length, qgrrs, g-score"
   3. third colomn of each row, "qgrs" has the selected subseq (short for subsequence)
   4. they've underlined the number of "G"(s) considered for that subseq
   5. so we basically count the length of first substring enclosed between `<u>...</u>` tags to determine whether this result is a 2g,3g, or 4g
   6. do this for every row, count total sequences


hmm, so what are the challenges?
