#!/usr/bin/env python3
import re
seq = ''
with open ('Python_07_ApoI.fasta.txt', 'r') as ApoI:
    for line in ApoI:
        if re.findall(r"^[ATGC].*", line):
            seq += line.rstrip()

for site in re.finditer(r"([AG])AATT([CT])", seq):
    print(site.group(0), site.start(1), site.end(2))

new_seq  = re.sub(r"([AG])AATT([CT])", r"\1^AATT^\2",seq)
#print(new_seq)
new_seq_split = new_seq.split("^")
#print(new_seq_split)
new_seq_split.sort(key=len,reverse=True)
print(new_seq_split)
#print(seq)
        