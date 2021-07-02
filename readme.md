## 2 July  2021

### Challenge
Particularly Large sequences
		KM103369.1
		NC_001666.2

Script takes too long to process these, test once more. But it seems we need a better of handling large sequences, namely, get the API response into a file (roughly 139 kB for NC_001666.2) and then read it, and send to the portal. Our current method of `request.text` seems to be the bottleneck.


## 1 July 2021

Requirement

1. GUI on website as a tool.
	1. User should be able to enter an `NCBI ID` or `FASTA sequence` and get the following details
		1. Total PQS, 2g, 3g, 4g, 5g, 6g
		2. Segregated Tables for each of the above PQS
		3. Add an option to export tables?
	2. They should be able to set different parameters as given on QGRS Mapper
	
2. Backend handling - Github code, or WebScraping using Chrome? For webscraping we'll need a dedicated system to run at all times.
	1. Check github code with webscraping 
	

3. Excel sheet
	1. If given sheet in new format
		1. Beside the same rows, add output of the script for verification.
	2. If we remove brackets, can we modify old format of the sheet to new format  (with just 7 fields)?



# 10 June 2021
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
