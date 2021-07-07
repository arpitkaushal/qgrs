## 7 July 2021
One optimization we could do is store results for specific queries, and if they are asked again, we just retrieve them locally

√ Getting data just using requests Done

so if i want to work with requests, i need to get a few params that can later than give me the response I need for the `data view` of a sequence. 

```py
import requests as req
uri = 'https://bioinformatics.ramapo.edu/QGRS/dataview.php'
params = {'sq':'1','product':'0','id':'8fa7481fcf3a11126710fe9c6d0b9942','overlaps':'0'}
r = req.get(uri,params=params)
# r.url  = 'https://bioinformatics.ramapo.edu/QGRS/dataview.php?sq=1&product=0&id=8fa7481fcf3a11126710fe9c6d0b9942&overlaps=0'
# r.text = <html of the page, from which we just have to parse using bs4/xpath or something>
```

So, we need four parameters to access the data view, obviously one of them would be assigned after we make a POST request to the server via form @ 'https://bioinformatics.ramapo.edu/QGRS/analyze.php' giving the sequence, and other options we desire for the analysis of sequence. 

So, we need that response using request, get those params from response to our POST req of the form, and then make another GET req like mentioned in the above example. After that




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
