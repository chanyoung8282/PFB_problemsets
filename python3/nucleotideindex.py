#!/usr/bin/env python3
import sys
dna = sys.argv[1]
DNA = dna.upper()
print(f'nucleotide number 100 is {DNA[99]},number 200 is {DNA[199]}')
Gcount = DNA[100:201]
print(f'G count in 100 to 200 is {Gcount.count('G')}')
