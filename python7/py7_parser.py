#!/usr/bin/env python3
import re
fastadict= {}
seq_id = ''
lines = ''
with open('Python_07.fasta', 'r') as seq_file_obj:
    for line in seq_file_obj:
        lines = line.rstrip()
        if re.findall(r"^>.*", line):
            seq_id = lines
            fastadict[seq_id] = ''
        else:
            fastadict[seq_id] += lines

print(fastadict)
   