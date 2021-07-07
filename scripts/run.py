import sys                      # to parse command line argument
from pathlib import Path
from utility import *

dir_path = Path().absolute()

# start browser
# d1 = newdriver("chrome",dir_path)

# NCBI_ID for which you want to get count
NCBI_ID = sys.argv[1] if (len(sys.argv)>1) else "NR_026892.1"   

# get FASTA sequence for NCBI_ID
# seq = getseq(NCBI_ID)

# G count for single ID
# getGcount(d1,NCBI_ID)

# G count for multiple IDs
# IDs = "NR_149020.1, NR_130107.1".split(", ")
# IDs = "NR_026939.1, NR_026940.1, NR_026941.1, NR_034105.4".split(", ")
IDs = "NR_131948.1, NR_024049.1, NR_024050.1".split(", ")

# getGcountMultipleSel(d1,IDs)
for id in IDs:
    getGcountReq(id)