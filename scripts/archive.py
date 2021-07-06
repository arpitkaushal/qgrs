for row in range(2,ipSheet.max_row):
    num_transcripts = ipSheet.cell(row,2).value
    total_pqs = ipSheet.cell(row,3).value
    g2 = ipSheet.cell(row,4).value
    g3 = ipSheet.cell(row,5).value
    g4 = ipSheet.cell(row,6).value
    ncbi_id = ipSheet.cell(row,7).value
    
    print(num_transcripts,total_pqs,g2,g3,g4,ncbi_id)