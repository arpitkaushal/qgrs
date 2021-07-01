import sys                      # to parse command line argument
from pathlib import Path
from utility import *

dir_path = Path().absolute()

# start browser
d1 = newdriver("chrome",dir_path)

# NCBI_ID for which you want to get count
NCBI_ID = sys.argv[1] if (len(sys.argv)>1) else "NR_026892.1"   

# get FASTA sequence for NCBI_ID
# seq = getseq(NCBI_ID)

getGcount(d1,NCBI_ID)