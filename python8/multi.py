#!/usr/bin/env python3
import sys
import re
fastadict ={}
seq_id = ''
nt_count={}

with open(sys.argv[1], 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if re.findall(r"^>\w", line):
            line = line.split()
            seq_id = line[0]
            fastadict[seq_id] = {'A':0,'T':0,'G':0,'C':0}
        else:
            for nt in line:
                if nt in fastadict[seq_id]:  
                    fastadict[seq_id][nt] += 1 
#print(fastadict)
for id in fastadict:
        print(f"seqs{fastadict} ")
        

#
# print(fastadict)
#print(seq_id)
#print(sequence)
#print(seq_id)