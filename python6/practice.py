#!/usr/bin/env python3
genes = {}
with open('Python_06.seq.txt','r') as seq_file_obj:
    for line in seq_file_obj:
        #line = line.rstrip()
        gene_id,seq = line.split()
        genes[gene_id] = seq
    #print(genes)

    for key in genes:
        #seq_write.write(f"{key}\t{genes.get(key)}\n")
        print(f""">{key}\t{genes.get(key):10}\n""")