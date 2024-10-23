#!/usr/bin/env python3
from Bio import SeqIO
filename = "seq.nt.fa"
for seq_record in SeqIO.parse(filename, "fasta"):
    type(seq_record)
    print(seq_record.seq)
    print(seq_record)
