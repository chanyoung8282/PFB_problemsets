#!/usr/bin/env python3

fastadict= {}
seq_id = ''
lines = ''
with open('Python_06.fasta', 'r') as seq_file_obj:
    for line in seq_file_obj:
        lines = line.rstrip()
        if line.startswith('>'):
            seq_id = lines[1:]
            fastadict[seq_id] = ''
        else:
            fastadict[seq_id] += lines

print(fastadict)
   
